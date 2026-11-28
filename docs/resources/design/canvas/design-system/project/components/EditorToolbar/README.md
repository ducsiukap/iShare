# EditorToolbar

Thanh công cụ của trình soạn: đúng các định dạng FR cho phép, nhóm bằng vạch ngăn.

**Dùng khi:** trình soạn bài (BR-M03-03) và bản tối giản cho bình luận, trả lời (BR-M04-01: đậm, nghiêng, code trong dòng, LaTeX, liên kết, nhắc tên, trích dẫn).

**Không dùng khi:** định dạng FR không có — không thêm màu chữ, cỡ chữ, căn lề.

## Biến thể và trạng thái

- Nút đang áp dụng ở vị trí con trỏ: `aria-pressed`, nền `primary-soft`.
- Nút tắt khi không dùng được (đã đủ 10 ảnh, đã có bình chọn).
- Mỗi nút có Tooltip kèm phím tắt.

## Cần cung cấp

- Bộ định dạng theo loại trình soạn; trạng thái của vùng chọn.

## Khả năng truy cập

- `role="toolbar"` có nhãn; Tab vào thanh rồi dùng phím mũi tên giữa các nút; mọi nút có `aria-label`.

## Class và token

`is-toolbar`, `is-toolbar__sep`, `is-iconbtn--sm` · token `line-strong`, `line`, `primary-soft`, `control-h-sm`.
