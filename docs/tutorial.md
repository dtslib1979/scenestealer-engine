# SceneStealer Engine Tutorial

Learn how to use SceneStealer Engine to create beautiful, cohesive designs quickly.

## Getting Started

### 1. Open the Editor
Visit the [SceneStealer Editor](../editor/) to start creating.

### 2. Choose a Preset
Start with a preset theme:
- **Default**: Balanced dark theme with blue accents
- **Minimal**: Clean, light theme with subtle shadows
- **Vibrant**: High-contrast theme with bold colors

### 3. Customize Tokens
Adjust design tokens to match your vision:
- **Colors**: Primary, background, text, accent
- **Border Radius**: From sharp to rounded
- **Shadows**: None to dramatic

### 4. Select Sections
Toggle sections on/off:
- **Hero**: Main header with call-to-action
- **Features**: Grid of feature highlights  
- **Pricing**: Pricing tiers
- **FAQ**: Frequently asked questions
- **Footer**: Site footer with links

### 5. Export Your Design
- **Export Design**: Download complete HTML + theme JSON
- **Copy HTML**: Copy to clipboard for immediate use
- **Download Theme**: Save theme tokens as JSON

## Design Philosophy

### Token-Based Design
SceneStealer uses design tokens for consistency:

```css
:root {
  --primary: #4c8bf5;    /* Primary brand color */
  --bg: #0f1115;         /* Background color */
  --ink: #e6e8ee;        /* Text color */
  --accent: #8b5cf6;     /* Accent color */
  --radius: 10px;        /* Border radius */
  --shadow: sm;          /* Shadow intensity */
}
```

All components use these tokens, ensuring visual cohesion.

### Section-Based Layout
Build pages by combining sections:
- Each section has consistent spacing and typography
- Sections adapt to your chosen tokens
- Mix and match for custom layouts

## Advanced Usage

### Custom Tokens
Edit the exported HTML to add custom tokens:

```css
:root {
  --custom-gradient: linear-gradient(135deg, var(--primary), var(--accent));
  --custom-spacing: 2rem;
}
```

### Component Variations
Modify exported HTML to create variations:

```html
<!-- Standard button -->
<button class="btn">Click me</button>

<!-- Accent button -->  
<button class="btn" style="background: var(--accent)">Special</button>

<!-- Ghost button -->
<button class="btn" style="background: transparent; border: 1px solid var(--primary); color: var(--primary)">Ghost</button>
```

### Responsive Design
All exports are mobile-first responsive:

```css
@media (max-width: 640px) {
  .hero h1 { font-size: 32px; }
  .grid { grid-template-columns: 1fr; }
}
```

## Integration Workflows

### Blog Integration
1. Export your design
2. Extract sections you need
3. Integrate with your blog template
4. Use tokens for theme consistency

### GitHub Pages
1. Export complete HTML
2. Add to your repository
3. Enable GitHub Pages
4. Your design is live!

### CMS Integration
1. Export sections individually
2. Convert to your CMS's template format
3. Map tokens to CMS theme variables
4. Apply across your site

## Tips & Tricks

### Color Harmony
- Use the primary color for actions and links
- Use the accent sparingly for highlights
- Keep text colors high-contrast for accessibility

### Spacing Consistency
- The engine uses consistent spacing patterns
- Sections have 60px vertical padding
- Cards have 24px internal padding
- Maintain these ratios for visual harmony

### Typography Scale
The built-in scale works well:
- H1: 48px (mobile: 32px)
- H2: 32px (mobile: 24px)  
- H3: 24px (mobile: 20px)
- Body: 15px with 1.6 line-height

### Shadow Usage
- `sm`: Subtle lift for cards
- `md`: Medium shadow for dropdowns
- `lg`: Strong shadow for modals
- Use consistently across similar elements

## Common Patterns

### Call-to-Action Sections
```html
<section class="section cta">
  <div class="container">
    <h2>Ready to get started?</h2>
    <p>Join thousands of users already using our platform.</p>
    <button class="btn">Sign Up Free</button>
  </div>
</section>
```

### Feature Grids
```html
<div class="grid">
  <div class="card">
    <h3>Feature Name</h3>
    <p>Feature description here.</p>
  </div>
  <!-- Repeat for more features -->
</div>
```

### Pricing Tables
```html
<div class="tiers">
  <div class="tier">
    <div class="name">Plan Name</div>
    <div class="price">$X/mo</div>
    <button class="btn primary">Choose Plan</button>
  </div>
</div>
```

## Best Practices

### Accessibility
- Maintain color contrast ratios
- Use semantic HTML structure
- Include proper ARIA labels
- Test with screen readers

### Performance
- Inline critical CSS
- Minimize HTTP requests  
- Optimize images
- Use system fonts when possible

### Maintenance
- Document your token choices
- Keep a style guide
- Test across devices
- Version your themes

## Troubleshooting

### Colors Not Applying
- Check CSS variable syntax
- Ensure tokens are defined in `:root`
- Verify no typos in variable names

### Layout Issues  
- Check grid container structure
- Verify responsive breakpoints
- Test on various screen sizes

### Export Problems
- Ensure modern browser
- Check browser console for errors
- Try refreshing and re-exporting

## Getting Help

- Check the [Archive](../archive.html) for examples
- Review exported HTML for reference patterns
- Open browser dev tools to inspect styles
- File issues on GitHub for bugs