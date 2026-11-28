# TextField

Ô nhập một dòng có nhãn luôn hiện, gợi ý định dạng và lỗi nằm ngay dưới ô.

**Dùng khi:** nhập email, username, tên hiển thị, tiêu đề, mã kích hoạt, tên nhóm; biến thể mật khẩu và chỉ đọc có nút Sao chép (link mời nhóm).

**Không dùng khi:** nhập nhiều dòng (dùng TextArea) hoặc chọn trong danh sách cố định (Select, Radio).

## Biến thể và trạng thái

- Mặc định, rê chuột (viền `ink-muted`), focus (viền và vòng `focus`), lỗi (`aria-invalid`, viền `danger`, thông báo lỗi có icon), tắt, chỉ đọc (nền `bg`).
- Bộ đếm ký tự khi FR có giới hạn (username 3–20, tiêu đề ≤150).
- Mật khẩu: nút Hiện/Ẩn mật khẩu (QF-09); cho dán, `autocomplete` đúng loại.
- Chỉ đọc kèm nút Sao chép (link mời nhóm, link mời nhóm chat).
- Cỡ nhỏ `--sm` cho bộ lọc khu quản trị.

## Cần cung cấp

- Nhãn, gợi ý định dạng trước khi nhập, thông báo lỗi nói cách sửa (lấy đúng câu của SC).
- Ô bắt buộc ghi rõ "(bắt buộc)" hoặc ô tùy chọn ghi "(không bắt buộc)" — chọn một cách cho cả form.

## Khả năng truy cập

- `<label for>` gắn với ô; gợi ý và lỗi nối bằng `aria-describedby`.
- Không xóa dữ liệu đã nhập khi lỗi (QF-08).

## Class và token

`is-field`, `is-field__label`, `is-field__hint`, `is-field__error`, `is-field__count`, `is-input`, `is-inputwrap` · token `line-strong`, `focus`, `danger`, `ink-muted`, `bg`, `control-h`.
