# Tammi — Quản lý gói cước: tổng quan & nguồn tài liệu

> Dự án **thật** user đang làm (không phải bài tập Perfex CRM). Hệ thống "Tổng đài Tammi" / **Tammi OA**, phân hệ **CMS admin** quản lý gói cước + **Web OA** (kênh bán/mua gói).
> Module thư mục: `goi-cuoc` · nền tảng `web` · TC viết dạng **Excel theo file mẫu** (không phải Markdown 4 vòng) → dùng skill `skills-srs-excel-testcases`.
> Chưa có REQ ID — truy vết theo **STT SRS** ở cột Ghi chú.

## Nguồn — dùng đúng link (đã từng nhầm)

| Nguồn | Link / file | Ghi chú |
|---|---|---|
| **SRS đúng** | Google Docs `1Tl-XuDdMvenP1cUilgXbsOMHfwKcFMliw52gmrN7y7M` (tab `t.ik8z71qi70ys`) | Tên: "TLNV_Tổng đài Tammi_Gói cước_phase 1". Nhiều tab: Quản lý gói cước (UC1–UC4, bảng Trạng thái gói cước), Luồng mua gói trên Web OA, Cửa hàng & Giỏ hàng… |
| Bản SRS tải về | `docs/requirements/TLNV_Tổng đài Tammi _Gói cước_phase 1 v0.1.docx` (+ bản `.md.docx`) | Bản offline |
| **SRS Gói cước - Đơn hàng (mới 02-10/05-10-2026)** | Google Docs `1gebcMrCOvHDA9jNmpakhRug4a8VKc1WBcq7dJUrLKvQ` (tab `t.2l2tiqe3sf3r`) | Tách 2 hệ thống Gói cước + **Đơn hàng**. Gồm các tài liệu: Tổng quan · Tổng hợp trạng thái (A gói cước, B đơn hàng, C miniapp) · Quản lý loại gói / gói / CTKM · **Danh sách đơn hàng (CMS)** · Gói cước đã đăng ký · Miniapp gói cước Tammi · Web OA. Tải bằng `fetch_sources.py` được (link công khai) |
| **Figma CMS Quản lý đơn hàng** | `[WEB] Tammi OA`, page `CMS Gói cước`, section `T_Danh sách đơn hàng` node `42456-50485` | Danh sách, panel Bộ lọc, Empty cases, Chi tiết đơn hàng (3 biến thể hoá đơn: MST / mã QHNS / Cá nhân) |
| **Figma Miniapp mua gói** | `Super App File 01` (`tjRAgsO3j8Xp2ffMOI1Qyr`), page `Gói cước Tammi`, node `113087-6879` | ⚠️ KHÔNG phải node `34842-144249` trong file Tammi OA (user dán nhầm 07-10). Hàng 1: danh sách loại gói → Đăng ký gói → Thanh toán CTT/OTP → Kết quả; hàng 2: Gói cước của tôi + Lịch sử giao dịch |
| ❌ Link SAI | Google Docs `1yE1O60Z…` | Là SRS **PIFA Buyer – Quản lý đơn hàng**, KHÔNG phải gói cước. User từng dán nhầm 30-09-2026 |
| **Figma** | `figma.com/design/MM9eqvd9vBTdRKfqzIZO6Q/-WEB--Tammi-OA` | Node `34842-144249` = section **"Chi tiết gói cước"** (màn chi tiết + popup phát hành). Trang `CMS Gói cước → Thanh toán gói cước → UI` = luồng mua/thanh toán. File rất lớn (44.075 × 6.709 px). **User đăng nhập Figma sẵn trên trình duyệt** — cách đọc: xem [trinh-duyet-figma-playwright.md](../03_moi-truong-cong-cu/trinh-duyet-figma-playwright.md) |
| **Sheet TC thật của Tammi** | Google Sheet `1gKNbC-lEFeFCD9TgqQN8nf51bbNqRn2cn5LMe2jkmI8`, sheet **"CMS-Quản lý gói cước"** (gid `2086735008`) | Cột A–G, ID bằng công thức, ghi chú `[Bổ sung dd/mm/yyyy]`. Có cả sheet **CMS-CTKM** dùng tham chiếu cách viết |
| Sheet mẫu format "Quanlykho" | Google Sheet `1D98QXyTaUD9jJHPIVOD815brg6nsoSZh3PnKym1xSPg` ("TC_F2C CMS", 22 sheet) — gid `1321670876` = **Quanlykho** | User chỉ định **dùng sheet Quanlykho làm khuôn** cho bộ UC1–UC4 |
| Sheet mẫu QLDH | Google Sheet `1wlyeOquNOb8XIF7jNrfrgwGQMI2oSZ3_QSUeNq80faY`, gid `822482002` = **QLDH_Chi tiết đơn hàng** | Đã dùng làm khuôn lúc bắt đầu UC Thanh toán (đã dừng) |

## Luồng nghiệp vụ chính (đã nắm)

- **Trạng thái gói**: Nháp → (Ban hành) → Đã phát hành / Đang kinh doanh → Ngừng kinh doanh. Ban hành có 2 chế độ: **Tự động** (TH1.1–TH1.3 theo mốc thời gian bắt đầu/kết thúc, có job quét) và **Thủ công** (Th2.1–Th2.2).
- Loại hình gói: **Chính / Add-on / Nền**. Kênh bán: Web OA, Mini app…
- Màn danh sách (UC1) có: tìm kiếm, sắp xếp, phân trang, **Cài đặt bảng** (ẩn/hiện cột), **Bộ lọc** (Chu kỳ / Loại hình gói / Trạng thái / Kênh phân phối), Xuất excel.

## File chi tiết

- TC đã viết, số lượng, quy ước ID → [tc-da-viet-va-quy-uoc-id.md](tc-da-viet-va-quy-uoc-id.md)
- AMB UC4 Ban hành → [amb-uc4-ban-hanh.md](amb-uc4-ban-hanh.md)
- AMB UC1 Cài đặt bảng + Bộ lọc → [amb-uc1-cai-dat-bang-bo-loc.md](amb-uc1-cai-dat-bang-bo-loc.md)
- AMB CMS Quản lý đơn hàng → [amb-cms-quan-ly-don-hang.md](amb-cms-quan-ly-don-hang.md)
- AMB UC Thanh toán gói (chưa viết TC) → [amb-uc-thanh-toan-goi-cuoc.md](amb-uc-thanh-toan-goi-cuoc.md)
