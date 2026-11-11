# Kịch bản nghiệp vụ — M02 User Profile

[Vietnamese Doc] — Tái kiểm 11/11/2026 — Skill scenarios v1.4.

Mục đích: triển khai các chức năng actor thực hiện hoàn chỉnh từ FR + US. Boundary là toàn iShare: mọi module nội bộ và nơi lưu ảnh đều là SYSTEM. Không có actor dịch vụ ảnh ngoài nguồn.

**Phạm vi:** 3 nhóm UC chính, 8 UC con, 9 mapping; 7 hành trình chức năng. Không tạo scenario riêng cho UC008 lọc nội dung, các trạng thái hoặc tác vụ AUT. Ngoài phạm vi: đăng nhập/đăng ký, Follow/Unfollow, đăng/khôi phục bài, Chat, tính điểm/Trending, kiểm duyệt hồ sơ người khác.

**Trạng thái:** Đang soạn để review; FR-M02 đã chốt nhưng US-M02 và US-overview Chờ duyệt. GAP-001 giới hạn diễn giải bộ đếm lúc đang nhập, không tự chốt yêu cầu mới.

## 1. Baseline và dữ liệu

<!-- sc:document -->

| key | value |
|---|---|
| module | M02 |
| scope | ALL |
| skill_version | 1.4 |
| output_dir | docs/specs/scenarios/M02 |
| date | 2026-11-11 |
| completed_steps | 1, 2, 3, 4 |
| status | Đang soạn |
| approval_evidence | - |


| Nguồn | Version | Ngày | Trạng thái | SHA-256 |
|---|---|---|---|---|
| [docs/specs/fr/FR-M02.md](../../fr/FR-M02.md) | 1.6 | 2026-10-24 | Đã chốt | e86aca71e0415ee2e121a4fdc3628261be335e9d266fcf6e9654b2fdf3cd357e |
| [docs/specs/us/US-M02.md](../../us/US-M02.md) | Không có version tài liệu; skill 2.2 | 2026-10-30 | Chờ duyệt | b9ab9639f363fe1c6753c06eded95ecaabe7315248f6f20fe17dc8baaf0a6dd2 |
| [docs/specs/us/US-overview.md](../../us/US-overview.md) | 1.1 | 2026-11-02 | Chờ duyệt | c1d624b7036ea2c7a9968eaa46c482c04fa1a15e2554d536cdfc12f177e26e33 |
| [docs/specs/fr/FR-M01.md](../../fr/FR-M01.md) | 1.10 | 2026-10-24 | Đã chốt | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a |
| [docs/specs/fr/FR-M03.md](../../fr/FR-M03.md) | 1.10 | 2026-10-24 | Đã chốt | fc996ec5520b6485277fca6a3dbae018bfce02263aba8e15ea87871f35865980 |
| [docs/specs/fr/FR-M11.md](../../fr/FR-M11.md) | 1.3 | 2026-10-24 | Đã chốt | 1908d300f75d5f7fa0fd5b31b1d375bc6a63ccd42da254de6e9d0d7d9ef16307 |
| [docs/specs/fr/FR-M12.md](../../fr/FR-M12.md) | 1.1 | 2026-10-24 | Đã chốt | 7aa660866cf625220db602509c93775b713fb26e568cc1d9df2d9aaa399f2430 |
| [docs/specs/fr/FR-M16.md](../../fr/FR-M16.md) | 1.0 | 2026-10-24 | Đã chốt | c8ef96e52479806637b0eac334bbe57fa9fe4f73bdacc73913467960050f0671 |


FR-M02 chính thức và bản làm việc chung có cùng byte/SHA-256. US-overview chỉ là tập chọn UC chính; phạm vi module lấy toàn catalog M02. Phương pháp: [scenarios](../../../../.agent-instructions/skills/scenarios/SKILL.md).

<!-- sc:actors -->

| id | name | kind | source |
|---|---|---|---|
| ACT-001 | Guest — người chưa có phiên | human | FR-M02-01.16, FR-M02-02.05, FR-M02-05.02 |
| ACT-002 | User — người có phiên | human | FR-M02-01.05, FR-M02-02.03, FR-M02-03.02, FR-M02-07.01 |
| ACT-003 | Mod / Admin | human | FR-M02-03.10, FR-M02-04.07, BR-M02-36 |


Mỗi sự kiện chỉ một chủ thể ACT-001/002/003 hoặc SYSTEM. ACT-003 kế thừa User theo US, không vượt điều kiện sở hữu/ACTIVE. Khi bảo trì, chỉ ADMIN thật sự được M01 cho phép; không suy mọi Mod đều được phép. Phiên hợp lệ là đầu vào của hành trình qua phiên, không thêm đăng nhập ở đầu mỗi SC.

| Bộ dữ liệu giả lập | Giá trị và trạng thái |
|---|---|
| D-PROFILE | U-LAN ACTIVE; username=lan_12, display_name=Lan, avatar=lan-old.png, bio="Thích Toán 📐", Lớp=11, tham gia=01/09/2026, điểm=150, badge đã đạt=B100; chưa đạt B300; đạt Ngôi sao tuần ở tuần vừa chốt; followers=2, following=2 |
| D-POSTS | P101 công khai tạo 08/11 08:00; P102 nhóm Private G12 tạo 08/11 09:00; P103 nháp 07/11 10:00; P104 chờ duyệt 07/11 09:00; P105 bị từ chối 07/11 08:00; P106 tự ẩn 06/11 12:00; P107 đăng ẩn danh 06/11 11:00; P108 bị Mod ẩn; P109 đã xóa còn hạn khôi phục |
| D-OWN | Thứ tự tab Bài viết: P102, P101, P103, P104, P105, P106, P107 (dấu ẩn danh); không đưa P108/P109 vào tab này. Lan còn là thành viên G12; P109 thuộc tab Đã xóa. |
| D-PUBLIC | Người ngoài G12 chỉ thấy P101; thành viên G12 thấy P102 rồi P101. Không thấy P103–P109; không dùng dòng thay thế Bookmark trong tab Bài viết. |
| D-NETWORK | Minh theo dõi Lan lúc 08/11 09:00; Tú theo dõi Lan lúc 07/11 10:00; Hà (BANNED) và Bình (DEACTIVATED) có quan hệ nhưng bị lọc. Lan theo dõi Minh lúc 08/11 08:00, Tú lúc 06/11 08:00, Hà/Bình bị lọc; Topic Toán và bài P101 không phải quan hệ người dùng. |
| D-BOOK | Lan lưu P201 lúc 08/11 10:00, P202 lúc 07/11 09:00, P203 lúc 06/11 08:00. P201/P203 xem được, P202 tạm bị ẩn. Thứ tự theo lưu: P201, dòng Nội dung không tồn tại (P202), P203; lý do ẩn chỉ là dữ liệu kiểm tra, không trả trong dòng hiển thị. |


Các mã U-/P-/G- là giả lập. Mỗi SC/nhánh là snapshot độc lập; không áp dữ liệu mâu thuẫn cùng lần chạy. Thời điểm dùng Asia/Saigon (+07). A×156 là chuỗi A đúng 156 ký tự. Tên ảnh/kích thước là ví dụ, không có upload thực tế. Các nhánh hợp lệ thay một chiều dữ liệu, không nhân tích mọi tổ hợp; nếu nhiều giá trị sai thì không khẳng định thứ tự báo lỗi chưa có nguồn.

## 2. Kiểm kê nhóm UC

<!-- sc:decomposition -->

| core | sub | source |
|---|---|---|
| UC-M02-010 | UC-M02-001 | FR-M02-01, BR-M02-01, BR-M02-02, BR-M02-03, BR-M02-15, BR-M02-16, BR-M02-26, BR-M02-34, BR-M02-37 |
| UC-M02-010 | UC-M02-002 | FR-M02-02, BR-M02-14, BR-M02-27, BR-M02-31 |
| UC-M02-010 | UC-M02-008 | FR-M02-01.07, FR-M02-01.17, FR-M02-01.19, FR-M02-07.03, FR-M02-07.04, FR-M02-07.07, BR-M02-28, BR-M02-29, BR-M02-31 |
| UC-M02-020 | UC-M02-003 | FR-M02-03, BR-M02-04, BR-M02-09, BR-M02-18, BR-M02-33, BR-M02-36, FR-M01-03.15, FR-M01-03.16 |
| UC-M02-020 | UC-M02-004 | FR-M02-04, BR-M02-06, BR-M02-07, BR-M02-08, BR-M02-18, BR-M02-36 |
| UC-M02-030 | UC-M02-005 | FR-M02-05, BR-M02-21, BR-M02-22, BR-M02-24, BR-M02-25 |
| UC-M02-030 | UC-M02-006 | FR-M02-06, FR-M02-05.02, FR-M02-07.05, BR-M02-24, BR-M02-25, BR-M02-29 |
| UC-M02-030 | UC-M02-007 | FR-M02-07, BR-M02-23, BR-M02-29, BR-M02-30, BR-M02-31 |
| UC-M02-030 | UC-M02-008 | FR-M02-01.07, FR-M02-01.17, FR-M02-01.19, FR-M02-07.03, FR-M02-07.04, FR-M02-07.07, BR-M02-28, BR-M02-29, BR-M02-31 |


<!-- sc:ucs -->

| id | treatment | scenarios | coverage | rationale | sources |
|---|---|---|---|---|---|
| UC-M02-010 | aggregate | SC-M02-001, SC-M02-002, SC-M02-007 | SC-M02-001/M2, SC-M02-002/M2, SC-M02-007/M2 | Nhóm mục tiêu độc lập, không chạy tất cả UC con nối tiếp. | FR-M02-01, FR-M02-02, BR-M02-01, BR-M02-14, BR-M02-28 |
| UC-M02-020 | aggregate | SC-M02-003, SC-M02-004 | SC-M02-003/M2, SC-M02-004/M2 | Nhóm mục tiêu độc lập, không chạy tất cả UC con nối tiếp. | FR-M02-03, FR-M02-04, BR-M02-18, BR-M02-36 |
| UC-M02-030 | aggregate | SC-M02-001, SC-M02-005, SC-M02-006, SC-M02-007 | SC-M02-001/M2, SC-M02-005/M2, SC-M02-006/M2, SC-M02-007/M2 | Nhóm mục tiêu độc lập, không chạy tất cả UC con nối tiếp. | FR-M02-05, FR-M02-06, FR-M02-07, BR-M02-21, BR-M02-23, BR-M02-30 |
| UC-M02-001 | scenario | SC-M02-001 | SC-M02-001/M2 | Actor chủ động thực hiện chức năng đến kết quả; có thể tham gia phần mở rộng hành trình khác. | FR-M02-01, BR-M02-01, BR-M02-02, BR-M02-03, BR-M02-15, BR-M02-16, BR-M02-26, BR-M02-34, BR-M02-37 |
| UC-M02-002 | scenario | SC-M02-001, SC-M02-002 | SC-M02-001/M2, SC-M02-002/M2 | Actor chủ động thực hiện chức năng đến kết quả; có thể tham gia phần mở rộng hành trình khác. | FR-M02-02, BR-M02-14, BR-M02-27, BR-M02-31 |
| UC-M02-003 | scenario | SC-M02-003 | SC-M02-003/M2 | Actor chủ động thực hiện chức năng đến kết quả; có thể tham gia phần mở rộng hành trình khác. | FR-M02-03, BR-M02-04, BR-M02-09, BR-M02-18, BR-M02-33, BR-M02-36, FR-M01-03.15, FR-M01-03.16 |
| UC-M02-004 | scenario | SC-M02-004 | SC-M02-004/M2 | Actor chủ động thực hiện chức năng đến kết quả; có thể tham gia phần mở rộng hành trình khác. | FR-M02-04, BR-M02-06, BR-M02-07, BR-M02-08, BR-M02-18, BR-M02-36 |
| UC-M02-005 | scenario | SC-M02-005 | SC-M02-005/M2 | Actor chủ động thực hiện chức năng đến kết quả; có thể tham gia phần mở rộng hành trình khác. | FR-M02-05, BR-M02-21, BR-M02-22, BR-M02-24, BR-M02-25 |
| UC-M02-006 | scenario | SC-M02-006, SC-M02-007 | SC-M02-006/M2, SC-M02-007/M2 | Actor chủ động thực hiện chức năng đến kết quả; có thể tham gia phần mở rộng hành trình khác. | FR-M02-06, FR-M02-05.02, FR-M02-07.05, BR-M02-24, BR-M02-25, BR-M02-29 |
| UC-M02-007 | scenario | SC-M02-007 | SC-M02-007/M2 | Actor chủ động thực hiện chức năng đến kết quả; có thể tham gia phần mở rộng hành trình khác. | FR-M02-07, BR-M02-23, BR-M02-29, BR-M02-30, BR-M02-31 |
| UC-M02-008 | embedded | SC-M02-001, SC-M02-007 | SC-M02-001/M2, SC-M02-007/M2 | Lọc nội dung thực hiện trong lượt trả hồ sơ/Bookmark, không tạo BF SYSTEM riêng. | FR-M02-01.07, FR-M02-01.17, FR-M02-01.19, FR-M02-07.03, FR-M02-07.04, FR-M02-07.07, BR-M02-28, BR-M02-29, BR-M02-31 |


| Sơ đồ nguồn | Số UC thành viên | Đối chiếu |
|---|---|---|
| D-M02-CORE | 3 | Khớp ID thành viên; giữ quan hệ và mapping nguồn |
| D-M02-010 | 4 | Khớp ID thành viên; giữ quan hệ và mapping nguồn |
| D-M02-020 | 3 | Khớp ID thành viên; giữ quan hệ và mapping nguồn |
| D-M02-030 | 5 | Khớp ID thành viên; giữ quan hệ và mapping nguồn |


## 3. Danh mục luồng nghiệp vụ

<!-- sc:flows -->

| id | uc | primary | trigger | goal | completion | covered_ucs | rationale | scenario | sources |
|---|---|---|---|---|---|---|---|---|---|
| BF-M02-001 | UC-M02-001 | ACT-002 | Lan yêu cầu trang /u/LAN_12 của mình. | Xem trang hồ sơ và nội dung theo ngữ cảnh người xem | Hồ sơ được trả theo người xem, trạng thái và quyền nội dung; không đổi dữ liệu hồ sơ hoặc trạng thái bài. | UC-M02-001, UC-M02-002, UC-M02-008 | Có yêu cầu chức năng độc lập của actor và kết quả trả đủ; khác trạng thái/ngữ cảnh chỉ là nhánh. | SC-M02-001 | FR-M02-01.20, BR-M02-01, BR-M02-34, FR-M02-01.01, FR-M02-01.02, FR-M02-01.03, FR-M02-01.05, FR-M02-01.07, FR-M02-01.09, FR-M02-01.10, FR-M02-01.13, FR-M02-01.14, FR-M02-01.15, FR-M02-01.17, FR-M02-01.19, FR-M02-01.23, FR-M02-01.24, FR-M02-01.25, FR-M02-01.27, BR-M02-02, BR-M02-03, BR-M02-08, BR-M02-11, BR-M02-12, BR-M02-13, BR-M02-17, BR-M02-19, BR-M02-20, BR-M02-28, BR-M02-31, BR-M02-37, FR-M02-01.21, FR-M02-01.22, FR-M02-01.11, FR-M02-02.04, BR-M02-15, FR-M02-01.06, FR-M02-01.26, FR-M02-01.12, BR-M02-16, FR-M01-05.06, FR-M02-01.04, FR-M02-01.18, BR-M02-05, BR-M02-32, FR-M02-01.08, FR-M03-15.03, FR-M02-02.01, FR-M02-02.02, FR-M02-02.03, FR-M02-02.06, FR-M02-02.07, FR-M02-02.08, FR-M02-02.09, BR-M02-14, BR-M02-27, FR-M02-01.16, BR-M02-26 |
| BF-M02-002 | UC-M02-002 | ACT-002 | Minh chọn số Người theo dõi trên hồ sơ Lan. | Xem danh sách người theo dõi hoặc đang theo dõi | Người xem nhận đúng hướng danh sách đã chọn và số đếm sau lọc; không thay đổi quan hệ theo dõi. | UC-M02-002 | Có yêu cầu chức năng độc lập của actor và kết quả trả đủ; khác trạng thái/ngữ cảnh chỉ là nhánh. | SC-M02-002 | FR-M02-02.01, FR-M02-02.02, FR-M02-02.03, FR-M02-02.06, FR-M02-02.07, FR-M02-02.08, FR-M02-02.09, BR-M02-14, BR-M02-27, BR-M02-31, FR-M02-02.04, BR-M02-15, FR-M02-02.05 |
| BF-M02-003 | UC-M02-003 | ACT-002 | Lan chọn Sửa hồ sơ của mình. | Sửa và lưu thông tin hồ sơ của mình | Các giá trị hợp lệ được lưu theo nhánh, kết quả trả cho chủ hồ sơ; giữ avatar. Không tự tăng Lớp qua năm hoặc gửi nhắc cập nhật; Lớp bài viết độc lập. | UC-M02-003 | Có yêu cầu chức năng độc lập của actor và kết quả trả đủ; khác trạng thái/ngữ cảnh chỉ là nhánh. | SC-M02-003 | FR-M02-03.01, FR-M02-03.09, FR-M02-03.10, BR-M02-18, BR-M02-36, FR-M02-03.03, FR-M02-03.11, FR-M02-03.13, BR-M02-04, BR-M02-33, FR-M02-03.02, FR-M01-03.15, FR-M01-03.16, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.08, FR-M02-03.12, FR-M02-03.14, FR-M02-03.15, BR-M02-09, BR-M02-10, BR-M02-35, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-36, BR-M02-05 |
| BF-M02-004 | UC-M02-004 | ACT-002 | Lan tải ảnh mới làm avatar của mình. | Đổi avatar của mình | Ảnh mới hợp lệ là avatar hiện hành, lưu bản gốc; ảnh tải lên cũ được xóa sau thành công; không sửa các thông tin hồ sơ khác. | UC-M02-004 | Có yêu cầu chức năng độc lập của actor và kết quả trả đủ; khác trạng thái/ngữ cảnh chỉ là nhánh. | SC-M02-004 | FR-M02-04.01, FR-M02-04.02, FR-M02-04.05, FR-M02-04.06, FR-M02-04.07, FR-M02-01.03, BR-M02-06, BR-M02-07, BR-M02-08, BR-M02-18, BR-M02-36, FR-M02-04.03, FR-M02-04.04 |
| BF-M02-005 | UC-M02-005 | ACT-002 | Lan chọn Lưu bài P201. | Lưu bài viết để đọc lại | Có đúng một bookmark U-LAN/P201 theo thời điểm lưu ban đầu; không bật thông báo bài hoặc thay quyền đọc nội dung. | UC-M02-005 | Có yêu cầu chức năng độc lập của actor và kết quả trả đủ; khác trạng thái/ngữ cảnh chỉ là nhánh. | SC-M02-005 | FR-M02-05.01, FR-M02-05.03, FR-M02-05.05, BR-M02-21, BR-M02-22, BR-M02-23, BR-M02-24, FR-M02-05.04, BR-M02-25, FR-M02-05.02 |
| BF-M02-006 | UC-M02-006 | ACT-002 | Lan chọn Bỏ lưu bài P201 đang lưu. | Bỏ lưu bài khỏi danh sách cá nhân | Bookmark đích bị xóa khỏi danh sách của chính actor; nội dung bài và dữ liệu người khác không bị xóa. | UC-M02-006 | Có yêu cầu chức năng độc lập của actor và kết quả trả đủ; khác trạng thái/ngữ cảnh chỉ là nhánh. | SC-M02-006 | FR-M02-06.01, BR-M02-24, FR-M02-07.05, BR-M02-29, FR-M02-06.02, BR-M02-25, FR-M02-05.02 |
| BF-M02-007 | UC-M02-007 | ACT-002 | Lan mở tab Bookmark trên hồ sơ của mình. | Xem danh sách Bookmark riêng tư của mình | Danh sách riêng tư được trả đúng thứ tự; giữ bookmark/thời điểm khi mất quyền tạm thời, không lộ nội dung/lý do của bài bị thay thế. | UC-M02-006, UC-M02-007, UC-M02-008 | Có yêu cầu chức năng độc lập của actor và kết quả trả đủ; khác trạng thái/ngữ cảnh chỉ là nhánh. | SC-M02-007 | FR-M02-07.01, FR-M02-07.03, FR-M02-07.04, FR-M02-07.07, BR-M02-23, BR-M02-29, BR-M02-31, FR-M02-07.02, FR-M02-07.06, BR-M02-30, FR-M02-07.05, FR-M02-06.01 |


UC002 extend UC001 tại EP-PROFILE-FOLLOW và UC006 extend UC007 tại EP-BOOKMARK-REMOVE theo đúng US. Điểm gọi được khai triển ngay trong nhánh của SC001/007; hai chức năng cũng có SC độc lập vì actor có thể yêu cầu riêng. UC001/007 include UC008, được gộp trong lượt SYSTEM lọc và trả dữ liệu, không dừng ở câu gọi UC.

## 4. Scenario sáu phần

<a id="sc-m02-001"></a>

<!-- sc:scenario SC-M02-001 -->

### SC-M02-001

#### 1. Tên kịch bản chuẩn

Xem trang hồ sơ và nội dung theo ngữ cảnh người xem — BF-M02-001; UC owner: [UC-M02-001](../../us/US-M02.md#uc-m02-001). Trigger: Lan yêu cầu trang /u/LAN_12 của mình.

#### 2. Actor thực hiện

ACT-002 — người có phiên là actor chính; ACT-003 kế thừa tương tác User theo US-M02, không được vượt sở hữu/ACTIVE hoặc sửa hồ sơ người khác. ACT-001 — Guest có đường thay thế V1 trong mục 6.

#### 3. Tiền điều kiện

Có địa chỉ hồ sơ cần tra cứu. Không mặc định username tồn tại hoặc tài khoản đích ACTIVE. Đường chuẩn: Lan có phiên hợp lệ xem hồ sơ chính mình; là thành viên G12. Các snapshot thay thế ghi trong mục 6.

#### 4. Hậu điều kiện

<!-- sc:post SC-M02-001 -->

| result | condition |
|---|---|
| SUCCESS | Hồ sơ được trả theo người xem, trạng thái và quyền nội dung; không đổi dữ liệu hồ sơ hoặc trạng thái bài. |
| REJECTED | Không cung cấp nội dung hồ sơ/danh sách của tài khoản không tồn tại hoặc không được phép; câu trả đúng theo nhánh. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M02-001 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan yêu cầu trang /u/LAN_12 của mình. | U-LAN ACTIVE; username=lan_12, display_name=Lan, avatar=lan-old.png, bio="Thích Toán 📐", Lớp=11, tham gia=01/09/2026, điểm=150, badge đã đạt=B100; chưa đạt B300; đạt Ngôi sao tuần ở tuần vừa chốt; followers=2, following=2; so username bỏ phân biệt hoa/thường | M2 | FR-M02-01.20, BR-M02-01, BR-M02-34 |
| M2 | SYSTEM | Hệ thống phân giải về U-LAN; xác định chính chủ, trả các trường hồ sơ, nút sửa và ba tab Bài viết/Bookmark/Đã xóa; mở Bài viết mặc định. Lọc nội dung theo UC-M02-008 rồi trả danh sách mới nhất trước, không hiện nút Nhắn tin cho chính mình. | Avatar tròn; display_name Lan, username lan_12, bio Thích Toán 📐, Lớp 11, ngày tham gia 01/09/2026, tổng điểm 150, badge B100, danh hiệu tuần vừa chốt cạnh badge, followers=2/following=2. Không hiện tiến độ B300, mức cảnh báo, lịch sử username, liên kết mạng xã hội, stars nhận/cho, số lần/lịch sử danh hiệu tuần.; Thứ tự tab Bài viết: P102, P101, P103, P104, P105, P106, P107 (dấu ẩn danh); không đưa P108/P109 vào tab này. Lan còn là thành viên G12; P109 thuộc tab Đã xóa. | END:SUCCESS | FR-M02-01.01, FR-M02-01.02, FR-M02-01.03, FR-M02-01.05, FR-M02-01.07, FR-M02-01.09, FR-M02-01.10, FR-M02-01.13, FR-M02-01.14, FR-M02-01.15, FR-M02-01.17, FR-M02-01.19, FR-M02-01.23, FR-M02-01.24, FR-M02-01.25, FR-M02-01.27, BR-M02-01, BR-M02-02, BR-M02-03, BR-M02-08, BR-M02-11, BR-M02-12, BR-M02-13, BR-M02-17, BR-M02-19, BR-M02-20, BR-M02-28, BR-M02-31, BR-M02-37 |


#### 6. Các ngoại lệ

Mỗi E thay bước tại cột at; guard thay dữ liệu/ngữ cảnh của đúng lần thực thi, không chạy sau bước đã thành công. Nhánh quay lại dùng dữ liệu đã sửa; vẫn sai thì áp lại nhánh tương ứng, không tự đặt số lần thử.

<!-- sc:exceptions SC-M02-001 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Username không tồn tại, kể cả username cũ đã đổi và chưa có người nhận lại | E1.1 | FR-M02-01.21, FR-M02-01.22, BR-M02-34 |
| E2 | system | M2 | Tài khoản đích là DEACTIVATED hoặc DELETED | E2.1 | FR-M02-01.11, FR-M02-02.04, BR-M02-15 |
| E3 | system | M2 | Username cũ đã được tài khoản khác nhận lại | E3.1 | FR-M02-01.20, FR-M02-01.22, FR-M02-01.06, FR-M02-01.26, BR-M02-34 |
| E4 | system | M2 | Người có phiên đang xem hồ sơ người khác | E4.1 | FR-M02-01.01, FR-M02-01.02, FR-M02-01.06, FR-M02-01.07, FR-M02-01.26, BR-M02-01, BR-M02-03, BR-M02-28 |
| E5 | system | M2 | Tài khoản đích BANNED, người yêu cầu khác chủ có phiên hợp lệ | E5.1 | FR-M02-01.01, FR-M02-01.06, FR-M02-01.07, FR-M02-01.12, BR-M02-16, FR-M01-05.06 |
| E6 | system | M2 | Bio rỗng, chưa đặt avatar/Lớp và không đạt danh hiệu tuần vừa chốt | E6.1 | FR-M02-01.02, FR-M02-01.03, FR-M02-01.04, FR-M02-01.10, FR-M02-01.18, FR-M02-01.24, FR-M02-01.25, BR-M02-05, BR-M02-08, BR-M02-13, BR-M02-32, BR-M02-37 |
| E7 | system | M2 | Người xem có phiên là thành viên G12 | E7.1 | FR-M02-01.06, FR-M02-01.07, FR-M02-01.19, FR-M02-01.26, BR-M02-28, BR-M02-31 |
| E8 | user-choice | M2 | Chính chủ chọn tab Đã xóa sau khi hồ sơ đã được trả | E8.1 | FR-M02-01.01, FR-M02-01.02, FR-M02-01.03, FR-M02-01.05, FR-M02-01.07, FR-M02-01.09, FR-M02-01.10, FR-M02-01.13, FR-M02-01.14, FR-M02-01.15, FR-M02-01.17, FR-M02-01.19, FR-M02-01.23, FR-M02-01.24, FR-M02-01.25, FR-M02-01.27, BR-M02-01, BR-M02-02, BR-M02-03, BR-M02-08, BR-M02-11, BR-M02-12, BR-M02-13, BR-M02-17, BR-M02-19, BR-M02-20, BR-M02-28, BR-M02-31, BR-M02-37, FR-M02-01.08, FR-M03-15.03 |
| E9 | user-choice | M2 | Tại EP-PROFILE-FOLLOW, người có phiên chọn số followers sau khi xem hồ sơ | E9.1 | FR-M02-01.01, FR-M02-01.02, FR-M02-01.03, FR-M02-01.05, FR-M02-01.07, FR-M02-01.09, FR-M02-01.10, FR-M02-01.13, FR-M02-01.14, FR-M02-01.15, FR-M02-01.17, FR-M02-01.19, FR-M02-01.23, FR-M02-01.24, FR-M02-01.25, FR-M02-01.27, BR-M02-01, BR-M02-02, BR-M02-03, BR-M02-08, BR-M02-11, BR-M02-12, BR-M02-13, BR-M02-17, BR-M02-19, BR-M02-20, BR-M02-28, BR-M02-31, BR-M02-37, FR-M02-02.01, FR-M02-02.02, FR-M02-02.03, FR-M02-02.06, FR-M02-02.07, FR-M02-02.08, FR-M02-02.09, BR-M02-14, BR-M02-27 |
| E10 | system | M2 | Tập bài đủ điều kiện của người xem là rỗng | E10.1 | FR-M02-01.02, FR-M02-01.05, FR-M02-01.06, FR-M02-01.07, FR-M02-01.17, FR-M02-01.19, BR-M02-28, BR-M02-31 |
| E11 | system | M1 | ACT-001 — Người khởi tạo là ACT-001 Guest: thay toàn bộ M1→M2, không giả lập đăng nhập. Kết quả chuẩn của đường này: END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4. | E11.1 | FR-M02-01.01, FR-M02-01.06, FR-M02-01.07, FR-M02-01.11, FR-M02-01.12, FR-M02-01.16, FR-M02-01.20, FR-M02-01.21, FR-M02-01.27, BR-M02-26, BR-M02-28, BR-M02-34 |
| E12 | system | M1 | ACT-001 — Guest tra cứu hồ sơ BANNED; thay toàn bộ M1→M2. Kết quả chuẩn của đường này: END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4. | E12.1 | FR-M02-01.01, FR-M02-01.06, FR-M02-01.07, FR-M02-01.12, FR-M02-01.16, FR-M02-01.27, BR-M02-16, BR-M02-26, BR-M02-28 |
| E13 | system | M1 | ACT-001 — Guest tra cứu username không tồn tại hoặc tên cũ chưa có chủ hiện hành. Kết quả chuẩn của đường này: END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4. | E13.1 | FR-M02-01.21, FR-M02-01.22, BR-M02-34 |
| E14 | system | M1 | ACT-001 — Guest tra cứu hồ sơ DEACTIVATED hoặc DELETED. Kết quả chuẩn của đường này: END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4. | E14.1 | FR-M02-01.11, FR-M02-02.04, BR-M02-15 |


<!-- sc:branch SC-M02-001 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống trả "người dùng không tồn tại"; không chuyển hướng theo tên cũ. | /u/lan_old không có chủ hiện hành; Lan đã đổi sang lan_12 | END:REJECTED | FR-M02-01.21, FR-M02-01.22, BR-M02-34 |


<!-- sc:branch SC-M02-001 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống thay toàn bộ nội dung hồ sơ bằng "người dùng không tồn tại"; không cung cấp danh sách theo dõi. | U-LAN DEACTIVATED hoặc DELETED; không lộ bio/nội dung/danh tính | END:REJECTED | FR-M02-01.11, FR-M02-02.04, BR-M02-15 |


<!-- sc:branch SC-M02-001 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống mở hồ sơ chủ hiện hành của username đó, không chuyển sang người sở hữu cũ; áp ngữ cảnh người xem và lọc bài của chủ mới. | /u/lan_old nay thuộc U-TU ACTIVE; trả hồ sơ Tú, chỉ Bài viết và Nhắn tin vì Lan có phiên; không trả hồ sơ Lan | END:SUCCESS | FR-M02-01.20, FR-M02-01.22, FR-M02-01.06, FR-M02-01.26, BR-M02-34 |


<!-- sc:branch SC-M02-001 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống trả hồ sơ công khai, chỉ tab Bài viết, không nút sửa; có nút Nhắn tin dẫn tới M16. Lọc bài theo quyền hiện tại. | Avatar tròn; display_name Lan, username lan_12, bio Thích Toán 📐, Lớp 11, ngày tham gia 01/09/2026, tổng điểm 150, badge B100, danh hiệu tuần vừa chốt cạnh badge, followers=2/following=2. Không hiện tiến độ B300, mức cảnh báo, lịch sử username, liên kết mạng xã hội, stars nhận/cho, số lần/lịch sử danh hiệu tuần.; Người ngoài G12 chỉ thấy P101; thành viên G12 thấy P102 rồi P101. Không thấy P103–P109; không dùng dòng thay thế Bookmark trong tab Bài viết.; người xem Minh không trong G12; nút Nhắn tin hiện | END:SUCCESS | FR-M02-01.01, FR-M02-01.02, FR-M02-01.06, FR-M02-01.07, FR-M02-01.26, BR-M02-01, BR-M02-03, BR-M02-28 |


<!-- sc:branch SC-M02-001 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống trả hồ sơ công khai với nhãn "Tài khoản đã bị khóa"; chỉ Bài viết theo quyền của người xem, không cấp quyền dùng phiên bình thường cho chủ tài khoản BANNED. | Avatar tròn; display_name Lan, username lan_12, bio Thích Toán 📐, Lớp 11, ngày tham gia 01/09/2026, tổng điểm 150, badge B100, danh hiệu tuần vừa chốt cạnh badge, followers=2/following=2. Không hiện tiến độ B300, mức cảnh báo, lịch sử username, liên kết mạng xã hội, stars nhận/cho, số lần/lịch sử danh hiệu tuần.; Người ngoài G12 chỉ thấy P101; thành viên G12 thấy P102 rồi P101. Không thấy P103–P109; không dùng dòng thay thế Bookmark trong tab Bài viết.; U-LAN BANNED, Minh ACTIVE xem | END:SUCCESS | FR-M02-01.01, FR-M02-01.06, FR-M02-01.07, FR-M02-01.12, BR-M02-16, FR-M01-05.06 |


<!-- sc:branch SC-M02-001 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống trả hồ sơ theo quyền, dùng avatar mặc định dạng tròn, không hiển thị gì ở vị trí bio/Lớp; giữ badge đã đạt vĩnh viễn nhưng không hiện danh hiệu của các tuần cũ. | U-LAN ACTIVE; username=lan_12, display_name=Lan, avatar=lan-old.png, bio="Thích Toán 📐", Lớp=11, tham gia=01/09/2026, điểm=150, badge đã đạt=B100; chưa đạt B300; đạt Ngôi sao tuần ở tuần vừa chốt; followers=2, following=2 thay bio="", avatar chưa đặt, Lớp trống; B100 vẫn có; chỉ đạt danh hiệu tuần cũ | END:SUCCESS | FR-M02-01.02, FR-M02-01.03, FR-M02-01.04, FR-M02-01.10, FR-M02-01.18, FR-M02-01.24, FR-M02-01.25, BR-M02-05, BR-M02-08, BR-M02-13, BR-M02-32, BR-M02-37 |


<!-- sc:branch SC-M02-001 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống trả hồ sơ công khai người khác, chỉ tab Bài viết, nút Nhắn tin; đưa cả bài Private G12 được phép vào đúng thứ tự tạo. | Avatar tròn; display_name Lan, username lan_12, bio Thích Toán 📐, Lớp 11, ngày tham gia 01/09/2026, tổng điểm 150, badge B100, danh hiệu tuần vừa chốt cạnh badge, followers=2/following=2. Không hiện tiến độ B300, mức cảnh báo, lịch sử username, liên kết mạng xã hội, stars nhận/cho, số lần/lịch sử danh hiệu tuần.; P102 rồi P101, các bài còn lại loại; không lộ bài ẩn danh của người khác | END:SUCCESS | FR-M02-01.06, FR-M02-01.07, FR-M02-01.19, FR-M02-01.26, BR-M02-28, BR-M02-31 |


<!-- sc:branch SC-M02-001 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống trả hồ sơ chính chủ, ba tab và danh sách Bài viết theo quyền. | Avatar tròn; display_name Lan, username lan_12, bio Thích Toán 📐, Lớp 11, ngày tham gia 01/09/2026, tổng điểm 150, badge B100, danh hiệu tuần vừa chốt cạnh badge, followers=2/following=2. Không hiện tiến độ B300, mức cảnh báo, lịch sử username, liên kết mạng xã hội, stars nhận/cho, số lần/lịch sử danh hiệu tuần.; Thứ tự tab Bài viết: P102, P101, P103, P104, P105, P106, P107 (dấu ẩn danh); không đưa P108/P109 vào tab này. Lan còn là thành viên G12; P109 thuộc tab Đã xóa. | E8.2 | FR-M02-01.01, FR-M02-01.02, FR-M02-01.03, FR-M02-01.05, FR-M02-01.07, FR-M02-01.09, FR-M02-01.10, FR-M02-01.13, FR-M02-01.14, FR-M02-01.15, FR-M02-01.17, FR-M02-01.19, FR-M02-01.23, FR-M02-01.24, FR-M02-01.25, FR-M02-01.27, BR-M02-01, BR-M02-02, BR-M02-03, BR-M02-08, BR-M02-11, BR-M02-12, BR-M02-13, BR-M02-17, BR-M02-19, BR-M02-20, BR-M02-28, BR-M02-31, BR-M02-37 |
| E8.2 | ACT-002 | Lan chọn tab Đã xóa. | U-LAN; không yêu cầu khôi phục bài | E8.3 | FR-M02-01.08 |
| E8.3 | SYSTEM | Hệ thống hiển thị bài đã xóa còn được giữ của Lan tại tab Đã xóa theo M03; không thực hiện khôi phục. | P109 thuộc Lan, đã xóa lúc 07/11 08:00, chưa bị xóa hẳn; không lẫn vào Bài viết | END:SUCCESS | FR-M02-01.08, FR-M03-15.03 |


<!-- sc:branch SC-M02-001 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống trả hồ sơ đúng ngữ cảnh và hai số mạng lưới. | Avatar tròn; display_name Lan, username lan_12, bio Thích Toán 📐, Lớp 11, ngày tham gia 01/09/2026, tổng điểm 150, badge B100, danh hiệu tuần vừa chốt cạnh badge, followers=2/following=2. Không hiện tiến độ B300, mức cảnh báo, lịch sử username, liên kết mạng xã hội, stars nhận/cho, số lần/lịch sử danh hiệu tuần. | E9.2 | FR-M02-01.01, FR-M02-01.02, FR-M02-01.03, FR-M02-01.05, FR-M02-01.07, FR-M02-01.09, FR-M02-01.10, FR-M02-01.13, FR-M02-01.14, FR-M02-01.15, FR-M02-01.17, FR-M02-01.19, FR-M02-01.23, FR-M02-01.24, FR-M02-01.25, FR-M02-01.27, BR-M02-01, BR-M02-02, BR-M02-03, BR-M02-08, BR-M02-11, BR-M02-12, BR-M02-13, BR-M02-17, BR-M02-19, BR-M02-20, BR-M02-28, BR-M02-31, BR-M02-37 |
| E9.2 | ACT-002 | Lan chọn số Người theo dõi. | Minh theo dõi Lan lúc 08/11 09:00; Tú theo dõi Lan lúc 07/11 10:00; Hà (BANNED) và Bình (DEACTIVATED) có quan hệ nhưng bị lọc. Lan theo dõi Minh lúc 08/11 08:00, Tú lúc 06/11 08:00, Hà/Bình bị lọc; Topic Toán và bài P101 không phải quan hệ người dùng. | E9.3 | FR-M02-02.01 |
| E9.3 | SYSTEM | Hệ thống kiểm phiên và tài khoản đích, lọc trạng thái, trả danh sách followers mới nhất trước trong ngữ cảnh hồ sơ. | Theo hướng followers: Minh, Tú; tổng 2. Theo hướng following: Minh, Tú; tổng 2. Mỗi hướng xếp theo đúng thời điểm bắt đầu quan hệ của hướng đó; không có tùy chọn ẩn danh sách.; Minh theo dõi Lan lúc 08/11 09:00; Tú theo dõi Lan lúc 07/11 10:00; Hà (BANNED) và Bình (DEACTIVATED) có quan hệ nhưng bị lọc. Lan theo dõi Minh lúc 08/11 08:00, Tú lúc 06/11 08:00, Hà/Bình bị lọc; Topic Toán và bài P101 không phải quan hệ người dùng. | END:SUCCESS | FR-M02-02.01, FR-M02-02.02, FR-M02-02.03, FR-M02-02.06, FR-M02-02.07, FR-M02-02.08, FR-M02-02.09, BR-M02-14, BR-M02-27, BR-M02-31 |


<!-- sc:branch SC-M02-001 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống vẫn trả các thông tin hồ sơ và tab Bài viết theo đúng ngữ cảnh, danh sách bài rỗng; không chèn các bài không đủ quyền hoặc placeholder Bookmark vào tab này. | Avatar tròn; display_name Lan, username lan_12, bio Thích Toán 📐, Lớp 11, ngày tham gia 01/09/2026, tổng điểm 150, badge B100, danh hiệu tuần vừa chốt cạnh badge, followers=2/following=2. Không hiện tiến độ B300, mức cảnh báo, lịch sử username, liên kết mạng xã hội, stars nhận/cho, số lần/lịch sử danh hiệu tuần.; snapshot không có bài đủ điều kiện: Bài viết=[] | END:SUCCESS | FR-M02-01.02, FR-M02-01.05, FR-M02-01.06, FR-M02-01.07, FR-M02-01.17, FR-M02-01.19, BR-M02-28, BR-M02-31 |


**E11 — thay toàn bộ đường đi theo actor:** Người khởi tạo là ACT-001 Guest: thay toàn bộ M1→M2, không giả lập đăng nhập. Kết quả chuẩn của đường này: END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:branch SC-M02-001 E11 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E11.1 | ACT-001 | Guest mở /u/LAN_12 để tra cứu hồ sơ Lan. | Avatar tròn; display_name Lan, username lan_12, bio Thích Toán 📐, Lớp 11, ngày tham gia 01/09/2026, tổng điểm 150, badge B100, danh hiệu tuần vừa chốt cạnh badge, followers=2/following=2. Không hiện tiến độ B300, mức cảnh báo, lịch sử username, liên kết mạng xã hội, stars nhận/cho, số lần/lịch sử danh hiệu tuần.; Người ngoài G12 chỉ thấy P101; thành viên G12 thấy P102 rồi P101. Không thấy P103–P109; không dùng dòng thay thế Bookmark trong tab Bài viết.; Guest chỉ thấy P101; trạng thái chuẩn ACTIVE | E11.2 | FR-M02-01.01, FR-M02-01.06, FR-M02-01.07, FR-M02-01.11, FR-M02-01.12, FR-M02-01.16, FR-M02-01.20, FR-M02-01.21, FR-M02-01.27, BR-M02-26, BR-M02-28, BR-M02-34 |
| E11.2 | SYSTEM | Hệ thống mở hồ sơ người khác chỉ đọc: trả thông tin công khai, chỉ Bài viết; không sửa/Bookmark/Đã xóa/Nhắn tin. Lọc Private như người ngoài nhóm; không lộ bài ẩn danh. | Avatar tròn; display_name Lan, username lan_12, bio Thích Toán 📐, Lớp 11, ngày tham gia 01/09/2026, tổng điểm 150, badge B100, danh hiệu tuần vừa chốt cạnh badge, followers=2/following=2. Không hiện tiến độ B300, mức cảnh báo, lịch sử username, liên kết mạng xã hội, stars nhận/cho, số lần/lịch sử danh hiệu tuần.; Người ngoài G12 chỉ thấy P101; thành viên G12 thấy P102 rồi P101. Không thấy P103–P109; không dùng dòng thay thế Bookmark trong tab Bài viết.; Guest chỉ thấy P101; trạng thái chuẩn ACTIVE | END:SUCCESS | FR-M02-01.01, FR-M02-01.06, FR-M02-01.07, FR-M02-01.11, FR-M02-01.12, FR-M02-01.16, FR-M02-01.20, FR-M02-01.21, FR-M02-01.27, BR-M02-26, BR-M02-28, BR-M02-34 |


**E12 — thay toàn bộ đường đi theo actor:** Guest tra cứu hồ sơ BANNED; thay toàn bộ M1→M2. Kết quả chuẩn của đường này: END:SUCCESS, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:branch SC-M02-001 E12 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E12.1 | ACT-001 | Guest mở /u/lan_12 của tài khoản BANNED. | Avatar tròn; display_name Lan, username lan_12, bio Thích Toán 📐, Lớp 11, ngày tham gia 01/09/2026, tổng điểm 150, badge B100, danh hiệu tuần vừa chốt cạnh badge, followers=2/following=2. Không hiện tiến độ B300, mức cảnh báo, lịch sử username, liên kết mạng xã hội, stars nhận/cho, số lần/lịch sử danh hiệu tuần.; U-LAN BANNED; Guest ngoài G12 | E12.2 | FR-M02-01.01, FR-M02-01.06, FR-M02-01.07, FR-M02-01.12, FR-M02-01.16, FR-M02-01.27, BR-M02-16, BR-M02-26, BR-M02-28 |
| E12.2 | SYSTEM | Hệ thống trả hồ sơ chỉ đọc với nhãn Tài khoản đã bị khóa; chỉ tab Bài viết và P101 đủ quyền, không nút sửa hoặc Nhắn tin. | Avatar tròn; display_name Lan, username lan_12, bio Thích Toán 📐, Lớp 11, ngày tham gia 01/09/2026, tổng điểm 150, badge B100, danh hiệu tuần vừa chốt cạnh badge, followers=2/following=2. Không hiện tiến độ B300, mức cảnh báo, lịch sử username, liên kết mạng xã hội, stars nhận/cho, số lần/lịch sử danh hiệu tuần.; U-LAN BANNED; Guest ngoài G12 | END:SUCCESS | FR-M02-01.01, FR-M02-01.06, FR-M02-01.07, FR-M02-01.12, FR-M02-01.16, FR-M02-01.27, BR-M02-16, BR-M02-26, BR-M02-28 |


**E13 — thay toàn bộ đường đi theo actor:** Guest tra cứu username không tồn tại hoặc tên cũ chưa có chủ hiện hành. Kết quả chuẩn của đường này: END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:branch SC-M02-001 E13 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E13.1 | ACT-001 | Guest mở /u/lan_old. | /u/lan_old không có tài khoản hiện hành | E13.2 | FR-M02-01.21, FR-M02-01.22, BR-M02-34 |
| E13.2 | SYSTEM | Hệ thống trả người dùng không tồn tại, không chuyển hướng sang username mới. | /u/lan_old không có tài khoản hiện hành | END:REJECTED | FR-M02-01.21, FR-M02-01.22, BR-M02-34 |


**E14 — thay toàn bộ đường đi theo actor:** Guest tra cứu hồ sơ DEACTIVATED hoặc DELETED. Kết quả chuẩn của đường này: END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:branch SC-M02-001 E14 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E14.1 | ACT-001 | Guest mở /u/lan_12. | U-LAN DEACTIVATED hoặc DELETED | E14.2 | FR-M02-01.11, FR-M02-02.04, BR-M02-15 |
| E14.2 | SYSTEM | Hệ thống trả người dùng không tồn tại thay toàn bộ hồ sơ; không cung cấp danh sách riêng tư. | U-LAN DEACTIVATED hoặc DELETED | END:REJECTED | FR-M02-01.11, FR-M02-02.04, BR-M02-15 |


<!-- sc:end SC-M02-001 -->

<a id="sc-m02-002"></a>

<!-- sc:scenario SC-M02-002 -->

### SC-M02-002

#### 1. Tên kịch bản chuẩn

Xem danh sách người theo dõi hoặc đang theo dõi — BF-M02-002; UC owner: [UC-M02-002](../../us/US-M02.md#uc-m02-002). Trigger: Minh chọn số Người theo dõi trên hồ sơ Lan.

#### 2. Actor thực hiện

ACT-002 — người có phiên là actor chính; ACT-003 kế thừa tương tác User theo US-M02, không được vượt sở hữu/ACTIVE hoặc sửa hồ sơ người khác. ACT-001 — Guest có đường thay thế V1 trong mục 6.

#### 3. Tiền điều kiện

Có ngữ cảnh hồ sơ U-LAN. Phiên và trạng thái đích được kiểm trong phản hồi; không mặc định mọi yêu cầu được mở danh sách.

#### 4. Hậu điều kiện

<!-- sc:post SC-M02-002 -->

| result | condition |
|---|---|
| SUCCESS | Người xem nhận đúng hướng danh sách đã chọn và số đếm sau lọc; không thay đổi quan hệ theo dõi. |
| REJECTED | Không mở danh sách; nếu Guest thì yêu cầu đăng nhập, nếu đích không tồn tại theo trạng thái thì không trả mạng lưới. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M02-002 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Minh chọn số Người theo dõi trên hồ sơ Lan. | Minh theo dõi Lan lúc 08/11 09:00; Tú theo dõi Lan lúc 07/11 10:00; Hà (BANNED) và Bình (DEACTIVATED) có quan hệ nhưng bị lọc. Lan theo dõi Minh lúc 08/11 08:00, Tú lúc 06/11 08:00, Hà/Bình bị lọc; Topic Toán và bài P101 không phải quan hệ người dùng. | M2 | FR-M02-02.01 |
| M2 | SYSTEM | Hệ thống kiểm phiên và tài khoản đích; đọc các quan hệ giữa người dùng, loại/không đếm DEACTIVATED/BANNED; trả followers theo thời điểm bắt đầu, mới nhất trước trong ngữ cảnh hồ sơ. | Theo hướng followers: Minh, Tú; tổng 2. Theo hướng following: Minh, Tú; tổng 2. Mỗi hướng xếp theo đúng thời điểm bắt đầu quan hệ của hướng đó; không có tùy chọn ẩn danh sách.; Minh theo dõi Lan lúc 08/11 09:00; Tú theo dõi Lan lúc 07/11 10:00; Hà (BANNED) và Bình (DEACTIVATED) có quan hệ nhưng bị lọc. Lan theo dõi Minh lúc 08/11 08:00, Tú lúc 06/11 08:00, Hà/Bình bị lọc; Topic Toán và bài P101 không phải quan hệ người dùng. | END:SUCCESS | FR-M02-02.01, FR-M02-02.02, FR-M02-02.03, FR-M02-02.06, FR-M02-02.07, FR-M02-02.08, FR-M02-02.09, BR-M02-14, BR-M02-27, BR-M02-31 |


#### 6. Các ngoại lệ

Mỗi E thay bước tại cột at; guard thay dữ liệu/ngữ cảnh của đúng lần thực thi, không chạy sau bước đã thành công. Nhánh quay lại dùng dữ liệu đã sửa; vẫn sai thì áp lại nhánh tương ứng, không tự đặt số lần thử.

<!-- sc:exceptions SC-M02-002 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Người xem chọn Đang theo dõi thay vì Người theo dõi | E1.1 | FR-M02-02.02, FR-M02-02.01, FR-M02-02.03, FR-M02-02.06, FR-M02-02.07, FR-M02-02.08, FR-M02-02.09, BR-M02-14, BR-M02-27, BR-M02-31 |
| E2 | system | M2 | Tài khoản đích DEACTIVATED hoặc DELETED | E2.1 | FR-M02-02.04, BR-M02-15 |
| E3 | system | M2 | Hà/Bình đã trở lại ACTIVE và các quan hệ vẫn còn | E3.1 | FR-M02-02.07, FR-M02-02.08, FR-M02-02.09, BR-M02-27, BR-M02-31 |
| E4 | system | M2 | Không có quan hệ đủ điều kiện sau lọc | E4.1 | FR-M02-02.01, FR-M02-02.07, FR-M02-02.09, BR-M02-27, BR-M02-31 |
| E5 | system | M1 | ACT-001 — ACT-001 Guest chọn một trong hai số; thay toàn bộ M1→M2. Kết quả chuẩn của đường này: END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4. | E5.1 | FR-M02-02.05, BR-M02-14 |


<!-- sc:branch SC-M02-002 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Minh chọn số Đang theo dõi trên hồ sơ Lan. | Minh theo dõi Lan lúc 08/11 09:00; Tú theo dõi Lan lúc 07/11 10:00; Hà (BANNED) và Bình (DEACTIVATED) có quan hệ nhưng bị lọc. Lan theo dõi Minh lúc 08/11 08:00, Tú lúc 06/11 08:00, Hà/Bình bị lọc; Topic Toán và bài P101 không phải quan hệ người dùng. | E1.2 | FR-M02-02.02 |
| E1.2 | SYSTEM | Hệ thống trả following là những người Lan theo dõi, chỉ người dùng, không Topic/bài; áp lọc và thứ tự theo thời điểm bắt đầu theo dõi của từng quan hệ. | Theo hướng followers: Minh, Tú; tổng 2. Theo hướng following: Minh, Tú; tổng 2. Mỗi hướng xếp theo đúng thời điểm bắt đầu quan hệ của hướng đó; không có tùy chọn ẩn danh sách.; Minh theo dõi Lan lúc 08/11 09:00; Tú theo dõi Lan lúc 07/11 10:00; Hà (BANNED) và Bình (DEACTIVATED) có quan hệ nhưng bị lọc. Lan theo dõi Minh lúc 08/11 08:00, Tú lúc 06/11 08:00, Hà/Bình bị lọc; Topic Toán và bài P101 không phải quan hệ người dùng. | END:SUCCESS | FR-M02-02.01, FR-M02-02.02, FR-M02-02.03, FR-M02-02.06, FR-M02-02.07, FR-M02-02.08, FR-M02-02.09, BR-M02-14, BR-M02-27, BR-M02-31 |


<!-- sc:branch SC-M02-002 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống không hiển thị danh sách theo dõi của tài khoản đó. | U-LAN DEACTIVATED/DELETED; không lộ danh sách | END:REJECTED | FR-M02-02.04, BR-M02-15 |


<!-- sc:branch SC-M02-002 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống hiển thị và đếm lại Hà/Bình; không tạo mới quan hệ và vẫn xếp theo thời điểm bắt đầu ban đầu. | Hà: 08/11 08:30, Bình: 06/11 10:00; followers Minh,Hà,Tú,Bình; tổng=4 | END:SUCCESS | FR-M02-02.07, FR-M02-02.08, FR-M02-02.09, BR-M02-27, BR-M02-31 |


<!-- sc:branch SC-M02-002 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống trả danh sách người theo dõi đã chọn là rỗng, số đếm bằng 0; không tự tạo quan hệ hoặc nêu một lỗi không có trong nguồn. | followers=[]; count=0; snapshot không có quan hệ ACTIVE | END:SUCCESS | FR-M02-02.01, FR-M02-02.07, FR-M02-02.09, BR-M02-27, BR-M02-31 |


**E5 — thay toàn bộ đường đi theo actor:** ACT-001 Guest chọn một trong hai số; thay toàn bộ M1→M2. Kết quả chuẩn của đường này: END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:branch SC-M02-002 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-001 | Guest chọn Người theo dõi hoặc Đang theo dõi của Lan. | U-LAN ACTIVE; Guest chưa có phiên; hai số 2/2 | E5.2 | FR-M02-02.05, BR-M02-14 |
| E5.2 | SYSTEM | Hệ thống yêu cầu đăng nhập, chưa mở danh sách; Guest vẫn được xem hai con số trên hồ sơ. Không tự đăng nhập hoặc thêm UC login vào hành trình. | U-LAN ACTIVE; Guest chưa có phiên; hai số 2/2 | END:REJECTED | FR-M02-02.05, BR-M02-14 |


<!-- sc:end SC-M02-002 -->

<a id="sc-m02-003"></a>

<!-- sc:scenario SC-M02-003 -->

### SC-M02-003

#### 1. Tên kịch bản chuẩn

Sửa và lưu thông tin hồ sơ của mình — BF-M02-003; UC owner: [UC-M02-003](../../us/US-M02.md#uc-m02-003). Trigger: Lan chọn Sửa hồ sơ của mình.

#### 2. Actor thực hiện

ACT-002 — người có phiên là actor chính; ACT-003 kế thừa tương tác User theo US-M02, không được vượt sở hữu/ACTIVE hoặc sửa hồ sơ người khác. Không có actor dịch vụ ngoài.

#### 3. Tiền điều kiện

Có phiên người thao tác; cổng truy cập M01 đã cho phép đến chức năng. Kiểm quyền sở hữu và ACTIVE trong M2/M6. Snapshot chuẩn U-LAN đang ACTIVE; avatar thay đổi qua SC-M02-004 độc lập, không bắt đổi ảnh để lưu hồ sơ.

#### 4. Hậu điều kiện

<!-- sc:post SC-M02-003 -->

| result | condition |
|---|---|
| SUCCESS | Các giá trị hợp lệ được lưu theo nhánh, kết quả trả cho chủ hồ sơ; giữ avatar. Không tự tăng Lớp qua năm hoặc gửi nhắc cập nhật; Lớp bài viết độc lập. |
| REJECTED | Không sửa hồ sơ khi khác chủ/không ACTIVE; không cam kết rollback cho lỗi lưu trữ chưa có nguồn. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M02-003 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan chọn Sửa hồ sơ của mình. | U-LAN ACTIVE; username=lan_12, display_name=Lan, avatar=lan-old.png, bio="Thích Toán 📐", Lớp=11, tham gia=01/09/2026, điểm=150, badge đã đạt=B100; chưa đạt B300; đạt Ngôi sao tuần ở tuần vừa chốt; followers=2, following=2 | M2 | FR-M02-03.01 |
| M2 | SYSTEM | Hệ thống kiểm chính chủ và ACTIVE, trả trang sửa gồm bio, Lớp/Khối, avatar, username, display_name hiện có. | U-LAN ACTIVE; username=lan_12, display_name=Lan, avatar=lan-old.png, bio="Thích Toán 📐", Lớp=11, tham gia=01/09/2026, điểm=150, badge đã đạt=B100; chưa đạt B300; đạt Ngôi sao tuần ở tuần vừa chốt; followers=2, following=2; các giá trị trước sửa được điền theo dữ liệu hiện có | M3 | FR-M02-03.01, FR-M02-03.09, FR-M02-03.10, BR-M02-18, BR-M02-36 |
| M3 | ACT-002 | Lan nhập bio mới, có khoảng trắng đầu/cuối và một emoji. | bio nhập="  Thích Toán 📐  " | M4 | FR-M02-03.03 |
| M4 | SYSTEM | Hệ thống hiển thị số ký tự bio đã dùng; số dùng để nghiệm thu khi lưu được đếm sau trim, emoji/xuống dòng mỗi loại một ký tự. | bio chuẩn hóa="Thích Toán 📐", độ dài lưu=12; cách bộ đếm lúc đang gõ xử lý khoảng trắng chưa chốt, xem GAP-001 | M5 | FR-M02-03.03, FR-M02-03.11, FR-M02-03.13, BR-M02-04, BR-M02-33 |
| M5 | ACT-002 | Lan chọn Lớp 12, đổi username/display_name rồi gửi lưu. | bio="  Thích Toán 📐  "; Lớp=12; username mới=Lan_Nguyen; display_name="  Nguyễn Lan  " | M6 | FR-M02-03.02, FR-M01-03.15, FR-M01-03.16 |
| M6 | SYSTEM | Hệ thống kiểm lại chính chủ/ACTIVE, trim và kiểm bio ≤155, Lớp hợp lệ, username 3–20 ký tự cho phép và duy nhất không phân biệt hoa/thường kể cả tên DELETED; trim display_name, kiểm 1–50 ký tự và tập ký tự hợp lệ, cho trùng display_name. Lưu các giá trị hợp lệ và trả kết quả đã cập nhật; giữ nguyên avatar. Giải phóng username cũ ngay, không tạo alias URL, không giới hạn số lần đổi. | U-LAN: bio=Thích Toán 📐 (12), Lớp 11→12, username lan_12→Lan_Nguyen giữ hoa/thường, display_name=Nguyễn Lan; /u/Lan_Nguyen là URL hiện hành; lan_12 được giải phóng | END:SUCCESS | FR-M02-03.02, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.08, FR-M02-03.09, FR-M02-03.10, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-03.14, FR-M02-03.15, BR-M02-04, BR-M02-09, BR-M02-10, BR-M02-18, BR-M02-33, BR-M02-35, BR-M02-36, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, FR-M01-03.15, FR-M01-03.16, BR-M01-36 |


#### 6. Các ngoại lệ

Mỗi E thay bước tại cột at; guard thay dữ liệu/ngữ cảnh của đúng lần thực thi, không chạy sau bước đã thành công. Nhánh quay lại dùng dữ liệu đã sửa; vẫn sai thì áp lại nhánh tương ứng, không tự đặt số lần thử.

<!-- sc:exceptions SC-M02-003 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Người yêu cầu khác chủ hồ sơ, kể cả Mod/Admin | E1.1 | FR-M02-03.10, BR-M02-36 |
| E2 | system | M2 | Tài khoản chủ hồ sơ không ACTIVE tại lần kiểm tra này | E2.1 | FR-M02-03.09, BR-M02-18 |
| E3 | system | M6 | Người yêu cầu khác chủ hồ sơ, kể cả Mod/Admin | E3.1 | FR-M02-03.10, BR-M02-36 |
| E4 | system | M6 | Tài khoản chủ hồ sơ không ACTIVE tại lần kiểm tra này | E4.1 | FR-M02-03.09, BR-M02-18 |
| E5 | system | M6 | Bio sau trim >155 ký tự | E5.1 | FR-M02-03.04, BR-M02-04 |
| E6 | system | M6 | Lớp/Khối không thuộc 10/11/12 và không trống | E6.1 | FR-M02-03.06, BR-M02-09 |
| E7 | system | M6 | Username sai độ dài hoặc ký tự | E7.1 | FR-M01-03.05, FR-M01-03.15 |
| E8 | system | M6 | Username trùng tên tài khoản khác kể cả DELETED | E8.1 | FR-M01-03.06, FR-M01-03.15 |
| E9 | system | M6 | Display_name sau trim rỗng hoặc >50 ký tự | E9.1 | FR-M01-03.12, FR-M01-03.13, FR-M01-03.16 |
| E10 | system | M6 | Display_name có ký tự không cho phép | E10.1 | FR-M01-03.14, FR-M01-03.16 |
| E11 | user-choice | M5 | Actor chọn bỏ trống bio và bỏ chọn Lớp đã đặt | E11.1 | FR-M02-03.05, FR-M02-03.07, FR-M02-03.12, FR-M02-03.14, BR-M02-09, BR-M02-33, FR-M02-03.08, FR-M02-03.09, FR-M02-03.10, FR-M02-03.11, FR-M02-03.15, BR-M02-05, BR-M02-10, BR-M02-35 |
| E12 | system | M6 | Bio có xuống dòng, display_name trùng tên người khác nhưng hợp lệ | E12.1 | FR-M02-03.02, FR-M02-03.11, FR-M02-03.13, BR-M02-33, FR-M01-03.07, FR-M01-03.16 |


<!-- sc:branch SC-M02-003 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối sửa hồ sơ người khác; không có quyền gỡ bio bằng vai trò kiểm duyệt. | Minh thao tác U-LAN hoặc Mod thao tác Lan; không cập nhật | END:REJECTED | FR-M02-03.10, BR-M02-36 |


<!-- sc:branch SC-M02-003 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối sửa thông tin hồ sơ. | U-LAN BANNED/DEACTIVATED/DELETED; không sửa | END:REJECTED | FR-M02-03.09, BR-M02-18 |


<!-- sc:branch SC-M02-003 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối sửa hồ sơ người khác; không có quyền gỡ bio bằng vai trò kiểm duyệt. | Minh thao tác U-LAN hoặc Mod thao tác Lan; không cập nhật | END:REJECTED | FR-M02-03.10, BR-M02-36 |


<!-- sc:branch SC-M02-003 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối sửa thông tin hồ sơ. | U-LAN BANNED/DEACTIVATED/DELETED; không sửa | END:REJECTED | FR-M02-03.09, BR-M02-18 |


<!-- sc:branch SC-M02-003 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối giá trị vi phạm, cho sửa rồi gửi lại theo UC003/A3 hoặc A4; chưa ghi nhận giá trị lỗi là hợp lệ. | bio="A"×156 | E5.2 | FR-M02-03.04, BR-M02-04 |
| E5.2 | ACT-002 | Lan sửa trường bị lỗi về giá trị hợp lệ rồi gửi lại; các trường còn lại dùng dữ liệu hợp lệ của lần gửi. | bio="A"×155 | M6 | FR-M02-03.04, BR-M02-04 |


<!-- sc:branch SC-M02-003 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối giá trị vi phạm, cho sửa rồi gửi lại theo UC003/A3 hoặc A4; chưa ghi nhận giá trị lỗi là hợp lệ. | Lớp=9 | E6.2 | FR-M02-03.06, BR-M02-09 |
| E6.2 | ACT-002 | Lan sửa trường bị lỗi về giá trị hợp lệ rồi gửi lại; các trường còn lại dùng dữ liệu hợp lệ của lần gửi. | Lớp=12 | M6 | FR-M02-03.06, BR-M02-09 |


<!-- sc:branch SC-M02-003 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối giá trị vi phạm, cho sửa rồi gửi lại theo UC003/A3 hoặc A4; chưa ghi nhận giá trị lỗi là hợp lệ. | username="ab", "A"×21 hoặc lan.nguyen | E7.2 | FR-M01-03.05, FR-M01-03.15 |
| E7.2 | ACT-002 | Lan sửa trường bị lỗi về giá trị hợp lệ rồi gửi lại; các trường còn lại dùng dữ liệu hợp lệ của lần gửi. | username=Lan_Nguyen | M6 | FR-M01-03.05, FR-M01-03.15 |


<!-- sc:branch SC-M02-003 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống từ chối giá trị vi phạm, cho sửa rồi gửi lại theo UC003/A3 hoặc A4; chưa ghi nhận giá trị lỗi là hợp lệ. | Lan_Nguyen trùng lan_nguyen (tài khoản khác hoặc DELETED) | E8.2 | FR-M01-03.06, FR-M01-03.15 |
| E8.2 | ACT-002 | Lan sửa trường bị lỗi về giá trị hợp lệ rồi gửi lại; các trường còn lại dùng dữ liệu hợp lệ của lần gửi. | username=Lan_Nguyen2 khả dụng | M6 | FR-M01-03.06, FR-M01-03.15 |


<!-- sc:branch SC-M02-003 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống từ chối giá trị vi phạm, cho sửa rồi gửi lại theo UC003/A3 hoặc A4; chưa ghi nhận giá trị lỗi là hợp lệ. | display_name="   " hoặc "A"×51 | E9.2 | FR-M01-03.12, FR-M01-03.13, FR-M01-03.16 |
| E9.2 | ACT-002 | Lan sửa trường bị lỗi về giá trị hợp lệ rồi gửi lại; các trường còn lại dùng dữ liệu hợp lệ của lần gửi. | display_name="  Nguyễn Lan  " | M6 | FR-M01-03.12, FR-M01-03.13, FR-M01-03.16 |


<!-- sc:branch SC-M02-003 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống từ chối giá trị vi phạm, cho sửa rồi gửi lại theo UC003/A3 hoặc A4; chưa ghi nhận giá trị lỗi là hợp lệ. | display_name="Lan 😊" | E10.2 | FR-M01-03.14, FR-M01-03.16 |
| E10.2 | ACT-002 | Lan sửa trường bị lỗi về giá trị hợp lệ rồi gửi lại; các trường còn lại dùng dữ liệu hợp lệ của lần gửi. | display_name="Nguyễn Lan" | M6 | FR-M01-03.14, FR-M01-03.16 |


<!-- sc:branch SC-M02-003 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-002 | Lan để bio toàn khoảng trắng, bỏ chọn Lớp đã đặt, giữ tên hợp lệ rồi gửi lưu. | bio="    "; Lớp=trống; username/display_name hiện có hợp lệ | E11.2 | FR-M02-03.05, FR-M02-03.07, FR-M02-03.12, FR-M02-03.14, BR-M02-09, BR-M02-33 |
| E11.2 | SYSTEM | Hệ thống kiểm lại chính chủ/ACTIVE, trim bio toàn khoảng trắng thành trống, nhận việc bỏ chọn Lớp; kiểm tên hợp lệ và lưu hồ sơ không có bio/Lớp. Không tự điền lại theo năm học hoặc theo Lớp trên bài. | bio="    "→""; Lớp=trống; username/display_name hợp lệ giữ nguyên; bio không hiển thị | END:SUCCESS | FR-M02-03.05, FR-M02-03.07, FR-M02-03.08, FR-M02-03.09, FR-M02-03.10, FR-M02-03.11, FR-M02-03.12, FR-M02-03.14, FR-M02-03.15, BR-M02-05, BR-M02-09, BR-M02-10, BR-M02-33, BR-M02-35 |


<!-- sc:branch SC-M02-003 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | SYSTEM | Hệ thống đếm mỗi emoji/xuống dòng một ký tự sau trim, chấp nhận display_name trùng, lưu thay đổi hợp lệ. | bio="A<br>📐" dài 3; display_name=Nguyễn Lan đã có ở người khác; username vẫn duy nhất | END:SUCCESS | FR-M02-03.02, FR-M02-03.11, FR-M02-03.13, BR-M02-33, FR-M01-03.07, FR-M01-03.16 |


<!-- sc:end SC-M02-003 -->

<a id="sc-m02-004"></a>

<!-- sc:scenario SC-M02-004 -->

### SC-M02-004

#### 1. Tên kịch bản chuẩn

Đổi avatar của mình — BF-M02-004; UC owner: [UC-M02-004](../../us/US-M02.md#uc-m02-004). Trigger: Lan tải ảnh mới làm avatar của mình.

#### 2. Actor thực hiện

ACT-002 — người có phiên là actor chính; ACT-003 kế thừa tương tác User theo US-M02, không được vượt sở hữu/ACTIVE hoặc sửa hồ sơ người khác. Không có actor dịch vụ ngoài.

#### 3. Tiền điều kiện

Có phiên người thao tác được cổng M01 cho phép. U-LAN có ảnh cũ lan-old.png; quyền sở hữu/ACTIVE và ảnh được kiểm ở M2. Không phải sửa bio/Lớp cùng lần.

#### 4. Hậu điều kiện

<!-- sc:post SC-M02-004 -->

| result | condition |
|---|---|
| SUCCESS | Ảnh mới hợp lệ là avatar hiện hành, lưu bản gốc; ảnh tải lên cũ được xóa sau thành công; không sửa các thông tin hồ sơ khác. |
| REJECTED | Ảnh bị từ chối không được đặt làm avatar; yêu cầu sai quyền không đổi avatar. Chưa quy định retry/rollback lỗi lưu trữ. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M02-004 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan tải ảnh mới làm avatar của mình. | lan-new.png; PNG 2 MB; bản gốc 1200×900; chủ U-LAN | M2 | FR-M02-04.01 |
| M2 | SYSTEM | Hệ thống kiểm chính chủ/ACTIVE, loại ảnh và dung lượng; lưu nguyên ảnh gốc, đặt ảnh mới làm avatar rồi xóa ảnh tải lên cũ sau khi đặt thành công. Trả avatar mới hiển thị cắt tròn, không bắt actor cắt ảnh gốc. | avatar=lan-new.png; bản gốc 1200×900 được giữ; lan-old.png bị xóa; bio/Lớp/tên giữ nguyên | END:SUCCESS | FR-M02-04.01, FR-M02-04.02, FR-M02-04.05, FR-M02-04.06, FR-M02-04.07, FR-M02-01.03, BR-M02-06, BR-M02-07, BR-M02-08, BR-M02-18, BR-M02-36 |


#### 6. Các ngoại lệ

Mỗi E thay bước tại cột at; guard thay dữ liệu/ngữ cảnh của đúng lần thực thi, không chạy sau bước đã thành công. Nhánh quay lại dùng dữ liệu đã sửa; vẫn sai thì áp lại nhánh tương ứng, không tự đặt số lần thử.

<!-- sc:exceptions SC-M02-004 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Sai loại, kể cả GIF động | E1.1 | FR-M02-04.03 |
| E2 | system | M2 | Dung lượng >5 MB | E2.1 | FR-M02-04.04 |
| E3 | system | M2 | Tài khoản không ACTIVE | E3.1 | FR-M02-04.06 |
| E4 | system | M2 | Người thao tác khác chủ, kể cả Mod/Admin | E4.1 | FR-M02-04.07, BR-M02-36 |
| E5 | system | M2 | Chưa có avatar tải lên trước đó, hoặc chọn JPEG/WebP hợp lệ | E5.1 | FR-M02-04.01, FR-M02-04.02, FR-M02-04.05, BR-M02-06, BR-M02-07, BR-M02-08 |


<!-- sc:branch SC-M02-004 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối ảnh/yêu cầu theo điều kiện vi phạm; không đặt ảnh đó làm avatar. | lan.gif 1 MB hoặc lan.svg | END:REJECTED | FR-M02-04.03 |


<!-- sc:branch SC-M02-004 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối ảnh/yêu cầu theo điều kiện vi phạm; không đặt ảnh đó làm avatar. | lan.png 6 MB | END:REJECTED | FR-M02-04.04 |


<!-- sc:branch SC-M02-004 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối ảnh/yêu cầu theo điều kiện vi phạm; không đặt ảnh đó làm avatar. | U-LAN không ACTIVE | END:REJECTED | FR-M02-04.06 |


<!-- sc:branch SC-M02-004 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối ảnh/yêu cầu theo điều kiện vi phạm; không đặt ảnh đó làm avatar. | Mod thao tác avatar của U-LAN | END:REJECTED | FR-M02-04.07, BR-M02-36 |


<!-- sc:branch SC-M02-004 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống nhận ảnh JPEG/PNG/WebP không quá 5 MB, lưu bản gốc và đặt avatar; không xóa ảnh mặc định dùng chung như ảnh cá nhân. Với ảnh tải lên cũ thì xóa sau thành công. | lan.webp 5 MB theo đơn vị nguồn; chưa có ảnh tải lên cũ; avatar mặc định được thay hiển thị, tài nguyên mặc định giữ nguyên | END:SUCCESS | FR-M02-04.01, FR-M02-04.02, FR-M02-04.05, BR-M02-06, BR-M02-07, BR-M02-08 |


<!-- sc:end SC-M02-004 -->

<a id="sc-m02-005"></a>

<!-- sc:scenario SC-M02-005 -->

### SC-M02-005

#### 1. Tên kịch bản chuẩn

Lưu bài viết để đọc lại — BF-M02-005; UC owner: [UC-M02-005](../../us/US-M02.md#uc-m02-005). Trigger: Lan chọn Lưu bài P201.

#### 2. Actor thực hiện

ACT-002 — người có phiên là actor chính; ACT-003 kế thừa tương tác User theo US-M02, không được vượt sở hữu/ACTIVE hoặc sửa hồ sơ người khác. ACT-001 — Guest có đường thay thế V1 trong mục 6.

#### 3. Tiền điều kiện

Bài P201 trong ngữ cảnh truy cập hợp lệ của người thao tác theo M03/M11. Không mặc định đã đăng nhập hoặc chưa có bookmark: hệ thống kiểm lúc xử lý.

#### 4. Hậu điều kiện

<!-- sc:post SC-M02-005 -->

| result | condition |
|---|---|
| SUCCESS | Có đúng một bookmark U-LAN/P201 theo thời điểm lưu ban đầu; không bật thông báo bài hoặc thay quyền đọc nội dung. |
| REJECTED | Không lưu vì chưa có phiên; hệ thống yêu cầu đăng nhập và kết thúc lần yêu cầu này. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M02-005 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan chọn Lưu bài P201. | U-LAN; P201 chưa lưu; lúc 08/11/2026 10:00 +07 | M2 | FR-M02-05.01 |
| M2 | SYSTEM | Hệ thống kiểm phiên và bài chưa lưu, thêm đúng một bookmark cá nhân với thời điểm lưu, trả kết quả bài đã được lưu. Không đăng ký theo dõi hoặc gửi thông báo chỉ vì lưu bài. | Bookmark(U-LAN,P201,08/11 10:00); chỉ chủ xem danh sách; không thêm quan hệ Follow | END:SUCCESS | FR-M02-05.01, FR-M02-05.03, FR-M02-05.05, BR-M02-21, BR-M02-22, BR-M02-23, BR-M02-24 |


#### 6. Các ngoại lệ

Mỗi E thay bước tại cột at; guard thay dữ liệu/ngữ cảnh của đúng lần thực thi, không chạy sau bước đã thành công. Nhánh quay lại dùng dữ liệu đã sửa; vẫn sai thì áp lại nhánh tương ứng, không tự đặt số lần thử.

<!-- sc:exceptions SC-M02-005 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | P201 đã được Lan lưu trước lần yêu cầu này | E1.1 | FR-M02-05.03, BR-M02-22 |
| E2 | system | M2 | Bài đang Khóa toàn bộ nhưng người dùng có phiên và chưa lưu | E2.1 | FR-M02-05.01, FR-M02-05.04, FR-M02-05.05, BR-M02-21, BR-M02-25 |
| E3 | system | M1 | ACT-001 — ACT-001 Guest chọn Lưu; thay toàn bộ M1→M2. Kết quả chuẩn của đường này: END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4. | E3.1 | FR-M02-05.02, BR-M02-24 |


<!-- sc:branch SC-M02-005 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống không thêm lần nữa, giữ một bookmark đã có; không suy ra làm mới thời điểm lưu. | Bookmark(U-LAN,P201,07/11 09:00) vẫn chỉ một bản; không tự đổi lên 08/11 | END:SUCCESS | FR-M02-05.03, BR-M02-22 |


<!-- sc:branch SC-M02-005 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống vẫn thêm bookmark và trả kết quả đã lưu; Khóa toàn bộ không chặn lưu, không phát thông báo vì bookmark. | P201 Khóa toàn bộ; Bookmark(U-LAN,P201,08/11 10:00) | END:SUCCESS | FR-M02-05.01, FR-M02-05.04, FR-M02-05.05, BR-M02-21, BR-M02-25 |


**E3 — thay toàn bộ đường đi theo actor:** ACT-001 Guest chọn Lưu; thay toàn bộ M1→M2. Kết quả chuẩn của đường này: END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:branch SC-M02-005 E3 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E3.1 | ACT-001 | Guest chọn Lưu P201. | Guest; P201; chưa có bookmark được tạo từ yêu cầu | E3.2 | FR-M02-05.02, BR-M02-24 |
| E3.2 | SYSTEM | Hệ thống yêu cầu đăng nhập, chưa thêm bookmark; kết thúc yêu cầu lưu hiện tại, không tự chạy đăng nhập. | Guest; P201; chưa có bookmark được tạo từ yêu cầu | END:REJECTED | FR-M02-05.02, BR-M02-24 |


<!-- sc:end SC-M02-005 -->

<a id="sc-m02-006"></a>

<!-- sc:scenario SC-M02-006 -->

### SC-M02-006

#### 1. Tên kịch bản chuẩn

Bỏ lưu bài khỏi danh sách cá nhân — BF-M02-006; UC owner: [UC-M02-006](../../us/US-M02.md#uc-m02-006). Trigger: Lan chọn Bỏ lưu bài P201 đang lưu.

#### 2. Actor thực hiện

ACT-002 — người có phiên là actor chính; ACT-003 kế thừa tương tác User theo US-M02, không được vượt sở hữu/ACTIVE hoặc sửa hồ sơ người khác. ACT-001 — Guest có đường thay thế V1 trong mục 6.

#### 3. Tiền điều kiện

Có bookmark của người yêu cầu cho P201. Nội dung không bắt buộc xem được. Phiên được kiểm lúc xử lý; thao tác với bookmark vốn không tồn tại chưa được nguồn quy định.

#### 4. Hậu điều kiện

<!-- sc:post SC-M02-006 -->

| result | condition |
|---|---|
| SUCCESS | Bookmark đích bị xóa khỏi danh sách của chính actor; nội dung bài và dữ liệu người khác không bị xóa. |
| REJECTED | Không bỏ lưu khi chưa có phiên; bookmark cũ chưa bị xóa bởi yêu cầu bị từ chối. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M02-006 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan chọn Bỏ lưu bài P201 đang lưu. | Bookmark(U-LAN,P201,08/11 10:00) tồn tại | M2 | FR-M02-06.01 |
| M2 | SYSTEM | Hệ thống kiểm phiên, xóa bookmark P201 của Lan và trả kết quả không còn lưu; không xóa bài gốc và không đổi danh sách người khác. | Bookmark U-LAN/P201 không còn; P201 còn nguyên; bookmark U-MINH/P201 nếu có giữ nguyên | END:SUCCESS | FR-M02-06.01, BR-M02-24 |


#### 6. Các ngoại lệ

Mỗi E thay bước tại cột at; guard thay dữ liệu/ngữ cảnh của đúng lần thực thi, không chạy sau bước đã thành công. Nhánh quay lại dùng dữ liệu đã sửa; vẫn sai thì áp lại nhánh tương ứng, không tự đặt số lần thử.

<!-- sc:exceptions SC-M02-006 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Lan chọn bỏ lưu dòng thay thế trong Bookmark | E1.1 | FR-M02-07.05, FR-M02-06.01, BR-M02-29 |
| E2 | system | M2 | Bài đang Khóa toàn bộ | E2.1 | FR-M02-06.01, FR-M02-06.02, BR-M02-25 |
| E3 | system | M1 | ACT-001 — ACT-001 Guest chọn Bỏ lưu; thay toàn bộ M1→M2. Kết quả chuẩn của đường này: END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4. | E3.1 | FR-M02-05.02, BR-M02-24 |


<!-- sc:branch SC-M02-006 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Lan chọn Bỏ lưu trên dòng Nội dung không tồn tại. | P202 được lưu nhưng tạm không xem được; không mở nội dung bài | E1.2 | FR-M02-07.05 |
| E1.2 | SYSTEM | Hệ thống kiểm phiên và xóa bookmark của chính Lan, bỏ dòng đó khỏi danh sách; không yêu cầu mở được bài. | P202 không còn trong Bookmark của Lan; P201/P203 giữ thứ tự | END:SUCCESS | FR-M02-06.01, FR-M02-07.05, BR-M02-29 |


<!-- sc:branch SC-M02-006 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống vẫn xóa bookmark theo yêu cầu hợp lệ, trả kết quả bỏ lưu. | P201 Khóa toàn bộ; bookmark U-LAN/P201 bị xóa | END:SUCCESS | FR-M02-06.01, FR-M02-06.02, BR-M02-25 |


**E3 — thay toàn bộ đường đi theo actor:** ACT-001 Guest chọn Bỏ lưu; thay toàn bộ M1→M2. Kết quả chuẩn của đường này: END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:branch SC-M02-006 E3 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E3.1 | ACT-001 | Guest gửi yêu cầu Bỏ lưu P201. | Không có phiên; không xóa bookmark của bất kỳ chủ nào | E3.2 | FR-M02-05.02, BR-M02-24 |
| E3.2 | SYSTEM | Hệ thống yêu cầu đăng nhập, chưa bỏ lưu; không truy cập/xóa bookmark riêng tư khi chưa xác định chủ. | Không có phiên; không xóa bookmark của bất kỳ chủ nào | END:REJECTED | FR-M02-05.02, BR-M02-24 |


<!-- sc:end SC-M02-006 -->

<a id="sc-m02-007"></a>

<!-- sc:scenario SC-M02-007 -->

### SC-M02-007

#### 1. Tên kịch bản chuẩn

Xem danh sách Bookmark riêng tư của mình — BF-M02-007; UC owner: [UC-M02-007](../../us/US-M02.md#uc-m02-007). Trigger: Lan mở tab Bookmark trên hồ sơ của mình.

#### 2. Actor thực hiện

ACT-002 — người có phiên là actor chính; ACT-003 kế thừa tương tác User theo US-M02, không được vượt sở hữu/ACTIVE hoặc sửa hồ sơ người khác. ACT-001 — Guest có đường thay thế V1 trong mục 6.

#### 3. Tiền điều kiện

Có ngữ cảnh yêu cầu danh sách của U-LAN; kiểm phiên và chủ danh sách ở M2. Dữ liệu thời điểm lưu khác thời điểm tạo bài. Không giả định mọi bài đang xem được.

#### 4. Hậu điều kiện

<!-- sc:post SC-M02-007 -->

| result | condition |
|---|---|
| SUCCESS | Danh sách riêng tư được trả đúng thứ tự; giữ bookmark/thời điểm khi mất quyền tạm thời, không lộ nội dung/lý do của bài bị thay thế. |
| REJECTED | Không cung cấp danh sách riêng tư cho người khác hoặc khi không có phiên xác định chủ. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M02-007 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan mở tab Bookmark trên hồ sơ của mình. | U-LAN có ba bookmark trong D-BOOK | M2 | FR-M02-07.01 |
| M2 | SYSTEM | Hệ thống kiểm đúng chủ đang có phiên; lấy bookmark còn tồn tại, áp UC-M02-008 theo khả năng xem từng bài. Trả danh sách mới nhất trước theo thời điểm lưu; bài tạm không xem được có dòng thay thế đúng vị trí, không kèm lý do và vẫn cho bỏ lưu. | Lan lưu P201 lúc 08/11 10:00, P202 lúc 07/11 09:00, P203 lúc 06/11 08:00. P201/P203 xem được, P202 tạm bị ẩn. Thứ tự theo lưu: P201, dòng Nội dung không tồn tại (P202), P203; lý do ẩn chỉ là dữ liệu kiểm tra, không trả trong dòng hiển thị. | END:SUCCESS | FR-M02-07.01, FR-M02-07.03, FR-M02-07.04, FR-M02-07.07, BR-M02-23, BR-M02-29, BR-M02-31 |


#### 6. Các ngoại lệ

Mỗi E thay bước tại cột at; guard thay dữ liệu/ngữ cảnh của đúng lần thực thi, không chạy sau bước đã thành công. Nhánh quay lại dùng dữ liệu đã sửa; vẫn sai thì áp lại nhánh tương ứng, không tự đặt số lần thử.

<!-- sc:exceptions SC-M02-007 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Người yêu cầu khác chủ danh sách hoặc phiên không xác định được chủ | E1.1 | FR-M02-07.02, BR-M02-23 |
| E2 | system | M2 | P202 xem được trở lại và không có lưu/bỏ lưu xen giữa | E2.1 | FR-M02-07.03, FR-M02-07.04, FR-M02-07.07, BR-M02-29, BR-M02-31 |
| E3 | system | M2 | P202 bị xóa hẳn hoặc tác giả chuyển DELETED | E3.1 | FR-M02-07.06, FR-M02-07.07, BR-M02-30, BR-M02-31 |
| E4 | user-choice | M2 | Tại EP-BOOKMARK-REMOVE, Lan chọn bỏ lưu dòng thay thế sau khi xem danh sách | E4.1 | FR-M02-07.01, FR-M02-07.03, FR-M02-07.04, FR-M02-07.07, BR-M02-23, BR-M02-29, BR-M02-31, FR-M02-07.05, FR-M02-06.01 |
| E5 | system | M2 | Chủ tài khoản không có bookmark nào còn tồn tại | E5.1 | FR-M02-07.01, FR-M02-07.06, FR-M02-07.07, BR-M02-23, BR-M02-30, BR-M02-31 |
| E6 | system | M1 | ACT-001 — Guest yêu cầu danh sách Bookmark riêng tư; thay toàn bộ M1→M2. Kết quả chuẩn của đường này: END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4. | E6.1 | FR-M02-07.02, BR-M02-23 |


<!-- sc:branch SC-M02-007 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối hiển thị danh sách Bookmark, không trả các dòng hoặc metadata riêng tư. | Minh yêu cầu Bookmark của Lan hoặc yêu cầu không có phiên hợp lệ | END:REJECTED | FR-M02-07.02, BR-M02-23 |


<!-- sc:branch SC-M02-007 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống trả lại nội dung P202 thay dòng Nội dung không tồn tại ở vị trí cũ theo thời điểm lưu, không coi là lưu mới. | P201 (08/11), P202 (07/11), P203 (06/11); không đổi timestamp của P202 | END:SUCCESS | FR-M02-07.03, FR-M02-07.04, FR-M02-07.07, BR-M02-29, BR-M02-31 |


<!-- sc:branch SC-M02-007 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống áp sự kiện AUT-M02-003 xóa bookmark P202; trả các bookmark còn lại, không giữ placeholder cho bài đã bị xóa hẳn. | P201 rồi P203; bookmark P202 không còn; khác với tạm bị ẩn | END:SUCCESS | FR-M02-07.06, FR-M02-07.07, BR-M02-30, BR-M02-31 |


<!-- sc:branch SC-M02-007 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống trả Bookmark theo đúng quyền và thứ tự, với dòng Nội dung không tồn tại có thể bỏ lưu. | Lan lưu P201 lúc 08/11 10:00, P202 lúc 07/11 09:00, P203 lúc 06/11 08:00. P201/P203 xem được, P202 tạm bị ẩn. Thứ tự theo lưu: P201, dòng Nội dung không tồn tại (P202), P203; lý do ẩn chỉ là dữ liệu kiểm tra, không trả trong dòng hiển thị. | E4.2 | FR-M02-07.01, FR-M02-07.03, FR-M02-07.04, FR-M02-07.07, BR-M02-23, BR-M02-29, BR-M02-31 |
| E4.2 | ACT-002 | Lan chọn Bỏ lưu trên dòng P202 đang thay thế. | Không mở nội dung P202 | E4.3 | FR-M02-07.05 |
| E4.3 | SYSTEM | Hệ thống kiểm phiên, triển khai bỏ lưu UC-M02-006 bằng cách xóa bookmark U-LAN/P202 và trả lại danh sách còn P201, P203 theo thứ tự lưu; không xóa bài P202. | P201 (08/11), P203 (06/11); không còn dòng thay thế P202 | END:SUCCESS | FR-M02-06.01, FR-M02-07.05, FR-M02-07.07, BR-M02-29, BR-M02-31 |


<!-- sc:branch SC-M02-007 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống kiểm chính chủ rồi trả danh sách Bookmark rỗng; không tạo dòng giả hoặc khôi phục bookmark đã xóa. | U-LAN; Bookmark=[] | END:SUCCESS | FR-M02-07.01, FR-M02-07.06, FR-M02-07.07, BR-M02-23, BR-M02-30, BR-M02-31 |


**E6 — thay toàn bộ đường đi theo actor:** Guest yêu cầu danh sách Bookmark riêng tư; thay toàn bộ M1→M2. Kết quả chuẩn của đường này: END:REJECTED, dùng hậu điều kiện tương ứng ở mục 4.

<!-- sc:branch SC-M02-007 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-001 | Guest yêu cầu Bookmark của Lan. | Không có phiên; danh sách U-LAN không bị lộ | E6.2 | FR-M02-07.02, BR-M02-23 |
| E6.2 | SYSTEM | Hệ thống từ chối cung cấp danh sách vì không có phiên xác định chủ; không trả các dòng riêng tư. | Không có phiên; danh sách U-LAN không bị lộ | END:REJECTED | FR-M02-07.02, BR-M02-23 |


<!-- sc:end SC-M02-007 -->

## 5. Quy tắc nền và giao tiếp có nguồn

| ID | Trigger/điều kiện | Hiệu ứng và phạm vi | sources |
|---|---|---|---|
| AUT-M02-001 | Sau khi avatar mới được đặt thành công | Xóa ảnh tải lên cũ; không xóa tài nguyên avatar mặc định dùng chung. Đã triển khai ở SC-M02-004/M2. Không tự đặt timer/retry/rollback. | FR-M02-04.05, BR-M02-07 |
| AUT-M02-002 | M12 cung cấp tổng điểm mới | Điểm trên hồ sơ phản ánh ngay, ví dụ 150→151 khi có thay đổi; không chờ chu kỳ bảng xếp hạng. M02 chỉ hiển thị điểm/badge do M12 cung cấp, không tự trao điểm. Danh hiệu tuần vừa chốt tách biệt điểm tức thời. | FR-M02-01.09, FR-M02-01.10, FR-M02-01.24, FR-M02-01.25, BR-M02-11, BR-M02-12, BR-M02-13, BR-M02-37, FR-M12-05.12, FR-M12-05.13 |
| AUT-M02-003 | Bài lưu bị xóa hẳn hoặc tác giả DELETED; hoặc chính người lưu DELETED | Xóa bookmark bị ảnh hưởng; trường hợp chính người lưu DELETED thì M01 xóa mọi bookmark của họ. Tạm mất quyền không xóa bookmark. Không dựng actor Scheduler. | FR-M02-07.06, BR-M02-30, FR-M01-12.08 |
| RULE-M02-001 | Phân giải URL và ngữ cảnh người xem | URL không phân biệt hoa/thường, không alias tên cũ; người nhận username cũ là chủ hiện hành của URL đó. Guest chỉ đọc; người có phiên xem người khác có Nhắn tin; chính chủ có ba tab, không Nhắn tin chính mình. Không tự cấp quyền dùng ứng dụng cho tài khoản BANNED. | FR-M02-01.05, FR-M02-01.06, FR-M02-01.16, FR-M02-01.20, FR-M02-01.21, FR-M02-01.22, FR-M02-01.26, FR-M02-01.27, BR-M02-01, BR-M02-03, BR-M02-26, BR-M02-34, FR-M01-05.06 |
| RULE-M02-002 | Đọc số/danh sách theo dõi hoặc trạng thái quan hệ đổi | Theo dõi chỉ người dùng; không đếm/hiện BANNED/DEACTIVATED, trở lại ACTIVE thì hiện/đếm lại nếu quan hệ còn; DELETED xóa quan hệ hai chiều theo M01. Không tự Follow/Unfollow từ thao tác xem. | FR-M02-02.03, FR-M02-02.06, FR-M02-02.07, FR-M02-02.08, FR-M02-02.09, BR-M02-14, BR-M02-27, BR-M02-31, FR-M01-12.08 |
| RULE-M02-003 | Lớp/Khối và định danh được sửa hoặc bước sang năm học | Lớp 10/11/12 hoặc trống, giữ đến khi chính chủ sửa; không tự tăng hoặc nhắc cập nhật, độc lập Lớp của bài. Khi đổi tên, áp M01; display_name là tên chính, username giữ hoa/thường; không có lịch sử tên. Dữ liệu Lớp cung cấp M12/M15, không triển khai lọc bảng xếp hạng/thống kê tại M02. | FR-M02-03.07, FR-M02-03.08, FR-M02-03.14, FR-M02-03.15, BR-M02-09, BR-M02-10, BR-M02-19, BR-M02-35, FR-M01-03.10, FR-M01-03.11, FR-M01-03.15, FR-M01-03.16 |
| RULE-M02-FLAGS | Cờ Group hoặc Chat tắt | Bài nhóm vẫn xuất hiện ở hồ sơ/Bookmark nếu đủ điều kiện; không xóa bookmark/ẩn bài chỉ vì cờ Group tắt. Khi actor mở bài nhóm thì M11 báo đang bận theo quyền cờ. Nút Nhắn tin trên hồ sơ người khác vẫn hiện khi Chat tắt; mở trò chuyện M16 xử lý đang bận. Chỉ mô tả hợp đồng lối vào, không triển khai chức năng Chat/Group. | FR-M02-01.07, FR-M02-01.26, FR-M02-01.27, FR-M02-07.03, FR-M16-15.07 |


## 6. Truy vết hai chiều

| FR/BR | SC/bước/nhánh hoặc quy tắc | Mức đối soát |
|---|---|---|
| FR-M02-01 | SC-M02-001/M1; SC-M02-001/E3.1; SC-M02-001/E11.1; SC-M02-001/E11.2; RULE-M02-001; SC-M02-001/M2; SC-M02-001/E4.1; SC-M02-001/E5.1; SC-M02-001/E8.1; SC-M02-001/E9.1; SC-M02-001/E12.1; SC-M02-001/E12.2; SC-M02-001/E6.1; SC-M02-001/E10.1; SC-M02-004/M2; SC-M02-001/E7.1; RULE-M02-FLAGS; AUT-M02-002; SC-M02-001/E1.1; SC-M02-001/E13.1; SC-M02-001/E13.2; SC-M02-001/E2.1; SC-M02-001/E14.1; SC-M02-001/E14.2; SC-M02-001/E8.2; SC-M02-001/E8.3 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-02 | SC-M02-001/E2.1; SC-M02-001/E14.1; SC-M02-001/E14.2; SC-M02-002/E2.1; SC-M02-001/E9.2; SC-M02-001/E9.3; SC-M02-002/M1; SC-M02-002/M2; SC-M02-002/E1.2; SC-M02-002/E4.1; SC-M02-002/E1.1; RULE-M02-002; SC-M02-002/E3.1; SC-M02-002/E5.1; SC-M02-002/E5.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03 | SC-M02-003/M1; SC-M02-003/M2; SC-M02-003/M6; SC-M02-003/E2.1; SC-M02-003/E4.1; SC-M02-003/E11.2; SC-M02-003/E1.1; SC-M02-003/E3.1; SC-M02-003/M3; SC-M02-003/M4; SC-M02-003/E12.1; SC-M02-003/M5; SC-M02-003/E5.1; SC-M02-003/E5.2; SC-M02-003/E11.1; SC-M02-003/E6.1; SC-M02-003/E6.2; RULE-M02-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-04 | SC-M02-004/M1; SC-M02-004/M2; SC-M02-004/E5.1; AUT-M02-001; SC-M02-004/E3.1; SC-M02-004/E4.1; SC-M02-004/E1.1; SC-M02-004/E2.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-05 | SC-M02-005/M1; SC-M02-005/M2; SC-M02-005/E2.1; SC-M02-005/E1.1; SC-M02-005/E3.1; SC-M02-005/E3.2; SC-M02-006/E3.1; SC-M02-006/E3.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-06 | SC-M02-006/M1; SC-M02-006/M2; SC-M02-006/E1.2; SC-M02-006/E2.1; SC-M02-007/E4.3 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-07 | SC-M02-006/E1.1; SC-M02-006/E1.2; SC-M02-007/E4.2; SC-M02-007/E4.3; SC-M02-007/M1; SC-M02-007/M2; SC-M02-007/E4.1; SC-M02-007/E5.1; SC-M02-007/E2.1; RULE-M02-FLAGS; SC-M02-007/E3.1; SC-M02-007/E1.1; SC-M02-007/E6.1; SC-M02-007/E6.2; AUT-M02-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.01 | SC-M02-001/M2; SC-M02-001/E4.1; SC-M02-001/E5.1; SC-M02-001/E8.1; SC-M02-001/E9.1; SC-M02-001/E11.1; SC-M02-001/E11.2; SC-M02-001/E12.1; SC-M02-001/E12.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.02 | SC-M02-001/M2; SC-M02-001/E4.1; SC-M02-001/E6.1; SC-M02-001/E8.1; SC-M02-001/E9.1; SC-M02-001/E10.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.03 | SC-M02-001/M2; SC-M02-001/E6.1; SC-M02-001/E8.1; SC-M02-001/E9.1; SC-M02-004/M2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.04 | SC-M02-001/E6.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.05 | SC-M02-001/M2; SC-M02-001/E8.1; SC-M02-001/E9.1; SC-M02-001/E10.1; RULE-M02-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.06 | SC-M02-001/E3.1; SC-M02-001/E4.1; SC-M02-001/E5.1; SC-M02-001/E7.1; SC-M02-001/E10.1; SC-M02-001/E11.1; SC-M02-001/E11.2; SC-M02-001/E12.1; SC-M02-001/E12.2; RULE-M02-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.07 | SC-M02-001/M2; SC-M02-001/E4.1; SC-M02-001/E5.1; SC-M02-001/E7.1; SC-M02-001/E8.1; SC-M02-001/E9.1; SC-M02-001/E10.1; SC-M02-001/E11.1; SC-M02-001/E11.2; SC-M02-001/E12.1; SC-M02-001/E12.2; RULE-M02-FLAGS | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.08 | SC-M02-001/E8.2; SC-M02-001/E8.3 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.09 | SC-M02-001/M2; SC-M02-001/E8.1; SC-M02-001/E9.1; AUT-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.10 | SC-M02-001/M2; SC-M02-001/E6.1; SC-M02-001/E8.1; SC-M02-001/E9.1; AUT-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.11 | SC-M02-001/E2.1; SC-M02-001/E11.1; SC-M02-001/E11.2; SC-M02-001/E14.1; SC-M02-001/E14.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.12 | SC-M02-001/E5.1; SC-M02-001/E11.1; SC-M02-001/E11.2; SC-M02-001/E12.1; SC-M02-001/E12.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.13 | SC-M02-001/M2; SC-M02-001/E8.1; SC-M02-001/E9.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.14 | SC-M02-001/M2; SC-M02-001/E8.1; SC-M02-001/E9.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.15 | SC-M02-001/M2; SC-M02-001/E8.1; SC-M02-001/E9.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.16 | SC-M02-001/E11.1; SC-M02-001/E11.2; SC-M02-001/E12.1; SC-M02-001/E12.2; RULE-M02-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.17 | SC-M02-001/M2; SC-M02-001/E8.1; SC-M02-001/E9.1; SC-M02-001/E10.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.18 | SC-M02-001/E6.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.19 | SC-M02-001/M2; SC-M02-001/E7.1; SC-M02-001/E8.1; SC-M02-001/E9.1; SC-M02-001/E10.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.20 | SC-M02-001/M1; SC-M02-001/E3.1; SC-M02-001/E11.1; SC-M02-001/E11.2; RULE-M02-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.21 | SC-M02-001/E1.1; SC-M02-001/E11.1; SC-M02-001/E11.2; SC-M02-001/E13.1; SC-M02-001/E13.2; RULE-M02-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.22 | SC-M02-001/E1.1; SC-M02-001/E3.1; SC-M02-001/E13.1; SC-M02-001/E13.2; RULE-M02-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.23 | SC-M02-001/M2; SC-M02-001/E8.1; SC-M02-001/E9.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.24 | SC-M02-001/M2; SC-M02-001/E6.1; SC-M02-001/E8.1; SC-M02-001/E9.1; AUT-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.25 | SC-M02-001/M2; SC-M02-001/E6.1; SC-M02-001/E8.1; SC-M02-001/E9.1; AUT-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.26 | SC-M02-001/E3.1; SC-M02-001/E4.1; SC-M02-001/E7.1; RULE-M02-001; RULE-M02-FLAGS | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-01.27 | SC-M02-001/M2; SC-M02-001/E8.1; SC-M02-001/E9.1; SC-M02-001/E11.1; SC-M02-001/E11.2; SC-M02-001/E12.1; SC-M02-001/E12.2; RULE-M02-001; RULE-M02-FLAGS | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-02.01 | SC-M02-001/E9.2; SC-M02-001/E9.3; SC-M02-002/M1; SC-M02-002/M2; SC-M02-002/E1.2; SC-M02-002/E4.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-02.02 | SC-M02-001/E9.3; SC-M02-002/M2; SC-M02-002/E1.1; SC-M02-002/E1.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-02.03 | SC-M02-001/E9.3; SC-M02-002/M2; SC-M02-002/E1.2; RULE-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-02.04 | SC-M02-001/E2.1; SC-M02-001/E14.1; SC-M02-001/E14.2; SC-M02-002/E2.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-02.05 | SC-M02-002/E5.1; SC-M02-002/E5.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-02.06 | SC-M02-001/E9.3; SC-M02-002/M2; SC-M02-002/E1.2; RULE-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-02.07 | SC-M02-001/E9.3; SC-M02-002/M2; SC-M02-002/E1.2; SC-M02-002/E3.1; SC-M02-002/E4.1; RULE-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-02.08 | SC-M02-001/E9.3; SC-M02-002/M2; SC-M02-002/E1.2; SC-M02-002/E3.1; RULE-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-02.09 | SC-M02-001/E9.3; SC-M02-002/M2; SC-M02-002/E1.2; SC-M02-002/E3.1; SC-M02-002/E4.1; RULE-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03.01 | SC-M02-003/M1; SC-M02-003/M2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03.02 | SC-M02-003/M5; SC-M02-003/M6; SC-M02-003/E12.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03.03 | SC-M02-003/M3; SC-M02-003/M4 | Một phần — GAP-001 cho bộ đếm khi đang gõ |
| FR-M02-03.04 | SC-M02-003/M6; SC-M02-003/E5.1; SC-M02-003/E5.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03.05 | SC-M02-003/M6; SC-M02-003/E11.1; SC-M02-003/E11.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03.06 | SC-M02-003/M6; SC-M02-003/E6.1; SC-M02-003/E6.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03.07 | SC-M02-003/M6; SC-M02-003/E11.1; SC-M02-003/E11.2; RULE-M02-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03.08 | SC-M02-003/M6; SC-M02-003/E11.2; RULE-M02-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03.09 | SC-M02-003/M2; SC-M02-003/M6; SC-M02-003/E2.1; SC-M02-003/E4.1; SC-M02-003/E11.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03.10 | SC-M02-003/M2; SC-M02-003/M6; SC-M02-003/E1.1; SC-M02-003/E3.1; SC-M02-003/E11.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03.11 | SC-M02-003/M4; SC-M02-003/M6; SC-M02-003/E11.2; SC-M02-003/E12.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03.12 | SC-M02-003/M6; SC-M02-003/E11.1; SC-M02-003/E11.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03.13 | SC-M02-003/M4; SC-M02-003/M6; SC-M02-003/E12.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03.14 | SC-M02-003/M6; SC-M02-003/E11.1; SC-M02-003/E11.2; RULE-M02-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-03.15 | SC-M02-003/M6; SC-M02-003/E11.2; RULE-M02-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-04.01 | SC-M02-004/M1; SC-M02-004/M2; SC-M02-004/E5.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-04.02 | SC-M02-004/M2; SC-M02-004/E5.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-04.03 | SC-M02-004/E1.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-04.04 | SC-M02-004/E2.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-04.05 | SC-M02-004/M2; SC-M02-004/E5.1; AUT-M02-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-04.06 | SC-M02-004/M2; SC-M02-004/E3.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-04.07 | SC-M02-004/M2; SC-M02-004/E4.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-05.01 | SC-M02-005/M1; SC-M02-005/M2; SC-M02-005/E2.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-05.02 | SC-M02-005/E3.1; SC-M02-005/E3.2; SC-M02-006/E3.1; SC-M02-006/E3.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-05.03 | SC-M02-005/M2; SC-M02-005/E1.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-05.04 | SC-M02-005/E2.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-05.05 | SC-M02-005/M2; SC-M02-005/E2.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-06.01 | SC-M02-006/M1; SC-M02-006/M2; SC-M02-006/E1.2; SC-M02-006/E2.1; SC-M02-007/E4.3 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-06.02 | SC-M02-006/E2.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-07.01 | SC-M02-007/M1; SC-M02-007/M2; SC-M02-007/E4.1; SC-M02-007/E5.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-07.02 | SC-M02-007/E1.1; SC-M02-007/E6.1; SC-M02-007/E6.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-07.03 | SC-M02-007/M2; SC-M02-007/E2.1; SC-M02-007/E4.1; RULE-M02-FLAGS | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-07.04 | SC-M02-007/M2; SC-M02-007/E2.1; SC-M02-007/E4.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-07.05 | SC-M02-006/E1.1; SC-M02-006/E1.2; SC-M02-007/E4.2; SC-M02-007/E4.3 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-07.06 | SC-M02-007/E3.1; SC-M02-007/E5.1; AUT-M02-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M02-07.07 | SC-M02-007/M2; SC-M02-007/E2.1; SC-M02-007/E3.1; SC-M02-007/E4.1; SC-M02-007/E4.3; SC-M02-007/E5.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-01 | SC-M02-001/M1; SC-M02-001/M2; SC-M02-001/E4.1; SC-M02-001/E8.1; SC-M02-001/E9.1; RULE-M02-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-02 | SC-M02-001/M2; SC-M02-001/E8.1; SC-M02-001/E9.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-03 | SC-M02-001/M2; SC-M02-001/E4.1; SC-M02-001/E8.1; SC-M02-001/E9.1; RULE-M02-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-04 | SC-M02-003/M4; SC-M02-003/M6; SC-M02-003/E5.1; SC-M02-003/E5.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-05 | SC-M02-001/E6.1; SC-M02-003/E11.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-06 | SC-M02-004/M2; SC-M02-004/E5.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-07 | SC-M02-004/M2; SC-M02-004/E5.1; AUT-M02-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-08 | SC-M02-001/M2; SC-M02-001/E6.1; SC-M02-001/E8.1; SC-M02-001/E9.1; SC-M02-004/M2; SC-M02-004/E5.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-09 | SC-M02-003/M6; SC-M02-003/E6.1; SC-M02-003/E6.2; SC-M02-003/E11.1; SC-M02-003/E11.2; RULE-M02-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-10 | SC-M02-003/M6; SC-M02-003/E11.2; RULE-M02-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-11 | SC-M02-001/M2; SC-M02-001/E8.1; SC-M02-001/E9.1; AUT-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-12 | SC-M02-001/M2; SC-M02-001/E8.1; SC-M02-001/E9.1; AUT-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-13 | SC-M02-001/M2; SC-M02-001/E6.1; SC-M02-001/E8.1; SC-M02-001/E9.1; AUT-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-14 | SC-M02-001/E9.3; SC-M02-002/M2; SC-M02-002/E1.2; SC-M02-002/E5.1; SC-M02-002/E5.2; RULE-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-15 | SC-M02-001/E2.1; SC-M02-001/E14.1; SC-M02-001/E14.2; SC-M02-002/E2.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-16 | SC-M02-001/E5.1; SC-M02-001/E12.1; SC-M02-001/E12.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-17 | SC-M02-001/M2; SC-M02-001/E8.1; SC-M02-001/E9.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-18 | SC-M02-003/M2; SC-M02-003/M6; SC-M02-003/E2.1; SC-M02-003/E4.1; SC-M02-004/M2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-19 | SC-M02-001/M2; SC-M02-001/E8.1; SC-M02-001/E9.1; RULE-M02-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-20 | SC-M02-001/M2; SC-M02-001/E8.1; SC-M02-001/E9.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-21 | SC-M02-005/M2; SC-M02-005/E2.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-22 | SC-M02-005/M2; SC-M02-005/E1.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-23 | SC-M02-005/M2; SC-M02-007/M2; SC-M02-007/E1.1; SC-M02-007/E4.1; SC-M02-007/E5.1; SC-M02-007/E6.1; SC-M02-007/E6.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-24 | SC-M02-005/M2; SC-M02-005/E3.1; SC-M02-005/E3.2; SC-M02-006/M2; SC-M02-006/E3.1; SC-M02-006/E3.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-25 | SC-M02-005/E2.1; SC-M02-006/E2.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-26 | SC-M02-001/E11.1; SC-M02-001/E11.2; SC-M02-001/E12.1; SC-M02-001/E12.2; RULE-M02-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-27 | SC-M02-001/E9.3; SC-M02-002/M2; SC-M02-002/E1.2; SC-M02-002/E3.1; SC-M02-002/E4.1; RULE-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-28 | SC-M02-001/M2; SC-M02-001/E4.1; SC-M02-001/E7.1; SC-M02-001/E8.1; SC-M02-001/E9.1; SC-M02-001/E10.1; SC-M02-001/E11.1; SC-M02-001/E11.2; SC-M02-001/E12.1; SC-M02-001/E12.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-29 | SC-M02-006/E1.2; SC-M02-007/M2; SC-M02-007/E2.1; SC-M02-007/E4.1; SC-M02-007/E4.3 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-30 | SC-M02-007/E3.1; SC-M02-007/E5.1; AUT-M02-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-31 | SC-M02-001/M2; SC-M02-001/E7.1; SC-M02-001/E8.1; SC-M02-001/E9.1; SC-M02-001/E9.3; SC-M02-001/E10.1; SC-M02-002/M2; SC-M02-002/E1.2; SC-M02-002/E3.1; SC-M02-002/E4.1; SC-M02-007/M2; SC-M02-007/E2.1; SC-M02-007/E3.1; SC-M02-007/E4.1; SC-M02-007/E4.3; SC-M02-007/E5.1; RULE-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-32 | SC-M02-001/E6.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-33 | SC-M02-003/M4; SC-M02-003/M6; SC-M02-003/E11.1; SC-M02-003/E11.2; SC-M02-003/E12.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-34 | SC-M02-001/M1; SC-M02-001/E1.1; SC-M02-001/E3.1; SC-M02-001/E11.1; SC-M02-001/E11.2; SC-M02-001/E13.1; SC-M02-001/E13.2; RULE-M02-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-35 | SC-M02-003/M6; SC-M02-003/E11.2; RULE-M02-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-36 | SC-M02-003/M2; SC-M02-003/M6; SC-M02-003/E1.1; SC-M02-003/E3.1; SC-M02-004/M2; SC-M02-004/E4.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M02-37 | SC-M02-001/M2; SC-M02-001/E6.1; SC-M02-001/E8.1; SC-M02-001/E9.1; AUT-M02-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |


Truy vết ngược nằm trong sources của từng bước. Có vị trí không tự chứng minh đầy đủ ngữ nghĩa. E ghi bước thay thế, gồm cả hành trình tại M1 theo actor Guest trong cùng chức năng, không phải BF mới. Không trộn actor Guest và User trong cùng một bước, không bịa đăng nhập để đổi vai trò.

## 7. GAP, giới hạn và trạng thái

| ID | Nguồn | Điều chưa rõ / giới hạn | Ảnh hưởng |
|---|---|---|---|
| GAP-SC-M02-001 | FR-M02-03.03, FR-M02-03.11, BR-M02-33; UC003/main-3/main-4 | Nguồn yêu cầu hiển thị số ký tự khi nhập và đếm sau trim khi lưu, nhưng chưa xác định bộ đếm lúc đang gõ có trim tức thời hay không. Không tự hiển thị một con số xác định cho chuỗi còn khoảng trắng đầu/cuối. | SC003/M4 mô tả hiện bộ đếm; dữ liệu 12 là số dùng kiểm khi lưu. Đường lưu hợp lệ/sửa lỗi vẫn có; cần chốt bộ đếm trước nghiệm thu HMI. |
| NOTE-M02-02 | US-M02 NOTE-M02-02; FR-M02-01.18 | Hình thức avatar mặc định chưa chọn. | Dùng avatar mặc định, không bịa màu/chữ cái/ảnh mẫu. |
| NOTE-M02-04 | US-M02 NOTE-M02-04 | Không có hợp đồng retry/rollback ảnh, UX lỗi mạng hoặc bỏ lưu bookmark vốn không tồn tại. | Không thêm các nhánh này; thao tác bỏ lưu giả định bookmark tồn tại. Không coi im lặng nguồn là quyền tạo cơ chế mới. |
| NOTE-SCOPE | FR-M02 Phụ lục B.2 và US NOTE-M02-01/05 | FR không có TBD nghiệp vụ mở; Mod/Admin gỡ avatar/bio người khác đã quyết không làm. | GAP-001 chỉ ghi ở bản scenario để review, không tự sửa FR/US/register. Không mở lại tính năng đã loại. |


## 8. Kiểm tra và bàn giao

Kết quả thực tế, lệnh kiểm và giới hạn nằm ở [QA-M02.md](QA-M02.md). Chưa có phê duyệt cuối. Chỉ tạo thư mục M02 khi ghi đầu ra, không tạo thư mục module khác.


## Chuyển đổi ID nhánh sau QA-SC-01

Ngày 11/11/2026, các biến thể vai trò được đăng ký thành E tại M1 theo skill v1.4. Bảng này giữ ID lịch sử để đối chiếu các tài liệu đã dẫn V. Mỗi hàng ánh xạ cả nhánh và các bước cùng số thứ tự, ví dụ V1.2 sang bước .2 của E tương ứng.

| ID lịch sử | ID hiện hành | Điểm thay | Số bước | Nguồn |
| --- | --- | --- | --- | --- |
| SC-M02-001/V1 | SC-M02-001/E11 | M1 | 2 | FR-M02-01.01, FR-M02-01.06, FR-M02-01.07, FR-M02-01.11, FR-M02-01.12, FR-M02-01.16, FR-M02-01.20, FR-M02-01.21, FR-M02-01.27, BR-M02-26, BR-M02-28, BR-M02-34 |
| SC-M02-001/V2 | SC-M02-001/E12 | M1 | 2 | FR-M02-01.01, FR-M02-01.06, FR-M02-01.07, FR-M02-01.12, FR-M02-01.16, FR-M02-01.27, BR-M02-16, BR-M02-26, BR-M02-28 |
| SC-M02-001/V3 | SC-M02-001/E13 | M1 | 2 | FR-M02-01.21, FR-M02-01.22, BR-M02-34 |
| SC-M02-001/V4 | SC-M02-001/E14 | M1 | 2 | FR-M02-01.11, FR-M02-02.04, BR-M02-15 |
| SC-M02-002/V1 | SC-M02-002/E5 | M1 | 2 | FR-M02-02.05, BR-M02-14 |
| SC-M02-005/V1 | SC-M02-005/E3 | M1 | 2 | FR-M02-05.02, BR-M02-24 |
| SC-M02-006/V1 | SC-M02-006/E3 | M1 | 2 | FR-M02-05.02, BR-M02-24 |
| SC-M02-007/V1 | SC-M02-007/E6 | M1 | 2 | FR-M02-07.02, BR-M02-23 |
