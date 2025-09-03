#!/usr/bin/env python3
"""
Generate sitemap.xml for SceneStealer samples
Creates an XML sitemap for better SEO
"""

import os
import sys
from datetime import datetime
from pathlib import Path
import html

def generate_sitemap(samples_dir, output_file, base_url="https://dtslib1979.github.io/scenestealer-engine"):
    """Generate sitemap.xml for all pages"""
    samples_path = Path(samples_dir)
    
    current_time = datetime.now().strftime('%Y-%m-%d')
    
    sitemap_content = f'''<?xml version="1.0" encoding="UTF-8"?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">
  <url>
    <loc>{base_url}/</loc>
    <lastmod>{current_time}</lastmod>
    <changefreq>weekly</changefreq>
    <priority>1.0</priority>
  </url>
  <url>
    <loc>{base_url}/archive.html</loc>
    <lastmod>{current_time}</lastmod>
    <changefreq>daily</changefreq>
    <priority>0.9</priority>
  </url>
  <url>
    <loc>{base_url}/editor/</loc>
    <lastmod>{current_time}</lastmod>
    <changefreq>monthly</changefreq>
    <priority>0.8</priority>
  </url>'''

    if samples_path.exists():
        html_files = list(samples_path.glob('*.html'))
        html_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
        
        for html_file in html_files:
            try:
                last_modified = datetime.fromtimestamp(html_file.stat().st_mtime).strftime('%Y-%m-%d')
                
                sitemap_content += f'''
  <url>
    <loc>{base_url}/samples/{html_file.name}</loc>
    <lastmod>{last_modified}</lastmod>
    <changefreq>never</changefreq>
    <priority>0.7</priority>
  </url>'''
            
            except Exception as e:
                print(f"Error processing {html_file.name} for sitemap: {e}")
    
    sitemap_content += '''
</urlset>'''

    # Write the sitemap file
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(sitemap_content)
    
    sample_count = len(list(samples_path.glob('*.html'))) if samples_path.exists() else 0
    print(f"Generated sitemap {output_file} with {sample_count + 3} URLs")

if __name__ == '__main__':
    if len(sys.argv) not in [3, 4]:
        print("Usage: python generate_sitemap.py <samples_dir> <output_file> [base_url]")
        sys.exit(1)
    
    samples_dir = sys.argv[1]
    output_file = sys.argv[2]
    base_url = sys.argv[3] if len(sys.argv) > 3 else "https://dtslib1979.github.io/scenestealer-engine"
    
    generate_sitemap(samples_dir, output_file, base_url)