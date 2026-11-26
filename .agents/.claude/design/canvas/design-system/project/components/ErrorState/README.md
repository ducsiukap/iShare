# ErrorState

Trang hoặc vùng báo lỗi: không tìm thấy, không có quyền, lỗi tải, hệ thống bận, bảo trì (SCR-SHARED-03, SCR-SHARED-04).

**Dùng khi:** khi không hiện được nội dung vì lỗi hoặc quyền.

**Không dùng khi:** danh sách trống bình thường (dùng EmptyState).

## Biến thể và trạng thái

- Không tìm thấy: "Nội dung không tồn tại" / "Người dùng không tồn tại".
- Không có quyền: nói vì sao (bài trong nhóm Private, chỉ Admin).
- Lỗi tải, hệ thống bận (cờ tính năng tắt): "Hệ thống đang bận, vui lòng thử lại sau" + Thử lại.
- Bảo trì: trang riêng, chỉ ADMIN dùng được hệ thống.
- Căn giữa vùng nội dung như EmptyState; nút dạng chữ: Button chữ chính (việc chính) và chữ phụ (việc phụ), không nền, không viền.

## Cần cung cấp

- Câu đúng như SC; hành động tiếp theo (Thử lại, Về trang chủ, Đăng nhập).

## Khả năng truy cập

- Tiêu đề `h1` khi là cả trang; trong vùng nhỏ dùng heading đúng cấp.

## Class và token

`is-errorpage`, `is-errorpage__code`, `is-errorpage__title`, `is-errorpage__text`, `is-errorpage__acts` · token `h1`, `ink-muted`.
