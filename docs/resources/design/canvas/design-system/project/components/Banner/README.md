# Banner

Thông báo toàn trang của Admin: một dải dưới thanh trên cùng, văn bản thuần ≤200 ký tự, người xem đóng được (FR-M10).

**Dùng khi:** SCR-SHARED-02 trên mọi trang, cho mọi người kể cả Guest; nội dung mới thì hiện lại.

**Không dùng khi:** thông báo riêng cho một người (dùng InlineAlert, thông báo).

## Biến thể và trạng thái

- Tone thông tin (mặc định); tone cảnh báo cho thông báo bảo trì sắp tới.
- Văn bản dài xuống dòng, không cắt.

## Cần cung cấp

- Nội dung banner Admin nhập.

## Khả năng truy cập

- `role="region"` có nhãn "Thông báo"; nút Đóng có nhãn.

## Class và token

`is-banner`, `is-banner--warning` · token `info-soft`, `warning-soft`, `ink`, `line`.
