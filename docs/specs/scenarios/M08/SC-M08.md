# Kịch bản nghiệp vụ — M08 Moderation

[Vietnamese Doc] — Tái kiểm 11/11/2026 — Skill scenarios v1.4.

**Phạm vi:** 6 UC chính + 17 UC con, 22 mapping; 16 hành trình actor hoàn tất với iShare. Giữ 25 quan hệ US (19 include, 6 extend), hai extension point và 7 SVG nguồn; không suy số BF từ số oval. Có 15 UC sở hữu scenario (UC015 có hai mục tiêu Ẩn/Khóa), 5 embedded, 3 aggregate; 8 AUT + 6 RULE là phản ứng nền/ràng buộc, không phải scenario tự động.

**Boundary:** toàn iShare là SYSTEM; M13 nội bộ gọi ACT-006 AI bên ngoài trong AUT002. Hệ thống (AI) là nhãn reporter dữ liệu, không actor mới. Group Owner/Group Mod không là Mod hệ thống; M08 dùng ACT-008/ACT-007, không ACT-003 gộp của các module trước.

**Ngoài phạm vi:** quét/duyệt trước đăng M03, sản xuất lại FR/US/UML, triển khai API/CSDL/cron/transaction, giao email/push M07, giải quyết khiếu nại M09, bổ nhiệm role M10, nghiệp vụ quản trị nhóm M11 hoặc điểm/BXH M12. Không thêm xóa nội dung người khác/avatar/bio, report Chat, rút/sửa báo cáo, nhả vụ thủ công, bỏ ẩn nhóm, AI ban, tự phạt reporter, cấu hình hằng số trên UI.

**Trạng thái:** Đang soạn để review. FR-M08 v1.7 Đã chốt; US-M08/overview Chờ duyệt. Có 6 GAP (5 điểm từ NOTE nguồn và 1 điểm đối soát M08–M11) và hai bộ ngưỡng tạm; phần chưa có hợp đồng được ghi rõ, không tự lấp hoặc nhận đã phê duyệt. Đây là tài liệu kịch bản, không thực hiện chế tài/gửi thông báo thật.

## 1. Baseline, actor và dữ liệu dùng chung

<!-- sc:document -->

| key | value |
|---|---|
| module | M08 |
| scope | ALL |
| skill_version | 1.4 |
| output_dir | docs/specs/scenarios/M08 |
| status | Đang soạn |
| completed_steps | 1, 2, 3, 4 |
| date | 2026-11-11 |
| approval_evidence | - |


| Nguồn | Version | Ngày | Trạng thái | SHA-256 |
|---|---|---|---|---|
| [docs/specs/fr/FR-M08.md](../../fr/FR-M08.md) | 1.7 | 2026-10-24 | Đã chốt | a92e6e370038af300a9ddd735414dcb2c4fbffe07c81abaaa3c92dff447c25f0 |
| [docs/specs/us/US-M08.md](../../us/US-M08.md) | Không có version tài liệu (skill_version không là version) | 2026-10-31 | Chờ duyệt | 2847171edf824aacba181041c392fea1ae589a35ad93a24775d4ca0d7b6913ae |
| [docs/specs/us/US-overview.md](../../us/US-overview.md) | 1.1 | 2026-11-02 | Chờ duyệt | c1d624b7036ea2c7a9968eaa46c482c04fa1a15e2554d536cdfc12f177e26e33 |
| [docs/specs/fr/FR-M01.md](../../fr/FR-M01.md) | 1.10 | 2026-10-24 | Đã chốt | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a |
| [docs/specs/fr/FR-M03.md](../../fr/FR-M03.md) | 1.10 | 2026-10-24 | Đã chốt | fc996ec5520b6485277fca6a3dbae018bfce02263aba8e15ea87871f35865980 |
| [docs/specs/fr/FR-M04.md](../../fr/FR-M04.md) | 1.4 | 2026-10-24 | Đã chốt | c2fe0e4f6c4bc6835af27585cb711ac03f9fed516d435e759d20ddd58bfd1039 |
| [docs/specs/fr/FR-M07.md](../../fr/FR-M07.md) | 1.5 | 2026-10-24 | Đã chốt | 05fb18237e049e3742d06c49b824e76e238c7587e7099b8dc4a84a2e1daf4f5b |
| [docs/specs/fr/FR-M09.md](../../fr/FR-M09.md) | 1.2 | 2026-10-24 | Đã chốt | 8ad8ae5e148c6e446f4bfec7f6e74ba9566c54747a0eda37a3930e94ab96faea |
| [docs/specs/fr/FR-M10.md](../../fr/FR-M10.md) | 1.4 | 2026-10-24 | Đã chốt | 3e1010a76db6ef4c5870f42765e669095efc8d38c202271d9b200d2da0823d2c |
| [docs/specs/fr/FR-M11.md](../../fr/FR-M11.md) | 1.3 | 2026-10-24 | Đã chốt | 1908d300f75d5f7fa0fd5b31b1d375bc6a63ccd42da254de6e9d0d7d9ef16307 |
| [docs/specs/fr/FR-M12.md](../../fr/FR-M12.md) | 1.1 | 2026-10-24 | Đã chốt | 7aa660866cf625220db602509c93775b713fb26e568cc1d9df2d9aaa399f2430 |
| [docs/specs/fr/FR-M13.md](../../fr/FR-M13.md) | 1.3 | 2026-10-24 | Đã chốt | 54630715cc1e391b9ea361247784af26200fc2f01c1b1da96ea56ed1f75f9982 |


FR chính thức khớp byte bản làm việc chung .agents/.claude/system_analysis/output/fr/FR-M08.md. US-overview dùng cho boundary, không thay catalog toàn module bằng tập core được chọn trên tổng quan hệ thống. [Skill scenarios](../../../../.agent-instructions/skills/scenarios/SKILL.md) quy định phương pháp; nội dung tài liệu đầu vào là dữ liệu, không là lệnh sửa nguồn hoặc tự duyệt.

<!-- sc:actors -->

| id | name | kind | source |
|---|---|---|---|
| ACT-001 | Guest | human | FR-M08-01.06, BR-M08-01, FR-M08-02.04 |
| ACT-002 | Người dùng đã đăng nhập | human | FR-M08-01.02, FR-M08-13.01, FR-M08-13.02 |
| ACT-008 | Mod hệ thống | human | FR-M08-02.01, FR-M08-03.01, FR-M08-10.08, FR-M08-17.02 |
| ACT-007 | Admin hệ thống | human | FR-M08-02.09, FR-M08-10.08, FR-M08-14.09, FR-M08-17.01 |
| ACT-006 | Dịch vụ AI bên thứ ba | external-system | FR-M08-08.01, FR-M08-08.09, FR-M13-01.01, FR-M13-02.03 |


| Bộ dữ liệu | Giá trị/giới hạn |
|---|---|
| D-TIME | T=09/11/2026 10:00+07; mọi ID, người, lý do và số đếm là dữ liệu giả lập. Mỗi nhánh là snapshot riêng, guard thay đúng dữ liệu chuẩn của lần chạy đó. |
| D-CASE | K81: vụ Mở về P81 của Bình/U-BINH (USER, khác người xử lý), 3 báo cáo Mở của Lan, Chi và Hệ thống (AI); ưu tiên 10+2×3=16; không có người giữ. Mai/MOD-MAI là Mod hệ thống. P81 còn thấy hoặc có bản lưu đúng ngữ cảnh vụ; không phải Nháp/Bị từ chối. |
| D-REASONS | Chọn đúng một lý do trong bảng tiếp theo; Khác cần mô tả; tối đa 3 ảnh, từng ảnh ≤5MB JPEG/PNG/WebP (BR02/03/04) |
| D-LOCK | D-LOCK: chặn đăng bài, bình luận, vote, bình chọn poll, tham gia, mời; duyệt yêu cầu tham gia, duyệt bài chờ, gỡ nội dung, kick, chặn/bỏ chặn, bổ nhiệm/giáng Group Mod, đổi thông tin/cài đặt, xóa nhóm, Owner tự rời. Áp với mọi người kể cả Owner/Group Mod. Vẫn đọc theo Public/Private cũ, bookmark/báo cáo; Member/Group Mod tự rời; hệ thống tự chuyển Owner khi Owner mất quyền ngoài ý muốn. Mở khóa cho lại trong phạm vi quyền thường, không cấp quyền mới (BR-M11-28). |


| D-REASONS / target | Danh mục nguồn BR-M08-02 |
|---|---|
| Bài viết | Spam/Quảng cáo; Nội dung sai/hiểu nhầm; Đạo văn/Vi phạm bản quyền; Quấy rối/Bắt nạt; Ngôn từ thù ghét/Phân biệt; Nội dung người lớn/Không phù hợp; Bạo lực/Đe dọa; Khác |
| Bình luận | Spam/Quảng cáo; Nội dung sai/hiểu nhầm; Quấy rối/Bắt nạt; Ngôn từ thù ghét/Phân biệt; Nội dung người lớn/Không phù hợp; Bạo lực/Đe dọa; Khác |
| Tài khoản | Quấy rối/Bắt nạt có hệ thống; Khác |
| Nhóm | Nội dung người lớn/Không phù hợp; Group giả mạo; Quấy rối/Bắt nạt có hệ thống; Khác |


Mỗi SC/nhánh là một lần chạy giả lập riêng; không lấy trạng thái sau của SC trước làm tiền điều kiện mọi SC sau. Nếu đổi target sang comment/group thì K81 trong nhánh là vụ của target đó; dữ liệu cụ thể được ghi tại nhánh. Giá trị 0.7 chỉ minh họa trong khoảng tạm, không là chính sách mới. Reporter/target/actor xử lý là các chủ thể dữ liệu khác nhau; nhánh E tại M1 Admin thay cả actor/người giữ/người làm, không chỉ thay nhãn vai trò.

## 2. Kiểm kê nhóm use case chi tiết

<!-- sc:decomposition -->

| core | sub | source |
|---|---|---|
| UC-M08-020 | UC-M08-001 | FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-07.09, BR-M08-05, BR-M08-49 |
| UC-M08-020 | UC-M08-002 | FR-M08-01.05, FR-M08-02.01, FR-M08-02.07, BR-M08-06, BR-M08-07, BR-M08-49 |
| UC-M08-021 | UC-M08-003 | FR-M08-02, FR-M08-04, BR-M08-11, BR-M08-15, BR-M08-19, BR-M08-46 |
| UC-M08-021 | UC-M08-004 | FR-M08-03, BR-M08-08, BR-M08-09, BR-M08-46 |
| UC-M08-021 | UC-M08-005 | FR-M08-05, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14 |
| UC-M08-021 | UC-M08-006 | FR-M08-03.03, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-46, BR-M08-48 |
| UC-M08-022 | UC-M08-007 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, BR-M08-23, BR-M08-48 |
| UC-M08-022 | UC-M08-008 | FR-M08-06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11 |
| UC-M08-022 | UC-M08-006 | FR-M08-03.03, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-46, BR-M08-48 |
| UC-M08-023 | UC-M08-009 | FR-M08-10, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-36 |
| UC-M08-023 | UC-M08-010 | FR-M08-11, BR-M08-54, FR-M08-16.05 |
| UC-M08-023 | UC-M08-011 | FR-M08-14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-52, BR-M08-53 |
| UC-M08-023 | UC-M08-012 | FR-M08-15, BR-M08-38, BR-M08-48, BR-M08-34, FR-M10-06.01 |
| UC-M08-023 | UC-M08-013 | FR-M08-13, BR-M08-31, BR-M08-32, BR-M08-43 |
| UC-M08-023 | UC-M08-014 | FR-M08-09.04, FR-M08-10.02, FR-M08-11.03, FR-M08-11.05, FR-M08-12, BR-M08-28, BR-M08-29, BR-M08-30, BR-M08-54 |
| UC-M08-023 | UC-M08-006 | FR-M08-03.03, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-46, BR-M08-48 |
| UC-M08-024 | UC-M08-015 | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.08, BR-M08-50, BR-M11-28 |
| UC-M08-024 | UC-M08-016 | FR-M08-18.07, FR-M08-18.09, FR-M08-18.10, BR-M08-48, BR-M08-50 |
| UC-M08-024 | UC-M08-009 | FR-M08-10, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-36 |
| UC-M08-024 | UC-M08-011 | FR-M08-14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-52, BR-M08-53 |
| UC-M08-024 | UC-M08-006 | FR-M08-03.03, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-46, BR-M08-48 |
| UC-M08-025 | UC-M08-017 | FR-M08-17, BR-M08-40, BR-M08-41 |


<!-- sc:ucs -->

| id | treatment | scenarios | coverage | rationale | sources |
|---|---|---|---|---|---|
| UC-M08-020 | scenario | SC-M08-001 | SC-M08-001/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-01, BR-M08-01, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-55 |
| UC-M08-021 | scenario | SC-M08-004 | SC-M08-004/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-02, FR-M08-03, FR-M08-04, FR-M08-05, BR-M08-08, BR-M08-10, BR-M08-46, BR-M08-48 |
| UC-M08-022 | aggregate | SC-M08-002, SC-M08-003, SC-M08-004, SC-M08-005, SC-M08-006, SC-M08-007, SC-M08-008, SC-M08-009, SC-M08-010, SC-M08-011, SC-M08-013, SC-M08-014, SC-M08-015 | SC-M08-002/M2, SC-M08-003/M2, SC-M08-004/M2, SC-M08-005/M2, SC-M08-006/M2, SC-M08-007/M2, SC-M08-008/M2, SC-M08-009/M2, SC-M08-010/M2, SC-M08-011/M2, SC-M08-013/M2, SC-M08-014/M2, SC-M08-015/M2 | Core Summary tổng hợp chức năng con/quy tắc nền, không ép thực hiện liên tiếp mọi thao tác hoặc tạo BF chỉ SYSTEM. | FR-M08-06, FR-M08-07, FR-M08-08, FR-M08-09, BR-M08-22, BR-M08-23, BR-M08-55 |
| UC-M08-023 | aggregate | SC-M08-002, SC-M08-003, SC-M08-004, SC-M08-005, SC-M08-006, SC-M08-007, SC-M08-008, SC-M08-009, SC-M08-010, SC-M08-011, SC-M08-012, SC-M08-013, SC-M08-014, SC-M08-015 | SC-M08-002/M2, SC-M08-003/M2, SC-M08-004/M2, SC-M08-005/M2, SC-M08-006/M2, SC-M08-007/M2, SC-M08-008/M2, SC-M08-009/M2, SC-M08-010/M2, SC-M08-011/M2, SC-M08-012/M2, SC-M08-013/M2, SC-M08-014/M2, SC-M08-015/M2 | Core Summary tổng hợp chức năng con/quy tắc nền, không ép thực hiện liên tiếp mọi thao tác hoặc tạo BF chỉ SYSTEM. | FR-M08-09, FR-M08-10, FR-M08-11, FR-M08-12, FR-M08-13, FR-M08-14, FR-M08-15, BR-M08-31, BR-M08-33, BR-M08-46 |
| UC-M08-024 | aggregate | SC-M08-002, SC-M08-003, SC-M08-004, SC-M08-005, SC-M08-006, SC-M08-007, SC-M08-008, SC-M08-009, SC-M08-010, SC-M08-011, SC-M08-013, SC-M08-014, SC-M08-015 | SC-M08-002/M2, SC-M08-003/M2, SC-M08-004/M2, SC-M08-005/M2, SC-M08-006/M2, SC-M08-007/M2, SC-M08-008/M2, SC-M08-009/M2, SC-M08-010/M2, SC-M08-011/M2, SC-M08-013/M2, SC-M08-014/M2, SC-M08-015/M2 | Core Summary tổng hợp chức năng con/quy tắc nền, không ép thực hiện liên tiếp mọi thao tác hoặc tạo BF chỉ SYSTEM. | FR-M08-18, BR-M08-46, BR-M08-48, BR-M08-50, BR-M11-28 |
| UC-M08-025 | scenario | SC-M08-016 | SC-M08-016/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-16, FR-M08-17, BR-M08-39, BR-M08-40, BR-M08-41 |
| UC-M08-001 | embedded | SC-M08-001 | SC-M08-001/M4 | Ghép báo cáo vào đúng vụ trong lượt lưu báo cáo; mục AI theo AUT004. | FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-07.09, BR-M08-05, BR-M08-49 |
| UC-M08-002 | embedded | SC-M08-001, SC-M08-002, SC-M08-004 | SC-M08-001/M2, SC-M08-002/M2, SC-M08-004/M2 | Ưu tiên được tính khi lưu báo cáo và dùng khi đọc hàng chờ; không tạo thao tác actor chỉ tính số. | FR-M08-01.05, FR-M08-02.01, FR-M08-02.07, BR-M08-06, BR-M08-07, BR-M08-49 |
| UC-M08-003 | scenario | SC-M08-002, SC-M08-004 | SC-M08-002/M2, SC-M08-004/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-02, FR-M08-04, BR-M08-11, BR-M08-15, BR-M08-19, BR-M08-46 |
| UC-M08-004 | scenario | SC-M08-003, SC-M08-004 | SC-M08-003/M2, SC-M08-004/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-03, BR-M08-08, BR-M08-09, BR-M08-46 |
| UC-M08-005 | scenario | SC-M08-004, SC-M08-005 | SC-M08-004/M2, SC-M08-005/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-05, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14 |
| UC-M08-006 | embedded | SC-M08-002, SC-M08-003, SC-M08-004, SC-M08-005, SC-M08-006, SC-M08-007, SC-M08-008, SC-M08-009, SC-M08-010, SC-M08-011, SC-M08-013, SC-M08-014, SC-M08-015 | SC-M08-002/M2, SC-M08-003/M2, SC-M08-004/M2, SC-M08-005/M2, SC-M08-006/M2, SC-M08-007/M2, SC-M08-008/M2, SC-M08-009/M2, SC-M08-010/M2, SC-M08-011/M2, SC-M08-013/M2, SC-M08-014/M2, SC-M08-015/M2 | Kiểm đúng chế độ đọc/nhận/giữ/trực tiếp tại caller, không có BF chỉ kiểm quyền. | FR-M08-03.03, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-46, BR-M08-48 |
| UC-M08-007 | scenario | SC-M08-004, SC-M08-006 | SC-M08-004/M2, SC-M08-006/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, BR-M08-23, BR-M08-48 |
| UC-M08-008 | scenario | SC-M08-004, SC-M08-007 | SC-M08-004/M2, SC-M08-007/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11 |
| UC-M08-009 | scenario | SC-M08-004, SC-M08-006, SC-M08-008 | SC-M08-004/M2, SC-M08-006/M2, SC-M08-008/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-10, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-36 |
| UC-M08-010 | scenario | SC-M08-009 | SC-M08-009/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-11, BR-M08-54, FR-M08-16.05 |
| UC-M08-011 | scenario | SC-M08-004, SC-M08-008, SC-M08-010 | SC-M08-004/M2, SC-M08-008/M2, SC-M08-010/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-52, BR-M08-53 |
| UC-M08-012 | scenario | SC-M08-011 | SC-M08-011/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-15, BR-M08-38, BR-M08-48, BR-M08-34, FR-M10-06.01 |
| UC-M08-013 | scenario | SC-M08-012 | SC-M08-012/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-13, BR-M08-31, BR-M08-32, BR-M08-43 |
| UC-M08-014 | embedded | SC-M08-004, SC-M08-006, SC-M08-008, SC-M08-009 | SC-M08-004/E8.2, SC-M08-006/E4.6, SC-M08-008/M2, SC-M08-009/M2 | Cập nhật số/mức/hạn nằm trong cảnh cáo/bỏ AI; AI/giảm mức thuộc tác vụ nền. | FR-M08-09.04, FR-M08-10.02, FR-M08-11.03, FR-M08-11.05, FR-M08-12, BR-M08-28, BR-M08-29, BR-M08-30, BR-M08-54 |
| UC-M08-015 | scenario | SC-M08-004, SC-M08-013, SC-M08-014 | SC-M08-004/M2, SC-M08-013/M2, SC-M08-014/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.08, BR-M08-50, BR-M11-28 |
| UC-M08-016 | scenario | SC-M08-015 | SC-M08-015/M2 | Actor có mục tiêu chức năng độc lập và nhận kết quả hoàn tất. Các lớp target/quyền/trạng thái là nhánh; không tách theo số oval. | FR-M08-18.07, FR-M08-18.09, FR-M08-18.10, BR-M08-48, BR-M08-50 |
| UC-M08-017 | embedded | SC-M08-016 | SC-M08-016/M2 | Xác định phạm vi trước khi trả log ở chức năng tra cứu. | FR-M08-17, BR-M08-40, BR-M08-41 |


| SVG nguồn | Số UC | Đối chiếu |
|---|---|---|
| C-M08 | 6 | Tập ID khớp US; không sửa/vẽ lại UML |
| D-M08-020 | 3 | Tập ID khớp US; không sửa/vẽ lại UML |
| D-M08-021 | 10 | Tập ID khớp US; không sửa/vẽ lại UML |
| D-M08-022 | 5 | Tập ID khớp US; không sửa/vẽ lại UML |
| D-M08-023 | 9 | Tập ID khớp US; không sửa/vẽ lại UML |
| D-M08-024 | 7 | Tập ID khớp US; không sửa/vẽ lại UML |
| D-M08-025 | 2 | Tập ID khớp US; không sửa/vẽ lại UML |


## 3. Luồng nghiệp vụ theo mục tiêu actor

<!-- sc:flows -->

| id | uc | primary | trigger | goal | completion | covered_ucs | rationale | scenario | sources |
|---|---|---|---|---|---|---|---|---|---|
| BF-M08-001 | UC-M08-020 | ACT-002 | Lan chọn Báo cáo trên bài P81. | Gửi báo cáo vi phạm một đối tượng | Báo cáo Mở hợp lệ được giữ trong đúng một vụ Mở của target; ưu tiên/thứ tự cập nhật, trả kết quả tiếp nhận. Chưa giải quyết vụ và chưa đổi trạng thái nội dung. | UC-M08-001, UC-M08-002, UC-M08-020 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-001 | FR-M08-01.01, FR-M08-01.06, FR-M08-01.11, FR-M08-01.12, FR-M08-01.15, FR-M08-01.16, FR-M08-01.19, FR-M08-01.20, BR-M08-01, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-55, FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-07.10, BR-M08-05, BR-M08-06, BR-M08-07, FR-M08-01.14, BR-M08-50, BR-M08-17, FR-M08-01.07, FR-M08-01.08, FR-M08-01.09, FR-M08-01.10, BR-M08-46, FR-M08-01.13, FR-M08-01.17, BR-M08-31, BR-M08-45, BR-M08-32 |
| BF-M08-002 | UC-M08-003 | ACT-008 | Mai mở hàng chờ báo cáo. | Tra cứu hàng chờ và điều tra chi tiết vụ | Trả đúng hàng chờ/chi tiết trong phạm vi staff, đủ dữ liệu điều tra và riêng tư; chỉ đọc không tự giữ vụ, áp biện pháp hoặc đóng vụ. | UC-M08-002, UC-M08-003, UC-M08-006 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-002 | FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.04, FR-M08-02.05, FR-M08-02.06, FR-M08-02.07, FR-M08-02.08, FR-M08-02.09, BR-M08-06, BR-M08-07, BR-M08-46, FR-M08-04.01, BR-M08-11, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-26, BR-M08-55 |
| BF-M08-003 | UC-M08-004 | ACT-008 | Mai chọn Nhận xử lý cho K81. | Nhận quyền xử lý duy nhất của một vụ | K81 Mở có đúng người xử lý hiện tại; người khác không được tác động/kết luận. Đây là mục tiêu nhận quyền đã xong, không khẳng định vụ đã được giải quyết. | UC-M08-004, UC-M08-006 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-003 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.08, FR-M08-03.09, FR-M08-16.07, BR-M08-08, BR-M08-09, BR-M08-46, BR-M08-05, FR-M08-02.06, FR-M08-02.09, BR-M08-44, BR-M08-55 |
| BF-M08-004 | UC-M08-021 | ACT-008 | Mai chọn K81 từ hàng chờ để giải quyết. | Giải quyết hoàn chỉnh một vụ báo cáo | Vụ và mọi báo cáo Mở đã được kết luận cùng kết quả, lưu người làm/lý do/thời điểm/nhật ký và sự kiện kết quả đúng người nhận. Nếu actor chọn biện pháp, thực hiện đến hiệu lực rồi vẫn quay lại để kết luận; chưa đóng vụ không là thành công của BF này. | UC-M08-002, UC-M08-003, UC-M08-004, UC-M08-005, UC-M08-006, UC-M08-007, UC-M08-008, UC-M08-009, UC-M08-011, UC-M08-014, UC-M08-015, UC-M08-021 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-004 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07, FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-05.01, FR-M08-05.03, BR-M08-10, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-12, BR-M08-13, BR-M08-39, BR-M08-40, FR-M08-03.05, FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, FR-M12-02.10, FR-M12-02.11, FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-53, FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-52, FR-M10-06.01, FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-50, BR-M11-28, FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-49, FR-M12-02.21, FR-M08-16.07, BR-M08-55 |
| BF-M08-005 | UC-M08-005 | ACT-008 | Mai chọn Bác bỏ, nhập lý do và gửi kết luận K81. | Kết luận một vụ đang giữ | Vụ và mọi báo cáo Mở đóng cùng kết luận; lý do/người làm/thời điểm và log được lưu; reporter người dùng chỉ nhận kết quả chung, target chỉ nhận chi tiết khi Có xử lý đúng loại/đường khiếu nại. | UC-M08-005, UC-M08-006 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-005 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40, FR-M08-02.06, FR-M08-03.07, BR-M08-46, FR-M08-02.09, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-16.07, FR-M08-03.01, FR-M08-03.05, FR-M08-03.06, BR-M08-44, BR-M08-55 |
| BF-M08-006 | UC-M08-007 | ACT-008 | Mai mở nội dung đang chờ xét của K81. | Xét và quyết định nội dung đang chờ sau AI | Quyết định xét hợp lệ đã áp vào nội dung; cảnh cáo chỉ tăng nếu actor chọn và đủ điều kiện. Vụ vẫn cần kết luận riêng; đây là mục tiêu xét nội dung, không phải BF giải quyết toàn vụ. | UC-M08-006, UC-M08-007, UC-M08-009, UC-M08-014 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-006 | FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, FR-M12-02.10, FR-M12-02.11, FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-43, BR-M08-53, BR-M08-22, BR-M08-54, FR-M08-03.01, FR-M08-03.05, FR-M08-16.07, BR-M08-55 |
| BF-M08-007 | UC-M08-008 | ACT-008 | Mai chọn Ẩn P81 trong K81 vì vi phạm. | Ẩn một bài viết hoặc bình luận vi phạm trong vụ | Nội dung hợp lệ đã Bị ẩn, dữ liệu/log giữ và hệ quả điểm/hiển thị theo owner; không tự cảnh cáo/ban hoặc kết luận vụ. | UC-M08-006, UC-M08-008 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-007 | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11, FR-M08-05.11, FR-M08-02.06, FR-M08-03.07, BR-M08-46, FR-M08-02.09, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-16.07, FR-M08-03.01, FR-M08-03.05, FR-M08-03.06, BR-M08-44, BR-M08-55 |
| BF-M08-008 | UC-M08-009 | ACT-008 | Mai chọn cảnh cáo Bình trong K81 và nhập lý do. | Cảnh cáo người vi phạm được xác định trong vụ | Cảnh cáo hợp lệ đã lưu issuer/lý do/vụ, tăng số lần/tính mức/reset hạn đúng chính sách, áp hạn chế/log và sự kiện app có khiếu nại. Vụ chưa tự đóng; không cảnh cáo mới khi target đã HEAVY. | UC-M08-006, UC-M08-009, UC-M08-011, UC-M08-014 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-008 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53, BR-M08-19, FR-M08-04.10, BR-M08-50, BR-M08-55, FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-52, FR-M10-06.01, FR-M08-02.06, FR-M08-03.07, FR-M08-02.09, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-16.07, FR-M08-03.01, FR-M08-03.05, FR-M08-03.06, BR-M08-44 |
| BF-M08-009 | UC-M08-010 | ACT-008 | Mai chọn bỏ cảnh cáo AI W81 của Bình. | Bỏ một cảnh cáo do AI ra | Record AI được giữ/đánh dấu đã bỏ, số lần giảm một và mức tính lại trong trường hợp số lần dương; hạn cũ giữ, nội dung ẩn giữ, log có. Không bao phủ phép trừ tại số lần 0 chưa chốt. | UC-M08-006, UC-M08-010, UC-M08-014 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-009 | FR-M08-11.01, FR-M08-11.02, FR-M08-11.03, FR-M08-11.04, FR-M08-11.05, FR-M08-16.05, BR-M08-28, BR-M08-31, BR-M08-54, BR-M08-44 |
| BF-M08-010 | UC-M08-011 | ACT-008 | Mai chọn Ban Bình trong K81, nhập lý do vi phạm. | Ban người vi phạm trong vụ theo quyết định con người | Đúng một ban Đang hiệu lực được tạo theo lệnh/lịch sử, account BANNED và Mod target bị thu hồi role nếu có; log/sự kiện app+email có khiếu nại. Không tự giải quyết vụ, tự AI ban hoặc thay thử thách cảnh cáo. | UC-M08-006, UC-M08-011 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-010 | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01, BR-M08-55, FR-M08-15.01, FR-M08-15.05, FR-M08-15.02, FR-M08-16.05, BR-M08-38, FR-M10-06.02, FR-M08-02.06, FR-M08-03.07, FR-M08-02.09, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-16.07, FR-M08-03.01, FR-M08-03.05, FR-M08-03.06, FR-M08-04.10, BR-M08-50, FR-M11-11.01, FR-M11-11.05, FR-M11-11.06, FR-M11-11.07, BR-M08-44, FR-M08-10.09 |
| BF-M08-011 | UC-M08-012 | ACT-008 | Mai chọn Gỡ ban B81 trực tiếp trên tài khoản Bình. | Gỡ sớm một ban đang hiệu lực | Ban Đã gỡ, account ACTIVE ngay; log và sự kiện app+email có, lịch sử còn tính; không phục hồi Mod hoặc nội dung. | UC-M08-006, UC-M08-012 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-011 | FR-M08-15.01, FR-M08-15.05, FR-M08-15.02, FR-M08-15.03, FR-M08-15.04, FR-M08-16.05, BR-M08-34, BR-M08-38, BR-M08-48, FR-M10-06.02, BR-M08-44 |
| BF-M08-012 | UC-M08-013 | ACT-002 | Lan mở thông tin mức cảnh cáo và thử thách của mình. | Xem mức cảnh cáo và hạn thử thách được phép | Mức và hạn hiện tại được trả đúng chủ thể/quyền riêng tư; không cập nhật mức từ một thao tác đọc, không hiển thị công khai. | UC-M08-013 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-012 | FR-M08-13.01, FR-M08-13.02, FR-M08-13.03, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-43, BR-M08-30, BR-M08-01, FR-M08-04.05 |
| BF-M08-013 | UC-M08-015 | ACT-008 | Mai chọn Ẩn nhóm G81 trong K81. | Ẩn nhóm vi phạm và toàn bộ nội dung của nhóm | G81 Bị ẩn và toàn bộ nội dung không ai nhìn thấy, dữ liệu/log giữ, không có bỏ ẩn. Vụ Mở chờ kết luận, Owner chưa tự nhận cảnh cáo/ban. | UC-M08-006, UC-M08-015 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-013 | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-16.07, FR-M08-03.01, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| BF-M08-014 | UC-M08-015 | ACT-008 | Mai chọn Khóa nhóm G81 trong K81. | Khóa hoạt động một nhóm vi phạm | G81 Bị khóa; mọi hạn chế/ngoại lệ ở D-LOCK có hiệu lực, đọc vẫn theo quyền cũ; log giữ. Không tự đóng vụ, phạt Owner hoặc tạo chức năng bỏ ẩn. | UC-M08-006, UC-M08-015 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-014 | FR-M08-18.04, FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-16.07, FR-M08-03.01, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| BF-M08-015 | UC-M08-016 | ACT-008 | Mai chọn Mở khóa G81 trực tiếp. | Mở khóa nhóm để hoạt động theo quyền thông thường | G81 Bình thường, hoạt động được phép lại trong phạm vi quyền M11; log có. Không đòi giữ vụ hoặc phục hồi nhóm đã Bị ẩn. | UC-M08-006, UC-M08-016 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-015 | FR-M08-18.07, FR-M08-18.09, FR-M08-18.10, FR-M08-16.05, BR-M08-48, BR-M08-50, BR-M11-28, BR-M08-44 |
| BF-M08-016 | UC-M08-025 | ACT-008 | Mai mở nhật ký kiểm duyệt để tra các vụ mình đã xử lý. | Tra cứu nhật ký kiểm duyệt trong phạm vi được phép | Tập và dòng nhật ký đúng phạm vi được trả chỉ đọc; Admin có phạm vi toàn bộ/lọc actor, Mod chỉ vụ mình xử lý hoặc đúng một thao tác của khiếu nại đang được mình xét. Không sửa/xóa log hoặc suy quyền từ link. | UC-M08-017, UC-M08-025 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; không tách vì role, trạng thái hoặc bước nội bộ. | SC-M08-016 | FR-M08-17.02, FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, FR-M08-17.01, FR-M08-17.03, FR-M08-17.04, FR-M08-17.05, FR-M08-17.06, BR-M08-39, BR-M08-40, BR-M08-41, BR-M08-43, BR-M08-44 |


Nhận quyền (SC003) và kết luận vụ đang giữ (SC005) có hợp đồng mục tiêu độc lập trong US. Chúng cũng được mở đầy đủ trong SC004, nơi actor bắt đầu giải quyết một vụ và phải đi đến kết luận; không kết thúc ở nhận quyền hay mới áp biện pháp. SC006–010/013–014 hoàn tất biện pháp riêng trên vụ đang giữ, không gọi đó là đã giải quyết toàn vụ. Bỏ AI, gỡ ban, mở khóa là chức năng trực tiếp không cần giữ vụ. Ẩn nhóm (mất hiển thị, không bỏ ẩn) và Khóa nhóm (ngăn hoạt động, vẫn đọc) là hai thao tác độc lập; bài/comment và Ban/Ban vĩnh viễn là các biến thể trong cùng chức năng tương ứng.

| Quan hệ US | Điểm chèn nguồn | Trở về nguồn |
|---|---|---|
| UC-M08-020 include UC-M08-001 | #uc-m08-020-main-3 | #uc-m08-020-main-4 |
| UC-M08-001 include UC-M08-002 | #uc-m08-001-main-3 | #uc-m08-001-main-4 |
| UC-M08-021 include UC-M08-004 | #uc-m08-021-main-2 | #uc-m08-021-main-3 |
| UC-M08-021 include UC-M08-003 | #uc-m08-021-main-3 | #uc-m08-021-main-4 |
| UC-M08-021 include UC-M08-005 | #uc-m08-021-main-5 | #uc-m08-021-main-6 |
| UC-M08-003 include UC-M08-006 | #uc-m08-003-main-1 | #uc-m08-003-main-2 |
| UC-M08-004 include UC-M08-006 | #uc-m08-004-main-1 | #uc-m08-004-main-2 |
| UC-M08-005 include UC-M08-006 | #uc-m08-005-main-1 | #uc-m08-005-main-2 |
| UC-M08-007 include UC-M08-006 | #uc-m08-007-main-1 | #uc-m08-007-main-2 |
| UC-M08-008 include UC-M08-006 | #uc-m08-008-main-1 | #uc-m08-008-main-2 |
| UC-M08-009 include UC-M08-006 | #uc-m08-009-main-1 | #uc-m08-009-main-2 |
| UC-M08-010 include UC-M08-006 | #uc-m08-010-main-1 | #uc-m08-010-main-2 |
| UC-M08-011 include UC-M08-006 | #uc-m08-011-main-1 | #uc-m08-011-main-2 |
| UC-M08-012 include UC-M08-006 | #uc-m08-012-main-1 | #uc-m08-012-main-2 |
| UC-M08-015 include UC-M08-006 | #uc-m08-015-main-1 | #uc-m08-015-main-2 |
| UC-M08-016 include UC-M08-006 | #uc-m08-016-main-1 | #uc-m08-016-main-2 |
| UC-M08-009 include UC-M08-014 | #uc-m08-009-main-3 | #uc-m08-009-main-4 |
| UC-M08-010 include UC-M08-014 | #uc-m08-010-main-2 | #uc-m08-010-main-3 |
| UC-M08-025 include UC-M08-017 | #uc-m08-025-main-2 | #uc-m08-025-main-3 |
| UC-M08-007 extend UC-M08-021 | EP-CASE-ACTION | #uc-m08-021-main-4 |
| UC-M08-008 extend UC-M08-021 | EP-CASE-ACTION | #uc-m08-021-main-4 |
| UC-M08-009 extend UC-M08-021 | EP-CASE-ACTION | #uc-m08-021-main-4 |
| UC-M08-011 extend UC-M08-021 | EP-CASE-ACTION | #uc-m08-021-main-4 |
| UC-M08-015 extend UC-M08-021 | EP-CASE-ACTION | #uc-m08-021-main-4 |
| UC-M08-009 extend UC-M08-007 | EP-FLAG-WARNING | #uc-m08-007-main-4 |


SC004 mở nhận vụ/điều tra/kết luận trong main; các nhánh EP-CASE-ACTION trên vụ P81 thực hiện biện pháp bằng bước actor–SYSTEM rồi nhập M5 để chọn biện pháp tiếp hoặc kết luận. Biến thể vụ C81/G81 chọn đúng target từ đầu, mở đủ nhận/điều tra/biện pháp/kết luận trong nhánh toàn hành trình; không thay target giữa lúc điều tra. M5 chuẩn Bác bỏ chỉ áp khi chưa có biện pháp; sau biện pháp đúng target chọn nhánh Có xử lý. Xét comment có cảnh cáo mở cả quyết định nội dung và chọn/lưu cảnh cáo; không tăng cảnh cáo hai lần vì vừa ở UC007 vừa ở core021. UC006 kiểm đọc không cần giữ, mutation cần giữ, bỏ AI/gỡ ban/mở khóa là trực tiếp. UC014 nằm ở lượt cập nhật; UC017 kiểm scope trước trả log. Quan hệ UML không bị đổi thành thứ tự bắt buộc của tất cả hành vi.

## 4. Scenario sáu phần

<a id="sc-m08-001"></a>

<!-- sc:scenario SC-M08-001 -->

### SC-M08-001

#### 1. Tên kịch bản chuẩn

Gửi báo cáo vi phạm một đối tượng — BF-M08-001; owner [UC-M08-020](../../us/US-M08.md#uc-m08-020).

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Có đối tượng cần báo cáo; phiên, khả năng nhìn thấy, loại đối tượng và trùng báo cáo được kiểm trong luồng. Chuẩn: Lan có phiên, được xem P81 của Bình, chưa báo cáo trong vụ Mở của P81; P81 không thuộc Admin.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-001 -->

| result | condition |
|---|---|
| SUCCESS | Báo cáo Mở hợp lệ được giữ trong đúng một vụ Mở của target; ưu tiên/thứ tự cập nhật, trả kết quả tiếp nhận. Chưa giải quyết vụ và chưa đổi trạng thái nội dung. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-001 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan chọn Báo cáo trên bài P81. | type=post; target=P81; reporter=U-LAN | M2 | FR-M08-01.01 |
| M2 | SYSTEM | Hệ thống kiểm phiên, target còn nhìn thấy, không tự báo cáo/không thuộc Admin và chưa trùng trong vụ Mở; trả đúng danh mục lý do của bài và giới hạn mô tả/ảnh. | P81 của Bình; chọn đúng một lý do; tối đa 3 ảnh, mỗi ảnh ≤5MB JPEG/PNG/WebP | M3 | FR-M08-01.01, FR-M08-01.06, FR-M08-01.11, FR-M08-01.12, FR-M08-01.15, FR-M08-01.16, FR-M08-01.19, FR-M08-01.20, BR-M08-01, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-55 |
| M3 | ACT-002 | Lan chọn Quấy rối/Bắt nạt, nhập mô tả và gửi báo cáo. | Mô tả: “Đoạn 2 nhắm vào cá nhân”; ảnh A81.png 2MB; một lý do | M4 | FR-M08-01.02, FR-M08-01.19, BR-M08-02, BR-M08-03, BR-M08-04 |
| M4 | SYSTEM | Hệ thống kiểm lại quyền/đối tượng, một lý do, mô tả và ảnh; lưu báo cáo Mở cùng reporter, loại/ID target, lý do, mô tả, bằng chứng. Chưa có vụ Mở nên tạo K81 Mở, gắn báo cáo, tính ưu tiên và đưa vào hàng chờ; trả báo cáo đã tiếp nhận. Chỉ gửi báo cáo không ẩn/gắn cờ bài. | R81 thuộc K81; max trọng số=10; số báo cáo=1; ưu tiên=12; P81 giữ nguyên trạng thái | END:SUCCESS | FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-01.19, FR-M08-07.10, BR-M08-05, BR-M08-06, BR-M08-07, BR-M08-47 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-001 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M4 | Đã có vụ Mở cho P81, Lan chưa có báo cáo trong vụ đó | E1.1 | FR-M08-01.02, FR-M08-01.03, FR-M08-01.05, FR-M08-07.10, BR-M08-05, BR-M08-06 |
| E2 | system | M4 | Chỉ có vụ cũ Đã xử lý, không còn vụ Mở của P81 | E2.1 | FR-M08-01.02, FR-M08-01.04, FR-M08-01.05, FR-M08-01.16, BR-M08-05, BR-M08-06, BR-M08-47 |
| E3 | user-choice | M1 | Lan báo cáo comment thay bài viết | E3.1 | FR-M08-01.01, FR-M08-01.14, FR-M08-01.19, FR-M08-01.20, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-50, FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-07.10, BR-M08-05, BR-M08-06, BR-M08-17 |
| E4 | user-choice | M1 | Lan báo cáo account thay bài viết | E4.1 | FR-M08-01.01, FR-M08-01.14, FR-M08-01.19, FR-M08-01.20, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-50, FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-07.10, BR-M08-05, BR-M08-06, BR-M08-17 |
| E5 | user-choice | M1 | Lan báo cáo group thay bài viết | E5.1 | FR-M08-01.01, FR-M08-01.14, FR-M08-01.19, FR-M08-01.20, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-50, FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-07.10, BR-M08-05, BR-M08-06, BR-M08-17 |
| E6 | system | M4 | Chưa chọn lý do | E6.1 | FR-M08-01.07, BR-M08-02, BR-M08-03, BR-M08-04, FR-M08-01.02, FR-M08-01.19 |
| E7 | system | M4 | Chọn Khác nhưng không có mô tả | E7.1 | FR-M08-01.08, BR-M08-02, BR-M08-03, BR-M08-04, FR-M08-01.02, FR-M08-01.19 |
| E8 | system | M4 | Chọn hơn một lý do | E8.1 | FR-M08-01.19, BR-M08-02, BR-M08-03, BR-M08-04, FR-M08-01.02 |
| E9 | system | M4 | Đính kèm ảnh thứ tư | E9.1 | FR-M08-01.09, BR-M08-02, BR-M08-03, BR-M08-04, FR-M08-01.02, FR-M08-01.19 |
| E10 | system | M4 | Một ảnh quá 5MB | E10.1 | FR-M08-01.10, BR-M08-02, BR-M08-03, BR-M08-04, FR-M08-01.02, FR-M08-01.19 |
| E11 | system | M4 | Ảnh không đúng định dạng | E11.1 | FR-M08-01.10, BR-M08-02, BR-M08-03, BR-M08-04, FR-M08-01.02, FR-M08-01.19 |
| E12 | system | M4 | Target trong nhóm Private mà Lan không là thành viên | E12.1 | FR-M08-01.11, BR-M08-46, BR-M08-47, BR-M08-55 |
| E13 | system | M4 | Target đã không còn nhìn thấy khi gửi | E13.1 | FR-M08-01.12, BR-M08-46, BR-M08-47, BR-M08-55 |
| E14 | system | M4 | Tự báo cáo bài, bình luận hoặc tài khoản mình | E14.1 | FR-M08-01.15, BR-M08-46, BR-M08-47, BR-M08-55 |
| E15 | system | M4 | Lan đã báo cáo cùng target trong vụ Mở | E15.1 | FR-M08-01.16, BR-M08-46, BR-M08-47, BR-M08-55 |
| E16 | system | M4 | Target là bài, bình luận, tài khoản Admin hoặc nhóm Owner Admin | E16.1 | FR-M08-01.20, BR-M08-46, BR-M08-47, BR-M08-55 |
| E17 | system | M4 | Lan đang HEAVY và P81 Khóa toàn bộ nhưng vẫn được nhìn thấy | E17.1 | FR-M08-01.13, FR-M08-01.17, BR-M08-31, BR-M08-45, BR-M08-47 |
| E18 | system | M1 | ACT-001 — Guest yêu cầu chức năng cần tài khoản. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E18.1 | FR-M08-01.01, FR-M08-01.06, BR-M08-01, BR-M08-32 |
| E19 | system | M1 | ACT-008 — Mod Mai gửi báo cáo đối tượng USER khác mình, không phải nội dung/nhóm Owner Admin và chưa trùng. Actor khởi tạo ACT-008; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E19.1 | FR-M08-01.01, FR-M08-01.06, FR-M08-01.11, FR-M08-01.12, FR-M08-01.15, FR-M08-01.16, FR-M08-01.19, FR-M08-01.20, BR-M08-01, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-55, FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-07.10, BR-M08-05, BR-M08-06, BR-M08-07 |
| E20 | system | M1 | ACT-007 — Admin An gửi báo cáo đối tượng USER khác mình, không phải nội dung/nhóm Owner Admin và chưa trùng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E20.1 | FR-M08-01.01, FR-M08-01.06, FR-M08-01.11, FR-M08-01.12, FR-M08-01.15, FR-M08-01.16, FR-M08-01.19, FR-M08-01.20, BR-M08-01, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-55, FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-07.10, BR-M08-05, BR-M08-06, BR-M08-07 |
| E21 | system | M1 | ACT-007 — An Admin gửi báo cáo đối tượng được miễn là post/comment/account Admin khác hoặc nhóm Owner Admin. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E21.1 | FR-M08-01.01, FR-M08-01.20, BR-M08-55 |


<!-- sc:branch SC-M08-001 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm lại dữ liệu/quyền hợp lệ rồi lưu R81 vào K80 Mở hiện có; không tạo vụ thứ hai hoặc mở lại vụ đã đóng. Tính lại ưu tiên và trả đã tiếp nhận. | K80 trước: 2 báo cáo, max trọng số 5, ưu tiên 9; thêm lý do trọng số 10→3 báo cáo, ưu tiên 16; nội dung không đổi | END:SUCCESS | FR-M08-01.02, FR-M08-01.03, FR-M08-01.05, FR-M08-07.10, BR-M08-05, BR-M08-06 |


<!-- sc:branch SC-M08-001 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống giữ nguyên vụ cũ và kết luận, lưu báo cáo mới vào vụ Mở K82 mới, tính ưu tiên và trả tiếp nhận; không áp trùng báo cáo của vụ đã kết luận sang vụ mới. | K79 Đã xử lý không đổi; K82/R82 Mở; một báo cáo lý do trọng số 10→ưu tiên 12 | END:SUCCESS | FR-M08-01.02, FR-M08-01.04, FR-M08-01.05, FR-M08-01.16, BR-M08-05, BR-M08-06, BR-M08-47 |


<!-- sc:branch SC-M08-001 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-002 | Lan chọn Báo cáo trên C81. | type=comment; target=C81; còn nhìn thấy, không thuộc Admin | E3.2 | FR-M08-01.01 |
| E3.2 | SYSTEM | Hệ thống kiểm phiên, target, quyền nhìn thấy và chưa trùng; trả đúng danh mục lý do theo loại, một lựa chọn và giới hạn ảnh/mô tả. | Bình luận chưa quét AI cũng báo cáo được | E3.3 | FR-M08-01.01, FR-M08-01.14, FR-M08-01.19, FR-M08-01.20, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-50 |
| E3.3 | ACT-002 | Lan chọn lý do và gửi báo cáo. | Bạo lực/Đe dọa; mô tả minh họa hợp lệ; ảnh trống (không bắt buộc) | E3.4 | FR-M08-01.02, FR-M08-01.19, BR-M08-02, BR-M08-04 |
| E3.4 | SYSTEM | Hệ thống kiểm dữ liệu/quyền hiện tại, lưu báo cáo Mở vào vụ Mở của đúng target hoặc tạo vụ nếu chưa có; tính ưu tiên và trả tiếp nhận, không áp chế tài. | R82/C81; chưa có vụ Mở→K82; trọng số 10, số báo cáo 1, ưu tiên 12 | END:SUCCESS | FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-07.10, BR-M08-05, BR-M08-06, BR-M08-17, BR-M08-50 |


<!-- sc:branch SC-M08-001 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-002 | Lan chọn Báo cáo trên U-BINH. | type=account; target=U-BINH; còn nhìn thấy, không thuộc Admin | E4.2 | FR-M08-01.01 |
| E4.2 | SYSTEM | Hệ thống kiểm phiên, target, quyền nhìn thấy và chưa trùng; trả đúng danh mục lý do theo loại, một lựa chọn và giới hạn ảnh/mô tả. | Không yêu cầu sửa avatar/bio | E4.3 | FR-M08-01.01, FR-M08-01.14, FR-M08-01.19, FR-M08-01.20, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-50 |
| E4.3 | ACT-002 | Lan chọn lý do và gửi báo cáo. | Quấy rối/Bắt nạt có hệ thống; mô tả minh họa hợp lệ; ảnh trống (không bắt buộc) | E4.4 | FR-M08-01.02, FR-M08-01.19, BR-M08-02, BR-M08-04 |
| E4.4 | SYSTEM | Hệ thống kiểm dữ liệu/quyền hiện tại, lưu báo cáo Mở vào vụ Mở của đúng target hoặc tạo vụ nếu chưa có; tính ưu tiên và trả tiếp nhận, không áp chế tài. | R82/U-BINH; chưa có vụ Mở→K82; trọng số 10, số báo cáo 1, ưu tiên 12 | END:SUCCESS | FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-07.10, BR-M08-05, BR-M08-06, BR-M08-17, BR-M08-50 |


<!-- sc:branch SC-M08-001 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-002 | Lan chọn Báo cáo trên G81. | type=group; target=G81; còn nhìn thấy, không thuộc Admin | E5.2 | FR-M08-01.01 |
| E5.2 | SYSTEM | Hệ thống kiểm phiên, target, quyền nhìn thấy và chưa trùng; trả đúng danh mục lý do theo loại, một lựa chọn và giới hạn ảnh/mô tả. | Owner là Bình USER, khác Lan; không dùng nhóm của chính staff | E5.3 | FR-M08-01.01, FR-M08-01.14, FR-M08-01.19, FR-M08-01.20, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-50 |
| E5.3 | ACT-002 | Lan chọn lý do và gửi báo cáo. | Group giả mạo; mô tả minh họa hợp lệ; ảnh trống (không bắt buộc) | E5.4 | FR-M08-01.02, FR-M08-01.19, BR-M08-02, BR-M08-04 |
| E5.4 | SYSTEM | Hệ thống kiểm dữ liệu/quyền hiện tại, lưu báo cáo Mở vào vụ Mở của đúng target hoặc tạo vụ nếu chưa có; tính ưu tiên và trả tiếp nhận, không áp chế tài. | R82/G81; chưa có vụ Mở→K82; trọng số 10, số báo cáo 1, ưu tiên 12 | END:SUCCESS | FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-07.10, BR-M08-05, BR-M08-06, BR-M08-17, BR-M08-50 |


<!-- sc:branch SC-M08-001 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối dữ liệu không hợp lệ, nêu phần cần sửa; chưa lưu báo cáo hoặc tạo vụ. | reason=trống | E6.2 | FR-M08-01.07, BR-M08-02, BR-M08-03, BR-M08-04 |
| E6.2 | ACT-002 | Lan sửa dữ liệu theo yêu cầu và gửi lại. | Một lý do Quấy rối; mô tả hợp lệ; 3 ảnh JPEG/PNG/WebP lần lượt 5MB, 2MB, 1MB | M4 | FR-M08-01.02, FR-M08-01.19, BR-M08-02, BR-M08-03, BR-M08-04 |


<!-- sc:branch SC-M08-001 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối dữ liệu không hợp lệ, nêu phần cần sửa; chưa lưu báo cáo hoặc tạo vụ. | reason=Khác; description=trống | E7.2 | FR-M08-01.08, BR-M08-02, BR-M08-03, BR-M08-04 |
| E7.2 | ACT-002 | Lan sửa dữ liệu theo yêu cầu và gửi lại. | Một lý do Quấy rối; mô tả hợp lệ; 3 ảnh JPEG/PNG/WebP lần lượt 5MB, 2MB, 1MB | M4 | FR-M08-01.02, FR-M08-01.19, BR-M08-02, BR-M08-03, BR-M08-04 |


<!-- sc:branch SC-M08-001 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống từ chối dữ liệu không hợp lệ, nêu phần cần sửa; chưa lưu báo cáo hoặc tạo vụ. | reason=[Spam, Quấy rối] | E8.2 | FR-M08-01.19, BR-M08-02, BR-M08-03, BR-M08-04 |
| E8.2 | ACT-002 | Lan sửa dữ liệu theo yêu cầu và gửi lại. | Một lý do Quấy rối; mô tả hợp lệ; 3 ảnh JPEG/PNG/WebP lần lượt 5MB, 2MB, 1MB | M4 | FR-M08-01.02, FR-M08-01.19, BR-M08-02, BR-M08-03, BR-M08-04 |


<!-- sc:branch SC-M08-001 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống từ chối dữ liệu không hợp lệ, nêu phần cần sửa; chưa lưu báo cáo hoặc tạo vụ. | 4 ảnh đều PNG, từng ảnh 2MB | E9.2 | FR-M08-01.09, BR-M08-02, BR-M08-03, BR-M08-04 |
| E9.2 | ACT-002 | Lan sửa dữ liệu theo yêu cầu và gửi lại. | Một lý do Quấy rối; mô tả hợp lệ; 3 ảnh JPEG/PNG/WebP lần lượt 5MB, 2MB, 1MB | M4 | FR-M08-01.02, FR-M08-01.19, BR-M08-02, BR-M08-03, BR-M08-04 |


<!-- sc:branch SC-M08-001 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống từ chối dữ liệu không hợp lệ, nêu phần cần sửa; chưa lưu báo cáo hoặc tạo vụ. | 3 ảnh PNG, có ảnh 5.1MB | E10.2 | FR-M08-01.10, BR-M08-02, BR-M08-03, BR-M08-04 |
| E10.2 | ACT-002 | Lan sửa dữ liệu theo yêu cầu và gửi lại. | Một lý do Quấy rối; mô tả hợp lệ; 3 ảnh JPEG/PNG/WebP lần lượt 5MB, 2MB, 1MB | M4 | FR-M08-01.02, FR-M08-01.19, BR-M08-02, BR-M08-03, BR-M08-04 |


<!-- sc:branch SC-M08-001 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | SYSTEM | Hệ thống từ chối dữ liệu không hợp lệ, nêu phần cần sửa; chưa lưu báo cáo hoặc tạo vụ. | evidence=A81.gif | E11.2 | FR-M08-01.10, BR-M08-02, BR-M08-03, BR-M08-04 |
| E11.2 | ACT-002 | Lan sửa dữ liệu theo yêu cầu và gửi lại. | Một lý do Quấy rối; mô tả hợp lệ; 3 ảnh JPEG/PNG/WebP lần lượt 5MB, 2MB, 1MB | M4 | FR-M08-01.02, FR-M08-01.19, BR-M08-02, BR-M08-03, BR-M08-04 |


<!-- sc:branch SC-M08-001 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | SYSTEM | Hệ thống từ chối tiếp nhận báo cáo theo điều kiện nguồn; không tạo báo cáo/vụ hoặc đổi trạng thái target. | P81 thuộc G-PRIVATE; Lan ngoài nhóm | END:REJECTED | FR-M08-01.11, BR-M08-46, BR-M08-47, BR-M08-55 |


<!-- sc:branch SC-M08-001 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | SYSTEM | Hệ thống từ chối tiếp nhận báo cáo theo điều kiện nguồn; không tạo báo cáo/vụ hoặc đổi trạng thái target. | P81 bị xóa/ẩn trước kiểm lại | END:REJECTED | FR-M08-01.12, BR-M08-46, BR-M08-47, BR-M08-55 |


<!-- sc:branch SC-M08-001 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | SYSTEM | Hệ thống từ chối tiếp nhận báo cáo theo điều kiện nguồn; không tạo báo cáo/vụ hoặc đổi trạng thái target. | target thuộc U-LAN, type thuộc post/comment/account | END:REJECTED | FR-M08-01.15, BR-M08-46, BR-M08-47, BR-M08-55 |


<!-- sc:branch SC-M08-001 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | SYSTEM | Hệ thống từ chối tiếp nhận báo cáo theo điều kiện nguồn; không tạo báo cáo/vụ hoặc đổi trạng thái target. | K81 Mở đã có R80 reporter Lan | END:REJECTED | FR-M08-01.16, BR-M08-46, BR-M08-47, BR-M08-55 |


<!-- sc:branch SC-M08-001 E16 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E16.1 | SYSTEM | Hệ thống từ chối tiếp nhận báo cáo theo điều kiện nguồn; không tạo báo cáo/vụ hoặc đổi trạng thái target. | U-ADMIN là Admin; miễn báo cáo theo loại nêu trên | END:REJECTED | FR-M08-01.20, BR-M08-46, BR-M08-47, BR-M08-55 |


<!-- sc:branch SC-M08-001 E17 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E17.1 | SYSTEM | Hệ thống vẫn cho báo cáo, kiểm dữ liệu hợp lệ, lưu báo cáo vào đúng vụ Mở hoặc tạo vụ mới, tính ưu tiên rồi trả tiếp nhận. Không lấy HEAVY/khóa toàn bộ thay quyền nhìn thấy. | Lan HEAVY; P81 Khóa toàn bộ; chưa trùng; một báo cáo trọng số 10→ưu tiên 12 nếu vụ mới | END:SUCCESS | FR-M08-01.13, FR-M08-01.17, BR-M08-31, BR-M08-45, BR-M08-47 |


**E18 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng cần tài khoản. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-001 E18 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E18.1 | ACT-001 | Guest chọn gửi báo cáo vi phạm một đối tượng. | Không có phiên; chưa phát sinh dữ liệu nghiệp vụ | E18.2 | FR-M08-01.01 |
| E18.2 | SYSTEM | Hệ thống từ chối chức năng yêu cầu người dùng đã đăng nhập; không lưu báo cáo hoặc trả mức cảnh cáo riêng tư. | Không tạo báo cáo/quan hệ quyền từ ID | END:REJECTED | FR-M08-01.06, BR-M08-01, BR-M08-32 |


**E19 — thay toàn bộ M1 đến kết thúc:** Mod Mai gửi báo cáo đối tượng USER khác mình, không phải nội dung/nhóm Owner Admin và chưa trùng. Actor khởi tạo ACT-008; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-001 E19 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E19.1 | ACT-008 | Mod Mai chọn Báo cáo trên bài P81. | type=post; target=P81; reporter=STAFF-REPORTER | E19.2 | FR-M08-01.01 |
| E19.2 | SYSTEM | Hệ thống kiểm phiên, target còn nhìn thấy, không tự báo cáo/không thuộc Admin và chưa trùng trong vụ Mở; trả đúng danh mục lý do của bài và giới hạn mô tả/ảnh. | P81 của Bình; chọn đúng một lý do; tối đa 3 ảnh, mỗi ảnh ≤5MB JPEG/PNG/WebP | E19.3 | FR-M08-01.01, FR-M08-01.06, FR-M08-01.11, FR-M08-01.12, FR-M08-01.15, FR-M08-01.16, FR-M08-01.19, FR-M08-01.20, BR-M08-01, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-55 |
| E19.3 | ACT-008 | Mod Mai chọn Quấy rối/Bắt nạt, nhập mô tả và gửi báo cáo. | Mô tả: “Đoạn 2 nhắm vào cá nhân”; ảnh A81.png 2MB; một lý do | E19.4 | FR-M08-01.02, FR-M08-01.19, BR-M08-02, BR-M08-03, BR-M08-04 |
| E19.4 | SYSTEM | Hệ thống kiểm lại quyền/đối tượng, một lý do, mô tả và ảnh; lưu báo cáo Mở cùng reporter, loại/ID target, lý do, mô tả, bằng chứng. Chưa có vụ Mở nên tạo K81 Mở, gắn báo cáo, tính ưu tiên và đưa vào hàng chờ; trả báo cáo đã tiếp nhận. Chỉ gửi báo cáo không ẩn/gắn cờ bài. | R81 thuộc K81; max trọng số=10; số báo cáo=1; ưu tiên=12; P81 giữ nguyên trạng thái | END:SUCCESS | FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-01.19, FR-M08-07.10, BR-M08-05, BR-M08-06, BR-M08-07, BR-M08-47 |


**E20 — thay toàn bộ M1 đến kết thúc:** Admin An gửi báo cáo đối tượng USER khác mình, không phải nội dung/nhóm Owner Admin và chưa trùng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-001 E20 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E20.1 | ACT-007 | Admin An chọn Báo cáo trên bài P81. | type=post; target=P81; reporter=STAFF-REPORTER | E20.2 | FR-M08-01.01 |
| E20.2 | SYSTEM | Hệ thống kiểm phiên, target còn nhìn thấy, không tự báo cáo/không thuộc Admin và chưa trùng trong vụ Mở; trả đúng danh mục lý do của bài và giới hạn mô tả/ảnh. | P81 của Bình; chọn đúng một lý do; tối đa 3 ảnh, mỗi ảnh ≤5MB JPEG/PNG/WebP | E20.3 | FR-M08-01.01, FR-M08-01.06, FR-M08-01.11, FR-M08-01.12, FR-M08-01.15, FR-M08-01.16, FR-M08-01.19, FR-M08-01.20, BR-M08-01, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-55 |
| E20.3 | ACT-007 | Admin An chọn Quấy rối/Bắt nạt, nhập mô tả và gửi báo cáo. | Mô tả: “Đoạn 2 nhắm vào cá nhân”; ảnh A81.png 2MB; một lý do | E20.4 | FR-M08-01.02, FR-M08-01.19, BR-M08-02, BR-M08-03, BR-M08-04 |
| E20.4 | SYSTEM | Hệ thống kiểm lại quyền/đối tượng, một lý do, mô tả và ảnh; lưu báo cáo Mở cùng reporter, loại/ID target, lý do, mô tả, bằng chứng. Chưa có vụ Mở nên tạo K81 Mở, gắn báo cáo, tính ưu tiên và đưa vào hàng chờ; trả báo cáo đã tiếp nhận. Chỉ gửi báo cáo không ẩn/gắn cờ bài. | R81 thuộc K81; max trọng số=10; số báo cáo=1; ưu tiên=12; P81 giữ nguyên trạng thái | END:SUCCESS | FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-01.19, FR-M08-07.10, BR-M08-05, BR-M08-06, BR-M08-07, BR-M08-47 |


**E21 — thay toàn bộ M1 đến kết thúc:** An Admin gửi báo cáo đối tượng được miễn là post/comment/account Admin khác hoặc nhóm Owner Admin. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-001 E21 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E21.1 | ACT-007 | An chọn báo cáo một đối tượng của Admin khác. | type=post/comment/account của ADM-BAO hoặc group có Owner ADM-BAO; còn thấy | E21.2 | FR-M08-01.01 |
| E21.2 | SYSTEM | Hệ thống từ chối báo cáo đối tượng Admin được miễn, không tạo báo cáo hoặc vụ. | Không có ngoại lệ cho reporter Admin | END:REJECTED | FR-M08-01.20, BR-M08-55 |


<!-- sc:end SC-M08-001 -->

<a id="sc-m08-002"></a>

<!-- sc:scenario SC-M08-002 -->

### SC-M08-002

#### 1. Tên kịch bản chuẩn

Tra cứu hàng chờ và điều tra chi tiết vụ — BF-M08-002; owner [UC-M08-003](../../us/US-M08.md#uc-m08-003).

#### 2. Actor thực hiện

ACT-008 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Có yêu cầu đọc hàng chờ/vụ; không buộc giữ vụ để chỉ xem. Chuẩn Mai là Mod, K81 về Bình USER không phải mình/Mod/Admin; dữ liệu chỉ số có mẫu số dương.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-002 -->

| result | condition |
|---|---|
| SUCCESS | Trả đúng hàng chờ/chi tiết trong phạm vi staff, đủ dữ liệu điều tra và riêng tư; chỉ đọc không tự giữ vụ, áp biện pháp hoặc đóng vụ. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-002 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai mở hàng chờ báo cáo. | actor=MOD-MAI; bộ K81/K82/K83 | M2 | FR-M08-02.01 |
| M2 | SYSTEM | Hệ thống kiểm vai trò/phạm vi đọc; trả mọi vụ Mở được phép, ưu tiên giảm dần và hòa theo mở trước, đánh dấu người giữ/yêu cầu ban. Không giới hạn thời gian phải xử lý vụ. | K81=16 mở 08:00; K82=16 mở 08:05; K83=9 mở 07:00→K81,K82,K83; K82 do Mod khác giữ; K83 yêu cầu ban | M3 | FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.04, FR-M08-02.05, FR-M08-02.06, FR-M08-02.07, FR-M08-02.08, FR-M08-02.09, BR-M08-06, BR-M08-07, BR-M08-46 |
| M3 | ACT-008 | Mai chọn K81 để điều tra. | Mở đúng vụ P81, chỉ đọc; chưa nhận xử lý | M4 | FR-M08-04.01, BR-M08-11 |
| M4 | SYSTEM | Hệ thống kiểm lại phạm vi và trả từng báo cáo, reporter/lý do/mô tả/ảnh, nội dung đúng vụ, lịch sử vụ đã đóng/kết luận, mức cảnh cáo và chỉ số tập trung. Hiện danh tính thật cho staff nếu bài ẩn danh/tác giả vô hiệu hóa; mục AI hiện Hệ thống (AI) và nhóm AI. Không cấp quyền duyệt nội dung lưu giữ ngoài ngữ cảnh; chỉ xem khi chưa giữ không gia hạn quyền giữ của người khác. | Lan: 6 báo cáo bị bác về chính P81 / 10 báo cáo đã xử lý của Lan trong 90×24h=0.6; mốc đúng T−90×24h bị loại; reporter khác 2/10=0.2. Bình LIGHT, hạn 12/11 10:00+07 | END:SUCCESS | FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-002 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M4 | Nội dung vụ đã tự ẩn, xóa hoặc xóa vĩnh viễn nhưng có bản lưu đúng ngữ cảnh | E1.1 | FR-M08-04.02, FR-M08-04.03, FR-M08-04.06, FR-M08-04.07, BR-M08-14, BR-M08-15 |
| E2 | system | M2 | AI tổng hoặc Moderation đang tắt | E2.1 | FR-M08-02.01, FR-M08-02.05, FR-M08-02.07, BR-M08-07, BR-M08-26 |
| E3 | system | M4 | Đòi duyệt nội dung người khác đã xóa/ẩn ngoài vụ, lịch sử hoặc khiếu nại liên quan | E3.1 | FR-M08-04.07, BR-M08-15 |
| E4 | system | M2 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | E4.1 | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |
| E5 | system | M2 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | E5.1 | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |
| E6 | system | M1 | ACT-007 — An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.04, FR-M08-02.05, FR-M08-02.06, FR-M08-02.07, FR-M08-02.08, FR-M08-02.09, BR-M08-06, BR-M08-07, BR-M08-46, FR-M08-04.01, BR-M08-11, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| E7 | system | M1 | ACT-002 — User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.04, FR-M08-02.05, FR-M08-02.06, FR-M08-02.07, FR-M08-02.08, FR-M08-02.09, BR-M08-06, BR-M08-07, BR-M08-46, BR-M08-44 |
| E8 | system | M1 | ACT-001 — Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.04, FR-M08-02.05, FR-M08-02.06, FR-M08-02.07, FR-M08-02.08, FR-M08-02.09, BR-M08-06, BR-M08-07, BR-M08-46, BR-M08-44 |
| E9 | system | M1 | ACT-007 — An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.04, FR-M08-02.05, FR-M08-02.06, FR-M08-02.07, FR-M08-02.08, FR-M08-02.09, BR-M08-06, BR-M08-07, BR-M08-46, FR-M08-04.01, BR-M08-11, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| E10 | system | M1 | ACT-007 — An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M08-02.01, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |


<!-- sc:branch SC-M08-002 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm vụ/lịch sử/khiếu nại liên quan rồi trả bản lưu của đúng nội dung và báo cáo cho Mai đủ quyền; vẫn giữ riêng tư với người bị báo cáo. Không mở tìm kiếm/duyệt toàn bộ nội dung lưu giữ hoặc Nháp/Bị từ chối của người khác. | P81 đã xóa vĩnh viễn; bản lưu liên quan K81; không đổi trạng thái xóa hoặc biến thành nội dung công khai | END:SUCCESS | FR-M08-04.02, FR-M08-04.03, FR-M08-04.06, FR-M08-04.07, BR-M08-14, BR-M08-15 |


<!-- sc:branch SC-M08-002 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống vẫn kiểm quyền và trả hàng chờ Mở đúng thứ tự/phạm vi, gồm backlog AI đã tồn tại và vụ thủ công; không xóa vụ hoặc ngừng giải quyết chỉ vì cờ tắt. | AI tổng=false hoặc Moderation=false; K81=16,K82=16,K83=9; thứ tự theo mốc mở | M3 | FR-M08-02.01, FR-M08-02.05, FR-M08-02.07, BR-M08-07, BR-M08-26 |


<!-- sc:branch SC-M08-002 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống không trả bản lưu ngoài ngữ cảnh được phép; không coi vai trò staff là quyền duyệt tùy ý. | target=P99 không liên quan K81 | END:REJECTED | FR-M08-04.07, BR-M08-15 |


<!-- sc:branch SC-M08-002 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-MAI | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |


<!-- sc:branch SC-M08-002 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-HOA | END:REJECTED | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |


**E6 — thay toàn bộ M1 đến kết thúc:** An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-002 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-007 | An mở hàng chờ báo cáo. | actor=ADM-AN; bộ K81/K82/K83 | E6.2 | FR-M08-02.01 |
| E6.2 | SYSTEM | Hệ thống kiểm vai trò/phạm vi đọc; trả mọi vụ Mở được phép, ưu tiên giảm dần và hòa theo mở trước, đánh dấu người giữ/yêu cầu ban. Không giới hạn thời gian phải xử lý vụ. | K81=16 mở 08:00; K82=16 mở 08:05; K83=9 mở 07:00→K81,K82,K83; K82 do Mod khác giữ; K83 yêu cầu ban | E6.3 | FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.04, FR-M08-02.05, FR-M08-02.06, FR-M08-02.07, FR-M08-02.08, FR-M08-02.09, BR-M08-06, BR-M08-07, BR-M08-46 |
| E6.3 | ACT-007 | An chọn K81 để điều tra. | Mở đúng vụ P81, chỉ đọc; chưa nhận xử lý | E6.4 | FR-M08-04.01, BR-M08-11 |
| E6.4 | SYSTEM | Hệ thống kiểm lại phạm vi và trả từng báo cáo, reporter/lý do/mô tả/ảnh, nội dung đúng vụ, lịch sử vụ đã đóng/kết luận, mức cảnh cáo và chỉ số tập trung. Hiện danh tính thật cho staff nếu bài ẩn danh/tác giả vô hiệu hóa; mục AI hiện Hệ thống (AI) và nhóm AI. Không cấp quyền duyệt nội dung lưu giữ ngoài ngữ cảnh; chỉ xem khi chưa giữ không gia hạn quyền giữ của người khác. | Lan: 6 báo cáo bị bác về chính P81 / 10 báo cáo đã xử lý của Lan trong 90×24h=0.6; mốc đúng T−90×24h bị loại; reporter khác 2/10=0.2. Bình LIGHT, hạn 12/11 10:00+07 | END:SUCCESS | FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |


**E7 — thay toàn bộ M1 đến kết thúc:** User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-002 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-002 | Người yêu cầu chọn tra cứu hàng chờ và điều tra chi tiết vụ. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E7.2 | FR-M08-02.01 |
| E7.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.04, FR-M08-02.05, FR-M08-02.06, FR-M08-02.07, FR-M08-02.08, FR-M08-02.09, BR-M08-06, BR-M08-07, BR-M08-46, BR-M08-44 |


**E8 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-002 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-001 | Người yêu cầu chọn tra cứu hàng chờ và điều tra chi tiết vụ. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E8.2 | FR-M08-02.01 |
| E8.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.04, FR-M08-02.05, FR-M08-02.06, FR-M08-02.07, FR-M08-02.08, FR-M08-02.09, BR-M08-06, BR-M08-07, BR-M08-46, BR-M08-44 |


**E9 — thay toàn bộ M1 đến kết thúc:** An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-002 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-007 | An mở hàng chờ báo cáo. | actor=ADM-AN; bộ K81/K82/K83 | E9.2 | FR-M08-02.01 |
| E9.2 | SYSTEM | Hệ thống kiểm vai trò/phạm vi đọc; trả mọi vụ Mở được phép, ưu tiên giảm dần và hòa theo mở trước, đánh dấu người giữ/yêu cầu ban. Không giới hạn thời gian phải xử lý vụ. | K81=16 mở 08:00; K82=16 mở 08:05; K83=9 mở 07:00→K81,K82,K83; K82 do Mod khác giữ; K83 yêu cầu ban | E9.3 | FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.04, FR-M08-02.05, FR-M08-02.06, FR-M08-02.07, FR-M08-02.08, FR-M08-02.09, BR-M08-06, BR-M08-07, BR-M08-46 |
| E9.3 | ACT-007 | An chọn K81 để điều tra. | Mở đúng vụ P81, chỉ đọc; chưa nhận xử lý | E9.4 | FR-M08-04.01, BR-M08-11 |
| E9.4 | SYSTEM | Hệ thống kiểm lại phạm vi và trả từng báo cáo, reporter/lý do/mô tả/ảnh, nội dung đúng vụ, lịch sử vụ đã đóng/kết luận, mức cảnh cáo và chỉ số tập trung. Hiện danh tính thật cho staff nếu bài ẩn danh/tác giả vô hiệu hóa; mục AI hiện Hệ thống (AI) và nhóm AI. Không cấp quyền duyệt nội dung lưu giữ ngoài ngữ cảnh; chỉ xem khi chưa giữ không gia hạn quyền giữ của người khác. | Lan: 6 báo cáo bị bác về chính P81 / 10 báo cáo đã xử lý của Lan trong 90×24h=0.6; mốc đúng T−90×24h bị loại; reporter khác 2/10=0.2. Hoa LIGHT, hạn 12/11 10:00+07 | END:SUCCESS | FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |


**E10 — thay toàn bộ M1 đến kết thúc:** An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-002 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-007 | An yêu cầu tra cứu hàng chờ và điều tra chi tiết vụ đối với vụ của chính mình. | target type=post/comment/account; owner=ADM-AN; không phải nhóm | E10.2 | FR-M08-02.01 |
| E10.2 | SYSTEM | Hệ thống loại vụ khỏi phạm vi nhìn thấy/nhận và từ chối truy cập/xử lý đối tượng của chính An theo nguồn, không cấp quyền nhờ role Admin. | Không trả dữ liệu tố cáo/không áp biện pháp | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |


<!-- sc:end SC-M08-002 -->

<a id="sc-m08-003"></a>

<!-- sc:scenario SC-M08-003 -->

### SC-M08-003

#### 1. Tên kịch bản chuẩn

Nhận quyền xử lý duy nhất của một vụ — BF-M08-003; owner [UC-M08-004](../../us/US-M08.md#uc-m08-004).

#### 2. Actor thực hiện

ACT-008 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Vụ/người thao tác được nhận diện; kiểm lại quyền, trạng thái Mở và người giữ khi nhận. Chuẩn Mai đủ phạm vi, K81 Mở chưa ai giữ.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-003 -->

| result | condition |
|---|---|
| SUCCESS | K81 Mở có đúng người xử lý hiện tại; người khác không được tác động/kết luận. Đây là mục tiêu nhận quyền đã xong, không khẳng định vụ đã được giải quyết. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-003 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai chọn Nhận xử lý cho K81. | K81: vụ Mở về P81 của Bình/U-BINH (USER, khác người xử lý), 3 báo cáo Mở của Lan, Chi và Hệ thống (AI); ưu tiên 10+2×3=16; không có người giữ. Mai/MOD-MAI là Mod hệ thống. P81 còn thấy hoặc có bản lưu đúng ngữ cảnh vụ; không phải Nháp/Bị từ chối. | M2 | FR-M08-03.01 |
| M2 | SYSTEM | Hệ thống kiểm staff, phạm vi target, vụ còn Mở/chưa ai giữ rồi gắn duy nhất Mai làm người giữ và trả kết quả đã nhận. Bắt đầu mốc hoạt động; không đóng vụ, không ghi log nhận. Mục tiêu độc lập này là nhận quyền, việc giải quyết toàn vụ ở SC004. | holder(K81)=MOD-MAI; activity=T; tự nhả sau 30 phút không thao tác hợp lệ; K81 vẫn Mở | END:SUCCESS | FR-M08-03.01, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.08, FR-M08-03.09, FR-M08-16.07, BR-M08-08, BR-M08-09, BR-M08-46 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-003 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Vụ do người khác giữ | E1.1 | FR-M08-03.02, BR-M08-08 |
| E2 | system | M2 | Vụ đã được kết luận trước lúc nhận | E2.1 | FR-M08-03.05, BR-M08-05 |
| E3 | system | M2 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | E3.1 | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |
| E4 | system | M2 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | E4.1 | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |
| E5 | system | M1 | ACT-007 — An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.08, FR-M08-03.09, FR-M08-16.07, BR-M08-08, BR-M08-09, BR-M08-46 |
| E6 | system | M1 | ACT-002 — User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.08, FR-M08-03.09, FR-M08-16.07, BR-M08-08, BR-M08-09, BR-M08-46, BR-M08-44 |
| E7 | system | M1 | ACT-001 — Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.08, FR-M08-03.09, FR-M08-16.07, BR-M08-08, BR-M08-09, BR-M08-46, BR-M08-44 |
| E8 | system | M1 | ACT-007 — An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.08, FR-M08-03.09, FR-M08-16.07, BR-M08-08, BR-M08-09, BR-M08-46 |
| E9 | system | M1 | ACT-007 — An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M08-03.01, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |


<!-- sc:branch SC-M08-003 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối nhận chồng; giữ người đang giữ và không cấp quyền xử lý cho Mai. | K81 holder=MOD-HOA | END:REJECTED | FR-M08-03.02, BR-M08-08 |


<!-- sc:branch SC-M08-003 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối nhận vụ đã đóng; không mở lại vụ. | K81 Đã xử lý | END:REJECTED | FR-M08-03.05, BR-M08-05 |


<!-- sc:branch SC-M08-003 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-MAI | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |


<!-- sc:branch SC-M08-003 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-HOA | END:REJECTED | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |


**E5 — thay toàn bộ M1 đến kết thúc:** An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-003 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-007 | An chọn Nhận xử lý cho K81. | K81: vụ Mở về P81 của Bình/U-BINH (USER, khác người xử lý), 3 báo cáo Mở của Lan, Chi và Hệ thống (AI); ưu tiên 10+2×3=16; không có người giữ. An/ADM-AN là Mod hệ thống. P81 còn thấy hoặc có bản lưu đúng ngữ cảnh vụ; không phải Nháp/Bị từ chối. | E5.2 | FR-M08-03.01 |
| E5.2 | SYSTEM | Hệ thống kiểm staff, phạm vi target, vụ còn Mở/chưa ai giữ rồi gắn duy nhất An làm người giữ và trả kết quả đã nhận. Bắt đầu mốc hoạt động; không đóng vụ, không ghi log nhận. Mục tiêu độc lập này là nhận quyền, việc giải quyết toàn vụ ở SC004. | holder(K81)=ADM-AN; activity=T; tự nhả sau 30 phút không thao tác hợp lệ; K81 vẫn Mở | END:SUCCESS | FR-M08-03.01, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.08, FR-M08-03.09, FR-M08-16.07, BR-M08-08, BR-M08-09, BR-M08-46 |


**E6 — thay toàn bộ M1 đến kết thúc:** User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-003 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-002 | Người yêu cầu chọn nhận quyền xử lý duy nhất của một vụ. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E6.2 | FR-M08-03.01 |
| E6.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-03.01, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.08, FR-M08-03.09, FR-M08-16.07, BR-M08-08, BR-M08-09, BR-M08-46, BR-M08-44 |


**E7 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-003 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-001 | Người yêu cầu chọn nhận quyền xử lý duy nhất của một vụ. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E7.2 | FR-M08-03.01 |
| E7.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-03.01, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.08, FR-M08-03.09, FR-M08-16.07, BR-M08-08, BR-M08-09, BR-M08-46, BR-M08-44 |


**E8 — thay toàn bộ M1 đến kết thúc:** An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-003 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-007 | An chọn Nhận xử lý cho K81. | K81: vụ Mở về P81 của Hoa/MOD-HOA (MODERATOR, khác người xử lý), 3 báo cáo Mở của Lan, Chi và Hệ thống (AI); ưu tiên 10+2×3=16; không có người giữ. An/ADM-AN là Mod hệ thống. P81 còn thấy hoặc có bản lưu đúng ngữ cảnh vụ; không phải Nháp/Bị từ chối. | E8.2 | FR-M08-03.01 |
| E8.2 | SYSTEM | Hệ thống kiểm staff, phạm vi target, vụ còn Mở/chưa ai giữ rồi gắn duy nhất An làm người giữ và trả kết quả đã nhận. Bắt đầu mốc hoạt động; không đóng vụ, không ghi log nhận. Mục tiêu độc lập này là nhận quyền, việc giải quyết toàn vụ ở SC004. | holder(K81)=ADM-AN; activity=T; tự nhả sau 30 phút không thao tác hợp lệ; K81 vẫn Mở | END:SUCCESS | FR-M08-03.01, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.08, FR-M08-03.09, FR-M08-16.07, BR-M08-08, BR-M08-09, BR-M08-46 |


**E9 — thay toàn bộ M1 đến kết thúc:** An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-003 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-007 | An yêu cầu nhận quyền xử lý duy nhất của một vụ đối với vụ của chính mình. | target type=post/comment/account; owner=ADM-AN; không phải nhóm | E9.2 | FR-M08-03.01 |
| E9.2 | SYSTEM | Hệ thống loại vụ khỏi phạm vi nhìn thấy/nhận và từ chối truy cập/xử lý đối tượng của chính An theo nguồn, không cấp quyền nhờ role Admin. | Không trả dữ liệu tố cáo/không áp biện pháp | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |


<!-- sc:end SC-M08-003 -->

<a id="sc-m08-004"></a>

<!-- sc:scenario SC-M08-004 -->

### SC-M08-004

#### 1. Tên kịch bản chuẩn

Giải quyết hoàn chỉnh một vụ báo cáo — BF-M08-004; owner [UC-M08-021](../../us/US-M08.md#uc-m08-021).

#### 2. Actor thực hiện

ACT-008 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Có yêu cầu giải quyết vụ; không giả định đã có quyền giữ. Chuẩn K81 Mở/chưa giữ, Mai đủ phạm vi, mẫu số chỉ số dương. Đường Bác bỏ chưa áp bất kỳ biện pháp nào; phần chưa chốt sau biện pháp được giữ tại GAP005.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-004 -->

| result | condition |
|---|---|
| SUCCESS | Vụ và mọi báo cáo Mở đã được kết luận cùng kết quả, lưu người làm/lý do/thời điểm/nhật ký và sự kiện kết quả đúng người nhận. Nếu actor chọn biện pháp, thực hiện đến hiệu lực rồi vẫn quay lại để kết luận; chưa đóng vụ không là thành công của BF này. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-004 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai chọn K81 từ hàng chờ để giải quyết. | K81: vụ Mở về P81 của Bình/U-BINH (USER, khác người xử lý), 3 báo cáo Mở của Lan, Chi và Hệ thống (AI); ưu tiên 10+2×3=16; không có người giữ. Mai/MOD-MAI là Mod hệ thống. P81 còn thấy hoặc có bản lưu đúng ngữ cảnh vụ; không phải Nháp/Bị từ chối. | M2 | FR-M08-02.01, FR-M08-03.01 |
| M2 | SYSTEM | Hệ thống kiểm vai trò/phạm vi đọc và khả năng nhận; dùng hàng chờ ưu tiên giảm dần (max trọng số + 2×số báo cáo), hòa theo vụ mở trước, trả K81 Mở, chưa có người giữ và cho Mai chọn nhận. Vụ tự nhắm mình/Mod theo quyền bị loại trước khi xem/nhận. | K81 ưu tiên 16 về Bình USER; Mai khác Bình; chưa giữ | M3 | BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |
| M3 | ACT-008 | Mai chọn Nhận xử lý và mở K81 để điều tra. | Yêu cầu nắm quyền K81 hiện Mở/chưa giữ | M4 | FR-M08-03.01, FR-M08-04.01 |
| M4 | SYSTEM | Hệ thống kiểm lại quyền/phạm vi và gắn Mai là người giữ duy nhất nếu vừa nhận; mở hồ sơ điều tra: từng báo cáo/người gửi/lý do/mô tả/ảnh, nội dung và bản lưu đúng vụ, lịch sử đã kết luận, mức cảnh cáo, chỉ số tập trung theo 90×24h. Hiện danh tính thật cho staff và nhãn Hệ thống (AI) đúng dữ liệu; cập nhật mốc xem vụ của chính Mai đang giữ. | K81 Mở, holder Mai; Lan 6/10=0.6, mẫu số dương; Bình USER LIGHT; dữ liệu tố cáo không đưa cho Bình | M5 | FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| M5 | ACT-008 | Mai đánh giá không đủ căn cứ, chọn Bác bỏ và nhập lý do để kết luận vụ. | K81 chưa áp biện pháp; lý do=Không đủ căn cứ vi phạm | M6 | FR-M08-05.01, FR-M08-05.03, BR-M08-10 |
| M6 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Bác bỏ cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “không phát hiện vi phạm”; không gửi kết quả cho Bình hoặc mục AI. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Bác bỏ; lý do=Không đủ căn cứ vi phạm; biện pháp=không có biện pháp; actor Mai; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-004 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Mai đã là người giữ hợp lệ lúc chọn giải quyết | E1.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19 |
| E2 | system | M4 | Người khác nhận K81 trước lúc xử lý yêu cầu nhận của Mai | E2.1 | FR-M08-03.02, FR-M08-03.03, BR-M08-08 |
| E3 | system | M4 | Vụ đã đóng trước lúc Mai nhận | E3.1 | FR-M08-03.05 |
| E4 | system | M6 | Thiếu lý do kết luận; quyền giữ/vụ vẫn hợp lệ | E4.1 | FR-M08-05.09, FR-M08-05.01 |
| E5 | system | M6 | Vụ đã được đóng trước xử lý kết luận | E5.1 | FR-M08-05.08 |
| E6 | user-choice | M5 | Tại EP-CASE-ACTION, người giữ chọn Ẩn bài vi phạm với target đúng vụ và guard của biện pháp hợp lệ | E6.1 | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11 |
| E7 | user-choice | M1 | Chọn từ đầu vụ về C81 với mọi guard nhận/biện pháp/kết luận hợp lệ; Tại EP-CASE-ACTION, người giữ chọn Ẩn bình luận vi phạm với target đúng vụ và guard của biện pháp hợp lệ | E7.1 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07, FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-06.02, FR-M08-06.01, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, FR-M12-02.10, FR-M12-02.11, FR-M08-05.11, FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-39, BR-M08-40 |
| E8 | user-choice | M5 | Tại EP-CASE-ACTION, người giữ chọn Cảnh cáo tác giả theo đánh giá con người với target đúng vụ và guard của biện pháp hợp lệ | E8.1 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |
| E9 | user-choice | M5 | Tại EP-CASE-ACTION, người giữ chọn Ban theo lịch sử với target đúng vụ và guard của biện pháp hợp lệ | E9.1 | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |
| E10 | user-choice | M5 | Tại EP-CASE-ACTION, người giữ chọn Ban vĩnh viễn thủ công với target đúng vụ và guard của biện pháp hợp lệ | E10.1 | FR-M08-14.02, FR-M08-14.01, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |
| E11 | user-choice | M1 | Chọn từ đầu vụ về G81 với mọi guard nhận/biện pháp/kết luận hợp lệ; Tại EP-CASE-ACTION, người giữ chọn Ẩn nhóm vi phạm với target đúng vụ và guard của biện pháp hợp lệ | E11.1 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07, FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-50, BR-M11-28, FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-39, BR-M08-40 |
| E12 | user-choice | M1 | Chọn từ đầu vụ về G81 với mọi guard nhận/biện pháp/kết luận hợp lệ; Tại EP-CASE-ACTION, người giữ chọn Khóa nhóm vi phạm với target đúng vụ và guard của biện pháp hợp lệ | E12.1 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07, FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-18.04, FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-50, BR-M11-28, FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-39, BR-M08-40 |
| E13 | user-choice | M5 | Tại EP-CASE-ACTION, người giữ chọn Xét bài đang bị gắn cờ, quyết định không vi phạm với target đúng vụ và guard của biện pháp hợp lệ | E13.1 | FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| E14 | user-choice | M1 | Chọn từ đầu vụ về C81 với mọi guard nhận/biện pháp/kết luận hợp lệ; Tại EP-CASE-ACTION, người giữ chọn Xét comment trung bình và chọn cảnh cáo với target đúng vụ và guard của biện pháp hợp lệ | E14.1 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07, FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-07.04, FR-M08-07.05, BR-M08-23, FR-M12-02.21, FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-53, FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-39, BR-M08-40 |
| E15 | user-choice | M5 | Đã áp biện pháp đối với người bị báo cáo/nội dung/nhóm và Mai chọn Có xử lý để hoàn tất vụ | E15.1 | FR-M08-05.01, FR-M08-05.03, BR-M08-10, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |
| E16 | user-choice | M1 | Chọn từ đầu vụ về C81 với mọi guard nhận/biện pháp/kết luận hợp lệ; Chỉ xét nội dung đang chờ và xác định vi phạm, không chọn cảnh cáo | E16.1 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07, FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-07.04, FR-M08-07.05, BR-M08-23, FR-M12-02.21, FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-39, BR-M08-40 |
| E17 | system | M2 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | E17.1 | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |
| E18 | system | M2 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | E18.1 | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |
| E19 | system | M6 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | E19.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |
| E20 | user-choice | M6 | Vụ tự nhả 30 phút, còn Mở/chưa ai giữ và Mai chọn nhận lại trước tiếp tục | E20.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-03.01, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-16.07 |
| E21 | user-choice | M5 | Tại EP-CASE-ACTION, Nội dung đã ẩn khi người giữ chọn biện pháp | E21.1 | FR-M08-06.05 |
| E22 | user-choice | M5 | Tại EP-CASE-ACTION, Nội dung không còn chờ xét khi người giữ chọn biện pháp | E22.1 | FR-M08-07.07 |
| E23 | user-choice | M5 | Tại EP-CASE-ACTION, Target đã HEAVY khi người giữ chọn biện pháp | E23.1 | FR-M08-10.10, FR-M08-14.11, BR-M08-36 |
| E24 | user-choice | M5 | Tại EP-CASE-ACTION, Mod đòi chế tài Mod khác khi người giữ chọn biện pháp | E24.1 | FR-M08-10.08, FR-M08-14.09, BR-M08-46 |
| E25 | user-choice | M5 | Tại EP-CASE-ACTION, Target có ban Đang hiệu lực khi người giữ chọn biện pháp | E25.1 | FR-M08-14.13, BR-M08-52 |
| E26 | user-choice | M5 | Sau biện pháp hợp lệ, Mai chọn Có xử lý nhưng quên lý do | E26.1 | FR-M08-05.01, FR-M08-05.09, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |
| E27 | user-choice | M1 | Vụ từ đầu về nhóm G81, người giữ chọn Khóa nhóm rồi cảnh cáo Owner Bình USER (khác Mai, chưa HEAVY) | E27.1 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07, FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-18.04, FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-50, BR-M11-28, FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-53, FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-39, BR-M08-40 |
| E28 | user-choice | M5 | Vụ P81 từ đầu, tại EP-CASE-ACTION Mai xét bài gắn cờ điểm trung bình và chọn Ẩn bài + cảnh cáo tác giả | E28.1 | FR-M08-07.02, FR-M08-07.05, BR-M08-23, FR-M08-07.01, FR-M08-07.03, FR-M08-07.04, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, FR-M12-02.10, FR-M12-02.11, FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-43, BR-M08-53 |
| E29 | system | M1 | ACT-007 — An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E29.1 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07, FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-05.01, FR-M08-05.03, BR-M08-10, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-12, BR-M08-13, BR-M08-39, BR-M08-40 |
| E30 | system | M1 | ACT-002 — User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E30.1 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |
| E31 | system | M1 | ACT-001 — Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E31.1 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |
| E32 | system | M1 | ACT-007 — An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E32.1 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07, FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-05.01, FR-M08-05.03, BR-M08-10, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-12, BR-M08-13, BR-M08-39, BR-M08-40 |
| E33 | system | M1 | ACT-007 — An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E33.1 | FR-M08-02.01, FR-M08-03.01, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |


<!-- sc:branch SC-M08-004 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm K81 Mở và quyền giữ hiện tại của Mai; cho mở chi tiết, không bắt nhận lại. | K81 holder Mai, chưa mất quyền | E1.2 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| E1.2 | ACT-008 | Mai mở chi tiết K81 để tiếp tục điều tra. | Chính người giữ mở lại vụ | E1.3 | FR-M08-04.01 |
| E1.3 | SYSTEM | Hệ thống kiểm lại quyền/phạm vi và mở hồ sơ điều tra: từng báo cáo/người gửi/lý do/mô tả/ảnh, nội dung và bản lưu đúng vụ, lịch sử đã kết luận, mức cảnh cáo, chỉ số tập trung theo 90×24h. Hiện danh tính thật cho staff và nhãn Hệ thống (AI) đúng dữ liệu; cập nhật mốc xem vụ của chính Mai đang giữ. | K81 Mở, holder Mai; Lan 6/10=0.6, mẫu số dương; Bình USER LIGHT; dữ liệu tố cáo không đưa cho Bình | M5 | FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |


<!-- sc:branch SC-M08-004 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối cấp quyền; không cho tác động hoặc kết luận thay người giữ. | K81 holder=MOD-HOA | END:REJECTED | FR-M08-03.02, FR-M08-03.03, BR-M08-08 |


<!-- sc:branch SC-M08-004 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối nhận/giải quyết lại vụ đã đóng. | K81 Đã xử lý | END:REJECTED | FR-M08-03.05 |


<!-- sc:branch SC-M08-004 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối kết luận thiếu lý do; vụ và các báo cáo vẫn Mở, giữ hiệu ứng hợp lệ đã có. | reason=trống; holder Mai; K81 Mở | E4.2 | FR-M08-05.09 |
| E4.2 | ACT-008 | Mai nhập lý do và gửi lại cùng lựa chọn kết luận. | Bác bỏ, Không đủ căn cứ vi phạm; chưa có biện pháp | M6 | FR-M08-05.01, FR-M08-05.09 |


<!-- sc:branch SC-M08-004 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối kết luận lần hai; giữ kết quả đã lưu, không phát lại sự kiện thành công mới. | K81 Đã xử lý | END:REJECTED | FR-M08-05.08 |


<!-- sc:branch SC-M08-004 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-008 | Mai chọn Ẩn P81 trong K81 vì vi phạm. | P81 Đã đăng/Bình thường; lý do=Quấy rối | E6.2 | FR-M08-06.01 |
| E6.2 | SYSTEM | Hệ thống kiểm staff, phạm vi và còn giữ K81, đúng target chưa ẩn; chuyển P81 sang Bị ẩn (Bị Mod ẩn theo M03), giữ dữ liệu, ghi log actor/target/lý do/thời điểm. Áp hiển thị và trừ ngay phần điểm từ upvote hiệu lực theo M12, ghi số điểm đã trừ; trả đã ẩn. Không xóa bài người khác hoặc tự đóng vụ. | P81→Bị ẩn; tác giả có 100 điểm, P81 có 5 Post Star × 2 điểm/Star = 10 điểm hiệu lực → 90, ghi khoản đã trừ 10 điểm cho P81; K81 vẫn Mở | M5 | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11, FR-M12-02.01, BR-M12-05 |


<!-- sc:branch SC-M08-004 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | ACT-008 | Mai chọn giải quyết K81 về C81 từ hàng chờ. | Ngay từ đầu K81 là vụ Mở về C81 của Bình USER, không phải vụ của P81; 3 báo cáo, ưu tiên 16; chưa ai giữ | E7.2 | FR-M08-02.01, FR-M08-03.01 |
| E7.2 | SYSTEM | Hệ thống kiểm staff/phạm vi, thứ tự ưu tiên và vụ Mở/chưa giữ; trả đúng vụ của C81 để nhận, không chuyển sang target khác. | Mai khác tác giả/Owner Bình; nếu nhóm thì Owner không là Admin | E7.3 | BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |
| E7.3 | ACT-008 | Mai chọn Nhận xử lý và mở chi tiết K81 về C81. | Đúng target của vụ vừa chọn, chưa ai giữ | E7.4 | FR-M08-03.01, FR-M08-04.01 |
| E7.4 | SYSTEM | Hệ thống kiểm lại quyền/phạm vi và gắn Mai là người giữ duy nhất nếu vừa nhận; mở hồ sơ điều tra: từng báo cáo/người gửi/lý do/mô tả/ảnh, nội dung và bản lưu đúng vụ, lịch sử đã kết luận, mức cảnh cáo, chỉ số tập trung theo 90×24h. Hiện danh tính thật cho staff và nhãn Hệ thống (AI) đúng dữ liệu; cập nhật mốc xem vụ của chính Mai đang giữ. | K81 Mở, holder Mai; Lan 6/10=0.6, mẫu số dương; Bình USER LIGHT; dữ liệu tố cáo không đưa cho Bình | E7.5 | FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| E7.5 | ACT-008 | Mai chọn Ẩn C81 trong K81 vì vi phạm. | C81 chưa Bị ẩn; K81 Mở về C81 do Mai giữ, Bình USER | E7.6 | FR-M08-06.02 |
| E7.6 | SYSTEM | Hệ thống kiểm staff/phạm vi/giữ/target và chưa ẩn; chuyển C81 Bị ẩn, ghi log và áp trừ phần điểm từ upvote hiệu lực theo M12, trả đã ẩn. Không xóa bình luận hoặc tự đóng vụ; thông báo kết luận comment không có khiếu nại. | C81 Bình thường→Bị ẩn; 3 điểm upvote hiệu lực→trừ 3; K81 Mở | E7.7 | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11, FR-M08-05.11 |
| E7.7 | ACT-008 | Mai chọn Có xử lý, nhập lý do Vi phạm đã xác định và kết luận K81. | Target vẫn C81; biện pháp vừa áp trong K81; Mai vẫn giữ | E7.8 | FR-M08-05.01, FR-M08-05.03 |
| E7.8 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Có xử lý cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “đã có biện pháp xử lý”; người bị báo cáo (Owner nếu nhóm) nhận lý do/mức xử lý, không nhận danh tính/lý do/mô tả/ảnh tố cáo. Chỉ cảnh cáo, ban, bài ẩn có đường khiếu nại; comment/nhóm ẩn-khóa không có. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Có xử lý; lý do=Vi phạm đã xác định; biện pháp=biện pháp vừa áp trên C81; actor Mai; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


<!-- sc:branch SC-M08-004 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | ACT-008 | Mai chọn cảnh cáo Bình trong K81 và nhập lý do. | target=U-BINH USER; 2/LIGHT; reason=Quấy rối | E8.2 | FR-M08-10.01 |
| E8.2 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Mod/Admin đối với Mod và chưa HEAVY; ghi cảnh cáo do Mai ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Bình: số lần 2→3, mức mới MEDIUM, hạn=T+10×24h; record issuer=Mai; K81 Mở; cảnh cáo chỉ app, không email | M5 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |


<!-- sc:branch SC-M08-004 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | ACT-008 | Mai chọn Ban Bình trong K81, nhập lý do vi phạm. | command=Ban; target=U-BINH; reason=Tái phạm đã xác định; số ban trước 0 | E9.2 | FR-M08-14.01 |
| E9.2 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Admin, Mod chỉ do Admin xử lý và không có ban Đang hiệu lực. Đếm lịch sử mọi ban từng hiệu lực, gồm đã gỡ/vĩnh viễn thủ công, loại Bị lật; áp thời hạn leo thang. Ghi ban Đang hiệu lực với lý do/người làm/mốc bắt đầu, đặt account BANNED; nếu target là Mod thì thu hồi vai trò về USER. Ghi log, phát sự kiện app+email lý do/đường khiếu nại, trả đã ban; không reset cảnh cáo/thử thách hoặc tự đóng vụ. | Bình; lệnh=Ban; số ban trước tính được=0; thời hạn=30×24h; bắt đầu T; account→BANNED; K81 Mở | M5 | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |


<!-- sc:branch SC-M08-004 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | ACT-008 | Mai chọn Ban vĩnh viễn Bình trong K81 và nhập lý do. | Lịch sử được tính 0; không có ban Đang hiệu lực; lựa chọn thủ công | E10.2 | FR-M08-14.02 |
| E10.2 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Admin, Mod chỉ do Admin xử lý và không có ban Đang hiệu lực. Áp Ban vĩnh viễn thủ công, bỏ leo thang. Ghi ban Đang hiệu lực với lý do/người làm/mốc bắt đầu, đặt account BANNED; nếu target là Mod thì thu hồi vai trò về USER. Ghi log, phát sự kiện app+email lý do/đường khiếu nại, trả đã ban; không reset cảnh cáo/thử thách hoặc tự đóng vụ. | Bình; lệnh=Ban vĩnh viễn; số ban trước tính được=0; thời hạn=vĩnh viễn; bắt đầu T; account→BANNED; K81 Mở | M5 | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |


<!-- sc:branch SC-M08-004 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-008 | Mai chọn giải quyết K81 về G81 từ hàng chờ. | Ngay từ đầu K81 là vụ Mở về G81 của Bình USER, không phải vụ của P81; 3 báo cáo, ưu tiên 16; chưa ai giữ | E11.2 | FR-M08-02.01, FR-M08-03.01 |
| E11.2 | SYSTEM | Hệ thống kiểm staff/phạm vi, thứ tự ưu tiên và vụ Mở/chưa giữ; trả đúng vụ của G81 để nhận, không chuyển sang target khác. | Mai khác tác giả/Owner Bình; nếu nhóm thì Owner không là Admin | E11.3 | BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |
| E11.3 | ACT-008 | Mai chọn Nhận xử lý và mở chi tiết K81 về G81. | Đúng target của vụ vừa chọn, chưa ai giữ | E11.4 | FR-M08-03.01, FR-M08-04.01 |
| E11.4 | SYSTEM | Hệ thống kiểm lại quyền/phạm vi và gắn Mai là người giữ duy nhất nếu vừa nhận; mở hồ sơ điều tra: từng báo cáo/người gửi/lý do/mô tả/ảnh, nội dung và bản lưu đúng vụ, lịch sử đã kết luận, mức cảnh cáo, chỉ số tập trung theo 90×24h. Hiện danh tính thật cho staff và nhãn Hệ thống (AI) đúng dữ liệu; cập nhật mốc xem vụ của chính Mai đang giữ. | K81 Mở, holder Mai; Lan 6/10=0.6, mẫu số dương; Bình USER LIGHT; dữ liệu tố cáo không đưa cho Bình | E11.5 | FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| E11.5 | ACT-008 | Mai chọn Ẩn nhóm G81 trong K81. | G81 Bình thường; lý do=Nội dung người lớn đã xác định | E11.6 | FR-M08-18.01 |
| E11.6 | SYSTEM | Hệ thống kiểm staff/phạm vi/còn giữ vụ nhóm và trạng thái cho phép; chuyển nhóm Bị ẩn, ẩn nhóm và toàn bộ nội dung với mọi người kể cả Owner/thành viên, giữ dữ liệu và không có bỏ ẩn. Ghi log và trả biện pháp đã áp; không tự cảnh cáo/ban Owner hoặc đóng vụ. | G81 Bình thường→Bị ẩn; K81 Mở do Mai giữ; Owner Bình USER, Mai khác Owner | E11.7 | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |
| E11.7 | ACT-008 | Mai chọn Có xử lý, nhập lý do Vi phạm đã xác định và kết luận K81. | Target vẫn G81; biện pháp vừa áp trong K81; Mai vẫn giữ | E11.8 | FR-M08-05.01, FR-M08-05.03 |
| E11.8 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Có xử lý cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “đã có biện pháp xử lý”; người bị báo cáo (Owner nếu nhóm) nhận lý do/mức xử lý, không nhận danh tính/lý do/mô tả/ảnh tố cáo. Chỉ cảnh cáo, ban, bài ẩn có đường khiếu nại; comment/nhóm ẩn-khóa không có. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Có xử lý; lý do=Vi phạm đã xác định; biện pháp=biện pháp vừa áp trên G81; actor Mai; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


<!-- sc:branch SC-M08-004 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | ACT-008 | Mai chọn giải quyết K81 về G81 từ hàng chờ. | Ngay từ đầu K81 là vụ Mở về G81 của Bình USER, không phải vụ của P81; 3 báo cáo, ưu tiên 16; chưa ai giữ | E12.2 | FR-M08-02.01, FR-M08-03.01 |
| E12.2 | SYSTEM | Hệ thống kiểm staff/phạm vi, thứ tự ưu tiên và vụ Mở/chưa giữ; trả đúng vụ của G81 để nhận, không chuyển sang target khác. | Mai khác tác giả/Owner Bình; nếu nhóm thì Owner không là Admin | E12.3 | BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |
| E12.3 | ACT-008 | Mai chọn Nhận xử lý và mở chi tiết K81 về G81. | Đúng target của vụ vừa chọn, chưa ai giữ | E12.4 | FR-M08-03.01, FR-M08-04.01 |
| E12.4 | SYSTEM | Hệ thống kiểm lại quyền/phạm vi và gắn Mai là người giữ duy nhất nếu vừa nhận; mở hồ sơ điều tra: từng báo cáo/người gửi/lý do/mô tả/ảnh, nội dung và bản lưu đúng vụ, lịch sử đã kết luận, mức cảnh cáo, chỉ số tập trung theo 90×24h. Hiện danh tính thật cho staff và nhãn Hệ thống (AI) đúng dữ liệu; cập nhật mốc xem vụ của chính Mai đang giữ. | K81 Mở, holder Mai; Lan 6/10=0.6, mẫu số dương; Bình USER LIGHT; dữ liệu tố cáo không đưa cho Bình | E12.5 | FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| E12.5 | ACT-008 | Mai chọn Khóa nhóm G81 trong K81. | G81 Bình thường; reason=Vi phạm đã xác định | E12.6 | FR-M08-18.04 |
| E12.6 | SYSTEM | Hệ thống kiểm staff/phạm vi/còn giữ vụ nhóm và trạng thái cho phép; chuyển nhóm Bị khóa; vẫn đọc theo Public/Private và giữ bookmark/báo cáo, chặn đầy đủ thao tác tại D-LOCK với mọi người kể cả Owner/Group Mod. Member/Group Mod vẫn tự rời, Owner không tự rời; hệ thống vẫn tự chuyển Owner khi mất quyền ngoài ý muốn. Ghi log và trả biện pháp đã áp; không tự cảnh cáo/ban Owner hoặc đóng vụ. | G81 Bình thường→Bị khóa; K81 Mở do Mai giữ; Owner Bình USER, Mai khác Owner | E12.7 | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |
| E12.7 | ACT-008 | Mai chọn Có xử lý, nhập lý do Vi phạm đã xác định và kết luận K81. | Target vẫn G81; biện pháp vừa áp trong K81; Mai vẫn giữ | E12.8 | FR-M08-05.01, FR-M08-05.03 |
| E12.8 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Có xử lý cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “đã có biện pháp xử lý”; người bị báo cáo (Owner nếu nhóm) nhận lý do/mức xử lý, không nhận danh tính/lý do/mô tả/ảnh tố cáo. Chỉ cảnh cáo, ban, bài ẩn có đường khiếu nại; comment/nhóm ẩn-khóa không có. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Có xử lý; lý do=Vi phạm đã xác định; biện pháp=biện pháp vừa áp trên G81; actor Mai; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


<!-- sc:branch SC-M08-004 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | ACT-008 | Mai mở nội dung đang chờ xét của K81. | P81 Bị gắn cờ; holder Mai | E13.2 | FR-M08-07.06 |
| E13.2 | SYSTEM | Hệ thống kiểm staff/phạm vi/quyền giữ, vụ và nội dung còn chờ xét; trả nội dung, loại/điểm AI và các quyết định tương ứng, không tự tăng cảnh cáo. | P81 Bị gắn cờ; nhóm Quấy rối, điểm minh họa 0.7 | E13.3 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| E13.3 | ACT-008 | Mai quyết định giữ bài vì không vi phạm. | P81; giữ bài, không cảnh cáo | E13.4 | FR-M08-07.01 |
| E13.4 | SYSTEM | Hệ thống kiểm lại guard, chuyển P81 về Bình thường và trả kết quả đã xét. Không tự kết luận vụ hoặc đồng nhất quyết định nội dung với chế tài tác giả. | P81 Bị gắn cờ→Bình thường; K81 vẫn Mở, holder Mai; số cảnh cáo không tăng | M5 | FR-M08-07.01, FR-M08-07.05, FR-M08-07.07, BR-M08-23, BR-M08-48 |


<!-- sc:branch SC-M08-004 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | ACT-008 | Mai chọn giải quyết K81 về C81 từ hàng chờ. | Ngay từ đầu K81 là vụ Mở về C81 của Bình USER, không phải vụ của P81; 3 báo cáo, ưu tiên 16; chưa ai giữ | E14.2 | FR-M08-02.01, FR-M08-03.01 |
| E14.2 | SYSTEM | Hệ thống kiểm staff/phạm vi, thứ tự ưu tiên và vụ Mở/chưa giữ; trả đúng vụ của C81 để nhận, không chuyển sang target khác. | Mai khác tác giả/Owner Bình; nếu nhóm thì Owner không là Admin | E14.3 | BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |
| E14.3 | ACT-008 | Mai chọn Nhận xử lý và mở chi tiết K81 về C81. | Đúng target của vụ vừa chọn, chưa ai giữ | E14.4 | FR-M08-03.01, FR-M08-04.01 |
| E14.4 | SYSTEM | Hệ thống kiểm lại quyền/phạm vi và gắn Mai là người giữ duy nhất nếu vừa nhận; mở hồ sơ điều tra: từng báo cáo/người gửi/lý do/mô tả/ảnh, nội dung và bản lưu đúng vụ, lịch sử đã kết luận, mức cảnh cáo, chỉ số tập trung theo 90×24h. Hiện danh tính thật cho staff và nhãn Hệ thống (AI) đúng dữ liệu; cập nhật mốc xem vụ của chính Mai đang giữ. | K81 Mở, holder Mai; Lan 6/10=0.6, mẫu số dương; Bình USER LIGHT; dữ liệu tố cáo không đưa cho Bình | E14.5 | FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| E14.5 | ACT-008 | Mai kết luận C81 vi phạm và chọn có cảnh cáo tác giả. | C81 Bị ẩn do AI 0.7, đang chờ; Bình USER 2/LIGHT; K81 Mai giữ | E14.6 | FR-M08-07.04, FR-M08-07.05, BR-M08-23 |
| E14.6 | SYSTEM | Hệ thống kiểm lại quyền/trạng thái chờ, giữ C81 Bị ẩn, áp trừ điểm upvote hiệu lực tại lúc xác định vi phạm và trả quyết định nội dung; cung cấp lựa chọn cảnh cáo tách riêng, không tự tăng số lần. | C81 Bị ẩn; 3 điểm upvote hiệu lực→trừ 3; Bình vẫn 2/LIGHT trước chọn cảnh cáo | E14.7 | FR-M08-07.04, FR-M08-07.05, FR-M12-02.21 |
| E14.7 | ACT-008 | Mai chọn Cảnh cáo Bình, nhập lý do vi phạm của C81. | K81 vẫn do Mai giữ; lý do Quấy rối; Bình chưa HEAVY | E14.8 | FR-M08-10.01 |
| E14.8 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Mod/Admin đối với Mod và chưa HEAVY; ghi cảnh cáo do Mai ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Bình: số lần 2→3, mức mới MEDIUM, hạn=T+10×24h; record issuer=Mai; K81 Mở; cảnh cáo chỉ app, không email | E14.9 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |
| E14.9 | ACT-008 | Mai chọn Có xử lý, nhập lý do Vi phạm đã xác định và kết luận K81. | Target vẫn C81; biện pháp vừa áp trong K81; Mai vẫn giữ | E14.10 | FR-M08-05.01, FR-M08-05.03 |
| E14.10 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Có xử lý cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “đã có biện pháp xử lý”; người bị báo cáo (Owner nếu nhóm) nhận lý do/mức xử lý, không nhận danh tính/lý do/mô tả/ảnh tố cáo. Chỉ cảnh cáo, ban, bài ẩn có đường khiếu nại; comment/nhóm ẩn-khóa không có. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Có xử lý; lý do=Vi phạm đã xác định; biện pháp=biện pháp vừa áp trên C81; actor Mai; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


<!-- sc:branch SC-M08-004 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | ACT-008 | Mai chọn Có xử lý, ghi lý do kết luận và gửi đóng K81. | Biện pháp đã có và đúng target: ẩn bài/comment, cảnh cáo, ban hoặc ẩn/khóa nhóm; lý do=Vi phạm đã xác định | E15.2 | FR-M08-05.01, FR-M08-05.03, BR-M08-10 |
| E15.2 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Có xử lý cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “đã có biện pháp xử lý”; người bị báo cáo (Owner nếu nhóm) nhận lý do/mức xử lý, không nhận danh tính/lý do/mô tả/ảnh tố cáo. Chỉ cảnh cáo, ban, bài ẩn có đường khiếu nại; comment/nhóm ẩn-khóa không có. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Có xử lý; lý do=Vi phạm đã xác định; biện pháp=các biện pháp đã có, đúng target; actor Mai; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


<!-- sc:branch SC-M08-004 E16 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E16.1 | ACT-008 | Mai chọn giải quyết K81 về C81 từ hàng chờ. | Ngay từ đầu K81 là vụ Mở về C81 của Bình USER, không phải vụ của P81; 3 báo cáo, ưu tiên 16; chưa ai giữ | E16.2 | FR-M08-02.01, FR-M08-03.01 |
| E16.2 | SYSTEM | Hệ thống kiểm staff/phạm vi, thứ tự ưu tiên và vụ Mở/chưa giữ; trả đúng vụ của C81 để nhận, không chuyển sang target khác. | Mai khác tác giả/Owner Bình; nếu nhóm thì Owner không là Admin | E16.3 | BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |
| E16.3 | ACT-008 | Mai chọn Nhận xử lý và mở chi tiết K81 về C81. | Đúng target của vụ vừa chọn, chưa ai giữ | E16.4 | FR-M08-03.01, FR-M08-04.01 |
| E16.4 | SYSTEM | Hệ thống kiểm lại quyền/phạm vi và gắn Mai là người giữ duy nhất nếu vừa nhận; mở hồ sơ điều tra: từng báo cáo/người gửi/lý do/mô tả/ảnh, nội dung và bản lưu đúng vụ, lịch sử đã kết luận, mức cảnh cáo, chỉ số tập trung theo 90×24h. Hiện danh tính thật cho staff và nhãn Hệ thống (AI) đúng dữ liệu; cập nhật mốc xem vụ của chính Mai đang giữ. | K81 Mở, holder Mai; Lan 6/10=0.6, mẫu số dương; Bình USER LIGHT; dữ liệu tố cáo không đưa cho Bình | E16.5 | FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| E16.5 | ACT-008 | Mai chọn xét C81 AI 0.7 và quyết định vi phạm, không cảnh cáo. | C81 Bị ẩn trung bình, chờ xét; K81 Mở do Mai giữ; Bình USER chưa HEAVY | E16.6 | FR-M08-07.04, FR-M08-07.05, BR-M08-23 |
| E16.6 | SYSTEM | Hệ thống kiểm lại quyền/trạng thái, giữ C81 Bị ẩn, áp điểm upvote hiệu lực theo M12 và trả đã xét; không tăng cảnh cáo, vẫn phải kết luận vụ. | C81 Bị ẩn, xác định vi phạm; K81 Mở; quay lại lựa chọn biện pháp/kết luận | E16.7 | FR-M08-07.04, FR-M08-07.05, FR-M12-02.21 |
| E16.7 | ACT-008 | Mai chọn Có xử lý, nhập lý do Vi phạm đã xác định và kết luận K81. | Target vẫn C81; biện pháp vừa áp trong K81; Mai vẫn giữ | E16.8 | FR-M08-05.01, FR-M08-05.03 |
| E16.8 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Có xử lý cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “đã có biện pháp xử lý”; người bị báo cáo (Owner nếu nhóm) nhận lý do/mức xử lý, không nhận danh tính/lý do/mô tả/ảnh tố cáo. Chỉ cảnh cáo, ban, bài ẩn có đường khiếu nại; comment/nhóm ẩn-khóa không có. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Có xử lý; lý do=Vi phạm đã xác định; biện pháp=biện pháp vừa áp trên C81; actor Mai; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


<!-- sc:branch SC-M08-004 E17 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E17.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-MAI | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |


<!-- sc:branch SC-M08-004 E18 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E18.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-HOA | END:REJECTED | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |


<!-- sc:branch SC-M08-004 E19 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E19.1 | SYSTEM | Hệ thống kiểm hiện tại và từ chối tác động ngoài vụ đang giữ; không áp biện pháp/kết luận thành công. | K81 holder Hoa hoặc target không thuộc vụ Mai giữ; dữ liệu đã áp trước đó giữ nguyên | END:REJECTED | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |


<!-- sc:branch SC-M08-004 E20 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E20.1 | SYSTEM | Hệ thống từ chối quyền cũ, giữ biện pháp đã có, cho biết vụ Mở chưa ai giữ; không tự đóng vụ. | holder=trống sau 30 phút không hoạt động hợp lệ | E20.2 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |
| E20.2 | ACT-008 | Mai chọn Nhận xử lý lại K81. | Mai vẫn đủ quyền/phạm vi, vụ chưa bị người khác nhận | E20.3 | FR-M08-03.01 |
| E20.3 | SYSTEM | Hệ thống kiểm lại điều kiện nhận và gắn duy nhất Mai làm người giữ, trả quyền hiện tại; không log nhận. | holder Mai; activity=T; biện pháp đã có không bị rollback | M5 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-16.07, BR-M08-08 |


<!-- sc:branch SC-M08-004 E21 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E21.1 | ACT-008 | Mai yêu cầu Ẩn P81 trong vụ đang xử lý. | P81 Bị ẩn | E21.2 | FR-M08-06.05 |
| E21.2 | SYSTEM | Hệ thống kiểm điều kiện và từ chối biện pháp bị cấm, giữ biện pháp cũ/vụ Mở; trả quyền lựa chọn hợp lệ tiếp theo. Không áp biện pháp thành công giả. | P81 Bị ẩn | M5 | FR-M08-06.05 |


<!-- sc:branch SC-M08-004 E22 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E22.1 | ACT-008 | Mai yêu cầu Xét P81 trong vụ đang xử lý. | P81 không còn Bị gắn cờ | E22.2 | FR-M08-07.07 |
| E22.2 | SYSTEM | Hệ thống kiểm điều kiện và từ chối biện pháp bị cấm, giữ biện pháp cũ/vụ Mở; trả quyền lựa chọn hợp lệ tiếp theo. Không áp biện pháp thành công giả. | P81 không còn Bị gắn cờ | M5 | FR-M08-07.07 |


<!-- sc:branch SC-M08-004 E23 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E23.1 | ACT-008 | Mai yêu cầu Cảnh cáo Bình trong vụ đang xử lý. | Bình 5/HEAVY; không tăng số lần, đánh dấu yêu cầu ban | E23.2 | FR-M08-10.10, FR-M08-14.11, BR-M08-36 |
| E23.2 | SYSTEM | Hệ thống kiểm điều kiện và từ chối biện pháp bị cấm, giữ biện pháp cũ/vụ Mở; trả quyền lựa chọn hợp lệ tiếp theo. Đánh dấu yêu cầu ban để con người quyết, không tự ban. | Bình 5/HEAVY; không tăng số lần, đánh dấu yêu cầu ban | M5 | FR-M08-10.10, FR-M08-14.11, BR-M08-36 |


<!-- sc:branch SC-M08-004 E24 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E24.1 | ACT-008 | Mai yêu cầu Cảnh cáo hoặc Ban reporter Hoa Mod trong vụ về Bình USER trong vụ đang xử lý. | Mai là Mod, reporter Hoa Mod; không suy rằng được chế tài vì target chính là User | E24.2 | FR-M08-10.08, FR-M08-14.09, BR-M08-46 |
| E24.2 | SYSTEM | Hệ thống kiểm điều kiện và từ chối biện pháp bị cấm, giữ biện pháp cũ/vụ Mở; trả quyền lựa chọn hợp lệ tiếp theo. Không áp biện pháp thành công giả. | Mai là Mod, reporter Hoa Mod; không suy rằng được chế tài vì target chính là User | M5 | FR-M08-10.08, FR-M08-14.09, BR-M08-46 |


<!-- sc:branch SC-M08-004 E25 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E25.1 | ACT-008 | Mai yêu cầu Ban Bình trong vụ đang xử lý. | B80 Đang hiệu lực; không có quyết định gỡ | E25.2 | FR-M08-14.13, BR-M08-52 |
| E25.2 | SYSTEM | Hệ thống kiểm điều kiện và từ chối biện pháp bị cấm, giữ biện pháp cũ/vụ Mở; trả quyền lựa chọn hợp lệ tiếp theo. Không áp biện pháp thành công giả. | B80 Đang hiệu lực; không có quyết định gỡ | M5 | FR-M08-14.13, BR-M08-52 |


<!-- sc:branch SC-M08-004 E26 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E26.1 | ACT-008 | Mai gửi kết luận Có xử lý thiếu lý do. | K81 Mai giữ; đã có biện pháp hợp lệ đối với target; reason=trống | E26.2 | FR-M08-05.01, FR-M08-05.09 |
| E26.2 | SYSTEM | Hệ thống từ chối kết luận thiếu lý do; giữ vụ Mở và biện pháp đã có. | Không rollback biện pháp | E26.3 | FR-M08-05.09 |
| E26.3 | ACT-008 | Mai bổ sung lý do Vi phạm đã xác định và gửi lại Có xử lý. | K81 vẫn Mở và Mai còn giữ | E26.4 | FR-M08-05.01, FR-M08-05.09 |
| E26.4 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Có xử lý cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “đã có biện pháp xử lý”; người bị báo cáo (Owner nếu nhóm) nhận lý do/mức xử lý, không nhận danh tính/lý do/mô tả/ảnh tố cáo. Chỉ cảnh cáo, ban, bài ẩn có đường khiếu nại; comment/nhóm ẩn-khóa không có. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Có xử lý; lý do=Vi phạm đã xác định; biện pháp=biện pháp hợp lệ đã có; actor Mai; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


<!-- sc:branch SC-M08-004 E27 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E27.1 | ACT-008 | Mai chọn giải quyết K81 về G81 từ hàng chờ. | Ngay từ đầu K81 là vụ Mở về G81 của Bình USER, không phải vụ của P81; 3 báo cáo, ưu tiên 16; chưa ai giữ | E27.2 | FR-M08-02.01, FR-M08-03.01 |
| E27.2 | SYSTEM | Hệ thống kiểm staff/phạm vi, thứ tự ưu tiên và vụ Mở/chưa giữ; trả đúng vụ của G81 để nhận, không chuyển sang target khác. | Mai khác tác giả/Owner Bình; nếu nhóm thì Owner không là Admin | E27.3 | BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |
| E27.3 | ACT-008 | Mai chọn Nhận xử lý và mở chi tiết K81 về G81. | Đúng target của vụ vừa chọn, chưa ai giữ | E27.4 | FR-M08-03.01, FR-M08-04.01 |
| E27.4 | SYSTEM | Hệ thống kiểm lại quyền/phạm vi và gắn Mai là người giữ duy nhất nếu vừa nhận; mở hồ sơ điều tra: từng báo cáo/người gửi/lý do/mô tả/ảnh, nội dung và bản lưu đúng vụ, lịch sử đã kết luận, mức cảnh cáo, chỉ số tập trung theo 90×24h. Hiện danh tính thật cho staff và nhãn Hệ thống (AI) đúng dữ liệu; cập nhật mốc xem vụ của chính Mai đang giữ. | K81 Mở, holder Mai; Lan 6/10=0.6, mẫu số dương; Bình USER LIGHT; dữ liệu tố cáo không đưa cho Bình | E27.5 | FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| E27.5 | ACT-008 | Mai chọn Khóa nhóm G81 trong K81. | G81 Bình thường; reason=Vi phạm đã xác định | E27.6 | FR-M08-18.04 |
| E27.6 | SYSTEM | Hệ thống kiểm staff/phạm vi/còn giữ vụ nhóm và trạng thái cho phép; chuyển nhóm Bị khóa; vẫn đọc theo Public/Private và giữ bookmark/báo cáo, chặn đầy đủ thao tác tại D-LOCK với mọi người kể cả Owner/Group Mod. Member/Group Mod vẫn tự rời, Owner không tự rời; hệ thống vẫn tự chuyển Owner khi mất quyền ngoài ý muốn. Ghi log và trả biện pháp đã áp; không tự cảnh cáo/ban Owner hoặc đóng vụ. | G81 Bình thường→Bị khóa; K81 Mở do Mai giữ; Owner Bình USER, Mai khác Owner | E27.7 | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |
| E27.7 | ACT-008 | Mai chọn cảnh cáo Owner Bình trong cùng vụ nhóm, nhập lý do đã đánh giá. | Bình USER 2/LIGHT; khác Mai, không Admin; K81 vẫn do Mai giữ; không tự suy cảnh cáo từ việc khóa nhóm | E27.8 | FR-M08-10.01, FR-M08-04.10, BR-M08-50 |
| E27.8 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Mod/Admin đối với Mod và chưa HEAVY; ghi cảnh cáo do Mai ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Bình (Owner): số lần 2→3, mức mới MEDIUM, hạn=T+10×24h; record issuer=Mai; K81 Mở; cảnh cáo chỉ app, không email | E27.9 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |
| E27.9 | ACT-008 | Mai chọn Có xử lý, ghi lý do và kết luận vụ nhóm. | K81 vẫn Mở do Mai giữ; nhóm đã khóa, Owner đã cảnh cáo; lý do=Vi phạm đã xác định | E27.10 | FR-M08-05.01, FR-M08-05.03 |
| E27.10 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Có xử lý cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “đã có biện pháp xử lý”; người bị báo cáo (Owner nếu nhóm) nhận lý do/mức xử lý, không nhận danh tính/lý do/mô tả/ảnh tố cáo. Chỉ cảnh cáo, ban, bài ẩn có đường khiếu nại; comment/nhóm ẩn-khóa không có. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Có xử lý; lý do=Vi phạm đã xác định; biện pháp=G81 Bị khóa; Owner có cảnh cáo riêng; actor Mai; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


<!-- sc:branch SC-M08-004 E28 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E28.1 | ACT-008 | Mai xác định P81 điểm 0.7 vi phạm, chọn Ẩn bài và có cảnh cáo tác giả. | P81 Bị gắn cờ, đúng K81 do Mai giữ; Bình USER 2/LIGHT, chưa HEAVY | E28.2 | FR-M08-07.02, FR-M08-07.05, BR-M08-23 |
| E28.2 | SYSTEM | Hệ thống kiểm lại quyền giữ/phạm vi/trạng thái chờ, chuyển P81 Bị ẩn, ghi log ẩn và trừ ngay 10 điểm từ 5 Post Star × 2 điểm/Star, ghi số điểm đã trừ; trả quyết định nội dung và lựa chọn cảnh cáo riêng. Chưa tự tăng cảnh cáo. | P81 Bị gắn cờ→Bị ẩn; điểm Bình 100→90, khoản trừ P81=10 điểm (5 Post Star × 2); số lần vẫn 2/LIGHT trước chọn cảnh cáo | E28.3 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, FR-M12-02.10, FR-M12-02.11, FR-M12-02.01, BR-M12-05 |
| E28.3 | ACT-008 | Mai chọn Cảnh cáo Bình và ghi lý do vi phạm đã xác định. | K81 vẫn Mở do Mai giữ; Bình USER, chưa HEAVY; lý do=Quấy rối | E28.4 | FR-M08-10.01 |
| E28.4 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Mod/Admin đối với Mod và chưa HEAVY; ghi cảnh cáo do Mai ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Bình: số lần 2→3, mức mới MEDIUM, hạn=T+10×24h; record issuer=Mai; K81 Mở; cảnh cáo chỉ app, không email | M5 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |


**E29 — thay toàn bộ M1 đến kết thúc:** An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-004 E29 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E29.1 | ACT-007 | An chọn K81 từ hàng chờ để giải quyết. | K81: vụ Mở về P81 của Bình/U-BINH (USER, khác người xử lý), 3 báo cáo Mở của Lan, Chi và Hệ thống (AI); ưu tiên 10+2×3=16; không có người giữ. An/ADM-AN là Mod hệ thống. P81 còn thấy hoặc có bản lưu đúng ngữ cảnh vụ; không phải Nháp/Bị từ chối. | E29.2 | FR-M08-02.01, FR-M08-03.01 |
| E29.2 | SYSTEM | Hệ thống kiểm vai trò/phạm vi đọc và khả năng nhận; dùng hàng chờ ưu tiên giảm dần (max trọng số + 2×số báo cáo), hòa theo vụ mở trước, trả K81 Mở, chưa có người giữ và cho An chọn nhận. Vụ tự nhắm mình/Mod theo quyền bị loại trước khi xem/nhận. | K81 ưu tiên 16 về Bình USER; An khác Bình; chưa giữ | E29.3 | BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |
| E29.3 | ACT-007 | An chọn Nhận xử lý và mở K81 để điều tra. | Yêu cầu nắm quyền K81 hiện Mở/chưa giữ | E29.4 | FR-M08-03.01, FR-M08-04.01 |
| E29.4 | SYSTEM | Hệ thống kiểm lại quyền/phạm vi và gắn An là người giữ duy nhất nếu vừa nhận; mở hồ sơ điều tra: từng báo cáo/người gửi/lý do/mô tả/ảnh, nội dung và bản lưu đúng vụ, lịch sử đã kết luận, mức cảnh cáo, chỉ số tập trung theo 90×24h. Hiện danh tính thật cho staff và nhãn Hệ thống (AI) đúng dữ liệu; cập nhật mốc xem vụ của chính An đang giữ. | K81 Mở, holder An; Lan 6/10=0.6, mẫu số dương; Bình USER LIGHT; dữ liệu tố cáo không đưa cho Bình | E29.5 | FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| E29.5 | ACT-007 | An đánh giá không đủ căn cứ, chọn Bác bỏ và nhập lý do để kết luận vụ. | K81 chưa áp biện pháp; lý do=Không đủ căn cứ vi phạm | E29.6 | FR-M08-05.01, FR-M08-05.03, BR-M08-10 |
| E29.6 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Bác bỏ cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “không phát hiện vi phạm”; không gửi kết quả cho Bình hoặc mục AI. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Bác bỏ; lý do=Không đủ căn cứ vi phạm; biện pháp=không có biện pháp; actor An; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


**E30 — thay toàn bộ M1 đến kết thúc:** User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-004 E30 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E30.1 | ACT-002 | Người yêu cầu chọn giải quyết hoàn chỉnh một vụ báo cáo. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E30.2 | FR-M08-02.01, FR-M08-03.01 |
| E30.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |


**E31 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-004 E31 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E31.1 | ACT-001 | Người yêu cầu chọn giải quyết hoàn chỉnh một vụ báo cáo. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E31.2 | FR-M08-02.01, FR-M08-03.01 |
| E31.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |


**E32 — thay toàn bộ M1 đến kết thúc:** An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-004 E32 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E32.1 | ACT-007 | An chọn K81 từ hàng chờ để giải quyết. | K81: vụ Mở về P81 của Hoa/MOD-HOA (MODERATOR, khác người xử lý), 3 báo cáo Mở của Lan, Chi và Hệ thống (AI); ưu tiên 10+2×3=16; không có người giữ. An/ADM-AN là Mod hệ thống. P81 còn thấy hoặc có bản lưu đúng ngữ cảnh vụ; không phải Nháp/Bị từ chối. | E32.2 | FR-M08-02.01, FR-M08-03.01 |
| E32.2 | SYSTEM | Hệ thống kiểm vai trò/phạm vi đọc và khả năng nhận; dùng hàng chờ ưu tiên giảm dần (max trọng số + 2×số báo cáo), hòa theo vụ mở trước, trả K81 Mở, chưa có người giữ và cho An chọn nhận. Vụ tự nhắm mình/Mod theo quyền bị loại trước khi xem/nhận. | K81 ưu tiên 16 về Hoa MODERATOR; An khác Hoa; chưa giữ | E32.3 | BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |
| E32.3 | ACT-007 | An chọn Nhận xử lý và mở K81 để điều tra. | Yêu cầu nắm quyền K81 hiện Mở/chưa giữ | E32.4 | FR-M08-03.01, FR-M08-04.01 |
| E32.4 | SYSTEM | Hệ thống kiểm lại quyền/phạm vi và gắn An là người giữ duy nhất nếu vừa nhận; mở hồ sơ điều tra: từng báo cáo/người gửi/lý do/mô tả/ảnh, nội dung và bản lưu đúng vụ, lịch sử đã kết luận, mức cảnh cáo, chỉ số tập trung theo 90×24h. Hiện danh tính thật cho staff và nhãn Hệ thống (AI) đúng dữ liệu; cập nhật mốc xem vụ của chính An đang giữ. | K81 Mở, holder An; Lan 6/10=0.6, mẫu số dương; Hoa MODERATOR LIGHT; dữ liệu tố cáo không đưa cho Hoa | E32.5 | FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, BR-M08-46, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| E32.5 | ACT-007 | An đánh giá không đủ căn cứ, chọn Bác bỏ và nhập lý do để kết luận vụ. | K81 chưa áp biện pháp; lý do=Không đủ căn cứ vi phạm | E32.6 | FR-M08-05.01, FR-M08-05.03, BR-M08-10 |
| E32.6 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Bác bỏ cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “không phát hiện vi phạm”; không gửi kết quả cho Hoa hoặc mục AI. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Bác bỏ; lý do=Không đủ căn cứ vi phạm; biện pháp=không có biện pháp; actor An; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


**E33 — thay toàn bộ M1 đến kết thúc:** An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-004 E33 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E33.1 | ACT-007 | An yêu cầu giải quyết hoàn chỉnh một vụ báo cáo đối với vụ của chính mình. | target type=post/comment/account; owner=ADM-AN; không phải nhóm | E33.2 | FR-M08-02.01, FR-M08-03.01 |
| E33.2 | SYSTEM | Hệ thống loại vụ khỏi phạm vi nhìn thấy/nhận và từ chối truy cập/xử lý đối tượng của chính An theo nguồn, không cấp quyền nhờ role Admin. | Không trả dữ liệu tố cáo/không áp biện pháp | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |


<!-- sc:end SC-M08-004 -->

<a id="sc-m08-005"></a>

<!-- sc:scenario SC-M08-005 -->

### SC-M08-005

#### 1. Tên kịch bản chuẩn

Kết luận một vụ đang giữ — BF-M08-005; owner [UC-M08-005](../../us/US-M08.md#uc-m08-005).

#### 2. Actor thực hiện

ACT-008 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Có hồ sơ vụ và kết quả điều tra đã có; kiểm lại quyền giữ/trạng thái/lý do trong lượt xử lý. Chuẩn Mai đang giữ K81, chưa áp biện pháp, đủ căn cứ Bác bỏ; không dùng kết luận để tự suy rollback biện pháp đã có.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-005 -->

| result | condition |
|---|---|
| SUCCESS | Vụ và mọi báo cáo Mở đóng cùng kết luận; lý do/người làm/thời điểm và log được lưu; reporter người dùng chỉ nhận kết quả chung, target chỉ nhận chi tiết khi Có xử lý đúng loại/đường khiếu nại. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-005 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai chọn Bác bỏ, nhập lý do và gửi kết luận K81. | K81 Mở; holder Mai; Không đủ căn cứ vi phạm; chưa áp biện pháp | M2 | FR-M08-05.01, FR-M08-05.03 |
| M2 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Bác bỏ cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “không phát hiện vi phạm”; không gửi kết quả cho Bình hoặc mục AI. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Bác bỏ; lý do=Không đủ căn cứ vi phạm; biện pháp=không có biện pháp; actor Mai; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-005 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Thiếu lý do kết luận; quyền giữ/vụ vẫn hợp lệ | E1.1 | FR-M08-05.09, FR-M08-05.01 |
| E2 | system | M2 | Vụ đã được đóng trước xử lý kết luận | E2.1 | FR-M08-05.08 |
| E3 | user-choice | M1 | Mai kết luận Có xử lý sau biện pháp hợp lệ với bài viết | E3.1 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.11, FR-M08-18.11, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |
| E4 | user-choice | M1 | Mai kết luận Có xử lý sau biện pháp hợp lệ với bình luận | E4.1 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.11, FR-M08-18.11, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |
| E5 | user-choice | M1 | Mai kết luận Có xử lý sau biện pháp hợp lệ với nhóm | E5.1 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.11, FR-M08-18.11, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |
| E6 | user-choice | M1 | Mai kết luận Có xử lý sau biện pháp hợp lệ với tài khoản | E6.1 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.11, FR-M08-18.11, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |
| E7 | system | M2 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | E7.1 | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |
| E8 | system | M2 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | E8.1 | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |
| E9 | system | M2 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | E9.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |
| E10 | user-choice | M2 | Quyền giữ đã tự nhả sau đủ 30 phút không hoạt động; K81 vẫn Mở/chưa ai nhận, Mai còn đủ phạm vi và chọn nhận lại | E10.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-16.07, FR-M08-03.01, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-05.01, FR-M08-05.03 |
| E11 | system | M1 | ACT-007 — An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E11.1 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |
| E12 | system | M1 | ACT-002 — User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E12.1 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40, BR-M08-44 |
| E13 | system | M1 | ACT-001 — Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E13.1 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40, BR-M08-44 |
| E14 | system | M1 | ACT-007 — An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E14.1 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |
| E15 | system | M1 | ACT-007 — An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E15.1 | FR-M08-05.01, FR-M08-05.03, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |


<!-- sc:branch SC-M08-005 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối kết luận thiếu lý do; vụ và các báo cáo vẫn Mở, giữ hiệu ứng hợp lệ đã có. | reason=trống; holder Mai; K81 Mở | E1.2 | FR-M08-05.09 |
| E1.2 | ACT-008 | Mai nhập lý do và gửi lại cùng lựa chọn kết luận. | Bác bỏ, Không đủ căn cứ vi phạm; chưa có biện pháp | M2 | FR-M08-05.01, FR-M08-05.09 |


<!-- sc:branch SC-M08-005 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối kết luận lần hai; giữ kết quả đã lưu, không phát lại sự kiện thành công mới. | K81 Đã xử lý | END:REJECTED | FR-M08-05.08 |


<!-- sc:branch SC-M08-005 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-008 | Mai chọn Có xử lý, nhập lý do kết luận và gửi K81. | P81 đã Bị ẩn, đường khiếu nại cho bài; K81 Mở do Mai giữ; lý do=Vi phạm đã xác định, có thể khác lý do reporter | E3.2 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.11, FR-M08-18.11 |
| E3.2 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Có xử lý cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “đã có biện pháp xử lý”; người bị báo cáo (Owner nếu nhóm) nhận lý do/mức xử lý, không nhận danh tính/lý do/mô tả/ảnh tố cáo. Chỉ cảnh cáo, ban, bài ẩn có đường khiếu nại; comment/nhóm ẩn-khóa không có. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Có xử lý; lý do=Vi phạm đã xác định; biện pháp=P81 đã Bị ẩn, đường khiếu nại cho bài; actor Mai; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


<!-- sc:branch SC-M08-005 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-008 | Mai chọn Có xử lý, nhập lý do kết luận và gửi K81. | C81 đã Bị ẩn, không đường khiếu nại cho comment; K81 Mở do Mai giữ; lý do=Vi phạm đã xác định, có thể khác lý do reporter | E4.2 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.11, FR-M08-18.11 |
| E4.2 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Có xử lý cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “đã có biện pháp xử lý”; người bị báo cáo (Owner nếu nhóm) nhận lý do/mức xử lý, không nhận danh tính/lý do/mô tả/ảnh tố cáo. Chỉ cảnh cáo, ban, bài ẩn có đường khiếu nại; comment/nhóm ẩn-khóa không có. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Có xử lý; lý do=Vi phạm đã xác định; biện pháp=C81 đã Bị ẩn, không đường khiếu nại cho comment; actor Mai; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


<!-- sc:branch SC-M08-005 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-008 | Mai chọn Có xử lý, nhập lý do kết luận và gửi K81. | G81 đã Bị ẩn hoặc Bị khóa, Owner Bình nhận chi tiết, không đường khiếu nại cho nhóm; K81 Mở do Mai giữ; lý do=Vi phạm đã xác định, có thể khác lý do reporter | E5.2 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.11, FR-M08-18.11 |
| E5.2 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Có xử lý cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “đã có biện pháp xử lý”; người bị báo cáo (Owner nếu nhóm) nhận lý do/mức xử lý, không nhận danh tính/lý do/mô tả/ảnh tố cáo. Chỉ cảnh cáo, ban, bài ẩn có đường khiếu nại; comment/nhóm ẩn-khóa không có. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Có xử lý; lý do=Vi phạm đã xác định; biện pháp=G81 đã Bị ẩn hoặc Bị khóa, Owner Bình nhận chi tiết, không đường khiếu nại cho nhóm; actor Mai; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


<!-- sc:branch SC-M08-005 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-008 | Mai chọn Có xử lý, nhập lý do kết luận và gửi K81. | Bình đã cảnh cáo hoặc ban, có đường khiếu nại cho chế tài; K81 Mở do Mai giữ; lý do=Vi phạm đã xác định, có thể khác lý do reporter | E6.2 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.11, FR-M08-18.11 |
| E6.2 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Có xử lý cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “đã có biện pháp xử lý”; người bị báo cáo (Owner nếu nhóm) nhận lý do/mức xử lý, không nhận danh tính/lý do/mô tả/ảnh tố cáo. Chỉ cảnh cáo, ban, bài ẩn có đường khiếu nại; comment/nhóm ẩn-khóa không có. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Có xử lý; lý do=Vi phạm đã xác định; biện pháp=Bình đã cảnh cáo hoặc ban, có đường khiếu nại cho chế tài; actor Mai; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


<!-- sc:branch SC-M08-005 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-MAI | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |


<!-- sc:branch SC-M08-005 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-HOA | END:REJECTED | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |


<!-- sc:branch SC-M08-005 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống kiểm hiện tại và từ chối tác động ngoài vụ đang giữ; không áp biện pháp/kết luận thành công. | K81 holder Hoa hoặc target không thuộc vụ Mai giữ; dữ liệu đã áp trước đó giữ nguyên | END:REJECTED | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |


<!-- sc:branch SC-M08-005 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống từ chối yêu cầu theo quyền giữ cũ, cho biết K81 Mở chưa ai giữ; không tự gắn lại Mai hoặc ghi log tự nhả. | lastActivity=T−30 phút; người khác chỉ xem không làm mới mốc; holder=trống | E10.2 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-16.07 |
| E10.2 | ACT-008 | Mai chọn Nhận xử lý lại K81. | K81 còn Mở/chưa ai giữ; Mai đủ quyền | E10.3 | FR-M08-03.01 |
| E10.3 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/trạng thái/chưa giữ, gắn duy nhất Mai giữ K81, trả đã nhận; không log nhận. | holder=Mai; activity=T | E10.4 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-16.07, BR-M08-08 |
| E10.4 | ACT-008 | Mai chọn Bác bỏ, nhập lý do và gửi kết luận K81. | K81 Mở; holder Mai; Không đủ căn cứ vi phạm; chưa áp biện pháp; quyền vừa nhận lại còn hợp lệ | M2 | FR-M08-05.01, FR-M08-05.03 |


**E11 — thay toàn bộ M1 đến kết thúc:** An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-005 E11 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E11.1 | ACT-007 | An chọn Bác bỏ, nhập lý do và gửi kết luận K81. | K81 Mở; holder An; Không đủ căn cứ vi phạm; chưa áp biện pháp | E11.2 | FR-M08-05.01, FR-M08-05.03 |
| E11.2 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Bác bỏ cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “không phát hiện vi phạm”; không gửi kết quả cho Bình hoặc mục AI. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Bác bỏ; lý do=Không đủ căn cứ vi phạm; biện pháp=không có biện pháp; actor An; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


**E12 — thay toàn bộ M1 đến kết thúc:** User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-005 E12 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E12.1 | ACT-002 | Người yêu cầu chọn kết luận một vụ đang giữ. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E12.2 | FR-M08-05.01, FR-M08-05.03 |
| E12.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40, BR-M08-44 |


**E13 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-005 E13 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E13.1 | ACT-001 | Người yêu cầu chọn kết luận một vụ đang giữ. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E13.2 | FR-M08-05.01, FR-M08-05.03 |
| E13.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40, BR-M08-44 |


**E14 — thay toàn bộ M1 đến kết thúc:** An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-005 E14 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E14.1 | ACT-007 | An chọn Bác bỏ, nhập lý do và gửi kết luận K81. | K81 Mở; holder An; Không đủ căn cứ vi phạm; chưa áp biện pháp | E14.2 | FR-M08-05.01, FR-M08-05.03 |
| E14.2 | SYSTEM | Hệ thống kiểm lại vai trò/phạm vi, vụ Mở, quyền giữ và lý do; lưu kết luận Bác bỏ cùng lý do/người làm/thời điểm, đóng vụ và toàn bộ báo cáo Mở cùng kết quả, ghi nhật ký bất biến. Mọi reporter người dùng chỉ nhận kết quả chung “không phát hiện vi phạm”; không gửi kết quả cho Hoa hoặc mục AI. Trả vụ đã giải quyết; câu chữ thông báo cuối theo thiết kế M07. | K81 và mọi báo cáo Mở→Đã xử lý; kết quả=Bác bỏ; lý do=Không đủ căn cứ vi phạm; biện pháp=không có biện pháp; actor An; thời điểm T | END:SUCCESS | FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |


**E15 — thay toàn bộ M1 đến kết thúc:** An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-005 E15 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E15.1 | ACT-007 | An yêu cầu kết luận một vụ đang giữ đối với vụ của chính mình. | target type=post/comment/account; owner=ADM-AN; không phải nhóm | E15.2 | FR-M08-05.01, FR-M08-05.03 |
| E15.2 | SYSTEM | Hệ thống loại vụ khỏi phạm vi nhìn thấy/nhận và từ chối truy cập/xử lý đối tượng của chính An theo nguồn, không cấp quyền nhờ role Admin. | Không trả dữ liệu tố cáo/không áp biện pháp | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |


<!-- sc:end SC-M08-005 -->

<a id="sc-m08-006"></a>

<!-- sc:scenario SC-M08-006 -->

### SC-M08-006

#### 1. Tên kịch bản chuẩn

Xét và quyết định nội dung đang chờ sau AI — BF-M08-006; owner [UC-M08-007](../../us/US-M08.md#uc-m08-007).

#### 2. Actor thực hiện

ACT-008 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Nội dung/vụ được nhận diện, không mặc định mọi nội dung Bị ẩn đều được hiện lại. Chuẩn P81 Bị gắn cờ sau quét lại M03, thuộc K81 Mở do Mai giữ; tác giả Bình USER chưa HEAVY; lựa chọn không vi phạm.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-006 -->

| result | condition |
|---|---|
| SUCCESS | Quyết định xét hợp lệ đã áp vào nội dung; cảnh cáo chỉ tăng nếu actor chọn và đủ điều kiện. Vụ vẫn cần kết luận riêng; đây là mục tiêu xét nội dung, không phải BF giải quyết toàn vụ. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-006 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai mở nội dung đang chờ xét của K81. | P81 Bị gắn cờ; holder Mai | M2 | FR-M08-07.06 |
| M2 | SYSTEM | Hệ thống kiểm staff/phạm vi/quyền giữ, vụ và nội dung còn chờ xét; trả nội dung, loại/điểm AI và các quyết định tương ứng, không tự tăng cảnh cáo. | P81 Bị gắn cờ; nhóm Quấy rối, điểm minh họa 0.7 | M3 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| M3 | ACT-008 | Mai quyết định giữ bài vì không vi phạm. | P81; giữ bài, không cảnh cáo | M4 | FR-M08-07.01 |
| M4 | SYSTEM | Hệ thống kiểm lại guard, chuyển P81 về Bình thường và trả kết quả đã xét. Không tự kết luận vụ hoặc đồng nhất quyết định nội dung với chế tài tác giả. | P81 Bị gắn cờ→Bình thường; K81 vẫn Mở, holder Mai; số cảnh cáo không tăng | END:SUCCESS | FR-M08-07.01, FR-M08-07.05, FR-M08-07.07, BR-M08-23, BR-M08-48 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-006 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M3 | Chọn Ẩn bài đối với P81 | E1.1 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, FR-M12-02.10, FR-M12-02.11 |
| E2 | user-choice | M1 | Ngay từ đầu chọn xét C81 AI trung bình trong vụ C81, không phải P81; Chọn Không vi phạm đối với C81 | E2.1 | FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| E3 | user-choice | M1 | Ngay từ đầu chọn xét C81 AI trung bình trong vụ C81, không phải P81; Chọn Vi phạm, không cảnh cáo đối với C81 | E3.1 | FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| E4 | user-choice | M1 | Ngay từ đầu chọn xét C81 AI trung bình trong vụ C81, không phải P81; Comment điểm trung bình được xác định vi phạm và Mai chọn cảnh cáo tác giả | E4.1 | FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-43, BR-M08-53 |
| E5 | system | M1 | Ngay từ đầu chọn xét C81 AI trung bình trong vụ C81, không phải P81; Target đã HEAVY và staff xác định vi phạm nội dung trung bình | E5.1 | FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-09.11, FR-M08-14.11 |
| E6 | system | M4 | Nội dung không còn chờ xét hoặc không thuộc loại được xét lại | E6.1 | FR-M08-07.07, BR-M08-22, BR-M08-54 |
| E7 | system | M2 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | E7.1 | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |
| E8 | system | M2 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | E8.1 | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |
| E9 | system | M4 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | E9.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |
| E10 | user-choice | M4 | Vụ tự nhả 30 phút, còn Mở/chưa ai giữ và Mai chọn nhận lại trước tiếp tục | E10.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-03.01, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-16.07 |
| E11 | user-choice | M3 | P81 đang gắn cờ, điểm trung bình, Mai chọn Ẩn bài rồi cảnh cáo tác giả đủ điều kiện | E11.1 | FR-M08-07.02, FR-M08-07.05, BR-M08-23, FR-M08-07.01, FR-M08-07.03, FR-M08-07.04, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, FR-M12-02.10, FR-M12-02.11, FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-43, BR-M08-53 |
| E12 | system | M1 | ACT-007 — An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E12.1 | FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| E13 | system | M1 | ACT-002 — User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E13.1 | FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| E14 | system | M1 | ACT-001 — Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E14.1 | FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| E15 | system | M1 | ACT-007 — An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E15.1 | FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| E16 | system | M1 | ACT-007 — An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E16.1 | FR-M08-07.06, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |


<!-- sc:branch SC-M08-006 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-008 | Mai chọn Ẩn bài cho nội dung đang xét. | P81: Bị gắn cờ; K81 Mở do Mai giữ; Bình USER chưa HEAVY | E1.2 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21 |
| E1.2 | SYSTEM | Hệ thống kiểm lại quyền giữ/phạm vi và nội dung còn chờ xét, áp quyết định Ẩn bài và trả kết quả. Ẩn bài, ghi log và trừ ngay phần điểm upvote hiệu lực theo M12, ghi số điểm đã trừ. Không tăng cảnh cáo từ lựa chọn không cảnh cáo. K81 vẫn Mở chờ kết luận vụ. | P81→Bị ẩn; không tự Ban/cảnh cáo; trạng thái vụ không đổi; điểm Bình 100→90, ghi khoản đã trừ 10 điểm (5 Post Star × 2) cho P81 | END:SUCCESS | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, FR-M12-02.10, FR-M12-02.11, FR-M12-02.01, BR-M12-05 |


<!-- sc:branch SC-M08-006 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-008 | Mai mở C81 đang chờ xét trong vụ của chính C81. | C81 Bị ẩn do AI 0.7, chưa có quyết định staff; K81 Mở do Mai giữ | E2.2 | FR-M08-07.06 |
| E2.2 | SYSTEM | Hệ thống kiểm staff/phạm vi/quyền giữ và nội dung còn chờ; trả C81 Bị ẩn do AI trung bình cùng điểm/nhóm và lựa chọn Không vi phạm/Vi phạm, cảnh cáo tách riêng. | C81 đúng vụ K81; tác giả Bình USER; nếu guard HEAVY thì Bình 5/HEAVY, còn lại chưa HEAVY | E2.3 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| E2.3 | ACT-008 | Mai chọn Không vi phạm cho nội dung đang xét. | C81: Bị ẩn do AI, 0.7, đang chờ xét; K81 Mở do Mai giữ; Bình USER chưa HEAVY | E2.4 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21 |
| E2.4 | SYSTEM | Hệ thống kiểm lại quyền giữ/phạm vi và nội dung còn chờ xét, áp quyết định Không vi phạm và trả kết quả. Không trừ điểm khi comment được xác định không vi phạm. Không tăng cảnh cáo từ lựa chọn không cảnh cáo. K81 vẫn Mở chờ kết luận vụ. | C81→Bình thường; không tự Ban/cảnh cáo; trạng thái vụ không đổi | END:SUCCESS | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21 |


<!-- sc:branch SC-M08-006 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-008 | Mai mở C81 đang chờ xét trong vụ của chính C81. | C81 Bị ẩn do AI 0.7, chưa có quyết định staff; K81 Mở do Mai giữ | E3.2 | FR-M08-07.06 |
| E3.2 | SYSTEM | Hệ thống kiểm staff/phạm vi/quyền giữ và nội dung còn chờ; trả C81 Bị ẩn do AI trung bình cùng điểm/nhóm và lựa chọn Không vi phạm/Vi phạm, cảnh cáo tách riêng. | C81 đúng vụ K81; tác giả Bình USER; nếu guard HEAVY thì Bình 5/HEAVY, còn lại chưa HEAVY | E3.3 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| E3.3 | ACT-008 | Mai chọn Vi phạm, không cảnh cáo cho nội dung đang xét. | C81: Bị ẩn do AI, 0.7, đang chờ xét; K81 Mở do Mai giữ; Bình USER chưa HEAVY | E3.4 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21 |
| E3.4 | SYSTEM | Hệ thống kiểm lại quyền giữ/phạm vi và nội dung còn chờ xét, áp quyết định Vi phạm, không cảnh cáo và trả kết quả. Trừ phần điểm upvote hiệu lực tại lúc xác định vi phạm theo M12; giữ comment ẩn không phải ẩn lặp. Không tăng cảnh cáo từ lựa chọn không cảnh cáo. K81 vẫn Mở chờ kết luận vụ. | C81→Bị ẩn; không tự Ban/cảnh cáo; trạng thái vụ không đổi | END:SUCCESS | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21 |


<!-- sc:branch SC-M08-006 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-008 | Mai mở C81 đang chờ xét trong vụ của chính C81. | C81 Bị ẩn do AI 0.7, chưa có quyết định staff; K81 Mở do Mai giữ | E4.2 | FR-M08-07.06 |
| E4.2 | SYSTEM | Hệ thống kiểm staff/phạm vi/quyền giữ và nội dung còn chờ; trả C81 Bị ẩn do AI trung bình cùng điểm/nhóm và lựa chọn Không vi phạm/Vi phạm, cảnh cáo tách riêng. | C81 đúng vụ K81; tác giả Bình USER; nếu guard HEAVY thì Bình 5/HEAVY, còn lại chưa HEAVY | E4.3 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| E4.3 | ACT-008 | Mai kết luận C81 vi phạm và chọn có cảnh cáo tác giả. | C81 Bị ẩn do AI 0.7, đang chờ; Bình USER 2/LIGHT; K81 Mai giữ | E4.4 | FR-M08-07.04, FR-M08-07.05, BR-M08-23 |
| E4.4 | SYSTEM | Hệ thống kiểm lại quyền/trạng thái chờ, giữ C81 Bị ẩn, áp trừ điểm upvote hiệu lực tại lúc xác định vi phạm và trả quyết định nội dung; cung cấp lựa chọn cảnh cáo tách riêng, không tự tăng số lần. | C81 Bị ẩn; 3 điểm upvote hiệu lực→trừ 3; Bình vẫn 2/LIGHT trước chọn cảnh cáo | E4.5 | FR-M08-07.04, FR-M08-07.05, FR-M12-02.21 |
| E4.5 | ACT-008 | Mai chọn Cảnh cáo Bình, nhập lý do vi phạm của C81. | K81 vẫn do Mai giữ; lý do Quấy rối; Bình chưa HEAVY | E4.6 | FR-M08-10.01 |
| E4.6 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Mod/Admin đối với Mod và chưa HEAVY; ghi cảnh cáo do Mai ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Bình: số lần 2→3, mức mới MEDIUM, hạn=T+10×24h; record issuer=Mai; K81 Mở; cảnh cáo chỉ app, không email | END:SUCCESS | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |


<!-- sc:branch SC-M08-006 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-008 | Mai mở C81 đang chờ xét trong vụ của chính C81. | C81 Bị ẩn do AI 0.7, chưa có quyết định staff; K81 Mở do Mai giữ | E5.2 | FR-M08-07.06 |
| E5.2 | SYSTEM | Hệ thống kiểm staff/phạm vi/quyền giữ và nội dung còn chờ; trả C81 Bị ẩn do AI trung bình cùng điểm/nhóm và lựa chọn Không vi phạm/Vi phạm, cảnh cáo tách riêng. | C81 đúng vụ K81; tác giả Bình USER; nếu guard HEAVY thì Bình 5/HEAVY, còn lại chưa HEAVY | E5.3 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| E5.3 | ACT-008 | Mai xác định C81 điểm trung bình vi phạm, tác giả đã HEAVY. | C81 AI 0.7 đang chờ xét; Bình 5/HEAVY; K81 Mai giữ | E5.4 | FR-M08-07.04, BR-M08-36 |
| E5.4 | SYSTEM | Hệ thống kiểm quyền giữ/phạm vi và nội dung đang chờ, giữ C81 Bị ẩn vì vi phạm, áp điểm theo M12; không tăng cảnh cáo. Đánh dấu yêu cầu ban trên vụ hiện có, trả quyết định xét cho Mai để con người cân nhắc Ban riêng. Không tự ban, tạo mục AI mới từ quyết định thủ công hoặc tự đóng vụ. | Snapshot: C81 trung bình 0.7, Bình 5/HEAVY; Mai đã chọn Vi phạm thay giữ bài; K81 Mở có dấu yêu cầu ban; Bình vẫn 5 | END:SUCCESS | FR-M08-07.04, FR-M08-07.05, FR-M08-09.11, FR-M08-14.11, BR-M08-36, BR-M08-49, FR-M12-02.21 |


<!-- sc:branch SC-M08-006 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối quyết định xét không còn hợp lệ; không phục hồi comment ẩn điểm cao hoặc staff ẩn chỉ vì bỏ/lật chế tài. | P81 đã Bình thường; hoặc C81 bị AI ẩn ≥0.9/staff ẩn, không phải mục trung bình chờ xét | END:REJECTED | FR-M08-07.07, BR-M08-22, BR-M08-54 |


<!-- sc:branch SC-M08-006 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-MAI | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |


<!-- sc:branch SC-M08-006 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-HOA | END:REJECTED | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |


<!-- sc:branch SC-M08-006 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống kiểm hiện tại và từ chối tác động ngoài vụ đang giữ; không áp biện pháp/kết luận thành công. | K81 holder Hoa hoặc target không thuộc vụ Mai giữ; dữ liệu đã áp trước đó giữ nguyên | END:REJECTED | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |


<!-- sc:branch SC-M08-006 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống từ chối quyền cũ, giữ biện pháp đã có, cho biết vụ Mở chưa ai giữ; không tự đóng vụ. | holder=trống sau 30 phút không hoạt động hợp lệ | E10.2 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |
| E10.2 | ACT-008 | Mai chọn Nhận xử lý lại K81. | Mai vẫn đủ quyền/phạm vi, vụ chưa bị người khác nhận | E10.3 | FR-M08-03.01 |
| E10.3 | SYSTEM | Hệ thống kiểm lại điều kiện nhận và gắn duy nhất Mai làm người giữ, trả quyền hiện tại; không log nhận. | holder Mai; activity=T; biện pháp đã có không bị rollback | M3 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-16.07, BR-M08-08 |


<!-- sc:branch SC-M08-006 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-008 | Mai xác định P81 điểm 0.7 vi phạm, chọn Ẩn bài và có cảnh cáo tác giả. | P81 Bị gắn cờ, đúng K81 do Mai giữ; Bình USER 2/LIGHT, chưa HEAVY | E11.2 | FR-M08-07.02, FR-M08-07.05, BR-M08-23 |
| E11.2 | SYSTEM | Hệ thống kiểm lại quyền giữ/phạm vi/trạng thái chờ, chuyển P81 Bị ẩn, ghi log ẩn và trừ ngay 10 điểm từ 5 Post Star × 2 điểm/Star, ghi số điểm đã trừ; trả quyết định nội dung và lựa chọn cảnh cáo riêng. Chưa tự tăng cảnh cáo. | P81 Bị gắn cờ→Bị ẩn; điểm Bình 100→90, khoản trừ P81=10 điểm (5 Post Star × 2); số lần vẫn 2/LIGHT trước chọn cảnh cáo | E11.3 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, FR-M12-02.10, FR-M12-02.11, FR-M12-02.01, BR-M12-05 |
| E11.3 | ACT-008 | Mai chọn Cảnh cáo Bình và ghi lý do vi phạm đã xác định. | K81 vẫn Mở do Mai giữ; Bình USER, chưa HEAVY; lý do=Quấy rối | E11.4 | FR-M08-10.01 |
| E11.4 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Mod/Admin đối với Mod và chưa HEAVY; ghi cảnh cáo do Mai ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Bình: số lần 2→3, mức mới MEDIUM, hạn=T+10×24h; record issuer=Mai; K81 Mở; cảnh cáo chỉ app, không email | END:SUCCESS | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |


**E12 — thay toàn bộ M1 đến kết thúc:** An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-006 E12 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E12.1 | ACT-007 | An mở nội dung đang chờ xét của K81. | P81 Bị gắn cờ; holder An | E12.2 | FR-M08-07.06 |
| E12.2 | SYSTEM | Hệ thống kiểm staff/phạm vi/quyền giữ, vụ và nội dung còn chờ xét; trả nội dung, loại/điểm AI và các quyết định tương ứng, không tự tăng cảnh cáo. | P81 Bị gắn cờ; nhóm Quấy rối, điểm minh họa 0.7 | E12.3 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| E12.3 | ACT-007 | An quyết định giữ bài vì không vi phạm. | P81; giữ bài, không cảnh cáo | E12.4 | FR-M08-07.01 |
| E12.4 | SYSTEM | Hệ thống kiểm lại guard, chuyển P81 về Bình thường và trả kết quả đã xét. Không tự kết luận vụ hoặc đồng nhất quyết định nội dung với chế tài tác giả. | P81 Bị gắn cờ→Bình thường; K81 vẫn Mở, holder An; số cảnh cáo không tăng | END:SUCCESS | FR-M08-07.01, FR-M08-07.05, FR-M08-07.07, BR-M08-23, BR-M08-48 |


**E13 — thay toàn bộ M1 đến kết thúc:** User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-006 E13 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E13.1 | ACT-002 | Người yêu cầu chọn xét và quyết định nội dung đang chờ sau ai. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E13.2 | FR-M08-07.06 |
| E13.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |


**E14 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-006 E14 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E14.1 | ACT-001 | Người yêu cầu chọn xét và quyết định nội dung đang chờ sau ai. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E14.2 | FR-M08-07.06 |
| E14.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |


**E15 — thay toàn bộ M1 đến kết thúc:** An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-006 E15 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E15.1 | ACT-007 | An mở nội dung đang chờ xét của K81. | P81 Bị gắn cờ; holder An | E15.2 | FR-M08-07.06 |
| E15.2 | SYSTEM | Hệ thống kiểm staff/phạm vi/quyền giữ, vụ và nội dung còn chờ xét; trả nội dung, loại/điểm AI và các quyết định tương ứng, không tự tăng cảnh cáo. | P81 Bị gắn cờ; nhóm Quấy rối, điểm minh họa 0.7 | E15.3 | FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.06, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| E15.3 | ACT-007 | An quyết định giữ bài vì không vi phạm. | P81; giữ bài, không cảnh cáo | E15.4 | FR-M08-07.01 |
| E15.4 | SYSTEM | Hệ thống kiểm lại guard, chuyển P81 về Hoa thường và trả kết quả đã xét. Không tự kết luận vụ hoặc đồng nhất quyết định nội dung với chế tài tác giả. | P81 Bị gắn cờ→Hoa thường; K81 vẫn Mở, holder An; số cảnh cáo không tăng | END:SUCCESS | FR-M08-07.01, FR-M08-07.05, FR-M08-07.07, BR-M08-23, BR-M08-48 |


**E16 — thay toàn bộ M1 đến kết thúc:** An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-006 E16 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E16.1 | ACT-007 | An yêu cầu xét và quyết định nội dung đang chờ sau ai đối với vụ của chính mình. | target type=post/comment/account; owner=ADM-AN; không phải nhóm | E16.2 | FR-M08-07.06 |
| E16.2 | SYSTEM | Hệ thống loại vụ khỏi phạm vi nhìn thấy/nhận và từ chối truy cập/xử lý đối tượng của chính An theo nguồn, không cấp quyền nhờ role Admin. | Không trả dữ liệu tố cáo/không áp biện pháp | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |


<!-- sc:end SC-M08-006 -->

<a id="sc-m08-007"></a>

<!-- sc:scenario SC-M08-007 -->

### SC-M08-007

#### 1. Tên kịch bản chuẩn

Ẩn một bài viết hoặc bình luận vi phạm trong vụ — BF-M08-007; owner [UC-M08-008](../../us/US-M08.md#uc-m08-008).

#### 2. Actor thực hiện

ACT-008 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Có nội dung và vụ liên quan; kiểm giữ vụ/role/trạng thái khi xử lý. Chuẩn P81 chưa bị ẩn, K81 Mở do Mai giữ, Bình USER, actor đã xác định vi phạm.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-007 -->

| result | condition |
|---|---|
| SUCCESS | Nội dung hợp lệ đã Bị ẩn, dữ liệu/log giữ và hệ quả điểm/hiển thị theo owner; không tự cảnh cáo/ban hoặc kết luận vụ. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-007 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai chọn Ẩn P81 trong K81 vì vi phạm. | P81 Đã đăng/Bình thường; lý do=Quấy rối | M2 | FR-M08-06.01 |
| M2 | SYSTEM | Hệ thống kiểm staff, phạm vi và còn giữ K81, đúng target chưa ẩn; chuyển P81 sang Bị ẩn (Bị Mod ẩn theo M03), giữ dữ liệu, ghi log actor/target/lý do/thời điểm. Áp hiển thị và trừ ngay phần điểm từ upvote hiệu lực theo M12, ghi số điểm đã trừ; trả đã ẩn. Không xóa bài người khác hoặc tự đóng vụ. | P81→Bị ẩn; tác giả có 100 điểm, P81 có 5 Post Star × 2 điểm/Star = 10 điểm hiệu lực → 90, ghi khoản đã trừ 10 điểm cho P81; K81 vẫn Mở | END:SUCCESS | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11, FR-M12-02.01, BR-M12-05 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-007 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Mai chọn ẩn bình luận thay bài viết | E1.1 | FR-M08-06.02, FR-M08-06.01, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11, FR-M08-05.11 |
| E2 | system | M2 | Nội dung đã Bị ẩn | E2.1 | FR-M08-06.05 |
| E3 | system | M2 | Yêu cầu xóa nội dung người khác thay thao tác Ẩn | E3.1 | FR-M08-06.03, BR-M08-16 |
| E4 | system | M2 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | E4.1 | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |
| E5 | system | M2 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | E5.1 | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |
| E6 | system | M2 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | E6.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |
| E7 | user-choice | M2 | Quyền giữ đã tự nhả sau đủ 30 phút không hoạt động; K81 vẫn Mở/chưa ai nhận, Mai còn đủ phạm vi và chọn nhận lại | E7.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-16.07, FR-M08-03.01, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-06.01 |
| E8 | system | M1 | ACT-007 — An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11 |
| E9 | system | M1 | ACT-002 — User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11, BR-M08-44 |
| E10 | system | M1 | ACT-001 — Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11, BR-M08-44 |
| E11 | system | M1 | ACT-007 — An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E11.1 | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11 |
| E12 | system | M1 | ACT-007 — An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E12.1 | FR-M08-06.01, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |


<!-- sc:branch SC-M08-007 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-008 | Mai chọn Ẩn C81 trong K81 vì vi phạm. | C81 chưa Bị ẩn; K81 Mở về C81 do Mai giữ, Bình USER | E1.2 | FR-M08-06.02 |
| E1.2 | SYSTEM | Hệ thống kiểm staff/phạm vi/giữ/target và chưa ẩn; chuyển C81 Bị ẩn, ghi log và áp trừ phần điểm từ upvote hiệu lực theo M12, trả đã ẩn. Không xóa bình luận hoặc tự đóng vụ; thông báo kết luận comment không có khiếu nại. | C81 Bình thường→Bị ẩn; 3 điểm upvote hiệu lực→trừ 3; K81 Mở | END:SUCCESS | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11, FR-M08-05.11 |


<!-- sc:branch SC-M08-007 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối ẩn lần nữa; không tạo tác động ẩn/trừ điểm lặp từ yêu cầu này. | P81 hoặc C81 Bị ẩn | END:REJECTED | FR-M08-06.05 |


<!-- sc:branch SC-M08-007 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống không cung cấp/thực hiện xóa nội dung người khác; giữ dữ liệu và yêu cầu xử lý theo thao tác Ẩn đúng quyền. | operation=delete; target thuộc Bình | END:REJECTED | FR-M08-06.03, BR-M08-16 |


<!-- sc:branch SC-M08-007 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-MAI | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |


<!-- sc:branch SC-M08-007 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-HOA | END:REJECTED | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |


<!-- sc:branch SC-M08-007 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống kiểm hiện tại và từ chối tác động ngoài vụ đang giữ; không áp biện pháp/kết luận thành công. | K81 holder Hoa hoặc target không thuộc vụ Mai giữ; dữ liệu đã áp trước đó giữ nguyên | END:REJECTED | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |


<!-- sc:branch SC-M08-007 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối yêu cầu theo quyền giữ cũ, cho biết K81 Mở chưa ai giữ; không tự gắn lại Mai hoặc ghi log tự nhả. | lastActivity=T−30 phút; người khác chỉ xem không làm mới mốc; holder=trống | E7.2 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-16.07 |
| E7.2 | ACT-008 | Mai chọn Nhận xử lý lại K81. | K81 còn Mở/chưa ai giữ; Mai đủ quyền | E7.3 | FR-M08-03.01 |
| E7.3 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/trạng thái/chưa giữ, gắn duy nhất Mai giữ K81, trả đã nhận; không log nhận. | holder=Mai; activity=T | E7.4 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-16.07, BR-M08-08 |
| E7.4 | ACT-008 | Mai chọn Ẩn P81 trong K81 vì vi phạm. | P81 Đã đăng/Bình thường; lý do=Quấy rối; quyền vừa nhận lại còn hợp lệ | M2 | FR-M08-06.01 |


**E8 — thay toàn bộ M1 đến kết thúc:** An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-007 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-007 | An chọn Ẩn P81 trong K81 vì vi phạm. | P81 Đã đăng/Bình thường; lý do=Quấy rối | E8.2 | FR-M08-06.01 |
| E8.2 | SYSTEM | Hệ thống kiểm staff, phạm vi và còn giữ K81, đúng target chưa ẩn; chuyển P81 sang Bị ẩn (Bị Mod ẩn theo M03), giữ dữ liệu, ghi log actor/target/lý do/thời điểm. Áp hiển thị và trừ ngay phần điểm từ upvote hiệu lực theo M12, ghi số điểm đã trừ; trả đã ẩn. Không xóa bài người khác hoặc tự đóng vụ. | P81→Bị ẩn; tác giả có 100 điểm, P81 có 5 Post Star × 2 điểm/Star = 10 điểm hiệu lực → 90, ghi khoản đã trừ 10 điểm cho P81; K81 vẫn Mở | END:SUCCESS | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11, FR-M12-02.01, BR-M12-05 |


**E9 — thay toàn bộ M1 đến kết thúc:** User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-007 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-002 | Người yêu cầu chọn ẩn một bài viết hoặc bình luận vi phạm trong vụ. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E9.2 | FR-M08-06.01 |
| E9.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11, BR-M08-44 |


**E10 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-007 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-001 | Người yêu cầu chọn ẩn một bài viết hoặc bình luận vi phạm trong vụ. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E10.2 | FR-M08-06.01 |
| E10.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11, BR-M08-44 |


**E11 — thay toàn bộ M1 đến kết thúc:** An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-007 E11 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E11.1 | ACT-007 | An chọn Ẩn P81 trong K81 vì vi phạm. | P81 Đã đăng/Hoa thường; lý do=Quấy rối | E11.2 | FR-M08-06.01 |
| E11.2 | SYSTEM | Hệ thống kiểm staff, phạm vi và còn giữ K81, đúng target chưa ẩn; chuyển P81 sang Bị ẩn (Bị Mod ẩn theo M03), giữ dữ liệu, ghi log actor/target/lý do/thời điểm. Áp hiển thị và trừ ngay phần điểm từ upvote hiệu lực theo M12, ghi số điểm đã trừ; trả đã ẩn. Không xóa bài người khác hoặc tự đóng vụ. | P81→Bị ẩn; tác giả có 100 điểm, P81 có 5 Post Star × 2 điểm/Star = 10 điểm hiệu lực → 90, ghi khoản đã trừ 10 điểm cho P81; K81 vẫn Mở | END:SUCCESS | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11, FR-M12-02.01, BR-M12-05 |


**E12 — thay toàn bộ M1 đến kết thúc:** An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-007 E12 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E12.1 | ACT-007 | An yêu cầu ẩn một bài viết hoặc bình luận vi phạm trong vụ đối với vụ của chính mình. | target type=post/comment/account; owner=ADM-AN; không phải nhóm | E12.2 | FR-M08-06.01 |
| E12.2 | SYSTEM | Hệ thống loại vụ khỏi phạm vi nhìn thấy/nhận và từ chối truy cập/xử lý đối tượng của chính An theo nguồn, không cấp quyền nhờ role Admin. | Không trả dữ liệu tố cáo/không áp biện pháp | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |


<!-- sc:end SC-M08-007 -->

<a id="sc-m08-008"></a>

<!-- sc:scenario SC-M08-008 -->

### SC-M08-008

#### 1. Tên kịch bản chuẩn

Cảnh cáo người vi phạm được xác định trong vụ — BF-M08-008; owner [UC-M08-009](../../us/US-M08.md#uc-m08-009).

#### 2. Actor thực hiện

ACT-008 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Có vụ và đối tượng vi phạm được con người đánh giá; không mặc định Bác bỏ là reporter ác ý. Chuẩn Mai giữ K81 về Bình USER, số cảnh cáo 2/LIGHT, chưa HEAVY, lý do Quấy rối.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-008 -->

| result | condition |
|---|---|
| SUCCESS | Cảnh cáo hợp lệ đã lưu issuer/lý do/vụ, tăng số lần/tính mức/reset hạn đúng chính sách, áp hạn chế/log và sự kiện app có khiếu nại. Vụ chưa tự đóng; không cảnh cáo mới khi target đã HEAVY. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-008 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai chọn cảnh cáo Bình trong K81 và nhập lý do. | target=U-BINH USER; 2/LIGHT; reason=Quấy rối | M2 | FR-M08-10.01 |
| M2 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Mod/Admin đối với Mod và chưa HEAVY; ghi cảnh cáo do Mai ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Bình: số lần 2→3, mức mới MEDIUM, hạn=T+10×24h; record issuer=Mai; K81 Mở; cảnh cáo chỉ app, không email | END:SUCCESS | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-008 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Target chưa HEAVY, số lần hiện tại 0 | E1.1 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |
| E2 | system | M2 | Target chưa HEAVY, số lần hiện tại 1 | E2.1 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |
| E3 | system | M2 | Target chưa HEAVY, số lần hiện tại 3 | E3.1 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |
| E4 | system | M2 | Target chưa HEAVY, số lần hiện tại 4 | E4.1 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |
| E5 | user-choice | M1 | Mai xác định reporter cố ý báo cáo ác ý trong vụ sau đánh giá con người | E5.1 | FR-M08-10.04, FR-M08-10.05, BR-M08-18, BR-M08-19, FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |
| E6 | user-choice | M1 | Vụ về tài khoản hoặc nhóm, staff chọn cảnh cáo người bị báo cáo/Owner riêng | E6.1 | FR-M08-10.01, FR-M08-10.06, FR-M08-04.10, BR-M08-17, BR-M08-50, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |
| E7 | system | M2 | Mod chọn cảnh cáo Mod khác | E7.1 | FR-M08-10.08, BR-M08-46 |
| E8 | system | M2 | Target là Admin | E8.1 | FR-M08-10.09, BR-M08-46, BR-M08-55 |
| E9 | user-choice | M2 | Bình đã HEAVY; Mai chọn Ban sau khi cảnh cáo mới bị từ chối | E9.1 | FR-M08-10.10, FR-M08-14.11, BR-M08-36, FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |
| E10 | system | M2 | Bình đã HEAVY, Mai không chọn Ban | E10.1 | FR-M08-10.10, FR-M08-14.11, BR-M08-36 |
| E11 | system | M2 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | E11.1 | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |
| E12 | system | M2 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | E12.1 | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |
| E13 | system | M2 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | E13.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |
| E14 | user-choice | M2 | Quyền giữ đã tự nhả sau đủ 30 phút không hoạt động; K81 vẫn Mở/chưa ai nhận, Mai còn đủ phạm vi và chọn nhận lại | E14.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-16.07, FR-M08-03.01, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-10.01 |
| E15 | system | M1 | ACT-007 — An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E15.1 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |
| E16 | system | M1 | ACT-002 — User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E16.1 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53, BR-M08-44 |
| E17 | system | M1 | ACT-001 — Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E17.1 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53, BR-M08-44 |
| E18 | system | M1 | ACT-007 — An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E18.1 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |
| E19 | system | M1 | ACT-007 — An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E19.1 | FR-M08-10.01, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |
| E20 | system | M1 | ACT-007 — Ngay cả Admin không được cảnh cáo/ban Admin khác. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E20.1 | FR-M08-10.01, FR-M08-10.09, FR-M08-14.10, BR-M08-46, BR-M08-55 |


<!-- sc:branch SC-M08-008 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Mod/Admin đối với Mod và chưa HEAVY; ghi cảnh cáo do Mai ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Bình: số lần 0→1, mức mới LIGHT, hạn=T+7×24h; record issuer=Mai; K81 Mở; cảnh cáo chỉ app, không email | END:SUCCESS | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |


<!-- sc:branch SC-M08-008 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Mod/Admin đối với Mod và chưa HEAVY; ghi cảnh cáo do Mai ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Bình: số lần 1→2, mức mới LIGHT, hạn=T+7×24h; record issuer=Mai; K81 Mở; cảnh cáo chỉ app, không email | END:SUCCESS | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |


<!-- sc:branch SC-M08-008 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Mod/Admin đối với Mod và chưa HEAVY; ghi cảnh cáo do Mai ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Bình: số lần 3→4, mức mới MEDIUM, hạn=T+10×24h; record issuer=Mai; K81 Mở; cảnh cáo chỉ app, không email | END:SUCCESS | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |


<!-- sc:branch SC-M08-008 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Mod/Admin đối với Mod và chưa HEAVY; ghi cảnh cáo do Mai ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Bình: số lần 4→5, mức mới HEAVY, hạn=T+15×24h; record issuer=Mai; K81 Mở; cảnh cáo chỉ app, không email | END:SUCCESS | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |


<!-- sc:branch SC-M08-008 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-008 | Mai chọn cảnh cáo Lan là reporter của K81 vì cố ý báo cáo ác ý và ghi lý do. | Lan USER; hiện 2/LIGHT; chỉ số 6/10 là tham khảo, không đủ tự kết tội; Mai đã đánh giá bằng chứng | E5.2 | FR-M08-10.04, FR-M08-10.05, BR-M08-18, BR-M08-19 |
| E5.2 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Mod/Admin đối với Mod và chưa HEAVY; ghi cảnh cáo do Mai ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Lan: số lần 2→3, mức mới MEDIUM, hạn=T+10×24h; record issuer=Mai; K81 Mở; cảnh cáo chỉ app, không email | END:SUCCESS | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |


<!-- sc:branch SC-M08-008 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-008 | Mai chọn cảnh cáo Bình trong vụ về tài khoản hoặc nhóm và nhập lý do đã xác định. | Bình USER 2/LIGHT; nếu nhóm thì Bình là Owner, Mai khác Owner; K81 Mở do Mai giữ | E6.2 | FR-M08-10.01, FR-M08-10.06, FR-M08-04.10, BR-M08-17, BR-M08-50 |
| E6.2 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Mod/Admin đối với Mod và chưa HEAVY; ghi cảnh cáo do Mai ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Bình (người bị báo cáo hoặc Owner): số lần 2→3, mức mới MEDIUM, hạn=T+10×24h; record issuer=Mai; K81 Mở; cảnh cáo chỉ app, không email | END:SUCCESS | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |


<!-- sc:branch SC-M08-008 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối cảnh cáo Mod; chỉ Admin được quyết đúng quyền, không tăng số lần. | actor Mai MODERATOR; target MOD-HOA | END:REJECTED | FR-M08-10.08, BR-M08-46 |


<!-- sc:branch SC-M08-008 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống từ chối cảnh cáo Admin với mọi người thao tác. | target U-ADMIN | END:REJECTED | FR-M08-10.09, BR-M08-46, BR-M08-55 |


<!-- sc:branch SC-M08-008 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống từ chối tăng cảnh cáo, đánh dấu yêu cầu ban trên K81 và trả lựa chọn để con người cân nhắc; không tự ban. | Bình 5/HEAVY, giữ 5; K81 Mai giữ; không có ban Đang hiệu lực | E9.2 | FR-M08-10.10, FR-M08-14.11, BR-M08-36 |
| E9.2 | ACT-008 | Mai chọn Ban trong K81 và nhập lý do tái phạm. | Bình USER; lịch sử 0; kiểm lại quyền giữ khi ban | E9.3 | FR-M08-14.01 |
| E9.3 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Admin, Mod chỉ do Admin xử lý và không có ban Đang hiệu lực. Đếm lịch sử mọi ban từng hiệu lực, gồm đã gỡ/vĩnh viễn thủ công, loại Bị lật; áp thời hạn leo thang. Ghi ban Đang hiệu lực với lý do/người làm/mốc bắt đầu, đặt account BANNED; nếu target là Mod thì thu hồi vai trò về USER. Ghi log, phát sự kiện app+email lý do/đường khiếu nại, trả đã ban; không reset cảnh cáo/thử thách hoặc tự đóng vụ. | Bình; lệnh=Ban; số ban trước tính được=0; thời hạn=30×24h; bắt đầu T; account→BANNED; K81 Mở | END:SUCCESS | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |


<!-- sc:branch SC-M08-008 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống từ chối cảnh cáo mới, giữ số lần hiện hành và đánh dấu yêu cầu ban; không có ban khi con người chưa quyết. | Bình 5 hoặc 6/HEAVY; K81 vẫn Mở; quyền Ban là quyết định riêng | END:REJECTED | FR-M08-10.10, FR-M08-14.11, BR-M08-36 |


<!-- sc:branch SC-M08-008 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-MAI | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |


<!-- sc:branch SC-M08-008 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-HOA | END:REJECTED | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |


<!-- sc:branch SC-M08-008 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | SYSTEM | Hệ thống kiểm hiện tại và từ chối tác động ngoài vụ đang giữ; không áp biện pháp/kết luận thành công. | K81 holder Hoa hoặc target không thuộc vụ Mai giữ; dữ liệu đã áp trước đó giữ nguyên | END:REJECTED | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |


<!-- sc:branch SC-M08-008 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | SYSTEM | Hệ thống từ chối yêu cầu theo quyền giữ cũ, cho biết K81 Mở chưa ai giữ; không tự gắn lại Mai hoặc ghi log tự nhả. | lastActivity=T−30 phút; người khác chỉ xem không làm mới mốc; holder=trống | E14.2 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-16.07 |
| E14.2 | ACT-008 | Mai chọn Nhận xử lý lại K81. | K81 còn Mở/chưa ai giữ; Mai đủ quyền | E14.3 | FR-M08-03.01 |
| E14.3 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/trạng thái/chưa giữ, gắn duy nhất Mai giữ K81, trả đã nhận; không log nhận. | holder=Mai; activity=T | E14.4 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-16.07, BR-M08-08 |
| E14.4 | ACT-008 | Mai chọn cảnh cáo Bình trong K81 và nhập lý do. | target=U-BINH USER; 2/LIGHT; reason=Quấy rối; quyền vừa nhận lại còn hợp lệ | M2 | FR-M08-10.01 |


**E15 — thay toàn bộ M1 đến kết thúc:** An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-008 E15 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E15.1 | ACT-007 | An chọn cảnh cáo Bình trong K81 và nhập lý do. | target=U-BINH USER; 2/LIGHT; reason=Quấy rối | E15.2 | FR-M08-10.01 |
| E15.2 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Mod/Admin đối với Mod và chưa HEAVY; ghi cảnh cáo do An ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Bình: số lần 2→3, mức mới MEDIUM, hạn=T+10×24h; record issuer=An; K81 Mở; cảnh cáo chỉ app, không email | END:SUCCESS | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |


**E16 — thay toàn bộ M1 đến kết thúc:** User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-008 E16 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E16.1 | ACT-002 | Người yêu cầu chọn cảnh cáo người vi phạm được xác định trong vụ. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E16.2 | FR-M08-10.01 |
| E16.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53, BR-M08-44 |


**E17 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-008 E17 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E17.1 | ACT-001 | Người yêu cầu chọn cảnh cáo người vi phạm được xác định trong vụ. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E17.2 | FR-M08-10.01 |
| E17.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53, BR-M08-44 |


**E18 — thay toàn bộ M1 đến kết thúc:** An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-008 E18 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E18.1 | ACT-007 | An chọn cảnh cáo Hoa trong K81 và nhập lý do. | target=MOD-HOA MODERATOR; 2/LIGHT; reason=Quấy rối | E18.2 | FR-M08-10.01 |
| E18.2 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, actor An là Admin, target Hoa là Mod khác An và không phải Admin và chưa HEAVY; ghi cảnh cáo do An ra với lý do/vụ, tăng số lần và tính mức. Reset thử thách đúng mức từ T, áp hạn chế riêng tư; ghi log và sự kiện app kèm khiếu nại, trả đã cảnh cáo. Không tự ẩn nội dung/ban hoặc đóng vụ. | Hoa: số lần 2→3, mức mới MEDIUM, hạn=T+10×24h; record issuer=An; K81 Mở; cảnh cáo chỉ app, không email | END:SUCCESS | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |


**E19 — thay toàn bộ M1 đến kết thúc:** An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-008 E19 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E19.1 | ACT-007 | An yêu cầu cảnh cáo người vi phạm được xác định trong vụ đối với vụ của chính mình. | target type=post/comment/account; owner=ADM-AN; không phải nhóm | E19.2 | FR-M08-10.01 |
| E19.2 | SYSTEM | Hệ thống loại vụ khỏi phạm vi nhìn thấy/nhận và từ chối truy cập/xử lý đối tượng của chính An theo nguồn, không cấp quyền nhờ role Admin. | Không trả dữ liệu tố cáo/không áp biện pháp | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |


**E20 — thay toàn bộ M1 đến kết thúc:** Ngay cả Admin không được cảnh cáo/ban Admin khác. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-008 E20 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E20.1 | ACT-007 | An chọn cảnh cáo Admin khác. | target=ADM-BAO ADMIN | E20.2 | FR-M08-10.01 |
| E20.2 | SYSTEM | Hệ thống từ chối chế tài Admin; không tăng cảnh cáo/tạo ban hoặc thu hồi role. | Admin miễn cảnh cáo/ban | END:REJECTED | FR-M08-10.09, FR-M08-14.10, BR-M08-46, BR-M08-55 |


<!-- sc:end SC-M08-008 -->

<a id="sc-m08-009"></a>

<!-- sc:scenario SC-M08-009 -->

### SC-M08-009

#### 1. Tên kịch bản chuẩn

Bỏ một cảnh cáo do AI ra — BF-M08-009; owner [UC-M08-010](../../us/US-M08.md#uc-m08-010).

#### 2. Actor thực hiện

ACT-008 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Xác định record AI và target, không đòi vụ đang giữ. Đường đủ hợp đồng: cảnh cáo AI chưa bỏ, số lần hiện tại >0. Số lần 0 còn record lịch sử là GAP002, không tự đặt sàn 0/đếm âm/từ chối sản phẩm.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-009 -->

| result | condition |
|---|---|
| SUCCESS | Record AI được giữ/đánh dấu đã bỏ, số lần giảm một và mức tính lại trong trường hợp số lần dương; hạn cũ giữ, nội dung ẩn giữ, log có. Không bao phủ phép trừ tại số lần 0 chưa chốt. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-009 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai chọn bỏ cảnh cáo AI W81 của Bình. | W81 do AI ra, chưa bỏ; Bình 3/MEDIUM; hạn hiện tại 19/11/2026 10:00+07 | M2 | FR-M08-11.01 |
| M2 | SYSTEM | Hệ thống kiểm vai trò staff và cảnh cáo do AI ra, giảm số lần một và tính mức; giữ record đánh dấu đã bỏ, giữ nguyên hạn thử thách hiện tại, áp hạn chế mức mới và ghi log bỏ AI rồi trả kết quả. Không tự hiện lại nội dung đã ẩn, giảm lần lần hai theo kết quả M09 hoặc đặt hạn mới. | Số lần 3→2, MEDIUM→LIGHT; hạn vẫn 19/11 10:00+07; W81 đã bỏ, không xóa; C81 vẫn Bị ẩn; không cần holder | END:SUCCESS | FR-M08-11.01, FR-M08-11.02, FR-M08-11.03, FR-M08-11.04, FR-M08-11.05, FR-M08-16.05, BR-M08-28, BR-M08-31, BR-M08-54 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-009 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Cảnh cáo do staff ra, không phải AI | E1.1 | FR-M08-11.01 |
| E2 | system | M2 | Cảnh cáo AI chưa bỏ và số lần hiện hành là 1, đủ điều kiện bỏ | E2.1 | FR-M08-11.01, FR-M08-11.03, FR-M08-11.04, FR-M08-11.05, FR-M08-16.05, BR-M08-28, BR-M08-54 |
| E3 | system | M1 | ACT-007 — An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E3.1 | FR-M08-11.01, FR-M08-11.02, FR-M08-11.03, FR-M08-11.04, FR-M08-11.05, FR-M08-16.05, BR-M08-28, BR-M08-31, BR-M08-54 |
| E4 | system | M1 | ACT-002 — User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M08-11.01, FR-M08-11.02, FR-M08-11.03, FR-M08-11.04, FR-M08-11.05, FR-M08-16.05, BR-M08-28, BR-M08-31, BR-M08-54, BR-M08-44 |
| E5 | system | M1 | ACT-001 — Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M08-11.01, FR-M08-11.02, FR-M08-11.03, FR-M08-11.04, FR-M08-11.05, FR-M08-16.05, BR-M08-28, BR-M08-31, BR-M08-54, BR-M08-44 |


<!-- sc:branch SC-M08-009 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống không dùng thao tác bỏ cảnh cáo AI cho record do staff ra; không sửa số lần/record. | W82 issuer=MOD-HOA | END:REJECTED | FR-M08-11.01 |


<!-- sc:branch SC-M08-009 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống kiểm staff/record AI, giảm số lần từ 1 xuống 0, tính mức Sạch; giữ record đánh dấu đã bỏ, giữ nguyên hạn thử thách hiện tại, áp hạn chế mức mới và ghi log rồi trả kết quả. Không tự hiện lại nội dung ẩn. | W81 chưa bỏ→đã bỏ; 1/LIGHT→0/Sạch; hạn hiện tại 16/11 10:00+07 giữ nguyên; khác GAP002 nơi số lần đã 0 trước bỏ | END:SUCCESS | FR-M08-11.01, FR-M08-11.03, FR-M08-11.04, FR-M08-11.05, FR-M08-16.05, BR-M08-28, BR-M08-54 |


**E3 — thay toàn bộ M1 đến kết thúc:** An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-009 E3 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E3.1 | ACT-007 | An chọn bỏ cảnh cáo AI W81 của Bình. | W81 do AI ra, chưa bỏ; Bình 3/MEDIUM; hạn hiện tại 19/11/2026 10:00+07 | E3.2 | FR-M08-11.01 |
| E3.2 | SYSTEM | Hệ thống kiểm vai trò staff và cảnh cáo do AI ra, giảm số lần một và tính mức; giữ record đánh dấu đã bỏ, giữ nguyên hạn thử thách hiện tại, áp hạn chế mức mới và ghi log bỏ AI rồi trả kết quả. Không tự hiện lại nội dung đã ẩn, giảm lần lần hai theo kết quả M09 hoặc đặt hạn mới. | Số lần 3→2, MEDIUM→LIGHT; hạn vẫn 19/11 10:00+07; W81 đã bỏ, không xóa; C81 vẫn Bị ẩn; không cần holder | END:SUCCESS | FR-M08-11.01, FR-M08-11.02, FR-M08-11.03, FR-M08-11.04, FR-M08-11.05, FR-M08-16.05, BR-M08-28, BR-M08-31, BR-M08-54 |


**E4 — thay toàn bộ M1 đến kết thúc:** User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-009 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-002 | Người yêu cầu chọn bỏ một cảnh cáo do ai ra. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E4.2 | FR-M08-11.01 |
| E4.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-11.01, FR-M08-11.02, FR-M08-11.03, FR-M08-11.04, FR-M08-11.05, FR-M08-16.05, BR-M08-28, BR-M08-31, BR-M08-54, BR-M08-44 |


**E5 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-009 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-001 | Người yêu cầu chọn bỏ một cảnh cáo do ai ra. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E5.2 | FR-M08-11.01 |
| E5.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-11.01, FR-M08-11.02, FR-M08-11.03, FR-M08-11.04, FR-M08-11.05, FR-M08-16.05, BR-M08-28, BR-M08-31, BR-M08-54, BR-M08-44 |


<!-- sc:end SC-M08-009 -->

<a id="sc-m08-010"></a>

<!-- sc:scenario SC-M08-010 -->

### SC-M08-010

#### 1. Tên kịch bản chuẩn

Ban người vi phạm trong vụ theo quyết định con người — BF-M08-010; owner [UC-M08-011](../../us/US-M08.md#uc-m08-011).

#### 2. Actor thực hiện

ACT-008 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Có quyết định con người trong vụ; quyền giữ/role/ban hiệu lực kiểm lại. Chuẩn Mai giữ K81 về Bình USER, vi phạm đã xác định, chưa có ban Đang hiệu lực và không có ban trước được tính.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-010 -->

| result | condition |
|---|---|
| SUCCESS | Đúng một ban Đang hiệu lực được tạo theo lệnh/lịch sử, account BANNED và Mod target bị thu hồi role nếu có; log/sự kiện app+email có khiếu nại. Không tự giải quyết vụ, tự AI ban hoặc thay thử thách cảnh cáo. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-010 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai chọn Ban Bình trong K81, nhập lý do vi phạm. | command=Ban; target=U-BINH; reason=Tái phạm đã xác định; số ban trước 0 | M2 | FR-M08-14.01 |
| M2 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Admin, Mod chỉ do Admin xử lý và không có ban Đang hiệu lực. Đếm lịch sử mọi ban từng hiệu lực, gồm đã gỡ/vĩnh viễn thủ công, loại Bị lật; áp thời hạn leo thang. Ghi ban Đang hiệu lực với lý do/người làm/mốc bắt đầu, đặt account BANNED; nếu target là Mod thì thu hồi vai trò về USER. Ghi log, phát sự kiện app+email lý do/đường khiếu nại, trả đã ban; không reset cảnh cáo/thử thách hoặc tự đóng vụ. | Bình; lệnh=Ban; số ban trước tính được=0; thời hạn=30×24h; bắt đầu T; account→BANNED; K81 Mở | END:SUCCESS | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-010 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Lệnh Ban với 1 ban trước được tính, không có ban Đang hiệu lực | E1.1 | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |
| E2 | system | M2 | Lệnh Ban với 2 ban trước được tính, không có ban Đang hiệu lực | E2.1 | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |
| E3 | user-choice | M1 | Người giữ chọn Ban vĩnh viễn thay Ban | E3.1 | FR-M08-14.02, FR-M08-14.01, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |
| E4 | system | M2 | Mod chọn ban Mod khác | E4.1 | FR-M08-14.09, BR-M08-46 |
| E5 | system | M2 | Target là Admin | E5.1 | FR-M08-14.10, BR-M08-46, BR-M08-55 |
| E6 | user-choice | M2 | Target đang có ban Đang hiệu lực, Mai muốn thay bằng ban vĩnh viễn | E6.1 | FR-M08-14.13, BR-M08-52, FR-M08-15.01, FR-M08-15.05, FR-M08-15.02, FR-M08-16.05, BR-M08-34, BR-M08-38, FR-M10-06.02, FR-M08-14.02, FR-M08-14.01, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.14, BR-M08-33, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53, FR-M10-06.01 |
| E7 | system | M2 | Target có ban Đang hiệu lực và không chọn gỡ trước | E7.1 | FR-M08-14.13, BR-M08-52 |
| E8 | system | M2 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | E8.1 | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |
| E9 | system | M2 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | E9.1 | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |
| E10 | system | M2 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | E10.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |
| E11 | user-choice | M2 | Quyền giữ đã tự nhả sau đủ 30 phút không hoạt động; K81 vẫn Mở/chưa ai nhận, Mai còn đủ phạm vi và chọn nhận lại | E11.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-16.07, FR-M08-03.01, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-14.01 |
| E12 | user-choice | M1 | Vụ từ đầu về nhóm G81, Mai chọn Ban Owner Bình USER riêng với biện pháp nhóm | E12.1 | FR-M08-04.10, FR-M08-14.01, BR-M08-48, BR-M08-50, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-52, BR-M08-53, FR-M10-06.01, FR-M11-11.01, FR-M11-11.05, FR-M11-11.06, FR-M11-11.07 |
| E13 | system | M1 | ACT-007 — An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E13.1 | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |
| E14 | system | M1 | ACT-002 — User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E14.1 | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01, BR-M08-44 |
| E15 | system | M1 | ACT-001 — Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E15.1 | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01, BR-M08-44 |
| E16 | system | M1 | ACT-007 — An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E16.1 | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |
| E17 | system | M1 | ACT-007 — An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E17.1 | FR-M08-14.01, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |
| E18 | system | M1 | ACT-007 — Ngay cả Admin không được cảnh cáo/ban Admin khác. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E18.1 | FR-M08-14.01, FR-M08-10.09, FR-M08-14.10, BR-M08-46, BR-M08-55 |


<!-- sc:branch SC-M08-010 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Admin, Mod chỉ do Admin xử lý và không có ban Đang hiệu lực. Đếm lịch sử mọi ban từng hiệu lực, gồm đã gỡ/vĩnh viễn thủ công, loại Bị lật; áp thời hạn leo thang. Ghi ban Đang hiệu lực với lý do/người làm/mốc bắt đầu, đặt account BANNED; nếu target là Mod thì thu hồi vai trò về USER. Ghi log, phát sự kiện app+email lý do/đường khiếu nại, trả đã ban; không reset cảnh cáo/thử thách hoặc tự đóng vụ. | Bình; lệnh=Ban; số ban trước tính được=1; thời hạn=90×24h; bắt đầu T; account→BANNED; K81 Mở | END:SUCCESS | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |


<!-- sc:branch SC-M08-010 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Admin, Mod chỉ do Admin xử lý và không có ban Đang hiệu lực. Đếm lịch sử mọi ban từng hiệu lực, gồm đã gỡ/vĩnh viễn thủ công, loại Bị lật; áp thời hạn leo thang. Ghi ban Đang hiệu lực với lý do/người làm/mốc bắt đầu, đặt account BANNED; nếu target là Mod thì thu hồi vai trò về USER. Ghi log, phát sự kiện app+email lý do/đường khiếu nại, trả đã ban; không reset cảnh cáo/thử thách hoặc tự đóng vụ. | Bình; lệnh=Ban; số ban trước tính được=2; thời hạn=vĩnh viễn; bắt đầu T; account→BANNED; K81 Mở | END:SUCCESS | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |


<!-- sc:branch SC-M08-010 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-008 | Mai chọn Ban vĩnh viễn Bình trong K81 và nhập lý do. | Lịch sử được tính 0; không có ban Đang hiệu lực; lựa chọn thủ công | E3.2 | FR-M08-14.02 |
| E3.2 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Admin, Mod chỉ do Admin xử lý và không có ban Đang hiệu lực. Áp Ban vĩnh viễn thủ công, bỏ leo thang. Ghi ban Đang hiệu lực với lý do/người làm/mốc bắt đầu, đặt account BANNED; nếu target là Mod thì thu hồi vai trò về USER. Ghi log, phát sự kiện app+email lý do/đường khiếu nại, trả đã ban; không reset cảnh cáo/thử thách hoặc tự đóng vụ. | Bình; lệnh=Ban vĩnh viễn; số ban trước tính được=0; thời hạn=vĩnh viễn; bắt đầu T; account→BANNED; K81 Mở | END:SUCCESS | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |


<!-- sc:branch SC-M08-010 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối ban Mod bởi Mod; không ghi ban hoặc thu hồi vai trò. | actor Mai MODERATOR, target MOD-HOA | END:REJECTED | FR-M08-14.09, BR-M08-46 |


<!-- sc:branch SC-M08-010 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối ban Admin, kể cả lệnh Ban vĩnh viễn. | target U-ADMIN | END:REJECTED | FR-M08-14.10, BR-M08-46, BR-M08-55 |


<!-- sc:branch SC-M08-010 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối ban chồng, cho biết phải gỡ ban cũ trước rồi mới thực hiện Ban vĩnh viễn nếu vẫn đủ quyền giữ vụ. | B80 Đang hiệu lực, ban tạm; K81 do Mai giữ | E6.2 | FR-M08-14.13, BR-M08-52 |
| E6.2 | ACT-008 | Mai chọn Gỡ ban B80 trực tiếp. | B80 Đang hiệu lực; không cần vụ cho riêng gỡ ban | E6.3 | FR-M08-15.01, FR-M08-15.05 |
| E6.3 | SYSTEM | Hệ thống kiểm staff/ban hiện tại, chuyển B80 Đã gỡ, account ACTIVE; giữ lịch sử, không khôi phục Mod; ghi log và sự kiện app+email, trả đã gỡ. | B80 Đã gỡ vẫn tính lịch sử; account ACTIVE | E6.4 | FR-M08-15.01, FR-M08-15.02, FR-M08-15.05, FR-M08-16.05, BR-M08-34, BR-M08-38, FR-M10-06.02 |
| E6.4 | ACT-008 | Mai chọn Ban vĩnh viễn trong K81 và nhập lý do. | K81 vẫn Mở và do Mai giữ; không còn ban Đang hiệu lực; B80 tính lịch sử | E6.5 | FR-M08-14.02 |
| E6.5 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Admin, Mod chỉ do Admin xử lý và không có ban Đang hiệu lực. Áp Ban vĩnh viễn thủ công, bỏ leo thang. Ghi ban Đang hiệu lực với lý do/người làm/mốc bắt đầu, đặt account BANNED; nếu target là Mod thì thu hồi vai trò về USER. Ghi log, phát sự kiện app+email lý do/đường khiếu nại, trả đã ban; không reset cảnh cáo/thử thách hoặc tự đóng vụ. | Bình; lệnh=Ban vĩnh viễn; số ban trước tính được=1; thời hạn=vĩnh viễn; bắt đầu T; account→BANNED; K81 Mở | END:SUCCESS | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |


<!-- sc:branch SC-M08-010 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối tạo ban thứ hai; giữ ban hiện tại và tài khoản BANNED. | B80 Đang hiệu lực; không có quyết định gỡ | END:REJECTED | FR-M08-14.13, BR-M08-52 |


<!-- sc:branch SC-M08-010 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-MAI | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46 |


<!-- sc:branch SC-M08-010 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống loại vụ khỏi tập được nhìn thấy/nhận và từ chối yêu cầu trực tiếp; không trả dữ liệu tố cáo hoặc cấp quyền xử lý. | target type=post/comment/account, owner=MOD-HOA | END:REJECTED | FR-M08-02.09, FR-M08-03.09, BR-M08-46 |


<!-- sc:branch SC-M08-010 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống kiểm hiện tại và từ chối tác động ngoài vụ đang giữ; không áp biện pháp/kết luận thành công. | K81 holder Hoa hoặc target không thuộc vụ Mai giữ; dữ liệu đã áp trước đó giữ nguyên | END:REJECTED | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |


<!-- sc:branch SC-M08-010 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | SYSTEM | Hệ thống từ chối yêu cầu theo quyền giữ cũ, cho biết K81 Mở chưa ai giữ; không tự gắn lại Mai hoặc ghi log tự nhả. | lastActivity=T−30 phút; người khác chỉ xem không làm mới mốc; holder=trống | E11.2 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-16.07 |
| E11.2 | ACT-008 | Mai chọn Nhận xử lý lại K81. | K81 còn Mở/chưa ai giữ; Mai đủ quyền | E11.3 | FR-M08-03.01 |
| E11.3 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/trạng thái/chưa giữ, gắn duy nhất Mai giữ K81, trả đã nhận; không log nhận. | holder=Mai; activity=T | E11.4 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-16.07, BR-M08-08 |
| E11.4 | ACT-008 | Mai chọn Ban Bình trong K81, nhập lý do vi phạm. | command=Ban; target=U-BINH; reason=Tái phạm đã xác định; số ban trước 0; quyền vừa nhận lại còn hợp lệ | M2 | FR-M08-14.01 |


<!-- sc:branch SC-M08-010 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | ACT-008 | Mai chọn Ban Owner Bình trong vụ K81 về nhóm G81 và nhập lý do vi phạm đã đánh giá. | K81 Mở do Mai giữ; Owner Bình USER khác Mai, không Admin, không có ban hiệu lực; lịch sử 0; nhóm không tự bị ẩn/khóa từ Ban; G81 có Group Mod Thảo thâm niên dài nhất từ 01/09/2026 | E12.2 | FR-M08-04.10, FR-M08-14.01, BR-M08-48, BR-M08-50 |
| E12.2 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Admin, Mod chỉ do Admin xử lý và không có ban Đang hiệu lực. Đếm lịch sử mọi ban từng hiệu lực, gồm đã gỡ/vĩnh viễn thủ công, loại Bị lật; áp thời hạn leo thang. Ghi ban Đang hiệu lực với lý do/người làm/mốc bắt đầu, đặt account BANNED; nếu target là Mod thì thu hồi vai trò về USER. Ghi log, phát sự kiện app+email lý do/đường khiếu nại, trả đã ban; không reset cảnh cáo/thử thách hoặc tự đóng vụ. M11 đồng thời chuyển ngay Owner từ Bình sang Group Mod Thảo có thâm niên dài nhất, giữ Bình làm Member và phát sự kiện app cho Owner mới; không tự kết luận K81. | Bình (Owner); lệnh=Ban; số ban trước tính được=0; thời hạn=30×24h; bắt đầu T; account→BANNED; K81 Mở; Owner G81 Bình→Thảo; Bình BANNED/Member; K81 Mở, phần kết luận khi Owner đổi còn GAP006 | END:SUCCESS | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01, FR-M11-11.01, FR-M11-11.05, FR-M11-11.06, FR-M11-11.07 |


**E13 — thay toàn bộ M1 đến kết thúc:** An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-010 E13 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E13.1 | ACT-007 | An chọn Ban Bình trong K81, nhập lý do vi phạm. | command=Ban; target=U-BINH; reason=Tái phạm đã xác định; số ban trước 0 | E13.2 | FR-M08-14.01 |
| E13.2 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Admin, Mod chỉ do Admin xử lý và không có ban Đang hiệu lực. Đếm lịch sử mọi ban từng hiệu lực, gồm đã gỡ/vĩnh viễn thủ công, loại Bị lật; áp thời hạn leo thang. Ghi ban Đang hiệu lực với lý do/người làm/mốc bắt đầu, đặt account BANNED; nếu target là Mod thì thu hồi vai trò về USER. Ghi log, phát sự kiện app+email lý do/đường khiếu nại, trả đã ban; không reset cảnh cáo/thử thách hoặc tự đóng vụ. | Bình; lệnh=Ban; số ban trước tính được=0; thời hạn=30×24h; bắt đầu T; account→BANNED; K81 Mở | END:SUCCESS | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |


**E14 — thay toàn bộ M1 đến kết thúc:** User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-010 E14 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E14.1 | ACT-002 | Người yêu cầu chọn ban người vi phạm trong vụ theo quyết định con người. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E14.2 | FR-M08-14.01 |
| E14.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01, BR-M08-44 |


**E15 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-010 E15 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E15.1 | ACT-001 | Người yêu cầu chọn ban người vi phạm trong vụ theo quyết định con người. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E15.2 | FR-M08-14.01 |
| E15.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01, BR-M08-44 |


**E16 — thay toàn bộ M1 đến kết thúc:** An Admin xử lý vụ về Hoa Mod khác mình; chỉ An thấy/nhận/áp chế tài khi đủ quyền giữ, không target Admin; thay actor, target và người giữ nhất quán. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-010 E16 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E16.1 | ACT-007 | An chọn Ban Hoa trong K81, nhập lý do vi phạm. | command=Ban; target=MOD-HOA; reason=Tái phạm đã xác định; số ban trước 0 | E16.2 | FR-M08-14.01 |
| E16.2 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/giữ vụ, target không Admin, Mod chỉ do Admin xử lý và không có ban Đang hiệu lực. Đếm lịch sử mọi ban từng hiệu lực, gồm đã gỡ/vĩnh viễn thủ công, loại Bị lật; áp thời hạn leo thang. Ghi ban Đang hiệu lực với lý do/người làm/mốc bắt đầu, đặt account BANNED; nếu target là Mod thì thu hồi vai trò về USER. Ghi log, phát sự kiện app+email lý do/đường khiếu nại, trả đã ban; không reset cảnh cáo/thử thách hoặc tự đóng vụ. | Hoa; lệnh=Ban; số ban trước tính được=0; thời hạn=30×24h; bắt đầu T; account→BANNED; K81 Mở; Hoa MODERATOR→USER ngay, không khôi phục role khi gỡ/hết hạn | END:SUCCESS | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |


**E17 — thay toàn bộ M1 đến kết thúc:** An Admin yêu cầu vụ nhắm post/comment/account của chính An; lệnh cấm tự xử lý vẫn áp, không mở rộng sang nhóm chưa chốt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-010 E17 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E17.1 | ACT-007 | An yêu cầu ban người vi phạm trong vụ theo quyết định con người đối với vụ của chính mình. | target type=post/comment/account; owner=ADM-AN; không phải nhóm | E17.2 | FR-M08-14.01 |
| E17.2 | SYSTEM | Hệ thống loại vụ khỏi phạm vi nhìn thấy/nhận và từ chối truy cập/xử lý đối tượng của chính An theo nguồn, không cấp quyền nhờ role Admin. | Không trả dữ liệu tố cáo/không áp biện pháp | END:REJECTED | FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |


**E18 — thay toàn bộ M1 đến kết thúc:** Ngay cả Admin không được cảnh cáo/ban Admin khác. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-010 E18 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E18.1 | ACT-007 | An chọn Ban vĩnh viễn Admin khác. | target=ADM-BAO ADMIN | E18.2 | FR-M08-14.01 |
| E18.2 | SYSTEM | Hệ thống từ chối chế tài Admin; không tăng cảnh cáo/tạo ban hoặc thu hồi role. | Admin miễn cảnh cáo/ban | END:REJECTED | FR-M08-10.09, FR-M08-14.10, BR-M08-46, BR-M08-55 |


<!-- sc:end SC-M08-010 -->

<a id="sc-m08-011"></a>

<!-- sc:scenario SC-M08-011 -->

### SC-M08-011

#### 1. Tên kịch bản chuẩn

Gỡ sớm một ban đang hiệu lực — BF-M08-011; owner [UC-M08-012](../../us/US-M08.md#uc-m08-012).

#### 2. Actor thực hiện

ACT-008 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Có tài khoản/bản ghi ban cần gỡ; không đòi giữ vụ. Chuẩn Bình BANNED do B81 Đang hiệu lực, từng là Mod nay USER; Mai là staff.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-011 -->

| result | condition |
|---|---|
| SUCCESS | Ban Đã gỡ, account ACTIVE ngay; log và sự kiện app+email có, lịch sử còn tính; không phục hồi Mod hoặc nội dung. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-011 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai chọn Gỡ ban B81 trực tiếp trên tài khoản Bình. | B81 Đang hiệu lực; Bình BANNED/USER; không có vụ do Mai giữ | M2 | FR-M08-15.01, FR-M08-15.05 |
| M2 | SYSTEM | Hệ thống kiểm staff và B81 còn Đang hiệu lực; chuyển B81 Đã gỡ và account ACTIVE ngay, giữ lịch sử ban để tính leo thang, giữ vai trò USER. Ghi log gỡ và sự kiện app+email, trả kết quả; không khôi phục Mod, không hiện lại nội dung hoặc thay hạn cảnh cáo. | B81→Đã gỡ; Bình→ACTIVE/USER; cảnh cáo và nội dung giữ trạng thái trước | END:SUCCESS | FR-M08-15.01, FR-M08-15.02, FR-M08-15.03, FR-M08-15.04, FR-M08-15.05, FR-M08-16.05, BR-M08-34, BR-M08-38, BR-M08-48, FR-M10-06.02 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-011 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Bản ban không còn Đang hiệu lực | E1.1 | FR-M08-15.03 |
| E2 | system | M1 | ACT-007 — An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E2.1 | FR-M08-15.01, FR-M08-15.05, FR-M08-15.02, FR-M08-15.03, FR-M08-15.04, FR-M08-16.05, BR-M08-34, BR-M08-38, BR-M08-48, FR-M10-06.02 |
| E3 | system | M1 | ACT-002 — User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E3.1 | FR-M08-15.01, FR-M08-15.05, FR-M08-15.02, FR-M08-15.03, FR-M08-15.04, FR-M08-16.05, BR-M08-34, BR-M08-38, BR-M08-48, FR-M10-06.02, BR-M08-44 |
| E4 | system | M1 | ACT-001 — Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M08-15.01, FR-M08-15.05, FR-M08-15.02, FR-M08-15.03, FR-M08-15.04, FR-M08-16.05, BR-M08-34, BR-M08-38, BR-M08-48, FR-M10-06.02, BR-M08-44 |


<!-- sc:branch SC-M08-011 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối gỡ ban không hiệu lực, không ghi một lần gỡ thành công mới. | B81 Hết hạn, Đã gỡ hoặc Bị lật; kiểm đúng bản ban được chọn | END:REJECTED | FR-M08-15.03 |


**E2 — thay toàn bộ M1 đến kết thúc:** An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-011 E2 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E2.1 | ACT-007 | An chọn Gỡ ban B81 trực tiếp trên tài khoản Bình. | B81 Đang hiệu lực; Bình BANNED/USER; không có vụ do An giữ | E2.2 | FR-M08-15.01, FR-M08-15.05 |
| E2.2 | SYSTEM | Hệ thống kiểm staff và B81 còn Đang hiệu lực; chuyển B81 Đã gỡ và account ACTIVE ngay, giữ lịch sử ban để tính leo thang, giữ vai trò USER. Ghi log gỡ và sự kiện app+email, trả kết quả; không khôi phục Mod, không hiện lại nội dung hoặc thay hạn cảnh cáo. | B81→Đã gỡ; Bình→ACTIVE/USER; cảnh cáo và nội dung giữ trạng thái trước | END:SUCCESS | FR-M08-15.01, FR-M08-15.02, FR-M08-15.03, FR-M08-15.04, FR-M08-15.05, FR-M08-16.05, BR-M08-34, BR-M08-38, BR-M08-48, FR-M10-06.02 |


**E3 — thay toàn bộ M1 đến kết thúc:** User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-011 E3 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E3.1 | ACT-002 | Người yêu cầu chọn gỡ sớm một ban đang hiệu lực. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E3.2 | FR-M08-15.01, FR-M08-15.05 |
| E3.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-15.01, FR-M08-15.02, FR-M08-15.03, FR-M08-15.04, FR-M08-15.05, FR-M08-16.05, BR-M08-34, BR-M08-38, BR-M08-48, FR-M10-06.02, BR-M08-44 |


**E4 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-011 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-001 | Người yêu cầu chọn gỡ sớm một ban đang hiệu lực. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E4.2 | FR-M08-15.01, FR-M08-15.05 |
| E4.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-15.01, FR-M08-15.02, FR-M08-15.03, FR-M08-15.04, FR-M08-15.05, FR-M08-16.05, BR-M08-34, BR-M08-38, BR-M08-48, FR-M10-06.02, BR-M08-44 |


<!-- sc:end SC-M08-011 -->

<a id="sc-m08-012"></a>

<!-- sc:scenario SC-M08-012 -->

### SC-M08-012

#### 1. Tên kịch bản chuẩn

Xem mức cảnh cáo và hạn thử thách được phép — BF-M08-012; owner [UC-M08-013](../../us/US-M08.md#uc-m08-013).

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Có yêu cầu xem; danh tính/phạm vi được kiểm. Chuẩn Lan có phiên, xem dữ liệu riêng của mình hiện MEDIUM; không cần giữ vụ.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-012 -->

| result | condition |
|---|---|
| SUCCESS | Mức và hạn hiện tại được trả đúng chủ thể/quyền riêng tư; không cập nhật mức từ một thao tác đọc, không hiển thị công khai. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-012 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan mở thông tin mức cảnh cáo và thử thách của mình. | target=U-LAN; số lần 3/MEDIUM; hạn 19/11/2026 10:00+07 | M2 | FR-M08-13.01 |
| M2 | SYSTEM | Hệ thống xác nhận chính chủ, trả mức hiện tại và thời điểm kết thúc thử thách theo giờ Việt Nam, các hạn chế tương ứng. Không công khai mức trên bài, bình luận hoặc hồ sơ cho người khác; MEDIUM không tạo bài mới, vẫn bình luận, feed không bị hạ vì mức cảnh cáo. | Lan MEDIUM; hạn 19/11 10:00+07; chỉ Lan và staff đủ quyền được xem | END:SUCCESS | FR-M08-13.01, FR-M08-13.02, FR-M08-13.03, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-43 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-012 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Lan yêu cầu mức cảnh cáo người khác | E1.1 | FR-M08-13.02, FR-M08-13.03, BR-M08-32 |
| E2 | system | M2 | Mức hiện tại là HEAVY | E2.1 | FR-M08-13.01, FR-M08-13.02, FR-M08-13.03, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-43 |
| E3 | system | M2 | Không còn cảnh cáo hiện hành | E3.1 | FR-M08-13.01, BR-M08-28, BR-M08-30, BR-M08-32 |
| E4 | system | M1 | ACT-001 — Guest yêu cầu chức năng cần tài khoản. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M08-13.01, FR-M08-13.02, BR-M08-01, BR-M08-32 |
| E5 | system | M1 | ACT-008 — Mod Mai xem mức của người dùng Bình theo quyền staff, không coi là dữ liệu công khai. Actor khởi tạo ACT-008; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M08-04.05, FR-M08-13.02, FR-M08-13.03, BR-M08-32 |
| E6 | system | M1 | ACT-007 — Admin An xem mức của người dùng Bình theo quyền staff, không coi là dữ liệu công khai. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M08-04.05, FR-M08-13.02, FR-M08-13.03, BR-M08-32 |


<!-- sc:branch SC-M08-012 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối trả mức/hạn người khác cho User, kể cả xem hồ sơ/bài/bình luận. | actor U-LAN; target U-BINH | END:REJECTED | FR-M08-13.02, FR-M08-13.03, BR-M08-32 |


<!-- sc:branch SC-M08-012 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống xác nhận chính chủ và trả HEAVY/hạn hiện tại. Không tạo bài/bình luận mới; vẫn sửa/xóa nội dung cũ theo owner, vote, báo cáo; search Liên quan nhân 0.5 và loại BXH công khai, không hạ feed chỉ vì HEAVY. | Lan 5/HEAVY; hạn 24/11 10:00+07; riêng tư | END:SUCCESS | FR-M08-13.01, FR-M08-13.02, FR-M08-13.03, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-43 |


<!-- sc:branch SC-M08-012 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống xác nhận chính chủ rồi trả mức Sạch theo số lần hiện hành 0, không tạo hạn thử thách mới từ thao tác xem. | Lan 0/Sạch; không suy xóa record cảnh cáo lịch sử | END:SUCCESS | FR-M08-13.01, BR-M08-28, BR-M08-30, BR-M08-32 |


**E4 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng cần tài khoản. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-012 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-001 | Guest chọn xem mức cảnh cáo và hạn thử thách được phép. | Không có phiên; chưa phát sinh dữ liệu nghiệp vụ | E4.2 | FR-M08-13.01 |
| E4.2 | SYSTEM | Hệ thống từ chối chức năng yêu cầu người dùng đã đăng nhập; không lưu báo cáo hoặc trả mức cảnh cáo riêng tư. | Không tạo báo cáo/quan hệ quyền từ ID | END:REJECTED | FR-M08-13.01, FR-M08-13.02, BR-M08-01, BR-M08-32 |


**E5 — thay toàn bộ M1 đến kết thúc:** Mod Mai xem mức của người dùng Bình theo quyền staff, không coi là dữ liệu công khai. Actor khởi tạo ACT-008; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-012 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-008 | Mod Mai yêu cầu xem mức cảnh cáo/hạn thử thách của Bình. | target U-BINH USER; MEDIUM, hạn 19/11 10:00+07 | E5.2 | FR-M08-04.05, FR-M08-13.02 |
| E5.2 | SYSTEM | Hệ thống kiểm staff/phạm vi được phép, trả MEDIUM và hạn hiện tại của Bình chỉ cho staff; không công khai lên bài, bình luận/hồ sơ hoặc thay mức. | Bình MEDIUM; hạn 19/11 10:00+07; dữ liệu không thuộc actor đang xem | END:SUCCESS | FR-M08-04.05, FR-M08-13.02, FR-M08-13.03, BR-M08-32 |


**E6 — thay toàn bộ M1 đến kết thúc:** Admin An xem mức của người dùng Bình theo quyền staff, không coi là dữ liệu công khai. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-012 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-007 | Admin An yêu cầu xem mức cảnh cáo/hạn thử thách của Bình. | target U-BINH USER; MEDIUM, hạn 19/11 10:00+07 | E6.2 | FR-M08-04.05, FR-M08-13.02 |
| E6.2 | SYSTEM | Hệ thống kiểm staff/phạm vi được phép, trả MEDIUM và hạn hiện tại của Bình chỉ cho staff; không công khai lên bài, bình luận/hồ sơ hoặc thay mức. | Bình MEDIUM; hạn 19/11 10:00+07; dữ liệu không thuộc actor đang xem | END:SUCCESS | FR-M08-04.05, FR-M08-13.02, FR-M08-13.03, BR-M08-32 |


<!-- sc:end SC-M08-012 -->

<a id="sc-m08-013"></a>

<!-- sc:scenario SC-M08-013 -->

### SC-M08-013

#### 1. Tên kịch bản chuẩn

Ẩn nhóm vi phạm và toàn bộ nội dung của nhóm — BF-M08-013; owner [UC-M08-015](../../us/US-M08.md#uc-m08-015).

#### 2. Actor thực hiện

ACT-008 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Nhóm/vụ được nhận diện; chuẩn G81 Bình thường, Owner Bình USER khác Mai, K81 Mở do Mai giữ. Không suy chính sách tự xử lý nhóm của staff từ quy tắc tự nhắm post/comment/account (GAP004).

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-013 -->

| result | condition |
|---|---|
| SUCCESS | G81 Bị ẩn và toàn bộ nội dung không ai nhìn thấy, dữ liệu/log giữ, không có bỏ ẩn. Vụ Mở chờ kết luận, Owner chưa tự nhận cảnh cáo/ban. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-013 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai chọn Ẩn nhóm G81 trong K81. | G81 Bình thường; lý do=Nội dung người lớn đã xác định | M2 | FR-M08-18.01 |
| M2 | SYSTEM | Hệ thống kiểm staff/phạm vi/còn giữ vụ nhóm và trạng thái cho phép; chuyển nhóm Bị ẩn, ẩn nhóm và toàn bộ nội dung với mọi người kể cả Owner/thành viên, giữ dữ liệu và không có bỏ ẩn. Ghi log và trả biện pháp đã áp; không tự cảnh cáo/ban Owner hoặc đóng vụ. | G81 Bình thường→Bị ẩn; K81 Mở do Mai giữ; Owner Bình USER, Mai khác Owner | END:SUCCESS | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-013 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Nhóm đang Bị khóa, đây là vụ báo cáo sau | E1.1 | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.08, BR-M08-50 |
| E2 | system | M2 | Nhóm đã Bị ẩn | E2.1 | FR-M08-18.09, BR-M08-50 |
| E3 | system | M2 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | E3.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |
| E4 | user-choice | M2 | Quyền giữ đã tự nhả sau đủ 30 phút không hoạt động; K81 vẫn Mở/chưa ai nhận, Mai còn đủ phạm vi và chọn nhận lại | E4.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-16.07, FR-M08-03.01, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-18.01 |
| E5 | system | M1 | ACT-007 — An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |
| E6 | system | M1 | ACT-002 — User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |
| E7 | system | M1 | ACT-001 — Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |


<!-- sc:branch SC-M08-013 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm quyền giữ K81/vụ sau và trạng thái, cho Ẩn G81 đang Bị khóa; chuyển Bị ẩn, ẩn mọi nội dung với mọi người kể cả Owner/thành viên, giữ dữ liệu/log và trả đã ẩn. Không có bỏ ẩn, không đóng vụ hoặc tự phạt Owner. | G81 Bị khóa→Bị ẩn; K81 là vụ sau, Mở do Mai giữ | END:SUCCESS | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.08, BR-M08-50 |


<!-- sc:branch SC-M08-013 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối ẩn lại hoặc khóa nhóm Bị ẩn; giữ trạng thái Bị ẩn, không cung cấp bỏ ẩn. | G81 Bị ẩn | END:REJECTED | FR-M08-18.09, BR-M08-50 |


<!-- sc:branch SC-M08-013 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống kiểm hiện tại và từ chối tác động ngoài vụ đang giữ; không áp biện pháp/kết luận thành công. | K81 holder Hoa hoặc target không thuộc vụ Mai giữ; dữ liệu đã áp trước đó giữ nguyên | END:REJECTED | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |


<!-- sc:branch SC-M08-013 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối yêu cầu theo quyền giữ cũ, cho biết K81 Mở chưa ai giữ; không tự gắn lại Mai hoặc ghi log tự nhả. | lastActivity=T−30 phút; người khác chỉ xem không làm mới mốc; holder=trống | E4.2 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-16.07 |
| E4.2 | ACT-008 | Mai chọn Nhận xử lý lại K81. | K81 còn Mở/chưa ai giữ; Mai đủ quyền | E4.3 | FR-M08-03.01 |
| E4.3 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/trạng thái/chưa giữ, gắn duy nhất Mai giữ K81, trả đã nhận; không log nhận. | holder=Mai; activity=T | E4.4 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-16.07, BR-M08-08 |
| E4.4 | ACT-008 | Mai chọn Ẩn nhóm G81 trong K81. | G81 Bình thường; lý do=Nội dung người lớn đã xác định; quyền vừa nhận lại còn hợp lệ | M2 | FR-M08-18.01 |


**E5 — thay toàn bộ M1 đến kết thúc:** An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-013 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-007 | An chọn Ẩn nhóm G81 trong K81. | G81 Bình thường; lý do=Nội dung người lớn đã xác định | E5.2 | FR-M08-18.01 |
| E5.2 | SYSTEM | Hệ thống kiểm staff/phạm vi/còn giữ vụ nhóm và trạng thái cho phép; chuyển nhóm Bị ẩn, ẩn nhóm và toàn bộ nội dung với mọi người kể cả Owner/thành viên, giữ dữ liệu và không có bỏ ẩn. Ghi log và trả biện pháp đã áp; không tự cảnh cáo/ban Owner hoặc đóng vụ. | G81 Bình thường→Bị ẩn; K81 Mở do An giữ; Owner Bình USER, An khác Owner | END:SUCCESS | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |


**E6 — thay toàn bộ M1 đến kết thúc:** User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-013 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-002 | Người yêu cầu chọn ẩn nhóm vi phạm và toàn bộ nội dung của nhóm. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E6.2 | FR-M08-18.01 |
| E6.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |


**E7 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-013 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-001 | Người yêu cầu chọn ẩn nhóm vi phạm và toàn bộ nội dung của nhóm. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E7.2 | FR-M08-18.01 |
| E7.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |


<!-- sc:end SC-M08-013 -->

<a id="sc-m08-014"></a>

<!-- sc:scenario SC-M08-014 -->

### SC-M08-014

#### 1. Tên kịch bản chuẩn

Khóa hoạt động một nhóm vi phạm — BF-M08-014; owner [UC-M08-015](../../us/US-M08.md#uc-m08-015).

#### 2. Actor thực hiện

ACT-008 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Nhóm/vụ được nhận diện; chuẩn G81 Bình thường, Owner Bình USER khác Mai; K81 Mở do Mai giữ. Khóa là mục tiêu ngăn hoạt động nhưng còn quyền đọc, khác Ẩn làm mất hiển thị.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-014 -->

| result | condition |
|---|---|
| SUCCESS | G81 Bị khóa; mọi hạn chế/ngoại lệ ở D-LOCK có hiệu lực, đọc vẫn theo quyền cũ; log giữ. Không tự đóng vụ, phạt Owner hoặc tạo chức năng bỏ ẩn. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-014 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai chọn Khóa nhóm G81 trong K81. | G81 Bình thường; reason=Vi phạm đã xác định | M2 | FR-M08-18.04 |
| M2 | SYSTEM | Hệ thống kiểm staff/phạm vi/còn giữ vụ nhóm và trạng thái cho phép; chuyển nhóm Bị khóa; vẫn đọc theo Public/Private và giữ bookmark/báo cáo, chặn đầy đủ thao tác tại D-LOCK với mọi người kể cả Owner/Group Mod. Member/Group Mod vẫn tự rời, Owner không tự rời; hệ thống vẫn tự chuyển Owner khi mất quyền ngoài ý muốn. Ghi log và trả biện pháp đã áp; không tự cảnh cáo/ban Owner hoặc đóng vụ. | G81 Bình thường→Bị khóa; K81 Mở do Mai giữ; Owner Bình USER, Mai khác Owner | END:SUCCESS | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-014 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Nhóm đã Bị ẩn | E1.1 | FR-M08-18.09, BR-M08-50 |
| E2 | system | M2 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | E2.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |
| E3 | user-choice | M2 | Quyền giữ đã tự nhả sau đủ 30 phút không hoạt động; K81 vẫn Mở/chưa ai nhận, Mai còn đủ phạm vi và chọn nhận lại | E3.1 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-16.07, FR-M08-03.01, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-18.04 |
| E4 | system | M1 | ACT-007 — An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M08-18.04, FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |
| E5 | system | M1 | ACT-002 — User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M08-18.04, FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |
| E6 | system | M1 | ACT-001 — Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M08-18.04, FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |


<!-- sc:branch SC-M08-014 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối ẩn lại hoặc khóa nhóm Bị ẩn; giữ trạng thái Bị ẩn, không cung cấp bỏ ẩn. | G81 Bị ẩn | END:REJECTED | FR-M08-18.09, BR-M08-50 |


<!-- sc:branch SC-M08-014 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống kiểm hiện tại và từ chối tác động ngoài vụ đang giữ; không áp biện pháp/kết luận thành công. | K81 holder Hoa hoặc target không thuộc vụ Mai giữ; dữ liệu đã áp trước đó giữ nguyên | END:REJECTED | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48 |


<!-- sc:branch SC-M08-014 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối yêu cầu theo quyền giữ cũ, cho biết K81 Mở chưa ai giữ; không tự gắn lại Mai hoặc ghi log tự nhả. | lastActivity=T−30 phút; người khác chỉ xem không làm mới mốc; holder=trống | E3.2 | FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, FR-M08-16.07 |
| E3.2 | ACT-008 | Mai chọn Nhận xử lý lại K81. | K81 còn Mở/chưa ai giữ; Mai đủ quyền | E3.3 | FR-M08-03.01 |
| E3.3 | SYSTEM | Hệ thống kiểm lại staff/phạm vi/trạng thái/chưa giữ, gắn duy nhất Mai giữ K81, trả đã nhận; không log nhận. | holder=Mai; activity=T | E3.4 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-16.07, BR-M08-08 |
| E3.4 | ACT-008 | Mai chọn Khóa nhóm G81 trong K81. | G81 Bình thường; reason=Vi phạm đã xác định; quyền vừa nhận lại còn hợp lệ | M2 | FR-M08-18.04 |


**E4 — thay toàn bộ M1 đến kết thúc:** An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-014 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-007 | An chọn Khóa nhóm G81 trong K81. | G81 Bình thường; reason=Vi phạm đã xác định | E4.2 | FR-M08-18.04 |
| E4.2 | SYSTEM | Hệ thống kiểm staff/phạm vi/còn giữ vụ nhóm và trạng thái cho phép; chuyển nhóm Bị khóa; vẫn đọc theo Public/Private và giữ bookmark/báo cáo, chặn đầy đủ thao tác tại D-LOCK với mọi người kể cả Owner/Group Mod. Member/Group Mod vẫn tự rời, Owner không tự rời; hệ thống vẫn tự chuyển Owner khi mất quyền ngoài ý muốn. Ghi log và trả biện pháp đã áp; không tự cảnh cáo/ban Owner hoặc đóng vụ. | G81 Bình thường→Bị khóa; K81 Mở do An giữ; Owner Bình USER, An khác Owner | END:SUCCESS | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |


**E5 — thay toàn bộ M1 đến kết thúc:** User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-014 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-002 | Người yêu cầu chọn khóa hoạt động một nhóm vi phạm. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E5.2 | FR-M08-18.04 |
| E5.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |


**E6 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-014 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-001 | Người yêu cầu chọn khóa hoạt động một nhóm vi phạm. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E6.2 | FR-M08-18.04 |
| E6.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |


<!-- sc:end SC-M08-014 -->

<a id="sc-m08-015"></a>

<!-- sc:scenario SC-M08-015 -->

### SC-M08-015

#### 1. Tên kịch bản chuẩn

Mở khóa nhóm để hoạt động theo quyền thông thường — BF-M08-015; owner [UC-M08-016](../../us/US-M08.md#uc-m08-016).

#### 2. Actor thực hiện

ACT-008 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Có nhóm cần mở khóa; không đòi vụ đang giữ. Chuẩn G81 Bị khóa, Mai là Mod; kiểm trạng thái và vai trò khi xử lý.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-015 -->

| result | condition |
|---|---|
| SUCCESS | G81 Bình thường, hoạt động được phép lại trong phạm vi quyền M11; log có. Không đòi giữ vụ hoặc phục hồi nhóm đã Bị ẩn. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-015 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai chọn Mở khóa G81 trực tiếp. | G81 Bị khóa; không có vụ do Mai giữ | M2 | FR-M08-18.07 |
| M2 | SYSTEM | Hệ thống kiểm staff và G81 Bị khóa, chuyển Bình thường; cho lại các thao tác bị chặn bởi khóa theo quyền thông thường M11 và ghi log mở khóa, trả kết quả. Không cấp quyền Private/thành viên mới, xóa vụ cũ hoặc bỏ ẩn nhóm. | G81 Bị khóa→Bình thường; vẫn Public/Private và phân quyền như trước; K81 cũ không thay | END:SUCCESS | FR-M08-18.07, FR-M08-18.09, FR-M08-18.10, FR-M08-16.05, BR-M08-48, BR-M08-50, BR-M11-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-015 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Nhóm Bị ẩn thay vì Bị khóa | E1.1 | FR-M08-18.09, BR-M08-50 |
| E2 | system | M1 | ACT-007 — An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E2.1 | FR-M08-18.07, FR-M08-18.09, FR-M08-18.10, FR-M08-16.05, BR-M08-48, BR-M08-50, BR-M11-28 |
| E3 | system | M1 | ACT-002 — User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E3.1 | FR-M08-18.07, FR-M08-18.09, FR-M08-18.10, FR-M08-16.05, BR-M08-48, BR-M08-50, BR-M11-28, BR-M08-44 |
| E4 | system | M1 | ACT-001 — Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M08-18.07, FR-M08-18.09, FR-M08-18.10, FR-M08-16.05, BR-M08-48, BR-M08-50, BR-M11-28, BR-M08-44 |


<!-- sc:branch SC-M08-015 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối mở khóa nhóm Bị ẩn, không biến mở khóa thành bỏ ẩn. | G81 Bị ẩn | END:REJECTED | FR-M08-18.09, BR-M08-50 |


**E2 — thay toàn bộ M1 đến kết thúc:** An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-015 E2 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E2.1 | ACT-007 | An chọn Mở khóa G81 trực tiếp. | G81 Bị khóa; không có vụ do An giữ | E2.2 | FR-M08-18.07 |
| E2.2 | SYSTEM | Hệ thống kiểm staff và G81 Bị khóa, chuyển Bình thường; cho lại các thao tác bị chặn bởi khóa theo quyền thông thường M11 và ghi log mở khóa, trả kết quả. Không cấp quyền Private/thành viên mới, xóa vụ cũ hoặc bỏ ẩn nhóm. | G81 Bị khóa→Bình thường; vẫn Public/Private và phân quyền như trước; K81 cũ không thay | END:SUCCESS | FR-M08-18.07, FR-M08-18.09, FR-M08-18.10, FR-M08-16.05, BR-M08-48, BR-M08-50, BR-M11-28 |


**E3 — thay toàn bộ M1 đến kết thúc:** User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-015 E3 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E3.1 | ACT-002 | Người yêu cầu chọn mở khóa nhóm để hoạt động theo quyền thông thường. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E3.2 | FR-M08-18.07 |
| E3.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-18.07, FR-M08-18.09, FR-M08-18.10, FR-M08-16.05, BR-M08-48, BR-M08-50, BR-M11-28, BR-M08-44 |


**E4 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-015 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-001 | Người yêu cầu chọn mở khóa nhóm để hoạt động theo quyền thông thường. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E4.2 | FR-M08-18.07 |
| E4.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-18.07, FR-M08-18.09, FR-M08-18.10, FR-M08-16.05, BR-M08-48, BR-M08-50, BR-M11-28, BR-M08-44 |


<!-- sc:end SC-M08-015 -->

<a id="sc-m08-016"></a>

<!-- sc:scenario SC-M08-016 -->

### SC-M08-016

#### 1. Tên kịch bản chuẩn

Tra cứu nhật ký kiểm duyệt trong phạm vi được phép — BF-M08-016; owner [UC-M08-025](../../us/US-M08.md#uc-m08-025).

#### 2. Actor thực hiện

ACT-008 là actor chính. ACT-007 kế thừa ACT-008 kế thừa ACT-002, vẫn theo quyền target/caller; đường E tại M1 ghi toàn bộ khi actor khởi tạo khác. ACT-001 chỉ có đường từ chối; ACT-006 hỗ trợ quét nền, không ra lệnh ban hoặc giữ vụ. Group Mod/Owner không đồng nghĩa Mod hệ thống.

#### 3. Tiền điều kiện

Có yêu cầu tra cứu; vai trò/phạm vi nhật ký được kiểm trước trả dữ liệu. Chuẩn Mai Mod xem vụ mình đã xử lý, không có quyền mọi log hoặc mọi vụ do từng mở xem/nhận.

#### 4. Hậu điều kiện

<!-- sc:post SC-M08-016 -->

| result | condition |
|---|---|
| SUCCESS | Tập và dòng nhật ký đúng phạm vi được trả chỉ đọc; Admin có phạm vi toàn bộ/lọc actor, Mod chỉ vụ mình xử lý hoặc đúng một thao tác của khiếu nại đang được mình xét. Không sửa/xóa log hoặc suy quyền từ link. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không tạo hiệu ứng thành công cho yêu cầu đó. Dữ liệu và các biện pháp hợp lệ đã thực hiện trước điểm rẽ được giữ; không ngầm rollback, đóng vụ hoặc khôi phục nội dung/vai trò. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M08-016 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai mở nhật ký kiểm duyệt để tra các vụ mình đã xử lý. | actor=MOD-MAI; K80 đã xử lý bởi Mai; K79 do Hoa xử lý | M2 | FR-M08-17.02 |
| M2 | SYSTEM | Hệ thống xác định phạm vi Mod: chỉ các vụ mình đã xử lý, rồi trả các dòng được phép với người làm/loại/target/lý do/thời điểm. Giữ log vĩnh viễn, bất biến; không cho đọc K79 của Hoa nếu không đúng ngoại lệ khiếu nại. Không ghi nhận/tự nhả vụ thành log. | K80: Mai/ẩn P80/Quấy rối/T−1h và Mai/kết luận Có xử lý/T−50phút; K79 không trả | M3 | FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, FR-M08-17.01, FR-M08-17.02, FR-M08-17.03, FR-M08-17.04, FR-M08-17.05, FR-M08-17.06, BR-M08-39, BR-M08-40, BR-M08-41 |
| M3 | ACT-008 | Mai chọn dòng kết luận K80 để tra chi tiết. | Dòng thuộc phạm vi vụ Mai đã xử lý, không sửa/xóa | M4 | FR-M08-17.02 |
| M4 | SYSTEM | Hệ thống kiểm lại phạm vi của dòng rồi trả chi tiết nhật ký chỉ đọc, theo giờ Việt Nam; không mở rộng quyền sang nhật ký người khác hoặc bản nội dung lưu giữ ngoài ngữ cảnh. | actor/operation/target/reason/time của chính dòng; không thay log | END:SUCCESS | FR-M08-16.01, FR-M08-16.03, FR-M08-16.04, FR-M08-16.06, FR-M08-17.02, FR-M08-17.04, BR-M08-39, BR-M08-40, BR-M08-41, BR-M08-43 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước ấy đã hoàn tất. Dữ liệu/guard nhánh thay snapshot chuẩn cho lần chạy này. E tại M1 thay toàn bộ đường theo actor khác, không đổi actor giữa chừng. Không tự thêm nút xác nhận/hủy, retry AI/email hoặc rollback ngoài nguồn. Điểm thiếu hợp đồng ghi GAP tại mục 7, không biến thành phản ứng sản phẩm do agent đặt.

<!-- sc:exceptions SC-M08-016 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M4 | Mod đòi dòng thao tác Mod khác, không đang xét khiếu nại về thao tác ấy | E1.1 | FR-M08-17.03, FR-M08-17.04, BR-M08-41 |
| E2 | user-choice | M1 | Mai đang xét khiếu nại M09 về đúng thao tác của Mod khác | E2.1 | FR-M08-17.03, FR-M08-17.04, FR-M08-16.01, FR-M08-16.03, FR-M08-16.04, FR-M08-16.06, BR-M08-40, BR-M08-41 |
| E3 | system | M1 | ACT-007 — An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E3.1 | FR-M08-17.02, FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, FR-M08-17.01, FR-M08-17.03, FR-M08-17.04, FR-M08-17.05, FR-M08-17.06, BR-M08-39, BR-M08-40, BR-M08-41, BR-M08-43 |
| E4 | system | M1 | ACT-002 — User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M08-17.02, FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, FR-M08-17.01, FR-M08-17.03, FR-M08-17.04, FR-M08-17.05, FR-M08-17.06, BR-M08-39, BR-M08-40, BR-M08-41, BR-M08-44 |
| E5 | system | M1 | ACT-001 — Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M08-17.02, FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, FR-M08-17.01, FR-M08-17.03, FR-M08-17.04, FR-M08-17.05, FR-M08-17.06, BR-M08-39, BR-M08-40, BR-M08-41, BR-M08-44 |
| E6 | system | M1 | ACT-007 — An Admin tra toàn bộ nhật ký và lọc theo người làm, kể cả người đã xóa. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M08-17.01, FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, BR-M08-39, BR-M08-40, BR-M08-41, FR-M08-17.06 |


<!-- sc:branch SC-M08-016 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối trả dòng vượt phạm vi, không coi biết link/ID hoặc từng nhận vụ là được xem. | K79 operation do Hoa làm; không có appeal hiện tại của Mai | END:REJECTED | FR-M08-17.03, FR-M08-17.04, BR-M08-41 |


<!-- sc:branch SC-M08-016 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-008 | Mai từ khiếu nại A81 đang xét yêu cầu nhật ký thao tác bị khiếu nại. | A81 currently reviewed by Mai; operation=OP-HOA-81, actor Hoa | E2.2 | FR-M08-17.03 |
| E2.2 | SYSTEM | Hệ thống kiểm staff và quan hệ hiện tại giữa người xét, khiếu nại và đúng thao tác; trả riêng OP-HOA-81 chỉ đọc với dữ liệu đầy đủ. Không mở mọi log của Hoa hoặc xử lý khiếu nại thay M09. | Chỉ OP-HOA-81; không cho OP-HOA-82; không sửa/xóa dòng | END:SUCCESS | FR-M08-17.03, FR-M08-17.04, FR-M08-16.01, FR-M08-16.03, FR-M08-16.04, FR-M08-16.06, BR-M08-40, BR-M08-41 |


**E3 — thay toàn bộ M1 đến kết thúc:** An là Admin hệ thống, khác target USER/Owner, thay toàn bộ hành trình và người giữ/người làm Mai bằng An; mọi guard của chức năng còn áp dụng. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-016 E3 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E3.1 | ACT-007 | An mở nhật ký kiểm duyệt để tra các vụ mình đã xử lý. | actor=ADM-AN; K80 đã xử lý bởi An; K79 do Hoa xử lý | E3.2 | FR-M08-17.02 |
| E3.2 | SYSTEM | Hệ thống xác định phạm vi Mod: chỉ các vụ mình đã xử lý, rồi trả các dòng được phép với người làm/loại/target/lý do/thời điểm. Giữ log vĩnh viễn, bất biến; không cho đọc K79 của Hoa nếu không đúng ngoại lệ khiếu nại. Không ghi nhận/tự nhả vụ thành log. | K80: An/ẩn P80/Quấy rối/T−1h và An/kết luận Có xử lý/T−50phút; K79 không trả | E3.3 | FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, FR-M08-17.01, FR-M08-17.02, FR-M08-17.03, FR-M08-17.04, FR-M08-17.05, FR-M08-17.06, BR-M08-39, BR-M08-40, BR-M08-41 |
| E3.3 | ACT-007 | An chọn dòng kết luận K80 để tra chi tiết. | Dòng thuộc phạm vi vụ An đã xử lý, không sửa/xóa | E3.4 | FR-M08-17.02 |
| E3.4 | SYSTEM | Hệ thống kiểm lại phạm vi của dòng rồi trả chi tiết nhật ký chỉ đọc, theo giờ Việt Nam; không mở rộng quyền sang nhật ký người khác hoặc bản nội dung lưu giữ ngoài ngữ cảnh. | actor/operation/target/reason/time của chính dòng; không thay log | END:SUCCESS | FR-M08-16.01, FR-M08-16.03, FR-M08-16.04, FR-M08-16.06, FR-M08-17.02, FR-M08-17.04, BR-M08-39, BR-M08-40, BR-M08-41, BR-M08-43 |


**E4 — thay toàn bộ M1 đến kết thúc:** User chỉ có quyền cá nhân, kể cả Owner/Group Mod nhưng không là staff hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-016 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-002 | Người yêu cầu chọn tra cứu nhật ký kiểm duyệt trong phạm vi được phép. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E4.2 | FR-M08-17.02 |
| E4.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, FR-M08-17.01, FR-M08-17.02, FR-M08-17.03, FR-M08-17.04, FR-M08-17.05, FR-M08-17.06, BR-M08-39, BR-M08-40, BR-M08-41, BR-M08-44 |


**E5 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-016 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-001 | Người yêu cầu chọn tra cứu nhật ký kiểm duyệt trong phạm vi được phép. | Không có vai trò staff hệ thống; không có quyền từ việc biết ID/link | E5.2 | FR-M08-17.02 |
| E5.2 | SYSTEM | Hệ thống kiểm vai trò và từ chối chức năng staff; không trả dữ liệu điều tra/nhật ký hoặc thay dữ liệu quản trị. | Vai trò không phải ACT-008/ACT-007; không ghi thành công | END:REJECTED | FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, FR-M08-17.01, FR-M08-17.02, FR-M08-17.03, FR-M08-17.04, FR-M08-17.05, FR-M08-17.06, BR-M08-39, BR-M08-40, BR-M08-41, BR-M08-44 |


**E6 — thay toàn bộ M1 đến kết thúc:** An Admin tra toàn bộ nhật ký và lọc theo người làm, kể cả người đã xóa. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M08-016 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-007 | An mở nhật ký kiểm duyệt toàn bộ. | actor An ADMIN; nguồn có log Mai/Hoa/AI và người DELETED | E6.2 | FR-M08-17.01 |
| E6.2 | SYSTEM | Hệ thống kiểm Admin, trả tập log của tất cả người làm với đầy đủ loại/target/lý do/thời điểm, chỉ đọc; không phải tập vụ An từng xử lý. | Gồm log M05 đổi Topic/Tag, vô hiệu/kích hoạt Tag; không log nhận/tự nhả | E6.3 | FR-M08-17.01, FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, BR-M08-39, BR-M08-40, BR-M08-41 |
| E6.3 | ACT-007 | An lọc nhật ký theo username người làm đã xóa và chọn một dòng. | username=mod_cu; người làm đã DELETED | E6.4 | FR-M08-17.06, FR-M08-16.04 |
| E6.4 | SYSTEM | Hệ thống xác nhận phạm vi Admin, lọc đúng actor theo username và trả dòng chi tiết; tên hiển thị [Người dùng đã xóa], giữ lý do/target/thời điểm và tính bất biến. | Không xóa lịch sử vì actor DELETED; không sửa log | END:SUCCESS | FR-M08-17.01, FR-M08-17.06, FR-M08-16.03, FR-M08-16.04, FR-M08-16.06, BR-M08-40, BR-M08-41 |


<!-- sc:end SC-M08-016 -->

## 5. Hành vi nền và ràng buộc xuyên UC

| ID | Trigger/điều kiện | Hiệu ứng/ngoại lệ/ranh giới | sources |
|---|---|---|---|
| AUT-M08-001 | Vụ Mở được giữ, đủ 30 phút từ mở xem/ẩn/cảnh cáo/ban/kết luận hợp lệ cuối của chính người giữ | Tự nhả thành Mở chưa giữ, không đóng vụ/ghi log nhận hoặc tự nhả; người khác xem không reset mốc. Không có nút nhả thủ công hoặc hạn xử lý toàn vụ. | FR-M08-03.04, FR-M08-03.08, FR-M08-16.07, BR-M08-09 |
| AUT-M08-002 | Hai cờ AI tổng và Moderation bật; luồng đạt ngưỡng tạm 10 trả lời trong cửa sổ trượt 5 phút | Chỉ đếm reply, không gốc; quét gốc + mọi reply chưa quét bản nội dung hiện tại, bỏ Admin. Đăng/sửa không tự kích hoạt quét; sửa đợi lần kích hoạt tới. Qua M13 lấy max 4 điểm; ≥0.9 ẩn comment ngay, không hàng chờ nội dung, trừ điểm ngay theo M12; 0.5–<0.9 ẩn + mục AI vào vụ, chỉ trừ điểm khi staff xác định vi phạm; <0.5 giữ nguyên kể cả vốn ẩn. Đánh dấu bản hiện tại đã quét khi thành công. AI lỗi sau 1 retry (2 lần tổng) giữ trạng thái, log lỗi cho Admin, không đánh dấu thành công; một cờ tắt không quét. AI ẩn báo app đúng câu Bình luận của bạn đã bị ẩn. | FR-M08-08.01, FR-M08-08.02, FR-M08-08.03, FR-M08-08.04, FR-M08-08.05, FR-M08-08.06, FR-M08-08.07, FR-M08-08.08, FR-M08-08.09, FR-M08-08.10, FR-M08-08.11, FR-M08-08.12, BR-M08-20, BR-M08-21, BR-M08-22, BR-M08-25, BR-M08-26, BR-M08-27, BR-M08-51, BR-M08-55, FR-M13-02.03, FR-M13-02.06, FR-M13-08.09, FR-M12-02.20, FR-M12-02.21 |
| AUT-M08-003 | Kết quả quét post M03 hoặc comment, hai cờ cùng bật | <0.5 không cảnh cáo; trung bình không tự cảnh cáo. ≥0.9: User chưa HEAVY mỗi nội dung một cảnh cáo, cập nhật số/mức/hạn, log và app có khiếu nại. Mod không tự cảnh cáo, đưa vụ cho Admin; Admin không quét/không cảnh cáo; đã HEAVY không thêm cảnh cáo mà yêu cầu ban. Hai nhánh nội dung/chế tài độc lập; không AI ban. Nhiều nội dung vẫn mỗi nội dung một cảnh cáo nếu đủ điều kiện, thứ tự qua biên HEAVY chưa chốt (GAP003). Post AI từ chối+cảnh cáo dùng thông báo gộp do M09 sở hữu. | FR-M08-09.01, FR-M08-09.02, FR-M08-09.03, FR-M08-09.04, FR-M08-09.05, FR-M08-09.06, FR-M08-09.07, FR-M08-09.08, FR-M08-09.09, FR-M08-09.10, FR-M08-09.11, FR-M08-09.12, BR-M08-23, BR-M08-24, BR-M08-26, BR-M08-28, BR-M08-29, BR-M08-33, BR-M08-36, BR-M08-46, BR-M08-55, FR-M09-01.19 |
| AUT-M08-004 | Post gắn cờ sau quét lại; comment trung bình; Mod ≥0.9; HEAVY vi phạm tiếp do AI hoặc staff xác định | Sự việc do AI có reporter dữ liệu Hệ thống (AI), lý do nhóm cao nhất, tính 1 báo cáo; ghép đúng vụ Mở hoặc tạo mới, tính ưu tiên. HEAVY đánh dấu yêu cầu ban trên vụ nội dung hoặc mở vụ khi chưa có; staff xác định không tự thêm mục AI. Không hàng chờ AI/ban riêng, không mở lại vụ đóng/không tự ban, không tự đặt dedup AI theo quota người dùng. | FR-M08-07.09, FR-M08-08.05, FR-M08-09.08, FR-M08-09.11, FR-M08-14.11, BR-M08-05, BR-M08-06, BR-M08-36, BR-M08-49, BR-M08-51 |
| AUT-M08-005 | Đến hạn thử thách hiện hành, kể cả đang ban và không phụ thuộc cờ AI | HEAVY→MEDIUM, số lần 4, hạn mới +10×24h; MEDIUM→LIGHT, 2, +7×24h; LIGHT→Sạch, 0. Mốc giảm là mốc bắt đầu thử thách mới, áp hạn chế mới ngay; không làm tròn ngày lịch, không xóa record lịch sử/hiện lại nội dung, không tự gỡ ban. | FR-M08-12.01, FR-M08-12.02, FR-M08-12.03, FR-M08-12.04, FR-M08-12.05, BR-M08-29, BR-M08-30, BR-M08-31, BR-M08-43 |
| AUT-M08-006 | Cảnh cáo/bỏ AI, ban/gỡ ban, ẩn nội dung, kết luận, ẩn-khóa-mở khóa nhóm, thao tác Tag/Topic M05 được liệt kê | Ghi người làm Mod/Admin/AI, loại, target, lý do, thời điểm; giữ vĩnh viễn, không sửa/xóa. M05: vô hiệu/kích hoạt Tag, đổi Topic/Tag bài người khác; Admin còn log Admin M10. Actor DELETED hiện [Người dùng đã xóa], vẫn tra username. Không log nhận/tự nhả vụ; log AI thô của M13 khác nhật ký kiểm duyệt; không chốt giao dịch/rollback. | FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, BR-M08-39, BR-M08-40, FR-M01-12.10, FR-M10-14.03 |
| AUT-M08-007 | Kết luận vụ, AI ẩn comment, cảnh cáo, ban hoặc gỡ ban | Reporter người dùng cùng kết quả chung, không biết mức xử lý; AI reporter không nhận. Chỉ Có xử lý gửi target/Owner chi tiết, giấu reporter/lý do/mô tả/ảnh tố cáo. App cảnh cáo có khiếu nại; ban app+email có khiếu nại; gỡ ban app+email; AI ẩn comment app. Bài ẩn có khiếu nại, comment/nhóm ẩn-khóa không có. M07 sở hữu lưu/đẩy/email, không bảo đảm mọi thiết bị đã nhận; câu kết quả chung cuối theo thiết kế. | FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.10, FR-M08-05.11, FR-M08-08.07, FR-M08-09.05, FR-M08-10.03, FR-M08-14.04, FR-M08-15.02, FR-M08-18.11, BR-M08-12, BR-M08-13, BR-M08-14 |
| AUT-M08-008 | Đúng thời điểm hết hạn ban tạm đang hiệu lực | Ban→Hết hạn, account→ACTIVE ngay theo M01, lịch sử vẫn tính trừ Bị lật; không khôi phục Mod, reset cảnh cáo/thử thách hoặc tự thêm email hết ban. Ban vĩnh viễn không có hạn hết tự động. | FR-M08-14.08, BR-M08-34, BR-M08-37, BR-M08-43, FR-M01-05.17, FR-M10-06.02 |
| RULE-M08-001 | Role/target ở mọi caller | ACT007 kế thừa ACT008 kế thừa ACT002; Owner/Group Mod không là staff. Mod không thấy/nhận vụ post/comment/account của mình/Mod khác, Admin thấy Mod nhưng không tự xử lý đối tượng mình. Không ai cảnh cáo/ban Admin; không report post/comment/account Admin/nhóm Owner Admin; AI bỏ Admin, không tự cảnh cáo Mod. Phạm vi tự nhắm nhóm chưa chốt, không mở rộng lệnh cấm sang nhóm vô nguồn (GAP004). | FR-M08-01.20, FR-M08-02.06, FR-M08-02.09, FR-M08-03.07, FR-M08-03.09, FR-M08-10.08, FR-M08-10.09, FR-M08-14.09, FR-M08-14.10, BR-M08-44, BR-M08-46, BR-M08-55 |
| RULE-M08-002 | Báo cáo hợp lệ và sắp hàng chờ | Bốn loại, đúng một lý do theo D-REASONS, Khác bắt buộc mô tả; tối đa 3 ảnh JPEG/PNG/WebP, mỗi ảnh ≤5MB. Chỉ target còn thấy, Private theo quyền, HEAVY và bài Khóa toàn bộ vẫn report được. Không self post/comment/account, không trùng actor trong cùng vụ Mở; không sửa/rút báo cáo. Mỗi target một vụ Mở, báo cáo mới sau đóng có thể vụ mới; gửi không tự đổi trạng thái nội dung. Ưu tiên=max trọng số+2×số báo cáo (AI=1): 10 bạo lực/người lớn/thù ghét/quấy rối gồm có hệ thống/giả mạo nhóm, 5 sai thông tin/đạo văn, 2 Spam/Khác. Hòa theo vụ mở trước, không deadline. | FR-M08-01.01, FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-01.06, FR-M08-01.07, FR-M08-01.08, FR-M08-01.09, FR-M08-01.10, FR-M08-01.11, FR-M08-01.12, FR-M08-01.13, FR-M08-01.14, FR-M08-01.15, FR-M08-01.16, FR-M08-01.17, FR-M08-01.18, FR-M08-01.19, FR-M08-01.20, FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.07, FR-M08-02.08, FR-M08-07.10, BR-M08-01, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-05, BR-M08-06, BR-M08-07, BR-M08-45, BR-M08-47 |
| RULE-M08-003 | Giữ vụ/điều tra/kết luận | Một người giữ; tác động/đóng phải còn quyền giữ. Bản lưu chỉ đúng vụ/lịch sử/khiếu nại liên quan, không duyệt tùy ý hoặc Nháp/Bị từ chối người khác. Chỉ số 90×24h = báo cáo của reporter bị bác về đúng target / mọi báo cáo của reporter đã xử lý trong cửa sổ; mốc đúng biên cũ bị loại, mẫu số 0 còn GAP001. Chỉ tham khảo, không tự phạt reporter; ác ý do người đánh giá. Kết luận lý do có thể khác reporter, đóng mọi báo cáo cùng kết quả, giữ riêng tư. Sau đã áp biện pháp mà chọn Bác bỏ hoặc chỉ phạt reporter còn GAP005, không tự rollback/ép kết quả. | FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, FR-M08-05.01, FR-M08-05.02, FR-M08-05.03, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-10.04, FR-M08-10.05, BR-M08-08, BR-M08-09, BR-M08-10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-18, BR-M08-19 |
| RULE-M08-004 | Phạm vi và cờ AI | Chỉ 4 nhóm: Quấy rối, Ngôn từ thù ghét, Nội dung người lớn, Bạo lực; max điểm, hòa nhóm do M13. Không AI Spam/đạo văn/sai thông tin. Ngưỡng tạm 0.9/0.5 dùng chung mọi mức cảnh cáo; ngưỡng tạm 10 reply/5 phút, không cấu hình UI, TBD04/05 chưa chốt. Tắt một cờ không quét/tự cảnh cáo nhưng thủ công/backlog còn dùng. | FR-M08-02.05, FR-M08-08.01, FR-M08-08.02, FR-M08-08.03, FR-M08-08.04, FR-M08-08.05, FR-M08-08.06, FR-M08-08.07, FR-M08-08.08, FR-M08-08.09, FR-M08-08.10, FR-M08-08.11, FR-M08-08.12, FR-M08-09.07, FR-M08-09.10, BR-M08-20, BR-M08-24, BR-M08-25, BR-M08-26, BR-M08-27, BR-M08-42, BR-M08-51 |
| RULE-M08-005 | Cảnh cáo, thời gian, Ban và đảo ngược | 0 Sạch, 1–2 LIGHT/7 ngày, 3–4 MEDIUM/10, 5–6 HEAVY/15; thêm hợp lệ reset hạn dù mức không đổi; đã HEAVY không có cảnh cáo thứ 7. Bỏ/lật giữ record và hạn, giảm lần/tính mức; M09 không giảm lần lần hai, sàn 0 M09 không tự áp M08 (GAP002). Ban 0 lịch sử→30 ngày, 1→90, ≥2→vĩnh viễn; tính mọi từng hiệu lực gồm gỡ sớm/vĩnh viễn thủ công, loại Bị lật. Ban vĩnh viễn thủ công bỏ leo thang; không ban chồng, gỡ trước rồi mới ban lại. Gỡ/hết ban ACTIVE, không khôi phục Mod; thử thách độc lập ban. LIGHT không hạn chế; MEDIUM cấm tạo bài; HEAVY thêm cấm tạo comment, vẫn sửa/xóa cũ/vote/report, search Liên quan ×0.5, loại BXH công khai, không hạ feed. Mức riêng tư. Thời gian VN, N×24h, không chọn cron/UI sửa hằng số. Chỉ warn/Ban/Ban vĩnh viễn, không Suspend/tắt account người khác. | FR-M08-10.02, FR-M08-10.06, FR-M08-10.10, FR-M08-11.01, FR-M08-11.02, FR-M08-11.03, FR-M08-11.04, FR-M08-11.05, FR-M08-12.01, FR-M08-12.02, FR-M08-12.03, FR-M08-12.04, FR-M08-12.05, FR-M08-13.01, FR-M08-13.02, FR-M08-13.03, FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, FR-M08-15.01, FR-M08-15.02, FR-M08-15.03, FR-M08-15.04, FR-M08-15.05, BR-M08-17, BR-M08-28, BR-M08-29, BR-M08-30, BR-M08-31, BR-M08-32, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-37, BR-M08-38, BR-M08-42, BR-M08-43, BR-M08-52, BR-M08-53, BR-M08-54, FR-M09-08.05 |
| RULE-M08-006 | Ẩn nội dung và nhóm | Ẩn khác xóa, staff không xóa nội dung người khác; bỏ/lật cảnh cáo/ban không tự hiện lại nội dung ẩn. Chỉ comment trung bình đang chờ được xét để hiện lại; hậu khiếu nại post do M09/M03. Nhóm Owner là người bị báo cáo, không tự phạt Owner. Ẩn mọi người, không bỏ ẩn; Khóa theo D-LOCK, vẫn quyền Public/Private. Khóa có thể Ẩn ở vụ sau; mở khóa trực tiếp chỉ Bị khóa, không cần giữ vụ; không mở khóa nhóm ẩn. Khi Owner bị ban/vô hiệu hóa/xóa, M11 chuyển ngay cho Group Mod thâm niên dài nhất tính từ bổ nhiệm gần nhất, nếu không có thì Member vào sớm nhất, nếu chỉ có Owner thì xóa mềm nhóm; Owner cũ thành Member, Owner mới có app. Vẫn chạy khi cờ Group tắt/nhóm khóa. M08 chưa chốt ràng buộc Owner/người nhận kết luận khi Owner thay đổi (GAP006). | FR-M08-06.03, FR-M08-07.03, FR-M08-07.04, FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, FR-M08-18.11, BR-M08-16, BR-M08-44, BR-M08-45, BR-M08-48, BR-M08-50, BR-M11-28, FR-M11-11.01, FR-M11-11.02, FR-M11-11.03, FR-M11-11.04, FR-M11-11.05, FR-M11-11.06, FR-M11-11.07, BR-M11-26 |


### Đối soát dữ liệu và biên

| Dữ liệu giả lập/điều kiện | Kết quả phải giữ |
|---|---|
| Vụ 2 báo cáo trọng số max 5; thêm báo cáo trọng số 10 | Ưu tiên 9→16; 3 báo cáo trong cùng vụ Mở; AI item tính 1; hòa ưu tiên theo mốc mở cũ |
| Báo cáo gồm 3 ảnh, có ảnh đúng 5MB; chọn Khác có mô tả | Chấp nhận nếu mọi guard khác hợp lệ; ảnh thứ 4, >5MB, GIF hoặc Khác thiếu mô tả cần sửa rồi gửi lại |
| Người giữ xem K81 lúc T; người khác xem lúc T+20 phút | Mốc người giữ vẫn T; đủ 30 phút không hoạt động hợp lệ thì tự nhả; tác động phải kiểm/nhận lại, không log nhận/nhả |
| Chỉ số: 6 báo cáo bị bác về P81 / 10 đã xử lý của Lan trong 90×24h | 0.6, không dùng tổng mọi báo cáo bị bác về mọi target; đúng T−90×24h bị loại; mẫu số 0 là GAP001 |
| Điểm AI comment 0.499 / 0.5 / 0.899 / 0.9 | Giữ trạng thái / ẩn+vụ chờ / ẩn+vụ chờ / ẩn ngay+trừ điểm; nhánh cảnh cáo độc lập, ngưỡng vẫn tạm |
| Tác giả User chưa HEAVY / Mod / Admin / đã HEAVY | AI cao: cảnh cáo mỗi nội dung nếu đủ điều kiện / đưa Admin quyết / bỏ quét và miễn / yêu cầu ban, không thêm cảnh cáo; không AI ban |
| Thêm cảnh cáo lúc T, số lần 1→2 hoặc 2→3 hoặc 4→5 | LIGHT hạn T+7×24h dù mức không đổi / MEDIUM T+10×24h / HEAVY T+15×24h |
| Đến hạn HEAVY ngày 24/11 10:00+07 từ cảnh cáo T | Giảm MEDIUM 4, hạn mới 04/12 10:00; tiếp giảm LIGHT 2 hạn 11/12 10:00; tiếp Sạch 0; vẫn độc lập ban |
| Bỏ AI khi 3/MEDIUM, hạn 19/11 10:00 | 2/LIGHT, record đã bỏ, hạn vẫn 19/11 10:00; không reset 7 ngày, không tự hiện lại comment ẩn |
| Ban trước: Đã gỡ 1, Bị lật 1; không có ban Đang hiệu lực | Chỉ tính 1→Ban 90×24h; Ban vĩnh viễn thủ công bỏ leo thang; không tạo chồng, gỡ trước rồi mới áp lệnh mới |
| Gỡ/hết ban một người từng là Mod | Account ACTIVE, role USER giữ; lịch sử tính trừ Bị lật; không phục hồi role/nội dung hoặc reset thử thách |
| Ẩn hoặc Khóa nhóm, Owner chưa có chế tài riêng | Chỉ áp trạng thái nhóm; cảnh cáo/ban Owner là lựa chọn riêng với kiểm role, không suy tự động |
| Kết luận Có xử lý ẩn comment/nhóm; cảnh cáo/ban/bài ẩn | Comment/nhóm không URL khiếu nại; chế tài và bài ẩn có; reporter chỉ kết quả chung, target không xem tố cáo |
| Mod có link nhật ký Hoa nhưng không đang xét appeal về đúng thao tác | Từ chối; active appeal về OP81 chỉ mở OP81, không toàn bộ log Hoa; Admin được toàn bộ/lọc actor |


Các bảng AUT/RULE mô tả phản ứng trong boundary, không tạo scenario SYSTEM–AI hoặc scheduler. Không tự chọn cơ chế retry ngoài M13/M07, lịch cron, atomicity/rollback, thứ tự đồng thời hoặc hành vi lỗi hạ tầng chưa có nguồn.

## 6. Truy vết và ma trận quyết định

| Mã hiệu lực | SC/bước/nhánh hoặc AUT/RULE | Mức đối soát |
|---|---|---|
| FR-M08-01 | SC-M08-001/M1; SC-M08-001/M2; SC-M08-001/E3.1; SC-M08-001/E3.2; SC-M08-001/E4.1; SC-M08-001/E4.2; SC-M08-001/E5.1; SC-M08-001/E5.2; SC-M08-001/E18.1; SC-M08-001/E19.1; SC-M08-001/E19.2; SC-M08-001/E20.1; SC-M08-001/E20.2; SC-M08-001/E21.1; RULE-M08-002; SC-M08-001/E18.2; SC-M08-001/E12.1; SC-M08-001/E13.1; SC-M08-001/E14.1; SC-M08-001/E2.1; SC-M08-001/E15.1; SC-M08-001/M3; SC-M08-001/M4; SC-M08-001/E3.3; SC-M08-001/E4.3; SC-M08-001/E5.3; SC-M08-001/E6.2; SC-M08-001/E7.2; SC-M08-001/E8.1; SC-M08-001/E8.2; SC-M08-001/E9.2; SC-M08-001/E10.2; SC-M08-001/E11.2; SC-M08-001/E19.3; SC-M08-001/E19.4; SC-M08-001/E20.3; SC-M08-001/E20.4; SC-M08-001/E16.1; SC-M08-001/E21.2; RULE-M08-001; SC-M08-001/E1.1; SC-M08-001/E3.4; SC-M08-001/E4.4; SC-M08-001/E5.4; SC-M08-001/E6.1; SC-M08-001/E7.1; SC-M08-001/E9.1; SC-M08-001/E10.1; SC-M08-001/E11.1; SC-M08-001/E17.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-02 | SC-M08-002/M1; SC-M08-002/M2; SC-M08-002/E2.1; SC-M08-002/E6.1; SC-M08-002/E6.2; SC-M08-002/E7.1; SC-M08-002/E7.2; SC-M08-002/E8.1; SC-M08-002/E8.2; SC-M08-002/E9.1; SC-M08-002/E9.2; SC-M08-002/E10.1; SC-M08-004/M1; SC-M08-004/E7.1; SC-M08-004/E11.1; SC-M08-004/E12.1; SC-M08-004/E14.1; SC-M08-004/E16.1; SC-M08-004/E27.1; SC-M08-004/E29.1; SC-M08-004/E30.1; SC-M08-004/E31.1; SC-M08-004/E32.1; SC-M08-004/E33.1; RULE-M08-002; SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-004/M2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E7.2; SC-M08-004/E7.4; SC-M08-004/E11.2; SC-M08-004/E11.4; SC-M08-004/E12.2; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.2; SC-M08-004/E14.4; SC-M08-004/E16.2; SC-M08-004/E16.4; SC-M08-004/E27.2; SC-M08-004/E27.4; SC-M08-004/E29.2; SC-M08-004/E29.4; SC-M08-004/E30.2; SC-M08-004/E31.2; SC-M08-004/E32.2; SC-M08-004/E32.4; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; RULE-M08-004; SC-M08-002/E4.1; SC-M08-002/E10.2; SC-M08-003/E3.1; SC-M08-003/E9.2; SC-M08-004/E17.1; SC-M08-004/E33.2; SC-M08-005/E7.1; SC-M08-005/E15.2; SC-M08-006/E7.1; SC-M08-006/E16.2; SC-M08-007/E4.1; SC-M08-007/E12.2; SC-M08-008/E11.1; SC-M08-008/E19.2; SC-M08-010/E8.1; SC-M08-010/E17.2; RULE-M08-001; SC-M08-002/E5.1; SC-M08-003/E4.1; SC-M08-004/E18.1; SC-M08-005/E8.1; SC-M08-006/E8.1; SC-M08-007/E5.1; SC-M08-008/E12.1; SC-M08-010/E9.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-03 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-003/M2; SC-M08-003/E1.1; SC-M08-003/E5.2; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-003/E8.2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E2.1; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E19.1; SC-M08-004/E20.1; SC-M08-004/E20.3; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; SC-M08-005/E9.1; SC-M08-005/E10.1; SC-M08-005/E10.3; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E9.1; SC-M08-006/E10.1; SC-M08-006/E10.3; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-007/E6.1; SC-M08-007/E7.1; SC-M08-007/E7.3; SC-M08-008/E13.1; SC-M08-008/E14.1; SC-M08-008/E14.3; SC-M08-010/E10.1; SC-M08-010/E11.1; SC-M08-010/E11.3; SC-M08-013/E3.1; SC-M08-013/E4.1; SC-M08-013/E4.3; SC-M08-014/E2.1; SC-M08-014/E3.1; SC-M08-014/E3.3; RULE-M08-003; AUT-M08-001; SC-M08-004/M2; SC-M08-004/E7.2; SC-M08-004/E11.2; SC-M08-004/E12.2; SC-M08-004/E14.2; SC-M08-004/E16.2; SC-M08-004/E27.2; SC-M08-004/E29.2; SC-M08-004/E30.2; SC-M08-004/E31.2; SC-M08-004/E32.2; SC-M08-002/E4.1; SC-M08-002/E10.2; SC-M08-003/E3.1; SC-M08-003/E9.2; SC-M08-004/E17.1; SC-M08-004/E33.2; SC-M08-005/E7.1; SC-M08-005/E15.2; SC-M08-006/E7.1; SC-M08-006/E16.2; SC-M08-007/E4.1; SC-M08-007/E12.2; SC-M08-008/E11.1; SC-M08-008/E19.2; SC-M08-010/E8.1; SC-M08-010/E17.2; RULE-M08-001; SC-M08-002/E5.1; SC-M08-003/E4.1; SC-M08-004/E18.1; SC-M08-005/E8.1; SC-M08-006/E8.1; SC-M08-007/E5.1; SC-M08-008/E12.1; SC-M08-010/E9.1; SC-M08-003/M1; SC-M08-003/E5.1; SC-M08-003/E6.1; SC-M08-003/E7.1; SC-M08-003/E8.1; SC-M08-003/E9.1; SC-M08-004/M1; SC-M08-004/M3; SC-M08-004/E7.1; SC-M08-004/E7.3; SC-M08-004/E11.1; SC-M08-004/E11.3; SC-M08-004/E12.1; SC-M08-004/E12.3; SC-M08-004/E14.1; SC-M08-004/E14.3; SC-M08-004/E16.1; SC-M08-004/E16.3; SC-M08-004/E20.2; SC-M08-004/E27.1; SC-M08-004/E27.3; SC-M08-004/E29.1; SC-M08-004/E29.3; SC-M08-004/E30.1; SC-M08-004/E31.1; SC-M08-004/E32.1; SC-M08-004/E32.3; SC-M08-004/E33.1; SC-M08-005/E10.2; SC-M08-006/E10.2; SC-M08-007/E7.2; SC-M08-008/E14.2; SC-M08-010/E11.2; SC-M08-013/E4.2; SC-M08-014/E3.2; SC-M08-003/E2.1; SC-M08-004/E3.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-04 | SC-M08-002/M3; SC-M08-002/M4; SC-M08-002/E6.3; SC-M08-002/E6.4; SC-M08-002/E9.3; SC-M08-002/E9.4; SC-M08-004/M3; SC-M08-004/M4; SC-M08-004/E1.2; SC-M08-004/E1.3; SC-M08-004/E7.3; SC-M08-004/E7.4; SC-M08-004/E11.3; SC-M08-004/E11.4; SC-M08-004/E12.3; SC-M08-004/E12.4; SC-M08-004/E14.3; SC-M08-004/E14.4; SC-M08-004/E16.3; SC-M08-004/E16.4; SC-M08-004/E27.3; SC-M08-004/E27.4; SC-M08-004/E29.3; SC-M08-004/E29.4; SC-M08-004/E32.3; SC-M08-004/E32.4; RULE-M08-003; SC-M08-002/E1.1; SC-M08-012/E5.1; SC-M08-012/E5.2; SC-M08-012/E6.1; SC-M08-012/E6.2; SC-M08-002/E3.1; SC-M08-004/E27.7; SC-M08-008/E6.1; SC-M08-010/E12.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-05 | SC-M08-004/M5; SC-M08-004/M6; SC-M08-004/E4.2; SC-M08-004/E7.7; SC-M08-004/E7.8; SC-M08-004/E11.7; SC-M08-004/E11.8; SC-M08-004/E12.7; SC-M08-004/E12.8; SC-M08-004/E14.9; SC-M08-004/E14.10; SC-M08-004/E15.1; SC-M08-004/E15.2; SC-M08-004/E16.7; SC-M08-004/E16.8; SC-M08-004/E26.1; SC-M08-004/E26.3; SC-M08-004/E26.4; SC-M08-004/E27.9; SC-M08-004/E27.10; SC-M08-004/E29.5; SC-M08-004/E29.6; SC-M08-004/E32.5; SC-M08-004/E32.6; SC-M08-005/M1; SC-M08-005/M2; SC-M08-005/E1.2; SC-M08-005/E3.1; SC-M08-005/E3.2; SC-M08-005/E4.1; SC-M08-005/E4.2; SC-M08-005/E5.1; SC-M08-005/E5.2; SC-M08-005/E6.1; SC-M08-005/E6.2; SC-M08-005/E10.4; SC-M08-005/E11.1; SC-M08-005/E11.2; SC-M08-005/E12.1; SC-M08-005/E12.2; SC-M08-005/E13.1; SC-M08-005/E13.2; SC-M08-005/E14.1; SC-M08-005/E14.2; SC-M08-005/E15.1; RULE-M08-003; AUT-M08-007; SC-M08-004/E5.1; SC-M08-005/E2.1; SC-M08-004/E4.1; SC-M08-004/E26.2; SC-M08-005/E1.1; SC-M08-004/E7.6; SC-M08-007/E1.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-06 | SC-M08-004/E6.1; SC-M08-004/E6.2; SC-M08-004/E7.6; SC-M08-004/E28.2; SC-M08-006/E1.2; SC-M08-006/E11.2; SC-M08-007/M1; SC-M08-007/M2; SC-M08-007/E1.2; SC-M08-007/E7.4; SC-M08-007/E8.1; SC-M08-007/E8.2; SC-M08-007/E9.1; SC-M08-007/E9.2; SC-M08-007/E10.1; SC-M08-007/E10.2; SC-M08-007/E11.1; SC-M08-007/E11.2; SC-M08-007/E12.1; SC-M08-004/E7.5; SC-M08-007/E1.1; SC-M08-007/E3.1; RULE-M08-006; SC-M08-004/E21.1; SC-M08-004/E21.2; SC-M08-007/E2.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-07 | SC-M08-001/M4; SC-M08-001/E1.1; SC-M08-001/E3.4; SC-M08-001/E4.4; SC-M08-001/E5.4; SC-M08-001/E19.4; SC-M08-001/E20.4; SC-M08-004/E13.2; SC-M08-004/E28.2; SC-M08-006/M2; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E11.2; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; RULE-M08-002; SC-M08-004/E13.1; SC-M08-006/M1; SC-M08-006/E2.1; SC-M08-006/E3.1; SC-M08-006/E4.1; SC-M08-006/E5.1; SC-M08-006/E12.1; SC-M08-006/E13.1; SC-M08-006/E14.1; SC-M08-006/E15.1; SC-M08-006/E16.1; SC-M08-004/E13.3; SC-M08-004/E13.4; SC-M08-006/M3; SC-M08-006/M4; SC-M08-006/E12.3; SC-M08-006/E12.4; SC-M08-006/E15.3; SC-M08-006/E15.4; SC-M08-004/E28.1; SC-M08-006/E11.1; RULE-M08-006; SC-M08-004/E14.5; SC-M08-004/E14.6; SC-M08-004/E16.5; SC-M08-004/E16.6; SC-M08-006/E4.3; SC-M08-006/E4.4; SC-M08-006/E5.3; SC-M08-006/E5.4; SC-M08-004/E22.1; SC-M08-004/E22.2; SC-M08-006/E6.1; AUT-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-08 | AUT-M08-002; RULE-M08-004; AUT-M08-004; AUT-M08-007 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-09 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E5.4; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; AUT-M08-003; AUT-M08-004; AUT-M08-007; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-10 | SC-M08-004/E8.1; SC-M08-004/E8.2; SC-M08-004/E14.7; SC-M08-004/E14.8; SC-M08-004/E27.7; SC-M08-004/E27.8; SC-M08-004/E28.3; SC-M08-004/E28.4; SC-M08-006/E4.5; SC-M08-006/E4.6; SC-M08-006/E11.3; SC-M08-006/E11.4; SC-M08-008/M1; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.1; SC-M08-008/E6.2; SC-M08-008/E14.4; SC-M08-008/E15.1; SC-M08-008/E15.2; SC-M08-008/E16.1; SC-M08-008/E16.2; SC-M08-008/E17.1; SC-M08-008/E17.2; SC-M08-008/E18.1; SC-M08-008/E18.2; SC-M08-008/E19.1; SC-M08-008/E20.1; RULE-M08-005; AUT-M08-007; SC-M08-008/E5.1; RULE-M08-003; SC-M08-004/E24.1; SC-M08-004/E24.2; SC-M08-008/E7.1; RULE-M08-001; SC-M08-008/E8.1; SC-M08-008/E20.2; SC-M08-010/E18.2; SC-M08-004/E23.1; SC-M08-004/E23.2; SC-M08-008/E9.1; SC-M08-008/E10.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-11 | SC-M08-009/M1; SC-M08-009/M2; SC-M08-009/E1.1; SC-M08-009/E2.1; SC-M08-009/E3.1; SC-M08-009/E3.2; SC-M08-009/E4.1; SC-M08-009/E4.2; SC-M08-009/E5.1; SC-M08-009/E5.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-12 | AUT-M08-005; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-13 | SC-M08-012/M1; SC-M08-012/M2; SC-M08-012/E2.1; SC-M08-012/E3.1; SC-M08-012/E4.1; SC-M08-012/E4.2; RULE-M08-005; SC-M08-012/E1.1; SC-M08-012/E5.1; SC-M08-012/E5.2; SC-M08-012/E6.1; SC-M08-012/E6.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14 | SC-M08-004/E8.2; SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-004/E14.8; SC-M08-004/E23.1; SC-M08-004/E23.2; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E5.4; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E9.1; SC-M08-008/E9.3; SC-M08-008/E10.1; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; AUT-M08-004; RULE-M08-005; SC-M08-004/E9.1; SC-M08-008/E9.2; SC-M08-010/M1; SC-M08-010/E11.4; SC-M08-010/E12.1; SC-M08-010/E13.1; SC-M08-010/E14.1; SC-M08-010/E15.1; SC-M08-010/E16.1; SC-M08-010/E17.1; SC-M08-010/E18.1; SC-M08-004/E10.1; SC-M08-010/E3.1; SC-M08-010/E6.4; AUT-M08-007; AUT-M08-008; SC-M08-004/E24.1; SC-M08-004/E24.2; SC-M08-010/E4.1; RULE-M08-001; SC-M08-008/E20.2; SC-M08-010/E5.1; SC-M08-010/E18.2; SC-M08-004/E25.1; SC-M08-004/E25.2; SC-M08-010/E6.1; SC-M08-010/E7.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-15 | SC-M08-010/E6.2; SC-M08-010/E6.3; SC-M08-011/M1; SC-M08-011/M2; SC-M08-011/E2.1; SC-M08-011/E2.2; SC-M08-011/E3.1; SC-M08-011/E3.2; SC-M08-011/E4.1; SC-M08-011/E4.2; RULE-M08-005; AUT-M08-007; SC-M08-011/E1.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-16 | SC-M08-003/M2; SC-M08-003/E5.2; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-003/E8.2; SC-M08-004/E20.3; SC-M08-005/E10.1; SC-M08-005/E10.3; SC-M08-006/E10.3; SC-M08-007/E7.1; SC-M08-007/E7.3; SC-M08-008/E14.1; SC-M08-008/E14.3; SC-M08-010/E11.1; SC-M08-010/E11.3; SC-M08-013/E4.1; SC-M08-013/E4.3; SC-M08-014/E3.1; SC-M08-014/E3.3; SC-M08-016/M2; SC-M08-016/E3.2; SC-M08-016/E4.2; SC-M08-016/E5.2; SC-M08-016/E6.2; AUT-M08-001; AUT-M08-006; SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; SC-M08-016/M4; SC-M08-016/E2.2; SC-M08-016/E3.4; SC-M08-016/E6.4; SC-M08-009/M2; SC-M08-009/E2.1; SC-M08-009/E3.2; SC-M08-009/E4.2; SC-M08-009/E5.2; SC-M08-010/E6.3; SC-M08-011/M2; SC-M08-011/E2.2; SC-M08-011/E3.2; SC-M08-011/E4.2; SC-M08-015/M2; SC-M08-015/E2.2; SC-M08-015/E3.2; SC-M08-015/E4.2; SC-M08-016/E6.3 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-17 | SC-M08-016/M1; SC-M08-016/M2; SC-M08-016/M3; SC-M08-016/M4; SC-M08-016/E3.1; SC-M08-016/E3.2; SC-M08-016/E3.3; SC-M08-016/E3.4; SC-M08-016/E4.1; SC-M08-016/E4.2; SC-M08-016/E5.1; SC-M08-016/E5.2; SC-M08-016/E6.1; SC-M08-016/E6.2; SC-M08-016/E6.4; SC-M08-016/E1.1; SC-M08-016/E2.1; SC-M08-016/E2.2; SC-M08-016/E6.3 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-18 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.1; SC-M08-005/E3.2; SC-M08-005/E4.1; SC-M08-005/E4.2; SC-M08-005/E5.1; SC-M08-005/E5.2; SC-M08-005/E6.1; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; AUT-M08-007; RULE-M08-006; SC-M08-004/E11.5; SC-M08-004/E11.6; SC-M08-004/E12.6; SC-M08-004/E27.6; SC-M08-013/M1; SC-M08-013/M2; SC-M08-013/E1.1; SC-M08-013/E4.4; SC-M08-013/E5.1; SC-M08-013/E5.2; SC-M08-013/E6.1; SC-M08-013/E6.2; SC-M08-013/E7.1; SC-M08-013/E7.2; SC-M08-014/M2; SC-M08-014/E4.2; SC-M08-014/E5.2; SC-M08-014/E6.2; SC-M08-004/E12.5; SC-M08-004/E27.5; SC-M08-014/M1; SC-M08-014/E3.4; SC-M08-014/E4.1; SC-M08-014/E5.1; SC-M08-014/E6.1; SC-M08-015/M1; SC-M08-015/M2; SC-M08-015/E2.1; SC-M08-015/E2.2; SC-M08-015/E3.1; SC-M08-015/E3.2; SC-M08-015/E4.1; SC-M08-015/E4.2; SC-M08-013/E2.1; SC-M08-014/E1.1; SC-M08-015/E1.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.01 | SC-M08-001/M1; SC-M08-001/M2; SC-M08-001/E3.1; SC-M08-001/E3.2; SC-M08-001/E4.1; SC-M08-001/E4.2; SC-M08-001/E5.1; SC-M08-001/E5.2; SC-M08-001/E18.1; SC-M08-001/E19.1; SC-M08-001/E19.2; SC-M08-001/E20.1; SC-M08-001/E20.2; SC-M08-001/E21.1; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.02 | SC-M08-001/M3; SC-M08-001/M4; SC-M08-001/E1.1; SC-M08-001/E2.1; SC-M08-001/E3.3; SC-M08-001/E3.4; SC-M08-001/E4.3; SC-M08-001/E4.4; SC-M08-001/E5.3; SC-M08-001/E5.4; SC-M08-001/E6.2; SC-M08-001/E7.2; SC-M08-001/E8.2; SC-M08-001/E9.2; SC-M08-001/E10.2; SC-M08-001/E11.2; SC-M08-001/E19.3; SC-M08-001/E19.4; SC-M08-001/E20.3; SC-M08-001/E20.4; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.03 | SC-M08-001/M4; SC-M08-001/E1.1; SC-M08-001/E3.4; SC-M08-001/E4.4; SC-M08-001/E5.4; SC-M08-001/E19.4; SC-M08-001/E20.4; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.04 | SC-M08-001/M4; SC-M08-001/E2.1; SC-M08-001/E3.4; SC-M08-001/E4.4; SC-M08-001/E5.4; SC-M08-001/E19.4; SC-M08-001/E20.4; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.05 | SC-M08-001/M4; SC-M08-001/E1.1; SC-M08-001/E2.1; SC-M08-001/E3.4; SC-M08-001/E4.4; SC-M08-001/E5.4; SC-M08-001/E19.4; SC-M08-001/E20.4; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.06 | SC-M08-001/M2; SC-M08-001/E18.2; SC-M08-001/E19.2; SC-M08-001/E20.2; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.07 | SC-M08-001/E6.1; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.08 | SC-M08-001/E7.1; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.09 | SC-M08-001/E9.1; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.10 | SC-M08-001/E10.1; SC-M08-001/E11.1; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.11 | SC-M08-001/M2; SC-M08-001/E12.1; SC-M08-001/E19.2; SC-M08-001/E20.2; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.12 | SC-M08-001/M2; SC-M08-001/E13.1; SC-M08-001/E19.2; SC-M08-001/E20.2; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.13 | SC-M08-001/E17.1; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.14 | SC-M08-001/E3.2; SC-M08-001/E4.2; SC-M08-001/E5.2; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.15 | SC-M08-001/M2; SC-M08-001/E14.1; SC-M08-001/E19.2; SC-M08-001/E20.2; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.16 | SC-M08-001/M2; SC-M08-001/E2.1; SC-M08-001/E15.1; SC-M08-001/E19.2; SC-M08-001/E20.2; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.17 | SC-M08-001/E17.1; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.18 | RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.19 | SC-M08-001/M2; SC-M08-001/M3; SC-M08-001/M4; SC-M08-001/E3.2; SC-M08-001/E3.3; SC-M08-001/E4.2; SC-M08-001/E4.3; SC-M08-001/E5.2; SC-M08-001/E5.3; SC-M08-001/E6.2; SC-M08-001/E7.2; SC-M08-001/E8.1; SC-M08-001/E8.2; SC-M08-001/E9.2; SC-M08-001/E10.2; SC-M08-001/E11.2; SC-M08-001/E19.2; SC-M08-001/E19.3; SC-M08-001/E19.4; SC-M08-001/E20.2; SC-M08-001/E20.3; SC-M08-001/E20.4; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-01.20 | SC-M08-001/M2; SC-M08-001/E3.2; SC-M08-001/E4.2; SC-M08-001/E5.2; SC-M08-001/E16.1; SC-M08-001/E19.2; SC-M08-001/E20.2; SC-M08-001/E21.2; RULE-M08-001; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-02.01 | SC-M08-002/M1; SC-M08-002/M2; SC-M08-002/E2.1; SC-M08-002/E6.1; SC-M08-002/E6.2; SC-M08-002/E7.1; SC-M08-002/E7.2; SC-M08-002/E8.1; SC-M08-002/E8.2; SC-M08-002/E9.1; SC-M08-002/E9.2; SC-M08-002/E10.1; SC-M08-004/M1; SC-M08-004/E7.1; SC-M08-004/E11.1; SC-M08-004/E12.1; SC-M08-004/E14.1; SC-M08-004/E16.1; SC-M08-004/E27.1; SC-M08-004/E29.1; SC-M08-004/E30.1; SC-M08-004/E31.1; SC-M08-004/E32.1; SC-M08-004/E33.1; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-02.02 | SC-M08-002/M2; SC-M08-002/E6.2; SC-M08-002/E7.2; SC-M08-002/E8.2; SC-M08-002/E9.2; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-02.03 | SC-M08-002/M2; SC-M08-002/E6.2; SC-M08-002/E7.2; SC-M08-002/E8.2; SC-M08-002/E9.2; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-02.04 | SC-M08-002/M2; SC-M08-002/M4; SC-M08-002/E6.2; SC-M08-002/E6.4; SC-M08-002/E7.2; SC-M08-002/E8.2; SC-M08-002/E9.2; SC-M08-002/E9.4; SC-M08-004/M2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E7.2; SC-M08-004/E7.4; SC-M08-004/E11.2; SC-M08-004/E11.4; SC-M08-004/E12.2; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.2; SC-M08-004/E14.4; SC-M08-004/E16.2; SC-M08-004/E16.4; SC-M08-004/E27.2; SC-M08-004/E27.4; SC-M08-004/E29.2; SC-M08-004/E29.4; SC-M08-004/E30.2; SC-M08-004/E31.2; SC-M08-004/E32.2; SC-M08-004/E32.4; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-02.05 | SC-M08-002/M2; SC-M08-002/E2.1; SC-M08-002/E6.2; SC-M08-002/E7.2; SC-M08-002/E8.2; SC-M08-002/E9.2; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-02.06 | SC-M08-002/M2; SC-M08-002/M4; SC-M08-002/E4.1; SC-M08-002/E6.2; SC-M08-002/E6.4; SC-M08-002/E7.2; SC-M08-002/E8.2; SC-M08-002/E9.2; SC-M08-002/E9.4; SC-M08-002/E10.2; SC-M08-003/E3.1; SC-M08-003/E9.2; SC-M08-004/M2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E7.2; SC-M08-004/E7.4; SC-M08-004/E11.2; SC-M08-004/E11.4; SC-M08-004/E12.2; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.2; SC-M08-004/E14.4; SC-M08-004/E16.2; SC-M08-004/E16.4; SC-M08-004/E17.1; SC-M08-004/E27.2; SC-M08-004/E27.4; SC-M08-004/E29.2; SC-M08-004/E29.4; SC-M08-004/E30.2; SC-M08-004/E31.2; SC-M08-004/E32.2; SC-M08-004/E32.4; SC-M08-004/E33.2; SC-M08-005/E7.1; SC-M08-005/E15.2; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E7.1; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-006/E16.2; SC-M08-007/E4.1; SC-M08-007/E12.2; SC-M08-008/E11.1; SC-M08-008/E19.2; SC-M08-010/E8.1; SC-M08-010/E17.2; RULE-M08-001 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-02.07 | SC-M08-002/M2; SC-M08-002/E2.1; SC-M08-002/E6.2; SC-M08-002/E7.2; SC-M08-002/E8.2; SC-M08-002/E9.2; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-02.08 | SC-M08-002/M2; SC-M08-002/E6.2; SC-M08-002/E7.2; SC-M08-002/E8.2; SC-M08-002/E9.2; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-02.09 | SC-M08-002/M2; SC-M08-002/M4; SC-M08-002/E5.1; SC-M08-002/E6.2; SC-M08-002/E6.4; SC-M08-002/E7.2; SC-M08-002/E8.2; SC-M08-002/E9.2; SC-M08-002/E9.4; SC-M08-003/E4.1; SC-M08-004/M2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E7.2; SC-M08-004/E7.4; SC-M08-004/E11.2; SC-M08-004/E11.4; SC-M08-004/E12.2; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.2; SC-M08-004/E14.4; SC-M08-004/E16.2; SC-M08-004/E16.4; SC-M08-004/E18.1; SC-M08-004/E27.2; SC-M08-004/E27.4; SC-M08-004/E29.2; SC-M08-004/E29.4; SC-M08-004/E30.2; SC-M08-004/E31.2; SC-M08-004/E32.2; SC-M08-004/E32.4; SC-M08-005/E8.1; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E8.1; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-007/E5.1; SC-M08-008/E12.1; SC-M08-010/E9.1; RULE-M08-001 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-03.01 | SC-M08-003/M1; SC-M08-003/M2; SC-M08-003/E5.1; SC-M08-003/E5.2; SC-M08-003/E6.1; SC-M08-003/E6.2; SC-M08-003/E7.1; SC-M08-003/E7.2; SC-M08-003/E8.1; SC-M08-003/E8.2; SC-M08-003/E9.1; SC-M08-004/M1; SC-M08-004/M3; SC-M08-004/E7.1; SC-M08-004/E7.3; SC-M08-004/E11.1; SC-M08-004/E11.3; SC-M08-004/E12.1; SC-M08-004/E12.3; SC-M08-004/E14.1; SC-M08-004/E14.3; SC-M08-004/E16.1; SC-M08-004/E16.3; SC-M08-004/E20.2; SC-M08-004/E20.3; SC-M08-004/E27.1; SC-M08-004/E27.3; SC-M08-004/E29.1; SC-M08-004/E29.3; SC-M08-004/E30.1; SC-M08-004/E31.1; SC-M08-004/E32.1; SC-M08-004/E32.3; SC-M08-004/E33.1; SC-M08-005/E10.2; SC-M08-005/E10.3; SC-M08-006/E10.2; SC-M08-006/E10.3; SC-M08-007/E7.2; SC-M08-007/E7.3; SC-M08-008/E14.2; SC-M08-008/E14.3; SC-M08-010/E11.2; SC-M08-010/E11.3; SC-M08-013/E4.2; SC-M08-013/E4.3; SC-M08-014/E3.2; SC-M08-014/E3.3 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-03.02 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-003/M2; SC-M08-003/E1.1; SC-M08-003/E5.2; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-003/E8.2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E2.1; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E19.1; SC-M08-004/E20.1; SC-M08-004/E20.3; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; SC-M08-005/E9.1; SC-M08-005/E10.1; SC-M08-005/E10.3; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E9.1; SC-M08-006/E10.1; SC-M08-006/E10.3; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-007/E6.1; SC-M08-007/E7.1; SC-M08-007/E7.3; SC-M08-008/E13.1; SC-M08-008/E14.1; SC-M08-008/E14.3; SC-M08-010/E10.1; SC-M08-010/E11.1; SC-M08-010/E11.3; SC-M08-013/E3.1; SC-M08-013/E4.1; SC-M08-013/E4.3; SC-M08-014/E2.1; SC-M08-014/E3.1; SC-M08-014/E3.3 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-03.03 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-003/M2; SC-M08-003/E5.2; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-003/E8.2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E2.1; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E19.1; SC-M08-004/E20.1; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; SC-M08-005/E9.1; SC-M08-005/E10.1; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E9.1; SC-M08-006/E10.1; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-007/E6.1; SC-M08-007/E7.1; SC-M08-008/E13.1; SC-M08-008/E14.1; SC-M08-010/E10.1; SC-M08-010/E11.1; SC-M08-013/E3.1; SC-M08-013/E4.1; SC-M08-014/E2.1; SC-M08-014/E3.1; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-03.04 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-003/M2; SC-M08-003/E5.2; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-003/E8.2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E19.1; SC-M08-004/E20.1; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; SC-M08-005/E9.1; SC-M08-005/E10.1; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E9.1; SC-M08-006/E10.1; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-007/E6.1; SC-M08-007/E7.1; SC-M08-008/E13.1; SC-M08-008/E14.1; SC-M08-010/E10.1; SC-M08-010/E11.1; SC-M08-013/E3.1; SC-M08-013/E4.1; SC-M08-014/E2.1; SC-M08-014/E3.1; AUT-M08-001; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-03.05 | SC-M08-003/M2; SC-M08-003/E2.1; SC-M08-003/E5.2; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-003/E8.2; SC-M08-004/E3.1; SC-M08-004/E20.3; SC-M08-005/E10.3; SC-M08-006/E10.3; SC-M08-007/E7.3; SC-M08-008/E14.3; SC-M08-010/E11.3; SC-M08-013/E4.3; SC-M08-014/E3.3 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-03.06 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-003/M2; SC-M08-003/E5.2; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-003/E8.2; SC-M08-004/M2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E7.2; SC-M08-004/E7.4; SC-M08-004/E11.2; SC-M08-004/E11.4; SC-M08-004/E12.2; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.2; SC-M08-004/E14.4; SC-M08-004/E16.2; SC-M08-004/E16.4; SC-M08-004/E20.3; SC-M08-004/E27.2; SC-M08-004/E27.4; SC-M08-004/E29.2; SC-M08-004/E29.4; SC-M08-004/E30.2; SC-M08-004/E31.2; SC-M08-004/E32.2; SC-M08-004/E32.4; SC-M08-005/E10.3; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E10.3; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-007/E7.3; SC-M08-008/E14.3; SC-M08-010/E11.3; SC-M08-013/E4.3; SC-M08-014/E3.3 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-03.07 | SC-M08-002/M4; SC-M08-002/E4.1; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-002/E10.2; SC-M08-003/M2; SC-M08-003/E3.1; SC-M08-003/E5.2; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-003/E8.2; SC-M08-003/E9.2; SC-M08-004/M2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E7.2; SC-M08-004/E7.4; SC-M08-004/E11.2; SC-M08-004/E11.4; SC-M08-004/E12.2; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.2; SC-M08-004/E14.4; SC-M08-004/E16.2; SC-M08-004/E16.4; SC-M08-004/E17.1; SC-M08-004/E20.3; SC-M08-004/E27.2; SC-M08-004/E27.4; SC-M08-004/E29.2; SC-M08-004/E29.4; SC-M08-004/E30.2; SC-M08-004/E31.2; SC-M08-004/E32.2; SC-M08-004/E32.4; SC-M08-004/E33.2; SC-M08-005/E7.1; SC-M08-005/E10.3; SC-M08-005/E15.2; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E7.1; SC-M08-006/E10.3; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-006/E16.2; SC-M08-007/E4.1; SC-M08-007/E7.3; SC-M08-007/E12.2; SC-M08-008/E11.1; SC-M08-008/E14.3; SC-M08-008/E19.2; SC-M08-010/E8.1; SC-M08-010/E11.3; SC-M08-010/E17.2; SC-M08-013/E4.3; SC-M08-014/E3.3; RULE-M08-001 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-03.08 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-003/M2; SC-M08-003/E5.2; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-003/E8.2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E19.1; SC-M08-004/E20.1; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; SC-M08-005/E9.1; SC-M08-005/E10.1; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E9.1; SC-M08-006/E10.1; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-007/E6.1; SC-M08-007/E7.1; SC-M08-008/E13.1; SC-M08-008/E14.1; SC-M08-010/E10.1; SC-M08-010/E11.1; SC-M08-013/E3.1; SC-M08-013/E4.1; SC-M08-014/E2.1; SC-M08-014/E3.1; AUT-M08-001; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-03.09 | SC-M08-002/M4; SC-M08-002/E5.1; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-003/M2; SC-M08-003/E4.1; SC-M08-003/E5.2; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-003/E8.2; SC-M08-004/M2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E7.2; SC-M08-004/E7.4; SC-M08-004/E11.2; SC-M08-004/E11.4; SC-M08-004/E12.2; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.2; SC-M08-004/E14.4; SC-M08-004/E16.2; SC-M08-004/E16.4; SC-M08-004/E18.1; SC-M08-004/E20.3; SC-M08-004/E27.2; SC-M08-004/E27.4; SC-M08-004/E29.2; SC-M08-004/E29.4; SC-M08-004/E30.2; SC-M08-004/E31.2; SC-M08-004/E32.2; SC-M08-004/E32.4; SC-M08-005/E8.1; SC-M08-005/E10.3; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E8.1; SC-M08-006/E10.3; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-007/E5.1; SC-M08-007/E7.3; SC-M08-008/E12.1; SC-M08-008/E14.3; SC-M08-010/E9.1; SC-M08-010/E11.3; SC-M08-013/E4.3; SC-M08-014/E3.3; RULE-M08-001 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-04.01 | SC-M08-002/M3; SC-M08-002/M4; SC-M08-002/E6.3; SC-M08-002/E6.4; SC-M08-002/E9.3; SC-M08-002/E9.4; SC-M08-004/M3; SC-M08-004/M4; SC-M08-004/E1.2; SC-M08-004/E1.3; SC-M08-004/E7.3; SC-M08-004/E7.4; SC-M08-004/E11.3; SC-M08-004/E11.4; SC-M08-004/E12.3; SC-M08-004/E12.4; SC-M08-004/E14.3; SC-M08-004/E14.4; SC-M08-004/E16.3; SC-M08-004/E16.4; SC-M08-004/E27.3; SC-M08-004/E27.4; SC-M08-004/E29.3; SC-M08-004/E29.4; SC-M08-004/E32.3; SC-M08-004/E32.4; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-04.02 | SC-M08-002/M4; SC-M08-002/E1.1; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-004/M4; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-04.03 | SC-M08-002/M4; SC-M08-002/E1.1; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-004/M4; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-04.04 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-004/M4; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt; GAP001 tại mẫu số 0 |
| FR-M08-04.05 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-004/M4; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; SC-M08-012/E5.1; SC-M08-012/E5.2; SC-M08-012/E6.1; SC-M08-012/E6.2; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-04.06 | SC-M08-002/M4; SC-M08-002/E1.1; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-004/M4; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-04.07 | SC-M08-002/M4; SC-M08-002/E1.1; SC-M08-002/E3.1; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-004/M4; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-04.08 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-004/M4; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-04.09 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-004/M4; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-04.10 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-004/M4; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E27.4; SC-M08-004/E27.7; SC-M08-004/E29.4; SC-M08-004/E32.4; SC-M08-008/E6.1; SC-M08-010/E12.1; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt; GAP006 Owner thay đổi trong vụ |
| FR-M08-05.01 | SC-M08-004/M5; SC-M08-004/M6; SC-M08-004/E4.2; SC-M08-004/E7.7; SC-M08-004/E7.8; SC-M08-004/E11.7; SC-M08-004/E11.8; SC-M08-004/E12.7; SC-M08-004/E12.8; SC-M08-004/E14.9; SC-M08-004/E14.10; SC-M08-004/E15.1; SC-M08-004/E15.2; SC-M08-004/E16.7; SC-M08-004/E16.8; SC-M08-004/E26.1; SC-M08-004/E26.3; SC-M08-004/E26.4; SC-M08-004/E27.9; SC-M08-004/E27.10; SC-M08-004/E29.5; SC-M08-004/E29.6; SC-M08-004/E32.5; SC-M08-004/E32.6; SC-M08-005/M1; SC-M08-005/M2; SC-M08-005/E1.2; SC-M08-005/E3.1; SC-M08-005/E3.2; SC-M08-005/E4.1; SC-M08-005/E4.2; SC-M08-005/E5.1; SC-M08-005/E5.2; SC-M08-005/E6.1; SC-M08-005/E6.2; SC-M08-005/E10.4; SC-M08-005/E11.1; SC-M08-005/E11.2; SC-M08-005/E12.1; SC-M08-005/E12.2; SC-M08-005/E13.1; SC-M08-005/E13.2; SC-M08-005/E14.1; SC-M08-005/E14.2; SC-M08-005/E15.1; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt; GAP005 kết luận sau biện pháp/chỉ phạt reporter |
| FR-M08-05.02 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-05.03 | SC-M08-004/M5; SC-M08-004/M6; SC-M08-004/E7.7; SC-M08-004/E7.8; SC-M08-004/E11.7; SC-M08-004/E11.8; SC-M08-004/E12.7; SC-M08-004/E12.8; SC-M08-004/E14.9; SC-M08-004/E14.10; SC-M08-004/E15.1; SC-M08-004/E15.2; SC-M08-004/E16.7; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.9; SC-M08-004/E27.10; SC-M08-004/E29.5; SC-M08-004/E29.6; SC-M08-004/E32.5; SC-M08-004/E32.6; SC-M08-005/M1; SC-M08-005/M2; SC-M08-005/E3.1; SC-M08-005/E3.2; SC-M08-005/E4.1; SC-M08-005/E4.2; SC-M08-005/E5.1; SC-M08-005/E5.2; SC-M08-005/E6.1; SC-M08-005/E6.2; SC-M08-005/E10.4; SC-M08-005/E11.1; SC-M08-005/E11.2; SC-M08-005/E12.1; SC-M08-005/E12.2; SC-M08-005/E13.1; SC-M08-005/E13.2; SC-M08-005/E14.1; SC-M08-005/E14.2; SC-M08-005/E15.1; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-05.04 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; AUT-M08-007; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-05.05 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; AUT-M08-007; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-05.06 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; AUT-M08-007; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-05.07 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-05.08 | SC-M08-004/M6; SC-M08-004/E5.1; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E2.1; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-05.09 | SC-M08-004/M6; SC-M08-004/E4.1; SC-M08-004/E4.2; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.1; SC-M08-004/E26.2; SC-M08-004/E26.3; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E1.1; SC-M08-005/E1.2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-05.10 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; AUT-M08-007; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-05.11 | SC-M08-004/M6; SC-M08-004/E7.6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.1; SC-M08-005/E3.2; SC-M08-005/E4.1; SC-M08-005/E4.2; SC-M08-005/E5.1; SC-M08-005/E5.2; SC-M08-005/E6.1; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; SC-M08-007/E1.2; AUT-M08-007; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-06.01 | SC-M08-004/E6.1; SC-M08-004/E6.2; SC-M08-004/E7.6; SC-M08-004/E28.2; SC-M08-006/E1.2; SC-M08-006/E11.2; SC-M08-007/M1; SC-M08-007/M2; SC-M08-007/E1.2; SC-M08-007/E7.4; SC-M08-007/E8.1; SC-M08-007/E8.2; SC-M08-007/E9.1; SC-M08-007/E9.2; SC-M08-007/E10.1; SC-M08-007/E10.2; SC-M08-007/E11.1; SC-M08-007/E11.2; SC-M08-007/E12.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-06.02 | SC-M08-004/E6.2; SC-M08-004/E7.5; SC-M08-004/E7.6; SC-M08-004/E28.2; SC-M08-006/E1.2; SC-M08-006/E11.2; SC-M08-007/M2; SC-M08-007/E1.1; SC-M08-007/E1.2; SC-M08-007/E8.2; SC-M08-007/E9.2; SC-M08-007/E10.2; SC-M08-007/E11.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-06.03 | SC-M08-004/E6.2; SC-M08-004/E7.6; SC-M08-004/E28.2; SC-M08-006/E1.2; SC-M08-006/E11.2; SC-M08-007/M2; SC-M08-007/E1.2; SC-M08-007/E3.1; SC-M08-007/E8.2; SC-M08-007/E9.2; SC-M08-007/E10.2; SC-M08-007/E11.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-06.04 | SC-M08-004/E6.2; SC-M08-004/E7.6; SC-M08-004/E28.2; SC-M08-006/E1.2; SC-M08-006/E11.2; SC-M08-007/M2; SC-M08-007/E1.2; SC-M08-007/E8.2; SC-M08-007/E9.2; SC-M08-007/E10.2; SC-M08-007/E11.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-06.05 | SC-M08-004/E6.2; SC-M08-004/E7.6; SC-M08-004/E21.1; SC-M08-004/E21.2; SC-M08-004/E28.2; SC-M08-006/E1.2; SC-M08-006/E11.2; SC-M08-007/M2; SC-M08-007/E1.2; SC-M08-007/E2.1; SC-M08-007/E8.2; SC-M08-007/E9.2; SC-M08-007/E10.2; SC-M08-007/E11.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-06.06 | SC-M08-004/E6.2; SC-M08-004/E7.6; SC-M08-004/E28.2; SC-M08-006/E1.2; SC-M08-006/E11.2; SC-M08-007/M2; SC-M08-007/E1.2; SC-M08-007/E8.2; SC-M08-007/E9.2; SC-M08-007/E10.2; SC-M08-007/E11.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-07.01 | SC-M08-004/E13.2; SC-M08-004/E13.3; SC-M08-004/E13.4; SC-M08-004/E28.2; SC-M08-006/M2; SC-M08-006/M3; SC-M08-006/M4; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E11.2; SC-M08-006/E12.2; SC-M08-006/E12.3; SC-M08-006/E12.4; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-006/E15.3; SC-M08-006/E15.4 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-07.02 | SC-M08-004/E13.2; SC-M08-004/E28.1; SC-M08-004/E28.2; SC-M08-006/M2; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E11.1; SC-M08-006/E11.2; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-07.03 | SC-M08-004/E13.2; SC-M08-004/E28.2; SC-M08-006/M2; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E11.2; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-07.04 | SC-M08-004/E13.2; SC-M08-004/E14.5; SC-M08-004/E14.6; SC-M08-004/E16.5; SC-M08-004/E16.6; SC-M08-004/E28.2; SC-M08-006/M2; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E4.3; SC-M08-006/E4.4; SC-M08-006/E5.2; SC-M08-006/E5.3; SC-M08-006/E5.4; SC-M08-006/E11.2; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-07.05 | SC-M08-004/E13.2; SC-M08-004/E13.4; SC-M08-004/E14.5; SC-M08-004/E14.6; SC-M08-004/E16.5; SC-M08-004/E16.6; SC-M08-004/E28.1; SC-M08-004/E28.2; SC-M08-006/M2; SC-M08-006/M4; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E4.3; SC-M08-006/E4.4; SC-M08-006/E5.2; SC-M08-006/E5.4; SC-M08-006/E11.1; SC-M08-006/E11.2; SC-M08-006/E12.2; SC-M08-006/E12.4; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-006/E15.4 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-07.06 | SC-M08-004/E13.1; SC-M08-004/E13.2; SC-M08-004/E28.2; SC-M08-006/M1; SC-M08-006/M2; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.1; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.1; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.1; SC-M08-006/E4.2; SC-M08-006/E5.1; SC-M08-006/E5.2; SC-M08-006/E11.2; SC-M08-006/E12.1; SC-M08-006/E12.2; SC-M08-006/E13.1; SC-M08-006/E13.2; SC-M08-006/E14.1; SC-M08-006/E14.2; SC-M08-006/E15.1; SC-M08-006/E15.2; SC-M08-006/E16.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-07.07 | SC-M08-004/E13.2; SC-M08-004/E13.4; SC-M08-004/E22.1; SC-M08-004/E22.2; SC-M08-004/E28.2; SC-M08-006/M2; SC-M08-006/M4; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E6.1; SC-M08-006/E11.2; SC-M08-006/E12.2; SC-M08-006/E12.4; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-006/E15.4 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-07.08 | SC-M08-004/E13.2; SC-M08-004/E28.2; SC-M08-006/M2; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E11.2; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-07.09 | SC-M08-004/E13.2; SC-M08-004/E28.2; SC-M08-006/M2; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E11.2; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; AUT-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-07.10 | SC-M08-001/M4; SC-M08-001/E1.1; SC-M08-001/E3.4; SC-M08-001/E4.4; SC-M08-001/E5.4; SC-M08-001/E19.4; SC-M08-001/E20.4; SC-M08-004/E13.2; SC-M08-004/E28.2; SC-M08-006/M2; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E11.2; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-08.01 | AUT-M08-002; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-08.02 | AUT-M08-002; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-08.03 | AUT-M08-002; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-08.04 | AUT-M08-002; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-08.05 | AUT-M08-002; AUT-M08-004; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-08.06 | AUT-M08-002; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-08.07 | AUT-M08-002; AUT-M08-007; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-08.08 | AUT-M08-002; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-08.09 | AUT-M08-002; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-08.10 | AUT-M08-002; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-08.11 | AUT-M08-002; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-08.12 | AUT-M08-002; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-09.01 | AUT-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-09.02 | AUT-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-09.03 | AUT-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-09.04 | AUT-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-09.05 | AUT-M08-003; AUT-M08-007 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-09.06 | AUT-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-09.07 | AUT-M08-003; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-09.08 | AUT-M08-003; AUT-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-09.09 | AUT-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-09.10 | AUT-M08-003; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-09.11 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E5.4; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; AUT-M08-003; AUT-M08-004 | Có vị trí đối soát; chưa phê duyệt; GAP003 tại lô qua biên HEAVY |
| FR-M08-09.12 | AUT-M08-003 | Có vị trí đối soát; chưa phê duyệt; GAP003 tại lô qua biên HEAVY |
| FR-M08-10.01 | SC-M08-004/E8.1; SC-M08-004/E8.2; SC-M08-004/E14.7; SC-M08-004/E14.8; SC-M08-004/E27.7; SC-M08-004/E27.8; SC-M08-004/E28.3; SC-M08-004/E28.4; SC-M08-006/E4.5; SC-M08-006/E4.6; SC-M08-006/E11.3; SC-M08-006/E11.4; SC-M08-008/M1; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.1; SC-M08-008/E6.2; SC-M08-008/E14.4; SC-M08-008/E15.1; SC-M08-008/E15.2; SC-M08-008/E16.1; SC-M08-008/E16.2; SC-M08-008/E17.1; SC-M08-008/E17.2; SC-M08-008/E18.1; SC-M08-008/E18.2; SC-M08-008/E19.1; SC-M08-008/E20.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-10.02 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-10.03 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; AUT-M08-007 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-10.04 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt; GAP005 kết luận sau biện pháp/chỉ phạt reporter |
| FR-M08-10.05 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-10.06 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.1; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-10.07 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-10.08 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E24.1; SC-M08-004/E24.2; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E7.1; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; RULE-M08-001 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-10.09 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E8.1; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; SC-M08-008/E20.2; SC-M08-010/E18.2; RULE-M08-001 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-10.10 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E23.1; SC-M08-004/E23.2; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E9.1; SC-M08-008/E10.1; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-10.11 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-11.01 | SC-M08-009/M1; SC-M08-009/M2; SC-M08-009/E1.1; SC-M08-009/E2.1; SC-M08-009/E3.1; SC-M08-009/E3.2; SC-M08-009/E4.1; SC-M08-009/E4.2; SC-M08-009/E5.1; SC-M08-009/E5.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-11.02 | SC-M08-009/M2; SC-M08-009/E3.2; SC-M08-009/E4.2; SC-M08-009/E5.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-11.03 | SC-M08-009/M2; SC-M08-009/E2.1; SC-M08-009/E3.2; SC-M08-009/E4.2; SC-M08-009/E5.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt; GAP002 bỏ AI tại số lần 0 |
| FR-M08-11.04 | SC-M08-009/M2; SC-M08-009/E2.1; SC-M08-009/E3.2; SC-M08-009/E4.2; SC-M08-009/E5.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-11.05 | SC-M08-009/M2; SC-M08-009/E2.1; SC-M08-009/E3.2; SC-M08-009/E4.2; SC-M08-009/E5.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-12.01 | AUT-M08-005; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-12.02 | AUT-M08-005; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-12.03 | AUT-M08-005; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-12.04 | AUT-M08-005; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-12.05 | AUT-M08-005; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-13.01 | SC-M08-012/M1; SC-M08-012/M2; SC-M08-012/E2.1; SC-M08-012/E3.1; SC-M08-012/E4.1; SC-M08-012/E4.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-13.02 | SC-M08-012/M2; SC-M08-012/E1.1; SC-M08-012/E2.1; SC-M08-012/E4.2; SC-M08-012/E5.1; SC-M08-012/E5.2; SC-M08-012/E6.1; SC-M08-012/E6.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-13.03 | SC-M08-012/M2; SC-M08-012/E1.1; SC-M08-012/E2.1; SC-M08-012/E5.2; SC-M08-012/E6.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14.01 | SC-M08-004/E9.1; SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-008/E9.2; SC-M08-008/E9.3; SC-M08-010/M1; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E11.4; SC-M08-010/E12.1; SC-M08-010/E12.2; SC-M08-010/E13.1; SC-M08-010/E13.2; SC-M08-010/E14.1; SC-M08-010/E14.2; SC-M08-010/E15.1; SC-M08-010/E15.2; SC-M08-010/E16.1; SC-M08-010/E16.2; SC-M08-010/E17.1; SC-M08-010/E18.1; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14.02 | SC-M08-004/E9.2; SC-M08-004/E10.1; SC-M08-004/E10.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.1; SC-M08-010/E3.2; SC-M08-010/E6.4; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14.03 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14.04 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; AUT-M08-007; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14.05 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14.06 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14.07 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14.08 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; AUT-M08-008; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14.09 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-004/E24.1; SC-M08-004/E24.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E4.1; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; RULE-M08-001; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14.10 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-008/E9.3; SC-M08-008/E20.2; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E5.1; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; SC-M08-010/E18.2; RULE-M08-001; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14.11 | SC-M08-004/E8.2; SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-004/E14.8; SC-M08-004/E23.1; SC-M08-004/E23.2; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E5.4; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E9.1; SC-M08-008/E9.3; SC-M08-008/E10.1; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; AUT-M08-004; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14.12 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14.13 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-004/E25.1; SC-M08-004/E25.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.1; SC-M08-010/E6.5; SC-M08-010/E7.1; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-14.14 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-15.01 | SC-M08-010/E6.2; SC-M08-010/E6.3; SC-M08-011/M1; SC-M08-011/M2; SC-M08-011/E2.1; SC-M08-011/E2.2; SC-M08-011/E3.1; SC-M08-011/E3.2; SC-M08-011/E4.1; SC-M08-011/E4.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-15.02 | SC-M08-010/E6.3; SC-M08-011/M2; SC-M08-011/E2.2; SC-M08-011/E3.2; SC-M08-011/E4.2; AUT-M08-007; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-15.03 | SC-M08-011/M2; SC-M08-011/E1.1; SC-M08-011/E2.2; SC-M08-011/E3.2; SC-M08-011/E4.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-15.04 | SC-M08-011/M2; SC-M08-011/E2.2; SC-M08-011/E3.2; SC-M08-011/E4.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-15.05 | SC-M08-010/E6.2; SC-M08-010/E6.3; SC-M08-011/M1; SC-M08-011/M2; SC-M08-011/E2.1; SC-M08-011/E2.2; SC-M08-011/E3.1; SC-M08-011/E3.2; SC-M08-011/E4.1; SC-M08-011/E4.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-16.01 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; SC-M08-016/M2; SC-M08-016/M4; SC-M08-016/E2.2; SC-M08-016/E3.2; SC-M08-016/E3.4; SC-M08-016/E4.2; SC-M08-016/E5.2; SC-M08-016/E6.2; AUT-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-16.02 | SC-M08-016/M2; SC-M08-016/E3.2; SC-M08-016/E4.2; SC-M08-016/E5.2; SC-M08-016/E6.2; AUT-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-16.03 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; SC-M08-016/M2; SC-M08-016/M4; SC-M08-016/E2.2; SC-M08-016/E3.2; SC-M08-016/E3.4; SC-M08-016/E4.2; SC-M08-016/E5.2; SC-M08-016/E6.2; SC-M08-016/E6.4; AUT-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-16.04 | SC-M08-016/M2; SC-M08-016/M4; SC-M08-016/E2.2; SC-M08-016/E3.2; SC-M08-016/E3.4; SC-M08-016/E4.2; SC-M08-016/E5.2; SC-M08-016/E6.2; SC-M08-016/E6.3; SC-M08-016/E6.4; AUT-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-16.05 | SC-M08-009/M2; SC-M08-009/E2.1; SC-M08-009/E3.2; SC-M08-009/E4.2; SC-M08-009/E5.2; SC-M08-010/E6.3; SC-M08-011/M2; SC-M08-011/E2.2; SC-M08-011/E3.2; SC-M08-011/E4.2; SC-M08-015/M2; SC-M08-015/E2.2; SC-M08-015/E3.2; SC-M08-015/E4.2; SC-M08-016/M2; SC-M08-016/E3.2; SC-M08-016/E4.2; SC-M08-016/E5.2; SC-M08-016/E6.2; AUT-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-16.06 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; SC-M08-016/M2; SC-M08-016/M4; SC-M08-016/E2.2; SC-M08-016/E3.2; SC-M08-016/E3.4; SC-M08-016/E4.2; SC-M08-016/E5.2; SC-M08-016/E6.2; SC-M08-016/E6.4; AUT-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-16.07 | SC-M08-003/M2; SC-M08-003/E5.2; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-003/E8.2; SC-M08-004/E20.3; SC-M08-005/E10.1; SC-M08-005/E10.3; SC-M08-006/E10.3; SC-M08-007/E7.1; SC-M08-007/E7.3; SC-M08-008/E14.1; SC-M08-008/E14.3; SC-M08-010/E11.1; SC-M08-010/E11.3; SC-M08-013/E4.1; SC-M08-013/E4.3; SC-M08-014/E3.1; SC-M08-014/E3.3; SC-M08-016/M2; SC-M08-016/E3.2; SC-M08-016/E4.2; SC-M08-016/E5.2; SC-M08-016/E6.2; AUT-M08-001; AUT-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-17.01 | SC-M08-016/M2; SC-M08-016/E3.2; SC-M08-016/E4.2; SC-M08-016/E5.2; SC-M08-016/E6.1; SC-M08-016/E6.2; SC-M08-016/E6.4 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-17.02 | SC-M08-016/M1; SC-M08-016/M2; SC-M08-016/M3; SC-M08-016/M4; SC-M08-016/E3.1; SC-M08-016/E3.2; SC-M08-016/E3.3; SC-M08-016/E3.4; SC-M08-016/E4.1; SC-M08-016/E4.2; SC-M08-016/E5.1; SC-M08-016/E5.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-17.03 | SC-M08-016/M2; SC-M08-016/E1.1; SC-M08-016/E2.1; SC-M08-016/E2.2; SC-M08-016/E3.2; SC-M08-016/E4.2; SC-M08-016/E5.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-17.04 | SC-M08-016/M2; SC-M08-016/M4; SC-M08-016/E1.1; SC-M08-016/E2.2; SC-M08-016/E3.2; SC-M08-016/E3.4; SC-M08-016/E4.2; SC-M08-016/E5.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-17.05 | SC-M08-016/M2; SC-M08-016/E3.2; SC-M08-016/E4.2; SC-M08-016/E5.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-17.06 | SC-M08-016/M2; SC-M08-016/E3.2; SC-M08-016/E4.2; SC-M08-016/E5.2; SC-M08-016/E6.3; SC-M08-016/E6.4 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-18.01 | SC-M08-004/E11.5; SC-M08-004/E11.6; SC-M08-004/E12.6; SC-M08-004/E27.6; SC-M08-013/M1; SC-M08-013/M2; SC-M08-013/E1.1; SC-M08-013/E4.4; SC-M08-013/E5.1; SC-M08-013/E5.2; SC-M08-013/E6.1; SC-M08-013/E6.2; SC-M08-013/E7.1; SC-M08-013/E7.2; SC-M08-014/M2; SC-M08-014/E4.2; SC-M08-014/E5.2; SC-M08-014/E6.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-18.02 | SC-M08-004/E11.6; SC-M08-004/E12.6; SC-M08-004/E27.6; SC-M08-013/M2; SC-M08-013/E1.1; SC-M08-013/E5.2; SC-M08-013/E6.2; SC-M08-013/E7.2; SC-M08-014/M2; SC-M08-014/E4.2; SC-M08-014/E5.2; SC-M08-014/E6.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-18.03 | SC-M08-004/E11.6; SC-M08-004/E12.6; SC-M08-004/E27.6; SC-M08-013/M2; SC-M08-013/E1.1; SC-M08-013/E5.2; SC-M08-013/E6.2; SC-M08-013/E7.2; SC-M08-014/M2; SC-M08-014/E4.2; SC-M08-014/E5.2; SC-M08-014/E6.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-18.04 | SC-M08-004/E11.6; SC-M08-004/E12.5; SC-M08-004/E12.6; SC-M08-004/E27.5; SC-M08-004/E27.6; SC-M08-013/M2; SC-M08-013/E5.2; SC-M08-013/E6.2; SC-M08-013/E7.2; SC-M08-014/M1; SC-M08-014/M2; SC-M08-014/E3.4; SC-M08-014/E4.1; SC-M08-014/E4.2; SC-M08-014/E5.1; SC-M08-014/E5.2; SC-M08-014/E6.1; SC-M08-014/E6.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-18.05 | SC-M08-004/E11.6; SC-M08-004/E12.6; SC-M08-004/E27.6; SC-M08-013/M2; SC-M08-013/E5.2; SC-M08-013/E6.2; SC-M08-013/E7.2; SC-M08-014/M2; SC-M08-014/E4.2; SC-M08-014/E5.2; SC-M08-014/E6.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-18.06 | SC-M08-004/E11.6; SC-M08-004/E12.6; SC-M08-004/E27.6; SC-M08-013/M2; SC-M08-013/E5.2; SC-M08-013/E6.2; SC-M08-013/E7.2; SC-M08-014/M2; SC-M08-014/E4.2; SC-M08-014/E5.2; SC-M08-014/E6.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-18.07 | SC-M08-004/E11.6; SC-M08-004/E12.6; SC-M08-004/E27.6; SC-M08-013/M2; SC-M08-013/E5.2; SC-M08-013/E6.2; SC-M08-013/E7.2; SC-M08-014/M2; SC-M08-014/E4.2; SC-M08-014/E5.2; SC-M08-014/E6.2; SC-M08-015/M1; SC-M08-015/M2; SC-M08-015/E2.1; SC-M08-015/E2.2; SC-M08-015/E3.1; SC-M08-015/E3.2; SC-M08-015/E4.1; SC-M08-015/E4.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-18.08 | SC-M08-004/E11.6; SC-M08-004/E12.6; SC-M08-004/E27.6; SC-M08-013/M2; SC-M08-013/E1.1; SC-M08-013/E5.2; SC-M08-013/E6.2; SC-M08-013/E7.2; SC-M08-014/M2; SC-M08-014/E4.2; SC-M08-014/E5.2; SC-M08-014/E6.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-18.09 | SC-M08-004/E11.6; SC-M08-004/E12.6; SC-M08-004/E27.6; SC-M08-013/M2; SC-M08-013/E2.1; SC-M08-013/E5.2; SC-M08-013/E6.2; SC-M08-013/E7.2; SC-M08-014/M2; SC-M08-014/E1.1; SC-M08-014/E4.2; SC-M08-014/E5.2; SC-M08-014/E6.2; SC-M08-015/M2; SC-M08-015/E1.1; SC-M08-015/E2.2; SC-M08-015/E3.2; SC-M08-015/E4.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-18.10 | SC-M08-004/E11.6; SC-M08-004/E12.6; SC-M08-004/E27.6; SC-M08-013/M2; SC-M08-013/E5.2; SC-M08-013/E6.2; SC-M08-013/E7.2; SC-M08-014/M2; SC-M08-014/E4.2; SC-M08-014/E5.2; SC-M08-014/E6.2; SC-M08-015/M2; SC-M08-015/E2.2; SC-M08-015/E3.2; SC-M08-015/E4.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M08-18.11 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.1; SC-M08-005/E3.2; SC-M08-005/E4.1; SC-M08-005/E4.2; SC-M08-005/E5.1; SC-M08-005/E5.2; SC-M08-005/E6.1; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; AUT-M08-007; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt; GAP006 Owner thay đổi trong vụ |
| BR-M08-01 | SC-M08-001/M2; SC-M08-001/E18.2; SC-M08-001/E19.2; SC-M08-001/E20.2; SC-M08-012/E4.2; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-02 | SC-M08-001/M2; SC-M08-001/M3; SC-M08-001/E3.2; SC-M08-001/E3.3; SC-M08-001/E4.2; SC-M08-001/E4.3; SC-M08-001/E5.2; SC-M08-001/E5.3; SC-M08-001/E6.1; SC-M08-001/E6.2; SC-M08-001/E7.1; SC-M08-001/E7.2; SC-M08-001/E8.1; SC-M08-001/E8.2; SC-M08-001/E9.1; SC-M08-001/E9.2; SC-M08-001/E10.1; SC-M08-001/E10.2; SC-M08-001/E11.1; SC-M08-001/E11.2; SC-M08-001/E19.2; SC-M08-001/E19.3; SC-M08-001/E20.2; SC-M08-001/E20.3; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-03 | SC-M08-001/M2; SC-M08-001/M3; SC-M08-001/E3.2; SC-M08-001/E4.2; SC-M08-001/E5.2; SC-M08-001/E6.1; SC-M08-001/E6.2; SC-M08-001/E7.1; SC-M08-001/E7.2; SC-M08-001/E8.1; SC-M08-001/E8.2; SC-M08-001/E9.1; SC-M08-001/E9.2; SC-M08-001/E10.1; SC-M08-001/E10.2; SC-M08-001/E11.1; SC-M08-001/E11.2; SC-M08-001/E19.2; SC-M08-001/E19.3; SC-M08-001/E20.2; SC-M08-001/E20.3; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-04 | SC-M08-001/M2; SC-M08-001/M3; SC-M08-001/E3.2; SC-M08-001/E3.3; SC-M08-001/E4.2; SC-M08-001/E4.3; SC-M08-001/E5.2; SC-M08-001/E5.3; SC-M08-001/E6.1; SC-M08-001/E6.2; SC-M08-001/E7.1; SC-M08-001/E7.2; SC-M08-001/E8.1; SC-M08-001/E8.2; SC-M08-001/E9.1; SC-M08-001/E9.2; SC-M08-001/E10.1; SC-M08-001/E10.2; SC-M08-001/E11.1; SC-M08-001/E11.2; SC-M08-001/E19.2; SC-M08-001/E19.3; SC-M08-001/E20.2; SC-M08-001/E20.3; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-05 | SC-M08-001/M4; SC-M08-001/E1.1; SC-M08-001/E2.1; SC-M08-001/E3.4; SC-M08-001/E4.4; SC-M08-001/E5.4; SC-M08-001/E19.4; SC-M08-001/E20.4; SC-M08-003/E2.1; AUT-M08-004; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-06 | SC-M08-001/M4; SC-M08-001/E1.1; SC-M08-001/E2.1; SC-M08-001/E3.4; SC-M08-001/E4.4; SC-M08-001/E5.4; SC-M08-001/E19.4; SC-M08-001/E20.4; SC-M08-002/M2; SC-M08-002/E6.2; SC-M08-002/E7.2; SC-M08-002/E8.2; SC-M08-002/E9.2; SC-M08-004/M2; SC-M08-004/E7.2; SC-M08-004/E11.2; SC-M08-004/E12.2; SC-M08-004/E14.2; SC-M08-004/E16.2; SC-M08-004/E27.2; SC-M08-004/E29.2; SC-M08-004/E30.2; SC-M08-004/E31.2; SC-M08-004/E32.2; AUT-M08-004; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-07 | SC-M08-001/M4; SC-M08-001/E19.4; SC-M08-001/E20.4; SC-M08-002/M2; SC-M08-002/E2.1; SC-M08-002/E6.2; SC-M08-002/E7.2; SC-M08-002/E8.2; SC-M08-002/E9.2; SC-M08-004/M2; SC-M08-004/E7.2; SC-M08-004/E11.2; SC-M08-004/E12.2; SC-M08-004/E14.2; SC-M08-004/E16.2; SC-M08-004/E27.2; SC-M08-004/E29.2; SC-M08-004/E30.2; SC-M08-004/E31.2; SC-M08-004/E32.2; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-08 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-003/M2; SC-M08-003/E1.1; SC-M08-003/E5.2; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-003/E8.2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E2.1; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E19.1; SC-M08-004/E20.1; SC-M08-004/E20.3; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; SC-M08-005/E9.1; SC-M08-005/E10.1; SC-M08-005/E10.3; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E9.1; SC-M08-006/E10.1; SC-M08-006/E10.3; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-007/E6.1; SC-M08-007/E7.1; SC-M08-007/E7.3; SC-M08-008/E13.1; SC-M08-008/E14.1; SC-M08-008/E14.3; SC-M08-010/E10.1; SC-M08-010/E11.1; SC-M08-010/E11.3; SC-M08-013/E3.1; SC-M08-013/E4.1; SC-M08-013/E4.3; SC-M08-014/E2.1; SC-M08-014/E3.1; SC-M08-014/E3.3; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-09 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-003/M2; SC-M08-003/E5.2; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-003/E8.2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E19.1; SC-M08-004/E20.1; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; SC-M08-005/E9.1; SC-M08-005/E10.1; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E9.1; SC-M08-006/E10.1; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-007/E6.1; SC-M08-007/E7.1; SC-M08-008/E13.1; SC-M08-008/E14.1; SC-M08-010/E10.1; SC-M08-010/E11.1; SC-M08-013/E3.1; SC-M08-013/E4.1; SC-M08-014/E2.1; SC-M08-014/E3.1; AUT-M08-001; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-10 | SC-M08-004/M5; SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.1; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.5; SC-M08-004/E29.6; SC-M08-004/E32.5; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-11 | SC-M08-002/M3; SC-M08-002/M4; SC-M08-002/E6.3; SC-M08-002/E6.4; SC-M08-002/E9.3; SC-M08-002/E9.4; SC-M08-004/M4; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-12 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; AUT-M08-007 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-13 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; AUT-M08-007 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-14 | SC-M08-002/M4; SC-M08-002/E1.1; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-004/M4; SC-M08-004/M6; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E7.8; SC-M08-004/E11.4; SC-M08-004/E11.8; SC-M08-004/E12.4; SC-M08-004/E12.8; SC-M08-004/E14.4; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.4; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.4; SC-M08-004/E27.10; SC-M08-004/E29.4; SC-M08-004/E29.6; SC-M08-004/E32.4; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; AUT-M08-007; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-15 | SC-M08-002/M4; SC-M08-002/E1.1; SC-M08-002/E3.1; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-004/M4; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-16 | SC-M08-004/E6.2; SC-M08-004/E7.6; SC-M08-004/E28.2; SC-M08-006/E1.2; SC-M08-006/E11.2; SC-M08-007/M2; SC-M08-007/E1.2; SC-M08-007/E3.1; SC-M08-007/E8.2; SC-M08-007/E9.2; SC-M08-007/E10.2; SC-M08-007/E11.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-17 | SC-M08-001/E3.4; SC-M08-001/E4.4; SC-M08-001/E5.4; SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.1; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-18 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-19 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-004/M4; SC-M08-004/E1.3; SC-M08-004/E7.4; SC-M08-004/E11.4; SC-M08-004/E12.4; SC-M08-004/E14.4; SC-M08-004/E16.4; SC-M08-004/E27.4; SC-M08-004/E29.4; SC-M08-004/E32.4; SC-M08-008/E5.1; RULE-M08-003 | Có vị trí đối soát; chưa phê duyệt; GAP001 tại mẫu số 0 |
| BR-M08-20 | AUT-M08-002; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-21 | AUT-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-22 | SC-M08-006/E6.1; AUT-M08-002 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-23 | SC-M08-004/E13.2; SC-M08-004/E13.4; SC-M08-004/E14.5; SC-M08-004/E16.5; SC-M08-004/E28.1; SC-M08-004/E28.2; SC-M08-006/M2; SC-M08-006/M4; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E4.3; SC-M08-006/E5.2; SC-M08-006/E11.1; SC-M08-006/E11.2; SC-M08-006/E12.2; SC-M08-006/E12.4; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-006/E15.4; AUT-M08-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-24 | AUT-M08-003; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-25 | AUT-M08-002; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-26 | SC-M08-002/E2.1; AUT-M08-002; AUT-M08-003; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-27 | AUT-M08-002; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-28 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; SC-M08-009/M2; SC-M08-009/E2.1; SC-M08-009/E3.2; SC-M08-009/E4.2; SC-M08-009/E5.2; SC-M08-012/M2; SC-M08-012/E2.1; SC-M08-012/E3.1; AUT-M08-003; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-29 | SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; SC-M08-012/M2; SC-M08-012/E2.1; AUT-M08-003; AUT-M08-005; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-30 | SC-M08-012/E3.1; AUT-M08-005; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-31 | SC-M08-001/E17.1; SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; SC-M08-009/M2; SC-M08-009/E3.2; SC-M08-009/E4.2; SC-M08-009/E5.2; SC-M08-012/M2; SC-M08-012/E2.1; AUT-M08-005; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-32 | SC-M08-001/E18.2; SC-M08-004/E8.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; SC-M08-012/M2; SC-M08-012/E1.1; SC-M08-012/E2.1; SC-M08-012/E3.1; SC-M08-012/E4.2; SC-M08-012/E5.2; SC-M08-012/E6.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-33 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; AUT-M08-003; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-34 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.3; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; SC-M08-011/M2; SC-M08-011/E2.2; SC-M08-011/E3.2; SC-M08-011/E4.2; AUT-M08-008; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-35 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-36 | SC-M08-004/E8.2; SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-004/E13.2; SC-M08-004/E14.8; SC-M08-004/E23.1; SC-M08-004/E23.2; SC-M08-004/E27.8; SC-M08-004/E28.2; SC-M08-004/E28.4; SC-M08-006/M2; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E4.6; SC-M08-006/E5.2; SC-M08-006/E5.3; SC-M08-006/E5.4; SC-M08-006/E11.2; SC-M08-006/E11.4; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E9.1; SC-M08-008/E9.3; SC-M08-008/E10.1; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; AUT-M08-003; AUT-M08-004; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt; GAP003 tại lô qua biên HEAVY |
| BR-M08-37 | AUT-M08-008; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-38 | SC-M08-010/E6.3; SC-M08-011/M2; SC-M08-011/E2.2; SC-M08-011/E3.2; SC-M08-011/E4.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-39 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; SC-M08-016/M2; SC-M08-016/M4; SC-M08-016/E3.2; SC-M08-016/E3.4; SC-M08-016/E4.2; SC-M08-016/E5.2; SC-M08-016/E6.2; AUT-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-40 | SC-M08-004/M6; SC-M08-004/E7.8; SC-M08-004/E11.8; SC-M08-004/E12.8; SC-M08-004/E14.10; SC-M08-004/E15.2; SC-M08-004/E16.8; SC-M08-004/E26.4; SC-M08-004/E27.10; SC-M08-004/E29.6; SC-M08-004/E32.6; SC-M08-005/M2; SC-M08-005/E3.2; SC-M08-005/E4.2; SC-M08-005/E5.2; SC-M08-005/E6.2; SC-M08-005/E11.2; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-005/E14.2; SC-M08-016/M2; SC-M08-016/M4; SC-M08-016/E2.2; SC-M08-016/E3.2; SC-M08-016/E3.4; SC-M08-016/E4.2; SC-M08-016/E5.2; SC-M08-016/E6.2; SC-M08-016/E6.4; AUT-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-41 | SC-M08-016/M2; SC-M08-016/M4; SC-M08-016/E1.1; SC-M08-016/E2.2; SC-M08-016/E3.2; SC-M08-016/E3.4; SC-M08-016/E4.2; SC-M08-016/E5.2; SC-M08-016/E6.2; SC-M08-016/E6.4 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-42 | RULE-M08-004; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-43 | SC-M08-004/E8.2; SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E9.3; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; SC-M08-012/M2; SC-M08-012/E2.1; SC-M08-016/M4; SC-M08-016/E3.4; AUT-M08-005; AUT-M08-008; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-44 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E7.2; SC-M08-002/E8.2; SC-M08-002/E9.4; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-004/M2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E7.2; SC-M08-004/E7.4; SC-M08-004/E11.2; SC-M08-004/E11.4; SC-M08-004/E11.6; SC-M08-004/E12.2; SC-M08-004/E12.4; SC-M08-004/E12.6; SC-M08-004/E13.2; SC-M08-004/E14.2; SC-M08-004/E14.4; SC-M08-004/E16.2; SC-M08-004/E16.4; SC-M08-004/E27.2; SC-M08-004/E27.4; SC-M08-004/E27.6; SC-M08-004/E29.2; SC-M08-004/E29.4; SC-M08-004/E30.2; SC-M08-004/E31.2; SC-M08-004/E32.2; SC-M08-004/E32.4; SC-M08-005/E12.2; SC-M08-005/E13.2; SC-M08-006/M2; SC-M08-006/E2.2; SC-M08-006/E3.2; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-007/E9.2; SC-M08-007/E10.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-009/E4.2; SC-M08-009/E5.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-011/E3.2; SC-M08-011/E4.2; SC-M08-013/M2; SC-M08-013/E5.2; SC-M08-013/E6.2; SC-M08-013/E7.2; SC-M08-014/M2; SC-M08-014/E4.2; SC-M08-014/E5.2; SC-M08-014/E6.2; SC-M08-015/E3.2; SC-M08-015/E4.2; SC-M08-016/E4.2; SC-M08-016/E5.2; RULE-M08-001; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-45 | SC-M08-001/E17.1; RULE-M08-002; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-46 | SC-M08-001/E12.1; SC-M08-001/E13.1; SC-M08-001/E14.1; SC-M08-001/E15.1; SC-M08-001/E16.1; SC-M08-002/M2; SC-M08-002/M4; SC-M08-002/E4.1; SC-M08-002/E5.1; SC-M08-002/E6.2; SC-M08-002/E6.4; SC-M08-002/E7.2; SC-M08-002/E8.2; SC-M08-002/E9.2; SC-M08-002/E9.4; SC-M08-002/E10.2; SC-M08-003/M2; SC-M08-003/E3.1; SC-M08-003/E4.1; SC-M08-003/E5.2; SC-M08-003/E6.2; SC-M08-003/E7.2; SC-M08-003/E8.2; SC-M08-003/E9.2; SC-M08-004/M2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E7.2; SC-M08-004/E7.4; SC-M08-004/E8.2; SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-004/E11.2; SC-M08-004/E11.4; SC-M08-004/E12.2; SC-M08-004/E12.4; SC-M08-004/E13.2; SC-M08-004/E14.2; SC-M08-004/E14.4; SC-M08-004/E14.8; SC-M08-004/E16.2; SC-M08-004/E16.4; SC-M08-004/E17.1; SC-M08-004/E18.1; SC-M08-004/E24.1; SC-M08-004/E24.2; SC-M08-004/E27.2; SC-M08-004/E27.4; SC-M08-004/E27.8; SC-M08-004/E28.2; SC-M08-004/E28.4; SC-M08-004/E29.2; SC-M08-004/E29.4; SC-M08-004/E30.2; SC-M08-004/E31.2; SC-M08-004/E32.2; SC-M08-004/E32.4; SC-M08-004/E33.2; SC-M08-005/E7.1; SC-M08-005/E8.1; SC-M08-005/E15.2; SC-M08-006/M2; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E4.6; SC-M08-006/E5.2; SC-M08-006/E7.1; SC-M08-006/E8.1; SC-M08-006/E11.2; SC-M08-006/E11.4; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-006/E16.2; SC-M08-007/E4.1; SC-M08-007/E5.1; SC-M08-007/E12.2; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E7.1; SC-M08-008/E8.1; SC-M08-008/E9.3; SC-M08-008/E11.1; SC-M08-008/E12.1; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; SC-M08-008/E19.2; SC-M08-008/E20.2; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E4.1; SC-M08-010/E5.1; SC-M08-010/E6.5; SC-M08-010/E8.1; SC-M08-010/E9.1; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; SC-M08-010/E17.2; SC-M08-010/E18.2; AUT-M08-003; RULE-M08-001 | Có vị trí đối soát; chưa phê duyệt; GAP004 tự nhắm nhóm |
| BR-M08-47 | SC-M08-001/M2; SC-M08-001/M4; SC-M08-001/E2.1; SC-M08-001/E3.2; SC-M08-001/E4.2; SC-M08-001/E5.2; SC-M08-001/E12.1; SC-M08-001/E13.1; SC-M08-001/E14.1; SC-M08-001/E15.1; SC-M08-001/E16.1; SC-M08-001/E17.1; SC-M08-001/E19.2; SC-M08-001/E19.4; SC-M08-001/E20.2; SC-M08-001/E20.4; RULE-M08-002 | Có vị trí đối soát; chưa phê duyệt; GAP004 tự nhắm nhóm |
| BR-M08-48 | SC-M08-002/M4; SC-M08-002/E6.4; SC-M08-002/E9.4; SC-M08-004/M2; SC-M08-004/M4; SC-M08-004/E1.1; SC-M08-004/E1.3; SC-M08-004/E6.2; SC-M08-004/E7.2; SC-M08-004/E7.4; SC-M08-004/E7.6; SC-M08-004/E8.2; SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-004/E11.2; SC-M08-004/E11.4; SC-M08-004/E11.6; SC-M08-004/E12.2; SC-M08-004/E12.4; SC-M08-004/E12.6; SC-M08-004/E13.2; SC-M08-004/E13.4; SC-M08-004/E14.2; SC-M08-004/E14.4; SC-M08-004/E14.8; SC-M08-004/E16.2; SC-M08-004/E16.4; SC-M08-004/E19.1; SC-M08-004/E20.1; SC-M08-004/E27.2; SC-M08-004/E27.4; SC-M08-004/E27.6; SC-M08-004/E27.8; SC-M08-004/E28.2; SC-M08-004/E28.4; SC-M08-004/E29.2; SC-M08-004/E29.4; SC-M08-004/E30.2; SC-M08-004/E31.2; SC-M08-004/E32.2; SC-M08-004/E32.4; SC-M08-005/E9.1; SC-M08-005/E10.1; SC-M08-006/M2; SC-M08-006/M4; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E4.6; SC-M08-006/E5.2; SC-M08-006/E9.1; SC-M08-006/E10.1; SC-M08-006/E11.2; SC-M08-006/E11.4; SC-M08-006/E12.2; SC-M08-006/E12.4; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; SC-M08-006/E15.4; SC-M08-007/M2; SC-M08-007/E1.2; SC-M08-007/E6.1; SC-M08-007/E7.1; SC-M08-007/E8.2; SC-M08-007/E9.2; SC-M08-007/E10.2; SC-M08-007/E11.2; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E9.3; SC-M08-008/E13.1; SC-M08-008/E14.1; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E10.1; SC-M08-010/E11.1; SC-M08-010/E12.1; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; SC-M08-011/M2; SC-M08-011/E2.2; SC-M08-011/E3.2; SC-M08-011/E4.2; SC-M08-013/M2; SC-M08-013/E3.1; SC-M08-013/E4.1; SC-M08-013/E5.2; SC-M08-013/E6.2; SC-M08-013/E7.2; SC-M08-014/M2; SC-M08-014/E2.1; SC-M08-014/E3.1; SC-M08-014/E4.2; SC-M08-014/E5.2; SC-M08-014/E6.2; SC-M08-015/M2; SC-M08-015/E2.2; SC-M08-015/E3.2; SC-M08-015/E4.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-49 | SC-M08-004/E13.2; SC-M08-004/E28.2; SC-M08-006/M2; SC-M08-006/E1.1; SC-M08-006/E1.2; SC-M08-006/E2.2; SC-M08-006/E2.3; SC-M08-006/E2.4; SC-M08-006/E3.2; SC-M08-006/E3.3; SC-M08-006/E3.4; SC-M08-006/E4.2; SC-M08-006/E5.2; SC-M08-006/E5.4; SC-M08-006/E11.2; SC-M08-006/E12.2; SC-M08-006/E13.2; SC-M08-006/E14.2; SC-M08-006/E15.2; AUT-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-50 | SC-M08-001/E3.2; SC-M08-001/E3.4; SC-M08-001/E4.2; SC-M08-001/E4.4; SC-M08-001/E5.2; SC-M08-001/E5.4; SC-M08-004/E11.6; SC-M08-004/E12.6; SC-M08-004/E27.6; SC-M08-004/E27.7; SC-M08-008/E6.1; SC-M08-010/E12.1; SC-M08-013/M2; SC-M08-013/E1.1; SC-M08-013/E2.1; SC-M08-013/E5.2; SC-M08-013/E6.2; SC-M08-013/E7.2; SC-M08-014/M2; SC-M08-014/E1.1; SC-M08-014/E4.2; SC-M08-014/E5.2; SC-M08-014/E6.2; SC-M08-015/M2; SC-M08-015/E1.1; SC-M08-015/E2.2; SC-M08-015/E3.2; SC-M08-015/E4.2; RULE-M08-006 | Có vị trí đối soát; chưa phê duyệt; GAP004 tự nhắm nhóm; GAP006 Owner thay đổi trong vụ |
| BR-M08-51 | AUT-M08-002; AUT-M08-004; RULE-M08-004 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-52 | SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-004/E25.1; SC-M08-004/E25.2; SC-M08-008/E9.3; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.1; SC-M08-010/E6.5; SC-M08-010/E7.1; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-53 | SC-M08-004/E8.2; SC-M08-004/E9.2; SC-M08-004/E10.2; SC-M08-004/E14.8; SC-M08-004/E27.8; SC-M08-004/E28.4; SC-M08-006/E4.6; SC-M08-006/E11.4; SC-M08-008/M2; SC-M08-008/E1.1; SC-M08-008/E2.1; SC-M08-008/E3.1; SC-M08-008/E4.1; SC-M08-008/E5.2; SC-M08-008/E6.2; SC-M08-008/E9.3; SC-M08-008/E15.2; SC-M08-008/E16.2; SC-M08-008/E17.2; SC-M08-008/E18.2; SC-M08-010/M2; SC-M08-010/E1.1; SC-M08-010/E2.1; SC-M08-010/E3.2; SC-M08-010/E6.5; SC-M08-010/E12.2; SC-M08-010/E13.2; SC-M08-010/E14.2; SC-M08-010/E15.2; SC-M08-010/E16.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M08-54 | SC-M08-006/E6.1; SC-M08-009/M2; SC-M08-009/E2.1; SC-M08-009/E3.2; SC-M08-009/E4.2; SC-M08-009/E5.2; RULE-M08-005 | Có vị trí đối soát; chưa phê duyệt; GAP002 bỏ AI tại số lần 0 |
| BR-M08-55 | SC-M08-001/M2; SC-M08-001/E12.1; SC-M08-001/E13.1; SC-M08-001/E14.1; SC-M08-001/E15.1; SC-M08-001/E16.1; SC-M08-001/E19.2; SC-M08-001/E20.2; SC-M08-001/E21.2; SC-M08-002/E10.2; SC-M08-003/E9.2; SC-M08-004/E33.2; SC-M08-005/E15.2; SC-M08-006/E16.2; SC-M08-007/E12.2; SC-M08-008/E8.1; SC-M08-008/E19.2; SC-M08-008/E20.2; SC-M08-010/E5.1; SC-M08-010/E17.2; SC-M08-010/E18.2; AUT-M08-002; AUT-M08-003; RULE-M08-001 | Có vị trí đối soát; chưa phê duyệt |


| UC owner | Guard/lựa chọn | Nhánh | Đích |
|---|---|---|---|
| UC-M08-020 | Đã có vụ Mở cho P81, Lan chưa có báo cáo trong vụ đó | SC-M08-001/E1 | END:SUCCESS |
| UC-M08-020 | Chỉ có vụ cũ Đã xử lý, không còn vụ Mở của P81 | SC-M08-001/E2 | END:SUCCESS |
| UC-M08-020 | Lan báo cáo comment thay bài viết | SC-M08-001/E3 | END:SUCCESS |
| UC-M08-020 | Lan báo cáo account thay bài viết | SC-M08-001/E4 | END:SUCCESS |
| UC-M08-020 | Lan báo cáo group thay bài viết | SC-M08-001/E5 | END:SUCCESS |
| UC-M08-020 | Chưa chọn lý do | SC-M08-001/E6 | M4 |
| UC-M08-020 | Chọn Khác nhưng không có mô tả | SC-M08-001/E7 | M4 |
| UC-M08-020 | Chọn hơn một lý do | SC-M08-001/E8 | M4 |
| UC-M08-020 | Đính kèm ảnh thứ tư | SC-M08-001/E9 | M4 |
| UC-M08-020 | Một ảnh quá 5MB | SC-M08-001/E10 | M4 |
| UC-M08-020 | Ảnh không đúng định dạng | SC-M08-001/E11 | M4 |
| UC-M08-020 | Target trong nhóm Private mà Lan không là thành viên | SC-M08-001/E12 | END:REJECTED |
| UC-M08-020 | Target đã không còn nhìn thấy khi gửi | SC-M08-001/E13 | END:REJECTED |
| UC-M08-020 | Tự báo cáo bài, bình luận hoặc tài khoản mình | SC-M08-001/E14 | END:REJECTED |
| UC-M08-020 | Lan đã báo cáo cùng target trong vụ Mở | SC-M08-001/E15 | END:REJECTED |
| UC-M08-020 | Target là bài, bình luận, tài khoản Admin hoặc nhóm Owner Admin | SC-M08-001/E16 | END:REJECTED |
| UC-M08-020 | Lan đang HEAVY và P81 Khóa toàn bộ nhưng vẫn được nhìn thấy | SC-M08-001/E17 | END:SUCCESS |
| UC-M08-003 | Nội dung vụ đã tự ẩn, xóa hoặc xóa vĩnh viễn nhưng có bản lưu đúng ngữ cảnh | SC-M08-002/E1 | END:SUCCESS |
| UC-M08-003 | AI tổng hoặc Moderation đang tắt | SC-M08-002/E2 | M3 |
| UC-M08-003 | Đòi duyệt nội dung người khác đã xóa/ẩn ngoài vụ, lịch sử hoặc khiếu nại liên quan | SC-M08-002/E3 | END:REJECTED |
| UC-M08-003 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | SC-M08-002/E4 | END:REJECTED |
| UC-M08-003 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | SC-M08-002/E5 | END:REJECTED |
| UC-M08-004 | Vụ do người khác giữ | SC-M08-003/E1 | END:REJECTED |
| UC-M08-004 | Vụ đã được kết luận trước lúc nhận | SC-M08-003/E2 | END:REJECTED |
| UC-M08-004 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | SC-M08-003/E3 | END:REJECTED |
| UC-M08-004 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | SC-M08-003/E4 | END:REJECTED |
| UC-M08-021 | Mai đã là người giữ hợp lệ lúc chọn giải quyết | SC-M08-004/E1 | M5 |
| UC-M08-021 | Người khác nhận K81 trước lúc xử lý yêu cầu nhận của Mai | SC-M08-004/E2 | END:REJECTED |
| UC-M08-021 | Vụ đã đóng trước lúc Mai nhận | SC-M08-004/E3 | END:REJECTED |
| UC-M08-021 | Thiếu lý do kết luận; quyền giữ/vụ vẫn hợp lệ | SC-M08-004/E4 | M6 |
| UC-M08-021 | Vụ đã được đóng trước xử lý kết luận | SC-M08-004/E5 | END:REJECTED |
| UC-M08-021 | Tại EP-CASE-ACTION, người giữ chọn Ẩn bài vi phạm với target đúng vụ và guard của biện pháp hợp lệ | SC-M08-004/E6 | M5 |
| UC-M08-021 | Chọn từ đầu vụ về C81 với mọi guard nhận/biện pháp/kết luận hợp lệ; Tại EP-CASE-ACTION, người giữ chọn Ẩn bình luận vi phạm với target đúng vụ và guard của biện pháp hợp lệ | SC-M08-004/E7 | END:SUCCESS |
| UC-M08-021 | Tại EP-CASE-ACTION, người giữ chọn Cảnh cáo tác giả theo đánh giá con người với target đúng vụ và guard của biện pháp hợp lệ | SC-M08-004/E8 | M5 |
| UC-M08-021 | Tại EP-CASE-ACTION, người giữ chọn Ban theo lịch sử với target đúng vụ và guard của biện pháp hợp lệ | SC-M08-004/E9 | M5 |
| UC-M08-021 | Tại EP-CASE-ACTION, người giữ chọn Ban vĩnh viễn thủ công với target đúng vụ và guard của biện pháp hợp lệ | SC-M08-004/E10 | M5 |
| UC-M08-021 | Chọn từ đầu vụ về G81 với mọi guard nhận/biện pháp/kết luận hợp lệ; Tại EP-CASE-ACTION, người giữ chọn Ẩn nhóm vi phạm với target đúng vụ và guard của biện pháp hợp lệ | SC-M08-004/E11 | END:SUCCESS |
| UC-M08-021 | Chọn từ đầu vụ về G81 với mọi guard nhận/biện pháp/kết luận hợp lệ; Tại EP-CASE-ACTION, người giữ chọn Khóa nhóm vi phạm với target đúng vụ và guard của biện pháp hợp lệ | SC-M08-004/E12 | END:SUCCESS |
| UC-M08-021 | Tại EP-CASE-ACTION, người giữ chọn Xét bài đang bị gắn cờ, quyết định không vi phạm với target đúng vụ và guard của biện pháp hợp lệ | SC-M08-004/E13 | M5 |
| UC-M08-021 | Chọn từ đầu vụ về C81 với mọi guard nhận/biện pháp/kết luận hợp lệ; Tại EP-CASE-ACTION, người giữ chọn Xét comment trung bình và chọn cảnh cáo với target đúng vụ và guard của biện pháp hợp lệ | SC-M08-004/E14 | END:SUCCESS |
| UC-M08-021 | Đã áp biện pháp đối với người bị báo cáo/nội dung/nhóm và Mai chọn Có xử lý để hoàn tất vụ | SC-M08-004/E15 | END:SUCCESS |
| UC-M08-021 | Chọn từ đầu vụ về C81 với mọi guard nhận/biện pháp/kết luận hợp lệ; Chỉ xét nội dung đang chờ và xác định vi phạm, không chọn cảnh cáo | SC-M08-004/E16 | END:SUCCESS |
| UC-M08-021 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | SC-M08-004/E17 | END:REJECTED |
| UC-M08-021 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | SC-M08-004/E18 | END:REJECTED |
| UC-M08-021 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | SC-M08-004/E19 | END:REJECTED |
| UC-M08-021 | Vụ tự nhả 30 phút, còn Mở/chưa ai giữ và Mai chọn nhận lại trước tiếp tục | SC-M08-004/E20 | M5 |
| UC-M08-021 | Tại EP-CASE-ACTION, Nội dung đã ẩn khi người giữ chọn biện pháp | SC-M08-004/E21 | M5 |
| UC-M08-021 | Tại EP-CASE-ACTION, Nội dung không còn chờ xét khi người giữ chọn biện pháp | SC-M08-004/E22 | M5 |
| UC-M08-021 | Tại EP-CASE-ACTION, Target đã HEAVY khi người giữ chọn biện pháp | SC-M08-004/E23 | M5 |
| UC-M08-021 | Tại EP-CASE-ACTION, Mod đòi chế tài Mod khác khi người giữ chọn biện pháp | SC-M08-004/E24 | M5 |
| UC-M08-021 | Tại EP-CASE-ACTION, Target có ban Đang hiệu lực khi người giữ chọn biện pháp | SC-M08-004/E25 | M5 |
| UC-M08-021 | Sau biện pháp hợp lệ, Mai chọn Có xử lý nhưng quên lý do | SC-M08-004/E26 | END:SUCCESS |
| UC-M08-021 | Vụ từ đầu về nhóm G81, người giữ chọn Khóa nhóm rồi cảnh cáo Owner Bình USER (khác Mai, chưa HEAVY) | SC-M08-004/E27 | END:SUCCESS |
| UC-M08-021 | Vụ P81 từ đầu, tại EP-CASE-ACTION Mai xét bài gắn cờ điểm trung bình và chọn Ẩn bài + cảnh cáo tác giả | SC-M08-004/E28 | M5 |
| UC-M08-005 | Thiếu lý do kết luận; quyền giữ/vụ vẫn hợp lệ | SC-M08-005/E1 | M2 |
| UC-M08-005 | Vụ đã được đóng trước xử lý kết luận | SC-M08-005/E2 | END:REJECTED |
| UC-M08-005 | Mai kết luận Có xử lý sau biện pháp hợp lệ với bài viết | SC-M08-005/E3 | END:SUCCESS |
| UC-M08-005 | Mai kết luận Có xử lý sau biện pháp hợp lệ với bình luận | SC-M08-005/E4 | END:SUCCESS |
| UC-M08-005 | Mai kết luận Có xử lý sau biện pháp hợp lệ với nhóm | SC-M08-005/E5 | END:SUCCESS |
| UC-M08-005 | Mai kết luận Có xử lý sau biện pháp hợp lệ với tài khoản | SC-M08-005/E6 | END:SUCCESS |
| UC-M08-005 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | SC-M08-005/E7 | END:REJECTED |
| UC-M08-005 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | SC-M08-005/E8 | END:REJECTED |
| UC-M08-005 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | SC-M08-005/E9 | END:REJECTED |
| UC-M08-005 | Quyền giữ đã tự nhả sau đủ 30 phút không hoạt động; K81 vẫn Mở/chưa ai nhận, Mai còn đủ phạm vi và chọn nhận lại | SC-M08-005/E10 | M2 |
| UC-M08-007 | Chọn Ẩn bài đối với P81 | SC-M08-006/E1 | END:SUCCESS |
| UC-M08-007 | Ngay từ đầu chọn xét C81 AI trung bình trong vụ C81, không phải P81; Chọn Không vi phạm đối với C81 | SC-M08-006/E2 | END:SUCCESS |
| UC-M08-007 | Ngay từ đầu chọn xét C81 AI trung bình trong vụ C81, không phải P81; Chọn Vi phạm, không cảnh cáo đối với C81 | SC-M08-006/E3 | END:SUCCESS |
| UC-M08-007 | Ngay từ đầu chọn xét C81 AI trung bình trong vụ C81, không phải P81; Comment điểm trung bình được xác định vi phạm và Mai chọn cảnh cáo tác giả | SC-M08-006/E4 | END:SUCCESS |
| UC-M08-007 | Ngay từ đầu chọn xét C81 AI trung bình trong vụ C81, không phải P81; Target đã HEAVY và staff xác định vi phạm nội dung trung bình | SC-M08-006/E5 | END:SUCCESS |
| UC-M08-007 | Nội dung không còn chờ xét hoặc không thuộc loại được xét lại | SC-M08-006/E6 | END:REJECTED |
| UC-M08-007 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | SC-M08-006/E7 | END:REJECTED |
| UC-M08-007 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | SC-M08-006/E8 | END:REJECTED |
| UC-M08-007 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | SC-M08-006/E9 | END:REJECTED |
| UC-M08-007 | Vụ tự nhả 30 phút, còn Mở/chưa ai giữ và Mai chọn nhận lại trước tiếp tục | SC-M08-006/E10 | M3 |
| UC-M08-007 | P81 đang gắn cờ, điểm trung bình, Mai chọn Ẩn bài rồi cảnh cáo tác giả đủ điều kiện | SC-M08-006/E11 | END:SUCCESS |
| UC-M08-008 | Mai chọn ẩn bình luận thay bài viết | SC-M08-007/E1 | END:SUCCESS |
| UC-M08-008 | Nội dung đã Bị ẩn | SC-M08-007/E2 | END:REJECTED |
| UC-M08-008 | Yêu cầu xóa nội dung người khác thay thao tác Ẩn | SC-M08-007/E3 | END:REJECTED |
| UC-M08-008 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | SC-M08-007/E4 | END:REJECTED |
| UC-M08-008 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | SC-M08-007/E5 | END:REJECTED |
| UC-M08-008 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | SC-M08-007/E6 | END:REJECTED |
| UC-M08-008 | Quyền giữ đã tự nhả sau đủ 30 phút không hoạt động; K81 vẫn Mở/chưa ai nhận, Mai còn đủ phạm vi và chọn nhận lại | SC-M08-007/E7 | M2 |
| UC-M08-009 | Target chưa HEAVY, số lần hiện tại 0 | SC-M08-008/E1 | END:SUCCESS |
| UC-M08-009 | Target chưa HEAVY, số lần hiện tại 1 | SC-M08-008/E2 | END:SUCCESS |
| UC-M08-009 | Target chưa HEAVY, số lần hiện tại 3 | SC-M08-008/E3 | END:SUCCESS |
| UC-M08-009 | Target chưa HEAVY, số lần hiện tại 4 | SC-M08-008/E4 | END:SUCCESS |
| UC-M08-009 | Mai xác định reporter cố ý báo cáo ác ý trong vụ sau đánh giá con người | SC-M08-008/E5 | END:SUCCESS |
| UC-M08-009 | Vụ về tài khoản hoặc nhóm, staff chọn cảnh cáo người bị báo cáo/Owner riêng | SC-M08-008/E6 | END:SUCCESS |
| UC-M08-009 | Mod chọn cảnh cáo Mod khác | SC-M08-008/E7 | END:REJECTED |
| UC-M08-009 | Target là Admin | SC-M08-008/E8 | END:REJECTED |
| UC-M08-009 | Bình đã HEAVY; Mai chọn Ban sau khi cảnh cáo mới bị từ chối | SC-M08-008/E9 | END:SUCCESS |
| UC-M08-009 | Bình đã HEAVY, Mai không chọn Ban | SC-M08-008/E10 | END:REJECTED |
| UC-M08-009 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | SC-M08-008/E11 | END:REJECTED |
| UC-M08-009 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | SC-M08-008/E12 | END:REJECTED |
| UC-M08-009 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | SC-M08-008/E13 | END:REJECTED |
| UC-M08-009 | Quyền giữ đã tự nhả sau đủ 30 phút không hoạt động; K81 vẫn Mở/chưa ai nhận, Mai còn đủ phạm vi và chọn nhận lại | SC-M08-008/E14 | M2 |
| UC-M08-010 | Cảnh cáo do staff ra, không phải AI | SC-M08-009/E1 | END:REJECTED |
| UC-M08-010 | Cảnh cáo AI chưa bỏ và số lần hiện hành là 1, đủ điều kiện bỏ | SC-M08-009/E2 | END:SUCCESS |
| UC-M08-011 | Lệnh Ban với 1 ban trước được tính, không có ban Đang hiệu lực | SC-M08-010/E1 | END:SUCCESS |
| UC-M08-011 | Lệnh Ban với 2 ban trước được tính, không có ban Đang hiệu lực | SC-M08-010/E2 | END:SUCCESS |
| UC-M08-011 | Người giữ chọn Ban vĩnh viễn thay Ban | SC-M08-010/E3 | END:SUCCESS |
| UC-M08-011 | Mod chọn ban Mod khác | SC-M08-010/E4 | END:REJECTED |
| UC-M08-011 | Target là Admin | SC-M08-010/E5 | END:REJECTED |
| UC-M08-011 | Target đang có ban Đang hiệu lực, Mai muốn thay bằng ban vĩnh viễn | SC-M08-010/E6 | END:SUCCESS |
| UC-M08-011 | Target có ban Đang hiệu lực và không chọn gỡ trước | SC-M08-010/E7 | END:REJECTED |
| UC-M08-011 | Mai yêu cầu xem/nhận/xử lý vụ nhắm bài, bình luận hoặc tài khoản của chính Mai | SC-M08-010/E8 | END:REJECTED |
| UC-M08-011 | Mod yêu cầu vụ nhắm bài, bình luận hoặc tài khoản của Mod khác | SC-M08-010/E9 | END:REJECTED |
| UC-M08-011 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | SC-M08-010/E10 | END:REJECTED |
| UC-M08-011 | Quyền giữ đã tự nhả sau đủ 30 phút không hoạt động; K81 vẫn Mở/chưa ai nhận, Mai còn đủ phạm vi và chọn nhận lại | SC-M08-010/E11 | M2 |
| UC-M08-011 | Vụ từ đầu về nhóm G81, Mai chọn Ban Owner Bình USER riêng với biện pháp nhóm | SC-M08-010/E12 | END:SUCCESS |
| UC-M08-012 | Bản ban không còn Đang hiệu lực | SC-M08-011/E1 | END:REJECTED |
| UC-M08-013 | Lan yêu cầu mức cảnh cáo người khác | SC-M08-012/E1 | END:REJECTED |
| UC-M08-013 | Mức hiện tại là HEAVY | SC-M08-012/E2 | END:SUCCESS |
| UC-M08-013 | Không còn cảnh cáo hiện hành | SC-M08-012/E3 | END:SUCCESS |
| UC-M08-015 | Nhóm đang Bị khóa, đây là vụ báo cáo sau | SC-M08-013/E1 | END:SUCCESS |
| UC-M08-015 | Nhóm đã Bị ẩn | SC-M08-013/E2 | END:REJECTED |
| UC-M08-015 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | SC-M08-013/E3 | END:REJECTED |
| UC-M08-015 | Quyền giữ đã tự nhả sau đủ 30 phút không hoạt động; K81 vẫn Mở/chưa ai nhận, Mai còn đủ phạm vi và chọn nhận lại | SC-M08-013/E4 | M2 |
| UC-M08-015 | Nhóm đã Bị ẩn | SC-M08-014/E1 | END:REJECTED |
| UC-M08-015 | Vụ không do actor giữ tại lúc tác động (do người khác đang giữ hoặc không có vụ liên quan) | SC-M08-014/E2 | END:REJECTED |
| UC-M08-015 | Quyền giữ đã tự nhả sau đủ 30 phút không hoạt động; K81 vẫn Mở/chưa ai nhận, Mai còn đủ phạm vi và chọn nhận lại | SC-M08-014/E3 | M2 |
| UC-M08-016 | Nhóm Bị ẩn thay vì Bị khóa | SC-M08-015/E1 | END:REJECTED |
| UC-M08-025 | Mod đòi dòng thao tác Mod khác, không đang xét khiếu nại về thao tác ấy | SC-M08-016/E1 | END:REJECTED |
| UC-M08-025 | Mai đang xét khiếu nại M09 về đúng thao tác của Mod khác | SC-M08-016/E2 | END:SUCCESS |


239 mã = 18 nhóm + 166 FR chi tiết + 55 BR; không có mã đã bỏ trong thân baseline này. Vị trí nguồn không đồng nghĩa mỗi mã là một BF hoặc mọi tổ hợp đã chốt. Truy vết ngược ở sources từng bước; bảng AUT/RULE giữ phần tự động/quyền/chính sách.

Lớp tương đương: report bốn loại/giới hạn nhập; post–comment khi ẩn; Ban leo thang–vĩnh viễn trong một mục tiêu; role/phạm vi nhìn/giữ/mutation/direct khác nhau; hide/lock nhóm là thao tác riêng. Tổ hợp thay kết quả có đường cụ thể: quyền giữ mất rồi nhận lại; flag nội dung + chọn/không cảnh cáo; HEAVY + yêu cầu ban + con người Ban; ban đang hiệu lực + gỡ trước/vĩnh viễn; nhóm khóa→ẩn ở vụ sau; kết luận + loại biện pháp/quyền riêng tư; appeal hiện tại + đúng một thao tác. Không nhân mọi số đếm/tên/role thành BF hoặc áp cùng lúc các snapshot loại trừ.

## 7. GAP, TBD và giới hạn

| ID | Nguồn/phần ảnh hưởng | Điểm chưa rõ/cách giữ phạm vi |
|---|---|---|
| GAP-SC-M08-001 | NOTE-M08-01; BR-M08-19; UC003/021 | Mẫu số chỉ số tập trung bằng 0 chưa có cách hiển thị/xử lý. Đường điều tra minh họa dùng mẫu số dương, không gán 0/100%, báo lỗi hoặc từ chối xem do agent đặt. Chưa thể khép riêng nhánh chỉ số này; các quyền/chi tiết độc lập vẫn giữ. |
| GAP-SC-M08-002 | NOTE-M08-02; FR-M08-11.03/05; BR-M08-54; UC010/014 | Số lần hiện tại 0 nhưng còn cảnh cáo AI lịch sử: chưa chốt record nào còn được trừ/sàn hay điều kiện bỏ. Chỉ viết đường số lần dương, không mượn sàn 0 M09, không tạo âm hoặc từ chối mới. Cần owner chốt trước hoàn thiện nhánh này. |
| GAP-SC-M08-003 | NOTE-M08-03; FR-M08-09.11/12; BR-M08-28/36; AUT003/004 | Nhiều nội dung cùng tác giả trong một lô quét qua biên HEAVY chưa chốt thứ tự đồng thời. Giữ mỗi nội dung một cảnh cáo khi đủ điều kiện và guard đã HEAVY không tăng; không tự định serialization, cảnh cáo thứ 7 hoặc AI ban. |
| GAP-SC-M08-004 | NOTE-M08-04; BR-M08-46/47/50; UC020/006/015 | Self-report/self-handle vụ nhóm của chính staff chưa được nêu như post/comment/account. Dùng Owner khác actor trong đường hợp lệ; không tự cho phép hoặc cấm rộng mọi nhóm Owner Mod. Nhóm Owner Admin không được report đã chốt riêng. Cần chốt phần tự nhắm nhóm, không mở lại quyền đã rõ. |
| GAP-SC-M08-005 | NOTE-M08-06; FR-M08-05, FR-M08-10.04; UC021/005 | Sau khi đã áp biện pháp rồi chọn Bác bỏ, hoặc chỉ cảnh cáo reporter ác ý nhưng kết luận về người bị báo cáo: chưa chốt ý nghĩa kết luận/hệ quả. Không rollback, tự ép Có xử lý hoặc tự báo target vi phạm. Luồng chuẩn Bác bỏ chưa có biện pháp, Có xử lý sau biện pháp đúng target; cảnh cáo reporter có mục tiêu độc lập, riêng kết luận phần này còn thiếu hợp đồng. |
| GAP-SC-M08-006 | Đối chiếu FR-M08-04.10/18.11, BR-M08-50 với FR-M11-11.01/05/07, BR-M11-26 | Ban Owner khiến M11 chuyển Owner ngay (hoặc xóa mềm nhóm nếu chỉ có Owner), kể cả nhóm đang khóa. M08 chưa nêu mốc ràng buộc Owner trong hồ sơ vụ: Owner lúc báo cáo/xử lý hay Owner hiện tại, và người nhận/mức chi tiết kết luận sau thay đổi. Đã viết Ban Owner đến hiệu lực cùng chuyển quyền theo M11; chưa tự chốt kết luận toàn vụ sau thay đổi Owner, không gán thông báo/kết tội Owner mới hoặc giả định giữ snapshot Owner cũ. Phần giải quyết toàn vụ ở tổ hợp này cần hợp đồng M08–M11; nhánh Khóa + cảnh cáo Owner không đổi quyền vẫn viết đầy đủ. |
| NOTE-M08-05 | BR-M08-54; TBD-M08-02/03 đã đóng | Bỏ/lật cảnh cáo hoặc ban không tự hiện lại comment ẩn. Chỉ comment trung bình còn chờ được xét hiện lại; post khiếu nại theo M09/M03. Không mở lại TBD đã đóng. |
| TBD-M08-01 | Chat report | Hoãn MS1, không tạo BF report/quét Chat. |
| TBD-M08-04/05 | BR-M08-20/24; AUT002/RULE004 | 10 reply/5 phút và 0.9/0.5 là giá trị tạm để viết dữ liệu biên; chưa biến thành ngưỡng đã chốt hoặc chức năng cấu hình UI. |


Sáu GAP chặn kết luận đầy đủ chính những nhánh thiếu hợp đồng; phần đã đủ căn cứ vẫn triển khai và kiểm. Không dùng terminal REJECTED/HANDED_OFF để che phần nguồn chưa quyết. Trạng thái toàn tài liệu là Đang soạn; không tự sửa FR, US, register, skill hoặc module khác. [QA-M08.md](QA-M08.md) ghi số lượng/lệnh và giới hạn kiểm.


## Chuyển đổi ID nhánh sau QA-SC-01

Ngày 11/11/2026, các biến thể vai trò được đăng ký thành E tại M1 theo skill v1.4. Bảng này giữ ID lịch sử để đối chiếu các tài liệu đã dẫn V. Mỗi hàng ánh xạ cả nhánh và các bước cùng số thứ tự, ví dụ V1.2 sang bước .2 của E tương ứng.

| ID lịch sử | ID hiện hành | Điểm thay | Số bước | Nguồn |
| --- | --- | --- | --- | --- |
| SC-M08-001/V1 | SC-M08-001/E18 | M1 | 2 | FR-M08-01.01, FR-M08-01.06, BR-M08-01, BR-M08-32 |
| SC-M08-001/V2 | SC-M08-001/E19 | M1 | 4 | FR-M08-01.01, FR-M08-01.06, FR-M08-01.11, FR-M08-01.12, FR-M08-01.15, FR-M08-01.16, FR-M08-01.19, FR-M08-01.20, BR-M08-01, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-55, FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-07.10, BR-M08-05, BR-M08-06, BR-M08-07 |
| SC-M08-001/V3 | SC-M08-001/E20 | M1 | 4 | FR-M08-01.01, FR-M08-01.06, FR-M08-01.11, FR-M08-01.12, FR-M08-01.15, FR-M08-01.16, FR-M08-01.19, FR-M08-01.20, BR-M08-01, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-55, FR-M08-01.02, FR-M08-01.03, FR-M08-01.04, FR-M08-01.05, FR-M08-07.10, BR-M08-05, BR-M08-06, BR-M08-07 |
| SC-M08-001/V4 | SC-M08-001/E21 | M1 | 2 | FR-M08-01.01, FR-M08-01.20, BR-M08-55 |
| SC-M08-002/V1 | SC-M08-002/E6 | M1 | 4 | FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.04, FR-M08-02.05, FR-M08-02.06, FR-M08-02.07, FR-M08-02.08, FR-M08-02.09, BR-M08-06, BR-M08-07, BR-M08-46, FR-M08-04.01, BR-M08-11, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| SC-M08-002/V2 | SC-M08-002/E7 | M1 | 2 | FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.04, FR-M08-02.05, FR-M08-02.06, FR-M08-02.07, FR-M08-02.08, FR-M08-02.09, BR-M08-06, BR-M08-07, BR-M08-46, BR-M08-44 |
| SC-M08-002/V3 | SC-M08-002/E8 | M1 | 2 | FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.04, FR-M08-02.05, FR-M08-02.06, FR-M08-02.07, FR-M08-02.08, FR-M08-02.09, BR-M08-06, BR-M08-07, BR-M08-46, BR-M08-44 |
| SC-M08-002/V4 | SC-M08-002/E9 | M1 | 4 | FR-M08-02.01, FR-M08-02.02, FR-M08-02.03, FR-M08-02.04, FR-M08-02.05, FR-M08-02.06, FR-M08-02.07, FR-M08-02.08, FR-M08-02.09, BR-M08-06, BR-M08-07, BR-M08-46, FR-M08-04.01, BR-M08-11, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, BR-M08-48, BR-M08-44, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09 |
| SC-M08-002/V5 | SC-M08-002/E10 | M1 | 2 | FR-M08-02.01, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |
| SC-M08-003/V1 | SC-M08-003/E5 | M1 | 2 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.08, FR-M08-03.09, FR-M08-16.07, BR-M08-08, BR-M08-09, BR-M08-46 |
| SC-M08-003/V2 | SC-M08-003/E6 | M1 | 2 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.08, FR-M08-03.09, FR-M08-16.07, BR-M08-08, BR-M08-09, BR-M08-46, BR-M08-44 |
| SC-M08-003/V3 | SC-M08-003/E7 | M1 | 2 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.08, FR-M08-03.09, FR-M08-16.07, BR-M08-08, BR-M08-09, BR-M08-46, BR-M08-44 |
| SC-M08-003/V4 | SC-M08-003/E8 | M1 | 2 | FR-M08-03.01, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.05, FR-M08-03.06, FR-M08-03.07, FR-M08-03.08, FR-M08-03.09, FR-M08-16.07, BR-M08-08, BR-M08-09, BR-M08-46 |
| SC-M08-003/V5 | SC-M08-003/E9 | M1 | 2 | FR-M08-03.01, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |
| SC-M08-004/V1 | SC-M08-004/E29 | M1 | 6 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07, FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-05.01, FR-M08-05.03, BR-M08-10, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-12, BR-M08-13, BR-M08-39, BR-M08-40 |
| SC-M08-004/V2 | SC-M08-004/E30 | M1 | 2 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |
| SC-M08-004/V3 | SC-M08-004/E31 | M1 | 2 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07 |
| SC-M08-004/V4 | SC-M08-004/E32 | M1 | 6 | FR-M08-02.01, FR-M08-03.01, BR-M08-44, BR-M08-46, BR-M08-48, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, BR-M08-06, BR-M08-07, FR-M08-04.01, FR-M08-04.02, FR-M08-04.03, FR-M08-04.04, FR-M08-04.05, FR-M08-04.06, FR-M08-04.07, FR-M08-04.08, FR-M08-04.09, FR-M08-04.10, BR-M08-11, BR-M08-14, BR-M08-15, BR-M08-19, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09, FR-M08-05.01, FR-M08-05.03, BR-M08-10, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-12, BR-M08-13, BR-M08-39, BR-M08-40 |
| SC-M08-004/V5 | SC-M08-004/E33 | M1 | 2 | FR-M08-02.01, FR-M08-03.01, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |
| SC-M08-005/V1 | SC-M08-005/E11 | M1 | 2 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |
| SC-M08-005/V2 | SC-M08-005/E12 | M1 | 2 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40, BR-M08-44 |
| SC-M08-005/V3 | SC-M08-005/E13 | M1 | 2 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40, BR-M08-44 |
| SC-M08-005/V4 | SC-M08-005/E14 | M1 | 2 | FR-M08-05.01, FR-M08-05.03, FR-M08-05.02, FR-M08-05.04, FR-M08-05.05, FR-M08-05.06, FR-M08-05.07, FR-M08-05.08, FR-M08-05.09, FR-M08-05.10, FR-M08-05.11, FR-M08-16.01, FR-M08-16.03, FR-M08-16.06, FR-M08-18.11, BR-M08-10, BR-M08-12, BR-M08-13, BR-M08-14, BR-M08-39, BR-M08-40 |
| SC-M08-005/V5 | SC-M08-005/E15 | M1 | 2 | FR-M08-05.01, FR-M08-05.03, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |
| SC-M08-006/V1 | SC-M08-006/E12 | M1 | 4 | FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| SC-M08-006/V2 | SC-M08-006/E13 | M1 | 2 | FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| SC-M08-006/V3 | SC-M08-006/E14 | M1 | 2 | FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| SC-M08-006/V4 | SC-M08-006/E15 | M1 | 4 | FR-M08-07.06, FR-M08-07.01, FR-M08-07.02, FR-M08-07.03, FR-M08-07.04, FR-M08-07.05, FR-M08-07.07, FR-M08-07.08, FR-M08-07.09, FR-M08-07.10, BR-M08-23, BR-M08-36, BR-M08-46, BR-M08-48, BR-M08-49, FR-M12-02.21, BR-M08-44, FR-M08-02.04, FR-M08-02.06, FR-M08-02.09, FR-M08-03.06, FR-M08-03.07, FR-M08-03.09, FR-M08-03.02, FR-M08-03.03, FR-M08-03.04, FR-M08-03.08, BR-M08-08, BR-M08-09 |
| SC-M08-006/V5 | SC-M08-006/E16 | M1 | 2 | FR-M08-07.06, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |
| SC-M08-007/V1 | SC-M08-007/E8 | M1 | 2 | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11 |
| SC-M08-007/V2 | SC-M08-007/E9 | M1 | 2 | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11, BR-M08-44 |
| SC-M08-007/V3 | SC-M08-007/E10 | M1 | 2 | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11, BR-M08-44 |
| SC-M08-007/V4 | SC-M08-007/E11 | M1 | 2 | FR-M08-06.01, FR-M08-06.02, FR-M08-06.03, FR-M08-06.04, FR-M08-06.05, FR-M08-06.06, BR-M08-16, BR-M08-48, FR-M12-02.10, FR-M12-02.11 |
| SC-M08-007/V5 | SC-M08-007/E12 | M1 | 2 | FR-M08-06.01, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |
| SC-M08-008/V1 | SC-M08-008/E15 | M1 | 2 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |
| SC-M08-008/V2 | SC-M08-008/E16 | M1 | 2 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53, BR-M08-44 |
| SC-M08-008/V3 | SC-M08-008/E17 | M1 | 2 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53, BR-M08-44 |
| SC-M08-008/V4 | SC-M08-008/E18 | M1 | 2 | FR-M08-10.01, FR-M08-10.02, FR-M08-10.03, FR-M08-10.04, FR-M08-10.05, FR-M08-10.06, FR-M08-10.07, FR-M08-10.08, FR-M08-10.09, FR-M08-10.10, FR-M08-10.11, FR-M08-09.11, FR-M08-14.11, BR-M08-17, BR-M08-18, BR-M08-28, BR-M08-29, BR-M08-31, BR-M08-32, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-53 |
| SC-M08-008/V5 | SC-M08-008/E19 | M1 | 2 | FR-M08-10.01, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |
| SC-M08-008/V6 | SC-M08-008/E20 | M1 | 2 | FR-M08-10.01, FR-M08-10.09, FR-M08-14.10, BR-M08-46, BR-M08-55 |
| SC-M08-009/V1 | SC-M08-009/E3 | M1 | 2 | FR-M08-11.01, FR-M08-11.02, FR-M08-11.03, FR-M08-11.04, FR-M08-11.05, FR-M08-16.05, BR-M08-28, BR-M08-31, BR-M08-54 |
| SC-M08-009/V2 | SC-M08-009/E4 | M1 | 2 | FR-M08-11.01, FR-M08-11.02, FR-M08-11.03, FR-M08-11.04, FR-M08-11.05, FR-M08-16.05, BR-M08-28, BR-M08-31, BR-M08-54, BR-M08-44 |
| SC-M08-009/V3 | SC-M08-009/E5 | M1 | 2 | FR-M08-11.01, FR-M08-11.02, FR-M08-11.03, FR-M08-11.04, FR-M08-11.05, FR-M08-16.05, BR-M08-28, BR-M08-31, BR-M08-54, BR-M08-44 |
| SC-M08-010/V1 | SC-M08-010/E13 | M1 | 2 | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |
| SC-M08-010/V2 | SC-M08-010/E14 | M1 | 2 | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01, BR-M08-44 |
| SC-M08-010/V3 | SC-M08-010/E15 | M1 | 2 | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01, BR-M08-44 |
| SC-M08-010/V4 | SC-M08-010/E16 | M1 | 2 | FR-M08-14.01, FR-M08-14.02, FR-M08-14.03, FR-M08-14.04, FR-M08-14.05, FR-M08-14.06, FR-M08-14.07, FR-M08-14.08, FR-M08-14.09, FR-M08-14.10, FR-M08-14.11, FR-M08-14.12, FR-M08-14.13, FR-M08-14.14, BR-M08-33, BR-M08-34, BR-M08-35, BR-M08-36, BR-M08-43, BR-M08-46, BR-M08-48, BR-M08-52, BR-M08-53, FR-M10-06.01 |
| SC-M08-010/V5 | SC-M08-010/E17 | M1 | 2 | FR-M08-14.01, FR-M08-02.06, FR-M08-03.07, BR-M08-46, BR-M08-55 |
| SC-M08-010/V6 | SC-M08-010/E18 | M1 | 2 | FR-M08-14.01, FR-M08-10.09, FR-M08-14.10, BR-M08-46, BR-M08-55 |
| SC-M08-011/V1 | SC-M08-011/E2 | M1 | 2 | FR-M08-15.01, FR-M08-15.05, FR-M08-15.02, FR-M08-15.03, FR-M08-15.04, FR-M08-16.05, BR-M08-34, BR-M08-38, BR-M08-48, FR-M10-06.02 |
| SC-M08-011/V2 | SC-M08-011/E3 | M1 | 2 | FR-M08-15.01, FR-M08-15.05, FR-M08-15.02, FR-M08-15.03, FR-M08-15.04, FR-M08-16.05, BR-M08-34, BR-M08-38, BR-M08-48, FR-M10-06.02, BR-M08-44 |
| SC-M08-011/V3 | SC-M08-011/E4 | M1 | 2 | FR-M08-15.01, FR-M08-15.05, FR-M08-15.02, FR-M08-15.03, FR-M08-15.04, FR-M08-16.05, BR-M08-34, BR-M08-38, BR-M08-48, FR-M10-06.02, BR-M08-44 |
| SC-M08-012/V1 | SC-M08-012/E4 | M1 | 2 | FR-M08-13.01, FR-M08-13.02, BR-M08-01, BR-M08-32 |
| SC-M08-012/V2 | SC-M08-012/E5 | M1 | 2 | FR-M08-04.05, FR-M08-13.02, FR-M08-13.03, BR-M08-32 |
| SC-M08-012/V3 | SC-M08-012/E6 | M1 | 2 | FR-M08-04.05, FR-M08-13.02, FR-M08-13.03, BR-M08-32 |
| SC-M08-013/V1 | SC-M08-013/E5 | M1 | 2 | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |
| SC-M08-013/V2 | SC-M08-013/E6 | M1 | 2 | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |
| SC-M08-013/V3 | SC-M08-013/E7 | M1 | 2 | FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.04, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |
| SC-M08-014/V1 | SC-M08-014/E4 | M1 | 2 | FR-M08-18.04, FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |
| SC-M08-014/V2 | SC-M08-014/E5 | M1 | 2 | FR-M08-18.04, FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |
| SC-M08-014/V3 | SC-M08-014/E6 | M1 | 2 | FR-M08-18.04, FR-M08-18.01, FR-M08-18.02, FR-M08-18.03, FR-M08-18.05, FR-M08-18.06, FR-M08-18.07, FR-M08-18.08, FR-M08-18.09, FR-M08-18.10, BR-M08-44, BR-M08-48, BR-M08-50, BR-M11-28 |
| SC-M08-015/V1 | SC-M08-015/E2 | M1 | 2 | FR-M08-18.07, FR-M08-18.09, FR-M08-18.10, FR-M08-16.05, BR-M08-48, BR-M08-50, BR-M11-28 |
| SC-M08-015/V2 | SC-M08-015/E3 | M1 | 2 | FR-M08-18.07, FR-M08-18.09, FR-M08-18.10, FR-M08-16.05, BR-M08-48, BR-M08-50, BR-M11-28, BR-M08-44 |
| SC-M08-015/V3 | SC-M08-015/E4 | M1 | 2 | FR-M08-18.07, FR-M08-18.09, FR-M08-18.10, FR-M08-16.05, BR-M08-48, BR-M08-50, BR-M11-28, BR-M08-44 |
| SC-M08-016/V1 | SC-M08-016/E3 | M1 | 4 | FR-M08-17.02, FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, FR-M08-17.01, FR-M08-17.03, FR-M08-17.04, FR-M08-17.05, FR-M08-17.06, BR-M08-39, BR-M08-40, BR-M08-41, BR-M08-43 |
| SC-M08-016/V2 | SC-M08-016/E4 | M1 | 2 | FR-M08-17.02, FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, FR-M08-17.01, FR-M08-17.03, FR-M08-17.04, FR-M08-17.05, FR-M08-17.06, BR-M08-39, BR-M08-40, BR-M08-41, BR-M08-44 |
| SC-M08-016/V3 | SC-M08-016/E5 | M1 | 2 | FR-M08-17.02, FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, FR-M08-17.01, FR-M08-17.03, FR-M08-17.04, FR-M08-17.05, FR-M08-17.06, BR-M08-39, BR-M08-40, BR-M08-41, BR-M08-44 |
| SC-M08-016/V4 | SC-M08-016/E6 | M1 | 4 | FR-M08-17.01, FR-M08-16.01, FR-M08-16.02, FR-M08-16.03, FR-M08-16.04, FR-M08-16.05, FR-M08-16.06, FR-M08-16.07, BR-M08-39, BR-M08-40, BR-M08-41, FR-M08-17.06 |

## Dữ liệu điểm được đối soát sau QA-SC-02

Bộ mẫu P81 có 5 Post Star hiệu lực. Mỗi Post Star cộng 2 điểm theo FR-M12-02.01, nên khoản điểm của bài bằng 10. Tác giả đang có 100 điểm trước khi bài bị staff ẩn, sau trừ còn 90, record khoản đã trừ của P81 bằng 10 điểm. Khi khiếu nại đủ điều kiện hoàn khoản này, căn cứ là record 10 điểm của lần xử lý đó. Comment Star có trọng số 1 điểm theo FR-M12-02.02 và giữ bộ dữ liệu riêng.
