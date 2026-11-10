# Kịch bản nghiệp vụ — M10 Admin Panel

[Vietnamese Doc] — 2026-11-10 — Skill scenarios v1.3.

Mục đích: chuyển FR + phân tích UC thành hành trình actor thực hiện chức năng với iShare đến kết quả, có dữ liệu và ngoại lệ. Dùng bảng kiểm kê để đọc theo nhóm core–sub, các SC sáu phần để đi từng đường và nguồn/truy vết để review.

**Phạm vi:** 4 UC chính + 18 UC con, 18 mapping; 15 BF/15 SC, 15 UC sở hữu SC, 3 embedded (009/014/018), 1 abstract (002), 3 aggregate (020/021/022). Giữ 9 quan hệ (7 include, 2 generalization), không extend/extension point, 5 SVG nguồn. Bốn AUT và sáu RULE giữ xử lý nền/ràng buộc, không tính BF/SC.

**Boundary:** toàn iShare là SYSTEM; M01/06/07/08/09/11/12/13/14/16 là thành phần nội bộ. Dấu ADMIN gốc nằm trên ACT-007, không actor/role thứ tư. M10 không gọi AI/email hoặc tạo scheduler; Group Mod/Owner/Admin nhóm chat không phải ADMIN hệ thống. Phiên/quyền trang chung theo M01, không mở lối cá nhân vượt bảo trì/trạng thái account; quyền M10 vẫn kiểm tại từng yêu cầu.

**Ngoài phạm vi:** sản xuất lại FR/US/UML, cấu hình API/CSDL/giao dịch, ban/cảnh cáo/xét báo cáo/khiếu nại, quản trị Topic/Tag, chi tiết sử dụng Group/Chat/Gamification, delivery M07 và AI fallback chi tiết của owner. Không thêm phong thẳng, điều kiện uy tín, khiếu nại giáng/thu hồi, tự phục hồi Mod, chỉnh hằng số/chính sách trên UI, email switch/tóm tắt riêng/cờ module khác, KPI Mod riêng, nhiều banner/hẹn giờ.

**Trạng thái:** Đang soạn để review. FR-M10 v1.4 Đã chốt, US-M10/overview Chờ duyệt; 5 GAP theo NOTE01–05 giữ nguyên giới hạn nguồn, không tự lấp bằng chính sách hay nhận đã phê duyệt. Đây là tài liệu kịch bản, không thực hiện cấp/thu hồi quyền hoặc đổi cấu hình thật.

## 1. Baseline, actor và dữ liệu

<!-- sc:document -->

| key | value |
|---|---|
| module | M10 |
| scope | ALL |
| skill_version | 1.3 |
| output_dir | docs/specs/scenarios/M10 |
| status | Đang soạn |
| completed_steps | 1, 2, 3, 4 |
| date | 2026-11-10 |
| approval_evidence | - |


| Nguồn | Version | Ngày | Trạng thái | SHA-256 |
|---|---|---|---|---|
| [docs/specs/fr/FR-M10.md](../../fr/FR-M10.md) | 1.4 | 2026-10-24 | Đã chốt | 3e1010a76db6ef4c5870f42765e669095efc8d38c202271d9b200d2da0823d2c |
| [docs/specs/us/US-M10.md](../../us/US-M10.md) | Không có version tài liệu; skill_version không là version | 2026-11-01 | Chờ duyệt | 1ea6cd46f840f4d2e36dff97723d5f58bb63dced94c87b39246e3828b3930e89 |
| [docs/specs/us/US-overview.md](../../us/US-overview.md) | 1.1 | 2026-11-02 | Chờ duyệt | c1d624b7036ea2c7a9968eaa46c482c04fa1a15e2554d536cdfc12f177e26e33 |
| [docs/specs/fr/FR-M01.md](../../fr/FR-M01.md) | 1.10 | 2026-10-24 | Đã chốt | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a |
| [docs/specs/fr/FR-M06.md](../../fr/FR-M06.md) | 1.5 | 2026-10-24 | Đã chốt | 63606046efb11356276a2c9180f53cadad76f83e2e86502ed00341d915e0b084 |
| [docs/specs/fr/FR-M07.md](../../fr/FR-M07.md) | 1.5 | 2026-10-24 | Đã chốt | 05fb18237e049e3742d06c49b824e76e238c7587e7099b8dc4a84a2e1daf4f5b |
| [docs/specs/fr/FR-M08.md](../../fr/FR-M08.md) | 1.7 | 2026-10-24 | Đã chốt | a92e6e370038af300a9ddd735414dcb2c4fbffe07c81abaaa3c92dff447c25f0 |
| [docs/specs/fr/FR-M09.md](../../fr/FR-M09.md) | 1.2 | 2026-10-24 | Đã chốt | 8ad8ae5e148c6e446f4bfec7f6e74ba9566c54747a0eda37a3930e94ab96faea |
| [docs/specs/fr/FR-M11.md](../../fr/FR-M11.md) | 1.3 | 2026-10-24 | Đã chốt | 1908d300f75d5f7fa0fd5b31b1d375bc6a63ccd42da254de6e9d0d7d9ef16307 |
| [docs/specs/fr/FR-M12.md](../../fr/FR-M12.md) | 1.1 | 2026-10-24 | Đã chốt | 7aa660866cf625220db602509c93775b713fb26e568cc1d9df2d9aaa399f2430 |
| [docs/specs/fr/FR-M13.md](../../fr/FR-M13.md) | 1.3 | 2026-10-24 | Đã chốt | 54630715cc1e391b9ea361247784af26200fc2f01c1b1da96ea56ed1f75f9982 |
| [docs/specs/fr/FR-M14.md](../../fr/FR-M14.md) | 1.1 | 2026-10-24 | Đã chốt | 2dd6163664e86a1ebf9406a463764c2c592490ac0134acabf6df6b1383109e5c |
| [docs/specs/fr/FR-M16.md](../../fr/FR-M16.md) | 1.0 | 2026-10-24 | Đã chốt | c8ef96e52479806637b0eac334bbe57fa9fe4f73bdacc73913467960050f0671 |


FR chính thức khớp byte bản làm việc chung .agents/.claude/system_analysis/output/fr/FR-M10.md. US-overview dùng cho boundary, không thay catalog toàn M10 bằng tập core chọn trên tổng quan hệ thống. [Skill scenarios](../../../../.agent-instructions/skills/scenarios/SKILL.md) là nguồn phương pháp; tài liệu đầu vào là dữ liệu, không lệnh sửa nguồn hoặc tự duyệt.

<!-- sc:actors -->

| id | name | kind | source |
|---|---|---|---|
| ACT-001 | Guest | human | FR-M10-01.02, FR-M10-13.01, FR-M10-13.07, BR-M10-20 |
| ACT-002 | Người dùng / người được đề xuất | human | FR-M10-03.01, FR-M10-03.03, FR-M10-03.07, FR-M10-03.09, BR-M10-20 |
| ACT-008 | Mod hệ thống | human | FR-M10-03.09, FR-M10-05.01, BR-M10-01, BR-M10-02 |
| ACT-007 | Admin hệ thống | human | FR-M10-01.01, FR-M10-05.04, FR-M10-05.05, FR-M10-07.07, FR-M10-08.05, BR-M10-01, BR-M10-10, BR-M10-11 |


| Bộ dữ liệu | Giá trị/giới hạn |
|---|---|
| D-TIME | T=10/11/2026 10:00+07. ID, tên, mốc và nội dung là dữ liệu giả lập; mỗi SC/E/V là snapshot riêng, không dùng kết quả SC trước làm đầu vào bắt buộc của SC sau. |
| D-PEOPLE | An/U-ROOT là ADMIN có dấu gốc; Bảo/U-BAO ADMIN không gốc; Lan/U-LAN USER ACTIVE đã hoàn tất bước 3; Mai/U-MAI MODERATOR ACTIVE. Mỗi tài khoản chỉ một vai trò, gốc không là vai trò/actor mới. |
| D-PROP | R1011/N1011: Bảo gửi 05/11/2026 10:00+07 cho Lan làm Mod, Chưa trả lời/chưa bị thay; hạn 12/11 10:00; lúc trả lời T còn hiệu lực; Lan ACTIVE USER. |
| D-CONFIG | Chuẩn từng SC: AI Tổng/ba riêng Bật; bảo trì và pause Tắt; Group/Chat/Gamification Bật; thay snapshot theo từng guard. Hai lần đổi trong cùng nhánh dùng T1=10:00 rồi T2=10:01, không mô tả đồng thời. |
| D-BANNER | TEXT=Bao tri he thong luc 22:00.; B100 hiện tại, B099 bản cũ, C1/C2 hai trình duyệt. Ký tự biên ASCII 1/200/201 không chọn đơn vị Unicode. |
| D-LOG | L1003 T−1 phút: Hệ thống/thu hồi Mod do ban/Tuấn/lý do Mất quyền Mod do ban B1003; L1002 T−2 phút: Minh/chấp nhận đề xuất Mod/Minh/lý do trống; L1001 T−3 phút: Bảo/đổi AI Search/Search/lý do trống. Đây là tập giả lập độc lập, không vai trò sau các SC trước. |


Mỗi SC/E/V là một lần chạy độc lập; guard thay dữ liệu tương ứng từ đầu. P1001/P1002 là bản mới khi gửi tại T; R1011/R1012 là bản đã gửi 05/11 dùng cho phản hồi, không lẫn thời điểm/hạn. Role trong dữ liệu là vai trò account, khác ID actor kiểu tương tác; một actor có năng lực kế thừa vẫn chịu guard. Lý do log M10 tùy chọn; dữ liệu không nhập lý do minh họa hợp lệ, không tạo trường UI bắt buộc mới.

## 2. Kiểm kê nhóm UC chi tiết

<!-- sc:decomposition -->

| core | sub | source |
|---|---|---|
| UC-M10-020 | UC-M10-001 | FR-M10-01, BR-M10-02, BR-M10-29, BR-M10-30, BR-M06-09 |
| UC-M10-020 | UC-M10-002 | FR-M10-02, FR-M10-07, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-11, BR-M10-27 |
| UC-M10-020 | UC-M10-003 | FR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27 |
| UC-M10-020 | UC-M10-004 | FR-M10-07, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-27 |
| UC-M10-020 | UC-M10-005 | FR-M10-03, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27 |
| UC-M10-020 | UC-M10-006 | FR-M10-04, BR-M10-02, BR-M10-08 |
| UC-M10-020 | UC-M10-007 | FR-M10-08, BR-M10-10, BR-M10-11 |
| UC-M10-020 | UC-M10-008 | FR-M10-05, BR-M10-10, BR-M10-25 |
| UC-M10-020 | UC-M10-009 | FR-M10-02.06, FR-M10-02.07, FR-M10-02.09, FR-M10-07.01, FR-M10-07.02, FR-M10-07.07, FR-M10-07.08, FR-M10-03.10, FR-M10-03.11, BR-M10-05, BR-M10-11, BR-M10-27 |
| UC-M10-021 | UC-M10-010 | FR-M10-09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16 |
| UC-M10-021 | UC-M10-011 | FR-M10-10, BR-M10-13, BR-M10-17 |
| UC-M10-021 | UC-M10-012 | FR-M10-11, BR-M10-13, BR-M10-18 |
| UC-M10-021 | UC-M10-013 | FR-M10-12, BR-M10-13, BR-M10-19, BR-M10-28 |
| UC-M10-021 | UC-M10-014 | FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, BR-M10-13 |
| UC-M10-022 | UC-M10-015 | FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.05, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, BR-M10-20 |
| UC-M10-022 | UC-M10-016 | FR-M10-13.02, FR-M10-13.03, BR-M10-20 |
| UC-M10-022 | UC-M10-017 | FR-M10-13.01, FR-M10-13.06, FR-M10-13.07, FR-M10-13.08, BR-M10-20 |
| UC-M10-023 | UC-M10-018 | FR-M10-15.01, FR-M10-15.02, FR-M10-15.04, FR-M10-15.05, BR-M10-02, BR-M10-23 |


<!-- sc:ucs -->

| id | treatment | scenarios | coverage | rationale | sources |
|---|---|---|---|---|---|
| UC-M10-020 | aggregate | SC-M10-001, SC-M10-002, SC-M10-003, SC-M10-004, SC-M10-005, SC-M10-006, SC-M10-007 | SC-M10-001/M2, SC-M10-002/M2, SC-M10-003/M2, SC-M10-004/M2, SC-M10-005/M2, SC-M10-006/M2, SC-M10-007/M2 | Core Summary tổng hợp các chức năng và hành vi nền, không ép làm liên tiếp. | FR-M10-01, FR-M10-02, FR-M10-03, FR-M10-04, FR-M10-05, FR-M10-06, FR-M10-07, FR-M10-08, BR-M10-01, BR-M10-02, BR-M10-05, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-25, BR-M10-27 |
| UC-M10-021 | aggregate | SC-M10-008, SC-M10-009, SC-M10-010, SC-M10-011 | SC-M10-008/M2, SC-M10-009/M2, SC-M10-010/M2, SC-M10-011/M2 | Core Summary tổng hợp các chức năng và hành vi nền, không ép làm liên tiếp. | FR-M10-09, FR-M10-10, FR-M10-11, FR-M10-12, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, BR-M10-17, BR-M10-18, BR-M10-19, BR-M10-26, BR-M10-28 |
| UC-M10-022 | aggregate | SC-M10-012, SC-M10-013, SC-M10-014 | SC-M10-012/M2, SC-M10-013/M2, SC-M10-014/M2 | Core Summary tổng hợp các chức năng và hành vi nền, không ép làm liên tiếp. | FR-M10-13, BR-M10-20, BR-M10-26 |
| UC-M10-023 | scenario | SC-M10-015 | SC-M10-015/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-14, FR-M10-15, BR-M10-02, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| UC-M10-001 | scenario | SC-M10-001 | SC-M10-001/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-01, BR-M10-02, BR-M10-29, BR-M10-30, BR-M06-09 |
| UC-M10-002 | abstract | SC-M10-002, SC-M10-003 | SC-M10-002/M2, SC-M10-003/M2 | Contract abstract được hiện thực bởi hai loại đề xuất, không có lần gửi chưa xác định loại hoặc BF thứ ba. | FR-M10-02, FR-M10-07, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-11, BR-M10-27 |
| UC-M10-003 | scenario | SC-M10-002 | SC-M10-002/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27 |
| UC-M10-004 | scenario | SC-M10-003 | SC-M10-003/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-07, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-27 |
| UC-M10-005 | scenario | SC-M10-004 | SC-M10-004/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-03, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27 |
| UC-M10-006 | scenario | SC-M10-005 | SC-M10-005/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-04, BR-M10-02, BR-M10-08 |
| UC-M10-007 | scenario | SC-M10-006 | SC-M10-006/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-08, BR-M10-10, BR-M10-11 |
| UC-M10-008 | scenario | SC-M10-007 | SC-M10-007/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-05, BR-M10-10, BR-M10-25 |
| UC-M10-009 | embedded | SC-M10-002, SC-M10-003, SC-M10-004 | SC-M10-002/M2, SC-M10-003/M2, SC-M10-004/M4 | Kiểm riêng theo ngữ cảnh gửi/chấp nhận tại caller, không tạo BF chỉ so ACTIVE/role. | FR-M10-02.06, FR-M10-02.07, FR-M10-02.09, FR-M10-07.01, FR-M10-07.02, FR-M10-07.07, FR-M10-07.08, FR-M10-03.10, FR-M10-03.11, BR-M10-05, BR-M10-11, BR-M10-27 |
| UC-M10-010 | scenario | SC-M10-008 | SC-M10-008/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16 |
| UC-M10-011 | scenario | SC-M10-009 | SC-M10-009/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-10, BR-M10-13, BR-M10-17 |
| UC-M10-012 | scenario | SC-M10-010 | SC-M10-010/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-11, BR-M10-13, BR-M10-18 |
| UC-M10-013 | scenario | SC-M10-011 | SC-M10-011/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-12, BR-M10-13, BR-M10-19, BR-M10-28 |
| UC-M10-014 | embedded | SC-M10-008, SC-M10-009, SC-M10-010, SC-M10-011 | SC-M10-008/M2, SC-M10-009/M2, SC-M10-010/M2, SC-M10-011/M2 | Lượt SYSTEM kiểm quyền/lưu bền/áp sau đổi được mở ở từng loại cấu hình, không BF chỉ lưu công tắc. | FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, BR-M10-13 |
| UC-M10-015 | scenario | SC-M10-012 | SC-M10-012/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.05, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, BR-M10-20 |
| UC-M10-016 | scenario | SC-M10-013 | SC-M10-013/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-13.02, FR-M10-13.03, BR-M10-20 |
| UC-M10-017 | scenario | SC-M10-014 | SC-M10-014/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả trọn mục tiêu; biến thể role/trạng thái/giá trị là nhánh. | FR-M10-13.01, FR-M10-13.06, FR-M10-13.07, FR-M10-13.08, BR-M10-20 |
| UC-M10-018 | embedded | SC-M10-015 | SC-M10-015/M2 | Lập tập/lọc/sắp log trong tra cứu, không BF chỉ truy xuất nội bộ. | FR-M10-15.01, FR-M10-15.02, FR-M10-15.04, FR-M10-15.05, BR-M10-02, BR-M10-23 |


| SVG nguồn | Số UC | Đối chiếu |
|---|---|---|
| C-M10 | 4 | Tập UC khớp US; không sửa/vẽ/render mới UML |
| D-M10-020 | 10 | Tập UC khớp US; không sửa/vẽ/render mới UML |
| D-M10-021 | 6 | Tập UC khớp US; không sửa/vẽ/render mới UML |
| D-M10-022 | 4 | Tập UC khớp US; không sửa/vẽ/render mới UML |
| D-M10-023 | 2 | Tập UC khớp US; không sửa/vẽ/render mới UML |


## 3. Luồng nghiệp vụ theo mục tiêu actor

<!-- sc:flows -->

| id | uc | primary | trigger | goal | completion | covered_ucs | rationale | scenario | sources |
|---|---|---|---|---|---|---|---|---|---|
| BF-M10-001 | UC-M10-001 | ACT-007 | Bảo mở quản lý người dùng, nhập mai và lọc MODERATOR. | Tra cứu người dùng và thao tác quản trị áp dụng | Trả danh sách/chi tiết đúng khớp tên, lọc vai trò và trường nguồn, cùng thao tác phù hợp; chỉ xem không đổi vai trò. Nếu chọn Xem thao tác, mở đúng nhật ký kiểm duyệt lọc Mod, không tạo KPI riêng. | UC-M10-001 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-001 | FR-M10-01.03, FR-M10-01.04, BR-M10-29, FR-M10-01.02, FR-M10-01.05, BR-M10-02, BR-M06-09, FR-M10-01.01, FR-M10-01.06, FR-M10-14.08, BR-M10-11, BR-M10-30, FR-M10-08.02, FR-M10-08.03, FR-M10-08.04, FR-M10-08.05, BR-M10-10, FR-M08-17.01, FR-M08-17.06, FR-M10-02.09, FR-M10-07.07 |
| BF-M10-002 | UC-M10-003 | ACT-007 | Bảo chọn gửi Đề xuất làm Mod cho Lan. | Gửi đề xuất nhận vai trò Mod | Đề xuất Mod mới Chưa trả lời có người gửi/nhận/mốc/hạn, một bản cùng loại hiệu lực, thông báo mới và log đúng người gửi; Lan chưa thành Mod. Mục tiêu gửi hoàn tất ở tiếp nhận đề xuất, người nhận trả lời là chức năng riêng. | UC-M10-002, UC-M10-003, UC-M10-009 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-002 | FR-M10-02.01, FR-M10-02.02, FR-M10-02.03, FR-M10-02.04, FR-M10-02.05, FR-M10-02.06, FR-M10-02.07, FR-M10-02.08, FR-M10-02.09, FR-M10-02.10, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |
| BF-M10-003 | UC-M10-004 | ACT-007 | An chọn gửi Đề xuất làm Admin cho Lan. | Gửi đề xuất nhận vai trò Admin | Đề xuất Admin mới Chưa trả lời và thông báo/log mới được lưu bởi ADMIN gốc; USER/MODERATOR nhận giữ vai trò đến chấp nhận. Chấp nhận sẽ nhận ADMIN thường, không nhận dấu gốc. | UC-M10-002, UC-M10-004, UC-M10-009 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-003 | FR-M10-07.05, FR-M10-07.01, FR-M10-07.02, FR-M10-07.06, FR-M10-07.07, FR-M10-07.08, FR-M10-07.09, FR-M10-07.10, FR-M10-07.11, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |
| BF-M10-004 | UC-M10-005 | ACT-002 | Lan mở thông báo R1011 để phản hồi. | Trả lời một đề xuất nhận vai trò của mình | Một lựa chọn hợp lệ được ghi và hiện, không trả lời lại: Chấp nhận đổi ngay một vai trò theo loại, Từ chối giữ vai trò. Không kết thúc ở chuyển lựa chọn M07 hoặc kiểm điều kiện xong. | UC-M10-005, UC-M10-009 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-004 | FR-M07-02.14, FR-M07-05.02, FR-M10-03.04, FR-M10-03.07, FR-M10-03.08, BR-M10-07, BR-M10-27, FR-M10-03.01, FR-M10-03.02, FR-M10-03.03, FR-M10-03.06, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11, BR-M10-05, BR-M10-06, FR-M07-02.28, FR-M07-02.31, FR-M07-02.32, FR-M10-14.06, FR-M10-14.08, BR-M10-01, BR-M10-21, FR-M10-07.06, FR-M10-02.10, FR-M10-02.08, FR-M07-02.30, FR-M07-05.05 |
| BF-M10-005 | UC-M10-006 | ACT-007 | Bảo chọn Giáng cấp Mai. | Giáng cấp một Mod về User | Đích MODERATOR→USER ngay, log người Admin giáng cấp, không cần đồng ý/không khiếu nại; không xóa tài khoản hoặc ban đích. | UC-M10-006 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-005 | FR-M10-04.01, FR-M10-04.02, FR-M10-04.03, FR-M10-04.04, FR-M10-04.05, FR-M10-05.06, BR-M10-02, BR-M10-08, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| BF-M10-006 | UC-M10-007 | ACT-007 | An chọn Thu hồi vai trò Admin của Bảo. | Thu hồi vai trò Admin của một Admin khác | Admin đích khác gốc về USER ngay, log đúng ADMIN gốc; không khôi phục Mod cũ, không yêu cầu đồng ý/cho khiếu nại, không thu hồi gốc. | UC-M10-007 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-006 | FR-M10-08.03, FR-M10-08.01, FR-M10-08.02, FR-M10-08.04, FR-M10-08.05, FR-M10-08.06, BR-M10-10, BR-M10-11, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, BR-M10-02 |
| BF-M10-007 | UC-M10-008 | ACT-008 | Mai chọn Từ chức vai trò của chính mình. | Tự từ chức vai trò sau xác nhận | Chính Mod/Admin không gốc về USER sau một xác nhận; log chính người từ chức. Hủy giữ role, gốc không được từ chức. | UC-M10-008 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-007 | FR-M10-05.01, FR-M10-05.02, FR-M10-05.03, FR-M10-05.05, BR-M10-10, BR-M10-25, FR-M10-05.06, FR-M10-14.06, BR-M10-21, FR-M10-05.04 |
| BF-M10-008 | UC-M10-010 | ACT-007 | Bảo đặt Search AI từ Bật sang Tắt. | Điều chỉnh AI tổng hoặc một phạm vi AI riêng | Đúng công tắc lưu bền, có hiệu lực sau đổi và log Admin; hiệu lực AI theo Tổng AND riêng, tóm tắt theo Tổng. Cách dự phòng/tạo bù thuộc owner, không khẳng định việc nền đã hoàn tất. | UC-M10-010, UC-M10-014 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-008 | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, BR-M13-07 |
| BF-M10-009 | UC-M10-011 | ACT-007 | Bảo bật chế độ bảo trì. | Bật hoặc tắt chế độ bảo trì | Bảo trì lưu/áp sau T, M01 thi hành chỉ ADMIN khi bật và bỏ rào khi tắt; log đổi công tắc có, không xóa account hoặc tự đặt logout. | UC-M10-011, UC-M10-014 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-009 | FR-M10-10.01, FR-M10-10.02, FR-M10-10.03, BR-M10-13, BR-M10-17, FR-M01-05.19, FR-M01-05.20, FR-M10-09.02, FR-M10-09.08, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| BF-M10-010 | UC-M10-012 | ACT-007 | Bảo bật tạm dừng đăng ký. | Bật hoặc tắt tạm dừng đăng ký mới | Cấu hình lưu/áp sau T, chặn tài khoản mới khi bật nhưng giữ các ngoại lệ liên kết/tiếp đăng ký; log đúng, không chặn toàn bộ đăng nhập. | UC-M10-012, UC-M10-014 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-010 | FR-M10-11.01, FR-M10-11.02, FR-M10-11.03, BR-M10-13, BR-M10-18, FR-M01-01.08, FR-M01-01.09, FR-M01-04.10, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| BF-M10-011 | UC-M10-013 | ACT-007 | Bảo tắt cờ Group. | Bật hoặc tắt cờ Group, Chat hoặc Gamification | Đúng cờ lưu/áp sau T và log; người không Admin bị chặn theo owner, lối vào/dữ liệu/việc nền/kiểm duyệt giữ, Admin qua rào cờ vẫn theo quyền; bật lại không tính bù. | UC-M10-013, UC-M10-014 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-011 | FR-M10-12.01, FR-M10-12.02, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M10-12.08, BR-M10-13, BR-M10-19, BR-M10-28, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| BF-M10-012 | UC-M10-015 | ACT-007 | Bảo nhập nội dung và yêu cầu đặt banner. | Đặt mới hoặc sửa nội dung banner toàn trang | Tối đa một banner văn bản thuần 1–200 ký tự sau trim được công bố/thay nội dung, hiện lại cho người đã đóng khi nội dung đổi/đặt mới; log Admin. Không hẹn giờ hoặc giữ nhiều banner. | UC-M10-015 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-012 | FR-M10-13.01, FR-M10-13.05, FR-M10-13.06, FR-M10-13.03, FR-M10-13.04, FR-M10-13.08, FR-M10-13.09, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, BR-M10-02 |
| BF-M10-013 | UC-M10-016 | ACT-007 | Bảo chọn Gỡ banner đang hiện. | Gỡ banner cho toàn hệ thống | Banner Không hiện toàn trang, log gỡ của Admin có; không gán đây là đóng cá nhân hoặc chính sách xóa lịch sử. | UC-M10-016 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-013 | FR-M10-13.02, FR-M10-13.03, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, BR-M10-02 |
| BF-M10-014 | UC-M10-017 | ACT-001 | Guest mở một trang iShare được phép xem. | Xem và đóng riêng banner hiện tại | Banner được hiển thị hoặc không hiển thị đúng bản/người xem; nếu đóng thì bản ấy không hiện lại trong phạm vi nguồn, người khác không bị ảnh hưởng, bản đổi nội dung/đặt mới hiện lại. Guest phạm vi trình duyệt; lưu/đồng bộ người đăng nhập chưa chốt GAP002. | UC-M10-017 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-014 | FR-M10-13.01, FR-M10-13.06, FR-M10-13.07, FR-M10-14.08, BR-M10-20, FR-M10-13.08, FR-M10-13.02 |
| BF-M10-015 | UC-M10-023 | ACT-007 | Bảo mở nhật ký thao tác Admin, chưa chọn tiêu chí. | Tra cứu nhật ký thao tác Admin theo tiêu chí | Danh sách đúng quyền/tiêu chí, mới nhất trước, đủ năm trường và giờ Việt Nam được trả chỉ đọc; không tạo log đọc/lọc, không sửa/xóa bản ghi. | UC-M10-018, UC-M10-023 | Actor yêu cầu một chức năng và nhận kết quả hoàn tất; không tách theo Bật/Tắt, lỗi hoặc role người khởi tạo. | SC-M10-015 | FR-M10-15.01, FR-M10-15.04, FR-M10-15.02, FR-M10-15.05, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-02, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M10-15.03 |


Gửi Mod/Admin là hai lời mời được quản lý độc lập: vai trò/trách nhiệm đích khác, mỗi loại có hồ sơ/thông báo/vòng đời riêng và có thể đồng thời hiệu lực cho cùng một người (BR27). Chỉ gốc gửi Admin là guard, không phải lý do duy nhất tách; không tạo thêm BF gửi abstract hoặc ghép người nhận phản hồi vào phiên gửi. Phản hồi một đề xuất là chức năng riêng; Chấp nhận/Từ chối và loại role là nhánh.

Giáng Mod, thu hồi Admin và tự từ chức có người quyết định/đối tượng/ràng buộc riêng nên là ba chức năng. Bốn loại công tắc có mục đích vận hành khác, còn Bật/Tắt/tên riêng là dữ liệu nhánh. Đặt/Sửa banner cùng chức năng công bố một nội dung duy nhất, khác trạng thái đầu; gỡ toàn trang và đóng cá nhân là mục tiêu khác. Không tạo BF khởi tạo/đếm hạn/thu hồi do ban/ghi log.

| Quan hệ US giữ nguyên | Điểm chèn/contract nguồn | Trở về nguồn |
|---|---|---|
| UC-M10-003 generalization UC-M10-002 | #uc-m10-002-contract | - |
| UC-M10-004 generalization UC-M10-002 | #uc-m10-002-contract | - |
| UC-M10-002 include UC-M10-009 | #uc-m10-002-main-1 | #uc-m10-002-main-2 |
| UC-M10-005 include UC-M10-009 | #uc-m10-005-main-3 | #uc-m10-005-main-4 |
| UC-M10-010 include UC-M10-014 | #uc-m10-010-main-2 | #uc-m10-010-main-3 |
| UC-M10-011 include UC-M10-014 | #uc-m10-011-main-2 | #uc-m10-011-main-3 |
| UC-M10-012 include UC-M10-014 | #uc-m10-012-main-2 | #uc-m10-012-main-3 |
| UC-M10-013 include UC-M10-014 | #uc-m10-013-main-2 | #uc-m10-013-main-3 |
| UC-M10-023 include UC-M10-018 | #uc-m10-023-main-2 | #uc-m10-023-main-3 |


UC003/004 kế thừa contract UC002 và mở kiểm UC009 tại lượt SYSTEM trước thay/lưu bản mới; UC005 chỉ chèn UC009 trên nhánh Chấp nhận. UC010–013 mở UC014 đầy đủ kiểm quyền/lưu bền/áp sau đổi rồi trả hiệu lực đúng loại; core023 mở UC018 trước trả danh sách. Không bắt chạy hai chuyên biệt liên tiếp hoặc tạo include từ gửi tới trả lời. Nhánh Xem thao tác trả đúng nhật ký M08 đã lọc theo Mod, không dừng ở URL hoặc dựng chức năng KPI mới; [UC-M08-025](../../us/US-M08.md#uc-m08-025) giữ owner nhật ký kiểm duyệt.

## 4. Scenario sáu phần

<a id="sc-m10-001"></a>

<!-- sc:scenario SC-M10-001 -->

### SC-M10-001

#### 1. Tên kịch bản chuẩn

Tra cứu người dùng và thao tác quản trị áp dụng — BF-M10-001; owner [UC-M10-001](../../us/US-M10.md#uc-m10-001).

#### 2. Actor thực hiện

ACT-007 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Có yêu cầu tìm/lọc; phiên và quyền ADMIN kiểm trong luồng. Chuẩn Bảo Admin thường tìm Mai; chỉ dùng tập ACTIVE giả lập để minh họa, không tự đặt bộ lọc ACTIVE/xong bước 3 hoặc tập đầy đủ DELETED (GAP005).

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-001 -->

| result | condition |
|---|---|
| SUCCESS | Trả danh sách/chi tiết đúng khớp tên, lọc vai trò và trường nguồn, cùng thao tác phù hợp; chỉ xem không đổi vai trò. Nếu chọn Xem thao tác, mở đúng nhật ký kiểm duyệt lọc Mod, không tạo KPI riêng. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không có thay đổi được yêu cầu thành công. Hiệu ứng hợp lệ đã có được giữ; không tự ghi nhận thao tác thành công, xóa hồ sơ, rollback hoặc cấp quyền mới. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-001 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | Bảo mở quản lý người dùng, nhập mai và lọc MODERATOR. | query=mai; role=MODERATOR; tập mẫu có Mai Nguyen/mai.nguyen và Lan/lan USER | M2 | FR-M10-01.03, FR-M10-01.04, BR-M10-29 |
| M2 | SYSTEM | Hệ thống kiểm ADMIN; tìm theo username/tên hiển thị, chuỗi ở bất kỳ vị trí, không phân biệt hoa/thường và dấu, khớp sai nhẹ theo M06, kết quả giống hơn trước; áp lọc MODERATOR. Trả trường nguồn, không lấy giới hạn 3/debounce hay tập công khai M06 sang quản trị. | Mai Nguyen; username=mai.nguyen; MODERATOR; ACTIVE; không nhãn gốc | M3 | FR-M10-01.02, FR-M10-01.03, FR-M10-01.04, FR-M10-01.05, BR-M10-02, BR-M10-29, BR-M06-09 |
| M3 | ACT-007 | Bảo chọn Mai để xem thao tác vai trò áp dụng. | target=U-MAI MODERATOR; Bảo ADMIN không gốc | M4 | FR-M10-01.01 |
| M4 | SYSTEM | Hệ thống kiểm quyền/ngữ cảnh target hiện tại, trả thao tác giáng cấp Mod và lối Xem thao tác theo nhật ký M08; không phong vai trò hoặc giáng cấp chỉ vì chọn người. Quyền gốc mới có thêm khả năng đề xuất/thu hồi Admin theo đúng target. | Mai vẫn MODERATOR; Bảo không có quyền gửi/thu hồi Admin; không ghi log Admin cho việc xem | END:SUCCESS | FR-M10-01.01, FR-M10-01.05, FR-M10-01.06, FR-M10-14.08, BR-M10-02, BR-M10-11, BR-M10-29, BR-M10-30 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-001 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Không có tài khoản khớp tên và vai trò trong tập được tra cứu | E1.1 | FR-M10-01.02, FR-M10-01.03, FR-M10-01.04, FR-M10-01.05, BR-M10-29, BR-M06-09 |
| E2 | user-choice | M1 | An ADMIN gốc tìm Admin và chọn một người để xem khả năng thu hồi | E2.1 | FR-M10-01.03, FR-M10-01.04, BR-M10-29, FR-M10-01.02, FR-M10-01.05, BR-M06-09, FR-M10-01.01, FR-M10-08.02, FR-M10-08.03, FR-M10-08.04, FR-M10-08.05, FR-M10-14.08, BR-M10-10, BR-M10-11 |
| E3 | user-choice | M3 | Bảo chọn Xem thao tác của Mai thay vì thao tác đổi role | E3.1 | FR-M10-01.06, BR-M10-30, FR-M08-17.01, FR-M08-17.06 |
| E4 | user-choice | M1 | Bảo lọc USER, chọn Lan và nhận thao tác đề xuất Mod phù hợp | E4.1 | FR-M10-01.03, FR-M10-01.04, BR-M10-29, FR-M10-01.02, FR-M10-01.05, BR-M06-09, FR-M10-01.01, FR-M10-02.09, FR-M10-07.07, FR-M10-14.08, BR-M10-11 |
| E5 | user-choice | M1 | Bảo chỉ lọc ADMIN và xem nhãn gốc trong tập năm Admin giả lập | E5.1 | FR-M10-01.03, FR-M10-01.04, BR-M10-29, FR-M10-01.02, FR-M10-01.05, FR-M10-01.01, FR-M10-08.04, FR-M10-08.05, FR-M10-14.08, BR-M10-10, BR-M10-11 |


<!-- sc:branch SC-M10-001 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm ADMIN, áp cách khớp M06 và lọc vai trò rồi trả danh sách rỗng; không gán thêm trạng thái lọc hoặc tạo tài khoản. | query=zzq_nomatch; role=MODERATOR; results=[] | END:SUCCESS | FR-M10-01.02, FR-M10-01.03, FR-M10-01.04, FR-M10-01.05, BR-M10-29, BR-M06-09 |


<!-- sc:branch SC-M10-001 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-007 | An tìm bao và lọc ADMIN trong quản lý người dùng. | An ADMIN gốc; Bảo ADMIN không gốc | E2.2 | FR-M10-01.03, FR-M10-01.04, BR-M10-29 |
| E2.2 | SYSTEM | Hệ thống kiểm ADMIN và tìm/lọc đúng tên, trả username/tên/role/trạng thái, gắn nhãn gốc cho An nếu kết quả có An; không giới hạn theo tìm công khai. | Bảo/bao.admin/ADMIN/ACTIVE, không gốc | E2.3 | FR-M10-01.02, FR-M10-01.03, FR-M10-01.04, FR-M10-01.05, BR-M10-29, BR-M06-09 |
| E2.3 | ACT-007 | An chọn Bảo để xem thao tác áp dụng. | An gốc, target Bảo ADMIN không gốc | E2.4 | FR-M10-01.01 |
| E2.4 | SYSTEM | Hệ thống trả khả năng Thu hồi Admin cho An theo đúng loại đích; không dùng Giáng cấp Mod cho Admin hoặc đổi role chỉ vì chọn. Điều kiện phải kiểm lại lúc thực hiện thao tác. | Bảo vẫn ADMIN; gốc có quyền riêng, không ghi log vì xem | END:SUCCESS | FR-M10-01.01, FR-M10-08.02, FR-M10-08.03, FR-M10-08.04, FR-M10-08.05, FR-M10-14.08, BR-M10-10, BR-M10-11 |


<!-- sc:branch SC-M10-001 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-007 | Bảo chọn Xem thao tác của Mai. | U-MAI MODERATOR đã chọn; actor Bảo ADMIN | E3.2 | FR-M10-01.06 |
| E3.2 | SYSTEM | Hệ thống kiểm quyền Admin đối với nhật ký kiểm duyệt M08, mở và trả tập được lọc người làm=Mai, có người làm/thao tác/target/lý do/thời điểm. Không tạo màn/chỉ số hiệu suất mới hoặc dùng nhật ký Admin thay nhật ký kiểm duyệt. | Filter Mai; dòng mẫu Mai/ẩn P88/Quấy rối/T−1 ngày; chỉ thao tác Mai trong snapshot, chưa giáng cấp | END:SUCCESS | FR-M10-01.06, BR-M10-30, FR-M08-17.01, FR-M08-17.06 |


<!-- sc:branch SC-M10-001 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-007 | Bảo tìm lan và lọc USER. | Bảo ADMIN không gốc; Lan USER ACTIVE SETUP_COMPLETED | E4.2 | FR-M10-01.03, FR-M10-01.04, BR-M10-29 |
| E4.2 | SYSTEM | Hệ thống kiểm ADMIN, tìm/lọc đúng tên và trả đủ trường của Lan; chưa gọi bộ kiểm gửi đề xuất hoặc đổi role. | username=lan; tên Lan; USER; ACTIVE; không nhãn gốc | E4.3 | FR-M10-01.02, FR-M10-01.03, FR-M10-01.04, FR-M10-01.05, BR-M10-29, BR-M06-09 |
| E4.3 | ACT-007 | Bảo chọn Lan để xem thao tác áp dụng. | Bảo không gốc, Lan USER | E4.4 | FR-M10-01.01 |
| E4.4 | SYSTEM | Hệ thống trả khả năng Đề xuất làm Mod; gửi thật vẫn phải kiểm đủ điều kiện khi thực hiện. Không cấp quyền Đề xuất Admin cho Bảo hoặc phong Mod chỉ vì chọn. | Lan vẫn USER; Bảo không gốc; không log vì xem | END:SUCCESS | FR-M10-01.01, FR-M10-02.09, FR-M10-07.07, FR-M10-14.08, BR-M10-11 |


<!-- sc:branch SC-M10-001 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-007 | Bảo mở quản lý người dùng và lọc ADMIN, không đưa chuỗi tên. | Tập mẫu: An, Bảo, Chi, Dũng, Em đều ADMIN ACTIVE; chỉ An gốc | E5.2 | FR-M10-01.03, FR-M10-01.04, BR-M10-29 |
| E5.2 | SYSTEM | Hệ thống kiểm ADMIN, áp lọc và trả đủ năm tài khoản trong tập mẫu này, không tự chặn ở ba như tìm công khai M06. Mỗi dòng có username/tên/role/ACTIVE; An hiện nhãn gốc, các dòng khác không gốc. Không khẳng định giới hạn/phân trang hoặc tập trạng thái DELETED. | an.root/An/ADMIN/ACTIVE/gốc; bao.admin/Bảo/ADMIN/ACTIVE; chi.admin/Chi/ADMIN/ACTIVE; dung.admin/Dũng/ADMIN/ACTIVE; em.admin/Em/ADMIN/ACTIVE | E5.3 | FR-M10-01.02, FR-M10-01.04, FR-M10-01.05, BR-M10-29 |
| E5.3 | ACT-007 | Bảo chọn An gốc để xem quyền áp dụng. | Actor Bảo ADMIN không gốc; target An ADMIN gốc | E5.4 | FR-M10-01.01 |
| E5.4 | SYSTEM | Hệ thống không cung cấp khả năng thu hồi/giáng Mod áp lên An gốc; giữ thông tin chỉ đọc, không đổi role hoặc ghi log xem. Quy tắc bảo vệ gốc vẫn áp khi có yêu cầu trực tiếp. | An giữ ADMIN gốc; Bảo không được thu hồi Admin; không phát sinh thay đổi role | END:SUCCESS | FR-M10-01.01, FR-M10-08.04, FR-M10-08.05, FR-M10-14.08, BR-M10-10, BR-M10-11 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-001 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Người yêu cầu chọn tra cứu người dùng và thao tác quản trị áp dụng. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V1.2 | FR-M10-01.02, BR-M10-02 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-01.02, BR-M10-02 |


**V2 — thay toàn bộ M1 đến kết thúc:** User thường. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-001 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-002 | Người yêu cầu chọn tra cứu người dùng và thao tác quản trị áp dụng. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V2.2 | FR-M10-01.02, BR-M10-02 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-01.02, BR-M10-02 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mod hệ thống (kể cả Owner/Group Mod/Admin nhóm chat nhưng không ADMIN hệ thống). Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-001 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-008 | Người yêu cầu chọn tra cứu người dùng và thao tác quản trị áp dụng. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V3.2 | FR-M10-01.02, BR-M10-02 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-01.02, BR-M10-02 |


<!-- sc:end SC-M10-001 -->

<a id="sc-m10-002"></a>

<!-- sc:scenario SC-M10-002 -->

### SC-M10-002

#### 1. Tên kịch bản chuẩn

Gửi đề xuất nhận vai trò Mod — BF-M10-002; owner [UC-M10-003](../../us/US-M10.md#uc-m10-003).

#### 2. Actor thực hiện

ACT-007 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Có người nhận được chọn; không giả đủ điều kiện trước kiểm. Chuẩn Bảo ADMIN không gốc, Lan USER ACTIVE/xong bước 3, chưa có đề xuất Mod hiệu lực, 0 điểm và tài khoản mới vẫn hợp lệ.

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-002 -->

| result | condition |
|---|---|
| SUCCESS | Đề xuất Mod mới Chưa trả lời có người gửi/nhận/mốc/hạn, một bản cùng loại hiệu lực, thông báo mới và log đúng người gửi; Lan chưa thành Mod. Mục tiêu gửi hoàn tất ở tiếp nhận đề xuất, người nhận trả lời là chức năng riêng. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không có thay đổi được yêu cầu thành công. Hiệu ứng hợp lệ đã có được giữ; không tự ghi nhận thao tác thành công, xóa hồ sơ, rollback hoặc cấp quyền mới. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-002 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | Bảo chọn gửi Đề xuất làm Mod cho Lan. | U-BAO ADMIN; U-LAN USER ACTIVE SETUP_COMPLETED, 0 điểm; không lý do bắt buộc | M2 | FR-M10-02.01 |
| M2 | SYSTEM | Hệ thống kiểm hiện tại: người gửi ADMIN, người nhận USER đang ACTIVE/xong bước 3; không kiểm điểm, uy tín hoặc thâm niên. Không có bản cùng loại cần thay. Lưu P1001 mới Chưa trả lời, loại Mod, người gửi Bảo, người nhận Lan, gửi T, hạn T+7×24h; giữ vai trò USER của người nhận. Cung cấp M07 sự kiện Đề xuất làm Mod và N1001 mới với Chấp nhận/Từ chối, trả đã gửi; chưa phong vai trò hoặc đợi câu trả lời. Ghi thêm nhật ký Admin: người làm Bảo, thao tác gửi đề xuất Mod, đối tượng Lan, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | P1001/N1001; Lan vẫn USER; gửi 10/11 10:00, hạn 17/11 10:00+07; tối đa 1 bản hiệu lực mỗi loại/người; lý do không bắt buộc | END:SUCCESS | FR-M10-02.01, FR-M10-02.02, FR-M10-02.03, FR-M10-02.04, FR-M10-02.05, FR-M10-02.06, FR-M10-02.07, FR-M10-02.08, FR-M10-02.09, FR-M10-02.10, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-002 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Có bản cùng loại cũ Chưa trả lời; người gửi/nhận vẫn đủ điều kiện | E1.1 | FR-M10-02.01, FR-M10-02.02, FR-M10-02.03, FR-M10-02.04, FR-M10-02.05, FR-M10-02.06, FR-M10-02.07, FR-M10-02.08, FR-M10-02.09, FR-M10-02.10, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |
| E2 | system | M2 | Có bản cùng loại cũ Đã từ chối; người gửi/nhận vẫn đủ điều kiện | E2.1 | FR-M10-02.01, FR-M10-02.02, FR-M10-02.03, FR-M10-02.04, FR-M10-02.05, FR-M10-02.06, FR-M10-02.07, FR-M10-02.08, FR-M10-02.09, FR-M10-02.10, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |
| E3 | system | M2 | Có bản cùng loại cũ Hết hiệu lực; người gửi/nhận vẫn đủ điều kiện | E3.1 | FR-M10-02.01, FR-M10-02.02, FR-M10-02.03, FR-M10-02.04, FR-M10-02.05, FR-M10-02.06, FR-M10-02.07, FR-M10-02.08, FR-M10-02.09, FR-M10-02.10, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |
| E4 | system | M2 | Đang có đề xuất loại còn lại cho cùng Lan; hai loại không thay nhau | E4.1 | FR-M10-02.01, FR-M10-02.02, FR-M10-02.03, FR-M10-02.04, FR-M10-02.05, FR-M10-02.06, FR-M10-02.07, FR-M10-02.08, FR-M10-02.09, FR-M10-02.10, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |
| E5 | system | M2 | Người nhận không ACTIVE: DEACTIVATED | E5.1 | FR-M10-02.09, BR-M10-05 |
| E6 | system | M2 | Người nhận không ACTIVE: BANNED | E6.1 | FR-M10-02.09, BR-M10-05 |
| E7 | system | M2 | Người nhận không ACTIVE: DELETED | E7.1 | FR-M10-02.09, BR-M10-05 |
| E8 | system | M2 | Người nhận chưa hoàn tất bước 3 | E8.1 | FR-M10-02.09, BR-M10-05 |
| E9 | system | M2 | Đích sai vai trò cho loại đề xuất | E9.1 | FR-M10-02.07, BR-M10-27 |


<!-- sc:branch SC-M10-002 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm hiện tại: người gửi ADMIN, người nhận USER đang ACTIVE/xong bước 3; không kiểm điểm, uy tín hoặc thâm niên. Sau khi kiểm đạt, chuyển P0991 cùng loại/cùng người gửi 05/11 10:00, đang hiệu lực đến trước 12/11 10:00, sang Hết hiệu lực TRƯỚC lưu bản mới; thông báo cũ không trả lời được, không gán nhãn Đã hết hạn cho nguyên nhân bị thay. Lưu P1001 mới Chưa trả lời, loại Mod, người gửi Bảo, người nhận Lan, gửi T, hạn T+7×24h; giữ vai trò USER của người nhận. Cung cấp M07 sự kiện Đề xuất làm Mod và N1001 mới với Chấp nhận/Từ chối, trả đã gửi; chưa phong vai trò hoặc đợi câu trả lời. Ghi thêm nhật ký Admin: người làm Bảo, thao tác gửi đề xuất Mod, đối tượng Lan, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | P1001/N1001; Lan vẫn USER; gửi 10/11 10:00, hạn 17/11 10:00+07; tối đa 1 bản hiệu lực mỗi loại/người; lý do không bắt buộc | END:SUCCESS | FR-M10-02.01, FR-M10-02.02, FR-M10-02.03, FR-M10-02.04, FR-M10-02.05, FR-M10-02.06, FR-M10-02.07, FR-M10-02.08, FR-M10-02.09, FR-M10-02.10, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |


<!-- sc:branch SC-M10-002 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống kiểm hiện tại: người gửi ADMIN, người nhận USER đang ACTIVE/xong bước 3; không kiểm điểm, uy tín hoặc thâm niên. Giữ nguyên bản cùng loại cũ Đã từ chối, tạo bản mới, không mở lại bản cũ. Lưu P1001 mới Chưa trả lời, loại Mod, người gửi Bảo, người nhận Lan, gửi T, hạn T+7×24h; giữ vai trò USER của người nhận. Cung cấp M07 sự kiện Đề xuất làm Mod và N1001 mới với Chấp nhận/Từ chối, trả đã gửi; chưa phong vai trò hoặc đợi câu trả lời. Ghi thêm nhật ký Admin: người làm Bảo, thao tác gửi đề xuất Mod, đối tượng Lan, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | P1001/N1001; Lan vẫn USER; gửi 10/11 10:00, hạn 17/11 10:00+07; tối đa 1 bản hiệu lực mỗi loại/người; lý do không bắt buộc | END:SUCCESS | FR-M10-02.01, FR-M10-02.02, FR-M10-02.03, FR-M10-02.04, FR-M10-02.05, FR-M10-02.06, FR-M10-02.07, FR-M10-02.08, FR-M10-02.09, FR-M10-02.10, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |


<!-- sc:branch SC-M10-002 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống kiểm hiện tại: người gửi ADMIN, người nhận USER đang ACTIVE/xong bước 3; không kiểm điểm, uy tín hoặc thâm niên. Giữ nguyên bản cùng loại cũ Hết hiệu lực, tạo bản mới, không mở lại bản cũ. Lưu P1001 mới Chưa trả lời, loại Mod, người gửi Bảo, người nhận Lan, gửi T, hạn T+7×24h; giữ vai trò USER của người nhận. Cung cấp M07 sự kiện Đề xuất làm Mod và N1001 mới với Chấp nhận/Từ chối, trả đã gửi; chưa phong vai trò hoặc đợi câu trả lời. Ghi thêm nhật ký Admin: người làm Bảo, thao tác gửi đề xuất Mod, đối tượng Lan, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | P1001/N1001; Lan vẫn USER; gửi 10/11 10:00, hạn 17/11 10:00+07; tối đa 1 bản hiệu lực mỗi loại/người; lý do không bắt buộc | END:SUCCESS | FR-M10-02.01, FR-M10-02.02, FR-M10-02.03, FR-M10-02.04, FR-M10-02.05, FR-M10-02.06, FR-M10-02.07, FR-M10-02.08, FR-M10-02.09, FR-M10-02.10, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |


<!-- sc:branch SC-M10-002 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống kiểm hiện tại: người gửi ADMIN, người nhận USER đang ACTIVE/xong bước 3; không kiểm điểm, uy tín hoặc thâm niên. Không có bản cùng loại cần thay. Giữ đề xuất loại còn lại độc lập. Lưu P1001 mới Chưa trả lời, loại Mod, người gửi Bảo, người nhận Lan, gửi T, hạn T+7×24h; giữ vai trò USER của người nhận. Cung cấp M07 sự kiện Đề xuất làm Mod và N1001 mới với Chấp nhận/Từ chối, trả đã gửi; chưa phong vai trò hoặc đợi câu trả lời. Ghi thêm nhật ký Admin: người làm Bảo, thao tác gửi đề xuất Mod, đối tượng Lan, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | P1001/N1001; Lan vẫn USER; gửi 10/11 10:00, hạn 17/11 10:00+07; tối đa 1 bản hiệu lực mỗi loại/người; lý do không bắt buộc | END:SUCCESS | FR-M10-02.01, FR-M10-02.02, FR-M10-02.03, FR-M10-02.04, FR-M10-02.05, FR-M10-02.06, FR-M10-02.07, FR-M10-02.08, FR-M10-02.09, FR-M10-02.10, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |


<!-- sc:branch SC-M10-002 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống kiểm người nhận trước thay bản cũ, từ chối gửi; không tạo đề xuất/thông báo/log gửi thành công hoặc tự đổi hiệu lực bản cũ. | Lan DEACTIVATED; role USER; mọi bản cũ vẫn theo vòng đời trước đó | END:REJECTED | FR-M10-02.09, BR-M10-05 |


<!-- sc:branch SC-M10-002 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống kiểm người nhận trước thay bản cũ, từ chối gửi; không tạo đề xuất/thông báo/log gửi thành công hoặc tự đổi hiệu lực bản cũ. | Lan BANNED; role USER; mọi bản cũ vẫn theo vòng đời trước đó | END:REJECTED | FR-M10-02.09, BR-M10-05 |


<!-- sc:branch SC-M10-002 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống kiểm người nhận trước thay bản cũ, từ chối gửi; không tạo đề xuất/thông báo/log gửi thành công hoặc tự đổi hiệu lực bản cũ. | Lan DELETED; role USER; mọi bản cũ vẫn theo vòng đời trước đó | END:REJECTED | FR-M10-02.09, BR-M10-05 |


<!-- sc:branch SC-M10-002 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống từ chối gửi trước khi thay/lưu đề xuất; không bổ sung điều kiện điểm hay thâm niên. | Lan ACTIVE nhưng mới xong bước 1 hoặc 2 | END:REJECTED | FR-M10-02.09, BR-M10-05 |


<!-- sc:branch SC-M10-002 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống từ chối gửi cho vai trò không hợp lệ; không tự hạ role đích để gửi. | Target MODERATOR hoặc ADMIN | END:REJECTED | FR-M10-02.07, BR-M10-27 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-002 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Người yêu cầu chọn gửi đề xuất nhận vai trò mod. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V1.2 | FR-M10-02.06, BR-M10-02 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-02.06, BR-M10-02 |


**V2 — thay toàn bộ M1 đến kết thúc:** User thường. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-002 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-002 | Người yêu cầu chọn gửi đề xuất nhận vai trò mod. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V2.2 | FR-M10-02.06, BR-M10-02 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-02.06, BR-M10-02 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mod hệ thống (kể cả Owner/Group Mod/Admin nhóm chat nhưng không ADMIN hệ thống). Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-002 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-008 | Người yêu cầu chọn gửi đề xuất nhận vai trò mod. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V3.2 | FR-M10-02.06, BR-M10-02 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-02.06, BR-M10-02 |


<!-- sc:end SC-M10-002 -->

<a id="sc-m10-003"></a>

<!-- sc:scenario SC-M10-003 -->

### SC-M10-003

#### 1. Tên kịch bản chuẩn

Gửi đề xuất nhận vai trò Admin — BF-M10-003; owner [UC-M10-004](../../us/US-M10.md#uc-m10-004).

#### 2. Actor thực hiện

ACT-007 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Có người nhận được chọn; quyền gốc/loại/ACTIVE/xong bước 3 kiểm trong luồng. Chuẩn An ADMIN gốc, Lan USER hợp lệ; người nhận Admin không được cấp dấu gốc.

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-003 -->

| result | condition |
|---|---|
| SUCCESS | Đề xuất Admin mới Chưa trả lời và thông báo/log mới được lưu bởi ADMIN gốc; USER/MODERATOR nhận giữ vai trò đến chấp nhận. Chấp nhận sẽ nhận ADMIN thường, không nhận dấu gốc. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không có thay đổi được yêu cầu thành công. Hiệu ứng hợp lệ đã có được giữ; không tự ghi nhận thao tác thành công, xóa hồ sơ, rollback hoặc cấp quyền mới. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-003 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | An chọn gửi Đề xuất làm Admin cho Lan. | An ADMIN gốc; Lan USER ACTIVE SETUP_COMPLETED; không điều kiện điểm/uy tín | M2 | FR-M10-07.05 |
| M2 | SYSTEM | Hệ thống kiểm hiện tại: người gửi ADMIN có dấu gốc, người nhận USER hoặc MODERATOR đang ACTIVE/xong bước 3; không kiểm điểm, uy tín hoặc thâm niên. Không có bản cùng loại cần thay. Lưu P1002 mới Chưa trả lời, loại Admin, người gửi An, người nhận Lan, gửi T, hạn T+7×24h; giữ vai trò USER của người nhận. Cung cấp M07 sự kiện Đề xuất làm Admin và N1002 mới với Chấp nhận/Từ chối, trả đã gửi; chưa phong vai trò hoặc đợi câu trả lời. Ghi thêm nhật ký Admin: người làm An, thao tác gửi đề xuất Admin, đối tượng Lan, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | P1002/N1002; Lan vẫn USER; gửi 10/11 10:00, hạn 17/11 10:00+07; tối đa 1 bản hiệu lực mỗi loại/người; lý do không bắt buộc | END:SUCCESS | FR-M10-07.01, FR-M10-07.02, FR-M10-07.05, FR-M10-07.06, FR-M10-07.07, FR-M10-07.08, FR-M10-07.09, FR-M10-07.10, FR-M10-07.11, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-003 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Có bản cùng loại cũ Chưa trả lời; người gửi/nhận vẫn đủ điều kiện | E1.1 | FR-M10-07.01, FR-M10-07.02, FR-M10-07.05, FR-M10-07.06, FR-M10-07.07, FR-M10-07.08, FR-M10-07.09, FR-M10-07.10, FR-M10-07.11, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |
| E2 | system | M2 | Có bản cùng loại cũ Đã từ chối; người gửi/nhận vẫn đủ điều kiện | E2.1 | FR-M10-07.01, FR-M10-07.02, FR-M10-07.05, FR-M10-07.06, FR-M10-07.07, FR-M10-07.08, FR-M10-07.09, FR-M10-07.10, FR-M10-07.11, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |
| E3 | system | M2 | Có bản cùng loại cũ Hết hiệu lực; người gửi/nhận vẫn đủ điều kiện | E3.1 | FR-M10-07.01, FR-M10-07.02, FR-M10-07.05, FR-M10-07.06, FR-M10-07.07, FR-M10-07.08, FR-M10-07.09, FR-M10-07.10, FR-M10-07.11, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |
| E4 | system | M2 | Đang có đề xuất loại còn lại cho cùng Lan; hai loại không thay nhau | E4.1 | FR-M10-07.01, FR-M10-07.02, FR-M10-07.05, FR-M10-07.06, FR-M10-07.07, FR-M10-07.08, FR-M10-07.09, FR-M10-07.10, FR-M10-07.11, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |
| E5 | system | M2 | Người nhận không ACTIVE: DEACTIVATED | E5.1 | FR-M10-07.08, BR-M10-05 |
| E6 | system | M2 | Người nhận không ACTIVE: BANNED | E6.1 | FR-M10-07.08, BR-M10-05 |
| E7 | system | M2 | Người nhận không ACTIVE: DELETED | E7.1 | FR-M10-07.08, BR-M10-05 |
| E8 | system | M2 | Người nhận chưa hoàn tất bước 3 | E8.1 | FR-M10-07.08, BR-M10-05 |
| E9 | system | M2 | Đích sai vai trò cho loại đề xuất | E9.1 | FR-M10-07.02, BR-M10-27 |
| E10 | user-choice | M1 | An gửi đề xuất Admin cho Mai đang MODERATOR hợp lệ | E10.1 | FR-M10-07.05, FR-M10-07.01, FR-M10-07.02, FR-M10-07.06, FR-M10-07.07, FR-M10-07.08, FR-M10-07.09, FR-M10-07.10, FR-M10-07.11, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |
| E11 | system | M1 | Người gửi ADMIN nhưng không gốc | E11.1 | FR-M10-07.07, BR-M10-11 |


<!-- sc:branch SC-M10-003 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm hiện tại: người gửi ADMIN có dấu gốc, người nhận USER hoặc MODERATOR đang ACTIVE/xong bước 3; không kiểm điểm, uy tín hoặc thâm niên. Sau khi kiểm đạt, chuyển P0992 cùng loại/cùng người gửi 05/11 10:00, đang hiệu lực đến trước 12/11 10:00, sang Hết hiệu lực TRƯỚC lưu bản mới; thông báo cũ không trả lời được, không gán nhãn Đã hết hạn cho nguyên nhân bị thay. Lưu P1002 mới Chưa trả lời, loại Admin, người gửi An, người nhận Lan, gửi T, hạn T+7×24h; giữ vai trò USER của người nhận. Cung cấp M07 sự kiện Đề xuất làm Admin và N1002 mới với Chấp nhận/Từ chối, trả đã gửi; chưa phong vai trò hoặc đợi câu trả lời. Ghi thêm nhật ký Admin: người làm An, thao tác gửi đề xuất Admin, đối tượng Lan, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | P1002/N1002; Lan vẫn USER; gửi 10/11 10:00, hạn 17/11 10:00+07; tối đa 1 bản hiệu lực mỗi loại/người; lý do không bắt buộc | END:SUCCESS | FR-M10-07.01, FR-M10-07.02, FR-M10-07.05, FR-M10-07.06, FR-M10-07.07, FR-M10-07.08, FR-M10-07.09, FR-M10-07.10, FR-M10-07.11, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |


<!-- sc:branch SC-M10-003 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống kiểm hiện tại: người gửi ADMIN có dấu gốc, người nhận USER hoặc MODERATOR đang ACTIVE/xong bước 3; không kiểm điểm, uy tín hoặc thâm niên. Giữ nguyên bản cùng loại cũ Đã từ chối, tạo bản mới, không mở lại bản cũ. Lưu P1002 mới Chưa trả lời, loại Admin, người gửi An, người nhận Lan, gửi T, hạn T+7×24h; giữ vai trò USER của người nhận. Cung cấp M07 sự kiện Đề xuất làm Admin và N1002 mới với Chấp nhận/Từ chối, trả đã gửi; chưa phong vai trò hoặc đợi câu trả lời. Ghi thêm nhật ký Admin: người làm An, thao tác gửi đề xuất Admin, đối tượng Lan, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | P1002/N1002; Lan vẫn USER; gửi 10/11 10:00, hạn 17/11 10:00+07; tối đa 1 bản hiệu lực mỗi loại/người; lý do không bắt buộc | END:SUCCESS | FR-M10-07.01, FR-M10-07.02, FR-M10-07.05, FR-M10-07.06, FR-M10-07.07, FR-M10-07.08, FR-M10-07.09, FR-M10-07.10, FR-M10-07.11, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |


<!-- sc:branch SC-M10-003 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống kiểm hiện tại: người gửi ADMIN có dấu gốc, người nhận USER hoặc MODERATOR đang ACTIVE/xong bước 3; không kiểm điểm, uy tín hoặc thâm niên. Giữ nguyên bản cùng loại cũ Hết hiệu lực, tạo bản mới, không mở lại bản cũ. Lưu P1002 mới Chưa trả lời, loại Admin, người gửi An, người nhận Lan, gửi T, hạn T+7×24h; giữ vai trò USER của người nhận. Cung cấp M07 sự kiện Đề xuất làm Admin và N1002 mới với Chấp nhận/Từ chối, trả đã gửi; chưa phong vai trò hoặc đợi câu trả lời. Ghi thêm nhật ký Admin: người làm An, thao tác gửi đề xuất Admin, đối tượng Lan, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | P1002/N1002; Lan vẫn USER; gửi 10/11 10:00, hạn 17/11 10:00+07; tối đa 1 bản hiệu lực mỗi loại/người; lý do không bắt buộc | END:SUCCESS | FR-M10-07.01, FR-M10-07.02, FR-M10-07.05, FR-M10-07.06, FR-M10-07.07, FR-M10-07.08, FR-M10-07.09, FR-M10-07.10, FR-M10-07.11, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |


<!-- sc:branch SC-M10-003 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống kiểm hiện tại: người gửi ADMIN có dấu gốc, người nhận USER hoặc MODERATOR đang ACTIVE/xong bước 3; không kiểm điểm, uy tín hoặc thâm niên. Không có bản cùng loại cần thay. Giữ đề xuất loại còn lại độc lập. Lưu P1002 mới Chưa trả lời, loại Admin, người gửi An, người nhận Lan, gửi T, hạn T+7×24h; giữ vai trò USER của người nhận. Cung cấp M07 sự kiện Đề xuất làm Admin và N1002 mới với Chấp nhận/Từ chối, trả đã gửi; chưa phong vai trò hoặc đợi câu trả lời. Ghi thêm nhật ký Admin: người làm An, thao tác gửi đề xuất Admin, đối tượng Lan, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | P1002/N1002; Lan vẫn USER; gửi 10/11 10:00, hạn 17/11 10:00+07; tối đa 1 bản hiệu lực mỗi loại/người; lý do không bắt buộc | END:SUCCESS | FR-M10-07.01, FR-M10-07.02, FR-M10-07.05, FR-M10-07.06, FR-M10-07.07, FR-M10-07.08, FR-M10-07.09, FR-M10-07.10, FR-M10-07.11, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |


<!-- sc:branch SC-M10-003 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống kiểm người nhận trước thay bản cũ, từ chối gửi; không tạo đề xuất/thông báo/log gửi thành công hoặc tự đổi hiệu lực bản cũ. | Lan DEACTIVATED; role USER; mọi bản cũ vẫn theo vòng đời trước đó | END:REJECTED | FR-M10-07.08, BR-M10-05 |


<!-- sc:branch SC-M10-003 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống kiểm người nhận trước thay bản cũ, từ chối gửi; không tạo đề xuất/thông báo/log gửi thành công hoặc tự đổi hiệu lực bản cũ. | Lan BANNED; role USER; mọi bản cũ vẫn theo vòng đời trước đó | END:REJECTED | FR-M10-07.08, BR-M10-05 |


<!-- sc:branch SC-M10-003 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống kiểm người nhận trước thay bản cũ, từ chối gửi; không tạo đề xuất/thông báo/log gửi thành công hoặc tự đổi hiệu lực bản cũ. | Lan DELETED; role USER; mọi bản cũ vẫn theo vòng đời trước đó | END:REJECTED | FR-M10-07.08, BR-M10-05 |


<!-- sc:branch SC-M10-003 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống từ chối gửi trước khi thay/lưu đề xuất; không bổ sung điều kiện điểm hay thâm niên. | Lan ACTIVE nhưng mới xong bước 1 hoặc 2 | END:REJECTED | FR-M10-07.08, BR-M10-05 |


<!-- sc:branch SC-M10-003 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống từ chối gửi cho vai trò không hợp lệ; không tự hạ role đích để gửi. | Target đã ADMIN | END:REJECTED | FR-M10-07.02, BR-M10-27 |


<!-- sc:branch SC-M10-003 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | ACT-007 | An chọn Đề xuất làm Admin cho Mai. | An ADMIN gốc; Mai MODERATOR ACTIVE SETUP_COMPLETED | E10.2 | FR-M10-07.05 |
| E10.2 | SYSTEM | Hệ thống kiểm hiện tại: người gửi ADMIN có dấu gốc, người nhận USER hoặc MODERATOR đang ACTIVE/xong bước 3; không kiểm điểm, uy tín hoặc thâm niên. Không có bản cùng loại cần thay. Lưu P1002 mới Chưa trả lời, loại Admin, người gửi An, người nhận Mai, gửi T, hạn T+7×24h; giữ vai trò MODERATOR của người nhận. Cung cấp M07 sự kiện Đề xuất làm Admin và N1002 mới với Chấp nhận/Từ chối, trả đã gửi; chưa phong vai trò hoặc đợi câu trả lời. Ghi thêm nhật ký Admin: người làm An, thao tác gửi đề xuất Admin, đối tượng Mai, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | P1002/N1002; Mai vẫn MODERATOR; gửi 10/11 10:00, hạn 17/11 10:00+07; tối đa 1 bản hiệu lực mỗi loại/người; lý do không bắt buộc | END:SUCCESS | FR-M10-07.01, FR-M10-07.02, FR-M10-07.05, FR-M10-07.06, FR-M10-07.07, FR-M10-07.08, FR-M10-07.09, FR-M10-07.10, FR-M10-07.11, BR-M10-02, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-27, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, FR-M07-02.14, FR-M07-02.30, FR-M07-02.32 |


<!-- sc:branch SC-M10-003 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-007 | Bảo ADMIN thường yêu cầu gửi đề xuất Admin cho Lan. | Bảo là actor ngay từ đầu, không phải An gốc; Lan hợp lệ | E11.2 | FR-M10-07.07 |
| E11.2 | SYSTEM | Hệ thống từ chối gửi đề xuất Admin bởi Admin thường; không tạo bản mới/thông báo hoặc phong Admin. | Bảo ADMIN không gốc, người nhận Lan vẫn USER | END:REJECTED | FR-M10-07.07, BR-M10-11 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-003 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Người yêu cầu chọn gửi đề xuất nhận vai trò admin. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V1.2 | FR-M10-07.01, BR-M10-02 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-07.01, BR-M10-02 |


**V2 — thay toàn bộ M1 đến kết thúc:** User thường. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-003 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-002 | Người yêu cầu chọn gửi đề xuất nhận vai trò admin. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V2.2 | FR-M10-07.01, BR-M10-02 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-07.01, BR-M10-02 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mod hệ thống (kể cả Owner/Group Mod/Admin nhóm chat nhưng không ADMIN hệ thống). Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-003 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-008 | Người yêu cầu chọn gửi đề xuất nhận vai trò admin. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V3.2 | FR-M10-07.01, BR-M10-02 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-07.01, BR-M10-02 |


<!-- sc:end SC-M10-003 -->

<a id="sc-m10-004"></a>

<!-- sc:scenario SC-M10-004 -->

### SC-M10-004

#### 1. Tên kịch bản chuẩn

Trả lời một đề xuất nhận vai trò của mình — BF-M10-004; owner [UC-M10-005](../../us/US-M10.md#uc-m10-005).

#### 2. Actor thực hiện

ACT-002 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Có phiên và thông báo/đề xuất của người thao tác; không cần quyền vào Panel. Chuẩn R1011/N1011: Bảo gửi 05/11/2026 10:00+07 cho Lan làm Mod, Chưa trả lời/chưa bị thay; hạn 12/11 10:00; lúc trả lời T còn hiệu lực; Lan ACTIVE USER. Quyền sở hữu/hiệu lực kiểm khi mở, kiểm lại tại lúc nhận lựa chọn; điều kiện chấp nhận khác từ chối.

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-004 -->

| result | condition |
|---|---|
| SUCCESS | Một lựa chọn hợp lệ được ghi và hiện, không trả lời lại: Chấp nhận đổi ngay một vai trò theo loại, Từ chối giữ vai trò. Không kết thúc ở chuyển lựa chọn M07 hoặc kiểm điều kiện xong. |
| REJECTED | Không có lần trả lời hợp lệ mới/không đổi vai trò theo yêu cầu bị từ chối. Đã trả lời hoặc Hết hiệu lực giữ quyết định/hiệu lực nguồn. Nếu Chấp nhận bị từ chối vì vai trò/ACTIVE, trạng thái đề xuất sau đó và khả năng thử lại là GAP001; không khẳng định vẫn Chưa trả lời, tự Đã từ chối/Hết hiệu lực hoặc tiêu thụ lượt. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-004 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan mở thông báo R1011 để phản hồi. | R1011/N1011: Bảo gửi 05/11/2026 10:00+07 cho Lan làm Mod, Chưa trả lời/chưa bị thay; hạn 12/11 10:00; lúc trả lời T còn hiệu lực; Lan ACTIVE USER. | M2 | FR-M07-02.14, FR-M07-05.02 |
| M2 | SYSTEM | Hệ thống xác nhận người nhận, trả R1011 còn Chưa trả lời/chưa bị thay/còn hạn cùng hai lựa chọn; chỉ mở chưa tiêu thụ quyền trả lời hoặc đổi vai trò. | U-LAN USER ACTIVE; đề xuất Mod; T trước 12/11 10:00 | M3 | FR-M10-03.04, FR-M10-03.07, FR-M10-03.08, BR-M10-07, BR-M10-27, FR-M07-02.14 |
| M3 | ACT-002 | Lan chọn Chấp nhận R1011. | Đúng người nhận; kiểm lại ACTIVE/vai trò/hiệu lực khi xử lý | M4 | FR-M10-03.01, FR-M10-03.02 |
| M4 | SYSTEM | Hệ thống kiểm đúng người nhận, bản chưa trả lời/chưa bị thay và thời điểm trước gửi+7×24h. Kiểm ACTIVE và vai trò hiện tại USER; đổi đúng một vai trò USER→MODERATOR ngay, đề xuất→Đã chấp nhận. Không kiểm lại quyền người gửi cũ hoặc buộc xác minh đăng ký mới; không cấp dấu gốc. Ghi thêm nhật ký Admin: người làm Lan, thao tác chấp nhận đề xuất Mod, đối tượng Lan, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. M07 hiện lựa chọn Chấp nhận trên thông báo, khóa trả lời lại và trả kết quả cho Lan. | Lan; loại=Mod; lựa chọn=Chấp nhận; vai trò sau=MODERATOR; thông báo được giữ, hiện lựa chọn đã chọn | END:SUCCESS | FR-M10-03.01, FR-M10-03.02, FR-M10-03.03, FR-M10-03.04, FR-M10-03.06, FR-M10-03.07, FR-M10-03.08, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M07-02.14, FR-M07-02.28, FR-M07-02.31, FR-M07-02.32, FR-M10-14.06, FR-M10-14.08, BR-M10-01, BR-M10-21 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-004 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M3 | Lan chọn Từ chối đề xuất Mod còn hiệu lực | E1.1 | FR-M10-03.03, FR-M10-03.01, FR-M10-03.02, FR-M10-03.04, FR-M10-03.06, FR-M10-03.07, FR-M10-03.08, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M07-02.14, FR-M07-02.28, FR-M07-02.31, FR-M07-02.32, FR-M10-14.06, FR-M10-14.08, BR-M10-01, BR-M10-21 |
| E2 | user-choice | M1 | Lan USER nhận đề xuất Admin của An gốc và chọn Chấp nhận | E2.1 | FR-M10-07.06, FR-M10-03.07, FR-M10-03.08, BR-M10-07, BR-M10-27, FR-M10-03.09, FR-M10-03.01, FR-M10-03.02, FR-M10-03.03, FR-M10-03.04, FR-M10-03.06, FR-M10-03.10, FR-M10-03.11, BR-M10-05, BR-M10-06, FR-M07-02.14, FR-M07-02.28, FR-M07-02.31, FR-M07-02.32, FR-M10-14.06, FR-M10-14.08, BR-M10-01, BR-M10-21 |
| E3 | user-choice | M1 | Lan được đề xuất Admin khi là Mod nhưng đã bị giáng về USER trước trả lời, vẫn ACTIVE | E3.1 | FR-M10-03.09, FR-M10-03.10, BR-M10-27, FR-M10-03.07, FR-M10-03.08, FR-M10-03.01, FR-M10-03.02, FR-M10-03.03, FR-M10-03.04, FR-M10-03.06, FR-M10-03.11, BR-M10-05, BR-M10-06, BR-M10-07, FR-M07-02.14, FR-M07-02.28, FR-M07-02.31, FR-M07-02.32, FR-M10-14.06, FR-M10-14.08, BR-M10-01, BR-M10-21 |
| E4 | system | M4 | Bảo đã từ chức/mất ADMIN sau khi gửi hợp lệ R1011, Lan vẫn đủ điều kiện nhận Mod | E4.1 | FR-M10-03.01, FR-M10-03.02, FR-M10-03.03, FR-M10-03.04, FR-M10-03.06, FR-M10-03.07, FR-M10-03.08, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M07-02.14, FR-M07-02.28, FR-M07-02.31, FR-M07-02.32, FR-M10-14.06, BR-M10-21 |
| E5 | system | M2 | R1011 đã Đã chấp nhận trước khi mở phản hồi | E5.1 | FR-M10-03.04, FR-M10-03.06, BR-M10-07 |
| E6 | system | M2 | R1011 đã Đã từ chối trước khi mở phản hồi | E6.1 | FR-M10-03.04, FR-M10-03.06, BR-M10-07 |
| E7 | system | M2 | Đã đủ 7×24h trước khi mở phản hồi | E7.1 | FR-M10-02.10, FR-M10-03.08, BR-M10-07, FR-M07-02.31 |
| E8 | system | M2 | Đề xuất đã bị bản mới cùng loại thay trước khi mở phản hồi | E8.1 | FR-M10-02.08, FR-M10-03.08, BR-M10-27, FR-M07-02.30, FR-M07-02.32 |
| E9 | system | M4 | R1011 đã Đã chấp nhận sau lúc hiển thị, trước xử lý lựa chọn | E9.1 | FR-M10-03.04, FR-M10-03.06, BR-M10-07 |
| E10 | system | M4 | R1011 đã Đã từ chối sau lúc hiển thị, trước xử lý lựa chọn | E10.1 | FR-M10-03.04, FR-M10-03.06, BR-M10-07 |
| E11 | system | M4 | Đã đủ 7×24h sau lúc hiển thị, trước xử lý lựa chọn | E11.1 | FR-M10-02.10, FR-M10-03.08, BR-M10-07, FR-M07-02.31 |
| E12 | system | M4 | Đề xuất đã bị bản mới cùng loại thay sau lúc hiển thị, trước xử lý lựa chọn | E12.1 | FR-M10-02.08, FR-M10-03.08, BR-M10-27, FR-M07-02.30, FR-M07-02.32 |
| E13 | system | M2 | Người trả lời không phải người nhận | E13.1 | FR-M10-03.07, FR-M07-05.05 |
| E14 | system | M4 | Lúc Chấp nhận role không còn hợp lệ | E14.1 | FR-M10-03.10, BR-M10-27 |
| E15 | system | M4 | Lúc Chấp nhận account không ACTIVE | E15.1 | FR-M10-03.11, BR-M10-05 |


<!-- sc:branch SC-M10-004 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Lan chọn Từ chối R1011. | R1011 đúng Lan, Chưa trả lời/chưa bị thay, T trước hạn | E1.2 | FR-M10-03.03 |
| E1.2 | SYSTEM | Hệ thống kiểm đúng người nhận, bản chưa trả lời/chưa bị thay và thời điểm trước gửi+7×24h. Không chạy bộ kiểm ACTIVE/vai trò của nhánh Chấp nhận; giữ vai trò USER, chuyển Đã từ chối; không có thay đổi vai trò để ghi log. M07 hiện lựa chọn Từ chối trên thông báo, khóa trả lời lại và trả kết quả cho Lan. | Lan; loại=Mod; lựa chọn=Từ chối; vai trò sau=USER; thông báo được giữ, hiện lựa chọn đã chọn | END:SUCCESS | FR-M10-03.01, FR-M10-03.02, FR-M10-03.03, FR-M10-03.04, FR-M10-03.06, FR-M10-03.07, FR-M10-03.08, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M07-02.14, FR-M07-02.28, FR-M07-02.31, FR-M07-02.32, FR-M10-14.06, FR-M10-14.08, BR-M10-01, BR-M10-21 |


<!-- sc:branch SC-M10-004 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | Lan mở thông báo R1012 đề xuất Admin do An gốc gửi. | Lan USER ACTIVE; R1012 gửi 05/11 10:00, hạn 12/11 10:00, chưa trả lời/bị thay | E2.2 | FR-M10-07.06 |
| E2.2 | SYSTEM | Hệ thống xác nhận người nhận và hiệu lực, trả hai lựa chọn; không gán ADMIN trước quyết định. | R1012 loại Admin, người nhận Lan; T trước hạn | E2.3 | FR-M10-03.07, FR-M10-03.08, BR-M10-07, BR-M10-27 |
| E2.3 | ACT-002 | Lan chọn Chấp nhận R1012. | Vai trò lúc xử lý USER, account ACTIVE | E2.4 | FR-M10-03.09 |
| E2.4 | SYSTEM | Hệ thống kiểm đúng người nhận, bản chưa trả lời/chưa bị thay và thời điểm trước gửi+7×24h. Kiểm ACTIVE và vai trò hiện tại USER/MODERATOR; đổi đúng một vai trò USER→ADMIN ngay, đề xuất→Đã chấp nhận. Không kiểm lại quyền người gửi cũ hoặc buộc xác minh đăng ký mới; không cấp dấu gốc. Ghi thêm nhật ký Admin: người làm Lan, thao tác chấp nhận đề xuất Admin, đối tượng Lan, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. M07 hiện lựa chọn Chấp nhận trên thông báo, khóa trả lời lại và trả kết quả cho Lan. | Lan; loại=Admin; lựa chọn=Chấp nhận; vai trò sau=ADMIN; thông báo được giữ, hiện lựa chọn đã chọn | END:SUCCESS | FR-M10-03.01, FR-M10-03.02, FR-M10-03.03, FR-M10-03.04, FR-M10-03.06, FR-M10-03.07, FR-M10-03.08, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M07-02.14, FR-M07-02.28, FR-M07-02.31, FR-M07-02.32, FR-M10-14.06, FR-M10-14.08, BR-M10-01, BR-M10-21 |


<!-- sc:branch SC-M10-004 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-002 | Lan mở R1012 đề xuất Admin của mình. | Role lúc gửi MODERATOR, hiện USER; ACTIVE; R1012 còn hiệu lực | E3.2 | FR-M10-03.09, FR-M10-03.10, BR-M10-27 |
| E3.2 | SYSTEM | Hệ thống kiểm ownership/hiệu lực và trả lựa chọn, không vô hiệu chỉ vì Mod đã thành USER. | USER vẫn là role nguồn hợp lệ của đề xuất Admin | E3.3 | FR-M10-03.07, FR-M10-03.08, FR-M10-03.10, BR-M10-27 |
| E3.3 | ACT-002 | Lan chọn Chấp nhận nhận Admin. | Hiện USER ACTIVE, đúng R1012 | E3.4 | FR-M10-03.09 |
| E3.4 | SYSTEM | Hệ thống kiểm đúng người nhận, bản chưa trả lời/chưa bị thay và thời điểm trước gửi+7×24h. Kiểm ACTIVE và vai trò hiện tại USER/MODERATOR; đổi đúng một vai trò USER→ADMIN ngay, đề xuất→Đã chấp nhận. Không kiểm lại quyền người gửi cũ hoặc buộc xác minh đăng ký mới; không cấp dấu gốc. Ghi thêm nhật ký Admin: người làm Lan, thao tác chấp nhận đề xuất Admin, đối tượng Lan, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. M07 hiện lựa chọn Chấp nhận trên thông báo, khóa trả lời lại và trả kết quả cho Lan. | Lan; loại=Admin; lựa chọn=Chấp nhận; vai trò sau=ADMIN; thông báo được giữ, hiện lựa chọn đã chọn | END:SUCCESS | FR-M10-03.01, FR-M10-03.02, FR-M10-03.03, FR-M10-03.04, FR-M10-03.06, FR-M10-03.07, FR-M10-03.08, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M07-02.14, FR-M07-02.28, FR-M07-02.31, FR-M07-02.32, FR-M10-14.06, FR-M10-14.08, BR-M10-01, BR-M10-21 |


<!-- sc:branch SC-M10-004 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống kiểm chủ đề xuất, hiệu lực, Lan hiện USER/ACTIVE; không kiểm lại quyền người gửi cũ vì M10 không đặt điều kiện này. Đổi Lan MODERATOR, bản Đã chấp nhận, M07 hiện lựa chọn/khóa trả lời lại; trả thành công. Ghi thêm nhật ký Admin: người làm Lan, thao tác chấp nhận đề xuất Mod, đối tượng Lan, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | Bảo hiện USER nhưng gửi R1011 khi ADMIN; Lan USER→MODERATOR, R1011 Đã chấp nhận | END:SUCCESS | FR-M10-03.01, FR-M10-03.02, FR-M10-03.03, FR-M10-03.04, FR-M10-03.06, FR-M10-03.07, FR-M10-03.08, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M07-02.14, FR-M07-02.28, FR-M07-02.31, FR-M07-02.32, FR-M10-14.06, BR-M10-21 |


<!-- sc:branch SC-M10-004 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối lần trả lời mới, hiện/giữ lựa chọn đã có và khóa chọn lại; không đổi role lần nữa. | R1011=Đã chấp nhận; quyết định cũ không bị ghi đè | END:REJECTED | FR-M10-03.04, FR-M10-03.06, BR-M10-07 |


<!-- sc:branch SC-M10-004 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối lần trả lời mới, hiện/giữ lựa chọn đã có và khóa chọn lại; không đổi role lần nữa. | R1011=Đã từ chối; quyết định cũ không bị ghi đè | END:REJECTED | FR-M10-03.04, FR-M10-03.06, BR-M10-07 |


<!-- sc:branch SC-M10-004 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống dùng mốc gửi+7×24h, đánh dấu Hết hiệu lực khi chưa trả lời, M07 hiện Đã hết hạn và không cho chọn; từ chối yêu cầu trả lời, giữ role. | R1011 gửi 05/11 10:00, xử lý 12/11 10:00 hoặc muộn hơn, không phải T chuẩn | END:REJECTED | FR-M10-02.10, FR-M10-03.08, BR-M10-07, FR-M07-02.31 |


<!-- sc:branch SC-M10-004 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống từ chối trả lời bản cũ, không cấp role; giữ thông báo mới riêng và vô hiệu lựa chọn bản cũ, không tự gọi nguyên nhân bị thay là hết hạn. | R1011 cũ Hết hiệu lực do R1013 Mod mới cùng Lan; N1013 khác N1011 | END:REJECTED | FR-M10-02.08, FR-M10-03.08, BR-M10-27, FR-M07-02.30, FR-M07-02.32 |


<!-- sc:branch SC-M10-004 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống từ chối lần trả lời mới, hiện/giữ lựa chọn đã có và khóa chọn lại; không đổi role lần nữa. | R1011=Đã chấp nhận; quyết định cũ không bị ghi đè | END:REJECTED | FR-M10-03.04, FR-M10-03.06, BR-M10-07 |


<!-- sc:branch SC-M10-004 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống từ chối lần trả lời mới, hiện/giữ lựa chọn đã có và khóa chọn lại; không đổi role lần nữa. | R1011=Đã từ chối; quyết định cũ không bị ghi đè | END:REJECTED | FR-M10-03.04, FR-M10-03.06, BR-M10-07 |


<!-- sc:branch SC-M10-004 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | SYSTEM | Hệ thống dùng mốc gửi+7×24h, đánh dấu Hết hiệu lực khi chưa trả lời, M07 hiện Đã hết hạn và không cho chọn; từ chối yêu cầu trả lời, giữ role. | R1011 gửi 05/11 10:00, xử lý 12/11 10:00 hoặc muộn hơn, không phải T chuẩn | END:REJECTED | FR-M10-02.10, FR-M10-03.08, BR-M10-07, FR-M07-02.31 |


<!-- sc:branch SC-M10-004 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | SYSTEM | Hệ thống từ chối trả lời bản cũ, không cấp role; giữ thông báo mới riêng và vô hiệu lựa chọn bản cũ, không tự gọi nguyên nhân bị thay là hết hạn. | R1011 cũ Hết hiệu lực do R1013 Mod mới cùng Lan; N1013 khác N1011 | END:REJECTED | FR-M10-02.08, FR-M10-03.08, BR-M10-27, FR-M07-02.30, FR-M07-02.32 |


<!-- sc:branch SC-M10-004 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | SYSTEM | Hệ thống từ chối đọc/phản hồi hộ đề xuất, không đổi role hoặc để lộ thông báo người khác. | R1011 thuộc Bình, actor Lan | END:REJECTED | FR-M10-03.07, FR-M07-05.05 |


<!-- sc:branch SC-M10-004 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | SYSTEM | Hệ thống từ chối Chấp nhận và giữ role, không tự đặt trạng thái Đã từ chối/Hết hiệu lực hoặc khẳng định có thể thử lại; phần trạng thái bản còn GAP001. | R1011 Mod nhưng Lan hiện MODERATOR/ADMIN; hoặc đề xuất Admin nhưng Lan hiện ADMIN | END:REJECTED | FR-M10-03.10, BR-M10-27 |


<!-- sc:branch SC-M10-004 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | SYSTEM | Hệ thống từ chối Chấp nhận, không đổi role; trạng thái đề xuất/khả năng thử lại chưa chốt ở GAP001, không giả tiêu thụ một lượt hợp lệ. | Lan chuyển DEACTIVATED/BANNED trước xử lý; chưa có thay đổi role từ yêu cầu này | END:REJECTED | FR-M10-03.11, BR-M10-05 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest không có phiên xác định chủ đề xuất nên không được phản hồi hộ. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-004 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest gửi yêu cầu Chấp nhận R1011. | Không có phiên U-LAN, chỉ biết ID đề xuất | V1.2 | FR-M10-03.07 |
| V1.2 | SYSTEM | Hệ thống không xác nhận được đúng người nhận, từ chối phản hồi và không đổi role; biết ID không cấp quyền xem thông báo hoặc nhận vai trò. | R1011 không có trả lời hợp lệ mới | END:REJECTED | FR-M10-03.07, FR-M07-05.05 |


**V2 — thay toàn bộ M1 đến kết thúc:** Mai MODERATOR ACTIVE trả lời đề xuất Admin R1012 của chính Mai do An gốc gửi; lựa chọn Chấp nhận. Actor khởi tạo ACT-008; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-004 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-008 | Mai mở R1012 đề xuất Admin của mình. | Mai MODERATOR ACTIVE; gửi 05/11 10:00, hạn 12/11 10:00; Chưa trả lời/chưa thay | V2.2 | FR-M10-07.06 |
| V2.2 | SYSTEM | Hệ thống kiểm đúng người nhận và hiệu lực, trả lựa chọn cho Mai, không bắt Mod vào Panel. | R1012 loại Admin, target U-MAI, T còn hạn | V2.3 | FR-M10-03.07, FR-M10-03.08, BR-M10-07, BR-M10-27 |
| V2.3 | ACT-008 | Mai chọn Chấp nhận R1012. | Role hiện MODERATOR, account ACTIVE; đúng chủ | V2.4 | FR-M10-03.03, FR-M10-03.09, BR-M10-27 |
| V2.4 | SYSTEM | Hệ thống kiểm đúng người nhận, bản chưa trả lời/chưa bị thay và thời điểm trước gửi+7×24h. Kiểm ACTIVE và vai trò hiện tại USER/MODERATOR; đổi đúng một vai trò MODERATOR→ADMIN ngay, đề xuất→Đã chấp nhận. Không kiểm lại quyền người gửi cũ hoặc buộc xác minh đăng ký mới; không cấp dấu gốc. Ghi thêm nhật ký Admin: người làm Mai, thao tác chấp nhận đề xuất Admin, đối tượng Mai, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. M07 hiện lựa chọn Chấp nhận trên thông báo, khóa trả lời lại và trả kết quả cho Mai. | Mai; loại=Admin; lựa chọn=Chấp nhận; vai trò sau=ADMIN; thông báo được giữ, hiện lựa chọn đã chọn | END:SUCCESS | FR-M10-03.01, FR-M10-03.02, FR-M10-03.03, FR-M10-03.04, FR-M10-03.06, FR-M10-03.07, FR-M10-03.08, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M07-02.14, FR-M07-02.28, FR-M07-02.31, FR-M07-02.32, FR-M10-14.06, FR-M10-14.08, BR-M10-01, BR-M10-21 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mai MODERATOR ACTIVE trả lời đề xuất Admin R1012 của chính Mai do An gốc gửi; lựa chọn Từ chối. Actor khởi tạo ACT-008; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-004 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-008 | Mai mở R1012 đề xuất Admin của mình. | Mai MODERATOR ACTIVE; gửi 05/11 10:00, hạn 12/11 10:00; Chưa trả lời/chưa thay | V3.2 | FR-M10-07.06 |
| V3.2 | SYSTEM | Hệ thống kiểm đúng người nhận và hiệu lực, trả lựa chọn cho Mai, không bắt Mod vào Panel. | R1012 loại Admin, target U-MAI, T còn hạn | V3.3 | FR-M10-03.07, FR-M10-03.08, BR-M10-07, BR-M10-27 |
| V3.3 | ACT-008 | Mai chọn Từ chối R1012. | Role hiện MODERATOR, account ACTIVE; đúng chủ | V3.4 | FR-M10-03.03, FR-M10-03.09, BR-M10-27 |
| V3.4 | SYSTEM | Hệ thống kiểm đúng người nhận, bản chưa trả lời/chưa bị thay và thời điểm trước gửi+7×24h. Không chạy bộ kiểm ACTIVE/vai trò của nhánh Chấp nhận; giữ vai trò MODERATOR, chuyển Đã từ chối; không có thay đổi vai trò để ghi log. M07 hiện lựa chọn Từ chối trên thông báo, khóa trả lời lại và trả kết quả cho Mai. | Mai; loại=Admin; lựa chọn=Từ chối; vai trò sau=MODERATOR; thông báo được giữ, hiện lựa chọn đã chọn | END:SUCCESS | FR-M10-03.01, FR-M10-03.02, FR-M10-03.03, FR-M10-03.04, FR-M10-03.06, FR-M10-03.07, FR-M10-03.08, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M07-02.14, FR-M07-02.28, FR-M07-02.31, FR-M07-02.32, FR-M10-14.06, FR-M10-14.08, BR-M10-01, BR-M10-21 |


**V4 — thay toàn bộ M1 đến kết thúc:** Lan nay là ADMIN không gốc do đã nhận đề xuất Admin khác loại; bản Mod R1011 vẫn hiệu lực. Lan chọn Từ chối trực tiếp, không phải thử lại sau một lần Chấp nhận lỗi. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-004 V4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V4.1 | ACT-007 | Lan ADMIN chọn Từ chối R1011 Mod cũ của chính mình. | R1011 Mod còn Chưa trả lời/chưa thay, T còn hạn; trước đó Lan nhận Admin qua R1012 khác loại; actor U-LAN | V4.2 | FR-M10-03.03, BR-M10-27 |
| V4.2 | SYSTEM | Hệ thống kiểm đúng người nhận, bản chưa trả lời/chưa bị thay và thời điểm trước gửi+7×24h. Không chạy bộ kiểm ACTIVE/vai trò của nhánh Chấp nhận; giữ vai trò ADMIN, chuyển Đã từ chối; không có thay đổi vai trò để ghi log. M07 hiện lựa chọn Từ chối trên thông báo, khóa trả lời lại và trả kết quả cho Lan. | Lan; loại=Mod; lựa chọn=Từ chối; vai trò sau=ADMIN; thông báo được giữ, hiện lựa chọn đã chọn | END:SUCCESS | FR-M10-03.01, FR-M10-03.02, FR-M10-03.03, FR-M10-03.04, FR-M10-03.06, FR-M10-03.07, FR-M10-03.08, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-27, FR-M07-02.14, FR-M07-02.28, FR-M07-02.31, FR-M07-02.32, FR-M10-14.06, FR-M10-14.08, BR-M10-01, BR-M10-21 |


**V5 — thay toàn bộ M1 đến kết thúc:** Lan đã là ADMIN qua đề xuất khác loại, bấm Chấp nhận R1011 Mod còn hiệu lực thì bị guard role từ chối; chưa chốt trạng thái bản sau lỗi. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-004 V5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V5.1 | ACT-007 | Lan ADMIN gửi lựa chọn Chấp nhận R1011 Mod của chính mình. | R1011 Mod còn Chưa trả lời/chưa thay/còn hạn, nhưng Lan hiện ADMIN ACTIVE | V5.2 | FR-M10-03.01, FR-M10-03.10, BR-M10-27 |
| V5.2 | SYSTEM | Hệ thống kiểm chủ/hiệu lực rồi từ chối Chấp nhận vì hiện không còn USER để nhận Mod; giữ ADMIN. Không tự quyết trạng thái đề xuất hoặc quyền thử lại khi nguồn còn GAP001. | Lan ADMIN→ADMIN; không có log đổi role thành công | END:REJECTED | FR-M10-03.10, BR-M10-27 |


<!-- sc:end SC-M10-004 -->

<a id="sc-m10-005"></a>

<!-- sc:scenario SC-M10-005 -->

### SC-M10-005

#### 1. Tên kịch bản chuẩn

Giáng cấp một Mod về User — BF-M10-005; owner [UC-M10-006](../../us/US-M10.md#uc-m10-006).

#### 2. Actor thực hiện

ACT-007 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Có tài khoản đích; quyền ADMIN và role đích kiểm khi xử lý. Chuẩn Bảo ADMIN thường, Mai MODERATOR, không cần lý do bắt buộc hoặc đồng ý của Mai.

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-005 -->

| result | condition |
|---|---|
| SUCCESS | Đích MODERATOR→USER ngay, log người Admin giáng cấp, không cần đồng ý/không khiếu nại; không xóa tài khoản hoặc ban đích. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không có thay đổi được yêu cầu thành công. Hiệu ứng hợp lệ đã có được giữ; không tự ghi nhận thao tác thành công, xóa hồ sơ, rollback hoặc cấp quyền mới. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-005 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | Bảo chọn Giáng cấp Mai. | target U-MAI MODERATOR; actor U-BAO ADMIN | M2 | FR-M10-04.01 |
| M2 | SYSTEM | Hệ thống kiểm actor ADMIN và đích còn MODERATOR; chuyển Mai→USER ngay, không hỏi Mai đồng ý, không tạo xử lý khiếu nại được. Trả đã giáng cấp; nhận lại vai trò cần đề xuất mới hợp lệ. Ghi thêm nhật ký Admin: người làm Bảo, thao tác giáng cấp Mod, đối tượng Mai, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | Mai MODERATOR→USER; trạng thái tài khoản giữ nguyên; không phục hồi Mod theo một lần gỡ/lật ban | END:SUCCESS | FR-M10-04.01, FR-M10-04.02, FR-M10-04.03, FR-M10-04.04, FR-M10-04.05, FR-M10-05.06, BR-M10-02, BR-M10-08, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-005 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Target không còn MODERATOR: USER | E1.1 | FR-M10-04.05 |
| E2 | system | M2 | Target không còn MODERATOR: ADMIN | E2.1 | FR-M10-04.05 |


<!-- sc:branch SC-M10-005 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối Giáng cấp Mod cho đích khác loại; không dùng để thu hồi Admin hoặc đổi role USER. | Mai hiện USER | END:REJECTED | FR-M10-04.05 |


<!-- sc:branch SC-M10-005 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối Giáng cấp Mod cho đích khác loại; không dùng để thu hồi Admin hoặc đổi role USER. | Mai hiện ADMIN | END:REJECTED | FR-M10-04.05 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-005 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Người yêu cầu chọn giáng cấp một mod về user. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V1.2 | FR-M10-04.04, BR-M10-02 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-04.04, BR-M10-02 |


**V2 — thay toàn bộ M1 đến kết thúc:** User thường. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-005 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-002 | Người yêu cầu chọn giáng cấp một mod về user. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V2.2 | FR-M10-04.04, BR-M10-02 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-04.04, BR-M10-02 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mod hệ thống (kể cả Owner/Group Mod/Admin nhóm chat nhưng không ADMIN hệ thống). Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-005 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-008 | Người yêu cầu chọn giáng cấp một mod về user. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V3.2 | FR-M10-04.04, BR-M10-02 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-04.04, BR-M10-02 |


<!-- sc:end SC-M10-005 -->

<a id="sc-m10-006"></a>

<!-- sc:scenario SC-M10-006 -->

### SC-M10-006

#### 1. Tên kịch bản chuẩn

Thu hồi vai trò Admin của một Admin khác — BF-M10-006; owner [UC-M10-007](../../us/US-M10.md#uc-m10-007).

#### 2. Actor thực hiện

ACT-007 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Có đích được chọn, dấu gốc/người thao tác/role đích kiểm trong luồng. Chuẩn An ADMIN gốc, Bảo ADMIN không gốc, trước đây từng là Mod.

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-006 -->

| result | condition |
|---|---|
| SUCCESS | Admin đích khác gốc về USER ngay, log đúng ADMIN gốc; không khôi phục Mod cũ, không yêu cầu đồng ý/cho khiếu nại, không thu hồi gốc. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không có thay đổi được yêu cầu thành công. Hiệu ứng hợp lệ đã có được giữ; không tự ghi nhận thao tác thành công, xóa hồ sơ, rollback hoặc cấp quyền mới. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-006 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | An chọn Thu hồi vai trò Admin của Bảo. | actor An ADMIN gốc; target Bảo ADMIN không gốc, trước đây MODERATOR | M2 | FR-M10-08.03 |
| M2 | SYSTEM | Hệ thống kiểm người làm là ADMIN gốc, đích ADMIN và khác tài khoản gốc; đổi Bảo→USER ngay, không trả MODERATOR cũ, không hỏi đồng ý hoặc cho khiếu nại. Trả đã thu hồi; An vẫn ADMIN gốc nên luôn còn Admin. Ghi thêm nhật ký Admin: người làm An, thao tác thu hồi vai trò Admin, đối tượng Bảo, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | Bảo ADMIN→USER; An ADMIN gốc không đổi; account không bị ban/xóa | END:SUCCESS | FR-M10-08.01, FR-M10-08.02, FR-M10-08.03, FR-M10-08.04, FR-M10-08.05, FR-M10-08.06, BR-M10-10, BR-M10-11, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-006 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Target không ADMIN: USER | E1.1 | FR-M10-08.02 |
| E2 | system | M2 | Target không ADMIN: MODERATOR | E2.1 | FR-M10-08.02 |
| E3 | system | M1 | Người thao tác là ADMIN thường, không gốc | E3.1 | FR-M10-08.05, BR-M10-11 |
| E4 | system | M1 | Target là ADMIN gốc, kể cả yêu cầu từ chính gốc | E4.1 | FR-M10-08.04, BR-M10-10 |


<!-- sc:branch SC-M10-006 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối thu hồi Admin, không đổi role đích khác loại. | Bảo hiện USER | END:REJECTED | FR-M10-08.02 |


<!-- sc:branch SC-M10-006 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối thu hồi Admin, không đổi role đích khác loại. | Bảo hiện MODERATOR | END:REJECTED | FR-M10-08.02 |


<!-- sc:branch SC-M10-006 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-007 | Bảo yêu cầu thu hồi Admin của Chi. | Ngay từ đầu actor Bảo ADMIN không gốc; target Chi ADMIN không gốc | E3.2 | FR-M10-08.05 |
| E3.2 | SYSTEM | Hệ thống từ chối thu hồi bởi Admin thường, không làm mất Admin đích. | Chi vẫn ADMIN; không log thu hồi thành công | END:REJECTED | FR-M10-08.05, BR-M10-11 |


<!-- sc:branch SC-M10-006 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-007 | An yêu cầu thu hồi vai trò của chính An gốc. | Actor=target An ADMIN gốc; không phải Bảo trong main | E4.2 | FR-M10-08.04 |
| E4.2 | SYSTEM | Hệ thống từ chối tuyệt đối thu hồi gốc; An giữ ADMIN và hệ thống còn ít nhất một Admin. | An ADMIN gốc không đổi | END:REJECTED | FR-M10-08.04, BR-M10-10 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-006 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Người yêu cầu chọn thu hồi vai trò admin của một admin khác. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V1.2 | FR-M10-08.01, BR-M10-02 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-08.01, BR-M10-02 |


**V2 — thay toàn bộ M1 đến kết thúc:** User thường. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-006 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-002 | Người yêu cầu chọn thu hồi vai trò admin của một admin khác. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V2.2 | FR-M10-08.01, BR-M10-02 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-08.01, BR-M10-02 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mod hệ thống (kể cả Owner/Group Mod/Admin nhóm chat nhưng không ADMIN hệ thống). Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-006 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-008 | Người yêu cầu chọn thu hồi vai trò admin của một admin khác. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V3.2 | FR-M10-08.01, BR-M10-02 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-08.01, BR-M10-02 |


<!-- sc:end SC-M10-006 -->

<a id="sc-m10-007"></a>

<!-- sc:scenario SC-M10-007 -->

### SC-M10-007

#### 1. Tên kịch bản chuẩn

Tự từ chức vai trò sau xác nhận — BF-M10-007; owner [UC-M10-008](../../us/US-M10.md#uc-m10-008).

#### 2. Actor thực hiện

ACT-008 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Chính người thao tác yêu cầu; kiểm role MODERATOR hoặc ADMIN không gốc. Chuẩn Mai MODERATOR, không cần mở Admin Panel để từ chức.

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-007 -->

| result | condition |
|---|---|
| SUCCESS | Chính Mod/Admin không gốc về USER sau một xác nhận; log chính người từ chức. Hủy giữ role, gốc không được từ chức. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không có thay đổi được yêu cầu thành công. Hiệu ứng hợp lệ đã có được giữ; không tự ghi nhận thao tác thành công, xóa hồ sơ, rollback hoặc cấp quyền mới. |
| CANCELLED | Actor hủy tại bước xác nhận, role giữ nguyên; không có thay đổi vai trò hoặc log tự từ chức thành công. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-007 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-008 | Mai chọn Từ chức vai trò của chính mình. | actor=target=U-MAI MODERATOR | M2 | FR-M10-05.01 |
| M2 | SYSTEM | Hệ thống kiểm chính chủ, role Mod hoặc Admin không gốc rồi hỏi xác nhận một lần; chưa đổi vai trò. | Mai vẫn MODERATOR; có Xác nhận hoặc Hủy | M3 | FR-M10-05.01, FR-M10-05.02, FR-M10-05.03, FR-M10-05.05, BR-M10-10, BR-M10-25 |
| M3 | ACT-008 | Mai xác nhận từ chức. | Chính Mai đồng ý về USER; một lần xác nhận | M4 | FR-M10-05.01, FR-M10-05.03 |
| M4 | SYSTEM | Hệ thống kiểm điều kiện hiện tại và chuyển chính Mai→USER; trả đã từ chức. Muốn có lại role chỉ qua chấp nhận đề xuất mới, không tự hoàn tác. Ghi thêm nhật ký Admin: người làm Mai, thao tác tự từ chức Mod, đối tượng Mai, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | Mai MODERATOR→USER; người làm log Mai, không Hệ thống; không đặt chính sách logout/phiên mới | END:SUCCESS | FR-M10-05.01, FR-M10-05.03, FR-M10-05.06, FR-M10-14.06, BR-M10-21, BR-M10-25 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-007 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M3 | Mai hủy ở bước xác nhận | E1.1 | FR-M10-05.03, BR-M10-21, BR-M10-25 |
| E2 | system | M4 | Role đã không còn MODERATOR/ADMIN tại lúc xử lý xác nhận | E2.1 | FR-M10-05.01, FR-M10-05.02, BR-M10-21, BR-M10-25 |


<!-- sc:branch SC-M10-007 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-008 | Mai chọn Hủy xác nhận từ chức. | Mai vẫn MODERATOR, chưa có thay đổi | E1.2 | FR-M10-05.03 |
| E1.2 | SYSTEM | Hệ thống kết thúc yêu cầu từ chức, giữ MODERATOR; không ghi log tự từ chức thành công vì không đổi role. | Mai MODERATOR→MODERATOR; không tự gửi đề xuất mới | END:CANCELLED | FR-M10-05.03, BR-M10-21, BR-M10-25 |


<!-- sc:branch SC-M10-007 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống kiểm hiện tại và từ chối tạo lần từ chức nữa vì không còn role nguồn; giữ USER và không ghi log role thay đổi không xảy ra. | Mai đã USER bởi thay đổi hợp lệ khác trước T; không dùng vai trò cũ ở lúc mở xác nhận | END:SUCCESS | FR-M10-05.01, FR-M10-05.02, BR-M10-21, BR-M10-25 |


**V1 — thay toàn bộ M1 đến kết thúc:** Bảo ADMIN không gốc tự từ chức với một xác nhận. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-007 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-007 | Bảo chọn từ chức Admin của chính mình. | actor=target U-BAO ADMIN, gốc=false | V1.2 | FR-M10-05.04 |
| V1.2 | SYSTEM | Hệ thống kiểm ADMIN không gốc và chính người yêu cầu, hỏi xác nhận một lần; chưa đổi role. | Bảo vẫn ADMIN; có Xác nhận/Hủy | V1.3 | FR-M10-05.03, FR-M10-05.04, FR-M10-05.05, BR-M10-25 |
| V1.3 | ACT-007 | Bảo xác nhận từ chức Admin. | Chính Bảo xác nhận, không phải thao tác thu hồi của gốc | V1.4 | FR-M10-05.04 |
| V1.4 | SYSTEM | Hệ thống kiểm lại và đổi Bảo→USER, ghi log chính Bảo tự từ chức Admin, lý do tùy chọn và T, trả đã từ chức. Nhận lại cần đề xuất mới, không quay về Mod cũ. | Bảo ADMIN→USER; An gốc vẫn ADMIN; không tự đăng xuất/đổi chính sách phiên | END:SUCCESS | FR-M10-05.03, FR-M10-05.04, FR-M10-05.06, FR-M10-14.06, BR-M10-10, BR-M10-21, BR-M10-25 |


**V2 — thay toàn bộ M1 đến kết thúc:** An ADMIN gốc không được từ chức. Actor khởi tạo ACT-007; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-007 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-007 | An yêu cầu tự từ chức. | An ADMIN gốc | V2.2 | FR-M10-05.05 |
| V2.2 | SYSTEM | Hệ thống từ chối từ chức của gốc, không đổi role hoặc tạo log từ chức thành công. | An vẫn ADMIN gốc; không phải role thứ tư | END:REJECTED | FR-M10-05.05, BR-M10-10 |


**V3 — thay toàn bộ M1 đến kết thúc:** USER không phải staff. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-007 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-002 | Người yêu cầu tự từ chức vai trò. | Không có role MODERATOR hoặc ADMIN | V3.2 | FR-M10-05.02 |
| V3.2 | SYSTEM | Hệ thống từ chối từ chức khi không có role nguồn hợp lệ, không tạo thay đổi/log role. | USER không phải staff | END:REJECTED | FR-M10-05.02 |


**V4 — thay toàn bộ M1 đến kết thúc:** Guest chưa có role được từ chức. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-007 V4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V4.1 | ACT-001 | Người yêu cầu tự từ chức vai trò. | Không có role MODERATOR hoặc ADMIN | V4.2 | FR-M10-05.02 |
| V4.2 | SYSTEM | Hệ thống từ chối từ chức khi không có role nguồn hợp lệ, không tạo thay đổi/log role. | Guest chưa có role được từ chức | END:REJECTED | FR-M10-05.02 |


**V5 — thay toàn bộ M1 đến kết thúc:** Bảo ADMIN không gốc chọn Hủy sau một lần hỏi xác nhận, khác An gốc bị từ chối từ đầu. Actor khởi tạo ACT-007; END:CANCELLED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-007 V5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V5.1 | ACT-007 | Bảo chọn từ chức Admin của chính mình. | Bảo ADMIN không gốc | V5.2 | FR-M10-05.04 |
| V5.2 | SYSTEM | Hệ thống kiểm chính chủ/ADMIN không gốc rồi hỏi xác nhận một lần; chưa đổi role. | Bảo vẫn ADMIN; Xác nhận/Hủy | V5.3 | FR-M10-05.03, FR-M10-05.04, BR-M10-25 |
| V5.3 | ACT-007 | Bảo chọn Hủy. | Không xác nhận từ chức | V5.4 | FR-M10-05.03 |
| V5.4 | SYSTEM | Hệ thống kết thúc yêu cầu, giữ Bảo ADMIN không gốc; không tạo log từ chức thành công vì không đổi role. | Bảo ADMIN→ADMIN; An gốc giữ nguyên | END:CANCELLED | FR-M10-05.03, BR-M10-21, BR-M10-25 |


<!-- sc:end SC-M10-007 -->

<a id="sc-m10-008"></a>

<!-- sc:scenario SC-M10-008 -->

### SC-M10-008

#### 1. Tên kịch bản chuẩn

Điều chỉnh AI tổng hoặc một phạm vi AI riêng — BF-M10-008; owner [UC-M10-010](../../us/US-M10.md#uc-m10-010).

#### 2. Actor thực hiện

ACT-007 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Biết công tắc/giá trị; quyền ADMIN kiểm khi lưu. Chuẩn Bảo ADMIN, Tổng/Search/Moderation/Topic suggestion đều Bật; chọn tắt Search, không đụng hai riêng còn lại.

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-008 -->

| result | condition |
|---|---|
| SUCCESS | Đúng công tắc lưu bền, có hiệu lực sau đổi và log Admin; hiệu lực AI theo Tổng AND riêng, tóm tắt theo Tổng. Cách dự phòng/tạo bù thuộc owner, không khẳng định việc nền đã hoàn tất. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không có thay đổi được yêu cầu thành công. Hiệu ứng hợp lệ đã có được giữ; không tự ghi nhận thao tác thành công, xóa hồ sơ, rollback hoặc cấp quyền mới. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-008 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | Bảo đặt Search AI từ Bật sang Tắt. | Tổng=true; Search=true; Moderation=true; Topic suggestion=true; value Search=false | M2 | FR-M10-09.01, FR-M10-09.02 |
| M2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc AI/Search, lưu bền Tắt và áp cho mọi thao tác sau T, không cần triển khai lại. AI hiệu lực: Search=Tắt, Moderation=Bật, Topic suggestion=Bật; tóm tắt chỉ theo Tổng=Bật. Giữ các riêng độc lập, không reset khi đổi tổng; tắt chủ đích dùng dự phòng của owner, khác lỗi AI. Khi Tổng và Search cùng bật, M13 xử lý hàng tạo bù theo nội dung hiện tại khi AI trả lời được, không hứa đã tạo bù xong hoặc tạo bù tóm tắt. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi AI/Search, đối tượng Search, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Tắt. | Search: Bật→Tắt; thời điểm đổi T; các công tắc khác không tự reset; Tổng=True; riêng={'Search': False, 'Moderation': True, 'Topic suggestion': True}; riêng trước={'Search': True, 'Moderation': True, 'Topic suggestion': True} | END:SUCCESS | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-008 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Đổi riêng Search Bật→Tắt trong khi Tổng đang Tắt | E1.1 | FR-M10-09.06, FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E2 | user-choice | M1 | Bật riêng Search khi Tổng Bật | E2.1 | FR-M10-09.02, FR-M10-09.01, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E3 | user-choice | M1 | Đổi riêng Moderation Bật→Tắt trong khi Tổng đang Tắt | E3.1 | FR-M10-09.06, FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E4 | user-choice | M1 | Bật riêng Moderation khi Tổng Bật | E4.1 | FR-M10-09.02, FR-M10-09.01, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E5 | user-choice | M1 | Đổi riêng Topic suggestion Bật→Tắt trong khi Tổng đang Tắt | E5.1 | FR-M10-09.06, FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E6 | user-choice | M1 | Bật riêng Topic suggestion khi Tổng Bật | E6.1 | FR-M10-09.02, FR-M10-09.01, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E7 | user-choice | M1 | Bảo tắt Tổng rồi bật Tổng lại, giữ từng công tắc riêng | E7.1 | FR-M10-09.03, FR-M10-09.01, FR-M10-09.02, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E8 | user-choice | M1 | Đổi riêng khi Tổng Tắt rồi bật Tổng để dùng giá trị riêng đã lưu | E8.1 | FR-M10-09.06, FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E9 | system | M2 | Một lời gọi AI lỗi tạm thời ở module nhận, không phải cấu hình Tắt | E9.1 | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, BR-M13-07 |


<!-- sc:branch SC-M10-008 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-007 | Bảo tắt công tắc riêng Search khi Tổng đã Tắt. | Trước: Tổng=false; ba riêng=true; yêu cầu riêng=false | E1.2 | FR-M10-09.06 |
| E1.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc AI/Search, lưu bền Tắt và áp cho mọi thao tác sau T, không cần triển khai lại. AI hiệu lực: Search=Tắt, Moderation=Tắt, Topic suggestion=Tắt; tóm tắt chỉ theo Tổng=Tắt. Giữ các riêng độc lập, không reset khi đổi tổng; tắt chủ đích dùng dự phòng của owner, khác lỗi AI. Khi Tổng và Search cùng bật, M13 xử lý hàng tạo bù theo nội dung hiện tại khi AI trả lời được, không hứa đã tạo bù xong hoặc tạo bù tóm tắt. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi AI/Search, đối tượng Search, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Tắt. | Search: Bật→Tắt; thời điểm đổi T; các công tắc khác không tự reset; Tổng=False; riêng={'Search': False, 'Moderation': True, 'Topic suggestion': True}; riêng trước={'Search': True, 'Moderation': True, 'Topic suggestion': True} | END:SUCCESS | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-008 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-007 | Bảo bật riêng Search. | Tổng=true; riêng Search=false→true; riêng khác=true | E2.2 | FR-M10-09.02 |
| E2.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc AI/Search, lưu bền Bật và áp cho mọi thao tác sau T, không cần triển khai lại. AI hiệu lực: Search=Bật, Moderation=Bật, Topic suggestion=Bật; tóm tắt chỉ theo Tổng=Bật. Giữ các riêng độc lập, không reset khi đổi tổng; tắt chủ đích dùng dự phòng của owner, khác lỗi AI. Khi Tổng và Search cùng bật, M13 xử lý hàng tạo bù theo nội dung hiện tại khi AI trả lời được, không hứa đã tạo bù xong hoặc tạo bù tóm tắt. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi AI/Search, đối tượng Search, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Bật. | Search: Tắt→Bật; thời điểm đổi T; các công tắc khác không tự reset; Tổng=True; riêng={'Search': True, 'Moderation': True, 'Topic suggestion': True}; riêng trước={'Search': False, 'Moderation': True, 'Topic suggestion': True} | END:SUCCESS | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-008 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-007 | Bảo tắt công tắc riêng Moderation khi Tổng đã Tắt. | Trước: Tổng=false; ba riêng=true; yêu cầu riêng=false | E3.2 | FR-M10-09.06 |
| E3.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc AI/Moderation, lưu bền Tắt và áp cho mọi thao tác sau T, không cần triển khai lại. AI hiệu lực: Search=Tắt, Moderation=Tắt, Topic suggestion=Tắt; tóm tắt chỉ theo Tổng=Tắt. Giữ các riêng độc lập, không reset khi đổi tổng; tắt chủ đích dùng dự phòng của owner, khác lỗi AI. Khi Tổng và Search cùng bật, M13 xử lý hàng tạo bù theo nội dung hiện tại khi AI trả lời được, không hứa đã tạo bù xong hoặc tạo bù tóm tắt. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi AI/Moderation, đối tượng Moderation, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Tắt. | Moderation: Bật→Tắt; thời điểm đổi T; các công tắc khác không tự reset; Tổng=False; riêng={'Search': True, 'Moderation': False, 'Topic suggestion': True}; riêng trước={'Search': True, 'Moderation': True, 'Topic suggestion': True} | END:SUCCESS | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-008 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-007 | Bảo bật riêng Moderation. | Tổng=true; riêng Moderation=false→true; riêng khác=true | E4.2 | FR-M10-09.02 |
| E4.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc AI/Moderation, lưu bền Bật và áp cho mọi thao tác sau T, không cần triển khai lại. AI hiệu lực: Search=Bật, Moderation=Bật, Topic suggestion=Bật; tóm tắt chỉ theo Tổng=Bật. Giữ các riêng độc lập, không reset khi đổi tổng; tắt chủ đích dùng dự phòng của owner, khác lỗi AI. Khi Tổng và Search cùng bật, M13 xử lý hàng tạo bù theo nội dung hiện tại khi AI trả lời được, không hứa đã tạo bù xong hoặc tạo bù tóm tắt. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi AI/Moderation, đối tượng Moderation, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Bật. | Moderation: Tắt→Bật; thời điểm đổi T; các công tắc khác không tự reset; Tổng=True; riêng={'Search': True, 'Moderation': True, 'Topic suggestion': True}; riêng trước={'Search': True, 'Moderation': False, 'Topic suggestion': True} | END:SUCCESS | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-008 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-007 | Bảo tắt công tắc riêng Topic suggestion khi Tổng đã Tắt. | Trước: Tổng=false; ba riêng=true; yêu cầu riêng=false | E5.2 | FR-M10-09.06 |
| E5.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc AI/Topic suggestion, lưu bền Tắt và áp cho mọi thao tác sau T, không cần triển khai lại. AI hiệu lực: Search=Tắt, Moderation=Tắt, Topic suggestion=Tắt; tóm tắt chỉ theo Tổng=Tắt. Giữ các riêng độc lập, không reset khi đổi tổng; tắt chủ đích dùng dự phòng của owner, khác lỗi AI. Khi Tổng và Search cùng bật, M13 xử lý hàng tạo bù theo nội dung hiện tại khi AI trả lời được, không hứa đã tạo bù xong hoặc tạo bù tóm tắt. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi AI/Topic suggestion, đối tượng Topic suggestion, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Tắt. | Topic suggestion: Bật→Tắt; thời điểm đổi T; các công tắc khác không tự reset; Tổng=False; riêng={'Search': True, 'Moderation': True, 'Topic suggestion': False}; riêng trước={'Search': True, 'Moderation': True, 'Topic suggestion': True} | END:SUCCESS | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-008 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-007 | Bảo bật riêng Topic suggestion. | Tổng=true; riêng Topic suggestion=false→true; riêng khác=true | E6.2 | FR-M10-09.02 |
| E6.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc AI/Topic suggestion, lưu bền Bật và áp cho mọi thao tác sau T, không cần triển khai lại. AI hiệu lực: Search=Bật, Moderation=Bật, Topic suggestion=Bật; tóm tắt chỉ theo Tổng=Bật. Giữ các riêng độc lập, không reset khi đổi tổng; tắt chủ đích dùng dự phòng của owner, khác lỗi AI. Khi Tổng và Search cùng bật, M13 xử lý hàng tạo bù theo nội dung hiện tại khi AI trả lời được, không hứa đã tạo bù xong hoặc tạo bù tóm tắt. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi AI/Topic suggestion, đối tượng Topic suggestion, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Bật. | Topic suggestion: Tắt→Bật; thời điểm đổi T; các công tắc khác không tự reset; Tổng=True; riêng={'Search': True, 'Moderation': True, 'Topic suggestion': True}; riêng trước={'Search': True, 'Moderation': True, 'Topic suggestion': False} | END:SUCCESS | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-008 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | ACT-007 | Bảo tắt AI Tổng. | Tổng=true; Search=true; Moderation=false; Topic suggestion=true | E7.2 | FR-M10-09.03 |
| E7.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc AI/Tổng, lưu bền Tắt và áp cho mọi thao tác sau T1 (10/11 10:00+07), không cần triển khai lại. AI hiệu lực: Search=Tắt, Moderation=Tắt, Topic suggestion=Tắt; tóm tắt chỉ theo Tổng=Tắt. Giữ các riêng độc lập, không reset khi đổi tổng; tắt chủ đích dùng dự phòng của owner, khác lỗi AI. Khi Tổng và Search cùng bật, M13 xử lý hàng tạo bù theo nội dung hiện tại khi AI trả lời được, không hứa đã tạo bù xong hoặc tạo bù tóm tắt. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi AI/Tổng, đối tượng Tổng, lý do tùy chọn không nhập, thời điểm T1 (10/11 10:00+07); giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Tắt. | Tổng: Bật→Tắt; thời điểm đổi T1 (10/11 10:00+07); các công tắc khác không tự reset; Tổng=False; riêng={'Search': True, 'Moderation': False, 'Topic suggestion': True}; riêng trước={'Search': True, 'Moderation': False, 'Topic suggestion': True} | E7.3 | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E7.3 | ACT-007 | Bảo bật lại AI Tổng ở lần thay đổi tiếp theo. | Tổng=false→true; riêng lưu Search=true, Moderation=false, Topic suggestion=true; lần đổi thứ hai lúc 10:01, sau lần đổi thứ nhất 10:00 | E7.4 | FR-M10-09.02, FR-M10-09.04 |
| E7.4 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc AI/Tổng, lưu bền Bật và áp cho mọi thao tác sau T2 (10/11 10:01+07), không cần triển khai lại. AI hiệu lực: Search=Bật, Moderation=Tắt, Topic suggestion=Bật; tóm tắt chỉ theo Tổng=Bật. Giữ các riêng độc lập, không reset khi đổi tổng; tắt chủ đích dùng dự phòng của owner, khác lỗi AI. Khi Tổng và Search cùng bật, M13 xử lý hàng tạo bù theo nội dung hiện tại khi AI trả lời được, không hứa đã tạo bù xong hoặc tạo bù tóm tắt. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi AI/Tổng, đối tượng Tổng, lý do tùy chọn không nhập, thời điểm T2 (10/11 10:01+07); giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Bật. | Tổng: Tắt→Bật; thời điểm đổi T2 (10/11 10:01+07); các công tắc khác không tự reset; Tổng=True; riêng={'Search': True, 'Moderation': False, 'Topic suggestion': True}; riêng trước={'Search': True, 'Moderation': False, 'Topic suggestion': True} | END:SUCCESS | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-008 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | ACT-007 | Bảo tắt Search riêng khi Tổng Tắt. | Tổng=false; Search=true; Moderation/Topic suggestion=true | E8.2 | FR-M10-09.06 |
| E8.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc AI/Search, lưu bền Tắt và áp cho mọi thao tác sau T1 (10/11 10:00+07), không cần triển khai lại. AI hiệu lực: Search=Tắt, Moderation=Tắt, Topic suggestion=Tắt; tóm tắt chỉ theo Tổng=Tắt. Giữ các riêng độc lập, không reset khi đổi tổng; tắt chủ đích dùng dự phòng của owner, khác lỗi AI. Khi Tổng và Search cùng bật, M13 xử lý hàng tạo bù theo nội dung hiện tại khi AI trả lời được, không hứa đã tạo bù xong hoặc tạo bù tóm tắt. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi AI/Search, đối tượng Search, lý do tùy chọn không nhập, thời điểm T1 (10/11 10:00+07); giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Tắt. | Search: Bật→Tắt; thời điểm đổi T1 (10/11 10:00+07); các công tắc khác không tự reset; Tổng=False; riêng={'Search': False, 'Moderation': True, 'Topic suggestion': True}; riêng trước={'Search': True, 'Moderation': True, 'Topic suggestion': True} | E8.3 | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E8.3 | ACT-007 | Bảo bật Tổng ở lần đổi tiếp. | Tổng=false→true; riêng Search đã lưu false, hai riêng khác true; lần đổi thứ hai lúc 10:01, sau lần đổi thứ nhất 10:00 | E8.4 | FR-M10-09.02, FR-M10-09.04, FR-M10-09.06 |
| E8.4 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc AI/Tổng, lưu bền Bật và áp cho mọi thao tác sau T2 (10/11 10:01+07), không cần triển khai lại. AI hiệu lực: Search=Tắt, Moderation=Bật, Topic suggestion=Bật; tóm tắt chỉ theo Tổng=Bật. Giữ các riêng độc lập, không reset khi đổi tổng; tắt chủ đích dùng dự phòng của owner, khác lỗi AI. Khi Tổng và Search cùng bật, M13 xử lý hàng tạo bù theo nội dung hiện tại khi AI trả lời được, không hứa đã tạo bù xong hoặc tạo bù tóm tắt. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi AI/Tổng, đối tượng Tổng, lý do tùy chọn không nhập, thời điểm T2 (10/11 10:01+07); giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Bật. | Tổng: Tắt→Bật; thời điểm đổi T2 (10/11 10:01+07); các công tắc khác không tự reset; Tổng=True; riêng={'Search': False, 'Moderation': True, 'Topic suggestion': True}; riêng trước={'Search': False, 'Moderation': True, 'Topic suggestion': True} | END:SUCCESS | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-008 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc AI/Search, lưu bền Tắt và áp cho mọi thao tác sau T, không cần triển khai lại. AI hiệu lực: Search=Tắt, Moderation=Bật, Topic suggestion=Bật; tóm tắt chỉ theo Tổng=Bật. Giữ các riêng độc lập, không reset khi đổi tổng; tắt chủ đích dùng dự phòng của owner, khác lỗi AI. Khi Tổng và Search cùng bật, M13 xử lý hàng tạo bù theo nội dung hiện tại khi AI trả lời được, không hứa đã tạo bù xong hoặc tạo bù tóm tắt. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi AI/Search, đối tượng Search, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Tắt. Lỗi tạm thời của một lời gọi khác do M13/module gọi xử lý, không tự đổi thêm công tắc hoặc thêm retry tầng M10. | Search: Bật→Tắt; thời điểm đổi T; các công tắc khác không tự reset; Tổng=True; riêng={'Search': False, 'Moderation': True, 'Topic suggestion': True}; riêng trước={'Search': True, 'Moderation': True, 'Topic suggestion': True} | END:SUCCESS | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, BR-M13-07 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-008 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Người yêu cầu chọn điều chỉnh ai tổng hoặc một phạm vi ai riêng. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V1.2 | FR-M10-09.08, BR-M10-02 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-09.08, BR-M10-02 |


**V2 — thay toàn bộ M1 đến kết thúc:** User thường. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-008 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-002 | Người yêu cầu chọn điều chỉnh ai tổng hoặc một phạm vi ai riêng. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V2.2 | FR-M10-09.08, BR-M10-02 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-09.08, BR-M10-02 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mod hệ thống (kể cả Owner/Group Mod/Admin nhóm chat nhưng không ADMIN hệ thống). Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-008 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-008 | Người yêu cầu chọn điều chỉnh ai tổng hoặc một phạm vi ai riêng. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V3.2 | FR-M10-09.08, BR-M10-02 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-09.08, BR-M10-02 |


<!-- sc:end SC-M10-008 -->

<a id="sc-m10-009"></a>

<!-- sc:scenario SC-M10-009 -->

### SC-M10-009

#### 1. Tên kịch bản chuẩn

Bật hoặc tắt chế độ bảo trì — BF-M10-009; owner [UC-M10-011](../../us/US-M10.md#uc-m10-011).

#### 2. Actor thực hiện

ACT-007 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Có yêu cầu cấu hình; kiểm ADMIN. Chuẩn Bảo ADMIN, bảo trì Tắt; người khác có thể đã có phiên, thay đổi phải áp cả thao tác qua phiên cũ.

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-009 -->

| result | condition |
|---|---|
| SUCCESS | Bảo trì lưu/áp sau T, M01 thi hành chỉ ADMIN khi bật và bỏ rào khi tắt; log đổi công tắc có, không xóa account hoặc tự đặt logout. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không có thay đổi được yêu cầu thành công. Hiệu ứng hợp lệ đã có được giữ; không tự ghi nhận thao tác thành công, xóa hồ sơ, rollback hoặc cấp quyền mới. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-009 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | Bảo bật chế độ bảo trì. | maintenance=false→true; Bảo ADMIN | M2 | FR-M10-10.01 |
| M2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc Bảo trì/Bảo trì, lưu bền Bật và áp cho mọi thao tác sau T, không cần triển khai lại. Cung cấp M01: chỉ ADMIN đăng nhập/thao tác, người khác bị từ chối kể cả phiên đang có; không tự chọn logout. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi Bảo trì/Bảo trì, đối tượng Bảo trì, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Bật. | Bảo trì: Tắt→Bật; thời điểm đổi T; các công tắc khác không tự reset | END:SUCCESS | FR-M10-10.01, FR-M10-10.02, FR-M10-10.03, BR-M10-13, BR-M10-17, FR-M01-05.19, FR-M01-05.20, FR-M10-09.02, FR-M10-09.08, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-009 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Bảo tắt cấu hình đang Bật | E1.1 | FR-M10-10.01, FR-M10-10.02, FR-M10-10.03, BR-M10-13, BR-M10-17, FR-M01-05.19, FR-M01-05.20, FR-M10-09.02, FR-M10-09.08, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-009 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-007 | Bảo tắt Bảo trì. | Bảo trì=true→false; ADMIN | E1.2 | FR-M10-10.01 |
| E1.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc Bảo trì/Bảo trì, lưu bền Tắt và áp cho mọi thao tác sau T, không cần triển khai lại. Cung cấp M01: không áp rào bảo trì nữa, các quyền/trạng thái M01 khác vẫn kiểm; không cấp quyền mới. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi Bảo trì/Bảo trì, đối tượng Bảo trì, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Tắt. | Bảo trì: Bật→Tắt; thời điểm đổi T; các công tắc khác không tự reset | END:SUCCESS | FR-M10-10.01, FR-M10-10.02, FR-M10-10.03, BR-M10-13, BR-M10-17, FR-M01-05.19, FR-M01-05.20, FR-M10-09.02, FR-M10-09.08, FR-M10-11.01, FR-M10-11.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-009 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Người yêu cầu chọn bật hoặc tắt chế độ bảo trì. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V1.2 | FR-M10-10.03, BR-M10-02 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-10.03, BR-M10-02 |


**V2 — thay toàn bộ M1 đến kết thúc:** User thường. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-009 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-002 | Người yêu cầu chọn bật hoặc tắt chế độ bảo trì. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V2.2 | FR-M10-10.03, BR-M10-02 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-10.03, BR-M10-02 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mod hệ thống (kể cả Owner/Group Mod/Admin nhóm chat nhưng không ADMIN hệ thống). Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-009 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-008 | Người yêu cầu chọn bật hoặc tắt chế độ bảo trì. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V3.2 | FR-M10-10.03, BR-M10-02 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-10.03, BR-M10-02 |


<!-- sc:end SC-M10-009 -->

<a id="sc-m10-010"></a>

<!-- sc:scenario SC-M10-010 -->

### SC-M10-010

#### 1. Tên kịch bản chuẩn

Bật hoặc tắt tạm dừng đăng ký mới — BF-M10-010; owner [UC-M10-012](../../us/US-M10.md#uc-m10-012).

#### 2. Actor thực hiện

ACT-007 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Có yêu cầu cấu hình; kiểm ADMIN. Chuẩn Bảo ADMIN, pause Tắt; đây là mục riêng, không cờ tính năng M01.

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-010 -->

| result | condition |
|---|---|
| SUCCESS | Cấu hình lưu/áp sau T, chặn tài khoản mới khi bật nhưng giữ các ngoại lệ liên kết/tiếp đăng ký; log đúng, không chặn toàn bộ đăng nhập. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không có thay đổi được yêu cầu thành công. Hiệu ứng hợp lệ đã có được giữ; không tự ghi nhận thao tác thành công, xóa hồ sơ, rollback hoặc cấp quyền mới. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-010 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | Bảo bật tạm dừng đăng ký. | pause=false→true; có người đã xong bước 1 trước T | M2 | FR-M10-11.01 |
| M2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc Tạm dừng đăng ký/Tạm dừng đăng ký, lưu bền Bật và áp cho mọi thao tác sau T, không cần triển khai lại. Cung cấp M01: từ chối email mới/Google lần đầu tạo account; vẫn cho liên kết Google vào account sẵn có và tiếp bước 2/3 khi đã xong bước 1. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi Tạm dừng đăng ký/Tạm dừng đăng ký, đối tượng Tạm dừng đăng ký, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Bật. | Tạm dừng đăng ký: Tắt→Bật; thời điểm đổi T; các công tắc khác không tự reset | END:SUCCESS | FR-M10-11.01, FR-M10-11.02, FR-M10-11.03, BR-M10-13, BR-M10-18, FR-M01-01.08, FR-M01-01.09, FR-M01-04.10, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-010 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Bảo tắt cấu hình đang Bật | E1.1 | FR-M10-11.01, FR-M10-11.02, FR-M10-11.03, BR-M10-13, BR-M10-18, FR-M01-01.08, FR-M01-01.09, FR-M01-04.10, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-010 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-007 | Bảo tắt Tạm dừng đăng ký. | Tạm dừng đăng ký=true→false; ADMIN | E1.2 | FR-M10-11.01 |
| E1.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc Tạm dừng đăng ký/Tạm dừng đăng ký, lưu bền Tắt và áp cho mọi thao tác sau T, không cần triển khai lại. Cung cấp M01: nhận lại đăng ký mới theo điều kiện M01, không bỏ xác minh/điều kiện khác; không phát lại yêu cầu đã bị từ chối. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi Tạm dừng đăng ký/Tạm dừng đăng ký, đối tượng Tạm dừng đăng ký, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Tắt. | Tạm dừng đăng ký: Bật→Tắt; thời điểm đổi T; các công tắc khác không tự reset | END:SUCCESS | FR-M10-11.01, FR-M10-11.02, FR-M10-11.03, BR-M10-13, BR-M10-18, FR-M01-01.08, FR-M01-01.09, FR-M01-04.10, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-12.01, FR-M10-12.02, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-010 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Người yêu cầu chọn bật hoặc tắt tạm dừng đăng ký mới. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V1.2 | FR-M10-11.03, BR-M10-02 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-11.03, BR-M10-02 |


**V2 — thay toàn bộ M1 đến kết thúc:** User thường. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-010 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-002 | Người yêu cầu chọn bật hoặc tắt tạm dừng đăng ký mới. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V2.2 | FR-M10-11.03, BR-M10-02 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-11.03, BR-M10-02 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mod hệ thống (kể cả Owner/Group Mod/Admin nhóm chat nhưng không ADMIN hệ thống). Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-010 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-008 | Người yêu cầu chọn bật hoặc tắt tạm dừng đăng ký mới. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V3.2 | FR-M10-11.03, BR-M10-02 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-11.03, BR-M10-02 |


<!-- sc:end SC-M10-010 -->

<a id="sc-m10-011"></a>

<!-- sc:scenario SC-M10-011 -->

### SC-M10-011

#### 1. Tên kịch bản chuẩn

Bật hoặc tắt cờ Group, Chat hoặc Gamification — BF-M10-011; owner [UC-M10-013](../../us/US-M10.md#uc-m10-013).

#### 2. Actor thực hiện

ACT-007 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Chọn đúng một trong ba cờ; kiểm ADMIN. Chuẩn Bảo ADMIN, cờ Group Bật→Tắt; dữ liệu có sẵn giữ, không bắt tác vụ nền dừng theo người dùng.

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-011 -->

| result | condition |
|---|---|
| SUCCESS | Đúng cờ lưu/áp sau T và log; người không Admin bị chặn theo owner, lối vào/dữ liệu/việc nền/kiểm duyệt giữ, Admin qua rào cờ vẫn theo quyền; bật lại không tính bù. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không có thay đổi được yêu cầu thành công. Hiệu ứng hợp lệ đã có được giữ; không tự ghi nhận thao tác thành công, xóa hồ sơ, rollback hoặc cấp quyền mới. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-011 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | Bảo tắt cờ Group. | Group=true→false; Chat/Gamification vẫn true | M2 | FR-M10-12.01 |
| M2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc Cờ tính năng/Group, lưu bền Tắt và áp cho mọi thao tác sau T, không cần triển khai lại. Tắt Group: người không ADMIN bị chặn theo owner và hiện “Hệ thống đang bận, vui lòng thử lại sau”; lối vào còn; dữ liệu giữ nguyên, việc tự làm/kiểm duyệt liên quan vẫn chạy; ADMIN dùng như khi bật, vẫn phải đúng quyền/sở hữu/thành viên theo owner. Chi tiết tại RULE-M10-004, không thiết kế nghiệp vụ module đó trong lượt đổi cờ. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi Cờ tính năng/Group, đối tượng Group, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Tắt. | Group: Bật→Tắt; thời điểm đổi T; các công tắc khác không tự reset | END:SUCCESS | FR-M10-12.01, FR-M10-12.02, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M10-12.08, BR-M10-13, BR-M10-19, BR-M10-28, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-011 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Bảo bật lại cờ Group | E1.1 | FR-M10-12.01, FR-M10-12.07, FR-M10-12.02, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.08, BR-M10-13, BR-M10-19, BR-M10-28, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E2 | user-choice | M1 | Bảo tắt cờ Chat | E2.1 | FR-M10-12.01, FR-M10-12.02, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M10-12.08, BR-M10-13, BR-M10-19, BR-M10-28, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E3 | user-choice | M1 | Bảo bật lại cờ Chat | E3.1 | FR-M10-12.01, FR-M10-12.07, FR-M10-12.02, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.08, BR-M10-13, BR-M10-19, BR-M10-28, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E4 | user-choice | M1 | Bảo tắt cờ Gamification | E4.1 | FR-M10-12.01, FR-M10-12.02, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M10-12.08, BR-M10-13, BR-M10-19, BR-M10-28, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E5 | user-choice | M1 | Bảo bật lại cờ Gamification | E5.1 | FR-M10-12.01, FR-M10-12.07, FR-M10-12.02, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.08, BR-M10-13, BR-M10-19, BR-M10-28, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-011 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-007 | Bảo bật lại cờ Group. | Group=false→true; dữ liệu/việc nền đã giữ trong lúc tắt | E1.2 | FR-M10-12.01, FR-M10-12.07 |
| E1.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc Cờ tính năng/Group, lưu bền Bật và áp cho mọi thao tác sau T, không cần triển khai lại. Bật lại Group: bỏ rào do cờ, giữ dữ liệu hiện tại và việc tự làm đã diễn ra; không tính bù/phát lại thao tác từng bị chặn, quyền owner khác vẫn kiểm. Chi tiết tại RULE-M10-004, không thiết kế nghiệp vụ module đó trong lượt đổi cờ. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi Cờ tính năng/Group, đối tượng Group, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Bật. | Group: Tắt→Bật; thời điểm đổi T; các công tắc khác không tự reset | END:SUCCESS | FR-M10-12.01, FR-M10-12.02, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M10-12.08, BR-M10-13, BR-M10-19, BR-M10-28, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-011 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-007 | Bảo tắt cờ Chat. | Chat=true→false; cờ khác giữ | E2.2 | FR-M10-12.01 |
| E2.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc Cờ tính năng/Chat, lưu bền Tắt và áp cho mọi thao tác sau T, không cần triển khai lại. Tắt Chat: người không ADMIN bị chặn theo owner và hiện “Hệ thống đang bận, vui lòng thử lại sau”; lối vào còn; dữ liệu giữ nguyên, việc tự làm/kiểm duyệt liên quan vẫn chạy; ADMIN dùng như khi bật, vẫn phải đúng quyền/sở hữu/thành viên theo owner. Chi tiết tại RULE-M10-004, không thiết kế nghiệp vụ module đó trong lượt đổi cờ. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi Cờ tính năng/Chat, đối tượng Chat, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Tắt. | Chat: Bật→Tắt; thời điểm đổi T; các công tắc khác không tự reset | END:SUCCESS | FR-M10-12.01, FR-M10-12.02, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M10-12.08, BR-M10-13, BR-M10-19, BR-M10-28, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-011 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-007 | Bảo bật lại cờ Chat. | Chat=false→true; dữ liệu/việc nền đã giữ trong lúc tắt | E3.2 | FR-M10-12.01, FR-M10-12.07 |
| E3.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc Cờ tính năng/Chat, lưu bền Bật và áp cho mọi thao tác sau T, không cần triển khai lại. Bật lại Chat: bỏ rào do cờ, giữ dữ liệu hiện tại và việc tự làm đã diễn ra; không tính bù/phát lại thao tác từng bị chặn, quyền owner khác vẫn kiểm. Chi tiết tại RULE-M10-004, không thiết kế nghiệp vụ module đó trong lượt đổi cờ. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi Cờ tính năng/Chat, đối tượng Chat, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Bật. | Chat: Tắt→Bật; thời điểm đổi T; các công tắc khác không tự reset | END:SUCCESS | FR-M10-12.01, FR-M10-12.02, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M10-12.08, BR-M10-13, BR-M10-19, BR-M10-28, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-011 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-007 | Bảo tắt cờ Gamification. | Gamification=true→false; cờ khác giữ | E4.2 | FR-M10-12.01 |
| E4.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc Cờ tính năng/Gamification, lưu bền Tắt và áp cho mọi thao tác sau T, không cần triển khai lại. Tắt Gamification: người không ADMIN bị chặn theo owner và hiện “Hệ thống đang bận, vui lòng thử lại sau”; lối vào còn; dữ liệu giữ nguyên, việc tự làm/kiểm duyệt liên quan vẫn chạy; ADMIN dùng như khi bật, vẫn phải đúng quyền/sở hữu/thành viên theo owner. Chi tiết tại RULE-M10-004, không thiết kế nghiệp vụ module đó trong lượt đổi cờ. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi Cờ tính năng/Gamification, đối tượng Gamification, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Tắt. | Gamification: Bật→Tắt; thời điểm đổi T; các công tắc khác không tự reset | END:SUCCESS | FR-M10-12.01, FR-M10-12.02, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M10-12.08, BR-M10-13, BR-M10-19, BR-M10-28, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-011 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-007 | Bảo bật lại cờ Gamification. | Gamification=false→true; dữ liệu/việc nền đã giữ trong lúc tắt | E5.2 | FR-M10-12.01, FR-M10-12.07 |
| E5.2 | SYSTEM | Hệ thống kiểm quyền ADMIN hiện tại và đúng công tắc Cờ tính năng/Gamification, lưu bền Bật và áp cho mọi thao tác sau T, không cần triển khai lại. Bật lại Gamification: bỏ rào do cờ, giữ dữ liệu hiện tại và việc tự làm đã diễn ra; không tính bù/phát lại thao tác từng bị chặn, quyền owner khác vẫn kiểm. Chi tiết tại RULE-M10-004, không thiết kế nghiệp vụ module đó trong lượt đổi cờ. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đổi Cờ tính năng/Gamification, đối tượng Gamification, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. Trả trạng thái đã lưu Bật. | Gamification: Tắt→Bật; thời điểm đổi T; các công tắc khác không tự reset | END:SUCCESS | FR-M10-12.01, FR-M10-12.02, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M10-12.08, BR-M10-13, BR-M10-19, BR-M10-28, FR-M10-09.02, FR-M10-09.08, FR-M10-10.01, FR-M10-10.03, FR-M10-11.01, FR-M10-11.03, BR-M10-02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-011 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Người yêu cầu chọn bật hoặc tắt cờ group, chat hoặc gamification. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V1.2 | FR-M10-12.02, BR-M10-02 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-12.02, BR-M10-02 |


**V2 — thay toàn bộ M1 đến kết thúc:** User thường. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-011 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-002 | Người yêu cầu chọn bật hoặc tắt cờ group, chat hoặc gamification. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V2.2 | FR-M10-12.02, BR-M10-02 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-12.02, BR-M10-02 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mod hệ thống (kể cả Owner/Group Mod/Admin nhóm chat nhưng không ADMIN hệ thống). Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-011 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-008 | Người yêu cầu chọn bật hoặc tắt cờ group, chat hoặc gamification. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V3.2 | FR-M10-12.02, BR-M10-02 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-12.02, BR-M10-02 |


<!-- sc:end SC-M10-011 -->

<a id="sc-m10-012"></a>

<!-- sc:scenario SC-M10-012 -->

### SC-M10-012

#### 1. Tên kịch bản chuẩn

Đặt mới hoặc sửa nội dung banner toàn trang — BF-M10-012; owner [UC-M10-015](../../us/US-M10.md#uc-m10-015).

#### 2. Actor thực hiện

ACT-007 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Có nội dung/yêu cầu, kiểm ADMIN và độ dài khi xử lý. Chuẩn chưa có banner, Bảo đặt nội dung ASCII hợp lệ; các trường hợp Unicode/sửa nhưng không đổi nội dung còn GAP003.

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-012 -->

| result | condition |
|---|---|
| SUCCESS | Tối đa một banner văn bản thuần 1–200 ký tự sau trim được công bố/thay nội dung, hiện lại cho người đã đóng khi nội dung đổi/đặt mới; log Admin. Không hẹn giờ hoặc giữ nhiều banner. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không có thay đổi được yêu cầu thành công. Hiệu ứng hợp lệ đã có được giữ; không tự ghi nhận thao tác thành công, xóa hồ sơ, rollback hoặc cấp quyền mới. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-012 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | Bảo nhập nội dung và yêu cầu đặt banner. | Nội dung=Bao tri he thong luc 22:00.; chưa có banner; không lý do bắt buộc | M2 | FR-M10-13.01, FR-M10-13.05, FR-M10-13.06 |
| M2 | SYSTEM | Hệ thống kiểm ADMIN và nội dung sau trim dài 1–200 ký tự, lưu/hiện dạng văn bản thuần. Đặt nội dung mới, nếu đang có thì thay banner cũ, không có hai banner đồng thời. Hiện nội dung mới/đã sửa với mọi người kể cả Guest và người đã đóng bản cũ; trả kết quả công bố, không bắt người xem tương tác trong phiên Admin. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đặt banner, đối tượng banner hiện hành, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | Trước=không có banner; sau=Đang hiện; nội dung=Bao tri he thong luc 22:00.; chỉ một banner; snapshot ký tự biên dùng ASCII để không quyết đơn vị Unicode | END:SUCCESS | FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.05, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-012 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Đặt mới khi có banner hiện hành | E1.1 | FR-M10-13.04, FR-M10-13.01, FR-M10-13.03, FR-M10-13.05, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E2 | user-choice | M1 | Sửa nội dung khác với bản hiện hành | E2.1 | FR-M10-13.09, FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.05, FR-M10-13.06, FR-M10-13.08, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E3 | user-choice | M1 | Đặt nội dung ASCII dài 1 ký tự | E3.1 | FR-M10-13.05, FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E4 | user-choice | M1 | Đặt nội dung ASCII dài 200 ký tự | E4.1 | FR-M10-13.05, FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E5 | system | M2 | Trống; Bảo sửa nội dung để hoàn tất | E5.1 | FR-M10-13.05, FR-M10-13.01, BR-M10-20, FR-M10-13.03, FR-M10-13.04, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E6 | system | M2 | Chỉ khoảng trắng; Bảo sửa nội dung để hoàn tất | E6.1 | FR-M10-13.05, FR-M10-13.01, BR-M10-20, FR-M10-13.03, FR-M10-13.04, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E7 | system | M2 | Quá 200 ký tự; Bảo sửa nội dung để hoàn tất | E7.1 | FR-M10-13.05, FR-M10-13.01, BR-M10-20, FR-M10-13.03, FR-M10-13.04, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| E8 | user-choice | M1 | Nội dung trông giống cú pháp đánh dấu nhưng chỉ hiển thị thuần | E8.1 | FR-M10-13.06, FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.05, FR-M10-13.08, FR-M10-13.09, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-012 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-007 | Bảo đặt banner mới thay thông báo cũ. | Banner B099 đang hiện, một số người đã đóng; nhập Bao tri he thong luc 22:00. | E1.2 | FR-M10-13.04 |
| E1.2 | SYSTEM | Hệ thống kiểm ADMIN và nội dung sau trim dài 1–200 ký tự, lưu/hiện dạng văn bản thuần. Đặt nội dung mới, nếu đang có thì thay banner cũ, không có hai banner đồng thời. Hiện nội dung mới/đã sửa với mọi người kể cả Guest và người đã đóng bản cũ; trả kết quả công bố, không bắt người xem tương tác trong phiên Admin. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đặt banner, đối tượng banner hiện hành, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | Trước=B099 Đang hiện, nội dung Cu, có người đã đóng; sau=Đang hiện; nội dung=Bao tri he thong luc 22:00.; chỉ một banner; snapshot ký tự biên dùng ASCII để không quyết đơn vị Unicode | END:SUCCESS | FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.05, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-012 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-007 | Bảo sửa nội dung banner đang hiện. | B099 đang hiện “Cu”; nội dung mới “Thong bao moi.”; người xem từng đóng bản Cu | E2.2 | FR-M10-13.09 |
| E2.2 | SYSTEM | Hệ thống kiểm ADMIN và nội dung sau trim dài 1–200 ký tự, lưu/hiện dạng văn bản thuần. Thay nội dung banner đang hiện trên mọi trang. Hiện nội dung mới/đã sửa với mọi người kể cả Guest và người đã đóng bản cũ; trả kết quả công bố, không bắt người xem tương tác trong phiên Admin. Ghi thêm nhật ký Admin: người làm Bảo, thao tác sửa banner, đối tượng banner hiện hành, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | Trước=B099 nội dung Cu, có người đã đóng; sau=Đang hiện; nội dung=Thong bao moi.; chỉ một banner; snapshot ký tự biên dùng ASCII để không quyết đơn vị Unicode | END:SUCCESS | FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.05, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-012 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-007 | Bảo đặt nội dung ở biên độ dài hợp lệ. | Nội dung=X; sau trim=1 ký tự ASCII | E3.2 | FR-M10-13.05 |
| E3.2 | SYSTEM | Hệ thống kiểm ADMIN và nội dung sau trim dài 1–200 ký tự, lưu/hiện dạng văn bản thuần. Đặt nội dung mới, nếu đang có thì thay banner cũ, không có hai banner đồng thời. Hiện nội dung mới/đã sửa với mọi người kể cả Guest và người đã đóng bản cũ; trả kết quả công bố, không bắt người xem tương tác trong phiên Admin. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đặt banner, đối tượng banner hiện hành, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | Trước=không có banner; sau=Đang hiện; nội dung=X; chỉ một banner; snapshot ký tự biên dùng ASCII để không quyết đơn vị Unicode | END:SUCCESS | FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.05, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-012 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-007 | Bảo đặt nội dung ở biên độ dài hợp lệ. | Nội dung=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA; sau trim=200 ký tự ASCII | E4.2 | FR-M10-13.05 |
| E4.2 | SYSTEM | Hệ thống kiểm ADMIN và nội dung sau trim dài 1–200 ký tự, lưu/hiện dạng văn bản thuần. Đặt nội dung mới, nếu đang có thì thay banner cũ, không có hai banner đồng thời. Hiện nội dung mới/đã sửa với mọi người kể cả Guest và người đã đóng bản cũ; trả kết quả công bố, không bắt người xem tương tác trong phiên Admin. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đặt banner, đối tượng banner hiện hành, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | Trước=không có banner; sau=Đang hiện; nội dung=AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA; chỉ một banner; snapshot ký tự biên dùng ASCII để không quyết đơn vị Unicode | END:SUCCESS | FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.05, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-012 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối nội dung không đạt 1–200 ký tự sau trim; chưa công bố/thay banner hoặc ghi log đặt thành công. | chuỗi rỗng | E5.2 | FR-M10-13.05 |
| E5.2 | ACT-007 | Bảo thay bằng nội dung hợp lệ và gửi lại. | Nội dung=Bao tri he thong luc 22:00.; chưa có banner trong snapshot nhánh | E5.3 | FR-M10-13.01, FR-M10-13.05, BR-M10-20 |
| E5.3 | SYSTEM | Hệ thống kiểm ADMIN và nội dung sau trim dài 1–200 ký tự, lưu/hiện dạng văn bản thuần. Đặt nội dung mới, nếu đang có thì thay banner cũ, không có hai banner đồng thời. Hiện nội dung mới/đã sửa với mọi người kể cả Guest và người đã đóng bản cũ; trả kết quả công bố, không bắt người xem tương tác trong phiên Admin. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đặt banner, đối tượng banner hiện hành, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | Trước=không có banner; sau=Đang hiện; nội dung=Bao tri he thong luc 22:00.; chỉ một banner; snapshot ký tự biên dùng ASCII để không quyết đơn vị Unicode | END:SUCCESS | FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.05, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-012 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối nội dung không đạt 1–200 ký tự sau trim; chưa công bố/thay banner hoặc ghi log đặt thành công. | 3 dấu cách, sau trim 0 | E6.2 | FR-M10-13.05 |
| E6.2 | ACT-007 | Bảo thay bằng nội dung hợp lệ và gửi lại. | Nội dung=Bao tri he thong luc 22:00.; chưa có banner trong snapshot nhánh | E6.3 | FR-M10-13.01, FR-M10-13.05, BR-M10-20 |
| E6.3 | SYSTEM | Hệ thống kiểm ADMIN và nội dung sau trim dài 1–200 ký tự, lưu/hiện dạng văn bản thuần. Đặt nội dung mới, nếu đang có thì thay banner cũ, không có hai banner đồng thời. Hiện nội dung mới/đã sửa với mọi người kể cả Guest và người đã đóng bản cũ; trả kết quả công bố, không bắt người xem tương tác trong phiên Admin. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đặt banner, đối tượng banner hiện hành, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | Trước=không có banner; sau=Đang hiện; nội dung=Bao tri he thong luc 22:00.; chỉ một banner; snapshot ký tự biên dùng ASCII để không quyết đơn vị Unicode | END:SUCCESS | FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.05, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-012 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối nội dung không đạt 1–200 ký tự sau trim; chưa công bố/thay banner hoặc ghi log đặt thành công. | 201 chữ A, sau trim 201 | E7.2 | FR-M10-13.05 |
| E7.2 | ACT-007 | Bảo thay bằng nội dung hợp lệ và gửi lại. | Nội dung=Bao tri he thong luc 22:00.; chưa có banner trong snapshot nhánh | E7.3 | FR-M10-13.01, FR-M10-13.05, BR-M10-20 |
| E7.3 | SYSTEM | Hệ thống kiểm ADMIN và nội dung sau trim dài 1–200 ký tự, lưu/hiện dạng văn bản thuần. Đặt nội dung mới, nếu đang có thì thay banner cũ, không có hai banner đồng thời. Hiện nội dung mới/đã sửa với mọi người kể cả Guest và người đã đóng bản cũ; trả kết quả công bố, không bắt người xem tương tác trong phiên Admin. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đặt banner, đối tượng banner hiện hành, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | Trước=không có banner; sau=Đang hiện; nội dung=Bao tri he thong luc 22:00.; chỉ một banner; snapshot ký tự biên dùng ASCII để không quyết đơn vị Unicode | END:SUCCESS | FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.05, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-012 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | ACT-007 | Bảo đặt chuỗi `**Thong bao**`. | 13 ký tự ASCII tính cả dấu *; không phải yêu cầu định dạng Markdown | E8.2 | FR-M10-13.06 |
| E8.2 | SYSTEM | Hệ thống kiểm ADMIN và nội dung sau trim dài 1–200 ký tự, lưu/hiện dạng văn bản thuần. Đặt nội dung mới, nếu đang có thì thay banner cũ, không có hai banner đồng thời. Hiện nội dung mới/đã sửa với mọi người kể cả Guest và người đã đóng bản cũ; trả kết quả công bố, không bắt người xem tương tác trong phiên Admin. Ghi thêm nhật ký Admin: người làm Bảo, thao tác đặt banner, đối tượng banner hiện hành, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | Trước=không có banner; sau=Đang hiện; nội dung=`**Thong bao**`; chỉ một banner; snapshot ký tự biên dùng ASCII để không quyết đơn vị Unicode | END:SUCCESS | FR-M10-13.01, FR-M10-13.03, FR-M10-13.04, FR-M10-13.05, FR-M10-13.06, FR-M10-13.08, FR-M10-13.09, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-012 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Người yêu cầu chọn đặt mới hoặc sửa nội dung banner toàn trang. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V1.2 | FR-M10-13.03, BR-M10-02 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-13.03, BR-M10-02 |


**V2 — thay toàn bộ M1 đến kết thúc:** User thường. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-012 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-002 | Người yêu cầu chọn đặt mới hoặc sửa nội dung banner toàn trang. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V2.2 | FR-M10-13.03, BR-M10-02 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-13.03, BR-M10-02 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mod hệ thống (kể cả Owner/Group Mod/Admin nhóm chat nhưng không ADMIN hệ thống). Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-012 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-008 | Người yêu cầu chọn đặt mới hoặc sửa nội dung banner toàn trang. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V3.2 | FR-M10-13.03, BR-M10-02 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-13.03, BR-M10-02 |


<!-- sc:end SC-M10-012 -->

<a id="sc-m10-013"></a>

<!-- sc:scenario SC-M10-013 -->

### SC-M10-013

#### 1. Tên kịch bản chuẩn

Gỡ banner cho toàn hệ thống — BF-M10-013; owner [UC-M10-016](../../us/US-M10.md#uc-m10-016).

#### 2. Actor thực hiện

ACT-007 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Có banner Đang hiện; quyền ADMIN kiểm trong luồng. Chuẩn Bảo gỡ banner mang nội dung Bao tri he thong luc 22:00.

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-013 -->

| result | condition |
|---|---|
| SUCCESS | Banner Không hiện toàn trang, log gỡ của Admin có; không gán đây là đóng cá nhân hoặc chính sách xóa lịch sử. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không có thay đổi được yêu cầu thành công. Hiệu ứng hợp lệ đã có được giữ; không tự ghi nhận thao tác thành công, xóa hồ sơ, rollback hoặc cấp quyền mới. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-013 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | Bảo chọn Gỡ banner đang hiện. | Banner Đang hiện cho mọi trang; actor ADMIN | M2 | FR-M10-13.02 |
| M2 | SYSTEM | Hệ thống kiểm ADMIN rồi đặt banner Không hiện trên mọi trang cho mọi người, trả đã gỡ; đây là gỡ toàn hệ thống, khác người xem đóng riêng. Không suy diễn xóa cứng lịch sử banner. Ghi thêm nhật ký Admin: người làm Bảo, thao tác gỡ banner, đối tượng banner hiện hành, lý do tùy chọn không nhập, thời điểm T; giữ vĩnh viễn, không sửa/xóa. | Banner Đang hiện→Không hiện; không có banner hiện thay thế | END:SUCCESS | FR-M10-13.02, FR-M10-13.03, BR-M10-20, FR-M10-14.01, FR-M10-14.02, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-013 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|



**V1 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-013 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Người yêu cầu chọn gỡ banner cho toàn hệ thống. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V1.2 | FR-M10-13.03, BR-M10-02 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-13.03, BR-M10-02 |


**V2 — thay toàn bộ M1 đến kết thúc:** User thường. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-013 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-002 | Người yêu cầu chọn gỡ banner cho toàn hệ thống. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V2.2 | FR-M10-13.03, BR-M10-02 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-13.03, BR-M10-02 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mod hệ thống (kể cả Owner/Group Mod/Admin nhóm chat nhưng không ADMIN hệ thống). Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-013 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-008 | Người yêu cầu chọn gỡ banner cho toàn hệ thống. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V3.2 | FR-M10-13.03, BR-M10-02 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-13.03, BR-M10-02 |


<!-- sc:end SC-M10-013 -->

<a id="sc-m10-014"></a>

<!-- sc:scenario SC-M10-014 -->

### SC-M10-014

#### 1. Tên kịch bản chuẩn

Xem và đóng riêng banner hiện tại — BF-M10-014; owner [UC-M10-017](../../us/US-M10.md#uc-m10-017).

#### 2. Actor thực hiện

ACT-001 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Có ngữ cảnh trang/người xem; không đòi đăng nhập. Chuẩn Guest dùng trình duyệt C1, banner B100 Đang hiện, chưa đóng bản hiện tại; trang được truy cập theo quyền owner.

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-014 -->

| result | condition |
|---|---|
| SUCCESS | Banner được hiển thị hoặc không hiển thị đúng bản/người xem; nếu đóng thì bản ấy không hiện lại trong phạm vi nguồn, người khác không bị ảnh hưởng, bản đổi nội dung/đặt mới hiện lại. Guest phạm vi trình duyệt; lưu/đồng bộ người đăng nhập chưa chốt GAP002. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không có thay đổi được yêu cầu thành công. Hiệu ứng hợp lệ đã có được giữ; không tự ghi nhận thao tác thành công, xóa hồ sơ, rollback hoặc cấp quyền mới. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-014 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-001 | Guest mở một trang iShare được phép xem. | Browser C1; banner B100 hiện hành, chưa đóng | M2 | FR-M10-13.01 |
| M2 | SYSTEM | Hệ thống trả trang cùng banner B100 dạng văn bản thuần vì đang hiện/chưa đóng trong trình duyệt C1; không tạo log Admin chỉ vì xem. | B100=Bao tri he thong luc 22:00.; chưa ghi dấu đóng; mọi người khác giữ trạng thái riêng | M3 | FR-M10-13.01, FR-M10-13.06, FR-M10-13.07, FR-M10-14.08, BR-M10-20 |
| M3 | ACT-001 | Guest chọn đóng B100. | Người xem trên C1 chỉ muốn ngừng thấy bản B100 hiện tại | M4 | FR-M10-13.07 |
| M4 | SYSTEM | Hệ thống ghi nhận B100 đã đóng trong trình duyệt C1 và không hiện lại bản đó cho Guest ở C1; giữ công bố cho người khác, không gỡ toàn trang. Nội dung sửa/đặt mới sẽ hiện lại, không chọn cơ chế lưu dấu đóng hoặc thời hạn. | C1 đã đóng B100; C2 chưa đóng vẫn thấy B100; trạng thái công bố B100 giữ nguyên; không log Admin | END:SUCCESS | FR-M10-13.07, FR-M10-13.08, FR-M10-14.08, BR-M10-20 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-014 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M2 | Người xem chỉ đọc banner và không chọn đóng | E1.1 | FR-M10-13.01, FR-M10-13.06, FR-M10-13.07, FR-M10-14.08, BR-M10-20 |
| E2 | system | M2 | Hiện không có banner được công bố | E2.1 | FR-M10-13.02, FR-M10-13.07, BR-M10-20 |
| E3 | system | M2 | Guest đã đóng đúng bản B100 trong trình duyệt C1 | E3.1 | FR-M10-13.02, FR-M10-13.07, BR-M10-20 |
| E4 | system | M2 | Admin đã sửa nội dung hoặc đặt bản mới sau khi C1 đóng B099 | E4.1 | FR-M10-13.01, FR-M10-13.06, FR-M10-13.08, BR-M10-20 |
| E5 | user-choice | M4 | Guest mở trang khác cùng C1 sau khi đóng | E5.1 | FR-M10-13.07, BR-M10-20, FR-M10-13.08 |


<!-- sc:branch SC-M10-014 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống trả trang với B100 văn bản thuần đang hiện, không tạo dấu đóng chỉ vì mở trang hoặc thêm log Admin. | C1 chưa đóng B100; nội dung Bao tri he thong luc 22:00.; giữ công bố và trạng thái chưa đóng | END:SUCCESS | FR-M10-13.01, FR-M10-13.06, FR-M10-13.07, FR-M10-14.08, BR-M10-20 |


<!-- sc:branch SC-M10-014 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống trả trang không hiện banner cho người xem theo trạng thái hiện tại; không tạo banner mới hoặc sửa công bố cho người khác. | Hiện không có banner được công bố; C1, không áp dấu đóng của C1 cho C2 | END:SUCCESS | FR-M10-13.02, FR-M10-13.07, BR-M10-20 |


<!-- sc:branch SC-M10-014 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống trả trang không hiện banner cho người xem theo trạng thái hiện tại; không tạo banner mới hoặc sửa công bố cho người khác. | Guest đã đóng đúng bản B100 trong trình duyệt C1; C1, không áp dấu đóng của C1 cho C2 | END:SUCCESS | FR-M10-13.02, FR-M10-13.07, BR-M10-20 |


<!-- sc:branch SC-M10-014 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống trả B100 nội dung mới dạng thuần dù C1 đã đóng B099; không tự gọi chức năng quản trị từ lượt xem. B100 chưa đóng ở C1. | Sự kiện trước lượt xem: Bảo thay bản Cu bằng B100=Bao tri he thong luc 22:00.; C1 đóng Cu, không phải B100 | M3 | FR-M10-13.01, FR-M10-13.06, FR-M10-13.08, BR-M10-20 |


<!-- sc:branch SC-M10-014 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống ghi B100 đã đóng trong C1; không ảnh hưởng công bố hoặc C2. | C1 closed B100; C2 chưa đóng | E5.2 | FR-M10-13.07, BR-M10-20 |
| E5.2 | ACT-001 | Guest mở trang khác trong C1. | Cùng browser C1, bản B100 chưa đổi nội dung | E5.3 | FR-M10-13.07 |
| E5.3 | SYSTEM | Hệ thống trả trang không hiện B100 trong C1, giữ khả năng hiện cho C2 và cho bản thay nội dung/đặt mới về sau. | C1 không B100; C2 vẫn theo dấu riêng; không chọn cookie hoặc thời hạn lưu | END:SUCCESS | FR-M10-13.07, FR-M10-13.08, BR-M10-20 |


**V1 — thay toàn bộ M1 đến kết thúc:** Lan là người xem đã đăng nhập, đóng bản hiện tại trong ngữ cảnh lượt xem; không quyết đồng bộ/qua phiên của GAP002. Actor khởi tạo ACT-002; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-014 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-002 | Lan mở trang được phép xem. | B100 Đang hiện, Lan chưa đóng bản hiện tại trong ngữ cảnh này | V1.2 | FR-M10-13.01 |
| V1.2 | SYSTEM | Hệ thống hiện B100 văn bản thuần, không yêu cầu quyền Panel hoặc ghi log xem. | B100=Bao tri he thong luc 22:00. | V1.3 | FR-M10-13.01, FR-M10-13.06, FR-M10-14.08, BR-M10-20 |
| V1.3 | ACT-002 | Lan chọn đóng B100. | Chỉ ngừng thấy bản hiện tại cho người xem này | V1.4 | FR-M10-13.07 |
| V1.4 | SYSTEM | Hệ thống ghi nhận đóng B100 cho người xem này theo phạm vi nguồn và không hiện lại bản đó trong ngữ cảnh đã đóng; giữ người khác, bản mới/sửa hiện lại. Không tự quyết theo tài khoản/thiết bị, thời hạn hoặc cơ chế lưu (GAP002). | Lan đã đóng B100; công bố toàn hệ thống vẫn giữ; không ghi log Admin cho thao tác cá nhân | END:SUCCESS | FR-M10-13.07, FR-M10-13.08, FR-M10-14.08, BR-M10-20 |


**V2 — thay toàn bộ M1 đến kết thúc:** Mai là người xem đã đăng nhập, đóng bản hiện tại trong ngữ cảnh lượt xem; không quyết đồng bộ/qua phiên của GAP002. Actor khởi tạo ACT-008; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-014 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-008 | Mai mở trang được phép xem. | B100 Đang hiện, Mai chưa đóng bản hiện tại trong ngữ cảnh này | V2.2 | FR-M10-13.01 |
| V2.2 | SYSTEM | Hệ thống hiện B100 văn bản thuần, không yêu cầu quyền Panel hoặc ghi log xem. | B100=Bao tri he thong luc 22:00. | V2.3 | FR-M10-13.01, FR-M10-13.06, FR-M10-14.08, BR-M10-20 |
| V2.3 | ACT-008 | Mai chọn đóng B100. | Chỉ ngừng thấy bản hiện tại cho người xem này | V2.4 | FR-M10-13.07 |
| V2.4 | SYSTEM | Hệ thống ghi nhận đóng B100 cho người xem này theo phạm vi nguồn và không hiện lại bản đó trong ngữ cảnh đã đóng; giữ người khác, bản mới/sửa hiện lại. Không tự quyết theo tài khoản/thiết bị, thời hạn hoặc cơ chế lưu (GAP002). | Mai đã đóng B100; công bố toàn hệ thống vẫn giữ; không ghi log Admin cho thao tác cá nhân | END:SUCCESS | FR-M10-13.07, FR-M10-13.08, FR-M10-14.08, BR-M10-20 |


**V3 — thay toàn bộ M1 đến kết thúc:** Bảo là người xem đã đăng nhập, đóng bản hiện tại trong ngữ cảnh lượt xem; không quyết đồng bộ/qua phiên của GAP002. Actor khởi tạo ACT-007; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-014 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-007 | Bảo mở trang được phép xem. | B100 Đang hiện, Bảo chưa đóng bản hiện tại trong ngữ cảnh này | V3.2 | FR-M10-13.01 |
| V3.2 | SYSTEM | Hệ thống hiện B100 văn bản thuần, không yêu cầu quyền Panel hoặc ghi log xem. | B100=Bao tri he thong luc 22:00. | V3.3 | FR-M10-13.01, FR-M10-13.06, FR-M10-14.08, BR-M10-20 |
| V3.3 | ACT-007 | Bảo chọn đóng B100. | Chỉ ngừng thấy bản hiện tại cho người xem này | V3.4 | FR-M10-13.07 |
| V3.4 | SYSTEM | Hệ thống ghi nhận đóng B100 cho người xem này theo phạm vi nguồn và không hiện lại bản đó trong ngữ cảnh đã đóng; giữ người khác, bản mới/sửa hiện lại. Không tự quyết theo tài khoản/thiết bị, thời hạn hoặc cơ chế lưu (GAP002). | Bảo đã đóng B100; công bố toàn hệ thống vẫn giữ; không ghi log Admin cho thao tác cá nhân | END:SUCCESS | FR-M10-13.07, FR-M10-13.08, FR-M10-14.08, BR-M10-20 |


<!-- sc:end SC-M10-014 -->

<a id="sc-m10-015"></a>

<!-- sc:scenario SC-M10-015 -->

### SC-M10-015

#### 1. Tên kịch bản chuẩn

Tra cứu nhật ký thao tác Admin theo tiêu chí — BF-M10-015; owner [UC-M10-023](../../us/US-M10.md#uc-m10-023).

#### 2. Actor thực hiện

ACT-007 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-007 là Admin hệ thống; dấu gốc chỉ là ngữ cảnh trên actor này. ACT-008/ACT-002 có quyền cá nhân trả lời/từ chức/banner theo guard, không được cấp Panel vì quan hệ kế thừa. Đường V thay toàn bộ khi actor khởi tạo khác; không có actor module/AI/email/clock.

#### 3. Tiền điều kiện

Có yêu cầu đọc; kiểm ADMIN. Chuẩn Bảo mở không tiêu chí để xem mọi người làm, gồm account hoặc Hệ thống; tập mẫu L1001–L1003, không đồng nhất với nhật ký kiểm duyệt hoặc nhật ký AI.

#### 4. Hậu điều kiện

<!-- sc:post SC-M10-015 -->

| result | condition |
|---|---|
| SUCCESS | Danh sách đúng quyền/tiêu chí, mới nhất trước, đủ năm trường và giờ Việt Nam được trả chỉ đọc; không tạo log đọc/lọc, không sửa/xóa bản ghi. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không có thay đổi được yêu cầu thành công. Hiệu ứng hợp lệ đã có được giữ; không tự ghi nhận thao tác thành công, xóa hồ sơ, rollback hoặc cấp quyền mới. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M10-015 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | Bảo mở nhật ký thao tác Admin, chưa chọn tiêu chí. | L1003 T−1 phút: Hệ thống/thu hồi Mod do ban/Tuấn/lý do Mất quyền Mod do ban B1003; L1002 T−2 phút: Minh/chấp nhận đề xuất Mod/Minh/lý do trống; L1001 T−3 phút: Bảo/đổi AI Search/Search/lý do trống. Đây là tập giả lập độc lập, không vai trò sau các SC trước. | M2 | FR-M10-15.01, FR-M10-15.04 |
| M2 | SYSTEM | Hệ thống kiểm ADMIN, lập tập theo tiêu chí (trống không thu hẹp), sắp mới nhất trước và trả năm trường người làm/thao tác/đối tượng/lý do tùy chọn/thời điểm giờ Việt Nam. Bao gồm mọi người làm được ghi, không chỉ chính Bảo; chỉ đọc, không ghi thêm log vì xem/lọc. | L1003,L1002,L1001; T−1/−2/−3 phút theo UTC+7; mục không sửa/xóa, giữ vĩnh viễn | END:SUCCESS | FR-M10-15.01, FR-M10-15.02, FR-M10-15.04, FR-M10-15.05, FR-M10-14.04, FR-M10-14.08, FR-M10-14.09, BR-M10-02, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |


#### 6. Các ngoại lệ

E thay đúng bước at, không thực hiện sau khi bước ấy đã xong. Guard/dữ liệu nhánh thay snapshot của lần chạy; không cộng các trạng thái loại trừ. Đổi actor định danh/dấu gốc hoặc target khác từ đầu có đường đầy đủ từ M1. V thay toàn bộ đường theo actor; không đổi người giữa các lượt. Mỗi nhánh đi đến kết quả hoặc điểm nhập lại thực sự; phần trạng thái/đường lỗi chưa chốt được ghi GAP, không tự đặt retry/rollback/hủy/đồng bộ.

<!-- sc:exceptions SC-M10-015 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Bảo lọc đồng thời người làm Bảo và thao tác đổi AI Search | E1.1 | FR-M10-15.05, FR-M10-15.01, FR-M10-15.02, FR-M10-15.04, FR-M10-14.08, FR-M10-14.09, BR-M10-23 |
| E2 | user-choice | M1 | Bảo lọc đồng thời người làm Hệ thống và thao tác thu hồi Mod do ban | E2.1 | FR-M10-15.05, FR-M10-15.01, FR-M10-15.02, FR-M10-15.04, FR-M10-14.08, FR-M10-14.09, BR-M10-23 |
| E3 | user-choice | M2 | Bảo đổi chỉ tiêu chí người làm sau khi xem tập chung | E3.1 | FR-M10-15.01, FR-M10-15.02, FR-M10-15.04, BR-M10-23, FR-M10-15.05, FR-M10-14.08 |
| E4 | user-choice | M2 | Bảo đổi chỉ tiêu chí loại thao tác sau khi xem tập chung | E4.1 | FR-M10-15.01, FR-M10-15.02, FR-M10-15.04, BR-M10-23, FR-M10-15.05, FR-M10-14.08 |
| E5 | system | M2 | Không có mục khớp tiêu chí | E5.1 | FR-M10-15.01, FR-M10-15.02, FR-M10-15.04, FR-M10-15.05, BR-M10-23, BR-M10-24 |
| E6 | system | M1 | Bất kỳ Admin nào yêu cầu sửa một mục nhật ký | E6.1 | FR-M10-15.03, FR-M10-14.04, BR-M10-22 |
| E7 | system | M1 | Bất kỳ Admin nào yêu cầu xóa một mục nhật ký | E7.1 | FR-M10-15.03, FR-M10-14.04, BR-M10-22 |


<!-- sc:branch SC-M10-015 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-007 | Bảo mở/lọc nhật ký theo người làm và loại thao tác. | actorFilter=Bảo; operationFilter=đổi AI Search; dữ liệu AUDIT | E1.2 | FR-M10-15.05 |
| E1.2 | SYSTEM | Hệ thống kiểm ADMIN, áp giao của hai tiêu chí rồi sắp mới nhất trước; trả đầy đủ năm trường theo giờ Việt Nam, không ghi log việc xem/lọc. | Chỉ L1001 khớp cả hai; lý do có thể trống | END:SUCCESS | FR-M10-15.01, FR-M10-15.02, FR-M10-15.04, FR-M10-15.05, FR-M10-14.08, FR-M10-14.09, BR-M10-23 |


<!-- sc:branch SC-M10-015 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-007 | Bảo mở/lọc nhật ký theo người làm và loại thao tác. | actorFilter=Hệ thống; operationFilter=thu hồi Mod do ban; dữ liệu AUDIT | E2.2 | FR-M10-15.05 |
| E2.2 | SYSTEM | Hệ thống kiểm ADMIN, áp giao của hai tiêu chí rồi sắp mới nhất trước; trả đầy đủ năm trường theo giờ Việt Nam, không ghi log việc xem/lọc. | Chỉ L1003 khớp cả hai; lý do có thể trống | END:SUCCESS | FR-M10-15.01, FR-M10-15.02, FR-M10-15.04, FR-M10-15.05, FR-M10-14.08, FR-M10-14.09, BR-M10-23 |


<!-- sc:branch SC-M10-015 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống trả tập Admin chung đúng quyền, mới nhất trước và chỉ đọc. | L1003 T−1 phút: Hệ thống/thu hồi Mod do ban/Tuấn/lý do Mất quyền Mod do ban B1003; L1002 T−2 phút: Minh/chấp nhận đề xuất Mod/Minh/lý do trống; L1001 T−3 phút: Bảo/đổi AI Search/Search/lý do trống. Đây là tập giả lập độc lập, không vai trò sau các SC trước. | E3.2 | FR-M10-15.01, FR-M10-15.02, FR-M10-15.04, BR-M10-23 |
| E3.2 | ACT-007 | Bảo đặt tiêu chí người làm. | người làm=Bảo; tiêu chí còn lại không thu hẹp | E3.3 | FR-M10-15.05 |
| E3.3 | SYSTEM | Hệ thống áp đúng tiêu chí được đưa vào, không tự thêm bộ lọc chỉ dòng của chính Bảo; trả tập khớp với năm trường/giờ Việt Nam, không tạo log mới. | Kết quả L1001 | END:SUCCESS | FR-M10-15.01, FR-M10-15.04, FR-M10-15.05, FR-M10-14.08, BR-M10-23 |


<!-- sc:branch SC-M10-015 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống trả tập Admin chung đúng quyền, mới nhất trước và chỉ đọc. | L1003 T−1 phút: Hệ thống/thu hồi Mod do ban/Tuấn/lý do Mất quyền Mod do ban B1003; L1002 T−2 phút: Minh/chấp nhận đề xuất Mod/Minh/lý do trống; L1001 T−3 phút: Bảo/đổi AI Search/Search/lý do trống. Đây là tập giả lập độc lập, không vai trò sau các SC trước. | E4.2 | FR-M10-15.01, FR-M10-15.02, FR-M10-15.04, BR-M10-23 |
| E4.2 | ACT-007 | Bảo đặt tiêu chí loại thao tác. | loại thao tác=chấp nhận đề xuất Mod; tiêu chí còn lại không thu hẹp | E4.3 | FR-M10-15.05 |
| E4.3 | SYSTEM | Hệ thống áp đúng tiêu chí được đưa vào, không tự thêm bộ lọc chỉ dòng của chính Bảo; trả tập khớp với năm trường/giờ Việt Nam, không tạo log mới. | Kết quả L1002 (người làm Minh) | END:SUCCESS | FR-M10-15.01, FR-M10-15.04, FR-M10-15.05, FR-M10-14.08, BR-M10-23 |


<!-- sc:branch SC-M10-015 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống kiểm ADMIN và trả danh sách rỗng theo tiêu chí; không lấy log AI hoặc log kiểm duyệt để lấp kết quả. | results=[]; không đổi/xóa mục đã có | END:SUCCESS | FR-M10-15.01, FR-M10-15.02, FR-M10-15.04, FR-M10-15.05, BR-M10-23, BR-M10-24 |


<!-- sc:branch SC-M10-015 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-007 | Bảo yêu cầu sửa L1001. | L1001 đã ghi; ADMIN không có ngoại lệ sửa/xóa | E6.2 | FR-M10-15.03 |
| E6.2 | SYSTEM | Hệ thống từ chối sửa mục nhật ký, giữ dữ liệu vĩnh viễn và chỉ ghi thêm theo nguồn; không có chức năng quản trị sửa lịch sử. | L1001 giữ nguyên; không phát thao tác sửa thành công | END:REJECTED | FR-M10-15.03, FR-M10-14.04, BR-M10-22 |


<!-- sc:branch SC-M10-015 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | ACT-007 | Bảo yêu cầu xóa L1001. | L1001 đã ghi; ADMIN không có ngoại lệ sửa/xóa | E7.2 | FR-M10-15.03 |
| E7.2 | SYSTEM | Hệ thống từ chối xóa mục nhật ký, giữ dữ liệu vĩnh viễn và chỉ ghi thêm theo nguồn; không có chức năng quản trị sửa lịch sử. | L1001 giữ nguyên; không phát thao tác xóa thành công | END:REJECTED | FR-M10-15.03, FR-M10-14.04, BR-M10-22 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-015 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Người yêu cầu chọn tra cứu nhật ký thao tác admin theo tiêu chí. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V1.2 | FR-M10-15.02, BR-M10-02 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-15.02, BR-M10-02 |


**V2 — thay toàn bộ M1 đến kết thúc:** User thường. Actor khởi tạo ACT-002; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-015 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-002 | Người yêu cầu chọn tra cứu nhật ký thao tác admin theo tiêu chí. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V2.2 | FR-M10-15.02, BR-M10-02 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-15.02, BR-M10-02 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mod hệ thống (kể cả Owner/Group Mod/Admin nhóm chat nhưng không ADMIN hệ thống). Actor khởi tạo ACT-008; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:role-path SC-M10-015 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-008 | Người yêu cầu chọn tra cứu nhật ký thao tác admin theo tiêu chí. | Không có quyền ADMIN hiện hành; biết ID/link không cấp quyền | V3.2 | FR-M10-15.02, BR-M10-02 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền và từ chối vào chức năng quản trị này; không trả dữ liệu ngoài quyền hoặc thực hiện thay đổi/log thành công từ yêu cầu bị từ chối. | Role không ADMIN hoặc chưa xác thực; dữ liệu được bảo toàn | END:REJECTED | FR-M10-15.02, BR-M10-02 |


<!-- sc:end SC-M10-015 -->

## 5. Hành vi nền và đối soát dữ liệu

| ID | Trigger/điều kiện | Hiệu ứng/ngoại lệ/giới hạn | sources |
|---|---|---|---|
| AUT-M10-001 | Khởi tạo hệ thống, không phải mỗi lần mở Panel/triển khai | Có một ADMIN gốc do đội phát triển tạo sẵn, không qua đăng ký, giữ thông tin đăng nhập theo nguồn, không đặt mật khẩu mẫu. Gốc là dấu trên ADMIN, không thu hồi/từ chức. AI Tổng và ba riêng Bật; bảo trì/pause Tắt; Group/Chat/Gamification Bật; không banner. Không reset cấu hình đang vận hành khi mở Panel. | FR-M10-07.04, FR-M10-09.10, FR-M10-10.04, FR-M10-11.04, FR-M10-12.09, FR-M10-13.10, BR-M10-10, BR-M10-26 |
| AUT-M10-002 | Đạt mốc gửi+7×24h khi đề xuất còn Chưa trả lời | Chuyển Hết hiệu lực, role giữ, M07 hiện Đã hết hạn/khóa lựa chọn. Bản đã trả lời không quay về Chưa trả lời; bị bản cùng loại thay là nguyên nhân khác, không tự dùng nhãn hết hạn. Bộ kiểm trả lời cũng dùng đúng mốc, đúng hạn đã từ chối; không thêm cron/audit tự động cho hết hạn. | FR-M10-02.10, FR-M10-07.10, FR-M10-03.08, BR-M10-07, BR-M10-27, FR-M07-02.31, FR-M07-02.32 |
| AUT-M10-003 | M08 ban một tài khoản đang MODERATOR | Đổi ngay MODERATOR→USER; account BANNED là trục trạng thái khác. Admin ban có mục ban riêng, mất Mod có log người làm Hệ thống. Hết/gỡ/lật ban vẫn USER, không tự phục hồi Mod/đề xuất mới. M10 không có BF người dùng tự chạy thu hồi do ban. | FR-M10-06.01, FR-M10-06.02, FR-M10-14.07, BR-M10-09, BR-M10-21, FR-M08-14.05, FR-M09-08.11 |
| AUT-M10-004 | Hoàn tất thao tác Admin đổi dữ liệu hoặc một thay đổi role nguồn nêu | Ghi người làm, thao tác, đối tượng, lý do tùy chọn lấy đúng lý do bắt buộc từ module gốc nếu có, thời điểm; append-only/vĩnh viễn. Admin gửi đề xuất/giáng Mod/thu hồi Admin/đổi từng công tắc/đặt-sửa-gỡ banner là người làm. Nhận đề xuất/từ chức ghi chính người đó, ban Mod đổi role ghi Hệ thống. Kiểm duyệt/khiếu nại/Topic/Tag của Admin ghi song song log M08 khi thuộc owner: cảnh cáo/bỏ AI/ban/gỡ ban/ẩn nội dung/ẩn-khóa-mở khóa nhóm/kết luận vụ/khiếu nại, thêm-gộp-xóa Topic, vô hiệu-kích hoạt Tag, đổi Topic/Tag trên bài người khác. Không log xem/nhận-nhả vụ hoặc khiếu nại/Admin đăng bài-bình luận-Star như User/AI quyết định. Không bắt lý do cho mọi M10 action, không log role không đổi khi người nhận Từ chối. | FR-M10-14.01, FR-M10-14.02, FR-M10-14.03, FR-M10-14.04, FR-M10-14.05, FR-M10-14.06, FR-M10-14.07, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| RULE-M10-001 | Vai trò và dấu gốc ở từng thao tác | Đúng một role USER<MODERATOR<ADMIN. Chỉ ADMIN vào Panel, đổi role/cấu hình/đọc log Admin; mọi Admin có quyền Mod theo owner nhưng Group Mod/Owner/Admin nhóm chat không là ADMIN hệ thống. Chỉ gốc gửi/thu hồi Admin, gốc không từ chức/thu hồi; có ít nhất một Admin. Cá nhân trả lời đề xuất/từ chức ngoài Panel, không cấp Panel cho User/Mod. Không tái tạo xử lý M05/M08/M09 trong M10. | BR-M10-01, BR-M10-02, BR-M10-03, BR-M10-10, BR-M10-11, BR-M10-25, FR-M10-07.03 |
| RULE-M10-002 | Gửi, nhận và thay đề xuất theo loại | Khi gửi: quyền theo loại, đích ACTIVE/xong bước 3, USER cho Mod, USER/MODERATOR cho Admin; không kiểm điểm/uy tín/thâm niên. Kiểm trước thay bản cùng loại, hết hiệu lực bản cũ trước lưu mới; bản từ chối/hết giữ lịch sử, lập bản mới+thông báo mới. Một hiệu lực mỗi người/mỗi loại; Mod và Admin không tự thay nhau. Nhận: đúng chủ, chưa trả lời/chưa bị thay, trước hạn; Chấp nhận kiểm ACTIVE/role hiện tại, không kiểm lại quyền người gửi cũ hoặc thêm xác minh đăng ký mới. Từ chối chỉ kiểm chủ/hiệu lực/một lần, không chạy guard riêng Chấp nhận; role giữ, không log đổi role không có. Sau Chấp nhận lỗi role/ACTIVE còn GAP001, không tự quyết trạng thái/khả năng thử lại. | FR-M10-02.01, FR-M10-02.02, FR-M10-02.03, FR-M10-02.04, FR-M10-02.05, FR-M10-02.06, FR-M10-02.07, FR-M10-02.08, FR-M10-02.09, FR-M10-02.10, FR-M10-03.01, FR-M10-03.02, FR-M10-03.03, FR-M10-03.04, FR-M10-03.06, FR-M10-03.07, FR-M10-03.08, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11, FR-M10-07.01, FR-M10-07.02, FR-M10-07.05, FR-M10-07.06, FR-M10-07.07, FR-M10-07.08, FR-M10-07.09, FR-M10-07.10, FR-M10-07.11, BR-M10-05, BR-M10-06, BR-M10-07, BR-M10-11, BR-M10-27 |
| RULE-M10-003 | Cấu hình và hiệu lực theo thời điểm | Đúng năm mục: AI, bảo trì, pause, cờ tính năng, banner; không công tắc email/AI tóm tắt riêng/cờ module khác. Lưu bền, áp sau đổi, không triển khai lại/reset công tắc khác; yêu cầu trước đổi dùng cấu hình trước theo nguồn, đang chạy/đồng thời/lỗi còn GAP004, không tự hủy/hồi tố. Chính sách cảnh cáo/ban/ngưỡng AI/trọng số/thời gian chờ AI/hạn đề xuất/nội dung-version trang chính sách không chỉnh UI. AI hiệu lực=Tổng AND riêng; tóm tắt chỉ Tổng. Riêng khi Tổng Tắt vẫn lưu, bật Tổng lại dùng đúng riêng. Search embedding bài/truy vấn, Moderation quét bài/comment/tự cảnh cáo, Topic suggestion gợi ý; tắt chủ đích dùng dự phòng, khác lỗi AI. Tổng+Search bật lại M13 tạo bù theo nội dung hiện tại khi AI trả lời được, không tạo bù tóm tắt. | FR-M10-09.01, FR-M10-09.02, FR-M10-09.03, FR-M10-09.04, FR-M10-09.05, FR-M10-09.06, FR-M10-09.07, FR-M10-09.08, FR-M10-09.09, FR-M10-09.10, FR-M10-10.01, FR-M10-10.02, FR-M10-10.03, FR-M10-10.04, FR-M10-11.01, FR-M10-11.02, FR-M10-11.03, FR-M10-11.04, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, BR-M10-17, BR-M10-18, BR-M10-26, FR-M13-03.08, FR-M13-03.10, FR-M13-06.11, BR-M13-07 |
| RULE-M10-004 | Cờ Group, Chat, Gamification theo owner | Cờ tắt từ chối người không ADMIN đúng câu Hệ thống đang bận, vui lòng thử lại sau; lối vào còn, dữ liệu giữ, tác vụ nền/kiểm duyệt chạy, Admin dùng như bật nhưng vẫn theo quyền owner. Group còn nhóm/bài nhóm tại danh sách/Trending/Group-Following feed/hồ sơ/tìm/bookmark/thông báo; mở nhóm/bài/tương tác bị chặn. Gamification chặn upvote/rút upvote/BXH, nút còn; vẫn cộng/trừ/hoàn điểm, huy hiệu, bảng toàn thời gian/chốt tuần-tháng/danh hiệu/thông báo và hiện số upvote/điểm/huy hiệu/danh hiệu/nhãn tài khoản khóa. Chat chặn mở hộp thư/cuộc, bắt đầu 1-1/tạo nhóm/gửi-thu hồi/thêm-xóa thành viên/duyệt/đổi tên/chuyển quyền/rời/bật-tắt duyệt/lấy link-xin gia nhập; vẫn biểu tượng-unread/nút nhắn tin, tự tắt duyệt do Admin nhóm không thể khôi phục và hạn thu hồi 5 phút chạy. Bật lại không tính bù thao tác bị chặn; không nhầm tạo bù Search AI với cờ. M14 feed còn truy cập, M15 không cờ. Chi tiết nghiệp vụ không triển khai thành SC M10. | FR-M10-12.01, FR-M10-12.02, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.06, FR-M10-12.07, FR-M10-12.08, FR-M10-12.09, BR-M10-19, BR-M10-28, FR-M11-17.01, FR-M11-17.07, FR-M11-17.08, FR-M12-08.08, FR-M12-08.09, FR-M12-08.10, FR-M16-15.04, FR-M16-15.06, FR-M16-15.07, FR-M16-15.08, FR-M14-01.07 |
| RULE-M10-005 | Banner và dấu đóng | Một banner plain text, 1–200 ký tự sau trim. Gỡ ngừng toàn trang; người xem đóng chỉ riêng mình, Guest theo browser đã đóng. Sửa nội dung/đặt mới thay bản hiện tại và hiện lại với mọi người kể cả người đã đóng. Không tự chọn lưu cookie/localStorage/server, thời hạn/đồng bộ người đăng nhập (GAP002), đơn vị Unicode hoặc Sửa nhưng nội dung không đổi (GAP003). Không nhiều banner/hẹn giờ, không diễn giải HTML/Markdown; snapshot ký tự biên dùng ASCII. | FR-M10-13.01, FR-M10-13.02, FR-M10-13.03, FR-M10-13.04, FR-M10-13.05, FR-M10-13.06, FR-M10-13.07, FR-M10-13.08, FR-M10-13.09, FR-M10-13.10, BR-M10-20, BR-M10-26 |
| RULE-M10-006 | Đọc nhật ký và tìm người | Log Admin mọi người làm, mới nhất trước, lọc theo người làm/loại thao tác (giao khi đưa cả hai), đủ năm trường, UTC+7; chỉ đọc/vĩnh viễn, không ai sửa/xóa, không log xem. Log AI M13 và kiểm duyệt M08 khác, không cấp Mod quyền log Admin. Không tự đặt nhãn người làm DELETED của M08 sang log Admin. Tìm quản trị chỉ tái dùng khớp username/display_name M06: substring/không phân biệt hoa-dấu/fuzzy nhẹ, giống hơn trước; lọc role và hiện trạng thái/nhãn gốc. Không bê giới hạn 3/debounce/chỉ ACTIVE/xong bước 3 từ tìm công khai; phạm vi đầy đủ trạng thái tài khoản trả về còn GAP005. Xem thao tác Mod mở M08 lọc đúng người, không KPI riêng. | FR-M10-01.01, FR-M10-01.02, FR-M10-01.03, FR-M10-01.04, FR-M10-01.05, FR-M10-01.06, FR-M10-15.01, FR-M10-15.02, FR-M10-15.03, FR-M10-15.04, FR-M10-15.05, FR-M10-14.04, FR-M10-14.05, FR-M10-14.08, FR-M10-14.09, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24, BR-M10-29, BR-M10-30, BR-M06-09, FR-M08-17.01, FR-M08-17.06 |


| Dữ liệu/biên giả lập | Kết quả đúng nguồn |
|---|---|
| Gửi đề xuất mới tại T=10/11 10:00 | Hạn 17/11 10:00; trước một giây còn hạn, tại đúng mốc không trả lời; không dùng ngày lịch |
| Bản Mod P0991 còn hiệu lực; gửi P1001 Mod mới khi nhận vẫn hợp lệ | Kiểm trước, P0991 Hết hiệu lực trước lưu P1001; N mới, N cũ khóa; không thay bản Admin độc lập |
| Người nhận 0 điểm, vừa hoàn tất bước 3, ACTIVE và role hợp lệ | Được gửi đề xuất, không thêm uy tín/thâm niên. Không ACTIVE/chưa xong bước 3 bị từ chối trước thay bản cũ |
| Mod nhận Admin nhưng đã bị giáng USER; hoặc người gửi Mod cũ đã từ chức | USER vẫn nhận Admin được nếu ACTIVE/hiệu lực; không kiểm lại quyền người gửi cũ khi chấp nhận; gốc không thể tự từ chức |
| Lan nhận Admin qua loại khác, R1011 Mod cũ vẫn hiệu lực và chọn Từ chối trực tiếp | Chỉ kiểm chủ/hiệu lực/một lần, giữ ADMIN, Đã từ chối; không chạy guard nhận Mod hoặc ghi role thay đổi không có |
| Bảo tự từ chức hoặc An thu hồi Bảo, Bảo từng Mod trước Admin | Về USER, không quay về MODERATOR; An gốc không bị thu hồi/từ chức, vẫn có ít nhất một Admin |
| Tổng=false, Search riêng true→false; rồi Tổng=true | Lưu Search=false dù đang không hiệu lực; sau bật Tổng, Search vẫn off, riêng khác dùng giá trị đã lưu |
| Tắt Tổng khi Search=true, Moderation=false, Topic suggestion=true; bật lại | Tổng off mọi AI off, không reset riêng; bật lại Search/Topic on, Moderation off, tóm tắt theo Tổng |
| Một tìm kiếm trước đổi Search 09:59:55, đổi 10:00, tìm sau 10:00:05 | Thao tác trước theo cấu hình trước, sau dùng cấu hình mới; không tự hủy/hồi tố yêu cầu đang chạy |
| Bảo trì bật, User đã có phiên; pause bật, người đã qua bước 1 | Phiên User không dùng được khi bảo trì, Admin vẫn dùng; pause vẫn cho tiếp bước 2/3 và liên kết Google tài khoản có sẵn, khác bảo trì |
| Group/Chat/Gamification tắt rồi bật lại | Lối vào và dữ liệu/việc tự làm giữ, người không Admin bị chặn theo owner; Admin vẫn theo quyền owner; không bù thao tác bị chặn, khác tạo bù embedding Search |
| Banner trống, chỉ spaces, 1 ASCII, 200 ASCII, 201 ASCII | Từ chối/từ chối/nhận/nhận/từ chối sau trim; lỗi sửa nội dung rồi gửi đến công bố; không quyết grapheme/UTF-16 |
| Banner chứa chuỗi **Thong bao** (13 ký tự ASCII) | Hiện nguyên ký tự dạng văn bản thuần, không diễn giải Markdown; bản mới/sửa nội dung hiện lại với người đã đóng |
| Guest C1 đóng B100, C2 chưa đóng; Bảo sửa thành bản mới | C1 không B100, C2 vẫn có; bản đổi nội dung hiện lại cho cả hai. Người đăng nhập đồng bộ/qua phiên còn GAP002 |
| Nhật ký thời điểm 01/11 17:30 UTC và 17:29 UTC | Hiện 02/11 00:30+07 trước 00:29+07; lý do trống hợp lệ cho thao tác M10 không bắt buộc |
| Admin ban Mod, người nhận chấp nhận/từ chức, người xem mở log | Ban có dòng Admin và mất Mod có dòng Hệ thống; chấp nhận/từ chức ghi chính người đó; xem không có dòng mới |


Các bảng quy tắc/đối soát giữ hành vi theo sự kiện, không biến SYSTEM/clock thành actor hoặc dựng scenario sáu phần phụ. Không chọn retry/outbox/rollback, nơi lưu dấu đóng, đơn vị Unicode hoặc tập account DELETED không có nguồn.

## 6. Truy vết và ma trận quyết định

| Mã hiệu lực | SC/bước/nhánh hoặc AUT/RULE | Mức đối soát |
|---|---|---|
| FR-M10-01 | SC-M10-001/M1; SC-M10-001/M2; SC-M10-001/E1.1; SC-M10-001/E2.1; SC-M10-001/E2.2; SC-M10-001/E4.1; SC-M10-001/E4.2; SC-M10-001/E5.1; RULE-M10-006; SC-M10-001/E5.2; SC-M10-001/V1.1; SC-M10-001/V1.2; SC-M10-001/V2.1; SC-M10-001/V2.2; SC-M10-001/V3.1; SC-M10-001/V3.2; SC-M10-001/M4; SC-M10-001/M3; SC-M10-001/E2.3; SC-M10-001/E2.4; SC-M10-001/E4.3; SC-M10-001/E4.4; SC-M10-001/E5.3; SC-M10-001/E5.4; SC-M10-001/E3.1; SC-M10-001/E3.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-02 | SC-M10-001/E4.4; SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-002/E5.1; SC-M10-002/E6.1; SC-M10-002/E7.1; SC-M10-002/E8.1; RULE-M10-002; SC-M10-002/M1; SC-M10-002/V1.1; SC-M10-002/V1.2; SC-M10-002/V2.1; SC-M10-002/V2.2; SC-M10-002/V3.1; SC-M10-002/V3.2; SC-M10-002/E9.1; SC-M10-004/E8.1; SC-M10-004/E12.1; SC-M10-004/E7.1; SC-M10-004/E11.1; AUT-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-03 | SC-M10-004/M2; SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/E5.1; SC-M10-004/E6.1; SC-M10-004/E9.1; SC-M10-004/E10.1; SC-M10-004/V2.4; SC-M10-004/V3.4; SC-M10-004/V4.2; RULE-M10-002; SC-M10-004/E2.2; SC-M10-004/E3.2; SC-M10-004/E13.1; SC-M10-004/V1.1; SC-M10-004/V1.2; SC-M10-004/V2.2; SC-M10-004/V3.2; SC-M10-004/E7.1; SC-M10-004/E8.1; SC-M10-004/E11.1; SC-M10-004/E12.1; AUT-M10-002; SC-M10-004/M3; SC-M10-004/V5.1; SC-M10-004/E1.1; SC-M10-004/V2.3; SC-M10-004/V3.3; SC-M10-004/V4.1; SC-M10-004/E2.3; SC-M10-004/E3.1; SC-M10-004/E3.3; SC-M10-004/E14.1; SC-M10-004/V5.2; SC-M10-004/E15.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-04 | SC-M10-005/M1; SC-M10-005/M2; SC-M10-005/V1.1; SC-M10-005/V1.2; SC-M10-005/V2.1; SC-M10-005/V2.2; SC-M10-005/V3.1; SC-M10-005/V3.2; SC-M10-005/E1.1; SC-M10-005/E2.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-05 | SC-M10-005/M2; SC-M10-007/M4; SC-M10-007/V1.4; SC-M10-007/M1; SC-M10-007/M2; SC-M10-007/M3; SC-M10-007/E2.1; SC-M10-007/V3.1; SC-M10-007/V3.2; SC-M10-007/V4.1; SC-M10-007/V4.2; SC-M10-007/E1.1; SC-M10-007/E1.2; SC-M10-007/V1.2; SC-M10-007/V5.2; SC-M10-007/V5.3; SC-M10-007/V5.4; SC-M10-007/V2.1; SC-M10-007/V2.2; SC-M10-007/V1.1; SC-M10-007/V1.3; SC-M10-007/V5.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-06 | AUT-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-07 | SC-M10-001/E4.4; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-003/E11.1; SC-M10-003/E11.2; RULE-M10-002; SC-M10-003/M1; SC-M10-003/E10.1; SC-M10-003/V1.1; SC-M10-003/V1.2; SC-M10-003/V2.1; SC-M10-003/V2.2; SC-M10-003/V3.1; SC-M10-003/V3.2; SC-M10-003/E9.1; SC-M10-004/E2.1; SC-M10-004/V2.1; SC-M10-004/V3.1; SC-M10-003/E5.1; SC-M10-003/E6.1; SC-M10-003/E7.1; SC-M10-003/E8.1; AUT-M10-002; AUT-M10-001; RULE-M10-001 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-08 | SC-M10-001/E2.4; SC-M10-006/M2; SC-M10-006/E1.1; SC-M10-006/E2.1; SC-M10-006/M1; SC-M10-001/E5.4; SC-M10-006/E4.1; SC-M10-006/E4.2; SC-M10-006/E3.1; SC-M10-006/E3.2; SC-M10-006/V1.1; SC-M10-006/V1.2; SC-M10-006/V2.1; SC-M10-006/V2.2; SC-M10-006/V3.1; SC-M10-006/V3.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-09 | SC-M10-008/M1; SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; RULE-M10-003; SC-M10-008/E2.1; SC-M10-008/E4.1; SC-M10-008/E6.1; SC-M10-008/E7.3; SC-M10-008/E8.3; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; SC-M10-008/E7.1; SC-M10-008/E1.1; SC-M10-008/E3.1; SC-M10-008/E5.1; SC-M10-008/E8.1; SC-M10-008/V1.1; SC-M10-008/V1.2; SC-M10-008/V2.1; SC-M10-008/V2.2; SC-M10-008/V3.1; SC-M10-008/V3.2; AUT-M10-001 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-10 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M1; SC-M10-009/M2; SC-M10-009/E1.1; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-003; SC-M10-009/V1.1; SC-M10-009/V1.2; SC-M10-009/V2.1; SC-M10-009/V2.2; SC-M10-009/V3.1; SC-M10-009/V3.2; AUT-M10-001 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-11 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M1; SC-M10-010/M2; SC-M10-010/E1.1; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-003; SC-M10-010/V1.1; SC-M10-010/V1.2; SC-M10-010/V2.1; SC-M10-010/V2.2; SC-M10-010/V3.1; SC-M10-010/V3.2; AUT-M10-001 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-12 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M1; SC-M10-011/M2; SC-M10-011/E1.1; SC-M10-011/E1.2; SC-M10-011/E2.1; SC-M10-011/E2.2; SC-M10-011/E3.1; SC-M10-011/E3.2; SC-M10-011/E4.1; SC-M10-011/E4.2; SC-M10-011/E5.1; SC-M10-011/E5.2; RULE-M10-004; SC-M10-011/V1.1; SC-M10-011/V1.2; SC-M10-011/V2.1; SC-M10-011/V2.2; SC-M10-011/V3.1; SC-M10-011/V3.2; AUT-M10-001 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-13 | SC-M10-012/M1; SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.2; SC-M10-012/E5.3; SC-M10-012/E6.2; SC-M10-012/E6.3; SC-M10-012/E7.2; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-014/M1; SC-M10-014/M2; SC-M10-014/E1.1; SC-M10-014/E4.1; SC-M10-014/V1.1; SC-M10-014/V1.2; SC-M10-014/V2.1; SC-M10-014/V2.2; SC-M10-014/V3.1; SC-M10-014/V3.2; RULE-M10-005; SC-M10-012/E3.1; SC-M10-012/E4.1; SC-M10-012/E5.1; SC-M10-012/E6.1; SC-M10-012/E7.1; SC-M10-012/E8.1; SC-M10-012/V1.1; SC-M10-012/V1.2; SC-M10-012/V2.1; SC-M10-012/V2.2; SC-M10-012/V3.1; SC-M10-012/V3.2; SC-M10-013/M2; SC-M10-013/V1.1; SC-M10-013/V1.2; SC-M10-013/V2.1; SC-M10-013/V2.2; SC-M10-013/V3.1; SC-M10-013/V3.2; SC-M10-012/E1.1; SC-M10-014/M4; SC-M10-014/E5.3; SC-M10-014/V1.4; SC-M10-014/V2.4; SC-M10-014/V3.4; SC-M10-012/E2.1; SC-M10-013/M1; SC-M10-014/E2.1; SC-M10-014/E3.1; SC-M10-014/M3; SC-M10-014/E5.1; SC-M10-014/E5.2; SC-M10-014/V1.3; SC-M10-014/V2.3; SC-M10-014/V3.3; AUT-M10-001 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-14 | SC-M10-001/M4; SC-M10-001/E2.4; SC-M10-001/E4.4; SC-M10-001/E5.4; SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/V2.4; SC-M10-004/V3.4; SC-M10-004/V4.2; SC-M10-005/M2; SC-M10-006/M2; SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-013/M2; SC-M10-014/M2; SC-M10-014/M4; SC-M10-014/E1.1; SC-M10-014/V1.2; SC-M10-014/V1.4; SC-M10-014/V2.2; SC-M10-014/V2.4; SC-M10-014/V3.2; SC-M10-014/V3.4; SC-M10-015/M2; SC-M10-015/E1.2; SC-M10-015/E2.2; SC-M10-015/E3.3; SC-M10-015/E4.3; AUT-M10-004; RULE-M10-006; SC-M10-015/E6.2; SC-M10-015/E7.2; SC-M10-004/E4.1; SC-M10-007/M4; SC-M10-007/V1.4; AUT-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-15 | SC-M10-015/M1; SC-M10-015/M2; SC-M10-015/E1.2; SC-M10-015/E2.2; SC-M10-015/E3.1; SC-M10-015/E3.3; SC-M10-015/E4.1; SC-M10-015/E4.3; SC-M10-015/E5.1; RULE-M10-006; SC-M10-015/V1.1; SC-M10-015/V1.2; SC-M10-015/V2.1; SC-M10-015/V2.2; SC-M10-015/V3.1; SC-M10-015/V3.2; SC-M10-015/E1.1; SC-M10-015/E2.1; SC-M10-015/E3.2; SC-M10-015/E4.2; SC-M10-015/E6.1; SC-M10-015/E6.2; SC-M10-015/E7.1; SC-M10-015/E7.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-01.01 | SC-M10-001/M3; SC-M10-001/M4; SC-M10-001/E2.3; SC-M10-001/E2.4; SC-M10-001/E4.3; SC-M10-001/E4.4; SC-M10-001/E5.3; SC-M10-001/E5.4; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-01.02 | SC-M10-001/M2; SC-M10-001/E1.1; SC-M10-001/E2.2; SC-M10-001/E4.2; SC-M10-001/E5.2; SC-M10-001/V1.1; SC-M10-001/V1.2; SC-M10-001/V2.1; SC-M10-001/V2.2; SC-M10-001/V3.1; SC-M10-001/V3.2; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-01.03 | SC-M10-001/M1; SC-M10-001/M2; SC-M10-001/E1.1; SC-M10-001/E2.1; SC-M10-001/E2.2; SC-M10-001/E4.1; SC-M10-001/E4.2; SC-M10-001/E5.1; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt; GAP005 tập trạng thái account |
| FR-M10-01.04 | SC-M10-001/M1; SC-M10-001/M2; SC-M10-001/E1.1; SC-M10-001/E2.1; SC-M10-001/E2.2; SC-M10-001/E4.1; SC-M10-001/E4.2; SC-M10-001/E5.1; SC-M10-001/E5.2; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt; GAP005 tập trạng thái account |
| FR-M10-01.05 | SC-M10-001/M2; SC-M10-001/M4; SC-M10-001/E1.1; SC-M10-001/E2.2; SC-M10-001/E4.2; SC-M10-001/E5.2; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt; GAP005 tập trạng thái account |
| FR-M10-01.06 | SC-M10-001/M4; SC-M10-001/E3.1; SC-M10-001/E3.2; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-02.01 | SC-M10-002/M1; SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-02.02 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-02.03 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-02.04 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-02.05 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-02.06 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-002/V1.1; SC-M10-002/V1.2; SC-M10-002/V2.1; SC-M10-002/V2.2; SC-M10-002/V3.1; SC-M10-002/V3.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-02.07 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-002/E9.1; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-02.08 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-004/E8.1; SC-M10-004/E12.1; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt; GAP004 hợp đồng lỗi/đồng thời |
| FR-M10-02.09 | SC-M10-001/E4.4; SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-002/E5.1; SC-M10-002/E6.1; SC-M10-002/E7.1; SC-M10-002/E8.1; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-02.10 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-004/E7.1; SC-M10-004/E11.1; AUT-M10-002; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-03.01 | SC-M10-004/M3; SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/V2.4; SC-M10-004/V3.4; SC-M10-004/V4.2; SC-M10-004/V5.1; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-03.02 | SC-M10-004/M3; SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/V2.4; SC-M10-004/V3.4; SC-M10-004/V4.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-03.03 | SC-M10-004/M4; SC-M10-004/E1.1; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/V2.3; SC-M10-004/V2.4; SC-M10-004/V3.3; SC-M10-004/V3.4; SC-M10-004/V4.1; SC-M10-004/V4.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-03.04 | SC-M10-004/M2; SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/E5.1; SC-M10-004/E6.1; SC-M10-004/E9.1; SC-M10-004/E10.1; SC-M10-004/V2.4; SC-M10-004/V3.4; SC-M10-004/V4.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-03.06 | SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/E5.1; SC-M10-004/E6.1; SC-M10-004/E9.1; SC-M10-004/E10.1; SC-M10-004/V2.4; SC-M10-004/V3.4; SC-M10-004/V4.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-03.07 | SC-M10-004/M2; SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.2; SC-M10-004/E2.4; SC-M10-004/E3.2; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/E13.1; SC-M10-004/V1.1; SC-M10-004/V1.2; SC-M10-004/V2.2; SC-M10-004/V2.4; SC-M10-004/V3.2; SC-M10-004/V3.4; SC-M10-004/V4.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-03.08 | SC-M10-004/M2; SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.2; SC-M10-004/E2.4; SC-M10-004/E3.2; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/E7.1; SC-M10-004/E8.1; SC-M10-004/E11.1; SC-M10-004/E12.1; SC-M10-004/V2.2; SC-M10-004/V2.4; SC-M10-004/V3.2; SC-M10-004/V3.4; SC-M10-004/V4.2; AUT-M10-002; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-03.09 | SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.3; SC-M10-004/E2.4; SC-M10-004/E3.1; SC-M10-004/E3.3; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/V2.3; SC-M10-004/V2.4; SC-M10-004/V3.3; SC-M10-004/V3.4; SC-M10-004/V4.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-03.10 | SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.1; SC-M10-004/E3.2; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/E14.1; SC-M10-004/V2.4; SC-M10-004/V3.4; SC-M10-004/V4.2; SC-M10-004/V5.1; SC-M10-004/V5.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt; GAP001 trạng thái sau Chấp nhận lỗi |
| FR-M10-03.11 | SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/E15.1; SC-M10-004/V2.4; SC-M10-004/V3.4; SC-M10-004/V4.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt; GAP001 trạng thái sau Chấp nhận lỗi |
| FR-M10-04.01 | SC-M10-005/M1; SC-M10-005/M2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-04.02 | SC-M10-005/M2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-04.03 | SC-M10-005/M2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-04.04 | SC-M10-005/M2; SC-M10-005/V1.1; SC-M10-005/V1.2; SC-M10-005/V2.1; SC-M10-005/V2.2; SC-M10-005/V3.1; SC-M10-005/V3.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-04.05 | SC-M10-005/M2; SC-M10-005/E1.1; SC-M10-005/E2.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-05.01 | SC-M10-007/M1; SC-M10-007/M2; SC-M10-007/M3; SC-M10-007/M4; SC-M10-007/E2.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-05.02 | SC-M10-007/M2; SC-M10-007/E2.1; SC-M10-007/V3.1; SC-M10-007/V3.2; SC-M10-007/V4.1; SC-M10-007/V4.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-05.03 | SC-M10-007/M2; SC-M10-007/M3; SC-M10-007/M4; SC-M10-007/E1.1; SC-M10-007/E1.2; SC-M10-007/V1.2; SC-M10-007/V1.4; SC-M10-007/V5.2; SC-M10-007/V5.3; SC-M10-007/V5.4 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-05.04 | SC-M10-007/V1.1; SC-M10-007/V1.2; SC-M10-007/V1.3; SC-M10-007/V1.4; SC-M10-007/V5.1; SC-M10-007/V5.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-05.05 | SC-M10-007/M2; SC-M10-007/V1.2; SC-M10-007/V2.1; SC-M10-007/V2.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-05.06 | SC-M10-005/M2; SC-M10-007/M4; SC-M10-007/V1.4 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-06.01 | AUT-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-06.02 | AUT-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-07.01 | SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-003/V1.1; SC-M10-003/V1.2; SC-M10-003/V2.1; SC-M10-003/V2.2; SC-M10-003/V3.1; SC-M10-003/V3.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-07.02 | SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E9.1; SC-M10-003/E10.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-07.03 | RULE-M10-001 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-07.04 | AUT-M10-001 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-07.05 | SC-M10-003/M1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.1; SC-M10-003/E10.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-07.06 | SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-004/E2.1; SC-M10-004/V2.1; SC-M10-004/V3.1; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-07.07 | SC-M10-001/E4.4; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-003/E11.1; SC-M10-003/E11.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-07.08 | SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E5.1; SC-M10-003/E6.1; SC-M10-003/E7.1; SC-M10-003/E8.1; SC-M10-003/E10.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-07.09 | SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt; GAP004 hợp đồng lỗi/đồng thời |
| FR-M10-07.10 | SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; AUT-M10-002; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-07.11 | SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-08.01 | SC-M10-006/M2; SC-M10-006/V1.1; SC-M10-006/V1.2; SC-M10-006/V2.1; SC-M10-006/V2.2; SC-M10-006/V3.1; SC-M10-006/V3.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-08.02 | SC-M10-001/E2.4; SC-M10-006/M2; SC-M10-006/E1.1; SC-M10-006/E2.1 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-08.03 | SC-M10-001/E2.4; SC-M10-006/M1; SC-M10-006/M2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-08.04 | SC-M10-001/E2.4; SC-M10-001/E5.4; SC-M10-006/M2; SC-M10-006/E4.1; SC-M10-006/E4.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-08.05 | SC-M10-001/E2.4; SC-M10-001/E5.4; SC-M10-006/M2; SC-M10-006/E3.1; SC-M10-006/E3.2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-08.06 | SC-M10-006/M2 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-09.01 | SC-M10-008/M1; SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-09.02 | SC-M10-008/M1; SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.1; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.1; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.1; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.3; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.3; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt; GAP004 hợp đồng lỗi/đồng thời |
| FR-M10-09.03 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.1; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-09.04 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.3; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.3; SC-M10-008/E8.4; SC-M10-008/E9.1; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-09.05 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-09.06 | SC-M10-008/M2; SC-M10-008/E1.1; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.1; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.1; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.1; SC-M10-008/E8.2; SC-M10-008/E8.3; SC-M10-008/E8.4; SC-M10-008/E9.1; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-09.07 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-09.08 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-008/V1.1; SC-M10-008/V1.2; SC-M10-008/V2.1; SC-M10-008/V2.2; SC-M10-008/V3.1; SC-M10-008/V3.2; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-09.09 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-09.10 | AUT-M10-001; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-10.01 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M1; SC-M10-009/M2; SC-M10-009/E1.1; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-10.02 | SC-M10-009/M2; SC-M10-009/E1.2; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-10.03 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-009/V1.1; SC-M10-009/V1.2; SC-M10-009/V2.1; SC-M10-009/V2.2; SC-M10-009/V3.1; SC-M10-009/V3.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-10.04 | AUT-M10-001; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-11.01 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M1; SC-M10-010/M2; SC-M10-010/E1.1; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-11.02 | SC-M10-010/M2; SC-M10-010/E1.2; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-11.03 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-010/V1.1; SC-M10-010/V1.2; SC-M10-010/V2.1; SC-M10-010/V2.2; SC-M10-010/V3.1; SC-M10-010/V3.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-11.04 | AUT-M10-001; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-12.01 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M1; SC-M10-011/M2; SC-M10-011/E1.1; SC-M10-011/E1.2; SC-M10-011/E2.1; SC-M10-011/E2.2; SC-M10-011/E3.1; SC-M10-011/E3.2; SC-M10-011/E4.1; SC-M10-011/E4.2; SC-M10-011/E5.1; SC-M10-011/E5.2; RULE-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-12.02 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; SC-M10-011/V1.1; SC-M10-011/V1.2; SC-M10-011/V2.1; SC-M10-011/V2.2; SC-M10-011/V3.1; SC-M10-011/V3.2; RULE-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-12.03 | SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-12.04 | SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-12.05 | SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-12.06 | SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-12.07 | SC-M10-011/M2; SC-M10-011/E1.1; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.1; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.1; SC-M10-011/E5.2; RULE-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-12.08 | SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-12.09 | AUT-M10-001; RULE-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-13.01 | SC-M10-012/M1; SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.2; SC-M10-012/E5.3; SC-M10-012/E6.2; SC-M10-012/E6.3; SC-M10-012/E7.2; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-014/M1; SC-M10-014/M2; SC-M10-014/E1.1; SC-M10-014/E4.1; SC-M10-014/V1.1; SC-M10-014/V1.2; SC-M10-014/V2.1; SC-M10-014/V2.2; SC-M10-014/V3.1; SC-M10-014/V3.2; RULE-M10-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-13.02 | SC-M10-013/M1; SC-M10-013/M2; SC-M10-014/E2.1; SC-M10-014/E3.1; RULE-M10-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-13.03 | SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-012/V1.1; SC-M10-012/V1.2; SC-M10-012/V2.1; SC-M10-012/V2.2; SC-M10-012/V3.1; SC-M10-012/V3.2; SC-M10-013/M2; SC-M10-013/V1.1; SC-M10-013/V1.2; SC-M10-013/V2.1; SC-M10-013/V2.2; SC-M10-013/V3.1; SC-M10-013/V3.2; RULE-M10-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-13.04 | SC-M10-012/M2; SC-M10-012/E1.1; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.2; RULE-M10-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-13.05 | SC-M10-012/M1; SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.1; SC-M10-012/E3.2; SC-M10-012/E4.1; SC-M10-012/E4.2; SC-M10-012/E5.1; SC-M10-012/E5.2; SC-M10-012/E5.3; SC-M10-012/E6.1; SC-M10-012/E6.2; SC-M10-012/E6.3; SC-M10-012/E7.1; SC-M10-012/E7.2; SC-M10-012/E7.3; SC-M10-012/E8.2; RULE-M10-005 | Có vị trí đối soát; chưa phê duyệt; GAP003 Unicode/sửa không đổi nội dung |
| FR-M10-13.06 | SC-M10-012/M1; SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.1; SC-M10-012/E8.2; SC-M10-014/M2; SC-M10-014/E1.1; SC-M10-014/E4.1; SC-M10-014/V1.2; SC-M10-014/V2.2; SC-M10-014/V3.2; RULE-M10-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-13.07 | SC-M10-014/M2; SC-M10-014/M3; SC-M10-014/M4; SC-M10-014/E1.1; SC-M10-014/E2.1; SC-M10-014/E3.1; SC-M10-014/E5.1; SC-M10-014/E5.2; SC-M10-014/E5.3; SC-M10-014/V1.3; SC-M10-014/V1.4; SC-M10-014/V2.3; SC-M10-014/V2.4; SC-M10-014/V3.3; SC-M10-014/V3.4; RULE-M10-005 | Có vị trí đối soát; chưa phê duyệt; GAP002 phạm vi đóng người đăng nhập |
| FR-M10-13.08 | SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-014/M4; SC-M10-014/E4.1; SC-M10-014/E5.3; SC-M10-014/V1.4; SC-M10-014/V2.4; SC-M10-014/V3.4; RULE-M10-005 | Có vị trí đối soát; chưa phê duyệt; GAP003 Unicode/sửa không đổi nội dung |
| FR-M10-13.09 | SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.1; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.2; RULE-M10-005 | Có vị trí đối soát; chưa phê duyệt; GAP003 Unicode/sửa không đổi nội dung |
| FR-M10-13.10 | AUT-M10-001; RULE-M10-005 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-14.01 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-005/M2; SC-M10-006/M2; SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-013/M2; AUT-M10-004 | Có vị trí đối soát; chưa phê duyệt; GAP004 hợp đồng lỗi/đồng thời |
| FR-M10-14.02 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-005/M2; SC-M10-006/M2; SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-013/M2; AUT-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-14.03 | AUT-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-14.04 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-005/M2; SC-M10-006/M2; SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-013/M2; SC-M10-015/M2; SC-M10-015/E6.2; SC-M10-015/E7.2; AUT-M10-004; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-14.05 | AUT-M10-004; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-14.06 | SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/V2.4; SC-M10-004/V3.4; SC-M10-004/V4.2; SC-M10-007/M4; SC-M10-007/V1.4; AUT-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-14.07 | AUT-M10-003; AUT-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-14.08 | SC-M10-001/M4; SC-M10-001/E2.4; SC-M10-001/E4.4; SC-M10-001/E5.4; SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/V2.4; SC-M10-004/V3.4; SC-M10-004/V4.2; SC-M10-005/M2; SC-M10-006/M2; SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-013/M2; SC-M10-014/M2; SC-M10-014/M4; SC-M10-014/E1.1; SC-M10-014/V1.2; SC-M10-014/V1.4; SC-M10-014/V2.2; SC-M10-014/V2.4; SC-M10-014/V3.2; SC-M10-014/V3.4; SC-M10-015/M2; SC-M10-015/E1.2; SC-M10-015/E2.2; SC-M10-015/E3.3; SC-M10-015/E4.3; AUT-M10-004; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-14.09 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-005/M2; SC-M10-006/M2; SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-013/M2; SC-M10-015/M2; SC-M10-015/E1.2; SC-M10-015/E2.2; AUT-M10-004; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-15.01 | SC-M10-015/M1; SC-M10-015/M2; SC-M10-015/E1.2; SC-M10-015/E2.2; SC-M10-015/E3.1; SC-M10-015/E3.3; SC-M10-015/E4.1; SC-M10-015/E4.3; SC-M10-015/E5.1; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-15.02 | SC-M10-015/M2; SC-M10-015/E1.2; SC-M10-015/E2.2; SC-M10-015/E3.1; SC-M10-015/E4.1; SC-M10-015/E5.1; SC-M10-015/V1.1; SC-M10-015/V1.2; SC-M10-015/V2.1; SC-M10-015/V2.2; SC-M10-015/V3.1; SC-M10-015/V3.2; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-15.03 | SC-M10-015/E6.1; SC-M10-015/E6.2; SC-M10-015/E7.1; SC-M10-015/E7.2; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-15.04 | SC-M10-015/M1; SC-M10-015/M2; SC-M10-015/E1.2; SC-M10-015/E2.2; SC-M10-015/E3.1; SC-M10-015/E3.3; SC-M10-015/E4.1; SC-M10-015/E4.3; SC-M10-015/E5.1; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| FR-M10-15.05 | SC-M10-015/M2; SC-M10-015/E1.1; SC-M10-015/E1.2; SC-M10-015/E2.1; SC-M10-015/E2.2; SC-M10-015/E3.2; SC-M10-015/E3.3; SC-M10-015/E4.2; SC-M10-015/E4.3; SC-M10-015/E5.1; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-01 | SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/V2.4; SC-M10-004/V3.4; SC-M10-004/V4.2; RULE-M10-001 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-02 | SC-M10-001/M2; SC-M10-001/M4; SC-M10-001/V1.1; SC-M10-001/V1.2; SC-M10-001/V2.1; SC-M10-001/V2.2; SC-M10-001/V3.1; SC-M10-001/V3.2; SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-002/V1.1; SC-M10-002/V1.2; SC-M10-002/V2.1; SC-M10-002/V2.2; SC-M10-002/V3.1; SC-M10-002/V3.2; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-003/V1.1; SC-M10-003/V1.2; SC-M10-003/V2.1; SC-M10-003/V2.2; SC-M10-003/V3.1; SC-M10-003/V3.2; SC-M10-005/M2; SC-M10-005/V1.1; SC-M10-005/V1.2; SC-M10-005/V2.1; SC-M10-005/V2.2; SC-M10-005/V3.1; SC-M10-005/V3.2; SC-M10-006/V1.1; SC-M10-006/V1.2; SC-M10-006/V2.1; SC-M10-006/V2.2; SC-M10-006/V3.1; SC-M10-006/V3.2; SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-008/V1.1; SC-M10-008/V1.2; SC-M10-008/V2.1; SC-M10-008/V2.2; SC-M10-008/V3.1; SC-M10-008/V3.2; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-009/V1.1; SC-M10-009/V1.2; SC-M10-009/V2.1; SC-M10-009/V2.2; SC-M10-009/V3.1; SC-M10-009/V3.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-010/V1.1; SC-M10-010/V1.2; SC-M10-010/V2.1; SC-M10-010/V2.2; SC-M10-010/V3.1; SC-M10-010/V3.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; SC-M10-011/V1.1; SC-M10-011/V1.2; SC-M10-011/V2.1; SC-M10-011/V2.2; SC-M10-011/V3.1; SC-M10-011/V3.2; SC-M10-012/V1.1; SC-M10-012/V1.2; SC-M10-012/V2.1; SC-M10-012/V2.2; SC-M10-012/V3.1; SC-M10-012/V3.2; SC-M10-013/V1.1; SC-M10-013/V1.2; SC-M10-013/V2.1; SC-M10-013/V2.2; SC-M10-013/V3.1; SC-M10-013/V3.2; SC-M10-015/M2; SC-M10-015/V1.1; SC-M10-015/V1.2; SC-M10-015/V2.1; SC-M10-015/V2.2; SC-M10-015/V3.1; SC-M10-015/V3.2; RULE-M10-001 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-03 | RULE-M10-001 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-04 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-05 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-002/E5.1; SC-M10-002/E6.1; SC-M10-002/E7.1; SC-M10-002/E8.1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E5.1; SC-M10-003/E6.1; SC-M10-003/E7.1; SC-M10-003/E8.1; SC-M10-003/E10.2; SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/E15.1; SC-M10-004/V2.4; SC-M10-004/V3.4; SC-M10-004/V4.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt; GAP001 trạng thái sau Chấp nhận lỗi |
| BR-M10-06 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/V2.4; SC-M10-004/V3.4; SC-M10-004/V4.2; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-07 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-004/M2; SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/E5.1; SC-M10-004/E6.1; SC-M10-004/E7.1; SC-M10-004/E9.1; SC-M10-004/E10.1; SC-M10-004/E11.1; SC-M10-004/V2.2; SC-M10-004/V2.4; SC-M10-004/V3.2; SC-M10-004/V3.4; SC-M10-004/V4.2; AUT-M10-002; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-08 | SC-M10-005/M2 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-09 | AUT-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-10 | SC-M10-001/E2.4; SC-M10-001/E5.4; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-006/M2; SC-M10-006/E4.2; SC-M10-007/M2; SC-M10-007/V1.4; SC-M10-007/V2.2; AUT-M10-001; RULE-M10-001 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-11 | SC-M10-001/M4; SC-M10-001/E2.4; SC-M10-001/E4.4; SC-M10-001/E5.4; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-003/E11.2; SC-M10-006/M2; SC-M10-006/E3.2; RULE-M10-001; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-12 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-13 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt; GAP004 hợp đồng lỗi/đồng thời |
| BR-M10-14 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-15 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-16 | SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-17 | SC-M10-009/M2; SC-M10-009/E1.2; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-18 | SC-M10-010/M2; SC-M10-010/E1.2; RULE-M10-003 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-19 | SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-20 | SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.2; SC-M10-012/E5.3; SC-M10-012/E6.2; SC-M10-012/E6.3; SC-M10-012/E7.2; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-013/M2; SC-M10-014/M2; SC-M10-014/M4; SC-M10-014/E1.1; SC-M10-014/E2.1; SC-M10-014/E3.1; SC-M10-014/E4.1; SC-M10-014/E5.1; SC-M10-014/E5.3; SC-M10-014/V1.2; SC-M10-014/V1.4; SC-M10-014/V2.2; SC-M10-014/V2.4; SC-M10-014/V3.2; SC-M10-014/V3.4; RULE-M10-005 | Có vị trí đối soát; chưa phê duyệt; GAP002 phạm vi đóng người đăng nhập; GAP003 Unicode/sửa không đổi nội dung |
| BR-M10-21 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.4; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/V2.4; SC-M10-004/V3.4; SC-M10-004/V4.2; SC-M10-005/M2; SC-M10-006/M2; SC-M10-007/M4; SC-M10-007/E1.2; SC-M10-007/E2.1; SC-M10-007/V1.4; SC-M10-007/V5.4; SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-013/M2; SC-M10-015/M2; AUT-M10-003; AUT-M10-004; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-22 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-005/M2; SC-M10-006/M2; SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-013/M2; SC-M10-015/M2; SC-M10-015/E6.2; SC-M10-015/E7.2; AUT-M10-004; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-23 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-005/M2; SC-M10-006/M2; SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-013/M2; SC-M10-015/M2; SC-M10-015/E1.2; SC-M10-015/E2.2; SC-M10-015/E3.1; SC-M10-015/E3.3; SC-M10-015/E4.1; SC-M10-015/E4.3; SC-M10-015/E5.1; AUT-M10-004; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-24 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E10.2; SC-M10-005/M2; SC-M10-006/M2; SC-M10-008/M2; SC-M10-008/E1.2; SC-M10-008/E2.2; SC-M10-008/E3.2; SC-M10-008/E4.2; SC-M10-008/E5.2; SC-M10-008/E6.2; SC-M10-008/E7.2; SC-M10-008/E7.4; SC-M10-008/E8.2; SC-M10-008/E8.4; SC-M10-008/E9.1; SC-M10-009/M2; SC-M10-009/E1.2; SC-M10-010/M2; SC-M10-010/E1.2; SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; SC-M10-012/M2; SC-M10-012/E1.2; SC-M10-012/E2.2; SC-M10-012/E3.2; SC-M10-012/E4.2; SC-M10-012/E5.3; SC-M10-012/E6.3; SC-M10-012/E7.3; SC-M10-012/E8.2; SC-M10-013/M2; SC-M10-015/M2; SC-M10-015/E5.1; AUT-M10-004; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-25 | SC-M10-007/M2; SC-M10-007/M4; SC-M10-007/E1.2; SC-M10-007/E2.1; SC-M10-007/V1.2; SC-M10-007/V1.4; SC-M10-007/V5.2; SC-M10-007/V5.4; RULE-M10-001 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-26 | AUT-M10-001; RULE-M10-003; RULE-M10-005 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-27 | SC-M10-002/M2; SC-M10-002/E1.1; SC-M10-002/E2.1; SC-M10-002/E3.1; SC-M10-002/E4.1; SC-M10-002/E9.1; SC-M10-003/M2; SC-M10-003/E1.1; SC-M10-003/E2.1; SC-M10-003/E3.1; SC-M10-003/E4.1; SC-M10-003/E9.1; SC-M10-003/E10.2; SC-M10-004/M2; SC-M10-004/M4; SC-M10-004/E1.2; SC-M10-004/E2.2; SC-M10-004/E2.4; SC-M10-004/E3.1; SC-M10-004/E3.2; SC-M10-004/E3.4; SC-M10-004/E4.1; SC-M10-004/E8.1; SC-M10-004/E12.1; SC-M10-004/E14.1; SC-M10-004/V2.2; SC-M10-004/V2.3; SC-M10-004/V2.4; SC-M10-004/V3.2; SC-M10-004/V3.3; SC-M10-004/V3.4; SC-M10-004/V4.1; SC-M10-004/V4.2; SC-M10-004/V5.1; SC-M10-004/V5.2; AUT-M10-002; RULE-M10-002 | Có vị trí đối soát; chưa phê duyệt; GAP001 trạng thái sau Chấp nhận lỗi |
| BR-M10-28 | SC-M10-011/M2; SC-M10-011/E1.2; SC-M10-011/E2.2; SC-M10-011/E3.2; SC-M10-011/E4.2; SC-M10-011/E5.2; RULE-M10-004 | Có vị trí đối soát; chưa phê duyệt |
| BR-M10-29 | SC-M10-001/M1; SC-M10-001/M2; SC-M10-001/M4; SC-M10-001/E1.1; SC-M10-001/E2.1; SC-M10-001/E2.2; SC-M10-001/E4.1; SC-M10-001/E4.2; SC-M10-001/E5.1; SC-M10-001/E5.2; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt; GAP005 tập trạng thái account |
| BR-M10-30 | SC-M10-001/M4; SC-M10-001/E3.2; RULE-M10-006 | Có vị trí đối soát; chưa phê duyệt |


| Mã đã bỏ | Cách xử lý |
|---|---|
| FR-M10-03.05 | Loại khỏi 152 mã hiệu lực; không khôi phục đề xuất vô hạn, dùng FR-M10-03.08/BR-M10-07 hiện hành |


| UC owner | Guard/lựa chọn | SC/nhánh | Đích |
|---|---|---|---|
| UC-M10-001 | Không có tài khoản khớp tên và vai trò trong tập được tra cứu | SC-M10-001/E1 | END:SUCCESS |
| UC-M10-001 | An ADMIN gốc tìm Admin và chọn một người để xem khả năng thu hồi | SC-M10-001/E2 | END:SUCCESS |
| UC-M10-001 | Bảo chọn Xem thao tác của Mai thay vì thao tác đổi role | SC-M10-001/E3 | END:SUCCESS |
| UC-M10-001 | Bảo lọc USER, chọn Lan và nhận thao tác đề xuất Mod phù hợp | SC-M10-001/E4 | END:SUCCESS |
| UC-M10-001 | Bảo chỉ lọc ADMIN và xem nhãn gốc trong tập năm Admin giả lập | SC-M10-001/E5 | END:SUCCESS |
| UC-M10-003 | Có bản cùng loại cũ Chưa trả lời; người gửi/nhận vẫn đủ điều kiện | SC-M10-002/E1 | END:SUCCESS |
| UC-M10-003 | Có bản cùng loại cũ Đã từ chối; người gửi/nhận vẫn đủ điều kiện | SC-M10-002/E2 | END:SUCCESS |
| UC-M10-003 | Có bản cùng loại cũ Hết hiệu lực; người gửi/nhận vẫn đủ điều kiện | SC-M10-002/E3 | END:SUCCESS |
| UC-M10-003 | Đang có đề xuất loại còn lại cho cùng Lan; hai loại không thay nhau | SC-M10-002/E4 | END:SUCCESS |
| UC-M10-003 | Người nhận không ACTIVE: DEACTIVATED | SC-M10-002/E5 | END:REJECTED |
| UC-M10-003 | Người nhận không ACTIVE: BANNED | SC-M10-002/E6 | END:REJECTED |
| UC-M10-003 | Người nhận không ACTIVE: DELETED | SC-M10-002/E7 | END:REJECTED |
| UC-M10-003 | Người nhận chưa hoàn tất bước 3 | SC-M10-002/E8 | END:REJECTED |
| UC-M10-003 | Đích sai vai trò cho loại đề xuất | SC-M10-002/E9 | END:REJECTED |
| UC-M10-004 | Có bản cùng loại cũ Chưa trả lời; người gửi/nhận vẫn đủ điều kiện | SC-M10-003/E1 | END:SUCCESS |
| UC-M10-004 | Có bản cùng loại cũ Đã từ chối; người gửi/nhận vẫn đủ điều kiện | SC-M10-003/E2 | END:SUCCESS |
| UC-M10-004 | Có bản cùng loại cũ Hết hiệu lực; người gửi/nhận vẫn đủ điều kiện | SC-M10-003/E3 | END:SUCCESS |
| UC-M10-004 | Đang có đề xuất loại còn lại cho cùng Lan; hai loại không thay nhau | SC-M10-003/E4 | END:SUCCESS |
| UC-M10-004 | Người nhận không ACTIVE: DEACTIVATED | SC-M10-003/E5 | END:REJECTED |
| UC-M10-004 | Người nhận không ACTIVE: BANNED | SC-M10-003/E6 | END:REJECTED |
| UC-M10-004 | Người nhận không ACTIVE: DELETED | SC-M10-003/E7 | END:REJECTED |
| UC-M10-004 | Người nhận chưa hoàn tất bước 3 | SC-M10-003/E8 | END:REJECTED |
| UC-M10-004 | Đích sai vai trò cho loại đề xuất | SC-M10-003/E9 | END:REJECTED |
| UC-M10-004 | An gửi đề xuất Admin cho Mai đang MODERATOR hợp lệ | SC-M10-003/E10 | END:SUCCESS |
| UC-M10-004 | Người gửi ADMIN nhưng không gốc | SC-M10-003/E11 | END:REJECTED |
| UC-M10-005 | Lan chọn Từ chối đề xuất Mod còn hiệu lực | SC-M10-004/E1 | END:SUCCESS |
| UC-M10-005 | Lan USER nhận đề xuất Admin của An gốc và chọn Chấp nhận | SC-M10-004/E2 | END:SUCCESS |
| UC-M10-005 | Lan được đề xuất Admin khi là Mod nhưng đã bị giáng về USER trước trả lời, vẫn ACTIVE | SC-M10-004/E3 | END:SUCCESS |
| UC-M10-005 | Bảo đã từ chức/mất ADMIN sau khi gửi hợp lệ R1011, Lan vẫn đủ điều kiện nhận Mod | SC-M10-004/E4 | END:SUCCESS |
| UC-M10-005 | R1011 đã Đã chấp nhận trước khi mở phản hồi | SC-M10-004/E5 | END:REJECTED |
| UC-M10-005 | R1011 đã Đã từ chối trước khi mở phản hồi | SC-M10-004/E6 | END:REJECTED |
| UC-M10-005 | Đã đủ 7×24h trước khi mở phản hồi | SC-M10-004/E7 | END:REJECTED |
| UC-M10-005 | Đề xuất đã bị bản mới cùng loại thay trước khi mở phản hồi | SC-M10-004/E8 | END:REJECTED |
| UC-M10-005 | R1011 đã Đã chấp nhận sau lúc hiển thị, trước xử lý lựa chọn | SC-M10-004/E9 | END:REJECTED |
| UC-M10-005 | R1011 đã Đã từ chối sau lúc hiển thị, trước xử lý lựa chọn | SC-M10-004/E10 | END:REJECTED |
| UC-M10-005 | Đã đủ 7×24h sau lúc hiển thị, trước xử lý lựa chọn | SC-M10-004/E11 | END:REJECTED |
| UC-M10-005 | Đề xuất đã bị bản mới cùng loại thay sau lúc hiển thị, trước xử lý lựa chọn | SC-M10-004/E12 | END:REJECTED |
| UC-M10-005 | Người trả lời không phải người nhận | SC-M10-004/E13 | END:REJECTED |
| UC-M10-005 | Lúc Chấp nhận role không còn hợp lệ | SC-M10-004/E14 | END:REJECTED |
| UC-M10-005 | Lúc Chấp nhận account không ACTIVE | SC-M10-004/E15 | END:REJECTED |
| UC-M10-006 | Target không còn MODERATOR: USER | SC-M10-005/E1 | END:REJECTED |
| UC-M10-006 | Target không còn MODERATOR: ADMIN | SC-M10-005/E2 | END:REJECTED |
| UC-M10-007 | Target không ADMIN: USER | SC-M10-006/E1 | END:REJECTED |
| UC-M10-007 | Target không ADMIN: MODERATOR | SC-M10-006/E2 | END:REJECTED |
| UC-M10-007 | Người thao tác là ADMIN thường, không gốc | SC-M10-006/E3 | END:REJECTED |
| UC-M10-007 | Target là ADMIN gốc, kể cả yêu cầu từ chính gốc | SC-M10-006/E4 | END:REJECTED |
| UC-M10-008 | Mai hủy ở bước xác nhận | SC-M10-007/E1 | END:CANCELLED |
| UC-M10-008 | Role đã không còn MODERATOR/ADMIN tại lúc xử lý xác nhận | SC-M10-007/E2 | END:SUCCESS |
| UC-M10-010 | Đổi riêng Search Bật→Tắt trong khi Tổng đang Tắt | SC-M10-008/E1 | END:SUCCESS |
| UC-M10-010 | Bật riêng Search khi Tổng Bật | SC-M10-008/E2 | END:SUCCESS |
| UC-M10-010 | Đổi riêng Moderation Bật→Tắt trong khi Tổng đang Tắt | SC-M10-008/E3 | END:SUCCESS |
| UC-M10-010 | Bật riêng Moderation khi Tổng Bật | SC-M10-008/E4 | END:SUCCESS |
| UC-M10-010 | Đổi riêng Topic suggestion Bật→Tắt trong khi Tổng đang Tắt | SC-M10-008/E5 | END:SUCCESS |
| UC-M10-010 | Bật riêng Topic suggestion khi Tổng Bật | SC-M10-008/E6 | END:SUCCESS |
| UC-M10-010 | Bảo tắt Tổng rồi bật Tổng lại, giữ từng công tắc riêng | SC-M10-008/E7 | END:SUCCESS |
| UC-M10-010 | Đổi riêng khi Tổng Tắt rồi bật Tổng để dùng giá trị riêng đã lưu | SC-M10-008/E8 | END:SUCCESS |
| UC-M10-010 | Một lời gọi AI lỗi tạm thời ở module nhận, không phải cấu hình Tắt | SC-M10-008/E9 | END:SUCCESS |
| UC-M10-011 | Bảo tắt cấu hình đang Bật | SC-M10-009/E1 | END:SUCCESS |
| UC-M10-012 | Bảo tắt cấu hình đang Bật | SC-M10-010/E1 | END:SUCCESS |
| UC-M10-013 | Bảo bật lại cờ Group | SC-M10-011/E1 | END:SUCCESS |
| UC-M10-013 | Bảo tắt cờ Chat | SC-M10-011/E2 | END:SUCCESS |
| UC-M10-013 | Bảo bật lại cờ Chat | SC-M10-011/E3 | END:SUCCESS |
| UC-M10-013 | Bảo tắt cờ Gamification | SC-M10-011/E4 | END:SUCCESS |
| UC-M10-013 | Bảo bật lại cờ Gamification | SC-M10-011/E5 | END:SUCCESS |
| UC-M10-015 | Đặt mới khi có banner hiện hành | SC-M10-012/E1 | END:SUCCESS |
| UC-M10-015 | Sửa nội dung khác với bản hiện hành | SC-M10-012/E2 | END:SUCCESS |
| UC-M10-015 | Đặt nội dung ASCII dài 1 ký tự | SC-M10-012/E3 | END:SUCCESS |
| UC-M10-015 | Đặt nội dung ASCII dài 200 ký tự | SC-M10-012/E4 | END:SUCCESS |
| UC-M10-015 | Trống; Bảo sửa nội dung để hoàn tất | SC-M10-012/E5 | END:SUCCESS |
| UC-M10-015 | Chỉ khoảng trắng; Bảo sửa nội dung để hoàn tất | SC-M10-012/E6 | END:SUCCESS |
| UC-M10-015 | Quá 200 ký tự; Bảo sửa nội dung để hoàn tất | SC-M10-012/E7 | END:SUCCESS |
| UC-M10-015 | Nội dung trông giống cú pháp đánh dấu nhưng chỉ hiển thị thuần | SC-M10-012/E8 | END:SUCCESS |
| UC-M10-017 | Người xem chỉ đọc banner và không chọn đóng | SC-M10-014/E1 | END:SUCCESS |
| UC-M10-017 | Hiện không có banner được công bố | SC-M10-014/E2 | END:SUCCESS |
| UC-M10-017 | Guest đã đóng đúng bản B100 trong trình duyệt C1 | SC-M10-014/E3 | END:SUCCESS |
| UC-M10-017 | Admin đã sửa nội dung hoặc đặt bản mới sau khi C1 đóng B099 | SC-M10-014/E4 | M3 |
| UC-M10-017 | Guest mở trang khác cùng C1 sau khi đóng | SC-M10-014/E5 | END:SUCCESS |
| UC-M10-023 | Bảo lọc đồng thời người làm Bảo và thao tác đổi AI Search | SC-M10-015/E1 | END:SUCCESS |
| UC-M10-023 | Bảo lọc đồng thời người làm Hệ thống và thao tác thu hồi Mod do ban | SC-M10-015/E2 | END:SUCCESS |
| UC-M10-023 | Bảo đổi chỉ tiêu chí người làm sau khi xem tập chung | SC-M10-015/E3 | END:SUCCESS |
| UC-M10-023 | Bảo đổi chỉ tiêu chí loại thao tác sau khi xem tập chung | SC-M10-015/E4 | END:SUCCESS |
| UC-M10-023 | Không có mục khớp tiêu chí | SC-M10-015/E5 | END:SUCCESS |
| UC-M10-023 | Bất kỳ Admin nào yêu cầu sửa một mục nhật ký | SC-M10-015/E6 | END:REJECTED |
| UC-M10-023 | Bất kỳ Admin nào yêu cầu xóa một mục nhật ký | SC-M10-015/E7 | END:REJECTED |


152 mã hiệu lực = 15 nhóm + 107 FR chi tiết + 30 BR; một mã bỏ ghi riêng. Truy vết ngược tại sources từng bước; vị trí không đồng nghĩa mỗi mã là BF hoặc mọi tổ hợp đã chốt.

Lớp tương đương không nhân theo tên/số lượng: role người khởi tạo, target đủ/sai điều kiện, trước/đúng/sau hạn; các riêng AI, ba feature flags, Bật/Tắt; nội dung banner qua cùng phép kiểm; tiêu chí log. Tổ hợp thay kết quả có đường cụ thể: cùng loại/thay bản/loại khác; role hiện tại khác role nhận đề xuất; người gửi đã mất quyền; Từ chối không chạy guard Chấp nhận; gốc với gửi/thu hồi/từ chức; Tổng off + lưu riêng + bật lại; cờ off + việc tự làm/Admin; banner cũ đã đóng + sửa/đặt mới; hai tiêu chí log. Không lấp mọi tổ hợp nguồn chưa chốt bằng xử lý giả.

## 7. GAP và giới hạn nguồn

| ID | Nguồn/phần ảnh hưởng | Điểm chưa rõ/cách giữ phạm vi |
|---|---|---|
| GAP-SC-M10-001 | NOTE-M10-01; FR-M10-03.10/11; BR-M10-05/27 | Chấp nhận bị từ chối vì role không phù hợp/không ACTIVE đã rõ không đổi role; trạng thái đề xuất sau lỗi và khả năng thử lại chưa chốt. Viết phản hồi từ chối đã có nguồn, không tự đặt Đã từ chối/Hết hiệu lực/giữ Chưa trả lời hoặc tiêu thụ lượt; chưa viết tiếp đường thử lại dựa vào trạng thái chưa rõ. |
| GAP-SC-M10-002 | NOTE-M10-02; FR-M10-13.07; BR-M10-20 | Nguồn chỉ chốt Guest đóng theo trình duyệt; người đăng nhập chưa chốt theo tài khoản/thiết bị, bao lâu/qua phiên và đồng bộ thế nào. Giữ kết quả đóng cho người xem và bản đổi nội dung hiện lại, không tự chọn kỹ thuật hoặc thời hạn. |
| GAP-SC-M10-003 | NOTE-M10-03; FR-M10-13.05/08/09; BR-M10-20 | Chưa chốt đơn vị ký tự Unicode (grapheme/code point/UTF-16) hoặc Sửa nhưng nhập lại cùng nội dung có được coi là bản mới/reset dấu đóng không. Viết biên ASCII trống/1/200/201 và sửa khác nội dung/đặt mới; không gán chính sách cho emoji/ký tự tổ hợp hoặc chỉnh không thay đổi. |
| GAP-SC-M10-004 | NOTE-M10-04; FR-M10-02.08/07.09/09.02/14.01; BR-M10-13 | Chưa chốt lỗi lưu/thông báo/audit, giao dịch nhiều thay đổi, đồng thời hoặc yêu cầu đang chạy. Giữ hợp đồng thành công và thứ tự kiểm→hết hiệu lực bản cũ→lưu mới; không thêm rollback/outbox/retry/khóa hoặc nhận thành công khi chức năng chưa trọn. |
| GAP-SC-M10-005 | NOTE-M10-05; FR-M10-01.03/04/05; BR-M10-29; BR-M06-09 | Chưa liệt kê riêng tập trạng thái account được tìm quản trị, nhất là DELETED. Giữ cách khớp/role/trường đã chốt; không tự lọc chỉ ACTIVE/xong bước 3, giới hạn ba hoặc khẳng định tập đầy đủ tài khoản đã xóa. Mẫu minh họa các account ACTIVE, điều kiện đề xuất vẫn kiểm riêng. |
| TBD-M10-01 | Đã đóng ở FR v1.1; M11/M12/M16 | Giữ chi tiết cờ hiện hành ở RULE004 và nguồn owner, không mở lại TBD chỉ vì đoạn cũ còn dẫn xem TBD. |
| FR-M10-03.05 | Đã bỏ ở v0.1 | Không khôi phục đề xuất vô hạn; dùng đủ 7×24h, đúng mốc hết hạn không trả lời được. |


Năm GAP giới hạn chính những nhánh chưa có hợp đồng; phần độc lập đủ căn cứ đã triển khai và đối chiếu. Tài liệu Đang soạn, không tự sửa FR/US/register/skill/module khác. [QA-M10.md](QA-M10.md) ghi số lượng, lệnh kiểm thực tế và giới hạn của validator.
