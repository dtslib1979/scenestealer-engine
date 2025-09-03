#!/usr/bin/env python3
"""
Update main index.html with latest sample
Adds a featured sample section to the main page
"""

import os
import sys
import re
from datetime import datetime
from pathlib import Path

def extract_title_from_html(html_content):
    """Extract title from HTML content"""
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
    if title_match:
        return title_match.group(1).replace(' - Scenestealer Engine', '')
    return "Latest Sample"

def extract_description_from_html(html_content):
    """Extract description from HTML content"""
    # Try first paragraph in hero section
    p_match = re.search(r'<p[^>]*>(.*?)</p>', html_content, re.IGNORECASE)
    if p_match:
        text = re.sub(r'<[^>]*>', '', p_match.group(1))
        return text[:100] + ('...' if len(text) > 100 else '')
    return "Check out our latest design sample"

def get_latest_sample(samples_dir):
    """Get the most recently modified sample"""
    samples_path = Path(samples_dir)
    
    if not samples_path.exists():
        return None
    
    html_files = list(samples_path.glob('*.html'))
    if not html_files:
        return None
    
    # Get most recent file
    latest_file = max(html_files, key=lambda x: x.stat().st_mtime)
    
    try:
        with open(latest_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        return {
            'filename': latest_file.name,
            'title': extract_title_from_html(content),
            'description': extract_description_from_html(content),
            'modified': datetime.fromtimestamp(latest_file.stat().st_mtime).strftime('%B %d, %Y')
        }
    except Exception as e:
        print(f"Error reading latest sample: {e}")
        return None

def update_index_html(samples_dir, index_file):
    """Update the main index.html with latest sample info"""
    latest_sample = get_latest_sample(samples_dir)
    
    try:
        with open(index_file, 'r', encoding='utf-8') as f:
            content = f.read()
    except FileNotFoundError:
        print(f"Index file {index_file} not found")
        return
    
    # Create the latest sample section HTML
    if latest_sample:
        latest_section = f'''
      <div class="latest-sample">
        <div class="sample-badge">🆕 Latest Sample</div>
        <h3>{latest_sample['title']}</h3>
        <p>{latest_sample['description']}</p>
        <div class="sample-actions">
          <a href="samples/{latest_sample['filename']}" target="_blank" class="btn">Preview</a>
          <a href="editor/?sample={latest_sample['filename']}" class="btn secondary">Edit</a>
          <a href="archive.html" class="btn secondary">View All</a>
        </div>
        <div class="sample-date">Updated {latest_sample['modified']}</div>
      </div>'''
    else:
        latest_section = '''
      <div class="latest-sample">
        <div class="sample-badge">📁 Archive</div>
        <h3>Browse Design Samples</h3>
        <p>Explore our collection of beautiful, ready-to-use design templates.</p>
        <div class="sample-actions">
          <a href="archive.html" class="btn">Browse Archive</a>
          <a href="editor/" class="btn secondary">Open Editor</a>
        </div>
      </div>'''
    
    # Add CSS for the latest sample section if not present
    css_addition = '''
  .latest-sample{
    background:var(--card); padding:24px; border-radius:var(--radius);
    box-shadow:var(--shadow); border:1px solid var(--border);
    margin:24px 0; text-align:center;
  }
  .sample-badge{
    display:inline-block; padding:4px 12px; background:var(--accent);
    color:white; border-radius:16px; font-size:12px; font-weight:500;
    margin-bottom:16px;
  }
  .latest-sample h3{margin:0 0 12px; color:var(--ink)}
  .latest-sample p{color:var(--muted); margin:0 0 16px}
  .sample-actions{display:flex; gap:12px; justify-content:center; flex-wrap:wrap}
  .sample-date{color:var(--muted); font-size:12px; margin-top:16px}'''
    
    # Insert CSS if not already present
    if '.latest-sample{' not in content:
        css_insert_pos = content.find('</style>')
        if css_insert_pos != -1:
            content = content[:css_insert_pos] + css_addition + '\n' + content[css_insert_pos:]
    
    # Find where to insert the latest sample section
    # Look for the CTA section and insert before it
    cta_match = re.search(r'(<div class="cta">)', content, re.IGNORECASE)
    if cta_match:
        insert_pos = cta_match.start()
        content = content[:insert_pos] + latest_section + '\n      ' + content[insert_pos:]
    else:
        # If no CTA section found, insert before closing of hero section
        hero_close = re.search(r'(</div>\s*</section>)', content, re.IGNORECASE)
        if hero_close:
            insert_pos = hero_close.start()
            content = content[:insert_pos] + latest_section + '\n    ' + content[insert_pos:]
    
    # Write back the updated content
    with open(index_file, 'w', encoding='utf-8') as f:
        f.write(content)
    
    if latest_sample:
        print(f"Updated {index_file} with latest sample: {latest_sample['title']}")
    else:
        print(f"Updated {index_file} with archive link (no samples found)")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python update_index.py <samples_dir> <index_file>")
        sys.exit(1)
    
    samples_dir = sys.argv[1]
    index_file = sys.argv[2]
    update_index_html(samples_dir, index_file)