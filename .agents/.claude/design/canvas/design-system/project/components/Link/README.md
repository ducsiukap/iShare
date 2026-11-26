# Link

Liên kết điều hướng tới trang hoặc nội dung khác.

**Dùng khi:** đi tới trang khác: "Xem lịch sử", tên tác giả, tiêu đề bài, "Chính sách và Điều khoản" ở chân cột menu.

**Không dùng khi:** thực hiện thao tác thay đổi dữ liệu (dùng Button).

## Biến thể và trạng thái

- Mặc định: màu `primary`, gạch chân 1px — trong đoạn văn luôn gạch chân để không chỉ dựa vào màu (QF-03).
- Rê chuột: gạch chân dày 2px.
- Trầm (`--quiet`): tên người, tiêu đề bài trong danh sách — màu chữ thường, gạch chân khi rê chuột.

## Cần cung cấp

- `href` thật; nhãn nói rõ đích tới.

## Khả năng truy cập

- Dùng `<a href>`; focus hiện vòng `focus`.

## Class và token

`is-link`, `is-link--quiet` · token `primary`, `ink`, `focus`.
