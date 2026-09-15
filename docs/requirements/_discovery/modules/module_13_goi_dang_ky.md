# Module 13 — Gói đăng ký (`SUB`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)

| Mục | Giá trị |
|---|---|
| Tên UI | Subscriptions |
| Route | `/admin/subscriptions` · `/admin/subscriptions/create` (tạo mới) |
| Loại màn hình | Danh sách + Summary · Form |
| CRUD | New Subscription · Export · form: Save |
| Status flow | ✅ 8 trạng thái (Summary, kèm logo stripe): Not Subscribed · Active · Future · Past Due · Unpaid · Incomplete · Canceled · Incomplete Expired |
| Risk | 🟡 Trung bình — thanh toán định kỳ qua cổng ngoài, nhưng phụ thuộc tích hợp chưa rõ có bật |
| Ước REQ | ~15 |
| Evidence | [`sub_overview_viewport.png`](../evidence/sub_overview_viewport.png) |

## Quan sát

| Thành phần | Chi tiết |
|---|---|
| Cột bảng | `#` · Subscription Name · Customer · Project · Status · Next Billing Cycle · Date Subscribed · Last Sent |
| Form tạo mới | 11 field hiển thị · "Select Stripe plan" · tiền tệ "USD $" · "No Tax" |

## Phát hiện tầng network

| Request | Ý nghĩa |
|---|---|
| `POST /admin/subscriptions/table` | Danh sách server-side |

## Vùng chưa xác minh

- ❔ Stripe đã cấu hình chưa (AMB-05) — không có thì không kiểm được luồng đầu-cuối
- ❔ Danh sách rỗng (AMB-03) → chưa mở chi tiết
- ⚪ Nếu Stripe chưa bật: TC luồng thanh toán viết trước, đánh `skip`
