# Người dùng — hồ sơ & cách làm việc mong muốn

## Hồ sơ

- QA **manual tester**, giao tiếp bằng **Tiếng Việt**. GitHub: `HoangThiHoai` (git user `KunMan`).
- Đang học khoá **AI Test** (khung `.claude/` lấy từ "thầy", hệ thống thực hành Perfex CRM) và **áp dụng vào dự án thật**: Tammi gói cước, F2C/PIFA (Viettel Post).
- Viết TC dự án thật dưới dạng **Excel / Google Sheet** theo template công ty ("KỊCH BẢN KIỂM THỬ"), dùng kỹ thuật: phân vùng tương đương, giá trị biên, bảng quyết định, sơ đồ chuyển trạng thái.
- Gõ nhanh, hay sai chính tả / tên lệnh (VD `/analyze-requiment-doccument`, `/update-TC-form-impact`) → tự hiểu ý, map sang lệnh đúng.

## Cách làm việc user muốn (feedback đã thể hiện)

| Điều | Vì sao / bằng chứng |
|---|---|
| **KHÔNG sửa trực tiếp Google Sheet / file gốc** — luôn tạo **file Excel riêng / bản nháp** để user review trước | Nhắc lại trong mọi yêu cầu viết TC (30-09, 02-10-2026) |
| **Đọc đủ nguồn trước khi viết TC** — đặc biệt **Figma thật** (user đã đăng nhập sẵn), không chỉ ảnh nhúng trong SRS | 30-09: user **ngắt** khi agent bắt đầu viết TC mà chưa đọc được Figma: "dừng viết TC, hãy đọc file figma mà tôi đã đăng nhập…" |
| **Liệt kê điểm mơ hồ / mâu thuẫn (cần CF với BA)** song song với TC — đây là yêu cầu bắt buộc, không phải phụ | Cùng lần ngắt trên: "…và còn phải liệt kê điểm mơ hồ mà" |
| Phát hiện **đã có TC** cho phạm vi được giao → **dừng hỏi**, ưu tiên **bổ sung** thay vì viết lại | 30-09: user chọn "rà lại và bổ sung" cho UC4 |
| Thích **một file hoàn chỉnh** hơn nhiều file lẻ: bổ sung xong thì gộp vào file chính, chèn đúng nhóm | 30-09: "gộp lại thành 1 bản hoàn chỉnh giúp tôi" |
| Dữ liệu test biên phải **chính xác tuyệt đối** (đúng byte) và **là file hợp lệ** (mở/phát được) | 24-09: bộ ảnh/video upload biên — chọn quy ước **1MB = 1.048.576 byte (MiB)** |
| Muốn agent **tự xử lý sự cố git** khi được nhờ, nhưng thao tác viết lại lịch sử phải **xin đồng ý** trước | 30-09: push bị chặn do file > 100MB |
| Khi đổi quy tắc: sửa **RULE trước → SKILL → COMMAND** sau cùng. Rule chung để ở `CLAUDE.md` | Ghi trong `noteHoai.txt` |
| Muốn kiến thức tích luỹ được **lưu trong repo** (`memories/`) để phiên sau đọc lại | 07-10-2026 — chính yêu cầu tạo thư mục này |

## Ghi chú xưng hô

User chưa nói cách xưng hô mong muốn. Dùng "bạn" trung tính; không đoán theo tên.
