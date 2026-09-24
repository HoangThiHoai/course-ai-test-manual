# Danh mục Test Cases

> Điểm vào cấp hệ thống cho toàn bộ `docs/testcases/`. Đọc file này trước khi sinh TC cho module mới — tránh trùng prefix TC ID.

## 1. Bảng danh mục module

| # | Module | Namespace | Prefix TC ID | Số TC | Độ hạt | REQ bao phủ | Tài liệu | Cập nhật |
|---|---|---|---|---|---|---|---|---|
| 1 | `ORDBUY` — Quản lý đơn hàng, App Buyer (luồng Trả hàng/Hoàn tiền v3.0.0) | `_f2c/` | `F2C_ORDBUY_TC_` | 62 | GỘP | REQ-F2C-ORDBUY-01 → 33 (33/33) | [test_cases_ORDBUY.md](ORDBUY/test_cases_ORDBUY.md) | 2026-09-18 |
| 2 | `goi-cuoc` — Quản lý gói cước, CMS admin (UC1 Danh sách, UC2 Tạo mới, UC3 Xem chi tiết, UC4 Ban hành) — Excel theo format sheet Quanlykho | — | `TC-` (công thức theo file mẫu) | 353 (233 + 120) | Excel | Truy vết theo STT SRS ở cột Ghi chú (chưa có REQ ID) | [TCs_GOICUOC_Quanlygoicuoc_UC1_UC2.xlsx](goi-cuoc/web/TCs_GOICUOC_Quanlygoicuoc_UC1_UC2.xlsx) · [TCs_GOICUOC_Chitiet_Banhanh_UC3_UC4.xlsx](goi-cuoc/web/TCs_GOICUOC_Chitiet_Banhanh_UC3_UC4.xlsx) | 24-09-2026 |

## 2. Độ phủ so với requirements

| Namespace | Module có tài liệu requirements | Module đã có TC | Ghi chú |
|---|---|---|---|
| `_f2c/` | `ORDADM`, `ORDSEL`, `ORDBUY` (xem `docs/requirements/_f2c/README.md`) | `ORDBUY` (một phần — chỉ delta v3.0.0) | `ORDADM`, `ORDSEL` chưa sinh TC |
| Hệ thống mặc định (Perfex CRM) | — | — | Chưa có module nào được phân tích |

## 3. Cấu trúc thư mục chuẩn

```
docs/testcases/
├── README.md                                   ← DANH MỤC (file này)
└── <module>/
    ├── test_cases_<module>.md                  ← INDEX — TÊN FILE BẤT BIẾN
    ├── parts/part_NN_<slug>.md                 ← khi tách (>40 TC TÁCH · >50 TC GỘP)
    ├── impact/impact_plan_<TICKET-ID>.md       ← Mode DELTA
    └── archive/test_cases_<module>_vN.md       ← phiên bản cũ
```

## 4. Kết quả thực thi

Chưa có lần thực thi nào — xem `docs/executions/` khi chạy `/execute-test-cases`.

## 5. Quy trình sử dụng tiếp theo

| Tình huống | Workflow |
|---|---|
| Requirements đổi theo ticket, module đã có TC | `/update-testcases-from-impact` (Mode DELTA) — **KHÔNG** chạy lại QUICK/FULL RBT |
| Module mới chưa có TC | `/generate-testcases-from-requirements` (QUICK) hoặc `/generate-testcases-manual-rbt` (FULL RBT) |
| Cần chạy thử trên browser thật | `/execute-test-cases` |
| Cần review chất lượng | `/review-testcases` |
| Chuyển sang automation | `/generate-automation-from-testcases` |

## 6. Nhật ký danh mục

| Ngày | Thay đổi | Lý do |
|---|---|---|
| 2026-09-18 | Khởi tạo danh mục · thêm `ORDBUY` (62 TC, độ hạt GỘP, prefix `F2C_ORDBUY_TC_`) | `/generate-testcases-from-requirements` (Mode QUICK) cho luồng Trả hàng/Hoàn tiền delta Ver 3.0.0, sau khi toàn bộ `AMB-01`→`08` được PO xác nhận |
