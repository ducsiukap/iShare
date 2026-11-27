# PostCard

Một bài trong danh sách (trang chủ, kết quả tìm kiếm, hồ sơ, trang nhóm): tác giả, tiêu đề, trích đoạn 2 dòng, Chủ đề, Tag, số upvote và bình luận chỉ để xem (DD-UI-13).

**Dùng khi:** mọi danh sách bài.

**Không dùng khi:** kết quả phụ (người dùng, nhóm) của trang tìm kiếm — dùng UserRow, GroupCard.

## Biến thể và trạng thái

- Các thẻ nằm chung một khối `is-feed`, ngăn bằng đường kẻ `line` — không lồng thẻ trong thẻ (AP-23).
- Rê chuột: nền `surface-hover`; cả thẻ bấm được qua liên kết tiêu đề.
- Biến thể: trong nhóm (dòng meta có "trong CLB Toán"), ẩn danh (avatar trung tính, "Ẩn danh"), có nhãn trạng thái (Chờ duyệt, Bị từ chối, Nháp ở hồ sơ chủ tài khoản), tiêu đề dài 2 dòng.

## Cần cung cấp

- Tiêu đề ≤150 ký tự, trích đoạn (cắt 2 dòng), tác giả hoặc Ẩn danh, thời điểm, Lớp/Khối, nhóm, Chủ đề, Tag, số upvote, số bình luận.

## Khả năng truy cập

- Mỗi thẻ là `<article>`; tiêu đề lấy cấp theo ngữ cảnh: `h2` khi danh sách nằm ngay dưới `h1` của trang, `h3` khi danh sách nằm trong một mục có `h2` (QF-17). Con số kèm chữ ẩn "upvote", "bình luận".

## Class và token

`is-feed`, `is-postcard`, `is-meta`, `is-postcard__title`, `is-postcard__excerpt`, `is-stat--up` · token `surface`, `line`, `surface-hover`, `primary`, `ink-muted`.
