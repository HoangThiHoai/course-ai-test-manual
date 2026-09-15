# Bản đồ hệ thống — F2C (PIFA Marketplace)

> INDEX bất biến của namespace `_f2c/`. Danh mục module + prefix: [`../README.md`](../README.md).
> Mode khám phá: **DOC** — chỉ có 3 tài liệu SRS, **chưa truy cập được hệ thống thật** (chưa có URL, chưa có tài khoản).

## 1. Bối cảnh khảo sát

| Mục | Giá trị |
|---|---|
| Ngày chạy | 2026-09-15 |
| Mode | DOC (chỉ tài liệu — user chưa cung cấp URL/tài khoản) |
| Nguồn | 3 SRS Google Docs do user cung cấp qua `/discover-system` — export dạng text, lưu tại `sources/` |
| Role đã dùng | Không có — chưa đăng nhập hệ thống nào |
| Môi trường dùng chung | ❔ Chưa hỏi được — chưa có hệ thống thật |
| Phạm vi crawl | Không crawl UI. Chỉ đọc 3 tài liệu, rút cấu trúc luồng nghiệp vụ + danh sách UC |

## 2. Sơ đồ điều hướng toàn hệ thống

❔ **Chưa xác định được** — mode DOC không có UI để crawl menu. Từ tài liệu suy ra hệ thống có **ít nhất 3 phân hệ/app riêng biệt**:

```
F2C / PIFA Marketplace
├── CMS Admin (nội bộ vận hành)   — module đã biết: Quản lý đơn hàng (ORDADM)
├── App Seller (Nhà bán)          — module đã biết: Quản lý đơn hàng (ORDSEL)
└── App Buyer (Người mua)         — module đã biết: Quản lý đơn hàng (ORDBUY)
```

Mỗi phân hệ chắc chắn còn nhiều module khác (đăng nhập/tài khoản, sản phẩm, thanh toán, khuyến mãi, vận chuyển, đánh giá...) nhưng **không có tài liệu nào đề cập** — không đưa vào bảng module ở mục 3 theo đúng nguyên tắc mode DOC (không suy diễn module ngoài tài liệu).

## 3. Bảng module tổng

| Module | Bí danh trong tài liệu | Prefix | File khám phá | Loại màn hình | Risk | Ghi chú |
|---|---|---|---|---|---|---|
| Quản lý đơn hàng — CMS Admin | "PIFA - CMS", hệ thống "PiFa Admin" | `ORDADM` | [sources/srs_order_admin_cms_v1.1.txt](sources/srs_order_admin_cms_v1.1.txt) | Danh sách (tab trạng thái) + Chi tiết + Wizard hành động (duyệt/hủy/chuẩn bị hàng) | 🔴 Cao | 6 UC: Danh sách đơn, Chi tiết đơn, Xuất báo cáo, Hủy đơn, Duyệt đơn, Chuẩn bị hàng. Tài liệu v1.1 bổ sung luồng Hoàn/Huỷ |
| Quản lý đơn hàng — App Seller | "Nhà bán", dự án gọi "F2C" | `ORDSEL` | [sources/srs_order_seller_v4.txt](sources/srs_order_seller_v4.txt) | Danh sách (7 tab trạng thái) + Chi tiết + In nhãn vận chuyển | 🔴 Cao | 6 chức năng: Danh sách đơn (7 tab: Chờ thanh toán/chờ duyệt/chờ giao hàng/đang giao hàng/đã giao hàng/trả hàng/huỷ), Chi tiết, Hủy đơn, Xuất báo cáo, Chuẩn bị hàng, In nhãn. v4.0 bổ sung luồng Hoàn/Huỷ (3.1, 3.2.2.9→3.2.2.12) |
| Quản lý đơn hàng — App Buyer | "Người mua", tích hợp Figma "GOM - Vipomall-F2C" | `ORDBUY` | [sources/srs_order_buyer_v3.txt](sources/srs_order_buyer_v3.txt) | Danh sách (6 tab cha, có sub-status) + Chi tiết + luồng Trả hàng/Hoàn tiền + eKYC | 🔴 Cao | Tài liệu dày nhất về business rule: cơ chế chống spam hủy đơn (khóa 10 phút sau 5 lần hủy/10 phút), luồng eKYC khi hoàn/huỷ, đếm ngược thanh toán tự động huỷ, luồng Trả hàng/Hoàn tiền có 4 trạng thái con (Chờ hoàn tiền/Đã hoàn tiền/Hoàn tiền thất bại/Đã huỷ) |

## 4. Bản đồ entity & phụ thuộc

- **Entity trung tâm: Đơn hàng (Order)** — vòng đời đi qua cả 3 phân hệ: Buyer tạo đơn → CMS Admin duyệt → Seller chuẩn bị hàng + tạo vận đơn → đơn vị vận chuyển (Viettel Post, tích hợp qua "F2C") giao hàng → Buyer xác nhận nhận hàng / phát sinh Trả hàng-Hoàn tiền.
- **Phụ thuộc bên ngoài quan sát được trong tài liệu:**
  - Đơn vị vận chuyển **Viettel Post** — tạo đơn vận, in nhãn, cập nhật trạng thái giao hàng
  - **F2C** — lớp trung gian giữa Seller/CMS và đơn vị vận chuyển (gửi yêu cầu tạo đơn, in nhãn)
  - **eKYC** — xác thực định danh Buyer khi thực hiện Hoàn/Huỷ (Ver 2.0.0 buyer doc)
  - **CMS** (nội bộ) — cấu hình chi phí cho đơn hàng, ảnh hưởng doanh thu Seller
- **Trạng thái đơn hàng (tổng hợp từ 3 tài liệu — CHƯA đối chiếu UI thật, có thể lệch tên gọi giữa 3 app:**
  - Chờ thanh toán → Chờ duyệt → Chờ giao hàng → Đang giao hàng → Đã giao hàng → (Đã hoàn thành | Trả hàng → Chờ hoàn tiền/Đã hoàn tiền/Hoàn tiền thất bại) | Đã huỷ
  - Buyer: có tab "Trả hàng" riêng + sub-status hoàn tiền chi tiết hơn Admin/Seller — **nghi ngờ 3 app hiển thị tập trạng thái không đồng nhất**, cần xác minh khi có UI thật

## 5. Ma trận phân quyền sơ bộ

❔ Chưa xác định — tài liệu không mô tả role/permission matrix, chỉ mô tả theo tác nhân cố định của từng app (Admin dùng CMS, Nhà bán dùng App Seller, Người mua dùng App Buyer). Không có thông tin về sub-role bên trong từng app (VD: Admin có phân cấp nhân viên điều hành vs quản trị viên hay không).

## 6. Thứ tự khảo sát đề xuất (khi có UI thật)

Chưa chốt được — phụ thuộc vào việc user cung cấp URL/tài khoản cho phân hệ nào trước. Đề xuất mặc định theo phụ thuộc nghiệp vụ (Buyer tạo đơn trước, Admin duyệt, Seller xử lý sau):

1. `ORDBUY` — đầu chuỗi vòng đời đơn hàng, tài liệu dày nhất/nhiều business rule nhất
2. `ORDADM` — điểm duyệt/kiểm soát trung gian
3. `ORDSEL` — cuối chuỗi xử lý vận chuyển

## 7. Nhật ký khám phá

| Ngày | Sự kiện | Mode | Ghi chú |
|---|---|---|---|
| 2026-09-15 | Khởi tạo lần đầu namespace `_f2c/` | DOC | Nạp 3 SRS (Admin/Seller/Buyer) đều scope "Quản lý đơn hàng". Chưa có URL/tài khoản hệ thống thật → mọi module `⬜ Chưa khảo sát UI`. User chốt: tách 3 module theo phân hệ, TC ID prefix `F2C_` |
