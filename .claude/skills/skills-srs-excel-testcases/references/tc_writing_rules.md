# Quy tắc viết Test Case theo file mẫu dạng "KỊCH BẢN KIỂM THỬ" (Excel/Google Sheet)

> Rút ra từ file TC thực tế của dự án:
> - **Format A** — app mobile Buyer: sheet `QLĐH_Hủy đơn hàng`, `QLDH_Chi tiết đơn hàng`, `QLĐH_Đánh giá đơn hàng`…
> - **Format B** — web CMS / Seller F2C: sheet **`Quanlykho`** (Quản lý địa chỉ kho, 314 TC) của file "TC_F2C CMS", cùng họ với `Quanlynhaban`, `Quản lý tài khoản`, `Danhsachdonhang`…
>
> **Luôn chạy `inspect_tc_template.py` trên file mẫu của dự án đang làm** — nếu khác các quy tắc dưới đây thì file mẫu thắng.

---

## 1. Cấu trúc sheet — nhận diện format trước khi viết

| | **Format A** (mobile, QLĐH) | **Format B** (web CMS, `Quanlykho`) |
|---|---|---|
| Nhận biết nhanh | Khối header ở cột **D→E**, có cột thiết bị (Tablet, Z Fold 4, Ipad, IOS, Samsung) | Khối header ở cột **A (nhãn, merge A:B) → C (giá trị)**, 13 cột A→M |
| Khối header | `Tên màn hình/Tên chức năng` · `Mã testcase` · `Số testcase đạt (Pass)` · `không đạt (Fail)` · `chưa test` · `Tổng số testcase` · `Link tài liệu` | `Chức năng` (C2) · `Link TL + task` (C3) · `ID` (C4 = mã, VD `TC`, `DSDH`) · `Người tạo` (C5) · `Số lượng Testcase` (C6) · `Pass` (C7) · `Fail` (C8) · `N/A` (C9) — một số sheet thêm `Số testcase pending` |
| Tiêu đề cột (merge 2 dòng) | ID · Chức năng · Mục đích · Các bước thực hiện kiểm thử · Kết quả mong muốn · Dữ liệu kiểm thử · Người tạo TCs · Ngày tạo TCs · Log cập nhật · Ngày test · Log test lại · Log người test · cột thiết bị · **Trạng thái** · **Ghi chú** | ID · Chức năng · Mục đích · Các bước thực hiện kiểm thử · Kết quả mong muốn · Dữ liệu kiểm thử · **Ngày tạo TCs** · Người thực hiện · Ngày thực hiện · Log ngày Test lại · **Trạng thái** · Test sau Upcode · **Ghi chú** |
| Cấp section | 1 cấp: tên nhóm màn hình (nền xanh, merge A:C) | **3 cấp**: `UCn: Chức năng …` (nền xanh `4A86E8`, merge A:C) → **nhóm con** (merge A:K, không nền: `Kiểm tra gui UI/UX` · `Kiểm tra validate` · `Kiểm tra chức năng`, hoặc tên vùng màn hình như `Vùng thông tin Tìm kiếm`) → Pre-condition (merge A:M) |
| Công thức ID | `=$E$4&"-"&TEXT(COUNTA($E$15:E15),"00")` — đếm cột **Kết quả** | `=$C$4&"-"&TEXT(COUNTA($D$13:D14),"00")` — đếm cột **Các bước** |
| Dropdown Trạng thái | `Pass, Fail, N/A` | `Pass, Fail, Pending, N/A` |
| Thống kê | Pass/Fail = `COUNTIF`, Tổng = `COUNTA`, Chưa test = Tổng − Pass − Fail | Số lượng = đếm TC, Pass/Fail/N/A = `COUNTIF` cột Trạng thái |
| Merge dọc | Cột Chức năng theo nhóm | Cột Chức năng theo nhóm **và** cột Mục đích khi nhiều TC chung 1 mục đích, khác bước/dữ liệu |

**Quy tắc chung cả hai format — phải giữ nguyên, KHÔNG ghi số tĩnh:**

- ID là **công thức đếm** → tự đánh `TC-01, TC-02…`; dòng section/nhóm con/Pre-condition không có giá trị ở cột được đếm nên không bị tính. Chèn TC vào giữa → ID phía sau **dịch đi**
- Thống kê là công thức trỏ vào cột Trạng thái. Cột Trạng thái **để trống** khi mới viết
- Format B: sheet `Overview` của file gốc lấy `C2` (tên), `C6` (tổng), `C7`/`C8`/`C9` của từng sheet → **không đổi vị trí khối header**, nếu không Overview gãy khi dán sheet mới vào

`build_tc_excel.py` tự nhận format từ sheet khuôn (đọc công thức ID, dropdown, vùng merge) và làm đúng những điều này.

## 2. Văn phong từng cột

| Cột | Quy tắc | Ví dụ |
|---|---|---|
| **Chức năng** | Tên field / vùng / thành phần UI, chỉ ghi ở TC đầu nhóm (ô merge dọc cả nhóm). Format B hay đặt `Kiểm tra trường <Tên field>`, `Button <tên>`, `Icon mở rộng - <action>`, `Thêm mới thành công` / `Thêm mới thất bại` | `Kiểm tra trường Họ và tên` |
| **Mục đích** | Bắt đầu bằng `Check …` hoặc `Kiểm tra …`, 1 câu, nêu **điều kiện phân biệt**. Điều kiện dữ liệu chung có thể đặt dòng đầu `Pre: …` / `Pre-condition: …` rồi xuống dòng | `Pre: danh sách địa chỉ kho trống\nKiểm tra hiển thị màn hình danh sách địa chỉ kho` |
| **Các bước** | Điều kiện riêng dòng đầu: `ĐK: …`, `TH: …` (trường hợp dữ liệu) hoặc `Pre-condition: …`. Bước đánh số `1. `, `2. ` — mỗi bước 1 hành động; nối thao tác liền mạch bằng `>` (`Click dropdown > chọn Hà Nội > Nhấn Áp dụng`) | `ĐK: Dữ liệu gồm 50 bản ghi, mặc định 10 bản ghi/trang\n1. Thực hiện tìm kiếm có 20 bản ghi thoả mãn\n2. Click trang 2` |
| **Kết quả mong muốn** | Quan sát được, đo được. **Ghi số bước đang kiểm** ở đầu khi kết quả thuộc bước cuối (`4. \n- …`); liệt kê bằng `- ` hoặc `+ `. Chép **nguyên văn** text/toast/popup/lỗi inline trong `"…"` | `4. \n- Cho phép tìm kiếm gần đúng theo Số điện thoại đã nhập\n- Hiển thị tất cả địa chỉ kho có Số điện thoại chứa "09"` |
| **Dữ liệu kiểm thử** | Giá trị cụ thể dùng để chạy (từ khoá, số ký tự, số bản ghi, ngày, dung lượng) | `09` · `Chuỗi 51 ký tự` · `Ảnh 21MB` |
| **Ngày tạo TCs** (B) | `DD/MM/YYYY`; TC bổ sung mang ngày bổ sung riêng | `07/10/2026` |
| **Ghi chú** | Mục SRS truy vết · kỹ thuật thiết kế · điểm cần BA confirm · lý do N/A · tiền tố `[Bổ sung dd/mm/yyyy]` khi chèn vào bộ cũ | `Mục 2.1 STT 4 - Kỹ thuật: Giá trị biên` |

- Không lặp lại các bước đã có trong Pre-condition. (File mẫu Format B có chỗ vẫn lặp `1. User đăng nhập vào CMS\n2. Click menu …` — chấp nhận khi TC cần đi lại từ đầu, nhưng **không** làm mặc định.)
- **Một mục đích – nhiều biến thể dữ liệu** (Format B): giữ 1 ô Mục đích, mỗi biến thể là 1 TC riêng có ID riêng, ô Mục đích để `None` để merge dọc. VD `Kiểm tra tìm kiếm gần đúng theo Số điện thoại` → TC với `09` và TC với `0987888787`.

## 3. TC giao diện bắt buộc đầu mỗi màn hình

### 3a. Format A — màn mobile (4 TC, copy nguyên văn từ file mẫu, chỉ đổi tên màn)

1. `Kiểm tra giao diện <màn>` — title + hiển thị đủ label theo design (liệt kê các label)
2. `Kiểm tra hiển thị giao diện <màn>` — bố cục / font chữ, cỡ chữ, màu chữ / chính tả
3. `Kiểm tra dữ liệu khi màn hình để chế độ sáng`
4. `Kiểm tra dữ liệu khi màn hình để chế độ tối`

### 3b. Format B — màn web CMS (nhóm `Kiểm tra UI`, 5 TC)

| Mục đích | Bước | Kết quả mong muốn (nguyên văn file mẫu) |
|---|---|---|
| Kiểm tra hiển thị giao diện mặc định | Kiểm tra hiển thị | Hiển thị màn hình giống design (liệt kê vùng/label chính) |
| Kiểm tra tổng thể giao diện màn hình | Kiểm tra về bố cục, font chữ, chính tả, màu chữ | `1. Các label, có độ dài, rộng và khoảng cách bằng nhau, không xô lệch` · `2. Các label sử dụng cùng 1 loại font, cỡ chữ, căn lề` · `3. Kiểm tra tất cả lỗi về chính tả, cấu trúc câu, ngữ pháp trên màn hình` · `4. Form được bố trí hợp lý và dễ sử dụng` |
| Kiểm tra thứ tự di chuyển trỏ trên màn hình khi nhấn phím Tab | Nhấn Tab liên tục | Con trỏ di chuyển lần lượt theo thứ tự: Từ trái qua phải, từ trên xuống dưới |
| Kiểm tra thứ tự con trỏ di chuyển ngược lại khi nhấn Shift-Tab | Nhấn phím Shift-Tab liên tục | Con trỏ di chuyển ngược lại theo thứ tự: từ dưới lên trên, từ phải qua trái |
| Kiểm tra giao diện khi thu nhỏ, phóng to | Nhấn Ctrl - / Ctrl + | Màn hình thu nhỏ, phóng to tương ứng và không bị vỡ giao diện |

**Popup / form (Thêm mới, Chỉnh sửa, Chi tiết):** thêm 4 TC — `Kiểm tra tiêu đề` (text tiêu đề nguyên văn) · `Kiểm tra icon X` (vị trí + click → đóng popup, quay lại danh sách) · `Kiểm tra khi click chuột ra ngoài` (đóng / không đóng theo design) · `Kiểm tra button` (text các button + trạng thái enable).

Màn danh sách: thêm 2 TC "có dữ liệu" / "chưa có dữ liệu" (Mục đích dạng `Pre: …\nKiểm tra hiển thị màn hình …`).

## 4. Checklist phủ theo loại thành phần (đọc từng dòng bảng "STT | Label | Kiểu | Bắt buộc | Mô tả")

### 4a. Thành phần chung / mobile

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

Cuối mỗi màn mobile: nhóm **Kiểm thử kỹ thuật** — đối chiếu dữ liệu API · API lỗi 500 · mất mạng · thời gian phản hồi · xoay màn hình · chuyển app ra nền · màn hình nhỏ · tablet · cỡ chữ hệ thống lớn.

### 4b. Web CMS — rút từ sheet `Quanlykho` (màn CRUD: Danh sách + Tìm kiếm → Thêm mới → Chỉnh sửa → Xem chi tiết → Xoá)

Mỗi chức năng là 1 `UCn`. Trong UC Thêm mới / Chỉnh sửa tách 3 nhóm con theo thứ tự: **`Kiểm tra gui UI/UX` → `Kiểm tra validate` (từng field) → `Kiểm tra chức năng` (Lưu thành công / thất bại)**.

| Thành phần | TC tối thiểu | Kỹ thuật |
|---|---|---|
| **Ô tìm kiếm dạng text** (bộ lọc) | giá trị mặc định + placeholder · từ khoá không tồn tại → danh sách trống + `"Không có dữ liệu"` · tìm **gần đúng** (1 phần) · tìm **chính xác** (đủ chuỗi) · nhập **toàn khoảng trắng** → hiển thị toàn bộ · khoảng trắng **giữa** từ khoá · chuỗi rất dài → không vỡ layout · để trống → hiển thị toàn bộ · copy ra / paste vào · ràng buộc riêng field (SĐT: chỉ số, chặn chữ, tối đa N ký tự, đầu số ngoài nhà mạng) | Phân vùng tương đương + Giá trị biên |
| **Dropdown lọc** | mặc định trống + placeholder · danh sách đủ, không thiếu/lặp · gõ tìm gần đúng trong dropdown · chọn giá trị **có** dữ liệu / **không có** dữ liệu · không chọn + Áp dụng → tất cả · Áp dụng 2 lần → kết quả không đổi · icon X → xoá lựa chọn, kết quả chưa đổi · icon X rồi Áp dụng → tất cả · **dropdown con khi chưa chọn cha** (`Không có dữ liệu`) · dropdown con lọc theo cha | Phân vùng tương đương |
| **Kết hợp điều kiện lọc** | từng **cặp** điều kiện · **tất cả** điều kiện · click Áp dụng **liên tục** | Pairwise / bảng quyết định |
| **Button mở form** (Thêm mới…) | click → mở đúng popup | — |
| **Danh sách** | chưa có dữ liệu (icon + `"Không có dữ liệu"`) · có dữ liệu · text tổng `Tổng số {X} …` · sau **xoá** → `{X-1}` · sau **thêm** → `{X+1}` · **thứ tự** sắp xếp (bản ghi mặc định/mới nhất ở đâu) · từng cột hiển thị (định dạng ghép như địa chỉ) · tag trạng thái hiện / ẩn | Phân vùng + Sơ đồ chuyển trạng thái |
| **Cột thao tác / menu Mở rộng** | danh sách action hiển thị · từng action **enable/disable theo trạng thái bản ghi** (VD `Đặt làm mặc định`, `Xoá` disable khi là bản ghi mặc định) · click từng action → đúng popup/màn | Bảng quyết định |
| **Phân trang** | dữ liệu nhiều trang (20 bản ghi / 10 mỗi trang → 2 trang) · chuyển trang · quay lại trang 1 **giữ kết quả tìm kiếm** · xoá bản ghi khi đang lọc → cập nhật · phân trang luôn ở cuối, mặc định 10/trang · dropdown số bản ghi `10 / 20 / 50 / 100` · chọn 20 → hiển thị 20 | Giá trị biên |
| **Popup xác nhận** (đặt mặc định, xoá…) | nội dung nguyên văn có tham số `[địa chỉ]` · **Huỷ** → đóng, dữ liệu không đổi · **X** → đóng, dữ liệu không đổi · **Xác nhận** → toast nguyên văn + dữ liệu đổi + **vị trí** bản ghi trong danh sách | Chuyển trạng thái UI |
| **Textbox trong form** | hiển thị mặc định (Thêm: trống · **Sửa: giá trị lần lưu gần nhất**) · placeholder (Sửa: xoá dữ liệu cũ trước khi kiểm) · để trống → lỗi inline nguyên văn (`Vui lòng không để trống`) / cho phép trống nếu không bắt buộc · chỉ dấu cách · **max** / **max+1** (`Tự động cắt khi nhập quá N ký tự`) · html/css · chữ + số + ký tự đặc biệt · link · chữ hoa → lưu đúng chữ hoa · copy ra · paste vào · khoảng trắng đầu/cuối → trim | Giá trị biên + Phân vùng |
| **Số điện thoại** | trống · dấu cách · max / max+1 · ký tự khác số bị chặn · sai định dạng (`012345678910`, `00000000000000`, `123564976`) → `Số điện thoại sai định dạng` · **mỗi nhóm đầu số hợp lệ 1 TC** theo regex SRS (VD `(1900\|1800)[0-9]{4}` · `(05\|03\|04\|07\|08\|09\|024\|028\|06)[0-9]{8}` · `(\+84\|84)[0-9]{9}` · số cố định `02x…`) · copy/paste | Phân vùng tương đương theo regex |
| **Combobox chọn 1** (Tỉnh/Thành, Phường/Xã…) | hiển thị (trống / giá trị cũ) · placeholder · để trống + Lưu → lỗi · click mũi tên → danh sách đúng nguồn · gõ tìm gợi ý · chọn từ kết quả tìm · chọn 1 · **không chọn được nhiều** · icon X → clear · combobox con khi chưa chọn cha → rỗng + lỗi khi click ra ngoài | Phân vùng |
| **Checkbox cờ "mặc định"** | lần đầu (chưa có bản ghi) → **checked**, bỏ tích → lỗi nguyên văn + tự tích lại · đã có bản ghi → unchecked · tích chọn → đổi bản ghi mặc định, bỏ mặc định bản ghi cũ | Sơ đồ chuyển trạng thái |
| **Lưu – thành công** | chỉ nhập trường bắt buộc · nhập tất cả · Sửa không đổi dữ liệu → vẫn thành công, dữ liệu giữ nguyên · toast nguyên văn · **vị trí** bản ghi trong danh sách · tạo lần đầu / lần 2 có-không tích mặc định · **Check database / API** khi QA có quyền | Phân vùng |
| **Lưu – thất bại** | trùng tên / trùng toàn bộ → lỗi nguyên văn · để trống tất cả → lỗi inline · **giới hạn số bản ghi** (N−1 → thành công, N → toast giới hạn) · **2 tab cùng thêm tại biên** (tab 1 thành công, tab 2 báo giới hạn) · bỏ cờ mặc định khi chỉ có 1 bản ghi / khi có nhiều bản ghi (2 message khác nhau) | Giá trị biên + Bảng quyết định |
| **Huỷ / X trên form** | Huỷ khi **chưa** nhập / **đã** nhập · X khi chưa nhập / đã nhập → đóng, không tạo/sửa bản ghi | Phân vùng |
| **Xem chi tiết** | popup đủ vùng (title, thông tin, vùng button) · từng field · tag · **button theo trạng thái** bản ghi (mặc định: chỉ Chỉnh sửa · không mặc định: Chỉnh sửa, Đặt mặc định, Xoá) · click từng button · mở sau khi tìm kiếm · mở sau khi chỉnh sửa | Bảng quyết định |
| **Xoá** | action enable/disable theo trạng thái · popup nội dung nguyên văn · Huỷ / X / Xác nhận · xoá **bản ghi duy nhất** / **bản ghi mặc định** → lỗi · **ràng buộc dữ liệu phụ thuộc** (VD kho có 0 / 1 / nhiều sản phẩm, sản phẩm hết tồn, đã huỷ hàng) · tìm lại bản ghi vừa xoá → không còn · xoá khi đang lọc → mất khỏi kết quả lọc | Bảng quyết định |
| **Đồng thời** | 2 tab / 2 thiết bị cùng tài khoản: tab 1 xoá – tab 2 sửa · cùng xoá · cùng thêm tại biên giới hạn | Sơ đồ chuyển trạng thái (tranh chấp) |

## 5. Kỹ thuật thiết kế — khi nào dùng, ghi ở đâu

| Kỹ thuật | Dùng khi SRS có | Bằng chứng trong file |
|---|---|---|
| **Phân vùng tương đương** | Nhiều loại đầu vào cùng hành vi (có/không voucher, thanh toán QR/Zalopay, nhóm đầu số SĐT, có/không dữ liệu) | Ghi chú `Kỹ thuật: Phân vùng tương đương` |
| **Phân tích giá trị biên** | Giới hạn số: ký tự, dung lượng, số file, số ngày, số giờ, số lượt, **số bản ghi tối đa** (29/30), số bản ghi mỗi trang | Bảng BVA ở sheet `Kỹ thuật thiết kế TC` + Ghi chú |
| **Bảng quyết định** | Thành phần hiện/ẩn/enable theo **tổ hợp** điều kiện (trạng thái × vai trò × cờ mặc định), kết hợp điều kiện lọc | Bảng quyết định ở sheet phụ, mỗi ô → ≥ 1 TC |
| **Sơ đồ chuyển trạng thái** | Đối tượng có vòng đời (đơn hàng, yêu cầu, thanh toán, bản ghi mặc định ↔ thường) | Bảng chuyển trạng thái ở sheet phụ, mỗi phép chuyển hợp lệ → 1 TC, thêm TC cho phép chuyển **không** hợp lệ và tranh chấp (2 bên đổi trạng thái cùng lúc) |

Sheet phụ `Kỹ thuật thiết kế TC` sinh từ biến `TECHNIQUES` trong file dữ liệu — giúp reviewer thấy TC nào sinh từ ô nào. File mẫu `Quanlykho` **không** có sheet này và không ghi kỹ thuật ở Ghi chú — đây là phần skill **bổ sung thêm**, không xoá khi user không yêu cầu.

## 6. Xử lý khi tài liệu không rõ / mâu thuẫn

| Tình huống | Làm gì |
|---|---|
| SRS mâu thuẫn design (VD SRS `Bắt buộc = No`, design có `*`) | Viết TC theo **design** (thứ người dùng thấy), ghi Ghi chú `Mâu thuẫn SRS (…) và design (…) - cần BA confirm`. Báo lại trong tóm tắt |
| SRS mâu thuẫn chính nó (2 mục nói khác nhau) | Ghi cả 2 mục vào Ghi chú, BA confirm |
| Tính năng ghi "chưa làm phase này" | Vẫn viết TC, Ghi chú lý do → tester chấm `N/A` |
| SRS không liệt kê giá trị (danh sách lý do, định dạng file, nội dung popup) | Kết quả ghi `theo design`, Ghi chú `Đối chiếu … với Figma/BA trước khi test`. **Không bịa danh sách** |
| `Tương tự STT x mục y` | Mở mục y đọc rồi mới viết — không để nguyên "tương tự" trong kết quả mong muốn |
| Chưa biết tên API/trường | Ghi `Bổ sung tên API và tên trường sau khi dev cung cấp` |

## 7. Lỗi hay gặp trong file mẫu — KHÔNG chép theo

File mẫu là bài làm thật, có lỗi. Học **cấu trúc và cách phủ**, không học lỗi:

| Lỗi trong `Quanlykho` | Viết đúng |
|---|---|
| Kết quả đánh số bước không khớp bước (`Kiểm tra icon X` có 3 bước nhưng kết quả ghi `4.`) | Số ở đầu Kết quả = số bước cuối cùng của TC |
| Tiêu đề Mục đích trùng nhưng khác dữ liệu (`(\+84\|84)[0-9]{8}` cho cả TC `{10}`) | Mục đích nêu đúng biến thể |
| Lỗi chính tả (`desgin`, `layoput`, `chuối`, `poppup`, `butotn`) | Kiểm chính tả trước khi xuất |
| UC đánh số trùng (`UC3` dùng cho cả Chỉnh sửa, Xem chi tiết, Xoá) | Đánh số UC tăng dần không trùng |
| Ô Mục đích ghi `Button X`, Bước ghi `Check khi click x` (lệch cột) | Tên thành phần ở cột Chức năng, `Check khi click …` ở Mục đích |
| Kết quả ghi lẫn lời nhắn trong ngoặc kép lồng nhau (`"Thông báo toast lỗi: "Vui lòng…"`) | `Hiển thị toast lỗi: "Vui lòng chọn địa chỉ khác làm mặc định trước!"` |
| Kết quả mơ hồ (`Không thêm mới bản ghi thành công`, `Hệ thống cập nhật theo thời gian thực`) | Nêu message/hành vi quan sát được; chưa rõ → Ghi chú BA confirm |
| Dòng TC thiếu công thức ID (ô A trống) | Mọi dòng TC đều có công thức ID |
