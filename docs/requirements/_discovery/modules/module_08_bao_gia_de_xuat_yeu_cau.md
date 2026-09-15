# Module 08 — Báo giá, Đề xuất & Yêu cầu báo giá (`EST` · `PROP` · `ESTREQ`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)
> Gộp file vì cùng giai đoạn tiền bán hàng, chuyển đổi sang nhau. **Ba prefix riêng**, về sau sinh 3 file requirements riêng.

---

## Estimates (`EST`)

| Mục | Giá trị |
|---|---|
| Tên UI | Estimates (menu Sales ▸ Estimates) |
| Route | `/admin/estimates` · `/admin/estimates/estimate` (tạo mới) · `/admin/estimates/list_estimates/{id}` (chi tiết) |
| Loại màn hình | Danh sách · Form có bảng dòng hàng · Chi tiết 5 tab |
| CRUD | Create New Estimate · Export · form: Save · chi tiết: More · **Convert to Invoice** |
| Status flow | ✅ 6 trạng thái (widget "Estimate overview" ở Dashboard): Draft · Not Sent · Sent · Expired · Declined · Accepted. Form tạo mới mặc định hiển thị "Draft" |
| Risk | 🟡 Trung bình — có tiền và chuyển sang hoá đơn, nhưng chưa phát sinh công nợ |
| Ước REQ | ~30 |
| Evidence | [`est_overview_viewport.png`](../evidence/est_overview_viewport.png) |

| Thành phần | Chi tiết |
|---|---|
| Cột bảng | Estimate # · Amount · Total Tax · Customer · Project · Tags · Date · Expiry Date · Reference # · Status |
| Form tạo mới | 25 field hiển thị · bảng dòng hàng · Add Item |
| 5 tab chi tiết | Estimate · Tasks · Activity Log · Reminders · Notes |

| Request | Ý nghĩa |
|---|---|
| `POST /admin/estimates/table` | Danh sách server-side |
| `GET /admin/estimates/get_estimate_data_ajax/{id}` | Nạp panel chi tiết |
| `GET /admin/misc/get_currency/{id}` | Nạp tiền tệ khi mở form |

**Vùng chưa xác minh:** ❔ điều kiện tự chuyển Expired · ❔ Convert to Invoice giữ/đổi trạng thái estimate

---

## Proposals (`PROP`)

| Mục | Giá trị |
|---|---|
| Tên UI | Proposals (menu Sales ▸ Proposals) |
| Route | `/admin/proposals` · `/admin/proposals/proposal` (tạo mới) · `/admin/proposals/list_proposals/{id}` (chi tiết) |
| Loại màn hình | Danh sách · Form có bảng dòng hàng · Chi tiết 6 tab |
| CRUD | New Proposal · Export · form: Save & Send · Save · chi tiết: More · **Convert** |
| Status flow | ✅ 6 trạng thái (widget "Proposal overview" ở Dashboard): Draft · Sent · Open · Revised · Declined · Accepted. Form mặc định "Draft" |
| Risk | 🟡 Trung bình |
| Ước REQ | ~30 |
| Evidence | [`prop_overview_header_clip.png`](../evidence/prop_overview_header_clip.png) — cắt vùng đầu trang, cột "To" chứa email người nhận |

| Thành phần | Chi tiết |
|---|---|
| Cột bảng | Proposal # · Subject · To · Total · Date · Open Till · Project · Tags · Date Created · Status |
| Form tạo mới | 29 field hiển thị · bảng dòng hàng · Add Item |
| 6 tab chi tiết | Proposal · Comments · Reminders · Tasks · Notes · Templates |

| Request | Ý nghĩa |
|---|---|
| `POST /admin/proposals/table` | Danh sách server-side |
| `GET /admin/proposals/get_proposal_data_ajax/{id}` | Nạp panel chi tiết |
| `GET /admin/misc/get_currency/{id}` | Nạp tiền tệ khi mở form |

**Vùng chưa xác minh:** ❔ "To" gửi cho Customer hay Lead (hoặc cả hai) · ❔ Convert sang Estimate hay Invoice · ❔ Comments từ phía khách hàng

---

## Estimate Request (`ESTREQ`)

| Mục | Giá trị |
|---|---|
| Tên UI | Estimate Request |
| Route | `/admin/estimate_request` |
| Loại màn hình | Danh sách · form builder (nút New Form) |
| CRUD | New Form · Export |
| Status flow | Có cột Status — giá trị ❔ (danh sách rỗng) |
| Risk | 🟡 Trung bình — form công khai thu yêu cầu từ bên ngoài |
| Ước REQ | ~15 |
| Evidence | [`estreq_overview_viewport.png`](../evidence/estreq_overview_viewport.png) |

| Thành phần | Chi tiết |
|---|---|
| Cột bảng | `#` · Email · Tags · Assigned · Status · Created |

| Request | Ý nghĩa |
|---|---|
| `POST /admin/estimate_request/table` | Danh sách server-side |

**Vùng chưa xác minh:** ❔ danh sách rỗng (AMB-03) · ❔ New Form — chưa mở · ❔ form công khai nằm ngoài `/admin/` · ❔ quan hệ với Leads / Estimates
