# Quy trình lệnh theo bước (user đang học & dùng)

> Tóm từ `noteHoai.txt` của user. Danh sách đầy đủ các lệnh + mô tả: mục 10 của `CLAUDE.md`. File này chỉ ghi **thứ tự user quen dùng** và tên lệnh user hay gõ sai.

| Bước | Việc | Lệnh đúng | User hay gõ |
|---|---|---|---|
| B1 | Khám phá hệ thống (UI / URL / tài liệu) | `/discover-system` | `/discovery` |
| B2 | Phân tích requirement | `/analyze-requirement-document` | `/analyze-requiment-doccument` |
| B3 | Cập nhật requirement, giải AMB (AMB chưa chốt → lấy giá trị gợi ý user đã chốt) | `/update-requirements-from-ticket` | `/update-requiment-form-tiket` |
| B4 | Tài liệu đổi → cập nhật TC | `/update-testcases-from-impact` (Mode PLAN rồi APPLY) | `/update-TC-form-impact` |
| B5 | Lập kế hoạch kiểm thử | `/generate-master-test-plan` | |
| B6 | Sinh TC (Markdown, khung 4 vòng) | `/generate-testcases-from-requirements` (QUICK, mặc định `GỘP`) hoặc `/generate-testcases-manual-rbt` | |
| B7 | Review TC | `/review-testcases` (REVIEW / FIX) | |
| B8 | Thực thi TC trên browser | `/execute-test-cases` | |
| B9 | Log bug | `/create-bug-report` (hoặc `/analyze-test-report`) | `/analyze-bug-report` |
| B10 | Retest | `/retest-fixed-bugs` (RETEST / FULL) | `/retest-fixed-bug` |
| B11–B15 | Vòng delta: ticket → update REQ → update TC (PLAN) → execute TC impact → bug → retest | như trên | |

**Ngoài chuỗi trên — dự án thật (Tammi, F2C Excel):** `/generate-testcases-srs-excel` (SRS + Figma + file TC mẫu → Excel riêng). Xem [07_ky-thuat-viet-tc/tc-excel-theo-file-mau.md](../07_ky-thuat-viet-tc/tc-excel-theo-file-mau.md).

## Mẫu tham số user hay dùng (ví dụ thật)

```
/execute-test-cases
File TC: docs/testcases/login/TEST_CASES_LOGIN_SUMMARY.md
Phạm vi: chỉ CRM_LOGIN_TC_025
URL và tài khoản: lấy từ .env
Môi trường dùng chung: CÓ
Build: demo-2026-09-28
```

## Sửa quy tắc / skill

- Thứ tự: **RULE → SKILL → COMMAND**. Rule chung ở `CLAUDE.md`.
- Muốn đổi format TC Markdown → sửa skill `skills-rbt-manual-testing` (B6).
- User hay nói: "cập nhật lại rule, skill để tôi sử dụng cho các lần sau" → sửa vào `.claude/`, và ghi bài học vào `memories/`.
