# Bản đồ hệ thống — Perfex CRM

> **INDEX tầng khám phá — tên file bất biến.** Không chứa mã `REQ-XXX-NN`; chỉ cấp prefix.
> Trạng thái recon của từng module **chỉ** ghi ở [`../README.md`](../README.md) — file này không nhân bản.

## 1. Bối cảnh khảo sát

| Mục | Giá trị |
|---|---|
| Ngày | 2026-09-14 |
| Mode | **UI** — không có tài liệu, hệ thống truy cập được |
| URL | Xem `BASE_URL` trong `.env`. Mọi route dưới đây là đường dẫn tương đối |
| Role đã dùng | 1 tài khoản (`EMAIL_ADMIN` trong `.env`) — tên hiển thị "Admin Example", **không có quyền admin** (`app.user_is_admin` rỗng · `body` class `user-id-2`). Đăng nhập do user tự thực hiện |
| Môi trường dùng chung | ✅ Có — toàn bộ khảo sát **chỉ đọc**: mở danh sách, mở form tạo mới để đếm field, mở chi tiết 1 bản ghi; **không** bấm Save / Delete / đổi trạng thái |
| Phạm vi crawl | Toàn bộ `#side-menu` (16 mục, 3 mục có menu con) · menu tạo nhanh + menu hồ sơ ở thanh đầu trang · gom `a[href*="/admin/"]` trên Dashboard · 12 route cấu hình thử bằng điều hướng thẳng URL (chỉ URL đọc) · form tạo mới của 11 entity · màn hình chi tiết của 6 entity có bản ghi · trang login & quên mật khẩu (trình duyệt riêng, chưa đăng nhập) |
| Tầng network | Chỉ quan sát thụ động request XHR/fetch do UI tự phát sinh — không gọi API trực tiếp |
| Viewport | `1600×750` |
| Tổng số trang đã mở | 51 route danh sách/form/cấu hình + 18 route chi tiết/phụ |

## 2. Sơ đồ điều hướng toàn hệ thống

```
[Chưa đăng nhập]
  /admin/authentication                    Login
  /admin/authentication/forgot_password    Forgot Password

[Thanh đầu trang — mọi trang]
  Ô Search · nút (+) tạo nhanh · icon chia sẻ · To Do (badge) · ảnh hồ sơ · Timer (badge) · Notifications
  (+) tạo nhanh → Invoice · Estimate · Proposal · Credit Note · Customer · Subscription · Project
                   · Expense · Contract · Article · Ticket · Event
  Hồ sơ        → My Profile · My Timesheets · Edit Profile · Language (System Default + 26 ngôn ngữ) · Logout

[Sidebar #side-menu]
  Dashboard ............ /admin/
  Customers ............ /admin/clients
  Projects ............. /admin/projects
  Tasks ................ /admin/tasks
  Contracts ............ /admin/contracts
  Sales ▸
    Proposals .......... /admin/proposals
    Estimates .......... /admin/estimates
    Invoices ........... /admin/invoices
    Payments ........... /admin/payments
    Credit Notes ....... /admin/credit_notes
    Items .............. /admin/invoice_items
  Subscriptions ........ /admin/subscriptions
  Expenses ............. /admin/expenses
  Support .............. /admin/tickets
  Leads ................ /admin/leads
  Estimate Request ..... /admin/estimate_request
  Knowledge Base ....... /admin/knowledge_base
  Utilities ▸
    Media .............. /admin/utilities/media
    Bulk PDF Export .... /admin/utilities/bulk_pdf_exporter
    Calendar ........... /admin/utilities/calendar
  Reports ▸
    Sales .............. /admin/reports/sales
    Expenses ........... /admin/reports/expenses
    Expenses vs Income . /admin/reports/expenses_vs_income
    Leads .............. /admin/reports/leads
    Timesheets overview  /admin/staff/timesheets?view=all
    KB Articles ........ /admin/reports/knowledge_base_articles

[Menu Setup — #setup-menu]
  DOM chỉ có tiêu đề "Setup" + nút đóng, KHÔNG có mục nào với tài khoản hiện tại

[Không có trong menu — vào bằng URL / nút]
  /admin/announcements  ·  /admin/todo  ·  /admin/profile  ·  /admin/staff/edit_profile
  /admin/clients/all_contacts  ·  /admin/invoices/recurring  ·  /admin/tasks/detailed_overview
  /admin/invoice_items/groups  ·  /admin/knowledge_base/manage_groups  ·  /admin/misc/reminders
```

## 3. Bảng module tổng

| # | Tên UI (nguyên văn) | Bí danh | Prefix | File khám phá | Loại màn hình | Risk | Ước REQ |
|---|---|---|---|---|---|---|---|
| 1 | Login · Forgot Password | Authentication | `LOGIN` | [module_01](modules/module_01_dang_nhap.md) | Form | 🔴 | ~12 |
| 2 | Customers · Contacts | Clients | `CUST` | [module_02](modules/module_02_khach_hang_lien_he.md) | Danh sách · Form · Chi tiết 19 tab | 🔴 | ~40 |
| 3 | Items | Invoice Items | `ITEM` | [module_03](modules/module_03_mat_hang.md) | Danh sách · Modal | 🟡 | ~15 |
| 4 | Projects | — | `PRJ` | [module_04](modules/module_04_du_an.md) | Danh sách · Form · Chi tiết 12 tab | 🔴 | ~45 |
| 5 | Tasks | — | `TASK` | [module_05](modules/module_05_cong_viec.md) | Danh sách · Modal · Tổng quan | 🔴 | ~35 |
| 6 | Invoices | — | `INV` | [module_06](modules/module_06_hoa_don.md) | Danh sách · Form dòng hàng · Chi tiết 6 tab | 🔴 | ~40 |
| 7 | Payments | — | `PAY` | [module_07](modules/module_07_thanh_toan_ghi_co.md) | Danh sách | 🔴 | ~15 |
| 8 | Estimates | — | `EST` | [module_08](modules/module_08_bao_gia_de_xuat_yeu_cau.md) | Danh sách · Form dòng hàng · Chi tiết 5 tab | 🟡 | ~30 |
| 9 | Proposals | — | `PROP` | [module_08](modules/module_08_bao_gia_de_xuat_yeu_cau.md) | Danh sách · Form dòng hàng · Chi tiết 6 tab | 🟡 | ~30 |
| 10 | Credit Notes | — | `CRN` | [module_07](modules/module_07_thanh_toan_ghi_co.md) | Danh sách · Form dòng hàng | 🟡 | ~25 |
| 11 | Contracts | — | `CTR` | [module_09](modules/module_09_hop_dong.md) | Danh sách + biểu đồ · Form · Chi tiết 7 tab | 🟡 | ~30 |
| 12 | Expenses | — | `EXP` | [module_10](modules/module_10_chi_phi.md) | Danh sách · Form | 🟡 | ~25 |
| 13 | Leads | — | `LEAD` | [module_11](modules/module_11_khach_tiem_nang.md) | Danh sách · Kanban · Modal | 🔴 | ~35 |
| 14 | Support | Tickets | `TKT` | [module_12](modules/module_12_ho_tro_kien_thuc.md) | Danh sách · Form | 🟡 | ~30 |
| 15 | Subscriptions | — | `SUB` | [module_13](modules/module_13_goi_dang_ky.md) | Danh sách · Form | 🟡 | ~15 |
| 16 | Estimate Request | — | `ESTREQ` | [module_08](modules/module_08_bao_gia_de_xuat_yeu_cau.md) | Danh sách · Form builder | 🟡 | ~15 |
| 17 | Knowledge Base | — | `KB` | [module_12](modules/module_12_ho_tro_kien_thuc.md) | Danh sách · Form | 🟢 | ~15 |
| 18 | Dashboard · Announcements · thanh đầu trang | — | `DASH` | [module_14](modules/module_14_tong_quan_ca_nhan.md) | Dashboard | 🟢 | ~10 |
| 19 | My Profile · Edit Profile · My Timesheets · My To Do Items · Notifications | — | `PROFILE` | [module_14](modules/module_14_tong_quan_ca_nhan.md) | Form · Danh sách | 🟡 | ~25 |
| 20 | Reports | — | `RPT` | [module_15](modules/module_15_bao_cao_tien_ich.md) | Báo cáo | 🟡 | ~25 |
| 21 | Utilities (Media · Bulk PDF Export · Calendar) | — | `UTIL` | [module_15](modules/module_15_bao_cao_tien_ich.md) | Tiện ích | 🟢 | ~20 |
| 22 | Setup | — | `SETUP` | [module_16](modules/module_16_cau_hinh_he_thong.md) | Cấu hình — **BLOCKED** | 🔴 | ❔ |

**Tổng: 22 module · 22 prefix · 16 file khám phá · ước ~527 REQ (chưa tính `SETUP`).**

## 4. Bản đồ entity & phụ thuộc

> Quan hệ lấy từ **nhãn cột bảng, field form, tab chi tiết và nút chuyển đổi** quan sát được. ✅ = thấy nút/tab trực tiếp · ⚠️ = suy từ nhãn cột/field, chưa kiểm chứng hành vi.

```
                         ┌──────── Setup (BLOCKED): Taxes · Currencies · Payment Modes · Customer Groups
                         │                           Departments · Staff · Roles · Custom Fields · Emails
                         ▼
 Lead ──(chuyển KH ⚠️)──▶ Customer ◀── Contact (tab Contacts ✅)
   ▲                         │
   │                         ├──▶ Project ──▶ Task · Milestone · Discussion · Timesheet (tab ✅)
 Estimate Request ⚠️          │        └──▶ "Invoice Project" ✅ ─┐
                             ├──▶ Proposal ──(Convert ✅)──▶ Estimate / Invoice ⚠️
                             ├──▶ Estimate ──(Convert to Invoice ✅)──▶ Invoice
                             ├──▶ Invoice ──▶ Payment (tab Payments ✅ · nút Payment ✅ · Batch Payments ✅)
                             ├──▶ Credit Note ──(Remaining Amount ⚠️ trừ vào Invoice)
                             ├──▶ Contract (cột Customer, Project ⚠️)
                             ├──▶ Expense (cột Customer, Project, Invoice ⚠️)
                             ├──▶ Subscription (Stripe ⚠️)
                             └──▶ Ticket (cột Contact, Department ⚠️) ◀── Knowledge Base ("Insert knowledge base link" ✅)
 Item ──▶ dòng hàng của Proposal · Estimate · Invoice · Credit Note (bảng Item/Description/Qty/Rate/Tax/Amount ✅)
 Task ──▶ gắn vào Invoice · Estimate · Proposal · Contract (tab Tasks ✅) · "Bill Tasks" trên form Invoice ✅
```

**Module được phụ thuộc nhiều nhất:** `CUST` (≥ 12 tab liên kết) → `ITEM` → `PRJ` → `INV`.

### Phát hiện network cấp hệ thống

| Phát hiện | Chi tiết | Hệ quả cho recon module |
|---|---|---|
| Bảng danh sách dùng DataTables server-side | Mẫu chung `POST /admin/<entity>/table` (clients, projects, tasks, contracts, proposals, estimates, invoices, payments, credit_notes, invoice_items, subscriptions, expenses, leads, estimate_request) | Phân trang / tìm kiếm / sắp xếp chạy ở server — phải bắt response khi recon |
| CSRF token trên request | Tham số `csrf_token_name` dạng `<32 ký tự hex>` | Không ghi giá trị vào tài liệu |
| Dữ liệu chi tiết nạp bằng AJAX | `GET /admin/<entity>/get_<entity>_data_ajax/{id}` (invoices, estimates, proposals) | Màn hình chi tiết = khung danh sách + panel nạp động |
| Tiền tệ | `GET /admin/misc/get_currency/{id}` — gọi khi mở form Invoice / Estimate / Proposal / Credit Note | Phụ thuộc cấu hình Currencies (Setup — BLOCKED) |
| Lịch | `GET /admin/utilities/get_calendar_data` — gọi ở Dashboard và Calendar | Dữ liệu sự kiện cắt ngang Project / Contract / Task |
| Chặn quyền | Route không đủ quyền → chuyển hướng `/admin/access_denied`; riêng `/admin/modules` → `/admin/` | AMB-04 |
| Timer công việc | Trang có modal ẩn "Started tasks timers found! Are you sure you want to logout without stopping the timers?" | Liên quan `TASK` + `LOGIN` (logout) |

## 5. Ma trận phân quyền sơ bộ cấp module

> Chỉ có 1 tài khoản → áp thang 3 mức (skill 3.1.2). ✅/❌ = đã kiểm chứng bằng điều hướng thật · ❔ = chưa có căn cứ.

| Module | Tài khoản hiện tại (không phải admin) | Admin | Role khác |
|---|---|---|---|
| `LOGIN` · `CUST` · `ITEM` · `PRJ` · `TASK` · `INV` · `PAY` · `EST` · `PROP` · `CRN` · `CTR` · `EXP` · `LEAD` · `TKT` · `SUB` · `ESTREQ` · `KB` · `DASH` · `PROFILE` · `RPT` · `UTIL` (21 module) | ✅ vào được trang danh sách / trang chính | ❔ | ❔ |
| `CUST` — Customer Groups (`/admin/clients/groups`) | ❌ access_denied | ❔ | ❔ |
| `SETUP` — 11 route cấu hình + Activity Log | ❌ access_denied (`/admin/modules` → Dashboard) | ❔ | ❔ |

**Đã kiểm chứng: 23 ô · Suy diễn: 0 ô · Chưa rõ: 46 ô.** Danh sách role của hệ thống: ❔ (AMB-02).
> "Vào được trang danh sách" ≠ có quyền tạo/sửa/xoá — quyền thao tác kiểm ở tầng module.

## 6. Thứ tự khảo sát đã chốt

Chốt với user 2026-09-14 — **phụ thuộc trước, risk sau**:

```
LOGIN → CUST → ITEM → PRJ → TASK → INV → PAY → EST → PROP → CRN → CTR → EXP
      → LEAD → TKT → SUB → ESTREQ → KB → DASH → PROFILE → RPT → UTIL → SETUP
```

| Module BLOCKED | Chặn bởi | Gỡ khi |
|---|---|---|
| `SETUP` | AMB-01 — tài khoản không có quyền admin | Có tài khoản admin thật → chạy `/discover-system` mode ADD cho `SETUP` |

⚠️ Recon `INV` · `PAY` · `CRN` · `TKT` · `LEAD` sẽ gặp field phụ thuộc cấu hình trong Setup (thuế, tiền tệ, phương thức thanh toán, phòng ban, trạng thái/nguồn lead) — ghi `❔` + tham chiếu AMB-01, không suy đoán danh sách giá trị.

## 7. Nhật ký khám phá

| Ngày | Mode | Phạm vi | Kết quả | Nguồn |
|---|---|---|---|---|
| 2026-09-14 | Recon module | `LOGIN` | Lệch so với bản đồ: ước ~12 REQ → thực tế **35 REQ / 4 Story** (thêm luồng Logout + chuyển hướng chặn truy cập) · ❔ 2FA: **không** xuất hiện bước thứ hai với tài khoản test · Logout có 2 phần tử `li.header-logout` (1 ẩn trong `#mobile-collapse`) + popup cảnh báo timer khi tài khoản có timer chạy · Forgot Password không có link quay lại Login · route chặn/logout trả `307` (AMB-09) | Kiểm chứng thực tế · [login](../login/requirements_login.md) |
| 2026-09-14 | UI | Toàn hệ thống, 1 tài khoản | Lần đầu: 22 module · 22 prefix · `SETUP` BLOCKED · AMB-01 → AMB-05 · 21 ảnh evidence | UI thực tế |

## Bản đồ tài liệu

Trạng thái recon: xem cột tương ứng ở [`../README.md`](../README.md) — không nhân bản ở đây.

| File | Module bao phủ | Prefix |
|---|---|---|
| [modules/module_01_dang_nhap.md](modules/module_01_dang_nhap.md) | Authentication | `LOGIN` |
| [modules/module_02_khach_hang_lien_he.md](modules/module_02_khach_hang_lien_he.md) | Customers (+ Contacts) | `CUST` |
| [modules/module_03_mat_hang.md](modules/module_03_mat_hang.md) | Items | `ITEM` |
| [modules/module_04_du_an.md](modules/module_04_du_an.md) | Projects | `PRJ` |
| [modules/module_05_cong_viec.md](modules/module_05_cong_viec.md) | Tasks | `TASK` |
| [modules/module_06_hoa_don.md](modules/module_06_hoa_don.md) | Invoices | `INV` |
| [modules/module_07_thanh_toan_ghi_co.md](modules/module_07_thanh_toan_ghi_co.md) | Payments · Credit Notes | `PAY` · `CRN` |
| [modules/module_08_bao_gia_de_xuat_yeu_cau.md](modules/module_08_bao_gia_de_xuat_yeu_cau.md) | Estimates · Proposals · Estimate Request | `EST` · `PROP` · `ESTREQ` |
| [modules/module_09_hop_dong.md](modules/module_09_hop_dong.md) | Contracts | `CTR` |
| [modules/module_10_chi_phi.md](modules/module_10_chi_phi.md) | Expenses | `EXP` |
| [modules/module_11_khach_tiem_nang.md](modules/module_11_khach_tiem_nang.md) | Leads | `LEAD` |
| [modules/module_12_ho_tro_kien_thuc.md](modules/module_12_ho_tro_kien_thuc.md) | Support · Knowledge Base | `TKT` · `KB` |
| [modules/module_13_goi_dang_ky.md](modules/module_13_goi_dang_ky.md) | Subscriptions | `SUB` |
| [modules/module_14_tong_quan_ca_nhan.md](modules/module_14_tong_quan_ca_nhan.md) | Dashboard · Cá nhân | `DASH` · `PROFILE` |
| [modules/module_15_bao_cao_tien_ich.md](modules/module_15_bao_cao_tien_ich.md) | Reports · Utilities | `RPT` · `UTIL` |
| [modules/module_16_cau_hinh_he_thong.md](modules/module_16_cau_hinh_he_thong.md) | Setup | `SETUP` |

**Tự kiểm:** 16 file · 22 module (1+1+1+1+1+1+2+3+1+1+1+2+1+2+2+1) = 22 dòng ở mục 3 ✅

### Danh mục Evidence (`evidence/`)

| Tệp | Màn hình · trạng thái | Module | Ghi chú phạm vi |
|---|---|---|---|
| `login_overview_viewport.png` | Login, chưa đăng nhập | `LOGIN` | |
| `cust_overview_header_clip.png` | Customers — thanh công cụ + Summary + tiêu đề cột | `CUST` | Cắt vùng đầu trang: danh sách chứa email/SĐT khách hàng |
| `item_overview_viewport.png` | Items — danh sách | `ITEM` | |
| `prj_overview_viewport.png` | Projects — Summary + danh sách | `PRJ` | |
| `task_overview_viewport.png` | Tasks — Summary + danh sách | `TASK` | |
| `inv_overview_viewport.png` | Invoices — danh sách (menu Sales mở) | `INV` | |
| `pay_overview_viewport.png` | Payments — danh sách | `PAY` | |
| `est_overview_viewport.png` | Estimates — danh sách | `EST` | |
| `prop_overview_header_clip.png` | Proposals — thanh công cụ + tiêu đề cột | `PROP` | Cắt vùng đầu trang: cột "To" chứa email người nhận |
| `crn_overview_viewport.png` | Credit Notes — danh sách rỗng | `CRN` | |
| `ctr_overview_viewport.png` | Contracts — Summary + biểu đồ | `CTR` | Bảng danh sách nằm dưới viewport |
| `exp_overview_viewport.png` | Expenses — danh sách rỗng | `EXP` | |
| `lead_overview_viewport.png` | Leads — danh sách rỗng | `LEAD` | |
| `tkt_overview_viewport.png` | Support — Summary + danh sách rỗng | `TKT` | |
| `sub_overview_viewport.png` | Subscriptions — Summary Stripe + danh sách rỗng | `SUB` | |
| `estreq_overview_viewport.png` | Estimate Request — danh sách rỗng | `ESTREQ` | |
| `kb_overview_viewport.png` | Knowledge Base — danh sách rỗng | `KB` | |
| `dash_overview_viewport.png` | Dashboard — phần trên | `DASH` | |
| `dash_announcements_viewport.png` | Announcements — danh sách rỗng | `DASH` | |
| `profile_todo_viewport.png` | My To Do Items | `PROFILE` | Chưa có ảnh My Profile / Edit Profile — trang chứa thông tin cá nhân tài khoản |
| `rpt_sales_viewport.png` | Reports › Sales | `RPT` | |
| `util_calendar_viewport.png` | Utilities › Calendar tháng 09/2026 | `UTIL` | |
| — | `SETUP` | `SETUP` | Không có ảnh — mọi route bị chuyển về access_denied; bằng chứng là kết quả điều hướng ghi ở module_16 |

Mọi ảnh trong bảng đã được mở lại xác nhận đúng trạng thái trước khi ghi danh mục.
