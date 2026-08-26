# Software Requirements Specification (SRS)
## Module: Login (Đăng nhập)
### Hệ thống: Perfex CRM – Anh Tester Demo
### URL: https://crm.anhtester.com/admin/authentication

---

## 1. Giới thiệu

### 1.1 Mục đích
Tài liệu này mô tả yêu cầu chức năng và phi chức năng của module **Đăng nhập (Login)** trong hệ thống Perfex CRM, làm cơ sở cho việc thiết kế, phát triển và kiểm thử.

### 1.2 Phạm vi
Module Login cho phép người dùng (Admin/Staff) truy cập vào hệ thống CRM thông qua Email và Mật khẩu. Phạm vi tài liệu bao gồm:
- Đăng nhập hệ thống
- Ghi nhớ đăng nhập (Remember me)
- Khôi phục mật khẩu (Forgot Password)
- Đăng xuất (Logout)

### 1.3 Đối tượng sử dụng
| Vai trò | Mô tả |
|---|---|
| Admin | Quản trị viên hệ thống, có toàn quyền truy cập |
| Staff | Nhân viên được cấp tài khoản truy cập CRM |

---

## 2. Tổng quan hệ thống

Trang đăng nhập được truy cập tại địa chỉ `/admin/authentication`, hiển thị Form gồm các thành phần:

| # | Thành phần | Loại | Bắt buộc |
|---|---|---|---|
| 1 | Email Address | Textbox (type=email) | Có |
| 2 | Password | Textbox (type=password) | Có |
| 3 | Remember me | Checkbox | Không |
| 4 | Login | Button (submit) | - |
| 5 | Forgot Password? | Link → `/admin/authentication/forgot_password` | - |

Sau khi đăng nhập thành công, người dùng được điều hướng tới trang **Bảng tin (Dashboard)**.

---

## 3. Yêu cầu chức năng (Functional Requirements)

### FR-01: Đăng nhập thành công
**Mô tả:** Người dùng nhập đúng Email và Mật khẩu đã đăng ký, hệ thống cho phép truy cập vào hệ thống.
**Input:** Email hợp lệ đã tồn tại + Password đúng
**Output:** Chuyển hướng tới trang Bảng tin (Dashboard), hiển thị menu chức năng (Khách hàng, Dự án, Công việc, Hợp đồng, Doanh số, Thuê bao, Chi phí, Hỗ trợ, Khách tiềm năng, Báo cáo...).

### FR-02: Đăng nhập thất bại – sai thông tin
**Mô tả:** Khi Email hoặc Mật khẩu không đúng, hệ thống từ chối đăng nhập.
**Output:** Hiển thị thông báo lỗi: `Invalid email or password`. Người dùng vẫn ở lại trang Login.

### FR-03: Validate bỏ trống trường bắt buộc
**Mô tả:** Khi nhấn Login mà chưa nhập Email và/hoặc Password, hệ thống chặn submit và hiển thị thông báo lỗi tương ứng.
**Output:**
- `The Email Address field is required.` (khi bỏ trống Email)
- `The Password field is required.` (khi bỏ trống Password)

### FR-04: Validate định dạng Email
**Mô tả:** Trường Email Address có kiểu `type="email"`, trình duyệt thực hiện validate định dạng phía client (phải chứa ký tự `@` và domain hợp lệ). Nếu nhập sai định dạng, form không được submit.

### FR-05: Chức năng "Remember me"
**Mô tả:** Cho phép người dùng chọn checkbox "Remember me" để hệ thống ghi nhớ phiên đăng nhập trên trình duyệt cho lần truy cập sau, không yêu cầu đăng nhập lại trong thời gian quy định.

### FR-06: Chức năng "Forgot Password"
**Mô tả:** Người dùng nhấn link "Forgot Password?" để chuyển tới trang `/admin/authentication/forgot_password`, gồm:
| Thành phần | Loại |
|---|---|
| Email Address | Textbox |
| Confirm | Button (submit) |

Người dùng nhập Email đã đăng ký và nhấn "Confirm" để nhận email khôi phục mật khẩu (đặt lại mật khẩu qua liên kết gửi tới email).

### FR-07: Đăng xuất (Logout)
**Mô tả:** Người dùng đã đăng nhập có thể đăng xuất khỏi hệ thống qua chức năng Logout (`/admin/authentication/logout`). Sau khi đăng xuất, phiên làm việc kết thúc và hệ thống điều hướng trở lại trang Login.

### FR-08: Điều hướng khi chưa đăng nhập
**Mô tả:** Nếu người dùng chưa đăng nhập (hoặc phiên đã hết hạn/đăng xuất) mà truy cập vào các URL nội bộ của hệ thống (ví dụ Dashboard), hệ thống phải tự động điều hướng về trang Login.

---

## 4. Yêu cầu phi chức năng (Non-Functional Requirements)

| Mã | Hạng mục | Yêu cầu |
|---|---|---|
| NFR-01 | Bảo mật | Mật khẩu phải được che (masked) khi nhập, truyền tải qua HTTPS |
| NFR-02 | Bảo mật | Không hiển thị chi tiết Email/Password sai (chỉ hiển thị thông báo chung "Invalid email or password") để tránh dò thông tin tài khoản |
| NFR-03 | Hiệu năng | Thời gian phản hồi đăng nhập không quá 3 giây trong điều kiện mạng bình thường |
| NFR-04 | Khả dụng | Thông báo lỗi phải rõ ràng, hiển thị ngay tại trang Login, không mất dữ liệu người dùng đã nhập (ngoại trừ password) |
| NFR-05 | Khả năng tương thích | Hoạt động tốt trên các trình duyệt phổ biến (Chrome, Edge, Firefox) |
| NFR-06 | Đa ngôn ngữ | Giao diện hỗ trợ hiển thị theo ngôn ngữ hệ thống (English/Tiếng Việt tùy cấu hình) |

---

## 5. Quy tắc nghiệp vụ (Business Rules)

- BR-01: Email và Password là hai trường bắt buộc phải nhập trước khi submit.
- BR-02: Hệ thống không phân biệt lỗi cụ thể là "sai email" hay "sai mật khẩu" mà gộp chung thành một thông báo lỗi duy nhất.
- BR-03: Sau khi đăng nhập thành công, phiên làm việc được duy trì cho đến khi người dùng chủ động Logout hoặc phiên hết hạn (session timeout).
- BR-04: Khi chọn "Remember me", thời gian duy trì phiên đăng nhập được kéo dài hơn so với mặc định.

---

## 6. Kịch bản kiểm thử tham khảo (Test Scenarios)

| ID | Kịch bản | Dữ liệu | Kết quả mong đợi |
|---|---|---|---|
| TC-01 | Đăng nhập với Email/Password hợp lệ | admin@example.com / 123456 | Đăng nhập thành công, chuyển tới Dashboard |
| TC-02 | Đăng nhập với Email không tồn tại | wrong@example.com / wrongpass | Hiển thị "Invalid email or password" |
| TC-03 | Đăng nhập với Password sai | Email đúng / Password sai | Hiển thị "Invalid email or password" |
| TC-04 | Bỏ trống cả 2 trường rồi Login | (trống) | Hiển thị lỗi required cho cả Email và Password |
| TC-05 | Bỏ trống Email, nhập Password | Password bất kỳ | Hiển thị "The Email Address field is required." |
| TC-06 | Bỏ trống Password, nhập Email | Email bất kỳ | Hiển thị "The Password field is required." |
| TC-07 | Nhập Email sai định dạng (không có @) | notanemail | Trình duyệt chặn submit, hiển thị cảnh báo định dạng |
| TC-08 | Chọn "Remember me" rồi đăng nhập | Email/Password hợp lệ + check Remember me | Đăng nhập thành công, phiên được ghi nhớ |
| TC-09 | Nhấn "Forgot Password?" | - | Chuyển tới trang Forgot Password với form nhập Email |
| TC-10 | Gửi yêu cầu khôi phục mật khẩu | Email hợp lệ đã đăng ký | Hệ thống xác nhận đã gửi email khôi phục |
| TC-11 | Đăng xuất khỏi hệ thống | Đang ở trạng thái đã đăng nhập | Chuyển về trang Login, không thể truy cập lại Dashboard nếu không đăng nhập lại |
| TC-12 | Truy cập URL nội bộ khi chưa đăng nhập | Truy cập trực tiếp URL Dashboard | Tự động điều hướng về trang Login |

---

## 7. Ghi chú
Tài liệu được biên soạn dựa trên khảo sát thực tế giao diện và hành vi của module Login tại `https://crm.anhtester.com/admin/authentication` (Perfex CRM – Anh Tester Demo).
