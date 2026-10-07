# -*- coding: utf-8 -*-
"""TC CMS - Quản lý đơn hàng (Tammi Gói cước - Đơn hàng, phase 1).

Nguồn:
- SRS "XÂY DỰNG MODULE GÓI CƯỚC- ĐƠN HÀNG" (Google Docs 1gebcMrC…, tab t.2l2tiqe3sf3r):
  tài liệu "Danh sách đơn hàng" (UC Xem danh sách, Bộ lọc, Cài đặt bảng, Tìm kiếm, Xem chi tiết, Xuất excel)
  + "Tổng hợp trạng thái" mục B (Đơn hàng) và C (Miniapp gói cước) + "Miniapp gói cước Tammi"
  (UC Tạo đơn hàng và thanh toán, sơ đồ PlantUML tạo đơn / kích hoạt).
- Figma CMS: [WEB] Tammi OA, page "CMS Gói cước", section T_Danh sách đơn hàng (node 42456-50485).
- Figma Miniapp: Super App File 01, page "Gói cước Tammi", section GÓI CƯỚC TAMMI (node 113087-6879).
Khuôn format: sheet "CMS-Quản lý gói cước" (cột A..G: ID, Chức năng, Mục đích, Các bước, Kết quả, Trạng thái, Ghi chú).

ROWS: ('S', ...) UC · ('G', ...) nhóm con · ('P', ...) Pre-condition · T(...) test case.
T(func, purpose, steps, expected, note, key): key = tên ngắn để sheet "Kỹ thuật thiết kế TC" tham chiếu ID thật qua {key}.
"""

BA = 'Cần BA confirm'
SRS = 'SRS Danh sách đơn hàng'

_RAW = []


def S(text):
    _RAW.append(('S', text))


def G(text):
    _RAW.append(('G', text))


def P(text):
    _RAW.append(('P', text))


def T(func, purpose, steps, expected, note='', key=None):
    _RAW.append(('T', func, purpose, steps, expected, '', note, key))


PRE = ('Pre-condition: \nBước 1: Admin đăng nhập thành công vào hệ thống CMS, tài khoản có quyền quản lý đơn hàng\n'
       'Bước 2: Click menu Quản lý đơn hàng > Danh sách đơn hàng')

# =====================================================================
S('UC1: (CMS admin) Chức năng Xem danh sách đơn hàng')
P(PRE)

G('Kiểm tra gui UI/UX')
T('Kiểm tra UI', 'Kiểm tra hiển thị giao diện mặc định',
  '1. Kiểm tra hiển thị màn hình Danh sách đơn hàng',
  '1. Hiển thị màn hình giống design gồm:\n'
  ' + Tiêu đề: Danh sách đơn hàng\n'
  ' + Ô tìm kiếm có icon kính lúp\n'
  ' + Button Xuất file excel, Button Cài đặt bảng, icon Bộ lọc\n'
  ' + Bảng danh sách đơn hàng, cột Thao tác cố định bên phải\n'
  ' + Vùng phân trang: dropdown số dòng/trang, text tổng số kết quả, các nút chuyển trang',
  'Figma T_Danh sách đơn hàng', 'ui_default')
T(None, 'Kiểm tra tổng thể giao diện màn hình',
  '1. Kiểm tra về bố cục, font chữ, chính tả, màu chữ',
  '1. \n - Các label, có độ dài, rộng và khoảng cách bằng nhau, không xô lệch\n'
  ' - Các label sử dụng cùng 1 loại font, cỡ chữ, căn lề\n'
  ' - Kiểm tra tất cả lỗi về chính tả, cấu trúc câu, ngữ pháp trên màn hình\n'
  ' - Form được bố trí hợp lý và dễ sử dụng')
T(None, 'Kiểm tra thứ tự di chuyển trỏ trên màn hình khi nhấn phím Tab',
  '1. Nhấn Tab liên tục',
  '1. Con trỏ di chuyển lần lượt theo thứ tự: Từ trái qua phải, từ trên xuống dưới')
T(None, 'Kiểm tra thứ tự con trỏ di chuyển ngược lại trên màn hình khi nhấn Shift-Tab',
  '1. Nhấn phím Shift-Tab liên tục',
  '1. Con trỏ di chuyển ngược lại theo thứ tự: từ dưới lên trên, từ phải qua trái')
T(None, 'Kiểm tra giao diện khi thu nhỏ, phóng to',
  '1. Trên màn hình chức năng\n2. Nhấn tổ hợp phím Ctrl -\n3. Nhấn tổ hợp phím Ctrl +',
  '3. Màn hình thu nhỏ, phóng to tương ứng và không bị vỡ giao diện')
T(None, 'Kiểm tra hiển thị menu đang chọn trên sidebar',
  '1. Kiểm tra menu Danh sách đơn hàng trên sidebar',
  '1. Menu con Danh sách đơn hàng được highlight (đang chọn), nhóm menu Quản lý đơn hàng ở trạng thái mở rộng',
  'Figma')

G('Kiểm tra phân quyền & truy cập')
T('Phân quyền', 'Kiểm tra truy cập bằng tài khoản có quyền quản lý đơn hàng',
  '1. Đăng nhập CMS bằng tài khoản có quyền quản lý đơn hàng\n2. Click menu Quản lý đơn hàng > Danh sách đơn hàng',
  '2. Truy cập thành công, hiển thị màn Danh sách đơn hàng',
  f'{SRS} - UC Xem DS - Pre-condition', 'perm_ok')
T(None, 'Kiểm tra truy cập bằng tài khoản không có quyền quản lý đơn hàng',
  '1. Đăng nhập CMS bằng tài khoản KHÔNG có quyền quản lý đơn hàng\n2. Truy cập màn Danh sách đơn hàng (click menu hoặc nhập URL trực tiếp)',
  '2. Không hiển thị dữ liệu danh sách, hiển thị toast: "Bạn ko có quyền truy cập tính năng nay. Vui lòng liên hệ quản trị viên"',
  f'{SRS} - UC Xem DS - Luồng ngoại lệ. {BA}: (1) câu toast trong SRS có lỗi chính tả "ko", "nay" - chốt câu chuẩn; '
  '(2) tài khoản không có quyền thì menu bị ẩn hay vẫn hiện', 'perm_no')
T(None, 'Kiểm tra truy cập URL chi tiết đơn hàng bằng tài khoản không có quyền',
  '1. Đăng nhập CMS bằng tài khoản không có quyền quản lý đơn hàng\n2. Dán URL màn Chi tiết đơn hàng của 1 đơn hàng có thật',
  '2. Không hiển thị thông tin đơn hàng, hiển thị toast không có quyền như TC trên',
  f'NFR 3.1 RBAC - {BA}: SRS UC Xem chi tiết chưa mô tả ngoại lệ không có quyền', 'perm_detail')
T(None, 'Kiểm tra khi quyền quản lý đơn hàng bị thu hồi trong lúc đang ở màn danh sách',
  'ĐK: Admin A đang mở màn Danh sách đơn hàng\n1. Quản trị hệ thống thu hồi quyền quản lý đơn hàng của Admin A\n2. Admin A F5 tải lại trang',
  '2. Hiển thị toast không có quyền truy cập, không còn hiển thị dữ liệu đơn hàng',
  f'{BA} cơ chế cập nhật quyền (ngay lập tức hay sau khi đăng nhập lại)')

G('Vùng danh sách - Hiển thị chung')
T('Danh sách chưa có dữ liệu', 'Kiểm tra hiển thị khi hệ thống chưa có đơn hàng nào',
  'ĐK: Hệ thống chưa có đơn hàng nào (hoặc tất cả đã bị xoá mềm)\n1. Truy cập màn Danh sách đơn hàng',
  '1. Bảng chỉ hiển thị header các cột, vùng dữ liệu hiển thị icon hộp quà + text "Danh sách trống"',
  f'{SRS} - UC Xem DS - Ngoại lệ "Ko có bản ghi nào" + Figma Empty cases', 'list_empty')
T('Danh sách đã có dữ liệu', 'Kiểm tra hiển thị danh sách khi đã có đơn hàng',
  'ĐK: Hệ thống có đơn hàng\n1. Truy cập màn Danh sách đơn hàng\n2. Kiểm tra vùng danh sách',
  '2. Hiển thị bảng danh sách đơn hàng dạng phân trang, mỗi dòng là 1 đơn hàng (đơn cha), hiển thị đủ các cột theo SRS',
  f'{SRS} - UC Xem DS - Luồng chính', 'list_has')
T(None, 'Kiểm tra danh sách không hiển thị đơn hàng đã bị xoá mềm',
  'ĐK: Có đơn hàng A bình thường và đơn hàng B đã bị xoá mềm trong DB\n1. Truy cập màn Danh sách đơn hàng\n2. Tìm kiếm mã đơn hàng B',
  '1. Không hiển thị đơn hàng B trong danh sách\n2. Tìm kiếm mã B → "Không tìm thấy kết quả"',
  f'{SRS} - UC Xem DS - BR "Chỉ lấy các bản ghi chưa được xoá mềm" - Check database (cần quyền truy vấn DB)', 'list_softdel')
T(None, 'Kiểm tra thứ tự sắp xếp mặc định của danh sách',
  'ĐK: Có ≥ 3 đơn hàng tạo ở các thời điểm khác nhau\n1. Truy cập màn Danh sách đơn hàng\n2. Kiểm tra cột Thời gian tạo theo thứ tự từ trên xuống',
  '2. Danh sách sắp xếp theo Thời gian tạo từ gần tới xa (đơn mới nhất ở dòng đầu)',
  f'{SRS} - UC Xem DS - BR1', 'list_sort_default')
T(None, 'Kiểm tra đơn hàng mới tạo từ Miniapp hiển thị ở đầu danh sách',
  'ĐK: Đang mở màn Danh sách đơn hàng\n1. Trên Miniapp gói cước Tammi, thực hiện mua 1 gói cước (tạo đơn thành công)\n2. Quay lại CMS, F5 tải lại màn danh sách',
  '2. Đơn hàng vừa tạo hiển thị ở dòng đầu tiên, Trạng thái thanh toán = Chờ thanh toán (hoặc trạng thái tương ứng kết quả thanh toán), Kênh bán = Miniapp gói cước Tammi',
  f'{SRS} - BR1 + Luồng tạo đơn miniapp. {BA}: danh sách có tự cập nhật realtime hay phải tải lại', 'list_new')
T(None, 'Kiểm tra text tổng số kết quả',
  'ĐK: Hệ thống có 112 đơn hàng\n1. Kiểm tra text phía dưới bảng',
  '1. Hiển thị "Hiển thị 1-10 trong tổng số 112 kết quả" (số đầu-cuối theo trang và số dòng/trang đang chọn)',
  f'Figma - SRS chưa mô tả text này. {BA} số dòng/trang mặc định (xem nhóm Phân trang)')
T(None, 'Kiểm tra cuộn ngang bảng khi có nhiều cột',
  '1. Cuộn ngang bảng danh sách sang phải đến cột cuối cùng',
  '1. \n - Bảng cuộn ngang được, các cột hiển thị đầy đủ không chồng lấn\n - Cột Thao tác luôn cố định bên phải, không bị cuộn theo',
  'Figma: bảng 23 cột, cột Thao tác cố định', 'list_scroll')
T(None, 'Kiểm tra màu badge trạng thái phân biệt theo giá trị',
  'ĐK: Có đơn hàng ở đủ các trạng thái\n1. Kiểm tra badge cột Trạng thái thanh toán và Trạng thái đơn hàng',
  '1. Badge hiển thị đúng màu theo design:\n - Chờ thanh toán: hồng\n - Thất bại: xám\n - Thành công: xanh lá\n - Đã huỷ: đỏ\n'
  ' - Chờ cung cấp dịch vụ: xanh dương\n - Hoàn thành: xanh lá\n - Chờ xử lý hoàn tiền: theo design',
  f'Figma. {BA}: design chưa có mẫu màu badge "Chờ xử lý hoàn tiền"')

G('Vùng danh sách - Từng cột thông tin')
T('Cột STT', 'Kiểm tra hiển thị cột STT',
  'ĐK: Danh sách có nhiều trang\n1. Kiểm tra cột STT tại trang 1\n2. Chuyển sang trang 2',
  '1. STT tự tăng bắt đầu từ 1\n2. STT của trang 2 bắt đầu lại từ 1',
  f'{SRS} - Mô tả giao diện STT 1 "theo từng trang phân trang (bắt đầu từ 1)". {BA}: trang 2 đánh lại từ 1 hay nối tiếp (11, 12…)', 'col_stt')
T('Cột ID', 'Kiểm tra hiển thị cột ID',
  '1. Kiểm tra cột ID của 1 đơn hàng\n2. Đối chiếu với ID đơn hàng trong DB',
  '2. Hiển thị đúng ID định danh nội bộ của đơn hàng',
  f'{SRS} - STT 2 - Check database')
T('Cột Trạng thái thanh toán', 'Kiểm tra giá trị cột Trạng thái thanh toán',
  'ĐK: Có đơn hàng ở các trạng thái thanh toán khác nhau\n1. Kiểm tra cột Trạng thái thanh toán',
  '1. Chỉ hiển thị 1 trong các giá trị: Chờ thanh toán, Thất bại, Thành công; đúng với trạng thái thanh toán của đơn',
  f'{SRS} - STT 3 + Tổng hợp trạng thái B. {BA}: khi hoàn tiền thành công, trạng thái thanh toán = "Đã hoàn tiền" (giá trị thứ 4?) có hiển thị không', 'col_tttt')
T('Cột Trạng thái đơn hàng', 'Kiểm tra giá trị cột Trạng thái đơn hàng',
  'ĐK: Có đơn hàng ở các trạng thái khác nhau\n1. Kiểm tra cột Trạng thái đơn hàng',
  '1. Chỉ hiển thị 1 trong các giá trị: Chờ thanh toán, Đã hủy, Chờ cung cấp dịch vụ, Chờ xử lý hoàn tiền, Hoàn thành; đúng trạng thái tổng thể của đơn',
  f'{SRS} - STT 4', 'col_ttdh')
T('Cột Mã đơn hàng', 'Kiểm tra hiển thị cột Mã đơn hàng',
  '1. Kiểm tra cột Mã đơn hàng',
  '1. Hiển thị mã đơn hàng do hệ thống order tự sinh, định dạng màu đỏ dạng link (VD: ORD2026080200222)',
  f'{SRS} - STT 5. {BA}: (1) design chỉ dòng đầu có mã màu đỏ, các dòng khác màu đen; '
  '(2) định dạng mã: SRS UC Tìm kiếm ví dụ "ORD2026080200222", UC Chi tiết ví dụ "8867544479346"', 'col_madh')
T(None, 'Kiểm tra click Mã đơn hàng',
  '1. Click vào Mã đơn hàng của 1 dòng',
  '1. Điều hướng sang màn Chi tiết đơn hàng của đúng đơn hàng đã chọn',
  f'{SRS} - STT 5 + Trigger UC Xem chi tiết', 'col_madh_click')
T('Cột Mã đơn hàng CTT Tammi', 'Kiểm tra hiển thị cột Mã đơn hàng CTT Tammi khi đơn đã có mã giao dịch CTT',
  'ĐK: Đơn hàng đã được CTT trả miniapprequestid\n1. Kiểm tra cột Mã đơn hàng CTT Tammi',
  '1. Hiển thị đúng mã giao dịch đối soát nhận về từ CTT Tammi (miniapprequestid)',
  f'{SRS} - STT 6 - Phân vùng tương đương (có/không có mã)', 'col_ctt_has')
T(None, 'Kiểm tra hiển thị cột Mã đơn hàng CTT Tammi khi đơn chưa có mã giao dịch CTT',
  'ĐK: Đơn hàng vừa tạo, chưa nhận mã từ CTT\n1. Kiểm tra cột Mã đơn hàng CTT Tammi',
  '1. Ô để trống / hiển thị "-" theo design',
  f'{SRS} - STT 6 (Bắt buộc = Không). {BA} cách hiển thị khi rỗng', 'col_ctt_empty')
T('Cột Loại dịch vụ', 'Kiểm tra hiển thị cột Loại dịch vụ',
  '1. Kiểm tra cột Loại dịch vụ của đơn mua gói cước',
  '1. Hiển thị "Gói cước"', f'{SRS} - STT 7')
T('Cột Thuê bao đăng kí dịch vụ', 'Kiểm tra hiển thị cột Thuê bao đăng kí dịch vụ',
  '1. Kiểm tra cột Thuê bao đăng kí dịch vụ\n2. Đối chiếu với SĐT tài khoản Tammi đã mua gói trên Miniapp',
  '2. Hiển thị đúng SĐT của tài khoản thực hiện tạo đơn/mua hàng', f'{SRS} - STT 8')
T('Cột Loại thuê bao đăng kí dịch vụ', 'Kiểm tra hiển thị cột Loại thuê bao đăng kí dịch vụ',
  '1. Kiểm tra cột Loại thuê bao đăng kí dịch vụ của đơn tạo từ Miniapp',
  '1. Hiển thị "Tk Tammi"', f'{SRS} - STT 9')
T('Cột Thuê bao thụ hưởng dịch vụ', 'Kiểm tra hiển thị cột Thuê bao thụ hưởng dịch vụ khi loại thuê bao thụ hưởng = Tk Tammi',
  'ĐK: Đơn hàng có loại thuê bao thụ hưởng = Tk Tammi\n1. Kiểm tra cột Thuê bao thụ hưởng dịch vụ',
  '1. Hiển thị SĐT của tài khoản nhận quyền lợi', f'{SRS} - STT 10 - Phân vùng tương đương theo loại thuê bao', 'col_tb_tammi')
T(None, 'Kiểm tra hiển thị cột Thuê bao thụ hưởng dịch vụ khi loại thuê bao thụ hưởng = Tk OA',
  'ĐK: Đơn hàng có loại thuê bao thụ hưởng = Tk OA\n1. Kiểm tra cột Thuê bao thụ hưởng dịch vụ',
  '1. Hiển thị định danh thuê bao thụ hưởng theo SRS (SĐT)',
  f'{SRS} - STT 10. {BA}: Tk OA thì hiển thị SĐT hay OA ID (màn Gói cước đã đăng ký hiển thị OA ID)', 'col_tb_oa')
T('Cột Loại thuê bao thụ hưởng dịch vụ', 'Kiểm tra hiển thị cột Loại thuê bao thụ hưởng dịch vụ',
  'ĐK: Có đơn hàng thụ hưởng Tk Tammi và đơn thụ hưởng Tk OA\n1. Kiểm tra cột Loại thuê bao thụ hưởng dịch vụ',
  '1. Hiển thị đúng 1 trong 2 giá trị: Tk Tammi, Tk OA', f'{SRS} - STT 11')
T('Cột Tổng giá gốc', 'Kiểm tra hiển thị cột Tổng giá gốc',
  '1. Kiểm tra cột Tổng giá gốc của đơn hàng',
  '1. Hiển thị tổng giá trị ban đầu trước khi áp dụng chiết khấu, định dạng VND có dấu chấm phân cách hàng nghìn + "đ" (VD: 100.000đ)',
  f'{SRS} - STT 12', 'col_giagoc')
T('Cột Tổng chiết khấu dịch vụ', 'Kiểm tra hiển thị cột Tổng chiết khấu dịch vụ khi đơn có áp dụng CTKM',
  'ĐK: Đơn hàng mua gói có CTKM giảm 20.000đ\n1. Kiểm tra cột Tổng chiết khấu dịch vụ',
  '1. Hiển thị 20.000đ', f'{SRS} - STT 13 - Phân vùng tương đương (có/không CTKM)', 'col_ck_has')
T(None, 'Kiểm tra hiển thị cột Tổng chiết khấu dịch vụ khi đơn không áp dụng CTKM',
  'ĐK: Đơn hàng mua gói không có CTKM\n1. Kiểm tra cột Tổng chiết khấu dịch vụ',
  '1. Hiển thị 0đ', f'{SRS} - STT 13 "Ko có hiển thị= 0đ"', 'col_ck_none')
T('Cột Tổng tiền sau chiết khấu dịch vụ', 'Kiểm tra công thức Tổng tiền sau chiết khấu dịch vụ',
  'ĐK: Đơn hàng Tổng giá gốc 100.000đ, Tổng chiết khấu 20.000đ\n1. Kiểm tra cột Tổng tiền sau chiết khấu dịch vụ',
  '1. Hiển thị 80.000đ (= Tổng giá gốc - Tổng chiết khấu dịch vụ)', f'{SRS} - STT 14', 'col_sauck')
T(None, 'Kiểm tra Tổng tiền sau chiết khấu khi CTKM giảm theo %',
  'ĐK: Gói giá gốc 199.000đ, CTKM giảm 15%\n1. Mua gói trên Miniapp\n2. Kiểm tra Tổng chiết khấu và Tổng tiền sau chiết khấu trên CMS',
  '2. Tổng chiết khấu = 29.850đ, Tổng tiền sau chiết khấu = 169.150đ; số tiền làm tròn theo quy tắc hệ thống, khớp số tiền hiển thị trên Miniapp',
  f'Kỹ thuật: Giá trị biên làm tròn. {BA} quy tắc làm tròn tiền chiết khấu %', 'col_sauck_pct')
T('Cột Tổng tiền thanh toán', 'Kiểm tra Tổng tiền thanh toán khi khách dùng voucher của CTT',
  'ĐK: Gói 80.000đ sau CTKM dịch vụ; trên màn Thanh toán của CTT khách áp voucher Viettel giảm 1.000đ\n1. Thanh toán thành công\n2. Kiểm tra cột Tổng tiền thanh toán và Tổng tiền sau chiết khấu dịch vụ',
  '2. \n - Tổng tiền thanh toán = 79.000đ (số tiền CTT trả về cho kênh bán)\n - Tổng tiền sau chiết khấu dịch vụ vẫn = 80.000đ',
  f'{SRS} - STT 15 + Figma Miniapp màn Thanh toán (Voucher Viettel). Kỹ thuật: Phân vùng tương đương', 'col_tt_voucher')
T(None, 'Kiểm tra Tổng tiền thanh toán khi khách không dùng voucher CTT',
  'ĐK: Gói 80.000đ sau CTKM dịch vụ, không áp voucher CTT\n1. Thanh toán thành công\n2. Kiểm tra cột Tổng tiền thanh toán',
  '2. Tổng tiền thanh toán = 80.000đ = Tổng tiền sau chiết khấu dịch vụ', f'{SRS} - STT 15')
T(None, 'Kiểm tra Tổng tiền thanh toán khi đơn chưa thanh toán / thanh toán thất bại',
  'ĐK: Có đơn Trạng thái thanh toán = Chờ thanh toán và đơn = Thất bại\n1. Kiểm tra cột Tổng tiền thanh toán',
  '1. Hiển thị theo quy định của BA (để trống / 0đ / bằng Tổng tiền sau chiết khấu)',
  f'{BA}: SRS chỉ nói "do CTT trả" - chưa có giá trị khi CTT chưa trả kết quả', 'col_tt_unpaid')
T('Cột Phương thức thanh toán', 'Kiểm tra hiển thị cột Phương thức thanh toán',
  'ĐK: Đơn thanh toán thành công qua Viettel Money\n1. Kiểm tra cột Phương thức thanh toán',
  '1. Hiển thị "Viettel Money"',
  f'{SRS} - STT 16 (Bắt buộc = Có). {BA}: đơn Chờ thanh toán / Thất bại chưa có PTTT thì hiển thị gì')
T('Cột Kênh bán', 'Kiểm tra hiển thị cột Kênh bán',
  'ĐK: Có đơn tạo từ Miniapp gói cước Tammi\n1. Kiểm tra cột Kênh bán',
  '1. Hiển thị "Miniapp gói cước Tammi"', f'{SRS} - STT 17')
T('Cột Kết quả cung cấp dịch vụ', 'Kiểm tra cột Kết quả cung cấp dịch vụ khi tất cả quyền lợi kích hoạt thành công',
  'ĐK: Đơn đã thanh toán thành công, tất cả quyền lợi của gói kích hoạt thành công\n1. Kiểm tra cột Kết quả cung cấp dịch vụ',
  '1. Hiển thị "Cung cấp dịch vụ thành công"',
  f'{SRS} - STT 18 + sơ đồ Luồng kích hoạt tổng thể - Bảng quyết định. {BA}: Figma chi tiết ghi "Hoàn thành cung cấp dịch vụ"', 'ccdv_ok')
T(None, 'Kiểm tra cột Kết quả cung cấp dịch vụ khi 1 phần quyền lợi kích hoạt thất bại',
  'ĐK: Gói có 3 quyền lợi, 1 quyền lợi kích hoạt thất bại sau khi retry hết 3 lần\n1. Kiểm tra cột Kết quả cung cấp dịch vụ',
  '1. Hiển thị "Cung cấp dịch vụ 1 phần"', f'{SRS} - STT 18 - Bảng quyết định', 'ccdv_part')
T(None, 'Kiểm tra cột Kết quả cung cấp dịch vụ khi tất cả quyền lợi kích hoạt thất bại',
  'ĐK: Tất cả quyền lợi của gói kích hoạt thất bại\n1. Kiểm tra cột Kết quả cung cấp dịch vụ',
  '1. Hiển thị "Cung cấp dịch vụ thất bại"', f'{SRS} - STT 18 - Bảng quyết định', 'ccdv_fail')
T(None, 'Kiểm tra cột Kết quả cung cấp dịch vụ khi đơn chưa tới bước cung cấp dịch vụ',
  'ĐK: Có đơn Chờ thanh toán, đơn Đã hủy, đơn Chờ cung cấp dịch vụ\n1. Kiểm tra cột Kết quả cung cấp dịch vụ',
  '1. Hiển thị theo quy định của BA (để trống / "-")',
  f'{BA}: SRS đặt Bắt buộc = Có nhưng chưa có giá trị trước khi CCDV; design mẫu lại để "thành công" cho cả đơn Chờ thanh toán', 'ccdv_none')
T('Cột Thời gian tạo', 'Kiểm tra định dạng cột Thời gian tạo',
  '1. Kiểm tra cột Thời gian tạo\n2. Đối chiếu với thời điểm tạo đơn trên Miniapp',
  '1. Hiển thị định dạng DD/MM/YYYY HH:MM:SS\n2. Đúng mốc thời gian hệ thống khởi tạo đơn hàng',
  f'{SRS} - STT 19. Mâu thuẫn SRS (DD/MM/YYYY HH:MM:SS) và design danh sách (2026-08-08 17:43:52) - {BA}', 'col_time')
T('Cột Thời gian cập nhật', 'Kiểm tra cột Thời gian cập nhật thay đổi khi trạng thái đơn thay đổi',
  'ĐK: Đơn đang Chờ thanh toán\n1. Ghi nhận Thời gian cập nhật\n2. Hoàn tất thanh toán thành công trên Miniapp\n3. Tải lại danh sách',
  '3. Thời gian cập nhật đổi thành thời điểm đơn chuyển trạng thái, định dạng giống Thời gian tạo',
  f'{SRS} - STT 20')
T('Cột Người cập nhật', 'Kiểm tra cột Người cập nhật khi đơn chỉ do hệ thống cập nhật',
  'ĐK: Đơn chỉ được cập nhật bởi luồng tự động (thanh toán, kích hoạt)\n1. Kiểm tra cột Người cập nhật',
  '1. Hiển thị "System"',
  f'{SRS} - STT 21 (Bắt buộc = Không) - ví dụ "System" lấy từ UC Chi tiết. {BA}: phase 1 CMS không có thao tác sửa đơn → cột luôn là System?')
T('Cột Thao tác', 'Kiểm tra hiển thị cột Thao tác',
  '1. Kiểm tra cột Thao tác',
  '1. Mỗi dòng hiển thị icon (i) xem chi tiết, cột cố định bên phải bảng',
  f'Figma. {BA}: SRS không mô tả cột Thao tác (chỉ có click Mã đơn hàng)', 'col_action')
T(None, 'Kiểm tra click icon (i) tại cột Thao tác',
  '1. Click icon (i) của 1 dòng',
  '1. Điều hướng sang màn Chi tiết đơn hàng của đúng đơn hàng đó', f'Figma - {BA}')
T('Hiển thị text dài', 'Kiểm tra hiển thị khi dữ liệu cột dài',
  'ĐK: Đơn có Mã đơn hàng CTT 50 ký tự\n1. Kiểm tra cột Mã đơn hàng CTT Tammi',
  '1. Text hiển thị đầy đủ / xuống dòng / cắt "..." có tooltip theo design, không vỡ layout bảng',
  f'{BA} quy tắc hiển thị text dài')

G('Sắp xếp')
T('Sắp xếp theo cột', 'Kiểm tra hiển thị icon sắp xếp trên header các cột',
  '1. Kiểm tra header các cột của bảng',
  '1. Các cột có icon sắp xếp (mũi tên lên/xuống) theo design; cột Tổng giá gốc và cột Thao tác không có icon sắp xếp',
  f'Figma. {BA}: SRS không mô tả chức năng sắp xếp theo cột', 'sort_icon')
T(None, 'Kiểm tra sắp xếp tăng dần theo cột Thời gian tạo',
  '1. Click icon sắp xếp cột Thời gian tạo 1 lần',
  '1. Danh sách sắp xếp Thời gian tạo từ xa đến gần, icon hiển thị trạng thái tăng dần', f'Figma - {BA}', 'sort_asc')
T(None, 'Kiểm tra sắp xếp giảm dần theo cột Thời gian tạo',
  '1. Click icon sắp xếp cột Thời gian tạo 2 lần',
  '1. Danh sách sắp xếp Thời gian tạo từ gần đến xa', f'Figma - {BA}', 'sort_desc')
T(None, 'Kiểm tra sắp xếp theo cột dạng tiền tệ',
  '1. Click icon sắp xếp cột Tổng tiền thanh toán',
  '1. Danh sách sắp xếp theo giá trị số (100.000đ đứng sau 99.000đ khi tăng dần), không sắp xếp theo chuỗi ký tự',
  f'Figma - {BA}')
T(None, 'Kiểm tra sắp xếp theo cột trạng thái',
  '1. Click icon sắp xếp cột Trạng thái đơn hàng',
  '1. Danh sách sắp xếp theo quy tắc BA quy định (theo tên A-Z hoặc theo thứ tự vòng đời)', f'{BA} quy tắc sort cột trạng thái')
T(None, 'Kiểm tra sắp xếp giữ nguyên khi chuyển trang',
  'ĐK: Đang sắp xếp Tổng tiền thanh toán tăng dần\n1. Chuyển sang trang 2',
  '1. Trang 2 tiếp tục thứ tự tăng dần nối tiếp trang 1 (sắp xếp trên toàn bộ dữ liệu, không chỉ trong trang)', f'{BA}')

G('Phân trang')
T('Phân trang', 'Kiểm tra số dòng/trang mặc định',
  'ĐK: Có > 30 đơn hàng\n1. Truy cập màn Danh sách đơn hàng\n2. Kiểm tra dropdown số dòng/trang và số dòng hiển thị',
  '2. Mặc định hiển thị 25 dòng/trang',
  f'{SRS} - UC Xem DS - Luồng chính "mặc định số dòng trên trang= 25". Mâu thuẫn design hiển thị "10 dòng" - {BA}', 'page_default')
T(None, 'Kiểm tra danh sách giá trị dropdown số dòng/trang',
  '1. Click dropdown số dòng/trang',
  '1. Hiển thị danh sách lựa chọn số dòng/trang theo design',
  f'{BA}: SRS và design chưa liệt kê các giá trị (VD 10/25/50/100)', 'page_options')
T(None, 'Kiểm tra đổi số dòng/trang',
  'ĐK: Có 112 đơn hàng\n1. Chọn số dòng/trang khác giá trị mặc định (VD 50)',
  '1. \n - Bảng hiển thị đúng 50 dòng\n - Quay về trang 1\n - Text tổng: "Hiển thị 1-50 trong tổng số 112 kết quả", số trang cập nhật lại = 3')
T(None, 'Kiểm tra số trang khi số bản ghi bằng đúng số dòng/trang',
  'ĐK: Có đúng 25 đơn hàng, 25 dòng/trang\n1. Kiểm tra vùng phân trang',
  '1. Chỉ có 1 trang, nút trang sau bị disable', 'Kỹ thuật: Giá trị biên (= số dòng/trang)', 'page_eq')
T(None, 'Kiểm tra số trang khi số bản ghi lớn hơn số dòng/trang 1 bản ghi',
  'ĐK: Có 26 đơn hàng, 25 dòng/trang\n1. Kiểm tra vùng phân trang\n2. Click trang 2',
  '1. Có 2 trang\n2. Trang 2 hiển thị 1 đơn hàng, text "Hiển thị 26-26 trong tổng số 26 kết quả"',
  'Kỹ thuật: Giá trị biên (số dòng/trang + 1)', 'page_over')
T(None, 'Kiểm tra chuyển trang bằng nút số trang / mũi tên',
  'ĐK: Có ≥ 3 trang\n1. Click số trang 2\n2. Click mũi tên →\n3. Click mũi tên ←',
  '1. Hiển thị dữ liệu trang 2, số trang 2 được highlight\n2. Chuyển sang trang 3\n3. Quay về trang 2')
T(None, 'Kiểm tra trạng thái nút mũi tên ở trang đầu / trang cuối',
  '1. Ở trang 1 kiểm tra mũi tên ←\n2. Chuyển tới trang cuối, kiểm tra mũi tên →',
  '1. Mũi tên ← disable\n2. Mũi tên → disable')
T(None, 'Kiểm tra hiển thị dấu "..." khi có nhiều trang',
  'ĐK: Có 15 trang\n1. Kiểm tra dãy số trang',
  '1. Hiển thị 1 2 3 ... 15 theo design, click 15 chuyển tới trang cuối', 'Figma')
T(None, 'Kiểm tra phân trang giữ điều kiện tìm kiếm/lọc',
  'ĐK: Tìm kiếm/lọc ra 30 kết quả\n1. Chuyển sang trang 2\n2. Quay lại trang 1',
  '1, 2. Dữ liệu các trang chỉ gồm kết quả thoả điều kiện tìm kiếm/lọc, từ khoá & điều kiện lọc được giữ nguyên')

G('Xử lý ngoại lệ')
T('Lỗi hệ thống', 'Kiểm tra khi hệ thống không truy vấn được CSDL / quá tải',
  'ĐK: Giả lập API danh sách đơn hàng trả lỗi 500/timeout\n1. Truy cập màn Danh sách đơn hàng',
  '1. Hiển thị thông báo lỗi: "Hệ thống bận, vui lòng thử lại sau"',
  f'{SRS} - UC Xem DS - Ngoại lệ "Lỗi kết nối / Quá tải" - cần mock API hoặc dev hỗ trợ', 'err_500')
T('Mất mạng', 'Kiểm tra khi mất mạng lúc tải danh sách',
  '1. Ngắt kết nối mạng\n2. F5 / chuyển trang danh sách',
  '2. Hiển thị thông báo: "Lỗi đường truyền. Vui lòng kiểm tra kết nối của bạn"',
  f'{SRS} - UC Xem DS - Ngoại lệ "Mất mạng"', 'err_net')
T(None, 'Kiểm tra tải lại dữ liệu khi có mạng trở lại',
  'ĐK: Đang hiển thị thông báo lỗi đường truyền\n1. Bật lại mạng\n2. Chuyển trang / F5',
  '2. Danh sách tải lại bình thường, không hiển thị thông báo lỗi')

# =====================================================================
S('UC2: (CMS admin) Chức năng Tìm kiếm đơn hàng')
P(PRE)

G('Kiểm tra gui UI/UX')
T('Ô tìm kiếm', 'Kiểm tra hiển thị mặc định ô tìm kiếm',
  '1. Kiểm tra ô tìm kiếm',
  '1. Mặc định trống, có icon kính lúp, hiển thị placeholder: "Tìm kiếm theo mã đơn hàng"',
  f'Figma. {BA}: SRS cho tìm theo ID và Mã đơn hàng nhưng placeholder design chỉ ghi "mã đơn hàng"', 'search_ph')

G('Kiểm tra chức năng')
T('Tìm kiếm theo Mã đơn hàng', 'Kiểm tra tìm kiếm chính xác theo Mã đơn hàng',
  'ĐK: Có đơn hàng mã ORD2026080200222\n1. Nhập "ORD2026080200222" vào ô tìm kiếm\n2. Dừng gõ',
  '2. Hiển thị đúng đơn hàng có Mã đơn hàng ORD2026080200222',
  f'{SRS} - UC Tìm kiếm - Luồng chính, BR1 - Phân vùng tương đương', 'srch_madh')
T(None, 'Kiểm tra tìm kiếm gần đúng theo 1 phần Mã đơn hàng',
  '1. Nhập "20260802" vào ô tìm kiếm',
  '1. Hiển thị các đơn hàng có Mã đơn hàng chứa "20260802"',
  f'{BA}: SRS mục đích "tìm kiếm chính xác" nhưng không nói rõ có tìm gần đúng hay không', 'srch_partial')
T('Tìm kiếm theo ID', 'Kiểm tra tìm kiếm theo ID đơn hàng',
  'ĐK: Có đơn hàng ID 12234\n1. Nhập "12234" vào ô tìm kiếm',
  '1. Hiển thị đơn hàng có ID 12234', f'{SRS} - UC Tìm kiếm - BR1 "Tìm kiếm theo ID, mã đơn hàng"', 'srch_id')
T('Không phân biệt hoa thường', 'Kiểm tra tìm kiếm không phân biệt chữ hoa, chữ thường',
  '1. Nhập "ord2026080200222" vào ô tìm kiếm',
  '1. Hiển thị đơn hàng ORD2026080200222', f'{SRS} - BR1', 'srch_case')
T(None, 'Kiểm tra tìm kiếm không phân biệt chữ có dấu/không dấu',
  '1. Nhập từ khoá có dấu tương ứng mã đơn hàng (VD "ÒRD2026080200222")',
  '1. Hệ thống bỏ dấu khi so khớp, hiển thị đơn hàng ORD2026080200222', f'{SRS} - BR1')
T('Số ký tự bắt đầu tìm kiếm', 'Kiểm tra nhập 1 ký tự',
  '1. Nhập "O" vào ô tìm kiếm\n2. Dừng gõ',
  '2. Hệ thống chưa thực hiện tìm kiếm, danh sách giữ nguyên',
  f'{SRS} - BR1 "Tìm kiếm bắt đầu từ ký tự thứ 3" - Kỹ thuật: Giá trị biên', 'srch_1')
T(None, 'Kiểm tra nhập 2 ký tự',
  '1. Nhập "OR" vào ô tìm kiếm\n2. Dừng gõ',
  '2. Hệ thống chưa thực hiện tìm kiếm, danh sách giữ nguyên', 'Kỹ thuật: Giá trị biên (3-1)', 'srch_2')
T(None, 'Kiểm tra nhập 3 ký tự',
  '1. Nhập "ORD" vào ô tìm kiếm\n2. Dừng gõ',
  '2. Hệ thống thực hiện tìm kiếm, hiển thị các đơn hàng khớp "ORD"', 'Kỹ thuật: Giá trị biên (=3)', 'srch_3')
T(None, 'Kiểm tra tìm kiếm ID có ít hơn 3 chữ số',
  'ĐK: Có đơn hàng ID = 12\n1. Nhập "12" vào ô tìm kiếm',
  '1. Hệ thống không tìm kiếm (do < 3 ký tự) → không tìm được đơn ID 12',
  f'{BA}: rule "từ ký tự thứ 3" khiến không tìm được ID 1-2 chữ số - có chấp nhận không', 'srch_id_short')
T('Độ dài tối đa', 'Kiểm tra nhập 49 ký tự',
  '1. Nhập chuỗi 49 ký tự vào ô tìm kiếm',
  '1. Cho phép nhập đủ 49 ký tự', f'{SRS} - BR1 "Chặn nhập quá 50 ký tự" - Kỹ thuật: Giá trị biên', 'srch_49')
T(None, 'Kiểm tra nhập 50 ký tự',
  '1. Nhập chuỗi 50 ký tự vào ô tìm kiếm',
  '1. Cho phép nhập đủ 50 ký tự, thực hiện tìm kiếm', 'Kỹ thuật: Giá trị biên', 'srch_50')
T(None, 'Kiểm tra nhập 51 ký tự',
  '1. Nhập chuỗi 51 ký tự vào ô tìm kiếm',
  '1. Hệ thống chặn, chỉ nhận 50 ký tự đầu', 'Kỹ thuật: Giá trị biên', 'srch_51')
T(None, 'Kiểm tra paste chuỗi vượt 50 ký tự',
  '1. Copy chuỗi 60 ký tự\n2. Paste vào ô tìm kiếm',
  '2. Ô tìm kiếm chỉ nhận 50 ký tự đầu', 'Kỹ thuật: Giá trị biên')
T('Khoảng trắng', 'Kiểm tra từ khoá có khoảng trắng đầu/cuối',
  '1. Nhập "  ORD2026080200222  " vào ô tìm kiếm',
  '1. Hệ thống bỏ dấu cách 2 đầu, hiển thị đơn hàng ORD2026080200222', f'{SRS} - BR1 "Bỏ dấu cách 2 đầu để search"', 'srch_trim')
T(None, 'Kiểm tra nhập toàn khoảng trắng',
  '1. Nhập 5 dấu cách vào ô tìm kiếm',
  '1. Sau khi trim từ khoá rỗng → hiển thị toàn bộ danh sách, không báo lỗi', f'{SRS} - BR1 - {BA}')
T(None, 'Kiểm tra từ khoá có khoảng trắng ở giữa',
  '1. Nhập "ORD2026 080200222"',
  '1. Không tìm thấy kết quả (khoảng trắng giữa được giữ nguyên khi so khớp)', f'{BA}')
T('Ký tự đặc biệt', 'Kiểm tra nhập ký tự đặc biệt / script',
  '1. Nhập "<script>alert(1)</script>" vào ô tìm kiếm',
  '1. Không thực thi script, hiển thị "Không tìm thấy kết quả", hệ thống không lỗi', 'Bảo mật cơ bản (XSS)')
T(None, 'Kiểm tra nhập ký tự wildcard SQL',
  "1. Nhập \"%' OR '1'='1\" vào ô tìm kiếm",
  '1. Không trả về toàn bộ danh sách, hiển thị "Không tìm thấy kết quả", hệ thống không lỗi', 'Bảo mật cơ bản (SQL injection)')
T('Không có kết quả', 'Kiểm tra tìm kiếm từ khoá không tồn tại',
  '1. Nhập "Mã đơn hàng ABC" vào ô tìm kiếm',
  '1. Bảng không có dữ liệu, hiển thị icon + text "Không tìm thấy kết quả"',
  f'{SRS} - UC Tìm kiếm - Ngoại lệ. Mâu thuẫn design: "Không tìm thấy kết quả phù hợp" + "Vui lòng thử từ khóa khác" - {BA}', 'srch_none')
T('Cơ chế trigger', 'Kiểm tra tự động tìm kiếm sau khi dừng gõ 300ms',
  '1. Nhập "ORD2026" vào ô tìm kiếm, không nhấn Enter\n2. Dừng gõ',
  '2. Sau khoảng 300ms hệ thống tự thực hiện tìm kiếm, không cần nhấn Enter',
  f'{SRS} - BR1 "Hệ thống tự động tìm kiếm sau 300ms"', 'srch_300')
T(None, 'Kiểm tra gõ liên tục không gửi nhiều request',
  '1. Gõ liên tục "ORD2026080200222" (mỗi ký tự cách nhau < 300ms)\n2. Quan sát request mạng (DevTools)',
  '2. Chỉ phát sinh 1 request tìm kiếm sau khi dừng gõ, kết quả cuối khớp từ khoá đầy đủ', f'{SRS} - BR1 - debounce')
T(None, 'Kiểm tra nhấn Enter',
  '1. Nhập "ORD2026080200222"\n2. Nhấn Enter',
  '2. Thực hiện tìm kiếm, kết quả giống khi chờ 300ms, không phát sinh lỗi/không reload trang')
T('Xoá từ khoá', 'Kiểm tra xoá từ khoá tìm kiếm',
  'ĐK: Đang hiển thị kết quả tìm kiếm\n1. Xoá hết từ khoá trong ô tìm kiếm',
  '1. Hệ thống tải lại toàn bộ danh sách đơn hàng ban đầu', f'{SRS} - UC Tìm kiếm - Luồng thay thế', 'srch_clear')
T('Copy/Paste', 'Kiểm tra paste mã đơn hàng vào ô tìm kiếm',
  '1. Copy Mã đơn hàng từ màn chi tiết\n2. Paste vào ô tìm kiếm',
  '2. Hiển thị đúng đơn hàng vừa copy')
T('Kết hợp bộ lọc', 'Kiểm tra tìm kiếm khi đang áp dụng bộ lọc',
  'ĐK: Đang lọc Trạng thái thanh toán = Thành công\n1. Nhập mã của 1 đơn có trạng thái thanh toán Thất bại',
  '1. Hiển thị "Không tìm thấy kết quả" (kết quả áp dụng đồng thời từ khoá và bộ lọc)', f'{SRS} - BR2', 'srch_filter_none')
T(None, 'Kiểm tra tìm kiếm khi đang lọc và đơn thoả cả 2 điều kiện',
  'ĐK: Đang lọc Trạng thái thanh toán = Thành công\n1. Nhập mã của 1 đơn có trạng thái thanh toán Thành công',
  '1. Hiển thị đúng đơn hàng đó', f'{SRS} - BR2', 'srch_filter_ok')
T(None, 'Kiểm tra kết quả tìm kiếm quay về trang 1',
  'ĐK: Đang ở trang 3 của danh sách\n1. Nhập từ khoá tìm kiếm có kết quả',
  '1. Kết quả hiển thị từ trang 1, phân trang và text tổng số kết quả cập nhật theo kết quả tìm kiếm')
T('Xử lý ngoại lệ', 'Kiểm tra tìm kiếm khi hệ thống lỗi / timeout',
  'ĐK: Giả lập API tìm kiếm trả lỗi/timeout\n1. Nhập từ khoá tìm kiếm',
  '1. Hiển thị thông báo: "Lỗi hệ thống, vui lòng thử lại sau"',
  f'{SRS} - UC Tìm kiếm - Ngoại lệ. {BA}: câu lỗi khác UC Xem DS ("Hệ thống bận, vui lòng thử lại sau")')
T(None, 'Kiểm tra tìm kiếm khi mất mạng',
  '1. Ngắt mạng\n2. Nhập từ khoá tìm kiếm',
  '2. Hiển thị thông báo: "Lỗi đường truyền. Vui lòng kiểm tra kết nối của bạn"', f'{SRS} - UC Tìm kiếm - Ngoại lệ')

# =====================================================================
S('UC3: (CMS admin) Chức năng Bộ lọc danh sách đơn hàng')
P(PRE + '\nBước 3: Click icon Bộ lọc → hiển thị panel Bộ lọc bên phải')

G('Kiểm tra gui UI/UX')
T('Icon Bộ lọc', 'Kiểm tra click icon Bộ lọc',
  '1. Click icon Bộ lọc (phễu) trên thanh công cụ',
  '1. \n - Hiển thị panel Bộ lọc bên phải danh sách\n - Icon Bộ lọc chuyển trạng thái active (nền đậm) theo design',
  f'{SRS} - UC Bộ lọc - Trigger + Figma', 'flt_open')
T(None, 'Kiểm tra click lại icon Bộ lọc khi panel đang mở',
  '1. Click icon Bộ lọc lần nữa',
  '1. Đóng panel Bộ lọc, icon trở về trạng thái mặc định; điều kiện đã áp dụng được giữ nguyên',
  f'{BA} cách đóng panel (click icon / click ngoài / có nút X)', 'flt_close')
T('Panel Bộ lọc', 'Kiểm tra giao diện panel Bộ lọc',
  '1. Kiểm tra panel Bộ lọc',
  '1. Hiển thị giống design gồm:\n + Tiêu đề "Bộ lọc" và link "Xoá lọc" góc trên phải\n'
  ' + 3 ô nhập có icon kính lúp: Mã đơn hàng CTT Tammi, Thuê bao đăng kí dịch vụ, Thuê bao thụ hưởng dịch vụ\n'
  ' + 6 dropdown: Phương thức thanh toán, Nguồn tiền, Kênh bán, Kết quả cung cấp dịch vụ, Trạng thái thanh toán, Trạng thái đơn hàng\n'
  ' + 2 ô chọn khoảng ngày có icon lịch: Thời gian tạo, Thời gian cập nhật\n + Button "Áp dụng" cuối panel',
  f'{SRS} - UC Bộ lọc - Mô tả giao diện + Figma. {BA}: bảng SRS đánh STT 1,2,3,8…15 (thiếu 4-7) - xác nhận không thiếu tiêu chí lọc', 'flt_ui')
T(None, 'Kiểm tra giá trị mặc định các trường trong panel Bộ lọc',
  'ĐK: Chưa từng áp dụng bộ lọc\n1. Kiểm tra giá trị các trường',
  '1. Ô nhập trống + placeholder đúng tên trường; dropdown trống + placeholder; ô khoảng ngày trống',
  f'{BA}: design ô Thời gian tạo/cập nhật đang hiển thị sẵn "10/08/2026 - 15/08/…" - mặc định trống hay có sẵn khoảng ngày', 'flt_default')
T(None, 'Kiểm tra cuộn panel Bộ lọc',
  '1. Thu nhỏ chiều cao cửa sổ trình duyệt\n2. Cuộn trong panel Bộ lọc',
  '2. Panel cuộn dọc được, xem được đến trường cuối cùng, button Áp dụng hiển thị đầy đủ theo design', 'Figma')
T('Button Áp dụng', 'Kiểm tra trạng thái button Áp dụng khi chưa nhập/chọn điều kiện nào',
  '1. Kiểm tra button Áp dụng khi tất cả trường trống',
  '1. Button Áp dụng ở trạng thái disable (màu xám) theo design',
  f'Figma. {BA}: SRS chưa có quy tắc enable/disable button Áp dụng', 'flt_btn_dis')
T(None, 'Kiểm tra trạng thái button Áp dụng khi đã nhập/chọn ít nhất 1 điều kiện',
  '1. Chọn Trạng thái thanh toán = Thành công\n2. Kiểm tra button Áp dụng',
  '2. Button Áp dụng enable', f'Figma - {BA}', 'flt_btn_en')

G('Kiểm tra validate - Ô nhập tìm kiếm trong bộ lọc')
for fld, note in (('Mã đơn hàng CTT Tammi', 'STT 1 - tìm theo miniapprequestid'),
                  ('Thuê bao đăng kí dịch vụ', 'STT 2'),
                  ('Thuê bao thụ hưởng dịch vụ', 'STT 3')):
    k = {'Mã đơn hàng CTT Tammi': 'ctt', 'Thuê bao đăng kí dịch vụ': 'tbdk', 'Thuê bao thụ hưởng dịch vụ': 'tbth'}[fld]
    T(f'Trường {fld}', 'Kiểm tra hiển thị mặc định',
      f'1. Kiểm tra ô {fld}',
      f'1. Mặc định trống, có icon kính lúp, placeholder: "{fld}"', f'{SRS} - UC Bộ lọc - {note}')
    T(None, 'Kiểm tra nhập 50 ký tự',
      f'1. Nhập chuỗi 50 ký tự vào ô {fld}',
      '1. Cho phép nhập đủ 50 ký tự', f'{SRS} - {note} "Chặn nhập quá 50 ký tự" - Kỹ thuật: Giá trị biên', f'flt_{k}_50')
    T(None, 'Kiểm tra nhập 51 ký tự',
      f'1. Nhập chuỗi 51 ký tự vào ô {fld}',
      '1. Hệ thống chặn, chỉ nhận 50 ký tự đầu', 'Kỹ thuật: Giá trị biên', f'flt_{k}_51')
T('Lọc theo Mã đơn hàng CTT Tammi', 'Kiểm tra lọc theo Mã đơn hàng CTT Tammi đúng toàn bộ chuỗi',
  'ĐK: Có đơn hàng mã CTT 123444444\n1. Nhập "123444444" vào ô Mã đơn hàng CTT Tammi\n2. Click Áp dụng',
  '2. Hiển thị đúng đơn hàng có Mã đơn hàng CTT Tammi = 123444444', f'{SRS} - STT 1', 'flt_ctt_ok')
T(None, 'Kiểm tra lọc theo 1 phần Mã đơn hàng CTT Tammi',
  '1. Nhập "12344" vào ô Mã đơn hàng CTT Tammi\n2. Click Áp dụng',
  '2. Hiển thị các đơn hàng có Mã đơn hàng CTT chứa "12344"', f'{BA}: tìm gần đúng hay chính xác', 'flt_ctt_part')
T(None, 'Kiểm tra lọc Mã đơn hàng CTT Tammi không phân biệt hoa thường, có dấu/không dấu',
  'ĐK: Có mã CTT chứa chữ cái (VD "abc123444")\n1. Nhập "ABC123444"\n2. Click Áp dụng',
  '2. Hiển thị đơn hàng có mã "abc123444"', f'{SRS} - STT 1')
T('Lọc theo Thuê bao đăng kí dịch vụ', 'Kiểm tra lọc theo đúng SĐT thuê bao đăng kí',
  'ĐK: Có đơn hàng do thuê bao 0987123456 mua\n1. Nhập "0987123456" vào ô Thuê bao đăng kí dịch vụ\n2. Click Áp dụng',
  '2. Hiển thị tất cả đơn hàng có Thuê bao đăng kí dịch vụ = 0987123456', f'{SRS} - STT 2', 'flt_tbdk_ok')
T(None, 'Kiểm tra lọc Thuê bao đăng kí dịch vụ nhập dạng +84',
  '1. Nhập "+84987123456" vào ô Thuê bao đăng kí dịch vụ\n2. Click Áp dụng',
  '2. Hiển thị các đơn hàng của thuê bao 0987123456',
  f'{BA}: UC Gói cước đã đăng ký có rule nhận diện +84, UC Đơn hàng chưa ghi', 'flt_tbdk_84')
T(None, 'Kiểm tra lọc Thuê bao đăng kí dịch vụ nhập chữ cái / ký tự đặc biệt',
  '1. Nhập "abc@#" vào ô Thuê bao đăng kí dịch vụ\n2. Click Áp dụng',
  '2. Hiển thị "Danh sách trống" (hoặc chặn nhập ký tự khác số theo quy định BA)',
  f'{BA}: SRS chưa giới hạn kiểu ký tự cho ô SĐT')
T('Lọc theo Thuê bao thụ hưởng dịch vụ', 'Kiểm tra lọc theo đúng SĐT thuê bao thụ hưởng',
  'ĐK: Có đơn hàng thụ hưởng thuê bao 0888333333333\n1. Nhập "0888333333333" vào ô Thuê bao thụ hưởng dịch vụ\n2. Click Áp dụng',
  '2. Hiển thị tất cả đơn hàng có Thuê bao thụ hưởng dịch vụ = 0888333333333', f'{SRS} - STT 3', 'flt_tbth_ok')
T(None, 'Kiểm tra lọc khi thuê bao đăng kí khác thuê bao thụ hưởng',
  'ĐK: Đơn A: thuê bao đăng kí X, thụ hưởng Y\n1. Nhập Y vào ô Thuê bao đăng kí dịch vụ\n2. Click Áp dụng',
  '2. Không hiển thị đơn A (lọc đúng theo trường đăng kí, không lẫn trường thụ hưởng)', 'Kỹ thuật: Phân vùng tương đương')
T(None, 'Kiểm tra ô nhập trong bộ lọc có khoảng trắng đầu/cuối',
  '1. Nhập "  0987123456  " vào ô Thuê bao đăng kí dịch vụ\n2. Click Áp dụng',
  '2. Hệ thống trim khoảng trắng, hiển thị đúng đơn hàng của thuê bao 0987123456', f'{BA}: rule trim chỉ ghi ở UC Tìm kiếm')

G('Kiểm tra validate - Dropdown lọc')
for fld, vals, stt, k in (
        ('Phương thức thanh toán', 'các kênh thanh toán (VD: Viettel Money, VNPay, ZaloPay…)', 'STT 8', 'pttt'),
        ('Nguồn tiền', 'các nguồn tiền thanh toán (VD: Viettel Pay…)', 'STT 9', 'nguon'),
        ('Kênh bán', 'các kênh phát sinh đơn hàng (VD: Miniapp gói cước Tammi, Web OA)', 'STT 10', 'kenh'),
        ('Kết quả cung cấp dịch vụ', 'Cung cấp dịch vụ thành công, Cung cấp dịch vụ thất bại, Cung cấp dịch vụ 1 phần', 'STT 11', 'ccdv'),
        ('Trạng thái thanh toán', 'Chờ thanh toán, Thành công, Thất bại', 'STT 12', 'tttt'),
        ('Trạng thái đơn hàng', 'Chờ thanh toán, Đã hủy, Chờ cung cấp dịch vụ, Chờ xử lý hoàn tiền, Hoàn thành', 'STT 13', 'ttdh')):
    T(f'Dropdown {fld}', 'Kiểm tra danh sách giá trị của dropdown',
      f'1. Click dropdown {fld}',
      f'1. Hiển thị đầy đủ {vals}; không thiếu, không lặp giá trị',
      f'{SRS} - UC Bộ lọc - {stt}' + ('' if k in ('ccdv', 'tttt', 'ttdh') else f'. {BA}: SRS chỉ ghi "Ví dụ" - chốt danh sách và nguồn dữ liệu'),
      f'flt_{k}_list')
    T(None, 'Kiểm tra lọc chọn 1 giá trị có dữ liệu',
      f'1. Chọn 1 giá trị trong dropdown {fld} (có đơn hàng thoả)\n2. Click Áp dụng',
      f'2. Chỉ hiển thị các đơn hàng có {fld} = giá trị đã chọn', f'{SRS} - {stt} - Phân vùng tương đương', f'flt_{k}_one')
    T(None, 'Kiểm tra lọc chọn nhiều giá trị',
      f'1. Chọn 2 giá trị trong dropdown {fld}\n2. Click Áp dụng',
      f'2. Hiển thị các đơn hàng có {fld} thuộc 1 trong 2 giá trị đã chọn (OR trong cùng 1 trường)',
      f'{SRS} - {stt} "Chọn 1 hoặc nhiều"', f'flt_{k}_multi')
T('Dropdown lọc - hành vi chung', 'Kiểm tra lọc chọn giá trị không có dữ liệu',
  'ĐK: Không có đơn hàng nào Trạng thái đơn hàng = Chờ xử lý hoàn tiền\n1. Chọn Trạng thái đơn hàng = Chờ xử lý hoàn tiền\n2. Click Áp dụng',
  '2. Bảng hiển thị "Danh sách trống"', f'{SRS} - UC Bộ lọc - Ngoại lệ', 'flt_empty')
T(None, 'Kiểm tra bỏ chọn 1 giá trị đã chọn trong dropdown',
  'ĐK: Đã chọn 2 giá trị Thành công, Thất bại ở dropdown Trạng thái thanh toán\n1. Bỏ chọn "Thất bại"\n2. Click Áp dụng',
  '2. Chỉ lọc theo "Thành công"')
T(None, 'Kiểm tra chọn tất cả giá trị của 1 dropdown',
  '1. Chọn đủ 3 giá trị của dropdown Trạng thái thanh toán\n2. Click Áp dụng',
  '2. Hiển thị toàn bộ đơn hàng (giống không lọc theo trường này)', 'Kỹ thuật: Giá trị biên (chọn tối đa)')
T(None, 'Kiểm tra hiển thị nhiều giá trị đã chọn trong ô dropdown',
  '1. Chọn 4 giá trị dropdown Trạng thái đơn hàng',
  '1. Ô dropdown hiển thị các giá trị đã chọn dạng tag / "+n" theo design, không tràn ô', f'{BA} cách hiển thị nhiều lựa chọn')
T(None, 'Kiểm tra đóng dropdown khi click ra ngoài',
  '1. Mở dropdown Kênh bán\n2. Click ra ngoài vùng dropdown',
  '2. Dropdown đóng, giữ các giá trị đã chọn')

G('Kiểm tra validate - Khoảng thời gian')
for fld, stt, k in (('Thời gian tạo', 'STT 14', 'tgt'), ('Thời gian cập nhật', 'STT 15', 'tgcn')):
    T(f'Trường {fld}', 'Kiểm tra mở lịch chọn khoảng ngày',
      f'1. Click icon lịch ở ô {fld}',
      '1. Hiển thị date range picker, cho phép chọn ngày bắt đầu và ngày kết thúc', f'{SRS} - {stt}')
    T(None, 'Kiểm tra định dạng hiển thị sau khi chọn',
      f'1. Chọn từ ngày 10/08/2026 đến 15/08/2026 ở ô {fld}',
      '1. Ô hiển thị "10/08/2026 - 15/08/2026" (định dạng DD/MM/YYYY - DD/MM/YYYY) và icon x để xoá', f'{SRS} - {stt} + Figma')
    T(None, 'Kiểm tra lọc lấy đơn tại 00:00:00 ngày bắt đầu',
      f'ĐK: Có đơn hàng {fld.lower()} lúc 10/08/2026 00:00:00\n1. Chọn {fld} 10/08/2026 - 15/08/2026\n2. Click Áp dụng',
      '2. Đơn hàng lúc 10/08/2026 00:00:00 có trong kết quả', f'{SRS} - {stt} "từ ngày bắt đầu (0h)" - Kỹ thuật: Giá trị biên', f'flt_{k}_start')
    T(None, 'Kiểm tra lọc không lấy đơn trước ngày bắt đầu',
      f'ĐK: Có đơn hàng {fld.lower()} lúc 09/08/2026 23:59:59\n1. Chọn {fld} 10/08/2026 - 15/08/2026\n2. Click Áp dụng',
      '2. Đơn hàng lúc 09/08/2026 23:59:59 KHÔNG có trong kết quả', 'Kỹ thuật: Giá trị biên (dưới biên)', f'flt_{k}_before')
    T(None, 'Kiểm tra lọc lấy đơn tại 23:59:59 ngày kết thúc',
      f'ĐK: Có đơn hàng {fld.lower()} lúc 15/08/2026 23:59:59\n1. Chọn {fld} 10/08/2026 - 15/08/2026\n2. Click Áp dụng',
      '2. Đơn hàng lúc 15/08/2026 23:59:59 có trong kết quả', f'{SRS} - {stt} "đến ngày kết thúc (23:59:59)" - Kỹ thuật: Giá trị biên', f'flt_{k}_end')
    T(None, 'Kiểm tra lọc không lấy đơn sau ngày kết thúc',
      f'ĐK: Có đơn hàng {fld.lower()} lúc 16/08/2026 00:00:00\n1. Chọn {fld} 10/08/2026 - 15/08/2026\n2. Click Áp dụng',
      '2. Đơn hàng lúc 16/08/2026 00:00:00 KHÔNG có trong kết quả', 'Kỹ thuật: Giá trị biên (trên biên)', f'flt_{k}_after')
T('Khoảng thời gian - hành vi chung', 'Kiểm tra chọn ngày bắt đầu = ngày kết thúc',
  'ĐK: Có đơn tạo lúc 10/08/2026 08:00 và 11/08/2026 08:00\n1. Chọn Thời gian tạo 10/08/2026 - 10/08/2026\n2. Click Áp dụng',
  '2. Chỉ hiển thị đơn hàng tạo trong ngày 10/08/2026', 'Kỹ thuật: Giá trị biên (khoảng 1 ngày)', 'flt_sameday')
T(None, 'Kiểm tra chọn ngày kết thúc nhỏ hơn ngày bắt đầu',
  '1. Trên date range picker chọn ngày bắt đầu 15/08/2026 rồi chọn ngày 10/08/2026',
  '1. Không cho phép chọn ngày kết thúc < ngày bắt đầu (hoặc tự hoán đổi) theo quy định',
  f'{BA}: SRS chưa có rule validate khoảng ngày', 'flt_reverse')
T(None, 'Kiểm tra chọn ngày trong tương lai',
  '1. Chọn Thời gian tạo từ hôm nay đến 1 ngày trong tương lai\n2. Click Áp dụng',
  '2. Cho phép chọn / chặn ngày tương lai theo quy định; nếu cho phép thì kết quả chỉ gồm đơn đến hiện tại',
  f'{BA}: có giới hạn ngày tương lai và độ dài khoảng ngày tối đa không')
T(None, 'Kiểm tra click icon x xoá khoảng ngày đã chọn',
  'ĐK: Ô Thời gian tạo đang có giá trị\n1. Click icon x trong ô',
  '1. Xoá giá trị khoảng ngày, ô trở về trống', 'Figma')
T(None, 'Kiểm tra chỉ chọn ngày bắt đầu, không chọn ngày kết thúc',
  '1. Chọn ngày bắt đầu 10/08/2026, đóng picker không chọn ngày kết thúc\n2. Click Áp dụng',
  '2. Xử lý theo quy định: chặn Áp dụng / báo lỗi / tự lấy ngày kết thúc = ngày bắt đầu', f'{BA}')

G('Kiểm tra chức năng - Kết hợp điều kiện & Xoá lọc')
T('Kết hợp điều kiện', 'Kiểm tra kết hợp 2 điều kiện: Trạng thái thanh toán + Kênh bán',
  'ĐK: Có đơn (Thành công, Miniapp), (Thất bại, Miniapp), (Thành công, Web OA)\n1. Chọn Trạng thái thanh toán = Thành công, Kênh bán = Miniapp gói cước Tammi\n2. Click Áp dụng',
  '2. Chỉ hiển thị đơn thoả đồng thời 2 điều kiện: (Thành công, Miniapp)', f'{SRS} - UC Bộ lọc - BR (AND giữa các trường) - Pairwise', 'cmb_2a')
T(None, 'Kiểm tra kết hợp 2 điều kiện: Trạng thái đơn hàng + Kết quả cung cấp dịch vụ',
  '1. Chọn Trạng thái đơn hàng = Chờ xử lý hoàn tiền, Kết quả CCDV = Cung cấp dịch vụ 1 phần\n2. Click Áp dụng',
  '2. Chỉ hiển thị đơn thoả đồng thời 2 điều kiện', 'Pairwise', 'cmb_2b')
T(None, 'Kiểm tra kết hợp ô nhập + dropdown: Thuê bao đăng kí + Trạng thái thanh toán',
  '1. Nhập Thuê bao đăng kí = 0987123456, chọn Trạng thái thanh toán = Thất bại\n2. Click Áp dụng',
  '2. Chỉ hiển thị các đơn thất bại của thuê bao 0987123456', 'Pairwise', 'cmb_2c')
T(None, 'Kiểm tra kết hợp dropdown + khoảng ngày: Phương thức thanh toán + Thời gian tạo',
  '1. Chọn Phương thức thanh toán = Viettel Money, Thời gian tạo 01/08/2026 - 31/08/2026\n2. Click Áp dụng',
  '2. Chỉ hiển thị đơn thanh toán Viettel Money tạo trong tháng 08/2026', 'Pairwise', 'cmb_2d')
T(None, 'Kiểm tra kết hợp 2 khoảng ngày: Thời gian tạo + Thời gian cập nhật',
  '1. Chọn Thời gian tạo 01/08/2026 - 05/08/2026, Thời gian cập nhật 06/08/2026 - 10/08/2026\n2. Click Áp dụng',
  '2. Chỉ hiển thị đơn tạo từ 01-05/08 và có lần cập nhật gần nhất từ 06-10/08', 'Pairwise', 'cmb_2e')
T(None, 'Kiểm tra kết hợp tất cả điều kiện lọc có kết quả',
  'ĐK: Có 1 đơn thoả tất cả 11 điều kiện\n1. Nhập/chọn đủ 11 trường đúng thông tin đơn đó\n2. Click Áp dụng',
  '2. Hiển thị đúng 1 đơn hàng thoả mãn', f'{SRS} - BR "thỏa mãn đồng thời tất cả các điều kiện"', 'cmb_all')
T(None, 'Kiểm tra kết hợp điều kiện mâu thuẫn',
  '1. Chọn Trạng thái thanh toán = Thất bại, Trạng thái đơn hàng = Hoàn thành\n2. Click Áp dụng',
  '2. Hiển thị "Danh sách trống" (theo sơ đồ trạng thái, đơn thanh toán thất bại luôn Đã hủy)', 'Sơ đồ chuyển trạng thái - kết hợp không hợp lệ', 'cmb_conflict')
T(None, 'Kiểm tra click Áp dụng liên tục nhiều lần',
  '1. Chọn Trạng thái thanh toán = Thành công\n2. Click Áp dụng liên tiếp 5 lần',
  '2. Kết quả không đổi, không phát sinh lỗi, không hiển thị trùng bản ghi')
T(None, 'Kiểm tra thay đổi điều kiện nhưng chưa click Áp dụng',
  'ĐK: Đang áp dụng Trạng thái thanh toán = Thành công\n1. Đổi sang Thất bại, không click Áp dụng',
  '1. Danh sách vẫn hiển thị theo điều kiện cũ (Thành công)')
T(None, 'Kiểm tra kết quả lọc quay về trang 1 và cập nhật tổng số kết quả',
  'ĐK: Đang ở trang 3\n1. Chọn 1 điều kiện lọc\n2. Click Áp dụng',
  '2. Hiển thị kết quả từ trang 1, text tổng số kết quả và số trang tính theo kết quả lọc')
T(None, 'Kiểm tra giữ điều kiện lọc khi quay lại từ màn chi tiết',
  'ĐK: Đang áp dụng bộ lọc\n1. Click Mã đơn hàng 1 dòng → màn chi tiết\n2. Click ← quay lại',
  '2. Danh sách vẫn giữ điều kiện lọc và trang đang xem', f'{BA}', 'flt_keep_back')
T(None, 'Kiểm tra điều kiện lọc sau khi F5 tải lại trang',
  'ĐK: Đang áp dụng bộ lọc\n1. Nhấn F5',
  '1. Giữ / reset điều kiện lọc theo quy định', f'{BA}: SRS chưa nêu')
T('Xoá lọc', 'Kiểm tra click Xoá lọc khi đã áp dụng điều kiện',
  'ĐK: Đã nhập/chọn và áp dụng nhiều điều kiện\n1. Click "Xoá lọc"',
  '1. Reset toàn bộ giá trị các trường về mặc định, danh sách hiển thị lại toàn bộ đơn hàng',
  f'{SRS} - UC Bộ lọc - Luồng thay thế. {BA}: Xoá lọc có tự áp dụng luôn hay cần click Áp dụng', 'flt_reset')
T(None, 'Kiểm tra click Xoá lọc khi chưa nhập điều kiện nào',
  '1. Click "Xoá lọc" khi các trường đang trống',
  '1. Không thay đổi gì, không lỗi')
T(None, 'Kiểm tra Xoá lọc không ảnh hưởng từ khoá ô tìm kiếm',
  'ĐK: Ô tìm kiếm có "ORD2026", bộ lọc có Trạng thái thanh toán = Thành công\n1. Click "Xoá lọc"',
  '1. Chỉ xoá điều kiện trong panel; từ khoá ô tìm kiếm giữ nguyên và vẫn áp dụng', f'{BA}')
T('Xử lý ngoại lệ', 'Kiểm tra lọc khi hệ thống lỗi',
  'ĐK: Giả lập API lọc trả lỗi\n1. Chọn điều kiện\n2. Click Áp dụng',
  '2. Hiển thị thông báo lỗi hệ thống', f'{SRS} - UC Bộ lọc - Ngoại lệ. {BA}: SRS chưa có câu thông báo cụ thể')
T(None, 'Kiểm tra lọc khi mất mạng',
  '1. Ngắt mạng\n2. Click Áp dụng',
  '2. Hiển thị thông báo: "Lỗi đường truyền. Vui lòng kiểm tra kết nối của bạn"', f'{SRS} - UC Bộ lọc - Luồng thay thế')

# =====================================================================
S('UC4: (CMS admin) Chức năng Cài đặt bảng danh sách đơn hàng')
P(PRE + '\nBước 3: Click button Cài đặt bảng')

G('Kiểm tra gui UI/UX')
T('Button Cài đặt bảng', 'Kiểm tra hiển thị button Cài đặt bảng',
  '1. Kiểm tra button Cài đặt bảng trên thanh công cụ',
  '1. Hiển thị button viền, icon bánh răng + text "Cài đặt bảng", trạng thái enable', 'Figma')
T(None, 'Kiểm tra click button Cài đặt bảng',
  '1. Click button Cài đặt bảng',
  '1. Hiển thị popup danh sách các cột của bảng kèm checkbox để chọn ẩn/hiện và nút xác nhận',
  f'{SRS} - UC Cài đặt bảng - Main flow. {BA}: Figma chưa có frame popup Cài đặt bảng của màn đơn hàng - xin design', 'cdb_open')
T('Popup Cài đặt bảng', 'Kiểm tra danh sách và thứ tự các lựa chọn',
  '1. Kiểm tra danh sách lựa chọn trong popup',
  '1. Gồm lựa chọn "Tất cả" + các cột theo đúng tên và thứ tự mô tả tại UC Xem danh sách (STT, ID, Trạng thái thanh toán, … , Người cập nhật)',
  f'{SRS} - UC Cài đặt bảng - BR "Danh sách, thứ tự các lựa chọn: lấy theo tên cột thông tin được mô tả tại UC". {BA}: cột Thao tác có trong danh sách không', 'cdb_list')
T(None, 'Kiểm tra trạng thái mặc định lần đầu mở popup',
  'ĐK: Tài khoản chưa từng cài đặt bảng\n1. Mở popup Cài đặt bảng',
  '1. Tất cả lựa chọn đều được tick, kể cả "Tất cả"', f'{SRS} - BR "Lần đầu click … mặc định tích chọn tất cả các cột (có cả cột tất cả)"', 'cdb_default')

G('Kiểm tra chức năng')
T('Checkbox Tất cả', 'Kiểm tra bỏ tick "Tất cả"',
  'ĐK: Tất cả lựa chọn đang được tick\n1. Bỏ tick "Tất cả"',
  '1. Bỏ tick toàn bộ lựa chọn; nút xác nhận chuyển disable', f'{SRS} - BR "Bỏ click tất cả→ Bỏ tick tất cả lựa chọn" + "Btn xác nhận chỉ enable nếu có ít nhất 1 lựa chọn"', 'cdb_all_off')
T(None, 'Kiểm tra tick "Tất cả" khi đang bỏ tick một số cột',
  'ĐK: Đang bỏ tick 3 cột\n1. Tick "Tất cả"',
  '1. Tick toàn bộ lựa chọn', f'{SRS} - BR "Click tất cả → tick tất cả lựa chọn"', 'cdb_all_on')
T(None, 'Kiểm tra trạng thái "Tất cả" khi bỏ tick 1 cột',
  'ĐK: Tất cả đang được tick\n1. Bỏ tick cột "Mã đơn hàng CTT Tammi"',
  '1. Checkbox "Tất cả" tự bỏ tick (hoặc trạng thái chọn 1 phần theo design)', f'{BA}', 'cdb_partial')
T(None, 'Kiểm tra "Tất cả" tự được tick khi tick đủ các cột',
  'ĐK: Chỉ còn 1 cột chưa tick\n1. Tick cột đó',
  '1. Checkbox "Tất cả" tự động được tick', f'{BA}')
T('Nút xác nhận', 'Kiểm tra trạng thái nút xác nhận khi chỉ còn 1 lựa chọn được tick',
  '1. Bỏ tick tất cả các cột trừ cột "Mã đơn hàng"',
  '1. Nút xác nhận vẫn enable', f'{SRS} - BR - Kỹ thuật: Giá trị biên (1 lựa chọn)', 'cdb_btn_1')
T(None, 'Kiểm tra trạng thái nút xác nhận khi không còn lựa chọn nào',
  '1. Bỏ tick toàn bộ lựa chọn',
  '1. Nút xác nhận disable', f'{SRS} - BR - Kỹ thuật: Giá trị biên (0 lựa chọn)', 'cdb_btn_0')
T(None, 'Kiểm tra ẩn 1 cột',
  '1. Bỏ tick cột "Mã đơn hàng CTT Tammi"\n2. Click xác nhận',
  '2. Đóng popup, bảng không còn cột Mã đơn hàng CTT Tammi; các cột khác giữ đúng thứ tự và dữ liệu', f'{SRS} - Main flow bước 3', 'cdb_hide1')
T(None, 'Kiểm tra ẩn nhiều cột',
  '1. Bỏ tick 5 cột bất kỳ\n2. Click xác nhận',
  '2. Bảng ẩn đúng 5 cột đã bỏ tick', 'Kỹ thuật: Phân vùng tương đương', 'cdb_hideN')
T(None, 'Kiểm tra chỉ hiển thị 1 cột',
  '1. Chỉ tick cột "Mã đơn hàng"\n2. Click xác nhận',
  '2. Bảng chỉ còn cột Mã đơn hàng (và cột Thao tác nếu là cột cố định), không vỡ layout', 'Kỹ thuật: Giá trị biên')
T(None, 'Kiểm tra hiển thị lại cột đã ẩn',
  'ĐK: Cột Kênh bán đang bị ẩn\n1. Tick cột Kênh bán\n2. Click xác nhận',
  '2. Cột Kênh bán hiển thị lại đúng vị trí ban đầu, dữ liệu đúng', 'Sơ đồ chuyển trạng thái (Ẩn → Hiện)', 'cdb_show')
T(None, 'Kiểm tra popup hiển thị đúng cấu hình đang áp dụng khi mở lại',
  'ĐK: Đã ẩn cột Kênh bán và xác nhận\n1. Mở lại popup Cài đặt bảng',
  '1. Cột Kênh bán bỏ tick, các cột khác được tick, "Tất cả" bỏ tick')
T('Click outside', 'Kiểm tra click ra ngoài popup khi đã thay đổi lựa chọn',
  '1. Bỏ tick cột Kênh bán\n2. Click ra ngoài popup',
  '2. Đóng popup, không lưu lựa chọn, bảng không ẩn/hiện cột theo lựa chọn vừa đổi', f'{SRS} - Alternate Flow Th3', 'cdb_outside')
T('Không ảnh hưởng tìm kiếm/lọc/sắp xếp', 'Kiểm tra cài đặt bảng giữ nguyên kết quả tìm kiếm, lọc, sắp xếp',
  'ĐK: Đang tìm kiếm "ORD2026", lọc Trạng thái thanh toán = Thành công, sắp xếp Thời gian tạo tăng dần\n1. Ẩn cột Trạng thái thanh toán\n2. Click xác nhận',
  '2. Kết quả danh sách, điều kiện lọc, từ khoá và thứ tự sắp xếp giữ nguyên; chỉ ẩn cột', f'{SRS} - BR "Việc cài đặt bảng ko ảnh hưởng đến bộ lọc/ tìm kiếm/ sort"', 'cdb_keep')
T(None, 'Kiểm tra lọc theo trường có cột đang bị ẩn',
  'ĐK: Cột Kênh bán đang ẩn\n1. Lọc Kênh bán = Miniapp gói cước Tammi',
  '1. Lọc vẫn hoạt động đúng dù cột đang ẩn')
T('Lưu cấu hình', 'Kiểm tra cấu hình bảng sau khi F5 / đăng nhập lại',
  'ĐK: Đã ẩn cột Kênh bán\n1. F5 tải lại trang\n2. Đăng xuất, đăng nhập lại',
  '1, 2. Giữ / reset cấu hình theo quy định',
  f'{BA}: SRS chỉ ghi "Lần đầu click … mặc định tích tất cả" - cấu hình lưu theo tài khoản, theo trình duyệt hay theo phiên')
T(None, 'Kiểm tra cấu hình bảng độc lập giữa 2 tài khoản admin',
  'ĐK: Admin A ẩn cột Kênh bán\n1. Đăng nhập Admin B, mở Danh sách đơn hàng',
  '1. Admin B vẫn thấy cột Kênh bán (cấu hình không dùng chung)', f'{BA}')
T('Xử lý ngoại lệ', 'Kiểm tra lưu cài đặt bảng khi mất mạng',
  '1. Bỏ tick 1 cột\n2. Ngắt mạng\n3. Click xác nhận',
  '3. Hiển thị toast: "Thất bại. Vui lòng kiểm tra lại kết nối"; bảng không thay đổi', f'{SRS} - Alternate Flow TH1')
T(None, 'Kiểm tra lưu cài đặt bảng khi hệ thống lỗi',
  'ĐK: Giả lập API lưu cài đặt bảng trả lỗi\n1. Bỏ tick 1 cột\n2. Click xác nhận',
  '2. Hiển thị toast: "Hệ thống bận. Vui lòng thử lại sau"; bảng không thay đổi', f'{SRS} - Alternate Flow TH2')

# =====================================================================
S('UC5: (CMS admin) Chức năng Xem chi tiết đơn hàng')
P(PRE + '\nBước 3: Click Mã đơn hàng (hoặc icon (i) cột Thao tác) của 1 đơn hàng')

G('Kiểm tra gui UI/UX')
T('Kiểm tra UI', 'Kiểm tra hiển thị giao diện mặc định màn Chi tiết đơn hàng',
  '1. Kiểm tra màn Chi tiết đơn hàng',
  '1. Hiển thị giống design gồm:\n + Icon ← và tiêu đề "Chi tiết đơn hàng"\n + Dải thông tin đầu trang: Mã đơn hàng, ID, Trạng thái đơn hàng (badge + icon ⓘ)\n'
  ' + Khối "Thông tin đơn hàng" (mở rộng)\n + Khối "Dòng đơn hàng" (dropdown lọc Trạng thái, button Cài đặt bảng, bảng dòng đơn hàng)\n'
  ' + Khối "Thông tin xuất hóa đơn" (khi đơn có xuất hoá đơn)',
  f'{SRS} - UC Xem chi tiết - Luồng chính bước 3 + Figma Chi tiết đơn hàng', 'dt_ui')
T(None, 'Kiểm tra tổng thể giao diện màn hình',
  '1. Kiểm tra về bố cục, font chữ, chính tả, màu chữ',
  '1. \n - Các label, có độ dài, rộng và khoảng cách bằng nhau, không xô lệch\n'
  ' - Các label sử dụng cùng 1 loại font, cỡ chữ, căn lề\n'
  ' - Kiểm tra tất cả lỗi về chính tả, cấu trúc câu, ngữ pháp trên màn hình\n - Form được bố trí hợp lý và dễ sử dụng')
T(None, 'Kiểm tra giao diện khi thu nhỏ, phóng to',
  '1. Nhấn tổ hợp phím Ctrl -\n2. Nhấn tổ hợp phím Ctrl +',
  '2. Màn hình thu nhỏ, phóng to tương ứng và không bị vỡ giao diện')
T('Tiêu đề trang', 'Kiểm tra tiêu đề trang chi tiết',
  '1. Kiểm tra tiêu đề góc trên bên trái',
  '1. Hiển thị tiêu đề kèm ID đơn hàng: "Chi tiết đơn hàng- ID: <ID>" (VD: Chi tiết đơn hàng- ID: 12233344444)',
  f'{SRS} - Khối đơn cha STT 1. Mâu thuẫn design: tiêu đề chỉ "Chi tiết đơn hàng", ID hiển thị ở ô riêng - {BA}', 'dt_title')
T('Icon quay lại', 'Kiểm tra click icon ← quay lại',
  '1. Click icon ← cạnh tiêu đề',
  '1. Quay về màn Danh sách đơn hàng', f'Figma - SRS chưa mô tả', 'dt_back')
T('Collapse/Expand khối', 'Kiểm tra thu gọn khối Thông tin đơn hàng',
  'ĐK: Khối Thông tin đơn hàng đang mở\n1. Click icon ⌃ tại khối Thông tin đơn hàng',
  '1. Ẩn nội dung khối, icon đổi thành ⌄; các khối khác giữ nguyên', 'Figma (frame Chi tiết - Thông tin đơn hàng thu gọn)', 'dt_collapse')
T(None, 'Kiểm tra mở rộng lại khối Thông tin đơn hàng',
  'ĐK: Khối Thông tin đơn hàng đang thu gọn\n1. Click icon ⌄',
  '1. Hiển thị lại toàn bộ nội dung khối, icon đổi thành ⌃', 'Figma', 'dt_expand')
T(None, 'Kiểm tra thu gọn/mở rộng khối Dòng đơn hàng và khối Thông tin xuất hóa đơn',
  '1. Click icon ⌃ của khối Dòng đơn hàng\n2. Click icon ⌃ của khối Thông tin xuất hóa đơn\n3. Click lại icon ⌄ của 2 khối',
  '1, 2. Khối tương ứng thu gọn\n3. Khối mở rộng lại, dữ liệu không đổi', 'Figma')
T(None, 'Kiểm tra trạng thái mặc định các khối khi mở màn chi tiết',
  '1. Mở màn Chi tiết đơn hàng',
  '1. Tất cả các khối ở trạng thái mở rộng', f'Figma - {BA}')

G('Khối thông tin đầu trang & Thông tin đơn hàng')
T('Mã đơn hàng', 'Kiểm tra hiển thị Mã đơn hàng',
  '1. Kiểm tra trường Mã đơn hàng\n2. Đối chiếu với Mã đơn hàng ở màn danh sách',
  '2. Hiển thị đúng mã đơn hàng nội bộ của đơn đã chọn', f'{SRS} - Khối đơn cha STT 2')
T('ID', 'Kiểm tra hiển thị ID đơn hàng',
  '1. Kiểm tra trường ID',
  '1. Hiển thị đúng ID đơn hàng đã chọn từ danh sách', 'Figma')
T('Trạng thái đơn hàng', 'Kiểm tra badge Trạng thái đơn hàng',
  '1. Kiểm tra badge Trạng thái đơn hàng',
  '1. Hiển thị đúng 1 trong các giá trị: Chờ thanh toán, Đã hủy, Chờ cung cấp dịch vụ, Chờ xử lý hoàn tiền, Hoàn thành; khớp cột trạng thái ở màn danh sách',
  f'{SRS} - Khối đơn cha STT 3')
T(None, 'Kiểm tra hover icon ⓘ cạnh Trạng thái đơn hàng',
  '1. Di chuột / click icon ⓘ cạnh label Trạng thái đơn hàng',
  '1. Hiển thị tooltip giải thích trạng thái theo design',
  f'Figma. {BA}: SRS không mô tả icon ⓘ và nội dung tooltip', 'dt_tooltip')
T('Loại dịch vụ', 'Kiểm tra hiển thị Loại dịch vụ',
  '1. Kiểm tra trường Loại dịch vụ', '1. Hiển thị "Gói cước"', f'{SRS} - Khối đơn cha STT 4')
T('Phương thức thanh toán', 'Kiểm tra hiển thị Phương thức thanh toán',
  'ĐK: Đơn thanh toán qua Viettel Money\n1. Kiểm tra trường Phương thức thanh toán',
  '1. Hiển thị tên phương thức thanh toán "Viettel Money"',
  f'{SRS} - Khối đơn cha STT 5. {BA}: SRS mô tả STT 5 "Hiển thị số điện thoại của tài khoản…" (lỗi copy) - xác nhận hiển thị tên PTTT', 'dt_pttt')
T('Thuê bao đăng ký dịch vụ', 'Kiểm tra hiển thị Thuê bao đăng ký dịch vụ',
  '1. Kiểm tra trường Thuê bao đăng ký dịch vụ', '1. Hiển thị đúng SĐT tài khoản thực hiện đăng ký', f'{SRS} - Khối đơn cha STT 6')
T('Nguồn tiền', 'Kiểm tra hiển thị Nguồn tiền',
  'ĐK: Đơn thanh toán thành công, CTT trả nguồn tiền Viettel Pay\n1. Kiểm tra trường Nguồn tiền',
  '1. Hiển thị "Viettel Pay"', f'{SRS} - Khối đơn cha STT 7 "ctt trả". {BA}: đơn chưa thanh toán hiển thị gì')
T('Loại thuê bao đăng ký dịch vụ', 'Kiểm tra hiển thị Loại thuê bao đăng ký dịch vụ',
  '1. Kiểm tra trường Loại thuê bao đăng ký dịch vụ', '1. Hiển thị "Tk Tammi"',
  f'{SRS} - Khối đơn cha STT 8 (dữ liệu mẫu design đang sai: hiển thị dãy số)')
T('Kênh bán', 'Kiểm tra hiển thị Kênh bán',
  '1. Kiểm tra trường Kênh bán', '1. Hiển thị "Miniapp gói cước Tammi"', f'{SRS} - Khối đơn cha STT 9')
T('Mã đơn hàng CTT', 'Kiểm tra hiển thị Mã đơn hàng CTT',
  'ĐK: Đơn đã có mã giao dịch CTT\n1. Kiểm tra trường Mã đơn hàng CTT',
  '1. Hiển thị đúng miniapprequestid; khớp cột Mã đơn hàng CTT Tammi ở danh sách',
  f'{SRS} - Khối đơn cha STT 10. {BA}: tên trường khác màn danh sách ("Mã đơn hàng CTT" / "Mã đơn hàng CTT Tammi")')
T('Mã giới thiệu', 'Kiểm tra hiển thị Mã giới thiệu khi đơn có mã nhân viên giới thiệu',
  'ĐK: Đơn có nhập mã nhân viên giới thiệu\n1. Kiểm tra trường Mã giới thiệu',
  '1. Hiển thị đúng mã nhân viên giới thiệu', f'{SRS} - Khối đơn cha (dòng không STT) - Phân vùng tương đương', 'dt_ref_has')
T(None, 'Kiểm tra hiển thị Mã giới thiệu khi đơn không có mã giới thiệu',
  'ĐK: Đơn mua trên Miniapp không nhập mã giới thiệu\n1. Kiểm tra trường Mã giới thiệu',
  '1. Để trống / hiển thị "-" theo quy định',
  f'{BA}: (1) Figma Miniapp không có bước nhập mã giới thiệu - phase 1 có dữ liệu này không; (2) cách hiển thị khi rỗng', 'dt_ref_none')
T('Thuê bao thụ hưởng dịch vụ', 'Kiểm tra hiển thị Thuê bao thụ hưởng dịch vụ',
  '1. Kiểm tra trường Thuê bao thụ hưởng dịch vụ', '1. Hiển thị đúng SĐT thuê bao nhận quyền lợi', f'{SRS} - Khối đơn cha STT 11')
T('Kết quả cung cấp dịch vụ', 'Kiểm tra hiển thị Kết quả cung cấp dịch vụ',
  'ĐK: Đơn đã kích hoạt thành công toàn bộ quyền lợi\n1. Kiểm tra trường Kết quả cung cấp dịch vụ',
  '1. Hiển thị "Cung cấp dịch vụ thành công", khớp cột ở màn danh sách',
  f'{SRS} - Khối đơn cha STT 12. Mâu thuẫn design ("Hoàn thành cung cấp dịch vụ") - {BA}')
T('Loại thuê bao thụ hưởng dịch vụ', 'Kiểm tra hiển thị Loại thuê bao thụ hưởng dịch vụ',
  '1. Kiểm tra trường Loại thuê bao thụ hưởng dịch vụ', '1. Hiển thị Tk Tammi hoặc Tk OA đúng dữ liệu đơn', f'{SRS} - Khối đơn cha STT 13')
T('Trạng thái thanh toán', 'Kiểm tra badge Trạng thái thanh toán',
  '1. Kiểm tra badge Trạng thái thanh toán',
  '1. Hiển thị đúng trạng thái; "Thành công" màu xanh lá', f'{SRS} - Khối đơn cha STT 14')
T('Số tiền', 'Kiểm tra Tổng giá gốc, Tổng chiết khấu, Tổng tiền sau chiết khấu, Tổng tiền thanh toán',
  'ĐK: Đơn giá gốc 100.000đ, CTKM 20.000đ, voucher CTT 1.000đ\n1. Kiểm tra 4 trường số tiền',
  '1. Tổng giá gốc 100.000đ; Tổng chiết khấu dịch vụ 20.000đ; Tổng tiền sau chiết khấu dịch vụ 80.000đ; Tổng tiền thanh toán 79.000đ; khớp các cột tương ứng ở màn danh sách',
  f'{SRS} - Khối đơn cha STT 15, 17, (không STT), 19', 'dt_money')
T(None, 'Kiểm tra Tổng chiết khấu dịch vụ khi đơn không có CTKM',
  'ĐK: Đơn không áp dụng CTKM\n1. Kiểm tra trường Tổng chiết khấu dịch vụ',
  '1. Hiển thị 0đ', f'{SRS} - STT 17 "Ko có hiển thị= 0đ"')
T(None, 'Kiểm tra Tổng tiền sau chiết khấu khớp với số tiền hiển thị trên Miniapp',
  'ĐK: Mua gói trên Miniapp, nút đăng ký hiển thị "Đăng ký chỉ với 1.365.000đ/ 7 tháng"\n1. Thanh toán thành công\n2. Mở chi tiết đơn trên CMS',
  '2. Tổng tiền sau chiết khấu dịch vụ = 1.365.000đ, bằng "Số tiền" trên màn kết quả Miniapp',
  'Figma Miniapp màn Đăng ký gói + màn Kết quả; SRS màn Kết quả STT 9 "tổng giá tiền sau CK của đơn hàng"', 'dt_money_app')
T('Thời gian thanh toán thành công', 'Kiểm tra Thời gian thanh toán thành công khi đơn đã thanh toán',
  'ĐK: Đơn thanh toán thành công\n1. Kiểm tra trường Thời gian thanh toán thành công',
  '1. Hiển thị mốc thời gian ghi nhận thanh toán thành công, định dạng DD/MM/YYYY HH:MM:SS; khớp thời gian trên màn kết quả Miniapp',
  f'{SRS} - Khối đơn cha STT 16 - Phân vùng tương đương', 'dt_paytime')
T(None, 'Kiểm tra Thời gian thanh toán thành công khi đơn chưa/không thanh toán thành công',
  'ĐK: Đơn Chờ thanh toán hoặc thanh toán Thất bại\n1. Kiểm tra trường Thời gian thanh toán thành công',
  '1. Để trống / hiển thị "-"', f'{SRS} - STT 16 (Bắt buộc = Không) - {BA} cách hiển thị', 'dt_paytime_none')
T('Thời gian tạo', 'Kiểm tra hiển thị Thời gian tạo',
  '1. Kiểm tra trường Thời gian tạo',
  '1. Hiển thị mốc thời gian khởi tạo đơn, định dạng DD/MM/YYYY HH:MM:SS, khớp màn danh sách',
  f'{SRS} - Khối đơn cha STT 18 (dữ liệu mẫu design đang sai: hiển thị dãy số)')
T('Thời gian cập nhật', 'Kiểm tra hiển thị Thời gian cập nhật',
  '1. Kiểm tra trường Thời gian cập nhật',
  '1. Hiển thị mốc thời gian gần nhất đơn có thay đổi (VD 30/07/2026 00:12:20)', f'{SRS} - Khối đơn cha STT 20')
T('Người cập nhật', 'Kiểm tra hiển thị Người cập nhật',
  '1. Kiểm tra trường Người cập nhật',
  '1. Hiển thị tài khoản thực hiện cập nhật gần nhất (VD: System)', f'{SRS} - Khối đơn cha STT 21')

G('Khối Dòng đơn hàng')
T('Bảng dòng đơn hàng', 'Kiểm tra các cột của bảng Dòng đơn hàng',
  '1. Cuộn ngang bảng Dòng đơn hàng, kiểm tra header các cột',
  '1. Hiển thị đủ các cột: STT, ID, Trạng thái, Mã gói cước, ID loại gói cước, Tên loại gói cước, Loại dịch vụ gói cước, Loại hình gói, Chu kỳ, '
  'Số lượng chu kỳ, Tên - Giá trị tham số, Số lượng giá trị tham số, Mã CTKM, Giá trị khuyến mại, Giá gốc, Chiết khấu, Thành tiền, Thời gian tạo, Thời gian cập nhật, Người cập nhật',
  f'{SRS} - Khối bảng dòng đơn hàng. {BA}: design có thêm cột "Gia hạn tự động" không có trong SRS', 'line_cols')
T(None, 'Kiểm tra số dòng đơn hàng của đơn mua từ Miniapp',
  'ĐK: Đơn mua 1 gói trên Miniapp\n1. Kiểm tra bảng Dòng đơn hàng',
  '1. Chỉ có 1 dòng đơn hàng; Số lượng chu kỳ = 1',
  'SRS Miniapp - UC Kiểm tra gói, tạo đơn - BR2 "1 đơn hàng chỉ có 1 gói cước (1 dòng hàng)… Số lượng chu kì… mặc định bằng 1"', 'line_one')
T(None, 'Kiểm tra thứ tự hiển thị các dòng đơn hàng',
  'ĐK: Đơn có nhiều dòng đơn hàng (đơn tạo từ kênh khác / dữ liệu test)\n1. Kiểm tra cột ID',
  '1. Các dòng sắp xếp theo ID từ bé đến lớn', f'{SRS} - UC Xem chi tiết - BR1', 'line_order')
T('Cột Trạng thái dòng đơn hàng', 'Kiểm tra badge trạng thái dòng đơn hàng',
  'ĐK: Có dòng đơn hàng ở các trạng thái khác nhau\n1. Kiểm tra cột Trạng thái',
  '1. Hiển thị đúng 1 trong các giá trị: Khởi tạo, Chờ cung cấp dịch vụ, Đã hủy, Cung cấp dịch vụ thất bại, Cung cấp dịch vụ 1 phần, Cung cấp dịch vụ thành công; mỗi trạng thái 1 màu badge theo design',
  f'{SRS} - Dòng đơn hàng STT 3. {BA}: bảng "Trạng thái đơn hàng con" ở Tổng hợp trạng thái không có "Chờ cung cấp dịch vụ"', 'line_status')
T('Thông tin gói', 'Kiểm tra Mã gói cước, ID loại gói cước, Tên loại gói cước, Loại dịch vụ gói cước, Loại hình gói, Chu kỳ',
  '1. Kiểm tra các cột thông tin gói\n2. Đối chiếu với gói đã mua trên Miniapp',
  '2. Hiển thị đúng thông tin gói tại thời điểm mua (VD Mã gói TM30, Loại dịch vụ OA, Loại hình Gói chính/Gói add-on, Chu kỳ "1 tháng" = chu kỳ + đơn vị)',
  f'{SRS} - Dòng đơn hàng STT 4-9', 'line_pkg')
T(None, 'Kiểm tra thông tin dòng đơn hàng là bản snapshot tại thời điểm mua',
  'ĐK: Đơn đã mua gói X\n1. Trên CMS Quản lý gói cước sửa mô tả/tag/giá gốc của gói X (trạng thái cho phép sửa)\n2. Mở lại chi tiết đơn hàng',
  '2. Thông tin trên dòng đơn hàng giữ nguyên giá trị tại thời điểm mua, không đổi theo gói X',
  'SRS Miniapp - BR3 "bắt buộc phải snapshot lại các thông tin loại gói, gói, quyền lợi gói, CTKM"', 'line_snapshot')
T('Tham số', 'Kiểm tra Tên - Giá trị tham số và Số lượng giá trị tham số khi gói có tham số',
  'ĐK: Gói có tham số Số lượng cộng dồn 5.000 tin\n1. Kiểm tra 2 cột tham số',
  '1. Tên - Giá trị tham số: "Số lượng cộng dồn- 5.000 tin"; Số lượng giá trị tham số hiển thị đúng', f'{SRS} - Dòng đơn hàng STT 11, 12', 'line_param')
T(None, 'Kiểm tra cột tham số khi gói không có tham số',
  'ĐK: Gói không có tham số lựa chọn\n1. Kiểm tra 2 cột tham số',
  '1. Tên - Giá trị tham số hiển thị "-"; Số lượng giá trị tham số để trống/"-"',
  f'{SRS} - STT 11 "hiển thị dấu - nếu không có", STT 12 "null". {BA} thống nhất cách hiển thị', 'line_param_none')
T('Khuyến mại', 'Kiểm tra Mã CTKM, Giá trị khuyến mại, Chiết khấu khi CTKM giảm %',
  'ĐK: Gói giá gốc 100.000đ, CTKM 12344555 giảm 30%\n1. Kiểm tra các cột Mã CTKM, Giá trị khuyến mại, Chiết khấu, Thành tiền',
  '1. Mã CTKM 12344555; Giá trị khuyến mại "30%"; Chiết khấu 30.000đ; Thành tiền 70.000đ',
  f'{SRS} - Dòng đơn hàng STT 13-17 - Phân vùng tương đương (giảm %/giảm tiền/không CTKM). Design mẫu ghi 30% nhưng chiết khấu 20.000đ - dữ liệu mẫu lệch', 'line_km_pct')
T(None, 'Kiểm tra Mã CTKM, Giá trị khuyến mại, Chiết khấu khi CTKM giảm số tiền',
  'ĐK: Gói giá gốc 100.000đ, CTKM giảm 10.000đ\n1. Kiểm tra các cột khuyến mại',
  '1. Giá trị khuyến mại "10.000đ"; Chiết khấu 10.000đ; Thành tiền 90.000đ', f'{SRS} - Dòng đơn hàng STT 14', 'line_km_vnd')
T(None, 'Kiểm tra các cột khuyến mại khi gói không có CTKM',
  'ĐK: Gói không có CTKM\n1. Kiểm tra các cột khuyến mại',
  '1. Mã CTKM, Giá trị khuyến mại để trống/"-"; Chiết khấu 0đ (hoặc trống); Thành tiền = Giá gốc', f'{SRS} - STT 13, 14, 16 (Bắt buộc = Không) - {BA}', 'line_km_none')
T(None, 'Kiểm tra tổng các dòng đơn hàng khớp khối Thông tin đơn hàng',
  'ĐK: Đơn có ≥ 1 dòng đơn hàng\n1. Cộng Giá gốc, Chiết khấu, Thành tiền các dòng\n2. So với Tổng giá gốc, Tổng chiết khấu dịch vụ, Tổng tiền sau chiết khấu',
  '2. Các tổng khớp nhau', f'{SRS} - Khối đơn cha STT 15, 17 + Dòng đơn hàng STT 15-17. {BA}: Giá gốc dòng đã nhân Số lượng chu kỳ chưa', 'line_sum')
T('Thời gian/Người cập nhật dòng', 'Kiểm tra Thời gian tạo, Thời gian cập nhật, Người cập nhật của dòng đơn hàng',
  '1. Kiểm tra 3 cột cuối bảng Dòng đơn hàng',
  '1. Thời gian định dạng DD/MM/YYYY HH:MM:SS; Thời gian cập nhật đổi khi trạng thái dòng đổi; Người cập nhật VD "System"',
  f'{SRS} - STT 18-20. Mâu thuẫn design dùng định dạng 2026-08-08 17:43:52 - {BA}')
T('Dropdown lọc Trạng thái', 'Kiểm tra danh sách giá trị dropdown Trạng thái của khối Dòng đơn hàng',
  '1. Click dropdown "Trạng thái" phía trên bảng Dòng đơn hàng',
  '1. Hiển thị: Khởi tạo, Chờ cung cấp dịch vụ, Đã hủy, Cung cấp dịch vụ thất bại, Cung cấp dịch vụ 1 phần, Cung cấp dịch vụ thành công; cho phép chọn 1 hoặc nhiều',
  f'{SRS} - Khối dòng đơn hàng - Bộ lọc Trạng thái', 'line_flt_list')
T(None, 'Kiểm tra lọc dòng đơn hàng theo 1 trạng thái có dữ liệu',
  '1. Chọn Trạng thái = Cung cấp dịch vụ thành công',
  '1. Bảng chỉ hiển thị các dòng có trạng thái Cung cấp dịch vụ thành công', f'{SRS} - Bộ lọc Trạng thái', 'line_flt_one')
T(None, 'Kiểm tra lọc dòng đơn hàng theo nhiều trạng thái',
  '1. Chọn Trạng thái = Khởi tạo và Đã hủy',
  '1. Bảng hiển thị các dòng có trạng thái Khởi tạo hoặc Đã hủy', f'{SRS} - Bộ lọc Trạng thái "một hoặc nhiều"')
T(None, 'Kiểm tra lọc dòng đơn hàng theo trạng thái không có dữ liệu',
  '1. Chọn Trạng thái = Cung cấp dịch vụ thất bại (đơn không có dòng nào ở trạng thái này)',
  '1. Bảng hiển thị "Danh sách trống"', f'{SRS} - Bộ lọc Trạng thái "nếu ko có để Danh sách trống"', 'line_flt_empty')
T(None, 'Kiểm tra bỏ chọn trạng thái lọc',
  'ĐK: Đang lọc 1 trạng thái\n1. Bỏ chọn trạng thái',
  '1. Bảng hiển thị lại toàn bộ dòng đơn hàng', f'{BA}: lọc áp dụng ngay khi chọn hay cần nút áp dụng')
T('Cài đặt bảng dòng đơn hàng', 'Kiểm tra mở Cài đặt bảng của khối Dòng đơn hàng',
  '1. Click button Cài đặt bảng trong khối Dòng đơn hàng',
  '1. Hiển thị droplist tất cả các cột của bảng dòng đơn hàng, mặc định tick hết', f'{SRS} - Khối dòng đơn hàng - Cài đặt bảng', 'line_cdb')
T(None, 'Kiểm tra ẩn cột bảng dòng đơn hàng',
  '1. Bỏ tick cột Mã CTKM\n2. Click áp dụng',
  '2. Bảng Dòng đơn hàng ẩn cột Mã CTKM; bảng danh sách đơn hàng ngoài màn danh sách không bị ảnh hưởng', f'{SRS} - "user click áp dụng để hệ thống trả kết quả"')
T(None, 'Kiểm tra click ra ngoài droplist Cài đặt bảng của dòng đơn hàng',
  '1. Bỏ tick 1 cột\n2. Click ra ngoài droplist',
  '2. Đóng droplist, không áp dụng thay đổi', f'Tương tự UC Cài đặt bảng danh sách - {BA}')
T('Cột Gia hạn tự động (design)', 'Kiểm tra cột Gia hạn tự động trên bảng dòng đơn hàng',
  '1. Kiểm tra cột Gia hạn tự động',
  '1. Hiển thị "Không" (phase 1 chưa làm gia hạn)',
  f'Chỉ có trên Figma, SRS không mô tả. {BA}: (1) có giữ cột không; (2) Figma Miniapp có frame "Bắt buộc tự động gia hạn" và màn kết quả ghi "Tự động gia hạn: Có" - trái với "phase 1 mặc định Không"', 'line_renew')

G('Khối Thông tin xuất hóa đơn')
T('Hiển thị khối', 'Kiểm tra không hiển thị khối khi đơn không xuất hoá đơn',
  'ĐK: Đơn hàng khách không chọn xuất hoá đơn\n1. Mở chi tiết đơn hàng',
  '1. Không hiển thị khối Thông tin xuất hóa đơn', f'{SRS} - UC Xem chi tiết - BR2 + "Trường hợp ko xuất hđ→ ko hiển thị khối này"', 'inv_none')
T(None, 'Kiểm tra hiển thị khối khi đơn có xuất hoá đơn',
  'ĐK: Đơn hàng khách chọn xuất hoá đơn\n1. Mở chi tiết đơn hàng',
  '1. Hiển thị khối Thông tin xuất hóa đơn ở cuối trang',
  f'{SRS} - BR2. {BA}: Figma Miniapp phase 1 không có bước nhập thông tin xuất hoá đơn - đơn từ Miniapp có phát sinh khối này không', 'inv_has')
T('Công ty dùng mã số thuế', 'Kiểm tra thông tin hoá đơn - Công ty/Tổ chức dùng mã số thuế',
  'ĐK: Đơn xuất hoá đơn Công ty/Tổ chức, dùng mã số thuế\n1. Kiểm tra khối Thông tin xuất hóa đơn',
  '1. Hiển thị: Loại pháp nhân "Công ty/ Tổ chức", Mã số thuế, Tên công ty, Địa chỉ công ty, Email nhận hóa đơn, Người mua hàng, Trạng thái, Thời gian tạo, Thời gian cập nhật, Người cập nhật; đúng dữ liệu khách nhập',
  f'{SRS} - Khối xuất hoá đơn STT 1-10 + Figma Th1.1 công ty dùng MS thuế - Phân vùng tương đương', 'inv_mst')
T('Công ty dùng mã QHNS', 'Kiểm tra thông tin hoá đơn - Công ty dùng mã đơn vị quan hệ ngân sách',
  'ĐK: Đơn xuất hoá đơn Công ty, dùng mã đơn vị quan hệ ngân sách\n1. Kiểm tra khối Thông tin xuất hóa đơn',
  '1. Hiển thị label và giá trị "Mã đơn vị quan hệ ngân sách" thay cho Mã số thuế, các trường khác như TC trên',
  f'{SRS} - STT 2 "Mã số thuế / Mã đơn vị quan hệ ngân sách". Mâu thuẫn design Th1.1 QHNS vẫn ghi label "Mã số thuế" - {BA}', 'inv_qhns')
T('Cá nhân', 'Kiểm tra thông tin hoá đơn - Cá nhân',
  'ĐK: Đơn xuất hoá đơn loại Cá nhân\n1. Kiểm tra khối Thông tin xuất hóa đơn',
  '1. Hiển thị: Loại pháp nhân "Cá nhân", Email nhận hóa đơn, Người mua hàng, Địa chỉ người mua, Trạng thái, Thời gian tạo, Thời gian cập nhật, Người cập nhật; KHÔNG hiển thị Mã số thuế, Tên công ty',
  f'Figma Th2 cá nhân. {BA}: SRS STT 2, 3 (MST, Tên công ty) đặt Bắt buộc = Có, chưa ghi ẩn với Cá nhân', 'inv_personal')
T('Trạng thái hoá đơn', 'Kiểm tra badge trạng thái hoá đơn',
  'ĐK: Có đơn hoá đơn Chờ xuất hoá đơn, Thành công, Thất bại\n1. Kiểm tra badge Trạng thái ở từng đơn',
  '1. Hiển thị đúng: "Chờ xuất hoá đơn" (xanh dương), "Thành công" (xanh lá), "Thất bại" (đỏ)',
  f'{SRS} - Khối xuất hoá đơn STT 7 + Figma. {BA}: BN 4.2 xuất hoá đơn qua IM có trong phase 1 không', 'inv_status')
T('Hiển thị text dài', 'Kiểm tra hiển thị Tên công ty / Địa chỉ dài',
  'ĐK: Tên công ty, địa chỉ dài > 200 ký tự\n1. Kiểm tra khối hoá đơn',
  '1. Text xuống dòng, hiển thị đầy đủ, không đè sang cột bên cạnh', f'{BA}')

G('Xử lý ngoại lệ')
T('Lỗi hệ thống', 'Kiểm tra mở chi tiết khi hệ thống lỗi / timeout',
  'ĐK: Giả lập API chi tiết đơn hàng trả lỗi\n1. Click Mã đơn hàng',
  '1. Hiển thị thông báo: "Lỗi hệ thống, vui lòng thử lại sau"', f'{SRS} - UC Xem chi tiết - Ngoại lệ')
T('Mất mạng', 'Kiểm tra mở chi tiết khi mất mạng',
  '1. Ngắt mạng\n2. Click Mã đơn hàng',
  '2. Hiển thị thông báo: "Lỗi đường truyền. Vui lòng kiểm tra kết nối của bạn"', f'{SRS} - UC Xem chi tiết - Ngoại lệ')
T('Đơn không tồn tại', 'Kiểm tra truy cập URL chi tiết của đơn không tồn tại / đã xoá mềm',
  '1. Nhập URL chi tiết với ID đơn hàng không tồn tại',
  '1. Không hiển thị dữ liệu, thông báo đơn hàng không tồn tại hoặc điều hướng về danh sách',
  f'{SRS} - Pre-condition "Đơn hàng … phải tồn tại". {BA} hành vi khi không tồn tại')

# =====================================================================
S('UC6: (CMS admin) Chức năng Xuất excel danh sách đơn hàng')
P(PRE)
G('Kiểm tra chức năng')
T('Button Xuất file excel', 'Kiểm tra hiển thị button Xuất file excel',
  '1. Kiểm tra button Xuất file excel',
  '1. Hiển thị button viền, icon bảng tính màu xanh lá + text "Xuất file excel", trạng thái enable', 'Figma', 'xls_btn')
T(None, 'Kiểm tra click button Xuất file excel',
  '1. Click button Xuất file excel',
  '1. Thực hiện chức năng xuất file excel theo UC Xuất excel danh sách đơn hàng',
  f'{SRS} - "UC: xuất excel danh sách đơn hàng" chỉ có tiêu đề, chưa có nội dung → N/A, {BA} (cột, tên file, xuất theo bộ lọc, giới hạn số dòng)', 'xls_click')

# =====================================================================
S('UC7: Đối soát trạng thái đơn hàng phát sinh từ Miniapp gói cước trên CMS')
P('Pre-condition: \nBước 1: Có tài khoản Tammi đăng nhập Miniapp gói cước Tammi; có gói cước Đang kinh doanh, kênh bán = Miniapp gói cước Tammi\n'
  'Bước 2: Admin đăng nhập CMS, mở Danh sách đơn hàng ở tab khác')

G('Luồng thanh toán')
T('Validate trước tạo đơn', 'Kiểm tra không tạo đơn khi giá gói thay đổi lúc bấm thanh toán',
  'ĐK: Admin đổi giá gói X sau khi user đã mở màn Đăng ký gói\n1. Trên Miniapp bấm "Đăng ký chỉ với …" gói X\n2. Kiểm tra Danh sách đơn hàng trên CMS',
  '1. Miniapp hiển thị toast "Giá gói cước đã được cập nhật"\n2. Không phát sinh đơn hàng mới',
  f'SRS Miniapp - UC Tạo đơn hàng và thanh toán bước 3 + Figma. {BA}: câu toast SRS bảng ("Giá gói cước đã được cập nhật") khác sơ đồ PlantUML ("Giá thay đổi, vui lòng tải lại")', 'st_price')
T(None, 'Kiểm tra không tạo đơn khi gói đã ngừng kinh doanh',
  'ĐK: Gói X chuyển Ngừng kinh doanh sau khi user mở màn Đăng ký gói\n1. Trên Miniapp bấm thanh toán gói X\n2. Kiểm tra Danh sách đơn hàng trên CMS',
  '1. Miniapp hiển thị popup "Gói cước đã ngừng kinh doanh. Vui lòng lựa chọn gói cước khác."\n2. Không phát sinh đơn hàng mới',
  'SRS Miniapp - bước 4 + Figma', 'st_stop')
T(None, 'Kiểm tra không tạo đơn khi thuê bao đạt số lượng mua gói tối đa',
  'ĐK: Thuê bao đã đạt số lượng mua tối đa của gói\n1. Trên Miniapp bấm thanh toán\n2. Kiểm tra Danh sách đơn hàng trên CMS',
  '1. Miniapp hiển thị popup "Thuê bao đã đạt số lượng mua gói cước tối đa."\n2. Không phát sinh đơn hàng mới',
  f'Chỉ có trên Figma Miniapp. {BA}: SRS chưa có rule giới hạn số lượng mua gói / thuê bao', 'st_max')
T('Tạo đơn thành công', 'Kiểm tra đơn hàng khi vừa tạo, chưa có kết quả thanh toán',
  '1. Trên Miniapp bấm thanh toán gói hợp lệ, dừng ở màn Thanh toán của CTT (chưa xác nhận)\n2. Kiểm tra đơn mới trên CMS',
  '2. Đơn mới: Trạng thái thanh toán = Chờ thanh toán; Trạng thái đơn hàng = Chờ thanh toán; dòng đơn hàng trạng thái = Khởi tạo; Kênh bán = Miniapp gói cước Tammi',
  'Tổng hợp trạng thái B, C - đơn cha "Chờ thanh toán", đơn con "Khởi tạo" - Sơ đồ chuyển trạng thái', 'st_create')
T(None, 'Kiểm tra lỗi hệ thống khi tạo đơn',
  'ĐK: Giả lập service Đơn hàng lỗi 500/timeout\n1. Trên Miniapp bấm thanh toán\n2. Kiểm tra CMS',
  '1. Miniapp hiển thị popup "Hệ thống bận. Vui lòng thử lại sau"\n2. Không phát sinh đơn hàng', 'SRS Miniapp - bước 7')
T('Thanh toán thành công', 'Kiểm tra đơn hàng sau khi thanh toán thành công',
  '1. Trên Miniapp hoàn tất thanh toán (nhập OTP đúng)\n2. Kiểm tra đơn trên CMS ngay sau đó',
  '2. Trạng thái thanh toán = Thành công; Trạng thái đơn hàng = Chờ cung cấp dịch vụ; dòng đơn hàng = Chờ cung cấp dịch vụ; có Mã đơn hàng CTT, Phương thức thanh toán, Nguồn tiền, Tổng tiền thanh toán, Thời gian thanh toán thành công',
  'Tổng hợp trạng thái B - "Chờ cung cấp dịch vụ" + Trạng thái thanh toán "Thành công" - Sơ đồ chuyển trạng thái', 'st_paid')
T('Thanh toán thất bại', 'Kiểm tra đơn hàng khi thanh toán thất bại',
  '1. Trên Miniapp thanh toán thất bại (VD ví không đủ số dư)\n2. Kiểm tra đơn trên CMS',
  '1. Miniapp hiển thị popup "Thanh toán không thành công"\n2. Trạng thái thanh toán = Thất bại; Trạng thái đơn hàng = Đã hủy; tất cả dòng đơn hàng = Đã hủy; Kết quả cung cấp dịch vụ không có giá trị',
  'Tổng hợp trạng thái B, C - "Đã hủy" + Figma Miniapp - Sơ đồ chuyển trạng thái', 'st_fail')
T(None, 'Kiểm tra đơn hàng khi user huỷ thanh toán tại CTT',
  '1. Tại màn Thanh toán của CTT, user đóng/huỷ giao dịch\n2. Kiểm tra đơn trên CMS',
  '2. Trạng thái thanh toán = Thất bại; Trạng thái đơn hàng = Đã hủy', 'SRS Miniapp - bước 10 "user hủy" + PlantUML', 'st_cancel')
T(None, 'Kiểm tra đơn hàng khi giao dịch CTT hết hạn (timeout)',
  '1. Tại màn Thanh toán của CTT, không thao tác đến khi hết hạn giao dịch\n2. Kiểm tra đơn trên CMS',
  '2. Trạng thái thanh toán = Thất bại; Trạng thái đơn hàng = Đã hủy',
  f'SRS Miniapp - bước 10 "timeout". {BA}: thời gian hết hạn giao dịch', 'st_timeout')
T(None, 'Kiểm tra đơn hàng khi user thoát Miniapp lúc đang thanh toán',
  '1. Màn "Đang thanh toán gói cước", user tắt Miniapp\n2. Kiểm tra đơn trên CMS sau 30 phút',
  '2. Trạng thái đơn được cập nhật theo kết quả CTT trả về (Thành công/Thất bại), không treo vô thời hạn ở Chờ thanh toán',
  f'Figma Miniapp màn "Đang thanh toán gói cước". {BA}: cơ chế đối soát/huỷ đơn treo ở Chờ thanh toán', 'st_pending')

G('Luồng cung cấp dịch vụ')
T('CCDV thành công', 'Kiểm tra đơn hàng khi tất cả quyền lợi kích hoạt thành công',
  'ĐK: Đơn đã thanh toán thành công\n1. Chờ luồng kích hoạt xong, tất cả quyền lợi thành công\n2. Kiểm tra đơn trên CMS',
  '2. Trạng thái đơn hàng = Hoàn thành; dòng đơn hàng = Cung cấp dịch vụ thành công; Kết quả cung cấp dịch vụ = Cung cấp dịch vụ thành công',
  'Tổng hợp trạng thái B "Hoàn thành" + Luồng kích hoạt tổng thể - Sơ đồ chuyển trạng thái', 'st_ccdv_ok')
T('CCDV 1 phần', 'Kiểm tra đơn hàng khi 1 phần quyền lợi kích hoạt thất bại',
  'ĐK: Đơn đã thanh toán thành công, giả lập 1 dịch vụ đích trả lỗi sau 3 lần retry\n1. Kiểm tra đơn trên CMS',
  '1. Trạng thái đơn hàng = Chờ xử lý hoàn tiền; dòng đơn hàng = Cung cấp dịch vụ 1 phần; Kết quả cung cấp dịch vụ = Cung cấp dịch vụ 1 phần',
  f'Tổng hợp trạng thái B "Chờ xử lý hoàn tiền". {BA}: luồng hoàn tiền "TẠM CHƯA LÀM" → đơn giữ mãi ở "Chờ xử lý hoàn tiền"?', 'st_ccdv_part')
T('CCDV thất bại', 'Kiểm tra đơn hàng khi tất cả quyền lợi kích hoạt thất bại',
  'ĐK: Đơn đã thanh toán thành công, giả lập tất cả dịch vụ đích lỗi\n1. Kiểm tra đơn trên CMS',
  '1. Trạng thái đơn hàng = Chờ xử lý hoàn tiền; dòng đơn hàng = Cung cấp dịch vụ thất bại; Kết quả cung cấp dịch vụ = Cung cấp dịch vụ thất bại',
  'Tổng hợp trạng thái B - Sơ đồ chuyển trạng thái', 'st_ccdv_fail')
T(None, 'Kiểm tra retry kích hoạt thành công ở lần thử lại',
  'ĐK: Giả lập dịch vụ đích lỗi lần 1, thành công lần 2\n1. Kiểm tra đơn trên CMS',
  '1. Đơn Hoàn thành, dòng đơn hàng Cung cấp dịch vụ thành công (lần lỗi đầu không làm đơn chuyển sang thất bại)',
  'Luồng kích hoạt tổng thể - "Retry tối đa 3 lần" - Kỹ thuật: Giá trị biên số lần retry', 'st_retry')
T('Chuyển trạng thái không hợp lệ', 'Kiểm tra đơn đã hủy không chuyển sang trạng thái khác',
  'ĐK: Đơn Đã hủy (thanh toán thất bại)\n1. Gửi lại callback thanh toán thành công trùng miniapprequestid (giả lập)\n2. Kiểm tra đơn trên CMS',
  '2. Đơn giữ trạng thái Đã hủy hoặc xử lý theo quy định đối soát; không kích hoạt gói',
  f'Sơ đồ chuyển trạng thái - phép chuyển không hợp lệ. NFR 1.3 chống double-spending. {BA}', 'st_invalid')
T(None, 'Kiểm tra callback thanh toán thành công gửi trùng 2 lần',
  'ĐK: Đơn đã thanh toán thành công\n1. Giả lập CTT gửi lại callback thành công lần 2\n2. Kiểm tra đơn trên CMS',
  '2. Đơn không bị tạo/kích hoạt trùng, Thời gian thanh toán thành công giữ nguyên lần đầu',
  'NFR 1.3 + NFR 2.3 retry webhook - Sơ đồ chuyển trạng thái (tranh chấp)', 'st_dup')
T('Hiển thị trên CMS', 'Kiểm tra thông tin đơn trên CMS khớp màn Lịch sử thanh toán của Miniapp',
  'ĐK: Đơn đã thanh toán thành công\n1. Trên Miniapp mở Gói cước của tôi > Lịch sử thanh toán > chi tiết giao dịch\n2. Đối chiếu với chi tiết đơn trên CMS',
  '2. Trạng thái, Phương thức thanh toán, Số tiền, Tên gói, Chu kỳ, Thời gian khớp nhau giữa Miniapp và CMS',
  f'Figma Miniapp Lịch sử giao dịch. {BA}: Miniapp có "Loại giao dịch" (Đăng ký/Gia hạn) nhưng CMS không có cột này', 'st_match')

# ---------------------------------------------------------------------
# Đánh số TC theo thứ tự (khớp công thức ID của sheet: TC-01, TC-02…) và bỏ khoá
_ID = {}
ROWS = []
_n = 0
for item in _RAW:
    if item[0] == 'T':
        _n += 1
        if item[7]:
            _ID[item[7]] = f'TC-{_n:02d}'
        ROWS.append(item[:7])
    else:
        ROWS.append(item)


def _ids(*keys):
    return ', '.join(_ID[k] for k in keys)


TECHNIQUES = [
    {
        'title': '1. SƠ ĐỒ CHUYỂN TRẠNG THÁI - Đơn hàng cha (Trạng thái đơn hàng × Trạng thái thanh toán)',
        'header': ['Trạng thái hiện tại', 'Sự kiện', 'Trạng thái đơn hàng kế tiếp', 'Trạng thái thanh toán', 'Dòng đơn hàng', 'TC'],
        'rows': [
            ['(chưa có)', 'Kênh bán tạo đơn thành công', 'Chờ thanh toán', 'Chờ thanh toán', 'Khởi tạo', _ids('st_create')],
            ['(chưa có)', 'Validate thất bại (giá đổi / ngừng KD / đạt tối đa)', 'Không tạo đơn', '-', '-', _ids('st_price', 'st_stop', 'st_max')],
            ['Chờ thanh toán', 'CTT báo thanh toán thành công', 'Chờ cung cấp dịch vụ', 'Thành công', 'Chờ cung cấp dịch vụ', _ids('st_paid')],
            ['Chờ thanh toán', 'CTT báo thất bại / user huỷ / timeout', 'Đã hủy', 'Thất bại', 'Đã hủy', _ids('st_fail', 'st_cancel', 'st_timeout')],
            ['Chờ thanh toán', 'User thoát app khi đang thanh toán', 'Theo kết quả CTT (BA confirm)', '?', '?', _ids('st_pending')],
            ['Chờ cung cấp dịch vụ', 'Tất cả quyền lợi thành công', 'Hoàn thành', 'Thành công', 'CCDV thành công', _ids('st_ccdv_ok', 'st_retry')],
            ['Chờ cung cấp dịch vụ', 'Có quyền lợi thất bại (1 phần)', 'Chờ xử lý hoàn tiền', 'Thành công', 'CCDV 1 phần', _ids('st_ccdv_part')],
            ['Chờ cung cấp dịch vụ', 'Tất cả quyền lợi thất bại', 'Chờ xử lý hoàn tiền', 'Thành công', 'CCDV thất bại', _ids('st_ccdv_fail')],
            ['Chờ xử lý hoàn tiền', 'Hoàn tiền thành công (phase 1 TẠM CHƯA LÀM)', 'Hoàn thành', 'Đã hoàn tiền', '-', 'BA confirm - chưa viết TC'],
            ['Đã hủy', 'Callback thành công đến muộn (không hợp lệ)', 'Giữ Đã hủy (BA confirm)', 'Thất bại', 'Đã hủy', _ids('st_invalid')],
            ['Chờ cung cấp dịch vụ', 'Callback thành công gửi trùng (tranh chấp)', 'Không đổi, không kích hoạt trùng', 'Thành công', '-', _ids('st_dup')],
        ],
    },
    {
        'title': '2. BẢNG QUYẾT ĐỊNH - Kết quả cung cấp dịch vụ (tổng hợp từ trạng thái quyền lợi)',
        'header': ['Điều kiện', 'R1', 'R2', 'R3', 'R4'],
        'rows': [
            ['Đơn đã thanh toán thành công', 'Y', 'Y', 'Y', 'N'],
            ['Tất cả quyền lợi Thành công', 'Y', 'N', 'N', '-'],
            ['Có ít nhất 1 quyền lợi Thành công', 'Y', 'Y', 'N', '-'],
            ['=> Kết quả CCDV', 'CCDV thành công', 'CCDV 1 phần', 'CCDV thất bại', 'Trống (BA confirm)'],
            ['=> Trạng thái đơn hàng', 'Hoàn thành', 'Chờ xử lý hoàn tiền', 'Chờ xử lý hoàn tiền', 'Chờ thanh toán / Đã hủy'],
            ['TC', _ids('ccdv_ok', 'st_ccdv_ok'), _ids('ccdv_part', 'st_ccdv_part'), _ids('ccdv_fail', 'st_ccdv_fail'), _ids('ccdv_none')],
        ],
    },
    {
        'title': '3. BẢNG QUYẾT ĐỊNH - Cài đặt bảng',
        'header': ['Điều kiện / Hành động', 'R1', 'R2', 'R3', 'R4', 'R5', 'R6'],
        'rows': [
            ['Số cột đang tick', 'Tất cả', '0', '1', 'n (1<n<tất cả)', 'Tất cả-1', 'bất kỳ'],
            ['Hành động', 'Bỏ tick "Tất cả"', 'Tick "Tất cả"', '-', 'Xác nhận', 'Tick cột còn lại', 'Click outside'],
            ['=> Checkbox "Tất cả"', 'Bỏ tick', 'Tick', 'Bỏ tick', 'Bỏ tick', 'Tự tick', 'Không đổi'],
            ['=> Nút xác nhận', 'Disable', 'Enable', 'Enable', 'Enable', 'Enable', '-'],
            ['=> Bảng', 'Không đổi', 'Không đổi', 'Không đổi', 'Ẩn cột bỏ tick', 'Không đổi', 'Không lưu'],
            ['TC', _ids('cdb_all_off', 'cdb_btn_0'), _ids('cdb_all_on'), _ids('cdb_btn_1'), _ids('cdb_hide1', 'cdb_hideN'), _ids('cdb_partial'), _ids('cdb_outside')],
        ],
    },
    {
        'title': '4. PHÂN TÍCH GIÁ TRỊ BIÊN',
        'header': ['Ràng buộc', 'Dưới biên', 'Tại biên', 'Trên biên', 'TC'],
        'rows': [
            ['Ô tìm kiếm - bắt đầu tìm từ ký tự thứ 3', '1 ký tự, 2 ký tự (không tìm)', '3 ký tự (tìm)', '-', _ids('srch_1', 'srch_2', 'srch_3', 'srch_id_short')],
            ['Ô tìm kiếm - tối đa 50 ký tự', '49', '50', '51 (bị chặn)', _ids('srch_49', 'srch_50', 'srch_51')],
            ['Bộ lọc Mã đơn hàng CTT Tammi - tối đa 50', '-', '50', '51 (bị chặn)', _ids('flt_ctt_50', 'flt_ctt_51')],
            ['Bộ lọc Thuê bao đăng kí - tối đa 50', '-', '50', '51 (bị chặn)', _ids('flt_tbdk_50', 'flt_tbdk_51')],
            ['Bộ lọc Thuê bao thụ hưởng - tối đa 50', '-', '50', '51 (bị chặn)', _ids('flt_tbth_50', 'flt_tbth_51')],
            ['Thời gian tạo: từ 0h ngày bắt đầu', '23:59:59 ngày trước (loại)', '00:00:00 ngày bắt đầu (lấy)', '-', _ids('flt_tgt_before', 'flt_tgt_start')],
            ['Thời gian tạo: đến 23:59:59 ngày kết thúc', '-', '23:59:59 ngày kết thúc (lấy)', '00:00:00 ngày sau (loại)', _ids('flt_tgt_end', 'flt_tgt_after')],
            ['Thời gian cập nhật: từ 0h ngày bắt đầu', '23:59:59 ngày trước (loại)', '00:00:00 ngày bắt đầu (lấy)', '-', _ids('flt_tgcn_before', 'flt_tgcn_start')],
            ['Thời gian cập nhật: đến 23:59:59 ngày kết thúc', '-', '23:59:59 ngày kết thúc (lấy)', '00:00:00 ngày sau (loại)', _ids('flt_tgcn_end', 'flt_tgcn_after')],
            ['Khoảng ngày', 'Kết thúc < bắt đầu', 'Bắt đầu = kết thúc', '-', _ids('flt_reverse', 'flt_sameday')],
            ['Phân trang (25 dòng/trang theo SRS)', '-', '25 bản ghi = 1 trang', '26 bản ghi = 2 trang', _ids('page_eq', 'page_over')],
            ['Cài đặt bảng - số cột được tick', '0 (xác nhận disable)', '1 (enable)', '-', _ids('cdb_btn_0', 'cdb_btn_1')],
            ['Retry kích hoạt quyền lợi - tối đa 3 lần', '-', 'Thành công ở lần retry', 'Hết 3 lần vẫn lỗi → thất bại', _ids('st_retry', 'st_ccdv_part')],
        ],
    },
    {
        'title': '5. PHÂN VÙNG TƯƠNG ĐƯƠNG',
        'header': ['Đầu vào', 'Lớp hợp lệ', 'Lớp không hợp lệ / đặc biệt', 'TC'],
        'rows': [
            ['Từ khoá tìm kiếm', 'Đủ mã đơn hàng · 1 phần mã · ID · khác hoa/thường · có dấu', 'Không tồn tại · toàn khoảng trắng · khoảng trắng giữa · script/SQL',
             _ids('srch_madh', 'srch_partial', 'srch_id', 'srch_case', 'srch_none', 'srch_trim')],
            ['Loại thuê bao thụ hưởng', 'Tk Tammi', 'Tk OA (hiển thị SĐT hay OA ID - BA confirm)', _ids('col_tb_tammi', 'col_tb_oa')],
            ['CTKM dịch vụ', 'Giảm % · giảm số tiền', 'Không có CTKM (0đ / trống)', _ids('line_km_pct', 'line_km_vnd', 'line_km_none', 'col_ck_has', 'col_ck_none')],
            ['Voucher CTT', 'Có voucher (Tổng thanh toán < Tổng sau CK)', 'Không voucher (bằng nhau) · chưa thanh toán', _ids('col_tt_voucher', 'col_tt_unpaid')],
            ['Mã đơn hàng CTT', 'Có mã', 'Chưa có mã', _ids('col_ctt_has', 'col_ctt_empty')],
            ['Thông tin xuất hoá đơn', 'Công ty - MST · Công ty - mã QHNS · Cá nhân', 'Không xuất hoá đơn (ẩn khối)', _ids('inv_mst', 'inv_qhns', 'inv_personal', 'inv_none')],
            ['Dropdown lọc (mỗi trường)', 'Chọn 1 giá trị · chọn nhiều giá trị', 'Giá trị không có dữ liệu', _ids('flt_tttt_one', 'flt_tttt_multi', 'flt_empty')],
            ['Quyền tài khoản', 'Có quyền quản lý đơn hàng', 'Không có quyền · bị thu hồi quyền', _ids('perm_ok', 'perm_no', 'perm_detail')],
        ],
    },
    {
        'title': '6. KẾT HỢP ĐIỀU KIỆN LỌC (Pairwise rút gọn + tất cả + mâu thuẫn)',
        'header': ['Cặp điều kiện', 'TC'],
        'rows': [
            ['Trạng thái thanh toán × Kênh bán', _ids('cmb_2a')],
            ['Trạng thái đơn hàng × Kết quả CCDV', _ids('cmb_2b')],
            ['Thuê bao đăng kí (ô nhập) × Trạng thái thanh toán', _ids('cmb_2c')],
            ['Phương thức thanh toán × Thời gian tạo', _ids('cmb_2d')],
            ['Thời gian tạo × Thời gian cập nhật', _ids('cmb_2e')],
            ['Tất cả 11 điều kiện', _ids('cmb_all')],
            ['Kết hợp mâu thuẫn theo sơ đồ trạng thái (Thất bại × Hoàn thành)', _ids('cmb_conflict')],
            ['Từ khoá tìm kiếm × Bộ lọc', _ids('srch_filter_none', 'srch_filter_ok')],
        ],
    },
]
