# Checkbox

Bật hoặc tắt một lựa chọn độc lập, hoặc chọn nhiều trong một nhóm.

**Dùng khi:** đồng ý chính sách khi đăng ký, chọn nhiều lựa chọn của bình chọn, "chỉ nội dung đang theo dõi" trong bộ lọc, danh sách việc cần làm trong bài.

**Không dùng khi:** bật/tắt có hiệu lực ngay (dùng Switch).

## Biến thể và trạng thái

- Chưa chọn, đã chọn, focus, tắt; màu `primary` qua `accent-color`.
- Nhóm dùng `fieldset` + `legend`.

## Cần cung cấp

- Nhãn đứng sau ô, bấm vào nhãn cũng chọn được.

## Khả năng truy cập

- `<input type="checkbox">` thật trong `<label>`.

## Class và token

`is-check`, `is-fieldset` · token `primary`, `line-strong`.
