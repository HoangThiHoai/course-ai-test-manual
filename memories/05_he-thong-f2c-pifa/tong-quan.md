# F2C / PIFA marketplace (Viettel Post) — tổng quan

> Hệ thống thật thứ hai trong repo. Thương hiệu trong tài liệu: "PIFA", "F2C", "Vipomall/GOM". Template TC Excel mang header **"TỔNG CÔNG TY CỔ PHẦN BƯU CHÍNH VIETTEL — KỊCH BẢN KIỂM THỬ"**.
> Danh mục chính thức (đọc trước khi làm): `docs/requirements/_f2c/README.md` — prefix, REQ kế tiếp, AMB kế tiếp, năng lực QA.

## Hai cách tài liệu cùng tồn tại

| Kiểu | Vị trí | Nội dung |
|---|---|---|
| Markdown theo chuẩn repo (namespace `_f2c/`) | `docs/requirements/_f2c/{ORDADM,ORDSEL,ORDBUY}/analysis/` · `docs/testcases/ORDBUY/` | 3 module "Quản lý đơn hàng" tách theo phân hệ Admin / Seller / Buyer (chốt 15-09-2026). TC ID `F2C_<MODULE>_TC_<3 số>`. ORDBUY có 62 TC (GỘP), phủ REQ-F2C-ORDBUY-01→33 |
| Excel theo file mẫu (skill `skills-srs-excel-testcases`) | `docs/testcases/qldh/mobile/` | `TCs_QLDH_YeuCau_TraHang_HoanTien_1.3.3.xlsx` (SRS mục 1.3.3) · `TCs_QLDH_ChiTiet_HoanTien_1.3.4.xlsx` (mục 1.3.4) — app Buyer, nguồn `src/tcdata_1.3.3.py`, `src/tcdata_1.3.4.py` |

## Nguồn

- SRS Buyer QLĐH: Google Docs `1yE1O60Z…` — "New Request v3.0.0 Domain Buyer_Quản lý đơn hàng.docx" (UC1 Xem đơn hàng, mục 1.3.1–1.3.7: Danh sách, Chi tiết, Trả hàng/Hoàn tiền…).
- File TC mẫu "TC_F2C CMS": Google Sheet `1D98QX…` (22 sheet: Quanlykho, Quanlynhaban, Chitietdonhang, Quanlychiendich…).
- File "TC_F2C CMS" còn có sheet `Function list` (danh sách chức năng cấp 1–2 + trạng thái bàn giao) và `Overview` (tổng hợp Pass/Fail/N/A/Pending từng sheet bằng tham chiếu `C2`, `C6`–`C9`). 🔒 Sheet `Overview` chứa **tài khoản VDI ghi thẳng** — không chép giá trị đó vào repo/memories.
- Bản text đã trích: `docs/requirements/_f2c/_discovery/sources/srs_order_*.txt`.

## Năng lực QA (chốt 18-09-2026, áp mọi bộ TC `_f2c/`)

Gọi API ✅ · Truy vấn CSDL ❌ · Kiểm tích hợp (Seller/Admin CMS, ĐVVC, Zalopay) ❌ · Nhật ký hoạt động ❌ · DevTools ✅. Mode khám phá **DOC** — chưa có URL/tài khoản hệ thống thật.

## Khác

- `docs/testcases/TN/mobile/TCs_TN_HoaHongGioiThieu_Ver4.0.0.xlsx` — "Thu nhập - Hoa hồng giới thiệu (SRS Ver 4.0.0)", cùng template Viettel Post, app mobile. Chưa rõ thuộc hệ thống nào (chưa có tài liệu requirements trong repo) — hỏi user khi cần làm tiếp.
