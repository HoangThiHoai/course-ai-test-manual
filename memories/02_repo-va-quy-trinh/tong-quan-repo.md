# Tổng quan repo `course-ai-test-manual`

- Remote: `https://github.com/HoangThiHoai/course-ai-test-manual.git` · nhánh làm việc `main` · có nhánh local `backup/before-remove-large-files` (xem [git-push-va-file-lon.md](git-push-va-file-lon.md)).
- Mục đích: khung agent QA (`.claude/` rules · skills · commands) + tài liệu kiểm thử của **nhiều hệ thống** trong cùng repo.
- `README.md` ở gốc đã **lỗi thời** (vẫn tả cấu trúc `docs/SRS_Login.md`, `TC/TC.rtf`) — đừng dựa vào nó; đọc `CLAUDE.md`.

## Hệ thống trong repo

| Hệ thống | Loại | Nơi tài liệu | Memory |
|---|---|---|---|
| Perfex CRM (Anh Tester demo) | Bài thực hành khoá học | `docs2/docs/` + một phần `docs/requirements/` | [06_he-thong-perfex-crm](../06_he-thong-perfex-crm/tong-quan.md) |
| Tammi — Quản lý gói cước | Dự án thật, TC Excel | `docs/testcases/goi-cuoc/web/` | [04_he-thong-tammi-goi-cuoc](../04_he-thong-tammi-goi-cuoc/tong-quan-va-nguon.md) |
| F2C / PIFA (Viettel Post) | Dự án thật, Markdown + Excel | `docs/requirements/_f2c/` · `docs/testcases/ORDBUY/` · `docs/testcases/qldh/mobile/` | [05_he-thong-f2c-pifa](../05_he-thong-f2c-pifa/tong-quan.md) |

## Thư mục / file đáng chú ý ở gốc

| Đường dẫn | Ghi chú |
|---|---|
| `noteHoai.txt` | Ghi chú cá nhân của user: thứ tự lệnh B1–B15 (xem [quy-trinh-lenh-theo-buoc.md](quy-trinh-lenh-theo-buoc.md)). File của user — không tự sửa |
| `task.md` | Checklist batch sinh TC LOGIN (đã xong) |
| `claude_legacy/` | Bản rules/skills cũ — không dùng |
| `AI_FULL_FLOW_MANUAL.md` · `AI_FULL_FLOW_AUTOMATION.md` | Tài liệu luồng tổng của khoá học |
| `prompts/prompt_00…32_*.txt` | Prompt mẫu cho từng workflow |
| `.claude/skills/skills-srs-excel-testcases/` | Skill **riêng của user** (SRS + Figma → TC Excel theo file mẫu) — xem [07_ky-thuat-viet-tc](../07_ky-thuat-viet-tc/tc-excel-theo-file-mau.md) |
| `.mcp.json` + `.claude/playwright-mcp-config.json` | Playwright MCP viewport `1600,770`, cửa sổ `--window-position=-3,0` |
| `scripts/*-viewer/bundle.html` | Trang xem TC / execution / bug offline — xem [03_moi-truong-cong-cu/execution-viewer.md](../03_moi-truong-cong-cu/execution-viewer.md) |
| `memories/` | Bộ nhớ dự án (thư mục này) |

## Bảo mật — vấn đề đang tồn tại

Xem [bao-mat-env-gitignore.md](bao-mat-env-gitignore.md): `.gitignore` **rỗng**, `.env` và `.playwright-mcp/` **đang bị git theo dõi**.
