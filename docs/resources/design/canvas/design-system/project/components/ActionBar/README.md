# ActionBar

Thanh thao tác dưới bài: Upvote · Bình luận · Tóm tắt · Lưu, Báo cáo ở cuối (DD-UI-10).

**Dùng khi:** dưới nội dung bài ở trang chi tiết.

**Không dùng khi:** danh sách bài — số upvote và bình luận chỉ để xem (DD-UI-13).

## Biến thể và trạng thái

- Mọi nút trơn như nhau (không viền, không nền); Upvote nổi bật bằng màu `primary`, chữ đậm 700 và icon nét dày (DD-UI-11).
- Đã upvote: icon tô đặc, số tăng; đã lưu: icon tô đặc, chữ "Đã lưu", màu `primary`.
- Tóm tắt chỉ có khi bài từ 300 từ và AI bật; mở ngăn Tóm tắt (Drawer).
- Bài của chính mình: Upvote tắt (BR-M12-03), giữ chỗ để thanh không nhảy; bình luận đã khóa: chữ "đã khóa" + icon khóa.
- Guest bấm Upvote, Lưu, Báo cáo: mở lời mời đăng nhập.

## Cần cung cấp

- Số upvote, số bình luận, trạng thái đã upvote/đã lưu của người xem, bài có đủ 300 từ không, bình luận có bị khóa không.

## Khả năng truy cập

- `role="group"` có nhãn; Upvote và Lưu là nút bật/tắt với `aria-pressed`; Bình luận là liên kết tới khu bình luận.

## Class và token

`is-actions`, `is-act`, `is-act--up`, `is-act--end` · token `primary`, `ink-muted`, `surface-hover`, `line`, `control-h`.
