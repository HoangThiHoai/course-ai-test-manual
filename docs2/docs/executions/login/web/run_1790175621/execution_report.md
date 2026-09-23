# Execution Report — Đăng nhập (`LOGIN`) · Chạy lại TC BLOCKED

| Thông tin | Nội dung |
|---|---|
| Run ID | run_1790175621 |
| Nền tảng | `web` |
| Nguồn TC | [docs2/docs/testcases/login/web/parts/part_01_web_giao_dien_nhap_lieu.md](../../../../testcases/login/web/parts/part_01_web_giao_dien_nhap_lieu.md) |
| Phạm vi | 1 TC — `CRM_LOGIN_TC_008`, chạy lại TC ⚠️ BLOCKED của [`run_1790175154`](../run_1790175154/execution_report.md) · loại 0 TC `@Deprecated` |
| Môi trường | `https://crm.anhtester.com` — Anh Tester Demo |
| Build / Version | Không công bố |
| Tài khoản | `admin@example.com` (Admin) — dùng lại phiên do tester đăng nhập ở `run_1790175154`, còn hiệu lực |
| Trình duyệt | Chromium qua Playwright MCP, headed, viewport `1600×770` |
| Người thực hiện | KunMan (agent hỗ trợ) |
| Bắt đầu → Kết thúc | 23-09-2026 22:00 → 22:01 |
| Môi trường dùng chung? | Có — auto-skip TC phá huỷ đang BẬT |

## 1. Tổng kết

| Trạng thái | Số lượng | Tỷ lệ |
|---|---|---|
| ✅ PASS | 1 | 100% |
| ❌ FAIL | 0 | 0% |
| ⚠️ BLOCKED | 0 | 0% |
| ⏭️ SKIPPED | 0 | 0% |
| **Tổng** | **1** | 100% |

> **Pass rate (không tính SKIPPED):** 1/1 = 100%.
>
> **Gộp với `run_1790175154`** (dải 001–010, lấy kết quả mới nhất của từng TC): PASS 9 · FAIL 1 (TC_004 — `@KnownBug`) · BLOCKED 0 · SKIPPED 0 → pass rate 9/10 = 90%.

## 2. Kết quả từng TC

| TC ID | Test Scenario | Kết quả | Bước fail | Ghi chú |
|---|---|---|---|---|
| CRM_LOGIN_TC_008 | Không có bộ đếm giờ đang chạy thì bấm Logout là đăng xuất ngay, về trang đăng nhập | ✅ PASS | — | **Tiền đề:** tester báo đã tắt 2 timer đang chạy. Agent kiểm lại: danh sách đồng hồ ghi `No started timers found` ✅ (đóng danh sách bằng phím `Esc`). Bước 1: menu ảnh đại diện mở ra. Bước 2: **không** có hộp xác nhận, trình duyệt chuyển trang ngay (REQ-31). Bước 3: dừng ở `https://crm.anhtester.com/admin/authentication`, có biểu mẫu đăng nhập, **không** có dải thông báo nào (REQ-32) |

## 3. Chi tiết TC FAIL

_(không có)_

## 4. TC BLOCKED

_(không có)_

## 5. Dữ liệu đã tạo & dọn dẹp

| Dữ liệu | ID | Nơi tạo | Đã xoá? |
|---|---|---|---|
| _(không có)_ | — | — | — |

> Không tạo bản ghi nào. 2 timer bị chặn ở lần chạy trước do **tester** tự dừng — agent không đụng vào. Phiên Admin đã kết thúc ở bước 2 của TC (đăng xuất), trình duyệt đang ở trang đăng nhập.

## 6. Đề xuất bước tiếp theo

- Dải `001`–`010` đã chạy đủ: chỉ còn TC_004 FAIL, là lỗi đã biết (`BUG_login_1787226513_TC004`) — ghi lần tái hiện vào lịch sử bug, không tạo bug mới
- Tài khoản Admin dùng chung dễ bị người khác bật timer: nên xin tài khoản test riêng cho các TC đăng xuất (`008`, `031`, `056`, `057`)
- Chạy tiếp `CRM_LOGIN_TC_011` → `022` để phủ hết part 01
