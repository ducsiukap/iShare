# NavBar

Cột điều hướng trái 200px (DD-UI-21); khu kiểm duyệt dùng cùng cột với menu quản trị (DD-UI-22).

**Dùng khi:** mọi trang desktop.

**Không dùng khi:** điều hướng trong một trang (dùng Tabs).

## Biến thể và trạng thái

- Người dùng: Trang chủ, Chủ đề, Nhóm, Bảng xếp hạng; dòng chân Privacy Policy/ToS; rộng `nav-w` 200px.
- Khu kiểm duyệt (`--wide`, `nav-w-wide` 240px): nhóm Kiểm duyệt (Hàng chờ báo cáo, Hàng chờ duyệt bài, Hàng chờ khiếu nại, Quản lý Tag, Nhật ký kiểm duyệt), nhóm Quản trị chỉ Admin thấy, mục "Về iShare".
- Mục đang xem: nền `primary-soft`, chữ và icon `primary`; rê chuột `surface-hover`.

## Cần cung cấp

- Danh sách mục theo vai trò, mục hiện tại.

## Khả năng truy cập

- `<nav>` có nhãn; mục hiện tại `aria-current="page"`.

## Class và token

`is-nav`, `is-nav__item`, `is-nav__group`, `is-nav__foot` · token `nav-w`, `primary-soft`, `primary`, `surface-hover`.
