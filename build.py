"""Dựng index.html (bản PWA) từ app-src.html (bản artifact gốc)."""
import re, pathlib
src = pathlib.Path("app-src.html").read_text(encoding="utf-8")
head_add = ('<meta name="theme-color" content="#0d6e5f">'
            '<link rel="manifest" href="manifest.webmanifest">'
            '<link rel="icon" href="icons/icon-192.png">'
            '<link rel="apple-touch-icon" href="icons/icon-192.png">'
            '<meta name="apple-mobile-web-app-capable" content="yes">')
assert src.count("</head>") == 1
src = src.replace("</head>", head_add + "</head>", 1)
src = src.replace("<html>", '<html lang="vi">', 1)
scripts = ('<script src="vendor/firebase-app-compat.js"></script>\n'
           '<script src="vendor/firebase-auth-compat.js"></script>\n'
           '<script src="vendor/firebase-firestore-compat.js"></script>\n'
           '<script src="config.js"></script>\n'
           '<script src="nt-firebase.js"></script>\n')
i = src.index("<script>")
src = src[:i] + scripts + src[i:]
src = src.replace("Quyền phê duyệt SOP/đóng sự cố vẫn do Claude quản lý theo quyền chia sẻ (Can edit) thực tế của artifact.",
                  "Quyền phê duyệt SOP/đóng sự cố do Phòng Điều dưỡng cấp cho từng tài khoản (Được sửa / Chỉ xem).")
pathlib.Path("index.html").write_text(src, encoding="utf-8")
print("ok", len(src))
