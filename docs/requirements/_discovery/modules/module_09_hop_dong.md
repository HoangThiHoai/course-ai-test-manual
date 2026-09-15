# Module 09 — Hợp đồng (`CTR`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)

| Mục | Giá trị |
|---|---|
| Tên UI | Contracts |
| Route | `/admin/contracts` · `/admin/contracts/contract` (tạo mới) · `/admin/contracts/contract/{id}` (chi tiết / sửa) |
| Loại màn hình | Summary + 2 biểu đồ + danh sách · Form · Chi tiết 7 tab |
| CRUD | New Contract · Export · form: Save · chi tiết: More |
| Status flow | ✅ Nhóm trạng thái trên Summary: Active · Expired · About to Expire · Recently Added · Trash |
| Risk | 🟡 Trung bình — có giá trị tiền, ký điện tử (cột Signature), gia hạn (tab Renewal History) |
| Ước REQ | ~30 |
| Evidence | [`ctr_overview_viewport.png`](../evidence/ctr_overview_viewport.png) — bảng danh sách nằm dưới viewport |

## Quan sát

| Thành phần | Chi tiết |
|---|---|
| Biểu đồ | Contracts by Type · Contracts Value by Type (USD) |
| Cột bảng | `#` · Subject · Customer · Contract Type · Contract Value · Start Date · End Date · Project · Signature |
| Form tạo mới | Tiêu đề "Contract Information" · 9 field hiển thị |
| 7 tab chi tiết | Contract · Attachments · Comments · Renewal History · Tasks · Notes · Templates |

## Phát hiện tầng network

| Request | Ý nghĩa |
|---|---|
| `POST /admin/contracts/table` | Danh sách server-side |

## Vùng chưa xác minh

- ❔ Danh sách Contract Type — nơi cấu hình chưa xác định (nghi Setup, AMB-01)
- ❔ "About to Expire" tính theo bao nhiêu ngày
- ❔ Luồng ký hợp đồng phía khách hàng (ngoài `/admin/`)
- ❔ Trash là trạng thái hay xoá mềm
