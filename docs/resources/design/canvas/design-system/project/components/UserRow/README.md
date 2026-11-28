# UserRow

Dòng một người dùng: avatar, tên hiển thị, @username, Lớp/Khối, nhãn vai trò, thao tác.

**Dùng khi:** người theo dõi / đang theo dõi, thành viên nhóm, kết quả tìm người, mời vào nhóm, thành viên nhóm chat.

**Không dùng khi:** bảng quản trị người dùng nhiều cột (dùng DataTable).

## Biến thể và trạng thái

- Thao tác theo ngữ cảnh: Theo dõi / Đang theo dõi, Nhắn tin, menu "…" (Bổ nhiệm Group Mod, Giáng, Kick).
- Nhãn vai trò bằng StatusLabel: Owner, Group Mod, Mod, Admin; nhãn tài khoản: Tài khoản đã bị khóa.
- Tài khoản đã xóa: "[Người dùng đã xóa]", avatar trung tính, không liên kết.

## Cần cung cấp

- Tên hiển thị, username, Lớp/Khối (nếu có), vai trò trong ngữ cảnh, quan hệ theo dõi.

## Khả năng truy cập

- Tên là liên kết tới hồ sơ; nút Theo dõi có `aria-pressed`.

## Class và token

`is-li` + `is-avatar` + `is-status` · token như ListItem.
