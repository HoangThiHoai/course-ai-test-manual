# Module 03 — Mặt hàng (`ITEM`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)

| Mục | Giá trị |
|---|---|
| Tên UI | Items (menu Sales ▸ Items) — title trang "Invoice Items" |
| Route | `/admin/invoice_items` · `/admin/invoice_items/groups` |
| Loại màn hình | Danh sách · form tạo dạng modal (chưa mở) |
| CRUD | New Item · Import Items · Groups · Export · Bulk Actions |
| Status flow | Không |
| Risk | 🟡 Trung bình — nguồn dòng hàng cho Proposal / Estimate / Invoice / Credit Note; thuế phụ thuộc Setup › Taxes (BLOCKED) |
| Ước REQ | ~15 |
| Evidence | [`item_overview_viewport.png`](../evidence/item_overview_viewport.png) |

## Quan sát

| Thành phần | Chi tiết |
|---|---|
| Cột bảng | Description · Long Description · Rate · Tax 1 · Tax 2 · Unit · Group Name |
| Groups | `/admin/invoice_items/groups` mở được nhưng **không** hiện nút thao tác nào |

## Phát hiện tầng network

| Request | Ý nghĩa |
|---|---|
| `POST /admin/invoice_items/table` | Danh sách server-side |

## Vùng chưa xác minh

- ❔ Form New Item (modal) — chưa mở, chưa đếm field
- ❔ Trang Groups không có nút — do quyền hay do thiết kế?
- ❔ Danh sách thuế Tax 1 / Tax 2 — cấu hình ở Setup (AMB-01)
- ❔ Định dạng file Import Items
