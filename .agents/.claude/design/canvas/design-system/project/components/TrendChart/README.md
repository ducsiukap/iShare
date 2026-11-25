# TrendChart

Biểu đồ cột xu hướng theo thời gian của trang Thống kê; tối đa 3 chuỗi chồng nhau, khác nhau bằng độ sáng của cùng một sắc.

**Dùng khi:** xu hướng đăng ký mới, bài viết mới, bình luận mới (một chuỗi `chart-2`); cảnh cáo theo mức LIGHT/MEDIUM/HEAVY (`chart-1/2/3`); ban tạm thời / vĩnh viễn (`chart-1/2`).

**Không dùng khi:** so sánh các nhóm không theo thời gian (dùng StatTile hoặc DataTable).

## Biến thể và trạng thái

- Chia cột theo giờ (Hôm nay), ngày (7 hoặc 30 ngày), tháng (Toàn thời gian) — FR-M15-01.19.
- Chú thích luôn có chữ; nút "Xem bảng số liệu" mở bảng cùng dữ liệu (không chỉ dựa vào màu, QF-03).
- Trống: trục và dòng "Chưa có dữ liệu trong khoảng này"; đang tải: Skeleton khối.

## Cần cung cấp

- Nhãn trục thời gian, các chuỗi số đếm, tên chuỗi.

## Khả năng truy cập

- SVG `role="img"` với tiêu đề; bảng số liệu tương đương trong `details`; cột ≥ 3:1 trên `surface`.

## Class và token

`is-chart`, `is-chart__grid`, `is-chart__axis`, `is-chart__s1|s2|s3`, `is-legend` · token `chart-1`, `chart-2`, `chart-3`, `line`, `ink-muted`.
