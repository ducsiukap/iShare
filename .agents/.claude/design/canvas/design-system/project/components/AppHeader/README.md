# AppHeader

Thanh trên cùng cố định của mọi trang (DD-UI-20): chữ "iShare", ô tìm kiếm ở giữa khoảng còn lại, nhóm nút bên phải.

**Dùng khi:** mọi trang, kể cả khu kiểm duyệt và quản trị.

**Không dùng khi:** —

## Biến thể và trạng thái

- Đã đăng nhập: Viết bài, chuông Thông báo (Counter), Tin nhắn (Counter), avatar mở menu tài khoản (Hồ sơ, Cài đặt tài khoản, Khiếu nại của tôi, Khu kiểm duyệt cho Mod/Admin, Đăng xuất).
- Guest: Đăng nhập, Đăng ký thay cho chuông, tin nhắn, avatar.
- Logo: "i" màu `ink`, "Share" màu `primary`, chữ Be Vietnam Pro 700 — không có tệp logo (DD-UI-03).

## Cần cung cấp

- Người xem (tên, chữ cái đầu), số thông báo chưa đọc, số cuộc trò chuyện chưa đọc, vai trò.

## Khả năng truy cập

- `<header>` landmark; ô tìm kiếm `role="search"`; liên kết bỏ qua tới nội dung chính đứng trước thanh.

## Class và token

`is-topbar`, `is-logo`, `is-topbar__mid`, `is-topbar__end`, `is-avbtn` · token `topbar-h`, `surface`, `line`, `primary`.
