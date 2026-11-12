/* Cấu hình Firebase của dự án nt-nursing (không phải mật khẩu; bảo mật nằm ở Firestore Rules).
   Đã đối chiếu với bản chép từ Firebase Console ngày 12/11/2026. */
window.NT_FIREBASE_CONFIG = {
  apiKey: "AIzaSyBSS3DFguM7KyqH96JFo0-9c2ouCOP5T2E",
  authDomain: "nt-nursing.firebaseapp.com",
  projectId: "nt-nursing",
  storageBucket: "nt-nursing.firebasestorage.app",
  messagingSenderId: "408611565304",
  appId: "1:408611565304:web:557791ef84c2246ce0950d"
};
/* Email quản trị: tài khoản này duyệt người dùng mới (phải xác minh email). Trùng với firestore.rules. */
window.NT_ADMIN_EMAILS = ["pddbvnt@gmail.com"];
/* Bản cũ trên Claude, để mở khi cần */
window.NT_LEGACY_URL = "https://claude.ai/artifact/6pdLLwzGqq2i3rAtHbrB3a";
