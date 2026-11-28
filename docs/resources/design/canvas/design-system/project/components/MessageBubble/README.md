# MessageBubble

Tin nhắn trong cuộc trò chuyện: tin của người khác bên trái, của mình bên phải nền `primary-soft`.

**Dùng khi:** Cuộc trò chuyện 1-1 và nhóm chat (SCR-M16-02).

**Không dùng khi:** bình luận bài (dùng Comment).

## Biến thể và trạng thái

- Nhóm chat: tên người gửi trên tin đầu của chuỗi; 1-1: không có tên.
- "Đã xem" dưới tin mới nhất của mình; tin đã thu hồi (trong 5 phút): khung nét đứt, chữ nghiêng "Tin nhắn đã được thu hồi".
- Tin hệ thống (thêm thành viên, đổi tên nhóm) căn giữa; dải ngày ngăn theo ngày.
- Đang đọc tin cũ mà có tin mới: nút "Tin mới" để nhảy xuống (SC-M16-003).

## Cần cung cấp

- Nội dung, người gửi, thời điểm, đã xem, đã thu hồi.

## Khả năng truy cập

- Danh sách tin có `role="log"` và `aria-live="polite"`; thời điểm đọc được.

## Class và token

`is-msgs`, `is-msg`, `is-msg--out`, `is-bubble`, `is-msg__meta`, `is-msg--recalled`, `is-sysmsg`, `is-datesep` · token `primary-soft`, `surface`, `line`, `bg`, `body-comment`.
