#!/usr/bin/env python3
"""
Migrate rich Markdown content from an `old-site/` checkout into the new repo pages,
replacing only the body content while preserving existing frontmatter and
adding migration notes. Prints progress continuously.

Assumptions:
- The `old-site/` directory is located at `<root>/old-site` and contains
  Markdown files whose paths broadly match current site paths (e.g., guide/, playbook/, posts/).
- We use `migrated_stubs_log.csv` to know which repo files were auto-filled
  from live HTML and need richer Markdown from the old site.

Usage:
  python3 python/migrate_from_old_site.py --root /Users/mgifford/civicactions-a11ysite

Outputs:
- Console logs per file with found/not found status.
- Updates target files’ body content with Markdown from old-site when available.
"""
import argparse
import csv
import re
from pathlib import Path
import time


def split_frontmatter(text: str):
    text = text.replace('\r\n', '\n')
    if text.strip().startswith('---'):
        parts = text.split('---')
        if len(parts) >= 3:
            fm = parts[1]
            body = '---'.join(parts[2:])
            return ('---\n' + fm + '---\n', body)
    return ('', text)


def detect_title(text: str) -> str:
    # Try frontmatter title
    m = re.search(r'^title\s*:\s*\"?([^\n\"]+)\"?', text, flags=re.M)
    if m:
        return m.group(1).strip()
    # Fallback H1
    m = re.search(r'^#\s+([^\n]+)', text, flags=re.M)
    return m.group(1).strip() if m else ''


def add_migration_notes_to_frontmatter(fm: str, note: str):
    fm_content = fm.replace('---', '')
    lines = [ln for ln in fm_content.strip().splitlines() if ln.strip()]
    ts = time.strftime('%Y-%m-%d')
    # Remove any existing migration_notes/editor_notes to avoid duplicates
    lines = [ln for ln in lines if not ln.lower().startswith('migration_notes:') and not ln.lower().startswith('editor_notes:')]
    lines.append(f"migration_notes: \"Migrated Markdown from old-site on {ts}.\"")
    if note:
        safe_note = note.replace('\n', ' ').replace('"', '\\"')
        lines.append(f"editor_notes: \"{safe_note}\"")
    new_fm = '---\n' + '\n'.join(lines) + '\n---\n'
    return new_fm


def probable_old_paths(repo_rel: str) -> list[str]:
    # Try direct mapping and common folder adjustments
    candidates = []
    # Direct
    candidates.append(repo_rel)
    # posts mapping (about/news -> posts)
    if repo_rel.startswith('about/news/'):
        candidates.append(repo_rel.replace('about/news/', 'posts/'))
    # guide
    if repo_rel.startswith('guide/'):
        candidates.append(repo_rel)
    # playbook
    if repo_rel.startswith('playbook/'):
        candidates.append(repo_rel)
    # projects
    if repo_rel.startswith('projects/'):
        candidates.append(repo_rel)
    # roles
    if repo_rel.startswith('roles/'):
        candidates.append(repo_rel)
    # top-level
    if '/' not in repo_rel:
        candidates.append(repo_rel)
    # index.md variants
    if repo_rel.endswith('.md'):
        base = repo_rel[:-3]
        candidates.append(base + '/index.md')
    return list(dict.fromkeys(candidates))

from typing import Optional

def find_old_file(old_root: Path, repo_rel: str) -> Optional[Path]:
    # Try direct candidates
    for c in probable_old_paths(repo_rel):
        p = old_root / c
        if p.exists():
            return p
    # Try by filename match anywhere
    name = Path(repo_rel).name
    for p in old_root.rglob(name):
        if p.is_file():
            return p
    # Try by stem match (e.g., personalization.md -> any *personalization*.md)
    stem = Path(repo_rel).stem
    matches = [p for p in old_root.rglob('*.md') if stem.lower() in p.stem.lower()]
    if matches:
        return matches[0]
    # Try known legacy folders
    legacy_folders = ['_guide', '_playbook', '_people', '_projects', '_posts', 'pages', '_pages']
    for folder in legacy_folders:
        cand = old_root / folder / name
        if cand.exists():
            return cand
        # also index.md under folder/stem
        cand2 = old_root / folder / stem / 'index.md'
        if cand2.exists():
            return cand2
    return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--root', required=True)
    args = ap.parse_args()
    root = Path(args.root)
    old = root / 'old-site'
    log = root / 'migrated_stubs_log.csv'

    if not old.exists():
        print(f"[old-site] Not found: {old}. Aborting.")
        return
    if not log.exists():
        print(f"[log] Not found: {log}. Aborting.")
        return

    rows = list(csv.DictReader(log.open(encoding='utf-8')))
    print(f"[migrate] Migrating Markdown from old-site for {len(rows)} entries")
    migrated = 0
    missing = 0

    for r in rows:
        repo_file = r.get('repo_file', '').strip()
        src_url = r.get('source_url', '').strip()
        if not repo_file:
            continue
        target = root / repo_file
        if not target.exists():
            print(f"[skip] Missing target {repo_file}")
            continue

        # Build candidate old-site paths
        found_old = find_old_file(old, repo_file)
        if not found_old:
            print(f"[miss] No old-site match for {repo_file}.")
            missing += 1
            continue

        # Read contents
        try:
            new_text = target.read_text(encoding='utf-8')
            fm, body = split_frontmatter(new_text)
        except Exception:
            fm, body = ('', '')
            new_text = ''

        try:
            old_text = found_old.read_text(encoding='utf-8')
        except Exception:
            print(f"[error] Could not read {found_old}")
            missing += 1
            continue

        # Split old frontmatter + body; prefer old body only
        old_fm, old_body = split_frontmatter(old_text)
        if not old_body.strip():
            # if old has no body, fallback to whole
            old_body = old_text

        # Keep existing frontmatter, append migration notes
        title = detect_title(fm or new_text)
        note = f"Source: {src_url}" if src_url else ''
        fm_updated = add_migration_notes_to_frontmatter(fm or '---\n---\n', note)
        merged = fm_updated + '\n' + old_body.strip() + '\n'
        target.write_text(merged, encoding='utf-8')
        migrated += 1
        print(f"[ok] Replaced body from old-site: {repo_file} <- {found_old}")

    print(f"[done] Migrated: {migrated}; Missing old match: {missing}")


if __name__ == '__main__':
    main()
