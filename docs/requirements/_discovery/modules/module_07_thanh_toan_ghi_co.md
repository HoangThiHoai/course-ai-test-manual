# Module 07 — Thanh toán & Ghi có (`PAY` · `CRN`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)
> Gộp file vì cùng xoay quanh số dư hoá đơn. **Hai prefix riêng**, về sau sinh 2 file `pay/requirements_pay.md` và `crn/requirements_crn.md`.

---

## Payments (`PAY`)

| Mục | Giá trị |
|---|---|
| Tên UI | Payments (menu Sales ▸ Payments) |
| Route | `/admin/payments` |
| Loại màn hình | Danh sách |
| CRUD | Chỉ Export trên trang danh sách — **không có nút tạo**. Ghi thanh toán từ hoá đơn (nút **Payment** trong chi tiết Invoice · **Batch Payments** ở danh sách Invoice) |
| Status flow | Không thấy |
| Risk | 🔴 Cao — tiền; làm đổi trạng thái hoá đơn; phương thức thanh toán phụ thuộc Setup (BLOCKED) |
| Ước REQ | ~15 |
| Evidence | [`pay_overview_viewport.png`](../evidence/pay_overview_viewport.png) |

| Thành phần | Chi tiết |
|---|---|
| Cột bảng | Payment # · Invoice # · Payment Mode · Transaction ID · Customer · Amount · Date |

| Request | Ý nghĩa |
|---|---|
| `POST /admin/payments/table` | Danh sách server-side |

**Vùng chưa xác minh**
- ❔ Màn hình chi tiết / biên nhận thanh toán — chưa mở
- ❔ Danh sách Payment Mode — Setup › Payment Modes access_denied (AMB-01)

---

## Credit Notes (`CRN`)

| Mục | Giá trị |
|---|---|
| Tên UI | Credit Notes (menu Sales ▸ Credit Notes) |
| Route | `/admin/credit_notes` · `/admin/credit_notes/credit_note` (tạo mới) |
| Loại màn hình | Danh sách · Form có bảng dòng hàng |
| CRUD | New Credit Note · Export · form: Save & Send · Save |
| Status flow | Có cột Status — giá trị ❔ (danh sách rỗng) |
| Risk | 🟡 Trung bình — trừ số dư hoá đơn (cột Remaining Amount) nhưng tần suất dùng thấp |
| Ước REQ | ~25 |
| Evidence | [`crn_overview_viewport.png`](../evidence/crn_overview_viewport.png) |

| Thành phần | Chi tiết |
|---|---|
| Cột bảng | Credit Note # · Credit Note Date · Customer · Status · Project · Reference # · Amount · Remaining Amount |
| Form tạo mới | 21 field hiển thị · bảng dòng hàng Item · Description · Qty · Rate · Tax · Amount · Add Item |

| Request | Ý nghĩa |
|---|---|
| `POST /admin/credit_notes/table` | Danh sách server-side |
| `GET /admin/misc/get_currency/{id}` | Nạp tiền tệ khi mở form |

**Vùng chưa xác minh**
- ❔ Danh sách rỗng (AMB-03) → chưa mở chi tiết, chưa đếm tab, chưa biết giá trị trạng thái
- ❔ Luồng áp ghi có vào hoá đơn
