---
name: skills-srs-excel-testcases
description: Skill sinh manual test case cho MỘT MỤC của tài liệu SRS (.docx / Google Docs) kết hợp thiết kế Figma, học đúng format + văn phong + kỹ thuật viết của file test case có sẵn (Excel / Google Sheet), rồi xuất ra một FILE EXCEL RIÊNG giữ nguyên format file mẫu (header, style, công thức ID & thống kê, dropdown Trạng thái) — kèm sheet "Kỹ thuật thiết kế TC" (bảng quyết định, sơ đồ chuyển trạng thái, giá trị biên). Không sửa trực tiếp Google Sheet.
---

# SRS + Figma → Test Case Excel theo format file mẫu

## Khi nào dùng

- Người dùng đưa **link Figma + link SRS (kèm số mục, VD `1.3.4`) + link file TC có sẵn**, muốn viết TC bổ sung cho mục đó "giống các TC trước"
- Đầu ra phải là **file Excel riêng** (không ghi thẳng vào Google Sheet)
- Dự án đã có file TC dạng bảng "KỊCH BẢN KIỂM THỬ" và cần TC mới khớp format để dán/gộp vào

Không dùng khi: cần TC dạng Markdown trong `docs/testcases/` theo khung 4 vòng → dùng `skills-rbt-manual-testing`. Chỉ cần phân tích requirement, chưa viết TC → `/analyze-requirement-document`.

## Đầu vào

| Đầu vào | Bắt buộc | Ghi chú |
|---|---|---|
| Link SRS (Google Docs / file .docx) + **số mục** | ✅ | Nếu người dùng chỉ nói "mục 1.3.4" thì chỉ viết cho mục đó |
| Link file TC mẫu (Google Sheet / .xlsx) | ✅ | Có `gid` thì đó là sheet người dùng đang xem — ưu tiên soi sheet đó |
| Link Figma (node-id) | Nên có | Xem mục "Đọc Figma" — thường lấy qua ảnh nhúng trong SRS |
| Module / nền tảng | Tự suy | Quyết định thư mục đầu ra |

**Tái sử dụng:** nếu trong cùng phiên đã đọc Figma/SRS/file mẫu rồi (người dùng nói "dùng lại cái đã đọc") → **không tải/đọc lại**, chỉ đọc phần mới (mục SRS mới) và mở các file trung gian đã có trong scratchpad.

## Quy trình 6 bước

Scripts nằm ở `.claude/skills/skills-srs-excel-testcases/scripts/`. Trên Windows luôn đặt `PYTHONIOENCODING=utf-8`. Cần `lxml`, `openpyxl` (`pip install lxml openpyxl`). File trung gian để trong **scratchpad**, không để trong repo.

### Bước 1 — Tải nguồn

```bash
python scripts/fetch_sources.py --srs "<link Google Docs>" --tc "<link Google Sheets>" --out <scratchpad>/src
```

- Link chia sẻ công khai → tải được ngay qua URL export, **không cần trình duyệt, không cần đăng nhập**
- Script báo "không phải file Office" → file bị giới hạn quyền. Lúc đó mới thử trình duyệt đã đăng nhập (Claude in Chrome); không được nữa thì **nhờ người dùng tải file về** và đưa đường dẫn local — không đoán nội dung

### Bước 2 — Trích mục SRS

```bash
python scripts/extract_srs.py <src>/srs.docx --out <src> --section 1.3.4
```

- In mục lục toàn tài liệu, ghi `section_<mục>.txt`, giải nén ảnh vào `<src>/media/`
- Bảng field hiển thị dạng `STT | Label | Kiểu | Bắt buộc | Mô tả`, ảnh dạng `[IMG media/imageN.png]` **đúng vị trí trong mục**
- Script liệt kê các mục bị tham chiếu (`Tương tự STT x mục y`) → **đọc thêm các mục đó** trong `srs_full.txt`
- Đọc thêm các mục khác nhắc tới cùng nghiệp vụ (VD viết 1.3.4 thì đọc rule thời gian/trạng thái ở màn Danh sách, Chi tiết đơn hàng) — grep `srs_full.txt` theo từ khoá nghiệp vụ

> ⚠️ **Không dùng `python-docx` `document.tables`** — bảng field của SRS hay nằm lồng trong khối khác, python-docx bỏ sót âm thầm (đã gặp: mục 1.3.3/1.3.4 ra rỗng). `extract_srs.py` duyệt thẳng XML nên không sót.
>
> ⚠️ Google **đánh số lại tên ảnh** (`imageN.png`) mỗi lần xuất file → không ghi tên ảnh vào tài liệu lâu dài, không dùng lại tên ảnh giữa hai lần tải.

### Bước 3 — Đọc thiết kế (Figma)

Thứ tự ưu tiên:

1. **Ảnh design nhúng trong SRS** (`[IMG …]` của mục) — thường chính là ảnh export từ Figma, đã gắn đúng mục. Mở bằng Read tool để xem: text nguyên văn của toast/popup/bottom sheet, dấu `*` bắt buộc, bộ đếm ký tự, các biến thể trạng thái
2. Mở link Figma ở trình duyệt để xác nhận đúng trang/luồng (file view-only mở được không cần đăng nhập). **Canvas Figma là WebGL — không trích được text qua DOM**, ô trình duyệt nhỏ thì zoom/pan rất tốn công → chỉ dùng để xác nhận, không dùng làm nguồn chính
3. Thiếu màn nào (SRS không có ảnh) → nhờ người dùng export frame đó ra PNG, hoặc cung cấp Figma personal access token để gọi REST API `GET https://api.figma.com/v1/files/<key>/nodes?ids=<node-id>` (token để trong `.env`, **không** ghi vào tài liệu)

Ghi lại mọi chỗ **design ≠ SRS** để đưa vào cột Ghi chú.

### Bước 4 — Học format file TC mẫu

```bash
python scripts/inspect_tc_template.py <src>/tcs.xlsx                        # liệt kê sheet
python scripts/inspect_tc_template.py <src>/tcs.xlsx --sheet "<sheet>" --rows 90
```

Soi **2–3 sheet cùng loại màn hình** (VD viết màn chi tiết → soi `Chi tiết đơn hàng`, `Hủy đơn hàng`, `Đánh giá đơn hàng`) để học: cột, section, Pre-condition, cách viết Mục đích/Bước/Kết quả, mức độ tách TC, TC giao diện chuẩn, cách ghi N/A. Đối chiếu với [`references/tc_writing_rules.md`](references/tc_writing_rules.md) — file mẫu khác thì **file mẫu thắng**.

Chọn **1 sheet làm khuôn** (sheet gọn, có đủ dòng section + Pre-condition + TC, VD `QLĐH_Hủy đơn hàng`).

### Bước 5 — Phân tích & viết TC

1. Dựng khung kỹ thuật **trước** khi viết từng TC:
   - **Bảng quyết định**: thành phần UI × trạng thái/điều kiện → Hiện/Ẩn/Enable
   - **Sơ đồ chuyển trạng thái**: vòng đời đối tượng (trạng thái hiện tại → sự kiện → trạng thái kế tiếp), kể cả chuyển không hợp lệ và tranh chấp
   - **Giá trị biên**: mọi con số trong SRS (ký tự, MB, số file, ngày, giờ, số lượt) → dưới/tại/trên biên
   - **Phân vùng tương đương**: các lớp đầu vào (phương thức thanh toán, có/không voucher, loại tài khoản…)
2. Duyệt **từng dòng STT** của bảng field theo checklist ở `tc_writing_rules.md` mục 4. Mỗi dòng STT phải có ≥ 1 TC
3. Viết vào `docs/testcases/<module>/<nền-tảng>/src/tcdata_<mục>.py` theo mẫu [`references/tcdata_example.py`](references/tcdata_example.py) (`ROWS` + `TECHNIQUES`). File này **được lưu cùng file Excel** để lần sau sửa/dựng lại mà không phải viết lại
4. Cột Ghi chú: số mục/STT SRS truy vết · kỹ thuật dùng · điểm cần BA confirm

> File dữ liệu dài → tạo bằng Write tool, **không** nhét vào heredoc của Bash (Windows báo `ENAMETOOLONG`).

### Bước 6 — Xuất Excel & kiểm tra

```bash
python scripts/build_tc_excel.py --template <src>/tcs.xlsx --template-sheet "<sheet khuôn>" \
  --data docs/testcases/<module>/<nền-tảng>/src/tcdata_<mục>.py \
  --out  docs/testcases/<module>/<nền-tảng>/TCs_<MODULE>_<TenManKhongDau>_<mục>.xlsx \
  --sheet-name "<tên sheet theo quy ước file mẫu>" \
  --screen "<Tên màn hình> (SRS mục <mục>)" \
  --doc-link "SRS: <tên tài liệu> - mục <mục> | Figma: <tên file> node <node-id>"
```

Script tự:
- kiểm tra dữ liệu (thiếu Mục đích/Bước/Kết quả, TC đầu nhóm thiếu Chức năng, TC trùng) → dừng nếu lỗi
- giữ khối header + style + độ rộng cột của sheet khuôn, merge section/Pre-condition/cột Chức năng như file mẫu
- sinh **công thức** ID (`=$E$4&"-"&TEXT(COUNTA(...),"00")`) và thống kê Pass/Fail/Chưa test/Tổng giống file mẫu, dropdown `Pass,Fail,N/A` cho cột Trạng thái
- xoá các sheet khác, thêm sheet `Kỹ thuật thiết kế TC` nếu có `TECHNIQUES`

Sau khi xuất: mở lại file bằng openpyxl kiểm tra số TC, vài ô công thức, vùng merge; gửi file cho người dùng.

## Đầu ra & vị trí

```
docs/testcases/<module>/<nền-tảng>/
├── TCs_<MODULE>_<Ten_man>_<mục>.xlsx     ← giao cho người dùng
└── src/tcdata_<mục>.py                     ← nguồn dựng lại được
```

`<nền-tảng>` ∈ `web` · `mobile` · `api` (quy ước CLAUDE.md). Không để file ở gốc repo. File tải về (`srs.docx`, `tcs.xlsx`, ảnh) để ở scratchpad — **không commit** (có thể chứa dữ liệu nội bộ).

## Báo cáo cuối (Tiếng Việt, ngắn)

1. Nguồn đã đọc (mục SRS nào, ảnh design nào, sheet mẫu nào) — nói rõ nếu tái sử dụng phân tích cũ
2. Tổng số TC + số TC từng nhóm
3. Kỹ thuật đã áp dụng và nằm ở đâu trong file
4. **Danh sách điểm cần BA xác nhận** (mâu thuẫn SRS/design, thiếu giá trị, tính năng chưa làm phase này)
5. Link file

## Cấm

- ❌ Ghi thẳng vào Google Sheet của người dùng
- ❌ Bịa danh sách giá trị SRS/design không nêu (lý do, định dạng file, nội dung popup) — ghi "theo design" + Ghi chú BA confirm
- ❌ Tự chọn một bên khi SRS mâu thuẫn design/mâu thuẫn chính nó mà không ghi chú
- ❌ Ghi số tĩnh vào ô ID/thống kê khi file mẫu dùng công thức
- ❌ Viết TC cho mục khác mục người dùng yêu cầu (đọc mục khác để lấy rule thì được, nhưng TC chỉ cho mục được yêu cầu)
