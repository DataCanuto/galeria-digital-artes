// ============================================
// SERVICE WORKER - Cache Offline + Performance
// ============================================

const CACHE_NAME = 'galeria-digital-v1';
const ASSETS_TO_CACHE = [
    '/',
    '/catalog_mobile/index.html',
    '/assets/css/style.css',
];

// ============================================
// INSTALAÇÃO - Pré-cacheia assets críticos
// ============================================
self.addEventListener('install', event => {
    console.log('[Service Worker] Instalando...');
    
    event.waitUntil(
        caches.open(CACHE_NAME).then(cache => {
            console.log('[Service Worker] Cacheando assets críticos');
            return cache.addAll(ASSETS_TO_CACHE);
        }).catch(err => {
            console.log('[Service Worker] Erro ao cachear:', err);
        })
    );
    
    self.skipWaiting();
});

// ============================================
// ATIVAÇÃO - Remove caches antigas
// ============================================
self.addEventListener('activate', event => {
    console.log('[Service Worker] Ativando...');
    
    event.waitUntil(
        caches.keys().then(cacheNames => {
            return Promise.all(
                cacheNames.map(cacheName => {
                    if (cacheName !== CACHE_NAME) {
                        console.log('[Service Worker] Removendo cache antiga:', cacheName);
                        return caches.delete(cacheName);
                    }
                })
            );
        })
    );
    
    self.clients.claim();
});

// ============================================
// FETCH - Estratégia Network-First para imagens
// ============================================
self.addEventListener('fetch', event => {
    const { request } = event;
    
    // HTML e CSS: Network-First
    if (request.destination === 'document' || 
        request.destination === 'style' || 
        request.destination === 'script') {
        
        event.respondWith(
            fetch(request)
                .then(response => {
                    // Cacheia resposta bem-sucedida
                    if (response.ok) {
                        const cache = caches.open(CACHE_NAME);
                        cache.then(c => c.put(request, response.clone()));
                    }
                    return response;
                })
                .catch(() => {
                    // Se falhar, usa cache
                    return caches.match(request);
                })
        );
    }
    
    // Imagens: Cache-First (offline + performance)
    else if (request.destination === 'image') {
        event.respondWith(
            caches.match(request)
                .then(response => {
                    // Se está em cache, retorna
                    if (response) {
                        return response;
                    }
                    
                    // Senão, busca na rede
                    return fetch(request)
                        .then(response => {
                            // Se resposta é válida, cacheia
                            if (response.ok) {
                                const cache = caches.open(CACHE_NAME);
                                cache.then(c => c.put(request, response.clone()));
                            }
                            return response;
                        })
                        .catch(() => {
                            // Se falhar, retorna imagem placeholder
                            return new Response(
                                '<svg width="100" height="100" xmlns="http://www.w3.org/2000/svg">' +
                                '<rect fill="#ddd" width="100" height="100"/>' +
                                '<text x="50" y="50" text-anchor="middle" dy=".3em" font-size="12" fill="#999">' +
                                'Offline</text></svg>',
                                { headers: { 'Content-Type': 'image/svg+xml' } }
                            );
                        });
                })
        );
    }
    
    // Outras requisições: Network-First
    else {
        event.respondWith(
            fetch(request)
                .then(response => response)
                .catch(() => caches.match(request))
        );
    }
});

// ============================================
// LIMPEZA - Remove entradas de cache muito antigas
// ============================================
self.addEventListener('message', event => {
    if (event.data && event.data.type === 'SKIP_WAITING') {
        self.skipWaiting();
    }
});

console.log('[Service Worker] Carregado com sucesso');
