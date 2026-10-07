# AMB — UC Thanh toán / Bán hàng gói cước (Web OA) — CHƯA viết TC

> Nguồn: phiên 30-09-2026 (session `32a3a1f4`). SRS đọc lúc đó là phần **"Cửa hàng & Giỏ hàng" / Luồng mua gói trên Web OA** + ảnh design nhúng trong SRS + biên bản họp 16/09. **Chưa đối chiếu được Figma** (trang `CMS Gói cước → Thanh toán gói cước → UI`) vì canvas không chụp được.
>
> Trạng thái: user **dừng** việc viết TC cho UC này, chuyển sang bổ sung UC4 Ban hành (xem [tc-da-viet-va-quy-uoc-id.md](tc-da-viet-va-quy-uoc-id.md)). Danh sách dưới đây **chưa gửi BA, chưa có câu trả lời** — khi quay lại UC Thanh toán, dùng làm điểm xuất phát rồi đối chiếu Figma để bổ sung.
>
> Sheet khuôn đã chọn lúc đó: **QLDH_Chi tiết đơn hàng** (theo `gid` user gửi), đầu ra dự kiến `docs/testcases/goi-cuoc/web/`.

## Danh sách điểm mơ hồ / mâu thuẫn (36 điểm)

**A. Phạm vi**
1. Biên bản họp 16/09 ghi "Xuất hoá đơn" là **ngoài phạm vi phase 1**, nhưng SRS vẫn có UC "Nhập thông tin xuất hoá đơn" đủ các trường. Có viết TC không, hay viết rồi đánh dấu N/A?
2. UC "Nhập mã nhân viên giới thiệu", "Kiểm tra điều kiện checkout, cảnh báo lựa chọn gói" và "Luồng thanh toán đơn hàng" **chỉ có tiêu đề, không có nội dung**. Biên bản cũng ghi "Ghi nhận doanh thu cho nhân viên kênh" là ngoài phạm vi.
3. Phương thức thanh toán trên web chưa chốt. Sơ đồ ghi "Lựa chọn PTTT → trang quét QR", nhưng không có mô tả màn hình.

**B. Mua gói chính**
4. Biên bản ghi "tại 1 thời điểm chỉ có 1 gói chính, **hết hạn mới được đăng ký thêm**". Trong khi đó BR3 và sơ đồ ghi "cho phép mua gói chính mới + cảnh báo, **huỷ gói cũ**". Hai chỗ trái nhau.
5. Nội dung cảnh báo khi TK OA đang có gói chính chỉ có trong sơ đồ, câu chữ chưa chuẩn ("tk OA đang có gói chính…"). Chưa có nút nào ngoài "Chọn lại / Xác nhận".
6. BR2 "đã dùng gói miễn phí thì không được chọn lại": nút hiển thị thế nào ("Đã đăng kí" + disable?) và câu thông báo là gì?
7. Đổi chu kỳ (7 → 15 tháng) khi đã chọn một gói ở chu kỳ cũ thì gói trong giỏ bị giữ, bị bỏ hay tự đổi sang chu kỳ mới?
8. Chu kỳ khác đơn vị (7 ngày và 1 tháng) sắp xếp và gộp thế nào? (Biên bản chốt 1 tháng = 30 ngày.)
9. Màu tag chỉ định nghĩa cho 3 gói (xanh – cam – tím). Gói thứ 4 trở đi màu gì?
10. Thẻ gói chính có hiển thị tag CTKM hoặc giá gốc gạch ngang không? SRS chỉ ghi "giá bán theo chu kỳ".
11. Tham số giá trị "Không": SRS ghi "-", design hiển thị "—". Giá trị lớn (5000) có dấu phân cách hàng nghìn không?

**C. Gói 0đ và gói add-on**
12. BR_03 ghi "**tuyệt đối không** tồn tại add-on trong giỏ khi gói chính 0đ". Nhưng luồng 4a và design vẫn **giữ add-on trong giỏ**, chỉ disable nút Thanh toán.
13. Bước 5 ghi "không chọn gói chính nào thì enable nút Thanh toán". Trong khi đó BR2 của giỏ hàng ghi "chỉ enable khi có ít nhất 1 gói chính".
14. Chưa chọn gói chính thì vùng add-on enable hay disable? Theo sơ đồ, nếu TK OA **đã có gói chính đang hoạt động** thì được mua add-on lẻ, nhưng như vậy trái với BR2 của giỏ hàng.
15. Có được chọn **2 gói cùng một loại gói add-on** không (ví dụ Brandname 5.000 tin và 10.000 tin)? BR4 chỉ nói về gói chính của dịch vụ khác.
16. Design "Bộ miniapp hành chính công" cho tick nhiều gói cùng lúc. Có mâu thuẫn với BR4 không?
17. Công thức BR3 ghi "× % giảm giá", đúng nghĩa phải là "× (1 − %)". CTKM giảm tiền thì trừ **1 lần** hay trừ theo mỗi số lượng/chu kỳ? "Giá gói (chu kỳ bé nhất)" là giá của gói nào?
18. Stepper Số lượng / Thời gian: có **giá trị tối đa** không? Có cho nhập tay không? Gói có nhiều tham số "yêu cầu lựa chọn" thì hiển thị bao nhiêu stepper?
19. UC Hiển thị gói add-on có luồng A1 ghi "ẩn block **Gói chính**". Đây là lỗi copy, phải là block Add-on?
20. Mua lại / nâng cấp / hạ cấp gói add-on (BR3 tổng hợp): chưa có câu cảnh báo, chưa rõ chặn ở bước nào, chưa có định nghĩa cụ thể "gói cao hơn".
21. Chu kỳ add-on lớn hơn gói chính thì cảnh báo. Khi đó so với gói chính **trong giỏ** hay gói chính **đang hoạt động**? Có tính cả thời gian đã tăng bằng stepper không?

**D. Giỏ hàng và Checkout**
22. Tên nút: SRS ghi **"Tiếp tục"**, design ghi **"Thanh toán"**.
23. Số liệu mẫu trên design không khớp công thức: 2.140.000 − 100.000 ≠ 1.141.800. Card mẫu còn có giá gốc 180.000 thấp hơn giá bán 199.000.
24. "Xóa tất cả" có popup xác nhận không? Giỏ trống hiển thị đúng câu gì ("vui lòng chọn gói cước")?
25. Reload trang hoặc đăng nhập lại thì giỏ hàng có được giữ không?
26. Giỏ chỉ có gói 0đ (tổng 0đ): vẫn đi qua checkout và cổng thanh toán?
27. Banner checkout: SRS ghi "icon bóng đèn", design là icon "!". Khi không có add-on thì có ẩn header "GÓI ADD-ON" không?
28. Câu toast lỗi mạng không thống nhất: "Thất bại. Vui lòng kiểm tra lại kết nối." và "Vui lòng kiểm tra đường truyền".
29. Mở thẳng URL checkout khi giỏ trống, hoặc gói/CTKM hết hiệu lực giữa chừng, thì xử lý thế nào?

**E. Thông tin xuất hoá đơn**
30. Chuyển Cá nhân ↔ Công ty: A2 ghi "chỉ giữ Email, các trường khác làm trống", còn E3 ghi "**giữ lại toàn bộ**".
31. Mã số thuế: String-14 "chỉ cho nhập số", nhưng MST chi nhánh có dạng `0100109106-001`, có dấu "-". Độ dài tối thiểu (10 / 13 số) là bao nhiêu?
32. Email của form Cá nhân không có maxlength (form Công ty là 100). Chưa có câu lỗi riêng từng trường (CCCD thiếu số, email sai định dạng); SRS chỉ có câu chung "Vui lòng nhập đầy đủ thông tin thanh toán".
33. Tên người mua / người đại diện có cho nhập số và ký tự đặc biệt không? Form Công ty chưa có placeholder.
34. Bỏ tick "Xuất hoá đơn" sau khi đã nhập: dữ liệu bị xoá hay được giữ khi tick lại?
35. BR3 ghi "click thanh toán **tại giỏ hàng** để validate", nhưng form này nằm ở màn Checkout.

**F. Phân quyền**
36. TK vừa không có quyền, vừa sai trạng thái thì hiện thông báo nào trước? Câu "(hoặc mẫu thông báo chung)" cũng chưa chốt.
