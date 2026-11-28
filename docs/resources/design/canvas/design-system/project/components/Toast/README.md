# Toast

Thông báo ngắn góc dưới trái sau một thao tác của chính người dùng, tự ẩn sau vài giây.

**Dùng khi:** Đã lưu bài, Đã sao chép link mời, Đã gửi báo cáo, lỗi mạng khi gửi.

**Không dùng khi:** lỗi của ô nhập (để cạnh ô), thông báo phải đọc kỹ hoặc cần quyết định (dùng InlineAlert, Dialog).

## Biến thể và trạng thái

- Thành công, thông tin, cảnh báo, lỗi — icon và màu theo tone, chữ luôn `ink`.
- Có thể kèm một nút ("Thử lại"); lỗi không tự ẩn.

## Cần cung cấp

- Một câu: chuyện gì xảy ra (+ làm gì tiếp nếu lỗi), theo giọng văn PRODUCT.md mục 8.

## Khả năng truy cập

- `role="status"` (lỗi: `role="alert"`); không cướp focus; nút Đóng có nhãn.

## Class và token

`is-toast`, `is-toast__ic`, `is-tone-*` · token `surface-raised`, `shadow-1`, `success`, `info`, `warning`, `danger`.
