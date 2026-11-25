# Poll

Bình chọn đóng trong bài: chọn một hoặc nhiều, có hạn kết thúc (BR-M03-09…13).

**Dùng khi:** dưới nội dung bài có bình chọn.

**Không dùng khi:** khảo sát mở cho người đọc thêm lựa chọn — FR không có.

## Biến thể và trạng thái

- Chưa bình chọn: danh sách lựa chọn (checkbox khi chọn nhiều, radio khi chọn một), nút Bình chọn; kết quả ẩn nếu tác giả không bật "hiện kết quả trước khi bình chọn".
- Đã bình chọn: thanh kết quả với phần trăm và số phiếu, lựa chọn của mình có dấu kiểm và chữ "Bạn đã chọn".
- Đã đóng: nhãn "Đã kết thúc", chỉ còn kết quả.
- Tác giả: thêm nút Quản lý bình chọn (PollEditor).

## Cần cung cấp

- Câu hỏi (tiêu đề bài), lựa chọn 2–10, chế độ chọn một/nhiều, hạn kết thúc, số phiếu, lựa chọn của người xem.

## Khả năng truy cập

- `fieldset` + `legend`; thanh kết quả có chữ phần trăm, không chỉ dựa vào độ dài thanh.

## Class và token

`is-poll`, `is-poll__opt`, `is-poll__res`, `is-bar`, `is-bar__fill`, `is-poll__mine` · token `primary`, `surface-hover`, `line-strong`, `radius-full`.
