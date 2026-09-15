# 📋 Phân Tích Requirement: SRS-ORDSEL-V4
## Luồng Trả hàng/Hoàn tiền — App Seller (PIFA/F2C) — delta ver 4.0

## 1. Tổng Quan Ticket

| Mục | Giá trị |
|---|---|
| **Loại tài liệu** | SRS (không phải Jira ticket) — "TÀI LIỆU ĐẶC TẢ NGHIỆP VỤ QUẢN LÝ ĐƠN HÀNG SELLER", DỰ ÁN: F2C |
| **Hệ thống / Module** | F2C (PIFA Marketplace) — module `ORDSEL` (namespace `docs/requirements/_f2c/`) |
| **Phiên bản phân tích** | ver 4.0 — 26/08/2026 (chỉ phần **thay đổi/mới**, được tác giả tô **highlight màu vàng** trong Google Doc gốc) |
| **Chuẩn bị bởi / Xác nhận bởi** | AIT / VTP |
| **Nguồn phân tích** | `docs/requirements/_f2c/_discovery/sources/srs_order_seller_v4.txt` (export text) + bản HTML gốc (dò highlight, không lưu vào `docs/`) |
| **Dải mã đã dùng** | `REQ-F2C-ORDSEL-01` → `REQ-F2C-ORDSEL-39` · `AMB-09` → `AMB-14` · `RISK-06` → `RISK-10` |
| **Mã kế tiếp** | Đợt sau bắt đầu từ `REQ-F2C-ORDSEL-40`. AMB/RISK tiếp tục từ dải chung của namespace `_f2c/` (xem `docs/requirements/_f2c/README.md` — đã có `AMB-01`→`AMB-08`, `RISK-01`→`RISK-05` từ đợt phân tích `ORDBUY`) |
| **Mức độ đầy đủ** | ⚠️ Đủ để sinh test case cho luồng UI Seller, nhưng phụ thuộc trực tiếp 2 điểm chặn đã phát hiện ở đợt phân tích `ORDBUY` (CMS import hoàn tiền chưa xây) — xem AMB-09 |

### ⚠️ Ghi chú phạm vi

Đã dò tự động toàn bộ HTML export (3328 đoạn văn, 596 đoạn nền vàng `#ffff00`, dùng 7 class CSS khác nhau — nhiều hơn hẳn tài liệu Buyer). Đối chiếu với changelog ver 4.0:

> *"Bổ sung luồng Hoàn/Huỷ - Danh sách đơn hàng (3.1) - Chi tiết đơn hàng (3.2.2.9 -> 3.2.2.12)"*

Khác với đợt phân tích `ORDBUY` (nơi phạm vi highlight lệch nhẹ so với changelog), lần này **khớp chính xác 100%** — toàn bộ 596 đoạn tô vàng nằm gọn trong đúng 2 vùng đã công bố: mục 3.1 (một phần) và mục 3.2.2.9 → 3.2.2.12 (toàn bộ 4 mục con). Không phát hiện phần tô vàng nào nằm ngoài phạm vi changelog.

**Riêng lưu ý về 3.2.2.12:** mục này chứa **2 bảng field** cho 2 kịch bản khác nhau — bảng 1 (STT1→7.5, dòng 2927-3104, "Trường hợp Người mua **chưa** thanh toán đơn hàng") **KHÔNG được tô vàng** (đã có từ trước); chỉ bảng 2 (STT1→17, dòng 3105-3222, "Trường hợp Người mua **đã** thanh toán / Hoàn tiền thất bại") là nội dung mới ver 4.0. Phân tích dưới đây **chỉ** phân tích bảng 2.

**Không thuộc phạm vi phân tích này**: 3.1 STT1-22 (chỉ STT23-27 mới), 3.2.2.1→3.2.2.8 (các trạng thái đơn hàng khác), 3.2.2.12 bảng 1, 3.3 trở đi (Chức năng huỷ đơn hàng, Xuất báo cáo, Chuẩn bị hàng, In nhãn).

## 2. User Story

Không có format "As a... I want... So that...". Trích mục đích (I.1, áp dụng toàn SRS):

> *"Tài liệu được xây dựng nhằm mục đích mô tả chức năng quản lý đơn hàng trên hệ thống Seller F2C"*

Diễn giải cho riêng phần delta: **Là Nhà bán (Seller), tôi muốn xem và xử lý (phê duyệt/từ chối) các yêu cầu Trả hàng/Hoàn tiền từ Người mua, theo dõi tiến trình xử lý hàng hoàn, để hoàn tất nghĩa vụ với Buyer và cập nhật đúng doanh thu đơn hàng.**

## 3. Phạm Vi Áp Dụng (Scope)

| Trong phạm vi | Vị trí | Ghi chú |
|---|---|---|
| Tab "Trả hàng" + "Đã hoàn thành" trên Danh sách đơn hàng | 3.1, STT1(intro)/16(action) | Điều kiện lọc + action theo trạng thái |
| 4 field mới hiển thị trên card đơn hàng (tab Trả hàng/Đã huỷ) | 3.1 STT23→27 | Trạng thái hoàn tiền, Số lần khiếu nại, Phương thức trả hàng, Người duyệt, Người huỷ |
| Chi tiết đơn hàng — Trả hàng (Chờ xét duyệt/Chờ giao hàng/Đang giao hàng/Đã hoàn tiền/Hoàn tiền thất bại) `[MỚI toàn màn]` | 3.2.2.9 | STT1→23 |
| Chi tiết đơn hàng — Giao hàng thất bại (Lưu kho/Tiêu huỷ) `[MỚI toàn màn]` | 3.2.2.10 | STT1→19 |
| Chi tiết đơn hàng — Đã hoàn thành `[MỚI toàn màn]` | 3.2.2.11 | STT1→15 |
| Chi tiết đơn hàng — Đã huỷ, trường hợp đã thanh toán/Hoàn tiền thất bại `[MỚI]` | 3.2.2.12 (bảng 2) | STT1→17 |

| Ngoài phạm vi (thuộc SRS nhưng chưa phân tích) | Lý do |
|---|---|
| 3.1 STT1-22, 3.2.2.1→3.2.2.8, 3.2.2.12 bảng 1, 3.3+ | Không bôi vàng |
| Hành vi phía **Buyer** (tạo yêu cầu) | Đã phân tích riêng — xem [`ORDBUY/analysis/analysis_SRS-ORDBUY-V3.md`](../../ORDBUY/analysis/analysis_SRS-ORDBUY-V3.md) |
| Hành vi phía **Admin/CMS** (phê duyệt lần 2, import kết quả hoàn tiền, cấu hình phí chiết khấu/dịch vụ) | Thuộc `srs_order_admin_cms_v1.1.txt` — chưa phân tích |

## 4. Acceptance Criteria — Phân Tích Chi Tiết

### 4.1. Danh sách đơn hàng — tab và field mới (3.1)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDSEL-01` | Tab "Trả hàng" hiển thị đơn có yêu cầu Trả hàng/Hoàn tiền ở các trạng thái: Chờ xét duyệt, Chờ giao hàng, Đang giao hàng, Đã giao hàng, Giao thất bại - Lưu kho (mã 506), Giao thất bại - Tiêu huỷ (mã 503) | dòng 311-312, 326 |
| `REQ-F2C-ORDSEL-02` | Tab "Đã hoàn thành" hiển thị đơn đã giao thành công VÀ (không phát sinh yêu cầu Trả hàng/Hoàn tiền sau 5 ngày kể từ giao thành công) HOẶC (có yêu cầu nhưng đã bị huỷ/từ chối) | dòng 313-314, 327 |
| `REQ-F2C-ORDSEL-03` | Action (menu Thao tác STT16) với đơn ở trạng thái Chờ xét duyệt: "Xem chi tiết", "Phê duyệt" | dòng 263-265, 572-574 |
| `REQ-F2C-ORDSEL-04` | Action với đơn ở trạng thái Chờ giao hàng/Đang giao hàng/Đã giao hàng (trong tab Trả hàng): chỉ "Xem chi tiết" | dòng 266-267 |
| `REQ-F2C-ORDSEL-05` | Action với đơn ở tab Đã hoàn thành: chỉ "Xem chi tiết" | dòng 271-274, 575-576 |
| `REQ-F2C-ORDSEL-06` | STT23 "Trạng thái hoàn tiền" (Label, không bắt buộc) — chỉ hiện với tab Trả hàng; 1 trong 3 giá trị: Chờ hoàn tiền (sau khi được Nhà bán/Admin phê duyệt), Đã hoàn tiền, Hoàn tiền thất bại (2 giá trị sau lấy theo **file import của Admin** — xem AMB-09); trống nếu đơn đang ở Chờ xét duyệt | dòng 632-642 |
| `REQ-F2C-ORDSEL-07` | STT24 "Số lần khiếu nại" — chỉ hiện tab Trả hàng; Buyer có **tối đa 2 lần** khiếu nại cho mỗi đơn hàng; lần 1 bị Nhà bán từ chối → lần 2 tự động chuyển Admin phê duyệt | dòng 643-651 — ⭐ **xác nhận chính thức con số "2 lần"**, xem AMB-10 |
| `REQ-F2C-ORDSEL-08` | STT25 "Phương thức trả hàng" — chỉ hiện tab Trả hàng; 1 trong 2 giá trị: "Trả hàng và Hoàn tiền", "Hoàn tiền ngay (không trả hàng)" | dòng 652-659 |
| `REQ-F2C-ORDSEL-09` | STT26 "Người duyệt" — chỉ hiện tab Trả hàng; giá trị: Admin hoặc tên nhà bán | dòng 660-667 |
| `REQ-F2C-ORDSEL-10` | STT27 "Người huỷ" (bắt buộc = **Y**, khác toàn bộ field khác trong nhóm này đều N) — chỉ hiện tab Đã huỷ; giá trị: Admin, tên nhà bán, hoặc tên người mua | dòng 668-675 |

### 4.2. Chi tiết đơn hàng — Trả hàng (Chờ xét duyệt/Chờ giao hàng/Đang giao hàng/Đã hoàn tiền/Hoàn tiền thất bại) `[MỚI toàn màn]` (3.2.2.9)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDSEL-11` | STT3 "Trạng thái đơn hàng" — hiện trạng thái xét duyệt yêu cầu và trả hàng; **chỉ hiện** khi phương thức trả hàng là "Trả hàng và Hoàn tiền" | dòng 2437-2444 |
| `REQ-F2C-ORDSEL-12` | STT4 "Trạng thái hoàn tiền" (bắt buộc = X) — trống khi yêu cầu chưa được duyệt hoặc ĐVVC chưa lấy hàng thành công | dòng 2445-2451 — xem AMB-11 (mâu thuẫn cột "Bắt buộc" và rule cho phép trống) |
| `REQ-F2C-ORDSEL-13` | STT5 "Thời gian duyệt yêu cầu" — chỉ hiện ở trạng thái Chờ xét duyệt; đếm ngược từ 24:00:00, format HH:MM:SS; tooltip icon-i: "Thời gian Nhà bán phê duyệt yêu cầu Trả hàng/Hoàn tiền. Sau thời gian này, yêu cầu sẽ được chuyển sang Admin phê duyệt" | dòng 2452-2463 |
| `REQ-F2C-ORDSEL-14` | STT6 "Thanh trạng thái" (Progress Bar) — 2 nhánh: phương án "Trả hàng và Hoàn tiền" → 4 bước (Chờ duyệt → Chờ giao hàng → Đang giao hàng → Đã giao hàng); phương án "Hoàn tiền ngay" → 3 bước (Chờ duyệt → Chờ hoàn tiền → Đã hoàn tiền) | dòng 2464-2475 |
| `REQ-F2C-ORDSEL-15` | STT7 "Button Từ chối" — chỉ hiện khi: đơn ở Chờ xét duyệt, yêu cầu **lần đầu**, còn hạn 24h. Click → popup "Chọn lý do từ chối" (dropdown lý do có sẵn + "Lý do khác" cho nhập textbox tự do ≤200 ký tự, cho phép chữ/số/ký tự đặc biệt/hoa/thường, chặn nhập quá, tự trim đầu-cuối) → Xác nhận: từ chối yêu cầu, điều hướng Chi tiết đơn hàng trạng thái Đã giao hàng, gửi thông báo cho Buyer | dòng 2476-2493 |
| `REQ-F2C-ORDSEL-16` | STT8 "Button Phê duyệt" — điều kiện hiện tương tự REQ-15. Click → popup "Chọn Phương án Trả hàng/Hoàn tiền" (mặc định chọn "Trả hàng và Hoàn tiền") → Xác nhận: phê duyệt, gửi thông báo Buyer; nếu chọn "Trả hàng và Hoàn tiền" → điều hướng Chi tiết đơn hàng trạng thái Chờ giao hàng + toast "Phê duyệt yêu cầu thành công"; nếu chọn "Hoàn tiền ngay" → điều hướng trạng thái Chờ hoàn tiền | dòng 2494-2509 |
| `REQ-F2C-ORDSEL-17` | `[Business rule]` Yêu cầu Trả hàng/Hoàn tiền **lần 2** của cùng 1 đơn hàng luôn do **Admin** phê duyệt (không phải Seller) — lặp lại xác nhận ở cả STT7 và STT8 | dòng 2483, 2501 — xem AMB-12 (UI cho Seller xem yêu cầu lần 2 có ẩn 2 nút này không?) |
| `REQ-F2C-ORDSEL-18` | STT9 "Thông tin giao hàng & Thông tin vận chuyển" (luôn hiện) — người nhận (tên/SĐT/địa chỉ) + vận chuyển chiều đi (tên ĐVVC mặc định Viettel Post, mã vận đơn, địa chỉ lấy hàng) | dòng 2510-2522 |
| `REQ-F2C-ORDSEL-19` | STT10 "Thông tin Trả hàng" — chỉ hiện với phương án "Trả hàng và Hoàn tiền". Gồm: mã yêu cầu (copy được); "Hoàn tiền vào" theo phương thức thanh toán gốc (Zalopay/QR); thời gian yêu cầu; lý do kèm ảnh/video; mã vận đơn trả hàng (mã hoàn/thu hồi của ĐVVC, hiện từ khi đơn ở Chờ giao hàng, trống nếu chưa có); địa chỉ nhận hàng hoàn (hiện sau khi Buyer chọn phương thức trả hàng, hiện ở mọi trạng thái trừ Chờ duyệt) | dòng 2523-2537 |
| `REQ-F2C-ORDSEL-20` | STT11 "Thông tin hoàn tiền" — Tổng tiền thanh toán (tiền Buyer đã trả khi đặt hàng); Phí vận chuyển hoàn (E2 trả data); Số tiền hoàn = Tổng tiền thanh toán | dòng 2538-2546 |
| `REQ-F2C-ORDSEL-21` | STT12→20 "Thông tin đơn hàng giao cho Người mua" — kế thừa nguyên vẹn rule từ STT5-19 mục 3.2.2.1 (ngoài phạm vi phân tích đợt này) | dòng 2547-2602 |
| `REQ-F2C-ORDSEL-22` | STT21 "Hành trình đơn hàng" — mốc thời gian ghi nhận cho 6 sự kiện liên quan Trả hàng/Hoàn tiền: Buyer tạo yêu cầu · Nhà bán/Admin từ chối (kèm lý do) · Nhà bán/Admin phê duyệt · Buyer huỷ yêu cầu · ĐVVC lấy hàng hoàn thành công/thất bại · ĐVVC giao hàng hoàn thành công/thất bại. Format hh:mm:ss dd/mm/yyyy. Rule: không cập nhật lại 1 trạng thái đã ghi nhận | dòng 2603-2619 |
| `REQ-F2C-ORDSEL-23` | STT22 "Thời gian chọn phương thức trả hàng/hoàn tiền" — chỉ hiện khi đơn ở Chờ giao hàng VÀ được **Admin** phê duyệt (không phải Nhà bán); đếm ngược 24:00:00, format HH:MM:SS; hết hạn → phương thức mặc định "Trả hàng và Hoàn tiền" | dòng 2620-2630 |
| `REQ-F2C-ORDSEL-24` | STT23 "Chọn phương thức trả hàng" (button) — điều kiện hiện giống REQ-23; click → popup chọn phương thức (rule giống STT8 cùng mục) | dòng 2631-2638 |

### 4.3. Chi tiết đơn hàng — Giao hàng thất bại (Lưu kho/Tiêu huỷ) `[MỚI toàn màn]` (3.2.2.10)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDSEL-25` | STT3 "Trạng thái đơn hàng" — 2 giá trị: "Giao hàng thất bại - Lưu kho" (ĐVVC giao hàng hoàn cho Nhà bán thất bại, mã 506 phía E2), "Giao thất bại - Tiêu huỷ" (mã 503 phía E2) | dòng 2661-2672 |
| `REQ-F2C-ORDSEL-26` | STT5 "Thời gian lấy hàng lưu kho" — chỉ hiện ở trạng thái Lưu kho; đếm ngược **7 ngày** kể từ ngày đơn chuyển mã 503 phía E2/EVTP; format HH:MM:SS ngày DD/MM/YYYY; hết hạn → hàng bị **tiêu huỷ** | dòng 2680-2690 |
| `REQ-F2C-ORDSEL-27` | STT6 "Thanh trạng thái" — 4 bước: Chờ duyệt, Chờ giao hàng, Đang giao hàng, Giao hàng thất bại. Ghi chú: nếu đơn ở "Giao thất bại - Lưu kho" mà ĐVVC giao lại thành công cho Nhà bán → đơn chuyển sang "Đã giao" (mã 501), rời khỏi luồng lỗi | dòng 2691-2698 |
| `REQ-F2C-ORDSEL-28` | STT8 "Thông tin Trả hàng" — giống STT10 mục 3.2.2.9, **cộng thêm** field "Địa chỉ bưu cục lưu hàng" (hiện sau khi đơn ở mã 503 phía EVTP, lấy theo bưu cục giao từ EVTP) | dòng 2712-2726 |
| `REQ-F2C-ORDSEL-29` | STT9 "Thông tin hoàn tiền" — công thức chi tiết hơn 3.2.2.9: Tổng tiền thanh toán = giá sản phẩm (Nhà bán/Admin upload) + phí vận chuyển chiều đi (E2 trả data, **hiện = 0 với mọi đơn**) − voucher giảm giá (nếu có); Phí vận chuyển hoàn (E2 trả data, hiện = 0) | dòng 2727-2735 — xem AMB-13 (giá trị 0 là tạm thời hay chính sách vĩnh viễn?) |
| `REQ-F2C-ORDSEL-30` | STT10→18 kế thừa STT5-19 mục 3.2.2.1 (giống REQ-21, ngoài phạm vi) | dòng 2736-2791 |
| `REQ-F2C-ORDSEL-31` | STT19 "Hành trình đơn hàng" — kế thừa STT21 mục 3.2.2.9 (REQ-22), cộng thêm: nếu đơn giao thất bại (mã 506) thì hiển thị lý do giao hàng thất bại (E2 gửi kèm) | dòng 2792-2798 |

### 4.4. Chi tiết đơn hàng — Đã hoàn thành `[MỚI toàn màn]` (3.2.2.11)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDSEL-32` | STT1 "Back" — điều hướng về Danh sách đơn hàng **đúng tab "Đã hoàn thành"** (khác các màn 3.2.2.9/10 chỉ ghi chung "Danh sách đơn hàng") | dòng 2813-2818 |
| `REQ-F2C-ORDSEL-33` | STT4 "Thanh trạng thái" — 5 bước, **không có bước Trả hàng**: Chờ thanh toán, Chờ giao hàng, Đang giao hàng, Đã giao hàng, Đã hoàn thành | dòng 2831-2837 |
| `REQ-F2C-ORDSEL-34` | STT6→14 kế thừa STT5-19 mục 3.2.2.1 (giống REQ-21) | dòng 2851-2906 |
| `REQ-F2C-ORDSEL-35` | STT15 "Hành trình đơn hàng" — kế thừa cấu trúc REQ-22, **cộng thêm**: nếu đơn từng có yêu cầu Trả hàng/Hoàn tiền bị huỷ hoặc bị từ chối → hiện nút "Xem thêm" để xem lại thông tin yêu cầu đó | dòng 2907-2926 |

### 4.5. Chi tiết đơn hàng — Đã huỷ, trường hợp đã thanh toán / Hoàn tiền thất bại `[MỚI]` (3.2.2.12, bảng 2)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDSEL-36` | STT3 "Trạng thái đơn hàng" = "Đã huỷ" | dòng 3131-3136 |
| `REQ-F2C-ORDSEL-37` | STT4 "Trạng thái hoàn tiền" — 1 trong 3 giá trị: Chờ hoàn tiền, Đã hoàn tiền, Hoàn tiền thất bại | dòng 3137-3142 |
| `REQ-F2C-ORDSEL-38` | STT5 "Thanh trạng thái" — 4 bước: Đã huỷ, Chờ hoàn tiền, Đã hoàn tiền, Hoàn tiền thất bại | dòng 3143-3149 |
| `REQ-F2C-ORDSEL-39` | STT6/STT7 kế thừa nguyên văn STT9 / STT11 mục 3.2.2.9 (REQ-18/REQ-20); STT8→16 kế thừa mục 3.2.2.1 (giống REQ-21); STT17 "Hành trình đơn hàng" kế thừa STT21 mục 3.2.2.9 (REQ-22) | dòng 3150-3222 |

## 4b. Đối Chiếu Chéo Nguồn

Chỉ 1 nguồn văn bản (chính SRS này), không có field-spec `.xlsx`/mockup đính kèm khác. Áp dụng đối chiếu **nội bộ trong tài liệu** và **liên tài liệu với `ORDBUY`** (đã phân tích trước, cùng đặc tả 1 luồng nghiệp vụ nhìn từ 2 phía):

| Hạng mục | SRS Seller (tài liệu này) | SRS Buyer (đã phân tích) | Kết luận |
|---|---|---|---|
| Số lần tối đa yêu cầu Trả hàng/Hoàn tiền / đơn | Nêu rõ **"tối đa 2 lần khiếu nại"** (dòng 650) | Chỉ suy đoán gián tiếp từ text đổi theo "lần 2" (AMB-05 của `ORDBUY`, không có số tường minh) | ✅ **Giải quyết được AMB-05 cũ** — xác nhận con số là **2 lần**. Đề xuất cập nhật trạng thái AMB-05 ở README sang "đã xác nhận qua chéo tài liệu Seller", nhưng **vẫn giữ mở** một phần: cần PO xác nhận đây đúng là cùng 1 khái niệm ("khiếu nại" ở Seller = "yêu cầu Trả hàng/Hoàn tiền" ở Buyer) trước khi đóng hẳn |
| Tính năng import kết quả hoàn tiền trên CMS | *"tính năng này chưa làm ở giai đoạn hiện tại"* (dòng 640-641) | *"tính năng này chưa làm ở giai đoạn hiện tại"* (nguồn gốc AMB-02 của `ORDBUY`) | ✅ Nhất quán 2 tài liệu — củng cố AMB-09 (RISK-06) là chặn thật, không phải lỗi 1 tài liệu |
| Format hiển thị "Thời gian yêu cầu" | `dd/yy/mmmm - hh:mm` (dòng 2534, 2722) | Field tương tự dùng `DD/MM/YYYY` chuẩn, nhưng 1 chỗ khác dùng sai format tương tự (`RISK-04` của `ORDBUY`) | ⚠️ Cùng kiểu lỗi định dạng xuất hiện ở **cả 2 tài liệu độc lập** → tăng khả năng đây là copy-paste lỗi từ 1 template chung, không phải lỗi ngẫu nhiên → `AMB-14` |
| Ai duyệt yêu cầu | "Nhà bán/Admin" — Seller xử lý lần 1, Admin xử lý lần 2 | Buyer doc dùng cụm "Seller/Admin" tương tự nhưng không tách rõ lần 1 và lần 2 | Seller doc **chi tiết hơn** — dùng làm nguồn chính cho quy tắc phân quyền duyệt |

## 5. Phụ Thuộc (Dependencies)

### 5.1. Phụ thuộc `ORDBUY` (đã phân tích)
- Toàn bộ 39 REQ ở trên chỉ xử lý yêu cầu **do Buyer đã tạo** (REQ-F2C-ORDBUY-22→29) — không có nghiệp vụ nào ở Seller tự khởi tạo yêu cầu Trả hàng/Hoàn tiền
- Trạng thái "Hoàn tiền vào" (REQ-19) phụ thuộc trực tiếp lựa chọn tài khoản nhận tiền của Buyer (REQ-F2C-ORDBUY-23)

### 5.2. Phụ thuộc Admin/CMS (chưa phân tích)
- Phê duyệt yêu cầu **lần 2** (REQ-17)
- Chọn phương thức trả hàng thay Seller nếu Seller không chọn kịp (REQ-23, tương tự cơ chế 24h)
- **Import trạng thái hoàn tiền thủ công** — cơ chế duy nhất hiện có để chuyển trạng thái Đã hoàn tiền/Hoàn tiền thất bại, và theo cả 2 tài liệu (Seller + Buyer) đều ghi nhận **chưa được xây** (xem AMB-09)
- Cấu hình phí chiết khấu sàn, phí dịch vụ (nhắc ở 3.2.2.12 bảng 1, ngoài phạm vi trực tiếp nhưng liên quan tính "Doanh thu ước tính")

### 5.3. Phụ thuộc bên ngoài (ĐVVC — Viettel Post / E2)
- Sinh mã vận đơn hoàn (thu hồi)
- Trả trạng thái 501 (đã giao)/503 (tiêu huỷ)/506 (giao thất bại — lưu kho) — các mã trạng thái **phía E2**, không phải trạng thái nội bộ F2C, cần bảng ánh xạ đầy đủ (chỉ thấy 3 mã trong phạm vi phân tích này)
- Trả phí vận chuyển (hiện tại luôn = 0, xem AMB-13)
- Trả lý do giao hàng thất bại (dùng cho REQ-31)

### 5.4. Business Rules tổng hợp
- Luồng phê duyệt 2 tầng: Seller xử lý trong 24h đầu → hết hạn hoặc Seller không xử lý → tự động chuyển Admin → Seller **mất quyền** xử lý yêu cầu đó (REQ-17, AMB-12)
- Toàn bộ số tiền hoàn = đúng số tiền Buyer đã thanh toán (không có logic trừ phí ở phía Seller nhìn thấy — nhất quán với `ORDBUY`)
- Đồng bộ 3 chiều: mọi thay đổi trạng thái Trả hàng/Hoàn tiền phải phản ánh đồng thời trên UI Buyer, Seller, và (khi phân tích tới) Admin — xem RISK-07

## 6. Phân Tích Mockup/Screenshot

Không áp dụng — SRS chỉ tham chiếu Figma (`figma.com/design/qUEAPxxRd2hC561l6GIDTr/F2C`), không đính kèm ảnh đọc được trực tiếp. Tài liệu tự chèn ảnh minh hoạ (Hình 2.7 → 2.16) nhưng không trích xuất được nội dung ảnh qua export text/HTML — chỉ có caption. Nếu cần đối chiếu UI thật, đề xuất chạy `/discover-system` mode HYBRID khi có URL app Seller thật.

## 7. Các Điểm Mơ Hồ & Rủi Ro

### 7.1. Điểm Mơ Hồ (Ambiguities)

> Đánh số tiếp từ `AMB-08` của namespace `_f2c/` (đợt phân tích `ORDBUY` trước đó dùng hết `AMB-01`→`AMB-08`).

| Mã | Câu hỏi | Nguy cơ | Mức độ | Assumption tạm |
|---|---|---|---|---|
| `AMB-09` | Xác nhận chéo với `ORDBUY`: tính năng Admin import trạng thái hoàn tiền trên CMS **vẫn chưa được xây** ở cả 2 tài liệu. Có cách nào khác (API nội bộ, seed DB) để đưa đơn vào trạng thái Đã hoàn tiền/Hoàn tiền thất bại trong môi trường test hiện tại không? | Block toàn bộ TC cho REQ-06, REQ-12, REQ-37 (mọi field "Trạng thái hoàn tiền" phía Seller) | 🔴 High | Giống `AMB-02` của `ORDBUY` — TC đánh dấu `⚪ BLOCKED chờ tính năng CMS import` |
| `AMB-10` | Con số "tối đa 2 lần khiếu nại" (REQ-07) đã xác nhận rõ ràng ở đây — nhưng cần PO xác nhận **"khiếu nại"** (thuật ngữ Seller dùng) và **"yêu cầu Trả hàng/Hoàn tiền"** (thuật ngữ Buyer dùng) là **cùng một khái niệm** | Nếu là 2 khái niệm khác nhau (VD: khiếu nại là 1 tầng riêng, xảy ra sau khi yêu cầu bị từ chối), việc "đóng" AMB-05 cũ của `ORDBUY` là sai | 🟡 Medium | Giả định 2 thuật ngữ đồng nghĩa (ngữ cảnh dùng lẫn nhau xuyên suốt cả 2 tài liệu) |
| `AMB-11` | Cột "Bắt buộc" ở field spec ghi `X` (REQ-12, "Trạng thái hoàn tiền") nhưng mô tả lại cho phép "để trống trường này (hiển thị như UI)" khi điều kiện chưa đủ. "Bắt buộc = X" nghĩa là field **luôn được render** (dù giá trị rỗng) hay **luôn phải có giá trị**? | Sai lệch cách hiểu quy ước field-spec ảnh hưởng tới toàn bộ field có cột tương tự trong cả 3 SRS | 🟢 Low | Giả định "Bắt buộc" = luôn render field trên UI (kể cả rỗng), không phải luôn có giá trị — cần PO/BA xác nhận quy ước chung 1 lần cho cả 3 tài liệu |
| `AMB-12` | Sau khi yêu cầu chuyển sang **lần 2** (Admin xử lý), màn Chi tiết đơn hàng phía Seller có còn hiện nút "Từ chối"/"Phê duyệt" không (REQ-17)? Ẩn hoàn toàn, hay hiện nhưng disable? | Sai kỳ vọng UI khi viết TC cho kịch bản "yêu cầu lần 2" | 🟡 Medium | Giả định: ẩn hoàn toàn 2 nút (Seller chỉ còn xem, không còn quyền thao tác) |
| `AMB-13` | Phí vận chuyển (chiều đi và chiều hoàn) hiện đang hard-code = 0 "với tất cả đơn hàng" (REQ-29) — đây là giá trị **tạm thời** (chờ tích hợp tính phí thật của Viettel Post) hay là **chính sách miễn phí vĩnh viễn**? | Nếu tạm thời: TC hiện tại assert `= 0` sẽ **fail** ngay khi tính năng tính phí thật được bật, cần đánh dấu rõ để không bị coi là regression | 🟡 Medium | Giả định tạm thời — ghi rõ trong TC là "giá trị 0 theo cấu hình hiện tại của E2, cần xác nhận lại khi tích hợp phí thật" |
| `AMB-14` | Format "Thời gian yêu cầu: dd/yy/mmmm - hh:mm" (REQ-19) xuất hiện giống hệt lỗi định dạng đã ghi nhận ở `RISK-04` của `ORDBUY` (tài liệu Buyer). Đây có phải copy-paste lỗi từ 1 template chung giữa 2 tài liệu, hay là format thật sự khác biệt có chủ đích? | Viết sai assertion format ngày cho field này ở cả 2 phân hệ nếu không xác nhận | 🟢 Low | Giả định là lỗi đánh máy lặp lại (không phải chủ đích) — dùng format `DD/MM/YYYY - HH:MM` khi viết TC, không assert cứng theo `dd/yy/mmmm` |

### 7.2. Rủi Ro Kiểm Thử (Testing Risks)

> Đánh số tiếp từ `RISK-05` của namespace `_f2c/`.

| Mã | Rủi ro | Mô tả | Mitigation |
|---|---|---|---|
| `RISK-06` | Không kiểm thử được luồng hoàn tiền tự động end-to-end (phía Seller) | Cùng gốc với `RISK-01` của `ORDBUY` — CMS import chưa xây, giờ xác nhận thêm ở tài liệu Seller | Phối hợp QA phía CMS/Admin; tách riêng nhóm TC BLOCKED |
| `RISK-07` | Đồng bộ trạng thái xuyên suốt **3 hệ thống** (Buyer/Seller/Admin), không phải 2 như đã ghi nhận ở `ORDBUY` | Cùng 1 trạng thái Trả hàng/Hoàn tiền phải hiển thị nhất quán trên UI của cả 3 phân hệ, mỗi phân hệ có field/label riêng (VD: Buyer gọi "Trả hàng" theo tab cha, Seller gọi "Trạng thái đơn hàng" chi tiết hơn) | Viết bộ TC đối chiếu 3 chiều cho mỗi lần chuyển trạng thái, không test riêng lẻ từng phân hệ |
| `RISK-08` | Chồng chéo mốc thời gian đếm ngược, giờ có thêm phía Seller | Seller có thêm 24h (duyệt), 24h (chọn phương thức), 7 ngày (lấy hàng lưu kho) — cộng dồn với 5 mốc đã có phía Buyer (`RISK-05` của `ORDBUY`) → tổng cộng **8 mốc thời gian độc lập** trên vòng đời 1 đơn hàng | Vẽ lại ma trận trạng thái tổng hợp cả 3 phân hệ (mục 8) trước khi phân rã TC; dùng dữ liệu giả lập thời gian, không chờ thời gian thật |
| `RISK-09` | Giá trị phí vận chuyển hard-code = 0 che giấu lỗi tính phí tương lai | Xem AMB-13 — TC hiện tại sẽ luôn pass dù logic tính phí thật (nếu có bug) chưa từng được thực thi | Đánh dấu rõ trong TC: "kiểm tra giá trị hiện tại = 0 theo cấu hình E2 tạm thời" — không đặt tên TC kiểu khẳng định "phí vận chuyển luôn miễn phí" |
| `RISK-10` | Mã trạng thái phía E2 (501/503/506) dùng trực tiếp trong SRS mà không có bảng tra cứu đầy đủ | Chỉ thấy 3 mã trong phạm vi phân tích (501=Đã giao, 503=Tiêu huỷ, 506=Giao thất bại-Lưu kho) — không biết còn mã nào khác ảnh hưởng luồng Trả hàng/Hoàn tiền | Xin bảng đầy đủ mã trạng thái E2/Viettel Post trước khi thiết kế test data mô phỏng webhook/callback từ ĐVVC |

## 8. Ma Trận Trạng Thái

| Trạng thái con (trong tab Trả hàng) | Điều kiện vào | Điều kiện ra / chuyển tiếp | Màn hình tương ứng |
|---|---|---|---|
| Chờ xét duyệt | Buyer gửi yêu cầu Trả hàng/Hoàn tiền | Seller Phê duyệt → Chờ giao hàng (hoặc Chờ hoàn tiền nếu chọn Hoàn tiền ngay) · Seller Từ chối → Đã giao hàng (kết thúc) · Quá 24h không xử lý → chuyển Admin xét duyệt (REQ-17) | 3.2.2.9 |
| Chờ giao hàng | Yêu cầu được phê duyệt (phương án Trả hàng và Hoàn tiền) | Chọn phương thức trả hàng (Seller hoặc mặc định sau 24h) → ĐVVC lấy hàng thành công → Đang giao hàng | 3.2.2.9 |
| Đang giao hàng | ĐVVC lấy hàng hoàn thành công | ĐVVC giao hàng hoàn thành công → Đã giao hàng · ĐVVC giao thất bại → Giao hàng thất bại (Lưu kho mã 506 / Tiêu huỷ mã 503) | 3.2.2.9 → 3.2.2.10 |
| Giao hàng thất bại - Lưu kho | ĐVVC giao hoàn cho Seller thất bại (mã 506) | Seller lên bưu cục lấy trong 7 ngày → Đã giao (mã 501, "cứu" lại luồng bình thường) · Hết 7 ngày → Tiêu huỷ (mã 503) | 3.2.2.10 |
| Chờ hoàn tiền | ĐVVC giao hàng hoàn thành công (phương án Trả hàng và Hoàn tiền), hoặc ngay sau khi duyệt (phương án Hoàn tiền ngay) | Admin import kết quả (REQ-06, AMB-09) → Đã hoàn tiền / Hoàn tiền thất bại | 3.2.2.9, 3.2.2.12 |
| Đã hoàn tiền / Hoàn tiền thất bại | Admin import CMS | Trạng thái cuối (terminal), đơn ở tab Đã huỷ | 3.2.2.12 |

## 9. Tóm Tắt Acceptance Criteria (Checklist)

**Danh sách đơn hàng (3.1)**
- [ ] REQ-01, REQ-02 Điều kiện lọc 2 tab mới
- [ ] REQ-03 → REQ-05 Action đúng theo trạng thái
- [ ] REQ-06 → REQ-10 5 field mới trên card đơn hàng

**Chi tiết — Trả hàng (3.2.2.9)**
- [ ] REQ-11 → REQ-14 Trạng thái + Progress Bar đúng 2 nhánh
- [ ] REQ-15, REQ-16 2 button Từ chối/Phê duyệt đúng điều kiện + luồng
- [ ] REQ-17 Rule "lần 2 luôn do Admin"
- [ ] REQ-18 → REQ-20 3 field thông tin chi tiết
- [ ] REQ-21 Kế thừa field cũ
- [ ] REQ-22 Hành trình đơn hàng đủ 6 mốc
- [ ] REQ-23, REQ-24 Countdown + chọn phương thức

**Chi tiết — Giao hàng thất bại (3.2.2.10)**
- [ ] REQ-25 2 trạng thái con
- [ ] REQ-26, REQ-27 Countdown 7 ngày + Progress Bar 4 bước + rule "cứu" đơn
- [ ] REQ-28 → REQ-31 Field riêng + kế thừa

**Chi tiết — Đã hoàn thành (3.2.2.11)**
- [ ] REQ-32 Back về đúng tab
- [ ] REQ-33 Progress Bar 5 bước không có Trả hàng
- [ ] REQ-34, REQ-35 Kế thừa + nhánh Xem thêm

**Chi tiết — Đã huỷ, đã thanh toán (3.2.2.12 bảng 2)**
- [ ] REQ-36 → REQ-39 Trạng thái + Progress Bar 4 bước + kế thừa

## 10. Khuyến Nghị Cho Kiểm Thử

1. **Chốt AMB-09 trước tiên** — đây là điểm chặn chung cho CẢ HAI module `ORDBUY` và `ORDSEL`, không phải vấn đề riêng của Seller. Giải quyết 1 lần, gỡ chặn cho cả 2 bộ TC.
2. **Xác nhận AMB-10 để chính thức đóng AMB-05 của `ORDBUY`** — nếu PO xác nhận "khiếu nại" = "yêu cầu Trả hàng/Hoàn tiền", cập nhật ngược trạng thái AMB-05 ở `docs/requirements/_f2c/README.md` từ 🔴 sang đã xác nhận (giữ nguyên mã, chỉ đổi trạng thái — không xoá).
3. **Thiết kế TC theo góc nhìn Seller riêng biệt với Buyer**, dù cùng 1 luồng nghiệp vụ — 2 bộ REQ (ORDBUY-* và ORDSEL-*) mô tả **cùng sự kiện** nhưng từ 2 UI khác nhau, KHÔNG suy ra TC của bên này từ TC đã viết cho bên kia.
4. **Ưu tiên test rule "lần 2 do Admin"** (REQ-17, AMB-12) — đây là rule dễ bị bỏ sót nhất vì nó thay đổi **quyền thao tác** (không chỉ nội dung hiển thị) giữa lần 1 và lần 2.
5. **Chuẩn bị bảng tra cứu mã trạng thái E2** (RISK-10) trước khi viết test data cho các trạng thái Giao hàng thất bại/Tiêu huỷ.
6. **Đặt tên TC rõ ràng cho case phí vận chuyển = 0** (AMB-13/RISK-09) để khi tính năng tính phí thật được bật, không hiểu nhầm là lỗi hồi quy.
7. **Khi có URL/tài khoản Seller thật**, chạy `/discover-system` mode HYBRID để đối chiếu 39 REQ với UI thật — đặc biệt các con số cứng (24h, 7 ngày, 2 lần) và 8 mã trạng thái tiến trình khác nhau giữa các màn hình.
8. **Không tách rời phân tích 3 phân hệ khi thiết kế test case cấp cao** — dù mỗi SRS phân tích riêng (đúng theo tài liệu nguồn), bộ test case cuối cùng cho tính năng Trả hàng/Hoàn tiền nên có ít nhất một layer test **end-to-end xuyên 3 phân hệ** (Buyer tạo → Seller/Admin duyệt → Buyer/Seller cùng thấy đúng trạng thái).

---

*Tài liệu này được sinh bởi `/analyze-requirement-document` — KHÔNG chứa test case. Bước tiếp theo: `/generate-testcases-from-requirements` hoặc `/generate-testcases-manual-rbt` cho module `ORDSEL`, ưu tiên các REQ không bị chặn bởi AMB-09.*
