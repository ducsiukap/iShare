# SectionCard

Khối nền `surface`, viền `line` mảnh, bo `radius-sm`: gom một phần nội dung thành một tờ giấy trên nền trang (hướng "Sổ tay").

**Dùng khi:** khu bình luận, form trong trang (sửa hồ sơ, cài đặt), khối thông tin trong khu quản trị; bản gọn (`--compact`) cho các khối ở cột phụ: "Phân loại", "Gửi bài", "Thông tin bài", bộ lọc.

**Không dùng khi:** thẻ bài trong danh sách (dùng PostCard), hộp thoại (dùng Dialog), thông báo (dùng InlineAlert).

## Biến thể và trạng thái

- Thường: đệm `space-8`, rộng tối đa `content-max`.
- Gọn (`--compact`): đệm `space-5`, rộng theo cột chứa.
- Tiêu đề khối: PageHeader với `is-h2` (khối thường) hoặc `is-label` (khối gọn).

## Cần cung cấp

- Tiêu đề (tùy chọn) và nội dung.

## Khả năng truy cập

- Khối có tiêu đề nên là `<section aria-labelledby>`; khối chỉ để trang trí thì dùng `<div>`.

## Class và token

`is-card`, `is-card--compact` · token `surface`, `line`, `radius-sm`, `space-8`, `space-5`, `content-max`.
