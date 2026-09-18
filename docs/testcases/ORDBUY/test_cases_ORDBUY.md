# Test Cases — ORDBUY (Quản lý đơn hàng — App Buyer) — tổng 62 TC · 4 part

> Phạm vi: đúng delta **luồng Trả hàng/Hoàn tiền Ver 3.0.0** đã phân tích ở `analysis_SRS-ORDBUY-V3.md` — REQ-F2C-ORDBUY-01 → 33. KHÔNG bao gồm các mục khác của module `ORDBUY` chưa được phân tích.

| Thông tin | Nội dung |
|---|---|
| Nguồn requirement | [analysis_SRS-ORDBUY-V3.md](../../requirements/_f2c/ORDBUY/analysis/analysis_SRS-ORDBUY-V3.md) |
| Mode sinh TC | QUICK (`/generate-testcases-from-requirements`) |
| Độ hạt | **GỘP** (mặc định) |
| Mức rủi ro · độ sâu | `Cao` → **Đầy đủ**. Căn cứ: đụng tiền hoàn tiền · có thao tác không hồi lại (Huỷ yêu cầu, Gửi yêu cầu) · là cổng vào phụ thuộc 2 module khác (`ORDSEL`, `ORDADM`). **Nâng lên khi:** không áp dụng — đã ở mức cao nhất |
| TC ID | `F2C_ORDBUY_TC_001` → `F2C_ORDBUY_TC_062` |
| Ngày sinh | 2026-09-18 |

## Assumptions (ASM)

| Mã | Điểm chưa rõ | Giả định đã áp dụng | TC bị ảnh hưởng |
|---|---|---|---|
| `ASM-01` | Module `ORDBUY` (namespace `_f2c/`, mode DOC) **không có bất kỳ ảnh evidence nào** — chưa từng khảo sát UI thật, SRS chỉ có 1 link Figma không đọc được trực tiếp | Toàn bộ TC thuộc 4 nhóm bắt buộc evidence (bố cục/thứ tự, nhãn nguyên văn, giá trị mặc định, định dạng hiển thị) viết theo đúng nội dung SRS (vốn trích khá chi tiết nhãn nguyên văn) nhưng gắn `@NeedsVerify` — phải đối chiếu lại UI thật trước khi giao automation | Toàn bộ TC nhóm V1 UI cơ bản + phần lớn TC hiển thị/label ở V2 (xem cột Tags) |
| `ASM-02` | Nền tảng UI (web responsive hay mobile app) của "App Buyer" chưa xác định — SRS gọi là "App" nhưng chưa rõ web hay native | Viết TC theo giả định **web responsive** (nhất quán với công cụ Playwright của repo); nhánh V4 Compatibility/Responsive chấm `➖` vì chưa có hệ thống thật để xác nhận nền tảng và chốt breakpoint | TC_059 (Part 4) |

## Bản đồ tài liệu

| File | Nhóm chức năng | Số TC | TC ID range | REQ bao phủ |
|---|---|---|---|---|
| [Part 1](parts/part_01_danh_sach.md) | Danh sách đơn hàng (1.3.1) | 12 | TC_001–TC_012 | REQ-01 → 12 |
| [Part 2](parts/part_02_chi_tiet_don_hang.md) | Chi tiết đơn hàng — 3 trạng thái (1.3.2.4/5/6) | 13 | TC_013–TC_025 | REQ-13 → 21 |
| [Part 3](parts/part_03_form_yeu_cau.md) | Form Yêu cầu Trả hàng/Hoàn tiền (1.3.3) | 15 | TC_026–TC_040 | REQ-22 → 29 |
| [Part 4](parts/part_04_hoan_tien_technical.md) | Chi tiết hoàn tiền (1.3.4) + Technical (V3) + Non-functional (V4) | 22 | TC_041–TC_062 | REQ-30 → 33 |

**Tổng: 62 TC · 84 case (tính cả biến thể gộp)** — 10 TC dùng Bảng biến thể (32 biến thể), 52 TC còn lại 1 case/TC.

## Bảng Đối Soát Coverage (toàn module)

| REQ ID | Mô tả ngắn | Số TC | TC IDs | Đủ Positive/Negative/Boundary? |
|---|---|---|---|---|
| REQ-F2C-ORDBUY-01 | Tab "Đã hoàn thành" — điều kiện lọc | 1 | TC_004 (3 biến thể) | ✅ |
| REQ-F2C-ORDBUY-02 | Tab "Trả hàng" — điều kiện lọc | 1 | TC_005 (2 biến thể) | ✅ |
| REQ-F2C-ORDBUY-03 | Nhãn trạng thái theo tab | 1 | TC_001 | ✅ (Bảng kiểm) |
| REQ-F2C-ORDBUY-04 | CTA "Huỷ yêu cầu hoàn tiền" | 1 | TC_001 | ✅ (Bảng kiểm) |
| REQ-F2C-ORDBUY-05 | CTA "Đánh giá"/"Xem đánh giá" | 1 | TC_001 | ✅ (Bảng kiểm) |
| REQ-F2C-ORDBUY-06 | Text đổi theo số lần Buyer tự huỷ | 3 | TC_006, TC_012, TC_038 | ✅ |
| REQ-F2C-ORDBUY-07 | Text đổi theo số lần bị từ chối | 3 | TC_007, TC_012, TC_038 | ✅ |
| REQ-F2C-ORDBUY-08 | Field "Đang chờ xử lý" — hạn 24h | 1 | TC_008 | ✅ |
| REQ-F2C-ORDBUY-09 | Field "Chọn phương thức trễ nhất" — hạn 24h | 1 | TC_009 | ✅ (Boundary) |
| REQ-F2C-ORDBUY-10 | Field "Chờ hoàn tiền" — hạn 10 ngày | 1 | TC_010 | ✅ |
| REQ-F2C-ORDBUY-11 | Field "Hoàn tiền thành công" | 1 | TC_011 | ⚪ BLOCKED (AMB-02) |
| REQ-F2C-ORDBUY-12 | Field "Hoàn tiền thất bại" | 1 | TC_011 | ⚪ BLOCKED (AMB-02) |
| REQ-F2C-ORDBUY-13 | 3 nhánh nội dung theo số lần yêu cầu | 2 | TC_015, TC_016 (3 biến thể) | ✅ |
| REQ-F2C-ORDBUY-14 | Onclick điều hướng | 1 | TC_015 | ✅ |
| REQ-F2C-ORDBUY-15 | Tái sử dụng field từ 1.3.2.1/2 | 1 | TC_013 | ✅ (Bảng kiểm) |
| REQ-F2C-ORDBUY-16 | Nội dung mô tả — Đã hoàn thành | 1 | TC_017 (2 biến thể) | ✅ |
| REQ-F2C-ORDBUY-17 | 5 mốc thời gian, mốc mới | 2 | TC_013, TC_018 | ✅ |
| REQ-F2C-ORDBUY-18 | Button "Mua lại" | 1 | TC_019 | ✅ (Positive — điều hướng, không có negative áp dụng) |
| REQ-F2C-ORDBUY-19 | Button "Đánh giá" | 1 | TC_020 | ✅ (Positive) |
| REQ-F2C-ORDBUY-20 | 4 trạng thái con + mốc ngày | 4 | TC_014, TC_021, TC_022, TC_023 | ✅ (2 trạng thái cuối ⚪ BLOCKED) |
| REQ-F2C-ORDBUY-21 | Nội dung theo trạng thái con | 2 | TC_024 (3 biến thể), TC_025 | ✅ (⚪ BLOCKED một phần) |
| REQ-F2C-ORDBUY-22 | Truy cập màn Yêu cầu Trả hàng/Hoàn tiền | 7 | TC_026, 027, 028, 030, 038, 050, 051 | ✅ |
| REQ-F2C-ORDBUY-23 | Field "Hoàn tiền vào" | 2 | TC_029, TC_030 | ✅ |
| REQ-F2C-ORDBUY-24 | Field "Tổng tiền hoàn" | 1 | TC_031 | ✅ |
| REQ-F2C-ORDBUY-25 | Field "Lý do" | 2 | TC_028, TC_032 | ✅ |
| REQ-F2C-ORDBUY-26 | Field "Mô tả" | 2 | TC_028, TC_033 (5 biến thể) | ✅ |
| REQ-F2C-ORDBUY-27 | Field "Hình ảnh & video" | 4 | TC_028, 034 (6 biến thể), 035, 039 | ✅ |
| REQ-F2C-ORDBUY-28 | Field "Email cập nhật tình hình" | 1 | TC_036 | ✅ |
| REQ-F2C-ORDBUY-29 | Button "Gửi yêu cầu" | 4 | TC_028, 037, 040, 052 | ✅ |
| REQ-F2C-ORDBUY-30 | Progress Bar 4 mốc | 3 | TC_041, TC_042, TC_043 | ✅ (2 mốc cuối ⚪ BLOCKED) |
| REQ-F2C-ORDBUY-31 | Button "Huỷ yêu cầu" | 3 | TC_044, TC_045, TC_050 | ✅ |
| REQ-F2C-ORDBUY-32 | "Chọn phương thức trả hàng" | 3 | TC_046, TC_047, TC_048 | ✅ |
| REQ-F2C-ORDBUY-33 | "Hướng dẫn trả hàng" | 1 | TC_049 | ✅ (Positive) |

**33/33 REQ có ≥1 TC — không có dòng 🔴.**

## Bảng Đối Soát Evidence

| Ảnh evidence | Màn hình / trạng thái | TC dựa vào | Đầy đủ? |
|---|---|---|---|
| *(không có)* | Toàn bộ 6 màn hình của luồng Trả hàng/Hoàn tiền | Mọi TC nhóm UI cơ bản/hiển thị (TC_001, 013, 014, 026, 041, và các TC hiển thị nội dung khác) | 🔴 **THIẾU HOÀN TOÀN** — mode DOC, module `ORDBUY` chưa từng khảo sát UI thật. TC vẫn viết theo nhãn nguyên văn trích từ SRS, nhưng **toàn bộ gắn `@NeedsVerify`** |

> **Khuyến nghị:** chạy `/discover-system` mode HYBRID (hoặc riêng recon UI) ngay khi có URL/tài khoản Buyer thật, đối chiếu lại toàn bộ TC gắn `@NeedsVerify` trước khi bàn giao automation.

## Đối soát loại kiểm thử (4 vòng) — tổng hợp

Chi tiết từng nhánh nằm trong bảng cuối mỗi part. Tổng hợp mức module:

| Vòng | Đã sinh đủ? | Ghi chú |
|---|---|---|
| V1 Smoke | ✅ | Đủ 6 nhánh cho từng màn hình chính (Part 1–4) |
| V2 Functional | ✅ | Đủ nhánh có điều kiện kích hoạt; 2 nhánh liên quan trạng thái Hoàn tiền thành công/thất bại `⚪ BLOCKED` (AMB-02) |
| V3 Technical | ✅ | `Permission`/`Database`/`Integration`/`Logging` chấm `➖` có lý do (Part 4); `Security`/`API` có TC đầy đủ |
| V4 Non-functional | ✅ | `Accessibility`/`Localization` có TC; `Compatibility`/`Performance`/`Regression`/`E2E` chấm `➖` có lý do (Part 4) |

## Rà soát đặc tính chất lượng (ISO/IEC 25010:2023)

| Đặc tính | Trạng thái | TC ID / Lý do |
|---|---|---|
| Functional Suitability | ✅ Có TC | TC_001–TC_049 (toàn bộ luồng chức năng) |
| Performance Efficiency | ➖ Ngoài phạm vi | Không có công cụ đo tải — chưa có hệ thống thật, đội Hạ tầng đảm nhận khi có |
| Compatibility | ➖ Ngoài phạm vi | Chưa có hệ thống thật để chốt trình duyệt/breakpoint — QA lead, rà lại khi có URL thật |
| Interaction Capability | ✅ Có TC | TC_037 (nút enable/disable), TC_032 (cảnh báo required), TC_057 (bàn phím) |
| Reliability | ✅ Có TC | TC_040 (double-submit) — chưa có TC session timeout/mất mạng giữa chừng (module chưa có hệ thống thật để mô phỏng) |
| Security | ✅ Có TC | TC_050, TC_051 (IDOR, truy cập chưa đăng nhập) |
| Maintainability | ➖ Không áp dụng | Đặc tính của mã nguồn, không kiểm bằng manual TC |
| Flexibility | ➖ Ngoài phạm vi | Responsive/đổi ngôn ngữ chưa chốt được vì chưa có hệ thống thật — QA lead |
| Safety | ✅ Có TC | TC_045 (popup xác nhận trước khi Huỷ yêu cầu — thao tác không hồi lại) |

## Quy trình tiếp theo

| Tình huống | Workflow |
|---|---|
| Có URL/tài khoản Buyer thật | `/discover-system` mode HYBRID — đối chiếu lại toàn bộ TC gắn `@NeedsVerify`, đặc biệt 4 nhóm UI cơ bản |
| Chuyển sang automation | `/generate-automation-from-testcases` — ưu tiên TC không bị `⚪ BLOCKED`/`@NeedsVerify` |
| Cần review chất lượng bộ TC | `/review-testcases` |
| Cần checklist smoke rút gọn | `/generate-checklist-test` |
| CMS import (AMB-02) đã được xây | Bổ sung TC cho REQ-11, REQ-12, REQ-20 (2 trạng thái cuối), REQ-21 (2 nhánh cuối), REQ-30 (2 mốc cuối) — hiện đang `⚪ BLOCKED` |
