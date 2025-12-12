#!/usr/bin/env python3
"""
Check for stub or empty content pages on localhost:8080
"""

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin, urlparse

BASE_URL = "http://localhost:8080"
visited = set()
stub_pages = []

def normalize_url(url):
    """Normalize URL by removing trailing slashes and fragments"""
    parsed = urlparse(url)
    path = parsed.path.rstrip('/')
    if not path:
        path = '/'
    return f"{parsed.scheme}://{parsed.netloc}{path}"

def get_main_content(soup):
    """Extract main content text from page"""
    # Try to find main content area
    main = soup.find('main') or soup.find('article') or soup.find('body')
    if not main:
        return ""
    
    # Remove nav, footer, header from content check
    for element in main.find_all(['nav', 'footer', 'header', 'script', 'style']):
        element.decompose()
    
    return main.get_text(strip=True)

def is_stub_content(content, url):
    """Check if content appears to be a stub"""
    # Strip whitespace
    content = content.strip()
    
    # Empty content
    if len(content) < 50:
        return True, "Very short content (< 50 chars)"
    
    # Common stub indicators
    stub_keywords = [
        'placeholder',
        'coming soon',
        'under construction',
        'stub',
        'todo',
        'to be written',
        'content goes here',
        'lorem ipsum'
    ]
    
    content_lower = content.lower()
    for keyword in stub_keywords:
        if keyword in content_lower:
            return True, f"Contains stub keyword: '{keyword}'"
    
    # Very short content
    if len(content) < 200:
        return True, f"Short content ({len(content)} chars)"
    
    return False, None

def crawl_page(url):
    """Crawl a single page and check for stub content"""
    normalized_url = normalize_url(url)
    
    if normalized_url in visited:
        return
    
    visited.add(normalized_url)
    
    try:
        response = requests.get(url, timeout=5)
        if response.status_code != 200:
            return
        
        soup = BeautifulSoup(response.content, 'html.parser')
        
        # Get main content
        content = get_main_content(soup)
        
        # Check if it's a stub
        is_stub, reason = is_stub_content(content, url)
        if is_stub:
            title = soup.find('title')
            title_text = title.get_text(strip=True) if title else "No title"
            stub_pages.append({
                'url': url,
                'title': title_text,
                'reason': reason,
                'content_length': len(content),
                'preview': content[:100] + '...' if len(content) > 100 else content
            })
            print(f"🚩 STUB: {url}")
            print(f"   Title: {title_text}")
            print(f"   Reason: {reason}")
            print(f"   Preview: {content[:100]}...")
            print()
        
        # Find and crawl internal links
        for link in soup.find_all('a', href=True):
            href = link['href']
            
            if href.startswith(('http://', 'https://')) and not href.startswith(BASE_URL):
                continue
            if href.startswith(('mailto:', 'tel:', '#', 'javascript:')):
                continue
            
            if href.startswith('/'):
                full_url = BASE_URL + href
            else:
                full_url = urljoin(url, href)
            
            if full_url.startswith(BASE_URL):
                crawl_page(full_url)
                
    except requests.RequestException as e:
        print(f"❌ Error crawling {url}: {e}")

def main():
    print(f"Checking for stub content on {BASE_URL}")
    print("=" * 80)
    
    crawl_page(BASE_URL)
    
    print("\n" + "=" * 80)
    print(f"Crawled {len(visited)} pages")
    
    if stub_pages:
        print(f"\n🚩 Found {len(stub_pages)} stub pages:\n")
        for stub in stub_pages:
            print(f"URL: {stub['url']}")
            print(f"Title: {stub['title']}")
            print(f"Reason: {stub['reason']}")
            print(f"Content length: {stub['content_length']} chars")
            print(f"Preview: {stub['preview']}")
            print("-" * 80)
    else:
        print("\n✅ No stub pages found!")

if __name__ == "__main__":
    main()
