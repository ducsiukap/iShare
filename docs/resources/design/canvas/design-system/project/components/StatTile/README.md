# StatTile

Ô một chỉ số: nhãn, con số lớn, dòng phụ.

**Dùng khi:** trang Thống kê (M15): số tài khoản theo trạng thái, vai trò, Lớp/Khối, mức cảnh cáo; số bài theo trạng thái; số báo cáo, khiếu nại theo nhóm.

**Không dùng khi:** trang của học sinh — không đặt dải thống kê trang trí (AP-24).

## Biến thể và trạng thái

- Lưới 3 cột; nhóm 0 hiện "0" (FR-M15-01.11); không có dữ liệu cho tỷ lệ: "Chưa có dữ liệu" thay phần trăm (FR-M15-02.08).
- Đang tải: Skeleton cùng kích thước.

## Cần cung cấp

- Nhãn đúng thuật ngữ FR, giá trị (định dạng số Việt Nam: 1.284), dòng phụ (khoảng thời gian).

## Khả năng truy cập

- Nhóm ô là danh sách định nghĩa hoặc `role="group"` có nhãn; con số không chỉ thể hiện bằng màu.

## Class và token

`is-tiles`, `is-tile`, `is-tile__label`, `is-tile__value`, `is-tile__sub` · token `h1` (con số 26px), `ink-muted`, `line`.
