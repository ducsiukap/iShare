# Select

Chọn một giá trị trong danh sách ngắn, cố định.

**Dùng khi:** Lớp/Khối (10, 11, 12, Chưa khai), sắp xếp (Liên quan / Mới nhất / Nhiều upvote nhất), lý do báo cáo trong bộ lọc.

**Không dùng khi:** dưới 4 lựa chọn cần thấy ngay (dùng Radio hoặc SegmentedControl) hoặc danh sách dài cần tìm (dùng Combobox).

## Biến thể và trạng thái

- Mặc định, focus, tắt; cỡ nhỏ `--sm` trong bộ lọc.
- Dùng `<select>` thật, mũi tên là icon trang trí.

## Cần cung cấp

- Nhãn và các lựa chọn bằng tiếng Việt; lựa chọn mặc định theo FR.

## Khả năng truy cập

- `<label for>`; mũi tên `aria-hidden`.

## Class và token

`is-selectwrap`, `is-input is-select` · token `line-strong`, `ink-muted`, `focus`.
