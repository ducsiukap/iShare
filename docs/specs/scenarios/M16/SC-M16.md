# Kịch bản nghiệp vụ — SC-M16 Chat & Messaging

[Vietnamese Doc] — Tái kiểm 11/11/2026 — Skill scenarios v1.4.

Tài liệu triển khai chức năng actor yêu cầu từ FR và phân tích use case M16 thành hành trình sáu phần để BA review từng đường chính, nhánh và kết quả. Boundary là toàn hệ thống iShare. Các chức năng trong Chat gồm bắt đầu/mở lại 1-1, hộp thư/lịch sử, gửi/thu hồi, tạo/mở rộng và quản lý vòng đời nhóm chat.

Phạm vi là 4 UC chính và 20 UC con của US-M16. Phân tích theo mục tiêu cho 15 BF và 15 scenario. Các UC 006, 007, 018, 019, 020 được triển khai tại điểm gọi. Giữ nguyên 26 mapping và 25 quan hệ include nguồn. Các tác vụ tự động có trigger riêng nằm ở N1–N3. Popup/mute thuộc M07, đăng nhập/vòng đời tài khoản thuộc M01, bật cờ thuộc M10, khiếu nại thuộc M09. Chat group độc lập Group M11. Đọc catalog trước, chọn BF rồi đi từ M1 hoặc đúng E tại M1, rẽ E tại bước bị thay thế và đối chiếu kết quả mục 4.

## 1. Metadata và baseline

<!-- sc:document -->

| key | value |
|---|---|
| module | M16 |
| scope | ALL |
| skill_version | 1.4 |
| output_dir | docs/specs/scenarios/M16 |
| status | Đang soạn |
| completed_steps | 1, 2, 3, 4 |
| date | 2026-11-11 |
| approval_evidence | - |


FR-M16 v1.0 Đã chốt, ngày 2026-10-24. US-M16 Chờ duyệt, ngày 2026-11-02, chưa có version tài liệu riêng. US-overview v1.1 Chờ duyệt. Các bản FR chính thức và bản làm việc được so SHA-256 tại QA. Có 6 nhóm giới hạn nguồn còn mở nên đầu ra giữ Đang soạn. Các dữ liệu A/B/G/Q và thời gian trong kịch bản là giả lập.

| Path từ repo root | Version | Ngày | Trạng thái nguồn | SHA-256 | Vai trò |
|---|---|---|---|---|---|
| [docs/specs/fr/FR-M16.md](../../fr/FR-M16.md) | 1.0 | 2026-10-24 | Đã chốt | c8ef96e52479806637b0eac334bbe57fa9fe4f73bdacc73913467960050f0671 | FR/US và boundary |
| [docs/specs/fr/FR-M01.md](../../fr/FR-M01.md) | 1.10 | 2026-10-24 | Đã chốt | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a | FR/US và boundary |
| [docs/specs/fr/FR-M02.md](../../fr/FR-M02.md) | 1.6 | 2026-10-24 | Đã chốt | e86aca71e0415ee2e121a4fdc3628261be335e9d266fcf6e9654b2fdf3cd357e | FR/US và boundary |
| [docs/specs/fr/FR-M07.md](../../fr/FR-M07.md) | 1.5 | 2026-10-24 | Đã chốt | 05fb18237e049e3742d06c49b824e76e238c7587e7099b8dc4a84a2e1daf4f5b | FR/US và boundary |
| [docs/specs/fr/FR-M08.md](../../fr/FR-M08.md) | 1.7 | 2026-10-24 | Đã chốt | a92e6e370038af300a9ddd735414dcb2c4fbffe07c81abaaa3c92dff447c25f0 | FR/US và boundary |
| [docs/specs/fr/FR-M09.md](../../fr/FR-M09.md) | 1.2 | 2026-10-24 | Đã chốt | 8ad8ae5e148c6e446f4bfec7f6e74ba9566c54747a0eda37a3930e94ab96faea | FR/US và boundary |
| [docs/specs/fr/FR-M10.md](../../fr/FR-M10.md) | 1.4 | 2026-10-24 | Đã chốt | 3e1010a76db6ef4c5870f42765e669095efc8d38c202271d9b200d2da0823d2c | FR/US và boundary |
| [docs/specs/fr/FR-M11.md](../../fr/FR-M11.md) | 1.3 | 2026-10-24 | Đã chốt | 1908d300f75d5f7fa0fd5b31b1d375bc6a63ccd42da254de6e9d0d7d9ef16307 | FR/US và boundary |
| [docs/specs/fr/FR-M13.md](../../fr/FR-M13.md) | 1.3 | 2026-10-24 | Đã chốt | 54630715cc1e391b9ea361247784af26200fc2f01c1b1da96ea56ed1f75f9982 | FR/US và boundary |
| [docs/specs/us/US-M16.md](../../us/US-M16.md) | Không có version tài liệu, skill_version 2.2 | 2026-11-02 | Chờ duyệt | a467e7f3be89f462e4c6b74316f6f54f2caee120c23c6bdf479bd01b2a7747f3 | FR/US và boundary |
| [docs/specs/us/US-overview.md](../../us/US-overview.md) | 1.1 | 2026-11-02 | Chờ duyệt | c1d624b7036ea2c7a9968eaa46c482c04fa1a15e2554d536cdfc12f177e26e33 | FR/US và boundary |
| [.agents/.claude/system_analysis/output/fr/FR-M16.md](../../../../.agents/.claude/system_analysis/output/fr/FR-M16.md) | 1.0 | 2026-10-24 | Đã chốt | c8ef96e52479806637b0eac334bbe57fa9fe4f73bdacc73913467960050f0671 | FR/US và boundary |
| [.agent-instructions/skills/scenarios/SKILL.md](../../../../.agent-instructions/skills/scenarios/SKILL.md) | 1.4 | — | — | 9ccee596aaeebfad15085bf8ad6b60001b1a246fe4e2f178f6d97884e262f11c | FR/US và boundary |
| [docs/specs/us/diagrams/M16/C-M16.svg](../../us/diagrams/M16/C-M16.svg) | — | — | — | 283ef1b93dfa0b19468a9e71f236153b05c0652d57f2f8271b86d6e438417ca5 | Sơ đồ UC nguồn |
| [docs/specs/us/diagrams/M16/D-M16-030.svg](../../us/diagrams/M16/D-M16-030.svg) | — | — | — | a30af28d3436230e48c4fdf986c91aca576682fe1cd1a793887ebc81b3570c36 | Sơ đồ UC nguồn |
| [docs/specs/us/diagrams/M16/D-M16-031.svg](../../us/diagrams/M16/D-M16-031.svg) | — | — | — | daef38d491f132ba9bacf238071bec85ffb8d210e326f34a43038453eca23208 | Sơ đồ UC nguồn |
| [docs/specs/us/diagrams/M16/D-M16-032.svg](../../us/diagrams/M16/D-M16-032.svg) | — | — | — | 4f2421380c6ca5c2371e1ddb47182dd360be4cf668e6513c62aeebccc2f7c74a | Sơ đồ UC nguồn |
| [docs/specs/us/diagrams/M16/D-M16-033.svg](../../us/diagrams/M16/D-M16-033.svg) | — | — | — | 3174bd3f885cff41a332fb64060893310849369c33016ab89cc0eed662db606d | Sơ đồ UC nguồn |


### Actor và quyền

<!-- sc:actors -->

| id | name | kind | source |
|---|---|---|---|
| ACT-001 | Guest | human | FR-M16-01.03, FR-M16-03.02, FR-M16-16.02 |
| ACT-002 | Người dùng đã đăng nhập | human | FR-M16-01.01, FR-M16-02.01, FR-M16-03.01, FR-M16-16.01 |
| ACT-008 | Mod hệ thống | human | FR-M16-04.08, FR-M16-05.06, BR-M16-20, FR-M16-15.01 |
| ACT-007 | Admin hệ thống | human | FR-M16-15.04, FR-M16-04.08, FR-M16-06.04 |
| ACT-012 | Thành viên cuộc trò chuyện | human | FR-M16-04.01, FR-M16-05.01, FR-M16-06.01, BR-M16-05 |
| ACT-013 | Admin nhóm chat | human | FR-M16-02.02, FR-M16-09.01, FR-M16-10.01, FR-M16-13.01, BR-M16-04, BR-M16-05 |
| ACT-014 | Thành viên cũ nhóm chat | human | FR-M16-04.10, FR-M16-11.01, FR-M16-14.01, BR-M16-27 |


ACT-013 chỉ quyền Admin của đúng nhóm chat. ACT-007 chỉ được miễn cổng cờ, vẫn kiểm quyền cuộc/role/sender/giới hạn. ACT-014 chỉ lịch sử trước cutoff khi chưa vào lại. A, B là người giả lập, mỗi đường chọn một vai trò phù hợp với snapshot, ID actor là ID vai trò trong US. SYSTEM chứa M01/M02/M07/M09/M10 và xử lý nội bộ cần thiết.

## 2. Kiểm kê UC và luồng nghiệp vụ

<!-- sc:decomposition -->

| core | sub | source |
|---|---|---|
| UC-M16-030 | UC-M16-001 | FR-M16-01, BR-M16-01, BR-M16-02, BR-M16-24, BR-M16-25 |
| UC-M16-030 | UC-M16-002 | FR-M16-03, BR-M16-31, BR-M16-27 |
| UC-M16-030 | UC-M16-003 | FR-M16-04, BR-M16-17, BR-M16-26, BR-M16-27 |
| UC-M16-030 | UC-M16-006 | FR-M16-07, BR-M16-13, BR-M16-14 |
| UC-M16-030 | UC-M16-007 | FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-06.09, BR-M16-15, BR-M16-16 |
| UC-M16-030 | UC-M16-018 | FR-M16-03.02, FR-M16-03.03, FR-M16-04.08, FR-M16-05.06, FR-M16-15, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23 |
| UC-M16-031 | UC-M16-004 | FR-M16-05, FR-M16-01.02, BR-M16-08, BR-M16-09, BR-M16-21, BR-M16-25 |
| UC-M16-031 | UC-M16-005 | FR-M16-06, BR-M16-11, BR-M16-12, BR-M16-18 |
| UC-M16-031 | UC-M16-006 | FR-M16-07, BR-M16-13, BR-M16-14 |
| UC-M16-031 | UC-M16-007 | FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-06.09, BR-M16-15, BR-M16-16 |
| UC-M16-031 | UC-M16-018 | FR-M16-03.02, FR-M16-03.03, FR-M16-04.08, FR-M16-05.06, FR-M16-15, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23 |
| UC-M16-032 | UC-M16-008 | FR-M16-02, BR-M16-01, BR-M16-03, BR-M16-04, BR-M16-06, BR-M16-25, BR-M16-32 |
| UC-M16-032 | UC-M16-009 | FR-M16-08, BR-M16-03, BR-M16-06, BR-M16-25, BR-M16-28 |
| UC-M16-032 | UC-M16-010 | FR-M16-08.10, FR-M16-08.11, FR-M16-08.12, FR-M16-08.13, BR-M16-29 |
| UC-M16-032 | UC-M16-011 | FR-M16-16, BR-M16-06, BR-M16-28, BR-M16-29 |
| UC-M16-032 | UC-M16-012 | FR-M16-10, BR-M16-03, BR-M16-05, BR-M16-06 |
| UC-M16-032 | UC-M16-018 | FR-M16-03.02, FR-M16-03.03, FR-M16-04.08, FR-M16-05.06, FR-M16-15, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23 |
| UC-M16-032 | UC-M16-019 | FR-M16-02.02, FR-M16-08.01, FR-M16-08.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.09, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, BR-M16-03, BR-M16-25, BR-M16-27 |
| UC-M16-033 | UC-M16-013 | FR-M16-09, BR-M16-06, BR-M16-33 |
| UC-M16-033 | UC-M16-014 | FR-M16-11, FR-M16-14.03, BR-M16-05, BR-M16-27 |
| UC-M16-033 | UC-M16-015 | FR-M16-12, BR-M16-05, BR-M16-32 |
| UC-M16-033 | UC-M16-016 | FR-M16-13, BR-M16-04, BR-M16-05, BR-M16-07, BR-M16-30 |
| UC-M16-033 | UC-M16-017 | FR-M16-14, BR-M16-03, BR-M16-07, BR-M16-27, BR-M16-28 |
| UC-M16-033 | UC-M16-018 | FR-M16-03.02, FR-M16-03.03, FR-M16-04.08, FR-M16-05.06, FR-M16-15, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23 |
| UC-M16-033 | UC-M16-019 | FR-M16-02.02, FR-M16-08.01, FR-M16-08.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.09, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, BR-M16-03, BR-M16-25, BR-M16-27 |
| UC-M16-033 | UC-M16-020 | FR-M16-09.03, FR-M16-09.04, FR-M16-17.02, BR-M16-33 |


<!-- sc:ucs -->

| id | name | treatment | scenarios | coverage | rationale | sources |
|---|---|---|---|---|---|---|
| UC-M16-030 | Bắt đầu và truy cập cuộc trò chuyện | aggregate | SC-M16-001, SC-M16-002, SC-M16-003 | SC-M16-001/M2, SC-M16-002/M2, SC-M16-003/M2 | Summary gom các mục tiêu con độc lập, mỗi mục tiêu có hành trình riêng. | FR-M16-01, FR-M16-03, FR-M16-04, FR-M16-07, FR-M16-15 |
| UC-M16-031 | Trao đổi và quản lý tin nhắn | aggregate | SC-M16-004, SC-M16-005 | SC-M16-004/M2, SC-M16-005/M2 | Summary gom các mục tiêu con độc lập, mỗi mục tiêu có hành trình riêng. | FR-M16-05, FR-M16-06, FR-M16-07, FR-M16-15 |
| UC-M16-032 | Hình thành và mở rộng nhóm chat | aggregate | SC-M16-006, SC-M16-007, SC-M16-008, SC-M16-009, SC-M16-010 | SC-M16-006/M2, SC-M16-007/M2, SC-M16-008/M2, SC-M16-009/M2, SC-M16-010/M2 | Summary gom các mục tiêu con độc lập, mỗi mục tiêu có hành trình riêng. | FR-M16-02, FR-M16-08, FR-M16-10, FR-M16-16, FR-M16-15 |
| UC-M16-033 | Quản lý vòng đời nhóm chat | aggregate | SC-M16-011, SC-M16-012, SC-M16-013, SC-M16-014, SC-M16-015 | SC-M16-011/M2, SC-M16-012/M2, SC-M16-013/M2, SC-M16-014/M2, SC-M16-015/M2 | Summary gom các mục tiêu con độc lập, mỗi mục tiêu có hành trình riêng. | FR-M16-09, FR-M16-11, FR-M16-12, FR-M16-13, FR-M16-14, FR-M16-17, FR-M16-15 |
| UC-M16-001 | Bắt đầu hoặc mở lại trò chuyện 1-1 | scenario | SC-M16-001 | SC-M16-001/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-01, BR-M16-01, BR-M16-02, BR-M16-24, BR-M16-25 |
| UC-M16-002 | Xem hộp thư Chat | scenario | SC-M16-002 | SC-M16-002/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-03, BR-M16-31, BR-M16-27 |
| UC-M16-003 | Xem cuộc trò chuyện và lịch sử | scenario | SC-M16-001, SC-M16-003 | SC-M16-001/M2, SC-M16-003/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-04, BR-M16-17, BR-M16-26, BR-M16-27 |
| UC-M16-004 | Gửi tin nhắn văn bản | scenario | SC-M16-004 | SC-M16-004/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-05, FR-M16-01.02, BR-M16-08, BR-M16-09, BR-M16-21, BR-M16-25 |
| UC-M16-005 | Thu hồi tin nhắn của mình | scenario | SC-M16-005 | SC-M16-005/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-06, BR-M16-11, BR-M16-12, BR-M16-18 |
| UC-M16-006 | Ghi mốc đã đọc của thành viên | embedded | SC-M16-001, SC-M16-003, SC-M16-004 | SC-M16-001/E1.1, SC-M16-003/M2, SC-M16-004/M2 | Xử lý hỗ trợ triển khai trong lượt SYSTEM của hành trình bao chứa, AUT liên quan giữ ở N1–N3. | FR-M16-07, BR-M16-13, BR-M16-14 |
| UC-M16-007 | Suy ra trạng thái và người đã xem | embedded | SC-M16-001, SC-M16-003, SC-M16-004, SC-M16-005 | SC-M16-001/E1.1, SC-M16-003/M2, SC-M16-004/M2, SC-M16-005/M2 | Xử lý hỗ trợ triển khai trong lượt SYSTEM của hành trình bao chứa, AUT liên quan giữ ở N1–N3. | FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-06.09, BR-M16-15, BR-M16-16 |
| UC-M16-008 | Tạo nhóm chat | scenario | SC-M16-006 | SC-M16-006/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-02, BR-M16-01, BR-M16-03, BR-M16-04, BR-M16-06, BR-M16-25, BR-M16-32 |
| UC-M16-009 | Thêm hoặc đề nghị thêm thành viên | scenario | SC-M16-007 | SC-M16-007/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-08, BR-M16-03, BR-M16-06, BR-M16-25, BR-M16-28 |
| UC-M16-010 | Lấy link mời nhóm chat | scenario | SC-M16-008 | SC-M16-008/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-08.10, FR-M16-08.11, FR-M16-08.12, FR-M16-08.13, BR-M16-29 |
| UC-M16-011 | Xin gia nhập qua link mời | scenario | SC-M16-009 | SC-M16-009/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-16, BR-M16-06, BR-M16-28, BR-M16-29 |
| UC-M16-012 | Duyệt người chờ vào nhóm chat | scenario | SC-M16-010 | SC-M16-010/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-10, BR-M16-03, BR-M16-05, BR-M16-06 |
| UC-M16-013 | Bật hoặc tắt duyệt thành viên mới | scenario | SC-M16-011 | SC-M16-011/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-09, BR-M16-06, BR-M16-33 |
| UC-M16-014 | Xóa Member khỏi nhóm chat | scenario | SC-M16-012 | SC-M16-012/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-11, FR-M16-14.03, BR-M16-05, BR-M16-27 |
| UC-M16-015 | Đổi tên nhóm chat | scenario | SC-M16-013 | SC-M16-013/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-12, BR-M16-05, BR-M16-32 |
| UC-M16-016 | Chuyển quyền Admin nhóm chat | scenario | SC-M16-014 | SC-M16-014/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-13, BR-M16-04, BR-M16-05, BR-M16-07, BR-M16-30 |
| UC-M16-017 | Rời nhóm chat | scenario | SC-M16-015 | SC-M16-015/M2 | Actor có thể chủ động yêu cầu chức năng và nhận kết quả hoàn tất riêng. | FR-M16-14, BR-M16-03, BR-M16-07, BR-M16-27, BR-M16-28 |
| UC-M16-018 | Kiểm tra quyền thực hiện thao tác Chat | embedded | SC-M16-001, SC-M16-002, SC-M16-003, SC-M16-004, SC-M16-005, SC-M16-006, SC-M16-007, SC-M16-008, SC-M16-009, SC-M16-010, SC-M16-011, SC-M16-012, SC-M16-013, SC-M16-014, SC-M16-015 | SC-M16-001/M2, SC-M16-002/M2, SC-M16-003/M2, SC-M16-004/M2, SC-M16-005/M2, SC-M16-006/M2, SC-M16-007/M2, SC-M16-008/M2, SC-M16-009/M2, SC-M16-010/M2, SC-M16-011/M2, SC-M16-012/M2, SC-M16-013/M2, SC-M16-014/M2, SC-M16-015/M2 | Xử lý hỗ trợ triển khai trong lượt SYSTEM của hành trình bao chứa, AUT liên quan giữ ở N1–N3. | FR-M16-03.02, FR-M16-03.03, FR-M16-04.08, FR-M16-05.06, FR-M16-15, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23 |
| UC-M16-019 | Kết nạp một Member vào nhóm chat | embedded | SC-M16-006, SC-M16-007, SC-M16-009, SC-M16-010, SC-M16-011 | SC-M16-006/M2, SC-M16-007/M2, SC-M16-009/M4, SC-M16-010/M4, SC-M16-011/M2 | Xử lý hỗ trợ triển khai trong lượt SYSTEM của hành trình bao chứa, AUT liên quan giữ ở N1–N3. | FR-M16-02.02, FR-M16-08.01, FR-M16-08.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.09, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, BR-M16-03, BR-M16-25, BR-M16-27 |
| UC-M16-020 | Giải quyết hàng chờ khi tắt duyệt | embedded | SC-M16-011 | SC-M16-011/M2 | Xử lý hỗ trợ triển khai trong lượt SYSTEM của hành trình bao chứa, AUT liên quan giữ ở N1–N3. | FR-M16-09.03, FR-M16-09.04, FR-M16-17.02, BR-M16-33 |


<!-- sc:flows -->

| id | uc | primary | trigger | goal | completion | covered_ucs | rationale | scenario | sources |
|---|---|---|---|---|---|---|---|---|---|
| BF-M16-001 | UC-M16-001 | ACT-002 | Chọn người nhận từ hồ sơ để bắt đầu hoặc mở lại trò chuyện 1-1. | Bắt đầu hoặc mở lại trò chuyện 1-1 | Mở C-AB duy nhất của A–B với đúng hai thành viên, lịch sử rỗng, chưa có tin gửi. | UC-M16-001, UC-M16-003, UC-M16-006, UC-M16-007, UC-M16-018, UC-M16-030 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-001 | FR-M16-01.01, FR-M16-01.02, FR-M16-01.03, FR-M16-01.04, FR-M16-01.05, FR-M16-01.06, FR-M16-01.07, FR-M16-03.07, FR-M16-04.01, BR-M16-01, BR-M16-02, BR-M16-24, BR-M16-25, BR-M16-31, FR-M02-01.26, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-04.04, FR-M16-04.07, FR-M16-04.09, FR-M16-04.11, FR-M16-04.12, FR-M16-05.13, FR-M16-05.14, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-26, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02 |
| BF-M16-002 | UC-M16-002 | ACT-002 | Mở hộp thư Chat từ biểu tượng Tin nhắn. | Xem hộp thư Chat | A nhận 20 cuộc ở lần đầu và 3 cuộc kế tiếp khi chọn tải thêm, tổng 23 cuộc hợp lệ, theo thứ tự tin cuối được thấy và nhãn chưa đọc đúng phạm vi. | UC-M16-002, UC-M16-018, UC-M16-030 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-002 | FR-M16-03.01, FR-M16-03.02, FR-M16-03.03, FR-M16-03.04, FR-M16-03.05, FR-M16-03.06, FR-M16-03.07, FR-M16-03.08, FR-M16-07.10, BR-M16-26, BR-M16-27, BR-M16-31, FR-M07-07.02, FR-M07-07.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-01.03, FR-M16-02.06, FR-M16-16.02 |
| BF-M16-003 | UC-M16-003 | ACT-012 | Mở nhóm G45 để đọc cuộc trò chuyện và lịch sử. | Xem cuộc trò chuyện và lịch sử | A nhận trang #26–#45 khi mở, rồi #6–#25 và #1–#5 khi cuộn lên, đọc được toàn bộ 45 tin. Mốc A từ #40 tới #45 và không lùi do tải tin cũ, receipt tin cuối theo từng viewer. | UC-M16-003, UC-M16-006, UC-M16-007, UC-M16-018, UC-M16-030 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-003 | FR-M16-04.01, FR-M16-04.02, FR-M16-04.03, FR-M16-04.04, FR-M16-04.05, FR-M16-04.06, FR-M16-04.07, FR-M16-04.08, FR-M16-04.09, FR-M16-04.10, FR-M16-04.11, FR-M16-04.12, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-12, BR-M16-17, BR-M16-19, BR-M16-26, BR-M16-27, FR-M01-13.06, FR-M01-13.07, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| BF-M16-004 | UC-M16-004 | ACT-012 | Nhập và gửi tin văn bản “Mai ôn thi nhé 😀” vào C-AB. | Gửi tin nhắn văn bản | Tin #46 nhận 10:01:00, mốc A=#46, B chưa đọc nên Đã gửi, nội dung đến view hợp lệ và sự kiện M07 được cung cấp. Không email, chuông hoặc thông báo được mời. | UC-M16-004, UC-M16-006, UC-M16-007, UC-M16-018, UC-M16-031 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-004 | FR-M16-05.01, FR-M16-05.02, FR-M16-05.03, FR-M16-05.04, FR-M16-05.05, FR-M16-05.06, FR-M16-05.07, FR-M16-05.08, FR-M16-05.09, FR-M16-05.10, FR-M16-05.11, FR-M16-05.12, FR-M16-05.13, FR-M16-05.14, FR-M16-01.02, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-08, BR-M16-09, BR-M16-10, BR-M16-18, BR-M16-20, BR-M16-21, BR-M16-25, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, FR-M16-04.08, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02, FR-M16-04.10, BR-M16-27, BR-M16-28 |
| BF-M16-005 | UC-M16-005 | ACT-012 | Chọn thu hồi tin #50 trong G50. | Thu hồi tin nhắn của mình | #50 gắn đã thu hồi, gốc được giữ và che với mọi actor kể cả staff. Tin cuối là placeholder #50, Đã xem do B đã đọc, vị trí/thời điểm tin giữ nguyên. | UC-M16-005, UC-M16-007, UC-M16-018, UC-M16-031 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-005 | FR-M16-06.01, FR-M16-06.02, FR-M16-06.03, FR-M16-06.04, FR-M16-06.05, FR-M16-06.06, FR-M16-06.07, FR-M16-06.08, FR-M16-06.09, FR-M16-05.08, BR-M16-11, BR-M16-12, BR-M16-15, BR-M16-18, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-07.08, FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02, FR-M16-04.10, BR-M16-27, BR-M16-28 |
| BF-M16-006 | UC-M16-008 | ACT-002 | Nhập tên và chọn thành viên rồi yêu cầu tạo nhóm chat. | Tạo nhóm chat | G-ABC có tên Ôn thi Lý, A Admin nhóm chat, B/C Member, tổng 3, công tắc Tắt. Thành viên dùng luồng đọc/gửi riêng khi chủ động yêu cầu. | UC-M16-008, UC-M16-018, UC-M16-019, UC-M16-032 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-006 | FR-M16-02.01, FR-M16-02.02, FR-M16-02.03, FR-M16-02.04, FR-M16-02.05, FR-M16-02.06, FR-M16-02.07, FR-M16-02.08, FR-M16-02.09, BR-M16-01, BR-M16-03, BR-M16-04, BR-M16-06, BR-M16-25, BR-M16-32, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-01.03, FR-M16-03.02, FR-M16-16.02 |
| BF-M16-007 | UC-M16-009 | ACT-012 | Chọn thêm Dũng vào nhóm G-ABC. | Thêm hoặc đề nghị thêm thành viên | D thành Member ngay, tổng 3→4, có quyền đọc toàn lịch sử. | UC-M16-009, UC-M16-018, UC-M16-019, UC-M16-032 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-007 | FR-M16-08.01, FR-M16-08.04, FR-M16-08.05, FR-M16-08.06, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, BR-M16-01, BR-M16-03, BR-M16-06, BR-M16-25, BR-M16-28, FR-M16-02.02, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-27, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-08.03, FR-M16-08.02, FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, FR-M16-04.08, FR-M16-05.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02, FR-M16-04.10 |
| BF-M16-008 | UC-M16-010 | ACT-012 | Yêu cầu lấy link mời của G-ABC. | Lấy link mời nhóm chat | B nhận đúng L-G-ABC sẵn có, tư cách/số người/công tắc giữ nguyên. | UC-M16-010, UC-M16-018, UC-M16-032 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-008 | FR-M16-08.10, FR-M16-08.11, FR-M16-08.12, FR-M16-08.13, BR-M16-29, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02, FR-M16-04.10, BR-M16-27, BR-M16-28 |
| BF-M16-009 | UC-M16-011 | ACT-002 | Mở link mời L-G-ABC để xin gia nhập. | Xin gia nhập qua link mời | D nhận tư cách Member, tổng 3→4, được đọc toàn lịch sử khi mở cuộc. | UC-M16-011, UC-M16-018, UC-M16-019, UC-M16-032 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-009 | FR-M16-16.01, FR-M16-16.02, FR-M16-16.03, FR-M16-16.04, FR-M16-16.05, FR-M16-16.06, FR-M16-16.07, FR-M16-16.08, BR-M16-06, BR-M16-28, BR-M16-29, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, BR-M16-03, BR-M16-25, BR-M16-27, FR-M07-09.08, BR-M07-08, FR-M16-10.04, FR-M16-01.03, FR-M16-02.06, FR-M16-03.02 |
| BF-M16-010 | UC-M16-012 | ACT-013 | Mở danh sách người chờ của G98 để duyệt. | Duyệt người chờ vào nhóm chat | P-D Đã chấp nhận và D Member, tổng 98→99. Admin nhận kết quả quyết định. | UC-M16-012, UC-M16-018, UC-M16-019, UC-M16-032 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-010 | FR-M16-10.01, FR-M16-10.02, FR-M16-10.03, FR-M16-10.04, FR-M16-10.05, FR-M16-10.06, FR-M16-10.07, BR-M16-03, BR-M16-05, BR-M16-06, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-16.03, FR-M16-16.08, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-16.07, FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02, FR-M16-04.10 |
| BF-M16-011 | UC-M16-013 | ACT-013 | Chọn Tắt duyệt thành viên mới cho G98. | Bật hoặc tắt duyệt thành viên mới | Công tắc Tắt, Q1/Q2 Đã chấp nhận và 2 Member mới, Q3/Q4/Q5 Đã từ chối, tổng 98→100. Không giữ người dư Chờ duyệt. | UC-M16-013, UC-M16-018, UC-M16-019, UC-M16-020, UC-M16-033 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-011 | FR-M16-09.01, FR-M16-09.02, FR-M16-09.03, FR-M16-09.04, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, BR-M16-06, BR-M16-33, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-08.02, FR-M16-08.03, FR-M16-16.04, FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02, FR-M16-04.10 |
| BF-M16-012 | UC-M16-014 | ACT-013 | Chọn xóa Member C khỏi G-ABC. | Xóa Member khỏi nhóm chat | C Bị xóa cutoff21:00, tổng 3→2, A/B vẫn nhắn và thêm được. C giữ hộp thư và lịch sử trước cutoff, mute riêng bị bỏ theo M07. | UC-M16-014, UC-M16-018, UC-M16-033 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-012 | FR-M16-11.01, FR-M16-11.02, FR-M16-11.03, FR-M16-14.03, BR-M16-03, BR-M16-05, BR-M16-27, BR-M16-28, FR-M07-09.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-12.02, FR-M16-13.02, FR-M16-04.10 |
| BF-M16-013 | UC-M16-015 | ACT-012 | Nhập và gửi tên mới cho nhóm G-ABC. | Đổi tên nhóm chat | Tên Ôn thi Toán áp cho mọi thành viên, link L-G-ABC và tư cách giữ nguyên. | UC-M16-015, UC-M16-018, UC-M16-033 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-013 | FR-M16-12.01, FR-M16-12.02, FR-M16-12.03, BR-M16-05, BR-M16-29, BR-M16-32, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-13.02, FR-M16-04.10, BR-M16-27, BR-M16-28 |
| BF-M16-014 | UC-M16-016 | ACT-013 | Chọn Member B nhận quyền Admin nhóm chat của G-ABC. | Chuyển quyền Admin nhóm chat | Sau B Admin, A/C Member, tổng 3 giữ3, tối đa1 Admin, A chưa rời nhóm. | UC-M16-016, UC-M16-018, UC-M16-033 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-014 | FR-M16-13.01, FR-M16-13.02, FR-M16-13.03, FR-M16-14.02, BR-M16-04, BR-M16-05, BR-M16-07, BR-M16-25, BR-M16-30, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-04.10, BR-M16-27, BR-M16-28 |
| BF-M16-015 | UC-M16-017 | ACT-012 | Chọn rời nhóm chat G-ABC. | Rời nhóm chat | B Đã rời cutoff21:00, tổng 3→2, chỉ lịch sử trước cutoff cho B. A/C vẫn hoạt động, B không còn gửi/quản lý, mute riêng bị bỏ. | UC-M16-017, UC-M16-018, UC-M16-033 | Actor yêu cầu chức năng trọn vẹn và nhận kết quả từ SYSTEM, không dừng ở kiểm tra hoặc tạo trạng thái trung gian ngoài mục tiêu. | SC-M16-015 | FR-M16-14.01, FR-M16-14.02, FR-M16-14.03, FR-M16-14.04, FR-M16-14.05, BR-M16-03, BR-M16-05, BR-M16-07, BR-M16-18, BR-M16-27, BR-M16-28, FR-M07-09.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02, FR-M16-04.10 |


### Điểm gọi include

| UC nguồn | UC được gọi | Guard nguồn | Điểm triển khai và trở về |
|---|---|---|---|
| UC-M16-001 | UC-M16-018 | Mỗi yêu cầu bắt đầu/mở lại 1-1. | SC-M16-001 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-001 | UC-M16-003 | Sau chọn/tạo được cuộc hợp lệ. | SC-M16-001 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-002 | UC-M16-018 | Mở/tải thêm hộp thư. | SC-M16-002 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-003 | UC-M16-018 | Mở/tải cuộc với tư cách hợp lệ. | SC-M16-001, SC-M16-003 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-003 | UC-M16-006 | Thành viên hiện tại mở cuộc có tin; không tự áp mốc global cho cựu. | SC-M16-001, SC-M16-003 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-004 | UC-M16-018 | Trước ghi tin. | SC-M16-004 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-004 | UC-M16-006 | Sau ghi thành công tin, cập nhật sender. | SC-M16-004 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-005 | UC-M16-018 | Trước kiểm sở hữu/hạn thu hồi. | SC-M16-005 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-006 | UC-M16-007 | Ghi/xét mốc hợp lệ, suy dữ liệu trạng thái của tin mới nhất. | SC-M16-001, SC-M16-003, SC-M16-004 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-008 | UC-M16-018 | Mỗi yêu cầu theo vai trò/phạm vi thao tác. | SC-M16-006 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-009 | UC-M16-018 | Mỗi yêu cầu theo vai trò/phạm vi thao tác. | SC-M16-007 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-010 | UC-M16-018 | Mỗi yêu cầu theo vai trò/phạm vi thao tác. | SC-M16-008 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-011 | UC-M16-018 | Mỗi yêu cầu theo vai trò/phạm vi thao tác. | SC-M16-009 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-012 | UC-M16-018 | Mỗi yêu cầu theo vai trò/phạm vi thao tác. | SC-M16-010 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-013 | UC-M16-018 | Mỗi yêu cầu theo vai trò/phạm vi thao tác. | SC-M16-011 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-014 | UC-M16-018 | Mỗi yêu cầu theo vai trò/phạm vi thao tác. | SC-M16-012 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-015 | UC-M16-018 | Mỗi yêu cầu theo vai trò/phạm vi thao tác. | SC-M16-013 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-016 | UC-M16-018 | Mỗi yêu cầu theo vai trò/phạm vi thao tác. | SC-M16-014 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-017 | UC-M16-018 | Mỗi yêu cầu theo vai trò/phạm vi thao tác. | SC-M16-015 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-008 | UC-M16-019 | Từng người được chọn hợp lệ khi tạo, không gồm người tạo đã là Admin. | SC-M16-006 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-009 | UC-M16-019 | Admin nhóm chat thêm hoặc công tắc Tắt; không gọi ở nhánh đề nghị chờ. | SC-M16-007 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-011 | UC-M16-019 | Công tắc Tắt, sau kiểm request/link. | SC-M16-009 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-012 | UC-M16-019 | Quyết định Chấp nhận còn hợp lệ; Từ chối không admission. | SC-M16-010 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-013 | UC-M16-020 | Hành động Tắt duyệt; Bật không nhả hàng chờ. | SC-M16-011 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |
| UC-M16-020 | UC-M16-019 | Theo FIFO từng người chờ còn chỗ; không qua cổng của Admin đã mất quyền trong AUT. | SC-M16-011 — các xử lý liên tiếp cùng SYSTEM được gộp, kết quả trả về trong cùng lượt hoặc nhánh E, không thêm thao tác actor giả. |


## 3. Dữ liệu minh họa và ranh giới

Mỗi D là một snapshot độc lập, E thay dữ liệu đúng guard từ đầu. Nhóm G-ABC xuất hiện ở nhiều D để minh họa cùng loại đối tượng, không ghép các D thành một chuỗi giao dịch. Số bước do tương tác cần thiết quyết định, không tự thêm xác nhận hoặc nút khi HMI chưa chốt.

| Dữ liệu | Trước và quy tắc | Kết quả minh họa |
|---|---|---|
| D1 | A/B ACTIVE khác nhau, chưa follow, chưa có cuộc, hoặc biến thể45 tin | Một cuộc mỗi cặp, mới rỗng hoặc mở lại lịch sử cũ |
| D2 | 23 cuộc hợp lệ, thời điểm tin cuối phân biệt và1 cuộc1-1 rỗng | 20+3 cuộc, rỗng1-1 bị loại, cựu tính theo tin trước cutoff |
| D3 | G45 có 45 tin, A current mốc 40, hoặc cựu cutoff21:00 tại tin 60 | Trang26–45, 6–25, 1–5. Cựu chỉ tới 60 dù toàn cuộc đã80 |
| D4 | t10:00:59 có 30 tin, 1 tin ở10:00:00. Giới hạn theo người/cuộc | 10:00:59 từ chối, 10:01:00 bỏ lượt đúng 60 giây, nhận nếu còn 29 |
| D5 | Tin50 gửi20:00:00, hạn300 giây | 20:04:59 và20:05:00 được, 20:05:01 bị từ chối. Placeholder giữ vị trí/tin cuối |
| D6 | A tạo với B/C, tên trim Ôn thi Lý dài9 ký tự | Tổng3, A Admin, B/C Member, công tắc Tắt. Kiểm biên2/3/100/101 và1/100/101 ký tự |
| D7–D10 | Thêm/link/duyệt dữ liệu ACTIVE, pending phân biệt, nhóm chưa đầy | Vào ngay hoặc ghi pending đúng công tắc/vai trò. Duyệt tay đầy từ chối thao tác |
| D11 | 98 thành viên, 5 pending Q1–Q5 thời gian09:01–09:05, hai loại xen kẽ | FIFO Q1/Q2 vào đủ100, Q3–Q5 Đã từ chối. 50+5→55, 100+5→100 |
| D12–D15 | Xóa/rời cutoff21:00, Member/Admin theo từng D | Bị xóa khác Đã rời, còn 2/1 vẫn hoạt động, Admin cuối được rời thành0 |


## 4. Scenario

<a id="sc-m16-001"></a>

<!-- sc:scenario SC-M16-001 -->

### SC-M16-001

#### 1. Tên kịch bản chuẩn

Bắt đầu hoặc mở lại trò chuyện 1-1 — BF-M16-001. UC owner [UC-M16-001](../../us/US-M16.md#uc-m16-001).

#### 2. Actor thực hiện

ACT-002 — Người dùng đã đăng nhập khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Có định danh người gọi và người nhận. Đường chuẩn dùng D1 mới, cờ Bật. Phiên, cờ, tự nhắn và trạng thái người nhận được kiểm trong luồng. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-001 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. Mở C-AB duy nhất của A–B với đúng hai thành viên, lịch sử rỗng, chưa có tin gửi. C-AB giữ 45 tin, hai thành viên và định danh cuộc cũ. Mốc A #40→#45. Với snapshot ACTIVE, #45 do A gửi, mốc B=#44 nên Đã gửi. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-001 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Chọn người nhận từ hồ sơ để bắt đầu hoặc mở lại trò chuyện 1-1. | An=A, Bình=B, A≠B, cả hai ACTIVE, chưa có cuộc của cặp, không theo dõi nhau. | M2 | FR-M16-01.01, FR-M16-01.02, FR-M16-01.03, FR-M16-01.04, FR-M16-01.05, FR-M16-01.06, FR-M16-01.07, FR-M16-03.07, FR-M16-04.01, BR-M16-01, BR-M16-02, BR-M16-24, BR-M16-25, BR-M16-31, FR-M02-01.26 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Xác định chưa có cuộc của cặp An–Bình, hai tài khoản khác nhau và Bình ACTIVE. Tạo cuộc C-AB đúng hai thành viên, không đòi follow, cùng Group hoặc chấp nhận nhắn tin. Mở cuộc theo UC-M16-003, trả lịch sử rỗng, chưa tạo mốc/receipt khi chưa có tin. Chưa liệt kê C-AB trong hộp thư. Gửi tin đầu tiên là mục tiêu SC-M16-004. | Mở C-AB duy nhất của A–B với đúng hai thành viên, lịch sử rỗng, chưa có tin gửi. | END:SUCCESS | FR-M16-01.01, FR-M16-01.02, FR-M16-01.03, FR-M16-01.04, FR-M16-01.05, FR-M16-01.06, FR-M16-01.07, FR-M16-03.07, FR-M16-04.01, BR-M16-01, BR-M16-02, BR-M16-24, BR-M16-25, BR-M16-31, FR-M02-01.26, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-001 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Đã có C-AB, gồm trường hợp Bình BANNED, DEACTIVATED hoặc DELETED. | E1.1 | FR-M16-01.05, FR-M16-04.01, FR-M16-04.04, FR-M16-04.07, FR-M16-04.09, FR-M16-04.11, FR-M16-04.12, FR-M16-05.13, FR-M16-05.14, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-24, BR-M16-25, BR-M16-26 |
| E2 | system | M2 | Người nhận chính là A. | E2.1 | FR-M16-01.06, BR-M16-24 |
| E3 | system | M2 | Chưa có cuộc với đích BANNED, DEACTIVATED hoặc DELETED. | E3.1 | FR-M16-01.07, BR-M16-25 |
| E4 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E4.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E5 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E5.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E6 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E6.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E7 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E7.1 | FR-M16-01.01, FR-M16-01.02, FR-M16-01.03, FR-M16-01.04, FR-M16-01.05, FR-M16-01.06, FR-M16-01.07, FR-M16-03.07, FR-M16-04.01, BR-M16-01, BR-M16-02, BR-M16-24, BR-M16-25, BR-M16-31, FR-M02-01.26, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |


<!-- sc:branch SC-M16-001 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Tái sử dụng C-AB và mở lịch sử được phép qua UC-M16-003. Tải #26–#45 trong 45 tin, có thể cuộn lên theo SC-M16-003. Đưa mốc A tới #45 không lùi, suy receipt của tin cuối và cung cấp M07 cuộc đang mở. Bình DELETED hiện [Người dùng đã xóa], DEACTIVATED hiện Tài khoản tạm thời vô hiệu hoá cùng avatar mặc định, BANNED hiện như bình thường. Quyền gửi tiếp kiểm ở SC-M16-004. | C-AB giữ 45 tin, hai thành viên và định danh cuộc cũ. Mốc A #40→#45. Với snapshot ACTIVE, #45 do A gửi, mốc B=#44 nên Đã gửi. | END:SUCCESS | FR-M16-01.05, FR-M16-04.01, FR-M16-04.04, FR-M16-04.07, FR-M16-04.09, FR-M16-04.11, FR-M16-04.12, FR-M16-05.13, FR-M16-05.14, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-24, BR-M16-25, BR-M16-26 |


<!-- sc:branch SC-M16-001 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Từ chối bắt đầu cuộc tự nhắn và trả kết quả yêu cầu. | Đích A, không tạo cuộc tự nhắn. | END:REJECTED | FR-M16-01.06, BR-M16-24 |


<!-- sc:branch SC-M16-001 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Từ chối bắt đầu cuộc mới với tài khoản đích ở trạng thái đã chọn. | D1 đích X, chưa có C-AX, không tạo mới C-AX. | END:REJECTED | FR-M16-01.07, BR-M16-25 |


<!-- sc:branch SC-M16-001 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-001 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E6 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-001 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-001 | Chọn người nhận từ hồ sơ để bắt đầu hoặc mở lại trò chuyện 1-1. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E6.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E6.2 | SYSTEM | Từ chối yêu cầu Chat của Guest, trả kết quả không được thực hiện chức năng này. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E7 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-001 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-007 | Chọn người nhận từ hồ sơ để bắt đầu hoặc mở lại trò chuyện 1-1. | An=A, Bình=B, A≠B, cả hai ACTIVE, chưa có cuộc của cặp, không theo dõi nhau. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E7.2 | FR-M16-01.01, FR-M16-01.02, FR-M16-01.03, FR-M16-01.04, FR-M16-01.05, FR-M16-01.06, FR-M16-01.07, FR-M16-03.07, FR-M16-04.01, BR-M16-01, BR-M16-02, BR-M16-24, BR-M16-25, BR-M16-31, FR-M02-01.26, FR-M16-15.04, FR-M10-12.08 |
| E7.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Xác định chưa có cuộc của cặp An–Bình, hai tài khoản khác nhau và Bình ACTIVE. Tạo cuộc C-AB đúng hai thành viên, không đòi follow, cùng Group hoặc chấp nhận nhắn tin. Mở cuộc theo UC-M16-003, trả lịch sử rỗng, chưa tạo mốc/receipt khi chưa có tin. Chưa liệt kê C-AB trong hộp thư. Gửi tin đầu tiên là mục tiêu SC-M16-004. | Mở C-AB duy nhất của A–B với đúng hai thành viên, lịch sử rỗng, chưa có tin gửi. | END:SUCCESS | FR-M16-01.01, FR-M16-01.02, FR-M16-01.03, FR-M16-01.04, FR-M16-01.05, FR-M16-01.06, FR-M16-01.07, FR-M16-03.07, FR-M16-04.01, BR-M16-01, BR-M16-02, BR-M16-24, BR-M16-25, BR-M16-31, FR-M02-01.26, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


<!-- sc:end SC-M16-001 -->

<a id="sc-m16-002"></a>

<!-- sc:scenario SC-M16-002 -->

### SC-M16-002

#### 1. Tên kịch bản chuẩn

Xem hộp thư Chat — BF-M16-002. UC owner [UC-M16-002](../../us/US-M16.md#uc-m16-002).

#### 2. Actor thực hiện

ACT-002 — Người dùng đã đăng nhập khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Hộp thư thuộc người gọi. D2 có dữ liệu đã nêu, việc chưa có cuộc và không có phiên là nhánh. Không giả định có tin trong mọi nhóm mới tạo. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-002 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. A nhận 20 cuộc ở lần đầu và 3 cuộc kế tiếp khi chọn tải thêm, tổng 23 cuộc hợp lệ, theo thứ tự tin cuối được thấy và nhãn chưa đọc đúng phạm vi. 0 cuộc, không tạo cuộc/tin để lấp danh sách. D2 tổng 23 cuộc hợp lệ đã được trả, cuộc thứ 24 là 1-1 rỗng vẫn bị loại. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-002 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Mở hộp thư Chat từ biểu tượng Tin nhắn. | D2 có 23 cuộc hợp lệ và 1 cuộc 1-1 rỗng bị loại, thời điểm tin cuối phân biệt. | M2 | FR-M16-03.01, FR-M16-03.02, FR-M16-03.03, FR-M16-03.04, FR-M16-03.05, FR-M16-03.06, FR-M16-03.07, FR-M16-03.08, FR-M16-07.10, BR-M16-26, BR-M16-27, BR-M16-31, FR-M07-07.02, FR-M07-07.03 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Chọn cuộc mà A là thành viên hoặc thành viên cũ. Loại 1-1 chưa tin. Xếp theo thời điểm tin cuối A được thấy giảm dần, trả tối đa 20 cuộc, tên nhóm hoặc display_name/avatar người kia, snippet hoặc placeholder thu hồi và thời điểm UTC+7. Đánh dấu chưa đọc chỉ với tin được thấy mới hơn mốc A, cùng ngữ nghĩa M07. Với nhóm cũ chỉ dùng tin trước cutoff cho snippet, thời gian, thứ tự và chưa đọc. | 20 cuộc đầu của A được trả theo thứ tự D2, nhãn chưa đọc theo phạm vi thấy được, chưa mở các cuộc chỉ vì xem hộp thư. | M3 | FR-M16-03.01, FR-M16-03.02, FR-M16-03.03, FR-M16-03.04, FR-M16-03.05, FR-M16-03.06, FR-M16-03.07, FR-M16-03.08, FR-M16-07.10, BR-M16-26, BR-M16-27, BR-M16-31, FR-M07-07.02, FR-M07-07.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| M3 | ACT-002 | Cuộn xuống để tải tiếp hộp thư. | D2 đã tải dòng 1–20, còn 3 cuộc. | M4 | FR-M16-03.08 |
| M4 | SYSTEM | Kiểm quyền lại và trả 3 cuộc kế tiếp theo cùng phạm vi/thứ tự. Một chu kỳ tải thêm tối đa 20 được lặp khi còn cuộc và người dùng tiếp tục cuộn, dừng khi hết hoặc ngừng yêu cầu tải. | D2 tổng 23 cuộc hợp lệ đã được trả, cuộc thứ 24 là 1-1 rỗng vẫn bị loại. | END:SUCCESS | FR-M16-03.07, FR-M16-03.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, BR-M16-31 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-002 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Không có cuộc hợp lệ hoặc chỉ có 1-1 rỗng. | E1.1 | FR-M16-03.01, FR-M16-03.07, BR-M16-31 |
| E2 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E2.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E3 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E3.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E4 | system | M4 | Cờ Chat Tắt với người không ADMIN tại yêu cầu tải tiếp ở bước M3. | E4.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E5 | system | M4 | Tài khoản BANNED hoặc phiên không còn hợp lệ tại yêu cầu tải tiếp. | E5.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E6 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E6.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E7 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E7.1 | FR-M16-03.01, FR-M16-03.02, FR-M16-03.03, FR-M16-03.04, FR-M16-03.05, FR-M16-03.06, FR-M16-03.07, FR-M16-03.08, FR-M16-07.10, BR-M16-26, BR-M16-27, BR-M16-31, FR-M07-07.02, FR-M07-07.03, FR-M16-15.04, FR-M10-12.08, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |


<!-- sc:branch SC-M16-002 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Kiểm quyền và trả tập hộp thư hợp lệ rỗng. Nội dung trạng thái rỗng và CTA nằm ở GAP-SC-M16-002. | 0 cuộc, không tạo cuộc/tin để lấp danh sách. | END:SUCCESS | FR-M16-03.01, FR-M16-03.07, BR-M16-31 |


<!-- sc:branch SC-M16-002 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-002 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


<!-- sc:branch SC-M16-002 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Kiểm quyền ở yêu cầu tải tiếp và từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Trả kết quả không tải trang tiếp, giữ dữ liệu và không làm bù yêu cầu khi cờ bật lại. | Phần đã trả ở các bước trước giữ phạm vi quyền khi được trả. Yêu cầu tải tiếp hiện tại bị từ chối, chính sách stream đang mở giữ GAP-SC-M16-001. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


<!-- sc:branch SC-M16-002 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Kiểm trạng thái/phiên ở yêu cầu hiện tại và từ chối tải thêm, không dựa vào quyền ở lần tải trước. | Không trả trang tiếp theo cho yêu cầu bị chặn. Dữ liệu lưu của cuộc/tin được giữ theo chính sách nguồn. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


**E6 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-002 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-001 | Mở hộp thư Chat từ biểu tượng Tin nhắn. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E6.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E6.2 | SYSTEM | Từ chối yêu cầu Chat của Guest, trả kết quả không được thực hiện chức năng này. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E7 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-002 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-007 | Mở hộp thư Chat từ biểu tượng Tin nhắn. | D2 có 23 cuộc hợp lệ và 1 cuộc 1-1 rỗng bị loại, thời điểm tin cuối phân biệt. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E7.2 | FR-M16-03.01, FR-M16-03.02, FR-M16-03.03, FR-M16-03.04, FR-M16-03.05, FR-M16-03.06, FR-M16-03.07, FR-M16-03.08, FR-M16-07.10, BR-M16-26, BR-M16-27, BR-M16-31, FR-M07-07.02, FR-M07-07.03, FR-M16-15.04, FR-M10-12.08 |
| E7.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Chọn cuộc mà A là thành viên hoặc thành viên cũ. Loại 1-1 chưa tin. Xếp theo thời điểm tin cuối A được thấy giảm dần, trả tối đa 20 cuộc, tên nhóm hoặc display_name/avatar người kia, snippet hoặc placeholder thu hồi và thời điểm UTC+7. Đánh dấu chưa đọc chỉ với tin được thấy mới hơn mốc A, cùng ngữ nghĩa M07. Với nhóm cũ chỉ dùng tin trước cutoff cho snippet, thời gian, thứ tự và chưa đọc. | 20 cuộc đầu của A được trả theo thứ tự D2, nhãn chưa đọc theo phạm vi thấy được, chưa mở các cuộc chỉ vì xem hộp thư. | E7.3 | FR-M16-03.01, FR-M16-03.02, FR-M16-03.03, FR-M16-03.04, FR-M16-03.05, FR-M16-03.06, FR-M16-03.07, FR-M16-03.08, FR-M16-07.10, BR-M16-26, BR-M16-27, BR-M16-31, FR-M07-07.02, FR-M07-07.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E7.3 | ACT-007 | Cuộn xuống để tải tiếp hộp thư. | D2 đã tải dòng 1–20, còn 3 cuộc. | E7.4 | FR-M16-03.08, FR-M16-15.04, FR-M10-12.08 |
| E7.4 | SYSTEM | Kiểm quyền lại và trả 3 cuộc kế tiếp theo cùng phạm vi/thứ tự. Một chu kỳ tải thêm tối đa 20 được lặp khi còn cuộc và người dùng tiếp tục cuộn, dừng khi hết hoặc ngừng yêu cầu tải. | D2 tổng 23 cuộc hợp lệ đã được trả, cuộc thứ 24 là 1-1 rỗng vẫn bị loại. | END:SUCCESS | FR-M16-03.07, FR-M16-03.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, BR-M16-31 |


<!-- sc:end SC-M16-002 -->

<a id="sc-m16-003"></a>

<!-- sc:scenario SC-M16-003 -->

### SC-M16-003

#### 1. Tên kịch bản chuẩn

Xem cuộc trò chuyện và lịch sử — BF-M16-003. UC owner [UC-M16-003](../../us/US-M16.md#uc-m16-003).

#### 2. Actor thực hiện

ACT-012 — Thành viên cuộc trò chuyện khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Có cuộc G45, người xem và tư cách theo D3. Tải trang đầu là một kết quả đọc hợp lệ. Các bước M3–M6 minh họa lựa chọn xem tiếp tới tin đầu, không bắt buộc mọi lần đọc phải cuộn hết. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-003 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. A nhận trang #26–#45 khi mở, rồi #6–#25 và #1–#5 khi cuộn lên, đọc được toàn bộ 45 tin. Mốc A từ #40 tới #45 và không lùi do tải tin cũ, receipt tin cuối theo từng viewer. D3-rỗng có 0 tin, không có ứng viên ghi mốc. Mốc A #45→#46, tin #46 được tính đã đọc của A, trạng thái/avatars theo mốc từng thành viên. Mốc A #45→#46, chưa đọc trong cuộc được tính lại cho M07. Cửa sổ hiển thị, đang đọc cũ, tin #46 còn chưa đọc của A. A current, mốc #45→#46, B gửi #46, không cần tải lại trang. D3-sole B gửi #45, mốc B=#45, C/D=#40, A mở và mốc #40→#45. A thấy Đã xem với danh sách avatar rỗng. Cựu chỉ đọc #1–#60, không thấy hoạt động sau cutoff. A xem được #1–#45, mốc #45, không có tin cũ hơn #1. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-003 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-012 | Mở nhóm G45 để đọc cuộc trò chuyện và lịch sử. | D3 G45 có #1–#45, A current, mốc A=#40, #45 do B gửi, B/C đã đọc #45, D=#42. | M2 | FR-M16-04.01, FR-M16-04.02, FR-M16-04.03, FR-M16-04.04, FR-M16-04.05, FR-M16-04.06, FR-M16-04.07, FR-M16-04.08, FR-M16-04.09, FR-M16-04.10, FR-M16-04.11, FR-M16-04.12, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-12, BR-M16-17, BR-M16-19, BR-M16-26, BR-M16-27, FR-M01-13.06, FR-M01-13.07 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Trả #26–#45 trong D3 theo trang 20 tin, mỗi tin có người gửi/nội dung/thời điểm UTC+7. Mở cuộc current có tin gọi UC-M16-006 với #45. Ghi một mốc mỗi người mỗi cuộc bằng tin mới hơn giữa mốc hiện tại và ứng viên qua UC-M16-006. UC-M16-007 suy Đã xem khi có thành viên khác người gửi đọc tới tin cuối, còn lại Đã gửi. Chỉ tin cuối có trạng thái, avatar loại người gửi và chính người xem, gộp nhiều người, loại người chưa đọc tới. Cập nhật receipt ngay cho các view hợp lệ và cung cấp mốc/tin chưa đọc được thấy cho M07. Cung cấp M07 cuộc đang mở. Tin đã thu hồi hiển thị placeholder tại vị trí cũ. Người gửi DELETED dùng [Người dùng đã xóa], DEACTIVATED dùng Tài khoản tạm thời vô hiệu hoá/avatar mặc định, BANNED dùng danh tính bình thường. | A nhận #26–#45, mốc #40→#45. Tin #45 Đã xem, A xem thấy avatar C, loại B người gửi và A người xem. D chưa đọc không có avatar, tin cũ không có trạng thái. | M3 | FR-M16-04.01, FR-M16-04.02, FR-M16-04.03, FR-M16-04.04, FR-M16-04.05, FR-M16-04.06, FR-M16-04.07, FR-M16-04.08, FR-M16-04.09, FR-M16-04.10, FR-M16-04.11, FR-M16-04.12, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-12, BR-M16-17, BR-M16-19, BR-M16-26, BR-M16-27, FR-M01-13.06, FR-M01-13.07, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| M3 | ACT-012 | Cuộn lên đến tin cũ nhất đang hiển thị. | Đang có #26–#45, yêu cầu tin trước #26. | M4 | FR-M16-04.02 |
| M4 | SYSTEM | Kiểm quyền rồi trả 20 tin cũ hơn #6–#25, giữ vị trí đọc. Không đưa mốc từ #45 lùi xuống #25. | A đã thấy #6–#45, mốc A vẫn #45. | M5 | FR-M16-04.02, FR-M16-04.03, FR-M16-07.05, BR-M16-13, BR-M16-17, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| M5 | ACT-012 | Cuộn lên tiếp đến đầu phần lịch sử đã tải. | Yêu cầu các tin trước #6. | M6 | FR-M16-04.02, FR-M16-04.03 |
| M6 | SYSTEM | Kiểm quyền, trả #1–#5 và dừng tải cũ vì đã tới tin đầu. Cùng chu kỳ 20 tin mỗi lần áp cho lịch sử dài hơn, không giới hạn tổng. AUT-M16-002/003 áp cho tin mới trong lúc đọc theo các nhánh E. | A xem được #1–#45, mốc #45, không có tin cũ hơn #1. | END:SUCCESS | FR-M16-04.01, FR-M16-04.02, FR-M16-04.03, FR-M16-04.05, FR-M16-04.06, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, BR-M16-17 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-003 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Cuộc chưa có tin khi mở. | E1.1 | FR-M16-04.01, FR-M16-04.03, FR-M16-04.09, BR-M16-15, BR-M16-17 |
| E2 | system | M4 | Tin #46 mới tới lúc A đang đọc tin cũ ở #10, sau đó A chọn cuộn về cuối. | E2.1 | FR-M16-04.05, FR-M16-04.06, FR-M16-04.09, FR-M16-07.04, FR-M07-07.06, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, BR-M07-02, BR-M07-08 |
| E3 | user-choice | M3 | Cửa sổ đang ẩn nhận tin #46, A quay lại cửa sổ đang ở cuối. | E3.1 | FR-M16-07.03, FR-M16-04.05, BR-M16-14, FR-M16-07.01, FR-M16-07.02, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08 |
| E4 | user-choice | M3 | Cửa sổ hiện lại nhưng A vẫn ở phần tin cũ, chưa chọn cuộn tới cuối. | E4.1 | FR-M16-04.06, FR-M16-07.03, FR-M16-07.04, BR-M16-14 |
| E5 | system | M2 | Tin mới tới khi A đang xem ở cuối và cửa sổ hiển thị. | E5.1 | FR-M16-04.05, FR-M16-07.02, FR-M16-07.01, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08 |
| E6 | system | M2 | A mở cuộc và là người duy nhất ngoài người gửi B đã đọc tin mới nhất #45. | E6.1 | FR-M16-04.01, FR-M16-07.01, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, BR-M16-13, BR-M16-15 |
| E7 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E7.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E8 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E8.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E9 | system | M4 | Cờ Chat Tắt với người không ADMIN tại yêu cầu tải tiếp ở bước M3. | E9.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E10 | system | M4 | Tài khoản BANNED hoặc phiên không còn hợp lệ tại yêu cầu tải tiếp. | E10.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E11 | system | M6 | Cờ Chat Tắt với người không ADMIN tại yêu cầu tải tiếp ở bước M5. | E11.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E12 | system | M6 | Tài khoản BANNED hoặc phiên không còn hợp lệ tại yêu cầu tải tiếp. | E12.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E13 | system | M1 | ACT-014 — A đã rời hoặc bị xóa lúc 21:00, tin #60 gửi 20:59, #61–#80 gửi sau 21:00. | E13.1 | FR-M16-04.10, FR-M16-04.01, FR-M16-07.10, BR-M16-17, BR-M16-27, FR-M16-04.02, FR-M16-04.03 |
| E14 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E14.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E15 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E15.1 | FR-M16-04.01, FR-M16-04.02, FR-M16-04.03, FR-M16-04.04, FR-M16-04.05, FR-M16-04.06, FR-M16-04.07, FR-M16-04.08, FR-M16-04.09, FR-M16-04.10, FR-M16-04.11, FR-M16-04.12, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-12, BR-M16-17, BR-M16-19, BR-M16-26, BR-M16-27, FR-M01-13.06, FR-M01-13.07, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| E16 | system | M1 | ACT-002 — Người dùng ngoài cuộc, chưa từng là thành viên nhóm. | E16.1 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| E17 | system | M1 | ACT-008 — Staff ACTIVE ngoài cuộc, cờ Bật hoặc ADMIN khi cờ Tắt. | E17.1 | FR-M16-04.08, FR-M16-05.06, FR-M16-15.04 |
| E18 | system | M1 | ACT-007 — Staff ACTIVE ngoài cuộc, cờ Bật hoặc ADMIN khi cờ Tắt. | E18.1 | FR-M16-04.08, FR-M16-05.06, FR-M16-15.04 |


<!-- sc:branch SC-M16-003 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Kiểm quyền, trả lịch sử rỗng, không tạo tin/mốc/receipt giả. Cung cấp cuộc đang mở cho M07. | D3-rỗng có 0 tin, không có ứng viên ghi mốc. | END:SUCCESS | FR-M16-04.01, FR-M16-04.03, FR-M16-04.09, BR-M16-15, BR-M16-17 |


<!-- sc:branch SC-M16-003 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Trả trang cũ #6–#25 mà M3 yêu cầu. Khi A đang tại #10 và tin #46 mới tới, AUT-M16-002 hiển thị tin ngay, giữ vị trí #10, hiện nhãn tin nhắn mới. Chưa ghi mốc tới #46, M07 nhận cuộc đang mở nên không popup. | Snapshot độc lập có #1–#46, trước tin mới mốc A=#45, sau tin tới vẫn #45. | E2.2 | FR-M16-04.05, FR-M16-04.06, FR-M16-04.09, FR-M16-07.04, FR-M07-07.06 |
| E2.2 | ACT-012 | Cuộn xuống tới cuối cuộc để đọc tin mới. | Cửa sổ hiển thị, tới #46. | E2.3 | FR-M16-07.04 |
| E2.3 | SYSTEM | Ghi một mốc mỗi người mỗi cuộc bằng tin mới hơn giữa mốc hiện tại và ứng viên qua UC-M16-006. UC-M16-007 suy Đã xem khi có thành viên khác người gửi đọc tới tin cuối, còn lại Đã gửi. Chỉ tin cuối có trạng thái, avatar loại người gửi và chính người xem, gộp nhiều người, loại người chưa đọc tới. Cập nhật receipt ngay cho các view hợp lệ và cung cấp mốc/tin chưa đọc được thấy cho M07. AUT-M16-003 ghi ứng viên #46 khi hiển thị và ở cuối. | Mốc A #45→#46, tin #46 được tính đã đọc của A, trạng thái/avatars theo mốc từng thành viên. | END:SUCCESS | FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08 |


<!-- sc:branch SC-M16-003 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-012 | Chuyển cửa sổ cuộc trò chuyện sang trạng thái ẩn khi danh sách đang ở cuối. | Sau M2 đã mở và đọc tới #45, A chuyển sang cửa sổ khác. | E3.2 | FR-M16-07.03 |
| E3.2 | SYSTEM | Hoãn ghi mốc cho tin mới trong khi cửa sổ ẩn. AUT-M16-002 giữ tin để view hợp lệ hiển thị theo yêu cầu thời gian thực, không coi đã giao là đã đọc. | Mốc A=#45, tin cuối #46 do B, cửa sổ ẩn. | E3.3 | FR-M16-04.05, FR-M16-07.03, BR-M16-14 |
| E3.3 | ACT-012 | Đưa cửa sổ cuộc trò chuyện hiển thị lại tại cuối danh sách. | A trở về view ở cuối #46. | E3.4 | FR-M16-07.03 |
| E3.4 | SYSTEM | Ghi một mốc mỗi người mỗi cuộc bằng tin mới hơn giữa mốc hiện tại và ứng viên qua UC-M16-006. UC-M16-007 suy Đã xem khi có thành viên khác người gửi đọc tới tin cuối, còn lại Đã gửi. Chỉ tin cuối có trạng thái, avatar loại người gửi và chính người xem, gộp nhiều người, loại người chưa đọc tới. Cập nhật receipt ngay cho các view hợp lệ và cung cấp mốc/tin chưa đọc được thấy cho M07. AUT-M16-003 ghi tới #46 khi đủ cả hiển thị và ở cuối. | Mốc A #45→#46, chưa đọc trong cuộc được tính lại cho M07. | END:SUCCESS | FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08 |


<!-- sc:branch SC-M16-003 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-012 | Cuộn lên phần tin đã tải rồi chuyển cửa sổ sang trạng thái ẩn. | Sau M2 trang #26–#45, A đọc phần #30, mốc đã ghi #45. | E4.2 | FR-M16-04.06, FR-M16-07.03, FR-M16-07.04 |
| E4.2 | SYSTEM | Khi #46 tới, hoãn ghi vì cửa sổ ẩn và vị trí vẫn ở phần cũ. | Mốc A vẫn #45, tin cuối #46. | E4.3 | FR-M16-07.03, BR-M16-14 |
| E4.3 | ACT-012 | Đưa cửa sổ hiển thị lại tại phần tin cũ, chưa cuộn tới cuối. | A vẫn ở #30. | E4.4 | FR-M16-07.03, FR-M16-07.04 |
| E4.4 | SYSTEM | Trả view hợp lệ, giữ vị trí #30 và nhãn tin nhắn mới, mốc vẫn #45. Chỉ sự kiện tới cuối mới ghi #46 như E2. | Cửa sổ hiển thị, đang đọc cũ, tin #46 còn chưa đọc của A. | END:SUCCESS | FR-M16-04.06, FR-M16-07.03, FR-M16-07.04, BR-M16-14 |


<!-- sc:branch SC-M16-003 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Trả trang #26–#45 lúc mở, ghi mốc tới #45. Khi tin #46 tới trong lúc A vẫn ở cuối và cửa sổ hiển thị, AUT-M16-002 hiển thị ngay, AUT-M16-003 ghi tới #46. Ghi một mốc mỗi người mỗi cuộc bằng tin mới hơn giữa mốc hiện tại và ứng viên qua UC-M16-006. UC-M16-007 suy Đã xem khi có thành viên khác người gửi đọc tới tin cuối, còn lại Đã gửi. Chỉ tin cuối có trạng thái, avatar loại người gửi và chính người xem, gộp nhiều người, loại người chưa đọc tới. Cập nhật receipt ngay cho các view hợp lệ và cung cấp mốc/tin chưa đọc được thấy cho M07.  | A current, mốc #45→#46, B gửi #46, không cần tải lại trang. | END:SUCCESS | FR-M16-04.05, FR-M16-07.02, FR-M16-07.01, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08 |


<!-- sc:branch SC-M16-003 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Trả lịch sử, ghi mốc A tới #45, suy trạng thái Đã xem vì A khác người gửi đã đọc. Loại A người xem và B người gửi khỏi avatar, nên danh sách avatar rỗng. Các tin cũ không có trạng thái. | D3-sole B gửi #45, mốc B=#45, C/D=#40, A mở và mốc #40→#45. A thấy Đã xem với danh sách avatar rỗng. | END:SUCCESS | FR-M16-04.01, FR-M16-07.01, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, BR-M16-13, BR-M16-15 |


<!-- sc:branch SC-M16-003 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-003 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


<!-- sc:branch SC-M16-003 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Kiểm quyền ở yêu cầu tải tiếp và từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Trả kết quả không tải trang tiếp, giữ dữ liệu và không làm bù yêu cầu khi cờ bật lại. | Phần đã trả ở các bước trước giữ phạm vi quyền khi được trả. Yêu cầu tải tiếp hiện tại bị từ chối, chính sách stream đang mở giữ GAP-SC-M16-001. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


<!-- sc:branch SC-M16-003 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Kiểm trạng thái/phiên ở yêu cầu hiện tại và từ chối tải thêm, không dựa vào quyền ở lần tải trước. | Không trả trang tiếp theo cho yêu cầu bị chặn. Dữ liệu lưu của cuộc/tin được giữ theo chính sách nguồn. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-003 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | SYSTEM | Kiểm quyền ở yêu cầu tải tiếp và từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Trả kết quả không tải trang tiếp, giữ dữ liệu và không làm bù yêu cầu khi cờ bật lại. | Phần đã trả ở các bước trước giữ phạm vi quyền khi được trả. Yêu cầu tải tiếp hiện tại bị từ chối, chính sách stream đang mở giữ GAP-SC-M16-001. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


<!-- sc:branch SC-M16-003 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | SYSTEM | Kiểm trạng thái/phiên ở yêu cầu hiện tại và từ chối tải thêm, không dựa vào quyền ở lần tải trước. | Không trả trang tiếp theo cho yêu cầu bị chặn. Dữ liệu lưu của cuộc/tin được giữ theo chính sách nguồn. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


**E13 — thay toàn bộ M1 đến kết thúc.** A đã rời hoặc bị xóa lúc 21:00, tin #60 gửi 20:59, #61–#80 gửi sau 21:00.

<!-- sc:branch SC-M16-003 E13 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E13.1 | ACT-014 | Mở lại nhóm cũ để đọc lịch sử. | D3-cựu, cutoff 21:00, trạng thái Đã rời hoặc Bị xóa. | E13.2 | FR-M16-04.10 |
| E13.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Chỉ trả #41–#60 trong trang đầu thuộc phạm vi trước cutoff, chỉ đọc. Giữ nhóm trong hộp thư và tính chưa đọc từ tin trước cutoff. Chính sách mốc/receipt khi cựu đọc lại giữ GAP-SC-M16-003. | Không có #61–#80 trong nội dung trả. Lịch sử trước cutoff giữ nguyên. | E13.3 | FR-M16-04.01, FR-M16-04.10, FR-M16-07.10, BR-M16-17, BR-M16-27 |
| E13.3 | ACT-014 | Cuộn lên xem phần cũ hơn. | Yêu cầu trước #41. | E13.4 | FR-M16-04.02, FR-M16-04.10 |
| E13.4 | SYSTEM | Trả #21–#40 trong phạm vi được xem. Lặp tải tối đa 20 tin khi actor cuộn, tới #1 thì kết thúc tải cũ. | Cựu chỉ đọc #1–#60, không thấy hoạt động sau cutoff. | END:SUCCESS | FR-M16-04.02, FR-M16-04.03, FR-M16-04.10, BR-M16-17, BR-M16-27 |


**E14 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-003 E14 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E14.1 | ACT-001 | Mở nhóm G45 để đọc cuộc trò chuyện và lịch sử. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E14.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E14.2 | SYSTEM | Từ chối yêu cầu Chat của Guest, trả kết quả không được thực hiện chức năng này. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E15 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-003 E15 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E15.1 | ACT-007 | Mở nhóm G45 để đọc cuộc trò chuyện và lịch sử. | D3 G45 có #1–#45, A current, mốc A=#40, #45 do B gửi, B/C đã đọc #45, D=#42. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E15.2 | FR-M16-04.01, FR-M16-04.02, FR-M16-04.03, FR-M16-04.04, FR-M16-04.05, FR-M16-04.06, FR-M16-04.07, FR-M16-04.08, FR-M16-04.09, FR-M16-04.10, FR-M16-04.11, FR-M16-04.12, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-12, BR-M16-17, BR-M16-19, BR-M16-26, BR-M16-27, FR-M01-13.06, FR-M01-13.07, FR-M16-15.04, FR-M10-12.08 |
| E15.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Trả #26–#45 trong D3 theo trang 20 tin, mỗi tin có người gửi/nội dung/thời điểm UTC+7. Mở cuộc current có tin gọi UC-M16-006 với #45. Ghi một mốc mỗi người mỗi cuộc bằng tin mới hơn giữa mốc hiện tại và ứng viên qua UC-M16-006. UC-M16-007 suy Đã xem khi có thành viên khác người gửi đọc tới tin cuối, còn lại Đã gửi. Chỉ tin cuối có trạng thái, avatar loại người gửi và chính người xem, gộp nhiều người, loại người chưa đọc tới. Cập nhật receipt ngay cho các view hợp lệ và cung cấp mốc/tin chưa đọc được thấy cho M07. Cung cấp M07 cuộc đang mở. Tin đã thu hồi hiển thị placeholder tại vị trí cũ. Người gửi DELETED dùng [Người dùng đã xóa], DEACTIVATED dùng Tài khoản tạm thời vô hiệu hoá/avatar mặc định, BANNED dùng danh tính bình thường. | A nhận #26–#45, mốc #40→#45. Tin #45 Đã xem, A xem thấy avatar C, loại B người gửi và A người xem. D chưa đọc không có avatar, tin cũ không có trạng thái. | E15.3 | FR-M16-04.01, FR-M16-04.02, FR-M16-04.03, FR-M16-04.04, FR-M16-04.05, FR-M16-04.06, FR-M16-04.07, FR-M16-04.08, FR-M16-04.09, FR-M16-04.10, FR-M16-04.11, FR-M16-04.12, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-12, BR-M16-17, BR-M16-19, BR-M16-26, BR-M16-27, FR-M01-13.06, FR-M01-13.07, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E15.3 | ACT-007 | Cuộn lên đến tin cũ nhất đang hiển thị. | Đang có #26–#45, yêu cầu tin trước #26. | E15.4 | FR-M16-04.02, FR-M16-15.04, FR-M10-12.08 |
| E15.4 | SYSTEM | Kiểm quyền rồi trả 20 tin cũ hơn #6–#25, giữ vị trí đọc. Không đưa mốc từ #45 lùi xuống #25. | A đã thấy #6–#45, mốc A vẫn #45. | E15.5 | FR-M16-04.02, FR-M16-04.03, FR-M16-07.05, BR-M16-13, BR-M16-17, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E15.5 | ACT-007 | Cuộn lên tiếp đến đầu phần lịch sử đã tải. | Yêu cầu các tin trước #6. | E15.6 | FR-M16-04.02, FR-M16-04.03, FR-M16-15.04, FR-M10-12.08 |
| E15.6 | SYSTEM | Kiểm quyền, trả #1–#5 và dừng tải cũ vì đã tới tin đầu. Cùng chu kỳ 20 tin mỗi lần áp cho lịch sử dài hơn, không giới hạn tổng. AUT-M16-002/003 áp cho tin mới trong lúc đọc theo các nhánh E. | A xem được #1–#45, mốc #45, không có tin cũ hơn #1. | END:SUCCESS | FR-M16-04.01, FR-M16-04.02, FR-M16-04.03, FR-M16-04.05, FR-M16-04.06, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28, BR-M16-17 |


**E16 — thay toàn bộ M1 đến kết thúc.** Người dùng ngoài cuộc, chưa từng là thành viên nhóm.

<!-- sc:branch SC-M16-003 E16 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E16.1 | ACT-002 | Mở nhóm G45 để đọc cuộc trò chuyện và lịch sử. | Cờ Bật, phiên hợp lệ nhưng thiếu vai trò thành viên hiện tại. | E16.2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06 |
| E16.2 | SYSTEM | UC-M16-018 kiểm tư cách đúng cuộc/nhóm và từ chối yêu cầu vì thiếu quyền thành viên hiện tại. | Không đọc dữ liệu hoặc thay đổi trạng thái bằng yêu cầu trái quyền. | END:REJECTED | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |


**E17 — thay toàn bộ M1 đến kết thúc.** Staff ACTIVE ngoài cuộc, cờ Bật hoặc ADMIN khi cờ Tắt.

<!-- sc:branch SC-M16-003 E17 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E17.1 | ACT-008 | Mở nhóm G45 để đọc cuộc trò chuyện và lịch sử. | Staff không là current hoặc former của cuộc được chọn. | E17.2 | FR-M16-04.08, FR-M16-05.06 |
| E17.2 | SYSTEM | Kiểm tư cách và từ chối truy cập cuộc của người khác, kể cả ADMIN đã qua cổng cờ. | Không trả lịch sử hoặc ghi tin gửi trái quyền. | END:REJECTED | FR-M16-04.08, FR-M16-05.06, FR-M16-15.04 |


**E18 — thay toàn bộ M1 đến kết thúc.** Staff ACTIVE ngoài cuộc, cờ Bật hoặc ADMIN khi cờ Tắt.

<!-- sc:branch SC-M16-003 E18 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E18.1 | ACT-007 | Mở nhóm G45 để đọc cuộc trò chuyện và lịch sử. | Staff không là current hoặc former của cuộc được chọn. | E18.2 | FR-M16-04.08, FR-M16-05.06 |
| E18.2 | SYSTEM | Kiểm tư cách và từ chối truy cập cuộc của người khác, kể cả ADMIN đã qua cổng cờ. | Không trả lịch sử hoặc ghi tin gửi trái quyền. | END:REJECTED | FR-M16-04.08, FR-M16-05.06, FR-M16-15.04 |


<!-- sc:end SC-M16-003 -->

<a id="sc-m16-004"></a>

<!-- sc:scenario SC-M16-004 -->

### SC-M16-004

#### 1. Tên kịch bản chuẩn

Gửi tin nhắn văn bản — BF-M16-004. UC owner [UC-M16-004](../../us/US-M16.md#uc-m16-004).

#### 2. Actor thực hiện

ACT-012 — Thành viên cuộc trò chuyện khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Có định danh người gửi/cuộc/nội dung, kiểm quyền và giới hạn trong luồng. D4 là snapshot độc lập. B không cần online và không bắt buộc theo dõi A. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-004 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. Tin #46 nhận 10:01:00, mốc A=#46, B chưa đọc nên Đã gửi, nội dung đến view hợp lệ và sự kiện M07 được cung cấp. Không email, chuông hoặc thông báo được mời. D4-state C-AB có sẵn, tin #46 được giữ để B đọc khi trở lại. D4-boundary 30 lượt trước đó, 1 lượt đúng t−60 giây nên chỉ đếm 29, sau nhận có 30. Cuộc C-AC có cửa sổ riêng. D4-group A ACTIVE current, nhóm có B DELETED vẫn là thành viên, tin #46 do A được nhận. Không áp điều kiện đích 1-1 DELETED lên toàn nhóm. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-004 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-012 | Nhập và gửi tin văn bản “Mai ôn thi nhé 😀” vào C-AB. | D4 A current C-AB, B ACTIVE, t=10:01:00 UTC+7, trước gửi có 29 tin A trong (10:00:00, 10:01:00], mốc A=#45. | M2 | FR-M16-05.01, FR-M16-05.02, FR-M16-05.03, FR-M16-05.04, FR-M16-05.05, FR-M16-05.06, FR-M16-05.07, FR-M16-05.08, FR-M16-05.09, FR-M16-05.10, FR-M16-05.11, FR-M16-05.12, FR-M16-05.13, FR-M16-05.14, FR-M16-01.02, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-08, BR-M16-09, BR-M16-10, BR-M16-18, BR-M16-20, BR-M16-21, BR-M16-25 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm current membership, văn bản/emoji không rỗng/chỉ trắng, tối đa 1.000 từ ngăn cách bằng khoảng trắng, không ảnh/tệp. Đếm riêng (A, C-AB) các tin có thời điểm lớn hơn t−60 giây. Trong 1-1 kiểm B chưa DELETED. Ghi tin #46 với A và thời điểm hệ thống nhận. Ghi một mốc mỗi người mỗi cuộc bằng tin mới hơn giữa mốc hiện tại và ứng viên qua UC-M16-006. UC-M16-007 suy Đã xem khi có thành viên khác người gửi đọc tới tin cuối, còn lại Đã gửi. Chỉ tin cuối có trạng thái, avatar loại người gửi và chính người xem, gộp nhiều người, loại người chưa đọc tới. Cập nhật receipt ngay cho các view hợp lệ và cung cấp mốc/tin chưa đọc được thấy cho M07. Ứng viên của người gửi là #46 theo sự kiện gửi. AUT-M16-002 giao ngay tới thành viên hợp lệ đang mở, cung cấp M07 sự kiện tin mới/thành viên/mốc/cuộc đang mở để thông báo trong ứng dụng. Tin giữ vĩnh viễn, không sửa, không quét AI, không báo cáo/Block ở MS1. Tin đầu 1-1 giao không đợi chấp nhận. | Tin #46 nhận 10:01:00, mốc A=#46, B chưa đọc nên Đã gửi, nội dung đến view hợp lệ và sự kiện M07 được cung cấp. Không email, chuông hoặc thông báo được mời. | END:SUCCESS | FR-M16-05.01, FR-M16-05.02, FR-M16-05.03, FR-M16-05.04, FR-M16-05.05, FR-M16-05.06, FR-M16-05.07, FR-M16-05.08, FR-M16-05.09, FR-M16-05.10, FR-M16-05.11, FR-M16-05.12, FR-M16-05.13, FR-M16-05.14, FR-M16-01.02, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-08, BR-M16-09, BR-M16-10, BR-M16-18, BR-M16-20, BR-M16-21, BR-M16-25, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-004 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Tin trống hoặc chỉ có khoảng trắng. | E1.1 | FR-M16-05.11, BR-M16-08, BR-M16-09, BR-M16-25 |
| E2 | system | M2 | Tin có 1.001 từ. | E2.1 | FR-M16-05.12, BR-M16-08, BR-M16-09, BR-M16-25 |
| E3 | system | M2 | Actor gửi ảnh hoặc tệp đính kèm. | E3.1 | FR-M16-05.04, BR-M16-08, BR-M16-09, BR-M16-25 |
| E4 | system | M2 | Đã có 30 tin của A trong cùng C-AB sau t−60 giây. | E4.1 | FR-M16-05.05, BR-M16-09, BR-M16-08, BR-M16-25 |
| E5 | system | M2 | B trong cuộc 1-1 cũ đã DELETED. | E5.1 | FR-M16-05.13, BR-M16-08, BR-M16-09, BR-M16-25 |
| E6 | system | M2 | B trong 1-1 cũ BANNED hoặc DEACTIVATED, A vẫn hợp lệ. | E6.1 | FR-M16-05.01, FR-M16-05.02, FR-M16-05.03, FR-M16-05.14, FR-M16-07.11, BR-M16-25 |
| E7 | system | M2 | Tin ở đúng ranh giới 1.000 từ và đúng 60 giây sau tin sớm nhất trong 30 tin. | E7.1 | FR-M16-05.01, FR-M16-05.02, FR-M16-05.03, FR-M16-05.05, FR-M16-05.12, FR-M16-07.11, BR-M16-08, BR-M16-09 |
| E8 | system | M2 | A gửi vào nhóm mình đang thuộc, một thành viên khác BANNED, DEACTIVATED hoặc DELETED. | E8.1 | FR-M16-05.01, FR-M16-05.02, FR-M16-05.03, FR-M16-05.06, FR-M16-07.11, BR-M16-25 |
| E9 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E9.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E10 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E10.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E11 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E11.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E12 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E12.1 | FR-M16-05.01, FR-M16-05.02, FR-M16-05.03, FR-M16-05.04, FR-M16-05.05, FR-M16-05.06, FR-M16-05.07, FR-M16-05.08, FR-M16-05.09, FR-M16-05.10, FR-M16-05.11, FR-M16-05.12, FR-M16-05.13, FR-M16-05.14, FR-M16-01.02, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-08, BR-M16-09, BR-M16-10, BR-M16-18, BR-M16-20, BR-M16-21, BR-M16-25, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| E13 | system | M1 | ACT-002 — Người dùng ngoài cuộc, chưa từng là thành viên nhóm. | E13.1 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| E14 | system | M1 | ACT-014 — Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current. | E14.1 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |
| E15 | system | M1 | ACT-008 — Staff ACTIVE ngoài cuộc, cờ Bật hoặc ADMIN khi cờ Tắt. | E15.1 | FR-M16-04.08, FR-M16-05.06, FR-M16-15.04 |
| E16 | system | M1 | ACT-007 — Staff ACTIVE ngoài cuộc, cờ Bật hoặc ADMIN khi cờ Tắt. | E16.1 | FR-M16-04.08, FR-M16-05.06, FR-M16-15.04 |


<!-- sc:branch SC-M16-004 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Kiểm yêu cầu và từ chối gửi theo điều kiện, trả kết quả không nhận tin này. | Nội dung ba dấu cách, không có #46 mới. | END:REJECTED | FR-M16-05.11, BR-M16-08, BR-M16-09, BR-M16-25 |


<!-- sc:branch SC-M16-004 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Kiểm yêu cầu và từ chối gửi theo điều kiện, trả kết quả không nhận tin này. | Dữ liệu gồm 1.001 chuỗi ngăn cách bằng khoảng trắng, không có tin mới. | END:REJECTED | FR-M16-05.12, BR-M16-08, BR-M16-09, BR-M16-25 |


<!-- sc:branch SC-M16-004 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Kiểm yêu cầu và từ chối gửi theo điều kiện, trả kết quả không nhận tin này. | Một tệp minh họa bài-tập.pdf hoặc một ảnh, không ghi tin này. | END:REJECTED | FR-M16-05.04, BR-M16-08, BR-M16-09, BR-M16-25 |


<!-- sc:branch SC-M16-004 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Kiểm yêu cầu và từ chối gửi theo điều kiện, trả kết quả không nhận tin này. | D4-rate t=10:00:59, 30 tin từ 10:00:00 đến 10:00:40, tin thứ 31 bị từ chối và báo gửi quá nhanh. | END:REJECTED | FR-M16-05.05, BR-M16-09, BR-M16-08, BR-M16-25 |


<!-- sc:branch SC-M16-004 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Kiểm yêu cầu và từ chối gửi theo điều kiện, trả kết quả không nhận tin này. | C-AB giữ lịch sử nhưng không có tin #46 gửi mới đến B. | END:REJECTED | FR-M16-05.13, BR-M16-08, BR-M16-09, BR-M16-25 |


<!-- sc:branch SC-M16-004 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Nhận văn bản như đường chuẩn, ghi người gửi/thời điểm, cập nhật mốc sender và sự kiện M07. B được đọc khi hoạt động lại, không yêu cầu B chấp nhận. | D4-state C-AB có sẵn, tin #46 được giữ để B đọc khi trở lại. | END:SUCCESS | FR-M16-05.01, FR-M16-05.02, FR-M16-05.03, FR-M16-05.14, FR-M16-07.11, BR-M16-25 |


<!-- sc:branch SC-M16-004 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Loại tin 10:00:00 khỏi cửa sổ tại t=10:01:00. Còn 29 lượt của A trong C-AB, nhận tin 1.000 từ, ghi #46, cập nhật mốc người gửi và giao tin/sự kiện M07. | D4-boundary 30 lượt trước đó, 1 lượt đúng t−60 giây nên chỉ đếm 29, sau nhận có 30. Cuộc C-AC có cửa sổ riêng. | END:SUCCESS | FR-M16-05.01, FR-M16-05.02, FR-M16-05.03, FR-M16-05.05, FR-M16-05.12, FR-M16-07.11, BR-M16-08, BR-M16-09 |


<!-- sc:branch SC-M16-004 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm nội dung và cửa sổ gửi của A trong nhóm, nhận tin hợp lệ, ghi mốc sender, cung cấp sự kiện M07 và giao tới view thành viên được phép. Các tài khoản không ACTIVE vẫn giữ tư cách và tính vào số thành viên. | D4-group A ACTIVE current, nhóm có B DELETED vẫn là thành viên, tin #46 do A được nhận. Không áp điều kiện đích 1-1 DELETED lên toàn nhóm. | END:SUCCESS | FR-M16-05.01, FR-M16-05.02, FR-M16-05.03, FR-M16-05.06, FR-M16-07.11, BR-M16-25 |


<!-- sc:branch SC-M16-004 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-004 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E11 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-004 E11 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E11.1 | ACT-001 | Nhập và gửi tin văn bản “Mai ôn thi nhé 😀” vào C-AB. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E11.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E11.2 | SYSTEM | Từ chối yêu cầu Chat của Guest, trả kết quả không được thực hiện chức năng này. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E12 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-004 E12 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E12.1 | ACT-007 | Nhập và gửi tin văn bản “Mai ôn thi nhé 😀” vào C-AB. | D4 A current C-AB, B ACTIVE, t=10:01:00 UTC+7, trước gửi có 29 tin A trong (10:00:00, 10:01:00], mốc A=#45. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E12.2 | FR-M16-05.01, FR-M16-05.02, FR-M16-05.03, FR-M16-05.04, FR-M16-05.05, FR-M16-05.06, FR-M16-05.07, FR-M16-05.08, FR-M16-05.09, FR-M16-05.10, FR-M16-05.11, FR-M16-05.12, FR-M16-05.13, FR-M16-05.14, FR-M16-01.02, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-08, BR-M16-09, BR-M16-10, BR-M16-18, BR-M16-20, BR-M16-21, BR-M16-25, FR-M16-15.04, FR-M10-12.08 |
| E12.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm current membership, văn bản/emoji không rỗng/chỉ trắng, tối đa 1.000 từ ngăn cách bằng khoảng trắng, không ảnh/tệp. Đếm riêng (A, C-AB) các tin có thời điểm lớn hơn t−60 giây. Trong 1-1 kiểm B chưa DELETED. Ghi tin #46 với A và thời điểm hệ thống nhận. Ghi một mốc mỗi người mỗi cuộc bằng tin mới hơn giữa mốc hiện tại và ứng viên qua UC-M16-006. UC-M16-007 suy Đã xem khi có thành viên khác người gửi đọc tới tin cuối, còn lại Đã gửi. Chỉ tin cuối có trạng thái, avatar loại người gửi và chính người xem, gộp nhiều người, loại người chưa đọc tới. Cập nhật receipt ngay cho các view hợp lệ và cung cấp mốc/tin chưa đọc được thấy cho M07. Ứng viên của người gửi là #46 theo sự kiện gửi. AUT-M16-002 giao ngay tới thành viên hợp lệ đang mở, cung cấp M07 sự kiện tin mới/thành viên/mốc/cuộc đang mở để thông báo trong ứng dụng. Tin giữ vĩnh viễn, không sửa, không quét AI, không báo cáo/Block ở MS1. Tin đầu 1-1 giao không đợi chấp nhận. | Tin #46 nhận 10:01:00, mốc A=#46, B chưa đọc nên Đã gửi, nội dung đến view hợp lệ và sự kiện M07 được cung cấp. Không email, chuông hoặc thông báo được mời. | END:SUCCESS | FR-M16-05.01, FR-M16-05.02, FR-M16-05.03, FR-M16-05.04, FR-M16-05.05, FR-M16-05.06, FR-M16-05.07, FR-M16-05.08, FR-M16-05.09, FR-M16-05.10, FR-M16-05.11, FR-M16-05.12, FR-M16-05.13, FR-M16-05.14, FR-M16-01.02, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-08, BR-M16-09, BR-M16-10, BR-M16-18, BR-M16-20, BR-M16-21, BR-M16-25, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E13 — thay toàn bộ M1 đến kết thúc.** Người dùng ngoài cuộc, chưa từng là thành viên nhóm.

<!-- sc:branch SC-M16-004 E13 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E13.1 | ACT-002 | Nhập và gửi tin văn bản “Mai ôn thi nhé 😀” vào C-AB. | Cờ Bật, phiên hợp lệ nhưng thiếu vai trò thành viên hiện tại. | E13.2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06 |
| E13.2 | SYSTEM | UC-M16-018 kiểm tư cách đúng cuộc/nhóm và từ chối yêu cầu vì thiếu quyền thành viên hiện tại. | Không đọc dữ liệu hoặc thay đổi trạng thái bằng yêu cầu trái quyền. | END:REJECTED | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |


**E14 — thay toàn bộ M1 đến kết thúc.** Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current.

<!-- sc:branch SC-M16-004 E14 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E14.1 | ACT-014 | Nhập và gửi tin văn bản “Mai ôn thi nhé 😀” vào C-AB. | Có cutoff rời, chưa gia nhập lại, cờ Bật. | E14.2 | FR-M16-04.10, BR-M16-27 |
| E14.2 | SYSTEM | Từ chối thao tác cần current membership. Cựu chỉ đọc lịch sử trước cutoff theo SC-M16-003/E13, vào lại qua SC-M16-007 hoặc SC-M16-009. | Nhóm/hộp thư/lịch sử trước cutoff của cựu được giữ, không có thay đổi từ thao tác trái quyền. | END:REJECTED | FR-M16-04.10, FR-M16-05.06, BR-M16-05, BR-M16-27, BR-M16-28 |


**E15 — thay toàn bộ M1 đến kết thúc.** Staff ACTIVE ngoài cuộc, cờ Bật hoặc ADMIN khi cờ Tắt.

<!-- sc:branch SC-M16-004 E15 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E15.1 | ACT-008 | Nhập và gửi tin văn bản “Mai ôn thi nhé 😀” vào C-AB. | Staff không là current hoặc former của cuộc được chọn. | E15.2 | FR-M16-04.08, FR-M16-05.06 |
| E15.2 | SYSTEM | Kiểm tư cách và từ chối truy cập cuộc của người khác, kể cả ADMIN đã qua cổng cờ. | Không trả lịch sử hoặc ghi tin gửi trái quyền. | END:REJECTED | FR-M16-04.08, FR-M16-05.06, FR-M16-15.04 |


**E16 — thay toàn bộ M1 đến kết thúc.** Staff ACTIVE ngoài cuộc, cờ Bật hoặc ADMIN khi cờ Tắt.

<!-- sc:branch SC-M16-004 E16 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E16.1 | ACT-007 | Nhập và gửi tin văn bản “Mai ôn thi nhé 😀” vào C-AB. | Staff không là current hoặc former của cuộc được chọn. | E16.2 | FR-M16-04.08, FR-M16-05.06 |
| E16.2 | SYSTEM | Kiểm tư cách và từ chối truy cập cuộc của người khác, kể cả ADMIN đã qua cổng cờ. | Không trả lịch sử hoặc ghi tin gửi trái quyền. | END:REJECTED | FR-M16-04.08, FR-M16-05.06, FR-M16-15.04 |


<!-- sc:end SC-M16-004 -->

<a id="sc-m16-005"></a>

<!-- sc:scenario SC-M16-005 -->

### SC-M16-005

#### 1. Tên kịch bản chuẩn

Thu hồi tin nhắn của mình — BF-M16-005. UC owner [UC-M16-005](../../us/US-M16.md#uc-m16-005).

#### 2. Actor thực hiện

ACT-012 — Thành viên cuộc trò chuyện khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Có định danh tin, sender và cuộc. Quyền, hạn và trạng thái thu hồi đều kiểm trong luồng. D5 là dữ liệu độc lập với D4. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-005 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. #50 gắn đã thu hồi, gốc được giữ và che với mọi actor kể cả staff. Tin cuối là placeholder #50, Đã xem do B đã đọc, vị trí/thời điểm tin giữ nguyên. #50 thu hồi thành công ở ranh giới đúng 5 phút. Tin #49 gửi 20:00:00, thu hồi 20:04:59, #50 gửi 20:01:00. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-005 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-012 | Chọn thu hồi tin #50 trong G50. | D5 #50 gửi 20:00:00, yêu cầu nhận 20:04:59, A là sender/current. Tin cuối #50, B đã đọc #50. | M2 | FR-M16-06.01, FR-M16-06.02, FR-M16-06.03, FR-M16-06.04, FR-M16-06.05, FR-M16-06.06, FR-M16-06.07, FR-M16-06.08, FR-M16-06.09, FR-M16-05.08, BR-M16-11, BR-M16-12, BR-M16-15, BR-M16-18 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm current, đúng sender A, chưa thu hồi và thời gian trôi không quá 300 giây. Gắn cờ thu hồi, giữ gốc lâu dài. Trả placeholder Tin nhắn đã bị thu hồi ở vị trí #50 cho mọi phía, AUT-M16-002 cập nhật tức thời cho view hợp lệ. Tin cuối vẫn #50, giữ cơ chế receipt UC-M16-007 theo mốc, chỉ một kiểu thu hồi toàn cuộc. | #50 gắn đã thu hồi, gốc được giữ và che với mọi actor kể cả staff. Tin cuối là placeholder #50, Đã xem do B đã đọc, vị trí/thời điểm tin giữ nguyên. | END:SUCCESS | FR-M16-06.01, FR-M16-06.02, FR-M16-06.03, FR-M16-06.04, FR-M16-06.05, FR-M16-06.06, FR-M16-06.07, FR-M16-06.08, FR-M16-06.09, FR-M16-05.08, BR-M16-11, BR-M16-12, BR-M16-15, BR-M16-18, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-005 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Yêu cầu ở đúng 20:05:00, tin gửi 20:00:00. | E1.1 | FR-M16-06.01, FR-M16-06.02, FR-M16-06.07, FR-M16-06.08, FR-M16-06.09, BR-M16-11, BR-M16-12 |
| E2 | system | M2 | Yêu cầu ở 20:05:01 hoặc cờ vừa bật lại sau khi hạn đã hết. | E2.1 | FR-M16-06.03, FR-M16-15.05, FR-M16-15.08, BR-M16-11, BR-M16-23 |
| E3 | system | M2 | A chọn tin của B, gồm khi A là Admin nhóm chat. | E3.1 | FR-M16-06.04, BR-M16-11 |
| E4 | system | M2 | #50 đã thu hồi trước yêu cầu. | E4.1 | FR-M16-06.06 |
| E5 | user-choice | M1 | A thu hồi #49 chưa phải tin mới nhất, vẫn còn hạn. | E5.1 | FR-M16-06.01, BR-M16-11, FR-M16-06.02, FR-M16-06.07, FR-M16-06.08, FR-M16-07.08, BR-M16-12, BR-M16-15 |
| E6 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E6.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E7 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E7.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E8 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E8.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E9 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E9.1 | FR-M16-06.01, FR-M16-06.02, FR-M16-06.03, FR-M16-06.04, FR-M16-06.05, FR-M16-06.06, FR-M16-06.07, FR-M16-06.08, FR-M16-06.09, FR-M16-05.08, BR-M16-11, BR-M16-12, BR-M16-15, BR-M16-18, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| E10 | system | M1 | ACT-002 — Người dùng ngoài cuộc, chưa từng là thành viên nhóm. | E10.1 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| E11 | system | M1 | ACT-014 — Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current. | E11.1 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |


<!-- sc:branch SC-M16-005 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Thu hồi ở đúng 300 giây, gắn cờ, che gốc và trả placeholder cho mọi phía ngay, giữ tin cuối/receipt. | #50 thu hồi thành công ở ranh giới đúng 5 phút. | END:SUCCESS | FR-M16-06.01, FR-M16-06.02, FR-M16-06.07, FR-M16-06.08, FR-M16-06.09, BR-M16-11, BR-M16-12 |


<!-- sc:branch SC-M16-005 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Từ chối thu hồi vì đã quá 300 giây, không gia hạn vì thời gian Chat tắt. | #50 giữ nội dung/trạng thái trước yêu cầu, trôi 301 giây. | END:REJECTED | FR-M16-06.03, FR-M16-15.05, FR-M16-15.08, BR-M16-11, BR-M16-23 |


<!-- sc:branch SC-M16-005 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Từ chối thu hồi do không phải người gửi. | #50 sender B, caller A, nội dung và cờ thu hồi giữ nguyên. | END:REJECTED | FR-M16-06.04, BR-M16-11 |


<!-- sc:branch SC-M16-005 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Từ chối thu hồi lần nữa, trả kết quả cho yêu cầu lặp. | #50 vẫn là placeholder, gốc được giữ. | END:REJECTED | FR-M16-06.06 |


<!-- sc:branch SC-M16-005 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-012 | Chọn thu hồi tin #49 của mình thay vì tin mới nhất #50. | D5-old tin 49 gửi20:00:00, tin 50 gửi20:01:00, actor chọn 49 lúc 20:04:59. | E5.2 | FR-M16-06.01, BR-M16-11 |
| E5.2 | SYSTEM | Gắn cờ #49, cập nhật placeholder tại #49 cho mọi phía, tin cuối vẫn #50 và chỉ #50 có trạng thái đọc. | Tin #49 gửi 20:00:00, thu hồi 20:04:59, #50 gửi 20:01:00. | END:SUCCESS | FR-M16-06.01, FR-M16-06.02, FR-M16-06.07, FR-M16-06.08, FR-M16-07.08, BR-M16-12, BR-M16-15 |


<!-- sc:branch SC-M16-005 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-005 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E8 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-005 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-001 | Chọn thu hồi tin #50 trong G50. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E8.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E8.2 | SYSTEM | Từ chối yêu cầu Chat của Guest, trả kết quả không được thực hiện chức năng này. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E9 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-005 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-007 | Chọn thu hồi tin #50 trong G50. | D5 #50 gửi 20:00:00, yêu cầu nhận 20:04:59, A là sender/current. Tin cuối #50, B đã đọc #50. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E9.2 | FR-M16-06.01, FR-M16-06.02, FR-M16-06.03, FR-M16-06.04, FR-M16-06.05, FR-M16-06.06, FR-M16-06.07, FR-M16-06.08, FR-M16-06.09, FR-M16-05.08, BR-M16-11, BR-M16-12, BR-M16-15, BR-M16-18, FR-M16-15.04, FR-M10-12.08 |
| E9.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm current, đúng sender A, chưa thu hồi và thời gian trôi không quá 300 giây. Gắn cờ thu hồi, giữ gốc lâu dài. Trả placeholder Tin nhắn đã bị thu hồi ở vị trí #50 cho mọi phía, AUT-M16-002 cập nhật tức thời cho view hợp lệ. Tin cuối vẫn #50, giữ cơ chế receipt UC-M16-007 theo mốc, chỉ một kiểu thu hồi toàn cuộc. | #50 gắn đã thu hồi, gốc được giữ và che với mọi actor kể cả staff. Tin cuối là placeholder #50, Đã xem do B đã đọc, vị trí/thời điểm tin giữ nguyên. | END:SUCCESS | FR-M16-06.01, FR-M16-06.02, FR-M16-06.03, FR-M16-06.04, FR-M16-06.05, FR-M16-06.06, FR-M16-06.07, FR-M16-06.08, FR-M16-06.09, FR-M16-05.08, BR-M16-11, BR-M16-12, BR-M16-15, BR-M16-18, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E10 — thay toàn bộ M1 đến kết thúc.** Người dùng ngoài cuộc, chưa từng là thành viên nhóm.

<!-- sc:branch SC-M16-005 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-002 | Chọn thu hồi tin #50 trong G50. | Cờ Bật, phiên hợp lệ nhưng thiếu vai trò thành viên hiện tại. | E10.2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06 |
| E10.2 | SYSTEM | UC-M16-018 kiểm tư cách đúng cuộc/nhóm và từ chối yêu cầu vì thiếu quyền thành viên hiện tại. | Không đọc dữ liệu hoặc thay đổi trạng thái bằng yêu cầu trái quyền. | END:REJECTED | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |


**E11 — thay toàn bộ M1 đến kết thúc.** Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current.

<!-- sc:branch SC-M16-005 E11 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E11.1 | ACT-014 | Chọn thu hồi tin #50 trong G50. | Có cutoff rời, chưa gia nhập lại, cờ Bật. | E11.2 | FR-M16-04.10, BR-M16-27 |
| E11.2 | SYSTEM | Từ chối thao tác cần current membership. Cựu chỉ đọc lịch sử trước cutoff theo SC-M16-003/E13, vào lại qua SC-M16-007 hoặc SC-M16-009. | Nhóm/hộp thư/lịch sử trước cutoff của cựu được giữ, không có thay đổi từ thao tác trái quyền. | END:REJECTED | FR-M16-04.10, FR-M16-05.06, BR-M16-05, BR-M16-27, BR-M16-28 |


<!-- sc:end SC-M16-005 -->

<a id="sc-m16-006"></a>

<!-- sc:scenario SC-M16-006 -->

### SC-M16-006

#### 1. Tên kịch bản chuẩn

Tạo nhóm chat — BF-M16-006. UC owner [UC-M16-008](../../us/US-M16.md#uc-m16-008).

#### 2. Actor thực hiện

ACT-002 — Người dùng đã đăng nhập khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Có người tạo, tên và tập người được chọn, mọi điều kiện được kiểm trong luồng. D6 độc lập các nhóm đã có ở bộ khác. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-006 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. G-ABC có tên Ôn thi Lý, A Admin nhóm chat, B/C Member, tổng 3, công tắc Tắt. Thành viên dùng luồng đọc/gửi riêng khi chủ động yêu cầu. D6-max tên lặp a 100 lần, tập A và 99 tài khoản khác nhau. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-006 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Nhập tên và chọn thành viên rồi yêu cầu tạo nhóm chat. | D6 tên “  Ôn thi Lý  ”, A người tạo, chọn B, C ACTIVE, tổng 3, tên có thể trùng nhóm khác. | M2 | FR-M16-02.01, FR-M16-02.02, FR-M16-02.03, FR-M16-02.04, FR-M16-02.05, FR-M16-02.06, FR-M16-02.07, FR-M16-02.08, FR-M16-02.09, BR-M16-01, BR-M16-03, BR-M16-04, BR-M16-06, BR-M16-25, BR-M16-32, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Trim tên thành Ôn thi Lý, kiểm 1–100 ký tự và tổng 3–100 người khác nhau gồm người tạo. Các đích ACTIVE. Tạo G-ABC độc lập Group, đặt A Admin nhóm chat đầu tiên, công tắc Tắt. UC-M16-019 kiểm người đích chưa là thành viên, đủ điều kiện tài khoản và số thành viên thực tế trước khi vào, gồm cả tài khoản không ACTIVE đang còn tư cách. Ghi Member, người mới/vào lại đọc được toàn lịch sử, không áp cutoff cũ. Người chờ chưa chiếm chỗ. Khi vào lại cung cấp M07 thay đổi tư cách để bắt đầu Đang nhận riêng nhóm, giữ cài đặt tắt toàn Chat. Kết nạp B, C ngay, không đòi follow/cùng Group, không gửi thông báo được mời. Trả nhóm đã tạo. | G-ABC có tên Ôn thi Lý, A Admin nhóm chat, B/C Member, tổng 3, công tắc Tắt. Thành viên dùng luồng đọc/gửi riêng khi chủ động yêu cầu. | END:SUCCESS | FR-M16-02.01, FR-M16-02.02, FR-M16-02.03, FR-M16-02.04, FR-M16-02.05, FR-M16-02.06, FR-M16-02.07, FR-M16-02.08, FR-M16-02.09, BR-M16-01, BR-M16-03, BR-M16-04, BR-M16-06, BR-M16-25, BR-M16-32, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-006 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Sau trim tên rỗng hoặc dài 101 ký tự. | E1.1 | FR-M16-02.07, BR-M16-03, BR-M16-32 |
| E2 | system | M2 | Tổng số người khác nhau gồm A chỉ có 2. | E2.1 | FR-M16-02.04, BR-M16-03, BR-M16-32 |
| E3 | system | M2 | Tổng số người khác nhau gồm A là 101. | E3.1 | FR-M16-02.05, BR-M16-03, BR-M16-32 |
| E4 | system | M2 | Một người được chọn BANNED, DEACTIVATED hoặc DELETED. | E4.1 | FR-M16-02.09, BR-M16-25 |
| E5 | system | M2 | Tên đúng 100 ký tự và tổng đúng 100 người, tất cả đích ACTIVE. | E5.1 | FR-M16-02.01, FR-M16-02.02, FR-M16-02.05, FR-M16-02.07, FR-M16-02.08, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, BR-M16-32 |
| E6 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E6.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E7 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E7.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E8 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E8.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E9 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E9.1 | FR-M16-02.01, FR-M16-02.02, FR-M16-02.03, FR-M16-02.04, FR-M16-02.05, FR-M16-02.06, FR-M16-02.07, FR-M16-02.08, FR-M16-02.09, BR-M16-01, BR-M16-03, BR-M16-04, BR-M16-06, BR-M16-25, BR-M16-32, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |


<!-- sc:branch SC-M16-006 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Kiểm dữ liệu và từ chối tạo nhóm không hợp lệ. | Tên ba khoảng trắng hoặc lặp ký tự a 101 lần, yêu cầu tên bị từ chối. | END:REJECTED | FR-M16-02.07, BR-M16-03, BR-M16-32 |


<!-- sc:branch SC-M16-006 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Kiểm dữ liệu và từ chối tạo nhóm không hợp lệ. | A và B, yêu cầu tạo nhóm bị từ chối. | END:REJECTED | FR-M16-02.04, BR-M16-03, BR-M16-32 |


<!-- sc:branch SC-M16-006 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Kiểm dữ liệu và từ chối tạo nhóm không hợp lệ. | A cùng 100 người khác, yêu cầu tạo nhóm bị từ chối. | END:REJECTED | FR-M16-02.05, BR-M16-03, BR-M16-32 |


<!-- sc:branch SC-M16-006 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Từ chối đưa người không hợp lệ vào nhóm. Kết quả của cả thao tác chọn nhiều người, rollback hoặc tạo một phần chưa được nguồn chốt, ghi GAP-SC-M16-001. | D6-bad chọn B ACTIVE và X DEACTIVATED, X không được kết nạp. Không khẳng định trạng thái tổng thể nhóm sau lỗi một phần. | END:REJECTED | FR-M16-02.09, BR-M16-25 |


<!-- sc:branch SC-M16-006 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Chấp nhận ranh giới hợp lệ, tạo nhóm, A Admin, 99 người kia Member, công tắc Tắt, trả nhóm tổng 100. | D6-max tên lặp a 100 lần, tập A và 99 tài khoản khác nhau. | END:SUCCESS | FR-M16-02.01, FR-M16-02.02, FR-M16-02.05, FR-M16-02.07, FR-M16-02.08, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, BR-M16-32 |


<!-- sc:branch SC-M16-006 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-006 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E8 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-006 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-001 | Nhập tên và chọn thành viên rồi yêu cầu tạo nhóm chat. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E8.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E8.2 | SYSTEM | Từ chối yêu cầu Chat của Guest, trả kết quả không được thực hiện chức năng này. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E9 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-006 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-007 | Nhập tên và chọn thành viên rồi yêu cầu tạo nhóm chat. | D6 tên “  Ôn thi Lý  ”, A người tạo, chọn B, C ACTIVE, tổng 3, tên có thể trùng nhóm khác. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E9.2 | FR-M16-02.01, FR-M16-02.02, FR-M16-02.03, FR-M16-02.04, FR-M16-02.05, FR-M16-02.06, FR-M16-02.07, FR-M16-02.08, FR-M16-02.09, BR-M16-01, BR-M16-03, BR-M16-04, BR-M16-06, BR-M16-25, BR-M16-32, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-15.04, FR-M10-12.08 |
| E9.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Trim tên thành Ôn thi Lý, kiểm 1–100 ký tự và tổng 3–100 người khác nhau gồm người tạo. Các đích ACTIVE. Tạo G-ABC độc lập Group, đặt A Admin nhóm chat đầu tiên, công tắc Tắt. UC-M16-019 kiểm người đích chưa là thành viên, đủ điều kiện tài khoản và số thành viên thực tế trước khi vào, gồm cả tài khoản không ACTIVE đang còn tư cách. Ghi Member, người mới/vào lại đọc được toàn lịch sử, không áp cutoff cũ. Người chờ chưa chiếm chỗ. Khi vào lại cung cấp M07 thay đổi tư cách để bắt đầu Đang nhận riêng nhóm, giữ cài đặt tắt toàn Chat. Kết nạp B, C ngay, không đòi follow/cùng Group, không gửi thông báo được mời. Trả nhóm đã tạo. | G-ABC có tên Ôn thi Lý, A Admin nhóm chat, B/C Member, tổng 3, công tắc Tắt. Thành viên dùng luồng đọc/gửi riêng khi chủ động yêu cầu. | END:SUCCESS | FR-M16-02.01, FR-M16-02.02, FR-M16-02.03, FR-M16-02.04, FR-M16-02.05, FR-M16-02.06, FR-M16-02.07, FR-M16-02.08, FR-M16-02.09, BR-M16-01, BR-M16-03, BR-M16-04, BR-M16-06, BR-M16-25, BR-M16-32, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


<!-- sc:end SC-M16-006 -->

<a id="sc-m16-007"></a>

<!-- sc:scenario SC-M16-007 -->

### SC-M16-007

#### 1. Tên kịch bản chuẩn

Thêm hoặc đề nghị thêm thành viên — BF-M16-007. UC owner [UC-M16-009](../../us/US-M16.md#uc-m16-009).

#### 2. Actor thực hiện

ACT-012 — Thành viên cuộc trò chuyện khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Có nhóm/người thêm/người được thêm và công tắc. Kiểm các quyền/trạng thái trong luồng. Mục tiêu gồm yêu cầu thêm hoặc gửi đề nghị theo công tắc, kết quả Chờ duyệt chưa đồng nghĩa đã vào. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-007 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. D thành Member ngay, tổng 3→4, có quyền đọc toàn lịch sử. D7-pending tổng 3 giữ3, P-D mới Chờ duyệt, không thông báo được mời. D7-rejoin D có cutoff cũ21:00, sau vào đọc được cả lịch sử trước và sau cutoff. Mốc vào lại giữ GAP-SC-M16-005. Tổng3→4, D Member, công tắc vẫn Bật. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-007 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-012 | Chọn thêm Dũng vào nhóm G-ABC. | D7 G-ABC có A Admin, B/C Member tổng 3, caller B, D ACTIVE chưa tham gia, công tắc Tắt. | M2 | FR-M16-08.01, FR-M16-08.04, FR-M16-08.05, FR-M16-08.06, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, BR-M16-01, BR-M16-03, BR-M16-06, BR-M16-25, BR-M16-28, FR-M16-02.02, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-27, BR-M16-29, FR-M07-09.08, BR-M07-08 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm tư cách current trong chính nhóm và người đích chưa là thành viên, không BANNED/DEACTIVATED/DELETED. Công tắc đang Tắt, người thêm là Member. UC-M16-019 kiểm người đích chưa là thành viên, đủ điều kiện tài khoản và số thành viên thực tế trước khi vào, gồm cả tài khoản không ACTIVE đang còn tư cách. Ghi Member, người mới/vào lại đọc được toàn lịch sử, không áp cutoff cũ. Người chờ chưa chiếm chỗ. Khi vào lại cung cấp M07 thay đổi tư cách để bắt đầu Đang nhận riêng nhóm, giữ cài đặt tắt toàn Chat. Đưa D vào ngay và trả kết quả, không yêu cầu follow/cùng Group và không phát thông báo được mời. | D thành Member ngay, tổng 3→4, có quyền đọc toàn lịch sử. | END:SUCCESS | FR-M16-08.01, FR-M16-08.04, FR-M16-08.05, FR-M16-08.06, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, BR-M16-01, BR-M16-03, BR-M16-06, BR-M16-25, BR-M16-28, FR-M16-02.02, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-27, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-007 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Member B thêm D khi duyệt Bật, còn chỗ và dữ liệu người chờ không giao nhau. | E1.1 | FR-M16-08.03, FR-M16-08.13, FR-M16-10.07, BR-M16-06 |
| E2 | system | M2 | D đã là thành viên. | E2.1 | FR-M16-08.07 |
| E3 | system | M2 | D BANNED, DEACTIVATED hoặc DELETED. | E3.1 | FR-M16-08.09, BR-M16-25 |
| E4 | system | M2 | Nhánh thêm vào ngay nhưng nhóm đã100. | E4.1 | FR-M16-08.05, BR-M16-03 |
| E5 | system | M2 | D là cựu đã rời hoặc bị xóa, công tắc Tắt. | E5.1 | FR-M16-08.08, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08 |
| E6 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E6.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E7 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E7.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E8 | system | M1 | ACT-013 — A Admin nhóm chat thêm D khi duyệt Bật, tổng 3, D ACTIVE chưa tham gia. | E8.1 | FR-M16-08.02, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E9 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E9.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E10 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E10.1 | FR-M16-08.01, FR-M16-08.04, FR-M16-08.05, FR-M16-08.06, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, BR-M16-01, BR-M16-03, BR-M16-06, BR-M16-25, BR-M16-28, FR-M16-02.02, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-27, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| E11 | system | M1 | ACT-002 — Người dùng ngoài cuộc, chưa từng là thành viên nhóm. | E11.1 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| E12 | system | M1 | ACT-014 — Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current. | E12.1 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |


<!-- sc:branch SC-M16-007 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Kiểm dữ liệu rồi ghi đề nghị P-D Chờ duyệt, B là người đề nghị. Trả kết quả đang chờ, chưa kết nạp D, chưa cấp quyền đọc và chưa chiếm chỗ100. Admin xử lý ở SC-M16-010 hoặc tắt duyệt ở SC-M16-011. | D7-pending tổng 3 giữ3, P-D mới Chờ duyệt, không thông báo được mời. | END:SUCCESS | FR-M16-08.03, FR-M16-08.13, FR-M16-10.07, BR-M16-06 |


<!-- sc:branch SC-M16-007 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Không thêm D lần nữa, trả kết quả không có kết nạp mới. | Tổng và tư cách D giữ nguyên, không thành viên trùng. | END:REJECTED | FR-M16-08.07 |


<!-- sc:branch SC-M16-007 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Từ chối thêm tài khoản đích ở trạng thái đó. | D7-bad tổng 3 giữ3, không đưa D vào. | END:REJECTED | FR-M16-08.09, BR-M16-25 |


<!-- sc:branch SC-M16-007 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Kiểm admission và từ chối thêm, không vượt hạn. | D7-full tổng 100 giữ100, người mới chưa được vào. | END:REJECTED | FR-M16-08.05, BR-M16-03 |


<!-- sc:branch SC-M16-007 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | UC-M16-019 kiểm người đích chưa là thành viên, đủ điều kiện tài khoản và số thành viên thực tế trước khi vào, gồm cả tài khoản không ACTIVE đang còn tư cách. Ghi Member, người mới/vào lại đọc được toàn lịch sử, không áp cutoff cũ. Người chờ chưa chiếm chỗ. Khi vào lại cung cấp M07 thay đổi tư cách để bắt đầu Đang nhận riêng nhóm, giữ cài đặt tắt toàn Chat. Kết nạp lại như người mới theo công tắc hiện tại, trả tư cách Member. | D7-rejoin D có cutoff cũ21:00, sau vào đọc được cả lịch sử trước và sau cutoff. Mốc vào lại giữ GAP-SC-M16-005. | END:SUCCESS | FR-M16-08.08, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08 |


<!-- sc:branch SC-M16-007 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-007 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E8 — thay toàn bộ M1 đến kết thúc.** A Admin nhóm chat thêm D khi duyệt Bật, tổng 3, D ACTIVE chưa tham gia.

<!-- sc:branch SC-M16-007 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-013 | Chọn thêm D vào G-ABC. | D7-admin, A là Admin đúng nhóm, công tắc Bật. | E8.2 | FR-M16-08.02 |
| E8.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. UC-M16-019 kiểm người đích chưa là thành viên, đủ điều kiện tài khoản và số thành viên thực tế trước khi vào, gồm cả tài khoản không ACTIVE đang còn tư cách. Ghi Member, người mới/vào lại đọc được toàn lịch sử, không áp cutoff cũ. Người chờ chưa chiếm chỗ. Khi vào lại cung cấp M07 thay đổi tư cách để bắt đầu Đang nhận riêng nhóm, giữ cài đặt tắt toàn Chat. Đưa D vào ngay và trả kết quả. Không tạo đề nghị Chờ duyệt. | Tổng3→4, D Member, công tắc vẫn Bật. | END:SUCCESS | FR-M16-08.02, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E9 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-007 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-001 | Chọn thêm Dũng vào nhóm G-ABC. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E9.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E9.2 | SYSTEM | Từ chối yêu cầu Chat của Guest, trả kết quả không được thực hiện chức năng này. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E10 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-007 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-007 | Chọn thêm Dũng vào nhóm G-ABC. | D7 G-ABC có A Admin, B/C Member tổng 3, caller B, D ACTIVE chưa tham gia, công tắc Tắt. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E10.2 | FR-M16-08.01, FR-M16-08.04, FR-M16-08.05, FR-M16-08.06, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, BR-M16-01, BR-M16-03, BR-M16-06, BR-M16-25, BR-M16-28, FR-M16-02.02, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-27, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-15.04, FR-M10-12.08 |
| E10.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm tư cách current trong chính nhóm và người đích chưa là thành viên, không BANNED/DEACTIVATED/DELETED. Công tắc đang Tắt, người thêm là Member. UC-M16-019 kiểm người đích chưa là thành viên, đủ điều kiện tài khoản và số thành viên thực tế trước khi vào, gồm cả tài khoản không ACTIVE đang còn tư cách. Ghi Member, người mới/vào lại đọc được toàn lịch sử, không áp cutoff cũ. Người chờ chưa chiếm chỗ. Khi vào lại cung cấp M07 thay đổi tư cách để bắt đầu Đang nhận riêng nhóm, giữ cài đặt tắt toàn Chat. Đưa D vào ngay và trả kết quả, không yêu cầu follow/cùng Group và không phát thông báo được mời. | D thành Member ngay, tổng 3→4, có quyền đọc toàn lịch sử. | END:SUCCESS | FR-M16-08.01, FR-M16-08.04, FR-M16-08.05, FR-M16-08.06, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, BR-M16-01, BR-M16-03, BR-M16-06, BR-M16-25, BR-M16-28, FR-M16-02.02, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-27, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E11 — thay toàn bộ M1 đến kết thúc.** Người dùng ngoài cuộc, chưa từng là thành viên nhóm.

<!-- sc:branch SC-M16-007 E11 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E11.1 | ACT-002 | Chọn thêm Dũng vào nhóm G-ABC. | Cờ Bật, phiên hợp lệ nhưng thiếu vai trò thành viên hiện tại. | E11.2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06 |
| E11.2 | SYSTEM | UC-M16-018 kiểm tư cách đúng cuộc/nhóm và từ chối yêu cầu vì thiếu quyền thành viên hiện tại. | Không đọc dữ liệu hoặc thay đổi trạng thái bằng yêu cầu trái quyền. | END:REJECTED | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |


**E12 — thay toàn bộ M1 đến kết thúc.** Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current.

<!-- sc:branch SC-M16-007 E12 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E12.1 | ACT-014 | Chọn thêm Dũng vào nhóm G-ABC. | Có cutoff rời, chưa gia nhập lại, cờ Bật. | E12.2 | FR-M16-04.10, BR-M16-27 |
| E12.2 | SYSTEM | Từ chối thao tác cần current membership. Cựu chỉ đọc lịch sử trước cutoff theo SC-M16-003/E13, vào lại qua SC-M16-007 hoặc SC-M16-009. | Nhóm/hộp thư/lịch sử trước cutoff của cựu được giữ, không có thay đổi từ thao tác trái quyền. | END:REJECTED | FR-M16-04.10, FR-M16-05.06, BR-M16-05, BR-M16-27, BR-M16-28 |


<!-- sc:end SC-M16-007 -->

<a id="sc-m16-008"></a>

<!-- sc:scenario SC-M16-008 -->

### SC-M16-008

#### 1. Tên kịch bản chuẩn

Lấy link mời nhóm chat — BF-M16-008. UC owner [UC-M16-010](../../us/US-M16.md#uc-m16-010).

#### 2. Actor thực hiện

ACT-012 — Thành viên cuộc trò chuyện khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Có nhóm và người yêu cầu lấy link. Không lấy gửi link ngoài iShare thành bước bắt buộc để hoàn tất chức năng lấy link. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-008 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. B nhận đúng L-G-ABC sẵn có, tư cách/số người/công tắc giữ nguyên. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-008 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-012 | Yêu cầu lấy link mời của G-ABC. | D8 B current G-ABC, L-G-ABC là ký hiệu giả lập link mời, không chứa token thật. | M2 | FR-M16-08.10, FR-M16-08.11, FR-M16-08.12, FR-M16-08.13, BR-M16-29 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm current membership rồi trả link chung duy nhất L-G-ABC. Link không hết hạn, không có thu hồi/tạo lại, không tự phát thông báo được mời. Actor có thể gửi qua kênh bất kỳ sau khi nhận, người khác xin gia nhập ở SC-M16-009. | B nhận đúng L-G-ABC sẵn có, tư cách/số người/công tắc giữ nguyên. | END:SUCCESS | FR-M16-08.10, FR-M16-08.11, FR-M16-08.12, FR-M16-08.13, BR-M16-29, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-008 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E1.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E2 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E2.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E3 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E3.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E4 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E4.1 | FR-M16-08.10, FR-M16-08.11, FR-M16-08.12, FR-M16-08.13, BR-M16-29, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| E5 | system | M1 | ACT-002 — Người dùng ngoài cuộc, chưa từng là thành viên nhóm. | E5.1 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| E6 | system | M1 | ACT-014 — Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current. | E6.1 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |


<!-- sc:branch SC-M16-008 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-008 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E3 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-008 E3 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E3.1 | ACT-001 | Yêu cầu lấy link mời của G-ABC. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E3.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E3.2 | SYSTEM | Từ chối yêu cầu Chat của Guest, trả kết quả không được thực hiện chức năng này. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E4 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-008 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-007 | Yêu cầu lấy link mời của G-ABC. | D8 B current G-ABC, L-G-ABC là ký hiệu giả lập link mời, không chứa token thật. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E4.2 | FR-M16-08.10, FR-M16-08.11, FR-M16-08.12, FR-M16-08.13, BR-M16-29, FR-M16-15.04, FR-M10-12.08 |
| E4.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm current membership rồi trả link chung duy nhất L-G-ABC. Link không hết hạn, không có thu hồi/tạo lại, không tự phát thông báo được mời. Actor có thể gửi qua kênh bất kỳ sau khi nhận, người khác xin gia nhập ở SC-M16-009. | B nhận đúng L-G-ABC sẵn có, tư cách/số người/công tắc giữ nguyên. | END:SUCCESS | FR-M16-08.10, FR-M16-08.11, FR-M16-08.12, FR-M16-08.13, BR-M16-29, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E5 — thay toàn bộ M1 đến kết thúc.** Người dùng ngoài cuộc, chưa từng là thành viên nhóm.

<!-- sc:branch SC-M16-008 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-002 | Yêu cầu lấy link mời của G-ABC. | Cờ Bật, phiên hợp lệ nhưng thiếu vai trò thành viên hiện tại. | E5.2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06 |
| E5.2 | SYSTEM | UC-M16-018 kiểm tư cách đúng cuộc/nhóm và từ chối yêu cầu vì thiếu quyền thành viên hiện tại. | Không đọc dữ liệu hoặc thay đổi trạng thái bằng yêu cầu trái quyền. | END:REJECTED | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |


**E6 — thay toàn bộ M1 đến kết thúc.** Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current.

<!-- sc:branch SC-M16-008 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-014 | Yêu cầu lấy link mời của G-ABC. | Có cutoff rời, chưa gia nhập lại, cờ Bật. | E6.2 | FR-M16-04.10, BR-M16-27 |
| E6.2 | SYSTEM | Từ chối thao tác cần current membership. Cựu chỉ đọc lịch sử trước cutoff theo SC-M16-003/E13, vào lại qua SC-M16-007 hoặc SC-M16-009. | Nhóm/hộp thư/lịch sử trước cutoff của cựu được giữ, không có thay đổi từ thao tác trái quyền. | END:REJECTED | FR-M16-04.10, FR-M16-05.06, BR-M16-05, BR-M16-27, BR-M16-28 |


<!-- sc:end SC-M16-008 -->

<a id="sc-m16-009"></a>

<!-- sc:scenario SC-M16-009 -->

### SC-M16-009

#### 1. Tên kịch bản chuẩn

Xin gia nhập qua link mời — BF-M16-009. UC owner [UC-M16-011](../../us/US-M16.md#uc-m16-011).

#### 2. Actor thực hiện

ACT-002 — Người dùng đã đăng nhập khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Có link chung của nhóm và ngữ cảnh người mở. Phiên, số thành viên, công tắc và pending kiểm trong luồng. Kết quả chức năng xin gia nhập có thể là Member hoặc ghi nhận yêu cầu Chờ duyệt đúng nguồn. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-009 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. D nhận tư cách Member, tổng 3→4, được đọc toàn lịch sử khi mở cuộc. J-D Chờ duyệt, tổng 3 giữ3. Đây là thành công ghi nhận yêu cầu xin, không tuyên bố D đã vào. J-D cũ Đã từ chối, J-D2 Chờ duyệt mới, D chưa là thành viên. D9-rejoin D current mới, toàn lịch sử được phép, không có danh sách chặn. Mốc vào lại còn GAP-SC-M16-005. D Member, tổng 3→4, toàn lịch sử được phép xem, không tự tạo tin hay đọc lịch sử thay D. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-009 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Mở link mời L-G-ABC để xin gia nhập. | D9 D ACTIVE chưa là thành viên, nhóm tổng 3, duyệt Tắt, không có yêu cầu Chờ duyệt của D. | M2 | FR-M16-16.01, FR-M16-16.02, FR-M16-16.03, FR-M16-16.04, FR-M16-16.05, FR-M16-16.06, FR-M16-16.07, FR-M16-16.08, BR-M16-06, BR-M16-28, BR-M16-29 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm người mở link có phiên hợp lệ và cờ Chat, trả tên Ôn thi Lý cùng lựa chọn Xin gia nhập, chưa hiển thị tin của nhóm. | D chỉ thấy tên Ôn thi Lý và lựa chọn Xin gia nhập, chưa thấy lịch sử. | M3 | FR-M16-16.01, FR-M16-16.02, FR-M16-16.03, FR-M16-16.04, FR-M16-16.05, FR-M16-16.06, FR-M16-16.07, FR-M16-16.08, BR-M16-06, BR-M16-28, BR-M16-29, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| M3 | ACT-002 | Chọn Xin gia nhập nhóm. | D9 link G-ABC, người xin D. | M4 | FR-M16-16.03 |
| M4 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm nhóm chưa100, D chưa có yêu cầu gia nhập Chờ duyệt tới nhóm. Công tắc Tắt. UC-M16-019 kiểm người đích chưa là thành viên, đủ điều kiện tài khoản và số thành viên thực tế trước khi vào, gồm cả tài khoản không ACTIVE đang còn tư cách. Ghi Member, người mới/vào lại đọc được toàn lịch sử, không áp cutoff cũ. Người chờ chưa chiếm chỗ. Khi vào lại cung cấp M07 thay đổi tư cách để bắt đầu Đang nhận riêng nhóm, giữ cài đặt tắt toàn Chat. Trả kết quả gia nhập, không thông báo được mời. | D Member, tổng 3→4, toàn lịch sử được phép xem, không tự tạo tin hay đọc lịch sử thay D. | END:SUCCESS | FR-M16-16.03, FR-M16-16.05, FR-M16-16.06, FR-M16-16.08, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-009 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M4 | D chọn xin khi duyệt Bật, tổng 3, không có pending trùng. | E1.1 | FR-M16-16.04, FR-M16-10.07, BR-M16-06 |
| E2 | system | M4 | Nhóm đã100 tại lúc xin, gồm cả khi duyệt Bật. | E2.1 | FR-M16-16.05, BR-M16-29 |
| E3 | system | M4 | D đã có J-D Chờ duyệt tới cùng nhóm. | E3.1 | FR-M16-16.06, BR-M16-29 |
| E4 | system | M4 | J-D cũ Đã từ chối, D xin lại ngay, duyệt vẫn Bật và còn chỗ. | E4.1 | FR-M16-16.04, FR-M16-16.07, BR-M16-29 |
| E5 | system | M4 | D là cựu xin lại khi duyệt Tắt, còn chỗ và đủ điều kiện. | E5.1 | FR-M16-16.03, FR-M16-16.08, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08 |
| E6 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E6.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E7 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E7.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E8 | system | M4 | Đã qua bước xem ban đầu, nhưng cờ Chat Tắt với người không ADMIN tại lúc gửi yêu cầu hoặc quyết định. | E8.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E9 | system | M4 | Đã qua bước xem ban đầu, nhưng người gọi BANNED hoặc không còn quyền thao tác tại lúc gửi. | E9.1 | FR-M16-03.03, FR-M16-10.04, BR-M16-05, BR-M16-22, BR-M01-18 |
| E10 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E10.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E11 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E11.1 | FR-M16-16.01, FR-M16-16.02, FR-M16-16.03, FR-M16-16.04, FR-M16-16.05, FR-M16-16.06, FR-M16-16.07, FR-M16-16.08, BR-M16-06, BR-M16-28, BR-M16-29, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, BR-M16-03, BR-M16-25, BR-M16-27, FR-M07-09.08, BR-M07-08 |


<!-- sc:branch SC-M16-009 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Kiểm các điều kiện rồi tạo J-D Chờ duyệt, trả kết quả đã ghi nhận yêu cầu. D chưa là thành viên, chưa đọc lịch sử, chưa chiếm chỗ100. Quyết định Admin là chức năng SC-M16-010. | J-D Chờ duyệt, tổng 3 giữ3. Đây là thành công ghi nhận yêu cầu xin, không tuyên bố D đã vào. | END:SUCCESS | FR-M16-16.04, FR-M16-10.07, BR-M16-06 |


<!-- sc:branch SC-M16-009 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Từ chối xin gia nhập theo giới hạn nguồn trước khi tạo yêu cầu mới. | D9-full tổng 100, không có J-D mới hay Member D. | END:REJECTED | FR-M16-16.05, BR-M16-29 |


<!-- sc:branch SC-M16-009 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Từ chối gửi thêm yêu cầu gia nhập đang chờ. | J-D Chờ duyệt giữ nguyên, không thêm yêu cầu mới. | END:REJECTED | FR-M16-16.06, BR-M16-29 |


<!-- sc:branch SC-M16-009 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Ghi yêu cầu mới J-D2 Chờ duyệt, trả kết quả ghi nhận, không áp cooldown hoặc trần số lần. | J-D cũ Đã từ chối, J-D2 Chờ duyệt mới, D chưa là thành viên. | END:SUCCESS | FR-M16-16.04, FR-M16-16.07, BR-M16-29 |


<!-- sc:branch SC-M16-009 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | UC-M16-019 kiểm người đích chưa là thành viên, đủ điều kiện tài khoản và số thành viên thực tế trước khi vào, gồm cả tài khoản không ACTIVE đang còn tư cách. Ghi Member, người mới/vào lại đọc được toàn lịch sử, không áp cutoff cũ. Người chờ chưa chiếm chỗ. Khi vào lại cung cấp M07 thay đổi tư cách để bắt đầu Đang nhận riêng nhóm, giữ cài đặt tắt toàn Chat. Kết nạp lại theo công tắc hiện tại và trả tư cách Member. | D9-rejoin D current mới, toàn lịch sử được phép, không có danh sách chặn. Mốc vào lại còn GAP-SC-M16-005. | END:SUCCESS | FR-M16-16.03, FR-M16-16.08, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08 |


<!-- sc:branch SC-M16-009 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-009 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


<!-- sc:branch SC-M16-009 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | UC-M16-018 kiểm tại thao tác gửi và từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Trả kết quả, không làm bù thao tác này khi cờ bật lại. | Giữ dữ liệu đã có trước M3, không thực hiện yêu cầu xin hoặc quyết định duyệt bị chặn. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


<!-- sc:branch SC-M16-009 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | UC-M16-018 từ chối thao tác gửi theo trạng thái hoặc tư cách hiện tại, trả kết quả chưa thực hiện yêu cầu này. | Danh sách hoặc preview đã xem không cấp quyền gửi tiếp sau khi mất quyền. Chính sách giao stream cũ giữ GAP-SC-M16-001. | END:REJECTED | FR-M16-03.03, FR-M16-10.04, BR-M16-05, BR-M16-22, BR-M01-18 |


**E10 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-009 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-001 | Mở link mời L-G-ABC để xin gia nhập. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E10.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E10.2 | SYSTEM | Yêu cầu đăng nhập trước khi xin gia nhập, chưa cấp quyền đọc tin hoặc ghi yêu cầu gia nhập. Đăng nhập thuộc M01, sau có phiên actor có thể mở lại link và thực hiện đủ M1–M4, không hứa tự chuyển hướng. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E11 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-009 E11 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E11.1 | ACT-007 | Mở link mời L-G-ABC để xin gia nhập. | D9 D ACTIVE chưa là thành viên, nhóm tổng 3, duyệt Tắt, không có yêu cầu Chờ duyệt của D. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E11.2 | FR-M16-16.01, FR-M16-16.02, FR-M16-16.03, FR-M16-16.04, FR-M16-16.05, FR-M16-16.06, FR-M16-16.07, FR-M16-16.08, BR-M16-06, BR-M16-28, BR-M16-29, FR-M16-15.04, FR-M10-12.08 |
| E11.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm người mở link có phiên hợp lệ và cờ Chat, trả tên Ôn thi Lý cùng lựa chọn Xin gia nhập, chưa hiển thị tin của nhóm. | D chỉ thấy tên Ôn thi Lý và lựa chọn Xin gia nhập, chưa thấy lịch sử. | E11.3 | FR-M16-16.01, FR-M16-16.02, FR-M16-16.03, FR-M16-16.04, FR-M16-16.05, FR-M16-16.06, FR-M16-16.07, FR-M16-16.08, BR-M16-06, BR-M16-28, BR-M16-29, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E11.3 | ACT-007 | Chọn Xin gia nhập nhóm. | D9 link G-ABC, người xin D. | E11.4 | FR-M16-16.03, FR-M16-15.04, FR-M10-12.08 |
| E11.4 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm nhóm chưa100, D chưa có yêu cầu gia nhập Chờ duyệt tới nhóm. Công tắc Tắt. UC-M16-019 kiểm người đích chưa là thành viên, đủ điều kiện tài khoản và số thành viên thực tế trước khi vào, gồm cả tài khoản không ACTIVE đang còn tư cách. Ghi Member, người mới/vào lại đọc được toàn lịch sử, không áp cutoff cũ. Người chờ chưa chiếm chỗ. Khi vào lại cung cấp M07 thay đổi tư cách để bắt đầu Đang nhận riêng nhóm, giữ cài đặt tắt toàn Chat. Trả kết quả gia nhập, không thông báo được mời. | D Member, tổng 3→4, toàn lịch sử được phép xem, không tự tạo tin hay đọc lịch sử thay D. | END:SUCCESS | FR-M16-16.03, FR-M16-16.05, FR-M16-16.06, FR-M16-16.08, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


<!-- sc:end SC-M16-009 -->

<a id="sc-m16-010"></a>

<!-- sc:scenario SC-M16-010 -->

### SC-M16-010

#### 1. Tên kịch bản chuẩn

Duyệt người chờ vào nhóm chat — BF-M16-010. UC owner [UC-M16-012](../../us/US-M16.md#uc-m16-012).

#### 2. Actor thực hiện

ACT-013 — Admin nhóm chat khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Có nhóm, actor và các bản ghi chờ. Quyền và trạng thái phải được kiểm ở cả mở danh sách lẫn khi gửi quyết định, không giả định bản ghi còn chờ vì vừa hiển thị. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-010 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. P-D Đã chấp nhận và D Member, tổng 98→99. Admin nhận kết quả quyết định. P-D Đã từ chối, D chưa là thành viên, tổng 98 giữ98. Quyết định Từ chối là SUCCESS của chức năng duyệt. P-D Đã chấp nhận, D Member có toàn lịch sử, tổng 98→99, J-E còn Chờ duyệt. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-010 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-013 | Mở danh sách người chờ của G98 để duyệt. | D10 G98 có 98 thành viên, A Admin, P-D và J-E Chờ duyệt, đích ACTIVE chưa là thành viên. | M2 | FR-M16-10.01, FR-M16-10.02, FR-M16-10.03, FR-M16-10.04, FR-M16-10.05, FR-M16-10.06, FR-M16-10.07, BR-M16-03, BR-M16-05, BR-M16-06 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm Admin nhóm chat đúng nhóm, hiển thị đề nghị thêm và yêu cầu gia nhập đang Chờ duyệt. Người chờ không tính vào tổng hiện tại. | Danh sách có P-D do Member đề nghị và J-E do E xin qua link, cả hai Chờ duyệt, tổng thành viên98. | M3 | FR-M16-10.01, FR-M16-10.02, FR-M16-10.03, FR-M16-10.04, FR-M16-10.05, FR-M16-10.06, FR-M16-10.07, BR-M16-03, BR-M16-05, BR-M16-06, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| M3 | ACT-013 | Chọn Chấp nhận P-D. | Bản ghi P-D, quyết định Chấp nhận. | M4 | FR-M16-10.01 |
| M4 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm P-D vẫn Chờ duyệt. UC-M16-019 kiểm người đích chưa là thành viên, đủ điều kiện tài khoản và số thành viên thực tế trước khi vào, gồm cả tài khoản không ACTIVE đang còn tư cách. Ghi Member, người mới/vào lại đọc được toàn lịch sử, không áp cutoff cũ. Người chờ chưa chiếm chỗ. Khi vào lại cung cấp M07 thay đổi tư cách để bắt đầu Đang nhận riêng nhóm, giữ cài đặt tắt toàn Chat. Kết nạp thành công rồi chuyển P-D sang Đã chấp nhận, trả kết quả. Cùng quy tắc áp khi chọn J-E thay cho P-D. | P-D Đã chấp nhận, D Member có toàn lịch sử, tổng 98→99, J-E còn Chờ duyệt. | END:SUCCESS | FR-M16-10.01, FR-M16-10.06, FR-M16-10.07, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.03, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-010 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M3 | Admin lựa chọn Từ chối P-D hoặc J-E. | E1.1 | FR-M16-10.02, FR-M16-10.06, FR-M16-16.07, BR-M16-06, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E2 | system | M4 | P-D hoặc J-E không còn Chờ duyệt khi gửi quyết định. | E2.1 | FR-M16-10.06 |
| E3 | system | M4 | Nhóm đã100 khi Admin gửi Chấp nhận. | E3.1 | FR-M16-10.03, FR-M16-10.07, BR-M16-03 |
| E4 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E4.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E5 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E5.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E6 | system | M4 | Đã qua bước xem ban đầu, nhưng cờ Chat Tắt với người không ADMIN tại lúc gửi yêu cầu hoặc quyết định. | E6.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E7 | system | M4 | Đã qua bước xem ban đầu, nhưng người gọi BANNED hoặc không còn quyền thao tác tại lúc gửi. | E7.1 | FR-M16-03.03, FR-M16-10.04, BR-M16-05, BR-M16-22, BR-M01-18 |
| E8 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E8.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E9 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E9.1 | FR-M16-10.01, FR-M16-10.02, FR-M16-10.03, FR-M16-10.04, FR-M16-10.05, FR-M16-10.06, FR-M16-10.07, BR-M16-03, BR-M16-05, BR-M16-06, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-16.03, FR-M16-16.08, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08 |
| E10 | system | M1 | ACT-012 — Member hiện tại có yêu cầu chỉ Admin nhóm chat được làm. | E10.1 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| E11 | system | M1 | ACT-014 — Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current. | E11.1 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |


<!-- sc:branch SC-M16-010 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-013 | Chọn Từ chối bản ghi đang chờ P-D. | D10 quyết định Từ chối, P-D còn Chờ duyệt. | E1.2 | FR-M16-10.02 |
| E1.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm bản ghi vẫn Chờ duyệt rồi chuyển Đã từ chối, trả quyết định. Nếu là yêu cầu qua link, người xin được gửi lại ngay theo SC-M16-009. | P-D Đã từ chối, D chưa là thành viên, tổng 98 giữ98. Quyết định Từ chối là SUCCESS của chức năng duyệt. | END:SUCCESS | FR-M16-10.02, FR-M16-10.06, FR-M16-16.07, BR-M16-06, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


<!-- sc:branch SC-M16-010 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Từ chối thao tác Chấp nhận hoặc Từ chối bản ghi đã được giải quyết, trả kết quả không ra quyết định lần nữa. | Snapshot P-D đã Đã chấp nhận hoặc Đã từ chối, trạng thái đã có giữ nguyên. | END:REJECTED | FR-M16-10.06 |


<!-- sc:branch SC-M16-010 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Từ chối thao tác kết nạp, không đưa thêm thành viên. Không gán Đã từ chối cho bản ghi chỉ vì duyệt tay đầy chỗ. Đây là yêu cầu bị từ chối, bản ghi chờ chưa được quyết định lại. | D10-full tổng 100 giữ100, P-D vẫn Chờ duyệt trong snapshot không có thao tác khác. | END:REJECTED | FR-M16-10.03, FR-M16-10.07, BR-M16-03 |


<!-- sc:branch SC-M16-010 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-010 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


<!-- sc:branch SC-M16-010 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | UC-M16-018 kiểm tại thao tác gửi và từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Trả kết quả, không làm bù thao tác này khi cờ bật lại. | Giữ dữ liệu đã có trước M3, không thực hiện yêu cầu xin hoặc quyết định duyệt bị chặn. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


<!-- sc:branch SC-M16-010 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | UC-M16-018 từ chối thao tác gửi theo trạng thái hoặc tư cách hiện tại, trả kết quả chưa thực hiện yêu cầu này. | Danh sách hoặc preview đã xem không cấp quyền gửi tiếp sau khi mất quyền. Chính sách giao stream cũ giữ GAP-SC-M16-001. | END:REJECTED | FR-M16-03.03, FR-M16-10.04, BR-M16-05, BR-M16-22, BR-M01-18 |


**E8 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-010 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-001 | Mở danh sách người chờ của G98 để duyệt. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E8.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E8.2 | SYSTEM | Từ chối yêu cầu Chat của Guest, trả kết quả không được thực hiện chức năng này. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E9 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-010 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-007 | Mở danh sách người chờ của G98 để duyệt. | D10 G98 có 98 thành viên, A Admin, P-D và J-E Chờ duyệt, đích ACTIVE chưa là thành viên. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E9.2 | FR-M16-10.01, FR-M16-10.02, FR-M16-10.03, FR-M16-10.04, FR-M16-10.05, FR-M16-10.06, FR-M16-10.07, BR-M16-03, BR-M16-05, BR-M16-06, FR-M16-15.04, FR-M10-12.08 |
| E9.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm Admin nhóm chat đúng nhóm, hiển thị đề nghị thêm và yêu cầu gia nhập đang Chờ duyệt. Người chờ không tính vào tổng hiện tại. | Danh sách có P-D do Member đề nghị và J-E do E xin qua link, cả hai Chờ duyệt, tổng thành viên98. | E9.3 | FR-M16-10.01, FR-M16-10.02, FR-M16-10.03, FR-M16-10.04, FR-M16-10.05, FR-M16-10.06, FR-M16-10.07, BR-M16-03, BR-M16-05, BR-M16-06, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E9.3 | ACT-007 | Chọn Chấp nhận P-D. | Bản ghi P-D, quyết định Chấp nhận. | E9.4 | FR-M16-10.01, FR-M16-15.04, FR-M10-12.08 |
| E9.4 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm P-D vẫn Chờ duyệt. UC-M16-019 kiểm người đích chưa là thành viên, đủ điều kiện tài khoản và số thành viên thực tế trước khi vào, gồm cả tài khoản không ACTIVE đang còn tư cách. Ghi Member, người mới/vào lại đọc được toàn lịch sử, không áp cutoff cũ. Người chờ chưa chiếm chỗ. Khi vào lại cung cấp M07 thay đổi tư cách để bắt đầu Đang nhận riêng nhóm, giữ cài đặt tắt toàn Chat. Kết nạp thành công rồi chuyển P-D sang Đã chấp nhận, trả kết quả. Cùng quy tắc áp khi chọn J-E thay cho P-D. | P-D Đã chấp nhận, D Member có toàn lịch sử, tổng 98→99, J-E còn Chờ duyệt. | END:SUCCESS | FR-M16-10.01, FR-M16-10.06, FR-M16-10.07, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.03, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E10 — thay toàn bộ M1 đến kết thúc.** Member hiện tại có yêu cầu chỉ Admin nhóm chat được làm.

<!-- sc:branch SC-M16-010 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-012 | Mở danh sách người chờ của G98 để duyệt. | Cờ Bật, phiên hợp lệ nhưng thiếu vai trò Admin nhóm chat. | E10.2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06 |
| E10.2 | SYSTEM | UC-M16-018 kiểm tư cách đúng cuộc/nhóm và từ chối yêu cầu vì thiếu quyền Admin nhóm chat. | Không đọc dữ liệu hoặc thay đổi trạng thái bằng yêu cầu trái quyền. | END:REJECTED | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |


**E11 — thay toàn bộ M1 đến kết thúc.** Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current.

<!-- sc:branch SC-M16-010 E11 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E11.1 | ACT-014 | Mở danh sách người chờ của G98 để duyệt. | Có cutoff rời, chưa gia nhập lại, cờ Bật. | E11.2 | FR-M16-04.10, BR-M16-27 |
| E11.2 | SYSTEM | Từ chối thao tác cần current membership. Cựu chỉ đọc lịch sử trước cutoff theo SC-M16-003/E13, vào lại qua SC-M16-007 hoặc SC-M16-009. | Nhóm/hộp thư/lịch sử trước cutoff của cựu được giữ, không có thay đổi từ thao tác trái quyền. | END:REJECTED | FR-M16-04.10, FR-M16-05.06, BR-M16-05, BR-M16-27, BR-M16-28 |


<!-- sc:end SC-M16-010 -->

<a id="sc-m16-011"></a>

<!-- sc:scenario SC-M16-011 -->

### SC-M16-011

#### 1. Tên kịch bản chuẩn

Bật hoặc tắt duyệt thành viên mới — BF-M16-011. UC owner [UC-M16-013](../../us/US-M16.md#uc-m16-013).

#### 2. Actor thực hiện

ACT-013 — Admin nhóm chat khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Có công tắc và người chờ theo D11. Đường chuẩn chọn Tắt, lựa chọn Bật được mô tả ở E. Pending trùng/stale/timestamp bằng nhau giữ GAP-SC-M16-004. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-011 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. Công tắc Tắt, Q1/Q2 Đã chấp nhận và 2 Member mới, Q3/Q4/Q5 Đã từ chối, tổng 98→100. Không giữ người dư Chờ duyệt. Công tắc Tắt→Bật, thành viên hiện có giữ nguyên. D11-fit tổng 50→55, cả5 Member mới, không còn pending này. D11-empty tổng 3 giữ3, công tắc Bật→Tắt. D11-full tổng 100 giữ100, Q1–Q5 Đã từ chối. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-011 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-013 | Chọn Tắt duyệt thành viên mới cho G98. | D11 G98 tổng 98, công tắc Bật, A Admin. Q1–Q5 hai loại xen kẽ, thời gian 09:01–09:05 phân biệt, mọi đích ACTIVE chưa là thành viên. | M2 | FR-M16-09.01, FR-M16-09.02, FR-M16-09.03, FR-M16-09.04, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, BR-M16-06, BR-M16-33 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm Admin nhóm chat, áp công tắc Tắt. UC-M16-020 lấy chung người chờ hai loại theo thời điểm bắt đầu chờ sớm trước. Với mỗi người còn chỗ thực hiện UC-M16-019, kiểm tư cách/tài khoản/cap hiện tại, kết nạp Member rồi ghi Đã chấp nhận. Tới100, chuyển người dư sang Đã từ chối, trả cài đặt và kết quả hàng chờ. Người được vào có toàn lịch sử, người bị từ chối có thể vào lại theo luồng thường khi đủ điều kiện. | Công tắc Tắt, Q1/Q2 Đã chấp nhận và 2 Member mới, Q3/Q4/Q5 Đã từ chối, tổng 98→100. Không giữ người dư Chờ duyệt. | END:SUCCESS | FR-M16-09.01, FR-M16-09.02, FR-M16-09.03, FR-M16-09.04, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, BR-M16-06, BR-M16-33, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-011 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Actor chọn Bật duyệt thay cho Tắt. | E1.1 | FR-M16-09.01, FR-M16-08.02, FR-M16-08.03, FR-M16-16.04, BR-M16-06, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E2 | system | M2 | Admin Tắt khi có 50 thành viên và5 người chờ hợp lệ. | E2.1 | FR-M16-09.03, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, BR-M16-33 |
| E3 | system | M2 | Admin Tắt khi không có người chờ. | E3.1 | FR-M16-09.01, FR-M16-09.03, BR-M16-33 |
| E4 | system | M2 | Admin Tắt khi nhóm đã100 và5 người chờ hợp lệ. | E4.1 | FR-M16-09.03, FR-M16-09.04, BR-M16-33 |
| E5 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E5.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E6 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E6.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E7 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E7.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E8 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E8.1 | FR-M16-09.01, FR-M16-09.02, FR-M16-09.03, FR-M16-09.04, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, BR-M16-06, BR-M16-33, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| E9 | system | M1 | ACT-012 — Member hiện tại có yêu cầu chỉ Admin nhóm chat được làm. | E9.1 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| E10 | system | M1 | ACT-014 — Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current. | E10.1 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |


<!-- sc:branch SC-M16-011 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-013 | Chọn Bật duyệt thành viên mới. | D11-on công tắc trước Tắt, A Admin nhóm. | E1.2 | FR-M16-09.01 |
| E1.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Áp công tắc Bật cho lần thêm và xin sau đó. Member thêm tạo đề nghị, link tạo yêu cầu chờ, Admin nhóm thêm vẫn vào ngay. Không gọi UC-M16-020 khi Bật. | Công tắc Tắt→Bật, thành viên hiện có giữ nguyên. | END:SUCCESS | FR-M16-09.01, FR-M16-08.02, FR-M16-08.03, FR-M16-16.04, BR-M16-06, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


<!-- sc:branch SC-M16-011 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Áp Tắt, xử lý UC-M16-020 và UC-M16-019 lần lượt Q1–Q5 sớm trước, cả5 Đã chấp nhận, trả kết quả. | D11-fit tổng 50→55, cả5 Member mới, không còn pending này. | END:SUCCESS | FR-M16-09.03, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, BR-M16-33 |


<!-- sc:branch SC-M16-011 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Áp Tắt và trả kết quả hàng chờ rỗng, không tạo người hoặc yêu cầu giả. | D11-empty tổng 3 giữ3, công tắc Bật→Tắt. | END:SUCCESS | FR-M16-09.01, FR-M16-09.03, BR-M16-33 |


<!-- sc:branch SC-M16-011 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Áp Tắt và chuyển cả5 người chờ Đã từ chối do không còn chỗ, trả kết quả đầy đủ. | D11-full tổng 100 giữ100, Q1–Q5 Đã từ chối. | END:SUCCESS | FR-M16-09.03, FR-M16-09.04, BR-M16-33 |


<!-- sc:branch SC-M16-011 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-011 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E7 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-011 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-001 | Chọn Tắt duyệt thành viên mới cho G98. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E7.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E7.2 | SYSTEM | Từ chối yêu cầu Chat của Guest, trả kết quả không được thực hiện chức năng này. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E8 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-011 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-007 | Chọn Tắt duyệt thành viên mới cho G98. | D11 G98 tổng 98, công tắc Bật, A Admin. Q1–Q5 hai loại xen kẽ, thời gian 09:01–09:05 phân biệt, mọi đích ACTIVE chưa là thành viên. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E8.2 | FR-M16-09.01, FR-M16-09.02, FR-M16-09.03, FR-M16-09.04, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, BR-M16-06, BR-M16-33, FR-M16-15.04, FR-M10-12.08 |
| E8.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm Admin nhóm chat, áp công tắc Tắt. UC-M16-020 lấy chung người chờ hai loại theo thời điểm bắt đầu chờ sớm trước. Với mỗi người còn chỗ thực hiện UC-M16-019, kiểm tư cách/tài khoản/cap hiện tại, kết nạp Member rồi ghi Đã chấp nhận. Tới100, chuyển người dư sang Đã từ chối, trả cài đặt và kết quả hàng chờ. Người được vào có toàn lịch sử, người bị từ chối có thể vào lại theo luồng thường khi đủ điều kiện. | Công tắc Tắt, Q1/Q2 Đã chấp nhận và 2 Member mới, Q3/Q4/Q5 Đã từ chối, tổng 98→100. Không giữ người dư Chờ duyệt. | END:SUCCESS | FR-M16-09.01, FR-M16-09.02, FR-M16-09.03, FR-M16-09.04, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, BR-M16-06, BR-M16-33, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E9 — thay toàn bộ M1 đến kết thúc.** Member hiện tại có yêu cầu chỉ Admin nhóm chat được làm.

<!-- sc:branch SC-M16-011 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-012 | Chọn Tắt duyệt thành viên mới cho G98. | Cờ Bật, phiên hợp lệ nhưng thiếu vai trò Admin nhóm chat. | E9.2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06 |
| E9.2 | SYSTEM | UC-M16-018 kiểm tư cách đúng cuộc/nhóm và từ chối yêu cầu vì thiếu quyền Admin nhóm chat. | Không đọc dữ liệu hoặc thay đổi trạng thái bằng yêu cầu trái quyền. | END:REJECTED | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |


**E10 — thay toàn bộ M1 đến kết thúc.** Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current.

<!-- sc:branch SC-M16-011 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-014 | Chọn Tắt duyệt thành viên mới cho G98. | Có cutoff rời, chưa gia nhập lại, cờ Bật. | E10.2 | FR-M16-04.10, BR-M16-27 |
| E10.2 | SYSTEM | Từ chối thao tác cần current membership. Cựu chỉ đọc lịch sử trước cutoff theo SC-M16-003/E13, vào lại qua SC-M16-007 hoặc SC-M16-009. | Nhóm/hộp thư/lịch sử trước cutoff của cựu được giữ, không có thay đổi từ thao tác trái quyền. | END:REJECTED | FR-M16-04.10, FR-M16-05.06, BR-M16-05, BR-M16-27, BR-M16-28 |


<!-- sc:end SC-M16-011 -->

<a id="sc-m16-012"></a>

<!-- sc:scenario SC-M16-012 -->

### SC-M16-012

#### 1. Tên kịch bản chuẩn

Xóa Member khỏi nhóm chat — BF-M16-012. UC owner [UC-M16-014](../../us/US-M16.md#uc-m16-014).

#### 2. Actor thực hiện

ACT-013 — Admin nhóm chat khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Có nhóm và đích Member, trạng thái quyền được kiểm trong luồng. D12 là snapshot độc lập, không dùng thao tác tự rời để thay việc xóa Member. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-012 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. C Bị xóa cutoff21:00, tổng 3→2, A/B vẫn nhắn và thêm được. C giữ hộp thư và lịch sử trước cutoff, mute riêng bị bỏ theo M07. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-012 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-013 | Chọn xóa Member C khỏi G-ABC. | D12 trước A Admin, B/C Member tổng 3, C có mute riêng nhóm, #60 gửi20:59. | M2 | FR-M16-11.01, FR-M16-11.02, FR-M16-11.03, FR-M16-14.03, BR-M16-03, BR-M16-05, BR-M16-27, BR-M16-28, FR-M07-09.08 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm Admin chính nhóm và đích C là Member. Đưa C ra, ghi Bị xóa và thời điểm rời21:00, giữ nhóm trong hộp thư C với lịch sử tin gửi trước 21:00 chỉ đọc. C không gửi/quản lý nhóm sau khi bị xóa. Nhóm còn 2 vẫn hoạt động bình thường. Cung cấp thay đổi tư cách cho M07 bỏ mute riêng của C, vào lại theo luồng thường. | C Bị xóa cutoff21:00, tổng 3→2, A/B vẫn nhắn và thêm được. C giữ hộp thư và lịch sử trước cutoff, mute riêng bị bỏ theo M07. | END:SUCCESS | FR-M16-11.01, FR-M16-11.02, FR-M16-11.03, FR-M16-14.03, BR-M16-03, BR-M16-05, BR-M16-27, BR-M16-28, FR-M07-09.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-012 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E1.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E2 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E2.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E3 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E3.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E4 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E4.1 | FR-M16-11.01, FR-M16-11.02, FR-M16-11.03, FR-M16-14.03, BR-M16-03, BR-M16-05, BR-M16-27, BR-M16-28, FR-M07-09.08, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| E5 | system | M1 | ACT-012 — Member hiện tại có yêu cầu chỉ Admin nhóm chat được làm. | E5.1 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| E6 | system | M1 | ACT-014 — Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current. | E6.1 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |


<!-- sc:branch SC-M16-012 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-012 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E3 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-012 E3 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E3.1 | ACT-001 | Chọn xóa Member C khỏi G-ABC. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E3.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E3.2 | SYSTEM | Từ chối yêu cầu Chat của Guest, trả kết quả không được thực hiện chức năng này. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E4 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-012 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-007 | Chọn xóa Member C khỏi G-ABC. | D12 trước A Admin, B/C Member tổng 3, C có mute riêng nhóm, #60 gửi20:59. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E4.2 | FR-M16-11.01, FR-M16-11.02, FR-M16-11.03, FR-M16-14.03, BR-M16-03, BR-M16-05, BR-M16-27, BR-M16-28, FR-M07-09.08, FR-M16-15.04, FR-M10-12.08 |
| E4.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm Admin chính nhóm và đích C là Member. Đưa C ra, ghi Bị xóa và thời điểm rời21:00, giữ nhóm trong hộp thư C với lịch sử tin gửi trước 21:00 chỉ đọc. C không gửi/quản lý nhóm sau khi bị xóa. Nhóm còn 2 vẫn hoạt động bình thường. Cung cấp thay đổi tư cách cho M07 bỏ mute riêng của C, vào lại theo luồng thường. | C Bị xóa cutoff21:00, tổng 3→2, A/B vẫn nhắn và thêm được. C giữ hộp thư và lịch sử trước cutoff, mute riêng bị bỏ theo M07. | END:SUCCESS | FR-M16-11.01, FR-M16-11.02, FR-M16-11.03, FR-M16-14.03, BR-M16-03, BR-M16-05, BR-M16-27, BR-M16-28, FR-M07-09.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E5 — thay toàn bộ M1 đến kết thúc.** Member hiện tại có yêu cầu chỉ Admin nhóm chat được làm.

<!-- sc:branch SC-M16-012 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-012 | Chọn xóa Member C khỏi G-ABC. | Cờ Bật, phiên hợp lệ nhưng thiếu vai trò Admin nhóm chat. | E5.2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06 |
| E5.2 | SYSTEM | UC-M16-018 kiểm tư cách đúng cuộc/nhóm và từ chối yêu cầu vì thiếu quyền Admin nhóm chat. | Không đọc dữ liệu hoặc thay đổi trạng thái bằng yêu cầu trái quyền. | END:REJECTED | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |


**E6 — thay toàn bộ M1 đến kết thúc.** Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current.

<!-- sc:branch SC-M16-012 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-014 | Chọn xóa Member C khỏi G-ABC. | Có cutoff rời, chưa gia nhập lại, cờ Bật. | E6.2 | FR-M16-04.10, BR-M16-27 |
| E6.2 | SYSTEM | Từ chối thao tác cần current membership. Cựu chỉ đọc lịch sử trước cutoff theo SC-M16-003/E13, vào lại qua SC-M16-007 hoặc SC-M16-009. | Nhóm/hộp thư/lịch sử trước cutoff của cựu được giữ, không có thay đổi từ thao tác trái quyền. | END:REJECTED | FR-M16-04.10, FR-M16-05.06, BR-M16-05, BR-M16-27, BR-M16-28 |


<!-- sc:end SC-M16-012 -->

<a id="sc-m16-013"></a>

<!-- sc:scenario SC-M16-013 -->

### SC-M16-013

#### 1. Tên kịch bản chuẩn

Đổi tên nhóm chat — BF-M16-013. UC owner [UC-M16-015](../../us/US-M16.md#uc-m16-015).

#### 2. Actor thực hiện

ACT-012 — Thành viên cuộc trò chuyện khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Có nhóm/người yêu cầu/tên mới. Quyền và giới hạn tên kiểm trong luồng, mọi current member có thể yêu cầu đổi. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-013 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. Tên Ôn thi Toán áp cho mọi thành viên, link L-G-ABC và tư cách giữ nguyên. D13-max lặp a100 lần, tên mới dài100, hoặc tên Ôn thi Toán có sẵn ở nhóm khác. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-013 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-012 | Nhập và gửi tên mới cho nhóm G-ABC. | D13 B Member, tên trước Ôn thi Lý, nhập “  Ôn thi Toán  ”. | M2 | FR-M16-12.01, FR-M16-12.02, FR-M16-12.03, BR-M16-05, BR-M16-29, BR-M16-32 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm current membership rồi trim tên và kiểm 1–100 ký tự. Áp tên mới với mọi thành viên và trả kết quả, tên trùng với nhóm khác được. Giữ link chung và vai trò. | Tên Ôn thi Toán áp cho mọi thành viên, link L-G-ABC và tư cách giữ nguyên. | END:SUCCESS | FR-M16-12.01, FR-M16-12.02, FR-M16-12.03, BR-M16-05, BR-M16-29, BR-M16-32, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-013 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Tên sau trim rỗng hoặc dài101 ký tự. | E1.1 | FR-M16-12.03, BR-M16-32 |
| E2 | system | M2 | Tên sau trim đúng 100 ký tự hoặc trùng tên nhóm khác. | E2.1 | FR-M16-12.01, FR-M16-12.03, BR-M16-32 |
| E3 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E3.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E4 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E4.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E5 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E5.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E6 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E6.1 | FR-M16-12.01, FR-M16-12.02, FR-M16-12.03, BR-M16-05, BR-M16-29, BR-M16-32, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| E7 | system | M1 | ACT-002 — Người dùng ngoài cuộc, chưa từng là thành viên nhóm. | E7.1 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| E8 | system | M1 | ACT-014 — Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current. | E8.1 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |


<!-- sc:branch SC-M16-013 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Từ chối đổi tên và trả kết quả dữ liệu không hợp lệ. | D13-bad tên ba dấu cách hoặc101 ký tự a. Tên nhóm vẫn Ôn thi Lý. | END:REJECTED | FR-M16-12.03, BR-M16-32 |


<!-- sc:branch SC-M16-013 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Chấp nhận tên hợp lệ, cập nhật với mọi thành viên, trả tên mới. | D13-max lặp a100 lần, tên mới dài100, hoặc tên Ôn thi Toán có sẵn ở nhóm khác. | END:SUCCESS | FR-M16-12.01, FR-M16-12.03, BR-M16-32 |


<!-- sc:branch SC-M16-013 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-013 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E5 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-013 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-001 | Nhập và gửi tên mới cho nhóm G-ABC. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E5.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E5.2 | SYSTEM | Từ chối yêu cầu Chat của Guest, trả kết quả không được thực hiện chức năng này. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E6 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-013 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-007 | Nhập và gửi tên mới cho nhóm G-ABC. | D13 B Member, tên trước Ôn thi Lý, nhập “  Ôn thi Toán  ”. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E6.2 | FR-M16-12.01, FR-M16-12.02, FR-M16-12.03, BR-M16-05, BR-M16-29, BR-M16-32, FR-M16-15.04, FR-M10-12.08 |
| E6.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm current membership rồi trim tên và kiểm 1–100 ký tự. Áp tên mới với mọi thành viên và trả kết quả, tên trùng với nhóm khác được. Giữ link chung và vai trò. | Tên Ôn thi Toán áp cho mọi thành viên, link L-G-ABC và tư cách giữ nguyên. | END:SUCCESS | FR-M16-12.01, FR-M16-12.02, FR-M16-12.03, BR-M16-05, BR-M16-29, BR-M16-32, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E7 — thay toàn bộ M1 đến kết thúc.** Người dùng ngoài cuộc, chưa từng là thành viên nhóm.

<!-- sc:branch SC-M16-013 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-002 | Nhập và gửi tên mới cho nhóm G-ABC. | Cờ Bật, phiên hợp lệ nhưng thiếu vai trò thành viên hiện tại. | E7.2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06 |
| E7.2 | SYSTEM | UC-M16-018 kiểm tư cách đúng cuộc/nhóm và từ chối yêu cầu vì thiếu quyền thành viên hiện tại. | Không đọc dữ liệu hoặc thay đổi trạng thái bằng yêu cầu trái quyền. | END:REJECTED | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |


**E8 — thay toàn bộ M1 đến kết thúc.** Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current.

<!-- sc:branch SC-M16-013 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-014 | Nhập và gửi tên mới cho nhóm G-ABC. | Có cutoff rời, chưa gia nhập lại, cờ Bật. | E8.2 | FR-M16-04.10, BR-M16-27 |
| E8.2 | SYSTEM | Từ chối thao tác cần current membership. Cựu chỉ đọc lịch sử trước cutoff theo SC-M16-003/E13, vào lại qua SC-M16-007 hoặc SC-M16-009. | Nhóm/hộp thư/lịch sử trước cutoff của cựu được giữ, không có thay đổi từ thao tác trái quyền. | END:REJECTED | FR-M16-04.10, FR-M16-05.06, BR-M16-05, BR-M16-27, BR-M16-28 |


<!-- sc:end SC-M16-013 -->

<a id="sc-m16-014"></a>

<!-- sc:scenario SC-M16-014 -->

### SC-M16-014

#### 1. Tên kịch bản chuẩn

Chuyển quyền Admin nhóm chat — BF-M16-014. UC owner [UC-M16-016](../../us/US-M16.md#uc-m16-016).

#### 2. Actor thực hiện

ACT-013 — Admin nhóm chat khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Có nhóm và Member được chọn, kiểm vai trò trong luồng. Đích không bị áp thêm điều kiện ACTIVE do nguồn chưa quy định, giao nhau tài khoản không thể khôi phục giữ GAP-SC-M16-006. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-014 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. Sau B Admin, A/C Member, tổng 3 giữ3, tối đa1 Admin, A chưa rời nhóm. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-014 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-013 | Chọn Member B nhận quyền Admin nhóm chat của G-ABC. | D14 trước A Admin, B/C Member, chọn B. | M2 | FR-M16-13.01, FR-M16-13.02, FR-M16-13.03, FR-M16-14.02, BR-M16-04, BR-M16-05, BR-M16-07, BR-M16-25, BR-M16-30 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm người chuyển là Admin nhóm chat hiện tại và đích B là Member trong cùng nhóm. Đặt B Admin nhóm chat và A thành Member, trả vai trò mới, giữ tối đa1 Admin. Việc rời nhóm là yêu cầu riêng ở SC-M16-015. | Sau B Admin, A/C Member, tổng 3 giữ3, tối đa1 Admin, A chưa rời nhóm. | END:SUCCESS | FR-M16-13.01, FR-M16-13.02, FR-M16-13.03, FR-M16-14.02, BR-M16-04, BR-M16-05, BR-M16-07, BR-M16-25, BR-M16-30, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-014 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Đích X ngoài nhóm hoặc không có vai trò Member. | E1.1 | FR-M16-13.01, BR-M16-04, BR-M16-07 |
| E2 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E2.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E3 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E3.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E4 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E4.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E5 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E5.1 | FR-M16-13.01, FR-M16-13.02, FR-M16-13.03, FR-M16-14.02, BR-M16-04, BR-M16-05, BR-M16-07, BR-M16-25, BR-M16-30, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| E6 | system | M1 | ACT-012 — Member hiện tại có yêu cầu chỉ Admin nhóm chat được làm. | E6.1 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| E7 | system | M1 | ACT-014 — Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current. | E7.1 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |


<!-- sc:branch SC-M16-014 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Từ chối chuyển quyền cho đích không đúng vai trò, trả kết quả. | D14-bad A vẫn Admin, X ngoài nhóm không được thêm tự động. | END:REJECTED | FR-M16-13.01, BR-M16-04, BR-M16-07 |


<!-- sc:branch SC-M16-014 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-014 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E4 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-014 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-001 | Chọn Member B nhận quyền Admin nhóm chat của G-ABC. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E4.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E4.2 | SYSTEM | Từ chối yêu cầu Chat của Guest, trả kết quả không được thực hiện chức năng này. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E5 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-014 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-007 | Chọn Member B nhận quyền Admin nhóm chat của G-ABC. | D14 trước A Admin, B/C Member, chọn B. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E5.2 | FR-M16-13.01, FR-M16-13.02, FR-M16-13.03, FR-M16-14.02, BR-M16-04, BR-M16-05, BR-M16-07, BR-M16-25, BR-M16-30, FR-M16-15.04, FR-M10-12.08 |
| E5.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm người chuyển là Admin nhóm chat hiện tại và đích B là Member trong cùng nhóm. Đặt B Admin nhóm chat và A thành Member, trả vai trò mới, giữ tối đa1 Admin. Việc rời nhóm là yêu cầu riêng ở SC-M16-015. | Sau B Admin, A/C Member, tổng 3 giữ3, tối đa1 Admin, A chưa rời nhóm. | END:SUCCESS | FR-M16-13.01, FR-M16-13.02, FR-M16-13.03, FR-M16-14.02, BR-M16-04, BR-M16-05, BR-M16-07, BR-M16-25, BR-M16-30, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E6 — thay toàn bộ M1 đến kết thúc.** Member hiện tại có yêu cầu chỉ Admin nhóm chat được làm.

<!-- sc:branch SC-M16-014 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-012 | Chọn Member B nhận quyền Admin nhóm chat của G-ABC. | Cờ Bật, phiên hợp lệ nhưng thiếu vai trò Admin nhóm chat. | E6.2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06 |
| E6.2 | SYSTEM | UC-M16-018 kiểm tư cách đúng cuộc/nhóm và từ chối yêu cầu vì thiếu quyền Admin nhóm chat. | Không đọc dữ liệu hoặc thay đổi trạng thái bằng yêu cầu trái quyền. | END:REJECTED | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |


**E7 — thay toàn bộ M1 đến kết thúc.** Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current.

<!-- sc:branch SC-M16-014 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-014 | Chọn Member B nhận quyền Admin nhóm chat của G-ABC. | Có cutoff rời, chưa gia nhập lại, cờ Bật. | E7.2 | FR-M16-04.10, BR-M16-27 |
| E7.2 | SYSTEM | Từ chối thao tác cần current membership. Cựu chỉ đọc lịch sử trước cutoff theo SC-M16-003/E13, vào lại qua SC-M16-007 hoặc SC-M16-009. | Nhóm/hộp thư/lịch sử trước cutoff của cựu được giữ, không có thay đổi từ thao tác trái quyền. | END:REJECTED | FR-M16-04.10, FR-M16-05.06, BR-M16-05, BR-M16-27, BR-M16-28 |


<!-- sc:end SC-M16-014 -->

<a id="sc-m16-015"></a>

<!-- sc:scenario SC-M16-015 -->

### SC-M16-015

#### 1. Tên kịch bản chuẩn

Rời nhóm chat — BF-M16-015. UC owner [UC-M16-017](../../us/US-M16.md#uc-m16-017).

#### 2. Actor thực hiện

ACT-012 — Thành viên cuộc trò chuyện khởi tạo đường chính. Các vai trò khác có đường E tại M1 trong mục 6. Hệ thống iShare dùng chủ thể SYSTEM, các module nội bộ cùng thuộc SYSTEM.

#### 3. Tiền điều kiện

Có nhóm và người yêu cầu rời. Tư cách và điều kiện Admin kiểm trong luồng. D15 độc lập với việc C bị xóa ở D12. Mỗi guard E chọn snapshot riêng từ đầu, thay dữ liệu tương ứng trong D, các yêu cầu khác giữ hợp lệ nếu không được nêu ở guard. Phiên không hợp lệ theo M01 bị từ chối, xem N2.

#### 4. Hậu điều kiện

<!-- sc:post SC-M16-015 -->

| result | condition |
|---|---|
| SUCCESS | Kết quả đường chính hoặc đúng biến thể thành công đã chọn. B Đã rời cutoff21:00, tổng 3→2, chỉ lịch sử trước cutoff cho B. A/C vẫn hoạt động, B không còn gửi/quản lý, mute riêng bị bỏ. Tổng1→0, A thành cựu, không tự xóa tin hoặc bổ nhiệm Admin mới. |
| REJECTED | Yêu cầu bị từ chối theo guard và trả kết quả cụ thể ở bước kết thúc E. Không có hiệu ứng thành công từ thao tác bị từ chối. Nhánh chọn người không hợp lệ khi tạo nhiều người giữ nguyên giới hạn GAP-SC-M16-001 về kết quả toàn thể. Bản ghi đã giải quyết giữ trạng thái đã có, hạn/mốc và tác vụ tự động độc lập tuân N1–N3. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M16-015 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-012 | Chọn rời nhóm chat G-ABC. | D15 A Admin, B/C Member, B tự rời21:00, trước tổng 3. | M2 | FR-M16-14.01, FR-M16-14.02, FR-M16-14.03, FR-M16-14.04, FR-M16-14.05, BR-M16-03, BR-M16-05, BR-M16-07, BR-M16-18, BR-M16-27, BR-M16-28, FR-M07-09.08 |
| M2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm caller current. B là Member nên cho rời, ghi Đã rời/cutoff21:00, giữ nhóm trong hộp thư B và quyền đọc tin trước cutoff. Nhóm còn 2 tiếp tục hoạt động, dữ liệu tin giữ lâu dài. Cung cấp M07 thay đổi tư cách để bỏ mute riêng nhóm, trả kết quả rời. B vào lại theo luồng thêm/link và công tắc hiện tại. | B Đã rời cutoff21:00, tổng 3→2, chỉ lịch sử trước cutoff cho B. A/C vẫn hoạt động, B không còn gửi/quản lý, mute riêng bị bỏ. | END:SUCCESS | FR-M16-14.01, FR-M16-14.02, FR-M16-14.03, FR-M16-14.04, FR-M16-14.05, BR-M16-03, BR-M16-05, BR-M16-07, BR-M16-18, BR-M16-27, BR-M16-28, FR-M07-09.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, các bước trước đó chỉ chạy một lần. E tại M1 thay toàn đường từ M1 khi actor/ngữ cảnh vai trò khác, mỗi hàng chỉ có một chủ thể. END đối chiếu hậu điều kiện mục 4, dữ liệu tại bước cuối mô tả kết quả của chính đường đó. Các giao nhau chưa có quyết định giữ GAP, không tạo kết thúc thành công giả.

<!-- sc:exceptions SC-M16-015 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Tài khoản người yêu cầu đang BANNED khi thao tác. | E1.1 | FR-M16-03.03, BR-M16-22, BR-M01-18 |
| E2 | system | M2 | Cờ Chat Tắt, người yêu cầu không ADMIN hệ thống, kể cả Admin nhóm chat. | E2.1 | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E3 | system | M1 | ACT-013 — A Admin nhóm chat muốn rời khi còn B/C và chưa chuyển quyền. | E3.1 | FR-M16-14.02, BR-M16-07, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E4 | system | M1 | ACT-013 — A là Admin và thành viên cuối cùng. | E4.1 | FR-M16-14.04, FR-M16-14.01, BR-M16-07, BR-M16-18, BR-M16-27, FR-M07-09.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| E5 | system | M1 | ACT-001 — Guest yêu cầu chức năng từ đầu khi cờ Bật. | E5.1 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E6 | system | M1 | ACT-007 — ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt. | E6.1 | FR-M16-14.01, FR-M16-14.02, FR-M16-14.03, FR-M16-14.04, FR-M16-14.05, BR-M16-03, BR-M16-05, BR-M16-07, BR-M16-18, BR-M16-27, BR-M16-28, FR-M07-09.08, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| E7 | system | M1 | ACT-002 — Người dùng ngoài cuộc, chưa từng là thành viên nhóm. | E7.1 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| E8 | system | M1 | ACT-014 — Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current. | E8.1 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |


<!-- sc:branch SC-M16-015 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | UC-M16-018 từ chối thao tác Chat và trả kết quả bị chặn. Tài khoản chỉ có quyền khiếu nại chính lệnh ban theo M09. | Yêu cầu hiện tại chưa được thực hiện, không có quyền Chat từ vai trò thành viên hoặc quản trị hệ thống. | END:REJECTED | FR-M16-03.03, BR-M16-22, BR-M01-18 |


<!-- sc:branch SC-M16-015 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | UC-M16-018 từ chối với thông báo “Hệ thống đang bận, vui lòng thử lại sau”. Giữ lối vào, biểu tượng/số chưa đọc M07 và nút Nhắn tin trên hồ sơ, giữ dữ liệu do thao tác này, bật lại không làm bù. Hạn thu hồi vẫn trôi, AUT-M16-001 vẫn xử lý trigger đã chốt. | Yêu cầu này bị từ chối. Không ghi thay đổi từ yêu cầu người dùng. Hiệu ứng AUT độc lập tuân nền N1. | END:REJECTED | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E3 — thay toàn bộ M1 đến kết thúc.** A Admin nhóm chat muốn rời khi còn B/C và chưa chuyển quyền.

<!-- sc:branch SC-M16-015 E3 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E3.1 | ACT-013 | Chọn rời G-ABC. | A còn Admin, nhóm3 người. | E3.2 | FR-M16-14.02 |
| E3.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Từ chối rời vì còn thành viên khác và chưa chuyển quyền. Trả kết quả chưa rời. A có thể chủ động yêu cầu chức năng chuyển quyền SC-M16-014, sau thành Member thì yêu cầu rời theo đường chính ở lần sau. | A còn Admin/current, tổng 3 và công tắc giữ nguyên. Không tự chuyển quyền trong thao tác rời. | END:REJECTED | FR-M16-14.02, BR-M16-07, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E4 — thay toàn bộ M1 đến kết thúc.** A là Admin và thành viên cuối cùng.

<!-- sc:branch SC-M16-015 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-013 | Chọn rời nhóm chỉ còn mình. | D15-last tổng 1, A Admin cuối, cutoff21:00. | E4.2 | FR-M16-14.04 |
| E4.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Cho rời không cần chuyển quyền, ghi Đã rời/cutoff, giữ hộp thư và lịch sử trước cutoff. Cung cấp M07 thay đổi tư cách, trả kết quả. Nhóm không còn người gửi được tin. Vòng đời link/nhóm0 người giữ GAP-SC-M16-006. | Tổng1→0, A thành cựu, không tự xóa tin hoặc bổ nhiệm Admin mới. | END:SUCCESS | FR-M16-14.01, FR-M16-14.04, BR-M16-07, BR-M16-18, BR-M16-27, FR-M07-09.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E5 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu chức năng từ đầu khi cờ Bật.

<!-- sc:branch SC-M16-015 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-001 | Chọn rời nhóm chat G-ABC. | Không có phiên đăng nhập, dữ liệu đích như đường chính. | E5.2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| E5.2 | SYSTEM | Từ chối yêu cầu Chat của Guest, trả kết quả không được thực hiện chức năng này. | Không cấp quyền thực hiện yêu cầu Chat hoặc xem lịch sử cho Guest. | END:REJECTED | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |


**E6 — thay toàn bộ M1 đến kết thúc.** ADMIN hệ thống ACTIVE, đã đủ membership/vai trò nhóm/sở hữu/giới hạn như đường chính, cờ Tắt.

<!-- sc:branch SC-M16-015 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-007 | Chọn rời nhóm chat G-ABC. | D15 A Admin, B/C Member, B tự rời21:00, trước tổng 3. Đường V này tài khoản khởi tạo là ADMIN hệ thống, có đủ tư cách cuộc/nhóm theo đường chính, cờ Tắt. | E6.2 | FR-M16-14.01, FR-M16-14.02, FR-M16-14.03, FR-M16-14.04, FR-M16-14.05, BR-M16-03, BR-M16-05, BR-M16-07, BR-M16-18, BR-M16-27, BR-M16-28, FR-M07-09.08, FR-M16-15.04, FR-M10-12.08 |
| E6.2 | SYSTEM | Kiểm phiên và trạng thái người gọi, cờ Chat và quyền theo thao tác trong UC-M16-018. Kiểm caller current. B là Member nên cho rời, ghi Đã rời/cutoff21:00, giữ nhóm trong hộp thư B và quyền đọc tin trước cutoff. Nhóm còn 2 tiếp tục hoạt động, dữ liệu tin giữ lâu dài. Cung cấp M07 thay đổi tư cách để bỏ mute riêng nhóm, trả kết quả rời. B vào lại theo luồng thêm/link và công tắc hiện tại. | B Đã rời cutoff21:00, tổng 3→2, chỉ lịch sử trước cutoff cho B. A/C vẫn hoạt động, B không còn gửi/quản lý, mute riêng bị bỏ. | END:SUCCESS | FR-M16-14.01, FR-M16-14.02, FR-M16-14.03, FR-M16-14.04, FR-M16-14.05, BR-M16-03, BR-M16-05, BR-M16-07, BR-M16-18, BR-M16-27, BR-M16-28, FR-M07-09.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |


**E7 — thay toàn bộ M1 đến kết thúc.** Người dùng ngoài cuộc, chưa từng là thành viên nhóm.

<!-- sc:branch SC-M16-015 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-002 | Chọn rời nhóm chat G-ABC. | Cờ Bật, phiên hợp lệ nhưng thiếu vai trò thành viên hiện tại. | E7.2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06 |
| E7.2 | SYSTEM | UC-M16-018 kiểm tư cách đúng cuộc/nhóm và từ chối yêu cầu vì thiếu quyền thành viên hiện tại. | Không đọc dữ liệu hoặc thay đổi trạng thái bằng yêu cầu trái quyền. | END:REJECTED | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |


**E8 — thay toàn bộ M1 đến kết thúc.** Cựu đã rời hoặc bị xóa yêu cầu thao tác cần tư cách current.

<!-- sc:branch SC-M16-015 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-014 | Chọn rời nhóm chat G-ABC. | Có cutoff rời, chưa gia nhập lại, cờ Bật. | E8.2 | FR-M16-04.10, BR-M16-27 |
| E8.2 | SYSTEM | Từ chối thao tác cần current membership. Cựu chỉ đọc lịch sử trước cutoff theo SC-M16-003/E13, vào lại qua SC-M16-007 hoặc SC-M16-009. | Nhóm/hộp thư/lịch sử trước cutoff của cựu được giữ, không có thay đổi từ thao tác trái quyền. | END:REJECTED | FR-M16-04.10, FR-M16-05.06, BR-M16-05, BR-M16-27, BR-M16-28 |


<!-- sc:end SC-M16-015 -->

## 5. Quy tắc nền và giao tiếp

| Mã | Trigger/điều kiện | Hiệu ứng | Điểm triển khai hoặc lý do nền | sources |
|---|---|---|---|---|
| N1 / AUT-M16-001 / UC-M16-020 / UC-M16-019 | Admin nhóm chat DELETED, ban vĩnh viễn đủ90×24giờ không khiếu nại hoặc khiếu nại chính ban bị bác | Để nhóm không Admin. Nếu duyệt Bật thì Tắt và FIFO chung hai loại người chờ tới 100, dư Đã từ chối. D11 98/5 cho2 vào, 3 từ chối. Cả khi Chat Tắt vẫn chạy. Nếu còn khôi phục được như DEACTIVATED trong14×24giờ, ban tạm, ban vĩnh viễn còn hạn hoặc đang chờ khiếu nại đúng hạn thì giữ Admin/cài đặt. Không tự chọn kế nhiệm. Nếu đã Tắt thì giữ Tắt, không phát sinh admission giả. | Tác vụ nền theo trạng thái, không có actor khởi tạo. Liên quan SC-M16-011/M2 và SC-M16-014/015 hậu điều kiện. Giao nhau chưa chốt nằm GAP001/004/006. | FR-M16-17.01, FR-M16-17.02, FR-M16-17.03, FR-M16-13.03, FR-M16-15.08, FR-M16-09.03, FR-M16-09.04, BR-M16-30, BR-M16-33, BR-M01-21, BR-M09-04, BR-M09-05 |
| N2 / RULE-M16-001 | Mỗi yêu cầu Chat hoặc phiên không còn hợp lệ | Guest từ chối, link yêu cầu đăng nhập. BANNED chặn mọi thao tác. DEACTIVATED/DELETED không có phiên hợp lệ theo M01. ADMIN qua cờ vẫn cần quyền và dữ liệu. Tác vụ tự động dùng điều kiện riêng. Khi cờ tắt giữ dữ liệu/lối vào, hạn vẫn trôi, bật lại không làm bù yêu cầu từ chối. | UC018 triển khai M2 mọi SC và M4 của bước gửi quyết định/xin. Mỗi SC có E cờ/BANNED, E tại M1 Guest/ADMIN, E tại M1 thiếu tư cách khi phù hợp. | FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| N3 / AUT-M16-002 / AUT-M16-003 / UC-M16-006 / UC-M16-007 | Ghi tin/thu hồi/mốc mới, tin tới khi hiển thị ở cuối, hiện lại cửa sổ hoặc cuộn xuống cuối | Tin/placeholder/receipt đến view được phép ngay. Ẩn hoặc đọc cũ hoãn mốc, hiện/ở cuối mới ghi. Một mốc không lùi, ứng viên38 và mốc 40 giữ40, ứng viên45 thành45. Receipt tin cuối theo từng viewer, tin thu hồi vẫn là tin cuối. M07 nhận sự kiện/membership/mốc/cuộc đang mở, đếm số cuộc chưa đọc kể cả mute. Không popup khi đang mở đúng cuộc, mute không làm mất tin hoặc thay số cuộc, không chuông/email. | SC-M16-001/E1.1, SC-M16-003/M2 và E, SC-M16-004/M2, SC-M16-005/M2. Giao nhau cựu/danh tính/stream giữ GAP001/003/005. | FR-M16-04.05, FR-M16-04.06, FR-M16-04.09, FR-M16-05.02, FR-M16-05.03, FR-M16-06.08, FR-M16-06.09, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08 |
| N4 / RULE-M16-002 | Tài khoản đích hoặc danh tính người gửi thay đổi | Không tạo1-1 mới/thêm nhóm người BANNED/DEACTIVATED/DELETED, tài khoản đó vẫn là thành viên nhóm đã có và tính vào cap. Cuộc1-1 cũ nhận tin tới ban/vô hiệu hóa, DELETED từ chối gửi. Danh tính tin theo M01/M02. Cựu giới hạn cutoff, vào lại có toàn lịch sử. | SC001/E1/E3, SC003/M2/E13, SC004/E5/E6, SC006/E4, SC007/E3/E5, SC009/E5. | BR-M16-24, BR-M16-25, BR-M16-26, BR-M16-27, FR-M16-01.07, FR-M16-04.07, FR-M16-04.11, FR-M16-04.12, FR-M16-05.13, FR-M16-05.14, FR-M16-08.08, FR-M16-08.09, FR-M16-16.08, FR-M01-13.06, FR-M01-13.07, FR-M02-01.26 |
| N5 / RULE-M16-003 | Hộp thư/lịch sử | 20 cuộc mỗi lần, 20 tin mỗi lần, không giới hạn tổng. Tin trước cutoff cho cựu.1-1 rỗng không hiện hộp thư, nhóm rỗng giữ GAP002. | SC002/M2/M4, SC003/M2/M4/M6/E13. | FR-M16-03, FR-M16-04, BR-M16-17, BR-M16-27, BR-M16-31 |
| N6 / RULE-M16-004 | Gửi/thu hồi | Văn bản/emoji, 1.000 từ, 30 tin/60 giây người/cuộc, thu hồi sender≤300 giây, gốc giữ và che mọi actor. Không sửa/xóa chỉ tôi/AI scan/report/Block/gọi thoại/video/ảnh/tệp ở MS1. | SC004/M2/E, SC005/M2/E, TBD-M16-01 giữ hoãn, TBD-M16-02 đã đóng DEC-248. | FR-M16-05, FR-M16-06, BR-M16-08, BR-M16-09, BR-M16-10, BR-M16-11, BR-M16-12, BR-M16-18, BR-M16-20 |
| N7 / RULE-M16-005 | Mốc/receipt và M07 | Mở/gửi/tin mới đúng điều kiện mới ghi, mốc không lùi. Sender và viewer bị loại khỏi avatar. A gửi50, mốc A/B/C50, D47 → A thấy B, C, C thấy B. Chỉ B ngoài sender đã đọc và B đang xem thì Đã xem dù avatar rỗng. | SC001/E1.1, SC003/M2 và E, SC004/M2, SC005/M2. Cựu/vào lại và identity receipt giữ GAP003/005. | FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08 |
| N8 / RULE-M16-006 | Tạo/thêm/link/duyệt | Tên trim1–100, tổng 3–100 khi tạo, một Admin, mặc định Tắt. Mọi current member lấy link chung không hết hạn, không thông báo được mời. Member thêm Bật tạo đề nghị, link Bật tạo yêu cầu. Duyệt tay full từ chối thao tác, bulk dư Đã từ chối. Join có pending từ chối gửi thêm, bị bác xin ngay lại được. | SC006–SC010, helper019 triển khai tại admission. Pending giao nhau giữ GAP004. | FR-M16-02, FR-M16-08, FR-M16-10, FR-M16-16, BR-M16-01, BR-M16-03, BR-M16-04, BR-M16-06, BR-M16-28, BR-M16-29, BR-M16-32 |
| N9 / RULE-M16-007 | Quyền nhóm/chuyển/rời/Admin không khôi phục | Chỉ Admin nhóm duyệt/công tắc/xóa/chuyển. Current đều thêm/lấy link/đổi tên/rời đúng điều kiện. Admin còn người khác phải chủ động chuyển trước khi rời. Admin cuối rời được. Nhóm dưới 3 tiếp tục, không tự kế nhiệm. | SC011–SC015 và N1, vòng đời0/người nhận quyền không khôi phục giữ GAP006. | FR-M16-11, FR-M16-12, FR-M16-13, FR-M16-14, FR-M16-17, BR-M16-04, BR-M16-05, BR-M16-07, BR-M16-27, BR-M16-30 |
| N10 / RULE-M16-008 | Admin hoặc AUT001 tắt duyệt | UC020 dùng FIFO chung hai loại, admission mỗi người qua019 tới 100, dư Đã từ chối.50/5→55, 98/5→100. Tài khoản đổi trạng thái/pending trùng/timestamp bằng nhau giữ GAP004. | SC011/M2/E2/E3/E4 và N1, không tạo BF SYSTEM-only. | FR-M16-09.03, FR-M16-09.04, FR-M16-10.07, FR-M16-17.02, BR-M16-30, BR-M16-33 |


## 6. Truy vết nguồn và quyết định bao phủ

Có vị trí truy vết cho 177 mã hiệu lực gồm 17 nhóm FR, 127 FR chi tiết và33 BR. Truy vết có vị trí không đồng nghĩa các trường hợp biên trong GAP đã có hợp đồng đủ. FR17 là tác vụ theo trạng thái nằm ở N1, không ép actor khởi tạo một scenario.

| FR/BR | Nội dung nguồn hoặc loại BR | BF | SC/bước hoặc quy tắc nền | Mức bao phủ | Nền liên quan |
|---|---|---|---|---|---|
| FR-M16-01 | Bắt đầu trò chuyện 1-1 | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E1.1, SC-M16-001/E2.1, SC-M16-001/E3.1, SC-M16-001/E6.1, SC-M16-001/E6.2, SC-M16-001/E7.1, SC-M16-001/E7.2, SC-M16-002/E6.1, SC-M16-002/E6.2, SC-M16-003/E14.1, SC-M16-003/E14.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E11.1, SC-M16-004/E11.2, SC-M16-004/E12.1, SC-M16-004/E12.2, SC-M16-005/E8.1, SC-M16-005/E8.2, SC-M16-006/E8.1, SC-M16-006/E8.2, SC-M16-007/E9.1, SC-M16-007/E9.2, SC-M16-008/E3.1, SC-M16-008/E3.2, SC-M16-009/E10.1, SC-M16-009/E10.2, SC-M16-010/E8.1, SC-M16-010/E8.2, SC-M16-011/E7.1, SC-M16-011/E7.2, SC-M16-012/E3.1, SC-M16-012/E3.2, SC-M16-013/E5.1, SC-M16-013/E5.2, SC-M16-014/E4.1, SC-M16-014/E4.2, SC-M16-015/E5.1, SC-M16-015/E5.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-02 | Tạo nhóm chat | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/E6.1, SC-M16-001/E6.2, SC-M16-002/E6.1, SC-M16-002/E6.2, SC-M16-003/E14.1, SC-M16-003/E14.2, SC-M16-004/E11.1, SC-M16-004/E11.2, SC-M16-005/E8.1, SC-M16-005/E8.2, SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E1.1, SC-M16-006/E2.1, SC-M16-006/E3.1, SC-M16-006/E4.1, SC-M16-006/E5.1, SC-M16-006/E8.1, SC-M16-006/E8.2, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E9.1, SC-M16-007/E9.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-008/E3.1, SC-M16-008/E3.2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E10.1, SC-M16-009/E10.2, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E8.1, SC-M16-010/E8.2, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E7.1, SC-M16-011/E7.2, SC-M16-011/E8.1, SC-M16-011/E8.2, SC-M16-012/E3.1, SC-M16-012/E3.2, SC-M16-013/E5.1, SC-M16-013/E5.2, SC-M16-014/E4.1, SC-M16-014/E4.2, SC-M16-015/E5.1, SC-M16-015/E5.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N8 |
| FR-M16-03 | Xem hộp thư Chat | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E4.1, SC-M16-001/E5.1, SC-M16-001/E6.1, SC-M16-001/E6.2, SC-M16-001/E7.1, SC-M16-001/E7.2, SC-M16-002/M1, SC-M16-002/M2, SC-M16-002/M3, SC-M16-002/M4, SC-M16-002/E1.1, SC-M16-002/E2.1, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E5.1, SC-M16-002/E6.1, SC-M16-002/E6.2, SC-M16-002/E7.1, SC-M16-002/E7.2, SC-M16-002/E7.3, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E7.1, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E10.1, SC-M16-003/E11.1, SC-M16-003/E12.1, SC-M16-003/E14.1, SC-M16-003/E14.2, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.6, SC-M16-004/M2, SC-M16-004/E9.1, SC-M16-004/E10.1, SC-M16-004/E11.1, SC-M16-004/E11.2, SC-M16-004/E12.2, SC-M16-005/M2, SC-M16-005/E6.1, SC-M16-005/E7.1, SC-M16-005/E8.1, SC-M16-005/E8.2, SC-M16-005/E9.2, SC-M16-006/M2, SC-M16-006/E6.1, SC-M16-006/E7.1, SC-M16-006/E8.1, SC-M16-006/E8.2, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E6.1, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E9.1, SC-M16-007/E9.2, SC-M16-007/E10.2, SC-M16-008/M2, SC-M16-008/E1.1, SC-M16-008/E2.1, SC-M16-008/E3.1, SC-M16-008/E3.2, SC-M16-008/E4.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E6.1, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E9.1, SC-M16-009/E10.1, SC-M16-009/E10.2, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E4.1, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E7.1, SC-M16-010/E8.1, SC-M16-010/E8.2, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E5.1, SC-M16-011/E6.1, SC-M16-011/E7.1, SC-M16-011/E7.2, SC-M16-011/E8.2, SC-M16-012/M2, SC-M16-012/E1.1, SC-M16-012/E2.1, SC-M16-012/E3.1, SC-M16-012/E3.2, SC-M16-012/E4.2, SC-M16-013/M2, SC-M16-013/E3.1, SC-M16-013/E4.1, SC-M16-013/E5.1, SC-M16-013/E5.2, SC-M16-013/E6.2, SC-M16-014/M2, SC-M16-014/E2.1, SC-M16-014/E3.1, SC-M16-014/E4.1, SC-M16-014/E4.2, SC-M16-014/E5.2, SC-M16-015/M2, SC-M16-015/E1.1, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E5.1, SC-M16-015/E5.2, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N5 |
| FR-M16-04 | Xem cuộc trò chuyện và lịch sử tin nhắn | BF-M16-001, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E1.1, SC-M16-001/E7.1, SC-M16-001/E7.2, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/M3, SC-M16-003/M4, SC-M16-003/M5, SC-M16-003/M6, SC-M16-003/E1.1, SC-M16-003/E2.1, SC-M16-003/E3.2, SC-M16-003/E4.1, SC-M16-003/E4.4, SC-M16-003/E5.1, SC-M16-003/E6.1, SC-M16-003/E13.1, SC-M16-003/E13.2, SC-M16-003/E13.3, SC-M16-003/E13.4, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-003/E15.3, SC-M16-003/E15.4, SC-M16-003/E15.5, SC-M16-003/E15.6, SC-M16-003/E16.1, SC-M16-003/E16.2, SC-M16-003/E17.1, SC-M16-003/E17.2, SC-M16-003/E18.1, SC-M16-003/E18.2, SC-M16-004/E13.1, SC-M16-004/E13.2, SC-M16-004/E14.1, SC-M16-004/E14.2, SC-M16-004/E15.1, SC-M16-004/E15.2, SC-M16-004/E16.1, SC-M16-004/E16.2, SC-M16-005/E10.1, SC-M16-005/E10.2, SC-M16-005/E11.1, SC-M16-005/E11.2, SC-M16-007/E11.1, SC-M16-007/E11.2, SC-M16-007/E12.1, SC-M16-007/E12.2, SC-M16-008/E5.1, SC-M16-008/E5.2, SC-M16-008/E6.1, SC-M16-008/E6.2, SC-M16-010/E10.1, SC-M16-010/E10.2, SC-M16-010/E11.1, SC-M16-010/E11.2, SC-M16-011/E9.1, SC-M16-011/E9.2, SC-M16-011/E10.1, SC-M16-011/E10.2, SC-M16-012/E5.1, SC-M16-012/E5.2, SC-M16-012/E6.1, SC-M16-012/E6.2, SC-M16-013/E7.1, SC-M16-013/E7.2, SC-M16-013/E8.1, SC-M16-013/E8.2, SC-M16-014/E6.1, SC-M16-014/E6.2, SC-M16-014/E7.1, SC-M16-014/E7.2, SC-M16-015/E7.1, SC-M16-015/E7.2, SC-M16-015/E8.1, SC-M16-015/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N5 |
| FR-M16-05 | Gửi tin nhắn | BF-M16-001, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/E1.1, SC-M16-003/E16.1, SC-M16-003/E16.2, SC-M16-003/E17.1, SC-M16-003/E17.2, SC-M16-003/E18.1, SC-M16-003/E18.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E1.1, SC-M16-004/E2.1, SC-M16-004/E3.1, SC-M16-004/E4.1, SC-M16-004/E5.1, SC-M16-004/E6.1, SC-M16-004/E7.1, SC-M16-004/E8.1, SC-M16-004/E12.1, SC-M16-004/E12.2, SC-M16-004/E13.1, SC-M16-004/E13.2, SC-M16-004/E14.2, SC-M16-004/E15.1, SC-M16-004/E15.2, SC-M16-004/E16.1, SC-M16-004/E16.2, SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E9.1, SC-M16-005/E9.2, SC-M16-005/E10.1, SC-M16-005/E10.2, SC-M16-005/E11.2, SC-M16-007/E11.1, SC-M16-007/E11.2, SC-M16-007/E12.2, SC-M16-008/E5.1, SC-M16-008/E5.2, SC-M16-008/E6.2, SC-M16-010/E10.1, SC-M16-010/E10.2, SC-M16-010/E11.2, SC-M16-011/E9.1, SC-M16-011/E9.2, SC-M16-011/E10.2, SC-M16-012/E5.1, SC-M16-012/E5.2, SC-M16-012/E6.2, SC-M16-013/E7.1, SC-M16-013/E7.2, SC-M16-013/E8.2, SC-M16-014/E6.1, SC-M16-014/E6.2, SC-M16-014/E7.2, SC-M16-015/E7.1, SC-M16-015/E7.2, SC-M16-015/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N6 |
| FR-M16-06 | Thu hồi tin nhắn | BF-M16-001, BF-M16-003, BF-M16-004, BF-M16-005 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E5.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2, SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E1.1, SC-M16-005/E2.1, SC-M16-005/E3.1, SC-M16-005/E4.1, SC-M16-005/E5.1, SC-M16-005/E5.2, SC-M16-005/E9.1, SC-M16-005/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N6 |
| FR-M16-07 | Ghi nhận đã đọc và hiển thị Đã xem | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005 | SC-M16-001/E1.1, SC-M16-002/M1, SC-M16-002/M2, SC-M16-002/E7.1, SC-M16-002/E7.2, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/E2.1, SC-M16-003/E2.2, SC-M16-003/E2.3, SC-M16-003/E3.1, SC-M16-003/E3.2, SC-M16-003/E3.3, SC-M16-003/E3.4, SC-M16-003/E4.1, SC-M16-003/E4.2, SC-M16-003/E4.3, SC-M16-003/E4.4, SC-M16-003/E5.1, SC-M16-003/E6.1, SC-M16-003/E13.2, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E6.1, SC-M16-004/E7.1, SC-M16-004/E8.1, SC-M16-004/E12.1, SC-M16-004/E12.2, SC-M16-005/E5.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-08 | Thêm, mời thành viên vào nhóm chat | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/E16.2, SC-M16-004/E13.2, SC-M16-005/E10.2, SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E1.1, SC-M16-007/E2.1, SC-M16-007/E3.1, SC-M16-007/E4.1, SC-M16-007/E5.1, SC-M16-007/E8.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-007/E11.2, SC-M16-008/M1, SC-M16-008/M2, SC-M16-008/E4.1, SC-M16-008/E4.2, SC-M16-008/E5.2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E9.4, SC-M16-010/E10.2, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2, SC-M16-011/E9.2, SC-M16-012/E5.2, SC-M16-013/E7.2, SC-M16-014/E6.2, SC-M16-015/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N8 |
| FR-M16-09 | Bật, tắt duyệt thành viên mới | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/E16.2, SC-M16-004/E13.2, SC-M16-005/E10.2, SC-M16-007/E11.2, SC-M16-008/E5.2, SC-M16-010/E10.2, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E1.1, SC-M16-011/E1.2, SC-M16-011/E2.1, SC-M16-011/E3.1, SC-M16-011/E4.1, SC-M16-011/E8.1, SC-M16-011/E8.2, SC-M16-011/E9.2, SC-M16-012/E5.2, SC-M16-013/E7.2, SC-M16-014/E6.2, SC-M16-015/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-10 | Duyệt người chờ vào nhóm chat | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/E16.2, SC-M16-004/E13.2, SC-M16-005/E10.2, SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E1.1, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-007/E11.2, SC-M16-008/E5.2, SC-M16-009/M4, SC-M16-009/E1.1, SC-M16-009/E5.1, SC-M16-009/E9.1, SC-M16-009/E11.4, SC-M16-010/M1, SC-M16-010/M2, SC-M16-010/M3, SC-M16-010/M4, SC-M16-010/E1.1, SC-M16-010/E1.2, SC-M16-010/E2.1, SC-M16-010/E3.1, SC-M16-010/E7.1, SC-M16-010/E9.1, SC-M16-010/E9.2, SC-M16-010/E9.3, SC-M16-010/E9.4, SC-M16-010/E10.2, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2, SC-M16-011/E9.2, SC-M16-012/E5.2, SC-M16-013/E7.2, SC-M16-014/E6.2, SC-M16-015/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N8 |
| FR-M16-11 | Xóa thành viên khỏi nhóm chat | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/E16.2, SC-M16-004/E13.2, SC-M16-005/E10.2, SC-M16-007/E11.2, SC-M16-008/E5.2, SC-M16-010/E10.2, SC-M16-011/E9.2, SC-M16-012/M1, SC-M16-012/M2, SC-M16-012/E4.1, SC-M16-012/E4.2, SC-M16-012/E5.2, SC-M16-013/E7.2, SC-M16-014/E6.2, SC-M16-015/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N9 |
| FR-M16-12 | Đổi tên nhóm chat | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/E16.2, SC-M16-004/E13.2, SC-M16-005/E10.2, SC-M16-007/E11.2, SC-M16-008/E5.2, SC-M16-010/E10.2, SC-M16-011/E9.2, SC-M16-012/E5.2, SC-M16-013/M1, SC-M16-013/M2, SC-M16-013/E1.1, SC-M16-013/E2.1, SC-M16-013/E6.1, SC-M16-013/E6.2, SC-M16-013/E7.2, SC-M16-014/E6.2, SC-M16-015/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N9 |
| FR-M16-13 | Chuyển quyền Admin nhóm chat | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/E16.2, SC-M16-004/E13.2, SC-M16-005/E10.2, SC-M16-007/E11.2, SC-M16-008/E5.2, SC-M16-010/E10.2, SC-M16-011/E9.2, SC-M16-012/E5.2, SC-M16-013/E7.2, SC-M16-014/M1, SC-M16-014/M2, SC-M16-014/E1.1, SC-M16-014/E5.1, SC-M16-014/E5.2, SC-M16-014/E6.2, SC-M16-015/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N9 |
| FR-M16-14 | Rời nhóm chat | BF-M16-012, BF-M16-014, BF-M16-015 | SC-M16-012/M1, SC-M16-012/M2, SC-M16-012/E4.1, SC-M16-012/E4.2, SC-M16-014/M1, SC-M16-014/M2, SC-M16-014/E5.1, SC-M16-014/E5.2, SC-M16-015/M1, SC-M16-015/M2, SC-M16-015/E3.1, SC-M16-015/E3.2, SC-M16-015/E4.1, SC-M16-015/E4.2, SC-M16-015/E6.1, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N9 |
| FR-M16-15 | Chặn thao tác Chat khi cờ tính năng tắt | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M2, SC-M16-001/E5.1, SC-M16-001/E7.1, SC-M16-001/E7.2, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E7.1, SC-M16-002/E7.2, SC-M16-002/E7.3, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E11.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-003/E15.3, SC-M16-003/E15.4, SC-M16-003/E15.5, SC-M16-003/E15.6, SC-M16-003/E17.2, SC-M16-003/E18.2, SC-M16-004/M2, SC-M16-004/E10.1, SC-M16-004/E12.1, SC-M16-004/E12.2, SC-M16-004/E15.2, SC-M16-004/E16.2, SC-M16-005/M2, SC-M16-005/E2.1, SC-M16-005/E7.1, SC-M16-005/E9.1, SC-M16-005/E9.2, SC-M16-006/M2, SC-M16-006/E7.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-008/M2, SC-M16-008/E2.1, SC-M16-008/E4.1, SC-M16-008/E4.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E11.1, SC-M16-009/E11.2, SC-M16-009/E11.3, SC-M16-009/E11.4, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E9.1, SC-M16-010/E9.2, SC-M16-010/E9.3, SC-M16-010/E9.4, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E6.1, SC-M16-011/E8.1, SC-M16-011/E8.2, SC-M16-012/M2, SC-M16-012/E2.1, SC-M16-012/E4.1, SC-M16-012/E4.2, SC-M16-013/M2, SC-M16-013/E4.1, SC-M16-013/E6.1, SC-M16-013/E6.2, SC-M16-014/M2, SC-M16-014/E3.1, SC-M16-014/E5.1, SC-M16-014/E5.2, SC-M16-015/M2, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E6.1, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-16 | Xin gia nhập nhóm chat qua link mời | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/E6.1, SC-M16-001/E6.2, SC-M16-002/E6.1, SC-M16-002/E6.2, SC-M16-003/E14.1, SC-M16-003/E14.2, SC-M16-004/E11.1, SC-M16-004/E11.2, SC-M16-005/E8.1, SC-M16-005/E8.2, SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E8.1, SC-M16-006/E8.2, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E9.1, SC-M16-007/E9.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-008/E3.1, SC-M16-008/E3.2, SC-M16-009/M1, SC-M16-009/M2, SC-M16-009/M3, SC-M16-009/M4, SC-M16-009/E1.1, SC-M16-009/E2.1, SC-M16-009/E3.1, SC-M16-009/E4.1, SC-M16-009/E5.1, SC-M16-009/E10.1, SC-M16-009/E10.2, SC-M16-009/E11.1, SC-M16-009/E11.2, SC-M16-009/E11.3, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E8.1, SC-M16-010/E8.2, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E2.1, SC-M16-011/E7.1, SC-M16-011/E7.2, SC-M16-011/E8.1, SC-M16-011/E8.2, SC-M16-012/E3.1, SC-M16-012/E3.2, SC-M16-013/E5.1, SC-M16-013/E5.2, SC-M16-014/E4.1, SC-M16-014/E4.2, SC-M16-015/E5.1, SC-M16-015/E5.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N8 |
| FR-M16-17 | Tự tắt duyệt khi Admin nhóm chat không thể khôi phục | Nền theo trigger | N9 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N9 |
| FR-M16-01.01 | Khi người dùng đã đăng nhập chọn nhắn tin cho một người dùng khác, hệ thống phải cho bắt đầu trò chuyện 1-1 với người đó mà không yêu cầu hai người theo dõi nhau (BR-M16-02). | BF-M16-001 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E7.1, SC-M16-001/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-01.02 | Khi người dùng gửi tin đầu tiên trong trò chuyện 1-1, hệ thống phải giao tin tới người nhận mà không chờ người nhận chấp nhận (BR-M16-02). | BF-M16-001, BF-M16-004 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E7.1, SC-M16-001/E7.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-01.03 | Nếu Guest chọn nhắn tin cho một người dùng, hệ thống phải từ chối (BR-M16-02). | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E6.1, SC-M16-001/E6.2, SC-M16-001/E7.1, SC-M16-001/E7.2, SC-M16-002/E6.1, SC-M16-002/E6.2, SC-M16-003/E14.1, SC-M16-003/E14.2, SC-M16-004/E11.1, SC-M16-004/E11.2, SC-M16-005/E8.1, SC-M16-005/E8.2, SC-M16-006/E8.1, SC-M16-006/E8.2, SC-M16-007/E9.1, SC-M16-007/E9.2, SC-M16-008/E3.1, SC-M16-008/E3.2, SC-M16-009/E10.1, SC-M16-009/E10.2, SC-M16-010/E8.1, SC-M16-010/E8.2, SC-M16-011/E7.1, SC-M16-011/E7.2, SC-M16-012/E3.1, SC-M16-012/E3.2, SC-M16-013/E5.1, SC-M16-013/E5.2, SC-M16-014/E4.1, SC-M16-014/E4.2, SC-M16-015/E5.1, SC-M16-015/E5.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-01.04 | Khi một trò chuyện 1-1 được bắt đầu, hệ thống phải đặt đúng hai người dùng làm thành viên của cuộc (BR-M16-01). | BF-M16-001 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E7.1, SC-M16-001/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-01.05 | Khi người dùng chọn nhắn tin cho người đã có trò chuyện 1-1 với mình, hệ thống phải mở cuộc đã có với toàn bộ lịch sử thay vì tạo cuộc mới (BR-M16-24). | BF-M16-001 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E1.1, SC-M16-001/E7.1, SC-M16-001/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-01.06 | Nếu người dùng chọn nhắn tin cho chính mình, hệ thống phải từ chối (BR-M16-24). | BF-M16-001 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E2.1, SC-M16-001/E7.1, SC-M16-001/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-01.07 | Nếu người dùng chọn nhắn tin cho một tài khoản đang bị ban, đang vô hiệu hóa hoặc đã xóa mà hai người chưa có trò chuyện 1-1, hệ thống phải từ chối bắt đầu cuộc mới (BR-M16-25). | BF-M16-001 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E3.1, SC-M16-001/E7.1, SC-M16-001/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N4 |
| FR-M16-02.01 | Khi người dùng đã đăng nhập tạo nhóm chat và chọn các người dùng khác, hệ thống phải tạo nhóm chat gồm người tạo và những người được chọn (BR-M16-01). | BF-M16-006 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-02.02 | Khi tạo nhóm chat, hệ thống phải đặt người tạo làm Admin nhóm chat và những người được chọn làm Member (BR-M16-04). | BF-M16-006, BF-M16-007, BF-M16-009, BF-M16-010, BF-M16-011 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-02.03 | Hệ thống phải cho chọn thành viên nhóm chat mà không đòi họ theo dõi người tạo hay cùng thuộc một Group nào (BR-M16-01). | BF-M16-006 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E9.1, SC-M16-006/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-02.04 | Nếu tổng số thành viên, gồm cả người tạo, ít hơn 3, hệ thống phải từ chối tạo nhóm chat (BR-M16-03). | BF-M16-006 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E2.1, SC-M16-006/E9.1, SC-M16-006/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-02.05 | Nếu tổng số thành viên, gồm cả người tạo, nhiều hơn 100, hệ thống phải từ chối tạo nhóm chat (BR-M16-03). | BF-M16-006 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E3.1, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-02.06 | Nếu Guest chọn tạo nhóm chat, hệ thống phải từ chối (BR-M16-02). | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/E6.1, SC-M16-001/E6.2, SC-M16-002/E6.1, SC-M16-002/E6.2, SC-M16-003/E14.1, SC-M16-003/E14.2, SC-M16-004/E11.1, SC-M16-004/E11.2, SC-M16-005/E8.1, SC-M16-005/E8.2, SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E8.1, SC-M16-006/E8.2, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/E9.1, SC-M16-007/E9.2, SC-M16-008/E3.1, SC-M16-008/E3.2, SC-M16-009/E10.1, SC-M16-009/E10.2, SC-M16-010/E8.1, SC-M16-010/E8.2, SC-M16-011/E7.1, SC-M16-011/E7.2, SC-M16-012/E3.1, SC-M16-012/E3.2, SC-M16-013/E5.1, SC-M16-013/E5.2, SC-M16-014/E4.1, SC-M16-014/E4.2, SC-M16-015/E5.1, SC-M16-015/E5.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-02.07 | Nếu tên nhóm chat trống hoặc dài hơn 100 ký tự sau khi bỏ khoảng trắng đầu và cuối, hệ thống phải từ chối tạo nhóm chat (BR-M16-32). | BF-M16-006 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E1.1, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-02.08 | Khi tạo nhóm chat, hệ thống phải đặt công tắc duyệt thành viên mới ở trạng thái Tắt (BR-M16-06). | BF-M16-006 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-02.09 | Nếu người được chọn đang bị ban, đang vô hiệu hóa hoặc đã xóa, hệ thống phải từ chối đưa người đó vào nhóm chat (BR-M16-25). | BF-M16-006 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E4.1, SC-M16-006/E9.1, SC-M16-006/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-03.01 | Khi người dùng đã đăng nhập mở hộp thư Chat, hệ thống phải liệt kê các cuộc trò chuyện mà người đó là thành viên hoặc thành viên cũ, không liệt kê cuộc của người khác (BR-M16-31). | BF-M16-002 | SC-M16-002/M1, SC-M16-002/M2, SC-M16-002/E1.1, SC-M16-002/E7.1, SC-M16-002/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-03.02 | Nếu Guest mở hộp thư Chat, hệ thống phải từ chối (BR-M16-02). | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/E6.1, SC-M16-001/E6.2, SC-M16-002/M1, SC-M16-002/M2, SC-M16-002/E6.1, SC-M16-002/E6.2, SC-M16-002/E7.1, SC-M16-002/E7.2, SC-M16-003/E14.1, SC-M16-003/E14.2, SC-M16-004/E11.1, SC-M16-004/E11.2, SC-M16-005/E8.1, SC-M16-005/E8.2, SC-M16-006/E8.1, SC-M16-006/E8.2, SC-M16-007/E9.1, SC-M16-007/E9.2, SC-M16-008/E3.1, SC-M16-008/E3.2, SC-M16-009/E10.1, SC-M16-009/E10.2, SC-M16-010/E8.1, SC-M16-010/E8.2, SC-M16-011/E7.1, SC-M16-011/E7.2, SC-M16-012/E3.1, SC-M16-012/E3.2, SC-M16-013/E5.1, SC-M16-013/E5.2, SC-M16-014/E4.1, SC-M16-014/E4.2, SC-M16-015/E5.1, SC-M16-015/E5.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-03.03 | Nếu tài khoản đang bị ban thao tác bất kỳ với Chat, kể cả mở hộp thư, hệ thống phải từ chối (BR-M16-22). | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M2, SC-M16-001/E4.1, SC-M16-001/E5.1, SC-M16-001/E7.2, SC-M16-002/M1, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E2.1, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E5.1, SC-M16-002/E7.1, SC-M16-002/E7.2, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E7.1, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E10.1, SC-M16-003/E11.1, SC-M16-003/E12.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.6, SC-M16-004/M2, SC-M16-004/E9.1, SC-M16-004/E10.1, SC-M16-004/E12.2, SC-M16-005/M2, SC-M16-005/E6.1, SC-M16-005/E7.1, SC-M16-005/E9.2, SC-M16-006/M2, SC-M16-006/E6.1, SC-M16-006/E7.1, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E6.1, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E10.2, SC-M16-008/M2, SC-M16-008/E1.1, SC-M16-008/E2.1, SC-M16-008/E4.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E6.1, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E9.1, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E4.1, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E7.1, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E5.1, SC-M16-011/E6.1, SC-M16-011/E8.2, SC-M16-012/M2, SC-M16-012/E1.1, SC-M16-012/E2.1, SC-M16-012/E4.2, SC-M16-013/M2, SC-M16-013/E3.1, SC-M16-013/E4.1, SC-M16-013/E6.2, SC-M16-014/M2, SC-M16-014/E2.1, SC-M16-014/E3.1, SC-M16-014/E5.2, SC-M16-015/M2, SC-M16-015/E1.1, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N2 |
| FR-M16-03.04 | Hệ thống phải xếp các cuộc trong hộp thư theo thời điểm gửi của tin nhắn mới nhất, mới nhất trước; với nhóm chat mình là thành viên cũ thì theo tin cuối cùng mình còn thấy (BR-M16-31). | BF-M16-002 | SC-M16-002/M1, SC-M16-002/M2, SC-M16-002/E7.1, SC-M16-002/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-03.05 | Hệ thống phải hiển thị ở mỗi dòng: tên nhóm chat, hoặc display_name và avatar của người kia với trò chuyện 1-1; nội dung tin mới nhất ("Tin nhắn đã bị thu hồi" nếu tin đó đã thu hồi); thời điểm gửi của tin đó (BR-M16-31). | BF-M16-002 | SC-M16-002/M1, SC-M16-002/M2, SC-M16-002/E7.1, SC-M16-002/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-03.06 | Hệ thống phải đánh dấu chưa đọc cuộc có tin nhắn mới hơn mốc đã đọc của người xem trong số tin người đó thấy được (thành viên cũ: tin gửi trước thời điểm rời), theo cùng cách đếm với biểu tượng Tin nhắn (BR-M16-31). | BF-M16-002 | SC-M16-002/M1, SC-M16-002/M2, SC-M16-002/E7.1, SC-M16-002/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-03.07 | Hệ thống phải không đưa vào hộp thư trò chuyện 1-1 chưa có tin nhắn nào (BR-M16-31). | BF-M16-001, BF-M16-002 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E7.1, SC-M16-001/E7.2, SC-M16-002/M1, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E1.1, SC-M16-002/E7.1, SC-M16-002/E7.2, SC-M16-002/E7.4 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-03.08 | Hệ thống phải tải hộp thư 20 cuộc mỗi lần, cuộn xuống tải tiếp, không giới hạn tổng số cuộc (BR-M16-31). | BF-M16-002 | SC-M16-002/M1, SC-M16-002/M2, SC-M16-002/M3, SC-M16-002/M4, SC-M16-002/E7.1, SC-M16-002/E7.2, SC-M16-002/E7.3, SC-M16-002/E7.4 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-04.01 | Khi thành viên mở một cuộc trò chuyện, hệ thống phải hiển thị 20 tin nhắn mới nhất của cuộc (BR-M16-17). | BF-M16-001, BF-M16-003 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E1.1, SC-M16-001/E7.1, SC-M16-001/E7.2, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/M6, SC-M16-003/E1.1, SC-M16-003/E6.1, SC-M16-003/E13.2, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-003/E15.6 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-04.02 | Khi thành viên cuộn lên tới tin cũ nhất đang hiển thị, hệ thống phải tải thêm 20 tin cũ hơn kế tiếp (BR-M16-17). | BF-M16-003 | SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/M3, SC-M16-003/M4, SC-M16-003/M5, SC-M16-003/M6, SC-M16-003/E13.3, SC-M16-003/E13.4, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-003/E15.3, SC-M16-003/E15.4, SC-M16-003/E15.5, SC-M16-003/E15.6 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-04.03 | Hệ thống phải cho thành viên tải tiếp cho tới tin đầu tiên của cuộc, không giới hạn tổng số tin, kể cả với thành viên mới vào hoặc vào lại nhóm chat (BR-M16-17, BR-M16-27). | BF-M16-003 | SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M5, SC-M16-003/M6, SC-M16-003/E1.1, SC-M16-003/E13.4, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.5, SC-M16-003/E15.6 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-04.04 | Hệ thống phải hiển thị với mỗi tin nhắn: người gửi, nội dung và thời điểm gửi theo giờ Việt Nam. | BF-M16-001, BF-M16-003 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E15.1, SC-M16-003/E15.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-04.05 | Trong khi thành viên đang mở cuộc trò chuyện, hệ thống phải hiển thị tin nhắn mới của cuộc ngay khi có, không cần tải lại trang (BR-M16-16). | BF-M16-003 | SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/M6, SC-M16-003/E2.1, SC-M16-003/E3.2, SC-M16-003/E5.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-003/E15.6 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3 |
| FR-M16-04.06 | Nếu có tin mới tới trong lúc thành viên đang cuộn lên đọc tin cũ, hệ thống phải giữ nguyên vị trí đang đọc và hiện nhãn "tin nhắn mới" (BR-M16-14). | BF-M16-003 | SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/M6, SC-M16-003/E2.1, SC-M16-003/E4.1, SC-M16-003/E4.4, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-003/E15.6 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3 |
| FR-M16-04.07 | Hệ thống phải hiển thị tin nhắn của tài khoản đã xóa với nội dung giữ nguyên và người gửi "[Người dùng đã xóa]" (BR-M16-19). | BF-M16-001, BF-M16-003 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E15.1, SC-M16-003/E15.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N4 |
| FR-M16-04.08 | Nếu người không là thành viên và không là thành viên cũ của cuộc trò chuyện, kể cả Guest, Mod và Admin, mở cuộc đó, hệ thống phải từ chối. | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-003/E16.1, SC-M16-003/E16.2, SC-M16-003/E17.1, SC-M16-003/E17.2, SC-M16-003/E18.1, SC-M16-003/E18.2, SC-M16-004/E13.1, SC-M16-004/E13.2, SC-M16-004/E15.1, SC-M16-004/E15.2, SC-M16-004/E16.1, SC-M16-004/E16.2, SC-M16-005/E10.1, SC-M16-005/E10.2, SC-M16-007/E11.1, SC-M16-007/E11.2, SC-M16-008/E5.1, SC-M16-008/E5.2, SC-M16-010/E10.1, SC-M16-010/E10.2, SC-M16-011/E9.1, SC-M16-011/E9.2, SC-M16-012/E5.1, SC-M16-012/E5.2, SC-M16-013/E7.1, SC-M16-013/E7.2, SC-M16-014/E6.1, SC-M16-014/E6.2, SC-M16-015/E7.1, SC-M16-015/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-04.09 | Hệ thống phải cung cấp cho M07 cuộc trò chuyện mà mỗi người dùng đang mở, để M07 không hiện popup tin mới của chính cuộc đó. | BF-M16-001, BF-M16-003 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E1.1, SC-M16-003/E2.1, SC-M16-003/E15.1, SC-M16-003/E15.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3 |
| FR-M16-04.10 | Khi thành viên cũ mở nhóm chat mình đã rời hoặc bị xóa, hệ thống phải chỉ hiển thị các tin gửi trước thời điểm rời của người đó, chỉ để đọc (BR-M16-27). | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E13.1, SC-M16-003/E13.2, SC-M16-003/E13.3, SC-M16-003/E13.4, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/E14.1, SC-M16-004/E14.2, SC-M16-005/E11.1, SC-M16-005/E11.2, SC-M16-007/E12.1, SC-M16-007/E12.2, SC-M16-008/E6.1, SC-M16-008/E6.2, SC-M16-010/E11.1, SC-M16-010/E11.2, SC-M16-011/E10.1, SC-M16-011/E10.2, SC-M16-012/E6.1, SC-M16-012/E6.2, SC-M16-013/E8.1, SC-M16-013/E8.2, SC-M16-014/E7.1, SC-M16-014/E7.2, SC-M16-015/E8.1, SC-M16-015/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-04.11 | Hệ thống phải hiển thị người gửi của tài khoản đang vô hiệu hóa là "Tài khoản tạm thời vô hiệu hoá" với avatar mặc định (BR-M16-26). | BF-M16-001, BF-M16-003 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E15.1, SC-M16-003/E15.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N4 |
| FR-M16-04.12 | Hệ thống phải hiển thị người gửi của tài khoản đang bị ban như tài khoản bình thường (BR-M16-26). | BF-M16-001, BF-M16-003 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E15.1, SC-M16-003/E15.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N4 |
| FR-M16-05.01 | Khi thành viên gửi một tin nhắn văn bản, có thể kèm emoji, hệ thống phải thêm tin vào cuộc trò chuyện với người gửi và thời điểm gửi (BR-M16-08). | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E6.1, SC-M16-004/E7.1, SC-M16-004/E8.1, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-05.02 | Khi một tin nhắn được gửi, hệ thống phải giao tin tới các thành viên khác đang mở cuộc ngay khi có (BR-M16-16). | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E6.1, SC-M16-004/E7.1, SC-M16-004/E8.1, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3 |
| FR-M16-05.03 | Khi một tin nhắn được gửi, hệ thống phải báo sự kiện tin nhắn mới cho M07 để gửi thông báo trong ứng dụng tới các thành viên khác của cuộc, không gửi email (BR-M16-21). | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E6.1, SC-M16-004/E7.1, SC-M16-004/E8.1, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3 |
| FR-M16-05.04 | Nếu thành viên đính kèm ảnh hoặc tệp vào tin nhắn, hệ thống phải từ chối (BR-M16-08). | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E3.1, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-05.05 | Nếu người gửi đã gửi 30 tin vào cùng một cuộc trò chuyện trong 60 giây gần nhất, hệ thống phải từ chối tin kế tiếp của người đó trong cuộc đó và báo người gửi đã gửi quá nhanh (BR-M16-09). | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E4.1, SC-M16-004/E7.1, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-05.06 | Nếu người không là thành viên của cuộc trò chuyện, kể cả thành viên cũ, Guest, Mod và Admin, gửi tin vào cuộc đó, hệ thống phải từ chối. | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/E16.1, SC-M16-003/E16.2, SC-M16-003/E17.1, SC-M16-003/E17.2, SC-M16-003/E18.1, SC-M16-003/E18.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E8.1, SC-M16-004/E12.1, SC-M16-004/E12.2, SC-M16-004/E13.1, SC-M16-004/E13.2, SC-M16-004/E14.2, SC-M16-004/E15.1, SC-M16-004/E15.2, SC-M16-004/E16.1, SC-M16-004/E16.2, SC-M16-005/E10.1, SC-M16-005/E10.2, SC-M16-005/E11.2, SC-M16-007/E11.1, SC-M16-007/E11.2, SC-M16-007/E12.2, SC-M16-008/E5.1, SC-M16-008/E5.2, SC-M16-008/E6.2, SC-M16-010/E10.1, SC-M16-010/E10.2, SC-M16-010/E11.2, SC-M16-011/E9.1, SC-M16-011/E9.2, SC-M16-011/E10.2, SC-M16-012/E5.1, SC-M16-012/E5.2, SC-M16-012/E6.2, SC-M16-013/E7.1, SC-M16-013/E7.2, SC-M16-013/E8.2, SC-M16-014/E6.1, SC-M16-014/E6.2, SC-M16-014/E7.2, SC-M16-015/E7.1, SC-M16-015/E7.2, SC-M16-015/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-05.07 | Hệ thống phải không cho bất kỳ ai sửa nội dung tin nhắn đã gửi (BR-M16-10). | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-05.08 | Hệ thống phải giữ tin nhắn vĩnh viễn, không tự xóa theo thời gian (BR-M16-18). | BF-M16-004, BF-M16-005 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2, SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E9.1, SC-M16-005/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-05.09 | Hệ thống phải không gửi nội dung tin nhắn đi quét AI (BR-M16-20). | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-05.10 | Hệ thống phải không có thao tác báo cáo tin nhắn và chặn người dùng trong Chat ở MS1 (BR-M16-20). | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-05.11 | Nếu tin nhắn trống hoặc chỉ gồm khoảng trắng, hệ thống phải từ chối gửi (BR-M16-08). | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E1.1, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-05.12 | Nếu tin nhắn dài hơn 1.000 từ, hệ thống phải từ chối gửi (BR-M16-08). | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E2.1, SC-M16-004/E7.1, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-05.13 | Nếu thành viên gửi tin trong trò chuyện 1-1 với một tài khoản đã xóa, hệ thống phải từ chối (BR-M16-25). | BF-M16-001, BF-M16-004 | SC-M16-001/E1.1, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E5.1, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N4 |
| FR-M16-05.14 | Khi thành viên gửi tin trong trò chuyện 1-1 đã có với một tài khoản đang bị ban hoặc đang vô hiệu hóa, hệ thống phải nhận tin để người đó đọc khi tài khoản hoạt động trở lại (BR-M16-25). | BF-M16-001, BF-M16-004 | SC-M16-001/E1.1, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E6.1, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N4 |
| FR-M16-06.01 | Khi người gửi chọn thu hồi một tin nhắn của mình mà thời gian từ thời điểm gửi chưa quá 5 phút, hệ thống phải thu hồi tin đó với mọi thành viên của cuộc (BR-M16-11). | BF-M16-005 | SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E1.1, SC-M16-005/E5.1, SC-M16-005/E5.2, SC-M16-005/E9.1, SC-M16-005/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-06.02 | Khi một tin nhắn bị thu hồi, hệ thống phải hiển thị dòng "Tin nhắn đã bị thu hồi" ở đúng vị trí của tin đó cho mọi thành viên (BR-M16-12). | BF-M16-005 | SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E1.1, SC-M16-005/E5.2, SC-M16-005/E9.1, SC-M16-005/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-06.03 | Nếu thời gian từ thời điểm gửi đã quá 5 phút, hệ thống phải từ chối thu hồi (BR-M16-11). | BF-M16-005 | SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E2.1, SC-M16-005/E9.1, SC-M16-005/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-06.04 | Nếu người không phải người gửi, kể cả Admin nhóm chat, chọn thu hồi một tin nhắn, hệ thống phải từ chối (BR-M16-11). | BF-M16-005 | SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E3.1, SC-M16-005/E9.1, SC-M16-005/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-06.05 | Hệ thống phải chỉ có một kiểu thu hồi áp cho mọi thành viên, không có xóa tin chỉ ở phía người gửi (BR-M16-11). | BF-M16-005 | SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E9.1, SC-M16-005/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-06.06 | Nếu tin nhắn đã bị thu hồi, hệ thống phải từ chối thu hồi lần nữa. | BF-M16-005 | SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E4.1, SC-M16-005/E9.1, SC-M16-005/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-06.07 | Khi thu hồi một tin nhắn, hệ thống phải gắn cờ đã thu hồi và giữ nội dung gốc, không hiển thị nội dung đó với bất kỳ ai, kể cả Mod và Admin (BR-M16-12). | BF-M16-005 | SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E1.1, SC-M16-005/E5.2, SC-M16-005/E9.1, SC-M16-005/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-06.08 | Khi một tin nhắn bị thu hồi, hệ thống phải cập nhật dòng giữ chỗ ngay cho các thành viên đang mở cuộc, không cần tải lại trang (BR-M16-12). | BF-M16-005 | SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E1.1, SC-M16-005/E5.2, SC-M16-005/E9.1, SC-M16-005/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3 |
| FR-M16-06.09 | Khi tin nhắn mới nhất bị thu hồi, hệ thống phải giữ dòng giữ chỗ làm tin nhắn mới nhất, mang trạng thái Đã gửi, Đã xem (BR-M16-12). | BF-M16-001, BF-M16-003, BF-M16-004, BF-M16-005 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E5.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2, SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E1.1, SC-M16-005/E9.1, SC-M16-005/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| FR-M16-07.01 | Khi thành viên mở một cuộc trò chuyện, hệ thống phải ghi mốc đã đọc của thành viên tới tin nhắn mới nhất của cuộc (BR-M16-14). | BF-M16-001, BF-M16-003, BF-M16-004 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E5.1, SC-M16-003/E6.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| FR-M16-07.02 | Khi có tin mới tới trong lúc thành viên đang xem ở cuối cuộc trò chuyện, hệ thống phải ghi mốc đã đọc của thành viên tới tin đó (BR-M16-14). | BF-M16-001, BF-M16-003, BF-M16-004 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E5.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| FR-M16-07.03 | Trong khi cửa sổ cuộc trò chuyện đang bị ẩn, hệ thống phải hoãn ghi mốc cho tin mới tới khi cửa sổ hiển thị lại (BR-M16-14). | BF-M16-001, BF-M16-003, BF-M16-004 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E2.3, SC-M16-003/E3.1, SC-M16-003/E3.2, SC-M16-003/E3.3, SC-M16-003/E3.4, SC-M16-003/E4.1, SC-M16-003/E4.2, SC-M16-003/E4.3, SC-M16-003/E4.4, SC-M16-003/E5.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| FR-M16-07.04 | Khi thành viên đang đọc tin cũ cuộn xuống tới cuối cuộc trò chuyện, hệ thống phải ghi mốc đã đọc tới tin nhắn mới nhất (BR-M16-14). | BF-M16-001, BF-M16-003, BF-M16-004 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E2.1, SC-M16-003/E2.2, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E4.1, SC-M16-003/E4.3, SC-M16-003/E4.4, SC-M16-003/E5.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| FR-M16-07.05 | Khi ghi mốc đã đọc, hệ thống phải giữ tin mới hơn giữa mốc hiện tại và tin vừa đọc, không để mốc lùi (BR-M16-13). | BF-M16-001, BF-M16-003, BF-M16-004 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E5.1, SC-M16-003/E6.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| FR-M16-07.06 | Hệ thống phải hiển thị dưới tin nhắn mới nhất avatar của các thành viên đã đọc tới tin đó, gộp khi có nhiều người, trừ người gửi tin đó và chính người đang xem (BR-M16-15). | BF-M16-001, BF-M16-003, BF-M16-004 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E5.1, SC-M16-003/E6.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| FR-M16-07.07 | Hệ thống phải hiển thị Đã gửi ở tin nhắn mới nhất khi chưa có thành viên nào khác người gửi đọc tới tin đó (BR-M16-15). | BF-M16-001, BF-M16-003, BF-M16-004 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E5.1, SC-M16-003/E6.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| FR-M16-07.08 | Hệ thống phải không hiển thị trạng thái Đã gửi, Đã xem ở các tin cũ hơn tin nhắn mới nhất, và không hiển thị avatar của thành viên chưa đọc tới tin nhắn mới nhất (BR-M16-15). | BF-M16-001, BF-M16-003, BF-M16-004, BF-M16-005 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E5.1, SC-M16-003/E6.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2, SC-M16-005/E5.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| FR-M16-07.09 | Khi một thành viên có mốc đã đọc mới, hệ thống phải cập nhật hiển thị đã xem cho các thành viên khác đang mở cuộc ngay, không cần tải lại trang (BR-M16-16). | BF-M16-001, BF-M16-003, BF-M16-004 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E5.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| FR-M16-07.10 | Hệ thống phải cung cấp cho M07 mốc đã đọc của từng người trong mỗi cuộc trò chuyện và việc cuộc đó có tin chưa đọc mà người đó thấy được hay không (thành viên cũ chỉ tính tin gửi trước thời điểm rời), để M07 đếm số cuộc có tin chưa đọc trên biểu tượng Tin nhắn. | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004 | SC-M16-001/E1.1, SC-M16-002/M1, SC-M16-002/M2, SC-M16-002/E7.1, SC-M16-002/E7.2, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E5.1, SC-M16-003/E13.2, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| FR-M16-07.11 | Khi thành viên gửi một tin nhắn, hệ thống phải ghi mốc đã đọc của người gửi tới tin đó (BR-M16-13). | BF-M16-001, BF-M16-003, BF-M16-004 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E5.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E6.1, SC-M16-004/E7.1, SC-M16-004/E8.1, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| FR-M16-08.01 | Khi thành viên nhóm chat thêm một người dùng trong lúc công tắc duyệt thành viên mới đang tắt, hệ thống phải đưa người đó vào nhóm làm Member ngay (BR-M16-06). | BF-M16-007 | SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E10.1, SC-M16-007/E10.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-08.02 | Khi Admin nhóm chat thêm một người dùng, hệ thống phải đưa người đó vào nhóm làm Member ngay, kể cả khi công tắc duyệt đang bật (BR-M16-06). | BF-M16-007, BF-M16-011 | SC-M16-007/E8.1, SC-M16-007/E8.2, SC-M16-011/E1.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-08.03 | Khi Member thêm một người dùng trong lúc công tắc duyệt đang bật, hệ thống phải tạo đề nghị thêm thành viên ở trạng thái Chờ duyệt thay vì đưa người đó vào nhóm (BR-M16-06). | BF-M16-007, BF-M16-011 | SC-M16-007/E1.1, SC-M16-011/E1.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-08.04 | Hệ thống phải cho thêm người dùng mà không đòi người đó theo dõi người thêm hay cùng thuộc một Group nào (BR-M16-01). | BF-M16-007 | SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E10.1, SC-M16-007/E10.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-08.05 | Nếu nhóm chat đã có 100 thành viên, hệ thống phải từ chối đưa thêm người vào nhóm (BR-M16-03). | BF-M16-006, BF-M16-007, BF-M16-009, BF-M16-010, BF-M16-011 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E4.1, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-08.06 | Nếu người không là thành viên của nhóm chat, kể cả thành viên cũ, Guest, Mod và Admin, thêm người vào nhóm, hệ thống phải từ chối (BR-M16-05). | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/E16.2, SC-M16-004/E13.2, SC-M16-005/E10.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-007/E11.2, SC-M16-008/E5.2, SC-M16-010/E10.2, SC-M16-011/E9.2, SC-M16-012/E5.2, SC-M16-013/E7.2, SC-M16-014/E6.2, SC-M16-015/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-08.07 | Nếu người được thêm đã là thành viên của nhóm chat, hệ thống phải không thêm lần nữa. | BF-M16-006, BF-M16-007, BF-M16-009, BF-M16-010, BF-M16-011 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E2.1, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-08.08 | Khi thành viên thêm một thành viên cũ của nhóm, hệ thống phải xử lý như thêm người dùng mới, theo công tắc duyệt hiện tại (BR-M16-28). | BF-M16-006, BF-M16-007, BF-M16-009, BF-M16-010, BF-M16-011 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N4 |
| FR-M16-08.09 | Nếu người được thêm đang bị ban, đang vô hiệu hóa hoặc đã xóa, hệ thống phải từ chối thêm (BR-M16-25). | BF-M16-006, BF-M16-007, BF-M16-009, BF-M16-010, BF-M16-011 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E3.1, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N4 |
| FR-M16-08.10 | Khi thành viên nhóm chat lấy link mời, hệ thống phải đưa ra link mời chung duy nhất của nhóm (BR-M16-29). | BF-M16-008 | SC-M16-008/M1, SC-M16-008/M2, SC-M16-008/E4.1, SC-M16-008/E4.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-08.11 | Hệ thống phải giữ link mời của nhóm chat không hết hạn và không cho thu hồi hay tạo lại (BR-M16-29). | BF-M16-008 | SC-M16-008/M1, SC-M16-008/M2, SC-M16-008/E4.1, SC-M16-008/E4.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-08.12 | Nếu người không là thành viên của nhóm chat lấy link mời, hệ thống phải từ chối (BR-M16-29). | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/E16.2, SC-M16-004/E13.2, SC-M16-005/E10.2, SC-M16-007/E11.2, SC-M16-008/M1, SC-M16-008/M2, SC-M16-008/E4.1, SC-M16-008/E4.2, SC-M16-008/E5.2, SC-M16-010/E10.2, SC-M16-011/E9.2, SC-M16-012/E5.2, SC-M16-013/E7.2, SC-M16-014/E6.2, SC-M16-015/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-08.13 | Hệ thống phải không gửi thông báo "được mời" khi thành viên thêm người hay gửi link mời (BR-M16-29). | BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E1.1, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-008/M1, SC-M16-008/M2, SC-M16-008/E4.1, SC-M16-008/E4.2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-09.01 | Khi Admin nhóm chat bật hoặc tắt công tắc duyệt thành viên mới, hệ thống phải áp cài đặt mới cho các lần thêm thành viên và xin gia nhập sau đó (BR-M16-06). | BF-M16-011 | SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E1.1, SC-M16-011/E1.2, SC-M16-011/E3.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-09.02 | Nếu Member hoặc người không là thành viên của nhóm chat đổi công tắc duyệt, hệ thống phải từ chối (BR-M16-05). | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/E16.2, SC-M16-004/E13.2, SC-M16-005/E10.2, SC-M16-007/E11.2, SC-M16-008/E5.2, SC-M16-010/E10.2, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E8.1, SC-M16-011/E8.2, SC-M16-011/E9.2, SC-M16-012/E5.2, SC-M16-013/E7.2, SC-M16-014/E6.2, SC-M16-015/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-09.03 | Khi Admin nhóm chat tắt công tắc duyệt, hệ thống phải chấp nhận ngay người chờ duyệt của nhóm theo thứ tự bắt đầu chờ, sớm nhất trước, cho tới khi nhóm đủ 100 thành viên (BR-M16-33). | BF-M16-011 | SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E3.1, SC-M16-011/E4.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N1, N10 |
| FR-M16-09.04 | Khi công tắc duyệt được tắt mà nhóm không đủ chỗ cho mọi người chờ duyệt, hệ thống phải chuyển những người không vào được sang Đã từ chối (BR-M16-33). | BF-M16-011 | SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E4.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N1, N10 |
| FR-M16-10.01 | Khi Admin nhóm chat chấp nhận một đề nghị thêm thành viên hoặc yêu cầu gia nhập đang Chờ duyệt, hệ thống phải đưa người đó vào nhóm làm Member và chuyển đề nghị, yêu cầu sang Đã chấp nhận (BR-M16-06). | BF-M16-006, BF-M16-007, BF-M16-009, BF-M16-010, BF-M16-011 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.4, SC-M16-010/M1, SC-M16-010/M2, SC-M16-010/M3, SC-M16-010/M4, SC-M16-010/E9.1, SC-M16-010/E9.2, SC-M16-010/E9.3, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-10.02 | Khi Admin nhóm chat từ chối một đề nghị thêm thành viên hoặc yêu cầu gia nhập đang Chờ duyệt, hệ thống phải chuyển đề nghị, yêu cầu sang Đã từ chối và không đưa người đó vào nhóm (BR-M16-06). | BF-M16-010 | SC-M16-010/M1, SC-M16-010/M2, SC-M16-010/E1.1, SC-M16-010/E1.2, SC-M16-010/E9.1, SC-M16-010/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-10.03 | Nếu Admin nhóm chat chấp nhận khi nhóm đã có 100 thành viên, hệ thống phải từ chối thao tác (BR-M16-03). | BF-M16-006, BF-M16-007, BF-M16-009, BF-M16-010, BF-M16-011 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.4, SC-M16-010/M1, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E3.1, SC-M16-010/E9.1, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-10.04 | Nếu Member hoặc người không là thành viên của nhóm chat chấp nhận hoặc từ chối người chờ duyệt, hệ thống phải từ chối (BR-M16-05). | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/E16.2, SC-M16-004/E13.2, SC-M16-005/E10.2, SC-M16-007/E11.2, SC-M16-008/E5.2, SC-M16-009/E9.1, SC-M16-010/M1, SC-M16-010/M2, SC-M16-010/E7.1, SC-M16-010/E9.1, SC-M16-010/E9.2, SC-M16-010/E10.2, SC-M16-011/E9.2, SC-M16-012/E5.2, SC-M16-013/E7.2, SC-M16-014/E6.2, SC-M16-015/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-10.05 | Hệ thống phải hiển thị cho Admin nhóm chat các đề nghị thêm thành viên và yêu cầu gia nhập đang Chờ duyệt của nhóm. | BF-M16-010 | SC-M16-010/M1, SC-M16-010/M2, SC-M16-010/E9.1, SC-M16-010/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-10.06 | Nếu đề nghị hoặc yêu cầu không còn ở trạng thái Chờ duyệt, hệ thống phải từ chối chấp nhận hoặc từ chối nó. | BF-M16-010 | SC-M16-010/M1, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E2.1, SC-M16-010/E9.1, SC-M16-010/E9.2, SC-M16-010/E9.4 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-10.07 | Hệ thống phải không tính người chờ duyệt vào giới hạn 100 thành viên; giới hạn được kiểm lúc người đó vào nhóm (BR-M16-03). | BF-M16-006, BF-M16-007, BF-M16-009, BF-M16-010, BF-M16-011 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E1.1, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-009/M4, SC-M16-009/E1.1, SC-M16-009/E5.1, SC-M16-009/E11.4, SC-M16-010/M1, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E3.1, SC-M16-010/E9.1, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N10 |
| FR-M16-11.01 | Khi Admin nhóm chat xóa một Member, hệ thống phải đưa người đó ra khỏi nhóm với trạng thái Bị xóa và giữ nhóm trong hộp thư của người đó như thành viên cũ (BR-M16-05, BR-M16-27). | BF-M16-012 | SC-M16-012/M1, SC-M16-012/M2, SC-M16-012/E4.1, SC-M16-012/E4.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-11.02 | Nếu Member hoặc người không là thành viên của nhóm chat xóa thành viên, hệ thống phải từ chối (BR-M16-05). | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/E16.2, SC-M16-004/E13.2, SC-M16-005/E10.2, SC-M16-007/E11.2, SC-M16-008/E5.2, SC-M16-010/E10.2, SC-M16-011/E9.2, SC-M16-012/M1, SC-M16-012/M2, SC-M16-012/E4.1, SC-M16-012/E4.2, SC-M16-012/E5.2, SC-M16-013/E7.2, SC-M16-014/E6.2, SC-M16-015/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-11.03 | Khi nhóm chat còn dưới 3 thành viên sau khi có người bị xóa, hệ thống phải giữ nhóm hoạt động bình thường (BR-M16-03). | BF-M16-012 | SC-M16-012/M1, SC-M16-012/M2, SC-M16-012/E4.1, SC-M16-012/E4.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-12.01 | Khi một thành viên nhóm chat đổi tên nhóm, hệ thống phải áp tên mới cho nhóm với mọi thành viên (BR-M16-05). | BF-M16-013 | SC-M16-013/M1, SC-M16-013/M2, SC-M16-013/E2.1, SC-M16-013/E6.1, SC-M16-013/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-12.02 | Nếu người không là thành viên của nhóm chat, kể cả thành viên cũ, Guest, Mod và Admin, đổi tên nhóm, hệ thống phải từ chối (BR-M16-05). | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/E16.2, SC-M16-004/E13.2, SC-M16-005/E10.2, SC-M16-007/E11.2, SC-M16-008/E5.2, SC-M16-010/E10.2, SC-M16-011/E9.2, SC-M16-012/E5.2, SC-M16-013/M1, SC-M16-013/M2, SC-M16-013/E6.1, SC-M16-013/E6.2, SC-M16-013/E7.2, SC-M16-014/E6.2, SC-M16-015/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-12.03 | Nếu tên mới trống hoặc dài hơn 100 ký tự sau khi bỏ khoảng trắng đầu và cuối, hệ thống phải từ chối (BR-M16-32). | BF-M16-013 | SC-M16-013/M1, SC-M16-013/M2, SC-M16-013/E1.1, SC-M16-013/E2.1, SC-M16-013/E6.1, SC-M16-013/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-13.01 | Khi Admin nhóm chat chuyển quyền cho một Member, hệ thống phải đặt Member đó làm Admin nhóm chat và người chuyển làm Member (BR-M16-07). | BF-M16-014 | SC-M16-014/M1, SC-M16-014/M2, SC-M16-014/E1.1, SC-M16-014/E5.1, SC-M16-014/E5.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-13.02 | Nếu Member hoặc người không là thành viên của nhóm chat chuyển quyền Admin nhóm chat, hệ thống phải từ chối (BR-M16-05). | BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-007, BF-M16-008, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-003/E16.2, SC-M16-004/E13.2, SC-M16-005/E10.2, SC-M16-007/E11.2, SC-M16-008/E5.2, SC-M16-010/E10.2, SC-M16-011/E9.2, SC-M16-012/E5.2, SC-M16-013/E7.2, SC-M16-014/M1, SC-M16-014/M2, SC-M16-014/E5.1, SC-M16-014/E5.2, SC-M16-014/E6.2, SC-M16-015/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-13.03 | Hệ thống phải không tự chuyển quyền Admin nhóm chat cho thành viên nào, kể cả khi Admin nhóm chat bị ban, vô hiệu hóa hoặc xóa tài khoản (BR-M16-07, BR-M16-30). | BF-M16-014 | SC-M16-014/M1, SC-M16-014/M2, SC-M16-014/E5.1, SC-M16-014/E5.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N1 |
| FR-M16-14.01 | Khi Member chọn rời nhóm chat, hệ thống phải đưa người đó ra khỏi nhóm với trạng thái Đã rời và giữ nhóm trong hộp thư của người đó như thành viên cũ (BR-M16-05, BR-M16-27). | BF-M16-015 | SC-M16-015/M1, SC-M16-015/M2, SC-M16-015/E4.2, SC-M16-015/E6.1, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-14.02 | Nếu Admin nhóm chat chọn rời nhóm còn thành viên khác khi chưa chuyển quyền, hệ thống phải từ chối (BR-M16-07). | BF-M16-014, BF-M16-015 | SC-M16-014/M1, SC-M16-014/M2, SC-M16-014/E5.1, SC-M16-014/E5.2, SC-M16-015/M1, SC-M16-015/M2, SC-M16-015/E3.1, SC-M16-015/E3.2, SC-M16-015/E6.1, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-14.03 | Hệ thống phải phân biệt thành viên tự rời nhóm với thành viên bị Admin nhóm chat xóa (BR-M16-05). | BF-M16-012, BF-M16-015 | SC-M16-012/M1, SC-M16-012/M2, SC-M16-012/E4.1, SC-M16-012/E4.2, SC-M16-015/M1, SC-M16-015/M2, SC-M16-015/E6.1, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-14.04 | Khi Admin nhóm chat là thành viên cuối cùng chọn rời, hệ thống phải cho rời mà không cần chuyển quyền; nhóm không còn thành viên nào gửi được tin (BR-M16-07). | BF-M16-015 | SC-M16-015/M1, SC-M16-015/M2, SC-M16-015/E4.1, SC-M16-015/E4.2, SC-M16-015/E6.1, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-14.05 | Khi nhóm chat còn dưới 3 thành viên sau khi có người rời, hệ thống phải giữ nhóm hoạt động bình thường (BR-M16-03). | BF-M16-015 | SC-M16-015/M1, SC-M16-015/M2, SC-M16-015/E6.1, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-15.01 | Trong khi cờ tính năng Chat tắt, nếu người dùng không phải Admin thao tác với Chat, hệ thống phải từ chối với thông báo "Hệ thống đang bận, vui lòng thử lại sau" (BR-M16-23). | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M2, SC-M16-001/E5.1, SC-M16-001/E7.2, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E7.2, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E11.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.6, SC-M16-004/M2, SC-M16-004/E10.1, SC-M16-004/E12.2, SC-M16-005/M2, SC-M16-005/E7.1, SC-M16-005/E9.2, SC-M16-006/M2, SC-M16-006/E7.1, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E10.2, SC-M16-008/M2, SC-M16-008/E2.1, SC-M16-008/E4.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E6.1, SC-M16-011/E8.2, SC-M16-012/M2, SC-M16-012/E2.1, SC-M16-012/E4.2, SC-M16-013/M2, SC-M16-013/E4.1, SC-M16-013/E6.2, SC-M16-014/M2, SC-M16-014/E3.1, SC-M16-014/E5.2, SC-M16-015/M2, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N2 |
| FR-M16-15.02 | Trong khi cờ tính năng Chat tắt, hệ thống phải giữ nguyên các lối vào Chat (BR-M16-23). | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M2, SC-M16-001/E5.1, SC-M16-001/E7.2, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E7.2, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E11.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.6, SC-M16-004/M2, SC-M16-004/E10.1, SC-M16-004/E12.2, SC-M16-005/M2, SC-M16-005/E7.1, SC-M16-005/E9.2, SC-M16-006/M2, SC-M16-006/E7.1, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E10.2, SC-M16-008/M2, SC-M16-008/E2.1, SC-M16-008/E4.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E6.1, SC-M16-011/E8.2, SC-M16-012/M2, SC-M16-012/E2.1, SC-M16-012/E4.2, SC-M16-013/M2, SC-M16-013/E4.1, SC-M16-013/E6.2, SC-M16-014/M2, SC-M16-014/E3.1, SC-M16-014/E5.2, SC-M16-015/M2, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N2 |
| FR-M16-15.03 | Trong khi cờ tính năng Chat tắt, hệ thống phải không xóa hay đổi dữ liệu của Chat (BR-M16-23). | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M2, SC-M16-001/E5.1, SC-M16-001/E7.2, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E7.2, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E11.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.6, SC-M16-004/M2, SC-M16-004/E10.1, SC-M16-004/E12.2, SC-M16-005/M2, SC-M16-005/E7.1, SC-M16-005/E9.2, SC-M16-006/M2, SC-M16-006/E7.1, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E10.2, SC-M16-008/M2, SC-M16-008/E2.1, SC-M16-008/E4.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E6.1, SC-M16-011/E8.2, SC-M16-012/M2, SC-M16-012/E2.1, SC-M16-012/E4.2, SC-M16-013/M2, SC-M16-013/E4.1, SC-M16-013/E6.2, SC-M16-014/M2, SC-M16-014/E3.1, SC-M16-014/E5.2, SC-M16-015/M2, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N2 |
| FR-M16-15.04 | Trong khi cờ tính năng Chat tắt, hệ thống phải cho Admin dùng Chat như khi cờ bật (BR-M16-23). | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M2, SC-M16-001/E5.1, SC-M16-001/E7.1, SC-M16-001/E7.2, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E7.1, SC-M16-002/E7.2, SC-M16-002/E7.3, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E11.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-003/E15.3, SC-M16-003/E15.4, SC-M16-003/E15.5, SC-M16-003/E15.6, SC-M16-003/E17.2, SC-M16-003/E18.2, SC-M16-004/M2, SC-M16-004/E10.1, SC-M16-004/E12.1, SC-M16-004/E12.2, SC-M16-004/E15.2, SC-M16-004/E16.2, SC-M16-005/M2, SC-M16-005/E7.1, SC-M16-005/E9.1, SC-M16-005/E9.2, SC-M16-006/M2, SC-M16-006/E7.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-008/M2, SC-M16-008/E2.1, SC-M16-008/E4.1, SC-M16-008/E4.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E11.1, SC-M16-009/E11.2, SC-M16-009/E11.3, SC-M16-009/E11.4, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E9.1, SC-M16-010/E9.2, SC-M16-010/E9.3, SC-M16-010/E9.4, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E6.1, SC-M16-011/E8.1, SC-M16-011/E8.2, SC-M16-012/M2, SC-M16-012/E2.1, SC-M16-012/E4.1, SC-M16-012/E4.2, SC-M16-013/M2, SC-M16-013/E4.1, SC-M16-013/E6.1, SC-M16-013/E6.2, SC-M16-014/M2, SC-M16-014/E3.1, SC-M16-014/E5.1, SC-M16-014/E5.2, SC-M16-015/M2, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E6.1, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N2 |
| FR-M16-15.05 | Khi cờ tính năng Chat được bật lại, hệ thống phải không làm bù thao tác đã bị từ chối trong lúc cờ tắt (BR-M16-23). | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M2, SC-M16-001/E5.1, SC-M16-001/E7.2, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E7.2, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E11.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.6, SC-M16-004/M2, SC-M16-004/E10.1, SC-M16-004/E12.2, SC-M16-005/M2, SC-M16-005/E2.1, SC-M16-005/E7.1, SC-M16-005/E9.2, SC-M16-006/M2, SC-M16-006/E7.1, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E10.2, SC-M16-008/M2, SC-M16-008/E2.1, SC-M16-008/E4.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E6.1, SC-M16-011/E8.2, SC-M16-012/M2, SC-M16-012/E2.1, SC-M16-012/E4.2, SC-M16-013/M2, SC-M16-013/E4.1, SC-M16-013/E6.2, SC-M16-014/M2, SC-M16-014/E3.1, SC-M16-014/E5.2, SC-M16-015/M2, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N2 |
| FR-M16-15.06 | Trong khi cờ tính năng Chat tắt, hệ thống phải từ chối theo FR-M16-15.01 các thao tác: mở hộp thư, mở cuộc trò chuyện, bắt đầu trò chuyện 1-1, tạo nhóm chat, gửi tin, thu hồi tin, thêm thành viên, xóa thành viên, duyệt người chờ, đổi tên nhóm, chuyển quyền Admin nhóm chat, rời nhóm, bật tắt duyệt, lấy link mời, xin gia nhập (BR-M16-23). | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M2, SC-M16-001/E5.1, SC-M16-001/E7.2, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E7.2, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E11.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.6, SC-M16-004/M2, SC-M16-004/E10.1, SC-M16-004/E12.2, SC-M16-005/M2, SC-M16-005/E7.1, SC-M16-005/E9.2, SC-M16-006/M2, SC-M16-006/E7.1, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E10.2, SC-M16-008/M2, SC-M16-008/E2.1, SC-M16-008/E4.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E6.1, SC-M16-011/E8.2, SC-M16-012/M2, SC-M16-012/E2.1, SC-M16-012/E4.2, SC-M16-013/M2, SC-M16-013/E4.1, SC-M16-013/E6.2, SC-M16-014/M2, SC-M16-014/E3.1, SC-M16-014/E5.2, SC-M16-015/M2, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N2 |
| FR-M16-15.07 | Trong khi cờ tính năng Chat tắt, hệ thống phải vẫn hiển thị biểu tượng Tin nhắn cùng số chưa đọc (M07) và nút "Nhắn tin" trên hồ sơ (BR-M16-23). | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M2, SC-M16-001/E5.1, SC-M16-001/E7.2, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E7.2, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E11.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.6, SC-M16-004/M2, SC-M16-004/E10.1, SC-M16-004/E12.2, SC-M16-005/M2, SC-M16-005/E7.1, SC-M16-005/E9.2, SC-M16-006/M2, SC-M16-006/E7.1, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E10.2, SC-M16-008/M2, SC-M16-008/E2.1, SC-M16-008/E4.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E6.1, SC-M16-011/E8.2, SC-M16-012/M2, SC-M16-012/E2.1, SC-M16-012/E4.2, SC-M16-013/M2, SC-M16-013/E4.1, SC-M16-013/E6.2, SC-M16-014/M2, SC-M16-014/E3.1, SC-M16-014/E5.2, SC-M16-015/M2, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N2 |
| FR-M16-15.08 | Trong khi cờ tính năng Chat tắt, hệ thống phải vẫn tự tắt duyệt khi Admin nhóm chat không thể khôi phục (FR-M16-17) và vẫn tính hạn thu hồi 5 phút theo thời gian thực (BR-M16-23). | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M2, SC-M16-001/E5.1, SC-M16-001/E7.2, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E7.2, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E11.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.6, SC-M16-004/M2, SC-M16-004/E10.1, SC-M16-004/E12.2, SC-M16-005/M2, SC-M16-005/E2.1, SC-M16-005/E7.1, SC-M16-005/E9.2, SC-M16-006/M2, SC-M16-006/E7.1, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E10.2, SC-M16-008/M2, SC-M16-008/E2.1, SC-M16-008/E4.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E6.1, SC-M16-011/E8.2, SC-M16-012/M2, SC-M16-012/E2.1, SC-M16-012/E4.2, SC-M16-013/M2, SC-M16-013/E4.1, SC-M16-013/E6.2, SC-M16-014/M2, SC-M16-014/E3.1, SC-M16-014/E5.2, SC-M16-015/M2, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N1, N2 |
| FR-M16-16.01 | Khi người dùng đã đăng nhập mở link mời của một nhóm chat, hệ thống phải hiển thị tên nhóm chat và nút "Xin gia nhập", không hiển thị tin nhắn của nhóm (BR-M16-29). | BF-M16-009 | SC-M16-009/M1, SC-M16-009/M2, SC-M16-009/E11.1, SC-M16-009/E11.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-16.02 | Nếu Guest mở link mời, hệ thống phải yêu cầu đăng nhập trước khi xin gia nhập (BR-M16-29). | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/E6.1, SC-M16-001/E6.2, SC-M16-002/E6.1, SC-M16-002/E6.2, SC-M16-003/E14.1, SC-M16-003/E14.2, SC-M16-004/E11.1, SC-M16-004/E11.2, SC-M16-005/E8.1, SC-M16-005/E8.2, SC-M16-006/E8.1, SC-M16-006/E8.2, SC-M16-007/E9.1, SC-M16-007/E9.2, SC-M16-008/E3.1, SC-M16-008/E3.2, SC-M16-009/M1, SC-M16-009/M2, SC-M16-009/E10.1, SC-M16-009/E10.2, SC-M16-009/E11.1, SC-M16-009/E11.2, SC-M16-010/E8.1, SC-M16-010/E8.2, SC-M16-011/E7.1, SC-M16-011/E7.2, SC-M16-012/E3.1, SC-M16-012/E3.2, SC-M16-013/E5.1, SC-M16-013/E5.2, SC-M16-014/E4.1, SC-M16-014/E4.2, SC-M16-015/E5.1, SC-M16-015/E5.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-16.03 | Khi người dùng xin gia nhập trong lúc công tắc duyệt đang tắt, hệ thống phải đưa người đó vào nhóm làm Member ngay (BR-M16-06). | BF-M16-006, BF-M16-007, BF-M16-009, BF-M16-010, BF-M16-011 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-009/M1, SC-M16-009/M2, SC-M16-009/M3, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.1, SC-M16-009/E11.2, SC-M16-009/E11.3, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-16.04 | Khi người dùng xin gia nhập trong lúc công tắc duyệt đang bật, hệ thống phải tạo yêu cầu gia nhập ở trạng thái Chờ duyệt (BR-M16-06). | BF-M16-009, BF-M16-011 | SC-M16-009/M1, SC-M16-009/M2, SC-M16-009/E1.1, SC-M16-009/E4.1, SC-M16-009/E11.1, SC-M16-009/E11.2, SC-M16-011/E1.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-16.05 | Nếu nhóm chat đã có 100 thành viên, hệ thống phải từ chối xin gia nhập (BR-M16-29). | BF-M16-009 | SC-M16-009/M1, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E2.1, SC-M16-009/E11.1, SC-M16-009/E11.2, SC-M16-009/E11.4 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-16.06 | Nếu người dùng đang có một yêu cầu gia nhập Chờ duyệt tới cùng nhóm chat, hệ thống phải từ chối gửi thêm yêu cầu (BR-M16-29). | BF-M16-009 | SC-M16-009/M1, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E3.1, SC-M16-009/E11.1, SC-M16-009/E11.2, SC-M16-009/E11.4 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-16.07 | Khi yêu cầu gia nhập của một người bị từ chối, hệ thống phải cho người đó gửi yêu cầu mới ngay, không giới hạn số lần (BR-M16-29). | BF-M16-009, BF-M16-010 | SC-M16-009/M1, SC-M16-009/M2, SC-M16-009/E4.1, SC-M16-009/E11.1, SC-M16-009/E11.2, SC-M16-010/E1.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| FR-M16-16.08 | Khi thành viên cũ xin gia nhập lại qua link mời, hệ thống phải xử lý như người dùng mới, theo công tắc duyệt hiện tại (BR-M16-28). | BF-M16-006, BF-M16-007, BF-M16-009, BF-M16-010, BF-M16-011 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-009/M1, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.1, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N4 |
| FR-M16-17.01 | Trong khi tài khoản Admin nhóm chat còn khôi phục được, hệ thống phải giữ nguyên Admin và mọi cài đặt của nhóm chat (BR-M16-30). | Nền theo trigger | N1 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N1 |
| FR-M16-17.02 | Khi Admin nhóm chat trở thành không thể khôi phục và công tắc duyệt đang bật, hệ thống phải tắt công tắc duyệt và xử lý người chờ duyệt như FR-M16-09.03, FR-M16-09.04 (BR-M16-30, BR-M16-33). | Nền theo trigger | N1, N10 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N1, N10 |
| FR-M16-17.03 | Khi Admin nhóm chat trở thành không thể khôi phục, hệ thống phải để nhóm chat không có Admin nhóm chat (BR-M16-30). | Nền theo trigger | N1 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N1 |
| BR-M16-01 | Sự kiện | BF-M16-001, BF-M16-006, BF-M16-007 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E7.1, SC-M16-001/E7.2, SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E10.1, SC-M16-007/E10.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N8 |
| BR-M16-02 | Ràng buộc | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E5.1, SC-M16-001/E6.1, SC-M16-001/E6.2, SC-M16-001/E7.1, SC-M16-001/E7.2, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E6.1, SC-M16-002/E6.2, SC-M16-002/E7.2, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E11.1, SC-M16-003/E14.1, SC-M16-003/E14.2, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.6, SC-M16-004/M2, SC-M16-004/E10.1, SC-M16-004/E11.1, SC-M16-004/E11.2, SC-M16-004/E12.2, SC-M16-005/M2, SC-M16-005/E7.1, SC-M16-005/E8.1, SC-M16-005/E8.2, SC-M16-005/E9.2, SC-M16-006/M2, SC-M16-006/E7.1, SC-M16-006/E8.1, SC-M16-006/E8.2, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E9.1, SC-M16-007/E9.2, SC-M16-007/E10.2, SC-M16-008/M2, SC-M16-008/E2.1, SC-M16-008/E3.1, SC-M16-008/E3.2, SC-M16-008/E4.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E10.1, SC-M16-009/E10.2, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E8.1, SC-M16-010/E8.2, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E6.1, SC-M16-011/E7.1, SC-M16-011/E7.2, SC-M16-011/E8.2, SC-M16-012/M2, SC-M16-012/E2.1, SC-M16-012/E3.1, SC-M16-012/E3.2, SC-M16-012/E4.2, SC-M16-013/M2, SC-M16-013/E4.1, SC-M16-013/E5.1, SC-M16-013/E5.2, SC-M16-013/E6.2, SC-M16-014/M2, SC-M16-014/E3.1, SC-M16-014/E4.1, SC-M16-014/E4.2, SC-M16-014/E5.2, SC-M16-015/M2, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E5.1, SC-M16-015/E5.2, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N2 |
| BR-M16-03 | Ràng buộc | BF-M16-006, BF-M16-007, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-015 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E1.1, SC-M16-006/E2.1, SC-M16-006/E3.1, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E4.1, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.4, SC-M16-010/M1, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E3.1, SC-M16-010/E9.1, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2, SC-M16-012/M1, SC-M16-012/M2, SC-M16-012/E4.1, SC-M16-012/E4.2, SC-M16-015/M1, SC-M16-015/M2, SC-M16-015/E6.1, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N8 |
| BR-M16-04 | Sự kiện | BF-M16-006, BF-M16-014 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-014/M1, SC-M16-014/M2, SC-M16-014/E1.1, SC-M16-014/E5.1, SC-M16-014/E5.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N8, N9 |
| BR-M16-05 | Ràng buộc | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M2, SC-M16-001/E5.1, SC-M16-001/E7.2, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E7.2, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E11.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.6, SC-M16-003/E16.1, SC-M16-003/E16.2, SC-M16-004/M2, SC-M16-004/E10.1, SC-M16-004/E12.2, SC-M16-004/E13.1, SC-M16-004/E13.2, SC-M16-004/E14.2, SC-M16-005/M2, SC-M16-005/E7.1, SC-M16-005/E9.2, SC-M16-005/E10.1, SC-M16-005/E10.2, SC-M16-005/E11.2, SC-M16-006/M2, SC-M16-006/E7.1, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E10.2, SC-M16-007/E11.1, SC-M16-007/E11.2, SC-M16-007/E12.2, SC-M16-008/M2, SC-M16-008/E2.1, SC-M16-008/E4.2, SC-M16-008/E5.1, SC-M16-008/E5.2, SC-M16-008/E6.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E9.1, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M1, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E7.1, SC-M16-010/E9.1, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-010/E10.1, SC-M16-010/E10.2, SC-M16-010/E11.2, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E6.1, SC-M16-011/E8.2, SC-M16-011/E9.1, SC-M16-011/E9.2, SC-M16-011/E10.2, SC-M16-012/M1, SC-M16-012/M2, SC-M16-012/E2.1, SC-M16-012/E4.1, SC-M16-012/E4.2, SC-M16-012/E5.1, SC-M16-012/E5.2, SC-M16-012/E6.2, SC-M16-013/M1, SC-M16-013/M2, SC-M16-013/E4.1, SC-M16-013/E6.1, SC-M16-013/E6.2, SC-M16-013/E7.1, SC-M16-013/E7.2, SC-M16-013/E8.2, SC-M16-014/M1, SC-M16-014/M2, SC-M16-014/E3.1, SC-M16-014/E5.1, SC-M16-014/E5.2, SC-M16-014/E6.1, SC-M16-014/E6.2, SC-M16-014/E7.2, SC-M16-015/M1, SC-M16-015/M2, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E6.1, SC-M16-015/E6.2, SC-M16-015/E7.1, SC-M16-015/E7.2, SC-M16-015/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N2, N9 |
| BR-M16-06 | Kích hoạt | BF-M16-006, BF-M16-007, BF-M16-009, BF-M16-010, BF-M16-011 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E1.1, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-009/M1, SC-M16-009/M2, SC-M16-009/E1.1, SC-M16-009/E11.1, SC-M16-009/E11.2, SC-M16-010/M1, SC-M16-010/M2, SC-M16-010/E1.2, SC-M16-010/E9.1, SC-M16-010/E9.2, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N8 |
| BR-M16-07 | Ràng buộc | BF-M16-014, BF-M16-015 | SC-M16-014/M1, SC-M16-014/M2, SC-M16-014/E1.1, SC-M16-014/E5.1, SC-M16-014/E5.2, SC-M16-015/M1, SC-M16-015/M2, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E6.1, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N9 |
| BR-M16-08 | Ràng buộc | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E1.1, SC-M16-004/E2.1, SC-M16-004/E3.1, SC-M16-004/E4.1, SC-M16-004/E5.1, SC-M16-004/E7.1, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N6 |
| BR-M16-09 | Ràng buộc | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E1.1, SC-M16-004/E2.1, SC-M16-004/E3.1, SC-M16-004/E4.1, SC-M16-004/E5.1, SC-M16-004/E7.1, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N6 |
| BR-M16-10 | Ràng buộc | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N6 |
| BR-M16-11 | Ràng buộc | BF-M16-005 | SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E1.1, SC-M16-005/E2.1, SC-M16-005/E3.1, SC-M16-005/E5.1, SC-M16-005/E9.1, SC-M16-005/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N6 |
| BR-M16-12 | Kích hoạt | BF-M16-003, BF-M16-005 | SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E1.1, SC-M16-005/E5.2, SC-M16-005/E9.1, SC-M16-005/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N6 |
| BR-M16-13 | Tính toán | BF-M16-001, BF-M16-003, BF-M16-004 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E5.1, SC-M16-003/E6.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| BR-M16-14 | Kích hoạt | BF-M16-001, BF-M16-003, BF-M16-004 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E2.3, SC-M16-003/E3.2, SC-M16-003/E3.4, SC-M16-003/E4.2, SC-M16-003/E4.4, SC-M16-003/E5.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| BR-M16-15 | Suy diễn | BF-M16-001, BF-M16-003, BF-M16-004, BF-M16-005 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E1.1, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E5.1, SC-M16-003/E6.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2, SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E5.2, SC-M16-005/E9.1, SC-M16-005/E9.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| BR-M16-16 | Kích hoạt | BF-M16-001, BF-M16-003, BF-M16-004 | SC-M16-001/E1.1, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E2.3, SC-M16-003/E3.4, SC-M16-003/E5.1, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N3, N7 |
| BR-M16-17 | Ràng buộc | BF-M16-003 | SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E1.1, SC-M16-003/E13.2, SC-M16-003/E13.4, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.6 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N5 |
| BR-M16-18 | Sự kiện | BF-M16-004, BF-M16-005, BF-M16-015 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2, SC-M16-005/M1, SC-M16-005/M2, SC-M16-005/E9.1, SC-M16-005/E9.2, SC-M16-015/M1, SC-M16-015/M2, SC-M16-015/E4.2, SC-M16-015/E6.1, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N6 |
| BR-M16-19 | Kích hoạt | BF-M16-003 | SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E15.1, SC-M16-003/E15.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| BR-M16-20 | Sự kiện | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N6 |
| BR-M16-21 | Sự kiện | BF-M16-004 | SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E12.1, SC-M16-004/E12.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | Theo bước ghi rõ |
| BR-M16-22 | Ràng buộc | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M2, SC-M16-001/E4.1, SC-M16-001/E5.1, SC-M16-001/E7.2, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E2.1, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E5.1, SC-M16-002/E7.2, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E7.1, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E10.1, SC-M16-003/E11.1, SC-M16-003/E12.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.6, SC-M16-004/M2, SC-M16-004/E9.1, SC-M16-004/E10.1, SC-M16-004/E12.2, SC-M16-005/M2, SC-M16-005/E6.1, SC-M16-005/E7.1, SC-M16-005/E9.2, SC-M16-006/M2, SC-M16-006/E6.1, SC-M16-006/E7.1, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E6.1, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E10.2, SC-M16-008/M2, SC-M16-008/E1.1, SC-M16-008/E2.1, SC-M16-008/E4.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E6.1, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E9.1, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E4.1, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E7.1, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E5.1, SC-M16-011/E6.1, SC-M16-011/E8.2, SC-M16-012/M2, SC-M16-012/E1.1, SC-M16-012/E2.1, SC-M16-012/E4.2, SC-M16-013/M2, SC-M16-013/E3.1, SC-M16-013/E4.1, SC-M16-013/E6.2, SC-M16-014/M2, SC-M16-014/E2.1, SC-M16-014/E3.1, SC-M16-014/E5.2, SC-M16-015/M2, SC-M16-015/E1.1, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N2 |
| BR-M16-23 | Kích hoạt | BF-M16-001, BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-001/M2, SC-M16-001/E5.1, SC-M16-001/E7.2, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E3.1, SC-M16-002/E4.1, SC-M16-002/E7.2, SC-M16-002/E7.4, SC-M16-003/M2, SC-M16-003/M4, SC-M16-003/M6, SC-M16-003/E8.1, SC-M16-003/E9.1, SC-M16-003/E11.1, SC-M16-003/E15.2, SC-M16-003/E15.4, SC-M16-003/E15.6, SC-M16-004/M2, SC-M16-004/E10.1, SC-M16-004/E12.2, SC-M16-005/M2, SC-M16-005/E2.1, SC-M16-005/E7.1, SC-M16-005/E9.2, SC-M16-006/M2, SC-M16-006/E7.1, SC-M16-006/E9.2, SC-M16-007/M2, SC-M16-007/E7.1, SC-M16-007/E8.2, SC-M16-007/E10.2, SC-M16-008/M2, SC-M16-008/E2.1, SC-M16-008/E4.2, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E7.1, SC-M16-009/E8.1, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M2, SC-M16-010/M4, SC-M16-010/E1.2, SC-M16-010/E5.1, SC-M16-010/E6.1, SC-M16-010/E9.2, SC-M16-010/E9.4, SC-M16-011/M2, SC-M16-011/E1.2, SC-M16-011/E6.1, SC-M16-011/E8.2, SC-M16-012/M2, SC-M16-012/E2.1, SC-M16-012/E4.2, SC-M16-013/M2, SC-M16-013/E4.1, SC-M16-013/E6.2, SC-M16-014/M2, SC-M16-014/E3.1, SC-M16-014/E5.2, SC-M16-015/M2, SC-M16-015/E2.1, SC-M16-015/E3.2, SC-M16-015/E4.2, SC-M16-015/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N2 |
| BR-M16-24 | Ràng buộc | BF-M16-001 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E1.1, SC-M16-001/E2.1, SC-M16-001/E7.1, SC-M16-001/E7.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N4 |
| BR-M16-25 | Ràng buộc | BF-M16-001, BF-M16-004, BF-M16-006, BF-M16-007, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-014 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E1.1, SC-M16-001/E3.1, SC-M16-001/E7.1, SC-M16-001/E7.2, SC-M16-004/M1, SC-M16-004/M2, SC-M16-004/E1.1, SC-M16-004/E2.1, SC-M16-004/E3.1, SC-M16-004/E4.1, SC-M16-004/E5.1, SC-M16-004/E6.1, SC-M16-004/E8.1, SC-M16-004/E12.1, SC-M16-004/E12.2, SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E4.1, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E3.1, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2, SC-M16-014/M1, SC-M16-014/M2, SC-M16-014/E5.1, SC-M16-014/E5.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N4 |
| BR-M16-26 | Suy diễn | BF-M16-001, BF-M16-002, BF-M16-003 | SC-M16-001/E1.1, SC-M16-002/M1, SC-M16-002/M2, SC-M16-002/E7.1, SC-M16-002/E7.2, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E15.1, SC-M16-003/E15.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N4 |
| BR-M16-27 | Suy diễn | BF-M16-002, BF-M16-003, BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-002/M1, SC-M16-002/M2, SC-M16-002/E7.1, SC-M16-002/E7.2, SC-M16-003/M1, SC-M16-003/M2, SC-M16-003/E13.2, SC-M16-003/E13.4, SC-M16-003/E15.1, SC-M16-003/E15.2, SC-M16-004/E14.1, SC-M16-004/E14.2, SC-M16-005/E11.1, SC-M16-005/E11.2, SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-007/E12.1, SC-M16-007/E12.2, SC-M16-008/E6.1, SC-M16-008/E6.2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E9.4, SC-M16-010/E11.1, SC-M16-010/E11.2, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2, SC-M16-011/E10.1, SC-M16-011/E10.2, SC-M16-012/M1, SC-M16-012/M2, SC-M16-012/E4.1, SC-M16-012/E4.2, SC-M16-012/E6.1, SC-M16-012/E6.2, SC-M16-013/E8.1, SC-M16-013/E8.2, SC-M16-014/E7.1, SC-M16-014/E7.2, SC-M16-015/M1, SC-M16-015/M2, SC-M16-015/E4.2, SC-M16-015/E6.1, SC-M16-015/E6.2, SC-M16-015/E8.1, SC-M16-015/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N4, N5, N9 |
| BR-M16-28 | Kích hoạt | BF-M16-004, BF-M16-005, BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-012, BF-M16-013, BF-M16-014, BF-M16-015 | SC-M16-004/E14.2, SC-M16-005/E11.2, SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-007/E12.2, SC-M16-008/E6.2, SC-M16-009/M1, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E5.1, SC-M16-009/E11.1, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E9.4, SC-M16-010/E11.2, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2, SC-M16-011/E10.2, SC-M16-012/M1, SC-M16-012/M2, SC-M16-012/E4.1, SC-M16-012/E4.2, SC-M16-012/E6.2, SC-M16-013/E8.2, SC-M16-014/E7.2, SC-M16-015/M1, SC-M16-015/M2, SC-M16-015/E6.1, SC-M16-015/E6.2, SC-M16-015/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N8 |
| BR-M16-29 | Ràng buộc | BF-M16-006, BF-M16-007, BF-M16-008, BF-M16-009, BF-M16-010, BF-M16-011, BF-M16-013 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-007/M1, SC-M16-007/M2, SC-M16-007/E5.1, SC-M16-007/E8.2, SC-M16-007/E10.1, SC-M16-007/E10.2, SC-M16-008/M1, SC-M16-008/M2, SC-M16-008/E4.1, SC-M16-008/E4.2, SC-M16-009/M1, SC-M16-009/M2, SC-M16-009/M4, SC-M16-009/E2.1, SC-M16-009/E3.1, SC-M16-009/E4.1, SC-M16-009/E5.1, SC-M16-009/E11.1, SC-M16-009/E11.2, SC-M16-009/E11.4, SC-M16-010/M4, SC-M16-010/E9.4, SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E8.1, SC-M16-011/E8.2, SC-M16-013/M1, SC-M16-013/M2, SC-M16-013/E6.1, SC-M16-013/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N8 |
| BR-M16-30 | Kích hoạt | BF-M16-014 | SC-M16-014/M1, SC-M16-014/M2, SC-M16-014/E5.1, SC-M16-014/E5.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N1, N9, N10 |
| BR-M16-31 | Ràng buộc | BF-M16-001, BF-M16-002 | SC-M16-001/M1, SC-M16-001/M2, SC-M16-001/E7.1, SC-M16-001/E7.2, SC-M16-002/M1, SC-M16-002/M2, SC-M16-002/M4, SC-M16-002/E1.1, SC-M16-002/E7.1, SC-M16-002/E7.2, SC-M16-002/E7.4 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N5 |
| BR-M16-32 | Ràng buộc | BF-M16-006, BF-M16-013 | SC-M16-006/M1, SC-M16-006/M2, SC-M16-006/E1.1, SC-M16-006/E2.1, SC-M16-006/E3.1, SC-M16-006/E5.1, SC-M16-006/E9.1, SC-M16-006/E9.2, SC-M16-013/M1, SC-M16-013/M2, SC-M16-013/E1.1, SC-M16-013/E2.1, SC-M16-013/E6.1, SC-M16-013/E6.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N8 |
| BR-M16-33 | Kích hoạt | BF-M16-011 | SC-M16-011/M1, SC-M16-011/M2, SC-M16-011/E2.1, SC-M16-011/E3.1, SC-M16-011/E4.1, SC-M16-011/E8.1, SC-M16-011/E8.2 | Có vị trí triển khai, giới hạn theo GAP nếu guard giao nhau chưa chốt | N1, N10 |


| UC nguồn | Nhánh nguồn | Điều kiện nguyên văn | Vị trí scenario hoặc GAP | Đối soát |
|---|---|---|---|---|
| UC-M16-001 | A 1 | Guest hoặc không qua cổng tài khoản/cờ | SC-M16-001/E6/E4/E5 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-001 | A 2 | Người nhận là chính người gọi | SC-M16-001/E2 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-001 | A 3 | Chưa có cuộc và người nhận BANNED/DEACTIVATED/DELETED | SC-M16-001/E3 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-001 | A 4 | Đã có cuộc với người nhận đang ban/vô hiệu hóa/đã xóa | SC-M16-001/E1 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-002 | A 1 | Guest/BANNED hoặc Chat tắt với người không phải Admin hệ thống | SC-M16-002/E6/E2/E3 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-002 | A 2 | Không có cuộc hợp lệ hoặc chỉ có 1-1 rỗng | SC-M16-002/E1 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-003 | A 1 | Không là thành viên/cựu của cuộc, kể cả Mod/Admin hệ thống | SC-M16-003/E tại M1 thiếu tư cách/E tại M1 staff | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-003 | A 2 | Cựu thành viên nhóm | SC-M16-003/E13 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-003 | A 3 | Cuộc chưa có tin hoặc đã tải tới tin đầu | SC-M16-003/E1/M6 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-003 | A 4 | Tin mới tới khi cửa sổ ẩn hoặc đang cuộn lên | SC-M16-003/E2/E3/E4/E5 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-004 | A 1 | Không là thành viên hiện tại, kể cả cựu/Guest/Mod/Admin ngoài cuộc | SC-M16-004/E tại M1 thiếu tư cách/cựu/Guest/staff | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-004 | A 2 | Ảnh/tệp hoặc tin trống/chỉ trắng hoặc hơn 1.000 từ | SC-M16-004/E1/E2/E3 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-004 | A 3 | Đã gửi 30 tin trong cửa sổ trượt của cùng cuộc | SC-M16-004/E4 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-004 | A 4 | Người nhận 1-1 đã DELETED | SC-M16-004/E5 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-005 | A 1 | Không phải người gửi hoặc tin đã thu hồi | SC-M16-005/E3/E4 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-005 | A 2 | Đã quá 5 phút | SC-M16-005/E2 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-006 | A 1 | Cửa sổ ẩn hoặc đang cuộn lên đọc cũ khi nhận tin mới | SC003/E2/E3/E4 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-006 | A 2 | Ứng viên không mới hơn mốc đã có | SC003/M4, N3 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-007 | A 1 | Không có tin trong cuộc | SC001/M2 và SC003/E1 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-007 | A 2 | Người đang xem là người duy nhất khác sender đã đọc | SC003/E6, N7 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-008 | A 1 | Guest hoặc không qua UC018 | SC-M16-006/E8/E6/E7 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-008 | A 2 | Tên trống/quá 100 ký tự sau trim hoặc tổng dưới 3/trên 100 | SC-M16-006/E1/E2/E3 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-008 | A 3 | Người được chọn bị ban/vô hiệu hóa/đã xóa | SC-M16-006/E4/GAP001 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-009 | A 1 | Ngoài nhóm, kể cả cựu/Guest/Mod/Admin hệ thống | SC-M16-007/E tại M1 thiếu tư cách/cựu | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-009 | A 2 | Đã là thành viên hoặc tài khoản đích ban/vô hiệu hóa/đã xóa | SC-M16-007/E2/E3 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-009 | A 3 | Nhánh vào ngay nhưng nhóm đã đủ 100 | SC-M16-007/E4/GAP004 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-010 | A 1 | Người gọi không là thành viên hiện tại | SC-M16-008/E tại M1 thiếu tư cách/cựu | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-011 | A 1 | Guest mở link | SC-M16-009/E10 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-011 | A 2 | Nhóm đã đủ 100 hoặc có yêu cầu gia nhập Chờ duyệt | SC-M16-009/E2/E3 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-011 | A 3 | Tài khoản thay đổi trạng thái hoặc đã là thành viên do một đường khác | SC-M16-009/GAP004, N8 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-012 | A 1 | Member/người ngoài/cựu hoặc staff không có vai trò Admin nhóm chat | SC-M16-010/E tại M1 Member/cựu | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-012 | A 2 | Bản ghi không còn Chờ duyệt | SC-M16-010/E2 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-012 | A 3 | Nhóm đủ 100 khi chấp nhận | SC-M16-010/E3 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-013 | A 1 | Member hoặc ngoài nhóm yêu cầu đổi | SC-M16-011/E tại M1 Member/cựu | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-013 | A 2 | Không có người chờ hoặc không đủ chỗ cho tất cả | SC-M16-011/E2/E3/E4 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-014 | A 1 | Member hoặc ngoài nhóm/cựu/staffkhông có quyền Admin nhóm chat | SC-M16-012/E tại M1 Member/cựu | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-015 | A 1 | Ngoài nhóm/cựu/Guest/Mod/Admin hệ thống không có membership | SC-M16-013/E tại M1 ngoài/cựu | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-015 | A 2 | Tên sau trim trống hoặc hơn 100 ký tự | SC-M16-013/E1 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-016 | A 1 | Member hoặc người ngoài nhóm yêu cầu chuyển | SC-M16-014/E tại M1 Member/cựu | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-016 | A2 | Đích không là Member của nhóm | SC-M16-014/E1/GAP006 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-017 | A 1 | Admin còn thành viên khác và chưa chuyển quyền | SC-M16-015/E3 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-017 | A 2 | Admin là thành viên cuối | SC-M16-015/E4 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-018 | A 1 | Chưa đăng nhập/BANNED hoặc phiên tài khoản không còn hợp lệ | E tại M1 Guest/E BANNED/N2 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-018 | A 2 | Chat tắt với người không ADMIN hệ thống | E cờ/N2 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-018 | A 3 | Không có membership/vai trò đúng thao tác | E tại M1 thiếu tư cách/cựu/staff | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-019 | A 1 | Đã là thành viên hoặc người đích không hợp lệ | SC007/E2/E3, N8, GAP004 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-019 | A 2 | Đã đủ 100 | SC007/E4, SC010/E3, SC011/M2 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-020 | A 1 | Hàng chờ rỗng | SC011/E3 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-020 | A 2 | Nhóm 98 thành viên, 5 người chờ hợp lệ | SC011/M2 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |
| UC-M16-020 | A 3 | Thời điểm chờ bằng nhau, pending trùng/người đã vào hoặc tài khoản không còn hợp lệ | GAP004, N10 | Giữ guard nguồn và kết quả, GAP được chỉ rõ khi nguồn chưa đủ |


| Lớp/vòng lặp | Đường khả thi | Ranh giới và tổ hợp |
|---|---|---|
| Hộp thư/lịch sử | SC002 M1–M4, SC003 M1–M6 | Chu kỳ20, actor chọn tải thêm khi còn dữ liệu, dừng khi hết hoặc không yêu cầu. Chưa có tin trả rỗng, nhóm rỗng riêng GAP002 |
| Mở/gửi/thu hồi với trạng thái tài khoản | SC001/E1/E3, SC004/E5/E6, SC005/E | Đã có cuộc khác chưa có cuộc, DELETED khác BANNED/DEACTIVATED, sender khác người nhận. Tài khoản không ACTIVE trong nhóm vẫn tính cap |
| Cửa sổ/vị trí/mốc | SC003/E2–E5 và N3/N7 | Hiện+cuối ghi, ẩn hoãn, hiện+đọc cũ vẫn hoãn, quay về cuối mới ghi. Candidate cũ giữ mốc. Receipt phụ thuộc sender/viewer khác nhau |
| Cờ và quyền | E cờ/BANNED, E tại M1 ADMIN/Guest/ngoài/cựu | ADMIN qua cờ cần đủ role. BANNED dừng yêu cầu. Cờ không ngưng hạn/AUT. Giao nhau stream thay quyền chưa chốt GAP001 |
| Admission và hàng chờ | SC007/E1/E8, SC009/E1–E5, SC010/E1–E3, SC011 | Admin thêm Bật vào ngay, Member thêm Bật chờ, link full từ chối cả tạo pending. Duyệt tay full giữ chưa quyết định, bulk dư từ chối. Pending giao nhau GAP004 |
| Tạo và tên | SC006/E1–E5, SC013/E1/E2 | Tổng tính người khác nhau gồm creator, tối thiểu3 chỉ khi tạo. Tên trim1–100, trùng được. Không bảo đảm atomic khi nhiều người lỗi |
| Vòng đời Admin | SC014/M2, SC015/E3/E4, N1 | Chuyển chủ động khác tự động, Admin còn người khác chưa chuyển bị từ chối rời, Admin cuối được rời. Người không khôi phục không tự có kế nhiệm |


## 7. GAP, trạng thái và kiểm tra

| ID | Nguồn | Điều chưa rõ | Phạm vi ảnh hưởng | Mức chặn | Xử lý hiện tại |
|---|---|---|---|---|---|
| GAP-SC-M16-001 | NOTE-M16-01 / FR-M16-01.05, FR-M16-05.02, FR-M16-06.08, FR-M16-07.05, BR-M16-23, BR-M16-24 | Chưa chốt lỗi giao/ghi, gửi lại/reconnect/replay, tin cùng thời điểm, nhiều thiết bị/sự kiện đảo, mất quyền/BANNED/cờ đổi khi stream đang mở; tạo nhóm nhiều người không hợp lệ chưa có cam kết nguyên tử. | SC001–SC007, SC011, N1–N3 | Chặn khẳng định đã đủ ở các giao nhau nêu trong GAP | Không tự tạo retry/offline queue/transaction/khóa/messageID tie-break hoặc cho stale stream vượt quyền; giữ tức thời/không lùi/duy nhất mỗi cặp/100/ownership theo nghiệp vụ. Giữ hợp đồng thành công và nhánh từ chối đã chốt; xác định bảo đảm kỹ thuật/giao dịch và lỗi về phân tích/kỹ thuật, không tự thêm UI hoặc triển khai. |
| GAP-SC-M16-002 | NOTE-M16-02 / FR-M16-03.04, FR-M16-03.05, FR-M16-03.07, BR-M16-31 | Nguồn loại rõ 1-1 rỗng nhưng chưa nêu đủ nhóm mới tạo chưa có tin: trích nội dung/thời điểm/thứ tự; thứ tự khi cùng thời điểm cũng chưa chốt. | SC002 | Chặn khẳng định đã đủ ở các giao nhau nêu trong GAP | Không tự ẩn mọi nhóm rỗng, tạo tin hệ thống chào mừng, dùng thời điểm tạo thay tin cuối hoặc chọnID làm tie-break. Danh sách vẫn theo phạm vi current/former và không hiện 1-1 rỗng. Trạng thái rỗng/hình thức lỗi/dòng nhóm chưa tin cần nguồn bổ sung. |
| GAP-SC-M16-003 | NOTE-M16-03 / FR-M16-04.10, FR-M16-07.01, FR-M16-07.06, FR-M16-07.10, BR-M16-15, BR-M16-27 | Cựu chỉ đọc tới cutoff nhưng nguồn chưa quy định rõ cập nhật mốc khi họ đọc lại và cách hiển thị receipt khi tin mới nhất toàn cuộc nằm sau cutoff; danh sách người xem sau khi rời cũng chưa rõ. | SC002/SC003 và N3/N7 | Chặn khẳng định đã đủ ở các giao nhau nêu trong GAP | Không ghi mốc cựu tới tin toàn cuộc chưa được thấy, không lộ tin/avatar/hoạt động sau cutoff hoặc tự đổi định nghĩa tin mới nhất sang tin cuối cựu được thấy cho receipt. UC003 gọi UC006 cho current; cựu giữ lịch sử và unread trong phạm vi thấy được. Quy tắc mốc/receipt cho cựu cần làm rõ với M07, không tuyên bố đã chốt thuật toán. |
| GAP-SC-M16-004 | NOTE-M16-04 / FR-M16-08.03, FR-M16-08.05, FR-M16-08.07, FR-M16-08.09, FR-M16-10.03, FR-M16-16.05, FR-M16-16.06, BR-M16-33 | Chưa chốt pending trùng giữa đề nghị và join, thêm trực tiếp khi còn pending, tài khoản đổi ban/vô hiệu hóa/Deleted lúc chờ, tie thời điểm FIFO, tạo đề nghị Member khi nhóm đã 100; duyệt tay đủ 100 khác bulk tắt duyệt. | SC007/SC009/SC010/SC011, N1/N8/N10 | Chặn khẳng định đã đủ ở các giao nhau nêu trong GAP | Không mở rộng một join pending thành mọi pending hoặc tự skip/tie-break/sửa trạng thái/nhả chỗ của tài khoản không ACTIVE. FR-M16-16.05 vẫn từ chối xin qua link khi 100; bulk dư rõ Đã từ chối. Giữ limit kiểm lúc vào, không duplicate membership, FIFO/các trạng thái đã rõ. Xử lý giao nhau/hàng chờ biên cần chốt, không tự tạo rút pending/cooldown. |
| GAP-SC-M16-005 | NOTE-M16-05 / FR-M16-06.09, FR-M16-07.06, BR-M16-15, FR-M07-07.02, FR-M07-09.08 | Chưa mô tả đầy đủ receipt/hiển thị avatar của tài khoản DEACTIVATED/DELETED trong danh sách đã xem, hoặc mốc khi cựu vào lại. M07 rõ bỏ mute riêng khi rời nhưng không nói reset mốc. | SC001/SC003/SC004/SC005/SC007/SC009 và N3/N7 | Chặn khẳng định đã đủ ở các giao nhau nêu trong GAP | Không khôi phục danh tính đã xóa, tự reset mốc/read-all hoặc thay số cuộc bằng số tin. Tin thu hồi vẫn là tin cuối/readstate có thật. Dùng M01/M 02 cho danh tính được cung cấp, một mốc không lùi; quy tắc hiển thị giao nhau cần review, không tự thiết kế. |
| GAP-SC-M16-006 | NOTE-M16-06 / FR-M16-13.01, FR-M16-14.04, FR-M16-17.02, BR-M16-25, BR-M16-30 | Nguồn chỉ đòi đích chuyển quyền là Member, không nêu thêm điều kiện trạng thái; chuyển cho Member đã không khôi phục được, nhóm 0 thành viên còn link, và chạy AUT đồng thời chuyển quyền cần làm rõ. | SC014/SC015 và N1 | Chặn khẳng định đã đủ ở các giao nhau nêu trong GAP | Không tự cấm mọi Member BANNED/DEACTIVATED, xóa nhóm/link, bổ nhiệm người vào đầu tiên hoặc kế nhiệm Owner kiểu M11. Giữ tối đa 1 Admin, không tự chuyển, Member cũ còn dữ liệu; admission theo luồng thường và cổng hiện tại, giao nhau vòng đời cần nguồn quyết định. |


TBD-M16-01 / OPEN-003 giữ hoãn Block và báo cáo Chat ở MS1. TBD-M16-02 đã đóng bởi DEC-248, thu hồi là xóa mềm giữ gốc và che với mọi actor. Không có kịch bản MS1 đọc gốc tin thu hồi. Phê duyệt kết quả chưa có, đầu ra Đang soạn.

Báo cáo kiểm tra cấu trúc, đường vai trò, sơ đồ, baseline và dữ liệu nằm trong [QA-M16.md](QA-M16.md).


## Chuyển đổi ID nhánh sau QA-SC-01

Ngày 11/11/2026, các biến thể vai trò được đăng ký thành E tại M1 theo skill v1.4. Bảng này giữ ID lịch sử để đối chiếu các tài liệu đã dẫn V. Mỗi hàng ánh xạ cả nhánh và các bước cùng số thứ tự, ví dụ V1.2 sang bước .2 của E tương ứng.

| ID lịch sử | ID hiện hành | Điểm thay | Số bước | Nguồn |
| --- | --- | --- | --- | --- |
| SC-M16-001/V1 | SC-M16-001/E6 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-001/V2 | SC-M16-001/E7 | M1 | 2 | FR-M16-01.01, FR-M16-01.02, FR-M16-01.03, FR-M16-01.04, FR-M16-01.05, FR-M16-01.06, FR-M16-01.07, FR-M16-03.07, FR-M16-04.01, BR-M16-01, BR-M16-02, BR-M16-24, BR-M16-25, BR-M16-31, FR-M02-01.26, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| SC-M16-002/V1 | SC-M16-002/E6 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-002/V2 | SC-M16-002/E7 | M1 | 4 | FR-M16-03.01, FR-M16-03.02, FR-M16-03.03, FR-M16-03.04, FR-M16-03.05, FR-M16-03.06, FR-M16-03.07, FR-M16-03.08, FR-M16-07.10, BR-M16-26, BR-M16-27, BR-M16-31, FR-M07-07.02, FR-M07-07.03, FR-M16-15.04, FR-M10-12.08, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| SC-M16-003/V1 | SC-M16-003/E13 | M1 | 4 | FR-M16-04.10, FR-M16-04.01, FR-M16-07.10, BR-M16-17, BR-M16-27, FR-M16-04.02, FR-M16-04.03 |
| SC-M16-003/V2 | SC-M16-003/E14 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-003/V3 | SC-M16-003/E15 | M1 | 6 | FR-M16-04.01, FR-M16-04.02, FR-M16-04.03, FR-M16-04.04, FR-M16-04.05, FR-M16-04.06, FR-M16-04.07, FR-M16-04.08, FR-M16-04.09, FR-M16-04.10, FR-M16-04.11, FR-M16-04.12, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-12, BR-M16-17, BR-M16-19, BR-M16-26, BR-M16-27, FR-M01-13.06, FR-M01-13.07, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| SC-M16-003/V4 | SC-M16-003/E16 | M1 | 2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| SC-M16-003/V5 | SC-M16-003/E17 | M1 | 2 | FR-M16-04.08, FR-M16-05.06, FR-M16-15.04 |
| SC-M16-003/V6 | SC-M16-003/E18 | M1 | 2 | FR-M16-04.08, FR-M16-05.06, FR-M16-15.04 |
| SC-M16-004/V1 | SC-M16-004/E11 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-004/V2 | SC-M16-004/E12 | M1 | 2 | FR-M16-05.01, FR-M16-05.02, FR-M16-05.03, FR-M16-05.04, FR-M16-05.05, FR-M16-05.06, FR-M16-05.07, FR-M16-05.08, FR-M16-05.09, FR-M16-05.10, FR-M16-05.11, FR-M16-05.12, FR-M16-05.13, FR-M16-05.14, FR-M16-01.02, FR-M16-07.01, FR-M16-07.02, FR-M16-07.03, FR-M16-07.04, FR-M16-07.05, FR-M16-07.06, FR-M16-07.07, FR-M16-07.08, FR-M16-07.09, FR-M16-07.10, FR-M16-07.11, BR-M16-13, BR-M16-14, BR-M16-15, BR-M16-16, FR-M16-06.09, FR-M07-07.02, FR-M07-07.06, BR-M07-02, BR-M07-08, BR-M16-08, BR-M16-09, BR-M16-10, BR-M16-18, BR-M16-20, BR-M16-21, BR-M16-25, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| SC-M16-004/V3 | SC-M16-004/E13 | M1 | 2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| SC-M16-004/V4 | SC-M16-004/E14 | M1 | 2 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |
| SC-M16-004/V5 | SC-M16-004/E15 | M1 | 2 | FR-M16-04.08, FR-M16-05.06, FR-M16-15.04 |
| SC-M16-004/V6 | SC-M16-004/E16 | M1 | 2 | FR-M16-04.08, FR-M16-05.06, FR-M16-15.04 |
| SC-M16-005/V1 | SC-M16-005/E8 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-005/V2 | SC-M16-005/E9 | M1 | 2 | FR-M16-06.01, FR-M16-06.02, FR-M16-06.03, FR-M16-06.04, FR-M16-06.05, FR-M16-06.06, FR-M16-06.07, FR-M16-06.08, FR-M16-06.09, FR-M16-05.08, BR-M16-11, BR-M16-12, BR-M16-15, BR-M16-18, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| SC-M16-005/V3 | SC-M16-005/E10 | M1 | 2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| SC-M16-005/V4 | SC-M16-005/E11 | M1 | 2 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |
| SC-M16-006/V1 | SC-M16-006/E8 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-006/V2 | SC-M16-006/E9 | M1 | 2 | FR-M16-02.01, FR-M16-02.02, FR-M16-02.03, FR-M16-02.04, FR-M16-02.05, FR-M16-02.06, FR-M16-02.07, FR-M16-02.08, FR-M16-02.09, BR-M16-01, BR-M16-03, BR-M16-04, BR-M16-06, BR-M16-25, BR-M16-32, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| SC-M16-007/V1 | SC-M16-007/E8 | M1 | 2 | FR-M16-08.02, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| SC-M16-007/V2 | SC-M16-007/E9 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-007/V3 | SC-M16-007/E10 | M1 | 2 | FR-M16-08.01, FR-M16-08.04, FR-M16-08.05, FR-M16-08.06, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, BR-M16-01, BR-M16-03, BR-M16-06, BR-M16-25, BR-M16-28, FR-M16-02.02, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-27, BR-M16-29, FR-M07-09.08, BR-M07-08, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| SC-M16-007/V4 | SC-M16-007/E11 | M1 | 2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| SC-M16-007/V5 | SC-M16-007/E12 | M1 | 2 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |
| SC-M16-008/V1 | SC-M16-008/E3 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-008/V2 | SC-M16-008/E4 | M1 | 2 | FR-M16-08.10, FR-M16-08.11, FR-M16-08.12, FR-M16-08.13, BR-M16-29, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| SC-M16-008/V3 | SC-M16-008/E5 | M1 | 2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| SC-M16-008/V4 | SC-M16-008/E6 | M1 | 2 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |
| SC-M16-009/V1 | SC-M16-009/E10 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-009/V2 | SC-M16-009/E11 | M1 | 4 | FR-M16-16.01, FR-M16-16.02, FR-M16-16.03, FR-M16-16.04, FR-M16-16.05, FR-M16-16.06, FR-M16-16.07, FR-M16-16.08, BR-M16-06, BR-M16-28, BR-M16-29, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, BR-M16-03, BR-M16-25, BR-M16-27, FR-M07-09.08, BR-M07-08 |
| SC-M16-010/V1 | SC-M16-010/E8 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-010/V2 | SC-M16-010/E9 | M1 | 4 | FR-M16-10.01, FR-M16-10.02, FR-M16-10.03, FR-M16-10.04, FR-M16-10.05, FR-M16-10.06, FR-M16-10.07, BR-M16-03, BR-M16-05, BR-M16-06, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-16.03, FR-M16-16.08, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08 |
| SC-M16-010/V3 | SC-M16-010/E10 | M1 | 2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| SC-M16-010/V4 | SC-M16-010/E11 | M1 | 2 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |
| SC-M16-011/V1 | SC-M16-011/E7 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-011/V2 | SC-M16-011/E8 | M1 | 2 | FR-M16-09.01, FR-M16-09.02, FR-M16-09.03, FR-M16-09.04, FR-M16-02.02, FR-M16-08.05, FR-M16-08.07, FR-M16-08.08, FR-M16-08.09, FR-M16-08.13, FR-M16-10.01, FR-M16-10.03, FR-M16-10.07, FR-M16-16.03, FR-M16-16.08, BR-M16-03, BR-M16-25, BR-M16-27, BR-M16-28, BR-M16-29, FR-M07-09.08, BR-M07-08, BR-M16-06, BR-M16-33, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| SC-M16-011/V3 | SC-M16-011/E9 | M1 | 2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| SC-M16-011/V4 | SC-M16-011/E10 | M1 | 2 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |
| SC-M16-012/V1 | SC-M16-012/E3 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-012/V2 | SC-M16-012/E4 | M1 | 2 | FR-M16-11.01, FR-M16-11.02, FR-M16-11.03, FR-M16-14.03, BR-M16-03, BR-M16-05, BR-M16-27, BR-M16-28, FR-M07-09.08, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| SC-M16-012/V3 | SC-M16-012/E5 | M1 | 2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| SC-M16-012/V4 | SC-M16-012/E6 | M1 | 2 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |
| SC-M16-013/V1 | SC-M16-013/E5 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-013/V2 | SC-M16-013/E6 | M1 | 2 | FR-M16-12.01, FR-M16-12.02, FR-M16-12.03, BR-M16-05, BR-M16-29, BR-M16-32, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| SC-M16-013/V3 | SC-M16-013/E7 | M1 | 2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| SC-M16-013/V4 | SC-M16-013/E8 | M1 | 2 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |
| SC-M16-014/V1 | SC-M16-014/E4 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-014/V2 | SC-M16-014/E5 | M1 | 2 | FR-M16-13.01, FR-M16-13.02, FR-M16-13.03, FR-M16-14.02, BR-M16-04, BR-M16-05, BR-M16-07, BR-M16-25, BR-M16-30, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| SC-M16-014/V3 | SC-M16-014/E6 | M1 | 2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| SC-M16-014/V4 | SC-M16-014/E7 | M1 | 2 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |
| SC-M16-015/V1 | SC-M16-015/E3 | M1 | 2 | FR-M16-14.02, BR-M16-07, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| SC-M16-015/V2 | SC-M16-015/E4 | M1 | 2 | FR-M16-14.04, FR-M16-14.01, BR-M16-07, BR-M16-18, BR-M16-27, FR-M07-09.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.04, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-05, BR-M16-22, BR-M16-23, BR-M01-18, FR-M10-12.08, BR-M10-28 |
| SC-M16-015/V3 | SC-M16-015/E5 | M1 | 2 | FR-M16-01.03, FR-M16-02.06, FR-M16-03.02, FR-M16-16.02, BR-M16-02 |
| SC-M16-015/V4 | SC-M16-015/E6 | M1 | 2 | FR-M16-14.01, FR-M16-14.02, FR-M16-14.03, FR-M16-14.04, FR-M16-14.05, BR-M16-03, BR-M16-05, BR-M16-07, BR-M16-18, BR-M16-27, BR-M16-28, FR-M07-09.08, FR-M16-15.04, FR-M10-12.08, FR-M16-03.03, FR-M16-15.01, FR-M16-15.02, FR-M16-15.03, FR-M16-15.05, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, BR-M16-02, BR-M16-22, BR-M16-23, BR-M01-18, BR-M10-28 |
| SC-M16-015/V5 | SC-M16-015/E7 | M1 | 2 | BR-M16-05, FR-M16-04.08, FR-M16-05.06, FR-M16-08.06, FR-M16-08.12, FR-M16-09.02, FR-M16-10.04, FR-M16-11.02, FR-M16-12.02, FR-M16-13.02 |
| SC-M16-015/V6 | SC-M16-015/E8 | M1 | 2 | FR-M16-04.10, BR-M16-27, FR-M16-05.06, BR-M16-05, BR-M16-28 |
