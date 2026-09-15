# 📋 Phân Tích Requirement: SRS-ORDADM-V1.1
## Luồng Trả hàng/Hoàn tiền — CMS Admin (PIFA/F2C) — delta Ver 1.1.0

## 1. Tổng Quan Ticket

| Mục | Giá trị |
|---|---|
| **Loại tài liệu** | SRS (không phải Jira ticket) — "TÀI LIỆU ĐẶC TẢ NGHIỆP VỤ CHỨC NĂNG QUẢN LÝ ĐƠN HÀNG CMS", PIFA - CMS |
| **Hệ thống / Module** | F2C (PIFA Marketplace) — module `ORDADM` (namespace `docs/requirements/_f2c/`) |
| **Phiên bản phân tích** | Ver1.1.0 — 26/08/2026 (chỉ phần **thay đổi/mới**, tô **highlight màu vàng** trong Google Doc gốc) |
| **Chuẩn bị bởi / Xác nhận bởi** | AIT / VTP |
| **Nguồn phân tích** | `docs/requirements/_f2c/_discovery/sources/srs_order_admin_cms_v1.1.txt` + bản HTML gốc (dò highlight, không lưu vào `docs/`) |
| **Dải mã đã dùng** | `REQ-F2C-ORDADM-01` → `REQ-F2C-ORDADM-38` · `AMB-15` → `AMB-17` · `RISK-11` → `RISK-13` |
| **Mã kế tiếp** | Đợt sau bắt đầu từ `REQ-F2C-ORDADM-39`. AMB/RISK tiếp tục dải chung namespace `_f2c/` |
| **Mức độ đầy đủ** | ⚠️ Đủ để sinh test case cho luồng UI Admin, nhưng phụ thuộc điểm chặn chung `AMB-02`/`AMB-09` (CMS import hoàn tiền chưa xây) — nay có bằng chứng thứ 3 xác nhận |

### ⚠️ Ghi chú phạm vi

Đã dò tự động HTML export (3087 đoạn văn, 570 đoạn nền vàng `#ffff00`, 2 class CSS). Đối chiếu với changelog Ver1.1.0:

> *"Bổ sung luồng Hoàn/Huỷ - Danh sách đơn hàng (3.1) - Chi tiết đơn hàng (3.2.2.8 -> 3.2.2.11)"*

Khớp chính xác — toàn bộ đoạn tô vàng nằm gọn trong mục 3.1 (một phần) và 3.2.2.8→3.2.2.11 (4 mục con, tương đương 3.2.2.9→3.2.2.12 của tài liệu Seller — lệch 1 số thứ tự do Admin có ít mục trạng thái con hơn trước đó).

**Đây là SRS thứ 3 phân tích cho cùng 1 tính năng** (sau `ORDBUY` và `ORDSEL`) — nhìn từ góc CMS Admin. Nội dung **rất giống** tài liệu Seller (nhiều đoạn giống hệt từng chữ), phần phân tích dưới đây **tập trung nêu bật khác biệt riêng của Admin** thay vì lặp lại toàn bộ mô tả đã có ở [`ORDSEL/analysis/analysis_SRS-ORDSEL-V4.md`](../../ORDSEL/analysis/analysis_SRS-ORDSEL-V4.md) — mỗi REQ vẫn được trích dẫn nguồn riêng và cấp mã riêng cho module `ORDADM` theo đúng quy tắc.

**Không thuộc phạm vi phân tích này**: 3.1 STT1-18/20-23 (không bôi vàng), 3.2.2.1→3.2.2.7, field "Lịch sử thao tác" (xuất hiện ở mọi màn Admin nhưng **không được bôi vàng** — pre-existing, xem AMB-15/RISK-13), 3.3 trở đi.

## 2. User Story

Không có format chuẩn. Trích mục đích (I.1):

> *"Tài liệu này được xây dựng với mục đích mô tả các luồng chức năng Quản lý đơn hàng phân hệ Admin/CMS"*

Diễn giải riêng phần delta: **Là Admin, tôi muốn xử lý các yêu cầu Trả hàng/Hoàn tiền mà Nhà bán không xử lý kịp hoặc đã bị từ chối lần đầu, để đảm bảo Buyer luôn nhận được phản hồi trong thời gian cam kết.**

## 3. Phạm Vi Áp Dụng (Scope)

| Trong phạm vi | Vị trí | Ghi chú |
|---|---|---|
| Điều kiện lọc tab "Trả hàng"/"Đã hoàn thành" trên Danh sách đơn hàng | 3.1, phần "Điều kiện đầu vào" | — |
| Action "Phê duyệt" trong menu Thao tác của tab Trả hàng | 3.1 STT16 | Chỉ hiện đúng 2 điều kiện |
| 6 field mới trên card đơn hàng | 3.1 STT19, STT24→28 | STT19 "Mã yêu cầu" là field **chỉ có ở Admin**, không xuất hiện tương ứng ở card Seller |
| Chi tiết đơn hàng — Trả hàng (Chờ xét duyệt/…/Hoàn tiền thất bại) `[MỚI toàn màn]` | 3.2.2.8 | STT1→21 |
| Chi tiết đơn hàng — Giao hàng thất bại (Lưu kho/Tiêu huỷ) `[MỚI toàn màn]` | 3.2.2.9 | STT1→19 |
| Chi tiết đơn hàng — Đã hoàn thành `[MỚI toàn màn]` | 3.2.2.10 | STT1→15 |
| Chi tiết đơn hàng — Đã huỷ, đã thanh toán/Hoàn tiền thất bại `[MỚI]` | 3.2.2.11 (bảng 2) | STT1→17 |

| Ngoài phạm vi | Lý do |
|---|---|
| 3.1 STT1-18, 20-23; 3.2.2.1→3.2.2.7; 3.2.2.11 bảng 1 (chưa thanh toán) | Không bôi vàng |
| Field "Lịch sử thao tác" (audit log, xuất hiện ở mọi màn Admin) | Không bôi vàng — pre-existing, xem AMB-15/RISK-13 |
| Hành vi phía **Buyer**, **Seller** | Đã phân tích riêng — [`ORDBUY`](../../ORDBUY/analysis/analysis_SRS-ORDBUY-V3.md), [`ORDSEL`](../../ORDSEL/analysis/analysis_SRS-ORDSEL-V4.md) |

## 4. Acceptance Criteria — Phân Tích Chi Tiết

### 4.1. Danh sách đơn hàng — điều kiện lọc và field mới (3.1)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDADM-01` | Tab "Trả hàng" hiển thị đơn ở 1 trong 6 trạng thái: Chờ xét duyệt, Chờ giao hàng, Đang giao hàng, Đã giao hàng, Giao thất bại - Lưu kho (506), Giao thất bại - Tiêu huỷ (503) | dòng 174-175 |
| `REQ-F2C-ORDADM-02` | Tab "Đã hoàn thành" hiển thị đơn ở trạng thái Đã hoàn thành | dòng 176-177 |
| `REQ-F2C-ORDADM-03` | Action "Phê duyệt" (menu Thao tác, đơn ở tab Trả hàng) **chỉ hiển thị** khi: (a) yêu cầu lần 1 của Buyer không được Nhà bán duyệt trong 24h, HOẶC (b) yêu cầu lần 2 của Buyer | dòng 404-408 — ⭐ giải quyết dứt điểm `AMB-12` của `ORDSEL` (xem mục 4b) |
| `REQ-F2C-ORDADM-04` | Action với đơn ở tab Đã hoàn thành: chỉ "Xem chi tiết" | dòng 409-410 |
| `REQ-F2C-ORDADM-05` | STT19 "Mã yêu cầu" (Label) — hiển thị mã yêu cầu Trả hàng/Hoàn tiền ngay trên card đơn hàng. Field **chỉ tồn tại ở Admin**, không có field tương đương ở card Danh sách đơn hàng của Seller | dòng 428-436 — xem AMB-15 (cột Bắt buộc/I-O để trống) |
| `REQ-F2C-ORDADM-06` | STT24 "Trạng thái hoàn tiền" — hiện với tab Trả hàng; 1 trong 3 giá trị: Chờ hoàn tiền/Đã hoàn tiền/Hoàn tiền thất bại (2 giá trị sau lấy theo **file import của Admin** — "tính năng này chưa làm ở giai đoạn hiện tại"); trống nếu Chờ xét duyệt | dòng 475-486 — xác nhận lần 3 cho `AMB-02`/`AMB-09` |
| `REQ-F2C-ORDADM-07` | STT25 "Số lần khiếu nại" — tối đa **2 lần**/đơn; lần 1 bị Nhà bán từ chối → lần 2 chuyển Admin duyệt | dòng 487-495 — xác nhận chéo lần 3 cho con số "2 lần" (`AMB-05`/`AMB-10`) |
| `REQ-F2C-ORDADM-08` | STT26 "Phương thức trả hàng" — 1 trong 2: "Trả hàng và Hoàn tiền", "Hoàn tiền ngay (không trả hàng)" | dòng 496-503 |
| `REQ-F2C-ORDADM-09` | STT27 "Người duyệt" — giá trị: Admin hoặc tên nhà bán | dòng 504-511 |
| `REQ-F2C-ORDADM-10` | STT28 "Người huỷ" (bắt buộc = Y) — hiện tab Đã huỷ; giá trị: Admin, tên nhà bán, hoặc tên người mua | dòng 512-519 |

### 4.2. Chi tiết đơn hàng — Trả hàng (Chờ xét duyệt/…/Hoàn tiền thất bại) `[MỚI toàn màn]` (3.2.2.8)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDADM-11` | STT3 "Trạng thái đơn hàng" — chỉ hiện khi phương thức = "Trả hàng và Hoàn tiền" | dòng 2273-2280 |
| `REQ-F2C-ORDADM-12` | STT4 "Trạng thái hoàn tiền" — trống khi chưa duyệt/ĐVVC chưa lấy hàng thành công | dòng 2281-2287 |
| `REQ-F2C-ORDADM-13` | STT5 "Thời gian duyệt yêu cầu" — đếm ngược 24:00:00, format HH:MM:SS, tooltip nhắc chuyển Admin sau hạn | dòng 2288-2299 |
| `REQ-F2C-ORDADM-14` | STT6 "Thanh trạng thái" — 2 nhánh giống hệt `REQ-F2C-ORDSEL-14`: 4 bước (Trả hàng và Hoàn tiền) hoặc 3 bước (Hoàn tiền ngay) | dòng 2300-2311 |
| `REQ-F2C-ORDADM-15` | STT7 "Button Từ chối" — **chỉ hiện đúng 2 trường hợp** (nguyên văn, khác cách diễn đạt gián tiếp ở SRS Seller): *"Yêu cầu Trả hàng/Hoàn tiền lần 1 của Người mua không được Nhà bán duyệt trong 24h"* HOẶC *"Yêu cầu Trả hàng/Hoàn tiền lần 2 của Người mua"*. Luồng chọn lý do từ chối giống `REQ-F2C-ORDSEL-15` | dòng 2312-2332 |
| `REQ-F2C-ORDADM-16` | STT8 "Button Phê duyệt" — điều kiện hiện giống REQ-15. **Riêng của Admin**: nếu Admin không duyệt trong 24h, hệ thống gửi thông báo đến Admin *"Yêu cầu Trả hàng/Hoàn tiền [mã yêu cầu] đã quá hạn phê duyệt. Vui lòng kiểm tra và phê duyệt ngay để tránh khiếu nại!"* + hiển thị "Text đã quá hạn" ở màn chi tiết đơn hàng | dòng 2333-2351 — không có REQ tương đương ở `ORDSEL` (Seller không nhận nhắc nhở tương tự) |
| `REQ-F2C-ORDADM-17` | STT9 "Thông tin giao hàng & Thông tin vận chuyển" — giống `REQ-F2C-ORDSEL-18` | dòng 2352-2364 |
| `REQ-F2C-ORDADM-18` | STT10 "Thông tin Trả hàng" — giống `REQ-F2C-ORDSEL-19`, **cộng thêm field riêng của Admin**: "Lý do nhà bán từ chối" — *"hiển thị lý do nhà bán từ chối yêu cầu Trả hàng/Hoàn tiền"* (cần thiết vì Admin chỉ xử lý sau khi Seller đã từ chối hoặc không kịp xử lý) | dòng 2365-2380 — xem AMB-16 |
| `REQ-F2C-ORDADM-19` | STT11 "Thông tin hoàn tiền" — giống `REQ-F2C-ORDSEL-20` | dòng 2381-2389 |
| `REQ-F2C-ORDADM-20` | STT12→20 kế thừa STT5-19 mục 3.2.2.1 (ngoài phạm vi phân tích) | dòng 2390-2445 |
| `REQ-F2C-ORDADM-21` | STT21 "Hành trình đơn hàng" — 6 mốc sự kiện giống `REQ-F2C-ORDSEL-22` | dòng 2446-2462 |

### 4.3. Chi tiết đơn hàng — Giao hàng thất bại (Lưu kho/Tiêu huỷ) `[MỚI toàn màn]` (3.2.2.9)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDADM-22` | STT3 "Trạng thái đơn hàng" — 2 giá trị mã 506 (Lưu kho)/503 (Tiêu huỷ), giống `REQ-F2C-ORDSEL-25` | dòng 2524-2529 |
| `REQ-F2C-ORDADM-23` | STT5 "Thời gian lấy hàng lưu kho" — đếm ngược 7 ngày, hết hạn → tiêu huỷ, giống `REQ-F2C-ORDSEL-26` | dòng 2537-2547 |
| `REQ-F2C-ORDADM-24` | STT6 "Thanh trạng thái" — 4 bước + note "cứu" đơn về Đã giao (501), giống `REQ-F2C-ORDSEL-27` | dòng 2548-2555 |
| `REQ-F2C-ORDADM-25` | STT8 "Thông tin Trả hàng" — **KHÔNG có** field "Lý do nhà bán từ chối" (khác REQ-18 ở 3.2.2.8) — chỉ có field "Địa chỉ bưu cục lưu hàng" riêng cho màn này (giống `REQ-F2C-ORDSEL-28`) | dòng 2569-2583 — xem AMB-16 |
| `REQ-F2C-ORDADM-26` | STT9 "Thông tin hoàn tiền" — công thức chi tiết (trừ voucher, phí vận chuyển hiện = 0), giống `REQ-F2C-ORDSEL-29` | dòng 2584-2592 |
| `REQ-F2C-ORDADM-27` | STT10→18 kế thừa mục 3.2.2.1 (ngoài phạm vi) | dòng 2593-2648 |
| `REQ-F2C-ORDADM-28` | STT19 "Hành trình đơn hàng" — kế thừa STT21 mục 3.2.2.8 + lý do giao thất bại khi mã 506, giống `REQ-F2C-ORDSEL-31` | dòng 2649-2654 |

### 4.4. Chi tiết đơn hàng — Đã hoàn thành `[MỚI toàn màn]` (3.2.2.10)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDADM-29` | STT1 "Back" — về đúng tab "Đã hoàn thành", giống `REQ-F2C-ORDSEL-32` | dòng 2702-2707 |
| `REQ-F2C-ORDADM-30` | STT4 "Thanh trạng thái" — 5 bước không có Trả hàng, giống `REQ-F2C-ORDSEL-33` | dòng 2720-2726 |
| `REQ-F2C-ORDADM-31` | STT6→14 kế thừa mục 3.2.2.1 (ngoài phạm vi) | dòng 2740-2795 |
| `REQ-F2C-ORDADM-32` | STT15 "Hành trình đơn hàng" — nhánh "Xem thêm" khi yêu cầu bị huỷ/từ chối, giống `REQ-F2C-ORDSEL-35` | dòng 2796-2809 |

### 4.5. Chi tiết đơn hàng — Đã huỷ, đã thanh toán/Hoàn tiền thất bại `[MỚI]` (3.2.2.11, bảng 2)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDADM-33` | STT3 "Trạng thái đơn hàng" = "Đã huỷ" | dòng 3070-3075 |
| `REQ-F2C-ORDADM-34` | STT4 "Trạng thái hoàn tiền" — 1 trong 3: Chờ hoàn tiền/Đã hoàn tiền/Hoàn tiền thất bại | dòng 3076-3081 |
| `REQ-F2C-ORDADM-35` | STT5 "Thanh trạng thái" — 4 bước: Đã huỷ, Chờ hoàn tiền, Đã hoàn tiền, Hoàn tiền thất bại | dòng 3082-3088 |
| `REQ-F2C-ORDADM-36` | STT6/STT7 kế thừa STT9/STT11 mục 3.2.2.9 (REQ-17/REQ-19) | dòng 3089-3095 |
| `REQ-F2C-ORDADM-37` | STT8→16 kế thừa mục 3.2.2.1 (ngoài phạm vi) | (tiếp sau dòng 3095, cấu trúc giống Seller) |
| `REQ-F2C-ORDADM-38` | STT17 "Hành trình đơn hàng" kế thừa STT21 mục 3.2.2.8 | (cuối bảng 2) |

## 4b. Đối Chiếu Chéo Nguồn

Đây là **lần đối chiếu thứ 3** cho cùng 1 tính năng (sau `ORDBUY` ↔ `ORDSEL`). Bảng dưới đối chiếu 3 chiều:

| Hạng mục | SRS Buyer | SRS Seller | SRS Admin (tài liệu này) | Kết luận |
|---|---|---|---|---|
| Điều kiện Admin xử lý yêu cầu (thay Seller) | Không đề cập | Chỉ nói "lần 2 do Admin phê duyệt", KHÔNG nói rõ điều kiện nào kích hoạt lần 1 chuyển Admin (`AMB-12` còn treo) | Nêu **chính xác 2 điều kiện**: (a) lần 1 quá 24h Seller không duyệt, (b) mọi yêu cầu lần 2 | ✅ **Giải quyết dứt điểm `AMB-12`** của `ORDSEL` — đóng ambiguity này, cập nhật README |
| Số lần tối đa yêu cầu/khiếu nại | Suy đoán gián tiếp (`AMB-05`) | Nêu rõ "tối đa 2 lần" (`AMB-10`, đã hạ `AMB-05` xuống 🟡) | **Xác nhận lần 3**: "tối đa 2 lần khiếu nại" — cùng số liệu, cùng cách diễn đạt gần như y hệt Seller | ✅ Củng cố thêm — có thể **đóng hẳn phần con số** của `AMB-05`, chỉ còn treo phần thuật ngữ "khiếu nại" ≟ "yêu cầu Trả hàng/Hoàn tiền" |
| CMS import kết quả hoàn tiền | *"chưa làm ở giai đoạn hiện tại"* | *"chưa làm ở giai đoạn hiện tại"* | **Cùng câu chữ gần như y hệt**: *"chưa làm ở giái đoạn hiện tại"* (lỗi chính tả "giái" thay vì "giai" — dấu hiệu copy-paste giữa 3 tài liệu) | ✅ Xác nhận lần 3 — `AMB-02`/`AMB-09` là điểm chặn thật, không phải lỗi 1 tài liệu. Lỗi chính tả lặp lại củng cố giả thuyết 3 tài liệu dùng chung 1 template gốc |
| Field "Lý do nhà bán từ chối" | Không có | Không có | **Chỉ có ở Admin**, và chỉ ở màn 3.2.2.8 (không có ở 3.2.2.9) | Hợp lý về nghiệp vụ (chỉ Admin cần xem lịch sử quyết định của Seller trước khi ra quyết định lần 2) — nhưng thiếu ở 3.2.2.9 là đáng ngờ, xem `AMB-16` |

## 5. Phụ Thuộc (Dependencies)

### 5.1. Phụ thuộc `ORDBUY` và `ORDSEL` (đã phân tích)
- Toàn bộ REQ ở trên chỉ xử lý yêu cầu Buyer đã tạo (`ORDBUY`) mà Seller không xử lý kịp hoặc đã từ chối (`ORDSEL`)
- REQ-16 (thông báo quá hạn cho Admin) là điểm mới nhất trong chuỗi 3 tài liệu — chưa từng được Buyer/Seller doc nhắc tới

### 5.2. Business Rules tổng hợp (đối chiếu cả 3 tài liệu)
- Chuỗi phê duyệt đầy đủ: Buyer gửi yêu cầu → Seller có 24h → (Seller duyệt/từ chối trong hạn) HOẶC (quá hạn/là yêu cầu lần 2) → chuyển Admin → Admin có 24h (nếu quá hạn, chỉ nhận thông báo nhắc, **không** có bằng chứng hệ thống tự động làm gì tiếp theo — xem AMB-17)
- CMS import kết quả hoàn tiền là nút thắt chung của cả 3 phân hệ — xác nhận qua 3 nguồn độc lập

## 6. Phân Tích Mockup/Screenshot

Không áp dụng — SRS chỉ tham chiếu Figma và Function List (Google Sheet, chưa đọc). Ảnh minh hoạ (Hình 2.7→2.15) chỉ có caption, không trích xuất được nội dung.

## 7. Các Điểm Mơ Hồ & Rủi Ro

> Đánh số tiếp từ `AMB-14`/`RISK-10` của namespace `_f2c/`.

### 7.1. Điểm Mơ Hồ (Ambiguities)

| Mã | Câu hỏi | Nguy cơ | Mức độ | Assumption tạm |
|---|---|---|---|---|
| `AMB-15` | STT19 "Mã yêu cầu" trên Danh sách đơn hàng có cột "Bắt buộc" và "I/O" đều **để trống** — khác mọi field khác trong cùng bảng luôn có giá trị X/O rõ ràng. Là thiếu sót khi soạn tài liệu, hay field này có ý nghĩa khác (VD: ẩn/hiện có điều kiện mà tác giả quên ghi rule)? | Không chắc điều kiện hiển thị field này khi viết TC | 🟢 Low | Giả định: field luôn hiển thị (O), không bắt buộc — cần PO xác nhận |
| `AMB-16` | Field "Lý do nhà bán từ chối" chỉ có ở màn 3.2.2.8 (Trả hàng), KHÔNG có ở 3.2.2.9 (Giao hàng thất bại) dù đơn ở trạng thái Giao hàng thất bại vẫn có thể từng bị Seller từ chối trước đó (nếu sau đó Admin phê duyệt ở lần 2 rồi ĐVVC giao thất bại). Lý do từ chối cũ biến mất khỏi UI khi chuyển màn, hay đây là thiếu sót tài liệu? | Sai kỳ vọng UI khi viết TC cho đơn có lịch sử bị từ chối rồi sau đó giao thất bại | 🟡 Medium | Giả định: field bị lược bỏ có chủ đích ở màn Giao hàng thất bại (không còn liên quan trực tiếp) — cần PO xác nhận |
| `AMB-17` | Thông báo nhắc Admin khi quá 24h không duyệt (REQ-16) chỉ mô tả bằng lời, không có mockup đọc được. Kênh gửi thông báo là gì — email, in-app notification, hay cả hai? Gửi 1 lần hay lặp lại? | Không thiết kế được TC cho kênh thông báo nếu không xác nhận | 🟢 Low | Giả định: in-app notification tối thiểu (do có nhắc "Text đã quá hạn ở màn chi tiết đơn hàng") — email chưa xác nhận |

**Ambiguity từ đợt trước — nay đã có cập nhật:**
- `AMB-12` (`ORDSEL`): **ĐÃ GIẢI QUYẾT** — xem mục 4b. Đề xuất cập nhật trạng thái ở README từ 🟡 sang ✅ Đã xác nhận.
- `AMB-05`/`AMB-10` (`ORDBUY`/`ORDSEL`): con số "2 lần" nay được xác nhận **lần thứ 3** độc lập — đề xuất hạ mức xuống 🟢 Low, chỉ còn treo phần thuật ngữ.

### 7.2. Rủi Ro Kiểm Thử (Testing Risks)

| Mã | Rủi ro | Mô tả | Mitigation |
|---|---|---|---|
| `RISK-11` | Không kiểm thử được luồng hoàn tiền tự động end-to-end (phía Admin) | Xác nhận lần 3: CMS import chưa xây — cùng gốc `RISK-01`/`RISK-06` | Tách riêng nhóm TC BLOCKED, phối hợp Dev CMS |
| `RISK-12` | Số thứ tự (STT) và tên field không đồng nhất tuyệt đối giữa 3 tài liệu (Buyer/Seller/Admin) dù mô tả cùng 1 khái niệm | Dễ nhầm khi map TC chéo module chỉ dựa vào số STT — VD "STT21 Hành trình đơn hàng" ở Seller khác vị trí STT so với Admin dù cùng nội dung | Khi map test case liên module, luôn đối chiếu theo **tên field + mô tả**, không dựa vào số STT |
| `RISK-13` | Field "Lịch sử thao tác" (audit log) tồn tại ở mọi màn Admin nhưng ngoài phạm vi phân tích (không bôi vàng) | Khi viết TC cho các REQ đã phân tích, dễ vô tình mở rộng phạm vi test sang audit log (nhiều dữ liệu, nhiều tác nhân) không thuộc đợt phân tích này | Giới hạn rõ TC chỉ verify field trong dải REQ-01→38 ở trên; audit log để lại cho đợt phân tích riêng nếu cần |

## 8. Ma Trận Trạng Thái

Giống hệt ma trận đã lập ở [`ORDSEL/analysis/analysis_SRS-ORDSEL-V4.md`](../../ORDSEL/analysis/analysis_SRS-ORDSEL-V4.md) mục 8 — góc nhìn Admin không thêm trạng thái mới, chỉ thêm 2 quyền xử lý (Phê duyệt/Từ chối) tại đúng 2 điều kiện đã nêu ở REQ-15/REQ-16. Không lặp lại bảng ở đây để tránh 2 nguồn sự thật — xem file đã dẫn.

## 9. Tóm Tắt Acceptance Criteria (Checklist)

**Danh sách đơn hàng (3.1)**
- [ ] REQ-01, REQ-02 Điều kiện lọc 2 tab
- [ ] REQ-03, REQ-04 Action đúng theo trạng thái (đặc biệt REQ-03: đúng 2 điều kiện hiện "Phê duyệt")
- [ ] REQ-05 → REQ-10 6 field mới trên card

**Chi tiết — Trả hàng (3.2.2.8)**
- [ ] REQ-11 → REQ-14 Trạng thái + Progress Bar
- [ ] REQ-15, REQ-16 2 button đúng 2 điều kiện + thông báo quá hạn (riêng Admin)
- [ ] REQ-17 → REQ-19 3 field thông tin chi tiết, REQ-18 có field riêng "Lý do nhà bán từ chối"
- [ ] REQ-20, REQ-21 Kế thừa + Hành trình đơn hàng

**Chi tiết — Giao hàng thất bại (3.2.2.9)**
- [ ] REQ-22 → REQ-28 (đối chiếu: REQ-25 xác nhận field "Lý do nhà bán từ chối" **không** xuất hiện ở đây)

**Chi tiết — Đã hoàn thành (3.2.2.10)**
- [ ] REQ-29 → REQ-32

**Chi tiết — Đã huỷ, đã thanh toán (3.2.2.11 bảng 2)**
- [ ] REQ-33 → REQ-38

## 10. Khuyến Nghị Cho Kiểm Thử

1. **Đây là đợt phân tích thứ 3 — dùng để xác nhận chéo, không để bắt đầu lại từ đầu.** Khi viết TC cho `ORDADM`, tái sử dụng cấu trúc TC đã thiết kế cho `ORDSEL` (rất giống nhau), chỉ thêm/sửa đúng phần khác biệt (REQ-03, REQ-05, REQ-16, REQ-18).
2. **Ưu tiên test REQ-03 + REQ-15/16 (2 điều kiện chính xác)** — đây là rule quan trọng nhất vừa được làm rõ, nên có bộ TC boundary test đầy đủ: đúng lúc 24h, trước 24h, sau 24h, yêu cầu lần 2 bất kể thời gian.
3. **Đóng chính thức `AMB-12`** trong README trước khi sinh TC cho cả `ORDSEL` lẫn `ORDADM` — tránh 2 team viết TC dựa trên 2 giả định khác nhau về cùng 1 rule.
4. **Xác nhận AMB-16** (field "Lý do nhà bán từ chối" thiếu ở màn Giao hàng thất bại) trước khi viết TC cho luồng "đơn từng bị từ chối rồi sau đó giao thất bại" — đây là edge case dễ bị bỏ sót nếu không hỏi trước.
5. **Không mở rộng phạm vi test sang "Lịch sử thao tác"** (RISK-13) trong đợt TC này — giữ đúng ranh giới 38 REQ đã liệt kê.
6. **Khi có URL/tài khoản Admin thật**, chạy `/discover-system` mode HYBRID để đối chiếu — đặc biệt REQ-16 (thông báo quá hạn) cần xác minh kênh gửi thực tế (AMB-17).

---

*Tài liệu này được sinh bởi `/analyze-requirement-document` — KHÔNG chứa test case. Bước tiếp theo: `/generate-testcases-from-requirements` hoặc `/generate-testcases-manual-rbt` cho module `ORDADM`, ưu tiên các REQ không bị chặn bởi `AMB-02`/`AMB-09`.*
