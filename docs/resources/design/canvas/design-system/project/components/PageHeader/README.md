# PageHeader

Dòng tiêu đề: tiêu đề (kèm dòng phụ) bên trái, nút hoặc bộ chọn bên phải; xuống dòng khi hẹp.

**Dùng khi:** đầu mỗi trang (tiêu đề `is-h1` + dòng phụ + nút chính); đầu một khối hay khu vực trong trang (tiêu đề `is-h2` hoặc `is-label` + bộ sắp xếp, nhãn trạng thái).

**Không dùng khi:** tiêu đề trong bài viết (dùng kiểu chữ `post-h1/2/3` của PostBody).

## Biến thể và trạng thái

- Đầu trang: `is-h1` (26/700), dòng phụ `ink-muted`, nút căn đáy dòng.
- Đầu khu vực: `is-h2` (22/700) — ví dụ "5 bình luận" + SegmentedControl sắp xếp.
- Đầu khối nhỏ: `is-label` (15/600) — ví dụ "Mức hiện tại" + StatusLabel.

## Cần cung cấp

- Tiêu đề, dòng phụ (tùy chọn), hành động (tùy chọn).

## Khả năng truy cập

- Mỗi trang đúng một `h1`; tiêu đề khu vực dùng `h2`, không nhảy cấp.

## Class và token

`is-pagehead`, `is-h1`, `is-h2`, `is-label` · token `ink-muted`, `space-4`.
