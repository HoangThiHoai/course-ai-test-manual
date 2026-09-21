# -*- coding: utf-8 -*-
"""Tải tài liệu nguồn từ Google Docs / Google Sheets về máy (không cần đăng nhập).

Chỉ chạy được khi link được chia sẻ "Bất kỳ ai có đường liên kết". Nếu file bị
giới hạn quyền, Google trả về trang HTML đăng nhập -> script báo lỗi rõ ràng.

Cách dùng:
    python fetch_sources.py --srs  "<link Google Docs>"   --out <thư_mục>
    python fetch_sources.py --tc   "<link Google Sheets>" --out <thư_mục>
    python fetch_sources.py --srs "<...>" --tc "<...>" --out <thư_mục>

Kết quả: <out>/srs.docx, <out>/tcs.xlsx
"""
import argparse
import os
import re
import sys
import urllib.request

UA = {"User-Agent": "Mozilla/5.0"}


def file_id(url: str) -> str:
    m = re.search(r"/d/([A-Za-z0-9_-]{20,})", url)
    if not m:
        sys.exit(f"[LỖI] Không tách được file id từ link: {url}")
    return m.group(1)


def download(url: str) -> bytes:
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=180) as resp:
        return resp.read()


def save_zip(candidates, dest: str, label: str) -> None:
    """Thử lần lượt các URL, nhận kết quả đầu tiên là file Office (zip, bắt đầu bằng 'PK')."""
    for url in candidates:
        try:
            data = download(url)
        except Exception as exc:  # noqa: BLE001 - báo lại cho người dùng
            print(f"  - {url} -> lỗi mạng: {exc}")
            continue
        if data[:2] == b"PK":
            with open(dest, "wb") as fh:
                fh.write(data)
            print(f"[OK] {label}: {dest} ({len(data) / 1024 / 1024:.1f} MB)")
            return
        print(f"  - {url} -> không phải file Office (có thể là trang đăng nhập)")
    sys.exit(
        f"[LỖI] Không tải được {label}. Kiểm tra link đã chia sẻ 'Bất kỳ ai có đường liên kết' "
        "hoặc nhờ người dùng tải file về và đưa đường dẫn local."
    )


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--srs", help="Link Google Docs của tài liệu SRS")
    ap.add_argument("--tc", help="Link Google Sheets của file test case mẫu")
    ap.add_argument("--out", required=True, help="Thư mục lưu file")
    args = ap.parse_args()
    if not (args.srs or args.tc):
        ap.error("Cần ít nhất --srs hoặc --tc")
    os.makedirs(args.out, exist_ok=True)

    if args.srs:
        fid = file_id(args.srs)
        # File .docx upload lên Drive: dùng uc?export=download.
        # Google Docs gốc: dùng /export?format=docx.
        save_zip(
            [
                f"https://docs.google.com/uc?export=download&id={fid}",
                f"https://docs.google.com/document/d/{fid}/export?format=docx",
            ],
            os.path.join(args.out, "srs.docx"),
            "SRS",
        )
    if args.tc:
        fid = file_id(args.tc)
        save_zip(
            [
                f"https://docs.google.com/spreadsheets/d/{fid}/export?format=xlsx",
                f"https://docs.google.com/uc?export=download&id={fid}",
            ],
            os.path.join(args.out, "tcs.xlsx"),
            "File TC mẫu",
        )


if __name__ == "__main__":
    main()
