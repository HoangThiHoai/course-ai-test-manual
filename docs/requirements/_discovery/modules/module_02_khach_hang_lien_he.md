# Module 02 — Khách hàng & Liên hệ (`CUST`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)
> Ranh giới chốt 2026-09-14: **Contacts gộp vào `CUST`** (không cấp prefix riêng).

| Mục | Giá trị |
|---|---|
| Tên UI | Customers · Contacts |
| Route | `/admin/clients` (danh sách) · `/admin/clients/client` (tạo mới) · `/admin/clients/client/{id}` (chi tiết) · `/admin/clients/all_contacts` (Contacts) · `/admin/clients/groups` → ❌ access_denied |
| Loại màn hình | Danh sách + Summary · Form 2 tab · Chi tiết 19 tab |
| CRUD | Tạo (New Customer · Save · Save and create contact) · Import (Import Customers) · Export · Bulk Actions · Sửa trong tab Profile |
| Status flow | Bật/tắt **Active** (công tắc trên từng dòng) |
| Risk | 🔴 Cao — dữ liệu khách hàng; ≥ 12 module khác liên kết qua tab chi tiết; có import hàng loạt; tab **Vault** (lưu thông tin nhạy cảm) |
| Ước REQ | ~40 |
| Evidence | [`cust_overview_header_clip.png`](../evidence/cust_overview_header_clip.png) — cắt vùng đầu trang, không kèm dòng dữ liệu |

## Quan sát

| Thành phần | Chi tiết |
|---|---|
| Summary | Total Customers · Active Customers · Inactive Customers · Active Contacts · Inactive Contacts · Contacts Logged In Today |
| Cột bảng | `#` · Company · Primary Contact · Primary Email · Phone · Active · Groups · Date Created |
| Form tạo mới | Tab **Customer Details** · **Billing & Shipping** — 12 field hiển thị ở tab đầu (đếm DOM `offsetParent`) |
| 19 tab chi tiết | Profile · Contacts · Notes · Statement · Invoices · Payments · Proposals · Credit Notes · Estimates · Subscriptions · Expenses · Contracts · Projects · Tasks · Tickets · Files · Vault · Reminders · Map |
| Tab thuộc riêng `CUST` | Profile · Contacts · Notes · Statement · Files · Vault · Reminders · Map |
| Tab là khung nhìn của module khác | Invoices · Payments · Proposals · Credit Notes · Estimates · Subscriptions · Expenses · Contracts · Projects · Tasks · Tickets — recon ở module gốc |
| Contacts (tab) | Nút New Contact → form nạp qua AJAX |

## Phát hiện tầng network

| Request | Ý nghĩa |
|---|---|
| `POST /admin/clients/table` | Danh sách server-side |
| `POST /admin/clients/contacts/{id}` | Danh sách liên hệ của 1 khách hàng |
| `GET /admin/clients/form_contact/{id}/{id}` | Form liên hệ nạp động (khách hàng / liên hệ) |
| `POST /admin/clients/all_contacts` | Trang Contacts toàn hệ thống |

## Vùng chưa xác minh

- ❌ Customer Groups — `/admin/clients/groups` access_denied (AMB-01); cột Groups vẫn hiển thị
- ❔ Contact đăng nhập cổng khách hàng (summary có "Contacts Logged In Today") — cổng khách hàng nằm ngoài `/admin/`, chưa khảo sát
- ❔ Định dạng file Import Customers
- ❔ Tab Vault · Map — chưa mở nội dung
- ⚠️ Môi trường dùng chung: **CẤM** Bulk Actions / tắt Active trên khách hàng không do mình tạo
