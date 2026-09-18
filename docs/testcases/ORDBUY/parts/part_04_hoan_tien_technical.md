# Test Cases — ORDBUY — Part 4: Chi tiết hoàn tiền (1.3.4) + Technical + Non-functional

[← Về index](../test_cases_ORDBUY.md) · [← Part 3](part_03_form_yeu_cau.md)

| Nguồn | [analysis_SRS-ORDBUY-V3.md](../../../requirements/_f2c/ORDBUY/analysis/analysis_SRS-ORDBUY-V3.md) |
|---|---|
| Độ hạt | GỘP |
| Mức rủi ro · độ sâu | `Cao` → **Đầy đủ** |
| ⚠️ Evidence | Không có ảnh evidence — mọi TC nhóm UI/hiển thị gắn `@NeedsVerify` |
| Năng lực QA (Vòng 3) | Gọi API ✅ · CSDL ❌ · Tích hợp CMS ❌ · Nhật ký ❌ · DevTools ✅ — nguồn: `docs/requirements/_f2c/README.md`, chốt 2026-09-18 |

---

## V1 — Smoke

| TC ID | REQ ID | Module | Risk Level | Test Scenario | Pre-Condition | Test Steps | Test Data | Expected Result | Priority | Automatable | Auto Type | Tags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F2C_ORDBUY_TC_041 | REQ-F2C-ORDBUY-30 | ORDBUY | High | Bảng kiểm UI cơ bản — màn Chi tiết hoàn tiền | Yêu cầu vừa gửi, đang "Đang chờ xử lý" | 1. Mở màn Chi tiết hoàn tiền<br>2. Đối chiếu Bảng kiểm | — | **Bảng kiểm:**<br>`1` Có Progress Bar 4 mốc: Chấp nhận/Từ chối hoàn tiền → Trả hàng cho người bán → Đã hoàn tiền / Hoàn tiền thất bại<br>`2` Mốc "Chấp nhận/Từ chối hoàn tiền" đang ở trạng thái chờ (chưa hoàn thành)<br>`3` Có nút "Huỷ yêu cầu" (do chưa bàn giao ĐVVC) | Critical | Partial | UI | @Smoke @NeedsVerify |

## V2 — Functional

| TC ID | REQ ID | Module | Risk Level | Test Scenario | Pre-Condition | Test Steps | Test Data | Expected Result | Priority | Automatable | Auto Type | Tags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F2C_ORDBUY_TC_042 | REQ-F2C-ORDBUY-30 | ORDBUY | High | Progress Bar — 2 mốc đầu cập nhật đúng, format DD/MM | Yêu cầu đã được duyệt và ĐVVC đã lấy hàng thành công lúc 18/09/2026 | 1. Gọi API duyệt yêu cầu cho đơn `ORD_A_20260918`<br>2. Mở Chi tiết hoàn tiền, quan sát Progress Bar<br>3. Gọi API xác nhận ĐVVC lấy hàng thành công<br>4. Mở lại Chi tiết hoàn tiền | — | 2. Mốc "Chấp nhận/Từ chối hoàn tiền" hoàn thành, hiện ngày `18/09`<br>4. Mốc "Trả hàng cho người bán" hoàn thành, hiện ngày tương ứng, format DD/MM (không năm) | High | Partial | API | @Regression @TechCheck |
| F2C_ORDBUY_TC_043 | REQ-F2C-ORDBUY-30 | ORDBUY | High | Progress Bar — 2 mốc cuối (Đã hoàn tiền / Hoàn tiền thất bại) | Cần Admin import kết quả trên CMS | ⚪ BLOCKED — chờ tính năng CMS import (AMB-02) | — | — | High | No | N/A | @Blocked |
| F2C_ORDBUY_TC_044 | REQ-F2C-ORDBUY-31 | ORDBUY | High | Button "Huỷ yêu cầu" — hiện đúng điều kiện (chưa bàn giao ĐVVC) | 1 yêu cầu chưa bàn giao ĐVVC, 1 yêu cầu đã bàn giao | 1. Mở Chi tiết hoàn tiền đơn chưa bàn giao ĐVVC<br>2. Mở Chi tiết hoàn tiền đơn đã bàn giao ĐVVC | `ORD_A_20260918` (chưa bàn giao), `ORD_CHOHOANTIEN_20260918` (đã bàn giao) | 1. Nút "Huỷ yêu cầu" hiển thị<br>2. Nút "Huỷ yêu cầu" KHÔNG hiển thị | High | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_045 | REQ-F2C-ORDBUY-31 | ORDBUY | High | Button "Huỷ yêu cầu" — luồng xác nhận Đồng ý / Huỷ (Cancel) | Yêu cầu đủ điều kiện huỷ | 1. Bấm "Huỷ yêu cầu"<br>2. Bấm "Huỷ" (Cancel) trên popup xác nhận<br>3. Bấm lại "Huỷ yêu cầu", lần này bấm "Đồng ý" | — | 1. Popup xác nhận "Bạn có chắc muốn huỷ yêu cầu Trả hàng/Hoàn tiền?" hiện ra<br>2. Popup đóng, yêu cầu giữ nguyên trạng thái<br>3. Yêu cầu bị huỷ, điều hướng về Chi tiết đơn hàng kèm bottom sheet "Yêu cầu trả hàng/hoàn tiền đã được huỷ thành công" | Critical | Yes | UI | @Smoke @CriticalPath |
| F2C_ORDBUY_TC_046 | REQ-F2C-ORDBUY-32 | ORDBUY | Medium | Field "Chọn phương thức trả hàng" — chỉ hiện sau khi được duyệt | 1 yêu cầu chưa duyệt, 1 yêu cầu đã duyệt | 1. Mở Chi tiết hoàn tiền đơn chưa duyệt<br>2. Mở Chi tiết hoàn tiền đơn đã duyệt | `ORD_A_20260918` (chưa duyệt), `ORD_CHONPT_20260918` (đã duyệt) | 1. Tab "Chọn phương thức trả hàng" KHÔNG hiển thị<br>2. Tab hiển thị, mặc định chọn sẵn "Đơn vị vận chuyển đến lấy hàng" | Medium | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_047 | REQ-F2C-ORDBUY-32 | ORDBUY | Medium | Phương thức "Trả hàng tại bưu cục" — vẫn hiện nhưng báo đang phát triển (AMB-07, đã PO xác nhận) | Yêu cầu đã được duyệt | 1. Mở tab "Chọn phương thức trả hàng"<br>2. Bấm vào option "Trả hàng tại bưu cục" | — | 2. Option vẫn hiển thị trên UI (không ẩn), khi bấm vào hiện thông báo "Tính năng đang phát triển", không chuyển được sang phương thức này | Medium | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_048 | REQ-F2C-ORDBUY-32 | ORDBUY | Medium | Xác nhận phương thức — hiện thông tin người gửi, sửa được địa chỉ | Yêu cầu đã được duyệt, chọn "Đơn vị vận chuyển đến lấy hàng" | 1. Xác nhận phương thức mặc định<br>2. Quan sát thông tin hiển thị<br>3. Bấm sửa địa chỉ, nhập địa chỉ mới, lưu | Địa chỉ mới: `123 Đường Test, Phường 1, Quận 1, TP.HCM` | 2. Hiện đúng tên/SĐT/địa chỉ người gửi + thời gian dự kiến ĐVVC đến lấy (1-3 ngày kể từ khi duyệt)<br>3. Địa chỉ cập nhật đúng theo giá trị mới nhập | Medium | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_049 | REQ-F2C-ORDBUY-33 | ORDBUY | Medium | Field "Hướng dẫn trả hàng" — copy mã vận đơn, tải PDF | Đã chọn xong phương thức trả hàng | 1. Mở field "Hướng dẫn trả hàng"<br>2. Bấm copy mã vận đơn<br>3. Bấm tải file PDF phiếu vận đơn | — | 2. Mã vận đơn được copy vào clipboard, có thông báo copy thành công<br>3. File PDF được tải về đúng định dạng, mở được | Medium | Partial | UI | @Regression @NeedsVerify |

## V3 — Technical

> Áp dụng chung cho toàn module `ORDBUY` — không lặp lại ở các part khác.

| TC ID | REQ ID | Module | Risk Level | Test Scenario | Pre-Condition | Test Steps | Test Data | Expected Result | Priority | Automatable | Auto Type | Tags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F2C_ORDBUY_TC_050 | REQ-F2C-ORDBUY-22, 31 | ORDBUY | High | Security — Buyer A không xem/huỷ được yêu cầu của Buyer B qua API trực tiếp (IDOR/BOLA) | 2 tài khoản Buyer khác nhau, mỗi tài khoản có 1 yêu cầu Trả hàng/Hoàn tiền riêng | 1. Đăng nhập Buyer A, lấy token<br>2. Dùng token Buyer A gọi API xem chi tiết yêu cầu hoàn tiền thuộc đơn của Buyer B<br>3. Dùng token Buyer A gọi API huỷ yêu cầu thuộc đơn của Buyer B | Buyer A: `test_buyer_a_20260918@auto.test`; Buyer B: `test_buyer_b_20260918@auto.test` | 2. Bị từ chối, không trả về dữ liệu của Buyer B<br>3. Bị từ chối, yêu cầu của Buyer B không bị huỷ | Critical | Yes | API | @Security @TechCheck |
| F2C_ORDBUY_TC_051 | REQ-F2C-ORDBUY-22 | ORDBUY | Critical | Security — truy cập màn Yêu cầu Trả hàng/Hoàn tiền khi chưa đăng nhập | Chưa đăng nhập / đã đăng xuất | 1. Đăng xuất khỏi app<br>2. Truy cập trực tiếp URL màn Yêu cầu Trả hàng/Hoàn tiền | — | 2. Bị chuyển hướng về màn đăng nhập, không truy cập được form | Critical | Partial | UI | @Security @NeedsVerify |
| F2C_ORDBUY_TC_052 | REQ-F2C-ORDBUY-29 | ORDBUY | Medium | API — gọi trực tiếp API gửi yêu cầu thiếu/sai token | — | 1. Gọi API gửi yêu cầu Trả hàng/Hoàn tiền không kèm token xác thực<br>2. Gọi API với token đã hết hạn | — | 1. Trả về lỗi xác thực, không tạo yêu cầu<br>2. Trả về lỗi xác thực, không tạo yêu cầu | Medium | Yes | API | @TechCheck |
| F2C_ORDBUY_TC_053 | — | ORDBUY | — | Permission — phân quyền theo vai trò trong app Buyer | — | ➖ Không áp dụng — trong phạm vi app Buyer chỉ có đúng 1 vai trò (Buyer), không có chuyển đổi vai trò trên cùng UI. Phân quyền liên module (Seller duyệt, Admin import CMS) thuộc 2 SRS/module khác (`ORDSEL`, `ORDADM`), đã kiểm ở bộ TC riêng của 2 module đó | — | — | — | — | N/A | — |
| F2C_ORDBUY_TC_054 | — | ORDBUY | — | Database — dữ liệu lưu đúng bảng, xoá mềm/cứng | — | ➖ Không áp dụng — QA không có quyền truy vấn CSDL (chốt 2026-09-18, `docs/requirements/_f2c/README.md`) — Dev Backend/CMS chịu trách nhiệm xác minh | — | — | — | — | N/A | — |
| F2C_ORDBUY_TC_055 | — | ORDBUY | — | Integration — hành vi khi CMS/ĐVVC/Zalopay lỗi hoặc quá hạn chờ | — | ➖ Không áp dụng — QA không có tài khoản test Seller/Admin CMS, không kiểm được tầng tích hợp (chốt 2026-09-18) — Dev CMS chịu trách nhiệm | — | — | — | — | N/A | — |
| F2C_ORDBUY_TC_056 | — | ORDBUY | — | Logging/Audit — thao tác quan trọng có ghi nhật ký | — | ➖ Không áp dụng — requirements (SRS delta Ver 3.0.0) không nêu yêu cầu audit log cho luồng này, và QA không có quyền xem nhật ký hoạt động hệ thống | — | — | — | — | N/A | — |

## V4 — Non-functional & Regression

| TC ID | REQ ID | Module | Risk Level | Test Scenario | Pre-Condition | Test Steps | Test Data | Expected Result | Priority | Automatable | Auto Type | Tags |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| F2C_ORDBUY_TC_057 | REQ-F2C-ORDBUY-22 | ORDBUY | Low | Accessibility — điều hướng bàn phím trên form Yêu cầu Trả hàng/Hoàn tiền | Đang ở màn Yêu cầu Trả hàng/Hoàn tiền | 1. Dùng phím `Tab` di chuyển qua lần lượt các field<br>2. Dùng `Enter`/`Space` để kích hoạt nút "Gửi yêu cầu" khi đã đủ điều kiện | — | 1. Thứ tự Tab đi qua các field theo đúng thứ tự hiển thị trên màn hình, có viền/dấu hiệu focus rõ ràng<br>2. Nút được kích hoạt đúng như click chuột | Low | Partial | UI | @Regression @NeedsVerify |
| F2C_ORDBUY_TC_058 | REQ-F2C-ORDBUY-33 | ORDBUY | Low | Localization — Mô tả nhập tiếng Việt có dấu phức tạp | Đang ở màn Yêu cầu Trả hàng/Hoàn tiền | 1. Nhập Mô tả bằng tiếng Việt có dấu phức tạp<br>2. Gửi yêu cầu, mở lại Chi tiết hoàn tiền | `"Sản phẩm giao thiếu phụ kiện, ưu tiên xử lý gấp – cảm ơn ạ!"` | 2. Nội dung hiển thị lại đúng nguyên văn, không lỗi font/mất dấu | Low | Yes | UI | @Regression |
| F2C_ORDBUY_TC_059 | — | ORDBUY | — | Compatibility / Responsive | — | ➖ Không áp dụng — chưa có hệ thống thật (mode DOC) nên chưa chốt được danh sách trình duyệt/breakpoint cam kết. Rà lại khi chạy `/discover-system` mode HYBRID có URL thật | — | — | — | — | N/A | — |
| F2C_ORDBUY_TC_060 | — | ORDBUY | — | Performance | — | ➖ Không áp dụng — chưa có hệ thống thật để đo ngưỡng thời gian tải; không có công cụ tải trong tay QA | — | — | — | — | N/A | — |
| F2C_ORDBUY_TC_061 | — | ORDBUY | — | Regression | — | ➖ Không áp dụng — module mới (delta Ver 3.0.0), chưa có bug nào được đóng ở `docs/bugs/` cho luồng này | — | — | — | — | N/A | — |
| F2C_ORDBUY_TC_062 | — | ORDBUY | — | E2E xuyên module (Buyer → Seller/Admin) | — | ➖ Không áp dụng ở đây — thuộc phạm vi `/generate-cross-module-test-plan` giữa `ORDBUY`/`ORDSEL`/`ORDADM`, không sinh trong bộ TC 1 module | — | — | — | — | N/A | — |

## Đối soát loại kiểm thử (4 vòng) — Part 4 (và tổng hợp Vòng 3/4 cho cả module)

| Vòng | Nhánh | Trạng thái | TC ID / Lý do |
|---|---|---|---|
| 1 | UI cơ bản | ✅ | TC_041 |
| 2 | Business Rule — Progress Bar | ✅ (một phần `⚪ BLOCKED`) | TC_042 ✅ · TC_043 ⚪ |
| 2 | UI Behavior/Dependency — Huỷ yêu cầu, Chọn phương thức | ✅ | TC_044–TC_048 |
| 2 | Use Case — Hướng dẫn trả hàng | ✅ | TC_049 |
| 3 | Permission | `➖` | TC_053 — chỉ 1 vai trò trong phạm vi app Buyer |
| 3 | Security | ✅ | TC_050, TC_051 |
| 3 | API | ✅ | TC_052 |
| 3 | Database | `➖` | TC_054 — QA không có quyền CSDL (Dev Backend/CMS chịu trách nhiệm) |
| 3 | Integration | `➖` | TC_055 — QA không có tài khoản test CMS (Dev CMS chịu trách nhiệm) |
| 3 | Logging/Audit | `➖` | TC_056 — requirements không yêu cầu, QA không có quyền xem log |
| 4 | Accessibility | ✅ | TC_057 |
| 4 | Localization | ✅ | TC_058 |
| 4 | Compatibility/Responsive | `➖` | TC_059 — chưa có hệ thống thật để chốt breakpoint |
| 4 | Performance | `➖` | TC_060 — không có công cụ đo |
| 4 | Regression | `➖` | TC_061 — module mới, chưa có bug đóng |
| 4 | E2E | `➖` | TC_062 — thuộc phạm vi cross-module test plan |
