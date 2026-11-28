# NewMessagePopup

Popup nhỏ góc dưới phải khi có tin nhắn mới lúc người dùng ở trang khác (SCR-M07-03).

**Dùng khi:** mọi trang trừ trang Chat; tắt được cho từng cuộc hoặc toàn bộ Chat.

**Không dùng khi:** thông báo không phải tin nhắn (dùng ngăn thông báo).

## Biến thể và trạng thái

- Một popup mỗi lúc, tin mới thay tin cũ; tự ẩn sau một lúc; nút Đóng; bấm vào mở cuộc trò chuyện.

## Cần cung cấp

- Người gửi, nhóm chat (nếu có), đầu tin nhắn.

## Khả năng truy cập

- `role="status"`, không cướp focus; nút Đóng có nhãn.

## Class và token

`is-popup` · token `surface-raised`, `shadow-1`, `radius-sm`.
