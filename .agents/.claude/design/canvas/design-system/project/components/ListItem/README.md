# ListItem

Dòng danh sách chung: phần đầu (icon hoặc avatar), tiêu đề, dòng phụ, thao tác bên phải.

**Dùng khi:** danh sách Chủ đề và Tag (nút Theo dõi), các phiên bản ở Lịch sử sửa bài, danh sách chặn tham gia nhóm, yêu cầu tham gia chờ duyệt, mục cài đặt.

**Không dùng khi:** người dùng (dùng UserRow), bài (PostCard), dữ liệu nhiều cột cần sắp xếp (DataTable).

## Biến thể và trạng thái

- Mật độ vừa (cao tối thiểu `row-h` 52px) và gọn (`--compact`, `row-h-sm` 38px) cho khu quản trị.
- Cả dòng là liên kết (rê chuột `surface-hover`) hoặc dòng tĩnh có nút ở cuối; đang chọn `aria-current` nền `primary-soft`.

## Cần cung cấp

- Tiêu đề, dòng phụ (cắt bằng …), icon hoặc avatar, thao tác.

## Khả năng truy cập

- Danh sách là `<ul>`; dòng là `<li>`; một liên kết chính mỗi dòng, các nút phụ có nhãn riêng.

## Class và token

`is-list`, `is-li`, `is-li--compact`, `is-li__lead`, `is-li__main`, `is-li__title`, `is-li__sub`, `is-li__end` · token `row-h`, `row-h-sm`, `line`, `surface-hover`, `primary-soft`.
