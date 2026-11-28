# SegmentedControl

Nhóm 2–5 lựa chọn liền nhau, chọn đúng một, đổi ngay cách xem dữ liệu.

**Dùng khi:** khoảng thời gian của trang Thống kê (Hôm nay, 7 ngày, 30 ngày, Toàn thời gian), lọc Lớp/Khối ở Bảng xếp hạng, sắp xếp bình luận (Top / Mới nhất / Cũ nhất).

**Không dùng khi:** chuyển giữa các trang con có nội dung khác hẳn (dùng Tabs).

## Biến thể và trạng thái

- Đã chọn: nền `primary-soft`, chữ `primary`; rê chuột; focus.

## Cần cung cấp

- Nhãn ngắn; lựa chọn mặc định theo FR (Thống kê mở sẵn Toàn thời gian).

## Khả năng truy cập

- `role="radiogroup"` + `role="radio"` với `aria-checked`; phím mũi tên chuyển lựa chọn.

## Class và token

`is-seg`, `is-seg__opt` · token `primary-soft`, `primary`, `line-strong`, `control-h-sm`.
