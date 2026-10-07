# Perfex CRM (Anh Tester demo) — hệ thống bài tập của khoá học

> Hệ thống **mặc định** của repo, dùng để thực hành chuỗi workflow (`/discover-system` → requirements → TC → execute → bug → retest). URL + tài khoản nằm trong `.env` — hiện chỉ có 3 khoá `BASE_URL`, `EMAIL_ADMIN`, `PASSWORD_ADMIN` (ví dụ trong `noteHoai.txt` nhắc `EMAIL_PM`/`PASSWORD_PM` nhưng **chưa có** trong `.env`). **Không** ghi giá trị ra tài liệu.
> TC ID: `CRM_<MODULE>_TC_<3 số>`. Môi trường **dùng chung: CÓ** → cấm thao tác phá huỷ, dọn dữ liệu test.

## ⚠️ Hai cây tài liệu song song — dễ nhầm

| Thư mục | Là gì | Có gì |
|---|---|---|
| **`docs2/docs/`** | Bộ tài liệu mẫu / bài thực hành đầy đủ theo chuẩn tầng nền tảng (có `README.md` danh mục 23 module) | requirements: `login`, `customers`, `projects`, `camp`, `flight` · executions `login/web/run_*` · bugs `login/web/BUG_login_…_TC004.md` |
| **`docs/`** | Thư mục làm việc chính (chuẩn CLAUDE.md) — trộn nhiều hệ thống | `requirements/_discovery/system_map.md` (Perfex, khảo sát 14-09-2026, mode UI) · `requirements/login/requirements_login.md` (44 REQ, cập nhật 18-09 theo `PO-AMB-20260918`) · `test-plans/test_plan_release_1.0.md` (Draft, 19 ô treo) · **không có** `docs/requirements/README.md` |

Ghi chú `noteHoai.txt` trỏ các ví dụ lệnh vào `docs2\docs\...` (login web). Khi user nói "module login" mà không nói rõ → **hỏi lại docs hay docs2**.

## Đặc điểm đã biết

- 3 vai trò: Admin, Project Manager (đăng nhập `/admin/authentication`) và Customer (`/login`, cổng tách biệt).
- Tài khoản `EMAIL_ADMIN` là staff, **không** phải admin thật (`app.user_is_admin` rỗng). Activity Log trả "Từ chối truy cập".
- Năng lực QA (chốt 11-09-2026): API ❌ · DB ❌ · tích hợp ❌ · nhật ký ❌ · DevTools ✅.
- Không thử sai mật khẩu nhiều lần với tài khoản thật; không gửi Forgot Password với email thật.
- `task.md` ở gốc repo: checklist sinh TC module LOGIN (web) QUICK · GỘP — đã hoàn tất 5 batch (TC_001–053).
