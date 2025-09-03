# 🎭 SceneStealer Engine — Archive + Editor

**Extract the vibe · Assemble the site · Finish like a pro**

Automated design sample archive with integrated editor. Upload HTML samples → automatic gallery generation → instant preview & editing.

## ✨ Features

- 🎨 **Design Editor**: Token-based design system with live preview
- 📁 **Automatic Archive**: Upload samples, get instant gallery
- 🚀 **GitHub Actions**: Automated processing and deployment  
- 📱 **Responsive**: Works perfectly on mobile and desktop
- 🔄 **RSS Integration**: Blog-ready feeds for easy sharing
- 💾 **Export Ready**: Download HTML + JSON themes

## 🚀 Quick Start

### For Users (Browse & Edit)
1. Visit: `https://dtslib1979.github.io/scenestealer-engine/`
2. Browse the [Archive](https://dtslib1979.github.io/scenestealer-engine/archive.html)
3. Click "Edit" on any sample to customize
4. Export your customized design

### For Contributors (Add Samples)
1. Create your HTML sample file
2. Add it to `/samples/` directory
3. Commit & push to main branch
4. Archive updates automatically!

## 📂 Folder Structure

```
/scenestealer-engine/
├── samples/          ← HTML samples (triggers automation)
├── editor/           ← SceneStealer Engine (design tool)
├── docs/            ← Documentation & tutorials
├── web/             ← GitHub Pages site
│   ├── index.html   ← Main homepage
│   ├── archive.html ← Auto-generated gallery
│   ├── rss.xml      ← RSS feed
│   └── sitemap.xml  ← SEO sitemap
├── scripts/         ← Python automation
└── .github/workflows/ ← GitHub Actions
```

## 🔄 How It Works

1. **Upload Sample**: Add HTML file to `/samples/`
2. **Auto Processing**: GitHub Actions detects the change
3. **Generate Archive**: Creates gallery with previews
4. **Update Homepage**: Adds latest sample to main page
5. **Create Feeds**: Generates RSS and sitemap
6. **Deploy**: Everything goes live on GitHub Pages
7. **Notify**: Creates GitHub Issue with deployment info

## 📋 Sample Format

```html
<!doctype html>
<html lang="en">
<head>
  <title>Your Sample Name - Scenestealer Engine</title>
  <meta name="description" content="Brief description">
  <style>
    /* Your CSS here - inline recommended */
  </style>
</head>
<body>
  <!-- Your design here -->
</body>
</html>
```

## 🛠️ Documentation

- **[Archive Workflow Guide](docs/archive-workflow.md)** - Detailed automation docs
- **[Tutorial](docs/tutorial.md)** - How to use the editor
- **[Contributing](#-contributing)** - Add your own samples

## 🌐 Live Links

- **[Main Site](https://dtslib1979.github.io/scenestealer-engine/)**
- **[Sample Archive](https://dtslib1979.github.io/scenestealer-engine/archive.html)**
- **[Design Editor](https://dtslib1979.github.io/scenestealer-engine/editor/)**
- **[RSS Feed](https://dtslib1979.github.io/scenestealer-engine/rss.xml)**

## 💡 Use Cases

### For Designers
- Upload your HTML designs for showcase
- Get automatic gallery generation
- Share via RSS feeds to your blog

### For Developers  
- Browse design samples for inspiration
- Export HTML + CSS for your projects
- Use as starting points for new designs

### For Content Creators
- Integrate RSS feed with your blog
- Auto-generated content for social media
- Beautiful gallery for portfolio sites

## 🤖 Automation Scripts

- **`generate_archive.py`** - Creates sample gallery
- **`update_index.py`** - Updates homepage with latest sample
- **`generate_rss.py`** - Creates RSS feed for blogs
- **`generate_sitemap.py`** - SEO sitemap generation

## 🚀 GitHub Actions

Two workflows handle different scenarios:
- **`build-archive.yml`** - Triggered by sample uploads
- **`pages-deploy.yml`** - Handles other changes

## 📊 Stats & Notifications

The system automatically tracks:
- Total number of samples
- Latest sample information  
- Deploy success/failure notifications
- RSS feed updates

## 🔧 Contributing

### Adding Samples
1. Fork the repository
2. Add your HTML file to `/samples/`
3. Create a pull request
4. Once merged, automation takes over!

### Development
1. Clone the repository
2. Make changes to scripts or workflows
3. Test locally with Python scripts
4. Submit pull request with improvements

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details.

## 🙋‍♂️ Support

- Open [GitHub Issues](https://github.com/dtslib1979/scenestealer-engine/issues) for bugs
- Check [Discussions](https://github.com/dtslib1979/scenestealer-engine/discussions) for help
- Review [Documentation](docs/) for detailed guides

---

**Built with ❤️ using vanilla JavaScript, Python, and GitHub Actions**