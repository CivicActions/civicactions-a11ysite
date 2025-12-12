#!/usr/bin/env python3
"""
Crawl http://localhost:8080 and check for broken internal links.
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse
from collections import defaultdict

BASE_URL = "http://localhost:8080"
visited = set()
broken_links = defaultdict(list)
all_pages = set()

def normalize_url(url):
    """Normalize URL by removing trailing slashes and fragments"""
    parsed = urlparse(url)
    path = parsed.path.rstrip('/')
    if not path:
        path = '/'
    return f"{parsed.scheme}://{parsed.netloc}{path}"

def is_internal_link(url):
    """Check if URL is internal to localhost:8080"""
    return url.startswith(BASE_URL) or url.startswith('/')

def crawl_page(url):
    """Crawl a single page and find all links"""
    normalized_url = normalize_url(url)
    
    if normalized_url in visited:
        return
    
    visited.add(normalized_url)
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            print(f"❌ {response.status_code}: {url}")
            return
        
        all_pages.add(normalized_url)
        print(f"✓ Crawling: {url}")
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Find all links
        for link in soup.find_all('a', href=True):
            href = link['href']
            
            # Skip external links, mailto, etc
            if href.startswith(('http://', 'https://')) and not href.startswith(BASE_URL):
                continue
            if href.startswith(('mailto:', 'tel:', '#', 'javascript:')):
                continue
            
            # Convert relative URLs to absolute
            if href.startswith('/'):
                full_url = BASE_URL + href
            else:
                full_url = urljoin(url, href)
            
            # Check if link exists
            try:
                link_response = requests.head(full_url, timeout=5, allow_redirects=True)
                if link_response.status_code >= 400:
                    broken_links[url].append((href, full_url, link_response.status_code))
                    print(f"  ❌ BROKEN: {href} -> {link_response.status_code}")
                elif is_internal_link(full_url):
                    # Recursively crawl internal links
                    crawl_page(full_url)
            except requests.RequestException as e:
                broken_links[url].append((href, full_url, str(e)))
                print(f"  ❌ ERROR: {href} -> {e}")
                
    except requests.RequestException as e:
        print(f"❌ Failed to crawl {url}: {e}")

def main():
    print(f"Starting crawl of {BASE_URL}")
    print("=" * 80)
    
    crawl_page(BASE_URL)
    
    print("\n" + "=" * 80)
    print(f"Crawled {len(visited)} pages")
    print(f"Total pages found: {len(all_pages)}")
    
    if broken_links:
        print(f"\n❌ Found {sum(len(links) for links in broken_links.values())} broken links:\n")
        for page, links in sorted(broken_links.items()):
            print(f"\n{page}:")
            for href, full_url, status in links:
                print(f"  - {href} -> {full_url} ({status})")
    else:
        print("\n✅ No broken links found!")
    
    print(f"\n📄 All pages crawled:")
    for page in sorted(all_pages):
        print(f"  {page}")

if __name__ == "__main__":
    main()
