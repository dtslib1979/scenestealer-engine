const CACHE = 'scenestealer-v2'
const ASSETS = [
  './',
  './index.html',
  './style.css',
  './app.js',
  './export.js',
  './manifest.webmanifest',
  './presets/default.json',
  './presets/minimal.json',
  './presets/vibrant.json',
  './presets/linear.json'
]

self.addEventListener('install', e => {
  e.waitUntil(
    caches.open(CACHE).then(cache => {
      return cache.addAll(ASSETS).catch(err => {
        console.warn('Cache addAll failed:', err)
        // Try to cache individual files
        return Promise.allSettled(ASSETS.map(url => cache.add(url)))
      })
    })
  )
  self.skipWaiting()
})

self.addEventListener('activate', e => {
  e.waitUntil(
    caches.keys().then(cacheNames => {
      return Promise.all(
        cacheNames.map(cacheName => {
          if (cacheName !== CACHE) {
            return caches.delete(cacheName)
          }
        })
      )
    }).then(() => self.clients.claim())
  )
})

self.addEventListener('fetch', e => {
  e.respondWith(
    caches.match(e.request).then(response => {
      if (response) {
        return response
      }
      return fetch(e.request).catch(() => {
        // Fallback for navigation requests
        if (e.request.mode === 'navigate') {
          return caches.match('./index.html')
        }
      })
    })
  )
})