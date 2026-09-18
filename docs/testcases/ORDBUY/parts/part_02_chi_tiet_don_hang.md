# Test Cases — ORDBUY — Part 2: Chi tiết đơn hàng — 3 trạng thái (1.3.2.4 / 1.3.2.5 / 1.3.2.6)

[← Về index](../test_cases_ORDBUY.md) · [← Part 1](part_01_danh_sach.md) · [Part 3 →](part_03_form_yeu_cau.md)

| Nguồn | [analysis_SRS-ORDBUY-V3.md](../../../requirements/_f2c/ORDBUY/analysis/analysis_SRS-ORDBUY-V3.md) |
|---|---|
| Độ hạt | GỘP |
| Mức rủi ro · độ sâu | `Cao` → **Đầy đủ** |
| ⚠️ Evidence | Không có ảnh evidence — mọi TC nhóm UI/hiển thị gắn `@NeedsVerify` |

---

## V1 — Smoke

| TC ID | REQ ID | Module | Risk Level | Test Scenario | Pre-Condition | Test Steps | Test Data | Expected Result | Priority | Automatable | Auto Type | Tags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F2C_ORDBUY_TC_013 | REQ-F2C-ORDBUY-15 | ORDBUY | Medium | Bảng kiểm UI cơ bản — màn Chi tiết đơn hàng "Đã hoàn thành" | Có đơn ở trạng thái Đã hoàn thành | 1. Mở Chi tiết đơn `ORD_R1_20260918`<br>2. Đối chiếu Bảng kiểm | — | **Bảng kiểm:**<br>`1` (REQ-15) Đủ khối: Back, Thông tin vận chuyển, Thông tin nhận hàng, Publisher & sản phẩm, Tổng thanh toán, Hỗ trợ, Chính sách hỗ trợ, Thông tin đặt hàng, An tâm mua sắm<br>`2` (REQ-17) Thông tin đặt hàng có đủ 5 mốc: đặt hàng, thanh toán, ĐVVC lấy hàng, nhận hàng, **hoàn thành đơn**<br>`3` (REQ-18,19) Có nút "Mua lại" và nút "Đánh giá"/"Xem đánh giá" | Critical | Partial | UI | @Smoke @NeedsVerify |
| F2C_ORDBUY_TC_014 | REQ-F2C-ORDBUY-20 | ORDBUY | High | Bảng kiểm UI cơ bản — màn Chi tiết đơn hàng "Trả hàng" | Có đơn ở trạng thái Trả hàng, trạng thái con "Đang chờ xử lý" | 1. Mở Chi tiết đơn `ORD_A_20260918`<br>2. Đối chiếu Bảng kiểm | — | **Bảng kiểm:**<br>`1` Field "Trạng thái xử lý yêu cầu Trả hàng/Hoàn tiền" hiển thị đúng "Đang chờ xử lý" kèm mốc ngày đặt hàng<br>`2` Field "Mô tả trạng thái yêu cầu" (STT9) hiện đúng nội dung của trạng thái con "đang chờ phê duyệt" | Critical | Partial | UI | @Smoke @NeedsVerify |
| F2C_ORDBUY_TC_015 | REQ-F2C-ORDBUY-13 | ORDBUY | Medium | Onclick field "Mô tả trạng thái yêu cầu" ở màn Đã giao điều hướng đúng | Đơn ở trạng thái Đã giao, chưa từng yêu cầu | 1. Mở Chi tiết đơn `ORD_DAGIAO_20260918`<br>2. Bấm vào field "Mô tả trạng thái yêu cầu trả hàng/hoàn tiền" | — | 2. Điều hướng sang màn "Yêu cầu Trả hàng/Hoàn tiền" | High | Yes | UI | @Smoke |

## V2 — Functional

| TC ID | REQ ID | Module | Risk Level | Test Scenario | Pre-Condition | Test Steps | Test Data | Expected Result | Priority | Automatable | Auto Type | Tags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F2C_ORDBUY_TC_016 | REQ-F2C-ORDBUY-13 | ORDBUY | High | Decision Table — 3 nhánh nội dung field "Mô tả trạng thái yêu cầu" ở màn Đã giao | 3 đơn ở 3 tình huống số lần yêu cầu khác nhau | 1. Mở Chi tiết đơn theo từng đơn ở Bảng biến thể<br>2. Đối chiếu nội dung field "Mô tả trạng thái yêu cầu" | `a` chưa từng yêu cầu: `ORD_DAGIAO_20260918`<br>`b` đã yêu cầu 1 lần (huỷ/từ chối): `ORD_HUY1_20260918`<br>`c` đã hết lượt (huỷ/từ chối đủ 2 lần): `ORD_HETLUOT_20260918` | `a` Hiện hạn chót gửi yêu cầu = ngày giao + 5 ngày, format DD/MM/YYYY<br>`b` Hiện lại hạn chót tương tự nhưng format DD/MM (không năm)<br>`c` KHÔNG cho gửi thêm yêu cầu — field/nút liên quan bị khoá hoặc ẩn | High | Yes | UI | @Regression @Boundary |
| F2C_ORDBUY_TC_017 | REQ-F2C-ORDBUY-16 | ORDBUY | Medium | 2 nhánh nội dung field "Mô tả trạng thái yêu cầu" ở màn Đã hoàn thành | 2 đơn: yêu cầu bị huỷ / yêu cầu bị từ chối | 1. Mở Chi tiết đơn theo Bảng biến thể<br>2. Đối chiếu nội dung field<br>3. Bấm vào field | `a` yêu cầu bị huỷ: `ORD_HUY1_20260918`<br>`b` yêu cầu bị từ chối (kèm lý do): `ORD_TUCHOI1_20260918` | `a` Hiện đúng nội dung nhánh "yêu cầu bị huỷ"<br>`b` Hiện đúng nội dung nhánh "yêu cầu bị từ chối" kèm lý do từ chối<br>`a,b` Bấm vào field → điều hướng màn Yêu cầu Trả hàng/Hoàn tiền | High | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_018 | REQ-F2C-ORDBUY-17 | ORDBUY | Medium | Mốc "hoàn thành đơn" chỉ hiện đúng trạng thái Đã hoàn thành | 1 đơn Đã giao (chưa hoàn thành), 1 đơn Đã hoàn thành | 1. Mở Chi tiết đơn "Đã giao", xem "Thông tin đặt hàng"<br>2. Mở Chi tiết đơn "Đã hoàn thành", xem "Thông tin đặt hàng" | `ORD_DAGIAO_20260918`, `ORD_R1_20260918` | 1. Chỉ hiện 4 mốc (đặt hàng, thanh toán, ĐVVC lấy hàng, nhận hàng) — KHÔNG có mốc "hoàn thành đơn"<br>2. Hiện đủ 5 mốc, có "hoàn thành đơn" | Medium | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_019 | REQ-F2C-ORDBUY-18 | ORDBUY | Medium | Button "Mua lại" điều hướng đúng | Đơn ở trạng thái Đã hoàn thành | 1. Mở Chi tiết đơn `ORD_R1_20260918`<br>2. Bấm "Mua lại" | — | 2. Điều hướng sang màn Chi tiết sản phẩm của sản phẩm tương ứng | Medium | Yes | UI | @Regression |
| F2C_ORDBUY_TC_020 | REQ-F2C-ORDBUY-19 | ORDBUY | Low | Button "Đánh giá" điều hướng đúng | Đơn ở trạng thái Đã hoàn thành, chưa đánh giá | 1. Mở Chi tiết đơn `ORD_R1_20260918`<br>2. Bấm "Đánh giá" | — | 2. Điều hướng sang màn Đánh giá sản phẩm (mô tả tại 1.3.5 — ngoài phạm vi TC chi tiết của đợt này) | Low | Yes | UI | @Regression |
| F2C_ORDBUY_TC_021 | REQ-F2C-ORDBUY-20 | ORDBUY | High | State Transition — trạng thái con hợp lệ: Đang chờ xử lý → Chờ hoàn tiền | Yêu cầu đang ở "Đang chờ xử lý", vừa được Seller/Admin phê duyệt (mô phỏng qua API) | 1. Gọi API duyệt yêu cầu cho đơn `ORD_A_20260918`<br>2. Mở lại Chi tiết đơn hàng | — | 2. Trạng thái con chuyển đúng thành "Chờ hoàn tiền", kèm mốc ngày duyệt | High | Partial | API | @Regression @TechCheck |
| F2C_ORDBUY_TC_022 | REQ-F2C-ORDBUY-20 | ORDBUY | High | State Transition — chuyển "Hoàn tiền thành công/thất bại" | Cần Admin import kết quả trên CMS | ⚪ BLOCKED — chờ tính năng CMS import (AMB-02). QA không có tài khoản test CMS Admin | — | Không xác minh được cho tới khi có CMS import | High | No | N/A | @Blocked |
| F2C_ORDBUY_TC_023 | REQ-F2C-ORDBUY-20 | ORDBUY | Medium | State Transition — chặn chuyển tắt "Đang chờ xử lý" → "Chờ hoàn tiền" khi CHƯA được duyệt | Yêu cầu chưa được duyệt | 1. Gọi API cố tình chuyển trạng thái đơn `ORD_A_20260918` sang "Chờ hoàn tiền" khi chưa có hành động duyệt | — | 1. Hệ thống từ chối/báo lỗi, trạng thái vẫn giữ nguyên "Đang chờ xử lý" | Medium | Partial | API | @Regression @TechCheck |
| F2C_ORDBUY_TC_024 | REQ-F2C-ORDBUY-21 | ORDBUY | Medium | Nội dung mô tả STT9 đúng theo từng trạng thái con (màn Trả hàng) | 3 đơn ở 3 trạng thái con khác nhau (2 trạng thái cuối BLOCKED) | 1. Mở Chi tiết đơn theo Bảng biến thể<br>2. Đối chiếu nội dung field "Mô tả trạng thái yêu cầu" | `a` đang chờ phê duyệt: `ORD_A_20260918`<br>`b` đã phê duyệt, chờ chọn phương thức: `ORD_CHONPT_20260918`<br>`c` chờ hoàn tiền: `ORD_CHOHOANTIEN_20260918` | `a` Nội dung khớp nhánh "đang chờ phê duyệt"<br>`b` Nội dung khớp nhánh "đã phê duyệt chờ chọn phương thức"<br>`c` Nội dung khớp nhánh "chờ hoàn tiền" | Medium | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_025 | REQ-F2C-ORDBUY-21 | ORDBUY | High | Nội dung mô tả STT9 — 2 nhánh hoàn tiền thành công/thất bại | Cần Admin import kết quả trên CMS | ⚪ BLOCKED — chờ tính năng CMS import (AMB-02) | — | — | High | No | N/A | @Blocked |

## Đối soát loại kiểm thử (4 vòng) — Part 2

| Vòng | Nhánh | Trạng thái | TC ID / Lý do |
|---|---|---|---|
| 1 | UI cơ bản | ✅ | TC_013, TC_014 |
| 1 | Onclick / điều hướng | ✅ | TC_015 |
| 2 | Decision Table nội dung theo số lần yêu cầu | ✅ | TC_016 (1 TC · 3 biến thể) |
| 2 | UI Behavior — 2 nhánh nội dung Đã hoàn thành | ✅ | TC_017 (1 TC · 2 biến thể) |
| 2 | Business Rule — mốc "hoàn thành đơn" | ✅ | TC_018 |
| 2 | Use Case điều hướng | ✅ | TC_019, TC_020 |
| 2 | State Transition | ✅ (một phần `⚪ BLOCKED`) | TC_021, TC_023 ✅ · TC_022 ⚪ |
| 2 | Nội dung theo trạng thái con | ✅ (một phần `⚪ BLOCKED`) | TC_024 (1 TC · 3 biến thể) ✅ · TC_025 ⚪ |
