# Module 01 — Đăng nhập (`LOGIN`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)

| Mục | Giá trị |
|---|---|
| Tên UI | Login · Forgot Password |
| Route | `/admin/authentication` · `/admin/authentication/forgot_password` · `/admin/authentication/logout` (link trong menu hồ sơ, **không** mở) |
| Loại màn hình | Form |
| CRUD | Không |
| Status flow | Không |
| Risk | 🔴 Cao — cửa ngõ toàn hệ thống; lỗi ở đây chặn mọi module khác; liên quan bảo mật tài khoản |
| Ước REQ | ~12 |
| Evidence | [`login_overview_viewport.png`](../evidence/login_overview_viewport.png) |

## Quan sát

| Màn hình | Field (name:type — đọc DOM) | Hành động |
|---|---|---|
| Login — title `Perfex CRM \| Anh Tester Demo - Login` | `email:email` · `password:password` · `remember:checkbox` — nhãn "Email Address", "Password", "Remember me" | Nút **Login** · link **Forgot Password?** |
| Forgot Password — cùng title với Login | `email:email` | Nút **Confirm** |

## Phát hiện tầng network

Không quan sát được request đăng nhập — bước đăng nhập do user tự thực hiện. Recon module phải bật network khi submit sai để lấy validation server-side.

## Vùng chưa xác minh

- ❔ **2FA**: Edit Profile có mục "Two Factor Authentication" → có thể có bước xác thực thứ hai sau Login
- ❔ reCAPTCHA / khoá tài khoản khi sai nhiều lần — không thấy trên form ở phiên này
- ❔ Luồng email đặt lại mật khẩu — môi trường dùng chung, **không** bấm Confirm với email thật
- ❔ Modal "Started tasks timers found!…" khi logout lúc đang chạy timer (thấy trong DOM, liên quan `TASK`)
- ⚠️ Môi trường dùng chung: **CẤM** thử sai mật khẩu nhiều lần với tài khoản test chung — có thể khoá tài khoản của người khác
