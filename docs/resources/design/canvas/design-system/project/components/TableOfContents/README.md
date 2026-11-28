# TableOfContents

Mục lục "Trong bài này" ở cột phụ: các tiêu đề của bài, mục đang đọc tô màu chủ đạo.

**Dùng khi:** chi tiết bài có từ hai tiêu đề trở lên; trang Privacy Policy/ToS.

**Không dùng khi:** điều hướng giữa các trang (dùng NavBar, Tabs).

## Biến thể và trạng thái

- Mục thường `ink-muted`; rê chuột `ink`; mục đang đọc `primary`, đậm 600 (`aria-current="true"`).
- Vạch trái `line-strong` 1px nối các mục.

## Cần cung cấp

- Danh sách tiêu đề và mục đang đọc.

## Khả năng truy cập

- Đặt trong `<nav aria-label="Trong bài này">`; mỗi mục là liên kết tới tiêu đề trong bài.

## Class và token

`is-toc` · token `ink-muted`, `ink`, `primary`, `line-strong`.
