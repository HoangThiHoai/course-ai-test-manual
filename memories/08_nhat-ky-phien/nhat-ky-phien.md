# Nhật ký các phiên làm việc

> Mỗi phiên một dòng: ngày · việc · kết quả · việc còn treo. Phiên mới **thêm dòng ở cuối**, chi tiết đưa vào file chủ đề tương ứng.
> Dữ liệu trước 24-09-2026 không còn transcript trên máy — chỉ suy từ git log và `docs/`.

| Ngày | Session | Việc | Kết quả | Còn treo |
|---|---|---|---|---|
| 26-08 → 23-09-2026 | (không còn transcript) | Học khoá: Perfex CRM (`docs2/`), F2C/PIFA (`_f2c/`, ORDBUY 62 TC), QLĐH mobile Excel 1.3.3/1.3.4, TN Hoa hồng giới thiệu | Theo git log & danh mục `docs/` | — |
| 24-09-2026 | (git) | TC Tammi gói cước UC1–UC4 (Excel, format Quanlykho) | Commit `034ddf9`, `b4b3ae7`, `578090e` | UC4 chưa đối chiếu Figma (đã làm 30-09) |
| 24-09-2026 | `08a448a6` | Sinh 16 file ảnh/video upload theo biên | Đúng byte, file hợp lệ → [07/du-lieu-test-file-upload.md](../07_ky-thuat-viet-tc/du-lieu-test-file-upload.md) | — |
| 30-09-2026 | `32a3a1f4` | Bắt đầu TC UC Thanh toán/Bán hàng gói cước (Web OA) | User **dừng**: chưa đọc Figma. Ra 36 AMB → [04/amb-uc-thanh-toan-goi-cuoc.md](../04_he-thong-tammi-goi-cuoc/amb-uc-thanh-toan-goi-cuoc.md) | Chưa viết TC; chưa đọc Figma trang Thanh toán |
| 30-09-2026 | `e82bcd49` | Làm lại với link SRS đúng → bổ sung 30 TC UC4 Ban hành đối chiếu Figma → gộp vào file UC3_UC4 (150 TC) | [04/tc-da-viet-va-quy-uoc-id.md](../04_he-thong-tammi-goi-cuoc/tc-da-viet-va-quy-uoc-id.md) · 10 AMB mới | Xoá file thừa `TCs_GOICUOC_Banhanh_UC4_Bosung.xlsx`; BA trả lời AMB |
| 30-09-2026 | `9fa8df75` | Sửa lỗi push (file > 100MB) | Push xong `629320b` → [02/git-push-va-file-lon.md](../02_repo-va-quy-trinh/git-push-va-file-lon.md) | Xoá nhánh backup; điền `.gitignore` |
| 02-10-2026 | `e63a19f1` | Bổ sung TC Cài đặt bảng + Bộ lọc (UC1) từ 8 ảnh chụp | Bản nháp 498 TC (+117), chưa commit → [04/amb-uc1-cai-dat-bang-bo-loc.md](../04_he-thong-tammi-goi-cuoc/amb-uc1-cai-dat-bang-bo-loc.md) | User review bản nháp; cập nhật README danh mục |
| 07-10-2026 | `6ac895eb` | Gom toàn bộ bộ nhớ vào `memories/` + quy tắc đọc trong CLAUDE.md | Tạo thư mục này; phát hiện `.env` đang bị commit | Xử lý `.gitignore`/`.env` (chờ user) |
| 07-10-2026 | `6ac895eb` | Thêm rule gửi report lên Slack sau khi chạy test / có summary report mới | `CLAUDE.md` mục "📣 Gửi report lên Slack" + checklist DoD → [03/slack-notify.md](../03_moi-truong-cong-cu/slack-notify.md) | User thêm `SLACK_WEBHOOK_URL` vào `.env` |
| 07-10-2026 | `ee1d67ec` | Đọc sheet `Quanlykho` (file TC_F2C CMS) → cập nhật skill `skills-srs-excel-testcases` | `tc_writing_rules.md` thêm Format B + checklist web CMS + lỗi file mẫu; `build_tc_excel.py` sửa lỗi dựng sai Format B; SKILL.md, `tcdata_example.py`, command cập nhật → [07/tc-excel-theo-file-mau.md](../07_ky-thuat-viet-tc/tc-excel-theo-file-mau.md) | Chưa commit; quyết định giữ/xoá `build_quanlykho_format.py`; file `.pyc` cache bị theo dõi trong git đã bị xoá |
| 07-10-2026 | `937c1f7c` | `/generate-testcases-srs-excel` CMS Quản lý đơn hàng: đọc SRS mới (Gói cước - Đơn hàng) + Figma CMS + Figma Miniapp (user tự đăng nhập Figma trong pane; Playwright MCP lại rớt) | 289 TC → `TCs_GOICUOC_CMS_Quanlydonhang.xlsx` + 24 AMB → [04/amb-cms-quan-ly-don-hang.md](../04_he-thong-tammi-goi-cuoc/amb-cms-quan-ly-don-hang.md) | User review; BA trả lời AMB; chưa commit, chưa cập nhật README danh mục |
| 07-10-2026 | `937c1f7c` | User yêu cầu commit toàn bộ thay đổi đang treo | 5 commit trên `main` (TC Quản lý đơn hàng · bản nháp UC1 Cài đặt bảng/Bộ lọc · skill SRS-Excel · memories + CLAUDE.md · viewer + noteHoai) | Đã push `a735269..c45e289` |
