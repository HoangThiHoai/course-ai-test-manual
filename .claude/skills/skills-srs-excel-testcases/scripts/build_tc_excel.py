# -*- coding: utf-8 -*-
"""Dựng file Excel test case MỚI theo đúng format 1 sheet trong file TC mẫu.

Không sửa file mẫu / Google Sheet: script mở bản tải về, lấy 1 sheet làm khuôn
(giữ nguyên khối header, style, độ rộng cột), xoá nội dung cũ, ghi TC mới,
bỏ các sheet khác rồi lưu ra file mới.

Tự nhận 2 họ format "KỊCH BẢN KIỂM THỬ" (xem references/tc_writing_rules.md mục 1):
  - Format A (QLĐH mobile): header nhãn cột D / giá trị cột E, ID =$E$4&...COUNTA(cột E)
  - Format B (Quanlykho, web CMS): header nhãn cột A / giá trị cột C, ID =$C$4&...COUNTA(cột D),
    có dòng nhóm con, dropdown Pass/Fail/Pending/N/A
Công thức ID, dropdown Trạng thái, vùng merge section đều đọc từ sheet khuôn -> file mẫu thắng.

Cách dùng:
    python build_tc_excel.py --template tcs.xlsx --template-sheet "Quanlykho" \
        --data tcdata.py --out TCs_<module>_<muc>.xlsx \
        --sheet-name "Quanlydiachikho" \
        --screen "Quản lý địa chỉ kho (SRS mục 2.1)" \
        --doc-link "SRS ... mục 2.1 | Figma ... node ..." --created 07/10/2026

File --data là module Python khai báo:
    ROWS = [
      ('S', 'UC1: Chức năng ...'),                # dòng section / UC (nền màu)
      ('G', 'Kiểm tra validate'),                 # dòng nhóm con (tuỳ chọn — format B)
      ('P', 'Pre-condition: \\nBước 1: ...'),      # dòng điều kiện tiên quyết
      ('T', chức_năng|None, mục_đích|None, các_bước, kết_quả, dữ_liệu, ghi_chú[, ngày_tạo]),
    ]
    TECHNIQUES = [   # tuỳ chọn -> sinh sheet "Kỹ thuật thiết kế TC"
      {'title': '1. BẢNG QUYẾT ĐỊNH ...', 'header': [...], 'rows': [[...], ...]},
    ]
chức_năng = None -> cùng nhóm với TC phía trên (ô cột Chức năng được merge dọc).
mục_đích = None  -> cùng mục đích với TC phía trên, khác bước/dữ liệu (ô Mục đích được merge dọc).
ngày_tạo (phần tử thứ 8) -> ngày tạo riêng của TC bổ sung; không có thì lấy --created.
"""
import argparse
import copy
import importlib.util
import re
import sys

import openpyxl
from openpyxl.styles import Alignment, Border, Font, PatternFill, Side
from openpyxl.utils import get_column_letter as L
from openpyxl.worksheet.datavalidation import DataValidation

ID_FORMULA = re.compile(
    r'^=\$?([A-Z]+)\$?(\d+)&"-"&TEXT\(COUNTA\(\$?([A-Z]+)\$?\d+:\$?[A-Z]+\$?\d+\),"(0+)"\)$', re.I)

# Nhãn trong khối header -> khoá. Giá trị nằm ở ô ngay sau vùng merge của nhãn.
HEADER_LABELS = [
    ("tên màn hình", "screen"), ("mã testcase", "code"), ("link", "link"), ("người tạo", "author"),
    ("không đạt", "fail"), ("đạt", "pass"), ("chưa test", "untested"), ("pending", "pending"),
    ("n/a", "na"), ("tổng số testcase", "total"), ("số lượng testcase", "total"),
]
HEADER_EXACT = {"chức năng": "screen", "id": "code"}


def load_data(path):
    spec = importlib.util.spec_from_file_location("tcdata", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod.ROWS, getattr(mod, "TECHNIQUES", [])


def validate(rows):
    errors, seen = [], {}
    need_func, section, group, func, purpose = True, "", "", "", ""
    for i, item in enumerate(rows):
        kind = item[0]
        if kind in ("S", "G", "P"):
            if kind == "S":
                section, group = item[1], ""
            elif kind == "G":
                group = item[1]
            need_func = need_func or kind in ("S", "G")
            continue
        if kind != "T" or len(item) not in (7, 8):
            errors.append(f"Phần tử #{i}: sai cấu trúc, cần ('T', func, purpose, steps, expected, data, note[, created])")
            continue
        _, f, p, steps, expected = item[:5]
        if need_func and not f:
            errors.append(f"Phần tử #{i} ({p}): TC đầu tiên sau section/nhóm phải có tên Chức năng")
        if f and not p:
            errors.append(f"Phần tử #{i}: TC đầu nhóm Chức năng '{f}' phải có Mục đích")
        need_func = False
        func = f or func
        purpose = p or purpose
        for label, val in (("Mục đích", purpose), ("Các bước", steps), ("Kết quả mong muốn", expected)):
            if not str(val or "").strip():
                errors.append(f"Phần tử #{i}: thiếu {label}")
        # Cùng "Kiểm tra hiển thị / 1. Kiểm tra hiển thị" lặp lại ở nhiều field là bình thường
        key = (section, group, func, purpose, steps)
        if key in seen:
            errors.append(f"Phần tử #{i}: trùng hoàn toàn với phần tử #{seen[key]} ({purpose})")
        seen[key] = i
    return errors


def style_of(cell):
    return tuple(copy.copy(x) for x in (cell.font, cell.border, cell.alignment, cell.fill, cell.number_format))


def apply(cell, sty):
    cell.font, cell.border, cell.alignment, cell.fill = (copy.copy(s) for s in sty[:4])
    cell.number_format = sty[4]


def find_col(ws, header_row, *names):
    for c in ws[header_row]:
        if c.value and str(c.value).strip() in names:
            return c.column
    return None


def find_header_row(ws):
    """Dòng tiêu đề cột: cột A = 'ID' và cùng dòng có 'Mục đích' (format B còn 1 ô 'ID' trong khối header)."""
    for c in ws["A"]:
        if str(c.value or "").strip() == "ID":
            if any(str(x.value or "").strip() == "Mục đích" for x in ws[c.row]):
                return c.row
    return None


def merged_end_col(ws, cell):
    for m in ws.merged_cells.ranges:
        if m.min_row <= cell.row <= m.max_row and m.min_col <= cell.column <= m.max_col:
            return m.max_col
    return cell.column


def header_cells_of(ws, header_row):
    found = {}
    for row in ws.iter_rows(min_row=1, max_row=header_row - 1):
        for c in row:
            txt = str(c.value or "").strip().lower()
            if not txt or txt.startswith("="):
                continue
            name = HEADER_EXACT.get(txt) or next((n for k, n in HEADER_LABELS if k in txt), None)
            if name and name not in found:
                found[name] = ws.cell(row=c.row, column=merged_end_col(ws, c) + 1)
    return found


def classify_template_rows(ws, content_start):
    """Trả về (dòng section, dòng nhóm con, dòng pre-condition, dòng TC đầu) của sheet khuôn."""
    def span(row):
        for m in ws.merged_cells.ranges:
            if m.min_row == row and m.min_col == 1 and m.max_row == row:
                return m.max_col
        return 1

    labels, pre_row, tc_row = [], None, None
    for r in range(content_start, ws.max_row + 1):
        v = str(ws.cell(row=r, column=1).value or "").strip()
        if not v:
            continue
        if v.lower().startswith("pre-condition"):
            pre_row = pre_row or r
        elif re.match(r"^[A-Za-z_]*TC[-_ ]?\d+", v) or v.startswith("="):
            tc_row = tc_row or r
        else:
            labels.append(r)
        if tc_row and pre_row and len(labels) >= 2 and labels[-1] > tc_row:
            break
    if not tc_row:
        sys.exit("[LỖI] Sheet mẫu không có dòng TC nào để lấy style")
    sec_row = labels[0] if labels else tc_row
    fill_of = lambda r: ws.cell(row=r, column=1).fill.fgColor.rgb  # noqa: E731
    group_row = next((r for r in labels[1:] if span(r) != span(sec_row) or fill_of(r) != fill_of(sec_row)),
                     sec_row)
    return sec_row, group_row, pre_row or tc_row, tc_row, span


def status_dropdown(ws, col_status, tc_row):
    if col_status:
        letter = L(col_status)
        for dv in ws.data_validations.dataValidation:
            if dv.type == "list" and f"{letter}{tc_row}" in dv.sqref:
                return dv.formula1
    return '"Pass,Fail,N/A"'


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--template", required=True)
    ap.add_argument("--template-sheet", required=True)
    ap.add_argument("--data", required=True)
    ap.add_argument("--out", required=True)
    ap.add_argument("--sheet-name", required=True)
    ap.add_argument("--screen", required=True, help="Giá trị ô 'Tên màn hình/Tên chức năng' (format B: ô 'Chức năng')")
    ap.add_argument("--doc-link", default="", help="Giá trị ô 'Link tài liệu' / 'Link TL + task'")
    ap.add_argument("--created", default="", help="Ngày tạo TC (DD/MM/YYYY) ghi vào cột 'Ngày tạo TCs'")
    ap.add_argument("--author", default="", help="Người tạo — ghi vào ô header và cột 'Người tạo TCs' nếu có")
    ap.add_argument("--prefix", default="TC-", help="Tiền tố ID khi file mẫu KHÔNG dùng công thức")
    args = ap.parse_args()

    rows, techniques = load_data(args.data)
    errs = validate(rows)
    if errs:
        print("[LỖI] Dữ liệu TC chưa hợp lệ:")
        for e in errs:
            print("  -", e)
        sys.exit(1)

    wb = openpyxl.load_workbook(args.template)
    ws = wb[args.template_sheet]
    header_row = find_header_row(ws)
    if not header_row:
        sys.exit("[LỖI] Không tìm thấy dòng tiêu đề cột (cột A = 'ID', có cột 'Mục đích') trong sheet mẫu")
    last_col = max(c.column for c in ws[header_row] if c.value)

    # Dòng tiêu đề có thể merge 2 dòng -> nội dung bắt đầu sau vùng merge
    content_start = header_row + 1
    for m in ws.merged_cells.ranges:
        if m.min_row == header_row and m.min_col == 1:
            content_start = m.max_row + 1

    sec_row, group_row, pre_row, tc_row, span = classify_template_rows(ws, content_start)
    spans = {"S": span(sec_row), "G": span(group_row), "P": span(pre_row)}
    cols = range(1, last_col + 1)
    sty = {k: {c: style_of(ws.cell(row=r, column=c)) for c in cols}
           for k, r in (("S", sec_row), ("G", group_row), ("P", pre_row), ("T", tc_row))}

    col_func = find_col(ws, header_row, "Chức năng") or 2
    col_purpose = find_col(ws, header_row, "Mục đích") or 3
    col_steps = find_col(ws, header_row, "Các bước thực hiện kiểm thử") or 4
    col_expected = find_col(ws, header_row, "Kết quả mong muốn") or 5
    col_data = find_col(ws, header_row, "Dữ liệu kiểm thử") or 6
    col_created = find_col(ws, header_row, "Ngày tạo TCs", "Ngày tạo")
    col_author = find_col(ws, header_row, "Người tạo TCs", "Người tạo")
    col_status = find_col(ws, header_row, "Trạng thái")
    col_note = find_col(ws, header_row, "Ghi chú")

    # Công thức ID của file mẫu: =$<cột mã>$<dòng mã>&"-"&TEXT(COUNTA(<cột đếm>...),"00")
    m_id = ID_FORMULA.match(str(ws.cell(row=tc_row, column=1).value or ""))
    header_cells = header_cells_of(ws, header_row)
    dropdown = status_dropdown(ws, col_status, tc_row)

    for m in list(ws.merged_cells.ranges):
        if m.min_row >= content_start:
            ws.unmerge_cells(str(m))
    ws.data_validations.dataValidation = []
    ws.delete_rows(content_start, ws.max_row - content_start + 1)

    if m_id:
        code_ref = f"${m_id.group(1).upper()}${m_id.group(2)}"
        count_letter, digits = m_id.group(3).upper(), m_id.group(4)
    elif "code" in header_cells and str(ws.cell(row=tc_row, column=1).value or "").startswith("="):
        code_ref = f"${header_cells['code'].column_letter}${header_cells['code'].row}"
        count_letter, digits = L(col_expected), "00"
    else:
        code_ref = None
        count_letter = L(col_expected)

    r, tc_no, first_tc = content_start, 0, None
    starts = {col_func: None, col_purpose: None}

    def close(col, end_row):
        if starts[col] and end_row > starts[col]:
            ws.merge_cells(start_row=starts[col], start_column=col, end_row=end_row, end_column=col)
        starts[col] = None

    for item in rows:
        kind = item[0]
        for c in cols:
            apply(ws.cell(row=r, column=c), sty["T" if kind == "T" else kind][c])
        if kind in spans:
            close(col_purpose, r - 1)
            close(col_func, r - 1)
            ws.cell(row=r, column=1, value=item[1])
            if spans[kind] > 1:
                ws.merge_cells(start_row=r, start_column=1, end_row=r, end_column=spans[kind])
            ws.row_dimensions[r].height = max(45, 16 * (item[1].count("\n") + 1)) if kind == "P" else 20
        else:
            _, func, purpose, steps, expected, data, note = item[:7]
            created = item[7] if len(item) == 8 else args.created
            tc_no += 1
            first_tc = first_tc or r
            if code_ref:
                ws.cell(row=r, column=1,
                        value=f'={code_ref}&"-"&TEXT(COUNTA(${count_letter}${first_tc}:{count_letter}{r}),"{digits}")')
            else:
                ws.cell(row=r, column=1, value=f"{args.prefix}{tc_no:02d}")
            if func:
                close(col_purpose, r - 1)
                close(col_func, r - 1)
                ws.cell(row=r, column=col_func, value=func)
                starts[col_func] = r
            if purpose:
                close(col_purpose, r - 1)
                ws.cell(row=r, column=col_purpose, value=purpose)
                starts[col_purpose] = r
            ws.cell(row=r, column=col_steps, value=steps)
            ws.cell(row=r, column=col_expected, value=expected)
            if data:
                ws.cell(row=r, column=col_data, value=data)
            if created and col_created:
                ws.cell(row=r, column=col_created, value=created)
            if args.author and col_author:
                ws.cell(row=r, column=col_author, value=args.author)
            if note and col_note:
                ws.cell(row=r, column=col_note, value=note)
            lines = max(steps.count("\n"), expected.count("\n"), len(expected) // 45) + 1
            ws.row_dimensions[r].height = max(45, min(15 * (lines + 1), 260))
        r += 1
    close(col_purpose, r - 1)
    close(col_func, r - 1)
    last_row = r - 1

    if col_status and first_tc:
        dv = DataValidation(type="list", formula1=dropdown, allow_blank=True)
        ws.add_data_validation(dv)
        dv.add(f"{L(col_status)}{first_tc}:{L(col_status)}{last_row}")

    # Khối header: thống kê bằng công thức để tự cập nhật khi tester chấm Trạng thái
    if "screen" in header_cells:
        header_cells["screen"].value = args.screen
    if "link" in header_cells and args.doc_link:
        header_cells["link"].value = args.doc_link
    if "author" in header_cells and args.author:
        header_cells["author"].value = args.author
    if first_tc and col_status:
        st = L(col_status)
        st_rng = f"${st}${first_tc}:${st}${last_row}"
        ref = {k: c.coordinate for k, c in header_cells.items()}
        formulas = {
            "pass": f'=COUNTIF({st_rng},"Pass")',
            "fail": f'=COUNTIF({st_rng},"Fail")',
            "pending": f'=COUNTIF({st_rng},"Pending")',
            "na": f'=COUNTIF({st_rng},"N/A")',
            "total": f"=COUNTA({count_letter}{first_tc}:{count_letter}{last_row})",
        }
        if {"total", "pass", "fail"} <= ref.keys():
            formulas["untested"] = f"={ref['total']}-{ref['pass']}-{ref['fail']}"
        for name, formula in formulas.items():
            if name in header_cells:
                header_cells[name].value = formula

    ws.title = args.sheet_name
    for name in list(wb.sheetnames):
        if name != ws.title:
            del wb[name]

    if techniques:
        build_technique_sheet(wb, techniques)

    wb.save(args.out)
    print(f"[OK] {args.out}: {tc_no} TC (dòng {content_start}..{last_row})"
          + (f", ID theo công thức {code_ref} đếm cột {count_letter}" if code_ref else ", ID tĩnh")
          + f", dropdown {dropdown}"
          + (f", kèm sheet 'Kỹ thuật thiết kế TC' ({len(techniques)} bảng)" if techniques else ""))


def build_technique_sheet(wb, techniques):
    ws = wb.create_sheet("Kỹ thuật thiết kế TC")
    thin = Side(style="thin")
    bd = Border(left=thin, right=thin, top=thin, bottom=thin)
    f_title = Font(name="Times New Roman", size=13, bold=True)
    f_hdr = Font(name="Times New Roman", size=12, bold=True)
    f_txt = Font(name="Times New Roman", size=12)
    fill = PatternFill("solid", fgColor="FFD8D8D8")
    width = max(len(t["header"]) for t in techniques)
    for i in range(1, width + 1):
        ws.column_dimensions[L(i)].width = 34 if i == 1 else 22

    r = 1
    for block in techniques:
        ws.cell(row=r, column=1, value=block["title"]).font = f_title
        r += 2
        for line, is_hdr in [(block["header"], True)] + [(x, False) for x in block["rows"]]:
            for i, v in enumerate(line, start=1):
                c = ws.cell(row=r, column=i, value=v)
                c.border = bd
                c.font = f_hdr if is_hdr else f_txt
                c.alignment = Alignment(horizontal="center" if is_hdr else "left",
                                        vertical="center", wrap_text=True)
                if is_hdr:
                    c.fill = fill
            ws.row_dimensions[r].height = 45 if is_hdr else 32
            r += 1
        r += 2


if __name__ == "__main__":
    main()
