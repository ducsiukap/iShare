# Counter

Số đếm nhỏ cho mục chưa đọc hoặc số lượng trong tab.

**Dùng khi:** chuông thông báo, biểu tượng Tin nhắn (số cuộc trò chuyện có tin chưa đọc), cuộc trò chuyện, tab có số lượng.

**Không dùng khi:** số liệu chính của trang (dùng StatTile).

## Biến thể và trạng thái

- Nhấn mạnh: nền `primary`, chữ `on-primary` (chưa đọc).
- Trầm (`--muted`): số lượng trong tab.
- Trên 99 hiện "99+"; bằng 0 thì ẩn.

## Cần cung cấp

- Số nguyên.

## Khả năng truy cập

- Số đếm phải có trong nhãn của nút chứa nó; bản thân Counter `aria-hidden`.

## Class và token

`is-counter`, `is-counter--muted`, `is-dot` · token `primary`, `on-primary`, `surface-hover`, `radius-full`.
