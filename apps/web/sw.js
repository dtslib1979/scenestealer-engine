const CACHE = 'scenestealer-v1'
const ASSETS = [
  './',
  './index.html',
  './style.css',
  './app.js',
  './manifest.webmanifest',
  './presets/linear.json'
]
self.addEventListener('install', e=>{
  e.waitUntil(caches.open(CACHE).then(c=>c.addAll(ASSETS)))
})
self.addEventListener('activate', e=>{
  e.waitUntil(self.clients.claim())
})
self.addEventListener('fetch', e=>{
  e.respondWith(
    caches.match(e.request).then(r=> r || fetch(e.request))
  )
})