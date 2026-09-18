# Test Cases — ORDBUY — Part 3: Màn hình Yêu cầu Trả hàng/Hoàn tiền (1.3.3)

[← Về index](../test_cases_ORDBUY.md) · [← Part 2](part_02_chi_tiet_don_hang.md) · [Part 4 →](part_04_hoan_tien_technical.md)

| Nguồn | [analysis_SRS-ORDBUY-V3.md](../../../requirements/_f2c/ORDBUY/analysis/analysis_SRS-ORDBUY-V3.md) |
|---|---|
| Độ hạt | GỘP |
| Mức rủi ro · độ sâu | `Cao` → **Đầy đủ** — đây là màn hình ghi dữ liệu tiền hoàn, rủi ro cao nhất module |
| ⚠️ Evidence | Không có ảnh evidence — mọi TC nhóm UI/hiển thị gắn `@NeedsVerify` |

---

## V1 — Smoke

| TC ID | REQ ID | Module | Risk Level | Test Scenario | Pre-Condition | Test Steps | Test Data | Expected Result | Priority | Automatable | Auto Type | Tags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F2C_ORDBUY_TC_026 | REQ-F2C-ORDBUY-22 | ORDBUY | High | Bảng kiểm UI cơ bản — màn Yêu cầu Trả hàng/Hoàn tiền | Đơn đủ điều kiện gửi yêu cầu | 1. Mở màn Yêu cầu Trả hàng/Hoàn tiền<br>2. Đối chiếu Bảng kiểm | — | **Bảng kiểm:**<br>`1` Đủ field: "Hoàn tiền vào", "Tổng tiền hoàn", "Lý do", "Mô tả", "Hình ảnh & video", "Email cập nhật tình hình", nút "Gửi yêu cầu"<br>`2` Nút "Gửi yêu cầu" ở trạng thái disabled khi form còn trống | Critical | Partial | UI | @Smoke @NeedsVerify |
| F2C_ORDBUY_TC_027 | REQ-F2C-ORDBUY-22 | ORDBUY | Medium | Truy cập màn hình từ 2 lối vào | Đơn đủ điều kiện gửi yêu cầu | 1. Từ màn Danh sách đơn hàng, bấm "Yêu cầu Trả hàng/Hoàn tiền"<br>2. Quay lại, mở từ màn Chi tiết đơn hàng, bấm cùng nút | — | 1,2. Cả 2 lối đều mở đúng màn Yêu cầu Trả hàng/Hoàn tiền, đúng đơn hàng tương ứng | High | Yes | UI | @Smoke |
| F2C_ORDBUY_TC_028 | REQ-F2C-ORDBUY-25, 26, 27, 29 | ORDBUY | Critical | Happy path — điền đủ dữ liệu hợp lệ và gửi thành công | Đơn đủ điều kiện, TKNH đã liên kết | 1. Mở màn Yêu cầu Trả hàng/Hoàn tiền<br>2. Chọn "Hoàn tiền vào" = TKNH đã liên kết<br>3. Chọn "Lý do" = "Sản phẩm lỗi/hư hỏng"<br>4. Nhập "Mô tả" = "Sản phẩm bị vỡ khi nhận hàng"<br>5. Upload 2 ảnh hợp lệ<br>6. Bấm "Gửi yêu cầu" | TKNH: `VCB - 0123456789`; Mô tả: `Sản phẩm bị vỡ khi nhận hàng`; Ảnh: `damage_01.jpg` (2MB), `damage_02.jpg` (3MB) | 6. Toast hiện đúng "Yêu cầu Trả hàng/Hoàn tiền được gửi thành công. Thời gian xử lý từ 1-3 ngày. Sau thời gian này, nếu yêu cầu của bạn chưa được xử lý, liên hệ CSKH để được hỗ trợ."; điều hướng sang màn Chi tiết hoàn tiền | Critical | Yes | UI | @Smoke @CriticalPath |

## V2 — Functional

| TC ID | REQ ID | Module | Risk Level | Test Scenario | Pre-Condition | Test Steps | Test Data | Expected Result | Priority | Automatable | Auto Type | Tags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F2C_ORDBUY_TC_029 | REQ-F2C-ORDBUY-23 | ORDBUY | High | Field "Hoàn tiền vào" — chọn tài khoản khi có nhiều TKNH liên kết | Buyer có ≥2 TKNH liên kết qua eKYC | 1. Mở màn Yêu cầu Trả hàng/Hoàn tiền<br>2. Bấm vào field "Hoàn tiền vào"<br>3. Chọn 1 TKNH trong bottom sheet | TKNH 1: `VCB - 0123456789`; TKNH 2: `TCB - 0987654321` | 3. Bottom sheet liệt kê đủ TKNH đã liên kết; chọn xong field hiển thị đúng TKNH đã chọn | High | Yes | UI | @Regression |
| F2C_ORDBUY_TC_030 | REQ-F2C-ORDBUY-23 | ORDBUY | High | Field "Hoàn tiền vào" — đơn thanh toán qua Zalopay khi chưa tích hợp (AMB-03, đã PO xác nhận) | Đơn thanh toán gốc bằng Zalopay | 1. Mở màn Yêu cầu Trả hàng/Hoàn tiền cho đơn thanh toán Zalopay `ORD_ZALOPAY_20260918` | — | 1. Toàn bộ luồng Trả hàng/Hoàn tiền bị ẩn hoặc disable cho đơn này (theo assumption đã PO xác nhận) | High | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_031 | REQ-F2C-ORDBUY-24 | ORDBUY | Critical | Field "Tổng tiền hoàn" tính đúng — bằng đúng số tiền đã thanh toán, không trừ gì thêm (AMB-04, đã PO xác nhận) | Đơn đã thanh toán tổng 1.250.000đ | 1. Mở màn Yêu cầu Trả hàng/Hoàn tiền cho đơn `ORD_TIENHOAN_20260918`<br>2. Đối chiếu field "Tổng tiền hoàn" | Tổng đã thanh toán: `1.250.000đ` | 2. Field "Tổng tiền hoàn" hiển thị đúng `1.250.000đ`, không trừ phí vận chuyển/phí giao dịch/voucher | Critical | Yes | UI | @Regression @CriticalPath |
| F2C_ORDBUY_TC_032 | REQ-F2C-ORDBUY-25 | ORDBUY | High | Field "Lý do" — required, chỉ chọn được 1 | Đang ở màn Yêu cầu Trả hàng/Hoàn tiền | 1. Không chọn "Lý do", bấm "Gửi yêu cầu"<br>2. Bấm field "Lý do", chọn lý do A<br>3. Bấm lại field "Lý do", chọn lý do B | Lý do A: `Sản phẩm lỗi/hư hỏng`; Lý do B: `Giao sai sản phẩm` | 1. Không gửi được, trình hiện cảnh báo tại field "Lý do"<br>2. Field hiển thị đúng lý do A đã chọn<br>3. Field cập nhật thành lý do B (chỉ giữ 1 lựa chọn, không cộng dồn) | High | Yes | UI | @Regression |
| F2C_ORDBUY_TC_033 | REQ-F2C-ORDBUY-26 | ORDBUY | Medium | Field "Mô tả" — validate độ dài, trim, ký tự đặc biệt (textarea 15-field checklist) | Đang ở màn Yêu cầu Trả hàng/Hoàn tiền | 1. Nhập Mô tả theo từng biến thể, bấm "Gửi yêu cầu" (đã điền đủ field bắt buộc khác)<br>2. Quan sát field sau khi trang xử lý | `a` đúng 2.000 ký tự<br>`b` 2.001 ký tự (chặn nhập thêm)<br>`c` `"  có khoảng trắng đầu/cuối  "`<br>`d` ký tự đặc biệt `<>&"'@#$%`<br>`e` `"Sản phẩm bị vỡ 😢🎁 khi nhận"` (emoji + tiếng Việt có dấu) | `a` Gửi thành công, mô tả lưu đủ 2.000 ký tự<br>`b` Trình chặn không cho gõ/dán quá 2.000 ký tự<br>`c` Khoảng trắng đầu/cuối tự động bị cắt (trim) khi lưu<br>`d` Ký tự đặc biệt được chấp nhận, hiển thị lại đúng nguyên văn, không bị escape lỗi<br>`e` Lưu và hiển thị lại đúng nguyên văn, không vỡ font/mất ký tự | Medium | Yes | UI | @Regression @Boundary |
| F2C_ORDBUY_TC_034 | REQ-F2C-ORDBUY-27 | ORDBUY | Medium | Field "Hình ảnh & video" — giới hạn số lượng và dung lượng (file upload checklist) | Đang ở màn Yêu cầu Trả hàng/Hoàn tiền | 1. Upload lần lượt theo Bảng biến thể, quan sát kết quả | `a` 6 ảnh hợp lệ (≤20MB/ảnh)<br>`b` ảnh thứ 7 (vượt giới hạn 6 ảnh)<br>`c` 1 ảnh 21MB (vượt 20MB)<br>`d` 2 video hợp lệ (≤200MB/video)<br>`e` video thứ 3 (vượt giới hạn 2 video)<br>`f` video 201MB (vượt 200MB) | `a` Upload thành công, hiện đủ 6 thumbnail<br>`b` Bị chặn, thông báo đã đạt giới hạn 6 ảnh<br>`c` Bị chặn, thông báo vượt dung lượng cho phép<br>`d` Upload thành công, hiện đủ 2 video<br>`e` Bị chặn, thông báo đã đạt giới hạn 2 video<br>`f` Bị chặn, thông báo vượt dung lượng cho phép | Medium | Partial | UI | @Regression @Boundary |
| F2C_ORDBUY_TC_035 | REQ-F2C-ORDBUY-27 | ORDBUY | Low | Field "Hình ảnh & video" — không bắt buộc, gửi được khi bỏ trống | Đơn đủ điều kiện gửi yêu cầu | 1. Điền đủ field bắt buộc, KHÔNG upload ảnh/video<br>2. Bấm "Gửi yêu cầu" | — | 2. Gửi thành công, không bị chặn vì thiếu ảnh/video | Low | Yes | UI | @Regression |
| F2C_ORDBUY_TC_036 | REQ-F2C-ORDBUY-28 | ORDBUY | Medium | Field "Email cập nhật tình hình" — tự động điền/rỗng đúng theo loại tài khoản (AMB-04, đã PO xác nhận) | 2 tài khoản: 1 đăng ký bằng email, 1 đăng ký bằng SĐT | 1. Mở màn với tài khoản đăng ký bằng email<br>2. Mở màn với tài khoản đăng ký bằng SĐT<br>3. Thử bấm/gõ vào field Email ở trường hợp 2 | Email: `test_ordbuy_buyer_20260918@auto.test`; SĐT: `0912345678` | 1. Field tự động điền đúng email đã đăng ký, không sửa được<br>2. Field hiển thị rỗng<br>3. Không cho nhập tay — field vẫn khoá/không có ô nhập thay thế | Medium | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_037 | REQ-F2C-ORDBUY-29 | ORDBUY | Critical | UI Behavior — nút "Gửi yêu cầu" enable/disable đúng điều kiện | Đang ở màn Yêu cầu Trả hàng/Hoàn tiền | 1. Chỉ điền "Hoàn tiền vào"<br>2. Điền thêm "Lý do" (đủ 3 field bắt buộc: Hoàn tiền vào, Tổng tiền hoàn — tự có sẵn, Lý do) | — | 1. Nút "Gửi yêu cầu" vẫn disabled<br>2. Nút "Gửi yêu cầu" chuyển sang enabled | Critical | Yes | UI | @Smoke @CriticalPath |
| F2C_ORDBUY_TC_038 | REQ-F2C-ORDBUY-06, 07 | ORDBUY | High | Business Rule — chặn gửi khi đã hết lượt (2 lần, AMB-05 đã xác nhận) | Đơn đã huỷ/từ chối đủ 2 lần | 1. Cố mở màn Yêu cầu Trả hàng/Hoàn tiền cho đơn `ORD_HETLUOT_20260918` | — | 1. Không truy cập được màn hình (điều hướng bị chặn), hoặc mở được nhưng nút "Gửi yêu cầu" khoá vĩnh viễn kèm thông báo đã hết lượt | High | Partial | UI | @Regression @Boundary |
| F2C_ORDBUY_TC_039 | REQ-F2C-ORDBUY-27 | ORDBUY | Low | Voucher hướng dẫn — hiển thị nhưng không cấp thật (AMB-08, đã PO xác nhận) | Đơn đủ điều kiện, upload đủ 6 ảnh + video | 1. Điền đủ field, upload đủ 6 ảnh + 2 video theo đúng hướng dẫn voucher<br>2. Gửi yêu cầu thành công<br>3. Kiểm tra ví voucher của Buyer | — | 1. Dòng hướng dẫn voucher vẫn hiển thị theo field spec<br>3. KHÔNG có voucher giảm giá 10% nào được cấp vào ví — xác nhận đúng assumption AMB-08 | Medium | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_040 | REQ-F2C-ORDBUY-29 | ORDBUY | High | Error Guessing — double-submit không tạo 2 yêu cầu | Đơn đủ điều kiện, form đã điền hợp lệ | 1. Điền đủ field hợp lệ<br>2. Bấm "Gửi yêu cầu" 2 lần liên tiếp thật nhanh | — | 2. Chỉ tạo đúng 1 yêu cầu Trả hàng/Hoàn tiền cho đơn hàng, không tạo bản ghi trùng | High | Partial | UI | @Regression @TechCheck |

## Đối soát loại kiểm thử (4 vòng) — Part 3

| Vòng | Nhánh | Trạng thái | TC ID / Lý do |
|---|---|---|---|
| 1 | UI cơ bản | ✅ | TC_026 |
| 1 | Open form | ✅ | TC_027 |
| 1 | Input valid · Save · Verify | ✅ | TC_028 |
| 2 | UI Behavior — nút Gửi yêu cầu | ✅ | TC_037 |
| 2 | Required | ✅ | TC_032, TC_037 |
| 2 | Validation (đủ mục bảng field: Dropdown, Textarea, File Upload) | ✅ | TC_029–TC_036 (đủ N/N mục bảng Textarea (26) · File Upload (34)) |
| 2 | Business Rule (Zalopay ẩn, giới hạn 2 lần, voucher) | ✅ | TC_030, TC_038, TC_039 |
| 2 | Error Guessing | ✅ | TC_040 |
