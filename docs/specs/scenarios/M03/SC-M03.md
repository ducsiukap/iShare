# Kịch bản nghiệp vụ — M03 Post & Content

[Vietnamese Doc] — 2026-11-08 — Skill scenarios v1.3.

Mục đích: triển khai chức năng actor thực hiện hoàn chỉnh từ FR + US. Boundary là toàn iShare; M01–M15 là các thành phần SYSTEM, ACT-006 là nhà cung cấp AI ngoài boundary. Không có actor Scheduler/DAO/controller.

**Phạm vi:** 4 nhóm UC chính, 17 UC con, 20 mapping; 17 hành trình actor. UC002 đính kèm, UC003 cấu hình poll trước gửi, UC005 chính sách kiểm duyệt được triển khai trong luồng bao chứa. Không tách BF theo điểm AI, vai trò, trạng thái hoặc cờ. Không tạo scenario AUT chỉ hệ thống.

**Ngoài phạm vi:** xét báo cáo/gắn cờ M08, kết luận khiếu nại M09, duyệt nhóm M11, Follow/thông báo M07, vote điểm M12, thuật toán feed/Trending, vận hành AI ngoài contract được dẫn. Accepted Answer/ảnh bìa/ảnh inline không làm; lượt xem và SSR/SEO hoãn.

**Trạng thái:** Đang soạn để review. FR-M03 đã chốt; US-M03/overview Chờ duyệt. Giữ NOTE phần trăm poll chưa có lượt chọn và các giới hạn nguồn; không tự tạo luật mới.

## 1. Baseline và ngữ cảnh

<!-- sc:document -->

| key | value |
|---|---|
| module | M03 |
| scope | ALL |
| skill_version | 1.3 |
| output_dir | docs/specs/scenarios/M03 |
| status | Đang soạn |
| completed_steps | 1, 2, 3, 4 |
| date | 2026-11-08 |
| approval_evidence | - |


| Nguồn | Version | Ngày | Trạng thái | SHA-256 |
|---|---|---|---|---|
| [docs/specs/fr/FR-M03.md](../../fr/FR-M03.md) | 1.10 | 2026-10-24 | Đã chốt | fc996ec5520b6485277fca6a3dbae018bfce02263aba8e15ea87871f35865980 |
| [docs/specs/us/US-M03.md](../../us/US-M03.md) | Không có version tài liệu; skill 2.2 | 2026-10-30 | Chờ duyệt | 29a09c60064999441a47ab4a312c7fe5400e7e4011d6ac40a7f3bf0df82ad7fa |
| [docs/specs/us/US-overview.md](../../us/US-overview.md) | 1.1 | 2026-11-02 | Chờ duyệt | c1d624b7036ea2c7a9968eaa46c482c04fa1a15e2554d536cdfc12f177e26e33 |
| [docs/specs/fr/FR-M01.md](../../fr/FR-M01.md) | 1.10 | 2026-10-24 | Đã chốt | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a |
| [docs/specs/fr/FR-M02.md](../../fr/FR-M02.md) | 1.6 | 2026-10-24 | Đã chốt | e86aca71e0415ee2e121a4fdc3628261be335e9d266fcf6e9654b2fdf3cd357e |
| [docs/specs/fr/FR-M05.md](../../fr/FR-M05.md) | 1.7 | 2026-10-24 | Đã chốt | eb85b5dcb56995d791ed28a8d72a2f91c95588d8cd8d4fb1e74a8aabc2d701aa |
| [docs/specs/fr/FR-M09.md](../../fr/FR-M09.md) | 1.2 | 2026-10-24 | Đã chốt | 8ad8ae5e148c6e446f4bfec7f6e74ba9566c54747a0eda37a3930e94ab96faea |
| [docs/specs/fr/FR-M11.md](../../fr/FR-M11.md) | 1.3 | 2026-10-24 | Đã chốt | 1908d300f75d5f7fa0fd5b31b1d375bc6a63ccd42da254de6e9d0d7d9ef16307 |
| [docs/specs/fr/FR-M13.md](../../fr/FR-M13.md) | 1.3 | 2026-10-24 | Đã chốt | 54630715cc1e391b9ea361247784af26200fc2f01c1b1da96ea56ed1f75f9982 |


FR-M03 có cùng byte/hash với bản làm việc chung. Không lấy danh sách core được chọn ở US-overview làm phạm vi module. [Skill scenarios](../../../../.agent-instructions/skills/scenarios/SKILL.md) là nguồn phương pháp.

<!-- sc:actors -->

| id | name | kind | source |
|---|---|---|---|
| ACT-001 | Guest — chưa có phiên | human | FR-M03-07.01, FR-M03-07.06, FR-M03-12.03 |
| ACT-002 | User — có phiên | human | FR-M03-01.01, FR-M03-08.01, FR-M03-11.04, FR-M03-15.04 |
| ACT-003 | Mod / Admin | human | FR-M03-06.06, FR-M03-14.03, FR-M03-17.04, BR-M03-51 |
| ACT-006 | Dịch vụ AI bên ngoài | external-system | FR-M13-01.01, FR-M13-02.01, FR-M13-02.04, FR-M03-05.01 |


ACT-003 kế thừa hành vi User theo US nhưng miễn quét chỉ ADMIN thực tế. Các phiên đều chịu cổng M01, nhất là BANNED/bảo trì; không thêm đăng nhập vào đầu mọi scenario. Lan/Minh/Admin là dữ liệu vai trò giả lập. Mốc thời gian Asia/Saigon (+07); mỗi SC/nhánh là snapshot độc lập.

| Bộ dữ liệu giả lập | Giá trị |
|---|---|
| D-POST | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa |
| D-POLL | Q301: A="Phương pháp thế", B="Phân tích nhân tử", C="Dùng công thức"; chọn nhiều; ẩn kết quả trước vote; hạn 09/11/2026 10:00 +07; hiện 08/11/2026 10:00 +07 |
| D-HISTORY | Phiên bản trước V1: nội dung "Cách giải thứ nhất", U-LAN sửa 08/11 09:00; V2: "Cách giải thứ hai", U-LAN sửa 08/11 10:00; nội dung hiện hành "Cách giải thứ ba" |
| D-AI | Điểm bốn nhóm minh họa Quấy rối=0.20, Ngôn từ thù ghét=0.10, Nội dung người lớn=0.05, Bạo lực=0.10; max=0.20; Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt |


Giới hạn số từ đếm cụm chữ người đọc thấy ngăn cách khoảng trắng. A×151 là chuỗi A đúng151 ký tự, không phải placeholder. Hạn poll đặt trùng hiện tại được hiểu kết thúc ngay theo BR14; hạn xóa đủ7×24h là hết quyền khôi phục. Với nhánh chỉ ghi max=X (X≥0.20), bộ điểm giả lập là Quấy rối=X, ba nhóm còn lại=0.10; SYSTEM qua M13 lấy max, không giao AI quyết trạng thái bài. Không ép các nhánh dữ liệu loại trừ xảy ra cùng lần thực thi.

## 2. Nhóm use case và bao phủ

<!-- sc:decomposition -->

| core | sub | source |
|---|---|---|
| UC-M03-020 | UC-M03-001 | FR-M03-01, BR-M03-01, BR-M03-02, BR-M03-03, BR-M03-05, BR-M03-41, BR-M03-42 |
| UC-M03-020 | UC-M03-002 | FR-M03-02, BR-M03-04, BR-M03-07, BR-M03-08 |
| UC-M03-020 | UC-M03-003 | FR-M03-03, BR-M03-09, BR-M03-10, BR-M03-11, BR-M03-12 |
| UC-M03-020 | UC-M03-004 | FR-M03-04, BR-M03-19, BR-M03-22, BR-M03-24, BR-M03-25, BR-M03-40, BR-M03-51 |
| UC-M03-020 | UC-M03-005 | FR-M03-04.01, FR-M03-04.03, FR-M03-04.05, FR-M03-04.11, FR-M03-05, BR-M03-26, BR-M03-51 |
| UC-M03-020 | UC-M03-006 | FR-M03-06, BR-M03-23, BR-M03-25 |
| UC-M03-021 | UC-M03-007 | FR-M03-07, BR-M03-18, BR-M03-39, BR-M03-49 |
| UC-M03-021 | UC-M03-008 | FR-M03-08, BR-M03-11, BR-M03-13, BR-M03-16, BR-M03-45 |
| UC-M03-021 | UC-M03-009 | FR-M03-09, BR-M03-14, BR-M03-44 |
| UC-M03-022 | UC-M03-011 | FR-M03-11, BR-M03-26, BR-M03-27, BR-M03-28, BR-M03-47 |
| UC-M03-022 | UC-M03-012 | FR-M03-12, BR-M03-27, BR-M03-28 |
| UC-M03-022 | UC-M03-002 | FR-M03-02, BR-M03-04, BR-M03-07, BR-M03-08 |
| UC-M03-022 | UC-M03-005 | FR-M03-04.01, FR-M03-04.03, FR-M03-04.05, FR-M03-04.11, FR-M03-05, BR-M03-26, BR-M03-51 |
| UC-M03-023 | UC-M03-013 | FR-M03-13.01, FR-M03-13.03, FR-M03-13.04, BR-M03-29 |
| UC-M03-023 | UC-M03-017 | FR-M03-13.02, FR-M03-13.03, FR-M03-13.05, FR-M03-13.06, BR-M03-26, BR-M03-29, BR-M03-33 |
| UC-M03-023 | UC-M03-014 | FR-M03-14, BR-M03-30, BR-M03-31, BR-M03-32 |
| UC-M03-023 | UC-M03-015 | FR-M03-15, BR-M03-34, BR-M03-35 |
| UC-M03-023 | UC-M03-016 | FR-M03-16, BR-M03-35, BR-M03-36, BR-M03-37 |
| UC-M03-023 | UC-M03-018 | FR-M03-07.08, FR-M03-07.09, FR-M03-07.10, FR-M03-07.11, FR-M03-17.04, BR-M03-37, BR-M03-49 |
| UC-M03-023 | UC-M03-005 | FR-M03-04.01, FR-M03-04.03, FR-M03-04.05, FR-M03-04.11, FR-M03-05, BR-M03-26, BR-M03-51 |


<!-- sc:ucs -->

| id | treatment | scenarios | coverage | rationale | sources |
|---|---|---|---|---|---|
| UC-M03-020 | aggregate | SC-M03-001, SC-M03-004, SC-M03-006 | SC-M03-001/M1, SC-M03-004/M1, SC-M03-006/M1 | Nhóm chức năng độc lập; không chạy tất cả UC con nối tiếp. | FR-M03-01, FR-M03-02, FR-M03-03, FR-M03-04, FR-M03-05, FR-M03-06 |
| UC-M03-021 | aggregate | SC-M03-007, SC-M03-008, SC-M03-009, SC-M03-019, SC-M03-020 | SC-M03-007/M1, SC-M03-008/M1, SC-M03-009/M1, SC-M03-019/M1, SC-M03-020/M1 | Nhóm chức năng độc lập; không chạy tất cả UC con nối tiếp. | FR-M03-07, FR-M03-08, FR-M03-09, FR-M03-10 |
| UC-M03-022 | aggregate | SC-M03-011, SC-M03-012 | SC-M03-011/M1, SC-M03-012/M1 | Nhóm chức năng độc lập; không chạy tất cả UC con nối tiếp. | FR-M03-02.02, FR-M03-11, FR-M03-12, BR-M03-26, BR-M03-27 |
| UC-M03-023 | aggregate | SC-M03-013, SC-M03-014, SC-M03-015, SC-M03-016, SC-M03-017, SC-M03-018, SC-M03-021 | SC-M03-013/M1, SC-M03-014/M1, SC-M03-015/M1, SC-M03-016/M1, SC-M03-017/M1, SC-M03-018/M1, SC-M03-021/M1 | Nhóm chức năng độc lập; không chạy tất cả UC con nối tiếp. | FR-M03-13, FR-M03-14, FR-M03-15, FR-M03-16, FR-M03-17, FR-M03-07.08 |
| UC-M03-001 | scenario | SC-M03-001 | SC-M03-001/M1 | Sở hữu mục tiêu chức năng actor; các bước có nguồn bên dưới. | FR-M03-01, BR-M03-01, BR-M03-02, BR-M03-03, BR-M03-05, BR-M03-41, BR-M03-42 |
| UC-M03-002 | embedded | SC-M03-001, SC-M03-011 | SC-M03-001/E7.1, SC-M03-011/E10.1 | UC hỗ trợ được triển khai trong các bước/nhánh của hành trình, không có BF riêng. | FR-M03-02, BR-M03-04, BR-M03-07, BR-M03-08 |
| UC-M03-003 | embedded | SC-M03-001 | SC-M03-001/E15.1 | UC hỗ trợ được triển khai trong các bước/nhánh của hành trình, không có BF riêng. | FR-M03-03, BR-M03-09, BR-M03-10, BR-M03-11, BR-M03-12 |
| UC-M03-004 | scenario | SC-M03-004 | SC-M03-004/M1 | Sở hữu mục tiêu chức năng actor; các bước có nguồn bên dưới. | FR-M03-04, BR-M03-19, BR-M03-22, BR-M03-24, BR-M03-25, BR-M03-40, BR-M03-51 |
| UC-M03-005 | embedded | SC-M03-004, SC-M03-011, SC-M03-017 | SC-M03-004/M2, SC-M03-011/M4, SC-M03-017/M2 | UC hỗ trợ được triển khai trong các bước/nhánh của hành trình, không có BF riêng. | FR-M03-04.01, FR-M03-04.03, FR-M03-04.05, FR-M03-04.11, FR-M03-05, BR-M03-26, BR-M03-51 |
| UC-M03-006 | scenario | SC-M03-006 | SC-M03-006/M1 | Sở hữu mục tiêu chức năng actor; các bước có nguồn bên dưới. | FR-M03-06, BR-M03-23, BR-M03-25 |
| UC-M03-007 | scenario | SC-M03-007 | SC-M03-007/M1 | Sở hữu mục tiêu chức năng actor; các bước có nguồn bên dưới. | FR-M03-07, BR-M03-18, BR-M03-39, BR-M03-49 |
| UC-M03-008 | scenario | SC-M03-007, SC-M03-008 | SC-M03-007/M1, SC-M03-008/M1 | Sở hữu mục tiêu chức năng actor; các bước có nguồn bên dưới. | FR-M03-08, BR-M03-11, BR-M03-13, BR-M03-16, BR-M03-45 |
| UC-M03-009 | scenario | SC-M03-009, SC-M03-019, SC-M03-020 | SC-M03-009/M1, SC-M03-019/M1, SC-M03-020/M1 | Sở hữu mục tiêu chức năng actor; các bước có nguồn bên dưới. | FR-M03-09, BR-M03-14, BR-M03-44 |
| UC-M03-011 | scenario | SC-M03-011 | SC-M03-011/M1 | Sở hữu mục tiêu chức năng actor; các bước có nguồn bên dưới. | FR-M03-11, BR-M03-26, BR-M03-27, BR-M03-28, BR-M03-47 |
| UC-M03-012 | scenario | SC-M03-007, SC-M03-012 | SC-M03-007/M1, SC-M03-012/M1 | Sở hữu mục tiêu chức năng actor; các bước có nguồn bên dưới. | FR-M03-12, BR-M03-27, BR-M03-28 |
| UC-M03-013 | scenario | SC-M03-013 | SC-M03-013/M1 | Sở hữu mục tiêu chức năng actor; các bước có nguồn bên dưới. | FR-M03-13.01, FR-M03-13.03, FR-M03-13.04, BR-M03-29 |
| UC-M03-017 | scenario | SC-M03-017 | SC-M03-017/M1 | Sở hữu mục tiêu chức năng actor; các bước có nguồn bên dưới. | FR-M03-13.02, FR-M03-13.03, FR-M03-13.05, FR-M03-13.06, BR-M03-26, BR-M03-29, BR-M03-33 |
| UC-M03-014 | scenario | SC-M03-014, SC-M03-021 | SC-M03-014/M1, SC-M03-021/M1 | Sở hữu mục tiêu chức năng actor; các bước có nguồn bên dưới. | FR-M03-14, BR-M03-30, BR-M03-31, BR-M03-32 |
| UC-M03-015 | scenario | SC-M03-015 | SC-M03-015/M1 | Sở hữu mục tiêu chức năng actor; các bước có nguồn bên dưới. | FR-M03-15, BR-M03-34, BR-M03-35 |
| UC-M03-016 | scenario | SC-M03-016 | SC-M03-016/M1 | Sở hữu mục tiêu chức năng actor; các bước có nguồn bên dưới. | FR-M03-16, BR-M03-35, BR-M03-36, BR-M03-37 |
| UC-M03-018 | scenario | SC-M03-018 | SC-M03-018/M1 | Sở hữu mục tiêu chức năng actor; các bước có nguồn bên dưới. | FR-M03-07.08, FR-M03-07.09, FR-M03-07.10, FR-M03-07.11, FR-M03-17.04, BR-M03-37, BR-M03-49 |


| SVG nguồn | UC thành viên | Đối chiếu |
|---|---|---|
| D-M03-CORE | 4 | Khớp ID thành viên với US; không tạo quan hệ UML mới |
| D-M03-020 | 7 | Khớp ID thành viên với US; không tạo quan hệ UML mới |
| D-M03-021 | 5 | Khớp ID thành viên với US; không tạo quan hệ UML mới |
| D-M03-022 | 6 | Khớp ID thành viên với US; không tạo quan hệ UML mới |
| D-M03-023 | 8 | Khớp ID thành viên với US; không tạo quan hệ UML mới |


## 3. Danh mục luồng chức năng

<!-- sc:flows -->

| id | uc | primary | trigger | goal | completion | covered_ucs | rationale | scenario | sources |
|---|---|---|---|---|---|---|---|---|---|
| BF-M03-001 | UC-M03-001 | ACT-002 | Lan mở trình soạn bài mới. | Soạn và lưu bài nháp | Nháp hợp lệ được lưu với ba chiều trạng thái ban đầu, tác giả và mốc thời gian. Không gửi/quét bài; Lớp bài độc lập hồ sơ. | UC-M03-001, UC-M03-002, UC-M03-003 | Chức năng actor yêu cầu độc lập, đi đến kết quả quan sát được. | SC-M03-001 | FR-M03-01.01, FR-M03-01.02, FR-M03-01.03, FR-M03-01.04, FR-M03-01.05, FR-M03-01.11, BR-M03-01, BR-M03-02, BR-M03-03, BR-M03-04, BR-M03-05, BR-M03-06, BR-M03-50, FR-M03-01.07, FR-M05-01.01, FR-M05-01.10, FR-M03-01.16, BR-M03-42, BR-M03-43, FR-M03-01.06, FR-M03-01.08, FR-M03-01.09, FR-M03-01.10, FR-M03-01.12, FR-M03-01.13, FR-M03-01.14, FR-M03-01.15, BR-M03-17, BR-M03-38, BR-M03-41, BR-M03-48, BR-M03-47, FR-M03-01.17, FR-M03-02.01, BR-M03-07, BR-M03-08, FR-M03-02.02, FR-M03-02.03, FR-M03-02.04, FR-M03-02.05, FR-M03-02.06, FR-M03-02.07, FR-M03-02.08, FR-M03-02.09, FR-M03-02.10, FR-M03-02.11, FR-M03-03.01, FR-M03-03.02, FR-M03-03.05, FR-M03-03.06, BR-M03-10, BR-M03-11, FR-M03-03.07, FR-M03-03.03, FR-M03-03.04, FR-M03-03.08, FR-M03-03.09, FR-M03-03.10, FR-M03-03.11, BR-M03-09, BR-M03-12, BR-M03-44, FR-M03-07.06 |
| BF-M03-004 | UC-M03-004 | ACT-002 | Lan chọn Gửi bài nháp P301. | Gửi hoặc gửi lại bài để đăng theo chính sách | Yêu cầu gửi được xử lý đúng chính sách và trả trạng thái cụ thể: chuẩn Đã đăng; các nhánh có thể chờ người duyệt hoặc bị từ chối. Không tuyên bố đã được người duyệt chấp thuận khi mới vào hàng chờ. | UC-M03-004, UC-M03-005 | Chức năng actor yêu cầu độc lập, đi đến kết quả quan sát được. | SC-M03-004 | FR-M03-04.01, FR-M03-04.02, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43, BR-M03-19, BR-M03-40, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M03-05.01, BR-M03-20, FR-M05-01.03, FR-M05-01.09, FR-M03-04.03, FR-M03-05.08, BR-M03-22, FR-M03-04.04, BR-M03-24, FR-M03-05.02, FR-M03-05.03, FR-M03-05.12, FR-M03-05.13, BR-M03-46, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M03-05.04, BR-M03-21, FR-M03-04.05, BR-M03-25, FR-M11-12.01, FR-M11-12.04, FR-M11-12.05, FR-M11-12.03, FR-M11-12.16, FR-M11-12.18, FR-M11-12.19, FR-M11-12.02, FR-M11-12.17, FR-M11-12.14, FR-M11-12.11, FR-M11-12.15, FR-M03-07.06, FR-M03-04.11, FR-M03-05.15, BR-M03-51, FR-M11-12.06, FR-M11-12.20 |
| BF-M03-006 | UC-M03-006 | ACT-003 | Mod Minh yêu cầu hàng chờ duyệt hệ thống. | Duyệt bài đang nằm trong hàng chờ Mod hệ thống | Quyết định hợp lệ được ghi: chấp nhận Đã đăng hoặc từ chối Bị từ chối kèm lý do. Không quyết định cho bài đã đổi trạng thái. | UC-M03-006 | Chức năng actor yêu cầu độc lập, đi đến kết quả quan sát được. | SC-M03-006 | FR-M03-06.01, FR-M03-06.06, BR-M03-25, FR-M03-06.02, FR-M03-06.07, BR-M03-23, FR-M03-06.03, FR-M03-06.05, FR-M03-06.04, FR-M03-07.06 |
| BF-M03-007 | UC-M03-007 | ACT-002 | Minh mở đường dẫn bài P301. | Đọc bài viết và kết quả poll được phép | Bài và kết quả được hiển thị đúng quyền, không biến quyền đọc thành quyền tương tác; không đếm lượt xem ở MS1. | UC-M03-007, UC-M03-008, UC-M03-012 | Chức năng actor yêu cầu độc lập, đi đến kết quả quan sát được. | SC-M03-007 | FR-M03-07.01, FR-M03-07.02, FR-M03-07.03, FR-M03-07.04, FR-M03-07.05, FR-M03-07.07, BR-M03-17, BR-M03-18, BR-M03-39, BR-M03-49, FR-M03-02.03, FR-M03-08.07, FR-M03-12.01, BR-M03-04, FR-M05-04.04, FR-M05-04.05, FR-M11-03.06, FR-M01-13.01, FR-M03-06.05, FR-M03-08.08, FR-M03-08.09, FR-M03-08.10, FR-M03-08.12, BR-M03-15, FR-M03-08.01, FR-M03-08.03, FR-M03-08.13, BR-M03-11, FR-M03-12.02, FR-M03-12.03, FR-M03-12.04, BR-M03-27 |
| BF-M03-008 | UC-M03-008 | ACT-002 | Minh chọn A,C của Q301 và gửi phiếu. | Ghi, đổi hoặc bỏ phiếu poll của mình | Phiếu của actor được ghi/thay/xóa theo lựa chọn hợp lệ; kết quả hiển thị đúng cấu hình và trạng thái poll. | UC-M03-008 | Chức năng actor yêu cầu độc lập, đi đến kết quả quan sát được. | SC-M03-008 | FR-M03-08.01, FR-M03-08.03, BR-M03-10, BR-M03-11, FR-M03-08.09, FR-M03-08.11, FR-M03-08.12, FR-M03-08.13, BR-M03-15, BR-M03-45, FR-M03-08.06, BR-M03-13, FR-M03-08.04, BR-M03-16, FR-M03-08.05, FR-M03-08.07, FR-M03-08.02, FR-M03-07.06 |
| BF-M03-009 | UC-M03-009 | ACT-002 | Lan gửi hạn kết thúc mới cho Q301. | Đổi hạn kết thúc của poll đang mở | Hạn hợp lệ được cập nhật; không mở lại poll đã đóng. | UC-M03-009 | Actor có thể yêu cầu dời hạn riêng mà không đóng poll hoặc thêm lựa chọn. | SC-M03-009 | FR-M03-09.01, FR-M03-09.03, FR-M03-09.04, FR-M03-09.05, BR-M03-12, BR-M03-14, FR-M03-09.08, BR-M03-13, BR-M03-44, FR-M03-09.02, FR-M03-10.02, FR-M03-07.06 |
| BF-M03-011 | UC-M03-011 | ACT-002 | Lan mở sửa bài P301 đã gửi của mình. | Sửa và lưu phiên bản bài đã gửi của mình | Bản sửa hợp lệ và phiên bản trước được ghi, actor nhận kết quả; không bảo đảm luôn công khai vì quét lại có thể gắn cờ hoặc bài còn chịu ràng buộc khác. | UC-M03-002, UC-M03-005, UC-M03-011 | Chức năng actor yêu cầu độc lập, đi đến kết quả quan sát được. | SC-M03-011 | FR-M03-11.01, FR-M03-11.04, FR-M03-11.07, FR-M03-01.16, FR-M03-03.11, BR-M03-47, FR-M03-11.02, FR-M03-11.03, FR-M03-05.05, FR-M03-05.06, FR-M03-12.01, BR-M03-26, BR-M03-27, BR-M03-38, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M03-05.10, FR-M03-02.11, FR-M03-01.14, FR-M03-01.15, FR-M03-01.17, BR-M03-42, BR-M03-43, FR-M03-05.14, FR-M03-04.04, BR-M03-24, FR-M03-05.08, FR-M03-05.09, BR-M03-22, FR-M03-05.07, FR-M03-02.02, FR-M03-02.01, FR-M03-02.03, FR-M03-02.04, FR-M03-02.05, FR-M03-02.06, FR-M03-02.07, FR-M03-02.08, FR-M03-02.09, FR-M03-02.10, BR-M03-04, BR-M03-07, BR-M03-08, FR-M05-01.07, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M03-05.11, FR-M03-07.06, FR-M03-05.15, BR-M03-51 |
| BF-M03-012 | UC-M03-012 | ACT-002 | Minh chọn Xem lịch sử trên P301. | Xem các phiên bản lịch sử sửa bài | Người được phép đọc nhận các phiên bản trước; quyền xem lịch sử không vượt quyền đọc bài. | UC-M03-012 | Chức năng actor yêu cầu độc lập, đi đến kết quả quan sát được. | SC-M03-012 | FR-M03-12.02, FR-M03-12.01, FR-M03-12.03, FR-M03-12.04, BR-M03-27, FR-M03-07.01, FR-M03-07.02, FR-M03-07.05 |
| BF-M03-013 | UC-M03-013 | ACT-002 | Lan yêu cầu Tự ẩn P301. | Tự ẩn bài đang đăng của mình | Bài thành Tự ẩn, không còn công khai qua đường thường; kiểm duyệt/khóa không tự bị gỡ. | UC-M03-013 | Chức năng actor yêu cầu độc lập, đi đến kết quả quan sát được. | SC-M03-013 | FR-M03-13.01, FR-M03-13.03, FR-M03-13.04, BR-M03-29, FR-M03-07.06 |
| BF-M03-014 | UC-M03-014 | ACT-002 | Lan chọn Khóa bình luận cho P301 của mình. | Đặt mức khóa cho bài viết | Mức khóa/người khóa được ghi đúng quyền, các hệ quả tương tác được áp; bài không bị ẩn chỉ vì khóa. | UC-M03-014 | Chức năng actor yêu cầu độc lập, đi đến kết quả quan sát được. | SC-M03-014 | FR-M03-14.01, FR-M03-14.04, FR-M03-14.05, BR-M03-17, BR-M03-30, BR-M03-32, FR-M03-14.09, FR-M03-14.11, FR-M03-14.10, FR-M03-07.06, FR-M03-14.02, FR-M03-14.06, FR-M03-14.12, BR-M03-31, FR-M03-14.03 |
| BF-M03-015 | UC-M03-015 | ACT-002 | Lan chọn Xóa P301 của mình. | Xóa mềm bài của mình | Bài Đã xóa có mốc và trạng thái trước, không công khai; còn cơ hội khôi phục theo hạn/quyền. Không trừ/xóa dữ liệu vật lý ngoài giao tiếp nguồn. | UC-M03-015 | Chức năng actor yêu cầu độc lập, đi đến kết quả quan sát được. | SC-M03-015 | FR-M03-15.01, FR-M03-15.02, FR-M03-15.03, FR-M03-15.04, FR-M03-15.05, FR-M03-16.02, BR-M03-34, BR-M03-35, FR-M03-15.06, FR-M03-06.07, FR-M03-07.06 |
| BF-M03-016 | UC-M03-016 | ACT-002 | Lan yêu cầu Khôi phục P301 của mình từ tab Đã xóa. | Khôi phục bài đã xóa trong thời hạn | Bài trở về đúng trạng thái trước xóa; riêng trước đó Chờ duyệt thì về Nháp. Không phục hồi sau hạn hoặc tự bỏ khóa/kiểm duyệt. | UC-M03-016 | Chức năng actor yêu cầu độc lập, đi đến kết quả quan sát được. | SC-M03-016 | FR-M03-16.01, FR-M03-16.02, FR-M03-16.03, FR-M03-16.04, FR-M03-16.05, BR-M03-35, BR-M03-36, BR-M03-38, FR-M03-16.06, FR-M03-07.06 |
| BF-M03-017 | UC-M03-017 | ACT-002 | Lan yêu cầu Hiện lại P301. | Hiện lại bài đã tự ẩn | Trạng thái đăng được hiện lại đúng chính sách; không gỡ Bị Mod ẩn, cờ gắn cờ hoặc quyền nhóm trái nguồn. | UC-M03-005, UC-M03-017 | Chức năng actor yêu cầu độc lập, đi đến kết quả quan sát được. | SC-M03-017 | FR-M03-13.02, FR-M03-13.03, FR-M03-13.05, FR-M03-13.06, BR-M03-26, BR-M03-29, BR-M03-33, FR-M03-05.05, FR-M03-05.06, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M03-05.10, FR-M03-05.07, FR-M03-05.08, FR-M03-05.09, BR-M03-22, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M03-05.11, FR-M03-07.06, FR-M03-05.15, BR-M03-51 |
| BF-M03-018 | UC-M03-018 | ACT-002 | Lan mở thông báo kết quả xử lý về P301 của mình. | Xem lại bài từ ngữ cảnh xử lý hoặc khiếu nại liên quan | Bài được trả chỉ đọc trong ngữ cảnh hợp lệ, bảo vệ dữ liệu báo cáo; không hồi sinh nội dung công khai hoặc tạo nơi duyệt bài đã xóa. | UC-M03-018 | Chức năng actor yêu cầu độc lập, đi đến kết quả quan sát được. | SC-M03-018 | FR-M03-07.08, FR-M03-07.09, FR-M03-07.10, FR-M03-17.02, FR-M03-17.03, BR-M03-37, FR-M03-17.04, BR-M03-49, FR-M03-07.06, FR-M03-07.11, FR-M03-07.02, FR-M03-07.07 |
| BF-M03-019 | UC-M03-009 | ACT-002 | Lan yêu cầu Kết thúc ngay Q301. | Kết thúc poll ngay | Poll đóng ngay, kết quả được hiển thị đúng quyền và sự kiện kết thúc được cung cấp; không gửi phiếu mới. | UC-M03-009 | Actor yêu cầu chấm dứt nhận phiếu ngay, khác kết quả chỉ dời hạn hoặc thêm lựa chọn. | SC-M03-019 | FR-M03-09.02, FR-M03-09.04, FR-M03-10.02, FR-M03-08.06, FR-M03-08.10, FR-M03-08.12, BR-M03-13, BR-M03-14, BR-M03-15, FR-M03-09.03, FR-M03-09.08, BR-M03-44, FR-M03-07.06 |
| BF-M03-020 | UC-M03-009 | ACT-002 | Lan gửi lựa chọn D mới cho Q301. | Thêm lựa chọn vào poll đang mở của bài đã gửi | Lựa chọn mới được thêm hợp lệ; lựa chọn cũ và phiếu được giữ. | UC-M03-009 | Actor bổ sung phương án trả lời mới; không đòi dời hạn hoặc đóng poll. | SC-M03-020 | FR-M03-09.06, FR-M03-09.04, FR-M03-09.07, FR-M03-09.08, BR-M03-44, FR-M03-09.03, BR-M03-13, BR-M03-14, FR-M03-03.11, BR-M03-11, FR-M03-07.06 |
| BF-M03-021 | UC-M03-014 | ACT-002 | Lan yêu cầu mở khóa bình luận P301 do mình khóa. | Mở khóa hoặc hạ mức khóa bài viết | Mức khóa được mở/hạ hợp lệ; không vượt khóa Mod/Admin hoặc thay quyền đọc. | UC-M03-014 | Actor yêu cầu khôi phục khả năng tương tác, khác chức năng đặt hạn chế mới. | SC-M03-021 | FR-M03-14.07, BR-M03-32, FR-M03-14.09, FR-M03-14.11, FR-M03-07.06, FR-M03-14.08 |


UC009 có ba chức năng actor yêu cầu riêng: đổi hạn, kết thúc ngay và thêm lựa chọn; UC014 có đặt khóa và mở/hạ khóa. Đây là các mục tiêu có kết quả riêng, không nhân BF theo trạng thái. Soạn/lưu nháp khác gửi bài; gửi hoàn tất khi tác giả nhận đúng kết quả xử lý cổng, không bắt actor người gửi quyết định thay Mod/Owner.

Các quan hệ include/extend giữ nguyên theo US. Điểm gọi đính kèm/poll được viết thành các lượt actor–SYSTEM ngay trong SC001/011; các điểm đọc–vote/lịch sử được khai triển trong SC007. Include UC005 luôn áp chính sách, không đồng nghĩa luôn gọi AI. Mỗi lượt quét trong SC là thứ tự nghiệp vụ, không khẳng định HTTP đồng bộ hay UI phải chặn chờ.

| Quan hệ | Điểm gọi | Nơi triển khai/hoàn tất |
|---|---|---|
| UC-M03-002 extend UC-M03-001 | EP-DRAFT-ATTACH | #uc-m03-001-main-2 |
| UC-M03-003 extend UC-M03-001 | EP-DRAFT-POLL | #uc-m03-001-main-2 |
| UC-M03-002 extend UC-M03-011 | EP-EDIT-ATTACH | #uc-m03-011-main-2 |
| UC-M03-004 include UC-M03-005 | #uc-m03-004-main-3 | #uc-m03-004-main-4 |
| UC-M03-011 include UC-M03-005 | #uc-m03-011-main-4 | #uc-m03-011-main-5 |
| UC-M03-017 include UC-M03-005 | #uc-m03-017-main-2 | #uc-m03-017-main-3 |
| UC-M03-008 extend UC-M03-007 | EP-READ-VOTE | #uc-m03-007-main-3 |
| UC-M03-012 extend UC-M03-007 | EP-READ-HISTORY | #uc-m03-007-main-4 |


## 4. Scenario sáu phần

<a id="sc-m03-001"></a>

<!-- sc:scenario SC-M03-001 -->

### SC-M03-001

#### 1. Tên kịch bản chuẩn

Soạn và lưu bài nháp — BF-M03-001. UC owner: [UC-M03-001](../../us/US-M03.md#uc-m03-001). Trigger: Lan mở trình soạn bài mới.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Có phiên được M01 cho phép soạn; tác giả và mức cảnh cáo kiểm khi lưu. Đường chuẩn tạo nháp mới, cảnh cáo NONE/LIGHT; chưa có bài được gửi. Nháp không bắt buộc có Topic hoặc nội dung đầy đủ để gửi.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-001 -->

| result | condition |
|---|---|
| SUCCESS | Nháp hợp lệ được lưu với ba chiều trạng thái ban đầu, tác giả và mốc thời gian. Không gửi/quét bài; Lớp bài độc lập hồ sơ. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-001 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan mở trình soạn bài mới. | U-LAN; chưa tạo bài được lưu | M2 | FR-M03-01.01 |
| M2 | SYSTEM | Hệ thống cung cấp trình soạn một loại bài, hỗ trợ định dạng BR-M03-03 và LaTeX mã thô; có Lớp/Khối, tệp và poll tùy chọn; không có lựa chọn loại bài, ảnh inline hoặc ảnh bìa. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa | M3 | FR-M03-01.02, FR-M03-01.03, FR-M03-01.04, FR-M03-01.05, FR-M03-01.11, BR-M03-01, BR-M03-02, BR-M03-03, BR-M03-04, BR-M03-05, BR-M03-06, BR-M03-50 |
| M3 | ACT-002 | Lan nhập tiêu đề/nội dung LaTeX, chọn Lớp 10 và Topic Toán thủ công. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa | M4 | FR-M03-01.03, FR-M03-01.05, FR-M03-01.07, FR-M05-01.01, FR-M05-01.10 |
| M4 | SYSTEM | Hệ thống hiển thị nội dung định dạng/công thức từ mã thô; kiểm khi đang soạn, cảnh báo ngay kèm số hiện tại nếu vượt độ dài. Bộ dữ liệu chuẩn không vượt giới hạn. | LaTeX x^2 + 2x + 1 = 0 hiển thị công thức tương ứng; tiêu đề ≤150, nội dung ≤6000 từ; ảnh chỉ dưới nội dung | M5 | FR-M03-01.02, FR-M03-01.03, FR-M03-01.04, FR-M03-01.16, BR-M03-03, BR-M03-04, BR-M03-05, BR-M03-42, BR-M03-43 |
| M5 | ACT-002 | Lan chọn Lưu nháp. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; không yêu cầu công bố | M6 | FR-M03-01.01 |
| M6 | SYSTEM | Hệ thống kiểm tác giả, hạn chế tạo nháp mới, Lớp hợp lệ, ít nhất một trong tiêu đề/nội dung/poll/tệp và giới hạn độ dài; lưu P301 Nháp/Bình thường/Không khóa cùng tác giả và thời điểm tạo/cập nhật, trả nháp đã lưu. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; tạo=cập nhật=08/11 10:00; chưa quét công bố | END:SUCCESS | FR-M03-01.01, FR-M03-01.06, FR-M03-01.07, FR-M03-01.08, FR-M03-01.09, FR-M03-01.10, FR-M03-01.12, FR-M03-01.13, FR-M03-01.14, FR-M03-01.15, BR-M03-06, BR-M03-17, BR-M03-38, BR-M03-41, BR-M03-42, BR-M03-48 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-001 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M6 | Tác giả đang MEDIUM hoặc HEAVY khi lưu nháp mới | E1.1 | FR-M03-01.10, BR-M03-38 |
| E2 | system | M6 | Cả tiêu đề, nội dung, poll, tệp đều trống | E2.1 | FR-M03-01.13, BR-M03-41 |
| E3 | system | M6 | Lớp/Khối bài ngoài 10,11,12 và không trống | E3.1 | FR-M03-01.06, BR-M03-06 |
| E4 | system | M6 | Nháp chỉ có một thành phần hợp lệ trong tiêu đề/nội dung/poll/tệp | E4.1 | FR-M03-01.01, FR-M03-01.08, FR-M03-01.09, FR-M03-01.12, FR-M03-01.13, BR-M03-41, FR-M05-01.10 |
| E5 | user-choice | M1 | Tác giả mở và cập nhật bài Nháp đã lưu trước đó | E5.1 | FR-M03-01.01, BR-M03-47, FR-M03-01.02, FR-M03-01.08, FR-M03-01.13, FR-M03-01.14, FR-M03-01.15, BR-M03-41, BR-M03-42 |
| E6 | user-choice | M3 | Trong lúc nhập, tiêu đề 151 ký tự hoặc nội dung 6001 từ | E6.1 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |
| E7 | user-choice | M3 | Tại EP-DRAFT-ATTACH, tác giả chọn thêm rồi bỏ tệp trước khi lưu | E7.1 | FR-M03-02.01, BR-M03-07, BR-M03-08, FR-M03-02.02, FR-M03-02.03, FR-M03-02.04, FR-M03-02.05, FR-M03-02.06, FR-M03-02.07, FR-M03-02.08, FR-M03-02.09, FR-M03-02.10, FR-M03-02.11, BR-M03-04, FR-M03-01.01, FR-M03-01.08, FR-M03-01.09, FR-M03-01.12, FR-M03-01.13 |
| E8 | user-choice | M3 | EP-DRAFT-ATTACH: Ảnh sai định dạng | E8.1 | FR-M03-02.04, BR-M03-02, BR-M03-07, BR-M03-08, FR-M03-01.01, FR-M03-02.01 |
| E9 | user-choice | M3 | EP-DRAFT-ATTACH: Ảnh quá dung lượng | E9.1 | FR-M03-02.05, BR-M03-02, BR-M03-07, BR-M03-08, FR-M03-01.01, FR-M03-02.01 |
| E10 | user-choice | M3 | EP-DRAFT-ATTACH: Thêm ảnh thứ 11 | E10.1 | FR-M03-02.06, BR-M03-02, BR-M03-07, BR-M03-08, FR-M03-01.01, FR-M03-02.01 |
| E11 | user-choice | M3 | EP-DRAFT-ATTACH: Tài liệu sai loại | E11.1 | FR-M03-02.07, BR-M03-02, BR-M03-07, BR-M03-08, FR-M03-01.01, FR-M03-02.01 |
| E12 | user-choice | M3 | EP-DRAFT-ATTACH: Tài liệu quá dung lượng | E12.1 | FR-M03-02.08, BR-M03-02, BR-M03-07, BR-M03-08, FR-M03-01.01, FR-M03-02.01 |
| E13 | user-choice | M3 | EP-DRAFT-ATTACH: Thêm tài liệu thứ 4 | E13.1 | FR-M03-02.09, BR-M03-02, BR-M03-07, BR-M03-08, FR-M03-01.01, FR-M03-02.01 |
| E14 | system | M6 | Yêu cầu lưu kèm thêm/bỏ tệp do người khác tác giả gửi | E14.1 | FR-M03-02.11 |
| E15 | user-choice | M3 | Tại EP-DRAFT-POLL, tác giả muốn poll thay vì chỉ văn bản | E15.1 | FR-M03-03.01, FR-M03-03.02, FR-M03-03.05, FR-M03-03.06, BR-M03-10, BR-M03-11, FR-M03-03.07, FR-M03-03.03, FR-M03-03.04, FR-M03-03.08, FR-M03-03.09, FR-M03-03.10, FR-M03-03.11, BR-M03-09, BR-M03-12, BR-M03-44, FR-M03-01.01, FR-M03-01.08, FR-M03-01.09, FR-M03-01.12 |
| E16 | user-choice | M3 | EP-DRAFT-POLL: Số lựa chọn không hợp lệ | E16.1 | FR-M03-03.03 |
| E17 | user-choice | M3 | EP-DRAFT-POLL: Thêm poll thứ hai | E17.1 | FR-M03-03.04 |
| E18 | user-choice | M3 | EP-DRAFT-POLL: Thiếu hạn | E18.1 | FR-M03-03.07 |
| E19 | user-choice | M3 | EP-DRAFT-POLL: Hạn trước hiện tại | E19.1 | FR-M03-03.09 |
| E20 | user-choice | M3 | EP-DRAFT-POLL: Người tạo khác tác giả | E20.1 | FR-M03-03.08 |
| E21 | user-choice | M3 | Trong khi còn nháp, tác giả chọn sửa poll đang có | E21.1 | FR-M03-03.10, FR-M03-03.03, FR-M03-03.05, FR-M03-03.09, BR-M03-11, BR-M03-44, FR-M03-01.01 |
| E22 | user-choice | M3 | Trong khi còn nháp, tác giả chọn bỏ poll | E22.1 | FR-M03-03.10, BR-M03-44, FR-M03-01.01 |


<!-- sc:branch SC-M03-001 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối tạo nháp mới; không suy rộng hạn chế này sang sửa bài Đã đăng. | U-LAN MEDIUM/HEAVY; không tạo P301 | END:REJECTED | FR-M03-01.10, BR-M03-38 |


<!-- sc:branch SC-M03-001 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối lưu nháp trống; chỉ chọn Lớp không thay thế bốn thành phần. | title=""; body=""; poll=không; tệp=[]; Lớp=10 | END:REJECTED | FR-M03-01.13, BR-M03-41 |


<!-- sc:branch SC-M03-001 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối lưu bài với Lớp không hợp lệ. | Lớp bài=9 | END:REJECTED | FR-M03-01.06, BR-M03-06 |


<!-- sc:branch SC-M03-001 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống chấp nhận nháp không trống dù chưa đủ điều kiện gửi; Topic có thể 0–3, Lớp có thể trống. Lưu tác giả/mốc và trạng thái ban đầu. | Bộ thay thế độc lập: chỉ tiêu đề; hoặc chỉ nội dung; hoặc chỉ poll hợp lệ; hoặc chỉ PDF hợp lệ. Không có poll sai cấu hình trong lớp này. | END:SUCCESS | FR-M03-01.01, FR-M03-01.08, FR-M03-01.09, FR-M03-01.12, FR-M03-01.13, BR-M03-41, FR-M05-01.10 |


<!-- sc:branch SC-M03-001 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-002 | Lan mở lại Nháp P301 của mình. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; Nháp tạo07/11 09:00; cập nhật cũ07/11 10:00 | E5.2 | FR-M03-01.01, BR-M03-47 |
| E5.2 | SYSTEM | Hệ thống trả bản nháp hiện có với các thành phần để tiếp tục soạn. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; không coi là bài đã gửi, không tạo lịch sử sửa bài đã gửi | E5.3 | FR-M03-01.01, FR-M03-01.02, BR-M03-47 |
| E5.3 | ACT-002 | Lan sửa phần chữ hợp lệ và chọn Lưu nháp. | body=Cách giải đã bổ sung; Topic/Lớp hợp lệ; hiện08/11 10:00 | E5.4 | FR-M03-01.01 |
| E5.4 | SYSTEM | Hệ thống kiểm điều kiện nháp và giới hạn, lưu thay đổi với thời điểm cập nhật mới, giữ tác giả và thời điểm tạo ban đầu; trả bản nháp đã cập nhật, không gửi/quét công bố. | P301 Nháp; tạo07/11 09:00 giữ nguyên, cập nhật08/11 10:00 | END:SUCCESS | FR-M03-01.01, FR-M03-01.08, FR-M03-01.13, FR-M03-01.14, FR-M03-01.15, BR-M03-41, BR-M03-42, BR-M03-47 |


<!-- sc:branch SC-M03-001 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-002 | Lan nhập chuỗi vượt giới hạn. | title="A"×151 hoặc body=6001 từ tách bằng khoảng trắng | E6.2 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |
| E6.2 | SYSTEM | Hệ thống cảnh báo ngay kèm 151/150 hoặc 6001/6000; chưa xóa bản soạn. | Dữ liệu vượt giới hạn vẫn đang soạn | E6.3 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |
| E6.3 | ACT-002 | Lan thử lưu khi vẫn vượt giới hạn. | Giữ đúng chuỗi vượt giới hạn | E6.4 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |
| E6.4 | SYSTEM | Hệ thống từ chối lưu, giữ nguyên nội dung đang soạn để sửa. | Không tạo nháp thành công từ lần lỗi | E6.5 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |
| E6.5 | ACT-002 | Lan rút gọn về dữ liệu hợp lệ và chọn Lưu nháp. | title="A"×150; body=6000 từ; Lớp=10; các trường còn lại hợp lệ | M6 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |


<!-- sc:branch SC-M03-001 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | ACT-002 | Lan nhập phần chữ hợp lệ và chọn thêm ảnh/tài liệu. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; hinh.png PNG 5 MB, de.pdf PDF 20 MB | E7.2 | FR-M03-02.01, BR-M03-07, BR-M03-08 |
| E7.2 | SYSTEM | Hệ thống kiểm tác giả, định dạng/dung lượng và hạn mức độc lập; đặt tệp dưới nội dung, không inline, không quét mã độc tài liệu ở MS1. | 1/10 ảnh; 1/3 tài liệu; PNG/JPEG/WebP ≤5 MB; PDF/DOCX/XLSX/PPTX ≤20 MB | E7.3 | FR-M03-02.01, FR-M03-02.02, FR-M03-02.03, FR-M03-02.04, FR-M03-02.05, FR-M03-02.06, FR-M03-02.07, FR-M03-02.08, FR-M03-02.09, FR-M03-02.10, FR-M03-02.11, BR-M03-04, BR-M03-07, BR-M03-08 |
| E7.3 | ACT-002 | Lan bỏ de.pdf và chọn Lưu nháp. | Tệp còn [hinh.png]; văn bản giữ bộ hợp lệ | E7.4 | FR-M03-02.01 |
| E7.4 | SYSTEM | Hệ thống cập nhật phần tệp rồi kiểm nháp hợp lệ, lưu nháp và trả kết quả. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; P301 Nháp/Bình thường/Không khóa, tệp=[hinh.png] | END:SUCCESS | FR-M03-02.01, FR-M03-02.02, FR-M03-02.03, FR-M03-02.04, FR-M03-02.05, FR-M03-02.06, FR-M03-02.07, FR-M03-02.08, FR-M03-02.09, FR-M03-02.10, FR-M03-02.11, BR-M03-04, BR-M03-07, BR-M03-08, FR-M03-01.01, FR-M03-01.08, FR-M03-01.09, FR-M03-01.12, FR-M03-01.13 |


<!-- sc:branch SC-M03-001 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | ACT-002 | Lan soạn phần chữ hợp lệ và yêu cầu thêm tệp. | hinh.gif 1 MB | E8.2 | FR-M03-02.04 |
| E8.2 | SYSTEM | Hệ thống từ chối tệp thêm vi phạm; tác giả có thể tiếp tục bài không có tệp mới này, vì tệp là tùy chọn. | hinh.gif 1 MB; không coi tệp mới là đã đính kèm | E8.3 | FR-M03-02.04, BR-M03-02, BR-M03-07, BR-M03-08 |
| E8.3 | ACT-002 | Lan tiếp tục với phần chữ hợp lệ, không thêm tệp bị từ chối và chọn Lưu nháp. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; không có tệp vi phạm | M6 | FR-M03-01.01, FR-M03-02.01 |


<!-- sc:branch SC-M03-001 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | ACT-002 | Lan soạn phần chữ hợp lệ và yêu cầu thêm tệp. | hinh.png 6 MB | E9.2 | FR-M03-02.05 |
| E9.2 | SYSTEM | Hệ thống từ chối tệp thêm vi phạm; tác giả có thể tiếp tục bài không có tệp mới này, vì tệp là tùy chọn. | hinh.png 6 MB; không coi tệp mới là đã đính kèm | E9.3 | FR-M03-02.05, BR-M03-02, BR-M03-07, BR-M03-08 |
| E9.3 | ACT-002 | Lan tiếp tục với phần chữ hợp lệ, không thêm tệp bị từ chối và chọn Lưu nháp. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; không có tệp vi phạm | M6 | FR-M03-01.01, FR-M03-02.01 |


<!-- sc:branch SC-M03-001 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | ACT-002 | Lan soạn phần chữ hợp lệ và yêu cầu thêm tệp. | Đã có 10 ảnh hợp lệ; thêm a11.png | E10.2 | FR-M03-02.06 |
| E10.2 | SYSTEM | Hệ thống từ chối tệp thêm vi phạm; tác giả có thể tiếp tục bài không có tệp mới này, vì tệp là tùy chọn. | Đã có 10 ảnh hợp lệ; thêm a11.png; không coi tệp mới là đã đính kèm | E10.3 | FR-M03-02.06, BR-M03-02, BR-M03-07, BR-M03-08 |
| E10.3 | ACT-002 | Lan tiếp tục với phần chữ hợp lệ, không thêm tệp bị từ chối và chọn Lưu nháp. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; không có tệp vi phạm | M6 | FR-M03-01.01, FR-M03-02.01 |


<!-- sc:branch SC-M03-001 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-002 | Lan soạn phần chữ hợp lệ và yêu cầu thêm tệp. | de.zip 1 MB | E11.2 | FR-M03-02.07 |
| E11.2 | SYSTEM | Hệ thống từ chối tệp thêm vi phạm; tác giả có thể tiếp tục bài không có tệp mới này, vì tệp là tùy chọn. | de.zip 1 MB; không coi tệp mới là đã đính kèm | E11.3 | FR-M03-02.07, BR-M03-02, BR-M03-07, BR-M03-08 |
| E11.3 | ACT-002 | Lan tiếp tục với phần chữ hợp lệ, không thêm tệp bị từ chối và chọn Lưu nháp. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; không có tệp vi phạm | M6 | FR-M03-01.01, FR-M03-02.01 |


<!-- sc:branch SC-M03-001 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | ACT-002 | Lan soạn phần chữ hợp lệ và yêu cầu thêm tệp. | de.pdf 21 MB | E12.2 | FR-M03-02.08 |
| E12.2 | SYSTEM | Hệ thống từ chối tệp thêm vi phạm; tác giả có thể tiếp tục bài không có tệp mới này, vì tệp là tùy chọn. | de.pdf 21 MB; không coi tệp mới là đã đính kèm | E12.3 | FR-M03-02.08, BR-M03-02, BR-M03-07, BR-M03-08 |
| E12.3 | ACT-002 | Lan tiếp tục với phần chữ hợp lệ, không thêm tệp bị từ chối và chọn Lưu nháp. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; không có tệp vi phạm | M6 | FR-M03-01.01, FR-M03-02.01 |


<!-- sc:branch SC-M03-001 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | ACT-002 | Lan soạn phần chữ hợp lệ và yêu cầu thêm tệp. | Đã có 3 tài liệu; thêm d4.docx | E13.2 | FR-M03-02.09 |
| E13.2 | SYSTEM | Hệ thống từ chối tệp thêm vi phạm; tác giả có thể tiếp tục bài không có tệp mới này, vì tệp là tùy chọn. | Đã có 3 tài liệu; thêm d4.docx; không coi tệp mới là đã đính kèm | E13.3 | FR-M03-02.09, BR-M03-02, BR-M03-07, BR-M03-08 |
| E13.3 | ACT-002 | Lan tiếp tục với phần chữ hợp lệ, không thêm tệp bị từ chối và chọn Lưu nháp. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; không có tệp vi phạm | M6 | FR-M03-01.01, FR-M03-02.01 |


<!-- sc:branch SC-M03-001 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | SYSTEM | Hệ thống từ chối thay tệp người khác; không dùng quyền Mod/Admin để sửa tệp bài của Lan. | U-MINH thao tác P301 của U-LAN | END:REJECTED | FR-M03-02.11 |


<!-- sc:branch SC-M03-001 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | ACT-002 | Lan thêm poll vào bài đang soạn chưa gửi. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; chưa có poll | E15.2 | FR-M03-03.01 |
| E15.2 | SYSTEM | Hệ thống khởi tạo cấu hình mặc định chọn nhiều và tắt hiện kết quả trước vote; chỉ tác giả đặt lựa chọn. | Poll chưa hoàn tất; cần 2–10 lựa chọn và hạn | E15.3 | FR-M03-03.02, FR-M03-03.05, FR-M03-03.06, BR-M03-10, BR-M03-11 |
| E15.3 | ACT-002 | Lan nhập ba lựa chọn A/B/C, đặt hạn kết thúc rồi yêu cầu lưu nháp. | Q301: A="Phương pháp thế", B="Phân tích nhân tử", C="Dùng công thức"; chọn nhiều; ẩn kết quả trước vote; hạn 09/11/2026 10:00 +07; hiện 08/11/2026 10:00 +07 | E15.4 | FR-M03-03.07 |
| E15.4 | SYSTEM | Hệ thống kiểm đúng tác giả, chỉ một poll, 2–10 lựa chọn, hạn không trước hiện tại; lưu poll cùng nháp hợp lệ, trả nháp đã có poll. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; Q301: A="Phương pháp thế", B="Phân tích nhân tử", C="Dùng công thức"; chọn nhiều; ẩn kết quả trước vote; hạn 09/11/2026 10:00 +07; hiện 08/11/2026 10:00 +07; Nháp/Bình thường/Không khóa | END:SUCCESS | FR-M03-03.01, FR-M03-03.02, FR-M03-03.03, FR-M03-03.04, FR-M03-03.05, FR-M03-03.06, FR-M03-03.07, FR-M03-03.08, FR-M03-03.09, FR-M03-03.10, FR-M03-03.11, BR-M03-09, BR-M03-10, BR-M03-11, BR-M03-12, BR-M03-44, FR-M03-01.01, FR-M03-01.08, FR-M03-01.09, FR-M03-01.12 |


<!-- sc:branch SC-M03-001 E16 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E16.1 | ACT-002 | Người thao tác yêu cầu poll với dữ liệu thay thế này. | 1 hoặc 11 lựa chọn | E16.2 | FR-M03-03.03 |
| E16.2 | SYSTEM | Hệ thống từ chối tạo/cấu hình poll vi phạm; yêu cầu này chưa tạo nháp có poll hợp lệ. | 1 hoặc 11 lựa chọn; không cấp quyền hoặc lưu poll sai | END:REJECTED | FR-M03-03.03 |


<!-- sc:branch SC-M03-001 E17 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E17.1 | ACT-002 | Người thao tác yêu cầu poll với dữ liệu thay thế này. | P301 đã có Q301, thêm Q302 | E17.2 | FR-M03-03.04 |
| E17.2 | SYSTEM | Hệ thống từ chối tạo/cấu hình poll vi phạm; yêu cầu này chưa tạo nháp có poll hợp lệ. | P301 đã có Q301, thêm Q302; không cấp quyền hoặc lưu poll sai | END:REJECTED | FR-M03-03.04 |


<!-- sc:branch SC-M03-001 E18 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E18.1 | ACT-002 | Người thao tác yêu cầu poll với dữ liệu thay thế này. | deadline=trống | E18.2 | FR-M03-03.07 |
| E18.2 | SYSTEM | Hệ thống từ chối tạo/cấu hình poll vi phạm; yêu cầu này chưa tạo nháp có poll hợp lệ. | deadline=trống; không cấp quyền hoặc lưu poll sai | END:REJECTED | FR-M03-03.07 |


<!-- sc:branch SC-M03-001 E19 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E19.1 | ACT-002 | Người thao tác yêu cầu poll với dữ liệu thay thế này. | hiện 08/11 10:00; hạn 08/11 09:00 | E19.2 | FR-M03-03.09 |
| E19.2 | SYSTEM | Hệ thống từ chối tạo/cấu hình poll vi phạm; yêu cầu này chưa tạo nháp có poll hợp lệ. | hiện 08/11 10:00; hạn 08/11 09:00; không cấp quyền hoặc lưu poll sai | END:REJECTED | FR-M03-03.09 |


<!-- sc:branch SC-M03-001 E20 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E20.1 | ACT-002 | Người thao tác yêu cầu poll với dữ liệu thay thế này. | Minh tạo poll cho P301 của Lan | E20.2 | FR-M03-03.08 |
| E20.2 | SYSTEM | Hệ thống từ chối tạo/cấu hình poll vi phạm; yêu cầu này chưa tạo nháp có poll hợp lệ. | Minh tạo poll cho P301 của Lan; không cấp quyền hoặc lưu poll sai | END:REJECTED | FR-M03-03.08 |


<!-- sc:branch SC-M03-001 E21 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E21.1 | ACT-002 | Lan đổi poll của bài Nháp sang chọn một, bật hiện kết quả trước vote, thêm lựa chọn D và đổi hạn. | Q301: A="Phương pháp thế", B="Phân tích nhân tử", C="Dùng công thức"; chọn nhiều; ẩn kết quả trước vote; hạn 09/11/2026 10:00 +07; hiện 08/11/2026 10:00 +07; D=Cách khác; hạn mới10/11 10:00 | E21.2 | FR-M03-03.10 |
| E21.2 | SYSTEM | Hệ thống kiểm số lựa chọn/hạn và ghi cấu hình poll trước gửi, trả bản soạn với poll đã cập nhật. | Q301 có A/B/C/D, chọn một, hiện kết quả trước vote=true, hạn10/11 10:00 | E21.3 | FR-M03-03.03, FR-M03-03.05, FR-M03-03.09, FR-M03-03.10, BR-M03-11, BR-M03-44 |
| E21.3 | ACT-002 | Lan chọn Lưu nháp với phần chữ hợp lệ và poll đã sửa. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; Q301 cấu hình mới hợp lệ | M6 | FR-M03-01.01 |


<!-- sc:branch SC-M03-001 E22 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E22.1 | ACT-002 | Lan chọn bỏ Q301 của bài Nháp. | Q301: A="Phương pháp thế", B="Phân tích nhân tử", C="Dùng công thức"; chọn nhiều; ẩn kết quả trước vote; hạn 09/11/2026 10:00 +07; hiện 08/11/2026 10:00 +07 | E22.2 | FR-M03-03.10 |
| E22.2 | SYSTEM | Hệ thống bỏ poll khỏi bản đang soạn và trả phần soạn không còn poll. | P301 còn tiêu đề/nội dung hợp lệ, poll=không | E22.3 | FR-M03-03.10, BR-M03-44 |
| E22.3 | ACT-002 | Lan chọn Lưu nháp không có poll. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; poll=không | M6 | FR-M03-01.01 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-001 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu soạn và lưu bài nháp. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


<!-- sc:end SC-M03-001 -->

<a id="sc-m03-004"></a>

<!-- sc:scenario SC-M03-004 -->

### SC-M03-004

#### 1. Tên kịch bản chuẩn

Gửi hoặc gửi lại bài để đăng theo chính sách — BF-M03-004. UC owner: [UC-M03-004](../../us/US-M03.md#uc-m03-004). Trigger: Lan chọn Gửi bài nháp P301.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Có phiên; có bản bài của tác giả, Topic/Tag hợp lệ theo M05. Kiểm chủ, cảnh cáo, Nháp/Bị từ chối và điều kiện nội dung khi gửi. Đường chuẩn: bài Nháp ngoài nhóm, tác giả USER, hai cờ AI tổng/Moderation bật.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-004 -->

| result | condition |
|---|---|
| SUCCESS | Yêu cầu gửi được xử lý đúng chính sách và trả trạng thái cụ thể: chuẩn Đã đăng; các nhánh có thể chờ người duyệt hoặc bị từ chối. Không tuyên bố đã được người duyệt chấp thuận khi mới vào hàng chờ. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |
| HANDED_OFF | Tác giả chọn mục tiêu khiếu nại độc lập; M09 nhận đúng bài/kết quả AI; chưa coi đã được chấp nhận hoặc công khai. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-004 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan chọn Gửi bài nháp P301. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; Nháp/Bình thường/Không khóa | M2 | FR-M03-04.01 |
| M2 | SYSTEM | Hệ thống kiểm đúng tác giả, không MEDIUM/HEAVY, trạng thái cho gửi, có tiêu đề và nội dung hoặc poll, đúng giới hạn/Topic/Tag; chuyển Chờ duyệt và gửi yêu cầu quét qua M13. Trong khi quét chỉ tác giả và người duyệt hợp lệ được thấy bài. | Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt; P301 Chờ duyệt, chưa vào hàng Mod chỉ vì đang quét | M3 | FR-M03-04.01, FR-M03-04.02, FR-M03-04.06, FR-M03-04.07, FR-M03-04.08, FR-M03-04.09, FR-M03-04.10, FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43, BR-M03-19, BR-M03-40, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| M3 | ACT-006 | Dịch vụ AI trả bốn điểm vi phạm cho yêu cầu quét. | Điểm bốn nhóm minh họa Quấy rối=0.20, Ngôn từ thù ghét=0.10, Nội dung người lớn=0.05, Bạo lực=0.10; max=0.20 | M4 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| M4 | SYSTEM | Hệ thống lấy điểm cao nhất và nhóm tương ứng, áp ngưỡng mới gửi; score=0.20<0.5 nên chuyển Đã đăng, trả kết quả cho tác giả. Phát sự kiện công bố và thời điểm đăng cho các module nhận. | P301 Đã đăng/Bình thường; đăng lúc 08/11 10:01; không vào hàng Mod | END:SUCCESS | FR-M03-05.01, BR-M03-20 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-004 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Không phải tác giả | E1.1 | FR-M03-04.06 |
| E2 | system | M2 | Sai trạng thái | E2.1 | FR-M03-04.07 |
| E3 | system | M2 | Tác giả MEDIUM/HEAVY | E3.1 | FR-M03-04.10 |
| E4 | system | M2 | Thiếu tiêu đề | E4.1 | FR-M03-04.08 |
| E5 | system | M2 | Không nội dung và không poll | E5.1 | FR-M03-04.09 |
| E6 | system | M2 | Không có Topic hoặc Topic đã bị xóa | E6.1 | FR-M05-01.03, FR-M05-01.09 |
| E7 | system | M2 | Vượt giới hạn khi gửi; tác giả sửa rồi gửi lại | E7.1 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |
| E8 | system | M2 | Một trong hai cờ AI tắt | E8.1 | FR-M03-04.03, FR-M03-05.08, BR-M03-22 |
| E9 | system | M2 | Bài bị từ chối đã được tác giả sửa rồi gửi lại với hai cờ tắt | E9.1 | FR-M03-04.04, FR-M03-04.03, BR-M03-24 |
| E10 | system | M2 | Bài có tiêu đề và poll hợp lệ nhưng nội dung trống; hai cờ tắt | E10.1 | FR-M03-04.03, FR-M03-04.09, BR-M03-40 |
| E11 | system | M3 | AI trả score trong [0.5,0.9), ví dụ 0.5/0.89 | E11.1 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M03-05.02, FR-M03-04.02, BR-M03-20 |
| E12 | system | M3 | AI trả score≥0.9, kể cả đúng 0.9 | E12.1 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M03-05.03, FR-M03-05.12, FR-M03-05.13, BR-M03-20, BR-M03-46 |
| E13 | user-choice | M1 | Tác giả chọn sửa và gửi lại bài đã bị AI tự từ chối | E13.1 | FR-M03-04.04, FR-M03-05.13, BR-M03-24, BR-M03-46 |
| E14 | system | M3 | Lần quét đầu lỗi, lần thử lại thành công sạch | E14.1 | FR-M13-01.04, FR-M13-01.05, FR-M13-02.04, FR-M03-05.01, BR-M03-20 |
| E15 | system | M3 | Lần quét đầu lỗi, lần thử lại cũng lỗi | E15.1 | FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M03-05.04, BR-M03-21 |
| E16 | system | M3 | Lần quét đầu lỗi, lần thử lại thành công với max=0.6 | E16.1 | FR-M13-01.04, FR-M13-01.05, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M03-05.02 |
| E17 | system | M3 | Lần quét đầu lỗi, lần thử lại thành công với max=0.9 | E17.1 | FR-M13-01.04, FR-M13-01.05, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M03-05.03, FR-M03-05.12, BR-M03-46 |
| E18 | system | M2 | Bài nhóm của thành viên khác Owner, điểm sạch và duyệt trước bật | E18.1 | FR-M03-04.05, BR-M03-25, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M11-12.01, FR-M11-12.04 |
| E19 | system | M2 | Bài nhóm của member, điểm sạch và duyệt trước tắt | E19.1 | FR-M03-04.05, BR-M03-25, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M11-12.01, FR-M11-12.05 |
| E20 | system | M2 | Bài nhóm của member, điểm nghi ngờ dù duyệt trước tắt | E20.1 | FR-M03-04.05, BR-M03-25, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M11-12.03 |
| E21 | system | M2 | Owner gửi bài trong nhóm mình, điểm nghi ngờ | E21.1 | FR-M03-04.05, BR-M03-25, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M11-12.16, FR-M11-12.18 |
| E22 | system | M2 | Owner gửi bài nhóm mình với điểm sạch | E22.1 | FR-M03-04.05, BR-M03-25, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M11-12.16, FR-M11-12.19 |
| E23 | system | M2 | Member hoặc Owner bài nhóm có điểm cao | E23.1 | FR-M03-04.05, BR-M03-25, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M11-12.02, FR-M11-12.17 |
| E24 | system | M2 | Bài nhóm khi AI tổng hoặc Moderation tắt | E24.1 | FR-M03-04.05, BR-M03-25, FR-M11-12.14, FR-M11-12.16, FR-M11-12.19 |
| E25 | system | M2 | Người gửi không còn là thành viên nhóm đích | E25.1 | FR-M11-12.11 |
| E26 | system | M3 | Sau khi bị AI tự từ chối, tác giả chọn sửa rồi gửi lại | E26.1 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M03-05.03, FR-M03-05.12, BR-M03-46, FR-M03-04.04, FR-M03-05.13, BR-M03-24 |
| E27 | system | M3 | Sau khi bị AI tự từ chối, tác giả chọn khiếu nại M09 | E27.1 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M03-05.03, FR-M03-05.12, BR-M03-46 |
| E28 | system | M2 | Quét bài nhóm member lỗi cả hai lần | E28.1 | FR-M03-04.05, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M03-05.04, BR-M03-25, FR-M11-12.15 |
| E29 | system | M2 | Quét bài nhóm Owner lỗi cả hai lần | E29.1 | FR-M03-04.05, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M03-05.04, BR-M03-25, FR-M11-12.18 |


<!-- sc:branch SC-M03-004 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối gửi bài với dữ liệu/quyền chưa hợp lệ; không công bố do yêu cầu này. | Minh gửi P301 của Lan | END:REJECTED | FR-M03-04.06 |


<!-- sc:branch SC-M03-004 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối gửi bài với dữ liệu/quyền chưa hợp lệ; không công bố do yêu cầu này. | P301 Đã đăng/Chờ duyệt/Tự ẩn/Đã xóa | END:REJECTED | FR-M03-04.07 |


<!-- sc:branch SC-M03-004 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối gửi bài với dữ liệu/quyền chưa hợp lệ; không công bố do yêu cầu này. | U-LAN MEDIUM hoặc HEAVY | END:REJECTED | FR-M03-04.10 |


<!-- sc:branch SC-M03-004 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối gửi bài với dữ liệu/quyền chưa hợp lệ; không công bố do yêu cầu này. | title="" | END:REJECTED | FR-M03-04.08 |


<!-- sc:branch SC-M03-004 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối gửi bài với dữ liệu/quyền chưa hợp lệ; không công bố do yêu cầu này. | body=""; poll=không; vẫn có de.pdf | END:REJECTED | FR-M03-04.09 |


<!-- sc:branch SC-M03-004 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối gửi bài với dữ liệu/quyền chưa hợp lệ; không công bố do yêu cầu này. | Topic=[] hoặc Toán đã bị xóa khỏi danh mục | END:REJECTED | FR-M05-01.03, FR-M05-01.09 |


<!-- sc:branch SC-M03-004 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối gửi và giữ nguyên nội dung đang soạn; đã cảnh báo số hiện tại khi vượt. | title="A"×151 hoặc body=6001 từ | E7.2 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |
| E7.2 | ACT-002 | Lan rút gọn về giới hạn hợp lệ rồi gửi lại. | title="A"×150; body=6000 từ; Topic Toán | M2 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |


<!-- sc:branch SC-M03-004 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống kiểm điều kiện gửi hợp lệ và áp quyết định miễn quét; trả Đã đăng ngay, không quét. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; giữ Topic, cấu hình poll nếu có; ghi thời điểm đăng | END:SUCCESS | FR-M03-04.03, FR-M03-05.08, BR-M03-22 |


<!-- sc:branch SC-M03-004 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống kiểm điều kiện gửi hợp lệ và áp quyết định miễn quét; trả Đã đăng ngay, không quét. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; giữ Topic, cấu hình poll nếu có; ghi thời điểm đăng | END:SUCCESS | FR-M03-04.04, FR-M03-04.03, BR-M03-24 |


<!-- sc:branch SC-M03-004 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống kiểm điều kiện gửi hợp lệ và áp quyết định miễn quét; trả Đã đăng; poll thay được nội dung nhưng tệp không thay được. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; giữ Topic, cấu hình poll nếu có; ghi thời điểm đăng | END:SUCCESS | FR-M03-04.03, FR-M03-04.09, BR-M03-40 |


<!-- sc:branch SC-M03-004 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-006 | AI trả điểm nghi ngờ. | max=0.5 hoặc 0.89; nhóm Quấy rối | E11.2 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E11.2 | SYSTEM | Hệ thống giữ Chờ duyệt, đưa vào hàng chờ Mod hệ thống, trả tác giả kết quả đang chờ duyệt; chưa công khai. | P301 ngoài nhóm; chỉ tác giả/người duyệt hợp lệ thấy | END:SUCCESS | FR-M03-05.02, FR-M03-04.02, BR-M03-20 |


<!-- sc:branch SC-M03-004 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | ACT-006 | AI trả điểm cao và nhóm vi phạm. | max=0.90; nhóm Quấy rối | E12.2 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E12.2 | SYSTEM | Hệ thống chuyển Bị từ chối không qua Mod, hiển thị nhóm vi phạm cho tác giả; không công khai. Tác giả có quyền sửa/gửi lại không giới hạn lần theo đường gửi lại, hoặc khiếu nại M09. | P301 Bị từ chối; nhóm Quấy rối; chưa có khiếu nại | END:REJECTED | FR-M03-05.03, FR-M03-05.12, FR-M03-05.13, BR-M03-20, BR-M03-46 |


<!-- sc:branch SC-M03-004 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | ACT-002 | Lan sửa P301 Bị từ chối thành nội dung hợp lệ rồi chọn Gửi lại. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; tiêu đề/nội dung đã sửa, Topic Toán | M2 | FR-M03-04.04, FR-M03-05.13, BR-M03-24, BR-M03-46 |


<!-- sc:branch SC-M03-004 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | ACT-006 | Dịch vụ AI trả lỗi lần đầu. | Lần 1 lỗi; không có score | E14.2 | FR-M13-01.04 |
| E14.2 | SYSTEM | Hệ thống chờ 2 giây rồi gửi lại đúng một lần qua M13; giữ Chờ duyệt. | Không gửi hai lần thử đồng thời; cùng P301 | E14.3 | FR-M13-01.05 |
| E14.3 | ACT-006 | Dịch vụ AI trả kết quả lần thử lại. | Lần 2 max=0.20 | E14.4 | FR-M13-02.04 |
| E14.4 | SYSTEM | Hệ thống áp điểm sạch, chuyển Đã đăng và trả kết quả công bố cho tác giả. | P301 Đã đăng | END:SUCCESS | FR-M03-05.01, BR-M03-20 |


<!-- sc:branch SC-M03-004 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | ACT-006 | Dịch vụ AI trả lỗi lần đầu. | Lần 1 lỗi; không có score | E15.2 | FR-M13-01.04 |
| E15.2 | SYSTEM | Hệ thống chờ 2 giây rồi gửi lại đúng một lần qua M13; giữ Chờ duyệt. | Không gửi hai lần thử đồng thời; cùng P301 | E15.3 | FR-M13-01.05 |
| E15.3 | ACT-006 | Dịch vụ AI tiếp tục trả lỗi. | Lần 2 lỗi | E15.4 | FR-M13-01.04, FR-M13-01.06 |
| E15.4 | SYSTEM | Hệ thống giữ Chờ duyệt và đưa vào hàng Mod hệ thống, trả kết quả chờ duyệt, không tự đăng. | P301 Chờ duyệt | END:SUCCESS | FR-M03-05.04, BR-M03-21 |


<!-- sc:branch SC-M03-004 E16 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E16.1 | ACT-006 | AI báo lỗi lần đầu. | Không có kết quả | E16.2 | FR-M13-01.04 |
| E16.2 | SYSTEM | Hệ thống chờ2 giây rồi thử lại đúng một lần, giữ Chờ duyệt. | Không thử đồng thời | E16.3 | FR-M13-01.05 |
| E16.3 | ACT-006 | AI trả điểm ở lần thứ2. | max=0.6 | E16.4 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E16.4 | SYSTEM | Hệ thống áp classifier mới gửi: giữ Chờ duyệt, vào hàng Mod hệ thống, chưa công khai; trả kết quả xử lý cho tác giả. | P301 ngoài nhóm; nhóm vi phạm minh họa Quấy rối | END:SUCCESS | FR-M03-05.02 |


<!-- sc:branch SC-M03-004 E17 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E17.1 | ACT-006 | AI báo lỗi lần đầu. | Không có kết quả | E17.2 | FR-M13-01.04 |
| E17.2 | SYSTEM | Hệ thống chờ2 giây rồi thử lại đúng một lần, giữ Chờ duyệt. | Không thử đồng thời | E17.3 | FR-M13-01.05 |
| E17.3 | ACT-006 | AI trả điểm ở lần thứ2. | max=0.9 | E17.4 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E17.4 | SYSTEM | Hệ thống áp classifier mới gửi: chuyển Bị từ chối không qua Mod, hiện nhóm Quấy rối cho tác giả; trả kết quả xử lý cho tác giả. | P301 ngoài nhóm; nhóm vi phạm minh họa Quấy rối | END:REJECTED | FR-M03-05.03, FR-M03-05.12, BR-M03-46 |


<!-- sc:branch SC-M03-004 E18 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E18.1 | SYSTEM | Hệ thống kiểm điều kiện và thành viên nhóm, chuyển qua chính sách bài nhóm; khởi phát quét qua M13, chưa công khai. | G31; Lan là member; max=0.20; Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt | E18.2 | FR-M03-04.05, BR-M03-25, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M11-12.01, FR-M11-12.04 |
| E18.2 | ACT-006 | Dịch vụ AI trả điểm của bài nhóm. | max=0.2 | E18.3 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E18.3 | SYSTEM | Hệ thống áp kết quả cho đúng vai trò/công tắc duyệt trước; giữ Chờ duyệt và đưa hàng duyệt nhóm, không vào hàng Mod hệ thống; trả kết quả cho tác giả. | G31; Lan là member; max=0.20 | END:SUCCESS | FR-M11-12.01, FR-M11-12.04 |


<!-- sc:branch SC-M03-004 E19 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E19.1 | SYSTEM | Hệ thống kiểm điều kiện và thành viên nhóm, chuyển qua chính sách bài nhóm; khởi phát quét qua M13, chưa công khai. | G31; max=0.20; Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt | E19.2 | FR-M03-04.05, BR-M03-25, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M11-12.01, FR-M11-12.05 |
| E19.2 | ACT-006 | Dịch vụ AI trả điểm của bài nhóm. | max=0.2 | E19.3 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E19.3 | SYSTEM | Hệ thống áp kết quả cho đúng vai trò/công tắc duyệt trước; Đã đăng theo quyền nhóm; trả kết quả cho tác giả. | G31; max=0.20 | END:SUCCESS | FR-M11-12.01, FR-M11-12.05 |


<!-- sc:branch SC-M03-004 E20 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E20.1 | SYSTEM | Hệ thống kiểm điều kiện và thành viên nhóm, chuyển qua chính sách bài nhóm; khởi phát quét qua M13, chưa công khai. | G31; max=0.60; Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt | E20.2 | FR-M03-04.05, BR-M03-25, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M11-12.03 |
| E20.2 | ACT-006 | Dịch vụ AI trả điểm của bài nhóm. | max=0.6 | E20.3 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E20.3 | SYSTEM | Hệ thống áp kết quả cho đúng vai trò/công tắc duyệt trước; Chờ duyệt trong hàng nhóm; trả kết quả cho tác giả. | G31; max=0.60 | END:SUCCESS | FR-M11-12.03 |


<!-- sc:branch SC-M03-004 E21 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E21.1 | SYSTEM | Hệ thống kiểm điều kiện và thành viên nhóm, chuyển qua chính sách bài nhóm; khởi phát quét qua M13, chưa công khai. | Lan là Owner G31; max=0.60; Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt | E21.2 | FR-M03-04.05, BR-M03-25, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M11-12.16, FR-M11-12.18 |
| E21.2 | ACT-006 | Dịch vụ AI trả điểm của bài nhóm. | max=0.6 | E21.3 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E21.3 | SYSTEM | Hệ thống áp kết quả cho đúng vai trò/công tắc duyệt trước; Chờ duyệt trong hàng Mod hệ thống, không hàng nhóm; trả kết quả cho tác giả. | Lan là Owner G31; max=0.60 | END:SUCCESS | FR-M11-12.16, FR-M11-12.18 |


<!-- sc:branch SC-M03-004 E22 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E22.1 | SYSTEM | Hệ thống kiểm điều kiện và thành viên nhóm, chuyển qua chính sách bài nhóm; khởi phát quét qua M13, chưa công khai. | Lan là Owner G31; max=0.20; Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt | E22.2 | FR-M03-04.05, BR-M03-25, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M11-12.16, FR-M11-12.19 |
| E22.2 | ACT-006 | Dịch vụ AI trả điểm của bài nhóm. | max=0.2 | E22.3 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E22.3 | SYSTEM | Hệ thống áp kết quả cho đúng vai trò/công tắc duyệt trước; Đã đăng, bỏ hàng duyệt nhóm bất kể duyệt trước; trả kết quả cho tác giả. | Lan là Owner G31; max=0.20 | END:SUCCESS | FR-M11-12.16, FR-M11-12.19 |


<!-- sc:branch SC-M03-004 E23 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E23.1 | SYSTEM | Hệ thống kiểm điều kiện và thành viên nhóm, chuyển qua chính sách bài nhóm; khởi phát quét qua M13, chưa công khai. | G31; max=0.90; Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt | E23.2 | FR-M03-04.05, BR-M03-25, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M11-12.02, FR-M11-12.17 |
| E23.2 | ACT-006 | Dịch vụ AI trả điểm của bài nhóm. | max=0.9 | E23.3 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E23.3 | SYSTEM | Hệ thống áp kết quả cho đúng vai trò/công tắc duyệt trước; Bị từ chối, trả nhóm vi phạm; không công khai; trả kết quả cho tác giả. | G31; max=0.90 | END:REJECTED | FR-M11-12.02, FR-M11-12.17 |


<!-- sc:branch SC-M03-004 E24 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E24.1 | SYSTEM | Hệ thống kiểm điều kiện gửi và áp cổng nhóm theo M11; duyệt trước bật thì Chờ duyệt hàng nhóm, tắt thì Đã đăng; Owner thì Đã đăng; trả trạng thái/cổng nhận cho tác giả. | Lan member G31; không gọi AI | END:SUCCESS | FR-M03-04.05, BR-M03-25, FR-M11-12.14, FR-M11-12.16, FR-M11-12.19 |


<!-- sc:branch SC-M03-004 E25 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E25.1 | SYSTEM | Hệ thống từ chối gửi bài vào nhóm; không dùng quyền bài ngoài nhóm để vượt cổng nhóm. | Lan không là thành viên G31 | END:REJECTED | FR-M11-12.11 |


<!-- sc:branch SC-M03-004 E26 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E26.1 | ACT-006 | AI trả điểm cao cho bài mới gửi. | max=0.90, nhóm Quấy rối | E26.2 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E26.2 | SYSTEM | Hệ thống tự từ chối và hiển thị nhóm vi phạm cho tác giả. | P301 Bị từ chối | E26.3 | FR-M03-05.03, FR-M03-05.12, BR-M03-46 |
| E26.3 | ACT-002 | Lan sửa nội dung vi phạm về nội dung hợp lệ rồi gửi lại. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; P301 Bị từ chối; cùng bài, không tạo bản sao mới | M2 | FR-M03-04.04, FR-M03-05.13, BR-M03-24, BR-M03-46 |


<!-- sc:branch SC-M03-004 E27 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E27.1 | ACT-006 | AI trả điểm cao cho bài mới gửi. | max=0.90, nhóm Quấy rối | E27.2 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E27.2 | SYSTEM | Hệ thống tự từ chối và hiển thị nhóm vi phạm cho tác giả. | P301 Bị từ chối | E27.3 | FR-M03-05.03, FR-M03-05.12, BR-M03-46 |
| E27.3 | ACT-002 | Lan chọn phản đối kết quả qua Khiếu nại. | Đối tượng P301 bị AI tự từ chối | E27.4 | BR-M03-46 |
| E27.4 | SYSTEM | Hệ thống chuyển đúng ngữ cảnh bài và kết quả tự từ chối sang chức năng khiếu nại M09; chưa có kết luận và chưa công bố bài. | M09 nhận P301 của Lan; giữ Bị từ chối | END:HANDED_OFF | BR-M03-46 |


<!-- sc:branch SC-M03-004 E28 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E28.1 | SYSTEM | Hệ thống kiểm điều kiện gửi nhóm, khởi phát quét qua M13, chưa công khai. | G31; Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt | E28.2 | FR-M03-04.05, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E28.2 | ACT-006 | AI trả lỗi lần đầu. | Không có score | E28.3 | FR-M13-01.04 |
| E28.3 | SYSTEM | Hệ thống chờ 2 giây rồi thử lại đúng một lần. | Không thử đồng thời | E28.4 | FR-M13-01.05 |
| E28.4 | ACT-006 | AI tiếp tục lỗi lần hai. | Lần cuối thất bại | E28.5 | FR-M13-01.06 |
| E28.5 | SYSTEM | Hệ thống giữ Chờ duyệt, đưa bài vào hàng nhóm dù duyệt trước tắt và trả trạng thái đang chờ. | P301 Chờ duyệt, chưa công khai | END:SUCCESS | FR-M03-05.04, BR-M03-25, FR-M11-12.15 |


<!-- sc:branch SC-M03-004 E29 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E29.1 | SYSTEM | Hệ thống kiểm điều kiện gửi nhóm, khởi phát quét qua M13, chưa công khai. | G31; Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt | E29.2 | FR-M03-04.05, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E29.2 | ACT-006 | AI trả lỗi lần đầu. | Không có score | E29.3 | FR-M13-01.04 |
| E29.3 | SYSTEM | Hệ thống chờ 2 giây rồi thử lại đúng một lần. | Không thử đồng thời | E29.4 | FR-M13-01.05 |
| E29.4 | ACT-006 | AI tiếp tục lỗi lần hai. | Lần cuối thất bại | E29.5 | FR-M13-01.06 |
| E29.5 | SYSTEM | Hệ thống giữ Chờ duyệt, đưa bài vào hàng Mod hệ thống và trả trạng thái đang chờ. | P301 Chờ duyệt, chưa công khai | END:SUCCESS | FR-M03-05.04, BR-M03-25, FR-M11-12.18 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-004 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu gửi hoặc gửi lại bài để đăng theo chính sách. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


**V2 — thay toàn bộ M1 đến kết thúc:** ADMIN thực sự gửi/gửi lại bài của mình ngoài nhóm. Actor khởi tạo ACT-003; kết quả END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-004 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-003 | Admin gửi P301 Nháp hoặc bản Bị từ chối đã sửa của chính mình. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; author=U-ADMIN | V2.2 | FR-M03-04.11 |
| V2.2 | SYSTEM | Hệ thống kiểm điều kiện nội dung và sở hữu, chuyển Đã đăng ngay không quét và không hàng duyệt, trả kết quả cho Admin. Miễn quét không áp cho Mod. | P301 ngoài nhóm Đã đăng/Bình thường; hai cờ vẫn bật | END:SUCCESS | FR-M03-04.11, FR-M03-05.15, BR-M03-51 |


**V3 — thay toàn bộ M1 đến kết thúc:** Admin gửi bài nhóm, không phải Owner. Actor khởi tạo ACT-003; kết quả END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-004 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-003 | Admin gửi bài nhóm của chính mình. | P301 thuộc G31; tác giả Admin chỉ là thành viên, không Owner | V3.2 | FR-M03-04.05, BR-M03-51 |
| V3.2 | SYSTEM | Hệ thống không quét; đưa theo cổng duyệt trước: bật thì Chờ duyệt hàng nhóm, tắt thì Đã đăng. Không miễn duyệt nhóm chỉ vì là Admin. Trả trạng thái cụ thể cho tác giả. | G31; snapshot duyệt trước=true; Chờ duyệt hàng nhóm | END:SUCCESS | FR-M11-12.06 |


**V4 — thay toàn bộ M1 đến kết thúc:** Admin gửi bài nhóm, là Owner. Actor khởi tạo ACT-003; kết quả END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-004 V4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V4.1 | ACT-003 | Admin gửi bài nhóm của chính mình. | P301 thuộc G31; tác giả Admin là Owner | V4.2 | FR-M03-04.05, BR-M03-51 |
| V4.2 | SYSTEM | Hệ thống không quét; Owner Admin được Đã đăng ngay, bỏ hàng nhóm. Trả trạng thái cụ thể cho tác giả. | G31; snapshot duyệt trước=true; Đã đăng | END:SUCCESS | FR-M11-12.20 |


<!-- sc:end SC-M03-004 -->

<a id="sc-m03-006"></a>

<!-- sc:scenario SC-M03-006 -->

### SC-M03-006

#### 1. Tên kịch bản chuẩn

Duyệt bài đang nằm trong hàng chờ Mod hệ thống — BF-M03-006. UC owner: [UC-M03-006](../../us/US-M03.md#uc-m03-006). Trigger: Mod Minh yêu cầu hàng chờ duyệt hệ thống.

#### 2. Actor thực hiện

ACT-003 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Actor chính ACT-003 có phiên người duyệt; quyền được kiểm lại. Bài phải thật sự ở hàng Mod hệ thống, không coi bài đang quét hoặc hàng duyệt nhóm là hàng này.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-006 -->

| result | condition |
|---|---|
| SUCCESS | Quyết định hợp lệ được ghi: chấp nhận Đã đăng hoặc từ chối Bị từ chối kèm lý do. Không quyết định cho bài đã đổi trạng thái. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-006 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-003 | Mod Minh yêu cầu hàng chờ duyệt hệ thống. | P301 ngoài nhóm; Chờ duyệt do score=0.6 hoặc lỗi quét; P302 đang quét chưa ở hàng | M2 | FR-M03-06.01 |
| M2 | SYSTEM | Hệ thống kiểm quyền, trả các bài Chờ duyệt đang nằm trong hàng hệ thống cùng dữ liệu cần duyệt. | Danh sách có P301, không có P302 đang quét hoặc bài đang ở hàng nhóm | M3 | FR-M03-06.01, FR-M03-06.06, BR-M03-25 |
| M3 | ACT-003 | Mod chọn chấp nhận P301. | P301; quyết định chấp nhận | M4 | FR-M03-06.02 |
| M4 | SYSTEM | Hệ thống kiểm lại quyền/trạng thái Chờ duyệt, chuyển P301 Đã đăng, trả kết quả duyệt và cung cấp kết quả cho tác giả/sự kiện công bố. | P301 Đã đăng/Bình thường; thời điểm đăng 08/11 10:05 | END:SUCCESS | FR-M03-06.02, FR-M03-06.06, FR-M03-06.07, BR-M03-23 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-006 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M3 | Người duyệt chọn từ chối và nhập lý do | E1.1 | FR-M03-06.03, FR-M03-06.05, FR-M03-06.06, FR-M03-06.07, BR-M03-23 |
| E2 | user-choice | M3 | Người duyệt chọn từ chối nhưng bỏ trống lý do | E2.1 | FR-M03-06.04, FR-M03-06.03, FR-M03-06.05, FR-M03-06.06, FR-M03-06.07, BR-M03-23 |
| E3 | system | M2 | Vai trò Mod/Admin không còn hợp lệ lúc kiểm tra | E3.1 | FR-M03-06.06 |
| E4 | system | M4 | Vai trò Mod/Admin không còn hợp lệ lúc kiểm tra | E4.1 | FR-M03-06.06 |
| E5 | system | M4 | P301 không còn Chờ duyệt khi quyết định được gửi | E5.1 | FR-M03-06.07 |


<!-- sc:branch SC-M03-006 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-003 | Mod chọn từ chối P301 với lý do. | Lý do minh họa: Nội dung cần bổ sung căn cứ | E1.2 | FR-M03-06.03 |
| E1.2 | SYSTEM | Hệ thống kiểm quyền và bài còn Chờ duyệt, lưu lý do, chuyển Bị từ chối; hiển thị lý do cho tác giả và trả kết quả quyết định. | P301 Bị từ chối; lý do đã được lưu | END:SUCCESS | FR-M03-06.03, FR-M03-06.05, FR-M03-06.06, FR-M03-06.07, BR-M03-23 |


<!-- sc:branch SC-M03-006 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-003 | Mod gửi quyết định từ chối chưa có lý do. | reason="" | E2.2 | FR-M03-06.04 |
| E2.2 | SYSTEM | Hệ thống từ chối quyết định, yêu cầu nhập lý do; bài chưa chuyển Bị từ chối. | P301 vẫn Chờ duyệt | E2.3 | FR-M03-06.04 |
| E2.3 | ACT-003 | Mod bổ sung lý do rồi gửi lại quyết định từ chối. | reason=Nội dung cần bổ sung căn cứ | E2.4 | FR-M03-06.03 |
| E2.4 | SYSTEM | Hệ thống kiểm lại quyền và Chờ duyệt, lưu lý do, chuyển Bị từ chối và trả kết quả cho Mod/tác giả. | P301 Bị từ chối | END:SUCCESS | FR-M03-06.03, FR-M03-06.05, FR-M03-06.06, FR-M03-06.07, BR-M03-23 |


<!-- sc:branch SC-M03-006 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối hành vi duyệt. | Không có vai trò duyệt hợp lệ | END:REJECTED | FR-M03-06.06 |


<!-- sc:branch SC-M03-006 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối hành vi duyệt. | Không có vai trò duyệt hợp lệ | END:REJECTED | FR-M03-06.06 |


<!-- sc:branch SC-M03-006 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối quyết định, không ghi đè trạng thái mới. | P301 đã được người khác duyệt hoặc tác giả xóa | END:REJECTED | FR-M03-06.07 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-006 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu duyệt bài đang nằm trong hàng chờ mod hệ thống. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


**V2 — thay toàn bộ M1 đến kết thúc:** User không có vai trò Mod/Admin thử duyệt. Actor khởi tạo ACT-002; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-006 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-002 | User yêu cầu chấp nhận P301 trong hàng duyệt. | actor=U-LAN, role=USER | V2.2 | FR-M03-06.06 |
| V2.2 | SYSTEM | Hệ thống từ chối quyết định do không có quyền, không công bố bài. | P301 vẫn Chờ duyệt | END:REJECTED | FR-M03-06.06 |


<!-- sc:end SC-M03-006 -->

<a id="sc-m03-007"></a>

<!-- sc:scenario SC-M03-007 -->

### SC-M03-007

#### 1. Tên kịch bản chuẩn

Đọc bài viết và kết quả poll được phép — BF-M03-007. UC owner: [UC-M03-007](../../us/US-M03.md#uc-m03-007). Trigger: Minh mở đường dẫn bài P301.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Actor có URL bài, không mặc định bài tồn tại hoặc có quyền xem. Đường chuẩn người có phiên xem bài ngoài nhóm Đã đăng/Bình thường; mức khóa không quyết quyền đọc.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-007 -->

| result | condition |
|---|---|
| SUCCESS | Bài và kết quả được hiển thị đúng quyền, không biến quyền đọc thành quyền tương tác; không đếm lượt xem ở MS1. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-007 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Minh mở đường dẫn bài P301. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; Đã đăng/Bình thường/Khóa toàn bộ; có poll Q301 | M2 | FR-M03-07.01 |
| M2 | SYSTEM | Hệ thống kiểm quyền/trạng thái, hiển thị tiêu đề, nội dung, tác giả, Lớp nếu có, tệp dưới nội dung, Topic/Tag hiện hành và poll. Bài Khóa toàn bộ vẫn đọc được. Nếu poll mở/ẩn kết quả và người xem chưa vote thì không trả kết quả; bài đã sửa có nhãn và nút lịch sử. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; Q301: A="Phương pháp thế", B="Phân tích nhân tử", C="Dùng công thức"; chọn nhiều; ẩn kết quả trước vote; hạn 09/11/2026 10:00 +07; hiện 08/11/2026 10:00 +07; Minh chưa vote; không hiện phần trăm; ảnh ở phần tệp | END:SUCCESS | FR-M03-07.01, FR-M03-07.02, FR-M03-07.03, FR-M03-07.04, FR-M03-07.05, FR-M03-07.07, BR-M03-17, BR-M03-18, BR-M03-39, BR-M03-49, FR-M03-02.03, FR-M03-08.07, FR-M03-12.01, BR-M03-04, FR-M05-04.04, FR-M05-04.05 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-007 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Người khác tác giả không có quyền đọc | E1.1 | FR-M03-07.02, BR-M03-18, BR-M03-49 |
| E2 | system | M2 | Bài thuộc nhóm Private, người xem không là thành viên | E2.1 | FR-M11-03.06 |
| E3 | system | M2 | Bài bị module khác ẩn | E3.1 | FR-M03-07.01, FR-M01-13.01 |
| E4 | system | M2 | Bài đã xóa hẳn mở bằng URL thường, kể cả tác giả | E4.1 | FR-M03-07.05 |
| E5 | system | M2 | Tác giả xem bài của mình chưa bị xóa hẳn | E5.1 | FR-M03-07.03, FR-M03-07.04, FR-M03-06.05, BR-M03-49 |
| E6 | system | M2 | Poll mở, người xem đã vote hoặc bật hiện kết quả trước vote | E6.1 | FR-M03-07.01, FR-M03-07.02, FR-M03-07.03, FR-M03-07.04, FR-M03-07.05, FR-M03-07.07, BR-M03-17, BR-M03-18, BR-M03-39, BR-M03-49, FR-M03-08.07, FR-M03-08.08, FR-M03-08.09, FR-M03-08.10, FR-M03-08.12, BR-M03-15 |
| E7 | system | M2 | Poll đã đóng, bất kể tùy chọn hiện kết quả trước vote | E7.1 | FR-M03-07.01, FR-M03-07.02, FR-M03-07.03, FR-M03-07.04, FR-M03-07.05, FR-M03-07.07, BR-M03-17, BR-M03-18, BR-M03-39, BR-M03-49, FR-M03-08.07, FR-M03-08.08, FR-M03-08.09, FR-M03-08.10, FR-M03-08.12, BR-M03-15 |
| E8 | user-choice | M2 | EP-READ-VOTE: người đang đọc quyết định vote | E8.1 | FR-M03-07.01, FR-M03-07.02, FR-M03-07.03, FR-M03-07.04, FR-M03-07.05, FR-M03-07.07, BR-M03-17, BR-M03-18, BR-M03-39, BR-M03-49, FR-M03-08.07, FR-M03-08.01, FR-M03-08.03, FR-M03-08.09, FR-M03-08.12, FR-M03-08.13, BR-M03-11, BR-M03-15 |
| E9 | user-choice | M2 | EP-READ-HISTORY: người xem chọn lịch sử sau khi bài đã được trả | E9.1 | FR-M03-12.01, FR-M03-12.02, FR-M03-12.03, FR-M03-12.04, BR-M03-27 |


<!-- sc:branch SC-M03-007 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống không cung cấp nội dung qua đường đọc thông thường; với bài Đã xóa hẳn báo bài không tồn tại. Không tự chuyển sang quyền xem lại kiểm duyệt. | P301 Nháp/Bị từ chối/Chờ duyệt/Tự ẩn, hoặc Bị gắn cờ/Bị Mod ẩn; mở URL thường | END:REJECTED | FR-M03-07.02, BR-M03-18, BR-M03-49 |


<!-- sc:branch SC-M03-007 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống không cung cấp nội dung qua đường đọc thông thường; với bài Đã xóa hẳn báo bài không tồn tại. Không tự chuyển sang quyền xem lại kiểm duyệt. | P301 thuộc G31 Private; Minh ngoài G31 | END:REJECTED | FR-M11-03.06 |


<!-- sc:branch SC-M03-007 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống không cung cấp nội dung qua đường đọc thông thường; với bài Đã xóa hẳn báo bài không tồn tại. Không tự chuyển sang quyền xem lại kiểm duyệt. | Tác giả DEACTIVATED/DELETED; hoặc nhóm Bị ẩn; hoặc bài bị gỡ khỏi nhóm | END:REJECTED | FR-M03-07.01, FR-M01-13.01 |


<!-- sc:branch SC-M03-007 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống không cung cấp nội dung qua đường đọc thông thường; với bài Đã xóa hẳn báo bài không tồn tại. Không tự chuyển sang quyền xem lại kiểm duyệt. | P301 Đã xóa, permanent=true | END:REJECTED | FR-M03-07.05 |


<!-- sc:branch SC-M03-007 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống cho chính tác giả xem bài ở trạng thái đăng hiện có; hiển thị nội dung, lý do từ chối khi có và quyền thao tác riêng, không tự làm bài công khai. | U-LAN; P301 Nháp/Bị từ chối/Chờ duyệt/Tự ẩn/Đã xóa còn hạn theo từng snapshot độc lập; permanent=false | END:SUCCESS | FR-M03-07.03, FR-M03-07.04, FR-M03-06.05, BR-M03-49 |


<!-- sc:branch SC-M03-007 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống trả bài được phép và kết quả poll theo số lượt chọn/tổng lượt chọn, làm tròn số nguyên; không chia theo số người vote. | A=3, B=2, C=1; tổng=6 → 50%,33%,17%; nếu cùng 1/3 thì 33%×3=99%, không ép về 100% | END:SUCCESS | FR-M03-07.01, FR-M03-07.02, FR-M03-07.03, FR-M03-07.04, FR-M03-07.05, FR-M03-07.07, BR-M03-17, BR-M03-18, BR-M03-39, BR-M03-49, FR-M03-08.07, FR-M03-08.08, FR-M03-08.09, FR-M03-08.10, FR-M03-08.12, BR-M03-15 |


<!-- sc:branch SC-M03-007 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống trả bài được phép cùng kết quả phần trăm cho mọi người xem bài, không yêu cầu vote trước. | Q301 Đã đóng; 1,1,4 trên tổng6 → 17%,17%,67% (101%); tổng>0 | END:SUCCESS | FR-M03-07.01, FR-M03-07.02, FR-M03-07.03, FR-M03-07.04, FR-M03-07.05, FR-M03-07.07, BR-M03-17, BR-M03-18, BR-M03-39, BR-M03-49, FR-M03-08.07, FR-M03-08.08, FR-M03-08.09, FR-M03-08.10, FR-M03-08.12, BR-M03-15 |


<!-- sc:branch SC-M03-007 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống trả bài đủ quyền và poll đang mở; chưa hiện kết quả khi chưa vote theo cấu hình. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; Q301 mở; mức Không khóa | E8.2 | FR-M03-07.01, FR-M03-07.02, FR-M03-07.03, FR-M03-07.04, FR-M03-07.05, FR-M03-07.07, BR-M03-17, BR-M03-18, BR-M03-39, BR-M03-49, FR-M03-08.07 |
| E8.2 | ACT-002 | Minh chọn A và C rồi gửi phiếu. | Q301: A="Phương pháp thế", B="Phân tích nhân tử", C="Dùng công thức"; chọn nhiều; ẩn kết quả trước vote; hạn 09/11/2026 10:00 +07; hiện 08/11/2026 10:00 +07 | E8.3 | FR-M03-08.01 |
| E8.3 | SYSTEM | Hệ thống kiểm lại phiên/poll/mức khóa và lựa chọn, ghi phiếu, trả bài với kết quả mà người đã vote được xem. | Phiếu Minh=[A,C]; kết quả mẫu A3 B2 C1 →50/33/17%; không rời ngữ cảnh đọc | END:SUCCESS | FR-M03-08.01, FR-M03-08.03, FR-M03-08.09, FR-M03-08.12, FR-M03-08.13, BR-M03-11, BR-M03-15 |


<!-- sc:branch SC-M03-007 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống trả bài có ít nhất một bản sửa cùng nhãn (đã chỉnh sửa) và nút Xem lịch sử. | Phiên bản trước V1: nội dung "Cách giải thứ nhất", U-LAN sửa 08/11 09:00; V2: "Cách giải thứ hai", U-LAN sửa 08/11 10:00; nội dung hiện hành "Cách giải thứ ba" | E9.2 | FR-M03-12.01 |
| E9.2 | ACT-002 | Minh chọn Xem lịch sử. | P301; không yêu cầu chỉnh sửa lịch sử | E9.3 | FR-M03-12.02 |
| E9.3 | SYSTEM | Hệ thống kiểm lại quyền đọc, trả nội dung các phiên bản trước cùng người sửa/thời điểm trong ngữ cảnh bài. | Phiên bản trước V1: nội dung "Cách giải thứ nhất", U-LAN sửa 08/11 09:00; V2: "Cách giải thứ hai", U-LAN sửa 08/11 10:00; nội dung hiện hành "Cách giải thứ ba" | END:SUCCESS | FR-M03-12.02, FR-M03-12.03, FR-M03-12.04, BR-M03-27 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest có quyền đọc bài công khai; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-007 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest mở P301 công khai. | Đã đăng/Bình thường ngoài nhóm hoặc nhóm Public; không bị ẩn bởi module khác | V1.2 | FR-M03-07.01 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền rồi trả tiêu đề/nội dung/tác giả/Lớp/tệp/poll; poll mở ẩn kết quả và Guest chưa vote thì không trả kết quả, poll đóng tổng>0 thì trả phần trăm. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; Q301: A="Phương pháp thế", B="Phân tích nhân tử", C="Dùng công thức"; chọn nhiều; ẩn kết quả trước vote; hạn 09/11/2026 10:00 +07; hiện 08/11/2026 10:00 +07 | END:SUCCESS | FR-M03-07.01, FR-M03-07.02, FR-M03-07.03, FR-M03-07.04, FR-M03-07.05, FR-M03-07.07, BR-M03-17, BR-M03-18, BR-M03-39, BR-M03-49, FR-M03-08.07, FR-M03-08.08, FR-M03-08.09, FR-M03-08.10, FR-M03-08.12, BR-M03-15 |


**V2 — thay toàn bộ M1 đến kết thúc:** Guest không có quyền đọc bài do Private/trạng thái; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-007 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-001 | Guest yêu cầu đọc bài hoặc lịch sử P301. | G31 Private, Guest không là thành viên; hoặc bài không công khai | V2.2 | FR-M03-07.01, FR-M03-07.02, FR-M03-12.04 |
| V2.2 | SYSTEM | Hệ thống không cung cấp nội dung bài/lịch sử; không để quyền đọc công khai vượt quyền nhóm/trạng thái. | Không có dữ liệu riêng tư trả cho Guest | END:REJECTED | FR-M03-07.01, FR-M03-07.02, FR-M03-07.05, FR-M03-12.04 |


<!-- sc:end SC-M03-007 -->

<a id="sc-m03-008"></a>

<!-- sc:scenario SC-M03-008 -->

### SC-M03-008

#### 1. Tên kịch bản chuẩn

Ghi, đổi hoặc bỏ phiếu poll của mình — BF-M03-008. UC owner: [UC-M03-008](../../us/US-M03.md#uc-m03-008). Trigger: Minh chọn A,C của Q301 và gửi phiếu.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Có quyền xem bài theo M03/M11; kiểm phiên, poll còn mở và Khóa toàn bộ tại lần ghi. Đường chuẩn Minh có phiên; tác giả cũng được vote. Lựa chọn chỉ trong danh sách tác giả tạo.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-008 -->

| result | condition |
|---|---|
| SUCCESS | Phiếu của actor được ghi/thay/xóa theo lựa chọn hợp lệ; kết quả hiển thị đúng cấu hình và trạng thái poll. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-008 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Minh chọn A,C của Q301 và gửi phiếu. | Q301: A="Phương pháp thế", B="Phân tích nhân tử", C="Dùng công thức"; chọn nhiều; ẩn kết quả trước vote; hạn 09/11/2026 10:00 +07; hiện 08/11/2026 10:00 +07; trước đó Minh chưa vote | M2 | FR-M03-08.01, FR-M03-08.03, BR-M03-10, BR-M03-11 |
| M2 | SYSTEM | Hệ thống kiểm quyền và poll mở, bài không Khóa toàn bộ; ghi phiếu [A,C] của Minh và trả kết quả poll cho người đã vote theo tổng lượt chọn. | A3 B2 C1 /6 →50%,33%,17%; không thay phiếu người khác | END:SUCCESS | FR-M03-08.01, FR-M03-08.03, FR-M03-08.09, FR-M03-08.11, FR-M03-08.12, FR-M03-08.13, BR-M03-15, BR-M03-45 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-008 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Poll đã đóng, gồm thời điểm đúng hạn | E1.1 | FR-M03-08.06, BR-M03-13 |
| E2 | system | M2 | Bài Khóa toàn bộ | E2.1 | FR-M03-08.13 |
| E3 | user-choice | M1 | Người đã vote chọn đổi phiếu khi poll còn mở | E3.1 | FR-M03-08.04, FR-M03-08.09, FR-M03-08.12, BR-M03-16 |
| E4 | user-choice | M1 | Người đã vote muốn bỏ chọn trong khi poll còn mở | E4.1 | FR-M03-08.05, FR-M03-08.07, BR-M03-16 |
| E5 | system | M2 | Phiếu không đúng chế độ hoặc chứa lựa chọn không có sẵn | E5.1 | FR-M03-08.02, FR-M03-08.03, BR-M03-10, BR-M03-11 |
| E6 | system | M2 | Tác giả bình chọn poll của chính bài mình | E6.1 | FR-M03-08.01, FR-M03-08.11, BR-M03-45 |


<!-- sc:branch SC-M03-008 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối thao tác, không đổi phiếu đang có hoặc ghi phiếu mới. | hiện=09/11 10:00=deadline; thao tác vote/đổi/bỏ đều bị từ chối | END:REJECTED | FR-M03-08.06, BR-M03-13 |


<!-- sc:branch SC-M03-008 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối thao tác, không đổi phiếu đang có hoặc ghi phiếu mới. | Q301 mở nhưng bài Khóa toàn bộ; kể cả tác giả vote | END:REJECTED | FR-M03-08.13 |


<!-- sc:branch SC-M03-008 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-002 | Minh đổi phiếu từ A,C thành B. | Q301 mở, Không khóa; phiếu cũ=[A,C], mới=[B] | E3.2 | FR-M03-08.04 |
| E3.2 | SYSTEM | Hệ thống kiểm điều kiện và thay phiếu cũ bằng phiếu mới của Minh, trả kết quả đã cập nhật; không ghi thành phiếu thứ hai. | Chỉ phiếu Minh=[B]; số lượt chọn của A/C giảm, B tăng theo thay thế | END:SUCCESS | FR-M03-08.04, FR-M03-08.09, FR-M03-08.12, BR-M03-16 |


<!-- sc:branch SC-M03-008 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-002 | Minh chọn bỏ phiếu đã có. | Phiếu Minh=[B]; Q301 mở; không Khóa toàn bộ | E4.2 | FR-M03-08.05 |
| E4.2 | SYSTEM | Hệ thống kiểm điều kiện rồi xóa phiếu Minh. Nếu cấu hình ẩn kết quả trước vote đang tắt hiển thị và poll vẫn mở, Minh thành người chưa vote nên không được thấy kết quả. | Phiếu Minh không còn; không làm poll đóng; nếu tổng=0 thì không tự khẳng định phần trăm (NOTE-02) | END:SUCCESS | FR-M03-08.05, FR-M03-08.07, BR-M03-16 |


<!-- sc:branch SC-M03-008 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống không nhận phiếu không đúng ràng buộc; cho chọn lại theo UC008/A3. | Poll chọn một nhưng gửi A,B; hoặc chọn ID ngoài Q301 | E5.2 | FR-M03-08.02, FR-M03-08.03, BR-M03-10, BR-M03-11 |
| E5.2 | ACT-002 | Minh chọn đúng một lựa chọn A có sẵn rồi gửi lại. | Q301 ở snapshot chọn một, còn mở, không Khóa toàn bộ | M2 | FR-M03-08.02, BR-M03-11 |


<!-- sc:branch SC-M03-008 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống áp cùng điều kiện poll/mức khóa, ghi phiếu hợp lệ cho tác giả; không từ chối chỉ vì là chủ bài. | U-LAN chọn [A]; phiếu thuộc Lan; Không khóa, Q301 mở | END:SUCCESS | FR-M03-08.01, FR-M03-08.11, BR-M03-45 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-008 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu ghi, đổi hoặc bỏ phiếu poll của mình. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


<!-- sc:end SC-M03-008 -->

<a id="sc-m03-009"></a>

<!-- sc:scenario SC-M03-009 -->

### SC-M03-009

#### 1. Tên kịch bản chuẩn

Đổi hạn kết thúc của poll đang mở — BF-M03-009. UC owner: [UC-M03-009](../../us/US-M03.md#uc-m03-009). Trigger: Lan gửi hạn kết thúc mới cho Q301.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Có phiên tác giả bài đã gửi có poll; kiểm lại quyền và poll mở. Đổi hạn không cho đổi cấu hình hoặc lựa chọn cũ.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-009 -->

| result | condition |
|---|---|
| SUCCESS | Hạn hợp lệ được cập nhật; không mở lại poll đã đóng. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-009 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan gửi hạn kết thúc mới cho Q301. | Q301: A="Phương pháp thế", B="Phân tích nhân tử", C="Dùng công thức"; chọn nhiều; ẩn kết quả trước vote; hạn 09/11/2026 10:00 +07; hiện 08/11/2026 10:00 +07; hạn mới=10/11 10:00 | M2 | FR-M03-09.01 |
| M2 | SYSTEM | Hệ thống kiểm chính tác giả, poll chưa đóng và hạn không trước hiện tại; lưu hạn mới rồi trả cấu hình hiện hành, giữ lựa chọn/phiếu. | Q301 vẫn mở; deadline=10/11 10:00; A/B/C và phiếu không đổi | END:SUCCESS | FR-M03-09.01, FR-M03-09.03, FR-M03-09.04, FR-M03-09.05, BR-M03-12, BR-M03-14 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-009 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Tác giả dời hạn sớm hơn nhưng vẫn sau hiện tại | E1.1 | FR-M03-09.01, BR-M03-14 |
| E2 | system | M2 | Người thao tác không phải tác giả | E2.1 | FR-M03-09.04 |
| E3 | system | M2 | Poll đã đóng | E3.1 | FR-M03-09.03, FR-M03-09.08, BR-M03-13, BR-M03-14, BR-M03-44 |
| E4 | system | M2 | Hạn mới trước hiện tại | E4.1 | FR-M03-09.05 |
| E5 | system | M2 | Hạn mới đúng thời điểm hiện tại | E5.1 | FR-M03-09.01, FR-M03-09.02, FR-M03-10.02, BR-M03-13, BR-M03-14 |


<!-- sc:branch SC-M03-009 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống kiểm điều kiện rồi lưu hạn sớm hơn hợp lệ. | hiện 08/11 10:00; từ 09/11 10:00 về 08/11 18:00; vẫn mở | END:SUCCESS | FR-M03-09.01, BR-M03-14 |


<!-- sc:branch SC-M03-009 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối thay đổi poll của người khác. | Minh thao tác Q301 của Lan | END:REJECTED | FR-M03-09.04 |


<!-- sc:branch SC-M03-009 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối đổi hạn/mở lại/đóng lại/thêm lựa chọn; không làm poll mở lại. | Q301 Đã đóng | END:REJECTED | FR-M03-09.03, FR-M03-09.08, BR-M03-13, BR-M03-14, BR-M03-44 |


<!-- sc:branch SC-M03-009 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối lưu hạn mới, giữ hạn hiện hành. | hiện 08/11 10:00; hạn mới 08/11 09:00 | END:REJECTED | FR-M03-09.05 |


<!-- sc:branch SC-M03-009 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống nhận hạn bằng hiện tại là kết thúc ngay, chuyển poll Đã đóng, gửi sự kiện kết thúc và trả kết quả. | hiện=deadline=08/11 10:00; từ lúc này không nhận/đổi/bỏ phiếu | END:SUCCESS | FR-M03-09.01, FR-M03-09.02, FR-M03-10.02, BR-M03-13, BR-M03-14 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-009 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu đổi hạn kết thúc của poll đang mở. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


<!-- sc:end SC-M03-009 -->

<a id="sc-m03-011"></a>

<!-- sc:scenario SC-M03-011 -->

### SC-M03-011

#### 1. Tên kịch bản chuẩn

Sửa và lưu phiên bản bài đã gửi của mình — BF-M03-011. UC owner: [UC-M03-011](../../us/US-M03.md#uc-m03-011). Trigger: Lan mở sửa bài P301 đã gửi của mình.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Có phiên được M01 cho phép; kiểm tác giả và trạng thái tại M2/M4. Đường chuẩn bài Đã đăng/Bình thường, hai cờ bật, tác giả USER; được sửa dù đang bị khóa. Topic/Tag theo M05. Sửa Nháp thuộc hành trình SC001.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-011 -->

| result | condition |
|---|---|
| SUCCESS | Bản sửa hợp lệ và phiên bản trước được ghi, actor nhận kết quả; không bảo đảm luôn công khai vì quét lại có thể gắn cờ hoặc bài còn chịu ràng buộc khác. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-011 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan mở sửa bài P301 đã gửi của mình. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; Đã đăng/Bình thường/Khóa bình luận do Mod | M2 | FR-M03-11.01 |
| M2 | SYSTEM | Hệ thống kiểm chủ/trạng thái, trả nội dung để sửa tiêu đề, thân bài, Lớp và tệp. Có cảnh báo ngay kèm số hiện tại nếu vượt 150 ký tự/6000 từ; không cho sửa poll đã gửi ngoài các thao tác UC009. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; phiên bản đang thấy V1; Lớp=10 | M3 | FR-M03-11.01, FR-M03-11.04, FR-M03-11.07, FR-M03-01.16, FR-M03-03.11, BR-M03-47 |
| M3 | ACT-002 | Lan sửa nội dung và Lớp rồi gửi lưu. | P301 body mới="Cách giải thứ hai"; Lớp=11; Topic Toán giữ hợp lệ | M4 | FR-M03-11.01 |
| M4 | SYSTEM | Hệ thống kiểm lại quyền và dữ liệu, lưu bản trước cùng người sửa/thời điểm vào lịch sử, lưu nội dung mới, hiện nhãn lịch sử; áp UC005: gửi quét lại qua M13, giữ nội dung đã sửa ở trạng thái đang hiển thị trong lúc quét. Không mở khóa bài chỉ vì sửa. | V1 nội dung trước sửa, U-LAN, 08/11 10:00; P301 Đã đăng/Bình thường, vẫn Khóa bình luận; Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt | M5 | FR-M03-11.01, FR-M03-11.02, FR-M03-11.03, FR-M03-11.04, FR-M03-11.07, FR-M03-05.05, FR-M03-05.06, FR-M03-12.01, BR-M03-26, BR-M03-27, BR-M03-38, BR-M03-47, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| M5 | ACT-006 | AI trả điểm của bản sửa. | Điểm bốn nhóm minh họa Quấy rối=0.20, Ngôn từ thù ghét=0.10, Nội dung người lớn=0.05, Bạo lực=0.10; max=0.20 | M6 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| M6 | SYSTEM | Hệ thống nhận score sạch, giữ trạng thái đăng/kiểm duyệt/mức khóa hiện có; trả bản sửa và nhãn (đã chỉnh sửa), nút Xem lịch sử; phát sự kiện nội dung thay đổi cho module nhận. | P301 Đã đăng/Bình thường/Khóa bình luận; nội dung mới, lịch sử V1 được giữ | END:SUCCESS | FR-M03-05.10, FR-M03-11.02, FR-M03-12.01, BR-M03-26, BR-M03-27 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-011 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Người sửa khác tác giả | E1.1 | FR-M03-11.04, FR-M03-02.11 |
| E2 | system | M2 | Bài Chờ duyệt/Đã xóa hoặc kiểm duyệt Bị Mod ẩn | E2.1 | FR-M03-11.07, BR-M03-47 |
| E3 | system | M4 | Người sửa khác tác giả | E3.1 | FR-M03-11.04, FR-M03-02.11 |
| E4 | system | M4 | Bài Chờ duyệt/Đã xóa hoặc kiểm duyệt Bị Mod ẩn | E4.1 | FR-M03-11.07, BR-M03-47 |
| E5 | user-choice | M3 | Tác giả nhập vượt giới hạn trong lúc sửa | E5.1 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |
| E6 | system | M4 | Sửa bài Tự ẩn trong lúc ẩn | E6.1 | FR-M03-11.01, FR-M03-11.02, FR-M03-05.14, BR-M03-26, BR-M03-27 |
| E7 | system | M4 | Sửa bài Bị từ chối nhưng chưa gửi lại | E7.1 | FR-M03-11.01, FR-M03-11.02, FR-M03-04.04, BR-M03-24, BR-M03-27, BR-M03-47 |
| E8 | system | M4 | Sửa Đã đăng nhưng một trong hai cờ AI tắt | E8.1 | FR-M03-11.02, FR-M03-05.08, FR-M03-05.09, BR-M03-22, BR-M03-27 |
| E9 | system | M5 | Quét lại trả score≥0.5, kể cả ≥0.9 | E9.1 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M03-05.07, BR-M03-26 |
| E10 | user-choice | M3 | EP-EDIT-ATTACH: tác giả thay tệp khi sửa | E10.1 | FR-M03-02.02, FR-M03-11.01, FR-M03-02.01, FR-M03-02.03, FR-M03-02.04, FR-M03-02.05, FR-M03-02.06, FR-M03-02.07, FR-M03-02.08, FR-M03-02.09, FR-M03-02.10, FR-M03-02.11, BR-M03-04, BR-M03-07, BR-M03-08 |
| E11 | user-choice | M3 | EP-EDIT-ATTACH: Ảnh sai loại | E11.1 | FR-M03-02.04, FR-M03-02.02, FR-M03-11.01 |
| E12 | user-choice | M3 | EP-EDIT-ATTACH: Ảnh quá 5 MB | E12.1 | FR-M03-02.05, FR-M03-02.02, FR-M03-11.01 |
| E13 | user-choice | M3 | EP-EDIT-ATTACH: Ảnh thứ11 | E13.1 | FR-M03-02.06, FR-M03-02.02, FR-M03-11.01 |
| E14 | user-choice | M3 | EP-EDIT-ATTACH: Tài liệu sai loại | E14.1 | FR-M03-02.07, FR-M03-02.02, FR-M03-11.01 |
| E15 | user-choice | M3 | EP-EDIT-ATTACH: Tài liệu quá20 MB | E15.1 | FR-M03-02.08, FR-M03-02.02, FR-M03-11.01 |
| E16 | user-choice | M3 | EP-EDIT-ATTACH: Tài liệu thứ4 | E16.1 | FR-M03-02.09, FR-M03-02.02, FR-M03-11.01 |
| E17 | system | M4 | Bộ Topic sau sửa trống hoặc quá3 | E17.1 | FR-M05-01.07 |
| E18 | system | M5 | Quét lại lỗi lần đầu, lần thử lại sạch | E18.1 | FR-M13-01.04, FR-M13-01.05, FR-M13-02.04, FR-M03-05.10, BR-M03-26 |
| E19 | system | M5 | Quét lại lỗi lần đầu, lần thử lại cũng lỗi | E19.1 | FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M03-05.11, BR-M03-26 |


<!-- sc:branch SC-M03-011 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối sửa tiêu đề/nội dung/Lớp/tệp của người khác; Mod/Admin không có quyền sửa các trường này chỉ vì vai trò. | Minh sửa P301 của Lan | END:REJECTED | FR-M03-11.04, FR-M03-02.11 |


<!-- sc:branch SC-M03-011 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối lưu sửa bài không được sửa. | Không chuyển trạng thái hoặc tạo phiên bản từ lần bị từ chối | END:REJECTED | FR-M03-11.07, BR-M03-47 |


<!-- sc:branch SC-M03-011 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối sửa tiêu đề/nội dung/Lớp/tệp của người khác; Mod/Admin không có quyền sửa các trường này chỉ vì vai trò. | Minh sửa P301 của Lan | END:REJECTED | FR-M03-11.04, FR-M03-02.11 |


<!-- sc:branch SC-M03-011 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối lưu sửa bài không được sửa. | Không chuyển trạng thái hoặc tạo phiên bản từ lần bị từ chối | END:REJECTED | FR-M03-11.07, BR-M03-47 |


<!-- sc:branch SC-M03-011 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-002 | Lan nhập tiêu đề/nội dung quá giới hạn. | title=151 ký tự hoặc body=6001 từ | E5.2 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |
| E5.2 | SYSTEM | Hệ thống cảnh báo ngay kèm 151/150 hoặc 6001/6000. | Chưa xóa bản đang soạn | E5.3 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |
| E5.3 | ACT-002 | Lan thử lưu khi vẫn quá giới hạn. | Giữ nguyên bộ vi phạm | E5.4 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |
| E5.4 | SYSTEM | Hệ thống từ chối lưu, giữ nguyên nội dung để sửa. | Không ghi bản sửa vượt giới hạn | E5.5 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |
| E5.5 | ACT-002 | Lan rút gọn về đúng giới hạn rồi gửi lưu. | title=150; body=6000 từ; Topic Toán, Lớp hợp lệ | M4 | FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-42, BR-M03-43 |


<!-- sc:branch SC-M03-011 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống lưu bản sửa và lịch sử, giữ Tự ẩn, ghi có sửa trong lúc ẩn; không quét tại lúc lưu. Trả bản sửa cho tác giả, chờ tới hành động Hiện lại mới áp quét. | P301 Tự ẩn; dirty_since_hide=true; lịch sử V1/người sửa/thời điểm được ghi; không AI | END:SUCCESS | FR-M03-11.01, FR-M03-11.02, FR-M03-05.14, BR-M03-26, BR-M03-27 |


<!-- sc:branch SC-M03-011 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống lưu bản sửa hợp lệ và phiên bản trước; giữ Bị từ chối, chưa công bố/quét gửi lại. Trả bản sửa để tác giả có thể gửi lại qua SC004. | P301 Bị từ chối; body mới và lịch sử được lưu | END:SUCCESS | FR-M03-11.01, FR-M03-11.02, FR-M03-04.04, BR-M03-24, BR-M03-27, BR-M03-47 |


<!-- sc:branch SC-M03-011 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống kiểm và lưu bản sửa/historic hợp lệ, giữ trạng thái/mức khóa, không gọi quét. Bật lại sau đó không quét bù bản thời gian tắt. | P301 vẫn Đã đăng/Bình thường; V1 trước sửa được ghi, nhãn đã chỉnh sửa | END:SUCCESS | FR-M03-11.02, FR-M03-05.08, FR-M03-05.09, BR-M03-22, BR-M03-27 |


<!-- sc:branch SC-M03-011 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | ACT-006 | AI trả điểm quét lại đáng nghi hoặc cao. | max=0.50 hoặc 0.95 | E9.2 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E9.2 | SYSTEM | Hệ thống giữ trạng thái đăng, chuyển kiểm duyệt Bị gắn cờ, ẩn với người khác tác giả và chuyển Mod xét ở M08; không tự từ chối bài như quét mới. Trả kết quả bản sửa đã lưu nhưng bị gắn cờ. | P301 Đã đăng/Bị gắn cờ/Khóa bình luận; lịch sử còn | END:SUCCESS | FR-M03-05.07, BR-M03-26 |


<!-- sc:branch SC-M03-011 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | ACT-002 | Lan giữ phần chữ hợp lệ, bỏ tệp cũ và thêm tệp mới khi sửa. | Bỏ old.pdf; thêm new.docx 20 MB, new.webp 5 MB; tổng không vượt 3 tài liệu/10 ảnh | E10.2 | FR-M03-02.02, FR-M03-11.01 |
| E10.2 | SYSTEM | Hệ thống kiểm tác giả và cùng hạn mức ảnh/tài liệu độc lập, cập nhật phần tệp dưới nội dung; không đưa ảnh vào thân bài. | new.docx và new.webp hợp lệ; chưa tuyên bố đã lưu phiên bản bài | E10.3 | FR-M03-02.01, FR-M03-02.02, FR-M03-02.03, FR-M03-02.04, FR-M03-02.05, FR-M03-02.06, FR-M03-02.07, FR-M03-02.08, FR-M03-02.09, FR-M03-02.10, FR-M03-02.11, BR-M03-04, BR-M03-07, BR-M03-08 |
| E10.3 | ACT-002 | Lan gửi lưu bản sửa với bộ tệp mới. | Văn bản/Topic/Lớp hợp lệ; tệp hợp lệ | M4 | FR-M03-11.01 |


<!-- sc:branch SC-M03-011 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-002 | Lan sửa bài hợp lệ và yêu cầu thêm tệp. | hinh.gif | E11.2 | FR-M03-02.04 |
| E11.2 | SYSTEM | Hệ thống từ chối tệp thêm vi phạm, không đưa tệp đó vào phần đính kèm. | hinh.gif | E11.3 | FR-M03-02.04 |
| E11.3 | ACT-002 | Lan tiếp tục với các tệp hợp lệ và phần chữ hợp lệ, gửi lưu bản sửa. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; không thêm tệp bị từ chối | M4 | FR-M03-02.02, FR-M03-11.01 |


<!-- sc:branch SC-M03-011 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | ACT-002 | Lan sửa bài hợp lệ và yêu cầu thêm tệp. | hinh.png 6 MB | E12.2 | FR-M03-02.05 |
| E12.2 | SYSTEM | Hệ thống từ chối tệp thêm vi phạm, không đưa tệp đó vào phần đính kèm. | hinh.png 6 MB | E12.3 | FR-M03-02.05 |
| E12.3 | ACT-002 | Lan tiếp tục với các tệp hợp lệ và phần chữ hợp lệ, gửi lưu bản sửa. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; không thêm tệp bị từ chối | M4 | FR-M03-02.02, FR-M03-11.01 |


<!-- sc:branch SC-M03-011 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | ACT-002 | Lan sửa bài hợp lệ và yêu cầu thêm tệp. | 10 ảnh + thêm ảnh11 | E13.2 | FR-M03-02.06 |
| E13.2 | SYSTEM | Hệ thống từ chối tệp thêm vi phạm, không đưa tệp đó vào phần đính kèm. | 10 ảnh + thêm ảnh11 | E13.3 | FR-M03-02.06 |
| E13.3 | ACT-002 | Lan tiếp tục với các tệp hợp lệ và phần chữ hợp lệ, gửi lưu bản sửa. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; không thêm tệp bị từ chối | M4 | FR-M03-02.02, FR-M03-11.01 |


<!-- sc:branch SC-M03-011 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | ACT-002 | Lan sửa bài hợp lệ và yêu cầu thêm tệp. | de.zip | E14.2 | FR-M03-02.07 |
| E14.2 | SYSTEM | Hệ thống từ chối tệp thêm vi phạm, không đưa tệp đó vào phần đính kèm. | de.zip | E14.3 | FR-M03-02.07 |
| E14.3 | ACT-002 | Lan tiếp tục với các tệp hợp lệ và phần chữ hợp lệ, gửi lưu bản sửa. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; không thêm tệp bị từ chối | M4 | FR-M03-02.02, FR-M03-11.01 |


<!-- sc:branch SC-M03-011 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | ACT-002 | Lan sửa bài hợp lệ và yêu cầu thêm tệp. | de.pdf 21 MB | E15.2 | FR-M03-02.08 |
| E15.2 | SYSTEM | Hệ thống từ chối tệp thêm vi phạm, không đưa tệp đó vào phần đính kèm. | de.pdf 21 MB | E15.3 | FR-M03-02.08 |
| E15.3 | ACT-002 | Lan tiếp tục với các tệp hợp lệ và phần chữ hợp lệ, gửi lưu bản sửa. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; không thêm tệp bị từ chối | M4 | FR-M03-02.02, FR-M03-11.01 |


<!-- sc:branch SC-M03-011 E16 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E16.1 | ACT-002 | Lan sửa bài hợp lệ và yêu cầu thêm tệp. | 3 tài liệu + thêm tài liệu4 | E16.2 | FR-M03-02.09 |
| E16.2 | SYSTEM | Hệ thống từ chối tệp thêm vi phạm, không đưa tệp đó vào phần đính kèm. | 3 tài liệu + thêm tài liệu4 | E16.3 | FR-M03-02.09 |
| E16.3 | ACT-002 | Lan tiếp tục với các tệp hợp lệ và phần chữ hợp lệ, gửi lưu bản sửa. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; không thêm tệp bị từ chối | M4 | FR-M03-02.02, FR-M03-11.01 |


<!-- sc:branch SC-M03-011 E17 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E17.1 | SYSTEM | Hệ thống từ chối lưu bộ Topic vi phạm. | Topic=[] hoặc 4 Topic | END:REJECTED | FR-M05-01.07 |


<!-- sc:branch SC-M03-011 E18 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E18.1 | ACT-006 | Dịch vụ AI báo lỗi ở lần quét lại đầu. | Lần1 không có score | E18.2 | FR-M13-01.04 |
| E18.2 | SYSTEM | Hệ thống chờ 2 giây, thử lại đúng một lần, tiếp tục giữ bài với nội dung sửa theo trạng thái đang hiển thị. | Không đổi sang Chờ duyệt chỉ vì lỗi quét lại | E18.3 | FR-M13-01.05 |
| E18.3 | ACT-006 | Dịch vụ AI trả điểm sạch ở lần thử lại. | Lần2 max=0.20 | E18.4 | FR-M13-02.04 |
| E18.4 | SYSTEM | Hệ thống giữ nguyên trạng thái và tiếp tục hiển thị theo quyền; trả kết quả quét lại sạch. | P301 Đã đăng/Bình thường theo snapshot | END:SUCCESS | FR-M03-05.10, BR-M03-26 |


<!-- sc:branch SC-M03-011 E19 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E19.1 | ACT-006 | Dịch vụ AI báo lỗi ở lần quét lại đầu. | Lần1 không có score | E19.2 | FR-M13-01.04 |
| E19.2 | SYSTEM | Hệ thống chờ 2 giây, thử lại đúng một lần, tiếp tục giữ bài với nội dung sửa theo trạng thái đang hiển thị. | Không đổi sang Chờ duyệt chỉ vì lỗi quét lại | E19.3 | FR-M13-01.05 |
| E19.3 | ACT-006 | Dịch vụ AI tiếp tục lỗi. | Lần2 lỗi | E19.4 | FR-M13-01.06 |
| E19.4 | SYSTEM | Hệ thống giữ nguyên trạng thái và tiếp tục hiển thị theo quyền; trả kết quả quét lại thất bại, không tự gắn cờ/chờ duyệt. | P301 Đã đăng/Bình thường theo snapshot | END:SUCCESS | FR-M03-05.11, BR-M03-26 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-011 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu sửa và lưu phiên bản bài đã gửi của mình. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


**V2 — thay toàn bộ M1 đến kết thúc:** ADMIN sửa bài Đã đăng của mình khi hai cờ bật. Actor khởi tạo ACT-003; kết quả END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-011 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-003 | Admin mở sửa bài của chính mình. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; author=U-ADMIN | V2.2 | FR-M03-11.01 |
| V2.2 | SYSTEM | Hệ thống kiểm chủ/trạng thái và trả các trường được sửa. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa | V2.3 | FR-M03-11.01, FR-M03-11.04, FR-M03-11.07, BR-M03-47 |
| V2.3 | ACT-003 | Admin sửa nội dung hợp lệ rồi gửi lưu. | body=Cách giải thứ hai; Topic/Lớp hợp lệ | V2.4 | FR-M03-11.01 |
| V2.4 | SYSTEM | Hệ thống lưu bản trước vào lịch sử và lưu bản mới, hiển thị nhãn lịch sử, giữ trạng thái/khóa, trả kết quả; không gọi quét lại vì tác giả là ADMIN. | P301 Đã đăng/Bình thường; V1 trước sửa và người sửa U-ADMIN/thời điểm được ghi | END:SUCCESS | FR-M03-11.02, FR-M03-12.01, FR-M03-05.15, BR-M03-51 |


<!-- sc:end SC-M03-011 -->

<a id="sc-m03-012"></a>

<!-- sc:scenario SC-M03-012 -->

### SC-M03-012

#### 1. Tên kịch bản chuẩn

Xem các phiên bản lịch sử sửa bài — BF-M03-012. UC owner: [UC-M03-012](../../us/US-M03.md#uc-m03-012). Trigger: Minh chọn Xem lịch sử trên P301.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Bài có ít nhất một bản trong lịch sử; kiểm lại quyền đọc bài ở M2, không dựa chỉ vào URL đã mở trước đó. Không có hành động sửa lịch sử.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-012 -->

| result | condition |
|---|---|
| SUCCESS | Người được phép đọc nhận các phiên bản trước; quyền xem lịch sử không vượt quyền đọc bài. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-012 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Minh chọn Xem lịch sử trên P301. | Phiên bản trước V1: nội dung "Cách giải thứ nhất", U-LAN sửa 08/11 09:00; V2: "Cách giải thứ hai", U-LAN sửa 08/11 10:00; nội dung hiện hành "Cách giải thứ ba" | M2 | FR-M03-12.02 |
| M2 | SYSTEM | Hệ thống kiểm người xem còn quyền đọc, hiển thị các nội dung trước sửa kèm người sửa và thời điểm; giữ bài hiện tại, không tạo phiên bản mới. | Phiên bản trước V1: nội dung "Cách giải thứ nhất", U-LAN sửa 08/11 09:00; V2: "Cách giải thứ hai", U-LAN sửa 08/11 10:00; nội dung hiện hành "Cách giải thứ ba" | END:SUCCESS | FR-M03-12.01, FR-M03-12.02, FR-M03-12.03, FR-M03-12.04, BR-M03-27 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-012 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Người xem không còn quyền xem bài theo trạng thái/nhóm | E1.1 | FR-M03-12.04 |


<!-- sc:branch SC-M03-012 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống không hiển thị lịch sử. | P301 không còn công khai cho Minh hoặc Minh không thuộc Private | END:REJECTED | FR-M03-12.04 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest có quyền đọc bài công khai; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-012 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest chọn Xem lịch sử của P301 công khai. | Đã đăng/Bình thường ngoài nhóm hoặc nhóm Public; không bị ẩn bởi module khác | V1.2 | FR-M03-12.03 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền rồi trả các nội dung phiên bản trước, người sửa và thời điểm, không cho Guest sửa lịch sử. | P301 của U-LAN, ngoài nhóm; tiêu đề="Giải phương trình bậc hai"; nội dung chữ="x^2 + 2x + 1 = 0" (7 từ); Lớp bài=10, Lớp hồ sơ=12; Topic Toán trong danh mục; Tag #daiso; không có Accepted Answer/ảnh bìa; Phiên bản trước V1: nội dung "Cách giải thứ nhất", U-LAN sửa 08/11 09:00; V2: "Cách giải thứ hai", U-LAN sửa 08/11 10:00; nội dung hiện hành "Cách giải thứ ba" | END:SUCCESS | FR-M03-12.02, FR-M03-12.03, FR-M03-12.04, BR-M03-27 |


**V2 — thay toàn bộ M1 đến kết thúc:** Guest không có quyền đọc bài do Private/trạng thái; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-012 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-001 | Guest yêu cầu đọc bài hoặc lịch sử P301. | G31 Private, Guest không là thành viên; hoặc bài không công khai | V2.2 | FR-M03-07.01, FR-M03-07.02, FR-M03-12.04 |
| V2.2 | SYSTEM | Hệ thống không cung cấp nội dung bài/lịch sử; không để quyền đọc công khai vượt quyền nhóm/trạng thái. | Không có dữ liệu riêng tư trả cho Guest | END:REJECTED | FR-M03-07.01, FR-M03-07.02, FR-M03-07.05, FR-M03-12.04 |


<!-- sc:end SC-M03-012 -->

<a id="sc-m03-013"></a>

<!-- sc:scenario SC-M03-013 -->

### SC-M03-013

#### 1. Tên kịch bản chuẩn

Tự ẩn bài đang đăng của mình — BF-M03-013. UC owner: [UC-M03-013](../../us/US-M03.md#uc-m03-013). Trigger: Lan yêu cầu Tự ẩn P301.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Có phiên; kiểm tác giả và trạng thái Đã đăng trong phản hồi. Không phải quyền Mod gỡ bài người khác.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-013 -->

| result | condition |
|---|---|
| SUCCESS | Bài thành Tự ẩn, không còn công khai qua đường thường; kiểm duyệt/khóa không tự bị gỡ. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-013 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan yêu cầu Tự ẩn P301. | P301 Đã đăng/Bình thường/Khóa bình luận do Mod | M2 | FR-M03-13.01 |
| M2 | SYSTEM | Hệ thống kiểm tác giả và Đã đăng, chuyển trạng thái đăng sang Tự ẩn; giữ trạng thái kiểm duyệt và mức khóa/người khóa, trả kết quả đã ẩn. | P301 Tự ẩn/Bình thường/Khóa bình luận; người khác không đọc qua URL thường | END:SUCCESS | FR-M03-13.01, FR-M03-13.03, FR-M03-13.04, BR-M03-29 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-013 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Không phải tác giả | E1.1 | FR-M03-13.03 |
| E2 | system | M2 | Bài không Đã đăng | E2.1 | FR-M03-13.04 |


<!-- sc:branch SC-M03-013 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối tự ẩn bài với yêu cầu này. | Minh yêu cầu ẩn P301 của Lan | END:REJECTED | FR-M03-13.03 |


<!-- sc:branch SC-M03-013 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối tự ẩn bài với yêu cầu này. | Nháp/Chờ duyệt/Bị từ chối/Tự ẩn/Đã xóa | END:REJECTED | FR-M03-13.04 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-013 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu tự ẩn bài đang đăng của mình. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


<!-- sc:end SC-M03-013 -->

<a id="sc-m03-014"></a>

<!-- sc:scenario SC-M03-014 -->

### SC-M03-014

#### 1. Tên kịch bản chuẩn

Đặt mức khóa cho bài viết — BF-M03-014. UC owner: [UC-M03-014](../../us/US-M03.md#uc-m03-014). Trigger: Lan chọn Khóa bình luận cho P301 của mình.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Có phiên; kiểm vai trò, sở hữu và người khóa hiện hành lúc xử lý. Chuẩn tác giả khóa bình luận bài mình; không tác động trạng thái đăng/kiểm duyệt.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-014 -->

| result | condition |
|---|---|
| SUCCESS | Mức khóa/người khóa được ghi đúng quyền, các hệ quả tương tác được áp; bài không bị ẩn chỉ vì khóa. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-014 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan chọn Khóa bình luận cho P301 của mình. | P301 Đã đăng/Bình thường/Không khóa | M2 | FR-M03-14.01 |
| M2 | SYSTEM | Hệ thống kiểm tác giả và quyền đổi mức, đặt Khóa bình luận, ghi người khóa Lan và trả kết quả. Chặn bình luận mới, tiếp tục hiện bình luận cũ; không ẩn bài. | P301 mức=Khóa bình luận, locker=U-LAN; trạng thái đăng/kiểm duyệt giữ nguyên | END:SUCCESS | FR-M03-14.01, FR-M03-14.04, FR-M03-14.05, BR-M03-17, BR-M03-30, BR-M03-32 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-014 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Người khóa là Mod/Admin và tác giả muốn mở hoặc đổi mức | E1.1 | FR-M03-14.09, BR-M03-32 |
| E2 | system | M2 | Người yêu cầu không là tác giả, Mod hoặc Admin | E2.1 | FR-M03-14.11 |
| E3 | system | M2 | Người không phải Mod/Admin yêu cầu Khóa toàn bộ | E3.1 | FR-M03-14.10 |


<!-- sc:branch SC-M03-014 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối tác giả đổi/mở khóa do Mod/Admin đặt. | locker=U-MOD; actor=Lan tác giả | END:REJECTED | FR-M03-14.09, BR-M03-32 |


<!-- sc:branch SC-M03-014 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối thao tác khóa/mở khóa bình luận của người khác. | actor=Minh thường; author=Lan | END:REJECTED | FR-M03-14.11 |


<!-- sc:branch SC-M03-014 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối đặt Khóa toàn bộ. | actor=Lan tác giả nhưng không Mod/Admin | END:REJECTED | FR-M03-14.10 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-014 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu đặt mức khóa cho bài viết. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


**V2 — thay toàn bộ M1 đến kết thúc:** Mod/Admin đặt Khóa bình luận. Actor khởi tạo ACT-003; kết quả END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-014 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-003 | Mod Minh đặt Khóa bình luận cho P301. | Actor thực sự có vai trò MOD/ADMIN; P301 của Lan | V2.2 | FR-M03-14.02 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền rồi ghi mức khóa và người khóa là Mod/Admin hiện tại, trả kết quả; không ẩn bài. Áp chặn tương tác theo mức, giữ bình luận cũ. | level=Khóa bình luận; locker=U-MOD; Khóa toàn bộ chặn cả đổi/bỏ vote và rút upvote, không chặn bookmark/báo cáo | END:SUCCESS | FR-M03-14.02, FR-M03-14.04, FR-M03-14.05, FR-M03-14.06, FR-M03-14.12, BR-M03-30, BR-M03-31, BR-M03-32 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mod/Admin đặt Khóa toàn bộ. Actor khởi tạo ACT-003; kết quả END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-014 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-003 | Mod Minh đặt Khóa toàn bộ cho P301. | Actor thực sự có vai trò MOD/ADMIN; P301 của Lan | V3.2 | FR-M03-14.03 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền rồi ghi mức khóa và người khóa là Mod/Admin hiện tại, trả kết quả; không ẩn bài. Áp chặn tương tác theo mức, giữ bình luận cũ. | level=Khóa toàn bộ; locker=U-MOD; Khóa toàn bộ chặn cả đổi/bỏ vote và rút upvote, không chặn bookmark/báo cáo | END:SUCCESS | FR-M03-14.03, FR-M03-14.04, FR-M03-14.05, FR-M03-14.06, FR-M03-14.12, BR-M03-30, BR-M03-31, BR-M03-32 |


<!-- sc:end SC-M03-014 -->

<a id="sc-m03-015"></a>

<!-- sc:scenario SC-M03-015 -->

### SC-M03-015

#### 1. Tên kịch bản chuẩn

Xóa mềm bài của mình — BF-M03-015. UC owner: [UC-M03-015](../../us/US-M03.md#uc-m03-015). Trigger: Lan chọn Xóa P301 của mình.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Có phiên; kiểm tác giả và trạng thái chưa Đã xóa. Có thể xóa bài Nháp/Bị từ chối/Đã đăng/Tự ẩn/Chờ duyệt; không phải lệnh Mod gỡ bài.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-015 -->

| result | condition |
|---|---|
| SUCCESS | Bài Đã xóa có mốc và trạng thái trước, không công khai; còn cơ hội khôi phục theo hạn/quyền. Không trừ/xóa dữ liệu vật lý ngoài giao tiếp nguồn. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-015 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan chọn Xóa P301 của mình. | P301 Đã đăng/Bình thường/Khóa bình luận | M2 | FR-M03-15.01 |
| M2 | SYSTEM | Hệ thống kiểm chủ và chưa Đã xóa, ghi thời điểm xóa và trạng thái trước, chuyển Đã xóa; bỏ hiển thị feed/công khai, đưa vào tab Đã xóa của Lan trong hạn. Trả kết quả xóa mềm, không xóa vật lý dữ liệu. | P301 deleted_at=08/11/2026 10:00; prior=Đã đăng; hạn=15/11/2026 10:00; kiểm duyệt/khóa còn giữ | END:SUCCESS | FR-M03-15.01, FR-M03-15.02, FR-M03-15.03, FR-M03-15.04, FR-M03-15.05, FR-M03-16.02, BR-M03-34, BR-M03-35 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-015 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Không phải tác giả | E1.1 | FR-M03-15.04 |
| E2 | system | M2 | Bài đã Đã xóa | E2.1 | FR-M03-15.05 |
| E3 | system | M2 | Bài đang Chờ duyệt và nằm trong hàng Mod hệ thống | E3.1 | FR-M03-15.01, FR-M03-15.02, FR-M03-15.03, FR-M03-15.06, FR-M03-06.07, BR-M03-34 |


<!-- sc:branch SC-M03-015 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối xóa mềm bài người khác, kể cả Mod/Admin; xử lý kiểm duyệt ở M08. | Minh xóa P301 của Lan | END:REJECTED | FR-M03-15.04 |


<!-- sc:branch SC-M03-015 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối xóa lại, không làm mới hạn khôi phục. | P301 đã xóa 07/11 10:00 | END:REJECTED | FR-M03-15.05 |


<!-- sc:branch SC-M03-015 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống xóa mềm, ghi thời điểm/trạng thái trước Chờ duyệt và đưa bài khỏi hàng chờ Mod; không để quyết định duyệt cũ công bố bài. | P301 Đã xóa; prior=Chờ duyệt; không còn trong hàng; các lần duyệt sau bị từ chối vì sai trạng thái | END:SUCCESS | FR-M03-15.01, FR-M03-15.02, FR-M03-15.03, FR-M03-15.06, FR-M03-06.07, BR-M03-34 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-015 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu xóa mềm bài của mình. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


<!-- sc:end SC-M03-015 -->

<a id="sc-m03-016"></a>

<!-- sc:scenario SC-M03-016 -->

### SC-M03-016

#### 1. Tên kịch bản chuẩn

Khôi phục bài đã xóa trong thời hạn — BF-M03-016. UC owner: [UC-M03-016](../../us/US-M03.md#uc-m03-016). Trigger: Lan yêu cầu Khôi phục P301 của mình từ tab Đã xóa.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Có phiên; kiểm tác giả, Đã xóa, mốc thời gian và kiểm duyệt khi xử lý. Không mặc định còn hạn. Chuẩn xóa 01/11 10:00, yêu cầu 08/11 09:59 (+07), chưa đủ 7×24h.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-016 -->

| result | condition |
|---|---|
| SUCCESS | Bài trở về đúng trạng thái trước xóa; riêng trước đó Chờ duyệt thì về Nháp. Không phục hồi sau hạn hoặc tự bỏ khóa/kiểm duyệt. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-016 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan yêu cầu Khôi phục P301 của mình từ tab Đã xóa. | deleted_at=01/11/2026 10:00; prior=Đã đăng; request=08/11 09:59 | M2 | FR-M03-16.01 |
| M2 | SYSTEM | Hệ thống kiểm chủ, trạng thái Đã xóa, chưa hết 7×24h và không Bị Mod ẩn; khôi phục về trạng thái trước xóa, giữ kiểm duyệt/khóa và dữ liệu. Trả bài đã khôi phục; không tự quét lại hoặc gửi lại chỉ do khôi phục. | P301 Đã đăng/Bình thường/Khóa bình luận; cờ permanent=false; không làm mất lịch sử/poll/phiếu | END:SUCCESS | FR-M03-16.01, FR-M03-16.02, FR-M03-16.03, FR-M03-16.04, FR-M03-16.05, BR-M03-35, BR-M03-36, BR-M03-38 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-016 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Hết hạn, kể cả đúng mốc 7×24h | E1.1 | FR-M03-16.03, BR-M03-35, BR-M03-36 |
| E2 | system | M2 | Bị Mod ẩn | E2.1 | FR-M03-16.04, BR-M03-35, BR-M03-36 |
| E3 | system | M2 | Không phải tác giả | E3.1 | FR-M03-16.05, BR-M03-35, BR-M03-36 |
| E4 | system | M2 | Bài không ở trạng thái Đã xóa | E4.1 | FR-M03-16.01 |
| E5 | system | M2 | Trước khi xóa, bài đang Chờ duyệt | E5.1 | FR-M03-16.01, FR-M03-16.06, BR-M03-35 |
| E6 | system | M2 | Trạng thái trước xóa là Nháp/Bị từ chối/Tự ẩn | E6.1 | FR-M03-16.01, BR-M03-35 |


<!-- sc:branch SC-M03-016 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối khôi phục; không bỏ cờ xóa hẳn hoặc gỡ kiểm duyệt. | xóa01/11 10:00; yêu cầu08/11 10:00 hoặc sau; permanent=true | END:REJECTED | FR-M03-16.03, BR-M03-35, BR-M03-36 |


<!-- sc:branch SC-M03-016 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối khôi phục; không bỏ cờ xóa hẳn hoặc gỡ kiểm duyệt. | P301 Đã xóa/Bị Mod ẩn | END:REJECTED | FR-M03-16.04, BR-M03-35, BR-M03-36 |


<!-- sc:branch SC-M03-016 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối khôi phục; không bỏ cờ xóa hẳn hoặc gỡ kiểm duyệt. | Minh khôi phục P301 của Lan | END:REJECTED | FR-M03-16.05, BR-M03-35, BR-M03-36 |


<!-- sc:branch SC-M03-016 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống không thực hiện khôi phục bài chưa ở trạng thái được khôi phục; không ghi đè trạng thái hiện hành. | P301 Nháp/Đã đăng/Tự ẩn hoặc đã khôi phục trước yêu cầu này | END:REJECTED | FR-M03-16.01 |


<!-- sc:branch SC-M03-016 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống kiểm quyền/thời hạn và khôi phục về Nháp, không trở lại hàng duyệt cũ; muốn đăng phải gửi bài theo cổng hiện hành. | prior=Chờ duyệt; P301 sau khôi phục Nháp; không gọi AI chỉ vì khôi phục | END:SUCCESS | FR-M03-16.01, FR-M03-16.06, BR-M03-35 |


<!-- sc:branch SC-M03-016 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống kiểm điều kiện rồi khôi phục đúng trạng thái trước đó, không tự đổi sang Đã đăng; giữ dữ liệu/kiểm duyệt/khóa. | Snapshot thay thế prior=Nháp hoặc Bị từ chối hoặc Tự ẩn; sau=đúng prior | END:SUCCESS | FR-M03-16.01, BR-M03-35 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-016 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu khôi phục bài đã xóa trong thời hạn. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


<!-- sc:end SC-M03-016 -->

<a id="sc-m03-017"></a>

<!-- sc:scenario SC-M03-017 -->

### SC-M03-017

#### 1. Tên kịch bản chuẩn

Hiện lại bài đã tự ẩn — BF-M03-017. UC owner: [UC-M03-017](../../us/US-M03.md#uc-m03-017). Trigger: Lan yêu cầu Hiện lại P301.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Có phiên; kiểm chủ, Tự ẩn, kiểm duyệt và ràng buộc khác khi hiện lại. Chuẩn bài chưa sửa trong lúc ẩn, kiểm duyệt Bình thường.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-017 -->

| result | condition |
|---|---|
| SUCCESS | Trạng thái đăng được hiện lại đúng chính sách; không gỡ Bị Mod ẩn, cờ gắn cờ hoặc quyền nhóm trái nguồn. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-017 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan yêu cầu Hiện lại P301. | P301 Tự ẩn/Bình thường; dirty_since_hide=false | M2 | FR-M03-13.02 |
| M2 | SYSTEM | Hệ thống kiểm tác giả/Tự ẩn và không Bị Mod ẩn, chuyển về Đã đăng; áp UC005: không có bản sửa trong lúc ẩn nên không quét chỉ vì hiện lại. Giữ khóa và trả kết quả theo quyền hiển thị còn lại. | P301 Đã đăng/Bình thường; giữ mức khóa; không bảo đảm công khai nếu tài khoản/nhóm đang bị ẩn | END:SUCCESS | FR-M03-13.02, FR-M03-13.03, FR-M03-13.05, FR-M03-13.06, BR-M03-26, BR-M03-29, BR-M03-33 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-017 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Không phải tác giả | E1.1 | FR-M03-13.03, BR-M03-33 |
| E2 | system | M2 | Bài không Tự ẩn | E2.1 | FR-M03-13.02, BR-M03-33 |
| E3 | system | M2 | Kiểm duyệt Bị Mod ẩn | E3.1 | FR-M03-13.05, BR-M03-33 |
| E4 | system | M2 | Tác giả khác Admin đã sửa lúc ẩn, hai cờ bật | E4.1 | FR-M03-13.02, FR-M03-13.06, FR-M03-05.05, FR-M03-05.06, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, BR-M03-26, FR-M03-05.10 |
| E5 | system | M2 | Bài tự ẩn đã sửa, quét lại cho điểm≥0.5 | E5.1 | FR-M03-13.02, FR-M03-13.06, FR-M03-05.05, FR-M03-05.06, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, BR-M03-26, FR-M03-05.07 |
| E6 | system | M2 | Bài tự ẩn đã sửa nhưng một trong hai cờ AI tắt | E6.1 | FR-M03-13.02, FR-M03-13.06, FR-M03-05.08, FR-M03-05.09, BR-M03-22, BR-M03-26 |
| E7 | system | M2 | Quét lại lỗi lần đầu, lần thử lại sạch | E7.1 | FR-M03-13.02, FR-M03-13.06, FR-M03-05.05, FR-M03-05.06, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, BR-M03-26, FR-M13-01.04, FR-M13-01.05, FR-M03-05.10 |
| E8 | system | M2 | Quét lại lỗi lần đầu, lần thử lại cũng lỗi | E8.1 | FR-M03-13.02, FR-M03-13.06, FR-M03-05.05, FR-M03-05.06, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, BR-M03-26, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06, FR-M03-05.11 |


<!-- sc:branch SC-M03-017 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối hiện lại; Bị Mod ẩn chỉ có đường xử lý/khiếu nại do M08/M09, không tự chuyển công khai. | Minh hiện lại P301 của Lan | END:REJECTED | FR-M03-13.03, BR-M03-33 |


<!-- sc:branch SC-M03-017 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối hiện lại; Bị Mod ẩn chỉ có đường xử lý/khiếu nại do M08/M09, không tự chuyển công khai. | P301 Nháp/Đã đăng/Đã xóa | END:REJECTED | FR-M03-13.02, BR-M03-33 |


<!-- sc:branch SC-M03-017 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối hiện lại; Bị Mod ẩn chỉ có đường xử lý/khiếu nại do M08/M09, không tự chuyển công khai. | P301 Tự ẩn/Bị Mod ẩn | END:REJECTED | FR-M03-13.05, BR-M03-33 |


<!-- sc:branch SC-M03-017 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống kiểm điều kiện, chuyển về Đã đăng với bản sửa đã lưu, giữ khóa; do có sửa lúc ẩn và hai cờ bật nên gửi quét lại qua M13. Trong lúc quét giữ nội dung đã sửa đang hiển thị theo quyền. | P301 dirty_since_hide=true; Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt | E4.2 | FR-M03-13.02, FR-M03-13.06, FR-M03-05.05, FR-M03-05.06, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, BR-M03-26 |
| E4.2 | ACT-006 | AI trả điểm sạch cho lần quét lại. | Điểm bốn nhóm minh họa Quấy rối=0.20, Ngôn từ thù ghét=0.10, Nội dung người lớn=0.05, Bạo lực=0.10; max=0.20 | E4.3 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E4.3 | SYSTEM | Hệ thống giữ trạng thái đăng/kiểm duyệt hiện có sau kết quả sạch, trả kết quả hiện lại; không tạo một phiên bản sửa mới chỉ vì hiện lại. | P301 Đã đăng/Bình thường; lịch sử bản sửa trước còn | END:SUCCESS | FR-M03-05.10, BR-M03-26 |


<!-- sc:branch SC-M03-017 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống kiểm điều kiện, chuyển về Đã đăng với bản sửa đã lưu, giữ khóa; do có sửa lúc ẩn và hai cờ bật nên gửi quét lại qua M13. Trong lúc quét giữ nội dung đã sửa đang hiển thị theo quyền. | P301 dirty_since_hide=true; Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt | E5.2 | FR-M03-13.02, FR-M03-13.06, FR-M03-05.05, FR-M03-05.06, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, BR-M03-26 |
| E5.2 | ACT-006 | AI trả điểm quét lại đáng nghi/cao. | max=0.50 hoặc 0.95 | E5.3 | FR-M13-02.04, FR-M13-02.05, FR-M13-02.06 |
| E5.3 | SYSTEM | Hệ thống chuyển kiểm duyệt Bị gắn cờ, ẩn bài với người khác và chuyển Mod xét; trạng thái đăng vẫn Đã đăng, không đổi sang Bị từ chối vì điểm≥0.9. | P301 Đã đăng/Bị gắn cờ; trả kết quả xử lý cho tác giả | END:SUCCESS | FR-M03-05.07, BR-M03-26 |


<!-- sc:branch SC-M03-017 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống kiểm điều kiện rồi hiện lại về Đã đăng, không quét; giữ kiểm duyệt/khóa, không quét bù chỉ vì công tắc bật sau đó. | P301 dirty=true; Đã đăng/Bình thường ở snapshot; cờ AI hoặc Moderation=false | END:SUCCESS | FR-M03-13.02, FR-M03-13.06, FR-M03-05.08, FR-M03-05.09, BR-M03-22, BR-M03-26 |


<!-- sc:branch SC-M03-017 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống kiểm điều kiện, chuyển về Đã đăng với bản sửa đã lưu, giữ khóa; do có sửa lúc ẩn và hai cờ bật nên gửi quét lại qua M13. Trong lúc quét giữ nội dung đã sửa đang hiển thị theo quyền. | P301 dirty_since_hide=true; Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt | E7.2 | FR-M03-13.02, FR-M03-13.06, FR-M03-05.05, FR-M03-05.06, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, BR-M03-26 |
| E7.2 | ACT-006 | Dịch vụ AI báo lỗi ở lần quét lại đầu. | Lần1 không có score | E7.3 | FR-M13-01.04 |
| E7.3 | SYSTEM | Hệ thống chờ 2 giây, thử lại đúng một lần, tiếp tục giữ bài với nội dung sửa theo trạng thái đang hiển thị. | Không đổi sang Chờ duyệt chỉ vì lỗi quét lại | E7.4 | FR-M13-01.05 |
| E7.4 | ACT-006 | Dịch vụ AI trả điểm sạch ở lần thử lại. | Lần2 max=0.20 | E7.5 | FR-M13-02.04 |
| E7.5 | SYSTEM | Hệ thống giữ nguyên trạng thái và tiếp tục hiển thị theo quyền; trả kết quả quét lại sạch. | P301 Đã đăng/Bình thường theo snapshot | END:SUCCESS | FR-M03-05.10, BR-M03-26 |


<!-- sc:branch SC-M03-017 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống kiểm điều kiện, chuyển về Đã đăng với bản sửa đã lưu, giữ khóa; do có sửa lúc ẩn và hai cờ bật nên gửi quét lại qua M13. Trong lúc quét giữ nội dung đã sửa đang hiển thị theo quyền. | P301 dirty_since_hide=true; Tiêu đề, nội dung chữ, câu hỏi/lựa chọn poll và ảnh được gửi qua M13; PDF/DOCX/XLSX/PPTX không gửi AI kiểm duyệt | E8.2 | FR-M03-13.02, FR-M03-13.06, FR-M03-05.05, FR-M03-05.06, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, BR-M03-26 |
| E8.2 | ACT-006 | Dịch vụ AI báo lỗi ở lần quét lại đầu. | Lần1 không có score | E8.3 | FR-M13-01.04 |
| E8.3 | SYSTEM | Hệ thống chờ 2 giây, thử lại đúng một lần, tiếp tục giữ bài với nội dung sửa theo trạng thái đang hiển thị. | Không đổi sang Chờ duyệt chỉ vì lỗi quét lại | E8.4 | FR-M13-01.05 |
| E8.4 | ACT-006 | Dịch vụ AI tiếp tục lỗi. | Lần2 lỗi | E8.5 | FR-M13-01.06 |
| E8.5 | SYSTEM | Hệ thống giữ nguyên trạng thái và tiếp tục hiển thị theo quyền; trả kết quả quét lại thất bại, không tự gắn cờ/chờ duyệt. | P301 Đã đăng/Bình thường theo snapshot | END:SUCCESS | FR-M03-05.11, BR-M03-26 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-017 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu hiện lại bài đã tự ẩn. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


**V2 — thay toàn bộ M1 đến kết thúc:** ADMIN hiện lại bài tự ẩn đã sửa của mình. Actor khởi tạo ACT-003; kết quả END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-017 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-003 | Admin yêu cầu hiện lại P301. | P301 Tự ẩn/Bình thường, dirty=true; author=U-ADMIN | V2.2 | FR-M03-13.02 |
| V2.2 | SYSTEM | Hệ thống kiểm chủ/Tự ẩn và kiểm duyệt hợp lệ, chuyển Đã đăng, giữ khóa, trả kết quả; không quét lại vì tác giả ADMIN. | P301 Đã đăng/Bình thường; không vượt ràng buộc nhóm/tài khoản | END:SUCCESS | FR-M03-13.02, FR-M03-13.06, FR-M03-05.15, BR-M03-51 |


<!-- sc:end SC-M03-017 -->

<a id="sc-m03-018"></a>

<!-- sc:scenario SC-M03-018 -->

### SC-M03-018

#### 1. Tên kịch bản chuẩn

Xem lại bài từ ngữ cảnh xử lý hoặc khiếu nại liên quan — BF-M03-018. UC owner: [UC-M03-018](../../us/US-M03.md#uc-m03-018). Trigger: Lan mở thông báo kết quả xử lý về P301 của mình.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Có phiên, thông báo kết quả xử lý báo cáo bài mình hoặc khiếu nại của mình liên quan chính bài đó. Biết ID/URL không thay thế quyền; đường chuẩn tác giả xem lại bài đã xóa hẳn.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-018 -->

| result | condition |
|---|---|
| SUCCESS | Bài được trả chỉ đọc trong ngữ cảnh hợp lệ, bảo vệ dữ liệu báo cáo; không hồi sinh nội dung công khai hoặc tạo nơi duyệt bài đã xóa. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-018 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan mở thông báo kết quả xử lý về P301 của mình. | P301 Đã xóa/permanent=true; notification N301 trỏ kết quả vụ việc của P301 | M2 | FR-M03-07.08 |
| M2 | SYSTEM | Hệ thống kiểm chính tác giả và liên kết vụ việc rồi trả bài chỉ đọc, kể cả xóa hẳn; không hiển thị danh tính, lý do đã chọn, mô tả hoặc bằng chứng người báo cáo. Không đưa bài trở lại tab/feed hoặc cho khôi phục. | P301 nội dung/tệp/poll/phiếu/lịch sử còn giữ; dữ liệu người báo cáo không được trả | END:SUCCESS | FR-M03-07.08, FR-M03-07.09, FR-M03-07.10, FR-M03-17.02, FR-M03-17.03, BR-M03-37 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-018 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Người mở không phải tác giả trên đường xem lại dành cho tác giả | E1.1 | FR-M03-07.10 |
| E2 | system | M2 | Không có thông báo/khiếu nại hợp lệ liên quan bài | E2.1 | FR-M03-07.08, FR-M03-17.04, BR-M03-49 |


<!-- sc:branch SC-M03-018 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối xem lại bài xóa hẳn của người khác, không dựa vào việc biết link. | Minh mở N301/P301 của Lan | END:REJECTED | FR-M03-07.10 |


<!-- sc:branch SC-M03-018 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống không mở đường xem lại đặc biệt; URL thông thường phải theo quyền đọc. | Ngữ cảnh giả hoặc vụ việc liên quan P999 khác P301 | END:REJECTED | FR-M03-07.08, FR-M03-17.04, BR-M03-49 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-018 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu xem lại bài từ ngữ cảnh xử lý hoặc khiếu nại liên quan. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


**V2 — thay toàn bộ M1 đến kết thúc:** Mod/Admin mở đúng bài từ báo cáo/lịch sử báo cáo/khiếu nại liên quan. Actor khởi tạo ACT-003; kết quả END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-018 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-003 | Mod Minh mở P301 từ vụ việc liên quan chính P301. | Case C301 trỏ P301, Mod có quyền xử lý/tra cứu theo M08/M09; không browse bài riêng tư | V2.2 | FR-M03-07.11, FR-M03-17.04 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền và liên kết bài–vụ việc, trả nội dung được giữ của bài Tự ẩn/Đã xóa/Đã xóa hẳn trong ngữ cảnh vụ; Bị gắn cờ/Bị Mod ẩn theo đường M08/M09. Không biến hành vi đọc thành khôi phục hoặc công khai. | Snapshot P301 permanent=true, dữ liệu còn; chỉ vụ C301 đang xem | END:SUCCESS | FR-M03-07.02, FR-M03-07.11, FR-M03-17.02, FR-M03-17.04, BR-M03-37, BR-M03-49 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mở Nháp/Bị từ chối người khác. Actor khởi tạo ACT-003; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-018 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-003 | Mod yêu cầu đọc P301. | P301 Nháp hoặc Bị từ chối của Lan | V3.2 | FR-M03-07.07, FR-M03-07.11, FR-M03-17.04 |
| V3.2 | SYSTEM | Hệ thống từ chối đường truy cập không được phép; không có danh mục tìm/browse bài đã xóa. | P301 Nháp hoặc Bị từ chối của Lan | END:REJECTED | FR-M03-07.07, FR-M03-07.11, FR-M03-17.04, BR-M03-49 |


**V4 — thay toàn bộ M1 đến kết thúc:** Mở Tự ẩn/Đã xóa/xóa hẳn ngoài vụ liên quan. Actor khởi tạo ACT-003; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-018 V4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V4.1 | ACT-003 | Mod yêu cầu đọc P301. | P301 Tự ẩn/Đã xóa/permanent, URL trực tiếp không vụ liên quan | V4.2 | FR-M03-07.07, FR-M03-07.11, FR-M03-17.04 |
| V4.2 | SYSTEM | Hệ thống từ chối đường truy cập không được phép; không có danh mục tìm/browse bài đã xóa. | P301 Tự ẩn/Đã xóa/permanent, URL trực tiếp không vụ liên quan | END:REJECTED | FR-M03-07.07, FR-M03-07.11, FR-M03-17.04, BR-M03-49 |


<!-- sc:end SC-M03-018 -->

<a id="sc-m03-019"></a>

<!-- sc:scenario SC-M03-019 -->

### SC-M03-019

#### 1. Tên kịch bản chuẩn

Kết thúc poll ngay — BF-M03-019. UC owner: [UC-M03-009](../../us/US-M03.md#uc-m03-009). Trigger: Lan yêu cầu Kết thúc ngay Q301.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Có phiên và poll gắn bài đã gửi; kiểm chủ và poll đang mở. Không cần thay nội dung bài.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-019 -->

| result | condition |
|---|---|
| SUCCESS | Poll đóng ngay, kết quả được hiển thị đúng quyền và sự kiện kết thúc được cung cấp; không gửi phiếu mới. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-019 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan yêu cầu Kết thúc ngay Q301. | Q301: A="Phương pháp thế", B="Phân tích nhân tử", C="Dùng công thức"; chọn nhiều; ẩn kết quả trước vote; hạn 09/11/2026 10:00 +07; hiện 08/11/2026 10:00 +07 | M2 | FR-M03-09.02 |
| M2 | SYSTEM | Hệ thống kiểm tác giả và poll mở, đặt hạn bằng thời điểm hiện tại, chuyển Đã đóng; trả kết quả cuối cho người xem được bài và gửi sự kiện poll kết thúc tới M07. | Q301 deadline=08/11 10:00, Đã đóng; A3 B2 C1 /6 →50/33/17%; không nhận phiếu tiếp | END:SUCCESS | FR-M03-09.02, FR-M03-09.04, FR-M03-10.02, FR-M03-08.06, FR-M03-08.10, FR-M03-08.12, BR-M03-13, BR-M03-14, BR-M03-15 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-019 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Người thao tác không phải tác giả | E1.1 | FR-M03-09.04 |
| E2 | system | M2 | Poll đã đóng | E2.1 | FR-M03-09.03, FR-M03-09.08, BR-M03-13, BR-M03-14, BR-M03-44 |


<!-- sc:branch SC-M03-019 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối thay đổi poll của người khác. | Minh thao tác Q301 của Lan | END:REJECTED | FR-M03-09.04 |


<!-- sc:branch SC-M03-019 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối đổi hạn/mở lại/đóng lại/thêm lựa chọn; không làm poll mở lại. | Q301 Đã đóng | END:REJECTED | FR-M03-09.03, FR-M03-09.08, BR-M03-13, BR-M03-14, BR-M03-44 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-019 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu kết thúc poll ngay. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


<!-- sc:end SC-M03-019 -->

<a id="sc-m03-020"></a>

<!-- sc:scenario SC-M03-020 -->

### SC-M03-020

#### 1. Tên kịch bản chuẩn

Thêm lựa chọn vào poll đang mở của bài đã gửi — BF-M03-020. UC owner: [UC-M03-009](../../us/US-M03.md#uc-m03-009). Trigger: Lan gửi lựa chọn D mới cho Q301.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Có phiên; bài đã gửi có Q301 đang mở là dữ liệu chuẩn. Chỉ thêm, không sửa hoặc xóa lựa chọn đã có.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-020 -->

| result | condition |
|---|---|
| SUCCESS | Lựa chọn mới được thêm hợp lệ; lựa chọn cũ và phiếu được giữ. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-020 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan gửi lựa chọn D mới cho Q301. | A/B/C đã có; D="Cách khác"; tổng dự kiến=4 | M2 | FR-M03-09.06 |
| M2 | SYSTEM | Hệ thống kiểm tác giả, poll còn mở và tổng ≤10, thêm D và trả poll đã cập nhật; giữ các lựa chọn/phiếu cũ, không đổi chế độ. | Q301 có A,B,C,D; D chưa có lượt chọn; các phiếu cũ không đổi | END:SUCCESS | FR-M03-09.04, FR-M03-09.06, FR-M03-09.07, FR-M03-09.08, BR-M03-44 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-020 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Người thao tác không phải tác giả | E1.1 | FR-M03-09.04 |
| E2 | system | M2 | Poll đã đóng | E2.1 | FR-M03-09.03, FR-M03-09.08, BR-M03-13, BR-M03-14, BR-M03-44 |
| E3 | system | M2 | Thêm lựa chọn khiến tổng vượt 10 | E3.1 | FR-M03-09.07 |
| E4 | system | M2 | Tác giả yêu cầu thêm/bỏ cả poll, sửa/xóa lựa chọn cũ hoặc đổi cấu hình sau gửi | E4.1 | FR-M03-03.11, BR-M03-11, BR-M03-44 |
| E5 | system | M2 | Thêm lựa chọn thứ10 khi poll còn mở | E5.1 | FR-M03-09.06, FR-M03-09.07, BR-M03-44 |


<!-- sc:branch SC-M03-020 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối thay đổi poll của người khác. | Minh thao tác Q301 của Lan | END:REJECTED | FR-M03-09.04 |


<!-- sc:branch SC-M03-020 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối đổi hạn/mở lại/đóng lại/thêm lựa chọn; không làm poll mở lại. | Q301 Đã đóng | END:REJECTED | FR-M03-09.03, FR-M03-09.08, BR-M03-13, BR-M03-14, BR-M03-44 |


<!-- sc:branch SC-M03-020 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối lựa chọn thêm, giữ các lựa chọn trước đó. | Đã có 10, thêm lựa chọn thứ11 | END:REJECTED | FR-M03-09.07 |


<!-- sc:branch SC-M03-020 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối thay đổi bị khóa sau gửi; không dùng quyền thêm lựa chọn để vượt ràng buộc. | P301 đã gửi; muốn xóa A hoặc đổi chọn nhiều sang chọn một | END:REJECTED | FR-M03-03.11, BR-M03-11, BR-M03-44 |


<!-- sc:branch SC-M03-020 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống nhận lựa chọn mới của tác giả vì tổng vẫn trong giới hạn, trả poll 10 lựa chọn. | 9 lựa chọn cũ + lựa chọn thứ10 hợp lệ; giữ phiếu | END:SUCCESS | FR-M03-09.06, FR-M03-09.07, BR-M03-44 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-020 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu thêm lựa chọn vào poll đang mở của bài đã gửi. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


<!-- sc:end SC-M03-020 -->

<a id="sc-m03-021"></a>

<!-- sc:scenario SC-M03-021 -->

### SC-M03-021

#### 1. Tên kịch bản chuẩn

Mở khóa hoặc hạ mức khóa bài viết — BF-M03-021. UC owner: [UC-M03-014](../../us/US-M03.md#uc-m03-014). Trigger: Lan yêu cầu mở khóa bình luận P301 do mình khóa.

#### 2. Actor thực hiện

ACT-002 là actor chính. ACT-003 kế thừa User theo US, nhưng chỉ ADMIN thật sự được miễn quét. ACT-006 chỉ xuất hiện khi có lời gọi nhà cung cấp qua M13. Các đường V trong mục 6 ghi riêng actor khởi tạo thay thế, không thêm BF theo vai trò.

#### 3. Tiền điều kiện

Có phiên và mức khóa hiện hành. Kiểm người khóa trước đó; tác giả chỉ được mở khóa bình luận do chính mình đặt.

#### 4. Hậu điều kiện

<!-- sc:post SC-M03-021 -->

| result | condition |
|---|---|
| SUCCESS | Mức khóa được mở/hạ hợp lệ; không vượt khóa Mod/Admin hoặc thay quyền đọc. |
| REJECTED | Yêu cầu bị từ chối theo điều kiện ở nhánh; không coi là hoàn thành mục tiêu chuẩn. Dữ liệu và trạng thái giữ/đổi đúng mô tả của nhánh, không tự mở quyền. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M03-021 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan yêu cầu mở khóa bình luận P301 do mình khóa. | level=Khóa bình luận; locker=U-LAN | M2 | FR-M03-14.07 |
| M2 | SYSTEM | Hệ thống kiểm chính tác giả và người khóa, đặt Không khóa, trả mức mới; giữ các chiều trạng thái khác và các cổng quyền không thuộc mức khóa. | P301 level=Không khóa; không tự bỏ Bị gắn cờ/Bị Mod ẩn | END:SUCCESS | FR-M03-14.07, BR-M03-32 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau bước đó. Guard thay dữ liệu/ngữ cảnh của chính lần yêu cầu bằng bộ thay thế, không ghép dữ liệu chuẩn và dữ liệu lỗi. Các đường sửa/gửi lại quay về bước kiểm cụ thể; còn sai áp lại guard tương ứng, không tự đặt giới hạn số lần. Từ chối cuối cùng theo US có thể kết thúc REJECTED, không bịa OK/thử lại.

<!-- sc:exceptions SC-M03-021 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Người khóa là Mod/Admin và tác giả muốn mở hoặc đổi mức | E1.1 | FR-M03-14.09, BR-M03-32 |
| E2 | system | M2 | Người yêu cầu không là tác giả, Mod hoặc Admin | E2.1 | FR-M03-14.11 |


<!-- sc:branch SC-M03-021 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối tác giả đổi/mở khóa do Mod/Admin đặt. | locker=U-MOD; actor=Lan tác giả | END:REJECTED | FR-M03-14.09, BR-M03-32 |


<!-- sc:branch SC-M03-021 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối thao tác khóa/mở khóa bình luận của người khác. | actor=Minh thường; author=Lan | END:REJECTED | FR-M03-14.11 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này; thay toàn bộ đường chính. Actor khởi tạo ACT-001; kết quả END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-021 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu mở khóa hoặc hạ mức khóa bài viết. | Không có phiên đăng nhập | V1.2 | FR-M03-07.06 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác khi chưa đăng nhập; không tự chạy đăng nhập hoặc thay đổi bài/poll/phiếu. | Giữ dữ liệu trước yêu cầu, chưa hoàn tất chức năng | END:REJECTED | FR-M03-07.06 |


**V2 — thay toàn bộ M1 đến kết thúc:** Mod/Admin mở hoặc hạ mức xuống Không khóa. Actor khởi tạo ACT-003; kết quả END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-021 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-003 | Mod Minh yêu cầu đặt mức mới Không khóa. | P301 hiện Khóa toàn bộ bởi Mod, hoặc khóa bình luận bởi tác giả | V2.2 | FR-M03-14.08 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền Mod/Admin rồi đặt mức mới, trả kết quả; không đổi trạng thái đăng/kiểm duyệt. Khi mức mới còn hạn chế, cập nhật người khóa theo chủ thể đặt hạn chế. | level=Không khóa; không cho tác giả vượt khóa của Mod | END:SUCCESS | FR-M03-14.08, BR-M03-32 |


**V3 — thay toàn bộ M1 đến kết thúc:** Mod/Admin mở hoặc hạ mức xuống Khóa bình luận. Actor khởi tạo ACT-003; kết quả END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:role-path SC-M03-021 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-003 | Mod Minh yêu cầu đặt mức mới Khóa bình luận. | P301 hiện Khóa toàn bộ bởi Mod, hoặc khóa bình luận bởi tác giả | V3.2 | FR-M03-14.08 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền Mod/Admin rồi đặt mức mới, trả kết quả; không đổi trạng thái đăng/kiểm duyệt. Khi mức mới còn hạn chế, cập nhật người khóa theo chủ thể đặt hạn chế. | level=Khóa bình luận; không cho tác giả vượt khóa của Mod | END:SUCCESS | FR-M03-14.08, BR-M03-32 |


<!-- sc:end SC-M03-021 -->

## 5. Quy tắc nền/giao tiếp (không phải scenario)

| ID | Trigger/điều kiện | Hiệu ứng và giới hạn | sources |
|---|---|---|---|
| AUT-M03-001 | Gửi mới, sửa Đã đăng hoặc hiện lại Tự ẩn đã sửa, khi cần quét | UC005 quyết định chính sách trong SC004/011/017; M13 gửi dữ liệu/timeout 5 giây, chờ2 giây thử lại một lần, lấy max4 nhóm và xử hòa theo thứ tự Quấy rối, Ngôn từ thù ghét, Nội dung người lớn, Bạo lực. Quét mới dưới0.5 đăng, [0.5,0.9) chờ Mod, ≥0.9 tự từ chối; lỗi cuối chờ Mod. Quét lại ≥0.5 chỉ gắn cờ, lỗi giữ trạng thái. Admin không quét; cờ tắt không quét và bật lại không quét bù. | FR-M03-05.01, FR-M03-05.02, FR-M03-05.03, FR-M03-05.04, FR-M03-05.05, FR-M03-05.06, FR-M03-05.07, FR-M03-05.08, FR-M03-05.09, FR-M03-05.10, FR-M03-05.11, FR-M03-05.12, FR-M03-05.13, FR-M03-05.14, FR-M03-05.15, BR-M03-19, BR-M03-20, BR-M03-21, BR-M03-22, BR-M03-26, BR-M03-51, FR-M13-01.01, FR-M13-02.01, FR-M13-02.02, FR-M13-02.04, FR-M13-02.05, FR-M13-02.06, FR-M13-01.04, FR-M13-01.05, FR-M13-01.06 |
| AUT-M03-002 | Đến đúng hạn của poll đang mở | Chuyển Đã đóng, từ đúng thời điểm hạn không nhận mới/đổi/bỏ phiếu và không thể mở lại. Mọi người có quyền xem bài thấy kết quả. Không cần actor giả đóng poll tự động. | FR-M03-10.01, FR-M03-08.06, FR-M03-08.10, BR-M03-13, BR-M03-14, BR-M03-15 |
| AUT-M03-003 | Bài Đã xóa đủ 7×24h tính từ deleted_at | Gắn cờ Đã xóa hẳn, không cho phục hồi, bỏ khỏi mọi chỗ thông thường kể cả tab Đã xóa. Giữ toàn bộ nội dung, tệp, poll, phiếu, lịch sử, Topic/Tag, bình luận và lượt nhắc. Phát mốc cho M02 bỏ bookmark, M12 xử lý điểm, M15 thống kê; không xóa vật lý. Vẫn cho đường xem lại hẹp SC018. | FR-M03-17.01, FR-M03-17.02, FR-M03-17.03, FR-M03-17.04, FR-M03-16.02, FR-M03-16.03, BR-M03-35, BR-M03-37 |
| AUT-M03-004 | Poll chuyển Đã đóng do hết hạn hoặc kết thúc ngay | Gửi sự kiện poll kết thúc tới M07; phân phối thông báo thuộc M07, không bịa người bấm xác nhận hay lịch quét mới. | FR-M03-10.02 |
| RULE-M03-001 | Đọc bài qua URL thường hoặc qua vụ việc | Ba chiều độc lập: trạng thái đăng, kiểm duyệt, khóa/người khóa; xóa hẳn là cờ giữ dữ liệu. Công khai cần Đã đăng/Bình thường và qua quyền tài khoản/nhóm. Tác giả xem đến trước xóa hẳn; xóa hẳn chỉ xem lại đúng ngữ cảnh. Mod không đọc nháp/bị từ chối người khác; không tự browse bài riêng tư. | FR-M03-07.01, FR-M03-07.02, FR-M03-07.03, FR-M03-07.04, FR-M03-07.05, FR-M03-07.06, FR-M03-07.07, FR-M03-07.08, FR-M03-07.09, FR-M03-07.10, FR-M03-07.11, BR-M03-17, BR-M03-18, BR-M03-37, BR-M03-39, BR-M03-49, FR-M01-13.01, FR-M11-03.06 |
| RULE-M03-002 | Kiểm quyền, soạn/gửi/lưu và hạn chế cảnh cáo | MEDIUM/HEAVY chỉ chặn lưu nháp mới, gửi nháp, gửi lại từ chối; vẫn sửa Đã đăng, khôi phục, vote nếu các điều kiện khác hợp lệ. Giới hạn150ký tự/6000từ đếm chữ người đọc thấy theo cụm cách khoảng trắng; vượt phải cảnh báo ngay và giữ nội dung khi từ chối lưu/gửi. Editor hỗ trợ đậm/nghiêng/gạch chân/gạch ngang/tô sáng, H1–H3, danh sách chấm/số/việc cần làm, code inline/khối tô cú pháp, LaTeX mã thô, bảng, trích dẫn, đường ngang và link nhãn tùy chỉnh. Không có ảnh inline/ảnh bìa/Accepted Answer, không tự viết bài bằng AI. | FR-M03-01.02, FR-M03-01.03, FR-M03-01.04, FR-M03-01.10, FR-M03-01.11, FR-M03-01.14, FR-M03-01.15, FR-M03-01.16, FR-M03-01.17, BR-M03-01, BR-M03-03, BR-M03-04, BR-M03-05, BR-M03-38, BR-M03-42, BR-M03-43, BR-M03-50 |
| RULE-M03-003 | Hiển thị poll/kết quả | Mở + chưa vote chỉ thấy kết quả khi cấu hình bật; đã vote thấy kết quả; đóng ai được đọc bài cũng thấy. Tính số lượt chọn lựa chọn/tổng lượt chọn, không chia số người; làm tròn nguyên có thể tổng99/101%. Chưa có lượt chọn không tự khẳng định0/0 hoặc giá trị phần trăm chưa được nguồn quyết. | FR-M03-08.07, FR-M03-08.08, FR-M03-08.09, FR-M03-08.10, FR-M03-08.12, BR-M03-15 |
| RULE-M03-004 | Mức khóa đổi hoặc có tương tác | Khóa bình luận chặn bình luận mới, giữ bình luận cũ. Khóa toàn bộ chỉ Mod/Admin đặt, chặn bình luận, mọi upvote/rút upvote trên bài và bình luận, vote/đổi/bỏ phiếu; bookmark và báo cáo vẫn dùng. Người khóa được ghi; tác giả không vượt khóa Mod. M02/M04/M08/M12 thực hiện tương tác sở hữu, M03 cung cấp điều kiện. | FR-M03-14.01, FR-M03-14.02, FR-M03-14.03, FR-M03-14.04, FR-M03-14.05, FR-M03-14.06, FR-M03-14.07, FR-M03-14.08, FR-M03-14.09, FR-M03-14.10, FR-M03-14.11, FR-M03-14.12, FR-M03-08.13, BR-M03-30, BR-M03-31, BR-M03-32 |
| RULE-M03-005 | Công bố, sửa, khiếu nại hoặc phân loại liên module | Mọi đường công bố cung cấp thời điểm đăng, tác giả, ẩn danh và lần đầu công khai cho M07/M14/M15; M13 nhận sự kiện tạo/đổi nội dung để embedding. Mention theo M01 khi công khai, không chỉ lúc lưu nháp. Mod/Admin đổi Topic/Tag của người khác ở M05 không tạo phiên bản, nhãn chỉnh sửa hoặc báo tác giả. Khiếu nại AI tự từ chối được chấp nhận: ngoài nhóm Đã đăng ngay, trong nhóm qua cổng M11, không quét lại; nếu tác giả đã gửi lại trước kết luận thì không đổi trạng thái. Không triển khai xử lý khiếu nại trong M03. | FR-M03-11.02, FR-M03-11.05, FR-M03-11.06, FR-M03-12.01, FR-M03-04.03, FR-M03-04.11, FR-M03-05.01, FR-M03-05.03, FR-M03-06.02, FR-M03-06.03, BR-M03-27, BR-M03-28, BR-M03-46, FR-M09-08.12 |
| RULE-M03-CLASSIFICATION | Soạn/lưu/gửi/sửa có Topic/Tag | M05 cung cấp: nháp0–3 Topic; gửi/sửa cần1–3 trong danh mục còn hiệu lực;0–5 Tag hợp lệ, bỏ trùng và áp chuẩn hóa. M03 dùng contract, không chạy phân tích M05 hoặc gợi ý AI Topic khi không được actor yêu cầu. Dataset chọn Topic Toán, #daiso hợp lệ; cảnh báo gợi ý lỗi thời không chặn gửi. | FR-M05-01.01, FR-M05-01.02, FR-M05-01.03, FR-M05-01.07, FR-M05-01.09, FR-M05-01.10, FR-M05-03.01, FR-M05-02.11 |
| RULE-M03-GROUP | Bài thuộc nhóm hoặc quyền nhóm thay đổi | M11 quyết thành viên/Private/ẩn danh, cổng duyệt nhóm và cờ Group. Owner không vào hàng nhóm; score[0.5,0.9) hoặc lỗi cuối vào hàng Mod hệ thống. Member lỗi/nghi ngờ vào hàng nhóm, sạch theo duyệt trước. Admin miễn quét nhưng không miễn hàng nhóm nếu không là Owner. Cờ Group tắt không tự biến bài nhóm thành bài ngoài nhóm hoặc cấp quyền, không thêm browse nhóm ở M03. | FR-M03-04.05, BR-M03-25, BR-M03-51, FR-M11-12.01, FR-M11-12.02, FR-M11-12.03, FR-M11-12.04, FR-M11-12.05, FR-M11-12.06, FR-M11-12.14, FR-M11-12.15, FR-M11-12.16, FR-M11-12.17, FR-M11-12.18, FR-M11-12.19, FR-M11-12.20 |


## 6. Truy vết hai chiều

| Mã FR/BR | SC/bước/nhánh hoặc quy tắc | Mức đối soát |
|---|---|---|
| FR-M03-01 | SC-M03-001/M1; SC-M03-001/M5; SC-M03-001/M6; SC-M03-001/E4.1; SC-M03-001/E5.1; SC-M03-001/E5.2; SC-M03-001/E5.3; SC-M03-001/E5.4; SC-M03-001/E7.4; SC-M03-001/E8.3; SC-M03-001/E9.3; SC-M03-001/E10.3; SC-M03-001/E11.3; SC-M03-001/E12.3; SC-M03-001/E13.3; SC-M03-001/E15.4; SC-M03-001/E21.3; SC-M03-001/E22.3; SC-M03-001/M2; SC-M03-001/M4; RULE-M03-002; SC-M03-001/M3; SC-M03-001/E6.1; SC-M03-001/E6.2; SC-M03-001/E6.3; SC-M03-001/E6.4; SC-M03-001/E6.5; SC-M03-004/M2; SC-M03-004/E7.1; SC-M03-004/E7.2; SC-M03-011/M2; SC-M03-011/E5.1; SC-M03-011/E5.2; SC-M03-011/E5.3; SC-M03-011/E5.4; SC-M03-011/E5.5; SC-M03-001/E3.1; SC-M03-001/E1.1; SC-M03-001/E2.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-02 | SC-M03-001/E7.1; SC-M03-001/E7.2; SC-M03-001/E7.3; SC-M03-001/E7.4; SC-M03-001/E8.3; SC-M03-001/E9.3; SC-M03-001/E10.3; SC-M03-001/E11.3; SC-M03-001/E12.3; SC-M03-001/E13.3; SC-M03-011/E10.2; SC-M03-011/E10.1; SC-M03-011/E11.3; SC-M03-011/E12.3; SC-M03-011/E13.3; SC-M03-011/E14.3; SC-M03-011/E15.3; SC-M03-011/E16.3; SC-M03-007/M2; SC-M03-001/E8.1; SC-M03-001/E8.2; SC-M03-011/E11.1; SC-M03-011/E11.2; SC-M03-001/E9.1; SC-M03-001/E9.2; SC-M03-011/E12.1; SC-M03-011/E12.2; SC-M03-001/E10.1; SC-M03-001/E10.2; SC-M03-011/E13.1; SC-M03-011/E13.2; SC-M03-001/E11.1; SC-M03-001/E11.2; SC-M03-011/E14.1; SC-M03-011/E14.2; SC-M03-001/E12.1; SC-M03-001/E12.2; SC-M03-011/E15.1; SC-M03-011/E15.2; SC-M03-001/E13.1; SC-M03-001/E13.2; SC-M03-011/E16.1; SC-M03-011/E16.2; SC-M03-001/E14.1; SC-M03-011/E1.1; SC-M03-011/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-03 | SC-M03-001/E15.1; SC-M03-001/E15.4; SC-M03-001/E15.2; SC-M03-001/E21.2; SC-M03-001/E15.3; SC-M03-001/E18.1; SC-M03-001/E18.2; SC-M03-001/E16.1; SC-M03-001/E16.2; SC-M03-001/E17.1; SC-M03-001/E17.2; SC-M03-001/E20.1; SC-M03-001/E20.2; SC-M03-001/E19.1; SC-M03-001/E19.2; SC-M03-001/E21.1; SC-M03-001/E22.1; SC-M03-001/E22.2; SC-M03-011/M2; SC-M03-020/E4.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-04 | SC-M03-004/M1; SC-M03-004/M2; SC-M03-004/E11.2; SC-M03-004/E1.1; SC-M03-004/E2.1; SC-M03-004/E4.1; SC-M03-004/E5.1; SC-M03-004/E10.1; SC-M03-004/E3.1; SC-M03-004/E8.1; SC-M03-004/E9.1; RULE-M03-005; SC-M03-004/E13.1; SC-M03-004/E26.3; SC-M03-011/E7.1; SC-M03-004/E18.1; SC-M03-004/E19.1; SC-M03-004/E20.1; SC-M03-004/E21.1; SC-M03-004/E22.1; SC-M03-004/E23.1; SC-M03-004/E24.1; SC-M03-004/E28.1; SC-M03-004/E29.1; SC-M03-004/V3.1; SC-M03-004/V4.1; RULE-M03-GROUP; SC-M03-004/V2.1; SC-M03-004/V2.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05 | SC-M03-004/M4; SC-M03-004/E14.4; AUT-M03-001; RULE-M03-005; SC-M03-004/E8.1; SC-M03-011/E8.1; SC-M03-017/E6.1; SC-M03-004/E11.2; SC-M03-004/E16.4; SC-M03-004/E12.2; SC-M03-004/E17.4; SC-M03-004/E26.2; SC-M03-004/E27.2; SC-M03-004/E13.1; SC-M03-004/E26.3; SC-M03-004/E15.4; SC-M03-004/E28.5; SC-M03-004/E29.5; SC-M03-004/V2.2; SC-M03-011/V2.4; SC-M03-017/V2.2; SC-M03-011/M4; SC-M03-017/E4.1; SC-M03-017/E5.1; SC-M03-017/E7.1; SC-M03-017/E8.1; SC-M03-011/M6; SC-M03-011/E18.4; SC-M03-017/E4.3; SC-M03-017/E7.5; SC-M03-011/E6.1; SC-M03-011/E9.2; SC-M03-017/E5.3; SC-M03-011/E19.4; SC-M03-017/E8.5 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-06 | SC-M03-006/M1; SC-M03-006/M2; SC-M03-006/M4; SC-M03-006/E1.2; SC-M03-006/E2.4; SC-M03-006/E3.1; SC-M03-006/E4.1; SC-M03-006/V2.1; SC-M03-006/V2.2; SC-M03-006/M3; RULE-M03-005; SC-M03-006/E5.1; SC-M03-015/E3.1; SC-M03-006/E1.1; SC-M03-006/E2.3; SC-M03-007/E5.1; SC-M03-006/E2.1; SC-M03-006/E2.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-07 | SC-M03-001/V1.1; SC-M03-001/V1.2; SC-M03-004/V1.1; SC-M03-004/V1.2; SC-M03-006/V1.1; SC-M03-006/V1.2; SC-M03-008/V1.1; SC-M03-008/V1.2; SC-M03-009/V1.1; SC-M03-009/V1.2; SC-M03-011/V1.1; SC-M03-011/V1.2; SC-M03-013/V1.1; SC-M03-013/V1.2; SC-M03-014/V1.1; SC-M03-014/V1.2; SC-M03-015/V1.1; SC-M03-015/V1.2; SC-M03-016/V1.1; SC-M03-016/V1.2; SC-M03-017/V1.1; SC-M03-017/V1.2; SC-M03-018/V1.1; SC-M03-018/V1.2; SC-M03-019/V1.1; SC-M03-019/V1.2; SC-M03-020/V1.1; SC-M03-020/V1.2; SC-M03-021/V1.1; SC-M03-021/V1.2; RULE-M03-001; SC-M03-007/M1; SC-M03-007/M2; SC-M03-007/E3.1; SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.1; SC-M03-007/V1.1; SC-M03-007/V1.2; SC-M03-007/V2.1; SC-M03-007/V2.2; SC-M03-012/V2.1; SC-M03-012/V2.2; SC-M03-007/E1.1; SC-M03-018/V2.2; SC-M03-007/E5.1; SC-M03-007/E4.1; SC-M03-018/V3.1; SC-M03-018/V3.2; SC-M03-018/V4.1; SC-M03-018/V4.2; SC-M03-018/M1; SC-M03-018/M2; SC-M03-018/E2.1; SC-M03-018/E1.1; SC-M03-018/V2.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-08 | SC-M03-007/M2; SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.1; SC-M03-007/V1.2; SC-M03-008/E4.2; RULE-M03-003; SC-M03-007/E8.3; SC-M03-008/M2; SC-M03-008/E3.2; SC-M03-019/M2; AUT-M03-002; SC-M03-007/E8.2; SC-M03-008/M1; SC-M03-008/E6.1; SC-M03-008/E5.1; SC-M03-008/E2.1; RULE-M03-004; SC-M03-008/E1.1; SC-M03-008/E3.1; SC-M03-008/E4.1; SC-M03-008/E5.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-09 | SC-M03-009/M1; SC-M03-009/M2; SC-M03-009/E1.1; SC-M03-009/E5.1; SC-M03-009/E3.1; SC-M03-019/E2.1; SC-M03-020/E2.1; SC-M03-009/E2.1; SC-M03-019/M2; SC-M03-019/E1.1; SC-M03-020/M2; SC-M03-020/E1.1; SC-M03-009/E4.1; SC-M03-019/M1; SC-M03-020/M1; SC-M03-020/E5.1; SC-M03-020/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-10 | SC-M03-009/E5.1; SC-M03-019/M2; AUT-M03-004; AUT-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-11 | SC-M03-011/M1; SC-M03-011/M2; SC-M03-011/M3; SC-M03-011/M4; SC-M03-011/E6.1; SC-M03-011/E7.1; SC-M03-011/E10.1; SC-M03-011/E10.3; SC-M03-011/E11.3; SC-M03-011/E12.3; SC-M03-011/E13.3; SC-M03-011/E14.3; SC-M03-011/E15.3; SC-M03-011/E16.3; SC-M03-011/V2.1; SC-M03-011/V2.2; SC-M03-011/V2.3; SC-M03-011/E1.1; SC-M03-011/E3.1; SC-M03-011/E2.1; SC-M03-011/E4.1; SC-M03-011/M6; SC-M03-011/E8.1; SC-M03-011/V2.4; RULE-M03-005 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-12 | SC-M03-007/M2; SC-M03-007/E9.1; SC-M03-011/M4; SC-M03-011/M6; SC-M03-011/V2.4; SC-M03-012/M2; RULE-M03-005; SC-M03-007/E9.2; SC-M03-007/E9.3; SC-M03-012/M1; SC-M03-012/V1.2; SC-M03-012/V1.1; SC-M03-007/V2.1; SC-M03-007/V2.2; SC-M03-012/E1.1; SC-M03-012/V2.1; SC-M03-012/V2.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-13 | SC-M03-013/M1; SC-M03-013/M2; SC-M03-013/E1.1; SC-M03-017/M2; SC-M03-017/E1.1; SC-M03-013/E2.1; SC-M03-017/M1; SC-M03-017/E2.1; SC-M03-017/E4.1; SC-M03-017/E5.1; SC-M03-017/E6.1; SC-M03-017/E7.1; SC-M03-017/E8.1; SC-M03-017/V2.1; SC-M03-017/V2.2; SC-M03-017/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-14 | SC-M03-014/M1; SC-M03-014/M2; RULE-M03-004; SC-M03-014/V2.2; SC-M03-014/V3.2; SC-M03-014/E1.1; SC-M03-021/E1.1; SC-M03-014/E2.1; SC-M03-021/E2.1; SC-M03-014/E3.1; SC-M03-014/V2.1; SC-M03-014/V3.1; SC-M03-021/M1; SC-M03-021/M2; SC-M03-021/V2.1; SC-M03-021/V2.2; SC-M03-021/V3.1; SC-M03-021/V3.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-15 | SC-M03-015/M1; SC-M03-015/M2; SC-M03-015/E3.1; SC-M03-015/E1.1; SC-M03-015/E2.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-16 | SC-M03-015/M2; SC-M03-016/M2; AUT-M03-003; SC-M03-016/M1; SC-M03-016/E4.1; SC-M03-016/E5.1; SC-M03-016/E6.1; SC-M03-016/E1.1; SC-M03-016/E2.1; SC-M03-016/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-17 | SC-M03-018/M2; SC-M03-018/V2.2; AUT-M03-003; SC-M03-018/E2.1; SC-M03-018/V2.1; SC-M03-018/V3.1; SC-M03-018/V3.2; SC-M03-018/V4.1; SC-M03-018/V4.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.01 | SC-M03-001/M1; SC-M03-001/M5; SC-M03-001/M6; SC-M03-001/E4.1; SC-M03-001/E5.1; SC-M03-001/E5.2; SC-M03-001/E5.3; SC-M03-001/E5.4; SC-M03-001/E7.4; SC-M03-001/E8.3; SC-M03-001/E9.3; SC-M03-001/E10.3; SC-M03-001/E11.3; SC-M03-001/E12.3; SC-M03-001/E13.3; SC-M03-001/E15.4; SC-M03-001/E21.3; SC-M03-001/E22.3 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.02 | SC-M03-001/M2; SC-M03-001/M4; SC-M03-001/E5.2; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.03 | SC-M03-001/M2; SC-M03-001/M3; SC-M03-001/M4; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.04 | SC-M03-001/M2; SC-M03-001/M4; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.05 | SC-M03-001/M2; SC-M03-001/M3 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.06 | SC-M03-001/M6; SC-M03-001/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.07 | SC-M03-001/M3; SC-M03-001/M6 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.08 | SC-M03-001/M6; SC-M03-001/E4.1; SC-M03-001/E5.4; SC-M03-001/E7.4; SC-M03-001/E15.4 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.09 | SC-M03-001/M6; SC-M03-001/E4.1; SC-M03-001/E7.4; SC-M03-001/E15.4 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.10 | SC-M03-001/M6; SC-M03-001/E1.1; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.11 | SC-M03-001/M2; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.12 | SC-M03-001/M6; SC-M03-001/E4.1; SC-M03-001/E7.4; SC-M03-001/E15.4 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.13 | SC-M03-001/M6; SC-M03-001/E2.1; SC-M03-001/E4.1; SC-M03-001/E5.4; SC-M03-001/E7.4 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.14 | SC-M03-001/M6; SC-M03-001/E5.4; SC-M03-001/E6.1; SC-M03-001/E6.2; SC-M03-001/E6.3; SC-M03-001/E6.4; SC-M03-001/E6.5; SC-M03-004/M2; SC-M03-004/E7.1; SC-M03-004/E7.2; SC-M03-011/E5.1; SC-M03-011/E5.2; SC-M03-011/E5.3; SC-M03-011/E5.4; SC-M03-011/E5.5; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.15 | SC-M03-001/M6; SC-M03-001/E5.4; SC-M03-001/E6.1; SC-M03-001/E6.2; SC-M03-001/E6.3; SC-M03-001/E6.4; SC-M03-001/E6.5; SC-M03-004/M2; SC-M03-004/E7.1; SC-M03-004/E7.2; SC-M03-011/E5.1; SC-M03-011/E5.2; SC-M03-011/E5.3; SC-M03-011/E5.4; SC-M03-011/E5.5; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.16 | SC-M03-001/M4; SC-M03-001/E6.1; SC-M03-001/E6.2; SC-M03-001/E6.3; SC-M03-001/E6.4; SC-M03-001/E6.5; SC-M03-004/M2; SC-M03-004/E7.1; SC-M03-004/E7.2; SC-M03-011/M2; SC-M03-011/E5.1; SC-M03-011/E5.2; SC-M03-011/E5.3; SC-M03-011/E5.4; SC-M03-011/E5.5; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-01.17 | SC-M03-001/E6.1; SC-M03-001/E6.2; SC-M03-001/E6.3; SC-M03-001/E6.4; SC-M03-001/E6.5; SC-M03-004/M2; SC-M03-004/E7.1; SC-M03-004/E7.2; SC-M03-011/E5.1; SC-M03-011/E5.2; SC-M03-011/E5.3; SC-M03-011/E5.4; SC-M03-011/E5.5; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-02.01 | SC-M03-001/E7.1; SC-M03-001/E7.2; SC-M03-001/E7.3; SC-M03-001/E7.4; SC-M03-001/E8.3; SC-M03-001/E9.3; SC-M03-001/E10.3; SC-M03-001/E11.3; SC-M03-001/E12.3; SC-M03-001/E13.3; SC-M03-011/E10.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-02.02 | SC-M03-001/E7.2; SC-M03-001/E7.4; SC-M03-011/E10.1; SC-M03-011/E10.2; SC-M03-011/E11.3; SC-M03-011/E12.3; SC-M03-011/E13.3; SC-M03-011/E14.3; SC-M03-011/E15.3; SC-M03-011/E16.3 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-02.03 | SC-M03-001/E7.2; SC-M03-001/E7.4; SC-M03-007/M2; SC-M03-011/E10.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-02.04 | SC-M03-001/E7.2; SC-M03-001/E7.4; SC-M03-001/E8.1; SC-M03-001/E8.2; SC-M03-011/E10.2; SC-M03-011/E11.1; SC-M03-011/E11.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-02.05 | SC-M03-001/E7.2; SC-M03-001/E7.4; SC-M03-001/E9.1; SC-M03-001/E9.2; SC-M03-011/E10.2; SC-M03-011/E12.1; SC-M03-011/E12.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-02.06 | SC-M03-001/E7.2; SC-M03-001/E7.4; SC-M03-001/E10.1; SC-M03-001/E10.2; SC-M03-011/E10.2; SC-M03-011/E13.1; SC-M03-011/E13.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-02.07 | SC-M03-001/E7.2; SC-M03-001/E7.4; SC-M03-001/E11.1; SC-M03-001/E11.2; SC-M03-011/E10.2; SC-M03-011/E14.1; SC-M03-011/E14.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-02.08 | SC-M03-001/E7.2; SC-M03-001/E7.4; SC-M03-001/E12.1; SC-M03-001/E12.2; SC-M03-011/E10.2; SC-M03-011/E15.1; SC-M03-011/E15.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-02.09 | SC-M03-001/E7.2; SC-M03-001/E7.4; SC-M03-001/E13.1; SC-M03-001/E13.2; SC-M03-011/E10.2; SC-M03-011/E16.1; SC-M03-011/E16.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-02.10 | SC-M03-001/E7.2; SC-M03-001/E7.4; SC-M03-011/E10.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-02.11 | SC-M03-001/E7.2; SC-M03-001/E7.4; SC-M03-001/E14.1; SC-M03-011/E1.1; SC-M03-011/E3.1; SC-M03-011/E10.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-03.01 | SC-M03-001/E15.1; SC-M03-001/E15.4 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-03.02 | SC-M03-001/E15.2; SC-M03-001/E15.4 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-03.03 | SC-M03-001/E15.4; SC-M03-001/E16.1; SC-M03-001/E16.2; SC-M03-001/E21.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-03.04 | SC-M03-001/E15.4; SC-M03-001/E17.1; SC-M03-001/E17.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-03.05 | SC-M03-001/E15.2; SC-M03-001/E15.4; SC-M03-001/E21.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-03.06 | SC-M03-001/E15.2; SC-M03-001/E15.4 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-03.07 | SC-M03-001/E15.3; SC-M03-001/E15.4; SC-M03-001/E18.1; SC-M03-001/E18.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-03.08 | SC-M03-001/E15.4; SC-M03-001/E20.1; SC-M03-001/E20.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-03.09 | SC-M03-001/E15.4; SC-M03-001/E19.1; SC-M03-001/E19.2; SC-M03-001/E21.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-03.10 | SC-M03-001/E15.4; SC-M03-001/E21.1; SC-M03-001/E21.2; SC-M03-001/E22.1; SC-M03-001/E22.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-03.11 | SC-M03-001/E15.4; SC-M03-011/M2; SC-M03-020/E4.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-04.01 | SC-M03-004/M1; SC-M03-004/M2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-04.02 | SC-M03-004/M2; SC-M03-004/E11.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-04.03 | SC-M03-004/E8.1; SC-M03-004/E9.1; SC-M03-004/E10.1; RULE-M03-005 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-04.04 | SC-M03-004/E9.1; SC-M03-004/E13.1; SC-M03-004/E26.3; SC-M03-011/E7.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-04.05 | SC-M03-004/E18.1; SC-M03-004/E19.1; SC-M03-004/E20.1; SC-M03-004/E21.1; SC-M03-004/E22.1; SC-M03-004/E23.1; SC-M03-004/E24.1; SC-M03-004/E28.1; SC-M03-004/E29.1; SC-M03-004/V3.1; SC-M03-004/V4.1; RULE-M03-GROUP | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-04.06 | SC-M03-004/M2; SC-M03-004/E1.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-04.07 | SC-M03-004/M2; SC-M03-004/E2.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-04.08 | SC-M03-004/M2; SC-M03-004/E4.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-04.09 | SC-M03-004/M2; SC-M03-004/E5.1; SC-M03-004/E10.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-04.10 | SC-M03-004/M2; SC-M03-004/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-04.11 | SC-M03-004/V2.1; SC-M03-004/V2.2; RULE-M03-005 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.01 | SC-M03-004/M4; SC-M03-004/E14.4; AUT-M03-001; RULE-M03-005 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.02 | SC-M03-004/E11.2; SC-M03-004/E16.4; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.03 | SC-M03-004/E12.2; SC-M03-004/E17.4; SC-M03-004/E26.2; SC-M03-004/E27.2; AUT-M03-001; RULE-M03-005 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.04 | SC-M03-004/E15.4; SC-M03-004/E28.5; SC-M03-004/E29.5; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.05 | SC-M03-011/M4; SC-M03-017/E4.1; SC-M03-017/E5.1; SC-M03-017/E7.1; SC-M03-017/E8.1; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.06 | SC-M03-011/M4; SC-M03-017/E4.1; SC-M03-017/E5.1; SC-M03-017/E7.1; SC-M03-017/E8.1; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.07 | SC-M03-011/E9.2; SC-M03-017/E5.3; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.08 | SC-M03-004/E8.1; SC-M03-011/E8.1; SC-M03-017/E6.1; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.09 | SC-M03-011/E8.1; SC-M03-017/E6.1; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.10 | SC-M03-011/M6; SC-M03-011/E18.4; SC-M03-017/E4.3; SC-M03-017/E7.5; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.11 | SC-M03-011/E19.4; SC-M03-017/E8.5; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.12 | SC-M03-004/E12.2; SC-M03-004/E17.4; SC-M03-004/E26.2; SC-M03-004/E27.2; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.13 | SC-M03-004/E12.2; SC-M03-004/E13.1; SC-M03-004/E26.3; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.14 | SC-M03-011/E6.1; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-05.15 | SC-M03-004/V2.2; SC-M03-011/V2.4; SC-M03-017/V2.2; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-06.01 | SC-M03-006/M1; SC-M03-006/M2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-06.02 | SC-M03-006/M3; SC-M03-006/M4; RULE-M03-005 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-06.03 | SC-M03-006/E1.1; SC-M03-006/E1.2; SC-M03-006/E2.3; SC-M03-006/E2.4; RULE-M03-005 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-06.04 | SC-M03-006/E2.1; SC-M03-006/E2.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-06.05 | SC-M03-006/E1.2; SC-M03-006/E2.4; SC-M03-007/E5.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-06.06 | SC-M03-006/M2; SC-M03-006/M4; SC-M03-006/E1.2; SC-M03-006/E2.4; SC-M03-006/E3.1; SC-M03-006/E4.1; SC-M03-006/V2.1; SC-M03-006/V2.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-06.07 | SC-M03-006/M4; SC-M03-006/E1.2; SC-M03-006/E2.4; SC-M03-006/E5.1; SC-M03-015/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-07.01 | SC-M03-007/M1; SC-M03-007/M2; SC-M03-007/E3.1; SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.1; SC-M03-007/V1.1; SC-M03-007/V1.2; SC-M03-007/V2.1; SC-M03-007/V2.2; SC-M03-012/V2.1; SC-M03-012/V2.2; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-07.02 | SC-M03-007/M2; SC-M03-007/E1.1; SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.1; SC-M03-007/V1.2; SC-M03-007/V2.1; SC-M03-007/V2.2; SC-M03-012/V2.1; SC-M03-012/V2.2; SC-M03-018/V2.2; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-07.03 | SC-M03-007/M2; SC-M03-007/E5.1; SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.1; SC-M03-007/V1.2; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-07.04 | SC-M03-007/M2; SC-M03-007/E5.1; SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.1; SC-M03-007/V1.2; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-07.05 | SC-M03-007/M2; SC-M03-007/E4.1; SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.1; SC-M03-007/V1.2; SC-M03-007/V2.2; SC-M03-012/V2.2; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-07.06 | SC-M03-001/V1.1; SC-M03-001/V1.2; SC-M03-004/V1.1; SC-M03-004/V1.2; SC-M03-006/V1.1; SC-M03-006/V1.2; SC-M03-008/V1.1; SC-M03-008/V1.2; SC-M03-009/V1.1; SC-M03-009/V1.2; SC-M03-011/V1.1; SC-M03-011/V1.2; SC-M03-013/V1.1; SC-M03-013/V1.2; SC-M03-014/V1.1; SC-M03-014/V1.2; SC-M03-015/V1.1; SC-M03-015/V1.2; SC-M03-016/V1.1; SC-M03-016/V1.2; SC-M03-017/V1.1; SC-M03-017/V1.2; SC-M03-018/V1.1; SC-M03-018/V1.2; SC-M03-019/V1.1; SC-M03-019/V1.2; SC-M03-020/V1.1; SC-M03-020/V1.2; SC-M03-021/V1.1; SC-M03-021/V1.2; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-07.07 | SC-M03-007/M2; SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.1; SC-M03-007/V1.2; SC-M03-018/V3.1; SC-M03-018/V3.2; SC-M03-018/V4.1; SC-M03-018/V4.2; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-07.08 | SC-M03-018/M1; SC-M03-018/M2; SC-M03-018/E2.1; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-07.09 | SC-M03-018/M2; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-07.10 | SC-M03-018/M2; SC-M03-018/E1.1; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-07.11 | SC-M03-018/V2.1; SC-M03-018/V2.2; SC-M03-018/V3.1; SC-M03-018/V3.2; SC-M03-018/V4.1; SC-M03-018/V4.2; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-08.01 | SC-M03-007/E8.2; SC-M03-007/E8.3; SC-M03-008/M1; SC-M03-008/M2; SC-M03-008/E6.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-08.02 | SC-M03-008/E5.1; SC-M03-008/E5.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-08.03 | SC-M03-007/E8.3; SC-M03-008/M1; SC-M03-008/M2; SC-M03-008/E5.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-08.04 | SC-M03-008/E3.1; SC-M03-008/E3.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-08.05 | SC-M03-008/E4.1; SC-M03-008/E4.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-08.06 | SC-M03-008/E1.1; SC-M03-019/M2; AUT-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-08.07 | SC-M03-007/M2; SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.1; SC-M03-007/V1.2; SC-M03-008/E4.2; RULE-M03-003 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-08.08 | SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/V1.2; RULE-M03-003 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-08.09 | SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.3; SC-M03-007/V1.2; SC-M03-008/M2; SC-M03-008/E3.2; RULE-M03-003 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-08.10 | SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/V1.2; SC-M03-019/M2; AUT-M03-002; RULE-M03-003 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-08.11 | SC-M03-008/M2; SC-M03-008/E6.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-08.12 | SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.3; SC-M03-007/V1.2; SC-M03-008/M2; SC-M03-008/E3.2; SC-M03-019/M2; RULE-M03-003 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-08.13 | SC-M03-007/E8.3; SC-M03-008/M2; SC-M03-008/E2.1; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-09.01 | SC-M03-009/M1; SC-M03-009/M2; SC-M03-009/E1.1; SC-M03-009/E5.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-09.02 | SC-M03-009/E5.1; SC-M03-019/M1; SC-M03-019/M2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-09.03 | SC-M03-009/M2; SC-M03-009/E3.1; SC-M03-019/E2.1; SC-M03-020/E2.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-09.04 | SC-M03-009/M2; SC-M03-009/E2.1; SC-M03-019/M2; SC-M03-019/E1.1; SC-M03-020/M2; SC-M03-020/E1.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-09.05 | SC-M03-009/M2; SC-M03-009/E4.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-09.06 | SC-M03-020/M1; SC-M03-020/M2; SC-M03-020/E5.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-09.07 | SC-M03-020/M2; SC-M03-020/E3.1; SC-M03-020/E5.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-09.08 | SC-M03-009/E3.1; SC-M03-019/E2.1; SC-M03-020/M2; SC-M03-020/E2.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-10.01 | AUT-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-10.02 | SC-M03-009/E5.1; SC-M03-019/M2; AUT-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-11.01 | SC-M03-011/M1; SC-M03-011/M2; SC-M03-011/M3; SC-M03-011/M4; SC-M03-011/E6.1; SC-M03-011/E7.1; SC-M03-011/E10.1; SC-M03-011/E10.3; SC-M03-011/E11.3; SC-M03-011/E12.3; SC-M03-011/E13.3; SC-M03-011/E14.3; SC-M03-011/E15.3; SC-M03-011/E16.3; SC-M03-011/V2.1; SC-M03-011/V2.2; SC-M03-011/V2.3 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-11.02 | SC-M03-011/M4; SC-M03-011/M6; SC-M03-011/E6.1; SC-M03-011/E7.1; SC-M03-011/E8.1; SC-M03-011/V2.4; RULE-M03-005 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-11.03 | SC-M03-011/M4 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-11.04 | SC-M03-011/M2; SC-M03-011/M4; SC-M03-011/E1.1; SC-M03-011/E3.1; SC-M03-011/V2.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-11.05 | RULE-M03-005 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-11.06 | RULE-M03-005 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-11.07 | SC-M03-011/M2; SC-M03-011/M4; SC-M03-011/E2.1; SC-M03-011/E4.1; SC-M03-011/V2.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-12.01 | SC-M03-007/M2; SC-M03-007/E9.1; SC-M03-011/M4; SC-M03-011/M6; SC-M03-011/V2.4; SC-M03-012/M2; RULE-M03-005 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-12.02 | SC-M03-007/E9.2; SC-M03-007/E9.3; SC-M03-012/M1; SC-M03-012/M2; SC-M03-012/V1.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-12.03 | SC-M03-007/E9.3; SC-M03-012/M2; SC-M03-012/V1.1; SC-M03-012/V1.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-12.04 | SC-M03-007/E9.3; SC-M03-007/V2.1; SC-M03-007/V2.2; SC-M03-012/M2; SC-M03-012/E1.1; SC-M03-012/V1.2; SC-M03-012/V2.1; SC-M03-012/V2.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-13.01 | SC-M03-013/M1; SC-M03-013/M2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-13.02 | SC-M03-017/M1; SC-M03-017/M2; SC-M03-017/E2.1; SC-M03-017/E4.1; SC-M03-017/E5.1; SC-M03-017/E6.1; SC-M03-017/E7.1; SC-M03-017/E8.1; SC-M03-017/V2.1; SC-M03-017/V2.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-13.03 | SC-M03-013/M2; SC-M03-013/E1.1; SC-M03-017/M2; SC-M03-017/E1.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-13.04 | SC-M03-013/M2; SC-M03-013/E2.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-13.05 | SC-M03-017/M2; SC-M03-017/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-13.06 | SC-M03-017/M2; SC-M03-017/E4.1; SC-M03-017/E5.1; SC-M03-017/E6.1; SC-M03-017/E7.1; SC-M03-017/E8.1; SC-M03-017/V2.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-14.01 | SC-M03-014/M1; SC-M03-014/M2; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-14.02 | SC-M03-014/V2.1; SC-M03-014/V2.2; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-14.03 | SC-M03-014/V3.1; SC-M03-014/V3.2; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-14.04 | SC-M03-014/M2; SC-M03-014/V2.2; SC-M03-014/V3.2; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-14.05 | SC-M03-014/M2; SC-M03-014/V2.2; SC-M03-014/V3.2; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-14.06 | SC-M03-014/V2.2; SC-M03-014/V3.2; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-14.07 | SC-M03-021/M1; SC-M03-021/M2; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-14.08 | SC-M03-021/V2.1; SC-M03-021/V2.2; SC-M03-021/V3.1; SC-M03-021/V3.2; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-14.09 | SC-M03-014/E1.1; SC-M03-021/E1.1; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-14.10 | SC-M03-014/E3.1; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-14.11 | SC-M03-014/E2.1; SC-M03-021/E2.1; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-14.12 | SC-M03-014/V2.2; SC-M03-014/V3.2; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-15.01 | SC-M03-015/M1; SC-M03-015/M2; SC-M03-015/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-15.02 | SC-M03-015/M2; SC-M03-015/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-15.03 | SC-M03-015/M2; SC-M03-015/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-15.04 | SC-M03-015/M2; SC-M03-015/E1.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-15.05 | SC-M03-015/M2; SC-M03-015/E2.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-15.06 | SC-M03-015/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-16.01 | SC-M03-016/M1; SC-M03-016/M2; SC-M03-016/E4.1; SC-M03-016/E5.1; SC-M03-016/E6.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-16.02 | SC-M03-015/M2; SC-M03-016/M2; AUT-M03-003 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-16.03 | SC-M03-016/M2; SC-M03-016/E1.1; AUT-M03-003 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-16.04 | SC-M03-016/M2; SC-M03-016/E2.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-16.05 | SC-M03-016/M2; SC-M03-016/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-16.06 | SC-M03-016/E5.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-17.01 | AUT-M03-003 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-17.02 | SC-M03-018/M2; SC-M03-018/V2.2; AUT-M03-003 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-17.03 | SC-M03-018/M2; AUT-M03-003 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| FR-M03-17.04 | SC-M03-018/E2.1; SC-M03-018/V2.1; SC-M03-018/V2.2; SC-M03-018/V3.1; SC-M03-018/V3.2; SC-M03-018/V4.1; SC-M03-018/V4.2; AUT-M03-003 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-01 | SC-M03-001/M2; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-02 | SC-M03-001/M2; SC-M03-001/E8.2; SC-M03-001/E9.2; SC-M03-001/E10.2; SC-M03-001/E11.2; SC-M03-001/E12.2; SC-M03-001/E13.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-03 | SC-M03-001/M2; SC-M03-001/M4; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-04 | SC-M03-001/M2; SC-M03-001/M4; SC-M03-001/E7.2; SC-M03-001/E7.4; SC-M03-007/M2; SC-M03-011/E10.2; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-05 | SC-M03-001/M2; SC-M03-001/M4; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-06 | SC-M03-001/M2; SC-M03-001/M6; SC-M03-001/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-07 | SC-M03-001/E7.1; SC-M03-001/E7.2; SC-M03-001/E7.4; SC-M03-001/E8.2; SC-M03-001/E9.2; SC-M03-001/E10.2; SC-M03-001/E11.2; SC-M03-001/E12.2; SC-M03-001/E13.2; SC-M03-011/E10.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-08 | SC-M03-001/E7.1; SC-M03-001/E7.2; SC-M03-001/E7.4; SC-M03-001/E8.2; SC-M03-001/E9.2; SC-M03-001/E10.2; SC-M03-001/E11.2; SC-M03-001/E12.2; SC-M03-001/E13.2; SC-M03-011/E10.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-09 | SC-M03-001/E15.4 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-10 | SC-M03-001/E15.2; SC-M03-001/E15.4; SC-M03-008/M1; SC-M03-008/E5.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-11 | SC-M03-001/E15.2; SC-M03-001/E15.4; SC-M03-001/E21.2; SC-M03-007/E8.3; SC-M03-008/M1; SC-M03-008/E5.1; SC-M03-008/E5.2; SC-M03-020/E4.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-12 | SC-M03-001/E15.4; SC-M03-009/M2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-13 | SC-M03-008/E1.1; SC-M03-009/E3.1; SC-M03-009/E5.1; SC-M03-019/M2; SC-M03-019/E2.1; SC-M03-020/E2.1; AUT-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-14 | SC-M03-009/M2; SC-M03-009/E1.1; SC-M03-009/E3.1; SC-M03-009/E5.1; SC-M03-019/M2; SC-M03-019/E2.1; SC-M03-020/E2.1; AUT-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-15 | SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.3; SC-M03-007/V1.2; SC-M03-008/M2; SC-M03-019/M2; AUT-M03-002; RULE-M03-003 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-16 | SC-M03-008/E3.2; SC-M03-008/E4.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-17 | SC-M03-001/M6; SC-M03-007/M2; SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.1; SC-M03-007/V1.2; SC-M03-014/M2; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-18 | SC-M03-007/M2; SC-M03-007/E1.1; SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.1; SC-M03-007/V1.2; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-19 | SC-M03-004/M2; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-20 | SC-M03-004/M4; SC-M03-004/E11.2; SC-M03-004/E12.2; SC-M03-004/E14.4; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-21 | SC-M03-004/E15.4; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-22 | SC-M03-004/E8.1; SC-M03-011/E8.1; SC-M03-017/E6.1; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-23 | SC-M03-006/M4; SC-M03-006/E1.2; SC-M03-006/E2.4 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-24 | SC-M03-004/E9.1; SC-M03-004/E13.1; SC-M03-004/E26.3; SC-M03-011/E7.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-25 | SC-M03-004/E18.1; SC-M03-004/E19.1; SC-M03-004/E20.1; SC-M03-004/E21.1; SC-M03-004/E22.1; SC-M03-004/E23.1; SC-M03-004/E24.1; SC-M03-004/E28.5; SC-M03-004/E29.5; SC-M03-006/M2; RULE-M03-GROUP | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-26 | SC-M03-011/M4; SC-M03-011/M6; SC-M03-011/E6.1; SC-M03-011/E9.2; SC-M03-011/E18.4; SC-M03-011/E19.4; SC-M03-017/M2; SC-M03-017/E4.1; SC-M03-017/E4.3; SC-M03-017/E5.1; SC-M03-017/E5.3; SC-M03-017/E6.1; SC-M03-017/E7.1; SC-M03-017/E7.5; SC-M03-017/E8.1; SC-M03-017/E8.5; AUT-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-27 | SC-M03-007/E9.3; SC-M03-011/M4; SC-M03-011/M6; SC-M03-011/E6.1; SC-M03-011/E7.1; SC-M03-011/E8.1; SC-M03-012/M2; SC-M03-012/V1.2; RULE-M03-005 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-28 | RULE-M03-005 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-29 | SC-M03-013/M2; SC-M03-017/M2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-30 | SC-M03-014/M2; SC-M03-014/V2.2; SC-M03-014/V3.2; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-31 | SC-M03-014/V2.2; SC-M03-014/V3.2; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-32 | SC-M03-014/M2; SC-M03-014/E1.1; SC-M03-014/V2.2; SC-M03-014/V3.2; SC-M03-021/M2; SC-M03-021/E1.1; SC-M03-021/V2.2; SC-M03-021/V3.2; RULE-M03-004 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-33 | SC-M03-017/M2; SC-M03-017/E1.1; SC-M03-017/E2.1; SC-M03-017/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-34 | SC-M03-015/M2; SC-M03-015/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-35 | SC-M03-015/M2; SC-M03-016/M2; SC-M03-016/E1.1; SC-M03-016/E2.1; SC-M03-016/E3.1; SC-M03-016/E5.1; SC-M03-016/E6.1; AUT-M03-003 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-36 | SC-M03-016/M2; SC-M03-016/E1.1; SC-M03-016/E2.1; SC-M03-016/E3.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-37 | SC-M03-018/M2; SC-M03-018/V2.2; AUT-M03-003; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-38 | SC-M03-001/M6; SC-M03-001/E1.1; SC-M03-011/M4; SC-M03-016/M2; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-39 | SC-M03-007/M2; SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.1; SC-M03-007/V1.2; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-40 | SC-M03-004/M2; SC-M03-004/E10.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-41 | SC-M03-001/M6; SC-M03-001/E2.1; SC-M03-001/E4.1; SC-M03-001/E5.4 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-42 | SC-M03-001/M4; SC-M03-001/M6; SC-M03-001/E5.4; SC-M03-001/E6.1; SC-M03-001/E6.2; SC-M03-001/E6.3; SC-M03-001/E6.4; SC-M03-001/E6.5; SC-M03-004/M2; SC-M03-004/E7.1; SC-M03-004/E7.2; SC-M03-011/E5.1; SC-M03-011/E5.2; SC-M03-011/E5.3; SC-M03-011/E5.4; SC-M03-011/E5.5; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-43 | SC-M03-001/M4; SC-M03-001/E6.1; SC-M03-001/E6.2; SC-M03-001/E6.3; SC-M03-001/E6.4; SC-M03-001/E6.5; SC-M03-004/M2; SC-M03-004/E7.1; SC-M03-004/E7.2; SC-M03-011/E5.1; SC-M03-011/E5.2; SC-M03-011/E5.3; SC-M03-011/E5.4; SC-M03-011/E5.5; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-44 | SC-M03-001/E15.4; SC-M03-001/E21.2; SC-M03-001/E22.2; SC-M03-009/E3.1; SC-M03-019/E2.1; SC-M03-020/M2; SC-M03-020/E2.1; SC-M03-020/E4.1; SC-M03-020/E5.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-45 | SC-M03-008/M2; SC-M03-008/E6.1 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-46 | SC-M03-004/E12.2; SC-M03-004/E13.1; SC-M03-004/E17.4; SC-M03-004/E26.2; SC-M03-004/E26.3; SC-M03-004/E27.2; SC-M03-004/E27.3; SC-M03-004/E27.4; RULE-M03-005 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-47 | SC-M03-001/E5.1; SC-M03-001/E5.2; SC-M03-001/E5.4; SC-M03-011/M2; SC-M03-011/M4; SC-M03-011/E2.1; SC-M03-011/E4.1; SC-M03-011/E7.1; SC-M03-011/V2.2 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-48 | SC-M03-001/M6 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-49 | SC-M03-007/M2; SC-M03-007/E1.1; SC-M03-007/E5.1; SC-M03-007/E6.1; SC-M03-007/E7.1; SC-M03-007/E8.1; SC-M03-007/V1.2; SC-M03-018/E2.1; SC-M03-018/V2.2; SC-M03-018/V3.2; SC-M03-018/V4.2; RULE-M03-001 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-50 | SC-M03-001/M2; RULE-M03-002 | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |
| BR-M03-51 | SC-M03-004/V2.2; SC-M03-004/V3.1; SC-M03-004/V4.1; SC-M03-011/V2.4; SC-M03-017/V2.2; AUT-M03-001; RULE-M03-GROUP | Có vị trí triển khai theo nguồn; cần review ngữ nghĩa |


| UC | Guard/lựa chọn | Vị trí | Điểm tiếp tục |
|---|---|---|---|
| UC-M03-001 | Tác giả đang MEDIUM hoặc HEAVY khi lưu nháp mới | SC-M03-001/E1 | END:REJECTED |
| UC-M03-001 | Cả tiêu đề, nội dung, poll, tệp đều trống | SC-M03-001/E2 | END:REJECTED |
| UC-M03-001 | Lớp/Khối bài ngoài 10,11,12 và không trống | SC-M03-001/E3 | END:REJECTED |
| UC-M03-001 | Nháp chỉ có một thành phần hợp lệ trong tiêu đề/nội dung/poll/tệp | SC-M03-001/E4 | END:SUCCESS |
| UC-M03-001 | Tác giả mở và cập nhật bài Nháp đã lưu trước đó | SC-M03-001/E5 | END:SUCCESS |
| UC-M03-001 | Trong lúc nhập, tiêu đề 151 ký tự hoặc nội dung 6001 từ | SC-M03-001/E6 | M6 |
| UC-M03-001 | Tại EP-DRAFT-ATTACH, tác giả chọn thêm rồi bỏ tệp trước khi lưu | SC-M03-001/E7 | END:SUCCESS |
| UC-M03-001 | EP-DRAFT-ATTACH: Ảnh sai định dạng | SC-M03-001/E8 | M6 |
| UC-M03-001 | EP-DRAFT-ATTACH: Ảnh quá dung lượng | SC-M03-001/E9 | M6 |
| UC-M03-001 | EP-DRAFT-ATTACH: Thêm ảnh thứ 11 | SC-M03-001/E10 | M6 |
| UC-M03-001 | EP-DRAFT-ATTACH: Tài liệu sai loại | SC-M03-001/E11 | M6 |
| UC-M03-001 | EP-DRAFT-ATTACH: Tài liệu quá dung lượng | SC-M03-001/E12 | M6 |
| UC-M03-001 | EP-DRAFT-ATTACH: Thêm tài liệu thứ 4 | SC-M03-001/E13 | M6 |
| UC-M03-001 | Yêu cầu lưu kèm thêm/bỏ tệp do người khác tác giả gửi | SC-M03-001/E14 | END:REJECTED |
| UC-M03-001 | Tại EP-DRAFT-POLL, tác giả muốn poll thay vì chỉ văn bản | SC-M03-001/E15 | END:SUCCESS |
| UC-M03-001 | EP-DRAFT-POLL: Số lựa chọn không hợp lệ | SC-M03-001/E16 | END:REJECTED |
| UC-M03-001 | EP-DRAFT-POLL: Thêm poll thứ hai | SC-M03-001/E17 | END:REJECTED |
| UC-M03-001 | EP-DRAFT-POLL: Thiếu hạn | SC-M03-001/E18 | END:REJECTED |
| UC-M03-001 | EP-DRAFT-POLL: Hạn trước hiện tại | SC-M03-001/E19 | END:REJECTED |
| UC-M03-001 | EP-DRAFT-POLL: Người tạo khác tác giả | SC-M03-001/E20 | END:REJECTED |
| UC-M03-001 | Trong khi còn nháp, tác giả chọn sửa poll đang có | SC-M03-001/E21 | M6 |
| UC-M03-001 | Trong khi còn nháp, tác giả chọn bỏ poll | SC-M03-001/E22 | M6 |
| UC-M03-004 | Không phải tác giả | SC-M03-004/E1 | END:REJECTED |
| UC-M03-004 | Sai trạng thái | SC-M03-004/E2 | END:REJECTED |
| UC-M03-004 | Tác giả MEDIUM/HEAVY | SC-M03-004/E3 | END:REJECTED |
| UC-M03-004 | Thiếu tiêu đề | SC-M03-004/E4 | END:REJECTED |
| UC-M03-004 | Không nội dung và không poll | SC-M03-004/E5 | END:REJECTED |
| UC-M03-004 | Không có Topic hoặc Topic đã bị xóa | SC-M03-004/E6 | END:REJECTED |
| UC-M03-004 | Vượt giới hạn khi gửi; tác giả sửa rồi gửi lại | SC-M03-004/E7 | M2 |
| UC-M03-004 | Một trong hai cờ AI tắt | SC-M03-004/E8 | END:SUCCESS |
| UC-M03-004 | Bài bị từ chối đã được tác giả sửa rồi gửi lại với hai cờ tắt | SC-M03-004/E9 | END:SUCCESS |
| UC-M03-004 | Bài có tiêu đề và poll hợp lệ nhưng nội dung trống; hai cờ tắt | SC-M03-004/E10 | END:SUCCESS |
| UC-M03-004 | AI trả score trong [0.5,0.9), ví dụ 0.5/0.89 | SC-M03-004/E11 | END:SUCCESS |
| UC-M03-004 | AI trả score≥0.9, kể cả đúng 0.9 | SC-M03-004/E12 | END:REJECTED |
| UC-M03-004 | Tác giả chọn sửa và gửi lại bài đã bị AI tự từ chối | SC-M03-004/E13 | M2 |
| UC-M03-004 | Lần quét đầu lỗi, lần thử lại thành công sạch | SC-M03-004/E14 | END:SUCCESS |
| UC-M03-004 | Lần quét đầu lỗi, lần thử lại cũng lỗi | SC-M03-004/E15 | END:SUCCESS |
| UC-M03-004 | Lần quét đầu lỗi, lần thử lại thành công với max=0.6 | SC-M03-004/E16 | END:SUCCESS |
| UC-M03-004 | Lần quét đầu lỗi, lần thử lại thành công với max=0.9 | SC-M03-004/E17 | END:REJECTED |
| UC-M03-004 | Bài nhóm của thành viên khác Owner, điểm sạch và duyệt trước bật | SC-M03-004/E18 | END:SUCCESS |
| UC-M03-004 | Bài nhóm của member, điểm sạch và duyệt trước tắt | SC-M03-004/E19 | END:SUCCESS |
| UC-M03-004 | Bài nhóm của member, điểm nghi ngờ dù duyệt trước tắt | SC-M03-004/E20 | END:SUCCESS |
| UC-M03-004 | Owner gửi bài trong nhóm mình, điểm nghi ngờ | SC-M03-004/E21 | END:SUCCESS |
| UC-M03-004 | Owner gửi bài nhóm mình với điểm sạch | SC-M03-004/E22 | END:SUCCESS |
| UC-M03-004 | Member hoặc Owner bài nhóm có điểm cao | SC-M03-004/E23 | END:REJECTED |
| UC-M03-004 | Bài nhóm khi AI tổng hoặc Moderation tắt | SC-M03-004/E24 | END:SUCCESS |
| UC-M03-004 | Người gửi không còn là thành viên nhóm đích | SC-M03-004/E25 | END:REJECTED |
| UC-M03-004 | Sau khi bị AI tự từ chối, tác giả chọn sửa rồi gửi lại | SC-M03-004/E26 | M2 |
| UC-M03-004 | Sau khi bị AI tự từ chối, tác giả chọn khiếu nại M09 | SC-M03-004/E27 | END:HANDED_OFF |
| UC-M03-004 | Quét bài nhóm member lỗi cả hai lần | SC-M03-004/E28 | END:SUCCESS |
| UC-M03-004 | Quét bài nhóm Owner lỗi cả hai lần | SC-M03-004/E29 | END:SUCCESS |
| UC-M03-006 | Người duyệt chọn từ chối và nhập lý do | SC-M03-006/E1 | END:SUCCESS |
| UC-M03-006 | Người duyệt chọn từ chối nhưng bỏ trống lý do | SC-M03-006/E2 | END:SUCCESS |
| UC-M03-006 | Vai trò Mod/Admin không còn hợp lệ lúc kiểm tra | SC-M03-006/E3 | END:REJECTED |
| UC-M03-006 | Vai trò Mod/Admin không còn hợp lệ lúc kiểm tra | SC-M03-006/E4 | END:REJECTED |
| UC-M03-006 | P301 không còn Chờ duyệt khi quyết định được gửi | SC-M03-006/E5 | END:REJECTED |
| UC-M03-007 | Người khác tác giả không có quyền đọc | SC-M03-007/E1 | END:REJECTED |
| UC-M03-007 | Bài thuộc nhóm Private, người xem không là thành viên | SC-M03-007/E2 | END:REJECTED |
| UC-M03-007 | Bài bị module khác ẩn | SC-M03-007/E3 | END:REJECTED |
| UC-M03-007 | Bài đã xóa hẳn mở bằng URL thường, kể cả tác giả | SC-M03-007/E4 | END:REJECTED |
| UC-M03-007 | Tác giả xem bài của mình chưa bị xóa hẳn | SC-M03-007/E5 | END:SUCCESS |
| UC-M03-007 | Poll mở, người xem đã vote hoặc bật hiện kết quả trước vote | SC-M03-007/E6 | END:SUCCESS |
| UC-M03-007 | Poll đã đóng, bất kể tùy chọn hiện kết quả trước vote | SC-M03-007/E7 | END:SUCCESS |
| UC-M03-007 | EP-READ-VOTE: người đang đọc quyết định vote | SC-M03-007/E8 | END:SUCCESS |
| UC-M03-007 | EP-READ-HISTORY: người xem chọn lịch sử sau khi bài đã được trả | SC-M03-007/E9 | END:SUCCESS |
| UC-M03-008 | Poll đã đóng, gồm thời điểm đúng hạn | SC-M03-008/E1 | END:REJECTED |
| UC-M03-008 | Bài Khóa toàn bộ | SC-M03-008/E2 | END:REJECTED |
| UC-M03-008 | Người đã vote chọn đổi phiếu khi poll còn mở | SC-M03-008/E3 | END:SUCCESS |
| UC-M03-008 | Người đã vote muốn bỏ chọn trong khi poll còn mở | SC-M03-008/E4 | END:SUCCESS |
| UC-M03-008 | Phiếu không đúng chế độ hoặc chứa lựa chọn không có sẵn | SC-M03-008/E5 | M2 |
| UC-M03-008 | Tác giả bình chọn poll của chính bài mình | SC-M03-008/E6 | END:SUCCESS |
| UC-M03-009 | Tác giả dời hạn sớm hơn nhưng vẫn sau hiện tại | SC-M03-009/E1 | END:SUCCESS |
| UC-M03-009 | Người thao tác không phải tác giả | SC-M03-009/E2 | END:REJECTED |
| UC-M03-009 | Poll đã đóng | SC-M03-009/E3 | END:REJECTED |
| UC-M03-009 | Hạn mới trước hiện tại | SC-M03-009/E4 | END:REJECTED |
| UC-M03-009 | Hạn mới đúng thời điểm hiện tại | SC-M03-009/E5 | END:SUCCESS |
| UC-M03-011 | Người sửa khác tác giả | SC-M03-011/E1 | END:REJECTED |
| UC-M03-011 | Bài Chờ duyệt/Đã xóa hoặc kiểm duyệt Bị Mod ẩn | SC-M03-011/E2 | END:REJECTED |
| UC-M03-011 | Người sửa khác tác giả | SC-M03-011/E3 | END:REJECTED |
| UC-M03-011 | Bài Chờ duyệt/Đã xóa hoặc kiểm duyệt Bị Mod ẩn | SC-M03-011/E4 | END:REJECTED |
| UC-M03-011 | Tác giả nhập vượt giới hạn trong lúc sửa | SC-M03-011/E5 | M4 |
| UC-M03-011 | Sửa bài Tự ẩn trong lúc ẩn | SC-M03-011/E6 | END:SUCCESS |
| UC-M03-011 | Sửa bài Bị từ chối nhưng chưa gửi lại | SC-M03-011/E7 | END:SUCCESS |
| UC-M03-011 | Sửa Đã đăng nhưng một trong hai cờ AI tắt | SC-M03-011/E8 | END:SUCCESS |
| UC-M03-011 | Quét lại trả score≥0.5, kể cả ≥0.9 | SC-M03-011/E9 | END:SUCCESS |
| UC-M03-011 | EP-EDIT-ATTACH: tác giả thay tệp khi sửa | SC-M03-011/E10 | M4 |
| UC-M03-011 | EP-EDIT-ATTACH: Ảnh sai loại | SC-M03-011/E11 | M4 |
| UC-M03-011 | EP-EDIT-ATTACH: Ảnh quá 5 MB | SC-M03-011/E12 | M4 |
| UC-M03-011 | EP-EDIT-ATTACH: Ảnh thứ11 | SC-M03-011/E13 | M4 |
| UC-M03-011 | EP-EDIT-ATTACH: Tài liệu sai loại | SC-M03-011/E14 | M4 |
| UC-M03-011 | EP-EDIT-ATTACH: Tài liệu quá20 MB | SC-M03-011/E15 | M4 |
| UC-M03-011 | EP-EDIT-ATTACH: Tài liệu thứ4 | SC-M03-011/E16 | M4 |
| UC-M03-011 | Bộ Topic sau sửa trống hoặc quá3 | SC-M03-011/E17 | END:REJECTED |
| UC-M03-011 | Quét lại lỗi lần đầu, lần thử lại sạch | SC-M03-011/E18 | END:SUCCESS |
| UC-M03-011 | Quét lại lỗi lần đầu, lần thử lại cũng lỗi | SC-M03-011/E19 | END:SUCCESS |
| UC-M03-012 | Người xem không còn quyền xem bài theo trạng thái/nhóm | SC-M03-012/E1 | END:REJECTED |
| UC-M03-013 | Không phải tác giả | SC-M03-013/E1 | END:REJECTED |
| UC-M03-013 | Bài không Đã đăng | SC-M03-013/E2 | END:REJECTED |
| UC-M03-014 | Người khóa là Mod/Admin và tác giả muốn mở hoặc đổi mức | SC-M03-014/E1 | END:REJECTED |
| UC-M03-014 | Người yêu cầu không là tác giả, Mod hoặc Admin | SC-M03-014/E2 | END:REJECTED |
| UC-M03-014 | Người không phải Mod/Admin yêu cầu Khóa toàn bộ | SC-M03-014/E3 | END:REJECTED |
| UC-M03-015 | Không phải tác giả | SC-M03-015/E1 | END:REJECTED |
| UC-M03-015 | Bài đã Đã xóa | SC-M03-015/E2 | END:REJECTED |
| UC-M03-015 | Bài đang Chờ duyệt và nằm trong hàng Mod hệ thống | SC-M03-015/E3 | END:SUCCESS |
| UC-M03-016 | Hết hạn, kể cả đúng mốc 7×24h | SC-M03-016/E1 | END:REJECTED |
| UC-M03-016 | Bị Mod ẩn | SC-M03-016/E2 | END:REJECTED |
| UC-M03-016 | Không phải tác giả | SC-M03-016/E3 | END:REJECTED |
| UC-M03-016 | Bài không ở trạng thái Đã xóa | SC-M03-016/E4 | END:REJECTED |
| UC-M03-016 | Trước khi xóa, bài đang Chờ duyệt | SC-M03-016/E5 | END:SUCCESS |
| UC-M03-016 | Trạng thái trước xóa là Nháp/Bị từ chối/Tự ẩn | SC-M03-016/E6 | END:SUCCESS |
| UC-M03-017 | Không phải tác giả | SC-M03-017/E1 | END:REJECTED |
| UC-M03-017 | Bài không Tự ẩn | SC-M03-017/E2 | END:REJECTED |
| UC-M03-017 | Kiểm duyệt Bị Mod ẩn | SC-M03-017/E3 | END:REJECTED |
| UC-M03-017 | Tác giả khác Admin đã sửa lúc ẩn, hai cờ bật | SC-M03-017/E4 | END:SUCCESS |
| UC-M03-017 | Bài tự ẩn đã sửa, quét lại cho điểm≥0.5 | SC-M03-017/E5 | END:SUCCESS |
| UC-M03-017 | Bài tự ẩn đã sửa nhưng một trong hai cờ AI tắt | SC-M03-017/E6 | END:SUCCESS |
| UC-M03-017 | Quét lại lỗi lần đầu, lần thử lại sạch | SC-M03-017/E7 | END:SUCCESS |
| UC-M03-017 | Quét lại lỗi lần đầu, lần thử lại cũng lỗi | SC-M03-017/E8 | END:SUCCESS |
| UC-M03-018 | Người mở không phải tác giả trên đường xem lại dành cho tác giả | SC-M03-018/E1 | END:REJECTED |
| UC-M03-018 | Không có thông báo/khiếu nại hợp lệ liên quan bài | SC-M03-018/E2 | END:REJECTED |
| UC-M03-009 | Người thao tác không phải tác giả | SC-M03-019/E1 | END:REJECTED |
| UC-M03-009 | Poll đã đóng | SC-M03-019/E2 | END:REJECTED |
| UC-M03-009 | Người thao tác không phải tác giả | SC-M03-020/E1 | END:REJECTED |
| UC-M03-009 | Poll đã đóng | SC-M03-020/E2 | END:REJECTED |
| UC-M03-009 | Thêm lựa chọn khiến tổng vượt 10 | SC-M03-020/E3 | END:REJECTED |
| UC-M03-009 | Tác giả yêu cầu thêm/bỏ cả poll, sửa/xóa lựa chọn cũ hoặc đổi cấu hình sau gửi | SC-M03-020/E4 | END:REJECTED |
| UC-M03-009 | Thêm lựa chọn thứ10 khi poll còn mở | SC-M03-020/E5 | END:SUCCESS |
| UC-M03-014 | Người khóa là Mod/Admin và tác giả muốn mở hoặc đổi mức | SC-M03-021/E1 | END:REJECTED |
| UC-M03-014 | Người yêu cầu không là tác giả, Mod hoặc Admin | SC-M03-021/E2 | END:REJECTED |


Truy vết ngược nằm tại sources của từng bước. V là đường thay toàn bộ theo actor khác trong cùng mục tiêu; không tạo thêm BF và không nối một bước Guest vào giữa đường User. Hậu điều kiện áp theo kết quả và dữ liệu cụ thể trong nhánh, không áp đồng thời mọi snapshot.

## 7. Giới hạn nguồn và trạng thái

| ID nguồn | Phạm vi/giới hạn | Cách xử lý |
|---|---|---|
| TBD-M03-01 / OPEN-005 | Đếm lượt xem không làm MS1 | Đọc bài không tự tạo lượt xem hoặc AUT đếm. |
| TBD-M03-02 / OPEN-006 | SSR/SEO và xem trước link chưa tối ưu | Không tạo bước SEO hoặc fetch link ngoài yêu cầu. |
| NOTE-M03-01 | Ngưỡng0.5/0.9 tạm thời theo baseline | Giữ đúng biên, quét lại≥0.9 vẫn gắn cờ, không thêm màn chỉnh ngưỡng. |
| NOTE-M03-02 / BR-M03-15 | Chưa có cách hiển thị phần trăm khi tổng lượt chọn=0 | Không tính0/0, không khẳng định số% cụ thể khi chưa có lượt. Nếu bỏ phiếu cuối, trạng thái hiển thị theo quyền nhưng giá trị% để chốt nguồn. |
| NOTE-M03-03/04 | Xem lại xóa hẳn chỉ ngữ cảnh vụ việc; giữ dữ liệu | Không browse, không phục hồi hoặc xóa tệp vật lý. |
| NOTE-M03-05 | Nguồn chưa định nghĩa mọi lỗi kho tệp/lưu phiên bản/transaction | Không tự tạo rollback/retry. Chỉ dùng retry AI M13 đã có nguồn. |


Không sửa FR/US/register hoặc tuyên bố nguồn đã duyệt. Các phần hoãn/thiếu chi tiết trên không được tự lấp bằng giả định sản phẩm.

## 8. Kiểm tra và bàn giao

Kết quả thực tế, lệnh và giới hạn ở [QA-M03.md](QA-M03.md). Chưa có phê duyệt cuối. Chỉ tạo thư mục M03 khi ghi đầu ra.
