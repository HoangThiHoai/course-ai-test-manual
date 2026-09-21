# -*- coding: utf-8 -*-
"""File dữ liệu mẫu cho build_tc_excel.py — copy ra thành src/tcdata_<mục>.py rồi sửa.

ROWS:
  ('S', 'Tên section')                          -> dòng nhóm màn hình (nền màu, merge)
  ('P', 'Pre-condition: \\nBước 1: ...')         -> dòng điều kiện tiên quyết
  ('T', chức_năng | None, mục_đích, các_bước, kết_quả_mong_muốn, dữ_liệu, ghi_chú)
        chức_năng = None -> cùng nhóm với TC ngay phía trên (ô được merge dọc)
        TC đầu tiên sau mỗi section BẮT BUỘC có chức_năng

TECHNIQUES (tuỳ chọn) -> sheet "Kỹ thuật thiết kế TC":
  [{'title': ..., 'header': [...], 'rows': [[...], ...]}, ...]

Ví dụ thật đầy đủ: docs/testcases/qldh/mobile/src/tcdata_1.3.4.py
"""

ROWS = [
    ('S', 'Màn hình Chi tiết hoàn tiền'),
    ('P', 'Pre-condition: \nBước 1: Người dùng đăng nhập thành công vào hệ thống\n'
          'Bước 2: Người dùng click vào icon Đơn hàng trên navigation\n'
          'Bước 3: Click tab Trả hàng, chọn 1 đơn hàng có yêu cầu Trả hàng/Hoàn tiền'),

    ('T', 'Giao diện tổng quan', 'Kiểm tra giao diện tổng quan màn hình Chi tiết hoàn tiền',
     '1. Kiểm tra title của màn hình\n2. Kiểm tra hiển thị đầy đủ thông tin của các label trên màn hình',
     '1. Hiển thị title: Chi tiết hoàn tiền\n2. Hiển thị đầy đủ các label theo đúng design', '', ''),

    ('T', 'Button Huỷ yêu cầu', 'Check hiển thị button Huỷ yêu cầu khi yêu cầu đang chờ phê duyệt',
     'ĐK: Yêu cầu đang chờ xử lý\n1. Check button Huỷ yêu cầu',
     'Hiển thị button Huỷ yêu cầu', '', 'Mục 1.3.4 STT 4 - Kỹ thuật: Bảng quyết định'),
    ('T', None, 'Check ẩn button Huỷ yêu cầu sau khi ĐVVC đã lấy hàng',
     'ĐK: ĐVVC đã lấy hàng hoàn thành công\n1. Check button Huỷ yêu cầu',
     'Không hiển thị button Huỷ yêu cầu', '', 'Kỹ thuật: Bảng quyết định'),

    ('T', 'Mô tả', 'Check nhập quá 2.000 ký tự',
     '1. Nhập 2.001 ký tự vào trường Mô tả',
     'Hệ thống chặn nhập, chỉ ghi nhận 2.000 ký tự', 'Chuỗi 2001 ký tự',
     'Kỹ thuật: Phân tích giá trị biên'),
]

TECHNIQUES = [
    {
        'title': '1. BẢNG QUYẾT ĐỊNH - Hiển thị CTA theo trạng thái',
        'header': ['Thành phần / Trạng thái', 'Chờ phê duyệt', 'Đã lấy hàng'],
        'rows': [['Button Huỷ yêu cầu', 'Hiện', 'Ẩn']],
    },
    {
        'title': '2. PHÂN TÍCH GIÁ TRỊ BIÊN',
        'header': ['Ràng buộc', 'Dưới biên', 'Tại biên', 'Trên biên'],
        'rows': [['Mô tả tối đa 2.000 ký tự', '1.999', '2.000', '2.001 (bị chặn)']],
    },
]
