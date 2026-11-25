# LeaderboardRow

Một dòng bảng xếp hạng: thứ hạng, avatar, tên kèm username, dấu Ngôi sao tuần (chỉ tab Tuần), điểm trong chu kỳ (BR-M12-29).

**Dùng khi:** Bảng xếp hạng (SCR-M12-01), trình bày tiết chế (DD-UI-05): không cúp, không màu vàng bạc đồng.

**Không dùng khi:** danh sách người theo dõi (dùng UserRow).

## Biến thể và trạng thái

- Đồng hạng hiện cùng số; dòng của người đang xem nền `primary-soft`.
- Tài khoản đã xóa sau khi chốt: "[Người dùng đã xóa]", chữ `ink-muted` (BR-M12-21).

## Cần cung cấp

- Thứ hạng, tên hiển thị, username, điểm trong chu kỳ, có Ngôi sao tuần không.

## Khả năng truy cập

- Danh sách có thứ tự `<ol>`; điểm có chữ "điểm".

## Class và token

`is-rank`, `is-rank__n`, `is-rank__score`, `is-rank--me`, `is-rank--deleted`, `is-star` · token `primary-soft`, `primary`, `ink-muted`.
