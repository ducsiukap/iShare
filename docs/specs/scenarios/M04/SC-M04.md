# Kịch bản nghiệp vụ — M04 Comment

[Vietnamese Doc] — 2026-11-09 — Skill scenarios v1.3.

Mục đích: triển khai các chức năng actor hoàn thành cùng hệ thống từ FR + US. Boundary là toàn iShare; M01/M03/M07/M08/M09/M11/M12/M13 đều bên trong SYSTEM. M04 không có actor AI vì không gọi quét trước khi đăng.

**Phạm vi:** 3 nhóm UC chính,7 UC con,8 mapping;6 hành trình đọc/viết gốc/trả lời/sửa/xóa/xem lại. Core020 abstract và UC007 dùng chung được khai triển trong các luồng cụ thể. Không tách BF theo khóa, HEAVY, Bị ẩn, Guest hay loại đích trả lời.

**Ngoài phạm vi:** đăng nhập/ban, thuật toán nhắc tên, gửi thông báo, upvote/điểm, quét AI hoặc ẩn bình luận ở M08, xử lý khiếu nại, nhóm/Owner/Group Mod, feed/tìm kiếm/Trending/thống kê. Không thêm tệp, lịch sử sửa, khôi phục/xóa hẳn bình luận, Accepted Answer hoặc khiếu nại bình luận riêng.

**Trạng thái:** Đang soạn để review; FR-M04 đã chốt nhưng US-M04/overview Chờ duyệt. TBD-M04-01 đã đóng: lật cảnh cáo/ban không tự gỡ Bị ẩn. Giữ các chi tiết HMI chưa chốt thay vì bịa luật.

## 1. Baseline và dữ liệu

<!-- sc:document -->

| key | value |
|---|---|
| module | M04 |
| scope | ALL |
| skill_version | 1.3 |
| output_dir | docs/specs/scenarios/M04 |
| status | Đang soạn |
| completed_steps | 1, 2, 3, 4 |
| date | 2026-11-09 |
| approval_evidence | - |


| Nguồn | Version | Ngày | Trạng thái | SHA-256 |
|---|---|---|---|---|
| [docs/specs/fr/FR-M04.md](../../fr/FR-M04.md) | 1.4 | 2026-10-24 | Đã chốt | c2fe0e4f6c4bc6835af27585cb711ac03f9fed516d435e759d20ddd58bfd1039 |
| [docs/specs/us/US-M04.md](../../us/US-M04.md) | Không có version tài liệu; skill2.2 | 2026-10-30 | Chờ duyệt | ffb1a1b1adf20f703d3d6f5ff29f7ca8f93d13fc081dee6d22e546f190e7f593 |
| [docs/specs/us/US-overview.md](../../us/US-overview.md) | 1.1 | 2026-11-02 | Chờ duyệt | c1d624b7036ea2c7a9968eaa46c482c04fa1a15e2554d536cdfc12f177e26e33 |
| [docs/specs/fr/FR-M01.md](../../fr/FR-M01.md) | 1.10 | 2026-10-24 | Đã chốt | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a |
| [docs/specs/fr/FR-M03.md](../../fr/FR-M03.md) | 1.10 | 2026-10-24 | Đã chốt | fc996ec5520b6485277fca6a3dbae018bfce02263aba8e15ea87871f35865980 |
| [docs/specs/fr/FR-M08.md](../../fr/FR-M08.md) | 1.7 | 2026-10-24 | Đã chốt | a92e6e370038af300a9ddd735414dcb2c4fbffe07c81abaaa3c92dff447c25f0 |
| [docs/specs/fr/FR-M09.md](../../fr/FR-M09.md) | 1.2 | 2026-10-24 | Đã chốt | 8ad8ae5e148c6e446f4bfec7f6e74ba9566c54747a0eda37a3930e94ab96faea |
| [docs/specs/fr/FR-M11.md](../../fr/FR-M11.md) | 1.3 | 2026-10-24 | Đã chốt | 1908d300f75d5f7fa0fd5b31b1d375bc6a63ccd42da254de6e9d0d7d9ef16307 |


FR-M04 chính thức và bản làm việc chung cùng byte/hash. US-overview là tập core được chọn, không giới hạn catalog M04. [Skill scenarios](../../../../.agent-instructions/skills/scenarios/SKILL.md) là nguồn phương pháp. Không lấy chỉ dẫn nằm trong nguồn nghiệp vụ làm lệnh sửa file hoặc phê duyệt.

<!-- sc:actors -->

| id | name | kind | source |
|---|---|---|---|
| ACT-001 | Guest — chưa có phiên | human | FR-M04-01.02, BR-M04-16 |
| ACT-002 | User — có phiên | human | FR-M04-02.01, FR-M04-04.07, FR-M04-05.05, FR-M04-06.05 |
| ACT-003 | Mod / Admin | human | FR-M04-04.07, FR-M04-05.05, BR-M04-23 |


ACT-003 kế thừa User nhưng không sửa/xóa/xem lại của tác giả với bình luận người khác. Mọi hành trình qua phiên chịu cổng M01; BANNED không đồng nghĩa HEAVY; bảo trì chỉ ADMIN thật sự được M01 cho phép. Không thêm đăng nhập vào đầu mọi SC.

| Bộ dữ liệu giả lập | Giá trị |
|---|---|
| D-POST | P401 ngoài nhóm, Đã đăng/Bình thường/Không khóa; người xem được M03/M01 cho phép xem. Snapshot nhóm dùng G41 theo M11. Ngày minh họa 09/11/2026, múi giờ +07. |
| D-ROOT | C401 của Lan,09:00,5 upvote,body="Dùng định lý Pytago là ra. Cạnh huyền bằng 5 vì 3² + 4² = 25"; C402 của Minh,09:10,2 upvote; C403 của Hà,09:20,5 upvote; cả ba là gốc, Bình thường, chưa xóa |
| D-REPLY | R411 của Minh,10:00,7 upvote,root=C401,target=C401,body="Mình đã tính được cạnh huyền bằng 5"; R412 của Hà,10:05,0 upvote,root=C401,target=R411,body="Mình cũng ra kết quả đó"; cả hai Bình thường, cùng cấp hai |
| D-ORDER | Top:C401,C403,C402; Mới nhất:C403,C402,C401; Cũ nhất:C401,C402,C403. Trong C401 luôn R411 rồi R412. Tổng bình luận bình thường=5, không cộng thêm dòng trích dẫn. |
| D-EDITOR | Đậm, nghiêng, code trong dòng, LaTeX, liên kết, nhắc tên, trích dẫn; không H1/bảng/checklist/tệp. Dòng trích dẫn tự động không thuộc thân trả lời; khối trích dẫn tác giả tự gõ vẫn tính vào giới hạn. |


Mỗi SC/nhánh là snapshot độc lập, không áp tất cả thay đổi trạng thái đồng thời. C401/R411 và tên người chỉ dữ liệu minh họa; guard nêu người/ID khác thì thay bộ dữ liệu của lần yêu cầu đó. Thời điểm +07 ngày09/11/2026 trừ mốc khác ghi rõ. Các chuỗi1000/1001 từ là "từ" lặp số lần tương ứng, ngăn cách bởi một khoảng trắng. Không đưa dữ liệu cá nhân, token hoặc upload thật vào mẫu.

## 2. Kiểm kê nhóm UC

<!-- sc:decomposition -->

| core | sub | source |
|---|---|---|
| UC-M04-010 | UC-M04-001 | FR-M04-01, BR-M04-03, BR-M04-04, BR-M04-05, BR-M04-06, BR-M04-07, BR-M04-13, BR-M04-17, BR-M04-18 |
| UC-M04-010 | UC-M04-006 | FR-M04-06, BR-M04-22, BR-M04-23, FR-M09-08.15 |
| UC-M04-020 | UC-M04-002 | FR-M04-02, BR-M04-12, BR-M04-14, BR-M04-15, BR-M04-19 |
| UC-M04-020 | UC-M04-003 | FR-M04-03, BR-M04-03, BR-M04-04, BR-M04-14, BR-M04-15, BR-M04-19 |
| UC-M04-020 | UC-M04-007 | FR-M04-02.03, FR-M04-02.04, FR-M04-02.09, FR-M04-02.10, FR-M04-02.11, FR-M04-03.05, FR-M04-03.12, FR-M04-03.13, FR-M04-04.06, FR-M04-04.12, FR-M04-04.13, BR-M04-01, BR-M04-02, BR-M04-19 |
| UC-M04-030 | UC-M04-004 | FR-M04-04, BR-M04-07, BR-M04-19, BR-M04-20, FR-M08-08.03 |
| UC-M04-030 | UC-M04-005 | FR-M04-05, BR-M04-08, BR-M04-20, BR-M04-21, BR-M04-23 |
| UC-M04-030 | UC-M04-007 | FR-M04-02.03, FR-M04-02.04, FR-M04-02.09, FR-M04-02.10, FR-M04-02.11, FR-M04-03.05, FR-M04-03.12, FR-M04-03.13, FR-M04-04.06, FR-M04-04.12, FR-M04-04.13, BR-M04-01, BR-M04-02, BR-M04-19 |


<!-- sc:ucs -->

| id | treatment | scenarios | coverage | rationale | sources |
|---|---|---|---|---|---|
| UC-M04-010 | aggregate | SC-M04-001, SC-M04-006 | SC-M04-001/M2, SC-M04-006/M2 | Nhóm chức năng độc lập; không chạy tất cả UC con nối tiếp. | FR-M04-01, FR-M04-06, BR-M04-17, BR-M04-22 |
| UC-M04-020 | abstract | SC-M04-002, SC-M04-003 | SC-M04-002/M2, SC-M04-003/M2 | Hợp đồng trừu tượng, được thực hiện qua gốc/trả lời; không dựng lần chạy abstract. | FR-M04-02, FR-M04-03, BR-M04-03, BR-M04-12, BR-M04-14, BR-M04-15, BR-M04-16, BR-M04-19 |
| UC-M04-030 | aggregate | SC-M04-004, SC-M04-005 | SC-M04-004/M2, SC-M04-005/M2 | Nhóm chức năng độc lập; không chạy tất cả UC con nối tiếp. | FR-M04-04, FR-M04-05, BR-M04-07, BR-M04-08, BR-M04-20, BR-M04-21 |
| UC-M04-001 | scenario | SC-M04-001 | SC-M04-001/M2 | Actor chủ động thực hiện chức năng tới kết quả. | FR-M04-01, BR-M04-03, BR-M04-04, BR-M04-05, BR-M04-06, BR-M04-07, BR-M04-13, BR-M04-17, BR-M04-18 |
| UC-M04-002 | scenario | SC-M04-002 | SC-M04-002/M2 | Actor chủ động thực hiện chức năng tới kết quả. | FR-M04-02, BR-M04-12, BR-M04-14, BR-M04-15, BR-M04-19 |
| UC-M04-003 | scenario | SC-M04-003 | SC-M04-003/M2 | Actor chủ động thực hiện chức năng tới kết quả. | FR-M04-03, BR-M04-03, BR-M04-04, BR-M04-14, BR-M04-15, BR-M04-19 |
| UC-M04-004 | scenario | SC-M04-004 | SC-M04-004/M2 | Actor chủ động thực hiện chức năng tới kết quả. | FR-M04-04, BR-M04-07, BR-M04-19, BR-M04-20, FR-M08-08.03 |
| UC-M04-005 | scenario | SC-M04-005 | SC-M04-005/M2 | Actor chủ động thực hiện chức năng tới kết quả. | FR-M04-05, BR-M04-08, BR-M04-20, BR-M04-21, BR-M04-23 |
| UC-M04-006 | scenario | SC-M04-006 | SC-M04-006/M2 | Actor chủ động thực hiện chức năng tới kết quả. | FR-M04-06, BR-M04-22, BR-M04-23, FR-M09-08.15 |
| UC-M04-007 | embedded | SC-M04-002, SC-M04-003, SC-M04-004 | SC-M04-002/M2, SC-M04-003/M2, SC-M04-004/M2 | Phần soạn UC007 được triển khai trong M2/M3/M4 và các nhánh giới hạn của từng SC bao chứa; không có BF chỉ soạn. | FR-M04-02.03, FR-M04-02.04, FR-M04-02.09, FR-M04-02.10, FR-M04-02.11, FR-M04-03.05, FR-M04-03.12, FR-M04-03.13, FR-M04-04.06, FR-M04-04.12, FR-M04-04.13, BR-M04-01, BR-M04-02, BR-M04-19 |


| SVG nguồn | UC thành viên | Đối chiếu |
|---|---|---|
| D-M04-CORE | 3 | Khớp ID thành viên với US; không thêm quan hệ UML |
| D-M04-010 | 3 | Khớp ID thành viên với US; không thêm quan hệ UML |
| D-M04-020 | 4 | Khớp ID thành viên với US; không thêm quan hệ UML |
| D-M04-030 | 4 | Khớp ID thành viên với US; không thêm quan hệ UML |


## 3. Danh mục luồng nghiệp vụ

<!-- sc:flows -->

| id | uc | primary | trigger | goal | completion | covered_ucs | rationale | scenario | sources |
|---|---|---|---|---|---|---|---|---|---|
| BF-M04-001 | UC-M04-001 | ACT-002 | Minh mở phần bình luận của P401. | Đọc và sắp xếp luồng bình luận của bài | Luồng/dấu thay thế/trích dẫn/số đếm được trả đúng quyền và trạng thái, đúng thứ tự đã chọn; không sửa dữ liệu hoặc tạo phiếu upvote. | UC-M04-001 | Chức năng actor yêu cầu độc lập, từ yêu cầu tới kết quả; trạng thái/quyền/lỗi là nhánh. | SC-M04-001 | FR-M04-01.01, FR-M04-01.03, FR-M04-01.05, FR-M04-01.06, FR-M04-01.10, FR-M04-01.13, FR-M04-01.14, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04, BR-M04-05, BR-M04-06, BR-M04-07, BR-M04-17, BR-M04-18, FR-M04-01.11, FR-M11-03.06, FR-M04-01.04, FR-M04-01.07, FR-M04-01.08, FR-M04-01.09, BR-M04-08, BR-M04-13, FR-M04-01.15, FR-M04-01.12, BR-M04-14, FR-M03-14.04, FR-M03-14.05, FR-M01-13.03, FR-M01-13.04, FR-M04-01.02, BR-M04-16 |
| BF-M04-002 | UC-M04-002 | ACT-002 | Lan chọn viết bình luận gốc dưới P401. | Viết và gửi bình luận gốc dưới bài | Đúng một bình luận gốc mới được lưu và hiện ngay Bình thường, tác giả/mốc đúng; không đợi AI hoặc tự gửi thông báo ngoài contract M01/M07. | UC-M04-002, UC-M04-007 | Chức năng actor yêu cầu độc lập, từ yêu cầu tới kết quả; trạng thái/quyền/lỗi là nhánh. | SC-M04-002 | FR-M04-02.01, FR-M04-02.03, FR-M04-02.04, BR-M04-01, BR-M04-02, BR-M04-19, FR-M04-02.02, FR-M04-02.05, FR-M04-02.06, FR-M04-02.07, FR-M04-02.08, FR-M04-02.10, FR-M04-02.11, FR-M04-01.10, BR-M04-12, BR-M04-14, BR-M04-15, BR-M04-18, BR-M04-17, FR-M11-03.07, FR-M11-16.04, FR-M04-02.09, FR-M11-03.13, BR-M04-16 |
| BF-M04-003 | UC-M04-003 | ACT-002 | Hà bấm Trả lời trên C401 của Lan. | Trả lời bình luận trong luồng hai cấp | Trả lời mới hiển thị ngay đúng root và target, chỉ cấp hai; trích dẫn không thuộc body/độ dài, trạng thái Bình thường. | UC-M04-003, UC-M04-007 | Chức năng actor yêu cầu độc lập, từ yêu cầu tới kết quả; trạng thái/quyền/lỗi là nhánh. | SC-M04-003 | FR-M04-03.01, FR-M04-03.05, FR-M04-03.13, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04, FR-M04-03.02, FR-M04-03.04, FR-M04-03.06, FR-M04-03.07, FR-M04-03.08, FR-M04-03.09, FR-M04-03.10, FR-M04-03.12, FR-M04-01.05, FR-M04-01.10, BR-M04-06, BR-M04-12, BR-M04-14, BR-M04-15, BR-M04-18, BR-M04-19, FR-M04-03.03, FR-M04-03.11, BR-M04-17, FR-M11-03.07, FR-M11-16.04, FR-M04-02.09, FR-M04-02.10, FR-M04-02.11, FR-M11-03.13, BR-M04-16 |
| BF-M04-004 | UC-M04-004 | ACT-002 | Minh mở sửa R411 của mình. | Sửa nội dung bình luận của mình | Nội dung mới hợp lệ được lưu, mốc sửa gần nhất và nhãn đúng; giữ mốc đăng/vị trí/kiểm duyệt, không có lịch sử hoặc quét trước/khôi phục nội dung cũ. | UC-M04-004, UC-M04-007 | Chức năng actor yêu cầu độc lập, từ yêu cầu tới kết quả; trạng thái/quyền/lỗi là nhánh. | SC-M04-004 | FR-M04-04.05, FR-M04-04.04, FR-M04-04.06, FR-M04-04.07, FR-M04-04.08, FR-M04-04.09, FR-M04-04.10, BR-M04-01, BR-M04-02, BR-M04-07, BR-M04-20, FR-M04-04.01, FR-M04-04.02, FR-M04-04.03, FR-M04-04.11, FR-M04-04.13, FR-M04-01.06, FR-M04-01.16, BR-M04-04, BR-M04-19, FR-M08-08.03, FR-M11-10.09, FR-M04-04.12, FR-M11-10.08, BR-M04-16 |
| BF-M04-005 | UC-M04-005 | ACT-002 | Lan yêu cầu xóa bình luận gốc C401 của mình. | Xóa bình luận của mình khỏi luồng người dùng | Cờ xóa được ghi, dữ liệu giữ; luồng/dấu/trích dẫn/số đếm đúng trường hợp; không xóa người khác, không khôi phục hoặc xóa hẳn bình luận. | UC-M04-005 | Chức năng actor yêu cầu độc lập, từ yêu cầu tới kết quả; trạng thái/quyền/lỗi là nhánh. | SC-M04-005 | FR-M04-05.01, FR-M04-05.04, FR-M04-05.05, FR-M04-05.06, FR-M04-05.07, FR-M04-01.07, FR-M04-01.08, FR-M04-01.10, BR-M04-08, BR-M04-18, BR-M04-21, BR-M04-23, FR-M04-05.10, FR-M11-10.09, FR-M04-05.02, FR-M04-01.15, FR-M04-05.03, FR-M04-05.08, FR-M04-05.09, BR-M04-20, FR-M11-10.08, BR-M04-16 |
| BF-M04-006 | UC-M04-006 | ACT-002 | Lan mở thông báo Bình luận của bạn đã bị ẩn cho C401 của mình. | Xem lại nội dung bình luận mình đã bị xử lý | Tác giả nhận đúng nội dung chỉ đọc trong ngữ cảnh hợp lệ, dữ liệu người báo cáo được bảo vệ; không đổi cờ xóa/kiểm duyệt/quyền trong luồng. | UC-M04-006 | Chức năng actor yêu cầu độc lập, từ yêu cầu tới kết quả; trạng thái/quyền/lỗi là nhánh. | SC-M04-006 | FR-M04-06.01, FR-M04-06.04, FR-M04-06.05, BR-M04-22, BR-M04-23, FR-M04-06.02, FR-M04-06.03, FR-M09-08.15, BR-M04-21 |


UC002/003 chuyên biệt core020 theo hợp đồng chung: một lần gửi tạo gốc trực tiếp dưới bài hoặc trả lời một đích trong luồng hai cấp. Không tạo SC thứ ba cho core abstract. UC020 include UC007 được hai chuyên biệt kế thừa; UC004 include UC007. Phần soạn/kiểm/lưu đã viết đủ trong SC002/003/004, không dừng sau câu gọi UC. Không có extend chỉ vì các chức năng cùng hiện dưới bài.

| Quan hệ US | Điểm hợp đồng | Trở về |
|---|---|---|
| UC-M04-002 generalization UC-M04-020 | #uc-m04-020-contract | - |
| UC-M04-003 generalization UC-M04-020 | #uc-m04-020-contract | - |
| UC-M04-020 include UC-M04-007 | #uc-m04-020-main-2 | #uc-m04-020-main-3 |
| UC-M04-004 include UC-M04-007 | #uc-m04-004-main-2 | #uc-m04-004-main-3 |


## 4. Scenario sáu phần

<a id="sc-m04-001"></a>

<!-- sc:scenario SC-M04-001 -->

### SC-M04-001

#### 1. Tên kịch bản chuẩn

Đọc và sắp xếp luồng bình luận của bài — BF-M04-001. UC owner: [UC-M04-001](../../us/US-M04.md#uc-m04-001). Trigger: Minh mở phần bình luận của P401.

#### 2. Actor thực hiện

ACT-002 — User có phiên là actor chính. ACT-003 kế thừa tương tác User theo US, không có đặc quyền sửa/xóa/xem lại của tác giả đối với người khác. Actor khởi tạo thay thế được ghi tại đường V trong mục6. Không có actor AI hoặc dịch vụ nội bộ.

#### 3. Tiền điều kiện

Có yêu cầu xem bình luận của P401; không bắt buộc đăng nhập, quyền xem bài được kiểm khi trả kết quả. Đường chuẩn ACT-002 có quyền xem; dữ liệu D-ROOT/D-REPLY là các bình luận Bình thường chưa xóa.

#### 4. Hậu điều kiện

<!-- sc:post SC-M04-001 -->

| result | condition |
|---|---|
| SUCCESS | Luồng/dấu thay thế/trích dẫn/số đếm được trả đúng quyền và trạng thái, đúng thứ tự đã chọn; không sửa dữ liệu hoặc tạo phiếu upvote. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi kết quả gửi/sửa/xóa thành công trái điều kiện. Dữ liệu trước yêu cầu giữ nguyên trừ hiệu ứng được nêu rõ trong nhánh. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M04-001 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Minh mở phần bình luận của P401. | P401 ngoài nhóm, Đã đăng/Bình thường/Không khóa; người xem được M03/M01 cho phép xem. Snapshot nhóm dùng G41 theo M11. Ngày minh họa 09/11/2026, múi giờ +07. | M2 | FR-M04-01.01 |
| M2 | SYSTEM | Hệ thống kiểm quyền xem bài, dựng gốc và trả lời hai cấp, mặc định Top; dựng trích dẫn từ tên/nội dung hiện tại của đích, không lồng dòng trích dẫn hệ thống của đích. Hiện nhãn đã chỉnh sửa khi có, số bình luận chung, giữ trả lời cũ đến mới. | C401 của Lan,09:00,5 upvote,body="Dùng định lý Pytago là ra. Cạnh huyền bằng 5 vì 3² + 4² = 25"; C402 của Minh,09:10,2 upvote; C403 của Hà,09:20,5 upvote; cả ba là gốc, Bình thường, chưa xóa; R411 của Minh,10:00,7 upvote,root=C401,target=C401,body="Mình đã tính được cạnh huyền bằng 5"; R412 của Hà,10:05,0 upvote,root=C401,target=R411,body="Mình cũng ra kết quả đó"; cả hai Bình thường, cùng cấp hai; Top:C401,C403,C402; Mới nhất:C403,C402,C401; Cũ nhất:C401,C402,C403. Trong C401 luôn R411 rồi R412. Tổng bình luận bình thường=5, không cộng thêm dòng trích dẫn.; trích R411: Lan + phần đầu nội dung C401 vừa một dòng; trích R412: Minh + phần đầu body R411, không trích thêm C401 | END:SUCCESS | FR-M04-01.01, FR-M04-01.03, FR-M04-01.05, FR-M04-01.06, FR-M04-01.10, FR-M04-01.13, FR-M04-01.14, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04, BR-M04-05, BR-M04-06, BR-M04-07, BR-M04-17, BR-M04-18 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Guard chỉ bộ dữ liệu/ngữ cảnh thay thế cho lần thực thi: thay cả tên người/ID đối tượng minh họa khi được nêu, vẫn cùng vai trò actor; không gửi đồng thời bộ chuẩn và bộ lỗi. Các đường sửa quay lại bước kiểm cụ thể; nếu còn sai áp lại cùng guard, không tự giới hạn lần. REJECTED là kết thúc hợp lệ theo US, không bịa nút OK/hủy/thử lại ngoài nguồn.

<!-- sc:exceptions SC-M04-001 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Người yêu cầu không được xem bài, kể cả Private không đủ quyền hoặc bài không còn hiển thị | E1.1 | FR-M04-01.11, BR-M04-17, FR-M11-03.06 |
| E2 | user-choice | M2 | Sau khi luồng đã được trả, người xem chọn Mới nhất | E2.1 | FR-M04-01.01, FR-M04-01.03, FR-M04-01.05, FR-M04-01.06, FR-M04-01.10, FR-M04-01.13, FR-M04-01.14, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04, BR-M04-05, BR-M04-06, BR-M04-07, BR-M04-17, BR-M04-18, FR-M04-01.04 |
| E3 | user-choice | M2 | Sau khi luồng đã được trả, người xem chọn Cũ nhất | E3.1 | FR-M04-01.01, FR-M04-01.03, FR-M04-01.05, FR-M04-01.06, FR-M04-01.10, FR-M04-01.13, FR-M04-01.14, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04, BR-M04-05, BR-M04-06, BR-M04-07, BR-M04-17, BR-M04-18, FR-M04-01.04 |
| E4 | user-choice | M2 | Sau khi luồng đã được trả, người xem chọn Top | E4.1 | FR-M04-01.01, FR-M04-01.03, FR-M04-01.05, FR-M04-01.06, FR-M04-01.10, FR-M04-01.13, FR-M04-01.14, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04, BR-M04-05, BR-M04-06, BR-M04-07, BR-M04-17, BR-M04-18, FR-M04-01.04 |
| E5 | system | M2 | Gốc C401 đã xóa hoặc Bị ẩn, còn R411/R412 bình thường | E5.1 | FR-M04-01.07, FR-M04-01.08, FR-M04-01.09, FR-M04-01.10, BR-M04-08, BR-M04-13, BR-M04-18 |
| E6 | system | M2 | Trả lời R411 đã xóa hoặc Bị ẩn, R412 vẫn bình thường | E6.1 | FR-M04-01.08, FR-M04-01.09, FR-M04-01.10, BR-M04-04, BR-M04-08, BR-M04-13, BR-M04-18 |
| E7 | system | M2 | Gốc đang hiện dấu, mọi trả lời đều không còn hiển thị bình thường | E7.1 | FR-M04-01.07, FR-M04-01.09, FR-M04-01.10, FR-M04-01.15, BR-M04-08, BR-M04-13, BR-M04-18 |
| E8 | system | M2 | Đích của trích dẫn được tác giả sửa, người xem tải lại luồng | E8.1 | FR-M04-01.06, FR-M04-01.16, FR-M04-01.17, BR-M04-04, BR-M04-07 |
| E9 | system | M2 | Bài từ không hiển thị trở lại hiển thị với người xem | E9.1 | FR-M04-01.09, FR-M04-01.10, FR-M04-01.12, BR-M04-13, BR-M04-17, BR-M04-18 |
| E10 | system | M2 | Bài Khóa bình luận hoặc Khóa toàn bộ nhưng vẫn được phép đọc | E10.1 | FR-M04-01.13, BR-M04-14, FR-M03-14.04, FR-M03-14.05 |
| E11 | system | M2 | Tài khoản tác giả bình luận DEACTIVATED hoặc DELETED, bình luận chưa xóa/không Bị ẩn | E11.1 | FR-M01-13.03, FR-M01-13.04 |
| E12 | system | M2 | Bài không có bình luận bình thường hoặc dấu còn hợp lệ | E12.1 | FR-M04-01.01, FR-M04-01.10, FR-M04-01.15, BR-M04-18 |


<!-- sc:branch SC-M04-001 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống không hiển thị luồng bình luận cho người đó; không dùng link bình luận để vượt quyền bài. | P401 không hiển thị với Minh, hoặc G41 Private và Minh ngoài nhóm | END:REJECTED | FR-M04-01.11, BR-M04-17, FR-M11-03.06 |


<!-- sc:branch SC-M04-001 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống trả luồng đang xem với thứ tự Top ở lần mở đầu. | Top:C401,C403,C402; Mới nhất:C403,C402,C401; Cũ nhất:C401,C402,C403. Trong C401 luôn R411 rồi R412. Tổng bình luận bình thường=5, không cộng thêm dòng trích dẫn. | E2.2 | FR-M04-01.01, FR-M04-01.03, FR-M04-01.05, FR-M04-01.06, FR-M04-01.10, FR-M04-01.13, FR-M04-01.14, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04, BR-M04-05, BR-M04-06, BR-M04-07, BR-M04-17, BR-M04-18 |
| E2.2 | ACT-002 | Minh chọn Mới nhất. | P401; chỉ đổi tiêu chí gốc | E2.3 | FR-M04-01.04 |
| E2.3 | SYSTEM | Hệ thống kiểm quyền xem bài rồi sắp lại gốc theo tiêu chí, giữ trả lời cũ đến mới và số đếm chung. | Gốc=C403,C402,C401; R411,R412 không đổi; count=5 | END:SUCCESS | FR-M04-01.04, FR-M04-01.05, FR-M04-01.10, FR-M04-01.14, BR-M04-05, BR-M04-06, BR-M04-18 |


<!-- sc:branch SC-M04-001 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống trả luồng đang xem với thứ tự Top ở lần mở đầu. | Top:C401,C403,C402; Mới nhất:C403,C402,C401; Cũ nhất:C401,C402,C403. Trong C401 luôn R411 rồi R412. Tổng bình luận bình thường=5, không cộng thêm dòng trích dẫn. | E3.2 | FR-M04-01.01, FR-M04-01.03, FR-M04-01.05, FR-M04-01.06, FR-M04-01.10, FR-M04-01.13, FR-M04-01.14, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04, BR-M04-05, BR-M04-06, BR-M04-07, BR-M04-17, BR-M04-18 |
| E3.2 | ACT-002 | Minh chọn Cũ nhất. | P401; chỉ đổi tiêu chí gốc | E3.3 | FR-M04-01.04 |
| E3.3 | SYSTEM | Hệ thống kiểm quyền xem bài rồi sắp lại gốc theo tiêu chí, giữ trả lời cũ đến mới và số đếm chung. | Gốc=C401,C402,C403; R411,R412 không đổi; count=5 | END:SUCCESS | FR-M04-01.04, FR-M04-01.05, FR-M04-01.10, FR-M04-01.14, BR-M04-05, BR-M04-06, BR-M04-18 |


<!-- sc:branch SC-M04-001 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống trả luồng đang xem với thứ tự Top ở lần mở đầu. | Top:C401,C403,C402; Mới nhất:C403,C402,C401; Cũ nhất:C401,C402,C403. Trong C401 luôn R411 rồi R412. Tổng bình luận bình thường=5, không cộng thêm dòng trích dẫn. | E4.2 | FR-M04-01.01, FR-M04-01.03, FR-M04-01.05, FR-M04-01.06, FR-M04-01.10, FR-M04-01.13, FR-M04-01.14, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04, BR-M04-05, BR-M04-06, BR-M04-07, BR-M04-17, BR-M04-18 |
| E4.2 | ACT-002 | Minh chọn Top. | P401; chỉ đổi tiêu chí gốc | E4.3 | FR-M04-01.04 |
| E4.3 | SYSTEM | Hệ thống kiểm quyền xem bài rồi sắp lại gốc theo tiêu chí, giữ trả lời cũ đến mới và số đếm chung. | Gốc=C401,C403,C402; R411,R412 không đổi; count=5 | END:SUCCESS | FR-M04-01.04, FR-M04-01.05, FR-M04-01.10, FR-M04-01.14, BR-M04-05, BR-M04-06, BR-M04-18 |


<!-- sc:branch SC-M04-001 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống không trả nội dung gốc, kể cả người xem là tác giả; tại vị trí gốc giữ [Bình luận đã bị xóa] và giữ hai trả lời. R411 trỏ gốc nên trích dẫn là trả lời [bình luận đã bị xóa]; R412 vẫn trích nội dung hiện tại R411. | Count=4: C402,C403,R411,R412; dấu C401 không tính; vị trí dấu gốc theo luồng, không tự đặt luật xếp mới riêng cho dấu | END:SUCCESS | FR-M04-01.07, FR-M04-01.08, FR-M04-01.09, FR-M04-01.10, BR-M04-08, BR-M04-13, BR-M04-18 |


<!-- sc:branch SC-M04-001 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống bỏ R411 khỏi luồng; R412 vẫn nằm cấp hai dưới C401, dòng trích dẫn thành trả lời [bình luận đã bị xóa]. Không lộ nội dung R411 cho bất kỳ ai trong luồng. | C401,C402,C403,R412 còn bình thường; count=4; không đổi root của R412 | END:SUCCESS | FR-M04-01.08, FR-M04-01.09, FR-M04-01.10, BR-M04-04, BR-M04-08, BR-M04-13, BR-M04-18 |


<!-- sc:branch SC-M04-001 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống bỏ dấu [Bình luận đã bị xóa] khỏi luồng, không xóa dữ liệu gốc/trả lời; chỉ trả các bình luận còn bình thường. | C401 xóa/ẩn; R411,R412 xóa/ẩn; C402,C403 còn, count=2 | END:SUCCESS | FR-M04-01.07, FR-M04-01.09, FR-M04-01.10, FR-M04-01.15, BR-M04-08, BR-M04-13, BR-M04-18 |


<!-- sc:branch SC-M04-001 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống lấy body/tên hiện tại của đích cho một dòng trích, chỉ phần đầu vừa một dòng; không dùng nội dung cũ hoặc các dòng trích của đích. Hiện (đã chỉnh sửa) ở bình luận đã sửa. | R411.body mới="Mình đã kiểm tra lại kết quả"; R412 trích Minh + body mới R411; count vẫn5; không ấn định số ký tự một dòng | END:SUCCESS | FR-M04-01.06, FR-M04-01.16, FR-M04-01.17, BR-M04-04, BR-M04-07 |


<!-- sc:branch SC-M04-001 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống trả lại bình luận chưa xóa của bài theo trạng thái kiểm duyệt hiện tại; không tự làm nội dung Bị ẩn hiện lại. | P401 được hiển thị lại; C401/C402/R411/R412 Bình thường hiện, C403 Bị ẩn không hiện; count=4 | END:SUCCESS | FR-M04-01.09, FR-M04-01.10, FR-M04-01.12, BR-M04-13, BR-M04-17, BR-M04-18 |


<!-- sc:branch SC-M04-001 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống tiếp tục trả bình luận đã có và số đếm đúng quyền; không suy mức khóa thành ẩn luồng hoặc cho tạo/sửa. | P401 ngoài nhóm, Đã đăng/Bình thường/Không khóa; người xem được M03/M01 cho phép xem. Snapshot nhóm dùng G41 theo M11. Ngày minh họa 09/11/2026, múi giờ +07. thay mức khóa; Top:C401,C403,C402; Mới nhất:C403,C402,C401; Cũ nhất:C401,C402,C403. Trong C401 luôn R411 rồi R412. Tổng bình luận bình thường=5, không cộng thêm dòng trích dẫn. | END:SUCCESS | FR-M04-01.13, BR-M04-14, FR-M03-14.04, FR-M03-14.05 |


<!-- sc:branch SC-M04-001 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | SYSTEM | Hệ thống giữ nội dung bình luận và thay tên/avatar theo M01; không đồng nhất tài khoản đã xóa với bình luận đã xóa. | Tên=Tài khoản tạm thời vô hiệu hoá hoặc [Người dùng đã xóa]; avatar mặc định; body và count=5 giữ nguyên | END:SUCCESS | FR-M01-13.03, FR-M01-13.04 |


<!-- sc:branch SC-M04-001 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | SYSTEM | Hệ thống trả luồng rỗng và số bình luận 0; không tạo bình luận hoặc dấu giả. | Gốc/trả lời hiển thị=[]; count=0 | END:SUCCESS | FR-M04-01.01, FR-M04-01.10, FR-M04-01.15, BR-M04-18 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest đọc luồng của bài công khai, thay toàn bộ đường chính. Actor khởi tạo ACT-001, kết quả END:SUCCESS; dùng hậu điều kiện tương ứng mục4.

<!-- sc:role-path SC-M04-001 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest mở bình luận P401 công khai. | P401 ngoài nhóm, Đã đăng/Bình thường/Không khóa; người xem được M03/M01 cho phép xem. Snapshot nhóm dùng G41 theo M11. Ngày minh họa 09/11/2026, múi giờ +07. | V1.2 | FR-M04-01.02 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền đọc rồi trả hai cấp, Top mặc định, trả lời cũ đến mới, trích dẫn hiện tại, nhãn nếu đã sửa và count chung. Không yêu cầu đăng nhập để đọc và không cho Guest viết/sửa/xóa. | C401 của Lan,09:00,5 upvote,body="Dùng định lý Pytago là ra. Cạnh huyền bằng 5 vì 3² + 4² = 25"; C402 của Minh,09:10,2 upvote; C403 của Hà,09:20,5 upvote; cả ba là gốc, Bình thường, chưa xóa; R411 của Minh,10:00,7 upvote,root=C401,target=C401,body="Mình đã tính được cạnh huyền bằng 5"; R412 của Hà,10:05,0 upvote,root=C401,target=R411,body="Mình cũng ra kết quả đó"; cả hai Bình thường, cùng cấp hai; Top:C401,C403,C402; Mới nhất:C403,C402,C401; Cũ nhất:C401,C402,C403. Trong C401 luôn R411 rồi R412. Tổng bình luận bình thường=5, không cộng thêm dòng trích dẫn. | END:SUCCESS | FR-M04-01.01, FR-M04-01.03, FR-M04-01.05, FR-M04-01.06, FR-M04-01.10, FR-M04-01.13, FR-M04-01.14, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04, BR-M04-05, BR-M04-06, BR-M04-07, BR-M04-17, BR-M04-18, FR-M04-01.02, BR-M04-16 |


**V2 — thay toàn bộ M1 đến kết thúc:** Guest đọc rồi chọn Mới nhất. Actor khởi tạo ACT-001, kết quả END:SUCCESS; dùng hậu điều kiện tương ứng mục4.

<!-- sc:role-path SC-M04-001 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-001 | Guest mở luồng bình luận P401 công khai. | P401 ngoài nhóm, Đã đăng/Bình thường/Không khóa; người xem được M03/M01 cho phép xem. Snapshot nhóm dùng G41 theo M11. Ngày minh họa 09/11/2026, múi giờ +07. | V2.2 | FR-M04-01.02 |
| V2.2 | SYSTEM | Hệ thống trả luồng Top mặc định và count5. | Top:C401,C403,C402; Mới nhất:C403,C402,C401; Cũ nhất:C401,C402,C403. Trong C401 luôn R411 rồi R412. Tổng bình luận bình thường=5, không cộng thêm dòng trích dẫn. | V2.3 | FR-M04-01.01, FR-M04-01.03, FR-M04-01.05, FR-M04-01.06, FR-M04-01.10, FR-M04-01.13, FR-M04-01.14, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04, BR-M04-05, BR-M04-06, BR-M04-07, BR-M04-17, BR-M04-18 |
| V2.3 | ACT-001 | Guest chọn Mới nhất. | Chỉ thay cách sắp xếp gốc | V2.4 | FR-M04-01.04 |
| V2.4 | SYSTEM | Hệ thống kiểm quyền và trả thứ tự gốc theo lựa chọn, giữ R411 rồi R412 và count5. | Gốc=C403,C402,C401; trả lời vẫn cũ→mới | END:SUCCESS | FR-M04-01.04, FR-M04-01.05, FR-M04-01.10, FR-M04-01.14, BR-M04-05, BR-M04-06, BR-M04-18 |


**V3 — thay toàn bộ M1 đến kết thúc:** Guest đọc rồi chọn Cũ nhất. Actor khởi tạo ACT-001, kết quả END:SUCCESS; dùng hậu điều kiện tương ứng mục4.

<!-- sc:role-path SC-M04-001 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-001 | Guest mở luồng bình luận P401 công khai. | P401 ngoài nhóm, Đã đăng/Bình thường/Không khóa; người xem được M03/M01 cho phép xem. Snapshot nhóm dùng G41 theo M11. Ngày minh họa 09/11/2026, múi giờ +07. | V3.2 | FR-M04-01.02 |
| V3.2 | SYSTEM | Hệ thống trả luồng Top mặc định và count5. | Top:C401,C403,C402; Mới nhất:C403,C402,C401; Cũ nhất:C401,C402,C403. Trong C401 luôn R411 rồi R412. Tổng bình luận bình thường=5, không cộng thêm dòng trích dẫn. | V3.3 | FR-M04-01.01, FR-M04-01.03, FR-M04-01.05, FR-M04-01.06, FR-M04-01.10, FR-M04-01.13, FR-M04-01.14, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04, BR-M04-05, BR-M04-06, BR-M04-07, BR-M04-17, BR-M04-18 |
| V3.3 | ACT-001 | Guest chọn Cũ nhất. | Chỉ thay cách sắp xếp gốc | V3.4 | FR-M04-01.04 |
| V3.4 | SYSTEM | Hệ thống kiểm quyền và trả thứ tự gốc theo lựa chọn, giữ R411 rồi R412 và count5. | Gốc=C401,C402,C403; trả lời vẫn cũ→mới | END:SUCCESS | FR-M04-01.04, FR-M04-01.05, FR-M04-01.10, FR-M04-01.14, BR-M04-05, BR-M04-06, BR-M04-18 |


**V4 — thay toàn bộ M1 đến kết thúc:** Guest đọc rồi chọn Top. Actor khởi tạo ACT-001, kết quả END:SUCCESS; dùng hậu điều kiện tương ứng mục4.

<!-- sc:role-path SC-M04-001 V4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V4.1 | ACT-001 | Guest mở luồng bình luận P401 công khai. | P401 ngoài nhóm, Đã đăng/Bình thường/Không khóa; người xem được M03/M01 cho phép xem. Snapshot nhóm dùng G41 theo M11. Ngày minh họa 09/11/2026, múi giờ +07. | V4.2 | FR-M04-01.02 |
| V4.2 | SYSTEM | Hệ thống trả luồng Top mặc định và count5. | Top:C401,C403,C402; Mới nhất:C403,C402,C401; Cũ nhất:C401,C402,C403. Trong C401 luôn R411 rồi R412. Tổng bình luận bình thường=5, không cộng thêm dòng trích dẫn. | V4.3 | FR-M04-01.01, FR-M04-01.03, FR-M04-01.05, FR-M04-01.06, FR-M04-01.10, FR-M04-01.13, FR-M04-01.14, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04, BR-M04-05, BR-M04-06, BR-M04-07, BR-M04-17, BR-M04-18 |
| V4.3 | ACT-001 | Guest chọn Top. | Chỉ thay cách sắp xếp gốc | V4.4 | FR-M04-01.04 |
| V4.4 | SYSTEM | Hệ thống kiểm quyền và trả thứ tự gốc theo lựa chọn, giữ R411 rồi R412 và count5. | Gốc=C401,C403,C402; trả lời vẫn cũ→mới | END:SUCCESS | FR-M04-01.04, FR-M04-01.05, FR-M04-01.10, FR-M04-01.14, BR-M04-05, BR-M04-06, BR-M04-18 |


**V5 — thay toàn bộ M1 đến kết thúc:** Guest không có quyền đọc bài đích. Actor khởi tạo ACT-001, kết quả END:REJECTED; dùng hậu điều kiện tương ứng mục4.

<!-- sc:role-path SC-M04-001 V5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V5.1 | ACT-001 | Guest yêu cầu xem luồng P401. | G41 Private, Guest ngoài nhóm; hoặc bài không còn hiển thị | V5.2 | FR-M04-01.11 |
| V5.2 | SYSTEM | Hệ thống không trả bình luận vì không được xem bài; không dùng URL bình luận để lách quyền. | Không lộ body/luồng | END:REJECTED | FR-M04-01.11, BR-M04-17, FR-M11-03.06 |


**V6 — thay toàn bộ M1 đến kết thúc:** Mod/Admin đọc luồng có gốc Bị ẩn, không phải đang xử lý vụ việc. Actor khởi tạo ACT-003, kết quả END:SUCCESS; dùng hậu điều kiện tương ứng mục4.

<!-- sc:role-path SC-M04-001 V6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V6.1 | ACT-003 | Mod mở luồng bình luận P401 được phép đọc. | C401 Bị ẩn, R411/R412 bình thường; không dùng đường M08/M09 | V6.2 | FR-M04-01.09 |
| V6.2 | SYSTEM | Hệ thống không trả body C401 kể cả cho Mod/Admin; giữ dấu gốc và hai trả lời, trích R411 thành trả lời [bình luận đã bị xóa]. | C401 chỉ [Bình luận đã bị xóa]; count=4, không tính dấu | END:SUCCESS | FR-M04-01.07, FR-M04-01.08, FR-M04-01.09, FR-M04-01.10, BR-M04-13, BR-M04-18 |


<!-- sc:end SC-M04-001 -->

<a id="sc-m04-002"></a>

<!-- sc:scenario SC-M04-002 -->

### SC-M04-002

#### 1. Tên kịch bản chuẩn

Viết và gửi bình luận gốc dưới bài — BF-M04-002. UC owner: [UC-M04-002](../../us/US-M04.md#uc-m04-002). Trigger: Lan chọn viết bình luận gốc dưới P401.

#### 2. Actor thực hiện

ACT-002 — User có phiên là actor chính. ACT-003 kế thừa tương tác User theo US, không có đặc quyền sửa/xóa/xem lại của tác giả đối với người khác. Actor khởi tạo thay thế được ghi tại đường V trong mục6. Không có actor AI hoặc dịch vụ nội bộ.

#### 3. Tiền điều kiện

Có ngữ cảnh bài; phiên/quyền xem/khóa/HEAVY được kiểm trong luồng, không giả định bài luôn mở tương tác. Đường chuẩn Lan có phiên hợp lệ, mức LIGHT/MEDIUM, P401 đang được phép xem và Không khóa.

#### 4. Hậu điều kiện

<!-- sc:post SC-M04-002 -->

| result | condition |
|---|---|
| SUCCESS | Đúng một bình luận gốc mới được lưu và hiện ngay Bình thường, tác giả/mốc đúng; không đợi AI hoặc tự gửi thông báo ngoài contract M01/M07. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi kết quả gửi/sửa/xóa thành công trái điều kiện. Dữ liệu trước yêu cầu giữ nguyên trừ hiệu ứng được nêu rõ trong nhánh. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M04-002 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan chọn viết bình luận gốc dưới P401. | P401 ngoài nhóm, Đã đăng/Bình thường/Không khóa; người xem được M03/M01 cho phép xem. Snapshot nhóm dùng G41 theo M11. Ngày minh họa 09/11/2026, múi giờ +07. | M2 | FR-M04-02.01 |
| M2 | SYSTEM | Hệ thống kiểm phiên/quyền bài, cung cấp trình soạn tối giản UC007, không đính kèm và không tạo dòng trích dẫn đích trả lời. | Đậm, nghiêng, code trong dòng, LaTeX, liên kết, nhắc tên, trích dẫn; không H1/bảng/checklist/tệp. Dòng trích dẫn tự động không thuộc thân trả lời; khối trích dẫn tác giả tự gõ vẫn tính vào giới hạn. | M3 | FR-M04-02.03, FR-M04-02.04, BR-M04-01, BR-M04-02 |
| M3 | ACT-002 | Lan nhập nội dung ngắn có công thức rồi gửi. | body="Ta có 3² + 4² = 25"; không có target_comment_id | M4 | FR-M04-02.01, BR-M04-19 |
| M4 | SYSTEM | Hệ thống kiểm lại phiên, bài tồn tại/hiển thị, khóa, cảnh cáo và nội dung không trống ≤1000 từ; lưu C404 gắn trực tiếp P401 với Lan và thời điểm gửi, Bình thường, chưa xóa. Hiển thị ngay không quét trước, cập nhật số đếm và cung cấp sự kiện gốc mới cho module nhận. | C404 root, author=U-LAN, created09/11 11:00, Bình thường; count5→6; không có dòng trích dẫn hệ thống | END:SUCCESS | FR-M04-02.01, FR-M04-02.02, FR-M04-02.05, FR-M04-02.06, FR-M04-02.07, FR-M04-02.08, FR-M04-02.10, FR-M04-02.11, FR-M04-01.10, BR-M04-12, BR-M04-14, BR-M04-15, BR-M04-18, BR-M04-19 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Guard chỉ bộ dữ liệu/ngữ cảnh thay thế cho lần thực thi: thay cả tên người/ID đối tượng minh họa khi được nêu, vẫn cùng vai trò actor; không gửi đồng thời bộ chuẩn và bộ lỗi. Các đường sửa quay lại bước kiểm cụ thể; nếu còn sai áp lại cùng guard, không tự giới hạn lần. REJECTED là kết thúc hợp lệ theo US, không bịa nút OK/hủy/thử lại ngoài nguồn.

<!-- sc:exceptions SC-M04-002 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Bài Khóa bình luận hoặc Khóa toàn bộ | E1.1 | FR-M04-02.06, BR-M04-14 |
| E2 | system | M2 | Người gửi ở mức cảnh cáo HEAVY | E2.1 | FR-M04-02.07, BR-M04-15 |
| E3 | system | M2 | Bài không tồn tại hoặc không hiển thị với actor | E3.1 | FR-M04-02.08, BR-M04-17 |
| E4 | system | M2 | Quyền nhóm không cho bình luận: Private ngoài nhóm hoặc nhóm Bị khóa | E4.1 | FR-M11-03.07, FR-M11-16.04 |
| E5 | system | M4 | Bài Khóa bình luận hoặc Khóa toàn bộ | E5.1 | FR-M04-02.06, BR-M04-14 |
| E6 | system | M4 | Người gửi ở mức cảnh cáo HEAVY | E6.1 | FR-M04-02.07, BR-M04-15 |
| E7 | system | M4 | Bài không tồn tại hoặc không hiển thị với actor | E7.1 | FR-M04-02.08, BR-M04-17 |
| E8 | system | M4 | Quyền nhóm không cho bình luận: Private ngoài nhóm hoặc nhóm Bị khóa | E8.1 | FR-M11-03.07, FR-M11-16.04 |
| E9 | system | M4 | Nội dung gửi trống hoặc chỉ khoảng trắng | E9.1 | FR-M04-02.11, BR-M04-19 |
| E10 | user-choice | M3 | Trong lúc soạn vượt1000 từ, người gửi thử gửi rồi sửa | E10.1 | FR-M04-02.09, FR-M04-02.10, BR-M04-19 |
| E11 | system | M4 | Actor LIGHT/MEDIUM hoặc người ngoài nhóm Public có phiên, các điều kiện khác hợp lệ | E11.1 | FR-M04-02.01, FR-M04-02.02, BR-M04-12, BR-M04-15, FR-M11-03.13 |


<!-- sc:branch SC-M04-002 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối bình luận mới, kể cả Mod/Admin hay tác giả bài; giữ bình luận đã có. | P401 khóa một trong hai mức | END:REJECTED | FR-M04-02.06, BR-M04-14 |


<!-- sc:branch SC-M04-002 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối tạo bình luận/trả lời mới, không đồng nhất với chặn sửa/xóa bình luận cũ. | Actor HEAVY; các điều kiện khác có thể vẫn đạt | END:REJECTED | FR-M04-02.07, BR-M04-15 |


<!-- sc:branch SC-M04-002 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối gửi, không dùng URL/đích bình luận để vượt quyền bài. | P401 bị ẩn, bị xóa hoặc actor không có quyền xem | END:REJECTED | FR-M04-02.08, BR-M04-17 |


<!-- sc:branch SC-M04-002 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối tạo gốc/trả lời theo M11; không coi có phiên hay Owner/Group Mod là miễn điều kiện nhóm. | G41 Private actor ngoài nhóm; hoặc nhóm Bị khóa | END:REJECTED | FR-M11-03.07, FR-M11-16.04 |


<!-- sc:branch SC-M04-002 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối bình luận mới, kể cả Mod/Admin hay tác giả bài; giữ bình luận đã có. | P401 khóa một trong hai mức | END:REJECTED | FR-M04-02.06, BR-M04-14 |


<!-- sc:branch SC-M04-002 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối tạo bình luận/trả lời mới, không đồng nhất với chặn sửa/xóa bình luận cũ. | Actor HEAVY; các điều kiện khác có thể vẫn đạt | END:REJECTED | FR-M04-02.07, BR-M04-15 |


<!-- sc:branch SC-M04-002 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối gửi, không dùng URL/đích bình luận để vượt quyền bài. | P401 bị ẩn, bị xóa hoặc actor không có quyền xem | END:REJECTED | FR-M04-02.08, BR-M04-17 |


<!-- sc:branch SC-M04-002 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống từ chối tạo gốc/trả lời theo M11; không coi có phiên hay Owner/Group Mod là miễn điều kiện nhóm. | G41 Private actor ngoài nhóm; hoặc nhóm Bị khóa | END:REJECTED | FR-M11-03.07, FR-M11-16.04 |


<!-- sc:branch SC-M04-002 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống từ chối nội dung trống/chỉ khoảng trắng; cho nhập lại trong UC007. | body="" hoặc "   "; không tạo bình luận | E9.2 | FR-M04-02.11, BR-M04-19 |
| E9.2 | ACT-002 | Người gửi nhập nội dung hợp lệ và gửi lại đúng đích trước đó. | body="Mình đã kiểm tra kết quả"; bình luận gốc P401 | M4 | FR-M04-02.11, BR-M04-19 |


<!-- sc:branch SC-M04-002 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | ACT-002 | Người gửi nhập1001 từ vào thân bình luận. | body=chuỗi "từ" lặp1001 lần, cách nhau bởi khoảng trắng; không tính dòng trích hệ thống của trả lời | E10.2 | FR-M04-02.09, FR-M04-02.10, BR-M04-19 |
| E10.2 | SYSTEM | Hệ thống cảnh báo ngay kèm1001/1000. | Nội dung vẫn trong trình soạn | E10.3 | FR-M04-02.09, FR-M04-02.10, BR-M04-19 |
| E10.3 | ACT-002 | Người gửi thử gửi khi vẫn vượt giới hạn. | Giữ đúng body1001 từ và đích của hành trình | E10.4 | FR-M04-02.09, FR-M04-02.10, BR-M04-19 |
| E10.4 | SYSTEM | Hệ thống từ chối gửi, giữ nguyên nội dung đang soạn. | Không tạo bình luận từ lần bị từ chối | E10.5 | FR-M04-02.09, FR-M04-02.10, BR-M04-19 |
| E10.5 | ACT-002 | Người gửi rút gọn về1000 từ và gửi lại. | body=chuỗi "từ" lặp1000 lần; đích giữ nguyên | M4 | FR-M04-02.09, FR-M04-02.10, BR-M04-19 |


<!-- sc:branch SC-M04-002 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | SYSTEM | Hệ thống áp điều kiện chung, lưu/hiển thị ngay bình luận hợp lệ, không từ chối chỉ vì MEDIUM hoặc không là thành viên nhóm Public. | body hợp lệ; C404 gốc P401; count5→6; actor LIGHT/MEDIUM, G41 Public nếu có | END:SUCCESS | FR-M04-02.01, FR-M04-02.02, BR-M04-12, BR-M04-15, FR-M11-03.13 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này, thay toàn bộ đường chính. Actor khởi tạo ACT-001, kết quả END:REJECTED; dùng hậu điều kiện tương ứng mục4.

<!-- sc:role-path SC-M04-002 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu viết và gửi bình luận gốc dưới bài. | Không có phiên xác định tác giả/người thao tác | V1.2 | FR-M04-02.05, BR-M04-16 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác chưa đăng nhập; không tự chạy chức năng đăng nhập, không thay đổi hoặc cung cấp nội dung bình luận riêng tư. | Yêu cầu hiện tại kết thúc, chưa thành công | END:REJECTED | FR-M04-02.05, BR-M04-16 |


<!-- sc:end SC-M04-002 -->

<a id="sc-m04-003"></a>

<!-- sc:scenario SC-M04-003 -->

### SC-M04-003

#### 1. Tên kịch bản chuẩn

Trả lời bình luận trong luồng hai cấp — BF-M04-003. UC owner: [UC-M04-003](../../us/US-M04.md#uc-m04-003). Trigger: Hà bấm Trả lời trên C401 của Lan.

#### 2. Actor thực hiện

ACT-002 — User có phiên là actor chính. ACT-003 kế thừa tương tác User theo US, không có đặc quyền sửa/xóa/xem lại của tác giả đối với người khác. Actor khởi tạo thay thế được ghi tại đường V trong mục6. Không có actor AI hoặc dịch vụ nội bộ.

#### 3. Tiền điều kiện

Có bài và bình luận đích; kiểm phiên/quyền bài/khóa/HEAVY và trạng thái đích khi mở và gửi. Đường chuẩn Hà có phiên, đích C401 đang Bình thường/chưa xóa; P401 cho phép bình luận.

#### 4. Hậu điều kiện

<!-- sc:post SC-M04-003 -->

| result | condition |
|---|---|
| SUCCESS | Trả lời mới hiển thị ngay đúng root và target, chỉ cấp hai; trích dẫn không thuộc body/độ dài, trạng thái Bình thường. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi kết quả gửi/sửa/xóa thành công trái điều kiện. Dữ liệu trước yêu cầu giữ nguyên trừ hiệu ứng được nêu rõ trong nhánh. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M04-003 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Hà bấm Trả lời trên C401 của Lan. | root=C401, target=C401; P401 ngoài nhóm, Đã đăng/Bình thường/Không khóa; người xem được M03/M01 cho phép xem. Snapshot nhóm dùng G41 theo M11. Ngày minh họa 09/11/2026, múi giờ +07. | M2 | FR-M04-03.01 |
| M2 | SYSTEM | Hệ thống kiểm đích bình thường và quyền, mở trình soạn UC007 cùng các định dạng tối giản; ghi target=C401 và root=C401. Dòng trích dẫn hệ thống chỉ để hiển thị, không chép vào thân trả lời. | Đậm, nghiêng, code trong dòng, LaTeX, liên kết, nhắc tên, trích dẫn; không H1/bảng/checklist/tệp. Dòng trích dẫn tự động không thuộc thân trả lời; khối trích dẫn tác giả tự gõ vẫn tính vào giới hạn.; trích Lan + phần đầu body C401 vừa một dòng | M3 | FR-M04-03.01, FR-M04-03.05, FR-M04-03.13, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04 |
| M3 | ACT-002 | Hà nhập nội dung trả lời và gửi. | body="Mình đồng ý với cách giải này"; target=C401; root=C401 | M4 | FR-M04-03.02 |
| M4 | SYSTEM | Hệ thống kiểm lại phiên/quyền/khóa/HEAVY, đích chưa xóa/không ẩn, nội dung không trống ≤1000 từ không gồm trích dẫn hệ thống; lưu R413 vào luồng C401 với đích C401, tác giả Hà và mốc gửi. Hiển thị ngay Bình thường ở cấp hai, sau R411/R412 theo thời điểm; dựng trích dẫn hiện tại và cập nhật số đếm. | R413 author=U-HA,created09/11 11:00,root=C401,target=C401; count5→6; không tạo cấp ba | END:SUCCESS | FR-M04-03.02, FR-M04-03.04, FR-M04-03.06, FR-M04-03.07, FR-M04-03.08, FR-M04-03.09, FR-M04-03.10, FR-M04-03.12, FR-M04-03.13, FR-M04-01.05, FR-M04-01.10, FR-M04-01.16, FR-M04-01.17, BR-M04-03, BR-M04-04, BR-M04-06, BR-M04-12, BR-M04-14, BR-M04-15, BR-M04-18, BR-M04-19 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Guard chỉ bộ dữ liệu/ngữ cảnh thay thế cho lần thực thi: thay cả tên người/ID đối tượng minh họa khi được nêu, vẫn cùng vai trò actor; không gửi đồng thời bộ chuẩn và bộ lỗi. Các đường sửa quay lại bước kiểm cụ thể; nếu còn sai áp lại cùng guard, không tự giới hạn lần. REJECTED là kết thúc hợp lệ theo US, không bịa nút OK/hủy/thử lại ngoài nguồn.

<!-- sc:exceptions SC-M04-003 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Hà chọn trả lời R411 thay vì chọn gốc | E1.1 | FR-M04-03.01, FR-M04-03.03, FR-M04-03.11, FR-M04-03.13, BR-M04-03, BR-M04-04, FR-M04-03.04, FR-M04-01.05, FR-M04-01.10, FR-M04-01.16, BR-M04-18 |
| E2 | user-choice | M1 | Hà chọn trả lời R411 khi gốc C401 đang hiện dấu đã xóa/Bị ẩn | E2.1 | FR-M04-03.01, FR-M04-03.03, FR-M04-03.11, FR-M04-03.13, BR-M04-03, BR-M04-04, FR-M04-03.04, FR-M04-01.05, FR-M04-01.10, FR-M04-01.16, BR-M04-18 |
| E3 | system | M2 | Đích được chọn đã xóa hoặc Bị ẩn, kể cả gốc đang là dấu thay thế | E3.1 | FR-M04-03.10 |
| E4 | system | M4 | Đích được chọn đã xóa hoặc Bị ẩn, kể cả gốc đang là dấu thay thế | E4.1 | FR-M04-03.10 |
| E5 | system | M2 | Bài Khóa bình luận hoặc Khóa toàn bộ | E5.1 | FR-M04-03.07, BR-M04-14 |
| E6 | system | M2 | Người gửi ở mức cảnh cáo HEAVY | E6.1 | FR-M04-03.08, BR-M04-15 |
| E7 | system | M2 | Bài không tồn tại hoặc không hiển thị với actor | E7.1 | FR-M04-03.09, BR-M04-17 |
| E8 | system | M2 | Quyền nhóm không cho bình luận: Private ngoài nhóm hoặc nhóm Bị khóa | E8.1 | FR-M11-03.07, FR-M11-16.04 |
| E9 | system | M4 | Bài Khóa bình luận hoặc Khóa toàn bộ | E9.1 | FR-M04-03.07, BR-M04-14 |
| E10 | system | M4 | Người gửi ở mức cảnh cáo HEAVY | E10.1 | FR-M04-03.08, BR-M04-15 |
| E11 | system | M4 | Bài không tồn tại hoặc không hiển thị với actor | E11.1 | FR-M04-03.09, BR-M04-17 |
| E12 | system | M4 | Quyền nhóm không cho bình luận: Private ngoài nhóm hoặc nhóm Bị khóa | E12.1 | FR-M11-03.07, FR-M11-16.04 |
| E13 | system | M4 | Nội dung gửi trống hoặc chỉ khoảng trắng | E13.1 | FR-M04-03.12, BR-M04-19 |
| E14 | user-choice | M3 | Trong lúc soạn vượt1000 từ, người gửi thử gửi rồi sửa | E14.1 | FR-M04-03.12, FR-M04-03.13, FR-M04-02.09, FR-M04-02.10, FR-M04-02.11, BR-M04-19 |
| E15 | system | M4 | Actor LIGHT/MEDIUM hoặc người ngoài nhóm Public có phiên, các điều kiện khác hợp lệ | E15.1 | FR-M04-03.02, FR-M04-03.04, BR-M04-12, BR-M04-15, FR-M11-03.13 |
| E16 | system | M4 | Thân trả lời1000 từ nhưng bình luận được trích rất dài | E16.1 | FR-M04-03.02, FR-M04-03.04, FR-M04-03.12, FR-M04-03.13, FR-M04-01.16, FR-M04-01.17, BR-M04-04, BR-M04-19 |
| E17 | user-choice | M3 | Khối trích dẫn người gửi tự gõ làm tổng thân trả lời vượt giới hạn | E17.1 | BR-M04-19, FR-M04-03.12, FR-M04-03.13 |


<!-- sc:branch SC-M04-003 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Hà bấm Trả lời trên R411 còn hiển thị bình thường. | R411.root=C401; R411 Bình thường; C401 Bình thường | E1.2 | FR-M04-03.01 |
| E1.2 | SYSTEM | Hệ thống mở trình soạn, giữ đích R411 nhưng root=C401; dòng trích dùng tên Minh và body R411, không gồm dòng trích C401 mà R411 hiển thị. | Đậm, nghiêng, code trong dòng, LaTeX, liên kết, nhắc tên, trích dẫn; không H1/bảng/checklist/tệp. Dòng trích dẫn tự động không thuộc thân trả lời; khối trích dẫn tác giả tự gõ vẫn tính vào giới hạn.; không dựng cấp thứba | E1.3 | FR-M04-03.01, FR-M04-03.03, FR-M04-03.11, FR-M04-03.13, BR-M04-03, BR-M04-04 |
| E1.3 | ACT-002 | Hà nhập nội dung hợp lệ và gửi trả lời R411. | body="Mình kiểm tra cũng ra 5"; target=R411; root=C401 | E1.4 | FR-M04-03.03 |
| E1.4 | SYSTEM | Hệ thống kiểm lại điều kiện và đích R411, lưu R413 cùng cấp với R411/R412 dưới C401; hiện ngay và trích body hiện tại R411. Gốc có dấu không cấm trả lời một trả lời còn bình thường. | R411,R412,R413 theo created; count=5→6; target=R411 không đổi thành C401 | END:SUCCESS | FR-M04-03.03, FR-M04-03.04, FR-M04-03.11, FR-M04-03.13, FR-M04-01.05, FR-M04-01.10, FR-M04-01.16, BR-M04-03, BR-M04-04, BR-M04-18 |


<!-- sc:branch SC-M04-003 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | Hà bấm Trả lời trên R411 còn hiển thị bình thường. | R411.root=C401; R411 Bình thường; C401 hiện dấu | E2.2 | FR-M04-03.01 |
| E2.2 | SYSTEM | Hệ thống mở trình soạn, giữ đích R411 nhưng root=C401; dòng trích dùng tên Minh và body R411, không gồm dòng trích C401 mà R411 hiển thị. | Đậm, nghiêng, code trong dòng, LaTeX, liên kết, nhắc tên, trích dẫn; không H1/bảng/checklist/tệp. Dòng trích dẫn tự động không thuộc thân trả lời; khối trích dẫn tác giả tự gõ vẫn tính vào giới hạn.; không dựng cấp thứba | E2.3 | FR-M04-03.01, FR-M04-03.03, FR-M04-03.11, FR-M04-03.13, BR-M04-03, BR-M04-04 |
| E2.3 | ACT-002 | Hà nhập nội dung hợp lệ và gửi trả lời R411. | body="Mình kiểm tra cũng ra 5"; target=R411; root=C401 | E2.4 | FR-M04-03.03 |
| E2.4 | SYSTEM | Hệ thống kiểm lại điều kiện và đích R411, lưu R413 cùng cấp với R411/R412 dưới C401; hiện ngay và trích body hiện tại R411. Gốc có dấu không cấm trả lời một trả lời còn bình thường. | R411,R412,R413 theo created; count=4→5; target=R411 không đổi thành C401 | END:SUCCESS | FR-M04-03.03, FR-M04-03.04, FR-M04-03.11, FR-M04-03.13, FR-M04-01.05, FR-M04-01.10, FR-M04-01.16, BR-M04-03, BR-M04-04, BR-M04-18 |


<!-- sc:branch SC-M04-003 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối trả lời trực tiếp đích này; không tạo trả lời mới hoặc tự chọn đích khác. | target=C401 hoặc R411 deleted=true/Bị ẩn; các trả lời khác có thể vẫn bình thường | END:REJECTED | FR-M04-03.10 |


<!-- sc:branch SC-M04-003 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối trả lời trực tiếp đích này; không tạo trả lời mới hoặc tự chọn đích khác. | target=C401 hoặc R411 deleted=true/Bị ẩn; các trả lời khác có thể vẫn bình thường | END:REJECTED | FR-M04-03.10 |


<!-- sc:branch SC-M04-003 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối bình luận mới, kể cả Mod/Admin hay tác giả bài; giữ bình luận đã có. | P401 khóa một trong hai mức | END:REJECTED | FR-M04-03.07, BR-M04-14 |


<!-- sc:branch SC-M04-003 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối tạo bình luận/trả lời mới, không đồng nhất với chặn sửa/xóa bình luận cũ. | Actor HEAVY; các điều kiện khác có thể vẫn đạt | END:REJECTED | FR-M04-03.08, BR-M04-15 |


<!-- sc:branch SC-M04-003 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối gửi, không dùng URL/đích bình luận để vượt quyền bài. | P401 bị ẩn, bị xóa hoặc actor không có quyền xem | END:REJECTED | FR-M04-03.09, BR-M04-17 |


<!-- sc:branch SC-M04-003 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống từ chối tạo gốc/trả lời theo M11; không coi có phiên hay Owner/Group Mod là miễn điều kiện nhóm. | G41 Private actor ngoài nhóm; hoặc nhóm Bị khóa | END:REJECTED | FR-M11-03.07, FR-M11-16.04 |


<!-- sc:branch SC-M04-003 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống từ chối bình luận mới, kể cả Mod/Admin hay tác giả bài; giữ bình luận đã có. | P401 khóa một trong hai mức | END:REJECTED | FR-M04-03.07, BR-M04-14 |


<!-- sc:branch SC-M04-003 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống từ chối tạo bình luận/trả lời mới, không đồng nhất với chặn sửa/xóa bình luận cũ. | Actor HEAVY; các điều kiện khác có thể vẫn đạt | END:REJECTED | FR-M04-03.08, BR-M04-15 |


<!-- sc:branch SC-M04-003 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | SYSTEM | Hệ thống từ chối gửi, không dùng URL/đích bình luận để vượt quyền bài. | P401 bị ẩn, bị xóa hoặc actor không có quyền xem | END:REJECTED | FR-M04-03.09, BR-M04-17 |


<!-- sc:branch SC-M04-003 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | SYSTEM | Hệ thống từ chối tạo gốc/trả lời theo M11; không coi có phiên hay Owner/Group Mod là miễn điều kiện nhóm. | G41 Private actor ngoài nhóm; hoặc nhóm Bị khóa | END:REJECTED | FR-M11-03.07, FR-M11-16.04 |


<!-- sc:branch SC-M04-003 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | SYSTEM | Hệ thống từ chối nội dung trống/chỉ khoảng trắng; cho nhập lại trong UC007. | body="" hoặc "   "; không tạo bình luận | E13.2 | FR-M04-03.12, BR-M04-19 |
| E13.2 | ACT-002 | Người gửi nhập nội dung hợp lệ và gửi lại đúng đích trước đó. | body="Mình đã kiểm tra kết quả"; target=C401,root=C401 | M4 | FR-M04-03.12, BR-M04-19 |


<!-- sc:branch SC-M04-003 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | ACT-002 | Người gửi nhập1001 từ vào thân bình luận. | body=chuỗi "từ" lặp1001 lần, cách nhau bởi khoảng trắng; không tính dòng trích hệ thống của trả lời | E14.2 | FR-M04-03.12, FR-M04-03.13, FR-M04-02.09, FR-M04-02.10, FR-M04-02.11, BR-M04-19 |
| E14.2 | SYSTEM | Hệ thống cảnh báo ngay kèm1001/1000. | Nội dung vẫn trong trình soạn | E14.3 | FR-M04-03.12, FR-M04-03.13, FR-M04-02.09, FR-M04-02.10, FR-M04-02.11, BR-M04-19 |
| E14.3 | ACT-002 | Người gửi thử gửi khi vẫn vượt giới hạn. | Giữ đúng body1001 từ và đích của hành trình | E14.4 | FR-M04-03.12, FR-M04-03.13, FR-M04-02.09, FR-M04-02.10, FR-M04-02.11, BR-M04-19 |
| E14.4 | SYSTEM | Hệ thống từ chối gửi, giữ nguyên nội dung đang soạn. | Không tạo bình luận từ lần bị từ chối | E14.5 | FR-M04-03.12, FR-M04-03.13, FR-M04-02.09, FR-M04-02.10, FR-M04-02.11, BR-M04-19 |
| E14.5 | ACT-002 | Người gửi rút gọn về1000 từ và gửi lại. | body=chuỗi "từ" lặp1000 lần; đích giữ nguyên | M4 | FR-M04-03.12, FR-M04-03.13, FR-M04-02.09, FR-M04-02.10, FR-M04-02.11, BR-M04-19 |


<!-- sc:branch SC-M04-003 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | SYSTEM | Hệ thống áp điều kiện chung, lưu/hiển thị ngay bình luận hợp lệ, không từ chối chỉ vì MEDIUM hoặc không là thành viên nhóm Public. | body hợp lệ; R413,root=C401,target=C401; count5→6; actor LIGHT/MEDIUM, G41 Public nếu có | END:SUCCESS | FR-M04-03.02, FR-M04-03.04, BR-M04-12, BR-M04-15, FR-M11-03.13 |


<!-- sc:branch SC-M04-003 E16 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E16.1 | SYSTEM | Hệ thống chỉ tính1000 từ người gửi viết, nhận trả lời hợp lệ; dòng trích tự động của đích không cộng vào thân. Hiển thị trích phần đầu vừa một dòng và lưu target/root, không lưu bản chép đích vào nội dung trả lời. | reply.body=1000 từ; target.body=900 từ; root=C401,target=C401; đích chưa xóa/không ẩn; R413 Bình thường | END:SUCCESS | FR-M04-03.02, FR-M04-03.04, FR-M04-03.12, FR-M04-03.13, FR-M04-01.16, FR-M04-01.17, BR-M04-04, BR-M04-19 |


<!-- sc:branch SC-M04-003 E17 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E17.1 | ACT-002 | Hà nhập900 từ trả lời và thêm khối trích dẫn tự gõ101 từ. | Tổng body=1001 từ; không phải dòng trích tự động | E17.2 | BR-M04-19 |
| E17.2 | SYSTEM | Hệ thống cảnh báo1001/1000, tính cả khối trích dẫn tự gõ. | Dòng trích tự động vẫn loại khỏi độ dài | E17.3 | FR-M04-03.12, FR-M04-03.13, BR-M04-19 |
| E17.3 | ACT-002 | Hà rút ngắn khối tự gõ về100 từ rồi gửi. | body tổng1000 từ; target=C401; root=C401 | M4 | BR-M04-19 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này, thay toàn bộ đường chính. Actor khởi tạo ACT-001, kết quả END:REJECTED; dùng hậu điều kiện tương ứng mục4.

<!-- sc:role-path SC-M04-003 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu trả lời bình luận trong luồng hai cấp. | Không có phiên xác định tác giả/người thao tác | V1.2 | FR-M04-03.06, BR-M04-16 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác chưa đăng nhập; không tự chạy chức năng đăng nhập, không thay đổi hoặc cung cấp nội dung bình luận riêng tư. | Yêu cầu hiện tại kết thúc, chưa thành công | END:REJECTED | FR-M04-03.06, BR-M04-16 |


<!-- sc:end SC-M04-003 -->

<a id="sc-m04-004"></a>

<!-- sc:scenario SC-M04-004 -->

### SC-M04-004

#### 1. Tên kịch bản chuẩn

Sửa nội dung bình luận của mình — BF-M04-004. UC owner: [UC-M04-004](../../us/US-M04.md#uc-m04-004). Trigger: Minh mở sửa R411 của mình.

#### 2. Actor thực hiện

ACT-002 — User có phiên là actor chính. ACT-003 kế thừa tương tác User theo US, không có đặc quyền sửa/xóa/xem lại của tác giả đối với người khác. Actor khởi tạo thay thế được ghi tại đường V trong mục6. Không có actor AI hoặc dịch vụ nội bộ.

#### 3. Tiền điều kiện

Có phiên hợp lệ; kiểm tác giả/quyền nhóm, cờ xóa, Bị ẩn và khóa bài khi mở/lưu. Đường chuẩn Minh sửa R411 của mình; không có giới hạn thời gian/số lần sửa. Không kế thừa quy tắc cho phép sửa bài bị khóa của M03.

#### 4. Hậu điều kiện

<!-- sc:post SC-M04-004 -->

| result | condition |
|---|---|
| SUCCESS | Nội dung mới hợp lệ được lưu, mốc sửa gần nhất và nhãn đúng; giữ mốc đăng/vị trí/kiểm duyệt, không có lịch sử hoặc quét trước/khôi phục nội dung cũ. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi kết quả gửi/sửa/xóa thành công trái điều kiện. Dữ liệu trước yêu cầu giữ nguyên trừ hiệu ứng được nêu rõ trong nhánh. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M04-004 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Minh mở sửa R411 của mình. | R411 author=U-MINH,created09/11 10:00,last_edit10:10,Bình thường,chưa xóa; P401 Không khóa | M2 | FR-M04-04.05 |
| M2 | SYSTEM | Hệ thống kiểm điều kiện sửa, trả nội dung hiện tại trong trình soạn UC007; cùng bộ định dạng tối giản, không tệp và không có lịch sử sửa. | body hiện tại=Mình đã tính được cạnh huyền bằng5; Đậm, nghiêng, code trong dòng, LaTeX, liên kết, nhắc tên, trích dẫn; không H1/bảng/checklist/tệp. Dòng trích dẫn tự động không thuộc thân trả lời; khối trích dẫn tác giả tự gõ vẫn tính vào giới hạn. | M3 | FR-M04-04.04, FR-M04-04.06, FR-M04-04.07, FR-M04-04.08, FR-M04-04.09, FR-M04-04.10, BR-M04-01, BR-M04-02, BR-M04-07, BR-M04-20 |
| M3 | ACT-002 | Minh sửa nội dung và chọn Lưu. | body mới="Mình đã kiểm tra lại kết quả"; thời điểm lưu09/11 11:00 | M4 | FR-M04-04.01 |
| M4 | SYSTEM | Hệ thống kiểm lại quyền/trạng thái và nội dung hợp lệ≤1000 từ; thay body, ghi thời điểm sửa gần nhất thay mốc cũ. Giữ thời điểm đăng, root/target/vị trí và kiểm duyệt; hiện (đã chỉnh sửa). Không lưu body cũ/phiên bản, không quét ngay chỉ vì sửa. Các trích dẫn tới R411 dùng body mới. | R411.created10:00 giữ nguyên,last_edit11:00; vẫn trước R412.created10:05; R412 trích Minh + body mới R411; count vẫn5 | END:SUCCESS | FR-M04-04.01, FR-M04-04.02, FR-M04-04.03, FR-M04-04.04, FR-M04-04.05, FR-M04-04.11, FR-M04-04.13, FR-M04-01.06, FR-M04-01.16, BR-M04-04, BR-M04-07, BR-M04-19, BR-M04-20, FR-M08-08.03 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Guard chỉ bộ dữ liệu/ngữ cảnh thay thế cho lần thực thi: thay cả tên người/ID đối tượng minh họa khi được nêu, vẫn cùng vai trò actor; không gửi đồng thời bộ chuẩn và bộ lỗi. Các đường sửa quay lại bước kiểm cụ thể; nếu còn sai áp lại cùng guard, không tự giới hạn lần. REJECTED là kết thúc hợp lệ theo US, không bịa nút OK/hủy/thử lại ngoài nguồn.

<!-- sc:exceptions SC-M04-004 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Người sửa khác tác giả | E1.1 | FR-M04-04.07 |
| E2 | system | M2 | Bình luận đã xóa | E2.1 | FR-M04-04.08 |
| E3 | system | M2 | Bình luận Bị ẩn | E3.1 | FR-M04-04.10 |
| E4 | system | M2 | Bài Khóa bình luận hoặc Khóa toàn bộ | E4.1 | FR-M04-04.09 |
| E5 | system | M2 | Đã rời/kick khỏi nhóm Private | E5.1 | FR-M11-10.09 |
| E6 | system | M4 | Người sửa khác tác giả | E6.1 | FR-M04-04.07 |
| E7 | system | M4 | Bình luận đã xóa | E7.1 | FR-M04-04.08 |
| E8 | system | M4 | Bình luận Bị ẩn | E8.1 | FR-M04-04.10 |
| E9 | system | M4 | Bài Khóa bình luận hoặc Khóa toàn bộ | E9.1 | FR-M04-04.09 |
| E10 | system | M4 | Đã rời/kick khỏi nhóm Private | E10.1 | FR-M11-10.09 |
| E11 | system | M4 | Tác giả HEAVY hoặc đã lâu/rất nhiều lần kể từ khi đăng, các điều kiện khác hợp lệ | E11.1 | FR-M04-04.01, FR-M04-04.02, FR-M04-04.03, FR-M04-04.04, FR-M04-04.05, FR-M04-04.11, BR-M04-07, BR-M04-20 |
| E12 | system | M4 | Nội dung sửa trống hoặc chỉ khoảng trắng | E12.1 | FR-M04-04.13 |
| E13 | user-choice | M3 | Body đang sửa vượt1000 từ | E13.1 | FR-M04-04.12, FR-M04-04.13 |
| E14 | system | M4 | Tác giả rời/kick khỏi nhóm Public nhưng điều kiện sửa khác hợp lệ | E14.1 | FR-M04-04.01, FR-M04-04.02, FR-M04-04.03, BR-M04-07, FR-M11-10.08 |


<!-- sc:branch SC-M04-004 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối sửa, không cập nhật body hoặc mốc sửa từ yêu cầu bị từ chối. | Lan sửa R411 của Minh | END:REJECTED | FR-M04-04.07 |


<!-- sc:branch SC-M04-004 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối sửa, không cập nhật body hoặc mốc sửa từ yêu cầu bị từ chối. | R411.deleted=true | END:REJECTED | FR-M04-04.08 |


<!-- sc:branch SC-M04-004 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối sửa, không cập nhật body hoặc mốc sửa từ yêu cầu bị từ chối. | R411.Bị ẩn | END:REJECTED | FR-M04-04.10 |


<!-- sc:branch SC-M04-004 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối sửa, không cập nhật body hoặc mốc sửa từ yêu cầu bị từ chối. | P401 khóa, kể cả chính tác giả/Mod/Admin sửa | END:REJECTED | FR-M04-04.09 |


<!-- sc:branch SC-M04-004 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối sửa, không cập nhật body hoặc mốc sửa từ yêu cầu bị từ chối. | R411 thuộc G41 Private; Minh không còn thành viên | END:REJECTED | FR-M11-10.09 |


<!-- sc:branch SC-M04-004 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối sửa, không cập nhật body hoặc mốc sửa từ yêu cầu bị từ chối. | Lan sửa R411 của Minh | END:REJECTED | FR-M04-04.07 |


<!-- sc:branch SC-M04-004 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối sửa, không cập nhật body hoặc mốc sửa từ yêu cầu bị từ chối. | R411.deleted=true | END:REJECTED | FR-M04-04.08 |


<!-- sc:branch SC-M04-004 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống từ chối sửa, không cập nhật body hoặc mốc sửa từ yêu cầu bị từ chối. | R411.Bị ẩn | END:REJECTED | FR-M04-04.10 |


<!-- sc:branch SC-M04-004 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống từ chối sửa, không cập nhật body hoặc mốc sửa từ yêu cầu bị từ chối. | P401 khóa, kể cả chính tác giả/Mod/Admin sửa | END:REJECTED | FR-M04-04.09 |


<!-- sc:branch SC-M04-004 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống từ chối sửa, không cập nhật body hoặc mốc sửa từ yêu cầu bị từ chối. | R411 thuộc G41 Private; Minh không còn thành viên | END:REJECTED | FR-M11-10.09 |


<!-- sc:branch SC-M04-004 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | SYSTEM | Hệ thống vẫn lưu bản sửa hợp lệ; HEAVY chỉ chặn tạo mới. Giữ mốc đăng/vị trí/kiểm duyệt, cập nhật mốc sửa gần nhất và nhãn; không thêm giới hạn thời gian/lần sửa. | R411 tạo01/10 09:00; sửa09/11 11:00; author HEAVY; body mới hợp lệ; P401 Không khóa | END:SUCCESS | FR-M04-04.01, FR-M04-04.02, FR-M04-04.03, FR-M04-04.04, FR-M04-04.05, FR-M04-04.11, BR-M04-07, BR-M04-20 |


<!-- sc:branch SC-M04-004 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | SYSTEM | Hệ thống từ chối lưu, giữ nguyên nội dung trong trình soạn cho tác giả sửa lại. | body sửa="" hoặc "   "; body đã lưu chưa thay | E12.2 | FR-M04-04.13 |
| E12.2 | ACT-002 | Minh nhập body hợp lệ rồi chọn Lưu lại. | body=Mình đã kiểm tra lại kết quả | M4 | FR-M04-04.13 |


<!-- sc:branch SC-M04-004 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | ACT-002 | Minh nhập1001 từ vào bản đang sửa. | body="từ" lặp1001 lần | E13.2 | FR-M04-04.12 |
| E13.2 | SYSTEM | Hệ thống cảnh báo ngay1001/1000. | Giữ body đang sửa | E13.3 | FR-M04-04.12 |
| E13.3 | ACT-002 | Minh chọn Lưu khi body vẫn1001 từ. | Không thay dữ liệu lỗi bằng bộ chuẩn | E13.4 | FR-M04-04.13 |
| E13.4 | SYSTEM | Hệ thống từ chối lưu và giữ nguyên bản đang sửa; không ghi mốc sửa thành công. | Body lưu trước đó chưa thay; body1001 vẫn trong soạn | E13.5 | FR-M04-04.13 |
| E13.5 | ACT-002 | Minh rút gọn về1000 từ rồi gửi lưu lại. | body="từ" lặp1000 lần | M4 | FR-M04-04.13 |


<!-- sc:branch SC-M04-004 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | SYSTEM | Hệ thống cho tác giả sửa như bình luận ngoài nhóm, lưu nội dung/mốc sửa và nhãn, không xóa lịch sử không tồn tại hoặc đổi vị trí. | G41 Public; R411 của Minh; P401 Không khóa; R411 Bình thường,chưa xóa | END:SUCCESS | FR-M04-04.01, FR-M04-04.02, FR-M04-04.03, BR-M04-07, FR-M11-10.08 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này, thay toàn bộ đường chính. Actor khởi tạo ACT-001, kết quả END:REJECTED; dùng hậu điều kiện tương ứng mục4.

<!-- sc:role-path SC-M04-004 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu sửa nội dung bình luận của mình. | Không có phiên xác định tác giả/người thao tác | V1.2 | BR-M04-16 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác chưa đăng nhập; không tự chạy chức năng đăng nhập, không thay đổi hoặc cung cấp nội dung bình luận riêng tư. | Yêu cầu hiện tại kết thúc, chưa thành công | END:REJECTED | BR-M04-16 |


**V2 — thay toàn bộ M1 đến kết thúc:** Mod/Admin thử thao tác này trên bình luận người khác qua M04. Actor khởi tạo ACT-003, kết quả END:REJECTED; dùng hậu điều kiện tương ứng mục4.

<!-- sc:role-path SC-M04-004 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-003 | Mod yêu cầu sửa nội dung bình luận của mình đối với C401 của Lan. | actor=U-MOD; comment.author=U-LAN | V2.2 | FR-M04-04.07 |
| V2.2 | SYSTEM | Hệ thống từ chối quyền sửa/xóa hoặc xem lại dành cho tác giả đối với bình luận người khác. Vai trò Mod/Admin không thay điều kiện chủ; xử lý ẩn/tra cứu vụ liên quan do M08/M09 cấp riêng. | Không đổi cờ/body, không lộ nội dung qua đường xem lại của tác giả | END:REJECTED | FR-M04-04.07 |


<!-- sc:end SC-M04-004 -->

<a id="sc-m04-005"></a>

<!-- sc:scenario SC-M04-005 -->

### SC-M04-005

#### 1. Tên kịch bản chuẩn

Xóa bình luận của mình khỏi luồng người dùng — BF-M04-005. UC owner: [UC-M04-005](../../us/US-M04.md#uc-m04-005). Trigger: Lan yêu cầu xóa bình luận gốc C401 của mình.

#### 2. Actor thực hiện

ACT-002 — User có phiên là actor chính. ACT-003 kế thừa tương tác User theo US, không có đặc quyền sửa/xóa/xem lại của tác giả đối với người khác. Actor khởi tạo thay thế được ghi tại đường V trong mục6. Không có actor AI hoặc dịch vụ nội bộ.

#### 3. Tiền điều kiện

Có phiên; kiểm chính tác giả, quyền nhóm, chưa xóa/không Bị ẩn. Bài khóa và HEAVY không tự ngăn xóa. Đường chuẩn Lan xóa gốc C401 có R411/R412 Bình thường.

#### 4. Hậu điều kiện

<!-- sc:post SC-M04-005 -->

| result | condition |
|---|---|
| SUCCESS | Cờ xóa được ghi, dữ liệu giữ; luồng/dấu/trích dẫn/số đếm đúng trường hợp; không xóa người khác, không khôi phục hoặc xóa hẳn bình luận. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi kết quả gửi/sửa/xóa thành công trái điều kiện. Dữ liệu trước yêu cầu giữ nguyên trừ hiệu ứng được nêu rõ trong nhánh. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M04-005 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan yêu cầu xóa bình luận gốc C401 của mình. | C401 của Lan,09:00,5 upvote,body="Dùng định lý Pytago là ra. Cạnh huyền bằng 5 vì 3² + 4² = 25"; C402 của Minh,09:10,2 upvote; C403 của Hà,09:20,5 upvote; cả ba là gốc, Bình thường, chưa xóa; R411 của Minh,10:00,7 upvote,root=C401,target=C401,body="Mình đã tính được cạnh huyền bằng 5"; R412 của Hà,10:05,0 upvote,root=C401,target=R411,body="Mình cũng ra kết quả đó"; cả hai Bình thường, cùng cấp hai | M2 | FR-M04-05.01 |
| M2 | SYSTEM | Hệ thống kiểm chủ/quyền và trạng thái, gắn cờ C401 đã xóa nhưng giữ nội dung; tại gốc hiện [Bình luận đã bị xóa], giữ R411/R412. R411 trích trả lời [bình luận đã bị xóa]; R412 vẫn trích R411. Cập nhật count không tính dấu, trả kết quả xóa với người dùng là vĩnh viễn, không có khôi phục. | C401.deleted=true; body C401 còn lưu; R411/R412 không xóa; count5→4; không có xóa vật lý/cascade | END:SUCCESS | FR-M04-05.01, FR-M04-05.04, FR-M04-05.05, FR-M04-05.06, FR-M04-05.07, FR-M04-01.07, FR-M04-01.08, FR-M04-01.10, BR-M04-08, BR-M04-18, BR-M04-21, BR-M04-23 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Guard chỉ bộ dữ liệu/ngữ cảnh thay thế cho lần thực thi: thay cả tên người/ID đối tượng minh họa khi được nêu, vẫn cùng vai trò actor; không gửi đồng thời bộ chuẩn và bộ lỗi. Các đường sửa quay lại bước kiểm cụ thể; nếu còn sai áp lại cùng guard, không tự giới hạn lần. REJECTED là kết thúc hợp lệ theo US, không bịa nút OK/hủy/thử lại ngoài nguồn.

<!-- sc:exceptions SC-M04-005 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Người xóa khác tác giả | E1.1 | FR-M04-05.05 |
| E2 | system | M2 | Bình luận đã xóa | E2.1 | FR-M04-05.06 |
| E3 | system | M2 | Bình luận đang Bị ẩn | E3.1 | FR-M04-05.10 |
| E4 | system | M2 | Đã rời/kick khỏi nhóm Private | E4.1 | FR-M11-10.09 |
| E5 | system | M2 | Gốc của tác giả không có trả lời nào hiển thị bình thường | E5.1 | FR-M04-05.02, FR-M04-05.04, FR-M04-05.07, FR-M04-01.15, BR-M04-08, BR-M04-18 |
| E6 | system | M2 | Tác giả xóa một trả lời có trả lời khác trỏ tới nó | E6.1 | FR-M04-05.03, FR-M04-05.04, FR-M04-05.07, FR-M04-01.08, FR-M04-01.10, BR-M04-08, BR-M04-18 |
| E7 | system | M2 | Trả lời cuối cùng đang bình thường bị tác giả xóa, gốc đã hiện dấu | E7.1 | FR-M04-05.03, FR-M04-05.07, FR-M04-01.15, BR-M04-08, BR-M04-18 |
| E8 | system | M2 | Bài đang khóa và/hoặc tác giả HEAVY, điều kiện xóa khác hợp lệ | E8.1 | FR-M04-05.01, FR-M04-05.07, FR-M04-05.08, FR-M04-05.09, BR-M04-08, BR-M04-20 |
| E9 | system | M2 | Tác giả rời/kick khỏi nhóm Public, các điều kiện xóa khác hợp lệ | E9.1 | FR-M04-05.01, FR-M04-05.07, BR-M04-08, FR-M11-10.08 |


<!-- sc:branch SC-M04-005 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối thao tác xóa của tác giả, không gắn cờ mới hoặc đổi dữ liệu vì yêu cầu này. | Minh xóa C401 của Lan | END:REJECTED | FR-M04-05.05 |


<!-- sc:branch SC-M04-005 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối thao tác xóa của tác giả, không gắn cờ mới hoặc đổi dữ liệu vì yêu cầu này. | C401.deleted=true trước yêu cầu | END:REJECTED | FR-M04-05.06 |


<!-- sc:branch SC-M04-005 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối thao tác xóa của tác giả, không gắn cờ mới hoặc đổi dữ liệu vì yêu cầu này. | C401.Bị ẩn, tác giả yêu cầu xóa | END:REJECTED | FR-M04-05.10 |


<!-- sc:branch SC-M04-005 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối thao tác xóa của tác giả, không gắn cờ mới hoặc đổi dữ liệu vì yêu cầu này. | C401 thuộc G41 Private, Lan không còn là thành viên | END:REJECTED | FR-M11-10.09 |


<!-- sc:branch SC-M04-005 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống kiểm điều kiện rồi gắn cờ xóa, giữ body, bỏ gốc khỏi luồng; không để dấu khi không có trả lời bình thường. Tính lại count, không xóa/cascade dữ liệu trả lời đang bị ẩn. | C403 không có trả lời bình thường; Hà là tác giả và yêu cầu xóa; count5→4; C401/R411/R412/C402 giữ nguyên | END:SUCCESS | FR-M04-05.02, FR-M04-05.04, FR-M04-05.07, FR-M04-01.15, BR-M04-08, BR-M04-18 |


<!-- sc:branch SC-M04-005 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống kiểm điều kiện, gắn cờ R411 xóa và bỏ R411 khỏi luồng, giữ R412/root; R412 hiển thị trả lời [bình luận đã bị xóa]. Trả kết quả xóa, không khôi phục. | Minh xóa R411; R412 vẫn cấp hai rootC401; body R411 giữ; count5→4 | END:SUCCESS | FR-M04-05.03, FR-M04-05.04, FR-M04-05.07, FR-M04-01.08, FR-M04-01.10, BR-M04-08, BR-M04-18 |


<!-- sc:branch SC-M04-005 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống xóa bằng cờ trả lời cuối, bỏ trả lời và dấu gốc khỏi luồng; không xóa dữ liệu gốc hoặc các trả lời khác đã bị ẩn/xóa. | C401 đã xóa; R411 đã xóa; R412 là trả lời cuối bình thường, Hà xóa R412; C402/C403 còn, count3→2 | END:SUCCESS | FR-M04-05.03, FR-M04-05.07, FR-M04-01.15, BR-M04-08, BR-M04-18 |


<!-- sc:branch SC-M04-005 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống vẫn cho chính tác giả xóa bình luận chưa xóa/không Bị ẩn, gắn cờ và giữ dữ liệu; áp dấu, trích dẫn và số đếm. Không dùng điều kiện cho sửa để cấm xóa. | Lan HEAVY; P401 Khóa toàn bộ; C401 Bình thường còn R411/R412; xóa C401 thì count5→4, giữ dấu gốc | END:SUCCESS | FR-M04-05.01, FR-M04-05.07, FR-M04-05.08, FR-M04-05.09, BR-M04-08, BR-M04-20 |


<!-- sc:branch SC-M04-005 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống cho xóa bình luận của chính tác giả như ngoài nhóm; áp cùng cờ/dữ liệu/dấu, không cho quyền xóa của người khác. | G41 Public; Lan xóa C401 của mình, body còn; R411/R412 giữ; count5→4 | END:SUCCESS | FR-M04-05.01, FR-M04-05.07, BR-M04-08, FR-M11-10.08 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này, thay toàn bộ đường chính. Actor khởi tạo ACT-001, kết quả END:REJECTED; dùng hậu điều kiện tương ứng mục4.

<!-- sc:role-path SC-M04-005 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu xóa bình luận của mình khỏi luồng người dùng. | Không có phiên xác định tác giả/người thao tác | V1.2 | BR-M04-16 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác chưa đăng nhập; không tự chạy chức năng đăng nhập, không thay đổi hoặc cung cấp nội dung bình luận riêng tư. | Yêu cầu hiện tại kết thúc, chưa thành công | END:REJECTED | BR-M04-16 |


**V2 — thay toàn bộ M1 đến kết thúc:** Mod/Admin thử thao tác này trên bình luận người khác qua M04. Actor khởi tạo ACT-003, kết quả END:REJECTED; dùng hậu điều kiện tương ứng mục4.

<!-- sc:role-path SC-M04-005 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-003 | Mod yêu cầu xóa bình luận của mình khỏi luồng người dùng đối với C401 của Lan. | actor=U-MOD; comment.author=U-LAN | V2.2 | FR-M04-05.05, BR-M04-23 |
| V2.2 | SYSTEM | Hệ thống từ chối quyền sửa/xóa hoặc xem lại dành cho tác giả đối với bình luận người khác. Vai trò Mod/Admin không thay điều kiện chủ; xử lý ẩn/tra cứu vụ liên quan do M08/M09 cấp riêng. | Không đổi cờ/body, không lộ nội dung qua đường xem lại của tác giả | END:REJECTED | FR-M04-05.05, BR-M04-23 |


<!-- sc:end SC-M04-005 -->

<a id="sc-m04-006"></a>

<!-- sc:scenario SC-M04-006 -->

### SC-M04-006

#### 1. Tên kịch bản chuẩn

Xem lại nội dung bình luận mình đã bị xử lý — BF-M04-006. UC owner: [UC-M04-006](../../us/US-M04.md#uc-m04-006). Trigger: Lan mở thông báo Bình luận của bạn đã bị ẩn cho C401 của mình.

#### 2. Actor thực hiện

ACT-002 — User có phiên là actor chính. ACT-003 kế thừa tương tác User theo US, không có đặc quyền sửa/xóa/xem lại của tác giả đối với người khác. Actor khởi tạo thay thế được ghi tại đường V trong mục6. Không có actor AI hoặc dịch vụ nội bộ.

#### 3. Tiền điều kiện

Có phiên và ngữ cảnh thông báo/khiếu nại hợp lệ, kiểm đúng chủ và đúng bình luận trong phản hồi. Đường này không phải luồng thảo luận bình thường hoặc khiếu nại riêng cho bình luận.

#### 4. Hậu điều kiện

<!-- sc:post SC-M04-006 -->

| result | condition |
|---|---|
| SUCCESS | Tác giả nhận đúng nội dung chỉ đọc trong ngữ cảnh hợp lệ, dữ liệu người báo cáo được bảo vệ; không đổi cờ xóa/kiểm duyệt/quyền trong luồng. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi kết quả gửi/sửa/xóa thành công trái điều kiện. Dữ liệu trước yêu cầu giữ nguyên trừ hiệu ứng được nêu rõ trong nhánh. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M04-006 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan mở thông báo Bình luận của bạn đã bị ẩn cho C401 của mình. | N401 trỏ C401.author=U-LAN,moderation=Bị ẩn | M2 | FR-M04-06.01 |
| M2 | SYSTEM | Hệ thống kiểm phiên/chính tác giả/liên kết thông báo, trả body C401 chỉ đọc kèm nhãn cho biết đang Bị ẩn. Không trả danh tính, lý do đã chọn, mô tả hoặc bằng chứng người báo cáo; không mở sửa/xóa/khôi phục hoặc làm bình luận hiện lại trong luồng. | C401.body được giữ; chỉ đọc; Bị ẩn vẫn giữ; câu chữ nhãn chưa chốt HMI | END:SUCCESS | FR-M04-06.01, FR-M04-06.04, FR-M04-06.05, BR-M04-22, BR-M04-23 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Guard chỉ bộ dữ liệu/ngữ cảnh thay thế cho lần thực thi: thay cả tên người/ID đối tượng minh họa khi được nêu, vẫn cùng vai trò actor; không gửi đồng thời bộ chuẩn và bộ lỗi. Các đường sửa quay lại bước kiểm cụ thể; nếu còn sai áp lại cùng guard, không tự giới hạn lần. REJECTED là kết thúc hợp lệ theo US, không bịa nút OK/hủy/thử lại ngoài nguồn.

<!-- sc:exceptions SC-M04-006 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Tác giả mở thông báo kết quả xử lý báo cáo về bình luận mình | E1.1 | FR-M04-06.02, FR-M04-06.04, FR-M04-06.05, BR-M04-22 |
| E2 | user-choice | M1 | Tác giả mở khiếu nại cảnh cáo/ban của mình liên quan bình luận | E2.1 | FR-M04-06.03, FR-M04-06.04, FR-M04-06.05, BR-M04-22, BR-M04-23, FR-M09-08.15 |
| E3 | system | M2 | Người mở khác tác giả | E3.1 | FR-M04-06.05 |
| E4 | system | M2 | Không có ngữ cảnh thông báo/khiếu nại hợp lệ về đúng bình luận | E4.1 | FR-M04-06.01, FR-M04-06.02, FR-M04-06.03, BR-M04-21, BR-M04-22 |


<!-- sc:branch SC-M04-006 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Lan mở thông báo kết quả xử lý N402 liên quan C401 của mình. | C401 Bị ẩn hoặc đã bị Lan xóa; báo cáo liên quan chính C401 | E1.2 | FR-M04-06.02 |
| E1.2 | SYSTEM | Hệ thống kiểm ngữ cảnh/chủ, trả nội dung bình luận chỉ đọc kể cả Bị ẩn/đã xóa. Có thể cho tác giả biết kết quả/lý do xử lý được phép, nhưng không trả các dữ liệu của người báo cáo. | Không trả reporter identity,selected_reason,description,evidence; không khôi phục dữ liệu ra luồng | END:SUCCESS | FR-M04-06.02, FR-M04-06.04, FR-M04-06.05, BR-M04-22 |


<!-- sc:branch SC-M04-006 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | Lan mở khiếu nại cảnh cáo/ban của mình có liên kết C401. | Appeal A401 của Lan; không phải tạo khiếu nại bình luận mới | E2.2 | FR-M04-06.03 |
| E2.2 | SYSTEM | Hệ thống kiểm chính tác giả và liên kết vụ, trả body C401 chỉ đọc, che dữ liệu người báo cáo. Nếu cảnh cáo/ban đã được lật, vẫn giữ bình luận Bị ẩn theo quyết định nguồn. | C401.Bị ẩn giữ nguyên; không tự gỡ ẩn khi kết luận khiếu nại có lợi | END:SUCCESS | FR-M04-06.03, FR-M04-06.04, FR-M04-06.05, BR-M04-22, BR-M04-23, FR-M09-08.15 |


<!-- sc:branch SC-M04-006 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối đường xem lại của tác giả dù người mở biết ID hoặc link thông báo. | Minh mở C401 của Lan qua N401 | END:REJECTED | FR-M04-06.05 |


<!-- sc:branch SC-M04-006 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối truy cập nội dung Bị ẩn/đã xóa qua đường xem lại; không tạo mục duyệt các bình luận bị xóa. | N401 hoặc appeal không trỏ C401, hoặc yêu cầu URL tùy ý | END:REJECTED | FR-M04-06.01, FR-M04-06.02, FR-M04-06.03, BR-M04-21, BR-M04-22 |


**V1 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng này, thay toàn bộ đường chính. Actor khởi tạo ACT-001, kết quả END:REJECTED; dùng hậu điều kiện tương ứng mục4.

<!-- sc:role-path SC-M04-006 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest yêu cầu xem lại nội dung bình luận mình đã bị xử lý. | Không có phiên xác định tác giả/người thao tác | V1.2 | FR-M04-06.05, BR-M04-22 |
| V1.2 | SYSTEM | Hệ thống từ chối thao tác chưa đăng nhập; không tự chạy chức năng đăng nhập, không thay đổi hoặc cung cấp nội dung bình luận riêng tư. | Yêu cầu hiện tại kết thúc, chưa thành công | END:REJECTED | FR-M04-06.05, BR-M04-22 |


**V2 — thay toàn bộ M1 đến kết thúc:** Mod/Admin thử thao tác này trên bình luận người khác qua M04. Actor khởi tạo ACT-003, kết quả END:REJECTED; dùng hậu điều kiện tương ứng mục4.

<!-- sc:role-path SC-M04-006 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-003 | Mod yêu cầu xem lại nội dung bình luận mình đã bị xử lý đối với C401 của Lan. | actor=U-MOD; comment.author=U-LAN | V2.2 | FR-M04-06.05, BR-M04-23 |
| V2.2 | SYSTEM | Hệ thống từ chối quyền sửa/xóa hoặc xem lại dành cho tác giả đối với bình luận người khác. Vai trò Mod/Admin không thay điều kiện chủ; xử lý ẩn/tra cứu vụ liên quan do M08/M09 cấp riêng. | Không đổi cờ/body, không lộ nội dung qua đường xem lại của tác giả | END:REJECTED | FR-M04-06.05, BR-M04-23 |


<!-- sc:end SC-M04-006 -->

## 5. Quy tắc nền và giao tiếp — không phải scenario

| ID | Trigger/điều kiện | Hiệu ứng/phạm vi | sources |
|---|---|---|---|
| AUT-M04-001 | Tạo/xóa, đổi kiểm duyệt hoặc tập trả lời bình thường; dựng lại luồng | Gốc đã xóa/Bị ẩn có≥1 trả lời bình thường giữ [Bình luận đã bị xóa]; hết trả lời bình thường thì bỏ dấu, không xóa dữ liệu. Trả lời bị xóa/ẩn không hiện. Count chỉ gồm gốc+trả lời đang bình thường, không tính dấu hoặc nội dung Bị ẩn, như nhau với mọi người. Không chọn push/cron/WebSocket hoặc nơi lưu count. | FR-M04-01.07, FR-M04-01.09, FR-M04-01.10, FR-M04-01.15, BR-M04-08, BR-M04-13, BR-M04-18 |
| RULE-M04-001 | Dựng trích dẫn và danh tính tác giả | Đích của trả lời lưu cụ thể nhưng luôn ở cấp hai dưới gốc. Trích dùng tên/body hiện tại, phần đầu vừa một dòng, không lồng trích dẫn tự động của đích và không thuộc thân trả lời. Đích xóa/ẩn dùng trả lời [bình luận đã bị xóa]. Tài khoản DEACTIVATED/DELETED chỉ thay tên/avatar theo M01, không tự xóa nội dung bình luận. | FR-M04-01.08, FR-M04-01.09, FR-M04-01.16, FR-M04-01.17, FR-M04-03.03, FR-M04-03.13, BR-M04-03, BR-M04-04, BR-M04-13, FR-M01-13.03, FR-M01-13.04 |
| RULE-M04-002 | Quyền xem, bài khóa, cảnh cáo và quyền nhóm | Quyền luồng đi theo bài; bài hiện lại không tự gỡ Bị ẩn. Khóa bài cấm tạo/sửa nhưng cho tác giả xóa, bình luận cũ vẫn hiện. HEAVY chỉ chặn tạo; LIGHT/MEDIUM tạo được nếu điều kiện khác đạt. Bị ẩn thì tác giả không sửa/xóa. Phiên/BANNED/bảo trì theo M01, không đồng nhất HEAVY với BANNED. M11 Private chặn người ngoài, Public cho người có phiên; rời Private cấm sửa/xóa bình luận mình, rời Public vẫn theo điều kiện thường; nhóm Bị khóa cấm bình luận mới kể cả Owner/Group Mod. | FR-M04-01.11, FR-M04-01.12, FR-M04-01.13, FR-M04-02.06, FR-M04-02.07, FR-M04-03.07, FR-M04-03.08, FR-M04-04.09, FR-M04-04.10, FR-M04-04.11, FR-M04-05.08, FR-M04-05.09, FR-M04-05.10, BR-M04-14, BR-M04-15, BR-M04-16, BR-M04-17, BR-M04-20, FR-M11-03.07, FR-M11-03.13, FR-M11-10.08, FR-M11-10.09, FR-M11-16.04 |
| RULE-M04-003 | Công bố, AI, phản ứng và phân phối sự kiện | Gốc/trả lời hiển thị ngay Bình thường, M04 không gọi AI trực tiếp. Quét sau đăng theo kích hoạt tốc độ luồng do M08/M13; sửa chờ kích hoạt kế tiếp, không quét ngay. Admin không bị quét/báo cáo theo M08, không miễn điều kiện khóa/quyền bài ở M04 hoặc tự miễn cho Mod. Chỉ upvote, thao tác/điểm thuộc M12; không downvote/phản ứng khác, Accepted Answer, Topic/Tag riêng, tệp hay lịch sử. Gốc/trả lời mới cung cấp sự kiện cho M07, mốc hiển thị cho mention M01, count/thời điểm cho các module xếp hạng/thống kê; không triển khai gửi thông báo/điểm/Trending trong M04. | FR-M04-02.02, FR-M04-03.04, BR-M04-02, BR-M04-09, BR-M04-10, BR-M04-11, BR-M04-12, FR-M08-08.02, FR-M08-08.03, FR-M03-14.06 |
| RULE-M04-004 | Cờ xóa, bài bị xóa và phạm vi vụ việc | Bình luận không bao giờ xóa hẳn: cờ xóa giữ body, không khôi phục. Bài đã xóa kể cả đủ hạn xóa hẳn vẫn giữ các bình luận cùng bài, không cascade xóa riêng. Nội dung bình luận xóa chỉ tra cứu trong vụ báo cáo/lịch sử/khiếu nại liên quan, không browse/search. Mod/Admin chỉ ẩn người khác ở M08, không xóa bằng UC005. Không có khiếu nại bình luận riêng; lật cảnh cáo/ban liên quan giữ bình luận Bị ẩn, không làm nội dung tự trở lại luồng. | FR-M04-05.04, FR-M04-05.07, FR-M04-05.11, FR-M04-06.03, FR-M04-06.04, FR-M04-06.05, BR-M04-08, BR-M04-21, BR-M04-22, BR-M04-23, FR-M03-17.02, FR-M09-08.15 |
| RULE-M04-COMPOSER | Include UC007 trong tạo gốc, trả lời và sửa | Chỉ bộ định dạng tối giản BR01; không H1/bảng/checklist/tệp. Thân tối đa1000 từ, không rỗng/chỉ trắng. Vượt trong lúc soạn/sửa cảnh báo ngay số hiện tại/1000; gửi/lưu khi vượt giữ nguyên bản đang nhập để sửa. Dòng trích tự động không tính, khối trích do tác giả nhập vẫn tính. UC007 trả nội dung cho UC gọi, không lưu bình luận độc lập. Không bịa HMI cắt dòng hoặc số ký tự trích, retry/rollback lỗi mạng chưa có nguồn. | FR-M04-02.03, FR-M04-02.04, FR-M04-02.09, FR-M04-02.10, FR-M04-02.11, FR-M04-03.05, FR-M04-03.12, FR-M04-03.13, FR-M04-04.06, FR-M04-04.12, FR-M04-04.13, BR-M04-01, BR-M04-02, BR-M04-19 |


## 6. Truy vết và đối soát

| Mã FR/BR | SC/bước/nhánh hoặc quy tắc | Mức đối soát |
|---|---|---|
| FR-M04-01 | SC-M04-001/M1; SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E3.1; SC-M04-001/E4.1; SC-M04-001/E12.1; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V3.2; SC-M04-001/V4.2; SC-M04-001/E2.3; SC-M04-001/E3.3; SC-M04-001/E4.3; SC-M04-001/V2.4; SC-M04-001/V3.4; SC-M04-001/V4.4; SC-M04-003/M4; SC-M04-003/E1.4; SC-M04-003/E2.4; SC-M04-001/E8.1; SC-M04-004/M4; SC-M04-001/E5.1; SC-M04-001/E6.1; SC-M04-001/E7.1; SC-M04-001/E9.1; SC-M04-001/V6.2; SC-M04-002/M4; SC-M04-005/M2; SC-M04-005/E6.1; AUT-M04-001; SC-M04-001/E10.1; RULE-M04-002; SC-M04-003/M2; SC-M04-003/E16.1; RULE-M04-001; SC-M04-001/E1.1; SC-M04-001/V5.1; SC-M04-001/V5.2; SC-M04-001/E2.2; SC-M04-001/E3.2; SC-M04-001/E4.2; SC-M04-001/V2.3; SC-M04-001/V3.3; SC-M04-001/V4.3; SC-M04-001/V6.1; SC-M04-005/E5.1; SC-M04-005/E7.1; SC-M04-001/V1.1; SC-M04-001/V2.1; SC-M04-001/V3.1; SC-M04-001/V4.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-02 | SC-M04-002/M1; SC-M04-002/M3; SC-M04-002/M4; SC-M04-002/E11.1; SC-M04-002/M2; RULE-M04-COMPOSER; RULE-M04-003; SC-M04-002/V1.1; SC-M04-002/V1.2; SC-M04-002/E1.1; SC-M04-002/E5.1; RULE-M04-002; SC-M04-002/E2.1; SC-M04-002/E6.1; SC-M04-002/E3.1; SC-M04-002/E7.1; SC-M04-002/E10.1; SC-M04-002/E10.2; SC-M04-002/E10.3; SC-M04-002/E10.4; SC-M04-002/E10.5; SC-M04-003/E14.1; SC-M04-003/E14.2; SC-M04-003/E14.3; SC-M04-003/E14.4; SC-M04-003/E14.5; SC-M04-002/E9.1; SC-M04-002/E9.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-03 | SC-M04-003/M1; SC-M04-003/M2; SC-M04-003/E1.1; SC-M04-003/E1.2; SC-M04-003/E2.1; SC-M04-003/E2.2; RULE-M04-COMPOSER; SC-M04-003/M4; SC-M04-003/E1.4; SC-M04-003/E2.4; SC-M04-003/E14.1; SC-M04-003/E14.2; SC-M04-003/E14.3; SC-M04-003/E14.4; SC-M04-003/E14.5; SC-M04-003/E16.1; SC-M04-003/E17.2; RULE-M04-001; SC-M04-003/M3; SC-M04-003/E15.1; RULE-M04-003; SC-M04-003/V1.1; SC-M04-003/V1.2; SC-M04-003/E5.1; SC-M04-003/E9.1; RULE-M04-002; SC-M04-003/E6.1; SC-M04-003/E10.1; SC-M04-003/E7.1; SC-M04-003/E11.1; SC-M04-003/E3.1; SC-M04-003/E4.1; SC-M04-003/E13.1; SC-M04-003/E13.2; SC-M04-003/E1.3; SC-M04-003/E2.3 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-04 | SC-M04-004/M1; SC-M04-004/M4; SC-M04-004/E11.1; SC-M04-004/M2; RULE-M04-COMPOSER; SC-M04-004/E1.1; SC-M04-004/E6.1; SC-M04-004/V2.1; SC-M04-004/V2.2; SC-M04-004/E2.1; SC-M04-004/E7.1; SC-M04-004/E4.1; SC-M04-004/E9.1; RULE-M04-002; SC-M04-004/E3.1; SC-M04-004/E8.1; SC-M04-004/M3; SC-M04-004/E14.1; SC-M04-004/E12.1; SC-M04-004/E12.2; SC-M04-004/E13.3; SC-M04-004/E13.4; SC-M04-004/E13.5; SC-M04-004/E13.1; SC-M04-004/E13.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-05 | SC-M04-005/M1; SC-M04-005/M2; SC-M04-005/E8.1; SC-M04-005/E9.1; SC-M04-005/E5.1; SC-M04-005/E6.1; RULE-M04-004; SC-M04-005/E1.1; SC-M04-005/V2.1; SC-M04-005/V2.2; SC-M04-005/E2.1; SC-M04-005/E7.1; SC-M04-005/E3.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-06 | SC-M04-006/M1; SC-M04-006/M2; SC-M04-006/E4.1; SC-M04-006/E1.2; SC-M04-006/E2.2; RULE-M04-004; SC-M04-006/E3.1; SC-M04-006/V1.1; SC-M04-006/V1.2; SC-M04-006/V2.1; SC-M04-006/V2.2; SC-M04-006/E1.1; SC-M04-006/E2.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.01 | SC-M04-001/M1; SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E3.1; SC-M04-001/E4.1; SC-M04-001/E12.1; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V3.2; SC-M04-001/V4.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.02 | SC-M04-001/V1.1; SC-M04-001/V1.2; SC-M04-001/V2.1; SC-M04-001/V3.1; SC-M04-001/V4.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.03 | SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E3.1; SC-M04-001/E4.1; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V3.2; SC-M04-001/V4.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.04 | SC-M04-001/E2.2; SC-M04-001/E2.3; SC-M04-001/E3.2; SC-M04-001/E3.3; SC-M04-001/E4.2; SC-M04-001/E4.3; SC-M04-001/V2.3; SC-M04-001/V2.4; SC-M04-001/V3.3; SC-M04-001/V3.4; SC-M04-001/V4.3; SC-M04-001/V4.4 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.05 | SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E2.3; SC-M04-001/E3.1; SC-M04-001/E3.3; SC-M04-001/E4.1; SC-M04-001/E4.3; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V2.4; SC-M04-001/V3.2; SC-M04-001/V3.4; SC-M04-001/V4.2; SC-M04-001/V4.4; SC-M04-003/M4; SC-M04-003/E1.4; SC-M04-003/E2.4 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.06 | SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E3.1; SC-M04-001/E4.1; SC-M04-001/E8.1; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V3.2; SC-M04-001/V4.2; SC-M04-004/M4 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.07 | SC-M04-001/E5.1; SC-M04-001/E7.1; SC-M04-001/V6.2; SC-M04-005/M2; AUT-M04-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.08 | SC-M04-001/E5.1; SC-M04-001/E6.1; SC-M04-001/V6.2; SC-M04-005/M2; SC-M04-005/E6.1; RULE-M04-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.09 | SC-M04-001/E5.1; SC-M04-001/E6.1; SC-M04-001/E7.1; SC-M04-001/E9.1; SC-M04-001/V6.1; SC-M04-001/V6.2; AUT-M04-001; RULE-M04-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.10 | SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E2.3; SC-M04-001/E3.1; SC-M04-001/E3.3; SC-M04-001/E4.1; SC-M04-001/E4.3; SC-M04-001/E5.1; SC-M04-001/E6.1; SC-M04-001/E7.1; SC-M04-001/E9.1; SC-M04-001/E12.1; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V2.4; SC-M04-001/V3.2; SC-M04-001/V3.4; SC-M04-001/V4.2; SC-M04-001/V4.4; SC-M04-001/V6.2; SC-M04-002/M4; SC-M04-003/M4; SC-M04-003/E1.4; SC-M04-003/E2.4; SC-M04-005/M2; SC-M04-005/E6.1; AUT-M04-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.11 | SC-M04-001/E1.1; SC-M04-001/V5.1; SC-M04-001/V5.2; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.12 | SC-M04-001/E9.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.13 | SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E3.1; SC-M04-001/E4.1; SC-M04-001/E10.1; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V3.2; SC-M04-001/V4.2; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.14 | SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E2.3; SC-M04-001/E3.1; SC-M04-001/E3.3; SC-M04-001/E4.1; SC-M04-001/E4.3; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V2.4; SC-M04-001/V3.2; SC-M04-001/V3.4; SC-M04-001/V4.2; SC-M04-001/V4.4 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.15 | SC-M04-001/E7.1; SC-M04-001/E12.1; SC-M04-005/E5.1; SC-M04-005/E7.1; AUT-M04-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.16 | SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E3.1; SC-M04-001/E4.1; SC-M04-001/E8.1; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V3.2; SC-M04-001/V4.2; SC-M04-003/M2; SC-M04-003/M4; SC-M04-003/E1.4; SC-M04-003/E2.4; SC-M04-003/E16.1; SC-M04-004/M4; RULE-M04-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-01.17 | SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E3.1; SC-M04-001/E4.1; SC-M04-001/E8.1; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V3.2; SC-M04-001/V4.2; SC-M04-003/M2; SC-M04-003/M4; SC-M04-003/E16.1; RULE-M04-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-02.01 | SC-M04-002/M1; SC-M04-002/M3; SC-M04-002/M4; SC-M04-002/E11.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-02.02 | SC-M04-002/M4; SC-M04-002/E11.1; RULE-M04-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-02.03 | SC-M04-002/M2; RULE-M04-COMPOSER | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-02.04 | SC-M04-002/M2; RULE-M04-COMPOSER | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-02.05 | SC-M04-002/M4; SC-M04-002/V1.1; SC-M04-002/V1.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-02.06 | SC-M04-002/M4; SC-M04-002/E1.1; SC-M04-002/E5.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-02.07 | SC-M04-002/M4; SC-M04-002/E2.1; SC-M04-002/E6.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-02.08 | SC-M04-002/M4; SC-M04-002/E3.1; SC-M04-002/E7.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-02.09 | SC-M04-002/E10.1; SC-M04-002/E10.2; SC-M04-002/E10.3; SC-M04-002/E10.4; SC-M04-002/E10.5; SC-M04-003/E14.1; SC-M04-003/E14.2; SC-M04-003/E14.3; SC-M04-003/E14.4; SC-M04-003/E14.5; RULE-M04-COMPOSER | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-02.10 | SC-M04-002/M4; SC-M04-002/E10.1; SC-M04-002/E10.2; SC-M04-002/E10.3; SC-M04-002/E10.4; SC-M04-002/E10.5; SC-M04-003/E14.1; SC-M04-003/E14.2; SC-M04-003/E14.3; SC-M04-003/E14.4; SC-M04-003/E14.5; RULE-M04-COMPOSER | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-02.11 | SC-M04-002/M4; SC-M04-002/E9.1; SC-M04-002/E9.2; SC-M04-003/E14.1; SC-M04-003/E14.2; SC-M04-003/E14.3; SC-M04-003/E14.4; SC-M04-003/E14.5; RULE-M04-COMPOSER | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-03.01 | SC-M04-003/M1; SC-M04-003/M2; SC-M04-003/E1.1; SC-M04-003/E1.2; SC-M04-003/E2.1; SC-M04-003/E2.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-03.02 | SC-M04-003/M3; SC-M04-003/M4; SC-M04-003/E15.1; SC-M04-003/E16.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-03.03 | SC-M04-003/E1.2; SC-M04-003/E1.3; SC-M04-003/E1.4; SC-M04-003/E2.2; SC-M04-003/E2.3; SC-M04-003/E2.4; RULE-M04-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-03.04 | SC-M04-003/M4; SC-M04-003/E1.4; SC-M04-003/E2.4; SC-M04-003/E15.1; SC-M04-003/E16.1; RULE-M04-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-03.05 | SC-M04-003/M2; RULE-M04-COMPOSER | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-03.06 | SC-M04-003/M4; SC-M04-003/V1.1; SC-M04-003/V1.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-03.07 | SC-M04-003/M4; SC-M04-003/E5.1; SC-M04-003/E9.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-03.08 | SC-M04-003/M4; SC-M04-003/E6.1; SC-M04-003/E10.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-03.09 | SC-M04-003/M4; SC-M04-003/E7.1; SC-M04-003/E11.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-03.10 | SC-M04-003/M4; SC-M04-003/E3.1; SC-M04-003/E4.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-03.11 | SC-M04-003/E1.2; SC-M04-003/E1.4; SC-M04-003/E2.2; SC-M04-003/E2.4 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-03.12 | SC-M04-003/M4; SC-M04-003/E13.1; SC-M04-003/E13.2; SC-M04-003/E14.1; SC-M04-003/E14.2; SC-M04-003/E14.3; SC-M04-003/E14.4; SC-M04-003/E14.5; SC-M04-003/E16.1; SC-M04-003/E17.2; RULE-M04-COMPOSER | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-03.13 | SC-M04-003/M2; SC-M04-003/M4; SC-M04-003/E1.2; SC-M04-003/E1.4; SC-M04-003/E2.2; SC-M04-003/E2.4; SC-M04-003/E14.1; SC-M04-003/E14.2; SC-M04-003/E14.3; SC-M04-003/E14.4; SC-M04-003/E14.5; SC-M04-003/E16.1; SC-M04-003/E17.2; RULE-M04-001; RULE-M04-COMPOSER | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-04.01 | SC-M04-004/M3; SC-M04-004/M4; SC-M04-004/E11.1; SC-M04-004/E14.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-04.02 | SC-M04-004/M4; SC-M04-004/E11.1; SC-M04-004/E14.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-04.03 | SC-M04-004/M4; SC-M04-004/E11.1; SC-M04-004/E14.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-04.04 | SC-M04-004/M2; SC-M04-004/M4; SC-M04-004/E11.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-04.05 | SC-M04-004/M1; SC-M04-004/M4; SC-M04-004/E11.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-04.06 | SC-M04-004/M2; RULE-M04-COMPOSER | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-04.07 | SC-M04-004/M2; SC-M04-004/E1.1; SC-M04-004/E6.1; SC-M04-004/V2.1; SC-M04-004/V2.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-04.08 | SC-M04-004/M2; SC-M04-004/E2.1; SC-M04-004/E7.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-04.09 | SC-M04-004/M2; SC-M04-004/E4.1; SC-M04-004/E9.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-04.10 | SC-M04-004/M2; SC-M04-004/E3.1; SC-M04-004/E8.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-04.11 | SC-M04-004/M4; SC-M04-004/E11.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-04.12 | SC-M04-004/E13.1; SC-M04-004/E13.2; RULE-M04-COMPOSER | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-04.13 | SC-M04-004/M4; SC-M04-004/E12.1; SC-M04-004/E12.2; SC-M04-004/E13.3; SC-M04-004/E13.4; SC-M04-004/E13.5; RULE-M04-COMPOSER | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-05.01 | SC-M04-005/M1; SC-M04-005/M2; SC-M04-005/E8.1; SC-M04-005/E9.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-05.02 | SC-M04-005/E5.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-05.03 | SC-M04-005/E6.1; SC-M04-005/E7.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-05.04 | SC-M04-005/M2; SC-M04-005/E5.1; SC-M04-005/E6.1; RULE-M04-004 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-05.05 | SC-M04-005/M2; SC-M04-005/E1.1; SC-M04-005/V2.1; SC-M04-005/V2.2 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-05.06 | SC-M04-005/M2; SC-M04-005/E2.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-05.07 | SC-M04-005/M2; SC-M04-005/E5.1; SC-M04-005/E6.1; SC-M04-005/E7.1; SC-M04-005/E8.1; SC-M04-005/E9.1; RULE-M04-004 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-05.08 | SC-M04-005/E8.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-05.09 | SC-M04-005/E8.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-05.10 | SC-M04-005/E3.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-05.11 | RULE-M04-004 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-06.01 | SC-M04-006/M1; SC-M04-006/M2; SC-M04-006/E4.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-06.02 | SC-M04-006/E1.1; SC-M04-006/E1.2; SC-M04-006/E4.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-06.03 | SC-M04-006/E2.1; SC-M04-006/E2.2; SC-M04-006/E4.1; RULE-M04-004 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-06.04 | SC-M04-006/M2; SC-M04-006/E1.2; SC-M04-006/E2.2; RULE-M04-004 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| FR-M04-06.05 | SC-M04-006/M2; SC-M04-006/E1.2; SC-M04-006/E2.2; SC-M04-006/E3.1; SC-M04-006/V1.1; SC-M04-006/V1.2; SC-M04-006/V2.1; SC-M04-006/V2.2; RULE-M04-004 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-01 | SC-M04-002/M2; SC-M04-004/M2; RULE-M04-COMPOSER | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-02 | SC-M04-002/M2; SC-M04-004/M2; RULE-M04-003; RULE-M04-COMPOSER | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-03 | SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E3.1; SC-M04-001/E4.1; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V3.2; SC-M04-001/V4.2; SC-M04-003/M2; SC-M04-003/M4; SC-M04-003/E1.2; SC-M04-003/E1.4; SC-M04-003/E2.2; SC-M04-003/E2.4; RULE-M04-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-04 | SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E3.1; SC-M04-001/E4.1; SC-M04-001/E6.1; SC-M04-001/E8.1; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V3.2; SC-M04-001/V4.2; SC-M04-003/M2; SC-M04-003/M4; SC-M04-003/E1.2; SC-M04-003/E1.4; SC-M04-003/E2.2; SC-M04-003/E2.4; SC-M04-003/E16.1; SC-M04-004/M4; RULE-M04-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-05 | SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E2.3; SC-M04-001/E3.1; SC-M04-001/E3.3; SC-M04-001/E4.1; SC-M04-001/E4.3; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V2.4; SC-M04-001/V3.2; SC-M04-001/V3.4; SC-M04-001/V4.2; SC-M04-001/V4.4 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-06 | SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E2.3; SC-M04-001/E3.1; SC-M04-001/E3.3; SC-M04-001/E4.1; SC-M04-001/E4.3; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V2.4; SC-M04-001/V3.2; SC-M04-001/V3.4; SC-M04-001/V4.2; SC-M04-001/V4.4; SC-M04-003/M4 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-07 | SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E3.1; SC-M04-001/E4.1; SC-M04-001/E8.1; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V3.2; SC-M04-001/V4.2; SC-M04-004/M2; SC-M04-004/M4; SC-M04-004/E11.1; SC-M04-004/E14.1 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-08 | SC-M04-001/E5.1; SC-M04-001/E6.1; SC-M04-001/E7.1; SC-M04-005/M2; SC-M04-005/E5.1; SC-M04-005/E6.1; SC-M04-005/E7.1; SC-M04-005/E8.1; SC-M04-005/E9.1; AUT-M04-001; RULE-M04-004 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-09 | RULE-M04-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-10 | RULE-M04-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-11 | RULE-M04-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-12 | SC-M04-002/M4; SC-M04-002/E11.1; SC-M04-003/M4; SC-M04-003/E15.1; RULE-M04-003 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-13 | SC-M04-001/E5.1; SC-M04-001/E6.1; SC-M04-001/E7.1; SC-M04-001/E9.1; SC-M04-001/V6.2; AUT-M04-001; RULE-M04-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-14 | SC-M04-001/E10.1; SC-M04-002/M4; SC-M04-002/E1.1; SC-M04-002/E5.1; SC-M04-003/M4; SC-M04-003/E5.1; SC-M04-003/E9.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-15 | SC-M04-002/M4; SC-M04-002/E2.1; SC-M04-002/E6.1; SC-M04-002/E11.1; SC-M04-003/M4; SC-M04-003/E6.1; SC-M04-003/E10.1; SC-M04-003/E15.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-16 | SC-M04-001/V1.2; SC-M04-002/V1.1; SC-M04-002/V1.2; SC-M04-003/V1.1; SC-M04-003/V1.2; SC-M04-004/V1.1; SC-M04-004/V1.2; SC-M04-005/V1.1; SC-M04-005/V1.2; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-17 | SC-M04-001/M2; SC-M04-001/E1.1; SC-M04-001/E2.1; SC-M04-001/E3.1; SC-M04-001/E4.1; SC-M04-001/E9.1; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V3.2; SC-M04-001/V4.2; SC-M04-001/V5.2; SC-M04-002/E3.1; SC-M04-002/E7.1; SC-M04-003/E7.1; SC-M04-003/E11.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-18 | SC-M04-001/M2; SC-M04-001/E2.1; SC-M04-001/E2.3; SC-M04-001/E3.1; SC-M04-001/E3.3; SC-M04-001/E4.1; SC-M04-001/E4.3; SC-M04-001/E5.1; SC-M04-001/E6.1; SC-M04-001/E7.1; SC-M04-001/E9.1; SC-M04-001/E12.1; SC-M04-001/V1.2; SC-M04-001/V2.2; SC-M04-001/V2.4; SC-M04-001/V3.2; SC-M04-001/V3.4; SC-M04-001/V4.2; SC-M04-001/V4.4; SC-M04-001/V6.2; SC-M04-002/M4; SC-M04-003/M4; SC-M04-003/E1.4; SC-M04-003/E2.4; SC-M04-005/M2; SC-M04-005/E5.1; SC-M04-005/E6.1; SC-M04-005/E7.1; AUT-M04-001 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-19 | SC-M04-002/M3; SC-M04-002/M4; SC-M04-002/E9.1; SC-M04-002/E9.2; SC-M04-002/E10.1; SC-M04-002/E10.2; SC-M04-002/E10.3; SC-M04-002/E10.4; SC-M04-002/E10.5; SC-M04-003/M4; SC-M04-003/E13.1; SC-M04-003/E13.2; SC-M04-003/E14.1; SC-M04-003/E14.2; SC-M04-003/E14.3; SC-M04-003/E14.4; SC-M04-003/E14.5; SC-M04-003/E16.1; SC-M04-003/E17.1; SC-M04-003/E17.2; SC-M04-003/E17.3; SC-M04-004/M4; RULE-M04-COMPOSER | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-20 | SC-M04-004/M2; SC-M04-004/M4; SC-M04-004/E11.1; SC-M04-005/E8.1; RULE-M04-002 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-21 | SC-M04-005/M2; SC-M04-006/E4.1; RULE-M04-004 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-22 | SC-M04-006/M2; SC-M04-006/E1.2; SC-M04-006/E2.2; SC-M04-006/E4.1; SC-M04-006/V1.1; SC-M04-006/V1.2; RULE-M04-004 | Có vị trí triển khai theo nguồn; chưa phê duyệt |
| BR-M04-23 | SC-M04-005/M2; SC-M04-005/V2.1; SC-M04-005/V2.2; SC-M04-006/M2; SC-M04-006/E2.2; SC-M04-006/V2.1; SC-M04-006/V2.2; RULE-M04-004 | Có vị trí triển khai theo nguồn; chưa phê duyệt |


| UC | Guard/lựa chọn | SC/ngoại lệ | Đích |
|---|---|---|---|
| UC-M04-001 | Người yêu cầu không được xem bài, kể cả Private không đủ quyền hoặc bài không còn hiển thị | SC-M04-001/E1 | END:REJECTED |
| UC-M04-001 | Sau khi luồng đã được trả, người xem chọn Mới nhất | SC-M04-001/E2 | END:SUCCESS |
| UC-M04-001 | Sau khi luồng đã được trả, người xem chọn Cũ nhất | SC-M04-001/E3 | END:SUCCESS |
| UC-M04-001 | Sau khi luồng đã được trả, người xem chọn Top | SC-M04-001/E4 | END:SUCCESS |
| UC-M04-001 | Gốc C401 đã xóa hoặc Bị ẩn, còn R411/R412 bình thường | SC-M04-001/E5 | END:SUCCESS |
| UC-M04-001 | Trả lời R411 đã xóa hoặc Bị ẩn, R412 vẫn bình thường | SC-M04-001/E6 | END:SUCCESS |
| UC-M04-001 | Gốc đang hiện dấu, mọi trả lời đều không còn hiển thị bình thường | SC-M04-001/E7 | END:SUCCESS |
| UC-M04-001 | Đích của trích dẫn được tác giả sửa, người xem tải lại luồng | SC-M04-001/E8 | END:SUCCESS |
| UC-M04-001 | Bài từ không hiển thị trở lại hiển thị với người xem | SC-M04-001/E9 | END:SUCCESS |
| UC-M04-001 | Bài Khóa bình luận hoặc Khóa toàn bộ nhưng vẫn được phép đọc | SC-M04-001/E10 | END:SUCCESS |
| UC-M04-001 | Tài khoản tác giả bình luận DEACTIVATED hoặc DELETED, bình luận chưa xóa/không Bị ẩn | SC-M04-001/E11 | END:SUCCESS |
| UC-M04-001 | Bài không có bình luận bình thường hoặc dấu còn hợp lệ | SC-M04-001/E12 | END:SUCCESS |
| UC-M04-002 | Bài Khóa bình luận hoặc Khóa toàn bộ | SC-M04-002/E1 | END:REJECTED |
| UC-M04-002 | Người gửi ở mức cảnh cáo HEAVY | SC-M04-002/E2 | END:REJECTED |
| UC-M04-002 | Bài không tồn tại hoặc không hiển thị với actor | SC-M04-002/E3 | END:REJECTED |
| UC-M04-002 | Quyền nhóm không cho bình luận: Private ngoài nhóm hoặc nhóm Bị khóa | SC-M04-002/E4 | END:REJECTED |
| UC-M04-002 | Bài Khóa bình luận hoặc Khóa toàn bộ | SC-M04-002/E5 | END:REJECTED |
| UC-M04-002 | Người gửi ở mức cảnh cáo HEAVY | SC-M04-002/E6 | END:REJECTED |
| UC-M04-002 | Bài không tồn tại hoặc không hiển thị với actor | SC-M04-002/E7 | END:REJECTED |
| UC-M04-002 | Quyền nhóm không cho bình luận: Private ngoài nhóm hoặc nhóm Bị khóa | SC-M04-002/E8 | END:REJECTED |
| UC-M04-002 | Nội dung gửi trống hoặc chỉ khoảng trắng | SC-M04-002/E9 | M4 |
| UC-M04-002 | Trong lúc soạn vượt1000 từ, người gửi thử gửi rồi sửa | SC-M04-002/E10 | M4 |
| UC-M04-002 | Actor LIGHT/MEDIUM hoặc người ngoài nhóm Public có phiên, các điều kiện khác hợp lệ | SC-M04-002/E11 | END:SUCCESS |
| UC-M04-003 | Hà chọn trả lời R411 thay vì chọn gốc | SC-M04-003/E1 | END:SUCCESS |
| UC-M04-003 | Hà chọn trả lời R411 khi gốc C401 đang hiện dấu đã xóa/Bị ẩn | SC-M04-003/E2 | END:SUCCESS |
| UC-M04-003 | Đích được chọn đã xóa hoặc Bị ẩn, kể cả gốc đang là dấu thay thế | SC-M04-003/E3 | END:REJECTED |
| UC-M04-003 | Đích được chọn đã xóa hoặc Bị ẩn, kể cả gốc đang là dấu thay thế | SC-M04-003/E4 | END:REJECTED |
| UC-M04-003 | Bài Khóa bình luận hoặc Khóa toàn bộ | SC-M04-003/E5 | END:REJECTED |
| UC-M04-003 | Người gửi ở mức cảnh cáo HEAVY | SC-M04-003/E6 | END:REJECTED |
| UC-M04-003 | Bài không tồn tại hoặc không hiển thị với actor | SC-M04-003/E7 | END:REJECTED |
| UC-M04-003 | Quyền nhóm không cho bình luận: Private ngoài nhóm hoặc nhóm Bị khóa | SC-M04-003/E8 | END:REJECTED |
| UC-M04-003 | Bài Khóa bình luận hoặc Khóa toàn bộ | SC-M04-003/E9 | END:REJECTED |
| UC-M04-003 | Người gửi ở mức cảnh cáo HEAVY | SC-M04-003/E10 | END:REJECTED |
| UC-M04-003 | Bài không tồn tại hoặc không hiển thị với actor | SC-M04-003/E11 | END:REJECTED |
| UC-M04-003 | Quyền nhóm không cho bình luận: Private ngoài nhóm hoặc nhóm Bị khóa | SC-M04-003/E12 | END:REJECTED |
| UC-M04-003 | Nội dung gửi trống hoặc chỉ khoảng trắng | SC-M04-003/E13 | M4 |
| UC-M04-003 | Trong lúc soạn vượt1000 từ, người gửi thử gửi rồi sửa | SC-M04-003/E14 | M4 |
| UC-M04-003 | Actor LIGHT/MEDIUM hoặc người ngoài nhóm Public có phiên, các điều kiện khác hợp lệ | SC-M04-003/E15 | END:SUCCESS |
| UC-M04-003 | Thân trả lời1000 từ nhưng bình luận được trích rất dài | SC-M04-003/E16 | END:SUCCESS |
| UC-M04-003 | Khối trích dẫn người gửi tự gõ làm tổng thân trả lời vượt giới hạn | SC-M04-003/E17 | M4 |
| UC-M04-004 | Người sửa khác tác giả | SC-M04-004/E1 | END:REJECTED |
| UC-M04-004 | Bình luận đã xóa | SC-M04-004/E2 | END:REJECTED |
| UC-M04-004 | Bình luận Bị ẩn | SC-M04-004/E3 | END:REJECTED |
| UC-M04-004 | Bài Khóa bình luận hoặc Khóa toàn bộ | SC-M04-004/E4 | END:REJECTED |
| UC-M04-004 | Đã rời/kick khỏi nhóm Private | SC-M04-004/E5 | END:REJECTED |
| UC-M04-004 | Người sửa khác tác giả | SC-M04-004/E6 | END:REJECTED |
| UC-M04-004 | Bình luận đã xóa | SC-M04-004/E7 | END:REJECTED |
| UC-M04-004 | Bình luận Bị ẩn | SC-M04-004/E8 | END:REJECTED |
| UC-M04-004 | Bài Khóa bình luận hoặc Khóa toàn bộ | SC-M04-004/E9 | END:REJECTED |
| UC-M04-004 | Đã rời/kick khỏi nhóm Private | SC-M04-004/E10 | END:REJECTED |
| UC-M04-004 | Tác giả HEAVY hoặc đã lâu/rất nhiều lần kể từ khi đăng, các điều kiện khác hợp lệ | SC-M04-004/E11 | END:SUCCESS |
| UC-M04-004 | Nội dung sửa trống hoặc chỉ khoảng trắng | SC-M04-004/E12 | M4 |
| UC-M04-004 | Body đang sửa vượt1000 từ | SC-M04-004/E13 | M4 |
| UC-M04-004 | Tác giả rời/kick khỏi nhóm Public nhưng điều kiện sửa khác hợp lệ | SC-M04-004/E14 | END:SUCCESS |
| UC-M04-005 | Người xóa khác tác giả | SC-M04-005/E1 | END:REJECTED |
| UC-M04-005 | Bình luận đã xóa | SC-M04-005/E2 | END:REJECTED |
| UC-M04-005 | Bình luận đang Bị ẩn | SC-M04-005/E3 | END:REJECTED |
| UC-M04-005 | Đã rời/kick khỏi nhóm Private | SC-M04-005/E4 | END:REJECTED |
| UC-M04-005 | Gốc của tác giả không có trả lời nào hiển thị bình thường | SC-M04-005/E5 | END:SUCCESS |
| UC-M04-005 | Tác giả xóa một trả lời có trả lời khác trỏ tới nó | SC-M04-005/E6 | END:SUCCESS |
| UC-M04-005 | Trả lời cuối cùng đang bình thường bị tác giả xóa, gốc đã hiện dấu | SC-M04-005/E7 | END:SUCCESS |
| UC-M04-005 | Bài đang khóa và/hoặc tác giả HEAVY, điều kiện xóa khác hợp lệ | SC-M04-005/E8 | END:SUCCESS |
| UC-M04-005 | Tác giả rời/kick khỏi nhóm Public, các điều kiện xóa khác hợp lệ | SC-M04-005/E9 | END:SUCCESS |
| UC-M04-006 | Tác giả mở thông báo kết quả xử lý báo cáo về bình luận mình | SC-M04-006/E1 | END:SUCCESS |
| UC-M04-006 | Tác giả mở khiếu nại cảnh cáo/ban của mình liên quan bình luận | SC-M04-006/E2 | END:SUCCESS |
| UC-M04-006 | Người mở khác tác giả | SC-M04-006/E3 | END:REJECTED |
| UC-M04-006 | Không có ngữ cảnh thông báo/khiếu nại hợp lệ về đúng bình luận | SC-M04-006/E4 | END:REJECTED |


Truy vết ngược ở sources của từng bước. E thay bước trong đường chính; V thay toàn bộ đường theo actor khởi tạo khác trong cùng mục tiêu, không tạo BF mới. Cùng guard lặp lại khi sửa vẫn áp cùng kiểm; không nhân vô hạn số lần. Nguồn có ID/đích tồn tại không tự chứng minh mọi chi tiết đúng nghiệp vụ.

## 7. Điểm đã chốt, giới hạn và QA

| ID | Nguồn và giới hạn | Cách xử lý |
|---|---|---|
| TBD-M04-01 — Đã đóng | FR1.3/DEC-201; FR-M09-08.15 | Lật cảnh cáo/ban không làm bình luận Bị ẩn hiện lại; không coi đây là TBD mở. |
| NOTE-M04-01 | Nhãn đường xem lại cho biết bình luận đang bị ẩn, câu chữ HMI chưa chốt | Ghi đúng ý nghĩa nhãn/chỉ đọc, không sáng tác câu thông báo chính thức. |
| NOTE-M04-02 | Hai câu thay thế khác nhau | Gốc: [Bình luận đã bị xóa]; trích dẫn: trả lời [bình luận đã bị xóa]. |
| NOTE-M04-03 | Cách cắt dòng và lỗi gửi/lưu kỹ thuật chưa đủ nguồn | Trích tối đa một dòng theo phần đầu, không gán số ký tự cố định; không tự thêm retry/rollback/timeout hoặc nút xác nhận. |
| NOTE-M04-04/05 | Xem lại không gỡ ẩn; M04 không là Feed/cổng M03 | Không tạo khiếu nại bình luận, lịch sử sửa, khôi phục, quét trước đăng hoặc actor AI. |


Đường có đủ nguồn đã triển khai, không phát sinh quyết định nghiệp vụ thay FR/US/register. Kết quả kiểm, ma trận điều kiện và lệnh ở [QA-M04.md](QA-M04.md). Chưa có phê duyệt nội dung cuối.
