# US-overview — Use case tổng quan hệ thống iShare

[Vietnamese Doc]

**Mục đích:** trình bày các nghiệp vụ chính của toàn iShare thông qua **việc lựa chọn từ UC chính đã xác định tại US-M01–US-M16**. Tài liệu giữ nguyên ID, tên, owner, mức và actor nguồn; không tạo UC mới, không đặt lại tên để gom nhiều UC, không thay thế đặc tả module.

<!-- selected:document -->
| key | value |
|---|---|
| document_id | US-overview |
| version | 1.1 |
| profile | selected-module-core-overview |
| skill_version | 2.2 |
| modules | M01, M02, M03, M04, M05, M06, M07, M08, M09, M10, M11, M12, M13, M14, M15, M16 |
| status | Chờ duyệt |
| date | 2026-11-02 |
| current_step | 7 |
| completed_steps | 1, 2, 3, 4, 5, 6, 7 |
| approved_steps | - |
| source_baseline | FR-M01 1.10; FR-M02 1.6; FR-M03 1.10; FR-M04 1.4; FR-M05 1.7; FR-M06 1.5; FR-M07 1.5; FR-M08 1.7; FR-M09 1.2; FR-M10 1.4; FR-M11 1.3; FR-M12 1.1; FR-M13 1.3; FR-M14 1.1; FR-M15 1.1; FR-M16 1.0 |
| approval_evidence | Người dùng yêu cầu sửa: chỉ chọn từ core module hiện có, một khối iShare hoàn chỉnh, không khối con; chưa phê duyệt kết quả cuối. |
| semantic_review | Đã review lựa chọn, actor và quan hệ ở mức tổng quan; xem giới hạn mục 8. |
| diagram_check | Một view SVG; parse/render/xem ảnh và kiểm tra cấu trúc tại mục 8. |

## 1. Phạm vi và nguyên tắc lựa chọn

**Boundary:** toàn hệ thống iShare. M01–M16 là thành phần nội bộ, không phải actor bên ngoài. Biểu đồ có **đúng một khối iShare**, tất cả oval nằm trực tiếp trong khối đó; không package, không khung module, không khối chức năng con.

Nguồn có **64 UC chính**. Tổng quan chọn **51 UC chính hiện có**, không đưa 13 UC hỗ trợ lên hình. Một UC được giữ khi actor có thể hoàn tất một mục tiêu nghiệp vụ có kết quả rõ; UC mức Summary được giữ khi thể hiện một vòng đời/nghiệp vụ độc lập, có các nhánh đúng quyền. Không ép mọi nhánh của Summary chạy trong một lần.

Không chọn một UC chỉ vì được gắn `core` ở module. Các UC phục vụ một đoạn luồng như nhắc tên, phân loại, gợi ý/embedding, chỉ báo tin mới, lịch sử tìm kiếm hoặc hợp đồng abstract được giải thích tại mục 5 và giữ nguyên trong mô hình module. **Không đưa lên hình không có nghĩa xóa yêu cầu hoặc đổi UC đó thành UC khác.**

Không đặt quota số UC hoặc gom tên để làm hình ít oval hơn. Những nghiệp vụ độc lập như quản lý mật khẩu, vòng đời tài khoản, gửi báo cáo, xét khiếu nại, quản trị vai trò, thống kê và các mục tiêu Group/Chat vẫn cần được phân biệt bằng ID đã có.

Cách lựa chọn này áp dụng [skill use-case-analysis](../../../.agent-instructions/skills/use-case-analysis/SKILL.md) theo yêu cầu hiện tại: lấy **một tập con** core module, giữ định danh/hợp đồng; không tự xây một tầng mục tiêu thay thế. Sơ đồ chỉ vẽ quan hệ có bằng chứng, không dùng mũi tên để diễn đạt thứ tự hay phụ thuộc dữ liệu.

## 2. Sơ đồ tổng quan toàn hệ thống

![Biểu đồ use case tổng quan iShare](diagrams/overview/SYS-overview.svg)

[Mở SVG để phóng to](diagrams/overview/SYS-overview.svg).

**Nội dung:** 51 oval, đều là core được chọn từ module; 13 actor ngoài boundary; một khối iShare. Sơ đồ không chia module. Vị trí oval chỉ phục vụ bố cục và không mang nghĩa phân rã.

**Ký pháp:** association actor–UC là nét liền; actor generalization đi từ vai trò chuyên biệt đến vai trò chung bằng tam giác rỗng; «extend» là nét đứt từ UC mở rộng đến UC cơ sở. Không vẽ include/generalization giữa UC chỉ để đủ ba loại quan hệ. Quan hệ chi tiết có endpoint là UC không được chọn vẫn giữ tại US owner, không đổi endpoint thành core khác.

## 3. Actor tương tác trực tiếp

<!-- selected:actors -->
| ID | Tên actor | Loại | Parent nguyên gốc | Phạm vi / lý do ngoài boundary | Căn cứ |
|---|---|---|---|---|---|
| ACT-001 | Guest | human | - | Người ngoài subject bị từ chối Chat, riêng link được yêu cầu đăng nhập; không association thành công. | FR-M16-01.03, FR-M16-03.02, FR-M16-16.02 |
| ACT-002 | Người dùng đã đăng nhập | human | - | Bắt đầu 1-1, tạo/xin nhóm, hộp thư của mình; không mặc nhiên thuộc mọi cuộc. | FR-M16-01.01, FR-M16-02.01, FR-M16-03.01, FR-M16-16.01 |
| ACT-004 | Dịch vụ xác thực Google | external-system | - | Dịch vụ ngoài iShare cung cấp danh tính đã xác thực cho luồng Google | FR-M01-04.01, FR-M01-04.04, FR-M01-04.06, BR-M01-08 |
| ACT-005 | Dịch vụ gửi email bên ngoài | external-system | - | Hỗ trợ giao email ra ngoài iShare; tích hợp/điều phối thuộc M07. Không coi M07 là actor hoặc cấp quyền nhà cung cấp vào dữ liệu tài khoản | FR-M01-15.05, FR-M01-01.03, FR-M01-11.01, FR-M07-04.01, FR-M07-04.02 |
| ACT-006 | Dịch vụ AI bên ngoài | external-system | - | Dịch vụ ngoài iShare trả điểm quét qua lớp nội bộ M13; hỗ trợ có điều kiện khi cần quét bài. | FR-M13-02.01, FR-M13-02.08, FR-M13-02.11, FR-M11-12.02 |
| ACT-007 | Admin hệ thống | human | ACT-008 | Qua cờ Chat tắt, vẫn cần membership/vai trò nhóm/sở hữu/hạn và dữ liệu như thường. | FR-M16-15.04, FR-M16-04.08, FR-M16-06.04 |
| ACT-008 | Mod hệ thống | human | ACT-002 | Có năng lực User, không quyền đọc/kiểm duyệt chat ngoài membership; không qua cờ tắt. | FR-M16-04.08, FR-M16-05.06, BR-M16-20, FR-M16-15.01 |
| ACT-009 | Thành viên nhóm (Member) | human | ACT-002 | Vai trò tương tác theo nhóm cụ thể; đăng bài/mời/rời, không là vai trò hệ thống mới. | BR-M11-06, FR-M11-05.01, FR-M11-10.01, FR-M11-12.01 |
| ACT-010 | Group Mod | human | ACT-009 | Thành viên được phân công duyệt/gỡ/quản trị thành viên đúng nhóm; khác ACT-008. | BR-M11-05, BR-M11-06, BR-M11-39 |
| ACT-011 | Owner nhóm | human | ACT-010 | Chủ nhóm; thêm quyền cấu hình/quản trị, tự rời có điều kiện; mỗi nhóm một Owner. | BR-M11-04, BR-M11-06, BR-M11-25, BR-M11-40 |
| ACT-012 | Thành viên cuộc trò chuyện | human | ACT-002 | Một trong hai người 1-1 hoặc current member nhóm, là vai trò tương tác đọc/gửi/thu hồi và việc nhóm khi thích hợp. | FR-M16-04.01, FR-M16-05.01, FR-M16-06.01, BR-M16-05 |
| ACT-013 | Admin nhóm chat | human | ACT-012 | Quản trị chính nhóm đang xét, có hành vi member và thêm duyệt/công tắc/xóa/chuyển; không ADMIN hệ thống. | FR-M16-02.02, FR-M16-09.01, FR-M16-10.01, FR-M16-13.01, BR-M16-04, BR-M16-05 |
| ACT-014 | Thành viên cũ nhóm chat | human | ACT-002 | Đã rời/bị xóa, chỉ đọc phần lịch sử trước cutoff và giữ hộp thư; không generalization từ current member. | FR-M16-04.10, FR-M16-11.01, FR-M16-14.01, BR-M16-27 |

Có **10 vai trò người dùng** và **3 dịch vụ hỗ trợ**. Vai trò chính/hỗ trợ áp cho từng UC; bảng catalog giữ actor nguyên gốc của tài liệu module.

| Quy ước trên sơ đồ | Diễn giải |
|---|---|
| ACT-003 trong một số US cũ | Là nhãn gộp Mod/Admin, được chiếu sang ACT-008/ACT-007 khi vẽ, đúng nhánh/quyền tương ứng. Không tạo thêm một vai trò hệ thống. Catalog nguồn bên dưới vẫn giữ chuỗi actor gốc. |
| Các cạnh kế thừa actor | Giữ đúng chuỗi gốc: Admin → Mod → User; Owner → Group Mod → Member → User; Chat Admin → thành viên cuộc trò chuyện → User. Thành viên cũ → User, không kế thừa current member. |
| Association kế thừa | Không vẽ lặp association của actor con nếu actor cha đã nối cùng UC ở cùng vai trò. Danh sách tham gia trực tiếp trước khi rút gọn có 145 cặp duy nhất; hình vẽ 79 cạnh association, phần còn lại kế thừa. |
| Guest | Chỉ nhánh được phép: đọc công khai, tìm, xem hồ sơ/bảng/nhóm, nhận banner, khôi phục truy cập theo nguồn; không vì cùng oval Summary mà được vote/sửa bài/điều hành. |
| User / chủ nội dung | Quyền sở hữu, membership, trạng thái tài khoản/cảnh cáo/cờ vẫn kiểm theo từng nhánh. Association không thay ma trận quyền. |
| Admin hệ thống / Owner Group / Admin nhóm chat | Không đồng nhất. Admin hệ thống không đương nhiên đọc Private/Chat hoặc duyệt hàng chờ Group. |
| Google / email / AI | Chỉ hỗ trợ nhánh thật sự tích hợp. AI chỉ khi cổng cho phép và cần gọi; tóm tắt có cache, thống kê không gọi AI. Không có actor M07/M13/Clock/iShare. |

## 4. Các UC chính được chọn

Catalog dưới đây lấy **nguyên các trường của core nguồn**, không tái phân loại hoặc thay tên/actor/owner. Mỗi dòng có liên kết tới đặc tả module; các ID trong cột actor có thể là vai trò khởi tạo hoặc vai trò tham gia theo nhánh Summary.

<!-- selected:catalog -->
| id | name | tier | level | primary | supporting | owner | Đặc tả nguồn | sources |
|---|---|---|---|---|---|---|---|---|
| UC-M01-020 | Đăng ký tài khoản | core | User goal | ACT-001 | ACT-004, ACT-005 | M01 | [UC-M01-020](US-M01.md#uc-m01-020) | FR-M01-01, FR-M01-02, FR-M01-03, FR-M01-04, BR-M01-02, BR-M01-03, BR-M01-08 |
| UC-M01-021 | Quản lý phiên truy cập | core | Summary | ACT-001, ACT-002, ACT-003 | ACT-004, ACT-005 | M01 | [UC-M01-021](US-M01.md#uc-m01-021) | FR-M01-04, FR-M01-05, FR-M01-06, FR-M01-07 |
| UC-M01-022 | Quản lý mật khẩu | core | Summary | ACT-001, ACT-002, ACT-003 | ACT-005 | M01 | [UC-M01-022](US-M01.md#uc-m01-022) | FR-M01-08, FR-M01-09, BR-M01-13, BR-M01-14, BR-M01-15 |
| UC-M01-023 | Quản lý vòng đời tài khoản | core | Summary | ACT-001, ACT-002, ACT-003 | ACT-005 | M01 | [UC-M01-023](US-M01.md#uc-m01-023) | FR-M01-10, FR-M01-11, FR-M01-12, FR-M01-13, BR-M01-20, BR-M01-21 |
| UC-M01-024 | Thực hiện quyền riêng tư tài khoản | core | Summary | ACT-001, ACT-002, ACT-003 | - | M01 | [UC-M01-024](US-M01.md#uc-m01-024) | FR-M01-15, FR-M01-16, BR-M01-44, BR-M01-45 |
| UC-M02-010 | Xem và tra cứu hồ sơ cá nhân | core | Summary | ACT-001, ACT-002, ACT-003 | - | M02 | [UC-M02-010](US-M02.md#uc-m02-010) | FR-M02-01, FR-M02-02, BR-M02-01, BR-M02-14, BR-M02-28 |
| UC-M02-020 | Quản lý thông tin và hình ảnh đại diện | core | Summary | ACT-002, ACT-003 | - | M02 | [UC-M02-020](US-M02.md#uc-m02-020) | FR-M02-03, FR-M02-04, BR-M02-18, BR-M02-36 |
| UC-M02-030 | Quản lý danh sách bài viết đã lưu (Bookmark) | core | Summary | ACT-002, ACT-003 | - | M02 | [UC-M02-030](US-M02.md#uc-m02-030) | FR-M02-05, FR-M02-06, FR-M02-07, BR-M02-21, BR-M02-23, BR-M02-30 |
| UC-M03-020 | Soạn thảo và xuất bản bài viết | core | Summary | ACT-002, ACT-003 | ACT-006 | M03 | [UC-M03-020](US-M03.md#uc-m03-020) | FR-M03-01, FR-M03-02, FR-M03-03, FR-M03-04, FR-M03-05, FR-M03-06 |
| UC-M03-021 | Đọc bài và tương tác bình chọn (Poll) | core | Summary | ACT-001, ACT-002, ACT-003 | - | M03 | [UC-M03-021](US-M03.md#uc-m03-021) | FR-M03-07, FR-M03-08, FR-M03-09, FR-M03-10 |
| UC-M03-022 | Chỉnh sửa và theo dõi lịch sử bài viết | core | Summary | ACT-001, ACT-002, ACT-003 | ACT-006 | M03 | [UC-M03-022](US-M03.md#uc-m03-022) | FR-M03-02.02, FR-M03-11, FR-M03-12, BR-M03-26, BR-M03-27 |
| UC-M03-023 | Quản lý trạng thái và vòng đời bài viết | core | Summary | ACT-002, ACT-003 | ACT-006 | M03 | [UC-M03-023](US-M03.md#uc-m03-023) | FR-M03-13, FR-M03-14, FR-M03-15, FR-M03-16, FR-M03-17, FR-M03-07.08 |
| UC-M04-020 | Tham gia thảo luận và trả lời bình luận | core | User goal | ACT-002, ACT-003 | - | M04 | [UC-M04-020](US-M04.md#uc-m04-020) | FR-M04-02, FR-M04-03, BR-M04-03, BR-M04-12, BR-M04-14, BR-M04-15, BR-M04-16, BR-M04-19 |
| UC-M04-030 | Quản lý và hiệu chỉnh bình luận của tác giả | core | Summary | ACT-002, ACT-003 | - | M04 | [UC-M04-030](US-M04.md#uc-m04-030) | FR-M04-04, FR-M04-05, BR-M04-07, BR-M04-08, BR-M04-20, BR-M04-21 |
| UC-M05-021 | Tra cứu và khám phá Topic & Tag | core | Summary | ACT-001, ACT-002, ACT-003, ACT-007 | - | M05 | [UC-M05-021](US-M05.md#uc-m05-021) | FR-M05-04, FR-M05-05, BR-M05-01, BR-M05-29, BR-M05-30, BR-M05-31 |
| UC-M05-022 | Quản trị danh mục Topic hệ thống | core | Summary | ACT-007 | - | M05 | [UC-M05-022](US-M05.md#uc-m05-022) | FR-M05-06, FR-M05-07, FR-M05-08, BR-M05-05, BR-M05-08, BR-M05-09 |
| UC-M05-023 | Điều phối Tag và phân loại bài viết | core | Summary | ACT-003, ACT-007 | - | M05 | [UC-M05-023](US-M05.md#uc-m05-023) | FR-M05-09, FR-M05-10, FR-M05-11, BR-M05-04, BR-M05-25, BR-M05-26, BR-M05-27 |
| UC-M06-020 | Tìm và khai thác kết quả tìm kiếm | core | User goal | ACT-001, ACT-002, ACT-003 | ACT-006 | M06 | [UC-M06-020](US-M06.md#uc-m06-020) | FR-M06-02, FR-M06-03, FR-M06-04, BR-M06-16, BR-M06-17, BR-M06-19, BR-M06-21 |
| UC-M07-020 | Quản lý theo dõi người dùng và Topic | core | Summary | ACT-002, ACT-003 | - | M07 | [UC-M07-020](US-M07.md#uc-m07-020) | FR-M07-01, BR-M07-15, BR-M07-23, BR-M07-25 |
| UC-M07-021 | Tiếp nhận và xử lý thông báo cá nhân | core | Summary | ACT-002, ACT-003 | ACT-005 | M07 | [UC-M07-021](US-M07.md#uc-m07-021) | FR-M07-02, FR-M07-03, FR-M07-04, FR-M07-05, FR-M07-06, BR-M07-01, BR-M07-03, BR-M07-09, BR-M07-20 |
| UC-M08-020 | Gửi báo cáo vi phạm | core | User goal | ACT-002, ACT-008, ACT-007 | - | M08 | [UC-M08-020](US-M08.md#uc-m08-020) | FR-M08-01, BR-M08-01, BR-M08-02, BR-M08-03, BR-M08-04, BR-M08-47, BR-M08-55 |
| UC-M08-021 | Giải quyết một vụ báo cáo | core | User goal | ACT-008, ACT-007 | - | M08 | [UC-M08-021](US-M08.md#uc-m08-021) | FR-M08-02, FR-M08-03, FR-M08-04, FR-M08-05, BR-M08-08, BR-M08-10, BR-M08-46, BR-M08-48 |
| UC-M08-022 | Kiểm duyệt nội dung nghi vấn | core | Summary | ACT-008, ACT-007 | ACT-006 | M08 | [UC-M08-022](US-M08.md#uc-m08-022) | FR-M08-06, FR-M08-07, FR-M08-08, FR-M08-09, BR-M08-22, BR-M08-23, BR-M08-55 |
| UC-M08-023 | Quản lý cảnh cáo và ban | core | Summary | ACT-002, ACT-008, ACT-007 | - | M08 | [UC-M08-023](US-M08.md#uc-m08-023) | FR-M08-09, FR-M08-10, FR-M08-11, FR-M08-12, FR-M08-13, FR-M08-14, FR-M08-15, BR-M08-31, BR-M08-33, BR-M08-46 |
| UC-M08-024 | Kiểm duyệt nhóm vi phạm | core | Summary | ACT-008, ACT-007 | - | M08 | [UC-M08-024](US-M08.md#uc-m08-024) | FR-M08-18, BR-M08-46, BR-M08-48, BR-M08-50, BR-M11-28 |
| UC-M08-025 | Tra cứu nhật ký kiểm duyệt | core | User goal | ACT-008, ACT-007 | - | M08 | [UC-M08-025](US-M08.md#uc-m08-025) | FR-M08-16, FR-M08-17, BR-M08-39, BR-M08-40, BR-M08-41 |
| UC-M09-020 | Gửi và theo dõi khiếu nại | core | Summary | ACT-002, ACT-008 | - | M09 | [UC-M09-020](US-M09.md#uc-m09-020) | FR-M09-01, FR-M09-02, BR-M09-01, BR-M09-04, BR-M09-21, BR-M09-27 |
| UC-M09-021 | Giải quyết khiếu nại | core | User goal | ACT-008, ACT-007 | - | M09 | [UC-M09-021](US-M09.md#uc-m09-021) | FR-M09-03, FR-M09-04, FR-M09-06, FR-M09-07, BR-M09-11, BR-M09-12, BR-M09-27 |
| UC-M10-020 | Quản lý nhân sự và vai trò | core | Summary | ACT-007, ACT-002, ACT-008 | - | M10 | [UC-M10-020](US-M10.md#uc-m10-020) | FR-M10-01, FR-M10-02, FR-M10-03, FR-M10-04, FR-M10-05, FR-M10-06, FR-M10-07, FR-M10-08, BR-M10-01, BR-M10-02, BR-M10-05, BR-M10-07, BR-M10-10, BR-M10-11, BR-M10-25, BR-M10-27 |
| UC-M10-021 | Cấu hình hoạt động hệ thống | core | Summary | ACT-007 | - | M10 | [UC-M10-021](US-M10.md#uc-m10-021) | FR-M10-09, FR-M10-10, FR-M10-11, FR-M10-12, BR-M10-04, BR-M10-12, BR-M10-13, BR-M10-14, BR-M10-15, BR-M10-16, BR-M10-17, BR-M10-18, BR-M10-19, BR-M10-26, BR-M10-28 |
| UC-M10-022 | Phát và tiếp nhận thông báo toàn trang | core | Summary | ACT-007, ACT-001, ACT-002 | - | M10 | [UC-M10-022](US-M10.md#uc-m10-022) | FR-M10-13, BR-M10-20, BR-M10-26 |
| UC-M10-023 | Tra cứu nhật ký thao tác Admin | core | User goal | ACT-007 | - | M10 | [UC-M10-023](US-M10.md#uc-m10-023) | FR-M10-14, FR-M10-15, BR-M10-02, BR-M10-21, BR-M10-22, BR-M10-23, BR-M10-24 |
| UC-M11-030 | Khởi tạo và quản trị nhóm | core | Summary | ACT-002, ACT-011 | - | M11 | [UC-M11-030](US-M11.md#uc-m11-030) | FR-M11-01, FR-M11-02, FR-M11-15, BR-M11-03, BR-M11-04, BR-M11-06, BR-M11-23, BR-M11-31, BR-M11-32 |
| UC-M11-031 | Khám phá và xem nhóm | core | Summary | ACT-001, ACT-002, ACT-009, ACT-008, ACT-007 | - | M11 | [UC-M11-031](US-M11.md#uc-m11-031) | FR-M11-03, BR-M11-11, BR-M11-13, BR-M11-14, BR-M11-15, BR-M11-17, BR-M11-33, BR-M11-34, BR-M11-35 |
| UC-M11-032 | Quản lý tham gia và thành viên | core | Summary | ACT-002, ACT-009, ACT-010, ACT-011 | - | M11 | [UC-M11-032](US-M11.md#uc-m11-032) | FR-M11-04, FR-M11-05, FR-M11-06, FR-M11-07, FR-M11-08, FR-M11-09, FR-M11-10, FR-M11-11, BR-M11-05, BR-M11-06, BR-M11-07, BR-M11-08, BR-M11-09, BR-M11-10, BR-M11-12, BR-M11-24, BR-M11-25, BR-M11-26 |
| UC-M11-033 | Đăng bài trong nhóm | core | User goal | ACT-009, ACT-010, ACT-011 | ACT-006 | M11 | [UC-M11-033](US-M11.md#uc-m11-033) | FR-M11-12, FR-M11-13.11, FR-M11-13.12, FR-M11-13.14, BR-M11-01, BR-M11-16, BR-M11-17, BR-M11-18, BR-M11-19, BR-M11-38, BR-M11-40 |
| UC-M11-034 | Kiểm duyệt nội dung cấp nhóm | core | Summary | ACT-010, ACT-011 | - | M11 | [UC-M11-034](US-M11.md#uc-m11-034) | FR-M11-13, FR-M11-14, BR-M11-05, BR-M11-06, BR-M11-20, BR-M11-21, BR-M11-22, BR-M11-30, BR-M11-38, BR-M11-39 |
| UC-M12-020 | Đánh giá nội dung bằng upvote | core | User goal | ACT-002, ACT-007 | - | M12 | [UC-M12-020](US-M12.md#uc-m12-020) | FR-M12-01, FR-M12-02, BR-M12-01, BR-M12-02, BR-M12-03, BR-M12-04, BR-M12-05, BR-M12-07, BR-M12-28 |
| UC-M12-021 | Tra cứu bảng xếp hạng | core | User goal | ACT-001, ACT-002, ACT-007 | - | M12 | [UC-M12-021](US-M12.md#uc-m12-021) | FR-M12-04, FR-M12-05, FR-M12-06, BR-M12-14, BR-M12-16, BR-M12-18, BR-M12-19, BR-M12-20, BR-M12-21, BR-M12-22, BR-M12-24, BR-M12-29 |
| UC-M13-023 | Yêu cầu và xem tóm tắt bài viết | core | User goal | ACT-002, ACT-007 | ACT-006 | M13 | [UC-M13-023](US-M13.md#uc-m13-023) | FR-M13-06, FR-M13-07, BR-M13-06, BR-M13-19, BR-M13-20, BR-M13-27, BR-M13-28 |
| UC-M14-020 | Khám phá nội dung thịnh hành | core | Summary | ACT-001, ACT-002 | - | M14 | [UC-M14-020](US-M14.md#uc-m14-020) | FR-M14-01, FR-M14-02, FR-M14-03, BR-M14-01, BR-M14-03, BR-M14-19, BR-M14-24 |
| UC-M14-021 | Xem bài từ người dùng và Topic đang theo dõi | core | User goal | ACT-002 | - | M14 | [UC-M14-021](US-M14.md#uc-m14-021) | FR-M14-04, FR-M14-07, FR-M14-08, BR-M14-08, BR-M14-20 |
| UC-M14-022 | Xem bài từ các nhóm đã tham gia | core | User goal | ACT-002 | - | M14 | [UC-M14-022](US-M14.md#uc-m14-022) | FR-M14-05, FR-M14-07, FR-M14-08, BR-M14-07, BR-M14-21 |
| UC-M14-023 | Xem bài mới toàn site | core | User goal | ACT-001, ACT-002 | - | M14 | [UC-M14-023](US-M14.md#uc-m14-023) | FR-M14-06, FR-M14-07, FR-M14-08, BR-M14-06, BR-M14-09 |
| UC-M15-020 | Xem thống kê người dùng | core | User goal | ACT-007 | - | M15 | [UC-M15-020](US-M15.md#uc-m15-020) | FR-M15-01, BR-M15-07, BR-M15-20 |
| UC-M15-021 | Xem thống kê nội dung | core | User goal | ACT-007 | - | M15 | [UC-M15-021](US-M15.md#uc-m15-021) | FR-M15-02, BR-M15-08, BR-M15-09, BR-M15-17, BR-M15-21 |
| UC-M15-022 | Xem thống kê kiểm duyệt | core | User goal | ACT-007 | - | M15 | [UC-M15-022](US-M15.md#uc-m15-022) | FR-M15-03, BR-M15-10, BR-M15-11, BR-M15-12, BR-M15-13, BR-M15-14, BR-M15-22 |
| UC-M16-030 | Bắt đầu và truy cập cuộc trò chuyện | core | Summary | ACT-002, ACT-012, ACT-014 | - | M16 | [UC-M16-030](US-M16.md#uc-m16-030) | FR-M16-01, FR-M16-03, FR-M16-04, FR-M16-07, FR-M16-15 |
| UC-M16-031 | Trao đổi và quản lý tin nhắn | core | Summary | ACT-012 | - | M16 | [UC-M16-031](US-M16.md#uc-m16-031) | FR-M16-05, FR-M16-06, FR-M16-07, FR-M16-15 |
| UC-M16-032 | Hình thành và mở rộng nhóm chat | core | Summary | ACT-002, ACT-012, ACT-013 | - | M16 | [UC-M16-032](US-M16.md#uc-m16-032) | FR-M16-02, FR-M16-08, FR-M16-10, FR-M16-16, FR-M16-15 |
| UC-M16-033 | Quản lý vòng đời nhóm chat | core | Summary | ACT-012, ACT-013 | - | M16 | [UC-M16-033](US-M16.md#uc-m16-033) | FR-M16-09, FR-M16-11, FR-M16-12, FR-M16-13, FR-M16-14, FR-M16-17, FR-M16-15 |

### 4.1 Định vị các UC trong tài liệu tổng quan

Các anchor dưới đây định vị cùng ID để các bảng quan hệ/truy vết liên kết. Hợp đồng trigger, tiền điều kiện, kết quả, nhánh, UC con và AUT/BR được đọc trực tiếp ở owner; không lập một đặc tả khác cho cùng ID.

<a id="uc-m01-020"></a>

**UC-M01-020 — Đăng ký tài khoản:** owner M01, mức User goal. [Đọc hợp đồng và phân rã](US-M01.md#uc-m01-020).

<a id="uc-m01-021"></a>

**UC-M01-021 — Quản lý phiên truy cập:** owner M01, mức Summary. [Đọc hợp đồng và phân rã](US-M01.md#uc-m01-021).

<a id="uc-m01-022"></a>

**UC-M01-022 — Quản lý mật khẩu:** owner M01, mức Summary. [Đọc hợp đồng và phân rã](US-M01.md#uc-m01-022).

<a id="uc-m01-023"></a>

**UC-M01-023 — Quản lý vòng đời tài khoản:** owner M01, mức Summary. [Đọc hợp đồng và phân rã](US-M01.md#uc-m01-023).

<a id="uc-m01-024"></a>

**UC-M01-024 — Thực hiện quyền riêng tư tài khoản:** owner M01, mức Summary. [Đọc hợp đồng và phân rã](US-M01.md#uc-m01-024).

<a id="uc-m02-010"></a>

**UC-M02-010 — Xem và tra cứu hồ sơ cá nhân:** owner M02, mức Summary. [Đọc hợp đồng và phân rã](US-M02.md#uc-m02-010).

<a id="uc-m02-020"></a>

**UC-M02-020 — Quản lý thông tin và hình ảnh đại diện:** owner M02, mức Summary. [Đọc hợp đồng và phân rã](US-M02.md#uc-m02-020).

<a id="uc-m02-030"></a>

**UC-M02-030 — Quản lý danh sách bài viết đã lưu (Bookmark):** owner M02, mức Summary. [Đọc hợp đồng và phân rã](US-M02.md#uc-m02-030).

<a id="uc-m03-020"></a>

**UC-M03-020 — Soạn thảo và xuất bản bài viết:** owner M03, mức Summary. [Đọc hợp đồng và phân rã](US-M03.md#uc-m03-020).

<a id="uc-m03-021"></a>

**UC-M03-021 — Đọc bài và tương tác bình chọn (Poll):** owner M03, mức Summary. [Đọc hợp đồng và phân rã](US-M03.md#uc-m03-021).

<a id="uc-m03-022"></a>

**UC-M03-022 — Chỉnh sửa và theo dõi lịch sử bài viết:** owner M03, mức Summary. [Đọc hợp đồng và phân rã](US-M03.md#uc-m03-022).

<a id="uc-m03-023"></a>

**UC-M03-023 — Quản lý trạng thái và vòng đời bài viết:** owner M03, mức Summary. [Đọc hợp đồng và phân rã](US-M03.md#uc-m03-023).

<a id="uc-m04-020"></a>

**UC-M04-020 — Tham gia thảo luận và trả lời bình luận:** owner M04, mức User goal. [Đọc hợp đồng và phân rã](US-M04.md#uc-m04-020).

<a id="uc-m04-030"></a>

**UC-M04-030 — Quản lý và hiệu chỉnh bình luận của tác giả:** owner M04, mức Summary. [Đọc hợp đồng và phân rã](US-M04.md#uc-m04-030).

<a id="uc-m05-021"></a>

**UC-M05-021 — Tra cứu và khám phá Topic & Tag:** owner M05, mức Summary. [Đọc hợp đồng và phân rã](US-M05.md#uc-m05-021).

<a id="uc-m05-022"></a>

**UC-M05-022 — Quản trị danh mục Topic hệ thống:** owner M05, mức Summary. [Đọc hợp đồng và phân rã](US-M05.md#uc-m05-022).

<a id="uc-m05-023"></a>

**UC-M05-023 — Điều phối Tag và phân loại bài viết:** owner M05, mức Summary. [Đọc hợp đồng và phân rã](US-M05.md#uc-m05-023).

<a id="uc-m06-020"></a>

**UC-M06-020 — Tìm và khai thác kết quả tìm kiếm:** owner M06, mức User goal. [Đọc hợp đồng và phân rã](US-M06.md#uc-m06-020).

<a id="uc-m07-020"></a>

**UC-M07-020 — Quản lý theo dõi người dùng và Topic:** owner M07, mức Summary. [Đọc hợp đồng và phân rã](US-M07.md#uc-m07-020).

<a id="uc-m07-021"></a>

**UC-M07-021 — Tiếp nhận và xử lý thông báo cá nhân:** owner M07, mức Summary. [Đọc hợp đồng và phân rã](US-M07.md#uc-m07-021).

<a id="uc-m08-020"></a>

**UC-M08-020 — Gửi báo cáo vi phạm:** owner M08, mức User goal. [Đọc hợp đồng và phân rã](US-M08.md#uc-m08-020).

<a id="uc-m08-021"></a>

**UC-M08-021 — Giải quyết một vụ báo cáo:** owner M08, mức User goal. [Đọc hợp đồng và phân rã](US-M08.md#uc-m08-021).

<a id="uc-m08-022"></a>

**UC-M08-022 — Kiểm duyệt nội dung nghi vấn:** owner M08, mức Summary. [Đọc hợp đồng và phân rã](US-M08.md#uc-m08-022).

<a id="uc-m08-023"></a>

**UC-M08-023 — Quản lý cảnh cáo và ban:** owner M08, mức Summary. [Đọc hợp đồng và phân rã](US-M08.md#uc-m08-023).

<a id="uc-m08-024"></a>

**UC-M08-024 — Kiểm duyệt nhóm vi phạm:** owner M08, mức Summary. [Đọc hợp đồng và phân rã](US-M08.md#uc-m08-024).

<a id="uc-m08-025"></a>

**UC-M08-025 — Tra cứu nhật ký kiểm duyệt:** owner M08, mức User goal. [Đọc hợp đồng và phân rã](US-M08.md#uc-m08-025).

<a id="uc-m09-020"></a>

**UC-M09-020 — Gửi và theo dõi khiếu nại:** owner M09, mức Summary. [Đọc hợp đồng và phân rã](US-M09.md#uc-m09-020).

<a id="uc-m09-021"></a>

**UC-M09-021 — Giải quyết khiếu nại:** owner M09, mức User goal. [Đọc hợp đồng và phân rã](US-M09.md#uc-m09-021).

<a id="uc-m10-020"></a>

**UC-M10-020 — Quản lý nhân sự và vai trò:** owner M10, mức Summary. [Đọc hợp đồng và phân rã](US-M10.md#uc-m10-020).

<a id="uc-m10-021"></a>

**UC-M10-021 — Cấu hình hoạt động hệ thống:** owner M10, mức Summary. [Đọc hợp đồng và phân rã](US-M10.md#uc-m10-021).

<a id="uc-m10-022"></a>

**UC-M10-022 — Phát và tiếp nhận thông báo toàn trang:** owner M10, mức Summary. [Đọc hợp đồng và phân rã](US-M10.md#uc-m10-022).

<a id="uc-m10-023"></a>

**UC-M10-023 — Tra cứu nhật ký thao tác Admin:** owner M10, mức User goal. [Đọc hợp đồng và phân rã](US-M10.md#uc-m10-023).

<a id="uc-m11-030"></a>

**UC-M11-030 — Khởi tạo và quản trị nhóm:** owner M11, mức Summary. [Đọc hợp đồng và phân rã](US-M11.md#uc-m11-030).

<a id="uc-m11-031"></a>

**UC-M11-031 — Khám phá và xem nhóm:** owner M11, mức Summary. [Đọc hợp đồng và phân rã](US-M11.md#uc-m11-031).

<a id="uc-m11-032"></a>

**UC-M11-032 — Quản lý tham gia và thành viên:** owner M11, mức Summary. [Đọc hợp đồng và phân rã](US-M11.md#uc-m11-032).

<a id="uc-m11-033"></a>

**UC-M11-033 — Đăng bài trong nhóm:** owner M11, mức User goal. [Đọc hợp đồng và phân rã](US-M11.md#uc-m11-033).

<a id="uc-m11-034"></a>

**UC-M11-034 — Kiểm duyệt nội dung cấp nhóm:** owner M11, mức Summary. [Đọc hợp đồng và phân rã](US-M11.md#uc-m11-034).

<a id="uc-m12-020"></a>

**UC-M12-020 — Đánh giá nội dung bằng upvote:** owner M12, mức User goal. [Đọc hợp đồng và phân rã](US-M12.md#uc-m12-020).

<a id="uc-m12-021"></a>

**UC-M12-021 — Tra cứu bảng xếp hạng:** owner M12, mức User goal. [Đọc hợp đồng và phân rã](US-M12.md#uc-m12-021).

<a id="uc-m13-023"></a>

**UC-M13-023 — Yêu cầu và xem tóm tắt bài viết:** owner M13, mức User goal. [Đọc hợp đồng và phân rã](US-M13.md#uc-m13-023).

<a id="uc-m14-020"></a>

**UC-M14-020 — Khám phá nội dung thịnh hành:** owner M14, mức Summary. [Đọc hợp đồng và phân rã](US-M14.md#uc-m14-020).

<a id="uc-m14-021"></a>

**UC-M14-021 — Xem bài từ người dùng và Topic đang theo dõi:** owner M14, mức User goal. [Đọc hợp đồng và phân rã](US-M14.md#uc-m14-021).

<a id="uc-m14-022"></a>

**UC-M14-022 — Xem bài từ các nhóm đã tham gia:** owner M14, mức User goal. [Đọc hợp đồng và phân rã](US-M14.md#uc-m14-022).

<a id="uc-m14-023"></a>

**UC-M14-023 — Xem bài mới toàn site:** owner M14, mức User goal. [Đọc hợp đồng và phân rã](US-M14.md#uc-m14-023).

<a id="uc-m15-020"></a>

**UC-M15-020 — Xem thống kê người dùng:** owner M15, mức User goal. [Đọc hợp đồng và phân rã](US-M15.md#uc-m15-020).

<a id="uc-m15-021"></a>

**UC-M15-021 — Xem thống kê nội dung:** owner M15, mức User goal. [Đọc hợp đồng và phân rã](US-M15.md#uc-m15-021).

<a id="uc-m15-022"></a>

**UC-M15-022 — Xem thống kê kiểm duyệt:** owner M15, mức User goal. [Đọc hợp đồng và phân rã](US-M15.md#uc-m15-022).

<a id="uc-m16-030"></a>

**UC-M16-030 — Bắt đầu và truy cập cuộc trò chuyện:** owner M16, mức Summary. [Đọc hợp đồng và phân rã](US-M16.md#uc-m16-030).

<a id="uc-m16-031"></a>

**UC-M16-031 — Trao đổi và quản lý tin nhắn:** owner M16, mức Summary. [Đọc hợp đồng và phân rã](US-M16.md#uc-m16-031).

<a id="uc-m16-032"></a>

**UC-M16-032 — Hình thành và mở rộng nhóm chat:** owner M16, mức Summary. [Đọc hợp đồng và phân rã](US-M16.md#uc-m16-032).

<a id="uc-m16-033"></a>

**UC-M16-033 — Quản lý vòng đời nhóm chat:** owner M16, mức Summary. [Đọc hợp đồng và phân rã](US-M16.md#uc-m16-033).

## 5. UC chính nguồn không đưa lên sơ đồ

<!-- selected:excluded -->
| ID / tên nguyên gốc | Owner | Lý do không thể hiện thành oval tổng quan |
|---|---|---|
| [UC-M01-025](US-M01.md#uc-m01-025) — Nhắc tên người dùng | M01 | Mention hoàn tất một phần nội dung đang soạn, chưa hoàn tất nghiệp vụ công bố bài/thảo luận. Giữ trong chi tiết M01/M03/M04. |
| [UC-M04-010](US-M04.md#uc-m04-010) — Tiếp cận và đọc thảo luận bình luận | M04 | Đọc bình luận là phần đọc thảo luận gắn với bài; giữ đầy đủ ở chi tiết M04 và giao tiếp đọc bài, không bổ sung oval riêng trong view tổng quan. UC-M03-021 không bị đổi tên hay mở rộng đặc tả. |
| [UC-M05-020](US-M05.md#uc-m05-020) — Phân loại nội dung bài viết theo Chuyên mục và Thẻ | M05 | Chốt Topic/Tag là hợp đồng của nhánh soạn/gửi/sửa bài. Kết quả là dữ liệu phân loại, chưa hoàn tất nghiệp vụ công bố nội dung; giữ ở chi tiết M03/M05. |
| [UC-M06-021](US-M06.md#uc-m06-021) — Tra cứu nhanh người dùng, Tag, Topic và Group | M06 | Tra cứu nhanh phục vụ nhập/chọn đối tượng tìm, giữ ở chi tiết tìm kiếm thay vì một mục tiêu tổng quan riêng. |
| [UC-M06-022](US-M06.md#uc-m06-022) — Dùng lại và quản lý lịch sử tìm kiếm trên thiết bị | M06 | Dùng lại/xóa lịch sử là hành vi hỗ trợ quản lý truy vấn trên thiết bị; giữ ở chi tiết M06. |
| [UC-M07-022](US-M07.md#uc-m07-022) — Điều chỉnh cách nhận thông báo cá nhân | M07 | Cài đặt mute theo bài/cuộc/toàn Chat là lựa chọn trong trải nghiệm thông báo, không thêm oval cấu hình cá nhân trên tổng quan. |
| [UC-M07-023](US-M07.md#uc-m07-023) — Kiểm tra tin nhắn mới | M07 | Tín hiệu cuộc chưa đọc/popup/icon là điểm vào Chat; nghiệp vụ truy cập và trao đổi do các core M16 thể hiện. |
| [UC-M09-022](US-M09.md#uc-m09-022) — Thi hành đảo ngược xử lý | M09 | Hợp đồng abstract thi hành phán quyết Chấp nhận; không khởi chạy như mục tiêu độc lập. Giữ nguyên ID và các chuyên biệt trong chi tiết M09. |
| [UC-M12-022](US-M12.md#uc-m12-022) — Theo dõi điểm và thành tích đóng góp | M12 | Điểm/huy hiệu/nhãn được đọc trong hồ sơ và bối cảnh thành tích; tác vụ cập nhật giữ ở M12, không thêm mục tiêu riêng trên view này. |
| [UC-M13-020](US-M13.md#uc-m13-020) — Hỗ trợ kiểm duyệt nội dung bằng AI | M13 | Năng lực chấm điểm/điều phối AI hỗ trợ luồng kiểm duyệt, không mục tiêu độc lập do người dùng hoàn tất. |
| [UC-M13-021](US-M13.md#uc-m13-021) — Cung cấp biểu diễn ngữ nghĩa cho tìm kiếm | M13 | Embedding bài/truy vấn là năng lực nội bộ hỗ trợ tìm kiếm, không mục tiêu trực tiếp của actor. |
| [UC-M13-022](US-M13.md#uc-m13-022) — Cung cấp gợi ý Topic bằng AI | M13 | Provider gợi ý Topic hỗ trợ phân loại trong bài viết, không mục tiêu nghiệp vụ cấp hệ thống riêng. |
| [UC-M13-024](US-M13.md#uc-m13-024) — Kiểm tra căn cứ AI và chất lượng gợi ý Topic | M13 | Log căn cứ và metric phục vụ khiếu nại/thống kê; giữ ở chi tiết M09/M13/M15, không nâng năng lực hỗ trợ thành mục tiêu độc lập. |

Đây là **quyết định phạm vi view**, không phải bảng đổi ID, không khẳng định UC được chọn bao hàm toàn bộ core không vẽ bằng quan hệ include. Khi cần xem các hành vi này, dùng phân rã/sơ đồ chi tiết module.

## 6. Quan hệ giữa UC và giao tiếp liên module

### 6.1 Quan hệ thể hiện trên hình

Tổng quan này có **một quan hệ extend giữa hai core có sẵn**. Chưa có bằng chứng để thêm include hoặc generalization giữa các core được chọn mà vẫn giữ đúng hợp đồng và endpoint. Không tạo UC cha mới để nối Feed/Search; không chuyển đích từ UC con sang core chỉ để có cạnh liên module.

<a id="uc-m03-021-read-point"></a>

**Điểm trong UC-M03-021:** ở nhánh đọc, sau khi nội dung đầy đủ đã hiển thị bởi [bước 2 của UC-M03-007](US-M03.md#uc-m03-007-main-2). Người xem tiếp tục đọc bài/poll/lịch sử theo luồng nguồn; không cần yêu cầu tóm tắt để hoàn tất đọc.

<!-- selected:extension-points -->
| id | base | at | description |
|---|---|---|---|
| EP-M03-READ-SUMMARY | UC-M03-021 | #uc-m03-021-read-point | Sau khi hiện bài đầy đủ trong nhánh đọc. Đây là EP phân tích ghi ở tổng quan, có căn cứ FR-M13-07; không thêm chức năng, không đổi luồng module. |

<!-- selected:relations -->
| id | type | source | target | at | condition | return_to | rationale | sources |
|---|---|---|---|---|---|---|---|---|
| REL-OV-01 | extend | UC-M13-023 | UC-M03-021 | EP-M03-READ-SUMMARY | Trong nhánh đọc của UC-M03-021, User bấm Tóm tắt trên bài được quyền xem, tiêu đề+nội dung chữ từ 300 từ và công tắc AI tổng bật. | #uc-m03-021-read-point | UC-M03-021 ở nhánh đọc đã hiển thị đầy đủ bài và hoàn tất được khi không yêu cầu tóm tắt. UC-M13-023 bổ sung tóm tắt theo yêu cầu; cache/lỗi không chặn bài gốc. Điểm mở rộng thuộc nhánh đọc, không thuộc nhánh quản lý poll. Quan hệ được xác định tại tổng quan từ FR hiện có, không thêm UC hoặc sửa hợp đồng module. | FR-M13-07.01, FR-M13-07.03, FR-M13-07.05, FR-M13-07.08, FR-M03-07.01, BR-M13-20 |

**Thực hiện và trở về:** User yêu cầu tóm tắt → UC-M13-023 kiểm phiên/quyền/độ dài/công tắc → nhận tóm tắt hợp lệ đang giữ hoặc tạo mới → hiển thị ghi chú không bao gồm tệp → tiếp tục đọc tại điểm trên. Nếu AI tắt/lỗi hoặc không đủ điều kiện, xử lý theo M13 và bài đầy đủ vẫn đọc được. Guest chỉ được nhắc đăng nhập, không thực thi nhánh thành công của extension. EP không áp cho một lần chỉ quản lý poll.

### 6.2 Phụ thuộc module không tự tạo quan hệ UML

<!-- selected:interfaces -->
| Module liên quan | UC / luồng nguồn liên quan | Kết luận và cách thể hiện | Căn cứ |
|---|---|---|---|
| M01 ↔ các module cần phiên | UC-M01-021, UC-M01-024 và các thao tác được bảo vệ | Phiên/chính sách/trạng thái là cổng hoặc tiền điều kiện. Không include Đăng nhập vào mọi UC; đồng ý lại có thể phát sinh khi phiên còn hiệu lực. | FR-M01-05, FR-M01-16, BR-M01-18 |
| M01 ↔ M02 | UC-M01-020; UC-M02-010, UC-M02-020 | Đăng ký/thiết lập tạo hồ sơ, xem/sửa về sau có trigger riêng; không include đăng ký lại khi sửa. | FR-M01-03, FR-M02-01, FR-M02-03 |
| M03 ↔ M05 | UC-M03-020, UC-M03-022; hợp đồng phân loại của M05 | Phân loại là hành vi trong nhánh soạn/gửi/sửa. Core phân loại không chọn trên view, nên không thêm oval hoặc đổi đích include sang core danh mục/quản trị Topic. | FR-M03-01, FR-M03-04, FR-M03-11, FR-M05-01, FR-M05-03 |
| M05 ↔ M13 | Gợi ý Topic/feedback trong chi tiết bài viết | Năng lực hỗ trợ; gợi ý hợp lệ chọn sẵn tối đa 3 Topic, tác giả thay đổi lựa chọn cuối. Không actor M13 hay mục tiêu provider mới. | FR-M05-02.01, FR-M05-02.03, FR-M05-02.04, FR-M13-05 |
| M03 ↔ M11 | UC-M03-020, UC-M11-033, UC-M11-034 | Cổng công bố và hàng chờ khác phạm vi. Không generalization chỉ vì đều đăng bài; không include việc staff duyệt từ mọi lần tác giả gửi. | FR-M03-04, FR-M03-06, FR-M11-12, FR-M11-13 |
| M03/M04/M11 ↔ M08/M13 | UC-M03-020, UC-M04-020, UC-M08-022/023 | Quét/chấm điểm/cảnh cáo/ẩn là chính sách và tác vụ đúng ngữ cảnh. Không biến năng lực AI nội bộ thành actor; không quét mọi lần bình luận. | FR-M03-05, FR-M08-08, FR-M08-09, FR-M13-02 |
| M03 ↔ M13 | UC-M13-023 → UC-M03-021 | extend tại EP-M03-READ-SUMMARY; đúng hai UC nguồn được chọn, có điều kiện và điểm trở về. | FR-M13-07.01, FR-M13-07.05, FR-M13-07.08 |
| M02 ↔ M03/M11 | UC-M02-030; UC-M03-021 | Bookmark giữ tham chiếu, không cấp quyền nội dung. Mở bài có lựa chọn và cổng riêng, không include mọi lần đọc từ lưu bài. | FR-M02-05, FR-M02-07, FR-M03-07 |
| M05/M07/M11 ↔ M06/M14 | UC-M05-021, UC-M07-020, UC-M06-020; các core M14 | Topic/follow/membership cung cấp dữ liệu ứng viên; điều hướng sang tìm không include. Feed/Search không kế thừa nhau vì chưa có core cha chung hiện hữu. Search có thể cho thành viên tìm bài Private; Trending/Following không lấy Private kể cả thành viên. | FR-M05-04, FR-M06-02, FR-M07-01, FR-M14-04, FR-M14-05 |
| M03/M04/M08/M09/M10/M11/M12/M16 ↔ M07 | Các nghiệp vụ phát sự kiện; UC-M07-021 | Tạo/giao thông báo là sự kiện; người nhận đọc/đánh dấu bằng trigger khác. Không include đọc thông báo trong mọi lần công bố/ra phán quyết. | FR-M07-02, FR-M07-03, FR-M07-04, FR-M07-05 |
| M16 ↔ M07 | Các core M16; chỉ báo Chat giữ trong chi tiết M07 | M16 sở hữu read marker, M07 hiển thị số cuộc/popup/icon. Mute không đổi unread; Chat không vào chuông/email. Không đổi tương tác dữ liệu thành include kiểm tra tin mới từ mọi lần gửi. | FR-M16-03, FR-M16-07, FR-M07-07, FR-M07-09 |
| M11 ↔ M16 | Các core Group và Chat được chọn | Đối tượng/vai trò/vòng đời khác nhau, không generalization. Tự chuyển Owner Group không áp cho Chat Admin. | FR-M11-11, FR-M16-13, FR-M16-17 |
| M03/M04/M11 ↔ M08 | UC-M08-020 và UC-M08-021 | Gửi báo cáo hoàn tất ở ghi nhận; staff nhận/xét bằng trigger khác. Không include Giải quyết từ Gửi báo cáo; chưa kết luận không đồng nghĩa vi phạm. | FR-M08-01, FR-M08-02, FR-M08-05 |
| M08/M13 ↔ M09 | UC-M09-020, UC-M09-021 | Hồ sơ và căn cứ được dùng khi xét; gửi đơn không include xét đơn. Mở log đã ghi không tự gọi AI lại. | FR-M09-01, FR-M09-03, FR-M09-06, FR-M13-08, FR-M13-09 |
| M09 ↔ M01/M03/M08/M11/M12 | Chi tiết thi hành trong UC-M09-021 | Include thật ở module là UC-M09-006 → UC-M09-022. Không thay source thành core khi vẽ; hai endpoint không được chọn nên cạnh giữ ở chi tiết M09. Đảo ngược đúng loại, không tự phục hồi Mod/hiện mọi bình luận; bài Group có thể vẫn chờ duyệt. | FR-M09-07, FR-M09-08 |
| M12 ↔ M02/M03/M04/M08/M09/M14 | UC-M12-020/021; hồ sơ, chế tài, feed | Upvote/vi phạm/chu kỳ tạo sự kiện điểm/rank theo M12; xem bảng không tính lại. Không include xem Feed hoặc bảng từ upvote. HEAVY loại bảng không tự loại bài khỏi Feed. | FR-M12-01, FR-M12-02, FR-M12-04, FR-M12-05, FR-M14-03 |
| M10 ↔ M01/M07/M08 | Các core M10, UC-M07-021 | Đề xuất vai trò cần người nhận phản hồi; ban có AUT thu hồi Mod; cờ/audit áp đúng điều kiện, không xóa/làm bù dữ liệu. Không chuỗi include chỉ vì thao tác trước/sau. | FR-M10-02, FR-M10-03, FR-M10-06, FR-M10-09, FR-M10-12 |
| M15 ↔ M01/M03/M08/M09 | UC-M15-020/021/022 | Dữ liệu đầu vào thống kê, không include hoạt động được đếm. Admin xem số liệu không thực hiện đăng ký/đăng bài/ban/xét đơn. | FR-M15-01, FR-M15-02, FR-M15-03 |
| M15 ↔ M13/M05 | UC-M15-021 và metric ở chi tiết M13 | Include nguồn là UC-M15-021 → UC-M13-010 (UC con). Không đưa UC con lên tổng quan, không đổi đích thành core hỗ trợ AI. Chỉ số từ feedback cùng kỳ, vẫn tính khi AI tắt, không gọi provider. | FR-M15-02.07, FR-M15-02.08, FR-M15-02.09, FR-M13-10, BR-M13-29 |


## 7. Truy vết và tài liệu nguồn

### 7.1 Đối chiếu đủ 16 module

Mỗi core nguồn thuộc đúng một trong hai tập: **được chọn (51)** hoặc **không vẽ (13)**. Không có core nguồn bị thay tên, thay ID hoặc mất quyết định lựa chọn. Tất cả FR nguồn đang Đã chốt; US module đang Chờ duyệt, không tự nâng trạng thái phê duyệt khi tổng hợp.

<!-- selected:module-models -->
| Module | FR / phiên bản | US nguồn | UC được chọn | UC không vẽ |
|---|---|---|---|---|
| M01 | [FR-M01](../fr/FR-M01.md) v1.10 | [US-M01](US-M01.md) | [UC-M01-020](#uc-m01-020), [UC-M01-021](#uc-m01-021), [UC-M01-022](#uc-m01-022), [UC-M01-023](#uc-m01-023), [UC-M01-024](#uc-m01-024) | [UC-M01-025](US-M01.md#uc-m01-025) |
| M02 | [FR-M02](../fr/FR-M02.md) v1.6 | [US-M02](US-M02.md) | [UC-M02-010](#uc-m02-010), [UC-M02-020](#uc-m02-020), [UC-M02-030](#uc-m02-030) | - |
| M03 | [FR-M03](../fr/FR-M03.md) v1.10 | [US-M03](US-M03.md) | [UC-M03-020](#uc-m03-020), [UC-M03-021](#uc-m03-021), [UC-M03-022](#uc-m03-022), [UC-M03-023](#uc-m03-023) | - |
| M04 | [FR-M04](../fr/FR-M04.md) v1.4 | [US-M04](US-M04.md) | [UC-M04-020](#uc-m04-020), [UC-M04-030](#uc-m04-030) | [UC-M04-010](US-M04.md#uc-m04-010) |
| M05 | [FR-M05](../fr/FR-M05.md) v1.7 | [US-M05](US-M05.md) | [UC-M05-021](#uc-m05-021), [UC-M05-022](#uc-m05-022), [UC-M05-023](#uc-m05-023) | [UC-M05-020](US-M05.md#uc-m05-020) |
| M06 | [FR-M06](../fr/FR-M06.md) v1.5 | [US-M06](US-M06.md) | [UC-M06-020](#uc-m06-020) | [UC-M06-021](US-M06.md#uc-m06-021), [UC-M06-022](US-M06.md#uc-m06-022) |
| M07 | [FR-M07](../fr/FR-M07.md) v1.5 | [US-M07](US-M07.md) | [UC-M07-020](#uc-m07-020), [UC-M07-021](#uc-m07-021) | [UC-M07-022](US-M07.md#uc-m07-022), [UC-M07-023](US-M07.md#uc-m07-023) |
| M08 | [FR-M08](../fr/FR-M08.md) v1.7 | [US-M08](US-M08.md) | [UC-M08-020](#uc-m08-020), [UC-M08-021](#uc-m08-021), [UC-M08-022](#uc-m08-022), [UC-M08-023](#uc-m08-023), [UC-M08-024](#uc-m08-024), [UC-M08-025](#uc-m08-025) | - |
| M09 | [FR-M09](../fr/FR-M09.md) v1.2 | [US-M09](US-M09.md) | [UC-M09-020](#uc-m09-020), [UC-M09-021](#uc-m09-021) | [UC-M09-022](US-M09.md#uc-m09-022) |
| M10 | [FR-M10](../fr/FR-M10.md) v1.4 | [US-M10](US-M10.md) | [UC-M10-020](#uc-m10-020), [UC-M10-021](#uc-m10-021), [UC-M10-022](#uc-m10-022), [UC-M10-023](#uc-m10-023) | - |
| M11 | [FR-M11](../fr/FR-M11.md) v1.3 | [US-M11](US-M11.md) | [UC-M11-030](#uc-m11-030), [UC-M11-031](#uc-m11-031), [UC-M11-032](#uc-m11-032), [UC-M11-033](#uc-m11-033), [UC-M11-034](#uc-m11-034) | - |
| M12 | [FR-M12](../fr/FR-M12.md) v1.1 | [US-M12](US-M12.md) | [UC-M12-020](#uc-m12-020), [UC-M12-021](#uc-m12-021) | [UC-M12-022](US-M12.md#uc-m12-022) |
| M13 | [FR-M13](../fr/FR-M13.md) v1.3 | [US-M13](US-M13.md) | [UC-M13-023](#uc-m13-023) | [UC-M13-020](US-M13.md#uc-m13-020), [UC-M13-021](US-M13.md#uc-m13-021), [UC-M13-022](US-M13.md#uc-m13-022), [UC-M13-024](US-M13.md#uc-m13-024) |
| M14 | [FR-M14](../fr/FR-M14.md) v1.1 | [US-M14](US-M14.md) | [UC-M14-020](#uc-m14-020), [UC-M14-021](#uc-m14-021), [UC-M14-022](#uc-m14-022), [UC-M14-023](#uc-m14-023) | - |
| M15 | [FR-M15](../fr/FR-M15.md) v1.1 | [US-M15](US-M15.md) | [UC-M15-020](#uc-m15-020), [UC-M15-021](#uc-m15-021), [UC-M15-022](#uc-m15-022) | - |
| M16 | [FR-M16](../fr/FR-M16.md) v1.0 | [US-M16](US-M16.md) | [UC-M16-030](#uc-m16-030), [UC-M16-031](#uc-m16-031), [UC-M16-032](#uc-m16-032), [UC-M16-033](#uc-m16-033) | - |

### 7.2 Truy vết nhóm FR

Bảng là **kiểm kê tổng quan**, không chứng nhận đặc tả lại toàn bộ FR chi tiết/BR. Cột UC được chọn chỉ lấy nguồn core trực tiếp có căn cứ trong catalog module. Các nhóm chỉ hỗ trợ không bị ép ánh xạ sang một core khác; chúng trỏ về core hỗ trợ hoặc RULE/AUT tại module.

<details>
<summary>Mở bảng 174 nhóm FR còn hiệu lực</summary>

<!-- selected:trace -->
| Nhóm FR | Nội dung | UC có mặt trên tổng quan | Phần giữ ở mô hình module |
|---|---|---|---|
| FR-M01-01 | Đăng ký tài khoản bằng email | [UC-M01-020](#uc-m01-020) | [chi tiết M01](US-M01.md) |
| FR-M01-02 | Xác minh email | [UC-M01-020](#uc-m01-020) | [chi tiết M01](US-M01.md) |
| FR-M01-03 | Thiết lập tài khoản | [UC-M01-020](#uc-m01-020) | [chi tiết M01](US-M01.md) |
| FR-M01-04 | Đăng ký, đăng nhập bằng Google | [UC-M01-020](#uc-m01-020), [UC-M01-021](#uc-m01-021) | [chi tiết M01](US-M01.md) |
| FR-M01-05 | Đăng nhập bằng email và mật khẩu | [UC-M01-021](#uc-m01-021) | [chi tiết M01](US-M01.md) |
| FR-M01-06 | Duy trì phiên đăng nhập | [UC-M01-021](#uc-m01-021) | [chi tiết M01](US-M01.md) |
| FR-M01-07 | Đăng xuất | [UC-M01-021](#uc-m01-021) | [chi tiết M01](US-M01.md) |
| FR-M01-08 | Đổi mật khẩu | [UC-M01-022](#uc-m01-022) | [chi tiết M01](US-M01.md) |
| FR-M01-09 | Lấy lại mật khẩu | [UC-M01-022](#uc-m01-022) | [chi tiết M01](US-M01.md) |
| FR-M01-10 | Vô hiệu hóa tài khoản | [UC-M01-023](#uc-m01-023) | [chi tiết M01](US-M01.md) |
| FR-M01-11 | Kích hoạt lại tài khoản | [UC-M01-023](#uc-m01-023) | [chi tiết M01](US-M01.md) |
| FR-M01-12 | Tự xóa tài khoản hết hạn vô hiệu hóa | [UC-M01-023](#uc-m01-023) | [chi tiết M01](US-M01.md) |
| FR-M01-13 | Hiển thị nội dung của tài khoản đã vô hiệu hóa hoặc đã xóa | [UC-M01-023](#uc-m01-023) | [chi tiết M01](US-M01.md) |
| FR-M01-14 | Nhắc tên người dùng (@mention) | Không có oval riêng | [UC-M01-025](US-M01.md#uc-m01-025); [chi tiết M01](US-M01.md) |
| FR-M01-15 | Xem trang Privacy Policy/ToS | [UC-M01-024](#uc-m01-024) | [chi tiết M01](US-M01.md) |
| FR-M01-16 | Đồng ý lại khi chính sách đổi | [UC-M01-024](#uc-m01-024) | [chi tiết M01](US-M01.md) |
| FR-M02-01 | Xem trang hồ sơ | [UC-M02-010](#uc-m02-010) | [chi tiết M02](US-M02.md) |
| FR-M02-02 | Xem danh sách người theo dõi và đang theo dõi | [UC-M02-010](#uc-m02-010) | [chi tiết M02](US-M02.md) |
| FR-M02-03 | Sửa thông tin hồ sơ | [UC-M02-020](#uc-m02-020) | [chi tiết M02](US-M02.md) |
| FR-M02-04 | Đổi avatar | [UC-M02-020](#uc-m02-020) | [chi tiết M02](US-M02.md) |
| FR-M02-05 | Lưu bài viết (Bookmark) | [UC-M02-030](#uc-m02-030) | [chi tiết M02](US-M02.md) |
| FR-M02-06 | Bỏ lưu bài viết | [UC-M02-030](#uc-m02-030) | [chi tiết M02](US-M02.md) |
| FR-M02-07 | Xem danh sách bài đã lưu | [UC-M02-030](#uc-m02-030) | [chi tiết M02](US-M02.md) |
| FR-M03-01 | Soạn và lưu nháp bài viết | [UC-M03-020](#uc-m03-020) | [chi tiết M03](US-M03.md) |
| FR-M03-02 | Đính kèm tệp vào bài viết | [UC-M03-020](#uc-m03-020), [UC-M03-022](#uc-m03-022) | [chi tiết M03](US-M03.md) |
| FR-M03-03 | Tạo bình chọn trong bài viết | [UC-M03-020](#uc-m03-020) | [chi tiết M03](US-M03.md) |
| FR-M03-04 | Gửi bài viết để đăng | [UC-M03-020](#uc-m03-020) | [chi tiết M03](US-M03.md) |
| FR-M03-05 | Quét nội dung bài viết | [UC-M03-020](#uc-m03-020) | [chi tiết M03](US-M03.md) |
| FR-M03-06 | Duyệt bài viết chờ đăng | [UC-M03-020](#uc-m03-020) | [chi tiết M03](US-M03.md) |
| FR-M03-07 | Xem bài viết | [UC-M03-021](#uc-m03-021), [UC-M03-023](#uc-m03-023) | [chi tiết M03](US-M03.md) |
| FR-M03-08 | Bình chọn trong poll | [UC-M03-021](#uc-m03-021) | [chi tiết M03](US-M03.md) |
| FR-M03-09 | Đổi hạn, kết thúc và thêm lựa chọn cho poll | [UC-M03-021](#uc-m03-021) | [chi tiết M03](US-M03.md) |
| FR-M03-10 | Kết thúc poll khi hết hạn | [UC-M03-021](#uc-m03-021) | [chi tiết M03](US-M03.md) |
| FR-M03-11 | Sửa bài viết đã gửi | [UC-M03-022](#uc-m03-022) | [chi tiết M03](US-M03.md) |
| FR-M03-12 | Xem lịch sử sửa bài viết | [UC-M03-022](#uc-m03-022) | [chi tiết M03](US-M03.md) |
| FR-M03-13 | Tự ẩn và hiện lại bài viết | [UC-M03-023](#uc-m03-023) | [chi tiết M03](US-M03.md) |
| FR-M03-14 | Khóa và mở khóa bài viết | [UC-M03-023](#uc-m03-023) | [chi tiết M03](US-M03.md) |
| FR-M03-15 | Xóa bài viết | [UC-M03-023](#uc-m03-023) | [chi tiết M03](US-M03.md) |
| FR-M03-16 | Khôi phục bài viết đã xóa | [UC-M03-023](#uc-m03-023) | [chi tiết M03](US-M03.md) |
| FR-M03-17 | Chuyển bài hết hạn khôi phục sang Đã xóa hẳn | [UC-M03-023](#uc-m03-023) | [chi tiết M03](US-M03.md) |
| FR-M04-01 | Xem bình luận của bài viết | Không có oval riêng | [UC-M04-010](US-M04.md#uc-m04-010); [chi tiết M04](US-M04.md) |
| FR-M04-02 | Viết bình luận vào bài viết | [UC-M04-020](#uc-m04-020) | [chi tiết M04](US-M04.md) |
| FR-M04-03 | Trả lời bình luận | [UC-M04-020](#uc-m04-020) | [chi tiết M04](US-M04.md) |
| FR-M04-04 | Sửa bình luận | [UC-M04-030](#uc-m04-030) | [chi tiết M04](US-M04.md) |
| FR-M04-05 | Xóa bình luận | [UC-M04-030](#uc-m04-030) | [chi tiết M04](US-M04.md) |
| FR-M04-06 | Xem lại bình luận đã bị xử lý của mình | Không có oval riêng | [UC-M04-010](US-M04.md#uc-m04-010); [chi tiết M04](US-M04.md) |
| FR-M05-01 | Gán Topic cho bài viết | Không có oval riêng | [UC-M05-020](US-M05.md#uc-m05-020); [chi tiết M05](US-M05.md) |
| FR-M05-02 | Gợi ý Topic bằng AI | Không có oval riêng | [UC-M05-020](US-M05.md#uc-m05-020); [chi tiết M05](US-M05.md) |
| FR-M05-03 | Gắn Tag cho bài viết | Không có oval riêng | [UC-M05-020](US-M05.md#uc-m05-020); [chi tiết M05](US-M05.md) |
| FR-M05-04 | Xem danh sách Topic và Tag | [UC-M05-021](#uc-m05-021) | [chi tiết M05](US-M05.md) |
| FR-M05-05 | Tính Trending Topic và Trending Tag | [UC-M05-021](#uc-m05-021) | [chi tiết M05](US-M05.md) |
| FR-M05-06 | Thêm Topic | [UC-M05-022](#uc-m05-022) | [chi tiết M05](US-M05.md) |
| FR-M05-07 | Gộp Topic | [UC-M05-022](#uc-m05-022) | [chi tiết M05](US-M05.md) |
| FR-M05-08 | Xóa Topic | [UC-M05-022](#uc-m05-022) | [chi tiết M05](US-M05.md) |
| FR-M05-09 | Vô hiệu hóa Tag | [UC-M05-023](#uc-m05-023) | [chi tiết M05](US-M05.md) |
| FR-M05-10 | Kích hoạt lại Tag | [UC-M05-023](#uc-m05-023) | [chi tiết M05](US-M05.md) |
| FR-M05-11 | Đổi Topic, Tag trên bài viết của người khác | [UC-M05-023](#uc-m05-023) | [chi tiết M05](US-M05.md) |
| FR-M06-01 | Gợi ý người dùng, Tag, Topic, Group khi gõ | Không có oval riêng | [UC-M06-021](US-M06.md#uc-m06-021); [chi tiết M06](US-M06.md) |
| FR-M06-02 | Tìm bài viết | [UC-M06-020](#uc-m06-020) | [chi tiết M06](US-M06.md) |
| FR-M06-03 | Tìm người dùng, Tag, Topic, Group | [UC-M06-020](#uc-m06-020) | [UC-M06-021](US-M06.md#uc-m06-021); [chi tiết M06](US-M06.md) |
| FR-M06-04 | Lọc và sắp xếp kết quả bài viết | [UC-M06-020](#uc-m06-020) | [chi tiết M06](US-M06.md) |
| FR-M06-05 | Dùng lịch sử tìm kiếm | Không có oval riêng | [UC-M06-022](US-M06.md#uc-m06-022); [chi tiết M06](US-M06.md) |
| FR-M07-01 | Theo dõi và bỏ theo dõi người dùng, Topic | [UC-M07-020](#uc-m07-020) | [chi tiết M07](US-M07.md) |
| FR-M07-02 | Tạo thông báo khi có sự kiện | [UC-M07-021](#uc-m07-021) | [chi tiết M07](US-M07.md) |
| FR-M07-03 | Đẩy thông báo mới tới người dùng đang mở ứng dụng | [UC-M07-021](#uc-m07-021) | [chi tiết M07](US-M07.md) |
| FR-M07-04 | Gửi email thông báo | [UC-M07-021](#uc-m07-021) | [chi tiết M07](US-M07.md) |
| FR-M07-05 | Xem thông báo | [UC-M07-021](#uc-m07-021) | [chi tiết M07](US-M07.md) |
| FR-M07-06 | Đánh dấu thông báo đã đọc | [UC-M07-021](#uc-m07-021) | [chi tiết M07](US-M07.md) |
| FR-M07-07 | Báo tin nhắn mới qua popup và biểu tượng Tin nhắn | Không có oval riêng | [UC-M07-023](US-M07.md#uc-m07-023); [chi tiết M07](US-M07.md) |
| FR-M07-08 | Tắt thông báo cho một bài viết | Không có oval riêng | [UC-M07-022](US-M07.md#uc-m07-022); [chi tiết M07](US-M07.md) |
| FR-M07-09 | Tắt thông báo Chat | Không có oval riêng | [UC-M07-022](US-M07.md#uc-m07-022); [chi tiết M07](US-M07.md) |
| FR-M08-01 | Báo cáo bài viết, bình luận, người dùng hoặc nhóm | [UC-M08-020](#uc-m08-020) | [chi tiết M08](US-M08.md) |
| FR-M08-02 | Xem hàng chờ vụ báo cáo | [UC-M08-021](#uc-m08-021) | [chi tiết M08](US-M08.md) |
| FR-M08-03 | Nhận và nhả vụ báo cáo | [UC-M08-021](#uc-m08-021) | [chi tiết M08](US-M08.md) |
| FR-M08-04 | Xem chi tiết vụ báo cáo | [UC-M08-021](#uc-m08-021) | [chi tiết M08](US-M08.md) |
| FR-M08-05 | Kết luận vụ báo cáo | [UC-M08-021](#uc-m08-021) | [chi tiết M08](US-M08.md) |
| FR-M08-06 | Ẩn bài viết, bình luận vi phạm | [UC-M08-022](#uc-m08-022) | [chi tiết M08](US-M08.md) |
| FR-M08-07 | Xét nội dung bị gắn cờ | [UC-M08-022](#uc-m08-022) | [chi tiết M08](US-M08.md) |
| FR-M08-08 | Quét AI luồng bình luận | [UC-M08-022](#uc-m08-022) | [chi tiết M08](US-M08.md) |
| FR-M08-09 | Tự cảnh cáo bằng AI | [UC-M08-022](#uc-m08-022), [UC-M08-023](#uc-m08-023) | [chi tiết M08](US-M08.md) |
| FR-M08-10 | Cảnh cáo người dùng | [UC-M08-023](#uc-m08-023) | [chi tiết M08](US-M08.md) |
| FR-M08-11 | Bỏ cảnh cáo do AI ra | [UC-M08-023](#uc-m08-023) | [chi tiết M08](US-M08.md) |
| FR-M08-12 | Giảm mức cảnh cáo khi hết thời gian thử thách | [UC-M08-023](#uc-m08-023) | [chi tiết M08](US-M08.md) |
| FR-M08-13 | Xem mức cảnh cáo của mình | [UC-M08-023](#uc-m08-023) | [chi tiết M08](US-M08.md) |
| FR-M08-14 | Ban người dùng | [UC-M08-023](#uc-m08-023) | [chi tiết M08](US-M08.md) |
| FR-M08-15 | Gỡ ban | [UC-M08-023](#uc-m08-023) | [chi tiết M08](US-M08.md) |
| FR-M08-16 | Ghi nhật ký kiểm duyệt | [UC-M08-025](#uc-m08-025) | [chi tiết M08](US-M08.md) |
| FR-M08-17 | Xem nhật ký kiểm duyệt | [UC-M08-025](#uc-m08-025) | [chi tiết M08](US-M08.md) |
| FR-M08-18 | Ẩn, khóa và mở khóa nhóm | [UC-M08-024](#uc-m08-024) | [chi tiết M08](US-M08.md) |
| FR-M09-01 | Gửi khiếu nại | [UC-M09-020](#uc-m09-020) | [chi tiết M09](US-M09.md) |
| FR-M09-02 | Xem khiếu nại của mình | [UC-M09-020](#uc-m09-020) | [chi tiết M09](US-M09.md) |
| FR-M09-03 | Xem hàng chờ khiếu nại | [UC-M09-021](#uc-m09-021) | [chi tiết M09](US-M09.md) |
| FR-M09-04 | Nhận và nhả khiếu nại | [UC-M09-021](#uc-m09-021) | [chi tiết M09](US-M09.md) |
| FR-M09-06 | Xem chi tiết khiếu nại | [UC-M09-021](#uc-m09-021) | [chi tiết M09](US-M09.md) |
| FR-M09-07 | Kết luận khiếu nại | [UC-M09-021](#uc-m09-021) | [chi tiết M09](US-M09.md) |
| FR-M09-08 | Đảo ngược xử lý khi khiếu nại được chấp nhận | Không có oval riêng | [UC-M09-022](US-M09.md#uc-m09-022); [chi tiết M09](US-M09.md) |
| FR-M10-01 | Xem người dùng trong Admin Panel | [UC-M10-020](#uc-m10-020) | [chi tiết M10](US-M10.md) |
| FR-M10-02 | Đề xuất người dùng làm Mod | [UC-M10-020](#uc-m10-020) | [chi tiết M10](US-M10.md) |
| FR-M10-03 | Trả lời đề xuất làm Mod hoặc làm Admin | [UC-M10-020](#uc-m10-020) | [chi tiết M10](US-M10.md) |
| FR-M10-04 | Giáng cấp Mod | [UC-M10-020](#uc-m10-020) | [chi tiết M10](US-M10.md) |
| FR-M10-05 | Tự từ chức vai trò Mod hoặc Admin | [UC-M10-020](#uc-m10-020) | [chi tiết M10](US-M10.md) |
| FR-M10-06 | Thu hồi vai trò Mod khi Mod bị ban | [UC-M10-020](#uc-m10-020) | [chi tiết M10](US-M10.md) |
| FR-M10-07 | Đề xuất làm Admin | [UC-M10-020](#uc-m10-020) | [chi tiết M10](US-M10.md) |
| FR-M10-08 | Thu hồi vai trò Admin | [UC-M10-020](#uc-m10-020) | [chi tiết M10](US-M10.md) |
| FR-M10-09 | Bật, tắt công tắc AI | [UC-M10-021](#uc-m10-021) | [chi tiết M10](US-M10.md) |
| FR-M10-10 | Bật, tắt chế độ bảo trì | [UC-M10-021](#uc-m10-021) | [chi tiết M10](US-M10.md) |
| FR-M10-11 | Bật, tắt tạm dừng đăng ký | [UC-M10-021](#uc-m10-021) | [chi tiết M10](US-M10.md) |
| FR-M10-12 | Bật, tắt cờ tính năng | [UC-M10-021](#uc-m10-021) | [chi tiết M10](US-M10.md) |
| FR-M10-13 | Đặt, sửa, gỡ banner thông báo toàn trang | [UC-M10-022](#uc-m10-022) | [chi tiết M10](US-M10.md) |
| FR-M10-14 | Ghi nhật ký thao tác Admin | [UC-M10-023](#uc-m10-023) | [chi tiết M10](US-M10.md) |
| FR-M10-15 | Xem nhật ký thao tác Admin | [UC-M10-023](#uc-m10-023) | [chi tiết M10](US-M10.md) |
| FR-M11-01 | Tạo nhóm | [UC-M11-030](#uc-m11-030) | [chi tiết M11](US-M11.md) |
| FR-M11-02 | Sửa thông tin và cài đặt nhóm | [UC-M11-030](#uc-m11-030) | [chi tiết M11](US-M11.md) |
| FR-M11-03 | Xem danh sách nhóm và trang nhóm | [UC-M11-031](#uc-m11-031) | [chi tiết M11](US-M11.md) |
| FR-M11-04 | Tham gia nhóm | [UC-M11-032](#uc-m11-032) | [chi tiết M11](US-M11.md) |
| FR-M11-05 | Mời người khác vào nhóm | [UC-M11-032](#uc-m11-032) | [chi tiết M11](US-M11.md) |
| FR-M11-06 | Duyệt yêu cầu tham gia | [UC-M11-032](#uc-m11-032) | [chi tiết M11](US-M11.md) |
| FR-M11-07 | Chặn người gửi yêu cầu tham gia | [UC-M11-032](#uc-m11-032) | [chi tiết M11](US-M11.md) |
| FR-M11-08 | Bổ nhiệm, giáng Group Mod | [UC-M11-032](#uc-m11-032) | [chi tiết M11](US-M11.md) |
| FR-M11-09 | Kick thành viên khỏi nhóm | [UC-M11-032](#uc-m11-032) | [chi tiết M11](US-M11.md) |
| FR-M11-10 | Rời nhóm | [UC-M11-032](#uc-m11-032) | [chi tiết M11](US-M11.md) |
| FR-M11-11 | Tự chuyển quyền Owner khi Owner mất quyền | [UC-M11-032](#uc-m11-032) | [chi tiết M11](US-M11.md) |
| FR-M11-12 | Đăng bài trong nhóm | [UC-M11-033](#uc-m11-033) | [chi tiết M11](US-M11.md) |
| FR-M11-13 | Duyệt bài chờ đăng của nhóm | [UC-M11-033](#uc-m11-033), [UC-M11-034](#uc-m11-034) | [chi tiết M11](US-M11.md) |
| FR-M11-14 | Gỡ bài và bình luận khỏi nhóm | [UC-M11-034](#uc-m11-034) | [chi tiết M11](US-M11.md) |
| FR-M11-15 | Xóa nhóm | [UC-M11-030](#uc-m11-030) | [chi tiết M11](US-M11.md) |
| FR-M11-16 | Áp dụng trạng thái Ẩn, Khóa của nhóm | Không có oval riêng | [AUT-M11-006](US-M11.md#aut-m11-006); [chi tiết M11](US-M11.md) |
| FR-M11-17 | Chặn thao tác nhóm khi cờ Group tắt | Không có oval riêng | [RULE-M11-006](US-M11.md#rule-m11-006); [chi tiết M11](US-M11.md) |
| FR-M12-01 | Upvote và rút lại upvote | [UC-M12-020](#uc-m12-020) | [chi tiết M12](US-M12.md) |
| FR-M12-02 | Cập nhật điểm đóng góp | [UC-M12-020](#uc-m12-020) | [UC-M12-022](US-M12.md#uc-m12-022); [chi tiết M12](US-M12.md) |
| FR-M12-03 | Trao huy hiệu theo mốc điểm | Không có oval riêng | [UC-M12-022](US-M12.md#uc-m12-022); [chi tiết M12](US-M12.md) |
| FR-M12-04 | Tính bảng xếp hạng định kỳ | [UC-M12-021](#uc-m12-021) | [chi tiết M12](US-M12.md) |
| FR-M12-05 | Chốt chu kỳ và trao danh hiệu "Ngôi sao tuần" | [UC-M12-021](#uc-m12-021) | [UC-M12-022](US-M12.md#uc-m12-022); [chi tiết M12](US-M12.md) |
| FR-M12-06 | Xem bảng xếp hạng | [UC-M12-021](#uc-m12-021) | [chi tiết M12](US-M12.md) |
| FR-M12-07 | Gắn nhãn "Tài khoản đã bị khóa" | Không có oval riêng | [UC-M12-022](US-M12.md#uc-m12-022); [chi tiết M12](US-M12.md) |
| FR-M12-08 | Chặn thao tác Gamification khi cờ tắt | Không có oval riêng | [RULE-M12-006](US-M12.md#rule-m12-006); [chi tiết M12](US-M12.md) |
| FR-M13-01 | Gọi dịch vụ AI | Không có oval riêng | [UC-M13-020](US-M13.md#uc-m13-020); [chi tiết M13](US-M13.md) |
| FR-M13-02 | Chấm điểm kiểm duyệt bài viết, bình luận | Không có oval riêng | [UC-M13-020](US-M13.md#uc-m13-020); [chi tiết M13](US-M13.md) |
| FR-M13-03 | Tạo embedding cho bài viết | Không có oval riêng | [UC-M13-021](US-M13.md#uc-m13-021); [chi tiết M13](US-M13.md) |
| FR-M13-04 | Tạo embedding cho truy vấn tìm kiếm | Không có oval riêng | [UC-M13-021](US-M13.md#uc-m13-021); [chi tiết M13](US-M13.md) |
| FR-M13-05 | Lấy gợi ý Topic từ AI | Không có oval riêng | [UC-M13-022](US-M13.md#uc-m13-022); [chi tiết M13](US-M13.md) |
| FR-M13-06 | Tạo và giữ tạm tóm tắt bài viết | [UC-M13-023](#uc-m13-023) | [chi tiết M13](US-M13.md) |
| FR-M13-07 | Yêu cầu xem tóm tắt bài viết | [UC-M13-023](#uc-m13-023) | [chi tiết M13](US-M13.md) |
| FR-M13-08 | Ghi nhật ký quyết định AI | Không có oval riêng | [UC-M13-024](US-M13.md#uc-m13-024); [chi tiết M13](US-M13.md) |
| FR-M13-09 | Xem nhật ký quyết định AI | Không có oval riêng | [UC-M13-024](US-M13.md#uc-m13-024); [chi tiết M13](US-M13.md) |
| FR-M13-10 | Đánh giá chất lượng gợi ý Topic | Không có oval riêng | [UC-M13-024](US-M13.md#uc-m13-024); [chi tiết M13](US-M13.md) |
| FR-M14-01 | Mở trang chủ feed | [UC-M14-020](#uc-m14-020) | [chi tiết M14](US-M14.md) |
| FR-M14-02 | Xem tab Trending | [UC-M14-020](#uc-m14-020) | [chi tiết M14](US-M14.md) |
| FR-M14-03 | Tính điểm Trending Post | [UC-M14-020](#uc-m14-020) | [chi tiết M14](US-M14.md) |
| FR-M14-04 | Xem tab Following | [UC-M14-021](#uc-m14-021) | [chi tiết M14](US-M14.md) |
| FR-M14-05 | Xem tab Group | [UC-M14-022](#uc-m14-022) | [chi tiết M14](US-M14.md) |
| FR-M14-06 | Xem tab Newest | [UC-M14-023](#uc-m14-023) | [chi tiết M14](US-M14.md) |
| FR-M14-07 | Tải thêm bài khi cuộn | [UC-M14-021](#uc-m14-021), [UC-M14-022](#uc-m14-022), [UC-M14-023](#uc-m14-023) | [chi tiết M14](US-M14.md) |
| FR-M14-08 | Xem bài mới qua banner | [UC-M14-021](#uc-m14-021), [UC-M14-022](#uc-m14-022), [UC-M14-023](#uc-m14-023) | [chi tiết M14](US-M14.md) |
| FR-M15-01 | Xem thống kê người dùng | [UC-M15-020](#uc-m15-020) | [chi tiết M15](US-M15.md) |
| FR-M15-02 | Xem thống kê nội dung | [UC-M15-021](#uc-m15-021) | [chi tiết M15](US-M15.md) |
| FR-M15-03 | Xem thống kê kiểm duyệt | [UC-M15-022](#uc-m15-022) | [chi tiết M15](US-M15.md) |
| FR-M16-01 | Bắt đầu trò chuyện 1-1 | [UC-M16-030](#uc-m16-030) | [chi tiết M16](US-M16.md) |
| FR-M16-02 | Tạo nhóm chat | [UC-M16-032](#uc-m16-032) | [chi tiết M16](US-M16.md) |
| FR-M16-03 | Xem hộp thư Chat | [UC-M16-030](#uc-m16-030) | [chi tiết M16](US-M16.md) |
| FR-M16-04 | Xem cuộc trò chuyện và lịch sử tin nhắn | [UC-M16-030](#uc-m16-030) | [chi tiết M16](US-M16.md) |
| FR-M16-05 | Gửi tin nhắn | [UC-M16-031](#uc-m16-031) | [chi tiết M16](US-M16.md) |
| FR-M16-06 | Thu hồi tin nhắn | [UC-M16-031](#uc-m16-031) | [chi tiết M16](US-M16.md) |
| FR-M16-07 | Ghi nhận đã đọc và hiển thị Đã xem | [UC-M16-030](#uc-m16-030), [UC-M16-031](#uc-m16-031) | [chi tiết M16](US-M16.md) |
| FR-M16-08 | Thêm, mời thành viên vào nhóm chat | [UC-M16-032](#uc-m16-032) | [chi tiết M16](US-M16.md) |
| FR-M16-09 | Bật, tắt duyệt thành viên mới | [UC-M16-033](#uc-m16-033) | [chi tiết M16](US-M16.md) |
| FR-M16-10 | Duyệt người chờ vào nhóm chat | [UC-M16-032](#uc-m16-032) | [chi tiết M16](US-M16.md) |
| FR-M16-11 | Xóa thành viên khỏi nhóm chat | [UC-M16-033](#uc-m16-033) | [chi tiết M16](US-M16.md) |
| FR-M16-12 | Đổi tên nhóm chat | [UC-M16-033](#uc-m16-033) | [chi tiết M16](US-M16.md) |
| FR-M16-13 | Chuyển quyền Admin nhóm chat | [UC-M16-033](#uc-m16-033) | [chi tiết M16](US-M16.md) |
| FR-M16-14 | Rời nhóm chat | [UC-M16-033](#uc-m16-033) | [chi tiết M16](US-M16.md) |
| FR-M16-15 | Chặn thao tác Chat khi cờ tính năng tắt | [UC-M16-030](#uc-m16-030), [UC-M16-031](#uc-m16-031), [UC-M16-032](#uc-m16-032), [UC-M16-033](#uc-m16-033) | [chi tiết M16](US-M16.md) |
| FR-M16-16 | Xin gia nhập nhóm chat qua link mời | [UC-M16-032](#uc-m16-032) | [chi tiết M16](US-M16.md) |
| FR-M16-17 | Tự tắt duyệt khi Admin nhóm chat không thể khôi phục | [UC-M16-033](#uc-m16-033) | [chi tiết M16](US-M16.md) |

</details>

FR-M09-05 đã bỏ trong [FR-M09](../fr/FR-M09.md); quy tắc lọc chuyển Admin nằm ở FR-M09-03.09. Không tạo lại một UC “Chuyển lên Admin”.

## 8. Kiểm tra và giới hạn

### 8.1 Kết quả kiểm tra

<!-- selected:qa -->
| Hạng mục | Phương pháp | Kết quả / giới hạn |
|---|---|---|
| Nguồn UC | Đối chiếu từng dòng catalog với core trong US-M01–US-M16; kiểm ID/tên/tier/level/actor/owner/sources | Audit độc lập exit 0, errors=0; 51/51 dòng khớp nguồn, không UC mới hoặc UC con trong danh mục. |
| Lựa chọn và truy vết | Kiểm 51 chọn + 13 không vẽ = 64 core nguồn; 174 nhóm FR có đích core/RULE/AUT ở mô hình owner | Đủ 64 core trong hai tập không giao nhau, đủ 16 module và 174 nhóm FR còn hiệu lực; không ép các nhóm hỗ trợ thành mục tiêu tổng quan. |
| Sơ đồ | PlantUML 1.2026.8; chạy -checkonly, -tsvg, -tpng trên SYS-overview-selected.puml trong workspace agent; xem PNG tạm | Ba lệnh exit 0; đã xem ảnh cuối 922×3860. Một SVG bàn giao; chỉ một boundary iShare, không package/khung con. Nguồn/PNG chỉ ở workspace. |
| Mô hình ↔ SVG | So node/nhãn/actor, association rút gọn và kế thừa actor, endpoint/nhãn/hướng extend, EP; kiểm actor ngoài boundary và UC bên trong | Khớp 51 UC, 13 actor, 79 association, 8 kế thừa actor và 1 extend (88 cạnh tổng). SVG có đúng 1 boundary, không khối con; mọi actor ngoài và mọi oval trong iShare. |
| Liên kết và ID | Kiểm anchor/link local và liên tài liệu, mã FR/BR tồn tại, không mã UC tự tạo hoặc UC con trong catalog/hình | 52 anchor duy nhất, 582 liên kết hợp lệ; mọi UC được nhắc có thật tại module, mọi UC trên hình là core đã chọn. |
| Nguồn không đổi | So SHA-256 16 US module với baseline trước chỉnh tổng quan; xem git status/diff | 16/16 US module giữ nguyên hash. Chỉ thay bộ tổng quan; thư mục đầu ra còn một file SYS-overview.svg. |
| Checker hiện có | check_us.py --final đã kiểm 16 US đầu vào: 16/16 exit 0, errors=0; tổng 17 warning | Không báo checker chuẩn pass cho view chọn lọc này: mode overview của công cụ đang yêu cầu lấy đủ toàn bộ core từng module. Yêu cầu hiện tại là lấy tập con; audit độc lập kiểm đúng hợp đồng đó. Không sửa checker/skill để chạy vừa kết quả. |
| Phê duyệt | Đối chiếu quyền thực hiện và chấp nhận mô hình | Chờ duyệt; chưa có phê duyệt kết quả cuối. |

### 8.2 Giới hạn và điểm cần giữ khi review

- 51 mục tiêu không phải một luồng tuần tự chạy cả hệ thống. Summary giữ nguyên nghĩa/phạm vi nguồn; mỗi instance theo nhánh và cổng quyền riêng.
- Các quan hệ include/extend/generalization có endpoint ở chi tiết module không được nâng hoặc đổi đích sang core trên hình tổng quan. Xem mục 6 để phân biệt giao tiếp với quan hệ UML.
- UC-M13-023 → UC-M03-021 là quan hệ được xác định tại tổng quan từ hành vi FR hiện có, không phải tuyên bố cặp này đã có trong bảng quan hệ của US module. EP được ghi tại tài liệu này; không sửa tài liệu module.
- NOTE-M13-04 vẫn còn: có feedback nhưng tổng số Topic gợi ý bằng 0 chưa được nguồn quy định kết quả metric. Không suy ra 0%, 100% hoặc Không có dữ liệu cho trường hợp này.
- Mọi tác vụ tự động/quy tắc/UC hỗ trợ vẫn ở module; việc lọc view không bỏ nghiệp vụ hoặc đóng các note chưa rõ của nguồn.
- Tài liệu là tổng quan nghiệp vụ với một boundary, không là kiến trúc module hoặc activity diagram. Chi tiết thực hiện xem [US-M01](US-M01.md) đến [US-M16](US-M16.md).

### 8.3 Trạng thái bàn giao

**Chờ duyệt.** Đã thực hiện quyền chỉnh sửa và kiểm tra, chưa coi phản hồi yêu cầu sửa là phê duyệt kết quả cuối. Tài liệu FR, US module, register và skill giữ nguyên.

