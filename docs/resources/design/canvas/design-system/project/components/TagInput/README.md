# TagInput

Chọn nhiều giá trị thành chip trong một ô: Tag (gõ tự do, có gợi ý) hoặc Chủ đề (chọn trong danh mục, có gợi ý của AI).

**Dùng khi:** gắn Tag (≤5) và Chủ đề (1–3) khi viết bài, khi Mod đổi Chủ đề/Tag; chọn thành viên khi tạo nhóm chat.

**Không dùng khi:** chọn một giá trị (dùng Select hoặc Combobox).

## Biến thể và trạng thái

- Chế độ Tag: chip Tag có nút gỡ, ô gõ còn lại; gõ ra danh sách gợi ý (Combobox).
- Chế độ Chủ đề: chip TopicChip; dòng "Gợi ý chủ đề" với chip nét đứt bấm để thêm — ẩn khi AI tắt (FR-M05).
- Đã đủ số lượng: ô gõ tắt, gợi ý "Đã đủ 5 Tag"; lỗi thiếu Chủ đề: viền `danger` + câu lỗi.
- Chip không rộng quá ô; tên dài ("Khoa học tự nhiên (Lý/Hóa/Sinh)") xuống dòng trong chip, không tràn ô (QA-F-02).

## Cần cung cấp

- Danh sách đã chọn, giới hạn theo FR, nguồn gợi ý.

## Khả năng truy cập

- Mỗi chip có nút gỡ với `aria-label` "Gỡ Tag #daiso"; Backspace ở ô trống gỡ chip cuối.

## Class và token

`is-taginput`, `is-tag`, `is-tag__x`, `is-topic`, `is-topic--suggest` · token `line-strong`, `focus`, `primary`, `primary-soft`, `danger`.
