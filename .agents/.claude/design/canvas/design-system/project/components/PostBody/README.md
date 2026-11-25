# PostBody

Phần đầu và nội dung bài ở trang chi tiết: tiêu đề `display`, dòng tác giả, Chủ đề, Tag, rồi nội dung giàu định dạng theo BR-M03-03.

**Dùng khi:** trang Chi tiết bài viết, bản xem trước trong trình soạn, nội dung bài trong hàng chờ duyệt, Lịch sử sửa bài, trang Privacy Policy/ToS (chỉ phần nội dung).

**Không dùng khi:** trích đoạn trong danh sách (dùng PostCard).

## Biến thể và trạng thái

- Định dạng: đậm, nghiêng, gạch chân, gạch ngang, tô sáng (`mark`); tiêu đề mục H1–H3 (`post-h1/2/3`); danh sách chấm, số, việc cần làm; code trong dòng và khối code tô màu cú pháp (`syntax-*`, JetBrains Mono, tắt ký tự ghép); công thức KaTeX trong dòng và khối (1.1em, khối dài cuộn ngang); bảng (cuộn ngang trong khung); trích dẫn; đường kẻ ngang; liên kết có nhãn; @nhắc tên.
- Trạng thái trang (Bị ẩn, Chờ duyệt, Bị khóa bình luận, Ẩn danh) hiện bằng StatusLabel cạnh dòng tác giả và InlineAlert phía trên nội dung.

## Cần cung cấp

- HTML đã làm sạch từ trình soạn; LaTeX dạng mã để KaTeX dựng (bản preview tải KaTeX 0.16.11 từ jsDelivr).

## Khả năng truy cập

- Tiêu đề bài là `h1` của trang; H1–H3 trong bài là `h2`–`h4` để không nhảy cấp (QF-17).
- Bảng, công thức khối, khối code cuộn trong khung riêng, trang không cuộn ngang (QF-12, QF-14).

## Class và token

`is-post`, `is-post__title`, `is-prose`, `tok-k|s|n|f|c`, `is-mention` · token `body`, `post-h1`, `post-h2`, `post-h3`, `code`, `mark`, `syntax-*`, `primary-soft`, `bg`, `line`.
