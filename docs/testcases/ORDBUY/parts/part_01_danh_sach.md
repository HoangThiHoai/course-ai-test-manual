# Test Cases — ORDBUY — Part 1: Danh sách đơn hàng (1.3.1)

[← Về index](../test_cases_ORDBUY.md) · [Part 2 →](part_02_chi_tiet_don_hang.md)

| Nguồn | [analysis_SRS-ORDBUY-V3.md](../../../requirements/_f2c/ORDBUY/analysis/analysis_SRS-ORDBUY-V3.md) |
|---|---|
| Độ hạt | GỘP |
| Mức rủi ro · độ sâu | `Cao` → **Đầy đủ**. Căn cứ: đụng tiền hoàn tiền, cổng vào phụ thuộc Seller/Admin. **Nâng/hạ khi:** không áp dụng — đã ở mức cao nhất |
| ⚠️ Evidence | Module KHÔNG có ảnh evidence (mode DOC) — mọi TC nhóm UI/hiển thị gắn `@NeedsVerify` |

---

## V1 — Smoke

| TC ID | REQ ID | Module | Risk Level | Test Scenario | Pre-Condition | Test Steps | Test Data | Expected Result | Priority | Automatable | Auto Type | Tags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F2C_ORDBUY_TC_001 | REQ-F2C-ORDBUY-03, 04, 05 | ORDBUY | Medium | Bảng kiểm UI cơ bản — nhãn trạng thái và CTA đúng theo tab | Buyer đã đăng nhập; có ≥1 đơn ở tab "Đã hoàn thành" và ≥1 đơn ở tab "Trả hàng" | 1. Mở màn Danh sách đơn hàng<br>2. Chuyển sang tab "Đã hoàn thành"<br>3. Đối chiếu Bảng kiểm mục A trên card đơn<br>4. Chuyển sang tab "Trả hàng"<br>5. Đối chiếu Bảng kiểm mục B trên card đơn | Đơn mẫu: `ORD_F2C_20260918_001` (đã hoàn thành), `ORD_F2C_20260918_002` (đang trả hàng) | **Bảng kiểm — mọi mục phải đạt:**<br>`A1` (REQ-03) Nhãn trạng thái trên card ghi đúng "Đã hoàn thành"<br>`A2` (REQ-05) CTA hiện nút "Đánh giá" (đơn chưa đánh giá) hoặc "Xem đánh giá" (đơn đã đánh giá)<br>`B1` (REQ-03) Nhãn trạng thái trên card ghi đúng "Trả hàng"<br>`B2` (REQ-04) CTA hiện nút "Huỷ yêu cầu hoàn tiền" | Critical | Partial | UI | @Smoke @NeedsVerify |
| F2C_ORDBUY_TC_002 | REQ-F2C-ORDBUY-01, 02 | ORDBUY | High | Mở 2 tab mới, danh sách nạp được và không rỗng khi có dữ liệu | Buyer đã đăng nhập, có đơn hàng hợp lệ cho từng tab | 1. Mở màn Danh sách đơn hàng<br>2. Bấm tab "Đã hoàn thành"<br>3. Quan sát danh sách<br>4. Bấm tab "Trả hàng"<br>5. Quan sát danh sách | — | 2. Tab "Đã hoàn thành" được chọn, có icon/label active<br>3. Danh sách hiển thị đúng các đơn đã giao > 5 ngày không yêu cầu, hoặc yêu cầu đã huỷ/từ chối<br>4. Tab "Trả hàng" được chọn<br>5. Danh sách hiển thị đúng các đơn đang chờ xử lý hoặc đang xử lý hoàn tiền | Critical | Yes | UI | @Smoke |
| F2C_ORDBUY_TC_003 | REQ-F2C-ORDBUY-01, 02 | ORDBUY | Medium | Tab rỗng khi không có đơn thoả điều kiện | Buyer đã đăng nhập, tài khoản test không có đơn nào ở tab "Trả hàng" | 1. Mở màn Danh sách đơn hàng<br>2. Bấm tab "Trả hàng" | Tài khoản `test_ordbuy_empty_20260918@auto.test` | 2. Hiển thị trạng thái rỗng (empty state) đúng ngữ cảnh tab, không hiện lỗi, không crash | Medium | Partial | UI | @Smoke @NeedsVerify |

## V2 — Functional

| TC ID | REQ ID | Module | Risk Level | Test Scenario | Pre-Condition | Test Steps | Test Data | Expected Result | Priority | Automatable | Auto Type | Tags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F2C_ORDBUY_TC_004 | REQ-F2C-ORDBUY-01 | ORDBUY | High | Điều kiện lọc tab "Đã hoàn thành" — quy tắc kết hợp (Decision Table) | 3 đơn hàng ở 3 tình huống khác nhau đã chuẩn bị sẵn | 1. Mở màn Danh sách đơn hàng, tab "Đã hoàn thành"<br>2. Đối chiếu từng đơn theo Bảng biến thể | **Rule R1** đơn giao thành công, quá 5 ngày không yêu cầu: `ORD_R1_20260918`<br>**Rule R2** đơn có yêu cầu nhưng bị Buyer huỷ: `ORD_R2_20260918`<br>**Rule R3** đơn có yêu cầu nhưng bị Seller/Admin từ chối: `ORD_R3_20260918` | Cả 3 đơn `R1`, `R2`, `R3` đều xuất hiện trong tab "Đã hoàn thành" | High | Yes | UI | @Regression |
| F2C_ORDBUY_TC_005 | REQ-F2C-ORDBUY-02 | ORDBUY | High | Điều kiện lọc tab "Trả hàng" đúng 2 trường hợp | 2 đơn hàng chuẩn bị sẵn | 1. Mở màn Danh sách đơn hàng, tab "Trả hàng"<br>2. Đối chiếu từng đơn theo Bảng biến thể | `a` đơn có yêu cầu đang chờ xử lý: `ORD_A_20260918`<br>`b` đơn đã được duyệt, đang xử lý hoàn tiền: `ORD_B_20260918` | Cả 2 đơn `a`, `b` xuất hiện trong tab "Trả hàng"; đơn đã huỷ/từ chối (TC_004) KHÔNG xuất hiện ở tab này | High | Yes | UI | @Regression |
| F2C_ORDBUY_TC_006 | REQ-F2C-ORDBUY-06 | ORDBUY | Medium | Text hiển thị đổi đúng theo số lần Buyer tự huỷ yêu cầu | Đơn đã có lịch sử huỷ yêu cầu | 1. Mở đơn đã huỷ yêu cầu 1 lần, xem card<br>2. Mở đơn đã huỷ yêu cầu 2 lần, xem card | `a` huỷ lần 1: `ORD_HUY1_20260918`<br>`b` huỷ lần 2: `ORD_HUY2_20260918` | `a` Card hiện đúng "Bạn đã huỷ yêu cầu. Còn 1 lần trả hàng/hoàn tiền"<br>`b` Card hiện đúng "Bạn đã huỷ yêu cầu." (không còn số lần) | High | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_007 | REQ-F2C-ORDBUY-07 | ORDBUY | Medium | Text hiển thị đổi đúng theo số lần Sàn/Nhà bán từ chối | Đơn đã có lịch sử bị từ chối | 1. Mở đơn bị từ chối lần 1, xem card<br>2. Mở đơn bị từ chối lần 2, xem card | `a` từ chối lần 1: `ORD_TUCHOI1_20260918`<br>`b` từ chối lần 2: `ORD_TUCHOI2_20260918` | `a` Card hiện đúng "Sàn/Nhà bán đã từ chối yêu cầu. Còn 1 lần trả hàng/hoàn tiền"<br>`b` Card hiện đúng "Sàn/Nhà bán đã từ chối yêu cầu." | High | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_008 | REQ-F2C-ORDBUY-08 | ORDBUY | High | Field "Yêu cầu đang chờ xử lý" — đúng hạn 24h, đúng format, onclick điều hướng | Đơn vừa gửi yêu cầu trả hàng/hoàn tiền lúc 09:00 18/09/2026 | 1. Mở card đơn `ORD_CHO24H_20260918`<br>2. Đối chiếu nội dung field<br>3. Bấm vào field | — | 2. Hiện "Yêu cầu trả hàng/hoàn tiền đang chờ xử lý! 19/09/2026" (hạn = giờ gửi + 24h, format DD/MM/YYYY)<br>3. Điều hướng sang màn Chi tiết hoàn tiền | High | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_009 | REQ-F2C-ORDBUY-09 | ORDBUY | High | Field "Cần chọn phương thức trả hàng trễ nhất" — đúng hạn 24h kể từ duyệt, format DD/MM, tự động chọn khi quá hạn | Đơn vừa được Seller/Admin phê duyệt lúc 09:00 18/09/2026 | 1. Mở card đơn `ORD_CHONPT_20260918` trong 24h sau duyệt<br>2. Đối chiếu nội dung field<br>3. Để quá 24h không chọn phương thức, mở lại card | — | 2. Hiện "Bạn cần chọn phương thức trả hàng trễ nhất vào 19/09" (format DD/MM — KHÔNG có năm, khác REQ-08)<br>3. Hệ thống tự động chọn "Đơn vị vận chuyển đến lấy hàng" tại đúng địa chỉ ĐVVC đã giao hàng trước đó | High | Partial | UI | @Regression @NeedsVerify @Boundary |
| F2C_ORDBUY_TC_010 | REQ-F2C-ORDBUY-10 | ORDBUY | High | Field "Chờ hoàn tiền" — đúng hạn tối đa 10 ngày kể từ ĐVVC lấy hàng thành công, format DD/MM/YYYY | Đơn đã được ĐVVC lấy hàng thành công lúc 00:00 18/09/2026 | 1. Mở card đơn `ORD_CHOHOANTIEN_20260918`<br>2. Đối chiếu nội dung field | — | 2. Hiện "Chờ hoàn tiền 28/09/2026" (= ngày ĐVVC lấy hàng + 10 ngày, format DD/MM/YYYY) | High | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_011 | REQ-F2C-ORDBUY-11, 12 | ORDBUY | High | Field "Hoàn tiền thành công/thất bại" — đúng format DD/MM/YYYY - HH:MM | Cần dữ liệu đơn ở 1 trong 2 trạng thái cuối | ⚪ BLOCKED — chờ tính năng Admin import kết quả hoàn tiền trên CMS (AMB-02). QA không có quyền CSDL/tài khoản CMS để seed trạng thái này (xem `docs/requirements/_f2c/README.md`) | Không seed được | Không xác minh được cho tới khi có CMS import hoặc QA được cấp quyền seed dữ liệu | High | No | N/A | @Blocked |
| F2C_ORDBUY_TC_012 | REQ-F2C-ORDBUY-06, 07 | ORDBUY | High | Giới hạn tối đa 2 lần yêu cầu trên 1 đơn hàng (AMB-05, đã PO xác nhận) | Đơn đã bị huỷ/từ chối đủ 2 lần | 1. Mở đơn `ORD_HETLUOT_20260918` (đã huỷ/từ chối 2 lần)<br>2. Kiểm tra khả năng gửi yêu cầu lần 3 | — | 2. Hệ thống KHÔNG cho gửi thêm yêu cầu Trả hàng/Hoàn tiền lần 3 — nút/field liên quan bị khoá hoặc không hiển thị | High | Partial | UI | @Regression @Boundary |

## Đối soát loại kiểm thử (4 vòng) — Part 1

| Vòng | Nhánh | Trạng thái | TC ID / Lý do |
|---|---|---|---|
| 1 | UI cơ bản | ✅ | TC_001 (1 TC · 4 biến thể) |
| 1 | Display / danh sách nạp được | ✅ | TC_002, TC_003 |
| 2 | Decision Table lọc tab | ✅ | TC_004 (1 TC · 3 biến thể), TC_005 (1 TC · 2 biến thể) |
| 2 | UI Behavior — text đổi theo số lần | ✅ | TC_006, TC_007 (2 TC · 4 biến thể) |
| 2 | Business Rule — 6 field mốc thời gian | ✅ | TC_008–TC_012 |
| 2 | Boundary — giới hạn 2 lần | ✅ | TC_012 |
| 3 | (đặt ở Part 4 — thuộc tính cấp module, không lặp) | — | Xem Part 4 |
| 4 | (đặt ở Part 4) | — | Xem Part 4 |

> Phần Vòng 3/4 gộp chung về **Part 4** để tránh trùng lặp — module chỉ có 1 bộ Permission/Security/Non-functional áp dụng cho toàn `ORDBUY`.
