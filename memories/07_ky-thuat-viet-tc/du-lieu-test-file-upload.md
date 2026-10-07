# Dữ liệu test file upload theo giá trị biên (24-09-2026)

## Yêu cầu user đã dùng

Ảnh: 4× 5MB · 5.01MB · 4.9MB · 20MB · 19.9MB · 20.01MB. Video: 200MB · 199.9MB · 200.01MB · 99.9MB · 100.01MB · 2× 100MB. (Biên upload ảnh 5MB/20MB, video 100MB/200MB.)

## Cách đã làm (dùng lại được)

- Quy ước **1MB = 1.048.576 byte (MiB)** — user chọn. VD 5MB = 5.242.880 · 5.01MB = 5.253.366 · 4.9MB = 5.138.022 · 20MB = 20.971.520 · 19.9MB = 20.866.662 · 20.01MB = 20.982.006 byte. Hỏi lại nếu hệ thống đang test dùng MB thập phân (1.000.000).
- Ảnh `.jpg`, video `.mp4` H.264 **hợp lệ thật**: sinh file gốc rồi **pad phần dư vào vùng an toàn của định dạng** → đúng byte tuyệt đối mà vẫn mở/phát được. Verify cả byte size lẫn decode/phát thử file lớn nhất.
- Kỹ thuật dùng skill `skills-test-data-generator`.

## Lưu ý

- Bộ ~1,1 GiB này **không được commit** (đã gây sự cố push — [02_repo-va-quy-trinh/git-push-va-file-lon.md](../02_repo-va-quy-trinh/git-push-va-file-lon.md)). Thư mục `test-data/upload-boundary/` hiện **không còn trên máy** (07-10-2026) — cần thì sinh lại, để ngoài git.
