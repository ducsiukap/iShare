# SearchField

Ô tìm kiếm bo tròn hai đầu trên thanh trên cùng (DD-UI-09).

**Dùng khi:** tìm bài viết, người dùng, Tag, Chủ đề, nhóm từ mọi trang; ô lọc danh sách trong khu quản trị dùng TextField có icon.

**Không dùng khi:** lọc theo giá trị cố định (dùng FilterBar).

## Biến thể và trạng thái

- Mặc định (nền `bg`), rê chuột, focus (nền `surface`, viền `focus`) mở gợi ý (Combobox), có chữ (nút Xóa), lỗi giới hạn tần suất (dòng lỗi trong gợi ý).
- Rộng tối đa 560px, nằm giữa logo và nhóm nút bên phải.

## Cần cung cấp

- Placeholder gợi ý phạm vi tìm: "Tìm bài viết, Chủ đề, Tag, người dùng, nhóm".

## Khả năng truy cập

- `role="search"` trên form; `<label class="is-sr">`; khi mở gợi ý dùng mẫu combobox (xem Combobox).

## Class và token

`is-search`, `is-search__clear` · token `bg`, `surface`, `line-strong`, `focus`, `radius-full`, `control-h`.
