# Tag

Nhãn Tag của bài, viết có dấu # đứng trước, bấm mở Kết quả tìm kiếm lọc theo Tag đó.

**Dùng khi:** dưới tiêu đề bài, trong ô TagInput, danh sách Tag, chip bộ lọc đang áp dụng (có nút gỡ).

**Không dùng khi:** Chủ đề (dùng TopicChip) hoặc trạng thái (dùng StatusLabel).

## Biến thể và trạng thái

- Liên kết (rê chuột: viền `line-strong`, chữ `ink`), có nút gỡ, đã vô hiệu hóa (gạch ngang, chỉ thấy trong Quản lý Tag).

## Cần cung cấp

- Tên Tag có dấu #; đích liên kết `/search?tag=`.

## Khả năng truy cập

- Nút gỡ có `aria-label` "Gỡ Tag #…".

## Class và token

`is-tag`, `is-tag__x`, `is-tag--off` · token `line`, `line-strong`, `ink-muted`, `radius-sm`.
