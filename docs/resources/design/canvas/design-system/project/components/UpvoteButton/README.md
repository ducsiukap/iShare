# UpvoteButton

Nút Upvote bật/tắt cho bài viết (trong ActionBar) và cho bình luận (cỡ nhỏ).

**Dùng khi:** bài viết và bình luận; không có downvote (BR-M12-01).

**Không dùng khi:** danh sách bài — chỉ hiện số (Stat).

## Biến thể và trạng thái

- Chưa upvote: icon nét dày (Material Symbols weight 600), chữ đậm, màu `primary`.
- Đã upvote: icon tô đặc, số +1.
- Nội dung của chính mình: tắt, màu `ink-muted` (BR-M12-03).
- Bình luận: cỡ nhỏ `--sm`, chỉ số không kèm chữ "Upvote" nhưng có nhãn ẩn.

## Cần cung cấp

- Số upvote đang có hiệu lực, trạng thái của người xem.

## Khả năng truy cập

- `aria-pressed`; nhãn đọc được "Upvote, 12".

## Class và token

`is-act`, `is-act--up`, `is-act--sm` · token `primary`, `ink-muted`.
