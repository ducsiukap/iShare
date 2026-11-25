# Button

Nút bấm cho một hành động; nhãn là động từ rõ nghĩa, không có mũi tên ở cuối.

**Dùng khi:** người dùng thực hiện một việc: gửi, lưu, nhận xử lý, tham gia nhóm.

**Không dùng khi:** chỉ để đi tới trang khác (dùng Link) hoặc chỉ có icon (dùng IconButton).

## Biến thể và trạng thái

- **Chính** (`--primary`): tối đa một nút mỗi vùng, cho việc chính của màn hình: Đăng bài, Gửi khiếu nại, Nhận xử lý.
- **Phụ** (mặc định): việc phụ đứng cạnh nút chính: Lưu nháp, Hủy trong form.
- **Nhẹ** (`--ghost`): việc ít quan trọng trong dải nút: Hủy trong dialog, Bỏ qua.
- **Nguy hiểm** (`--danger`): việc không hoàn tác được: Ban, Xóa nhóm, Vô hiệu hóa tài khoản.
- Cỡ vừa (40px, mặc định) và nhỏ (`--sm`, 32px) cho bảng, bộ lọc khu quản trị và dòng thông báo.
- Trạng thái: mặc định, rê chuột, focus (vòng 2px `focus`, cách 2px), đang nhấn, tắt (`disabled`), đang xử lý (`aria-busy`, icon xoay, nhãn đổi thành dạng tiếp diễn).

## Cần cung cấp

- Nhãn tiếng Việt, viết hoa chữ đầu: "Đăng bài", không "ĐĂNG BÀI".
- Icon (tùy chọn) đặt trước nhãn, cỡ `icon-sm`.

## Khả năng truy cập

- Dùng `<button type="button">` (hoặc `submit` trong form); link điều hướng dùng `<a>`.
- Đang xử lý: `aria-busy="true"` và tắt bấm lại; nhãn mô tả việc đang làm.
- Nút tắt vẫn đọc được (chữ `ink-muted`); nếu tắt vì thiếu điều kiện, nói lý do cạnh nút.

## Class và token

`is-btn`, `is-btn--primary`, `is-btn--ghost`, `is-btn--danger`, `is-btn--sm` · token `primary`, `primary-hover`, `on-primary`, `danger`, `danger-hover`, `on-danger`, `line-strong`, `surface-hover`, `radius-sm`, `control-h`, `control-h-sm`.
