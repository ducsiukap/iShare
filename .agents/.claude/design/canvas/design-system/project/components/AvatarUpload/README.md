# AvatarUpload

Chọn ảnh đại diện, xem trước dạng tròn ngay tại chỗ.

**Dùng khi:** bước Thiết lập tài khoản (SCR-M01-03) và trang Sửa hồ sơ (SCR-M02-03).

**Không dùng khi:** đính kèm ảnh vào bài (dùng FileDrop).

## Biến thể và trạng thái

- Chưa có ảnh: avatar chữ cái đầu; có ảnh: xem trước tròn và nút Gỡ ảnh; lỗi định dạng/dung lượng.

## Cần cung cấp

- Giới hạn FR: JPEG, PNG hoặc WebP, ≤5 MB; ảnh hiển thị cắt tròn (FR-M02).

## Khả năng truy cập

- Nút Chọn ảnh mở `<input type="file" accept>`; ảnh xem trước có `alt` "Ảnh đại diện mới".

## Class và token

`is-avup`, `is-avatar--lg` · token `avatar-lg`, `radius-full`, `primary-soft`.
