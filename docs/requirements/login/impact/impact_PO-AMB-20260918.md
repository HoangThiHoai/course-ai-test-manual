# Impact Report — PO-AMB-20260918 · 2026-09-18

> Module: `LOGIN` · Tài liệu: [requirements_login.md](../requirements_login.md)
> Nguồn: PO chốt câu trả lời cho AMB-06 → AMB-18 (không có Ticket ID — mã `PO-AMB-20260918` do agent đặt để truy vết).
> Input cho: `/update-testcases-from-impact` · `/update-automation-from-impact`

### Tóm tắt

| Nhóm | Số lượng | REQ |
|---|---|---|
| 🟢 Thêm mới | 2 | REQ-LOGIN-36 (không khoá tài khoản khi sai nhiều lần) · REQ-LOGIN-37 (timer tiếp tục chạy sau khi đăng xuất) |
| 🟡 Sửa | 1 | REQ-LOGIN-14 — chỉ assert có khoá `remember`, bỏ assert giá trị `estimate` |
| 🔴 Bỏ | 0 | — |
| ⚪ Chưa build | 0 | — (REQ-19, 20, 29, 30 vẫn ⚪ như trước, không đổi) |
| ⏸️ Trùng, không tác động | 12 | REQ-LOGIN-17, 19, 20, 21, 23, 25, 26, 27, 29, 30, 32, 35 — chỉ ghi thêm kết luận PO vào AC/Nguồn (✏️ biên tập), hành vi giữ nguyên |

Sau cập nhật: **37 REQ** (🟢 32 · 🟡 1 · 🔴 0 · ⚪ 4) · Mã kế tiếp `REQ-LOGIN-38` · `AMB-20` · `RISK-07`.

### Test case cần xử lý

**Module LOGIN chưa có bộ test case** (`docs/testcases/` không có thư mục `login`, cũng chưa có RTM) → **không TC nào bị stale**. Tác động chỉ là các TC phải viết mới / viết đúng ngay từ đầu:

| TC ID | REQ liên quan | Hành động | Lý do |
|---|---|---|---|
| — | REQ-LOGIN-36 | ➕ Viết mới — gắn `skip` tới khi có tài khoản riêng | Không được chạy trên tài khoản chung (RISK-01); số lần sai N chờ AMB-19 (tạm dùng 5) |
| — | REQ-LOGIN-37 | ➕ Viết mới — gắn `skip` tới khi có tài khoản riêng | Cần bật timer trên task do TC tự tạo |
| — | REQ-LOGIN-14 | ➕ Viết mới theo AC đã sửa | Assert **có khoá** `remember`, **không** assert `remember=estimate` |
| — | REQ-LOGIN-29, 30 | ➕ Viết trước, gắn `skip` | AMB-12 ✅: chờ hộp thư test |
| — | REQ-LOGIN-19, 20 | ➕ Viết trước, gắn `skip` | AMB-06 ✅: chờ tài khoản riêng để chạy phép thử sạch |
| — | REQ-LOGIN-27 | ➕ Viết mới, gắn nhãn `known-issue` | AMB-10 ✅ → RISK-06: hành vi hiện tại là bug tiềm ẩn (dò tài khoản) |
| — | Mọi REQ có mã HTTP trong AC (05, 06, 09, 18, 21, 23, 26, 27, 34) | ✅ Không assert mã trạng thái | AMB-08 ✅, AMB-09 ✅ — chỉ assert URL cuối + nội dung hiển thị |

### Ambiguity

| Mã | Chuyển trạng thái | Ghi chú |
|---|---|---|
| AMB-06 | ❓ → ✅ | Trùng assumption: Remember me không tạo cookie ghi nhớ → REQ-19/20 giữ ⚪ |
| AMB-07 | ❓ → ✅ | Trùng assumption: máy chủ chỉ kiểm sự tồn tại của `remember` → REQ-14 🟡 |
| AMB-08 | ❓ → ✅ | Trùng assumption: không kiểm mã trả về |
| AMB-09 | ❓ → ✅ | Trùng assumption: không kiểm mã trả về |
| AMB-10 | ❓ → ✅ | Trùng assumption: ghi nhận bug tiềm ẩn → RISK-06 mới |
| AMB-11 | ❓ → ✅ | Trùng assumption: hành vi hiện tại đúng |
| AMB-12 | ❓ → ✅ | Trùng assumption: TC viết trước, gắn `skip` |
| AMB-13 | ❓ → ✅ | Trùng assumption: không khoá → sinh REQ-LOGIN-36 |
| AMB-14 | ❓ → ✅ | Trùng assumption: không assert tiêu đề trang Forgot |
| AMB-15 | ❓ → ✅ | Trùng assumption: (a) timer vẫn chạy → sinh REQ-LOGIN-37 · (b) REQ-35 giữ nội dung |
| AMB-16 | ❓ → ⏭️ | Không làm rõ ở đợt này — recon viewport mobile ở đợt riêng |
| AMB-17 | ❓ → ✅ | Trùng assumption: không yêu cầu xoay vòng CSRF token |
| AMB-18 | ❓ → ⏭️ | Chưa sinh REQ — kiểm lại khi có tài khoản riêng |
| AMB-19 | (mới) ❓ 🟢 | REQ-36 cần thử sai bao nhiêu lần? Tạm dùng N = 5 |

Mọi kết luận **trùng** Assumption tạm → không có TC "dựa trên giả định" nào phải sửa.

### Cảnh báo

- ⚠️ **Nút thắt tài khoản riêng:** REQ-19, 20, 36, 37 + AMB-18 đều chờ **một tài khoản test riêng**. Chưa có thì 4 REQ này chỉ có TC `skip`.
- ⚠️ **Hộp thư test** vẫn thiếu: REQ-29/30 và việc xác nhận RISK-06 bị chặn.
- 🐞 **RISK-06** là bug tiềm ẩn về bảo mật (dò tài khoản). Khi xác nhận được thì lập bug bằng `/create-bug-report`.
