# GroupCard

Thẻ một nhóm: Public/Private, tên, mô tả 2 dòng, số thành viên, nút tham gia theo trạng thái.

**Dùng khi:** Danh sách nhóm (SCR-M11-01), kết quả phụ "Nhóm" của trang tìm kiếm.

**Không dùng khi:** trang nhóm (đầu trang nhóm dựng từ cùng thành phần nhưng rộng hơn).

## Biến thể và trạng thái

- Nút theo quan hệ: Tham gia (Public), Gửi yêu cầu (Private), Rút yêu cầu (đang chờ), Đã tham gia (thành viên, mở menu Rời nhóm).
- Nhóm bị Mod khóa: StatusLabel "Bị khóa", không có nút tham gia.

## Cần cung cấp

- Tên, mô tả, Public/Private, số thành viên, quan hệ của người xem.

## Khả năng truy cập

- Thẻ là `<article>` có `h3`; nút nói rõ việc ("Gửi yêu cầu tham gia CLB Toán").

## Class và token

`is-group`, `is-group__name`, `is-group__desc`, `is-group__foot` · token `surface`, `line`, `radius-sm`.
