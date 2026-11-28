# DescriptionList

Danh sách cặp nhãn – giá trị, nhãn `ink-muted` bên trái, giá trị bên phải.

**Dùng khi:** thông tin bài, thông tin nhóm, chi tiết vụ báo cáo và khiếu nại, hồ sơ trong khu quản trị, cài đặt tài khoản.

**Không dùng khi:** dữ liệu nhiều cột so sánh được (dùng DataTable).

## Biến thể và trạng thái

- Cỡ chữ 14px; cột nhãn vừa nội dung, cột giá trị co giãn và xuống dòng.
- Biến thể `is-dl--stack` cho cột phụ hẹp (thông tin bài, cột Tác giả của vụ báo cáo): nhãn nằm trên giá trị, để ngày giờ và tên không bị tách dòng (QA-F-09).

## Cần cung cấp

- Các cặp nhãn – giá trị.

## Khả năng truy cập

- Dùng `<dl>`, `<dt>`, `<dd>` để trình đọc màn hình đọc đúng cặp.

## Class và token

`is-dl`, `is-dl--stack` · token `ink-muted`, `space-2`, `space-3`.
