# Comment

Bình luận và trả lời (2 cấp) có avatar cạnh tên (DD-UI-12), dòng trích khi trả lời, Upvote cỡ nhỏ.

**Dùng khi:** khu bình luận của bài (SCR-M04-01), xem lại bình luận đã bị xử lý (SCR-M04-02).

**Không dùng khi:** tin nhắn chat (dùng MessageBubble).

## Biến thể và trạng thái

- Bình luận gốc và trả lời thụt vào một cột avatar; trả lời có dòng trích "tên người được trả lời: đầu bình luận…" (BR-M04-04).
- Nhãn "Tác giả" cạnh tên tác giả bài; "(đã chỉnh sửa)"; Upvote cỡ nhỏ (tắt với bình luận của chính mình).
- Đã bị gỡ/xóa: chữ nghiêng `ink-muted` thay nội dung, không có thao tác.
- Menu "…": Sửa, Xóa (không hỏi lại — SC-M04), Báo cáo.

## Cần cung cấp

- Tác giả, thời điểm, nội dung (định dạng BR-M04-01), số upvote, trạng thái của người xem, dòng trích.

## Khả năng truy cập

- Mỗi bình luận là một mục danh sách; nút "…" có `aria-label` nêu tên tác giả.

## Class và token

`is-comment`, `is-comment__head`, `is-comment__body`, `is-quote`, `is-comment__replies`, `is-comment--removed` · token `body-comment`, `avatar-sm`, `ink-muted`, `line-strong`.
