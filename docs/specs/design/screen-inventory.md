---
ma_tai_lieu: SCREEN-INVENTORY
phien_ban: 1.0
trang_thai: Đã chốt
ngay: 2026-11-28
tac_gia: Phạm Văn Đức
---
# Danh mục màn hình — iShare

[Vietnamese Doc] — Hợp đồng của bước 5, 7, 8. Các bảng có marker `<!-- ui:… -->` được `check_inventory.py` đọc: giữ
đúng tên cột. Nhiều giá trị trong một ô cách nhau bằng dấu phẩy. Slug trạng thái theo `CONVENTIONS.md` mục 4.

## 1. Tóm tắt

Chỉ máy tính (DD-UI-02). Số artboard dự kiến = tổng số trạng thái của các màn hình, bản sáng, desktop 1440. Bản tối
(DD-UI-15): một artboard `--dark` cho trạng thái `default` của mỗi màn hình — cột "+ bản tối chỉ cho `default`" là số
chốt (tổng 356). Vẽ hết mọi màn hình trong danh mục, không để màn hình nào sau MS1 (DD-UI-14).

| Module | Số màn hình | Số artboard dự kiến (sáng) |
|---|---|---|
| SHARED | 6 | 13 |
| M01 | 10 | 29 |
| M02 | 3 | 17 |
| M03 | 5 | 33 |
| M04 | 2 | 13 |
| M05 | 5 | 11 |
| M06 | 2 | 10 |
| M07 | 3 | 10 |
| M08 | 6 | 22 |
| M09 | 4 | 18 |
| M10 | 6 | 16 |
| M11 | 11 | 41 |
| M12 | 1 | 5 |
| M13 | 1 | 3 |
| M14 | 1 | 6 |
| M15 | 3 | 9 |
| M16 | 6 | 25 |
| **Tổng** | **75** | **281** |

| Đợt | Số màn hình | Số artboard (sáng) | + bản tối chỉ cho `default` | + bản tối cho mọi trạng thái |
|---|---|---|---|---|
| A — Đọc và viết | 11 | 59 | 70 | 118 |
| B — Con người | 4 | 22 | 26 | 44 |
| C — Kiểm duyệt và quản trị | 27 | 84 | 111 | 168 |
| D — Cộng đồng và liên lạc | 20 | 76 | 96 | 152 |
| E — Vào hệ thống và tìm kiếm | 13 | 40 | 53 | 80 |
| **Tổng** | **75** | **281** | **356** | **562** |

## 2. Màn hình

Cột: `id` (SCR-Mxx-nn / SCR-SHARED-nn) · `name` · `module` (Mxx hoặc SHARED) · `roles` · `uc` · `sc` · `sources`
(FR/BR) · `states` · `devices` (desktop, mobile) · `batch` (A–E) · `notes`.

Vai trò (US `uc:actors`): ACT-001 Guest · ACT-002 Người dùng đã đăng nhập · ACT-003 Mod/Admin · ACT-007 Admin · ACT-008 Mod · ACT-009 Thành viên nhóm · ACT-010 Group Mod · ACT-011 Owner nhóm · ACT-012 Thành viên cuộc trò chuyện · ACT-013 Admin nhóm chat · ACT-014 Thành viên cũ nhóm chat.

<!-- ui:screens -->
| id | name | module | roles | uc | sc | sources | states | devices | batch | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| SCR-SHARED-01 | Khung ứng dụng (thanh trên cùng, điều hướng trái, menu tài khoản) | SHARED | ACT-001, ACT-002, ACT-003 | UC-M01-006, UC-M01-021, UC-M01-013 | SC-M01-014, SC-M01-037 | FR-M01-07, FR-M07-05, FR-M07-07, FR-M10-13 | default, guest, mod, admin | desktop | A | Logo chữ iShare, ô tìm kiếm (SCR-M06-01), nút Viết bài, chuông (SCR-M07-01), biểu tượng Tin nhắn có số chưa đọc (SCR-M07-03), avatar → menu: Hồ sơ, Cài đặt tài khoản, Đăng xuất. Guest: nút Đăng nhập/Đăng ký. Mod/Admin: thêm lối vào khung quản trị (SCR-SHARED-06). Chân cột menu có liên kết "Chính sách và Điều khoản" tới trang Privacy Policy/ToS (SC-M01-037, DD-UI-43). |
| SCR-SHARED-02 | Banner thông báo toàn trang | SHARED | ACT-001, ACT-002, ACT-003 | UC-M10-017 | SC-M10-014 | FR-M10-13 | default, long | desktop | A | Nằm trên mọi trang, dưới thanh trên cùng; có nút đóng. |
| SCR-SHARED-03 | Trang bảo trì | SHARED | ACT-001, ACT-002, ACT-008 | UC-M10-011 | SC-M10-009 | FR-M10-10 | default | desktop | E | Khi bật bảo trì (maintenance) chỉ tài khoản ADMIN dùng được hệ thống; default chính là trang bảo trì. |
| SCR-SHARED-04 | Trang lỗi chung | SHARED | ACT-001, ACT-002, ACT-003 | — | SC-M02-001, SC-M03-007 | FR-M02-01.21, FR-M03-07, FR-M11-03.06 | default, forbidden, error | desktop | A | default = không tìm thấy (not-found): "Người dùng không tồn tại", "Nội dung không tồn tại", không có quyền, lỗi tải. Khi cờ Group/Chat/Gamification tắt dùng thông báo "Hệ thống đang bận, vui lòng thử lại sau" (trạng thái error). |
| SCR-SHARED-05 | Màn hình tài khoản bị khóa (ban) | SHARED | ACT-002 | UC-M01-018 | SC-M01-007, SC-M09-001, SC-M01-014 | FR-M01-05, FR-M09-01 | default | desktop | C | default = trạng thái banned. Tài khoản BANNED đăng nhập: báo bị khóa, thời hạn, lối sang gửi khiếu nại (SCR-M09-01). Đang dùng mà tài khoản bị ban: báo bị khóa, bấm OK thì đăng xuất (SC-M01-014). Ban vĩnh viễn hoặc có thời hạn đều có lối khiếu nại. |
| SCR-SHARED-06 | Khung quản trị (Admin Panel, công cụ Mod) | SHARED | ACT-008, ACT-007 | UC-M10-020 | SC-M10-001 | FR-M10-01, FR-M08-02, FR-M09-03 | default, mod | desktop | C | default = Admin thấy đủ mục; mod = Mod chỉ thấy mục kiểm duyệt. Điều hướng riêng cho các màn hình M05 quản trị, M08, M09, M10, M15. Mod chỉ thấy mục kiểm duyệt; Admin thấy thêm người dùng, cấu hình, nhật ký Admin, thống kê. |
| SCR-M01-01 | Đăng ký (bước 1: email, mật khẩu, đồng ý chính sách) | M01 | ACT-001 | UC-M01-001, UC-M01-004, UC-M01-020 | SC-M01-001 | FR-M01-01, FR-M01-04, FR-M10-11 | default, validation, error, paused | desktop | E | Có nút đăng ký bằng Google. paused: Admin đang tạm dừng đăng ký (FR-M10-11). |
| SCR-M01-02 | Chờ xác minh email (bước 2) | M01 | ACT-001 | UC-M01-002, UC-M01-016 | SC-M01-001 | FR-M01-02 | default, expired, error | desktop | E | Magic link hạn 1 giờ; nút gửi lại email. |
| SCR-M01-03 | Thiết lập tài khoản (bước 3) | M01 | ACT-002 | UC-M01-003 | SC-M01-001 | FR-M01-03 | default, validation | desktop | E | Bắt buộc username (3–20 ký tự a–z, 0–9, _), display_name; bỏ qua được bio, Lớp/Khối, avatar. |
| SCR-M01-04 | Đăng nhập | M01 | ACT-001 | UC-M01-005, UC-M01-015, UC-M01-017, UC-M01-018 | SC-M01-007 | FR-M01-05, FR-M01-04 | default, validation, error | desktop | E | Email + mật khẩu, nút Google, lối sang quên mật khẩu và đăng ký. Theo nhánh của SC-M01-007: tài khoản chưa xong đăng ký → về bước xác minh (SCR-M01-02) hoặc thiết lập (SCR-M01-03); email chỉ có Google → nhắc đăng nhập bằng Google; DEACTIVATED → báo và dẫn sang trang kích hoạt lại; BANNED → SCR-SHARED-05; bảo trì → chỉ ADMIN vào được (SCR-SHARED-03); chính sách mới → SCR-M01-10. Đăng nhập Google tự liên kết tài khoản email cùng địa chỉ, không hỏi. |
| SCR-M01-05 | Quên mật khẩu | M01 | ACT-001 | UC-M01-008 | SC-M01-018 | FR-M01-09 | default, validation, submitted, banned | desktop | E | submitted: đã gửi magic link (hạn 15 phút). banned: tài khoản BANNED vẫn đặt lại được mật khẩu qua magic link, xong chỉ vào màn hình tài khoản bị khóa để khiếu nại (FR-M01-09.16, BF-M01-018; câu hỏi mở #6). |
| SCR-M01-06 | Đặt mật khẩu mới qua liên kết | M01 | ACT-001 | UC-M01-019 | SC-M01-018 | FR-M01-09 | default, validation, expired | desktop | E | — |
| SCR-M01-07 | Cài đặt tài khoản | M01 | ACT-002, ACT-003 | UC-M01-007, UC-M01-009, UC-M01-022, UC-M01-023 | SC-M01-017, SC-M01-022 | FR-M01-08, FR-M01-10, FR-M08-13, FR-M10-05 | default, validation, warned, mod | desktop | E | Gom: đổi mật khẩu, mức cảnh cáo của mình (SCR-M08-05), từ chức (Mod/Admin, SCR-M10-03), vô hiệu hóa tài khoản. FR không nói nơi đặt — xem câu hỏi mở #2. Vô hiệu hóa là một nút, SC-M01-022 không có bước xác nhận. |
| SCR-M01-08 | Kích hoạt lại tài khoản (trang riêng, nhập mã email) | M01 | ACT-001 | UC-M01-010 | SC-M01-023 | FR-M01-11 | default, validation, expired | desktop | E | — |
| SCR-M01-09 | Trang Privacy Policy/ToS | M01 | ACT-001, ACT-002, ACT-003 | UC-M01-013, UC-M01-024 | SC-M01-037 | FR-M01-15 | default, long | desktop | E | — |
| SCR-M01-10 | Đồng ý lại chính sách mới | M01 | ACT-002, ACT-003 | UC-M01-014 | SC-M01-039 | FR-M01-16 | default | desktop | E | Chặn dùng tiếp cho tới khi đồng ý phiên bản mới; từ chối thì chọn đăng xuất hoặc vô hiệu hóa tài khoản (SC-M01-039). |
| SCR-M02-01 | Hồ sơ người dùng (/u/{username}) | M02 | ACT-001, ACT-002, ACT-003 | UC-M02-001, UC-M02-007, UC-M02-008, UC-M02-010, UC-M02-030, UC-M07-001, UC-M07-002, UC-M12-009, UC-M12-010, UC-M12-022, UC-M03-016, UC-M08-012 | SC-M02-001, SC-M02-007, SC-M07-001, SC-M07-002, SC-M12-003, SC-M03-016, SC-M08-011 | FR-M02-01, FR-M02-07, FR-M07-01, FR-M12-07, FR-M03-16, FR-M08-15 | default, owner, visitor, guest, banned, not-found, empty, loading, long, mod | desktop | B | owner: nút Sửa hồ sơ, 3 tab Bài viết / Bookmark / Đã xóa (khôi phục bài). visitor: chỉ tab Bài viết, nút Theo dõi, Nhắn tin. Không hiện mức cảnh cáo, số stars. Bookmark không xem được hiện dòng "Nội dung không tồn tại". mod: Mod/Admin xem hồ sơ tài khoản đang bị ban có nút Gỡ ban (SC-M08-011: gỡ trực tiếp trên tài khoản, không qua vụ) — câu hỏi mở #3. Tab Bài viết của chủ hồ sơ có cả bài nháp, mở lại để soạn tiếp (SC-M03-001). |
| SCR-M02-02 | Người theo dõi / đang theo dõi (hộp thoại) | M02 | ACT-001, ACT-002, ACT-003 | UC-M02-002 | SC-M02-002 | FR-M02-02 | default, empty, guest, loading | desktop | B | Guest thấy hai con số nhưng phải đăng nhập mới mở danh sách. Hai tab Người theo dõi / Đang theo dõi (SC-M02-002). |
| SCR-M02-03 | Sửa hồ sơ (trang sửa) | M02 | ACT-002, ACT-003 | UC-M02-003, UC-M02-004, UC-M02-020 | SC-M02-003, SC-M02-004 | FR-M02-03, FR-M02-04, FR-M01-03 | default, validation, error | desktop | B | SC-M02-003: trang sửa gồm bio, Lớp/Khối, avatar, username, display_name. Bio ≤155 ký tự có bộ đếm; username 3–20 ký tự a–z, 0–9, _; avatar JPEG/PNG/WebP ≤5 MB, cắt tròn. |
| SCR-M03-01 | Viết bài / sửa bài (trình soạn) | M03 | ACT-002, ACT-003, ACT-009 | UC-M03-001, UC-M03-002, UC-M03-003, UC-M03-004, UC-M03-011, UC-M03-020, UC-M01-012, UC-M01-025, UC-M05-001, UC-M05-002, UC-M05-003, UC-M05-012, UC-M05-020, UC-M11-016, UC-M11-033 | SC-M03-001, SC-M03-004, SC-M03-011, SC-M05-001, SC-M05-002, SC-M01-034, SC-M11-018, SC-M13-001, SC-M13-005 | FR-M03-01, FR-M03-02, FR-M03-03, FR-M03-04, FR-M03-11, FR-M05-01, FR-M05-02, FR-M05-03, FR-M01-14, FR-M11-12 | default, validation, error, pending, rejected, warned, anonymous, long | desktop | A | Tiêu đề ≤150 ký tự, nội dung ≤6.000 từ có bộ đếm; LaTeX dạng mã; đính kèm ảnh/tài liệu; bình chọn; Lớp/Khối; Chủ đề 1–3 + Gợi ý chủ đề (ẩn khi AI tắt); Tag ≤5; @nhắc tên. anonymous: đăng trong nhóm bật ẩn danh. warned: mức MEDIUM/HEAVY không lưu, gửi được. rejected: sửa bài bị từ chối, có lý do. Khối tạo bình chọn trong trình soạn: 2–10 lựa chọn, chọn một/nhiều, hiện kết quả trước khi bình chọn, hạn kết thúc bắt buộc; sửa hoặc bỏ được khi còn nháp. Mở lại nháp từ hồ sơ. |
| SCR-M03-02 | Chi tiết bài viết | M03 | ACT-001, ACT-002, ACT-003, ACT-009 | UC-M03-007, UC-M03-008, UC-M03-013, UC-M03-017, UC-M03-021, UC-M03-023, UC-M02-005, UC-M02-006, UC-M12-001, UC-M12-002, UC-M12-020, UC-M07-009, UC-M01-011, UC-M05-004, UC-M03-014, UC-M03-015, UC-M03-018, UC-M11-020 | SC-M03-007, SC-M03-008, SC-M03-013, SC-M03-017, SC-M02-005, SC-M02-006, SC-M12-001, SC-M07-008, SC-M01-025, SC-M03-014, SC-M03-021, SC-M03-015, SC-M03-018, SC-M11-022 | FR-M03-07, FR-M03-08, FR-M03-13, FR-M02-05, FR-M02-06, FR-M12-01, FR-M07-08, FR-M01-13, FR-M05-04, FR-M13-07, FR-M03-14, FR-M03-15, FR-M11-14 | default, guest, owner, mod, pending, rejected, hidden, locked, deleted, anonymous, banned, not-found, forbidden, loading, long | desktop | A | Màn hình mẫu bước 3. Thanh thao tác Upvote · Bình luận · Tóm tắt (bài ≥300 từ) · Lưu, Báo cáo ở cuối (DD-UI-10, DD-UI-11). owner: menu sửa, tự ẩn/hiện lại, khóa/mở khóa bình luận, xóa (không có bước xác nhận theo SC-M03-014, SC-M03-015), quản lý bình chọn, tắt thông báo bài; mở từ thông báo kết quả xử lý thì xem bài trong ngữ cảnh kiểm duyệt (SC-M03-018). Group Mod/Owner: gỡ bài khỏi nhóm (SC-M11-022, không khiếu nại được). mod: khóa bình luận hoặc khóa toàn bộ, đổi Chủ đề/Tag, xem danh tính tài khoản đã vô hiệu hóa. banned: tác giả bị ban, nhãn "Tài khoản đã bị khóa". Khu bình luận là SCR-M04-01. |
| SCR-M03-03 | Lịch sử sửa bài | M03 | ACT-001, ACT-002, ACT-003 | UC-M03-012, UC-M03-022 | SC-M03-012 | FR-M03-12 | default, loading, forbidden | desktop | A | — |
| SCR-M03-04 | Quản lý bình chọn (trong khối bình chọn, chỉ tác giả) | M03 | ACT-002, ACT-003 | UC-M03-009 | SC-M03-009, SC-M03-019, SC-M03-020 | FR-M03-09 | default, validation | desktop | A | Đổi hạn kết thúc, kết thúc ngay, thêm lựa chọn (tổng ≤10) — ba thao tác riêng (SC-M03-009, -019, -020). |
| SCR-M03-05 | Hàng chờ duyệt bài (Mod/Admin) | M03 | ACT-008, ACT-007 | UC-M03-006 | SC-M03-006 | FR-M03-06 | default, empty, loading, validation, error | desktop | C | Đọc bài ngay trong hàng chờ; Chấp nhận, hoặc Từ chối kèm lý do bắt buộc (SC-M03-006 E1, E2). error: bài không còn chờ duyệt khi gửi quyết định. |
| SCR-M04-01 | Khu bình luận (trong chi tiết bài) | M04 | ACT-001, ACT-002, ACT-003, ACT-009 | UC-M04-001, UC-M04-002, UC-M04-003, UC-M04-004, UC-M04-005, UC-M04-007, UC-M04-010, UC-M04-020, UC-M04-030, UC-M01-012, UC-M12-001, UC-M12-002, UC-M11-020 | SC-M04-001, SC-M04-002, SC-M04-003, SC-M04-004, SC-M04-005, SC-M12-001, SC-M13-002, SC-M11-022 | FR-M04-01, FR-M04-02, FR-M04-03, FR-M04-04, FR-M04-05, FR-M12-01, FR-M01-13, FR-M11-14 | default, empty, guest, locked, hidden, deleted, warned, validation, loading, long | desktop | A | Sắp xếp Top / Mới nhất / Cũ nhất; trả lời 2 cấp có dòng trích; "(đã chỉnh sửa)"; avatar cạnh tên (DD-UI-12). Nằm trong trang SCR-M03-02, tách mã để quản lý trạng thái. Bình luận tối đa 1.000 từ. Xóa bình luận không có bước xác nhận (SC-M04). Group Mod/Owner gỡ bình luận khỏi nhóm. |
| SCR-M04-02 | Xem lại bình luận đã bị xử lý (chỉ đọc) | M04 | ACT-002, ACT-003 | UC-M04-006 | SC-M04-006 | FR-M04-06 | default, hidden, forbidden | desktop | C | Mở từ thông báo xử lý hoặc từ khiếu nại. |
| SCR-M05-01 | Danh sách Chủ đề và Tag | M05 | ACT-001, ACT-002, ACT-003 | UC-M05-004, UC-M05-021, UC-M07-001, UC-M07-002 | SC-M05-003, SC-M07-001, SC-M07-002 | FR-M05-04, FR-M07-01 | default, guest, loading | desktop | A | Danh sách Chủ đề và danh sách Tag (SC-M05-003). Bấm một Chủ đề/Tag mở Kết quả tìm kiếm lọc theo Chủ đề/Tag đó với truy vấn rỗng (SC-M05-009, SC-M06-003). Nút Theo dõi / Bỏ theo dõi ở từng Chủ đề (câu hỏi mở #1, đã duyệt). |
| SCR-M05-02 | Quản lý Chủ đề (Admin) | M05 | ACT-007 | UC-M05-006, UC-M05-008, UC-M05-022 | SC-M05-004, SC-M05-006 | FR-M05-06, FR-M05-08 | default, validation | desktop | C | Thêm Chủ đề; xóa khi Chủ đề không có bài nào ngoài bài nháp. |
| SCR-M05-03 | Gộp Chủ đề (hộp thoại) | M05 | ACT-007 | UC-M05-007 | SC-M05-005 | FR-M05-07 | default, validation | desktop | C | Chọn Chủ đề nguồn và đích; bài của nguồn chuyển sang đích. |
| SCR-M05-04 | Quản lý Tag (Mod/Admin) | M05 | ACT-008, ACT-007 | UC-M05-009, UC-M05-010, UC-M05-023 | SC-M05-007, SC-M05-008 | FR-M05-09, FR-M05-10 | default, no-result | desktop | C | Vô hiệu hóa / kích hoạt lại Tag. |
| SCR-M05-05 | Đổi Chủ đề, Tag của bài (hộp thoại Mod/Admin) | M05 | ACT-008, ACT-007 | UC-M05-011 | SC-M05-009 | FR-M05-11 | default, validation | desktop | C | Cùng giới hạn như tác giả: 1–3 Chủ đề, ≤5 Tag. |
| SCR-M06-01 | Gợi ý khi gõ và lịch sử tìm kiếm (ô tìm kiếm) | M06 | ACT-001, ACT-002, ACT-003 | UC-M06-001, UC-M06-005, UC-M06-006, UC-M06-007, UC-M06-009, UC-M06-021, UC-M06-022 | SC-M06-001, SC-M06-004, SC-M06-005, SC-M06-006 | FR-M06-01, FR-M06-05 | default, empty, no-result, error | desktop | E | Gợi ý người dùng, Tag, Chủ đề, Nhóm; 10 truy vấn gần nhất trên thiết bị, xóa toàn bộ. error: vượt giới hạn tần suất. |
| SCR-M06-02 | Kết quả tìm kiếm | M06 | ACT-001, ACT-002, ACT-003 | UC-M06-002, UC-M06-003, UC-M06-004, UC-M06-008, UC-M06-020, UC-M07-001, UC-M07-002 | SC-M06-002, SC-M06-003, SC-M13-004, SC-M05-009, SC-M07-001, SC-M07-002 | FR-M06-02, FR-M06-03, FR-M06-04, FR-M07-01 | default, guest, no-result, loading, error, long | desktop | E | Kết quả phụ tối đa 3 mỗi loại; lọc Chủ đề, Tag, khoảng thời gian (Hôm nay, Tuần này, Tháng này, Tất cả), chỉ nội dung đang theo dõi; sắp xếp Liên quan / Mới nhất / Nhiều upvote nhất; tối đa 120 kết quả, cuộn tải thêm. Cũng là "trang Chủ đề/Tag": lọc theo Chủ đề hoặc Tag với ô tìm rỗng (SC-M06-003). AI tắt → tìm full-text, giao diện như nhau. Khi lọc theo đúng một Chủ đề: đầu trang có nút Theo dõi / Bỏ theo dõi Chủ đề đó (câu hỏi mở #1, đã duyệt). |
| SCR-M07-01 | Ngăn thông báo (bấm chuông) | M07 | ACT-002, ACT-003 | UC-M07-003, UC-M07-004, UC-M07-007, UC-M07-021, UC-M07-006 | SC-M07-003, SC-M07-004 | FR-M07-05, FR-M07-06 | default, empty, loading, expired | desktop | D | 10 thông báo gần nhất, đã đọc / chưa đọc. |
| SCR-M07-02 | Trang Thông báo | M07 | ACT-002, ACT-003 | UC-M07-003, UC-M07-004, UC-M07-005, UC-M07-007, UC-M07-006, UC-M10-005 | SC-M07-003, SC-M07-004, SC-M07-005, SC-M07-006, SC-M10-004 | FR-M07-05, FR-M07-06, FR-M10-03 | default, empty, loading, error, expired | desktop | D | Tải thêm 20 mỗi lần cuộn; nút đánh dấu tất cả đã đọc. Thông báo đề xuất làm Mod/Admin có hai nút Chấp nhận / Từ chối ngay trên dòng thông báo (SC-M07-006, SC-M10-004); expired: đề xuất đã hết hạn, đã bị thay hoặc đã trả lời. |
| SCR-M07-03 | Popup tin nhắn mới và biểu tượng Tin nhắn | M07 | ACT-002, ACT-003 | UC-M07-008, UC-M07-023 | SC-M07-007 | FR-M07-07 | default | desktop | D | Popup nhỏ góc màn hình; số cuộc trò chuyện có tin chưa đọc trên thanh trên cùng. |
| SCR-M08-01 | Báo cáo vi phạm (hộp thoại) | M08 | ACT-002, ACT-003 | UC-M08-020 | SC-M08-001 | FR-M08-01 | default, validation, submitted | desktop | C | Cho bài viết, bình luận, người dùng, nhóm; lý do, mô tả, bằng chứng. |
| SCR-M08-02 | Hàng chờ báo cáo (Mod/Admin) | M08 | ACT-008, ACT-007 | UC-M08-003, UC-M08-022 | SC-M08-002, SC-M13-003 | FR-M08-02, FR-M08-07 | default, empty, flagged, loading | desktop | C | Vụ xếp theo ưu tiên, gồm vụ do AI tạo và nội dung AI gắn cờ. |
| SCR-M08-03 | Chi tiết vụ báo cáo | M08 | ACT-008, ACT-007 | UC-M08-004, UC-M08-006, UC-M08-007, UC-M08-021, UC-M08-024 | SC-M08-003, SC-M08-004, SC-M08-006 | FR-M08-03, FR-M08-04, FR-M08-07 | default, pending, forbidden, flagged, deleted | desktop | C | Khu thao tác của người giữ vụ (EP-CASE-ACTION): ẩn bài/bình luận, cảnh cáo (kể cả người báo cáo ác ý), ban theo lịch sử hoặc ban vĩnh viễn, ẩn/khóa nhóm, xét nội dung AI gắn cờ (giữ hoặc ẩn), kết luận Bác bỏ / Có xử lý. pending: vụ mở chưa ai giữ → nút Nhận xử lý. Không có nút nhả: vụ tự nhả sau 30 phút không thao tác. forbidden: người khác đang giữ, vụ về chính mình hoặc về Mod khác (Mod). deleted: nội dung đã tự ẩn/xóa, xem bản lưu. |
| SCR-M08-04 | Lý do cho biện pháp và kết luận vụ (hộp thoại) | M08 | ACT-008, ACT-007 | UC-M08-005, UC-M08-008, UC-M08-009, UC-M08-010, UC-M08-011, UC-M08-015, UC-M08-023 | SC-M08-005, SC-M08-007, SC-M08-008, SC-M08-009, SC-M08-010, SC-M08-013, SC-M08-014 | FR-M08-05, FR-M08-06, FR-M08-10, FR-M08-11, FR-M08-14, FR-M08-18 | default, validation | desktop | C | Nhập lý do khi cảnh cáo, ban, kết luận Bác bỏ / Có xử lý; thiếu lý do thì không gửi được. |
| SCR-M08-05 | Mức cảnh cáo của tôi | M08 | ACT-002, ACT-003 | UC-M08-013 | SC-M08-012 | FR-M08-13 | default, warned, empty | desktop | C | Một mục trong Cài đặt tài khoản (SCR-M01-07); chỉ chính người đó thấy. |
| SCR-M08-06 | Nhật ký kiểm duyệt | M08 | ACT-008, ACT-007 | UC-M08-017, UC-M08-025 | SC-M08-016 | FR-M08-16, FR-M08-17 | default, empty, mod, admin, loading | desktop | C | Admin xem toàn bộ, Mod xem phần của mình. Chọn một dòng để xem chi tiết kết luận; mở được từ khi xét khiếu nại (SC-M08-016). |
| SCR-M09-01 | Gửi khiếu nại | M09 | ACT-002, ACT-008 | UC-M09-001, UC-M09-003, UC-M09-020 | SC-M09-001 | FR-M09-01 | default, validation, forbidden, banned, submitted | desktop | C | Khiếu nại cảnh cáo, ban, bài bị gỡ, bài bị AI tự từ chối. forbidden: hết hạn hoặc không đủ điều kiện. Mở từ: màn hình tài khoản bị khóa, email ban vĩnh viễn, thông báo xử lý bài, thông báo AI từ chối bài/cảnh cáo AI (SC-M09-001). Lời giải thích + ảnh tùy chọn; gửi rồi không sửa, không rút được. |
| SCR-M09-02 | Khiếu nại của tôi | M09 | ACT-002, ACT-008 | UC-M09-002 | SC-M09-002 | FR-M09-02 | default, empty, pending, rejected, loading | desktop | C | Kết luận và lý do; xem lại nội dung bị xử lý (chỉ đọc). |
| SCR-M09-03 | Hàng chờ khiếu nại (Mod/Admin) | M09 | ACT-008, ACT-007 | UC-M09-004, UC-M09-007 | SC-M09-003 | FR-M09-03 | default, empty, mod, admin | desktop | C | Tách khỏi hàng chờ báo cáo; lọc theo loại. |
| SCR-M09-04 | Chi tiết khiếu nại | M09 | ACT-008, ACT-007 | UC-M09-005, UC-M09-006, UC-M09-008, UC-M09-009, UC-M09-010, UC-M09-011, UC-M09-012, UC-M09-021, UC-M09-022, UC-M13-009, UC-M13-024 | SC-M09-004, SC-M09-005, SC-M09-006, SC-M13-007 | FR-M09-04, FR-M09-06, FR-M09-07, FR-M09-08, FR-M13-09 | default, forbidden, validation, pending | desktop | C | Nhận khiếu nại, xem xử lý bị khiếu nại và căn cứ (kể cả nhật ký AI), kết luận Chấp nhận / Từ chối kèm lý do. pending: chưa ai nhận. Không có nút nhả: tự nhả sau 30 phút. |
| SCR-M10-01 | Người dùng (Admin Panel) | M10 | ACT-007 | UC-M10-001 | SC-M10-001 | FR-M10-01 | default, no-result, loading | desktop | C | — |
| SCR-M10-02 | Vai trò của một người dùng (đề xuất, giáng, thu hồi) | M10 | ACT-007 | UC-M10-002, UC-M10-003, UC-M10-004, UC-M10-006, UC-M10-007, UC-M10-009 | SC-M10-002, SC-M10-003, SC-M10-005, SC-M10-006 | FR-M10-02, FR-M10-04, FR-M10-07, FR-M10-08 | default, pending, forbidden | desktop | C | forbidden: chỉ ADMIN gốc đề xuất làm Admin và thu hồi Admin. Có nhãn ADMIN gốc. "Xem thao tác" của một Mod mở Nhật ký kiểm duyệt lọc theo người đó (FR-M10-01, SC-M10-001). |
| SCR-M10-03 | Tự từ chức vai trò (hộp thoại) | M10 | ACT-008, ACT-007 | UC-M10-008 | SC-M10-007 | FR-M10-05 | default, forbidden | desktop | C | Xác nhận một lần; ADMIN gốc không từ chức được. |
| SCR-M10-04 | Cấu hình hệ thống | M10 | ACT-007 | UC-M10-010, UC-M10-011, UC-M10-012, UC-M10-013, UC-M10-014, UC-M10-021 | SC-M10-008, SC-M10-009, SC-M10-010, SC-M10-011 | FR-M10-09, FR-M10-10, FR-M10-11, FR-M10-12 | default, error | desktop | C | Công tắc AI tổng + Search, Moderation, Topic suggestion; bảo trì; tạm dừng đăng ký; cờ Group, Chat, Gamification. |
| SCR-M10-05 | Banner toàn trang (đặt, sửa, gỡ) | M10 | ACT-007 | UC-M10-015, UC-M10-016, UC-M10-022 | SC-M10-012, SC-M10-013 | FR-M10-13 | default, empty, validation | desktop | C | — |
| SCR-M10-06 | Nhật ký thao tác Admin | M10 | ACT-007 | UC-M10-018, UC-M10-023 | SC-M10-015 | FR-M10-14, FR-M10-15 | default, no-result, loading | desktop | C | Chỉ xem, lọc; không sửa, không xóa. |
| SCR-M11-01 | Danh sách nhóm | M11 | ACT-001, ACT-002, ACT-003 | UC-M11-004, UC-M11-031 | SC-M11-004 | FR-M11-03 | default, empty, guest, loading, error | desktop | D | Nhóm Public và nhóm Private mình là thành viên, mới nhất trước; nút Tạo nhóm. |
| SCR-M11-02 | Tạo nhóm | M11 | ACT-002, ACT-003 | UC-M11-001, UC-M11-030 | SC-M11-001 | FR-M11-01 | default, validation | desktop | D | — |
| SCR-M11-03 | Trang nhóm | M11 | ACT-001, ACT-002, ACT-003, ACT-009, ACT-010, ACT-011 | UC-M11-005, UC-M11-007, UC-M11-008, UC-M11-023, UC-M11-024, UC-M11-032, UC-M11-034, UC-M08-016 | SC-M11-005, SC-M11-007, SC-M11-008, SC-M08-015 | FR-M11-03, FR-M11-04, FR-M11-16, FR-M11-17, FR-M08-18 | default, guest, visitor, owner, pending, forbidden, hidden, locked, anonymous, empty, error, mod | desktop | D | Tên, mô tả, bài của nhóm; Tham gia / Gửi yêu cầu / Rút yêu cầu; Đăng bài trong nhóm (SCR-M03-01). mod: Mod/Admin mở khóa nhóm. Mở qua link mời nhóm Private khi chưa là thành viên: chỉ thấy tên, mô tả và nút tham gia (SC-M11-005). |
| SCR-M11-04 | Gửi yêu cầu tham gia (hộp thoại câu hỏi tham gia) | M11 | ACT-002, ACT-003 | UC-M11-007 | SC-M11-007 | FR-M11-04 | default, validation, forbidden | desktop | D | forbidden: bị chặn gửi yêu cầu. |
| SCR-M11-05 | Thành viên nhóm | M11 | ACT-001, ACT-002, ACT-009, ACT-010, ACT-011 | UC-M11-006, UC-M11-012, UC-M11-013 | SC-M11-006, SC-M11-014, SC-M11-015, SC-M11-016 | FR-M11-03, FR-M11-08, FR-M11-09 | default, owner, visitor, forbidden | desktop | D | Vai trò từng người; Owner bổ nhiệm/giáng Group Mod, kick; Group Mod kick Member. |
| SCR-M11-06 | Yêu cầu tham gia chờ duyệt | M11 | ACT-010, ACT-011 | UC-M11-010, UC-M11-011 | SC-M11-010, SC-M11-011 | FR-M11-06, FR-M11-07 | default, empty | desktop | D | Xem câu trả lời; chấp nhận, từ chối, chặn người gửi. |
| SCR-M11-07 | Mời vào nhóm (hộp thoại) | M11 | ACT-009, ACT-010, ACT-011 | UC-M11-009 | SC-M11-009 | FR-M11-05 | default, validation | desktop | D | Mời người dùng hoặc lấy link mời. |
| SCR-M11-08 | Cài đặt nhóm | M11 | ACT-011 | UC-M11-002, UC-M11-003, UC-M11-022 | SC-M11-002, SC-M11-003 | FR-M11-02, FR-M11-15 | default, validation, locked | desktop | D | Tên, mô tả, Public/Private, duyệt trước, ẩn danh, câu hỏi tham gia; xóa nhóm. |
| SCR-M11-09 | Rời nhóm (hộp thoại) | M11 | ACT-009, ACT-010, ACT-011 | UC-M11-014, UC-M11-015 | SC-M11-017 | FR-M11-10 | default, owner | desktop | D | owner: phải chọn người kế nhiệm rồi xác nhận rời (SC-M11-017); Owner là thành viên cuối: cảnh báo nhóm sẽ bị xóa, xác nhận hoặc thôi. |
| SCR-M11-10 | Hàng chờ duyệt bài của nhóm | M11 | ACT-010, ACT-011 | UC-M11-017, UC-M11-018, UC-M11-019, UC-M11-021 | SC-M11-019, SC-M11-020, SC-M11-021 | FR-M11-13 | default, empty, forbidden, validation | desktop | D | Nhận bài để xét; Chấp nhận, hoặc Từ chối kèm lý do (SC-M11-021). |
| SCR-M11-11 | Danh sách chặn tham gia | M11 | ACT-010, ACT-011 | UC-M11-011 | SC-M11-012, SC-M11-013 | FR-M11-07 | default, empty | desktop | D | Xem người bị chặn gửi yêu cầu, bỏ chặn (SC-M11-012, SC-M11-013). |
| SCR-M12-01 | Bảng xếp hạng | M12 | ACT-001, ACT-002, ACT-003 | UC-M12-004, UC-M12-005, UC-M12-006, UC-M12-007, UC-M12-008, UC-M12-021 | SC-M12-002 | FR-M12-06, FR-M12-07, FR-M12-08 | default, empty, guest, loading, error | desktop | B | Tab Tuần / Tháng / Toàn thời gian; lọc Lớp/Khối 10, 11, 12, Tất cả; dấu Ngôi sao tuần; "[Người dùng đã xóa]". Trình bày tiết chế (DD-UI-05). |
| SCR-M13-01 | Tóm tắt bài viết (ngăn hiển thị) | M13 | ACT-002, ACT-003 | UC-M13-006, UC-M13-007, UC-M13-023 | SC-M13-006 | FR-M13-06, FR-M13-07 | default, loading, error | desktop | A | Chỉ bài từ 300 từ; mở từ nút Tóm tắt trong SCR-M03-02. |
| SCR-M14-01 | Trang chủ (bảng tin) | M14 | ACT-001, ACT-002, ACT-003 | UC-M14-001, UC-M14-002, UC-M14-003, UC-M14-004, UC-M14-005, UC-M14-020, UC-M14-021, UC-M14-022, UC-M14-023 | SC-M14-001, SC-M14-002, SC-M14-003, SC-M14-004, SC-M14-005, SC-M14-006 | FR-M14-01, FR-M14-02, FR-M14-04, FR-M14-05, FR-M14-06, FR-M14-07, FR-M14-08 | default, guest, empty, loading, error, long | desktop | A | Tab Thịnh hành (mục con Bài viết / Chủ đề / Tag) · Đang theo dõi · Nhóm · Mới nhất; banner "có bài mới" (trừ Thịnh hành); cuộn tải 20 bài. empty: Đang theo dõi → nút sang tìm kiếm; Nhóm → nút Khám phá Group. |
| SCR-M15-01 | Thống kê người dùng | M15 | ACT-007 | UC-M15-001, UC-M15-002, UC-M15-003, UC-M15-020 | SC-M15-001 | FR-M15-01 | default, empty, loading | desktop | C | — |
| SCR-M15-02 | Thống kê nội dung | M15 | ACT-007 | UC-M15-004, UC-M15-021, UC-M13-010 | SC-M15-002, SC-M13-008 | FR-M15-02, FR-M13-10 | default, empty, loading | desktop | C | Gồm tỷ lệ Chủ đề gợi ý được giữ lại. |
| SCR-M15-03 | Thống kê kiểm duyệt | M15 | ACT-007 | UC-M15-005, UC-M15-006, UC-M15-007, UC-M15-022 | SC-M15-003 | FR-M15-03 | default, empty, loading | desktop | C | — |
| SCR-M16-01 | Hộp thư Chat | M16 | ACT-002, ACT-003 | UC-M16-002, UC-M16-030, UC-M07-011 | SC-M16-002, SC-M07-010 | FR-M16-03, FR-M07-09, FR-M16-15 | default, empty, loading, error | desktop | D | Cuộc trò chuyện mới nhất trước, đánh dấu chưa đọc; tạo nhóm chat; bật/tắt popup toàn bộ Chat. |
| SCR-M16-02 | Cuộc trò chuyện (1-1 hoặc nhóm chat) | M16 | ACT-002, ACT-012, ACT-014 | UC-M16-001, UC-M16-003, UC-M16-004, UC-M16-005, UC-M16-006, UC-M16-007, UC-M16-018, UC-M16-031, UC-M07-010 | SC-M16-001, SC-M16-003, SC-M16-004, SC-M16-005, SC-M07-009 | FR-M16-01, FR-M16-04, FR-M16-05, FR-M16-06, FR-M16-07, FR-M07-09 | default, empty, loading, validation, forbidden, banned, long, error | desktop | D | Tải dần lịch sử; thu hồi trong 5 phút; "Đã xem" ở tin mới nhất; tắt popup cuộc này. forbidden: thành viên cũ chỉ đọc tới lúc rời. Đang đọc tin cũ mà có tin mới: hiện chỉ báo để nhảy xuống tin mới nhất (SC-M16-003). |
| SCR-M16-03 | Tạo nhóm chat (hộp thoại) | M16 | ACT-002, ACT-003 | UC-M16-008, UC-M16-032 | SC-M16-006 | FR-M16-02 | default, validation | desktop | D | Tên nhóm; 3–100 thành viên. |
| SCR-M16-04 | Thông tin nhóm chat | M16 | ACT-012, ACT-013 | UC-M16-010, UC-M16-012, UC-M16-013, UC-M16-014, UC-M16-015, UC-M16-016, UC-M16-017, UC-M16-020, UC-M16-033 | SC-M16-008, SC-M16-010, SC-M16-011, SC-M16-012, SC-M16-013, SC-M16-014, SC-M16-015 | FR-M16-08, FR-M16-09, FR-M16-10, FR-M16-11, FR-M16-12, FR-M16-13, FR-M16-14 | default, owner, pending, validation | desktop | D | Thành viên, đổi tên, link mời, rời nhóm. owner (Admin nhóm chat): duyệt người chờ, bật/tắt duyệt, xóa thành viên, chuyển quyền. |
| SCR-M16-05 | Xin gia nhập nhóm chat qua link mời | M16 | ACT-002, ACT-003 | UC-M16-011 | SC-M16-009 | FR-M16-16 | default, pending, not-found, error | desktop | D | — |
| SCR-M16-06 | Thêm thành viên vào nhóm chat (hộp thoại) | M16 | ACT-012, ACT-013 | UC-M16-009, UC-M16-019 | SC-M16-007 | FR-M16-08 | default, validation, pending | desktop | D | Người do Member thêm phải chờ Admin nhóm chat duyệt. |

## 3. UC không có màn hình riêng

UC con chỉ do hệ thống hoặc AI làm. Các UC con kiểu kiểm tra/tính toán mà kết quả hiện ngay trên một màn hình được
ghi vào cột `uc` của màn hình đó.

<!-- ui:no-screen -->
| uc | reason | shown_as |
|---|---|---|
| UC-M03-005 | Hệ thống áp chính sách kiểm duyệt khi công bố | SCR-M03-01, SCR-M03-02 trạng thái pending, rejected |
| UC-M08-001 | Hệ thống gom báo cáo vào vụ | SCR-M08-02 (một dòng mỗi vụ) |
| UC-M08-002 | Hệ thống tính ưu tiên vụ | SCR-M08-02 (thứ tự) |
| UC-M08-014 | Hệ thống tự cập nhật mức cảnh cáo khi hết thử thách | SCR-M08-06 |
| UC-M12-003 | Hệ thống cập nhật điểm khi upvote đổi | SCR-M02-01 (điểm), SCR-M12-01 |
| UC-M13-001 | AI chấm điểm bài, bình luận | SCR-M03-01/02 pending, rejected; SCR-M04-01 hidden; SCR-M08-02 flagged |
| UC-M13-002 | AI tổng hợp điểm quét | Như UC-M13-001 |
| UC-M13-003 | Tạo embedding bài viết | SCR-M06-02 (kết quả tìm theo ngữ nghĩa) |
| UC-M13-004 | Tạo embedding truy vấn | SCR-M06-02 |
| UC-M13-005 | AI trả Chủ đề gợi ý | SCR-M03-01 (nút Gợi ý chủ đề) |
| UC-M13-008 | Gọi dịch vụ AI dùng chung | Không hiện trực tiếp; lỗi AI hiện ở màn hình gọi |

## 4. Chia đợt

<!-- ui:batches -->
| batch | name | order_reason |
|---|---|---|
| A | Đọc và viết | Dùng màn hình mẫu bước 3; tạo phần lớn component (khung, thẻ bài, trình soạn, bình luận) |
| B | Con người | Dựa trên khung và thẻ bài của đợt A: hồ sơ, theo dõi, bảng xếp hạng |
| C | Kiểm duyệt và quản trị | Nhiều bảng, hàng chờ, hộp thoại; dùng chung khung quản trị |
| D | Cộng đồng và liên lạc | Nhóm dùng lại feed và trình soạn; thông báo và chat là khối riêng |
| E | Vào hệ thống và tìm kiếm | Form đơn giản; vẽ khi component form đã chốt ở các đợt trước |

## 5. Nguồn đã dùng

`check_inventory.py` so cột `version` với tài liệu hiện tại để báo màn hình bị ảnh hưởng khi nguồn đổi. FR: giá trị
`phien_ban`; US, SC: giá trị `date` trong bảng tài liệu.

<!-- ui:sources -->
| path | version |
|---|---|
| docs/specs/fr/FR-M01.md | 1.10 |
| docs/specs/fr/FR-M02.md | 1.6 |
| docs/specs/fr/FR-M03.md | 1.10 |
| docs/specs/fr/FR-M04.md | 1.4 |
| docs/specs/fr/FR-M05.md | 1.7 |
| docs/specs/fr/FR-M06.md | 1.5 |
| docs/specs/fr/FR-M07.md | 1.5 |
| docs/specs/fr/FR-M08.md | 1.7 |
| docs/specs/fr/FR-M09.md | 1.2 |
| docs/specs/fr/FR-M10.md | 1.4 |
| docs/specs/fr/FR-M11.md | 1.3 |
| docs/specs/fr/FR-M12.md | 1.1 |
| docs/specs/fr/FR-M13.md | 1.3 |
| docs/specs/fr/FR-M14.md | 1.1 |
| docs/specs/fr/FR-M15.md | 1.1 |
| docs/specs/fr/FR-M16.md | 1.0 |
| docs/specs/us/US-M01.md | 2026-10-29 |
| docs/specs/us/US-M02.md | 2026-10-30 |
| docs/specs/us/US-M03.md | 2026-10-30 |
| docs/specs/us/US-M04.md | 2026-10-30 |
| docs/specs/us/US-M05.md | 2026-10-30 |
| docs/specs/us/US-M06.md | 2026-10-30 |
| docs/specs/us/US-M07.md | 2026-10-30 |
| docs/specs/us/US-M08.md | 2026-10-31 |
| docs/specs/us/US-M09.md | 2026-10-31 |
| docs/specs/us/US-M10.md | 2026-11-01 |
| docs/specs/us/US-M11.md | 2026-11-01 |
| docs/specs/us/US-M12.md | 2026-11-01 |
| docs/specs/us/US-M13.md | 2026-11-02 |
| docs/specs/us/US-M14.md | 2026-11-02 |
| docs/specs/us/US-M15.md | 2026-11-02 |
| docs/specs/us/US-M16.md | 2026-11-02 |
| docs/specs/scenarios/M01/SC-M01.md | 2026-11-11 |
| docs/specs/scenarios/M02/SC-M02.md | 2026-11-11 |
| docs/specs/scenarios/M03/SC-M03.md | 2026-11-11 |
| docs/specs/scenarios/M04/SC-M04.md | 2026-11-11 |
| docs/specs/scenarios/M05/SC-M05.md | 2026-11-11 |
| docs/specs/scenarios/M06/SC-M06.md | 2026-11-11 |
| docs/specs/scenarios/M07/SC-M07.md | 2026-11-11 |
| docs/specs/scenarios/M08/SC-M08.md | 2026-11-11 |
| docs/specs/scenarios/M09/SC-M09.md | 2026-11-11 |
| docs/specs/scenarios/M10/SC-M10.md | 2026-11-11 |
| docs/specs/scenarios/M11/SC-M11.md | 2026-11-11 |
| docs/specs/scenarios/M12/SC-M12.md | 2026-11-11 |
| docs/specs/scenarios/M13/SC-M13.md | 2026-11-11 |
| docs/specs/scenarios/M14/SC-M14.md | 2026-11-11 |
| docs/specs/scenarios/M15/SC-M15.md | 2026-11-11 |
| docs/specs/scenarios/M16/SC-M16.md | 2026-11-11 |

## 6. Câu hỏi mở

| # | Câu hỏi | Màn hình | Trạng thái |
|---|---|---|---|
| 1 | Nút Theo dõi Chủ đề đặt ở đâu? SC-M07-001 có theo dõi Chủ đề nhưng không nói nơi bấm. Đề xuất: ở Danh sách Chủ đề và ở đầu trang kết quả lọc theo Chủ đề. | SCR-M05-01, SCR-M06-02 | Đã trả lời 2026-11-25: đồng ý đề xuất |
| 2 | FR không nói nơi đặt đổi mật khẩu, vô hiệu hóa tài khoản, xem mức cảnh cáo, từ chức. Đề xuất: gom vào một trang Cài đặt tài khoản mở từ menu avatar. | SCR-M01-07, SCR-M08-05, SCR-M10-03 | Đã trả lời 2026-11-25: đồng ý |
| 3 | SC-M08-011: Mod gỡ ban trực tiếp trên tài khoản, không qua vụ, nhưng không nói Mod mở tài khoản ở đâu (trang Người dùng của Admin Panel chỉ cho Admin). Đề xuất: hồ sơ người dùng ở chế độ Mod/Admin có nút Gỡ ban khi tài khoản đang bị ban. | SCR-M02-01 | Đã trả lời 2026-11-25: đồng ý |
| 4 | Phạm vi bản tối (PRODUCT.md câu hỏi mở #4): vẽ bản tối cho mọi trạng thái, chỉ trạng thái default của mỗi màn hình, hay vài màn hình đại diện? | Mọi màn hình | Đã trả lời 2026-11-25: bản tối cho trạng thái default của mỗi màn hình (75 artboard); bước 8 tự bật theme tối cho mọi trạng thái còn lại để soát (DD-UI-15) |
| 5 | Email hệ thống gửi (link xác minh, đặt lại mật khẩu, mã kích hoạt, thông báo ban, gỡ ban…) không nằm trong danh mục. Có cần thiết kế mẫu email không? Mặc định: không (ngoài giao diện ứng dụng). | — | Hoãn 2026-11-25: định dạng email quyết sau (DD-UI-19) |
| 6 | Ghi chú cũ của SCR-M01-05 `banned` nói tài khoản BANNED không lấy lại mật khẩu được; FR-M01-09.01, FR-M01-09.16 và BF-M01-018 cho đặt lại, xong chỉ vào màn hình tài khoản bị khóa. Đề xuất: theo FR, sửa ghi chú | SCR-M01-05 | Đã trả lời 2026-11-26: đồng ý theo FR |
