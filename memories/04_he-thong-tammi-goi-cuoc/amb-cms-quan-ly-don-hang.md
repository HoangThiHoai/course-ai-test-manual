# AMB — CMS Quản lý đơn hàng (Tammi Gói cước - Đơn hàng) — chưa gửi BA

> Phiên 07-10-2026. Nguồn: SRS mới `1gebcMrC…` (tài liệu "Danh sách đơn hàng" + "Tổng hợp trạng thái" B/C + "Miniapp gói cước Tammi"), Figma CMS node `42456-50485`, Figma Miniapp `Super App File 01` node `113087-6879`.
> TC: `docs/testcases/goi-cuoc/web/TCs_GOICUOC_CMS_Quanlydonhang.xlsx` (289 TC) — xem [tc-da-viet-va-quy-uoc-id.md](tc-da-viet-va-quy-uoc-id.md). Mỗi AMB đã ghi ở cột Ghi chú TC tương ứng ("Cần BA confirm").

## Mâu thuẫn SRS ↔ design
1. Phân trang mặc định: SRS 25 dòng/trang — design "10 dòng"; danh sách giá trị dropdown chưa có.
2. Định dạng thời gian: SRS `DD/MM/YYYY HH:MM:SS` — design bảng danh sách + dòng đơn hàng `2026-08-08 17:43:52` (màn chi tiết lại đúng SRS).
3. Không có kết quả tìm kiếm: SRS "Không tìm thấy kết quả" — design "Không tìm thấy kết quả phù hợp / Vui lòng thử từ khóa khác".
4. Tiêu đề chi tiết: SRS "Chi tiết đơn hàng- ID: xxx" — design "← Chi tiết đơn hàng", ID ở ô riêng, thêm icon ⓘ cạnh Trạng thái đơn hàng (tooltip chưa định nghĩa).
5. Xem chi tiết: SRS click Mã đơn hàng (màu đỏ) — design có thêm cột Thao tác icon (i); mã đỏ chỉ ở dòng đầu.
6. Kết quả CCDV: SRS "Cung cấp dịch vụ thành công" — design chi tiết "Hoàn thành cung cấp dịch vụ".
7. Dòng đơn hàng: design có cột "Gia hạn tự động" không có trong SRS; Miniapp màn kết quả ghi "Tự động gia hạn: Có" + frame "Bắt buộc tự động gia hạn" — trái "phase 1 mặc định Không".
8. Hoá đơn mã QHNS: design vẫn label "Mã số thuế"; Cá nhân ẩn MST/Tên công ty nhưng SRS đặt Bắt buộc = Có.
9. Placeholder tìm kiếm chỉ "Tìm kiếm theo mã đơn hàng" trong khi SRS tìm theo ID + mã.
10. Sắp xếp: design có icon sort mọi cột (trừ Tổng giá gốc, Thao tác) — SRS không mô tả.

## SRS thiếu / tự mâu thuẫn
11. Chi tiết STT 5 "Phương thức thanh toán: hiển thị số điện thoại…" — lỗi copy.
12. Đơn chưa thanh toán / thất bại: Tổng tiền thanh toán, PTTT, Nguồn tiền, Kết quả CCDV (Bắt buộc = Có) hiển thị gì.
13. Trạng thái thanh toán "Đã hoàn tiền" (nhắc trong Hoàn thành) có phải giá trị thứ 4 không; refund "TẠM CHƯA LÀM" → đơn CCDV lỗi kẹt mãi ở "Chờ xử lý hoàn tiền"?
14. Đơn con: UI liệt kê "Chờ cung cấp dịch vụ" nhưng bảng trạng thái đơn con không có.
15. Bộ lọc: STT nhảy 1,2,3,8…15; enable button Áp dụng; ngày mặc định (design có sẵn 10/08–15/08); validate khoảng ngày; tìm gần đúng hay chính xác; +84; trim.
16. Tìm kiếm "từ ký tự thứ 3" → không tìm được ID 1–2 chữ số. Câu lỗi khác nhau giữa các UC ("Hệ thống bận, vui lòng…" / "Lỗi hệ thống, vui lòng…" / "Hệ thống bận. Vui lòng…").
17. Cài đặt bảng: Figma chưa có popup; cột Thao tác có cấu hình không; lưu theo tài khoản/phiên.
18. Thuê bao thụ hưởng Tk OA: SĐT hay OA ID (màn Gói cước đã đăng ký dùng OA ID).
19. Toast không có quyền có lỗi chính tả ("ko", "nay"); menu ẩn hay hiện.
20. Mã giới thiệu & Thông tin xuất hoá đơn: Figma Miniapp phase 1 không có bước nhập → đơn miniapp có dữ liệu không.
21. Định dạng Mã đơn hàng: "ORD2026080200222" vs "8867544479346".
22. UC Xuất excel chỉ có tiêu đề → TC N/A.
23. Miniapp: popup "Thuê bao đã đạt số lượng mua gói cước tối đa" — rule chưa có trong SRS; toast giá đổi khác nhau giữa bảng và PlantUML; cơ chế xử lý đơn treo "Chờ thanh toán" khi user thoát app.
24. Miniapp Lịch sử giao dịch có "Loại giao dịch (Đăng ký/Gia hạn)" — CMS không có cột này.
