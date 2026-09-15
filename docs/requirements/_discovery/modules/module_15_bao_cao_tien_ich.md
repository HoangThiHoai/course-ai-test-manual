# Module 15 — Báo cáo & Tiện ích (`RPT` · `UTIL`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)
> Gộp file vì cùng là nhóm màn hình tra cứu/tiện ích nhỏ. **Hai prefix riêng**. Ranh giới chốt 2026-09-14: Timesheets overview thuộc `RPT`.

---

## Reports (`RPT`)

| Mục | Giá trị |
|---|---|
| Tên UI | Reports ▸ Sales · Expenses · Expenses vs Income · Leads · Timesheets overview · KB Articles |
| Route | `/admin/reports/sales` · `/admin/reports/expenses` · `/admin/reports/expenses_vs_income` · `/admin/reports/leads` · `/admin/staff/timesheets?view=all` · `/admin/reports/knowledge_base_articles` |
| Loại màn hình | Báo cáo (bảng + biểu đồ + bộ lọc) |
| CRUD | Chỉ đọc · Export (Timesheets) · Detailed Report (Expenses) |
| Status flow | Không |
| Risk | 🟡 Trung bình — số liệu tổng hợp tiền; sai công thức khó phát hiện |
| Ước REQ | ~25 |
| Evidence | [`rpt_sales_viewport.png`](../evidence/rpt_sales_viewport.png) |

| Trang | Quan sát |
|---|---|
| Sales | Sales Report: Invoices · Items · Payments Received · Credit Notes · Proposals · Estimates · Customers Report. Charts Based Report: Total Income · Payment Modes (Transactions) · Total Value By Customer Groups. Ghi chú đỏ: "Cancelled invoices are excluded from the report" |
| Expenses | Bảng Category × 12 tháng + cột "Year (2026)" · nút Detailed Report |
| Expenses vs Income | Biểu đồ · gọi `GET /admin/misc/get_currency/{id}` |
| Leads | Nút "Switch to staff report" · chọn tháng · `GET /admin/reports/leads_monthly_report/{id}`. ⚠️ title trang là "Perfex CRM \| Anh Tester Demo", không có tên báo cáo như các trang khác |
| Timesheets overview | Title "Today - All Staff Members" · bộ lọc My Timesheets / Today / All Staff Members / Customer / Project · Apply · Export · cột Staff Member · Task · Timesheet Tags · Start Time · End Time · Note · Related · Time (h) · Time (decimal) · `POST /admin/staff/timesheets` |
| KB Articles | Chọn "Choose Group" |

**Vùng chưa xác minh:** ❔ tài khoản không phải admin xem được dữ liệu của mọi nhân viên (Timesheets "All Staff Members") hay chỉ của mình · ❔ báo cáo "Total Value By Customer Groups" phụ thuộc Customer Groups (access_denied)

---

## Utilities (`UTIL`)

| Mục | Giá trị |
|---|---|
| Tên UI | Utilities ▸ Media · Bulk PDF Export · Calendar |
| Route | `/admin/utilities/media` · `/admin/utilities/bulk_pdf_exporter` · `/admin/utilities/calendar` · tạo sự kiện: `/admin/utilities/calendar?new_event=true&date=<dd-mm-yyyy>` |
| Loại màn hình | Trình quản lý file · Form xuất · Lịch |
| CRUD | Media: tải lên / xoá file (trình quản lý elFinder). Bulk PDF Export: Export. Calendar: tạo sự kiện |
| Status flow | Không |
| Risk | 🟢 Thấp |
| Ước REQ | ~20 |
| Evidence | [`util_calendar_viewport.png`](../evidence/util_calendar_viewport.png) |

| Trang | Quan sát |
|---|---|
| Media | Trình quản lý file; title trang dạng `<tên-tài-khoản>:Files`; `GET /admin/utilities/media_connector` |
| Bulk PDF Export | 4 field · selectpicker "Nothing selected" · Export |
| Calendar | Month · Week · Day · Filter By · Today · điều hướng tháng · hiển thị sự kiện của Project / Contract / Task; `GET /admin/utilities/get_calendar_data` |

**Vùng chưa xác minh:** ❔ Media dùng chung toàn hệ thống hay theo từng người · ❔ Bulk PDF Export chọn được những loại chứng từ nào · ⚠️ môi trường dùng chung: **CẤM** xoá file Media không do mình tải lên
