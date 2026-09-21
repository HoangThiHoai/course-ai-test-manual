# -*- coding: utf-8 -*-
"""Trích nội dung SRS (.docx) theo mục, KỂ CẢ bảng lồng và ảnh design nhúng.

Vì sao không dùng python-docx `document.tables`: bảng mô tả trường thông tin của
SRS thường nằm lồng trong khối khác (sdt / ô bảng) -> python-docx bỏ sót âm thầm.
Script duyệt thẳng XML theo đúng thứ tự tài liệu.

Cách dùng:
    python extract_srs.py <srs.docx> --out <thư_mục>                 # trích toàn bộ
    python extract_srs.py <srs.docx> --out <thư_mục> --section 1.3.4 # in riêng 1 mục

Kết quả trong <out>:
    srs_full.txt      toàn bộ văn bản, bảng dạng "cột | cột", ảnh dạng [IMG media/imageN.png]
    media/            ảnh design nhúng trong SRS (thường là ảnh chụp từ Figma)
    section_<mục>.txt nội dung riêng mục yêu cầu (khi có --section)
"""
import argparse
import os
import re
import sys
import zipfile

from lxml import etree

W = "{http://schemas.openxmlformats.org/wordprocessingml/2006/main}"
A = "{http://schemas.openxmlformats.org/drawingml/2006/main}"
R = "{http://schemas.openxmlformats.org/officeDocument/2006/relationships}"
HEADING = re.compile(r"^(\d+(?:\.\d+)+)\.?\s")
ROMAN = re.compile(r"^(I|II|III|IV|V|VI|VII|VIII|IX|X)\.\s")


def para_text(p) -> str:
    return "".join(t.text or "" for t in p.iter(W + "t")).strip()


def para_images(p, rels) -> list:
    return [rels.get(b.get(R + "embed")) for b in p.iter(A + "blip") if b.get(R + "embed") in rels]


def walk(el, rels, out):
    for ch in el:
        if ch.tag == W + "p":
            txt = para_text(ch)
            if txt:
                out.append(txt)
            for img in para_images(ch, rels):
                out.append(f"[IMG {img}]")
        elif ch.tag == W + "tbl":
            out.append("[TABLE]")
            for tr in ch.findall(W + "tr"):
                cells, imgs = [], []
                for tc in tr.findall(W + "tc"):
                    parts = []
                    for p in tc.iter(W + "p"):
                        s = para_text(p)
                        if s:
                            parts.append(s)
                        imgs.extend(para_images(p, rels))
                    cells.append(" / ".join(parts))
                out.append(" | ".join(cells))
                out.extend(f"[IMG {i}]" for i in imgs)
            out.append("[/TABLE]")
        else:
            walk(ch, rels, out)


def section_lines(lines, sec):
    depth = sec.count(".") + 1
    start = None
    for i, line in enumerate(lines):
        m = HEADING.match(line)
        if start is None:
            if m and m.group(1) == sec:
                start = i
            continue
        if ROMAN.match(line):
            return lines[start:i]
        if m and m.group(1).count(".") + 1 <= depth:
            return lines[start:i]
    return lines[start:] if start is not None else []


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("docx")
    ap.add_argument("--out", required=True)
    ap.add_argument("--section", help="Mã mục cần in riêng, VD: 1.3.4")
    args = ap.parse_args()
    os.makedirs(args.out, exist_ok=True)

    with zipfile.ZipFile(args.docx) as z:
        doc = etree.fromstring(z.read("word/document.xml"))
        rels_xml = etree.fromstring(z.read("word/_rels/document.xml.rels"))
        rels = {r.get("Id"): r.get("Target") for r in rels_xml}
        for name in z.namelist():
            if name.startswith("word/media/"):
                target = os.path.join(args.out, name[len("word/"):])
                os.makedirs(os.path.dirname(target), exist_ok=True)
                with open(target, "wb") as fh:
                    fh.write(z.read(name))

    lines = []
    walk(doc, rels, lines)
    full = os.path.join(args.out, "srs_full.txt")
    with open(full, "w", encoding="utf-8") as fh:
        fh.write("\n".join(lines))
    print(f"[OK] {full}: {len(lines)} dòng, ảnh lưu tại {os.path.join(args.out, 'media')}")

    headings = [l for l in lines if HEADING.match(l) and len(l) < 120]
    print("Mục lục phát hiện:")
    for h in headings:
        print("   ", h)

    if args.section:
        sec = section_lines(lines, args.section)
        if not sec:
            sys.exit(f"[LỖI] Không tìm thấy mục {args.section}")
        path = os.path.join(args.out, f"section_{args.section}.txt")
        with open(path, "w", encoding="utf-8") as fh:
            fh.write("\n".join(sec))
        imgs = [l for l in sec if l.startswith("[IMG ")]
        print(f"[OK] {path}: {len(sec)} dòng, {len(imgs)} ảnh design trong mục")
        refs = sorted(set(re.findall(r"(?:STT\s*\d+\s*)?mục\s*(\d+(?:\.\d+)+)", "\n".join(sec))))
        if refs:
            print("Mục được tham chiếu ('Tương tự STT x mục y') - PHẢI đọc thêm:", ", ".join(refs))


if __name__ == "__main__":
    main()
