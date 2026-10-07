# Git: sự cố push file lớn (30-09-2026) & quy tắc

## Chuyện đã xảy ra

- Commit `f054023` ("tttt") chứa 6 video trong `test-data/upload-boundary/videos/` (100–200MB). GitHub **chặn file > 100MB** → push bị từ chối, kể cả khi commit sau đã xoá file (vẫn nằm trong lịch sử).
- Xử lý (user đồng ý): tạo nhánh `backup/before-remove-large-files` → `git filter-branch` gỡ `test-data/upload-boundary` khỏi các commit **chưa push** → push `10e175f..629320b`. Tree hash trước/sau trùng (`b101cd6`) — code không đổi.
- Hash đổi: `469ac95` "tttt", `cc06f90` "43434", `629320b` "3334".

## Việc còn treo

- Nhánh `backup/before-remove-large-files` **vẫn còn** (07-10-2026). Khi user xác nhận GitHub ổn thì có thể xoá: `git branch -D backup/before-remove-large-files` — **hỏi trước**.
- `.gitignore` vẫn chưa chặn `test-data/` → xem [bao-mat-env-gitignore.md](bao-mat-env-gitignore.md).

## Quy tắc

- CLAUDE.md: **cấm** `git pull/checkout/merge/rebase/reset`; chỉ dùng read-only `status/diff/log`. Viết lại lịch sử chỉ khi user **đồng ý rõ ràng**, luôn tạo nhánh backup trước.
- File test lớn để ngoài git (hoặc Git LFS; LFS cũng không nhận file > 2GB).
- Commit message của user thường ngắn/ngẫu nhiên ("cmt", "3334") — không cần bắt chước, nhưng chỉ commit khi user yêu cầu.
