#!/usr/bin/env python3
"""
Add minimal eleventyNavigation frontmatter to pages missing it.

Sources missing list from migrated_stubs_log.csv (or scans the repo if needed).
Heuristics for parent/keys:
- guide/* -> parent "Guide"
- playbook/* -> parent "Playbook"
- projects/* -> parent "Projects"
- roles/* -> parent "Roles"
- Top-level files -> no parent, key from title or filename

Usage:
  python3 python/add_eleventy_navigation.py --root /Users/mgifford/civicactions-a11ysite
"""
import argparse
import csv
import re
from pathlib import Path
from typing import Optional


def detect_title(text: str) -> str:
    if text.strip().startswith('---'):
        # try to read title: ...
        m = re.search(r'^title\s*:\s*\"?([^\n\"]+)\"?', text, flags=re.M)
        if m:
            return m.group(1).strip()
    # fallback: first H1
    m = re.search(r'^#\s+([^\n]+)', text, flags=re.M)
    return m.group(1).strip() if m else ''


def insert_nav(text: str, parent: Optional[str], key: Optional[str]) -> str:
    lines = []
    if text.strip().startswith('---'):
        parts = text.split('---')
        fm = parts[1]
        body = '---'.join(parts[2:])
        fm_lines = fm.strip().splitlines()
        # remove any existing eleventyNavigation
        fm_lines = [ln for ln in fm_lines if not ln.lower().startswith('eleventynavigation')]
        fm_lines.append('eleventyNavigation:')
        if key:
            fm_lines.append(f"  key: \"{key}\"")
        if parent:
            fm_lines.append(f"  parent: \"{parent}\"")
        new_fm = '---\n' + '\n'.join(fm_lines) + '\n---\n'
        return new_fm + body
    else:
        # create frontmatter
        title = detect_title(text) or (key or '').replace('-', ' ').title()
        fm_lines = [f'title: "{title}"', 'eleventyNavigation:']
        if key:
            fm_lines.append(f"  key: \"{key}\"")
        if parent:
            fm_lines.append(f"  parent: \"{parent}\"")
        fm = '---\n' + '\n'.join(fm_lines) + '\n---\n\n'
        return fm + text


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    ap.add_argument('--scan-all', action='store_true', help='Ignore migrated log and scan the whole repo')
    args = ap.parse_args()
    root = Path(args.root)

    log = root / 'migrated_stubs_log.csv'
    candidates: list[Path] = []
    skip_names = {"LICENSE.md", "README.md", "SECURITY.md"}
    skip_paths = {Path('.config/remark/README.md')}

    if log.exists() and not args.scan_all:
        rows = list(csv.DictReader(log.open(encoding='utf-8')))
        for r in rows:
            f = r.get('repo_file', '')
            if not f:
                continue
            p = root / f
            if not p.exists():
                continue
            if p.name in skip_names or p.relative_to(root) in skip_paths:
                continue
            txt = p.read_text(encoding='utf-8', errors='ignore')
            has_fm = txt.strip().startswith('---')
            has_nav = False
            if has_fm:
                m = re.search(r'^eleventyNavigation\s*:', txt, flags=re.M|re.I)
                has_nav = bool(m)
            if not has_nav:
                candidates.append(p)
    else:
        # fallback: scan repo for markdown missing nav
        for p in root.rglob('*.md'):
            if any(part in ('node_modules', '.git', '_site', 'archive') for part in p.parts):
                continue
            if p.name in skip_names or p.relative_to(root) in skip_paths:
                continue
            txt = p.read_text(encoding='utf-8', errors='ignore')
            has_fm = txt.strip().startswith('---')
            has_nav = False
            if has_fm:
                m = re.search(r'^eleventyNavigation\s*:', txt, flags=re.M|re.I)
                has_nav = bool(m)
            if not has_nav:
                candidates.append(p)

    print(f"[nav] Candidates missing eleventyNavigation: {len(candidates)}")
    updated = 0
    for p in candidates:
        rel = p.relative_to(root)
        rel_str = str(rel)
        parent = None
        key = None
        parts = rel.parts
        if parts[0] == 'guide':
            parent = 'Guide'
            key = Path(rel_str).stem.replace('index', 'Guide').replace('-', ' ').title()
        elif parts[0] == 'playbook':
            parent = 'Playbook'
            key = Path(rel_str).stem.replace('index', 'Playbook').replace('-', ' ').title()
        elif parts[0] == 'projects':
            parent = 'Projects'
            key = Path(rel_str).stem.replace('-', ' ').title()
        elif parts[0] == 'roles':
            parent = 'Roles'
            key = Path(rel_str).stem.replace('index', 'Roles').replace('-', ' ').title()
        else:
            key = Path(rel_str).stem.replace('-', ' ').title()

        txt = p.read_text(encoding='utf-8', errors='ignore')
        new_txt = insert_nav(txt, parent, key)
        if new_txt != txt:
            p.write_text(new_txt, encoding='utf-8')
            updated += 1
            print(f"[nav] Updated {rel_str} parent={parent} key={key}")

    print(f"[nav] Done. Updated {updated} files.")


if __name__ == '__main__':
    main()
