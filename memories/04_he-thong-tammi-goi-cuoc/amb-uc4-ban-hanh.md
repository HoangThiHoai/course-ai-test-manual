# AMB — UC4 Ban hành gói cước (CMS admin)

> Nguồn: phiên 30-09-2026 (session `e82bcd49`), sau khi đối chiếu SRS tab Quản lý gói cước + Figma section **"Chi tiết gói cước"** (node `34842-144249`).
> Các TC liên quan ghi "BA confirm" ở cột Ghi chú trong `TCs_GOICUOC_Chitiet_Banhanh_UC3_UC4.xlsx`.
> Trạng thái: **chưa có câu trả lời của BA** (tính tới 07-10-2026). Có câu trả lời → cập nhật file này + sửa TC tương ứng.

## Mới phát hiện 30-09-2026

1. **Nút "Nhân bản gói"** có trên Figma ở trạng thái Nháp nhưng SRS không mô tả.
2. **Không tạo được dữ liệu TH1.2/TH1.3 qua giao diện**: SRS bắt buộc thời gian bắt đầu > hiện tại. Bộ TC cũ dùng "bắt đầu = hiện tại − 1 ngày" → phải sửa DB. Đã thêm TC theo cách "tạo gói rồi chờ qua mốc thời gian".
3. **Sửa ngày kết thúc ở TH1.3**: thời gian bắt đầu đã ở quá khứ; nếu màn Chỉnh sửa áp rule "bắt đầu > hiện tại" thì không lưu được. UC Chỉnh sửa gói cước trong SRS đang **để trống**.
4. **Luồng Thủ công mâu thuẫn**: SRS bước 2 ghi "chuyển trạng thái" ngay, sơ đồ luồng + Figma hiển thị popup trước.
5. **Thời gian bắt đầu ở UC2**: bảng mô tả ghi "bắt buộc khi Thủ công", BR02 ghi "bắt buộc khi Tự động".
6. **Job quét tự động có xử lý gói Nháp không?** Câu "Từ Nháp … tự động chuyển sang khi hệ thống quét" chưa rõ.
7. **Đã phát hành → Ngừng kinh doanh qua "Trạng thái kinh doanh"**, nhưng Đã phát hành chỉ xảy ra ở chế độ Tự động.
8. **Gói nền** sau phát hành hiển thị ở đâu, có cần phát hành không.
9. **Mốc so sánh thời gian**: giờ server hay giờ máy người dùng.
10. **Figma vẫn hiện nút Xóa ở trạng thái Đang kinh doanh**, bảng trạng thái cấm xoá gói đang kinh doanh.

## Đã ghi từ bộ cũ (24-09-2026), vẫn còn hiệu lực

- Popup trong SRS khác design (tiêu đề, nút Hủy/Sửa…).
- TH1.2 và TH1.3 chồng điều kiện nhau.
- Nhãn "đã ban hành" trên màn danh sách (UC1 đã có TC sắp xếp cột Trạng thái ghi mâu thuẫn này).
