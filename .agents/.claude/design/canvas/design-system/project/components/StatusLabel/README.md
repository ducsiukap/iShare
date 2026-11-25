# StatusLabel

Nhãn trạng thái nghiệp vụ, luôn có chữ (và icon khi có) — không bao giờ chỉ là một chấm màu (QF-03).

**Dùng khi:** trạng thái bài (Chờ duyệt, Bị từ chối, Bị ẩn, Tự ẩn, Bình luận đã khóa), bài/bình luận Bị gắn cờ, nhãn tài khoản (Tài khoản đã bị khóa, Tài khoản tạm thời vô hiệu hoá), vai trò (Mod, Admin, Tác giả), trạng thái vụ và khiếu nại.

**Không dùng khi:** huy hiệu thành tích (dùng Badge) hoặc Tag, Chủ đề.

## Biến thể và trạng thái

- `--success`: Đã đăng, Đã xử lý, Chấp nhận.
- `--warning`: Chờ duyệt, Chờ xét, cảnh cáo LIGHT/MEDIUM.
- `--danger`: Bị từ chối, Bị gắn cờ, Tài khoản đã bị khóa, HEAVY.
- `--info`: vai trò Mod, Admin, ADMIN gốc.
- Trung tính (mặc định): Bị ẩn, Tự ẩn, Bình luận đã khóa, Ẩn danh, Tác giả, Nháp.
- `--plain`: chỉ chữ và icon, không nền — trong dòng meta.

## Cần cung cấp

- Chữ đúng thuật ngữ của FR; icon theo nghĩa (schedule, block, visibility_off, lock, flag, shield_person).

## Khả năng truy cập

- Icon `aria-hidden`; chữ đọc được trên nền nhạt ở cả hai theme (≥ 4.5:1).

## Class và token

`is-status`, `is-status--success|warning|danger|info|plain` · token `success`, `warning`, `danger`, `info` và `*-soft`, `surface-hover`, `ink-muted`, `icon-xs`.
