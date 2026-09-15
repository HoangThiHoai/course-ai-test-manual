# Danh mục Requirements — F2C (PIFA Marketplace)

> **Điểm vào cấp hệ thống cho namespace `_f2c/`.** Đọc file này đầu tiên: module nào đã có tài liệu · prefix nào đã chiếm · mã kế tiếp · ambiguity 🔴 còn treo.
> Bản đồ hệ thống: [`_discovery/system_map.md`](_discovery/system_map.md)
> Bản đồ phủ tài liệu: [`_discovery/doc_inventory.md`](_discovery/doc_inventory.md)
>
> ⚠️ Namespace này **độc lập** với hệ thống mặc định của repo (Perfex CRM ở `docs/requirements/README.md`). Không đụng, không dùng chung prefix/REQ/TC ID với hệ thống đó.

| Thuộc tính | Giá trị |
|---|---|
| **Hệ thống** | F2C — nền tảng marketplace PIFA, gồm 3 phân hệ: CMS Admin · App Seller (Nhà bán) · App Buyer (Người mua). Tên thương hiệu xuất hiện trong tài liệu: "PIFA", "F2C", "Vipomall/GOM" |
| **URL · tài khoản** | ❔ Chưa có — mode DOC, chưa truy cập được hệ thống thật. Xem `.env` khi có |
| **Tiền tố TC ID** | `F2C_` → `F2C_<MODULE>_TC_<3 số>` (VD `F2C_ORDADM_TC_001`) — chốt 2026-09-15 |
| **Môi trường dùng chung** | ❔ Chưa chốt — chưa có hệ thống thật để hỏi; hỏi lại khi có URL/account |
| **Năng lực kiểm thử của QA** | ❔ Chưa chốt — mode DOC, chưa có hệ thống để đo |
| **Nguồn tài liệu đã nạp** | 3 file SRS (Google Docs, do user cung cấp qua lệnh `/discover-system`) — xem mục 1 |

---

## 1. Bảng danh mục module

Thứ tự dòng = thứ tự tài liệu được nạp (chưa có thứ tự khảo sát ưu tiên — mode DOC, chưa khảo sát UI).

| # | Module | Prefix | Trạng thái recon | Mức phủ tài liệu | Tài liệu nguồn | REQ đã dùng | Mã kế tiếp | AMB treo | Cập nhật |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Quản lý đơn hàng — CMS Admin | `ORDADM` | 🟨 Đang khảo sát (đã phân tích 1 phần: luồng Trả hàng/Hoàn tiền ver 1.1.0) | 🟨 Một phần | [sources/srs_order_admin_cms_v1.1.txt](_discovery/sources/srs_order_admin_cms_v1.1.txt) · [analysis/analysis_SRS-ORDADM-V1.1.md](ORDADM/analysis/analysis_SRS-ORDADM-V1.1.md) | `REQ-F2C-ORDADM-01` → `REQ-F2C-ORDADM-38` | `REQ-F2C-ORDADM-39` | AMB-15 → AMB-17 | 2026-09-15 |
| 2 | Quản lý đơn hàng — App Seller (Nhà bán) | `ORDSEL` | 🟨 Đang khảo sát (đã phân tích 1 phần: luồng Trả hàng/Hoàn tiền ver 4.0) | 🟨 Một phần | [sources/srs_order_seller_v4.txt](_discovery/sources/srs_order_seller_v4.txt) · [analysis/analysis_SRS-ORDSEL-V4.md](ORDSEL/analysis/analysis_SRS-ORDSEL-V4.md) | `REQ-F2C-ORDSEL-01` → `REQ-F2C-ORDSEL-39` | `REQ-F2C-ORDSEL-40` | AMB-09 → AMB-14 (🔴 AMB-09) | 2026-09-15 |
| 3 | Quản lý đơn hàng — App Buyer (Người mua) | `ORDBUY` | 🟨 Đang khảo sát (đã phân tích 1 phần: luồng Trả hàng/Hoàn tiền v3.0.0) | 🟨 Một phần | [sources/srs_order_buyer_v3.txt](_discovery/sources/srs_order_buyer_v3.txt) · [analysis/analysis_SRS-ORDBUY-V3.md](ORDBUY/analysis/analysis_SRS-ORDBUY-V3.md) | `REQ-F2C-ORDBUY-01` → `REQ-F2C-ORDBUY-33` | `REQ-F2C-ORDBUY-34` | AMB-01 → AMB-08 (🔴 AMB-02 · AMB-05) | 2026-09-15 |

**Tổng: 3 module** — ✅ 0 · 🟨 3 · ⬜ 0 · ⏸️ 0 · ⚪ 0. Mode khám phá: **DOC** (chỉ tài liệu, chưa truy cập được hệ thống thật) → mọi module `Trạng thái recon` = ⬜ Chưa khảo sát UI theo đúng quy tắc mode DOC.

**Bảng mã trạng thái recon:** ⬜ Chưa khảo sát · 🟨 Đang khảo sát · ✅ Đã có tài liệu · ⏸️ Hoãn · ⚪ Chưa implement

**Vì sao mức phủ chỉ 🟨 Một phần, không phải 🟩 Đầy đủ:** cả 3 tài liệu chỉ đặc tả đúng phạm vi "Quản lý đơn hàng" (danh sách, chi tiết, hủy, chuẩn bị hàng, in nhãn, hoàn/huỷ, trả hàng/hoàn tiền) — không có field spec đầy đủ mọi màn hình, không có ma trận phân quyền, không có validation message chi tiết cho từng field. Đủ để dựng khung luồng nghiệp vụ, chưa đủ để viết Field Spec hoàn chỉnh.

### Danh sách prefix đã chiếm (namespace `_f2c/`)

`ORDADM` · `ORDSEL` · `ORDBUY`

> Prefix đã cấp là **vĩnh viễn**. Đây là sổ prefix **riêng** của namespace `_f2c/` — không đối chiếu, không trùng với sổ prefix của hệ thống mặc định (`LOGIN`, `CUST`, `PRJ`...).

⚠️ **Ranh giới đã chốt với user (2026-09-15):** 1 entity nghiệp vụ "Đơn hàng" nhưng tách thành **3 module riêng theo phân hệ** (Admin/Seller/Buyer) vì là 3 app/UI hoàn toàn khác nhau, quyền và luồng xử lý khác nhau — không gộp chung 1 module.

⚠️ **Các module khác của hệ thống F2C/PIFA** (Sản phẩm, Tài khoản, Thanh toán, Khuyến mãi, Vận chuyển, Đánh giá...) **chưa có tài liệu và chưa được khảo sát** — không được liệt kê ở đây vì mode DOC không cho phép suy diễn module ngoài tài liệu đã nạp. Bổ sung khi có thêm SRS hoặc truy cập được hệ thống thật (chạy lại `/discover-system` mode ADD/HYBRID).

---

## 2. Trạng thái REQ toàn hệ thống (namespace `_f2c/`)

Chưa có module nào đã sinh tài liệu requirements → chưa có REQ nào được cấp. Bảng này khởi tạo rỗng, cập nhật khi chạy `/generate-requirements-from-website` hoặc `/analyze-requirement-document` cho từng module.

| Module | 🟢 | 🟡 | 🔴 | ⚪ | Tổng |
|---|---|---|---|---|---|
| **Tổng** | 0 | 0 | 0 | 0 | 0 |

---

## 3. Ambiguity còn treo

Mã AMB đánh số **toàn namespace `_f2c/`** (riêng, không dùng chung dải số với hệ thống mặc định). **AMB kế tiếp: `AMB-18`.**

| Mã | Mức | Nội dung | Ảnh hưởng | Cần ai trả lời | Nguồn |
|---|---|---|---|---|---|
| AMB-02 | 🔴 High | `ORDBUY` — Trạng thái "Hoàn tiền thành công/thất bại" phụ thuộc Admin import CMS, nhưng SRS tự ghi tính năng import **chưa được xây**. Xác nhận độc lập ở cả 3 SRS (Buyer/Seller/Admin — xem AMB-09 và mục 4b của `ORDADM`). Không rõ cách nào khác để test 2 trạng thái này ở giai đoạn hiện tại | Block toàn bộ TC liên quan Hoàn tiền thành công/thất bại, cả 3 module | PO / Dev CMS | [ORDBUY](ORDBUY/analysis/analysis_SRS-ORDBUY-V3.md) · [ORDSEL](ORDSEL/analysis/analysis_SRS-ORDSEL-V4.md) · [ORDADM](ORDADM/analysis/analysis_SRS-ORDADM-V1.1.md) |
| AMB-05 | 🟢 Low (hạ từ 🟡 — xác nhận độc lập lần 3 ở `ORDADM`) | Số lần tối đa Buyer được gửi yêu cầu Trả hàng/Hoàn tiền = **2 lần**, xác nhận đồng nhất ở cả SRS Seller và Admin. Chỉ còn treo: 2 thuật ngữ "khiếu nại" (Seller/Admin) và "yêu cầu Trả hàng/Hoàn tiền" (Buyer) có đồng nhất không | Rủi ro nhỏ nếu 2 thuật ngữ khác nhau | PO / BA | [ORDSEL](ORDSEL/analysis/analysis_SRS-ORDSEL-V4.md) AMB-10 · [ORDADM](ORDADM/analysis/analysis_SRS-ORDADM-V1.1.md) mục 4b |
| AMB-09 | 🔴 High | `ORDSEL` — xem AMB-02, cùng 1 điểm chặn | — | PO / Dev CMS | [ORDSEL/analysis/analysis_SRS-ORDSEL-V4.md](ORDSEL/analysis/analysis_SRS-ORDSEL-V4.md) |
| AMB-12 | ✅ Đã giải quyết | `ORDSEL` — "Sau lần 2, Seller có còn thấy nút Từ chối/Phê duyệt không?" **Đã trả lời** bởi SRS Admin: Admin chỉ xử lý đúng 2 trường hợp (lần 1 quá 24h HOẶC lần 2) → suy ra Seller chỉ xử lý được lần 1 trong hạn 24h, ngoài ra ẩn nút | Không còn block TC | — (đã đóng 2026-09-15) | [ORDADM/analysis/analysis_SRS-ORDADM-V1.1.md](ORDADM/analysis/analysis_SRS-ORDADM-V1.1.md) mục 4b |
| AMB-01 · AMB-03 · AMB-04 · AMB-06 · AMB-07 · AMB-08 | 🟡/🟢 | `ORDBUY` — xem chi tiết trong tài liệu phân tích | Xem tài liệu | PO / Dev | [ORDBUY/analysis/analysis_SRS-ORDBUY-V3.md](ORDBUY/analysis/analysis_SRS-ORDBUY-V3.md) mục 7.1 |
| AMB-10 · AMB-11 · AMB-13 · AMB-14 | 🟡/🟢 | `ORDSEL` — xem chi tiết trong tài liệu phân tích | Xem tài liệu | PO / Dev | [ORDSEL/analysis/analysis_SRS-ORDSEL-V4.md](ORDSEL/analysis/analysis_SRS-ORDSEL-V4.md) mục 7.1 |
| AMB-15 · AMB-16 · AMB-17 | 🟡/🟢 | `ORDADM` — xem chi tiết trong tài liệu phân tích | Xem tài liệu | PO / Dev | [ORDADM/analysis/analysis_SRS-ORDADM-V1.1.md](ORDADM/analysis/analysis_SRS-ORDADM-V1.1.md) mục 7.1 |

---

## 4. Cấu trúc thư mục (namespace `_f2c/`)

```
docs/requirements/_f2c/
├── README.md                              ← DANH MỤC (file này)
├── _discovery/
│   ├── system_map.md                      ← INDEX bất biến
│   ├── doc_inventory.md                   ← Bản đồ phủ tài liệu
│   └── sources/                           ← bản gốc 3 SRS (txt export từ Google Docs)
└── <module>/                              ← sẽ tạo khi chạy requirements-from-website/analyze-requirement-document
    └── requirements_<module>.md
```

## 5. Quy trình sử dụng tiếp theo

| Tình huống | Workflow | Ghi vào đâu |
|---|---|---|
| Có URL hệ thống thật + tài khoản Admin/Seller/Buyer | `/discover-system` (mode HYBRID, dùng lại 3 SRS này) | Cập nhật `system_map.md`, đối chiếu tài liệu ↔ UI, mở AMB nếu lệch pha |
| Sinh requirements chi tiết cho 1 module (đang có tài liệu 🟨) | `/analyze-requirement-document` với đúng file SRS nguồn | `<module>/analysis/` rồi `/generate-requirements-from-website` để ra `requirements_<module>.md` |
| Phát hiện thêm module khác (Sản phẩm, Tài khoản...) | `/discover-system` (mode ADD) | Thêm dòng mục 1 + cấp prefix mới trong namespace này |

## 6. Nhật ký danh mục

| Ngày | Thay đổi | Lý do |
|---|---|---|
| 2026-09-15 | `ORDADM` ⬜ → 🟨 · `REQ-F2C-ORDADM-01` → `38` · mở `AMB-15` → `AMB-17` · AMB kế tiếp `AMB-18` · **đóng `AMB-12`** (đã xác nhận qua SRS Admin) · hạ `AMB-05` 🟡 → 🟢 (xác nhận độc lập lần 3) | `/analyze-requirement-document` — phân tích luồng Trả hàng/Hoàn tiền (delta ver 1.1.0, phần bôi vàng) của `srs_order_admin_cms_v1.1.txt`. Đây là đợt phân tích thứ 3 cho cùng 1 tính năng — dùng để đối chiếu chéo với `ORDBUY`/`ORDSEL` |
| 2026-09-15 | `ORDSEL` ⬜ → 🟨 · `REQ-F2C-ORDSEL-01` → `39` · mở `AMB-09` → `AMB-14` (🔴 AMB-09) · AMB kế tiếp `AMB-15` · xác nhận chéo con số "2 lần" cho `AMB-05` (hạ 🔴 → 🟡) | `/analyze-requirement-document` — phân tích luồng Trả hàng/Hoàn tiền (delta ver 4.0, phần bôi vàng) của `srs_order_seller_v4.txt`. Highlight khớp 100% với changelog (khác `ORDBUY` có lệch nhẹ) |
| 2026-09-15 | `ORDBUY` ⬜ → 🟨 · `REQ-F2C-ORDBUY-01` → `33` · mở `AMB-01` → `AMB-08` (🔴 AMB-02, AMB-05 đưa lên mục 3) · AMB kế tiếp `AMB-09` | `/analyze-requirement-document` — phân tích luồng Trả hàng/Hoàn tiền (delta Ver 3.0.0, phần bôi vàng) của `srs_order_buyer_v3.txt`. Chưa phân tích các phần còn lại (không bôi vàng) của module `ORDBUY` |
| 2026-09-15 | Khởi tạo namespace `_f2c/` · cấp 3 prefix (`ORDADM`, `ORDSEL`, `ORDBUY`) · TC ID prefix `F2C_` chốt với user | `/discover-system` mode DOC lần đầu — 3 SRS (Admin/Seller/Buyer) đều chỉ phủ module Quản lý đơn hàng. Hệ thống mặc định của repo (Perfex CRM) đã có `docs/requirements/README.md` riêng — không đụng vào, tách namespace theo lựa chọn của user |
