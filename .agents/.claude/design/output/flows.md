---
ma_tai_lieu: FLOWS
phien_ban: 0.3
trang_thai: Đã duyệt
ngay: 2026-11-27
tac_gia: Phạm Văn Đức
---
# Sơ đồ trang, điều hướng và luồng — iShare

[Vietnamese Doc] — Bước 5 của skill designing-ui. Mã màn hình theo `screen-inventory.md` (đã duyệt 2026-11-25). Chỉ
máy tính (DD-UI-02). Đường dẫn ghi "đã định" khi FR quy định, "đề xuất" khi theo quy tắc chung dưới đây (Q5-02: người
dùng đồng ý đề xuất, 2026-11-25).

Quy tắc đường dẫn đề xuất: chữ thường tiếng Anh ngắn, không dấu; đối tượng có trang riêng dùng tiền tố một chữ cái
(`/p/` bài, `/u/` người dùng, `/g/` nhóm); trạng thái cần chia sẻ (tab, bộ lọc, chu kỳ) nằm trong query string; khu
kiểm duyệt dùng `/mod/…` (Mod và Admin), khu chỉ Admin dùng `/admin/…`. Hộp thoại, ngăn trượt và popup không có đường
dẫn riêng.

## 1. Sơ đồ trang

| Đường dẫn | Màn hình | Vai trò truy cập | Nguồn | Ghi chú (đã định / đề xuất) |
|---|---|---|---|---|
| `/` | SCR-M14-01 Trang chủ | Mọi người | FR-M14-01 | đề xuất; tab: `/?tab=following\|group\|newest`, mục con Thịnh hành: `/?sub=topic\|tag` (mặc định Thịnh hành › Bài viết) |
| `/p/{id}` | SCR-M03-02 Chi tiết bài viết (+ SCR-M04-01 khu bình luận, SCR-M13-01 tóm tắt) | Mọi người theo quyền xem | FR-M03-07 | đề xuất; bình luận: `/p/{id}#c-{id}` |
| `/p/{id}/history` | SCR-M03-03 Lịch sử sửa bài | Người xem được bài | FR-M03-12 | đề xuất |
| `/write` | SCR-M03-01 Viết bài | Người dùng | FR-M03-01 | đề xuất; viết trong nhóm: `/write?group={id}`; mở nháp: `/p/{id}/edit` |
| `/p/{id}/edit` | SCR-M03-01 Sửa bài | Tác giả | FR-M03-11 | đề xuất |
| `/u/{username}` | SCR-M02-01 Hồ sơ người dùng | Mọi người | FR-M02-01.01 | **đã định**; tab chủ hồ sơ: `?tab=bookmark\|deleted` |
| `/profile/edit` | SCR-M02-03 Sửa hồ sơ | Chủ hồ sơ | FR-M02-03, SC-M02-003 | đề xuất |
| `/topics` | SCR-M05-01 Danh sách Chủ đề và Tag | Mọi người | FR-M05-04 | đề xuất; danh sách Tag: `/topics?tab=tag` |
| `/search` | SCR-M06-02 Kết quả tìm kiếm | Mọi người | FR-M06-02…04 | đề xuất; `?q=&topic=&tag=&time=today\|week\|month&following=1&sort=relevant\|newest\|upvote`. "Trang Chủ đề/Tag" = `/search?topic={id}` hoặc `?tag={name}` với `q` rỗng (SC-M06-003) |
| `/leaderboard` | SCR-M12-01 Bảng xếp hạng | Mọi người | FR-M12-06 | đề xuất; `?period=week\|month\|all&grade=10\|11\|12` |
| `/groups` | SCR-M11-01 Danh sách nhóm | Mọi người | FR-M11-03 | đề xuất |
| `/groups/new` | SCR-M11-02 Tạo nhóm | Người dùng | FR-M11-01 | đề xuất |
| `/g/{id}` | SCR-M11-03 Trang nhóm | Theo chế độ nhóm | FR-M11-03 | đề xuất; link mời: `/g/{id}?invite={mã}` |
| `/g/{id}/members` | SCR-M11-05 Thành viên nhóm | Theo quyền xem nhóm | FR-M11-03.14 | đề xuất |
| `/g/{id}/requests` | SCR-M11-06 Yêu cầu tham gia chờ duyệt | Owner, Group Mod | FR-M11-06 | đề xuất |
| `/g/{id}/blocked` | SCR-M11-11 Danh sách chặn tham gia | Owner, Group Mod | FR-M11-07 | đề xuất |
| `/g/{id}/queue` | SCR-M11-10 Hàng chờ duyệt bài của nhóm | Owner, Group Mod | FR-M11-13 | đề xuất |
| `/g/{id}/settings` | SCR-M11-08 Cài đặt nhóm | Owner | FR-M11-02 | đề xuất |
| `/notifications` | SCR-M07-02 Trang Thông báo | Người dùng | FR-M07-05.02 | đề xuất |
| `/messages` | SCR-M16-01 Hộp thư Chat | Người dùng | FR-M16-03 | đề xuất |
| `/messages/{id}` | SCR-M16-02 Cuộc trò chuyện (+ SCR-M16-04 thông tin nhóm chat ở ngăn phải) | Thành viên | FR-M16-04 | đề xuất |
| `/chat-invite/{mã}` | SCR-M16-05 Xin gia nhập nhóm chat | Người dùng | FR-M16-16 | đề xuất |
| `/settings` | SCR-M01-07 Cài đặt tài khoản (+ SCR-M08-05 mức cảnh cáo) | Người dùng | DD-UI-17 | đề xuất |
| `/appeals` | SCR-M09-02 Khiếu nại của tôi | Người dùng | FR-M09-02 | đề xuất; chi tiết: `/appeals/{id}` |
| `/appeals/new` | SCR-M09-01 Gửi khiếu nại | Người bị xử lý | FR-M09-01 | đề xuất; `?ref={mã xử lý}` |
| `/c/{id}` | SCR-M04-02 Xem lại bình luận đã bị xử lý | Tác giả bình luận | FR-M04-06 | đề xuất |
| `/register` | SCR-M01-01 Đăng ký bước 1 | Guest | FR-M01-01 | đề xuất |
| `/register/verify` | SCR-M01-02 Chờ xác minh email | Guest | FR-M01-02 | đề xuất; magic link: `/verify-email?token=…` |
| `/register/setup` | SCR-M01-03 Thiết lập tài khoản | Chủ tài khoản đã xác minh | FR-M01-03 | đề xuất |
| `/login` | SCR-M01-04 Đăng nhập | Guest | FR-M01-05 | đề xuất |
| `/forgot-password` | SCR-M01-05 Quên mật khẩu | Guest | FR-M01-09 | đề xuất |
| `/reset-password` | SCR-M01-06 Đặt mật khẩu mới | Người có link | FR-M01-09 | đề xuất; `?token=…` |
| `/reactivate` | SCR-M01-08 Kích hoạt lại tài khoản | Chủ tài khoản DEACTIVATED | FR-M01-11 ("trang kích hoạt riêng") | đề xuất |
| `/policy` | SCR-M01-09 Privacy Policy/ToS | Mọi người | FR-M01-15 | đề xuất |
| `/banned` | SCR-SHARED-05 Tài khoản bị khóa | Tài khoản BANNED | FR-M01-05 | đề xuất |
| `/mod/reports` | SCR-M08-02 Hàng chờ báo cáo | Mod, Admin | FR-M08-02 | đề xuất; chi tiết vụ: `/mod/reports/{id}` (SCR-M08-03) |
| `/mod/review` | SCR-M03-05 Hàng chờ duyệt bài | Mod, Admin | FR-M03-06 | đề xuất |
| `/mod/appeals` | SCR-M09-03 Hàng chờ khiếu nại | Mod, Admin | FR-M09-03 | đề xuất; chi tiết: `/mod/appeals/{id}` (SCR-M09-04) |
| `/mod/tags` | SCR-M05-04 Quản lý Tag | Mod, Admin | FR-M05-09 | đề xuất |
| `/mod/logs` | SCR-M08-06 Nhật ký kiểm duyệt | Mod (của mình), Admin | FR-M08-17 | đề xuất; `?actor={username}` |
| `/admin/users` | SCR-M10-01 Người dùng; SCR-M10-02 vai trò ở ngăn phải | Admin | FR-M10-01 | đề xuất |
| `/admin/topics` | SCR-M05-02 Quản lý Chủ đề | Admin | FR-M05-06 | đề xuất |
| `/admin/settings` | SCR-M10-04 Cấu hình hệ thống | Admin | FR-M10-09…12 | đề xuất |
| `/admin/banner` | SCR-M10-05 Banner toàn trang | Admin | FR-M10-13 | đề xuất |
| `/admin/logs` | SCR-M10-06 Nhật ký thao tác Admin | Admin | FR-M10-15 | đề xuất |
| `/admin/stats/users`, `/content`, `/moderation` | SCR-M15-01, -02, -03 Thống kê | Admin | FR-M15-01…03 | đề xuất; `?range=today\|7d\|30d\|all` |

Không có đường dẫn riêng (hiện trên trang đang mở): SCR-SHARED-01…04, SCR-M01-10 (đồng ý lại chính sách, chặn mọi
trang), SCR-M02-02, SCR-M03-04, SCR-M05-03, SCR-M05-05, SCR-M06-01, SCR-M07-01, SCR-M07-03, SCR-M08-01, SCR-M08-04,
SCR-M10-03, SCR-M11-04, SCR-M11-07, SCR-M11-09, SCR-M13-01, SCR-M16-03, SCR-M16-06.

## 2. Điều hướng

| Bối cảnh | Mô hình | Mục | DD-UI |
|---|---|---|---|
| Desktop — thanh trên cùng | Một hàng cố định đầu trang | Chữ "iShare" (về `/`) · ô tìm kiếm nằm giữa logo và nhóm nút (DD-UI-09) · Viết bài · chuông Thông báo · biểu tượng Tin nhắn có số chưa đọc · avatar → menu: Hồ sơ, Cài đặt tài khoản, Khiếu nại của tôi, Khu kiểm duyệt (Mod/Admin), Đăng xuất. Guest: Đăng nhập, Đăng ký thay cho chuông/tin nhắn/avatar | DD-UI-20 |
| Desktop — cột trái | Danh sách dọc 200px, mục đang xem tô nền nhạt | Trang chủ · Chủ đề · Nhóm · Bảng xếp hạng. Tin nhắn không lặp ở cột trái (đã có biểu tượng trên thanh trên cùng, FR-M07-07) | DD-UI-21 |
| Desktop — chân trang | Một dòng cuối cột menu (cột người dùng và cột quản trị) | "Chính sách và Điều khoản" → trang Privacy Policy/ToS (SC-M01-037) | DD-UI-21, DD-UI-43 |
| Mobile | Không áp dụng (DD-UI-02) | — | — |
| Khu quản trị | Khung riêng AdminShell: cột menu nền sẫm cao hết trang có logo "iShare", mỗi mục có icon; thanh trên chỉ có vị trí trang (nhóm › trang), "Về iShare", chuông Thông báo, avatar (không có ô tìm kiếm, Viết bài, Tin nhắn); nội dung trải hết bề ngang. Mod chỉ thấy nhóm Kiểm duyệt | Kiểm duyệt (Mod, Admin): Hàng chờ báo cáo, Hàng chờ duyệt bài, Hàng chờ khiếu nại, Quản lý Tag, Nhật ký kiểm duyệt. Quản trị (chỉ Admin): Người dùng, Chủ đề, Cấu hình hệ thống, Banner, Nhật ký Admin, Thống kê (Người dùng, Nội dung, Kiểm duyệt) | DD-UI-22, DD-UI-42 |
| Vị trí cố định | Thông báo, chat, báo cáo, khiếu nại | Thông báo: chuông → ngăn 10 thông báo, cuối ngăn "Xem tất cả" → `/notifications`. Chat: biểu tượng → `/messages`; popup tin mới góc dưới phải. Báo cáo: mục "Báo cáo" cuối thanh thao tác bài (DD-UI-10), trong menu "…" của bình luận, hồ sơ, trang nhóm. Khiếu nại: nút "Khiếu nại" trong thông báo xử lý, trên màn hình tài khoản bị khóa, và menu avatar → Khiếu nại của tôi | DD-UI-23 |
| Hộp thoại | Hộp giữa màn hình, nền mờ phía sau; đóng bằng Esc hoặc nút Đóng | Báo cáo, lý do biện pháp, tạo nhóm chat, thêm thành viên, gửi yêu cầu tham gia, mời vào nhóm, rời nhóm, đổi Chủ đề/Tag (Mod), gộp Chủ đề, người theo dõi, từ chức | DD-UI-24 |
| Ngăn bên phải | Ngăn trượt trong trang, không rời trang | Tóm tắt bài (SCR-M13-01), thông tin nhóm chat (SCR-M16-04), vai trò người dùng (SCR-M10-02) | DD-UI-24 |

## 3. Luồng

Wireframe: canvas "iShare — Khám phá" (https://claude.ai/artifact/K2ZxJDPyzjGKHCw8rZZKrs), trang "Bước 5 — Wireframe".
Mỗi màn hình vẽ một lần ở luồng đầu tiên nó xuất hiện; luồng sau dẫn lại tên artboard.

### 3.1 Đăng ký và xác minh email (M01)

Nguồn: SC-M01-001, SC-M01-007. Artboard: `wf--dang-ky--SCR-M01-01…04--desktop`.

| # | Màn hình | Người dùng | Hệ thống phản hồi | Bước SC | Rẽ nhánh / lối ra |
|---|---|---|---|---|---|
| 1 | SCR-M01-01 | Bấm Đăng ký trên thanh trên cùng | Mở bước 1: email, mật khẩu, ô đồng ý, liên kết chính sách, nút Google | SC-M01-001/M1–M2 | Chọn Google → bước 3 với tên từ Google (E-Google); tạm dừng đăng ký → báo `paused` |
| 2 | SCR-M01-01 | Nhập email, mật khẩu, tick đồng ý, Gửi | Tạo tài khoản, gửi magic link | M3–M4 | Lỗi nhập → `validation` tại chỗ; đọc chính sách → `/policy` (EP-REG-POLICY) |
| 3 | SCR-M01-02 | Mở email, bấm link | Xác minh, mở bước 3 | M5–M6 | Link hết hạn → `expired`, nút Gửi lại email |
| 4 | SCR-M01-03 | Nhập username, display_name, bỏ qua tùy chọn, Hoàn tất | Lưu, vào trang chủ | M7–M8 | Username trùng/sai dạng → `validation` |
| 5 | SCR-M01-04 | (Lần sau) đăng nhập | Theo trạng thái tài khoản: vào, về bước còn dở, khóa, kích hoạt lại | SC-M01-007/M1–M2 | BANNED → `/banned`; DEACTIVATED → `/reactivate`; chính sách mới → SCR-M01-10 |

### 3.2 Soạn bài → gửi → đã đăng / chờ duyệt / bị từ chối (M03)

Nguồn: SC-M03-001, SC-M03-004, SC-M03-006, SC-M13-001. Artboard: `wf--soan-bai--SCR-M03-01--desktop`,
`wf--soan-bai--SCR-M03-05--desktop`.

| # | Màn hình | Người dùng | Hệ thống phản hồi | Bước SC | Rẽ nhánh / lối ra |
|---|---|---|---|---|---|
| 1 | SCR-SHARED-01 → SCR-M03-01 | Bấm Viết bài | Mở trình soạn trống | SC-M03-001/M1–M2 | Mức cảnh cáo MEDIUM/HEAVY → `warned`, không lưu được |
| 2 | SCR-M03-01 | Nhập tiêu đề, nội dung có LaTeX, chọn Lớp 10, Chủ đề Toán học | Hiện công thức từ mã thô; đếm ký tự/từ | M3–M4 | Vượt 150 ký tự / 6.000 từ → cảnh báo ngay; Gợi ý chủ đề (AI bật) |
| 3 | SCR-M03-01 | Lưu nháp | Lưu nháp; nháp xem lại ở hồ sơ | M5–M6 | Thiếu mọi nội dung → `validation` |
| 4 | SCR-M03-01 | Gửi bài | AI bật: quét → Đã đăng / Chờ duyệt / Bị từ chối; AI tắt: Đã đăng ngay | SC-M03-004/M1–M4, SC-M13-001 | Đã đăng → `/p/{id}`; Chờ duyệt → SCR-M03-02 `pending`; Bị từ chối → `rejected`, sửa và gửi lại |
| 5 | SCR-M03-05 | (Mod) mở Hàng chờ duyệt bài, đọc bài, Chấp nhận | Bài sang Đã đăng, tác giả nhận thông báo | SC-M03-006/M1–M4 | Từ chối thiếu lý do → `validation` (E2) |

### 3.3 Đọc bài → bình luận, trả lời → upvote (M14, M03, M04, M12)

Nguồn: SC-M14-001, SC-M03-007, SC-M04-002, SC-M04-003, SC-M12-001. Artboard: `wf--doc-bai--SCR-M14-01--desktop`,
`wf--doc-bai--SCR-M03-02--desktop` (gồm khu bình luận SCR-M04-01).

| # | Màn hình | Người dùng | Hệ thống phản hồi | Bước SC | Rẽ nhánh / lối ra |
|---|---|---|---|---|---|
| 1 | SCR-M14-01 | Mở trang chủ | Tab Thịnh hành › Bài viết, 20 bài đầu | SC-M14-001/M1–M2 | Cuộn → tải thêm 20 bài |
| 2 | SCR-M03-02 | Bấm một bài | Mở bài, thanh thao tác, khu bình luận | SC-M03-007/M1–M2 | Bài không xem được → SCR-SHARED-04 |
| 3 | SCR-M03-02 | Bấm Upvote | Bật/tắt upvote, số cập nhật | SC-M12-001/M1–M2 | Guest → yêu cầu đăng nhập; bài của chính mình → nút tắt |
| 4 | SCR-M04-01 | Viết bình luận gốc có công thức, Gửi | Hiện bình luận ngay | SC-M04-002/M1–M4 | Bài khóa bình luận → `locked`; >1.000 từ → `validation` |
| 5 | SCR-M04-01 | Bấm Trả lời trên một bình luận, Gửi | Trả lời cấp 2 kèm dòng trích | SC-M04-003/M1–M4 | Bình luận gốc đã ẩn/xóa → chặn |

### 3.4 Báo cáo → Mod xử lý → khiếu nại (M08, M09)

Nguồn: SC-M08-001, SC-M08-004, SC-M08-010, SC-M09-001, SC-M09-005, SC-M09-002. Artboard:
`wf--bao-cao--SCR-M08-01…04--desktop`, `wf--bao-cao--SCR-SHARED-05--desktop`, `wf--bao-cao--SCR-M09-01…04--desktop`.

| # | Màn hình | Người dùng | Hệ thống phản hồi | Bước SC | Rẽ nhánh / lối ra |
|---|---|---|---|---|---|
| 1 | SCR-M03-02 → SCR-M08-01 | Bấm Báo cáo trên bài | Mở hộp báo cáo | SC-M08-001/M1–M2 | Báo cáo bình luận / người dùng / nhóm dùng cùng hộp |
| 2 | SCR-M08-01 | Chọn lý do, nhập mô tả, Gửi | Lưu, gộp vào vụ, báo đã gửi | M3–M4 | Thiếu lý do → `validation` |
| 3 | SCR-M08-02 | (Mod) mở Hàng chờ báo cáo, chọn vụ | Mở chi tiết vụ | SC-M08-004/M1–M2 | Vụ về chính mình / Mod khác → `forbidden` |
| 4 | SCR-M08-03 | Nhận xử lý | Mod thành người giữ | M3–M4 | Người khác giữ → `forbidden`; tự nhả sau 30 phút |
| 5 | SCR-M08-03 → SCR-M08-04 | Chọn biện pháp (ẩn, cảnh cáo, ban) và nhập lý do; kết luận | Áp biện pháp, đóng vụ, báo hai bên | M5–M6, SC-M08-010/M1–M2 | Thiếu lý do → `validation` |
| 6 | SCR-SHARED-05 | (Người bị ban) đăng nhập | Màn hình bị khóa, nút Khiếu nại | SC-M01-007, SC-M09-001/E | — |
| 7 | SCR-M09-01 | Bấm Khiếu nại, nhập lời giải thích, ảnh tùy chọn, Gửi | Lưu, báo đã gửi | SC-M09-001/M1–M4 | Hết hạn / đã khiếu nại → `forbidden` |
| 8 | SCR-M09-03 → SCR-M09-04 | (Mod) chọn hồ sơ, Nhận xử lý, Chấp nhận + lý do | Lật xử lý, báo người khiếu nại | SC-M09-005/M1–M6 | Từ chối thiếu lý do → `validation` |
| 9 | SCR-M09-02 | (Người khiếu nại) xem kết quả | Kết luận và lý do | SC-M09-002/M1–M2 | — |

### 3.5 Tìm và tham gia nhóm, đăng bài ẩn danh (M11)

Nguồn: SC-M11-004, SC-M11-005, SC-M11-007, SC-M11-018, SC-M11-021. Artboard: `wf--nhom--SCR-M11-01--desktop`,
`wf--nhom--SCR-M11-03--desktop`, `wf--nhom--SCR-M11-04--desktop`, `wf--nhom--SCR-M11-10--desktop`.

| # | Màn hình | Người dùng | Hệ thống phản hồi | Bước SC | Rẽ nhánh / lối ra |
|---|---|---|---|---|---|
| 1 | SCR-M11-01 | Mở Nhóm ở cột trái | Danh sách nhóm Public + Private của mình | SC-M11-004/M1–M2 | Cờ Group tắt → "Hệ thống đang bận, vui lòng thử lại sau" |
| 2 | SCR-M11-03 | Mở một nhóm | Tên, mô tả, bài của nhóm | SC-M11-005/M1–M2 | Private, người ngoài → chỉ tên, mô tả |
| 3 | SCR-M11-03 → SCR-M11-04 | Tham gia | Public không câu hỏi: vào ngay; có câu hỏi / Private: hộp yêu cầu | SC-M11-007/M1–M2 | Bị chặn → `forbidden`; chờ duyệt → `pending`, Rút yêu cầu |
| 4 | SCR-M03-01 | (Thành viên) Đăng bài trong nhóm, bật Đăng ẩn danh | Qua cổng duyệt của nhóm | SC-M11-018/M1–M4 | Duyệt trước bật → Chờ duyệt |
| 5 | SCR-M11-10 | (Owner/Group Mod) nhận bài, Chấp nhận | Bài đăng trong nhóm, hiện "Ẩn danh" | SC-M11-021/M1–M2 | Từ chối kèm lý do |

### 3.6 Nhận thông báo → đi tới nội dung (M07)

Nguồn: SC-M07-003, SC-M07-004, SC-M07-006. Artboard: `wf--thong-bao--SCR-M07-01--desktop`,
`wf--thong-bao--SCR-M07-02--desktop`.

| # | Màn hình | Người dùng | Hệ thống phản hồi | Bước SC | Rẽ nhánh / lối ra |
|---|---|---|---|---|---|
| 1 | SCR-M07-01 | Bấm chuông | Ngăn 10 thông báo gần nhất, đã đọc / chưa đọc | SC-M07-003/M1–M2 | Không có → `empty` |
| 2 | SCR-M07-01 → đích | Bấm một thông báo | Đánh dấu đã đọc, mở nội dung | SC-M07-004/M1–M2 | Đích không xem được → "Nội dung không tồn tại" |
| 3 | SCR-M07-02 | "Xem tất cả" | Trang Thông báo, tải 20 mỗi lần cuộn | SC-M07-003 | Đánh dấu tất cả đã đọc (SC-M07-005) |
| 4 | SCR-M07-02 | Chấp nhận / Từ chối trên thông báo đề xuất làm Mod | Ghi quyết định | SC-M07-006/M1–M2 | Đề xuất hết hạn → `expired` |

### 3.7 Chat 1-1 và nhóm chat (M16)

Nguồn: SC-M16-001, SC-M16-002, SC-M16-003, SC-M16-004, SC-M16-006. Artboard: `wf--chat--SCR-M16-01--desktop`,
`wf--chat--SCR-M16-02--desktop`, `wf--chat--SCR-M16-03--desktop`.

| # | Màn hình | Người dùng | Hệ thống phản hồi | Bước SC | Rẽ nhánh / lối ra |
|---|---|---|---|---|---|
| 1 | SCR-M02-01 → SCR-M16-02 | Bấm Nhắn tin trên hồ sơ | Mở (hoặc tạo) cuộc 1-1 | SC-M16-001/M1–M2 | Cờ Chat tắt → bận |
| 2 | SCR-M16-01 | Bấm biểu tượng Tin nhắn | Hộp thư, mới nhất trước, đánh dấu chưa đọc | SC-M16-002/M1–M2 | Không có → `empty` |
| 3 | SCR-M16-02 | Mở nhóm chat, cuộn lên đọc cũ | Tải 20 tin mỗi lần, giữ vị trí | SC-M16-003/M1–M6 | Tới tin đầu → dừng tải |
| 4 | SCR-M16-02 | Nhập, gửi tin | Tin hiện ngay, "Đã xem" ở tin mới nhất | SC-M16-004/M1–M2 | Quá dài → `validation`; thu hồi trong 5 phút |
| 5 | SCR-M16-01 → SCR-M16-03 | Tạo nhóm chat: tên, chọn thành viên | Tạo, mở nhóm mới | SC-M16-006/M1–M2 | <3 hoặc >100 thành viên → `validation` |

### 3.8 Tìm kiếm có bộ lọc (M06)

Nguồn: SC-M06-001, SC-M06-002, SC-M06-003. Artboard: `wf--tim-kiem--SCR-M06-01--desktop`,
`wf--tim-kiem--SCR-M06-02--desktop`.

| # | Màn hình | Người dùng | Hệ thống phản hồi | Bước SC | Rẽ nhánh / lối ra |
|---|---|---|---|---|---|
| 1 | SCR-M06-01 | Đặt con trỏ vào ô tìm kiếm | 10 truy vấn gần đây | SC-M06-004/M1–M2 | Xóa lịch sử (SC-M06-006) |
| 2 | SCR-M06-01 | Gõ "toan", dừng 300 ms | Gợi ý người dùng, Tag, Chủ đề, Nhóm | SC-M06-001/M1–M2 | Bấm một gợi ý → trang đó |
| 3 | SCR-M06-02 | Enter | Kết quả bài + kết quả phụ (tối đa 3 mỗi loại) | SC-M06-002/M1–M4 | Không có → `no-result` |
| 4 | SCR-M06-02 | Lọc Chủ đề = Toán học, đổi sắp xếp | Danh sách lọc lại | SC-M06-003/M1–M2 | Lọc đúng một Chủ đề → nút Theo dõi Chủ đề (DD-UI-16) |

## 4. Chỗ SC mơ hồ ảnh hưởng điều hướng

| # | Chỗ mơ hồ | Cách xử lý trong wireframe |
|---|---|---|
| 1 | Nguồn không nói Mod vào khu kiểm duyệt từ đâu | Mục "Khu kiểm duyệt" trong menu avatar (DD-UI-22) |
| 2 | Nguồn không quy định đường dẫn ngoài `/u/{username}` | Theo quy tắc đầu tệp (Q5-02) |

## 5. Lịch sử thay đổi

| Phiên bản | Ngày | Thay đổi |
|---|---|---|
| 0.1 | 2026-11-25 | Tạo tệp ở bước 5 |
| 0.2 | 2026-11-25 | Bước 5 được duyệt; điều hướng DD-UI-20…24, quy tắc đường dẫn DD-UI-26 |
| 0.3 | 2026-11-27 | Mục 2: khu quản trị dùng khung AdminShell (DD-UI-42); chữ chân cột menu "Chính sách và Điều khoản" (DD-UI-43). Bảng màn hình → đường dẫn cho phase Coding: `handoff/routes.md` |
