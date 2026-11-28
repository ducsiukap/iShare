# Menu

Danh sách thao tác thả xuống từ một nút ("…", avatar).

**Dùng khi:** menu tài khoản, menu "…" của bài (Sửa, Tự ẩn, Khóa bình luận, Quản lý bình chọn, Tắt thông báo bài, Xóa), của bình luận, của thành viên nhóm.

**Không dùng khi:** chọn giá trị cho form (dùng Select) hoặc nội dung nhiều thông tin (dùng Popover).

## Biến thể và trạng thái

- Mục thường, mục có icon, mục đang bật (`aria-checked`), mục nguy hiểm `danger` (Xóa, Ban — đặt cuối, sau vạch ngăn), mục tắt.
- Menu tài khoản có đầu menu: tên và @username.

## Cần cung cấp

- Danh sách mục theo quyền của người xem; mục không có quyền thì không hiện.

## Khả năng truy cập

- `role="menu"`, `role="menuitem"`; phím mũi tên di chuyển, Esc đóng, trả focus về nút mở.

## Class và token

`is-menu`, `is-mi`, `is-mi--danger`, `is-menu__sep`, `is-menu__head` · token `surface-raised`, `shadow-1`, `surface-hover`, `danger`.
