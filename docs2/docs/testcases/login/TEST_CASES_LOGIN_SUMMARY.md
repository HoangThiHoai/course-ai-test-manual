# Test Cases — Module Đăng nhập / Xác thực (`LOGIN`) — tổng 60 TC · 112 biến thể · 1 nền tảng · độ hạt GỘP

| Thông tin | Nội dung |
|---|---|
| **Hệ thống** | Perfex CRM — Anh Tester Demo (`https://crm.anhtester.com`) · danh mục: [../README.md](../README.md) |
| **Module** | Đăng nhập / Xác thực · prefix `LOGIN` |
| **Nguồn requirement** | Index [REQUIREMENTS_LOGIN_SUMMARY.md](../../requirements/login/REQUIREMENTS_LOGIN_SUMMARY.md) · nền tảng [web/requirements_login_web.md](../../requirements/login/web/requirements_login_web.md) — 44 REQ, **40 trong phạm vi** (`27`, `34`, `35`, `40` ngoài phạm vi theo quyết định PO 18-08-2026) |
| **Mode sinh** | QUICK (`/generate-testcases-from-requirements`) · **độ hạt GỘP** |
| **Ngày sinh** | 21-09-2026 |
| **Dải TC ID** | `CRM_LOGIN_TC_001` → `CRM_LOGIN_TC_060` — chung mọi nền tảng |
| **Mã kế tiếp** | `CRM_LOGIN_TC_061` — **KHÔNG đánh lại từ 001** |
| **Mức rủi ro · độ sâu** | `Cao` → **Đầy đủ** — đủ 6 nhánh V1, mọi nhánh V2 có điều kiện kích hoạt, V3/V4 chấm từng nhánh.<br>Căn cứ chấm Cao: đụng **xác thực/phân quyền** · là **cổng vào** của 23 module còn lại (`RISK-LOGIN-06`) — một dấu hiệu đã đủ.<br>**Không hạ xuống khi:** chưa có module nào khác thay được vai trò cổng vào. **Rà lại độ sâu khi:** thêm nền tảng mobile/API, thêm đăng nhập bên thứ ba, hoặc bật lại tính năng Ghi nhớ đăng nhập (`REQ-LOGIN-40`) |
| **Môi trường** | ⚠️ **Dùng chung** — TC chỉ đọc hoặc tự dọn dữ liệu mình tạo (`CRM_LOGIN_TC_031`); không gửi mail đặt lại mật khẩu cho tài khoản thật |
| **Trình duyệt chuẩn** | Google Chrome, viewport desktop `1600×750`. Danh sách cam kết: Chrome · Edge · Firefox (người dùng chốt 19-09-2026) |
| **Tài khoản** | 🔒 Biến trong `.env`: `EMAIL_ADMIN`/`PASSWORD_ADMIN` · `EMAIL_PM`/`PASSWORD_PM` · `EMAIL_CUSTOMER`/`PASSWORD_CUSTOMER` — **KHÔNG** ghi giá trị thật vào tài liệu. ⚠️ `.env` hiện **mới có** biến Admin — xem Điều kiện #2 ở mục Đối soát cột Automation |

## Cách đọc bộ TC này

### 1. Độ hạt GỘP

- Biến thể của **cùng một trường**, **cùng loại phản hồi** nằm chung 1 TC ở **Bảng biến thể** (cột `Test Data`); kiểm tra tĩnh cùng màn hình nằm ở **Bảng kiểm** (cột `Expected Result`)
- Mỗi biến thể có mã riêng `a`, `b`, `c`… → báo FAIL **bắt buộc** ghi rõ: `CRM_LOGIN_TC_012-d FAIL`
- Chạy một TC là chạy **hết** biến thể của nó
- Sang automation: TC gộp → test data-driven (`test.each` · `@DataProvider` · `parametrize`), mỗi biến thể một bộ dữ liệu

### 2. Các ký hiệu trong TC

| Ký hiệu | Nghĩa | Tester làm gì |
|---|---|---|
| `🔧 Ghi chú kỹ thuật (cần DevTools)` + tag `@TechCheck` | Phần kiểm chứng không nhìn thấy trên màn hình (cookie, mã chống giả mạo, mã phản hồi) | Tester nghiệp vụ chạy **phần chính** là chấm được. Phần 🔧 do người có DevTools chạy thêm |
| 🐞 + tag `@KnownBug` | TC **thiết kế để FAIL** theo REQ ghi kỳ vọng đúng, bug đang mở | FAIL là kết quả đúng — ghi mã bug, **không** sửa TC |
| `⚠️ chưa có evidence` + tag `@NeedsVerify` | Kỳ vọng chưa có ảnh chụp chống lưng | Chạy và chụp ảnh bổ sung; lệch thì báo lại để sửa TC |
| tag `@PersonalOnly` | TC chạy trên 1 giờ — QA tự chạy, `/execute-test-cases` **bỏ qua** | Chạy tay ngoài đợt, ghi kết quả vào execution report sau |

## Bản đồ tài liệu

| Nền tảng | File | Nhóm chức năng | Số TC | Biến thể | TC ID | REQ bao phủ |
|---|---|---|---|---|---|---|
| Web | [web/parts/part_01_web_giao_dien_nhap_lieu.md](web/parts/part_01_web_giao_dien_nhap_lieu.md) | V1 Smoke · V2a Required & Validation (Email · Password · Remember me) | 22 | 51 | `001`–`022` | 01–15 · 23 · 24 · 29 · 31 · 32 · 36 · 38 |
| Web | [web/parts/part_02_web_phien_bao_mat_phi_chuc_nang.md](web/parts/part_02_web_phien_bao_mat_phi_chuc_nang.md) | V2b Phiên · Quên mật khẩu · Đoán lỗi · V3 Technical · V4 Non-functional · Bổ sung sau review 23-09-2026 (`054`–`060`) | 38 | 61 | `023`–`060` | 02 · 03 · 05 · 06 · 12–14 · 16–23 · 25 · 26 · 28–33 · 37 · 39 · 41–44 |
| Mobile | — | Chưa có requirements mobile | 0 | — | — | — |
| API | — | Chưa có requirements API | 0 | — | — | — |

> Web có 60 TC > ngưỡng 50 của độ hạt GỘP nên tách 2 part, cắt tại ranh giới **V2a | V2b** (giao diện & dữ liệu nhập | phiên & bảo mật). TC `054`–`060` bổ sung sau review nối vào **cuối part 02** để giữ dải ID liền của từng part, chia lại theo vòng ở mục riêng.

---

## Assumptions

| Mã | Điểm chưa rõ | Giả định đã áp dụng | TC bị ảnh hưởng |
|---|---|---|---|
| ASM-01 | Ảnh `login_form_375x700_fullpage.png` có trong `web/evidence/` nhưng **không** có dòng nào ở Danh mục Evidence (mục 12 requirements) | Dùng làm bằng chứng cho biến thể `375×700`. **Đề nghị bổ sung dòng vào Danh mục Evidence** | `CRM_LOGIN_TC_051-e` |
| ASM-02 | Phần trước `@` dài hơn 64 ký tự → máy chủ trả `The Email Address field must contain a valid email address.` (đo thật ở `run_1789759574`), nhưng mục 5 requirements **không** có dòng thông báo này và không REQ nào ràng buộc | Neo tạm vào `REQ-LOGIN-13` (kiểm định dạng email). **Đề nghị thêm REQ** cho kiểm định dạng phía máy chủ bằng `/update-requirements-from-ticket` | `CRM_LOGIN_TC_014`, `CRM_LOGIN_TC_015` |
| ASM-03 | Ảnh `login_form_empty_submit_error_fullpage.png` (ca gửi biểu mẫu **rỗng**) lại hiện sẵn `admin@example.com` và dấu chấm ở 2 ô | Không phải xung đột — là **trình duyệt tự điền** (đã giải thích ở mục 12 requirements). TC ghi *cửa sổ ẩn danh* ở tiền đề để tránh tự điền | `CRM_LOGIN_TC_009`–`011`, `024` |
| ASM-04 | Thứ tự `Tab` không chụp được bằng ảnh | Theo thứ tự hiển thị trên ảnh `login_form_default_fullpage.png` (Email → Password → Remember me → Login) + kết quả PASS của lần chạy `run_1787215085` | `CRM_LOGIN_TC_053` |
| ASM-05 | Mật khẩu tài khoản demo **toàn chữ số** (`RISK-LOGIN-07`) → không đảo kiểu chữ được | Cần tài khoản test riêng có mật khẩu **chứa chữ cái**, do QA lead cấp, lưu ở biến `EMAIL_CASE` / `PASSWORD_CASE` trong `.env` — môi trường dùng chung, QA không tự tạo tài khoản được (`/admin/staff` trả Từ chối truy cập). 🔒 Bản trước (mốc `82a814d`) từng ghi một mật khẩu dự kiến ngay trong tài liệu — **không** dùng chuỗi đó làm mật khẩu thật vì nó đã nằm trong lịch sử git | `CRM_LOGIN_TC_018` |
| ASM-06 | Liên kết đặt lại mật khẩu sai → trang lỗi của trình duyệt: đã chạy PASS ở `run_1787215085` nhưng **không** có ảnh | Kỳ vọng mô tả ở mức "trang lỗi của chính trình duyệt, không có giao diện ứng dụng" — không ghi câu chữ cụ thể của Chrome | `CRM_LOGIN_TC_037` |
| ASM-07 | Trang đăng nhập không nạp script (`REQ-LOGIN-37`) — hệ quả "tắt JavaScript vẫn đăng nhập được" **chưa đo** | Suy từ REQ: kiểm tra dữ liệu chạy ở máy chủ nên vẫn chạy khi tắt JavaScript | `CRM_LOGIN_TC_048` |
| ASM-08 | Đăng xuất ở màn hình điện thoại (`REQ-LOGIN-29` nhánh mobile): PASS ở `run_1787215085` (mã cũ `TC_033`, đã xác nhận hành vi thật) nhưng **không** có ảnh, và không tài liệu nào ghi vị trí nút mở menu. `REQ-LOGIN-29` ở requirements vẫn ghi nhánh mobile *"chưa recon"* — **ghi chú đó đã cũ**, cần cập nhật requirements | Mô tả vị trí ở mức "menu điều hướng thu gọn trên thanh đầu trang" — **không** đoán vị trí nút. Lần chạy tới chụp ảnh rồi bổ sung vào bước 2 | `CRM_LOGIN_TC_052` |
| ASM-09 | Email chứa dấu `'` (đúng chuẩn email) — máy chủ trả dải báo lỗi nào **chưa đo** | Giả định `Invalid email or password` (máy chủ dùng kiểm định dạng chuẩn, `'` hợp lệ). TC tách hai tầng: **bắt buộc** không vào Dashboard / không lỗi CSDL · **ghi nhận** câu chữ | `CRM_LOGIN_TC_046` |
| ASM-10 | Form tạo task và cách dừng bộ đếm giờ **chưa khảo sát chi tiết** — tầng khám phá ([module_06_cong_viec.md](../../requirements/_discovery/modules/module_06_cong_viec.md)) mới xác nhận có `New Task`, `Start Timer`, `Delete` trên từng dòng | Tiền đề TC_031 mô tả ở mức nút đã xác nhận; bước điền form và dừng timer ghi chung chung. Cập nhật lại khi module `TASK` có requirements | `CRM_LOGIN_TC_031` |
| ASM-11 | Password chỉ gồm khoảng trắng — máy chủ coi là trống hay đem đi so khớp **chưa đo** | Giả định coi là trống (`The Password field is required.`), đối xứng với ô Email ở TC_010-b | `CRM_LOGIN_TC_054` |
| ASM-12 | Trang Quên mật khẩu với email có khoảng trắng thừa, dài 64 ký tự trước `@`, hoặc chứa dấu `'` — câu chữ trả về **chưa đo** | Giả định `Email not found` như `REQ-LOGIN-26` (ô `type=email` tự bỏ khoảng trắng đầu/cuối trước khi gửi). TC_055 chỉ **ghi nhận** câu chữ, chấm theo "không gửi mail, không lỗi" | `CRM_LOGIN_TC_055`, `CRM_LOGIN_TC_059` |
| ASM-13 | Email sai định dạng phía máy chủ **và** Password trống cùng lúc — số dải và thứ tự **chưa đo** | Giả định 2 dải, Password trước (theo thứ tự đã đo ở TC_009) | `CRM_LOGIN_TC_060` |

---

## Bảng Đối Soát Coverage (toàn module)

> 40 REQ trong phạm vi · **40/40 có ≥ 1 TC** · Web ✅ trên mọi REQ (module mới có 1 nền tảng). Phép thử chiều ngược 6b: **không vi phạm**.

| REQ ID | Mô tả ngắn | Số TC | TC IDs (Web) | Đủ Positive/Negative/Boundary? | Ghi chú |
|---|---|---|---|---|---|
| REQ-LOGIN-01 | Truy cập trang đăng nhập | 1 | 001 | ✅ P | Trang tĩnh — chỉ có chiều Positive |
| REQ-LOGIN-02 | Thành phần biểu mẫu | 4 | 002, 019, 051, 053 | ✅ P/N | |
| REQ-LOGIN-03 | Con trỏ sẵn ở ô Email | 2 | 002, 053 | ✅ P | |
| REQ-LOGIN-04 | Logo về trang chủ | 1 | 004 | ✅ P | 🐞 `@KnownBug` |
| REQ-LOGIN-05 | Không CAPTCHA | 2 | 003, 023 | ✅ P/N | Mặc định: 003 · sau 6 lần sai: 023 |
| REQ-LOGIN-06 | Đăng nhập hợp lệ | 7 | 006, 038, 040, 041, 042, 050, 058 | ✅ P/N | |
| REQ-LOGIN-07 | Email không phân biệt hoa/thường | 1 | 016 | ✅ P (3 biến thể) | |
| REQ-LOGIN-08 | Tích Remember me → cookie ghi nhớ | 1 | 021 | ✅ P | |
| REQ-LOGIN-09 | Không tích → không cookie | 1 | 022 | ✅ N | |
| REQ-LOGIN-10 | Trống cả hai trường | 1 | 009 | ✅ N | |
| REQ-LOGIN-11 | Trống riêng Email | 1 | 010 | ✅ N (2 biến thể) | |
| REQ-LOGIN-12 | Trống riêng Password | 3 | 011, 054, 060 | ✅ N | 054 chỉ khoảng trắng · 060 kết hợp email sai định dạng |
| REQ-LOGIN-13 | Chặn email sai định dạng | 5 | 012, 014, 015, 046, 060 | ✅ P/N/B | Biên 64 ký tự trước `@` |
| REQ-LOGIN-14 | Thông báo sai thông tin | 6 | 013, 014, 018, 020, 045, 050 | ✅ N/B | |
| REQ-LOGIN-15 | Không lộ email có thật | 1 | 013 | ✅ N | TC_013 gánh REQ-14 (có TC khác) + REQ-15 (chỉ TC này) — hợp lệ theo 6b |
| REQ-LOGIN-16 | Giữ lại email sau lỗi | 1 | 024 | ✅ N | 🐞 thiết kế để FAIL |
| REQ-LOGIN-17 | Chặn URL nội bộ khi chưa đăng nhập | 2 | 025, 044 | ✅ N | |
| REQ-LOGIN-18 | Không nhớ URL đích | 1 | 026 | ✅ P | |
| REQ-LOGIN-19 | Có phiên → không vào trang đăng nhập | 1 | 027 | ✅ N (Admin, PM) | |
| REQ-LOGIN-20 | Có phiên → không vào Quên mật khẩu | 1 | 028 | ✅ N (Admin, PM) | |
| REQ-LOGIN-21 | Mã chống CSRF | 1 | 039 | ✅ P | `@TechCheck` |
| REQ-LOGIN-22 | Từ chối mã CSRF sai | 1 | 047 | ✅ N (sửa, xoá) | |
| REQ-LOGIN-23 | Trang Quên mật khẩu | 2 | 005, 036 | ✅ P/N | |
| REQ-LOGIN-24 | Không có lối quay lại | 1 | 005 | ✅ P | TC_005 gánh REQ-23 (có TC khác) + REQ-24 (chỉ TC này) — hợp lệ |
| REQ-LOGIN-25 | Quên mật khẩu — trống email | 1 | 034 | ✅ N | 🐞 thiết kế để FAIL |
| REQ-LOGIN-26 | Email không tồn tại | 3 | 035, 055, 059 | ✅ N/B | 055 chuỗi tấn công · 059 khoảng trắng + biên 64 |
| REQ-LOGIN-28 | Liên kết đặt lại sai | 1 | 037 | ✅ N (2 biến thể) | Hiện trạng được chấp nhận |
| REQ-LOGIN-29 | Một lối đăng xuất mỗi viewport | 2 | 007, 052 | ✅ P | Desktop + mobile |
| REQ-LOGIN-30 | Cảnh báo khi còn timer | 1 | 031 | ✅ P | Dựng tiền đề qua module `TASK` |
| REQ-LOGIN-31 | Không timer → đăng xuất ngay | 2 | 008, 056 | ✅ P | Admin + Project Manager |
| REQ-LOGIN-32 | Kết thúc phiên, về trang đăng nhập | 3 | 008, 029, 056 | ✅ P | |
| REQ-LOGIN-33 | URL nội bộ bị chặn sau đăng xuất | 3 | 029, 056, 057 | ✅ N (URL, Back, tab khác) | |
| REQ-LOGIN-36 | Không đăng nhập mạng xã hội | 1 | 002 | ✅ P | Bảng kiểm mục `6` |
| REQ-LOGIN-37 | Không nạp JavaScript | 1 | 048 | ✅ P | `@NeedsVerify` |
| REQ-LOGIN-38 | Bỏ khoảng trắng đầu/cuối email | 1 | 017 | ✅ P (3 biến thể) | |
| REQ-LOGIN-39 | Cookie ghi nhớ không tự đăng nhập lại | 1 | 030 | ✅ N | |
| REQ-LOGIN-41 | Không khoá tài khoản | 1 | 023 | ✅ N | |
| REQ-LOGIN-42 | Phiên hết hạn sau 1 giờ | 2 | 032, 033 | ✅ P/N (AC1 + AC2) | `@PersonalOnly` |
| REQ-LOGIN-43 | Customer bị từ chối ở `/admin` | 2 | 043, 044 | ✅ N | |
| REQ-LOGIN-44 | Ép HTTPS | 1 | 049 | ✅ N | 🐞 thiết kế để FAIL |
| REQ-LOGIN-27 · 34 · 35 · 40 | — | 0 | — | ➖ | **Ngoài phạm vi** theo quyết định PO 18-08-2026 (`AMB-LOGIN-04`, `06`, `07`, `15`) |

### Bảng quyết định — kết quả gửi biểu mẫu đăng nhập

| Rule | Email | Password | → Kết quả | TC |
|---|---|---|---|---|
| R1 | Trống | Trống | 2 dải `…Password…required` + `…Email Address…required` | 009 |
| R2 | Trống | Có | 1 dải `The Email Address field is required.` | 010 |
| R3 | Đúng định dạng | Trống / chỉ khoảng trắng | 1 dải `The Password field is required.` | 011, 054 |
| R4 | Sai định dạng (trình duyệt) | Bất kỳ | Trình duyệt chặn, không gửi | 012 |
| R5 | Sai định dạng (máy chủ — > 64 ký tự trước `@`) | Có | 1 dải `The Email Address field must contain a valid email address.` | 015 |
| R6 | Không tồn tại | Có | 1 dải `Invalid email or password` | 013-a, 013-c |
| R7 | Tồn tại · Admin/PM | Sai | 1 dải `Invalid email or password` | 013-b, 018, 020, 023, 045 |
| R8 | Tồn tại · Customer | Đúng | 1 dải `Invalid email or password` | 043 |
| R9 | Tồn tại · Admin/PM | Đúng | Vào Dashboard | 006, 016, 017, 042, 058 |
| R10 | Sai định dạng (máy chủ) | Trống | 2 dải: `The Password field is required.` rồi `…must contain a valid email address.` — chưa đo (`ASM-13`) | 060 |

---

## Đối soát Evidence

Đã mở **10/10** ảnh trong [`web/evidence/`](../../requirements/login/web/evidence/) ngày 21-09-2026.

| Ảnh evidence | Màn hình / trạng thái | TC dựa vào | Đầy đủ? |
|---|---|---|---|
| `login_form_default_fullpage.png` | Đăng nhập — mặc định | 001, 002, 003, 004, 053 | ✅ full-page |
| `login_form_filled_remember_checked_fullpage.png` | Đăng nhập — đã nhập, Remember me tích | 019, 021 | ✅ full-page |
| `login_form_empty_submit_error_fullpage.png` | Gửi rỗng — 2 dải lỗi | 009 | ✅ (ô có nội dung tự điền — `ASM-03`) |
| `login_form_wrong_credentials_fullpage.png` | Sai thông tin — `Invalid email or password` | 013, 023, 024 | ✅ full-page |
| `login_csrf_invalid_403_fullpage.png` | Mã CSRF sai — `419 Page Expired!` | 047 | ✅ full-page |
| `login_success_dashboard_viewport.png` | Dashboard sau đăng nhập — 14 mục menu trái | 006, 016, 017 | ✅ viewport (đúng phạm vi) |
| `logout_menu_open_viewport.png` | Menu ảnh đại diện đang mở — 5 mục | 007, 008 | ✅ viewport |
| `forgot_password_form_default_fullpage.png` | Quên mật khẩu — mặc định | 005 | ✅ full-page |
| `forgot_password_empty_submit_error_fullpage.png` | Quên mật khẩu gửi trống — `Email not found` | 034, 035 | ✅ full-page |
| `login_form_375x700_fullpage.png` | Đăng nhập ở `375×700` | 051-e | ⚠️ Không có trong Danh mục Evidence (`ASM-01`) |
| Ảnh ở [`executions/login/web/run_1789759574/evidence/`](../../executions/login/web/run_1789759574/evidence/) | Biên 64 ký tự · mật khẩu dài · 5 kích thước màn hình · 3 trình duyệt · dán mật khẩu | 014, 015, 019, 020, 050, 051 | ⚠️ Đo thật, nhưng **thư mục `executions/login/` đã bị xoá khỏi working tree** (git báo `D`, 23-09-2026) — file vẫn còn ở mốc `82a814d`. Khôi phục lại hoặc chuyển các dòng này sang `⚠️ chưa có evidence` |
| Ảnh `TC_034_logout_confirm_dialog.png` ở `run_1789759574` | Hộp xác nhận đăng xuất khi còn timer | 031 | ⚠️ Như dòng trên — file đã bị xoá khỏi working tree |
| (không có) | Trang lỗi trình duyệt khi liên kết đặt lại sai | 037 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Menu thu gọn + `Logout` ở `375×812` | 052 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Trang đăng nhập khi tắt JavaScript | 048 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Dải báo lỗi với email chứa `'` | 046 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Password chỉ gồm khoảng trắng | 054 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Quên mật khẩu: chuỗi tấn công · khoảng trắng · biên 64 | 055, 059 | 🔴 THIẾU — `@NeedsVerify` |
| (không có) | Email sai định dạng phía máy chủ + Password trống | 060 | 🔴 THIẾU — `@NeedsVerify` |

### Vùng chưa có evidence — đề xuất recon bổ sung

| TC | Cần chụp | Chuẩn chụp |
|---|---|---|
| `CRM_LOGIN_TC_037` | Trang lỗi sau khi mở liên kết đặt lại sai (biến thể `a`) | Viewport `1600×750` — `reset_password_invalid_key_viewport.png` |
| `CRM_LOGIN_TC_052` | Thanh đầu trang ở `375×812` với menu thu gọn **đang mở**, thấy `Logout` | Viewport — `logout_mobile_menu_open_375x812.png` |
| `CRM_LOGIN_TC_048` | Trang đăng nhập khi tắt JavaScript, sau khi gửi rỗng | Full-page — `login_js_disabled_empty_submit_fullpage.png` |
| `CRM_LOGIN_TC_046` | Dải báo lỗi với email `admin'--@example.com` | Full-page — `login_email_quote_message_fullpage.png` |
| `CRM_LOGIN_TC_054` | Dải báo lỗi khi Password chỉ gồm 3 khoảng trắng | Viewport — `login_password_spaces_only_viewport.png` |
| `CRM_LOGIN_TC_055` | Quên mật khẩu với email `admin'--@example.com` | Viewport — `forgot_password_email_quote_viewport.png` |
| `CRM_LOGIN_TC_059` | Quên mật khẩu với email có khoảng trắng thừa (biến thể `a`) | Viewport — `forgot_password_email_spaces_viewport.png` |
| `CRM_LOGIN_TC_060` | 2 dải báo lỗi khi email 65 ký tự trước `@` + Password trống | Viewport — `login_email_format_password_empty_viewport.png` |

---

## Đối soát Field-Level (bảng 15 loại field)

| Field | Loại | Mục bảng | Trạng thái | TC / Lý do |
|---|---|---|---|---|
| Email Address (Đăng nhập) | Email | Format hợp lệ | ✅ | 013-c, 014 |
| | | Thiếu `@` | ✅ | 012-a |
| | | Thiếu domain | ✅ | 012-b |
| | | Domain không hợp lệ | ✅ | 012-e |
| | | Nhiều `@` | ✅ | 012-d |
| | | Ký tự đặc biệt trước `@` | ✅ | 012-f (không hợp lệ), 013-c · 046 (hợp lệ) |
| | | Max length | ✅ | 014, 015 — ô không giới hạn, biên nằm ở 64 ký tự trước `@` |
| | | Case sensitivity | ✅ | 016 |
| | | Email đã tồn tại | ➖ | Không áp dụng — màn hình đăng nhập không tạo email mới |
| | *(bổ sung)* | Khoảng trắng đầu/cuối · chỉ khoảng trắng | ✅ | 017, 010-b |
| | *(bổ sung)* | Chuỗi tấn công | ✅ | 046 · XSS vào ô Email ➖: ký tự `<` `>` bị trình duyệt chặn ở bước định dạng |
| | | **Tổng** | **đủ 8/8 mục áp dụng** + 1 ➖ | |
| Password | Password | Min/Max length | ➖ | `AMB-LOGIN-09` ✅: không có chính sách mật khẩu → không có biên. Độ bền với chuỗi dài: 020-a/b |
| | | Yêu cầu ký tự đặc biệt | ➖ | Không có chính sách (`AMB-LOGIN-09`) |
| | | Yêu cầu chữ hoa/thường | ➖ | Không có chính sách. Phân biệt hoa/thường **khi so khớp**: 018 |
| | | Yêu cầu số | ➖ | Không có chính sách |
| | | Copy-paste bị chặn? | ✅ | 019 — dán được |
| | | Hiện/ẩn password | ✅ | 019 — không có nút, xác nhận vắng mặt |
| | | Confirm password | ➖ | Màn hình đăng nhập không có ô xác nhận |
| | *(bổ sung)* | Che ký tự · Unicode/emoji · chuỗi tấn công | ✅ | 019, 020-c, 045 |
| | *(bổ sung)* | Chỉ gồm khoảng trắng | ✅ | 054 `@NeedsVerify` |
| | *(bổ sung)* | Khoảng trắng đầu/cuối quanh mật khẩu đúng | 🔴 | Chưa có REQ — chốt REQ trước (review 23-09-2026, gap #2) |
| | | **Tổng** | **đủ 2/2 mục áp dụng** + 5 ➖ có lý do | |
| Remember me | Checkbox | Trạng thái mặc định | ✅ | 002 mục `3`, 022 |
| | | Check / Uncheck | ✅ | 021 (tích bằng chữ), 053 (tích bằng `Space`) |
| | | Required | ➖ | Không bắt buộc |
| | | Nhóm radio | ➖ | Không phải radio |
| Email Address (Quên mật khẩu) | Email | Required | ✅ | 034 🐞 |
| | | Format sai | ✅ | 036 (3 biến thể) |
| | | Không tồn tại | ✅ | 035 |
| | | Chuỗi tấn công | ✅ | 055 `@NeedsVerify` |
| | | Khoảng trắng đầu/cuối · biên 64 ký tự trước `@` | ✅ | 059 `@NeedsVerify`. Ca > 64 ký tự: chưa recon |
| | | Tồn tại | ⏭️ | `REQ-LOGIN-27` ngoài phạm vi — **PO quyết định 18-08-2026** (`AMB-LOGIN-04`). Rà lại khi có hộp thư test đọc được qua API |

---

## Đối soát loại kiểm thử (4 vòng)

| Vòng | Nhánh | Trạng thái | TC ID / Lý do |
|---|---|---|---|
| 1 | UI cơ bản | ✅ | TC_001–TC_004 (4 TC · 9 mục kiểm) — nhãn nguyên văn, thứ tự, mặc định, con trỏ |
| 1 | Open form | ✅ | TC_005 (lối vào bằng liên kết + URL), TC_007 (mở menu ảnh đại diện) — 2 TC · 8 mục. Đóng bằng X/ESC ➖: không có modal |
| 1 | Display | ✅ | TC_006 (Dashboard: tiêu đề tab, 14 mục menu), TC_007 — 2 TC · 4 mục |
| 1 | Input valid data | ✅ | TC_006 (bộ tối thiểu Email + Password), TC_021 (bộ đầy đủ có Remember me) |
| 1 | Save | ✅ | TC_006 — "lưu" ở module này là gửi biểu mẫu đăng nhập, điều hướng đúng về Dashboard |
| 1 | Verify data | ✅ | TC_006, TC_008 — xác nhận trạng thái phiên (vào được / ra được) |
| 2 | UI Behavior | ✅ | TC_009 (nút `Login` không tự khoá), TC_019 (che ký tự, không nút hiện/ẩn), TC_021 (bấm chữ tích ô), TC_058 (Enter trong ô Password) — 4 TC |
| 2 | Required | ✅ | TC_009, TC_010, TC_011, TC_034, TC_054 — 5 TC · 6 biến thể |
| 2 | Validation | ✅ | TC_012–TC_022, TC_036, TC_059 — 13 TC · 34 biến thể · đủ 8/8 mục bảng Email (đăng nhập) · 2/2 mục áp dụng bảng Password · 2/2 mục bảng Checkbox. Còn thiếu: khoảng trắng quanh mật khẩu (chờ REQ) |
| 2 | Equivalence Partitioning | ✅ | Email: sai định dạng (012) · đúng định dạng không tồn tại (013-a/c) · tồn tại sai mật khẩu (013-b) · tồn tại đúng (006) |
| 2 | Boundary Value Analysis | ✅ | TC_014, TC_015 — 2 TC · 5 biến thể (63 · 64 · 65 · 100 · 250 ký tự trước `@`). Biên Password ➖ — không có chính sách độ dài |
| 2 | Business Rule | ✅ | TC_023 (không khoá), TC_024 (giữ email 🐞), TC_013 (thông báo chung) |
| 2 | Decision Table | ✅ | Bảng quyết định 10 rule ở mục Coverage — mỗi rule trỏ về TC (R10 → TC_060) |
| 2 | State Transition | ✅ | TC_025–TC_033, TC_056, TC_057 (11 TC · 15 biến thể) — bảng chuyển trạng thái phiên ở part 02, có thêm ca nhiều tab |
| 2 | Dependency | ➖ | Không có trường phụ thuộc nhau — 2 ô nhập và ô tích độc lập |
| 2 | Use Case / Scenario | ✅ | TC_026 (bị chặn → đăng nhập → Dashboard), TC_030 (đăng nhập ghi nhớ → đăng xuất → thử vào lại) |
| 2 | Save / Edit / Delete | ➖ | Module không có CRUD |
| 2 | Error Guessing | ✅ | TC_038 (nhấp đúp), TC_039 (nạp lại nhiều lần), TC_040 (mất mạng), TC_041 (mạng chậm) — 4 TC |
| 3 | Permission | ✅ | TC_042 (PM), TC_043 · TC_044 (Customer), TC_027-b · TC_028-b (PM), TC_056 (PM đăng xuất) — phủ các hàng ma trận thuộc phạm vi module (mở trang đăng nhập / Quên mật khẩu · gửi biểu mẫu · mở URL nội bộ · vào Dashboard · đăng xuất). Bản trước ghi đã phủ đăng xuất cho cả 3 vai trò nhưng chưa có TC cho PM — đã bổ sung TC_056 (review 23-09-2026). Hàng "Mở khu Setup" thuộc module Setup — ngoài phạm vi |
| 3 | Security | ✅ | TC_003, 013, 023, 025, 029, 030, 045, 046, 047, 049, 055, 057 — truy cập khi chưa đăng nhập, sau đăng xuất, nút Back, tab khác, SQLi/XSS (cả trang Quên mật khẩu), CSRF, dò tài khoản, HTTPS. Chống cố định phiên: chưa có REQ — chốt REQ trước (review 23-09-2026, gap #9) |
| 3 | API | ➖ | QA không có quyền gọi API — **đội Dev** xác minh (`docs/requirements/README.md`, chốt 11-09-2026). TC_049 chỉ đọc phản hồi của trang, không gọi API nghiệp vụ |
| 3 | Database | ➖ | Không có quyền truy vấn CSDL — **đội Dev** xác minh |
| 3 | Integration | ⏭️ | Cố ý bỏ — tích hợp gửi mail đặt lại mật khẩu **có tồn tại** nhưng **PO quyết định 18-08-2026** không kiểm (`REQ-LOGIN-27` ngoài phạm vi, `AMB-LOGIN-04`). Rà lại khi có hộp thư test đọc được qua API. Không có tích hợp bên thứ ba khác (không CAPTCHA, không OAuth — `REQ-LOGIN-05`, `36`) |
| 3 | Logging / Audit | ➖ | Requirements không có yêu cầu nhật ký đăng nhập; QA không mở được Activity Log (đo 11-09-2026) |
| 4 | Compatibility | ✅ | TC_050 (1 TC · 3 biến thể: Chrome · Edge · Firefox). Safari **không** kiểm — không có máy macOS |
| 4 | Responsive / UI Stability | ✅ | TC_051 (5 biến thể: 1920 · 1600 · 1366 · 768 · 375), TC_052 (đăng xuất ở 375×812) |
| 4 | Accessibility | ✅ | TC_053 (Tab/Space/Enter, viền tiêu điểm, nhãn gắn ô), TC_002 mục `5`. WCAG đầy đủ ➖ — cần công cụ riêng, đội UX |
| 4 | Performance | ➖ | Requirements không có ngưỡng thời gian cam kết. Đo tải thuộc **đội Hạ tầng**. TC_041 chỉ kiểm hoàn tất trên mạng chậm |
| 4 | Regression | ✅ | TC_015-c — chống tái phát ca `BUG_login_1787226515_TC018` (bug duy nhất đã đóng, kết luận *không phải lỗi*) |
| 4 | E2E | 🟡 | TC_031 — luồng xuyên module `TASK` → `LOGIN` (timer đang chạy → đăng xuất). **Chưa chạy được** tới khi PO cho phép bật timer trên môi trường dùng chung (`AMB-LOGIN-14`) |

## Rà soát đặc tính chất lượng (ISO/IEC 25010:2023)

| Đặc tính | Trạng thái | TC ID / Lý do |
|---|---|---|
| Functional Suitability | ✅ Có TC | TC_001–TC_049, TC_054–TC_060 |
| Performance Efficiency | ➖ Ngoài phạm vi | Không có ngưỡng cam kết, không có công cụ tải — **đội Hạ tầng**. Quan sát thô: TC_041 |
| Compatibility | ✅ Có TC | TC_050 (Chrome, Edge, Firefox) |
| Interaction Capability | ✅ Có TC | TC_002 (nhãn, mặc định), TC_009–TC_013 (thông báo lỗi rõ ràng), TC_019, TC_053 (bàn phím) |
| Reliability | ✅ Có TC | TC_032, TC_033 (hết phiên / gia hạn), TC_038 (nhấp đúp), TC_040 (mất mạng), TC_041 (mạng chậm) |
| Security | ✅ Có TC | TC_003, 013, 023, 024, 025, 029, 030, 042–047, 049, 055, 057. Pentest / quét lỗ hổng: ➖ **đội Bảo mật** (`RISK-LOGIN-01`, `02` đã báo) |
| Maintainability | ➖ Không áp dụng | Đặc tính của mã nguồn — code review của **đội Dev** |
| Flexibility | ✅ Có TC | TC_051, TC_052 (responsive). Đổi ngôn ngữ ➖ — thuộc module `PROF`, trang đăng nhập chỉ có tiếng Anh |
| Safety | ➖ Không áp dụng | App nghiệp vụ CRM, lỗi đăng nhập không gây thiệt hại vật lý — **PO** xác nhận phạm vi |

## Đối soát cột Automation

| Nền tảng | Yes | Partial | No | ⏸️ Hoãn |
|---|---|---|---|---|
| Web | 54 | 6 | 0 | 8 (nằm trong 54 `Yes`) |

### Điều kiện cần chuẩn bị

| # | Điều kiện | Ai cấp | Trạng thái | TC phụ thuộc |
|---|---|---|---|---|
| 1 | Tài khoản test có mật khẩu chứa chữ cái — biến `EMAIL_CASE` / `PASSWORD_CASE` trong `.env` | QA lead / PO | ⏳ Chưa có | TC_018 |
| 2 | Bổ sung biến `EMAIL_PM`, `PASSWORD_PM`, `EMAIL_CUSTOMER`, `PASSWORD_CUSTOMER` vào `.env` (tài khoản đã được cấp 18-08-2026) | QA | ⏳ `.env` mới có biến Admin | TC_027-b, TC_028-b, TC_042, TC_043, TC_044, TC_056 |
| 3 | Môi trường test có thời hạn phiên rút ngắn (VD 2 phút) | Dev backend | ⏳ Chưa có | TC_032, TC_033 |
| 4 | Được phép bật timer trên task tự tạo ở môi trường dùng chung | PO (`AMB-LOGIN-14`) | ⏳ Chuyển sang module `TASK` | TC_031 |

### TC Partial · No · Hoãn

| TC ID | Nền tảng | Automation | Trục chặn | Điều kiện · phần kiểm tay · lý do |
|---|---|---|---|---|
| CRM_LOGIN_TC_018 | Web | Partial | 2 · tiền đề | Điều kiện #1 |
| CRM_LOGIN_TC_031 | Web | Partial | 2 · tiền đề | Điều kiện #4 — dựng task + timer, dọn sau khi chạy |
| CRM_LOGIN_TC_032 | Web | Partial | 1 · thời gian thật phía máy chủ | Điều kiện #3 — không có thì chạy tay (`@PersonalOnly`) |
| CRM_LOGIN_TC_033 | Web | Partial | 1 · thời gian thật phía máy chủ | Điều kiện #3 |
| CRM_LOGIN_TC_051 | Web | Partial | 2 · phần cần mắt người | Máy chấm: không cuộn ngang, đủ thành phần, độ rộng nút. Kiểm tay: không đè chữ, bố cục cân đối |
| CRM_LOGIN_TC_053 | Web | Partial | 2 · phần cần mắt người | Máy chấm: thứ tự Tab, Space/Enter. Kiểm tay: viền tiêu điểm nhìn thấy rõ |
| CRM_LOGIN_TC_037 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — chờ ảnh (`ASM-06`) |
| CRM_LOGIN_TC_046 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — chờ đo câu chữ (`ASM-09`) |
| CRM_LOGIN_TC_048 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — chờ đo (`ASM-07`) |
| CRM_LOGIN_TC_052 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — chờ ảnh (`ASM-08`) |
| CRM_LOGIN_TC_054 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — chờ đo (`ASM-11`) |
| CRM_LOGIN_TC_055 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — chờ đo câu chữ (`ASM-12`) |
| CRM_LOGIN_TC_059 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — chờ đo (`ASM-12`) |
| CRM_LOGIN_TC_060 | Web | Yes · ⏸️ Hoãn | — | `@NeedsVerify` — chờ đo (`ASM-13`) |

> **Thứ tự ưu tiên automate:** `@Smoke`/`@CriticalPath` (001, 002, 005–008, 013, 025, 029) → TC nhiều biến thể (012, 015–017, 020, 051) → TC 🐞 `@KnownBug` (004, 024, 034, 049) → phần còn lại.

---

## Ánh xạ TC ID cũ → mới (bug & execution report)

Bộ TC trước (51 TC, `CRM_LOGIN_TC_001`→`051`) đã bị **xoá khỏi đĩa trước khi sinh lại** và **chưa từng được commit** — không còn mốc git để tra. Mã TC trong 6 bug và 2 execution report cũ đang trỏ vào **nghĩa cũ**:

| Bug | TC ID cũ | Nội dung | TC ID mới | Ghi chú |
|---|---|---|---|---|
| `BUG_login_1785678750_TC039` | `CRM_LOGIN_TC_039` | Không ép HTTPS | `CRM_LOGIN_TC_049` | Đang mở |
| `BUG_login_1787226513_TC004` | `CRM_LOGIN_TC_004` | Logo không về trang chủ | `CRM_LOGIN_TC_004` | Trùng số — đang mở |
| `BUG_login_1787226514_TC016` | `CRM_LOGIN_TC_016` | Không giữ email sau lỗi | `CRM_LOGIN_TC_024` | Đang mở |
| `BUG_login_1787226515_TC018` | `CRM_LOGIN_TC_018-a` | Email 260 ký tự | `CRM_LOGIN_TC_015-c` | Đã đóng — không phải lỗi |
| `BUG_login_1787226516_TC028` | `CRM_LOGIN_TC_028` | Quên mật khẩu trống → `Email not found` | `CRM_LOGIN_TC_034` | Đang mở |
| `BUG_login_1787226517_TC029` | `CRM_LOGIN_TC_029` | Ô Email Quên mật khẩu không tự xoá sau khi gửi | `CRM_LOGIN_TC_035` (gần nhất) | ⚠️ **Không REQ nào** yêu cầu ô tự xoá — bộ TC mới không khẳng định hành vi này. Cần PO chốt có giữ bug không |

> ⚠️ Execution report `run_1787215085` và `run_1789759574` giữ nguyên làm lịch sử — **đọc theo mã cũ**. Lần chạy sau dùng mã mới.
>
> ⚠️ **23-09-2026:** 6 file bug ở `docs/bugs/login/web/` và 2 execution report ở trên **đã bị xoá khỏi working tree** (git báo `D`, chưa commit). Chúng vẫn còn ở mốc `82a814d` (`git show 82a814d:<đường dẫn>`). Nếu xoá là cố ý thì phải ghi bug đã chuyển đi đâu — bảng trên đang trỏ vào file không còn trên ổ đĩa.

## Nhật ký thay đổi

| Ngày | Thay đổi |
|---|---|
| 21-09-2026 | **Sinh mới toàn bộ** bằng `/generate-testcases-from-requirements` Mode QUICK, độ hạt GỘP, rủi ro Cao → Đầy đủ — **53 TC · 101 biến thể**, 2 part, phủ **40/40 REQ** trong phạm vi. Bộ cũ 51 TC đã bị xoá trước đó, chưa commit nên không có mốc git; TC ID đánh lại từ `001` — xem mục *Ánh xạ TC ID cũ → mới*. 4 TC thiết kế để FAIL (`004`, `024`, `034`, `049`) · 4 TC `@NeedsVerify` · 9 Assumptions |
| 23-09-2026 | **`/review-testcases` Mode FIX** — báo cáo [review/testcase_review_report_web_20260923.md](review/testcase_review_report_web_20260923.md). **Mốc git trước khi sửa: `82a814d`** (cả index và 2 part) — xem bản cũ bằng `git show 82a814d:<đường dẫn file>`. **Sửa tại chỗ 14 TC:** `018` (bỏ mật khẩu viết thẳng, dùng `EMAIL_CASE`/`PASSWORD_CASE`) · `031` (thêm bước dựng task, tách hậu điều kiện dọn dữ liệu) · `008` (kiểm timer chuyển thành tiền đề, có timer → BLOCKED) · `044` (tự đăng nhập Customer, bỏ phụ thuộc TC_043) · `021`, `022` (cookie chỉ chấm được bằng DevTools) · `046` (tách tiêu chí bắt buộc / ghi nhận) · `020` (≤ 5 giây, đổi tag) · `006` (liệt kê đủ 14 mục menu) · `002`, `003`, `022` (bỏ bước trùng với `019` / `023` / `002`) · `019` (tách bước gộp) · `052` (ghi chú evidence) · `023` (thêm neo `REQ-LOGIN-05`). **Thêm 7 TC** `054`–`060` (gap #1, #3–#8), trong đó 4 TC `@NeedsVerify`. Index: sửa nhãn Permission · Integration (`➖` → `⏭️`) · E2E (✅ → 🟡), thêm `ASM-10`…`ASM-13`, rule `R10`, đánh dấu evidence/bug đã bị xoá khỏi working tree. Tổng **60 TC · 112 biến thể** |
