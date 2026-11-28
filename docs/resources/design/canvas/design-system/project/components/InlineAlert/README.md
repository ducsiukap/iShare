# InlineAlert

Khối thông báo nằm trong trang, ngay chỗ liên quan; không tự ẩn.

**Dùng khi:** bài đang chờ duyệt hoặc bị từ chối (kèm lý do), tài khoản ở mức cảnh cáo MEDIUM/HEAVY khi soạn bài, Đăng ký đang tạm dừng, lỗi gửi form.

**Không dùng khi:** phản hồi nhanh sau thao tác (dùng Toast) hoặc thông báo toàn trang của Admin (dùng Banner).

## Biến thể và trạng thái

- Bốn tone: thông tin, thành công, cảnh báo, lỗi; nền `*-soft`, chữ `ink`, icon màu tone.
- Có thể kèm nút: Khiếu nại, Sửa bài, Đăng nhập.

## Cần cung cấp

- Tiêu đề ngắn, câu giải thích nêu lý do và thời hạn nếu có, hành động tiếp theo.

## Khả năng truy cập

- `role="alert"` cho lỗi, `role="status"` cho phần còn lại; nút có nhãn rõ.

## Class và token

`is-alert`, `is-alert--success|warning|danger`, `is-alert__title`, `is-alert__acts` · token `info-soft`, `success-soft`, `warning-soft`, `danger-soft`, `ink`.
