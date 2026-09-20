# Requirements — Authentication (Đăng nhập) · `LOGIN`

> ← [Danh mục](../README.md) · [Bản đồ hệ thống](../_discovery/system_map.md) · [Bản đồ khám phá module](../_discovery/modules/module_01_dang_nhap.md)

| Thuộc tính | Giá trị |
|---|---|
| **Hệ thống** | Perfex CRM — bản demo Anh Tester (khu vực quản trị `/admin/`) |
| **Module** | Authentication — Login · Forgot Password · Logout |
| **Prefix** | `LOGIN` (cấp bởi `/discover-system` 2026-09-14) |
| **Route** | `/admin/authentication` · `/admin/authentication/forgot_password` · `/admin/authentication/logout` |
| **Ngày khảo sát** | 2026-09-14 |
| **Cập nhật gần nhất** | 2026-09-18 · `PO-AMB-20260918` — PO chốt AMB-06 → AMB-18 ([Impact Report](impact/impact_PO-AMB-20260918.md)) |
| **Nhánh** | UI Recon (không có tài liệu) + quyết định PO (delta) |
| **Tài khoản** | 1 tài khoản (`EMAIL_ADMIN` trong `.env`) — staff, **không** phải admin (`app.user_is_admin` rỗng). Credential do **người dùng tự nhập** ở bước đăng nhập thành công |
| **Môi trường dùng chung** | ✅ Có — không thử sai mật khẩu nhiều lần với tài khoản thật (đúng 1 lần, REQ-LOGIN-10); không gửi Forgot Password với email thật |
| **Trình duyệt khảo sát** | Google Chrome `152.0.0.0` (Playwright MCP), `navigator.language = en-US`, viewport `1600×750`. Mọi AC dựa trên thông báo mặc định của trình duyệt **chỉ đúng với trình duyệt này** |
| **Tổng REQ** | 37 (🟢 32 · 🟡 1 · 🔴 0 · ⚪ 4) · 4 Story |
| **Dải mã đã dùng** | `REQ-LOGIN-01` → `REQ-LOGIN-37` (đợt 1: UI recon 01→35 · đợt 2: `PO-AMB-20260918` 36→37) · `AMB-06` → `AMB-19` (đánh số **toàn hệ thống**) · `RISK-01` → `RISK-06` (đánh số trong module) |
| **Mã kế tiếp** | Đợt phân tích sau bắt đầu từ `REQ-LOGIN-38` · `AMB-20` (tra `../README.md` mục 3 trước khi cấp) · `RISK-07` — **KHÔNG đánh lại từ 01** |

## 1. Tổng quan

Module Authentication là cửa ngõ vào khu vực quản trị: trang **Login** (email + mật khẩu + ghi nhớ), trang **Forgot Password** (yêu cầu đặt lại mật khẩu qua email), và **Logout** từ menu hồ sơ ở thanh đầu trang. Mọi route `/admin/*` đều chặn người chưa đăng nhập về trang Login.

**Trong phạm vi:** giao diện và validation của Login / Forgot Password · luồng đăng nhập thành công · cookie phiên · chuyển hướng chặn truy cập · đăng xuất (kể cả khi có timer công việc đang chạy).

**Ngoài phạm vi:** đăng nhập cổng khách hàng (`/authentication` phía client) · Two Factor Authentication (cấu hình ở Edit Profile — thuộc `PROFILE`) · đổi mật khẩu khi đã đăng nhập (`PROFILE`) · cấu hình bảo mật trong Setup (BLOCKED — AMB-01) · chọn ngôn ngữ trong menu hồ sơ (`PROFILE`) · giao diện viewport mobile (AMB-16 ⏭️ — recon ở đợt riêng).

## 2. Bản đồ phủ tài liệu

Không có tài liệu — toàn bộ REQ sinh từ khảo sát UI thực tế (DOM · network thụ động · ảnh chụp). Đợt 2 (2026-09-18) bổ sung REQ từ **quyết định PO** trả lời AMB — cột `Nguồn` ghi `Quyết định PO · AMB-XX`.

## 3. Yêu cầu chức năng

> Cột `Nguồn`: `Kiểm chứng thực tế` = đã tương tác và xác nhận · `UI thực tế` = chỉ đọc DOM/quan sát · `Chưa kiểm chứng` = suy luận, có AMB đi kèm · `Quyết định PO` = hành vi do PO chốt, chưa kiểm trên UI.
> Mã HTTP ghi trong AC là **số liệu quan sát**, **không** phải điều kiện assert — PO chốt 2026-09-18 (AMB-08 ✅, AMB-09 ✅): không kiểm mã trạng thái trả về. AC chỉ assert URL cuối, nội dung hiển thị, việc có/không phát sinh request.

### STORY-LOGIN-01 — Form đăng nhập & validation

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-LOGIN-01 | Trang Login hiển thị form đăng nhập | Là người dùng chưa đăng nhập, tôi thấy form để đăng nhập vào khu vực quản trị | Mở `/admin/authentication` khi chưa đăng nhập → có đúng 1 `<form method="post">` với `action` kết thúc bằng `/admin/authentication`; bên trong có `input#email[type=email]` (nhãn "Email Address"), `input#password[type=password]` (nhãn "Password"), `input#remember[type=checkbox]` (nhãn "Remember me"), `button[type=submit]` chữ "Login"; tiêu đề `H1` = "Login". Ở viewport 1600×750 cả 4 phần tử tương tác đều có `offsetParent ≠ null` và kích thước > 0 | 🟢 | — | Kiểm chứng thực tế · DOM · `login_form_default_viewport.png` |
| REQ-LOGIN-02 | Ô Email được focus sẵn khi mở trang Login | Người dùng gõ email ngay không cần bấm vào ô | `#email` có thuộc tính `autofocus`; ngay sau khi trang tải xong `document.activeElement` là `#email` | 🟢 | — | Kiểm chứng thực tế · DOM · `login_form_default_viewport.png` (viền focus) |
| REQ-LOGIN-03 | Tiêu đề tab trang Login chứa "Login" | Người dùng nhận biết tab đăng nhập | `document.title` **chứa** `Login`. Giá trị đầy đủ quan sát: `Perfex CRM \| Anh Tester Demo - Login` — phần tên công ty là cấu hình hệ thống, có thể khác giữa môi trường → **cấm** assert khớp tuyệt đối | 🟢 | — | UI thực tế · DOM |
| REQ-LOGIN-04 | Logo trang Login liên kết về trang chủ site | Bấm logo quay về website | Logo (`img` alt `Perfex CRM \| Anh Tester Demo`) nằm trong `<a>` có `href` là gốc domain (`/`). Chưa bấm thử | 🟢 | — | UI thực tế · DOM |
| REQ-LOGIN-05 | Bắt buộc nhập Email Address — kiểm ở máy chủ | Không cho đăng nhập khi thiếu email | Email trống, Password nhập giá trị giả → bấm Login → trình duyệt **không** chặn (`#email` không có thuộc tính `required`), POST `/admin/authentication` được gửi (quan sát `200`, không chuyển hướng) → hiển thị đúng 1 `.alert.alert-danger` nguyên văn **"The Email Address field is required."** | 🟢 | — | Kiểm chứng thực tế · network · `login_submit_password_only_error_viewport.png` |
| REQ-LOGIN-06 | Bắt buộc nhập Password — kiểm ở máy chủ | Không cho đăng nhập khi thiếu mật khẩu | Email hợp lệ (giả), Password trống → bấm Login → POST được gửi (quan sát `200`) → hiển thị đúng 1 `.alert.alert-danger` nguyên văn **"The Password field is required."** | 🟢 | — | Kiểm chứng thực tế · network · `login_submit_email_only_error_viewport.png` |
| REQ-LOGIN-07 | Để trống cả hai trường hiển thị cả hai thông báo bắt buộc | Người dùng thấy đủ lỗi trong một lần gửi | Email và Password đều trống → bấm Login → có đúng 2 `.alert.alert-danger`: "The Password field is required." và "The Email Address field is required.", mỗi câu 1 lần. Thứ tự DOM quan sát: Password trước Email — **không** assert thứ tự | 🟢 | — | Kiểm chứng thực tế · `login_submit_empty_error_viewport.png` |
| REQ-LOGIN-08 | Trình duyệt chặn gửi form Login khi Email sai định dạng | Lỗi định dạng được bắt trước khi gửi máy chủ | Nhập Email là chuỗi không có `@` + Password giả → bấm Login → `#email.checkValidity() === false`, `validity.typeMismatch === true`, và **không** phát sinh POST `/admin/authentication`. Tooltip Chrome 152 quan sát: *"Please include an '@' in the email address. '<giá trị>' is missing an '@'."* — chuỗi do trình duyệt sinh, **cấm dùng làm assertion** | 🟢 | — | Kiểm chứng thực tế · DOM + network |
| REQ-LOGIN-09 | Sai thông tin đăng nhập hiển thị thông báo chung | Không đăng nhập được với email không tồn tại | Email đúng định dạng nhưng không tồn tại + Password giả → bấm Login → POST (quan sát `303`, `Location` = `/admin/authentication`) → URL cuối `/admin/authentication`, hiển thị 1 `.alert.alert-danger` nguyên văn **"Invalid email or password"** | 🟢 | — | Kiểm chứng thực tế · network · `login_submit_invalid_credentials_viewport.png` |
| REQ-LOGIN-10 | Form Login không phân biệt email tồn tại hay không | Chống dò tìm tài khoản qua form đăng nhập | Email của tài khoản test (`EMAIL_ADMIN`) + mật khẩu **sai** → thông báo nguyên văn và luồng chuyển hướng **giống hệt** REQ-LOGIN-09. Chỉ thực hiện **1 lần** mỗi lượt chạy (RISK-01) | 🟢 | — | Kiểm chứng thực tế · DOM + network (1 lần) |
| REQ-LOGIN-11 | Thông báo sai thông tin biến mất khi tải lại trang | Thông báo lỗi chỉ hiện một lần (flash) | Sau khi thấy alert của REQ-LOGIN-09 → tải lại `/admin/authentication` → không còn phần tử `.alert` nào | 🟢 | — | Kiểm chứng thực tế · DOM |
| REQ-LOGIN-12 | Máy chủ không trả lại giá trị Email sau khi đăng nhập lỗi | Người dùng phải nhập lại email sau mọi lần lỗi | Sau REQ-LOGIN-05 / 06 / 09: `#email` **không có** thuộc tính `value` trong HTML trả về. **Cấm** assert "ô Email rỗng trên màn hình" — trình duyệt có thể tự điền (RISK-03). Quan sát ở profile Playwright sạch: ô rỗng | 🟢 | — | Kiểm chứng thực tế · DOM |
| REQ-LOGIN-13 | Trạng thái Remember me không được giữ lại sau khi đăng nhập lỗi | Người dùng phải tick lại sau lần lỗi | Tick Remember me + thông tin giả → bấm Login → sau khi quay lại trang, `#remember.checked === false` | 🟢 | — | Kiểm chứng thực tế · DOM |
| REQ-LOGIN-14 | Tick Remember me gửi trường `remember` lên máy chủ | Lựa chọn ghi nhớ được truyền đi | Tick Remember me → bấm Login → request body POST **có khoá** `remember`. Giá trị quan sát là `estimate` (thuộc tính `value` của checkbox) — **không** assert giá trị: PO chốt máy chủ chỉ kiểm sự tồn tại của trường (AMB-07 ✅) | 🟡 | 2026-09-18 · PO-AMB-20260918 | Kiểm chứng thực tế · network request body · Quyết định PO · AMB-07 |
| REQ-LOGIN-15 | Không tick Remember me thì không gửi trường `remember` | Mặc định không ghi nhớ | Không tick → bấm Login → request body chỉ gồm `csrf_token_name`, `email`, `password`; **không** có khoá `remember` | 🟢 | — | Kiểm chứng thực tế · network request body |
| REQ-LOGIN-16 | Nhấn Enter trong ô nhập gửi form Login | Gửi form bằng bàn phím | Focus ở `#email` (hoặc `#password`), nhấn Enter → phát sinh POST `/admin/authentication` mà không cần bấm nút Login | 🟢 | — | Kiểm chứng thực tế · network (2 lần: từ `#email`, từ `#password`) |
| REQ-LOGIN-17 | Form Login gửi kèm CSRF token | Chống giả mạo request | Form có `input[type=hidden][name=csrf_token_name]` hình thái `<32 ký tự hex>`; mọi POST `/admin/authentication` quan sát được đều chứa khoá `csrf_token_name`. Không chép giá trị token. Không yêu cầu token đổi sau khi đăng xuất (AMB-17 ✅) | 🟢 | — | Kiểm chứng thực tế · DOM + network |
| REQ-LOGIN-36 | Đăng nhập sai liên tiếp không khoá tài khoản | Người dùng nhập sai nhiều lần vẫn đăng nhập được khi nhập đúng | **Chỉ chạy trên tài khoản riêng**, tuyệt đối không dùng tài khoản chung (RISK-01). Nhập đúng email + mật khẩu **sai** liên tiếp N lần (N chưa chốt — AMB-19, tạm dùng 5) → mỗi lần đều hiện "Invalid email or password", **không** xuất hiện CAPTCHA hay thông báo khoá → lần N+1 nhập **đúng** mật khẩu → vào `/admin/`, `document.title` chứa `Dashboard` | 🟢 | 2026-09-18 · PO-AMB-20260918 | Quyết định PO · AMB-13 ✅ · **chưa kiểm chứng trên UI** |

### STORY-LOGIN-02 — Đăng nhập thành công, ghi nhớ & chặn truy cập

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-LOGIN-18 | Đăng nhập thành công chuyển vào Dashboard | Là staff, tôi vào được khu vực quản trị bằng email + mật khẩu đúng | Nhập đúng credential của tài khoản test → bấm Login → POST (quan sát `303`, `Location` = `/admin/`) → URL cuối `/admin/`, `document.title` chứa `Dashboard`, ảnh hồ sơ `.header-user-profile > a` hiển thị. Với tài khoản này **không** xuất hiện bước xác thực thứ hai | 🟢 | — | Kiểm chứng thực tế · network (credential do người dùng tự nhập) |
| REQ-LOGIN-19 | Remember me tạo cookie ghi nhớ đăng nhập | Tick Remember me thì hệ thống lưu dấu ghi nhớ dài hạn | **PO chốt (AMB-06 ✅): hiện tại Remember me không tạo cookie ghi nhớ** — giữ ⚪ tới khi kiểm bằng phép thử sạch trên tài khoản riêng. AC phép thử sạch: (1) xoá toàn bộ cookie domain → (2) xác nhận không còn cookie → (3) đăng nhập đúng **có** tick → (4) kiểm có cookie mới ngoài `csrf_cookie_name` / `sp_session`, có hạn dài hơn phiên. Quan sát 2026-09-14 (không xoá cookie trước, người dùng báo đã tick): chỉ có `csrf_cookie_name` (`<32 ký tự hex>`, HttpOnly, Secure, SameSite=Lax) và `sp_session` (`<40 ký tự hex>`, HttpOnly, Secure, SameSite=Lax, hạn < 1 ngày) | ⚪ | — | Chưa kiểm chứng · `context.cookies()` (chỉ tên + cờ) · Quyết định PO · AMB-06 |
| REQ-LOGIN-20 | Cookie ghi nhớ tự đăng nhập lại khi phiên kết thúc | Người dùng quay lại không phải nhập lại mật khẩu | **Giữ ⚪ theo AMB-06 ✅** — chỉ kiểm sau khi REQ-19 có kết quả phép thử sạch. Đăng nhập có tick → xoá riêng cookie phiên `sp_session` (giữ cookie ghi nhớ) → mở `/admin/` → vào thẳng Dashboard, không qua trang Login | ⚪ | — | Chưa kiểm chứng · Quyết định PO · AMB-06 |
| REQ-LOGIN-21 | Người đã đăng nhập mở trang Login bị chuyển về Dashboard | Không hiện form đăng nhập khi đã có phiên | Đang đăng nhập → mở `/admin/authentication` → URL cuối `/admin/`, không hiện form Login. Mã quan sát `307` — không assert (AMB-09 ✅) | 🟢 | — | Kiểm chứng thực tế · network |
| REQ-LOGIN-22 | Người đã đăng nhập mở trang Forgot Password bị chuyển về Dashboard | Không yêu cầu đặt lại mật khẩu khi đã có phiên | Đang đăng nhập → mở `/admin/authentication/forgot_password` → URL cuối `/admin/`, `document.title` chứa `Dashboard` | 🟢 | — | Kiểm chứng thực tế · điều hướng |
| REQ-LOGIN-23 | Người chưa đăng nhập mở route quản trị bị chuyển về trang Login | Chặn truy cập trái phép | Sau khi đăng xuất → mở `/admin/clients` (route chỉ đọc) → URL cuối `/admin/authentication`, form Login hiển thị. Mã quan sát `307` — không assert (AMB-09 ✅) | 🟢 | — | Kiểm chứng thực tế · network |

### STORY-LOGIN-03 — Quên mật khẩu

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-LOGIN-24 | Link "Forgot Password?" mở trang Quên mật khẩu | Người quên mật khẩu tìm được lối khôi phục | Trên trang Login bấm link "Forgot Password?" (`href` kết thúc `/admin/authentication/forgot_password`) → URL cuối `/admin/authentication/forgot_password`, `H1` = "Forgot Password" | 🟢 | — | Kiểm chứng thực tế · `forgot_password_form_default_viewport.png` |
| REQ-LOGIN-25 | Trang Forgot Password hiển thị form yêu cầu đặt lại mật khẩu | Nhập email để nhận hướng dẫn đặt lại | Có đúng 1 `<form method="post">` với `action` kết thúc `/admin/authentication/forgot_password`; gồm `input#email[type=email]` (nhãn "Email Address", **không** `required`, **không** `autofocus`), `button[type=submit]` chữ "Confirm", hidden `csrf_token_name` `<32 ký tự hex>`. Link duy nhất trên trang là logo → gốc domain. **Không** assert `document.title` của trang này (AMB-14 ✅) | 🟢 | — | Kiểm chứng thực tế · DOM · `forgot_password_form_default_viewport.png` |
| REQ-LOGIN-26 | Để trống Email ở Forgot Password hiển thị "Email not found" | Không gửi yêu cầu khi thiếu email | Email trống → bấm Confirm → POST `/admin/authentication/forgot_password` được gửi (quan sát `200`) → 1 `.alert.alert-danger` nguyên văn **"Email not found"**. PO chốt đây là hành vi đúng (AMB-11 ✅) | 🟢 | — | Kiểm chứng thực tế · network · `forgot_password_submit_empty_error_viewport.png` |
| REQ-LOGIN-27 | Email không tồn tại ở Forgot Password hiển thị "Email not found" | Báo cho người dùng email không có trong hệ thống | Email đúng định dạng, **không tồn tại** (dữ liệu giả) → Enter → POST (quan sát `200`) → 1 `.alert.alert-danger` nguyên văn **"Email not found"**. ⚠️ Hành vi này bị ghi nhận là **bug tiềm ẩn** — lộ thông tin email có tồn tại (AMB-10 ✅ · RISK-06) | 🟢 | — | Kiểm chứng thực tế · DOM + network |
| REQ-LOGIN-28 | Trình duyệt chặn gửi Forgot Password khi Email sai định dạng | Lỗi định dạng bắt trước khi gửi | Nhập chuỗi không có `@` → `#email.checkValidity() === false` (`typeMismatch`) → nhấn Enter **không** phát sinh POST `/admin/authentication/forgot_password`. Tooltip trình duyệt — **cấm assert** | 🟢 | — | Kiểm chứng thực tế · DOM + network |
| REQ-LOGIN-29 | Email tồn tại nhận được email đặt lại mật khẩu | Người dùng nhận hướng dẫn khôi phục qua hộp thư | **Chưa kiểm chứng — PO chốt (AMB-12 ✅): TC viết trước, gắn `skip` tới khi có hộp thư test.** Môi trường dùng chung, cấm gửi yêu cầu với email thật. Khi có hộp thư test: gửi email tồn tại → thông báo thành công hiển thị + email tới hộp thư | ⚪ | — | Chưa kiểm chứng · Quyết định PO · AMB-12 |
| REQ-LOGIN-30 | Liên kết đặt lại mật khẩu dùng được để đặt mật khẩu mới | Giá trị của email khôi phục nằm ở liên kết dùng được | **Chưa kiểm chứng — TC gắn `skip` (AMB-12 ✅).** Mở liên kết trong email → đặt mật khẩu mới → đăng nhập được bằng mật khẩu mới; mật khẩu cũ bị từ chối | ⚪ | — | Chưa kiểm chứng · Quyết định PO · AMB-12 |

### STORY-LOGIN-04 — Đăng xuất

| REQ ID | Tên yêu cầu | Mô tả | Acceptance Criteria | Trạng thái | Cập nhật lần cuối | Nguồn |
|---|---|---|---|---|---|---|
| REQ-LOGIN-31 | Menu hồ sơ có mục Logout ở vị trí cuối | Người dùng tìm thấy lối đăng xuất | Bấm ảnh hồ sơ `.header-user-profile > a` → `.header-user-profile` có class `open`; `.header-user-profile > ul.dropdown-menu` có **5** `<li>` con trực tiếp theo thứ tự: My Profile · My Timesheets · Edit Profile · Language · Logout; `> li:last-child` là `li.header-logout`. ⚠️ Submenu Language lồng thêm **27** `<li>` → locator bắt buộc dùng dấu `>`. Viewport 1600×750: link Logout render `160×32` | 🟢 | — | Kiểm chứng thực tế · DOM · `login_logout_menu_open_clip.png` |
| REQ-LOGIN-32 | Lối Logout của thanh điều hướng mobile bị ẩn ở viewport desktop | Người dùng desktop chỉ có một lối đăng xuất | DOM có **2** phần tử `li.header-logout`; ở viewport 1600×750 phần tử thứ hai có `offsetParent === null`, kích thước `0×0`, tổ tiên ẩn là `#mobile-collapse` (responsive). Kết luận chỉ đúng với viewport này — viewport mobile để recon ở đợt riêng (AMB-16 ⏭️) | 🟢 | — | UI thực tế · DOM (`offsetParent` + `getBoundingClientRect` + duyệt tổ tiên) |
| REQ-LOGIN-33 | Đăng xuất khi có timer công việc đang chạy hiển thị cảnh báo | Người dùng được nhắc trước khi rời đi với timer còn chạy | Tiền điều kiện: có ≥ 1 `.started-timers-top li.timer`. Bấm Logout trong menu hồ sơ → URL **vẫn** `/admin/`; popup hiển thị nguyên văn **"Started tasks timers found!"** / **"Are you sure you want to logout without stopping the timers?"** và đúng 1 nút `a.btn.btn-danger` chữ "Logout" có `href` kết thúc `/admin/authentication/logout` | 🟢 | — | Kiểm chứng thực tế · DOM · `login_logout_timer_warning_viewport.png` |
| REQ-LOGIN-34 | Xác nhận Logout trong cảnh báo timer đăng xuất người dùng | Người dùng vẫn đăng xuất được dù có timer | Tại popup REQ-LOGIN-33 bấm "Logout" → GET `/admin/authentication/logout` (quan sát `307`) → URL cuối `/admin/authentication`, form Login hiển thị. Popup **không** có lựa chọn dừng timer | 🟢 | — | Kiểm chứng thực tế · network |
| REQ-LOGIN-35 | Đăng xuất khi không có timer chuyển thẳng về trang Login | Không hiện cảnh báo khi không có timer | **Chưa kiểm chứng hành vi** — tài khoản chung đang có timer chạy. PO chốt hành vi đúng như mã JS `logout()` (AMB-15 ✅): không có `.started-timers-top li.timer` → `window.location.href = admin_url + "authentication/logout"`. AC: không có timer → bấm Logout → không có popup, URL cuối `/admin/authentication` | 🟢 | 2026-09-18 · PO-AMB-20260918 (✏️ nguồn) | Chưa kiểm chứng · mã JS `logout()` · Quyết định PO · AMB-15 |
| REQ-LOGIN-37 | Timer công việc tiếp tục chạy sau khi đăng xuất qua cảnh báo | Đăng xuất không dừng timer người dùng đã bật | **Chỉ chạy trên tài khoản riêng** với task do chính TC tạo (môi trường dùng chung). Bật timer cho task → Logout → xác nhận "Logout" trong popup (REQ-34) → đăng nhập lại → `.started-timers-top` vẫn có `li.timer` của task đó | 🟢 | 2026-09-18 · PO-AMB-20260918 | Quyết định PO · AMB-15 ✅ · **chưa kiểm chứng trên UI** |

## 4. Đặc tả trường dữ liệu

### 4.1. Trang Login — `POST /admin/authentication`

| Field (Label) | Loại UI | Required | Ràng buộc (min/max/format/default) | REQ liên quan | Ghi chú |
|---|---|---|---|---|---|
| Email Address | `input#email` `type=email` `name=email` | ✅ Máy chủ (không có thuộc tính `required`) | Không `maxlength` / `minlength` / `pattern` / `placeholder`; `autofocus`; định dạng kiểm bởi trình duyệt khi không rỗng; mặc định rỗng | 01, 02, 05, 08, 10, 12 | Không được máy chủ trả lại sau lỗi |
| Password | `input#password` `type=password` `name=password` | ✅ Máy chủ | Không `maxlength` / `minlength`; không có nút hiện mật khẩu | 01, 06, 36 | Sai nhiều lần không khoá tài khoản (AMB-13 ✅) |
| Remember me | `input#remember` `type=checkbox` `name=remember` | ❌ | `value="estimate"` — máy chủ chỉ kiểm **sự tồn tại** của trường (AMB-07 ✅); mặc định không tick; không giữ trạng thái sau lỗi | 13, 14, 15, 19, 20 | Hiện không tạo cookie ghi nhớ (AMB-06 ✅) |
| Login | `button[type=submit]` `.btn.btn-primary.btn-block` | — | Enter trong ô nhập cũng gửi form | 01, 16 | — |
| Forgot Password? | `a` → `/admin/authentication/forgot_password` | — | — | 24 | — |
| Logo | `a` → gốc domain, `img` alt `Perfex CRM \| Anh Tester Demo` | — | — | 04 | — |
| _(ẩn)_ `csrf_token_name` | `input[type=hidden]` | — | `<32 ký tự hex>`; không đổi sau khi đăng xuất trong cùng phiên trình duyệt — không yêu cầu xoay vòng (AMB-17 ✅) | 17 | — |

**Ánh xạ payload:** `csrf_token_name` · `email` · `password` · `remember` (chỉ khi tick). Form không bật `novalidate`. Trang không có CAPTCHA (`.g-recaptcha` / iframe / script recaptcha đều không tồn tại).

### 4.2. Trang Forgot Password — `POST /admin/authentication/forgot_password`

| Field (Label) | Loại UI | Required | Ràng buộc | REQ liên quan | Ghi chú |
|---|---|---|---|---|---|
| Email Address | `input#email` `type=email` `name=email` | ❌ Không có kiểm tra bắt buộc riêng — email rỗng được xử lý như email không tồn tại, trả "Email not found" (AMB-11 ✅) | Không `required` / `autofocus` / `maxlength` | 25, 26, 27, 28 | — |
| Confirm | `button[type=submit]` | — | — | 25 | — |
| _(ẩn)_ `csrf_token_name` | `input[type=hidden]` | — | `<32 ký tự hex>` | 25 | — |

### 4.3. Cookie sau khi đăng nhập (chỉ tên + cờ — không ghi giá trị)

| Cookie | Hình thái | HttpOnly | Secure | SameSite | Hạn | REQ |
|---|---|---|---|---|---|---|
| `csrf_cookie_name` | `<32 ký tự hex>` | ✅ | ✅ | Lax | Có hạn, < 1 ngày | 17 |
| `sp_session` | `<40 ký tự hex>` | ✅ | ✅ | Lax | Có hạn, < 1 ngày | 18 |

## 5. Business Rules & Validation Messages

| REQ ID | Rule / Trigger | Thông báo lỗi mong đợi (nguyên văn) |
|---|---|---|
| REQ-LOGIN-05 | Login — Email trống | `The Email Address field is required.` |
| REQ-LOGIN-06 | Login — Password trống | `The Password field is required.` |
| REQ-LOGIN-07 | Login — cả hai trống | Hai thông báo trên, mỗi câu 1 lần |
| REQ-LOGIN-08 | Login — Email thiếu `@` | _(tooltip Chrome 152, en-US — cấm assert)_ `Please include an '@' in the email address. '<giá trị>' is missing an '@'.` |
| REQ-LOGIN-09 · 10 | Login — sai email hoặc mật khẩu | `Invalid email or password` |
| REQ-LOGIN-36 | Login — sai mật khẩu liên tiếp (tài khoản riêng) | `Invalid email or password` ở mọi lần; không có thông báo khoá |
| REQ-LOGIN-26 | Forgot Password — Email trống | `Email not found` |
| REQ-LOGIN-27 | Forgot Password — Email không tồn tại | `Email not found` |
| REQ-LOGIN-28 | Forgot Password — Email thiếu `@` | _(tooltip trình duyệt — cấm assert)_ |
| REQ-LOGIN-33 | Logout khi có timer đang chạy | `Started tasks timers found!` · `Are you sure you want to logout without stopping the timers?` · nút `Logout` |

Mọi thông báo lỗi của ứng dụng hiển thị dạng `.alert.alert-danger` phía trên form (không hiển thị inline dưới từng ô).

## 6. Ma trận Phân quyền

| Hành động | Khách (chưa đăng nhập) | Tài khoản hiện tại (staff, không admin) | Admin | Role khác |
|---|---|---|---|---|
| Mở trang Login | ✅ | ❌ chuyển về Dashboard (REQ-21) | ❔ | ❔ |
| Đăng nhập thành công | — | ✅ (REQ-18) | ❔ | ❔ |
| Mở trang Forgot Password | ✅ | ❌ chuyển về Dashboard (REQ-22) | ❔ | ❔ |
| Vào route quản trị | ❌ chuyển về Login (REQ-23) | ✅ | ❔ | ❔ |
| Đăng xuất | — | ✅ (REQ-34) | ❔ | ❔ |

```
Tổng 20 ô = Đã kiểm chứng 8 · Suy diễn 0 · Chưa rõ 10 · Không áp dụng 2
Ô "không áp dụng": [Đăng nhập thành công × Khách] và [Đăng xuất × Khách] — khách chưa có phiên; đăng nhập thành công thì không còn là khách.
Admin chưa có account (AMB-01) · danh sách role chưa biết (AMB-02) — hai AMB cấp hệ thống, xem ../README.md mục 3.
```

## 7. Ma trận Trạng thái

Không áp dụng — module không có entity mang trạng thái. (Phiên đăng nhập có 2 trạng thái Khách / Đã đăng nhập, đã thể hiện ở mục 6.)

## 8. Luồng xử lý

**Luồng 1 — Đăng nhập**
```
Mở /admin/authentication ─(đã đăng nhập)─▶ /admin/ (REQ-21)
   │
   ▼ nhập Email + Password [+ Remember me] → Login / Enter
   ├─ Email sai định dạng ─▶ trình duyệt chặn, không gửi (REQ-08)
   ├─ Thiếu Email / Password ─▶ render lại tại chỗ + alert "…field is required." (REQ-05/06/07)
   ├─ Sai thông tin ─▶ chuyển về /admin/authentication + alert "Invalid email or password" (REQ-09/10), F5 mất alert (REQ-11)
   │     └─ sai liên tiếp nhiều lần ─▶ không khoá tài khoản (REQ-36)
   └─ Đúng ─▶ /admin/ Dashboard (REQ-18) — không có bước 2FA với tài khoản test
```

**Luồng 2 — Quên mật khẩu**
```
Login → "Forgot Password?" → /admin/authentication/forgot_password (REQ-24)
   ├─ Email sai định dạng ─▶ trình duyệt chặn (REQ-28)
   ├─ Email trống / không tồn tại ─▶ alert "Email not found" (REQ-26/27) ⚠️ bug tiềm ẩn RISK-06
   └─ Email tồn tại ─▶ ❔ chưa kiểm chứng, TC skip (REQ-29/30 · AMB-12 ✅)
```

**Luồng 3 — Đăng xuất**
```
Ảnh hồ sơ → menu → Logout (REQ-31)
   ├─ Có timer đang chạy ─▶ popup cảnh báo (REQ-33) → "Logout" → /admin/authentication (REQ-34)
   │                                                     └─ timer vẫn chạy (REQ-37)
   └─ Không có timer ─▶ /admin/authentication/logout → /admin/authentication (REQ-35 · chưa kiểm chứng)
Sau khi đăng xuất: mở route quản trị → về Login (REQ-23)
```

## 9. Yêu cầu phi chức năng (quan sát được)

| Hạng mục | Quan sát | Ghi chú |
|---|---|---|
| Bảo mật cookie | `csrf_cookie_name` và `sp_session` đều HttpOnly + Secure + SameSite=Lax | mục 4.3 |
| Cache | Response POST đăng nhập có `cache-control: no-store, no-cache, must-revalidate` | Quan sát trên response `303` |
| CAPTCHA / khoá tài khoản | Không có CAPTCHA trên form; PO chốt **không khoá** tài khoản khi sai nhiều lần (AMB-13 ✅) | REQ-36 — chưa kiểm chứng, chỉ kiểm trên tài khoản riêng |
| Dò tài khoản | Form Login giấu thông tin (REQ-10) nhưng Forgot Password báo "Email not found" | RISK-06 · bug tiềm ẩn (AMB-10 ✅) |
| Console | Trang Login: 0 lỗi, 0 cảnh báo console | Chrome 152 |
| Responsive | Chỉ khảo sát viewport 1600×750 | AMB-16 ⏭️ — recon mobile ở đợt riêng |

## 10. Điểm Mơ Hồ & Rủi Ro

### 10.1. Ambiguities

> Mã AMB đánh số **toàn hệ thống** (tiếp nối AMB-05 của `/discover-system`). AMB-01, AMB-02 là AMB cấp hệ thống — chỉ tham chiếu, không nhân bản.
> 2026-09-18: PO chốt AMB-06 → AMB-18 bằng **đúng Assumption tạm** (`PO-AMB-20260918`) → TC dựa trên assumption **không** phải sửa.

| Mã | Câu hỏi | Nguy cơ | Mức độ | Assumption tạm | Trạng thái | Kết luận |
|---|---|---|---|---|---|---|
| AMB-06 | Remember me có thực sự hoạt động? Sau khi đăng nhập có tick, chỉ thấy `csrf_cookie_name` và `sp_session` (hạn < 1 ngày), **không** có cookie ghi nhớ riêng. Lần quan sát này chưa chạy phép thử sạch (không xoá cookie trước) và dựa trên việc người dùng báo đã tick | Tính năng ghi nhớ không có tác dụng mà không TC nào phát hiện | 🔴 | Remember me **không** tạo cookie ghi nhớ → REQ-19/20 để ⚪ tới khi kiểm bằng phép thử sạch trên tài khoản riêng | ✅ Đã trả lời 2026-09-18 | Trùng assumption. REQ-19/20 giữ ⚪ — chờ tài khoản riêng để chạy phép thử sạch |
| AMB-07 | Checkbox Remember me có `value="estimate"` — cố ý hay lỗi copy template? | Máy chủ kiểm theo giá trị thì ghi nhớ không bao giờ bật | 🟡 | Máy chủ chỉ kiểm sự tồn tại của trường `remember` | ✅ Đã trả lời 2026-09-18 | Trùng assumption. REQ-14 🟡: chỉ assert có khoá `remember`, không assert giá trị |
| AMB-08 | Lỗi bắt buộc nhập trả `200` render tại chỗ, còn lỗi sai thông tin trả `303` về GET (PRG) — hai kiểu xử lý khác nhau cho cùng một form. Có cố ý? | Lỗi bắt buộc nhập: F5 sẽ hỏi gửi lại form | 🟡 | Hành vi hiện tại là đúng; TC không assert mã HTTP | ✅ Đã trả lời 2026-09-18 | Trùng assumption. Không cần kiểm mã trả về |
| AMB-09 | Chặn truy cập, chuyển hướng khi đã đăng nhập, và logout đều trả `307` thay vì `302/303`. Do ứng dụng hay do LiteSpeed/công cụ đo? | TC assert mã sẽ gãy khi đổi hạ tầng | 🟡 | Không assert mã; chỉ assert URL cuối | ✅ Đã trả lời 2026-09-18 | Trùng assumption. Không cần kiểm mã trả về |
| AMB-10 | Forgot Password báo "Email not found" cho email không tồn tại → có cho phép **dò email tồn tại** không (email tồn tại báo khác)? Chưa gửi email thật vì môi trường dùng chung. Mâu thuẫn với chính sách của form Login (REQ-10 giấu thông tin) | Lộ danh sách tài khoản staff | 🔴 | Email tồn tại nhận thông báo khác → rủi ro dò tài khoản; ghi thành bug tiềm ẩn chờ PO xác nhận | ✅ Đã trả lời 2026-09-18 | Trùng assumption: ghi nhận **bug tiềm ẩn** → mở RISK-06. REQ-27 giữ nguyên (mô tả hành vi hiện tại). Xác nhận hẳn cần hộp thư test (AMB-12) |
| AMB-11 | Forgot Password để trống Email báo "Email not found" thay vì thông báo bắt buộc như form Login | Thông báo gây hiểu nhầm; thiếu validation bắt buộc | 🟡 | Hành vi hiện tại là đúng như hệ thống đang chạy | ✅ Đã trả lời 2026-09-18 | Trùng assumption. REQ-26 giữ nguyên |
| AMB-12 | Luồng gửi email đặt lại mật khẩu và liên kết reset chưa kiểm được: cần hộp thư test + tài khoản riêng (không dùng tài khoản chung) | REQ-29/30 không có TC chạy được | 🔴 | TC viết trước, gắn `skip` tới khi có hộp thư test | ✅ Đã trả lời 2026-09-18 | Trùng assumption. REQ-29/30 giữ ⚪, TC gắn `skip` |
| AMB-13 | Có khoá tài khoản / CAPTCHA sau N lần sai mật khẩu không? Không thấy CAPTCHA; cấm thử nhiều lần trên tài khoản chung | Thiếu kiểm soát brute-force hoặc TC làm khoá tài khoản chung | 🟡 | Không có khoá; chỉ kiểm trên tài khoản riêng | ✅ Đã trả lời 2026-09-18 | Trùng assumption → sinh **REQ-LOGIN-36** (chỉ chạy trên tài khoản riêng) |
| AMB-14 | Trang Forgot Password không có link quay lại Login, và `document.title` vẫn là `… - Login` | Người dùng kẹt ở trang; tiêu đề sai ngữ cảnh | 🟢 | Ghi nhận như hành vi hiện tại, không assert tiêu đề trang Forgot | ✅ Đã trả lời 2026-09-18 | Trùng assumption. REQ-25 ghi rõ không assert tiêu đề |
| AMB-15 | (a) Đăng xuất qua cảnh báo timer có để timer tiếp tục chạy không? Popup không cho lựa chọn dừng. (b) Nhánh đăng xuất khi không có timer (REQ-35) chưa kiểm được vì tài khoản chung đang có timer chạy | Thời gian ghi nhận sai; TC logout rẽ nhánh không kiểm soát | 🟡 | (a) Timer vẫn chạy · (b) Hành vi đúng như mã JS `logout()` | ✅ Đã trả lời 2026-09-18 | Trùng assumption. (a) → sinh **REQ-LOGIN-37** · (b) REQ-35 giữ nội dung, ghi nguồn PO |
| AMB-16 | Lối Logout trong `#mobile-collapse` dùng được ở viewport mobile không? Chưa recon viewport mobile | Thiếu phủ responsive | 🟡 | Chưa khẳng định — cần recon riêng ở viewport mobile | ⏭️ Bỏ qua 2026-09-18 | PO chốt: không làm rõ ở đợt này, recon viewport mobile ở đợt riêng. Viewport mobile đưa ra ngoài phạm vi (mục 1) |
| AMB-17 | CSRF token trên form Login **không đổi** sau khi đăng xuất (so trong cùng phiên trình duyệt). Có yêu cầu xoay vòng token khi đổi phiên? | Rủi ro bảo mật thấp | 🟢 | Không yêu cầu xoay vòng | ✅ Đã trả lời 2026-09-18 | Trùng assumption. REQ-17 ghi rõ không yêu cầu đổi token |
| AMB-18 | Người bị chặn ở một route quản trị rồi đăng nhập có được đưa về đúng route đó không? Lần khảo sát kết thúc ở `/admin/` nhưng giữa hai bước có nhiều lần tải lại trang Login → chưa kết luận được | Thiếu REQ cho điều hướng sau đăng nhập | 🟡 | Chưa sinh REQ; kiểm lại bằng phép thử liền mạch trên tài khoản riêng | ⏭️ Bỏ qua 2026-09-18 | PO chốt: chưa sinh REQ ở đợt này; kiểm lại bằng phép thử liền mạch khi có tài khoản riêng |
| AMB-19 | REQ-LOGIN-36: cần thử sai **bao nhiêu lần** để khẳng định "không khoá"? PO chỉ chốt "không có khoá", chưa nêu con số | TC chọn N quá nhỏ thì không chứng minh được gì | 🟢 | N = 5 | ❓ Chờ trả lời | — |

### 10.2. Risks

| Mã | Rủi ro | Mô tả | Mitigation |
|---|---|---|---|
| RISK-01 | Làm nhiễu tài khoản test dùng chung | Hệ thống không khoá tài khoản (AMB-13 ✅), nhưng TC sai mật khẩu với email thật chạy lặp/song song vẫn làm bẩn log và có thể đụng người khác đang dùng | TC negative dùng email giả; TC REQ-10 chạy tối đa 1 lần/lượt, không chạy song song; REQ-36 **chỉ** chạy trên tài khoản riêng |
| RISK-02 | Timer trên tài khoản chung làm luồng Logout rẽ nhánh | Người khác bật/tắt timer làm TC logout lúc hiện popup, lúc không | TC kiểm tiền điều kiện `.started-timers-top li.timer` và đi đúng nhánh REQ-33/34 hoặc REQ-35; REQ-37 chỉ chạy trên tài khoản riêng |
| RISK-03 | Trình duyệt tự điền làm sai kết quả | Autofill điền email/mật khẩu khiến "ô rỗng" hoặc "không giữ giá trị" cho kết quả giả | Chạy profile sạch; assert thuộc tính `value` trong HTML, không assert nội dung ô |
| RISK-04 | Chuỗi validation HTML5 đổi theo trình duyệt/ngôn ngữ | Tooltip khác giữa Chrome/Firefox/locale | Assert `checkValidity()` và việc không phát sinh request |
| RISK-05 | Gửi email thật từ môi trường chung | Forgot Password với email tồn tại gửi mail tới người thật | Chỉ dùng email giả không tồn tại; luồng thật chờ hộp thư test (AMB-12) |
| RISK-06 | Dò tài khoản qua Forgot Password (bug tiềm ẩn) | Forgot Password trả "Email not found" với email không tồn tại, trong khi form Login cố ý giấu thông tin (REQ-10) → kẻ tấn công lọc được email staff hợp lệ (AMB-10 ✅) | Khi có hộp thư test: gửi email tồn tại, so thông báo với REQ-27 → khác nhau thì lập bug bằng `/create-bug-report` (severity cao — lộ thông tin); TC REQ-27 gắn nhãn `known-issue` |

## 11. Phân rã Epic / Story

**Epic:** `LOGIN` — Xác thực khu vực quản trị

| Story ID | Tên Story | REQ bao phủ | Số REQ | AMB / RISK liên quan | Ghi chú phạm vi |
|---|---|---|---|---|---|
| STORY-LOGIN-01 | Form đăng nhập & validation | REQ-LOGIN-01 → REQ-LOGIN-17 · REQ-LOGIN-36 | 18 | AMB-07 · AMB-08 · AMB-13 · AMB-17 · AMB-19 · RISK-01 · RISK-03 · RISK-04 | Giao diện, validation client/server, thông báo lỗi, payload, không khoá tài khoản |
| STORY-LOGIN-02 | Đăng nhập thành công, ghi nhớ & chặn truy cập | REQ-LOGIN-18 → REQ-LOGIN-23 | 6 | AMB-06 · AMB-09 · AMB-18 | Phiên, cookie, chuyển hướng theo trạng thái đăng nhập |
| STORY-LOGIN-03 | Quên mật khẩu | REQ-LOGIN-24 → REQ-LOGIN-30 | 7 | AMB-10 · AMB-11 · AMB-12 · AMB-14 · RISK-05 · RISK-06 | Trang Forgot Password, email khôi phục |
| STORY-LOGIN-04 | Đăng xuất | REQ-LOGIN-31 → REQ-LOGIN-35 · REQ-LOGIN-37 | 6 | AMB-15 · AMB-16 · RISK-02 | Menu hồ sơ, cảnh báo timer, timer sau đăng xuất, responsive |

**Tổng: 4 Story / 37 REQ** — `18 + 6 + 7 + 6 = 37 ✔`. Mọi REQ thuộc đúng một Story, không mồ côi, không trùng.

**Đối chiếu AMB/RISK:**

| Nhóm | Mã | Nằm ở đâu |
|---|---|---|
| AMB thuộc Story | AMB-06 → AMB-19 (14 mã) | Phân bổ ở bảng Story trên — mỗi mã đúng 1 Story |
| AMB cấp Epic | AMB-01 · AMB-02 _(cấp hệ thống, chỉ tham chiếu)_ | Ma trận Phân quyền (mục 6) |
| RISK thuộc Story | RISK-01 → RISK-06 | Phân bổ ở bảng Story trên |
| RISK cấp Epic | — | Không có |

Tự kiểm AMB thuộc Story: S1 5 (07, 08, 13, 17, 19) + S2 3 (06, 09, 18) + S3 4 (10, 11, 12, 14) + S4 2 (15, 16) = 14 ✔ · RISK: S1 3 + S3 2 + S4 1 = 6 ✔

**Hạng mục cấp Epic** (cố ý không gán Story):

| Hạng mục | Lý do |
|---|---|
| Ma trận Phân quyền (mục 6) | Cắt ngang Story 01 · 02 · 03 · 04 |
| Yêu cầu phi chức năng (mục 9) | Áp cho toàn module |
| Cookie phiên (mục 4.3) | Dùng chung cho Story 01 (CSRF) và Story 02 (phiên) |

**Thứ tự triển khai đề xuất:**

1. **STORY-LOGIN-01** — REQ-01 → 17 làm được ngay; REQ-36 **BLOCKED** chờ tài khoản riêng (+ AMB-19 🟢 chốt N)
2. **STORY-LOGIN-02** — cần credential hợp lệ; REQ-19/20 ⚪ **BLOCKED** chờ tài khoản riêng để chạy phép thử sạch (AMB-06 ✅ — kết luận hiện tại: không tạo cookie)
3. **STORY-LOGIN-04** — cần phiên đăng nhập từ Story 02; REQ-35 phụ thuộc trạng thái timer (RISK-02); REQ-37 **BLOCKED** chờ tài khoản riêng
4. **STORY-LOGIN-03** — REQ-24 → 28 làm được ngay; REQ-29/30 ⚪ TC gắn `skip` tới khi có hộp thư test (AMB-12 ✅); RISK-06 chờ hộp thư test để xác nhận bug

> ⚠️ **Nút thắt chung:** 4 REQ (19, 20, 36, 37) + AMB-18 cùng chờ **một tài khoản test riêng**. Xin được tài khoản này là gỡ phần lớn mục chặn của module.

## 12. Danh mục Evidence (`evidence/`)

| Tệp | Màn hình · trạng thái | REQ làm bằng chứng | Ghi chú phạm vi |
|---|---|---|---|
| `login_form_default_viewport.png` | Login — mặc định, focus ô Email | 01, 02 | |
| `login_submit_empty_error_viewport.png` | Login — submit để trống cả hai | 07 | |
| `login_submit_email_only_error_viewport.png` | Login — chỉ nhập Email | 06 | |
| `login_submit_password_only_error_viewport.png` | Login — chỉ nhập Password | 05 | |
| `login_submit_invalid_credentials_viewport.png` | Login — sai thông tin (email giả) | 09, 12 | |
| `forgot_password_form_default_viewport.png` | Forgot Password — mặc định | 24, 25 | |
| `forgot_password_submit_empty_error_viewport.png` | Forgot Password — submit để trống | 26 | |
| `login_logout_menu_open_clip.png` | Menu hồ sơ đang mở | 31 | Cắt vùng góc phải thanh đầu trang — ảnh viewport Dashboard chứa dữ liệu nghiệp vụ |
| `login_logout_timer_warning_viewport.png` | Popup cảnh báo timer khi Logout | 33 | Lớp phủ trắng che toàn trang — không lộ dữ liệu |

Không chụp: Dashboard sau khi đăng nhập (REQ-18, 21, 22 — chứa dữ liệu nghiệp vụ; bằng chứng là URL + `document.title` ghi trong AC) · REQ-08, 10, 11, 13 → 17, 23, 27, 28, 32, 34 — bằng chứng là số liệu DOM/network ghi trong AC · REQ-36, 37 — sinh từ quyết định PO, chưa kiểm trên UI nên chưa có ảnh.
Mọi ảnh trong bảng đã được mở lại xác nhận đúng trạng thái trước khi ghi danh mục.

## 13. Nhật ký Thay đổi

| Ngày | Nguồn | REQ ảnh hưởng | Loại | Tóm tắt thay đổi | TC cần xử lý |
|---|---|---|---|---|---|
| 2026-09-18 | PO-AMB-20260918 | REQ-LOGIN-36, REQ-LOGIN-37 | 🟢 Thêm | REQ-36 "Đăng nhập sai liên tiếp không khoá tài khoản" (giải quyết AMB-13) · REQ-37 "Timer tiếp tục chạy sau khi đăng xuất qua cảnh báo" (giải quyết AMB-15a). Cả hai chỉ chạy trên tài khoản riêng · mở AMB-19 🟢 (số lần sai N) | ➕ Viết mới — chưa có TC LOGIN |
| 2026-09-18 | PO-AMB-20260918 | REQ-LOGIN-14 | 🟡 Sửa | AC chỉ assert **có khoá** `remember` trong payload, không assert giá trị `estimate` (AMB-07 ✅) | Chưa có TC LOGIN — không TC nào stale |
| 2026-09-18 | PO-AMB-20260918 | REQ-LOGIN-17, 19, 20, 21, 23, 25, 26, 27, 29, 30, 32, 35 · mục 1, 3, 4, 8, 9, 10, 11 | ✏️ Biên tập | Ghi kết luận PO vào AC/Nguồn — **không đổi hành vi**: AMB-06, 08, 09, 10, 11, 12, 14, 15b, 17 → ✅ trùng assumption · AMB-16, 18 → ⏭️ · RISK-06 mới (dò tài khoản qua Forgot Password) · viewport mobile ra ngoài phạm vi | — |
| 2026-09-14 | UI recon | REQ-LOGIN-01 → REQ-LOGIN-35 | 🟢 Thêm | Khởi tạo tài liệu từ khảo sát UI thực tế (31 🟢 · 4 ⚪ — REQ-19, 20, 29, 30) · mở AMB-06 → AMB-18 · RISK-01 → RISK-05 | — (viết TC mới) |
