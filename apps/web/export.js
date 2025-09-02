// Export functionality for Scenestealer Engine
// Handles exporting complete HTML files and theme configurations

/**
 * Generates a complete HTML file with current theme tokens applied
 * @param {Object} tokens - Current theme tokens
 * @param {Object} sections - Current section configuration
 * @returns {string} Complete HTML document
 */
function generateCompleteHTML(tokens, sections) {
  const cssVariables = `
  :root {
    --color-primary: ${tokens.colors.primary};
    --color-bg: ${tokens.colors.bg};
    --color-fg: ${tokens.colors.fg};
    --color-accent: ${tokens.colors.accent};
    --radius: ${tokens.radii}px;
    --shadow: ${getShadowValue(tokens.shadow)};
    --font-body: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Noto Sans, Helvetica, Arial;
    --font-heading: ui-sans-serif, system-ui, -apple-system, Segoe UI, Roboto, Noto Sans, Helvetica, Arial;
  }`.trim();

  const baseStyles = `
  * { box-sizing: border-box; }
  html, body { height: 100%; margin: 0; }
  body {
    background: var(--color-bg);
    color: var(--color-fg);
    font-family: var(--font-body);
    line-height: 1.6;
    padding: 20px;
  }
  .section {
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: var(--radius);
    padding: 20px;
    margin-bottom: 14px;
    background: rgba(255,255,255,0.03);
    box-shadow: var(--shadow);
  }
  .section h3 { margin: 0 0 8px 0; color: var(--color-fg); }
  .hero {
    padding: 40px;
    text-align: center;
    background: linear-gradient(135deg, rgba(76,139,245,0.1), rgba(139,92,246,0.1));
  }
  .cta { display: flex; gap: 10px; justify-content: center; margin-top: 14px; }
  .btn {
    background: var(--color-primary);
    color: white;
    border: none;
    border-radius: var(--radius);
    padding: 12px 20px;
    cursor: pointer;
    font-weight: 600;
    text-decoration: none;
    display: inline-block;
    transition: all 0.2s ease;
  }
  .btn:hover { opacity: 0.9; transform: translateY(-1px); }
  .grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-top: 16px; }
  .card {
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: var(--radius);
    padding: 16px;
    background: rgba(255,255,255,0.05);
  }
  .card strong { color: var(--color-primary); display: block; margin-bottom: 6px; }
  .tiers { display: grid; grid-template-columns: repeat(auto-fit, minmax(200px, 1fr)); gap: 16px; margin-top: 16px; }
  .tier {
    border: 1px solid rgba(255,255,255,0.1);
    border-radius: var(--radius);
    padding: 20px;
    text-align: center;
    background: rgba(255,255,255,0.05);
  }
  .tier .name { font-weight: 600; font-size: 18px; margin-bottom: 8px; }
  .tier .price { font-size: 24px; color: var(--color-primary); margin-bottom: 16px; }
  details { margin: 8px 0; }
  summary { cursor: pointer; font-weight: 600; padding: 8px 0; }
  .footer {
    display: flex;
    justify-content: space-between;
    align-items: center;
    padding: 20px 0;
    border-top: 1px solid rgba(255,255,255,0.1);
    margin-top: 20px;
    opacity: 0.8;
  }
  .footer a { color: var(--color-primary); text-decoration: none; }
  .footer a:hover { text-decoration: underline; }
  `;

  // Generate section content based on current state
  let sectionsHTML = '';
  
  if (sections.hero) {
    sectionsHTML += `
    <section class="section hero">
      <h3>Aesthetic UI, faster.</h3>
      <p>Start from a great preset, tweak tokens, assemble sections, ship with pro finish.</p>
      <div class="cta">
        <button class="btn primary">Get Started</button>
        <button class="btn">Docs</button>
      </div>
    </section>`;
  }

  if (sections.features) {
    sectionsHTML += `
    <section class="section features">
      <h3>Features</h3>
      <div class="grid">
        <div class="card"><strong>Theme tokens</strong><p>Cohesive styling from a single source of truth.</p></div>
        <div class="card"><strong>Reusable components</strong><p>Cohesive styling from a single source of truth.</p></div>
        <div class="card"><strong>Pro finish</strong><p>Cohesive styling from a single source of truth.</p></div>
        <div class="card"><strong>Export/Pages</strong><p>Cohesive styling from a single source of truth.</p></div>
      </div>
    </section>`;
  }

  if (sections.pricing) {
    sectionsHTML += `
    <section class="section pricing">
      <h3>Pricing</h3>
      <div class="tiers">
        <div class="tier"><div class="name">Starter</div><div class="price">$0/mo</div><button class="btn primary">Choose</button></div>
        <div class="tier"><div class="name">Pro</div><div class="price">$9/mo</div><button class="btn primary">Choose</button></div>
        <div class="tier"><div class="name">Team</div><div class="price">$29/mo</div><button class="btn primary">Choose</button></div>
      </div>
    </section>`;
  }

  if (sections.faq) {
    sectionsHTML += `
    <section class="section faq">
      <h3>FAQ</h3>
      <details><summary>Is this legal?</summary><p>We use style tokens, not copying logos/assets.</p></details>
      <details><summary>Mobile friendly?</summary><p>Yes, preview and edits work on mobile.</p></details>
      <details><summary>Export?</summary><p>Copy HTML or download theme JSON now; ZIP/PR later.</p></details>
    </section>`;
  }

  if (sections.footer) {
    sectionsHTML += `
    <section class="section footer">
      <div class="footer">
        <span>© Scenestealer Engine</span>
        <a href="https://github.com" target="_blank" rel="noreferrer">GitHub</a>
      </div>
    </section>`;
  }

  const completeHTML = `<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1" />
  <title>Exported Design - Scenestealer Engine</title>
  <style>
${cssVariables}

${baseStyles}
  </style>
</head>
<body>
  <div class="container">
${sectionsHTML}
  </div>
</body>
</html>`;

  return completeHTML;
}

/**
 * Gets the CSS shadow value for a given shadow key
 * @param {string} shadowKey - Shadow configuration key
 * @returns {string} CSS shadow value
 */
function getShadowValue(shadowKey) {
  const shadows = {
    none: 'none',
    sm: '0 1px 2px rgba(0,0,0,.25)',
    md: '0 4px 12px rgba(0,0,0,.25)',
    lg: '0 10px 30px rgba(0,0,0,.35)'
  };
  return shadows[shadowKey] || shadows.sm;
}

/**
 * Downloads a file with the given content
 * @param {string} content - File content
 * @param {string} filename - Name of the file to download
 * @param {string} mimeType - MIME type of the file
 */
function downloadFile(content, filename, mimeType = 'text/html') {
  const blob = new Blob([content], { type: mimeType });
  const url = URL.createObjectURL(blob);
  const a = document.createElement('a');
  a.href = url;
  a.download = filename;
  a.click();
  URL.revokeObjectURL(url);
}

/**
 * Exports the current design as both HTML and theme JSON files
 * @param {Object} tokens - Current theme tokens
 * @param {Object} sections - Current section configuration
 */
function exportCurrentDesign(tokens, sections) {
  // Generate and download HTML file
  const html = generateCompleteHTML(tokens, sections);
  downloadFile(html, 'scenestealer-design.html', 'text/html');
  
  // Generate and download theme JSON file
  const themeJson = JSON.stringify({ 
    tokens, 
    sections,
    exportedAt: new Date().toISOString(),
    generator: 'Scenestealer Engine'
  }, null, 2);
  downloadFile(themeJson, 'scenestealer-theme.json', 'application/json');
  
  // Show success message
  if (typeof alert !== 'undefined') {
    alert('Design exported! Check your downloads for scenestealer-design.html and scenestealer-theme.json');
  }
}

// Export functions for use in app.js
if (typeof module !== 'undefined' && module.exports) {
  module.exports = { generateCompleteHTML, downloadFile, exportCurrentDesign };
} else if (typeof window !== 'undefined') {
  window.ScenestealerExport = { generateCompleteHTML, downloadFile, exportCurrentDesign };
}