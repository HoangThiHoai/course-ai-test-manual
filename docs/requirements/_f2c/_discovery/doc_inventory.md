# Bản đồ phủ tài liệu — F2C (PIFA Marketplace)

> Mode DOC: chỉ có 3 tài liệu SRS, chưa đối chiếu được với UI thật (chưa có hệ thống để mở). Bảng dưới ghi mức phủ **giữa các tài liệu với nhau**, không phải đối chiếu tài liệu ↔ UI (việc đó chờ chạy lại ở mode HYBRID).

## Danh mục file gốc

| File | Nguồn (Google Docs) | Phiên bản mới nhất trong tài liệu | Dung lượng text export |
|---|---|---|---|
| [sources/srs_order_admin_cms_v1.1.txt](sources/srs_order_admin_cms_v1.1.txt) | `docs.google.com/document/d/1kvutAWADq2N1A1Cv8sNlkVlR7IaBxBdUhYvKxiwzUdM` | Ver 1.1.0 — 26/08/2026 | ~135 KB |
| [sources/srs_order_seller_v4.txt](sources/srs_order_seller_v4.txt) | `docs.google.com/document/d/1gILRzzOsl7Qk4QjdL8ttprsHQc73U-OUEOO_DqQy7Zc` | ver 4.0 — 26/08/2026 | ~125 KB |
| [sources/srs_order_buyer_v3.txt](sources/srs_order_buyer_v3.txt) | `docs.google.com/document/d/1yE1O60ZuZc_Ops3dwW-LaANq4-M8osAi` | Ver 3.0.0 — 20/08/2026 | ~75 KB |

## Bản đồ phủ tài liệu

| Vùng nghiệp vụ | Tài liệu nào phủ | Mức phủ | Ghi chú |
|---|---|---|---|
| Danh sách đơn hàng theo tab trạng thái (CMS Admin) | `srs_order_admin_cms_v1.1.txt` mục 3.1 | 🟨 Một phần | Có UC + luồng, thiếu field spec đầy đủ từng cột bảng |
| Chi tiết đơn hàng + hủy/duyệt/chuẩn bị hàng (CMS Admin) | `srs_order_admin_cms_v1.1.txt` mục 3.2 → 3.6 | 🟨 Một phần | Có luồng xử lý, thiếu ma trận phân quyền role nội bộ CMS |
| Danh sách + chi tiết + hủy + chuẩn bị hàng + in nhãn (Seller) | `srs_order_seller_v4.txt` mục 3.1 → 3.6 | 🟨 Một phần | Có sơ đồ luồng quy trình (2.1), thiếu field spec toàn bộ form |
| Luồng Hoàn/Huỷ (Seller) | `srs_order_seller_v4.txt` mục 3.1, 3.2.2.9→3.2.2.12 (thêm ở ver 4.0) | 🟨 Một phần | Mới bổ sung gần nhất trong 3 tài liệu — khả năng đây là phần user quan tâm nhất (tên lệnh gọi là "SRS Hoàn huỷ Seller") |
| Danh sách đơn theo tab (Buyer) | `srs_order_buyer_v3.txt` mục 1.3.1 | 🟩 Đầy đủ hơn 2 tài liệu kia | Có mô tả rõ 6 tab cha + sub-status, business rule đếm ngược thanh toán |
| Luồng Trả hàng/Hoàn tiền (Buyer) | `srs_order_buyer_v3.txt` mục 1.3.3, 1.3.4 (thêm ở ver 3.0.0) | 🟨 Một phần | Có luồng, có 4 trạng thái con hoàn tiền, chưa rõ tiêu chí duyệt/từ chối yêu cầu |
| Cơ chế chống spam hủy đơn (Buyer) | `srs_order_buyer_v3.txt` mục 1.3.1 STT 9, 1.3.2 STT 12 (thêm ở ver 2.0.0) | 🟩 Đầy đủ | Business rule rõ ràng: khóa tạo/huỷ đơn 10 phút sau khi huỷ 5 đơn trong 10 phút |
| eKYC khi Hoàn/Huỷ (Buyer) | `srs_order_buyer_v3.txt` (ver 2.0.0) | 🟨 Một phần | Có nhắc đến, chưa rõ toàn bộ luồng xác thực |
| Tra cứu giao dịch (Buyer) | `srs_order_buyer_v3.txt` mục 1.3.5 (thêm ở ver 2.1.0) | ⬜ Trắng — chỉ có tên mục, chưa đọc chi tiết nội dung | Cần đọc kỹ khi phân tích requirements chính thức cho `ORDBUY` |
| Mọi module khác ngoài "Quản lý đơn hàng" | — | ⬜ Trắng | Không có tài liệu nào đề cập — xem ghi chú ở `README.md` mục 1 |

## Nghi vấn cần hỏi lại user trước khi phân tích requirements chi tiết

1. Tên lệnh gọi 3 tài liệu là "SRS Hoàn huỷ Seller / SRS Admin / SRS Buyer" — nhưng cả 3 file thực chất là SRS **toàn bộ module Quản lý đơn hàng** (Hoàn/Huỷ chỉ là phần bổ sung mới nhất). Xác nhận: khi chạy `/analyze-requirement-document` hoặc `/generate-requirements-from-website` tiếp theo, có phân tích **toàn bộ** nội dung Quản lý đơn hàng, hay **chỉ** phần Hoàn/Huỷ (mục 3.1/3.2.2.9-12 Seller, 3.1/3.2.2.8-11 Admin, 1.3.1/1.3.3/1.3.4 Buyer)?
2. 3 tài liệu có vẻ mô tả cùng một luồng "Đơn hàng" nhưng trạng thái/tên tab không hoàn toàn khớp nhau giữa Admin/Seller/Buyer (xem `system_map.md` mục 4) — đây là **thiết kế cố ý** (mỗi app hiển thị góc nhìn khác nhau) hay **tài liệu lệch pha**? Cần hỏi PO/BA khi vào bước phân tích chi tiết.
3. Function List được cả Admin và Buyer tham chiếu tới cùng 1 Google Sheet (`1Pt5sf-Ds4NyijBAD4SS9f8fyjl3zx-efMNvmR5RUn9E`) — chưa đọc, có thể chứa danh sách đầy đủ mọi chức năng của cả 2 app, giúp xác nhận ranh giới module tốt hơn. Đề xuất đọc file này ở bước phân tích tiếp theo nếu user cho phép truy cập.
