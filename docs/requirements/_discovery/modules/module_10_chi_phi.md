# Module 10 — Chi phí (`EXP`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)

| Mục | Giá trị |
|---|---|
| Tên UI | Expenses |
| Route | `/admin/expenses` · `/admin/expenses/expense` (tạo mới) |
| Loại màn hình | Danh sách · Form |
| CRUD | Record Expense · Import Expenses · Export · Bulk Actions · form: Save |
| Status flow | Không thấy |
| Risk | 🟡 Trung bình — tiền; có thể gắn vào hoá đơn khách hàng (cột Invoice) |
| Ước REQ | ~25 |
| Evidence | [`exp_overview_viewport.png`](../evidence/exp_overview_viewport.png) |

## Quan sát

| Thành phần | Chi tiết |
|---|---|
| Cột bảng | `-` · Category · Amount · Name · Receipt · Date · Project · Customer · Invoice · Reference # · Payment Mode |
| Form tạo mới | 12 field hiển thị · có khối "Advanced Options" · tiền tệ mặc định hiển thị "USD $" · "No Tax" |

## Phát hiện tầng network

| Request | Ý nghĩa |
|---|---|
| `POST /admin/expenses/table` | Danh sách server-side |
| `POST /admin/expenses/get_expenses_total` | Tổng chi phí (khối tổng hợp) |

## Vùng chưa xác minh

- ❔ Danh sách rỗng (AMB-03) → chưa mở chi tiết
- ❔ Danh mục Category — nơi cấu hình chưa xác định (nghi Setup, AMB-01)
- ❔ Nội dung Advanced Options (chi phí định kỳ, tính phí khách hàng?)
- ❔ Định dạng file Import Expenses · tải biên lai (Receipt)
