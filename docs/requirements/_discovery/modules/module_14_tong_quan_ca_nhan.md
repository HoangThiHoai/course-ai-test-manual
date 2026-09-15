# Module 14 — Tổng quan & Cá nhân (`DASH` · `PROFILE`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)
> Gộp file vì cùng phục vụ người dùng đang đăng nhập. **Hai prefix riêng**. Ranh giới chốt 2026-09-14: Announcements thuộc `DASH`; My Timesheets thuộc `PROFILE`.

---

## Dashboard (`DASH`)

| Mục | Giá trị |
|---|---|
| Tên UI | Dashboard · Announcements · thanh đầu trang (dùng chung mọi trang) |
| Route | `/admin/` · `/admin/announcements` · `/admin/staff/reset_dashboard` (link, **không** mở) |
| Loại màn hình | Dashboard widget |
| CRUD | Dashboard Options (tuỳ biến widget) · Announcements: chỉ Export, không có nút tạo |
| Status flow | Không (hiển thị tổng hợp trạng thái của INV / EST / PROP) |
| Risk | 🟢 Thấp — chỉ hiển thị tổng hợp; số liệu sai là hệ quả của module gốc |
| Ước REQ | ~10 |
| Evidence | [`dash_overview_viewport.png`](../evidence/dash_overview_viewport.png) · [`dash_announcements_viewport.png`](../evidence/dash_announcements_viewport.png) |

| Thành phần | Chi tiết |
|---|---|
| Widget | Invoice overview · Estimate overview · Proposal overview · Outstanding / Past Due / Paid Invoices theo năm · My To Do Items (Latest / finished) · khối tab My Tasks · My Projects · My Reminders · Tickets · Announcements · lịch |
| Thanh đầu trang | Ô Search · nút (+) tạo nhanh 12 mục · icon chia sẻ · To Do (badge) · ảnh hồ sơ · Timer (badge) · Notifications — cấu trúc menu ở [system_map mục 2](../system_map.md#2-sơ-đồ-điều-hướng-toàn-hệ-thống) |
| Announcements | Cột Name · Date · "No entries found" |

| Request | Ý nghĩa |
|---|---|
| `GET /admin/utilities/get_calendar_data` | Lịch trên Dashboard |
| `POST /admin/tasks/table` | Widget My Tasks |
| `POST /admin/announcements` | Danh sách thông báo |

**Vùng chưa xác minh:** ❔ quản lý Announcements (tạo/sửa) — nghi ở Setup (AMB-01) · ❔ Dashboard Options lưu theo từng người hay toàn hệ thống · ❔ ô Search toàn cục tìm những entity nào

---

## Cá nhân (`PROFILE`)

| Mục | Giá trị |
|---|---|
| Tên UI | My Profile · Edit Profile · My Timesheets · My To Do Items · Notifications · Language |
| Route | `/admin/profile` · `/admin/profile?notifications=true` · `/admin/staff/edit_profile` · `/admin/staff/timesheets` · `/admin/todo` · `/admin/staff/change_language/<ngôn ngữ>` (link, **không** bấm) |
| Loại màn hình | Form · Danh sách |
| CRUD | To Do: New To Do · sửa · xoá · đánh dấu hoàn thành · kéo thả · Load More. Edit Profile: Save |
| Status flow | To Do: chưa xong ↔ đã xong |
| Risk | 🟡 Trung bình — đổi mật khẩu, bật 2FA, đổi ngôn ngữ ảnh hưởng trực tiếp tài khoản test **dùng chung** |
| Ước REQ | ~25 |
| Evidence | [`profile_todo_viewport.png`](../evidence/profile_todo_viewport.png) — chưa chụp My Profile / Edit Profile vì trang chứa thông tin cá nhân tài khoản |

| Thành phần | Chi tiết |
|---|---|
| My Profile | Thông tin nhân viên · bảng Projects (Project Name · Start Date · Deadline · Status) · Notifications + "Mark all as read" |
| Edit Profile | 16 field hiển thị · khối "Change your password" · "Two Factor Authentication" · chọn ngôn ngữ · hướng LTR |
| Language | System Default + 26 ngôn ngữ (có Vietnamese) |
| My To Do Items | "Unfinished to do's" · "Latest finished to do's" |

| Request | Ý nghĩa |
|---|---|
| `POST /admin/todo` | Danh sách to do |
| `POST /admin/staff/notifications` | Thông báo |
| `POST /admin/projects/staff_projects` | Dự án của nhân viên |
| `POST /admin/staff/timesheets` | Timesheets |

**Vùng chưa xác minh**
- ❔ Luồng 2FA
- 🚫 Môi trường dùng chung: **CẤM** đổi mật khẩu, bật 2FA, đổi ngôn ngữ của tài khoản test chung — khoá người khác khỏi hệ thống. Recon cấp module chỉ trigger validation, **không** Save
