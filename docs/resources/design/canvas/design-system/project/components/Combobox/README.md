# Combobox

Ô gõ kèm danh sách gợi ý thả xuống; chọn bằng chuột hoặc phím mũi tên.

**Dùng khi:** gợi ý khi gõ ở ô tìm kiếm (người dùng, Tag, Chủ đề, nhóm + 10 truy vấn gần nhất), @nhắc tên trong trình soạn, mời vào nhóm, thêm thành viên nhóm chat, gõ Tag.

**Không dùng khi:** danh sách ngắn cố định (dùng Select).

## Biến thể và trạng thái

- Lịch sử (ô trống): 10 truy vấn gần nhất, nút "Xóa toàn bộ".
- Gợi ý theo nhóm (Người dùng, Tag, Chủ đề, Nhóm), phần khớp in đậm; mục đang trỏ nền `surface-hover`.
- Không có kết quả: một dòng "Không có gợi ý cho …"; lỗi giới hạn tần suất: dòng lỗi `danger`.

## Cần cung cấp

- Danh sách gợi ý theo FR-M06; mỗi mục có icon hoặc avatar nhận diện loại.

## Khả năng truy cập

- Mẫu combobox ARIA: ô `role="combobox"` `aria-expanded` `aria-controls`, danh sách `role="listbox"`, mục `role="option"` với `aria-selected`; Esc đóng.

## Class và token

`is-pop`, `is-pop__group`, `is-opt`, `is-opt__ic`, `is-opt__sub` · token `surface-raised`, `shadow-1`, `surface-hover`, `ink-muted`.
