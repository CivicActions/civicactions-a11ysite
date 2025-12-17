#!/usr/bin/env python3
"""
Remove former staff from public site listings:
- Find person pages by matching names
- Move person files to archive/people/
- Update about/people/index.md (and other listing files) to remove entries
Verbose progress is printed to the console.

Usage: python3 python/remove_staff.py
"""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
ARCHIVE_DIR = ROOT / 'archive' / 'people'
LISTING_CANDIDATES = [
    ROOT / 'about' / 'people' / 'index.md',
]

FORMER_STAFF = [
    'Jennifer Houde',
    'Michelle Kang',
    'Nira Datta',
    'Vanessa Luxen',
    'Allison Carroll',
]


def log(msg: str):
    print(msg, flush=True)


def name_to_slug(name: str) -> str:
    s = name.lower().strip()
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')


def find_person_files() -> list[Path]:
    people_dir = ROOT / 'about' / 'people'
    found = []
    if not people_dir.exists():
        log(f"[warn] People directory not found: {people_dir}")
        return found
    # candidate filenames like about/people/<slug>.md or about/people/<slug>/index.md
    for p in people_dir.rglob('*.md'):
        found.append(p)
    log(f"[scan] Found {len(found)} potential people files")
    return found


def file_matches_name(path: Path, name: str) -> bool:
    slug = name_to_slug(name)
    # check filename or parent dir
    rel = path.relative_to(ROOT)
    fn = rel.name.lower()
    parent = rel.parent.name.lower()
    if slug in fn or slug in parent:
        return True
    # check frontmatter/title
    try:
        txt = path.read_text(encoding='utf-8', errors='replace')
        for line in txt.splitlines():
            ls = line.strip().lower()
            if ls.startswith('title:') and name.lower() in line.lower():
                return True
    except Exception:
        pass
    return False


def ensure_archive_dir():
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)
    log(f"[archive] Using archive directory: {ARCHIVE_DIR}")


def move_to_archive(path: Path) -> Path:
    target = ARCHIVE_DIR / path.name
    # Avoid overwriting: add numeric suffix if needed
    i = 1
    base = target.stem
    ext = target.suffix
    while target.exists():
        target = ARCHIVE_DIR / f"{base}-{i}{ext}"
        i += 1
    path.rename(target)
    log(f"[move] {path.relative_to(ROOT)} -> {target.relative_to(ROOT)}")
    return target


def update_listings(names: list[str]):
    removed_total = 0
    for listing in LISTING_CANDIDATES:
        if not listing.exists():
            log(f"[list] Listing not found: {listing}")
            continue
        txt = listing.read_text(encoding='utf-8', errors='replace')
        orig_lines = txt.splitlines()
        new_lines = []
        removed_here = 0
        for line in orig_lines:
            keep = True
            for name in names:
                if name.lower() in line.lower():
                    keep = False
                    removed_here += 1
                    log(f"[list] Removing line with '{name}' from {listing.relative_to(ROOT)}")
                    break
            if keep:
                new_lines.append(line)
        if removed_here:
            listing.write_text('\n'.join(new_lines), encoding='utf-8')
            log(f"[list] Updated {listing.relative_to(ROOT)} (removed {removed_here} lines)")
            removed_total += removed_here
        else:
            log(f"[list] No matching lines to remove in {listing.relative_to(ROOT)}")
    log(f"[list] Total listing removals: {removed_total}")


def main():
    log("[start] Removing former staff from site listings")
    ensure_archive_dir()
    people_files = find_person_files()
    to_archive = []
    for name in FORMER_STAFF:
        matches = [p for p in people_files if file_matches_name(p, name)]
        if matches:
            log(f"[match] {name}: {len(matches)} file(s) matched")
            to_archive.extend(matches)
        else:
            log(f"[match] {name}: no files matched")

    archived = []
    for p in to_archive:
        archived.append(move_to_archive(p))
    log(f"[result] Archived {len(archived)} files")

    update_listings(FORMER_STAFF)
    log("[done] Staff removal process complete")


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        log(f"[error] {e}")
        sys.exit(1)
#!/usr/bin/env python3
"""Archive specified staff person pages and remove public listings.

Usage: python3 python/remove_staff.py
Modifies: moves person page files into `archive/people/` and removes simple list lines containing the name from `about/people/index.md` and any `about/people/*.md` files.
"""
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parents[1]
NAMES=['Jennifer Houde','Michelle Kang','Nira Datta','Vanessa Luxen','Allison Carroll']

def find_person_files(root,name):
    # name -> possible slugs
    slug=name.lower().replace(" ","-")
    candidates=[]
    # look for personas and about/people entries
    for p in root.rglob('about/people/**/*.md'):
        if any(part in ('node_modules','.git','_site','archive') for part in p.parts): continue
        txt=p.read_text(encoding='utf-8')
        if name in txt or slug in str(p):
            candidates.append(p)
    # also check top-level people files
    for p in root.rglob('**/*.md'):
        if '/people/' in str(p) and p.exists():
            txt=p.read_text(encoding='utf-8')
            if name in txt:
                candidates.append(p)
    return sorted(set(candidates))

def archive_files(files):
    arch=[]
    dest=ROOT/'archive'/'people'
    dest.mkdir(parents=True,exist_ok=True)
    for f in files:
        target=dest/f.name
        print(f'Moving {f} -> {target}')
        shutil.move(str(f),str(target))
        arch.append(target)
    return arch

def remove_name_from_listings(root,name):
    modified=[]
    for p in list(root.rglob('about/people/*.md')) + list(root.rglob('about/people/**/*.md')):
        if not p.exists(): continue
        txt=p.read_text(encoding='utf-8')
        lines=txt.splitlines()
        new=[]; changed=False
        for ln in lines:
            if name in ln and ('- ' in ln or '*' in ln or '<li>' in ln):
                print(f'Removing line from {p}: {ln}')
                changed=True
                continue
            new.append(ln)
        if changed:
            p.write_text('\n'.join(new)+"\n",encoding='utf-8')
            modified.append(p)
    return modified

def main():
    all_arch=[]; all_mod=[]
    for name in NAMES:
        print('Processing',name)
        files=find_person_files(ROOT,name)
        if not files:
            print('  No person page files found for',name)
        else:
            arch=archive_files(files)
            all_arch.extend(arch)
        mod=remove_name_from_listings(ROOT,name)
        all_mod.extend(mod)
    print('\nArchived files:')
    for a in all_arch: print(' -',a.relative_to(ROOT))
    print('\nModified listings:')
    for m in all_mod: print(' -',m.relative_to(ROOT))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
#!/usr/bin/env python3
"""Archive person pages and remove staff names from public listings.
Usage: python3 python/remove_staff.py
"""
from pathlib import Path
import shutil

ROOT=Path(__file__).resolve().parents[1]
names=[
    'Jennifer Houde',
    'Michelle Kang',
    'Nira Datta',
    'Vanessa Luxen',
    'Allison Carroll'
]

def slug(name):
    return name.lower().replace(' ','-')

def find_person_files(root, name):
    s=slug(name)
    candidates=[]
    # common locations
    md=root/'personas' # intentionally check personas too
    # primary people folder
    for p in root.rglob('about/people/**/*.md'):
        if any(part in ('node_modules','.git','_site','archive') for part in p.parts): continue
        txt=p.read_text(encoding='utf-8')
        if name in txt or s in str(p).lower():
            candidates.append(p)
    # root people files
    for p in root.rglob('**/*.md'):
        if '/about/people/' in str(p) and p not in candidates:
            txt=p.read_text(encoding='utf-8')
            if name in txt or s in str(p).lower():
                candidates.append(p)
    return candidates

def archive_files(files, root):
    arcroot=root/'archive'/'people'
    arcroot.mkdir(parents=True,exist_ok=True)
    moved=[]
    for p in files:
        target=arcroot/p.name
        p.rename(target)
        moved.append(target)
    return moved

def remove_from_listings(root, name):
    # remove lines containing the name from about/people/index.md and any about/* people listing files
    changed_files=[]
    for p in (root/'about').rglob('**/*.md'):
        if any(part in ('node_modules','.git','_site','archive') for part in p.parts): continue
        txt=p.read_text(encoding='utf-8')
        lines=txt.splitlines()
        new=[]
        removed=False
        for line in lines:
            if name in line:
                removed=True
                continue
            new.append(line)
        if removed:
            p.write_text('\n'.join(new)+"\n",encoding='utf-8')
            changed_files.append(p)
    return changed_files

def main():
    root=ROOT
    all_moved=[]
    all_changed=[]
    for name in names:
        print('Processing',name)
        files=find_person_files(root,name)
        if not files:
            print('  no person page files found for',name)
        else:
            for f in files: print('  will archive',f)
            moved=archive_files(files,root)
            for m in moved: print('  moved ->',m)
            all_moved.extend(moved)
        changed=remove_from_listings(root,name)
        if changed:
            for c in changed: print('  removed listing line from',c)
            all_changed.extend(changed)
        else:
            print('  no listing files needed edits for',name)
    print('\nSummary: moved',len(all_moved),'files, edited',len(all_changed),'files')
    if all_moved:
        print('Moved files:')
        for m in all_moved: print(' -',m.relative_to(ROOT))
    return 0

if __name__=='__main__':
    raise SystemExit(main())
