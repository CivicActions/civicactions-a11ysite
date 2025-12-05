#!/usr/bin/env python3
"""
Verbose site crawl + plan compare + optional stub migration.

Outputs progress continuously so you can see activity in the console.

Artifacts:
- live_vs_plan_report.csv: link -> in_plan, repo_exists, repo_file
- migrated_stubs_log.csv: records stub pages auto-filled from live content

Usage:
  python3 python/crawl_compare_and_migrate.py --base https://accessibility.civicactions.com \
      --root /Users/mgifford/civicactions-a11ysite \
      --migrate-stubs

Flags:
  --base            Base URL to crawl
  --root            Repo root path
  --max-pages N     Limit pages crawled (default 300)
  --migrate-stubs   If set, replace stub markdown content with fetched live HTML converted

Notes:
- This script prints progress for every request and comparison.
- If plan CSVs contain editorial text in the destination column, the matching may require manual review.
"""
import argparse
import csv
import re
import sys
import time
from collections import deque
from pathlib import Path
from html.parser import HTMLParser
from urllib.parse import urljoin, urlparse

try:
    import requests
except Exception:
    print("ERROR: Python 'requests' package is required. Install with: pip install requests", flush=True)
    sys.exit(1)


class LinkExtractor(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        href = dict(attrs).get('href')
        if href:
            self.links.append(href)


def normalize_path(href: str, base_host: str) -> str:
    if not href:
        return ''
    href = href.strip()
    if href.startswith(('mailto:', 'tel:', 'javascript:', '#')):
        return ''
    # strip absolute
    href = re.sub(r'https?://[^/]+', '', href)
    if not href.startswith('/'):
        href = '/' + href
    href = href.split('?')[0].split('#')[0]
    if href.endswith('/') and href != '/':
        href = href.rstrip('/')
    return href


def load_plan_destinations(plan_dir: Path):
    print(f"[plan] Loading plan CSVs from {plan_dir}", flush=True)
    plan_files = [
        plan_dir / 'Content redesign of accessibility.civicactions.com - 🗺️ Content plan.csv',
        plan_dir / 'Content redesign of accessibility.civicactions.com - 🛠️ Restructure plan.csv',
        plan_dir / 'Content redesign of accessibility.civicactions.com - Content audit.csv',
    ]
    planned = set()
    notes_map = {}
    for pf in plan_files:
        if not pf.exists():
            print(f"[plan] Skipping missing {pf}", flush=True)
            continue
        print(f"[plan] Reading {pf}", flush=True)
        try:
            with pf.open(newline='', encoding='utf-8') as f:
                r = csv.DictReader(f)
                # detect likely destination and notes columns
                dest_key = None
                notes_key = None
                for c in r.fieldnames or []:
                    lc = c.lower()
                    if 'destination url' in lc or lc == 'destination' or 'new url' in lc or lc == 'url' or 'path' in lc:
                        dest_key = c
                    if 'notes' in lc or 'migration note' in lc or 'editor notes' in lc:
                        notes_key = c
                for row in r:
                    val = row.get(dest_key, '') if dest_key else ''
                    if not val:
                        continue
                    n = re.sub(r'https?://[^/]+', '', val).split('?')[0].split('#')[0]
                    if not n.startswith('/'):
                        n = '/' + n
                    if n.endswith('/') and n != '/':
                        n = n.rstrip('/')
                    planned.add(n)
                    note_val = row.get(notes_key, '') if notes_key else ''
                    if note_val:
                        notes_map[n] = note_val
        except Exception as e:
            print(f"[plan] ERROR reading {pf}: {e}", flush=True)
    # redirects plan optional
    redir = plan_dir.parent / 'redirects-plan.txt'
    if redir.exists():
        print(f"[plan] Reading redirects {redir}", flush=True)
        for ln in redir.read_text(encoding='utf-8').splitlines():
            ln = ln.strip()
            if not ln or ln.startswith('#'):
                continue
            parts = ln.split()
            if len(parts) >= 2:
                dst = parts[1]
                dst = re.sub(r'https?://[^/]+', '', dst).split('?')[0].split('#')[0]
                if not dst.startswith('/'):
                    dst = '/' + dst
                if dst.endswith('/') and dst != '/':
                    dst = dst.rstrip('/')
                planned.add(dst)
    print(f"[plan] Destinations loaded: {len(planned)}", flush=True)
    return planned, notes_map


def repo_file_for(root: Path, path: str) -> str:
    p1 = root / (path.lstrip('/') + '.md')
    if p1.exists():
        return str(p1.relative_to(root))
    p2 = root / path.lstrip('/')
    if (p2 / 'index.md').exists():
        return str((p2 / 'index.md').relative_to(root))
    return ''


def is_stub(md_text: str) -> bool:
    # naive heuristics: very short body or contains 'Placeholder'
    body = md_text.split('---')[-1].strip() if '---' in md_text else md_text.strip()
    return ('Placeholder' in body) or (len(body) < 120)


def html_to_markdown_fallback(html: str) -> str:
    # very minimal fallback: strip tags, keep text
    # Prefer external converter like html2text if available, but avoid dependency.
    text = re.sub(r'<script[\s\S]*?</script>', '', html, flags=re.I)
    text = re.sub(r'<style[\s\S]*?</style>', '', text, flags=re.I)
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+\n', '\n', text)
    return text.strip()


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--base', required=True, help='Base URL to crawl')
    ap.add_argument('--root', required=True, help='Repo root path')
    ap.add_argument('--max-pages', type=int, default=300)
    ap.add_argument('--migrate-stubs', action='store_true')
    args = ap.parse_args()

    base = args.base.rstrip('/') + '/'
    root = Path(args.root)
    plan_dir = root / 'migration_plan'

    base_host = urlparse(base).netloc
    print(f"[crawl] Starting crawl at {base} (host {base_host}), max_pages={args.max_pages}", flush=True)

    planned, notes_map = load_plan_destinations(plan_dir)

    seen = set()
    q = deque(['/'])
    all_links = set()

    report_path = root / 'live_vs_plan_report.csv'
    migrate_log = root / 'migrated_stubs_log.csv'
    with report_path.open('w', newline='', encoding='utf-8') as rf:
        writer = csv.DictWriter(rf, fieldnames=['link', 'status', 'in_plan', 'repo_exists', 'repo_file'])
        writer.writeheader()

        crawled_count = 0
        while q and crawled_count < args.max_pages:
            path = q.popleft()
            if path in seen:
                continue
            seen.add(path)
            url = urljoin(base, path)
            print(f"[crawl] GET {url}", flush=True)
            try:
                resp = requests.get(url, timeout=15)
                status = resp.status_code
                print(f"[crawl] {status} {url}", flush=True)
                html = resp.text
            except Exception as e:
                print(f"[crawl] ERROR fetching {url}: {e}", flush=True)
                writer.writerow({'link': path, 'status': 'error', 'in_plan': False, 'repo_exists': False, 'repo_file': ''})
                continue

            crawled_count += 1
            # extract and enqueue links
            le = LinkExtractor()
            try:
                le.feed(html)
            except Exception:
                pass
            for href in le.links:
                norm = normalize_path(href, base_host)
                if not norm:
                    continue
                all_links.add(norm)
                if norm not in seen:
                    q.append(norm)

            # compare current path
            in_plan = path in planned
            repo_file = repo_file_for(root, path)
            repo_exists = bool(repo_file)
            writer.writerow({'link': path, 'status': status, 'in_plan': in_plan, 'repo_exists': repo_exists, 'repo_file': repo_file})
            print(f"[compare] path={path} in_plan={in_plan} repo_exists={repo_exists} file={repo_file}", flush=True)

            # optional migration: if repo file exists and looks like a stub, replace content from live
            if args.migrate_stubs and repo_exists:
                md_path = root / repo_file
                try:
                    md_text = md_path.read_text(encoding='utf-8')
                    if is_stub(md_text):
                        print(f"[migrate] Replacing stub content in {repo_file} from {url}", flush=True)
                        body_md = html_to_markdown_fallback(html)
                        # preserve frontmatter if present
                        if md_text.strip().startswith('---'):
                            parts = md_text.split('---')
                            fm_content = parts[1] if len(parts) > 2 else "\n"
                            # add migration notes into frontmatter
                            migration_note = notes_map.get(path, '').strip()
                            timestamp = time.strftime('%Y-%m-%d')
                            fm_lines = fm_content.strip().splitlines()
                            # ensure we have a newline-terminated fm
                            if fm_lines and fm_lines[-1].strip() == '':
                                fm_lines = fm_lines[:-1]
                            fm_lines.append(f"migration_notes: \"Auto-migrated from live on {timestamp}.\"")
                            if migration_note:
                                # append editor/migration notes from plan
                                safe_note = migration_note.replace('\n', ' ').replace('"', '\\"')
                                fm_lines.append(f"editor_notes: \"{safe_note}\"")
                            fm = '---\n' + '\n'.join(fm_lines) + '\n---\n\n'
                            new_text = fm + body_md + "\n"
                        else:
                            timestamp = time.strftime('%Y-%m-%d')
                            migration_note = notes_map.get(path, '').strip()
                            fm_lines = [f"title: \"\"", f"migration_notes: \"Auto-migrated from live on {timestamp}.\""]
                            if migration_note:
                                safe_note = migration_note.replace('\n', ' ').replace('"', '\\"')
                                fm_lines.append(f"editor_notes: \"{safe_note}\"")
                            fm = '---\n' + '\n'.join(fm_lines) + '\n---\n\n'
                            new_text = fm + body_md + "\n"
                        md_path.write_text(new_text, encoding='utf-8')
                        # log migration
                        with migrate_log.open('a', newline='', encoding='utf-8') as mf:
                            mw = csv.DictWriter(mf, fieldnames=['repo_file', 'source_url', 'timestamp'])
                            if mf.tell() == 0:
                                mw.writeheader()
                            mw.writerow({'repo_file': repo_file, 'source_url': url, 'timestamp': time.strftime('%Y-%m-%d %H:%M:%S')})
                except Exception as e:
                    print(f"[migrate] ERROR updating {repo_file}: {e}", flush=True)

    # After crawl, compare accumulated links to plan and repo presence
    print(f"[summary] Crawled pages: {len(seen)}; Unique links found: {len(all_links)}", flush=True)
    print(f"[summary] Writing consolidated comparison to {report_path}", flush=True)
    # Already wrote per-page; also ensure each discovered link row exists
    with report_path.open('a', newline='', encoding='utf-8') as rf:
        writer = csv.DictWriter(rf, fieldnames=['link', 'status', 'in_plan', 'repo_exists', 'repo_file'])
        for l in sorted(all_links):
            in_plan = l in planned
            rfpath = repo_file_for(root, l)
            writer.writerow({'link': l, 'status': '', 'in_plan': in_plan, 'repo_exists': bool(rfpath), 'repo_file': rfpath})
            print(f"[links] link={l} in_plan={in_plan} repo_exists={bool(rfpath)} file={rfpath}", flush=True)

    print("[done] live_vs_plan_report.csv written; see console for detailed progress.", flush=True)


if __name__ == '__main__':
    main()
