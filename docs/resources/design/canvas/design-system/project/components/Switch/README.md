# Switch

Công tắc bật/tắt có hiệu lực ngay, không cần nút Lưu.

**Dùng khi:** công tắc cấu hình hệ thống (AI tổng, Search, Moderation, Topic suggestion, bảo trì, tạm dừng đăng ký, cờ Group/Chat/Gamification), bật/tắt popup Chat, duyệt trước khi đăng trong nhóm.

**Không dùng khi:** lựa chọn trong form chỉ có hiệu lực khi bấm Lưu (dùng Checkbox).

## Biến thể và trạng thái

- Tắt: viền `line-strong`, núm `ink-muted`; bật: nền `primary`, núm `on-primary`; focus; tắt hẳn (disabled).
- Có dòng mô tả hậu quả dưới nhãn khi cần ("Chỉ tài khoản ADMIN dùng được hệ thống").

## Cần cung cấp

- Nhãn nói điều được bật, không phải trạng thái ("Chế độ bảo trì", không "Đang bật").

## Khả năng truy cập

- `<button role="switch" aria-checked>`; trạng thái đọc được, không chỉ dựa vào màu (vị trí núm).

## Class và token

`is-switch`, `is-switch__track`, `is-switch__thumb` · token `primary`, `on-primary`, `line-strong`, `ink-muted`, `radius-full`.
