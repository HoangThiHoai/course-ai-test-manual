# Tammi gói cước — các bộ TC đã viết & quy ước ID

> Thư mục: `docs/testcases/goi-cuoc/web/` · nguồn dựng lại Excel: `docs/testcases/goi-cuoc/web/src/`
> Danh mục: dòng `goi-cuoc` trong `docs/testcases/README.md` (đang ghi 383 TC tới 30-09-2026 — **chưa cộng 117 TC bản nháp 02-10**).

## Các file

| File Excel | Nội dung | Số TC | Nguồn dữ liệu | Trạng thái |
|---|---|---|---|---|
| `TCs_GOICUOC_Quanlygoicuoc_UC1_UC2.xlsx` | UC1 Danh sách, UC2 Tạo mới | 233 | `src/tcdata_qlgc_uc1_uc2.py` | Commit 24-09-2026 |
| `TCs_GOICUOC_Chitiet_Banhanh_UC3_UC4.xlsx` | UC3 Xem chi tiết (TC-01…74) + UC4 Ban hành | 150 (120 cũ + 30 bổ sung) | `src/tcdata_qlgc_uc3_uc4.py` | Gộp 30-09-2026 |
| `TCs_GOICUOC_Quanlygoicuoc_UC1_CaidatbangBoloc_Bosung.xlsx` | **Bản nháp chờ user review**: chép sheet gốc "CMS-Quản lý gói cước" + chèn 117 TC (Cài đặt bảng 36 · Bộ lọc 64 · Kết hợp/ngoại lệ 17) vào dòng 113–234, ngay sau nhóm "Phân trang" UC1. Dòng mới **nền vàng** | 498 (381 + 117) | `src/tcdata_qlgc_caidatbang_boloc.py` + `src/build_insert_bosung.py` | Đã commit 07-10-2026, chưa có phản hồi review |
| `TCs_GOICUOC_CMS_Quanlydonhang.xlsx` | **CMS Quản lý đơn hàng** (bản mới, file riêng): UC1 Xem DS 70 · UC2 Tìm kiếm 30 · UC3 Bộ lọc 82 · UC4 Cài đặt bảng 22 · UC5 Chi tiết 66 · UC6 Xuất excel 2 (N/A) · UC7 Đối soát trạng thái từ Miniapp 17. Khuôn = sheet `CMS-Quản lý gói cước` của file Bosung; sheet `Kỹ thuật thiết kế TC` 6 bảng | 289 | `src/tcdata_cms_quanlydonhang.py` (helper `T(..., key)` tự đánh số để bảng kỹ thuật ghi đúng TC-xx) | 07-10-2026, đã commit (chưa push), chờ user review; 24 AMB → [amb-cms-quan-ly-don-hang.md](amb-cms-quan-ly-don-hang.md) |
| `TCs_GOICUOC_Banhanh_UC4_Bosung.xlsx` | Bản bổ sung lẻ 30 TC — **đã gộp** vào file UC3_UC4 | — | (đã xoá `tcdata_qlgc_uc4_bosung.py`) | ⚠️ **Thừa** — lúc đó file đang mở nên không xoá được; nhắc user đóng Excel rồi xoá |

Script build dùng chung: `src/build_quanlykho_format.py` (từ 07-10-2026 script của skill `build_tc_excel.py` đã làm được Format B, xem [07/tc-excel-theo-file-mau.md](../07_ky-thuat-viet-tc/tc-excel-theo-file-mau.md)) (hỗ trợ ngày tạo riêng theo TC qua `CREATED_FROM`, tìm đúng dòng tiêu đề cột, nhóm con `S2`, header merge, giữ dropdown sheet mẫu).

## Quy ước khi bổ sung TC vào bộ đã có

- Cột Ghi chú của TC bổ sung: tiền tố **`[Bổ sung dd/mm/yyyy]`**; cột Ngày tạo = ngày bổ sung, TC cũ giữ ngày cũ.
- **Chèn vào đúng nhóm** chức năng (user muốn chạy test theo từng phần), không nối cuối file.
- Sửa file `tcdata_*.py` theo kiểu **chỉ thêm dòng** (không `pprint` cả file) để diff nhỏ.
- Sau khi dựng lại: so khớp **toàn bộ TC cũ phải giống hệt** bản sao lưu.
- **ID là công thức đếm** → chèn giữa làm ID phía sau **dịch đi**. Luôn báo user **bảng ID cũ → mới**. Muốn giữ ID cũ thì dán xuống cuối sheet.

## Bảng đổi ID UC4 (gộp 30-09-2026)

UC3 (TC-01…74) giữ nguyên. UC4: TC-75…81→83…89 · 82…86→92…96 · 87…89→99…101 · 90…91→103…104 · 92→106 · 93…95→108…110 · 96…98→112…114 · 99…104→116…121 · 105…107→125…127 · 108→134 · 109→136 · 110…117→138…145 · 118…120→147…149.
TC mới: 75–82, 90–91, 97–98, 102, 105, 107, 111, 115, 122–124, 128–133, 135, 137, 146, 150.

## Bản nháp 02-10-2026 — lưu ý khi dán sang Google Sheet

- ID các TC phía sau tăng thêm **117** (TC-94…99 → TC-211…216; UC2–UC4 tăng theo). Bug report nào ghi ID cũ phải sửa.
- Xoá nền vàng trước khi dán.
- Chưa mở bằng Excel để xem hiển thị thật — mới kiểm bằng script (công thức, merge, dropdown đúng).
