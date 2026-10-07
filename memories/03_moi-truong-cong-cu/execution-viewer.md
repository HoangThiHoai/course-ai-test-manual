# Web viewer offline (`scripts/*-viewer/bundle.html`)

- 3 trang: `testcases-viewer` · `execution-viewer` · `bugs-viewer` — double-click mở, chạy offline. Mô tả chung ở CLAUDE.md mục "Xem kết quả bằng web viewer".
- **Thay đổi chưa commit (07-10-2026)** trong `scripts/execution-viewer/bundle.html` + `README.md`:
  - **Gộp nhiều lần chạy** cùng module + nền tảng: mỗi TC một dòng, lấy kết quả **lần chạy mới nhất** có chạy TC đó (xếp theo số trong Run ID); kết quả cũ hiện mờ (`trước: BLOCKED`), cột `Lịch sử các lần chạy` khi export.
  - Export Excel khi gộp: sheet `Tổng hợp` + mỗi lần chạy một sheet nguyên bản.
  - So sánh lần chạy thêm nhóm **🔓 Hết BLOCKED**; "Mới fail" tính cả BLOCKED → FAIL.
  - Cảnh báo "Dữ liệu chưa dọn" bỏ qua ô `—` của dòng "Không tạo bản ghi nào".
- Nguồn gốc thay đổi này không nằm trong transcript nào còn lưu — nếu user hỏi, xác nhận lại với user trước khi commit.
