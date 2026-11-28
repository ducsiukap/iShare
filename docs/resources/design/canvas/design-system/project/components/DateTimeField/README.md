# DateTimeField

Chọn ngày và giờ, hiển thị theo giờ Việt Nam.

**Dùng khi:** hạn kết thúc bình chọn khi tạo và khi đổi hạn (FR-M03-03.07, FR-M03-09.01).

**Không dùng khi:** khoảng thời gian cố định của Thống kê (dùng SegmentedControl).

## Biến thể và trạng thái

- Mặc định, focus, lỗi (hạn trước thời điểm hiện tại), tắt (bình chọn đã đóng).
- Dùng ô `datetime-local` của trình duyệt; theme tối nhờ `color-scheme`.
- Ô gốc hiện ngày theo ngôn ngữ của trình duyệt; nếu cần cố định dd/mm/yyyy cho mọi máy, thay bằng bộ chọn ngày ở bước code nhưng giữ nhãn, gợi ý, lỗi như trên.

## Cần cung cấp

- Giá trị mặc định nếu FR có; câu lỗi của FR: "Hạn kết thúc phải sau thời điểm hiện tại".

## Khả năng truy cập

- `<label for>`; định dạng hiển thị dd/mm/yyyy, hh:mm nêu trong gợi ý.

## Class và token

`is-field`, `is-input` · token như TextField.
