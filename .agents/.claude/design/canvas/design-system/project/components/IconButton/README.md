# IconButton

Nút chỉ có icon, luôn kèm nhãn ẩn cho trình đọc màn hình.

**Dùng khi:** hành động quen thuộc ở vị trí cố định: chuông thông báo, tin nhắn, menu "…", đóng dialog, nút trên thanh soạn thảo.

**Không dùng khi:** hành động quan trọng hoặc lạ với người dùng — dùng Button có chữ.

## Biến thể và trạng thái

- Mặc định trong suốt, icon `ink-muted`; rê chuột nền `surface-hover`, icon `ink`.
- Đang bật hoặc đang mở (`aria-pressed`, `aria-expanded`): nền `primary-soft`, icon `primary`.
- Có số đếm (Counter) ở góc: chuông, tin nhắn.
- Cỡ vừa 40px, nhỏ 32px (thanh soạn thảo, thẻ Tag, dòng bảng); biến thể có viền `--outline`.

## Cần cung cấp

- `aria-label` bằng tiếng Việt mô tả việc: "Thông báo, 3 chưa đọc", "Thêm thao tác", "Đóng".

## Khả năng truy cập

- Vùng bấm tối thiểu 32×32 (QF-04).
- Số đếm nằm trong `aria-label`, không chỉ trong phần hiển thị.

## Class và token

`is-iconbtn`, `is-iconbtn--sm`, `is-iconbtn--outline` · token `ink-muted`, `surface-hover`, `primary-soft`, `primary`, `control-h`, `control-h-sm`.
