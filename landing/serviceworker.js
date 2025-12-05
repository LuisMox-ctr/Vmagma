const CACHE_NAME = "vmagma-cache-v1";

const urlsToCache = [
  "/", // Inicio
  "/offline/", // Página offline
  // Archivos estáticos
  "/static/landing/images/fondo1.gif",
  "/static/landing/images/eclipse5_logo.png",
  "/static/landing/icons/play-store3.png",
  "/static/landing/icons/app-store1.png",
  "/static/landing/icons/facebook.png",
  "/static/landing/icons/twitterpng.png",
  "/static/landing/icons/instagram.png",
  "/static/landing/icons/youtube.png",
  "/static/landing/juego/GamePromo.zip",
];

// Instalación con manejo de errores
self.addEventListener("install", (event) => {
  console.log("[SW] Instalando Service Worker...");
  event.waitUntil(
    Promise.all(
      urlsToCache.map((url) =>
        fetch(url)
          .then((resp) => {
            if (!resp.ok) throw new Error("No se puede cachear " + url);
            return caches.open(CACHE_NAME).then((cache) => cache.put(url, resp));
          })
          .catch((err) => console.warn("[SW] Error cacheando:", err))
      )
    )
  );
  self.skipWaiting();
});

// Activación
self.addEventListener("activate", (event) => {
  console.log("[SW] Activado");
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(
        keys.map((key) => {
          if (key !== CACHE_NAME) return caches.delete(key);
        })
      )
    )
  );
});

// Fetch: cache first
self.addEventListener("fetch", (event) => {
  event.respondWith(
    caches.match(event.request).then((cached) => {
      if (cached) return cached;
      return fetch(event.request).catch(() => caches.match("/offline/"));
    })
  );
});


