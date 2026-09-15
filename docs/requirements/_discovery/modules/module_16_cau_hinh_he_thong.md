# Module 16 — Cấu hình hệ thống (`SETUP`) — ⏸️ BLOCKED

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)
> Ranh giới chốt 2026-09-14: toàn bộ cấu hình gộp **1 prefix `SETUP`**. Khi có tài khoản admin và thấy Staff / Roles có vòng đời riêng, cân nhắc tách qua `/discover-system` mode ADD — **prefix `SETUP` giữ nguyên**.

| Mục | Giá trị |
|---|---|
| Tên UI | Setup (menu mở bằng nút ở thanh đầu trang) |
| Trạng thái | **BLOCKED** — tài khoản hiện tại không có quyền (AMB-01) |
| Loại màn hình | Cấu hình |
| Risk | 🔴 Cao — quyền và cấu hình toàn hệ thống; 5 module khác phụ thuộc giá trị cấu hình |
| Ước REQ | ❔ |
| Evidence | Không có ảnh — mọi route bị chuyển hướng; bằng chứng là bảng kết quả điều hướng bên dưới |

## Bằng chứng BLOCKED (kiểm chứng thực tế 2026-09-14)

| Kiểm tra | Kết quả |
|---|---|
| DOM `#setup-menu` | Chỉ có tiêu đề "Setup" + nút đóng, **không** có mục menu |
| `app.user_is_admin` (JS toàn cục) | Rỗng |
| Không tìm thấy nút mở Setup ở thanh đầu trang | — |

| Route (điều hướng thẳng URL, chỉ đọc) | Kết quả |
|---|---|
| `/admin/staff` | → `/admin/access_denied` |
| `/admin/roles` | → `/admin/access_denied` |
| `/admin/settings` | → `/admin/access_denied` |
| `/admin/departments` | → `/admin/access_denied` |
| `/admin/custom_fields` | → `/admin/access_denied` |
| `/admin/emails` | → `/admin/access_denied` |
| `/admin/gdpr` | → `/admin/access_denied` |
| `/admin/taxes` | → `/admin/access_denied` |
| `/admin/currencies` | → `/admin/access_denied` |
| `/admin/paymentmodes` | → `/admin/access_denied` |
| `/admin/clients/groups` | → `/admin/access_denied` |
| `/admin/utilities/activity_log` | → `/admin/access_denied` |
| `/admin/modules` | → `/admin/` (Dashboard) — **khác** các route còn lại (AMB-04) |

> Các route trên được thử theo mẫu route của hệ thống; việc bị chuyển sang `access_denied` cho thấy route **có tồn tại và bị chặn quyền**, nhưng nội dung bên trong **chưa ai nhìn thấy**.

## Module phụ thuộc cấu hình này

| Cấu hình (nghi) | Module chịu ảnh hưởng |
|---|---|
| Taxes · Currencies · Payment Modes | `ITEM` · `INV` · `PAY` · `EST` · `PROP` · `CRN` · `EXP` · `SUB` |
| Customer Groups | `CUST` · `RPT` |
| Departments · Services · Predefined Replies | `TKT` |
| Lead Statuses · Lead Sources | `LEAD` — ❔ nghi có, route chưa thử |
| Contract Types · Expense Categories | `CTR` · `EXP` — ❔ nghi có, route chưa thử |
| Staff · Roles | Ma trận phân quyền mọi module (AMB-02) |

## Gỡ BLOCKED

1. Có tài khoản admin thật → cập nhật `.env`
2. Chạy `/discover-system` mode ADD cho `SETUP` → liệt kê đủ mục menu, chụp evidence
3. Đổi trạng thái trong [danh mục](../../README.md) từ ⏸️ sang ⬜
