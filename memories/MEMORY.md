# MEMORY — bản đồ bộ nhớ dự án

> **Thứ tự đọc bắt buộc ở mỗi yêu cầu:** `CLAUDE.md` → **file này** → chỉ mở các file chủ đề khớp với việc đang làm (bảng "Làm việc gì → đọc gì" bên dưới).
> Không mở hết thư mục — chọn đúng file, giống chuỗi 3 tầng của `docs/`.
> Cập nhật lần cuối: 07-10-2026.

## Làm việc gì → đọc gì

| Khi user yêu cầu… | Đọc |
|---|---|
| **Bất kỳ việc gì** | [01_nguoi-dung/ho-so-va-cach-lam-viec.md](01_nguoi-dung/ho-so-va-cach-lam-viec.md) |
| Viết / bổ sung TC **Tammi gói cước** (CMS, Web OA) | [04 tổng quan & nguồn](04_he-thong-tammi-goi-cuoc/tong-quan-va-nguon.md) → [TC đã viết & quy ước ID](04_he-thong-tammi-goi-cuoc/tc-da-viet-va-quy-uoc-id.md) → file AMB của đúng UC → [07 TC Excel theo file mẫu](07_ky-thuat-viet-tc/tc-excel-theo-file-mau.md) |
| Viết TC từ **SRS + Figma + Google Sheet** (bất kỳ dự án) | [07 TC Excel theo file mẫu](07_ky-thuat-viet-tc/tc-excel-theo-file-mau.md) · [03 trình duyệt/Figma](03_moi-truong-cong-cu/trinh-duyet-figma-playwright.md) · [03 Python/Excel](03_moi-truong-cong-cu/python-excel-tren-may.md) |
| Việc trên **F2C / PIFA** (QLĐH, ORDBUY/ORDSEL/ORDADM, QLDH mobile, TN) | [05 tổng quan F2C](05_he-thong-f2c-pifa/tong-quan.md) |
| Việc trên **Perfex CRM** (login, customers… — bài thực hành) | [06 tổng quan Perfex](06_he-thong-perfex-crm/tong-quan.md) · [02 quy trình lệnh](02_repo-va-quy-trinh/quy-trinh-lenh-theo-buoc.md) |
| Chạy chuỗi lệnh khoá học (discover → REQ → TC → execute → bug → retest) | [02 quy trình lệnh theo bước](02_repo-va-quy-trinh/quy-trinh-lenh-theo-buoc.md) |
| **Git** (commit, push, lỗi push) | [02 git & file lớn](02_repo-va-quy-trinh/git-push-va-file-lon.md) · [02 bảo mật .env/.gitignore](02_repo-va-quy-trinh/bao-mat-env-gitignore.md) |
| Sinh **dữ liệu test** file upload / giá trị biên | [07 dữ liệu test file upload](07_ky-thuat-viet-tc/du-lieu-test-file-upload.md) |
| Dùng **Playwright MCP / trình duyệt / Figma** | [03 trình duyệt · Figma · Playwright](03_moi-truong-cong-cu/trinh-duyet-figma-playwright.md) |
| **Chạy test xong / có summary report mới** → gửi Slack | [03 Slack notify](03_moi-truong-cong-cu/slack-notify.md) + `CLAUDE.md` mục "📣 Gửi report lên Slack" |
| Sửa / xem **web viewer** (`scripts/*-viewer`) | [03 execution viewer](03_moi-truong-cong-cu/execution-viewer.md) |
| Không rõ repo có gì / hệ thống nào | [02 tổng quan repo](02_repo-va-quy-trinh/tong-quan-repo.md) |
| Muốn biết lần trước làm tới đâu, còn treo gì | [08 nhật ký phiên](08_nhat-ky-phien/nhat-ky-phien.md) |

## Cây thư mục

```
memories/
├── MEMORY.md                                ← file này (map)
├── 01_nguoi-dung/
│   └── ho-so-va-cach-lam-viec.md            ← user là ai · cách làm việc mong muốn (feedback)
├── 02_repo-va-quy-trinh/
│   ├── tong-quan-repo.md                    ← repo chứa gì · 3 hệ thống · file đáng chú ý
│   ├── quy-trinh-lenh-theo-buoc.md          ← B1–B15 · tên lệnh user hay gõ sai
│   ├── git-push-va-file-lon.md              ← sự cố push 30-09 · nhánh backup
│   └── bao-mat-env-gitignore.md             ← ⚠️ .env đang bị commit · .gitignore rỗng
├── 03_moi-truong-cong-cu/
│   ├── trinh-duyet-figma-playwright.md      ← đọc Figma · Playwright MCP hay rớt · Google link
│   ├── python-excel-tren-may.md             ← encoding · Excel bị khoá khi mở
│   ├── execution-viewer.md                  ← thay đổi chưa commit của viewer
│   └── slack-notify.md                      ← gửi report Slack · trạng thái cấu hình webhook
├── 04_he-thong-tammi-goi-cuoc/
│   ├── tong-quan-va-nguon.md                ← link SRS/Figma/Sheet ĐÚNG · luồng nghiệp vụ
│   ├── tc-da-viet-va-quy-uoc-id.md          ← các file Excel · số TC · bảng đổi ID
│   ├── amb-cms-quan-ly-don-hang.md      ← 24 AMB CMS Quản lý đơn hàng
│   ├── amb-uc4-ban-hanh.md                  ← 10 AMB mới + AMB cũ còn hiệu lực
│   ├── amb-uc1-cai-dat-bang-bo-loc.md       ← 8 AMB · giả định bảng quyết định
│   └── amb-uc-thanh-toan-goi-cuoc.md        ← 36 AMB · UC chưa viết TC
├── 05_he-thong-f2c-pifa/
│   └── tong-quan.md                         ← namespace _f2c · QLDH mobile Excel · TN
├── 06_he-thong-perfex-crm/
│   └── tong-quan.md                         ← docs vs docs2 · vai trò · năng lực QA
├── 07_ky-thuat-viet-tc/
│   ├── tc-excel-theo-file-mau.md            ← bài học dùng skill SRS-Excel
│   └── du-lieu-test-file-upload.md          ← quy ước MiB · cách sinh file hợp lệ
└── 08_nhat-ky-phien/
    └── nhat-ky-phien.md                     ← mỗi phiên 1 dòng · việc còn treo
```

## ⏳ Việc đang treo (tóm tắt — chi tiết trong từng file)

1. ⚠️ `.env` đang được git theo dõi và đã push; `.gitignore` rỗng → chờ user đồng ý xử lý.
2. Bản nháp Tammi UC1 Cài đặt bảng + Bộ lọc (117 TC) chờ user review · đã commit 07-10 · README danh mục chưa cập nhật.
3. File thừa `docs/testcases/goi-cuoc/web/TCs_GOICUOC_Banhanh_UC4_Bosung.xlsx` cần xoá (đã gộp).
4. AMB Tammi (UC4, UC1, UC Thanh toán) chưa có câu trả lời BA.
5. UC Thanh toán / Bán hàng gói cước chưa viết TC, chưa đọc Figma trang Thanh toán.
6. Nhánh `backup/before-remove-large-files` còn tồn tại.
7. Slack chưa cấu hình: `.env` chưa có `SLACK_WEBHOOK_URL` → report chưa gửi tự động được.
8. Cập nhật skill `skills-srs-excel-testcases` theo sheet Quanlykho đã commit 07-10 · `docs/testcases/goi-cuoc/web/src/build_quanlykho_format.py` nay trùng chức năng với script skill — chờ user quyết giữ/xoá.
9. Bộ TC **CMS Quản lý đơn hàng** (289 TC, 07-10) chờ user review · 24 AMB chưa gửi BA · đã commit + push 07-10 · README danh mục chưa cập nhật.

## Quy tắc ghi bộ nhớ

- **Khi nào ghi:** cuối mỗi việc có kết quả (TC mới, AMB mới, quyết định của user/BA, sự cố công cụ, feedback về cách làm). Thêm 1 dòng vào [nhật ký phiên](08_nhat-ky-phien/nhat-ky-phien.md) + cập nhật file chủ đề.
- **Ghi vào đâu:** đúng thư mục chủ đề; hệ thống mới → thư mục mới `NN_he-thong-<ten>/` và 1 dòng ở bảng "Làm việc gì → đọc gì".
- **Một file một chủ đề**, ngắn. File vượt ~150 dòng → tách theo UC/chức năng.
- Sửa tại chỗ khi thông tin cũ sai (AMB đã được BA trả lời → ghi câu trả lời, không xoá dòng). Cập nhật mục "Việc đang treo".
- **Không chép lại** thứ đã có trong `CLAUDE.md`, `.claude/skills/`, `docs/` — chỉ trỏ link + ghi điều không suy ra được từ đó.
- 🔒 **Không** ghi mật khẩu, token, cookie, giá trị `.env` — chỉ ghi tên khoá.
- Ngày viết `DD-MM-YYYY`.
