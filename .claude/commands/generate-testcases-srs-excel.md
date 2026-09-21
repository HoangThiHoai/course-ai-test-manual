---
description: Sinh manual test case cho một mục SRS (Google Docs/.docx) + Figma, học format file TC có sẵn (Google Sheet/.xlsx) và xuất ra file Excel riêng đúng format mẫu, kèm sheet kỹ thuật thiết kế TC.
skills:
  - skills-srs-excel-testcases
---

> **BẮT BUỘC (MANDATORY SKILL):** Nạp và đọc kỹ skill **`skills-srs-excel-testcases`** (tại `.claude/skills/skills-srs-excel-testcases/SKILL.md`) và `references/tc_writing_rules.md` trước khi làm.

# Command: SRS + Figma → Test Case Excel theo file mẫu

## Cách gọi

```
/generate-testcases-srs-excel
SRS:   <link Google Docs hoặc đường dẫn .docx>   mục <số mục, VD 1.3.4>
TC:    <link Google Sheet hoặc đường dẫn .xlsx>
Figma: <link Figma có node-id>        (không bắt buộc)
```

Người dùng có thể viết tự do (VD "đọc SRS mục 1.3.4 … viết TC … tạo file excel riêng") — tự bóc 3 đầu vào trên.

## Thực hiện

Làm đúng **6 bước** trong SKILL.md:

1. Tải nguồn — `fetch_sources.py` (bỏ qua nếu đã tải trong phiên này)
2. Trích mục SRS + mục được tham chiếu — `extract_srs.py --section <mục>`
3. Đọc design — ảnh nhúng trong mục SRS trước, Figma để xác nhận
4. Học format — `inspect_tc_template.py` trên 2–3 sheet cùng loại màn hình, chọn 1 sheet khuôn
5. Dựng bảng quyết định / sơ đồ chuyển trạng thái / giá trị biên → viết `src/tcdata_<mục>.py`
6. Xuất — `build_tc_excel.py`, kiểm tra lại file, gửi cho người dùng

## Nguyên tắc

- Người dùng nói **"dùng lại cái đã đọc"** → không tải/đọc lại phần đó
- Chỉ viết TC cho **đúng mục** được yêu cầu
- **Không** sửa Google Sheet — luôn tạo file Excel riêng trong `docs/testcases/<module>/<nền-tảng>/`
- Mâu thuẫn / thiếu thông tin → ghi cột Ghi chú "BA confirm", liệt kê lại trong báo cáo cuối
- Báo cáo bằng **Tiếng Việt**: nguồn đã đọc · số TC theo nhóm · kỹ thuật áp dụng · điểm cần BA xác nhận · link file
