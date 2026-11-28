# FileDrop

Vùng thêm tệp: có nút Chọn tệp, kéo-thả chỉ là cách thêm (QF-10).

**Dùng khi:** đính kèm ảnh, tài liệu vào bài; ảnh bằng chứng của báo cáo, khiếu nại.

**Không dùng khi:** chọn ảnh đại diện (dùng AvatarUpload).

## Biến thể và trạng thái

- Mặc định (viền nét đứt), đang kéo tệp vào (`is-dragover`, nền `primary-soft`), lỗi (viền `danger` + câu lỗi).
- Tệp đã thêm hiện bằng Attachment ngay dưới vùng, có nút gỡ.

## Cần cung cấp

- Giới hạn theo FR ngay trong vùng: ảnh JPEG/PNG/WebP ≤5 MB, tối đa 10 ảnh; tài liệu PDF/DOCX/XLSX/PPTX ≤20 MB, tối đa 3 tệp.
- Câu lỗi nói rõ tệp nào và vì sao ("anh-bai-tap.gif: chỉ nhận JPEG, PNG hoặc WebP").

## Khả năng truy cập

- Nút Chọn tệp là `<button>` mở `<input type="file">`; lỗi nối bằng `aria-describedby`.

## Class và token

`is-drop`, `is-drop.is-dragover`, `is-drop__ic` · token `line-strong`, `primary`, `primary-soft`, `danger`.
