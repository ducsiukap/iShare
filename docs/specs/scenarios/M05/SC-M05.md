# Kịch bản nghiệp vụ — M05 Topic & Tag

[Vietnamese Doc] — Tái kiểm 11/11/2026 — Skill scenarios v1.4.

Mục đích: từ FR/US triển khai các chức năng actor thực hiện hoàn chỉnh với iShare thành scenario sáu phần. Boundary là toàn iShare; M01/M03/M06/M07/M08/M10/M13/M14 là phần nội bộ SYSTEM. ACT-006 là dịch vụ AI ngoài hệ thống hỗ trợ theo yêu cầu tác giả, không phải actor khởi tạo BF.

**Trong phạm vi:** toàn bộ catalog M05 gồm 4 UC chính, 11 UC con, 12 mapping; 9 chức năng actor: chốt Topic, chốt Tag, đọc danh mục/nhãn, thêm/gộp/xóa Topic, vô hiệu/kích hoạt Tag, đổi phân loại bài người khác. UC002 gợi ý, UC012 kiểm/chuẩn hóa và hợp đồng core020 được khai triển trong các hành trình bao chứa. Trending và các AUT có bảng quy tắc nền, không tạo scenario chỉ SYSTEM.

**Ngoài phạm vi:** sản xuất lại FR/US/UML; cổng công bố/quét/duyệt/nội dung bài M03/M11, tìm/lọc/autocomplete M06, Follow/thông báo M07, màn hình/log Admin M10, log thô/đánh giá AI M13, tab Trending M14, thống kê M15. Chỉ ghi hợp đồng giao tiếp cần để hoàn tất phân loại/quản trị. Không thêm AI Tag, Topic con/đổi tên, sửa/gộp/xóa Tag, nhãn comment hay thông báo cho tác giả khi Mod đổi phân loại.

**Trạng thái:** Đang soạn để review; FR-M05 đã chốt 1.7, US-M05/overview còn Chờ duyệt. Việc lưu ở thư mục yêu cầu không là phê duyệt. Các NOTE/TBD được giữ ở mục 7; không tự bù chính sách UI/log/lỗi hạ tầng.

## 1. Baseline, actor và dữ liệu

<!-- sc:document -->

| key | value |
|---|---|
| module | M05 |
| scope | ALL |
| skill_version | 1.4 |
| output_dir | docs/specs/scenarios/M05 |
| status | Đang soạn |
| completed_steps | 1, 2, 3, 4 |
| date | 2026-11-11 |
| approval_evidence | - |


| Nguồn | Version | Ngày | Trạng thái | SHA-256 | Vai trò |
|---|---|---|---|---|---|
| [docs/specs/fr/FR-M05.md](../../fr/FR-M05.md) | 1.7 | 2026-10-24 | Đã chốt | eb85b5dcb56995d791ed28a8d72a2f91c95588d8cd8d4fb1e74a8aabc2d701aa | Yêu cầu owner |
| [docs/specs/us/US-M05.md](../../us/US-M05.md) | Không có version tài liệu; skill 2.2 | 2026-10-30 | Chờ duyệt | 6b2b6b9837cf889e795fedabff159dccb580d7eef3069efa4d6682b961385fdc | Mô hình module |
| [docs/specs/us/US-overview.md](../../us/US-overview.md) | 1.1 | 2026-11-02 | Chờ duyệt | c1d624b7036ea2c7a9968eaa46c482c04fa1a15e2554d536cdfc12f177e26e33 | Boundary |
| [docs/specs/fr/FR-M01.md](../../fr/FR-M01.md) | 1.10 | 2026-10-24 | Đã chốt | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a | Hợp đồng giao tiếp, không mở rộng scope |
| [docs/specs/fr/FR-M03.md](../../fr/FR-M03.md) | 1.10 | 2026-10-24 | Đã chốt | fc996ec5520b6485277fca6a3dbae018bfce02263aba8e15ea87871f35865980 | Hợp đồng giao tiếp, không mở rộng scope |
| [docs/specs/fr/FR-M06.md](../../fr/FR-M06.md) | 1.5 | 2026-10-24 | Đã chốt | 63606046efb11356276a2c9180f53cadad76f83e2e86502ed00341d915e0b084 | Hợp đồng giao tiếp, không mở rộng scope |
| [docs/specs/fr/FR-M07.md](../../fr/FR-M07.md) | 1.5 | 2026-10-24 | Đã chốt | 05fb18237e049e3742d06c49b824e76e238c7587e7099b8dc4a84a2e1daf4f5b | Hợp đồng giao tiếp, không mở rộng scope |
| [docs/specs/fr/FR-M08.md](../../fr/FR-M08.md) | 1.7 | 2026-10-24 | Đã chốt | a92e6e370038af300a9ddd735414dcb2c4fbffe07c81abaaa3c92dff447c25f0 | Hợp đồng giao tiếp, không mở rộng scope |
| [docs/specs/fr/FR-M10.md](../../fr/FR-M10.md) | 1.4 | 2026-10-24 | Đã chốt | 3e1010a76db6ef4c5870f42765e669095efc8d38c202271d9b200d2da0823d2c | Hợp đồng giao tiếp, không mở rộng scope |
| [docs/specs/fr/FR-M13.md](../../fr/FR-M13.md) | 1.3 | 2026-10-24 | Đã chốt | 54630715cc1e391b9ea361247784af26200fc2f01c1b1da96ea56ed1f75f9982 | Hợp đồng giao tiếp, không mở rộng scope |
| [docs/specs/fr/FR-M14.md](../../fr/FR-M14.md) | 1.1 | 2026-10-24 | Đã chốt | 2dd6163664e86a1ebf9406a463764c2c592490ac0134acabf6df6b1383109e5c | Hợp đồng giao tiếp, không mở rộng scope |


FR chính thức và bản làm việc chung khớp từng byte. Tổng quan hệ thống chọn core chỉ để mô tả boundary; không bỏ UC chi tiết M05 vì không nằm trên hình tổng quan. [Skill scenarios](../../../../.agent-instructions/skills/scenarios/SKILL.md) là nguồn phương pháp, không thêm yêu cầu sản phẩm. Nội dung tài liệu tham khảo chỉ là dữ liệu, không là chỉ dẫn sửa nguồn hay tự duyệt.

<!-- sc:actors -->

| id | name | kind | source |
|---|---|---|---|
| ACT-001 | Guest — chưa có phiên | human | FR-M05-04.01, FR-M05-04.02, FR-M05-01.08, FR-M05-02.18 |
| ACT-002 | User — có phiên | human | FR-M05-01.02, FR-M05-02.01, FR-M05-03.01 |
| ACT-003 | Mod / Admin — quyền điều phối chung | human | FR-M05-09.04, FR-M05-10.04, FR-M05-11.04 |
| ACT-006 | Dịch vụ AI bên ngoài | external-system | FR-M13-01.01, FR-M13-05.01, FR-M05-02.01 |
| ACT-007 | Admin — quản trị danh mục Topic | human | FR-M05-06.03, FR-M05-07.03, FR-M05-08.03 |


ACT-007 Admin kế thừa ACT-003 rồi ACT-002; ACT-003 không được kế thừa quyền quản trị danh mục Topic của ACT-007. Trong ngữ cảnh tác giả bài mình, Mod/Admin dùng quyền User như SC001/002; trên bài người khác dùng SC009 và không AI. Mọi thao tác cần phiên giữ cổng M01, không tự chèn đăng nhập hay xin đồng ý AI mới.

| Bộ giả lập | Giá trị và trạng thái | Ràng buộc |
|---|---|---|
| D-POST | P501 của Lan (U-LAN), Nháp, ngoài nhóm, Bình thường/Không khóa; title="Vận dụng định lý Bayes"; body="Bài viết trình bày cách tính xác suất có điều kiện bằng ví dụ rút bóng và giải thích từng bước tính."; Lớp=12; poll=không; tệp=bayes.pdf (PDF 1 MB); Tag=[]; Topic ban đầu=[]; title+body=27 từ | Nội dung hợp lệ để cô lập quy tắc M05, không thay FR-M03 |
| D-CAT | Toán học; Ngữ văn; Ngoại ngữ; Khoa học tự nhiên (Lý/Hóa/Sinh); Khoa học xã hội (Sử/Địa/KT&PL); Tin học; Kỹ năng mềm; Hướng nghiệp; Nghệ thuật & Sáng tạo; Góc Chill; Khác | BR-M05-01, BR-M05-02; có thể thêm Topic sau, không có tầng con |
| D-TAG | #bayes hoạt động, #xácsuất hoạt động, #abc bị vô hiệu hóa; #xácsuất và #xacsuat là hai Tag khác nhau | BR-M05-20, BR-M05-24, BR-M05-26 |
| D-MERGE | P510/P511/P512, tập follow U1/U2/U3 được ghi ngay SC005/M1 | BR-M05-09 |
| D-DELETE | Thử nghiệm chỉ có P520/P521 Nháp, 2 lượt theo dõi | BR-M05-08 |
| D-ROLE | Lan=User, Mai=Mod, An=Admin; tên/ID giả lập | Actor ID theo US, không dùng dữ liệu cá nhân thật |


Các bộ/nhánh là snapshot độc lập, không bắt tạo/gộp/xóa cùng đối tượng nối tiếp. Thời gian minh họa09/11/2026, UTC+7 trừ khi ghi khác. # là ký hiệu hiển thị, không tính vào độ dài tên Tag; chuỗi a×30/a×31 mô tả tên cụ thể lặp đúng số ký tự. Cổng nội dung khác đạt ở bộ chuẩn; gợi ý kiểm từ bằng khoảng trắng, không tính tệp.

## 2. Kiểm kê nhóm UC chi tiết

<!-- sc:decomposition -->

| core | sub | source |
|---|---|---|
| UC-M05-020 | UC-M05-001 | FR-M05-01, BR-M05-03, BR-M05-04 |
| UC-M05-020 | UC-M05-002 | FR-M05-02, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-13, BR-M05-14, BR-M05-17, BR-M05-18, BR-M05-19 |
| UC-M05-020 | UC-M05-003 | FR-M05-03, BR-M05-20, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-26 |
| UC-M05-020 | UC-M05-012 | FR-M05-01, FR-M05-03, FR-M05-11.01, FR-M05-11.02, FR-M05-11.03, BR-M05-03, BR-M05-04, BR-M05-20, BR-M05-22, BR-M05-23, BR-M05-24 |
| UC-M05-021 | UC-M05-004 | FR-M05-04, BR-M05-01, BR-M05-02, BR-M05-26 |
| UC-M05-022 | UC-M05-006 | FR-M05-06, BR-M05-01, BR-M05-05, BR-M05-06, BR-M05-07 |
| UC-M05-022 | UC-M05-007 | FR-M05-07, BR-M05-09 |
| UC-M05-022 | UC-M05-008 | FR-M05-08, BR-M05-08 |
| UC-M05-023 | UC-M05-009 | FR-M05-09, BR-M05-25, BR-M05-26 |
| UC-M05-023 | UC-M05-010 | FR-M05-10, BR-M05-25, BR-M05-27 |
| UC-M05-023 | UC-M05-011 | FR-M05-11, FR-M05-02.21, BR-M05-04, BR-M05-20, BR-M05-24 |
| UC-M05-023 | UC-M05-012 | FR-M05-01, FR-M05-03, FR-M05-11.01, FR-M05-11.02, FR-M05-11.03, BR-M05-03, BR-M05-04, BR-M05-20, BR-M05-22, BR-M05-23, BR-M05-24 |


<!-- sc:ucs -->

| id | treatment | scenarios | coverage | rationale | sources |
|---|---|---|---|---|---|
| UC-M05-020 | embedded | SC-M05-001, SC-M05-002 | SC-M05-001/M4, SC-M05-002/M4 | Giữ nguyên mức User goal của core020, không gọi core là abstract/Summary. Hợp đồng chốt cả Topic/Tag được triển khai tại hai chức năng con, không tạo BF core trùng hành trình; Tag rỗng vẫn được xử lý. | FR-M05-01, FR-M05-02, FR-M05-03, BR-M05-03, BR-M05-04, BR-M05-22 |
| UC-M05-021 | aggregate | SC-M05-003 | SC-M05-003/M2 | Core Summary tổng hợp chức năng con độc lập; không bắt actor làm tất cả nối tiếp. | FR-M05-04, FR-M05-05, BR-M05-01, BR-M05-29, BR-M05-30, BR-M05-31 |
| UC-M05-022 | aggregate | SC-M05-004, SC-M05-005, SC-M05-006 | SC-M05-004/M2, SC-M05-005/M2, SC-M05-006/M2 | Core Summary tổng hợp chức năng con độc lập; không bắt actor làm tất cả nối tiếp. | FR-M05-06, FR-M05-07, FR-M05-08, BR-M05-05, BR-M05-08, BR-M05-09 |
| UC-M05-023 | aggregate | SC-M05-007, SC-M05-008, SC-M05-009 | SC-M05-007/M2, SC-M05-008/M2, SC-M05-009/M4 | Core Summary tổng hợp chức năng con độc lập; không bắt actor làm tất cả nối tiếp. | FR-M05-09, FR-M05-10, FR-M05-11, BR-M05-04, BR-M05-25, BR-M05-26, BR-M05-27 |
| UC-M05-001 | scenario | SC-M05-001, SC-M05-002 | SC-M05-001/M4, SC-M05-002/M4 | Actor yêu cầu một chức năng độc lập, tương tác đến kết quả; các trạng thái/phương thức/lỗi nằm trong mục 6. | FR-M05-01, BR-M05-03, BR-M05-04 |
| UC-M05-002 | embedded | SC-M05-001 | SC-M05-001/E10.2 | Gợi ý là phương thức bổ sung ở EP-TOPIC-SUGGEST của chức năng chốt Topic; triển khai đầy đủ gọi/nhận/chọn cuối/lưu trong SC001, không tạo BF chỉ nhận kết quả AI. | FR-M05-02, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-13, BR-M05-14, BR-M05-17, BR-M05-18, BR-M05-19 |
| UC-M05-003 | scenario | SC-M05-001, SC-M05-002 | SC-M05-001/M4, SC-M05-002/M4 | Actor yêu cầu một chức năng độc lập, tương tác đến kết quả; các trạng thái/phương thức/lỗi nằm trong mục 6. | FR-M05-03, BR-M05-20, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-26 |
| UC-M05-004 | scenario | SC-M05-003 | SC-M05-003/M2 | Actor yêu cầu một chức năng độc lập, tương tác đến kết quả; các trạng thái/phương thức/lỗi nằm trong mục 6. | FR-M05-04, BR-M05-01, BR-M05-02, BR-M05-26 |
| UC-M05-006 | scenario | SC-M05-004 | SC-M05-004/M2 | Actor yêu cầu một chức năng độc lập, tương tác đến kết quả; các trạng thái/phương thức/lỗi nằm trong mục 6. | FR-M05-06, BR-M05-01, BR-M05-05, BR-M05-06, BR-M05-07 |
| UC-M05-007 | scenario | SC-M05-005 | SC-M05-005/M2 | Actor yêu cầu một chức năng độc lập, tương tác đến kết quả; các trạng thái/phương thức/lỗi nằm trong mục 6. | FR-M05-07, BR-M05-09 |
| UC-M05-008 | scenario | SC-M05-006 | SC-M05-006/M2 | Actor yêu cầu một chức năng độc lập, tương tác đến kết quả; các trạng thái/phương thức/lỗi nằm trong mục 6. | FR-M05-08, BR-M05-08 |
| UC-M05-009 | scenario | SC-M05-007 | SC-M05-007/M2 | Actor yêu cầu một chức năng độc lập, tương tác đến kết quả; các trạng thái/phương thức/lỗi nằm trong mục 6. | FR-M05-09, BR-M05-25, BR-M05-26 |
| UC-M05-010 | scenario | SC-M05-008 | SC-M05-008/M2 | Actor yêu cầu một chức năng độc lập, tương tác đến kết quả; các trạng thái/phương thức/lỗi nằm trong mục 6. | FR-M05-10, BR-M05-25, BR-M05-27 |
| UC-M05-011 | scenario | SC-M05-009 | SC-M05-009/M4 | Actor yêu cầu một chức năng độc lập, tương tác đến kết quả; các trạng thái/phương thức/lỗi nằm trong mục 6. | FR-M05-11, FR-M05-02.21, BR-M05-04, BR-M05-20, BR-M05-24 |
| UC-M05-012 | embedded | SC-M05-001, SC-M05-002, SC-M05-009 | SC-M05-001/M4, SC-M05-002/M4, SC-M05-009/M4 | Kiểm/chuẩn hóa theo phần Topic/Tag của từng điểm gọi UC001/003/011; không có hành trình chuẩn hóa độc lập. | FR-M05-01, FR-M05-03, FR-M05-11.01, FR-M05-11.02, FR-M05-11.03, BR-M05-03, BR-M05-04, BR-M05-20, BR-M05-22, BR-M05-23, BR-M05-24 |


| Sơ đồ nguồn | Số UC | Đối chiếu |
|---|---|---|
| D-M05-CORE | 4 | ID thành viên khớp catalog/mapping nguồn; không vẽ lại hoặc thêm quan hệ |
| D-M05-020 | 5 | ID thành viên khớp catalog/mapping nguồn; không vẽ lại hoặc thêm quan hệ |
| D-M05-021 | 2 | ID thành viên khớp catalog/mapping nguồn; không vẽ lại hoặc thêm quan hệ |
| D-M05-022 | 4 | ID thành viên khớp catalog/mapping nguồn; không vẽ lại hoặc thêm quan hệ |
| D-M05-023 | 5 | ID thành viên khớp catalog/mapping nguồn; không vẽ lại hoặc thêm quan hệ |


## 3. Các luồng nghiệp vụ

<!-- sc:flows -->

| id | uc | primary | trigger | goal | completion | covered_ucs | rationale | scenario | sources |
|---|---|---|---|---|---|---|---|---|---|
| BF-M05-001 | UC-M05-001 | ACT-002 | Lan yêu cầu chọn Topic cho P501 đang soạn. | Gán và chốt Topic cho bài viết của mình | Topic cuối được lưu đúng bài và đúng sự kiện: nháp 0–3, gửi/lưu sửa đã gửi 1–3 Topic khác nhau thuộc danh mục; phần Tag hiện có 0–5 hợp lệ. Có gợi ý gần nhất còn hiệu lực khi gửi/lưu sửa thì ghi suggested/final; không ghi khi chưa dùng, lỗi thời hoặc chỉ lưu nháp. SUCCESS là hoàn thành phân loại, không phải quyết định công bố của M03. | UC-M05-001, UC-M05-002, UC-M05-003, UC-M05-012, UC-M05-020 | Actor yêu cầu và hoàn tất một chức năng; không tách riêng kiểm quyền/trạng thái/lời gọi AI hoặc phản hồi nội bộ. | SC-M05-001 | FR-M05-01.01, FR-M05-02.02, FR-M05-03.01, BR-M05-03, BR-M05-22, FR-M05-01.02, FR-M05-02.14, FR-M03-04.01, FR-M03-04.08, FR-M03-04.09, FR-M05-01.04, FR-M05-01.05, FR-M05-01.03, FR-M05-01.09, FR-M05-01.10, BR-M05-16, FR-M03-01.01, FR-M05-01.06, BR-M05-04, FR-M03-11.01, FR-M03-11.07, FR-M05-01.07, FR-M05-02.12, FR-M05-02.13, FR-M03-11.02, FR-M05-02.01, BR-M05-10, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.04, FR-M05-02.06, FR-M05-02.07, FR-M05-02.08, BR-M05-19, FR-M13-01.06, FR-M13-01.07, FR-M13-05.03, FR-M05-02.17, FR-M10-09.03, FR-M10-09.04, FR-M10-09.07, FR-M13-05.04, FR-M13-08.01, FR-M13-08.02, FR-M05-02.09, BR-M05-15, FR-M05-02.10, FR-M05-02.11, FR-M03-02.01, FR-M05-02.20, FR-M05-11.04, FR-M05-03.10, FR-M01-06.04, FR-M13-01.09, FR-M05-01.08, FR-M05-02.18 |
| BF-M05-002 | UC-M05-003 | ACT-002 | Lan yêu cầu gắn Tag cho P503 của mình. | Gắn và chốt Tag tự do cho bài viết của mình | Tập cuối 0–5 liên kết Tag được lưu cho bài đúng quyền; tên mới hợp lệ tự tạo hoạt động, tên đã có dùng lại, không trùng. Chỉ Tag hoạt động được hiển thị chữ thường kèm #; giữ liên kết cũ đang vô hiệu hóa nếu actor không yêu cầu bỏ. Phần nhập mới trùng tên Tag vô hiệu hóa chỉ là văn bản, không liên kết mới. Không thay đổi Topic nếu actor không yêu cầu. | UC-M05-001, UC-M05-003, UC-M05-012, UC-M05-020 | Actor yêu cầu và hoàn tất một chức năng; không tách riêng kiểm quyền/trạng thái/lời gọi AI hoặc phản hồi nội bộ. | SC-M05-002 | FR-M05-03.01, FR-M05-03.11, BR-M05-20, BR-M05-22, BR-M05-23, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.05, FR-M05-03.06, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-21, BR-M05-24, BR-M05-26, FR-M05-01.02, FR-M05-03.10, FR-M03-11.01, FR-M03-11.07, FR-M05-02.12, FR-M05-02.13, FR-M05-02.14, BR-M05-16, FR-M03-11.02, FR-M05-01.03, FR-M05-01.09, BR-M05-03, FR-M05-11.04, FR-M05-01.06, FR-M01-06.04, FR-M05-04.05, FR-M05-09.03, BR-M05-04, FR-M05-03.12 |
| BF-M05-003 | UC-M05-004 | ACT-001 | Guest mở danh sách Topic. | Xem danh mục và nhãn phân loại Topic, Tag | Trả đúng tập danh mục hoặc nhãn phân loại theo yêu cầu đọc và quyền bài: Topic hiện hành, Tag chỉ hoạt động; nhãn bài chỉ hiện Tag hoạt động còn liên kết. Không sửa phân loại, không tạo phiên hoặc tự mở thao tác quản trị. | UC-M05-004 | Actor yêu cầu và hoàn tất một chức năng; không tách riêng kiểm quyền/trạng thái/lời gọi AI hoặc phản hồi nội bộ. | SC-M05-003 | FR-M05-04.01, FR-M05-04.06, BR-M05-01, BR-M05-02, FR-M05-05.10, FR-M05-04.02, FR-M05-04.03, FR-M05-03.14, BR-M05-26, FR-M05-04.04, FR-M05-04.05, FR-M03-07.01, FR-M03-07.02 |
| BF-M05-004 | UC-M05-006 | ACT-007 | Admin An gửi yêu cầu thêm Topic Tài chính cá nhân. | Thêm Topic mới vào danh mục hệ thống | Một Topic mới ngang cấp được thêm nếu không trùng; có trong danh mục để chọn thủ công và AI gợi ý, không tự gán bài cũ, không giới hạn số Topic; log thao tác Admin theo M10. | UC-M05-006 | Actor yêu cầu và hoàn tất một chức năng; không tách riêng kiểm quyền/trạng thái/lời gọi AI hoặc phản hồi nội bộ. | SC-M05-004 | FR-M05-06.01, FR-M05-06.03, FR-M05-06.04, FR-M05-06.05, FR-M05-06.06, FR-M05-06.07, FR-M05-06.08, BR-M05-01, BR-M05-05, BR-M05-06, BR-M05-07, FR-M10-14.01, FR-M10-14.02, FR-M10-14.09, FR-M05-06.02 |
| BF-M05-005 | UC-M05-007 | ACT-007 | Admin An yêu cầu gộp Tin hoc vào Tin học. | Gộp Topic nguồn vào Topic đích | Mọi liên kết bài nguồn được thay bằng đích, mỗi bài chỉ có đích một lần; follow nguồn chuyển sang đích không trùng; nguồn bị bỏ khỏi danh mục và có log Admin. Không mất bài vì nguồn đang có bài ngoài nháp; đây là gộp, không là xóa độc lập. | UC-M05-007 | Actor yêu cầu và hoàn tất một chức năng; không tách riêng kiểm quyền/trạng thái/lời gọi AI hoặc phản hồi nội bộ. | SC-M05-005 | FR-M05-07.01, FR-M05-07.02, FR-M05-07.03, FR-M05-07.05, FR-M05-07.06, BR-M05-09, FR-M10-14.01, FR-M10-14.02, FR-M10-14.09, FR-M05-07.04 |
| BF-M05-006 | UC-M05-008 | ACT-007 | Admin An yêu cầu xóa Topic Thử nghiệm. | Xóa Topic không có bài viết ngoài nháp | Topic đủ điều kiện không còn danh mục/được chọn/gợi ý; bỏ khỏi nháp và bỏ mọi follow; nháp còn 0 Topic vẫn hợp lệ. Có log Admin. Không xóa bài để hợp thức hóa việc xóa Topic. | UC-M05-008 | Actor yêu cầu và hoàn tất một chức năng; không tách riêng kiểm quyền/trạng thái/lời gọi AI hoặc phản hồi nội bộ. | SC-M05-006 | FR-M05-08.01, FR-M05-08.03, FR-M05-08.04, FR-M05-08.05, FR-M05-08.06, BR-M05-08, FR-M10-14.01, FR-M10-14.02, FR-M10-14.09, FR-M05-08.02, FR-M03-17.02 |
| BF-M05-007 | UC-M05-009 | ACT-003 | Mod Mai yêu cầu vô hiệu hóa #abc, có thể kèm lý do. | Vô hiệu hóa Tag trong tình huống khủng hoảng | Tag bị vô hiệu hóa, vẫn tồn tại cùng liên kết cũ, không hiển thị/gắn mới dưới dạng Tag. Ghi nhật ký kiểm duyệt cho thao tác có thay đổi theo nguồn; nếu người thực hiện là Admin có thêm nhật ký Admin. Yêu cầu lặp giữ trạng thái theo nhánh, không tự cam kết log lặp ngoài nguồn. | UC-M05-009 | Actor yêu cầu và hoàn tất một chức năng; không tách riêng kiểm quyền/trạng thái/lời gọi AI hoặc phản hồi nội bộ. | SC-M05-007 | FR-M05-09.01, FR-M05-09.02, FR-M05-09.03, FR-M05-09.07, FR-M05-03.09, FR-M05-04.03, FR-M05-04.05, FR-M05-05.07, BR-M05-26, FR-M08-16.02, FR-M06-03.04, FR-M05-09.05, FR-M05-09.04, FR-M01-06.04, FR-M10-14.01, FR-M10-14.02, FR-M10-14.03, FR-M10-14.09 |
| BF-M05-008 | UC-M05-010 | ACT-003 | Mod Mai yêu cầu kích hoạt lại #abc. | Kích hoạt lại Tag đã vô hiệu hóa | Tag hoạt động; các liên kết cũ còn giữ được hiển thị lại, phần chữ nhập khi vô hiệu không tự thành liên kết. Có log kiểm duyệt và thêm log Admin nếu Admin thực hiện; Trending vẫn theo kỳ tính gần nhất và điều kiện điểm>0, không tự tính realtime. | UC-M05-010 | Actor yêu cầu và hoàn tất một chức năng; không tách riêng kiểm quyền/trạng thái/lời gọi AI hoặc phản hồi nội bộ. | SC-M05-008 | FR-M05-10.01, FR-M05-10.02, FR-M05-10.03, FR-M05-10.06, FR-M05-05.10, FR-M05-05.14, BR-M05-27, BR-M05-30, BR-M05-31, FR-M08-16.02, FR-M05-10.05, FR-M05-05.07, FR-M05-10.04, FR-M01-06.04, FR-M10-14.01, FR-M10-14.02, FR-M10-14.03, FR-M10-14.09 |
| BF-M05-009 | UC-M05-011 | ACT-003 | Mod Mai yêu cầu đổi phân loại P540 của Lan. | Đổi Topic và Tag trên bài viết của người khác | Phân loại hợp lệ cuối được lưu: Topic 1–3 hiện hành, Tag 0–5 chuẩn hóa; không AI trên bài người khác, không báo tác giả/không lịch sử sửa công khai. Có log kiểm duyệt; Admin làm cùng thao tác còn có log Admin; các trường nội dung không thuộc quyền đổi phân loại giữ nguyên. | UC-M05-011, UC-M05-012 | Actor yêu cầu và hoàn tất một chức năng; không tách riêng kiểm quyền/trạng thái/lời gọi AI hoặc phản hồi nội bộ. | SC-M05-009 | FR-M05-11.01, FR-M05-11.02, FR-M05-11.04, FR-M05-02.21, FR-M03-11.04, FR-M03-11.07, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-01.01, FR-M05-01.02, FR-M05-01.03, FR-M05-01.04, FR-M05-01.05, FR-M05-01.07, FR-M05-01.09, FR-M05-01.10, BR-M05-03, BR-M05-04, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.05, FR-M05-03.06, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-20, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-26, FR-M08-16.02, FR-M03-11.05, FR-M03-11.06, FR-M05-11.03, FR-M01-06.04, FR-M05-09.03, FR-M05-04.05, FR-M10-14.01, FR-M10-14.02, FR-M10-14.03, FR-M10-14.09 |


SC001/002 cho phép tác giả chủ động chốt Topic hoặc Tag độc lập; trong lần lưu/gửi vẫn kiểm hợp đồng phân loại với phần còn lại hiện có, kể cả Tag rỗng. Lưu nháp/sửa bài, AI/thủ công, vai trò, dữ liệu và lỗi không tự thành BF mới. SC003 hoàn thành một yêu cầu đọc danh mục hoặc nhãn; không ép phải đọc cả danh mục lẫn bài. SC004/005/006 là ba chức năng quản trị độc lập; SC007/008 là hai yêu cầu trạng thái ở thời điểm khác nhau, không nối thành một lần bắt buộc.

| Quan hệ US giữ nguyên | Điểm hợp đồng | Trở về |
|---|---|---|
| UC-M05-020 include UC-M05-001 | #uc-m05-020-main-2 | #uc-m05-020-main-3 |
| UC-M05-020 include UC-M05-003 | #uc-m05-020-main-3 | #uc-m05-020-main-4 |
| UC-M05-001 include UC-M05-012 | #uc-m05-001-main-3 | #uc-m05-001-main-4 |
| UC-M05-003 include UC-M05-012 | #uc-m05-003-main-2 | #uc-m05-003-main-3 |
| UC-M05-011 include UC-M05-012 | #uc-m05-011-main-2 | #uc-m05-011-main-3 |
| UC-M05-002 extend UC-M05-001 | EP-TOPIC-SUGGEST | #uc-m05-001-main-2 |


Include được triển khai trực tiếp ở lượt SYSTEM kiểm/chốt phân loại, không che bằng câu gọi UC. Extend UC002 chỉ tại EP-TOPIC-SUGGEST sau tác giả bấm, trở về quyết định tập Topic cuối và lưu/gửi. Gộp Topic không include xóa độc lập vì điều kiện khác nhau.

## 4. Scenario sáu phần

<a id="sc-m05-001"></a>

<!-- sc:scenario SC-M05-001 -->

### SC-M05-001

#### 1. Tên kịch bản chuẩn

Gán và chốt Topic cho bài viết của mình — BF-M05-001. UC owner: [UC-M05-001](../../us/US-M05.md#uc-m05-001). Trigger: Lan yêu cầu chọn Topic cho P501 đang soạn.

#### 2. Actor thực hiện

ACT-002 — User — có phiên là actor chính. ACT-006 là dịch vụ ngoài hỗ trợ trong các nhánh gợi ý, không quyết định Topic cuối; M13 vẫn là SYSTEM. Các quyền kế thừa giữ đúng actor hierarchy của US. Đường E tại M1 thay toàn bộ khi actor khởi tạo khác, không đổi vai trò giữa luồng.

#### 3. Tiền điều kiện

Có ngữ cảnh soạn/sửa bài của tác giả; đường chuẩn là Lan có phiên hợp lệ, mức LIGHT, P501 ở D-POST. Danh mục/quyền và dữ liệu được kiểm ở lúc thao tác, không giả định mọi lựa chọn đều hợp lệ. M03 giữ cổng lưu/gửi nội dung; các phần nội dung khác của bộ minh họa hợp lệ.

#### 4. Hậu điều kiện

<!-- sc:post SC-M05-001 -->

| result | condition |
|---|---|
| SUCCESS | Topic cuối được lưu đúng bài và đúng sự kiện: nháp 0–3, gửi/lưu sửa đã gửi 1–3 Topic khác nhau thuộc danh mục; phần Tag hiện có 0–5 hợp lệ. Có gợi ý gần nhất còn hiệu lực khi gửi/lưu sửa thì ghi suggested/final; không ghi khi chưa dùng, lỗi thời hoặc chỉ lưu nháp. SUCCESS là hoàn thành phân loại, không phải quyết định công bố của M03. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không ghi nhận kết quả thành công của yêu cầu bị từ chối; không cấp thêm quyền hay tự sửa dữ liệu phân loại để vượt điều kiện. Các hiệu ứng đã hoàn tất trước yêu cầu này không bị suy thành rollback. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M05-001 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan yêu cầu chọn Topic cho P501 đang soạn. | P501 của Lan (U-LAN), Nháp, ngoài nhóm, Bình thường/Không khóa; title="Vận dụng định lý Bayes"; body="Bài viết trình bày cách tính xác suất có điều kiện bằng ví dụ rút bóng và giải thích từng bước tính."; Lớp=12; poll=không; tệp=bayes.pdf (PDF 1 MB); Tag=[]; Topic ban đầu=[] | M2 | FR-M05-01.01 |
| M2 | SYSTEM | Hệ thống kiểm phiên và quyền tác giả, trả danh mục Topic hiện tại để chọn thủ công; chỉ cung cấp gợi ý khi tác giả bấm Gợi ý topic. Xử lý phần Tag hiện có rỗng trong hợp đồng phân loại, không bắt nhập Tag. | Danh mục D-CAT; Topic=[]; Tag=[]; chưa có lượt gợi ý | M3 | FR-M05-01.01, FR-M05-02.02, FR-M05-03.01, BR-M05-03, BR-M05-22 |
| M3 | ACT-002 | Lan chọn Toán học và Tin học rồi gửi bài. | P501; Topic={Toán học, Tin học}; Tag=[]; title/body/tệp D-POST giữ nguyên | M4 | FR-M05-01.02, BR-M05-03 |
| M4 | SYSTEM | Hệ thống kiểm danh mục hiện tại, số lượng và trùng Topic, xử lý tập Tag rỗng hợp lệ; lưu chính tập Topic tác giả vừa gửi và trả kết quả phân loại đã được ghi nhận. Không ghi phản hồi gợi ý vì các đường nhập vào M4 chưa có gợi ý thành công; M03 tiếp nhận bài ở Chờ duyệt khi Moderation bật, không khẳng định bài đã được công bố. | Đường chuẩn P501.Topic={Toán học, Tin học}; nếu nhập lại M4 từ nhánh, dùng đúng tập Topic/title/body của bước actor gửi gần nhất trong nhánh, không thay bằng tập chuẩn. Tag=[]; phản hồi=không; trạng thái tiếp nhận=Chờ duyệt | END:SUCCESS | FR-M05-01.02, FR-M05-03.01, FR-M05-02.14, BR-M05-03, BR-M05-22, FR-M03-04.01, FR-M03-04.08, FR-M03-04.09 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Bộ dữ liệu trong guard thay bộ chuẩn cho lần chạy đó; mỗi nhánh là snapshot riêng. Điểm nhập lại nêu rõ bước kiểm; nếu dữ liệu còn sai áp lại guard, không tự giới hạn số lần. REJECTED là kết thúc từ chối hợp lệ của US; không bịa nút OK/hủy/thử lại hay rollback lỗi lưu trữ chưa có nguồn.

<!-- sc:exceptions SC-M05-001 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M3 | Lan chọn Topic thứ tư sau ba Topic khác nhau | E1.1 | FR-M05-01.04, BR-M05-03, FR-M05-01.02, FR-M05-03.01, FR-M05-02.14, BR-M05-22, FR-M03-04.01, FR-M03-04.08, FR-M03-04.09 |
| E2 | user-choice | M3 | Lan chọn lặp lại một Topic đã chọn | E2.1 | FR-M05-01.05, BR-M05-03, FR-M05-01.02, FR-M05-03.01, FR-M05-02.14, BR-M05-22, FR-M03-04.01, FR-M03-04.08, FR-M03-04.09 |
| E3 | system | M4 | Gửi không có Topic nào | E3.1 | FR-M05-01.03, BR-M05-03 |
| E4 | system | M4 | Topic Tin học đã chọn bị xóa khỏi danh mục trước khi gửi; tác giả chọn lại | E4.1 | FR-M05-01.09, FR-M05-01.01, FR-M05-01.02, BR-M05-03 |
| E5 | user-choice | M3 | Lan chọn lưu nháp với 0 Topic thay vì gửi | E5.1 | FR-M05-01.10, BR-M05-03, BR-M05-16, FR-M03-01.01 |
| E6 | user-choice | M3 | Lan chọn lưu nháp với 3 Topic thay vì gửi | E6.1 | FR-M05-01.10, BR-M05-03, BR-M05-16, FR-M03-01.01 |
| E7 | user-choice | M1 | Tác giả đổi Topic khi sửa bài đã gửi của mình | E7.1 | FR-M05-01.06, BR-M05-04, FR-M03-11.01, FR-M03-11.07, FR-M05-01.07, FR-M05-03.01, FR-M05-02.12, FR-M05-02.13, FR-M05-02.14, BR-M05-16, FR-M03-11.02 |
| E8 | user-choice | M1 | Lưu sửa bài đã gửi với 0 Topic không hợp lệ | E8.1 | FR-M05-01.06, FR-M03-11.07, FR-M05-01.07, BR-M05-04 |
| E9 | user-choice | M1 | Lưu sửa bài đã gửi với 4 Topic không hợp lệ | E9.1 | FR-M05-01.06, FR-M03-11.07, FR-M05-01.07, BR-M05-04 |
| E10 | user-choice | M3 | Tác giả chủ động dùng gợi ý rồi bỏ/chọn thêm và gửi bài | E10.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.04, FR-M05-01.02, FR-M05-01.06, FR-M05-02.12, FR-M05-03.01, BR-M05-03, BR-M05-04, BR-M05-16 |
| E11 | user-choice | M3 | Tác giả giữ nguyên toàn bộ gợi ý hợp lệ khi gửi | E11.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.04, FR-M05-02.12, BR-M05-16, FR-M05-01.02 |
| E12 | user-choice | M3 | Tác giả bỏ mọi gợi ý nhưng chọn Topic khác hợp lệ trước khi gửi | E12.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.04, FR-M05-01.02, FR-M05-02.12, BR-M05-16 |
| E13 | system | M3 | AI trả một phần Topic không thuộc danh mục | E13.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.04, FR-M05-01.02, FR-M05-01.06, FR-M05-02.12, FR-M05-03.01, BR-M05-03, BR-M05-04, BR-M05-16 |
| E14 | system | M3 | Mọi Topic AI trả về đều ngoài danh mục hiện tại | E14.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.06, FR-M05-02.07, FR-M05-02.08, BR-M05-14, BR-M05-19, FR-M13-01.06, FR-M13-01.07, FR-M13-05.03, FR-M05-01.01, FR-M05-01.02, FR-M05-02.14 |
| E15 | system | M3 | Tác giả yêu cầu gợi ý khi AI tổng Tắt, Topic suggestion Bật | E15.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.16, FR-M05-02.17, BR-M05-18, FR-M10-09.03, FR-M10-09.04, FR-M10-09.07, FR-M13-05.04, FR-M05-01.02 |
| E16 | system | M3 | Tác giả yêu cầu gợi ý khi AI tổng Bật, Topic suggestion Tắt | E16.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.16, FR-M05-02.17, BR-M05-18, FR-M10-09.03, FR-M10-09.04, FR-M10-09.07, FR-M13-05.04, FR-M05-01.02 |
| E17 | system | M3 | Tác giả yêu cầu gợi ý khi cả hai công tắc Tắt | E17.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.16, FR-M05-02.17, BR-M05-18, FR-M10-09.03, FR-M10-09.04, FR-M10-09.07, FR-M13-05.04, FR-M05-01.02 |
| E18 | system | M3 | Tổng tiêu đề và nội dung chữ chỉ 19 từ; tác giả chọn thủ công | E18.1 | FR-M05-02.01, FR-M05-02.05, BR-M05-12, FR-M05-01.02 |
| E19 | user-choice | M3 | Tác giả bổ sung từ thứ 20 sau cảnh báo quá ngắn rồi yêu cầu lại | E19.1 | FR-M05-02.01, FR-M05-02.05, BR-M05-12, FR-M05-02.02, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.04, FR-M05-01.02, FR-M05-01.06, FR-M05-02.12, FR-M05-03.01, BR-M05-03, BR-M05-04, BR-M05-16 |
| E20 | system | M3 | Yêu cầu thứ 11 trong 60 giây gần nhất, tác giả chọn thủ công | E20.1 | FR-M05-02.15, BR-M05-17, FR-M05-01.02 |
| E21 | user-choice | M3 | Yêu cầu được phép khi yêu cầu cũ đã rời cửa sổ trượt | E21.1 | FR-M05-02.15, BR-M05-17, FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.04, FR-M05-01.02, FR-M05-01.06, FR-M05-02.12, FR-M05-03.01, BR-M05-03, BR-M05-04, BR-M05-16 |
| E22 | system | M3 | Lần thử đầu lỗi/quá 10 giây, lần thử lại đúng một lần thành công | E22.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.04, FR-M05-01.02, FR-M05-01.06, FR-M05-02.12, FR-M05-03.01, BR-M05-03, BR-M05-04, BR-M05-16 |
| E23 | system | M3 | Cả hai lần thử AI lỗi hoặc quá 10 giây, tác giả chọn thủ công | E23.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M05-02.06, FR-M05-02.07, FR-M05-02.08, BR-M05-14, BR-M05-19, FR-M13-01.06, FR-M13-01.07, FR-M13-05.03, FR-M13-08.01, FR-M13-08.02, FR-M05-01.02, FR-M05-02.14 |
| E24 | user-choice | M3 | Sau gợi ý, tác giả đổi tiêu đề rồi gửi mà không gợi ý lại | E24.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.09, BR-M05-15, FR-M05-02.10, FR-M05-02.11, FR-M05-02.04, FR-M05-01.02, FR-M05-02.13, BR-M05-16 |
| E25 | user-choice | M3 | Sau gợi ý, tác giả đổi nội dung chữ rồi gửi mà không gợi ý lại | E25.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.09, BR-M05-15, FR-M05-02.10, FR-M05-02.11, FR-M05-02.04, FR-M05-01.02, FR-M05-02.13, BR-M05-16 |
| E26 | user-choice | M3 | Gợi ý lỗi thời, tác giả bấm gợi ý lại và chốt tập cuối rõ ràng | E26.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.09, FR-M05-02.10, FR-M05-02.04, FR-M05-01.02, FR-M05-01.06, FR-M05-02.12, FR-M05-03.01, BR-M05-03, BR-M05-04, BR-M05-16 |
| E27 | user-choice | M3 | Tác giả thay tệp, không đổi tiêu đề/nội dung chữ sau gợi ý | E27.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.09, BR-M05-15, FR-M03-02.01, FR-M05-01.02, FR-M05-02.12, BR-M05-16 |
| E28 | user-choice | M1 | Tác giả dùng AI khi sửa bài đã gửi, sau đó lưu bản sửa | E28.1 | FR-M05-01.06, FR-M05-02.20, FR-M03-11.07, FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.04, FR-M05-01.02, FR-M05-02.12, FR-M05-03.01, BR-M05-03, BR-M05-04, BR-M05-16 |
| E29 | user-choice | M3 | Có gợi ý hợp lệ nhưng tác giả chỉ lưu nháp | E29.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-01.10, FR-M05-02.12, BR-M05-16 |
| E30 | system | M2 | User có phiên nhưng đang đổi phân loại bài người khác mà không là Mod/Admin | E30.1 | FR-M05-11.04 |
| E31 | system | M4 | User có phiên nhưng đang đổi phân loại bài người khác mà không là Mod/Admin | E31.1 | FR-M05-11.04 |
| E32 | user-choice | M1 | Tác giả yêu cầu sửa phân loại bài Chờ duyệt/Đã xóa hoặc Bị Mod ẩn | E32.1 | FR-M03-11.07 |
| E33 | user-choice | M1 | Trạng thái bài chuyển sang không cho sửa sau khi đã mở sửa hợp lệ | E33.1 | FR-M03-11.01, FR-M05-01.06, FR-M05-03.10, FR-M03-11.07 |
| E34 | system | M4 | Phiên đã hết hiệu lực và không làm mới được tại thời điểm ghi | E34.1 | FR-M01-06.04 |
| E35 | user-choice | M3 | Sau gợi ý hợp lệ, tác giả gửi tập cuối có 0 Topic không hợp lệ | E35.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.04, FR-M05-01.03, FR-M05-01.04, BR-M05-03, FR-M05-02.12, BR-M05-16 |
| E36 | user-choice | M3 | Sau gợi ý hợp lệ, tác giả gửi tập cuối có 4 Topic không hợp lệ | E36.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.04, FR-M05-01.03, FR-M05-01.04, BR-M05-03, FR-M05-02.12, BR-M05-16 |
| E37 | user-choice | M3 | Gợi ý đã lỗi thời, tác giả yêu cầu lại khi công tắc gợi ý đang tắt rồi chọn thủ công | E37.1 | FR-M05-02.01, BR-M05-10, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M13-05.02, FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M05-03.11, FR-M05-02.09, FR-M05-02.10, FR-M05-02.17, FR-M13-01.09, FR-M05-01.02, FR-M05-02.13, BR-M05-15, BR-M05-16 |
| E38 | system | M1 | ACT-001 — Guest chưa có phiên thử gán/đổi Topic. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E38.1 | FR-M05-01.08 |
| E39 | system | M1 | ACT-001 — Guest yêu cầu gợi ý Topic. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E39.1 | FR-M05-02.18 |


<!-- sc:branch SC-M05-001 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Lan thay đổi tập Topic đang chọn theo bộ dữ liệu của nhánh. | {Toán học, Tin học, Khác}+Góc Chill | E1.2 | FR-M05-01.04, BR-M05-03 |
| E1.2 | SYSTEM | Hệ thống từ chối Góc Chill là Topic thứ tư, giữ ba Topic đã chọn. | Tập sau kiểm: {Toán học, Tin học, Khác} | E1.3 | FR-M05-01.04, BR-M05-03 |
| E1.3 | ACT-002 | Lan chốt tập hợp lệ sau kiểm và gửi P501. | Topic={Toán học, Tin học, Khác}; Tag=[] | E1.4 | FR-M05-01.04, BR-M05-03, FR-M05-01.02 |
| E1.4 | SYSTEM | Hệ thống kiểm lại danh mục/số lượng, lưu tập Topic vừa chốt cho lần gửi hợp lệ; không có gợi ý nên không ghi phản hồi. Trả đúng tập đã lưu, M03 tiếp nhận Chờ duyệt. | P501.Topic là tập hợp lệ ở bước ngay trước, không tự thêm/bớt Topic khác | END:SUCCESS | FR-M05-01.02, FR-M05-03.01, FR-M05-02.14, BR-M05-03, BR-M05-22, FR-M03-04.01, FR-M03-04.08, FR-M03-04.09, FR-M05-01.04 |


<!-- sc:branch SC-M05-001 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | Lan thay đổi tập Topic đang chọn theo bộ dữ liệu của nhánh. | {Toán học, Tin học}+Toán học | E2.2 | FR-M05-01.05, BR-M05-03 |
| E2.2 | SYSTEM | Hệ thống giữ Toán học một lần, không tạo liên kết trùng. | Tập sau kiểm: {Toán học, Tin học} | E2.3 | FR-M05-01.05, BR-M05-03 |
| E2.3 | ACT-002 | Lan chốt tập hợp lệ sau kiểm và gửi P501. | Topic={Toán học, Tin học}; Tag=[] | E2.4 | FR-M05-01.05, BR-M05-03, FR-M05-01.02 |
| E2.4 | SYSTEM | Hệ thống kiểm lại danh mục/số lượng, lưu tập Topic vừa chốt cho lần gửi hợp lệ; không có gợi ý nên không ghi phản hồi. Trả đúng tập đã lưu, M03 tiếp nhận Chờ duyệt. | P501.Topic là tập hợp lệ ở bước ngay trước, không tự thêm/bớt Topic khác | END:SUCCESS | FR-M05-01.02, FR-M05-03.01, FR-M05-02.14, BR-M05-03, BR-M05-22, FR-M03-04.01, FR-M03-04.08, FR-M03-04.09, FR-M05-01.05 |


<!-- sc:branch SC-M05-001 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối gửi P501 thiếu Topic, không tự gán Khác hoặc coi gửi thành công. | Topic=[]; các phần nội dung khác vẫn hợp lệ | END:REJECTED | FR-M05-01.03, BR-M05-03 |


<!-- sc:branch SC-M05-001 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại và từ chối Topic Tin học đã bị xóa; không tự thay bằng Topic khác. | Chọn trước={Toán học, Tin học}; hiện tại không còn Tin học | E4.2 | FR-M05-01.09 |
| E4.2 | ACT-002 | Lan chọn Toán học còn tồn tại và gửi lại P501. | Topic={Toán học}; Tag=[]; nội dung giữ nguyên | M4 | FR-M05-01.01, FR-M05-01.02, BR-M05-03 |


<!-- sc:branch SC-M05-001 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-002 | Lan chọn tập Topic rồi lưu nháp P501. | Topic={}; Tag=[]; title/body không rỗng | E5.2 | FR-M05-01.10 |
| E5.2 | SYSTEM | Hệ thống kiểm tập Topic 0–3 thuộc danh mục, lưu nháp với đúng tập đã chọn; không tạo phản hồi gợi ý chỉ vì lưu nháp. | P501.Nháp; Topic={}; phản hồi=không | END:SUCCESS | FR-M05-01.10, BR-M05-03, BR-M05-16, FR-M03-01.01 |


<!-- sc:branch SC-M05-001 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-002 | Lan chọn tập Topic rồi lưu nháp P501. | Topic={Toán học, Tin học, Khác}; Tag=[]; title/body không rỗng | E6.2 | FR-M05-01.10 |
| E6.2 | SYSTEM | Hệ thống kiểm tập Topic 0–3 thuộc danh mục, lưu nháp với đúng tập đã chọn; không tạo phản hồi gợi ý chỉ vì lưu nháp. | P501.Nháp; Topic={Toán học, Tin học, Khác}; phản hồi=không | END:SUCCESS | FR-M05-01.10, BR-M05-03, BR-M05-16, FR-M03-01.01 |


<!-- sc:branch SC-M05-001 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | ACT-002 | Lan mở sửa phân loại P502 Đã đăng của mình. | P502 của Lan, Bình thường; Topic={Tin học}; Tag={bayes}; nội dung như D-POST | E7.2 | FR-M05-01.06 |
| E7.2 | SYSTEM | Hệ thống kiểm quyền và trạng thái sửa theo M03, trả Topic hiện có và danh mục hiện tại; không buộc dùng AI. | P502.Topic={Tin học}; Tag={bayes} | E7.3 | FR-M05-01.06, BR-M05-04, FR-M03-11.01, FR-M03-11.07 |
| E7.3 | ACT-002 | Lan bỏ Tin học, thêm Toán học và lưu bản sửa. | P502.Topic cuối={Toán học}; giữ Tag={bayes} | E7.4 | FR-M05-01.06 |
| E7.4 | SYSTEM | Hệ thống kiểm 1–3 Topic và tập Tag hiện có hợp lệ, lưu thay đổi phân loại; trả P502 có Toán học, không ghi phản hồi vì không dùng gợi ý. Các tác động sửa bài do M03 tiếp tục theo hợp đồng nguồn, không suy thành đường công bố mới của M05. | P502.Topic={Toán học}; Tag={bayes}; phản hồi=không | END:SUCCESS | FR-M05-01.06, FR-M05-01.07, FR-M05-03.01, FR-M05-02.12, FR-M05-02.13, FR-M05-02.14, BR-M05-16, BR-M05-04, FR-M03-11.02 |


<!-- sc:branch SC-M05-001 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | ACT-002 | Lan yêu cầu đổi Topic P502 của mình. | P502 Đã đăng/Bình thường; Topic trước={Tin học} | E8.2 | FR-M05-01.06 |
| E8.2 | SYSTEM | Hệ thống kiểm quyền/trạng thái sửa, trả tập hiện tại và danh mục. | Topic trước={Tin học}; Tag={bayes} | E8.3 | FR-M05-01.06, FR-M03-11.07 |
| E8.3 | ACT-002 | Lan gửi bản sửa có tập Topic vi phạm. | Topic=[] | E8.4 | FR-M05-01.07 |
| E8.4 | SYSTEM | Hệ thống từ chối lưu tập Topic vi phạm; không coi việc bỏ hết Topic hay vượt 3 là bản sửa hợp lệ. | P502 không nhận tập 0 Topic của lần lưu này | END:REJECTED | FR-M05-01.07, BR-M05-04 |


<!-- sc:branch SC-M05-001 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | ACT-002 | Lan yêu cầu đổi Topic P502 của mình. | P502 Đã đăng/Bình thường; Topic trước={Tin học} | E9.2 | FR-M05-01.06 |
| E9.2 | SYSTEM | Hệ thống kiểm quyền/trạng thái sửa, trả tập hiện tại và danh mục. | Topic trước={Tin học}; Tag={bayes} | E9.3 | FR-M05-01.06, FR-M03-11.07 |
| E9.3 | ACT-002 | Lan gửi bản sửa có tập Topic vi phạm. | Topic={Toán học, Tin học, Khác, Góc Chill} | E9.4 | FR-M05-01.07 |
| E9.4 | SYSTEM | Hệ thống từ chối lưu tập Topic vi phạm; không coi việc bỏ hết Topic hay vượt 3 là bản sửa hợp lệ. | P502 không nhận tập 4 Topic của lần lưu này | END:REJECTED | FR-M05-01.07, BR-M05-04 |


<!-- sc:branch SC-M05-001 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E10.2 | FR-M05-02.01, BR-M05-10 |
| E10.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI.  | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E10.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E10.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E10.4 | FR-M13-05.01, FR-M13-05.02 |
| E10.4 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E10.5 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E10.5 | ACT-002 | Lan quyết định tập cuối rồi gửi bài. | P501; Topic={Toán học, Hướng nghiệp}; bỏ Tin học; title/body không đổi sau gợi ý; Tag=[] | E10.6 | FR-M05-02.04, FR-M05-01.02, FR-M05-01.06, BR-M05-13 |
| E10.6 | SYSTEM | Hệ thống kiểm 1–3 Topic hiện hành và Tag rỗng, lưu tập tác giả chốt cho lần gửi; ghi phản hồi gợi ý còn hiệu lực rồi trả kết quả phân loại đã lưu. Không đợi Mod duyệt gợi ý. | P501; suggested={Toán học, Tin học}; final={Toán học, Hướng nghiệp}; phản hồi được ghi ở sự kiện gửi bài; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-01.02, FR-M05-01.06, FR-M05-02.04, FR-M05-02.12, FR-M05-03.01, BR-M05-03, BR-M05-04, BR-M05-13, BR-M05-16 |


<!-- sc:branch SC-M05-001 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E11.2 | FR-M05-02.01, BR-M05-10 |
| E11.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI.  | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E11.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E11.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E11.4 | FR-M13-05.01, FR-M13-05.02 |
| E11.4 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E11.5 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E11.5 | ACT-002 | Lan giữ Toán học, Tin học và gửi bài, không đổi tiêu đề/nội dung chữ. | suggested=final={Toán học, Tin học}; Tag=[] | E11.6 | FR-M05-02.04, FR-M05-02.12, BR-M05-13, BR-M05-16 |
| E11.6 | SYSTEM | Hệ thống kiểm và lưu Toán học, Tin học, ghi phản hồi suggested bằng final; trả kết quả phân loại cho lần gửi hợp lệ. | P501.Topic={Toán học, Tin học}; có phản hồi; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-01.02, FR-M05-02.12, BR-M05-16 |


<!-- sc:branch SC-M05-001 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E12.2 | FR-M05-02.01, BR-M05-10 |
| E12.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI.  | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E12.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E12.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E12.4 | FR-M13-05.01, FR-M13-05.02 |
| E12.4 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E12.5 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E12.5 | ACT-002 | Lan bỏ Toán học, Tin học, chọn Hướng nghiệp rồi gửi. | suggested={Toán học, Tin học}; final={Hướng nghiệp}; nội dung không đổi | E12.6 | FR-M05-02.04, BR-M05-13 |
| E12.6 | SYSTEM | Hệ thống lưu Hướng nghiệp và ghi phản hồi cả khi không giữ gợi ý nào; trả tập Topic đã lưu, không tự coi đây là gợi ý lỗi thời. | P501.Topic={Hướng nghiệp}; suggested={Toán học, Tin học}; final={Hướng nghiệp} | END:SUCCESS | FR-M05-01.02, FR-M05-02.12, BR-M05-16 |


<!-- sc:branch SC-M05-001 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E13.2 | FR-M05-02.01, BR-M05-10 |
| E13.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI.  | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E13.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E13.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Vật lý, Tin học} | E13.4 | FR-M13-05.01, FR-M13-05.02 |
| E13.4 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI. Loại Vật lý vì tên đó không có trong D-CAT; vẫn là lần có gợi ý hợp lệ. | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E13.5 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E13.5 | ACT-002 | Lan quyết định tập cuối rồi gửi bài. | P501; Topic={Toán học, Hướng nghiệp}; bỏ Tin học; title/body không đổi sau gợi ý; Tag=[] | E13.6 | FR-M05-02.04, FR-M05-01.02, FR-M05-01.06, BR-M05-13 |
| E13.6 | SYSTEM | Hệ thống kiểm 1–3 Topic hiện hành và Tag rỗng, lưu tập tác giả chốt cho lần gửi; ghi phản hồi gợi ý còn hiệu lực rồi trả kết quả phân loại đã lưu. Không đợi Mod duyệt gợi ý. | P501; suggested={Toán học, Tin học}; final={Toán học, Hướng nghiệp}; phản hồi được ghi ở sự kiện gửi bài; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-01.02, FR-M05-01.06, FR-M05-02.04, FR-M05-02.12, FR-M05-03.01, BR-M05-03, BR-M05-04, BR-M05-13, BR-M05-16 |


<!-- sc:branch SC-M05-001 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E14.2 | FR-M05-02.01, BR-M05-10 |
| E14.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI.  | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E14.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E14.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Vật lý} | E14.4 | FR-M13-05.01, FR-M13-05.02 |
| E14.4 | SYSTEM | Hệ thống loại Vật lý, coi lần gợi ý thất bại; hiện thông báo không chặn “Không thể gợi ý chủ đề lúc này, vui lòng chọn thủ công”, không tự chọn Topic. | Kết quả hợp lệ=[]; chưa có gợi ý thành công | E14.5 | FR-M05-02.06, FR-M05-02.07, FR-M05-02.08, BR-M05-14, BR-M05-19, FR-M13-01.06, FR-M13-01.07, FR-M13-05.03 |
| E14.5 | ACT-002 | Lan chọn Toán học thủ công và gửi P501. | Topic={Toán học}; Tag=[]; không dùng gợi ý thành công | M4 | FR-M05-01.01, FR-M05-01.02, FR-M05-02.14 |


<!-- sc:branch SC-M05-001 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E15.2 | FR-M05-02.01, BR-M05-10 |
| E15.2 | SYSTEM | Hệ thống không gọi AI và không cung cấp gợi ý; cho chọn Topic thủ công, không dùng thông báo lỗi dịch vụ cho trạng thái tắt có chủ đích. | AI tổng Tắt, Topic suggestion Bật; danh mục D-CAT vẫn dùng được | E15.3 | FR-M05-02.16, FR-M05-02.17, BR-M05-18, FR-M10-09.03, FR-M10-09.04, FR-M10-09.07, FR-M13-05.04 |
| E15.3 | ACT-002 | Lan chọn Toán học thủ công và gửi. | Topic={Toán học}; Tag=[]; chưa có gợi ý | M4 | FR-M05-01.02, FR-M05-02.17 |


<!-- sc:branch SC-M05-001 E16 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E16.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E16.2 | FR-M05-02.01, BR-M05-10 |
| E16.2 | SYSTEM | Hệ thống không gọi AI và không cung cấp gợi ý; cho chọn Topic thủ công, không dùng thông báo lỗi dịch vụ cho trạng thái tắt có chủ đích. | AI tổng Bật, Topic suggestion Tắt; danh mục D-CAT vẫn dùng được | E16.3 | FR-M05-02.16, FR-M05-02.17, BR-M05-18, FR-M10-09.03, FR-M10-09.04, FR-M10-09.07, FR-M13-05.04 |
| E16.3 | ACT-002 | Lan chọn Toán học thủ công và gửi. | Topic={Toán học}; Tag=[]; chưa có gợi ý | M4 | FR-M05-01.02, FR-M05-02.17 |


<!-- sc:branch SC-M05-001 E17 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E17.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E17.2 | FR-M05-02.01, BR-M05-10 |
| E17.2 | SYSTEM | Hệ thống không gọi AI và không cung cấp gợi ý; cho chọn Topic thủ công, không dùng thông báo lỗi dịch vụ cho trạng thái tắt có chủ đích. | cả hai công tắc Tắt; danh mục D-CAT vẫn dùng được | E17.3 | FR-M05-02.16, FR-M05-02.17, BR-M05-18, FR-M10-09.03, FR-M10-09.04, FR-M10-09.07, FR-M13-05.04 |
| E17.3 | ACT-002 | Lan chọn Toán học thủ công và gửi. | Topic={Toán học}; Tag=[]; chưa có gợi ý | M4 | FR-M05-01.02, FR-M05-02.17 |


<!-- sc:branch SC-M05-001 E18 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E18.1 | ACT-002 | Lan bấm Gợi ý topic với nội dung ngắn. | title="Cách giải phương trình bậc hai có tham số m" (10 từ); body="Mình làm mãi không ra, mọi người giúp với" (9 từ); 19 từ | E18.2 | FR-M05-02.01, FR-M05-02.05, BR-M05-12 |
| E18.2 | SYSTEM | Hệ thống không gọi AI, báo nội dung quá ngắn; danh mục vẫn cho chọn thủ công. | 19<20; chưa có gợi ý | E18.3 | FR-M05-02.05, BR-M05-12 |
| E18.3 | ACT-002 | Lan chọn Toán học và gửi bài có tiêu đề, nội dung hợp lệ này. | Topic={Toán học}; 19 từ không cấm gửi bài; Tag=[] | M4 | FR-M05-01.02, FR-M05-02.05 |


<!-- sc:branch SC-M05-001 E19 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E19.1 | ACT-002 | Lan yêu cầu gợi ý cho tiêu đề 10 từ và nội dung 9 từ nêu ở nhánh trước. | Tổng19 từ; title/body của lần này thay D-POST | E19.2 | FR-M05-02.01, FR-M05-02.05, BR-M05-12 |
| E19.2 | SYSTEM | Hệ thống báo quá ngắn, không gửi AI. | 19 từ | E19.3 | FR-M05-02.05 |
| E19.3 | ACT-002 | Lan thêm “ạ” vào cuối nội dung rồi bấm Gợi ý topic. | Tổng20 từ; không xét tệp đính kèm | E19.4 | FR-M05-02.01, FR-M05-02.05, BR-M05-12 |
| E19.4 | SYSTEM | Hệ thống kiểm hai cờ/tần suất và gửi đúng tiêu đề/nội dung 20 từ của lần này tới AI. | title10 từ + body10 từ; bỏ tệp | E19.5 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E19.5 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E19.6 | FR-M13-05.01, FR-M13-05.02 |
| E19.6 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E19.7 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E19.7 | ACT-002 | Lan quyết định tập cuối rồi gửi bài. | P501; Topic={Toán học, Hướng nghiệp}; bỏ Tin học; title/body không đổi sau gợi ý; Tag=[] | E19.8 | FR-M05-02.04, FR-M05-01.02, FR-M05-01.06, BR-M05-13 |
| E19.8 | SYSTEM | Hệ thống kiểm 1–3 Topic hiện hành và Tag rỗng, lưu tập tác giả chốt cho lần gửi; ghi phản hồi gợi ý còn hiệu lực rồi trả kết quả phân loại đã lưu. Không đợi Mod duyệt gợi ý. | P501; suggested={Toán học, Tin học}; final={Toán học, Hướng nghiệp}; phản hồi được ghi ở sự kiện gửi bài; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-01.02, FR-M05-01.06, FR-M05-02.04, FR-M05-02.12, FR-M05-03.01, BR-M05-03, BR-M05-04, BR-M05-13, BR-M05-16 |


<!-- sc:branch SC-M05-001 E20 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E20.1 | ACT-002 | Lan bấm Gợi ý topic lúc10:01:10. | 10 yêu cầu đã có trong10:00:30–10:00:59; đủ độ dài; hai cờ bật | E20.2 | FR-M05-02.15, BR-M05-17 |
| E20.2 | SYSTEM | Hệ thống từ chối yêu cầu thứ 11, không gọi AI cho yêu cầu vượt hạn mức; cho chọn thủ công. | Cửa sổ60 giây có 10 yêu cầu trước; không dùng phút lịch | E20.3 | FR-M05-02.15, BR-M05-17 |
| E20.3 | ACT-002 | Lan chọn Toán học thủ công rồi gửi. | Topic={Toán học}; không có gợi ý thành công trong snapshot nhánh | M4 | FR-M05-01.02 |


<!-- sc:branch SC-M05-001 E21 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E21.1 | ACT-002 | Lan bấm Gợi ý topic lúc10:01:31 sau các yêu cầu10:00:30–10:00:59. | Đã có ít nhất một yêu cầu cũ nằm ngoài60 giây gần nhất; lần hiện tại không vượt10 | E21.2 | FR-M05-02.15, BR-M05-17 |
| E21.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI.  | P501; title/body27 từ; không tệp; hai cờ bật; lúc10:01:31, còn 9 yêu cầu10:00:31–10:00:59 trong cửa sổ, một yêu cầu10:00:30 đã ra ngoài; lần mới là thứ 10 | E21.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E21.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E21.4 | FR-M13-05.01, FR-M13-05.02 |
| E21.4 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E21.5 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E21.5 | ACT-002 | Lan quyết định tập cuối rồi gửi bài. | P501; Topic={Toán học, Hướng nghiệp}; bỏ Tin học; title/body không đổi sau gợi ý; Tag=[] | E21.6 | FR-M05-02.04, FR-M05-01.02, FR-M05-01.06, BR-M05-13 |
| E21.6 | SYSTEM | Hệ thống kiểm 1–3 Topic hiện hành và Tag rỗng, lưu tập tác giả chốt cho lần gửi; ghi phản hồi gợi ý còn hiệu lực rồi trả kết quả phân loại đã lưu. Không đợi Mod duyệt gợi ý. | P501; suggested={Toán học, Tin học}; final={Toán học, Hướng nghiệp}; phản hồi được ghi ở sự kiện gửi bài; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-01.02, FR-M05-01.06, FR-M05-02.04, FR-M05-02.12, FR-M05-03.01, BR-M05-03, BR-M05-04, BR-M05-13, BR-M05-16 |


<!-- sc:branch SC-M05-001 E22 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E22.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E22.2 | FR-M05-02.01, BR-M05-10 |
| E22.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI. Lần thử đầu lỗi hoặc quá 10 giây; hệ thống đợi2 giây rồi gửi lại đúng một lần, không song song. Lần thứ hai có kết quả trong10 giây. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E22.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E22.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E22.4 | FR-M13-05.01, FR-M13-05.02 |
| E22.4 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E22.5 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E22.5 | ACT-002 | Lan quyết định tập cuối rồi gửi bài. | P501; Topic={Toán học, Hướng nghiệp}; bỏ Tin học; title/body không đổi sau gợi ý; Tag=[] | E22.6 | FR-M05-02.04, FR-M05-01.02, FR-M05-01.06, BR-M05-13 |
| E22.6 | SYSTEM | Hệ thống kiểm 1–3 Topic hiện hành và Tag rỗng, lưu tập tác giả chốt cho lần gửi; ghi phản hồi gợi ý còn hiệu lực rồi trả kết quả phân loại đã lưu. Không đợi Mod duyệt gợi ý. | P501; suggested={Toán học, Tin học}; final={Toán học, Hướng nghiệp}; phản hồi được ghi ở sự kiện gửi bài; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-01.02, FR-M05-01.06, FR-M05-02.04, FR-M05-02.12, FR-M05-03.01, BR-M05-03, BR-M05-04, BR-M05-13, BR-M05-16 |


<!-- sc:branch SC-M05-001 E23 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E23.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E23.2 | FR-M05-02.01, BR-M05-10 |
| E23.2 | SYSTEM | Hệ thống kiểm điều kiện và gửi AI; lần đầu lỗi/quá 10 giây thì đợi2 giây, thử lại một lần. Khi lần hai cũng lỗi, ghi lời gọi thất bại theo M13, hiện “Không thể gợi ý chủ đề lúc này, vui lòng chọn thủ công”; không tự chọn Topic, không tắt công tắc và không tự thử lần ba. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước; tối đa 10 giây/lần; giữa hai lần 2 giây | E23.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01, FR-M05-02.06, FR-M05-02.07, FR-M05-02.08, BR-M05-14, BR-M05-19, FR-M13-01.06, FR-M13-01.07, FR-M13-05.03, FR-M13-08.01, FR-M13-08.02 |
| E23.3 | ACT-002 | Lan chọn Toán học thủ công và gửi P501. | Topic={Toán học}; Tag=[]; không có gợi ý thành công | M4 | FR-M05-01.02, FR-M05-02.14 |


<!-- sc:branch SC-M05-001 E24 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E24.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E24.2 | FR-M05-02.01, BR-M05-10 |
| E24.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI.  | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E24.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E24.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E24.4 | FR-M13-05.01, FR-M13-05.02 |
| E24.4 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E24.5 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E24.5 | ACT-002 | Lan sửa tiêu đề sau khi nhận gợi ý. | Tiêu đề mới="Ứng dụng Bayes trong bài toán rút bóng" | E24.6 | FR-M05-02.09, BR-M05-15 |
| E24.6 | SYSTEM | Hệ thống đánh dấu gợi ý lỗi thời, hiện cảnh báo nhẹ cùng nút gợi ý lại; không tự gọi AI, không chặn gửi. | suggested={Toán học, Tin học}; stale=true | E24.7 | FR-M05-02.09, FR-M05-02.10, FR-M05-02.11, BR-M05-15 |
| E24.7 | ACT-002 | Lan chốt Toán học và gửi với nội dung đã đổi, không bấm lại. | final={Toán học}; Tag=[]; gợi ý gần nhất lỗi thời | E24.8 | FR-M05-02.04, FR-M05-02.11, FR-M05-01.02 |
| E24.8 | SYSTEM | Hệ thống kiểm tập cuối hợp lệ, lưu Toán học và tiếp nhận sự kiện gửi; không ghi phản hồi gợi ý lỗi thời. Trả kết quả phân loại đã lưu, không dùng cảnh báo để ngăn gửi. | P501.Topic={Toán học}; phản hồi=không; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-02.11, FR-M05-02.13, FR-M05-01.02, BR-M05-15, BR-M05-16 |


<!-- sc:branch SC-M05-001 E25 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E25.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E25.2 | FR-M05-02.01, BR-M05-10 |
| E25.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI.  | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E25.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E25.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E25.4 | FR-M13-05.01, FR-M13-05.02 |
| E25.4 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E25.5 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E25.5 | ACT-002 | Lan sửa nội dung chữ sau khi nhận gợi ý. | Thêm câu “Ví dụ này dùng hai hộp bóng khác nhau.” vào body | E25.6 | FR-M05-02.09, BR-M05-15 |
| E25.6 | SYSTEM | Hệ thống đánh dấu gợi ý lỗi thời, hiện cảnh báo nhẹ cùng nút gợi ý lại; không tự gọi AI, không chặn gửi. | suggested={Toán học, Tin học}; stale=true | E25.7 | FR-M05-02.09, FR-M05-02.10, FR-M05-02.11, BR-M05-15 |
| E25.7 | ACT-002 | Lan chốt Toán học và gửi với nội dung đã đổi, không bấm lại. | final={Toán học}; Tag=[]; gợi ý gần nhất lỗi thời | E25.8 | FR-M05-02.04, FR-M05-02.11, FR-M05-01.02 |
| E25.8 | SYSTEM | Hệ thống kiểm tập cuối hợp lệ, lưu Toán học và tiếp nhận sự kiện gửi; không ghi phản hồi gợi ý lỗi thời. Trả kết quả phân loại đã lưu, không dùng cảnh báo để ngăn gửi. | P501.Topic={Toán học}; phản hồi=không; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-02.11, FR-M05-02.13, FR-M05-01.02, BR-M05-15, BR-M05-16 |


<!-- sc:branch SC-M05-001 E26 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E26.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E26.2 | FR-M05-02.01, BR-M05-10 |
| E26.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI.  | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E26.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E26.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E26.4 | FR-M13-05.01, FR-M13-05.02 |
| E26.4 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E26.5 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E26.5 | ACT-002 | Lan thêm một câu vào nội dung chữ. | body thêm="Bài toán được giải theo hai trường hợp." | E26.6 | FR-M05-02.09 |
| E26.6 | SYSTEM | Hệ thống đánh dấu gợi ý lỗi thời, hiện cảnh báo nhẹ và nút gợi ý lại. | Lượt cũ stale=true | E26.7 | FR-M05-02.10 |
| E26.7 | ACT-002 | Lan bấm gợi ý lại cho nội dung mới. | title/body mới đủ 20 từ; còn hạn mức; hai cờ bật | E26.8 | FR-M05-02.01, FR-M05-02.10, BR-M05-17 |
| E26.8 | SYSTEM | Hệ thống kiểm lại cờ, độ dài, tần suất và gửi nội dung mới qua M13. | Không tự chạy lại trước khi tác giả bấm; không gửi tệp | E26.9 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E26.9 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E26.10 | FR-M13-05.01, FR-M13-05.02 |
| E26.10 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI. Đây là lượt gần nhất với nội dung mới; không suy diễn cách UI hợp nhất/thay tập đã chọn trước đó. | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E26.11 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E26.11 | ACT-002 | Lan quyết định tập cuối rồi gửi bài. | P501; Topic={Toán học, Hướng nghiệp}; bỏ Tin học; title/body không đổi sau gợi ý; Tag=[] | E26.12 | FR-M05-02.04, FR-M05-01.02, FR-M05-01.06, BR-M05-13 |
| E26.12 | SYSTEM | Hệ thống kiểm 1–3 Topic hiện hành và Tag rỗng, lưu tập tác giả chốt cho lần gửi; ghi phản hồi gợi ý còn hiệu lực rồi trả kết quả phân loại đã lưu. Không đợi Mod duyệt gợi ý. | P501; suggested={Toán học, Tin học}; final={Toán học, Hướng nghiệp}; phản hồi được ghi ở sự kiện gửi bài; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-01.02, FR-M05-01.06, FR-M05-02.04, FR-M05-02.12, FR-M05-03.01, BR-M05-03, BR-M05-04, BR-M05-13, BR-M05-16 |


<!-- sc:branch SC-M05-001 E27 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E27.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E27.2 | FR-M05-02.01, BR-M05-10 |
| E27.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI.  | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E27.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E27.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E27.4 | FR-M13-05.01, FR-M13-05.02 |
| E27.4 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E27.5 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E27.5 | ACT-002 | Lan bỏ bayes.pdf, thêm minhhoa.pdf hợp lệ rồi gửi với Toán học. | title/body giữ nguyên; file mới PDF1 MB; final={Toán học}; Tag=[] | E27.6 | FR-M05-02.01, FR-M05-02.09, BR-M05-11, BR-M05-15, FR-M03-02.01 |
| E27.6 | SYSTEM | Hệ thống kiểm tập cuối, lưu Toán học và ghi phản hồi còn hiệu lực; việc thay tệp không phải thay tiêu đề/nội dung chữ làm lỗi thời gợi ý. | suggested={Toán học, Tin học}; final={Toán học}; có phản hồi | END:SUCCESS | FR-M05-01.02, FR-M05-02.09, FR-M05-02.12, BR-M05-11, BR-M05-16 |


<!-- sc:branch SC-M05-001 E28 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E28.1 | ACT-002 | Lan mở sửa Topic P502 của mình. | P502 Đã đăng/Bình thường; Topic={Tin học}; Tag=[]; title/body D-POST | E28.2 | FR-M05-01.06, FR-M05-02.20 |
| E28.2 | SYSTEM | Hệ thống kiểm quyền/trạng thái sửa, trả danh mục và khả năng gợi ý cho tác giả; lượt cũ nếu có không được giả định còn hiệu lực. | P502 hiện có Tin học; nội dung đủ 20 từ | E28.3 | FR-M05-01.06, FR-M05-02.20, FR-M03-11.07 |
| E28.3 | ACT-002 | Lan bấm Gợi ý topic cho P502. | P502; title/body D-POST; hai cờ bật; còn hạn mức | E28.4 | FR-M05-02.01, FR-M05-02.20 |
| E28.4 | SYSTEM | Hệ thống kiểm đủ điều kiện và chuyển title/body P502 tới AI, không chuyển tệp. | Ngữ cảnh=P502 đang sửa, đúng tác giả Lan | E28.5 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E28.5 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E28.6 | FR-M13-05.01, FR-M13-05.02 |
| E28.6 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E28.7 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E28.7 | ACT-002 | Lan quyết định tập cuối rồi lưu bản sửa. | P502; Topic={Toán học, Hướng nghiệp}; bỏ Tin học; title/body không đổi sau gợi ý; Tag=[] | E28.8 | FR-M05-02.04, FR-M05-01.02, FR-M05-01.06, BR-M05-13 |
| E28.8 | SYSTEM | Hệ thống kiểm 1–3 Topic hiện hành và Tag rỗng, lưu tập tác giả chốt cho bản sửa; ghi phản hồi gợi ý còn hiệu lực rồi trả kết quả phân loại đã lưu. Không đợi Mod duyệt gợi ý. | P502; suggested={Toán học, Tin học}; final={Toán học, Hướng nghiệp}; phản hồi được ghi ở sự kiện lưu sửa | END:SUCCESS | FR-M05-01.02, FR-M05-01.06, FR-M05-02.04, FR-M05-02.12, FR-M05-03.01, BR-M05-03, BR-M05-04, BR-M05-13, BR-M05-16 |


<!-- sc:branch SC-M05-001 E29 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E29.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E29.2 | FR-M05-02.01, BR-M05-10 |
| E29.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI.  | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E29.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E29.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E29.4 | FR-M13-05.01, FR-M13-05.02 |
| E29.4 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E29.5 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E29.5 | ACT-002 | Lan chọn Toán học rồi lưu nháp, chưa gửi. | P501.Topic={Toán học}; Tag=[]; gợi ý chưa cũ | E29.6 | FR-M05-01.10 |
| E29.6 | SYSTEM | Hệ thống kiểm 0–3 Topic, lưu nháp đúng tập; không ghi phản hồi vì chưa có sự kiện gửi hoặc lưu sửa bài đã gửi. | P501 vẫn Nháp; phản hồi=không | END:SUCCESS | FR-M05-01.10, FR-M05-02.12, BR-M05-16 |


<!-- sc:branch SC-M05-001 E30 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E30.1 | SYSTEM | Hệ thống từ chối; quyền tác giả của User không áp dụng cho bài người khác. | Actor Lan; bài của Minh; Lan không có vai trò điều phối | END:REJECTED | FR-M05-11.04 |


<!-- sc:branch SC-M05-001 E31 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E31.1 | SYSTEM | Hệ thống từ chối; quyền tác giả của User không áp dụng cho bài người khác. | Actor Lan; bài của Minh; Lan không có vai trò điều phối | END:REJECTED | FR-M05-11.04 |


<!-- sc:branch SC-M05-001 E32 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E32.1 | ACT-002 | Lan yêu cầu sửa phân loại bài đã gửi của mình. | P502 của Lan; Chờ duyệt/Đã xóa hoặc Bị Mod ẩn; chưa mở được thao tác sửa | E32.2 | FR-M03-11.07 |
| E32.2 | SYSTEM | Hệ thống áp cổng sửa M03, từ chối yêu cầu; không dùng M05 để vượt điều kiện trạng thái. | Không ghi thay đổi phân loại từ lần yêu cầu này | END:REJECTED | FR-M03-11.07 |


<!-- sc:branch SC-M05-001 E33 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E33.1 | ACT-002 | Lan yêu cầu sửa phân loại P502 của mình. | P502 Đã đăng/Bình thường lúc mở; Topic={Tin học}; Tag={bayes} | E33.2 | FR-M03-11.01 |
| E33.2 | SYSTEM | Hệ thống kiểm quyền/trạng thái và trả phân loại hiện tại để sửa. | Được sửa tại lúc mở; giữ cùng P502 | E33.3 | FR-M03-11.01 |
| E33.3 | ACT-002 | Lan gửi lưu bản sửa phân loại. | Topic={Toán học}; Tag={bayes}; trước lúc xử lý lưu, P502 chuyển Đã xóa hoặc Bị Mod ẩn | E33.4 | FR-M05-01.06, FR-M05-03.10 |
| E33.4 | SYSTEM | Hệ thống kiểm trạng thái hiện tại, từ chối lưu bản sửa không còn được phép; không dùng quyền lúc mở để vượt trạng thái khi lưu. | Không ghi tập sửa của lần lưu bị từ chối | END:REJECTED | FR-M03-11.07 |


<!-- sc:branch SC-M05-001 E34 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E34.1 | SYSTEM | Hệ thống từ chối thao tác cần phiên, yêu cầu đăng nhập lại theo M01; không ghi chốt phân loại từ yêu cầu không có phiên hợp lệ. | Phiên làm mới đã hết30 ngày; không chỉ là phiên truy cập hết1 giờ | END:REJECTED | FR-M01-06.04 |


<!-- sc:branch SC-M05-001 E35 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E35.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E35.2 | FR-M05-02.01, BR-M05-10 |
| E35.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI.  | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E35.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E35.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E35.4 | FR-M13-05.01, FR-M13-05.02 |
| E35.4 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E35.5 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E35.5 | ACT-002 | Lan gửi bài với tập Topic cuối vi phạm sau khi nhận gợi ý. | Topic=[] | E35.6 | FR-M05-02.04, FR-M05-01.03, FR-M05-01.04, BR-M05-03, BR-M05-13 |
| E35.6 | SYSTEM | Hệ thống từ chối gửi tập Topic vi phạm; có gợi ý AI không miễn hạn mức và không tự chốt thay tác giả. Không ghi phản hồi cho sự kiện gửi chưa được chấp nhận. | Gửi với0 Topic không thành công; không tự chọn lại Topic đã bỏ | END:REJECTED | FR-M05-01.03, FR-M05-01.04, FR-M05-02.04, FR-M05-02.12, BR-M05-03, BR-M05-13, BR-M05-16 |


<!-- sc:branch SC-M05-001 E36 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E36.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E36.2 | FR-M05-02.01, BR-M05-10 |
| E36.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI.  | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E36.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E36.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E36.4 | FR-M13-05.01, FR-M13-05.02 |
| E36.4 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E36.5 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E36.5 | ACT-002 | Lan gửi bài với tập Topic cuối vi phạm sau khi nhận gợi ý. | Topic={Toán học, Tin học, Khác, Góc Chill} | E36.6 | FR-M05-02.04, FR-M05-01.03, FR-M05-01.04, BR-M05-03, BR-M05-13 |
| E36.6 | SYSTEM | Hệ thống từ chối gửi tập Topic vi phạm; có gợi ý AI không miễn hạn mức và không tự chốt thay tác giả. Không ghi phản hồi cho sự kiện gửi chưa được chấp nhận. | Gửi với4 Topic không thành công; không tự chọn lại Topic đã bỏ | END:REJECTED | FR-M05-01.03, FR-M05-01.04, FR-M05-02.04, FR-M05-02.12, BR-M05-03, BR-M05-13, BR-M05-16 |


<!-- sc:branch SC-M05-001 E37 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E37.1 | ACT-002 | Lan bấm Gợi ý topic cho bài của mình. | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E37.2 | FR-M05-02.01, BR-M05-10 |
| E37.2 | SYSTEM | Hệ thống kiểm đúng tác giả, hai cờ bật, đủ 20 từ và hạn mức cửa sổ trượt; gửi chỉ tiêu đề và nội dung chữ qua M13 tới AI.  | P501; title+body=27 từ theo khoảng trắng; chỉ gửi title/body, không gửi bayes.pdf; hai cờ AI bật; 0 yêu cầu trong 60 giây trước | E37.3 | FR-M05-02.01, FR-M05-02.02, FR-M05-02.05, FR-M05-02.15, FR-M05-02.16, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-17, BR-M05-18, FR-M13-01.01, FR-M13-01.04, FR-M13-01.05, FR-M13-05.01 |
| E37.3 | ACT-006 | Dịch vụ AI trả kết quả Topic cho yêu cầu đã nhận. | {Toán học, Tin học} | E37.4 | FR-M13-05.01, FR-M13-05.02 |
| E37.4 | SYSTEM | Hệ thống đối chiếu danh mục hiện tại, hiển thị tối đa 3 gợi ý hợp lệ ở trạng thái chọn sẵn; không gán Tag bằng AI.  | Gợi ý={Toán học, Tin học}; lần gần nhất còn hiệu lực | E37.5 | FR-M05-02.03, FR-M05-02.19, BR-M05-13, BR-M05-14, FR-M13-05.02, FR-M05-03.11 |
| E37.5 | ACT-002 | Lan thêm một câu vào nội dung chữ. | Thêm “Ta cần phân biệt xác suất trước và sau điều kiện.” | E37.6 | FR-M05-02.09 |
| E37.6 | SYSTEM | Hệ thống đánh dấu gợi ý lỗi thời, hiện cảnh báo nhẹ và nút gợi ý lại. | Lượt cũ stale=true | E37.7 | FR-M05-02.09, FR-M05-02.10 |
| E37.7 | ACT-002 | Lan bấm gợi ý lại sau khi công tắc Topic suggestion đã tắt. | AI tổng bật; Topic suggestion tắt; nội dung mới đủ 20 từ | E37.8 | FR-M05-02.10, FR-M05-02.16, BR-M05-18 |
| E37.8 | SYSTEM | Hệ thống kiểm cờ hiện tại, không gọi AI, cho chọn thủ công; không có gợi ý mới còn hiệu lực cho nội dung đã đổi. | Không đổi cờ, không tự khôi phục hiệu lực lượt cũ | E37.9 | FR-M05-02.16, FR-M05-02.17, FR-M13-01.09 |
| E37.9 | ACT-002 | Lan chọn Hướng nghiệp thủ công rồi gửi với nội dung mới. | Topic={Hướng nghiệp}; Tag=[]; gợi ý cũ vẫn lỗi thời | E37.10 | FR-M05-01.02, FR-M05-02.17 |
| E37.10 | SYSTEM | Hệ thống kiểm tập Topic cuối, lưu Hướng nghiệp và trả kết quả phân loại; không ghi phản hồi vì không có lượt gần nhất còn hiệu lực. | P501.Topic={Hướng nghiệp}; phản hồi=không; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-01.02, FR-M05-02.13, BR-M05-15, BR-M05-16 |


**E38 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên thử gán/đổi Topic. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-001 E38 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E38.1 | ACT-001 | Guest yêu cầu gán/đổi Topic cho bài. | Chưa đăng nhập; không mượn phiên của tác giả | E38.2 | FR-M05-01.08 |
| E38.2 | SYSTEM | Hệ thống từ chối thao tác phân loại của Guest; không lưu thay đổi hoặc tự đăng nhập giúp. | Không ghi Topic/Tag từ yêu cầu này | END:REJECTED | FR-M05-01.08 |


**E39 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu gợi ý Topic. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-001 E39 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E39.1 | ACT-001 | Guest yêu cầu Gợi ý topic. | Chưa đăng nhập; title/body đủ 20 từ cũng không cấp quyền | E39.2 | FR-M05-02.18 |
| E39.2 | SYSTEM | Hệ thống từ chối, không gọi AI hoặc tự chọn Topic. | Không có gợi ý và không ghi phản hồi | END:REJECTED | FR-M05-02.18 |


<!-- sc:end SC-M05-001 -->

<a id="sc-m05-002"></a>

<!-- sc:scenario SC-M05-002 -->

### SC-M05-002

#### 1. Tên kịch bản chuẩn

Gắn và chốt Tag tự do cho bài viết của mình — BF-M05-002. UC owner: [UC-M05-003](../../us/US-M05.md#uc-m05-003). Trigger: Lan yêu cầu gắn Tag cho P503 của mình.

#### 2. Actor thực hiện

ACT-002 — User — có phiên là actor chính. Các quyền kế thừa giữ đúng actor hierarchy của US. Đường E tại M1 thay toàn bộ khi actor khởi tạo khác, không đổi vai trò giữa luồng.

#### 3. Tiền điều kiện

Có bài của tác giả trong ngữ cảnh soạn/sửa và phiên hợp lệ ở đường chuẩn; quyền/trạng thái vẫn được kiểm. P503 là nháp của Lan, title/body hợp lệ như D-POST, Topic đã chọn={Toán học}, Tag=[]; chưa tồn tại bayes2026. Chọn Topic là chức năng SC001, ở đây giữ một Topic hợp lệ, không bắt lặp lại thao tác đó.

#### 4. Hậu điều kiện

<!-- sc:post SC-M05-002 -->

| result | condition |
|---|---|
| SUCCESS | Tập cuối 0–5 liên kết Tag được lưu cho bài đúng quyền; tên mới hợp lệ tự tạo hoạt động, tên đã có dùng lại, không trùng. Chỉ Tag hoạt động được hiển thị chữ thường kèm #; giữ liên kết cũ đang vô hiệu hóa nếu actor không yêu cầu bỏ. Phần nhập mới trùng tên Tag vô hiệu hóa chỉ là văn bản, không liên kết mới. Không thay đổi Topic nếu actor không yêu cầu. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không ghi nhận kết quả thành công của yêu cầu bị từ chối; không cấp thêm quyền hay tự sửa dữ liệu phân loại để vượt điều kiện. Các hiệu ứng đã hoàn tất trước yêu cầu này không bị suy thành rollback. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M05-002 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan yêu cầu gắn Tag cho P503 của mình. | P503 Nháp; Topic={Toán học}; Tag=[]; title/body như D-POST | M2 | FR-M05-03.01 |
| M2 | SYSTEM | Hệ thống kiểm phiên/quyền bài, nhận tập Tag tự do để tác giả nhập; giữ ngữ cảnh Topic hợp lệ. Không dùng AI gợi ý hoặc gắn Tag. | Tag hiện có=[]; D-TAG; tối đa 5; chỉ chữ/số/_; có chữ; ≤30 ký tự | M3 | FR-M05-03.01, FR-M05-03.11, BR-M05-20, BR-M05-22, BR-M05-23 |
| M3 | ACT-002 | Lan nhập #Bayes2026 và #XácSuất rồi gửi bài. | Tên nhập={Bayes2026, XácSuất}; Topic giữ={Toán học} | M4 | FR-M05-03.01 |
| M4 | SYSTEM | Hệ thống chuẩn hóa chỉ hoa thành thường, kiểm tên/độ dài/số lượng, dùng lại xácsuất đã có và tạo bayes2026 chưa có ở trạng thái hoạt động, không duyệt. Lưu hai liên kết Tag cho sự kiện gửi hợp lệ, kiểm Topic hiện có, hiển thị #bayes2026 và #xácsuất; không tạo Tag từ AI. | P503.Tag={bayes2026, xácsuất}; Topic={Toán học}; Tag mới bayes2026: tên/thời điểm09/11/2026 10:00 +07/trạng thái hoạt động, không lưu người tạo; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.05, FR-M05-03.06, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-20, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-26, FR-M05-01.02, FR-M05-03.11 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Bộ dữ liệu trong guard thay bộ chuẩn cho lần chạy đó; mỗi nhánh là snapshot riêng. Điểm nhập lại nêu rõ bước kiểm; nếu dữ liệu còn sai áp lại guard, không tự giới hạn số lần. REJECTED là kết thúc từ chối hợp lệ của US; không bịa nút OK/hủy/thử lại hay rollback lỗi lưu trữ chưa có nguồn.

<!-- sc:exceptions SC-M05-002 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M3 | Tác giả không muốn gắn Tag hoặc bỏ hết Tag | E1.1 | FR-M05-03.01, BR-M05-22, FR-M05-03.11, FR-M05-01.02 |
| E2 | user-choice | M3 | Tag thứ sáu; tác giả sửa rồi gửi | E2.1 | FR-M05-03.04, BR-M05-22, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.05, FR-M05-03.06, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-20, BR-M05-21, BR-M05-23, BR-M05-24, BR-M05-26, FR-M05-01.02 |
| E3 | user-choice | M3 | Tên Tag 31 ký tự không tính #; tác giả sửa rồi gửi | E3.1 | FR-M05-03.05, BR-M05-23, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.06, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-20, BR-M05-21, BR-M05-22, BR-M05-24, BR-M05-26, FR-M05-01.02 |
| E4 | user-choice | M3 | Tên có ký tự không hợp lệ; tác giả sửa rồi gửi | E4.1 | FR-M05-03.06, BR-M05-20, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.05, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-26, FR-M05-01.02 |
| E5 | user-choice | M3 | Tên không có chữ cái; tác giả sửa rồi gửi | E5.1 | FR-M05-03.07, BR-M05-20, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.05, FR-M05-03.06, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-26, FR-M05-01.02 |
| E6 | user-choice | M3 | Tác giả nhập cùng tên Tag khác chữ hoa/thường hai lần | E6.1 | FR-M05-03.03, FR-M05-03.08, BR-M05-24, FR-M05-03.01, FR-M05-03.14 |
| E7 | user-choice | M3 | Tên có dấu và không dấu khác nhau, đều hợp lệ | E7.1 | FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, BR-M05-20, BR-M05-24, FR-M05-03.14 |
| E8 | user-choice | M3 | Tác giả nhập lại #abc đang bị vô hiệu hóa | E8.1 | FR-M05-03.09, FR-M05-03.01, FR-M05-03.03, FR-M05-03.14, BR-M05-26 |
| E9 | user-choice | M1 | Tác giả thêm/bỏ Tag khi sửa bài đã gửi | E9.1 | FR-M05-03.10, FR-M05-03.11, FR-M03-11.01, FR-M03-11.07, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.05, FR-M05-03.06, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-20, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-26, FR-M05-02.12, FR-M05-02.13, FR-M05-02.14, BR-M05-16, FR-M03-11.02 |
| E10 | system | M4 | Cổng gửi M03 không đạt vì Topic hiện có bị xóa hoặc không còn Topic hợp lệ | E10.1 | FR-M05-01.03, FR-M05-01.09, FR-M05-03.01, BR-M05-03 |
| E11 | system | M2 | User có phiên nhưng đang đổi phân loại bài người khác mà không là Mod/Admin | E11.1 | FR-M05-11.04 |
| E12 | system | M4 | User có phiên nhưng đang đổi phân loại bài người khác mà không là Mod/Admin | E12.1 | FR-M05-11.04 |
| E13 | user-choice | M1 | Tác giả yêu cầu sửa phân loại bài Chờ duyệt/Đã xóa hoặc Bị Mod ẩn | E13.1 | FR-M03-11.07 |
| E14 | user-choice | M1 | Trạng thái bài chuyển sang không cho sửa sau khi đã mở sửa hợp lệ | E14.1 | FR-M03-11.01, FR-M05-01.06, FR-M05-03.10, FR-M03-11.07 |
| E15 | system | M4 | Phiên đã hết hiệu lực và không làm mới được tại thời điểm ghi | E15.1 | FR-M01-06.04 |
| E16 | user-choice | M1 | Sửa Tag khác trong khi bài đang giữ liên kết với Tag bị vô hiệu hóa | E16.1 | FR-M05-03.10, FR-M05-04.05, FR-M05-09.03, BR-M05-26, FR-M05-03.01, FR-M05-03.03, FR-M05-03.14, BR-M05-04 |
| E17 | system | M1 | ACT-001 — Guest chưa có phiên thử gắn/đổi Tag. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E17.1 | FR-M05-03.12 |


<!-- sc:branch SC-M05-002 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Lan giữ tập Tag rỗng rồi gửi P503. | Tag=[]; Topic={Toán học}; title/body hợp lệ | E1.2 | FR-M05-03.01, BR-M05-22 |
| E1.2 | SYSTEM | Hệ thống kiểm Topic hiện có và chốt tập Tag rỗng hợp lệ cho lần gửi; không bắt nhập Tag hoặc tự gợi ý Tag bằng AI. | P503.Tag=[]; không tạo Tag; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-03.01, FR-M05-03.11, FR-M05-01.02, BR-M05-22 |


<!-- sc:branch SC-M05-002 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | Lan nhập tập Tag vi phạm nêu trong nhánh. | {bayes, xácsuất, đạo_hàm, lớp12, covid19}+tag_sáu; P503.Topic={Toán học} | E2.2 | FR-M05-03.04, BR-M05-22 |
| E2.2 | SYSTEM | Hệ thống từ chối Tag thứ sáu, giữ 5 Tag đã có. | Không nhận Tag vi phạm làm liên kết hợp lệ | E2.3 | FR-M05-03.04, BR-M05-22 |
| E2.3 | ACT-002 | Lan chốt tập Tag hợp lệ và gửi P503. | Tag cuối={bayes, xácsuất, đạo_hàm, lớp12, covid19}; Topic={Toán học}; nội dung giữ nguyên | E2.4 | FR-M05-03.04, BR-M05-22, FR-M05-03.01 |
| E2.4 | SYSTEM | Hệ thống kiểm lại tập cuối, chuẩn hóa, dùng lại/tạo Tag hợp lệ rồi lưu và trả đúng tập Tag đã chốt; Topic vẫn Toán học. Không coi Tag bị từ chối ở bước trước là đã gắn. | P503.Tag={bayes, xácsuất, đạo_hàm, lớp12, covid19} (tên chuẩn hóa không gồm #); hiển thị từng tên kèm #; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-03.04, BR-M05-22, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.05, FR-M05-03.06, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-20, BR-M05-21, BR-M05-23, BR-M05-24, BR-M05-26, FR-M05-01.02 |


<!-- sc:branch SC-M05-002 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-002 | Lan nhập tập Tag vi phạm nêu trong nhánh. | "a" lặp31 lần sau #; P503.Topic={Toán học} | E3.2 | FR-M05-03.05, BR-M05-23 |
| E3.2 | SYSTEM | Hệ thống từ chối Tag dài31 ký tự, không cắt tự động. | Không nhận Tag vi phạm làm liên kết hợp lệ | E3.3 | FR-M05-03.05, BR-M05-23 |
| E3.3 | ACT-002 | Lan chốt tập Tag hợp lệ và gửi P503. | Tag cuối="a" lặp30 lần sau #; Topic={Toán học}; nội dung giữ nguyên | E3.4 | FR-M05-03.05, BR-M05-23, FR-M05-03.01 |
| E3.4 | SYSTEM | Hệ thống kiểm lại tập cuối, chuẩn hóa, dùng lại/tạo Tag hợp lệ rồi lưu và trả đúng tập Tag đã chốt; Topic vẫn Toán học. Không coi Tag bị từ chối ở bước trước là đã gắn. | P503.Tag={aaaaaaaaaaaaaaaaaaaaaaaaaaaaaa} (tên chuẩn hóa không gồm #); hiển thị từng tên kèm #; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-03.05, BR-M05-23, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.06, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-20, BR-M05-21, BR-M05-22, BR-M05-24, BR-M05-26, FR-M05-01.02 |


<!-- sc:branch SC-M05-002 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-002 | Lan nhập tập Tag vi phạm nêu trong nhánh. | #Xác Suất hoặc #node.js hoặc #covid-19 hoặc #c++; P503.Topic={Toán học} | E4.2 | FR-M05-03.06, BR-M05-20 |
| E4.2 | SYSTEM | Hệ thống từ chối Tag chứa khoảng trắng/dấu chấm/gạch ngang/dấu cộng, không tự sửa. | Không nhận Tag vi phạm làm liên kết hợp lệ | E4.3 | FR-M05-03.06, BR-M05-20 |
| E4.3 | ACT-002 | Lan chốt tập Tag hợp lệ và gửi P503. | Tag cuối=#xácsuất; Topic={Toán học}; nội dung giữ nguyên | E4.4 | FR-M05-03.06, BR-M05-20, FR-M05-03.01 |
| E4.4 | SYSTEM | Hệ thống kiểm lại tập cuối, chuẩn hóa, dùng lại/tạo Tag hợp lệ rồi lưu và trả đúng tập Tag đã chốt; Topic vẫn Toán học. Không coi Tag bị từ chối ở bước trước là đã gắn. | P503.Tag={xácsuất} (tên chuẩn hóa không gồm #); hiển thị từng tên kèm #; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-03.06, BR-M05-20, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.05, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-26, FR-M05-01.02 |


<!-- sc:branch SC-M05-002 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-002 | Lan nhập tập Tag vi phạm nêu trong nhánh. | #2024 hoặc #___; P503.Topic={Toán học} | E5.2 | FR-M05-03.07, BR-M05-20 |
| E5.2 | SYSTEM | Hệ thống từ chối Tag không có chữ cái. | Không nhận Tag vi phạm làm liên kết hợp lệ | E5.3 | FR-M05-03.07, BR-M05-20 |
| E5.3 | ACT-002 | Lan chốt tập Tag hợp lệ và gửi P503. | Tag cuối=#lớp12; Topic={Toán học}; nội dung giữ nguyên | E5.4 | FR-M05-03.07, BR-M05-20, FR-M05-03.01 |
| E5.4 | SYSTEM | Hệ thống kiểm lại tập cuối, chuẩn hóa, dùng lại/tạo Tag hợp lệ rồi lưu và trả đúng tập Tag đã chốt; Topic vẫn Toán học. Không coi Tag bị từ chối ở bước trước là đã gắn. | P503.Tag={lớp12} (tên chuẩn hóa không gồm #); hiển thị từng tên kèm #; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-03.07, BR-M05-20, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.05, FR-M05-03.06, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-26, FR-M05-01.02 |


<!-- sc:branch SC-M05-002 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-002 | Lan nhập #Bayes và #bayes rồi gửi. | bayes đã tồn tại hoạt động; P503.Topic={Toán học} | E6.2 | FR-M05-03.03, FR-M05-03.08, BR-M05-24 |
| E6.2 | SYSTEM | Hệ thống chuẩn hóa thành bayes, dùng lại Tag hiện có và chỉ lưu một liên kết; trả #bayes, không tạo Tag hay liên kết thứ hai. | P503.Tag={bayes}; Topic={Toán học}; M03 tiếp nhận Chờ duyệt | END:SUCCESS | FR-M05-03.01, FR-M05-03.03, FR-M05-03.08, FR-M05-03.14, BR-M05-24 |


<!-- sc:branch SC-M05-002 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | ACT-002 | Lan nhập #XácSuất và #xacsuat rồi gửi. | xácsuất đã có; xacsuat chưa có; P503.Topic={Toán học} | E7.2 | FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, BR-M05-20, BR-M05-24 |
| E7.2 | SYSTEM | Hệ thống giữ dấu, chuẩn hóa hoa thành thường; dùng lại xácsuất và tạo xacsuat hoạt động; lưu hai Tag khác nhau, trả #xácsuất và #xacsuat. | P503.Tag={xácsuất, xacsuat}; không gộp hai tên | END:SUCCESS | FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.14, BR-M05-24 |


<!-- sc:branch SC-M05-002 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | ACT-002 | Lan nhập #abc cùng #Bayes rồi gửi. | abc tồn tại bị vô hiệu hóa; bayes hoạt động; Topic={Toán học} | E8.2 | FR-M05-03.09 |
| E8.2 | SYSTEM | Hệ thống giữ phần nhập #abc như văn bản, không tạo Tag hoạt động cùng tên và không thêm liên kết abc; lưu bayes hợp lệ, trả #bayes là Tag và #abc là chữ thường trong phần nhập được hiển thị. | P503.Tag={bayes}; văn bản=#abc; không suy vị trí/lưu trữ văn bản trên HMI | END:SUCCESS | FR-M05-03.01, FR-M05-03.03, FR-M05-03.09, FR-M05-03.14, BR-M05-26 |


<!-- sc:branch SC-M05-002 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | ACT-002 | Lan mở sửa Tag P504 Đã đăng của mình. | P504.Topic={Toán học}; Tag={bayes, xácsuất}; Bình thường | E9.2 | FR-M05-03.10 |
| E9.2 | SYSTEM | Hệ thống kiểm quyền/trạng thái sửa, trả tập Tag hiện tại và nhận phần thay đổi; không dùng AI. | Tag trước={bayes, xácsuất} | E9.3 | FR-M05-03.10, FR-M05-03.11, FR-M03-11.01, FR-M03-11.07 |
| E9.3 | ACT-002 | Lan bỏ xácsuất, thêm #đạo_hàm và lưu. | Tag cuối={bayes, đạo_hàm}; Topic giữ Toán học | E9.4 | FR-M05-03.10 |
| E9.4 | SYSTEM | Hệ thống kiểm tối đa 5, tên hợp lệ, chuẩn hóa, dùng lại/tạo Tag cần thiết rồi lưu tập cuối; trả #bayes và #đạo_hàm. Topic không bị thay, không ghi phản hồi gợi ý khi không dùng Topic suggestion. | P504.Tag={bayes, đạo_hàm}; Topic={Toán học} | END:SUCCESS | FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.05, FR-M05-03.06, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-20, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-26, FR-M05-03.10, FR-M05-03.11, FR-M05-02.12, FR-M05-02.13, FR-M05-02.14, BR-M05-16, FR-M03-11.02 |


<!-- sc:branch SC-M05-002 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống từ chối gửi/chốt phân loại thiếu Topic hợp lệ; có Tag hợp lệ không thay được Topic bắt buộc. Tác giả chọn Topic bằng SC001 trong lần thao tác tiếp theo nếu muốn. | P503.Topic=[] hoặc Toán học đã bị xóa trước gửi; Tag nhập vẫn hợp lệ | END:REJECTED | FR-M05-01.03, FR-M05-01.09, FR-M05-03.01, BR-M05-03 |


<!-- sc:branch SC-M05-002 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | SYSTEM | Hệ thống từ chối; quyền tác giả của User không áp dụng cho bài người khác. | Actor Lan; bài của Minh; Lan không có vai trò điều phối | END:REJECTED | FR-M05-11.04 |


<!-- sc:branch SC-M05-002 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | SYSTEM | Hệ thống từ chối; quyền tác giả của User không áp dụng cho bài người khác. | Actor Lan; bài của Minh; Lan không có vai trò điều phối | END:REJECTED | FR-M05-11.04 |


<!-- sc:branch SC-M05-002 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | ACT-002 | Lan yêu cầu sửa phân loại bài đã gửi của mình. | P502 của Lan; Chờ duyệt/Đã xóa hoặc Bị Mod ẩn; chưa mở được thao tác sửa | E13.2 | FR-M03-11.07 |
| E13.2 | SYSTEM | Hệ thống áp cổng sửa M03, từ chối yêu cầu; không dùng M05 để vượt điều kiện trạng thái. | Không ghi thay đổi phân loại từ lần yêu cầu này | END:REJECTED | FR-M03-11.07 |


<!-- sc:branch SC-M05-002 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | ACT-002 | Lan yêu cầu sửa phân loại P502 của mình. | P502 Đã đăng/Bình thường lúc mở; Topic={Tin học}; Tag={bayes} | E14.2 | FR-M03-11.01 |
| E14.2 | SYSTEM | Hệ thống kiểm quyền/trạng thái và trả phân loại hiện tại để sửa. | Được sửa tại lúc mở; giữ cùng P502 | E14.3 | FR-M03-11.01 |
| E14.3 | ACT-002 | Lan gửi lưu bản sửa phân loại. | Topic={Toán học}; Tag={bayes}; trước lúc xử lý lưu, P502 chuyển Đã xóa hoặc Bị Mod ẩn | E14.4 | FR-M05-01.06, FR-M05-03.10 |
| E14.4 | SYSTEM | Hệ thống kiểm trạng thái hiện tại, từ chối lưu bản sửa không còn được phép; không dùng quyền lúc mở để vượt trạng thái khi lưu. | Không ghi tập sửa của lần lưu bị từ chối | END:REJECTED | FR-M03-11.07 |


<!-- sc:branch SC-M05-002 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | SYSTEM | Hệ thống từ chối thao tác cần phiên, yêu cầu đăng nhập lại theo M01; không ghi chốt phân loại từ yêu cầu không có phiên hợp lệ. | Phiên làm mới đã hết30 ngày; không chỉ là phiên truy cập hết1 giờ | END:REJECTED | FR-M01-06.04 |


<!-- sc:branch SC-M05-002 E16 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E16.1 | ACT-002 | Lan mở sửa Tag P504 của mình. | P504 Đã đăng/Bình thường; Topic={Toán học}; Tag liên kết={bayes, abc}; abc vô hiệu | E16.2 | FR-M05-03.10 |
| E16.2 | SYSTEM | Hệ thống kiểm quyền/trạng thái, hiển thị #bayes đang hoạt động; không hiện #abc nhưng giữ liên kết cũ, không đồng nhất việc ẩn với bỏ Tag. | Liên kết vẫn={bayes, abc}; Tag hiển thị={#bayes} | E16.3 | FR-M05-03.10, FR-M05-04.05, FR-M05-09.03, BR-M05-26 |
| E16.3 | ACT-002 | Lan thêm #XácSuất rồi lưu, không yêu cầu bỏ các liên kết cũ. | Thêm xácsuất; Topic giữ Toán học; liên kết abc không bị tác giả yêu cầu bỏ | E16.4 | FR-M05-03.10 |
| E16.4 | SYSTEM | Hệ thống kiểm phần thêm, dùng lại xácsuất hoạt động, lưu thêm liên kết và giữ bayes/abc cũ; trả #bayes, #xácsuất, tiếp tục ẩn abc. Không tự bỏ abc chỉ vì không hiển thị. | P504.Tag liên kết={bayes, abc, xácsuất}; 3 liên kết≤5; hiển thị2 Tag; Topic={Toán học} | END:SUCCESS | FR-M05-03.01, FR-M05-03.03, FR-M05-03.10, FR-M05-03.14, FR-M05-09.03, FR-M05-04.05, BR-M05-04, BR-M05-26 |


**E17 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên thử gắn/đổi Tag. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-002 E17 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E17.1 | ACT-001 | Guest yêu cầu gắn/đổi Tag cho bài. | Chưa đăng nhập; không mượn phiên của tác giả | E17.2 | FR-M05-03.12 |
| E17.2 | SYSTEM | Hệ thống từ chối thao tác phân loại của Guest; không lưu thay đổi hoặc tự đăng nhập giúp. | Không ghi Topic/Tag từ yêu cầu này | END:REJECTED | FR-M05-03.12 |


<!-- sc:end SC-M05-002 -->

<a id="sc-m05-003"></a>

<!-- sc:scenario SC-M05-003 -->

### SC-M05-003

#### 1. Tên kịch bản chuẩn

Xem danh mục và nhãn phân loại Topic, Tag — BF-M05-003. UC owner: [UC-M05-004](../../us/US-M05.md#uc-m05-004). Trigger: Guest mở danh sách Topic.

#### 2. Actor thực hiện

ACT-001 — Guest — chưa có phiên là actor chính. Các quyền kế thừa giữ đúng actor hierarchy của US. Đường E tại M1 thay toàn bộ khi actor khởi tạo khác, không đổi vai trò giữa luồng.

#### 3. Tiền điều kiện

Không cần đăng nhập để xem danh mục. Đường chuẩn Guest yêu cầu danh sách Topic; các đường đọc nhãn bài chỉ trả khi có quyền đọc bài theo M03. D-CAT là snapshot trước các ví dụ thêm/gộp/xóa, không chạy các scenario nối tiếp bắt buộc.

#### 4. Hậu điều kiện

<!-- sc:post SC-M05-003 -->

| result | condition |
|---|---|
| SUCCESS | Trả đúng tập danh mục hoặc nhãn phân loại theo yêu cầu đọc và quyền bài: Topic hiện hành, Tag chỉ hoạt động; nhãn bài chỉ hiện Tag hoạt động còn liên kết. Không sửa phân loại, không tạo phiên hoặc tự mở thao tác quản trị. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không ghi nhận kết quả thành công của yêu cầu bị từ chối; không cấp thêm quyền hay tự sửa dữ liệu phân loại để vượt điều kiện. Các hiệu ứng đã hoàn tất trước yêu cầu này không bị suy thành rollback. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M05-003 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-001 | Guest mở danh sách Topic. | Loại danh sách=Topic | M2 | FR-M05-04.01 |
| M2 | SYSTEM | Hệ thống trả mọi Topic hiện tại trong danh mục phẳng: 11 Topic ban đầu và các Topic được Admin thêm còn tồn tại; không yêu cầu đăng nhập và không tính lại Trending do mở danh sách. | Snapshot D-CAT gồm 11 Topic; không Topic con; không tự áp giới hạn3/20 lên danh mục | END:SUCCESS | FR-M05-04.01, FR-M05-04.06, BR-M05-01, BR-M05-02, FR-M05-05.10 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Bộ dữ liệu trong guard thay bộ chuẩn cho lần chạy đó; mỗi nhánh là snapshot riêng. Điểm nhập lại nêu rõ bước kiểm; nếu dữ liệu còn sai áp lại guard, không tự giới hạn số lần. REJECTED là kết thúc từ chối hợp lệ của US; không bịa nút OK/hủy/thử lại hay rollback lỗi lưu trữ chưa có nguồn.

<!-- sc:exceptions SC-M05-003 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Người xem chọn danh sách Tag thay cho Topic | E1.1 | FR-M05-04.02, FR-M05-04.03, FR-M05-03.14, BR-M05-26 |
| E2 | user-choice | M1 | Người xem yêu cầu đọc nhãn Topic, Tag trên bài công khai | E2.1 | FR-M05-04.04, FR-M05-04.05, FR-M05-03.14, BR-M05-26, FR-M03-07.01 |
| E3 | system | M1 | Đọc nhãn bài không được phép hiển thị với Guest | E3.1 | FR-M05-04.04, FR-M03-07.01, FR-M03-07.02 |
| E4 | system | M1 | Danh sách Tag không có Tag hoạt động | E4.1 | FR-M05-04.02, FR-M05-04.03, BR-M05-26 |
| E5 | system | M1 | ACT-002 — User có phiên xem cùng các danh mục công khai; Mod/Admin kế thừa quyền này. Actor khởi tạo ACT-002, END:SUCCESS, dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M05-04.01, FR-M05-04.02, FR-M05-04.03, BR-M05-26 |


<!-- sc:branch SC-M05-003 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-001 | Guest mở danh sách Tag. | D-TAG; bayes/xácsuất hoạt động, abc vô hiệu hóa | E1.2 | FR-M05-04.02 |
| E1.2 | SYSTEM | Hệ thống trả các Tag hoạt động bằng tên chữ thường có#; loại abc khỏi danh sách nhưng không xóa Tag hoặc liên kết bài cũ. | #bayes, #xácsuất; không#abc | END:SUCCESS | FR-M05-04.02, FR-M05-04.03, FR-M05-03.14, BR-M05-26 |


<!-- sc:branch SC-M05-003 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-001 | Guest mở P505 công khai để đọc bài và nhãn phân loại. | P505 Đã đăng/Bình thường, ngoài nhóm, tác giả ACTIVE; Topic={Toán học}; Tag liên kết={bayes, abc}; abc vô hiệu | E2.2 | FR-M05-04.04 |
| E2.2 | SYSTEM | Hệ thống kiểm quyền đọc bài M03 rồi trả Topic Toán học và #bayes đang hoạt động; không hiện #abc, giữ liên kết abc với bài. | Nhãn Topic={Toán học}; Tag hiển thị={#bayes}; liên kết abc không xóa | END:SUCCESS | FR-M05-04.04, FR-M05-04.05, FR-M05-03.14, BR-M05-26, FR-M03-07.01 |


<!-- sc:branch SC-M05-003 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-001 | Guest mở đường dẫn P505 không có quyền đọc. | P505 thuộc Private mà Guest không là thành viên hoặc bài đang bị ẩn | E3.2 | FR-M05-04.04 |
| E3.2 | SYSTEM | Hệ thống áp cổng đọc M03, không trả bài và nhãn riêng qua M05 để vượt quyền. | Không lộ Topic/Tag của bài qua đường đọc này; danh mục công khai vẫn độc lập | END:REJECTED | FR-M05-04.04, FR-M03-07.01, FR-M03-07.02 |


<!-- sc:branch SC-M05-003 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-001 | Guest mở danh sách Tag. | Toàn bộ Tag trong snapshot đang vô hiệu hóa hoặc chưa có Tag | E4.2 | FR-M05-04.02 |
| E4.2 | SYSTEM | Hệ thống trả tập Tag hoạt động rỗng, không đưa Tag vô hiệu hóa vào để lấp danh sách. | Tag hoạt động=[] | END:SUCCESS | FR-M05-04.02, FR-M05-04.03, BR-M05-26 |


**E5 — thay toàn bộ M1 đến kết thúc:** User có phiên xem cùng các danh mục công khai; Mod/Admin kế thừa quyền này. Actor khởi tạo ACT-002, END:SUCCESS, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-003 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-002 | Lan mở danh sách Topic hoặc Tag. | loại=Topic hoặc Tag; D-CAT/D-TAG | E5.2 | FR-M05-04.01, FR-M05-04.02 |
| E5.2 | SYSTEM | Hệ thống trả toàn bộ Topic hiện tại hoặc Tag hoạt động đúng loại yêu cầu; không dùng phiên để đưa Tag vô hiệu vào danh sách. | D-CAT hoặc {#bayes, #xácsuất} | END:SUCCESS | FR-M05-04.01, FR-M05-04.02, FR-M05-04.03, BR-M05-26 |


<!-- sc:end SC-M05-003 -->

<a id="sc-m05-004"></a>

<!-- sc:scenario SC-M05-004 -->

### SC-M05-004

#### 1. Tên kịch bản chuẩn

Thêm Topic mới vào danh mục hệ thống — BF-M05-004. UC owner: [UC-M05-006](../../us/US-M05.md#uc-m05-006). Trigger: Admin An gửi yêu cầu thêm Topic Tài chính cá nhân.

#### 2. Actor thực hiện

ACT-007 — Admin — quản trị danh mục Topic là actor chính. Các quyền kế thừa giữ đúng actor hierarchy của US. Đường E tại M1 thay toàn bộ khi actor khởi tạo khác, không đổi vai trò giữa luồng.

#### 3. Tiền điều kiện

Có danh mục Topic hiện tại; kiểm vai trò Admin thực tế trong luồng. Đường chuẩn Admin An có phiên hợp lệ, Tài chính cá nhân chưa trùng tên so sánh; không quy định trường cha hoặc hạn mức danh mục mới.

#### 4. Hậu điều kiện

<!-- sc:post SC-M05-004 -->

| result | condition |
|---|---|
| SUCCESS | Một Topic mới ngang cấp được thêm nếu không trùng; có trong danh mục để chọn thủ công và AI gợi ý, không tự gán bài cũ, không giới hạn số Topic; log thao tác Admin theo M10. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không ghi nhận kết quả thành công của yêu cầu bị từ chối; không cấp thêm quyền hay tự sửa dữ liệu phân loại để vượt điều kiện. Các hiệu ứng đã hoàn tất trước yêu cầu này không bị suy thành rollback. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M05-004 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | Admin An gửi yêu cầu thêm Topic Tài chính cá nhân. | Tên=Tài chính cá nhân; không chọn Topic cha; không nhập lý do cũng hợp lệ | M2 | FR-M05-06.01 |
| M2 | SYSTEM | Hệ thống kiểm quyền Admin và so trùng không phân biệt hoa/thường, bỏ khoảng trắng thừa đầu/cuối/giữa nhưng giữ dấu. Thêm Topic ngang cấp, cho chọn khi gán/gợi ý, không tự gán vào bài cũ; ghi thao tác Admin M10 và trả Topic đã thêm. | Danh mục 11→12; Tài chính cá nhân chọn được; P505.Topic={Toán học} giữ nguyên; log Admin:An/thêm Topic/Tài chính cá nhân/lý do trống/09-11 10:00+07 | END:SUCCESS | FR-M05-06.01, FR-M05-06.03, FR-M05-06.04, FR-M05-06.05, FR-M05-06.06, FR-M05-06.07, FR-M05-06.08, BR-M05-01, BR-M05-05, BR-M05-06, BR-M05-07, FR-M10-14.01, FR-M10-14.02, FR-M10-14.09 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Bộ dữ liệu trong guard thay bộ chuẩn cho lần chạy đó; mỗi nhánh là snapshot riêng. Điểm nhập lại nêu rõ bước kiểm; nếu dữ liệu còn sai áp lại guard, không tự giới hạn số lần. REJECTED là kết thúc từ chối hợp lệ của US; không bịa nút OK/hủy/thử lại hay rollback lỗi lưu trữ chưa có nguồn.

<!-- sc:exceptions SC-M05-004 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Tên mới trùng tên hiện có sau quy tắc so sánh | E1.1 | FR-M05-06.02, FR-M05-06.08, BR-M05-05 |
| E2 | user-choice | M1 | Tên chỉ khác dấu không bị coi là trùng | E2.1 | FR-M05-06.01, FR-M05-06.08, BR-M05-05, FR-M05-06.04, FR-M05-06.05, FR-M05-06.07, BR-M05-01, BR-M05-07, FR-M10-14.01, FR-M10-14.02, FR-M10-14.09 |
| E3 | system | M2 | Danh mục đã có nhiều Topic, tên mới vẫn không trùng | E3.1 | FR-M05-06.01, FR-M05-06.04, FR-M05-06.05, FR-M05-06.06, FR-M05-06.07, FR-M05-06.08, BR-M05-06, FR-M10-14.01, FR-M10-14.02, FR-M10-14.09 |
| E4 | system | M1 | ACT-001 — Guest yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M05-06.03 |
| E5 | system | M1 | ACT-002 — User yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-002, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M05-06.03 |
| E6 | system | M1 | ACT-003 — Mod không có quyền Admin yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-003, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M05-06.03 |


<!-- sc:branch SC-M05-004 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối thêm; không tự gộp, đổi tên Topic cũ hoặc tạo bản sao. | Đã có Tin học; nhập " Tin  HỌC " cũng trùng | END:REJECTED | FR-M05-06.02, FR-M05-06.08, BR-M05-05 |


<!-- sc:branch SC-M05-004 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-007 | Admin An yêu cầu thêm Tin hoc khi đã có Tin học. | Tin hoc chưa có; Tin học đã có; các khoảng trắng thông thường | E2.2 | FR-M05-06.01, FR-M05-06.08, BR-M05-05 |
| E2.2 | SYSTEM | Hệ thống giữ khác biệt dấu khi so trùng, thêm Tin hoc ngang cấp và trả Topic mới; cho chọn/gợi ý nhưng không gán tự động vào bài cũ; ghi log Admin. | Tin hoc và Tin học là hai Topic; lý do trống được phép | END:SUCCESS | FR-M05-06.01, FR-M05-06.04, FR-M05-06.05, FR-M05-06.07, FR-M05-06.08, BR-M05-01, BR-M05-05, BR-M05-07, FR-M10-14.01, FR-M10-14.02, FR-M10-14.09 |


<!-- sc:branch SC-M05-004 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống không từ chối vì tổng số Topic; kiểm trùng/quyền như chuẩn, thêm Tài chính cá nhân ngang cấp, cho chọn/gợi ý và ghi log Admin; bài cũ giữ nguyên. | Giả lập hiện có 100 Topic gồm D-CAT, chưa có Tài chính cá nhân; 100→101, đây không phải giới hạn | END:SUCCESS | FR-M05-06.01, FR-M05-06.04, FR-M05-06.05, FR-M05-06.06, FR-M05-06.07, FR-M05-06.08, BR-M05-06, FR-M10-14.01, FR-M10-14.02, FR-M10-14.09 |


**E4 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-004 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-001 | Guest yêu cầu thêm topic mới vào danh mục hệ thống. | Vai trò thực tế không phải ADMIN; dữ liệu đối tượng như đường chuẩn | E4.2 | FR-M05-06.03 |
| E4.2 | SYSTEM | Hệ thống kiểm vai trò thực tế và từ chối; không gán quyền Admin theo tên gọi nhóm vai trò Mod/Admin. | Không thực hiện thêm/gộp/xóa từ yêu cầu này | END:REJECTED | FR-M05-06.03 |


**E5 — thay toàn bộ M1 đến kết thúc:** User yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-002, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-004 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-002 | User yêu cầu thêm topic mới vào danh mục hệ thống. | Vai trò thực tế không phải ADMIN; dữ liệu đối tượng như đường chuẩn | E5.2 | FR-M05-06.03 |
| E5.2 | SYSTEM | Hệ thống kiểm vai trò thực tế và từ chối; không gán quyền Admin theo tên gọi nhóm vai trò Mod/Admin. | Không thực hiện thêm/gộp/xóa từ yêu cầu này | END:REJECTED | FR-M05-06.03 |


**E6 — thay toàn bộ M1 đến kết thúc:** Mod không có quyền Admin yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-003, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-004 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-003 | Mod không có quyền Admin yêu cầu thêm topic mới vào danh mục hệ thống. | Vai trò thực tế không phải ADMIN; dữ liệu đối tượng như đường chuẩn | E6.2 | FR-M05-06.03 |
| E6.2 | SYSTEM | Hệ thống kiểm vai trò thực tế và từ chối; không gán quyền Admin theo tên gọi nhóm vai trò Mod/Admin. | Không thực hiện thêm/gộp/xóa từ yêu cầu này | END:REJECTED | FR-M05-06.03 |


<!-- sc:end SC-M05-004 -->

<a id="sc-m05-005"></a>

<!-- sc:scenario SC-M05-005 -->

### SC-M05-005

#### 1. Tên kịch bản chuẩn

Gộp Topic nguồn vào Topic đích — BF-M05-005. UC owner: [UC-M05-007](../../us/US-M05.md#uc-m05-007). Trigger: Admin An yêu cầu gộp Tin hoc vào Tin học.

#### 2. Actor thực hiện

ACT-007 — Admin — quản trị danh mục Topic là actor chính. Các quyền kế thừa giữ đúng actor hierarchy của US. Đường E tại M1 thay toàn bộ khi actor khởi tạo khác, không đổi vai trò giữa luồng.

#### 3. Tiền điều kiện

Danh mục có hai Topic Tin hoc và Tin học khác nhau theo dấu; kiểm quyền Admin và cặp nguồn/đích trong luồng. D-MERGE là snapshot riêng: Tin hoc gắn P510/P511/P512 thuộc mọi trạng thái nêu ở dữ liệu; không áp điều kiện xóa độc lập UC008 cho nguồn sau gộp.

#### 4. Hậu điều kiện

<!-- sc:post SC-M05-005 -->

| result | condition |
|---|---|
| SUCCESS | Mọi liên kết bài nguồn được thay bằng đích, mỗi bài chỉ có đích một lần; follow nguồn chuyển sang đích không trùng; nguồn bị bỏ khỏi danh mục và có log Admin. Không mất bài vì nguồn đang có bài ngoài nháp; đây là gộp, không là xóa độc lập. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không ghi nhận kết quả thành công của yêu cầu bị từ chối; không cấp thêm quyền hay tự sửa dữ liệu phân loại để vượt điều kiện. Các hiệu ứng đã hoàn tất trước yêu cầu này không bị suy thành rollback. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M05-005 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | Admin An yêu cầu gộp Tin hoc vào Tin học. | Nguồn=Tin hoc; đích=Tin học; P510 Nháp:{Tin hoc}; P511 Đã đăng:{Tin hoc, Tin học, Toán học}; P512 Đã xóa còn khôi phục:{Tin hoc}; follow nguồn={U1, U2}, đích={U2, U3} | M2 | FR-M05-07.01 |
| M2 | SYSTEM | Hệ thống kiểm Admin, nguồn/đích khác nhau; chuyển mọi bài có nguồn sang đích thay nguồn, loại liên kết trùng. Chuyển người theo dõi nguồn sang đích chỉ khi chưa theo, xóa nguồn khỏi danh mục sau gộp; ghi log Admin rồi trả kết quả toàn bộ thao tác. | P510:{Tin học}; P511:{Tin học, Toán học}; P512:{Tin học}; follow đích={U1, U2, U3}; không trùng U2; Tin hoc không còn danh mục; log An/gộp/Tin hoc→Tin học/lý do trống/10:05+07 | END:SUCCESS | FR-M05-07.01, FR-M05-07.02, FR-M05-07.03, FR-M05-07.05, FR-M05-07.06, BR-M05-09, FR-M10-14.01, FR-M10-14.02, FR-M10-14.09 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Bộ dữ liệu trong guard thay bộ chuẩn cho lần chạy đó; mỗi nhánh là snapshot riêng. Điểm nhập lại nêu rõ bước kiểm; nếu dữ liệu còn sai áp lại guard, không tự giới hạn số lần. REJECTED là kết thúc từ chối hợp lệ của US; không bịa nút OK/hủy/thử lại hay rollback lỗi lưu trữ chưa có nguồn.

<!-- sc:exceptions SC-M05-005 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Cùng Topic làm cả nguồn và đích | E1.1 | FR-M05-07.04 |
| E2 | user-choice | M1 | Admin chọn cặp khác, chưa có liên kết trùng đích | E2.1 | FR-M05-07.01, FR-M05-07.05, FR-M05-07.06, BR-M05-09, FR-M10-14.01, FR-M10-14.02, FR-M10-14.09 |
| E3 | system | M1 | ACT-001 — Guest yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E3.1 | FR-M05-07.03 |
| E4 | system | M1 | ACT-002 — User yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-002, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M05-07.03 |
| E5 | system | M1 | ACT-003 — Mod không có quyền Admin yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-003, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M05-07.03 |


<!-- sc:branch SC-M05-005 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối gộp một Topic với chính nó; không chuyển bài/follow hoặc bỏ Topic. | Nguồn=Tin học; đích=Tin học | END:REJECTED | FR-M05-07.04 |


<!-- sc:branch SC-M05-005 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-007 | Admin An gộp Tài chính cá nhân vào Hướng nghiệp. | Hai Topic khác nhau; P513:{Tài chính cá nhân, Khác}; follow nguồn={U4}, đích={U5}; không có bài trùng đích | E2.2 | FR-M05-07.01 |
| E2.2 | SYSTEM | Hệ thống kiểm Admin/cặp khác nhau, chuyển P513 sang Hướng nghiệp, chuyển follow U4, bỏ nguồn, ghi log và trả kết quả. | P513:{Hướng nghiệp, Khác}; follow Hướng nghiệp={U4, U5}; nguồn không còn | END:SUCCESS | FR-M05-07.01, FR-M05-07.05, FR-M05-07.06, BR-M05-09, FR-M10-14.01, FR-M10-14.02, FR-M10-14.09 |


**E3 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-005 E3 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E3.1 | ACT-001 | Guest yêu cầu gộp topic nguồn vào topic đích. | Vai trò thực tế không phải ADMIN; dữ liệu đối tượng như đường chuẩn | E3.2 | FR-M05-07.03 |
| E3.2 | SYSTEM | Hệ thống kiểm vai trò thực tế và từ chối; không gán quyền Admin theo tên gọi nhóm vai trò Mod/Admin. | Không thực hiện thêm/gộp/xóa từ yêu cầu này | END:REJECTED | FR-M05-07.03 |


**E4 — thay toàn bộ M1 đến kết thúc:** User yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-002, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-005 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-002 | User yêu cầu gộp topic nguồn vào topic đích. | Vai trò thực tế không phải ADMIN; dữ liệu đối tượng như đường chuẩn | E4.2 | FR-M05-07.03 |
| E4.2 | SYSTEM | Hệ thống kiểm vai trò thực tế và từ chối; không gán quyền Admin theo tên gọi nhóm vai trò Mod/Admin. | Không thực hiện thêm/gộp/xóa từ yêu cầu này | END:REJECTED | FR-M05-07.03 |


**E5 — thay toàn bộ M1 đến kết thúc:** Mod không có quyền Admin yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-003, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-005 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-003 | Mod không có quyền Admin yêu cầu gộp topic nguồn vào topic đích. | Vai trò thực tế không phải ADMIN; dữ liệu đối tượng như đường chuẩn | E5.2 | FR-M05-07.03 |
| E5.2 | SYSTEM | Hệ thống kiểm vai trò thực tế và từ chối; không gán quyền Admin theo tên gọi nhóm vai trò Mod/Admin. | Không thực hiện thêm/gộp/xóa từ yêu cầu này | END:REJECTED | FR-M05-07.03 |


<!-- sc:end SC-M05-005 -->

<a id="sc-m05-006"></a>

<!-- sc:scenario SC-M05-006 -->

### SC-M05-006

#### 1. Tên kịch bản chuẩn

Xóa Topic không có bài viết ngoài nháp — BF-M05-006. UC owner: [UC-M05-008](../../us/US-M05.md#uc-m05-008). Trigger: Admin An yêu cầu xóa Topic Thử nghiệm.

#### 2. Actor thực hiện

ACT-007 — Admin — quản trị danh mục Topic là actor chính. Các quyền kế thừa giữ đúng actor hierarchy của US. Đường E tại M1 thay toàn bộ khi actor khởi tạo khác, không đổi vai trò giữa luồng.

#### 3. Tiền điều kiện

Có Topic cần xóa; không giả định đã rỗng trước khi kiểm. Đường chuẩn Admin An có phiên; Topic Thử nghiệm chỉ gắn hai nháp P520/P521, có 2 lượt theo dõi; là Topic giả lập đã được thêm hợp lệ, không thay danh mục 11 ban đầu.

#### 4. Hậu điều kiện

<!-- sc:post SC-M05-006 -->

| result | condition |
|---|---|
| SUCCESS | Topic đủ điều kiện không còn danh mục/được chọn/gợi ý; bỏ khỏi nháp và bỏ mọi follow; nháp còn 0 Topic vẫn hợp lệ. Có log Admin. Không xóa bài để hợp thức hóa việc xóa Topic. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không ghi nhận kết quả thành công của yêu cầu bị từ chối; không cấp thêm quyền hay tự sửa dữ liệu phân loại để vượt điều kiện. Các hiệu ứng đã hoàn tất trước yêu cầu này không bị suy thành rollback. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M05-006 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-007 | Admin An yêu cầu xóa Topic Thử nghiệm. | P520 Nháp:{Thử nghiệm}; P521 Nháp:{Thử nghiệm, Toán học}; follow={U1, U2} | M2 | FR-M05-08.01 |
| M2 | SYSTEM | Hệ thống kiểm Admin và toàn bộ liên kết bài, xác nhận không có bài ngoài nháp; xóa Topic khỏi danh mục, bỏ khỏi các nháp và bỏ mọi follow Topic đó. Không cho chọn/gợi ý Topic đã xóa; ghi log Admin và trả kết quả xóa. | P520.Topic=[]; P521.Topic={Toán học}; follow Thử nghiệm=[]; không còn danh mục; log An/xóa/Thử nghiệm/lý do trống/10:10+07 | END:SUCCESS | FR-M05-08.01, FR-M05-08.03, FR-M05-08.04, FR-M05-08.05, FR-M05-08.06, BR-M05-08, FR-M10-14.01, FR-M10-14.02, FR-M10-14.09 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Bộ dữ liệu trong guard thay bộ chuẩn cho lần chạy đó; mỗi nhánh là snapshot riêng. Điểm nhập lại nêu rõ bước kiểm; nếu dữ liệu còn sai áp lại guard, không tự giới hạn số lần. REJECTED là kết thúc từ chối hợp lệ của US; không bịa nút OK/hủy/thử lại hay rollback lỗi lưu trữ chưa có nguồn.

<!-- sc:exceptions SC-M05-006 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Topic còn ít nhất một bài ngoài nháp: Chờ duyệt | E1.1 | FR-M05-08.02, BR-M05-08, FR-M03-17.02 |
| E2 | system | M2 | Topic còn ít nhất một bài ngoài nháp: Đã đăng | E2.1 | FR-M05-08.02, BR-M05-08, FR-M03-17.02 |
| E3 | system | M2 | Topic còn ít nhất một bài ngoài nháp: Tự ẩn | E3.1 | FR-M05-08.02, BR-M05-08, FR-M03-17.02 |
| E4 | system | M2 | Topic còn ít nhất một bài ngoài nháp: Bị từ chối | E4.1 | FR-M05-08.02, BR-M05-08, FR-M03-17.02 |
| E5 | system | M2 | Topic còn ít nhất một bài ngoài nháp: Đã xóa 2 ngày trước, còn 7 ngày khôi phục | E5.1 | FR-M05-08.02, BR-M05-08, FR-M03-17.02 |
| E6 | system | M2 | Topic còn ít nhất một bài ngoài nháp: Đã xóa hẳn nhưng M03 vẫn giữ liên kết bài–Topic | E6.1 | FR-M05-08.02, BR-M05-08, FR-M03-17.02 |
| E7 | system | M2 | Topic chưa có bài viết nào, cũng không có follow | E7.1 | FR-M05-08.01, FR-M05-08.04, FR-M05-08.05, FR-M05-08.06, BR-M05-08, FR-M10-14.01, FR-M10-14.02, FR-M10-14.09 |
| E8 | system | M1 | ACT-001 — Guest yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M05-08.03 |
| E9 | system | M1 | ACT-002 — User yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-002, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M05-08.03 |
| E10 | system | M1 | ACT-003 — Mod không có quyền Admin yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-003, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M05-08.03 |


<!-- sc:branch SC-M05-006 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối xóa Topic; không dọn liên kết bài, xóa bài hoặc tự chuyển sang gộp để vượt điều kiện. | Một bài gắn Thử nghiệm ở trạng thái Chờ duyệt; các nháp có thể vẫn tồn tại | END:REJECTED | FR-M05-08.02, BR-M05-08, FR-M03-17.02 |


<!-- sc:branch SC-M05-006 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối xóa Topic; không dọn liên kết bài, xóa bài hoặc tự chuyển sang gộp để vượt điều kiện. | Một bài gắn Thử nghiệm ở trạng thái Đã đăng; các nháp có thể vẫn tồn tại | END:REJECTED | FR-M05-08.02, BR-M05-08, FR-M03-17.02 |


<!-- sc:branch SC-M05-006 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối xóa Topic; không dọn liên kết bài, xóa bài hoặc tự chuyển sang gộp để vượt điều kiện. | Một bài gắn Thử nghiệm ở trạng thái Tự ẩn; các nháp có thể vẫn tồn tại | END:REJECTED | FR-M05-08.02, BR-M05-08, FR-M03-17.02 |


<!-- sc:branch SC-M05-006 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối xóa Topic; không dọn liên kết bài, xóa bài hoặc tự chuyển sang gộp để vượt điều kiện. | Một bài gắn Thử nghiệm ở trạng thái Bị từ chối; các nháp có thể vẫn tồn tại | END:REJECTED | FR-M05-08.02, BR-M05-08, FR-M03-17.02 |


<!-- sc:branch SC-M05-006 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối xóa Topic; không dọn liên kết bài, xóa bài hoặc tự chuyển sang gộp để vượt điều kiện. | Một bài gắn Thử nghiệm ở trạng thái Đã xóa 2 ngày trước, còn 7 ngày khôi phục; các nháp có thể vẫn tồn tại | END:REJECTED | FR-M05-08.02, BR-M05-08, FR-M03-17.02 |


<!-- sc:branch SC-M05-006 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối xóa Topic; không dọn liên kết bài, xóa bài hoặc tự chuyển sang gộp để vượt điều kiện. | Một bài gắn Thử nghiệm ở trạng thái Đã xóa hẳn nhưng M03 vẫn giữ liên kết bài–Topic; các nháp có thể vẫn tồn tại | END:REJECTED | FR-M05-08.02, BR-M05-08, FR-M03-17.02 |


<!-- sc:branch SC-M05-006 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống kiểm Admin và không có bài ngoài nháp, xóa Topic khỏi danh mục, không cho chọn/gợi ý, ghi log và trả thành công; không cần tạo dữ liệu nháp/follow để xóa. | Topic Thử nghiệm: bài=[], follow=[]; sau xóa không còn danh mục | END:SUCCESS | FR-M05-08.01, FR-M05-08.04, FR-M05-08.05, FR-M05-08.06, BR-M05-08, FR-M10-14.01, FR-M10-14.02, FR-M10-14.09 |


**E8 — thay toàn bộ M1 đến kết thúc:** Guest yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-006 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-001 | Guest yêu cầu xóa topic không có bài viết ngoài nháp. | Vai trò thực tế không phải ADMIN; dữ liệu đối tượng như đường chuẩn | E8.2 | FR-M05-08.03 |
| E8.2 | SYSTEM | Hệ thống kiểm vai trò thực tế và từ chối; không gán quyền Admin theo tên gọi nhóm vai trò Mod/Admin. | Không thực hiện thêm/gộp/xóa từ yêu cầu này | END:REJECTED | FR-M05-08.03 |


**E9 — thay toàn bộ M1 đến kết thúc:** User yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-002, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-006 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-002 | User yêu cầu xóa topic không có bài viết ngoài nháp. | Vai trò thực tế không phải ADMIN; dữ liệu đối tượng như đường chuẩn | E9.2 | FR-M05-08.03 |
| E9.2 | SYSTEM | Hệ thống kiểm vai trò thực tế và từ chối; không gán quyền Admin theo tên gọi nhóm vai trò Mod/Admin. | Không thực hiện thêm/gộp/xóa từ yêu cầu này | END:REJECTED | FR-M05-08.03 |


**E10 — thay toàn bộ M1 đến kết thúc:** Mod không có quyền Admin yêu cầu chức năng chỉ Admin. Actor khởi tạo ACT-003, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-006 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-003 | Mod không có quyền Admin yêu cầu xóa topic không có bài viết ngoài nháp. | Vai trò thực tế không phải ADMIN; dữ liệu đối tượng như đường chuẩn | E10.2 | FR-M05-08.03 |
| E10.2 | SYSTEM | Hệ thống kiểm vai trò thực tế và từ chối; không gán quyền Admin theo tên gọi nhóm vai trò Mod/Admin. | Không thực hiện thêm/gộp/xóa từ yêu cầu này | END:REJECTED | FR-M05-08.03 |


<!-- sc:end SC-M05-006 -->

<a id="sc-m05-007"></a>

<!-- sc:scenario SC-M05-007 -->

### SC-M05-007

#### 1. Tên kịch bản chuẩn

Vô hiệu hóa Tag trong tình huống khủng hoảng — BF-M05-007. UC owner: [UC-M05-009](../../us/US-M05.md#uc-m05-009). Trigger: Mod Mai yêu cầu vô hiệu hóa #abc, có thể kèm lý do.

#### 2. Actor thực hiện

ACT-003 — Mod / Admin — quyền điều phối chung là actor chính. Các quyền kế thừa giữ đúng actor hierarchy của US. Đường E tại M1 thay toàn bộ khi actor khởi tạo khác, không đổi vai trò giữa luồng.

#### 3. Tiền điều kiện

Mod Mai có phiên và đánh giá Tag cần ngừng hiển thị trong khủng hoảng; không tự đặt tiêu chí khủng hoảng hoặc bắt lý do. Tag abc đang hoạt động ở đường chuẩn; P530 đã liên kết abc, P531 chưa liên kết; trạng thái/quyền kiểm trong luồng.

#### 4. Hậu điều kiện

<!-- sc:post SC-M05-007 -->

| result | condition |
|---|---|
| SUCCESS | Tag bị vô hiệu hóa, vẫn tồn tại cùng liên kết cũ, không hiển thị/gắn mới dưới dạng Tag. Ghi nhật ký kiểm duyệt cho thao tác có thay đổi theo nguồn; nếu người thực hiện là Admin có thêm nhật ký Admin. Yêu cầu lặp giữ trạng thái theo nhánh, không tự cam kết log lặp ngoài nguồn. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không ghi nhận kết quả thành công của yêu cầu bị từ chối; không cấp thêm quyền hay tự sửa dữ liệu phân loại để vượt điều kiện. Các hiệu ứng đã hoàn tất trước yêu cầu này không bị suy thành rollback. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M05-007 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-003 | Mod Mai yêu cầu vô hiệu hóa #abc, có thể kèm lý do. | abc hoạt động; P530.Tag={abc, bayes}; lý do giả lập=Ngừng hiển thị trong khủng hoảng | M2 | FR-M05-09.01 |
| M2 | SYSTEM | Hệ thống kiểm quyền Mod/Admin và trạng thái, chuyển abc sang vô hiệu hóa; giữ Tag/liên kết P530, ngừng hiện trong gợi ý, tìm Tag, danh sách, Trending và nhãn bài. Lần nhập mới tên abc chỉ thành văn bản, không liên kết mới. Ghi nhật ký kiểm duyệt rồi trả Tag đã vô hiệu hóa. | abc vô hiệu; P530 liên kết abc vẫn còn nhưng không hiện; P531 nhập#abc chỉ là chữ; log Mai/vô hiệu Tag/abc/lý do đã nhập/10:15+07 | END:SUCCESS | FR-M05-09.01, FR-M05-09.02, FR-M05-09.03, FR-M05-09.07, FR-M05-03.09, FR-M05-04.03, FR-M05-04.05, FR-M05-05.07, BR-M05-26, FR-M08-16.02, FR-M06-03.04 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Bộ dữ liệu trong guard thay bộ chuẩn cho lần chạy đó; mỗi nhánh là snapshot riêng. Điểm nhập lại nêu rõ bước kiểm; nếu dữ liệu còn sai áp lại guard, không tự giới hạn số lần. REJECTED là kết thúc từ chối hợp lệ của US; không bịa nút OK/hủy/thử lại hay rollback lỗi lưu trữ chưa có nguồn.

<!-- sc:exceptions SC-M05-007 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Tag đã bị vô hiệu hóa từ trước | E1.1 | FR-M05-09.05, BR-M05-26 |
| E2 | user-choice | M1 | Mod không nhập lý do | E2.1 | FR-M05-09.01, FR-M05-09.07, FR-M05-09.02, FR-M05-09.03, BR-M05-26, FR-M08-16.02 |
| E3 | system | M2 | Phiên hoặc vai trò điều phối không còn hợp lệ khi yêu cầu | E3.1 | FR-M05-09.04, FR-M01-06.04 |
| E4 | system | M1 | ACT-001 — Guest không có quyền điều phối. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M05-09.04 |
| E5 | system | M1 | ACT-002 — User không phải tác giả đối tượng khi đổi bài không có quyền điều phối. Actor khởi tạo ACT-002, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M05-09.04 |
| E6 | system | M1 | ACT-007 — Admin thực hiện cùng chức năng với quyền điều phối kế thừa. Actor khởi tạo ACT-007, END:SUCCESS, dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M05-09.01, FR-M05-09.02, FR-M05-09.03, FR-M05-09.07, FR-M05-03.09, FR-M05-04.03, FR-M05-04.05, FR-M05-05.07, BR-M05-26, FR-M08-16.02, FR-M06-03.04, FR-M10-14.01, FR-M10-14.02, FR-M10-14.03, FR-M10-14.09 |


<!-- sc:branch SC-M05-007 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống giữ abc ở trạng thái vô hiệu hóa, giữ liên kết cũ và trả trạng thái hiện tại; không xóa Tag hay tái tạo Tag khác. Nguồn chưa quy định có thêm log cho yêu cầu không đổi trạng thái. | abc vẫn vô hiệu; P530 liên kết giữ; chưa khẳng định số log tăng | END:SUCCESS | FR-M05-09.05, BR-M05-26 |


<!-- sc:branch SC-M05-007 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-003 | Mod Mai yêu cầu vô hiệu hóa #abc, để trống lý do. | abc hoạt động; lý do trống | E2.2 | FR-M05-09.01, FR-M05-09.07 |
| E2.2 | SYSTEM | Hệ thống kiểm quyền/trạng thái, vô hiệu hóa abc, giữ liên kết cũ và ngừng hiển thị/gắn mới theo quy tắc; ghi log với lý do trống và trả kết quả. | log Mai/vô hiệu Tag/abc/lý do trống/10:15+07; abc vô hiệu | END:SUCCESS | FR-M05-09.01, FR-M05-09.02, FR-M05-09.03, FR-M05-09.07, BR-M05-26, FR-M08-16.02 |


<!-- sc:branch SC-M05-007 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối thao tác cần quyền; không dùng kết quả quyền cũ để tiếp tục. | Snapshot: mất vai trò điều phối hoặc phiên làm mới đã hết30 ngày | END:REJECTED | FR-M05-09.04, FR-M01-06.04 |


**E4 — thay toàn bộ M1 đến kết thúc:** Guest không có quyền điều phối. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-007 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-001 | Guest yêu cầu vô hiệu hóa tag trong tình huống khủng hoảng. | Không có vai trò Mod/Admin; P540 của Lan nếu là đổi phân loại | E4.2 | FR-M05-09.04 |
| E4.2 | SYSTEM | Hệ thống từ chối, không thay trạng thái Tag hay phân loại bài từ yêu cầu không quyền. | Không ghi kết quả điều phối thành công | END:REJECTED | FR-M05-09.04 |


**E5 — thay toàn bộ M1 đến kết thúc:** User không phải tác giả đối tượng khi đổi bài không có quyền điều phối. Actor khởi tạo ACT-002, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-007 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-002 | User không phải tác giả đối tượng khi đổi bài yêu cầu vô hiệu hóa tag trong tình huống khủng hoảng. | Không có vai trò Mod/Admin; P540 của Lan nếu là đổi phân loại | E5.2 | FR-M05-09.04 |
| E5.2 | SYSTEM | Hệ thống từ chối, không thay trạng thái Tag hay phân loại bài từ yêu cầu không quyền. | Không ghi kết quả điều phối thành công | END:REJECTED | FR-M05-09.04 |


**E6 — thay toàn bộ M1 đến kết thúc:** Admin thực hiện cùng chức năng với quyền điều phối kế thừa. Actor khởi tạo ACT-007, END:SUCCESS, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-007 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-007 | Admin An yêu cầu vô hiệu hóa #abc, có thể kèm lý do. | abc hoạt động; P530.Tag={abc, bayes}; lý do giả lập=Ngừng hiển thị trong khủng hoảng | E6.2 | FR-M05-09.01 |
| E6.2 | SYSTEM | Hệ thống kiểm quyền Mod/Admin và trạng thái, chuyển abc sang vô hiệu hóa; giữ Tag/liên kết P530, ngừng hiện trong gợi ý, tìm Tag, danh sách, Trending và nhãn bài. Lần nhập mới tên abc chỉ thành văn bản, không liên kết mới. Ghi nhật ký kiểm duyệt rồi trả Tag đã vô hiệu hóa. Đồng thời ghi thêm một mục nhật ký thao tác Admin riêng, không thay thế nhật ký kiểm duyệt. | abc vô hiệu; P530 liên kết abc vẫn còn nhưng không hiện; P531 nhập#abc chỉ là chữ; log An/vô hiệu Tag/abc/lý do đã nhập/10:15+07 | END:SUCCESS | FR-M05-09.01, FR-M05-09.02, FR-M05-09.03, FR-M05-09.07, FR-M05-03.09, FR-M05-04.03, FR-M05-04.05, FR-M05-05.07, BR-M05-26, FR-M08-16.02, FR-M06-03.04, FR-M10-14.01, FR-M10-14.02, FR-M10-14.03, FR-M10-14.09 |


<!-- sc:end SC-M05-007 -->

<a id="sc-m05-008"></a>

<!-- sc:scenario SC-M05-008 -->

### SC-M05-008

#### 1. Tên kịch bản chuẩn

Kích hoạt lại Tag đã vô hiệu hóa — BF-M05-008. UC owner: [UC-M05-010](../../us/US-M05.md#uc-m05-010). Trigger: Mod Mai yêu cầu kích hoạt lại #abc.

#### 2. Actor thực hiện

ACT-003 — Mod / Admin — quyền điều phối chung là actor chính. Các quyền kế thừa giữ đúng actor hierarchy của US. Đường E tại M1 thay toàn bộ khi actor khởi tạo khác, không đổi vai trò giữa luồng.

#### 3. Tiền điều kiện

Mod Mai có phiên; kiểm quyền và trạng thái Tag trong luồng. Đường chuẩn abc đang vô hiệu, P530 giữ liên kết abc; P531 chỉ có chữ #abc nhập trong lúc vô hiệu, không có liên kết abc. Trending chỉ nhận Tag đủ điểm dương theo kỳ tính M05.

#### 4. Hậu điều kiện

<!-- sc:post SC-M05-008 -->

| result | condition |
|---|---|
| SUCCESS | Tag hoạt động; các liên kết cũ còn giữ được hiển thị lại, phần chữ nhập khi vô hiệu không tự thành liên kết. Có log kiểm duyệt và thêm log Admin nếu Admin thực hiện; Trending vẫn theo kỳ tính gần nhất và điều kiện điểm>0, không tự tính realtime. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không ghi nhận kết quả thành công của yêu cầu bị từ chối; không cấp thêm quyền hay tự sửa dữ liệu phân loại để vượt điều kiện. Các hiệu ứng đã hoàn tất trước yêu cầu này không bị suy thành rollback. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M05-008 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-003 | Mod Mai yêu cầu kích hoạt lại #abc. | abc vô hiệu; P530 có liên kết; P531 chỉ có chữ; lý do tùy chọn=Khủng hoảng đã qua | M2 | FR-M05-10.01 |
| M2 | SYSTEM | Hệ thống kiểm quyền/trạng thái, chuyển abc sang hoạt động; cho hiển thị lại trong gợi ý, danh sách, trên P530 còn liên kết và Trending theo điểm/kỳ tính. Không biến chữ #abc của P531 thành Tag. Ghi log kiểm duyệt và trả Tag hoạt động. | abc hoạt động; P530 hiện#abc; P531 vẫn chỉ chữ; log Mai/kích hoạt Tag/abc/lý do đã nhập/10:20+07; không tạo hạng Trending điểm0 | END:SUCCESS | FR-M05-10.01, FR-M05-10.02, FR-M05-10.03, FR-M05-10.06, FR-M05-05.10, FR-M05-05.14, BR-M05-27, BR-M05-30, BR-M05-31, FR-M08-16.02 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Bộ dữ liệu trong guard thay bộ chuẩn cho lần chạy đó; mỗi nhánh là snapshot riêng. Điểm nhập lại nêu rõ bước kiểm; nếu dữ liệu còn sai áp lại guard, không tự giới hạn số lần. REJECTED là kết thúc từ chối hợp lệ của US; không bịa nút OK/hủy/thử lại hay rollback lỗi lưu trữ chưa có nguồn.

<!-- sc:exceptions SC-M05-008 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Tag đã hoạt động | E1.1 | FR-M05-10.03, FR-M05-10.05, BR-M05-27 |
| E2 | system | M2 | Tag được kích hoạt lại nhưng điểm Trending gần nhất bằng0 hoặc chưa có kỳ tính sau kích hoạt | E2.1 | FR-M05-10.01, FR-M05-10.02, FR-M05-10.03, FR-M05-10.06, FR-M05-05.07, FR-M05-05.10, FR-M05-05.14, BR-M05-27, BR-M05-30, BR-M05-31, FR-M08-16.02 |
| E3 | user-choice | M1 | Mod để trống lý do khi kích hoạt lại | E3.1 | FR-M05-10.01, FR-M05-10.06, FR-M05-10.02, FR-M05-10.03, BR-M05-27, BR-M05-30, BR-M05-31, FR-M08-16.02 |
| E4 | system | M2 | Phiên hoặc vai trò điều phối không còn hợp lệ khi yêu cầu | E4.1 | FR-M05-10.04, FR-M01-06.04 |
| E5 | system | M1 | ACT-001 — Guest không có quyền điều phối. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M05-10.04 |
| E6 | system | M1 | ACT-002 — User không phải tác giả đối tượng khi đổi bài không có quyền điều phối. Actor khởi tạo ACT-002, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M05-10.04 |
| E7 | system | M1 | ACT-007 — Admin thực hiện cùng chức năng với quyền điều phối kế thừa. Actor khởi tạo ACT-007, END:SUCCESS, dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M05-10.01, FR-M05-10.02, FR-M05-10.03, FR-M05-10.06, FR-M05-05.10, FR-M05-05.14, BR-M05-27, BR-M05-30, BR-M05-31, FR-M08-16.02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.03, FR-M10-14.09 |


<!-- sc:branch SC-M05-008 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống giữ abc hoạt động, trả trạng thái hiện tại; không thêm liên kết P531 từ chữ nhập trước. Không tự quy định log cho lần không đổi trạng thái. | abc hoạt động trước/sau; P531.Tag không có abc | END:SUCCESS | FR-M05-10.03, FR-M05-10.05, BR-M05-27 |


<!-- sc:branch SC-M05-008 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống kích hoạt abc, hiện lại danh sách/gợi ý/nhãn liên kết cũ và ghi log; Trending vẫn dùng kỳ gần nhất, chỉ có hạng khi dữ liệu đủ điều kiện cho điểm>0. Không tạo hạng điểm0 hoặc tự chọn chu kỳ mới. | abc hoạt động; P530 hiện#abc; P531 vẫn chữ; kỳ10:00 chưa có hạng abc, kỳ kế trong chu kỳ15–30 phút | END:SUCCESS | FR-M05-10.01, FR-M05-10.02, FR-M05-10.03, FR-M05-10.06, FR-M05-05.07, FR-M05-05.10, FR-M05-05.14, BR-M05-27, BR-M05-30, BR-M05-31, FR-M08-16.02 |


<!-- sc:branch SC-M05-008 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-003 | Mod Mai yêu cầu kích hoạt abc, không nhập lý do. | abc vô hiệu; lý do trống | E3.2 | FR-M05-10.01, FR-M05-10.06 |
| E3.2 | SYSTEM | Hệ thống kiểm quyền/trạng thái, kích hoạt abc, cho hiển thị liên kết cũ và giữ phần chữ P531; ghi log với lý do trống và trả kết quả. Trending tuân điểm dương/kỳ tính. | abc hoạt động; log Mai/kích hoạt Tag/abc/lý do trống/10:20+07 | END:SUCCESS | FR-M05-10.01, FR-M05-10.02, FR-M05-10.03, FR-M05-10.06, BR-M05-27, BR-M05-30, BR-M05-31, FR-M08-16.02 |


<!-- sc:branch SC-M05-008 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối thao tác cần quyền; không dùng kết quả quyền cũ để tiếp tục. | Snapshot: mất vai trò điều phối hoặc phiên làm mới đã hết30 ngày | END:REJECTED | FR-M05-10.04, FR-M01-06.04 |


**E5 — thay toàn bộ M1 đến kết thúc:** Guest không có quyền điều phối. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-008 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-001 | Guest yêu cầu kích hoạt lại tag đã vô hiệu hóa. | Không có vai trò Mod/Admin; P540 của Lan nếu là đổi phân loại | E5.2 | FR-M05-10.04 |
| E5.2 | SYSTEM | Hệ thống từ chối, không thay trạng thái Tag hay phân loại bài từ yêu cầu không quyền. | Không ghi kết quả điều phối thành công | END:REJECTED | FR-M05-10.04 |


**E6 — thay toàn bộ M1 đến kết thúc:** User không phải tác giả đối tượng khi đổi bài không có quyền điều phối. Actor khởi tạo ACT-002, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-008 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-002 | User không phải tác giả đối tượng khi đổi bài yêu cầu kích hoạt lại tag đã vô hiệu hóa. | Không có vai trò Mod/Admin; P540 của Lan nếu là đổi phân loại | E6.2 | FR-M05-10.04 |
| E6.2 | SYSTEM | Hệ thống từ chối, không thay trạng thái Tag hay phân loại bài từ yêu cầu không quyền. | Không ghi kết quả điều phối thành công | END:REJECTED | FR-M05-10.04 |


**E7 — thay toàn bộ M1 đến kết thúc:** Admin thực hiện cùng chức năng với quyền điều phối kế thừa. Actor khởi tạo ACT-007, END:SUCCESS, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-008 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-007 | Admin An yêu cầu kích hoạt lại #abc. | abc vô hiệu; P530 có liên kết; P531 chỉ có chữ; lý do tùy chọn=Khủng hoảng đã qua | E7.2 | FR-M05-10.01 |
| E7.2 | SYSTEM | Hệ thống kiểm quyền/trạng thái, chuyển abc sang hoạt động; cho hiển thị lại trong gợi ý, danh sách, trên P530 còn liên kết và Trending theo điểm/kỳ tính. Không biến chữ #abc của P531 thành Tag. Ghi log kiểm duyệt và trả Tag hoạt động. Đồng thời ghi thêm một mục nhật ký thao tác Admin riêng, không thay thế nhật ký kiểm duyệt. | abc hoạt động; P530 hiện#abc; P531 vẫn chỉ chữ; log An/kích hoạt Tag/abc/lý do đã nhập/10:20+07; không tạo hạng Trending điểm0 | END:SUCCESS | FR-M05-10.01, FR-M05-10.02, FR-M05-10.03, FR-M05-10.06, FR-M05-05.10, FR-M05-05.14, BR-M05-27, BR-M05-30, BR-M05-31, FR-M08-16.02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.03, FR-M10-14.09 |


<!-- sc:end SC-M05-008 -->

<a id="sc-m05-009"></a>

<!-- sc:scenario SC-M05-009 -->

### SC-M05-009

#### 1. Tên kịch bản chuẩn

Đổi Topic và Tag trên bài viết của người khác — BF-M05-009. UC owner: [UC-M05-011](../../us/US-M05.md#uc-m05-011). Trigger: Mod Mai yêu cầu đổi phân loại P540 của Lan.

#### 2. Actor thực hiện

ACT-003 — Mod / Admin — quyền điều phối chung là actor chính. Các quyền kế thừa giữ đúng actor hierarchy của US. Đường E tại M1 thay toàn bộ khi actor khởi tạo khác, không đổi vai trò giữa luồng.

#### 3. Tiền điều kiện

Có bài P540 của Lan mà Mod Mai được quyền tiếp cận và điều phối theo M03/M01; đường chuẩn Đã đăng/Bình thường, ngoài nhóm. Không cấp quyền sửa tiêu đề/nội dung/tệp bằng chức năng phân loại. Topic trước={Tin học}, Tag={bayes}; kiểm giới hạn khi lưu, không giả định thay đổi luôn hợp lệ.

#### 4. Hậu điều kiện

<!-- sc:post SC-M05-009 -->

| result | condition |
|---|---|
| SUCCESS | Phân loại hợp lệ cuối được lưu: Topic 1–3 hiện hành, Tag 0–5 chuẩn hóa; không AI trên bài người khác, không báo tác giả/không lịch sử sửa công khai. Có log kiểm duyệt; Admin làm cùng thao tác còn có log Admin; các trường nội dung không thuộc quyền đổi phân loại giữ nguyên. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard, không ghi nhận kết quả thành công của yêu cầu bị từ chối; không cấp thêm quyền hay tự sửa dữ liệu phân loại để vượt điều kiện. Các hiệu ứng đã hoàn tất trước yêu cầu này không bị suy thành rollback. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M05-009 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-003 | Mod Mai yêu cầu đổi phân loại P540 của Lan. | P540.Topic={Tin học}; Tag={bayes}; Mai khác tác giả | M2 | FR-M05-11.01, FR-M05-11.02 |
| M2 | SYSTEM | Hệ thống kiểm quyền điều phối và trạng thái bài, trả phân loại/danh mục hiện tại; không cung cấp AI gợi ý trên bài người khác, không mở quyền sửa nội dung bài. | Topic={Tin học}; Tag={bayes}; danh mục D-CAT, D-TAG | M3 | FR-M05-11.04, FR-M05-02.21, FR-M03-11.04, FR-M03-11.07 |
| M3 | ACT-003 | Mod Mai bỏ Tin học, chọn Toán học, thay #bayes bằng #XácSuất và lưu. | Topic cuối={Toán học}; Tag cuối={XácSuất}; lý do tùy chọn=Điều chỉnh phân loại | M4 | FR-M05-11.01, FR-M05-11.02 |
| M4 | SYSTEM | Hệ thống kiểm Topic 1–3 thuộc danh mục, Tag 0–5 đúng tên/chuẩn hóa/trạng thái, dùng lại hoặc tạo Tag theo tập vừa gửi; lưu và trả đúng phân loại cuối. Ghi log kiểm duyệt, không gửi thông báo cho tác giả, không ghi lần đổi này vào lịch sử sửa công khai; không dùng AI. | Đường chuẩn P540.Topic={Toán học}; Tag={xácsuất}; khi nhập lại từ nhánh dùng chính tập Topic/Tag/lý do của bước gửi gần nhất. Log Mai/đổi phân loại/P540/lý do nếu có/10:25+07; title/body/tệp giữ nguyên | END:SUCCESS | FR-M05-11.01, FR-M05-11.02, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-02.21, FR-M05-01.01, FR-M05-01.02, FR-M05-01.03, FR-M05-01.04, FR-M05-01.05, FR-M05-01.07, FR-M05-01.09, FR-M05-01.10, BR-M05-03, BR-M05-04, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.05, FR-M05-03.06, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-20, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-26, FR-M08-16.02, FR-M03-11.05, FR-M03-11.06 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã thành công. Bộ dữ liệu trong guard thay bộ chuẩn cho lần chạy đó; mỗi nhánh là snapshot riêng. Điểm nhập lại nêu rõ bước kiểm; nếu dữ liệu còn sai áp lại guard, không tự giới hạn số lần. REJECTED là kết thúc từ chối hợp lệ của US; không bịa nút OK/hủy/thử lại hay rollback lỗi lưu trữ chưa có nguồn.

<!-- sc:exceptions SC-M05-009 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M4 | Không còn Topic | E1.1 | FR-M05-11.03, BR-M05-04 |
| E2 | system | M4 | Có hơn3 Topic | E2.1 | FR-M05-11.03, BR-M05-04 |
| E3 | system | M4 | Có hơn5 Tag | E3.1 | FR-M05-11.03, BR-M05-04 |
| E4 | system | M4 | Topic đã bị xóa hoặc không thuộc danh mục | E4.1 | FR-M05-11.01, FR-M05-01.01, FR-M05-01.09, BR-M05-03 |
| E5 | system | M4 | Tag dài31 ký tự | E5.1 | FR-M05-11.02, FR-M05-03.05, BR-M05-23 |
| E6 | system | M4 | Tag có ký tự sai | E6.1 | FR-M05-11.02, FR-M05-03.06, BR-M05-20 |
| E7 | system | M4 | Tag không có chữ cái | E7.1 | FR-M05-11.02, FR-M05-03.07, BR-M05-20 |
| E8 | user-choice | M3 | Mod chỉ đổi Topic, phần không sửa được giữ | E8.1 | FR-M05-11.01, FR-M05-11.02, BR-M05-04, BR-M05-22, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-02.21, FR-M08-16.02 |
| E9 | user-choice | M3 | Mod chỉ đổi Tag, phần không sửa được giữ | E9.1 | FR-M05-11.01, FR-M05-11.02, BR-M05-04, BR-M05-22, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-02.21, FR-M08-16.02 |
| E10 | user-choice | M3 | Mod bỏ hết Tag, phần không sửa được giữ | E10.1 | FR-M05-11.01, FR-M05-11.02, BR-M05-04, BR-M05-22, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-02.21, FR-M08-16.02 |
| E11 | user-choice | M3 | Mod nhập Tag mới chưa có hoặc trùng sau chuẩn hóa | E11.1 | FR-M05-11.02, FR-M05-03.02, FR-M05-03.03, FR-M05-03.08, BR-M05-24, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-03.14, BR-M05-21, FR-M08-16.02 |
| E12 | user-choice | M3 | Mod nhập tên Tag bị vô hiệu hóa | E12.1 | FR-M05-11.02, FR-M05-03.09, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, BR-M05-26, FR-M08-16.02 |
| E13 | user-choice | M3 | Mod thử bấm yêu cầu gợi ý cho bài người khác rồi chọn thủ công | E13.1 | FR-M05-02.21, FR-M05-11.01, FR-M05-11.02 |
| E14 | system | M2 | Phiên hoặc vai trò điều phối không còn hợp lệ khi yêu cầu | E14.1 | FR-M05-11.04, FR-M01-06.04 |
| E15 | system | M2 | Bài không được phép sửa theo cổng trạng thái M03 | E15.1 | FR-M03-11.07 |
| E16 | system | M4 | Bài không được phép sửa theo cổng trạng thái M03 | E16.1 | FR-M03-11.07 |
| E17 | user-choice | M3 | Mod chỉ đổi Topic, bài vẫn giữ Tag cũ đang vô hiệu hóa | E17.1 | FR-M05-11.01, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-09.03, FR-M05-04.05, BR-M05-04, BR-M05-26, FR-M08-16.02 |
| E18 | system | M1 | ACT-001 — Guest không có quyền điều phối. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E18.1 | FR-M05-11.04 |
| E19 | system | M1 | ACT-002 — User không phải tác giả đối tượng khi đổi bài không có quyền điều phối. Actor khởi tạo ACT-002, END:REJECTED, dùng hậu điều kiện tương ứng mục 4. | E19.1 | FR-M05-11.04 |
| E20 | system | M1 | ACT-007 — Admin thực hiện cùng chức năng với quyền điều phối kế thừa. Actor khởi tạo ACT-007, END:SUCCESS, dùng hậu điều kiện tương ứng mục 4. | E20.1 | FR-M05-11.01, FR-M05-11.02, FR-M05-11.04, FR-M05-02.21, FR-M03-11.04, FR-M03-11.07, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-01.01, FR-M05-01.02, FR-M05-01.03, FR-M05-01.04, FR-M05-01.05, FR-M05-01.07, FR-M05-01.09, FR-M05-01.10, BR-M05-03, BR-M05-04, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.05, FR-M05-03.06, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-20, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-26, FR-M08-16.02, FR-M03-11.05, FR-M03-11.06, FR-M10-14.01, FR-M10-14.02, FR-M10-14.03, FR-M10-14.09 |


<!-- sc:branch SC-M05-009 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối tập thay đổi không hợp lệ, không tự đổi Topic Khác/sửa tên Tag để chốt thay actor; không ghi đây là lần đổi phân loại thành công. | Topic=[]; Tag={bayes} | END:REJECTED | FR-M05-11.03, BR-M05-04 |


<!-- sc:branch SC-M05-009 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối tập thay đổi không hợp lệ, không tự đổi Topic Khác/sửa tên Tag để chốt thay actor; không ghi đây là lần đổi phân loại thành công. | Topic={Toán học, Tin học, Khác, Góc Chill}; Tag={bayes} | END:REJECTED | FR-M05-11.03, BR-M05-04 |


<!-- sc:branch SC-M05-009 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối tập thay đổi không hợp lệ, không tự đổi Topic Khác/sửa tên Tag để chốt thay actor; không ghi đây là lần đổi phân loại thành công. | Topic={Toán học}; Tag={bayes, xácsuất, đạo_hàm, lớp12, covid19, tag_sáu} | END:REJECTED | FR-M05-11.03, BR-M05-04 |


<!-- sc:branch SC-M05-009 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối tập thay đổi không hợp lệ, không tự đổi Topic Khác/sửa tên Tag để chốt thay actor; không ghi đây là lần đổi phân loại thành công. | Topic={Vật lý}; Vật lý không có D-CAT | END:REJECTED | FR-M05-11.01, FR-M05-01.01, FR-M05-01.09, BR-M05-03 |


<!-- sc:branch SC-M05-009 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối tập thay đổi không hợp lệ, không tự đổi Topic Khác/sửa tên Tag để chốt thay actor; không ghi đây là lần đổi phân loại thành công. | Tag gồm "a" lặp31 lần, không tính# | END:REJECTED | FR-M05-11.02, FR-M05-03.05, BR-M05-23 |


<!-- sc:branch SC-M05-009 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối tập thay đổi không hợp lệ, không tự đổi Topic Khác/sửa tên Tag để chốt thay actor; không ghi đây là lần đổi phân loại thành công. | Tag={node.js}; Topic={Toán học} | END:REJECTED | FR-M05-11.02, FR-M05-03.06, BR-M05-20 |


<!-- sc:branch SC-M05-009 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối tập thay đổi không hợp lệ, không tự đổi Topic Khác/sửa tên Tag để chốt thay actor; không ghi đây là lần đổi phân loại thành công. | Tag={2024}; Topic={Toán học} | END:REJECTED | FR-M05-11.02, FR-M05-03.07, BR-M05-20 |


<!-- sc:branch SC-M05-009 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | ACT-003 | Mod Mai chỉ đổi Topic rồi lưu P540. | Topic cuối={Toán học}; Tag cuối={bayes}; lý do trống | E8.2 | FR-M05-11.01, FR-M05-11.02, BR-M05-04, BR-M05-22 |
| E8.2 | SYSTEM | Hệ thống áp UC012 cho phần đổi và giữ các phần hiện có hợp lệ, lưu đúng tập cuối; ghi log kiểm duyệt với lý do trống, trả kết quả, không báo tác giả/lịch sử công khai/AI. | P540.Topic={Toán học}; Tag={bayes}; title/body/tệp giữ nguyên | END:SUCCESS | FR-M05-11.01, FR-M05-11.02, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-02.21, BR-M05-04, BR-M05-22, FR-M08-16.02 |


<!-- sc:branch SC-M05-009 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | ACT-003 | Mod Mai chỉ đổi Tag rồi lưu P540. | Topic cuối={Tin học}; Tag cuối={xácsuất}; lý do trống | E9.2 | FR-M05-11.01, FR-M05-11.02, BR-M05-04, BR-M05-22 |
| E9.2 | SYSTEM | Hệ thống áp UC012 cho phần đổi và giữ các phần hiện có hợp lệ, lưu đúng tập cuối; ghi log kiểm duyệt với lý do trống, trả kết quả, không báo tác giả/lịch sử công khai/AI. | P540.Topic={Tin học}; Tag={xácsuất}; title/body/tệp giữ nguyên | END:SUCCESS | FR-M05-11.01, FR-M05-11.02, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-02.21, BR-M05-04, BR-M05-22, FR-M08-16.02 |


<!-- sc:branch SC-M05-009 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | ACT-003 | Mod Mai bỏ hết Tag rồi lưu P540. | Topic cuối={Tin học}; Tag cuối={}; lý do trống | E10.2 | FR-M05-11.01, FR-M05-11.02, BR-M05-04, BR-M05-22 |
| E10.2 | SYSTEM | Hệ thống áp UC012 cho phần đổi và giữ các phần hiện có hợp lệ, lưu đúng tập cuối; ghi log kiểm duyệt với lý do trống, trả kết quả, không báo tác giả/lịch sử công khai/AI. | P540.Topic={Tin học}; Tag={}; title/body/tệp giữ nguyên | END:SUCCESS | FR-M05-11.01, FR-M05-11.02, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-02.21, BR-M05-04, BR-M05-22, FR-M08-16.02 |


<!-- sc:branch SC-M05-009 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-003 | Mod Mai nhập #Bayes2026 hai lần khác hoa/thường rồi lưu. | Tên mới bayes2026 chưa có; nhập Bayes2026, bayes2026; Topic={Tin học} | E11.2 | FR-M05-11.02, FR-M05-03.02, FR-M05-03.03, FR-M05-03.08, BR-M05-24 |
| E11.2 | SYSTEM | Hệ thống chuẩn hóa, tạo một Tag bayes2026 hoạt động, không cần duyệt và chỉ gắn một liên kết; lưu phân loại, ghi log kiểm duyệt và trả kết quả. Không báo tác giả/lịch sử công khai/AI. | P540.Topic={Tin học}; Tag={bayes2026}; không lưu người tạo của Tag | END:SUCCESS | FR-M05-11.02, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-03.02, FR-M05-03.03, FR-M05-03.08, FR-M05-03.14, BR-M05-21, BR-M05-24, FR-M08-16.02 |


<!-- sc:branch SC-M05-009 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | ACT-003 | Mod Mai nhập #abc cùng #bayes rồi lưu. | abc bị vô hiệu hóa, không phải liên kết đã có của P540; bayes hoạt động | E12.2 | FR-M05-11.02, FR-M05-03.09 |
| E12.2 | SYSTEM | Hệ thống giữ phần nhập abc như văn bản, không liên kết mới hoặc tái tạo Tag abc; lưu bayes hợp lệ, ghi log kiểm duyệt và trả kết quả. Không báo tác giả/lịch sử công khai/AI. | P540.Tag={bayes}; phần chữ=#abc; Topic={Tin học} | END:SUCCESS | FR-M05-11.02, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-03.09, BR-M05-26, FR-M08-16.02 |


<!-- sc:branch SC-M05-009 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | ACT-003 | Mod Mai yêu cầu gợi ý Topic cho P540 của Lan. | Mai không phải tác giả P540 | E13.2 | FR-M05-02.21 |
| E13.2 | SYSTEM | Hệ thống không cung cấp gợi ý AI ở ngữ cảnh này; giữ lựa chọn thủ công trong quyền đổi phân loại. | Không gửi AI; danh mục D-CAT vẫn dùng | E13.3 | FR-M05-02.21, FR-M05-11.01 |
| E13.3 | ACT-003 | Mod Mai chọn Toán học thủ công, giữ Tag bayes rồi lưu. | Topic={Toán học}; Tag={bayes} | M4 | FR-M05-11.01, FR-M05-11.02 |


<!-- sc:branch SC-M05-009 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | SYSTEM | Hệ thống từ chối thao tác cần quyền; không dùng kết quả quyền cũ để tiếp tục. | Snapshot: mất vai trò điều phối hoặc phiên làm mới đã hết30 ngày | END:REJECTED | FR-M05-11.04, FR-M01-06.04 |


<!-- sc:branch SC-M05-009 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | SYSTEM | Hệ thống từ chối đổi phân loại, không dùng vai trò điều phối để vượt cổng trạng thái sửa bài. | P540 Chờ duyệt/Đã xóa/Bị Mod ẩn; các điều kiện quyền khác có thể đạt | END:REJECTED | FR-M03-11.07 |


<!-- sc:branch SC-M05-009 E16 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E16.1 | SYSTEM | Hệ thống từ chối đổi phân loại, không dùng vai trò điều phối để vượt cổng trạng thái sửa bài. | P540 Chờ duyệt/Đã xóa/Bị Mod ẩn; các điều kiện quyền khác có thể đạt | END:REJECTED | FR-M03-11.07 |


<!-- sc:branch SC-M05-009 E17 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E17.1 | ACT-003 | Mod Mai đổi Topic P540 sang Toán học rồi lưu, không sửa tập Tag. | Snapshot: Topic trước={Tin học}; Tag liên kết={bayes, abc}; abc vô hiệu; phần Tag giữ nguyên | E17.2 | FR-M05-11.01 |
| E17.2 | SYSTEM | Hệ thống kiểm và lưu Topic Toán học, giữ toàn bộ liên kết Tag cũ kể cả abc vô hiệu, chỉ hiện#bayes. Ghi log kiểm duyệt, không thông báo/lịch sử sửa/AI; không dùng việc Tag bị ẩn làm thao tác bỏ liên kết. | P540.Topic={Toán học}; Tag liên kết={bayes, abc}; Tag hiển thị={#bayes} | END:SUCCESS | FR-M05-11.01, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-09.03, FR-M05-04.05, BR-M05-04, BR-M05-26, FR-M08-16.02 |


**E18 — thay toàn bộ M1 đến kết thúc:** Guest không có quyền điều phối. Actor khởi tạo ACT-001, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-009 E18 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E18.1 | ACT-001 | Guest yêu cầu đổi topic và tag trên bài viết của người khác. | Không có vai trò Mod/Admin; P540 của Lan nếu là đổi phân loại | E18.2 | FR-M05-11.04 |
| E18.2 | SYSTEM | Hệ thống từ chối, không thay trạng thái Tag hay phân loại bài từ yêu cầu không quyền. | Không ghi kết quả điều phối thành công | END:REJECTED | FR-M05-11.04 |


**E19 — thay toàn bộ M1 đến kết thúc:** User không phải tác giả đối tượng khi đổi bài không có quyền điều phối. Actor khởi tạo ACT-002, END:REJECTED, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-009 E19 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E19.1 | ACT-002 | User không phải tác giả đối tượng khi đổi bài yêu cầu đổi topic và tag trên bài viết của người khác. | Không có vai trò Mod/Admin; P540 của Lan nếu là đổi phân loại | E19.2 | FR-M05-11.04 |
| E19.2 | SYSTEM | Hệ thống từ chối, không thay trạng thái Tag hay phân loại bài từ yêu cầu không quyền. | Không ghi kết quả điều phối thành công | END:REJECTED | FR-M05-11.04 |


**E20 — thay toàn bộ M1 đến kết thúc:** Admin thực hiện cùng chức năng với quyền điều phối kế thừa. Actor khởi tạo ACT-007, END:SUCCESS, dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M05-009 E20 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E20.1 | ACT-007 | Admin An yêu cầu đổi phân loại P540 của Lan. | P540.Topic={Tin học}; Tag={bayes}; An khác tác giả | E20.2 | FR-M05-11.01, FR-M05-11.02 |
| E20.2 | SYSTEM | Hệ thống kiểm quyền điều phối và trạng thái bài, trả phân loại/danh mục hiện tại; không cung cấp AI gợi ý trên bài người khác, không mở quyền sửa nội dung bài. | Topic={Tin học}; Tag={bayes}; danh mục D-CAT, D-TAG | E20.3 | FR-M05-11.04, FR-M05-02.21, FR-M03-11.04, FR-M03-11.07 |
| E20.3 | ACT-007 | Admin An bỏ Tin học, chọn Toán học, thay #bayes bằng #XácSuất và lưu. | Topic cuối={Toán học}; Tag cuối={XácSuất}; lý do tùy chọn=Điều chỉnh phân loại | E20.4 | FR-M05-11.01, FR-M05-11.02 |
| E20.4 | SYSTEM | Hệ thống kiểm Topic 1–3 thuộc danh mục, Tag 0–5 đúng tên/chuẩn hóa/trạng thái, dùng lại hoặc tạo Tag theo tập vừa gửi; lưu và trả đúng phân loại cuối. Ghi log kiểm duyệt, không gửi thông báo cho tác giả, không ghi lần đổi này vào lịch sử sửa công khai; không dùng AI. Đồng thời ghi thêm một mục nhật ký thao tác Admin riêng, không thay thế nhật ký kiểm duyệt. | Đường chuẩn P540.Topic={Toán học}; Tag={xácsuất}; khi nhập lại từ nhánh dùng chính tập Topic/Tag/lý do của bước gửi gần nhất. Log An/đổi phân loại/P540/lý do nếu có/10:25+07; title/body/tệp giữ nguyên | END:SUCCESS | FR-M05-11.01, FR-M05-11.02, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-02.21, FR-M05-01.01, FR-M05-01.02, FR-M05-01.03, FR-M05-01.04, FR-M05-01.05, FR-M05-01.07, FR-M05-01.09, FR-M05-01.10, BR-M05-03, BR-M05-04, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.05, FR-M05-03.06, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-20, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-26, FR-M08-16.02, FR-M03-11.05, FR-M03-11.06, FR-M10-14.01, FR-M10-14.02, FR-M10-14.03, FR-M10-14.09 |


<!-- sc:end SC-M05-009 -->

## 5. Quy tắc nền và giao tiếp — không phải scenario

| ID | Trigger/điều kiện | Hiệu ứng và giới hạn | sources |
|---|---|---|---|
| AUT-M05-001 | Đến kỳ tính lại trong chu kỳ15–30 phút; dùng thời điểm T của lần tính | Tính trên tương tác trong7×24 giờ ngược từ T, bất kể tuổi bài, chỉ bài đang hiện feed chính: Đã đăng, không ẩn bởi kiểm duyệt/tài khoản/nhóm, nhóm Public có tính, Private và bài gỡ khỏi nhóm không tính. Bài đăng trong cửa sổ +1, mỗi upvote bài +2, comment kể cả reply +1, bookmark +1. Tương tác rút trước tính, upvote comment, view không tính; upvote người DELETED còn giữ vẫn tính, bookmark đã xóa không tính. Một bài nhiều Topic/Tag góp đủ điểm cho từng mục, không chia; Tag vô hiệu không tính. Chỉ xuất điểm>0; điểm giảm, rồi số bài mới giảm, rồi tênA–Z; mỗi mục một hạng. Đưa tương tác đủ điều kiện vào điểm chậm nhất30 phút; giữa kỳ cung cấp kết quả lần gần nhất cho M14, không tự chọn cron/tính lại khi mở danh mục. | FR-M05-05.01, FR-M05-05.02, FR-M05-05.03, FR-M05-05.04, FR-M05-05.05, FR-M05-05.06, FR-M05-05.07, FR-M05-05.08, FR-M05-05.09, FR-M05-05.10, FR-M05-05.11, FR-M05-05.12, FR-M05-05.13, FR-M05-05.14, BR-M05-29, BR-M05-30, BR-M05-31, FR-M01-12.08, FR-M01-12.09, FR-M14-02.06 |
| AUT-M05-002 | Gửi bài/lưu sửa có gợi ý gần nhất chưa cũ; hoặc tài khoản tác giả chuyển DELETED | Ghi suggested/final kể cả tập giữ lại bằng0 nếu tác giả chọn Topic khác hợp lệ; không ghi khi không dùng gợi ý, gợi ý gần nhất cũ hoặc chỉ lưu nháp. Khi DELETED, giữ phản hồi không danh tính; phân biệt với log lời gọi AI vẫn liên kết username theo M13. Không tự đặt thời hạn lưu lượt gợi ý, không gửi phản hồi để train lại mô hình. | FR-M05-02.12, FR-M05-02.13, FR-M05-02.14, FR-M05-02.22, BR-M05-16, FR-M01-12.11, FR-M13-08.08, FR-M13-10.07 |
| AUT-M05-003 | Mod/Admin hoàn tất vô hiệu/kích hoạt Tag hoặc đổi phân loại bài người khác | Ghi người thực hiện, thao tác, đối tượng Tag/bài, lý do nếu có, thời điểm vào log kiểm duyệt M08. Admin có thêm log Admin M10 riêng; không ghi thao tác tác giả thường vào log Admin. Không thông báo tác giả và không ghi lịch sử sửa công khai khi Mod/Admin đổi phân loại bài người khác. Nguồn chỉ chốt giữ trạng thái với yêu cầu bật/tắt lặp, chưa chốt phát sinh log cho lần không đổi trạng thái; không tự thêm audit lần thử bị từ chối/rollback. | FR-M05-09.05, FR-M05-09.07, FR-M05-10.05, FR-M05-10.06, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M08-16.02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.03, FR-M10-14.08, FR-M10-14.09 |
| AUT-M05-004 | Tiêu đề hoặc nội dung chữ thay đổi sau gợi ý | Đánh dấu gợi ý lỗi thời, cảnh báo nhẹ kèm nút gợi ý lại; không tự gọi lại, không bắt gợi ý lại, không ngăn gửi tập cuối hợp lệ. Gợi ý lại chỉ sau tác giả bấm và vẫn kiểm hai cờ/độ dài/hạn mức. Thay tệp không được đồng nhất với đổi chữ/tiêu đề. Phản hồi xét lượt gần nhất ở thời điểm gửi/lưu sửa. | FR-M05-02.09, FR-M05-02.10, FR-M05-02.11, FR-M05-02.13, BR-M05-15, BR-M05-16 |
| RULE-M05-001 | Danh mục và danh tính dữ liệu phân loại | Danh mục phẳng, ban đầu11 Topic D-CAT, không Topic con/đổi tên; tổng số không giới hạn. Topic so trùng không phân biệt hoa/thường và khoảng trắng thừa đầu/cuối/giữa, giữ dấu. Tag chỉ đổi hoa→thường, giữ dấu, không lưu người tạo; chữ/số/_ và có chữ, ≤30 ký tự không tính#, tối đa 5, không bắt buộc. Không Topic/Tag riêng cho comment; không AI Tag. | FR-M05-04.06, FR-M05-06.06, FR-M05-06.07, FR-M05-06.08, FR-M05-03.05, FR-M05-03.06, FR-M05-03.07, FR-M05-03.11, FR-M05-03.13, FR-M05-03.14, BR-M05-01, BR-M05-02, BR-M05-05, BR-M05-06, BR-M05-20, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-28 |
| RULE-M05-002 | Tag vô hiệu hóa, kích hoạt lại và phần chữ | Vô hiệu không xóa Tag/liên kết cũ; không hiện gợi ý, tìm Tag, danh sách, Trending hoặc nhãn bài. Nhập lại thành văn bản, không tái tạo Tag hoạt động. Kích hoạt lại cho hiển thị các liên kết còn giữ, không tự đổi phần chữ nhập lúc vô hiệu thành Tag; Trending vẫn kỳ gần nhất/điểm>0. Mod/Admin không sửa tên/gộp/xóa Tag trong điều kiện thường. | FR-M05-03.09, FR-M05-04.03, FR-M05-04.05, FR-M05-05.07, FR-M05-05.10, FR-M05-05.14, FR-M05-09.02, FR-M05-09.03, FR-M05-09.06, FR-M05-10.02, FR-M05-10.03, BR-M05-25, BR-M05-26, BR-M05-27, FR-M06-01.04, FR-M06-03.04 |
| RULE-M05-003 | Quyền và ranh giới với M01/M03/M06/M07/M10/M14 | Chỉ Admin thêm/gộp/xóa Topic; Mod/Admin điều phối Tag/phân loại người khác, User chỉ bài mình. M03/M01 giữ quyền/trạng thái nội dung; không tự có quyền sửa title/body/tệp khi đổi phân loại. Gộp chuyển mọi bài và follow không trùng, xóa độc lập chỉ không có bài ngoài nháp; liên kết bài đi theo bài khi xóa hẳn, không tự dọn để đủ điều kiện xóa Topic. M06 sở hữu trang bài theo lọc/truy vấn rỗng, M14 sở hữu hiển thị Trending; không thêm trang liệt kê M05 hay thao tác theo dõi mới. M07 không thông báo khi Topic có bài mới; việc chuyển/bỏ follow không thêm thông báo đó. | FR-M05-06.03, FR-M05-07.01, FR-M05-07.02, FR-M05-07.03, FR-M05-07.05, FR-M05-07.06, FR-M05-08.01, FR-M05-08.02, FR-M05-08.03, FR-M05-08.05, FR-M05-08.06, FR-M05-09.04, FR-M05-10.04, FR-M05-11.04, BR-M05-08, BR-M05-09, FR-M03-17.02, FR-M03-11.04, FR-M07-02.24 |
| RULE-M05-004 | Lời gọi gợi ý từ tác giả và quyền quyết định cuối | Chỉ bấm nút mới gọi; dùng title+plaintext, không tệp. ≥20 từ theo cụm cách khoảng trắng (âm tiết Việt tính riêng); tối đa 10 yêu cầu/60 giây trượt/người, không giới hạn tần suất AI riêng mới. Hai cờ phải bật; tắt có chủ đích chọn thủ công. Lỗi lần đầu đợi2 giây thử lại một lần, 10 giây/lần, không song song; thất bại không tự tắt cờ và không tự chọn Topic. Loại phần ngoài danh mục, tất cả sai mới thất bại. Tác giả luôn chốt tập cuối1–3 khi gửi/lưu sửa, 0–3 nháp; không Mod duyệt gợi ý; Mod/Admin không được gợi ý trên bài người khác. Privacy/ToS M01 nêu việc gửi bài đang soạn tới nhà cung cấpAI; không thêm một hộp xin đồng ý riêng cho mỗi lần gợi ý. | FR-M05-02.01, FR-M05-02.02, FR-M05-02.03, FR-M05-02.04, FR-M05-02.05, FR-M05-02.06, FR-M05-02.07, FR-M05-02.08, FR-M05-02.09, FR-M05-02.10, FR-M05-02.11, FR-M05-02.12, FR-M05-02.13, FR-M05-02.14, FR-M05-02.15, FR-M05-02.16, FR-M05-02.17, FR-M05-02.18, FR-M05-02.19, FR-M05-02.20, FR-M05-02.21, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-13, BR-M05-14, BR-M05-17, BR-M05-18, BR-M05-19, FR-M13-01.04, FR-M13-01.05, FR-M13-01.08, FR-M13-05.01, FR-M13-05.02, FR-M01-15.04 |


### Minh họa đối soát Trending

Dữ liệu giả lập tại T=09/11/2026 10:00+07, cửa sổ7×24 giờ từ 02/11/2026 10:00. Bài A thuộc Toán học/Tin học và Tag bayes hoạt động, đăng05/11, có 3 upvote bài, 2 comment (1 gốc+1 reply), 1 bookmark trong cửa sổ:1+3×2+2+1=10. Bài B đăng20/10, có 2 upvote trong cửa sổ và1 upvote01/11 ngoài cửa sổ:4 điểm. Bài C đăng02/11 09:00 ngoài cửa sổ, có 1 comment03/11:1 điểm. Bài D Private có 20 upvote không tính. Toán học nhận15, Tin học nhận10 từ A; không chia10 theo2 Topic. Nếu bookmark ở A bị xóa trước tính (kể cả do tài khoản DELETED), A còn 9; upvote DELETED còn giữ vẫn góp2. View/upvote comment/rút tương tác không tạo điểm.

Ví dụ xếp hạng snapshot riêng: Ngữ văn12 (0 bài mới), Tin học10 (2), Hướng nghiệp10 (1), Toán học10 (1), Góc Chill0 → Ngữ văn, Tin học, Hướng nghiệp, Toán học; loại Góc Chill. Chu kỳ minh họa chỉ là ví dụ: tương tác10:05 phải có trong điểm không muộn10:35, không tự quyết định giờ cron. Các phép tính này kiểm quy tắc nền, không là scenario SYSTEM và không triển khai giao diện M14.

## 6. Truy vết và ma trận quyết định

| Mã FR/BR | SC/bước/nhánh hoặc quy tắc nền | Mức đối soát |
|---|---|---|
| FR-M05-01 | SC-M05-001/M1; SC-M05-001/M2; SC-M05-001/E4.2; SC-M05-001/E14.5; SC-M05-009/M4; SC-M05-009/E4.1; SC-M05-009/E20.4; SC-M05-001/M3; SC-M05-001/M4; SC-M05-001/E1.3; SC-M05-001/E1.4; SC-M05-001/E2.3; SC-M05-001/E2.4; SC-M05-001/E10.5; SC-M05-001/E10.6; SC-M05-001/E11.6; SC-M05-001/E12.6; SC-M05-001/E13.5; SC-M05-001/E13.6; SC-M05-001/E15.3; SC-M05-001/E16.3; SC-M05-001/E17.3; SC-M05-001/E18.3; SC-M05-001/E19.7; SC-M05-001/E19.8; SC-M05-001/E20.3; SC-M05-001/E21.5; SC-M05-001/E21.6; SC-M05-001/E22.5; SC-M05-001/E22.6; SC-M05-001/E23.3; SC-M05-001/E24.7; SC-M05-001/E24.8; SC-M05-001/E25.7; SC-M05-001/E25.8; SC-M05-001/E26.11; SC-M05-001/E26.12; SC-M05-001/E27.6; SC-M05-001/E28.7; SC-M05-001/E28.8; SC-M05-001/E37.9; SC-M05-001/E37.10; SC-M05-002/M4; SC-M05-002/E1.2; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-001/E1.1; SC-M05-001/E1.2; SC-M05-001/E35.5; SC-M05-001/E35.6; SC-M05-001/E36.5; SC-M05-001/E36.6; SC-M05-001/E2.1; SC-M05-001/E2.2; SC-M05-001/E3.1; SC-M05-002/E10.1; SC-M05-001/E4.1; SC-M05-001/E5.1; SC-M05-001/E5.2; SC-M05-001/E6.1; SC-M05-001/E6.2; SC-M05-001/E29.5; SC-M05-001/E29.6; SC-M05-001/E7.1; SC-M05-001/E7.2; SC-M05-001/E7.3; SC-M05-001/E7.4; SC-M05-001/E8.1; SC-M05-001/E8.2; SC-M05-001/E9.1; SC-M05-001/E9.2; SC-M05-001/E28.1; SC-M05-001/E28.2; SC-M05-001/E33.3; SC-M05-002/E14.3; SC-M05-001/E8.3; SC-M05-001/E8.4; SC-M05-001/E9.3; SC-M05-001/E9.4; SC-M05-001/E38.1; SC-M05-001/E38.2 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02 | SC-M05-001/M2; SC-M05-001/E10.2; SC-M05-001/E11.2; SC-M05-001/E12.2; SC-M05-001/E13.2; SC-M05-001/E14.2; SC-M05-001/E19.4; SC-M05-001/E21.2; SC-M05-001/E22.2; SC-M05-001/E23.2; SC-M05-001/E24.2; SC-M05-001/E25.2; SC-M05-001/E26.2; SC-M05-001/E26.8; SC-M05-001/E27.2; SC-M05-001/E28.4; SC-M05-001/E29.2; SC-M05-001/E35.2; SC-M05-001/E36.2; SC-M05-001/E37.2; RULE-M05-004; SC-M05-001/M4; SC-M05-001/E1.4; SC-M05-001/E2.4; SC-M05-001/E7.4; SC-M05-001/E14.5; SC-M05-001/E23.3; SC-M05-002/E9.4; AUT-M05-002; SC-M05-001/E10.6; SC-M05-001/E11.5; SC-M05-001/E11.6; SC-M05-001/E12.6; SC-M05-001/E13.6; SC-M05-001/E19.8; SC-M05-001/E21.6; SC-M05-001/E22.6; SC-M05-001/E26.12; SC-M05-001/E27.6; SC-M05-001/E28.8; SC-M05-001/E29.6; SC-M05-001/E35.6; SC-M05-001/E36.6; SC-M05-001/E24.8; SC-M05-001/E25.8; SC-M05-001/E37.10; AUT-M05-004; SC-M05-001/E10.1; SC-M05-001/E11.1; SC-M05-001/E12.1; SC-M05-001/E13.1; SC-M05-001/E14.1; SC-M05-001/E15.1; SC-M05-001/E16.1; SC-M05-001/E17.1; SC-M05-001/E18.1; SC-M05-001/E19.1; SC-M05-001/E19.3; SC-M05-001/E22.1; SC-M05-001/E23.1; SC-M05-001/E24.1; SC-M05-001/E25.1; SC-M05-001/E26.1; SC-M05-001/E26.7; SC-M05-001/E27.1; SC-M05-001/E27.5; SC-M05-001/E28.3; SC-M05-001/E29.1; SC-M05-001/E35.1; SC-M05-001/E36.1; SC-M05-001/E37.1; SC-M05-001/E18.2; SC-M05-001/E18.3; SC-M05-001/E19.2; SC-M05-001/E20.1; SC-M05-001/E20.2; SC-M05-001/E21.1; SC-M05-001/E15.2; SC-M05-001/E16.2; SC-M05-001/E17.2; SC-M05-001/E37.7; SC-M05-001/E37.8; SC-M05-001/E10.4; SC-M05-001/E11.4; SC-M05-001/E12.4; SC-M05-001/E13.4; SC-M05-001/E19.6; SC-M05-001/E21.4; SC-M05-001/E22.4; SC-M05-001/E24.4; SC-M05-001/E25.4; SC-M05-001/E26.4; SC-M05-001/E26.10; SC-M05-001/E27.4; SC-M05-001/E28.6; SC-M05-001/E29.4; SC-M05-001/E35.4; SC-M05-001/E36.4; SC-M05-001/E37.4; SC-M05-001/E10.5; SC-M05-001/E12.5; SC-M05-001/E13.5; SC-M05-001/E19.7; SC-M05-001/E21.5; SC-M05-001/E22.5; SC-M05-001/E24.7; SC-M05-001/E25.7; SC-M05-001/E26.11; SC-M05-001/E28.7; SC-M05-001/E35.5; SC-M05-001/E36.5; SC-M05-001/E14.4; SC-M05-001/E15.3; SC-M05-001/E16.3; SC-M05-001/E17.3; SC-M05-001/E37.9; SC-M05-001/E24.5; SC-M05-001/E24.6; SC-M05-001/E25.5; SC-M05-001/E25.6; SC-M05-001/E26.5; SC-M05-001/E37.5; SC-M05-001/E37.6; SC-M05-001/E26.6; SC-M05-001/E28.1; SC-M05-001/E28.2; SC-M05-001/E39.1; SC-M05-001/E39.2; SC-M05-009/M2; SC-M05-009/M4; SC-M05-009/E8.2; SC-M05-009/E9.2; SC-M05-009/E10.2; SC-M05-009/E13.1; SC-M05-009/E13.2; SC-M05-009/E20.2; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03 | SC-M05-001/M2; SC-M05-001/M4; SC-M05-001/E1.4; SC-M05-001/E2.4; SC-M05-001/E7.4; SC-M05-001/E10.6; SC-M05-001/E13.6; SC-M05-001/E19.8; SC-M05-001/E21.6; SC-M05-001/E22.6; SC-M05-001/E26.12; SC-M05-001/E28.8; SC-M05-002/M1; SC-M05-002/M2; SC-M05-002/M3; SC-M05-002/M4; SC-M05-002/E1.1; SC-M05-002/E1.2; SC-M05-002/E2.3; SC-M05-002/E2.4; SC-M05-002/E3.3; SC-M05-002/E3.4; SC-M05-002/E4.3; SC-M05-002/E4.4; SC-M05-002/E5.3; SC-M05-002/E5.4; SC-M05-002/E6.2; SC-M05-002/E7.1; SC-M05-002/E7.2; SC-M05-002/E8.2; SC-M05-002/E9.4; SC-M05-002/E10.1; SC-M05-002/E16.4; SC-M05-009/M4; SC-M05-009/E20.4; SC-M05-001/E10.4; SC-M05-001/E11.4; SC-M05-001/E12.4; SC-M05-001/E13.4; SC-M05-001/E19.6; SC-M05-001/E21.4; SC-M05-001/E22.4; SC-M05-001/E24.4; SC-M05-001/E25.4; SC-M05-001/E26.4; SC-M05-001/E26.10; SC-M05-001/E27.4; SC-M05-001/E28.6; SC-M05-001/E29.4; SC-M05-001/E35.4; SC-M05-001/E36.4; SC-M05-001/E37.4; SC-M05-002/E9.2; RULE-M05-001; SC-M05-001/E33.3; SC-M05-002/E9.1; SC-M05-002/E9.3; SC-M05-002/E14.3; SC-M05-002/E16.1; SC-M05-002/E16.2; SC-M05-002/E16.3; SC-M05-009/E11.1; SC-M05-009/E11.2; SC-M05-002/E6.1; SC-M05-002/E2.1; SC-M05-002/E2.2; SC-M05-002/E3.1; SC-M05-002/E3.2; SC-M05-009/E5.1; SC-M05-002/E4.1; SC-M05-002/E4.2; SC-M05-009/E6.1; SC-M05-002/E5.1; SC-M05-002/E5.2; SC-M05-009/E7.1; SC-M05-002/E8.1; SC-M05-007/M2; SC-M05-007/E6.2; SC-M05-009/E12.1; SC-M05-009/E12.2; RULE-M05-002; SC-M05-003/E1.2; SC-M05-003/E2.2; SC-M05-002/E17.1; SC-M05-002/E17.2 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-04 | SC-M05-002/E16.2; SC-M05-002/E16.4; SC-M05-003/E2.2; SC-M05-007/M2; SC-M05-007/E6.2; SC-M05-009/E17.2; RULE-M05-002; SC-M05-003/M1; SC-M05-003/M2; SC-M05-003/E5.1; SC-M05-003/E5.2; RULE-M05-001; SC-M05-003/E1.1; SC-M05-003/E1.2; SC-M05-003/E4.1; SC-M05-003/E4.2; SC-M05-003/E2.1; SC-M05-003/E3.1; SC-M05-003/E3.2 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05 | SC-M05-003/M2; SC-M05-008/M2; SC-M05-008/E2.1; SC-M05-008/E7.2; AUT-M05-001; RULE-M05-002; SC-M05-007/M2; SC-M05-007/E6.2 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-06 | SC-M05-004/M1; SC-M05-004/M2; SC-M05-004/E2.1; SC-M05-004/E2.2; SC-M05-004/E3.1; SC-M05-004/E4.1; SC-M05-004/E4.2; SC-M05-004/E5.1; SC-M05-004/E5.2; SC-M05-004/E6.1; SC-M05-004/E6.2; RULE-M05-003; RULE-M05-001; SC-M05-004/E1.1 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-07 | SC-M05-005/M1; SC-M05-005/M2; SC-M05-005/E2.1; SC-M05-005/E2.2; RULE-M05-003; SC-M05-005/E3.1; SC-M05-005/E3.2; SC-M05-005/E4.1; SC-M05-005/E4.2; SC-M05-005/E5.1; SC-M05-005/E5.2; SC-M05-005/E1.1 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-08 | SC-M05-006/M1; SC-M05-006/M2; SC-M05-006/E7.1; RULE-M05-003; SC-M05-006/E8.1; SC-M05-006/E8.2; SC-M05-006/E9.1; SC-M05-006/E9.2; SC-M05-006/E10.1; SC-M05-006/E10.2; SC-M05-006/E1.1; SC-M05-006/E2.1; SC-M05-006/E3.1; SC-M05-006/E4.1; SC-M05-006/E5.1; SC-M05-006/E6.1 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-09 | SC-M05-002/E16.2; SC-M05-002/E16.4; SC-M05-007/M2; SC-M05-007/E2.2; SC-M05-007/E6.2; SC-M05-009/E17.2; RULE-M05-002; SC-M05-007/M1; SC-M05-007/E2.1; SC-M05-007/E6.1; AUT-M05-003; SC-M05-007/E1.1; SC-M05-007/E3.1; SC-M05-007/E4.1; SC-M05-007/E4.2; SC-M05-007/E5.1; SC-M05-007/E5.2; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-10 | SC-M05-008/M1; SC-M05-008/M2; SC-M05-008/E2.1; SC-M05-008/E3.1; SC-M05-008/E3.2; SC-M05-008/E7.1; SC-M05-008/E7.2; RULE-M05-002; SC-M05-008/E1.1; AUT-M05-003; SC-M05-008/E4.1; SC-M05-008/E5.1; SC-M05-008/E5.2; SC-M05-008/E6.1; SC-M05-008/E6.2; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-11 | SC-M05-001/E30.1; SC-M05-001/E31.1; SC-M05-002/E11.1; SC-M05-002/E12.1; SC-M05-009/M2; SC-M05-009/E14.1; SC-M05-009/E18.1; SC-M05-009/E18.2; SC-M05-009/E19.1; SC-M05-009/E19.2; SC-M05-009/E20.2; RULE-M05-003; SC-M05-009/M1; SC-M05-009/M3; SC-M05-009/M4; SC-M05-009/E4.1; SC-M05-009/E8.1; SC-M05-009/E8.2; SC-M05-009/E9.1; SC-M05-009/E9.2; SC-M05-009/E10.1; SC-M05-009/E10.2; SC-M05-009/E13.2; SC-M05-009/E13.3; SC-M05-009/E17.1; SC-M05-009/E17.2; SC-M05-009/E20.1; SC-M05-009/E20.3; SC-M05-009/E20.4; SC-M05-009/E5.1; SC-M05-009/E6.1; SC-M05-009/E7.1; SC-M05-009/E11.1; SC-M05-009/E11.2; SC-M05-009/E12.1; SC-M05-009/E12.2; AUT-M05-003; SC-M05-009/E1.1; SC-M05-009/E2.1; SC-M05-009/E3.1 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-01.01 | SC-M05-001/M1; SC-M05-001/M2; SC-M05-001/E4.2; SC-M05-001/E14.5; SC-M05-009/M4; SC-M05-009/E4.1; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-01.02 | SC-M05-001/M3; SC-M05-001/M4; SC-M05-001/E1.3; SC-M05-001/E1.4; SC-M05-001/E2.3; SC-M05-001/E2.4; SC-M05-001/E4.2; SC-M05-001/E10.5; SC-M05-001/E10.6; SC-M05-001/E11.6; SC-M05-001/E12.6; SC-M05-001/E13.5; SC-M05-001/E13.6; SC-M05-001/E14.5; SC-M05-001/E15.3; SC-M05-001/E16.3; SC-M05-001/E17.3; SC-M05-001/E18.3; SC-M05-001/E19.7; SC-M05-001/E19.8; SC-M05-001/E20.3; SC-M05-001/E21.5; SC-M05-001/E21.6; SC-M05-001/E22.5; SC-M05-001/E22.6; SC-M05-001/E23.3; SC-M05-001/E24.7; SC-M05-001/E24.8; SC-M05-001/E25.7; SC-M05-001/E25.8; SC-M05-001/E26.11; SC-M05-001/E26.12; SC-M05-001/E27.6; SC-M05-001/E28.7; SC-M05-001/E28.8; SC-M05-001/E37.9; SC-M05-001/E37.10; SC-M05-002/M4; SC-M05-002/E1.2; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-009/M4; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-01.03 | SC-M05-001/E3.1; SC-M05-001/E35.5; SC-M05-001/E35.6; SC-M05-001/E36.5; SC-M05-001/E36.6; SC-M05-002/E10.1; SC-M05-009/M4; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-01.04 | SC-M05-001/E1.1; SC-M05-001/E1.2; SC-M05-001/E1.3; SC-M05-001/E1.4; SC-M05-001/E35.5; SC-M05-001/E35.6; SC-M05-001/E36.5; SC-M05-001/E36.6; SC-M05-009/M4; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-01.05 | SC-M05-001/E2.1; SC-M05-001/E2.2; SC-M05-001/E2.3; SC-M05-001/E2.4; SC-M05-009/M4; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-01.06 | SC-M05-001/E7.1; SC-M05-001/E7.2; SC-M05-001/E7.3; SC-M05-001/E7.4; SC-M05-001/E8.1; SC-M05-001/E8.2; SC-M05-001/E9.1; SC-M05-001/E9.2; SC-M05-001/E10.5; SC-M05-001/E10.6; SC-M05-001/E13.5; SC-M05-001/E13.6; SC-M05-001/E19.7; SC-M05-001/E19.8; SC-M05-001/E21.5; SC-M05-001/E21.6; SC-M05-001/E22.5; SC-M05-001/E22.6; SC-M05-001/E26.11; SC-M05-001/E26.12; SC-M05-001/E28.1; SC-M05-001/E28.2; SC-M05-001/E28.7; SC-M05-001/E28.8; SC-M05-001/E33.3; SC-M05-002/E14.3 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-01.07 | SC-M05-001/E7.4; SC-M05-001/E8.3; SC-M05-001/E8.4; SC-M05-001/E9.3; SC-M05-001/E9.4; SC-M05-009/M4; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-01.08 | SC-M05-001/E38.1; SC-M05-001/E38.2 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-01.09 | SC-M05-001/E4.1; SC-M05-002/E10.1; SC-M05-009/M4; SC-M05-009/E4.1; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-01.10 | SC-M05-001/E5.1; SC-M05-001/E5.2; SC-M05-001/E6.1; SC-M05-001/E6.2; SC-M05-001/E29.5; SC-M05-001/E29.6; SC-M05-009/M4; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.01 | SC-M05-001/E10.1; SC-M05-001/E10.2; SC-M05-001/E11.1; SC-M05-001/E11.2; SC-M05-001/E12.1; SC-M05-001/E12.2; SC-M05-001/E13.1; SC-M05-001/E13.2; SC-M05-001/E14.1; SC-M05-001/E14.2; SC-M05-001/E15.1; SC-M05-001/E16.1; SC-M05-001/E17.1; SC-M05-001/E18.1; SC-M05-001/E19.1; SC-M05-001/E19.3; SC-M05-001/E19.4; SC-M05-001/E21.2; SC-M05-001/E22.1; SC-M05-001/E22.2; SC-M05-001/E23.1; SC-M05-001/E23.2; SC-M05-001/E24.1; SC-M05-001/E24.2; SC-M05-001/E25.1; SC-M05-001/E25.2; SC-M05-001/E26.1; SC-M05-001/E26.2; SC-M05-001/E26.7; SC-M05-001/E26.8; SC-M05-001/E27.1; SC-M05-001/E27.2; SC-M05-001/E27.5; SC-M05-001/E28.3; SC-M05-001/E28.4; SC-M05-001/E29.1; SC-M05-001/E29.2; SC-M05-001/E35.1; SC-M05-001/E35.2; SC-M05-001/E36.1; SC-M05-001/E36.2; SC-M05-001/E37.1; SC-M05-001/E37.2; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.02 | SC-M05-001/M2; SC-M05-001/E10.2; SC-M05-001/E11.2; SC-M05-001/E12.2; SC-M05-001/E13.2; SC-M05-001/E14.2; SC-M05-001/E19.4; SC-M05-001/E21.2; SC-M05-001/E22.2; SC-M05-001/E23.2; SC-M05-001/E24.2; SC-M05-001/E25.2; SC-M05-001/E26.2; SC-M05-001/E26.8; SC-M05-001/E27.2; SC-M05-001/E28.4; SC-M05-001/E29.2; SC-M05-001/E35.2; SC-M05-001/E36.2; SC-M05-001/E37.2; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.03 | SC-M05-001/E10.4; SC-M05-001/E11.4; SC-M05-001/E12.4; SC-M05-001/E13.4; SC-M05-001/E19.6; SC-M05-001/E21.4; SC-M05-001/E22.4; SC-M05-001/E24.4; SC-M05-001/E25.4; SC-M05-001/E26.4; SC-M05-001/E26.10; SC-M05-001/E27.4; SC-M05-001/E28.6; SC-M05-001/E29.4; SC-M05-001/E35.4; SC-M05-001/E36.4; SC-M05-001/E37.4; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.04 | SC-M05-001/E10.5; SC-M05-001/E10.6; SC-M05-001/E11.5; SC-M05-001/E12.5; SC-M05-001/E13.5; SC-M05-001/E13.6; SC-M05-001/E19.7; SC-M05-001/E19.8; SC-M05-001/E21.5; SC-M05-001/E21.6; SC-M05-001/E22.5; SC-M05-001/E22.6; SC-M05-001/E24.7; SC-M05-001/E25.7; SC-M05-001/E26.11; SC-M05-001/E26.12; SC-M05-001/E28.7; SC-M05-001/E28.8; SC-M05-001/E35.5; SC-M05-001/E35.6; SC-M05-001/E36.5; SC-M05-001/E36.6; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.05 | SC-M05-001/E10.2; SC-M05-001/E11.2; SC-M05-001/E12.2; SC-M05-001/E13.2; SC-M05-001/E14.2; SC-M05-001/E18.1; SC-M05-001/E18.2; SC-M05-001/E18.3; SC-M05-001/E19.1; SC-M05-001/E19.2; SC-M05-001/E19.3; SC-M05-001/E19.4; SC-M05-001/E21.2; SC-M05-001/E22.2; SC-M05-001/E23.2; SC-M05-001/E24.2; SC-M05-001/E25.2; SC-M05-001/E26.2; SC-M05-001/E26.8; SC-M05-001/E27.2; SC-M05-001/E28.4; SC-M05-001/E29.2; SC-M05-001/E35.2; SC-M05-001/E36.2; SC-M05-001/E37.2; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.06 | SC-M05-001/E14.4; SC-M05-001/E23.2; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.07 | SC-M05-001/E14.4; SC-M05-001/E23.2; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.08 | SC-M05-001/E14.4; SC-M05-001/E23.2; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.09 | SC-M05-001/E24.5; SC-M05-001/E24.6; SC-M05-001/E25.5; SC-M05-001/E25.6; SC-M05-001/E26.5; SC-M05-001/E27.5; SC-M05-001/E27.6; SC-M05-001/E37.5; SC-M05-001/E37.6; AUT-M05-004; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.10 | SC-M05-001/E24.6; SC-M05-001/E25.6; SC-M05-001/E26.6; SC-M05-001/E26.7; SC-M05-001/E37.6; SC-M05-001/E37.7; AUT-M05-004; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.11 | SC-M05-001/E24.6; SC-M05-001/E24.7; SC-M05-001/E24.8; SC-M05-001/E25.6; SC-M05-001/E25.7; SC-M05-001/E25.8; AUT-M05-004; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.12 | SC-M05-001/E7.4; SC-M05-001/E10.6; SC-M05-001/E11.5; SC-M05-001/E11.6; SC-M05-001/E12.6; SC-M05-001/E13.6; SC-M05-001/E19.8; SC-M05-001/E21.6; SC-M05-001/E22.6; SC-M05-001/E26.12; SC-M05-001/E27.6; SC-M05-001/E28.8; SC-M05-001/E29.6; SC-M05-001/E35.6; SC-M05-001/E36.6; SC-M05-002/E9.4; AUT-M05-002; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.13 | SC-M05-001/E7.4; SC-M05-001/E24.8; SC-M05-001/E25.8; SC-M05-001/E37.10; SC-M05-002/E9.4; AUT-M05-002; AUT-M05-004; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.14 | SC-M05-001/M4; SC-M05-001/E1.4; SC-M05-001/E2.4; SC-M05-001/E7.4; SC-M05-001/E14.5; SC-M05-001/E23.3; SC-M05-002/E9.4; AUT-M05-002; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.15 | SC-M05-001/E10.2; SC-M05-001/E11.2; SC-M05-001/E12.2; SC-M05-001/E13.2; SC-M05-001/E14.2; SC-M05-001/E19.4; SC-M05-001/E20.1; SC-M05-001/E20.2; SC-M05-001/E21.1; SC-M05-001/E21.2; SC-M05-001/E22.2; SC-M05-001/E23.2; SC-M05-001/E24.2; SC-M05-001/E25.2; SC-M05-001/E26.2; SC-M05-001/E26.8; SC-M05-001/E27.2; SC-M05-001/E28.4; SC-M05-001/E29.2; SC-M05-001/E35.2; SC-M05-001/E36.2; SC-M05-001/E37.2; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.16 | SC-M05-001/E10.2; SC-M05-001/E11.2; SC-M05-001/E12.2; SC-M05-001/E13.2; SC-M05-001/E14.2; SC-M05-001/E15.2; SC-M05-001/E16.2; SC-M05-001/E17.2; SC-M05-001/E19.4; SC-M05-001/E21.2; SC-M05-001/E22.2; SC-M05-001/E23.2; SC-M05-001/E24.2; SC-M05-001/E25.2; SC-M05-001/E26.2; SC-M05-001/E26.8; SC-M05-001/E27.2; SC-M05-001/E28.4; SC-M05-001/E29.2; SC-M05-001/E35.2; SC-M05-001/E36.2; SC-M05-001/E37.2; SC-M05-001/E37.7; SC-M05-001/E37.8; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.17 | SC-M05-001/E15.2; SC-M05-001/E15.3; SC-M05-001/E16.2; SC-M05-001/E16.3; SC-M05-001/E17.2; SC-M05-001/E17.3; SC-M05-001/E37.8; SC-M05-001/E37.9; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.18 | SC-M05-001/E39.1; SC-M05-001/E39.2; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.19 | SC-M05-001/E10.4; SC-M05-001/E11.4; SC-M05-001/E12.4; SC-M05-001/E13.4; SC-M05-001/E19.6; SC-M05-001/E21.4; SC-M05-001/E22.4; SC-M05-001/E24.4; SC-M05-001/E25.4; SC-M05-001/E26.4; SC-M05-001/E26.10; SC-M05-001/E27.4; SC-M05-001/E28.6; SC-M05-001/E29.4; SC-M05-001/E35.4; SC-M05-001/E36.4; SC-M05-001/E37.4; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.20 | SC-M05-001/E28.1; SC-M05-001/E28.2; SC-M05-001/E28.3; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.21 | SC-M05-009/M2; SC-M05-009/M4; SC-M05-009/E8.2; SC-M05-009/E9.2; SC-M05-009/E10.2; SC-M05-009/E13.1; SC-M05-009/E13.2; SC-M05-009/E20.2; SC-M05-009/E20.4; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-02.22 | AUT-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03.01 | SC-M05-001/M2; SC-M05-001/M4; SC-M05-001/E1.4; SC-M05-001/E2.4; SC-M05-001/E7.4; SC-M05-001/E10.6; SC-M05-001/E13.6; SC-M05-001/E19.8; SC-M05-001/E21.6; SC-M05-001/E22.6; SC-M05-001/E26.12; SC-M05-001/E28.8; SC-M05-002/M1; SC-M05-002/M2; SC-M05-002/M3; SC-M05-002/M4; SC-M05-002/E1.1; SC-M05-002/E1.2; SC-M05-002/E2.3; SC-M05-002/E2.4; SC-M05-002/E3.3; SC-M05-002/E3.4; SC-M05-002/E4.3; SC-M05-002/E4.4; SC-M05-002/E5.3; SC-M05-002/E5.4; SC-M05-002/E6.2; SC-M05-002/E7.1; SC-M05-002/E7.2; SC-M05-002/E8.2; SC-M05-002/E9.4; SC-M05-002/E10.1; SC-M05-002/E16.4; SC-M05-009/M4; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03.02 | SC-M05-002/M4; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-002/E7.1; SC-M05-002/E7.2; SC-M05-002/E9.4; SC-M05-009/M4; SC-M05-009/E11.1; SC-M05-009/E11.2; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03.03 | SC-M05-002/M4; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-002/E6.1; SC-M05-002/E6.2; SC-M05-002/E7.1; SC-M05-002/E7.2; SC-M05-002/E8.2; SC-M05-002/E9.4; SC-M05-002/E16.4; SC-M05-009/M4; SC-M05-009/E11.1; SC-M05-009/E11.2; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03.04 | SC-M05-002/M4; SC-M05-002/E2.1; SC-M05-002/E2.2; SC-M05-002/E2.3; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-002/E9.4; SC-M05-009/M4; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03.05 | SC-M05-002/M4; SC-M05-002/E2.4; SC-M05-002/E3.1; SC-M05-002/E3.2; SC-M05-002/E3.3; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-002/E9.4; SC-M05-009/M4; SC-M05-009/E5.1; SC-M05-009/E20.4; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03.06 | SC-M05-002/M4; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.1; SC-M05-002/E4.2; SC-M05-002/E4.3; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-002/E9.4; SC-M05-009/M4; SC-M05-009/E6.1; SC-M05-009/E20.4; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03.07 | SC-M05-002/M4; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.1; SC-M05-002/E5.2; SC-M05-002/E5.3; SC-M05-002/E5.4; SC-M05-002/E9.4; SC-M05-009/M4; SC-M05-009/E7.1; SC-M05-009/E20.4; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03.08 | SC-M05-002/M4; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-002/E6.1; SC-M05-002/E6.2; SC-M05-002/E9.4; SC-M05-009/M4; SC-M05-009/E11.1; SC-M05-009/E11.2; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03.09 | SC-M05-002/M4; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-002/E8.1; SC-M05-002/E8.2; SC-M05-002/E9.4; SC-M05-007/M2; SC-M05-007/E6.2; SC-M05-009/M4; SC-M05-009/E12.1; SC-M05-009/E12.2; SC-M05-009/E20.4; RULE-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03.10 | SC-M05-001/E33.3; SC-M05-002/E9.1; SC-M05-002/E9.2; SC-M05-002/E9.3; SC-M05-002/E9.4; SC-M05-002/E14.3; SC-M05-002/E16.1; SC-M05-002/E16.2; SC-M05-002/E16.3; SC-M05-002/E16.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03.11 | SC-M05-001/E10.4; SC-M05-001/E11.4; SC-M05-001/E12.4; SC-M05-001/E13.4; SC-M05-001/E19.6; SC-M05-001/E21.4; SC-M05-001/E22.4; SC-M05-001/E24.4; SC-M05-001/E25.4; SC-M05-001/E26.4; SC-M05-001/E26.10; SC-M05-001/E27.4; SC-M05-001/E28.6; SC-M05-001/E29.4; SC-M05-001/E35.4; SC-M05-001/E36.4; SC-M05-001/E37.4; SC-M05-002/M2; SC-M05-002/M4; SC-M05-002/E1.2; SC-M05-002/E9.2; SC-M05-002/E9.4; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03.12 | SC-M05-002/E17.1; SC-M05-002/E17.2 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03.13 | RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-03.14 | SC-M05-002/M4; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-002/E6.2; SC-M05-002/E7.2; SC-M05-002/E8.2; SC-M05-002/E9.4; SC-M05-002/E16.4; SC-M05-003/E1.2; SC-M05-003/E2.2; SC-M05-009/M4; SC-M05-009/E11.2; SC-M05-009/E20.4; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-04.01 | SC-M05-003/M1; SC-M05-003/M2; SC-M05-003/E5.1; SC-M05-003/E5.2 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-04.02 | SC-M05-003/E1.1; SC-M05-003/E1.2; SC-M05-003/E4.1; SC-M05-003/E4.2; SC-M05-003/E5.1; SC-M05-003/E5.2 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-04.03 | SC-M05-003/E1.2; SC-M05-003/E4.2; SC-M05-003/E5.2; SC-M05-007/M2; SC-M05-007/E6.2; RULE-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-04.04 | SC-M05-003/E2.1; SC-M05-003/E2.2; SC-M05-003/E3.1; SC-M05-003/E3.2 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-04.05 | SC-M05-002/E16.2; SC-M05-002/E16.4; SC-M05-003/E2.2; SC-M05-007/M2; SC-M05-007/E6.2; SC-M05-009/E17.2; RULE-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-04.06 | SC-M05-003/M2; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05.01 | AUT-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05.02 | AUT-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05.03 | AUT-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05.04 | AUT-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05.05 | AUT-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05.06 | AUT-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05.07 | SC-M05-007/M2; SC-M05-007/E6.2; SC-M05-008/E2.1; AUT-M05-001; RULE-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05.08 | AUT-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05.09 | AUT-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05.10 | SC-M05-003/M2; SC-M05-008/M2; SC-M05-008/E2.1; SC-M05-008/E7.2; AUT-M05-001; RULE-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05.11 | AUT-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05.12 | AUT-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05.13 | AUT-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-05.14 | SC-M05-008/M2; SC-M05-008/E2.1; SC-M05-008/E7.2; AUT-M05-001; RULE-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-06.01 | SC-M05-004/M1; SC-M05-004/M2; SC-M05-004/E2.1; SC-M05-004/E2.2; SC-M05-004/E3.1 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-06.02 | SC-M05-004/E1.1 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-06.03 | SC-M05-004/M2; SC-M05-004/E4.1; SC-M05-004/E4.2; SC-M05-004/E5.1; SC-M05-004/E5.2; SC-M05-004/E6.1; SC-M05-004/E6.2; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-06.04 | SC-M05-004/M2; SC-M05-004/E2.2; SC-M05-004/E3.1 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-06.05 | SC-M05-004/M2; SC-M05-004/E2.2; SC-M05-004/E3.1 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-06.06 | SC-M05-004/M2; SC-M05-004/E3.1; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-06.07 | SC-M05-004/M2; SC-M05-004/E2.2; SC-M05-004/E3.1; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-06.08 | SC-M05-004/M2; SC-M05-004/E1.1; SC-M05-004/E2.1; SC-M05-004/E2.2; SC-M05-004/E3.1; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-07.01 | SC-M05-005/M1; SC-M05-005/M2; SC-M05-005/E2.1; SC-M05-005/E2.2; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-07.02 | SC-M05-005/M2; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-07.03 | SC-M05-005/M2; SC-M05-005/E3.1; SC-M05-005/E3.2; SC-M05-005/E4.1; SC-M05-005/E4.2; SC-M05-005/E5.1; SC-M05-005/E5.2; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-07.04 | SC-M05-005/E1.1 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-07.05 | SC-M05-005/M2; SC-M05-005/E2.2; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-07.06 | SC-M05-005/M2; SC-M05-005/E2.2; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-08.01 | SC-M05-006/M1; SC-M05-006/M2; SC-M05-006/E7.1; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-08.02 | SC-M05-006/E1.1; SC-M05-006/E2.1; SC-M05-006/E3.1; SC-M05-006/E4.1; SC-M05-006/E5.1; SC-M05-006/E6.1; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-08.03 | SC-M05-006/M2; SC-M05-006/E8.1; SC-M05-006/E8.2; SC-M05-006/E9.1; SC-M05-006/E9.2; SC-M05-006/E10.1; SC-M05-006/E10.2; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-08.04 | SC-M05-006/M2; SC-M05-006/E7.1 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-08.05 | SC-M05-006/M2; SC-M05-006/E7.1; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-08.06 | SC-M05-006/M2; SC-M05-006/E7.1; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-09.01 | SC-M05-007/M1; SC-M05-007/M2; SC-M05-007/E2.1; SC-M05-007/E2.2; SC-M05-007/E6.1; SC-M05-007/E6.2 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-09.02 | SC-M05-007/M2; SC-M05-007/E2.2; SC-M05-007/E6.2; RULE-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-09.03 | SC-M05-002/E16.2; SC-M05-002/E16.4; SC-M05-007/M2; SC-M05-007/E2.2; SC-M05-007/E6.2; SC-M05-009/E17.2; RULE-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-09.04 | SC-M05-007/E3.1; SC-M05-007/E4.1; SC-M05-007/E4.2; SC-M05-007/E5.1; SC-M05-007/E5.2; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-09.05 | SC-M05-007/E1.1; AUT-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-09.06 | RULE-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-09.07 | SC-M05-007/M2; SC-M05-007/E2.1; SC-M05-007/E2.2; SC-M05-007/E6.2; AUT-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-10.01 | SC-M05-008/M1; SC-M05-008/M2; SC-M05-008/E2.1; SC-M05-008/E3.1; SC-M05-008/E3.2; SC-M05-008/E7.1; SC-M05-008/E7.2 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-10.02 | SC-M05-008/M2; SC-M05-008/E2.1; SC-M05-008/E3.2; SC-M05-008/E7.2; RULE-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-10.03 | SC-M05-008/M2; SC-M05-008/E1.1; SC-M05-008/E2.1; SC-M05-008/E3.2; SC-M05-008/E7.2; RULE-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-10.04 | SC-M05-008/E4.1; SC-M05-008/E5.1; SC-M05-008/E5.2; SC-M05-008/E6.1; SC-M05-008/E6.2; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-10.05 | SC-M05-008/E1.1; AUT-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-10.06 | SC-M05-008/M2; SC-M05-008/E2.1; SC-M05-008/E3.1; SC-M05-008/E3.2; SC-M05-008/E7.2; AUT-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-11.01 | SC-M05-009/M1; SC-M05-009/M3; SC-M05-009/M4; SC-M05-009/E4.1; SC-M05-009/E8.1; SC-M05-009/E8.2; SC-M05-009/E9.1; SC-M05-009/E9.2; SC-M05-009/E10.1; SC-M05-009/E10.2; SC-M05-009/E13.2; SC-M05-009/E13.3; SC-M05-009/E17.1; SC-M05-009/E17.2; SC-M05-009/E20.1; SC-M05-009/E20.3; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-11.02 | SC-M05-009/M1; SC-M05-009/M3; SC-M05-009/M4; SC-M05-009/E5.1; SC-M05-009/E6.1; SC-M05-009/E7.1; SC-M05-009/E8.1; SC-M05-009/E8.2; SC-M05-009/E9.1; SC-M05-009/E9.2; SC-M05-009/E10.1; SC-M05-009/E10.2; SC-M05-009/E11.1; SC-M05-009/E11.2; SC-M05-009/E12.1; SC-M05-009/E12.2; SC-M05-009/E13.3; SC-M05-009/E20.1; SC-M05-009/E20.3; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-11.03 | SC-M05-009/E1.1; SC-M05-009/E2.1; SC-M05-009/E3.1 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-11.04 | SC-M05-001/E30.1; SC-M05-001/E31.1; SC-M05-002/E11.1; SC-M05-002/E12.1; SC-M05-009/M2; SC-M05-009/E14.1; SC-M05-009/E18.1; SC-M05-009/E18.2; SC-M05-009/E19.1; SC-M05-009/E19.2; SC-M05-009/E20.2; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-11.05 | SC-M05-009/M4; SC-M05-009/E8.2; SC-M05-009/E9.2; SC-M05-009/E10.2; SC-M05-009/E11.2; SC-M05-009/E12.2; SC-M05-009/E17.2; SC-M05-009/E20.4; AUT-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-11.06 | SC-M05-009/M4; SC-M05-009/E8.2; SC-M05-009/E9.2; SC-M05-009/E10.2; SC-M05-009/E11.2; SC-M05-009/E12.2; SC-M05-009/E17.2; SC-M05-009/E20.4; AUT-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| FR-M05-11.07 | SC-M05-009/M4; SC-M05-009/E8.2; SC-M05-009/E9.2; SC-M05-009/E10.2; SC-M05-009/E11.2; SC-M05-009/E12.2; SC-M05-009/E17.2; SC-M05-009/E20.4; AUT-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-01 | SC-M05-003/M2; SC-M05-004/M2; SC-M05-004/E2.2; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-02 | SC-M05-003/M2; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-03 | SC-M05-001/M2; SC-M05-001/M3; SC-M05-001/M4; SC-M05-001/E1.1; SC-M05-001/E1.2; SC-M05-001/E1.3; SC-M05-001/E1.4; SC-M05-001/E2.1; SC-M05-001/E2.2; SC-M05-001/E2.3; SC-M05-001/E2.4; SC-M05-001/E3.1; SC-M05-001/E4.2; SC-M05-001/E5.2; SC-M05-001/E6.2; SC-M05-001/E10.6; SC-M05-001/E13.6; SC-M05-001/E19.8; SC-M05-001/E21.6; SC-M05-001/E22.6; SC-M05-001/E26.12; SC-M05-001/E28.8; SC-M05-001/E35.5; SC-M05-001/E35.6; SC-M05-001/E36.5; SC-M05-001/E36.6; SC-M05-002/E10.1; SC-M05-009/M4; SC-M05-009/E4.1; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-04 | SC-M05-001/E7.2; SC-M05-001/E7.4; SC-M05-001/E8.4; SC-M05-001/E9.4; SC-M05-001/E10.6; SC-M05-001/E13.6; SC-M05-001/E19.8; SC-M05-001/E21.6; SC-M05-001/E22.6; SC-M05-001/E26.12; SC-M05-001/E28.8; SC-M05-002/E16.4; SC-M05-009/M4; SC-M05-009/E1.1; SC-M05-009/E2.1; SC-M05-009/E3.1; SC-M05-009/E8.1; SC-M05-009/E8.2; SC-M05-009/E9.1; SC-M05-009/E9.2; SC-M05-009/E10.1; SC-M05-009/E10.2; SC-M05-009/E17.2; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-05 | SC-M05-004/M2; SC-M05-004/E1.1; SC-M05-004/E2.1; SC-M05-004/E2.2; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-06 | SC-M05-004/M2; SC-M05-004/E3.1; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-07 | SC-M05-004/M2; SC-M05-004/E2.2 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-08 | SC-M05-006/M2; SC-M05-006/E1.1; SC-M05-006/E2.1; SC-M05-006/E3.1; SC-M05-006/E4.1; SC-M05-006/E5.1; SC-M05-006/E6.1; SC-M05-006/E7.1; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-09 | SC-M05-005/M2; SC-M05-005/E2.2; RULE-M05-003 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-10 | SC-M05-001/E10.1; SC-M05-001/E10.2; SC-M05-001/E11.1; SC-M05-001/E11.2; SC-M05-001/E12.1; SC-M05-001/E12.2; SC-M05-001/E13.1; SC-M05-001/E13.2; SC-M05-001/E14.1; SC-M05-001/E14.2; SC-M05-001/E15.1; SC-M05-001/E16.1; SC-M05-001/E17.1; SC-M05-001/E19.4; SC-M05-001/E21.2; SC-M05-001/E22.1; SC-M05-001/E22.2; SC-M05-001/E23.1; SC-M05-001/E23.2; SC-M05-001/E24.1; SC-M05-001/E24.2; SC-M05-001/E25.1; SC-M05-001/E25.2; SC-M05-001/E26.1; SC-M05-001/E26.2; SC-M05-001/E26.8; SC-M05-001/E27.1; SC-M05-001/E27.2; SC-M05-001/E28.4; SC-M05-001/E29.1; SC-M05-001/E29.2; SC-M05-001/E35.1; SC-M05-001/E35.2; SC-M05-001/E36.1; SC-M05-001/E36.2; SC-M05-001/E37.1; SC-M05-001/E37.2; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-11 | SC-M05-001/E10.2; SC-M05-001/E11.2; SC-M05-001/E12.2; SC-M05-001/E13.2; SC-M05-001/E14.2; SC-M05-001/E19.4; SC-M05-001/E21.2; SC-M05-001/E22.2; SC-M05-001/E23.2; SC-M05-001/E24.2; SC-M05-001/E25.2; SC-M05-001/E26.2; SC-M05-001/E26.8; SC-M05-001/E27.2; SC-M05-001/E27.5; SC-M05-001/E27.6; SC-M05-001/E28.4; SC-M05-001/E29.2; SC-M05-001/E35.2; SC-M05-001/E36.2; SC-M05-001/E37.2; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-12 | SC-M05-001/E10.2; SC-M05-001/E11.2; SC-M05-001/E12.2; SC-M05-001/E13.2; SC-M05-001/E14.2; SC-M05-001/E18.1; SC-M05-001/E18.2; SC-M05-001/E19.1; SC-M05-001/E19.3; SC-M05-001/E19.4; SC-M05-001/E21.2; SC-M05-001/E22.2; SC-M05-001/E23.2; SC-M05-001/E24.2; SC-M05-001/E25.2; SC-M05-001/E26.2; SC-M05-001/E26.8; SC-M05-001/E27.2; SC-M05-001/E28.4; SC-M05-001/E29.2; SC-M05-001/E35.2; SC-M05-001/E36.2; SC-M05-001/E37.2; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-13 | SC-M05-001/E10.4; SC-M05-001/E10.5; SC-M05-001/E10.6; SC-M05-001/E11.4; SC-M05-001/E11.5; SC-M05-001/E12.4; SC-M05-001/E12.5; SC-M05-001/E13.4; SC-M05-001/E13.5; SC-M05-001/E13.6; SC-M05-001/E19.6; SC-M05-001/E19.7; SC-M05-001/E19.8; SC-M05-001/E21.4; SC-M05-001/E21.5; SC-M05-001/E21.6; SC-M05-001/E22.4; SC-M05-001/E22.5; SC-M05-001/E22.6; SC-M05-001/E24.4; SC-M05-001/E25.4; SC-M05-001/E26.4; SC-M05-001/E26.10; SC-M05-001/E26.11; SC-M05-001/E26.12; SC-M05-001/E27.4; SC-M05-001/E28.6; SC-M05-001/E28.7; SC-M05-001/E28.8; SC-M05-001/E29.4; SC-M05-001/E35.4; SC-M05-001/E35.5; SC-M05-001/E35.6; SC-M05-001/E36.4; SC-M05-001/E36.5; SC-M05-001/E36.6; SC-M05-001/E37.4; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-14 | SC-M05-001/E10.4; SC-M05-001/E11.4; SC-M05-001/E12.4; SC-M05-001/E13.4; SC-M05-001/E14.4; SC-M05-001/E19.6; SC-M05-001/E21.4; SC-M05-001/E22.4; SC-M05-001/E23.2; SC-M05-001/E24.4; SC-M05-001/E25.4; SC-M05-001/E26.4; SC-M05-001/E26.10; SC-M05-001/E27.4; SC-M05-001/E28.6; SC-M05-001/E29.4; SC-M05-001/E35.4; SC-M05-001/E36.4; SC-M05-001/E37.4; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-15 | SC-M05-001/E24.5; SC-M05-001/E24.6; SC-M05-001/E24.8; SC-M05-001/E25.5; SC-M05-001/E25.6; SC-M05-001/E25.8; SC-M05-001/E27.5; SC-M05-001/E37.10; AUT-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-16 | SC-M05-001/E5.2; SC-M05-001/E6.2; SC-M05-001/E7.4; SC-M05-001/E10.6; SC-M05-001/E11.5; SC-M05-001/E11.6; SC-M05-001/E12.6; SC-M05-001/E13.6; SC-M05-001/E19.8; SC-M05-001/E21.6; SC-M05-001/E22.6; SC-M05-001/E24.8; SC-M05-001/E25.8; SC-M05-001/E26.12; SC-M05-001/E27.6; SC-M05-001/E28.8; SC-M05-001/E29.6; SC-M05-001/E35.6; SC-M05-001/E36.6; SC-M05-001/E37.10; SC-M05-002/E9.4; AUT-M05-002; AUT-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-17 | SC-M05-001/E10.2; SC-M05-001/E11.2; SC-M05-001/E12.2; SC-M05-001/E13.2; SC-M05-001/E14.2; SC-M05-001/E19.4; SC-M05-001/E20.1; SC-M05-001/E20.2; SC-M05-001/E21.1; SC-M05-001/E21.2; SC-M05-001/E22.2; SC-M05-001/E23.2; SC-M05-001/E24.2; SC-M05-001/E25.2; SC-M05-001/E26.2; SC-M05-001/E26.7; SC-M05-001/E26.8; SC-M05-001/E27.2; SC-M05-001/E28.4; SC-M05-001/E29.2; SC-M05-001/E35.2; SC-M05-001/E36.2; SC-M05-001/E37.2; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-18 | SC-M05-001/E10.2; SC-M05-001/E11.2; SC-M05-001/E12.2; SC-M05-001/E13.2; SC-M05-001/E14.2; SC-M05-001/E15.2; SC-M05-001/E16.2; SC-M05-001/E17.2; SC-M05-001/E19.4; SC-M05-001/E21.2; SC-M05-001/E22.2; SC-M05-001/E23.2; SC-M05-001/E24.2; SC-M05-001/E25.2; SC-M05-001/E26.2; SC-M05-001/E26.8; SC-M05-001/E27.2; SC-M05-001/E28.4; SC-M05-001/E29.2; SC-M05-001/E35.2; SC-M05-001/E36.2; SC-M05-001/E37.2; SC-M05-001/E37.7; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-19 | SC-M05-001/E14.4; SC-M05-001/E23.2; RULE-M05-004 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-20 | SC-M05-002/M2; SC-M05-002/M4; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.1; SC-M05-002/E4.2; SC-M05-002/E4.3; SC-M05-002/E4.4; SC-M05-002/E5.1; SC-M05-002/E5.2; SC-M05-002/E5.3; SC-M05-002/E5.4; SC-M05-002/E7.1; SC-M05-002/E9.4; SC-M05-009/M4; SC-M05-009/E6.1; SC-M05-009/E7.1; SC-M05-009/E20.4; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-21 | SC-M05-002/M4; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-002/E9.4; SC-M05-009/M4; SC-M05-009/E11.2; SC-M05-009/E20.4 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-22 | SC-M05-001/M2; SC-M05-001/M4; SC-M05-001/E1.4; SC-M05-001/E2.4; SC-M05-002/M2; SC-M05-002/M4; SC-M05-002/E1.1; SC-M05-002/E1.2; SC-M05-002/E2.1; SC-M05-002/E2.2; SC-M05-002/E2.3; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-002/E9.4; SC-M05-009/M4; SC-M05-009/E8.1; SC-M05-009/E8.2; SC-M05-009/E9.1; SC-M05-009/E9.2; SC-M05-009/E10.1; SC-M05-009/E10.2; SC-M05-009/E20.4; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-23 | SC-M05-002/M2; SC-M05-002/M4; SC-M05-002/E2.4; SC-M05-002/E3.1; SC-M05-002/E3.2; SC-M05-002/E3.3; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-002/E9.4; SC-M05-009/M4; SC-M05-009/E5.1; SC-M05-009/E20.4; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-24 | SC-M05-002/M4; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-002/E6.1; SC-M05-002/E6.2; SC-M05-002/E7.1; SC-M05-002/E7.2; SC-M05-002/E9.4; SC-M05-009/M4; SC-M05-009/E11.1; SC-M05-009/E11.2; SC-M05-009/E20.4; RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-25 | RULE-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-26 | SC-M05-002/M4; SC-M05-002/E2.4; SC-M05-002/E3.4; SC-M05-002/E4.4; SC-M05-002/E5.4; SC-M05-002/E8.2; SC-M05-002/E9.4; SC-M05-002/E16.2; SC-M05-002/E16.4; SC-M05-003/E1.2; SC-M05-003/E2.2; SC-M05-003/E4.2; SC-M05-003/E5.2; SC-M05-007/M2; SC-M05-007/E1.1; SC-M05-007/E2.2; SC-M05-007/E6.2; SC-M05-009/M4; SC-M05-009/E12.2; SC-M05-009/E17.2; SC-M05-009/E20.4; RULE-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-27 | SC-M05-008/M2; SC-M05-008/E1.1; SC-M05-008/E2.1; SC-M05-008/E3.2; SC-M05-008/E7.2; RULE-M05-002 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-28 | RULE-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-29 | AUT-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-30 | SC-M05-008/M2; SC-M05-008/E2.1; SC-M05-008/E3.2; SC-M05-008/E7.2; AUT-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |
| BR-M05-31 | SC-M05-008/M2; SC-M05-008/E2.1; SC-M05-008/E3.2; SC-M05-008/E7.2; AUT-M05-001 | Đối chiếu nội dung/nguồn, chưa phê duyệt |


| UC owner | Guard/lựa chọn | Nhánh | Đích |
|---|---|---|---|
| UC-M05-001 | Lan chọn Topic thứ tư sau ba Topic khác nhau | SC-M05-001/E1 | END:SUCCESS |
| UC-M05-001 | Lan chọn lặp lại một Topic đã chọn | SC-M05-001/E2 | END:SUCCESS |
| UC-M05-001 | Gửi không có Topic nào | SC-M05-001/E3 | END:REJECTED |
| UC-M05-001 | Topic Tin học đã chọn bị xóa khỏi danh mục trước khi gửi; tác giả chọn lại | SC-M05-001/E4 | M4 |
| UC-M05-001 | Lan chọn lưu nháp với 0 Topic thay vì gửi | SC-M05-001/E5 | END:SUCCESS |
| UC-M05-001 | Lan chọn lưu nháp với 3 Topic thay vì gửi | SC-M05-001/E6 | END:SUCCESS |
| UC-M05-001 | Tác giả đổi Topic khi sửa bài đã gửi của mình | SC-M05-001/E7 | END:SUCCESS |
| UC-M05-001 | Lưu sửa bài đã gửi với 0 Topic không hợp lệ | SC-M05-001/E8 | END:REJECTED |
| UC-M05-001 | Lưu sửa bài đã gửi với 4 Topic không hợp lệ | SC-M05-001/E9 | END:REJECTED |
| UC-M05-001 | Tác giả chủ động dùng gợi ý rồi bỏ/chọn thêm và gửi bài | SC-M05-001/E10 | END:SUCCESS |
| UC-M05-001 | Tác giả giữ nguyên toàn bộ gợi ý hợp lệ khi gửi | SC-M05-001/E11 | END:SUCCESS |
| UC-M05-001 | Tác giả bỏ mọi gợi ý nhưng chọn Topic khác hợp lệ trước khi gửi | SC-M05-001/E12 | END:SUCCESS |
| UC-M05-001 | AI trả một phần Topic không thuộc danh mục | SC-M05-001/E13 | END:SUCCESS |
| UC-M05-001 | Mọi Topic AI trả về đều ngoài danh mục hiện tại | SC-M05-001/E14 | M4 |
| UC-M05-001 | Tác giả yêu cầu gợi ý khi AI tổng Tắt, Topic suggestion Bật | SC-M05-001/E15 | M4 |
| UC-M05-001 | Tác giả yêu cầu gợi ý khi AI tổng Bật, Topic suggestion Tắt | SC-M05-001/E16 | M4 |
| UC-M05-001 | Tác giả yêu cầu gợi ý khi cả hai công tắc Tắt | SC-M05-001/E17 | M4 |
| UC-M05-001 | Tổng tiêu đề và nội dung chữ chỉ 19 từ; tác giả chọn thủ công | SC-M05-001/E18 | M4 |
| UC-M05-001 | Tác giả bổ sung từ thứ 20 sau cảnh báo quá ngắn rồi yêu cầu lại | SC-M05-001/E19 | END:SUCCESS |
| UC-M05-001 | Yêu cầu thứ 11 trong 60 giây gần nhất, tác giả chọn thủ công | SC-M05-001/E20 | M4 |
| UC-M05-001 | Yêu cầu được phép khi yêu cầu cũ đã rời cửa sổ trượt | SC-M05-001/E21 | END:SUCCESS |
| UC-M05-001 | Lần thử đầu lỗi/quá 10 giây, lần thử lại đúng một lần thành công | SC-M05-001/E22 | END:SUCCESS |
| UC-M05-001 | Cả hai lần thử AI lỗi hoặc quá 10 giây, tác giả chọn thủ công | SC-M05-001/E23 | M4 |
| UC-M05-001 | Sau gợi ý, tác giả đổi tiêu đề rồi gửi mà không gợi ý lại | SC-M05-001/E24 | END:SUCCESS |
| UC-M05-001 | Sau gợi ý, tác giả đổi nội dung chữ rồi gửi mà không gợi ý lại | SC-M05-001/E25 | END:SUCCESS |
| UC-M05-001 | Gợi ý lỗi thời, tác giả bấm gợi ý lại và chốt tập cuối rõ ràng | SC-M05-001/E26 | END:SUCCESS |
| UC-M05-001 | Tác giả thay tệp, không đổi tiêu đề/nội dung chữ sau gợi ý | SC-M05-001/E27 | END:SUCCESS |
| UC-M05-001 | Tác giả dùng AI khi sửa bài đã gửi, sau đó lưu bản sửa | SC-M05-001/E28 | END:SUCCESS |
| UC-M05-001 | Có gợi ý hợp lệ nhưng tác giả chỉ lưu nháp | SC-M05-001/E29 | END:SUCCESS |
| UC-M05-001 | User có phiên nhưng đang đổi phân loại bài người khác mà không là Mod/Admin | SC-M05-001/E30 | END:REJECTED |
| UC-M05-001 | User có phiên nhưng đang đổi phân loại bài người khác mà không là Mod/Admin | SC-M05-001/E31 | END:REJECTED |
| UC-M05-001 | Tác giả yêu cầu sửa phân loại bài Chờ duyệt/Đã xóa hoặc Bị Mod ẩn | SC-M05-001/E32 | END:REJECTED |
| UC-M05-001 | Trạng thái bài chuyển sang không cho sửa sau khi đã mở sửa hợp lệ | SC-M05-001/E33 | END:REJECTED |
| UC-M05-001 | Phiên đã hết hiệu lực và không làm mới được tại thời điểm ghi | SC-M05-001/E34 | END:REJECTED |
| UC-M05-001 | Sau gợi ý hợp lệ, tác giả gửi tập cuối có 0 Topic không hợp lệ | SC-M05-001/E35 | END:REJECTED |
| UC-M05-001 | Sau gợi ý hợp lệ, tác giả gửi tập cuối có 4 Topic không hợp lệ | SC-M05-001/E36 | END:REJECTED |
| UC-M05-001 | Gợi ý đã lỗi thời, tác giả yêu cầu lại khi công tắc gợi ý đang tắt rồi chọn thủ công | SC-M05-001/E37 | END:SUCCESS |
| UC-M05-003 | Tác giả không muốn gắn Tag hoặc bỏ hết Tag | SC-M05-002/E1 | END:SUCCESS |
| UC-M05-003 | Tag thứ sáu; tác giả sửa rồi gửi | SC-M05-002/E2 | END:SUCCESS |
| UC-M05-003 | Tên Tag 31 ký tự không tính #; tác giả sửa rồi gửi | SC-M05-002/E3 | END:SUCCESS |
| UC-M05-003 | Tên có ký tự không hợp lệ; tác giả sửa rồi gửi | SC-M05-002/E4 | END:SUCCESS |
| UC-M05-003 | Tên không có chữ cái; tác giả sửa rồi gửi | SC-M05-002/E5 | END:SUCCESS |
| UC-M05-003 | Tác giả nhập cùng tên Tag khác chữ hoa/thường hai lần | SC-M05-002/E6 | END:SUCCESS |
| UC-M05-003 | Tên có dấu và không dấu khác nhau, đều hợp lệ | SC-M05-002/E7 | END:SUCCESS |
| UC-M05-003 | Tác giả nhập lại #abc đang bị vô hiệu hóa | SC-M05-002/E8 | END:SUCCESS |
| UC-M05-003 | Tác giả thêm/bỏ Tag khi sửa bài đã gửi | SC-M05-002/E9 | END:SUCCESS |
| UC-M05-003 | Cổng gửi M03 không đạt vì Topic hiện có bị xóa hoặc không còn Topic hợp lệ | SC-M05-002/E10 | END:REJECTED |
| UC-M05-003 | User có phiên nhưng đang đổi phân loại bài người khác mà không là Mod/Admin | SC-M05-002/E11 | END:REJECTED |
| UC-M05-003 | User có phiên nhưng đang đổi phân loại bài người khác mà không là Mod/Admin | SC-M05-002/E12 | END:REJECTED |
| UC-M05-003 | Tác giả yêu cầu sửa phân loại bài Chờ duyệt/Đã xóa hoặc Bị Mod ẩn | SC-M05-002/E13 | END:REJECTED |
| UC-M05-003 | Trạng thái bài chuyển sang không cho sửa sau khi đã mở sửa hợp lệ | SC-M05-002/E14 | END:REJECTED |
| UC-M05-003 | Phiên đã hết hiệu lực và không làm mới được tại thời điểm ghi | SC-M05-002/E15 | END:REJECTED |
| UC-M05-003 | Sửa Tag khác trong khi bài đang giữ liên kết với Tag bị vô hiệu hóa | SC-M05-002/E16 | END:SUCCESS |
| UC-M05-004 | Người xem chọn danh sách Tag thay cho Topic | SC-M05-003/E1 | END:SUCCESS |
| UC-M05-004 | Người xem yêu cầu đọc nhãn Topic, Tag trên bài công khai | SC-M05-003/E2 | END:SUCCESS |
| UC-M05-004 | Đọc nhãn bài không được phép hiển thị với Guest | SC-M05-003/E3 | END:REJECTED |
| UC-M05-004 | Danh sách Tag không có Tag hoạt động | SC-M05-003/E4 | END:SUCCESS |
| UC-M05-006 | Tên mới trùng tên hiện có sau quy tắc so sánh | SC-M05-004/E1 | END:REJECTED |
| UC-M05-006 | Tên chỉ khác dấu không bị coi là trùng | SC-M05-004/E2 | END:SUCCESS |
| UC-M05-006 | Danh mục đã có nhiều Topic, tên mới vẫn không trùng | SC-M05-004/E3 | END:SUCCESS |
| UC-M05-007 | Cùng Topic làm cả nguồn và đích | SC-M05-005/E1 | END:REJECTED |
| UC-M05-007 | Admin chọn cặp khác, chưa có liên kết trùng đích | SC-M05-005/E2 | END:SUCCESS |
| UC-M05-008 | Topic còn ít nhất một bài ngoài nháp: Chờ duyệt | SC-M05-006/E1 | END:REJECTED |
| UC-M05-008 | Topic còn ít nhất một bài ngoài nháp: Đã đăng | SC-M05-006/E2 | END:REJECTED |
| UC-M05-008 | Topic còn ít nhất một bài ngoài nháp: Tự ẩn | SC-M05-006/E3 | END:REJECTED |
| UC-M05-008 | Topic còn ít nhất một bài ngoài nháp: Bị từ chối | SC-M05-006/E4 | END:REJECTED |
| UC-M05-008 | Topic còn ít nhất một bài ngoài nháp: Đã xóa 2 ngày trước, còn 7 ngày khôi phục | SC-M05-006/E5 | END:REJECTED |
| UC-M05-008 | Topic còn ít nhất một bài ngoài nháp: Đã xóa hẳn nhưng M03 vẫn giữ liên kết bài–Topic | SC-M05-006/E6 | END:REJECTED |
| UC-M05-008 | Topic chưa có bài viết nào, cũng không có follow | SC-M05-006/E7 | END:SUCCESS |
| UC-M05-009 | Tag đã bị vô hiệu hóa từ trước | SC-M05-007/E1 | END:SUCCESS |
| UC-M05-009 | Mod không nhập lý do | SC-M05-007/E2 | END:SUCCESS |
| UC-M05-009 | Phiên hoặc vai trò điều phối không còn hợp lệ khi yêu cầu | SC-M05-007/E3 | END:REJECTED |
| UC-M05-010 | Tag đã hoạt động | SC-M05-008/E1 | END:SUCCESS |
| UC-M05-010 | Tag được kích hoạt lại nhưng điểm Trending gần nhất bằng0 hoặc chưa có kỳ tính sau kích hoạt | SC-M05-008/E2 | END:SUCCESS |
| UC-M05-010 | Mod để trống lý do khi kích hoạt lại | SC-M05-008/E3 | END:SUCCESS |
| UC-M05-010 | Phiên hoặc vai trò điều phối không còn hợp lệ khi yêu cầu | SC-M05-008/E4 | END:REJECTED |
| UC-M05-011 | Không còn Topic | SC-M05-009/E1 | END:REJECTED |
| UC-M05-011 | Có hơn3 Topic | SC-M05-009/E2 | END:REJECTED |
| UC-M05-011 | Có hơn5 Tag | SC-M05-009/E3 | END:REJECTED |
| UC-M05-011 | Topic đã bị xóa hoặc không thuộc danh mục | SC-M05-009/E4 | END:REJECTED |
| UC-M05-011 | Tag dài31 ký tự | SC-M05-009/E5 | END:REJECTED |
| UC-M05-011 | Tag có ký tự sai | SC-M05-009/E6 | END:REJECTED |
| UC-M05-011 | Tag không có chữ cái | SC-M05-009/E7 | END:REJECTED |
| UC-M05-011 | Mod chỉ đổi Topic, phần không sửa được giữ | SC-M05-009/E8 | END:SUCCESS |
| UC-M05-011 | Mod chỉ đổi Tag, phần không sửa được giữ | SC-M05-009/E9 | END:SUCCESS |
| UC-M05-011 | Mod bỏ hết Tag, phần không sửa được giữ | SC-M05-009/E10 | END:SUCCESS |
| UC-M05-011 | Mod nhập Tag mới chưa có hoặc trùng sau chuẩn hóa | SC-M05-009/E11 | END:SUCCESS |
| UC-M05-011 | Mod nhập tên Tag bị vô hiệu hóa | SC-M05-009/E12 | END:SUCCESS |
| UC-M05-011 | Mod thử bấm yêu cầu gợi ý cho bài người khác rồi chọn thủ công | SC-M05-009/E13 | M4 |
| UC-M05-011 | Phiên hoặc vai trò điều phối không còn hợp lệ khi yêu cầu | SC-M05-009/E14 | END:REJECTED |
| UC-M05-011 | Bài không được phép sửa theo cổng trạng thái M03 | SC-M05-009/E15 | END:REJECTED |
| UC-M05-011 | Bài không được phép sửa theo cổng trạng thái M03 | SC-M05-009/E16 | END:REJECTED |
| UC-M05-011 | Mod chỉ đổi Topic, bài vẫn giữ Tag cũ đang vô hiệu hóa | SC-M05-009/E17 | END:SUCCESS |


Truy vết ngược ở sources từng bước. Mỗi E thay bước chính, các E tại M1 thay cả đường theo actor khởi tạo khác. E tại M1 không là BF thứ hai; được kiểm riêng vì graph validator mặc định chỉ đi main/E. Kết thúc REJECTED có hậu điều kiện từ chối, không giả thành SUCCESS.

Tổ hợp dùng lớp tương đương: lỗi tên Tag áp lại cùng hợp đồng ở lúc gắn và lưu, số lượng/tên/danh mục khác nhau không cần nhân mọi bộ dữ liệu. Quyền/trạng thái được kiểm ở lượt trả dữ liệu và lượt ghi; nếu thay đổi giữa hai lượt thì kết quả lúc ghi quyết định. Các lỗi Topic/Tag là kiểm độc lập trong tập cuối, không tạo chính sách ưu tiên thông báo khi nhiều lỗi cùng lúc. Gợi ý lỗi thời + gửi hợp lệ và lỗi thời + gợi ý lại đã có đường riêng vì thay điều kiện ghi phản hồi; sửa có gợi ý tươi phải ghi, lưu nháp không ghi. AI tắt không phải lỗi dịch vụ; lỗi/timeout sau retry đi chọn thủ công. Kích hoạt Tag không tự cho hạng Trending khi điểm0/chưa đến kỳ. Không thêm đường hủy/xác nhận hoặc lỗi mạng/lưu/log chưa có hợp đồng.

## 7. Giới hạn nguồn và QA

| ID nguồn | Phần chưa chốt/ranh giới | Xử lý trong bản soạn |
|---|---|---|
| TBD-M05-01 | SSR/SEO/preview link công khai hoãn OPEN-006 | Ngoài phạm vi scenario MS1, không tự thêm luồng |
| TBD-M05-02 | View không là tương tác Trending ở MS1 | Không tính view, không tạo bộ đếm mới |
| NOTE-M05-01 | UI hòa giải Topic đã chọn trước khi có gợi ý mới chưa quy định | Không khẳng định tự hợp nhất/thay toàn bộ tập cũ. SC001 ghi tập gợi ý hợp lệ chọn sẵn theo nguồn rồi actor chủ động chốt tập cuối rõ ràng; chi tiết UI vẫn cần thiết kế/chốt nếu ảnh hưởng lựa chọn |
| NOTE-M05-02 | Tag kích hoạt lại và Trending | Vẫn điểm>0/kỳ gần nhất; không tính realtime hoặc tạo hạng điểm0 |
| NOTE-M05-03 | Gộp khác xóa độc lập | Gộp chuyển mọi bài trước bỏ nguồn; xóa độc lập chặn mọi bài ngoài nháp kể cả còn liên kết theo M03 |
| NOTE-M05-04 | Mô tả cũ nói thông báo Topic có bài mới | Áp FR-M07-02.24 hiện hành: không tạo thông báo; vẫn chuyển/bỏ follow đúng nguồn |
| NOTE-M05-05 | Chưa chốt log của yêu cầu lặp không đổi trạng thái và lỗi lưu trữ/transaction | Chỉ ghi giữ trạng thái; không tự cam kết thêm log, retry hoặc rollback. Không dùng khoảng trống này làm cớ cắt ngắn đường có thay đổi thành công |


Không phát sinh GAP nghiệp vụ mới cần quyết định thay FR. Các NOTE/TBD nguồn nêu trên giới hạn tính đầy đủ: bộ scenario bao phủ hành vi đã xác định trong M05, chưa là đặc tả UI/hạ tầng hoặc mọi module giao tiếp. Báo cáo/lệnh/kiểm tra thực tế ở [QA-M05.md](QA-M05.md). Bản soạn chưa được stakeholder phê duyệt.


## Chuyển đổi ID nhánh sau QA-SC-01

Ngày 11/11/2026, các biến thể vai trò được đăng ký thành E tại M1 theo skill v1.4. Bảng này giữ ID lịch sử để đối chiếu các tài liệu đã dẫn V. Mỗi hàng ánh xạ cả nhánh và các bước cùng số thứ tự, ví dụ V1.2 sang bước .2 của E tương ứng.

| ID lịch sử | ID hiện hành | Điểm thay | Số bước | Nguồn |
| --- | --- | --- | --- | --- |
| SC-M05-001/V1 | SC-M05-001/E38 | M1 | 2 | FR-M05-01.08 |
| SC-M05-001/V2 | SC-M05-001/E39 | M1 | 2 | FR-M05-02.18 |
| SC-M05-002/V1 | SC-M05-002/E17 | M1 | 2 | FR-M05-03.12 |
| SC-M05-003/V1 | SC-M05-003/E5 | M1 | 2 | FR-M05-04.01, FR-M05-04.02, FR-M05-04.03, BR-M05-26 |
| SC-M05-004/V1 | SC-M05-004/E4 | M1 | 2 | FR-M05-06.03 |
| SC-M05-004/V2 | SC-M05-004/E5 | M1 | 2 | FR-M05-06.03 |
| SC-M05-004/V3 | SC-M05-004/E6 | M1 | 2 | FR-M05-06.03 |
| SC-M05-005/V1 | SC-M05-005/E3 | M1 | 2 | FR-M05-07.03 |
| SC-M05-005/V2 | SC-M05-005/E4 | M1 | 2 | FR-M05-07.03 |
| SC-M05-005/V3 | SC-M05-005/E5 | M1 | 2 | FR-M05-07.03 |
| SC-M05-006/V1 | SC-M05-006/E8 | M1 | 2 | FR-M05-08.03 |
| SC-M05-006/V2 | SC-M05-006/E9 | M1 | 2 | FR-M05-08.03 |
| SC-M05-006/V3 | SC-M05-006/E10 | M1 | 2 | FR-M05-08.03 |
| SC-M05-007/V1 | SC-M05-007/E4 | M1 | 2 | FR-M05-09.04 |
| SC-M05-007/V2 | SC-M05-007/E5 | M1 | 2 | FR-M05-09.04 |
| SC-M05-007/V3 | SC-M05-007/E6 | M1 | 2 | FR-M05-09.01, FR-M05-09.02, FR-M05-09.03, FR-M05-09.07, FR-M05-03.09, FR-M05-04.03, FR-M05-04.05, FR-M05-05.07, BR-M05-26, FR-M08-16.02, FR-M06-03.04, FR-M10-14.01, FR-M10-14.02, FR-M10-14.03, FR-M10-14.09 |
| SC-M05-008/V1 | SC-M05-008/E5 | M1 | 2 | FR-M05-10.04 |
| SC-M05-008/V2 | SC-M05-008/E6 | M1 | 2 | FR-M05-10.04 |
| SC-M05-008/V3 | SC-M05-008/E7 | M1 | 2 | FR-M05-10.01, FR-M05-10.02, FR-M05-10.03, FR-M05-10.06, FR-M05-05.10, FR-M05-05.14, BR-M05-27, BR-M05-30, BR-M05-31, FR-M08-16.02, FR-M10-14.01, FR-M10-14.02, FR-M10-14.03, FR-M10-14.09 |
| SC-M05-009/V1 | SC-M05-009/E18 | M1 | 2 | FR-M05-11.04 |
| SC-M05-009/V2 | SC-M05-009/E19 | M1 | 2 | FR-M05-11.04 |
| SC-M05-009/V3 | SC-M05-009/E20 | M1 | 4 | FR-M05-11.01, FR-M05-11.02, FR-M05-11.04, FR-M05-02.21, FR-M03-11.04, FR-M03-11.07, FR-M05-11.05, FR-M05-11.06, FR-M05-11.07, FR-M05-01.01, FR-M05-01.02, FR-M05-01.03, FR-M05-01.04, FR-M05-01.05, FR-M05-01.07, FR-M05-01.09, FR-M05-01.10, BR-M05-03, BR-M05-04, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.05, FR-M05-03.06, FR-M05-03.07, FR-M05-03.08, FR-M05-03.09, FR-M05-03.14, BR-M05-20, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-26, FR-M08-16.02, FR-M03-11.05, FR-M03-11.06, FR-M10-14.01, FR-M10-14.02, FR-M10-14.03, FR-M10-14.09 |
