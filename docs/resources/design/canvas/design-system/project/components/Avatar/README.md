# Avatar

Ảnh đại diện tròn; chưa có ảnh thì hiện chữ cái đầu của tên hiển thị.

**Dùng khi:** cạnh tên người ở bài, bình luận (DD-UI-12), danh sách, tin nhắn, menu tài khoản, trang hồ sơ.

**Không dùng khi:** trang trí không gắn với người nào.

## Biến thể và trạng thái

- Cỡ: nhỏ 28px (bình luận, tin nhắn, dòng bảng), vừa 40px (tác giả bài, danh sách), lớn 96px (hồ sơ).
- Chữ cái đầu trên nền `primary-soft`, chữ `primary`; có ảnh thì ảnh phủ kín vòng tròn.
- Ẩn danh và "[Người dùng đã xóa]": nền `surface-hover`, icon người, chữ `ink-muted` (`--muted`).

## Cần cung cấp

- Tên hiển thị để lấy chữ cái đầu (tối đa 2 chữ: chữ đầu họ và chữ đầu tên gọi); URL ảnh nếu có.

## Khả năng truy cập

- Đứng cạnh tên đã hiển thị thì `aria-hidden`; đứng một mình (nút menu tài khoản) thì nhãn ở nút.

## Class và token

`is-avatar`, `is-avatar--sm`, `is-avatar--lg`, `is-avatar--muted` · token `primary-soft`, `primary`, `surface-hover`, `avatar-sm`, `avatar-md`, `avatar-lg`, `radius-full`.
