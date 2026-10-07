# AMB — UC1 Danh sách gói cước: Cài đặt bảng + Bộ lọc

> Nguồn: phiên 02-10-2026 (session `e63a19f1`). Nghiệp vụ suy từ **8 ảnh chụp màn hình** user đính kèm (không có SRS cho phần này).
> 34 TC dựa trên rule ảnh chưa thể hiện → ghi "Cần BA confirm" ở cột Ghi chú, tổng hợp ở **bảng 7** sheet `Kỹ thuật thiết kế TC` của file `TCs_GOICUOC_Quanlygoicuoc_UC1_CaidatbangBoloc_Bosung.xlsx`.
> Trạng thái: **chưa có câu trả lời của BA** (tính tới 07-10-2026).

## Điểm cần BA xác nhận

1. **Tên gọi lệch nhau**: bộ lọc ghi "Kênh phân phối", option "Miniapp Tammi"; cột trên bảng ghi "Kênh bán", giá trị "Mini app gói cước". Bộ lọc "Loại hình gói" có option **"Nền"**, cột Loại hình chỉ có Chính / Add-on.
2. **Cột Thao tác** không có trong popup Cài đặt bảng → đang coi là cột cố định. Chưa rõ có được ẩn cột Mã gói không.
3. **Bỏ chọn hết cột**: nút Cập nhật bị khoá hay báo lỗi? Đang viết theo cách sheet **CMS-CTKM** làm.
4. **Lưu cấu hình bảng**: theo tài khoản, theo trình duyệt, hay mất khi tải lại trang?
5. **Chọn cả 2 kênh**: HOẶC hay VÀ?
6. **Sau khi lọc**: loại gói không còn gói nào khớp có bị ẩn không? Badge hiển thị tổng số hay số sau lọc?
7. **Xoá lọc** có tự tải lại danh sách không? Có xoá từ khoá ô tìm kiếm không?
8. **Đóng tab Bộ lọc / F5 / chuyển màn khác**: điều kiện lọc có được giữ không?

## Quy tắc đã giả định khi viết TC (bảng quyết định nút Áp dụng)

- Chưa chọn gì → nút Áp dụng bị khoá.
- Nhiều giá trị **trong cùng một trường** → HOẶC.
- Nhiều **trường** → VÀ.
- Lọc theo đơn vị chu kỳ **đã lưu**, không quy đổi (14 ngày ≠ 2 tuần).

Ghi chú cũ ở TC-15 ("Chưa có popup") và TC-99 ("Cần bổ sung thêm TC…") để nguyên — user tự quyết có xoá không.
