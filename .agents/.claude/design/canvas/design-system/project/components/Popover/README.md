# Popover

Ngăn nổi gắn với một nút, chứa nội dung giàu hơn menu: ngăn thông báo, gợi ý tìm kiếm.

**Dùng khi:** chuông → ngăn 10 thông báo gần nhất, cuối ngăn "Xem tất cả" tới `/notifications` (DD-UI-23).

**Không dùng khi:** danh sách thao tác (dùng Menu).

## Biến thể và trạng thái

- Đầu ngăn có tiêu đề và thao tác (Đánh dấu tất cả đã đọc); thân là danh sách; chân có liên kết.
- Trống: "Bạn chưa có thông báo nào"; đang tải: Skeleton dòng; phiên hết hạn: lời mời đăng nhập lại.

## Cần cung cấp

- Nội dung, nút gắn.

## Khả năng truy cập

- Nút mở có `aria-expanded`, `aria-controls`; Esc đóng; focus vào ngăn khi mở bằng bàn phím.

## Class và token

`is-pop`, `is-pop__head`, `is-pop__title`, `is-pop__foot` · token `surface-raised`, `shadow-1`, `line`.
