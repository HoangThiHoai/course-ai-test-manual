# Module 12 — Hỗ trợ & Cơ sở kiến thức (`TKT` · `KB`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)
> Gộp file vì ticket chèn liên kết bài viết KB khi trả lời. **Hai prefix riêng**, về sau sinh 2 file requirements riêng.

---

## Support (`TKT`)

| Mục | Giá trị |
|---|---|
| Tên UI | Support — title trang "Support Tickets" |
| Route | `/admin/tickets` · `/admin/tickets/add` (tạo mới) |
| Loại màn hình | Danh sách + Summary · Form |
| CRUD | New Ticket · Export · Bulk Actions · form: **Open Ticket** |
| Status flow | ✅ 5 trạng thái (Summary): Open · In Progress · Answered · On Hold · Closed |
| Risk | 🟡 Trung bình — status flow + mức ưu tiên; phòng ban / dịch vụ / câu trả lời mẫu cấu hình ở Setup (BLOCKED) |
| Ước REQ | ~30 |
| Evidence | [`tkt_overview_viewport.png`](../evidence/tkt_overview_viewport.png) |

| Thành phần | Chi tiết |
|---|---|
| Cột bảng | `-` · `#` · Subject · Tags · Department · Service · Contact · Status · Priority · Last Reply · Created |
| Form tạo mới | Khối "Ticket Information" + "Ticket Body" · 13 field hiển thị · lựa chọn "Ticket without contact" · priority mặc định hiển thị "Medium" · nút Insert predefined reply · Insert knowledge base link |

| Request | Ý nghĩa |
|---|---|
| `POST /admin/tickets` | Danh sách server-side (khác mẫu `/table` của module khác) |

**Vùng chưa xác minh**
- ❔ Danh sách rỗng (AMB-03) → chưa mở chi tiết ticket, chưa thấy luồng trả lời
- ❔ Department · Service · Predefined replies (AMB-01)
- ❔ Ticket nhận qua email (piping) — nghi có trong Setup

---

## Knowledge Base (`KB`)

| Mục | Giá trị |
|---|---|
| Tên UI | Knowledge Base |
| Route | `/admin/knowledge_base` · `/admin/knowledge_base/article` (tạo mới) · `/admin/knowledge_base/manage_groups` (Groups) |
| Loại màn hình | Danh sách · Form |
| CRUD | New Article · Groups · Export · form: Save · trang Groups: New Group · Articles · Export |
| Status flow | Không thấy (cột Date Published) |
| Risk | 🟢 Thấp — nội dung tĩnh |
| Ước REQ | ~15 |
| Evidence | [`kb_overview_viewport.png`](../evidence/kb_overview_viewport.png) |

| Thành phần | Chi tiết |
|---|---|
| Cột bảng | Article Name · Group · Date Published |
| Form tạo mới | 4 field hiển thị (+ trình soạn thảo) |

| Request | Ý nghĩa |
|---|---|
| `POST /admin/knowledge_base` | Danh sách server-side |

**Vùng chưa xác minh:** ❔ danh sách rỗng (AMB-03) · ❔ bài viết hiển thị ra cổng khách hàng · báo cáo KB nằm ở `RPT`
