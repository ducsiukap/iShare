# NavBar

Cột điều hướng trái 200px (DD-UI-21); khu kiểm duyệt và quản trị dùng biến thể `--console` nền sẫm trong AdminShell (DD-UI-42).

**Dùng khi:** mọi trang desktop.

**Không dùng khi:** điều hướng trong một trang (dùng Tabs).

## Biến thể và trạng thái

- Người dùng: Trang chủ, Chủ đề, Nhóm, Bảng xếp hạng; dòng chân Privacy Policy/ToS; rộng `nav-w` 200px.
- Mục đang xem: nền `primary-soft`, chữ và icon `primary`; rê chuột `surface-hover`.
- Khu kiểm duyệt và quản trị (`--console`, nằm trong cột `is-console__side` rộng `nav-w-wide` 240px của AdminShell): nhóm Kiểm duyệt (Hàng chờ báo cáo, Hàng chờ duyệt bài, Hàng chờ khiếu nại, Quản lý Tag, Nhật ký kiểm duyệt), nhóm Quản trị chỉ Admin thấy (Người dùng, Chủ đề, Cấu hình hệ thống, Banner, Nhật ký Admin, ba trang Thống kê); mỗi mục có icon. Chữ `console-ink`, icon và tên nhóm `console-ink-muted`; rê chuột `console-hover`; mục đang xem nền `console-active`, chữ và icon `console-accent`. Lối "Về iShare" nằm trên thanh của AdminShell.

## Cần cung cấp

- Danh sách mục theo vai trò, mục hiện tại.

## Khả năng truy cập

- `<nav>` có nhãn; mục hiện tại `aria-current="page"`.

## Class và token

`is-nav`, `is-nav--console`, `is-nav__item`, `is-nav__group`, `is-nav__foot` · token `nav-w`, `nav-w-wide`, `primary-soft`, `primary`, `surface-hover`, `console-*`.
