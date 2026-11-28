# GoogleButton

Nút đăng ký hoặc đăng nhập bằng tài khoản Google (FR-M01).

**Dùng khi:** màn hình Đăng ký (SCR-M01-01) và Đăng nhập (SCR-M01-04), đặt trên form email.

**Không dùng khi:** liên kết tài khoản trong Cài đặt — FR không có thao tác này.

## Biến thể và trạng thái

- Dáng nút phụ (nền `surface`, viền `line-strong`) với logo chữ G bốn màu của Google, không đổi màu logo.
- Nhãn: "Tiếp tục với Google" ở cả hai màn hình (Google tự liên kết tài khoản cùng email, FR-M01).
- Đang chuyển sang Google: `aria-busy`, icon xoay thay logo.

## Cần cung cấp

- Logo lấy từ `assets/Google/google-g.svg`; giữ đúng tỉ lệ, cỡ 20px, có khoảng trống quanh logo.
- Theo hướng dẫn thương hiệu của Google Identity; nếu triển khai bằng nút do Google cung cấp thì dùng nút đó thay cho component này.

## Khả năng truy cập

- Logo có `alt=""` vì nhãn đã nói đủ.

## Class và token

`is-btn`, `is-btn--block`, `is-btn__logo` · token `surface`, `line-strong`, `ink`, `control-h`.
