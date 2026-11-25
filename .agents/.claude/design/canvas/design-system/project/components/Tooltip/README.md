# Tooltip

Chú thích ngắn khi rê chuột hoặc focus vào một nút, nền `ink`, chữ `surface`.

**Dùng khi:** nhắc tên nút chỉ có icon trên thanh soạn thảo ("In đậm (Ctrl+B)"), giải thích vì sao nút bị tắt.

**Không dùng khi:** thông tin cần để làm việc — phải hiện sẵn trên trang.

## Biến thể và trạng thái

- Hiện sau 300ms rê chuột, ngay khi focus; ẩn khi Esc.

## Cần cung cấp

- Một câu ngắn.

## Khả năng truy cập

- `role="tooltip"` nối bằng `aria-describedby`; không đặt nội dung tương tác trong tooltip.

## Class và token

`is-tip` · token `ink`, `surface`, `shadow-1`, `radius-sm`.
