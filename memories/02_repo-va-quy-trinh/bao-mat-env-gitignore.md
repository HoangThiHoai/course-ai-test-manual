# Bảo mật: `.env` đang bị commit · `.gitignore` rỗng

> Phát hiện 07-10-2026 khi gom bộ nhớ. **Chưa xử lý** — chờ user quyết.

## Thực trạng

- `.gitignore` ở gốc **rỗng** (1 byte). Commit `c21d93f` "Create .gitignore" (24-09) không có nội dung hiệu lực.
- `.env` (`BASE_URL`, `EMAIL_ADMIN`, `PASSWORD_ADMIN`) **được git theo dõi từ commit `30542f5` (15-09-2026)** và đã push lên GitHub. CLAUDE.md lại ghi ".env đã .gitignore" — **không đúng thực tế**.
- `.playwright-mcp/` (console log của Playwright MCP) cũng đang được commit.
- `test-data/` (file upload dung lượng lớn) từng bị commit → gây sự cố push (xem [git-push-va-file-lon.md](git-push-va-file-lon.md)).
- `reports/`, `.allure/`, `.claude/settings.local.json` chưa được chặn.

## Hướng xử lý đề xuất (cần user đồng ý)

1. Điền `.gitignore`: `.env`, `.playwright-mcp/`, `test-data/`, `reports/`, `.allure/`, `.claude/settings.local.json`, `__pycache__/`.
2. `git rm --cached .env` và `git rm -r --cached .playwright-mcp` (không xoá file trên máy).
3. Mật khẩu đã lên lịch sử git thì **coi như lộ** → đổi mật khẩu tài khoản (nếu là tài khoản dùng thật, không chỉ demo công khai). Sửa file không xoá được lịch sử.

## Quy tắc cho agent

- **Không bao giờ** in giá trị `.env` ra chat, log, `docs/` hay `memories/` — chỉ ghi **tên khoá**.
- Trước khi commit: kiểm `git status` không có `.env`, `test-data/`, ảnh chứa dữ liệu khách hàng.
