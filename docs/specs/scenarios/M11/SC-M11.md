# Kịch bản nghiệp vụ — M11 Group

[Vietnamese Doc] — Tái kiểm 11/11/2026 — Skill scenarios v1.4.

**Phạm vi:** toàn M11 theo FR + US: 5 UC chính, 24 UC con, 30 mapping; 22 luồng nghiệp vụ/22 scenario, 19 UC sở hữu scenario, 6 UC embedded, 4 core Summary aggregate. Giữ 32 include, không extend/generalization UC; 6 SVG nguồn. Sáu AUT và sáu RULE giữ tác vụ/ràng buộc nền, không tính BF/SC.

**Boundary:** toàn iShare là SYSTEM; các module nội bộ không actor. Owner/Group Mod/Member là vai trò theo nhóm, khác Mod/Admin hệ thống. ACT-006 chỉ hỗ trợ khi quét, không là người theo đuổi mục tiêu đăng bài. Các lối vào feed/tìm kiếm/thông báo do owner cung cấp, quyền nhóm vẫn kiểm lại khi mở/thao tác.

**Ngoài phạm vi:** tạo lại FR/US/UML, thiết kế UI/API/CSDL/giao dịch; soạn/sửa bài chung M03, bình luận chung M04, tìm theo tên M06, delivery thông báo M07, xét báo cáo/ban/khóa/ẩn/mở khóa M08, xét khiếu nại M09, cấu hình cờ M10, tính điểm M12, triển khai AI M13, feed/Trending M14/M05 và thống kê M15. Chỉ mở các tương tác/hợp đồng cần để hoàn tất mục tiêu M11. Không thêm Group Chat, follow nhóm, leaderboard riêng, lời mời có chấp nhận riêng, cooldown, thu hồi link, khiếu nại cấp nhóm hoặc khôi phục nhóm.

**Trạng thái:** Đang soạn để review, có 8 GAP kế thừa NOTE-M11-01–08. FR-M11 v1.3 Đã chốt; US-M11/overview Chờ duyệt. Kiểm tra đạt không là phê duyệt và không làm những hành vi chưa có hợp đồng trở thành đã chốt.

## 1. Module, baseline, actor và dữ liệu

<!-- sc:document -->

| key | value |
|---|---|
| module | M11 |
| scope | ALL |
| skill_version | 1.4 |
| output_dir | docs/specs/scenarios/M11 |
| status | Đang soạn |
| completed_steps | 1, 2, 3, 4 |
| date | 2026-11-11 |
| approval_evidence | - |


| Nguồn từ repo root | Version | Ngày | Trạng thái | SHA-256 |
|---|---|---|---|---|
| [docs/specs/fr/FR-M11.md](../../fr/FR-M11.md) | 1.3 | 2026-10-24 | Đã chốt | 1908d300f75d5f7fa0fd5b31b1d375bc6a63ccd42da254de6e9d0d7d9ef16307 |
| [docs/specs/us/US-M11.md](../../us/US-M11.md) | Không có version tài liệu; skill_version không là version | 2026-11-01 | Chờ duyệt | 0c4b8f2a27333fab778f7d3ca18963612899db564e385bde87c389fbc0161918 |
| [docs/specs/us/US-overview.md](../../us/US-overview.md) | 1.1 | 2026-11-02 | Chờ duyệt | c1d624b7036ea2c7a9968eaa46c482c04fa1a15e2554d536cdfc12f177e26e33 |
| [docs/specs/fr/FR-M01.md](../../fr/FR-M01.md) | 1.10 | 2026-10-24 | Đã chốt | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a |
| [docs/specs/fr/FR-M02.md](../../fr/FR-M02.md) | 1.6 | 2026-10-24 | Đã chốt | e86aca71e0415ee2e121a4fdc3628261be335e9d266fcf6e9654b2fdf3cd357e |
| [docs/specs/fr/FR-M03.md](../../fr/FR-M03.md) | 1.10 | 2026-10-24 | Đã chốt | fc996ec5520b6485277fca6a3dbae018bfce02263aba8e15ea87871f35865980 |
| [docs/specs/fr/FR-M04.md](../../fr/FR-M04.md) | 1.4 | 2026-10-24 | Đã chốt | c2fe0e4f6c4bc6835af27585cb711ac03f9fed516d435e759d20ddd58bfd1039 |
| [docs/specs/fr/FR-M05.md](../../fr/FR-M05.md) | 1.7 | 2026-10-24 | Đã chốt | eb85b5dcb56995d791ed28a8d72a2f91c95588d8cd8d4fb1e74a8aabc2d701aa |
| [docs/specs/fr/FR-M06.md](../../fr/FR-M06.md) | 1.5 | 2026-10-24 | Đã chốt | 63606046efb11356276a2c9180f53cadad76f83e2e86502ed00341d915e0b084 |
| [docs/specs/fr/FR-M07.md](../../fr/FR-M07.md) | 1.5 | 2026-10-24 | Đã chốt | 05fb18237e049e3742d06c49b824e76e238c7587e7099b8dc4a84a2e1daf4f5b |
| [docs/specs/fr/FR-M08.md](../../fr/FR-M08.md) | 1.7 | 2026-10-24 | Đã chốt | a92e6e370038af300a9ddd735414dcb2c4fbffe07c81abaaa3c92dff447c25f0 |
| [docs/specs/fr/FR-M09.md](../../fr/FR-M09.md) | 1.2 | 2026-10-24 | Đã chốt | 8ad8ae5e148c6e446f4bfec7f6e74ba9566c54747a0eda37a3930e94ab96faea |
| [docs/specs/fr/FR-M10.md](../../fr/FR-M10.md) | 1.4 | 2026-10-24 | Đã chốt | 3e1010a76db6ef4c5870f42765e669095efc8d38c202271d9b200d2da0823d2c |
| [docs/specs/fr/FR-M12.md](../../fr/FR-M12.md) | 1.1 | 2026-10-24 | Đã chốt | 7aa660866cf625220db602509c93775b713fb26e568cc1d9df2d9aaa399f2430 |
| [docs/specs/fr/FR-M13.md](../../fr/FR-M13.md) | 1.3 | 2026-10-24 | Đã chốt | 54630715cc1e391b9ea361247784af26200fc2f01c1b1da96ea56ed1f75f9982 |
| [docs/specs/fr/FR-M14.md](../../fr/FR-M14.md) | 1.1 | 2026-10-24 | Đã chốt | 2dd6163664e86a1ebf9406a463764c2c592490ac0134acabf6df6b1383109e5c |
| [docs/specs/fr/FR-M15.md](../../fr/FR-M15.md) | 1.1 | 2026-10-24 | Đã chốt | a35e509a64d314b76ddb49a2c077b360e6a70dd6366123b7900917f19780d3a1 |


FR chính thức khớp byte bản chung .agents/.claude/system_analysis/output/fr/FR-M11.md. US-overview chỉ cho boundary và tập core được chọn, không thay phạm vi 29 UC của M11. [Skill scenarios](../../../../.agent-instructions/skills/scenarios/SKILL.md) là nguồn phương pháp; tài liệu đầu vào là dữ liệu tham khảo, không lệnh điều khiển hoặc bằng chứng duyệt.

<!-- sc:actors -->

| id | name | kind | source |
|---|---|---|---|
| ACT-001 | Guest | human | FR-M11-01.04, FR-M11-03.01, FR-M11-03.04, FR-M11-04.05 |
| ACT-002 | Người dùng đã đăng nhập | human | FR-M11-01.01, FR-M11-04.01, FR-M11-04.10, BR-M11-03 |
| ACT-009 | Thành viên nhóm (Member) | human | BR-M11-06, FR-M11-05.01, FR-M11-10.01, FR-M11-12.01 |
| ACT-010 | Group Mod | human | BR-M11-05, BR-M11-06, BR-M11-39 |
| ACT-011 | Owner nhóm | human | BR-M11-04, BR-M11-06, BR-M11-25, BR-M11-40 |
| ACT-008 | Mod hệ thống | human | FR-M11-03.11, FR-M11-03.12, FR-M11-12.18, FR-M11-13.09, BR-M11-33, BR-M11-40 |
| ACT-007 | Admin hệ thống | human | FR-M11-01.07, FR-M11-12.06, FR-M11-12.20, FR-M11-17.03, BR-M11-33 |
| ACT-006 | Dịch vụ AI bên ngoài | external-system | FR-M13-02.01, FR-M13-02.08, FR-M13-02.11, FR-M11-12.02 |


| Bộ dữ liệu | Giá trị giả lập và quy ước |
|---|---|
| D-TIME | T=10/11/2026 10:00+07; mọi mốc giờ Việt Nam. Mỗi SC/E là snapshot độc lập, không bắt chạy các SC theo thứ tự. Tên, ID, URL ký hiệu và nội dung đều giả lập. |
| D-PEOPLE | An/U-A Owner; Bình/U-B và Dũng/U-D Group Mod; Chi/U-C và Lan/U-L Member; Phúc/U-P người ngoài nhóm. Guest ACT-001 chưa đăng nhập. Mod hệ thống Minh/U-M và Admin Hòa/U-H không tự là thành viên; nếu một đường cho họ vai trò nhóm thì ghi rõ. |
| D-GROUP | N11: Ôn thi Toán, mô tả Trao đổi Toán lớp 11, Hoạt động/Bình thường; Public, không câu hỏi, duyệt trước Tắt, ẩn danh Bật. Một link chung LINK-N11 (ký hiệu giả lập), không hết hạn. N12 Private có câu hỏi Bạn học lớp mấy?. |
| D-MEMBERS | An Owner, Bình Group Mod bổ nhiệm 01/09/2026 09:00+07, Dũng Group Mod bổ nhiệm lại 20/10/2026 09:00+07 (lần trước không tính), Chi Member vào 01/08/2026, Lan Member vào 01/07/2026. Đây là snapshot chuẩn, từng chức năng có thể thay dữ liệu đích ghi ngay tại bước. |
| D-POST | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; storedAuthor=Chi, anonymous=true; tiêu đề/nội dung hợp lệ theo M03 |
| D-BOUND | Tên A×100 được/A×101 từ chối; mô tả B×500 được/B×501 từ chối; dùng ASCII để không chốt Unicode/trim (GAP002). Câu hỏi/câu trả lời không đặt giới hạn ngoài nguồn. |


Mỗi SC/E là một lần chạy độc lập; mã dùng lại không là một lịch sử bắt buộc xuyên các SC. Guard thay snapshot từ đầu; biến thể Private dùng nhóm/lối vào đã nêu. Vai trò nhóm thuộc đúng nhóm đang xét; ADMIN miễn cờ/AI vẫn cần vai trò nhóm, chịu Khóa và hạn tạo. Các mốc T2=10:11 ở nhánh nhận lại khác T chuẩn10:00 và được nêu tường minh.

| Bộ dữ liệu bổ sung | Giá trị giả lập |
|---|---|
| D-LIST | N1 tên Ôn thi Toán, mô tả Ôn tập Toán, Public, tạo01/11; N2 tên CLB Vật lý, mô tả Thảo luận Vật lý, Public, tạo05/11; N3 tên CLB Hóa, mô tả Trao đổi Hóa, Private, tạo03/11. Chi thành viên N3. N4 Bị ẩn và N5 Đã xóa không hiện. Mọi mục được trả gồm tên/mô tả/chế độ từ bộ này. |


## 2. Kiểm kê UC chính và UC con

<!-- sc:decomposition -->

| core | sub | source |
|---|---|---|
| UC-M11-030 | UC-M11-001 | FR-M11-01, BR-M11-03, BR-M11-04, BR-M11-31 |
| UC-M11-030 | UC-M11-002 | FR-M11-02, BR-M11-06, BR-M11-08, BR-M11-15, BR-M11-16, BR-M11-18, BR-M11-31, BR-M11-32 |
| UC-M11-030 | UC-M11-003 | FR-M11-15, BR-M11-06, BR-M11-23 |
| UC-M11-030 | UC-M11-022 | FR-M11-15, FR-M11-10.06, FR-M11-11.03, BR-M11-23, BR-M11-25, BR-M11-26 |
| UC-M11-030 | UC-M11-024 | FR-M11-16, FR-M11-17, BR-M11-06, BR-M11-13, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, BR-M11-33 |
| UC-M11-031 | UC-M11-004 | FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, FR-M11-03.16, FR-M11-03.17, BR-M11-11, BR-M11-35 |
| UC-M11-031 | UC-M11-005 | FR-M11-03.04, FR-M11-03.05, FR-M11-03.06, FR-M11-03.07, FR-M11-03.08, FR-M11-03.09, FR-M11-03.10, FR-M11-03.11, FR-M11-03.12, FR-M11-03.13, FR-M11-03.18, BR-M11-13, BR-M11-14, BR-M11-15, BR-M11-17, BR-M11-33 |
| UC-M11-031 | UC-M11-006 | FR-M11-03.14, FR-M11-03.15, FR-M11-08.05, BR-M11-34 |
| UC-M11-031 | UC-M11-023 | FR-M11-03, BR-M11-11, BR-M11-13, BR-M11-14, BR-M11-15, BR-M11-17, BR-M11-27, BR-M11-30, BR-M11-33, BR-M11-34, BR-M11-35 |
| UC-M11-031 | UC-M11-024 | FR-M11-16, FR-M11-17, BR-M11-06, BR-M11-13, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, BR-M11-33 |
| UC-M11-032 | UC-M11-006 | FR-M11-03.14, FR-M11-03.15, FR-M11-08.05, BR-M11-34 |
| UC-M11-032 | UC-M11-007 | FR-M11-04, FR-M11-05.05, BR-M11-03, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12 |
| UC-M11-032 | UC-M11-008 | FR-M11-04.10, BR-M11-36 |
| UC-M11-032 | UC-M11-009 | FR-M11-05, BR-M11-12 |
| UC-M11-032 | UC-M11-010 | FR-M11-06, BR-M11-06, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-37 |
| UC-M11-032 | UC-M11-011 | FR-M11-07, BR-M11-06, BR-M11-10 |
| UC-M11-032 | UC-M11-012 | FR-M11-08, BR-M11-05, BR-M11-06, BR-M11-26, BR-M11-37 |
| UC-M11-032 | UC-M11-013 | FR-M11-09, FR-M11-08.05, BR-M11-05, BR-M11-06, BR-M11-24 |
| UC-M11-032 | UC-M11-014 | FR-M11-10, BR-M11-24, BR-M11-25, BR-M11-28 |
| UC-M11-032 | UC-M11-015 | FR-M11-10.03, FR-M11-10.04, FR-M11-10.05, FR-M11-10.07, FR-M11-08.05, BR-M11-04, BR-M11-25, BR-M11-37 |
| UC-M11-032 | UC-M11-022 | FR-M11-15, FR-M11-10.06, FR-M11-11.03, BR-M11-23, BR-M11-25, BR-M11-26 |
| UC-M11-032 | UC-M11-024 | FR-M11-16, FR-M11-17, BR-M11-06, BR-M11-13, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, BR-M11-33 |
| UC-M11-033 | UC-M11-016 | FR-M11-12, FR-M11-13.14, BR-M11-18, BR-M11-19, BR-M11-38, BR-M11-40, FR-M13-02.08, FR-M13-02.11 |
| UC-M11-033 | UC-M11-024 | FR-M11-16, FR-M11-17, BR-M11-06, BR-M11-13, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, BR-M11-33 |
| UC-M11-034 | UC-M11-017 | FR-M11-13.01, FR-M11-13.08, FR-M11-13.09, BR-M11-20, BR-M11-33, BR-M11-39 |
| UC-M11-034 | UC-M11-018 | FR-M11-13.02, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, BR-M11-20, BR-M11-33, BR-M11-39 |
| UC-M11-034 | UC-M11-019 | FR-M11-13.03, FR-M11-13.05, FR-M11-13.06, FR-M11-13.07, FR-M11-13.08, FR-M11-13.09, FR-M11-13.10, FR-M11-13.11, FR-M11-13.12, FR-M11-13.13, BR-M11-18, BR-M11-20, BR-M11-21, BR-M11-38, BR-M11-39 |
| UC-M11-034 | UC-M11-020 | FR-M11-14, BR-M11-05, BR-M11-06, BR-M11-21, BR-M11-22, BR-M11-30 |
| UC-M11-034 | UC-M11-021 | FR-M11-13.03, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, BR-M11-06, BR-M11-20, BR-M11-33, BR-M11-39 |
| UC-M11-034 | UC-M11-024 | FR-M11-16, FR-M11-17, BR-M11-06, BR-M11-13, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, BR-M11-33 |


<!-- sc:ucs -->

| id | treatment | scenarios | coverage | rationale | sources |
|---|---|---|---|---|---|
| UC-M11-030 | aggregate | SC-M11-001, SC-M11-002, SC-M11-003, SC-M11-004, SC-M11-005, SC-M11-006, SC-M11-007, SC-M11-008, SC-M11-009, SC-M11-010, SC-M11-011, SC-M11-012, SC-M11-013, SC-M11-014, SC-M11-015, SC-M11-016, SC-M11-017, SC-M11-018, SC-M11-019, SC-M11-020, SC-M11-021, SC-M11-022 | SC-M11-001/M2, SC-M11-002/M2, SC-M11-003/M2, SC-M11-004/M2, SC-M11-005/M2, SC-M11-006/M2, SC-M11-007/M2, SC-M11-008/M2, SC-M11-009/M2, SC-M11-010/M2, SC-M11-011/M2, SC-M11-012/M2, SC-M11-013/M2, SC-M11-014/M2, SC-M11-015/M2, SC-M11-016/M2, SC-M11-017/M2, SC-M11-018/M2, SC-M11-019/M2, SC-M11-020/M2, SC-M11-021/M2, SC-M11-022/M2 | Summary gom các mục tiêu độc lập qua mapping; không bắt chạy liên tiếp. | FR-M11-01, FR-M11-02, FR-M11-15, BR-M11-03, BR-M11-04, BR-M11-06, BR-M11-23, BR-M11-31, BR-M11-32 |
| UC-M11-031 | aggregate | SC-M11-001, SC-M11-002, SC-M11-003, SC-M11-004, SC-M11-005, SC-M11-006, SC-M11-007, SC-M11-008, SC-M11-009, SC-M11-010, SC-M11-011, SC-M11-012, SC-M11-013, SC-M11-014, SC-M11-015, SC-M11-016, SC-M11-017, SC-M11-018, SC-M11-019, SC-M11-020, SC-M11-021, SC-M11-022 | SC-M11-001/M2, SC-M11-002/M2, SC-M11-003/M2, SC-M11-004/M2, SC-M11-005/M2, SC-M11-006/M2, SC-M11-007/M2, SC-M11-008/M2, SC-M11-009/M2, SC-M11-010/M2, SC-M11-011/M2, SC-M11-012/M2, SC-M11-013/M2, SC-M11-014/M2, SC-M11-015/M2, SC-M11-016/M2, SC-M11-017/M2, SC-M11-018/M2, SC-M11-019/M2, SC-M11-020/M2, SC-M11-021/M2, SC-M11-022/M2 | Summary gom các mục tiêu độc lập qua mapping; không bắt chạy liên tiếp. | FR-M11-03, BR-M11-11, BR-M11-13, BR-M11-14, BR-M11-15, BR-M11-17, BR-M11-33, BR-M11-34, BR-M11-35 |
| UC-M11-032 | aggregate | SC-M11-001, SC-M11-002, SC-M11-003, SC-M11-004, SC-M11-005, SC-M11-006, SC-M11-007, SC-M11-008, SC-M11-009, SC-M11-010, SC-M11-011, SC-M11-012, SC-M11-013, SC-M11-014, SC-M11-015, SC-M11-016, SC-M11-017, SC-M11-018, SC-M11-019, SC-M11-020, SC-M11-021, SC-M11-022 | SC-M11-001/M2, SC-M11-002/M2, SC-M11-003/M2, SC-M11-004/M2, SC-M11-005/M2, SC-M11-006/M2, SC-M11-007/M2, SC-M11-008/M2, SC-M11-009/M2, SC-M11-010/M2, SC-M11-011/M2, SC-M11-012/M2, SC-M11-013/M2, SC-M11-014/M2, SC-M11-015/M2, SC-M11-016/M2, SC-M11-017/M2, SC-M11-018/M2, SC-M11-019/M2, SC-M11-020/M2, SC-M11-021/M2, SC-M11-022/M2 | Summary gom các mục tiêu độc lập qua mapping; không bắt chạy liên tiếp. | FR-M11-04, FR-M11-05, FR-M11-06, FR-M11-07, FR-M11-08, FR-M11-09, FR-M11-10, FR-M11-11, BR-M11-05, BR-M11-06, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-24, BR-M11-25, BR-M11-26 |
| UC-M11-033 | scenario | SC-M11-018 | SC-M11-018/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-12, FR-M11-13.11, FR-M11-13.12, FR-M11-13.14, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-38, BR-M11-40 |
| UC-M11-034 | aggregate | SC-M11-001, SC-M11-002, SC-M11-003, SC-M11-004, SC-M11-005, SC-M11-006, SC-M11-007, SC-M11-008, SC-M11-009, SC-M11-010, SC-M11-011, SC-M11-012, SC-M11-013, SC-M11-014, SC-M11-015, SC-M11-016, SC-M11-017, SC-M11-018, SC-M11-019, SC-M11-020, SC-M11-021, SC-M11-022 | SC-M11-001/M2, SC-M11-002/M2, SC-M11-003/M2, SC-M11-004/M2, SC-M11-005/M2, SC-M11-006/M2, SC-M11-007/M2, SC-M11-008/M2, SC-M11-009/M2, SC-M11-010/M2, SC-M11-011/M2, SC-M11-012/M2, SC-M11-013/M2, SC-M11-014/M2, SC-M11-015/M2, SC-M11-016/M2, SC-M11-017/M2, SC-M11-018/M2, SC-M11-019/M2, SC-M11-020/M2, SC-M11-021/M2, SC-M11-022/M2 | Summary gom các mục tiêu độc lập qua mapping; không bắt chạy liên tiếp. | FR-M11-13, FR-M11-14, BR-M11-05, BR-M11-06, BR-M11-20, BR-M11-21, BR-M11-22, BR-M11-30, BR-M11-38, BR-M11-39 |
| UC-M11-001 | scenario | SC-M11-001 | SC-M11-001/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-01, BR-M11-03, BR-M11-04, BR-M11-31 |
| UC-M11-002 | scenario | SC-M11-002 | SC-M11-002/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-02, BR-M11-06, BR-M11-08, BR-M11-15, BR-M11-16, BR-M11-18, BR-M11-31, BR-M11-32 |
| UC-M11-003 | scenario | SC-M11-003 | SC-M11-003/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-15, BR-M11-06, BR-M11-23 |
| UC-M11-004 | scenario | SC-M11-004 | SC-M11-004/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, FR-M11-03.16, FR-M11-03.17, BR-M11-11, BR-M11-35 |
| UC-M11-005 | scenario | SC-M11-005 | SC-M11-005/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-03.04, FR-M11-03.05, FR-M11-03.06, FR-M11-03.07, FR-M11-03.08, FR-M11-03.09, FR-M11-03.10, FR-M11-03.11, FR-M11-03.12, FR-M11-03.13, FR-M11-03.18, BR-M11-13, BR-M11-14, BR-M11-15, BR-M11-17, BR-M11-33 |
| UC-M11-006 | scenario | SC-M11-006, SC-M11-014, SC-M11-015, SC-M11-016, SC-M11-017 | SC-M11-006/M2, SC-M11-014/M2, SC-M11-015/M2, SC-M11-016/M2, SC-M11-017/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-03.14, FR-M11-03.15, FR-M11-08.05, BR-M11-34 |
| UC-M11-007 | scenario | SC-M11-007 | SC-M11-007/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-04, FR-M11-05.05, BR-M11-03, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12 |
| UC-M11-008 | scenario | SC-M11-008 | SC-M11-008/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-04.10, BR-M11-36 |
| UC-M11-009 | scenario | SC-M11-009 | SC-M11-009/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-05, BR-M11-12 |
| UC-M11-010 | scenario | SC-M11-010 | SC-M11-010/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-06, BR-M11-06, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-37 |
| UC-M11-011 | scenario | SC-M11-011, SC-M11-012, SC-M11-013 | SC-M11-011/M2, SC-M11-012/M2, SC-M11-013/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-07, BR-M11-06, BR-M11-10 |
| UC-M11-012 | scenario | SC-M11-014, SC-M11-015 | SC-M11-014/M2, SC-M11-015/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-08, BR-M11-05, BR-M11-06, BR-M11-26, BR-M11-37 |
| UC-M11-013 | scenario | SC-M11-016 | SC-M11-016/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-09, FR-M11-08.05, BR-M11-05, BR-M11-06, BR-M11-24 |
| UC-M11-014 | scenario | SC-M11-017 | SC-M11-017/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-10, BR-M11-24, BR-M11-25, BR-M11-28 |
| UC-M11-015 | embedded | SC-M11-017 | SC-M11-017/M2 | Lựa chọn/chuyển quyền ở đường Owner rời, phải tiếp tục đưa người cũ ra, không BF chỉ chuyển quyền theo nguồn hiện tại. | FR-M11-10.03, FR-M11-10.04, FR-M11-10.05, FR-M11-10.07, FR-M11-08.05, BR-M11-04, BR-M11-25, BR-M11-37 |
| UC-M11-016 | embedded | SC-M11-018 | SC-M11-018/M4 | Cổng nằm trong gửi bài, có quét/không quét/kết quả đầy đủ, không BF SYSTEM–AI độc lập. | FR-M11-12, FR-M11-13.14, BR-M11-18, BR-M11-19, BR-M11-38, BR-M11-40, FR-M13-02.08, FR-M13-02.11 |
| UC-M11-017 | scenario | SC-M11-019 | SC-M11-019/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-13.01, FR-M11-13.08, FR-M11-13.09, BR-M11-20, BR-M11-33, BR-M11-39 |
| UC-M11-018 | scenario | SC-M11-020 | SC-M11-020/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-13.02, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, BR-M11-20, BR-M11-33, BR-M11-39 |
| UC-M11-019 | scenario | SC-M11-021 | SC-M11-021/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-13.03, FR-M11-13.05, FR-M11-13.06, FR-M11-13.07, FR-M11-13.08, FR-M11-13.09, FR-M11-13.10, FR-M11-13.11, FR-M11-13.12, FR-M11-13.13, BR-M11-18, BR-M11-20, BR-M11-21, BR-M11-38, BR-M11-39 |
| UC-M11-020 | scenario | SC-M11-022 | SC-M11-022/M2 | Mục tiêu actor chủ động thực hiện đến kết quả; có thể tham gia hành trình khác tại điểm chèn. | FR-M11-14, BR-M11-05, BR-M11-06, BR-M11-21, BR-M11-22, BR-M11-30 |
| UC-M11-021 | embedded | SC-M11-019, SC-M11-020, SC-M11-021 | SC-M11-019/M2, SC-M11-020/M2, SC-M11-021/M2 | Bộ kiểm pha xem/nhận/kết luận mở tại caller; không BF kiểm quyền. | FR-M11-13.03, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, BR-M11-06, BR-M11-20, BR-M11-33, BR-M11-39 |
| UC-M11-022 | embedded | SC-M11-003, SC-M11-017 | SC-M11-003/M2, SC-M11-017/E4.4 | Xóa mềm được mở ở Owner xóa/Owner cuối rời và AUT002, không BF chỉ cập nhật trạng thái. | FR-M11-15, FR-M11-10.06, FR-M11-11.03, BR-M11-23, BR-M11-25, BR-M11-26 |
| UC-M11-023 | embedded | SC-M11-004, SC-M11-005, SC-M11-006, SC-M11-014, SC-M11-015, SC-M11-016, SC-M11-017 | SC-M11-004/M2, SC-M11-005/M2, SC-M11-006/M2, SC-M11-014/M2, SC-M11-015/M2, SC-M11-016/M2, SC-M11-017/M2 | Lọc quyền/riêng tư/danh tính trong xem nhóm/danh sách/chọn thành viên, không BF chỉ lọc dữ liệu. | FR-M11-03, BR-M11-11, BR-M11-13, BR-M11-14, BR-M11-15, BR-M11-17, BR-M11-27, BR-M11-30, BR-M11-33, BR-M11-34, BR-M11-35 |
| UC-M11-024 | embedded | SC-M11-001, SC-M11-002, SC-M11-003, SC-M11-004, SC-M11-005, SC-M11-006, SC-M11-007, SC-M11-008, SC-M11-009, SC-M11-010, SC-M11-011, SC-M11-012, SC-M11-013, SC-M11-014, SC-M11-015, SC-M11-016, SC-M11-017, SC-M11-018, SC-M11-019, SC-M11-020, SC-M11-021, SC-M11-022 | SC-M11-001/M2, SC-M11-002/M2, SC-M11-003/M2, SC-M11-004/M2, SC-M11-005/M2, SC-M11-006/M2, SC-M11-007/M2, SC-M11-008/M2, SC-M11-009/M2, SC-M11-010/M2, SC-M11-011/M2, SC-M11-012/M2, SC-M11-013/M2, SC-M11-014/M2, SC-M11-015/M2, SC-M11-016/M2, SC-M11-017/M2, SC-M11-018/M2, SC-M11-019/M2, SC-M11-020/M2, SC-M11-021/M2, SC-M11-022/M2 | Kiểm điều kiện ngay trong từng mục tiêu, không BF chỉ kiểm cờ/quyền. | FR-M11-16, FR-M11-17, BR-M11-06, BR-M11-13, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, BR-M11-33 |


| SVG nguồn | Số UC | Đối chiếu |
|---|---|---|
| C-M11 | 5 | XML/tập UC khớp US; không sửa UML |
| D-M11-030 | 6 | XML/tập UC khớp US; không sửa UML |
| D-M11-031 | 6 | XML/tập UC khớp US; không sửa UML |
| D-M11-032 | 14 | XML/tập UC khớp US; không sửa UML |
| D-M11-033 | 3 | XML/tập UC khớp US; không sửa UML |
| D-M11-034 | 7 | XML/tập UC khớp US; không sửa UML |


## 3. Luồng nghiệp vụ theo chức năng actor

<!-- sc:flows -->

| id | uc | primary | trigger | goal | completion | covered_ucs | rationale | scenario | sources |
|---|---|---|---|---|---|---|---|---|---|
| BF-M11-001 | UC-M11-001 | ACT-002 | Phúc gửi yêu cầu tạo nhóm với tên, mô tả và chế độ. | Tạo một nhóm và trở thành Owner đầu tiên | Nhóm Hoạt động/Bình thường có cấu hình đã chọn hoặc mặc định, đúng một Owner đầu tiên và thời điểm tham gia=T; link chung được cấp, kết quả tạo trả cho người yêu cầu. | UC-M11-001, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-001 | FR-M11-01.01, FR-M11-01.10, FR-M11-01.11, FR-M11-01.12, BR-M11-31, FR-M11-01.02, FR-M11-01.03, FR-M11-01.05, FR-M11-01.06, FR-M11-01.08, FR-M11-01.09, FR-M11-05.06, BR-M11-02, BR-M11-03, BR-M11-04, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-01.04, FR-M11-01.07, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M10-12.08 |
| BF-M11-002 | UC-M11-002 | ACT-011 | An mở chức năng sửa thông tin/cài đặt N11. | Sửa thông tin và cài đặt một nhóm | Thông tin/cài đặt hợp lệ được lưu và trả; hiệu lực theo thời điểm, giữ bài ẩn danh cũ/hàng chờ bài. Nếu thành vào ngay thì mọi yêu cầu tham gia Chờ duyệt được chấp nhận tại T và báo người gửi, không chấp nhận hàng chờ bài. | UC-M11-002, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-002 | FR-M11-02.01, FR-M11-02.02, FR-M11-02.09, FR-M11-02.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-02.05, FR-M11-02.06, FR-M11-02.07, FR-M11-02.08, BR-M11-31, FR-M11-02.03, FR-M11-02.04, FR-M11-02.11, FR-M11-02.12, FR-M11-02.13, FR-M11-02.14, FR-M11-02.15, BR-M11-08, BR-M11-15, BR-M11-16, BR-M11-18, BR-M11-32, FR-M11-06.02, FR-M11-06.04, BR-M11-07, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-12.07, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-16.04, FR-M11-16.07, FR-M10-12.08 |
| BF-M11-003 | UC-M11-003 | ACT-011 | An chọn xóa N11. | Xóa mềm một nhóm do mình làm Owner | Nhóm Đã xóa, mọi nội dung không hiện với ai, dữ liệu và điểm giữ theo nguồn; actor nhận kết quả xóa. | UC-M11-003, UC-M11-022, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-003 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.03, FR-M11-15.05, BR-M11-23, FR-M12-02.14, FR-M11-15.04, FR-M11-01.06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-16.01, FR-M11-16.02, FR-M11-16.04, FR-M11-16.07, FR-M10-12.08 |
| BF-M11-004 | UC-M11-004 | ACT-001 | Guest mở trang danh sách nhóm. | Xem danh sách các nhóm được phép xuất hiện | Danh sách trả đúng người xem, đủ tên/mô tả/chế độ và thứ tự mới nhất; giữ quyền Private/ẩn/xóa, việc mở nhóm là yêu cầu khác. | UC-M11-004, UC-M11-023, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-004 | FR-M11-03.01, FR-M11-03.16, FR-M11-03.02, FR-M11-03.17, FR-M11-16.01, FR-M11-15.01, FR-M11-17.02, FR-M11-17.07, BR-M11-11, BR-M11-27, BR-M11-23, BR-M11-35, FR-M11-17.01, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.08, BR-M11-29, FR-M11-03.03 |
| BF-M11-005 | UC-M11-005 | ACT-001 | Guest mở trang N11 để đọc thông tin và bài đã đăng. | Mở trang nhóm hoặc đọc nội dung nhóm theo quyền | Actor nhận đúng thông tin/nội dung và trường tác giả theo lối vào/quyền; preview Private chỉ tên/mô tả, không được coi đã đọc nội dung. Không tự cho quyền tương tác theo dữ liệu đã tải. | UC-M11-005, UC-M11-023, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-005 | FR-M11-03.04, FR-M11-03.05, FR-M11-03.06, FR-M11-03.09, FR-M11-03.10, FR-M11-03.11, FR-M11-03.12, FR-M11-03.18, BR-M11-13, BR-M11-14, BR-M11-17, BR-M11-33, FR-M11-16.03, FR-M03-04.02, FR-M03-07.02, FR-M11-04.05, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, BR-M11-15, FR-M11-02.12, FR-M11-02.13, FR-M11-14.01, BR-M11-30, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M08-04.06, FR-M11-03.13, FR-M11-14.03, FR-M11-14.05, FR-M11-14.07 |
| BF-M11-006 | UC-M11-006 | ACT-001 | Guest yêu cầu xem danh sách thành viên N11. | Xem danh sách thành viên kèm vai trò nhóm | Danh sách thành viên/role đúng nhóm được trả cho người có quyền xem trang; không thay vai trò/thành viên hoặc cấp quyền quản trị. | UC-M11-006, UC-M11-023, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-006 | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M10-12.08 |
| BF-M11-007 | UC-M11-007 | ACT-002 | Phúc chọn Tham gia N11. | Tham gia nhóm hoặc gửi yêu cầu gia nhập theo cổng nhóm | Vào ngay: Member với mốc T và không thông báo. Nhóm cần duyệt: đúng một yêu cầu Chờ duyệt của người gửi, câu trả lời đúng nếu có câu hỏi, báo Owner/Group Mod; chưa là Member. Mục tiêu gửi yêu cầu hoàn tất ở xác nhận đã ghi nhận, không giả đã duyệt. | UC-M11-007, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-007 | FR-M11-04.01, FR-M11-05.05, FR-M11-04.06, FR-M11-04.07, FR-M11-04.09, FR-M11-05.04, FR-M11-06.08, BR-M11-03, BR-M11-07, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-04.02, FR-M11-04.03, FR-M11-04.08, FR-M11-06.07, BR-M11-08, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-04.04, FR-M11-09.07, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-16.04, FR-M11-16.07, FR-M11-04.05, FR-M10-12.08 |
| BF-M11-008 | UC-M11-008 | ACT-002 | Phúc yêu cầu rút R11 của mình. | Rút yêu cầu tham gia đang chờ của mình | Yêu cầu của người gửi chuyển Đã rút, dữ liệu được giữ, actor nhận kết quả; không tạo thành viên. | UC-M11-008, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-008 | FR-M11-04.10, BR-M11-36, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M10-12.08 |
| BF-M11-009 | UC-M11-009 | ACT-009 | Chi yêu cầu mời Phúc vào N12. | Mời người khác đến nhóm bằng link chung hoặc lời mời | Người yêu cầu nhận link chung hoặc kết quả đã gửi thông báo mời có đúng link cho người đích; chưa bảo đảm người được mời tham gia. Chức năng gửi mời hoàn tất, tham gia là mục tiêu độc lập. | UC-M11-009, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-009 | FR-M11-05.01, FR-M11-05.02, FR-M11-05.04, FR-M11-05.05, FR-M11-05.06, FR-M11-05.07, BR-M11-12, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-16.04, FR-M11-16.07, FR-M10-12.08, FR-M11-05.03 |
| BF-M11-010 | UC-M11-010 | ACT-010 | Bình mở danh sách yêu cầu tham gia N12. | Xét một yêu cầu tham gia nhóm | Quyết định hợp lệ được lưu và trả: Chấp nhận thêm Member/mốc/thông báo; Từ chối chuyển Đã từ chối, không thêm Member/không báo người gửi, cho gửi yêu cầu mới ngay. | UC-M11-010, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-010 | FR-M11-06.01, FR-M11-06.05, BR-M11-08, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-06.02, FR-M11-06.04, FR-M11-06.06, BR-M11-07, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-06.03, FR-M11-06.09, FR-M11-04.04, BR-M11-09, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-16.04, FR-M11-16.07, FR-M10-12.08 |
| BF-M11-011 | UC-M11-011 | ACT-010 | Bình chọn chặn Phúc gửi yêu cầu tới N12. | Chặn một người gửi yêu cầu tham gia nhóm | Người gửi có trong danh sách chặn của đúng nhóm, mọi yêu cầu Chờ duyệt hiện có bị từ chối; không thành ban hệ thống/thành viên, actor nhận kết quả. | UC-M11-011, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-011 | FR-M11-07.01, FR-M11-07.03, FR-M11-04.06, FR-M11-06.09, BR-M11-06, BR-M11-10, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-16.04, FR-M11-16.07, FR-M10-12.08, FR-M11-07.02 |
| BF-M11-012 | UC-M11-011 | ACT-010 | Bình mở danh sách chặn N12. | Xem danh sách người bị chặn tham gia nhóm | Danh sách chặn hiện tại đúng nhóm được trả chỉ đọc, không thay quyền tham gia/yêu cầu/thành viên. | UC-M11-011, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-012 | FR-M11-07.04, FR-M11-07.02, BR-M11-06, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M10-12.08 |
| BF-M11-013 | UC-M11-011 | ACT-010 | Bình mở danh sách chặn N12 để chọn người bỏ chặn. | Bỏ chặn một người khỏi danh sách chặn tham gia | U-P không còn trong danh sách chặn đúng nhóm, được dùng luồng gia nhập theo điều kiện hiện hành; chưa là Member/yêu cầu cũ không tự được chấp nhận. | UC-M11-011, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-013 | FR-M11-07.04, FR-M11-07.05, FR-M11-07.02, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-16.07, FR-M10-12.08 |
| BF-M11-014 | UC-M11-012 | ACT-011 | An mở chức năng bổ nhiệm Group Mod trong N11. | Bổ nhiệm một thành viên làm Group Mod | Chi chuyển Member→Group Mod trong đúng nhóm, kết quả trả Owner; mốc bổ nhiệm mới và thông báo người được bổ nhiệm. | UC-M11-006, UC-M11-012, UC-M11-023, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-014 | FR-M11-08.01, FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-08.03, FR-M11-11.06, BR-M11-05, BR-M11-26, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-08.02, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-16.04, FR-M11-16.07, FR-M10-12.08, FR-M11-08.04 |
| BF-M11-015 | UC-M11-012 | ACT-011 | An mở chức năng giáng Group Mod trong N11. | Giáng một thành viên từ Group Mod về Member | Bình chuyển Group Mod→Member trong đúng nhóm, kết quả trả Owner; không thông báo giáng, không đổi vai trò hệ thống. | UC-M11-006, UC-M11-012, UC-M11-023, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-015 | FR-M11-08.02, FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-08.06, FR-M11-11.06, BR-M11-05, BR-M11-26, BR-M11-37, FR-M11-08.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-16.04, FR-M11-16.07, FR-M10-12.08, FR-M11-08.04 |
| BF-M11-016 | UC-M11-013 | ACT-011 | An mở chức năng kick thành viên N11. | Kick một thành viên thuộc thẩm quyền khỏi nhóm | Đích ra khỏi đúng nhóm và nhận thông báo, không tự bị chặn; nội dung/tác giả/ẩn danh/điểm giữ, quyền sau rời phụ thuộc Public/Private. | UC-M11-006, UC-M11-013, UC-M11-023, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-016 | FR-M11-09.01, FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-09.05, FR-M11-09.06, FR-M11-09.07, FR-M11-10.08, BR-M11-05, BR-M11-24, BR-M11-37, FR-M12-02.15, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-09.03, FR-M11-10.09, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-16.04, FR-M11-16.07, FR-M11-09.02, FR-M10-12.08, FR-M11-09.04 |
| BF-M11-017 | UC-M11-014 | ACT-011 | An chọn rời N11 còn thành viên khác. | Tự rời nhóm, bảo toàn nội dung và kế nhiệm khi cần | Member/Group Mod rời: không còn là thành viên, giữ nội dung/tác giả/điểm. Owner còn người: người được chỉ định thành Owner trước rồi Owner cũ ra; thông báo người kế nhiệm. Owner cuối xác nhận cảnh báo: nhóm Đã xóa, giữ dữ liệu/điểm. | UC-M11-006, UC-M11-014, UC-M11-015, UC-M11-022, UC-M11-023, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-017 | FR-M11-10.03, FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-04, BR-M11-25, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-10.04, FR-M11-10.02, FR-M11-10.07, FR-M11-10.08, BR-M11-24, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-10.05, FR-M11-10.06, FR-M11-15.03, FR-M12-02.14, FR-M11-01.06, FR-M11-16.08, FR-M11-16.09, FR-M11-10.01, FR-M10-12.08, FR-M12-02.15, FR-M11-10.09 |
| BF-M11-018 | UC-M11-033 | ACT-009 | Chi gửi bài nháp P18 đã soạn qua M03 vào N11. | Gửi bài mới hoặc gửi lại bài bị từ chối vào nhóm | Bài được gửi qua đúng cổng và trả kết quả cho tác giả. Đã đăng: đúng phạm vi/ẩn danh, sự kiện M07 và mốc embedding theo owner. Nhánh chờ: xác nhận đã ghi nhận P18 trong queue nhóm hoặc Mod hệ thống đúng vai trò, chưa đăng/không hiện thường; mục tiêu gửi hoàn tất ở ghi nhận theo UC033. AI tự từ chối dùng REJECTED, không phải thành công đăng. | UC-M11-016, UC-M11-024, UC-M11-033 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-018 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11, FR-M11-13.11, FR-M11-02.06, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-16.04, FR-M11-16.07 |
| BF-M11-019 | UC-M11-017 | ACT-010 | Bình mở hàng chờ duyệt N11. | Tra cứu hàng chờ duyệt riêng của một nhóm | Trả đúng tập bài chờ nhóm duyệt được phép xem, tách queue báo cáo/hệ thống; không tự nhận hoặc duyệt bài. | UC-M11-017, UC-M11-021, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-019 | FR-M11-13.01, FR-M11-13.08, FR-M11-13.09, BR-M11-17, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-16.04, FR-M11-16.07, FR-M10-12.08 |
| BF-M11-020 | UC-M11-018 | ACT-010 | Bình chọn nhận P19 trong hàng chờ N11. | Nhận giữ một bài chờ nhóm duyệt để xử lý | Đúng người được ghi holder với mốc không thao tác; bài vẫn Chờ duyệt. Actor nhận xác nhận nhận giữ độc quyền để xử lý, mục tiêu nhận hoàn tất; kết luận là chức năng SC021. | UC-M11-018, UC-M11-021, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-020 | FR-M11-13.02, FR-M11-13.03, FR-M11-13.04, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-13.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-16.04, FR-M11-16.07, FR-M10-12.08 |
| BF-M11-021 | UC-M11-019 | ACT-010 | Bình chọn Chấp nhận P19 đang giữ. | Kết luận một bài đang chờ nhóm duyệt | Một quyết định hợp lệ được lưu và trả: Chấp nhận→Đã đăng có sự kiện/mốc embedding; Từ chối có lý do→Bị từ chối kèm lý do có sự kiện M03/M07, không khiếu nại cấp nhóm, tác giả được sửa/gửi lại. Không lấy từ chối bài hợp lệ của người duyệt làm REJECTED của chính chức năng kết luận. | UC-M11-019, UC-M11-021, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-021 | FR-M11-13.05, FR-M11-13.03, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, FR-M11-12.12, FR-M11-12.13, BR-M11-17, BR-M11-18, BR-M11-20, BR-M11-33, BR-M11-39, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-13.06, FR-M11-13.07, FR-M11-13.10, FR-M11-13.11, BR-M11-21, BR-M11-38, FR-M11-13.04, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-16.04, FR-M11-16.07, FR-M10-12.08 |
| BF-M11-022 | UC-M11-020 | ACT-010 | Bình chọn gỡ P11 của Chi khỏi N11. | Gỡ một bài hoặc bình luận khỏi nhóm theo quyền nhóm | Nội dung mang dấu gỡ xóa mềm, bài giữ trạng thái đăng và dữ liệu/điểm; tập xem thu hẹp đúng lớp quyền, tác giả nhận thông báo, không tự hiện lại/khiếu nại cấp nhóm. Actor nhận kết quả gỡ. | UC-M11-020, UC-M11-024 | Actor khởi tạo, có tương tác với SYSTEM và nhận kết quả chức năng; không tách chỉ vì role/trạng thái/lỗi. | SC-M11-022 | FR-M11-14.01, FR-M11-14.02, FR-M11-14.03, FR-M11-14.04, FR-M11-14.05, FR-M11-14.06, FR-M11-14.07, FR-M11-14.08, BR-M11-05, BR-M11-06, BR-M11-21, BR-M11-22, BR-M11-30, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M12-02.16, FR-M15-02.27, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, FR-M11-16.04, FR-M11-16.07, FR-M10-12.08 |


Chặn, xem danh sách chặn và bỏ chặn là ba mục tiêu độc lập trong UC011: cấm một người, đọc tập hiện tại, mở lại cổng gia nhập. Bổ nhiệm và giáng Group Mod là hai chuyển đổi chức năng đối nghịch trong UC012. Tạo/sửa/xóa nhóm và các mục tiêu xem/gia nhập/rút/mời/xét yêu cầu/kick/rời được triển khai riêng; không ép thành một phiên quản lý chung.

Gửi bài mới/gửi lại dùng cùng mục tiêu gửi qua cổng, là nhánh từ M1, không tách theo trạng thái. Gỡ bài/bình luận cùng chức năng gỡ nội dung, loại đích là nhánh từ M1. Chấp nhận/Từ chối thuộc cùng chức năng xét yêu cầu hoặc kết luận bài. Lấy link/mời người cụ thể thuộc cùng mục tiêu mời. Public/Private, câu hỏi, Owner/Admin, AI tắt/lỗi/điểm, Khóa/cờ là điều kiện/nhánh.

Xem queue, nhận giữ và kết luận có mục tiêu độc lập trong US: trả tập bài, xác nhận quyền giữ một bài, ra quyết định. Nhận không được coi là đã duyệt. Owner tự rời phải đi đến ra khỏi nhóm sau chuyển quyền hoặc xác nhận xóa nhóm cuối; không tạo BF chỉ chuyển Owner/xóa mềm. Tự kế nhiệm/nhả bài/áp quyết định M08/phát sự kiện ghi tại AUT, không dựng actor giả.

| Quan hệ US nguyên gốc | Điểm chèn | Guard/đường về |
|---|---|---|
| UC-M11-001 include UC-M11-024 | #uc-m11-001-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-001-main-3 |
| UC-M11-002 include UC-M11-024 | #uc-m11-002-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-002-main-3 |
| UC-M11-003 include UC-M11-024 | #uc-m11-003-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-003-main-3 |
| UC-M11-004 include UC-M11-024 | #uc-m11-004-main-2 | Ngữ cảnh lối vào; không tự cho mở nhóm khi cờ tắt; #uc-m11-004-main-3 |
| UC-M11-005 include UC-M11-024 | #uc-m11-005-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-005-main-3 |
| UC-M11-006 include UC-M11-024 | #uc-m11-006-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-006-main-3 |
| UC-M11-007 include UC-M11-024 | #uc-m11-007-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-007-main-3 |
| UC-M11-008 include UC-M11-024 | #uc-m11-008-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-008-main-3 |
| UC-M11-009 include UC-M11-024 | #uc-m11-009-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-009-main-3 |
| UC-M11-010 include UC-M11-024 | #uc-m11-010-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-010-main-3 |
| UC-M11-011 include UC-M11-024 | #uc-m11-011-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-011-main-3 |
| UC-M11-012 include UC-M11-024 | #uc-m11-012-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-012-main-3 |
| UC-M11-013 include UC-M11-024 | #uc-m11-013-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-013-main-3 |
| UC-M11-014 include UC-M11-024 | #uc-m11-014-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-014-main-3 |
| UC-M11-017 include UC-M11-024 | #uc-m11-017-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-017-main-3 |
| UC-M11-018 include UC-M11-024 | #uc-m11-018-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-018-main-3 |
| UC-M11-019 include UC-M11-024 | #uc-m11-019-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-019-main-3 |
| UC-M11-020 include UC-M11-024 | #uc-m11-020-main-2 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-020-main-3 |
| UC-M11-033 include UC-M11-024 | #uc-m11-033-main-1 | Mỗi lần thực hiện hành vi; các nhánh cùng loại kiểm theo pha; #uc-m11-033-main-2 |
| UC-M11-003 include UC-M11-022 | #uc-m11-003-main-3 | Owner được phép xóa trực tiếp; #uc-m11-003-main-4 |
| UC-M11-004 include UC-M11-023 | #uc-m11-004-main-3 | Ngữ cảnh danh sách/trang/thành viên tương ứng; #uc-m11-004-main-4 |
| UC-M11-005 include UC-M11-023 | #uc-m11-005-main-3 | Ngữ cảnh danh sách/trang/thành viên tương ứng; #uc-m11-005-main-4 |
| UC-M11-006 include UC-M11-023 | #uc-m11-006-main-3 | Ngữ cảnh danh sách/trang/thành viên tương ứng; #uc-m11-006-main-4 |
| UC-M11-012 include UC-M11-006 | #uc-m11-012-main-3 | Owner bổ nhiệm/giáng; #uc-m11-012-main-4 |
| UC-M11-013 include UC-M11-006 | #uc-m11-013-main-3 | Nhánh Owner kick; Group Mod không bắt luồng chọn của Owner; #uc-m11-013-main-4 |
| UC-M11-015 include UC-M11-006 | #uc-m11-015-main-2 | Owner chọn người kế nhiệm trước rời; #uc-m11-015-main-3 |
| UC-M11-014 include UC-M11-015 | #uc-m11-014-alt-1 | Owner rời, còn người khác, nhóm/cờ cho phép; #uc-m11-014-main-3 |
| UC-M11-014 include UC-M11-022 | #uc-m11-014-alt-2 | Owner là người duy nhất, đã xác nhận và nhóm/cờ cho phép; END: nhóm Đã xóa sau Owner cuối xác nhận cảnh báo |
| UC-M11-033 include UC-M11-016 | #uc-m11-033-main-3 | Gửi mới hoặc gửi lại; kết quả không đăng ngay kết thúc theo nhánh; #uc-m11-033-main-4 |
| UC-M11-017 include UC-M11-021 | #uc-m11-017-main-3 | Pha xem, không cần giữ; #uc-m11-017-main-4 |
| UC-M11-018 include UC-M11-021 | #uc-m11-018-main-3 | Pha nhận, cấm Group Mod tự nhận và không chiếm người giữ; #uc-m11-018-main-4 |
| UC-M11-019 include UC-M11-021 | #uc-m11-019-main-3 | Pha kết luận, cần đúng người giữ và không Group Mod tự duyệt; #uc-m11-019-main-4 |


Các include được mở trong lượt SYSTEM tương ứng, giữ tương tác actor khi cần chọn. UC006 được mở ở Owner bổ nhiệm/giáng/kick và chọn kế nhiệm; UC015→UC006 chỉ ở nhánh Owner còn người, UC014→UC022 chỉ Owner cuối đã xác nhận. UC023 lọc quyền trước trả dữ liệu; UC021 theo pha không buộc holder khi chỉ xem queue. Không tự tạo quan hệ UML từ thứ tự mời→tham gia hoặc gửi→duyệt.

## 4. Scenario sáu phần

<a id="sc-m11-001"></a>

<!-- sc:scenario SC-M11-001 -->

### SC-M11-001

#### 1. Tên kịch bản chuẩn

Tạo một nhóm và trở thành Owner đầu tiên — BF-M11-001; owner [UC-M11-001](../../us/US-M11.md#uc-m11-001); nhóm UC chính: UC-M11-030.

#### 2. Actor thực hiện

ACT-002 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có dữ liệu yêu cầu tạo, phiên theo M01; đăng nhập/hạn mức/cờ và độ dài được kiểm trong luồng. Chuẩn Phúc đã tạo 4 nhóm trong 24 giờ, đang sở hữu 40 nhóm; tên mới trùng một nhóm khác vẫn hợp lệ.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-001 -->

| result | condition |
|---|---|
| SUCCESS | Nhóm Hoạt động/Bình thường có cấu hình đã chọn hoặc mặc định, đúng một Owner đầu tiên và thời điểm tham gia=T; link chung được cấp, kết quả tạo trả cho người yêu cầu. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-001 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Phúc gửi yêu cầu tạo nhóm với tên, mô tả và chế độ. | Tên=Ôn thi Toán; mô tả=Trao đổi Toán lớp 11; Public; không đặt hai công tắc/câu hỏi; T | M2 | FR-M11-01.01, FR-M11-01.10, FR-M11-01.11, FR-M11-01.12, BR-M11-31 |
| M2 | SYSTEM | Hệ thống kiểm đã đăng nhập/cờ, tên không trống và ≤100 ký tự, mô tả ≤500. Đếm 4 nhóm người này tạo trong 24 giờ ngay trước T, gồm đã xóa, không tính nhóm đúng T−24h; không giới hạn tổng sở hữu. Tạo N11 Hoạt động/Bình thường, Phúc là Owner duy nhất/thành viên đầu tiên với thời điểm tham gia=T; duyệt trước và ẩn danh mặc định Tắt, câu hỏi trống, một link chung không hết hạn. Trả nhóm đã tạo. | 4→5 nhóm trong khoảng; Owner=Phúc; tên trùng được; tồn tại=Hoạt động; kiểm duyệt=Bình thường; duyệt trước=false; ẩn danh=false; question=trống; LINK-N11 | END:SUCCESS | FR-M11-01.01, FR-M11-01.02, FR-M11-01.03, FR-M11-01.05, FR-M11-01.06, FR-M11-01.08, FR-M11-01.09, FR-M11-01.10, FR-M11-01.12, FR-M11-05.06, BR-M11-02, BR-M11-03, BR-M11-04, BR-M11-31, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-001 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Phúc đã tạo đủ 5 nhóm trong 24 giờ ngay trước T, trong đó một nhóm đã xóa | E1.1 | FR-M11-01.03, FR-M11-01.06, BR-M11-03 |
| E2 | system | M1 | Dữ liệu tên trống; người dùng sửa về bộ hợp lệ | E2.1 | FR-M11-01.08, BR-M11-31, FR-M11-01.01 |
| E3 | system | M1 | Dữ liệu tên gồm101 chữ A; người dùng sửa về bộ hợp lệ | E3.1 | FR-M11-01.08, BR-M11-31, FR-M11-01.01 |
| E4 | system | M1 | Dữ liệu mô tả gồm501 chữ B; người dùng sửa về bộ hợp lệ | E4.1 | FR-M11-01.09, BR-M11-31, FR-M11-01.01 |
| E5 | user-choice | M1 | Người tạo đặt ngay cấu hình và dùng biên100/500 ASCII | E5.1 | FR-M11-01.01, FR-M11-01.10, FR-M11-01.11, FR-M11-01.12, BR-M11-31, FR-M11-01.02, FR-M11-01.03, FR-M11-01.04, FR-M11-01.05, FR-M11-01.06, FR-M11-01.07, FR-M11-01.08, FR-M11-01.09, FR-M11-05.06, BR-M11-03, BR-M11-04, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E6 | system | M1 | Nhóm tạo cũ đúng T−24h rời cửa sổ, không giới hạn tổng40 nhóm sở hữu | E6.1 | BR-M11-03, FR-M11-01.01, FR-M11-01.02, FR-M11-01.03, FR-M11-01.05, FR-M11-01.06, FR-M11-01.08, FR-M11-01.09, FR-M11-01.10, FR-M11-01.12, FR-M11-05.06, BR-M11-02, BR-M11-04, BR-M11-31, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E7 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E7.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E8 | system | M1 | ACT-001 — Guest chưa đăng nhập yêu cầu tạo. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M11-01.04, FR-M11-01.03, FR-M11-01.07, BR-M11-03, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E9 | system | M1 | ACT-007 — Hòa Admin có đủ 5 nhóm đã tạo trong 24h, kể cả cờ Tắt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M11-01.07, FR-M11-01.03, FR-M11-01.04, BR-M11-03, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E10 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng ngữ cảnh người dùng/người gửi; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M11-01.01, FR-M11-01.10, FR-M11-01.11, FR-M11-01.12, BR-M11-31, FR-M11-17.03, FR-M10-12.08, FR-M11-01.02, FR-M11-01.03, FR-M11-01.05, FR-M11-01.06, FR-M11-01.08, FR-M11-01.09, FR-M11-05.06, BR-M11-02, BR-M11-03, BR-M11-04, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-001 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống tính cả nhóm đã xóa, từ chối tạo nhóm thứ6; tổng sở hữu không làm thay đổi phép đếm. | 5 trong cửa sổ24h; N11 mới chưa được tạo; xóa nhóm cũ không làm giảm đếm | END:REJECTED | FR-M11-01.03, FR-M11-01.06, BR-M11-03 |


<!-- sc:branch SC-M11-001 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | Phúc gửi yêu cầu tạo với tên trống. | Các trường khác như chuẩn; count24h=4 | E2.2 | FR-M11-01.08 |
| E2.2 | SYSTEM | Hệ thống từ chối lưu vì tên trống; chưa tạo nhóm. | Tên bắt buộc≤100, mô tả≤500; dữ liệu không hợp lệ | E2.3 | FR-M11-01.08, BR-M11-31 |
| E2.3 | ACT-002 | Phúc sửa và gửi lại đúng bộ dữ liệu chuẩn. | Ôn thi Toán/Trao đổi Toán lớp 11/Public; không đặt công tắc/câu hỏi; count24h vẫn4 | M2 | FR-M11-01.01 |


<!-- sc:branch SC-M11-001 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-002 | Phúc gửi yêu cầu tạo với tên gồm101 chữ A. | Các trường khác như chuẩn; count24h=4 | E3.2 | FR-M11-01.08 |
| E3.2 | SYSTEM | Hệ thống từ chối lưu vì tên gồm101 chữ A; chưa tạo nhóm. | Tên bắt buộc≤100, mô tả≤500; dữ liệu không hợp lệ | E3.3 | FR-M11-01.08, BR-M11-31 |
| E3.3 | ACT-002 | Phúc sửa và gửi lại đúng bộ dữ liệu chuẩn. | Ôn thi Toán/Trao đổi Toán lớp 11/Public; không đặt công tắc/câu hỏi; count24h vẫn4 | M2 | FR-M11-01.01 |


<!-- sc:branch SC-M11-001 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-002 | Phúc gửi yêu cầu tạo với mô tả gồm501 chữ B. | Các trường khác như chuẩn; count24h=4 | E4.2 | FR-M11-01.09 |
| E4.2 | SYSTEM | Hệ thống từ chối lưu vì mô tả gồm501 chữ B; chưa tạo nhóm. | Tên bắt buộc≤100, mô tả≤500; dữ liệu không hợp lệ | E4.3 | FR-M11-01.09, BR-M11-31 |
| E4.3 | ACT-002 | Phúc sửa và gửi lại đúng bộ dữ liệu chuẩn. | Ôn thi Toán/Trao đổi Toán lớp 11/Public; không đặt công tắc/câu hỏi; count24h vẫn4 | M2 | FR-M11-01.01 |


<!-- sc:branch SC-M11-001 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-002 | Phúc gửi yêu cầu tạo nhóm với tên, mô tả và chế độ. | Tên=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA; mô tả=BBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBBB; Private; duyệt trước Bật; ẩn danh Bật; một câu hỏi=Bạn học lớp mấy?; 4 nhóm trong khoảng | E5.2 | FR-M11-01.01, FR-M11-01.10, FR-M11-01.11, FR-M11-01.12, BR-M11-31 |
| E5.2 | SYSTEM | Hệ thống kiểm đăng nhập/cờ, tên100/mô tả500 ASCII hợp lệ, count24h=4; tạo N11 Private/Hoạt động/Bình thường, Phúc Owner duy nhất và joinAt=T. Lưu duyệt trước Bật, ẩn danh Bật và đúng một câu hỏi đã gửi, trả nhóm với link chung không hạn. | Tên A×100/mô tả B×500/Private/true/true/Bạn học lớp mấy?; count4→5; Owner Phúc | END:SUCCESS | FR-M11-01.01, FR-M11-01.02, FR-M11-01.03, FR-M11-01.04, FR-M11-01.05, FR-M11-01.06, FR-M11-01.07, FR-M11-01.08, FR-M11-01.09, FR-M11-01.10, FR-M11-01.11, FR-M11-05.06, BR-M11-03, BR-M11-04, BR-M11-31, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-001 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-002 | Phúc gửi bộ tạo chuẩn lúc10:00 ngày10/11. | 5 nhóm trước:09/11 10:00,10:05,10:10,10:15,10:20; một đã xóa; sở hữu40 | E6.2 | BR-M11-03 |
| E6.2 | SYSTEM | Hệ thống kiểm đã đăng nhập/cờ, tên không trống và ≤100 ký tự, mô tả ≤500. Đếm 4 nhóm người này tạo trong 24 giờ ngay trước T, gồm đã xóa, không tính nhóm đúng T−24h; không giới hạn tổng sở hữu. Tạo N11 Hoạt động/Bình thường, Phúc là Owner duy nhất/thành viên đầu tiên với thời điểm tham gia=T; duyệt trước và ẩn danh mặc định Tắt, câu hỏi trống, một link chung không hết hạn. Trả nhóm đã tạo. | 4→5 nhóm trong khoảng; Owner=Phúc; tên trùng được; tồn tại=Hoạt động; kiểm duyệt=Bình thường; duyệt trước=false; ẩn danh=false; question=trống; LINK-N11 | END:SUCCESS | FR-M11-01.01, FR-M11-01.02, FR-M11-01.03, FR-M11-01.05, FR-M11-01.06, FR-M11-01.08, FR-M11-01.09, FR-M11-01.10, FR-M11-01.12, FR-M11-05.06, BR-M11-02, BR-M11-03, BR-M11-04, BR-M11-31, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-001 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


**E8 — thay toàn bộ M1 đến kết thúc:** Guest chưa đăng nhập yêu cầu tạo. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-001 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-001 | Guest yêu cầu tạo nhóm. | Tên Ôn thi Toán/Public; chưa đăng nhập | E8.2 | FR-M11-01.04 |
| E8.2 | SYSTEM | Hệ thống từ chối vì chưa đăng nhập. | Chưa tạo nhóm mới | END:REJECTED | FR-M11-01.03, FR-M11-01.04, FR-M11-01.07, BR-M11-03, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E9 — thay toàn bộ M1 đến kết thúc:** Hòa Admin có đủ 5 nhóm đã tạo trong 24h, kể cả cờ Tắt. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-001 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-007 | Hòa Admin yêu cầu tạo nhóm. | Tên Ôn thi Toán/Public; count24h=5; Group=false | E9.2 | FR-M11-01.07 |
| E9.2 | SYSTEM | Hệ thống cho ADMIN qua cờ nhưng vẫn từ chối tạo vượt5 trong 24h. | Chưa tạo nhóm mới | END:REJECTED | FR-M11-01.03, FR-M11-01.04, FR-M11-01.07, BR-M11-03, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E10 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng ngữ cảnh người dùng/người gửi; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-001 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-007 | Hòa gửi yêu cầu tạo nhóm với tên, mô tả và chế độ. | Tên=Ôn thi Toán; mô tả=Trao đổi Toán lớp 11; Public; không đặt hai công tắc/câu hỏi; T; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E10.2 | FR-M11-01.01, FR-M11-01.10, FR-M11-01.11, FR-M11-01.12, BR-M11-31, FR-M11-17.03, FR-M10-12.08 |
| E10.2 | SYSTEM | Hệ thống kiểm đã đăng nhập/cờ, tên không trống và ≤100 ký tự, mô tả ≤500. Đếm 4 nhóm người này tạo trong 24 giờ ngay trước T, gồm đã xóa, không tính nhóm đúng T−24h; không giới hạn tổng sở hữu. Tạo N11 Hoạt động/Bình thường, Hòa là Owner duy nhất/thành viên đầu tiên với thời điểm tham gia=T; duyệt trước và ẩn danh mặc định Tắt, câu hỏi trống, một link chung không hết hạn. Trả nhóm đã tạo. | 4→5 nhóm trong khoảng; Owner=Hòa; tên trùng được; tồn tại=Hoạt động; kiểm duyệt=Bình thường; duyệt trước=false; ẩn danh=false; question=trống; LINK-N11 | END:SUCCESS | FR-M11-01.01, FR-M11-01.02, FR-M11-01.03, FR-M11-01.05, FR-M11-01.06, FR-M11-01.08, FR-M11-01.09, FR-M11-01.10, FR-M11-01.12, FR-M11-05.06, BR-M11-02, BR-M11-03, BR-M11-04, BR-M11-31, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


<!-- sc:end SC-M11-001 -->

<a id="sc-m11-002"></a>

<!-- sc:scenario SC-M11-002 -->

### SC-M11-002

#### 1. Tên kịch bản chuẩn

Sửa thông tin và cài đặt một nhóm — BF-M11-002; owner [UC-M11-002](../../us/US-M11.md#uc-m11-002); nhóm UC chính: UC-M11-030.

#### 2. Actor thực hiện

ACT-011 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có nhóm và dữ liệu cần thay; kiểm Owner/quyền/trạng thái khi mở và lưu. Chuẩn N11 Public, duyệt trước/ẩn danh Bật; câu hỏi cũ Bạn học lớp mấy?; P-old đã ẩn danh, P-wait đang chờ nhóm duyệt; R1/R2 Chờ duyệt.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-002 -->

| result | condition |
|---|---|
| SUCCESS | Thông tin/cài đặt hợp lệ được lưu và trả; hiệu lực theo thời điểm, giữ bài ẩn danh cũ/hàng chờ bài. Nếu thành vào ngay thì mọi yêu cầu tham gia Chờ duyệt được chấp nhận tại T và báo người gửi, không chấp nhận hàng chờ bài. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-002 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-011 | An mở chức năng sửa thông tin/cài đặt N11. | An Owner; cấu hình cũ Public/duyệt trước Bật/ẩn danh Bật; một câu hỏi | M2 | FR-M11-02.01, FR-M11-02.02 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Chỉ Owner được sửa, nhóm không Bị khóa; trả thông tin và cài đặt hiện tại để thay. | Tên=Ôn thi Toán; mô tả cũ; Public; câu hỏi cũ; P-old/P-wait/R1/R2 giữ nguyên | M3 | FR-M11-02.01, FR-M11-02.02, FR-M11-02.09, FR-M11-02.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| M3 | ACT-011 | An đổi tên/mô tả, Public→Private, tắt duyệt trước và ẩn danh, sửa câu hỏi rồi lưu. | Tên=CLB Toán 11; mô tả=Cùng giải bài; Private; duyệt trước=false; ẩn danh=false; câu hỏi=Mục tiêu học tập của bạn? | M4 | FR-M11-02.01, FR-M11-02.02, FR-M11-02.05, FR-M11-02.06, FR-M11-02.07, FR-M11-02.08, BR-M11-31 |
| M4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Owner; tên không trống ≤100, mô tả ≤500, tối đa một câu hỏi, lưu đúng các giá trị tại T. Private áp yêu cầu mới: người ngoài đang đọc bản tải 09:55 chỉ đọc bản hiện sẵn, không bình luận/vote/báo cáo; tải feed/tìm sau T không trả bài, tải lại/link/bookmark/thông báo báo “Nội dung không tồn tại”. Duyệt trước mới chỉ áp bài gửi sau T, P-wait vẫn chờ. P-old vẫn ẩn danh, bài mới không chọn ẩn danh. Câu hỏi mới chỉ áp yêu cầu mới; R1/R2 vẫn chờ vì chưa thành vào ngay. Trả thông tin/cài đặt mới. | CLB Toán 11/Cùng giải bài/Private/false/false/Mục tiêu học tập của bạn?; P-old ẩn danh; P-wait/R1/R2 giữ trạng thái | END:SUCCESS | FR-M11-02.01, FR-M11-02.02, FR-M11-02.03, FR-M11-02.04, FR-M11-02.05, FR-M11-02.06, FR-M11-02.07, FR-M11-02.08, FR-M11-02.09, FR-M11-02.10, FR-M11-02.11, FR-M11-02.12, FR-M11-02.13, FR-M11-02.14, FR-M11-02.15, BR-M11-08, BR-M11-15, BR-M11-16, BR-M11-18, BR-M11-31, BR-M11-32, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-002 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M3 | Private→Public không câu hỏi khiến nhóm thành vào ngay | E1.1 | FR-M11-02.02, FR-M11-02.07, FR-M11-02.14, BR-M11-32, FR-M11-06.02, FR-M11-06.04, BR-M11-07, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E2 | user-choice | M3 | Bỏ câu hỏi của Public khiến nhóm thành vào ngay | E2.1 | FR-M11-02.02, FR-M11-02.07, FR-M11-02.14, BR-M11-32, FR-M11-06.02, FR-M11-06.04, BR-M11-07, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E3 | user-choice | M3 | Owner chỉ đổi Câu hỏi=Bạn muốn ôn phần nào? | E3.1 | FR-M11-02.07, FR-M11-02.08, FR-M11-02.14, BR-M11-08, BR-M11-32, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E4 | user-choice | M3 | Owner chỉ đổi Duyệt trước=Bật | E4.1 | FR-M11-02.05, FR-M11-02.15, BR-M11-18, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E5 | user-choice | M3 | Owner chỉ đổi Ẩn danh=Bật | E5.1 | FR-M11-02.06, FR-M11-12.07, BR-M11-16, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E6 | system | M3 | Owner lưu tên trống rồi sửa | E6.1 | FR-M11-02.11, BR-M11-31, FR-M11-02.01, FR-M11-02.02 |
| E7 | system | M3 | Owner lưu tên101 chữ A rồi sửa | E7.1 | FR-M11-02.11, BR-M11-31, FR-M11-02.01, FR-M11-02.02 |
| E8 | system | M3 | Owner lưu mô tả501 chữ B rồi sửa | E8.1 | FR-M11-02.11, BR-M11-31, FR-M11-02.01, FR-M11-02.02 |
| E9 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E9.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E10 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E10.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E11 | system | M2 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | E11.1 | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |
| E12 | system | M4 | Nhóm chuyển Bị khóa hoặc cờ Group Tắt với người không ADMIN sau lượt đọc nhưng trước lúc lưu | E12.1 | FR-M11-16.07, FR-M11-17.01, FR-M11-17.08, BR-M11-28, BR-M11-29 |
| E13 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Owner; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E13.1 | FR-M11-02.01, FR-M11-02.02, FR-M11-17.03, FR-M10-12.08, FR-M11-02.09, FR-M11-02.10, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-02.05, FR-M11-02.06, FR-M11-02.07, FR-M11-02.08, BR-M11-31, FR-M11-02.03, FR-M11-02.04, FR-M11-02.11, FR-M11-02.12, FR-M11-02.13, FR-M11-02.14, FR-M11-02.15, BR-M11-08, BR-M11-15, BR-M11-16, BR-M11-18, BR-M11-32 |
| E14 | system | M1 | ACT-010 — Bình Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-010; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E14.1 | FR-M11-02.09, FR-M11-02.10, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E15 | system | M1 | ACT-009 — Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E15.1 | FR-M11-02.09, FR-M11-02.10, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E16 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E16.1 | FR-M11-02.09, FR-M11-02.10, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E17 | system | M1 | ACT-007 — Hòa ADMIN không Owner yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E17.1 | FR-M11-02.09, FR-M11-02.10, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-002 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-011 | An lưu Private→Public không câu hỏi. | N11 trước=Private; sau=Public; question=trống; R1 Phúc/R2 Xuân Chờ duyệt; duyệt trước/ẩn danh không đổi | E1.2 | FR-M11-02.02, FR-M11-02.07, FR-M11-02.14, BR-M11-32 |
| E1.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner/không Khóa, lưu Public không câu hỏi. AUT001 chấp nhận ngay mọi R1/R2 đang Chờ duyệt; Phúc/Xuân trở thành Member với joinAt=T, thông báo ứng dụng cho từng người gửi. Trả cấu hình mới và kết quả nhận yêu cầu; không duyệt từng R theo SC010 hoặc nhả P-wait. | N11 Public/question trống; R1/R2→Đã chấp nhận; U-P/U-X→Member tại T; P-wait vẫn chờ; duyệt trước/ẩn danh giữ | END:SUCCESS | FR-M11-02.14, FR-M11-06.02, FR-M11-06.04, BR-M11-07, BR-M11-32, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-002 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-011 | An lưu Bỏ câu hỏi của Public. | N11 trước=Public; sau=Public; question=trống; R1 Phúc/R2 Xuân Chờ duyệt; duyệt trước/ẩn danh không đổi | E2.2 | FR-M11-02.02, FR-M11-02.07, FR-M11-02.14, BR-M11-32 |
| E2.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner/không Khóa, lưu Public không câu hỏi. AUT001 chấp nhận ngay mọi R1/R2 đang Chờ duyệt; Phúc/Xuân trở thành Member với joinAt=T, thông báo ứng dụng cho từng người gửi. Trả cấu hình mới và kết quả nhận yêu cầu; không duyệt từng R theo SC010 hoặc nhả P-wait. | N11 Public/question trống; R1/R2→Đã chấp nhận; U-P/U-X→Member tại T; P-wait vẫn chờ; duyệt trước/ẩn danh giữ | END:SUCCESS | FR-M11-02.14, FR-M11-06.02, FR-M11-06.04, BR-M11-07, BR-M11-32, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-002 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-011 | An lưu riêng Câu hỏi=Bạn muốn ôn phần nào?. | N11 Public; các trường khác giữ; R1/R2/P-wait/P-old có trước T | E3.2 | FR-M11-02.07, FR-M11-02.08, FR-M11-02.14, BR-M11-08, BR-M11-32 |
| E3.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Owner/không Khóa, lưu đúng trường Câu hỏi; chỉ áp yêu cầu mới; R1/R2 đang chờ không tự chấp nhận; không tự ghi phiên bản câu hỏi cũ (GAP002). Trả giá trị đã lưu. | Câu hỏi=Bạn muốn ôn phần nào?; không đặt thêm câu hỏi thứ hai/cấu hình khác | END:SUCCESS | FR-M11-02.07, FR-M11-02.08, FR-M11-02.14, BR-M11-08, BR-M11-32, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-002 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-011 | An lưu riêng Duyệt trước=Bật. | N11 Public; các trường khác giữ; R1/R2/P-wait/P-old có trước T | E4.2 | FR-M11-02.05, FR-M11-02.15, BR-M11-18 |
| E4.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Owner/không Khóa, lưu đúng trường Duyệt trước; chỉ áp bài gửi sau T; P-wait đã chờ vẫn chờ, không xử lý lại bài cũ. Trả giá trị đã lưu. | Duyệt trước=Bật; không đặt thêm câu hỏi thứ hai/cấu hình khác | END:SUCCESS | FR-M11-02.05, FR-M11-02.15, BR-M11-18, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-002 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-011 | An lưu riêng Ẩn danh=Bật. | N11 Public; các trường khác giữ; R1/R2/P-wait/P-old có trước T | E5.2 | FR-M11-02.06, FR-M11-12.07, BR-M11-16 |
| E5.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Owner/không Khóa, lưu đúng trường Ẩn danh; cho lựa chọn ẩn danh từng bài mới, bài cũ không bị đổi lựa chọn. Trả giá trị đã lưu. | Ẩn danh=Bật; không đặt thêm câu hỏi thứ hai/cấu hình khác | END:SUCCESS | FR-M11-02.06, FR-M11-12.07, BR-M11-16, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-002 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-011 | An gửi bản sửa tên trống. | Các giá trị cấu hình dự định giống đường chính | E6.2 | FR-M11-02.11 |
| E6.2 | SYSTEM | Hệ thống từ chối lưu do giới hạn tên/mô tả; chưa ghi bản sửa. | Tên bắt buộc≤100; mô tả≤500 | E6.3 | FR-M11-02.11, BR-M11-31 |
| E6.3 | ACT-011 | An sửa dữ liệu về bản hợp lệ và lưu. | CLB Toán 11/Cùng giải bài/Private/duyệt trước=false/ẩn danh=false/câu hỏi=Mục tiêu học tập của bạn? | M4 | FR-M11-02.01, FR-M11-02.02 |


<!-- sc:branch SC-M11-002 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | ACT-011 | An gửi bản sửa tên101 chữ A. | Các giá trị cấu hình dự định giống đường chính | E7.2 | FR-M11-02.11 |
| E7.2 | SYSTEM | Hệ thống từ chối lưu do giới hạn tên/mô tả; chưa ghi bản sửa. | Tên bắt buộc≤100; mô tả≤500 | E7.3 | FR-M11-02.11, BR-M11-31 |
| E7.3 | ACT-011 | An sửa dữ liệu về bản hợp lệ và lưu. | CLB Toán 11/Cùng giải bài/Private/duyệt trước=false/ẩn danh=false/câu hỏi=Mục tiêu học tập của bạn? | M4 | FR-M11-02.01, FR-M11-02.02 |


<!-- sc:branch SC-M11-002 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | ACT-011 | An gửi bản sửa mô tả501 chữ B. | Các giá trị cấu hình dự định giống đường chính | E8.2 | FR-M11-02.11 |
| E8.2 | SYSTEM | Hệ thống từ chối lưu do giới hạn tên/mô tả; chưa ghi bản sửa. | Tên bắt buộc≤100; mô tả≤500 | E8.3 | FR-M11-02.11, BR-M11-31 |
| E8.3 | ACT-011 | An sửa dữ liệu về bản hợp lệ và lưu. | CLB Toán 11/Cùng giải bài/Private/duyệt trước=false/ẩn danh=false/câu hỏi=Mục tiêu học tập của bạn? | M4 | FR-M11-02.01, FR-M11-02.02 |


<!-- sc:branch SC-M11-002 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-002 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-002 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | SYSTEM | Hệ thống từ chối hành vi trong nhóm Bị khóa kể cả Owner/Group Mod hoặc ADMIN; quyền đọc/lưu/báo cáo/Member-Group Mod tự rời và tự kế nhiệm theo hợp đồng riêng vẫn giữ. | Nhóm Bị khóa; không thực hiện thay đổi/duyệt/nhận mở queue bị chặn | END:REJECTED | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |


<!-- sc:branch SC-M11-002 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | SYSTEM | Hệ thống kiểm lại điều kiện hiện tại; nếu cờ Tắt từ chối đúng thông báo “Hệ thống đang bận, vui lòng thử lại sau”, nếu Khóa từ chối hành vi đã bị chặn. Không dùng lần đọc trước để hoàn tất thay đổi. | Không có thay đổi được yêu cầu của lần lưu này; trạng thái hiện tại giữ | END:REJECTED | FR-M11-16.07, FR-M11-17.01, FR-M11-17.08, BR-M11-28, BR-M11-29 |


**E13 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Owner; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-002 E13 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E13.1 | ACT-007 | Hòa mở chức năng sửa thông tin/cài đặt N11. | Hòa Owner; cấu hình cũ Public/duyệt trước Bật/ẩn danh Bật; một câu hỏi; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E13.2 | FR-M11-02.01, FR-M11-02.02, FR-M11-17.03, FR-M10-12.08 |
| E13.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Chỉ Owner được sửa, nhóm không Bị khóa; trả thông tin và cài đặt hiện tại để thay. | Tên=Ôn thi Toán; mô tả cũ; Public; câu hỏi cũ; P-old/P-wait/R1/R2 giữ nguyên | E13.3 | FR-M11-02.01, FR-M11-02.02, FR-M11-02.09, FR-M11-02.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |
| E13.3 | ACT-007 | Hòa đổi tên/mô tả, Public→Private, tắt duyệt trước và ẩn danh, sửa câu hỏi rồi lưu. | Tên=CLB Toán 11; mô tả=Cùng giải bài; Private; duyệt trước=false; ẩn danh=false; câu hỏi=Mục tiêu học tập của bạn? | E13.4 | FR-M11-02.01, FR-M11-02.02, FR-M11-02.05, FR-M11-02.06, FR-M11-02.07, FR-M11-02.08, BR-M11-31, FR-M11-17.03, FR-M10-12.08 |
| E13.4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Owner; tên không trống ≤100, mô tả ≤500, tối đa một câu hỏi, lưu đúng các giá trị tại T. Private áp yêu cầu mới: người ngoài đang đọc bản tải 09:55 chỉ đọc bản hiện sẵn, không bình luận/vote/báo cáo; tải feed/tìm sau T không trả bài, tải lại/link/bookmark/thông báo báo “Nội dung không tồn tại”. Duyệt trước mới chỉ áp bài gửi sau T, P-wait vẫn chờ. P-old vẫn ẩn danh, bài mới không chọn ẩn danh. Câu hỏi mới chỉ áp yêu cầu mới; R1/R2 vẫn chờ vì chưa thành vào ngay. Trả thông tin/cài đặt mới. | CLB Toán 11/Cùng giải bài/Private/false/false/Mục tiêu học tập của bạn?; P-old ẩn danh; P-wait/R1/R2 giữ trạng thái | END:SUCCESS | FR-M11-02.01, FR-M11-02.02, FR-M11-02.03, FR-M11-02.04, FR-M11-02.05, FR-M11-02.06, FR-M11-02.07, FR-M11-02.08, FR-M11-02.09, FR-M11-02.10, FR-M11-02.11, FR-M11-02.12, FR-M11-02.13, FR-M11-02.14, FR-M11-02.15, BR-M11-08, BR-M11-15, BR-M11-16, BR-M11-18, BR-M11-31, BR-M11-32, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


**E14 — thay toàn bộ M1 đến kết thúc:** Bình Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-010; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-002 E14 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E14.1 | ACT-010 | Bình Group Mod yêu cầu: Sửa thông tin và cài đặt một nhóm. | Đúng nhóm/đích của chức năng; Bình Group Mod không có vai trò nhóm bắt buộc; Group=true | E14.2 | FR-M11-02.09, FR-M11-02.10, BR-M11-06 |
| E14.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-02.09, FR-M11-02.10, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E15 — thay toàn bộ M1 đến kết thúc:** Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-002 E15 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E15.1 | ACT-009 | Chi Member yêu cầu: Sửa thông tin và cài đặt một nhóm. | Đúng nhóm/đích của chức năng; Chi Member không có vai trò nhóm bắt buộc; Group=true | E15.2 | FR-M11-02.09, FR-M11-02.10, BR-M11-06 |
| E15.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-02.09, FR-M11-02.10, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E16 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-002 E16 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E16.1 | ACT-002 | Phúc người ngoài yêu cầu: Sửa thông tin và cài đặt một nhóm. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E16.2 | FR-M11-02.09, FR-M11-02.10, BR-M11-06 |
| E16.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-02.09, FR-M11-02.10, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E17 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN không Owner yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-002 E17 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E17.1 | ACT-007 | Hòa ADMIN không Owner yêu cầu: Sửa thông tin và cài đặt một nhóm. | Đúng nhóm/đích của chức năng; Hòa ADMIN không Owner không có vai trò nhóm bắt buộc; Group=true | E17.2 | FR-M11-02.09, FR-M11-02.10, BR-M11-06 |
| E17.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-02.09, FR-M11-02.10, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-002 -->

<a id="sc-m11-003"></a>

<!-- sc:scenario SC-M11-003 -->

### SC-M11-003

#### 1. Tên kịch bản chuẩn

Xóa mềm một nhóm do mình làm Owner — BF-M11-003; owner [UC-M11-003](../../us/US-M11.md#uc-m11-003); nhóm UC chính: UC-M11-030.

#### 2. Actor thực hiện

ACT-011 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có N11 Hoạt động/Bình thường và yêu cầu xóa; quyền Owner/cờ/Khóa kiểm khi xử lý, không tự thêm bước xác nhận cho xóa trực tiếp.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-003 -->

| result | condition |
|---|---|
| SUCCESS | Nhóm Đã xóa, mọi nội dung không hiện với ai, dữ liệu và điểm giữ theo nguồn; actor nhận kết quả xóa. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-003 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-011 | An chọn xóa N11. | An Owner; N11 có nhiều thành viên và nội dung; Chi 20 điểm | M2 | FR-M11-15.01 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Chỉ Owner được xóa, không Bị khóa. Áp xóa mềm UC022: nhóm→Đã xóa, nhóm và mọi nội dung không hiện với bất kỳ ai kể cả thành viên cũ; giữ dữ liệu, giữ điểm từng người (Chi có 20 điểm từ bài vẫn 20). Từ chối mở/tham gia/đăng vào nhóm đã xóa; nhóm vẫn tính vào lịch sử tạo trong 24 giờ nếu còn trong khoảng. Trả kết quả Đã xóa. | N11 Hoạt động→Đã xóa; dữ liệu giữ; Chi20→20; không tạo chức năng khôi phục | END:SUCCESS | FR-M11-15.01, FR-M11-15.02, FR-M11-15.03, FR-M11-15.05, BR-M11-23, FR-M12-02.14, FR-M11-15.04, FR-M11-01.06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-003 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E1.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E2 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E2.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E3 | system | M2 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | E3.1 | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |
| E4 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Owner; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M11-15.01, FR-M11-17.03, FR-M10-12.08, FR-M11-15.02, FR-M11-15.03, FR-M11-15.05, BR-M11-23, FR-M12-02.14, FR-M11-15.04, FR-M11-01.06, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-27, BR-M11-28, BR-M11-29 |
| E5 | system | M1 | ACT-010 — Bình Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-010; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M11-15.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E6 | system | M1 | ACT-009 — Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M11-15.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E7 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M11-15.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E8 | system | M1 | ACT-007 — Hòa ADMIN không Owner yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M11-15.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-003 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-003 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-003 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối hành vi trong nhóm Bị khóa kể cả Owner/Group Mod hoặc ADMIN; quyền đọc/lưu/báo cáo/Member-Group Mod tự rời và tự kế nhiệm theo hợp đồng riêng vẫn giữ. | Nhóm Bị khóa; không thực hiện thay đổi/duyệt/nhận mở queue bị chặn | END:REJECTED | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |


**E4 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Owner; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-003 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-007 | Hòa chọn xóa N11. | Hòa Owner; N11 có nhiều thành viên và nội dung; Chi 20 điểm; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E4.2 | FR-M11-15.01, FR-M11-17.03, FR-M10-12.08 |
| E4.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Chỉ Owner được xóa, không Bị khóa. Áp xóa mềm UC022: nhóm→Đã xóa, nhóm và mọi nội dung không hiện với bất kỳ ai kể cả thành viên cũ; giữ dữ liệu, giữ điểm từng người (Chi có 20 điểm từ bài vẫn 20). Từ chối mở/tham gia/đăng vào nhóm đã xóa; nhóm vẫn tính vào lịch sử tạo trong 24 giờ nếu còn trong khoảng. Trả kết quả Đã xóa. | N11 Hoạt động→Đã xóa; dữ liệu giữ; Chi20→20; không tạo chức năng khôi phục | END:SUCCESS | FR-M11-15.01, FR-M11-15.02, FR-M11-15.03, FR-M11-15.05, BR-M11-23, FR-M12-02.14, FR-M11-15.04, FR-M11-01.06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


**E5 — thay toàn bộ M1 đến kết thúc:** Bình Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-010; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-003 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-010 | Bình Group Mod yêu cầu: Xóa mềm một nhóm do mình làm Owner. | Đúng nhóm/đích của chức năng; Bình Group Mod không có vai trò nhóm bắt buộc; Group=true | E5.2 | FR-M11-15.04, BR-M11-06 |
| E5.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-15.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E6 — thay toàn bộ M1 đến kết thúc:** Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-003 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-009 | Chi Member yêu cầu: Xóa mềm một nhóm do mình làm Owner. | Đúng nhóm/đích của chức năng; Chi Member không có vai trò nhóm bắt buộc; Group=true | E6.2 | FR-M11-15.04, BR-M11-06 |
| E6.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-15.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E7 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-003 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-002 | Phúc người ngoài yêu cầu: Xóa mềm một nhóm do mình làm Owner. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E7.2 | FR-M11-15.04, BR-M11-06 |
| E7.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-15.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E8 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN không Owner yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-003 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-007 | Hòa ADMIN không Owner yêu cầu: Xóa mềm một nhóm do mình làm Owner. | Đúng nhóm/đích của chức năng; Hòa ADMIN không Owner không có vai trò nhóm bắt buộc; Group=true | E8.2 | FR-M11-15.04, BR-M11-06 |
| E8.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-15.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-003 -->

<a id="sc-m11-004"></a>

<!-- sc:scenario SC-M11-004 -->

### SC-M11-004

#### 1. Tên kịch bản chuẩn

Xem danh sách các nhóm được phép xuất hiện — BF-M11-004; owner [UC-M11-004](../../us/US-M11.md#uc-m11-004); nhóm UC chính: UC-M11-031.

#### 2. Actor thực hiện

ACT-001 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Không cần đăng nhập để xem Public. Bộ nhóm: N1 Public tạo 01/11, N2 Public tạo 05/11; N3 Private tạo 03/11 (Chi là thành viên); N4 Bị ẩn, N5 Đã xóa.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-004 -->

| result | condition |
|---|---|
| SUCCESS | Danh sách trả đúng người xem, đủ tên/mô tả/chế độ và thứ tự mới nhất; giữ quyền Private/ẩn/xóa, việc mở nhóm là yêu cầu khác. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-004 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-001 | Guest mở trang danh sách nhóm. | Guest không là thành viên; tập N1–N5; có thể đến từ Khám phá Group | M2 | FR-M11-03.01, FR-M11-03.16 |
| M2 | SYSTEM | Hệ thống áp ngữ cảnh liệt kê lối vào UC024 và lọc UC023: chỉ Public N2,N1, không N3 Private, không N4 ẩn/N5 xóa. Trả tên/mô tả/chế độ, sắp tạo mới nhất trước; không mở nhóm hoặc tìm theo tên chỉ vì liệt kê. | N2(05/11,Public), N1(01/11,Public); N3/N4/N5 không hiện; mỗi mục có tên/mô tả/chế độ | END:SUCCESS | FR-M11-03.01, FR-M11-03.02, FR-M11-03.16, FR-M11-03.17, FR-M11-16.01, FR-M11-15.01, FR-M11-17.02, FR-M11-17.07, BR-M11-11, BR-M11-27, BR-M11-23, BR-M11-35 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-004 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Không có nhóm nào còn đủ điều kiện hiển thị | E1.1 | FR-M11-03.01, FR-M11-03.02, FR-M11-03.16, FR-M11-03.17, BR-M11-11, BR-M11-35, FR-M11-16.01, FR-M11-15.01 |
| E2 | system | M2 | Cờ Group Tắt, Guest vẫn xem danh sách như lối vào | E2.1 | FR-M11-03.01, FR-M11-03.02, FR-M11-03.16, FR-M11-03.17, FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, BR-M11-35 |
| E3 | system | M1 | ACT-002 — Chi đăng nhập, là thành viên N3 Private, kể cả danh sách còn khi cờ Tắt. Actor khởi tạo ACT-002; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E3.1 | FR-M11-03.03, FR-M11-03.16, FR-M11-03.01, FR-M11-03.02, FR-M11-03.17, FR-M11-17.07, BR-M11-11, BR-M11-35 |


<!-- sc:branch SC-M11-004 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống lọc cùng quyền Public/Private/ẩn/xóa và trả danh sách rỗng; không tự tạo nhóm hoặc nới quyền Private. | Nhóm ứng viên đều Private người xem không tham gia hoặc Bị ẩn/Đã xóa; results=[] | END:SUCCESS | FR-M11-03.01, FR-M11-03.02, FR-M11-03.16, FR-M11-03.17, BR-M11-11, BR-M11-35, FR-M11-16.01, FR-M11-15.01 |


<!-- sc:branch SC-M11-004 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống giữ lối vào/danh sách và lọc đúng quyền, trả N2,N1 mới nhất trước với tên/mô tả/chế độ. Không mở nhóm ở lần liệt kê này; Guest mở nhóm/bài hoặc tương tác sau đó bị chặn thông báo bận tại SC005, dữ liệu/việc tự làm giữ. | N2,N1 Public; không N3 Private/N4ẩn/N5xóa; Group=false | END:SUCCESS | FR-M11-03.01, FR-M11-03.02, FR-M11-03.16, FR-M11-03.17, FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, BR-M11-35 |


**E3 — thay toàn bộ M1 đến kết thúc:** Chi đăng nhập, là thành viên N3 Private, kể cả danh sách còn khi cờ Tắt. Actor khởi tạo ACT-002; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-004 E3 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E3.1 | ACT-002 | Chi mở danh sách nhóm. | Chi thành viên N3; Group=false; N1/N2 Public | E3.2 | FR-M11-03.03, FR-M11-03.16 |
| E3.2 | SYSTEM | Hệ thống lọc theo thành viên/ẩn/xóa, vẫn giữ danh sách như lối vào khi cờ Tắt, trả N2(05/11),N3(03/11),N1(01/11), đủ tên/mô tả/chế độ. Không cấp quyền mở khi cờ Tắt. | N2 Public,N3 Private,N1 Public; mới nhất trước; chỉ đọc | END:SUCCESS | FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, FR-M11-03.16, FR-M11-03.17, FR-M11-17.07, BR-M11-11, BR-M11-35 |


<!-- sc:end SC-M11-004 -->

<a id="sc-m11-005"></a>

<!-- sc:scenario SC-M11-005 -->

### SC-M11-005

#### 1. Tên kịch bản chuẩn

Mở trang nhóm hoặc đọc nội dung nhóm theo quyền — BF-M11-005; owner [UC-M11-005](../../us/US-M11.md#uc-m11-005); nhóm UC chính: UC-M11-031.

#### 2. Actor thực hiện

ACT-001 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có nhóm/nội dung và lối vào; quyền Private và trạng thái không được giả đạt trước kiểm. Chuẩn Guest mở N11 Public có P11 Đã đăng, không ẩn/tự ẩn/gỡ, tác giả Chi chọn ẩn danh; P-wait Chờ duyệt không là nội dung thường.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-005 -->

| result | condition |
|---|---|
| SUCCESS | Actor nhận đúng thông tin/nội dung và trường tác giả theo lối vào/quyền; preview Private chỉ tên/mô tả, không được coi đã đọc nội dung. Không tự cho quyền tương tác theo dữ liệu đã tải. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-005 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-001 | Guest mở trang N11 để đọc thông tin và bài đã đăng. | N11 Public; P11 ẩn danh, Đã đăng; P-wait Chờ duyệt; Guest | M2 | FR-M11-03.04 |
| M2 | SYSTEM | Hệ thống kiểm UC024: cờ cho phép, nhóm Hoạt động/không ẩn; Khóa vẫn đọc theo quyền. UC023 cho Public, lọc lớp trạng thái nội dung và trả tên/mô tả cùng P11, hiện “Ẩn danh”; không P-wait. Hệ thống giữ tác giả thật Chi, không cấp Guest quyền tương tác chỉ vì được đọc. | N11 Ôn thi Toán/Trao đổi Toán lớp 11; P11 đủ quyền xem, authorLabel=Ẩn danh; storedAuthor=U-C không trả Guest | END:SUCCESS | FR-M11-03.04, FR-M11-03.05, FR-M11-03.06, FR-M11-03.09, FR-M11-03.10, FR-M11-03.11, FR-M11-03.12, FR-M11-03.18, BR-M11-13, BR-M11-14, BR-M11-17, BR-M11-33, FR-M11-16.03, FR-M03-04.02, FR-M03-07.02 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-005 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Guest mở link mời của N12 Private chỉ để đọc giới thiệu | E1.1 | FR-M11-03.18, FR-M11-03.06, FR-M11-04.05, BR-M11-12, BR-M11-13, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E2 | system | M2 | N11 đã là Private ở lúc Guest mở bằng link thường/bookmark/thông báo | E2.1 | FR-M11-03.06, BR-M11-13, BR-M11-15 |
| E3 | system | M2 | N11 chuyển Public→Private sau lần tải trước, Guest tải lại/mở lại nội dung | E3.1 | FR-M11-02.12, FR-M11-02.13, BR-M11-15 |
| E4 | system | M2 | P11 đã bị gỡ khỏi nhóm; Guest không thuộc tập xem còn lại | E4.1 | FR-M11-14.01, BR-M11-30 |
| E5 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E5.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E6 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E6.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E7 | system | M1 | ACT-009 — Lan là Member N12 Private, P11 đủ quyền đọc và đăng ẩn danh. Actor khởi tạo ACT-009; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M11-03.05, FR-M11-03.04, FR-M11-03.06, FR-M11-03.09, FR-M11-03.10, FR-M11-03.11, FR-M11-03.12, FR-M11-03.18, BR-M11-13, BR-M11-14, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E8 | system | M1 | ACT-010 — Bình là Group Mod N12 Private, P11 đủ quyền đọc và đăng ẩn danh. Actor khởi tạo ACT-010; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M11-03.05, FR-M11-03.04, FR-M11-03.06, FR-M11-03.09, FR-M11-03.10, FR-M11-03.11, FR-M11-03.12, FR-M11-03.18, BR-M11-13, BR-M11-14, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E9 | system | M1 | ACT-011 — An là Owner N12 Private, P11 đủ quyền đọc và đăng ẩn danh. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M11-03.05, FR-M11-03.04, FR-M11-03.06, FR-M11-03.09, FR-M11-03.10, FR-M11-03.11, FR-M11-03.12, FR-M11-03.18, BR-M11-13, BR-M11-14, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E10 | system | M1 | ACT-008 — Minh không là thành viên N12 Private, mở từ vụ báo cáo mình đang giữ M08. Actor khởi tạo ACT-008; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M11-03.12, FR-M11-03.10, BR-M11-17, BR-M11-33, FR-M08-04.06 |
| E11 | system | M1 | ACT-008 — Minh không là thành viên Private, mở trang thường. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E11.1 | FR-M11-03.11, FR-M11-03.06, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E12 | system | M1 | ACT-008 — Minh đọc Public, thấy danh tính thật; ADMIN có thể đọc khi cờ Tắt. Actor khởi tạo ACT-008; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E12.1 | FR-M11-03.04, FR-M11-03.10, FR-M11-17.03, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E13 | system | M1 | ACT-007 — Hòa không là thành viên N12 Private, mở từ vụ báo cáo mình đang giữ M08. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E13.1 | FR-M11-03.12, FR-M11-03.10, BR-M11-17, BR-M11-33, FR-M08-04.06 |
| E14 | system | M1 | ACT-007 — Hòa không là thành viên Private, mở trang thường. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E14.1 | FR-M11-03.11, FR-M11-03.06, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E15 | system | M1 | ACT-007 — Hòa đọc Public, thấy danh tính thật; ADMIN có thể đọc khi cờ Tắt. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E15.1 | FR-M11-03.04, FR-M11-03.10, FR-M11-17.03, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E16 | system | M1 | ACT-002 — Phúc ngoài nhóm nhưng đã đăng nhập đọc Public. Actor khởi tạo ACT-002; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E16.1 | FR-M11-03.04, FR-M11-03.09, FR-M11-03.13, BR-M11-13, BR-M11-17, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E17 | system | M1 | ACT-009 — Chi đọc chính P11 bị gỡ ở nhóm Public còn hoạt động. Actor khởi tạo ACT-009; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E17.1 | FR-M11-14.01, FR-M11-14.03, FR-M11-14.05, FR-M11-14.07, BR-M11-30, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-005 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-001 | Guest mở LINK-N12. | Private; Guest chưa thành viên; LINK-N12 là link mời chung | E1.2 | FR-M11-03.18 |
| E1.2 | SYSTEM | Hệ thống kiểm nhóm/cờ cho phép lối mở, chỉ trả tên và mô tả N12 để tham gia; không bài/bình luận/danh sách thành viên hoặc tự thêm Member. Muốn gia nhập Guest bị yêu cầu đăng nhập theo SC007. | N12 tên=CLB Hóa; mô tả=Trao đổi Hóa; previewOnly=true; chưa Member | END:SUCCESS | FR-M11-03.06, FR-M11-03.18, FR-M11-04.05, BR-M11-12, BR-M11-13, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-005 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống không trả thông tin/nội dung Private cho người ngoài; quyền Public trước đây không còn đủ. | N11 Private; Guest không thành viên; không phải lời mời | END:REJECTED | FR-M11-03.06, BR-M11-13, BR-M11-15 |


<!-- sc:branch SC-M11-005 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống trả “Nội dung không tồn tại”; không dùng bản đã tải hoặc bookmark/thông báo để cấp quyền xem lần mới. | Bản tải09:55; N11 Private từ10:00; yêu cầu mới10:01; P11 không được trả | END:REJECTED | FR-M11-02.12, FR-M11-02.13, BR-M11-15 |


<!-- sc:branch SC-M11-005 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống áp thêm lớp dấu gỡ, không hiển thị P11 cho Guest; trạng thái đăng vẫn Đã đăng, dữ liệu/điểm giữ. | P11 Đã đăng và removedFromGroup=true; Guest không tác giả/nhóm staff/hệ thống staff | END:REJECTED | FR-M11-14.01, BR-M11-30 |


<!-- sc:branch SC-M11-005 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-005 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


**E7 — thay toàn bộ M1 đến kết thúc:** Lan là Member N12 Private, P11 đủ quyền đọc và đăng ẩn danh. Actor khởi tạo ACT-009; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-005 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-009 | Lan mở trang N12 và P11. | N12 Private; Lan thành viên; P11 Đã đăng/không ẩn/gỡ; tác giả Chi; anonymous=true | E7.2 | FR-M11-03.05 |
| E7.2 | SYSTEM | Hệ thống kiểm cờ/trạng thái, Private cho thành viên; trả tên/mô tả và P11 với nhãn tác giả Ẩn danh. Không hiện bài chờ cho người xem thường hoặc cấp quyền staff hệ thống từ role nhóm. | N12 Private; authorLabel=Ẩn danh; storedAuthor=Chi; membership=Member | END:SUCCESS | FR-M11-03.04, FR-M11-03.05, FR-M11-03.06, FR-M11-03.09, FR-M11-03.10, FR-M11-03.11, FR-M11-03.12, FR-M11-03.18, BR-M11-13, BR-M11-14, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E8 — thay toàn bộ M1 đến kết thúc:** Bình là Group Mod N12 Private, P11 đủ quyền đọc và đăng ẩn danh. Actor khởi tạo ACT-010; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-005 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-010 | Bình mở trang N12 và P11. | N12 Private; Bình thành viên; P11 Đã đăng/không ẩn/gỡ; tác giả Chi; anonymous=true | E8.2 | FR-M11-03.05 |
| E8.2 | SYSTEM | Hệ thống kiểm cờ/trạng thái, Private cho thành viên; trả tên/mô tả và P11 với nhãn tác giả Chi. Không hiện bài chờ cho người xem thường hoặc cấp quyền staff hệ thống từ role nhóm. | N12 Private; authorLabel=Chi; storedAuthor=Chi; membership=Group Mod | END:SUCCESS | FR-M11-03.04, FR-M11-03.05, FR-M11-03.06, FR-M11-03.09, FR-M11-03.10, FR-M11-03.11, FR-M11-03.12, FR-M11-03.18, BR-M11-13, BR-M11-14, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E9 — thay toàn bộ M1 đến kết thúc:** An là Owner N12 Private, P11 đủ quyền đọc và đăng ẩn danh. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-005 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-011 | An mở trang N12 và P11. | N12 Private; An thành viên; P11 Đã đăng/không ẩn/gỡ; tác giả Chi; anonymous=true | E9.2 | FR-M11-03.05 |
| E9.2 | SYSTEM | Hệ thống kiểm cờ/trạng thái, Private cho thành viên; trả tên/mô tả và P11 với nhãn tác giả Chi. Không hiện bài chờ cho người xem thường hoặc cấp quyền staff hệ thống từ role nhóm. | N12 Private; authorLabel=Chi; storedAuthor=Chi; membership=Owner | END:SUCCESS | FR-M11-03.04, FR-M11-03.05, FR-M11-03.06, FR-M11-03.09, FR-M11-03.10, FR-M11-03.11, FR-M11-03.12, FR-M11-03.18, BR-M11-13, BR-M11-14, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E10 — thay toàn bộ M1 đến kết thúc:** Minh không là thành viên N12 Private, mở từ vụ báo cáo mình đang giữ M08. Actor khởi tạo ACT-008; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-005 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-008 | Minh mở nội dung P11 trong vụ báo cáo C11 mình đang giữ. | C11 đang giữ bởiMinh; targetP11/N12 Private/ẩn danh; không mở trang nhóm | E10.2 | FR-M11-03.12 |
| E10.2 | SYSTEM | Hệ thống cho xem đúng nội dung Private trong ngữ cảnh vụ đang giữ và hiện tác giả thật Chi. Trả dữ liệu cho việc đọc nội dung trong vụ, không cấp trang nhóm/danh sách thành viên/queue nhóm. Việc xét và kết luận vụ vẫn thuộc M08. | P11 nội dung và author Chi trong C11; không phải quyền toàn N12 | END:SUCCESS | FR-M11-03.10, FR-M11-03.12, BR-M11-17, BR-M11-33, FR-M08-04.06 |


**E11 — thay toàn bộ M1 đến kết thúc:** Minh không là thành viên Private, mở trang thường. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-005 E11 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E11.1 | ACT-008 | Minh mở trang N12 Private bằng link thường. | Không thành viên/không ngữ cảnh vụ đang giữ; Group=true | E11.2 | FR-M11-03.11 |
| E11.2 | SYSTEM | Hệ thống không trả trang/thông tin/nội dung Private vì không là thành viên. Quyền thấy danh tính thật không cấp quyền mở nhóm. | N12 Private; không tiết lộ nội dung | END:REJECTED | FR-M11-03.06, FR-M11-03.11, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E12 — thay toàn bộ M1 đến kết thúc:** Minh đọc Public, thấy danh tính thật; ADMIN có thể đọc khi cờ Tắt. Actor khởi tạo ACT-008; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-005 E12 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E12.1 | ACT-008 | Minh mở P11 của N11 Public. | N11 Public; P11 Đã đăng/ẩn danh; Group=true; Minh MODERATOR | E12.2 | FR-M11-03.04, FR-M11-03.10 |
| E12.2 | SYSTEM | Hệ thống kiểm điều kiện mở, Public cho đọc; trả P11 với tác giả thật Chi theo quyền hệ thống, dữ liệu ẩn danh trong bài không bị xóa. | authorLabel=Chi; storedAuthorChi; anonymous=true; chỉ đọc | END:SUCCESS | FR-M11-03.04, FR-M11-03.10, FR-M11-17.03, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E13 — thay toàn bộ M1 đến kết thúc:** Hòa không là thành viên N12 Private, mở từ vụ báo cáo mình đang giữ M08. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-005 E13 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E13.1 | ACT-007 | Hòa mở nội dung P11 trong vụ báo cáo C11 mình đang giữ. | C11 đang giữ bởiHòa; targetP11/N12 Private/ẩn danh; không mở trang nhóm | E13.2 | FR-M11-03.12 |
| E13.2 | SYSTEM | Hệ thống cho xem đúng nội dung Private trong ngữ cảnh vụ đang giữ và hiện tác giả thật Chi. Trả dữ liệu cho việc đọc nội dung trong vụ, không cấp trang nhóm/danh sách thành viên/queue nhóm. Việc xét và kết luận vụ vẫn thuộc M08. | P11 nội dung và author Chi trong C11; không phải quyền toàn N12 | END:SUCCESS | FR-M11-03.10, FR-M11-03.12, BR-M11-17, BR-M11-33, FR-M08-04.06 |


**E14 — thay toàn bộ M1 đến kết thúc:** Hòa không là thành viên Private, mở trang thường. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-005 E14 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E14.1 | ACT-007 | Hòa mở trang N12 Private bằng link thường. | Không thành viên/không ngữ cảnh vụ đang giữ; Group=false nhưng có ADMIN | E14.2 | FR-M11-03.11 |
| E14.2 | SYSTEM | Hệ thống cho ADMIN qua cờ rồi không trả trang/thông tin/nội dung Private vì không là thành viên. Quyền thấy danh tính thật không cấp quyền mở nhóm. | N12 Private; không tiết lộ nội dung | END:REJECTED | FR-M11-03.06, FR-M11-03.11, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E15 — thay toàn bộ M1 đến kết thúc:** Hòa đọc Public, thấy danh tính thật; ADMIN có thể đọc khi cờ Tắt. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-005 E15 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E15.1 | ACT-007 | Hòa mở P11 của N11 Public. | N11 Public; P11 Đã đăng/ẩn danh; Group=false; Hòa ADMIN | E15.2 | FR-M11-03.04, FR-M11-03.10 |
| E15.2 | SYSTEM | Hệ thống kiểm điều kiện mở, cho ADMIN qua cờ, Public cho đọc; trả P11 với tác giả thật Chi theo quyền hệ thống, dữ liệu ẩn danh trong bài không bị xóa. | authorLabel=Chi; storedAuthorChi; anonymous=true; chỉ đọc | END:SUCCESS | FR-M11-03.04, FR-M11-03.10, FR-M11-17.03, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E16 — thay toàn bộ M1 đến kết thúc:** Phúc ngoài nhóm nhưng đã đăng nhập đọc Public. Actor khởi tạo ACT-002; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-005 E16 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E16.1 | ACT-002 | Phúc mở P11 của N11 Public. | Phúc không thành viên; P11 Đã đăng/ẩn danh; Group=true | E16.2 | FR-M11-03.04 |
| E16.2 | SYSTEM | Hệ thống kiểm quyền, trả Public với nhãn Ẩn danh. Các yêu cầu bình luận/vote/báo cáo/bookmark được phép theo lớp nhóm, owner M04/M12/M08/M02 vẫn kiểm từng chức năng; không thực hiện tương tác chỉ vì đọc. | P11 authorLabel=Ẩn danh; Phúc không thể gửi bài mới vào nhóm nếu chưa tham gia | END:SUCCESS | FR-M11-03.04, FR-M11-03.09, FR-M11-03.13, BR-M11-13, BR-M11-17, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E17 — thay toàn bộ M1 đến kết thúc:** Chi đọc chính P11 bị gỡ ở nhóm Public còn hoạt động. Actor khởi tạo ACT-009; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-005 E17 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E17.1 | ACT-009 | Chi mở P11 của mình sau khi bị nhóm gỡ. | Chi tác giả; N11 Public; P11 Đã đăng/removed=true; Group=true | E17.2 | FR-M11-14.01 |
| E17.2 | SYSTEM | Hệ thống kiểm các lớp xem, Public và tập tác giả cho Chi đọc nội dung bị gỡ; giữ trạng thái Đã đăng và dấu gỡ/ẩn danh. Không cho tự hiện lại hoặc khiếu nại cấp nhóm. | Nội dung P11 trả cho tác giả; removed=true; điểm giữ 20 | END:SUCCESS | FR-M11-14.01, FR-M11-14.03, FR-M11-14.05, FR-M11-14.07, BR-M11-30, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-005 -->

<a id="sc-m11-006"></a>

<!-- sc:scenario SC-M11-006 -->

### SC-M11-006

#### 1. Tên kịch bản chuẩn

Xem danh sách thành viên kèm vai trò nhóm — BF-M11-006; owner [UC-M11-006](../../us/US-M11.md#uc-m11-006); nhóm UC chính: UC-M11-031, UC-M11-032.

#### 2. Actor thực hiện

ACT-001 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có nhóm và ngữ cảnh yêu cầu xem, không cần đăng nhập cho Public; preview lời mời Private không là quyền xem trang. Chuẩn N11 Public.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-006 -->

| result | condition |
|---|---|
| SUCCESS | Danh sách thành viên/role đúng nhóm được trả cho người có quyền xem trang; không thay vai trò/thành viên hoặc cấp quyền quản trị. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-006 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-001 | Guest yêu cầu xem danh sách thành viên N11. | N11 Public; Guest; dữ liệu An Owner/Bình Group Mod/Chi Member | M2 | FR-M11-03.14 |
| M2 | SYSTEM | Hệ thống kiểm UC024 và quyền trang nhóm UC023; Public cho Guest. Trả thành viên cùng vai trò trong N11: An Owner, Bình/Dũng Group Mod, Chi/Lan Member. Không tự cấp quyền bổ nhiệm/kick/chuyển Owner từ việc đọc danh sách. | An Owner, Bình Group Mod bổ nhiệm 01/09/2026 09:00+07, Dũng Group Mod bổ nhiệm lại 20/10/2026 09:00+07 (lần trước không tính), Chi Member vào 01/08/2026, Lan Member vào 01/07/2026. Đây là snapshot chuẩn, từng chức năng có thể thay dữ liệu đích ghi ngay tại bước. | END:SUCCESS | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-006 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E1.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E2 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E2.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E3 | system | M1 | ACT-002 — Phúc ngoài N12 Private, kể cả chỉ có preview lời mời hoặc quyền hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E3.1 | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E4 | system | M1 | ACT-009 — Chi có quyền trang N12 Private. Actor khởi tạo ACT-009; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E5 | system | M1 | ACT-011 — An có quyền trang N12 Private. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E6 | system | M1 | ACT-007 — Hòa ngoài N12 Private, kể cả chỉ có preview lời mời hoặc quyền hệ thống. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E7 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng quyền Public; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M11-03.14, FR-M11-17.03, FR-M10-12.08, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-006 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-006 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


**E3 — thay toàn bộ M1 đến kết thúc:** Phúc ngoài N12 Private, kể cả chỉ có preview lời mời hoặc quyền hệ thống. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-006 E3 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E3.1 | ACT-002 | Phúc yêu cầu danh sách thành viên N12. | Private; thành viên=False; không ngữ cảnh xem trang được cấp từ vụ/preview | E3.2 | FR-M11-03.14, FR-M11-03.15 |
| E3.2 | SYSTEM | Hệ thống kiểm quyền trang/nhóm/cờ và không trả danh sách vì không được xem trang Private; preview/vụ riêng không là quyền xem danh sách. | N12; danh sách không được tiết lộ | END:REJECTED | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E4 — thay toàn bộ M1 đến kết thúc:** Chi có quyền trang N12 Private. Actor khởi tạo ACT-009; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-006 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-009 | Chi yêu cầu danh sách thành viên N12. | Private; thành viên=True; không ngữ cảnh xem trang được cấp từ vụ/preview | E4.2 | FR-M11-03.14, FR-M11-03.15 |
| E4.2 | SYSTEM | Hệ thống kiểm quyền trang/nhóm/cờ và trả thành viên kèm vai trò của N12, không đổi role. | An Owner, Bình Group Mod bổ nhiệm 01/09/2026 09:00+07, Dũng Group Mod bổ nhiệm lại 20/10/2026 09:00+07 (lần trước không tính), Chi Member vào 01/08/2026, Lan Member vào 01/07/2026. Đây là snapshot chuẩn, từng chức năng có thể thay dữ liệu đích ghi ngay tại bước. | END:SUCCESS | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E5 — thay toàn bộ M1 đến kết thúc:** An có quyền trang N12 Private. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-006 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-011 | An yêu cầu danh sách thành viên N12. | Private; thành viên=True; không ngữ cảnh xem trang được cấp từ vụ/preview | E5.2 | FR-M11-03.14, FR-M11-03.15 |
| E5.2 | SYSTEM | Hệ thống kiểm quyền trang/nhóm/cờ và trả thành viên kèm vai trò của N12, không đổi role. | An Owner, Bình Group Mod bổ nhiệm 01/09/2026 09:00+07, Dũng Group Mod bổ nhiệm lại 20/10/2026 09:00+07 (lần trước không tính), Chi Member vào 01/08/2026, Lan Member vào 01/07/2026. Đây là snapshot chuẩn, từng chức năng có thể thay dữ liệu đích ghi ngay tại bước. | END:SUCCESS | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E6 — thay toàn bộ M1 đến kết thúc:** Hòa ngoài N12 Private, kể cả chỉ có preview lời mời hoặc quyền hệ thống. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-006 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-007 | Hòa yêu cầu danh sách thành viên N12. | Private; thành viên=False; không ngữ cảnh xem trang được cấp từ vụ/preview | E6.2 | FR-M11-03.14, FR-M11-03.15 |
| E6.2 | SYSTEM | Hệ thống kiểm quyền trang/nhóm/cờ và không trả danh sách vì không được xem trang Private; preview/vụ riêng không là quyền xem danh sách. | N12; danh sách không được tiết lộ | END:REJECTED | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E7 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng quyền Public; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-006 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-007 | Hòa yêu cầu xem danh sách thành viên N11. | N11 Public; Hòa; dữ liệu An Owner/Bình Group Mod/Chi Member; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E7.2 | FR-M11-03.14, FR-M11-17.03, FR-M10-12.08 |
| E7.2 | SYSTEM | Hệ thống kiểm UC024 và quyền trang nhóm UC023; Public cho Hòa. Trả thành viên cùng vai trò trong N11: An Owner, Bình/Dũng Group Mod, Chi/Lan Member. Không tự cấp quyền bổ nhiệm/kick/chuyển Owner từ việc đọc danh sách. | An Owner, Bình Group Mod bổ nhiệm 01/09/2026 09:00+07, Dũng Group Mod bổ nhiệm lại 20/10/2026 09:00+07 (lần trước không tính), Chi Member vào 01/08/2026, Lan Member vào 01/07/2026. Đây là snapshot chuẩn, từng chức năng có thể thay dữ liệu đích ghi ngay tại bước. | END:SUCCESS | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


<!-- sc:end SC-M11-006 -->

<a id="sc-m11-007"></a>

<!-- sc:scenario SC-M11-007 -->

### SC-M11-007

#### 1. Tên kịch bản chuẩn

Tham gia nhóm hoặc gửi yêu cầu gia nhập theo cổng nhóm — BF-M11-007; owner [UC-M11-007](../../us/US-M11.md#uc-m11-007); nhóm UC chính: UC-M11-032.

#### 2. Actor thực hiện

ACT-002 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có nhóm/lối vào. Chuẩn Phúc chưa tham gia N11 Public không câu hỏi, không bị chặn và không có yêu cầu Chờ duyệt; các điều kiện được kiểm khi yêu cầu. Tham gia 100 nhóm trước đây không chặn chức năng.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-007 -->

| result | condition |
|---|---|
| SUCCESS | Vào ngay: Member với mốc T và không thông báo. Nhóm cần duyệt: đúng một yêu cầu Chờ duyệt của người gửi, câu trả lời đúng nếu có câu hỏi, báo Owner/Group Mod; chưa là Member. Mục tiêu gửi yêu cầu hoàn tất ở xác nhận đã ghi nhận, không giả đã duyệt. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-007 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Phúc chọn Tham gia N11. | N11 Public, không câu hỏi; Phúc người ngoài; T; có thể đến từ LINK-N11 | M2 | FR-M11-04.01, FR-M11-05.05 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm đăng nhập, nhóm không Khóa, Phúc không bị nhóm chặn và không có yêu cầu Chờ duyệt trùng. Public không câu hỏi nên thêm ngay Member với thời điểm tham gia=lúc chọn T; không giới hạn tổng nhóm. Không phát thông báo vào ngay. Trả kết quả đã tham gia. | U-P ngoài nhóm→Member; joinAt=T; không tạo yêu cầu Chờ duyệt hoặc lời mời riêng | END:SUCCESS | FR-M11-04.01, FR-M11-04.06, FR-M11-04.07, FR-M11-04.09, FR-M11-05.04, FR-M11-05.05, FR-M11-06.08, BR-M11-03, BR-M11-07, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-007 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Public có câu hỏi cần gửi yêu cầu | E1.1 | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |
| E2 | user-choice | M1 | Private không câu hỏi cần gửi yêu cầu | E2.1 | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |
| E3 | user-choice | M1 | Private có câu hỏi cần gửi yêu cầu | E3.1 | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |
| E4 | system | M1 | Nhóm có câu hỏi, Phúc gửi trống rồi bổ sung câu trả lời | E4.1 | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |
| E5 | system | M2 | Phúc đang có R11 Chờ duyệt tới N11 | E5.1 | FR-M11-04.09, BR-M11-09 |
| E6 | system | M1 | Phúc đang bị N11 chặn và vào bằng vào ngay | E6.1 | FR-M11-04.06, BR-M11-10 |
| E7 | system | M1 | Phúc đang bị N11 chặn và vào bằng gửi yêu cầu | E7.1 | FR-M11-04.06, BR-M11-10 |
| E8 | system | M1 | Phúc đang bị N11 chặn và vào bằng LINK-N11/lời mời | E8.1 | FR-M11-04.06, BR-M11-10 |
| E9 | system | M1 | Phúc từng bị từ chối/rời/kick, không bị chặn và quay lại ngay | E9.1 | FR-M11-04.04, FR-M11-04.07, FR-M11-09.07, FR-M11-04.01, FR-M11-04.06, FR-M11-04.09, FR-M11-05.04, FR-M11-05.05, FR-M11-06.08, BR-M11-03, BR-M11-07, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E10 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E10.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E11 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E11.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E12 | system | M2 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | E12.1 | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |
| E13 | system | M1 | ACT-001 — Guest yêu cầu tham gia kể cả qua link mời. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E13.1 | FR-M11-04.05, BR-M11-07 |
| E14 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng ngữ cảnh người dùng/người gửi; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E14.1 | FR-M11-04.01, FR-M11-05.05, FR-M11-17.03, FR-M10-12.08, FR-M11-04.06, FR-M11-04.07, FR-M11-04.09, FR-M11-05.04, FR-M11-06.08, BR-M11-03, BR-M11-07, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-007 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Phúc chọn tham gia N11 qua lối được phép. | group=N11; mode=Public; question=Bạn học lớp mấy?; không blocked/không pending | E1.2 | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E1.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm đăng nhập/không Khóa/không chặn/không trùng Chờ duyệt, trả câu hỏi của nhóm; chưa tạo yêu cầu khi chưa nhận câu trả lời. | Bạn học lớp mấy?; câu trả lời bắt buộc khi có câu hỏi | E1.3 | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E1.3 | ACT-002 | Phúc nhập câu trả lời và gửi yêu cầu gia nhập. | N11; answer=11 | E1.4 | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E1.4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm đăng nhập/nhóm cho phép, không chặn/không pending và câu trả lời không trống. Tạo R11 Chờ duyệt, lưu câu trả lời đã gửi khi có; M07 thông báo yêu cầu mới tới Owner/các Group Mod. Trả đã ghi nhận yêu cầu, chưa thêm Member. | R11/U-P/N11/Chờ duyệt; answer=11; recipients=An,Bình,Dũng; U-P vẫn ngoài nhóm | END:SUCCESS | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |


<!-- sc:branch SC-M11-007 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | Phúc chọn tham gia N12 qua lối được phép. | group=N12; mode=Private; question=trống; không blocked/không pending | E2.2 | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E2.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm đăng nhập/nhóm cho phép, không chặn/không pending và không buộc câu trả lời vì không có câu hỏi. Tạo R11 Chờ duyệt, lưu câu trả lời đã gửi khi có; M07 thông báo yêu cầu mới tới Owner/các Group Mod. Trả đã ghi nhận yêu cầu, chưa thêm Member. | R11/U-P/N12/Chờ duyệt; answer=không có; recipients=An,Bình,Dũng; U-P vẫn ngoài nhóm | END:SUCCESS | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |


<!-- sc:branch SC-M11-007 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-002 | Phúc chọn tham gia N12 qua lối được phép. | group=N12; mode=Private; question=Bạn học lớp mấy?; không blocked/không pending | E3.2 | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E3.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm đăng nhập/không Khóa/không chặn/không trùng Chờ duyệt, trả câu hỏi của nhóm; chưa tạo yêu cầu khi chưa nhận câu trả lời. | Bạn học lớp mấy?; câu trả lời bắt buộc khi có câu hỏi | E3.3 | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E3.3 | ACT-002 | Phúc nhập câu trả lời và gửi yêu cầu gia nhập. | N12; answer=11 | E3.4 | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E3.4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm đăng nhập/nhóm cho phép, không chặn/không pending và câu trả lời không trống. Tạo R11 Chờ duyệt, lưu câu trả lời đã gửi khi có; M07 thông báo yêu cầu mới tới Owner/các Group Mod. Trả đã ghi nhận yêu cầu, chưa thêm Member. | R11/U-P/N12/Chờ duyệt; answer=11; recipients=An,Bình,Dũng; U-P vẫn ngoài nhóm | END:SUCCESS | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |


<!-- sc:branch SC-M11-007 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-002 | Phúc chọn tham gia N12 qua lối được phép. | group=N12; mode=Private; question=Bạn học lớp mấy?; không blocked/không pending | E4.2 | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E4.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm đăng nhập/không Khóa/không chặn/không trùng Chờ duyệt, trả câu hỏi của nhóm; chưa tạo yêu cầu khi chưa nhận câu trả lời. | Bạn học lớp mấy?; câu trả lời bắt buộc khi có câu hỏi | E4.3 | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E4.3 | ACT-002 | Phúc gửi yêu cầu với câu trả lời trống. | N12; answer=""; chưa pending | E4.4 | FR-M11-04.08 |
| E4.4 | SYSTEM | Hệ thống từ chối gửi vì nhóm có câu hỏi mà chưa trả lời; chưa tạo yêu cầu Chờ duyệt. | R11 chưa tồn tại; không thêm Member | E4.5 | FR-M11-04.08, BR-M11-08 |
| E4.5 | ACT-002 | Phúc nhập câu trả lời và gửi yêu cầu gia nhập. | N12; answer=11 | E4.6 | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E4.6 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm đăng nhập/nhóm cho phép, không chặn/không pending và câu trả lời không trống. Tạo R11 Chờ duyệt, lưu câu trả lời đã gửi khi có; M07 thông báo yêu cầu mới tới Owner/các Group Mod. Trả đã ghi nhận yêu cầu, chưa thêm Member. | R11/U-P/N12/Chờ duyệt; answer=11; recipients=An,Bình,Dũng; U-P vẫn ngoài nhóm | END:SUCCESS | FR-M11-04.02, FR-M11-04.03, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-05.05, FR-M11-06.07, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |


<!-- sc:branch SC-M11-007 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối gửi thêm yêu cầu cùng nhóm, giữ R11 hiện tại; người gửi có thể rút bằng SC008. | R11 Chờ duyệt; không tạo R12 trùng | END:REJECTED | FR-M11-04.09, BR-M11-09 |


<!-- sc:branch SC-M11-007 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-002 | Phúc yêu cầu gia nhập N11 bằng vào ngay. | U-P thuộc blocked N11; Group=true; N11 không Khóa | E6.2 | FR-M11-04.06 |
| E6.2 | SYSTEM | Hệ thống kiểm chặn và từ chối mọi cách gia nhập, không tạo thành viên/yêu cầu mới. | blockedU-P giữ; lời mời không vượt chặn | END:REJECTED | FR-M11-04.06, BR-M11-10 |


<!-- sc:branch SC-M11-007 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | ACT-002 | Phúc yêu cầu gia nhập N11 bằng gửi yêu cầu. | U-P thuộc blocked N11; Group=true; N11 không Khóa | E7.2 | FR-M11-04.06 |
| E7.2 | SYSTEM | Hệ thống kiểm chặn và từ chối mọi cách gia nhập, không tạo thành viên/yêu cầu mới. | blockedU-P giữ; lời mời không vượt chặn | END:REJECTED | FR-M11-04.06, BR-M11-10 |


<!-- sc:branch SC-M11-007 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | ACT-002 | Phúc yêu cầu gia nhập N11 bằng LINK-N11/lời mời. | U-P thuộc blocked N11; Group=true; N11 không Khóa | E8.2 | FR-M11-04.06 |
| E8.2 | SYSTEM | Hệ thống kiểm chặn và từ chối mọi cách gia nhập, không tạo thành viên/yêu cầu mới. | blockedU-P giữ; lời mời không vượt chặn | END:REJECTED | FR-M11-04.06, BR-M11-10 |


<!-- sc:branch SC-M11-007 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | ACT-002 | Phúc chọn tham gia lại N11 Public không câu hỏi. | R-old Đã từ chối lúc09:59 hoặc đã rời/kick; hiện10:00; không pending/blocked; đã tham gia100 nhóm khác | E9.2 | FR-M11-04.04, FR-M11-04.07, FR-M11-09.07 |
| E9.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm đăng nhập, nhóm không Khóa, Phúc không bị nhóm chặn và không có yêu cầu Chờ duyệt trùng. Public không câu hỏi nên thêm ngay Member với thời điểm tham gia=lúc chọn T; không giới hạn tổng nhóm. Không phát thông báo vào ngay. Trả kết quả đã tham gia. | U-P ngoài nhóm→Member; joinAt=T; không tạo yêu cầu Chờ duyệt hoặc lời mời riêng | END:SUCCESS | FR-M11-04.01, FR-M11-04.06, FR-M11-04.07, FR-M11-04.09, FR-M11-05.04, FR-M11-05.05, FR-M11-06.08, BR-M11-03, BR-M11-07, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-007 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-007 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-007 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | SYSTEM | Hệ thống từ chối hành vi trong nhóm Bị khóa kể cả Owner/Group Mod hoặc ADMIN; quyền đọc/lưu/báo cáo/Member-Group Mod tự rời và tự kế nhiệm theo hợp đồng riêng vẫn giữ. | Nhóm Bị khóa; không thực hiện thay đổi/duyệt/nhận mở queue bị chặn | END:REJECTED | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |


**E13 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu tham gia kể cả qua link mời. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-007 E13 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E13.1 | ACT-001 | Guest chọn tham gia N12 từ LINK-N12. | Guest chưa đăng nhập; nhóm Private/có câu hỏi | E13.2 | FR-M11-04.05 |
| E13.2 | SYSTEM | Hệ thống từ chối và yêu cầu đăng nhập theo M01; chưa ghi yêu cầu/thành viên. Đây là từ chối hợp lệ của lần chưa đăng nhập, không tự include toàn phiên xác thực vào M11. | Chưa Member/chưa yêu cầu mới; muốn tiếp tục phải đăng nhập rồi chủ động thực hiện SC007 | END:REJECTED | FR-M11-04.05, BR-M11-07 |


**E14 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng ngữ cảnh người dùng/người gửi; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-007 E14 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E14.1 | ACT-007 | Hòa chọn Tham gia N11. | N11 Public, không câu hỏi; Hòa người ngoài; T; có thể đến từ LINK-N11; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E14.2 | FR-M11-04.01, FR-M11-05.05, FR-M11-17.03, FR-M10-12.08 |
| E14.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm đăng nhập, nhóm không Khóa, Hòa không bị nhóm chặn và không có yêu cầu Chờ duyệt trùng. Public không câu hỏi nên thêm ngay Member với thời điểm tham gia=lúc chọn T; không giới hạn tổng nhóm. Không phát thông báo vào ngay. Trả kết quả đã tham gia. | U-H ngoài nhóm→Member; joinAt=T; không tạo yêu cầu Chờ duyệt hoặc lời mời riêng | END:SUCCESS | FR-M11-04.01, FR-M11-04.06, FR-M11-04.07, FR-M11-04.09, FR-M11-05.04, FR-M11-05.05, FR-M11-06.08, BR-M11-03, BR-M11-07, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


<!-- sc:end SC-M11-007 -->

<a id="sc-m11-008"></a>

<!-- sc:scenario SC-M11-008 -->

### SC-M11-008

#### 1. Tên kịch bản chuẩn

Rút yêu cầu tham gia đang chờ của mình — BF-M11-008; owner [UC-M11-008](../../us/US-M11.md#uc-m11-008); nhóm UC chính: UC-M11-032.

#### 2. Actor thực hiện

ACT-002 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có R11 của Phúc tới N12 Bình thường, đang Chờ duyệt, chưa là Member; quyền sở hữu/trạng thái/cờ được kiểm. Rút khi Bị khóa chưa có hợp đồng, GAP004.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-008 -->

| result | condition |
|---|---|
| SUCCESS | Yêu cầu của người gửi chuyển Đã rút, dữ liệu được giữ, actor nhận kết quả; không tạo thành viên. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-008 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Phúc yêu cầu rút R11 của mình. | R11/U-P/N12/Chờ duyệt; không xóa bản ghi yêu cầu | M2 | FR-M11-04.10 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm R11 thuộc Phúc và còn Chờ duyệt; chuyển R11→Đã rút, giữ dữ liệu yêu cầu. Trả kết quả đã rút, không thêm Phúc làm Member. | R11 Chờ duyệt→Đã rút; U-P vẫn người ngoài N12 | END:SUCCESS | FR-M11-04.10, BR-M11-36, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-008 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | R11 đã Đã chấp nhận/Đã từ chối/Đã rút khi xử lý | E1.1 | FR-M11-04.10, BR-M11-36 |
| E2 | system | M1 | Phúc yêu cầu rút R-other của Xuân | E2.1 | FR-M11-04.10, BR-M11-36 |
| E3 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E3.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E4 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E4.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E5 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng ngữ cảnh người dùng/người gửi; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M11-04.10, FR-M11-17.03, FR-M10-12.08, BR-M11-36, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-008 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống không rút yêu cầu không còn Chờ duyệt; giữ trạng thái hiện tại, không xóa hoặc đưa thành viên đã vào ra khỏi nhóm. | R11 hiện tại không Chờ duyệt; không có lần rút mới | END:REJECTED | FR-M11-04.10, BR-M11-36 |


<!-- sc:branch SC-M11-008 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | Phúc chọn rút R-other. | R-other/U-X/N12/Chờ duyệt; actorU-P | E2.2 | FR-M11-04.10 |
| E2.2 | SYSTEM | Hệ thống kiểm người gửi và không cho rút yêu cầu người khác. | R-other vẫn Chờ duyệt; không xóa | END:REJECTED | FR-M11-04.10, BR-M11-36 |


<!-- sc:branch SC-M11-008 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-008 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


**E5 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng ngữ cảnh người dùng/người gửi; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-008 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-007 | Hòa yêu cầu rút R11 của mình. | R11/U-H/N12/Chờ duyệt; không xóa bản ghi yêu cầu; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E5.2 | FR-M11-04.10, FR-M11-17.03, FR-M10-12.08 |
| E5.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm R11 thuộc Hòa và còn Chờ duyệt; chuyển R11→Đã rút, giữ dữ liệu yêu cầu. Trả kết quả đã rút, không thêm Hòa làm Member. | R11 Chờ duyệt→Đã rút; U-H vẫn người ngoài N12 | END:SUCCESS | FR-M11-04.10, BR-M11-36, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


<!-- sc:end SC-M11-008 -->

<a id="sc-m11-009"></a>

<!-- sc:scenario SC-M11-009 -->

### SC-M11-009

#### 1. Tên kịch bản chuẩn

Mời người khác đến nhóm bằng link chung hoặc lời mời — BF-M11-009; owner [UC-M11-009](../../us/US-M11.md#uc-m11-009); nhóm UC chính: UC-M11-032.

#### 2. Actor thực hiện

ACT-009 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có nhóm và người muốn mời; kiểm thành viên/cờ/Khóa. Chuẩn Chi Member N12 Private, mời Phúc chưa là thành viên; LINK-N12 link chung có sẵn.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-009 -->

| result | condition |
|---|---|
| SUCCESS | Người yêu cầu nhận link chung hoặc kết quả đã gửi thông báo mời có đúng link cho người đích; chưa bảo đảm người được mời tham gia. Chức năng gửi mời hoàn tất, tham gia là mục tiêu độc lập. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-009 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-009 | Chi yêu cầu mời Phúc vào N12. | N12 Private; Chi Member; người nhận=U-P; LINK-N12 | M2 | FR-M11-05.01, FR-M11-05.02 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Chi là thành viên và nhóm không Khóa, cung cấp M07 thông báo mời trong ứng dụng cho Phúc kèm LINK-N12. Trả đã gửi mời; đây là link chung không hết hạn/thu hồi/tạo lại, không tạo thực thể chấp nhận/từ chối hoặc tự thêm thành viên. Người nhận muốn tham gia thực hiện SC007 theo cổng hiện hành. | Người nhận=U-P; nhóm N12; tên/mô tả/link được preview; Phúc chưa Member; không bỏ câu hỏi/chặn/duyệt | END:SUCCESS | FR-M11-05.01, FR-M11-05.02, FR-M11-05.04, FR-M11-05.05, FR-M11-05.06, FR-M11-05.07, BR-M11-12, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-009 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Chi chọn lấy link chung thay vì mời một người cụ thể | E1.1 | FR-M11-05.01, FR-M11-05.06, FR-M11-05.04, FR-M11-05.07, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E2 | user-choice | M1 | Chi muốn thu hồi hoặc tạo lại link mời | E2.1 | FR-M11-05.07, FR-M11-05.06, BR-M11-12 |
| E3 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E3.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E4 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E4.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E5 | system | M2 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | E5.1 | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |
| E6 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Member; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M11-05.01, FR-M11-05.02, FR-M11-17.03, FR-M10-12.08, FR-M11-05.04, FR-M11-05.05, FR-M11-05.06, FR-M11-05.07, BR-M11-12, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E7 | system | M1 | ACT-001 — Guest yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M11-05.03, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E8 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M11-05.03, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E9 | system | M1 | ACT-008 — Minh MODERATOR không thành viên yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M11-05.03, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E10 | system | M1 | ACT-007 — Hòa ADMIN không thành viên yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M11-05.03, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-009 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-009 | Chi lấy link mời N12. | Chi Member; N12 Private; không chỉ định người nhận | E1.2 | FR-M11-05.01, FR-M11-05.06 |
| E1.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/không Khóa, trả chính LINK-N12 chung không hết hạn; không tạo link theo từng thành viên, không thông báo khi chỉ lấy link hoặc tạo lời mời có Chấp nhận/Từ chối. | LINK-N12 đã có→cùng LINK-N12; không thay membership/yêu cầu | END:SUCCESS | FR-M11-05.01, FR-M11-05.04, FR-M11-05.06, FR-M11-05.07, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-009 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-009 | Chi yêu cầu thu hồi/tạo lại LINK-N12. | LINK-N12 chung; không hết hạn | E2.2 | FR-M11-05.07 |
| E2.2 | SYSTEM | Hệ thống không cho thu hồi/tạo lại link chung; giữ LINK-N12 cũ, không tạo link khác. | LINK-N12 còn nguyên; không thực hiện thao tác không được hỗ trợ | END:REJECTED | FR-M11-05.06, FR-M11-05.07, BR-M11-12 |


<!-- sc:branch SC-M11-009 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-009 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-009 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối hành vi trong nhóm Bị khóa kể cả Owner/Group Mod hoặc ADMIN; quyền đọc/lưu/báo cáo/Member-Group Mod tự rời và tự kế nhiệm theo hợp đồng riêng vẫn giữ. | Nhóm Bị khóa; không thực hiện thay đổi/duyệt/nhận mở queue bị chặn | END:REJECTED | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |


**E6 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Member; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-009 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-007 | Hòa yêu cầu mời Phúc vào N12. | N12 Private; Hòa Member; người nhận=U-P; LINK-N12; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E6.2 | FR-M11-05.01, FR-M11-05.02, FR-M11-17.03, FR-M10-12.08 |
| E6.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Hòa là thành viên và nhóm không Khóa, cung cấp M07 thông báo mời trong ứng dụng cho Phúc kèm LINK-N12. Trả đã gửi mời; đây là link chung không hết hạn/thu hồi/tạo lại, không tạo thực thể chấp nhận/từ chối hoặc tự thêm thành viên. Người nhận muốn tham gia thực hiện SC007 theo cổng hiện hành. | Người nhận=U-P; nhóm N12; tên/mô tả/link được preview; Phúc chưa Member; không bỏ câu hỏi/chặn/duyệt | END:SUCCESS | FR-M11-05.01, FR-M11-05.02, FR-M11-05.04, FR-M11-05.05, FR-M11-05.06, FR-M11-05.07, BR-M11-12, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


**E7 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-009 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-001 | Guest yêu cầu: Mời người khác đến nhóm bằng link chung hoặc lời mời. | Đúng nhóm/đích của chức năng; Guest không có vai trò nhóm bắt buộc; Group=true | E7.2 | FR-M11-05.03, BR-M11-12 |
| E7.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-05.03, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E8 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-009 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-002 | Phúc người ngoài yêu cầu: Mời người khác đến nhóm bằng link chung hoặc lời mời. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E8.2 | FR-M11-05.03, BR-M11-12 |
| E8.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-05.03, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E9 — thay toàn bộ M1 đến kết thúc:** Minh MODERATOR không thành viên yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-009 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-008 | Minh MODERATOR không thành viên yêu cầu: Mời người khác đến nhóm bằng link chung hoặc lời mời. | Đúng nhóm/đích của chức năng; Minh MODERATOR không thành viên không có vai trò nhóm bắt buộc; Group=true | E9.2 | FR-M11-05.03, BR-M11-12 |
| E9.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-05.03, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E10 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN không thành viên yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-009 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-007 | Hòa ADMIN không thành viên yêu cầu: Mời người khác đến nhóm bằng link chung hoặc lời mời. | Đúng nhóm/đích của chức năng; Hòa ADMIN không thành viên không có vai trò nhóm bắt buộc; Group=true | E10.2 | FR-M11-05.03, BR-M11-12 |
| E10.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-05.03, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-009 -->

<a id="sc-m11-010"></a>

<!-- sc:scenario SC-M11-010 -->

### SC-M11-010

#### 1. Tên kịch bản chuẩn

Xét một yêu cầu tham gia nhóm — BF-M11-010; owner [UC-M11-010](../../us/US-M11.md#uc-m11-010); nhóm UC chính: UC-M11-032.

#### 2. Actor thực hiện

ACT-010 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có N12 Private/câu hỏi, R11 Chờ duyệt của Phúc trả lời 11; quyền Owner/Group Mod và trạng thái kiểm khi xem và quyết định.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-010 -->

| result | condition |
|---|---|
| SUCCESS | Quyết định hợp lệ được lưu và trả: Chấp nhận thêm Member/mốc/thông báo; Từ chối chuyển Đã từ chối, không thêm Member/không báo người gửi, cho gửi yêu cầu mới ngay. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-010 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-010 | Bình mở danh sách yêu cầu tham gia N12. | Bình Group Mod; N12 Private; R11 U-P Chờ duyệt | M2 | FR-M11-06.01 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod của đúng nhóm, không Khóa; trả các yêu cầu đang Chờ duyệt kèm câu trả lời. | R11 Phúc; câu trả lời=11; Chờ duyệt; không yêu cầu lý do bắt buộc khi từ chối | M3 | FR-M11-06.01, FR-M11-06.05, BR-M11-08, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| M3 | ACT-010 | Bình chọn Chấp nhận R11. | R11; U-P; lựa chọn=Chấp nhận; thời điểm T | M4 | FR-M11-06.02 |
| M4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Group Mod và R11 còn Chờ duyệt; R11→Đã chấp nhận, Phúc→Member với thời điểm tham gia=T; thông báo trong ứng dụng cho Phúc qua M07. Trả kết quả chấp nhận. | R11 Đã chấp nhận; U-P Member N12, joinAt=T; recipient=U-P | END:SUCCESS | FR-M11-06.02, FR-M11-06.04, FR-M11-06.06, BR-M11-07, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-010 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M3 | Bình chọn Từ chối R11 đang Chờ duyệt | E1.1 | FR-M11-06.03, FR-M11-06.06, FR-M11-06.09, FR-M11-04.04, BR-M11-09, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E2 | system | M4 | R11 đã được xử lý/rút trước lúc nhận quyết định | E2.1 | FR-M11-06.06 |
| E3 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E3.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E4 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E4.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E5 | system | M2 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | E5.1 | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |
| E6 | system | M4 | Nhóm chuyển Bị khóa hoặc cờ Group Tắt với người không ADMIN sau lượt đọc nhưng trước lúc lưu | E6.1 | FR-M11-16.07, FR-M11-17.01, FR-M11-17.08, BR-M11-28, BR-M11-29 |
| E7 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M11-06.01, FR-M11-17.03, FR-M10-12.08, FR-M11-06.05, BR-M11-08, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-06.02, FR-M11-06.04, FR-M11-06.06, BR-M11-07, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |
| E8 | system | M1 | ACT-009 — Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M11-06.05, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E9 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M11-06.05, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E10 | system | M1 | ACT-008 — Minh MODERATOR không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M11-06.05, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E11 | system | M1 | ACT-007 — Hòa ADMIN không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E11.1 | FR-M11-06.05, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E12 | system | M1 | ACT-011 — An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E12.1 | FR-M11-06.01, FR-M11-06.05, BR-M11-08, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-06.02, FR-M11-06.04, FR-M11-06.06, BR-M11-07, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |


<!-- sc:branch SC-M11-010 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-010 | Bình chọn Từ chối R11. | R11/U-P/Chờ duyệt; không lý do bắt buộc | E1.2 | FR-M11-06.03 |
| E1.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Group Mod/không Khóa và R11 còn Chờ duyệt, R11→Đã từ chối; không thêm Member hoặc thông báo từ chối. Trả quyết định, người gửi được gửi yêu cầu mới ngay không giới hạn lần/cooldown. | R11 Đã từ chối; U-P vẫn người ngoài; không thông báo | END:SUCCESS | FR-M11-06.03, FR-M11-06.06, FR-M11-06.09, FR-M11-04.04, BR-M11-09, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-010 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống kiểm R11 không còn Chờ duyệt, từ chối chấp nhận hoặc từ chối lần nữa; giữ trạng thái hiện tại. | R11 Đã rút/Đã chấp nhận/Đã từ chối; không quyết định mới | END:REJECTED | FR-M11-06.06 |


<!-- sc:branch SC-M11-010 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-010 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-010 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối hành vi trong nhóm Bị khóa kể cả Owner/Group Mod hoặc ADMIN; quyền đọc/lưu/báo cáo/Member-Group Mod tự rời và tự kế nhiệm theo hợp đồng riêng vẫn giữ. | Nhóm Bị khóa; không thực hiện thay đổi/duyệt/nhận mở queue bị chặn | END:REJECTED | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |


<!-- sc:branch SC-M11-010 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống kiểm lại điều kiện hiện tại; nếu cờ Tắt từ chối đúng thông báo “Hệ thống đang bận, vui lòng thử lại sau”, nếu Khóa từ chối hành vi đã bị chặn. Không dùng lần đọc trước để hoàn tất thay đổi. | Không có thay đổi được yêu cầu của lần lưu này; trạng thái hiện tại giữ | END:REJECTED | FR-M11-16.07, FR-M11-17.01, FR-M11-17.08, BR-M11-28, BR-M11-29 |


**E7 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-010 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-007 | Hòa mở danh sách yêu cầu tham gia N12. | Hòa Group Mod; N12 Private; R11 U-P Chờ duyệt; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E7.2 | FR-M11-06.01, FR-M11-17.03, FR-M10-12.08 |
| E7.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod của đúng nhóm, không Khóa; trả các yêu cầu đang Chờ duyệt kèm câu trả lời. | R11 Phúc; câu trả lời=11; Chờ duyệt; không yêu cầu lý do bắt buộc khi từ chối | E7.3 | FR-M11-06.01, FR-M11-06.05, BR-M11-08, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |
| E7.3 | ACT-007 | Hòa chọn Chấp nhận R11. | R11; U-P; lựa chọn=Chấp nhận; thời điểm T | E7.4 | FR-M11-06.02, FR-M11-17.03, FR-M10-12.08 |
| E7.4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Group Mod và R11 còn Chờ duyệt; R11→Đã chấp nhận, Phúc→Member với thời điểm tham gia=T; thông báo trong ứng dụng cho Phúc qua M07. Trả kết quả chấp nhận. | R11 Đã chấp nhận; U-P Member N12, joinAt=T; recipient=U-P | END:SUCCESS | FR-M11-06.02, FR-M11-06.04, FR-M11-06.06, BR-M11-07, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


**E8 — thay toàn bộ M1 đến kết thúc:** Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-010 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-009 | Chi Member yêu cầu: Xét một yêu cầu tham gia nhóm. | Đúng nhóm/đích của chức năng; Chi Member không có vai trò nhóm bắt buộc; Group=true | E8.2 | FR-M11-06.05, BR-M11-06 |
| E8.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-06.05, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E9 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-010 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-002 | Phúc người ngoài yêu cầu: Xét một yêu cầu tham gia nhóm. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E9.2 | FR-M11-06.05, BR-M11-06 |
| E9.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-06.05, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E10 — thay toàn bộ M1 đến kết thúc:** Minh MODERATOR không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-010 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-008 | Minh MODERATOR không Group Mod yêu cầu: Xét một yêu cầu tham gia nhóm. | Đúng nhóm/đích của chức năng; Minh MODERATOR không Group Mod không có vai trò nhóm bắt buộc; Group=true | E10.2 | FR-M11-06.05, BR-M11-06 |
| E10.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-06.05, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E11 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-010 E11 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E11.1 | ACT-007 | Hòa ADMIN không Group Mod yêu cầu: Xét một yêu cầu tham gia nhóm. | Đúng nhóm/đích của chức năng; Hòa ADMIN không Group Mod không có vai trò nhóm bắt buộc; Group=true | E11.2 | FR-M11-06.05, BR-M11-06 |
| E11.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-06.05, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E12 — thay toàn bộ M1 đến kết thúc:** An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-010 E12 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E12.1 | ACT-011 | An mở danh sách yêu cầu tham gia N12. | An Owner; N12 Private; R11 U-P Chờ duyệt; An Owner; nếu có holder của bài đang xét thì holder=An, tác giả vẫn Chi | E12.2 | FR-M11-06.01 |
| E12.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner của đúng nhóm, không Khóa; trả các yêu cầu đang Chờ duyệt kèm câu trả lời. | R11 Phúc; câu trả lời=11; Chờ duyệt; không yêu cầu lý do bắt buộc khi từ chối | E12.3 | FR-M11-06.01, FR-M11-06.05, BR-M11-08, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E12.3 | ACT-011 | An chọn Chấp nhận R11. | R11; U-P; lựa chọn=Chấp nhận; thời điểm T | E12.4 | FR-M11-06.02 |
| E12.4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Group Mod và R11 còn Chờ duyệt; R11→Đã chấp nhận, Phúc→Member với thời điểm tham gia=T; thông báo trong ứng dụng cho Phúc qua M07. Trả kết quả chấp nhận. | R11 Đã chấp nhận; U-P Member N12, joinAt=T; recipient=U-P | END:SUCCESS | FR-M11-06.02, FR-M11-06.04, FR-M11-06.06, BR-M11-07, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-010 -->

<a id="sc-m11-011"></a>

<!-- sc:scenario SC-M11-011 -->

### SC-M11-011

#### 1. Tên kịch bản chuẩn

Chặn một người gửi yêu cầu tham gia nhóm — BF-M11-011; owner [UC-M11-011](../../us/US-M11.md#uc-m11-011); nhóm UC chính: UC-M11-032.

#### 2. Actor thực hiện

ACT-010 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có N12 và Phúc người gửi R11 Chờ duyệt; đây là chặn tham gia riêng nhóm, không kick/ban hệ thống. Kiểm quyền và Khóa/cờ trong luồng.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-011 -->

| result | condition |
|---|---|
| SUCCESS | Người gửi có trong danh sách chặn của đúng nhóm, mọi yêu cầu Chờ duyệt hiện có bị từ chối; không thành ban hệ thống/thành viên, actor nhận kết quả. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-011 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-010 | Bình chọn chặn Phúc gửi yêu cầu tới N12. | Bình Group Mod N12; U-P; R11 Chờ duyệt | M2 | FR-M11-07.01 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod đúng nhóm, không Khóa; ghi U-P vào danh sách chặn N12, R11 Chờ duyệt→Đã từ chối. Không gửi thông báo từ chối yêu cầu. Chặn mọi cách gia nhập N12: vào ngay/gửi yêu cầu/lời mời; nhóm khác không bị tác động, không cooldown. Trả kết quả đã chặn. | N12.blocked có U-P; R11 Đã từ chối; Phúc không Member | END:SUCCESS | FR-M11-07.01, FR-M11-07.03, FR-M11-04.06, FR-M11-06.09, BR-M11-06, BR-M11-10, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-011 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Phúc là người gửi cũ, hiện không có yêu cầu Chờ duyệt | E1.1 | FR-M11-07.01, FR-M11-07.03, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E2 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E2.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E3 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E3.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E4 | system | M2 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | E4.1 | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |
| E5 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M11-07.01, FR-M11-17.03, FR-M10-12.08, FR-M11-07.03, FR-M11-04.06, FR-M11-06.09, BR-M11-06, BR-M11-10, BR-M11-37, FR-M11-17.01, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E6 | system | M1 | ACT-009 — Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E7 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E8 | system | M1 | ACT-007 — Hòa ADMIN không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E9 | system | M1 | ACT-011 — An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M11-07.01, FR-M11-07.03, FR-M11-04.06, FR-M11-06.09, BR-M11-06, BR-M11-10, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-011 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod đúng nhóm/không Khóa, ghi Phúc vào blocked N12, giữ yêu cầu cũ Đã từ chối/Đã rút; chặn mọi lối gia nhập, trả đã chặn. | blocked N12 thêmU-P; không có yêu cầu Chờ duyệt để chuyển; không kick/ban hệ thống | END:SUCCESS | FR-M11-07.01, FR-M11-07.03, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-011 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-011 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-011 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối hành vi trong nhóm Bị khóa kể cả Owner/Group Mod hoặc ADMIN; quyền đọc/lưu/báo cáo/Member-Group Mod tự rời và tự kế nhiệm theo hợp đồng riêng vẫn giữ. | Nhóm Bị khóa; không thực hiện thay đổi/duyệt/nhận mở queue bị chặn | END:REJECTED | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |


**E5 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-011 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-007 | Hòa chọn chặn Phúc gửi yêu cầu tới N12. | Hòa Group Mod N12; U-P; R11 Chờ duyệt; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E5.2 | FR-M11-07.01, FR-M11-17.03, FR-M10-12.08 |
| E5.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod đúng nhóm, không Khóa; ghi U-P vào danh sách chặn N12, R11 Chờ duyệt→Đã từ chối. Không gửi thông báo từ chối yêu cầu. Chặn mọi cách gia nhập N12: vào ngay/gửi yêu cầu/lời mời; nhóm khác không bị tác động, không cooldown. Trả kết quả đã chặn. | N12.blocked có U-P; R11 Đã từ chối; Phúc không Member | END:SUCCESS | FR-M11-07.01, FR-M11-07.03, FR-M11-04.06, FR-M11-06.09, BR-M11-06, BR-M11-10, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


**E6 — thay toàn bộ M1 đến kết thúc:** Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-011 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-009 | Chi Member yêu cầu: Chặn một người gửi yêu cầu tham gia nhóm. | Đúng nhóm/đích của chức năng; Chi Member không có vai trò nhóm bắt buộc; Group=true | E6.2 | FR-M11-07.02, BR-M11-06 |
| E6.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E7 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-011 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-002 | Phúc người ngoài yêu cầu: Chặn một người gửi yêu cầu tham gia nhóm. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E7.2 | FR-M11-07.02, BR-M11-06 |
| E7.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E8 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-011 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-007 | Hòa ADMIN không Group Mod yêu cầu: Chặn một người gửi yêu cầu tham gia nhóm. | Đúng nhóm/đích của chức năng; Hòa ADMIN không Group Mod không có vai trò nhóm bắt buộc; Group=true | E8.2 | FR-M11-07.02, BR-M11-06 |
| E8.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E9 — thay toàn bộ M1 đến kết thúc:** An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-011 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-011 | An chọn chặn Phúc gửi yêu cầu tới N12. | An Owner N12; U-P; R11 Chờ duyệt; An Owner; nếu có holder của bài đang xét thì holder=An, tác giả vẫn Chi | E9.2 | FR-M11-07.01 |
| E9.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner đúng nhóm, không Khóa; ghi U-P vào danh sách chặn N12, R11 Chờ duyệt→Đã từ chối. Không gửi thông báo từ chối yêu cầu. Chặn mọi cách gia nhập N12: vào ngay/gửi yêu cầu/lời mời; nhóm khác không bị tác động, không cooldown. Trả kết quả đã chặn. | N12.blocked có U-P; R11 Đã từ chối; Phúc không Member | END:SUCCESS | FR-M11-07.01, FR-M11-07.03, FR-M11-04.06, FR-M11-06.09, BR-M11-06, BR-M11-10, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-011 -->

<a id="sc-m11-012"></a>

<!-- sc:scenario SC-M11-012 -->

### SC-M11-012

#### 1. Tên kịch bản chuẩn

Xem danh sách người bị chặn tham gia nhóm — BF-M11-012; owner [UC-M11-011](../../us/US-M11.md#uc-m11-011); nhóm UC chính: UC-M11-032.

#### 2. Actor thực hiện

ACT-010 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có N12 Bình thường và yêu cầu xem; quyền/cờ kiểm. Snapshot danh sách chặn U-P, U-X; nhóm Bị khóa tình huống này chưa chốt GAP004.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-012 -->

| result | condition |
|---|---|
| SUCCESS | Danh sách chặn hiện tại đúng nhóm được trả chỉ đọc, không thay quyền tham gia/yêu cầu/thành viên. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-012 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-010 | Bình mở danh sách chặn N12. | Bình Group Mod; N12.blocked={U-P,U-X} | M2 | FR-M11-07.04 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod đúng nhóm, trả những người đang bị nhóm chặn. Chỉ xem không bỏ chặn hoặc đổi yêu cầu/thành viên. | U-P/Phúc và U-X/Xuân đang bị chặn N12; dữ liệu trước=sau | END:SUCCESS | FR-M11-07.02, FR-M11-07.04, BR-M11-06, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-012 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Danh sách chặn N12 hiện rỗng | E1.1 | FR-M11-07.02, FR-M11-07.04, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E2 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E2.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E3 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E3.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E4 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M11-07.04, FR-M11-17.03, FR-M10-12.08, FR-M11-07.02, BR-M11-06, BR-M11-10, FR-M11-17.01, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E5 | system | M1 | ACT-009 — Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E6 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E7 | system | M1 | ACT-011 — An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M11-07.04, FR-M11-07.02, BR-M11-06, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-012 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod, trả danh sách chặn rỗng đúng N12, không tự tạo người bị chặn. | blocked N12=[]; chỉ đọc | END:SUCCESS | FR-M11-07.02, FR-M11-07.04, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-012 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-012 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


**E4 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-012 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-007 | Hòa mở danh sách chặn N12. | Hòa Group Mod; N12.blocked={U-P,U-X}; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E4.2 | FR-M11-07.04, FR-M11-17.03, FR-M10-12.08 |
| E4.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod đúng nhóm, trả những người đang bị nhóm chặn. Chỉ xem không bỏ chặn hoặc đổi yêu cầu/thành viên. | U-P/Phúc và U-X/Xuân đang bị chặn N12; dữ liệu trước=sau | END:SUCCESS | FR-M11-07.02, FR-M11-07.04, BR-M11-06, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


**E5 — thay toàn bộ M1 đến kết thúc:** Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-012 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-009 | Chi Member yêu cầu: Xem danh sách người bị chặn tham gia nhóm. | Đúng nhóm/đích của chức năng; Chi Member không có vai trò nhóm bắt buộc; Group=true | E5.2 | FR-M11-07.02, BR-M11-06 |
| E5.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E6 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-012 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-002 | Phúc người ngoài yêu cầu: Xem danh sách người bị chặn tham gia nhóm. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E6.2 | FR-M11-07.02, BR-M11-06 |
| E6.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E7 — thay toàn bộ M1 đến kết thúc:** An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-012 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-011 | An mở danh sách chặn N12. | An Owner; N12.blocked={U-P,U-X}; An Owner; nếu có holder của bài đang xét thì holder=An, tác giả vẫn Chi | E7.2 | FR-M11-07.04 |
| E7.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner đúng nhóm, trả những người đang bị nhóm chặn. Chỉ xem không bỏ chặn hoặc đổi yêu cầu/thành viên. | U-P/Phúc và U-X/Xuân đang bị chặn N12; dữ liệu trước=sau | END:SUCCESS | FR-M11-07.02, FR-M11-07.04, BR-M11-06, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-012 -->

<a id="sc-m11-013"></a>

<!-- sc:scenario SC-M11-013 -->

### SC-M11-013

#### 1. Tên kịch bản chuẩn

Bỏ chặn một người khỏi danh sách chặn tham gia — BF-M11-013; owner [UC-M11-011](../../us/US-M11.md#uc-m11-011); nhóm UC chính: UC-M11-032.

#### 2. Actor thực hiện

ACT-010 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có N12, U-P đang bị chặn, R11 Đã từ chối do chặn; kiểm quyền/trạng thái. Bỏ chặn không tự cho vào nhóm hay mở lại R11.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-013 -->

| result | condition |
|---|---|
| SUCCESS | U-P không còn trong danh sách chặn đúng nhóm, được dùng luồng gia nhập theo điều kiện hiện hành; chưa là Member/yêu cầu cũ không tự được chấp nhận. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-013 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-010 | Bình mở danh sách chặn N12 để chọn người bỏ chặn. | Group Mod Bình; N12 Bình thường; blocked U-P | M2 | FR-M11-07.04, FR-M11-07.05 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod; trả danh sách chặn hiện tại đúng N12 để chọn. | U-P Phúc, U-X Xuân; R11 vẫn Đã từ chối | M3 | FR-M11-07.02, FR-M11-07.04, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| M3 | ACT-010 | Bình chọn bỏ chặn Phúc. | N12/U-P; thao tác=Bỏ chặn | M4 | FR-M11-07.05 |
| M4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại vai trò và nhóm không Khóa; bỏ chặn U-P, cho Phúc gia nhập lại theo cổng hiện hành SC007 ngay. Không khôi phục yêu cầu Đã từ chối hoặc tự thành Member; trả đã bỏ chặn. | blocked N12 không còn U-P; R11 vẫn Đã từ chối; Phúc vẫn người ngoài, có thể gửi R12 mới | END:SUCCESS | FR-M11-07.05, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-013 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E1.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E2 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E2.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E3 | system | M4 | Nhóm chuyển Bị khóa hoặc cờ Group Tắt với người không ADMIN sau lượt đọc nhưng trước lúc lưu | E3.1 | FR-M11-16.07, FR-M11-17.01, FR-M11-17.08, BR-M11-28, BR-M11-29 |
| E4 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M11-07.04, FR-M11-07.05, FR-M11-17.03, FR-M10-12.08, FR-M11-07.02, BR-M11-10, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E5 | system | M1 | ACT-009 — Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E6 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E7 | system | M1 | ACT-011 — An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M11-07.04, FR-M11-07.05, FR-M11-07.02, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-013 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-013 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-013 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống kiểm lại điều kiện hiện tại; nếu cờ Tắt từ chối đúng thông báo “Hệ thống đang bận, vui lòng thử lại sau”, nếu Khóa từ chối hành vi đã bị chặn. Không dùng lần đọc trước để hoàn tất thay đổi. | Không có thay đổi được yêu cầu của lần lưu này; trạng thái hiện tại giữ | END:REJECTED | FR-M11-16.07, FR-M11-17.01, FR-M11-17.08, BR-M11-28, BR-M11-29 |


**E4 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-013 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-007 | Hòa mở danh sách chặn N12 để chọn người bỏ chặn. | Group Mod Hòa; N12 Hòa thường; blocked U-P; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E4.2 | FR-M11-07.04, FR-M11-07.05, FR-M11-17.03, FR-M10-12.08 |
| E4.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod; trả danh sách chặn hiện tại đúng N12 để chọn. | U-P Phúc, U-X Xuân; R11 vẫn Đã từ chối | E4.3 | FR-M11-07.02, FR-M11-07.04, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |
| E4.3 | ACT-007 | Hòa chọn bỏ chặn Phúc. | N12/U-P; thao tác=Bỏ chặn | E4.4 | FR-M11-07.05, FR-M11-17.03, FR-M10-12.08 |
| E4.4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại vai trò và nhóm không Khóa; bỏ chặn U-P, cho Phúc gia nhập lại theo cổng hiện hành SC007 ngay. Không khôi phục yêu cầu Đã từ chối hoặc tự thành Member; trả đã bỏ chặn. | blocked N12 không còn U-P; R11 vẫn Đã từ chối; Phúc vẫn người ngoài, có thể gửi R12 mới | END:SUCCESS | FR-M11-07.05, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


**E5 — thay toàn bộ M1 đến kết thúc:** Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-013 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-009 | Chi Member yêu cầu: Bỏ chặn một người khỏi danh sách chặn tham gia. | Đúng nhóm/đích của chức năng; Chi Member không có vai trò nhóm bắt buộc; Group=true | E5.2 | FR-M11-07.02, BR-M11-06 |
| E5.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E6 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-013 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-002 | Phúc người ngoài yêu cầu: Bỏ chặn một người khỏi danh sách chặn tham gia. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E6.2 | FR-M11-07.02, BR-M11-06 |
| E6.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E7 — thay toàn bộ M1 đến kết thúc:** An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-013 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-011 | An mở danh sách chặn N12 để chọn người bỏ chặn. | Group Mod An; N12 An thường; blocked U-P; An Owner; nếu có holder của bài đang xét thì holder=An, tác giả vẫn Chi | E7.2 | FR-M11-07.04, FR-M11-07.05 |
| E7.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner; trả danh sách chặn hiện tại đúng N12 để chọn. | U-P Phúc, U-X Xuân; R11 vẫn Đã từ chối | E7.3 | FR-M11-07.02, FR-M11-07.04, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E7.3 | ACT-011 | An chọn bỏ chặn Phúc. | N12/U-P; thao tác=Bỏ chặn | E7.4 | FR-M11-07.05 |
| E7.4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại vai trò và nhóm không Khóa; bỏ chặn U-P, cho Phúc gia nhập lại theo cổng hiện hành SC007 ngay. Không khôi phục yêu cầu Đã từ chối hoặc tự thành Member; trả đã bỏ chặn. | blocked N12 không còn U-P; R11 vẫn Đã từ chối; Phúc vẫn người ngoài, có thể gửi R12 mới | END:SUCCESS | FR-M11-07.05, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-013 -->

<a id="sc-m11-014"></a>

<!-- sc:scenario SC-M11-014 -->

### SC-M11-014

#### 1. Tên kịch bản chuẩn

Bổ nhiệm một thành viên làm Group Mod — BF-M11-014; owner [UC-M11-012](../../us/US-M11.md#uc-m11-012); nhóm UC chính: UC-M11-032.

#### 2. Actor thực hiện

ACT-011 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có N11 và ý định bổ nhiệm; quyền Owner, đích và trạng thái kiểm khi mở/lưu. Chuẩn Chi đang Member.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-014 -->

| result | condition |
|---|---|
| SUCCESS | Chi chuyển Member→Group Mod trong đúng nhóm, kết quả trả Owner; mốc bổ nhiệm mới và thông báo người được bổ nhiệm. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-014 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-011 | An mở chức năng bổ nhiệm Group Mod trong N11. | An Owner N11; hành vi=Bổ nhiệm | M2 | FR-M11-08.01 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner, không Khóa; mở UC006/023 trả thành viên kèm vai trò để Owner chọn. | An Owner, Bình Group Mod bổ nhiệm 01/09/2026 09:00+07, Dũng Group Mod bổ nhiệm lại 20/10/2026 09:00+07 (lần trước không tính), Chi Member vào 01/08/2026, Lan Member vào 01/07/2026. Đây là snapshot chuẩn, từng chức năng có thể thay dữ liệu đích ghi ngay tại bước. | M3 | FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| M3 | ACT-011 | An chọn Chi và yêu cầu bổ nhiệm. | Chi Member; N11; T | M4 | FR-M11-08.01 |
| M4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Owner/đích đúng Member thuộc nhóm, không Khóa. Chuyển Chi→Group Mod. Ghi thời điểm bổ nhiệm lần này=T để tính thâm niên, kể cả từng bị giáng; gửi thông báo trong ứng dụng cho Chi. Trả kết quả bổ nhiệm. | Chi Member→Group Mod; appointedAt=T; recipient=Chi | END:SUCCESS | FR-M11-08.01, FR-M11-08.03, FR-M11-11.06, BR-M11-05, BR-M11-06, BR-M11-26, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-014 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M4 | Đích đã không còn thuộc vai trò nguồn Member tại lúc xử lý | E1.1 | FR-M11-08.01, FR-M11-08.02, BR-M11-05, BR-M11-06 |
| E2 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E2.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E3 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E3.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E4 | system | M2 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | E4.1 | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |
| E5 | system | M4 | Nhóm chuyển Bị khóa hoặc cờ Group Tắt với người không ADMIN sau lượt đọc nhưng trước lúc lưu | E5.1 | FR-M11-16.07, FR-M11-17.01, FR-M11-17.08, BR-M11-28, BR-M11-29 |
| E6 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Owner; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M11-08.01, FR-M11-17.03, FR-M10-12.08, FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-08.03, FR-M11-11.06, BR-M11-05, BR-M11-26, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |
| E7 | system | M1 | ACT-010 — Bình Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-010; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E8 | system | M1 | ACT-009 — Lan Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E9 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E10 | system | M1 | ACT-007 — Hòa ADMIN không Owner yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-014 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm lại loại đích và không áp chuyển role ngoài điều kiện; không thay vai trò Owner/người ngoài hoặc người đã đổi role. | Đích không còn Member; không đổi vai trò theo lệnh này | END:REJECTED | FR-M11-08.01, FR-M11-08.02, BR-M11-05, BR-M11-06 |


<!-- sc:branch SC-M11-014 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-014 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-014 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối hành vi trong nhóm Bị khóa kể cả Owner/Group Mod hoặc ADMIN; quyền đọc/lưu/báo cáo/Member-Group Mod tự rời và tự kế nhiệm theo hợp đồng riêng vẫn giữ. | Nhóm Bị khóa; không thực hiện thay đổi/duyệt/nhận mở queue bị chặn | END:REJECTED | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |


<!-- sc:branch SC-M11-014 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống kiểm lại điều kiện hiện tại; nếu cờ Tắt từ chối đúng thông báo “Hệ thống đang bận, vui lòng thử lại sau”, nếu Khóa từ chối hành vi đã bị chặn. Không dùng lần đọc trước để hoàn tất thay đổi. | Không có thay đổi được yêu cầu của lần lưu này; trạng thái hiện tại giữ | END:REJECTED | FR-M11-16.07, FR-M11-17.01, FR-M11-17.08, BR-M11-28, BR-M11-29 |


**E6 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Owner; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-014 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-007 | Hòa mở chức năng bổ nhiệm Group Mod trong N11. | Hòa Owner N11; hành vi=Bổ nhiệm; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E6.2 | FR-M11-08.01, FR-M11-17.03, FR-M10-12.08 |
| E6.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner, không Khóa; mở UC006/023 trả thành viên kèm vai trò để Owner chọn. | Hòa Owner, Bình Group Mod bổ nhiệm 01/09/2026 09:00+07, Dũng Group Mod bổ nhiệm lại 20/10/2026 09:00+07 (lần trước không tính), Chi Member vào 01/08/2026, Lan Member vào 01/07/2026. Đây là snapshot chuẩn, từng chức năng có thể thay dữ liệu đích ghi ngay tại bước. | E6.3 | FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |
| E6.3 | ACT-007 | Hòa chọn Chi và yêu cầu bổ nhiệm. | Chi Member; N11; T | E6.4 | FR-M11-08.01, FR-M11-17.03, FR-M10-12.08 |
| E6.4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Owner/đích đúng Member thuộc nhóm, không Khóa. Chuyển Chi→Group Mod. Ghi thời điểm bổ nhiệm lần này=T để tính thâm niên, kể cả từng bị giáng; gửi thông báo trong ứng dụng cho Chi. Trả kết quả bổ nhiệm. | Chi Member→Group Mod; appointedAt=T; recipient=Chi | END:SUCCESS | FR-M11-08.01, FR-M11-08.03, FR-M11-11.06, BR-M11-05, BR-M11-06, BR-M11-26, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


**E7 — thay toàn bộ M1 đến kết thúc:** Bình Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-010; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-014 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-010 | Bình Group Mod yêu cầu: Bổ nhiệm một thành viên làm Group Mod. | Đúng nhóm/đích của chức năng; Bình Group Mod không có vai trò nhóm bắt buộc; Group=true | E7.2 | FR-M11-08.04, BR-M11-06 |
| E7.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E8 — thay toàn bộ M1 đến kết thúc:** Lan Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-014 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-009 | Lan Member yêu cầu: Bổ nhiệm một thành viên làm Group Mod. | Đúng nhóm/đích của chức năng; Lan Member không có vai trò nhóm bắt buộc; Group=true | E8.2 | FR-M11-08.04, BR-M11-06 |
| E8.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E9 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-014 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-002 | Phúc người ngoài yêu cầu: Bổ nhiệm một thành viên làm Group Mod. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E9.2 | FR-M11-08.04, BR-M11-06 |
| E9.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E10 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN không Owner yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-014 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-007 | Hòa ADMIN không Owner yêu cầu: Bổ nhiệm một thành viên làm Group Mod. | Đúng nhóm/đích của chức năng; Hòa ADMIN không Owner không có vai trò nhóm bắt buộc; Group=true | E10.2 | FR-M11-08.04, BR-M11-06 |
| E10.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-014 -->

<a id="sc-m11-015"></a>

<!-- sc:scenario SC-M11-015 -->

### SC-M11-015

#### 1. Tên kịch bản chuẩn

Giáng một thành viên từ Group Mod về Member — BF-M11-015; owner [UC-M11-012](../../us/US-M11.md#uc-m11-012); nhóm UC chính: UC-M11-032.

#### 2. Actor thực hiện

ACT-011 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có N11 và ý định giáng; quyền Owner, đích và trạng thái kiểm khi mở/lưu. Chuẩn Bình đang Group Mod.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-015 -->

| result | condition |
|---|---|
| SUCCESS | Bình chuyển Group Mod→Member trong đúng nhóm, kết quả trả Owner; không thông báo giáng, không đổi vai trò hệ thống. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-015 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-011 | An mở chức năng giáng Group Mod trong N11. | An Owner N11; hành vi=Giáng | M2 | FR-M11-08.02 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner, không Khóa; mở UC006/023 trả thành viên kèm vai trò để Owner chọn. | An Owner, Bình Group Mod bổ nhiệm 01/09/2026 09:00+07, Dũng Group Mod bổ nhiệm lại 20/10/2026 09:00+07 (lần trước không tính), Chi Member vào 01/08/2026, Lan Member vào 01/07/2026. Đây là snapshot chuẩn, từng chức năng có thể thay dữ liệu đích ghi ngay tại bước. | M3 | FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| M3 | ACT-011 | An chọn Bình và yêu cầu giáng. | Bình Group Mod; N11; T | M4 | FR-M11-08.02 |
| M4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Owner/đích đúng Group Mod thuộc nhóm, không Khóa. Chuyển Bình→Member. Không gửi thông báo cho người bị giáng; nếu bổ nhiệm lại thì thâm niên tính từ lần mới, không cộng lần cũ. Trả kết quả giáng. | Bình Group Mod→Member; không thông báo giáng | END:SUCCESS | FR-M11-08.02, FR-M11-08.06, FR-M11-11.06, BR-M11-05, BR-M11-06, BR-M11-26, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-015 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M4 | Đích đã không còn thuộc vai trò nguồn Group Mod tại lúc xử lý | E1.1 | FR-M11-08.01, FR-M11-08.02, BR-M11-05, BR-M11-06 |
| E2 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E2.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E3 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E3.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E4 | system | M2 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | E4.1 | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |
| E5 | system | M4 | Nhóm chuyển Bị khóa hoặc cờ Group Tắt với người không ADMIN sau lượt đọc nhưng trước lúc lưu | E5.1 | FR-M11-16.07, FR-M11-17.01, FR-M11-17.08, BR-M11-28, BR-M11-29 |
| E6 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Owner; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M11-08.02, FR-M11-17.03, FR-M10-12.08, FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-08.06, FR-M11-11.06, BR-M11-05, BR-M11-26, BR-M11-37 |
| E7 | system | M1 | ACT-010 — Dũng Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-010; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E8 | system | M1 | ACT-009 — Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E9 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-015 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm lại loại đích và không áp chuyển role ngoài điều kiện; không thay vai trò Owner/người ngoài hoặc người đã đổi role. | Đích không còn Group Mod; không đổi vai trò theo lệnh này | END:REJECTED | FR-M11-08.01, FR-M11-08.02, BR-M11-05, BR-M11-06 |


<!-- sc:branch SC-M11-015 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-015 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-015 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối hành vi trong nhóm Bị khóa kể cả Owner/Group Mod hoặc ADMIN; quyền đọc/lưu/báo cáo/Member-Group Mod tự rời và tự kế nhiệm theo hợp đồng riêng vẫn giữ. | Nhóm Bị khóa; không thực hiện thay đổi/duyệt/nhận mở queue bị chặn | END:REJECTED | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |


<!-- sc:branch SC-M11-015 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống kiểm lại điều kiện hiện tại; nếu cờ Tắt từ chối đúng thông báo “Hệ thống đang bận, vui lòng thử lại sau”, nếu Khóa từ chối hành vi đã bị chặn. Không dùng lần đọc trước để hoàn tất thay đổi. | Không có thay đổi được yêu cầu của lần lưu này; trạng thái hiện tại giữ | END:REJECTED | FR-M11-16.07, FR-M11-17.01, FR-M11-17.08, BR-M11-28, BR-M11-29 |


**E6 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Owner; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-015 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-007 | Hòa mở chức năng giáng Group Mod trong N11. | Hòa Owner N11; hành vi=Giáng; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E6.2 | FR-M11-08.02, FR-M11-17.03, FR-M10-12.08 |
| E6.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner, không Khóa; mở UC006/023 trả thành viên kèm vai trò để Owner chọn. | Hòa Owner, Bình Group Mod bổ nhiệm 01/09/2026 09:00+07, Dũng Group Mod bổ nhiệm lại 20/10/2026 09:00+07 (lần trước không tính), Chi Member vào 01/08/2026, Lan Member vào 01/07/2026. Đây là snapshot chuẩn, từng chức năng có thể thay dữ liệu đích ghi ngay tại bước. | E6.3 | FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |
| E6.3 | ACT-007 | Hòa chọn Bình và yêu cầu giáng. | Bình Group Mod; N11; T | E6.4 | FR-M11-08.02, FR-M11-17.03, FR-M10-12.08 |
| E6.4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Owner/đích đúng Group Mod thuộc nhóm, không Khóa. Chuyển Bình→Member. Không gửi thông báo cho người bị giáng; nếu bổ nhiệm lại thì thâm niên tính từ lần mới, không cộng lần cũ. Trả kết quả giáng. | Bình Group Mod→Member; không thông báo giáng | END:SUCCESS | FR-M11-08.02, FR-M11-08.06, FR-M11-11.06, BR-M11-05, BR-M11-06, BR-M11-26, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


**E7 — thay toàn bộ M1 đến kết thúc:** Dũng Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-010; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-015 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-010 | Dũng Group Mod yêu cầu: Giáng một thành viên từ Group Mod về Member. | Đúng nhóm/đích của chức năng; Dũng Group Mod không có vai trò nhóm bắt buộc; Group=true | E7.2 | FR-M11-08.04, BR-M11-06 |
| E7.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E8 — thay toàn bộ M1 đến kết thúc:** Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-015 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-009 | Chi Member yêu cầu: Giáng một thành viên từ Group Mod về Member. | Đúng nhóm/đích của chức năng; Chi Member không có vai trò nhóm bắt buộc; Group=true | E8.2 | FR-M11-08.04, BR-M11-06 |
| E8.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E9 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-015 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-002 | Phúc người ngoài yêu cầu: Giáng một thành viên từ Group Mod về Member. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E9.2 | FR-M11-08.04, BR-M11-06 |
| E9.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-015 -->

<a id="sc-m11-016"></a>

<!-- sc:scenario SC-M11-016 -->

### SC-M11-016

#### 1. Tên kịch bản chuẩn

Kick một thành viên thuộc thẩm quyền khỏi nhóm — BF-M11-016; owner [UC-M11-013](../../us/US-M11.md#uc-m11-013); nhóm UC chính: UC-M11-032.

#### 2. Actor thực hiện

ACT-011 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có N11, An Owner muốn kick Chi Member; dữ liệu P11/C11 của Chi vẫn còn, P11 ẩn danh, Chi20 điểm. Thứ bậc/quyền/cờ/Khóa kiểm khi xử lý.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-016 -->

| result | condition |
|---|---|
| SUCCESS | Đích ra khỏi đúng nhóm và nhận thông báo, không tự bị chặn; nội dung/tác giả/ẩn danh/điểm giữ, quyền sau rời phụ thuộc Public/Private. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-016 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-011 | An mở chức năng kick thành viên N11. | An Owner; N11 Hoạt động/Bình thường; Chi Member | M2 | FR-M11-09.01 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner và nhóm không Khóa; chèn UC006/023 trả thành viên kèm vai trò để chọn. | An Owner, Bình Group Mod bổ nhiệm 01/09/2026 09:00+07, Dũng Group Mod bổ nhiệm lại 20/10/2026 09:00+07 (lần trước không tính), Chi Member vào 01/08/2026, Lan Member vào 01/07/2026. Đây là snapshot chuẩn, từng chức năng có thể thay dữ liệu đích ghi ngay tại bước. | M3 | FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| M3 | ACT-011 | An chọn kick Chi khỏi N11. | target=U-C Member N11; An Owner; T | M4 | FR-M11-09.01 |
| M4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Owner và đích thấp hơn, đưa Chi ra khỏi nhóm; giữ P11/C11, tên tác giả như trước (P11 vẫn ẩn danh), điểm 20 giữ 20. Gửi thông báo kick cho Chi, không tự chặn. N11 Public nên quyền sửa/xóa nội dung mình còn theo M03/M04; quay lại qua cổng tham gia nếu không bị chặn. Trả kết quả đã kick. | U-C Member→người ngoài N11; P11/C11 giữ; 20→20; thông báo U-C; không blocked | END:SUCCESS | FR-M11-09.01, FR-M11-09.05, FR-M11-09.06, FR-M11-09.07, FR-M11-10.08, BR-M11-05, BR-M11-06, BR-M11-24, BR-M11-37, FR-M12-02.15, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-016 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M3 | Owner chọn kick Bình Group Mod thay vì Chi Member | E1.1 | FR-M11-09.01, FR-M11-09.05, FR-M11-09.06, FR-M11-09.07, FR-M11-10.08, BR-M11-05, BR-M11-24, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E2 | system | M4 | Đích đã thành Owner trước lúc xử lý | E2.1 | FR-M11-09.01, FR-M11-09.03, BR-M11-05, BR-M11-06 |
| E3 | system | M1 | Owner kick thành viên ở nhóm Private, hệ quả quyền sau kick khác Public | E3.1 | FR-M11-09.01, FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-09.05, FR-M11-09.06, FR-M11-09.07, FR-M11-10.09, BR-M11-24, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |
| E4 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E4.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E5 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E5.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E6 | system | M2 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | E6.1 | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |
| E7 | system | M4 | Nhóm chuyển Bị khóa hoặc cờ Group Tắt với người không ADMIN sau lượt đọc nhưng trước lúc lưu | E7.1 | FR-M11-16.07, FR-M11-17.01, FR-M11-17.08, BR-M11-28, BR-M11-29 |
| E8 | system | M1 | ACT-010 — Bình Group Mod kick Chi Member. Actor khởi tạo ACT-010; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M11-09.02, FR-M11-09.05, FR-M11-09.06, FR-M11-09.07, FR-M11-10.08, BR-M11-05, BR-M11-24, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E9 | system | M1 | ACT-010 — Bình Group Mod cố kick An Owner. Actor khởi tạo ACT-010; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M11-09.03, BR-M11-05 |
| E10 | system | M1 | ACT-010 — Bình Group Mod cố kick Dũng Group Mod. Actor khởi tạo ACT-010; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M11-09.03, BR-M11-05 |
| E11 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Owner; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E11.1 | FR-M11-09.01, FR-M11-17.03, FR-M10-12.08, FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-09.05, FR-M11-09.06, FR-M11-09.07, FR-M11-10.08, BR-M11-05, BR-M11-24, BR-M11-37, FR-M12-02.15, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |
| E12 | system | M1 | ACT-009 — Lan Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E12.1 | FR-M11-09.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E13 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E13.1 | FR-M11-09.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E14 | system | M1 | ACT-008 — Minh MODERATOR không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E14.1 | FR-M11-09.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-016 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-011 | An chọn kick Bình khỏi N11. | Bình Group Mod thấp hơn An Owner; danh sách đã trả đủ vai trò | E1.2 | FR-M11-09.01 |
| E1.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner/đích Group Mod/không Khóa, đưa Bình ra khỏi nhóm; giữ bài/bình luận/cách hiện tác giả/điểm, thông báo kick cho Bình. Không tự chặn; Public còn quyền nội dung mình theo M03/M04, tham gia lại theo cổng. | Bình Group Mod→người ngoài; nội dung/điểm giữ; recipient U-B | END:SUCCESS | FR-M11-09.01, FR-M11-09.05, FR-M11-09.06, FR-M11-09.07, FR-M11-10.08, BR-M11-05, BR-M11-24, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-016 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống kiểm thứ bậc hiện tại và không kick Owner theo lệnh cũ; không dùng dữ liệu danh sách cũ để cấp quyền. | Target không còn thấp hơn; tư cách hiện tại giữ | END:REJECTED | FR-M11-09.01, FR-M11-09.03, BR-M11-05, BR-M11-06 |


<!-- sc:branch SC-M11-016 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-011 | An mở chức năng kick trong N12 Private. | Owner An; Chi Member N12; các lớp nhóm khác Bình thường | E3.2 | FR-M11-09.01 |
| E3.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner/không Khóa, trả thành viên/vai trò N12 để Owner chọn. | An Owner/Chi Member/Bình Group Mod | E3.3 | FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E3.3 | ACT-011 | An chọn kick Chi khỏi N12. | Chi Member; N12 Private | E3.4 | FR-M11-09.01 |
| E3.4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner và đích thấp hơn/không Khóa, kick Chi, giữ bài/bình luận/tác giả/ẩn danh/điểm; thông báo Chi. Vì Private, Chi không sửa/xóa được nội dung mình sau kick; quay lại theo cổng nếu không bị chặn. | Chi ngoài N12; dữ liệu/điểm giữ; recipient U-C; không tự chặn | END:SUCCESS | FR-M11-09.01, FR-M11-09.05, FR-M11-09.06, FR-M11-09.07, FR-M11-10.09, BR-M11-24, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-016 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-016 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-016 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối hành vi trong nhóm Bị khóa kể cả Owner/Group Mod hoặc ADMIN; quyền đọc/lưu/báo cáo/Member-Group Mod tự rời và tự kế nhiệm theo hợp đồng riêng vẫn giữ. | Nhóm Bị khóa; không thực hiện thay đổi/duyệt/nhận mở queue bị chặn | END:REJECTED | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |


<!-- sc:branch SC-M11-016 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống kiểm lại điều kiện hiện tại; nếu cờ Tắt từ chối đúng thông báo “Hệ thống đang bận, vui lòng thử lại sau”, nếu Khóa từ chối hành vi đã bị chặn. Không dùng lần đọc trước để hoàn tất thay đổi. | Không có thay đổi được yêu cầu của lần lưu này; trạng thái hiện tại giữ | END:REJECTED | FR-M11-16.07, FR-M11-17.01, FR-M11-17.08, BR-M11-28, BR-M11-29 |


**E8 — thay toàn bộ M1 đến kết thúc:** Bình Group Mod kick Chi Member. Actor khởi tạo ACT-010; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-016 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-010 | Bình chọn kick Chi khỏi N11. | Bình Group Mod; Chi Member; không bắt bước danh sách chọn riêng của Owner | E8.2 | FR-M11-09.02 |
| E8.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod đúng nhóm/Chi thấp hơn/không Khóa, đưa Chi ra; giữ nội dung/tác giả/ẩn danh/điểm 20; thông báo Chi; không tự chặn, cho quay lại theo cổng. Public còn quyền sửa/xóa nội dung mình. | Chi Member→người ngoài N11; điểm 20; P11/C11 giữ; recipient U-C | END:SUCCESS | FR-M11-09.02, FR-M11-09.05, FR-M11-09.06, FR-M11-09.07, FR-M11-10.08, BR-M11-05, BR-M11-24, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E9 — thay toàn bộ M1 đến kết thúc:** Bình Group Mod cố kick An Owner. Actor khởi tạo ACT-010; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-016 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-010 | Bình yêu cầu kick An Owner. | N11; actorGroup Mod; target ngang/cao hơn | E9.2 | FR-M11-09.03 |
| E9.2 | SYSTEM | Hệ thống từ chối kick vì thứ bậc, không đưa đích ra khỏi nhóm. | Membership/role của An Owner giữ | END:REJECTED | FR-M11-09.03, BR-M11-05 |


**E10 — thay toàn bộ M1 đến kết thúc:** Bình Group Mod cố kick Dũng Group Mod. Actor khởi tạo ACT-010; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-016 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-010 | Bình yêu cầu kick Dũng Group Mod. | N11; actorGroup Mod; target ngang/cao hơn | E10.2 | FR-M11-09.03 |
| E10.2 | SYSTEM | Hệ thống từ chối kick vì thứ bậc, không đưa đích ra khỏi nhóm. | Membership/role của Dũng Group Mod giữ | END:REJECTED | FR-M11-09.03, BR-M11-05 |


**E11 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Owner; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-016 E11 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E11.1 | ACT-007 | Hòa mở chức năng kick thành viên N11. | Hòa Owner; N11 Hoạt động/Bình thường; Chi Member; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E11.2 | FR-M11-09.01, FR-M11-17.03, FR-M10-12.08 |
| E11.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner và nhóm không Khóa; chèn UC006/023 trả thành viên kèm vai trò để chọn. | Hòa Owner, Bình Group Mod bổ nhiệm 01/09/2026 09:00+07, Dũng Group Mod bổ nhiệm lại 20/10/2026 09:00+07 (lần trước không tính), Chi Member vào 01/08/2026, Lan Member vào 01/07/2026. Đây là snapshot chuẩn, từng chức năng có thể thay dữ liệu đích ghi ngay tại bước. | E11.3 | FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |
| E11.3 | ACT-007 | Hòa chọn kick Chi khỏi N11. | target=U-C Member N11; Hòa Owner; T | E11.4 | FR-M11-09.01, FR-M11-17.03, FR-M10-12.08 |
| E11.4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Owner và đích thấp hơn, đưa Chi ra khỏi nhóm; giữ P11/C11, tên tác giả như trước (P11 vẫn ẩn danh), điểm 20 giữ 20. Gửi thông báo kick cho Chi, không tự chặn. N11 Public nên quyền sửa/xóa nội dung mình còn theo M03/M04; quay lại qua cổng tham gia nếu không bị chặn. Trả kết quả đã kick. | U-C Member→người ngoài N11; P11/C11 giữ; 20→20; thông báo U-C; không blocked | END:SUCCESS | FR-M11-09.01, FR-M11-09.05, FR-M11-09.06, FR-M11-09.07, FR-M11-10.08, BR-M11-05, BR-M11-06, BR-M11-24, BR-M11-37, FR-M12-02.15, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


**E12 — thay toàn bộ M1 đến kết thúc:** Lan Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-016 E12 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E12.1 | ACT-009 | Lan Member yêu cầu: Kick một thành viên thuộc thẩm quyền khỏi nhóm. | Đúng nhóm/đích của chức năng; Lan Member không có vai trò nhóm bắt buộc; Group=true | E12.2 | FR-M11-09.04, BR-M11-06 |
| E12.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-09.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E13 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-016 E13 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E13.1 | ACT-002 | Phúc người ngoài yêu cầu: Kick một thành viên thuộc thẩm quyền khỏi nhóm. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E13.2 | FR-M11-09.04, BR-M11-06 |
| E13.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-09.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E14 — thay toàn bộ M1 đến kết thúc:** Minh MODERATOR không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-016 E14 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E14.1 | ACT-008 | Minh MODERATOR không Group Mod yêu cầu: Kick một thành viên thuộc thẩm quyền khỏi nhóm. | Đúng nhóm/đích của chức năng; Minh MODERATOR không Group Mod không có vai trò nhóm bắt buộc; Group=true | E14.2 | FR-M11-09.04, BR-M11-06 |
| E14.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-09.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-016 -->

<a id="sc-m11-017"></a>

<!-- sc:scenario SC-M11-017 -->

### SC-M11-017

#### 1. Tên kịch bản chuẩn

Tự rời nhóm, bảo toàn nội dung và kế nhiệm khi cần — BF-M11-017; owner [UC-M11-014](../../us/US-M11.md#uc-m11-014); nhóm UC chính: UC-M11-032.

#### 2. Actor thực hiện

ACT-011 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có nhóm và thành viên muốn rời; chuẩn An Owner N11 Public còn Bình/Dũng/Chi/Lan. Quyền/cờ/Khóa kiểm trong luồng; phải chọn và chuyển Owner trước rồi đưa An ra. Đường Member/Group Mod rời ngay và Owner cuối xác nhận xóa hoặc không xác nhận nằm trong mục6, không giả đã chuyển quyền làm tiền điều kiện.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-017 -->

| result | condition |
|---|---|
| SUCCESS | Member/Group Mod rời: không còn là thành viên, giữ nội dung/tác giả/điểm. Owner còn người: người được chỉ định thành Owner trước rồi Owner cũ ra; thông báo người kế nhiệm. Owner cuối xác nhận cảnh báo: nhóm Đã xóa, giữ dữ liệu/điểm. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |
| CANCELLED | Owner cuối không xác nhận cảnh báo: không xóa nhóm và không đưa Owner ra theo hành vi này, dữ liệu/vai trò/thành viên giữ. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-017 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-011 | An chọn rời N11 còn thành viên khác. | An Owner; Bình/Dũng/Chi/Lan còn trong N11 | M2 | FR-M11-10.03 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner/không Khóa; UC015 chèn UC006/023 hiện thành viên kèm vai trò, yêu cầu chọn một thành viên khác làm Owner và xác nhận rời. | An Owner, Bình Group Mod bổ nhiệm 01/09/2026 09:00+07, Dũng Group Mod bổ nhiệm lại 20/10/2026 09:00+07 (lần trước không tính), Chi Member vào 01/08/2026, Lan Member vào 01/07/2026. Đây là snapshot chuẩn, từng chức năng có thể thay dữ liệu đích ghi ngay tại bước. | M3 | FR-M11-10.03, FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-04, BR-M11-25, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| M3 | ACT-011 | An chọn Chi làm Owner rồi xác nhận rời. | Người kế nhiệm U-C hiện Member; An xác nhận rời; T | M4 | FR-M11-10.04 |
| M4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm lại Owner/không Khóa và Chi là thành viên khác; chuyển Chi→Owner TRƯỚC đưa An ra khỏi nhóm. Gửi thông báo trở thành Owner cho Chi. Giữ nội dung/tác giả/ẩn danh/điểm của An; Public còn quyền nội dung mình theo M03/M04. Trả đã chuyển quyền và An đã rời. | Owner duy nhất Chi; An người ngoài N11; Chi nhận thông báo; dữ liệu/điểm An giữ; không tự kế nhiệm theo thâm niên | END:SUCCESS | FR-M11-10.02, FR-M11-10.04, FR-M11-10.07, FR-M11-10.08, BR-M11-04, BR-M11-24, BR-M11-25, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-017 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E1.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E2 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E2.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E3 | system | M1 | Owner còn người nhưng chưa chọn kế nhiệm khi xác nhận rời | E3.1 | FR-M11-10.03, FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-04, BR-M11-25, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-10.05 |
| E4 | user-choice | M1 | Owner cuối chọn rời, xác nhận cảnh báo xóa | E4.1 | FR-M11-10.06, BR-M11-25, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-15.01, FR-M11-15.02, FR-M11-15.03, FR-M11-15.05, FR-M12-02.14, FR-M11-01.06 |
| E5 | user-choice | M1 | Owner cuối không xác nhận cảnh báo xóa | E5.1 | FR-M11-10.06, BR-M11-25, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E6 | system | M1 | Owner muốn rời khi nhóm Bị khóa | E6.1 | FR-M11-16.08, BR-M11-28 |
| E7 | system | M1 | ACT-010 — Bình Group Mod tự rời kể cả nhóm Bị khóa. Actor khởi tạo ACT-010; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M11-16.09, FR-M11-10.01, FR-M11-10.02, FR-M11-10.08, BR-M11-24, BR-M11-28, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-29 |
| E8 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Member; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M11-10.01, FR-M11-17.03, FR-M10-12.08, FR-M11-10.02, FR-M11-10.08, FR-M11-16.09, BR-M11-24, BR-M11-28, FR-M12-02.15, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-29 |
| E9 | system | M1 | ACT-009 — Chi tự rời N12 Private, nội dung giữ nhưng không sửa/xóa sau rời. Actor khởi tạo ACT-009; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M11-10.01, FR-M11-10.02, FR-M11-10.09, BR-M11-24, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E10 | system | M1 | ACT-009 — Chi Member tự rời N11 Public, kể cả Bị khóa nếu cờ cho phép. Actor khởi tạo ACT-009; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M11-10.01, FR-M11-10.02, FR-M11-10.08, FR-M11-16.09, BR-M11-24, BR-M11-28, FR-M12-02.15, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-29 |


<!-- sc:branch SC-M11-017 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-017 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-017 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-011 | An chọn rời N11 còn thành viên khác. | An Owner; Bình/Dũng/Chi/Lan còn trong N11 | E3.2 | FR-M11-10.03 |
| E3.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner/không Khóa; UC015 chèn UC006/023 hiện thành viên kèm vai trò, yêu cầu chọn một thành viên khác làm Owner và xác nhận rời. | An Owner, Bình Group Mod bổ nhiệm 01/09/2026 09:00+07, Dũng Group Mod bổ nhiệm lại 20/10/2026 09:00+07 (lần trước không tính), Chi Member vào 01/08/2026, Lan Member vào 01/07/2026. Đây là snapshot chuẩn, từng chức năng có thể thay dữ liệu đích ghi ngay tại bước. | E3.3 | FR-M11-10.03, FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-04, BR-M11-25, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E3.3 | ACT-011 | An xác nhận rời mà chưa chọn người kế nhiệm. | Người kế nhiệm=trống; còn thành viên khác | E3.4 | FR-M11-10.05 |
| E3.4 | SYSTEM | Hệ thống từ chối rời vì chưa chỉ định, không tự chọn theo thâm niên thay Owner. | An vẫn Owner/thành viên; Chi vẫn Member; không thông báo kế nhiệm | END:REJECTED | FR-M11-10.05, BR-M11-25 |


<!-- sc:branch SC-M11-017 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-011 | An là thành viên duy nhất chọn rời N11. | N11 chỉAn Owner, Hoạt động/Bình thường; Group=true | E4.2 | FR-M11-10.06 |
| E4.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner/không Khóa; nhóm chỉ có An, cảnh báo rời sẽ xóa nhóm, chờ xác nhận; chưa xóa. | An Owner/thành viên duy nhất; cảnh báo nhóm sẽ bị xóa | E4.3 | FR-M11-10.06, BR-M11-25, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E4.3 | ACT-011 | An xác nhận rời và xóa nhóm theo cảnh báo. | N11 chỉAn; xác nhận=true | E4.4 | FR-M11-10.06 |
| E4.4 | SYSTEM | Hệ thống kiểm lại căn cứ Owner cuối đã xác nhận/nhóm cho phép. Áp xóa mềm UC022: nhóm→Đã xóa, nhóm và mọi nội dung không hiện với bất kỳ ai kể cả thành viên cũ; giữ dữ liệu, giữ điểm từng người (Chi có 20 điểm từ bài vẫn 20). Từ chối mở/tham gia/đăng vào nhóm đã xóa; nhóm vẫn tính vào lịch sử tạo trong 24 giờ nếu còn trong khoảng. Trả kết quả Đã xóa. | N11 Hoạt động→Đã xóa; dữ liệu/điểm giữ; không gọi chọn kế nhiệm | END:SUCCESS | FR-M11-10.06, FR-M11-15.01, FR-M11-15.02, FR-M11-15.03, FR-M11-15.05, BR-M11-23, FR-M12-02.14, FR-M11-01.06, BR-M11-25, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-017 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-011 | An là thành viên duy nhất chọn rời N11. | N11 chỉAn Owner, Hoạt động/Bình thường; Group=true | E5.2 | FR-M11-10.06 |
| E5.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner/không Khóa; nhóm chỉ có An, cảnh báo rời sẽ xóa nhóm, chờ xác nhận; chưa xóa. | An Owner/thành viên duy nhất; cảnh báo nhóm sẽ bị xóa | E5.3 | FR-M11-10.06, BR-M11-25, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E5.3 | ACT-011 | An chọn không xác nhận rời/xóa. | Xác nhận=false | E5.4 | FR-M11-10.06 |
| E5.4 | SYSTEM | Hệ thống không thực hiện xóa/rời do không có xác nhận. | N11 Hoạt động; An vẫn Owner/thành viên duy nhất | END:CANCELLED | FR-M11-10.06, BR-M11-25 |


<!-- sc:branch SC-M11-017 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-011 | An chọn rời N11 đang Bị khóa. | An Owner; N11 Bị khóa; có thểcòn người hoặc chỉAn | E6.2 | FR-M11-16.08 |
| E6.2 | SYSTEM | Hệ thống từ chối Owner rời nhóm Bị khóa; không chuyển Owner hoặc xóa nhóm theo yêu cầu này. | An chưa rời; nhóm/role giữ | END:REJECTED | FR-M11-16.08, BR-M11-28 |


**E7 — thay toàn bộ M1 đến kết thúc:** Bình Group Mod tự rời kể cả nhóm Bị khóa. Actor khởi tạo ACT-010; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-017 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-010 | Bình chọn rời N11 Bị khóa. | Bình Group Mod; không Owner; Group=true | E7.2 | FR-M11-16.09 |
| E7.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Group Mod được tự rời nhóm Khóa, đưa Bình ra; giữ nội dung/tác giả/ẩn danh/điểm. Public còn quyền nội dung mình, quay lại theo cổng khi điều kiện cho phép. Trả đã rời. | Bình→người ngoài; không chuyển/xóaOwner; dữ liệu/điểm giữ | END:SUCCESS | FR-M11-10.01, FR-M11-10.02, FR-M11-10.08, FR-M11-16.09, BR-M11-24, BR-M11-28, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-29 |


**E8 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Member; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-017 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-007 | Hòa chọn rời N11. | Hòa Member N11; P11 ẩn danh/C11; 20 điểm; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E8.2 | FR-M11-10.01, FR-M11-17.03, FR-M10-12.08 |
| E8.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Hòa là thành viên, Member được tự rời kể cả Bị khóa; đưa Hòa ra. Giữ nội dung/tác giả/ẩn danh và điểm. N11 Public nên vẫn sửa/xóa nội dung mình qua M03/M04; quay lại theo SC007, không đặt giới hạn nhóm hoặc tự khôi phục role. Trả đã rời. | Hòa Member→người ngoài; P11/C11 giữ; 20→20; Public; không chặn | END:SUCCESS | FR-M11-10.01, FR-M11-10.02, FR-M11-10.08, FR-M11-16.09, BR-M11-24, BR-M11-28, FR-M12-02.15, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-29, FR-M10-12.08 |


**E9 — thay toàn bộ M1 đến kết thúc:** Chi tự rời N12 Private, nội dung giữ nhưng không sửa/xóa sau rời. Actor khởi tạo ACT-009; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-017 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-009 | Chi chọn rời N12 Private. | Chi Member; N12 Private; P11/C11 củaChi; 20 điểm | E9.2 | FR-M11-10.01 |
| E9.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Member; đưa Chi ra, giữ nội dung/tác giả/ẩn danh/điểm. Vì Private, sau rời không sửa/xóa nội dung mình; tham gia lại theo cổng nếu đủ điều kiện. Trả đã rời. | Chi ngoài N12; P11/C11 giữ; 20→20; không tự chặn | END:SUCCESS | FR-M11-10.01, FR-M11-10.02, FR-M11-10.09, BR-M11-24, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E10 — thay toàn bộ M1 đến kết thúc:** Chi Member tự rời N11 Public, kể cả Bị khóa nếu cờ cho phép. Actor khởi tạo ACT-009; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-017 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-009 | Chi chọn rời N11. | Chi Member N11; P11 ẩn danh/C11; 20 điểm | E10.2 | FR-M11-10.01 |
| E10.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Chi là thành viên, Member được tự rời kể cả Bị khóa; đưa Chi ra. Giữ nội dung/tác giả/ẩn danh và điểm. N11 Public nên vẫn sửa/xóa nội dung mình qua M03/M04; quay lại theo SC007, không đặt giới hạn nhóm hoặc tự khôi phục role. Trả đã rời. | Chi Member→người ngoài; P11/C11 giữ; 20→20; Public; không chặn | END:SUCCESS | FR-M11-10.01, FR-M11-10.02, FR-M11-10.08, FR-M11-16.09, BR-M11-24, BR-M11-28, FR-M12-02.15, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-29 |


<!-- sc:end SC-M11-017 -->

<a id="sc-m11-018"></a>

<!-- sc:scenario SC-M11-018 -->

### SC-M11-018

#### 1. Tên kịch bản chuẩn

Gửi bài mới hoặc gửi lại bài bị từ chối vào nhóm — BF-M11-018; owner [UC-M11-033](../../us/US-M11.md#uc-m11-033); nhóm UC chính: UC-M11-033.

#### 2. Actor thực hiện

ACT-009 là actor chính của đường chuẩn. ACT-006 hỗ trợ khi có quét AI; không khởi tạo mục tiêu đăng bài. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

M03 cung cấp P18 đã soạn/đã sửa và tác giả thật; không triển khai lại trình soạn, tệp hoặc poll chung. Chuẩn Chi Member N11 Public, P18 Nháp, tiêu đề/nội dung hợp lệ, cảnh cáo không MEDIUM/HEAVY; ẩn danh Bật, Chi chọn Có, duyệt trước Tắt, AI tổng/Moderation Bật. Quyền gửi và kết quả quét kiểm trong luồng.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-018 -->

| result | condition |
|---|---|
| SUCCESS | Bài được gửi qua đúng cổng và trả kết quả cho tác giả. Đã đăng: đúng phạm vi/ẩn danh, sự kiện M07 và mốc embedding theo owner. Nhánh chờ: xác nhận đã ghi nhận P18 trong queue nhóm hoặc Mod hệ thống đúng vai trò, chưa đăng/không hiện thường; mục tiêu gửi hoàn tất ở ghi nhận theo UC033. AI tự từ chối dùng REJECTED, không phải thành công đăng. |
| REJECTED | Yêu cầu gửi bị từ chối theo quyền/trạng thái/dữ liệu hoặc P18 Bị từ chối bởi AI với nhóm vi phạm trả về và sự kiện M03/M07. Không đăng/không ghi thành công gửi khi bị chặn. Tác giả có thể sửa/gửi lại qua chính SC018 hoặc khiếu nại AI theo SC-M09-001 nếu đủ điều kiện; không khiếu nại từ chối cấp nhóm. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-018 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-009 | Chi gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Chi; roleNhóm=Member; Nháp→gửi; anonymous=True; duyệt trước=False; AI tổng/Moderation=đều Bật | M2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Chi và lựa chọn ẩn danh=True hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=Chi; anonymous=True; attempt=1 | M3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| M3 | ACT-006 | Dịch vụ AI trả điểm quét và nhóm vi phạm cho P18. | P18 score=0.3; khoảng=thấp; nhóm vi phạm=[] | M4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| M4 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Public: xem ở trang nhóm, tab Group của thành viên; đủ điều kiện thì Trending/Following theo M14, không Newest. Bài ẩn danh không vào Following nhờ theo dõi tác giả. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Đã đăng; group=N11 Public; author=Chi; anonymous=True; score=0.3 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-018 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M3 | AI trả điểm 0.49; Chi không Owner, duyệt trước Tắt | E1.1 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E2 | system | M3 | AI trả điểm 0.5; Chi không Owner, duyệt trước Tắt | E2.1 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E3 | system | M3 | AI trả điểm 0.89; Chi không Owner, duyệt trước Tắt | E3.1 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E4 | system | M3 | AI trả điểm 0.9; Chi không Owner, duyệt trước Tắt | E4.1 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E5 | system | M3 | AI trả điểm 0.95; Chi không Owner, duyệt trước Tắt | E5.1 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E6 | system | M1 | Duyệt trước Bật, điểm0.3 vẫn chờ nhóm | E6.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E7 | system | M1 | Lần đầu lỗi, sau 2 giây thử lại đúng một lần trả0.3 | E7.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E8 | system | M1 | Cả hai lần quét lỗi, duyệt trước Tắt vẫn chờ nhóm | E8.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E9 | system | M1 | AI tổng hoặc Moderation Tắt, duyệt trước Tắt đăng ngay | E9.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |
| E10 | system | M1 | AI tổng hoặc Moderation Tắt, duyệt trước Bật chờ nhóm | E10.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |
| E11 | system | M1 | N12 Private, bài được đăng chỉ trong nhóm/tab Group | E11.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E12 | user-choice | M1 | Chi không chọn ẩn danh khi công tắc Bật | E12.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E13 | user-choice | M1 | Tác giả đã sửa bài Bị từ chối cấp nhóm và gửi lại, cổng chạy thêm một lần | E13.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.11, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E14 | user-choice | M1 | Tác giả đã sửa bài Bị AI từ chối và gửi lại, không chờ kết luận khiếu nại để gửi | E14.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.11, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E15 | system | M1 | Công tắc ẩn danh Tắt, Chi bỏ lựa chọn ẩn danh rồi gửi hợp lệ | E15.1 | FR-M11-12.08, FR-M11-02.06, BR-M11-16, FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E16 | system | M2 | P18 không còn Nháp/Bị từ chối | E16.1 | FR-M03-04.07 |
| E17 | system | M2 | Chi bị cảnh cáo MEDIUM hoặc HEAVY | E17.1 | FR-M03-04.10 |
| E18 | system | M2 | Người gửi không phải tác giả của P18 | E18.1 | FR-M03-04.06 |
| E19 | system | M1 | Tiêu đề thiếu hoặc nội dung/poll thiếu, tác giả bổ sung rồi gửi | E19.1 | FR-M03-04.08, FR-M03-04.09, FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E20 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E20.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E21 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E21.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E22 | system | M2 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | E22.1 | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |
| E23 | system | M1 | Dịch vụ AI im lặng cả hai lần, duyệt trước Tắt | E23.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E24 | system | M1 | ACT-010 — Bình có vai trò nhóm Group Mod; biến thể {'preapproval': False}. Actor khởi tạo ACT-010; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E24.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E25 | system | M1 | ACT-011 — An có vai trò nhóm Owner; biến thể {'preapproval': False}. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E25.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E26 | system | M1 | ACT-011 — An có vai trò nhóm Owner; biến thể {'preapproval': True, 'score': 0.5}. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E26.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E27 | system | M1 | ACT-011 — An có vai trò nhóm Owner; biến thể {'preapproval': True, 'score': 0.89}. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E27.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E28 | system | M1 | ACT-011 — An có vai trò nhóm Owner; biến thể {'preapproval': True, 'score': 0.9}. Actor khởi tạo ACT-011; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E28.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E29 | system | M1 | ACT-011 — An có vai trò nhóm Owner; biến thể {'preapproval': True, 'mode': 'failed'}. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E29.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E30 | system | M1 | ACT-011 — An có vai trò nhóm Owner; biến thể {'preapproval': True, 'mode': 'off'}. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E30.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |
| E31 | system | M1 | ACT-011 — An có vai trò nhóm Owner; biến thể {'preapproval': True, 'mode': 'retry-ok'}. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E31.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| E32 | system | M1 | ACT-007 — Hòa có vai trò nhóm Member; ADMIN miễn quét/qua cờ, vẫn kiểm membership/Khóa; biến thể {'preapproval': False}. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E32.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |
| E33 | system | M1 | ACT-007 — Hòa có vai trò nhóm Member; ADMIN miễn quét/qua cờ, vẫn kiểm membership/Khóa; biến thể {'preapproval': True}. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E33.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |
| E34 | system | M1 | ACT-007 — Hòa có vai trò nhóm Owner; ADMIN miễn quét/qua cờ, vẫn kiểm membership/Khóa; biến thể {'preapproval': False}. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E34.1 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |
| E35 | system | M1 | ACT-001 — Guest yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E35.1 | FR-M11-12.11, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E36 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E36.1 | FR-M11-12.11, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E37 | system | M1 | ACT-008 — Minh MODERATOR không thành viên yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E37.1 | FR-M11-12.11, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E38 | system | M1 | ACT-007 — Hòa ADMIN không thành viên yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E38.1 | FR-M11-12.11, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-018 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-006 | Dịch vụ AI trả kết quả chấm P18. | P18 score=0.49; nhóm vi phạm=[] | E1.2 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E1.2 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Public: xem ở trang nhóm, tab Group của thành viên; đủ điều kiện thì Trending/Following theo M14, không Newest. Bài ẩn danh không vào Following nhờ theo dõi tác giả. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Đã đăng; group=N11 Public; author=Chi; anonymous=True; score=0.49 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


<!-- sc:branch SC-M11-018 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-006 | Dịch vụ AI trả kết quả chấm P18. | P18 score=0.5; nhóm vi phạm=[] | E2.2 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E2.2 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Giữ P18 Chờ duyệt (chờ nhóm duyệt), đưa vào hàng chờ riêng N12 hoặc N11 đang xét, không trộn queue báo cáo/Mod hệ thống. Trả đã ghi nhận bài chờ nhóm; chỉ tác giả/người duyệt theo quyền biết trạng thái, người xem thường không thấy, chưa đăng. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Chờ duyệt/chờ nhóm duyệt; group=N11 Public; author=Chi; anonymous=True; score=0.5 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


<!-- sc:branch SC-M11-018 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-006 | Dịch vụ AI trả kết quả chấm P18. | P18 score=0.89; nhóm vi phạm=[] | E3.2 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E3.2 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Giữ P18 Chờ duyệt (chờ nhóm duyệt), đưa vào hàng chờ riêng N12 hoặc N11 đang xét, không trộn queue báo cáo/Mod hệ thống. Trả đã ghi nhận bài chờ nhóm; chỉ tác giả/người duyệt theo quyền biết trạng thái, người xem thường không thấy, chưa đăng. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Chờ duyệt/chờ nhóm duyệt; group=N11 Public; author=Chi; anonymous=True; score=0.89 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


<!-- sc:branch SC-M11-018 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-006 | Dịch vụ AI trả kết quả chấm P18. | P18 score=0.9; nhóm vi phạm=[Quấy rối] | E4.2 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E4.2 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Chuyển P18→Bị từ chối bởi AI, cung cấp nhóm vi phạm quét trả về cho tác giả qua M03 và sự kiện bài bị từ chối M07; không coi là nhóm từ chối. Tác giả được sửa/gửi lại hoặc khiếu nại M09 (luồng khác), chưa đăng bài. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Bị từ chối/nguồn AI; group=N11 Public; author=Chi; anonymous=True; score=0.9 | END:REJECTED | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


<!-- sc:branch SC-M11-018 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-006 | Dịch vụ AI trả kết quả chấm P18. | P18 score=0.95; nhóm vi phạm=[Quấy rối] | E5.2 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E5.2 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Chuyển P18→Bị từ chối bởi AI, cung cấp nhóm vi phạm quét trả về cho tác giả qua M03 và sự kiện bài bị từ chối M07; không coi là nhóm từ chối. Tác giả được sửa/gửi lại hoặc khiếu nại M09 (luồng khác), chưa đăng bài. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Bị từ chối/nguồn AI; group=N11 Public; author=Chi; anonymous=True; score=0.95 | END:REJECTED | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


<!-- sc:branch SC-M11-018 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-009 | Chi gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Chi; roleNhóm=Member; Nháp→gửi; anonymous=True; duyệt trước=True; AI tổng/Moderation=đều Bật | E6.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E6.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Chi và lựa chọn ẩn danh=True hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=Chi; anonymous=True; attempt=1 | E6.3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E6.3 | ACT-006 | Dịch vụ AI trả điểm quét và nhóm vi phạm cho P18. | P18 score=0.3; khoảng=thấp; nhóm vi phạm=[] | E6.4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E6.4 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Giữ P18 Chờ duyệt (chờ nhóm duyệt), đưa vào hàng chờ riêng N12 hoặc N11 đang xét, không trộn queue báo cáo/Mod hệ thống. Trả đã ghi nhận bài chờ nhóm; chỉ tác giả/người duyệt theo quyền biết trạng thái, người xem thường không thấy, chưa đăng. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Chờ duyệt/chờ nhóm duyệt; group=N11 Public; author=Chi; anonymous=True; score=0.3 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


<!-- sc:branch SC-M11-018 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | ACT-009 | Chi gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Chi; roleNhóm=Member; Nháp→gửi; anonymous=True; duyệt trước=False; AI tổng/Moderation=đều Bật | E7.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E7.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Chi và lựa chọn ẩn danh=True hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=Chi; anonymous=True; attempt=1 | E7.3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E7.3 | ACT-006 | Dịch vụ AI trả lỗi lần thử đầu. | P18 attempt1=error; chưa có điểm; không tự đổi công tắc | E7.4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E7.4 | SYSTEM | Hệ thống ghi nhận lỗi lần đầu, đợi 2 giây rồi gửi lại đúng một lần, không song song và không đổi công tắc. Mỗi lần chấm không có kết quả sau 5 giây cũng tính lỗi. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; attempt=2; cùng bài/tác giả/nhóm; hai công tắc vẫn Bật | E7.5 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E7.5 | ACT-006 | Dịch vụ AI trả điểm quét sau lần thử thứ hai. | P18 attempt2=ok; score=0.3; nhóm vi phạm=[] | E7.6 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E7.6 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Public: xem ở trang nhóm, tab Group của thành viên; đủ điều kiện thì Trending/Following theo M14, không Newest. Bài ẩn danh không vào Following nhờ theo dõi tác giả. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Đã đăng; group=N11 Public; author=Chi; anonymous=True; score=0.3 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


<!-- sc:branch SC-M11-018 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | ACT-009 | Chi gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Chi; roleNhóm=Member; Nháp→gửi; anonymous=True; duyệt trước=False; AI tổng/Moderation=đều Bật | E8.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E8.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Chi và lựa chọn ẩn danh=True hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=Chi; anonymous=True; attempt=1 | E8.3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E8.3 | ACT-006 | Dịch vụ AI trả lỗi lần thử đầu. | P18 attempt1=error; chưa có điểm; không tự đổi công tắc | E8.4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E8.4 | SYSTEM | Hệ thống ghi nhận lỗi lần đầu, đợi 2 giây rồi gửi lại đúng một lần, không song song và không đổi công tắc. Mỗi lần chấm không có kết quả sau 5 giây cũng tính lỗi. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; attempt=2; cùng bài/tác giả/nhóm; hai công tắc vẫn Bật | E8.5 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E8.5 | ACT-006 | Dịch vụ AI trả lỗi lần thử thứ hai. | P18 attempt2=error; không điểm | E8.6 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E8.6 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Giữ P18 Chờ duyệt (chờ nhóm duyệt), đưa vào hàng chờ riêng N12 hoặc N11 đang xét, không trộn queue báo cáo/Mod hệ thống. Trả đã ghi nhận bài chờ nhóm; chỉ tác giả/người duyệt theo quyền biết trạng thái, người xem thường không thấy, chưa đăng. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Chờ duyệt/chờ nhóm duyệt; group=N11 Public; author=Chi; anonymous=True; score=không có sau 2 lỗi | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


<!-- sc:branch SC-M11-018 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | ACT-009 | Chi gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Chi; roleNhóm=Member; Nháp→gửi; anonymous=True; duyệt trước=False; AI tổng/Moderation=có một cờ Tắt | E9.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E9.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Chi và lựa chọn ẩn danh=True hợp lệ với công tắc. AI tổng hoặc Moderation tắt nên không gọi AI, khác lỗi quét. Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Public: xem ở trang nhóm, tab Group của thành viên; đủ điều kiện thì Trending/Following theo M14, không Newest. Bài ẩn danh không vào Following nhờ theo dõi tác giả. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Đã đăng; group=N11 Public; author=Chi; anonymous=True; score=không quét | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |


<!-- sc:branch SC-M11-018 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | ACT-009 | Chi gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Chi; roleNhóm=Member; Nháp→gửi; anonymous=True; duyệt trước=True; AI tổng/Moderation=có một cờ Tắt | E10.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E10.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Chi và lựa chọn ẩn danh=True hợp lệ với công tắc. AI tổng hoặc Moderation tắt nên không gọi AI, khác lỗi quét. Hệ thống nhận kết quả cổng UC016. Giữ P18 Chờ duyệt (chờ nhóm duyệt), đưa vào hàng chờ riêng N12 hoặc N11 đang xét, không trộn queue báo cáo/Mod hệ thống. Trả đã ghi nhận bài chờ nhóm; chỉ tác giả/người duyệt theo quyền biết trạng thái, người xem thường không thấy, chưa đăng. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Chờ duyệt/chờ nhóm duyệt; group=N11 Public; author=Chi; anonymous=True; score=không quét | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |


<!-- sc:branch SC-M11-018 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-009 | Chi gửi bài nháp P18 đã soạn qua M03 vào N12. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Chi; roleNhóm=Member; Nháp→gửi; anonymous=False; duyệt trước=False; AI tổng/Moderation=đều Bật | E11.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E11.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N12, giữ tác giả thật Chi và lựa chọn ẩn danh=False hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N12; author=Chi; anonymous=False; attempt=1 | E11.3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E11.3 | ACT-006 | Dịch vụ AI trả điểm quét và nhóm vi phạm cho P18. | P18 score=0.3; khoảng=thấp; nhóm vi phạm=[] | E11.4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E11.4 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Private: không ra Trending/Newest/Following với bất kỳ ai kể cả thành viên; thành viên xem trang nhóm/tab Group. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=False. | P18; state=Đã đăng; group=N12 Private; author=Chi; anonymous=False; score=0.3 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


<!-- sc:branch SC-M11-018 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | ACT-009 | Chi gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Chi; roleNhóm=Member; Nháp→gửi; anonymous=False; duyệt trước=False; AI tổng/Moderation=đều Bật | E12.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E12.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Chi và lựa chọn ẩn danh=False hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=Chi; anonymous=False; attempt=1 | E12.3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E12.3 | ACT-006 | Dịch vụ AI trả điểm quét và nhóm vi phạm cho P18. | P18 score=0.3; khoảng=thấp; nhóm vi phạm=[] | E12.4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E12.4 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Public: xem ở trang nhóm, tab Group của thành viên; đủ điều kiện thì Trending/Following theo M14, không Newest. Following vẫn theo điều kiện M14. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=False. | P18; state=Đã đăng; group=N11 Public; author=Chi; anonymous=False; score=0.3 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


<!-- sc:branch SC-M11-018 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | ACT-009 | Chi gửi lại bản đã sửa P18 từng bị từ chối qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Chi; roleNhóm=Member; Bị từ chối→gửi lại; anonymous=True; duyệt trước=False; AI tổng/Moderation=đều Bật | E13.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.11, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E13.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Chi và lựa chọn ẩn danh=True hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=Chi; anonymous=True; attempt=1 | E13.3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.11, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E13.3 | ACT-006 | Dịch vụ AI trả điểm quét và nhóm vi phạm cho P18. | P18 score=0.3; khoảng=thấp; nhóm vi phạm=[] | E13.4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E13.4 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Public: xem ở trang nhóm, tab Group của thành viên; đủ điều kiện thì Trending/Following theo M14, không Newest. Bài ẩn danh không vào Following nhờ theo dõi tác giả. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Đã đăng; group=N11 Public; author=Chi; anonymous=True; score=0.3 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


<!-- sc:branch SC-M11-018 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | ACT-009 | Chi gửi lại bản đã sửa P18 từng bị từ chối qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Chi; roleNhóm=Member; Bị từ chối→gửi lại; anonymous=True; duyệt trước=True; AI tổng/Moderation=đều Bật | E14.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.11, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E14.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Chi và lựa chọn ẩn danh=True hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=Chi; anonymous=True; attempt=1 | E14.3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.11, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E14.3 | ACT-006 | Dịch vụ AI trả điểm quét và nhóm vi phạm cho P18. | P18 score=0.3; khoảng=thấp; nhóm vi phạm=[] | E14.4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E14.4 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Giữ P18 Chờ duyệt (chờ nhóm duyệt), đưa vào hàng chờ riêng N12 hoặc N11 đang xét, không trộn queue báo cáo/Mod hệ thống. Trả đã ghi nhận bài chờ nhóm; chỉ tác giả/người duyệt theo quyền biết trạng thái, người xem thường không thấy, chưa đăng. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Chờ duyệt/chờ nhóm duyệt; group=N11 Public; author=Chi; anonymous=True; score=0.3 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


<!-- sc:branch SC-M11-018 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | ACT-009 | Chi muốn gửi P18 ẩn danh vào N11 đang tắt ẩn danh. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; anonymous=true; groupAnonymous=false | E15.2 | FR-M11-12.08 |
| E15.2 | SYSTEM | Hệ thống không cho chọn ẩn danh khi công tắc nhóm Tắt; chưa gửi bài bằng lựa chọn không hợp lệ, trả điều kiện lựa chọn. | P18 chưa gửi; không đổi các bài ẩn danh cũ | E15.3 | FR-M11-12.08, FR-M11-02.06, BR-M11-16 |
| E15.3 | ACT-009 | Chi gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Chi; roleNhóm=Member; Nháp→gửi; anonymous=False; duyệt trước=False; AI tổng/Moderation=đều Bật | E15.4 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E15.4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Chi và lựa chọn ẩn danh=False hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=Chi; anonymous=False; attempt=1 | E15.5 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E15.5 | ACT-006 | Dịch vụ AI trả điểm quét và nhóm vi phạm cho P18. | P18 score=0.3; khoảng=thấp; nhóm vi phạm=[] | E15.6 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E15.6 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Public: xem ở trang nhóm, tab Group của thành viên; đủ điều kiện thì Trending/Following theo M14, không Newest. Following vẫn theo điều kiện M14. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=False. | P18; state=Đã đăng; group=N11 Public; author=Chi; anonymous=False; score=0.3 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


<!-- sc:branch SC-M11-018 E16 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E16.1 | SYSTEM | Hệ thống từ chối thao tác gửi bài không đúng trạng thái, không quét hoặc ghi lại kết quả gửi. | P18 Đã đăng, không là yêu cầu lưu sửa chung M03 | END:REJECTED | FR-M03-04.07 |


<!-- sc:branch SC-M11-018 E17 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E17.1 | SYSTEM | Hệ thống từ chối gửi bài nháp/gửi lại theo mức cảnh cáo, không gọi AI hoặc đăng. | P18 chưa gửi lần này; mứcMEDIUM/HEAVY | END:REJECTED | FR-M03-04.10 |


<!-- sc:branch SC-M11-018 E18 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E18.1 | SYSTEM | Hệ thống kiểm tác giả và từ chối gửi bài người khác. | Chi gửi P18 nhưng author=Lan; không thay author | END:REJECTED | FR-M03-04.06 |


<!-- sc:branch SC-M11-018 E19 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E19.1 | ACT-009 | Chi gửi P18 với tiêu đề trống hoặc cả nội dung/poll đều không có. | P18 Nháp củaChi; tên trống hoặc body trống/poll trống; có tệp cũng không đủ | E19.2 | FR-M03-04.08, FR-M03-04.09 |
| E19.2 | SYSTEM | Hệ thống từ chối gửi dữ liệu thiếu, chưa gọi quét/đăng. | P18 chưa gửi; tiêu đề và nội dung hoặc poll cần có | E19.3 | FR-M03-04.08, FR-M03-04.09 |
| E19.3 | ACT-009 | Chi gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Chi; roleNhóm=Member; Nháp→gửi; anonymous=True; duyệt trước=False; AI tổng/Moderation=đều Bật | E19.4 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E19.4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Chi và lựa chọn ẩn danh=True hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=Chi; anonymous=True; attempt=1 | E19.5 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E19.5 | ACT-006 | Dịch vụ AI trả điểm quét và nhóm vi phạm cho P18. | P18 score=0.3; khoảng=thấp; nhóm vi phạm=[] | E19.6 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E19.6 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Public: xem ở trang nhóm, tab Group của thành viên; đủ điều kiện thì Trending/Following theo M14, không Newest. Bài ẩn danh không vào Following nhờ theo dõi tác giả. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Đã đăng; group=N11 Public; author=Chi; anonymous=True; score=0.3 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


<!-- sc:branch SC-M11-018 E20 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E20.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-018 E21 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E21.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-018 E22 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E22.1 | SYSTEM | Hệ thống từ chối hành vi trong nhóm Bị khóa kể cả Owner/Group Mod hoặc ADMIN; quyền đọc/lưu/báo cáo/Member-Group Mod tự rời và tự kế nhiệm theo hợp đồng riêng vẫn giữ. | Nhóm Bị khóa; không thực hiện thay đổi/duyệt/nhận mở queue bị chặn | END:REJECTED | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |


<!-- sc:branch SC-M11-018 E23 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E23.1 | ACT-009 | Chi gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Chi; roleNhóm=Member; Nháp→gửi; anonymous=True; duyệt trước=False; AI tổng/Moderation=đều Bật | E23.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E23.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/tác giả/dữ liệu M03, gắn N11 và giữ Chi/ẩn danh; chuyển đang quét, gửi lần1 tại T. Sau5 giây không có kết quả tính lỗi, đợi2 giây gửi lần2, sau5 giây nữa vẫn không kết quả; công tắc giữ nguyên, không thử thêm. Hệ thống nhận kết quả cổng UC016. Giữ P18 Chờ duyệt (chờ nhóm duyệt), đưa vào hàng chờ riêng N12 hoặc N11 đang xét, không trộn queue báo cáo/Mod hệ thống. Trả đã ghi nhận bài chờ nhóm; chỉ tác giả/người duyệt theo quyền biết trạng thái, người xem thường không thấy, chưa đăng. Giữ nhóm đích và tác giả thật Chi, lựa chọn ẩn danh=True. | P18; state=Chờ duyệt/chờ nhóm duyệt; group=N11 Public; author=Chi; anonymous=True; score=không có sau 2 lỗi; timeline T, T+5s lỗi1, T+7s gọi2, T+12s lỗi2 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E24 — thay toàn bộ M1 đến kết thúc:** Bình có vai trò nhóm Group Mod; biến thể {'preapproval': False}. Actor khởi tạo ACT-010; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E24 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E24.1 | ACT-010 | Bình gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Bình; roleNhóm=Group Mod; Nháp→gửi; anonymous=True; duyệt trước=False; AI tổng/Moderation=đều Bật | E24.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E24.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Bình và lựa chọn ẩn danh=True hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=Bình; anonymous=True; attempt=1 | E24.3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E24.3 | ACT-006 | Dịch vụ AI trả điểm quét và nhóm vi phạm cho P18. | P18 score=0.3; khoảng=thấp; nhóm vi phạm=[] | E24.4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E24.4 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Public: xem ở trang nhóm, tab Group của thành viên; đủ điều kiện thì Trending/Following theo M14, không Newest. Bài ẩn danh không vào Following nhờ theo dõi tác giả. Giữ nhóm đích và tác giả thật Bình, lựa chọn ẩn danh=True. | P18; state=Đã đăng; group=N11 Public; author=Bình; anonymous=True; score=0.3 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


**E25 — thay toàn bộ M1 đến kết thúc:** An có vai trò nhóm Owner; biến thể {'preapproval': False}. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E25 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E25.1 | ACT-011 | An gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=An; roleNhóm=Owner; Nháp→gửi; anonymous=True; duyệt trước=False; AI tổng/Moderation=đều Bật | E25.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E25.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật An và lựa chọn ẩn danh=True hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=An; anonymous=True; attempt=1 | E25.3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E25.3 | ACT-006 | Dịch vụ AI trả điểm quét và nhóm vi phạm cho P18. | P18 score=0.3; khoảng=thấp; nhóm vi phạm=[] | E25.4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E25.4 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Public: xem ở trang nhóm, tab Group của thành viên; đủ điều kiện thì Trending/Following theo M14, không Newest. Bài ẩn danh không vào Following nhờ theo dõi tác giả. Giữ nhóm đích và tác giả thật An, lựa chọn ẩn danh=True. | P18; state=Đã đăng; group=N11 Public; author=An; anonymous=True; score=0.3 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


**E26 — thay toàn bộ M1 đến kết thúc:** An có vai trò nhóm Owner; biến thể {'preapproval': True, 'score': 0.5}. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E26 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E26.1 | ACT-011 | An gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=An; roleNhóm=Owner; Nháp→gửi; anonymous=True; duyệt trước=True; AI tổng/Moderation=đều Bật | E26.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E26.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật An và lựa chọn ẩn danh=True hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=An; anonymous=True; attempt=1 | E26.3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E26.3 | ACT-006 | Dịch vụ AI trả điểm quét và nhóm vi phạm cho P18. | P18 score=0.5; khoảng=trung bình; nhóm vi phạm=[] | E26.4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E26.4 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Giữ P18 Chờ duyệt và đưa vào hàng chờ Mod hệ thống M03 vì tác giả Owner, không vào queue nhóm dù duyệt trước Bật. Trả đã ghi nhận bài chờ đúng hàng; M03 sở hữu việc staff xét tiếp, không giả đã đăng. Giữ nhóm đích và tác giả thật An, lựa chọn ẩn danh=True. | P18; state=Chờ duyệt/Mod hệ thống; group=N11 Public; author=An; anonymous=True; score=0.5 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


**E27 — thay toàn bộ M1 đến kết thúc:** An có vai trò nhóm Owner; biến thể {'preapproval': True, 'score': 0.89}. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E27 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E27.1 | ACT-011 | An gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=An; roleNhóm=Owner; Nháp→gửi; anonymous=True; duyệt trước=True; AI tổng/Moderation=đều Bật | E27.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E27.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật An và lựa chọn ẩn danh=True hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=An; anonymous=True; attempt=1 | E27.3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E27.3 | ACT-006 | Dịch vụ AI trả điểm quét và nhóm vi phạm cho P18. | P18 score=0.89; khoảng=trung bình; nhóm vi phạm=[] | E27.4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E27.4 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Giữ P18 Chờ duyệt và đưa vào hàng chờ Mod hệ thống M03 vì tác giả Owner, không vào queue nhóm dù duyệt trước Bật. Trả đã ghi nhận bài chờ đúng hàng; M03 sở hữu việc staff xét tiếp, không giả đã đăng. Giữ nhóm đích và tác giả thật An, lựa chọn ẩn danh=True. | P18; state=Chờ duyệt/Mod hệ thống; group=N11 Public; author=An; anonymous=True; score=0.89 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


**E28 — thay toàn bộ M1 đến kết thúc:** An có vai trò nhóm Owner; biến thể {'preapproval': True, 'score': 0.9}. Actor khởi tạo ACT-011; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E28 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E28.1 | ACT-011 | An gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=An; roleNhóm=Owner; Nháp→gửi; anonymous=True; duyệt trước=True; AI tổng/Moderation=đều Bật | E28.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E28.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật An và lựa chọn ẩn danh=True hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=An; anonymous=True; attempt=1 | E28.3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E28.3 | ACT-006 | Dịch vụ AI trả điểm quét và nhóm vi phạm cho P18. | P18 score=0.9; khoảng=cao; nhóm vi phạm=[Quấy rối] | E28.4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E28.4 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Chuyển P18→Bị từ chối bởi AI, cung cấp nhóm vi phạm quét trả về cho tác giả qua M03 và sự kiện bài bị từ chối M07; không coi là nhóm từ chối. Tác giả được sửa/gửi lại hoặc khiếu nại M09 (luồng khác), chưa đăng bài. Giữ nhóm đích và tác giả thật An, lựa chọn ẩn danh=True. | P18; state=Bị từ chối/nguồn AI; group=N11 Public; author=An; anonymous=True; score=0.9 | END:REJECTED | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


**E29 — thay toàn bộ M1 đến kết thúc:** An có vai trò nhóm Owner; biến thể {'preapproval': True, 'mode': 'failed'}. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E29 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E29.1 | ACT-011 | An gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=An; roleNhóm=Owner; Nháp→gửi; anonymous=True; duyệt trước=True; AI tổng/Moderation=đều Bật | E29.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E29.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật An và lựa chọn ẩn danh=True hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=An; anonymous=True; attempt=1 | E29.3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E29.3 | ACT-006 | Dịch vụ AI trả lỗi lần thử đầu. | P18 attempt1=error; chưa có điểm; không tự đổi công tắc | E29.4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E29.4 | SYSTEM | Hệ thống ghi nhận lỗi lần đầu, đợi 2 giây rồi gửi lại đúng một lần, không song song và không đổi công tắc. Mỗi lần chấm không có kết quả sau 5 giây cũng tính lỗi. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; attempt=2; cùng bài/tác giả/nhóm; hai công tắc vẫn Bật | E29.5 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E29.5 | ACT-006 | Dịch vụ AI trả lỗi lần thử thứ hai. | P18 attempt2=error; không điểm | E29.6 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E29.6 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Giữ P18 Chờ duyệt và đưa vào hàng chờ Mod hệ thống M03 vì tác giả Owner, không vào queue nhóm dù duyệt trước Bật. Trả đã ghi nhận bài chờ đúng hàng; M03 sở hữu việc staff xét tiếp, không giả đã đăng. Giữ nhóm đích và tác giả thật An, lựa chọn ẩn danh=True. | P18; state=Chờ duyệt/Mod hệ thống; group=N11 Public; author=An; anonymous=True; score=không có sau 2 lỗi | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


**E30 — thay toàn bộ M1 đến kết thúc:** An có vai trò nhóm Owner; biến thể {'preapproval': True, 'mode': 'off'}. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E30 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E30.1 | ACT-011 | An gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=An; roleNhóm=Owner; Nháp→gửi; anonymous=True; duyệt trước=True; AI tổng/Moderation=có một cờ Tắt | E30.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E30.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật An và lựa chọn ẩn danh=True hợp lệ với công tắc. AI tổng hoặc Moderation tắt nên không gọi AI, khác lỗi quét. Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Public: xem ở trang nhóm, tab Group của thành viên; đủ điều kiện thì Trending/Following theo M14, không Newest. Bài ẩn danh không vào Following nhờ theo dõi tác giả. Giữ nhóm đích và tác giả thật An, lựa chọn ẩn danh=True. | P18; state=Đã đăng; group=N11 Public; author=An; anonymous=True; score=không quét | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |


**E31 — thay toàn bộ M1 đến kết thúc:** An có vai trò nhóm Owner; biến thể {'preapproval': True, 'mode': 'retry-ok'}. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E31 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E31.1 | ACT-011 | An gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=An; roleNhóm=Owner; Nháp→gửi; anonymous=True; duyệt trước=True; AI tổng/Moderation=đều Bật | E31.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E31.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật An và lựa chọn ẩn danh=True hợp lệ với công tắc. Đưa P18 vào Chờ duyệt (đang quét), không hiện cho người xem thường; qua lớp nội bộ M13 gửi tiêu đề/nội dung/poll/ảnh hiện có cho dịch vụ AI, chờ điểm và nhóm vi phạm. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; group=N11; author=An; anonymous=True; attempt=1 | E31.3 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E31.3 | ACT-006 | Dịch vụ AI trả lỗi lần thử đầu. | P18 attempt1=error; chưa có điểm; không tự đổi công tắc | E31.4 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E31.4 | SYSTEM | Hệ thống ghi nhận lỗi lần đầu, đợi 2 giây rồi gửi lại đúng một lần, không song song và không đổi công tắc. Mỗi lần chấm không có kết quả sau 5 giây cũng tính lỗi. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; attempt=2; cùng bài/tác giả/nhóm; hai công tắc vẫn Bật | E31.5 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E31.5 | ACT-006 | Dịch vụ AI trả điểm quét sau lần thử thứ hai. | P18 attempt2=ok; score=0.3; nhóm vi phạm=[] | E31.6 | FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08 |
| E31.6 | SYSTEM | Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Public: xem ở trang nhóm, tab Group của thành viên; đủ điều kiện thì Trending/Following theo M14, không Newest. Bài ẩn danh không vào Following nhờ theo dõi tác giả. Giữ nhóm đích và tác giả thật An, lựa chọn ẩn danh=True. | P18; state=Đã đăng; group=N11 Public; author=An; anonymous=True; score=0.3 | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |


**E32 — thay toàn bộ M1 đến kết thúc:** Hòa có vai trò nhóm Member; ADMIN miễn quét/qua cờ, vẫn kiểm membership/Khóa; biến thể {'preapproval': False}. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E32 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E32.1 | ACT-007 | Hòa gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Hòa; roleNhóm=Member; Nháp→gửi; anonymous=True; duyệt trước=False; AI tổng/Moderation=đều Bật; ADMIN; Group=false; vai trò nhóm=Member | E32.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E32.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Hòa và lựa chọn ẩn danh=True hợp lệ với công tắc. Admin không quét. Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Public: xem ở trang nhóm, tab Group của thành viên; đủ điều kiện thì Trending/Following theo M14, không Newest. Bài ẩn danh không vào Following nhờ theo dõi tác giả. Giữ nhóm đích và tác giả thật Hòa, lựa chọn ẩn danh=True. | P18; state=Đã đăng; group=N11 Public; author=Hòa; anonymous=True; score=không quét | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |


**E33 — thay toàn bộ M1 đến kết thúc:** Hòa có vai trò nhóm Member; ADMIN miễn quét/qua cờ, vẫn kiểm membership/Khóa; biến thể {'preapproval': True}. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E33 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E33.1 | ACT-007 | Hòa gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Hòa; roleNhóm=Member; Nháp→gửi; anonymous=True; duyệt trước=True; AI tổng/Moderation=đều Bật; ADMIN; Group=false; vai trò nhóm=Member | E33.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E33.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Hòa và lựa chọn ẩn danh=True hợp lệ với công tắc. Admin không quét. Hệ thống nhận kết quả cổng UC016. Giữ P18 Chờ duyệt (chờ nhóm duyệt), đưa vào hàng chờ riêng N12 hoặc N11 đang xét, không trộn queue báo cáo/Mod hệ thống. Trả đã ghi nhận bài chờ nhóm; chỉ tác giả/người duyệt theo quyền biết trạng thái, người xem thường không thấy, chưa đăng. Giữ nhóm đích và tác giả thật Hòa, lựa chọn ẩn danh=True. | P18; state=Chờ duyệt/chờ nhóm duyệt; group=N11 Public; author=Hòa; anonymous=True; score=không quét | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |


**E34 — thay toàn bộ M1 đến kết thúc:** Hòa có vai trò nhóm Owner; ADMIN miễn quét/qua cờ, vẫn kiểm membership/Khóa; biến thể {'preapproval': False}. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E34 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E34.1 | ACT-007 | Hòa gửi bài nháp P18 đã soạn qua M03 vào N11. | P18; title=Cùng giải phương trình bậc hai; body=Mình chia sẻ cách tính biệt thức và kiểm tra nghiệm.; Lớp=11; không poll/tệp; không có trường bắt buộc khác do M11 đặt; author=Hòa; roleNhóm=Owner; Nháp→gửi; anonymous=True; duyệt trước=False; AI tổng/Moderation=đều Bật; ADMIN; Group=false; vai trò nhóm=Owner | E34.2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10 |
| E34.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm thành viên/nhóm không Khóa, người gửi đúng tác giả, bài Nháp hoặc Bị từ chối, tiêu đề/nội dung và mức cảnh cáo theo M03. Gắn tối đa một nhóm N11, giữ tác giả thật Hòa và lựa chọn ẩn danh=True hợp lệ với công tắc. Admin không quét. Hệ thống nhận kết quả cổng UC016. Chuyển P18→Đã đăng, trả kết quả đăng; cung cấp sự kiện bài được đăng M03/M07 và mốc tạo embedding M13 theo cờ của owner. Public: xem ở trang nhóm, tab Group của thành viên; đủ điều kiện thì Trending/Following theo M14, không Newest. Bài ẩn danh không vào Following nhờ theo dõi tác giả. Giữ nhóm đích và tác giả thật Hòa, lựa chọn ẩn danh=True. | P18; state=Đã đăng; group=N11 Public; author=Hòa; anonymous=True; score=không quét | END:SUCCESS | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |


**E35 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E35 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E35.1 | ACT-001 | Guest yêu cầu: Gửi bài mới hoặc gửi lại bài bị từ chối vào nhóm. | Đúng nhóm/đích của chức năng; Guest không có vai trò nhóm bắt buộc; Group=true | E35.2 | FR-M11-12.11, BR-M11-06 |
| E35.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-12.11, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E36 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E36 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E36.1 | ACT-002 | Phúc người ngoài yêu cầu: Gửi bài mới hoặc gửi lại bài bị từ chối vào nhóm. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E36.2 | FR-M11-12.11, BR-M11-06 |
| E36.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-12.11, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E37 — thay toàn bộ M1 đến kết thúc:** Minh MODERATOR không thành viên yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E37 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E37.1 | ACT-008 | Minh MODERATOR không thành viên yêu cầu: Gửi bài mới hoặc gửi lại bài bị từ chối vào nhóm. | Đúng nhóm/đích của chức năng; Minh MODERATOR không thành viên không có vai trò nhóm bắt buộc; Group=true | E37.2 | FR-M11-12.11, BR-M11-06 |
| E37.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-12.11, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E38 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN không thành viên yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-018 E38 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E38.1 | ACT-007 | Hòa ADMIN không thành viên yêu cầu: Gửi bài mới hoặc gửi lại bài bị từ chối vào nhóm. | Đúng nhóm/đích của chức năng; Hòa ADMIN không thành viên không có vai trò nhóm bắt buộc; Group=true | E38.2 | FR-M11-12.11, BR-M11-06 |
| E38.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-12.11, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-018 -->

<a id="sc-m11-019"></a>

<!-- sc:scenario SC-M11-019 -->

### SC-M11-019

#### 1. Tên kịch bản chuẩn

Tra cứu hàng chờ duyệt riêng của một nhóm — BF-M11-019; owner [UC-M11-017](../../us/US-M11.md#uc-m11-017); nhóm UC chính: UC-M11-034.

#### 2. Actor thực hiện

ACT-010 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có N11, Bình Group Mod; P19 của Chi chờ nhóm duyệt, P20 của Bình cũng chờ nhóm, P21 của Owner nằm queue Mod hệ thống, P22 thuộc nhóm khác. Không giả quyền giữ chỉ vì có quyền đọc queue.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-019 -->

| result | condition |
|---|---|
| SUCCESS | Trả đúng tập bài chờ nhóm duyệt được phép xem, tách queue báo cáo/hệ thống; không tự nhận hoặc duyệt bài. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-019 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-010 | Bình mở hàng chờ duyệt N11. | Bình Group Mod N11; không tự nhận P19/P20 | M2 | FR-M11-13.01 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod đúng nhóm/không Khóa, UC021 pha xem không cần giữ và không cấm nhìn bài mình. Trả P19/P20 đang chờ nhóm duyệt riêng N11, thông tin nội dung/tác giả thật cho Group Mod; không P21 queue Mod hệ thống/P22 nhóm khác/vụ báo cáo. Chỉ xem chưa nhận hoặc kết luận. | queueN11={P19 Chi,P20 Bình}; holder không đổi; P21/P22 không thuộc tập | END:SUCCESS | FR-M11-13.01, FR-M11-13.08, FR-M11-13.09, BR-M11-17, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-019 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Queue nhóm hiện không có bài nào chờ | E1.1 | FR-M11-13.01, BR-M11-20, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E2 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E2.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E3 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E3.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E4 | system | M2 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | E4.1 | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |
| E5 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M11-13.01, FR-M11-17.03, FR-M10-12.08, FR-M11-13.08, FR-M11-13.09, BR-M11-17, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E6 | system | M1 | ACT-009 — Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E7 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E8 | system | M1 | ACT-008 — Minh MODERATOR không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E9 | system | M1 | ACT-007 — Hòa ADMIN không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E10 | system | M1 | ACT-011 — An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M11-13.01, FR-M11-13.08, FR-M11-13.09, BR-M11-17, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-019 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod và UC021 pha xem, trả hàng chờ rỗng đúng nhóm; không lấy bài từ queue khác để bù. | N11 groupQueue=[]; không có holder/trạng thái mới | END:SUCCESS | FR-M11-13.01, BR-M11-20, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-019 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-019 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-019 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối hành vi trong nhóm Bị khóa kể cả Owner/Group Mod hoặc ADMIN; quyền đọc/lưu/báo cáo/Member-Group Mod tự rời và tự kế nhiệm theo hợp đồng riêng vẫn giữ. | Nhóm Bị khóa; không thực hiện thay đổi/duyệt/nhận mở queue bị chặn | END:REJECTED | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |


**E5 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-019 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-007 | Hòa mở hàng chờ duyệt N11. | Hòa Group Mod N11; không tự nhận P19/P20; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E5.2 | FR-M11-13.01, FR-M11-17.03, FR-M10-12.08 |
| E5.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod đúng nhóm/không Khóa, UC021 pha xem không cần giữ và không cấm nhìn bài mình. Trả P19/P20 đang chờ nhóm duyệt riêng N11, thông tin nội dung/tác giả thật cho Group Mod; không P21 queue Mod hệ thống/P22 nhóm khác/vụ báo cáo. Chỉ xem chưa nhận hoặc kết luận. | queueN11={P19 Chi,P20 Hòa}; holder không đổi; P21/P22 không thuộc tập | END:SUCCESS | FR-M11-13.01, FR-M11-13.08, FR-M11-13.09, BR-M11-17, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


**E6 — thay toàn bộ M1 đến kết thúc:** Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-019 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-009 | Chi Member yêu cầu: Tra cứu hàng chờ duyệt riêng của một nhóm. | Đúng nhóm/đích của chức năng; Chi Member không có vai trò nhóm bắt buộc; Group=true | E6.2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33 |
| E6.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E7 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-019 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-002 | Phúc người ngoài yêu cầu: Tra cứu hàng chờ duyệt riêng của một nhóm. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E7.2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33 |
| E7.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E8 — thay toàn bộ M1 đến kết thúc:** Minh MODERATOR không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-019 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-008 | Minh MODERATOR không Group Mod yêu cầu: Tra cứu hàng chờ duyệt riêng của một nhóm. | Đúng nhóm/đích của chức năng; Minh MODERATOR không Group Mod không có vai trò nhóm bắt buộc; Group=true | E8.2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33 |
| E8.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E9 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-019 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-007 | Hòa ADMIN không Group Mod yêu cầu: Tra cứu hàng chờ duyệt riêng của một nhóm. | Đúng nhóm/đích của chức năng; Hòa ADMIN không Group Mod không có vai trò nhóm bắt buộc; Group=true | E9.2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33 |
| E9.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E10 — thay toàn bộ M1 đến kết thúc:** An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-019 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-011 | An mở hàng chờ duyệt N11. | An Owner; P19 Chi/P20 Bình chờ nhóm; P21 củaAn chờMod hệ thống | E10.2 | FR-M11-13.01 |
| E10.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner và UC021 pha xem, trả P19/P20 đúng queue nhóm với tác giả thật. P21 của An nằm queue Mod hệ thống nên không có ở đây. Chưa nhận/kết luận bài. | queueN11={P19 Chi Member,P20 Bình Group Mod}; P21 không thuộc queue nhóm | END:SUCCESS | FR-M11-13.01, FR-M11-13.08, FR-M11-13.09, BR-M11-17, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-019 -->

<a id="sc-m11-020"></a>

<!-- sc:scenario SC-M11-020 -->

### SC-M11-020

#### 1. Tên kịch bản chuẩn

Nhận giữ một bài chờ nhóm duyệt để xử lý — BF-M11-020; owner [UC-M11-018](../../us/US-M11.md#uc-m11-018); nhóm UC chính: UC-M11-034.

#### 2. Actor thực hiện

ACT-010 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có N11/P19 của Chi Chờ duyệt (chờ nhóm duyệt); quyền và holder kiểm khi nhận. Chuẩn Bình Group Mod, P19 chưa ai giữ, tác giả Chi khác Bình.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-020 -->

| result | condition |
|---|---|
| SUCCESS | Đúng người được ghi holder với mốc không thao tác; bài vẫn Chờ duyệt. Actor nhận xác nhận nhận giữ độc quyền để xử lý, mục tiêu nhận hoàn tất; kết luận là chức năng SC021. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-020 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-010 | Bình chọn nhận P19 trong hàng chờ N11. | Bình Group Mod; P19/Chi; holder=trống; T | M2 | FR-M11-13.02 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. UC021 pha nhận: kiểm bài đúng queue, không tự nhận bài mình, chưa người khác giữ; ghi Bình là holder P19 và mốc thao tác cuối=T. Trả đã nhận giữ; người khác không kết luận được. Không biến nhận bài thành chấp nhận. Nếu không thao tác đủ 30 phút sẽ tự nhả; chỉ lượt người giữ mở xem/chấp nhận/từ chối cập nhật mốc theo nguồn. | P19 vẫn Chờ duyệt; holder=U-B; lastActionAt=10:00+07; không thao tác thêm thì 10:30 tự nhả | END:SUCCESS | FR-M11-13.02, FR-M11-13.03, FR-M11-13.04, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-020 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | P19 đang được Dũng giữ, chưa đủ 30 phút không thao tác | E1.1 | FR-M11-13.02, FR-M11-13.03, FR-M11-13.04, BR-M11-20 |
| E2 | system | M1 | Bình muốn nhận chính P20 của mình | E2.1 | FR-M11-13.13, BR-M11-39 |
| E3 | system | M2 | P19 không còn ở hàng chờ nhóm N11 | E3.1 | FR-M11-13.01, FR-M11-13.02, BR-M11-20, BR-M11-33 |
| E4 | system | M2 | Holder cũ đã tự nhả đủ 30 phút trước yêu cầu nhận của Bình | E4.1 | FR-M11-13.02, FR-M11-13.03, FR-M11-13.04, FR-M11-13.13, BR-M11-20, BR-M11-39, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E5 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E5.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E6 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E6.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E7 | system | M2 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | E7.1 | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |
| E8 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M11-13.02, FR-M11-17.03, FR-M10-12.08, FR-M11-13.03, FR-M11-13.04, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E9 | system | M1 | ACT-009 — Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E10 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E11 | system | M1 | ACT-008 — Minh MODERATOR không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E11.1 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E12 | system | M1 | ACT-007 — Hòa ADMIN không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E12.1 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E13 | system | M1 | ACT-011 — An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E13.1 | FR-M11-13.02, FR-M11-13.03, FR-M11-13.04, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-020 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống không cho nhận đè P19, giữ holder Dũng và mốc thao tác cuối của người giữ. | P19 holder Dũng; lastAction09:50; T10:00; không chuyển cho Bình | END:REJECTED | FR-M11-13.02, FR-M11-13.03, FR-M11-13.04, BR-M11-20 |


<!-- sc:branch SC-M11-020 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-010 | Bình chọn nhận P20 của mình. | P20 authorBình; N11; chưa holder; Group ModBình | E2.2 | FR-M11-13.13 |
| E2.2 | SYSTEM | Hệ thống từ chối Group Mod tự nhận bài mình; Owner hoặc Group Mod khác có thể nhận theo quyền. Không ẩn P20 khỏi việc xem queue chỉ vì cấm nhận. | P20 vẫn Chờ duyệt, holder trống; Bình không được nhận | END:REJECTED | FR-M11-13.13, BR-M11-39 |


<!-- sc:branch SC-M11-020 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống kiểm bài/queue và không nhận một bài không còn chờ đúng nhóm; không đưa bài quay lại queue. | P19 đã Đã đăng hoặc thuộc queue Mod hệ thống/nhóm khác; không holder mới | END:REJECTED | FR-M11-13.01, FR-M11-13.02, BR-M11-20, BR-M11-33 |


<!-- sc:branch SC-M11-020 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. UC021 kiểm P19 đúng queue, tác giả khác Bình và holder đã trống do AUT003 lúc09:40+30 phút=10:10. Tại T2=10:11, ghi Bình giữ P19, lastAction=T2, trả đã nhận; không chiếm người đang giữ. | Dũng lastAction09:40→nhả10:10; Bình nhận10:11; P19 Chờ duyệt/holder Bình | END:SUCCESS | FR-M11-13.02, FR-M11-13.03, FR-M11-13.04, FR-M11-13.13, BR-M11-20, BR-M11-39, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-020 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-020 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-020 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối hành vi trong nhóm Bị khóa kể cả Owner/Group Mod hoặc ADMIN; quyền đọc/lưu/báo cáo/Member-Group Mod tự rời và tự kế nhiệm theo hợp đồng riêng vẫn giữ. | Nhóm Bị khóa; không thực hiện thay đổi/duyệt/nhận mở queue bị chặn | END:REJECTED | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |


**E8 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-020 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-007 | Hòa chọn nhận P19 trong hàng chờ N11. | Hòa Group Mod; P19/Chi; holder=trống; T; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E8.2 | FR-M11-13.02, FR-M11-17.03, FR-M10-12.08 |
| E8.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. UC021 pha nhận: kiểm bài đúng queue, không tự nhận bài mình, chưa người khác giữ; ghi Hòa là holder P19 và mốc thao tác cuối=T. Trả đã nhận giữ; người khác không kết luận được. Không biến nhận bài thành chấp nhận. Nếu không thao tác đủ 30 phút sẽ tự nhả; chỉ lượt người giữ mở xem/chấp nhận/từ chối cập nhật mốc theo nguồn. | P19 vẫn Chờ duyệt; holder=U-H; lastActionAt=10:00+07; không thao tác thêm thì 10:30 tự nhả | END:SUCCESS | FR-M11-13.02, FR-M11-13.03, FR-M11-13.04, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


**E9 — thay toàn bộ M1 đến kết thúc:** Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-020 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-009 | Chi Member yêu cầu: Nhận giữ một bài chờ nhóm duyệt để xử lý. | Đúng nhóm/đích của chức năng; Chi Member không có vai trò nhóm bắt buộc; Group=true | E9.2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33 |
| E9.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E10 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-020 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-002 | Phúc người ngoài yêu cầu: Nhận giữ một bài chờ nhóm duyệt để xử lý. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E10.2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33 |
| E10.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E11 — thay toàn bộ M1 đến kết thúc:** Minh MODERATOR không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-020 E11 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E11.1 | ACT-008 | Minh MODERATOR không Group Mod yêu cầu: Nhận giữ một bài chờ nhóm duyệt để xử lý. | Đúng nhóm/đích của chức năng; Minh MODERATOR không Group Mod không có vai trò nhóm bắt buộc; Group=true | E11.2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33 |
| E11.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E12 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-020 E12 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E12.1 | ACT-007 | Hòa ADMIN không Group Mod yêu cầu: Nhận giữ một bài chờ nhóm duyệt để xử lý. | Đúng nhóm/đích của chức năng; Hòa ADMIN không Group Mod không có vai trò nhóm bắt buộc; Group=true | E12.2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33 |
| E12.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E13 — thay toàn bộ M1 đến kết thúc:** An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-020 E13 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E13.1 | ACT-011 | An chọn nhận P19 trong hàng chờ N11. | An Owner; P19/Chi; holder=trống; T; An Owner; nếu có holder của bài đang xét thì holder=An, tác giả vẫn Chi | E13.2 | FR-M11-13.02 |
| E13.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. UC021 pha nhận: kiểm bài đúng queue, không tự nhận bài mình, chưa người khác giữ; ghi An là holder P19 và mốc thao tác cuối=T. Trả đã nhận giữ; người khác không kết luận được. Không biến nhận bài thành chấp nhận. Nếu không thao tác đủ 30 phút sẽ tự nhả; chỉ lượt người giữ mở xem/chấp nhận/từ chối cập nhật mốc theo nguồn. | P19 vẫn Chờ duyệt; holder=U-A; lastActionAt=10:00+07; không thao tác thêm thì 10:30 tự nhả | END:SUCCESS | FR-M11-13.02, FR-M11-13.03, FR-M11-13.04, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-020 -->

<a id="sc-m11-021"></a>

<!-- sc:scenario SC-M11-021 -->

### SC-M11-021

#### 1. Tên kịch bản chuẩn

Kết luận một bài đang chờ nhóm duyệt — BF-M11-021; owner [UC-M11-019](../../us/US-M11.md#uc-m11-019); nhóm UC chính: UC-M11-034.

#### 2. Actor thực hiện

ACT-010 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có N11/P19 của Chi Chờ duyệt (chờ nhóm duyệt), Bình Group Mod đang giữ; giữ bài không bị giấu như điều kiện luôn đúng: kiểm lại trong luồng. Chuẩn lần nhận 09:40, Bình mở xem09:50 nên mốc cuối09:50; T=10:00 chưa đủ 30 phút, duyệt trước không ảnh hưởng quyền kết luận.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-021 -->

| result | condition |
|---|---|
| SUCCESS | Một quyết định hợp lệ được lưu và trả: Chấp nhận→Đã đăng có sự kiện/mốc embedding; Từ chối có lý do→Bị từ chối kèm lý do có sự kiện M03/M07, không khiếu nại cấp nhóm, tác giả được sửa/gửi lại. Không lấy từ chối bài hợp lệ của người duyệt làm REJECTED của chính chức năng kết luận. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-021 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-010 | Bình chọn Chấp nhận P19 đang giữ. | P19 của Chi; Bình holder; lastAction09:50; T10:00; Chấp nhận | M2 | FR-M11-13.05 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. UC021 pha kết luận: kiểm Bình còn Group Mod, P19 đang chờ đúng nhóm và Bình đúng holder, không tự duyệt. Chuyển P19→Đã đăng/ra khỏi tập chờ nhóm, cập nhật mốc thao tác cuối theo nguồn. Trả đã chấp nhận, cung cấp sự kiện bài được đăng M03/M07 và mốc embedding M13; Public theo phạm vi/ẩn danh của bài, không mặc định ra Newest. | P19 Chờ duyệt→Đã đăng; tác giả Chi; anonymous=true; group N11; không đổi quyết định kiểm duyệt hệ thống | END:SUCCESS | FR-M11-13.03, FR-M11-13.05, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, FR-M11-12.12, FR-M11-12.13, BR-M11-17, BR-M11-18, BR-M11-20, BR-M11-33, BR-M11-39, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-021 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Bình chọn Từ chối bài kèm lý do | E1.1 | FR-M11-13.06, FR-M11-13.03, FR-M11-13.07, FR-M11-13.10, FR-M11-13.11, BR-M11-20, BR-M11-21, BR-M11-38, BR-M11-39, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E2 | system | M1 | Bình chọn Từ chối thiếu lý do rồi bổ sung | E2.1 | FR-M11-13.10, BR-M11-38, FR-M11-13.06, FR-M11-13.03, FR-M11-13.07, FR-M11-13.11, BR-M11-20, BR-M11-21, BR-M11-39, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E3 | system | M2 | Bình khác holder Dũng hoặc bài đã tự nhả trước lúc xử lý | E3.1 | FR-M11-13.03, FR-M11-13.04, BR-M11-20 |
| E4 | system | M2 | Bình đã bị giáng Group Mod trước khi gửi quyết định | E4.1 | FR-M11-13.08, BR-M11-06, BR-M11-20 |
| E5 | system | M1 | Bình Group Mod cố chấp nhận hoặc từ chối P20 của mình | E5.1 | FR-M11-13.13, BR-M11-39 |
| E6 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E6.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E7 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E7.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E8 | system | M2 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | E8.1 | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |
| E9 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M11-13.05, FR-M11-17.03, FR-M10-12.08, FR-M11-13.03, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, FR-M11-12.12, FR-M11-12.13, BR-M11-17, BR-M11-18, BR-M11-20, BR-M11-33, BR-M11-39, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E10 | system | M1 | ACT-009 — Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E11 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E11.1 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E12 | system | M1 | ACT-008 — Minh MODERATOR không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E12.1 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E13 | system | M1 | ACT-007 — Hòa ADMIN không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E13.1 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E14 | system | M1 | ACT-011 — An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E14.1 | FR-M11-13.05, FR-M11-13.03, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, FR-M11-12.12, FR-M11-12.13, BR-M11-17, BR-M11-18, BR-M11-20, BR-M11-33, BR-M11-39, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-021 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-010 | Bình chọn Từ chối P19 và nhập lý do Lạc đề. | P19 chờN11; holder Bình; reason=Lạc đề | E1.2 | FR-M11-13.06 |
| E1.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. UC021 kiểm đúng Group Mod/holder/không tự duyệt, P19 còn chờ; kiểm lý do có nội dung rồi lưu “Lạc đề”, chuyển P19→Bị từ chối, ra khỏi tập chờ. Cung cấp sự kiện bài bị từ chối M03/M07 và trả kết quả từ chối có lý do. Đây là quyết định cấp nhóm không khiếu nại, tác giả sửa/gửi lại qua SC018 được, cổng chạy lại. | P19 Bị từ chối; reason=Lạc đề; actor/holder Bình; author Chi; nguồn nhóm; không phảiAI | END:SUCCESS | FR-M11-13.03, FR-M11-13.06, FR-M11-13.07, FR-M11-13.10, FR-M11-13.11, BR-M11-20, BR-M11-21, BR-M11-38, BR-M11-39, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-021 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-010 | Bình chọn Từ chối P19, không nhập lý do. | reason=trống; holder Bình; P19 Chờ duyệt | E2.2 | FR-M11-13.10 |
| E2.2 | SYSTEM | Hệ thống từ chối thao tác vì thiếu lý do, chưa chuyển P19 sang Bị từ chối. | P19 vẫn chờ; không tự sinh lý do | E2.3 | FR-M11-13.10, BR-M11-38 |
| E2.3 | ACT-010 | Bình nhập Lạc đề và gửi lại quyết định Từ chối. | P19 còn chờ; Bình vẫn holder/còn quyền; reason=Lạc đề | E2.4 | FR-M11-13.06 |
| E2.4 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. UC021 kiểm đúng Group Mod/holder/không tự duyệt, P19 còn chờ; kiểm lý do có nội dung rồi lưu “Lạc đề”, chuyển P19→Bị từ chối, ra khỏi tập chờ. Cung cấp sự kiện bài bị từ chối M03/M07 và trả kết quả từ chối có lý do. Đây là quyết định cấp nhóm không khiếu nại, tác giả sửa/gửi lại qua SC018 được, cổng chạy lại. | P19 Bị từ chối; reason=Lạc đề; actor/holder Bình; author Chi; nguồn nhóm; không phảiAI | END:SUCCESS | FR-M11-13.03, FR-M11-13.06, FR-M11-13.07, FR-M11-13.10, FR-M11-13.11, BR-M11-20, BR-M11-21, BR-M11-38, BR-M11-39, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-021 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối kết luận vì người thao tác không đúng người giữ hiện tại. Không nhận đè hoặc tự gia hạn từ lần mở của người khác. | P19 holder Dũng hoặc trống; Bình không là holder; quyết định không được ghi | END:REJECTED | FR-M11-13.03, FR-M11-13.04, BR-M11-20 |


<!-- sc:branch SC-M11-021 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống kiểm quyền hiện tại và từ chối dù hồ sơ cũ vẫn ghi Bình giữ; không tự nhả ngay chỉ vì mất vai trò (GAP006), quy tắc30 phút vẫn theo nguồn. | Bình hiện Member; P19 Chờ duyệt; không quyết định hợp lệ mới | END:REJECTED | FR-M11-13.08, BR-M11-06, BR-M11-20 |


<!-- sc:branch SC-M11-021 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-010 | Bình gửi quyết định cho P20 của mình. | P20 authorBình; Group ModBình; dù dữ liệu giữ được gửi lên cũng không đủ | E5.2 | FR-M11-13.13 |
| E5.2 | SYSTEM | Hệ thống từ chối Group Mod tự chấp nhận/từ chối bài mình; không ghi kết luận. | P20 vẫn chờ; phải Owner/Group Mod khác xử lý đúng quyền giữ | END:REJECTED | FR-M11-13.13, BR-M11-39 |


<!-- sc:branch SC-M11-021 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-021 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-021 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống từ chối hành vi trong nhóm Bị khóa kể cả Owner/Group Mod hoặc ADMIN; quyền đọc/lưu/báo cáo/Member-Group Mod tự rời và tự kế nhiệm theo hợp đồng riêng vẫn giữ. | Nhóm Bị khóa; không thực hiện thay đổi/duyệt/nhận mở queue bị chặn | END:REJECTED | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |


**E9 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-021 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-007 | Hòa chọn Chấp nhận P19 đang giữ. | P19 của Chi; Hòa holder; lastAction09:50; T10:00; Chấp nhận; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E9.2 | FR-M11-13.05, FR-M11-17.03, FR-M10-12.08 |
| E9.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. UC021 pha kết luận: kiểm Hòa còn Group Mod, P19 đang chờ đúng nhóm và Hòa đúng holder, không tự duyệt. Chuyển P19→Đã đăng/ra khỏi tập chờ nhóm, cập nhật mốc thao tác cuối theo nguồn. Trả đã chấp nhận, cung cấp sự kiện bài được đăng M03/M07 và mốc embedding M13; Public theo phạm vi/ẩn danh của bài, không mặc định ra Newest. | P19 Chờ duyệt→Đã đăng; tác giả Chi; anonymous=true; group N11; không đổi quyết định kiểm duyệt hệ thống | END:SUCCESS | FR-M11-13.03, FR-M11-13.05, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, FR-M11-12.12, FR-M11-12.13, BR-M11-17, BR-M11-18, BR-M11-20, BR-M11-33, BR-M11-39, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


**E10 — thay toàn bộ M1 đến kết thúc:** Chi Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-021 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-009 | Chi Member yêu cầu: Kết luận một bài đang chờ nhóm duyệt. | Đúng nhóm/đích của chức năng; Chi Member không có vai trò nhóm bắt buộc; Group=true | E10.2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33 |
| E10.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E11 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-021 E11 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E11.1 | ACT-002 | Phúc người ngoài yêu cầu: Kết luận một bài đang chờ nhóm duyệt. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E11.2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33 |
| E11.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E12 — thay toàn bộ M1 đến kết thúc:** Minh MODERATOR không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-021 E12 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E12.1 | ACT-008 | Minh MODERATOR không Group Mod yêu cầu: Kết luận một bài đang chờ nhóm duyệt. | Đúng nhóm/đích của chức năng; Minh MODERATOR không Group Mod không có vai trò nhóm bắt buộc; Group=true | E12.2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33 |
| E12.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E13 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-021 E13 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E13.1 | ACT-007 | Hòa ADMIN không Group Mod yêu cầu: Kết luận một bài đang chờ nhóm duyệt. | Đúng nhóm/đích của chức năng; Hòa ADMIN không Group Mod không có vai trò nhóm bắt buộc; Group=true | E13.2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33 |
| E13.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E14 — thay toàn bộ M1 đến kết thúc:** An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-021 E14 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E14.1 | ACT-011 | An chọn Chấp nhận P19 đang giữ. | P19 của Chi; An holder; lastAction09:50; T10:00; Chấp nhận; An Owner; nếu có holder của bài đang xét thì holder=An, tác giả vẫn Chi | E14.2 | FR-M11-13.05 |
| E14.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. UC021 pha kết luận: kiểm An còn Owner, P19 đang chờ đúng nhóm và An đúng holder, không tự duyệt. Chuyển P19→Đã đăng/ra khỏi tập chờ nhóm, cập nhật mốc thao tác cuối theo nguồn. Trả đã chấp nhận, cung cấp sự kiện bài được đăng M03/M07 và mốc embedding M13; Public theo phạm vi/ẩn danh của bài, không mặc định ra Newest. | P19 Chờ duyệt→Đã đăng; tác giả Chi; anonymous=true; group N11; không đổi quyết định kiểm duyệt hệ thống | END:SUCCESS | FR-M11-13.03, FR-M11-13.05, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, FR-M11-12.12, FR-M11-12.13, BR-M11-17, BR-M11-18, BR-M11-20, BR-M11-33, BR-M11-39, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-021 -->

<a id="sc-m11-022"></a>

<!-- sc:scenario SC-M11-022 -->

### SC-M11-022

#### 1. Tên kịch bản chuẩn

Gỡ một bài hoặc bình luận khỏi nhóm theo quyền nhóm — BF-M11-022; owner [UC-M11-020](../../us/US-M11.md#uc-m11-020); nhóm UC chính: UC-M11-034.

#### 2. Actor thực hiện

ACT-010 là actor chính của đường chuẩn. Actor kế thừa vẫn chịu guard của nhóm đích. Đường E tại M1 ghi đầy đủ từ yêu cầu đầu khi người khởi tạo khác; SYSTEM là iShare, không thêm actor module/queue/DB/clock.

#### 3. Tiền điều kiện

Có N11/P11 Đã đăng của Chi Member, ẩn danh, Chi20 điểm từ P11; Bình Group Mod không phải tác giả. Không cần nhận bài queue để gỡ. Quyền/nhóm/thứ bậc kiểm khi xử lý; gỡ chính nội dung mình chưa rõ GAP003.

#### 4. Hậu điều kiện

<!-- sc:post SC-M11-022 -->

| result | condition |
|---|---|
| SUCCESS | Nội dung mang dấu gỡ xóa mềm, bài giữ trạng thái đăng và dữ liệu/điểm; tập xem thu hẹp đúng lớp quyền, tác giả nhận thông báo, không tự hiện lại/khiếu nại cấp nhóm. Actor nhận kết quả gỡ. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo điều kiện nguồn; không có thay đổi thành công của yêu cầu bị chặn. Hiệu ứng hợp lệ đã có trước đó được giữ, không tự rollback/cấp quyền/khôi phục hoặc ghi nhận thành công giả. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M11-022 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-010 | Bình chọn gỡ P11 của Chi khỏi N11. | P11 Đã đăng, chưa mang dấu gỡ; author=U-C Member; actor=U-B Group Mod; không nhập lý do bắt buộc do nguồn không đặt | M2 | FR-M11-14.01 |
| M2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod đúng nhóm/không Khóa và tác giả thấp hơn, đặt dấu Bị gỡ khỏi nhóm/xóa mềm; giữ dữ liệu và trạng thái đăng Đã đăng của P11. Tập xem bị giới hạn thêm: tác giả, Owner/Group Mod của nhóm, Mod/Admin theo quyền ngữ cảnh; dấu gỡ không cấp quyền mở Private hoặc nhóm Ẩn/Xóa. Thông báo ứng dụng cho Chi, không trừ20 điểm. Trả đã gỡ, tác giả không tự hiện lại/khiếu nại cấp nhóm; báo cáo/can thiệp M08 vẫn áp dụng. | P11 state Đã đăng→Đã đăng; removedFromGroup=false→true; author Chi; 20→20; recipient U-C; dữ liệu giữ | END:SUCCESS | FR-M11-14.01, FR-M11-14.02, FR-M11-14.03, FR-M11-14.04, FR-M11-14.05, FR-M11-14.06, FR-M11-14.07, FR-M11-14.08, BR-M11-05, BR-M11-06, BR-M11-21, BR-M11-22, BR-M11-30, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M12-02.16, FR-M15-02.27, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


#### 6. Các ngoại lệ

E thay đúng bước at. Guard thay dữ liệu của lần chạy từ đầu, không cộng các trạng thái loại trừ. Đổi nhóm/đích/lựa chọn từ đầu có đường thay M1; trạng thái đổi trong lúc thao tác được nêu rõ. E tại M1 thay toàn bộ M1 đến kết thúc khi actor khởi tạo khác. Mỗi đường đi đến kết quả hoặc điểm nhập lại cụ thể; các trường hợp thiếu hợp đồng chỉ ghi GAP, không tự dựng nhánh cho/chặn hoặc chuyển giao để cắt mục tiêu.

<!-- sc:exceptions SC-M11-022 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Bình chọn gỡ bình luận C11 của Chi thay vì bài P11 | E1.1 | FR-M11-14.01, FR-M11-14.03, FR-M11-14.04, FR-M11-14.05, FR-M11-14.06, FR-M11-14.07, FR-M11-14.08, BR-M11-05, BR-M11-21, BR-M11-22, BR-M11-30, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M12-02.16, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E2 | system | M1 | Bình Group Mod gỡ nội dung của An Owner | E2.1 | FR-M11-14.08, BR-M11-05 |
| E3 | system | M1 | Bình Group Mod gỡ nội dung của Dũng Group Mod | E3.1 | FR-M11-14.08, BR-M11-05 |
| E4 | system | M2 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | E4.1 | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |
| E5 | system | M2 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | E5.1 | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |
| E6 | system | M2 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | E6.1 | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |
| E7 | system | M1 | ACT-011 — An Owner gỡ bài của Bình Group Mod thấp hơn. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M11-14.01, FR-M11-14.03, FR-M11-14.04, FR-M11-14.05, FR-M11-14.06, FR-M11-14.07, BR-M11-05, BR-M11-30, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E8 | system | M1 | ACT-007 — Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M11-14.01, FR-M11-17.03, FR-M10-12.08, FR-M11-14.02, FR-M11-14.03, FR-M11-14.04, FR-M11-14.05, FR-M11-14.06, FR-M11-14.07, FR-M11-14.08, BR-M11-05, BR-M11-06, BR-M11-21, BR-M11-22, BR-M11-30, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M12-02.16, FR-M15-02.27, FR-M11-17.01, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E9 | system | M1 | ACT-009 — Lan Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M11-14.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E10 | system | M1 | ACT-002 — Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M11-14.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E11 | system | M1 | ACT-008 — Minh MODERATOR không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E11.1 | FR-M11-14.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E12 | system | M1 | ACT-007 — Hòa ADMIN không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E12.1 | FR-M11-14.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| E13 | system | M1 | ACT-011 — An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E13.1 | FR-M11-14.01, FR-M11-14.02, FR-M11-14.03, FR-M11-14.04, FR-M11-14.05, FR-M11-14.06, FR-M11-14.07, FR-M11-14.08, BR-M11-05, BR-M11-06, BR-M11-21, BR-M11-22, BR-M11-30, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M12-02.16, FR-M15-02.27, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-022 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-010 | Bình chọn gỡ C11 khỏi N11. | C11 củaChi Member; thuộcP11/N11; chưa gỡ; actorBình Group Mod | E1.2 | FR-M11-14.01 |
| E1.2 | SYSTEM | Hệ thống kiểm cờ/trạng thái, Group Mod Bình và tác giả Chi Member thấp hơn; đặt dấu Bị gỡ khỏi nhóm trên C11/xóa mềm, giữ dữ liệu. Chỉ tập tác giả/Owner/Group Mod/Mod/Admin theo các lớp quyền còn xem, báo ứng dụng cho Chi, không trừ điểm 20; không cho tự hiện lại/khiếu nại cấp nhóm. Trả đã gỡ bình luận, không gán trạng thái đăng của bài lên bình luận hoặc gỡ bài cha P11. | C11.removedFromGroup=true; P11 giữ nguyên; dữ liệu/điểm 20 giữ; recipient Chi | END:SUCCESS | FR-M11-14.01, FR-M11-14.03, FR-M11-14.04, FR-M11-14.05, FR-M11-14.06, FR-M11-14.07, FR-M11-14.08, BR-M11-05, BR-M11-21, BR-M11-22, BR-M11-30, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M12-02.16, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:branch SC-M11-022 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-010 | Bình yêu cầu gỡ P-other của An Owner. | N11; targetP-other; author ngang/cao hơnBình | E2.2 | FR-M11-14.08 |
| E2.2 | SYSTEM | Hệ thống từ chối gỡ nội dung Owner hoặc Group Mod khác bằng vai trò Group Mod; không đặt dấu gỡ mới. | P-other trạng thái/dấu/điểm giữ | END:REJECTED | FR-M11-14.08, BR-M11-05 |


<!-- sc:branch SC-M11-022 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-010 | Bình yêu cầu gỡ P-other của Dũng Group Mod. | N11; targetP-other; author ngang/cao hơnBình | E3.2 | FR-M11-14.08 |
| E3.2 | SYSTEM | Hệ thống từ chối gỡ nội dung Owner hoặc Group Mod khác bằng vai trò Group Mod; không đặt dấu gỡ mới. | P-other trạng thái/dấu/điểm giữ | END:REJECTED | FR-M11-14.08, BR-M11-05 |


<!-- sc:branch SC-M11-022 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối với “Hệ thống đang bận, vui lòng thử lại sau”; giữ lối vào/dữ liệu và các việc tự làm/kiểm duyệt M08. Bật lại không làm bù lệnh này; muốn làm cần yêu cầu mới hợp lệ. | Group=false; người yêu cầu không ADMIN; không thực hiện chức năng của lần bị chặn | END:REJECTED | FR-M11-17.01, FR-M11-17.02, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-29, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07 |


<!-- sc:branch SC-M11-022 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống không hiển thị nhóm/nội dung và không thực hiện hành vi trên nhóm không còn được mở; giữ dữ liệu theo xóa mềm/ẩn, không tự khôi phục. | Nhóm Đã xóa hoặc Bị ẩn; không nội dung được trả, dữ liệu giữ | END:REJECTED | FR-M11-15.01, FR-M11-15.02, FR-M11-15.05, FR-M11-16.01, FR-M11-16.02, BR-M11-23, BR-M11-27 |


<!-- sc:branch SC-M11-022 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối hành vi trong nhóm Bị khóa kể cả Owner/Group Mod hoặc ADMIN; quyền đọc/lưu/báo cáo/Member-Group Mod tự rời và tự kế nhiệm theo hợp đồng riêng vẫn giữ. | Nhóm Bị khóa; không thực hiện thay đổi/duyệt/nhận mở queue bị chặn | END:REJECTED | FR-M11-16.04, FR-M11-16.07, BR-M11-28 |


**E7 — thay toàn bộ M1 đến kết thúc:** An Owner gỡ bài của Bình Group Mod thấp hơn. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-022 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-011 | An chọn gỡ P-B của Bình khỏi N11. | OwnerAn; Group ModBình là tác giả; P-B Đã đăng; chưa gỡ | E7.2 | FR-M11-14.01 |
| E7.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner/không Khóa/thứ bậc, đặt dấu gỡ xóa mềm P-B, giữ trạng thái Đã đăng/dữ liệu/điểm. Thu hẹp tập xem theo lớp quyền, báo ứng dụng cho Bình. Không khiếu nại/hiện lại cấp nhóm; trả đã gỡ. | P-B.removed=true; stateĐã đăng; recipient Bình; dữ liệu/điểm giữ | END:SUCCESS | FR-M11-14.01, FR-M11-14.03, FR-M11-14.04, FR-M11-14.05, FR-M11-14.06, FR-M11-14.07, BR-M11-05, BR-M11-30, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E8 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN qua cờ Group Tắt, có đúng Group Mod; vẫn chịu Khóa/Private/hạn/quyền đích. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-022 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-007 | Hòa chọn gỡ P11 của Chi khỏi N11. | P11 Đã đăng, chưa mang dấu gỡ; author=U-C Member; actor=U-H Group Mod; không nhập lý do bắt buộc do nguồn không đặt; Hòa ADMIN hệ thống, Group=false; đúng vai trò nhóm cần cho chức năng như đường chuẩn, các điều kiện khác giữ | E8.2 | FR-M11-14.01, FR-M11-17.03, FR-M10-12.08 |
| E8.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Group Mod đúng nhóm/không Khóa và tác giả thấp hơn, đặt dấu Bị gỡ khỏi nhóm/xóa mềm; giữ dữ liệu và trạng thái đăng Đã đăng của P11. Tập xem bị giới hạn thêm: tác giả, Owner/Group Mod của nhóm, Mod/Admin theo quyền ngữ cảnh; dấu gỡ không cấp quyền mở Private hoặc nhóm Ẩn/Xóa. Thông báo ứng dụng cho Chi, không trừ20 điểm. Trả đã gỡ, tác giả không tự hiện lại/khiếu nại cấp nhóm; báo cáo/can thiệp M08 vẫn áp dụng. | P11 state Đã đăng→Đã đăng; removedFromGroup=false→true; author Chi; 20→20; recipient U-C; dữ liệu giữ | END:SUCCESS | FR-M11-14.01, FR-M11-14.02, FR-M11-14.03, FR-M11-14.04, FR-M11-14.05, FR-M11-14.06, FR-M11-14.07, FR-M11-14.08, BR-M11-05, BR-M11-06, BR-M11-21, BR-M11-22, BR-M11-30, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M12-02.16, FR-M15-02.27, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.08 |


**E9 — thay toàn bộ M1 đến kết thúc:** Lan Member yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-009; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-022 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-009 | Lan Member yêu cầu: Gỡ một bài hoặc bình luận khỏi nhóm theo quyền nhóm. | Đúng nhóm/đích của chức năng; Lan Member không có vai trò nhóm bắt buộc; Group=true | E9.2 | FR-M11-14.02, BR-M11-06 |
| E9.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-14.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E10 — thay toàn bộ M1 đến kết thúc:** Phúc người ngoài yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-022 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-002 | Phúc người ngoài yêu cầu: Gỡ một bài hoặc bình luận khỏi nhóm theo quyền nhóm. | Đúng nhóm/đích của chức năng; Phúc người ngoài không có vai trò nhóm bắt buộc; Group=true | E10.2 | FR-M11-14.02, BR-M11-06 |
| E10.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-14.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E11 — thay toàn bộ M1 đến kết thúc:** Minh MODERATOR không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-022 E11 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E11.1 | ACT-008 | Minh MODERATOR không Group Mod yêu cầu: Gỡ một bài hoặc bình luận khỏi nhóm theo quyền nhóm. | Đúng nhóm/đích của chức năng; Minh MODERATOR không Group Mod không có vai trò nhóm bắt buộc; Group=true | E11.2 | FR-M11-14.02, BR-M11-06 |
| E11.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-14.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E12 — thay toàn bộ M1 đến kết thúc:** Hòa ADMIN không Group Mod yêu cầu chức năng bằng quyền nhóm không có. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-022 E12 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E12.1 | ACT-007 | Hòa ADMIN không Group Mod yêu cầu: Gỡ một bài hoặc bình luận khỏi nhóm theo quyền nhóm. | Đúng nhóm/đích của chức năng; Hòa ADMIN không Group Mod không có vai trò nhóm bắt buộc; Group=true | E12.2 | FR-M11-14.02, BR-M11-06 |
| E12.2 | SYSTEM | Hệ thống kiểm quyền nhóm đúng hành vi và từ chối; quyền hệ thống không cấp membership/Owner/Group Mod. Không thực hiện thay đổi hoặc tiết lộ dữ liệu quản trị theo yêu cầu này. | Không có kết quả chức năng hợp lệ mới; dữ liệu trước giữ | END:REJECTED | FR-M11-14.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


**E13 — thay toàn bộ M1 đến kết thúc:** An Owner thực hiện chức năng kiểm duyệt/quản lý nhóm, vẫn đúng đích và holder khi cần. Actor khởi tạo ACT-011; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M11-022 E13 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E13.1 | ACT-011 | An chọn gỡ P11 của Chi khỏi N11. | P11 Đã đăng, chưa mang dấu gỡ; author=U-C Member; actor=U-A Owner; không nhập lý do bắt buộc do nguồn không đặt; An Owner; nếu có holder của bài đang xét thì holder=An, tác giả vẫn Chi | E13.2 | FR-M11-14.01 |
| E13.2 | SYSTEM | Hệ thống kiểm cờ Group cho phép (nếu Tắt chỉ ADMIN qua rào cờ), nhóm Hoạt động/không Bị ẩn, điều kiện Khóa và quyền hiện tại đúng hành vi. Kiểm Owner đúng nhóm/không Khóa và tác giả thấp hơn, đặt dấu Bị gỡ khỏi nhóm/xóa mềm; giữ dữ liệu và trạng thái đăng Đã đăng của P11. Tập xem bị giới hạn thêm: tác giả, Owner/Group Mod của nhóm, Mod/Admin theo quyền ngữ cảnh; dấu gỡ không cấp quyền mở Private hoặc nhóm Ẩn/Xóa. Thông báo ứng dụng cho Chi, không trừ20 điểm. Trả đã gỡ, tác giả không tự hiện lại/khiếu nại cấp nhóm; báo cáo/can thiệp M08 vẫn áp dụng. | P11 state Đã đăng→Đã đăng; removedFromGroup=false→true; author Chi; 20→20; recipient U-C; dữ liệu giữ | END:SUCCESS | FR-M11-14.01, FR-M11-14.02, FR-M11-14.03, FR-M11-14.04, FR-M11-14.05, FR-M11-14.06, FR-M11-14.07, FR-M11-14.08, BR-M11-05, BR-M11-06, BR-M11-21, BR-M11-22, BR-M11-30, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M12-02.16, FR-M15-02.27, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |


<!-- sc:end SC-M11-022 -->

## 5. Hành vi nền và quy tắc áp dụng

| ID nguồn | Trigger/điều kiện | Hiệu ứng/đường tiếp nối và giới hạn | sources |
|---|---|---|---|
| AUT-M11-001 | Owner lưu cấu hình làm Public không câu hỏi, yêu cầu R1/R2 còn Chờ duyệt | SC002 nhánh nhận ngay: mọi yêu cầu đang chờ→Đã chấp nhận, joinAt=T, thông báo từng người gửi; không tác động bài P-wait. Chỉ sửa câu hỏi hoặc tắt duyệt trước không kích hoạt. | FR-M11-02.14, BR-M11-07, BR-M11-32, BR-M11-37 |
| AUT-M11-002 | Owner bị ban tạm/vĩnh viễn, vô hiệu hóa kể cả tự làm, hoặc xóa tài khoản từ M01/M08 | Tự chuyển ngay, không actor giả/SC riêng. N11: Bình bổ nhiệm01/09 sớm hơn Dũng bổ nhiệm lại20/10→Bình Owner; không cộng lần cũ của Dũng. Không Group Mod: Lan vào01/07 sớm hơn Chi01/08→Lan Owner. Chỉ Owner: dùng xóa mềm UC022, nhóm Đã xóa, mọi nội dung không hiện, dữ liệu/điểm giữ. Owner cũ ở lại Member kể cả hoạt động lại; không lấy lại quyền. Thông báo người kế nhiệm. Chạy khi Group Tắt/Bị khóa. Không tự đặt tie-break hoặc lọc ACTIVE (GAP001). | FR-M11-11.01, FR-M11-11.02, FR-M11-11.03, FR-M11-11.04, FR-M11-11.05, FR-M11-11.06, FR-M11-11.07, FR-M11-16.10, FR-M11-15.01, FR-M11-15.02, FR-M11-15.03, FR-M11-01.06, BR-M11-04, BR-M11-23, BR-M11-26, BR-M11-28, BR-M11-29, BR-M11-37, FR-M01-10.01, FR-M01-12.01, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |
| AUT-M11-003 | Người giữ không thao tác trên bài đủ 30 phút từ mốc cuối | P19: Bình nhận09:40, mở xem09:50→nhả10:20 nếu không thêm thao tác. Dũng chỉ mở10:00 không gia hạn cho Bình. Nhả holder về trống/queue nhóm, không chấp nhận/từ chối/xóa; người đủ quyền nhận lại qua SC020. Không tự nút nhả tay hoặc nhả ngay lúc mất role (GAP006). | FR-M11-13.02, FR-M11-13.03, FR-M11-13.04, BR-M11-20 |
| AUT-M11-004 | M09 đã chấp nhận khiếu nại bài nhóm bị AI tự từ chối | Không BF chỉ SYSTEM: chưa sửa/gửi lại thì không quét lại, coi điểm<0.5: không Owner+duyệt trước Bật→chờ nhóm; duyệt trước Tắt hoặc Owner→Đã đăng và phát sự kiện/mốc embedding. Nếu đã sửa/gửi lại trước kết luận, giữ trạng thái hiện tại, không gọi lại cổng để ghi đè. Không áp quyết định nhóm từ chối/gỡ. Hoàn/đảo cảnh cáo do M09, quyền đọc khi xét Private và trạng thái chuyển tiếp GAP006/008. | FR-M11-13.12, FR-M11-13.14, BR-M11-21, BR-M11-38, FR-M09-08.18, BR-M03-46, FR-M13-03.01 |
| AUT-M11-005 | Sự kiện nhóm hoặc bài vừa hoàn tất đúng nguồn | Mời→người được mời +link; yêu cầu mới→Owner/các Group Mod; chấp nhận yêu cầu→người gửi; bổ nhiệm→người được bổ nhiệm; kick→người bị kick; kế nhiệm chỉ định/tự động→Owner mới; gỡ→tác giả. Bài đăng/từ chối dùng sự kiện M03/M07, Đã đăng giao mốc embedding M13; không hứa tạo embedding xong khi cờ/lỗi của M13. Không báo khi vào ngay Public, từ chối yêu cầu, giáng. Không email hoặc lời mời chấp nhận riêng; thông báo Private vẫn lọc quyền, preview mời chỉ tên/mô tả/link. Thứ tự/lỗi phát GAP007. Thông báo bài mới cho người theo dõi tác giả theo M07 chỉ ở lần công khai đầu đủ điều kiện, không gửi cho bài ẩn danh hoặc người không có quyền xem. | FR-M11-05.02, FR-M11-06.04, FR-M11-06.07, FR-M11-06.08, FR-M11-06.09, FR-M11-08.03, FR-M11-08.06, FR-M11-09.06, FR-M11-10.07, FR-M11-11.07, FR-M11-14.06, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, BR-M07-01, FR-M13-03.01, FR-M07-02.22, BR-M07-23 |
| AUT-M11-006 | M08 có quyết định Khóa/Ẩn/mở khóa nhóm hợp lệ | M11 chỉ áp kết quả: Khóa giữ Public/Private và đọc cũ, chặn đúng danh sách RULE006; Ẩn không hiện với ai kể cả Owner, dữ liệu giữ, không bỏ ẩn. Mở khóa trả điều kiện như trước, vẫn kiểm quyền/cờ/Private; nhóm Khóa vẫn có thể bị ẩn ở vụ sau. Xét vụ/ban/khóa/ẩn/mở khóa do M08, không BF mới trong M11. | FR-M11-16.01, FR-M11-16.02, FR-M11-16.03, FR-M11-16.04, FR-M11-16.05, FR-M11-16.06, FR-M11-16.07, FR-M11-16.08, FR-M11-16.09, FR-M11-16.10, BR-M11-27, BR-M11-28, FR-M08-18.02, FR-M08-18.05, FR-M08-18.06 |
| RULE-M11-001 | Quyền nhóm và tạo nhóm | Mỗi nhóm có một Owner; thứ bậc Owner > Group Mod > Member độc lập ADMIN/MODERATOR/USER hệ thống. Chỉ Owner sửa thông tin/cài đặt, xóa nhóm, bổ nhiệm/giáng Group Mod và kick Group Mod. Owner/Group Mod xét yêu cầu, quản lý chặn, duyệt/gỡ nội dung và kick Member. Tạo cần đăng nhập, tối đa 5 nhóm trong 24 giờ lăn, gồm nhóm đã xóa và cả Admin; đúng 24 giờ trước không còn tính. Không giới hạn tổng sở hữu/tham gia, không leaderboard/reputation riêng hoặc follow nhóm. Bổ nhiệm lại tính thâm niên từ lần mới; không tác động người ngang/cao hơn. | FR-M11-01.01, FR-M11-01.02, FR-M11-01.03, FR-M11-01.04, FR-M11-01.05, FR-M11-01.06, FR-M11-01.07, FR-M11-01.08, FR-M11-01.09, FR-M11-01.10, FR-M11-01.11, FR-M11-01.12, FR-M11-08.01, FR-M11-08.02, FR-M11-08.03, FR-M11-08.04, FR-M11-08.05, FR-M11-08.06, BR-M11-02, BR-M11-03, BR-M11-04, BR-M11-05, BR-M11-06, BR-M11-26, BR-M11-31, BR-M11-33 |
| RULE-M11-002 | Các lớp xem và quyền tương tác | Public mọi người đọc, Guest chưa được tương tác; người ngoài đã đăng nhập bình luận/vote/báo cáo/bookmark như thường qua owner M04/M12/M08/M02, không được tạo bài nhóm nếu chưa thành viên. Private thành viên mới đọc/tương tác; Mod/Admin ngoài nhóm chỉ xem nội dung ở vụ đang giữ M08, ngoại lệ Owner chờ Mod hệ thống theo M03. Quyền thấy tác giả thật không cấp quyền mở Private; Owner/Group Mod/Mod/Admin thấy thật nếu được đọc, người khác thấy Ẩn danh. Nhóm/bài Ẩn/Xóa và nội dung chờ/gỡ còn lớp lọc riêng. Danh sách nhóm Public+Private đã tham gia mới nhất trước, đủ tên/mô tả/chế độ; thành viên theo quyền trang, preview lời mời chỉ tên/mô tả. Public→Private: bản đang hiện chỉ đọc, bình luận/vote/báo cáo từ người ngoài bị chặn; tải lại/link/bookmark/thông báo báo Nội dung không tồn tại, tải feed/tìm sau lọc quyền mới. | FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06, FR-M11-03.07, FR-M11-03.08, FR-M11-03.09, FR-M11-03.10, FR-M11-03.11, FR-M11-03.12, FR-M11-03.13, FR-M11-03.14, FR-M11-03.15, FR-M11-03.16, FR-M11-03.17, FR-M11-03.18, FR-M11-02.02, FR-M11-02.03, FR-M11-02.04, FR-M11-02.12, FR-M11-02.13, FR-M11-14.01, BR-M11-11, BR-M11-12, BR-M11-13, BR-M11-14, BR-M11-15, BR-M11-17, BR-M11-30, BR-M11-33, BR-M11-34, BR-M11-35, FR-M02-01.07, FR-M02-01.17, FR-M02-07.03, FR-M06-01.13, FR-M06-02.08, FR-M06-02.09, FR-M06-03.08, FR-M08-01.11, FR-M12-01.11, FR-M03-06.01, FR-M03-07.02 |
| RULE-M11-003 | Tham gia/yêu cầu/mời/chặn | Public không câu hỏi vào ngay và không thông báo; Public có câu hỏi hoặc Private gửi Chờ duyệt, có câu hỏi bắt buộc trả lời, tối đa một câu hỏi. Người gửi rút của mình→Đã rút. Không trùng Chờ duyệt, sau từ chối gửi mới ngay không hạn lần/cooldown. Chặn mọi cách vào, chặn chuyển yêu cầu Chờ duyệt→Đã từ chối; bỏ chặn chỉ mở cổng lại, không khôi phục yêu cầu/membership. Mọi thành viên mời, link chung không hạn/thu hồi/tạo lại, mời cụ thể chỉ thông báo kèm link, người được mời vẫn đi cổng. Xem danh sách chặn là mục tiêu đọc độc lập, không thay dữ liệu. | FR-M11-04.01, FR-M11-04.02, FR-M11-04.03, FR-M11-04.04, FR-M11-04.05, FR-M11-04.06, FR-M11-04.07, FR-M11-04.08, FR-M11-04.09, FR-M11-04.10, FR-M11-05.01, FR-M11-05.02, FR-M11-05.03, FR-M11-05.04, FR-M11-05.05, FR-M11-05.06, FR-M11-05.07, FR-M11-06.01, FR-M11-06.02, FR-M11-06.03, FR-M11-06.04, FR-M11-06.05, FR-M11-06.06, FR-M11-06.07, FR-M11-06.08, FR-M11-06.09, FR-M11-07.01, FR-M11-07.02, FR-M11-07.03, FR-M11-07.04, FR-M11-07.05, BR-M11-03, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-32, BR-M11-36, BR-M11-37 |
| RULE-M11-004 | Gửi bài/cổng nhóm/duyệt bài | Một bài M03 thuộc tối đa một nhóm. Ẩn danh chỉ trong nhóm: bật thì chọn từng bài, tắt chỉ chặn lựa chọn cho bài mới và giữ bài cũ. Không Owner, AI bật: điểm ≥0.9 tự từ chối; 0.5≤điểm<0.9 chờ nhóm; điểm<0.5 theo công tắc duyệt trước. AI tắt chủ đích hoặc Admin không Owner không quét, theo duyệt trước. Lỗi sau một lần thử lại bắt buộc chờ nhóm. Owner bỏ qua queue nhóm: vẫn quét; điểm ≥0.9 từ chối; điểm trung bình hoặc lỗi vào queue Mod hệ thống; sạch hoặc AI tắt đăng ngay. Owner là ADMIN không quét, đăng ngay. Sau M09 chấp nhận AI từ chối không quét lại; đã gửi lại thì không ghi đè. Group Mod không tự nhận/duyệt, vẫn được thấy bài mình trong queue. Từ chối bài cần lý do, tác giả sửa/gửi lại đi cổng thêm lần nữa, không khiếu nại cấp nhóm. Public được phân phối Trending/Following theo M14, không Newest; ẩn danh không vào Following nhờ theo dõi tác giả. Private không ra feed chính kể cả với thành viên, vẫn có trang nhóm/tab Group. | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M11-02.05, FR-M11-02.06, FR-M11-02.15, FR-M11-13.01, FR-M11-13.02, FR-M11-13.03, FR-M11-13.04, FR-M11-13.05, FR-M11-13.06, FR-M11-13.07, FR-M11-13.08, FR-M11-13.09, FR-M11-13.10, FR-M11-13.11, FR-M11-13.12, FR-M11-13.13, FR-M11-13.14, BR-M11-20, BR-M11-21, BR-M11-22, BR-M11-38, BR-M11-39, FR-M03-04.05, FR-M13-02.11, FR-M14-04.07, FR-M14-04.09, FR-M14-04.13, FR-M14-05.01, FR-M05-05.11 |
| RULE-M11-005 | Rời/kick/gỡ/xóa và hệ quả nội dung/điểm | Rời/kick giữ nội dung, tác giả, lựa chọn ẩn danh và điểm. Public còn cho sửa/xóa nội dung mình theo M03/M04; Private không cho sau rời. Kick không tự chặn, được quay lại theo cổng. Owner tự rời còn người khác phải chọn/xác nhận kế nhiệm, chuyển quyền trước rồi đưa người cũ ra. Owner cuối được cảnh báo và chỉ xóa khi xác nhận, khác kế nhiệm tự động. Gỡ là dấu xóa mềm, bài giữ trạng thái đăng, chỉ tập tác giả/Owner/Group Mod/Mod/Admin theo lớp quyền còn xem; không trừ điểm, có thông báo, không tự hiện lại/khiếu nại cấp nhóm. Xóa nhóm làm mọi nội dung không hiện với ai nhưng giữ dữ liệu/điểm, không tự khôi phục hoặc xóa cứng. Không suy chính sách điểm của việc tác giả tự xóa từ chính sách gỡ nhóm. | FR-M11-09.05, FR-M11-09.07, FR-M11-10.01, FR-M11-10.02, FR-M11-10.08, FR-M11-10.09, BR-M11-24, FR-M12-02.15, FR-M11-15.01, FR-M11-15.02, FR-M11-15.03, FR-M11-15.05, BR-M11-23, FR-M12-02.14, FR-M11-10.03, FR-M11-10.04, FR-M11-10.05, FR-M11-10.06, FR-M11-10.07, FR-M11-14.01, FR-M11-14.02, FR-M11-14.03, FR-M11-14.04, FR-M11-14.05, FR-M11-14.06, FR-M11-14.07, FR-M11-14.08, BR-M11-25, BR-M11-26, BR-M11-30, FR-M12-02.16, FR-M15-02.27 |
| RULE-M11-006 | Nhóm Khóa/Ẩn/Xóa và cờ Group | Khóa chặn với tất cả, kể cả ADMIN/Owner/Group Mod: đăng bài, bình luận, vote, poll, tham gia, mời; duyệt yêu cầu/bài, nhận/mở queue, gỡ, kick, chặn/bỏ chặn, bổ nhiệm/giáng, sửa thông tin/cài đặt, xóa nhóm, Owner rời. Vẫn đọc theo Public/Private, bookmark, báo cáo, Member/Group Mod tự rời và tự kế nhiệm. Rút yêu cầu và chỉ xem danh sách chặn khi Khóa chưa chốt (GAP004). Cờ Tắt chặn mở nhóm/bài/tương tác/thao tác khác của người không ADMIN với đúng thông báo bận; danh sách/lối vào vẫn hiện theo quyền. Giữ dữ liệu, việc tự làm và kiểm duyệt M08; bật lại không bù thao tác bị chặn. ADMIN chỉ miễn cờ, vẫn chịu quyền nhóm, Private, Khóa và hạn tạo, không tự có vai trò nhóm. | FR-M11-16.01, FR-M11-16.02, FR-M11-16.03, FR-M11-16.04, FR-M11-16.05, FR-M11-16.06, FR-M11-16.07, FR-M11-16.08, FR-M11-16.09, FR-M11-16.10, FR-M11-17.01, FR-M11-17.02, FR-M11-17.03, FR-M11-17.04, FR-M11-17.05, FR-M11-17.06, FR-M11-17.07, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M10-12.08 |


Không có scenario phụ chỉ SYSTEM hoặc chỉ SYSTEM–AI. Tự động không có actor khởi tạo được giữ ở đây, có dữ liệu/điểm nguồn và điểm nối caller; phần chưa chốt nằm tại GAP.

## 6. Truy vết và ma trận quyết định

| Mã hiệu lực | SC/bước/nhánh hoặc AUT/RULE | Mức đối soát |
|---|---|---|
| FR-M11-01 | SC-M11-001/M1; SC-M11-001/M2; SC-M11-001/E2.3; SC-M11-001/E3.3; SC-M11-001/E4.3; SC-M11-001/E5.1; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E10.1; SC-M11-001/E10.2; RULE-M11-001; SC-M11-001/E1.1; SC-M11-001/E8.2; SC-M11-001/E9.2; SC-M11-003/M2; SC-M11-003/E4.2; SC-M11-017/E4.4; AUT-M11-002; SC-M11-001/E2.1; SC-M11-001/E2.2; SC-M11-001/E3.1; SC-M11-001/E3.2; SC-M11-001/E4.1; SC-M11-001/E4.2; SC-M11-001/E8.1; SC-M11-001/E9.1 | Đã đối soát phần đủ căn cứ |
| FR-M11-02 | SC-M11-002/M1; SC-M11-002/M2; SC-M11-002/M3; SC-M11-002/M4; SC-M11-002/E6.3; SC-M11-002/E7.3; SC-M11-002/E8.3; SC-M11-002/E13.1; SC-M11-002/E13.2; SC-M11-002/E13.3; SC-M11-002/E13.4; SC-M11-002/E1.1; SC-M11-002/E2.1; RULE-M11-002; SC-M11-002/E14.1; SC-M11-002/E14.2; SC-M11-002/E15.1; SC-M11-002/E15.2; SC-M11-002/E16.1; SC-M11-002/E16.2; SC-M11-002/E17.1; SC-M11-002/E17.2; SC-M11-002/E4.1; SC-M11-002/E4.2; RULE-M11-004; SC-M11-002/E5.1; SC-M11-002/E5.2; SC-M11-018/E15.2; SC-M11-002/E3.1; SC-M11-002/E3.2; SC-M11-002/E6.1; SC-M11-002/E6.2; SC-M11-002/E7.1; SC-M11-002/E7.2; SC-M11-002/E8.1; SC-M11-002/E8.2; SC-M11-005/E3.1; SC-M11-002/E1.2; SC-M11-002/E2.2; AUT-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-03 | SC-M11-004/M1; SC-M11-004/M2; SC-M11-004/E1.1; SC-M11-004/E2.1; SC-M11-004/E3.2; RULE-M11-002; SC-M11-004/E3.1; SC-M11-005/M1; SC-M11-005/M2; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E12.1; SC-M11-005/E12.2; SC-M11-005/E15.1; SC-M11-005/E15.2; SC-M11-005/E16.1; SC-M11-005/E16.2; SC-M11-005/E7.1; SC-M11-005/E8.1; SC-M11-005/E9.1; SC-M11-005/E1.2; SC-M11-005/E2.1; SC-M11-005/E11.2; SC-M11-005/E14.2; SC-M11-005/E10.2; SC-M11-005/E13.2; SC-M11-005/E11.1; SC-M11-005/E14.1; SC-M11-005/E10.1; SC-M11-005/E13.1; SC-M11-005/E1.1; SC-M11-006/M1; SC-M11-006/M2; SC-M11-006/E3.1; SC-M11-006/E3.2; SC-M11-006/E4.1; SC-M11-006/E4.2; SC-M11-006/E5.1; SC-M11-006/E5.2; SC-M11-006/E6.1; SC-M11-006/E6.2; SC-M11-006/E7.1; SC-M11-006/E7.2; SC-M11-014/M2; SC-M11-014/E6.2; SC-M11-015/M2; SC-M11-015/E6.2; SC-M11-016/M2; SC-M11-016/E3.2; SC-M11-016/E11.2; SC-M11-017/M2; SC-M11-017/E3.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-04 | SC-M11-005/E1.2; SC-M11-007/E13.1; SC-M11-007/E13.2; RULE-M11-003; SC-M11-007/M1; SC-M11-007/M2; SC-M11-007/E9.2; SC-M11-007/E14.1; SC-M11-007/E14.2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E6.1; SC-M11-007/E6.2; SC-M11-007/E7.1; SC-M11-007/E7.2; SC-M11-007/E8.1; SC-M11-007/E8.2; SC-M11-011/M2; SC-M11-011/E5.2; SC-M11-011/E9.2; SC-M11-007/E9.1; SC-M11-007/E5.1; SC-M11-007/E4.3; SC-M11-007/E4.4; SC-M11-010/E1.2; SC-M11-008/M1; SC-M11-008/M2; SC-M11-008/E1.1; SC-M11-008/E2.1; SC-M11-008/E2.2; SC-M11-008/E5.1; SC-M11-008/E5.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-05 | SC-M11-001/M2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E10.2; SC-M11-009/M2; SC-M11-009/E1.1; SC-M11-009/E1.2; SC-M11-009/E2.2; SC-M11-009/E6.2; RULE-M11-003; SC-M11-007/M1; SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.2; SC-M11-007/E14.1; SC-M11-007/E14.2; SC-M11-009/M1; SC-M11-009/E6.1; AUT-M11-005; SC-M11-009/E2.1; SC-M11-009/E7.1; SC-M11-009/E7.2; SC-M11-009/E8.1; SC-M11-009/E8.2; SC-M11-009/E9.1; SC-M11-009/E9.2; SC-M11-009/E10.1; SC-M11-009/E10.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-06 | SC-M11-002/E1.2; SC-M11-002/E2.2; SC-M11-010/M3; SC-M11-010/M4; SC-M11-010/E7.3; SC-M11-010/E7.4; SC-M11-010/E12.3; SC-M11-010/E12.4; RULE-M11-003; AUT-M11-005; SC-M11-007/M2; SC-M11-007/E9.2; SC-M11-007/E14.2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-010/M1; SC-M11-010/M2; SC-M11-010/E7.1; SC-M11-010/E7.2; SC-M11-010/E12.1; SC-M11-010/E12.2; SC-M11-010/E8.1; SC-M11-010/E8.2; SC-M11-010/E9.1; SC-M11-010/E9.2; SC-M11-010/E10.1; SC-M11-010/E10.2; SC-M11-010/E11.1; SC-M11-010/E11.2; SC-M11-010/E1.2; SC-M11-010/E2.1; SC-M11-010/E1.1; SC-M11-011/M2; SC-M11-011/E5.2; SC-M11-011/E9.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-07 | SC-M11-011/M1; SC-M11-011/M2; SC-M11-011/E1.1; SC-M11-011/E5.1; SC-M11-011/E5.2; SC-M11-011/E9.1; SC-M11-011/E9.2; RULE-M11-003; SC-M11-011/E6.1; SC-M11-011/E6.2; SC-M11-011/E7.1; SC-M11-011/E7.2; SC-M11-011/E8.1; SC-M11-011/E8.2; SC-M11-012/M2; SC-M11-012/E1.1; SC-M11-012/E4.2; SC-M11-012/E5.1; SC-M11-012/E5.2; SC-M11-012/E6.1; SC-M11-012/E6.2; SC-M11-012/E7.2; SC-M11-013/M2; SC-M11-013/E4.2; SC-M11-013/E5.1; SC-M11-013/E5.2; SC-M11-013/E6.1; SC-M11-013/E6.2; SC-M11-013/E7.2; SC-M11-012/M1; SC-M11-012/E4.1; SC-M11-012/E7.1; SC-M11-013/M1; SC-M11-013/E4.1; SC-M11-013/E7.1; SC-M11-013/M3; SC-M11-013/M4; SC-M11-013/E4.3; SC-M11-013/E4.4; SC-M11-013/E7.3; SC-M11-013/E7.4 | Đã đối soát phần đủ căn cứ |
| FR-M11-08 | SC-M11-014/M1; SC-M11-014/M3; SC-M11-014/M4; SC-M11-014/E1.1; SC-M11-014/E6.1; SC-M11-014/E6.3; SC-M11-014/E6.4; SC-M11-015/E1.1; RULE-M11-001; SC-M11-014/M2; SC-M11-014/E6.2; SC-M11-015/M2; SC-M11-015/E6.2; SC-M11-016/M2; SC-M11-016/E3.2; SC-M11-016/E11.2; SC-M11-017/M2; SC-M11-017/E3.2; AUT-M11-005; SC-M11-015/M1; SC-M11-015/M3; SC-M11-015/M4; SC-M11-015/E6.1; SC-M11-015/E6.3; SC-M11-015/E6.4; SC-M11-014/E7.1; SC-M11-014/E7.2; SC-M11-014/E8.1; SC-M11-014/E8.2; SC-M11-014/E9.1; SC-M11-014/E9.2; SC-M11-014/E10.1; SC-M11-014/E10.2; SC-M11-015/E7.1; SC-M11-015/E7.2; SC-M11-015/E8.1; SC-M11-015/E8.2; SC-M11-015/E9.1; SC-M11-015/E9.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-09 | SC-M11-007/E9.1; SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E3.4; SC-M11-016/E8.2; SC-M11-016/E11.4; RULE-M11-005; SC-M11-016/M1; SC-M11-016/M3; SC-M11-016/E1.1; SC-M11-016/E2.1; SC-M11-016/E3.1; SC-M11-016/E3.3; SC-M11-016/E11.1; SC-M11-016/E11.3; AUT-M11-005; SC-M11-016/E9.1; SC-M11-016/E9.2; SC-M11-016/E10.1; SC-M11-016/E10.2; SC-M11-016/E8.1; SC-M11-016/E12.1; SC-M11-016/E12.2; SC-M11-016/E13.1; SC-M11-016/E13.2; SC-M11-016/E14.1; SC-M11-016/E14.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-10 | SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E8.2; SC-M11-016/E11.4; SC-M11-017/M4; SC-M11-017/E7.2; SC-M11-017/E8.2; SC-M11-017/E10.2; RULE-M11-005; SC-M11-016/E3.4; SC-M11-017/E9.2; SC-M11-017/M1; SC-M11-017/M2; SC-M11-017/E3.1; SC-M11-017/E3.2; SC-M11-017/M3; AUT-M11-005; SC-M11-017/E3.3; SC-M11-017/E3.4; SC-M11-017/E4.1; SC-M11-017/E4.2; SC-M11-017/E4.3; SC-M11-017/E4.4; SC-M11-017/E5.1; SC-M11-017/E5.2; SC-M11-017/E5.3; SC-M11-017/E5.4; SC-M11-017/E8.1; SC-M11-017/E9.1; SC-M11-017/E10.1 | Đã đối soát phần đủ căn cứ |
| FR-M11-11 | SC-M11-014/M4; SC-M11-014/E6.4; SC-M11-015/M4; SC-M11-015/E6.4; AUT-M11-002; AUT-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-12 | SC-M11-002/E5.1; SC-M11-002/E5.2; SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004; SC-M11-018/E15.1; SC-M11-018/E15.2; SC-M11-018/E35.1; SC-M11-018/E35.2; SC-M11-018/E36.1; SC-M11-018/E36.2; SC-M11-018/E37.1; SC-M11-018/E37.2; SC-M11-018/E38.1; SC-M11-018/E38.2; SC-M11-021/M2; SC-M11-021/E9.2; SC-M11-021/E14.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-13 | SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.4; SC-M11-018/E7.6; SC-M11-018/E8.6; SC-M11-018/E9.2; SC-M11-018/E10.2; SC-M11-018/E11.4; SC-M11-018/E12.4; SC-M11-018/E13.4; SC-M11-018/E14.4; SC-M11-018/E15.6; SC-M11-018/E19.6; SC-M11-018/E23.2; SC-M11-018/E24.4; SC-M11-018/E25.4; SC-M11-018/E26.4; SC-M11-018/E27.4; SC-M11-018/E28.4; SC-M11-018/E29.6; SC-M11-018/E30.2; SC-M11-018/E31.6; SC-M11-018/E32.2; SC-M11-018/E33.2; SC-M11-018/E34.2; AUT-M11-004; RULE-M11-004; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-021/E1.2; SC-M11-021/E2.4; SC-M11-019/M1; SC-M11-019/M2; SC-M11-019/E1.1; SC-M11-019/E5.1; SC-M11-019/E5.2; SC-M11-019/E10.1; SC-M11-019/E10.2; SC-M11-020/E3.1; SC-M11-019/E6.1; SC-M11-019/E6.2; SC-M11-019/E7.1; SC-M11-019/E7.2; SC-M11-019/E8.1; SC-M11-019/E8.2; SC-M11-019/E9.1; SC-M11-019/E9.2; SC-M11-020/M2; SC-M11-020/E8.2; SC-M11-020/E9.1; SC-M11-020/E9.2; SC-M11-020/E10.1; SC-M11-020/E10.2; SC-M11-020/E11.1; SC-M11-020/E11.2; SC-M11-020/E12.1; SC-M11-020/E12.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E4.1; SC-M11-021/E9.2; SC-M11-021/E10.1; SC-M11-021/E10.2; SC-M11-021/E11.1; SC-M11-021/E11.2; SC-M11-021/E12.1; SC-M11-021/E12.2; SC-M11-021/E13.1; SC-M11-021/E13.2; SC-M11-021/E14.2; SC-M11-020/M1; SC-M11-020/E1.1; SC-M11-020/E4.1; SC-M11-020/E8.1; SC-M11-020/E13.1; AUT-M11-003; SC-M11-021/E3.1; SC-M11-020/E2.1; SC-M11-020/E2.2; SC-M11-021/E5.1; SC-M11-021/E5.2; SC-M11-021/M1; SC-M11-021/E9.1; SC-M11-021/E14.1; SC-M11-021/E1.1; SC-M11-021/E2.3; SC-M11-021/E2.1; SC-M11-021/E2.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-14 | SC-M11-005/E4.1; SC-M11-005/E17.1; SC-M11-005/E17.2; SC-M11-022/M1; SC-M11-022/M2; SC-M11-022/E1.1; SC-M11-022/E1.2; SC-M11-022/E7.1; SC-M11-022/E7.2; SC-M11-022/E8.1; SC-M11-022/E8.2; SC-M11-022/E13.1; SC-M11-022/E13.2; RULE-M11-002; RULE-M11-005; SC-M11-022/E9.1; SC-M11-022/E9.2; SC-M11-022/E10.1; SC-M11-022/E10.2; SC-M11-022/E11.1; SC-M11-022/E11.2; SC-M11-022/E12.1; SC-M11-022/E12.2; AUT-M11-005; SC-M11-022/E2.1; SC-M11-022/E2.2; SC-M11-022/E3.1; SC-M11-022/E3.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-15 | SC-M11-002/E10.1; SC-M11-003/M1; SC-M11-003/M2; SC-M11-003/E2.1; SC-M11-003/E4.1; SC-M11-003/E4.2; SC-M11-004/M2; SC-M11-004/E1.1; SC-M11-005/E6.1; SC-M11-006/E2.1; SC-M11-007/E11.1; SC-M11-008/E4.1; SC-M11-009/E4.1; SC-M11-010/E4.1; SC-M11-011/E3.1; SC-M11-012/E3.1; SC-M11-013/E2.1; SC-M11-014/E3.1; SC-M11-015/E3.1; SC-M11-016/E5.1; SC-M11-017/E2.1; SC-M11-017/E4.4; SC-M11-018/E21.1; SC-M11-019/E3.1; SC-M11-020/E6.1; SC-M11-021/E7.1; SC-M11-022/E5.1; AUT-M11-002; RULE-M11-005; SC-M11-003/E5.1; SC-M11-003/E5.2; SC-M11-003/E6.1; SC-M11-003/E6.2; SC-M11-003/E7.1; SC-M11-003/E7.2; SC-M11-003/E8.1; SC-M11-003/E8.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-16 | SC-M11-002/E10.1; SC-M11-003/E2.1; SC-M11-004/M2; SC-M11-004/E1.1; SC-M11-005/E6.1; SC-M11-006/E2.1; SC-M11-007/E11.1; SC-M11-008/E4.1; SC-M11-009/E4.1; SC-M11-010/E4.1; SC-M11-011/E3.1; SC-M11-012/E3.1; SC-M11-013/E2.1; SC-M11-014/E3.1; SC-M11-015/E3.1; SC-M11-016/E5.1; SC-M11-017/E2.1; SC-M11-018/E21.1; SC-M11-019/E3.1; SC-M11-020/E6.1; SC-M11-021/E7.1; SC-M11-022/E5.1; AUT-M11-006; RULE-M11-006; SC-M11-002/E11.1; SC-M11-003/E3.1; SC-M11-007/E12.1; SC-M11-009/E5.1; SC-M11-010/E5.1; SC-M11-011/E4.1; SC-M11-014/E4.1; SC-M11-015/E4.1; SC-M11-016/E6.1; SC-M11-018/E22.1; SC-M11-019/E4.1; SC-M11-020/E7.1; SC-M11-021/E8.1; SC-M11-022/E6.1; SC-M11-002/E12.1; SC-M11-010/E6.1; SC-M11-013/E3.1; SC-M11-014/E5.1; SC-M11-015/E5.1; SC-M11-016/E7.1; SC-M11-005/M2; SC-M11-017/E6.1; SC-M11-017/E6.2; SC-M11-017/E7.1; SC-M11-017/E7.2; SC-M11-017/E8.2; SC-M11-017/E10.2; AUT-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-17 | SC-M11-001/M2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E7.1; SC-M11-001/E8.2; SC-M11-001/E9.2; SC-M11-001/E10.2; SC-M11-002/M2; SC-M11-002/M4; SC-M11-002/E1.2; SC-M11-002/E2.2; SC-M11-002/E3.2; SC-M11-002/E4.2; SC-M11-002/E5.2; SC-M11-002/E9.1; SC-M11-002/E12.1; SC-M11-002/E13.2; SC-M11-002/E13.4; SC-M11-002/E14.2; SC-M11-002/E15.2; SC-M11-002/E16.2; SC-M11-002/E17.2; SC-M11-003/M2; SC-M11-003/E1.1; SC-M11-003/E4.2; SC-M11-003/E5.2; SC-M11-003/E6.2; SC-M11-003/E7.2; SC-M11-003/E8.2; SC-M11-004/E2.1; SC-M11-005/E1.2; SC-M11-005/E5.1; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E11.2; SC-M11-005/E12.2; SC-M11-005/E14.2; SC-M11-005/E15.2; SC-M11-005/E16.2; SC-M11-005/E17.2; SC-M11-006/M2; SC-M11-006/E1.1; SC-M11-006/E3.2; SC-M11-006/E4.2; SC-M11-006/E5.2; SC-M11-006/E6.2; SC-M11-006/E7.2; SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.2; SC-M11-007/E10.1; SC-M11-007/E14.2; SC-M11-008/M2; SC-M11-008/E3.1; SC-M11-008/E5.2; SC-M11-009/M2; SC-M11-009/E1.2; SC-M11-009/E3.1; SC-M11-009/E6.2; SC-M11-009/E7.2; SC-M11-009/E8.2; SC-M11-009/E9.2; SC-M11-009/E10.2; SC-M11-010/M2; SC-M11-010/M4; SC-M11-010/E1.2; SC-M11-010/E3.1; SC-M11-010/E6.1; SC-M11-010/E7.2; SC-M11-010/E7.4; SC-M11-010/E8.2; SC-M11-010/E9.2; SC-M11-010/E10.2; SC-M11-010/E11.2; SC-M11-010/E12.2; SC-M11-010/E12.4; SC-M11-011/M2; SC-M11-011/E1.1; SC-M11-011/E2.1; SC-M11-011/E5.2; SC-M11-011/E6.2; SC-M11-011/E7.2; SC-M11-011/E8.2; SC-M11-011/E9.2; SC-M11-012/M2; SC-M11-012/E1.1; SC-M11-012/E2.1; SC-M11-012/E4.2; SC-M11-012/E5.2; SC-M11-012/E6.2; SC-M11-012/E7.2; SC-M11-013/M2; SC-M11-013/M4; SC-M11-013/E1.1; SC-M11-013/E3.1; SC-M11-013/E4.2; SC-M11-013/E4.4; SC-M11-013/E5.2; SC-M11-013/E6.2; SC-M11-013/E7.2; SC-M11-013/E7.4; SC-M11-014/M2; SC-M11-014/M4; SC-M11-014/E2.1; SC-M11-014/E5.1; SC-M11-014/E6.2; SC-M11-014/E6.4; SC-M11-014/E7.2; SC-M11-014/E8.2; SC-M11-014/E9.2; SC-M11-014/E10.2; SC-M11-015/M2; SC-M11-015/M4; SC-M11-015/E2.1; SC-M11-015/E5.1; SC-M11-015/E6.2; SC-M11-015/E6.4; SC-M11-015/E7.2; SC-M11-015/E8.2; SC-M11-015/E9.2; SC-M11-016/M2; SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E3.2; SC-M11-016/E3.4; SC-M11-016/E4.1; SC-M11-016/E7.1; SC-M11-016/E8.2; SC-M11-016/E11.2; SC-M11-016/E11.4; SC-M11-016/E12.2; SC-M11-016/E13.2; SC-M11-016/E14.2; SC-M11-017/M2; SC-M11-017/M4; SC-M11-017/E1.1; SC-M11-017/E3.2; SC-M11-017/E4.2; SC-M11-017/E4.4; SC-M11-017/E5.2; SC-M11-017/E7.2; SC-M11-017/E8.2; SC-M11-017/E9.2; SC-M11-017/E10.2; SC-M11-018/M2; SC-M11-018/E6.2; SC-M11-018/E7.2; SC-M11-018/E8.2; SC-M11-018/E9.2; SC-M11-018/E10.2; SC-M11-018/E11.2; SC-M11-018/E12.2; SC-M11-018/E13.2; SC-M11-018/E14.2; SC-M11-018/E15.4; SC-M11-018/E19.4; SC-M11-018/E20.1; SC-M11-018/E23.2; SC-M11-018/E24.2; SC-M11-018/E25.2; SC-M11-018/E26.2; SC-M11-018/E27.2; SC-M11-018/E28.2; SC-M11-018/E29.2; SC-M11-018/E30.2; SC-M11-018/E31.2; SC-M11-018/E32.2; SC-M11-018/E33.2; SC-M11-018/E34.2; SC-M11-018/E35.2; SC-M11-018/E36.2; SC-M11-018/E37.2; SC-M11-018/E38.2; SC-M11-019/M2; SC-M11-019/E1.1; SC-M11-019/E2.1; SC-M11-019/E5.2; SC-M11-019/E6.2; SC-M11-019/E7.2; SC-M11-019/E8.2; SC-M11-019/E9.2; SC-M11-019/E10.2; SC-M11-020/M2; SC-M11-020/E4.1; SC-M11-020/E5.1; SC-M11-020/E8.2; SC-M11-020/E9.2; SC-M11-020/E10.2; SC-M11-020/E11.2; SC-M11-020/E12.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E1.2; SC-M11-021/E2.4; SC-M11-021/E6.1; SC-M11-021/E9.2; SC-M11-021/E10.2; SC-M11-021/E11.2; SC-M11-021/E12.2; SC-M11-021/E13.2; SC-M11-021/E14.2; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E4.1; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E9.2; SC-M11-022/E10.2; SC-M11-022/E11.2; SC-M11-022/E12.2; SC-M11-022/E13.2; RULE-M11-006; SC-M11-001/E10.1; SC-M11-002/E13.1; SC-M11-002/E13.3; SC-M11-003/E4.1; SC-M11-006/E7.1; SC-M11-007/E14.1; SC-M11-008/E5.1; SC-M11-009/E6.1; SC-M11-010/E7.1; SC-M11-010/E7.3; SC-M11-011/E5.1; SC-M11-012/E4.1; SC-M11-013/E4.1; SC-M11-013/E4.3; SC-M11-014/E6.1; SC-M11-014/E6.3; SC-M11-015/E6.1; SC-M11-015/E6.3; SC-M11-016/E11.1; SC-M11-016/E11.3; SC-M11-017/E8.1; SC-M11-019/E5.1; SC-M11-020/E8.1; SC-M11-021/E9.1; SC-M11-022/E8.1; SC-M11-004/M2; SC-M11-004/E3.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-01.01 | SC-M11-001/M1; SC-M11-001/M2; SC-M11-001/E2.3; SC-M11-001/E3.3; SC-M11-001/E4.3; SC-M11-001/E5.1; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E10.1; SC-M11-001/E10.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-01.02 | SC-M11-001/M2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E10.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-01.03 | SC-M11-001/M2; SC-M11-001/E1.1; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E8.2; SC-M11-001/E9.2; SC-M11-001/E10.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-01.04 | SC-M11-001/E5.2; SC-M11-001/E8.1; SC-M11-001/E8.2; SC-M11-001/E9.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-01.05 | SC-M11-001/M2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E10.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-01.06 | SC-M11-001/M2; SC-M11-001/E1.1; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E10.2; SC-M11-003/M2; SC-M11-003/E4.2; SC-M11-017/E4.4; AUT-M11-002; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-01.07 | SC-M11-001/E5.2; SC-M11-001/E8.2; SC-M11-001/E9.1; SC-M11-001/E9.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-01.08 | SC-M11-001/M2; SC-M11-001/E2.1; SC-M11-001/E2.2; SC-M11-001/E3.1; SC-M11-001/E3.2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E10.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-002 |
| FR-M11-01.09 | SC-M11-001/M2; SC-M11-001/E4.1; SC-M11-001/E4.2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E10.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-002 |
| FR-M11-01.10 | SC-M11-001/M1; SC-M11-001/M2; SC-M11-001/E5.1; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E10.1; SC-M11-001/E10.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-01.11 | SC-M11-001/M1; SC-M11-001/E5.1; SC-M11-001/E5.2; SC-M11-001/E10.1; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-01.12 | SC-M11-001/M1; SC-M11-001/M2; SC-M11-001/E5.1; SC-M11-001/E6.2; SC-M11-001/E10.1; SC-M11-001/E10.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-02.01 | SC-M11-002/M1; SC-M11-002/M2; SC-M11-002/M3; SC-M11-002/M4; SC-M11-002/E6.3; SC-M11-002/E7.3; SC-M11-002/E8.3; SC-M11-002/E13.1; SC-M11-002/E13.2; SC-M11-002/E13.3; SC-M11-002/E13.4 | Đã đối soát phần đủ căn cứ |
| FR-M11-02.02 | SC-M11-002/M1; SC-M11-002/M2; SC-M11-002/M3; SC-M11-002/M4; SC-M11-002/E1.1; SC-M11-002/E2.1; SC-M11-002/E6.3; SC-M11-002/E7.3; SC-M11-002/E8.3; SC-M11-002/E13.1; SC-M11-002/E13.2; SC-M11-002/E13.3; SC-M11-002/E13.4; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-02.03 | SC-M11-002/M4; SC-M11-002/E13.4; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-02.04 | SC-M11-002/M4; SC-M11-002/E13.4; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-02.05 | SC-M11-002/M3; SC-M11-002/M4; SC-M11-002/E4.1; SC-M11-002/E4.2; SC-M11-002/E13.3; SC-M11-002/E13.4; RULE-M11-004 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-006 |
| FR-M11-02.06 | SC-M11-002/M3; SC-M11-002/M4; SC-M11-002/E5.1; SC-M11-002/E5.2; SC-M11-002/E13.3; SC-M11-002/E13.4; SC-M11-018/E15.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-02.07 | SC-M11-002/M3; SC-M11-002/M4; SC-M11-002/E1.1; SC-M11-002/E2.1; SC-M11-002/E3.1; SC-M11-002/E3.2; SC-M11-002/E13.3; SC-M11-002/E13.4 | Đã đối soát phần đủ căn cứ |
| FR-M11-02.08 | SC-M11-002/M3; SC-M11-002/M4; SC-M11-002/E3.1; SC-M11-002/E3.2; SC-M11-002/E13.3; SC-M11-002/E13.4 | Đã đối soát phần đủ căn cứ |
| FR-M11-02.09 | SC-M11-002/M2; SC-M11-002/M4; SC-M11-002/E13.2; SC-M11-002/E13.4; SC-M11-002/E14.1; SC-M11-002/E14.2; SC-M11-002/E15.1; SC-M11-002/E15.2; SC-M11-002/E16.1; SC-M11-002/E16.2; SC-M11-002/E17.1; SC-M11-002/E17.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-02.10 | SC-M11-002/M2; SC-M11-002/M4; SC-M11-002/E13.2; SC-M11-002/E13.4; SC-M11-002/E14.1; SC-M11-002/E14.2; SC-M11-002/E15.1; SC-M11-002/E15.2; SC-M11-002/E16.1; SC-M11-002/E16.2; SC-M11-002/E17.1; SC-M11-002/E17.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-02.11 | SC-M11-002/M4; SC-M11-002/E6.1; SC-M11-002/E6.2; SC-M11-002/E7.1; SC-M11-002/E7.2; SC-M11-002/E8.1; SC-M11-002/E8.2; SC-M11-002/E13.4 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-002 |
| FR-M11-02.12 | SC-M11-002/M4; SC-M11-002/E13.4; SC-M11-005/E3.1; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-02.13 | SC-M11-002/M4; SC-M11-002/E13.4; SC-M11-005/E3.1; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-02.14 | SC-M11-002/M4; SC-M11-002/E1.1; SC-M11-002/E1.2; SC-M11-002/E2.1; SC-M11-002/E2.2; SC-M11-002/E3.1; SC-M11-002/E3.2; SC-M11-002/E13.4; AUT-M11-001 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-007 |
| FR-M11-02.15 | SC-M11-002/M4; SC-M11-002/E4.1; SC-M11-002/E4.2; SC-M11-002/E13.4; RULE-M11-004 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-006 |
| FR-M11-03.01 | SC-M11-004/M1; SC-M11-004/M2; SC-M11-004/E1.1; SC-M11-004/E2.1; SC-M11-004/E3.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.02 | SC-M11-004/M2; SC-M11-004/E1.1; SC-M11-004/E2.1; SC-M11-004/E3.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.03 | SC-M11-004/E3.1; SC-M11-004/E3.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.04 | SC-M11-005/M1; SC-M11-005/M2; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E12.1; SC-M11-005/E12.2; SC-M11-005/E15.1; SC-M11-005/E15.2; SC-M11-005/E16.1; SC-M11-005/E16.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.05 | SC-M11-005/M2; SC-M11-005/E7.1; SC-M11-005/E7.2; SC-M11-005/E8.1; SC-M11-005/E8.2; SC-M11-005/E9.1; SC-M11-005/E9.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.06 | SC-M11-005/M2; SC-M11-005/E1.2; SC-M11-005/E2.1; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E11.2; SC-M11-005/E14.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.07 | RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.08 | RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.09 | SC-M11-005/M2; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E16.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.10 | SC-M11-005/M2; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E10.2; SC-M11-005/E12.1; SC-M11-005/E12.2; SC-M11-005/E13.2; SC-M11-005/E15.1; SC-M11-005/E15.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.11 | SC-M11-005/M2; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E11.1; SC-M11-005/E11.2; SC-M11-005/E14.1; SC-M11-005/E14.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.12 | SC-M11-005/M2; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E10.1; SC-M11-005/E10.2; SC-M11-005/E13.1; SC-M11-005/E13.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.13 | SC-M11-005/E16.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.14 | SC-M11-006/M1; SC-M11-006/M2; SC-M11-006/E3.1; SC-M11-006/E3.2; SC-M11-006/E4.1; SC-M11-006/E4.2; SC-M11-006/E5.1; SC-M11-006/E5.2; SC-M11-006/E6.1; SC-M11-006/E6.2; SC-M11-006/E7.1; SC-M11-006/E7.2; SC-M11-014/M2; SC-M11-014/E6.2; SC-M11-015/M2; SC-M11-015/E6.2; SC-M11-016/M2; SC-M11-016/E3.2; SC-M11-016/E11.2; SC-M11-017/M2; SC-M11-017/E3.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.15 | SC-M11-006/M2; SC-M11-006/E3.1; SC-M11-006/E3.2; SC-M11-006/E4.1; SC-M11-006/E4.2; SC-M11-006/E5.1; SC-M11-006/E5.2; SC-M11-006/E6.1; SC-M11-006/E6.2; SC-M11-006/E7.2; SC-M11-014/M2; SC-M11-014/E6.2; SC-M11-015/M2; SC-M11-015/E6.2; SC-M11-016/M2; SC-M11-016/E3.2; SC-M11-016/E11.2; SC-M11-017/M2; SC-M11-017/E3.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.16 | SC-M11-004/M1; SC-M11-004/M2; SC-M11-004/E1.1; SC-M11-004/E2.1; SC-M11-004/E3.1; SC-M11-004/E3.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.17 | SC-M11-004/M2; SC-M11-004/E1.1; SC-M11-004/E2.1; SC-M11-004/E3.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-03.18 | SC-M11-005/M2; SC-M11-005/E1.1; SC-M11-005/E1.2; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-04.01 | SC-M11-007/M1; SC-M11-007/M2; SC-M11-007/E9.2; SC-M11-007/E14.1; SC-M11-007/E14.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-04.02 | SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-04.03 | SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-04.04 | SC-M11-007/E9.1; SC-M11-010/E1.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-04.05 | SC-M11-005/E1.2; SC-M11-007/E13.1; SC-M11-007/E13.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-04.06 | SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E6.1; SC-M11-007/E6.2; SC-M11-007/E7.1; SC-M11-007/E7.2; SC-M11-007/E8.1; SC-M11-007/E8.2; SC-M11-007/E9.2; SC-M11-007/E14.2; SC-M11-011/M2; SC-M11-011/E5.2; SC-M11-011/E9.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-04.07 | SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.1; SC-M11-007/E9.2; SC-M11-007/E14.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-04.08 | SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.3; SC-M11-007/E4.4; SC-M11-007/E4.5; SC-M11-007/E4.6; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-04.09 | SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E5.1; SC-M11-007/E9.2; SC-M11-007/E14.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-04.10 | SC-M11-008/M1; SC-M11-008/M2; SC-M11-008/E1.1; SC-M11-008/E2.1; SC-M11-008/E2.2; SC-M11-008/E5.1; SC-M11-008/E5.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-05.01 | SC-M11-009/M1; SC-M11-009/M2; SC-M11-009/E1.1; SC-M11-009/E1.2; SC-M11-009/E6.1; SC-M11-009/E6.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-05.02 | SC-M11-009/M1; SC-M11-009/M2; SC-M11-009/E6.1; SC-M11-009/E6.2; AUT-M11-005; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-05.03 | SC-M11-009/E7.1; SC-M11-009/E7.2; SC-M11-009/E8.1; SC-M11-009/E8.2; SC-M11-009/E9.1; SC-M11-009/E9.2; SC-M11-009/E10.1; SC-M11-009/E10.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-05.04 | SC-M11-007/M2; SC-M11-007/E9.2; SC-M11-007/E14.2; SC-M11-009/M2; SC-M11-009/E1.2; SC-M11-009/E6.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-05.05 | SC-M11-007/M1; SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.2; SC-M11-007/E14.1; SC-M11-007/E14.2; SC-M11-009/M2; SC-M11-009/E6.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-05.06 | SC-M11-001/M2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E10.2; SC-M11-009/M2; SC-M11-009/E1.1; SC-M11-009/E1.2; SC-M11-009/E2.2; SC-M11-009/E6.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-05.07 | SC-M11-009/M2; SC-M11-009/E1.2; SC-M11-009/E2.1; SC-M11-009/E2.2; SC-M11-009/E6.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-06.01 | SC-M11-010/M1; SC-M11-010/M2; SC-M11-010/E7.1; SC-M11-010/E7.2; SC-M11-010/E12.1; SC-M11-010/E12.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-06.02 | SC-M11-002/E1.2; SC-M11-002/E2.2; SC-M11-010/M3; SC-M11-010/M4; SC-M11-010/E7.3; SC-M11-010/E7.4; SC-M11-010/E12.3; SC-M11-010/E12.4; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-06.03 | SC-M11-010/E1.1; SC-M11-010/E1.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-06.04 | SC-M11-002/E1.2; SC-M11-002/E2.2; SC-M11-010/M4; SC-M11-010/E7.4; SC-M11-010/E12.4; AUT-M11-005; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-06.05 | SC-M11-010/M2; SC-M11-010/E7.2; SC-M11-010/E8.1; SC-M11-010/E8.2; SC-M11-010/E9.1; SC-M11-010/E9.2; SC-M11-010/E10.1; SC-M11-010/E10.2; SC-M11-010/E11.1; SC-M11-010/E11.2; SC-M11-010/E12.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-06.06 | SC-M11-010/M4; SC-M11-010/E1.2; SC-M11-010/E2.1; SC-M11-010/E7.4; SC-M11-010/E12.4; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-06.07 | SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; AUT-M11-005; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-06.08 | SC-M11-007/M2; SC-M11-007/E9.2; SC-M11-007/E14.2; AUT-M11-005; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-06.09 | SC-M11-010/E1.2; SC-M11-011/M2; SC-M11-011/E5.2; SC-M11-011/E9.2; AUT-M11-005; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-07.01 | SC-M11-011/M1; SC-M11-011/M2; SC-M11-011/E1.1; SC-M11-011/E5.1; SC-M11-011/E5.2; SC-M11-011/E9.1; SC-M11-011/E9.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-07.02 | SC-M11-011/E6.1; SC-M11-011/E6.2; SC-M11-011/E7.1; SC-M11-011/E7.2; SC-M11-011/E8.1; SC-M11-011/E8.2; SC-M11-012/M2; SC-M11-012/E1.1; SC-M11-012/E4.2; SC-M11-012/E5.1; SC-M11-012/E5.2; SC-M11-012/E6.1; SC-M11-012/E6.2; SC-M11-012/E7.2; SC-M11-013/M2; SC-M11-013/E4.2; SC-M11-013/E5.1; SC-M11-013/E5.2; SC-M11-013/E6.1; SC-M11-013/E6.2; SC-M11-013/E7.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-07.03 | SC-M11-011/M2; SC-M11-011/E1.1; SC-M11-011/E5.2; SC-M11-011/E9.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-07.04 | SC-M11-012/M1; SC-M11-012/M2; SC-M11-012/E1.1; SC-M11-012/E4.1; SC-M11-012/E4.2; SC-M11-012/E7.1; SC-M11-012/E7.2; SC-M11-013/M1; SC-M11-013/M2; SC-M11-013/E4.1; SC-M11-013/E4.2; SC-M11-013/E7.1; SC-M11-013/E7.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-004 |
| FR-M11-07.05 | SC-M11-013/M1; SC-M11-013/M3; SC-M11-013/M4; SC-M11-013/E4.1; SC-M11-013/E4.3; SC-M11-013/E4.4; SC-M11-013/E7.1; SC-M11-013/E7.3; SC-M11-013/E7.4; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| FR-M11-08.01 | SC-M11-014/M1; SC-M11-014/M3; SC-M11-014/M4; SC-M11-014/E1.1; SC-M11-014/E6.1; SC-M11-014/E6.3; SC-M11-014/E6.4; SC-M11-015/E1.1; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-08.02 | SC-M11-014/E1.1; SC-M11-015/M1; SC-M11-015/M3; SC-M11-015/M4; SC-M11-015/E1.1; SC-M11-015/E6.1; SC-M11-015/E6.3; SC-M11-015/E6.4; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-08.03 | SC-M11-014/M4; SC-M11-014/E6.4; AUT-M11-005; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-08.04 | SC-M11-014/E7.1; SC-M11-014/E7.2; SC-M11-014/E8.1; SC-M11-014/E8.2; SC-M11-014/E9.1; SC-M11-014/E9.2; SC-M11-014/E10.1; SC-M11-014/E10.2; SC-M11-015/E7.1; SC-M11-015/E7.2; SC-M11-015/E8.1; SC-M11-015/E8.2; SC-M11-015/E9.1; SC-M11-015/E9.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-08.05 | SC-M11-014/M2; SC-M11-014/E6.2; SC-M11-015/M2; SC-M11-015/E6.2; SC-M11-016/M2; SC-M11-016/E3.2; SC-M11-016/E11.2; SC-M11-017/M2; SC-M11-017/E3.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-08.06 | SC-M11-015/M4; SC-M11-015/E6.4; AUT-M11-005; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| FR-M11-09.01 | SC-M11-016/M1; SC-M11-016/M3; SC-M11-016/M4; SC-M11-016/E1.1; SC-M11-016/E1.2; SC-M11-016/E2.1; SC-M11-016/E3.1; SC-M11-016/E3.3; SC-M11-016/E3.4; SC-M11-016/E11.1; SC-M11-016/E11.3; SC-M11-016/E11.4 | Đã đối soát phần đủ căn cứ |
| FR-M11-09.02 | SC-M11-016/E8.1; SC-M11-016/E8.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-09.03 | SC-M11-016/E2.1; SC-M11-016/E9.1; SC-M11-016/E9.2; SC-M11-016/E10.1; SC-M11-016/E10.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-09.04 | SC-M11-016/E12.1; SC-M11-016/E12.2; SC-M11-016/E13.1; SC-M11-016/E13.2; SC-M11-016/E14.1; SC-M11-016/E14.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-09.05 | SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E3.4; SC-M11-016/E8.2; SC-M11-016/E11.4; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-09.06 | SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E3.4; SC-M11-016/E8.2; SC-M11-016/E11.4; AUT-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-09.07 | SC-M11-007/E9.1; SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E3.4; SC-M11-016/E8.2; SC-M11-016/E11.4; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-10.01 | SC-M11-017/E7.2; SC-M11-017/E8.1; SC-M11-017/E8.2; SC-M11-017/E9.1; SC-M11-017/E9.2; SC-M11-017/E10.1; SC-M11-017/E10.2; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-10.02 | SC-M11-017/M4; SC-M11-017/E7.2; SC-M11-017/E8.2; SC-M11-017/E9.2; SC-M11-017/E10.2; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-10.03 | SC-M11-017/M1; SC-M11-017/M2; SC-M11-017/E3.1; SC-M11-017/E3.2; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-10.04 | SC-M11-017/M3; SC-M11-017/M4; RULE-M11-005 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-007 |
| FR-M11-10.05 | SC-M11-017/E3.3; SC-M11-017/E3.4; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-10.06 | SC-M11-017/E4.1; SC-M11-017/E4.2; SC-M11-017/E4.3; SC-M11-017/E4.4; SC-M11-017/E5.1; SC-M11-017/E5.2; SC-M11-017/E5.3; SC-M11-017/E5.4; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-10.07 | SC-M11-017/M4; AUT-M11-005; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-10.08 | SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E8.2; SC-M11-016/E11.4; SC-M11-017/M4; SC-M11-017/E7.2; SC-M11-017/E8.2; SC-M11-017/E10.2; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-10.09 | SC-M11-016/E3.4; SC-M11-017/E9.2; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-11.01 | AUT-M11-002 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-001 |
| FR-M11-11.02 | AUT-M11-002 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-001 |
| FR-M11-11.03 | AUT-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-11.04 | AUT-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-11.05 | AUT-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-11.06 | SC-M11-014/M4; SC-M11-014/E6.4; SC-M11-015/M4; SC-M11-015/E6.4; AUT-M11-002 | Đã đối soát phần đủ căn cứ |
| FR-M11-11.07 | AUT-M11-002; AUT-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.01 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.02 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.03 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.04 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.05 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.06 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.07 | SC-M11-002/E5.1; SC-M11-002/E5.2; SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.08 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.1; SC-M11-018/E15.2; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.09 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.10 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.11 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; SC-M11-018/E35.1; SC-M11-018/E35.2; SC-M11-018/E36.1; SC-M11-018/E36.2; SC-M11-018/E37.1; SC-M11-018/E37.2; SC-M11-018/E38.1; SC-M11-018/E38.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.12 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; SC-M11-021/M2; SC-M11-021/E9.2; SC-M11-021/E14.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.13 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; SC-M11-021/M2; SC-M11-021/E9.2; SC-M11-021/E14.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.14 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.15 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.16 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.17 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.18 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.19 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-12.20 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-13.01 | SC-M11-019/M1; SC-M11-019/M2; SC-M11-019/E1.1; SC-M11-019/E5.1; SC-M11-019/E5.2; SC-M11-019/E10.1; SC-M11-019/E10.2; SC-M11-020/E3.1; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-13.02 | SC-M11-020/M1; SC-M11-020/M2; SC-M11-020/E1.1; SC-M11-020/E3.1; SC-M11-020/E4.1; SC-M11-020/E8.1; SC-M11-020/E8.2; SC-M11-020/E13.1; SC-M11-020/E13.2; AUT-M11-003; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-13.03 | SC-M11-020/M2; SC-M11-020/E1.1; SC-M11-020/E4.1; SC-M11-020/E8.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E1.2; SC-M11-021/E2.4; SC-M11-021/E3.1; SC-M11-021/E9.2; SC-M11-021/E14.2; AUT-M11-003; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-13.04 | SC-M11-020/M2; SC-M11-020/E1.1; SC-M11-020/E4.1; SC-M11-020/E8.2; SC-M11-020/E13.2; SC-M11-021/E3.1; AUT-M11-003; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-13.05 | SC-M11-021/M1; SC-M11-021/M2; SC-M11-021/E9.1; SC-M11-021/E9.2; SC-M11-021/E14.1; SC-M11-021/E14.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-13.06 | SC-M11-021/E1.1; SC-M11-021/E1.2; SC-M11-021/E2.3; SC-M11-021/E2.4; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-13.07 | SC-M11-021/E1.2; SC-M11-021/E2.4; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-13.08 | SC-M11-019/M2; SC-M11-019/E5.2; SC-M11-019/E6.1; SC-M11-019/E6.2; SC-M11-019/E7.1; SC-M11-019/E7.2; SC-M11-019/E8.1; SC-M11-019/E8.2; SC-M11-019/E9.1; SC-M11-019/E9.2; SC-M11-019/E10.2; SC-M11-020/M2; SC-M11-020/E8.2; SC-M11-020/E9.1; SC-M11-020/E9.2; SC-M11-020/E10.1; SC-M11-020/E10.2; SC-M11-020/E11.1; SC-M11-020/E11.2; SC-M11-020/E12.1; SC-M11-020/E12.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E4.1; SC-M11-021/E9.2; SC-M11-021/E10.1; SC-M11-021/E10.2; SC-M11-021/E11.1; SC-M11-021/E11.2; SC-M11-021/E12.1; SC-M11-021/E12.2; SC-M11-021/E13.1; SC-M11-021/E13.2; SC-M11-021/E14.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-13.09 | SC-M11-019/M2; SC-M11-019/E5.2; SC-M11-019/E6.1; SC-M11-019/E6.2; SC-M11-019/E7.1; SC-M11-019/E7.2; SC-M11-019/E8.1; SC-M11-019/E8.2; SC-M11-019/E9.1; SC-M11-019/E9.2; SC-M11-019/E10.2; SC-M11-020/M2; SC-M11-020/E8.2; SC-M11-020/E9.1; SC-M11-020/E9.2; SC-M11-020/E10.1; SC-M11-020/E10.2; SC-M11-020/E11.1; SC-M11-020/E11.2; SC-M11-020/E12.1; SC-M11-020/E12.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E9.2; SC-M11-021/E10.1; SC-M11-021/E10.2; SC-M11-021/E11.1; SC-M11-021/E11.2; SC-M11-021/E12.1; SC-M11-021/E12.2; SC-M11-021/E13.1; SC-M11-021/E13.2; SC-M11-021/E14.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-13.10 | SC-M11-021/E1.2; SC-M11-021/E2.1; SC-M11-021/E2.2; SC-M11-021/E2.4; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-13.11 | SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-021/E1.2; SC-M11-021/E2.4; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-13.12 | SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.4; SC-M11-018/E7.6; SC-M11-018/E8.6; SC-M11-018/E9.2; SC-M11-018/E10.2; SC-M11-018/E11.4; SC-M11-018/E12.4; SC-M11-018/E13.4; SC-M11-018/E14.4; SC-M11-018/E15.6; SC-M11-018/E19.6; SC-M11-018/E23.2; SC-M11-018/E24.4; SC-M11-018/E25.4; SC-M11-018/E26.4; SC-M11-018/E27.4; SC-M11-018/E28.4; SC-M11-018/E29.6; SC-M11-018/E30.2; SC-M11-018/E31.6; SC-M11-018/E32.2; SC-M11-018/E33.2; SC-M11-018/E34.2; AUT-M11-004; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-13.13 | SC-M11-020/M2; SC-M11-020/E2.1; SC-M11-020/E2.2; SC-M11-020/E4.1; SC-M11-020/E8.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E5.1; SC-M11-021/E5.2; SC-M11-021/E9.2; SC-M11-021/E14.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| FR-M11-13.14 | AUT-M11-004; RULE-M11-004 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-006 |
| FR-M11-14.01 | SC-M11-005/E4.1; SC-M11-005/E17.1; SC-M11-005/E17.2; SC-M11-022/M1; SC-M11-022/M2; SC-M11-022/E1.1; SC-M11-022/E1.2; SC-M11-022/E7.1; SC-M11-022/E7.2; SC-M11-022/E8.1; SC-M11-022/E8.2; SC-M11-022/E13.1; SC-M11-022/E13.2; RULE-M11-002; RULE-M11-005 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-003 |
| FR-M11-14.02 | SC-M11-022/M2; SC-M11-022/E8.2; SC-M11-022/E9.1; SC-M11-022/E9.2; SC-M11-022/E10.1; SC-M11-022/E10.2; SC-M11-022/E11.1; SC-M11-022/E11.2; SC-M11-022/E12.1; SC-M11-022/E12.2; SC-M11-022/E13.2; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-14.03 | SC-M11-005/E17.2; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E13.2; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-14.04 | SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E13.2; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-14.05 | SC-M11-005/E17.2; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E13.2; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-14.06 | SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E13.2; AUT-M11-005; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-14.07 | SC-M11-005/E17.2; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E13.2; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-14.08 | SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E2.1; SC-M11-022/E2.2; SC-M11-022/E3.1; SC-M11-022/E3.2; SC-M11-022/E8.2; SC-M11-022/E13.2; RULE-M11-005 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-003 |
| FR-M11-15.01 | SC-M11-002/E10.1; SC-M11-003/M1; SC-M11-003/M2; SC-M11-003/E2.1; SC-M11-003/E4.1; SC-M11-003/E4.2; SC-M11-004/M2; SC-M11-004/E1.1; SC-M11-005/E6.1; SC-M11-006/E2.1; SC-M11-007/E11.1; SC-M11-008/E4.1; SC-M11-009/E4.1; SC-M11-010/E4.1; SC-M11-011/E3.1; SC-M11-012/E3.1; SC-M11-013/E2.1; SC-M11-014/E3.1; SC-M11-015/E3.1; SC-M11-016/E5.1; SC-M11-017/E2.1; SC-M11-017/E4.4; SC-M11-018/E21.1; SC-M11-019/E3.1; SC-M11-020/E6.1; SC-M11-021/E7.1; SC-M11-022/E5.1; AUT-M11-002; RULE-M11-005 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-007 |
| FR-M11-15.02 | SC-M11-002/E10.1; SC-M11-003/M2; SC-M11-003/E2.1; SC-M11-003/E4.2; SC-M11-005/E6.1; SC-M11-006/E2.1; SC-M11-007/E11.1; SC-M11-008/E4.1; SC-M11-009/E4.1; SC-M11-010/E4.1; SC-M11-011/E3.1; SC-M11-012/E3.1; SC-M11-013/E2.1; SC-M11-014/E3.1; SC-M11-015/E3.1; SC-M11-016/E5.1; SC-M11-017/E2.1; SC-M11-017/E4.4; SC-M11-018/E21.1; SC-M11-019/E3.1; SC-M11-020/E6.1; SC-M11-021/E7.1; SC-M11-022/E5.1; AUT-M11-002; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-15.03 | SC-M11-003/M2; SC-M11-003/E4.2; SC-M11-017/E4.4; AUT-M11-002; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-15.04 | SC-M11-003/M2; SC-M11-003/E4.2; SC-M11-003/E5.1; SC-M11-003/E5.2; SC-M11-003/E6.1; SC-M11-003/E6.2; SC-M11-003/E7.1; SC-M11-003/E7.2; SC-M11-003/E8.1; SC-M11-003/E8.2 | Đã đối soát phần đủ căn cứ |
| FR-M11-15.05 | SC-M11-002/E10.1; SC-M11-003/M2; SC-M11-003/E2.1; SC-M11-003/E4.2; SC-M11-005/E6.1; SC-M11-006/E2.1; SC-M11-007/E11.1; SC-M11-008/E4.1; SC-M11-009/E4.1; SC-M11-010/E4.1; SC-M11-011/E3.1; SC-M11-012/E3.1; SC-M11-013/E2.1; SC-M11-014/E3.1; SC-M11-015/E3.1; SC-M11-016/E5.1; SC-M11-017/E2.1; SC-M11-017/E4.4; SC-M11-018/E21.1; SC-M11-019/E3.1; SC-M11-020/E6.1; SC-M11-021/E7.1; SC-M11-022/E5.1; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| FR-M11-16.01 | SC-M11-002/E10.1; SC-M11-003/E2.1; SC-M11-004/M2; SC-M11-004/E1.1; SC-M11-005/E6.1; SC-M11-006/E2.1; SC-M11-007/E11.1; SC-M11-008/E4.1; SC-M11-009/E4.1; SC-M11-010/E4.1; SC-M11-011/E3.1; SC-M11-012/E3.1; SC-M11-013/E2.1; SC-M11-014/E3.1; SC-M11-015/E3.1; SC-M11-016/E5.1; SC-M11-017/E2.1; SC-M11-018/E21.1; SC-M11-019/E3.1; SC-M11-020/E6.1; SC-M11-021/E7.1; SC-M11-022/E5.1; AUT-M11-006; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-16.02 | SC-M11-002/E10.1; SC-M11-003/E2.1; SC-M11-005/E6.1; SC-M11-006/E2.1; SC-M11-007/E11.1; SC-M11-008/E4.1; SC-M11-009/E4.1; SC-M11-010/E4.1; SC-M11-011/E3.1; SC-M11-012/E3.1; SC-M11-013/E2.1; SC-M11-014/E3.1; SC-M11-015/E3.1; SC-M11-016/E5.1; SC-M11-017/E2.1; SC-M11-018/E21.1; SC-M11-019/E3.1; SC-M11-020/E6.1; SC-M11-021/E7.1; SC-M11-022/E5.1; AUT-M11-006; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-16.03 | SC-M11-005/M2; AUT-M11-006; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-16.04 | SC-M11-002/E11.1; SC-M11-003/E3.1; SC-M11-007/E12.1; SC-M11-009/E5.1; SC-M11-010/E5.1; SC-M11-011/E4.1; SC-M11-014/E4.1; SC-M11-015/E4.1; SC-M11-016/E6.1; SC-M11-018/E22.1; SC-M11-019/E4.1; SC-M11-020/E7.1; SC-M11-021/E8.1; SC-M11-022/E6.1; AUT-M11-006; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-16.05 | AUT-M11-006; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-16.06 | AUT-M11-006; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-16.07 | SC-M11-002/E11.1; SC-M11-002/E12.1; SC-M11-003/E3.1; SC-M11-007/E12.1; SC-M11-009/E5.1; SC-M11-010/E5.1; SC-M11-010/E6.1; SC-M11-011/E4.1; SC-M11-013/E3.1; SC-M11-014/E4.1; SC-M11-014/E5.1; SC-M11-015/E4.1; SC-M11-015/E5.1; SC-M11-016/E6.1; SC-M11-016/E7.1; SC-M11-018/E22.1; SC-M11-019/E4.1; SC-M11-020/E7.1; SC-M11-021/E8.1; SC-M11-022/E6.1; AUT-M11-006; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-16.08 | SC-M11-017/E6.1; SC-M11-017/E6.2; AUT-M11-006; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-16.09 | SC-M11-017/E7.1; SC-M11-017/E7.2; SC-M11-017/E8.2; SC-M11-017/E10.2; AUT-M11-006; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-16.10 | AUT-M11-002; AUT-M11-006; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-17.01 | SC-M11-001/M2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E7.1; SC-M11-001/E8.2; SC-M11-001/E9.2; SC-M11-001/E10.2; SC-M11-002/M2; SC-M11-002/M4; SC-M11-002/E1.2; SC-M11-002/E2.2; SC-M11-002/E3.2; SC-M11-002/E4.2; SC-M11-002/E5.2; SC-M11-002/E9.1; SC-M11-002/E12.1; SC-M11-002/E13.2; SC-M11-002/E13.4; SC-M11-002/E14.2; SC-M11-002/E15.2; SC-M11-002/E16.2; SC-M11-002/E17.2; SC-M11-003/M2; SC-M11-003/E1.1; SC-M11-003/E4.2; SC-M11-003/E5.2; SC-M11-003/E6.2; SC-M11-003/E7.2; SC-M11-003/E8.2; SC-M11-004/E2.1; SC-M11-005/E1.2; SC-M11-005/E5.1; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E11.2; SC-M11-005/E12.2; SC-M11-005/E14.2; SC-M11-005/E15.2; SC-M11-005/E16.2; SC-M11-005/E17.2; SC-M11-006/M2; SC-M11-006/E1.1; SC-M11-006/E3.2; SC-M11-006/E4.2; SC-M11-006/E5.2; SC-M11-006/E6.2; SC-M11-006/E7.2; SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.2; SC-M11-007/E10.1; SC-M11-007/E14.2; SC-M11-008/M2; SC-M11-008/E3.1; SC-M11-008/E5.2; SC-M11-009/M2; SC-M11-009/E1.2; SC-M11-009/E3.1; SC-M11-009/E6.2; SC-M11-009/E7.2; SC-M11-009/E8.2; SC-M11-009/E9.2; SC-M11-009/E10.2; SC-M11-010/M2; SC-M11-010/M4; SC-M11-010/E1.2; SC-M11-010/E3.1; SC-M11-010/E6.1; SC-M11-010/E7.2; SC-M11-010/E7.4; SC-M11-010/E8.2; SC-M11-010/E9.2; SC-M11-010/E10.2; SC-M11-010/E11.2; SC-M11-010/E12.2; SC-M11-010/E12.4; SC-M11-011/M2; SC-M11-011/E1.1; SC-M11-011/E2.1; SC-M11-011/E5.2; SC-M11-011/E6.2; SC-M11-011/E7.2; SC-M11-011/E8.2; SC-M11-011/E9.2; SC-M11-012/M2; SC-M11-012/E1.1; SC-M11-012/E2.1; SC-M11-012/E4.2; SC-M11-012/E5.2; SC-M11-012/E6.2; SC-M11-012/E7.2; SC-M11-013/M2; SC-M11-013/M4; SC-M11-013/E1.1; SC-M11-013/E3.1; SC-M11-013/E4.2; SC-M11-013/E4.4; SC-M11-013/E5.2; SC-M11-013/E6.2; SC-M11-013/E7.2; SC-M11-013/E7.4; SC-M11-014/M2; SC-M11-014/M4; SC-M11-014/E2.1; SC-M11-014/E5.1; SC-M11-014/E6.2; SC-M11-014/E6.4; SC-M11-014/E7.2; SC-M11-014/E8.2; SC-M11-014/E9.2; SC-M11-014/E10.2; SC-M11-015/M2; SC-M11-015/M4; SC-M11-015/E2.1; SC-M11-015/E5.1; SC-M11-015/E6.2; SC-M11-015/E6.4; SC-M11-015/E7.2; SC-M11-015/E8.2; SC-M11-015/E9.2; SC-M11-016/M2; SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E3.2; SC-M11-016/E3.4; SC-M11-016/E4.1; SC-M11-016/E7.1; SC-M11-016/E8.2; SC-M11-016/E11.2; SC-M11-016/E11.4; SC-M11-016/E12.2; SC-M11-016/E13.2; SC-M11-016/E14.2; SC-M11-017/M2; SC-M11-017/M4; SC-M11-017/E1.1; SC-M11-017/E3.2; SC-M11-017/E4.2; SC-M11-017/E4.4; SC-M11-017/E5.2; SC-M11-017/E7.2; SC-M11-017/E8.2; SC-M11-017/E9.2; SC-M11-017/E10.2; SC-M11-018/M2; SC-M11-018/E6.2; SC-M11-018/E7.2; SC-M11-018/E8.2; SC-M11-018/E9.2; SC-M11-018/E10.2; SC-M11-018/E11.2; SC-M11-018/E12.2; SC-M11-018/E13.2; SC-M11-018/E14.2; SC-M11-018/E15.4; SC-M11-018/E19.4; SC-M11-018/E20.1; SC-M11-018/E23.2; SC-M11-018/E24.2; SC-M11-018/E25.2; SC-M11-018/E26.2; SC-M11-018/E27.2; SC-M11-018/E28.2; SC-M11-018/E29.2; SC-M11-018/E30.2; SC-M11-018/E31.2; SC-M11-018/E32.2; SC-M11-018/E33.2; SC-M11-018/E34.2; SC-M11-018/E35.2; SC-M11-018/E36.2; SC-M11-018/E37.2; SC-M11-018/E38.2; SC-M11-019/M2; SC-M11-019/E1.1; SC-M11-019/E2.1; SC-M11-019/E5.2; SC-M11-019/E6.2; SC-M11-019/E7.2; SC-M11-019/E8.2; SC-M11-019/E9.2; SC-M11-019/E10.2; SC-M11-020/M2; SC-M11-020/E4.1; SC-M11-020/E5.1; SC-M11-020/E8.2; SC-M11-020/E9.2; SC-M11-020/E10.2; SC-M11-020/E11.2; SC-M11-020/E12.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E1.2; SC-M11-021/E2.4; SC-M11-021/E6.1; SC-M11-021/E9.2; SC-M11-021/E10.2; SC-M11-021/E11.2; SC-M11-021/E12.2; SC-M11-021/E13.2; SC-M11-021/E14.2; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E4.1; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E9.2; SC-M11-022/E10.2; SC-M11-022/E11.2; SC-M11-022/E12.2; SC-M11-022/E13.2; RULE-M11-006 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-005 |
| FR-M11-17.02 | SC-M11-001/E7.1; SC-M11-002/E9.1; SC-M11-003/E1.1; SC-M11-004/M2; SC-M11-004/E2.1; SC-M11-005/E5.1; SC-M11-006/E1.1; SC-M11-007/E10.1; SC-M11-008/E3.1; SC-M11-009/E3.1; SC-M11-010/E3.1; SC-M11-011/E2.1; SC-M11-012/E2.1; SC-M11-013/E1.1; SC-M11-014/E2.1; SC-M11-015/E2.1; SC-M11-016/E4.1; SC-M11-017/E1.1; SC-M11-018/E20.1; SC-M11-019/E2.1; SC-M11-020/E5.1; SC-M11-021/E6.1; SC-M11-022/E4.1; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-17.03 | SC-M11-001/M2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E8.2; SC-M11-001/E9.2; SC-M11-001/E10.1; SC-M11-001/E10.2; SC-M11-002/M2; SC-M11-002/M4; SC-M11-002/E1.2; SC-M11-002/E2.2; SC-M11-002/E3.2; SC-M11-002/E4.2; SC-M11-002/E5.2; SC-M11-002/E13.1; SC-M11-002/E13.2; SC-M11-002/E13.3; SC-M11-002/E13.4; SC-M11-002/E14.2; SC-M11-002/E15.2; SC-M11-002/E16.2; SC-M11-002/E17.2; SC-M11-003/M2; SC-M11-003/E4.1; SC-M11-003/E4.2; SC-M11-003/E5.2; SC-M11-003/E6.2; SC-M11-003/E7.2; SC-M11-003/E8.2; SC-M11-005/E1.2; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E11.2; SC-M11-005/E12.2; SC-M11-005/E14.2; SC-M11-005/E15.2; SC-M11-005/E16.2; SC-M11-005/E17.2; SC-M11-006/M2; SC-M11-006/E3.2; SC-M11-006/E4.2; SC-M11-006/E5.2; SC-M11-006/E6.2; SC-M11-006/E7.1; SC-M11-006/E7.2; SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.2; SC-M11-007/E14.1; SC-M11-007/E14.2; SC-M11-008/M2; SC-M11-008/E5.1; SC-M11-008/E5.2; SC-M11-009/M2; SC-M11-009/E1.2; SC-M11-009/E6.1; SC-M11-009/E6.2; SC-M11-009/E7.2; SC-M11-009/E8.2; SC-M11-009/E9.2; SC-M11-009/E10.2; SC-M11-010/M2; SC-M11-010/M4; SC-M11-010/E1.2; SC-M11-010/E7.1; SC-M11-010/E7.2; SC-M11-010/E7.3; SC-M11-010/E7.4; SC-M11-010/E8.2; SC-M11-010/E9.2; SC-M11-010/E10.2; SC-M11-010/E11.2; SC-M11-010/E12.2; SC-M11-010/E12.4; SC-M11-011/M2; SC-M11-011/E1.1; SC-M11-011/E5.1; SC-M11-011/E5.2; SC-M11-011/E6.2; SC-M11-011/E7.2; SC-M11-011/E8.2; SC-M11-011/E9.2; SC-M11-012/M2; SC-M11-012/E1.1; SC-M11-012/E4.1; SC-M11-012/E4.2; SC-M11-012/E5.2; SC-M11-012/E6.2; SC-M11-012/E7.2; SC-M11-013/M2; SC-M11-013/M4; SC-M11-013/E4.1; SC-M11-013/E4.2; SC-M11-013/E4.3; SC-M11-013/E4.4; SC-M11-013/E5.2; SC-M11-013/E6.2; SC-M11-013/E7.2; SC-M11-013/E7.4; SC-M11-014/M2; SC-M11-014/M4; SC-M11-014/E6.1; SC-M11-014/E6.2; SC-M11-014/E6.3; SC-M11-014/E6.4; SC-M11-014/E7.2; SC-M11-014/E8.2; SC-M11-014/E9.2; SC-M11-014/E10.2; SC-M11-015/M2; SC-M11-015/M4; SC-M11-015/E6.1; SC-M11-015/E6.2; SC-M11-015/E6.3; SC-M11-015/E6.4; SC-M11-015/E7.2; SC-M11-015/E8.2; SC-M11-015/E9.2; SC-M11-016/M2; SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E3.2; SC-M11-016/E3.4; SC-M11-016/E8.2; SC-M11-016/E11.1; SC-M11-016/E11.2; SC-M11-016/E11.3; SC-M11-016/E11.4; SC-M11-016/E12.2; SC-M11-016/E13.2; SC-M11-016/E14.2; SC-M11-017/M2; SC-M11-017/M4; SC-M11-017/E3.2; SC-M11-017/E4.2; SC-M11-017/E4.4; SC-M11-017/E5.2; SC-M11-017/E7.2; SC-M11-017/E8.1; SC-M11-017/E8.2; SC-M11-017/E9.2; SC-M11-017/E10.2; SC-M11-018/M2; SC-M11-018/E6.2; SC-M11-018/E7.2; SC-M11-018/E8.2; SC-M11-018/E9.2; SC-M11-018/E10.2; SC-M11-018/E11.2; SC-M11-018/E12.2; SC-M11-018/E13.2; SC-M11-018/E14.2; SC-M11-018/E15.4; SC-M11-018/E19.4; SC-M11-018/E23.2; SC-M11-018/E24.2; SC-M11-018/E25.2; SC-M11-018/E26.2; SC-M11-018/E27.2; SC-M11-018/E28.2; SC-M11-018/E29.2; SC-M11-018/E30.2; SC-M11-018/E31.2; SC-M11-018/E32.2; SC-M11-018/E33.2; SC-M11-018/E34.2; SC-M11-018/E35.2; SC-M11-018/E36.2; SC-M11-018/E37.2; SC-M11-018/E38.2; SC-M11-019/M2; SC-M11-019/E1.1; SC-M11-019/E5.1; SC-M11-019/E5.2; SC-M11-019/E6.2; SC-M11-019/E7.2; SC-M11-019/E8.2; SC-M11-019/E9.2; SC-M11-019/E10.2; SC-M11-020/M2; SC-M11-020/E4.1; SC-M11-020/E8.1; SC-M11-020/E8.2; SC-M11-020/E9.2; SC-M11-020/E10.2; SC-M11-020/E11.2; SC-M11-020/E12.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E1.2; SC-M11-021/E2.4; SC-M11-021/E9.1; SC-M11-021/E9.2; SC-M11-021/E10.2; SC-M11-021/E11.2; SC-M11-021/E12.2; SC-M11-021/E13.2; SC-M11-021/E14.2; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E7.2; SC-M11-022/E8.1; SC-M11-022/E8.2; SC-M11-022/E9.2; SC-M11-022/E10.2; SC-M11-022/E11.2; SC-M11-022/E12.2; SC-M11-022/E13.2; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-17.04 | SC-M11-001/E7.1; SC-M11-002/E9.1; SC-M11-003/E1.1; SC-M11-004/E2.1; SC-M11-005/E5.1; SC-M11-006/E1.1; SC-M11-007/E10.1; SC-M11-008/E3.1; SC-M11-009/E3.1; SC-M11-010/E3.1; SC-M11-011/E2.1; SC-M11-012/E2.1; SC-M11-013/E1.1; SC-M11-014/E2.1; SC-M11-015/E2.1; SC-M11-016/E4.1; SC-M11-017/E1.1; SC-M11-018/E20.1; SC-M11-019/E2.1; SC-M11-020/E5.1; SC-M11-021/E6.1; SC-M11-022/E4.1; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-17.05 | SC-M11-001/E7.1; SC-M11-002/E9.1; SC-M11-003/E1.1; SC-M11-004/E2.1; SC-M11-005/E5.1; SC-M11-006/E1.1; SC-M11-007/E10.1; SC-M11-008/E3.1; SC-M11-009/E3.1; SC-M11-010/E3.1; SC-M11-011/E2.1; SC-M11-012/E2.1; SC-M11-013/E1.1; SC-M11-014/E2.1; SC-M11-015/E2.1; SC-M11-016/E4.1; SC-M11-017/E1.1; SC-M11-018/E20.1; SC-M11-019/E2.1; SC-M11-020/E5.1; SC-M11-021/E6.1; SC-M11-022/E4.1; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-17.06 | SC-M11-001/E7.1; SC-M11-002/E9.1; SC-M11-003/E1.1; SC-M11-004/E2.1; SC-M11-005/E5.1; SC-M11-006/E1.1; SC-M11-007/E10.1; SC-M11-008/E3.1; SC-M11-009/E3.1; SC-M11-010/E3.1; SC-M11-011/E2.1; SC-M11-012/E2.1; SC-M11-013/E1.1; SC-M11-014/E2.1; SC-M11-015/E2.1; SC-M11-016/E4.1; SC-M11-017/E1.1; SC-M11-018/E20.1; SC-M11-019/E2.1; SC-M11-020/E5.1; SC-M11-021/E6.1; SC-M11-022/E4.1; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| FR-M11-17.07 | SC-M11-001/E7.1; SC-M11-002/E9.1; SC-M11-003/E1.1; SC-M11-004/M2; SC-M11-004/E2.1; SC-M11-004/E3.2; SC-M11-005/E5.1; SC-M11-006/E1.1; SC-M11-007/E10.1; SC-M11-008/E3.1; SC-M11-009/E3.1; SC-M11-010/E3.1; SC-M11-011/E2.1; SC-M11-012/E2.1; SC-M11-013/E1.1; SC-M11-014/E2.1; SC-M11-015/E2.1; SC-M11-016/E4.1; SC-M11-017/E1.1; SC-M11-018/E20.1; SC-M11-019/E2.1; SC-M11-020/E5.1; SC-M11-021/E6.1; SC-M11-022/E4.1; RULE-M11-006 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-005 |
| FR-M11-17.08 | SC-M11-001/M2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E7.1; SC-M11-001/E8.2; SC-M11-001/E9.2; SC-M11-001/E10.2; SC-M11-002/M2; SC-M11-002/M4; SC-M11-002/E1.2; SC-M11-002/E2.2; SC-M11-002/E3.2; SC-M11-002/E4.2; SC-M11-002/E5.2; SC-M11-002/E9.1; SC-M11-002/E12.1; SC-M11-002/E13.2; SC-M11-002/E13.4; SC-M11-002/E14.2; SC-M11-002/E15.2; SC-M11-002/E16.2; SC-M11-002/E17.2; SC-M11-003/M2; SC-M11-003/E1.1; SC-M11-003/E4.2; SC-M11-003/E5.2; SC-M11-003/E6.2; SC-M11-003/E7.2; SC-M11-003/E8.2; SC-M11-004/E2.1; SC-M11-005/E1.2; SC-M11-005/E5.1; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E11.2; SC-M11-005/E12.2; SC-M11-005/E14.2; SC-M11-005/E15.2; SC-M11-005/E16.2; SC-M11-005/E17.2; SC-M11-006/M2; SC-M11-006/E1.1; SC-M11-006/E3.2; SC-M11-006/E4.2; SC-M11-006/E5.2; SC-M11-006/E6.2; SC-M11-006/E7.2; SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.2; SC-M11-007/E10.1; SC-M11-007/E14.2; SC-M11-008/M2; SC-M11-008/E3.1; SC-M11-008/E5.2; SC-M11-009/M2; SC-M11-009/E1.2; SC-M11-009/E3.1; SC-M11-009/E6.2; SC-M11-009/E7.2; SC-M11-009/E8.2; SC-M11-009/E9.2; SC-M11-009/E10.2; SC-M11-010/M2; SC-M11-010/M4; SC-M11-010/E1.2; SC-M11-010/E3.1; SC-M11-010/E6.1; SC-M11-010/E7.2; SC-M11-010/E7.4; SC-M11-010/E8.2; SC-M11-010/E9.2; SC-M11-010/E10.2; SC-M11-010/E11.2; SC-M11-010/E12.2; SC-M11-010/E12.4; SC-M11-011/M2; SC-M11-011/E1.1; SC-M11-011/E2.1; SC-M11-011/E5.2; SC-M11-011/E6.2; SC-M11-011/E7.2; SC-M11-011/E8.2; SC-M11-011/E9.2; SC-M11-012/M2; SC-M11-012/E1.1; SC-M11-012/E2.1; SC-M11-012/E4.2; SC-M11-012/E5.2; SC-M11-012/E6.2; SC-M11-012/E7.2; SC-M11-013/M2; SC-M11-013/M4; SC-M11-013/E1.1; SC-M11-013/E3.1; SC-M11-013/E4.2; SC-M11-013/E4.4; SC-M11-013/E5.2; SC-M11-013/E6.2; SC-M11-013/E7.2; SC-M11-013/E7.4; SC-M11-014/M2; SC-M11-014/M4; SC-M11-014/E2.1; SC-M11-014/E5.1; SC-M11-014/E6.2; SC-M11-014/E6.4; SC-M11-014/E7.2; SC-M11-014/E8.2; SC-M11-014/E9.2; SC-M11-014/E10.2; SC-M11-015/M2; SC-M11-015/M4; SC-M11-015/E2.1; SC-M11-015/E5.1; SC-M11-015/E6.2; SC-M11-015/E6.4; SC-M11-015/E7.2; SC-M11-015/E8.2; SC-M11-015/E9.2; SC-M11-016/M2; SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E3.2; SC-M11-016/E3.4; SC-M11-016/E4.1; SC-M11-016/E7.1; SC-M11-016/E8.2; SC-M11-016/E11.2; SC-M11-016/E11.4; SC-M11-016/E12.2; SC-M11-016/E13.2; SC-M11-016/E14.2; SC-M11-017/M2; SC-M11-017/M4; SC-M11-017/E1.1; SC-M11-017/E3.2; SC-M11-017/E4.2; SC-M11-017/E4.4; SC-M11-017/E5.2; SC-M11-017/E7.2; SC-M11-017/E8.2; SC-M11-017/E9.2; SC-M11-017/E10.2; SC-M11-018/M2; SC-M11-018/E6.2; SC-M11-018/E7.2; SC-M11-018/E8.2; SC-M11-018/E9.2; SC-M11-018/E10.2; SC-M11-018/E11.2; SC-M11-018/E12.2; SC-M11-018/E13.2; SC-M11-018/E14.2; SC-M11-018/E15.4; SC-M11-018/E19.4; SC-M11-018/E20.1; SC-M11-018/E23.2; SC-M11-018/E24.2; SC-M11-018/E25.2; SC-M11-018/E26.2; SC-M11-018/E27.2; SC-M11-018/E28.2; SC-M11-018/E29.2; SC-M11-018/E30.2; SC-M11-018/E31.2; SC-M11-018/E32.2; SC-M11-018/E33.2; SC-M11-018/E34.2; SC-M11-018/E35.2; SC-M11-018/E36.2; SC-M11-018/E37.2; SC-M11-018/E38.2; SC-M11-019/M2; SC-M11-019/E1.1; SC-M11-019/E2.1; SC-M11-019/E5.2; SC-M11-019/E6.2; SC-M11-019/E7.2; SC-M11-019/E8.2; SC-M11-019/E9.2; SC-M11-019/E10.2; SC-M11-020/M2; SC-M11-020/E4.1; SC-M11-020/E5.1; SC-M11-020/E8.2; SC-M11-020/E9.2; SC-M11-020/E10.2; SC-M11-020/E11.2; SC-M11-020/E12.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E1.2; SC-M11-021/E2.4; SC-M11-021/E6.1; SC-M11-021/E9.2; SC-M11-021/E10.2; SC-M11-021/E11.2; SC-M11-021/E12.2; SC-M11-021/E13.2; SC-M11-021/E14.2; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E4.1; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E9.2; SC-M11-022/E10.2; SC-M11-022/E11.2; SC-M11-022/E12.2; SC-M11-022/E13.2; RULE-M11-006 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-005 |
| BR-M11-01 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| BR-M11-02 | SC-M11-001/M2; SC-M11-001/E6.2; SC-M11-001/E10.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| BR-M11-03 | SC-M11-001/M2; SC-M11-001/E1.1; SC-M11-001/E5.2; SC-M11-001/E6.1; SC-M11-001/E6.2; SC-M11-001/E8.2; SC-M11-001/E9.2; SC-M11-001/E10.2; SC-M11-007/M2; SC-M11-007/E9.2; SC-M11-007/E14.2; RULE-M11-001; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| BR-M11-04 | SC-M11-001/M2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E10.2; SC-M11-017/M2; SC-M11-017/M4; SC-M11-017/E3.2; AUT-M11-002; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| BR-M11-05 | SC-M11-014/M4; SC-M11-014/E1.1; SC-M11-014/E6.4; SC-M11-015/M4; SC-M11-015/E1.1; SC-M11-015/E6.4; SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E2.1; SC-M11-016/E8.2; SC-M11-016/E9.2; SC-M11-016/E10.2; SC-M11-016/E11.4; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E2.2; SC-M11-022/E3.2; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E13.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-003 |
| BR-M11-06 | SC-M11-001/M2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E8.2; SC-M11-001/E9.2; SC-M11-001/E10.2; SC-M11-002/M2; SC-M11-002/M4; SC-M11-002/E1.2; SC-M11-002/E2.2; SC-M11-002/E3.2; SC-M11-002/E4.2; SC-M11-002/E5.2; SC-M11-002/E13.2; SC-M11-002/E13.4; SC-M11-002/E14.1; SC-M11-002/E14.2; SC-M11-002/E15.1; SC-M11-002/E15.2; SC-M11-002/E16.1; SC-M11-002/E16.2; SC-M11-002/E17.1; SC-M11-002/E17.2; SC-M11-003/M2; SC-M11-003/E4.2; SC-M11-003/E5.1; SC-M11-003/E5.2; SC-M11-003/E6.1; SC-M11-003/E6.2; SC-M11-003/E7.1; SC-M11-003/E7.2; SC-M11-003/E8.1; SC-M11-003/E8.2; SC-M11-005/E1.2; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E11.2; SC-M11-005/E12.2; SC-M11-005/E14.2; SC-M11-005/E15.2; SC-M11-005/E16.2; SC-M11-005/E17.2; SC-M11-006/M2; SC-M11-006/E3.2; SC-M11-006/E4.2; SC-M11-006/E5.2; SC-M11-006/E6.2; SC-M11-006/E7.2; SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.2; SC-M11-007/E14.2; SC-M11-008/M2; SC-M11-008/E5.2; SC-M11-009/M2; SC-M11-009/E1.2; SC-M11-009/E6.2; SC-M11-009/E7.2; SC-M11-009/E8.2; SC-M11-009/E9.2; SC-M11-009/E10.2; SC-M11-010/M2; SC-M11-010/M4; SC-M11-010/E1.2; SC-M11-010/E7.2; SC-M11-010/E7.4; SC-M11-010/E8.1; SC-M11-010/E8.2; SC-M11-010/E9.1; SC-M11-010/E9.2; SC-M11-010/E10.1; SC-M11-010/E10.2; SC-M11-010/E11.1; SC-M11-010/E11.2; SC-M11-010/E12.2; SC-M11-010/E12.4; SC-M11-011/M2; SC-M11-011/E1.1; SC-M11-011/E5.2; SC-M11-011/E6.1; SC-M11-011/E6.2; SC-M11-011/E7.1; SC-M11-011/E7.2; SC-M11-011/E8.1; SC-M11-011/E8.2; SC-M11-011/E9.2; SC-M11-012/M2; SC-M11-012/E1.1; SC-M11-012/E4.2; SC-M11-012/E5.1; SC-M11-012/E5.2; SC-M11-012/E6.1; SC-M11-012/E6.2; SC-M11-012/E7.2; SC-M11-013/M2; SC-M11-013/M4; SC-M11-013/E4.2; SC-M11-013/E4.4; SC-M11-013/E5.1; SC-M11-013/E5.2; SC-M11-013/E6.1; SC-M11-013/E6.2; SC-M11-013/E7.2; SC-M11-013/E7.4; SC-M11-014/M2; SC-M11-014/M4; SC-M11-014/E1.1; SC-M11-014/E6.2; SC-M11-014/E6.4; SC-M11-014/E7.1; SC-M11-014/E7.2; SC-M11-014/E8.1; SC-M11-014/E8.2; SC-M11-014/E9.1; SC-M11-014/E9.2; SC-M11-014/E10.1; SC-M11-014/E10.2; SC-M11-015/M2; SC-M11-015/M4; SC-M11-015/E1.1; SC-M11-015/E6.2; SC-M11-015/E6.4; SC-M11-015/E7.1; SC-M11-015/E7.2; SC-M11-015/E8.1; SC-M11-015/E8.2; SC-M11-015/E9.1; SC-M11-015/E9.2; SC-M11-016/M2; SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E2.1; SC-M11-016/E3.2; SC-M11-016/E3.4; SC-M11-016/E8.2; SC-M11-016/E11.2; SC-M11-016/E11.4; SC-M11-016/E12.1; SC-M11-016/E12.2; SC-M11-016/E13.1; SC-M11-016/E13.2; SC-M11-016/E14.1; SC-M11-016/E14.2; SC-M11-017/M2; SC-M11-017/M4; SC-M11-017/E3.2; SC-M11-017/E4.2; SC-M11-017/E4.4; SC-M11-017/E5.2; SC-M11-017/E7.2; SC-M11-017/E8.2; SC-M11-017/E9.2; SC-M11-017/E10.2; SC-M11-018/M2; SC-M11-018/E6.2; SC-M11-018/E7.2; SC-M11-018/E8.2; SC-M11-018/E9.2; SC-M11-018/E10.2; SC-M11-018/E11.2; SC-M11-018/E12.2; SC-M11-018/E13.2; SC-M11-018/E14.2; SC-M11-018/E15.4; SC-M11-018/E19.4; SC-M11-018/E23.2; SC-M11-018/E24.2; SC-M11-018/E25.2; SC-M11-018/E26.2; SC-M11-018/E27.2; SC-M11-018/E28.2; SC-M11-018/E29.2; SC-M11-018/E30.2; SC-M11-018/E31.2; SC-M11-018/E32.2; SC-M11-018/E33.2; SC-M11-018/E34.2; SC-M11-018/E35.1; SC-M11-018/E35.2; SC-M11-018/E36.1; SC-M11-018/E36.2; SC-M11-018/E37.1; SC-M11-018/E37.2; SC-M11-018/E38.1; SC-M11-018/E38.2; SC-M11-019/M2; SC-M11-019/E1.1; SC-M11-019/E5.2; SC-M11-019/E6.2; SC-M11-019/E7.2; SC-M11-019/E8.2; SC-M11-019/E9.2; SC-M11-019/E10.2; SC-M11-020/M2; SC-M11-020/E4.1; SC-M11-020/E8.2; SC-M11-020/E9.2; SC-M11-020/E10.2; SC-M11-020/E11.2; SC-M11-020/E12.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E1.2; SC-M11-021/E2.4; SC-M11-021/E4.1; SC-M11-021/E9.2; SC-M11-021/E10.2; SC-M11-021/E11.2; SC-M11-021/E12.2; SC-M11-021/E13.2; SC-M11-021/E14.2; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E9.1; SC-M11-022/E9.2; SC-M11-022/E10.1; SC-M11-022/E10.2; SC-M11-022/E11.1; SC-M11-022/E11.2; SC-M11-022/E12.1; SC-M11-022/E12.2; SC-M11-022/E13.2; RULE-M11-001 | Đã đối soát phần đủ căn cứ |
| BR-M11-07 | SC-M11-002/E1.2; SC-M11-002/E2.2; SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.2; SC-M11-007/E13.2; SC-M11-007/E14.2; SC-M11-010/M4; SC-M11-010/E7.4; SC-M11-010/E12.4; AUT-M11-001; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| BR-M11-08 | SC-M11-002/M4; SC-M11-002/E3.1; SC-M11-002/E3.2; SC-M11-002/E13.4; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.4; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-010/M2; SC-M11-010/E7.2; SC-M11-010/E12.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-002 |
| BR-M11-09 | SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E5.1; SC-M11-007/E9.2; SC-M11-007/E14.2; SC-M11-010/E1.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| BR-M11-10 | SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E6.2; SC-M11-007/E7.2; SC-M11-007/E8.2; SC-M11-007/E9.2; SC-M11-007/E14.2; SC-M11-011/M2; SC-M11-011/E1.1; SC-M11-011/E5.2; SC-M11-011/E9.2; SC-M11-012/M2; SC-M11-012/E1.1; SC-M11-012/E4.2; SC-M11-012/E7.2; SC-M11-013/M2; SC-M11-013/M4; SC-M11-013/E4.2; SC-M11-013/E4.4; SC-M11-013/E7.2; SC-M11-013/E7.4; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| BR-M11-11 | SC-M11-004/M2; SC-M11-004/E1.1; SC-M11-004/E3.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| BR-M11-12 | SC-M11-005/E1.2; SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.2; SC-M11-007/E14.2; SC-M11-009/M2; SC-M11-009/E1.2; SC-M11-009/E2.2; SC-M11-009/E6.2; SC-M11-009/E7.1; SC-M11-009/E7.2; SC-M11-009/E8.1; SC-M11-009/E8.2; SC-M11-009/E9.1; SC-M11-009/E9.2; SC-M11-009/E10.1; SC-M11-009/E10.2; RULE-M11-002; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| BR-M11-13 | SC-M11-005/M2; SC-M11-005/E1.2; SC-M11-005/E2.1; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E16.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| BR-M11-14 | SC-M11-005/M2; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| BR-M11-15 | SC-M11-002/M4; SC-M11-002/E13.4; SC-M11-005/E2.1; SC-M11-005/E3.1; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| BR-M11-16 | SC-M11-002/M4; SC-M11-002/E5.1; SC-M11-002/E5.2; SC-M11-002/E13.4; SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.2; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| BR-M11-17 | SC-M11-005/M2; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E10.2; SC-M11-005/E12.2; SC-M11-005/E13.2; SC-M11-005/E15.2; SC-M11-005/E16.2; SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; SC-M11-019/M2; SC-M11-019/E5.2; SC-M11-019/E10.2; SC-M11-021/M2; SC-M11-021/E9.2; SC-M11-021/E14.2; RULE-M11-002; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| BR-M11-18 | SC-M11-002/M4; SC-M11-002/E4.1; SC-M11-002/E4.2; SC-M11-002/E13.4; SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; SC-M11-021/M2; SC-M11-021/E9.2; SC-M11-021/E14.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| BR-M11-19 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| BR-M11-20 | SC-M11-019/M2; SC-M11-019/E1.1; SC-M11-019/E5.2; SC-M11-019/E10.2; SC-M11-020/M2; SC-M11-020/E1.1; SC-M11-020/E3.1; SC-M11-020/E4.1; SC-M11-020/E8.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E1.2; SC-M11-021/E2.4; SC-M11-021/E3.1; SC-M11-021/E4.1; SC-M11-021/E9.2; SC-M11-021/E14.2; AUT-M11-003; RULE-M11-004 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-006 |
| BR-M11-21 | SC-M11-021/E1.2; SC-M11-021/E2.4; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E8.2; SC-M11-022/E13.2; AUT-M11-004; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| BR-M11-22 | SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E8.2; SC-M11-022/E13.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| BR-M11-23 | SC-M11-001/M2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E8.2; SC-M11-001/E9.2; SC-M11-001/E10.2; SC-M11-002/M2; SC-M11-002/M4; SC-M11-002/E1.2; SC-M11-002/E2.2; SC-M11-002/E3.2; SC-M11-002/E4.2; SC-M11-002/E5.2; SC-M11-002/E10.1; SC-M11-002/E13.2; SC-M11-002/E13.4; SC-M11-002/E14.2; SC-M11-002/E15.2; SC-M11-002/E16.2; SC-M11-002/E17.2; SC-M11-003/M2; SC-M11-003/E2.1; SC-M11-003/E4.2; SC-M11-003/E5.2; SC-M11-003/E6.2; SC-M11-003/E7.2; SC-M11-003/E8.2; SC-M11-004/M2; SC-M11-005/E1.2; SC-M11-005/E6.1; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E11.2; SC-M11-005/E12.2; SC-M11-005/E14.2; SC-M11-005/E15.2; SC-M11-005/E16.2; SC-M11-005/E17.2; SC-M11-006/M2; SC-M11-006/E2.1; SC-M11-006/E3.2; SC-M11-006/E4.2; SC-M11-006/E5.2; SC-M11-006/E6.2; SC-M11-006/E7.2; SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.2; SC-M11-007/E11.1; SC-M11-007/E14.2; SC-M11-008/M2; SC-M11-008/E4.1; SC-M11-008/E5.2; SC-M11-009/M2; SC-M11-009/E1.2; SC-M11-009/E4.1; SC-M11-009/E6.2; SC-M11-009/E7.2; SC-M11-009/E8.2; SC-M11-009/E9.2; SC-M11-009/E10.2; SC-M11-010/M2; SC-M11-010/M4; SC-M11-010/E1.2; SC-M11-010/E4.1; SC-M11-010/E7.2; SC-M11-010/E7.4; SC-M11-010/E8.2; SC-M11-010/E9.2; SC-M11-010/E10.2; SC-M11-010/E11.2; SC-M11-010/E12.2; SC-M11-010/E12.4; SC-M11-011/M2; SC-M11-011/E1.1; SC-M11-011/E3.1; SC-M11-011/E5.2; SC-M11-011/E6.2; SC-M11-011/E7.2; SC-M11-011/E8.2; SC-M11-011/E9.2; SC-M11-012/M2; SC-M11-012/E1.1; SC-M11-012/E3.1; SC-M11-012/E4.2; SC-M11-012/E5.2; SC-M11-012/E6.2; SC-M11-012/E7.2; SC-M11-013/M2; SC-M11-013/M4; SC-M11-013/E2.1; SC-M11-013/E4.2; SC-M11-013/E4.4; SC-M11-013/E5.2; SC-M11-013/E6.2; SC-M11-013/E7.2; SC-M11-013/E7.4; SC-M11-014/M2; SC-M11-014/M4; SC-M11-014/E3.1; SC-M11-014/E6.2; SC-M11-014/E6.4; SC-M11-014/E7.2; SC-M11-014/E8.2; SC-M11-014/E9.2; SC-M11-014/E10.2; SC-M11-015/M2; SC-M11-015/M4; SC-M11-015/E3.1; SC-M11-015/E6.2; SC-M11-015/E6.4; SC-M11-015/E7.2; SC-M11-015/E8.2; SC-M11-015/E9.2; SC-M11-016/M2; SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E3.2; SC-M11-016/E3.4; SC-M11-016/E5.1; SC-M11-016/E8.2; SC-M11-016/E11.2; SC-M11-016/E11.4; SC-M11-016/E12.2; SC-M11-016/E13.2; SC-M11-016/E14.2; SC-M11-017/M2; SC-M11-017/M4; SC-M11-017/E2.1; SC-M11-017/E3.2; SC-M11-017/E4.2; SC-M11-017/E4.4; SC-M11-017/E5.2; SC-M11-017/E7.2; SC-M11-017/E8.2; SC-M11-017/E9.2; SC-M11-017/E10.2; SC-M11-018/M2; SC-M11-018/E6.2; SC-M11-018/E7.2; SC-M11-018/E8.2; SC-M11-018/E9.2; SC-M11-018/E10.2; SC-M11-018/E11.2; SC-M11-018/E12.2; SC-M11-018/E13.2; SC-M11-018/E14.2; SC-M11-018/E15.4; SC-M11-018/E19.4; SC-M11-018/E21.1; SC-M11-018/E23.2; SC-M11-018/E24.2; SC-M11-018/E25.2; SC-M11-018/E26.2; SC-M11-018/E27.2; SC-M11-018/E28.2; SC-M11-018/E29.2; SC-M11-018/E30.2; SC-M11-018/E31.2; SC-M11-018/E32.2; SC-M11-018/E33.2; SC-M11-018/E34.2; SC-M11-018/E35.2; SC-M11-018/E36.2; SC-M11-018/E37.2; SC-M11-018/E38.2; SC-M11-019/M2; SC-M11-019/E1.1; SC-M11-019/E3.1; SC-M11-019/E5.2; SC-M11-019/E6.2; SC-M11-019/E7.2; SC-M11-019/E8.2; SC-M11-019/E9.2; SC-M11-019/E10.2; SC-M11-020/M2; SC-M11-020/E4.1; SC-M11-020/E6.1; SC-M11-020/E8.2; SC-M11-020/E9.2; SC-M11-020/E10.2; SC-M11-020/E11.2; SC-M11-020/E12.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E1.2; SC-M11-021/E2.4; SC-M11-021/E7.1; SC-M11-021/E9.2; SC-M11-021/E10.2; SC-M11-021/E11.2; SC-M11-021/E12.2; SC-M11-021/E13.2; SC-M11-021/E14.2; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E5.1; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E9.2; SC-M11-022/E10.2; SC-M11-022/E11.2; SC-M11-022/E12.2; SC-M11-022/E13.2; AUT-M11-002; RULE-M11-005; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| BR-M11-24 | SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E3.4; SC-M11-016/E8.2; SC-M11-016/E11.4; SC-M11-017/M4; SC-M11-017/E7.2; SC-M11-017/E8.2; SC-M11-017/E9.2; SC-M11-017/E10.2; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| BR-M11-25 | SC-M11-017/M2; SC-M11-017/M4; SC-M11-017/E3.2; SC-M11-017/E3.4; SC-M11-017/E4.2; SC-M11-017/E4.4; SC-M11-017/E5.2; SC-M11-017/E5.4; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| BR-M11-26 | SC-M11-014/M4; SC-M11-014/E6.4; SC-M11-015/M4; SC-M11-015/E6.4; AUT-M11-002; RULE-M11-001; RULE-M11-005 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-001 |
| BR-M11-27 | SC-M11-001/M2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E8.2; SC-M11-001/E9.2; SC-M11-001/E10.2; SC-M11-002/M2; SC-M11-002/M4; SC-M11-002/E1.2; SC-M11-002/E2.2; SC-M11-002/E3.2; SC-M11-002/E4.2; SC-M11-002/E5.2; SC-M11-002/E10.1; SC-M11-002/E13.2; SC-M11-002/E13.4; SC-M11-002/E14.2; SC-M11-002/E15.2; SC-M11-002/E16.2; SC-M11-002/E17.2; SC-M11-003/M2; SC-M11-003/E2.1; SC-M11-003/E4.2; SC-M11-003/E5.2; SC-M11-003/E6.2; SC-M11-003/E7.2; SC-M11-003/E8.2; SC-M11-004/M2; SC-M11-005/E1.2; SC-M11-005/E6.1; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E11.2; SC-M11-005/E12.2; SC-M11-005/E14.2; SC-M11-005/E15.2; SC-M11-005/E16.2; SC-M11-005/E17.2; SC-M11-006/M2; SC-M11-006/E2.1; SC-M11-006/E3.2; SC-M11-006/E4.2; SC-M11-006/E5.2; SC-M11-006/E6.2; SC-M11-006/E7.2; SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.2; SC-M11-007/E11.1; SC-M11-007/E14.2; SC-M11-008/M2; SC-M11-008/E4.1; SC-M11-008/E5.2; SC-M11-009/M2; SC-M11-009/E1.2; SC-M11-009/E4.1; SC-M11-009/E6.2; SC-M11-009/E7.2; SC-M11-009/E8.2; SC-M11-009/E9.2; SC-M11-009/E10.2; SC-M11-010/M2; SC-M11-010/M4; SC-M11-010/E1.2; SC-M11-010/E4.1; SC-M11-010/E7.2; SC-M11-010/E7.4; SC-M11-010/E8.2; SC-M11-010/E9.2; SC-M11-010/E10.2; SC-M11-010/E11.2; SC-M11-010/E12.2; SC-M11-010/E12.4; SC-M11-011/M2; SC-M11-011/E1.1; SC-M11-011/E3.1; SC-M11-011/E5.2; SC-M11-011/E6.2; SC-M11-011/E7.2; SC-M11-011/E8.2; SC-M11-011/E9.2; SC-M11-012/M2; SC-M11-012/E1.1; SC-M11-012/E3.1; SC-M11-012/E4.2; SC-M11-012/E5.2; SC-M11-012/E6.2; SC-M11-012/E7.2; SC-M11-013/M2; SC-M11-013/M4; SC-M11-013/E2.1; SC-M11-013/E4.2; SC-M11-013/E4.4; SC-M11-013/E5.2; SC-M11-013/E6.2; SC-M11-013/E7.2; SC-M11-013/E7.4; SC-M11-014/M2; SC-M11-014/M4; SC-M11-014/E3.1; SC-M11-014/E6.2; SC-M11-014/E6.4; SC-M11-014/E7.2; SC-M11-014/E8.2; SC-M11-014/E9.2; SC-M11-014/E10.2; SC-M11-015/M2; SC-M11-015/M4; SC-M11-015/E3.1; SC-M11-015/E6.2; SC-M11-015/E6.4; SC-M11-015/E7.2; SC-M11-015/E8.2; SC-M11-015/E9.2; SC-M11-016/M2; SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E3.2; SC-M11-016/E3.4; SC-M11-016/E5.1; SC-M11-016/E8.2; SC-M11-016/E11.2; SC-M11-016/E11.4; SC-M11-016/E12.2; SC-M11-016/E13.2; SC-M11-016/E14.2; SC-M11-017/M2; SC-M11-017/M4; SC-M11-017/E2.1; SC-M11-017/E3.2; SC-M11-017/E4.2; SC-M11-017/E4.4; SC-M11-017/E5.2; SC-M11-017/E7.2; SC-M11-017/E8.2; SC-M11-017/E9.2; SC-M11-017/E10.2; SC-M11-018/M2; SC-M11-018/E6.2; SC-M11-018/E7.2; SC-M11-018/E8.2; SC-M11-018/E9.2; SC-M11-018/E10.2; SC-M11-018/E11.2; SC-M11-018/E12.2; SC-M11-018/E13.2; SC-M11-018/E14.2; SC-M11-018/E15.4; SC-M11-018/E19.4; SC-M11-018/E21.1; SC-M11-018/E23.2; SC-M11-018/E24.2; SC-M11-018/E25.2; SC-M11-018/E26.2; SC-M11-018/E27.2; SC-M11-018/E28.2; SC-M11-018/E29.2; SC-M11-018/E30.2; SC-M11-018/E31.2; SC-M11-018/E32.2; SC-M11-018/E33.2; SC-M11-018/E34.2; SC-M11-018/E35.2; SC-M11-018/E36.2; SC-M11-018/E37.2; SC-M11-018/E38.2; SC-M11-019/M2; SC-M11-019/E1.1; SC-M11-019/E3.1; SC-M11-019/E5.2; SC-M11-019/E6.2; SC-M11-019/E7.2; SC-M11-019/E8.2; SC-M11-019/E9.2; SC-M11-019/E10.2; SC-M11-020/M2; SC-M11-020/E4.1; SC-M11-020/E6.1; SC-M11-020/E8.2; SC-M11-020/E9.2; SC-M11-020/E10.2; SC-M11-020/E11.2; SC-M11-020/E12.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E1.2; SC-M11-021/E2.4; SC-M11-021/E7.1; SC-M11-021/E9.2; SC-M11-021/E10.2; SC-M11-021/E11.2; SC-M11-021/E12.2; SC-M11-021/E13.2; SC-M11-021/E14.2; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E5.1; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E9.2; SC-M11-022/E10.2; SC-M11-022/E11.2; SC-M11-022/E12.2; SC-M11-022/E13.2; AUT-M11-006; RULE-M11-006 | Đã đối soát phần đủ căn cứ |
| BR-M11-28 | SC-M11-001/M2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E8.2; SC-M11-001/E9.2; SC-M11-001/E10.2; SC-M11-002/M2; SC-M11-002/M4; SC-M11-002/E1.2; SC-M11-002/E2.2; SC-M11-002/E3.2; SC-M11-002/E4.2; SC-M11-002/E5.2; SC-M11-002/E11.1; SC-M11-002/E12.1; SC-M11-002/E13.2; SC-M11-002/E13.4; SC-M11-002/E14.2; SC-M11-002/E15.2; SC-M11-002/E16.2; SC-M11-002/E17.2; SC-M11-003/M2; SC-M11-003/E3.1; SC-M11-003/E4.2; SC-M11-003/E5.2; SC-M11-003/E6.2; SC-M11-003/E7.2; SC-M11-003/E8.2; SC-M11-005/E1.2; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E11.2; SC-M11-005/E12.2; SC-M11-005/E14.2; SC-M11-005/E15.2; SC-M11-005/E16.2; SC-M11-005/E17.2; SC-M11-006/M2; SC-M11-006/E3.2; SC-M11-006/E4.2; SC-M11-006/E5.2; SC-M11-006/E6.2; SC-M11-006/E7.2; SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.2; SC-M11-007/E12.1; SC-M11-007/E14.2; SC-M11-008/M2; SC-M11-008/E5.2; SC-M11-009/M2; SC-M11-009/E1.2; SC-M11-009/E5.1; SC-M11-009/E6.2; SC-M11-009/E7.2; SC-M11-009/E8.2; SC-M11-009/E9.2; SC-M11-009/E10.2; SC-M11-010/M2; SC-M11-010/M4; SC-M11-010/E1.2; SC-M11-010/E5.1; SC-M11-010/E6.1; SC-M11-010/E7.2; SC-M11-010/E7.4; SC-M11-010/E8.2; SC-M11-010/E9.2; SC-M11-010/E10.2; SC-M11-010/E11.2; SC-M11-010/E12.2; SC-M11-010/E12.4; SC-M11-011/M2; SC-M11-011/E1.1; SC-M11-011/E4.1; SC-M11-011/E5.2; SC-M11-011/E6.2; SC-M11-011/E7.2; SC-M11-011/E8.2; SC-M11-011/E9.2; SC-M11-012/M2; SC-M11-012/E1.1; SC-M11-012/E4.2; SC-M11-012/E5.2; SC-M11-012/E6.2; SC-M11-012/E7.2; SC-M11-013/M2; SC-M11-013/M4; SC-M11-013/E3.1; SC-M11-013/E4.2; SC-M11-013/E4.4; SC-M11-013/E5.2; SC-M11-013/E6.2; SC-M11-013/E7.2; SC-M11-013/E7.4; SC-M11-014/M2; SC-M11-014/M4; SC-M11-014/E4.1; SC-M11-014/E5.1; SC-M11-014/E6.2; SC-M11-014/E6.4; SC-M11-014/E7.2; SC-M11-014/E8.2; SC-M11-014/E9.2; SC-M11-014/E10.2; SC-M11-015/M2; SC-M11-015/M4; SC-M11-015/E4.1; SC-M11-015/E5.1; SC-M11-015/E6.2; SC-M11-015/E6.4; SC-M11-015/E7.2; SC-M11-015/E8.2; SC-M11-015/E9.2; SC-M11-016/M2; SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E3.2; SC-M11-016/E3.4; SC-M11-016/E6.1; SC-M11-016/E7.1; SC-M11-016/E8.2; SC-M11-016/E11.2; SC-M11-016/E11.4; SC-M11-016/E12.2; SC-M11-016/E13.2; SC-M11-016/E14.2; SC-M11-017/M2; SC-M11-017/M4; SC-M11-017/E3.2; SC-M11-017/E4.2; SC-M11-017/E4.4; SC-M11-017/E5.2; SC-M11-017/E6.2; SC-M11-017/E7.2; SC-M11-017/E8.2; SC-M11-017/E9.2; SC-M11-017/E10.2; SC-M11-018/M2; SC-M11-018/E6.2; SC-M11-018/E7.2; SC-M11-018/E8.2; SC-M11-018/E9.2; SC-M11-018/E10.2; SC-M11-018/E11.2; SC-M11-018/E12.2; SC-M11-018/E13.2; SC-M11-018/E14.2; SC-M11-018/E15.4; SC-M11-018/E19.4; SC-M11-018/E22.1; SC-M11-018/E23.2; SC-M11-018/E24.2; SC-M11-018/E25.2; SC-M11-018/E26.2; SC-M11-018/E27.2; SC-M11-018/E28.2; SC-M11-018/E29.2; SC-M11-018/E30.2; SC-M11-018/E31.2; SC-M11-018/E32.2; SC-M11-018/E33.2; SC-M11-018/E34.2; SC-M11-018/E35.2; SC-M11-018/E36.2; SC-M11-018/E37.2; SC-M11-018/E38.2; SC-M11-019/M2; SC-M11-019/E1.1; SC-M11-019/E4.1; SC-M11-019/E5.2; SC-M11-019/E6.2; SC-M11-019/E7.2; SC-M11-019/E8.2; SC-M11-019/E9.2; SC-M11-019/E10.2; SC-M11-020/M2; SC-M11-020/E4.1; SC-M11-020/E7.1; SC-M11-020/E8.2; SC-M11-020/E9.2; SC-M11-020/E10.2; SC-M11-020/E11.2; SC-M11-020/E12.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E1.2; SC-M11-021/E2.4; SC-M11-021/E8.1; SC-M11-021/E9.2; SC-M11-021/E10.2; SC-M11-021/E11.2; SC-M11-021/E12.2; SC-M11-021/E13.2; SC-M11-021/E14.2; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E6.1; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E9.2; SC-M11-022/E10.2; SC-M11-022/E11.2; SC-M11-022/E12.2; SC-M11-022/E13.2; AUT-M11-002; AUT-M11-006; RULE-M11-006 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-004 |
| BR-M11-29 | SC-M11-001/M2; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E7.1; SC-M11-001/E8.2; SC-M11-001/E9.2; SC-M11-001/E10.2; SC-M11-002/M2; SC-M11-002/M4; SC-M11-002/E1.2; SC-M11-002/E2.2; SC-M11-002/E3.2; SC-M11-002/E4.2; SC-M11-002/E5.2; SC-M11-002/E9.1; SC-M11-002/E12.1; SC-M11-002/E13.2; SC-M11-002/E13.4; SC-M11-002/E14.2; SC-M11-002/E15.2; SC-M11-002/E16.2; SC-M11-002/E17.2; SC-M11-003/M2; SC-M11-003/E1.1; SC-M11-003/E4.2; SC-M11-003/E5.2; SC-M11-003/E6.2; SC-M11-003/E7.2; SC-M11-003/E8.2; SC-M11-004/E2.1; SC-M11-005/E1.2; SC-M11-005/E5.1; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E11.2; SC-M11-005/E12.2; SC-M11-005/E14.2; SC-M11-005/E15.2; SC-M11-005/E16.2; SC-M11-005/E17.2; SC-M11-006/M2; SC-M11-006/E1.1; SC-M11-006/E3.2; SC-M11-006/E4.2; SC-M11-006/E5.2; SC-M11-006/E6.2; SC-M11-006/E7.2; SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.2; SC-M11-007/E10.1; SC-M11-007/E14.2; SC-M11-008/M2; SC-M11-008/E3.1; SC-M11-008/E5.2; SC-M11-009/M2; SC-M11-009/E1.2; SC-M11-009/E3.1; SC-M11-009/E6.2; SC-M11-009/E7.2; SC-M11-009/E8.2; SC-M11-009/E9.2; SC-M11-009/E10.2; SC-M11-010/M2; SC-M11-010/M4; SC-M11-010/E1.2; SC-M11-010/E3.1; SC-M11-010/E6.1; SC-M11-010/E7.2; SC-M11-010/E7.4; SC-M11-010/E8.2; SC-M11-010/E9.2; SC-M11-010/E10.2; SC-M11-010/E11.2; SC-M11-010/E12.2; SC-M11-010/E12.4; SC-M11-011/M2; SC-M11-011/E1.1; SC-M11-011/E2.1; SC-M11-011/E5.2; SC-M11-011/E6.2; SC-M11-011/E7.2; SC-M11-011/E8.2; SC-M11-011/E9.2; SC-M11-012/M2; SC-M11-012/E1.1; SC-M11-012/E2.1; SC-M11-012/E4.2; SC-M11-012/E5.2; SC-M11-012/E6.2; SC-M11-012/E7.2; SC-M11-013/M2; SC-M11-013/M4; SC-M11-013/E1.1; SC-M11-013/E3.1; SC-M11-013/E4.2; SC-M11-013/E4.4; SC-M11-013/E5.2; SC-M11-013/E6.2; SC-M11-013/E7.2; SC-M11-013/E7.4; SC-M11-014/M2; SC-M11-014/M4; SC-M11-014/E2.1; SC-M11-014/E5.1; SC-M11-014/E6.2; SC-M11-014/E6.4; SC-M11-014/E7.2; SC-M11-014/E8.2; SC-M11-014/E9.2; SC-M11-014/E10.2; SC-M11-015/M2; SC-M11-015/M4; SC-M11-015/E2.1; SC-M11-015/E5.1; SC-M11-015/E6.2; SC-M11-015/E6.4; SC-M11-015/E7.2; SC-M11-015/E8.2; SC-M11-015/E9.2; SC-M11-016/M2; SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E3.2; SC-M11-016/E3.4; SC-M11-016/E4.1; SC-M11-016/E7.1; SC-M11-016/E8.2; SC-M11-016/E11.2; SC-M11-016/E11.4; SC-M11-016/E12.2; SC-M11-016/E13.2; SC-M11-016/E14.2; SC-M11-017/M2; SC-M11-017/M4; SC-M11-017/E1.1; SC-M11-017/E3.2; SC-M11-017/E4.2; SC-M11-017/E4.4; SC-M11-017/E5.2; SC-M11-017/E7.2; SC-M11-017/E8.2; SC-M11-017/E9.2; SC-M11-017/E10.2; SC-M11-018/M2; SC-M11-018/E6.2; SC-M11-018/E7.2; SC-M11-018/E8.2; SC-M11-018/E9.2; SC-M11-018/E10.2; SC-M11-018/E11.2; SC-M11-018/E12.2; SC-M11-018/E13.2; SC-M11-018/E14.2; SC-M11-018/E15.4; SC-M11-018/E19.4; SC-M11-018/E20.1; SC-M11-018/E23.2; SC-M11-018/E24.2; SC-M11-018/E25.2; SC-M11-018/E26.2; SC-M11-018/E27.2; SC-M11-018/E28.2; SC-M11-018/E29.2; SC-M11-018/E30.2; SC-M11-018/E31.2; SC-M11-018/E32.2; SC-M11-018/E33.2; SC-M11-018/E34.2; SC-M11-018/E35.2; SC-M11-018/E36.2; SC-M11-018/E37.2; SC-M11-018/E38.2; SC-M11-019/M2; SC-M11-019/E1.1; SC-M11-019/E2.1; SC-M11-019/E5.2; SC-M11-019/E6.2; SC-M11-019/E7.2; SC-M11-019/E8.2; SC-M11-019/E9.2; SC-M11-019/E10.2; SC-M11-020/M2; SC-M11-020/E4.1; SC-M11-020/E5.1; SC-M11-020/E8.2; SC-M11-020/E9.2; SC-M11-020/E10.2; SC-M11-020/E11.2; SC-M11-020/E12.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E1.2; SC-M11-021/E2.4; SC-M11-021/E6.1; SC-M11-021/E9.2; SC-M11-021/E10.2; SC-M11-021/E11.2; SC-M11-021/E12.2; SC-M11-021/E13.2; SC-M11-021/E14.2; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E4.1; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E9.2; SC-M11-022/E10.2; SC-M11-022/E11.2; SC-M11-022/E12.2; SC-M11-022/E13.2; AUT-M11-002; RULE-M11-006 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-005 |
| BR-M11-30 | SC-M11-005/E4.1; SC-M11-005/E17.2; SC-M11-022/M2; SC-M11-022/E1.2; SC-M11-022/E7.2; SC-M11-022/E8.2; SC-M11-022/E13.2; RULE-M11-002; RULE-M11-005 | Đã đối soát phần đủ căn cứ |
| BR-M11-31 | SC-M11-001/M1; SC-M11-001/M2; SC-M11-001/E2.2; SC-M11-001/E3.2; SC-M11-001/E4.2; SC-M11-001/E5.1; SC-M11-001/E5.2; SC-M11-001/E6.2; SC-M11-001/E10.1; SC-M11-001/E10.2; SC-M11-002/M3; SC-M11-002/M4; SC-M11-002/E6.2; SC-M11-002/E7.2; SC-M11-002/E8.2; SC-M11-002/E13.3; SC-M11-002/E13.4; RULE-M11-001 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-002 |
| BR-M11-32 | SC-M11-002/M4; SC-M11-002/E1.1; SC-M11-002/E1.2; SC-M11-002/E2.1; SC-M11-002/E2.2; SC-M11-002/E3.1; SC-M11-002/E3.2; SC-M11-002/E13.4; AUT-M11-001; RULE-M11-003 | Đã đối soát phần đủ căn cứ |
| BR-M11-33 | SC-M11-005/M2; SC-M11-005/E7.2; SC-M11-005/E8.2; SC-M11-005/E9.2; SC-M11-005/E10.2; SC-M11-005/E11.2; SC-M11-005/E12.2; SC-M11-005/E13.2; SC-M11-005/E14.2; SC-M11-005/E15.2; SC-M11-019/M2; SC-M11-019/E5.2; SC-M11-019/E6.1; SC-M11-019/E6.2; SC-M11-019/E7.1; SC-M11-019/E7.2; SC-M11-019/E8.1; SC-M11-019/E8.2; SC-M11-019/E9.1; SC-M11-019/E9.2; SC-M11-019/E10.2; SC-M11-020/M2; SC-M11-020/E3.1; SC-M11-020/E8.2; SC-M11-020/E9.1; SC-M11-020/E9.2; SC-M11-020/E10.1; SC-M11-020/E10.2; SC-M11-020/E11.1; SC-M11-020/E11.2; SC-M11-020/E12.1; SC-M11-020/E12.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E9.2; SC-M11-021/E10.1; SC-M11-021/E10.2; SC-M11-021/E11.1; SC-M11-021/E11.2; SC-M11-021/E12.1; SC-M11-021/E12.2; SC-M11-021/E13.1; SC-M11-021/E13.2; SC-M11-021/E14.2; RULE-M11-001; RULE-M11-002 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-008 |
| BR-M11-34 | SC-M11-006/M2; SC-M11-006/E3.2; SC-M11-006/E4.2; SC-M11-006/E5.2; SC-M11-006/E6.2; SC-M11-006/E7.2; SC-M11-014/M2; SC-M11-014/E6.2; SC-M11-015/M2; SC-M11-015/E6.2; SC-M11-016/M2; SC-M11-016/E3.2; SC-M11-016/E11.2; SC-M11-017/M2; SC-M11-017/E3.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| BR-M11-35 | SC-M11-004/M2; SC-M11-004/E1.1; SC-M11-004/E2.1; SC-M11-004/E3.2; RULE-M11-002 | Đã đối soát phần đủ căn cứ |
| BR-M11-36 | SC-M11-008/M2; SC-M11-008/E1.1; SC-M11-008/E2.2; SC-M11-008/E5.2; RULE-M11-003 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-004 |
| BR-M11-37 | SC-M11-002/E1.2; SC-M11-002/E2.2; SC-M11-007/M2; SC-M11-007/E1.1; SC-M11-007/E1.2; SC-M11-007/E1.3; SC-M11-007/E1.4; SC-M11-007/E2.1; SC-M11-007/E2.2; SC-M11-007/E3.1; SC-M11-007/E3.2; SC-M11-007/E3.3; SC-M11-007/E3.4; SC-M11-007/E4.1; SC-M11-007/E4.2; SC-M11-007/E4.5; SC-M11-007/E4.6; SC-M11-007/E9.2; SC-M11-007/E14.2; SC-M11-009/M2; SC-M11-009/E6.2; SC-M11-010/M4; SC-M11-010/E1.2; SC-M11-010/E7.4; SC-M11-010/E12.4; SC-M11-011/M2; SC-M11-011/E5.2; SC-M11-011/E9.2; SC-M11-014/M4; SC-M11-014/E6.4; SC-M11-015/M4; SC-M11-015/E6.4; SC-M11-016/M4; SC-M11-016/E1.2; SC-M11-016/E3.4; SC-M11-016/E8.2; SC-M11-016/E11.4; SC-M11-017/M4; AUT-M11-001; AUT-M11-002; AUT-M11-005; RULE-M11-003 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-007 |
| BR-M11-38 | SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.4; SC-M11-018/E7.6; SC-M11-018/E8.6; SC-M11-018/E9.2; SC-M11-018/E10.2; SC-M11-018/E11.4; SC-M11-018/E12.4; SC-M11-018/E13.4; SC-M11-018/E14.4; SC-M11-018/E15.6; SC-M11-018/E19.6; SC-M11-018/E23.2; SC-M11-018/E24.4; SC-M11-018/E25.4; SC-M11-018/E26.4; SC-M11-018/E27.4; SC-M11-018/E28.4; SC-M11-018/E29.6; SC-M11-018/E30.2; SC-M11-018/E31.6; SC-M11-018/E32.2; SC-M11-018/E33.2; SC-M11-018/E34.2; SC-M11-021/E1.2; SC-M11-021/E2.2; SC-M11-021/E2.4; AUT-M11-004; RULE-M11-004 | Đã đối soát phần đủ căn cứ |
| BR-M11-39 | SC-M11-019/M2; SC-M11-019/E5.2; SC-M11-019/E10.2; SC-M11-020/M2; SC-M11-020/E2.2; SC-M11-020/E4.1; SC-M11-020/E8.2; SC-M11-020/E13.2; SC-M11-021/M2; SC-M11-021/E1.2; SC-M11-021/E2.4; SC-M11-021/E5.2; SC-M11-021/E9.2; SC-M11-021/E14.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-006 |
| BR-M11-40 | SC-M11-018/M1; SC-M11-018/M2; SC-M11-018/M4; SC-M11-018/E1.2; SC-M11-018/E2.2; SC-M11-018/E3.2; SC-M11-018/E4.2; SC-M11-018/E5.2; SC-M11-018/E6.1; SC-M11-018/E6.2; SC-M11-018/E6.4; SC-M11-018/E7.1; SC-M11-018/E7.2; SC-M11-018/E7.6; SC-M11-018/E8.1; SC-M11-018/E8.2; SC-M11-018/E8.6; SC-M11-018/E9.1; SC-M11-018/E9.2; SC-M11-018/E10.1; SC-M11-018/E10.2; SC-M11-018/E11.1; SC-M11-018/E11.2; SC-M11-018/E11.4; SC-M11-018/E12.1; SC-M11-018/E12.2; SC-M11-018/E12.4; SC-M11-018/E13.1; SC-M11-018/E13.2; SC-M11-018/E13.4; SC-M11-018/E14.1; SC-M11-018/E14.2; SC-M11-018/E14.4; SC-M11-018/E15.3; SC-M11-018/E15.4; SC-M11-018/E15.6; SC-M11-018/E19.3; SC-M11-018/E19.4; SC-M11-018/E19.6; SC-M11-018/E23.1; SC-M11-018/E23.2; SC-M11-018/E24.1; SC-M11-018/E24.2; SC-M11-018/E24.4; SC-M11-018/E25.1; SC-M11-018/E25.2; SC-M11-018/E25.4; SC-M11-018/E26.1; SC-M11-018/E26.2; SC-M11-018/E26.4; SC-M11-018/E27.1; SC-M11-018/E27.2; SC-M11-018/E27.4; SC-M11-018/E28.1; SC-M11-018/E28.2; SC-M11-018/E28.4; SC-M11-018/E29.1; SC-M11-018/E29.2; SC-M11-018/E29.6; SC-M11-018/E30.1; SC-M11-018/E30.2; SC-M11-018/E31.1; SC-M11-018/E31.2; SC-M11-018/E31.6; SC-M11-018/E32.1; SC-M11-018/E32.2; SC-M11-018/E33.1; SC-M11-018/E33.2; SC-M11-018/E34.1; SC-M11-018/E34.2; RULE-M11-004 | Đã đối soát phần đủ căn cứ; giới hạn GAP-SC-M11-006, GAP-SC-M11-008 |


| UC owner | Guard/lựa chọn | SC/nhánh | Đích |
|---|---|---|---|
| UC-M11-001 | Phúc đã tạo đủ 5 nhóm trong 24 giờ ngay trước T, trong đó một nhóm đã xóa | SC-M11-001/E1 | END:REJECTED |
| UC-M11-001 | Dữ liệu tên trống; người dùng sửa về bộ hợp lệ | SC-M11-001/E2 | M2 |
| UC-M11-001 | Dữ liệu tên gồm101 chữ A; người dùng sửa về bộ hợp lệ | SC-M11-001/E3 | M2 |
| UC-M11-001 | Dữ liệu mô tả gồm501 chữ B; người dùng sửa về bộ hợp lệ | SC-M11-001/E4 | M2 |
| UC-M11-001 | Người tạo đặt ngay cấu hình và dùng biên100/500 ASCII | SC-M11-001/E5 | END:SUCCESS |
| UC-M11-001 | Nhóm tạo cũ đúng T−24h rời cửa sổ, không giới hạn tổng40 nhóm sở hữu | SC-M11-001/E6 | END:SUCCESS |
| UC-M11-001 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-001/E7 | END:REJECTED |
| UC-M11-002 | Private→Public không câu hỏi khiến nhóm thành vào ngay | SC-M11-002/E1 | END:SUCCESS |
| UC-M11-002 | Bỏ câu hỏi của Public khiến nhóm thành vào ngay | SC-M11-002/E2 | END:SUCCESS |
| UC-M11-002 | Owner chỉ đổi Câu hỏi=Bạn muốn ôn phần nào? | SC-M11-002/E3 | END:SUCCESS |
| UC-M11-002 | Owner chỉ đổi Duyệt trước=Bật | SC-M11-002/E4 | END:SUCCESS |
| UC-M11-002 | Owner chỉ đổi Ẩn danh=Bật | SC-M11-002/E5 | END:SUCCESS |
| UC-M11-002 | Owner lưu tên trống rồi sửa | SC-M11-002/E6 | M4 |
| UC-M11-002 | Owner lưu tên101 chữ A rồi sửa | SC-M11-002/E7 | M4 |
| UC-M11-002 | Owner lưu mô tả501 chữ B rồi sửa | SC-M11-002/E8 | M4 |
| UC-M11-002 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-002/E9 | END:REJECTED |
| UC-M11-002 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-002/E10 | END:REJECTED |
| UC-M11-002 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | SC-M11-002/E11 | END:REJECTED |
| UC-M11-002 | Nhóm chuyển Bị khóa hoặc cờ Group Tắt với người không ADMIN sau lượt đọc nhưng trước lúc lưu | SC-M11-002/E12 | END:REJECTED |
| UC-M11-003 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-003/E1 | END:REJECTED |
| UC-M11-003 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-003/E2 | END:REJECTED |
| UC-M11-003 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | SC-M11-003/E3 | END:REJECTED |
| UC-M11-004 | Không có nhóm nào còn đủ điều kiện hiển thị | SC-M11-004/E1 | END:SUCCESS |
| UC-M11-004 | Cờ Group Tắt, Guest vẫn xem danh sách như lối vào | SC-M11-004/E2 | END:SUCCESS |
| UC-M11-005 | Guest mở link mời của N12 Private chỉ để đọc giới thiệu | SC-M11-005/E1 | END:SUCCESS |
| UC-M11-005 | N11 đã là Private ở lúc Guest mở bằng link thường/bookmark/thông báo | SC-M11-005/E2 | END:REJECTED |
| UC-M11-005 | N11 chuyển Public→Private sau lần tải trước, Guest tải lại/mở lại nội dung | SC-M11-005/E3 | END:REJECTED |
| UC-M11-005 | P11 đã bị gỡ khỏi nhóm; Guest không thuộc tập xem còn lại | SC-M11-005/E4 | END:REJECTED |
| UC-M11-005 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-005/E5 | END:REJECTED |
| UC-M11-005 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-005/E6 | END:REJECTED |
| UC-M11-006 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-006/E1 | END:REJECTED |
| UC-M11-006 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-006/E2 | END:REJECTED |
| UC-M11-007 | Public có câu hỏi cần gửi yêu cầu | SC-M11-007/E1 | END:SUCCESS |
| UC-M11-007 | Private không câu hỏi cần gửi yêu cầu | SC-M11-007/E2 | END:SUCCESS |
| UC-M11-007 | Private có câu hỏi cần gửi yêu cầu | SC-M11-007/E3 | END:SUCCESS |
| UC-M11-007 | Nhóm có câu hỏi, Phúc gửi trống rồi bổ sung câu trả lời | SC-M11-007/E4 | END:SUCCESS |
| UC-M11-007 | Phúc đang có R11 Chờ duyệt tới N11 | SC-M11-007/E5 | END:REJECTED |
| UC-M11-007 | Phúc đang bị N11 chặn và vào bằng vào ngay | SC-M11-007/E6 | END:REJECTED |
| UC-M11-007 | Phúc đang bị N11 chặn và vào bằng gửi yêu cầu | SC-M11-007/E7 | END:REJECTED |
| UC-M11-007 | Phúc đang bị N11 chặn và vào bằng LINK-N11/lời mời | SC-M11-007/E8 | END:REJECTED |
| UC-M11-007 | Phúc từng bị từ chối/rời/kick, không bị chặn và quay lại ngay | SC-M11-007/E9 | END:SUCCESS |
| UC-M11-007 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-007/E10 | END:REJECTED |
| UC-M11-007 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-007/E11 | END:REJECTED |
| UC-M11-007 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | SC-M11-007/E12 | END:REJECTED |
| UC-M11-008 | R11 đã Đã chấp nhận/Đã từ chối/Đã rút khi xử lý | SC-M11-008/E1 | END:REJECTED |
| UC-M11-008 | Phúc yêu cầu rút R-other của Xuân | SC-M11-008/E2 | END:REJECTED |
| UC-M11-008 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-008/E3 | END:REJECTED |
| UC-M11-008 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-008/E4 | END:REJECTED |
| UC-M11-009 | Chi chọn lấy link chung thay vì mời một người cụ thể | SC-M11-009/E1 | END:SUCCESS |
| UC-M11-009 | Chi muốn thu hồi hoặc tạo lại link mời | SC-M11-009/E2 | END:REJECTED |
| UC-M11-009 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-009/E3 | END:REJECTED |
| UC-M11-009 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-009/E4 | END:REJECTED |
| UC-M11-009 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | SC-M11-009/E5 | END:REJECTED |
| UC-M11-010 | Bình chọn Từ chối R11 đang Chờ duyệt | SC-M11-010/E1 | END:SUCCESS |
| UC-M11-010 | R11 đã được xử lý/rút trước lúc nhận quyết định | SC-M11-010/E2 | END:REJECTED |
| UC-M11-010 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-010/E3 | END:REJECTED |
| UC-M11-010 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-010/E4 | END:REJECTED |
| UC-M11-010 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | SC-M11-010/E5 | END:REJECTED |
| UC-M11-010 | Nhóm chuyển Bị khóa hoặc cờ Group Tắt với người không ADMIN sau lượt đọc nhưng trước lúc lưu | SC-M11-010/E6 | END:REJECTED |
| UC-M11-011 | Phúc là người gửi cũ, hiện không có yêu cầu Chờ duyệt | SC-M11-011/E1 | END:SUCCESS |
| UC-M11-011 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-011/E2 | END:REJECTED |
| UC-M11-011 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-011/E3 | END:REJECTED |
| UC-M11-011 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | SC-M11-011/E4 | END:REJECTED |
| UC-M11-011 | Danh sách chặn N12 hiện rỗng | SC-M11-012/E1 | END:SUCCESS |
| UC-M11-011 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-012/E2 | END:REJECTED |
| UC-M11-011 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-012/E3 | END:REJECTED |
| UC-M11-011 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-013/E1 | END:REJECTED |
| UC-M11-011 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-013/E2 | END:REJECTED |
| UC-M11-011 | Nhóm chuyển Bị khóa hoặc cờ Group Tắt với người không ADMIN sau lượt đọc nhưng trước lúc lưu | SC-M11-013/E3 | END:REJECTED |
| UC-M11-012 | Đích đã không còn thuộc vai trò nguồn Member tại lúc xử lý | SC-M11-014/E1 | END:REJECTED |
| UC-M11-012 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-014/E2 | END:REJECTED |
| UC-M11-012 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-014/E3 | END:REJECTED |
| UC-M11-012 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | SC-M11-014/E4 | END:REJECTED |
| UC-M11-012 | Nhóm chuyển Bị khóa hoặc cờ Group Tắt với người không ADMIN sau lượt đọc nhưng trước lúc lưu | SC-M11-014/E5 | END:REJECTED |
| UC-M11-012 | Đích đã không còn thuộc vai trò nguồn Group Mod tại lúc xử lý | SC-M11-015/E1 | END:REJECTED |
| UC-M11-012 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-015/E2 | END:REJECTED |
| UC-M11-012 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-015/E3 | END:REJECTED |
| UC-M11-012 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | SC-M11-015/E4 | END:REJECTED |
| UC-M11-012 | Nhóm chuyển Bị khóa hoặc cờ Group Tắt với người không ADMIN sau lượt đọc nhưng trước lúc lưu | SC-M11-015/E5 | END:REJECTED |
| UC-M11-013 | Owner chọn kick Bình Group Mod thay vì Chi Member | SC-M11-016/E1 | END:SUCCESS |
| UC-M11-013 | Đích đã thành Owner trước lúc xử lý | SC-M11-016/E2 | END:REJECTED |
| UC-M11-013 | Owner kick thành viên ở nhóm Private, hệ quả quyền sau kick khác Public | SC-M11-016/E3 | END:SUCCESS |
| UC-M11-013 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-016/E4 | END:REJECTED |
| UC-M11-013 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-016/E5 | END:REJECTED |
| UC-M11-013 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | SC-M11-016/E6 | END:REJECTED |
| UC-M11-013 | Nhóm chuyển Bị khóa hoặc cờ Group Tắt với người không ADMIN sau lượt đọc nhưng trước lúc lưu | SC-M11-016/E7 | END:REJECTED |
| UC-M11-014 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-017/E1 | END:REJECTED |
| UC-M11-014 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-017/E2 | END:REJECTED |
| UC-M11-014 | Owner còn người nhưng chưa chọn kế nhiệm khi xác nhận rời | SC-M11-017/E3 | END:REJECTED |
| UC-M11-014 | Owner cuối chọn rời, xác nhận cảnh báo xóa | SC-M11-017/E4 | END:SUCCESS |
| UC-M11-014 | Owner cuối không xác nhận cảnh báo xóa | SC-M11-017/E5 | END:CANCELLED |
| UC-M11-014 | Owner muốn rời khi nhóm Bị khóa | SC-M11-017/E6 | END:REJECTED |
| UC-M11-033 | AI trả điểm 0.49; Chi không Owner, duyệt trước Tắt | SC-M11-018/E1 | END:SUCCESS |
| UC-M11-033 | AI trả điểm 0.5; Chi không Owner, duyệt trước Tắt | SC-M11-018/E2 | END:SUCCESS |
| UC-M11-033 | AI trả điểm 0.89; Chi không Owner, duyệt trước Tắt | SC-M11-018/E3 | END:SUCCESS |
| UC-M11-033 | AI trả điểm 0.9; Chi không Owner, duyệt trước Tắt | SC-M11-018/E4 | END:REJECTED |
| UC-M11-033 | AI trả điểm 0.95; Chi không Owner, duyệt trước Tắt | SC-M11-018/E5 | END:REJECTED |
| UC-M11-033 | Duyệt trước Bật, điểm0.3 vẫn chờ nhóm | SC-M11-018/E6 | END:SUCCESS |
| UC-M11-033 | Lần đầu lỗi, sau 2 giây thử lại đúng một lần trả0.3 | SC-M11-018/E7 | END:SUCCESS |
| UC-M11-033 | Cả hai lần quét lỗi, duyệt trước Tắt vẫn chờ nhóm | SC-M11-018/E8 | END:SUCCESS |
| UC-M11-033 | AI tổng hoặc Moderation Tắt, duyệt trước Tắt đăng ngay | SC-M11-018/E9 | END:SUCCESS |
| UC-M11-033 | AI tổng hoặc Moderation Tắt, duyệt trước Bật chờ nhóm | SC-M11-018/E10 | END:SUCCESS |
| UC-M11-033 | N12 Private, bài được đăng chỉ trong nhóm/tab Group | SC-M11-018/E11 | END:SUCCESS |
| UC-M11-033 | Chi không chọn ẩn danh khi công tắc Bật | SC-M11-018/E12 | END:SUCCESS |
| UC-M11-033 | Tác giả đã sửa bài Bị từ chối cấp nhóm và gửi lại, cổng chạy thêm một lần | SC-M11-018/E13 | END:SUCCESS |
| UC-M11-033 | Tác giả đã sửa bài Bị AI từ chối và gửi lại, không chờ kết luận khiếu nại để gửi | SC-M11-018/E14 | END:SUCCESS |
| UC-M11-033 | Công tắc ẩn danh Tắt, Chi bỏ lựa chọn ẩn danh rồi gửi hợp lệ | SC-M11-018/E15 | END:SUCCESS |
| UC-M11-033 | P18 không còn Nháp/Bị từ chối | SC-M11-018/E16 | END:REJECTED |
| UC-M11-033 | Chi bị cảnh cáo MEDIUM hoặc HEAVY | SC-M11-018/E17 | END:REJECTED |
| UC-M11-033 | Người gửi không phải tác giả của P18 | SC-M11-018/E18 | END:REJECTED |
| UC-M11-033 | Tiêu đề thiếu hoặc nội dung/poll thiếu, tác giả bổ sung rồi gửi | SC-M11-018/E19 | END:SUCCESS |
| UC-M11-033 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-018/E20 | END:REJECTED |
| UC-M11-033 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-018/E21 | END:REJECTED |
| UC-M11-033 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | SC-M11-018/E22 | END:REJECTED |
| UC-M11-033 | Dịch vụ AI im lặng cả hai lần, duyệt trước Tắt | SC-M11-018/E23 | END:SUCCESS |
| UC-M11-017 | Queue nhóm hiện không có bài nào chờ | SC-M11-019/E1 | END:SUCCESS |
| UC-M11-017 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-019/E2 | END:REJECTED |
| UC-M11-017 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-019/E3 | END:REJECTED |
| UC-M11-017 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | SC-M11-019/E4 | END:REJECTED |
| UC-M11-018 | P19 đang được Dũng giữ, chưa đủ 30 phút không thao tác | SC-M11-020/E1 | END:REJECTED |
| UC-M11-018 | Bình muốn nhận chính P20 của mình | SC-M11-020/E2 | END:REJECTED |
| UC-M11-018 | P19 không còn ở hàng chờ nhóm N11 | SC-M11-020/E3 | END:REJECTED |
| UC-M11-018 | Holder cũ đã tự nhả đủ 30 phút trước yêu cầu nhận của Bình | SC-M11-020/E4 | END:SUCCESS |
| UC-M11-018 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-020/E5 | END:REJECTED |
| UC-M11-018 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-020/E6 | END:REJECTED |
| UC-M11-018 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | SC-M11-020/E7 | END:REJECTED |
| UC-M11-019 | Bình chọn Từ chối bài kèm lý do | SC-M11-021/E1 | END:SUCCESS |
| UC-M11-019 | Bình chọn Từ chối thiếu lý do rồi bổ sung | SC-M11-021/E2 | END:SUCCESS |
| UC-M11-019 | Bình khác holder Dũng hoặc bài đã tự nhả trước lúc xử lý | SC-M11-021/E3 | END:REJECTED |
| UC-M11-019 | Bình đã bị giáng Group Mod trước khi gửi quyết định | SC-M11-021/E4 | END:REJECTED |
| UC-M11-019 | Bình Group Mod cố chấp nhận hoặc từ chối P20 của mình | SC-M11-021/E5 | END:REJECTED |
| UC-M11-019 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-021/E6 | END:REJECTED |
| UC-M11-019 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-021/E7 | END:REJECTED |
| UC-M11-019 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | SC-M11-021/E8 | END:REJECTED |
| UC-M11-020 | Bình chọn gỡ bình luận C11 của Chi thay vì bài P11 | SC-M11-022/E1 | END:SUCCESS |
| UC-M11-020 | Bình Group Mod gỡ nội dung của An Owner | SC-M11-022/E2 | END:REJECTED |
| UC-M11-020 | Bình Group Mod gỡ nội dung của Dũng Group Mod | SC-M11-022/E3 | END:REJECTED |
| UC-M11-020 | Cờ Group Tắt và người yêu cầu không có vai trò hệ thống ADMIN | SC-M11-022/E4 | END:REJECTED |
| UC-M11-020 | Nhóm đích Đã xóa hoặc Bị ẩn tại lúc mở/thực hiện | SC-M11-022/E5 | END:REJECTED |
| UC-M11-020 | Nhóm đích Bị khóa, hành vi này thuộc tập bị chặn | SC-M11-022/E6 | END:REJECTED |


| Lớp tổ hợp | Đường khả thi/ranh giới |
|---|---|
| Hạn tạo | 4→5 nhận;5→6 từ chối kể cả đã xóa/Admin; đúng 24h không tính, tổng40 sở hữu không chặn |
| Đổi cài đặt | Public→Private giữ bản đang hiện chỉ đọc; Private→Public không câu hỏi hoặc bỏ câu hỏi Public tự nhận mọi yêu cầu chờ; đổi câu hỏi khác không nhận; tắt duyệt không nhả bài, tắt ẩn danh giữ bài cũ |
| Gia nhập | Bốn tổ hợp Public/Private×có/không câu hỏi; trống rồi bổ sung, trùng Chờ duyệt, bị chặn mọi lối, sau từ chối/kick/rời quay lại, Guest cần đăng nhập |
| Role nhóm | Member/Group Mod/Owner khác vai trò hệ thống; Owner kick Group Mod, Group Mod không kick/gỡ ngang hoặc cao; Owner/Group Mod kiểm duyệt vẫn đúng holder |
| Rời | Member/Group Mod ở Public/Private/Bị khóa; Owner còn người chọn/xác nhận/chuyển trước-ra sau; thiếu chọn bị từ chối; Owner cuối xác nhận xóa hoặc không xác nhận giữ; Owner Bị khóa bị từ chối |
| Cổng bài | Điểm0.49/0.5/0.89/0.9/0.95; duyệt trước Bật/Tắt; AI tổng/Moderation Tắt khác lỗi/timeout sau một retry; Owner vào Mod hệ thống khi điểm trung bình/lỗi; Admin Member vẫn theo duyệt trước, Admin Owner đăng ngay |
| Queue | Xem bài mình không nhận; nhận khi trống, không chiếm người giữ; nhả đủ 30 phút rồi nhận lại; đúng holder còn quyền mới kết luận; thiếu lý do bổ sung tới kết quả; Group Mod không tự nhận/chấp nhận/từ chối |
| Gỡ/xóa | Loại đích bài/bình luận có đường đầy đủ; dấu gỡ giữ trạng thái đăng/dữ liệu/điểm, có thông báo/tập xem riêng; xóa nhóm không hiện ai, giữ dữ liệu/điểm, không đồng nhất với gỡ/ẩn |
| Cờ/Khóa | Cờ Tắt giữ danh sách/lối vào, chặn mở/tương tác người khôngAdmin, Admin vẫn quyền nhóm/Khóa; đọc cũ khi Khóa và tự rời Member/Group Mod còn cho; tựkế nhiệm/kiểmduyệt vẫn chạy, bật lại không bù |
| Không nhân vô hạn | Tên/ID/nội dung hợp lệ khác nhau dùng cùng hợp đồng; vòng sửa/gửi lại và thử dữ liệu biểu diễn một chu kỳ có điểm thoát. Tổ hợp thay kết quả có đường riêng; tổ hợp thiếu nguồn không được gán kết quả giả. |


227 mã hiệu lực =17 nhóm +170 FR chi tiết +40 BR; không mã bỏ. Truy vết ngược tại sources từng bước; số lượng mã có vị trí không thay review ngữ nghĩa hoặc làm 8 GAP thành đã chốt.

## 7. GAP và giới hạn nguồn

| ID | Nguồn/phạm vi | Giới hạn/cách giữ phạm vi |
|---|---|---|
| GAP-SC-M11-001 | NOTE-M11-01; FR-M11-11.01, FR-M11-11.02, BR-M11-26 | AUT002: hòa thời điểm bổ nhiệm/tham gia hoặc trạng thái tài khoản ứng viên kế nhiệm chưa chốt. Chỉ minh họa ứng viên có mốc khác nhau; không tự tie-break/lọc ACTIVE. Chặn đúng trường hợp ứng viên chưa xác định. |
| GAP-SC-M11-002 | NOTE-M11-02; FR-M11-01.08, FR-M11-01.09, FR-M11-02.11, BR-M11-31, BR-M11-08 | SC001/002/007/010: đơn vị Unicode/trim, độ dài câu hỏi/câu trả lời và phiên bản câu hỏi sau sửa chưa chốt. Biên dùng ASCII100/101 và500/501, không tự trim/chặn dài câu hỏi/snapshot câu cũ. |
| GAP-SC-M11-003 | NOTE-M11-03; BR-M11-05, FR-M11-14.08, FR-M11-14.01 | SC022: dùng quyền nhóm gỡ chính nội dung mình chưa rõ. Không tạo nhánh cho/chặn giả; quyền sửa/xóa của tác giả vẫn theo M03/M04, không đồng nghĩa gỡ nhóm. |
| GAP-SC-M11-004 | NOTE-M11-04; BR-M11-28, BR-M11-36, FR-M11-07.04 | SC008/012 và lượt xem danh sách của SC013: rút yêu cầu/đọc danh sách chặn khi nhóm Bị khóa chưa chốt. Không tự gán terminal SUCCESS/REJECTED cho hai trường hợp thiếu nguồn; bỏ chặn khi Khóa đã rõ là bị chặn. |
| GAP-SC-M11-005 | NOTE-M11-05; FR-M11-17.01, FR-M11-17.07, FR-M11-17.08, BR-M11-29 | SC004/UC024: câu chặn mọi thao tác so với vẫn hiện danh sách/lối vào. Áp dòng cụ thể17.07: liệt kê còn theo quyền, mở/tương tác bị chặn với người không ADMIN. Không chặn phần đã rõ; cần xác nhận cách diễn đạt nguồn, không coi list là mởPrivate. |
| GAP-SC-M11-006 | NOTE-M11-06; FR-M11-02.05, FR-M11-02.15, FR-M11-13.14, BR-M11-20, BR-M11-39, BR-M11-40, BR-M03-46 | SC018/020/021, AUT003/004: nhóm/Owner/role thay đổi giữa lúc AI/duyệt/khiếu nại chờ, Group Mod có bài chờ rồi thànhOwner, mất role holder chưa đủ hợp đồng. Kiểm quyền hiện tại, không tự nhả sớm/chuyển queue/xả bài; giữ ngoại lệ đã gửi lại không ghi đè. |
| GAP-SC-M11-007 | NOTE-M11-07; FR-M11-10.04, FR-M11-02.14, FR-M11-15.01, BR-M11-37 | SC002/003/017 và các nhánh phát sự kiện: giao dịch/thất bại/thứ tự phát, chấp nhận hàng loạt/đồng thời chưa chốt. Giữ thứ tự chuyển Owner trước khi đưa người cũ ra theo nguồn, không bịa atomicity/rollback/retry/outbox/thông báo lỗi. |
| GAP-SC-M11-008 | NOTE-M11-08; BR-M11-33, BR-M11-40, FR-M03-06.01, FR-M03-07.02, FR-M09-06.04, FR-M09-06.05 | SC005/AUT004: giao tiếp Private trong ngữ cảnh xét khiếu nại M09 chưa có mô tả tương ứng đủ rõ ở M11. Giữ quyền ngữ cảnh owner M09/M03/M08, không biến cấm mở trang thường thành cấm xét hợp lệ hoặc tự cho xem toàn Private. |


GAP005 ghi cách áp yêu cầu cụ thể đã có, không chặn liệt kê lối vào. Các GAP khác chặn đúng tình huống chưa có hợp đồng, không dừng các đường độc lập đủ căn cứ. TBD-M11-01 đã đóng, không mở lại. [QA-M11.md](QA-M11.md) ghi lệnh kiểm và kết quả thực tế; chưa có phê duyệt stakeholder.


## Chuyển đổi ID nhánh sau QA-SC-01

Ngày 11/11/2026, các biến thể vai trò được đăng ký thành E tại M1 theo skill v1.4. Bảng này giữ ID lịch sử để đối chiếu các tài liệu đã dẫn V. Mỗi hàng ánh xạ cả nhánh và các bước cùng số thứ tự, ví dụ V1.2 sang bước .2 của E tương ứng.

| ID lịch sử | ID hiện hành | Điểm thay | Số bước | Nguồn |
| --- | --- | --- | --- | --- |
| SC-M11-001/V1 | SC-M11-001/E8 | M1 | 2 | FR-M11-01.04, FR-M11-01.03, FR-M11-01.07, BR-M11-03, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-001/V2 | SC-M11-001/E9 | M1 | 2 | FR-M11-01.07, FR-M11-01.03, FR-M11-01.04, BR-M11-03, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-001/V3 | SC-M11-001/E10 | M1 | 2 | FR-M11-01.01, FR-M11-01.10, FR-M11-01.11, FR-M11-01.12, BR-M11-31, FR-M11-17.03, FR-M10-12.08, FR-M11-01.02, FR-M11-01.03, FR-M11-01.05, FR-M11-01.06, FR-M11-01.08, FR-M11-01.09, FR-M11-05.06, BR-M11-02, BR-M11-03, BR-M11-04, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-002/V1 | SC-M11-002/E13 | M1 | 4 | FR-M11-02.01, FR-M11-02.02, FR-M11-17.03, FR-M10-12.08, FR-M11-02.09, FR-M11-02.10, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-02.05, FR-M11-02.06, FR-M11-02.07, FR-M11-02.08, BR-M11-31, FR-M11-02.03, FR-M11-02.04, FR-M11-02.11, FR-M11-02.12, FR-M11-02.13, FR-M11-02.14, FR-M11-02.15, BR-M11-08, BR-M11-15, BR-M11-16, BR-M11-18, BR-M11-32 |
| SC-M11-002/V2 | SC-M11-002/E14 | M1 | 2 | FR-M11-02.09, FR-M11-02.10, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-002/V3 | SC-M11-002/E15 | M1 | 2 | FR-M11-02.09, FR-M11-02.10, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-002/V4 | SC-M11-002/E16 | M1 | 2 | FR-M11-02.09, FR-M11-02.10, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-002/V5 | SC-M11-002/E17 | M1 | 2 | FR-M11-02.09, FR-M11-02.10, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-003/V1 | SC-M11-003/E4 | M1 | 2 | FR-M11-15.01, FR-M11-17.03, FR-M10-12.08, FR-M11-15.02, FR-M11-15.03, FR-M11-15.05, BR-M11-23, FR-M12-02.14, FR-M11-15.04, FR-M11-01.06, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-003/V2 | SC-M11-003/E5 | M1 | 2 | FR-M11-15.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-003/V3 | SC-M11-003/E6 | M1 | 2 | FR-M11-15.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-003/V4 | SC-M11-003/E7 | M1 | 2 | FR-M11-15.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-003/V5 | SC-M11-003/E8 | M1 | 2 | FR-M11-15.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-004/V1 | SC-M11-004/E3 | M1 | 2 | FR-M11-03.03, FR-M11-03.16, FR-M11-03.01, FR-M11-03.02, FR-M11-03.17, FR-M11-17.07, BR-M11-11, BR-M11-35 |
| SC-M11-005/V1 | SC-M11-005/E7 | M1 | 2 | FR-M11-03.05, FR-M11-03.04, FR-M11-03.06, FR-M11-03.09, FR-M11-03.10, FR-M11-03.11, FR-M11-03.12, FR-M11-03.18, BR-M11-13, BR-M11-14, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-005/V2 | SC-M11-005/E8 | M1 | 2 | FR-M11-03.05, FR-M11-03.04, FR-M11-03.06, FR-M11-03.09, FR-M11-03.10, FR-M11-03.11, FR-M11-03.12, FR-M11-03.18, BR-M11-13, BR-M11-14, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-005/V3 | SC-M11-005/E9 | M1 | 2 | FR-M11-03.05, FR-M11-03.04, FR-M11-03.06, FR-M11-03.09, FR-M11-03.10, FR-M11-03.11, FR-M11-03.12, FR-M11-03.18, BR-M11-13, BR-M11-14, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-005/V4 | SC-M11-005/E10 | M1 | 2 | FR-M11-03.12, FR-M11-03.10, BR-M11-17, BR-M11-33, FR-M08-04.06 |
| SC-M11-005/V5 | SC-M11-005/E11 | M1 | 2 | FR-M11-03.11, FR-M11-03.06, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-005/V6 | SC-M11-005/E12 | M1 | 2 | FR-M11-03.04, FR-M11-03.10, FR-M11-17.03, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-005/V7 | SC-M11-005/E13 | M1 | 2 | FR-M11-03.12, FR-M11-03.10, BR-M11-17, BR-M11-33, FR-M08-04.06 |
| SC-M11-005/V8 | SC-M11-005/E14 | M1 | 2 | FR-M11-03.11, FR-M11-03.06, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-005/V9 | SC-M11-005/E15 | M1 | 2 | FR-M11-03.04, FR-M11-03.10, FR-M11-17.03, BR-M11-17, BR-M11-33, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-005/V10 | SC-M11-005/E16 | M1 | 2 | FR-M11-03.04, FR-M11-03.09, FR-M11-03.13, BR-M11-13, BR-M11-17, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-005/V11 | SC-M11-005/E17 | M1 | 2 | FR-M11-14.01, FR-M11-14.03, FR-M11-14.05, FR-M11-14.07, BR-M11-30, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-006/V1 | SC-M11-006/E3 | M1 | 2 | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-006/V2 | SC-M11-006/E4 | M1 | 2 | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-006/V3 | SC-M11-006/E5 | M1 | 2 | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-006/V4 | SC-M11-006/E6 | M1 | 2 | FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-006/V5 | SC-M11-006/E7 | M1 | 2 | FR-M11-03.14, FR-M11-17.03, FR-M10-12.08, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-007/V1 | SC-M11-007/E13 | M1 | 2 | FR-M11-04.05, BR-M11-07 |
| SC-M11-007/V2 | SC-M11-007/E14 | M1 | 2 | FR-M11-04.01, FR-M11-05.05, FR-M11-17.03, FR-M10-12.08, FR-M11-04.06, FR-M11-04.07, FR-M11-04.09, FR-M11-05.04, FR-M11-06.08, BR-M11-03, BR-M11-07, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-37, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-008/V1 | SC-M11-008/E5 | M1 | 2 | FR-M11-04.10, FR-M11-17.03, FR-M10-12.08, BR-M11-36, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-009/V1 | SC-M11-009/E6 | M1 | 2 | FR-M11-05.01, FR-M11-05.02, FR-M11-17.03, FR-M10-12.08, FR-M11-05.04, FR-M11-05.05, FR-M11-05.06, FR-M11-05.07, BR-M11-12, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-009/V2 | SC-M11-009/E7 | M1 | 2 | FR-M11-05.03, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-009/V3 | SC-M11-009/E8 | M1 | 2 | FR-M11-05.03, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-009/V4 | SC-M11-009/E9 | M1 | 2 | FR-M11-05.03, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-009/V5 | SC-M11-009/E10 | M1 | 2 | FR-M11-05.03, BR-M11-12, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-010/V1 | SC-M11-010/E7 | M1 | 4 | FR-M11-06.01, FR-M11-17.03, FR-M10-12.08, FR-M11-06.05, BR-M11-08, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-06.02, FR-M11-06.04, FR-M11-06.06, BR-M11-07, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |
| SC-M11-010/V2 | SC-M11-010/E8 | M1 | 2 | FR-M11-06.05, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-010/V3 | SC-M11-010/E9 | M1 | 2 | FR-M11-06.05, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-010/V4 | SC-M11-010/E10 | M1 | 2 | FR-M11-06.05, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-010/V5 | SC-M11-010/E11 | M1 | 2 | FR-M11-06.05, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-010/V6 | SC-M11-010/E12 | M1 | 4 | FR-M11-06.01, FR-M11-06.05, BR-M11-08, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-06.02, FR-M11-06.04, FR-M11-06.06, BR-M11-07, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |
| SC-M11-011/V1 | SC-M11-011/E5 | M1 | 2 | FR-M11-07.01, FR-M11-17.03, FR-M10-12.08, FR-M11-07.03, FR-M11-04.06, FR-M11-06.09, BR-M11-06, BR-M11-10, BR-M11-37, FR-M11-17.01, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-011/V2 | SC-M11-011/E6 | M1 | 2 | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-011/V3 | SC-M11-011/E7 | M1 | 2 | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-011/V4 | SC-M11-011/E8 | M1 | 2 | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-011/V5 | SC-M11-011/E9 | M1 | 2 | FR-M11-07.01, FR-M11-07.03, FR-M11-04.06, FR-M11-06.09, BR-M11-06, BR-M11-10, BR-M11-37, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-012/V1 | SC-M11-012/E4 | M1 | 2 | FR-M11-07.04, FR-M11-17.03, FR-M10-12.08, FR-M11-07.02, BR-M11-06, BR-M11-10, FR-M11-17.01, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-012/V2 | SC-M11-012/E5 | M1 | 2 | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-012/V3 | SC-M11-012/E6 | M1 | 2 | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-012/V4 | SC-M11-012/E7 | M1 | 2 | FR-M11-07.04, FR-M11-07.02, BR-M11-06, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-013/V1 | SC-M11-013/E4 | M1 | 4 | FR-M11-07.04, FR-M11-07.05, FR-M11-17.03, FR-M10-12.08, FR-M11-07.02, BR-M11-10, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-013/V2 | SC-M11-013/E5 | M1 | 2 | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-013/V3 | SC-M11-013/E6 | M1 | 2 | FR-M11-07.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-013/V4 | SC-M11-013/E7 | M1 | 4 | FR-M11-07.04, FR-M11-07.05, FR-M11-07.02, BR-M11-10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-014/V1 | SC-M11-014/E6 | M1 | 4 | FR-M11-08.01, FR-M11-17.03, FR-M10-12.08, FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-08.03, FR-M11-11.06, BR-M11-05, BR-M11-26, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |
| SC-M11-014/V2 | SC-M11-014/E7 | M1 | 2 | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-014/V3 | SC-M11-014/E8 | M1 | 2 | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-014/V4 | SC-M11-014/E9 | M1 | 2 | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-014/V5 | SC-M11-014/E10 | M1 | 2 | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-015/V1 | SC-M11-015/E6 | M1 | 4 | FR-M11-08.02, FR-M11-17.03, FR-M10-12.08, FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-08.06, FR-M11-11.06, BR-M11-05, BR-M11-26, BR-M11-37 |
| SC-M11-015/V2 | SC-M11-015/E7 | M1 | 2 | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-015/V3 | SC-M11-015/E8 | M1 | 2 | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-015/V4 | SC-M11-015/E9 | M1 | 2 | FR-M11-08.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-016/V1 | SC-M11-016/E8 | M1 | 2 | FR-M11-09.02, FR-M11-09.05, FR-M11-09.06, FR-M11-09.07, FR-M11-10.08, BR-M11-05, BR-M11-24, BR-M11-37, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-016/V2 | SC-M11-016/E9 | M1 | 2 | FR-M11-09.03, BR-M11-05 |
| SC-M11-016/V3 | SC-M11-016/E10 | M1 | 2 | FR-M11-09.03, BR-M11-05 |
| SC-M11-016/V4 | SC-M11-016/E11 | M1 | 4 | FR-M11-09.01, FR-M11-17.03, FR-M10-12.08, FR-M11-08.05, FR-M11-03.14, FR-M11-03.15, BR-M11-34, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M11-09.05, FR-M11-09.06, FR-M11-09.07, FR-M11-10.08, BR-M11-05, BR-M11-24, BR-M11-37, FR-M12-02.15, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11 |
| SC-M11-016/V5 | SC-M11-016/E12 | M1 | 2 | FR-M11-09.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-016/V6 | SC-M11-016/E13 | M1 | 2 | FR-M11-09.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-016/V7 | SC-M11-016/E14 | M1 | 2 | FR-M11-09.04, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-017/V1 | SC-M11-017/E7 | M1 | 2 | FR-M11-16.09, FR-M11-10.01, FR-M11-10.02, FR-M11-10.08, BR-M11-24, BR-M11-28, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-29 |
| SC-M11-017/V2 | SC-M11-017/E8 | M1 | 2 | FR-M11-10.01, FR-M11-17.03, FR-M10-12.08, FR-M11-10.02, FR-M11-10.08, FR-M11-16.09, BR-M11-24, BR-M11-28, FR-M12-02.15, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-29 |
| SC-M11-017/V3 | SC-M11-017/E9 | M1 | 2 | FR-M11-10.01, FR-M11-10.02, FR-M11-10.09, BR-M11-24, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-017/V4 | SC-M11-017/E10 | M1 | 2 | FR-M11-10.01, FR-M11-10.02, FR-M11-10.08, FR-M11-16.09, BR-M11-24, BR-M11-28, FR-M12-02.15, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-29 |
| SC-M11-018/V1 | SC-M11-018/E24 | M1 | 4 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| SC-M11-018/V2 | SC-M11-018/E25 | M1 | 4 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| SC-M11-018/V3 | SC-M11-018/E26 | M1 | 4 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| SC-M11-018/V4 | SC-M11-018/E27 | M1 | 4 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| SC-M11-018/V5 | SC-M11-018/E28 | M1 | 4 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| SC-M11-018/V6 | SC-M11-018/E29 | M1 | 6 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| SC-M11-018/V7 | SC-M11-018/E30 | M1 | 2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |
| SC-M11-018/V8 | SC-M11-018/E31 | M1 | 6 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M13-01.07, FR-M13-02.01, FR-M13-02.08, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09 |
| SC-M11-018/V9 | SC-M11-018/E32 | M1 | 2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |
| SC-M11-018/V10 | SC-M11-018/E33 | M1 | 2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |
| SC-M11-018/V11 | SC-M11-018/E34 | M1 | 2 | FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.07, FR-M11-12.08, FR-M11-12.09, FR-M11-12.10, FR-M11-12.11, FR-M11-12.12, FR-M11-12.13, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-40, FR-M03-04.04, FR-M03-04.05, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M11-13.12, BR-M11-38, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M03-04.02, BR-M03-46, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29, FR-M13-01.02, FR-M13-01.03, FR-M13-02.11 |
| SC-M11-018/V12 | SC-M11-018/E35 | M1 | 2 | FR-M11-12.11, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-018/V13 | SC-M11-018/E36 | M1 | 2 | FR-M11-12.11, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-018/V14 | SC-M11-018/E37 | M1 | 2 | FR-M11-12.11, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-018/V15 | SC-M11-018/E38 | M1 | 2 | FR-M11-12.11, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-019/V1 | SC-M11-019/E5 | M1 | 2 | FR-M11-13.01, FR-M11-17.03, FR-M10-12.08, FR-M11-13.08, FR-M11-13.09, BR-M11-17, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-019/V2 | SC-M11-019/E6 | M1 | 2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-019/V3 | SC-M11-019/E7 | M1 | 2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-019/V4 | SC-M11-019/E8 | M1 | 2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-019/V5 | SC-M11-019/E9 | M1 | 2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-019/V6 | SC-M11-019/E10 | M1 | 2 | FR-M11-13.01, FR-M11-13.08, FR-M11-13.09, BR-M11-17, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-020/V1 | SC-M11-020/E8 | M1 | 2 | FR-M11-13.02, FR-M11-17.03, FR-M10-12.08, FR-M11-13.03, FR-M11-13.04, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-020/V2 | SC-M11-020/E9 | M1 | 2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-020/V3 | SC-M11-020/E10 | M1 | 2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-020/V4 | SC-M11-020/E11 | M1 | 2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-020/V5 | SC-M11-020/E12 | M1 | 2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-020/V6 | SC-M11-020/E13 | M1 | 2 | FR-M11-13.02, FR-M11-13.03, FR-M11-13.04, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, BR-M11-20, BR-M11-33, BR-M11-39, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-021/V1 | SC-M11-021/E9 | M1 | 2 | FR-M11-13.05, FR-M11-17.03, FR-M10-12.08, FR-M11-13.03, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, FR-M11-12.12, FR-M11-12.13, BR-M11-17, BR-M11-18, BR-M11-20, BR-M11-33, BR-M11-39, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-021/V2 | SC-M11-021/E10 | M1 | 2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-021/V3 | SC-M11-021/E11 | M1 | 2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-021/V4 | SC-M11-021/E12 | M1 | 2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-021/V5 | SC-M11-021/E13 | M1 | 2 | FR-M11-13.08, FR-M11-13.09, BR-M11-33, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-021/V6 | SC-M11-021/E14 | M1 | 2 | FR-M11-13.05, FR-M11-13.03, FR-M11-13.08, FR-M11-13.09, FR-M11-13.13, FR-M11-12.12, FR-M11-12.13, BR-M11-17, BR-M11-18, BR-M11-20, BR-M11-33, BR-M11-39, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M13-03.01, FR-M14-04.09, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-022/V1 | SC-M11-022/E7 | M1 | 2 | FR-M11-14.01, FR-M11-14.03, FR-M11-14.04, FR-M11-14.05, FR-M11-14.06, FR-M11-14.07, BR-M11-05, BR-M11-30, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-06, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-022/V2 | SC-M11-022/E8 | M1 | 2 | FR-M11-14.01, FR-M11-17.03, FR-M10-12.08, FR-M11-14.02, FR-M11-14.03, FR-M11-14.04, FR-M11-14.05, FR-M11-14.06, FR-M11-14.07, FR-M11-14.08, BR-M11-05, BR-M11-06, BR-M11-21, BR-M11-22, BR-M11-30, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M12-02.16, FR-M15-02.27, FR-M11-17.01, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-022/V3 | SC-M11-022/E9 | M1 | 2 | FR-M11-14.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-022/V4 | SC-M11-022/E10 | M1 | 2 | FR-M11-14.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-022/V5 | SC-M11-022/E11 | M1 | 2 | FR-M11-14.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-022/V6 | SC-M11-022/E12 | M1 | 2 | FR-M11-14.02, BR-M11-06, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
| SC-M11-022/V7 | SC-M11-022/E13 | M1 | 2 | FR-M11-14.01, FR-M11-14.02, FR-M11-14.03, FR-M11-14.04, FR-M11-14.05, FR-M11-14.06, FR-M11-14.07, FR-M11-14.08, BR-M11-05, BR-M11-06, BR-M11-21, BR-M11-22, BR-M11-30, FR-M07-02.01, FR-M07-02.02, FR-M07-02.11, FR-M12-02.16, FR-M15-02.27, FR-M11-17.01, FR-M11-17.03, FR-M11-17.08, BR-M11-23, BR-M11-27, BR-M11-28, BR-M11-29 |
