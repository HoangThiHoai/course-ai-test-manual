---
name: skills-generate-srs-from-website
description: Phân tích một yêu cầu/chức năng thành Happy Path, Alternate Path, Exception Path và liệt kê các điểm còn mơ hồ cần hỏi lại. Dùng trước khi sinh Test Case cho một chức năng phức tạp, nhiều luồng xử lý.
---

## Mục đích

Skill này dùng để phân tích một website/web application từ URL được cung cấp và tạo tài liệu SRS (Software Requirements Specification) dựa trên các chức năng, giao diện và business flow có thể quan sát được trên website.

Mục tiêu là tạo ra SRS có cấu trúc rõ ràng, đủ thông tin để BA/QA/Developer có thể sử dụng làm cơ sở:

- Phân tích yêu cầu
- Thiết kế Test Case
- Kiểm thử chức năng
- Kiểm thử validation
- Kiểm thử business rule
- Kiểm thử API nếu có thông tin
- Regression Test
- Xác định các requirement còn thiếu hoặc chưa rõ

---

# 1. Input

Skill nhận các thông tin đầu vào sau:

### Bắt buộc

- URL website cần phân tích.

### Có thể cung cấp thêm

- Tài khoản đăng nhập nếu website yêu cầu authentication.
- Requirement/SRS hiện tại.
- Tài liệu nghiệp vụ.
- Screenshot.
- Figma.
- API documentation / Swagger.
- Test Case cũ.
- Business rule.
- Các chức năng cần tập trung phân tích.

Nếu người dùng cung cấp tài liệu tham khảo, phải ưu tiên sử dụng tài liệu đó để xác định requirement.

---

# 2. Nguyên tắc phân tích

Khi phân tích website:

1. Không được tự ý bịa business rule.
2. Chỉ xác định requirement dựa trên:
   - Nội dung hiển thị trên website.
   - Hành vi thực tế quan sát được.
   - Dữ liệu người dùng nhập.
   - Navigation.
   - Validation.
   - Message.
   - Flow nghiệp vụ.
   - Tài liệu người dùng cung cấp.
3. Nếu không xác định được một requirement thì đánh dấu:
   `TBD`
4. Nếu có suy luận từ hành vi website thì phải ghi rõ:
   `Inferred`
5. Phân biệt rõ:
   - Requirement đã xác nhận.
   - Requirement quan sát được.
   - Requirement suy luận.
   - Requirement chưa xác định.

Không được biến assumption thành business rule chính thức.

---

# 3. Quy trình thực hiện

## Step 1 - Access website

Truy cập URL được cung cấp.

Xác định:

- Website title.
- URL.
- Login requirement.
- Các màn hình chính.
- Navigation.
- Menu.
- Header.
- Sidebar.
- Footer.
- Các module/chức năng.

---

## Step 2 - Analyze navigation

Xác định cấu trúc navigation:

```text
Website
├── Authentication
│   ├── Login
│   ├── Logout
│   └── Forgot Password
│
├── Dashboard
│
├── Module A
│   ├── List
│   ├── Detail
│   ├── Create
│   ├── Edit
│   └── Delete
│
└── Module B