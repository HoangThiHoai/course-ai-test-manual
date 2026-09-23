# Báo Cáo Review Test Cases — `LOGIN` · Web

> ⬆️ Index bộ TC: [../TEST_CASES_LOGIN_SUMMARY.md](../TEST_CASES_LOGIN_SUMMARY.md) · Requirements: [../../../requirements/login/web/requirements_login_web.md](../../../requirements/login/web/requirements_login_web.md)

## Tổng quan

- **Mode:** REVIEW (`/review-testcases`) — **không** sửa file TC nào
- **Ngày review:** 23-09-2026
- **Nguồn:** [web/parts/part_01_web_giao_dien_nhap_lieu.md](../web/parts/part_01_web_giao_dien_nhap_lieu.md) · [web/parts/part_02_web_phien_bao_mat_phi_chuc_nang.md](../web/parts/part_02_web_phien_bao_mat_phi_chuc_nang.md)
- **Mốc git của bộ TC lúc review:** file sạch, không có thay đổi chưa commit
- **Số TC review:** 53 (101 biến thể/mục kiểm — đã đếm lại, khớp số ghi ở index) · `@Deprecated`: 0
- **Kết quả:** 🟢 53 tốt | 🟡 0 cần sửa | 🔴 0 nên viết lại
- **Điểm trung bình:** 11,70/12 (39 TC đạt 12 · 12 TC đạt 11 · 2 TC đạt 10)
- **Requirements đối chiếu:** có — 40 REQ trong phạm vi, 40/40 có TC

> ⚠️ Tất cả TC đều 🟢 **không** có nghĩa bộ TC đã đủ. Rubric chỉ chấm cách viết từng TC. Lỗ hổng thật của bộ này nằm ở **mức bộ**: có 9 kịch bản còn thiếu, 3 nhánh ở bảng 4 vòng đang ghi nhãn sai, TC_018 có nguy cơ lộ mật khẩu, và các link evidence/bug đang trỏ vào file đã bị xoá khỏi ổ đĩa. Xem các mục bên dưới.

---

## Chi tiết từng TC

Cột C1–C6 = Rõ ràng · Expected đo được · Độc lập · Test data · Truy vết · Đúng trọng tâm.

### TC chưa đạt tối đa

| TC ID | C1 | C2 | C3 | C4 | C5 | C6 | Điểm | Xếp loại | Vấn đề chính | Đề xuất sửa |
|---|---|---|---|---|---|---|---|---|---|---|
| CRM_LOGIN_TC_018 | 2 | 2 | 1 | 1 | 2 | 2 | 10/12 | 🟢 | 🔒 **Ghi mật khẩu dự kiến vào tài liệu:** Pre-Condition ghi *"mật khẩu `<chuỗi dự kiến>` do QA lead cấp"*, và biến thể `a` (chuỗi đảo kiểu chữ) cho ra ngay mật khẩu gốc. Khi QA lead tạo tài khoản đúng mật khẩu này, `docs/` sẽ chứa bí mật thật (vi phạm quy tắc 🔒 của CLAUDE.md, và **không xoá được khỏi lịch sử git** nếu đã commit). Ngoài ra, TC phụ thuộc một tài khoản **chưa tồn tại** (Điều kiện #1 ⏳), nên khi chạy chỉ ra được BLOCKED | Pre-Condition: *"Tài khoản test có mật khẩu chứa chữ cái, lưu ở `EMAIL_CASE` / `PASSWORD_CASE` trong `.env` (xem `ASM-05`). Chưa có biến này thì ghi BLOCKED"*. Test Data: `a` *"Đảo toàn bộ kiểu chữ của `PASSWORD_CASE`"* · `b` *"Chỉ đổi kiểu chữ ký tự chữ cái đầu tiên của `PASSWORD_CASE`"*. Sửa luôn `ASM-05` ở index (câu đó cũng đang ghi mật khẩu). Nhắc QA lead **đừng** đặt đúng mật khẩu dự kiến ghi ở mốc `82a814d`, vì chuỗi này đã nằm trong lịch sử git |
| CRM_LOGIN_TC_031 | 1 | 2 | 2 | 1 | 2 | 2 | 10/12 | 🟢 | (1) Pre-Condition ghi *"dựng theo module `TASK`"* nhưng không có bước tạo task và bật bộ đếm giờ, nên tester chưa biết module TASK thì không chạy được. (2) Expected bước 1 chấm theo tên mẫu cố định *"đúng task `Auto_LOGIN_TC031_1790000000`"*, trong khi tên thật lấy theo timestamp lúc chạy. (3) Bước 5 là bước dọn dữ liệu nằm trong Steps: nếu TC FAIL ở bước 2 thì tester dừng lại, và task rác ở lại trên môi trường dùng chung | (1) Thêm Pre-Condition: *"a. Menu `Tasks` → `New Task`, Subject `Auto_LOGIN_TC031_<timestamp>` → `Save` · b. Trên trang task vừa tạo bấm `Start Timer`"*. (2) Expected bước 1: *"Danh sách có đúng task `Auto_LOGIN_TC031_<timestamp>` vừa tạo ở Pre-Condition"*. (3) Chuyển bước 5 thành dòng **Hậu điều kiện (luôn làm, dù PASS hay FAIL):** *"Đăng nhập lại Admin → dừng timer → xoá task vừa tạo"* |
| CRM_LOGIN_TC_002 | 2 | 2 | 2 | 2 | 2 | 1 | 11/12 | 🟢 | Bảng kiểm Kiểu B (6 mục tĩnh) lại có thêm 2 bước **tương tác** (bước 3 gõ để kiểm con trỏ, bước 4 gõ để kiểm che ký tự). Hai hành vi này đã có TC riêng: `TC_053` bước 2 kiểm con trỏ, `TC_019` bước 2 kiểm che ký tự | Giữ TC_002 ở mức quan sát tĩnh: bỏ bước 3–4, mục `5` giữ nguyên (*"Ô Email có viền xanh — đang được chọn sẵn"*). Nếu muốn smoke vẫn phủ REQ-03 thì giữ bước 3 và bỏ bước 4, vì che ký tự đã có ở TC_019 |
| CRM_LOGIN_TC_006 | 2 | 1 | 2 | 2 | 2 | 2 | 11/12 | 🟢 | Expected *"đủ **14** mục (`Dashboard` → `Reports`)"* chỉ ghi mục đầu và mục cuối. Tester không biết 12 mục ở giữa là gì nên không chấm được "đúng mục". TC_042 lại liệt kê đủ 5 mục chỉ Admin có, nên hai TC không cùng mức chi tiết | Liệt kê nguyên văn 14 mục theo đúng thứ tự trong ảnh `login_success_dashboard_viewport.png`, VD *"`Dashboard` · `Customers` · … · `Reports`"* |
| CRM_LOGIN_TC_008 | 2 | 2 | 1 | 2 | 2 | 2 | 11/12 | 🟢 | Tài khoản Admin **dùng chung**, người khác có thể đang bật timer. Bước 1 đang dùng Expected để kiểm tiền đề (*"ghi `No started timers found`"*). Nếu có timer thì theo cách viết hiện tại, tester sẽ chấm FAIL nhầm, trong khi đúng ra phải là BLOCKED | Chuyển bước 1–2 thành Pre-Condition: *"Bấm biểu tượng đồng hồ, xác nhận `No started timers found`. Có timer của người khác → ghi BLOCKED, **không** tự dừng timer của người khác"* |
| CRM_LOGIN_TC_014 | 2 | 2 | 2 | 2 | 1 | 2 | 11/12 | 🟢 | Mốc biên 64 ký tự trước `@` **không có REQ** ràng buộc, mới chỉ neo tạm vào REQ-13 qua `ASM-02`. REQ-13 chỉ nói về việc trình duyệt chặn email thiếu `@` | Chạy `/update-requirements-from-ticket` để thêm REQ cho bước kiểm định dạng phía máy chủ (dùng thông báo `The Email Address field must contain a valid email address.` đã đo thật), rồi đổi cột REQ ID sang mã mới |
| CRM_LOGIN_TC_015 | 2 | 2 | 2 | 2 | 1 | 2 | 11/12 | 🟢 | Như TC_014: thông báo `…must contain a valid email address.` hiện **không có** trong mục 5 của requirements | Như TC_014 |
| CRM_LOGIN_TC_019 | 2 | 2 | 2 | 2 | 2 | 1 | 11/12 | 🟢 | Một TC gánh 4 hành vi: che ký tự · không có nút hiện/ẩn · cho dán · mật khẩu dán vào đăng nhập được. Bước 5 còn gộp nhiều thao tác (*"Nhập Email…; xoá ô Password, dán mật khẩu thật…"*). Che ký tự đã được kiểm ở TC_002 bước 4 | Bỏ bước 2 (che ký tự, trùng TC_002) hoặc bỏ nó khỏi TC_002, chỉ giữ ở một nơi. Tách bước 5 thành: *"5. Nhập Email `admin@example.com` · 6. Xoá ô Password · 7. Dán giá trị `PASSWORD_ADMIN` bằng `Ctrl+V`"* |
| CRM_LOGIN_TC_020 | 2 | 1 | 2 | 2 | 2 | 2 | 11/12 | 🟢 | Expected bước 4 *"Trang nạp lại **trong vài giây**, không treo"* không đo được. Tag `@Localization` không hợp cho ca emoji trong mật khẩu | Expected: *"Trang nạp lại trong **≤ 5 giây**"* (hoặc mốc PO chốt). Đổi tag thành `@Boundary @ErrorGuessing` |
| CRM_LOGIN_TC_021 | 2 | 1 | 2 | 2 | 2 | 2 | 11/12 | 🟢 | Hành vi cốt lõi của REQ-08 (có cookie `autologin`) **chỉ** nằm ở phần 🔧. Phần chính (tích ô → vào Dashboard) cho kết quả giống hệt TC_006, nên tester không có DevTools sẽ chấm PASS mà chưa kiểm REQ-08. Đây là PASS rỗng | Thêm vào đầu Expected: *"⚠️ Kết luận PASS/FAIL của REQ-08 nằm ở dòng 🔧. Tester không có DevTools chỉ chấm được bước 4–6, ghi `PASS một phần — chưa kiểm cookie`"*. Hoặc chuyển Auto Type sang kiểm cookie bằng automation (đây là loại việc automation làm tốt) |
| CRM_LOGIN_TC_022 | 2 | 1 | 2 | 2 | 2 | 2 | 11/12 | 🟢 | Như TC_021: bằng chứng "không có cookie" chỉ nằm ở phần 🔧. Bước 2 (ô chưa tích) trùng với TC_002 mục `3` | Như TC_021. Bỏ bước 2 |
| CRM_LOGIN_TC_044 | 2 | 2 | 1 | 2 | 2 | 2 | 11/12 | 🟢 | Pre-Condition *"theo bước 5 của `CRM_LOGIN_TC_043`"*, tức phải chạy TC khác trước. Chạy lẻ TC_044 (hoặc chạy song song) thì không có phiên cổng khách hàng | Pre-Condition tự đứng được: *"Chrome, cửa sổ ẩn danh. Mở `https://crm.anhtester.com/login`, đăng nhập bằng `EMAIL_CUSTOMER` / `PASSWORD_CUSTOMER` → dừng ở `https://crm.anhtester.com/`"* |
| CRM_LOGIN_TC_046 | 2 | 1 | 2 | 2 | 2 | 2 | 11/12 | 🟢 | Expected tự nói là chưa chắc: *"Đúng **1** dải `Invalid email or password` … ⚠️ Câu chữ … chưa đo thật"*. Tester gặp câu khác (VD `…must contain a valid email address.`) sẽ không biết chấm PASS hay FAIL | Viết tiêu chí chấm tách hai tầng: *"**Bắt buộc:** không vào Dashboard, không có dòng lỗi CSDL/trang lỗi. **Ghi nhận:** câu chữ dải báo lỗi — chép nguyên văn vào execution report để chốt `ASM-09`"* |
| CRM_LOGIN_TC_052 | 1 | 2 | 2 | 2 | 2 | 2 | 11/12 | 🟢 | Bước 2 *"Bấm nút mở menu điều hướng thu gọn trên thanh đầu trang"* không nói nút nằm ở đâu và trông thế nào. Lần chạy `run_1787215085` đã recon thật (TC cũ `TC_033` PASS) nhưng thông tin đó chưa được đưa vào TC | Lấy mô tả từ execution report cũ đưa vào bước 2, VD *"Bấm biểu tượng ☰ ở góc trên bên **<trái/phải>**"*, và chụp ảnh `logout_mobile_menu_open_375x812.png` để đóng `ASM-08` |

### TC đạt 12/12 (39 TC)

`001` · `003` · `004` · `005` · `007` · `009` · `010` · `011` · `012` · `013` · `016` · `017` · `023` · `024` · `025` · `026` · `027` · `028` · `029` · `030` · `032` · `033` · `034` · `035` · `036` · `037` · `038` · `039` · `040` · `041` · `042` · `043` · `045` · `047` · `048` · `049` · `050` · `051` · `053`

**Ghi chú nhỏ, không trừ điểm:**

| TC ID | Ghi chú | Đề xuất |
|---|---|---|
| CRM_LOGIN_TC_032 | Để yên 65 phút trên **Dashboard** — nếu trang tự gửi yêu cầu nền định kỳ (thông báo, bộ đếm) thì phiên có thể được gia hạn ngầm, và TC FAIL oan | Thêm vào bước 1: *"Chuyển tab đó sang `about:blank` rồi để yên"* — vẫn giữ cookie phiên nhưng không còn yêu cầu nền |
| CRM_LOGIN_TC_029 | Biến thể `b` (nút Back): trình duyệt có thể hiện **bản lưu tạm** của trang cũ. Nếu thấy lại danh sách khách hàng, tester khó phân biệt đó là bản lưu tạm hay phiên còn sống | Thêm Expected: *"Nếu vẫn thấy trang cũ, bấm một mục menu bất kỳ → phải về trang đăng nhập"*. Việc trang cũ hiện lại từ bản lưu tạm vẫn là phát hiện bảo mật đáng báo riêng |
| Nhiều TC (`023`, `026`, `030`, `038`…) | Một bước gộp cả thao tác đăng nhập (*"Nhập Email…, Password…, bấm `Login`"*) | Chấp nhận được, vì đây là thao tác tiền đề quen thuộc. Chỉ tách khi chính bước đó là đối tượng kiểm |

---

## Đối soát loại kiểm thử (4 vòng)

| Vòng | Nhánh | Trạng thái | Ghi chú |
|---|---|---|---|
| 1 | UI cơ bản | ✅ | TC_001–004 — nhãn nguyên văn, thứ tự, mặc định, con trỏ |
| 1 | Open form | ✅ | TC_005, TC_007 |
| 1 | Display | ✅ | TC_006 (xem đề xuất liệt kê 14 mục), TC_007 |
| 1 | Input valid data | ✅ | TC_006, TC_021 |
| 1 | Save | ✅ | TC_006 |
| 1 | Verify data | ✅ | TC_006, TC_008 |
| 2 | UI Behavior | 🟡 Nông | TC_009, 019, 021. **Thiếu:** nhấn `Enter` ngay trong ô Password để gửi biểu mẫu — thao tác phổ biến nhất của người dùng (TC_053 chỉ nhấn Enter khi đang ở nút `Login`) — Gap #6 |
| 2 | Required | 🟡 Nông | TC_009–011, 034. Email chỉ gồm khoảng trắng đã có (010-b), nhưng **Password chỉ gồm khoảng trắng thì chưa có** — Gap #1 |
| 2 | Validation | 🟡 Nông | Ô Email của trang đăng nhập đủ 8/8 mục. **Ô Email của trang Quên mật khẩu mới có 3/9 mục** (Required · Format · Không tồn tại); còn thiếu chuỗi tấn công, khoảng trắng đầu/cuối, biên độ dài — Gap #3, #7. Ô Password chưa kiểm khoảng trắng đầu/cuối — Gap #2 |
| 2 | Equivalence Partitioning | ✅ | TC_006, 012, 013 |
| 2 | Boundary Value Analysis | ✅ | TC_014, 015 (63 · 64 · 65 · 100 · 250) — đang chờ REQ chính thức (`ASM-02`) |
| 2 | Business Rule | ✅ | TC_013, 023, 024 |
| 2 | Decision Table | 🟡 Nông | 9 rule, mỗi rule có TC. **Thiếu rule ưu tiên** khi hai lỗi xảy ra cùng lúc: Email sai định dạng phía máy chủ (> 64 ký tự) **và** Password trống thì hiện dải nào — Gap #8 |
| 2 | State Transition | 🟡 Nông | Bảng 11 chuyển trạng thái đầy đủ cho **một tab**. **Thiếu trường hợp nhiều tab:** đăng xuất ở tab B, rồi thao tác tiếp ở tab A vẫn đang mở khu quản trị — Gap #5 |
| 2 | Dependency | ➖ | Không có trường phụ thuộc nhau |
| 2 | Use Case / Scenario | ✅ | TC_026, 030 |
| 2 | Save / Edit / Delete | ➖ | Module không có CRUD |
| 2 | Error Guessing | ✅ | TC_038–041 |
| 3 | Permission | 🟡 Nông · **ghi nhãn sai** | Index ghi đã phủ *"… đăng xuất cho cả 3 vai trò"*, nhưng **không** TC nào đăng xuất bằng Project Manager (TC_008, 029 đều dùng Admin) — Gap #4. Phần còn lại đạt: TC_027-b, 028-b, 042, 043, 044 |
| 3 | Security | 🟡 Nông | Trang đăng nhập phủ tốt (003, 013, 023, 025, 029, 030, 045–047, 049). **Trang Quên mật khẩu chưa có TC chuỗi tấn công nào**, dù đây là điểm tra CSDL theo email — Gap #3. **Chưa kiểm cookie phiên có đổi sau khi đăng nhập** (chống cố định phiên) — Gap #9, cần REQ trước |
| 3 | API | ➖ | QA không có quyền gọi API — đội Dev xác minh |
| 3 | Database | ➖ | Không có quyền truy vấn CSDL |
| 3 | Integration | ⏭️ · **ghi nhãn sai** | Index ghi `➖` với lý do *"gửi mail đặt lại ngoài phạm vi"*. Tích hợp gửi mail **có tồn tại**, chỉ là PO quyết định không kiểm, nên nhãn đúng phải là `⏭️`: *"Cố ý bỏ — PO quyết định 18-08-2026 (`AMB-LOGIN-04`); rà lại khi có hộp thư test đọc được qua API"* |
| 3 | Logging / Audit | ➖ | Không có yêu cầu, QA không mở được Activity Log |
| 4 | Compatibility | ✅ | TC_050 (Chrome · Edge · Firefox) |
| 4 | Responsive | ✅ | TC_051, 052 |
| 4 | Accessibility | ✅ | TC_053, TC_002 mục `5` |
| 4 | Performance | ➖ | Không có ngưỡng cam kết — đội Hạ tầng |
| 4 | Regression | ✅ | TC_015-c; bốn TC `@KnownBug` dùng làm retest |
| 4 | E2E | 🟡 · **ghi nhãn sai** | Index ghi ✅, nhưng TC duy nhất là TC_031, đang `Partial` và **chờ PO cho phép** bật timer trên môi trường dùng chung (`AMB-LOGIN-14`). Chưa có quyết định thì nhánh này thực tế **chưa chạy được**. Nên ghi 🟡 kèm điều kiện |

---

## Đối soát bảng 15 loại field

| Field | Loại | Mục đã có | Mục thiếu (đích danh) |
|---|---|---|---|
| Email Address (Đăng nhập) | Email | Đủ 8/8 mục áp dụng + khoảng trắng + chuỗi tấn công | — |
| Password (Đăng nhập) | Password | Cho dán · không có nút hiện/ẩn · che ký tự · Unicode/emoji · chuỗi dài · chuỗi tấn công | **Chỉ gồm khoảng trắng** (Gap #1) · **khoảng trắng đầu/cuối quanh mật khẩu đúng** — có bị cắt đi không (Gap #2) |
| Remember me | Checkbox | Mặc định · tích bằng chữ · tích bằng `Space` | **Bỏ tích sau khi đã tích** (tích → bỏ → đăng nhập → không có cookie) — Low, có thể gộp làm biến thể của TC_022 |
| Email Address (Quên mật khẩu) | Email | Required · Format sai (3 biến thể) · Không tồn tại · Tồn tại ⏭️ hợp lệ | **Chuỗi tấn công** (Gap #3) · **khoảng trắng đầu/cuối** · **biên > 64 ký tự trước `@`** (Gap #7) · chữ hoa/thường ➖ (cần email tồn tại → rơi vào ⏭️ của REQ-27) |

---

## Coverage Gaps (TC còn thiếu)

| # | Kịch bản thiếu | Vòng / Nhánh | REQ neo | Priority đề xuất |
|---|---|---|---|---|
| 1 | Password chỉ gồm 3 khoảng trắng, Email `admin@example.com` → kỳ vọng dải `The Password field is required.` giống TC_011 (tương ứng TC_010-b của ô Email). **Chưa đo** → gắn `@NeedsVerify` | V2 · Required | REQ-LOGIN-12 | High |
| 2 | Password đúng nhưng có khoảng trắng ở đầu/cuối (`␣` + `PASSWORD_ADMIN` + `␣`) → hệ thống có cắt khoảng trắng không? Chưa có REQ → **recon trước**, rồi chốt REQ bằng `/update-requirements-from-ticket` | V2 · Validation | (cần REQ mới) | Medium |
| 3 | Trang Quên mật khẩu: nhập chuỗi tấn công đúng định dạng email (`admin'--@example.com`, `x'union'select@example.com`) → chỉ hiện `Email not found`, không có dòng lỗi CSDL hay trang lỗi | V3 · Security | REQ-LOGIN-26 | High |
| 4 | Project Manager bấm `Logout` (không có timer) → về trang đăng nhập; sau đó mở `/admin/clients` → bị chặn. Đây là hàng "đăng xuất × PM" của ma trận phân quyền | V3 · Permission | REQ-LOGIN-31, 32, 33 | Medium |
| 5 | Mở `/admin/clients` ở tab A, đăng xuất ở tab B, quay lại tab A bấm một mục menu → về trang đăng nhập, không thao tác tiếp được | V2 · State Transition | REQ-LOGIN-33 | Medium |
| 6 | Nhập Email + Password rồi nhấn `Enter` ngay trong ô Password → biểu mẫu được gửi, vào Dashboard | V2 · UI Behavior | REQ-LOGIN-06 | Medium |
| 7 | Trang Quên mật khẩu: email có khoảng trắng đầu/cuối, và email có > 64 ký tự trước `@` (dùng email **không tồn tại** để không gửi mail thật) → ghi nhận thông báo | V2 · Validation | REQ-LOGIN-26 | Low |
| 8 | Email 65 ký tự trước `@` **và** Password trống → hiện một hay hai dải báo lỗi, theo thứ tự nào (quy tắc ưu tiên của bảng quyết định) | V2 · Decision Table | REQ-LOGIN-12, 13 | Low |
| 9 | Cookie phiên **đổi giá trị** sau khi đăng nhập thành công (chống cố định phiên) — `@TechCheck`. Chưa có REQ → đề xuất thêm REQ trước, **không** viết TC mồ côi | V3 · Security | (cần REQ mới) | Medium |

---

## TC trùng lặp — đề xuất gọn lại

Không có cặp TC nào trùng **toàn bộ**, nên không cần `@Deprecated`. Có 3 chỗ trùng **một phần**, nên gọn lại để không phải chấm cùng một thứ hai lần:

| Cặp | Phần trùng | Đề xuất |
|---|---|---|
| TC_003 bước 3–5 ≈ TC_023 bước 3 | Cả hai kiểm *"sau nhiều lần sai không hiện CAPTCHA"* | Bỏ bước 3–5 khỏi TC_003, chỉ giữ phần quan sát tĩnh (bước 1–2). TC_023 đã kiểm *"không có … CAPTCHA"* sau 6 lần sai với tài khoản thật. Nếu muốn giữ ca email **không tồn tại**, thêm biến thể vào TC_023 |
| TC_002 bước 3–4 ≈ TC_053 bước 2 · TC_019 bước 2 | Con trỏ ở ô Email · che ký tự | Xem đề xuất ở dòng TC_002 và TC_019 |
| TC_022 bước 2 ≈ TC_002 mục `3` | Ô `Remember me` chưa tích mặc định | Bỏ bước 2 của TC_022 |

---

## Đối chiếu kết quả chạy & tính toàn vẹn của index

| # | Vấn đề | Căn cứ | Đề xuất |
|---|---|---|---|
| 1 | 🔴 **Evidence và bug mà index trỏ tới đã bị xoá khỏi ổ đĩa.** `git status` báo `D` cho toàn bộ `docs2/docs/executions/login/web/run_*` (2 execution report + ảnh) và `docs2/docs/bugs/login/web/BUG_*` (6 bug). Index dẫn chứng các thư mục này cho TC_014, 015, 019, 020, 031, 050, 051 và cho bảng *Ánh xạ TC ID cũ → mới* | Các file vẫn còn ở `HEAD` (đã đọc lại bằng `git show`) nhưng không còn trong working tree | Nếu việc xoá là **ngoài ý muốn**, bạn khôi phục lại (agent không tự chạy lệnh git thay đổi trạng thái theo CLAUDE.md). Nếu **cố ý** bỏ, thì phải sửa index: các dòng evidence đó chuyển thành `⚠️ chưa có evidence`, và bảng ánh xạ bug ghi rõ bug đã chuyển đi đâu |
| 2 | Ghi chú `@NeedsVerify` của TC_052 và TC_037 **một nửa đã cũ**: `run_1787215085` đã chạy PASS và xác nhận hành vi (TC cũ `TC_033` ghi *"Giải quyết `@NeedsVerify` — đã recon thật"*), chỉ còn thiếu ảnh | Execution report `run_1787215085` dòng 75 | Giữ tag tới khi có ảnh, nhưng sửa ghi chú thành *"hành vi đã xác nhận ở `run_1787215085`, chỉ thiếu ảnh"*. Đồng thời **REQ-LOGIN-29** ở requirements vẫn ghi nhánh mobile *"⚠️ chưa recon"* — ghi chú đó đã cũ, cần cập nhật |
| 3 | Viewport chuẩn ghi `1600×750` (index, part 01, TC_007, TC_051-b), trong khi CLAUDE.md hiện chốt headed là **`1600×770`** | CLAUDE.md mục Browser Rules | Thống nhất một con số. Nếu `1600×750` là mốc khảo sát cũ, ghi rõ ở index |
| 4 | Bug `BUG_login_1787226517_TC029` (ô Email không tự xoá) vẫn **chưa có REQ và chưa có TC**, đang chờ PO | Index mục *Ánh xạ TC ID cũ → mới* | Đưa vào danh sách câu hỏi cho PO. Nếu PO bỏ thì đóng bug với lý do *không phải lỗi* |
| 5 | Số liệu index: 53 TC · 101 biến thể · 47 Yes / 6 Partial | Đã đếm lại từng part | ✅ Khớp |

---

## Kết luận & Khuyến nghị

1. **Sửa TC_018 và `ASM-05` trước tiên** — thay mật khẩu viết thẳng trong tài liệu bằng biến `.env`. Báo QA lead **không** dùng mật khẩu dự kiến cũ làm mật khẩu thật.
2. **Xử lý các file evidence/bug bị xoá** (mục Đối chiếu #1): khôi phục lại, hoặc sửa index cho khớp. Hiện 7 TC đang dẫn chứng tới file không còn trên ổ đĩa.
3. **Bổ sung 3 TC ưu tiên High/Medium không cần REQ mới:** Gap #1 (Password chỉ khoảng trắng), #3 (chuỗi tấn công ở Quên mật khẩu), #4 (PM đăng xuất). Nối tiếp từ `CRM_LOGIN_TC_054`.
4. **Sửa 3 nhãn sai ở bảng 4 vòng của index:** Permission (đang ghi đã phủ PM đăng xuất), Integration (`➖` → `⏭️`), E2E (✅ → 🟡 chờ `AMB-LOGIN-14`).
5. **Chốt REQ còn thiếu** bằng `/update-requirements-from-ticket`: kiểm định dạng email phía máy chủ (`ASM-02`, gỡ neo tạm của TC_014/015), cách xử lý khoảng trắng của Password (Gap #2), chống cố định phiên (Gap #9).

> Muốn agent sửa luôn các TC ở trên và bổ sung TC cho gap thì chạy `/review-testcases FIX docs2\docs\testcases\login\web`. Bộ TC đang sạch trên git nên sửa tại chỗ được ngay.

---

## Kết quả Mode FIX — 23-09-2026

- **Mốc git trước khi sửa:** `82a814d` (index + 2 part)
- **Sửa tại chỗ 14 TC:** `002`, `003`, `006`, `008`, `018`, `019`, `020`, `021`, `022`, `023` (thêm neo REQ-05), `031`, `044`, `046`, `052` (chỉ ghi chú — không tài liệu nào ghi vị trí nút mở menu, **không** đoán)
- **Thêm 7 TC:** `054` (gap #1) · `055` (#3) · `056` (#4) · `057` (#5) · `058` (#6) · `059` (#7) · `060` (#8). Trong đó 4 TC `@NeedsVerify`: `054`, `055`, `059`, `060`
- **Chưa làm:** gap #2 và #9, chờ chốt REQ. Không khôi phục các file evidence/bug bị xoá (chỉ đánh dấu trong index). Chưa thống nhất viewport `1600×750` với `1600×770`
- **Index:** 60 TC · 112 biến thể · nhãn Permission / Integration / E2E đã sửa · `ASM-10`…`ASM-13` · rule `R10` · 1 dòng Nhật ký
- 🔒 Báo cáo này đã **xoá** chuỗi mật khẩu dự kiến từng trích ở bản đầu
