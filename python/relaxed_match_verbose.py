#!/usr/bin/env python3
"""
Verbose relaxed matching: extracts links from the live homepage HTML previously fetched
to /tmp/accessibility_home.html, compares to migration CSVs and local repo files using
slug + fuzzy matching, prints progress per step, and writes live_vs_plan_relaxed.csv.

Usage: python3 python/relaxed_match_verbose.py
"""
import csv
import re
import sys
from pathlib import Path
from html.parser import HTMLParser
from difflib import SequenceMatcher
import unicodedata

ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = Path('/tmp/accessibility_home.html')
OUT_CSV = ROOT / 'live_vs_plan_relaxed.csv'


def log(msg: str):
    print(msg, flush=True)


def read_homepage_html() -> str:
    if not HTML_PATH.exists():
        raise FileNotFoundError(f"Homepage HTML not found at {HTML_PATH}. Fetch it via: curl -sSf 'https://accessibility.civicactions.com/' -o {HTML_PATH}")
    log(f"[load] Reading homepage HTML from {HTML_PATH}")
    return HTML_PATH.read_text(encoding='utf-8', errors='replace')


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []
    def handle_starttag(self, tag, attrs):
        if tag != 'a':
            return
        href = dict(attrs).get('href')
        if href:
            self.links.append(href)


def normalize_href(h: str) -> str:
    h = (h or '').strip()
    if not h:
        return ''
    if h.startswith(('mailto:', 'tel:', 'javascript:')):
        return ''
    h = re.sub(r'https?://[^/]+', '', h)
    if not h.startswith('/'):
        h = '/' + h
    h = h.split('?')[0].split('#')[0]
    if h.endswith('/') and h != '/':
        h = h.rstrip('/')
    return h


def extract_links(html: str) -> list[str]:
    log("[parse] Extracting <a> links from homepage HTML…")
    p = LinkParser()
    p.feed(html)
    raw = set(p.links)
    links = []
    for href in sorted(raw):
        nh = normalize_href(href)
        if nh:
            links.append(nh)
    log(f"[parse] Found {len(links)} normalized homepage links")
    return links


def slug(s: str) -> str:
    s = unicodedata.normalize('NFKD', (s or '')).lower()
    s = re.sub(r'https?://[^/]+', '', s)
    s = re.sub(r'[^a-z0-9]+', '-', s)
    return s.strip('-')


def load_plan_rows() -> list[dict]:
    plan_files = [
        ROOT / 'migration_plan' / 'Content redesign of accessibility.civicactions.com - 🗺️ Content plan.csv',
        ROOT / 'migration_plan' / 'Content redesign of accessibility.civicactions.com - 🛠️ Restructure plan.csv',
        ROOT / 'migration_plan' / 'Content redesign of accessibility.civicactions.com - Content audit.csv',
    ]
    plans = []
    for pf in plan_files:
        if not pf.exists():
            log(f"[plan] Skipping missing CSV: {pf}")
            continue
        log(f"[plan] Reading: {pf}")
        with pf.open(newline='') as f:
            r = csv.DictReader(f)
            dest = None
            title = None
            for c in r.fieldnames:
                lc = c.lower()
                if dest is None and (('destination' in lc) or ('new url' in lc) or (lc == 'url') or ('path' in lc)):
                    dest = c
                if title is None and (('title' in lc) or ('page title' in lc) or (lc == 'name')):
                    title = c
            log(f"[plan] Columns detected -> dest: {dest}, title: {title}")
            count = 0
            for row in r:
                dst = row.get(dest, '') if dest else ''
                t = row.get(title, '') if title else ''
                if dst:
                    n = re.sub(r'https?://[^/]+', '', dst).split('?')[0].split('#')[0]
                    if not n.startswith('/'):
                        n = '/' + n
                    if n.endswith('/') and n != '/':
                        n = n.rstrip('/')
                    plans.append({'dest': n, 'title': t, 'row': row, 'source': pf.name})
                    count += 1
            log(f"[plan] Rows added from {pf}: {count}")
    log(f"[plan] Total plan destinations loaded: {len(plans)}")
    return plans


def load_repo_files() -> list[dict]:
    log("[repo] Scanning repository for .md files…")
    repo_files = []
    skipped_dirs = {'node_modules', '.git', '_site', 'archive'}
    for p in ROOT.rglob('*.md'):
        if any(part in skipped_dirs for part in p.parts):
            continue
        rel = '/' + str(p.relative_to(ROOT)).replace('index.md', '').replace('.md', '')
        rel = re.sub(r'//+', '/', rel)
        if rel.endswith('/') and rel != '/':
            rel = rel.rstrip('/')
        title = ''
        try:
            txt = p.read_text(encoding='utf-8', errors='replace')
            # Simple frontmatter title line detection
            for line in txt.splitlines():
                ls = line.strip().lower()
                if ls.startswith('title:'):
                    title = line.split(':', 1)[1].strip().strip('"')
                    break
        except Exception as e:
            log(f"[repo] Warning: failed reading {p}: {e}")
        repo_files.append({'path': rel, 'file': str(p.relative_to(ROOT)), 'title': title})
    log(f"[repo] Repo files indexed: {len(repo_files)}")
    return repo_files


def best_match(target_slug: str, candidates: list[dict], key: str) -> tuple[str, float, dict]:
    best_val = ''
    best_score = 0.0
    best_row = {}
    for c in candidates:
        s = slug(c.get(key, '') or c.get('title', ''))
        score = SequenceMatcher(None, target_slug, s).ratio()
        if score > best_score:
            best_score = score
            best_val = c.get(key, '')
            best_row = c
    return best_val, best_score, best_row


def main():
    try:
        html = read_homepage_html()
    except FileNotFoundError as e:
        log(f"[error] {e}")
        log("[hint] Fetch homepage HTML:")
        log(f"curl -sSf 'https://accessibility.civicactions.com/' -o {HTML_PATH}")
        sys.exit(1)

    links = extract_links(html)
    plans = load_plan_rows()
    repo_files = load_repo_files()

    if not links:
        log("[warn] No links extracted; aborting")
        sys.exit(1)

    log(f"[match] Starting relaxed matching for {len(links)} links…")
    with OUT_CSV.open('w', newline='', encoding='utf-8') as f:
        w = csv.DictWriter(
            f,
            fieldnames=['link', 'best_plan_dest', 'plan_title', 'plan_source', 'plan_score', 'best_repo_path', 'repo_file', 'repo_score'],
        )
        w.writeheader()
        for i, l in enumerate(links, 1):
            lslug = slug(l)
            plan_val, plan_score, plan_row = best_match(lslug, plans, 'dest')
            repo_val, repo_score, repo_row = best_match(lslug, repo_files, 'path')
            w.writerow({
                'link': l,
                'best_plan_dest': plan_val,
                'plan_title': plan_row.get('title', ''),
                'plan_source': plan_row.get('source', ''),
                'plan_score': round(plan_score, 3),
                'best_repo_path': repo_val,
                'repo_file': repo_row.get('file', ''),
                'repo_score': round(repo_score, 3),
            })
            log(f"[match] {i}/{len(links)} link='{l}' plan='{plan_val}' (score={plan_score:.3f}) repo='{repo_val}' (score={repo_score:.3f})")

    log(f"[done] Wrote {OUT_CSV}")


if __name__ == '__main__':
    main()
#!/usr/bin/env python3
"""Verbose relaxed matcher: extracts homepage links and matches them to plan rows and repo files.

Usage: python3 python/relaxed_match_verbose.py
Writes: live_vs_plan_relaxed.csv at repo root and prints per-link progress.
"""
from pathlib import Path
import csv, re, sys
from difflib import SequenceMatcher
import unicodedata

ROOT=Path(__file__).resolve().parents[1]
HTML_TMP='/tmp/accessibility_home.html'

def extract_links(html_path):
    from html.parser import HTMLParser
    class P(HTMLParser):
        def __init__(self):
            super().__init__(); self.links=[]
        def handle_starttag(self,tag,attrs):
            if tag!='a': return
            href=dict(attrs).get('href')
            if href: self.links.append(href)
    txt=Path(html_path).read_text(encoding='utf-8')
    p=P(); p.feed(txt)
    links=set()
    for href in set(p.links):
        if not href: continue
        href=href.strip()
        if href.startswith(('mailto:','tel:','javascript:')): continue
        href=re.sub(r'https?://[^/]+','',href)
        if not href.startswith('/'): href='/' + href
        href=href.split('?')[0].split('#')[0]
        if href.endswith('/') and href!='/': href=href.rstrip('/')
        links.add(href)
    return sorted(links)

def slug(s):
    s=(s or '')
    s=unicodedata.normalize('NFKD',s).lower()
    s=re.sub(r'https?://[^/]+','',s)
    s=re.sub(r'[^a-z0-9]+','-',s)
    return s.strip('-')

def load_plans(root):
    plan_files=[root/'migration_plan'/'Content redesign of accessibility.civicactions.com - 🗺️ Content plan.csv',
                root/'migration_plan'/'Content redesign of accessibility.civicactions.com - 🛠️ Restructure plan.csv',
                root/'migration_plan'/'Content redesign of accessibility.civicactions.com - Content audit.csv']
    plans=[]
    for pf in plan_files:
        if not pf.exists(): continue
        print(f'Loading plan rows from {pf.name}')
        with pf.open(newline='') as f:
            r=csv.DictReader(f)
            dest=None; title=None
            for c in r.fieldnames:
                lc=c.lower()
                if not dest and ('destination' in lc or 'url' in lc or 'new url' in lc or 'path' in lc): dest=c
                if not title and ('title' in lc or 'page title' in lc or 'name' in lc): title=c
            for row in r:
                dst=row.get(dest,'') if dest else ''
                t=row.get(title,'') if title else ''
                if dst:
                    n=re.sub(r'https?://[^/]+','',dst).split('?')[0].split('#')[0]
                    if not n.startswith('/'): n='/' + n
                    if n.endswith('/') and n!='/': n=n.rstrip('/')
                    plans.append({'dest':n,'title':t,'row':row,'source':pf.name,'slug':slug(n or t)})
    print(f'Loaded {len(plans)} planned destinations')
    return plans

def load_repo_files(root):
    repo_files=[]
    for p in root.rglob('*.md'):
        if any(part in ('node_modules','.git','_site','archive') for part in p.parts): continue
        rel='/' + str(p.relative_to(root)).replace('index.md','').replace('.md','')
        rel=re.sub(r'//+','/',rel)
        if rel.endswith('/') and rel!='/': rel=rel.rstrip('/')
        title=''
        try:
            txt=p.read_text(encoding='utf-8')
            for line in txt.splitlines():
                if line.strip().lower().startswith('title:'):
                    title=line.split(':',1)[1].strip().strip(' "')
                    break
        except Exception:
            pass
        repo_files.append({'path':rel,'file':str(p.relative_to(root)),'title':title,'slug':slug(rel or title)})
    print(f'Found {len(repo_files)} markdown files in repo')
    return repo_files

def best_match(lslug, items, key='slug'):
    best=None; best_score=0
    for it in items:
        score=SequenceMatcher(None, lslug, it.get(key,'')).ratio()
        if score>best_score:
            best_score=score; best=it
    return best, round(best_score,3)

def repo_file_for(root,path):
    p1=root/ (path.lstrip('/') + '.md')
    if p1.exists(): return str(p1.relative_to(root))
    p2=root/ path.lstrip('/')
    if (p2/'index.md').exists(): return str((p2/'index.md').relative_to(root))
    return ''

def main():
    if not Path(HTML_TMP).exists():
        print(f'Error: {HTML_TMP} not found. Please fetch the homepage HTML to this path (curl -sSf ... -o {HTML_TMP})')
        return 2
    links=extract_links(HTML_TMP)
    print(f'Extracted {len(links)} links from homepage')
    plans=load_plans(ROOT)
    repos=load_repo_files(ROOT)

    out=ROOT/'live_vs_plan_relaxed.csv'
    with out.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=['link','best_plan_dest','plan_title','plan_source','plan_score','best_repo_path','repo_file','repo_score'])
        w.writeheader()
        for i,l in enumerate(links,1):
            print(f'[{i}/{len(links)}] Processing {l}...')
            sys.stdout.flush()
            lslug=slug(l)
            best_p,pscore=best_match(lslug,plans)
            best_r,rscore=best_match(lslug,repos)
            w.writerow({'link':l,'best_plan_dest': best_p['dest'] if best_p else '',
                        'plan_title': best_p.get('title','') if best_p else '',
                        'plan_source': best_p.get('source','') if best_p else '',
                        'plan_score': pscore if best_p else 0,
                        'best_repo_path': best_r['path'] if best_r else '',
                        'repo_file': best_r['file'] if best_r else '',
                        'repo_score': rscore if best_r else 0})
    print('Wrote',out)
    return 0

if __name__=='__main__':
    raise SystemExit(main())
#!/usr/bin/env python3
"""Verbose relaxed matcher: maps extracted homepage links to migration plan rows and repo files.
Usage: python3 python/relaxed_match_verbose.py
"""
from pathlib import Path
import csv, re, sys
from difflib import SequenceMatcher
import unicodedata

ROOT=Path(__file__).resolve().parents[1]
HTML='/tmp/accessibility_home.html'

def slug(s):
    s=(s or '')
    s=unicodedata.normalize('NFKD',s).lower()
    s=re.sub(r'https?://[^/]+','',s)
    s=re.sub(r'[^a-z0-9]+','-',s)
    return s.strip('-')

def extract_links(html_path):
    from html.parser import HTMLParser
    class P(HTMLParser):
        def __init__(self):
            super().__init__(); self.links=[]
        def handle_starttag(self,tag,attrs):
            if tag!='a': return
            href=dict(attrs).get('href')
            if href: self.links.append(href)
    p=P(); p.feed(Path(html_path).read_text(encoding='utf-8'))
    out=[]
    for href in set(p.links):
        if not href: continue
        href=href.strip()
        if href.startswith(('mailto:','tel:','javascript:')): continue
        href=re.sub(r'https?://[^/]+','',href)
        if not href.startswith('/'): href='/' + href
        href=href.split('?')[0].split('#')[0]
        if href.endswith('/') and href!='/': href=href.rstrip('/')
        out.append(href)
    return sorted(out)

def load_plans(root):
    plan_files=[root/'migration_plan'/'Content redesign of accessibility.civicactions.com - 🗺️ Content plan.csv',
                root/'migration_plan'/'Content redesign of accessibility.civicactions.com - 🛠️ Restructure plan.csv',
                root/'migration_plan'/'Content redesign of accessibility.civicactions.com - Content audit.csv']
    plans=[]
    for pf in plan_files:
        if not pf.exists(): continue
        with pf.open(newline='') as f:
            r=csv.DictReader(f)
            dest=None; title=None
            for c in r.fieldnames:
                lc=c.lower()
                if not dest and ('destination' in lc or 'url' in lc or 'new url' in lc or 'path' in lc): dest=c
                if not title and ('title' in lc or 'page title' in lc or 'name' in lc): title=c
            for row in r:
                dst=row.get(dest,'') if dest else ''
                t=row.get(title,'') if title else ''
                if dst:
                    n=re.sub(r'https?://[^/]+','',dst).split('?')[0].split('#')[0]
                    if not n.startswith('/'):
                        n='/' + n
                    if n.endswith('/') and n!='/': n=n.rstrip('/')
                    plans.append({'dest':n,'title':t,'row':row,'source':pf.name,'slug':slug(n or t)})
    return plans

def load_repo_files(root):
    repo_files=[]
    for p in root.rglob('*.md'):
        if any(part in ('node_modules','.git','_site','archive') for part in p.parts): continue
        rel='/' + str(p.relative_to(root)).replace('index.md','').replace('.md','')
        rel=re.sub(r'//+','/',rel)
        if rel.endswith('/') and rel!='/': rel=rel.rstrip('/')
        title=''
        try:
            txt=p.read_text(encoding='utf-8')
            for line in txt.splitlines():
                if line.strip().lower().startswith('title:'):
                    title=line.split(':',1)[1].strip().strip(' "')
                    break
        except Exception:
            pass
        repo_files.append({'path':rel,'file':str(p.relative_to(root)),'title':title,'slug':slug(rel or title)})
    return repo_files

def main():
    root=ROOT
    if not Path(HTML).exists():
        print('Error: expected',HTML,'to exist (run curl to fetch homepage)')
        return 2
    print('Extracting links...')
    links=extract_links(HTML)
    print('Found',len(links),'links')
    plans=load_plans(root)
    print('Loaded',len(plans),'plan rows')
    repo_files=load_repo_files(root)
    print('Indexed',len(repo_files),'repo markdown files')
    out=root/'live_vs_plan_relaxed.csv'
    with out.open('w',newline='',encoding='utf-8') as f:
        w=csv.DictWriter(f,fieldnames=['link','best_plan_dest','plan_title','plan_source','plan_score','best_repo_path','repo_file','repo_score'])
        w.writeheader()
        from difflib import SequenceMatcher
        for i,l in enumerate(links,1):
            print(f'[{i}/{len(links)}] processing',l)
            lslug=slug(l)
            best_plan=''; best_score=0; best_title=''; best_source=''
            for p in plans:
                score=SequenceMatcher(None, lslug, p['slug']).ratio()
                if score>best_score:
                    best_score=score; best_plan=p['dest']; best_title=p.get('title',''); best_source=p.get('source','')
            best_repo=''; best_rscore=0; best_rfile=''
            for r in repo_files:
                score=SequenceMatcher(None, lslug, r['slug']).ratio()
                if score>best_rscore:
                    best_rscore=score; best_repo=r['path']; best_rfile=r['file']
            print('  best plan:',best_plan,'score',round(best_score,3),' best repo:',best_repo,'score',round(best_rscore,3))
            w.writerow({'link':l,'best_plan_dest':best_plan,'plan_title':best_title,'plan_source':best_source,
                        'plan_score':round(best_score,3),'best_repo_path':best_repo,'repo_file':best_rfile,'repo_score':round(best_rscore,3)})
    print('Wrote',out)
    return 0

if __name__=='__main__':
    raise SystemExit(main())
