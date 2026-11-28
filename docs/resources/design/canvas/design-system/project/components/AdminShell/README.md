# AdminShell

Khung riêng của khu kiểm duyệt và quản trị (DD-UI-42): cột menu nền sẫm cao hết trang có logo "iShare", thanh trên riêng chỉ có vị trí trang và vài nút, nội dung trải hết bề ngang cho bảng. Nhìn vào là biết đang ở khu quản trị, khác trang học sinh.

**Dùng khi:** mọi màn hình của Mod và Admin trong khu kiểm duyệt và quản trị: các hàng chờ, chi tiết vụ báo cáo, chi tiết khiếu nại, Quản lý Tag, Nhật ký kiểm duyệt, Người dùng, Vai trò, Chủ đề, Cấu hình hệ thống, Banner, Nhật ký Admin, Thống kê.

**Không dùng khi:** màn hình phía người dùng, kể cả khi người xem là Mod hay Admin (dùng AppHeader + NavBar): trang bài viết với hộp thoại đổi Chủ đề, Tag; Mức cảnh cáo của tôi; Gửi khiếu nại; Khiếu nại của tôi.

## Biến thể và trạng thái

- **Admin:** menu có hai nhóm Kiểm duyệt và Quản trị.
- **Mod:** menu chỉ có nhóm Kiểm duyệt.
- Cột menu: rộng `nav-w-wide` 240px, nền `console-bg`, viền phải `console-line`; ô logo cao `topbar-h`, chữ "i" `console-ink`, "Share" `console-accent`; menu là NavBar `--console`.
- Thanh trên: cao `topbar-h`, nền `surface`; trái là vị trí trang (nhóm › trang đang xem, chữ 14px); phải là "Về iShare" (Button ghost, là liên kết), chuông Thông báo, avatar mở menu tài khoản. Không có ô tìm kiếm, Viết bài, Tin nhắn.
- Vùng nội dung: PageLayout `--admin` (một cột) hoặc `--admin3` (thêm cột phụ 260px); banner toàn trang (nếu có) nằm ngay dưới thanh.
- Cột menu kéo dài hết chiều cao trang; mật độ gọn của khu quản trị giữ theo DD-UI-30.

## Cần cung cấp

- Vai trò người xem (Mod hoặc Admin), mục đang xem và nhóm của nó, tên và chữ cái đầu người xem.

## Khả năng truy cập

- Cột menu là `<nav>` nhãn "Khu kiểm duyệt", mục đang xem `aria-current="page"`; vị trí trang là `<nav>` nhãn "Vị trí trang" chứa `<ol>`; thanh là `<header>`, nội dung là `<main>`.
- Vòng focus trên cột menu dùng `console-accent` để vẫn thấy trên nền sẫm (≥ 3:1).

## Class và token

`is-console`, `is-console__side`, `is-console__brand`, `is-console__body`, `is-console__bar`, `is-console__where`, `is-console__crumb`, `is-console__end`, `is-nav--console` · token `console-bg`, `console-hover`, `console-active`, `console-ink`, `console-ink-muted`, `console-accent`, `console-line`, `nav-w-wide`, `topbar-h`, `surface`, `line`.
