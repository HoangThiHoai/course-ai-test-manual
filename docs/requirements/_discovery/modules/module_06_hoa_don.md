# Module 06 — Hoá đơn (`INV`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)

| Mục | Giá trị |
|---|---|
| Tên UI | Invoices (menu Sales ▸ Invoices) |
| Route | `/admin/invoices` · `/admin/invoices/invoice` (tạo mới) · `/admin/invoices/list_invoices/{id}` (chi tiết) · `/admin/invoices/recurring` (Recurring Invoices) |
| Loại màn hình | Danh sách · Form có bảng dòng hàng · Chi tiết 6 tab (panel bên phải danh sách) |
| CRUD | Create New Invoice · Batch Payments · Recurring Invoices · Filter by status · Export · trong chi tiết: More · Payment |
| Status flow | ✅ 6 trạng thái (widget "Invoice overview" ở Dashboard): Draft · Not Sent · Unpaid · Partially Paid · Overdue · Paid. Bảng danh sách thấy badge Paid · Unpaid |
| Risk | 🔴 Cao — tiền; tính thuế/giảm giá; trạng thái tự đổi theo thanh toán; hoá đơn định kỳ; tiền tệ + thuế + phương thức thanh toán phụ thuộc Setup (BLOCKED) |
| Ước REQ | ~40 |
| Evidence | [`inv_overview_viewport.png`](../evidence/inv_overview_viewport.png) |

## Quan sát

| Thành phần | Chi tiết |
|---|---|
| Cột bảng | Invoice # · Amount · Total Tax · Date · Customer · Project · Tags · Due Date · Status |
| Số hoá đơn | Có 2 định dạng trong dữ liệu: `INV-000007` và `ABC-553416` → quy tắc sinh số ❔ |
| Form tạo mới | 27 field hiển thị · bảng dòng hàng Item · Description · Qty · Rate · Tax · Amount · nút Add Item · **Bill Tasks** · giá trị mặc định hiển thị: phương thức "Bank", tiền tệ "USD $", "No discount", "No Tax" · nút **Save as Draft** · **Save** |
| 6 tab chi tiết | Invoice · Payments · Tasks · Activity Log · Reminders · Notes |

## Phát hiện tầng network

| Request | Ý nghĩa |
|---|---|
| `POST /admin/invoices/table` | Danh sách server-side (cả trang Recurring) |
| `GET /admin/invoices/get_invoice_data_ajax/{id}` | Nạp panel chi tiết |
| `GET /admin/misc/get_currency/{id}` | Nạp tiền tệ khi mở form |

## Vùng chưa xác minh

- ❔ Quy tắc sinh số hoá đơn (prefix `INV-` vs `ABC-`) — cấu hình ở Setup › Settings (AMB-01)
- ❔ Điều kiện chuyển Overdue / Partially Paid
- ❔ Batch Payments — chưa mở
- ⚠️ Môi trường dùng chung: **CẤM** ghi thanh toán / đổi trạng thái hoá đơn không do mình tạo
