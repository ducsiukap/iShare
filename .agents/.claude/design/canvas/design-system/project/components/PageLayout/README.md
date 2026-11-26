# PageLayout

Khung chia cột của một trang desktop, nằm dưới AppHeader. Mọi màn hình dùng một trong sáu biến thể này, nên khi lập trình chỉ dựng khung một lần.

**Dùng khi:** mọi trang. Ba cột (mặc định): chi tiết bài, trình soạn, kết quả tìm kiếm, hồ sơ. Hai cột (`--two`): trang chủ, Thông báo, lịch sử sửa bài, trang không có cột phụ. Quản trị (`--admin`, `--admin3` khi có cột phụ): vùng nội dung bên trong AdminShell của khu kiểm duyệt và quản trị. Chat (`--chat`): Tin nhắn. Giữa trang (`--center`): đăng ký, đăng nhập, mật khẩu, kích hoạt lại, bảo trì, đồng ý chính sách.

**Không dùng khi:** chia cột bên trong một khối (dùng `is-grid2`, `is-grid3`).

## Biến thể và trạng thái

- Ba cột: `nav-w` 200 · nội dung co giãn · `aside-w` 260; cách nhau `space-10`; đệm `space-8` hai bên, `space-16` dưới.
- Hai cột: nội dung tối đa `content-max` 820.
- Quản trị: nằm trong AdminShell (DD-UI-42), không có cột điều hướng riêng; nội dung trải hết bề ngang, SectionCard bỏ giới hạn 820px; `--admin3` thêm cột phụ `aside-w` 260.
- Chat: điều hướng · hộp thư `inbox-w` 340 · cuộc trò chuyện.
- Giữa trang: một khối ở giữa, đệm trên `space-16`; khối rộng `dialog-w` hoặc `content-max`.
- Không vỡ ở 1280px (DD-UI-02): cột nội dung co lại, hai cột bên giữ bề rộng.

## Cần cung cấp

- Biến thể; nội dung từng cột.

## Khả năng truy cập

- Cột nội dung là `<main>`, cột phụ là `<aside>`, điều hướng là `<nav>` có nhãn; thứ tự trong mã giống thứ tự đọc: điều hướng, nội dung, cột phụ.

## Class và token

`is-layout`, `is-layout--two`, `is-layout--admin`, `is-layout--admin3`, `is-layout--chat`, `is-layout--center`, `is-layout__main`, `is-layout__aside` · token `nav-w`, `nav-w-wide`, `aside-w`, `inbox-w`, `content-max`, `topbar-h`, `space-8`, `space-10`, `space-16`.
