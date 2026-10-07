# Viết TC Excel theo file mẫu (dự án thật) — bài học

> Quy tắc gốc: skill `.claude/skills/skills-srs-excel-testcases/SKILL.md` + `references/tc_writing_rules.md` (cấu trúc sheet, công thức ID, văn phong từng cột, 4 TC giao diện đầu màn hình, checklist phủ, xử lý mâu thuẫn). **Đọc skill đó trước** — file này chỉ ghi bài học rút ra khi dùng thật, không chép lại skill.
> Lệnh: `/generate-testcases-srs-excel`.

## Khi nào dùng skill này, khi nào không

- Dự án thật (Tammi, F2C QLĐH, TN…) có file TC dạng **"KỊCH BẢN KIỂM THỬ"** trên Google Sheet → dùng skill này, xuất `.xlsx` riêng vào `docs/testcases/<module>/<nền-tảng>/`, nguồn dữ liệu ở `src/tcdata_<mục>.py`.
- Perfex CRM / bộ TC Markdown khung 4 vòng → `skills-rbt-manual-testing`.

## Bài học khi chạy thật

1. **Xác minh nguồn đúng nghiệp vụ** trước khi đọc sâu: tìm từ khoá nghiệp vụ trong SRS/Sheet tải về. Sai → dừng, báo bảng "Nguồn | Tải được | Nội dung thực tế | Khớp?" và hỏi.
2. **Kiểm `docs/testcases/README.md` + thư mục module** xem đã có TC cho phạm vi được giao chưa. Có rồi → dừng hỏi (bổ sung hay viết lại). User chọn **bổ sung**.
3. Đọc **Figma** trước khi viết, không bỏ qua dù đã có ảnh nhúng SRS (user sẽ ngắt). Danh sách AMB là **đầu ra bắt buộc**.
4. Kiểm **trùng chéo** với các UC khác (VD UC1 đã có TC sắp xếp cột Trạng thái → bỏ nhóm trùng ở UC4).
5. Bổ sung vào bộ có sẵn: tiền tố Ghi chú `[Bổ sung dd/mm/yyyy]`, Ngày tạo riêng từng TC, **chèn đúng nhóm**, nền vàng cho bản nháp, báo **bảng ID cũ → mới** (ID là công thức đếm nên dịch theo). Chi tiết: [04_he-thong-tammi-goi-cuoc/tc-da-viet-va-quy-uoc-id.md](../04_he-thong-tammi-goi-cuoc/tc-da-viet-va-quy-uoc-id.md).
6. Bản nháp dựa trên sheet gốc: **chép nguyên sheet gốc rồi chèn** (giữ công thức ID, vùng merge, dropdown Trạng thái) — script mẫu `docs/testcases/goi-cuoc/web/src/build_insert_bosung.py`.
7. Sheet `Kỹ thuật thiết kế TC` đi kèm: bảng quyết định, bảng chuyển trạng thái, phân vùng tương đương, giá trị biên — **mỗi ô ghi ID TC tương ứng**; có 1 bảng tổng hợp các TC "Cần BA confirm".
8. Dữ liệu tạo được hay không qua UI: nếu rule SRS chặn việc tạo dữ liệu tiền điều kiện (VD "bắt đầu > hiện tại"), viết TC theo cách **tạo rồi chờ qua mốc**, và nêu thành AMB.
9. Báo cáo cuối: bảng số TC theo nhóm · kỹ thuật đã dùng · AMB cần BA xác nhận · lưu ý khi dán sang Google Sheet · danh sách file. **Không tự commit**.

## Hai họ format "KỊCH BẢN KIỂM THỬ" (đọc sheet Quanlykho 07-10-2026)

- **Format A** (mobile `QLĐH_*`): header cột D/E, ID đếm cột Kết quả, dropdown `Pass,Fail,N/A`.
- **Format B** (web CMS `Quanlykho`, file "TC_F2C CMS" `1D98QX…` — cũng là khuôn của bộ Tammi gói cước): header nhãn cột A / giá trị cột C, ID `=$C$4&…COUNTA(cột D)`, 3 cấp section (UC → nhóm con → Pre-condition), dropdown `Pass,Fail,Pending,N/A`, merge dọc cả ô Mục đích.
- Chi tiết + checklist phủ màn CRUD web CMS (mục 4b) + lỗi của file mẫu không được chép (mục 7): `.claude/skills/skills-srs-excel-testcases/references/tc_writing_rules.md`.
- `build_tc_excel.py` của skill **trước 07-10-2026 dựng sai Format B** (nhận nhầm ô `ID` ở dòng 4 làm dòng tiêu đề → xoá khối header, ID tĩnh, mất dropdown). Đã sửa: tự đọc công thức ID + dropdown của khuôn, hỗ trợ `('G', …)`, Mục đích `None`, ngày tạo riêng. Hồi quy khớp với output cũ của cả 2 format.
- `docs/testcases/goi-cuoc/web/src/build_quanlykho_format.py` (script riêng viết hồi 24-09 để né lỗi trên) giờ **trùng chức năng** với script của skill — chưa xoá, chờ user quyết.
