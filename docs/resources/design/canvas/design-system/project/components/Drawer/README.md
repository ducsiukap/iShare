# Drawer

Ngăn trượt bên phải 420px cho nội dung xem kèm, không rời trang (DD-UI-24).

**Dùng khi:** Tóm tắt bài (SCR-M13-01), thông tin nhóm chat (SCR-M16-04), vai trò của một người dùng (SCR-M10-02), chi tiết dòng nhật ký.

**Không dùng khi:** thao tác ngắn cần quyết định (dùng Dialog).

## Biến thể và trạng thái

- Đầu ngăn: tiêu đề + nút đóng; thân cuộn riêng.
- Tóm tắt: đang tải (Skeleton), lỗi (ErrorState nhỏ + Thử lại), ghi chú "Tóm tắt do AI tạo, có thể chưa chính xác".

## Cần cung cấp

- Tiêu đề, nội dung.

## Khả năng truy cập

- `role="dialog"` `aria-labelledby`; Esc đóng; trả focus về nút đã mở.

## Class và token

`is-drawerwrap`, `is-drawer` · token `drawer-w`, `surface-raised`, `shadow-2`, `scrim`.
