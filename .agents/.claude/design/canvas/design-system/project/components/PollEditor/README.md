# PollEditor

Khối tạo và quản lý bình chọn trong trình soạn bài và ở bài đã đăng (chỉ tác giả).

**Dùng khi:** trình soạn (SCR-M03-01) khi bấm nút Bình chọn trên EditorToolbar; Quản lý bình chọn (SCR-M03-04).

**Không dùng khi:** người đọc bình chọn (dùng Poll).

## Biến thể và trạng thái

- Bài nháp: sửa được mọi lựa chọn, chế độ, hạn; nút Bỏ bình chọn.
- Bài đã đăng: ba thao tác riêng — Đổi hạn kết thúc, Kết thúc ngay, Thêm lựa chọn (tổng ≤10); lựa chọn cũ chỉ đọc (SC-M03-009, -019, -020).
- Lỗi: thiếu lựa chọn (cần 2–10), thiếu hạn, hạn trước hiện tại.

## Cần cung cấp

- Danh sách lựa chọn, chế độ chọn một/nhiều (mặc định nhiều), hiện kết quả trước khi bình chọn (mặc định tắt), hạn kết thúc bắt buộc.

## Khả năng truy cập

- Mỗi ô lựa chọn có nhãn "Lựa chọn 1"…; nút gỡ có `aria-label`.

## Class và token

`is-poll`, `is-field`, `is-input`, `is-check` · token như TextField.
