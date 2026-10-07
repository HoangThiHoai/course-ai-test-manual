# Trình duyệt · Figma · Playwright MCP — kinh nghiệm thực tế

## Playwright MCP

- Hay **không kết nối được** (`CONNECTION_CLOSED`) — xảy ra ở các phiên 30-09 và 07-10-2026. Cách xử lý: báo user **khởi động lại Claude Code**; trong lúc chờ có thể dùng trình duyệt tích hợp của app (Claude Browser) để đọc trang.
- Cấu hình: `.mcp.json` → `--viewport-size=1600,770` + `.claude/playwright-mcp-config.json` (`--window-position=-3,0`). Không `browser_resize` vượt cửa sổ.

## Figma

- Figma vẽ bằng **canvas WebGL** → không đọc được text qua DOM/accessibility tree, chỉ đọc bằng **ảnh chụp**.
- Cửa sổ trình duyệt bị **ẩn / thu nhỏ** → Figma ngừng vẽ → mọi lần chụp **timeout**. Nhờ user giữ cửa sổ hiển thị.
- File Tammi rất lớn, tải chậm; mở thẳng node bằng `node-id` trong URL.
- Chưa đăng nhập thì chỉ xem chế độ khách. **User thường đã đăng nhập Figma sẵn** trên trình duyệt — dùng phiên đó, đừng kết luận "không truy cập được".
- 3 cách lấy nội dung Figma, theo độ đầy đủ tăng dần:
  1. Zoom + chụp từng frame trên trình duyệt (chậm).
  2. User **export PNG** các frame → đưa đường dẫn (nhanh, chính xác).
  3. User tạo **Figma personal access token**, tự dán vào `.env` (VD `FIGMA_TOKEN=`) → gọi REST API lấy nguyên văn text. Agent không tự nhập token.
- Thứ tự ưu tiên khi viết TC: ảnh design nhúng trong SRS trước, **Figma để xác nhận / phát hiện chỗ design khác SRS** (nút thừa như "Nhân bản gói", nút Xóa sai trạng thái…).

### Đọc Figma bằng trình duyệt tích hợp (Claude Browser) — 07-10-2026

- Agent **không được tự nhập mật khẩu** Figma (quy tắc an toàn) dù user đưa tài khoản → nhờ user tự đăng nhập trong pane; user đồng ý và làm ngay.
- Pane chỉ ~800px: thu sidebar (icon cạnh tên file), chọn frame → `shift+2` (zoom to selection) → `Escape` để ẩn panel phải. Đặt zoom bằng menu `%` ở góc phải (gõ số + Enter). Phím `-`, `ctrl+\` không ăn; cuộn chuột pan rất chậm → dùng **Hand tool** (toolbar) + kéo.
- Canvas vẽ trễ 1 nhịp: chờ 2–3 s rồi mới chụp, nếu ảnh giống lần trước thì chụp lại.
- Zoom 70–80% đọc được bảng web 1440px; màn mobile đọc tốt ở ~40%.
- Không `navigate` lại URL Figma khi đang ở trong file — reload toàn bộ file mất ~20 s.

## Google Docs / Sheets

- Tải bằng script `fetch_sources.py` của skill `skills-srs-excel-testcases` (cần chia sẻ "Bất kỳ ai có đường liên kết").
- **Kiểm tra nội dung tải về có đúng nghiệp vụ không** trước khi làm — đã từng nhận nhầm link (SRS PIFA thay vì Tammi). Tìm từ khoá nghiệp vụ trong file; không khớp → dừng hỏi user.
- `gid` trong link Sheet = sheet user đang xem → ưu tiên soi sheet đó. Tab Docs (`tab=t.xxx`) → xác định đúng tab.
