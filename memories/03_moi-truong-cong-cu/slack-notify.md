# Gửi report lên Slack

> Rule chính thức nằm ở `CLAUDE.md` mục **"📣 Gửi report lên Slack"**. File này chỉ ghi bối cảnh và trạng thái cấu hình, không chép lại rule.

## Bối cảnh

- 07-10-2026: user yêu cầu **luôn gửi report lên Slack** sau khi chạy test case xong hoặc khi có summary report mới.
- Trước ngày này, repo **chưa có** tích hợp Slack nào. Tích hợp ngoài duy nhất có sẵn là Jira/Xray.

## Trạng thái cấu hình (07-10-2026)

- `.env` **chưa có** `SLACK_WEBHOOK_URL` / `SLACK_CHANNEL`. User tự tạo Incoming Webhook trên Slack rồi tự dán vào `.env`; agent không tự nhập.
- Phiên này chưa có Slack connector/MCP.
- → Hiện tại mọi lần chạy sẽ rơi vào nhánh 3 của rule: **soạn tin, báo "chưa gửi được"**, đưa nội dung để user tự dán lên Slack.

## Ghi nhớ khi thực hiện

- Mỗi lần gửi đều **hiện bản xem trước và hỏi xác nhận**. Rule chỉ bắt buộc agent luôn đề nghị gửi, không phải tự động đăng.
- Tin nhắn không chứa bí mật / dữ liệu khách hàng, không đính kèm ảnh.
- Gửi bằng webhook: `curl -X POST -H 'Content-type: application/json' --data @payload.json "$SLACK_WEBHOOK_URL"`. Payload để ở scratchpad, không in URL webhook ra log.
- Khi đã cấu hình xong / đổi kênh → cập nhật mục "Trạng thái cấu hình" ở trên.
