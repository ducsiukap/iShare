# StepIndicator

Chỉ báo các bước của luồng nhiều bước: Đăng ký gồm Tài khoản → Xác minh email → Thiết lập hồ sơ.

**Dùng khi:** SCR-M01-01, -02, -03.

**Không dùng khi:** luồng một bước.

## Biến thể và trạng thái

- Bước đã xong và bước hiện tại: thanh `primary`; bước sau: thanh `line`; nhãn bước hiện tại đậm `ink`.

## Cần cung cấp

- Danh sách bước, bước hiện tại.

## Khả năng truy cập

- `<ol>`; bước hiện tại `aria-current="step"`; chữ "Bước 2 · …" nói rõ vị trí, không chỉ dựa vào màu.

## Class và token

`is-steps`, `is-step`, `is-step--done`, `is-step--current` · token `primary`, `line`, `radius-full`.
