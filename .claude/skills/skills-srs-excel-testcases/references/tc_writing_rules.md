# Quy tắc viết Test Case theo file mẫu dạng "KỊCH BẢN KIỂM THỬ" (Excel/Google Sheet)

> Rút ra từ file TC thực tế của dự án (sheet `QLĐH_Hủy đơn hàng`, `QLDH_Chi tiết đơn hàng`, `QLĐH_Đánh giá đơn hàng`…).
> **Luôn chạy `inspect_tc_template.py` trên file mẫu của dự án đang làm** — nếu khác các quy tắc dưới đây thì file mẫu thắng.

---

## 1. Cấu trúc sheet

| Vùng | Nội dung |
|---|---|
| Dòng 1 | Tiêu đề đơn vị + `KỊCH BẢN KIỂM THỬ` (merge) |
| Dòng 3–9 (cột D→E) | `Tên màn hình/Tên chức năng` · `Mã testcase` (VD `TC`) · `Số testcase đạt (Pass)` · `không đạt (Fail)` · `chưa test` · `Tổng số testcase` · `Link tài liệu` |
| Dòng 11–12 (merge dọc) | Tiêu đề cột: **ID · Chức năng · Mục đích · Các bước thực hiện kiểm thử · Kết quả mong muốn · Dữ liệu kiểm thử** · Người tạo · Ngày tạo · Log cập nhật · Ngày test · Log test lại · Người test · cột thiết bị (Tablet, Z Fold 4, Ipad, IOS, Samsung) · **Trạng thái** · **Ghi chú** |
| Dòng section | Tên nhóm màn hình, nền xanh, merge A:C |
| Dòng Pre-condition | `Pre-condition: \nBước 1: … \nBước 2: …`, merge A:M |
| Dòng TC | Từ dòng này trở xuống |

**Công thức có sẵn trong file mẫu — phải giữ nguyên, KHÔNG ghi số tĩnh:**

- ID: `=$E$4&"-"&TEXT(COUNTA($E$15:E15),"00")` → tự đánh `TC-01, TC-02…` theo số ô *Kết quả mong muốn* có dữ liệu. Dòng section/Pre-condition không có cột E nên không bị đếm
- Thống kê: `Pass = COUNTIF(<cột Trạng thái>,"Pass")`, `Fail = COUNTIF(…,"Fail")`, `Tổng = COUNTA(<cột Kết quả mong muốn>)`, `Chưa test = Tổng − Pass − Fail`
- Cột Trạng thái: dropdown `Pass, Fail, N/A`. **Để trống** khi mới viết

`build_tc_excel.py` tự làm đúng những điều này.

## 2. Văn phong từng cột

| Cột | Quy tắc | Ví dụ |
|---|---|---|
| **Chức năng** | Tên vùng/thành phần UI, chỉ ghi ở TC đầu nhóm (ô được merge dọc cả nhóm) | `Button Huỷ yêu cầu` |
| **Mục đích** | Bắt đầu bằng `Check …` hoặc `Kiểm tra …`, 1 câu, nêu **điều kiện phân biệt** giữa các TC | `Check ẩn button Huỷ yêu cầu sau khi ĐVVC đã lấy hàng` |
| **Các bước** | Điều kiện riêng đặt dòng đầu: `ĐK: …` (hoặc `TH: …` cho trường hợp dữ liệu). Bước đánh số `1. `, `2. ` — mỗi bước 1 hành động | `ĐK: Đã thêm đủ 6 ảnh\n1. Click ô Hình ảnh\n2. Chọn thêm 1 ảnh` |
| **Kết quả mong muốn** | Quan sát được, đo được. Liệt kê bằng `+ `. Chép **nguyên văn** text/toast/popup từ SRS/design trong dấu `"…"` | `Hiển thị toast message: "Yêu cầu … thành công…"` |
| **Dữ liệu kiểm thử** | Giá trị cụ thể dùng để chạy (số tiền, ngày, dung lượng, chuỗi ký tự) | `Ảnh 21MB` · `Ngày giao: 20/09/2026` |
| **Ghi chú** | Mục SRS truy vết · kỹ thuật thiết kế · điểm cần BA confirm · lý do N/A | `Mục 1.3.4 STT 4 - Kỹ thuật: Bảng quyết định` |

Không lặp lại các bước đã có trong Pre-condition.

## 3. 4 TC giao diện bắt buộc đầu mỗi màn hình

Copy nguyên văn từ file mẫu, chỉ đổi tên màn:

1. `Kiểm tra giao diện <màn>` — title + hiển thị đủ label theo design (liệt kê các label)
2. `Kiểm tra hiển thị giao diện <màn>` — bố cục / font chữ, cỡ chữ, màu chữ / chính tả (đoạn kết quả chuẩn của file mẫu)
3. `Kiểm tra dữ liệu khi màn hình để chế độ sáng`
4. `Kiểm tra dữ liệu khi màn hình để chế độ tối`

## 4. Checklist phủ theo loại thành phần (đọc từng dòng bảng "STT | Label | Kiểu | Bắt buộc | Mô tả")

| Kiểu trong SRS | TC tối thiểu | Kỹ thuật |
|---|---|---|
| **Button** | hiển thị/ẩn theo điều kiện · enable/disable · click → điều hướng/kết quả · click liên tiếp (chống gửi trùng) | Bảng quyết định |
| **Label** hiển thị dữ liệu | có dữ liệu · rỗng · định dạng (tiền `125.000 đ`, ngày `DD/MM/YYYY`) · text dài cắt `…` · lấy đúng nguồn API | Phân vùng tương đương |
| **Textbox** | placeholder · bộ đếm · max−1 / max / max+1 · paste vượt max · ký tự đặc biệt · xuống dòng · emoji/tiếng Việt · trim đầu/cuối · chỉ khoảng trắng · để trống (bắt buộc/không) | Giá trị biên + Phân vùng |
| **Upload ảnh/video** | mở thư viện/camera · 1 file · đủ số tối đa · vượt số tối đa · dung lượng đúng ngưỡng / vượt ngưỡng · sai định dạng · xoá · huỷ chọn · từ chối quyền · mất mạng khi tải | Giá trị biên |
| **Bottom sheet / popup** | mở · nội dung đúng design · chọn · Xác nhận · đóng không chọn (vuốt, click ngoài) · nút Huỷ/Đồng ý | Chuyển trạng thái UI |
| **Radio / chọn 1** | mặc định · chọn khác · chỉ chọn được 1 | Phân vùng |
| **Icon copy** | toast `Sao chép thành công` · paste ra đúng giá trị | — |
| **Progress bar / trạng thái** | mỗi trạng thái 1 TC · mốc chưa đạt hiển thị `---` · format ngày · cập nhật khi trạng thái đổi | Sơ đồ chuyển trạng thái |
| **Quy tắc thời gian / số lượt** | dưới biên · tại biên · trên biên | Giá trị biên |
| **Link ngoài (Zalo OA, PDF)** | mở đúng đích · chưa cài app · mất mạng | — |

Cuối mỗi màn: nhóm **Kiểm thử kỹ thuật** — đối chiếu dữ liệu API · API lỗi 500 · mất mạng · thời gian phản hồi · xoay màn hình · chuyển app ra nền · màn hình nhỏ · tablet · cỡ chữ hệ thống lớn.

## 5. Kỹ thuật thiết kế — khi nào dùng, ghi ở đâu

| Kỹ thuật | Dùng khi SRS có | Bằng chứng trong file |
|---|---|---|
| **Phân vùng tương đương** | Nhiều loại đầu vào cùng hành vi (có/không voucher, thanh toán QR/Zalopay, đăng ký email/SĐT) | Ghi chú `Kỹ thuật: Phân vùng tương đương` |
| **Phân tích giá trị biên** | Giới hạn số: ký tự, dung lượng, số file, số ngày, số giờ, số lượt | Bảng BVA ở sheet `Kỹ thuật thiết kế TC` + Ghi chú |
| **Bảng quyết định** | Thành phần hiện/ẩn/enable theo **tổ hợp** điều kiện (trạng thái × vai trò × cờ) | Bảng quyết định ở sheet phụ, mỗi ô → ≥ 1 TC |
| **Sơ đồ chuyển trạng thái** | Đối tượng có vòng đời (đơn hàng, yêu cầu, thanh toán) | Bảng chuyển trạng thái ở sheet phụ, mỗi phép chuyển hợp lệ → 1 TC, thêm TC cho phép chuyển **không** hợp lệ và tranh chấp (2 bên đổi trạng thái cùng lúc) |

Sheet phụ `Kỹ thuật thiết kế TC` sinh từ biến `TECHNIQUES` trong file dữ liệu — giúp reviewer thấy TC nào sinh từ ô nào.

## 6. Xử lý khi tài liệu không rõ / mâu thuẫn

| Tình huống | Làm gì |
|---|---|
| SRS mâu thuẫn design (VD SRS `Bắt buộc = No`, design có `*`) | Viết TC theo **design** (thứ người dùng thấy), ghi Ghi chú `Mâu thuẫn SRS (…) và design (…) - cần BA confirm`. Báo lại trong tóm tắt |
| SRS mâu thuẫn chính nó (2 mục nói khác nhau) | Ghi cả 2 mục vào Ghi chú, BA confirm |
| Tính năng ghi "chưa làm phase này" | Vẫn viết TC, Ghi chú lý do → tester chấm `N/A` |
| SRS không liệt kê giá trị (danh sách lý do, định dạng file) | Kết quả ghi `theo design`, Ghi chú `Đối chiếu … với Figma/BA trước khi test`. **Không bịa danh sách** |
| `Tương tự STT x mục y` | Mở mục y đọc rồi mới viết — không để nguyên "tương tự" trong kết quả mong muốn |
| Chưa biết tên API/trường | Ghi `Bổ sung tên API và tên trường sau khi dev cung cấp` |
