# Dialog

Hộp thoại giữa màn hình, nền mờ phía sau, cho thao tác ngắn cần tập trung (DD-UI-24).

**Dùng khi:** Báo cáo, lý do biện pháp, tạo nhóm chat, thêm thành viên, gửi yêu cầu tham gia, mời vào nhóm, rời nhóm, đổi Chủ đề/Tag, gộp Chủ đề, người theo dõi, từ chức, tài khoản bị khóa khi đang dùng.

**Không dùng khi:** nội dung xem kèm trang (dùng Drawer) hoặc xác nhận mà SC không có — không tự thêm bước hỏi lại (SC-M03-014, SC-M04).

## Biến thể và trạng thái

- Thường (520px) và rộng (`content-max`) cho dialog có danh sách; tiêu đề `h3`, nút đóng, thân, chân với nút chính bên phải.
- Nguy hiểm: nút chính `--danger` (Rời nhóm khi là thành viên cuối, Ban).

## Cần cung cấp

- Tiêu đề nêu việc, nội dung form, nhãn nút là động từ.

## Khả năng truy cập

- `role="dialog"` `aria-modal="true"` `aria-labelledby`; giữ focus trong hộp, Esc đóng, trả focus về nút đã mở (QF-06).

## Class và token

`is-scrim`, `is-dialog`, `is-dialog__head`, `is-dialog__title`, `is-dialog__body`, `is-dialog__foot` · token `scrim`, `surface-raised`, `shadow-2`, `dialog-w`.
