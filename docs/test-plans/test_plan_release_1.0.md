# Master Test Plan — Perfex CRM · Release 1.0

## Kiểm soát tài liệu

### Thông tin tài liệu

| | |
|---|---|
| Mã tài liệu | `test_plan_release_1.0` |
| Phiên bản tài liệu | v1.0 |
| Trạng thái | 🟨 Draft — còn 19 ô chờ thông tin |
| Mức phân loại | ❓ Chờ QA Lead chọn: công khai · nội bộ · mật |
| Ngày lập | 18-09-2026 |
| Ngày hiệu lực | — (chưa duyệt) |
| Người lập | Anh Tester — trưởng nhóm QA (phiếu để trống `Người lập` → lấy người có vai trò `trưởng nhóm QA`) |
| Người review | ❓ Chờ QA Lead chỉ định |
| Người phê duyệt | Anh Tester — QA Lead · ❓ Product Owner (chưa có tên) — chữ ký ở mục 11 |
| Hệ thống · Build | Perfex CRM (khu vực quản trị `/admin/`) · `v1.0.0` |
| Phiếu đầu vào | [`test_plan_release_1.0.input.yaml`](test_plan_release_1.0.input.yaml) (bản lưu của `plans/master-test-plan/test_plan.config.yaml`) |
| Cấu trúc tài liệu | Biên soạn **theo cấu trúc** ISO/IEC/IEEE 29119-3 — Test Plan · phủ đủ nội dung điển hình của ISTQB CTFL v4.0 mục 5.1.1 · ánh xạ ở mục 12 |

> **Trạng thái hợp lệ:** 🟨 Draft (đang soạn / còn ô treo) → 🟦 Chờ duyệt (đã review, không còn ô treo chặn) → 🟩 Đã duyệt (đủ chữ ký mục 11) → ⬛ Hết hiệu lực (có bản mới thay thế). Sửa nội dung bản 🟩 → quay về 🟨, tăng phiên bản.

> **Ô còn treo (19)** — gom theo người trả lời:
>
> **QA Lead (Anh Tester)**
> - **1.** Mức phân loại tài liệu (Kiểm soát tài liệu)
> - **2.** Người review plan (Kiểm soát tài liệu)
> - **3.** Duyệt các mục tiêu O1–O4 do agent đề xuất (1.1)
> - **4.** Người chịu trách nhiệm cho Hiệu năng và Bảo mật chuyên sâu, hai loại đã loại khỏi phạm vi (2.2)
> - **5.** Tương thích · Khả năng truy cập · Khả dụng · Độ tin cậy & phục hồi: có hay không (3.2.1)
> - **6.** Mức độc lập của kiểm thử thể hiện ở đâu, ví dụ review TC chéo (3.4)
> - **7.** Chiến lược tự động hoá: mục tiêu · phần không tự động · tỷ trọng tầng · tiêu chí chọn TC · kích hoạt chạy · người bảo trì (3.7)
> - **8.** Công cụ khác ngoài Jira / Playwright / GitHub Actions (5.3)
> - **9.** Nhu cầu đào tạo của từng người (6)
>
> **QA Lead + Dev Lead**
> - **10.** Quy trình trạng thái lỗi và thang Severity/Priority: dùng mặc định hay riêng (9.1–9.3)
> - **11.** Người phân loại lỗi và tần suất họp phân loại (9.4)
> - **12.** Thời hạn phản hồi / sửa xong theo Severity (9.4)
>
> **PM / Product Owner**
> - **13.** Tên Product Owner, người duyệt plan và làm UAT (2.4 · 11)
> - **14.** AMB-01 · AMB-02 🔴: cấp tài khoản admin thật và danh sách role (4.1 #3 · #7)
> - **15.** AMB-19 🟢: số lần thử sai mật khẩu để khẳng định "không khoá" (REQ-LOGIN-36)
>
> **Đội DEV / chủ môi trường**
> - **16.** Dữ liệu kiểm thử: dữ liệu nền · nguồn · có dữ liệu thật không · dọn dữ liệu · làm mới · người cung cấp (5.2)
> - **17.** Tài khoản test riêng và hộp thư test trên môi trường mới (4.1 #3 · 2.1 bảng REQ cần quyết định lại)
> - **18.** Năng lực kiểm thử của QA trên môi trường mới: gọi API · truy vấn CSDL · kiểm tầng tích hợp (2.3 · 3.2)
>
> **Người có bản chuẩn ISO/IEC/IEEE 29119-3**
> - **19.** Đối chiếu tên mục 29119-3 ở mục 12.1 trước khi đem đi audit

### Lịch sử thay đổi

| Phiên bản | Ngày | Người sửa | Mục thay đổi | Nội dung | Người duyệt |
|---|---|---|---|---|---|
| v1.0 | 18-09-2026 | Anh Tester (QA Lead) | Toàn bộ | Lập mới. Trước khi lập, phiếu đã được sửa theo xác nhận của QA Lead ngày 18-09-2026: danh sách module ngoài phạm vi theo prefix của danh mục · thay namespace `_book-api/` (không có trong repo) bằng `_f2c/` · CI là GitHub Actions · câu giả định ước lượng theo số liệu repo (CUST, PRJ chưa khảo sát · LOGIN chưa có TC) | ❓ |

---

## 1. Mục tiêu & Cơ sở kiểm thử

### 1.1 Mục tiêu kiểm thử

> ⚠️ Phiếu để trống `Mục tiêu` → agent đề xuất, **chờ QA Lead / PO duyệt**.

| # | Mục tiêu | Đo bằng |
|---|---|---|
| O1 | Xác nhận đăng nhập, quên mật khẩu, đăng xuất và chặn truy cập chưa đăng nhập (`LOGIN` × web) hoạt động đúng đặc tả | Tiêu chí exit #3, #4, #6 |
| O2 | Xác nhận quản lý khách hàng + liên hệ (`CUST` × web) và dự án (`PRJ` × web), kể cả liên kết khách hàng → dự án | Tiêu chí exit #3, #4, #7 |
| O3 | Không còn lỗi Critical, và không còn lỗi Major chưa có workaround, ở 3 module trước phát hành | Tiêu chí exit #1, #2 |
| O4 | Bộ Smoke và regression tự động của 3 module chạy được trên CI trước ngày 20-11-2026 (bắt đầu hồi quy) | Chỉ số 3.6 nhóm Tiến độ kiểm thử · báo riêng theo 3.7 |

### 1.2 Cơ sở kiểm thử (Test basis)

| Tài liệu | Phiên bản / ngày cập nhật | Module | Ghi chú |
|---|---|---|---|
| [`docs/requirements/login/requirements_login.md`](../requirements/login/requirements_login.md) | Nhật ký thay đổi 18-09-2026 (`PO-AMB-20260918`) | `LOGIN` | 37 REQ (🟢 32 · 🟡 1 · ⚪ 4) · 1 AMB 🟢 treo (AMB-19) · RISK-01 → RISK-06 |
| [`docs/requirements/login/impact/impact_PO-AMB-20260918.md`](../requirements/login/impact/impact_PO-AMB-20260918.md) | 18-09-2026 | `LOGIN` | Quyết định PO cho AMB-06 → AMB-18 |
| [`docs/requirements/_discovery/modules/module_02_khach_hang_lien_he.md`](../requirements/_discovery/modules/module_02_khach_hang_lien_he.md) | Khám phá 14-09-2026 | `CUST` | **Chỉ là bản đồ khám phá — chưa có REQ.** Ước ~40 REQ · risk 🔴 |
| [`docs/requirements/_discovery/modules/module_04_du_an.md`](../requirements/_discovery/modules/module_04_du_an.md) | Khám phá 14-09-2026 | `PRJ` | **Chỉ là bản đồ khám phá — chưa có REQ.** Ước ~45 REQ · risk 🔴 |
| [`docs/requirements/_discovery/system_map.md`](../requirements/_discovery/system_map.md) | Khám phá 14-09-2026 | Cả 3 | Phụ thuộc giữa module · ma trận phân quyền sơ bộ |

> Cơ sở kiểm thử của `CUST` và `PRJ` **chưa tồn tại** — phải chạy `/generate-requirements-from-website` cho 2 module này trước khi viết TC (tiêu chí vào #6, rủi ro R1).
>
> Cơ sở kiểm thử **đổi giữa đợt** (ticket sửa yêu cầu) → cập nhật bằng `/update-requirements-from-ticket` rồi tăng phiên bản plan — TC viết theo cơ sở cũ là TC sai.

## 2. Phạm vi

### 2.1 Trong phạm vi

> Mỗi dòng là **một module × một nền tảng** — đơn vị báo cáo tiến độ theo dõi và báo cáo tổng hợp chấm tiêu chí exit #7.

| Hệ thống | Module | Prefix | Nền tảng | Số REQ | Số TC hiện có | Đã từng chạy? | Ghi chú |
|---|---|---|---|---|---|---|---|
| Perfex CRM | Authentication (Đăng nhập) | `LOGIN` | web | 37 | 0 | Chưa | Đã có requirements · chưa có TC |
| Perfex CRM | Customers (+ Contacts) | `CUST` | web | 0 — ⬜ chưa khảo sát (bản đồ ước ~40) | 0 | Chưa | Customer Groups bị chặn quyền với tài khoản hiện tại (AMB-01) |
| Perfex CRM | Projects | `PRJ` | web | 0 — ⬜ chưa khảo sát (bản đồ ước ~45) | 0 | Chưa | Phụ thuộc `CUST` (dự án gắn khách hàng) |

**Tổng: 3 cặp module × nền tảng**, toàn bộ trên web.

**REQ cần quyết định lại** — REQ ⚪ trước đây chưa kiểm được vì môi trường dùng chung:

| REQ | Nội dung | Lý do bị loại trước đây | Quyết định theo phiếu |
|---|---|---|---|
| REQ-LOGIN-19 | Remember me tạo cookie ghi nhớ đăng nhập | Cần phép thử sạch trên tài khoản riêng; không làm được trên tài khoản dùng chung (AMB-06 ✅) | **Đưa lại vào phạm vi** (`Đưa lại REQ bị loại vì môi trường: có`), với điều kiện có tài khoản test riêng trên môi trường mới (ô treo 17) |
| REQ-LOGIN-20 | Cookie ghi nhớ tự đăng nhập lại khi phiên kết thúc | Chỉ kiểm được sau khi REQ-19 có kết quả phép thử sạch (AMB-06 ✅) | **Đưa lại**, chạy sau REQ-19 |
| REQ-LOGIN-29 | Email tồn tại nhận được email đặt lại mật khẩu | Môi trường dùng chung cấm gửi yêu cầu với email thật; chưa có hộp thư test (AMB-12 ✅) | **Đưa lại**, với điều kiện có hộp thư test. Chưa có thì TC vẫn gắn `skip` như PO đã chốt |
| REQ-LOGIN-30 | Liên kết đặt lại mật khẩu dùng được để đặt mật khẩu mới | Phụ thuộc REQ-29 (AMB-12 ✅) | **Đưa lại**, chạy sau REQ-29 |

> REQ-LOGIN-36 và 37 đang 🟢 nhưng AC ghi **chỉ chạy trên tài khoản riêng** — cùng điều kiện với REQ-19/20.

### 2.2 NGOÀI phạm vi (out of scope)

| Không kiểm thử | Lý do | Ai chịu trách nhiệm | Nguồn quyết định |
|---|---|---|---|
| 19 module CRM còn lại: `ITEM` · `TASK` · `INV` · `PAY` · `EST` · `PROP` · `CRN` · `CTR` · `EXP` · `LEAD` · `TKT` · `SUB` · `ESTREQ` · `KB` · `DASH` · `PROFILE` · `RPT` · `UTIL` · `SETUP` | Không thuộc Release 1.0. Riêng `SETUP` còn đang ⏸️ BLOCKED vì tài khoản không có quyền admin (AMB-01) | Đợt sau | Phiếu — Anh Tester (QA Lead), 17-09-2026 |
| Hệ thống F2C (namespace `_f2c/` — `ORDADM` · `ORDSEL` · `ORDBUY`) | Không thuộc Release 1.0 | Đợt sau | Phiếu — Anh Tester (QA Lead), 17-09-2026 |
| Cổng khách hàng (khu front-end ngoài `/admin`), kể cả đăng nhập phía client | Loại khỏi phạm vi Release 1.0 | Chưa xếp đợt — chờ PO chốt phạm vi cổng khách hàng | Phiếu — Anh Tester (QA Lead), 17-09-2026 · trùng mục 1 của `requirements_login.md` |
| Nền tảng mobile và API của `LOGIN` · `CUST` · `PRJ` | Đợt này chỉ kiểm web; hệ thống chưa khảo sát mặt mobile/API | Chưa xếp đợt | Phiếu — `Cách chạy mobile` · `Cách chạy API`: ngoài phạm vi |
| Kiểm thử hiệu năng | Phiếu ghi `không` | ❓ (ô treo 4) | Phiếu — `Loại kiểm thử` |
| Kiểm thử bảo mật chuyên sâu (pentest, quét lỗ hổng) | Phiếu ghi `không`. Các AC có yếu tố bảo mật của `LOGIN` (thông báo lỗi chung REQ-10, RISK-06 dò tài khoản qua Forgot Password) **vẫn** kiểm ở mức chức năng | ❓ (ô treo 4) | Phiếu — `Loại kiểm thử` |
| Giao diện `LOGIN` ở viewport mobile, lối Logout trong `#mobile-collapse` | Chưa khảo sát viewport mobile | Đợt recon riêng | PO, 18-09-2026 — AMB-16 ⏭️ |
| Two Factor Authentication · đổi mật khẩu khi đã đăng nhập · chọn ngôn ngữ ở menu hồ sơ | Thuộc module `PROFILE` (ngoài phạm vi đợt) | Đợt có `PROFILE` | Ranh giới module ở `requirements_login.md` mục 1 |
| Cấu hình bảo mật trong Setup | `SETUP` BLOCKED (AMB-01) | Chủ môi trường cấp tài khoản admin | `requirements_login.md` mục 1 · `system_map.md` mục 6 |
| Điều hướng về đúng route sau khi đăng nhập | Chưa sinh REQ ở đợt này | Kiểm lại khi có tài khoản riêng | PO, 18-09-2026 — AMB-18 ⏭️ |

> Mục này đã được thống nhất với Anh Tester (QA Lead) ngày 17-09-2026 theo phiếu, chờ PO xác nhận khi ký mục 11. Thay đổi phạm vi phải cập nhật tài liệu, tăng phiên bản và thông báo lại.
>
> Chưa có bảng ISO/IEC 25010 nào (chưa module nào có TC) → không có ô `➖` để đưa vào mục này. Khi sinh TC xong, ô `➖` của 3 module phải được thêm vào đây ở phiên bản sau.

### 2.3 Giả định & Ràng buộc

| Loại | Nội dung | Ảnh hưởng tới kiểm thử | Nguồn |
|---|---|---|---|
| Ràng buộc | Đợt này chạy trên **môi trường test riêng** (không dùng chung), khác môi trường demo **dùng chung** đã dùng khi khảo sát | Requirements `LOGIN` và bản đồ khám phá viết theo môi trường cũ: cấu hình (tên công ty trong tiêu đề trang, dữ liệu mẫu, timer đang chạy) có thể khác → rủi ro R5 | Phiếu `Môi trường` · `docs/requirements/README.md` |
| Ràng buộc | Tài khoản khảo sát duy nhất **không có quyền admin** | Nếu môi trường mới vẫn vậy: Customer Groups của `CUST`, mọi field phụ thuộc Setup, Activity Log đều không kiểm được | AMB-01 · `system_map.md` mục 5 |
| Ràng buộc | AC của `LOGIN` dựa trên Google Chrome 152, `en-US`, viewport 1600×750 | Firefox (trình duyệt phụ) có thông báo validation khác — TC phải assert `checkValidity()` thay vì câu chữ tooltip | `requirements_login.md` · RISK-04 |
| Giả định | Không assert mã trạng thái HTTP — chỉ assert URL cuối, nội dung hiển thị, việc có/không phát sinh request | Áp cho mọi TC `LOGIN` | PO, 18-09-2026 — AMB-08 ✅ · AMB-09 ✅ |
| Giả định | Ước lượng không tính công sức PO/BA làm UAT và thời gian Dev sửa bug | Mục 7.2 | Phiếu `Ước lượng` → `Giả định` |
| Giả định | `CUST` và `PRJ` phải recon và viết requirements trước khi viết TC | Kéo dài giai đoạn chuẩn bị (22-09 → 02-10-2026) | Phiếu · `docs/requirements/README.md` |
| Ràng buộc | Năng lực của QA: gọi API · truy vấn CSDL · kiểm tầng tích hợp ❔ chưa chốt · nhật ký hoạt động ❌ (tài khoản bị chặn) · DevTools ✅ | Nhánh Vòng 3 (kiểm kỹ thuật) của bộ TC chưa xác định được — ô treo 18 | `docs/requirements/README.md` |
| Ràng buộc | Không có ngân sách riêng cho kiểm thử | Mục 7.3 | Phiếu `Ngân sách` |
| Ràng buộc | Tổ chức chưa có Test Policy và Test Strategy | Mục 12.2 | Phiếu `Chuẩn tổ chức` |

### 2.4 Các bên liên quan & Giao tiếp

| Bên | Vai trò trong đợt | Liên quan tới kiểm thử | Nhận gì | Tần suất | Kênh |
|---|---|---|---|---|---|
| Anh Tester | QA Lead — lập và duyệt plan · tự động hoá | Chịu trách nhiệm toàn bộ đợt kiểm thử | Kế hoạch · báo cáo tiến độ · báo cáo tổng hợp | Hằng tuần thứ Sáu · cuối đợt | Jira · repo |
| ❓ (chưa có tên — ô treo 13) | Product Owner / BA — duyệt plan · thực hiện UAT | Chốt yêu cầu, trả lời AMB, nghiệm thu | Kế hoạch · báo cáo tiến độ · báo cáo tổng hợp | Hằng tuần thứ Sáu · cuối đợt | Email · Jira |
| Đội DEV | Sửa bug · dựng và duy trì môi trường test riêng | Cấp build, môi trường, tài khoản | Báo cáo lỗi | Khi phát sinh | Jira |
| Hồng · Lan · Huệ | Kiểm thử viên | Viết TC, thực thi, báo lỗi theo module phụ trách (mục 6) | — (người lập báo cáo) | — | Jira · repo |

**Mẫu tài liệu dùng trong đợt** (phiếu: `Dùng mẫu có sẵn của repo: có`):

| Tài liệu | Mẫu | Workflow sinh |
|---|---|---|
| Requirements | Mẫu của `skills-requirements-analyzer` | `/generate-requirements-from-website` |
| Test case | Mẫu của `skills-rbt-manual-testing` | `/generate-testcases-manual-rbt` |
| Execution report | Mẫu của `skills-manual-test-executor` | `/execute-test-cases` |
| Bug report | Mẫu của `skills-bug-reporter` | `/create-bug-report` |
| Báo cáo tiến độ | Mẫu của `skills-test-progress-reporter` | `/generate-test-progress-report` |
| Báo cáo tổng hợp | Mẫu của `skills-test-summary-reporter` | `/generate-test-summary-report` |

## 3. Chiến lược kiểm thử (Test approach)

### 3.1 Cấp độ kiểm thử

| Cấp độ | Trong đợt? | Ai thực hiện | Tiêu chí vào/ra |
|---|---|---|---|
| Component (unit) | ❌ ngoài phạm vi QA | Đội DEV | Theo quy trình DEV |
| Component integration | ❌ ngoài phạm vi QA | Đội DEV | Theo quy trình DEV |
| System | ✅ | QA | Bộ chung mục 4 |
| System integration | ✅ | QA | Bộ chung mục 4 |
| Acceptance (UAT) | ✅ | PO/BA nội bộ, QA hỗ trợ | Bộ chung mục 4 |

### 3.2 Loại kiểm thử

| Loại test | Nền tảng | Có làm? | Cách làm | Ghi chú |
|---|---|---|---|---|
| Kiểm thử chức năng | Web | ✅ | Manual theo TC — `/execute-test-cases` | Cả 3 module |
| Kiểm thử chức năng | Mobile | ❌ | — | Ngoài phạm vi (2.2) |
| Kiểm thử chức năng | API | ❌ | — | Ngoài phạm vi (2.2) |
| Regression | Web | ✅ | Bộ regression tự động (3.7) + chạy tay phần chưa tự động | 20-11 → 25-11-2026 |
| Retest bug | Web | ✅ | `/retest-fixed-bugs` | Critical/Major chạy mode FULL |
| Tích hợp liên module | Web | ✅ | `/generate-cross-module-test-plan` | `LOGIN` là cổng vào của mọi module · `CUST` → `PRJ` (dự án gắn khách hàng) |
| Tự động hoá | Web | ✅ | `/generate-automation-framework` → `/generate-automation-web` | Chi tiết 3.7 |
| Nghiệm thu (UAT) | Web | ✅ | PO/BA nội bộ, QA hỗ trợ | 30-11 → 04-12-2026 |
| Vòng 3 — kỹ thuật | Web | Theo *Năng lực kiểm thử của QA* | Nhánh ❌ → đội DEV xác minh | Năng lực gọi API/CSDL/tích hợp đang ❔ — ô treo 18. Không phải vùng trắng |
| Hiệu năng · Bảo mật chuyên sâu | — | ❌ | — | Ngoài phạm vi (2.2) |

**Tỷ trọng manual/automation:** chạy manual toàn bộ TC trên web · tự động hoá bộ Smoke và regression của `LOGIN`, `CUST`, `PRJ` bằng Playwright (theo phiếu) — chi tiết ở 3.7.

**Thứ tự ưu tiên thực thi:** `LOGIN` trước (cổng vào của mọi module) → `CUST` (module được phụ thuộc nhiều nhất, ≥ 12 tab liên kết) → `PRJ` (phụ thuộc `CUST`). Thứ tự này khớp thứ tự khảo sát đã chốt ở `system_map.md` mục 6.

#### 3.2.1 Kiểm thử phi chức năng

| Loại | Có làm? | Mục tiêu đo | Ngưỡng chấp nhận | Cách làm · công cụ | Môi trường | Ai thực hiện | TC đã có |
|---|---|---|---|---|---|---|---|
| Hiệu năng | ❌ → 2.2 | — | — | — | — | — | 0 |
| Bảo mật | ❌ chuyên sâu → 2.2 (AC bảo mật của `LOGIN` kiểm ở mức chức năng) | — | — | — | — | — | 0 |
| Tương thích | ❓ ô treo 5 | ❓ | ❓ | ❓ | ❓ | ❓ | 0 |
| Khả năng truy cập | ❓ ô treo 5 | ❓ | ❓ | ❓ | ❓ | ❓ | 0 |
| Khả dụng | ❓ ô treo 5 | ❓ | ❓ | ❓ | ❓ | ❓ | 0 |
| Độ tin cậy & phục hồi | ❓ ô treo 5 | ❓ | ❓ | ❓ | ❓ | ❓ | 0 |

> Phiếu khai Firefox là trình duyệt phụ (5.1) nhưng ô `Tương thích` để trống — cần QA Lead chốt Firefox được kiểm ở mức nào (toàn bộ TC hay chỉ Smoke) và ghi `có` kèm ngưỡng.

### 3.3 Kỹ thuật thiết kế test

Chưa module nào trong phạm vi có TC → **xác định khi sinh TC** bằng `/generate-testcases-manual-rbt`. Plan phiên bản sau cập nhật mục này từ tài liệu test case.

### 3.4 Mức độc lập của kiểm thử

| | |
|---|---|
| Mức độ | Đội QA riêng trong tổ chức |
| Thể hiện ở đâu | ❓ ô treo 6 (VD: QA không báo cáo cho trưởng nhóm DEV · kiểm thử viên review TC chéo module) |
| Giới hạn | UAT do PO/BA **nội bộ** thực hiện, không phải bên ngoài tổ chức. Anh Tester vừa là QA Lead, người làm tự động hoá và người duyệt plan — không có người review độc lập cho phần tự động hoá |

### 3.5 Retest & Regression

- Bug đã fix → `/retest-fixed-bugs`: Critical/Major chạy **mode FULL**, Minor/Trivial chạy mode RETEST
- Mỗi build mới lên môi trường test → chạy bộ Smoke trước khi thực thi tiếp
- Regression trước release (20-11 → 25-11-2026) → bộ regression tự động của 3 module (3.7) + chạy tay phần không tự động

### 3.6 Chỉ số theo dõi

> Nhóm theo ISTQB CTFL v4.0 mục 5.3.1. `/generate-test-progress-report` báo cáo **đúng các chỉ số này** mỗi kỳ.

| Nhóm | Chỉ số | Nguồn | Dùng để |
|---|---|---|---|
| Tiến độ kiểm thử | REQ đã viết cho `CUST`/`PRJ` · TC đã viết / đã review · TC đã chạy / chưa chạy · PASS · FAIL · BLOCKED | `docs/requirements/` · `docs/testcases/` · `execution_report.md` | Báo cáo tiến độ · tiêu chí exit #3, #4, #5, #7 |
| Tiến độ dự án | Công sức thực tế so với ước lượng 7.2 | Báo cáo tiến độ | Phát hiện trễ sớm |
| Lỗi | Bug mới / đã fix / đang mở theo Severity · regression phát sinh | `docs/bugs/` · Jira | Tiêu chí exit #1, #2 |
| Độ phủ | REQ có TC · REQ Critical có TC PASS | `traceability_matrix.md` (chưa có — sinh bằng `/generate-traceability-matrix`) | Tiêu chí exit #6 |
| Rủi ro | Trạng thái từng rủi ro ở 8.1 | Báo cáo tiến độ | Kiểm soát rủi ro |

### 3.7 Chiến lược tự động hoá

| | |
|---|---|
| Mục tiêu | ❓ ô treo 7 |
| Hiện trạng | **Chưa có gì** — repo chưa có project automation (không có `package.json` / `pom.xml` / `pyproject.toml`), chưa có file CI (`.github/workflows/` không tồn tại), 0 script. Phải dựng framework từ đầu |
| Tầng kiểm thử (kim tự tháp) | ❓ ô treo 7 — ISTQB CTFL v4.0 mục 5.1.6: càng lên tầng UI, test càng ít, chậm và dễ vỡ. Đợt này API ngoài phạm vi → gần như toàn bộ ở tầng UI |
| Tiêu chí chọn TC để tự động | ❓ ô treo 7 |
| Framework · report | Playwright + TypeScript · Allure report · output trong `reports/` |
| Hệ thống CI | GitHub Actions |
| Người bảo trì | ❓ ô treo 7 — phiếu `Nhân lực` phân Anh Tester làm tự động hoá cho cả 3 module, chờ xác nhận là người bảo trì |

**Phạm vi:**

| Tự động | Không tự động | Lý do không tự động |
|---|---|---|
| Bộ Smoke của `LOGIN` · `CUST` · `PRJ` × web (theo phiếu `Tỷ trọng thủ công / tự động`) | ❓ | ❓ ô treo 7 |
| Bộ regression của `LOGIN` · `CUST` · `PRJ` × web (theo phiếu) | Gợi ý cần xác nhận: REQ-LOGIN-29/30 (cần hộp thư test) · REQ-LOGIN-10 (chỉ chạy tối đa 1 lần/lượt, không song song — RISK-01) | Gợi ý của agent từ tài liệu `LOGIN`, chưa phải quyết định |

**Kích hoạt chạy:** ❓ ô treo 7 — phiếu chưa khai bộ chạy nào.

| Bộ chạy | Khi nào | Môi trường | Ai xem kết quả | Fail thì |
|---|---|---|---|---|
| Smoke | ❓ | Môi trường test riêng Release 1.0 | ❓ | Chặn thực thi manual — tiêu chí tạm dừng 4.3 |
| Regression | ❓ — phải chạy **trước** 25-11-2026 (hết hồi quy) | Môi trường test riêng Release 1.0 | ❓ | Phân loại bằng `/run-and-fix-tests` — **không** sửa test để né bug |

**Nguyên tắc:**
- Script chỉ tính là xong khi đạt Definition of Done của `CLAUDE.md` — PASS ổn định ≥ 2 lần liên tiếp, đủ Allure metadata và screenshot
- Kết quả automation **báo riêng**, không cộng vào pass rate manual của tiêu chí exit #3, #4
- Test chập chờn → `/analyze-flaky-tests`, **không** chạy lại tới khi xanh · UI đổi → `/heal-locators` · yêu cầu đổi → `/update-automation-from-impact`

## 4. Tiêu chí Vào / Ra

### 4.1 Tiêu chí VÀO (Entry) — chưa đủ thì CHƯA bắt đầu test

> Nhóm theo ISTQB CTFL v4.0 mục 5.1.3. Trạng thái tại ngày lập plan **18-09-2026**.

| # | Nhóm | Điều kiện | Trạng thái |
|---|---|---|---|
| 1 | Nguồn lực | Nhân lực ở mục 6 đã được phân công, đủ người cho mọi cặp module × nền tảng | ✅ Đạt — Hồng `LOGIN`, Lan `CUST`, Huệ `PRJ` |
| 2 | Nguồn lực | Môi trường test sẵn sàng, có dữ liệu nền | ❓ Dự kiến 05-10-2026 (Đội DEV) · dữ liệu nền chưa chốt (ô treo 16) |
| 3 | Nguồn lực | Tài khoản test đủ mọi vai trò trong phạm vi | ❌ Chưa đạt — hiện chỉ có 1 tài khoản không có quyền admin; thiếu tài khoản admin (AMB-01), tài khoản các role khác (AMB-02), tài khoản riêng cho REQ-LOGIN-19/20/36/37 và hộp thư test cho REQ-LOGIN-29/30 (ô treo 14, 17) |
| 4 | Nguồn lực | Công cụ sẵn sàng: quản lý bug · quản lý kết quả · automation | ❌ Chưa đạt — Jira: ❓ chưa xác nhận đã có project · automation: chưa có framework, chưa có CI |
| 5 | Nguồn lực | Ngân sách đã duyệt | Không áp dụng — không có ngân sách riêng |
| 6 | Testware | Tài liệu requirements của mọi module × nền tảng trong phạm vi đã có | ❌ Chưa đạt — `LOGIN` ✅ · `CUST` ❌ · `PRJ` ❌ |
| 7 | Testware | AMB 🔴 đã được giải đáp hoặc người duyệt chấp nhận treo | ❌ Chưa đạt — AMB-01, AMB-02 🔴 cấp hệ thống còn treo (ảnh hưởng `CUST`). `LOGIN` không còn AMB 🔴 |
| 8 | Testware | Test case đã viết và đã review — đủ từng nền tảng | ❌ Chưa đạt — 0 TC · dự kiến 02-10-2026 |
| 9 | Chất lượng ban đầu | Build `v1.0.0` đã deploy và truy cập được | ❓ Dự kiến 05-10-2026 |
| 10 | Chất lượng ban đầu | Smoke test đã pass | ❓ Chạy sau khi đạt #9 |

> ⚠️ Bắt đầu test khi chưa đạt tiêu chí vào là nguyên nhân số một khiến kết quả kiểm thử không dùng được — BLOCKED tràn lan, phải chạy lại từ đầu.

### 4.2 Tiêu chí RA (Exit)

> Bảng mặc định lấy **nguyên văn** từ `skills-test-summary-reporter`. `/generate-test-summary-report` chấm lại **cả bảng mặc định lẫn bảng bổ sung**.

| # | Tiêu chí | Ngưỡng |
|---|---|---|
| 1 | Bug **Critical** đang mở | **0** |
| 2 | Bug **Major** đang mở | 0, hoặc có workaround được PM chấp nhận bằng văn bản |
| 3 | Pass rate TC **Priority High** | **≥ 95%** |
| 4 | Pass rate toàn bộ TC đã chạy | ≥ 90% |
| 5 | Tỷ lệ **BLOCKED** | ≤ 5% |
| 6 | REQ mức Critical có ít nhất 1 TC **PASS** | 100% |
| 7 | Module trong phạm vi release đã có TC và đã chạy — tính trên **từng cặp module × nền tảng** trong phạm vi | 100% |

**Tiêu chí bổ sung của dự án:** không có — phiếu `Tiêu chí ra bổ sung` trống, `Bộ tiêu chí ra: mặc định`.

☑ Bộ mặc định  ☐ Bộ mặc định + bổ sung  ☐ Bộ tiêu chí riêng của dự án

> ⚠️ Tiêu chí #6 cần mỗi REQ có **mức độ quan trọng**. Tài liệu `LOGIN` hiện chưa gán mức Critical cho REQ nào → phải gán khi sinh TC theo RBT, nếu không tiêu chí #6 không chấm được (rủi ro R11).

> ⚠️ **Dừng kiểm thử khi hết thời gian hoặc ngân sách** (ISTQB CTFL v4.0 mục 5.1.3): được coi là hợp lệ **chỉ khi** Product Owner cùng Anh Tester (QA Lead) đã xem xét và **chấp nhận bằng văn bản** rủi ro phát hành mà chưa đạt đủ tiêu chí. Báo cáo tổng hợp khi đó ghi rõ tiêu chí nào chưa đạt và ai chấp nhận — **không** chấm lại thành "Đạt".

### 4.3 Tiêu chí TẠM DỪNG (Suspension) & tiếp tục

**Tạm dừng kiểm thử khi:** môi trường sập > 4 giờ · build lỗi không đăng nhập được · > 30% TC BLOCKED cùng một nguyên nhân · phát hiện bug Critical chặn luồng chính.

**Tiếp tục khi:** nguyên nhân đã xử lý, có build mới, và đã chạy lại smoke.

> Ngưỡng trên là đề xuất của agent — **đã xác nhận** (phiếu `Dùng ngưỡng tạm dừng đề xuất: có`).

## 5. Môi trường, Dữ liệu & Công cụ

### 5.1 Môi trường kiểm thử

| | |
|---|---|
| Môi trường | Môi trường test riêng cho Release 1.0 — URL lưu ở `.env`, **không** ghi vào tài liệu này |
| Dùng chung với đội khác? | **Không** — gỡ được các giới hạn của môi trường dùng chung (TC phá huỷ, gửi email, thử sai mật khẩu) nếu có tài khoản và hộp thư test riêng |
| Khác môi trường đã khảo sát? | **Có** — khảo sát 14-09-2026 làm trên môi trường demo dùng chung. Rủi ro lệch tài liệu ở R5 |
| Web — trình duyệt | Google Chrome (chính) · Firefox. Requirements `LOGIN` khảo sát trên Chrome 152, `en-US`, viewport 1600×750 |
| Người dựng · ngày sẵn sàng | Đội DEV · 05-10-2026 |

### 5.2 Quản lý dữ liệu kiểm thử

| | |
|---|---|
| Dữ liệu nền | ❓ ô treo 16 |
| Nguồn dữ liệu | ❓ ô treo 16 |
| Tài khoản test | Hiện có 1 tài khoản staff không admin. Cần thêm: admin · các role khác · tài khoản riêng cho TC phá huỷ (ô treo 14, 17). Mật khẩu ở `.env` |
| Dữ liệu thật của khách hàng | ❓ ô treo 16 |
| Quy tắc sinh dữ liệu | Random + traceable theo `CLAUDE.md` mục 7 — nhìn bản ghi biết test nào tạo |
| Dọn dữ liệu sau khi chạy | ❓ ô treo 16 |
| Làm mới dữ liệu nền | ❓ ô treo 16 |
| Người cung cấp | ❓ ô treo 16 |

> 🔒 Nếu dữ liệu nền là bản sao production, dữ liệu khách hàng thật sẽ lọt vào evidence (ảnh chụp, bug report). `CUST` là module chứa email/SĐT khách hàng — bản đồ khám phá đã phải cắt ảnh vì lý do này.

### 5.3 Công cụ

| Mục đích | Công cụ | Ghi chú |
|---|---|---|
| Quản lý lỗi | Jira · file markdown trong repo (`docs/bugs/`) | **Nguồn chính khi lệch:** Jira cho trạng thái bug |
| Quản lý kết quả kiểm thử | Jira · file markdown trong repo (`docs/executions/`) | **Nguồn chính khi lệch:** repo cho execution report |
| Tự động hoá | Playwright + TypeScript · Allure report | Chi tiết ở 3.7 |
| CI | GitHub Actions | Chưa có file workflow |
| Khác | ❓ ô treo 8 | |

## 6. Nhân lực & Phân công

| Vai trò | Người | Module × nền tảng phụ trách | Ghi chú |
|---|---|---|---|
| Trưởng nhóm QA | Anh Tester | Toàn bộ | Kiêm tự động hoá và duyệt plan |
| Kiểm thử viên | Hồng | `LOGIN` × web | |
| Kiểm thử viên | Lan | `CUST` × web | Recon + viết requirements `CUST` trước khi viết TC |
| Kiểm thử viên | Huệ | `PRJ` × web | Recon + viết requirements `PRJ` trước khi viết TC |
| Tự động hoá | Anh Tester | `LOGIN` × web · `CUST` × web · `PRJ` × web | Dựng framework từ đầu |

**Nhu cầu đào tạo:** ❓ ô treo 9 · **Nhu cầu tuyển thêm:** không.

## 7. Lịch trình, Ước lượng & Ngân sách

### 7.1 Lịch trình & Mốc

| Mốc | Ngày | Điều kiện hoàn thành |
|---|---|---|
| Duyệt plan | 21-09-2026 (thứ Hai) | Mục 11 có chữ ký |
| Hoàn tất viết & review TC | 02-10-2026 (thứ Sáu) | Requirements `CUST`, `PRJ` đã có · TC 3 module đã review |
| Môi trường sẵn sàng | 05-10-2026 (thứ Hai) | Tiêu chí vào #2, #3 |
| Bắt đầu thực thi | 06-10-2026 (thứ Ba) | Đạt toàn bộ tiêu chí vào 4.1 |
| Báo cáo tiến độ | Hằng tuần, thứ Sáu — kỳ đầu 09-10-2026 | `/generate-test-progress-report` — slug `release_1.0` |
| Code freeze | 19-11-2026 (thứ Năm) | |
| Regression | 20-11 → 25-11-2026 (thứ Sáu → thứ Tư) | 4 ngày làm việc |
| UAT | 30-11 → 04-12-2026 (thứ Hai → thứ Sáu) | 5 ngày làm việc |
| Báo cáo tổng hợp | 10-12-2026 (thứ Năm) | `/generate-test-summary-report` — slug `release_1.0` |
| Release | 15-12-2026 (thứ Ba) | |

> Không mốc nào rơi vào cuối tuần. Giai đoạn chuẩn bị từ duyệt plan tới hoàn tất TC chỉ có **9 ngày làm việc** (22-09 → 02-10-2026) nhưng phải gồm cả recon `CUST`, `PRJ` — xem R1.

### 7.2 Ước lượng công sức

| | |
|---|---|
| Kỹ thuật (ISTQB CTFL v4.0 mục 5.1.4) | Three-point estimation |
| Giả định của ước lượng | `LOGIN` đã có requirements (37 REQ) nhưng chưa có TC · `CUST` và `PRJ` chưa khảo sát — phải recon và viết requirements trước khi viết TC · không tính công sức PO/BA làm UAT · không tính thời gian DEV sửa bug |

Công thức: E = (a + 4m + b) / 6 · SD = (b − a) / 6. E tổng = cộng E các hạng mục. SD tổng = **cộng SD** các hạng mục (cách cộng thận trọng, cho khoảng rộng hơn cách lấy căn tổng bình phương). Đơn vị người-ngày.

| Hạng mục | a (lạc quan) | m (khả năng nhất) | b (bi quan) | E = (a+4m+b)/6 | SD = (b−a)/6 |
|---|---|---|---|---|---|
| Viết & review TC cho `LOGIN` · `CUST` · `PRJ` × web | 7 | 8 | 9 | 8.0 | 0.3 |
| Thực thi manual trên Web | 5 | 6 | 7 | 6.0 | 0.3 |
| Retest bug và regression | 2 | 3 | 4 | 3.0 | 0.3 |
| Hỗ trợ UAT, lập báo cáo và quản lý đợt | 1 | 2 | 3 | 2.0 | 0.3 |
| **Tổng** | | | | **19.0 người-ngày** | **±1.3** |

**Đối chiếu năng lực:**
- Giai đoạn thực thi (06-10 → 19-11-2026): 3 kiểm thử viên × 33 ngày làm việc = **99 người-ngày**, chưa tính QA Lead → **dư nhiều** so với 11.0 người-ngày ước cho thực thi + retest/regression.
- Giai đoạn viết TC (22-09 → 02-10-2026): 3 kiểm thử viên × 9 ngày làm việc = **27 người-ngày** so với 8.0 ước cho viết TC → đủ **nếu** không tính recon.

> ⚠️ Năng lực dư xa so với ước lượng thường là dấu hiệu **ước lượng thiếu hạng mục**, không phải thừa người. Bảng trên **không có** hạng mục: recon + viết requirements `CUST`, `PRJ` (bản đồ ước ~85 REQ) · dựng framework automation + CI + viết script Smoke/regression. Agent **không** tự thêm số — xem R2.

### 7.3 Ngân sách

Không có ngân sách riêng — chi phí nằm trong ngân sách dự án.

## 8. Rủi ro

### 8.1 Rủi ro DỰ ÁN & biện pháp

> Nhóm theo ISTQB CTFL v4.0 mục 5.2.2. Khả năng / Ảnh hưởng là **đề xuất của agent** — người duyệt xác nhận. `/generate-test-progress-report` theo dõi trạng thái từng dòng.

| # | Nhóm | Rủi ro | Khả năng | Ảnh hưởng | Biện pháp | Nguồn phát hiện |
|---|---|---|---|---|---|---|
| R1 | Tổ chức | `CUST` và `PRJ` chưa có requirements, trong khi hạn hoàn tất TC là 02-10-2026 (9 ngày làm việc sau duyệt plan) | Cao | Cao | Lan và Huệ chạy `/generate-requirements-from-website` cho `CUST`, `PRJ` ngay từ 22-09-2026. Báo cáo tiến độ kỳ đầu theo dõi số REQ đã viết. Trễ → dời hạn viết TC hoặc thu hẹp phạm vi, có văn bản | `docs/requirements/README.md` |
| R2 | Tổ chức | Ước lượng thiếu hạng mục recon requirements và tự động hoá — tổng 19.0 người-ngày thấp bất thường so với phạm vi | Cao | Trung bình | QA Lead bổ sung hạng mục vào phiếu `Chi tiết ba điểm`, tăng phiên bản plan | Bước 3 — đối chiếu năng lực |
| R3 | Nhà cung cấp | Chỉ có 1 tài khoản staff không admin (AMB-01, AMB-02): chặn Customer Groups của `CUST`, field phụ thuộc Setup, REQ-LOGIN-19/20/36/37 | Cao | Cao | Yêu cầu Đội DEV cấp tài khoản admin + tài khoản riêng trên môi trường mới **trước 05-10-2026**. Không có → phần bị chặn ghi BLOCKED, tiêu chí exit #5 có thể không đạt | AMB-01 · AMB-02 · `system_map.md` mục 5 |
| R4 | Nhà cung cấp | Chưa có hộp thư test → REQ-LOGIN-29/30 phải `skip`, không xác nhận được bug tiềm ẩn RISK-06 (dò tài khoản qua Forgot Password) | Trung bình | Trung bình | Xin hộp thư test cùng lúc với tài khoản riêng | AMB-12 · RISK-06 |
| R5 | Kỹ thuật | Môi trường test riêng khác môi trường demo đã khảo sát → AC lệch (tiêu đề trang, dữ liệu, cấu hình) | Trung bình | Trung bình | Chạy Smoke ngay khi có môi trường, đối chiếu AC `LOGIN`. Lệch → cập nhật bằng `/update-requirements-from-ticket` trước khi thực thi | Phiếu `Môi trường` · `docs/requirements/README.md` |
| R6 | Con người | Chưa có framework automation lẫn CI; Anh Tester kiêm QA Lead + tự động hoá + duyệt plan → bộ regression tự động có thể không kịp trước 20-11-2026 | Cao | Trung bình | Chốt 3.7 (ô treo 7). Ưu tiên bộ Smoke trước. Không kịp → regression chạy tay, ghi lệch mục tiêu O4 | Repo — không có `package.json` / `.github/workflows/` |
| R7 | Kỹ thuật | AC `LOGIN` khảo sát trên Chrome, còn Firefox là trình duyệt phụ — thông báo validation khác nhau | Trung bình | Thấp | TC assert `checkValidity()` thay vì câu chữ (RISK-04). Chốt ô `Tương thích` | `requirements_login.md` · RISK-04 |
| R8 | Tổ chức | Dữ liệu kiểm thử chưa chốt nguồn, chưa rõ có dữ liệu thật của khách hàng không | Trung bình | Trung bình | Đội DEV trả lời ô treo 16 trước 05-10-2026 | Phiếu `Dữ liệu kiểm thử` |
| R9 | Tổ chức | Chưa có người phân loại lỗi và thời hạn xử lý → bug tồn đọng không ai chốt Priority | Trung bình | Trung bình | QA Lead và Dev Lead chốt mục 9.4 trước 06-10-2026 | Phiếu `Quản lý lỗi` |
| R10 | Kỹ thuật | Năng lực QA gọi API / truy vấn CSDL / kiểm tầng tích hợp chưa chốt → nhánh Vòng 3 treo | Thấp | Trung bình | Hỏi Đội DEV khi bàn giao môi trường; ❌ thì chuyển DEV xác minh | `docs/requirements/README.md` |
| R11 | Tổ chức | REQ chưa được gán mức Critical → tiêu chí exit #6 không chấm được | Trung bình | Cao | Gán mức khi sinh TC bằng `/generate-testcases-manual-rbt` | Mục 4.2 |

### 8.2 Rủi ro SẢN PHẨM — tóm tắt

> **Nguồn chính** vẫn là tài liệu requirements (`RISK-xx`) và tài liệu test case (đánh giá RBT) của từng module. Sửa rủi ro ở tài liệu nguồn, **không** sửa ở đây.

| Module | Rủi ro | Mức | Kiểm soát bằng | Nguồn |
|---|---|---|---|---|
| `LOGIN` | RISK-06 — dò tài khoản qua Forgot Password: trả "Email not found" với email không tồn tại, trong khi form Login cố ý giấu thông tin | Cao (lộ thông tin) | Có hộp thư test → so thông báo với REQ-27, khác nhau thì lập bug · TC REQ-27 gắn `known-issue` | [requirements_login.md](../requirements/login/requirements_login.md) |
| `LOGIN` | RISK-02 — timer công việc làm luồng Logout rẽ nhánh | — | TC kiểm tiền điều kiện rồi đi đúng nhánh REQ-33/34 hoặc REQ-35 · REQ-37 chỉ chạy trên tài khoản riêng | [requirements_login.md](../requirements/login/requirements_login.md) |
| `LOGIN` | RISK-03 — trình duyệt tự điền làm sai kết quả | — | Chạy profile sạch · assert thuộc tính `value` trong HTML | [requirements_login.md](../requirements/login/requirements_login.md) |
| `CUST` | Chưa có tài liệu requirements. Bản đồ khám phá: risk 🔴, module được phụ thuộc nhiều nhất (≥ 12 tab liên kết), chi tiết 19 tab | 🔴 (bản đồ khám phá) | Bổ sung khi có requirements | [module_02](../requirements/_discovery/modules/module_02_khach_hang_lien_he.md) |
| `PRJ` | Chưa có tài liệu requirements. Bản đồ khám phá: risk 🔴, chi tiết 12 tab (Task · Milestone · Discussion · Timesheet · Invoice Project) | 🔴 (bản đồ khám phá) | Bổ sung khi có requirements | [module_04](../requirements/_discovery/modules/module_04_du_an.md) |

> Tài liệu `LOGIN` không ghi mức cho từng `RISK-xx` → cột Mức để `—`, chỉ RISK-06 có mức "severity cao" ghi trong biện pháp.

## 9. Quản lý lỗi

> Nội dung theo ISTQB CTFL v4.0 mục 5.5. Mục này là **phần mở rộng** so với khung 29119-3 — xem 12.1.
>
> ⚠️ Phiếu để trống `Quy trình trạng thái`, `Thang Severity`, `Thang Priority` → nội dung 9.1–9.3 dưới đây là **mặc định, chờ QA Lead + Dev Lead xác nhận** (ô treo 10).

### 9.1 Quy trình trạng thái lỗi

```text
TC FAIL ──/create-bug-report──→ 🔴 Đang mở ──Dev sửa──→ 🟡 Đã fix — chờ retest
                                    ▲                           │
                                    │                   /retest-fixed-bugs
                                    │                           │
                     NOT_FIXED ─────┤           ┌───────────────┼────────────────┐
                     PARTIAL   ─────┘         FIXED                      CANNOT_VERIFY
                                                │                   (giữ trạng thái, ghi lý do)
                                                ▼
                                            ⬛ Đóng
```

| Trạng thái | Ai chuyển | Điều kiện |
|---|---|---|
| 🔴 Đang mở | Tester | Bug report đủ Build/Version · TC ID · REQ ID · evidence |
| 🟡 Đã fix — chờ retest | Dev | Có build chứa bản sửa |
| ⬛ Đóng | Tester | Retest `FIXED` — lặp ≥ 2 lần theo Steps gốc |
| 🔴 Mở lại | Tester | Retest `NOT_FIXED` hoặc `PARTIAL` — **không** tạo bug trùng |

> Jira là nguồn chính cho trạng thái bug (5.3). Workflow Jira có thêm trạng thái như *Từ chối* · *Trùng* · *Hoãn* → khai `Quy trình trạng thái: riêng` trong phiếu. Bug *Hoãn* vẫn tính là **đang mở** khi chấm tiêu chí exit #1, #2 — trừ khi người có quyền ở 4.2 chấp nhận bằng văn bản.

### 9.2 Thang Severity

> Mặc định chép **nguyên văn** `skills-bug-reporter` — *Severity & Priority Guide*. Tiêu chí exit #1, #2 đếm theo thang này.

| Severity | Định nghĩa | Ví dụ |
|---|---|---|
| 🔴 **Critical** | Chặn luồng chính, mất data, crash, security | Không login được, thanh toán sai tiền |
| 🟠 **Major** | Chức năng chính sai nhưng có workaround | Filter sai kết quả, export thiếu cột |
| 🟡 **Minor** | Chức năng phụ sai, UI lệch ảnh hưởng sử dụng | Validation message sai, sort không đúng |
| 🟢 **Trivial** | Lỗi hiển thị nhỏ, không ảnh hưởng chức năng | Sai chính tả, lệch margin |

### 9.3 Thang Priority

| Priority | Định nghĩa |
|---|---|
| **P1** | Fix ngay trong sprint hiện tại / hotfix |
| **P2** | Fix trong sprint kế tiếp |
| **P3** | Fix khi có thời gian (backlog) |

> Severity đánh giá theo **mức ảnh hưởng kỹ thuật**; Priority theo **mức khẩn cấp business**. Hai giá trị độc lập nhau. Tester đề xuất Severity; **Priority do người phân loại lỗi chốt**.

### 9.4 Phân loại lỗi & thời hạn xử lý

| | |
|---|---|
| Người phân loại lỗi (triage) | ❓ ô treo 11 |
| Họp phân loại lỗi | ❓ ô treo 11 |
| Bug đang mở tại ngày lập | Critical 0 · Major 0 · Minor 0 · Trivial 0 — `docs/bugs/` chưa tồn tại, chưa có lần thực thi nào |

| Severity | Thời hạn phản hồi | Thời hạn sửa xong |
|---|---|---|
| Critical | ❓ | ❓ |
| Major | ❓ | ❓ |
| Minor | ❓ | ❓ |
| Trivial | ❓ | ❓ |

> Thời hạn **không có mặc định** (ô treo 12). Bug quá hạn là dữ liệu cho mục *trở ngại* của báo cáo tiến độ.

## 10. Sản phẩm bàn giao

| Sản phẩm | Nơi lưu | Workflow sinh ra |
|---|---|---|
| Master Test Plan + bản lưu phiếu | `docs/test-plans/test_plan_release_1.0.md` · `test_plan_release_1.0.input.yaml` | `/generate-master-test-plan` |
| Tài liệu requirements `CUST`, `PRJ` | `docs/requirements/<module>/` — tầng `web/` | `/generate-requirements-from-website` |
| Test cases | `docs/testcases/<module>/` — tầng `web/` | `/generate-testcases-manual-rbt` |
| Execution report | `docs/executions/<module>/web/run_*/` | `/execute-test-cases` |
| Retest report | `docs/executions/<module>/web/retest_*/` | `/retest-fixed-bugs` |
| Bug report | `docs/bugs/<module>/web/` | `/create-bug-report` |
| Automation script + report | Project automation · `reports/` | `/generate-automation-framework` · `/generate-automation-web` |
| Ma trận truy vết | `traceability_matrix.md` | `/generate-traceability-matrix` |
| **Báo cáo tiến độ** | `docs/executions/test_progress_release_1.0_<YYYYMMDD>.md` | `/generate-test-progress-report` |
| **Báo cáo tổng hợp** | `docs/executions/test_summary_release_1.0_*.md` | `/generate-test-summary-report` |

## 11. Phê duyệt

| Vai trò | Tên | Phiên bản duyệt | Ngày | Ý kiến |
|---|---|---|---|---|
| QA Lead | Anh Tester | | | |
| Product Owner | ❓ | | | |

## 12. Ánh xạ chuẩn tài liệu

### 12.1 Đối chiếu mục

> Tài liệu này biên soạn **theo cấu trúc** ISO/IEC/IEEE 29119-3 — Test Plan và phủ đủ nội dung điển hình của test plan theo **ISTQB CTFL v4.0 mục 5.1.1**. Cột IEEE 829 theo **khung Test Plan bản 1998**. Bảng dưới để người duyệt đối chiếu; **không** phải tuyên bố đã được đánh giá tuân thủ.

| Mục | ISO/IEC/IEEE 29119-3 — Test Plan | ISTQB CTFL v4.0 — 5.1.1 | IEEE 829-1998 — Test Plan |
|---|---|---|---|
| Kiểm soát tài liệu | Document-specific information — Unique identification · Issuing organization · Approval authority · Change history | — | Test plan identifier |
| 1.1 | Introduction — Scope · Context of the testing — Project/test sub-process | Context of testing — test objectives | Introduction |
| 1.2 | Context of the testing — Test item(s) | Context of testing — test basis | Introduction |
| 2.1 | Context of the testing — Test item(s) · Test scope | Context of testing — scope | Test items · Features to be tested |
| 2.2 | Context of the testing — Test scope (phần loại trừ) | Context of testing — scope | Features not to be tested |
| 2.3 | Context of the testing — Assumptions and constraints | Assumptions and constraints of the test project · Context of testing — constraints | — |
| 2.4 | Context of the testing — Stakeholders · Testing communication | Stakeholders — roles, relevance to testing · Communication — forms and frequency of communication, documentation templates | — |
| 3.1 | Test strategy — Test sub-processes | Test approach — test levels | Approach |
| 3.2 | Test strategy — Test sub-processes | Test approach — test types | Approach |
| 3.2.1 | Test strategy — Test sub-processes · Test design techniques | Test approach — test types | Approach |
| 3.3 | Test strategy — Test design techniques | Test approach — test techniques | Approach |
| 3.4 | Staffing — Roles, activities, and responsibilities | Test approach — independence of testing | Responsibilities |
| 3.5 | Test strategy — Retesting and regression testing | Test approach — test types | Approach |
| 3.6 | Test strategy — Metrics to be collected | Test approach — metrics to be collected | — |
| 3.7 | Test strategy — Test sub-processes | Test approach — test types *(kim tự tháp kiểm thử: CTFL v4.0 mục 5.1.6)* | Approach |
| 4.1 | Test strategy | Test approach — entry criteria | — |
| 4.2 | Test strategy — Test completion criteria | Test approach — exit criteria | Item pass/fail criteria |
| 4.3 | Test strategy — Suspension and resumption criteria | — | Suspension criteria and resumption requirements |
| 5.1 | Test strategy — Test environment requirements | Test approach — test environment requirements | Environmental needs |
| 5.2 | Test strategy — Test data requirements | Test approach — test data requirements | Environmental needs |
| 5.3 | Test strategy — Test environment requirements | — *(công cụ: CTFL v4.0 chương 6)* | Environmental needs |
| 6 | Staffing — Roles, activities, and responsibilities · Hiring needs · Training needs | Stakeholders — responsibilities, hiring and training needs | Responsibilities · Staffing and training needs |
| 7.1 | Schedule | Budget and schedule | Schedule |
| 7.2 | Testing activities and estimates | Budget and schedule | Testing tasks |
| 7.3 | Testing activities and estimates | Budget and schedule | — |
| 8.1 | Risk register — Project risks | Risk register — project risks | Risks and contingencies |
| 8.2 | Risk register — Product risks | Risk register — product risks | Risks and contingencies |
| 9 | — *(không có mục riêng trong Test Plan; báo cáo sự cố là tài liệu riêng — Incident Report)* | — *(quản lý lỗi: CTFL v4.0 mục 5.5)* | — *(Test incident report là tài liệu riêng)* |
| 10 | Test strategy — Test deliverables | Test approach — test deliverables | Test deliverables |
| 11 | Document-specific information — Approval authority | — | Approvals |
| 12.2 | Test strategy — Deviations from the Organizational Test Strategy | Test approach — deviations from the organizational test policy and test strategy | — |

**Rủi ro sản phẩm:** plan chỉ tóm tắt ở 8.2 — nguồn chính là tài liệu requirements và test case của từng module.

**Phần mở rộng ngoài khung chuẩn:** 3.7 Chiến lược tự động hoá · 9 Quản lý lỗi.

> Tên mục cột 29119-3 ghi theo khung Test Plan của chuẩn, chưa đối chiếu với bản chuẩn gốc — ô treo 19. Cột ISTQB đã đối chiếu giáo trình v4.0 (21-04-2023); bản sửa lỗi v4.0.1 chưa đối chiếu.

### 12.2 Điểm làm khác chính sách & chiến lược kiểm thử chung (Deviations)

Không áp dụng — tổ chức chưa có Test Policy và Test Strategy.
