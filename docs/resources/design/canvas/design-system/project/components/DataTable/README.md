# DataTable

Bảng dữ liệu nhiều cột của khu kiểm duyệt và quản trị: tiêu đề cột sắp xếp được, dòng chọn được, chân bảng có phân trang.

**Dùng khi:** Hàng chờ báo cáo, duyệt bài, khiếu nại; Nhật ký kiểm duyệt, Nhật ký Admin; Người dùng; Quản lý Chủ đề, Tag; số liệu theo nhóm ở Thống kê.

**Không dùng khi:** danh sách cho học sinh (dùng PostCard, ListItem).

## Biến thể và trạng thái

- Mật độ gọn (`--compact`, dòng 38px, chữ 14px) là mặc định ở khu kiểm duyệt và quản trị (DD-UI-30); mật độ vừa (dòng 52px) khi bảng đứng trong trang của học sinh.
- Cột đang sắp xếp: `aria-sort` + mũi tên; rê chuột dòng `surface-hover`; dòng đang chọn (mở chi tiết ở ngăn phải) `primary-soft`.
- Trống: EmptyState trong khung bảng; đang tải: Skeleton dòng; không có kết quả lọc: câu "Không có vụ nào khớp bộ lọc" + Xóa bộ lọc.
- Số căn phải, chữ số đều (tabular); chữ dài cắt bằng … và có đầy đủ khi mở chi tiết.

## Cần cung cấp

- Cột, dòng, cách sắp xếp mặc định theo FR (hàng chờ: ưu tiên giảm dần), tổng số, trang.

## Khả năng truy cập

- `<table>` thật có `caption` (có thể ẩn), `th scope="col"`; nút sắp xếp trong `th`; bảng rộng cuộn ngang trong khung (QF-12).

## Class và token

`is-tablebox`, `is-table`, `is-table--compact`, `is-num`, `is-trunc`, `is-sort`, `is-tablefoot` · token `row-h`, `row-h-sm`, `bg`, `line`, `surface-hover`, `primary-soft`.
