const $ = (q)=>document.querySelector(q)
const $$ = (q)=>Array.from(document.querySelectorAll(q))

const state = {
  tokens: {
    colors: { primary:'#4c8bf5', bg:'#0f1115', fg:'#e6e8ee', accent:'#8b5cf6' },
    radii: 10,
    shadow: 'sm'
  },
  sections: { hero:true, features:true, pricing:false, faq:false, footer:true }
}

const SHADOWS = {
  none: 'none',
  sm: '0 1px 2px rgba(0,0,0,.25)',
  md: '0 4px 12px rgba(0,0,0,.25)',
  lg: '0 10px 30px rgba(0,0,0,.35)'
}

// LocalStorage persistence functions
function saveState() {
  try {
    localStorage.setItem('scenestealer-tokens', JSON.stringify(state.tokens))
    localStorage.setItem('scenestealer-sections', JSON.stringify(state.sections))
  } catch (e) {
    console.warn('Could not save to localStorage:', e)
  }
}

function loadState() {
  try {
    const savedTokens = localStorage.getItem('scenestealer-tokens')
    const savedSections = localStorage.getItem('scenestealer-sections')
    
    if (savedTokens) {
      state.tokens = { ...state.tokens, ...JSON.parse(savedTokens) }
    }
    if (savedSections) {
      state.sections = { ...state.sections, ...JSON.parse(savedSections) }
    }
  } catch (e) {
    console.warn('Could not load from localStorage:', e)
  }
}

function applyTokens(){
  const r = document.documentElement
  r.style.setProperty('--color-primary', state.tokens.colors.primary)
  r.style.setProperty('--color-bg', state.tokens.colors.bg)
  r.style.setProperty('--color-fg', state.tokens.colors.fg)
  r.style.setProperty('--color-accent', state.tokens.colors.accent)
  r.style.setProperty('--radius', state.tokens.radii + 'px')
  r.style.setProperty('--shadow', SHADOWS[state.tokens.shadow] || SHADOWS.sm)
  saveState()
  render()
}

function render(){
  const v = $('#preview')
  v.innerHTML = ''

  if (state.sections.hero) v.appendChild(hero())
  if (state.sections.features) v.appendChild(features())
  if (state.sections.pricing) v.appendChild(pricing())
  if (state.sections.faq) v.appendChild(faq())
  if (state.sections.footer) v.appendChild(footer())
}

function hero(){
  const el = section('hero')
  el.innerHTML = `
    <h3>Aesthetic UI, faster.</h3>
    <p>Start from a great preset, tweak tokens, assemble sections, ship with pro finish.</p>
    <div class="cta">
      <button class="btn primary">Get Started</button>
      <button class="btn">Docs</button>
    </div>
  `
  return el
}
function features(){
  const el = section('features')
  el.innerHTML = `
    <h3>Features</h3>
    <div class="grid">
      ${['Theme tokens','Reusable components','Pro finish','Export/Pages'].map(t=>`
        <div class="card">
          <strong>${t}</strong>
          <p style="margin:6px 0 0 0">Cohesive styling from a single source of truth.</p>
        </div>`).join('')}
    </div>`
  return el
}
function pricing(){
  const el = section('pricing')
  el.innerHTML = `
    <h3>Pricing</h3>
    <div class="tiers">
      ${['Starter','Pro','Team'].map((t,i)=>`
        <div class="tier">
          <div class="name">${t}</div>
          <div class="price">${i===0?'$0':i===1?'$9':'$29'}/mo</div>
          <button class="btn primary">Choose</button>
        </div>`).join('')}
    </div>`
  return el
}
function faq(){
  const el = section('faq')
  el.innerHTML = `
    <h3>FAQ</h3>
    ${[ ['Is this legal?','We use style tokens, not copying logos/assets.'],
        ['Mobile friendly?','Yes, preview and edits work on mobile.'],
        ['Export?','Copy HTML or download theme JSON now; ZIP/PR later.'] ]
        .map(([q,a])=>`<details><summary>${q}</summary><p>${a}</p></details>`).join('')}
  `
  return el
}
function footer(){
  const el = section('footer')
  el.innerHTML = `
    <div class="footer">
      <span>© Scenestealer Engine</span>
      <a href="https://github.com" target="_blank" rel="noreferrer">GitHub</a>
    </div>`
  return el
}
function section(cls){
  const el = document.createElement('section')
  el.className = `section ${cls}`
  return el
}

// UI wiring
$('#loadPreset').addEventListener('click', async ()=>{
  const name = $('#presetSelect').value
  const res = await fetch(`./presets/${name}.json`)
  const json = await res.json()
  state.tokens = json.tokens || state.tokens
  
  // Update UI inputs to reflect loaded preset
  $('#colorPrimary').value = state.tokens.colors.primary
  $('#colorBg').value = state.tokens.colors.bg
  $('#colorFg').value = state.tokens.colors.fg
  $('#colorAccent').value = state.tokens.colors.accent
  $('#radius').value = state.tokens.radii
  $('#shadow').value = state.tokens.shadow
  
  applyTokens()
})
$('#applyTheme').addEventListener('click', ()=>{
  state.tokens.colors.primary = $('#colorPrimary').value
  state.tokens.colors.bg = $('#colorBg').value
  state.tokens.colors.fg = $('#colorFg').value
  state.tokens.colors.accent = $('#colorAccent').value
  state.tokens.radii = +$('#radius').value
  state.tokens.shadow = $('#shadow').value
  applyTokens()
})
$$('.sectionToggle').forEach(cb=>{
  cb.addEventListener('change', e=>{
    const id = e.target.dataset.id
    state.sections[id] = e.target.checked
    saveState()
    render()
  })
})

$('#toggleDark').addEventListener('change', e=>{
  if(e.target.checked){
    state.tokens.colors.bg = '#0a0c10'
    state.tokens.colors.fg = '#ffffff'
  }else{
    state.tokens.colors.bg = $('#colorBg').value
    state.tokens.colors.fg = $('#colorFg').value
  }
  applyTokens()
})
$('#toggleBaseline').addEventListener('change', e=>{
  document.body.classList.toggle('baseline', e.target.checked)
})
$('#toggleHiContrast').addEventListener('change', e=>{
  document.body.classList.toggle('high-contrast', e.target.checked)
})
$('#toggleReduceMotion').addEventListener('change', e=>{
  document.body.classList.toggle('reduce-motion', e.target.checked)
})

$('#downloadTheme').addEventListener('click', ()=>{
  const blob = new Blob([JSON.stringify({tokens:state.tokens}, null, 2)], {type:'application/json'})
  const a = document.createElement('a'); a.href = URL.createObjectURL(blob); a.download = 'theme.json'; a.click()
  URL.revokeObjectURL(a.href)
})

$('#exportDesign').addEventListener('click', ()=>{
  if (window.ScenestealerExport) {
    window.ScenestealerExport.exportCurrentDesign(state.tokens, state.sections)
  } else {
    alert('Export functionality not loaded. Please refresh the page.')
  }
})
$('#copyHTML').addEventListener('click', ()=>{
  const html = document.documentElement.outerHTML
  navigator.clipboard.writeText(html).then(()=>alert('HTML copied to clipboard'))
})

function detectPWA(){
  const isStandalone = window.matchMedia('(display-mode: standalone)').matches || window.navigator.standalone
  $('#pwaStatus').textContent = isStandalone ? 'yes' : 'no'
}

function initializeUI() {
  // Load saved state
  loadState()
  
  // Update UI controls to reflect loaded state
  $('#colorPrimary').value = state.tokens.colors.primary
  $('#colorBg').value = state.tokens.colors.bg
  $('#colorFg').value = state.tokens.colors.fg
  $('#colorAccent').value = state.tokens.colors.accent
  $('#radius').value = state.tokens.radii
  $('#shadow').value = state.tokens.shadow
  
  // Update section toggles
  $$('.sectionToggle').forEach(cb => {
    const id = cb.dataset.id
    if (state.sections.hasOwnProperty(id)) {
      cb.checked = state.sections[id]
    }
  })
}

initializeUI()
applyTokens()
detectPWA()
render()