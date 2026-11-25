# TextArea

Ô nhập nhiều dòng có bộ đếm khi FR giới hạn độ dài.

**Dùng khi:** bio (≤155 ký tự), mô tả báo cáo, lời giải thích khiếu nại, lý do biện pháp, nội dung banner (≤200 ký tự), câu hỏi tham gia nhóm.

**Không dùng khi:** soạn bài hay bình luận có định dạng (dùng trình soạn với EditorToolbar, CommentComposer).

## Biến thể và trạng thái

- Cùng trạng thái với TextField; cao tối thiểu 104px, kéo giãn theo chiều dọc.
- Bộ đếm đổi sang `danger` kèm chữ khi vượt giới hạn.

## Cần cung cấp

- Nhãn, giới hạn độ dài theo FR, câu lỗi của SC ("Vui lòng nhập lý do").

## Khả năng truy cập

- Bộ đếm có `aria-live="polite"` để đọc khi gần chạm giới hạn.

## Class và token

`is-field`, `is-input` (trên `textarea`), `is-field__count` · token như TextField.
