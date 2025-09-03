# 🎬 SceneStealer Engine — Archive & Editor

This repository provides a **SceneStealer Archive** system with automated GitHub Pages deployment.  
It combines a design editor with an automated sample archive workflow.

## Philosophy
- **Repository = App Unit (Static)**
- **Author = Sample Creator**, **User = Design Consumer**
- Automatic archive generation from uploaded samples

## SceneStealer Archive Structure

```
/
├── samples/          # HTML design samples (author uploads regularly)  
├── editor/           # SceneStealer engine (in-browser editor)
├── docs/             # Usage & tutorials
├── web/              # Auto-generated website (GitHub Pages)
│   ├── index.html    # Latest sample & editor links
│   ├── archive.html  # All samples list (auto-generated)
│   ├── rss.xml       # RSS feed (auto-generated)
│   └── sitemap.xml   # Sitemap (auto-generated)
├── scripts/          # Automation scripts
├── apps/web/         # Original editor source
└── .github/workflows/build-archive.yml  # Auto-build workflow
```

## How to Publish a New Sample
1. **Create** a new HTML file in `samples/` (e.g., `2025-09-03-sample1.html`)
2. **Commit & push** your changes
3. **Wait** for GitHub Actions to automatically:
   - Rebuild `web/archive.html` (samples list)
   - Update `web/index.html` (latest sample preview)
   - Generate `web/rss.xml` and `web/sitemap.xml`
   - Deploy to GitHub Pages

**Public URLs**
- **Latest Sample**: `/` 
- **Archive**: `/archive.html`
- **Editor**: `/editor/` 
- **Editor with Sample Preload**: `/editor/index.html?load=../samples/<file.html>`

## User Workflow
1. Browse samples at `/archive.html`
2. Select a sample that looks interesting  
3. Click "Open in Editor" to customize it
4. Export the customized HTML for your own site

## Features
- **Automated Archive Generation** - Upload samples, get instant archive
- **Sample Preview** - Latest sample shown with iframe preview
- **Editor Integration** - Direct links to edit any sample
- **RSS/Sitemap** - SEO-friendly feeds for discovery
- **Mobile Responsive** - Works on all devices
- **GitHub Pages** - Free hosting and deployment

## Manual Testing
```bash
# Test scripts locally
python scripts/generate_archive.py samples web/archive.html
python scripts/update_index.py samples web/index.html  
python scripts/generate_rss.py samples web/rss.xml
python scripts/generate_sitemap.py web web/sitemap.xml
```

## License
MIT