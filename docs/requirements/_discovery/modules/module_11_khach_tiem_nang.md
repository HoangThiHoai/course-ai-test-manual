# Module 11 — Khách hàng tiềm năng (`LEAD`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)

| Mục | Giá trị |
|---|---|
| Tên UI | Leads |
| Route | `/admin/leads` (danh sách; nút icon chuyển kanban / summary) |
| Loại màn hình | Danh sách · Kanban · form tạo dạng modal (chưa mở) |
| CRUD | New Lead · Export · Bulk Actions |
| Status flow | Có cột Status + Source — giá trị ❔ (danh sách rỗng) |
| Risk | 🔴 Cao — dữ liệu liên hệ cá nhân; chuyển đổi thành Customer; trạng thái/nguồn lead cấu hình ở Setup (BLOCKED); danh sách rỗng bất thường trên môi trường demo dùng chung |
| Ước REQ | ~35 |
| Evidence | [`lead_overview_viewport.png`](../evidence/lead_overview_viewport.png) |

## Quan sát

| Thành phần | Chi tiết |
|---|---|
| Cột bảng | `-` · `#` · Name · Company · Email · Phone · Value · Tags · Assigned · Status · Source · Last Contact · Created |
| Danh sách | "No entries found" |
| Kanban | `/admin/leads?kanban=true` vẫn trả về dạng bảng — kanban bật bằng nút icon, chưa bấm |

## Phát hiện tầng network

| Request | Ý nghĩa |
|---|---|
| `POST /admin/leads/table` | Danh sách server-side |

## Vùng chưa xác minh

- ❔ Danh sách rỗng: trống thật hay bị lọc theo quyền "chỉ xem lead được giao" (AMB-03)
- ❔ Form New Lead (modal) · luồng Convert to Customer
- ❔ Danh sách Status / Source (AMB-01)
- ❔ Chế độ Kanban — kéo thả đổi trạng thái
