# Pagination

Tải thêm cho danh sách của học sinh (cuộn tải 20 mục) và phân trang số cho bảng khu quản trị.

**Dùng khi:** trang chủ, kết quả tìm kiếm (tối đa 120), thông báo, bảng xếp hạng: Tải thêm; bảng quản trị: trang số.

**Không dùng khi:** danh sách ngắn hiện đủ một lần.

## Biến thể và trạng thái

- Tải thêm: nút phụ, đang tải (`aria-busy`), hết ("Đã hiện tất cả kết quả").
- Trang số: trang hiện tại `primary-soft`, nút trước/sau tắt ở đầu/cuối.

## Cần cung cấp

- Còn mục để tải không, trang hiện tại, tổng số trang.

## Khả năng truy cập

- Phân trang là `<nav aria-label="Phân trang">`; trang hiện tại `aria-current="page"`; khi tải thêm, đưa focus vào mục đầu tiên mới.

## Class và token

`is-more`, `is-pager`, `is-page` · token `primary-soft`, `primary`, `control-h-sm`.
