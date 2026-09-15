# 📋 Phân Tích Requirement: SRS-ORDBUY-V3
## Luồng Trả hàng/Hoàn tiền — App Buyer (PIFA/F2C) — delta Ver 3.0.0

## 1. Tổng Quan Ticket

| Mục | Giá trị |
|---|---|
| **Loại tài liệu** | SRS (không phải Jira ticket) — "TÀI LIỆU NEW REQUEST ĐẶC TẢ NGHIỆP VỤ CHỨC NĂNG QUẢN LÝ ĐƠN HÀNG PHÂN HỆ BUYER (NGƯỜI MUA)" |
| **Hệ thống / Module** | F2C (PIFA Marketplace) — module `ORDBUY` (namespace `docs/requirements/_f2c/`) |
| **Phiên bản phân tích** | Ver 3.0.0 — 20/08/2026 (chỉ phần **thay đổi/mới** so với Ver 2.1.0, được tác giả tài liệu tô **highlight màu vàng**) |
| **Chuẩn bị bởi / Xác nhận bởi** | AIT / VTP |
| **Nguồn phân tích** | 1 file: `docs/requirements/_f2c/_discovery/sources/srs_order_buyer_v3.txt` (export text từ Google Docs) + bản HTML gốc (để dò định dạng highlight — không lưu vào `docs/`, chỉ dùng nội bộ khi phân tích) |
| **Dải mã đã dùng** | `REQ-F2C-ORDBUY-01` → `REQ-F2C-ORDBUY-33` · `AMB-01` → `AMB-08` · `RISK-01` → `RISK-05` |
| **Mã kế tiếp** | Đợt sau bắt đầu từ `REQ-F2C-ORDBUY-34` — KHÔNG đánh lại từ 01 |
| **Mức độ đầy đủ** | ⚠️ **Đủ để sinh test case cho luồng UI**, nhưng **thiếu** đặc tả phía CMS Admin (duyệt/từ chối yêu cầu, import kết quả hoàn tiền) và thiếu ngưỡng chính xác cho 2 rule quan trọng (xem AMB-01, AMB-05) |

### ⚠️ Ghi chú phạm vi (BẮT BUỘC đọc trước khi dùng tài liệu này)

Theo yêu cầu của user, tài liệu này **CHỈ phân tích phần được tác giả bôi màu vàng** trong Google Doc gốc — tức đúng phần liệt kê ở Nhật ký thay đổi Ver 3.0.0 của SRS:
- *"Cập nhật luồng mới Trả hàng/Hoàn tiền (1.3.1, 1.3.3, 1.3.4)"*
- *"Bổ sung trạng thái đơn hàng: Đã hoàn thành (1.3.2.5)"*
- *"Bổ sung mô tả trạng thái yêu cầu Trả hàng/Hoàn tiền (STT 9 mục 1.3.2.4)"*

Đã dò tự động toàn bộ file HTML export (1258 đoạn văn, 338 đoạn có nền vàng `#ffff00`) và đối chiếu ngược với nội dung — kết quả khớp đúng 3 mục trên, **cộng thêm một phần lớn mục 1.3.2.6 "Trạng thái Trả hàng"** cũng mang nền vàng dù **không được liệt kê tên trong changelog** → xem AMB-01.

**Không thuộc phạm vi phân tích này** (không bôi vàng, thuộc các phiên bản trước): 1.3.2.1/2.2/2.3/2.7 (Chờ thanh toán/Chờ giao hàng/Đang giao/Đã huỷ), 1.3.5 (Đánh giá đơn hàng), cơ chế chống Spam huỷ đơn (thêm ở Ver 2.0.0), luồng eKYC (Ver 2.0.0). Các phần này đã tồn tại trong SRS nhưng **chưa được phân tích ở đợt này** — cần chạy `/analyze-requirement-document` riêng nếu muốn có REQ đầy đủ cho toàn bộ module `ORDBUY`.

## 2. User Story

Tài liệu không viết theo format "As a... I want... So that..." — đây là SRS mô tả luồng nghiệp vụ trực tiếp. Trích nguyên văn mục đích (I.1, áp dụng cho toàn bộ SRS, không riêng phần delta):

> *"Tài liệu này được xây dựng nhằm mô tả các luồng chức năng và quy tắc hoạt động của chức năng Quản lý đơn hàng trong phân hệ Buyer"*

Diễn giải tương đương cho riêng phần delta Ver 3.0.0: **Là Người mua (Buyer), tôi muốn yêu cầu trả hàng/hoàn tiền cho đơn hàng đã giao khi có vấn đề, theo dõi tiến trình xử lý và nhận lại tiền vào tài khoản đã liên kết, để tôi yên tâm mua sắm trên nền tảng.**

## 3. Phạm Vi Áp Dụng (Scope)

| Trong phạm vi (đã phân tích) | Vị trí trong SRS | Ghi chú |
|---|---|---|
| Tab "Đã hoàn thành" + "Trả hàng" trên màn Danh sách đơn hàng | 1.3.1 STT5, STT10 | Nhãn trạng thái + CTA mới |
| 6 label mới hiển thị trên card đơn hàng (Trả hàng) | 1.3.1 STT14→20 | Toàn bộ field mới |
| Mô tả trạng thái yêu cầu trên màn Chi tiết đơn hàng — trạng thái Đã giao | 1.3.2.4 STT9 | Cập nhật nội dung |
| Màn Chi tiết đơn hàng — trạng thái **Đã hoàn thành** (toàn màn hình mới) | 1.3.2.5 | STT1→13 |
| Màn Chi tiết đơn hàng — trạng thái **Trả hàng** | 1.3.2.6 | STT1→11 — xem AMB-01 về việc không được nêu tên ở changelog |
| Màn **Yêu cầu Trả hàng/Hoàn tiền** (form gửi yêu cầu) | 1.3.3 | STT1→9 |
| Màn **Chi tiết hoàn tiền** (theo dõi tiến trình) | 1.3.4 | STT1→9 |

| Ngoài phạm vi (In scope của SRS nhưng KHÔNG phân tích ở đợt này) | Lý do |
|---|---|
| 1.3.1 các field khác (STT1-4, 6-9, 11-13, 21+) | Không bôi vàng — thuộc bản mô tả cũ |
| 1.3.2.1/2.2/2.3/2.7 | Không bôi vàng |
| 1.3.5 Màn hình Đánh giá đơn hàng | Không bôi vàng |
| Cơ chế chống Spam huỷ đơn, eKYC | Bôi vàng ở **Ver 2.0.0**, không phải Ver 3.0.0 — sẽ phân tích ở đợt khác nếu user yêu cầu |
| Hành vi phía **Seller** (duyệt/từ chối yêu cầu, chuẩn bị hàng hoàn) và **Admin/CMS** (import kết quả hoàn tiền) | Thuộc 2 SRS khác (`srs_order_seller_v4.txt`, `srs_order_admin_cms_v1.1.txt`) — xem AMB-06 |
| Out of Scope theo tuyên bố của chính tài liệu (mục I.2) | *"Mọi tính năng, thay đổi... không thể hiện trong thiết kế Figma hiện tại"* — SRS này chỉ tham chiếu 1 Figma link, chưa đối chiếu được vì không mở được Figma (không phải công cụ đọc file) |

## 4. Acceptance Criteria — Phân Tích Chi Tiết

> Ký hiệu `[MỚI]` = trường/màn hình hoàn toàn mới ở Ver 3.0.0. `[SỬA]` = nội dung đã có, được cập nhật.

### 4.1. Danh sách đơn hàng — tab và nhãn trạng thái mới (1.3.1)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDBUY-01` | `[MỚI]` Tab trạng thái cha "Đã hoàn thành" hiển thị đơn hàng: đã giao thành công VÀ (không phát sinh yêu cầu Trả hàng/Hoàn tiền sau 5 ngày kể từ giao thành công) HOẶC (có yêu cầu nhưng yêu cầu đó đã bị huỷ/từ chối) | `srs_order_buyer_v3.txt` dòng 200 |
| `REQ-F2C-ORDBUY-02` | `[MỚI]` Tab trạng thái cha "Trả hàng" hiển thị đơn hàng có yêu cầu Trả hàng/Hoàn tiền đang chờ xử lý HOẶC đã được phê duyệt và đang xử lý hoàn tiền | dòng 201 |
| `REQ-F2C-ORDBUY-03` | `[SỬA]` Nhãn trạng thái hiển thị trên card đơn hàng: Tab "Đã hoàn thành" → nhãn "Đã hoàn thành"; Tab "Trả hàng" → nhãn "Trả hàng" | dòng 240-241 |
| `REQ-F2C-ORDBUY-04` | `[MỚI]` CTA trên card ở trạng thái "Trả hàng": nút "Huỷ yêu cầu hoàn tiền" — chỉ hiện với đơn đang có yêu cầu Trả hàng/Hoàn tiền | dòng 285 |
| `REQ-F2C-ORDBUY-05` | `[SỬA]` CTA trên card ở trạng thái "Đã hoàn thành": nút "Đánh giá" (đơn chưa đánh giá) hoặc "Xem đánh giá" (đơn đã đánh giá) | dòng 286 |
| `REQ-F2C-ORDBUY-06` | `[MỚI]` Field "Bạn đã huỷ yêu cầu. Còn 1 lần trả hàng/hoàn tiền" — hiện trên card đơn ở trạng thái Đã giao, khi đơn đã có 1 lần yêu cầu và Người dùng tự huỷ. Nếu đơn bị huỷ **lần thứ 2**, đổi text thành "Bạn đã huỷ yêu cầu." (không còn số lần) | dòng 353-357 |
| `REQ-F2C-ORDBUY-07` | `[MỚI]` Field "Sàn/Nhà bán đã từ chối yêu cầu. Còn 1 lần trả hàng/hoàn tiền" — hiện khi Sàn/Nhà bán từ chối phê duyệt yêu cầu lần 1. Nếu bị từ chối **lần thứ 2**, đổi text thành "Sàn/Nhà bán đã từ chối yêu cầu." | dòng 358-362 |
| `REQ-F2C-ORDBUY-08` | `[MỚI]` Field "Yêu cầu trả hàng/hoàn tiền đang chờ xử lý! [date]" — hiện ở trạng thái Trả hàng; thời gian xử lý dự kiến 24h kể từ khi gửi yêu cầu; format `[date]` = DD/MM/YYYY; onclick vào Chi tiết hoàn tiền | dòng 363-370 |
| `REQ-F2C-ORDBUY-09` | `[MỚI]` Field "Bạn cần chọn phương thức trả hàng trễ nhất vào [date]" — hiện ở trạng thái Trả hàng sau khi được duyệt; hạn chọn phương thức = 24h kể từ khi Nhà bán/Admin phê duyệt; quá hạn → tự động chọn "Đơn vị vận chuyển đến lấy hàng" tại địa chỉ ĐVVC đã giao hàng; format `[date]` = DD/MM (**khác** format DD/MM/YYYY của field khác cùng nhóm — xem RISK-05) | dòng 371-378 |
| `REQ-F2C-ORDBUY-10` | `[MỚI]` Field "Chờ hoàn tiền [date]" — thời gian hoàn tiền dự kiến tối đa 10 ngày kể từ khi ĐVVC lấy hàng hoàn thành công; format DD/MM/YYYY | dòng 379-386 |
| `REQ-F2C-ORDBUY-11` | `[MỚI]` Field "Hoàn tiền thành công [date] - [time]"; format DD/MM/YYYY - HH:MM | dòng 387-394 |
| `REQ-F2C-ORDBUY-12` | `[MỚI]` Field "Hoàn tiền thất bại [date] - [time]"; format DD/MM/YYYY - HH:MM | dòng 395-402 |

### 4.2. Chi tiết đơn hàng — trạng thái "Đã giao" (cập nhật STT9) (1.3.2.4)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDBUY-13` | `[SỬA]` Field "Mô tả trạng thái yêu cầu trả hàng/hoàn tiền" — 3 nhánh nội dung theo trạng thái yêu cầu của Người dùng: **(a)** chưa từng yêu cầu → hiển thị hạn chót gửi yêu cầu = 5 ngày kể từ ngày ĐVVC giao hàng thành công, format DD/MM/YYYY; **(b)** đã yêu cầu 1 lần (và bị huỷ/từ chối) → hiển thị lại hạn chót tương tự nhưng format DD/MM (không năm); **(c)** đã hết lượt yêu cầu (huỷ/từ chối đủ 2 lần — xem AMB-05) → không cho gửi thêm | dòng 825-837 |
| `REQ-F2C-ORDBUY-14` | Onclick vào field trên → điều hướng màn Yêu cầu Trả hàng/Hoàn tiền (1.3.3) | dòng 836 |

### 4.3. Chi tiết đơn hàng — trạng thái "Đã hoàn thành" `[MỚI toàn màn]` (1.3.2.5)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDBUY-15` | Màn hình hiển thị khi đơn hàng ở tab "Đã hoàn thành". Bố cục field STT1-8, 10-11 **tái sử dụng nguyên văn** đặc tả của các mục tương ứng ở 1.3.2.1/1.3.2.2 (Back, Thông tin vận chuyển, Thông tin nhận hàng, Thông tin publisher và sản phẩm, Tổng thanh toán, Hỗ trợ, Chính sách hỗ trợ, Thông tin đặt hàng, An tâm mua sắm) | dòng 876-946 |
| `REQ-F2C-ORDBUY-16` | STT9 "Mô tả trạng thái yêu cầu trả hàng/hoàn tiền" tại màn Đã hoàn thành hiển thị 1 trong 2 nhánh: yêu cầu bị huỷ, hoặc yêu cầu bị từ chối kèm lý do từ chối; onclick → màn Yêu cầu Trả hàng/Hoàn tiền (1.3.3) | dòng 919-929 |
| `REQ-F2C-ORDBUY-17` | STT10 "Thông tin đặt hàng" liệt kê đủ 5 mốc thời gian: đặt hàng, thanh toán, ĐVVC lấy hàng, nhận hàng, **hoàn thành đơn** (mốc mới, chỉ hiện ở trạng thái Đã hoàn thành) | dòng 933-941 |
| `REQ-F2C-ORDBUY-18` | STT12 "Button Mua lại" → điều hướng màn Chi tiết sản phẩm | dòng 948-951 |
| `REQ-F2C-ORDBUY-19` | STT13 "Button Đánh giá" → điều hướng màn Đánh giá sản phẩm (mô tả tại 1.3.5 — ngoài phạm vi phân tích này) | dòng 952-956 |

### 4.4. Chi tiết đơn hàng — trạng thái "Trả hàng" `[MỚI toàn màn]` (1.3.2.6)

> ⚠️ Mục này **không được nêu tên** trong changelog Ver 3.0.0 nhưng phần lớn nội dung mang nền vàng — xem AMB-01.

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDBUY-20` | Field "Trạng thái xử lý yêu cầu Trả hàng/Hoàn tiền" hiển thị 1 trong 4 trạng thái, mỗi trạng thái kèm mốc ngày đặt hàng: **Đang chờ xử lý** · **Chờ hoàn tiền** (đã được Nhà bán/Admin phê duyệt) · **Hoàn tiền thành công** (cập nhật khi Admin import kết quả trên CMS — xem AMB-02) · **Hoàn tiền thất bại** (tương tự) | dòng 973-988 |
| `REQ-F2C-ORDBUY-21` | STT9 "Mô tả trạng thái yêu cầu trả hàng/hoàn tiền" tại màn Trả hàng — nội dung khác với STT9 ở màn Đã giao (4.2): mô tả chi tiết theo từng trạng thái con (đang chờ phê duyệt/đã phê duyệt chờ chọn phương thức/chờ hoàn tiền/hoàn tiền thành công kèm số tiền/hoàn tiền thất bại kèm lý do) | dòng 1019-1040 |

### 4.5. Màn hình Yêu cầu Trả hàng/Hoàn tiền `[MỚI]` (1.3.3)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDBUY-22` | Truy cập màn hình từ button "Yêu cầu Trả hàng/Hoàn tiền" ở màn Danh sách đơn hàng hoặc Chi tiết đơn hàng | dòng 1149 |
| `REQ-F2C-ORDBUY-23` | Field "Hoàn tiền vào" — tài khoản nhận tiền hoàn phụ thuộc phương thức thanh toán gốc: Zalopay → TKNH thanh toán qua Zalopay (**chưa phát triển** — phụ thuộc tích hợp Zalopay, xem AMB-03); QR chuyển khoản → TKNH liên kết đã khai báo lúc eKYC. Onclick → bottom sheet chọn tài khoản nhận tiền hoàn (nếu có nhiều TKNH đã liên kết) | dòng 1174-1181 |
| `REQ-F2C-ORDBUY-24` | Field "Tổng tiền hoàn" = tổng tiền Người mua đã thanh toán cho đơn hàng (không trừ phí/voucher — tài liệu không nói rõ, xem AMB-04) | dòng 1183-1186 |
| `REQ-F2C-ORDBUY-25` | Field "Lý do" — bắt buộc, chọn qua bottom sheet, chỉ được chọn **1** lý do | dòng 1188-1192 |
| `REQ-F2C-ORDBUY-26` | Field "Mô tả" — textbox, không bắt buộc. Validate: tối đa 2.000 ký tự (gồm khoảng trắng/xuống dòng, chặn nhập quá), cho phép ký tự đặc biệt, tự động trim khoảng trắng đầu/cuối | dòng 1194-1202 |
| `REQ-F2C-ORDBUY-27` | Field "Hình ảnh & video" — không bắt buộc, tối đa 6 ảnh (≤20MB/ảnh), 2 video (≤200MB/video); onclick mở thư viện/camera thiết bị tương ứng | dòng 1204-1211 |
| `REQ-F2C-ORDBUY-28` | Field "Email cập nhật tình hình" — lấy tự động từ email đăng ký; **rỗng** nếu tài khoản đăng ký bằng SĐT (không cho nhập tay — tài liệu không nói rõ, xem AMB-04) | dòng 1213-1216 |
| `REQ-F2C-ORDBUY-29` | Button "Gửi yêu cầu" — chỉ enable khi đã điền đủ trường bắt buộc (Hoàn tiền vào, Tổng tiền hoàn, Lý do). Click → gửi yêu cầu tới Seller/Admin, hiển thị toast "Yêu cầu Trả hàng/Hoàn tiền được gửi thành công. Thời gian xử lý từ 1-3 ngày. Sau thời gian này, nếu yêu cầu của bạn chưa được xử lý, liên hệ CSKH để được hỗ trợ.", điều hướng sang màn Chi tiết hoàn tiền | dòng 1218-1222 |

### 4.6. Màn hình Chi tiết hoàn tiền `[MỚI]` (1.3.4)

| REQ ID | Mô tả | Nguồn |
|---|---|---|
| `REQ-F2C-ORDBUY-30` | Field "Tiến trình hoàn tiền" (Progress Bar) — 4 mốc tuần tự: Chấp nhận/Từ chối hoàn tiền (Seller/Admin phê duyệt) → Trả hàng cho người bán (ĐVVC lấy hàng hoàn thành công) → Đã hoàn tiền / Hoàn tiền thất bại. Format thời gian mốc: DD/MM (không năm — khác format DD/MM/YYYY dùng ở nơi khác, xem RISK-05) | dòng 1256-1270 |
| `REQ-F2C-ORDBUY-31` | Button "Huỷ yêu cầu" — chỉ hiện khi Người dùng **chưa** bàn giao đơn hàng cho ĐVVC. Onclick → popup xác nhận "Bạn có chắc muốn huỷ yêu cầu Trả hàng/Hoàn tiền?" → Đồng ý: huỷ, điều hướng về Chi tiết đơn hàng + bottom sheet "Yêu cầu trả hàng/hoàn tiền đã được huỷ thành công" | dòng 1272-1283 |
| `REQ-F2C-ORDBUY-32` | Field "Chọn phương thức trả hàng" (Tab) — chỉ hiện khi yêu cầu đã được Nhà bán/Admin phê duyệt. 2 phương thức: "Đơn vị vận chuyển đến lấy hàng" (mặc định chọn) và "Trả hàng tại bưu cục" (**chưa triển khai ở Phase 1** — xem AMB-07). Sau khi xác nhận, hiển thị tên/SĐT/địa chỉ người gửi (có thể sửa địa chỉ) + thời gian dự kiến ĐVVC đến lấy (1-3 ngày kể từ khi được duyệt) | dòng 1289-1301 |
| `REQ-F2C-ORDBUY-33` | Field "Hướng dẫn trả hàng" — hiện sau khi chọn phương thức; cho phép copy mã vận đơn, tải file PDF phiếu vận đơn (file do "E2" — đơn vị/hệ thống khác — cung cấp, xem AMB-06) | dòng 1327-1341 |

## 4b. Đối Chiếu Chéo Nguồn

Chỉ có **1 nguồn văn bản** (chính SRS) cho đợt phân tích này — không có file field-spec `.xlsx` riêng, không có mockup/screenshot đính kèm được cung cấp (SRS chỉ **link** tới Figma, không phải file đọc được trực tiếp), không có comment/ticket liên quan được đưa vào. Vì vậy áp dụng đối chiếu **nội bộ trong chính văn bản** — giữa mô tả tổng quan (đầu mục 1.3.1, đầu mục 1.3.2.6) và bảng field chi tiết:

| Hạng mục | Mô tả tổng quan / changelog | Bảng field chi tiết | Kết luận |
|---|---|---|---|
| Phạm vi mục được cập nhật | Changelog chỉ nêu "1.3.1, 1.3.3, 1.3.4" + "1.3.2.5" + "STT9 mục 1.3.2.4" | Highlight thực tế phủ thêm phần lớn 1.3.2.6 | ⚠️ Xung đột nhẹ → `AMB-01` |
| Format hiển thị ngày ở nhóm field trạng thái Trả hàng (1.3.1 STT16-20) | Không nêu quy tắc chung | STT16/18/19/20 dùng DD/MM/YYYY, STT17 dùng DD/MM | ⚠️ Không nhất quán → `RISK-05` |
| Số lần tối đa được gửi yêu cầu Trả hàng/Hoàn tiền | Không phát biểu trực tiếp bằng số | Suy ra gián tiếp từ STT14/15 ("còn 1 lần" ↔ "lần thứ 2" đổi text, ngụ ý tối đa 2 lần) | ⚠️ Cần PO xác nhận con số chính thức → `AMB-05` |

## 5. Phụ Thuộc (Dependencies)

Toàn bộ luồng Trả hàng/Hoàn tiền của Buyer phụ thuộc hành động ở **2 phân hệ khác**, mỗi phân hệ có SRS riêng đã được nạp vào namespace `_f2c/` (mục `/discover-system` trước đó) nhưng **chưa được phân tích chi tiết**:

### 5.1. Phụ thuộc Seller (`srs_order_seller_v4.txt`)
- Duyệt/từ chối yêu cầu Trả hàng/Hoàn tiền của Buyer (REQ-F2C-ORDBUY-20 tham chiếu trực tiếp hành động "Nhà bán/Admin phê duyệt")
- Chuẩn bị nhận hàng hoàn khi ĐVVC giao trả

### 5.2. Phụ thuộc Admin/CMS (`srs_order_admin_cms_v1.1.txt`)
- Phê duyệt yêu cầu (song song quyền với Seller — tài liệu Buyer dùng cụm "Nhà bán/Admin" ở hầu hết chỗ, ngụ ý cả 2 vai trò đều duyệt được, nhưng không nói ai có quyền ưu tiên)
- **Import trạng thái hoàn tiền thủ công trên CMS** — đây là cơ chế **duy nhất** hiện có để đơn hàng chuyển "Hoàn tiền thành công/thất bại" (REQ-F2C-ORDBUY-20 nguồn dòng 983-987 nói rõ: *"tính năng này chưa làm ở giai đoạn hiện tại"* — nghĩa là ngay cả import thủ công cũng **chưa có** ở thời điểm viết tài liệu) → xem AMB-02, RISK-01

### 5.3. Business Rules tổng hợp (chỉ trong phạm vi phân tích)
- Toàn bộ mốc thời gian được tính từ 1 trong 3 sự kiện gốc: **ĐVVC giao hàng thành công**, **Nhà bán/Admin phê duyệt yêu cầu**, **ĐVVC lấy hàng hoàn thành công** — không có mốc nào tính từ thời điểm Buyer gửi yêu cầu (ngoại trừ hạn xử lý 24h ở REQ-F2C-ORDBUY-08)
- Tài khoản nhận tiền hoàn luôn gắn với **phương thức thanh toán gốc** của đơn hàng (Zalopay hoặc QR/TKNH liên kết) — Buyer không tự do chọn tài khoản khác ngoài danh sách đã liên kết

## 6. Phân Tích Mockup/Screenshot

Không áp dụng — tài liệu chỉ cung cấp 1 link Figma tham khảo (`figma.com/design/wYFuVvh4Jfi2zVGsoXuJ07/GOM---Vipomall-F2C`), không phải file ảnh có thể đọc trực tiếp. Nếu cần đối chiếu UI thật, đề xuất user cung cấp screenshot export từ Figma hoặc quyền truy cập, hoặc chạy `/discover-system` mode HYBRID khi có URL app thật.

## 7. Các Điểm Mơ Hồ & Rủi Ro

### 7.1. Điểm Mơ Hồ (Ambiguities)

| Mã | Câu hỏi | Nguy cơ | Mức độ | Assumption tạm |
|---|---|---|---|---|
| `AMB-01` | Mục 1.3.2.6 "Trạng thái Trả hàng" mang nền vàng gần như toàn bộ nhưng **không được liệt kê tên** trong changelog Ver 3.0.0 (chỉ nêu 1.3.1/1.3.3/1.3.4/1.3.2.5). Đây là thiếu sót khi cập nhật changelog, hay nội dung này thực ra thuộc phiên bản cũ hơn và vô tình bị tô màu? | Nếu 1.3.2.6 thực ra KHÔNG phải phần mới → REQ-F2C-ORDBUY-20/21 có thể đã tồn tại từ trước, cần đối chiếu với Ver 2.1.0 để tránh trùng lặp khi PO viết Change Request tiếp theo | 🟡 Medium | Coi 1.3.2.6 là một phần của cùng feature Trả hàng/Hoàn tiền Ver 3.0.0 (vì nội dung phụ thuộc trực tiếp REQ-F2C-ORDBUY-22→33 mới có ở Ver 3.0.0) |
| `AMB-02` | REQ-F2C-ORDBUY-20 nói "Hoàn tiền thành công/thất bại" cập nhật "sau khi Admin import trạng thái hoàn tiền trên CMS (**tính năng này chưa làm ở giai đoạn hiện tại**)". Vậy ở giai đoạn hiện tại, đơn hàng có **cách nào khác** để chuyển sang 2 trạng thái này không (VD: cập nhật thẳng qua DB, qua API nội bộ), hay tính năng này **hoàn toàn không thể test end-to-end** cho tới khi CMS import được xây? | Không xác định được cách nào để đưa đơn hàng vào trạng thái Hoàn tiền thành công/thất bại trong môi trường test → block toàn bộ TC liên quan 2 trạng thái này | 🔴 High | Giả định BLOCKED — TC cho 2 trạng thái này đánh dấu `⚪ BLOCKED chờ tính năng CMS import`, chỉ test được qua thao tác chỉnh DB trực tiếp (nếu QA có quyền — xem năng lực kiểm thử ở README) |
| `AMB-03` | Field "Hoàn tiền vào" với phương thức Zalopay ghi "phát triển sau khi tích hợp xong với Zalopay" — hiện tại tích hợp Zalopay đã xong chưa? Nếu chưa, Buyer thanh toán bằng Zalopay có được phép gửi yêu cầu Trả hàng/Hoàn tiền không, hay bị chặn hoàn toàn? | Không rõ hành vi hệ thống khi Buyer thanh toán Zalopay cố gắng vào màn Yêu cầu Trả hàng/Hoàn tiền trước khi tích hợp xong | 🟡 Medium | Giả định: nếu chưa tích hợp, ẩn/disable toàn bộ luồng Trả hàng/Hoàn tiền cho đơn thanh toán Zalopay — cần PO xác nhận |
| `AMB-04` | "Tổng tiền hoàn" = tổng tiền đã thanh toán — có **trừ phí vận chuyển, phí giao dịch, hay voucher đã dùng** không? Field "Email cập nhật tình hình" khi tài khoản đăng ký bằng SĐT thì **rỗng** — Buyer có được nhập tay email thay thế không, hay bắt buộc bỏ trống? | Rủi ro tính sai số tiền hoàn (khiếu nại tài chính) và rủi ro Buyer không nhận được thông báo tiến trình nếu không có email | 🟡 Medium | Giả định: Tổng tiền hoàn = đúng số tiền đã thanh toán (không trừ gì thêm); Email không cho nhập tay nếu tài khoản gốc là SĐT |
| `AMB-05` | Số lần tối đa Buyer được gửi yêu cầu Trả hàng/Hoàn tiền cho **1 đơn hàng** không được phát biểu trực tiếp bằng số — chỉ suy ra gián tiếp (REQ-F2C-ORDBUY-06/07: "còn 1 lần" ↔ đổi text khi "lần thứ 2"). Con số chính xác là bao nhiêu, và đây là giới hạn **per-order** hay **per-Buyer trong khung thời gian** (giống cơ chế chống Spam huỷ đơn ở Ver 2.0.0)? | Test sai boundary (test 2 lần thay vì 3, hoặc nhầm với cơ chế chống Spam khác) | 🔴 High | Giả định: tối đa **2 lần yêu cầu** trên **cùng 1 đơn hàng** (không liên quan cơ chế chống Spam theo Buyer) — CẦN PO xác nhận trước khi viết TC |
| `AMB-06` | File PDF phiếu vận đơn ở REQ-F2C-ORDBUY-33 ghi "(E2 cung cấp)" — "E2" là viết tắt của hệ thống/đối tác nào? Không xuất hiện định nghĩa ở mục 1.3 Thuật ngữ (mục này trong SRS đang để trống) | Không xác định được nguồn dữ liệu để mock/stub khi test màn Hướng dẫn trả hàng | 🟢 Low | Giả định E2 = hệ thống trung gian tương tự "F2C" nhắc ở SRS Seller (lớp trung gian gọi đơn vị vận chuyển) — cần xác nhận |
| `AMB-07` | Phương thức "Trả hàng tại bưu cục" — "chưa làm tính năng" ở Phase 1: option này có **hiển thị dạng disabled** trên Tab chọn phương thức hay **ẩn hoàn toàn**? | Sai kỳ vọng UI khi viết TC cho màn Chọn phương thức trả hàng | 🟢 Low | Giả định: ẩn hoàn toàn (chỉ hiện 1 option "Đơn vị vận chuyển đến lấy hàng") |
| `AMB-08` | Voucher giảm giá 10% khi upload đủ ảnh + video (REQ-F2C-ORDBUY-27, dòng "Nội dung hướng dẫn") — dòng riêng khác trong cùng tài liệu (ngoài phạm vi bôi vàng, dòng ~1065) ghi rõ *"Ràng buộc: Hệ thống chỉ ghi nhận tặng voucher khi... - Chưa làm giai đoạn SP8"*. Vậy UI có nên **ẩn** dòng hướng dẫn voucher này ở giai đoạn hiện tại, hay vẫn hiện (gây hiểu lầm) nhưng không cấp voucher thật? | UX gây hiểu lầm — Buyer làm theo hướng dẫn nhưng không nhận được gì | 🟡 Medium | Giả định: vẫn hiển thị hướng dẫn (theo đúng field spec), nhưng **không** có logic cấp voucher — test phải xác nhận KHÔNG có voucher xuất hiện sau khi upload đủ ảnh/video |

### 7.2. Rủi Ro Kiểm Thử (Testing Risks)

| Mã | Rủi ro | Mô tả | Mitigation |
|---|---|---|---|
| `RISK-01` | Không kiểm thử được luồng hoàn tiền tự động end-to-end | Trạng thái "Hoàn tiền thành công/thất bại" phụ thuộc thao tác thủ công qua CMS import — tính năng này bản thân SRS ghi nhận **chưa được xây** (AMB-02) | Phối hợp QA phía CMS/Admin để biết cách hiện tại đưa dữ liệu test vào 2 trạng thái này (DB seed, API nội bộ); đánh dấu rõ TC nào BLOCKED trong bộ test case |
| `RISK-02` | Nhầm lẫn giữa 2 cơ chế giới hạn khác nhau | Cơ chế chống Spam huỷ **đơn** (Ver 2.0.0, giới hạn 5 đơn/10 phút) và giới hạn số lần yêu cầu Trả hàng/Hoàn tiền **trên 1 đơn** (Ver 3.0.0, ngụ ý 2 lần — AMB-05) dễ bị viết TC gộp chung do cùng dùng từ "huỷ" | Đặt tên TC rõ ràng phân biệt 2 rule; test riêng từng rule độc lập |
| `RISK-03` | Đồng bộ trạng thái giữa 3 màn hình | Cùng 1 trạng thái hoàn tiền được hiển thị ở 3 nơi khác nhau với format khác nhau: card đơn hàng (1.3.1 STT16-20), field mô tả trên Chi tiết đơn hàng (1.3.2.6 STT9), Progress Bar (1.3.4 STT3) — dễ lệch dữ liệu nếu code cập nhật không đồng bộ cả 3 | TC phải luôn kiểm tra **đồng thời cả 3 màn hình** cho mỗi thay đổi trạng thái, không kiểm riêng lẻ từng màn |
| `RISK-04` | Format ngày không nhất quán | Ít nhất 2 chỗ dùng format khác `DD/MM/YYYY` chuẩn: STT9/1.3.2.6 dòng 1025 ghi *"Format: DD/YY/MMMM"* (nhiều khả năng là lỗi đánh máy), STT17/1.3.1 và Progress Bar/1.3.4 dùng `DD/MM` (không năm) | Xác nhận lại với PO/BA format thật trước khi viết assertion cứng cho từng field; KHÔNG giả định `DD/YY/MMMM` là format chính thức — rất có thể là typo của `DD/MM/YYYY` |
| `RISK-05` | Nhiều mốc thời gian chồng chéo dễ tính sai deadline | Ít nhất 5 mốc thời hạn khác nhau đang hoạt động song song cho cùng 1 đơn hàng: 5 ngày (hạn gửi yêu cầu), 24h (hạn duyệt), 24h (hạn chọn phương thức), 1-3 ngày (ĐVVC đến lấy), 10 ngày (hạn hoàn tiền) | Vẽ ma trận trạng thái đầy đủ (mục 8) trước khi viết TC; test riêng từng mốc với dữ liệu đếm ngược giả lập (không chờ thời gian thật) |

## 8. Ma Trận Trạng Thái

| Trạng thái đơn hàng (tab cha) | Điều kiện vào | Điều kiện ra / chuyển tiếp | Màn hình chi tiết tương ứng |
|---|---|---|---|
| Đã giao | ĐVVC giao hàng thành công, hoặc Buyer click "Đã nhận hàng" | → Đã hoàn thành (sau 5 ngày không yêu cầu, hoặc yêu cầu bị huỷ/từ chối đủ số lần) · → Trả hàng (Buyer gửi yêu cầu Trả hàng/Hoàn tiền thành công) | 1.3.2.4 |
| Trả hàng | Có yêu cầu Trả hàng/Hoàn tiền đang chờ xử lý hoặc đã duyệt đang xử lý hoàn tiền | Trạng thái con: Đang chờ xử lý → Chờ hoàn tiền (Nhà bán/Admin duyệt) → Hoàn tiền thành công / Hoàn tiền thất bại (Admin import CMS — xem RISK-01) | 1.3.2.6, 1.3.4 |
| Đã hoàn thành | Đã giao + không có yêu cầu hợp lệ đang xử lý (hết hạn 5 ngày, hoặc yêu cầu bị huỷ/từ chối) | Trạng thái cuối (terminal) — vẫn cho phép "Mua lại", "Đánh giá" | 1.3.2.5 |

## 9. Tóm Tắt Acceptance Criteria (Checklist)

**Danh sách đơn hàng (1.3.1)**
- [ ] REQ-01 Tab "Đã hoàn thành" lọc đúng điều kiện
- [ ] REQ-02 Tab "Trả hàng" lọc đúng điều kiện
- [ ] REQ-03 Nhãn trạng thái đúng theo tab
- [ ] REQ-04, REQ-05 CTA đúng theo trạng thái
- [ ] REQ-06, REQ-07 Text hiển thị đổi đúng theo số lần huỷ/từ chối (1 lần vs lần 2)
- [ ] REQ-08 → REQ-12 6 field mốc thời gian, đúng format, đúng điều kiện hiện/ẩn

**Chi tiết đơn hàng — Đã giao (1.3.2.4)**
- [ ] REQ-13 3 nhánh nội dung đúng theo số lần yêu cầu
- [ ] REQ-14 Onclick điều hướng đúng

**Chi tiết đơn hàng — Đã hoàn thành (1.3.2.5)**
- [ ] REQ-15 Tái sử dụng đúng field từ 1.3.2.1/1.3.2.2
- [ ] REQ-16 Nội dung mô tả trạng thái yêu cầu (2 nhánh)
- [ ] REQ-17 Đủ 5 mốc thời gian, mốc "hoàn thành đơn" chỉ hiện đúng trạng thái
- [ ] REQ-18, REQ-19 2 button điều hướng đúng

**Chi tiết đơn hàng — Trả hàng (1.3.2.6)**
- [ ] REQ-20 4 trạng thái con đúng điều kiện + mốc ngày
- [ ] REQ-21 Nội dung mô tả theo từng trạng thái con

**Yêu cầu Trả hàng/Hoàn tiền (1.3.3)**
- [ ] REQ-22 Truy cập đúng 2 điểm vào
- [ ] REQ-23 "Hoàn tiền vào" đúng theo phương thức thanh toán gốc
- [ ] REQ-24 "Tổng tiền hoàn" tính đúng
- [ ] REQ-25 "Lý do" bắt buộc, chỉ chọn 1
- [ ] REQ-26 "Mô tả" validate đúng (2000 ký tự, trim, ký tự đặc biệt)
- [ ] REQ-27 Upload ảnh/video đúng giới hạn số lượng + dung lượng
- [ ] REQ-28 "Email" tự động điền/rỗng đúng điều kiện
- [ ] REQ-29 Button "Gửi yêu cầu" enable/disable đúng, gửi thành công đúng luồng

**Chi tiết hoàn tiền (1.3.4)**
- [ ] REQ-30 Progress Bar đúng 4 mốc, đúng điều kiện
- [ ] REQ-31 "Huỷ yêu cầu" đúng điều kiện hiện + luồng xác nhận
- [ ] REQ-32 "Chọn phương thức trả hàng" đúng điều kiện hiện + mặc định + luồng xác nhận
- [ ] REQ-33 "Hướng dẫn trả hàng" copy mã vận đơn + tải PDF

## 10. Khuyến Nghị Cho Kiểm Thử

1. **Xác nhận AMB-02 và AMB-05 với PO/BA trước khi viết test case** — đây là 2 điểm chặn cao nhất: không có 2 con số/cơ chế này, không thể viết test boundary chính xác cho phần lõi của feature (giới hạn số lần yêu cầu + luồng hoàn tiền thành công/thất bại).
2. **Tách riêng nhóm TC "BLOCKED chờ CMS import"** (RISK-01) ngay từ đầu để không lẫn với nhóm TC test được ngay trên UI Buyer — tránh báo cáo sai tỷ lệ pass/fail.
3. **Ưu tiên vẽ lại toàn bộ ma trận trạng thái** (mục 8) thành sơ đồ trước khi phân rã test case chi tiết — nhiều mốc thời gian chồng chéo (RISK-05) rất dễ bỏ sót case nếu chỉ đọc tuần tự từng STT.
4. **Test đồng bộ 3 màn hình cùng lúc** cho mỗi thay đổi trạng thái (RISK-03) — không coi 1.3.1/1.3.2.6/1.3.4 là 3 bộ test case độc lập.
5. **Test riêng rẽ 2 cơ chế giới hạn** (chống Spam huỷ đơn vs giới hạn số lần Trả hàng/Hoàn tiền — RISK-02), đặt tên TC phân biệt rõ ràng ngay từ lúc viết để tránh nhầm lẫn khi review.
6. **Chuẩn bị dữ liệu test cho từng trạng thái con** (đang chờ xử lý / chờ hoàn tiền / thành công / thất bại) bằng cách seed thẳng DB nếu QA có quyền (kiểm tra lại năng lực kiểm thử QA đã chốt ở `docs/requirements/_f2c/README.md` — hiện đang ❔ chưa chốt vì chưa có hệ thống thật).
7. **Khi có URL/tài khoản hệ thống thật**, chạy `/discover-system` mode HYBRID cho riêng phần này để đối chiếu 33 REQ ở trên với UI thật — SRS mô tả rất chi tiết nhưng chưa có gì đảm bảo triển khai đúng 100% (đặc biệt các phần đã tự ghi "chưa làm" trong chính tài liệu: AMB-02, AMB-03, AMB-08).
8. **Format ngày (RISK-04)** — trước khi viết assertion cứng, xác nhận lại `DD/YY/MMMM` ở dòng 1025 có đúng là lỗi đánh máy của `DD/MM/YYYY` không; nếu không xác nhận được, viết assertion lỏng hơn (kiểm tra có ngày hợp lệ, không kiểm khớp định dạng tuyệt đối).

---

*Tài liệu này được sinh bởi `/analyze-requirement-document` — KHÔNG chứa test case. Bước tiếp theo: `/generate-testcases-from-requirements` hoặc `/generate-testcases-manual-rbt` cho module `ORDBUY`, ưu tiên các REQ không bị AMB 🔴 chặn.*
