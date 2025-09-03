#!/usr/bin/env python3
"""
Generate RSS feed for SceneStealer samples
Creates an RSS XML feed for blog integration
"""

import os
import sys
from datetime import datetime
from pathlib import Path
import re
import html

def extract_title_from_html(html_content):
    """Extract title from HTML content"""
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
    if title_match:
        return html.escape(title_match.group(1))
    return "SceneStealer Sample"

def extract_description_from_html(html_content):
    """Extract description from HTML content"""
    # Try meta description first
    desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html_content, re.IGNORECASE)
    if desc_match:
        return html.escape(desc_match.group(1))
    
    # Try first paragraph
    p_match = re.search(r'<p[^>]*>(.*?)</p>', html_content, re.IGNORECASE)
    if p_match:
        text = re.sub(r'<[^>]*>', '', p_match.group(1))
        return html.escape(text[:200] + ('...' if len(text) > 200 else ''))
    
    return "A beautiful design sample created with SceneStealer Engine"

def generate_rss_feed(samples_dir, output_file, base_url="https://dtslib1979.github.io/scenestealer-engine"):
    """Generate RSS feed for samples"""
    samples_path = Path(samples_dir)
    
    if not samples_path.exists():
        print(f"Samples directory {samples_dir} does not exist")
        return
    
    html_files = list(samples_path.glob('*.html'))
    html_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    
    # Take only the 20 most recent samples for the feed
    recent_files = html_files[:20]
    
    current_time = datetime.now()
    
    rss_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0" xmlns:atom="http://www.w3.org/2005/Atom">
  <channel>
    <title>SceneStealer Archive - Design Samples</title>
    <link>{base_url}</link>
    <description>Latest design samples and templates from SceneStealer Engine</description>
    <language>en-us</language>
    <lastBuildDate>{current_time.strftime('%a, %d %b %Y %H:%M:%S %z')}</lastBuildDate>
    <atom:link href="{base_url}/rss.xml" rel="self" type="application/rss+xml" />
    <generator>SceneStealer Engine Archive Generator</generator>
    <image>
      <url>{base_url}/favicon.ico</url>
      <title>SceneStealer Archive</title>
      <link>{base_url}</link>
    </image>
'''

    for html_file in recent_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            title = extract_title_from_html(content)
            description = extract_description_from_html(content)
            pub_date = datetime.fromtimestamp(html_file.stat().st_mtime)
            
            rss_content += f'''
    <item>
      <title>{title}</title>
      <link>{base_url}/samples/{html_file.name}</link>
      <guid>{base_url}/samples/{html_file.name}</guid>
      <description>{description}</description>
      <pubDate>{pub_date.strftime('%a, %d %b %Y %H:%M:%S %z')}</pubDate>
      <category>Design Sample</category>
      <category>SceneStealer</category>
      <enclosure url="{base_url}/samples/{html_file.name}" type="text/html" length="{html_file.stat().st_size}"/>
    </item>'''
        
        except Exception as e:
            print(f"Error processing {html_file.name} for RSS: {e}")
    
    rss_content += '''
  </channel>
</rss>'''

    # Write the RSS file
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rss_content)
    
    print(f"Generated RSS feed {output_file} with {len(recent_files)} items")

if __name__ == '__main__':
    if len(sys.argv) not in [3, 4]:
        print("Usage: python generate_rss.py <samples_dir> <output_file> [base_url]")
        sys.exit(1)
    
    samples_dir = sys.argv[1]
    output_file = sys.argv[2]
    base_url = sys.argv[3] if len(sys.argv) > 3 else "https://dtslib1979.github.io/scenestealer-engine"
    
    generate_rss_feed(samples_dir, output_file, base_url)