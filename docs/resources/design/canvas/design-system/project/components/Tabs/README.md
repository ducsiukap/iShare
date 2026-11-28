# Tabs

Chuyển giữa các phần cùng cấp trong một trang; tab đang chọn gạch chân `primary`.

**Dùng khi:** bốn tab trang chủ (Thịnh hành / Đang theo dõi / Nhóm / Mới nhất) với mục con của Thịnh hành (Bài viết / Chủ đề / Tag), tab hồ sơ, Người theo dõi / Đang theo dõi, chu kỳ Bảng xếp hạng.

**Không dùng khi:** lọc dữ liệu (dùng SegmentedControl, FilterBar).

## Biến thể và trạng thái

- Tab chính: chữ `label`, gạch chân 2px khi chọn; có thể kèm Counter trầm.
- Mục con: chip nhỏ (`is-subtab`), chọn thì nền `primary-soft`.
- Trạng thái tab đặt vào URL khi FR có (`/?tab=following`).

## Cần cung cấp

- Nhãn tab, tab mặc định.

## Khả năng truy cập

- `role="tablist"`, `role="tab"` với `aria-selected`, `aria-controls`; phím mũi tên chuyển tab.

## Class và token

`is-tabs`, `is-tab`, `is-subtabs`, `is-subtab` · token `primary`, `primary-soft`, `line`, `ink-muted`.
