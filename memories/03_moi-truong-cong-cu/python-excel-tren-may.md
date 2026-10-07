# Máy Windows của user: Python · Excel · encoding

- Windows 11, shell chính PowerShell 5.1 (có Git Bash). Python dùng được qua `python` (WindowsApps) — có `openpyxl`. Lần đầu dùng skill SRS-Excel phải **cài thư viện Python** (`python-docx`, `openpyxl`…).
- In tiếng Việt ra console hay lỗi encoding → chạy với `PYTHONIOENCODING=utf-8`, hoặc verify bằng script không in Unicode. Lỗi in log **không** có nghĩa tạo file lỗi.
- File Excel **đang mở trong Excel thì bị khoá** — không xoá/ghi đè được. Nhờ user đóng file rồi thử lại.
- Không có pandoc / LibreOffice (đã thấy ở máy học khác). Đọc `.docx` có thể giải nén ZIP → `word/document.xml` + `comments.xml`.
- Chưa có cách render Excel ra ảnh để soát mắt → kiểm bằng script (công thức, merge, dropdown, số dòng) và nói rõ với user là chưa xem bằng Excel thật.
