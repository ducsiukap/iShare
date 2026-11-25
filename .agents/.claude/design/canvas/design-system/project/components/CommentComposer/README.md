# CommentComposer

Ô soạn bình luận, trả lời và tin nhắn chat.

**Dùng khi:** cuối khu bình luận, dưới bình luận khi bấm Trả lời (có dòng trích), sửa bình luận; biến thể chat ở chân cuộc trò chuyện.

**Không dùng khi:** soạn bài (trình soạn đầy đủ với EditorToolbar bài viết).

## Biến thể và trạng thái

- Bình luận: avatar người xem, ô nhập, thanh định dạng tối giản, bộ đếm từ (≤1.000 từ), nút Gửi.
- Trả lời: dòng trích "Trả lời Trần Minh Đức: …" và nút Hủy.
- Lỗi: vượt 1.000 từ (bộ đếm `danger`, Gửi tắt).
- Guest, bình luận đã khóa, tài khoản bị khóa: thay ô bằng một dòng giải thích (+ Đăng nhập cho Guest).
- Chat: ô nhiều dòng + nút gửi chỉ icon; Enter gửi, Shift+Enter xuống dòng.

## Cần cung cấp

- Người xem, đối tượng trả lời, giới hạn từ.

## Khả năng truy cập

- Ô có nhãn (ẩn) "Viết bình luận"; bộ đếm `aria-live`; nút Gửi có chữ (bản chat có `aria-label`).

## Class và token

`is-composer`, `is-composer__box`, `is-composer__text`, `is-composer__bar`, `is-chatbox` · token `line-strong`, `focus`, `danger`, `body-comment`.
