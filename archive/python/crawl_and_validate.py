#!/usr/bin/env python3
"""
Crawl https://accessibility.civicactions.com/ and validate migration completeness.
"""

import os
import re
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from pathlib import Path
import time

BASE_URL = "https://accessibility.civicactions.com"
REPO_ROOT = Path(__file__).parent.parent
VISITED_URLS = set()
ALL_PAGES = []

def get_sitemap_urls():
    """Fetch URLs from sitemap.xml"""
    print("Fetching sitemap.xml...")
    response = requests.get(f"{BASE_URL}/sitemap.xml")
    soup = BeautifulSoup(response.content, 'xml')
    urls = [loc.text for loc in soup.find_all('loc')]
    print(f"Found {len(urls)} URLs in sitemap")
    return urls

def load_migration_plan():
    """Load URLs from redirects-plan.txt"""
    plan_file = REPO_ROOT / "redirects-plan.txt"
    urls_in_plan = set()

    if plan_file.exists():
        with open(plan_file, 'r') as f:
            for line in f:
                # Extract URLs from migration plan
                if 'accessibility.civicactions.com' in line and not line.strip().startswith('#'):
                    matches = re.findall(r'https://accessibility\.civicactions\.com[^\s\[]+', line)
                    urls_in_plan.update(matches)

    print(f"Found {len(urls_in_plan)} URLs in migration plan")
    return urls_in_plan

def check_file_exists_in_repo(url):
    """Check if corresponding file exists in new repo structure"""
    path = urlparse(url).path.strip('/')

    # Check various possible locations
    possible_paths = [
        REPO_ROOT / f"{path}.md",
        REPO_ROOT / path / "index.md",
        REPO_ROOT / "guides" / f"{path}.md",
        REPO_ROOT / "guides" / path / "index.md",
        REPO_ROOT / "champions" / f"{path}.md",
        REPO_ROOT / "champions" / path / "index.md",
        REPO_ROOT / "about" / f"{path}.md",
        REPO_ROOT / "about" / path / "index.md",
    ]

    # Check archive directories
    archive_paths = [
        REPO_ROOT / "archive" / path / "index.md",
        REPO_ROOT / "archive" / f"{path}.md",
        REPO_ROOT / "archive/missing-pages" / f"{path.replace('/', '-')}.md",
    ]

    for p in possible_paths:
        if p.exists():
            return True, p, "migrated"

    for p in archive_paths:
        if p.exists():
            return True, p, "archived"

    return False, None, None

def fetch_page_content(url):
    """Fetch markdown source from GitHub repo"""
    # Map URL to potential GitHub source path
    path = urlparse(url).path.strip('/')

    # Try different source locations in original repo
    possible_sources = []

    if path.startswith('guide/'):
        possible_sources.append(f"_guide/{path.replace('guide/', '')}.md")
    elif path.startswith('playbook/'):
        possible_sources.append(f"_playbook/{path.replace('playbook/', '')}.md")
    elif path.startswith('about/people/'):
        possible_sources.append(f"_people/{path.replace('about/people/', '')}.md")
    elif path.startswith('posts/'):
        possible_sources.append(f"_posts/{path.replace('posts/', '')}.md")

    # Also try root level
    possible_sources.append(f"_{path}.md")
    possible_sources.append(f"{path}.md")

    for source_path in possible_sources:
        github_url = f"https://raw.githubusercontent.com/CivicActions/accessibility/main/{source_path}"
        try:
            response = requests.get(github_url)
            if response.status_code == 200 and len(response.text) > 10:
                return response.text, source_path
        except:
            continue

    return None, None

def main():
    print("=" * 80)
    print("MIGRATION VALIDATION REPORT")
    print("=" * 80)
    print()

    # Get all URLs from sitemap
    sitemap_urls = get_sitemap_urls()

    # Load migration plan
    plan_urls = load_migration_plan()

    # Analysis
    missing_from_plan = []
    missing_from_repo = []
    archived_pages = []
    migrated_pages = []

    print("\nAnalyzing pages...")
    print("-" * 80)

    for url in sitemap_urls:
        # Skip non-HTML pages
        if any(ext in url for ext in ['.xml', '.pdf', '.json', '.css', '.js']):
            continue

        # Check if in migration plan
        in_plan = url in plan_urls

        # Check if file exists in repo
        exists, file_path, status = check_file_exists_in_repo(url)

        result = {
            'url': url,
            'in_plan': in_plan,
            'exists': exists,
            'path': file_path,
            'status': status
        }

        if status == "migrated":
            migrated_pages.append(result)
        elif status == "archived":
            archived_pages.append(result)
        elif not exists and not in_plan:
            missing_from_plan.append(result)
            missing_from_repo.append(result)
        elif not exists:
            missing_from_repo.append(result)

    # Print summary
    print(f"\n{'SUMMARY':^80}")
    print("=" * 80)
    print(f"Total URLs in sitemap:        {len(sitemap_urls)}")
    print(f"URLs in migration plan:       {len(plan_urls)}")
    print(f"Migrated pages (found):       {len(migrated_pages)}")
    print(f"Archived pages (found):       {len(archived_pages)}")
    print(f"Missing from plan:            {len(missing_from_plan)}")
    print(f"Missing from repo:            {len(missing_from_repo)}")
    print()

    # Show pages missing from both plan and repo
    if missing_from_repo:
        print(f"\n{'PAGES NEEDING ARCHIVAL':^80}")
        print("=" * 80)
        print("These pages exist on live site but not in migration plan or repo:\n")

        to_archive = []
        for item in missing_from_repo[:20]:  # Show first 20
            print(f"  {item['url']}")

            # Try to fetch content
            content, source = fetch_page_content(item['url'])
            if content:
                to_archive.append({
                    'url': item['url'],
                    'content': content,
                    'source': source
                })

        if len(missing_from_repo) > 20:
            print(f"\n  ... and {len(missing_from_repo) - 20} more")

        # Save missing pages
        if to_archive:
            print(f"\n\nSaving {len(to_archive)} missing pages to archive...")
            archive_dir = REPO_ROOT / "archive" / "missing-pages"
            archive_dir.mkdir(parents=True, exist_ok=True)

            saved_count = 0
            for item in to_archive:
                # Create filename from URL
                path = urlparse(item['url']).path.strip('/').replace('/', '-')
                if not path:
                    path = 'homepage'
                filename = f"{path}.md"

                # Check if already archived
                filepath = archive_dir / filename
                if not filepath.exists():
                    with open(filepath, 'w') as f:
                        f.write(item['content'])
                    saved_count += 1
                    print(f"  ✓ Saved: {filename}")

            print(f"\nArchived {saved_count} new pages to /archive/missing-pages/")

    # Show archived pages
    if archived_pages:
        print(f"\n{'ALREADY ARCHIVED':^80}")
        print("=" * 80)
        print(f"These {len(archived_pages)} pages are already in archive:\n")
        for item in archived_pages[:10]:
            print(f"  {item['url']}")
            print(f"    → {item['path'].relative_to(REPO_ROOT)}")
        if len(archived_pages) > 10:
            print(f"\n  ... and {len(archived_pages) - 10} more")

    print("\n" + "=" * 80)
    print("VALIDATION COMPLETE")
    print("=" * 80)

if __name__ == "__main__":
    main()
