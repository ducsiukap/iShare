# FilterBar

Hàng bộ lọc phía trên danh sách hoặc bảng; lọc có hiệu lực ngay, chip bộ lọc đang áp dụng có nút gỡ.

**Dùng khi:** Kết quả tìm kiếm (Chủ đề, Tag, thời gian, chỉ nội dung đang theo dõi, sắp xếp), nhật ký và hàng chờ khu quản trị.

**Không dùng khi:** chuyển chế độ xem (dùng Tabs, SegmentedControl).

## Biến thể và trạng thái

- Select cỡ nhỏ, Checkbox hoặc Switch, ô tìm có icon; nút "Xóa bộ lọc" khi có bộ lọc khác mặc định.
- Hàng chip bộ lọc đang áp dụng (Tag có nút gỡ).

## Cần cung cấp

- Bộ lọc và giá trị theo FR: thời gian Hôm nay / Tuần này / Tháng này / Tất cả; sắp xếp Liên quan / Mới nhất / Nhiều upvote nhất.

## Khả năng truy cập

- Mỗi bộ lọc có nhãn; vùng kết quả cập nhật thông báo số kết quả qua `aria-live`.

## Class và token

`is-filters`, `is-field`, `is-input--sm`, `is-check` · token `control-h-sm`, `ink-muted`.
