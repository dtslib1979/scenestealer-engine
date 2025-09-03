# 🎭 SceneStealer Archive Workflow

Automated system for managing HTML design samples with GitHub Actions integration.

## Overview

This workflow enables automatic processing of HTML design samples uploaded to the repository. When you add samples to the `/samples/` directory, GitHub Actions automatically:

1. **Generates Archive Page** - Creates a beautiful gallery at `/web/archive.html`
2. **Updates Main Index** - Adds latest sample to the homepage
3. **Creates RSS Feed** - For blog integration at `/web/rss.xml`
4. **Generates Sitemap** - For SEO at `/web/sitemap.xml`
5. **Deploys to GitHub Pages** - Everything goes live automatically
6. **Sends Notifications** - Via GitHub Issues

## Folder Structure

```
/scenestealer-engine/
├── samples/          ← HTML samples (trigger automation)
├── editor/           ← SceneStealer Engine (user editor)
├── docs/            ← Documentation & tutorials
├── web/             ← GitHub Pages deployment
│   ├── index.html   ← Main homepage
│   ├── archive.html ← Auto-generated sample gallery
│   ├── rss.xml      ← Auto-generated RSS feed
│   └── sitemap.xml  ← Auto-generated sitemap
└── scripts/         ← Python automation scripts
```

## How to Use

### Adding New Samples

1. Create your HTML design file
2. Upload it to `/samples/` directory
3. Commit and push to main branch
4. Automation runs automatically!

### Sample File Format

Your HTML files should include:

```html
<!doctype html>
<html lang="en">
<head>
  <title>Your Sample Title - Scenestealer Engine</title>
  <meta name="description" content="Description of your design">
  <!-- Your styles here -->
</head>
<body>
  <!-- Your design content -->
</body>
</html>
```

The automation will extract the title and description automatically.

### Accessing Results

After automation completes:
- **Archive**: `https://yourusername.github.io/repo/archive.html`
- **Editor**: `https://yourusername.github.io/repo/editor/`
- **RSS Feed**: `https://yourusername.github.io/repo/rss.xml`

## Workflow Details

### Triggers
- Push to `main` branch with changes in `samples/**`
- Manual workflow dispatch

### Generated Content

#### Archive Page (`archive.html`)
- Gallery of all samples with previews
- Preview, Download, and Edit buttons for each
- Responsive design with iframe previews
- Auto-generated from sample metadata

#### RSS Feed (`rss.xml`)
- Latest 20 samples
- Blog-compatible XML format
- Includes sample metadata and links

#### Sitemap (`sitemap.xml`)
- All pages for SEO optimization
- Automatic priority and change frequency
- Includes samples, editor, and main pages

### Notifications

The workflow creates GitHub Issues for:
- ✅ Successful deployments (with stats)
- ❌ Build failures (with debugging info)

Issues are labeled with `auto-archive` for easy filtering.

## Customization

### Modifying Templates

Edit the Python scripts in `/scripts/` to customize:
- **Archive layout**: `generate_archive.py`
- **Index integration**: `update_index.py` 
- **RSS format**: `generate_rss.py`
- **Sitemap structure**: `generate_sitemap.py`

### Workflow Settings

Edit `.github/workflows/build-archive.yml` to:
- Change trigger conditions
- Modify notification settings
- Add additional automation steps

### Styling

The archive page uses CSS variables for theming:
```css
:root {
  --bg: #0b0f16;
  --ink: #e7ecf5;
  --primary: #4c8bf5;
  --accent: #8b5cf6;
  /* ... */
}
```

## Integration with Blogs

### RSS Feed Integration
Add to your blog/Tistory:
```xml
https://yourusername.github.io/repo/rss.xml
```

### Direct Links
Link to specific samples:
```
https://yourusername.github.io/repo/samples/your-sample.html
```

Link to archive:
```
https://yourusername.github.io/repo/archive.html
```

## Troubleshooting

### Build Failures
Check GitHub Actions tab for detailed logs. Common issues:
- Invalid HTML syntax in samples
- Missing Python dependencies
- GitHub Pages configuration

### Missing Samples
Ensure files are:
- In `/samples/` directory
- Have `.html` extension
- Contain valid HTML

### Preview Issues
Sample previews use iframes. Ensure your HTML:
- Doesn't block iframe embedding
- Uses relative paths for assets
- Has responsive design

## Technical Details

### Automation Scripts
- **Python 3.9+** required
- Pure Python, no external dependencies
- HTML parsing with regex (lightweight)
- File system operations only

### GitHub Actions
- Runs on `ubuntu-latest`
- Uses standard GitHub Actions
- Deploys via `peaceiris/actions-gh-pages`
- Creates issues via GitHub API

### Performance
- Processes any number of samples
- Generates previews with CSS scaling
- Optimized for GitHub Pages hosting
- RSS limited to 20 most recent items

## Best Practices

1. **File Naming**: Use descriptive names like `sample-1-minimal.html`
2. **Self-Contained**: Include all CSS/JS inline for portability  
3. **Responsive**: Design works on mobile and desktop
4. **Semantic HTML**: Proper title and meta tags
5. **Lightweight**: Keep file sizes reasonable

## Contributing

The automation is designed to be minimal and maintainable. When adding features:
- Keep Python scripts simple
- Maintain backward compatibility
- Test with various sample formats
- Update documentation