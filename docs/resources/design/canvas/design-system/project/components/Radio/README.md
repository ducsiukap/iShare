# Radio

Chọn đúng một trong vài lựa chọn luôn hiện.

**Dùng khi:** lý do báo cáo, Public/Private khi tạo nhóm, chọn một của bình chọn, hình thức ban.

**Không dùng khi:** nhiều hơn 6 lựa chọn (dùng Select) hoặc chuyển chế độ xem (dùng SegmentedControl, Tabs).

## Biến thể và trạng thái

- Chưa chọn, đã chọn, focus, tắt.
- Lựa chọn có giải thích: dòng phụ `caption` dưới nhãn.

## Cần cung cấp

- `fieldset` với `legend` là câu hỏi; mỗi lựa chọn một nhãn.

## Khả năng truy cập

- `<input type="radio">` cùng `name`; di chuyển bằng phím mũi tên.

## Class và token

`is-fieldset`, `is-check` · token `primary`.
