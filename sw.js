/* NT Nursing service worker: mở được khi mất mạng.
   Đổi VERSION mỗi lần cập nhật phần mềm. */
var VERSION = "2026-11-12a";
var SHELL = "nt-shell-" + VERSION;
var DOCS = "nt-docs";
var SHELL_FILES = [
  "./", "index.html", "config.js", "nt-firebase.js", "manifest.webmanifest", "logo.png",
  "icons/icon-192.png", "icons/icon-512.png",
  "vendor/firebase-app-compat.js", "vendor/firebase-auth-compat.js", "vendor/firebase-firestore-compat.js"
];

self.addEventListener("install", function(e){
  e.waitUntil(caches.open(SHELL).then(function(c){ return c.addAll(SHELL_FILES); }).then(function(){ return self.skipWaiting(); }));
});
self.addEventListener("activate", function(e){
  e.waitUntil(caches.keys().then(function(keys){
    return Promise.all(keys.filter(function(k){ return k.indexOf("nt-shell-")===0 && k!==SHELL; }).map(function(k){ return caches.delete(k); }));
  }).then(function(){ return self.clients.claim(); }));
});

self.addEventListener("fetch", function(e){
  var req = e.request;
  if(req.method!=="GET") return;
  var url = new URL(req.url);
  if(url.origin!==self.location.origin) return; /* Firebase tự lo phần đồng bộ */

  /* Tài liệu: lấy trong máy trước, chưa có thì tải và lưu lại */
  if(url.pathname.indexOf("/tai-lieu/")>=0){
    e.respondWith(caches.open(DOCS).then(function(c){
      return c.match(req, {ignoreSearch:true}).then(function(hit){
        if(hit) return hit;
        return fetch(req).then(function(res){ if(res.ok) c.put(req, res.clone()); return res; });
      });
    }));
    return;
  }

  /* Trang chính: ưu tiên bản mới trên mạng (chờ tối đa 4 giây), mất mạng thì dùng bản đã lưu */
  if(req.mode==="navigate" || url.pathname.endsWith("/index.html")){
    e.respondWith(new Promise(function(resolve){
      var done = false;
      var fallback = function(){ if(done) return; done = true; caches.match("index.html", {ignoreSearch:true}).then(function(r){ resolve(r || caches.match("./")); }); };
      var t = setTimeout(fallback, 4000);
      fetch(req).then(function(res){
        if(done) return;
        clearTimeout(t); done = true;
        if(res.ok){ var cp = res.clone(); caches.open(SHELL).then(function(c){ c.put("index.html", cp); }); }
        resolve(res);
      }).catch(function(){ clearTimeout(t); fallback(); });
    }));
    return;
  }

  /* Tệp khác của phần mềm: dùng bản đã lưu, cập nhật ngầm */
  e.respondWith(caches.match(req, {ignoreSearch:true}).then(function(hit){
    var net = fetch(req).then(function(res){
      if(res.ok){ var cp = res.clone(); caches.open(SHELL).then(function(c){ c.put(req, cp); }); }
      return res;
    }).catch(function(){ return hit; });
    return hit || net;
  }));
});
