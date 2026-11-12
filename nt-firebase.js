/* NT Nursing — lớp nối Firebase (đăng nhập, Firestore lưu offline, tự đồng bộ).
   Thay thế window.claude.use("db"/"user") của bản artifact bằng Firestore,
   nên phần giao diện chính giữ nguyên. */
(function(){
  "use strict";
  var CFG = window.NT_FIREBASE_CONFIG;
  var ADMIN_EMAILS = (window.NT_ADMIN_EMAILS||[]).map(function(e){ return String(e).toLowerCase(); });
  var LEGACY_URL = window.NT_LEGACY_URL || "";
  var ROLE_LABEL = {admin:"Quản trị", editor:"Được sửa", viewer:"Chỉ xem"};
  var DEPTS = ["Phòng Điều dưỡng","Cấp cứu - HSTC & Chống độc","Khám bệnh","Nội Tổng quát","Nội Tiêu hóa","Phụ Sản","Ngoại Tổng quát","Ngoại Chấn thương","Liên Chuyên khoa","Nhi","Khoa Truyền nhiễm","PT - GMHS","YHCT - PHCN","Thận Nhân tạo","Xét nghiệm","CĐHA - TDCN","Dược","Kiểm soát nhiễm khuẩn","Tổ Tiêm chủng","Khác"];

  firebase.initializeApp(CFG);
  var auth = firebase.auth();
  var fs = firebase.firestore();
  /* Chỉ dùng khi thử nghiệm trên máy lập trình: http://localhost/?emu=1 */
  if((location.hostname==="localhost"||location.hostname==="127.0.0.1") && /[?&]emu=1/.test(location.search)){
    auth.useEmulator("http://127.0.0.1:9099");
    fs.useEmulator("127.0.0.1", 8085);
  }
  var persistenceOK = true;
  fs.enablePersistence({synchronizeTabs:true}).catch(function(err){
    persistenceOK = false;
    console.warn("Không bật được lưu offline:", err && err.code);
  });

  /* ------------------------------------------------------------ */
  /* Giao diện cổng đăng nhập + chip trạng thái đồng bộ            */
  /* ------------------------------------------------------------ */
  var css = document.createElement("style");
  css.textContent = [
    "#nt-gate{position:fixed;inset:0;z-index:500;background:var(--bg,#f5f6f2);color:var(--text,#1b241f);display:flex;align-items:center;justify-content:center;padding:16px;overflow-y:auto}",
    "#nt-gate .box{width:min(400px,100%);background:var(--surface,#fff);border:1px solid var(--border,#dde3d8);border-radius:14px;padding:22px 20px;box-shadow:var(--shadow)}",
    "#nt-gate img.logo{display:block;height:44px;margin:0 auto 10px}",
    "#nt-gate h1{font-size:18px;text-align:center;margin:0 0 4px}",
    "#nt-gate .sub{font-size:12.5px;color:var(--text-muted,#5c6b60);text-align:center;margin-bottom:16px}",
    "#nt-gate label{display:block;font-size:11.5px;font-weight:700;color:var(--text-muted);text-transform:uppercase;letter-spacing:.03em;margin:10px 0 4px}",
    "#nt-gate input,#nt-gate select{width:100%;padding:10px 11px;border-radius:9px;border:1px solid var(--border);background:var(--bg);color:var(--text);font-size:15px;box-sizing:border-box}",
    "#nt-gate button{width:100%;margin-top:14px;padding:11px;border-radius:9px;border:1px solid var(--accent,#0d6e5f);background:var(--accent,#0d6e5f);color:var(--accent-contrast,#fff);font-weight:700;font-size:14.5px;cursor:pointer}",
    "#nt-gate button.ghost{background:transparent;color:var(--accent)}",
    "#nt-gate .tabs2{display:flex;gap:6px;margin-bottom:6px}#nt-gate .tabs2 button{margin-top:0;padding:8px;font-size:13px}",
    "#nt-gate .msg{font-size:13px;margin-top:12px;padding:9px 11px;border-radius:9px;background:var(--warn-soft,#fbecd4);color:var(--warn,#9a5b06)}",
    "#nt-gate .msg.err{background:var(--danger-soft,#fbe6e3);color:var(--danger,#b23327)}",
    "#nt-gate .msg.ok{background:var(--ok-soft,#e2f5ea);color:var(--ok,#187a54)}",
    "#nt-gate .note{font-size:12px;color:var(--text-muted);margin-top:14px;line-height:1.5}",
    "#nt-sync{position:fixed;right:12px;bottom:calc(12px + env(safe-area-inset-bottom,0px));z-index:150;display:flex;align-items:center;gap:6px;padding:6px 11px;border-radius:999px;border:1px solid var(--border);background:var(--surface);color:var(--text-muted);font-size:12px;font-weight:600;box-shadow:var(--shadow);cursor:pointer;max-width:calc(100vw - 24px)}",
    "#nt-sync .d{width:8px;height:8px;border-radius:50%;background:var(--ok,#187a54);flex:none}",
    "#nt-sync.off .d{background:var(--warn,#9a5b06)}#nt-sync.err .d{background:var(--danger,#b23327)}",
    "#nt-sync .t{white-space:nowrap;overflow:hidden;text-overflow:ellipsis}",
    "#nt-panel{position:fixed;inset:0;z-index:400;background:rgba(10,15,12,.45);display:flex;align-items:center;justify-content:center;padding:16px}",
    "#nt-panel .pn{background:var(--surface);color:var(--text);border-radius:14px;width:min(620px,100%);max-height:88vh;overflow-y:auto;box-shadow:var(--shadow)}",
    "#nt-panel .ph{display:flex;align-items:center;justify-content:space-between;padding:14px 16px;border-bottom:1px solid var(--border);position:sticky;top:0;background:var(--surface)}",
    "#nt-panel .ph h3{font-size:15px;margin:0}",
    "#nt-panel .pb{padding:14px 16px;font-size:13px;display:flex;flex-direction:column;gap:10px}",
    "#nt-panel .row{display:flex;gap:8px;align-items:center;flex-wrap:wrap;padding:8px 0;border-bottom:1px dashed var(--border)}",
    "#nt-panel .row .who{flex:1 1 200px;min-width:0}#nt-panel .row .who b{display:block;overflow-wrap:anywhere}",
    "#nt-panel .row .who span{font-size:11.5px;color:var(--text-muted)}",
    "#nt-panel select,#nt-panel input[type=file]{padding:6px 8px;border-radius:8px;border:1px solid var(--border);background:var(--bg);color:var(--text);max-width:100%}",
    "#nt-panel .bar{height:8px;border-radius:5px;background:var(--surface-2);overflow:hidden}#nt-panel .bar span{display:block;height:100%;background:var(--accent);width:0}",
    "#nt-panel h4{margin:8px 0 0;font-size:13px}",
    "#nt-panel .hint{font-size:12px;color:var(--text-muted)}"
  ].join("\n");
  document.head.appendChild(css);

  function h(s){ return String(s==null?"":s).replace(/[&<>"']/g,function(c){return {"&":"&amp;","<":"&lt;",">":"&gt;",'"':"&quot;","'":"&#39;"}[c];}); }
  var gate = document.createElement("div"); gate.id = "nt-gate";
  document.body.appendChild(gate);
  function showGate(html){ gate.innerHTML = '<div class="box"><img class="logo" src="logo.png" alt="Logo BVĐK Nhật Tân"><h1>NT Nursing</h1><div class="sub">Phòng Điều dưỡng, BVĐK Nhật Tân</div>'+html+'</div>'; gate.hidden = false; }
  function hideGate(){ gate.hidden = true; gate.innerHTML = ""; }
  showGate('<div class="sub">Đang mở…</div>');

  var mode = "login";
  function viErr(e){
    var c = (e && e.code) || "";
    var m = {
      "auth/invalid-email":"Email không đúng định dạng.",
      "auth/user-not-found":"Không có tài khoản với email này.",
      "auth/wrong-password":"Sai mật khẩu.",
      "auth/invalid-credential":"Email hoặc mật khẩu không đúng.",
      "auth/invalid-login-credentials":"Email hoặc mật khẩu không đúng.",
      "auth/too-many-requests":"Đăng nhập sai nhiều lần, vui lòng thử lại sau ít phút.",
      "auth/network-request-failed":"Không có mạng. Lần đăng nhập đầu tiên cần có mạng.",
      "auth/email-already-in-use":"Email này đã có tài khoản, hãy chọn Đăng nhập.",
      "auth/weak-password":"Mật khẩu cần ít nhất 6 ký tự.",
      "auth/api-key-not-valid.-please-pass-a-valid-api-key.":"Cấu hình Firebase (apiKey) chưa đúng, báo Phòng Điều dưỡng.",
      "permission-denied":"Tài khoản không có quyền thực hiện thao tác này."
    }[c];
    return m || ("Lỗi: "+((e&&e.message)||e));
  }
  function loginForm(msg, cls){
    var reg = mode==="register";
    showGate(
      '<div class="tabs2"><button type="button" class="'+(reg?"ghost":"")+'" data-m="login">Đăng nhập</button><button type="button" class="'+(reg?"":"ghost")+'" data-m="register">Tạo tài khoản</button></div>'+
      '<form id="nt-login" autocomplete="on">'+
      (reg?'<label for="nt-name">Họ và tên</label><input id="nt-name" required autocomplete="name">'+
        '<label for="nt-dept">Khoa, phòng</label><select id="nt-dept">'+DEPTS.map(function(d){return '<option>'+h(d)+'</option>';}).join("")+'</select>':'')+
      '<label for="nt-email">Email</label><input id="nt-email" type="email" required autocomplete="username" inputmode="email">'+
      '<label for="nt-pass">Mật khẩu</label><input id="nt-pass" type="password" required minlength="6" autocomplete="'+(reg?"new-password":"current-password")+'">'+
      '<button type="submit">'+(reg?"Tạo tài khoản":"Đăng nhập")+'</button>'+
      (reg?'':'<button type="button" class="ghost" id="nt-forgot">Quên mật khẩu</button>')+
      '</form>'+
      (msg?'<div class="msg '+(cls||"")+'">'+h(msg)+'</div>':'')+
      '<div class="note">'+(reg?'Sau khi tạo, tài khoản chờ Phòng Điều dưỡng duyệt mới xem được dữ liệu.':'Đăng nhập một lần khi có mạng. Sau đó máy này mở được phần mềm cả khi mất mạng; dữ liệu nhập lúc mất mạng tự gửi lên khi có mạng lại.')+'</div>'
    );
    gate.querySelectorAll("[data-m]").forEach(function(b){ b.onclick = function(){ mode = b.getAttribute("data-m"); loginForm(); }; });
    var f = document.getElementById("nt-forgot");
    if(f) f.onclick = function(){
      var em = document.getElementById("nt-email").value.trim();
      if(!em){ loginForm("Nhập email trước rồi bấm Quên mật khẩu.", "err"); return; }
      auth.sendPasswordResetEmail(em).then(function(){ loginForm("Đã gửi thư đặt lại mật khẩu tới "+em+". Kiểm tra hộp thư (cả mục Spam).", "ok"); })
        .catch(function(e){ loginForm(viErr(e), "err"); });
    };
    document.getElementById("nt-login").onsubmit = function(ev){
      ev.preventDefault();
      var em = document.getElementById("nt-email").value.trim(), pw = document.getElementById("nt-pass").value;
      var btn = ev.target.querySelector("button[type=submit]"); btn.disabled = true; btn.textContent = "Đang xử lý…";
      if(reg){
        var nm = document.getElementById("nt-name").value.trim(), dp = document.getElementById("nt-dept").value;
        try{ localStorage.setItem("nt-reg-info", JSON.stringify({name:nm, dept:dp})); }catch(e){}
        auth.createUserWithEmailAndPassword(em, pw).then(function(c){ return c.user.updateProfile({displayName:nm}); })
          .catch(function(e){ loginForm(viErr(e), "err"); });
      } else {
        auth.signInWithEmailAndPassword(em, pw).catch(function(e){ loginForm(viErr(e), "err"); });
      }
    };
  }

  /* ------------------------------------------------------------ */
  /* Ghi dữ liệu: trả kết quả ngay (kể cả khi mất mạng), theo dõi   */
  /* số thay đổi còn chờ gửi lên máy chủ                            */
  /* ------------------------------------------------------------ */
  var pending = 0, lastErr = null;
  function track(p){
    pending++; renderSync();
    p.then(function(){ pending--; renderSync(); }, function(e){
      pending--; lastErr = e; renderSync();
      console.error("Ghi Firestore lỗi", e);
      toast("Không lưu được lên máy chủ: "+viErr(e));
    });
    return Promise.resolve();
  }
  function wrapDoc(ref){
    return {
      id: ref.id, path: ref.path, _ref: ref,
      get: function(o){ return ref.get(o); },
      onSnapshot: function(){ return ref.onSnapshot.apply(ref, arguments); },
      set: function(d,o){ return track(o ? ref.set(clean(d),o) : ref.set(clean(d))); },
      update: function(d){ return track(ref.update(clean(d))); },
      delete: function(){ return track(ref.delete()); },
      collection: function(n){ return wrapCol(ref.collection(n)); }
    };
  }
  function wrapCol(col){
    var w = Object.create(col);
    w.doc = function(id){ return wrapDoc(id===undefined ? col.doc() : col.doc(id)); };
    w.add = function(d){ var r = col.doc(); track(r.set(clean(d))); return Promise.resolve(wrapDoc(r)); };
    w.onSnapshot = function(){ return col.onSnapshot.apply(col, arguments); };
    w.get = function(o){ return col.get(o); };
    return w;
  }
  /* Firestore không nhận giá trị undefined */
  function clean(v){
    if(v===undefined) return null;
    if(Array.isArray(v)) return v.map(clean);
    if(v && typeof v==="object" && Object.getPrototypeOf(v)===Object.prototype){
      var o = {}; Object.keys(v).forEach(function(k){ if(v[k]!==undefined) o[k] = clean(v[k]); }); return o;
    }
    return v;
  }
  var dbAdapter = {
    collection: function(n){ return wrapCol(fs.collection(n)); },
    doc: function(p){ return wrapDoc(fs.doc(p)); },
    raw: fs
  };

  /* ------------------------------------------------------------ */
  /* Phiên đăng nhập và quyền                                       */
  /* ------------------------------------------------------------ */
  var session = null, resolveReady, readyP = new Promise(function(r){ resolveReady = r; });
  function isAdminUser(u){ return !!u && u.emailVerified && ADMIN_EMAILS.indexOf(String(u.email||"").toLowerCase())>=0; }
  function cacheRole(uid, m){ try{ localStorage.setItem("nt-member-"+uid, JSON.stringify(m)); }catch(e){} }
  function cachedRole(uid){ try{ return JSON.parse(localStorage.getItem("nt-member-"+uid)||"null"); }catch(e){ return null; } }

  auth.onAuthStateChanged(function(u){
    if(!u){ session = null; renderSync(); loginForm(); return; }
    if(ADMIN_EMAILS.indexOf(String(u.email||"").toLowerCase())>=0 && !u.emailVerified){ verifyScreen(u); return; }
    if(isAdminUser(u)){ start(u, {role:"admin", name:u.displayName||"Quản trị PĐD", dept:"Phòng Điều dưỡng"}); return; }
    showGate('<div class="sub">Đang kiểm tra quyền truy cập…</div>');
    fs.doc("members/"+u.uid).get().then(function(s){
      if(s.exists){ var m = s.data(); cacheRole(u.uid, m); start(u, m); }
      else requestAccess(u);
    }).catch(function(e){
      var c = cachedRole(u.uid);
      if(c) start(u, c);
      else showGate('<div class="msg err">'+h(viErr(e))+'</div><div class="note">Máy này chưa từng mở phần mềm khi có mạng. Hãy kết nối mạng rồi tải lại trang.</div><button id="nt-retry">Thử lại</button><button class="ghost" id="nt-out">Đăng xuất</button>'), bindRetry();
    });
  });
  function bindRetry(){
    var r = document.getElementById("nt-retry"); if(r) r.onclick = function(){ location.reload(); };
    var o = document.getElementById("nt-out"); if(o) o.onclick = function(){ auth.signOut(); };
  }
  function verifyScreen(u){
    showGate('<div class="msg">Tài khoản quản trị <b>'+h(u.email)+'</b> cần xác minh email một lần.</div>'+
      '<button id="nt-send">Gửi thư xác minh</button><button class="ghost" id="nt-done">Tôi đã bấm link xác minh</button><button class="ghost" id="nt-out">Đăng xuất</button>'+
      '<div class="note">Mở Gmail '+h(u.email)+', tìm thư từ Firebase (xem cả mục Spam), bấm link trong thư, rồi quay lại bấm "Tôi đã bấm link xác minh".</div>');
    document.getElementById("nt-send").onclick = function(){ u.sendEmailVerification().then(function(){ toast("Đã gửi thư xác minh"); }).catch(function(e){ toast(viErr(e)); }); };
    document.getElementById("nt-done").onclick = function(){ u.reload().then(function(){ return u.getIdToken(true); }).then(function(){ if(auth.currentUser.emailVerified) start(auth.currentUser, {role:"admin", name:u.displayName||"Quản trị PĐD", dept:"Phòng Điều dưỡng"}); else toast("Chưa thấy xác minh, thử lại sau vài giây"); }); };
    bindRetry();
  }
  function requestAccess(u){
    var info = {}; try{ info = JSON.parse(localStorage.getItem("nt-reg-info")||"{}"); }catch(e){}
    fs.doc("requests/"+u.uid).set({email:u.email, name:info.name||u.displayName||"", dept:info.dept||"", requestedAt:new Date().toISOString()}, {merge:true}).catch(function(){});
    showGate('<div class="msg">Tài khoản <b>'+h(u.email)+'</b> đã gửi yêu cầu, đang chờ Phòng Điều dưỡng duyệt.</div>'+
      '<button id="nt-retry">Kiểm tra lại</button><button class="ghost" id="nt-out">Đăng xuất</button>'+
      '<div class="note">Khi được duyệt, bấm "Kiểm tra lại" để vào phần mềm.</div>');
    bindRetry();
  }
  function start(u, m){
    session = {uid:u.uid, email:u.email, name:m.name||u.displayName||u.email, dept:m.dept||"", role:m.role||"viewer"};
    if(session.role==="admin") cacheRole(u.uid, m);
    hideGate(); renderSync();
    resolveReady(session);
  }

  /* API giống window.claude của bản artifact, để phần mềm chính chạy không cần sửa */
  window.claude = {
    use: function(name){
      if(name==="db") return readyP.then(function(){ return dbAdapter; });
      if(name==="user") return readyP.then(function(s){
        return { me: function(){ return Promise.resolve({
          id: s.uid, name: s.name, avatarUrl: "icons/icon-192.png",
          isOwner: s.role==="admin", canEdit: s.role==="admin" || s.role==="editor"
        }); } };
      });
      return Promise.resolve(null);
    }
  };

  /* ------------------------------------------------------------ */
  /* Chip trạng thái + bảng tài khoản                               */
  /* ------------------------------------------------------------ */
  var chip = document.createElement("button"); chip.id = "nt-sync"; chip.type = "button";
  chip.innerHTML = '<span class="d"></span><span class="t"></span>';
  document.body.appendChild(chip);
  chip.onclick = openPanel;
  function renderSync(){
    chip.hidden = !session;
    var on = navigator.onLine, t;
    chip.className = on ? (lastErr && pending===0 ? "" : "") : "off";
    if(!on) t = pending ? "Mất mạng · "+pending+" thay đổi chờ gửi" : "Mất mạng · đang dùng dữ liệu đã lưu";
    else t = pending ? "Đang đồng bộ "+pending+" thay đổi…" : "Đã đồng bộ";
    chip.querySelector(".t").textContent = t;
    chip.title = "Tài khoản: "+(session?session.email:"")+" — bấm để xem";
  }
  window.addEventListener("online", renderSync);
  window.addEventListener("offline", renderSync);

  function toast(msg){
    var r = document.getElementById("toast-root") || document.body;
    var d = document.createElement("div"); d.className = "toast"; d.textContent = msg; d.setAttribute("role","status");
    r.appendChild(d); setTimeout(function(){ d.remove(); }, 4200);
  }

  function closePanel(){ var p = document.getElementById("nt-panel"); if(p) p.remove(); }
  function panel(title, body){
    closePanel();
    var p = document.createElement("div"); p.id = "nt-panel";
    p.innerHTML = '<div class="pn" role="dialog" aria-label="'+h(title)+'"><div class="ph"><h3>'+h(title)+'</h3><button type="button" class="iconbtn" id="nt-pclose" aria-label="Đóng" style="font-size:20px;line-height:1">×</button></div><div class="pb">'+body+'</div></div>';
    p.addEventListener("click", function(e){ if(e.target===p) closePanel(); });
    document.body.appendChild(p);
    document.getElementById("nt-pclose").onclick = closePanel;
    return p;
  }

  function openPanel(){
    if(!session) return;
    var adm = session.role==="admin";
    var p = panel("Tài khoản và đồng bộ",
      '<div><b>'+h(session.name)+'</b><br><span class="hint">'+h(session.email)+' · '+h(session.dept)+' · Quyền: '+h(ROLE_LABEL[session.role]||session.role)+'</span></div>'+
      '<div class="hint">'+(navigator.onLine?'Đang có mạng.':'Đang mất mạng.')+' '+(pending?pending+' thay đổi đang chờ gửi lên máy chủ.':'Không có thay đổi nào đang chờ.')+(persistenceOK?'':' <b>Trình duyệt này không lưu offline được</b> (thường do mở 2 cửa sổ cùng lúc hoặc chế độ ẩn danh).')+'</div>'+
      '<h4>Dùng khi mất mạng</h4><div class="hint">Tài liệu PDF đã mở một lần sẽ tự lưu lại trên máy. Muốn mở được mọi tài liệu khi mất mạng thì bấm nút dưới (khoảng 185 MB, nên dùng Wi-Fi).</div>'+
      '<div><button class="btn" id="nt-dl">Tải sẵn tất cả tài liệu</button></div><div class="bar" id="nt-dlbar" hidden><span></span></div><div class="hint" id="nt-dlmsg"></div>'+
      (adm?'<h4>Quản trị</h4><div style="display:flex;gap:8px;flex-wrap:wrap"><button class="btn" id="nt-users">Duyệt và phân quyền tài khoản</button><button class="btn" id="nt-import">Nhập dữ liệu từ bản cũ</button></div>':'')+
      (LEGACY_URL?'<div class="hint">Bản cũ trên Claude: <a href="'+h(LEGACY_URL)+'" target="_blank" rel="noopener">mở bản cũ</a></div>':'')+
      '<div><button class="btn danger" id="nt-logout">Đăng xuất</button></div>');
    document.getElementById("nt-logout").onclick = function(){
      if(pending && !confirm("Còn "+pending+" thay đổi chưa gửi lên máy chủ. Đăng xuất bây giờ có thể mất các thay đổi này. Vẫn đăng xuất?")) return;
      auth.signOut().then(function(){ location.reload(); });
    };
    document.getElementById("nt-dl").onclick = precacheDocs;
    if(adm){
      document.getElementById("nt-users").onclick = openUsers;
      document.getElementById("nt-import").onclick = openImport;
    }
  }

  function precacheDocs(){
    var bar = document.getElementById("nt-dlbar"), msg = document.getElementById("nt-dlmsg");
    if(!("caches" in window)){ msg.textContent = "Trình duyệt không hỗ trợ lưu tài liệu."; return; }
    bar.hidden = false; msg.textContent = "Đang lấy danh sách…";
    fetch("tai-lieu-manifest.json", {cache:"no-store"}).then(function(r){ return r.json(); }).then(function(list){
      return caches.open("nt-docs").then(function(c){
        var i = 0, ok = 0, fail = 0;
        function next(){
          if(i>=list.length){ msg.textContent = "Xong: "+ok+" tệp đã lưu"+(fail?", "+fail+" tệp lỗi":"")+"."; return; }
          var u = list[i++];
          return c.match(u).then(function(hit){
            if(hit){ ok++; return; }
            return fetch(u).then(function(res){ if(res.ok){ ok++; return c.put(u, res); } fail++; });
          }).catch(function(){ fail++; }).then(function(){
            bar.firstChild.style.width = Math.round(i/list.length*100)+"%";
            msg.textContent = "Đang tải "+i+"/"+list.length+"…";
            return next();
          });
        }
        return next();
      });
    }).catch(function(e){ msg.textContent = "Không tải được: "+(e&&e.message||e); });
  }

  /* --- Duyệt, phân quyền --- */
  function openUsers(){
    var p = panel("Duyệt và phân quyền tài khoản", '<div class="hint">Đang tải…</div>');
    Promise.all([fs.collection("requests").get(), fs.collection("members").get()]).then(function(r){
      var reqs = r[0].docs, mems = r[1].docs, memIds = {};
      mems.forEach(function(d){ memIds[d.id] = true; });
      reqs = reqs.filter(function(d){ return !memIds[d.id]; });
      function roleSel(id, cur){ return '<select data-role="'+h(id)+'">'+["viewer","editor","admin"].map(function(k){ return '<option value="'+k+'"'+(cur===k?" selected":"")+'>'+ROLE_LABEL[k]+'</option>'; }).join("")+'</select>'; }
      var html = '<div class="hint">"Chỉ xem": xem dữ liệu. "Được sửa": nhập, sửa dữ liệu, duyệt SOP. "Quản trị": như Được sửa (riêng duyệt tài khoản chỉ email quản trị làm được).</div>';
      html += '<h4>Chờ duyệt ('+reqs.length+')</h4>';
      html += reqs.length ? reqs.map(function(d){ var x = d.data(); return '<div class="row"><div class="who"><b>'+h(x.name||"(chưa ghi tên)")+'</b><span>'+h(x.email)+' · '+h(x.dept||"")+'</span></div>'+roleSel(d.id,"editor")+'<button class="btn sm primary" data-approve="'+h(d.id)+'">Duyệt</button><button class="btn sm" data-reject="'+h(d.id)+'">Từ chối</button></div>'; }).join("") : '<div class="hint">Không có yêu cầu nào.</div>';
      html += '<h4>Đã cấp quyền ('+mems.length+')</h4>';
      html += mems.map(function(d){ var x = d.data(); return '<div class="row"><div class="who"><b>'+h(x.name||x.email)+'</b><span>'+h(x.email)+' · '+h(x.dept||"")+'</span></div>'+roleSel(d.id,x.role)+'<button class="btn sm" data-save="'+h(d.id)+'">Lưu</button><button class="btn sm" data-remove="'+h(d.id)+'">Thu hồi</button></div>'; }).join("");
      p.querySelector(".pb").innerHTML = html;
      var byId = {}; reqs.concat(mems).forEach(function(d){ byId[d.id] = d.data(); });
      function sel(id){ return p.querySelector('select[data-role="'+id+'"]').value; }
      p.querySelectorAll("[data-approve]").forEach(function(b){ b.onclick = function(){ var id = b.getAttribute("data-approve"), x = byId[id];
        fs.doc("members/"+id).set({email:x.email, name:x.name||"", dept:x.dept||"", role:sel(id), approvedAt:new Date().toISOString(), approvedBy:session.email})
          .then(function(){ return fs.doc("requests/"+id).delete(); }).then(function(){ toast("Đã duyệt "+x.email); openUsers(); }).catch(function(e){ toast(viErr(e)); }); }; });
      p.querySelectorAll("[data-reject]").forEach(function(b){ b.onclick = function(){ var id = b.getAttribute("data-reject");
        if(!confirm("Từ chối yêu cầu của "+byId[id].email+"?")) return;
        fs.doc("requests/"+id).delete().then(openUsers).catch(function(e){ toast(viErr(e)); }); }; });
      p.querySelectorAll("[data-save]").forEach(function(b){ b.onclick = function(){ var id = b.getAttribute("data-save");
        fs.doc("members/"+id).update({role:sel(id)}).then(function(){ toast("Đã lưu quyền"); }).catch(function(e){ toast(viErr(e)); }); }; });
      p.querySelectorAll("[data-remove]").forEach(function(b){ b.onclick = function(){ var id = b.getAttribute("data-remove");
        if(!confirm("Thu hồi quyền của "+byId[id].email+"? Người này sẽ không xem được dữ liệu nữa.")) return;
        fs.doc("members/"+id).delete().then(openUsers).catch(function(e){ toast(viErr(e)); }); }; });
    }).catch(function(e){ p.querySelector(".pb").innerHTML = '<div class="hint">'+h(viErr(e))+'</div>'; });
  }

  /* --- Nhập dữ liệu từ bản artifact cũ (tệp JSON xuất sẵn) --- */
  function openImport(){
    var p = panel("Nhập dữ liệu từ bản cũ",
      '<div class="hint">Chọn tệp dữ liệu (.json) Phòng Điều dưỡng nhận được. Phần mềm sẽ đếm số bản ghi và hỏi lại trước khi ghi.</div>'+
      '<input type="file" id="nt-file" accept=".json,application/json">'+
      '<label class="hint"><input type="checkbox" id="nt-over"> Ghi đè bản ghi đã có cùng mã (mặc định: bỏ qua bản ghi đã có)</label>'+
      '<div id="nt-imsg" class="hint"></div><div class="bar" id="nt-ibar" hidden><span></span></div>');
    document.getElementById("nt-file").onchange = function(ev){
      var f = ev.target.files[0]; if(!f) return;
      var rd = new FileReader();
      rd.onload = function(){
        var data; try{ data = JSON.parse(rd.result); }catch(e){ document.getElementById("nt-imsg").textContent = "Tệp không đọc được: "+e.message; return; }
        var cols = data.collections || {};
        var names = Object.keys(cols), total = 0;
        names.forEach(function(n){ total += cols[n].length; });
        var msg = document.getElementById("nt-imsg");
        msg.innerHTML = 'Tệp có <b>'+total+'</b> bản ghi trong '+names.length+' mục: '+names.map(function(n){ return h(n)+" ("+cols[n].length+")"; }).join(", ")+'. <br><button class="btn primary" id="nt-go" style="margin-top:8px">Bắt đầu nhập</button>';
        document.getElementById("nt-go").onclick = function(){
          var over = document.getElementById("nt-over").checked;
          if(!confirm("Nhập "+total+" bản ghi vào Firebase"+(over?" và GHI ĐÈ bản ghi trùng mã":"")+"?")) return;
          runImport(cols, over);
        };
      };
      rd.readAsText(f);
    };
  }
  function runImport(cols, over){
    var msg = document.getElementById("nt-imsg"), bar = document.getElementById("nt-ibar");
    bar.hidden = false;
    var names = Object.keys(cols), done = 0, written = 0, skipped = 0, total = 0;
    names.forEach(function(n){ total += cols[n].length; });
    var chain = Promise.resolve();
    names.forEach(function(n){
      chain = chain.then(function(){ return over ? {} : fs.collection(n).get({source:"server"}).then(function(s){ var m = {}; s.docs.forEach(function(d){ m[d.id] = true; }); return m; }); })
        .then(function(exist){
          var rows = cols[n].filter(function(r){ if(!over && exist[r.id]){ skipped++; done++; return false; } return true; });
          var c = Promise.resolve();
          for(var i=0;i<rows.length;i+=400){
            (function(part){
              c = c.then(function(){
                var b = fs.batch();
                part.forEach(function(r){ var d = Object.assign({}, r); delete d.id; b.set(fs.collection(n).doc(r.id), clean(d)); });
                return b.commit().then(function(){ written += part.length; done += part.length;
                  bar.firstChild.style.width = Math.round(done/total*100)+"%";
                  msg.textContent = "Đang nhập "+n+": "+done+"/"+total+"…"; });
              });
            })(rows.slice(i,i+400));
          }
          return c;
        });
    });
    chain.then(function(){ bar.firstChild.style.width = "100%"; msg.textContent = "Xong. Đã ghi "+written+" bản ghi, bỏ qua "+skipped+" bản ghi đã có."; })
      .catch(function(e){ msg.textContent = "Dừng do lỗi: "+viErr(e)+". Đã ghi "+written+" bản ghi; có thể chạy lại, bản ghi đã có sẽ được bỏ qua."; });
  }

  /* ------------------------------------------------------------ */
  /* Service worker: chạy offline                                  */
  /* ------------------------------------------------------------ */
  if("serviceWorker" in navigator && location.protocol!=="file:"){
    navigator.serviceWorker.register("sw.js").then(function(reg){
      reg.addEventListener("updatefound", function(){
        var nw = reg.installing;
        nw && nw.addEventListener("statechange", function(){
          if(nw.state==="installed" && navigator.serviceWorker.controller) toast("Có bản cập nhật mới. Đóng và mở lại phần mềm để dùng bản mới.");
        });
      });
    }).catch(function(e){ console.warn("SW", e); });
  }
})();
