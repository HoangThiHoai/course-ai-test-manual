# Phân tích Requirement - Module Login

**Nguồn:** [docs/SRS_Login.md](../SRS_Login.md)
**Hệ thống:** Perfex CRM – Anh Tester Demo
**URL:** https://crm.anhtester.com/admin/authentication

---

## 1. Happy Path (Luồng chính)

- Người dùng truy cập trang Login tại `/admin/authentication`.
- Nhập đúng **Email** đã đăng ký và đúng **Password**.
- Nhấn nút **Login**.
- Hệ thống xác thực thành công, điều hướng tới trang **Dashboard** với đầy đủ menu chức năng (Khách hàng, Dự án, Công việc, Hợp đồng, Doanh số, Thuê bao, Chi phí, Hỗ trợ, Khách tiềm năng, Báo cáo...). *(FR-01)*
- (Tùy chọn) Người dùng tick **Remember me** trước khi Login → đăng nhập thành công và phiên được ghi nhớ lâu hơn mặc định. *(FR-05, BR-04)*
- Người dùng chủ động **Logout** → hệ thống kết thúc phiên và điều hướng về trang Login. *(FR-07)*

## 2. Alternate Path (Luồng thay thế)

- **Quên mật khẩu:** Người dùng nhấn link "Forgot Password?" → chuyển tới `/admin/authentication/forgot_password` → nhập Email đã đăng ký → nhấn "Confirm" → hệ thống gửi email khôi phục mật khẩu (đặt lại mật khẩu qua liên kết trong email). *(FR-06)*
- **Remember me:** Chọn checkbox trước khi đăng nhập để duy trì phiên lâu hơn cho lần truy cập sau, không cần đăng nhập lại trong thời gian quy định. *(FR-05, BR-04)*
- **Truy cập lại khi đã có phiên "remember":** Người dùng quay lại hệ thống trong thời gian phiên còn hiệu lực → được vào thẳng Dashboard mà không cần nhập lại Email/Password (suy luận từ FR-05, chưa được mô tả rõ trong tài liệu).

## 3. Exception Path (Luồng lỗi / bị từ chối)

- **Sai thông tin đăng nhập:** Nhập sai Email hoặc sai Password (hoặc cả hai) → hệ thống từ chối, hiển thị thông báo chung `Invalid email or password`, không chỉ rõ trường nào sai (BR-02), người dùng ở lại trang Login. *(FR-02, NFR-02)*
- **Bỏ trống trường bắt buộc:**
  - Bỏ trống cả Email và Password → hiển thị đồng thời cả hai lỗi required.
  - Chỉ bỏ trống Email → `The Email Address field is required.`
  - Chỉ bỏ trống Password → `The Password field is required.`
  *(FR-03, BR-01)*
- **Sai định dạng Email:** Nhập Email không đúng định dạng (thiếu `@`, thiếu domain...) → trình duyệt chặn submit ở phía client, hiển thị cảnh báo định dạng gốc của trình duyệt. *(FR-04)*
- **Truy cập trái phép khi chưa đăng nhập:** Chưa đăng nhập (hoặc phiên hết hạn/đã logout) mà truy cập trực tiếp URL nội bộ (VD: Dashboard) → hệ thống tự động điều hướng về trang Login. *(FR-08)*
- **Phiên hết hạn (session timeout):** Phiên làm việc tự hết hạn sau một khoảng thời gian không hoạt động → người dùng bị đưa về trang Login khi thao tác tiếp hoặc tải lại trang. *(BR-03, suy luận)*

## 4. Các điểm còn mơ hồ / thiếu sót cần làm rõ

1. **Giới hạn số lần đăng nhập sai:** Tài liệu không đề cập cơ chế khóa tài khoản/CAPTCHA sau N lần đăng nhập sai liên tiếp. Có áp dụng brute-force protection không?
2. **Thời gian phiên cụ thể:** FR-05/BR-04 nói "thời gian quy định" và "kéo dài hơn mặc định" nhưng không nêu con số cụ thể (VD: mặc định 30 phút, remember me 7 ngày?). Cần giá trị chính xác để viết test case về thời gian hết hạn.
3. **Độ dài/độ phức tạp Password:** Không có yêu cầu về ràng buộc định dạng, độ dài tối thiểu/tối đa của Password khi đăng nhập (khác với khi tạo mới). Có giới hạn ký tự nhập vào ô Password không (VD: max length)?
4. **Khoảng trắng đầu/cuối (trim) và phân biệt hoa-thường của Email:** Hệ thống có tự trim khoảng trắng thừa hay phân biệt chữ hoa/thường trong Email khi so khớp tài khoản không?
5. **Tài khoản bị vô hiệu hóa/khóa:** Nếu tài khoản Admin/Staff bị deactivate hoặc bị khóa bởi quản trị viên, thông báo lỗi khi đăng nhập là gì? Có giống thông báo "Invalid email or password" hay khác?
6. **Forgot Password với Email không tồn tại:** FR-06/TC-10 chỉ mô tả trường hợp Email hợp lệ đã đăng ký. Khi nhập Email không tồn tại trong hệ thống thì phản hồi ra sao (báo lỗi cụ thể hay vẫn hiển thị thông báo chung để tránh dò tài khoản, theo tinh thần NFR-02)?
7. **Đa phiên đăng nhập (multi-session):** Một tài khoản có được phép đăng nhập đồng thời trên nhiều thiết bị/trình duyệt không, hay phiên cũ sẽ bị hủy khi đăng nhập nơi khác?
8. **Hành vi khi mất kết nối mạng/timeout server (NFR-03):** Nếu phản hồi vượt quá 3 giây hoặc mất kết nối giữa chừng, hệ thống hiển thị thông báo lỗi gì cho người dùng?
9. **Đăng nhập khi phiên đang hoạt động:** Nếu người dùng đã đăng nhập, truy cập lại trực tiếp URL `/admin/authentication` thì hệ thống xử lý thế nào (tự động chuyển vào Dashboard hay vẫn hiển thị lại form Login)?
