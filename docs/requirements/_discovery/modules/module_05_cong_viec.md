# Module 05 — Công việc (`TASK`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)

| Mục | Giá trị |
|---|---|
| Tên UI | Tasks |
| Route | `/admin/tasks` · `/admin/tasks/view/{id}` (link thấy trên Dashboard) · `/admin/tasks/detailed_overview` (Tasks Overview) · `/admin/tasks/delete_task/{id}` (link thấy trên Dashboard — **không** mở) |
| Loại màn hình | Danh sách + Summary · form tạo dạng modal (chưa mở) · Tổng quan chi tiết |
| CRUD | New Task · Tasks Overview · Export · Bulk Actions · đổi Status / Priority **ngay trên dòng** (dropdown) |
| Status flow | ✅ 5 trạng thái: Not Started · In Progress · Testing · Awaiting Feedback · Complete |
| Risk | 🔴 Cao — status flow đổi trực tiếp trên bảng; công việc lặp lại (badge "Recurring Task"); timer; gắn vào Project / Invoice / Estimate / Proposal / Contract |
| Ước REQ | ~35 |
| Evidence | [`task_overview_viewport.png`](../evidence/task_overview_viewport.png) |

## Quan sát

| Thành phần | Chi tiết |
|---|---|
| Summary | Mỗi trạng thái kèm dòng "Tasks assigned to me: N" |
| Cột bảng | `-` (checkbox) · `#` · Name · Status · Start Date · Due Date · Assigned to · Tags · Priority |
| Dòng dữ liệu | Dưới tên có liên kết tới đối tượng cha (VD `#<id> - <tên dự án> - <khách hàng>`); badge "Recurring Task"; dòng quá hạn tô nền đỏ nhạt |
| Tasks Overview | Bộ lọc: nhân viên · tháng · trạng thái · năm · Filter · Export · Back to tasks list |

## Phát hiện tầng network

| Request | Ý nghĩa |
|---|---|
| `POST /admin/tasks/table` | Danh sách server-side (cũng gọi ở Dashboard) |

## Vùng chưa xác minh

- ❔ Form New Task (modal) — chưa mở
- ❔ Chuyển trạng thái có ràng buộc thứ tự không (Complete → Not Started?)
- ❔ Timer (icon đồng hồ ở thanh đầu trang có badge) — bắt đầu/dừng timer ghi Timesheet
- ⚠️ Môi trường dùng chung: dropdown Status/Priority trên dòng **đổi dữ liệu ngay khi chọn** — CẤM thử trên task không do mình tạo
