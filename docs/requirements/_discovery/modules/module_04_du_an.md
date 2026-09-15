# Module 04 — Dự án (`PRJ`)

> ← [Bản đồ hệ thống](../system_map.md) · Trạng thái recon: xem [danh mục](../../README.md)
> Ranh giới chốt 2026-09-14: Milestones · Discussions · Gantt · tab Timesheets **thuộc `PRJ`**, không tách prefix.

| Mục | Giá trị |
|---|---|
| Tên UI | Projects |
| Route | `/admin/projects` · `/admin/projects/project` (tạo mới) · `/admin/projects/view/{id}` (chi tiết) |
| Loại màn hình | Danh sách + Summary · Form 2 tab · Chi tiết 12 tab |
| CRUD | New Project · Export · trong chi tiết: New Task · Invoice Project · More |
| Status flow | ✅ 5 trạng thái: Not Started · In Progress · On Hold · Cancelled · Finished (Summary + badge cột Status) |
| Risk | 🔴 Cao — status flow 5 trạng thái; lập hoá đơn từ dự án (Invoice Project); nhiều module gắn vào (Task, Ticket, Contract, Sales, Expense) |
| Ước REQ | ~45 |
| Evidence | [`prj_overview_viewport.png`](../evidence/prj_overview_viewport.png) |

## Quan sát

| Thành phần | Chi tiết |
|---|---|
| Cột bảng | `#` · Project Name · Customer · Tags · Start Date · Deadline · Members · Status |
| Form tạo mới | Tab **Project** · **Project Settings** — 12 field hiển thị; giá trị mặc định hiển thị trên selectpicker: "Fixed Rate" · "In Progress" · thành viên là tài khoản hiện tại |
| 12 tab chi tiết | Overview · Tasks · Timesheets · Milestones · Files · Discussions · Gantt · Tickets · Contracts · Sales · Notes · Activity |
| Tab thuộc riêng `PRJ` | Overview · Timesheets · Milestones · Files · Discussions · Gantt · Notes · Activity |
| Tab là khung nhìn của module khác | Tasks · Tickets · Contracts · Sales |

## Phát hiện tầng network

| Request | Ý nghĩa |
|---|---|
| `POST /admin/projects/table` | Danh sách server-side |
| `POST /admin/projects/staff_projects` | Dự án của nhân viên (gọi ở My Profile) |

## Vùng chưa xác minh

- ❔ Dữ liệu mẫu có Deadline trước Start Date (VD Start 14-05-2026, Deadline 14-06-2024) — form có chặn không? Kiểm ở recon module
- ❔ Nội dung tab Project Settings (quyền khách hàng xem dự án)
- ❔ Luồng Invoice Project → `INV`
- ⚠️ Môi trường dùng chung: **CẤM** đổi trạng thái dự án không do mình tạo
