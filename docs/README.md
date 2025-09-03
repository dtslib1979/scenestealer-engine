# SceneStealer Archive Documentation

## Overview
The SceneStealer Archive system provides automated management of HTML design samples with GitHub Pages deployment.

## Folder Structure
```
/
├── samples/          # HTML design samples (upload here)
├── editor/          # SceneStealer editor (symlink to apps/web/)
├── docs/            # Documentation
├── web/             # Auto-generated site for GitHub Pages
│   ├── index.html   # Latest sample preview
│   ├── archive.html # All samples list
│   ├── rss.xml      # RSS feed
│   └── sitemap.xml  # Sitemap
└── scripts/         # Automation scripts
```

## How to Add New Samples
1. Create an HTML file in the `samples/` directory
2. Name it with a date prefix (e.g., `2025-09-03-sample1.html`)
3. Commit and push your changes
4. GitHub Actions will automatically:
   - Generate updated archive.html and index.html
   - Create RSS feed and sitemap
   - Deploy to GitHub Pages

## Scripts
- `generate_archive.py` - Creates the samples archive page
- `update_index.py` - Updates the latest sample preview
- `generate_rss.py` - Generates RSS feed
- `generate_sitemap.py` - Generates sitemap

## Manual Testing
```bash
# Generate all files locally
python scripts/generate_archive.py samples web/archive.html
python scripts/update_index.py samples web/index.html  
python scripts/generate_rss.py samples web/rss.xml
python scripts/generate_sitemap.py web web/sitemap.xml
```