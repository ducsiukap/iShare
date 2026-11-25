# Skeleton

Khung xám giữ chỗ trong lúc tải, cùng bố cục với nội dung thật để trang không nhảy.

**Dùng khi:** trạng thái `loading` của danh sách bài, bình luận, bảng, Tóm tắt, Thống kê.

**Không dùng khi:** thao tác đang chạy trên một nút (dùng Button `aria-busy`).

## Biến thể và trạng thái

- Dòng chữ, tiêu đề, avatar, khối; nhấp nháy nhẹ 1,6 giây, đứng yên khi `prefers-reduced-motion`.

## Cần cung cấp

- Số dòng gần với nội dung thật (3 thẻ bài, 5 dòng bảng).

## Khả năng truy cập

- Vùng đang tải có `aria-busy="true"` và chữ ẩn "Đang tải…"; các khối `aria-hidden`.

## Class và token

`is-skel`, `is-skel--line`, `is-skel--title`, `is-skel--avatar` · token `surface-hover`, `radius-sm`, `avatar-md`.
