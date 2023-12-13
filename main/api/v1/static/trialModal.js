function openModal(id) {
    var modal = document.getElementById(id);
    if (modal) {
      modal.style.display = "block";
    }
  }
  
  function closeModal(id) {
    var modal = document.getElementById(id);
    if (modal) {
      modal.style.display = "none";
    }
  }
  
  document.getElementById('btn1').addEventListener('click', function() {
    openModal('modal-hotd');
  });
  
  self.addEventListener('fetch', event => {
    event.respondWith(async function() {
      const preloadResponse = await event.preloadResponse;
  
      if (preloadResponse) {
        return preloadResponse;
      }
  
      const response = await fetch(event.request);
      return response;
    }());
  
    event.waitUntil(async function() {
      const preloadResponse = await caches.match(event.request);
      if (!preloadResponse) {
        const response = await fetch(event.request);
        const cache = await caches.open('my-cache');
        cache.put(event.request, response.clone());
      }
    }());
  });
  