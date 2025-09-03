#!/usr/bin/env python3
"""
Generate archive.html from samples directory
Creates a gallery page with previews and download links for all samples
"""

import os
import sys
from datetime import datetime
from pathlib import Path
import re

def extract_title_from_html(html_content):
    """Extract title from HTML content"""
    title_match = re.search(r'<title>(.*?)</title>', html_content, re.IGNORECASE)
    if title_match:
        return title_match.group(1)
    
    h1_match = re.search(r'<h1[^>]*>(.*?)</h1>', html_content, re.IGNORECASE)
    if h1_match:
        return re.sub(r'<[^>]*>', '', h1_match.group(1))
    
    return "Untitled Sample"

def extract_description_from_html(html_content):
    """Extract description from HTML content"""
    # Try meta description first
    desc_match = re.search(r'<meta[^>]*name=["\']description["\'][^>]*content=["\']([^"\']*)["\']', html_content, re.IGNORECASE)
    if desc_match:
        return desc_match.group(1)
    
    # Try first paragraph
    p_match = re.search(r'<p[^>]*>(.*?)</p>', html_content, re.IGNORECASE)
    if p_match:
        text = re.sub(r'<[^>]*>', '', p_match.group(1))
        return text[:200] + ('...' if len(text) > 200 else '')
    
    return "A beautiful SceneStealer sample design"

def generate_archive_html(samples_dir, output_file):
    """Generate the archive.html file"""
    samples_path = Path(samples_dir)
    
    if not samples_path.exists():
        print(f"Samples directory {samples_dir} does not exist")
        return
    
    html_files = list(samples_path.glob('*.html'))
    html_files.sort(key=lambda x: x.stat().st_mtime, reverse=True)
    
    samples_data = []
    
    for html_file in html_files:
        try:
            with open(html_file, 'r', encoding='utf-8') as f:
                content = f.read()
            
            sample_data = {
                'filename': html_file.name,
                'title': extract_title_from_html(content),
                'description': extract_description_from_html(content),
                'size': f"{html_file.stat().st_size / 1024:.1f} KB",
                'modified': datetime.fromtimestamp(html_file.stat().st_mtime).strftime('%Y-%m-%d')
            }
            samples_data.append(sample_data)
        except Exception as e:
            print(f"Error processing {html_file.name}: {e}")
    
    # Generate archive HTML
    archive_html = f'''<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>SceneStealer Archive - Design Samples</title>
  <meta name="description" content="Browse and download beautiful design samples created with SceneStealer Engine" />
  <style>
    :root{{
      --bg:#0b0f16; --ink:#e7ecf5; --muted:#94a3b8; --primary:#4c8bf5; --accent:#8b5cf6;
      --card:#0f1520; --border:#1f2734; --radius:12px; 
      --shadow: 0 4px 12px rgba(0,0,0,.25);
      --glow: 0 10px 40px rgba(76,139,245,.25);
    }}
    *{{box-sizing:border-box}}
    body{{
      margin:0; font: 15px/1.6 ui-sans-serif,system-ui,-apple-system,Segoe UI,Roboto,Helvetica,Arial;
      color:var(--ink); background:var(--bg);
      background-image: 
        radial-gradient(circle at 20% 80%, rgba(76,139,245,.15) 0%, transparent 50%),
        radial-gradient(circle at 80% 20%, rgba(139,92,246,.15) 0%, transparent 50%);
    }}
    .container{{max-width:1200px; margin:0 auto; padding:0 20px}}
    .header{{text-align:center; padding:60px 0 40px}}
    .header h1{{font-size:48px; margin:0 0 16px; background:linear-gradient(135deg, var(--primary), var(--accent)); 
               background-clip:text; -webkit-background-clip:text; color:transparent}}
    .header p{{font-size:20px; color:var(--muted); margin:0 0 32px}}
    .stats{{display:flex; justify-content:center; gap:40px; margin-bottom:40px}}
    .stat{{text-align:center}}
    .stat-number{{font-size:32px; font-weight:bold; color:var(--primary)}}
    .stat-label{{color:var(--muted); font-size:14px}}
    .nav{{display:flex; justify-content:center; gap:20px; margin-bottom:40px}}
    .btn{{
      display:inline-block; padding:12px 24px; background:var(--primary); 
      color:white; text-decoration:none; border-radius:var(--radius);
      border:none; cursor:pointer; font-weight:500; transition:all 0.2s;
    }}
    .btn:hover{{transform:translateY(-2px); box-shadow:var(--glow)}}
    .btn.secondary{{background:transparent; border:1px solid var(--border); color:var(--ink)}}
    .btn.secondary:hover{{background:var(--card); border-color:var(--primary)}}
    .grid{{display:grid; grid-template-columns:repeat(auto-fill, minmax(400px, 1fr)); gap:24px; padding:40px 0}}
    .sample-card{{
      background:var(--card); border-radius:var(--radius); 
      box-shadow:var(--shadow); border:1px solid var(--border);
      overflow:hidden; transition:all 0.3s;
    }}
    .sample-card:hover{{transform:translateY(-4px); box-shadow:var(--glow)}}
    .sample-preview{{
      height:200px; background:linear-gradient(135deg, var(--primary), var(--accent));
      position:relative; overflow:hidden;
    }}
    .sample-preview iframe{{width:100%; height:400px; transform:scale(0.5); transform-origin:top left; border:none}}
    .sample-info{{padding:24px}}
    .sample-title{{font-size:20px; font-weight:600; margin:0 0 8px; color:var(--ink)}}
    .sample-description{{color:var(--muted); margin:0 0 16px; line-height:1.5}}
    .sample-meta{{display:flex; justify-content:space-between; color:var(--muted); font-size:14px; margin-bottom:16px}}
    .sample-actions{{display:flex; gap:12px}}
    .btn-small{{padding:8px 16px; font-size:14px}}
    .footer{{text-align:center; padding:60px 0; border-top:1px solid var(--border); margin-top:60px}}
    @media (max-width:640px){{
      .header h1{{font-size:32px}}
      .grid{{grid-template-columns:1fr; gap:16px}}
      .stats{{flex-direction:column; gap:20px}}
    }}
  </style>
</head>
<body>
  <div class="container">
    <div class="header">
      <h1>SceneStealer Archive</h1>
      <p>Browse beautiful design samples · Pick what you like · Edit in the engine</p>
      
      <div class="stats">
        <div class="stat">
          <div class="stat-number">{len(samples_data)}</div>
          <div class="stat-label">Samples</div>
        </div>
        <div class="stat">
          <div class="stat-number">{datetime.now().strftime('%Y')}</div>
          <div class="stat-label">Latest Year</div>
        </div>
      </div>
      
      <div class="nav">
        <a href="../editor/" class="btn">Open Editor</a>
        <a href="/" class="btn secondary">Back to Home</a>
      </div>
    </div>

    <div class="grid">'''

    for sample in samples_data:
        archive_html += f'''
      <div class="sample-card">
        <div class="sample-preview">
          <iframe src="../samples/{sample['filename']}" loading="lazy"></iframe>
        </div>
        <div class="sample-info">
          <div class="sample-title">{sample['title']}</div>
          <div class="sample-description">{sample['description']}</div>
          <div class="sample-meta">
            <span>Size: {sample['size']}</span>
            <span>Updated: {sample['modified']}</span>
          </div>
          <div class="sample-actions">
            <a href="../samples/{sample['filename']}" target="_blank" class="btn btn-small">Preview</a>
            <a href="../samples/{sample['filename']}" download class="btn btn-small secondary">Download</a>
            <a href="../editor/?sample={sample['filename']}" class="btn btn-small" style="background:var(--accent)">Edit</a>
          </div>
        </div>
      </div>'''

    archive_html += f'''
    </div>

    <div class="footer">
      <p>Generated on {datetime.now().strftime('%Y-%m-%d %H:%M')} • <a href="https://github.com/dtslib1979/scenestealer-engine" style="color:var(--primary)">SceneStealer Engine</a></p>
    </div>
  </div>
</body>
</html>'''

    # Write the file
    output_path = Path(output_file)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(archive_html)
    
    print(f"Generated {output_file} with {len(samples_data)} samples")

if __name__ == '__main__':
    if len(sys.argv) != 3:
        print("Usage: python generate_archive.py <samples_dir> <output_file>")
        sys.exit(1)
    
    samples_dir = sys.argv[1]
    output_file = sys.argv[2]
    generate_archive_html(samples_dir, output_file)