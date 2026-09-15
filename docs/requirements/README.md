# Danh mục Requirements — Perfex CRM

> **Điểm vào cấp hệ thống.** Đọc file này đầu tiên: module nào đã có tài liệu · prefix nào đã chiếm · mã kế tiếp · ambiguity 🔴 còn treo.
> Bản đồ hệ thống: [`_discovery/system_map.md`](_discovery/system_map.md)

| Thuộc tính | Giá trị |
|---|---|
| **Hệ thống** | Perfex CRM — bản demo Anh Tester (khu vực quản trị `/admin/`) |
| **URL · tài khoản** | Xem `.env` (`BASE_URL`, `EMAIL_ADMIN`) — **KHÔNG** ghi vào `docs/` |
| **Tiền tố TC ID** | `CRM_` → `CRM_<MODULE>_TC_<3 số>` (VD `CRM_LOGIN_TC_001`) — chốt 2026-09-14 |
| **Môi trường dùng chung** | ✅ **CÓ** — chốt 2026-09-14. Recon chỉ đọc; TC phải tự sinh dữ liệu riêng, tự dọn; **CẤM** thao tác phá huỷ lên dữ liệu không do mình tạo; **CẤM** đổi mật khẩu / ngôn ngữ / cấu hình dùng chung của tài khoản test |
| **Tài khoản đang có** | 1 tài khoản (`EMAIL_ADMIN` trong `.env`) — tên hiển thị "Admin Example" nhưng **KHÔNG có quyền admin** (đo 2026-09-14: `app.user_is_admin` rỗng, menu Setup rỗng, 12 route cấu hình → `/admin/access_denied`). Xem AMB-01 |
| **Năng lực kiểm thử của QA** | Chốt 2026-09-14 — dùng cho nhánh Vòng 3 của **mọi** bộ TC:<br>• Gọi API: ❔ chưa chốt — user chưa trả lời, hỏi lại trước khi sinh TC nhánh API<br>• Truy vấn CSDL: ❔ chưa chốt<br>• Kiểm tầng tích hợp: ❔ chưa chốt<br>• Xem nhật ký hoạt động: ❌ tài khoản bị chặn (`/admin/utilities/activity_log` → `/admin/access_denied`, đo 2026-09-14) — cần tài khoản admin<br>• DevTools trình duyệt: ✅ có |
| **Viewport recon** | `1600×750` (headed) |

---

## 1. Bảng danh mục module

Thứ tự dòng = **thứ tự khảo sát đã chốt** (2026-09-14).

| # | Module | Prefix | Trạng thái recon | Mức phủ tài liệu | Tài liệu | REQ đã dùng | Mã kế tiếp | AMB treo | Story | Cập nhật |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Authentication (Đăng nhập) | `LOGIN` | ✅ Đã có tài liệu | ⬜ Trắng | [login/requirements_login.md](login/requirements_login.md) | `REQ-LOGIN-01` → `REQ-LOGIN-35` | `REQ-LOGIN-36` | 13 (🔴 AMB-06 · AMB-10 · AMB-12) | 4 | 2026-09-14 |
| 2 | Customers (+ Contacts) | `CUST` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-CUST-01` | AMB-01 | — | 2026-09-14 |
| 3 | Items | `ITEM` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-ITEM-01` | — | — | 2026-09-14 |
| 4 | Projects | `PRJ` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-PRJ-01` | — | — | 2026-09-14 |
| 5 | Tasks | `TASK` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-TASK-01` | — | — | 2026-09-14 |
| 6 | Invoices | `INV` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-INV-01` | AMB-01 | — | 2026-09-14 |
| 7 | Payments | `PAY` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-PAY-01` | AMB-01 | — | 2026-09-14 |
| 8 | Estimates | `EST` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-EST-01` | — | — | 2026-09-14 |
| 9 | Proposals | `PROP` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-PROP-01` | — | — | 2026-09-14 |
| 10 | Credit Notes | `CRN` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-CRN-01` | AMB-03 | — | 2026-09-14 |
| 11 | Contracts | `CTR` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-CTR-01` | — | — | 2026-09-14 |
| 12 | Expenses | `EXP` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-EXP-01` | AMB-03 | — | 2026-09-14 |
| 13 | Leads | `LEAD` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-LEAD-01` | AMB-03 | — | 2026-09-14 |
| 14 | Support (Tickets) | `TKT` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-TKT-01` | AMB-01 · AMB-03 | — | 2026-09-14 |
| 15 | Subscriptions | `SUB` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-SUB-01` | AMB-03 · AMB-05 | — | 2026-09-14 |
| 16 | Estimate Request | `ESTREQ` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-ESTREQ-01` | AMB-03 | — | 2026-09-14 |
| 17 | Knowledge Base | `KB` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-KB-01` | AMB-03 | — | 2026-09-14 |
| 18 | Dashboard (+ Announcements, thanh đầu trang) | `DASH` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-DASH-01` | — | — | 2026-09-14 |
| 19 | Cá nhân (Profile · Edit Profile · My Timesheets · To Do · Notifications) | `PROFILE` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-PROFILE-01` | — | — | 2026-09-14 |
| 20 | Reports | `RPT` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-RPT-01` | — | — | 2026-09-14 |
| 21 | Utilities (Media · Bulk PDF Export · Calendar) | `UTIL` | ⬜ Chưa khảo sát | ⬜ Trắng | — | — | `REQ-UTIL-01` | — | — | 2026-09-14 |
| 22 | Setup (cấu hình hệ thống) | `SETUP` | ⏸️ Hoãn — **BLOCKED**: tài khoản không có quyền (AMB-01) | ⬜ Trắng | — | — | `REQ-SETUP-01` | AMB-01 · AMB-02 · AMB-04 | — | 2026-09-14 |

**Tổng: 22 module** — ✅ 1 · 🟨 0 · ⬜ 20 · ⏸️ 1 · ⚪ 0. Mode khám phá: UI (không có tài liệu) → mọi module mức phủ ⬜ Trắng.

**Bảng mã trạng thái recon:** ⬜ Chưa khảo sát · 🟨 Đang khảo sát · ✅ Đã có tài liệu · ⏸️ Hoãn · ⚪ Chưa implement

### Danh sách prefix đã chiếm

`LOGIN` · `CUST` · `ITEM` · `PRJ` · `TASK` · `INV` · `PAY` · `EST` · `PROP` · `CRN` · `CTR` · `EXP` · `LEAD` · `TKT` · `SUB` · `ESTREQ` · `KB` · `DASH` · `PROFILE` · `RPT` · `UTIL` · `SETUP`

> Prefix đã cấp là **vĩnh viễn** — kể cả khi module đổi tên trên UI. Module mới **phải** chọn prefix ngoài danh sách này.
> Ranh giới đã chốt với user (2026-09-14): Contacts thuộc `CUST` · Timesheets cá nhân thuộc `PROFILE`, Timesheets overview thuộc `RPT`, tab Timesheets của dự án thuộc `PRJ` · Announcements thuộc `DASH` · toàn bộ cấu hình gộp `SETUP`.

---

## 2. Trạng thái REQ toàn hệ thống

| Module | 🟢 | 🟡 | 🔴 | ⚪ | Tổng |
|---|---|---|---|---|---|
| `LOGIN` | 31 | 0 | 0 | 4 | 35 |
| **Tổng** | **31** | **0** | **0** | **4** | **35** |

---

## 3. Ambiguity còn treo

Mã AMB đánh số **toàn hệ thống**. **AMB kế tiếp: `AMB-19`** — tài liệu module đánh tiếp từ số này, KHÔNG đánh lại từ 01.
Bảng dưới gom AMB cấp hệ thống + mọi AMB 🔴 High của module. AMB 🟡/🟢 của module nằm trong tài liệu module.

| Mã | Mức | Nội dung | Ảnh hưởng | Cần ai trả lời | Nguồn |
|---|---|---|---|---|---|
| AMB-01 | 🔴 High | Tài khoản trong `.env` được mô tả là admin nhưng **không có quyền admin**: `app.user_is_admin` rỗng, menu Setup rỗng, 12 route cấu hình → `/admin/access_denied`. Xin tài khoản admin thật | Chặn toàn bộ `SETUP`; không xem được Activity Log; không kiểm được cấu hình đứng sau `CUST` (Customer Groups), `INV`/`PAY` (Taxes, Currencies, Payment Modes), `TKT` (Departments) | PO / chủ môi trường | Kiểm chứng thực tế · DOM `#setup-menu` + điều hướng thẳng URL |
| AMB-02 | 🔴 High | Hệ thống có những role nào, quyền từng role ra sao? Không mở được `/admin/roles`, `/admin/staff` → ma trận phân quyền cấp module toàn `❔` với mọi role ngoài tài khoản hiện tại. Xin tài khoản cho từng role | Mọi mục 6.5 (Ma trận phân quyền) ở tầng module | PO | Kiểm chứng thực tế · `/admin/roles` → access_denied |
| AMB-03 | 🟡 Medium | Leads, Support, Expenses, Credit Notes, Subscriptions, Estimate Request, Knowledge Base, Announcements đều "No entries found" trên môi trường demo dùng chung. **Trống thật** hay tài khoản bị giới hạn "chỉ xem của mình"? | Không mở được màn hình chi tiết → chưa đếm được tab con; không phân biệt được "rỗng" với "bị lọc theo quyền" | PO / chủ môi trường | UI thực tế |
| AMB-04 | 🟡 Medium | `/admin/modules` bị chuyển về Dashboard (`/admin/`) thay vì `/admin/access_denied` như 11 route cấu hình khác — hành vi chặn quyền **không nhất quán** | Rule phân quyền của `SETUP` | Dev | Kiểm chứng thực tế · điều hướng thẳng URL |
| AMB-05 | 🟡 Medium | Subscriptions gắn với Stripe (logo stripe, nút "Select Stripe plan"). Môi trường demo đã cấu hình Stripe chưa? | Không cấu hình → luồng tạo subscription không kiểm được đầu-cuối | Chủ môi trường | UI thực tế · `/admin/subscriptions/create` |
| AMB-06 | 🔴 High | `LOGIN` — Remember me có hoạt động? Sau khi đăng nhập có tick chỉ thấy `csrf_cookie_name` + `sp_session` (hạn < 1 ngày), không có cookie ghi nhớ riêng | REQ-LOGIN-19/20 ⚪ BLOCKED | PO / Dev | Kiểm chứng thực tế · `context.cookies()` · [login](login/requirements_login.md) |
| AMB-10 | 🔴 High | `LOGIN` — Forgot Password báo "Email not found" cho email không tồn tại → có cho dò email tồn tại không? Mâu thuẫn với form Login (giấu thông tin) | Rủi ro lộ danh sách tài khoản staff | PO / Dev | Kiểm chứng thực tế · [login](login/requirements_login.md) |
| AMB-12 | 🔴 High | `LOGIN` — Luồng email đặt lại mật khẩu + liên kết reset chưa kiểm được: cần hộp thư test + tài khoản riêng | REQ-LOGIN-29/30 ⚪ BLOCKED | Chủ môi trường | Môi trường dùng chung · [login](login/requirements_login.md) |

---

## 4. Cấu trúc thư mục chuẩn

```
docs/requirements/
├── README.md                              ← DANH MỤC (file này)
├── _discovery/                            ← TẦNG KHÁM PHÁ — cấp hệ thống, KHÔNG có mã REQ
│   ├── system_map.md                      ← INDEX bất biến
│   ├── modules/module_NN_<slug>.md        ← chi tiết từng nhóm module
│   └── evidence/*.png                     ← 1 ảnh tổng quan mỗi module
└── <module>/
    ├── requirements_<module>.md           ← INDEX — TÊN FILE BẤT BIẾN
    ├── evidence/*.png
    ├── stories/story_NN_<slug>.md         ← chỉ khi tách
    ├── analysis/analysis_<TICKET-ID>.md
    └── impact/impact_<TICKET-ID>.md
```

## 5. Quy trình sử dụng

| Tình huống | Workflow | Ghi vào đâu |
|---|---|---|
| Khảo sát module kế tiếp | `/generate-requirements-from-website <module>` | `<module>/requirements_<module>.md` → cập nhật dòng module ở mục 1 sang ✅ + dải REQ |
| Có ticket / tài liệu cho module | `/analyze-requirement-document` | `<module>/analysis/` |
| Module đã có tài liệu, có ticket thay đổi | `/update-requirements-from-ticket` | Sửa tại chỗ + `<module>/impact/` |
| Phát hiện module bị sót | `/discover-system` (mode ADD) | Thêm dòng mục 1 + `_discovery/` |
| Hệ thống vừa deploy tính năng mới | `/discover-system` (mode DELTA) | Nhật ký khám phá trong `system_map.md` |
| Có tài khoản admin (gỡ AMB-01) | `/discover-system` (mode ADD) cho `SETUP` | Đổi `SETUP` từ ⏸️ sang ⬜ |

## 6. Nhật ký danh mục

| Ngày | Thay đổi | Lý do |
|---|---|---|
| 2026-09-14 | `LOGIN` ⬜ → ✅ · `REQ-LOGIN-01` → `35` · 4 Story · mở AMB-06 → AMB-18 (🔴 AMB-06, AMB-10, AMB-12 đưa lên mục 3) · AMB kế tiếp `AMB-19` | `/generate-requirements-from-website` LOGIN — UI recon, không tài liệu |
| 2026-09-14 | Khởi tạo danh mục · cấp 22 prefix · `SETUP` ⏸️ BLOCKED · mở AMB-01 → AMB-05 | `/discover-system` mode UI lần đầu. Đối chiếu Bước 1: `docs/` chưa tồn tại → không có điểm lệch |
