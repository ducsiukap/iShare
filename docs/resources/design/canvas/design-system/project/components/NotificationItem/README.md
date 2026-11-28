# NotificationItem

Một thông báo: ai hoặc hệ thống, việc gì, lúc nào; bấm đi tới nội dung (FR-M07).

**Dùng khi:** ngăn thông báo (Popover, 10 mục gần nhất) và trang Thông báo (tải thêm 20).

**Không dùng khi:** thông báo tức thời sau thao tác của chính người dùng (dùng Toast).

## Biến thể và trạng thái

- Chưa đọc: chữ đậm 600 + chấm `primary` có nhãn "Chưa đọc"; đã đọc: chữ thường.
- Thông báo của hệ thống (kiểm duyệt, huy hiệu): ô icon trung tính thay avatar.
- Đề xuất làm Mod/Admin: hai nút Chấp nhận / Từ chối ngay trên dòng; hết hạn: chữ "Đề xuất đã hết hạn" thay nút (SCR-M07-02).
- Thông báo xử lý (cảnh cáo, ẩn bài): giọng tôn trọng, có lý do và nút Khiếu nại khi được phép (PRODUCT.md mục 8).

## Cần cung cấp

- Chủ thể, hành động, đối tượng, thời điểm, đã đọc chưa, đích liên kết.

## Khả năng truy cập

- Mỗi thông báo là một liên kết; nút trong dòng không lồng trong liên kết (dòng có nút dùng `div`).

## Class và token

`is-noti`, `is-noti--unread`, `is-noti__ic`, `is-noti__text`, `is-noti__time`, `is-noti__acts`, `is-dot` · token `primary`, `surface-hover`, `ink-muted`.
