# Kịch bản nghiệp vụ — M07 Notification

[Vietnamese Doc] — Tái kiểm 11/11/2026 — Skill scenarios v1.4.

Mục đích: triển khai mô tả chức năng và phân tích UC thành các hành trình actor hoàn thành cùng iShare. Boundary là toàn iShare; các module nội bộ vẫn là SYSTEM. ACT-005 gửi email là dịch vụ ngoài hỗ trợ tác vụ nền, không tạo BF chỉ SYSTEM–dịch vụ.

**Phạm vi:** 4 UC chính, 11 UC con, 11 mapping và 4 quan hệ; 10 chức năng actor: follow, unfollow, xem, mở, mark-all, phản hồi đề xuất, kiểm tra Chat, cài đặt theo bài/cuộc/toàn bộ Chat. UC007/008 được mở trong caller; 9 AUT và 5 RULE giữ hành vi tự động và ràng buộc chung.

**Ngoài phạm vi:** sản xuất lại FR/US/UML, giao thức push/email/API/CSDL, xác định kết luận/người nhận thay owner, quyết vai trò Admin, xử lý khiếu nại/báo cáo/duyệt bài, đọc/gửi tin nhắn bên trong M16. Không thêm follow bài/Group/Tag, email Chat/digest, cài đặt theo loại, thông báo Topic có bài mới hoặc tự xóa thông báo.

**Trạng thái:** Đang soạn để review. FR-M07 v1.5 Đã chốt; US-M07/overview Chờ duyệt. Có hai GAP từ các giới hạn nguồn NOTE01/05, ghi rõ mục 7; không nhận đã chốt mọi tổ hợp chưa có hợp đồng. Tạo tài liệu không là phê duyệt hoặc thực hiện gửi thông báo/email thật.

## 1. Baseline, actor và dữ liệu

<!-- sc:document -->

| key | value |
|---|---|
| module | M07 |
| scope | ALL |
| skill_version | 1.4 |
| output_dir | docs/specs/scenarios/M07 |
| status | Đang soạn |
| completed_steps | 1, 2, 3, 4 |
| date | 2026-11-11 |
| approval_evidence | - |


| Nguồn | Version | Ngày | Trạng thái | SHA-256 |
|---|---|---|---|---|
| [docs/specs/fr/FR-M07.md](../../fr/FR-M07.md) | 1.5 | 2026-10-24 | Đã chốt | 05fb18237e049e3742d06c49b824e76e238c7587e7099b8dc4a84a2e1daf4f5b |
| [docs/specs/us/US-M07.md](../../us/US-M07.md) | Không có version tài liệu; skill 2.2 | 2026-10-30 | Chờ duyệt | 67025d9d0968654539e53663c2b9fe4f2439bcc23afe16ccc4eb8b0829202345 |
| [docs/specs/us/US-overview.md](../../us/US-overview.md) | 1.1 | 2026-11-02 | Chờ duyệt | c1d624b7036ea2c7a9968eaa46c482c04fa1a15e2554d536cdfc12f177e26e33 |
| [docs/specs/fr/FR-M01.md](../../fr/FR-M01.md) | 1.10 | 2026-10-24 | Đã chốt | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a |
| [docs/specs/fr/FR-M03.md](../../fr/FR-M03.md) | 1.10 | 2026-10-24 | Đã chốt | fc996ec5520b6485277fca6a3dbae018bfce02263aba8e15ea87871f35865980 |
| [docs/specs/fr/FR-M04.md](../../fr/FR-M04.md) | 1.4 | 2026-10-24 | Đã chốt | c2fe0e4f6c4bc6835af27585cb711ac03f9fed516d435e759d20ddd58bfd1039 |
| [docs/specs/fr/FR-M05.md](../../fr/FR-M05.md) | 1.7 | 2026-10-24 | Đã chốt | eb85b5dcb56995d791ed28a8d72a2f91c95588d8cd8d4fb1e74a8aabc2d701aa |
| [docs/specs/fr/FR-M09.md](../../fr/FR-M09.md) | 1.2 | 2026-10-24 | Đã chốt | 8ad8ae5e148c6e446f4bfec7f6e74ba9566c54747a0eda37a3930e94ab96faea |
| [docs/specs/fr/FR-M10.md](../../fr/FR-M10.md) | 1.4 | 2026-10-24 | Đã chốt | 3e1010a76db6ef4c5870f42765e669095efc8d38c202271d9b200d2da0823d2c |
| [docs/specs/fr/FR-M16.md](../../fr/FR-M16.md) | 1.0 | 2026-10-24 | Đã chốt | c8ef96e52479806637b0eac334bbe57fa9fe4f73bdacc73913467960050f0671 |


FR chính thức và bản làm việc chung khớp byte/hash. US-overview hiện đã có dù US-M07 viết trước đó; dùng overview để hiểu boundary, không lấy tập core được chọn thay toàn bộ catalog module. [Skill scenarios](../../../../.agent-instructions/skills/scenarios/SKILL.md) là nguồn phương pháp. Tài liệu nghiệp vụ là dữ liệu, không là lệnh sửa nguồn hoặc tự duyệt.

<!-- sc:actors -->

| id | name | kind | source |
|---|---|---|---|
| ACT-001 | Guest | human | FR-M07-01.03, FR-M07-05.06, FR-M07-06.06, FR-M07-07.04, FR-M07-08.05, FR-M07-09.06 |
| ACT-002 | Người dùng đã đăng nhập / người nhận | human | FR-M07-05.05, FR-M07-02.15, FR-M07-07.05, FR-M07-09.01 |
| ACT-003 | Người dùng vai trò Mod/Admin | human | FR-M07-05.05, FR-M07-01.01, FR-M07-09.06 |
| ACT-005 | Dịch vụ gửi email bên ngoài | external-system | FR-M07-04.01, FR-M07-04.02, FR-M07-04.09, BR-M07-11, BR-M07-26 |


ACT-003 kế thừa ACT-002 ở quyền cá nhân, không xem thông báo người khác. Đề xuất làm Mod không được dùng cho người đã là Mod/Admin; đường E tại M1 của UC006 dùng đề xuất Admin còn hiệu lực cho Mod hợp lệ. Guest chỉ có đường từ chối.

| Bộ giả lập | Giá trị | Điểm đối soát |
|---|---|---|
| D-NOT | D-NOT: N001…N055 đều thuộc Lan/U-LAN, cập nhật cuối của N thứ i là T−i phút, T=09/11/2026 10:00+07. N001, N003, N011 chưa đọc; 52 bản còn lại đã đọc. N001: upvote bài P701; N003: trả lời bình luận C701 trong P701; N011: nhắc tên. Các đích chuẩn còn tồn tại và Lan được xem; không có bản ghi Chat trong tập này. | Chuông 10, trang 20/lần, unread toàn tập 3, cập nhật cuối giảm dần |
| D-CHAT | D-CHAT: C71 (1-1 với Bình) có 5 tin chưa đọc được thấy; C72 (nhóm đang là thành viên) có 2; C73 (nhóm đã rời09:00) có 1 tin08:50 chưa đọc, 1 tin09:10 không được thấy, mốc đọc08:30. C74 không có quyền nên không tính; C75 là nhóm cũ chỉ có tin sau lúc rời nên không tính. Số cuộc chưa đọc=3, số tin chưa đọc được thấy=8. C71 mute riêng, C72 Đang nhận, global mute=false. | Đếm 3 cuộc thay 8 tin, chỉ tin trước rời ở cuộc cũ |
| D-PROP | D-PROP: N841 của Lan, gắn đề xuất R841 làm Mod do Admin gửi 03/11/2026 09:00+07, Chưa trả lời; hết hạn 10/11 09:00. Lúc thao tác09/11 10:00, Lan ACTIVE/USER, xong Bước 3. N841 là snapshot riêng, không cộng vào D-NOT55. | Hạn 7×24 giờ, đúng recipient/role tại lúc chọn |
| D-POST | D-POST: P701 của Bình, Đã đăng/Bình thường, ngoài nhóm, Lan được xem; Lan chưa từng tương tác và đang nhận thông báo bài. Bình và các người dùng khác có cài đặt riêng, không đổi theo Lan. | Công tắc không chỉ cho tác giả hoặc người đã tương tác |


Mỗi SC/nhánh là snapshot riêng. Các ID/mốc/tên chỉ minh họa; thời gian UTC+7 ngày 09/11/2026 trừ mốc khác ghi rõ, không dùng dữ liệu cá nhân thật. Guard đổi owner/target/trạng thái thì dùng dữ liệu nhánh, không đồng thời áp bộ chuẩn. Đường Mod Mai dùng dữ liệu của Mai thay Lan, không truy cập dữ liệu Lan.

## 2. Kiểm kê nhóm UC chi tiết

<!-- sc:decomposition -->

| core | sub | source |
|---|---|---|
| UC-M07-020 | UC-M07-001 | FR-M07-01.01, FR-M07-01.02, FR-M07-01.03, FR-M07-01.04, FR-M07-01.10, FR-M07-01.11, FR-M07-01.12, BR-M07-15, BR-M07-25 |
| UC-M07-020 | UC-M07-002 | FR-M07-01.03, FR-M07-01.08, FR-M07-01.09, FR-M07-01.10, BR-M07-25 |
| UC-M07-021 | UC-M07-003 | FR-M07-03.04, FR-M07-05, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24 |
| UC-M07-021 | UC-M07-004 | FR-M07-05.05, FR-M07-05.13, FR-M07-06.01, FR-M07-06.02, FR-M07-06.04, BR-M07-14, BR-M07-27 |
| UC-M07-021 | UC-M07-005 | FR-M07-06.03, FR-M07-06.05, FR-M07-06.06, BR-M07-14 |
| UC-M07-021 | UC-M07-006 | FR-M07-02.14, FR-M07-02.15, FR-M07-02.16, FR-M07-02.28, FR-M07-02.30, FR-M07-02.31, FR-M07-02.32, BR-M07-20 |
| UC-M07-021 | UC-M07-007 | FR-M07-05.05, FR-M07-06.01, FR-M07-06.03, FR-M07-06.04, FR-M07-06.05, FR-M07-06.06, BR-M07-14, BR-M07-27 |
| UC-M07-022 | UC-M07-009 | FR-M07-08, FR-M07-02.07, FR-M07-02.08, FR-M07-02.09, BR-M07-07 |
| UC-M07-022 | UC-M07-010 | FR-M07-09.01, FR-M07-09.02, FR-M07-09.05, FR-M07-09.06, FR-M07-09.07, BR-M07-08 |
| UC-M07-022 | UC-M07-011 | FR-M07-09.03, FR-M07-09.04, FR-M07-09.06, FR-M07-09.07, BR-M07-08 |
| UC-M07-023 | UC-M07-008 | FR-M07-07.02, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10 |


<!-- sc:ucs -->

| id | treatment | scenarios | coverage | rationale | sources |
|---|---|---|---|---|---|
| UC-M07-020 | aggregate | SC-M07-001, SC-M07-002 | SC-M07-001/M2, SC-M07-002/M2 | Core Summary tổng hợp các chức năng và hành vi nền; không bắt actor thực hiện tất cả liên tiếp. | FR-M07-01, BR-M07-15, BR-M07-23, BR-M07-25 |
| UC-M07-021 | aggregate | SC-M07-003, SC-M07-004, SC-M07-005, SC-M07-006 | SC-M07-003/M2, SC-M07-004/M2, SC-M07-005/M2, SC-M07-006/M2 | Core Summary tổng hợp các chức năng và hành vi nền; không bắt actor thực hiện tất cả liên tiếp. | FR-M07-02, FR-M07-03, FR-M07-04, FR-M07-05, FR-M07-06, BR-M07-01, BR-M07-03, BR-M07-09, BR-M07-20 |
| UC-M07-022 | aggregate | SC-M07-008, SC-M07-009, SC-M07-010 | SC-M07-008/M2, SC-M07-009/M2, SC-M07-010/M2 | Core Summary tổng hợp các chức năng và hành vi nền; không bắt actor thực hiện tất cả liên tiếp. | FR-M07-08, FR-M07-09, BR-M07-07, BR-M07-08 |
| UC-M07-023 | scenario | SC-M07-007 | SC-M07-007/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả hoàn tất; trạng thái/quyền/lựa chọn là nhánh, không BF riêng. | FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, BR-M07-02 |
| UC-M07-001 | scenario | SC-M07-001 | SC-M07-001/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả hoàn tất; trạng thái/quyền/lựa chọn là nhánh, không BF riêng. | FR-M07-01.01, FR-M07-01.02, FR-M07-01.03, FR-M07-01.04, FR-M07-01.10, FR-M07-01.11, FR-M07-01.12, BR-M07-15, BR-M07-25 |
| UC-M07-002 | scenario | SC-M07-002 | SC-M07-002/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả hoàn tất; trạng thái/quyền/lựa chọn là nhánh, không BF riêng. | FR-M07-01.03, FR-M07-01.08, FR-M07-01.09, FR-M07-01.10, BR-M07-25 |
| UC-M07-003 | scenario | SC-M07-003, SC-M07-006 | SC-M07-003/M2, SC-M07-006/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả hoàn tất; trạng thái/quyền/lựa chọn là nhánh, không BF riêng. | FR-M07-03.04, FR-M07-05, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24 |
| UC-M07-004 | scenario | SC-M07-004 | SC-M07-004/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả hoàn tất; trạng thái/quyền/lựa chọn là nhánh, không BF riêng. | FR-M07-05.05, FR-M07-05.13, FR-M07-06.01, FR-M07-06.02, FR-M07-06.04, BR-M07-14, BR-M07-27 |
| UC-M07-005 | scenario | SC-M07-005 | SC-M07-005/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả hoàn tất; trạng thái/quyền/lựa chọn là nhánh, không BF riêng. | FR-M07-06.03, FR-M07-06.05, FR-M07-06.06, BR-M07-14 |
| UC-M07-006 | scenario | SC-M07-006 | SC-M07-006/M4 | Chức năng actor chủ động yêu cầu và nhận kết quả hoàn tất; trạng thái/quyền/lựa chọn là nhánh, không BF riêng. | FR-M07-02.14, FR-M07-02.15, FR-M07-02.16, FR-M07-02.28, FR-M07-02.30, FR-M07-02.31, FR-M07-02.32, BR-M07-20 |
| UC-M07-007 | embedded | SC-M07-004, SC-M07-005 | SC-M07-004/M2, SC-M07-005/M2 | Cập nhật read đơn lẻ/tất cả được mở tại lượt kiểm quyền và thay đổi trạng thái trong hai caller; không có BF đọc cờ nội bộ. | FR-M07-05.05, FR-M07-06.01, FR-M07-06.03, FR-M07-06.04, FR-M07-06.05, FR-M07-06.06, BR-M07-14, BR-M07-27 |
| UC-M07-008 | embedded | SC-M07-007 | SC-M07-007/M2 | Đếm đúng cuộc/tin được thấy theo M16 trong chức năng kiểm tra Chat, không tạo BF chỉ chạy phép đếm. | FR-M07-07.02, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10 |
| UC-M07-009 | scenario | SC-M07-008 | SC-M07-008/M4 | Chức năng actor chủ động yêu cầu và nhận kết quả hoàn tất; trạng thái/quyền/lựa chọn là nhánh, không BF riêng. | FR-M07-08, FR-M07-02.07, FR-M07-02.08, FR-M07-02.09, BR-M07-07 |
| UC-M07-010 | scenario | SC-M07-009 | SC-M07-009/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả hoàn tất; trạng thái/quyền/lựa chọn là nhánh, không BF riêng. | FR-M07-09.01, FR-M07-09.02, FR-M07-09.05, FR-M07-09.06, FR-M07-09.07, BR-M07-08 |
| UC-M07-011 | scenario | SC-M07-010 | SC-M07-010/M2 | Chức năng actor chủ động yêu cầu và nhận kết quả hoàn tất; trạng thái/quyền/lựa chọn là nhánh, không BF riêng. | FR-M07-09.03, FR-M07-09.04, FR-M07-09.06, FR-M07-09.07, BR-M07-08 |


| SVG nguồn | Số UC | Đối chiếu |
|---|---|---|
| C-M07 | 4 | Tập ID khớp US; không vẽ lại hoặc thêm cạnh |
| D-M07-020 | 3 | Tập ID khớp US; không vẽ lại hoặc thêm cạnh |
| D-M07-021 | 6 | Tập ID khớp US; không vẽ lại hoặc thêm cạnh |
| D-M07-022 | 4 | Tập ID khớp US; không vẽ lại hoặc thêm cạnh |
| D-M07-023 | 2 | Tập ID khớp US; không vẽ lại hoặc thêm cạnh |


## 3. Luồng nghiệp vụ theo mục tiêu actor

<!-- sc:flows -->

| id | uc | primary | trigger | goal | completion | covered_ucs | rationale | scenario | sources |
|---|---|---|---|---|---|---|---|---|---|
| BF-M07-001 | UC-M07-001 | ACT-002 | Lan bấm Theo dõi trên hồ sơ Bình. | Theo dõi người dùng hoặc Topic | Quan hệ người dùng–người dùng/Topic đã được tạo với thời điểm bắt đầu. Follow người dùng chỉ phát sự kiện người theo dõi mới một lần cho mỗi cặp; Topic không sinh thông báo. Không khẳng định đẩy tới mọi thiết bị chắc chắn thành công. | UC-M07-001 | Actor yêu cầu và hoàn thành một chức năng; không tách theo loại target, trạng thái, vai trò, bật/tắt hoặc lỗi. | SC-M07-001 | FR-M07-01.01, FR-M07-01.04, FR-M07-01.11, FR-M07-01.12, FR-M07-02.01, FR-M07-02.02, FR-M07-02.25, FR-M07-03.01, FR-M07-03.02, BR-M07-15, BR-M07-24, BR-M07-25, FR-M07-02.24, FR-M07-01.10, FR-M07-01.02, FR-M07-01.03 |
| BF-M07-002 | UC-M07-002 | ACT-002 | Lan bấm Bỏ theo dõi Bình. | Bỏ theo dõi người dùng hoặc Topic | Quan hệ đang theo dõi của mình đã bị xóa, số theo dõi target giảm1; không thông báo unfollow và không xóa dấu từng báo follow hoặc thông báo cũ. | UC-M07-002 | Actor yêu cầu và hoàn thành một chức năng; không tách theo loại target, trạng thái, vai trò, bật/tắt hoặc lỗi. | SC-M07-002 | FR-M07-01.08, FR-M07-01.09, FR-M07-01.10, BR-M07-25, FR-M07-01.13, BR-M07-15, FR-M07-01.03 |
| BF-M07-003 | UC-M07-003 | ACT-002 | Lan bấm chuông thông báo. | Xem chuông và danh sách thông báo của mình | Danh sách/số chưa đọc chỉ của mình được trả đúng số lượng, thứ tự cập nhật cuối, read/unread và UTC+7. Chỉ xem không đánh dấu đọc; các thông báo đã lưu không bị xóa hay mất chỉ vì đẩy lỗi. | UC-M07-003 | Actor yêu cầu và hoàn thành một chức năng; không tách theo loại target, trạng thái, vai trò, bật/tắt hoặc lỗi. | SC-M07-003 | FR-M07-05.01, FR-M07-03.04, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24, BR-M07-02, FR-M07-03.03, FR-M07-02.03, FR-M07-02.04, FR-M07-02.18, FR-M07-02.20, BR-M07-05, FR-M07-02.26, FR-M07-05.09, FR-M07-05.06 |
| BF-M07-004 | UC-M07-004 | ACT-002 | Lan bấm N003 trong danh sách thông báo của mình. | Đọc một thông báo và mở nội dung liên quan | Thông báo đã đọc được giữ; nội dung hợp lệ hoặc đường xem lại chỉ đọc của chủ nội dung được mở đúng quyền. Không thay mốc đọc Chat hoặc thông báo khác. | UC-M07-004, UC-M07-007 | Actor yêu cầu và hoàn thành một chức năng; không tách theo loại target, trạng thái, vai trò, bật/tắt hoặc lỗi. | SC-M07-004 | FR-M07-06.01, FR-M07-06.02, FR-M07-05.05, FR-M07-05.13, FR-M07-06.04, BR-M07-14, BR-M07-27, FR-M03-07.08, FR-M03-07.09, FR-M04-06.01, FR-M04-06.04, FR-M07-05.09, FR-M07-05.06, FR-M07-06.06 |
| BF-M07-005 | UC-M07-005 | ACT-002 | Lan bấm Đánh dấu tất cả đã đọc. | Đánh dấu tất cả thông báo của mình đã đọc | Mọi thông báo chưa đọc của chính người thao tác tại phạm vi xử lý đã thành đã đọc, số unread 0 theo dữ liệu đó; Chat và dữ liệu người khác không đổi. Không cam kết đồng bộ read tức thời trên mọi thiết bị hoặc chặn sự kiện mới sau thao tác. | UC-M07-005, UC-M07-007 | Actor yêu cầu và hoàn thành một chức năng; không tách theo loại target, trạng thái, vai trò, bật/tắt hoặc lỗi. | SC-M07-005 | FR-M07-06.03, FR-M07-05.05, FR-M07-06.05, FR-M07-06.06, BR-M07-14, FR-M07-05.09 |
| BF-M07-006 | UC-M07-006 | ACT-002 | Lan mở trang Thông báo để phản hồi đề xuất R841. | Phản hồi đề xuất làm Mod hoặc Admin | Một quyết định được ghi nhận cho đề xuất còn hiệu lực: Chấp nhận đổi vai trò ngay theo loại; Từ chối giữ vai trò. Thông báo hiện lựa chọn và không cho trả lời lại; không kết thúc ở việc chỉ chuyển yêu cầu cho M10. | UC-M07-003, UC-M07-006 | Actor yêu cầu và hoàn thành một chức năng; không tách theo loại target, trạng thái, vai trò, bật/tắt hoặc lỗi. | SC-M07-006 | FR-M07-05.02, FR-M07-03.04, FR-M07-05.01, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24, FR-M07-02.14, FR-M07-02.15, FR-M07-02.16, FR-M07-02.28, FR-M07-02.30, FR-M07-02.31, FR-M07-02.32, BR-M07-20, FR-M10-03.01, FR-M10-03.02, FR-M10-03.04, FR-M10-03.10, FR-M10-03.11, FR-M10-03.03, FR-M10-07.05, FR-M10-07.06, FR-M10-03.09, FR-M10-03.06, FR-M10-02.10, FR-M10-03.08, FR-M10-02.08, FR-M10-03.07, FR-M07-05.06 |
| BF-M07-007 | UC-M07-023 | ACT-002 | Lan mở ứng dụng để kiểm tra tin nhắn mới. | Kiểm tra số cuộc trò chuyện chưa đọc và mở hộp thư | Chỉ báo đúng số cuộc có tin chưa đọc được thấy được trả, không loại cuộc mute hoặc đếm tin sau lúc rời không được thấy. Khi actor chọn mở hộp thư, điều hướng M16 đúng quyền, không tự đọc mọi cuộc hay ảnh hưởng chuông. | UC-M07-008, UC-M07-023 | Actor yêu cầu và hoàn thành một chức năng; không tách theo loại target, trạng thái, vai trò, bật/tắt hoặc lỗi. | SC-M07-007 | FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10, FR-M16-03.01, FR-M16-07.01, FR-M07-09.03 |
| BF-M07-008 | UC-M07-009 | ACT-002 | Lan mở P701 để thay cài đặt nhận thông báo cho bài này. | Bật hoặc tắt nhận thông báo tương tác theo bài | Cài đặt theo bài của mình đã được lưu/bỏ đúng lựa chọn, chỉ tác động các loại tương tác được quy định. Bật lại nhận từ lúc đó; nhắc tên/xử lý khác vẫn theo quy tắc chung, người khác và bản ghi cũ không bị thay đổi. | UC-M07-009 | Actor yêu cầu và hoàn thành một chức năng; không tách theo loại target, trạng thái, vai trò, bật/tắt hoặc lỗi. | SC-M07-008 | FR-M07-08.01, FR-M07-08.02, FR-M07-08.03, FR-M07-08.04, FR-M07-02.07, FR-M07-02.08, FR-M07-02.09, BR-M07-06, BR-M07-07, FR-M07-08.05 |
| BF-M07-009 | UC-M07-010 | ACT-002 | Lan chọn tắt thông báo C71 đang là thành viên. | Bật hoặc tắt popup riêng của một cuộc trò chuyện | Mute riêng của thành viên–cuộc được lưu/bỏ theo lựa chọn. Popup còn phụ thuộc global mute và đang xem đúng cuộc; số cuộc unread/read marker và cài đặt người khác không đổi do mute. | UC-M07-010 | Actor yêu cầu và hoàn thành một chức năng; không tách theo loại target, trạng thái, vai trò, bật/tắt hoặc lỗi. | SC-M07-009 | FR-M07-09.01, FR-M07-09.02, FR-M07-09.05, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28, FR-M07-09.03, FR-M07-09.06 |
| BF-M07-010 | UC-M07-011 | ACT-002 | Lan bật Tắt thông báo cho toàn bộ Chat. | Bật hoặc tắt popup toàn bộ Chat | Global mute được lưu theo lựa chọn. Khi bật, mọi popup Chat của mình bị chặn; khi bỏ, popup tuân cài đặt riêng đã giữ và điều kiện đang xem/đang mở. Không xóa mute riêng hoặc unread. | UC-M07-011 | Actor yêu cầu và hoàn thành một chức năng; không tách theo loại target, trạng thái, vai trò, bật/tắt hoặc lỗi. | SC-M07-010 | FR-M07-09.03, FR-M07-09.04, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28, FR-M07-09.06 |


Follow/unfollow là hai chức năng độc lập; không ép một lần follow rồi unfollow. Xem danh sách không bắt mở/mark-all/trả lời đề xuất. Phản hồi chấp nhận/từ chối là hai lựa chọn của cùng chức năng; từ chối đề xuất hợp lệ là SUCCESS của phản hồi, khác với yêu cầu bị hệ thống từ chối. Bật/tắt cùng một phạm vi cài đặt là lựa chọn trong cùng BF; cài đặt bài, từng cuộc và global có phạm vi/mục tiêu riêng.

| Quan hệ US giữ nguyên | Điểm gọi/chèn | Trở về |
|---|---|---|
| UC-M07-004 include UC-M07-007 | #uc-m07-004-main-2 | #uc-m07-004-main-3 |
| UC-M07-005 include UC-M07-007 | #uc-m07-005-main-2 | #uc-m07-005-main-3 |
| UC-M07-006 extend UC-M07-003 | EP-PROPOSAL | #uc-m07-003-main-4 |
| UC-M07-023 include UC-M07-008 | #uc-m07-023-main-2 | #uc-m07-023-main-3 |


UC004/005 include UC007 được triển khai trực tiếp ở lượt kiểm quyền/ghi read; đích mất quyền vẫn phải ghi read trước. UC023 include UC008 được mở trong lượt nhận yêu cầu và đếm tin được thấy. UC006 extend UC003 tại EP-PROPOSAL, SC006 viết cả xem đề xuất, chọn và kết quả role để trở về danh sách; không dừng ở câu gọi M10. Không tạo include giữa follow và unfollow, hoặc giữa chuông với Chat.

## 4. Scenario sáu phần

<a id="sc-m07-001"></a>

<!-- sc:scenario SC-M07-001 -->

### SC-M07-001

#### 1. Tên kịch bản chuẩn

Theo dõi người dùng hoặc Topic — BF-M07-001; owner [UC-M07-001](../../us/US-M07.md#uc-m07-001).

#### 2. Actor thực hiện

ACT-002 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-003 kế thừa quyền cá nhân User; đường E tại M1 ghi rõ dữ liệu thuộc actor đó. ACT-001 chỉ có đường từ chối. ACT-005 không tham gia chức năng actor này; email nằm ở AUT004/005.

#### 3. Tiền điều kiện

Đối tượng được nhận diện; phiên, loại đối tượng và trạng thái target được kiểm trong luồng. Đường chuẩn Lan có phiên, Bình ACTIVE, khác Lan; cặp Lan–Bình chưa có quan hệ và chưa từng có thông báo người theo dõi mới.

#### 4. Hậu điều kiện

<!-- sc:post SC-M07-001 -->

| result | condition |
|---|---|
| SUCCESS | Quan hệ người dùng–người dùng/Topic đã được tạo với thời điểm bắt đầu. Follow người dùng chỉ phát sự kiện người theo dõi mới một lần cho mỗi cặp; Topic không sinh thông báo. Không khẳng định đẩy tới mọi thiết bị chắc chắn thành công. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi nhận thao tác thành công hoặc sửa dữ liệu ngoài phạm vi của người thao tác. Những hiệu ứng riêng được nêu trong nhánh và hậu điều kiện tương ứng vẫn được giữ. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M07-001 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan bấm Theo dõi trên hồ sơ Bình. | actor=U-LAN; target=U-BINH ACTIVE; Bình có 10 người theo dõi; cặp này chưa từng được báo | M2 | FR-M07-01.01 |
| M2 | SYSTEM | Hệ thống kiểm đăng nhập, target là người dùng khác mình và không BANNED; tạo quan hệ Lan–Bình kèm thời điểm bắt đầu. Ghi nhận sự kiện người theo dõi mới lần đầu của cặp, lưu thông báo chưa đọc cho Bình theo AUT001 trước khi đẩy theo AUT003; trả quan hệ đã theo dõi cho Lan. | Quan hệ U-LAN→U-BINH, bắt đầu09/11 10:00+07; count Bình10→11; thông báo của Bình có causer Lan, không phải thông báo cho Lan; không email | END:SUCCESS | FR-M07-01.01, FR-M07-01.04, FR-M07-01.11, FR-M07-01.12, FR-M07-02.01, FR-M07-02.02, FR-M07-02.25, FR-M07-03.01, FR-M07-03.02, BR-M07-15, BR-M07-24, BR-M07-25 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã hoàn tất. Guard và dữ liệu nhánh thay snapshot chuẩn cho lần chạy này; không áp đồng thời các snapshot. Mỗi đường ghi đầy đủ bước tới terminal hoặc điểm nhập lại. E tại M1 thay toàn bộ đường khi actor khởi tạo khác, không đổi danh tính giữa chừng. Không tự thêm nút OK/hủy/retry hoặc cơ chế rollback chưa có nguồn.

<!-- sc:exceptions SC-M07-001 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Lan chọn theo dõi Topic thay người dùng | E1.1 | FR-M07-01.01, FR-M07-02.24, BR-M07-15 |
| E2 | system | M2 | Theo dõi lại Bình sau khi đã bỏ theo dõi và cặp này đã từng được báo | E2.1 | FR-M07-01.01, FR-M07-01.10, BR-M07-25 |
| E3 | system | M2 | Target là Tag | E3.1 | FR-M07-01.02, BR-M07-15 |
| E4 | system | M2 | Target là Group | E4.1 | FR-M07-01.02, BR-M07-15 |
| E5 | system | M2 | Target là bài viết | E5.1 | FR-M07-01.02, BR-M07-15 |
| E6 | system | M2 | Theo dõi chính mình | E6.1 | FR-M07-01.11, BR-M07-15 |
| E7 | system | M2 | Bắt đầu theo dõi tài khoản BANNED | E7.1 | FR-M07-01.12, BR-M07-15 |
| E8 | system | M1 | ACT-001 — Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E8.1 | FR-M07-01.03 |
| E9 | system | M1 | ACT-003 — Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M07-01.01, FR-M07-01.04, FR-M07-01.11, FR-M07-01.12, FR-M07-02.01, FR-M07-02.02, FR-M07-02.25, FR-M07-03.01, FR-M07-03.02, BR-M07-15, BR-M07-24, BR-M07-25 |


<!-- sc:branch SC-M07-001 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Lan bấm Theo dõi Topic Toán học. | Topic T71 còn trong danh mục; Lan chưa theo dõi; Topic có 20 người theo dõi | E1.2 | FR-M07-01.01 |
| E1.2 | SYSTEM | Hệ thống kiểm phiên và loại Topic, tạo quan hệ cùng mốc bắt đầu rồi trả đã theo dõi. Không tạo thông báo follow Topic hoặc thông báo khi Topic có bài mới; quan hệ phục vụ Following/lọc theo owner. | U-LAN→T71, 09/11 10:00+07; count 20→21; không thông báo và không email | END:SUCCESS | FR-M07-01.01, FR-M07-02.24, BR-M07-15 |


<!-- sc:branch SC-M07-001 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống kiểm điều kiện hiện tại, tạo lại quan hệ Lan–Bình với mốc bắt đầu của lần này và trả đã theo dõi; không tạo lại sự kiện/thông báo người theo dõi mới. | Quan hệ trước lần này không tồn tại; dấu đã từng báo cặp được giữ; count 10→11; mốc mới09/11 10:00+07 | END:SUCCESS | FR-M07-01.01, FR-M07-01.10, BR-M07-25 |


<!-- sc:branch SC-M07-001 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối tạo quan hệ theo dõi cho yêu cầu bị cấm; không tăng số theo dõi hoặc tạo sự kiện follow. | target=#bayes | END:REJECTED | FR-M07-01.02, BR-M07-15 |


<!-- sc:branch SC-M07-001 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối tạo quan hệ theo dõi cho yêu cầu bị cấm; không tăng số theo dõi hoặc tạo sự kiện follow. | target=G71 | END:REJECTED | FR-M07-01.02, BR-M07-15 |


<!-- sc:branch SC-M07-001 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối tạo quan hệ theo dõi cho yêu cầu bị cấm; không tăng số theo dõi hoặc tạo sự kiện follow. | target=P701 | END:REJECTED | FR-M07-01.02, BR-M07-15 |


<!-- sc:branch SC-M07-001 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối tạo quan hệ theo dõi cho yêu cầu bị cấm; không tăng số theo dõi hoặc tạo sự kiện follow. | target=U-LAN | END:REJECTED | FR-M07-01.11, BR-M07-15 |


<!-- sc:branch SC-M07-001 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối tạo quan hệ theo dõi cho yêu cầu bị cấm; không tăng số theo dõi hoặc tạo sự kiện follow. | target=U-BINH BANNED | END:REJECTED | FR-M07-01.12, BR-M07-15 |


**E8 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-001 E8 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E8.1 | ACT-001 | Guest yêu cầu theo dõi người dùng hoặc topic. | Chưa có phiên, không mượn dữ liệu/cài đặt của Lan | E8.2 | FR-M07-01.03 |
| E8.2 | SYSTEM | Hệ thống từ chối thao tác cần phiên và yêu cầu đăng nhập; không tự đăng nhập hoặc sửa dữ liệu. | Không có kết quả cá nhân hoặc thay đổi từ yêu cầu Guest | END:REJECTED | FR-M07-01.03 |


**E9 — thay toàn bộ M1 đến kết thúc:** Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-001 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-003 | Mod Mai bấm Theo dõi trên hồ sơ Bình. | actor=U-MAI; target=U-BINH ACTIVE; Bình có 10 người theo dõi; cặp này chưa từng được báo | E9.2 | FR-M07-01.01 |
| E9.2 | SYSTEM | Hệ thống kiểm đăng nhập, target là người dùng khác mình và không BANNED; tạo quan hệ Mod Mai–Bình kèm thời điểm bắt đầu. Ghi nhận sự kiện người theo dõi mới lần đầu của cặp, lưu thông báo chưa đọc cho Bình theo AUT001 trước khi đẩy theo AUT003; trả quan hệ đã theo dõi cho Mod Mai. | Quan hệ U-MAI→U-BINH, bắt đầu09/11 10:00+07; count Bình10→11; thông báo của Bình có causer Mod Mai, không phải thông báo cho Mod Mai; không email | END:SUCCESS | FR-M07-01.01, FR-M07-01.04, FR-M07-01.11, FR-M07-01.12, FR-M07-02.01, FR-M07-02.02, FR-M07-02.25, FR-M07-03.01, FR-M07-03.02, BR-M07-15, BR-M07-24, BR-M07-25 |


<!-- sc:end SC-M07-001 -->

<a id="sc-m07-002"></a>

<!-- sc:scenario SC-M07-002 -->

### SC-M07-002

#### 1. Tên kịch bản chuẩn

Bỏ theo dõi người dùng hoặc Topic — BF-M07-002; owner [UC-M07-002](../../us/US-M07.md#uc-m07-002).

#### 2. Actor thực hiện

ACT-002 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-003 kế thừa quyền cá nhân User; đường E tại M1 ghi rõ dữ liệu thuộc actor đó. ACT-001 chỉ có đường từ chối. ACT-005 không tham gia chức năng actor này; email nằm ở AUT004/005.

#### 3. Tiền điều kiện

Có quan hệ đang theo dõi của chính người thao tác; kiểm phiên trong luồng. Đường chuẩn U-LAN→U-BINH đang tồn tại, Bình có 11 người theo dõi; dấu cặp đã từng nhận thông báo follow được giữ.

#### 4. Hậu điều kiện

<!-- sc:post SC-M07-002 -->

| result | condition |
|---|---|
| SUCCESS | Quan hệ đang theo dõi của mình đã bị xóa, số theo dõi target giảm1; không thông báo unfollow và không xóa dấu từng báo follow hoặc thông báo cũ. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi nhận thao tác thành công hoặc sửa dữ liệu ngoài phạm vi của người thao tác. Những hiệu ứng riêng được nêu trong nhánh và hậu điều kiện tương ứng vẫn được giữ. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M07-002 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan bấm Bỏ theo dõi Bình. | Quan hệ U-LAN→U-BINH đang tồn tại; Bình ACTIVE | M2 | FR-M07-01.08 |
| M2 | SYSTEM | Hệ thống kiểm phiên và quan hệ của Lan, xóa quan hệ này, giảm số người theo dõi Bình một đơn vị và trả đã bỏ theo dõi. Không tạo thông báo cho ai; giữ dấu đã từng báo follow để lần theo dõi lại không phát lặp. | U-LAN→U-BINH không còn; count 11→10; không xóa thông báo follow đã lưu trước đây | END:SUCCESS | FR-M07-01.08, FR-M07-01.09, FR-M07-01.10, BR-M07-25 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã hoàn tất. Guard và dữ liệu nhánh thay snapshot chuẩn cho lần chạy này; không áp đồng thời các snapshot. Mỗi đường ghi đầy đủ bước tới terminal hoặc điểm nhập lại. E tại M1 thay toàn bộ đường khi actor khởi tạo khác, không đổi danh tính giữa chừng. Không tự thêm nút OK/hủy/retry hoặc cơ chế rollback chưa có nguồn.

<!-- sc:exceptions SC-M07-002 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Lan bỏ theo dõi Topic đang theo dõi | E1.1 | FR-M07-01.08, FR-M07-01.09, BR-M07-25 |
| E2 | system | M2 | Target đã chuyển BANNED nhưng quan hệ cũ vẫn còn | E2.1 | FR-M07-01.08, FR-M07-01.09, FR-M07-01.13, BR-M07-15, BR-M07-25 |
| E3 | system | M2 | Target đã chuyển DEACTIVATED nhưng quan hệ cũ vẫn còn | E3.1 | FR-M07-01.08, FR-M07-01.09, FR-M07-01.13, BR-M07-15, BR-M07-25 |
| E4 | system | M1 | ACT-001 — Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M07-01.03 |
| E5 | system | M1 | ACT-003 — Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M07-01.08, FR-M07-01.09, FR-M07-01.10, BR-M07-25 |


<!-- sc:branch SC-M07-002 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Lan bấm Bỏ theo dõi Topic Toán học. | U-LAN→T71 tồn tại; count 21 | E1.2 | FR-M07-01.08 |
| E1.2 | SYSTEM | Hệ thống kiểm phiên/quyền quan hệ, xóa U-LAN→T71 và trả đã bỏ theo dõi; không tạo thông báo. | Topic count 21→20; không thay quan hệ của người khác | END:SUCCESS | FR-M07-01.08, FR-M07-01.09, BR-M07-25 |


<!-- sc:branch SC-M07-002 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống không coi trạng thái target là đã tự xóa follow; kiểm quan hệ hiện có của Lan rồi thực hiện yêu cầu bỏ theo dõi và giảm count. Không phát thông báo. | U-BINH=BANNED; quan hệ cũ có thật, count 11→10; không thêm lệnh cấm unfollow như lệnh cấm bắt đầu follow BANNED | END:SUCCESS | FR-M07-01.08, FR-M07-01.09, FR-M07-01.13, BR-M07-15, BR-M07-25 |


<!-- sc:branch SC-M07-002 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống không coi trạng thái target là đã tự xóa follow; kiểm quan hệ hiện có của Lan rồi thực hiện yêu cầu bỏ theo dõi và giảm count. Không phát thông báo. | U-BINH=DEACTIVATED; quan hệ cũ có thật, count 11→10; không thêm lệnh cấm unfollow như lệnh cấm bắt đầu follow BANNED | END:SUCCESS | FR-M07-01.08, FR-M07-01.09, FR-M07-01.13, BR-M07-15, BR-M07-25 |


**E4 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-002 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-001 | Guest yêu cầu bỏ theo dõi người dùng hoặc topic. | Chưa có phiên, không mượn dữ liệu/cài đặt của Lan | E4.2 | FR-M07-01.03 |
| E4.2 | SYSTEM | Hệ thống từ chối thao tác cần phiên và yêu cầu đăng nhập; không tự đăng nhập hoặc sửa dữ liệu. | Không có kết quả cá nhân hoặc thay đổi từ yêu cầu Guest | END:REJECTED | FR-M07-01.03 |


**E5 — thay toàn bộ M1 đến kết thúc:** Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-002 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-003 | Mod Mai bấm Bỏ theo dõi Bình. | Quan hệ U-MAI→U-BINH đang tồn tại; Bình ACTIVE | E5.2 | FR-M07-01.08 |
| E5.2 | SYSTEM | Hệ thống kiểm phiên và quan hệ của Mod Mai, xóa quan hệ này, giảm số người theo dõi Bình một đơn vị và trả đã bỏ theo dõi. Không tạo thông báo cho ai; giữ dấu đã từng báo follow để lần theo dõi lại không phát lặp. | U-MAI→U-BINH không còn; count 11→10; không xóa thông báo follow đã lưu trước đây | END:SUCCESS | FR-M07-01.08, FR-M07-01.09, FR-M07-01.10, BR-M07-25 |


<!-- sc:end SC-M07-002 -->

<a id="sc-m07-003"></a>

<!-- sc:scenario SC-M07-003 -->

### SC-M07-003

#### 1. Tên kịch bản chuẩn

Xem chuông và danh sách thông báo của mình — BF-M07-003; owner [UC-M07-003](../../us/US-M07.md#uc-m07-003).

#### 2. Actor thực hiện

ACT-002 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-003 kế thừa quyền cá nhân User; đường E tại M1 ghi rõ dữ liệu thuộc actor đó. ACT-001 chỉ có đường từ chối. ACT-005 không tham gia chức năng actor này; email nằm ở AUT004/005.

#### 3. Tiền điều kiện

Có yêu cầu đọc danh sách; phiên/trạng thái tài khoản được kiểm, không giả định mọi người đều được xem. Đường chuẩn Lan ACTIVE có phiên, bộ D-NOT55 đã lưu; số cuộc Chat theo D-CHAT độc lập.

#### 4. Hậu điều kiện

<!-- sc:post SC-M07-003 -->

| result | condition |
|---|---|
| SUCCESS | Danh sách/số chưa đọc chỉ của mình được trả đúng số lượng, thứ tự cập nhật cuối, read/unread và UTC+7. Chỉ xem không đánh dấu đọc; các thông báo đã lưu không bị xóa hay mất chỉ vì đẩy lỗi. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi nhận thao tác thành công hoặc sửa dữ liệu ngoài phạm vi của người thao tác. Những hiệu ứng riêng được nêu trong nhánh và hậu điều kiện tương ứng vẫn được giữ. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M07-003 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan bấm chuông thông báo. | D-NOT: N001…N055 đều thuộc Lan/U-LAN, cập nhật cuối của N thứ i là T−i phút, T=09/11/2026 10:00+07. N001, N003, N011 chưa đọc; 52 bản còn lại đã đọc. N001: upvote bài P701; N003: trả lời bình luận C701 trong P701; N011: nhắc tên. Các đích chuẩn còn tồn tại và Lan được xem; không có bản ghi Chat trong tập này. | M2 | FR-M07-05.01 |
| M2 | SYSTEM | Hệ thống kiểm phiên và tài khoản không BANNED, tải thông báo của Lan từ nguồn đã lưu dù đẩy trước đó có lỗi. Trả10 mục gần nhất theo lần cập nhật cuối, nhãn read/unread, giờ Việt Nam và số chưa đọc của toàn tập; chỉ mở chuông nên không đánh dấu đọc. | Hiện N001…N010; chuông=3 (gồm N011 ngoài 10 mục); N001/N003/N011 vẫn chưa đọc; Chat=3 cuộc, không cộng vào chuông | END:SUCCESS | FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã hoàn tất. Guard và dữ liệu nhánh thay snapshot chuẩn cho lần chạy này; không áp đồng thời các snapshot. Mỗi đường ghi đầy đủ bước tới terminal hoặc điểm nhập lại. E tại M1 thay toàn bộ đường khi actor khởi tạo khác, không đổi danh tính giữa chừng. Không tự thêm nút OK/hủy/retry hoặc cơ chế rollback chưa có nguồn.

<!-- sc:exceptions SC-M07-003 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Xem trang Thông báo và tải tới thông báo cũ nhất | E1.1 | FR-M07-05.02, FR-M07-03.04, FR-M07-05.01, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24 |
| E2 | system | M2 | Chưa có thông báo được lưu | E2.1 | FR-M07-05.01, FR-M07-05.02, FR-M07-05.05, FR-M07-05.10, BR-M07-02, BR-M07-12 |
| E3 | system | M2 | Đẩy trước đó tới thiết bị hiện tại đã thất bại | E3.1 | FR-M07-03.03, FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24 |
| E4 | system | M2 | Người gây N001 chuyển DEACTIVATED | E4.1 | FR-M07-05.12, BR-M07-24, FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22 |
| E5 | system | M2 | Người gây N001 chuyển DELETED | E5.1 | FR-M07-05.12, BR-M07-24, FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22 |
| E6 | system | M2 | Thông báo upvote đã đọc được gộp thêm trong cửa sổ5 phút | E6.1 | FR-M07-02.03, FR-M07-02.04, FR-M07-02.18, FR-M07-02.20, FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24, BR-M07-05 |
| E7 | system | M2 | Lan ACTIVE trở lại sau thời gian DEACTIVATED hoặc BANNED | E7.1 | FR-M07-02.26, FR-M07-05.05, FR-M07-05.09, FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24 |
| E8 | system | M2 | Người yêu cầu đang BANNED | E8.1 | FR-M07-05.09, FR-M07-02.26, BR-M07-24 |
| E9 | system | M1 | ACT-001 — Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M07-05.06 |
| E10 | system | M1 | ACT-003 — Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M07-05.01, FR-M07-03.04, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24 |


<!-- sc:branch SC-M07-003 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Lan mở trang Thông báo để xem toàn bộ. | D-NOT: N001…N055 đều thuộc Lan/U-LAN, cập nhật cuối của N thứ i là T−i phút, T=09/11/2026 10:00+07. N001, N003, N011 chưa đọc; 52 bản còn lại đã đọc. N001: upvote bài P701; N003: trả lời bình luận C701 trong P701; N011: nhắc tên. Các đích chuẩn còn tồn tại và Lan được xem; không có bản ghi Chat trong tập này. | E1.2 | FR-M07-05.02 |
| E1.2 | SYSTEM | Hệ thống kiểm quyền và tải 20 mục đầu từ dữ liệu của Lan, mới nhất theo cập nhật cuối; hiện trạng thái/giờ, không tự đánh dấu đã đọc. | N001…N020; 20/55; chưa đọc3; Chat 3 | E1.3 | FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24 |
| E1.3 | ACT-002 | Lan cuộn tới cuối phần thông báo đã tải. | Đã tải 20/55, không bấm một thông báo | E1.4 | FR-M07-05.02 |
| E1.4 | SYSTEM | Hệ thống tiếp tục trả tối đa20 thông báo kế tiếp của Lan tới mục cũ nhất; giữ toàn bộ bản ghi và trạng thái đọc. | N021…N040; tổng 40/55; chưa đọc3; còn 15 mục | E1.5 | FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, BR-M07-12, BR-M07-13, BR-M07-22 |
| E1.5 | ACT-002 | Lan cuộn tới cuối phần thông báo đã tải. | Đã tải 40/55, không bấm một thông báo | E1.6 | FR-M07-05.02 |
| E1.6 | SYSTEM | Hệ thống tiếp tục trả tối đa20 thông báo kế tiếp của Lan tới mục cũ nhất; giữ toàn bộ bản ghi và trạng thái đọc. | N041…N055; tổng 55/55; chưa đọc3; lô cuối15 | END:SUCCESS | FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, BR-M07-12, BR-M07-13, BR-M07-22 |


<!-- sc:branch SC-M07-003 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống trả danh sách rỗng và số chưa đọc0, không tạo thông báo giả hoặc đưa tin Chat vào để lấp. | notifications=[]; chuông 0; Chat vẫn3 theo D-CHAT | END:SUCCESS | FR-M07-05.01, FR-M07-05.02, FR-M07-05.05, FR-M07-05.10, BR-M07-02, BR-M07-12 |


<!-- sc:branch SC-M07-003 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống tải từ bản ghi đã lưu và trả10 mục D-NOT gần nhất cùng số chưa đọc; không đẩy lại như retry email và không coi push lỗi là mất thông báo. | N001…N010; chưa đọc3; bản ghi nguồn vẫn55; thiết bị khác không có bản ghi riêng cho cùng người nhận | END:SUCCESS | FR-M07-03.03, FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24 |


<!-- sc:branch SC-M07-003 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống trả danh sách của Lan, thay tên causer theo trạng thái hiện tại, không xóa thông báo hoặc đồng nhất causer với người nhận. | N001 hiện tên “Tài khoản tạm thời vô hiệu hoá”; giữ 55 bản và unread 3; Lan vẫn ACTIVE | END:SUCCESS | FR-M07-05.12, BR-M07-24, FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22 |


<!-- sc:branch SC-M07-003 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống trả danh sách của Lan, thay tên causer theo trạng thái hiện tại, không xóa thông báo hoặc đồng nhất causer với người nhận. | N001 hiện tên “[Người dùng đã xóa]”; giữ 55 bản và unread 3; Lan vẫn ACTIVE | END:SUCCESS | FR-M07-05.12, BR-M07-24, FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22 |


<!-- sc:branch SC-M07-003 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống đọc trạng thái mới đã lưu sau AUT002: đưa thông báo gộp lên đầu theo cập nhật cuối, hiện causer mới nhất và số người khác nhau, unread lại. Không khẳng định có đẩy lại mọi cập nhật gộp. | Snapshot riêng: N900 tạo10:00, đã đọc; 10:02 thêm người mới→N900 unread, lên đầu; trước unread 3, sau4; cửa sổ vẫn hết10:05 | END:SUCCESS | FR-M07-02.03, FR-M07-02.04, FR-M07-02.18, FR-M07-02.20, FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24, BR-M07-05 |


<!-- sc:branch SC-M07-003 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống kiểm trạng thái ACTIVE hiện tại rồi trả những thông báo của Lan đã được lưu cả trong thời gian bị hạn chế; không tạo lại bản sao chỉ vì tài khoản hoạt động trở lại. | N901 phát khi Lan DEACTIVATED, N902 phát khi BANNED, đều đã lưu; hiện lại theo thứ tự cập nhật thực tế và trạng thái đã lưu | END:SUCCESS | FR-M07-02.26, FR-M07-05.05, FR-M07-05.09, FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24 |


<!-- sc:branch SC-M07-003 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống không cho xem chuông/trang Thông báo; các bản ghi được tạo và giữ theo quy tắc người nhận, không xóa do bị từ chối xem. | Lan BANNED; D-NOT vẫn lưu | END:REJECTED | FR-M07-05.09, FR-M07-02.26, BR-M07-24 |


**E9 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-003 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-001 | Guest yêu cầu xem chuông và danh sách thông báo của mình. | Chưa có phiên, không mượn dữ liệu/cài đặt của Lan | E9.2 | FR-M07-05.06 |
| E9.2 | SYSTEM | Hệ thống từ chối thao tác cần phiên và yêu cầu đăng nhập; không tự đăng nhập hoặc sửa dữ liệu. | Không có kết quả cá nhân hoặc thay đổi từ yêu cầu Guest | END:REJECTED | FR-M07-05.06 |


**E10 — thay toàn bộ M1 đến kết thúc:** Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-003 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-003 | Mod Mai bấm chuông thông báo. | D-NOT: N001…N055 đều thuộc Mod Mai/U-MAI, cập nhật cuối của N thứ i là T−i phút, T=09/11/2026 10:00+07. N001, N003, N011 chưa đọc; 52 bản còn lại đã đọc. N001: upvote bài P701; N003: trả lời bình luận C701 trong P701; N011: nhắc tên. Các đích chuẩn còn tồn tại và Mod Mai được xem; không có bản ghi Chat trong tập này. | E10.2 | FR-M07-05.01 |
| E10.2 | SYSTEM | Hệ thống kiểm phiên và tài khoản không BANNED, tải thông báo của Mod Mai từ nguồn đã lưu dù đẩy trước đó có lỗi. Trả10 mục gần nhất theo lần cập nhật cuối, nhãn read/unread, giờ Việt Nam và số chưa đọc của toàn tập; chỉ mở chuông nên không đánh dấu đọc. | Hiện N001…N010; chuông=3 (gồm N011 ngoài 10 mục); N001/N003/N011 vẫn chưa đọc; Chat=3 cuộc, không cộng vào chuông | END:SUCCESS | FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24 |


<!-- sc:end SC-M07-003 -->

<a id="sc-m07-004"></a>

<!-- sc:scenario SC-M07-004 -->

### SC-M07-004

#### 1. Tên kịch bản chuẩn

Đọc một thông báo và mở nội dung liên quan — BF-M07-004; owner [UC-M07-004](../../us/US-M07.md#uc-m07-004).

#### 2. Actor thực hiện

ACT-002 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-003 kế thừa quyền cá nhân User; đường E tại M1 ghi rõ dữ liệu thuộc actor đó. ACT-001 chỉ có đường từ chối. ACT-005 không tham gia chức năng actor này; email nằm ở AUT004/005.

#### 3. Tiền điều kiện

Lan có ngữ cảnh một thông báo; kiểm quyền sở hữu/phiên trước thay đổi. Đường chuẩn N003 thuộc Lan, chưa đọc, liên quan C701/P701 ngoài nhóm, đích còn tồn tại và Lan được xem; D-NOT unread 3.

#### 4. Hậu điều kiện

<!-- sc:post SC-M07-004 -->

| result | condition |
|---|---|
| SUCCESS | Thông báo đã đọc được giữ; nội dung hợp lệ hoặc đường xem lại chỉ đọc của chủ nội dung được mở đúng quyền. Không thay mốc đọc Chat hoặc thông báo khác. |
| REJECTED | Nếu phiên/quyền thông báo không hợp lệ: không sửa bản ghi. Nếu đã kiểm đúng thông báo của mình nhưng đích xóa/ẩn/mất quyền: thông báo vẫn chuyển/giữ đã đọc và được giữ, hiện “Nội dung không tồn tại”; chỉ việc mở đích bị từ chối, không rollback trạng thái đọc. Không cấp quyền xem nội dung. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M07-004 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan bấm N003 trong danh sách thông báo của mình. | N003 unread; target=C701 trong P701; unread tổng 3 | M2 | FR-M07-06.01, FR-M07-06.02 |
| M2 | SYSTEM | Hệ thống kiểm phiên/quyền thông báo của Lan, chuyển N003 thành đã đọc rồi kiểm đích/quyền hiện tại và đưa Lan tới C701/P701 được phép xem. Giữ bản ghi thông báo và trạng thái đọc của Chat. | N003 read; chuông 3→2; bản ghi vẫn55; Chat vẫn3 cuộc; không tự đánh dấu thông báo khác | END:SUCCESS | FR-M07-05.05, FR-M07-05.13, FR-M07-06.01, FR-M07-06.02, FR-M07-06.04, BR-M07-14, BR-M07-27 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã hoàn tất. Guard và dữ liệu nhánh thay snapshot chuẩn cho lần chạy này; không áp đồng thời các snapshot. Mỗi đường ghi đầy đủ bước tới terminal hoặc điểm nhập lại. E tại M1 thay toàn bộ đường khi actor khởi tạo khác, không đổi danh tính giữa chừng. Không tự thêm nút OK/hủy/retry hoặc cơ chế rollback chưa có nguồn.

<!-- sc:exceptions SC-M07-004 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | N003 vốn đã đọc | E1.1 | FR-M07-06.02, FR-M07-06.04, FR-M07-05.05, BR-M07-14 |
| E2 | system | M2 | Đích không khả dụng: nội dung đã bị xóa | E2.1 | FR-M07-05.13, FR-M07-06.01, BR-M07-27 |
| E3 | system | M2 | Đích không khả dụng: nội dung bị ẩn, người mở không thuộc ngoại lệ chủ nội dung | E3.1 | FR-M07-05.13, FR-M07-06.01, BR-M07-27 |
| E4 | system | M2 | Đích không khả dụng: Lan rời nhóm Private nên không còn quyền xem đích | E4.1 | FR-M07-05.13, FR-M07-06.01, BR-M07-27 |
| E5 | user-choice | M1 | Chủ bài mở thông báo kết quả xử lý về bài đã xóa hẳn của mình | E5.1 | FR-M07-06.01, FR-M07-06.02, FR-M07-05.13, FR-M07-05.05, FR-M07-06.04, BR-M07-14, BR-M07-27, FR-M03-07.08, FR-M03-07.09 |
| E6 | user-choice | M1 | Tác giả mở thông báo bình luận của mình bị ẩn | E6.1 | FR-M07-05.13, FR-M07-06.01, FR-M07-06.02, FR-M07-05.05, FR-M07-06.04, BR-M07-14, BR-M07-27, FR-M04-06.01, FR-M04-06.04 |
| E7 | system | M2 | Yêu cầu trỏ thông báo của người khác | E7.1 | FR-M07-05.05 |
| E8 | system | M2 | Lan đang BANNED | E8.1 | FR-M07-05.09 |
| E9 | system | M1 | ACT-001 — Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E9.1 | FR-M07-05.06, FR-M07-06.06 |
| E10 | system | M1 | ACT-003 — Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E10.1 | FR-M07-06.01, FR-M07-06.02, FR-M07-05.05, FR-M07-05.13, FR-M07-06.04, BR-M07-14, BR-M07-27 |


<!-- sc:branch SC-M07-004 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống giữ N003 đã đọc, kiểm đích/quyền và mở C701/P701 hợp lệ; không giảm số chưa đọc thêm một lần. | N003 read trước/sau; snapshot unread 2→2; Chat 3 | END:SUCCESS | FR-M07-06.02, FR-M07-06.04, FR-M07-05.05, BR-M07-14 |


<!-- sc:branch SC-M07-004 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống xác nhận N003 của Lan, đánh dấu đã đọc trước; đích không được mở nên hiện “Nội dung không tồn tại”. Giữ thông báo và không sửa read marker Chat. | N003 unread→read; chuông 3→2; bản ghi vẫn55; nguyên nhân=nội dung đã bị xóa | END:REJECTED | FR-M07-05.13, FR-M07-06.01, BR-M07-27 |


<!-- sc:branch SC-M07-004 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống xác nhận N003 của Lan, đánh dấu đã đọc trước; đích không được mở nên hiện “Nội dung không tồn tại”. Giữ thông báo và không sửa read marker Chat. | N003 unread→read; chuông 3→2; bản ghi vẫn55; nguyên nhân=nội dung bị ẩn, người mở không thuộc ngoại lệ chủ nội dung | END:REJECTED | FR-M07-05.13, FR-M07-06.01, BR-M07-27 |


<!-- sc:branch SC-M07-004 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống xác nhận N003 của Lan, đánh dấu đã đọc trước; đích không được mở nên hiện “Nội dung không tồn tại”. Giữ thông báo và không sửa read marker Chat. | N003 unread→read; chuông 3→2; bản ghi vẫn55; nguyên nhân=Lan rời nhóm Private nên không còn quyền xem đích | END:REJECTED | FR-M07-05.13, FR-M07-06.01, BR-M07-27 |


<!-- sc:branch SC-M07-004 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-002 | Lan mở thông báo kết quả báo cáo về P702 của chính Lan. | N910 của Lan unread; P702 đã xóa hẳn, ngoài nhóm; đây là đường xem lại được M03 cho phép | E5.2 | FR-M07-06.01, FR-M07-06.02, FR-M07-05.13 |
| E5.2 | SYSTEM | Hệ thống đánh dấu N910 đã đọc, thực hiện đường xem lại M03: trả nội dung P702 ở chế độ chỉ đọc, không cho khôi phục/sửa qua đường này và không lộ người báo cáo. Không dùng thông báo để công khai bài cho người khác. | N910 read; P702 chỉ đọc; không khẳng định bài được phục hồi | END:SUCCESS | FR-M07-05.05, FR-M07-05.13, FR-M07-06.01, FR-M07-06.02, FR-M07-06.04, BR-M07-14, BR-M07-27, FR-M03-07.08, FR-M03-07.09 |


<!-- sc:branch SC-M07-004 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-002 | Lan mở thông báo “Bình luận của bạn đã bị ẩn”. | N911 unread của Lan; C702 Bị ẩn, Lan là tác giả | E6.2 | FR-M07-05.13, FR-M07-06.01, FR-M07-06.02 |
| E6.2 | SYSTEM | Hệ thống đánh dấu N911 đã đọc, trả nội dung C702 chỉ đọc kèm nhãn cho biết bình luận đang bị ẩn theo M04; không gỡ ẩn/sửa/xóa hoặc tạo khiếu nại bình luận riêng. | N911 read; C702 vẫn Bị ẩn; không tiết lộ thông tin người báo cáo | END:SUCCESS | FR-M07-05.05, FR-M07-05.13, FR-M07-06.01, FR-M07-06.02, FR-M07-06.04, BR-M07-14, BR-M07-27, FR-M04-06.01, FR-M04-06.04 |


<!-- sc:branch SC-M07-004 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối đọc/cập nhật/chuyển đích từ bản ghi không thuộc Lan; không dùng ID trực tiếp để vượt quyền. | N003 trong snapshot nhánh thuộc Bình; trạng thái của Bình không đổi | END:REJECTED | FR-M07-05.05 |


<!-- sc:branch SC-M07-004 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống từ chối truy cập thông báo, không cập nhật read bằng đường trực tiếp khi tài khoản không được xem. | Lan BANNED; N003 của Lan chưa đọc vẫn giữ | END:REJECTED | FR-M07-05.09 |


**E9 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-004 E9 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E9.1 | ACT-001 | Guest yêu cầu đọc một thông báo và mở nội dung liên quan. | Chưa có phiên, không mượn dữ liệu/cài đặt của Lan | E9.2 | FR-M07-05.06, FR-M07-06.06 |
| E9.2 | SYSTEM | Hệ thống từ chối thao tác cần phiên và yêu cầu đăng nhập; không tự đăng nhập hoặc sửa dữ liệu. | Không có kết quả cá nhân hoặc thay đổi từ yêu cầu Guest | END:REJECTED | FR-M07-05.06, FR-M07-06.06 |


**E10 — thay toàn bộ M1 đến kết thúc:** Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-004 E10 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E10.1 | ACT-003 | Mod Mai bấm N003 trong danh sách thông báo của mình. | N003 unread; target=C701 trong P701; unread tổng 3 | E10.2 | FR-M07-06.01, FR-M07-06.02 |
| E10.2 | SYSTEM | Hệ thống kiểm phiên/quyền thông báo của Mod Mai, chuyển N003 thành đã đọc rồi kiểm đích/quyền hiện tại và đưa Mod Mai tới C701/P701 được phép xem. Giữ bản ghi thông báo và trạng thái đọc của Chat. | N003 read; chuông 3→2; bản ghi vẫn55; Chat vẫn3 cuộc; không tự đánh dấu thông báo khác | END:SUCCESS | FR-M07-05.05, FR-M07-05.13, FR-M07-06.01, FR-M07-06.02, FR-M07-06.04, BR-M07-14, BR-M07-27 |


<!-- sc:end SC-M07-004 -->

<a id="sc-m07-005"></a>

<!-- sc:scenario SC-M07-005 -->

### SC-M07-005

#### 1. Tên kịch bản chuẩn

Đánh dấu tất cả thông báo của mình đã đọc — BF-M07-005; owner [UC-M07-005](../../us/US-M07.md#uc-m07-005).

#### 2. Actor thực hiện

ACT-002 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-003 kế thừa quyền cá nhân User; đường E tại M1 ghi rõ dữ liệu thuộc actor đó. ACT-001 chỉ có đường từ chối. ACT-005 không tham gia chức năng actor này; email nằm ở AUT004/005.

#### 3. Tiền điều kiện

Có ngữ cảnh người thao tác; không yêu cầu đã tải toàn bộ bản ghi hoặc phải có unread. Đường chuẩn Lan có phiên, ACTIVE; D-NOT55 có 3 unread, trong đó N011 ngoài 10 mục chuông; D-CHAT có 3 cuộc unread.

#### 4. Hậu điều kiện

<!-- sc:post SC-M07-005 -->

| result | condition |
|---|---|
| SUCCESS | Mọi thông báo chưa đọc của chính người thao tác tại phạm vi xử lý đã thành đã đọc, số unread 0 theo dữ liệu đó; Chat và dữ liệu người khác không đổi. Không cam kết đồng bộ read tức thời trên mọi thiết bị hoặc chặn sự kiện mới sau thao tác. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi nhận thao tác thành công hoặc sửa dữ liệu ngoài phạm vi của người thao tác. Những hiệu ứng riêng được nêu trong nhánh và hậu điều kiện tương ứng vẫn được giữ. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M07-005 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan bấm Đánh dấu tất cả đã đọc. | Người thao tác U-LAN; D-NOT55; chỉ đang thấy10 mục chuông | M2 | FR-M07-06.03 |
| M2 | SYSTEM | Hệ thống kiểm phiên và phạm vi dữ liệu của Lan; chuyển mọi thông báo chưa đọc của Lan thành đã đọc kể cả ngoài phần đang hiển thị, giữ các bản vốn đã đọc. Trả chuông 0 và giữ mốc đọc/số cuộc Chat, không xóa thông báo. | N001, N003, N011 đều read; unread 3→0; vẫn55 bản; thông báo Bình không đổi; Chat 3 cuộc/8 tin được thấy chưa đọc giữ nguyên | END:SUCCESS | FR-M07-05.05, FR-M07-06.03, FR-M07-06.05, FR-M07-06.06, BR-M07-14 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã hoàn tất. Guard và dữ liệu nhánh thay snapshot chuẩn cho lần chạy này; không áp đồng thời các snapshot. Mỗi đường ghi đầy đủ bước tới terminal hoặc điểm nhập lại. E tại M1 thay toàn bộ đường khi actor khởi tạo khác, không đổi danh tính giữa chừng. Không tự thêm nút OK/hủy/retry hoặc cơ chế rollback chưa có nguồn.

<!-- sc:exceptions SC-M07-005 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Tập thông báo đã đọc hết hoặc rỗng | E1.1 | FR-M07-06.03, FR-M07-06.05, FR-M07-05.05, BR-M07-14 |
| E2 | system | M2 | Yêu cầu muốn đánh dấu dữ liệu của người khác | E2.1 | FR-M07-05.05 |
| E3 | system | M2 | Tài khoản không được truy cập thông báo vì BANNED | E3.1 | FR-M07-05.09, FR-M07-06.06 |
| E4 | system | M1 | ACT-001 — Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E4.1 | FR-M07-06.06 |
| E5 | system | M1 | ACT-003 — Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M07-06.03, FR-M07-05.05, FR-M07-06.05, FR-M07-06.06, BR-M07-14 |


<!-- sc:branch SC-M07-005 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống xác nhận người thao tác, giữ tập read/rỗng và trả unread 0, không phát sinh thay đổi Chat hoặc bản ghi thông báo mới. | notifications=[] hoặc55 bản đều read; unread 0→0; Chat 3 | END:SUCCESS | FR-M07-06.03, FR-M07-06.05, FR-M07-05.05, BR-M07-14 |


<!-- sc:branch SC-M07-005 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống chỉ cho thao tác phạm vi của chính Lan, từ chối yêu cầu chỉ định toàn bộ thông báo của Bình. | target recipient=U-BINH; read/unread của Bình không đổi | END:REJECTED | FR-M07-05.05 |


<!-- sc:branch SC-M07-005 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống áp quyền truy cập trước cập nhật, từ chối đường đánh dấu từ trang thông báo không được phép xem. | Lan BANNED; không thay unread từ yêu cầu này | END:REJECTED | FR-M07-05.09, FR-M07-06.06 |


**E4 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-005 E4 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E4.1 | ACT-001 | Guest yêu cầu đánh dấu tất cả thông báo của mình đã đọc. | Chưa có phiên, không mượn dữ liệu/cài đặt của Lan | E4.2 | FR-M07-06.06 |
| E4.2 | SYSTEM | Hệ thống từ chối thao tác cần phiên và yêu cầu đăng nhập; không tự đăng nhập hoặc sửa dữ liệu. | Không có kết quả cá nhân hoặc thay đổi từ yêu cầu Guest | END:REJECTED | FR-M07-06.06 |


**E5 — thay toàn bộ M1 đến kết thúc:** Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-005 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-003 | Mod Mai bấm Đánh dấu tất cả đã đọc. | Người thao tác U-MAI; D-NOT55; chỉ đang thấy10 mục chuông | E5.2 | FR-M07-06.03 |
| E5.2 | SYSTEM | Hệ thống kiểm phiên và phạm vi dữ liệu của Mod Mai; chuyển mọi thông báo chưa đọc của Mod Mai thành đã đọc kể cả ngoài phần đang hiển thị, giữ các bản vốn đã đọc. Trả chuông 0 và giữ mốc đọc/số cuộc Chat, không xóa thông báo. | N001, N003, N011 đều read; unread 3→0; vẫn55 bản; thông báo Bình không đổi; Chat 3 cuộc/8 tin được thấy chưa đọc giữ nguyên | END:SUCCESS | FR-M07-05.05, FR-M07-06.03, FR-M07-06.05, FR-M07-06.06, BR-M07-14 |


<!-- sc:end SC-M07-005 -->

<a id="sc-m07-006"></a>

<!-- sc:scenario SC-M07-006 -->

### SC-M07-006

#### 1. Tên kịch bản chuẩn

Phản hồi đề xuất làm Mod hoặc Admin — BF-M07-006; owner [UC-M07-006](../../us/US-M07.md#uc-m07-006).

#### 2. Actor thực hiện

ACT-002 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-003 kế thừa quyền cá nhân User; đường E tại M1 ghi rõ dữ liệu thuộc actor đó. ACT-001 chỉ có đường từ chối. ACT-005 không tham gia chức năng actor này; email nằm ở AUT004/005.

#### 3. Tiền điều kiện

Đề xuất/thông báo và người nhận được nhận diện; kiểm hiệu lực, trạng thái và vai trò khi xử lý, không giả định mọi đề xuất còn hạn. D-PROP là đường chuẩn; M10 sở hữu quyết định hiệu lực/vai trò.

#### 4. Hậu điều kiện

<!-- sc:post SC-M07-006 -->

| result | condition |
|---|---|
| SUCCESS | Một quyết định được ghi nhận cho đề xuất còn hiệu lực: Chấp nhận đổi vai trò ngay theo loại; Từ chối giữ vai trò. Thông báo hiện lựa chọn và không cho trả lời lại; không kết thúc ở việc chỉ chuyển yêu cầu cho M10. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi nhận thao tác thành công hoặc sửa dữ liệu ngoài phạm vi của người thao tác. Những hiệu ứng riêng được nêu trong nhánh và hậu điều kiện tương ứng vẫn được giữ. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M07-006 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan mở trang Thông báo để phản hồi đề xuất R841. | D-PROP: N841 của Lan, gắn đề xuất R841 làm Mod do Admin gửi 03/11/2026 09:00+07, Chưa trả lời; hết hạn 10/11 09:00. Lúc thao tác09/11 10:00, Lan ACTIVE/USER, xong Bước 3. N841 là snapshot riêng, không cộng vào D-NOT55. | M2 | FR-M07-05.02 |
| M2 | SYSTEM | Hệ thống kiểm quyền xem danh sách của Lan, tải N841 từ dữ liệu đã lưu cùng trạng thái đề xuất hiện tại; R841 còn hiệu lực, chưa trả lời nên hiện Chấp nhận/Từ chối ở EP-PROPOSAL. Chỉ xem danh sách không tự đổi trạng thái đọc. | N841/R841 đúng Lan; USER; hai lựa chọn còn dùng được; giờ 09/11 10:00 trước 10/11 09:00 | M3 | FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24, FR-M07-02.14, FR-M07-02.15, FR-M07-02.16, FR-M07-02.28, FR-M07-02.30, FR-M07-02.31, FR-M07-02.32, BR-M07-20 |
| M3 | ACT-002 | Lan chọn Chấp nhận trên N841. | R841 đề xuất làm Mod; điều kiện tài khoản/vai trò và hiệu lực phải được kiểm lại khi xử lý lựa chọn | M4 | FR-M07-02.15 |
| M4 | SYSTEM | Hệ thống kiểm lại đúng người nhận, hiệu lực/chưa trả lời và vai trò/tài khoản M10 hiện tại; chuyển lựa chọn cho M10 và hoàn tất đổi vai trò MODERATOR ngay. Ghi đề xuất Đã chấp nhận, hiện lựa chọn trên N841, khóa chọn lại và trả kết quả trong danh sách thông báo. | Lan USER→MODERATOR; R841 Đã chấp nhận; N841 hiện lựa chọn đã chấp nhận, không còn lựa chọn mới; không xóa N841 | END:SUCCESS | FR-M07-02.15, FR-M07-02.28, BR-M07-20, FR-M10-03.01, FR-M10-03.02, FR-M10-03.04, FR-M10-03.10, FR-M10-03.11 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã hoàn tất. Guard và dữ liệu nhánh thay snapshot chuẩn cho lần chạy này; không áp đồng thời các snapshot. Mỗi đường ghi đầy đủ bước tới terminal hoặc điểm nhập lại. E tại M1 thay toàn bộ đường khi actor khởi tạo khác, không đổi danh tính giữa chừng. Không tự thêm nút OK/hủy/retry hoặc cơ chế rollback chưa có nguồn.

<!-- sc:exceptions SC-M07-006 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M3 | Người nhận chọn Từ chối đề xuất còn hiệu lực | E1.1 | FR-M07-02.16, FR-M07-02.28, BR-M07-20, FR-M10-03.03, FR-M10-03.04 |
| E2 | user-choice | M1 | Người dùng USER chấp nhận đề xuất làm Admin do ADMIN gốc gửi | E2.1 | FR-M07-05.02, FR-M07-02.14, FR-M07-03.04, FR-M07-05.01, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24, FR-M07-02.15, FR-M07-02.16, FR-M07-02.28, FR-M07-02.30, FR-M07-02.31, FR-M07-02.32, BR-M07-20, FR-M10-07.05, FR-M10-07.06, FR-M10-03.02, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11 |
| E3 | system | M4 | Đề xuất đã được trả lời sau lúc hiển thị, trước xử lý lựa chọn mới | E3.1 | FR-M07-02.28, FR-M10-03.06 |
| E4 | system | M4 | Đề xuất hết hạn sau lúc hiển thị, trước xử lý lựa chọn | E4.1 | FR-M07-02.31, BR-M07-20, FR-M10-02.10, FR-M10-03.08 |
| E5 | system | M4 | Đề xuất cũ bị thay sau lúc hiển thị, trước xử lý lựa chọn | E5.1 | FR-M07-02.30, FR-M07-02.32, BR-M07-20, FR-M10-02.08, FR-M10-03.08 |
| E6 | system | M4 | Vai trò không còn hợp lệ ở lúc chấp nhận | E6.1 | FR-M10-03.10 |
| E7 | system | M4 | Tài khoản không còn ACTIVE tại lúc chấp nhận | E7.1 | FR-M10-03.11 |
| E8 | user-choice | M1 | Đề xuất đã trả lời trước khi mở danh sách | E8.1 | FR-M07-05.02, FR-M07-02.28, FR-M10-03.06, FR-M07-05.05 |
| E9 | user-choice | M1 | Đề xuất đã hết hạn trước khi mở danh sách | E9.1 | FR-M07-05.02, FR-M07-02.31, BR-M07-20, FR-M10-02.10, FR-M07-05.05 |
| E10 | user-choice | M1 | Đề xuất đã bị thay thế trước khi mở danh sách | E10.1 | FR-M07-05.02, FR-M07-02.30, FR-M07-02.32, BR-M07-20, FR-M10-02.08, FR-M07-05.05 |
| E11 | system | M2 | Thông báo đề xuất không thuộc người đang xem | E11.1 | FR-M07-05.05, FR-M10-03.07 |
| E12 | system | M4 | Người gửi lựa chọn khác người được đề xuất | E12.1 | FR-M10-03.07 |
| E13 | system | M1 | ACT-001 — Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E13.1 | FR-M07-05.06 |
| E14 | system | M1 | ACT-003 — Người đang MODERATOR chấp nhận đề xuất làm Admin của ADMIN gốc. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E14.1 | FR-M07-05.02, FR-M07-02.14, FR-M07-03.04, FR-M07-05.01, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24, FR-M07-02.15, FR-M07-02.16, FR-M07-02.28, FR-M07-02.30, FR-M07-02.31, FR-M07-02.32, BR-M07-20, FR-M10-07.05, FR-M10-03.02, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11 |


<!-- sc:branch SC-M07-006 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Lan chọn Từ chối trên N841. | R841 còn hiệu lực, chưa trả lời; Lan USER | E1.2 | FR-M07-02.16 |
| E1.2 | SYSTEM | Hệ thống kiểm đúng người nhận/hiệu lực, ghi R841 Đã từ chối, giữ vai trò USER; hiện lựa chọn đã từ chối trên N841, khóa chọn lại và trả kết quả. Đây là hoàn thành phản hồi của actor. | Lan USER→USER; R841 Đã từ chối; N841 được giữ | END:SUCCESS | FR-M07-02.16, FR-M07-02.28, BR-M07-20, FR-M10-03.03, FR-M10-03.04 |


<!-- sc:branch SC-M07-006 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | Lan mở thông báo đề xuất làm Admin N842 của mình. | R842 do ADMIN gốc gửi, còn hiệu lực; Lan ACTIVE/USER | E2.2 | FR-M07-05.02, FR-M07-02.14 |
| E2.2 | SYSTEM | Hệ thống kiểm quyền của Lan, hiện R842 chưa trả lời và hai lựa chọn đúng hiệu lực. | Loại=Admin; giữ vai trò USER cho tới khi chấp nhận | E2.3 | FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24, FR-M07-02.14, FR-M07-02.15, FR-M07-02.16, FR-M07-02.28, FR-M07-02.30, FR-M07-02.31, FR-M07-02.32, BR-M07-20, FR-M10-07.05, FR-M10-07.06 |
| E2.3 | ACT-002 | Lan chọn Chấp nhận R842. | Đúng người nhận, ACTIVE/USER và đề xuất còn hiệu lực | E2.4 | FR-M07-02.15 |
| E2.4 | SYSTEM | Hệ thống kiểm lại điều kiện M10, đổi vai trò ADMIN ngay; ghi Đã chấp nhận, hiện lựa chọn và khóa chọn lại, giữ thông báo. | Lan USER→ADMIN; R842 Đã chấp nhận | END:SUCCESS | FR-M07-02.15, FR-M07-02.28, BR-M07-20, FR-M10-03.02, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11 |


<!-- sc:branch SC-M07-006 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối nhận lựa chọn mới, giữ quyết định và vai trò đã có, hiện lựa chọn đã chọn trên thông báo. | R841 còn hiệu lực lúc M2; trước xử lý M4 đã Đã từ chối; người nhận vẫn USER | END:REJECTED | FR-M07-02.28, FR-M10-03.06 |


<!-- sc:branch SC-M07-006 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống dùng trạng thái M10, hiện “Đã hết hạn”, không cho Chấp nhận/Từ chối, giữ nguyên vai trò. | R841 gửi 03/11 09:00; M2 lúc09/11 10:00 còn hạn; lựa chọn xử lý10/11 09:00:01 đã quá hạn, chưa trả lời | END:REJECTED | FR-M07-02.31, BR-M07-20, FR-M10-02.10, FR-M10-03.08 |


<!-- sc:branch SC-M07-006 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối lựa chọn trên đề xuất cũ, giữ thông báo mới riêng; không tự gán nhãn hết hạn cho nguyên nhân thay thế. | R841 còn hiệu lực lúc M2; trước M4 có R843 mới cùng loại/cùng người nên R841 Hết hiệu lực; N843 khác N841 | END:REJECTED | FR-M07-02.30, FR-M07-02.32, BR-M07-20, FR-M10-02.08, FR-M10-03.08 |


<!-- sc:branch SC-M07-006 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối chấp nhận theo M10, không đổi vai trò hoặc ghi một lần chấp nhận thành công giả. | R841 đề xuất Mod nhưng Lan đã là ADMIN ở lúc chọn | END:REJECTED | FR-M10-03.10 |


<!-- sc:branch SC-M07-006 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối chấp nhận theo M10, giữ vai trò; không dùng điều kiện ACTIVE lúc mở danh sách thay điều kiện khi chọn. | Lan chuyển DEACTIVATED/BANNED trước xử lý lựa chọn | END:REJECTED | FR-M10-03.11 |


<!-- sc:branch SC-M07-006 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | ACT-002 | Lan mở thông báo đề xuất cũ để kiểm tra khả năng phản hồi. | R841 đã Đã từ chối; vai trò USER | E8.2 | FR-M07-05.02 |
| E8.2 | SYSTEM | Hệ thống trả thông báo của Lan với lựa chọn đã từ chối, không hiện hai lựa chọn còn dùng được và không nhận quyết định mới. | R841 đã Đã từ chối; vai trò USER | END:REJECTED | FR-M07-02.28, FR-M10-03.06, FR-M07-05.05 |


<!-- sc:branch SC-M07-006 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | ACT-002 | Lan mở thông báo đề xuất cũ để kiểm tra khả năng phản hồi. | R841 gửi 01/11 09:00; lúc mở09/11 10:00 đã quá7×24 giờ, chưa trả lời | E9.2 | FR-M07-05.02 |
| E9.2 | SYSTEM | Hệ thống trả thông báo hiện Đã hết hạn theo M10, không cho chọn Chấp nhận/Từ chối, không đổi vai trò. | R841 gửi 01/11 09:00; lúc mở09/11 10:00 đã quá7×24 giờ, chưa trả lời | END:REJECTED | FR-M07-02.31, BR-M07-20, FR-M10-02.10, FR-M07-05.05 |


<!-- sc:branch SC-M07-006 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | ACT-002 | Lan mở thông báo đề xuất cũ để kiểm tra khả năng phản hồi. | R841 cũ Hết hiệu lực; R843 mới cùng loại/cùng Lan còn hiệu lực, N843 mới khác N841 | E10.2 | FR-M07-05.02 |
| E10.2 | SYSTEM | Hệ thống trả thông báo cũ không còn lựa chọn có hiệu lực và giữ thông báo mới riêng; không gán nhãn hết hạn cho nguyên nhân thay thế. | R841 cũ Hết hiệu lực; R843 mới cùng loại/cùng Lan còn hiệu lực, N843 mới khác N841 | END:REJECTED | FR-M07-02.30, FR-M07-02.32, BR-M07-20, FR-M10-02.08, FR-M07-05.05 |


<!-- sc:branch SC-M07-006 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | SYSTEM | Hệ thống không hiển thị thông báo đề xuất của Bình qua danh sách/ID cho Lan và không cho phản hồi hộ. | N841 trong snapshot nhánh thuộc U-BINH | END:REJECTED | FR-M07-05.05, FR-M10-03.07 |


<!-- sc:branch SC-M07-006 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | SYSTEM | Hệ thống từ chối phản hồi, không đổi vai trò hoặc quyết định của người nhận thật. | Lan gửi lựa chọn cho R841 của Bình | END:REJECTED | FR-M10-03.07 |


**E13 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-006 E13 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E13.1 | ACT-001 | Guest yêu cầu phản hồi đề xuất làm mod hoặc admin. | Chưa có phiên, không mượn dữ liệu/cài đặt của Lan | E13.2 | FR-M07-05.06 |
| E13.2 | SYSTEM | Hệ thống từ chối thao tác cần phiên và yêu cầu đăng nhập; không tự đăng nhập hoặc sửa dữ liệu. | Không có kết quả cá nhân hoặc thay đổi từ yêu cầu Guest | END:REJECTED | FR-M07-05.06 |


**E14 — thay toàn bộ M1 đến kết thúc:** Người đang MODERATOR chấp nhận đề xuất làm Admin của ADMIN gốc. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-006 E14 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E14.1 | ACT-003 | Mod Mai mở thông báo đề xuất làm Admin của mình. | N844/R844 do ADMIN gốc gửi, còn hiệu lực, chưa trả lời; Mai ACTIVE/MODERATOR | E14.2 | FR-M07-05.02, FR-M07-02.14 |
| E14.2 | SYSTEM | Hệ thống kiểm đúng Mai, tải đề xuất làm Admin hiện tại và hai lựa chọn. | N844 thuộc Mai, R844 còn hiệu lực; không phải đề xuất làm Mod cho một Mod | E14.3 | FR-M07-03.04, FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24, FR-M07-02.14, FR-M07-02.15, FR-M07-02.16, FR-M07-02.28, FR-M07-02.30, FR-M07-02.31, FR-M07-02.32, BR-M07-20, FR-M10-07.05 |
| E14.3 | ACT-003 | Mod Mai chọn Chấp nhận R844. | Mai vẫn ACTIVE/MODERATOR; đúng người nhận | E14.4 | FR-M07-02.15 |
| E14.4 | SYSTEM | Hệ thống kiểm điều kiện M10 và đổi vai trò ADMIN ngay, ghi Đã chấp nhận, hiện lựa chọn/khóa chọn lại và giữ N844. | Mai MODERATOR→ADMIN; R844 Đã chấp nhận | END:SUCCESS | FR-M07-02.15, FR-M07-02.28, BR-M07-20, FR-M10-03.02, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11 |


<!-- sc:end SC-M07-006 -->

<a id="sc-m07-007"></a>

<!-- sc:scenario SC-M07-007 -->

### SC-M07-007

#### 1. Tên kịch bản chuẩn

Kiểm tra số cuộc trò chuyện chưa đọc và mở hộp thư — BF-M07-007; owner [UC-M07-023](../../us/US-M07.md#uc-m07-023).

#### 2. Actor thực hiện

ACT-002 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-003 kế thừa quyền cá nhân User; đường E tại M1 ghi rõ dữ liệu thuộc actor đó. ACT-001 chỉ có đường từ chối. ACT-005 không tham gia chức năng actor này; email nằm ở AUT004/005.

#### 3. Tiền điều kiện

Có ngữ cảnh yêu cầu kiểm tra tin mới; phiên và dữ liệu tin được thấy/mốc đọc từ M16 được xét. Đường chuẩn Lan có phiên, D-CHAT, chuông 3; không giả định số tin bằng số cuộc hoặc mute làm mất unread.

#### 4. Hậu điều kiện

<!-- sc:post SC-M07-007 -->

| result | condition |
|---|---|
| SUCCESS | Chỉ báo đúng số cuộc có tin chưa đọc được thấy được trả, không loại cuộc mute hoặc đếm tin sau lúc rời không được thấy. Khi actor chọn mở hộp thư, điều hướng M16 đúng quyền, không tự đọc mọi cuộc hay ảnh hưởng chuông. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi nhận thao tác thành công hoặc sửa dữ liệu ngoài phạm vi của người thao tác. Những hiệu ứng riêng được nêu trong nhánh và hậu điều kiện tương ứng vẫn được giữ. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M07-007 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan mở ứng dụng để kiểm tra tin nhắn mới. | D-CHAT: C71 (1-1 với Bình) có 5 tin chưa đọc được thấy; C72 (nhóm đang là thành viên) có 2; C73 (nhóm đã rời09:00) có 1 tin08:50 chưa đọc, 1 tin09:10 không được thấy, mốc đọc08:30. C74 không có quyền nên không tính; C75 là nhóm cũ chỉ có tin sau lúc rời nên không tính. Số cuộc chưa đọc=3, số tin chưa đọc được thấy=8. C71 mute riêng, C72 Đang nhận, global mute=false. | M2 | FR-M07-07.01, FR-M07-07.02 |
| M2 | SYSTEM | Hệ thống xác định Lan có phiên, lấy mốc đọc và tin được thấy từ M16; đếm mỗi cuộc có ít nhất một tin chưa đọc được thấy một lần, kể cả cuộc mute. Hiện biểu tượng Tin nhắn riêng với số3, tách chuông; không tự đánh dấu tin hay thông báo đã đọc. | C71, C72, C73 đóng góp3; C74/C75 không góp; 8 tin được thấy không biến thành badge 8; chuông 3 giữ riêng | END:SUCCESS | FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã hoàn tất. Guard và dữ liệu nhánh thay snapshot chuẩn cho lần chạy này; không áp đồng thời các snapshot. Mỗi đường ghi đầy đủ bước tới terminal hoặc điểm nhập lại. E tại M1 thay toàn bộ đường khi actor khởi tạo khác, không đổi danh tính giữa chừng. Không tự thêm nút OK/hủy/retry hoặc cơ chế rollback chưa có nguồn.

<!-- sc:exceptions SC-M07-007 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M2 | Lan chọn mở hộp thư từ biểu tượng sau khi kiểm tra số tin | E1.1 | FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10, FR-M16-03.01, FR-M16-07.01 |
| E2 | system | M2 | Toàn bộ Chat bị mute hoặc các cuộc có tin đều mute riêng | E2.1 | FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10, FR-M07-09.03 |
| E3 | system | M2 | Cờ Chat tắt | E3.1 | FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10 |
| E4 | system | M2 | Chỉ nhóm cũ có tin mới sau lúc rời, không còn tin chưa đọc được thấy | E4.1 | FR-M07-07.02, BR-M07-02, FR-M16-07.10 |
| E5 | system | M2 | Chỉ một cuộc nhận nhiều tin chưa đọc | E5.1 | FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10 |
| E6 | system | M1 | ACT-001 — Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M07-07.04 |
| E7 | system | M1 | ACT-003 — Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E7.1 | FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10 |


<!-- sc:branch SC-M07-007 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống trả chỉ báo3 cuộc đúng D-CHAT, tách chuông và không đổi mốc đọc. | Biểu tượng Tin nhắn3; chuông 3 | E1.2 | FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10 |
| E1.2 | ACT-002 | Lan bấm biểu tượng Tin nhắn. | Yêu cầu mở hộp thư, chưa mở từng cuộc | E1.3 | FR-M07-07.03 |
| E1.3 | SYSTEM | Hệ thống chuyển tới hộp thư Chat M16, hiển thị các cuộc Lan là thành viên hoặc thành viên cũ theo quyền. Không coi mở hộp thư là đọc hết mọi cuộc; thao tác mở/đọc từng cuộc thuộc M16. | Hộp thư của Lan; chỉ báo vẫn theo read marker M16, không tự ghi badge 0 hoặc thay chuông | END:SUCCESS | FR-M07-07.03, BR-M07-02, FR-M16-03.01, FR-M16-07.01 |


<!-- sc:branch SC-M07-007 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống vẫn đếm đủ C71, C72, C73 theo dữ liệu được thấy, trả số3; mute chỉ chặn popup, không làm badge 0 hoặc đưa tin vào chuông/email. | global mute=true hoặc per-conversation mute=true; Chat 3, chuông 3 | END:SUCCESS | FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10, FR-M07-09.03 |


<!-- sc:branch SC-M07-007 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống vẫn trả biểu tượng và số cuộc chưa đọc theo dữ liệu M16; không tự coi cờ tắt là hết tin hoặc xóa lịch sử. Hành vi thao tác bên trong Chat khi mở do M16 sở hữu. | D-CHAT cho badge 3; chưa yêu cầu mở hộp thư trong đường này | END:SUCCESS | FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10 |


<!-- sc:branch SC-M07-007 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống dùng quyền tin/mốc đọc của M16, không đếm tin gửi sau lúc rời. Trả số0 nếu không cuộc nào còn tin chưa đọc được thấy; không đổi mốc để tạo kết quả này. | C73 trước rời đã đọc hết; chỉ tin09:10 sau lúc rời09:00 chưa đọc nhưng không được thấy; C71/C72 không unread | END:SUCCESS | FR-M07-07.02, BR-M07-02, FR-M16-07.10 |


<!-- sc:branch SC-M07-007 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống đếm cuộc có tin chưa đọc, không đếm số tin; trả1 và giữ số chuông độc lập. | C71 có 5 tin được thấy chưa đọc; mọi cuộc khác không unread; badge 1, không5 | END:SUCCESS | FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10 |


**E6 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-007 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-001 | Guest yêu cầu kiểm tra số cuộc trò chuyện chưa đọc và mở hộp thư. | Chưa có phiên, không mượn dữ liệu/cài đặt của Lan | E6.2 | FR-M07-07.04 |
| E6.2 | SYSTEM | Hệ thống không hiện biểu tượng Tin nhắn cho Guest; không trả dữ liệu cuộc trò chuyện. | Không có kết quả cá nhân hoặc thay đổi từ yêu cầu Guest | END:REJECTED | FR-M07-07.04 |


**E7 — thay toàn bộ M1 đến kết thúc:** Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-007 E7 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E7.1 | ACT-003 | Mod Mai mở ứng dụng để kiểm tra tin nhắn mới. | D-CHAT: C71 (1-1 với Bình) có 5 tin chưa đọc được thấy; C72 (nhóm đang là thành viên) có 2; C73 (nhóm đã rời09:00) có 1 tin08:50 chưa đọc, 1 tin09:10 không được thấy, mốc đọc08:30. C74 không có quyền nên không tính; C75 là nhóm cũ chỉ có tin sau lúc rời nên không tính. Số cuộc chưa đọc=3, số tin chưa đọc được thấy=8. C71 mute riêng, C72 Đang nhận, global mute=false. | E7.2 | FR-M07-07.01, FR-M07-07.02 |
| E7.2 | SYSTEM | Hệ thống xác định Mod Mai có phiên, lấy mốc đọc và tin được thấy từ M16; đếm mỗi cuộc có ít nhất một tin chưa đọc được thấy một lần, kể cả cuộc mute. Hiện biểu tượng Tin nhắn riêng với số3, tách chuông; không tự đánh dấu tin hay thông báo đã đọc. | C71, C72, C73 đóng góp3; C74/C75 không góp; 8 tin được thấy không biến thành badge 8; chuông 3 giữ riêng | END:SUCCESS | FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10 |


<!-- sc:end SC-M07-007 -->

<a id="sc-m07-008"></a>

<!-- sc:scenario SC-M07-008 -->

### SC-M07-008

#### 1. Tên kịch bản chuẩn

Bật hoặc tắt nhận thông báo tương tác theo bài — BF-M07-008; owner [UC-M07-009](../../us/US-M07.md#uc-m07-009).

#### 2. Actor thực hiện

ACT-002 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-003 kế thừa quyền cá nhân User; đường E tại M1 ghi rõ dữ liệu thuộc actor đó. ACT-001 chỉ có đường từ chối. ACT-005 không tham gia chức năng actor này; email nằm ở AUT004/005.

#### 3. Tiền điều kiện

Có bài và người thao tác; không cần là tác giả hoặc đã từng tương tác mới có công tắc. Đường chuẩn Lan có phiên và được xem P701; đang nhận thông báo bài, dữ liệu D-POST.

#### 4. Hậu điều kiện

<!-- sc:post SC-M07-008 -->

| result | condition |
|---|---|
| SUCCESS | Cài đặt theo bài của mình đã được lưu/bỏ đúng lựa chọn, chỉ tác động các loại tương tác được quy định. Bật lại nhận từ lúc đó; nhắc tên/xử lý khác vẫn theo quy tắc chung, người khác và bản ghi cũ không bị thay đổi. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi nhận thao tác thành công hoặc sửa dữ liệu ngoài phạm vi của người thao tác. Những hiệu ứng riêng được nêu trong nhánh và hậu điều kiện tương ứng vẫn được giữ. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M07-008 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan mở P701 để thay cài đặt nhận thông báo cho bài này. | D-POST: P701 của Bình, Đã đăng/Bình thường, ngoài nhóm, Lan được xem; Lan chưa từng tương tác và đang nhận thông báo bài. Bình và các người dùng khác có cài đặt riêng, không đổi theo Lan. | M2 | FR-M07-08.01 |
| M2 | SYSTEM | Hệ thống kiểm ngữ cảnh đăng nhập/quyền bài và hiện công tắc Tắt thông báo cho bài này cùng cài đặt cá nhân hiện tại. Không buộc Lan đã viết/vote bài. | U-LAN/P701: đang nhận; công tắc Tắt đang=false | M3 | FR-M07-08.01 |
| M3 | ACT-002 | Lan bật Tắt thông báo cho bài này. | U-LAN/P701: muốn mute=true | M4 | FR-M07-08.02 |
| M4 | SYSTEM | Hệ thống lưu mute cho cặp Lan–P701, trả cài đặt đã tắt. Từ hiệu lực cài đặt chặn bình luận mới, trả lời, upvote bài và upvote bình luận của Lan trong bài; nhắc tên/thông báo xử lý khác vẫn theo quyền/người nhận chung. Người khác và thông báo đã lưu không bị đổi. | mute(U-LAN, P701)=true; Bình vẫn nhận theo cài đặt của Bình; D-NOT55 vẫn giữ, unread 3 không tự về0 | END:SUCCESS | FR-M07-08.01, FR-M07-08.02, FR-M07-08.03, FR-M07-08.04, FR-M07-02.07, FR-M07-02.08, FR-M07-02.09, BR-M07-06, BR-M07-07 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã hoàn tất. Guard và dữ liệu nhánh thay snapshot chuẩn cho lần chạy này; không áp đồng thời các snapshot. Mỗi đường ghi đầy đủ bước tới terminal hoặc điểm nhập lại. E tại M1 thay toàn bộ đường khi actor khởi tạo khác, không đổi danh tính giữa chừng. Không tự thêm nút OK/hủy/retry hoặc cơ chế rollback chưa có nguồn.

<!-- sc:exceptions SC-M07-008 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M2 | Bài đang mute, Lan chọn nhận lại | E1.1 | FR-M07-08.01, FR-M07-08.03, FR-M07-08.04, BR-M07-07 |
| E2 | system | M1 | ACT-001 — Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E2.1 | FR-M07-08.05 |
| E3 | system | M1 | ACT-003 — Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E3.1 | FR-M07-08.01, FR-M07-08.02, FR-M07-08.03, FR-M07-08.04, FR-M07-02.07, FR-M07-02.08, FR-M07-02.09, BR-M07-06, BR-M07-07 |


<!-- sc:branch SC-M07-008 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống trả công tắc hiện có đã bật Tắt cho Lan–P701. | mute=true; các thông báo cũ vẫn giữ | E1.2 | FR-M07-08.01 |
| E1.2 | ACT-002 | Lan tắt công tắc Tắt thông báo cho bài này. | Muốn bỏ mute của mình, không đổi người khác | E1.3 | FR-M07-08.03 |
| E1.3 | SYSTEM | Hệ thống bỏ ghi nhận mute Lan–P701, trả đang nhận; các sự kiện đủ điều kiện từ thời điểm này được nhận bình thường. Không tự phát lại các sự kiện đã bị chặn trước đó vì nguồn chưa có chính sách đó. | mute=false từ09/11 10:00; thông báo cũ/read-unread giữ theo dữ liệu đang có | END:SUCCESS | FR-M07-08.03, FR-M07-08.04, BR-M07-07 |


**E2 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-008 E2 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E2.1 | ACT-001 | Guest yêu cầu bật hoặc tắt nhận thông báo tương tác theo bài. | Chưa có phiên, không mượn dữ liệu/cài đặt của Lan | E2.2 | FR-M07-08.05 |
| E2.2 | SYSTEM | Hệ thống từ chối thao tác cần phiên và yêu cầu đăng nhập; không tự đăng nhập hoặc sửa dữ liệu. | Không có kết quả cá nhân hoặc thay đổi từ yêu cầu Guest | END:REJECTED | FR-M07-08.05 |


**E3 — thay toàn bộ M1 đến kết thúc:** Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-008 E3 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E3.1 | ACT-003 | Mod Mai mở P701 để thay cài đặt nhận thông báo cho bài này. | D-POST: P701 của Bình, Đã đăng/Bình thường, ngoài nhóm, Mod Mai được xem; Mod Mai chưa từng tương tác và đang nhận thông báo bài. Bình và các người dùng khác có cài đặt riêng, không đổi theo Mod Mai. | E3.2 | FR-M07-08.01 |
| E3.2 | SYSTEM | Hệ thống kiểm ngữ cảnh đăng nhập/quyền bài và hiện công tắc Tắt thông báo cho bài này cùng cài đặt cá nhân hiện tại. Không buộc Mod Mai đã viết/vote bài. | U-MAI/P701: đang nhận; công tắc Tắt đang=false | E3.3 | FR-M07-08.01 |
| E3.3 | ACT-003 | Mod Mai bật Tắt thông báo cho bài này. | U-MAI/P701: muốn mute=true | E3.4 | FR-M07-08.02 |
| E3.4 | SYSTEM | Hệ thống lưu mute cho cặp Mod Mai–P701, trả cài đặt đã tắt. Từ hiệu lực cài đặt chặn bình luận mới, trả lời, upvote bài và upvote bình luận của Mod Mai trong bài; nhắc tên/thông báo xử lý khác vẫn theo quyền/người nhận chung. Người khác và thông báo đã lưu không bị đổi. | mute(U-MAI, P701)=true; Bình vẫn nhận theo cài đặt của Bình; D-NOT55 vẫn giữ, unread 3 không tự về0 | END:SUCCESS | FR-M07-08.01, FR-M07-08.02, FR-M07-08.03, FR-M07-08.04, FR-M07-02.07, FR-M07-02.08, FR-M07-02.09, BR-M07-06, BR-M07-07 |


<!-- sc:end SC-M07-008 -->

<a id="sc-m07-009"></a>

<!-- sc:scenario SC-M07-009 -->

### SC-M07-009

#### 1. Tên kịch bản chuẩn

Bật hoặc tắt popup riêng của một cuộc trò chuyện — BF-M07-009; owner [UC-M07-010](../../us/US-M07.md#uc-m07-010).

#### 2. Actor thực hiện

ACT-002 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-003 kế thừa quyền cá nhân User; đường E tại M1 ghi rõ dữ liệu thuộc actor đó. ACT-001 chỉ có đường từ chối. ACT-005 không tham gia chức năng actor này; email nằm ở AUT004/005.

#### 3. Tiền điều kiện

Có cuộc C71 và người thao tác; đăng nhập/thành viên được kiểm. Đường chuẩn Lan là thành viên C71, đang nhận popup C71 (snapshot thay trạng thái mute của D-CHAT), global mute=false; badge vẫn3 theo dữ liệu tin hiện có.

#### 4. Hậu điều kiện

<!-- sc:post SC-M07-009 -->

| result | condition |
|---|---|
| SUCCESS | Mute riêng của thành viên–cuộc được lưu/bỏ theo lựa chọn. Popup còn phụ thuộc global mute và đang xem đúng cuộc; số cuộc unread/read marker và cài đặt người khác không đổi do mute. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi nhận thao tác thành công hoặc sửa dữ liệu ngoài phạm vi của người thao tác. Những hiệu ứng riêng được nêu trong nhánh và hậu điều kiện tương ứng vẫn được giữ. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M07-009 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan chọn tắt thông báo C71 đang là thành viên. | C71 1-1; per mute=false; global mute=false; badge 3 | M2 | FR-M07-09.01 |
| M2 | SYSTEM | Hệ thống kiểm phiên và thành viên hiện tại, ghi mute riêng cho Lan–C71, trả cài đặt đã tắt. Tin mới C71 không popup cho Lan; badge vẫn đếm C71 nếu có tin chưa đọc được thấy, không đổi người khác hoặc mốc đọc. | per mute(U-LAN, C71)=true; global=false; badge 3→3; không thêm tin Chat vào chuông/email | END:SUCCESS | FR-M07-09.01, FR-M07-09.02, FR-M07-09.05, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã hoàn tất. Guard và dữ liệu nhánh thay snapshot chuẩn cho lần chạy này; không áp đồng thời các snapshot. Mỗi đường ghi đầy đủ bước tới terminal hoặc điểm nhập lại. E tại M1 thay toàn bộ đường khi actor khởi tạo khác, không đổi danh tính giữa chừng. Không tự thêm nút OK/hủy/retry hoặc cơ chế rollback chưa có nguồn.

<!-- sc:exceptions SC-M07-009 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Lan bật lại riêng C71; global mute=false | E1.1 | FR-M07-09.02, FR-M07-09.03, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |
| E2 | user-choice | M1 | Lan bật lại riêng C71; global mute=true | E2.1 | FR-M07-09.02, FR-M07-09.03, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |
| E3 | user-choice | M1 | Thành viên tắt popup cho nhóm chat thay cuộc1-1 | E3.1 | FR-M07-09.01, FR-M07-09.02, FR-M07-09.05, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |
| E4 | system | M2 | Lan không còn là thành viên cuộc | E4.1 | FR-M07-09.05 |
| E5 | system | M1 | ACT-001 — Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E5.1 | FR-M07-09.06 |
| E6 | system | M1 | ACT-003 — Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E6.1 | FR-M07-09.01, FR-M07-09.02, FR-M07-09.05, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |


<!-- sc:branch SC-M07-009 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Lan chọn bật lại thông báo C71. | Lan vẫn là thành viên; per mute=true; global mute=false | E1.2 | FR-M07-09.02 |
| E1.2 | SYSTEM | Hệ thống kiểm quyền, bỏ mute riêng và trả cài đặt cấp cuộc đang nhận. Popup tin mới từ lúc này còn cần đang mở ứng dụng và không xem đúng cuộc. | per mute=false; global=false; badge 3 giữ nguyên; không phát lại popup cũ | END:SUCCESS | FR-M07-09.02, FR-M07-09.03, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |


<!-- sc:branch SC-M07-009 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | Lan chọn bật lại thông báo C71. | Lan vẫn là thành viên; per mute=true; global mute=true | E2.2 | FR-M07-09.02 |
| E2.2 | SYSTEM | Hệ thống kiểm quyền, bỏ mute riêng và trả cài đặt cấp cuộc đang nhận. Global mute vẫn chặn mọi popup, không có ngoại lệ riêng. | per mute=false; global=true; badge 3 giữ nguyên; không phát lại popup cũ | END:SUCCESS | FR-M07-09.02, FR-M07-09.03, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |


<!-- sc:branch SC-M07-009 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-002 | Lan tắt thông báo nhóm chat C72 đang tham gia. | C72 là nhóm; per mute=false; global=false | E3.2 | FR-M07-09.01 |
| E3.2 | SYSTEM | Hệ thống kiểm tư cách thành viên và lưu mute cho Lan–C72, trả cài đặt đã tắt; không tắt popup của các thành viên khác hay thay badge/read marker. | per mute(U-LAN, C72)=true; badge 3 giữ nguyên | END:SUCCESS | FR-M07-09.01, FR-M07-09.02, FR-M07-09.05, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |


<!-- sc:branch SC-M07-009 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối tắt thông báo cuộc đó; không coi quyền xem tin cũ của thành viên cũ là quyền đổi cài đặt cuộc đang tham gia. | Lan đã rời C72 hoặc không thuộc C71 tại lúc xử lý | END:REJECTED | FR-M07-09.05 |


**E5 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-009 E5 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E5.1 | ACT-001 | Guest yêu cầu bật hoặc tắt popup riêng của một cuộc trò chuyện. | Chưa có phiên, không mượn dữ liệu/cài đặt của Lan | E5.2 | FR-M07-09.06 |
| E5.2 | SYSTEM | Hệ thống từ chối thao tác cần phiên và yêu cầu đăng nhập; không tự đăng nhập hoặc sửa dữ liệu. | Không có kết quả cá nhân hoặc thay đổi từ yêu cầu Guest | END:REJECTED | FR-M07-09.06 |


**E6 — thay toàn bộ M1 đến kết thúc:** Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-009 E6 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E6.1 | ACT-003 | Mod Mai chọn tắt thông báo C71 đang là thành viên. | C71 1-1; per mute=false; global mute=false; badge 3 | E6.2 | FR-M07-09.01 |
| E6.2 | SYSTEM | Hệ thống kiểm phiên và thành viên hiện tại, ghi mute riêng cho Mod Mai–C71, trả cài đặt đã tắt. Tin mới C71 không popup cho Mod Mai; badge vẫn đếm C71 nếu có tin chưa đọc được thấy, không đổi người khác hoặc mốc đọc. | per mute(U-MAI, C71)=true; global=false; badge 3→3; không thêm tin Chat vào chuông/email | END:SUCCESS | FR-M07-09.01, FR-M07-09.02, FR-M07-09.05, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |


<!-- sc:end SC-M07-009 -->

<a id="sc-m07-010"></a>

<!-- sc:scenario SC-M07-010 -->

### SC-M07-010

#### 1. Tên kịch bản chuẩn

Bật hoặc tắt popup toàn bộ Chat — BF-M07-010; owner [UC-M07-011](../../us/US-M07.md#uc-m07-011).

#### 2. Actor thực hiện

ACT-002 là actor chính, chủ động yêu cầu và nhận kết quả. ACT-003 kế thừa quyền cá nhân User; đường E tại M1 ghi rõ dữ liệu thuộc actor đó. ACT-001 chỉ có đường từ chối. ACT-005 không tham gia chức năng actor này; email nằm ở AUT004/005.

#### 3. Tiền điều kiện

Có người thao tác và cài đặt cá nhân; kiểm phiên. Đường chuẩn Lan có global mute=false, C71 mute riêng, C72 đang nhận; số cuộc unread 3. Cài đặt riêng phải được giữ qua đổi global.

#### 4. Hậu điều kiện

<!-- sc:post SC-M07-010 -->

| result | condition |
|---|---|
| SUCCESS | Global mute được lưu theo lựa chọn. Khi bật, mọi popup Chat của mình bị chặn; khi bỏ, popup tuân cài đặt riêng đã giữ và điều kiện đang xem/đang mở. Không xóa mute riêng hoặc unread. |
| REJECTED | Yêu cầu hiện tại bị từ chối theo guard; không cấp quyền, không ghi nhận thao tác thành công hoặc sửa dữ liệu ngoài phạm vi của người thao tác. Những hiệu ứng riêng được nêu trong nhánh và hậu điều kiện tương ứng vẫn được giữ. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M07-010 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Lan bật Tắt thông báo cho toàn bộ Chat. | Global false→true; C71 mute riêng=true, C72=false | M2 | FR-M07-09.03 |
| M2 | SYSTEM | Hệ thống ghi global mute cho Lan, trả đã tắt popup mọi cuộc1-1/nhóm chat, không có ngoại lệ. Giữ mute riêng từng cuộc, badge/read marker, chuông và cài đặt người khác. | global=true; per C71=true, C72=false giữ; Chat badge 3→3; chuông 3 giữ | END:SUCCESS | FR-M07-09.03, FR-M07-09.04, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |


#### 6. Các ngoại lệ

E thay đúng bước at, không chạy sau khi bước đó đã hoàn tất. Guard và dữ liệu nhánh thay snapshot chuẩn cho lần chạy này; không áp đồng thời các snapshot. Mỗi đường ghi đầy đủ bước tới terminal hoặc điểm nhập lại. E tại M1 thay toàn bộ đường khi actor khởi tạo khác, không đổi danh tính giữa chừng. Không tự thêm nút OK/hủy/retry hoặc cơ chế rollback chưa có nguồn.

<!-- sc:exceptions SC-M07-010 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Lan bỏ Tắt toàn bộ Chat để nhận lại theo từng cuộc | E1.1 | FR-M07-09.04, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |
| E2 | system | M1 | ACT-001 — Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4. | E2.1 | FR-M07-09.06 |
| E3 | system | M1 | ACT-003 — Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4. | E3.1 | FR-M07-09.03, FR-M07-09.04, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |


<!-- sc:branch SC-M07-010 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Lan tắt Tắt thông báo cho toàn bộ Chat. | Global đang=true; C71 mute riêng=true, C72=false | E1.2 | FR-M07-09.04 |
| E1.2 | SYSTEM | Hệ thống bỏ global mute, giữ nguyên từng cài đặt riêng; trả global=false. Tin mới C71 vẫn không popup vì mute riêng; C72 có thể popup nếu đủ điều kiện, badge vẫn3. | global=false; per C71=true, C72=false; không tự bật nhận mọi cuộc | END:SUCCESS | FR-M07-09.04, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |


**E2 — thay toàn bộ M1 đến kết thúc:** Guest chưa có phiên yêu cầu chức năng này. Actor khởi tạo ACT-001; END:REJECTED; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-010 E2 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E2.1 | ACT-001 | Guest yêu cầu bật hoặc tắt popup toàn bộ chat. | Chưa có phiên, không mượn dữ liệu/cài đặt của Lan | E2.2 | FR-M07-09.06 |
| E2.2 | SYSTEM | Hệ thống từ chối thao tác cần phiên và yêu cầu đăng nhập; không tự đăng nhập hoặc sửa dữ liệu. | Không có kết quả cá nhân hoặc thay đổi từ yêu cầu Guest | END:REJECTED | FR-M07-09.06 |


**E3 — thay toàn bộ M1 đến kết thúc:** Mod/Admin thực hiện chức năng cá nhân như User; snapshot dữ liệu/cài đặt thuộc Mod Mai thay Lan, không cấp quyền với dữ liệu người khác. Actor khởi tạo ACT-003; END:SUCCESS; dùng hậu điều kiện tương ứng mục 4.

<!-- sc:branch SC-M07-010 E3 -->

| step | subject | action | data | next | sources |
| --- | --- | --- | --- | --- | --- |
| E3.1 | ACT-003 | Mod Mai bật Tắt thông báo cho toàn bộ Chat. | Global false→true; C71 mute riêng=true, C72=false | E3.2 | FR-M07-09.03 |
| E3.2 | SYSTEM | Hệ thống ghi global mute cho Mod Mai, trả đã tắt popup mọi cuộc1-1/nhóm chat, không có ngoại lệ. Giữ mute riêng từng cuộc, badge/read marker, chuông và cài đặt người khác. | global=true; per C71=true, C72=false giữ; Chat badge 3→3; chuông 3 giữ | END:SUCCESS | FR-M07-09.03, FR-M07-09.04, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |


<!-- sc:end SC-M07-010 -->

## 5. Hành vi nền, kênh và ví dụ đối soát

| ID | Trigger/điều kiện | Hiệu ứng, lỗi/lựa chọn và giới hạn | sources |
|---|---|---|---|
| AUT-M07-001 | Owner cung cấp sự kiện, recipient, nội dung và thời điểm | Với sự kiện whitelist, tạo một thông báo unread riêng cho mỗi người nhận đủ điều kiện; dùng dữ liệu owner, lưu trước đẩy, giữ vô thời hạn. Xét mute bài, quyền Private và trạng thái recipient: BANNED/DEACTIVATED vẫn tạo, DELETED không tạo. Causer trùng recipient không tự báo; riêng hợp đồng causer của bảo mật còn GAP-SC-M07-001, không tự loại mất thông báo bảo mật hoặc đặt ngoại lệ mới. Chat/cảnh báo tự xóa/các loại bị loại không tạo chuông; bài AI tự từ chối kèm cảnh cáo dùng thông báo gộp M09. Xử lý khiếu nại được có link, đề xuất vai trò gắn đúng ID/loại, mời nhóm chỉ link mời theo owner. | FR-M07-02.01, FR-M07-02.02, FR-M07-02.07, FR-M07-02.08, FR-M07-02.09, FR-M07-02.10, FR-M07-02.11, FR-M07-02.13, FR-M07-02.14, FR-M07-02.17, FR-M07-02.24, FR-M07-02.25, FR-M07-02.26, FR-M07-02.27, FR-M07-02.30, BR-M07-01, BR-M07-06, BR-M07-18, BR-M07-21, BR-M07-24, FR-M09-01.19 |
| AUT-M07-002 | Upvote hoặc bỏ upvote trên từng bài/bình luận | Đầu tiên khi không có cửa sổ mở: tạo thông báo ngay, mở [t0, t0+5 phút). Người mới tiếp theo trong cửa sổ cập nhật cùng bản: A mới nhất, N người khác nhau còn lại, unread và lên đầu; không kéo dài cửa sổ. Bỏ upvote giữ thông báo; người đã đếm bỏ rồi upvote lại không đổi/đếm thêm. Mỗi bài/bình luận cửa sổ riêng; tại đúng t0+5 phút mở bản/cửa sổ mới cho lượt tiếp. Không tự khẳng định đẩy lại mọi cập nhật gộp (NOTE02). | FR-M07-02.03, FR-M07-02.04, FR-M07-02.18, FR-M07-02.19, FR-M07-02.20, BR-M07-05 |
| AUT-M07-003 | Thông báo vừa tạo đã được lưu | Đẩy tới mọi thiết bị đang mở ứng dụng của recipient; lỗi thiết bị nào không thử đẩy lại. Bản ghi của người nhận vẫn là nguồn chính khi bấm chuông/mở trang; không nhân bản theo thiết bị hoặc chọn giao thức realtime. Đồng bộ read thời gian thực/biên đồng thời chưa chốt theo NOTE04. | FR-M07-03.01, FR-M07-03.02, FR-M07-03.03, FR-M07-03.04, BR-M07-09, BR-M07-10 |
| AUT-M07-004 | Sự kiện đúng whitelist email từ owner | Đưa một email vào hàng đợi, thao tác gốc hoàn tất không chờ gửi. Chỉ mật khẩu đã đổi (đổi/đặt lại), liên kết Google, cảnh báo tự xóa, ban/gỡ ban, kết luận khiếu nại ban. Email ban có link khiếu nại. Cảnh báo tự xóa chỉ email, đúng một email lúc còn 24 giờ trước DELETED do M01 xác định; không thêm chuông cho cảnh báo này. Không email Chat/cảnh cáo/khiếu nại bài/khiếu nại cảnh cáo hoặc digest. | FR-M07-04.01, FR-M07-04.03, FR-M07-04.04, FR-M07-04.06, FR-M07-04.08, BR-M07-03, BR-M07-04, BR-M07-11, FR-M01-12.05 |
| AUT-M07-005 | Quét hàng đợi email mỗi 60 giây | Gửi email chưa thành công qua ACT-005. Thành công ghi đã gửi; lỗi giữ trong hàng đợi để lần quét kế tiếp gửi lại, tối đa3 lần gửi lại sau lần đầu (tối đa4 lần thử). Lỗi cả3 retry thì dừng, không tự thêm retry thủ công/backoff/xóa hàng đợi. Đây là tác vụ tự động, không BF giao tiếp giữa SYSTEM với dịch vụ email. | FR-M07-04.02, FR-M07-04.09, FR-M07-04.10, BR-M07-11, BR-M07-26 |
| AUT-M07-006 | Bài lần đầu hiển thị công khai từ M03/M11 | Thông báo trong ứng dụng cho từng follower tác giả có quyền xem và đủ điều kiện recipient; không email. Không gửi cho bài ẩn danh, follower ngoài quyền Private, bài bị từ chối/sửa/khôi phục; không dùng follow Topic làm subscription bài mới. M07 không tự chạy quét/duyệt hay tạo sự kiện công bố. | FR-M07-02.21, FR-M07-02.22, FR-M07-02.23, FR-M07-02.24, BR-M07-18, BR-M07-23 |
| AUT-M07-007 | Vòng đời đề xuất từ M10 | Đề xuất mới có thông báo mới; trả lời hiện lựa chọn/khóa chọn lại. Đủ 7×24 giờ mà chưa trả lời: Hết hiệu lực, thông báo Đã hết hạn; đề xuất mới cùng loại/cùng người thay đề xuất cũ cũng khóa lựa chọn cũ nhưng không tự đặt nhãn hết hạn cho lý do thay thế. Không xóa thông báo cũ, không đổi role do thời gian trôi hoặc chỉ có đề xuất mới. | FR-M07-02.14, FR-M07-02.28, FR-M07-02.30, FR-M07-02.31, FR-M07-02.32, BR-M07-20, FR-M10-02.10, FR-M10-07.10 |
| AUT-M07-008 | M16 phát tin mới hoặc dữ liệu unread | Mỗi tin mới hiện một popup cho thành viên đang mở ứng dụng, trừ đang xem đúng cuộc, mute riêng hoặc global mute. Không tạo bản ghi chuông/email Chat. Số cuộc theo read marker/tin được thấy M16 gồm mute; người cũ chỉ tính tin trước lúc rời. Cờ Chat tắt vẫn hiện biểu tượng/số; thao tác Chat khi mở do M16. Không tự thêm retry popup/nội dung popup chưa có nguồn. | FR-M07-02.10, FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, FR-M07-09.07, BR-M07-02, BR-M07-08, BR-M07-28, FR-M16-05.03, FR-M16-07.10 |
| AUT-M07-009 | Rời hoặc bị xóa khỏi nhóm chat theo M16 | Bỏ mute riêng cặp người–nhóm chat. Vào lại bắt đầu Đang nhận ở cấp cuộc, không khôi phục mute cũ; global mute nếu còn bật vẫn chặn popup. Không xóa tin/read marker hoặc đổi cài đặt của cuộc/người khác. | FR-M07-09.08, FR-M07-09.03, FR-M07-09.04, BR-M07-08, FR-M16-07.10 |
| RULE-M07-001 | Kênh/người nhận/quyền | Chỉ các loại BR01/03, đúng owner và quyền Private; không tự nhận sự kiện của mình, không tạo cho DELETED; giữ tạo cho BANNED/DEACTIVATED nhưng quyền xem độc lập. Không Accepted Answer, nhắc Lớp/Khối, thông báo Topic có bài mới, đổi Topic/Tag bởi Mod/Admin, khiếu nại chỉ ADMIN thấy, digest hay cài đặt theo loại. Nhắc tên vẫn chịu quyền/recipient chung và mốc công khai của M01; bảo mật cần làm rõ causer theo GAP001. | FR-M07-02.01, FR-M07-02.02, FR-M07-02.07, FR-M07-02.10, FR-M07-02.11, FR-M07-02.17, FR-M07-02.24, FR-M07-02.25, FR-M07-02.26, FR-M07-02.27, BR-M07-01, BR-M07-03, BR-M07-06, BR-M07-18, BR-M07-21, BR-M07-24 |
| RULE-M07-002 | Lưu/hiện/đọc/mở | Giữ vô thời hạn, lưu UTC và hiện Asia/Ho_Chi_Minh; chuông 10/trang 20 mỗi lần, cập nhật cuối giảm dần, số unread toàn tập không tính Chat. Chỉ xem của mình, Guest bị từ chối, BANNED không xem. Mở danh sách không đọc; click từng thông báo đọc trước kiểm đích, đã đọc giữ nguyên; mark-all chỉ thông báo mình. Đích xóa/ẩn/mất quyền hiện Nội dung không tồn tại vẫn giữ read/bản ghi; ngoại lệ chủ nội dung chỉ đọc thuộc M03/M04. Causer DEACTIVATED/DELETED hiện nhãn đã chốt, không tự đổi thông báo về unread ngoài gộp upvote. | FR-M07-05.01, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.06, FR-M07-05.07, FR-M07-05.09, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, FR-M07-05.13, FR-M07-06.01, FR-M07-06.02, FR-M07-06.03, FR-M07-06.04, FR-M07-06.05, FR-M07-06.06, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-14, BR-M07-22, BR-M07-24, BR-M07-27 |
| RULE-M07-003 | Follow và vòng đời | Chỉ User/Topic; phiên bắt buộc, không tự follow mình hoặc bắt đầu follow BANNED. Quan hệ cũ với BANNED/DEACTIVATED giữ; M01 xóa quan hệ khi DELETED, M05 chuyển/bỏ follow khi gộp/xóa Topic. Unfollow không báo; follow lại không lặp sự kiện của cặp; Topic không sinh thông báo. Chưa tự chốt bắt đầu follow DEACTIVATED ngoài nguồn (GAP002). | FR-M07-01.01, FR-M07-01.02, FR-M07-01.03, FR-M07-01.04, FR-M07-01.08, FR-M07-01.09, FR-M07-01.10, FR-M07-01.11, FR-M07-01.12, FR-M07-01.13, BR-M07-15, BR-M07-25, FR-M01-12.08, FR-M05-07.06, FR-M05-08.06 |
| RULE-M07-004 | Mute Chat, popup và chỉ báo | Popup cần thành viên+đang mở ứng dụng+không xem đúng cuộc+không mute riêng+không global mute. Global chặn mọi cuộc không ngoại lệ; bỏ global giữ per mute; mute không đổi số cuộc unread. Rời/kick nhóm chat reset per mute khi vào lại, global vẫn chi phối. Mark-all chuông không đọc Chat. ACT-003 có quyền cá nhân như User, không xem thông báo hay mốc tin của người khác. | FR-M07-07.02, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, FR-M07-09.01, FR-M07-09.02, FR-M07-09.03, FR-M07-09.04, FR-M07-09.05, FR-M07-09.06, FR-M07-09.07, FR-M07-09.08, BR-M07-02, BR-M07-08, BR-M07-28, FR-M16-07.10 |
| RULE-M07-005 | Mute theo bài | Công tắc mọi bài cho người đăng nhập, không đòi từng tương tác/tác giả. Theo cặp người–bài, chặn4 nhóm: bình luận mới/trả lời/upvote bài/upvote bình luận mình trong bài. Nhắc tên và xử lý khác vẫn theo điều kiện quyền/recipient. Bật lại nhận từ thời điểm đó; không ảnh hưởng người khác hay xóa thông báo cũ, không tự thêm replay sự kiện đã mute. | FR-M07-08.01, FR-M07-08.02, FR-M07-08.03, FR-M07-08.04, FR-M07-08.05, FR-M07-02.07, FR-M07-02.08, FR-M07-02.09, BR-M07-06, BR-M07-07 |


### Danh sách sự kiện và kênh

| Nhóm sự kiện do owner phát | Trong ứng dụng | Email | Giới hạn |
|---|---|---|---|
| Mật khẩu đã đổi (đổi/đặt lại), liên kết Google | Theo yêu cầu nguồn; hợp đồng causer còn GAP001 | Có | Không tự gán causer hoặc ngoại lệ self; M01/M07 cần làm rõ |
| Ban/gỡ ban/kết luận khiếu nại ban | Có; BANNED không được xem chuông khi còn ban | Có; email ban có link khiếu nại | Owner quyết recipient/kết luận; không chờ email |
| Cảnh báo tự xóa tài khoản | Không | Có, đúng một sự kiện24 giờ trước tự DELETED | M01 sở hữu thời điểm và điều kiện; retries là cùng email |
| Follow người lần đầu; bài mới của người đang follow | Có nếu đủ điều kiện | Không | Không lặp follow cùng cặp; không bài ẩn danh/sửa/khôi phục/Topic |
| Bài đăng/từ chối/ẩn/poll kết thúc; comment/reply/mention/upvote | Có theo recipient/quyền/mute/gộp | Không | Mention mốc công khai M01; AI từ chối kèm cảnh cáo gộp theo M09 |
| Kết quả báo cáo, cảnh cáo, khiếu nại bài/cảnh cáo | Có theo owner | Không | Đường khiếu nại nếu xử lý được khiếu nại; không thêm điều kiện owner |
| Nhóm: mời/yêu cầu tham gia/chấp nhận/bổ nhiệm Group Mod/kick/Owner/gỡ bài-comment khỏi nhóm | Có theo recipient và ngoại lệ M11 | Không | Mời dùng link mời; không thay thành đề xuất role hệ thống |
| Badge/mốc điểm (cùng sự kiện), Ngôi sao tuần | Có | Không | Không tạo thông báo mốc điểm thứ hai |
| Đề xuất làm Mod/Admin | Có, hai lựa chọn và vòng đời M10 | Không | Không email mới ngoài whitelist |
| Tin nhắn1-1/nhóm chat | Popup/chỉ báo riêng, không chuông | Không | M16 cấp sự kiện/read marker; mute chỉ popup |
| Topic có bài mới; đổi Topic/Tag của người khác; khiếu nại chỉ ADMIN thấy; nhắc Lớp/Khối | Không | Không | Theo BR21/quyết định không làm; không Accepted Answer/digest |


### Các phép đối soát nghiệp vụ

| Thời điểm/điều kiện giả lập | Hiệu ứng phải có |
|---|---|
| 10:00 Bình upvote P701; 10:01 Lan đã đọc thông báo; 10:02 Chi upvote P701 | N900 mở ngay10:00, cửa sổ tới trước 10:05; cập nhật N900 thành Chi và 1 người khác, unread và lên đầu, không kéo dài cửa sổ |
| 10:03 Bình bỏ rồi upvote lại P701 trong cùng cửa sổ | Không đổi/đếm thêm Bình; vẫn giữ N900 và số người đã đếm |
| 10:04 Dũng upvote C701; 10:05:00 Em upvote P701 | C701 có thông báo/cửa sổ riêng; P701 đã hết cửa sổ cũ nên Em mở thông báo mới, không xóa N900 |
| Email ban lỗi ở quét10:01; lỗi tiếp10:02/10:03/10:04 | Lần đầu+3 retry=4 lần; không gửi tiếp10:05, không bắt thao tác ban chờ gửi |
| C71 mute riêng, C72 đang nhận; global=false→true→false | C71 vẫn mute ở cả3 trạng thái; C72 chỉ có thể popup khi global=false và đủ điều kiện; badge 3 không đổi vì đổi mute |
| C72 mute, Lan rời/kick rồi vào lại; global vẫn=true | Xóa per mute khi rời, vào lại per Đang nhận nhưng global vẫn chặn popup, không tự khôi phục mute cũ |
| N011 ngoài 10 mục chuông nhưng unread; Lan mark-all | N011 vẫn thành read; tổng 3→0; Chat vẫn3 cuộc |
| Tài khoản nhận BANNED/DEACTIVATED/DELETED; causer khác recipient | Hai trạng thái đầu vẫn tạo, DELETED không tạo; quyền xem BANNED độc lập. Causer trùng recipient bị lọc với sự kiện đã xác định causer; bảo mật còn GAP001 |


Bảng quy tắc/đối soát mô tả phản ứng theo sự kiện, không là scenario sáu phần của scheduler hoặc dịch vụ email. Không dùng step actor giả để biến quá trình tự động thành BF.

## 6. Truy vết và ma trận quyết định

| Mã hiệu lực | SC/bước/nhánh/quy tắc | Mức đối soát |
|---|---|---|
| FR-M07-01 | SC-M07-001/M1; SC-M07-001/M2; SC-M07-001/E1.1; SC-M07-001/E1.2; SC-M07-001/E2.1; SC-M07-001/E9.1; SC-M07-001/E9.2; RULE-M07-003; SC-M07-001/E6.1; SC-M07-001/E7.1; SC-M07-002/M2; SC-M07-002/E5.2; SC-M07-001/E3.1; SC-M07-001/E4.1; SC-M07-001/E5.1; SC-M07-001/E8.1; SC-M07-001/E8.2; SC-M07-002/E4.1; SC-M07-002/E4.2; SC-M07-002/M1; SC-M07-002/E1.1; SC-M07-002/E1.2; SC-M07-002/E2.1; SC-M07-002/E3.1; SC-M07-002/E5.1 | Có vị trí; chưa phê duyệt |
| FR-M07-02 | SC-M07-001/M2; SC-M07-001/E9.2; AUT-M07-001; RULE-M07-001; SC-M07-001/E1.2; AUT-M07-006; SC-M07-003/E6.1; AUT-M07-002; SC-M07-003/E7.1; SC-M07-003/E8.1; SC-M07-006/M2; SC-M07-006/E2.1; SC-M07-006/E2.2; SC-M07-006/E14.1; SC-M07-006/E14.2; AUT-M07-007; SC-M07-006/M3; SC-M07-006/M4; SC-M07-006/E2.3; SC-M07-006/E2.4; SC-M07-006/E14.3; SC-M07-006/E14.4; SC-M07-006/E1.1; SC-M07-006/E1.2; SC-M07-006/E3.1; SC-M07-006/E8.2; SC-M07-006/E5.1; SC-M07-006/E10.2; SC-M07-006/E4.1; SC-M07-006/E9.2; SC-M07-008/M4; SC-M07-008/E3.4; RULE-M07-005; AUT-M07-008 | Có vị trí; chưa phê duyệt |
| FR-M07-03 | SC-M07-001/M2; SC-M07-001/E9.2; AUT-M07-003; SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2 | Có vị trí; chưa phê duyệt |
| FR-M07-04 | AUT-M07-004; AUT-M07-005 | Có vị trí; chưa phê duyệt |
| FR-M07-05 | SC-M07-003/M1; SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E2.1; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2; RULE-M07-002; SC-M07-003/E1.1; SC-M07-003/E1.3; SC-M07-003/E1.4; SC-M07-003/E1.5; SC-M07-003/E1.6; SC-M07-006/M1; SC-M07-006/E2.1; SC-M07-006/E8.1; SC-M07-006/E9.1; SC-M07-006/E10.1; SC-M07-006/E14.1; SC-M07-004/M2; SC-M07-004/E1.1; SC-M07-004/E5.2; SC-M07-004/E6.2; SC-M07-004/E7.1; SC-M07-004/E10.2; SC-M07-005/M2; SC-M07-005/E1.1; SC-M07-005/E2.1; SC-M07-005/E5.2; SC-M07-006/E8.2; SC-M07-006/E9.2; SC-M07-006/E10.2; SC-M07-006/E11.1; SC-M07-003/E8.1; SC-M07-004/E8.1; SC-M07-005/E3.1; SC-M07-003/E9.1; SC-M07-003/E9.2; SC-M07-004/E9.1; SC-M07-004/E9.2; SC-M07-006/E13.1; SC-M07-006/E13.2; SC-M07-004/E2.1; SC-M07-004/E3.1; SC-M07-004/E4.1; SC-M07-004/E5.1; SC-M07-004/E6.1 | Có vị trí; chưa phê duyệt |
| FR-M07-06 | SC-M07-004/M1; SC-M07-004/M2; SC-M07-004/E2.1; SC-M07-004/E3.1; SC-M07-004/E4.1; SC-M07-004/E5.1; SC-M07-004/E5.2; SC-M07-004/E6.1; SC-M07-004/E6.2; SC-M07-004/E10.1; SC-M07-004/E10.2; RULE-M07-002; SC-M07-004/E1.1; SC-M07-004/E9.1; SC-M07-004/E9.2; SC-M07-005/M2; SC-M07-005/E3.1; SC-M07-005/E4.1; SC-M07-005/E4.2; SC-M07-005/E5.2; SC-M07-005/M1; SC-M07-005/E1.1; SC-M07-005/E5.1 | Có vị trí; chưa phê duyệt |
| FR-M07-07 | SC-M07-007/M1; SC-M07-007/M2; SC-M07-007/E1.1; SC-M07-007/E2.1; SC-M07-007/E3.1; SC-M07-007/E5.1; SC-M07-007/E7.1; SC-M07-007/E7.2; AUT-M07-008; SC-M07-007/E4.1; RULE-M07-004; SC-M07-007/E1.2; SC-M07-007/E1.3; SC-M07-007/E6.1; SC-M07-007/E6.2; SC-M07-009/M2; SC-M07-009/E1.2; SC-M07-009/E2.2; SC-M07-009/E3.2; SC-M07-009/E6.2; SC-M07-010/M2; SC-M07-010/E1.2; SC-M07-010/E3.2 | Có vị trí; chưa phê duyệt |
| FR-M07-08 | SC-M07-008/M1; SC-M07-008/M2; SC-M07-008/M4; SC-M07-008/E1.1; SC-M07-008/E3.1; SC-M07-008/E3.2; SC-M07-008/E3.4; RULE-M07-005; SC-M07-008/M3; SC-M07-008/E3.3; SC-M07-008/E1.2; SC-M07-008/E1.3; SC-M07-008/E2.1; SC-M07-008/E2.2 | Có vị trí; chưa phê duyệt |
| FR-M07-09 | SC-M07-007/M2; SC-M07-007/E1.1; SC-M07-007/E2.1; SC-M07-007/E3.1; SC-M07-007/E5.1; SC-M07-007/E7.2; SC-M07-009/M2; SC-M07-009/E1.2; SC-M07-009/E2.2; SC-M07-009/E3.2; SC-M07-009/E6.2; SC-M07-010/M2; SC-M07-010/E1.2; SC-M07-010/E3.2; AUT-M07-008; RULE-M07-004; SC-M07-010/M1; SC-M07-010/E3.1; AUT-M07-009; SC-M07-009/M1; SC-M07-009/E3.1; SC-M07-009/E6.1; SC-M07-009/E1.1; SC-M07-009/E2.1; SC-M07-009/E4.1; SC-M07-009/E5.1; SC-M07-009/E5.2; SC-M07-010/E2.1; SC-M07-010/E2.2; SC-M07-010/E1.1 | Có vị trí; chưa phê duyệt |
| FR-M07-01.01 | SC-M07-001/M1; SC-M07-001/M2; SC-M07-001/E1.1; SC-M07-001/E1.2; SC-M07-001/E2.1; SC-M07-001/E9.1; SC-M07-001/E9.2; RULE-M07-003 | Có vị trí; chưa phê duyệt |
| FR-M07-01.02 | SC-M07-001/E3.1; SC-M07-001/E4.1; SC-M07-001/E5.1; RULE-M07-003 | Có vị trí; chưa phê duyệt |
| FR-M07-01.03 | SC-M07-001/E8.1; SC-M07-001/E8.2; SC-M07-002/E4.1; SC-M07-002/E4.2; RULE-M07-003 | Có vị trí; chưa phê duyệt |
| FR-M07-01.04 | SC-M07-001/M2; SC-M07-001/E9.2; RULE-M07-003 | Có vị trí; chưa phê duyệt |
| FR-M07-01.08 | SC-M07-002/M1; SC-M07-002/M2; SC-M07-002/E1.1; SC-M07-002/E1.2; SC-M07-002/E2.1; SC-M07-002/E3.1; SC-M07-002/E5.1; SC-M07-002/E5.2; RULE-M07-003 | Có vị trí; chưa phê duyệt |
| FR-M07-01.09 | SC-M07-002/M2; SC-M07-002/E1.2; SC-M07-002/E2.1; SC-M07-002/E3.1; SC-M07-002/E5.2; RULE-M07-003 | Có vị trí; chưa phê duyệt |
| FR-M07-01.10 | SC-M07-001/E2.1; SC-M07-002/M2; SC-M07-002/E5.2; RULE-M07-003 | Có vị trí; chưa phê duyệt |
| FR-M07-01.11 | SC-M07-001/M2; SC-M07-001/E6.1; SC-M07-001/E9.2; RULE-M07-003 | Có vị trí; chưa phê duyệt |
| FR-M07-01.12 | SC-M07-001/M2; SC-M07-001/E7.1; SC-M07-001/E9.2; RULE-M07-003 | Có vị trí; chưa phê duyệt; GAP002 ở bắt đầu follow DEACTIVATED |
| FR-M07-01.13 | SC-M07-002/E2.1; SC-M07-002/E3.1; RULE-M07-003 | Có vị trí; chưa phê duyệt |
| FR-M07-02.01 | SC-M07-001/M2; SC-M07-001/E9.2; AUT-M07-001; RULE-M07-001 | Có vị trí; chưa phê duyệt |
| FR-M07-02.02 | SC-M07-001/M2; SC-M07-001/E9.2; AUT-M07-001; RULE-M07-001 | Có vị trí; chưa phê duyệt |
| FR-M07-02.03 | SC-M07-003/E6.1; AUT-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-02.04 | SC-M07-003/E6.1; AUT-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-02.07 | SC-M07-008/M4; SC-M07-008/E3.4; AUT-M07-001; RULE-M07-001; RULE-M07-005 | Có vị trí; chưa phê duyệt |
| FR-M07-02.08 | SC-M07-008/M4; SC-M07-008/E3.4; AUT-M07-001; RULE-M07-005 | Có vị trí; chưa phê duyệt |
| FR-M07-02.09 | SC-M07-008/M4; SC-M07-008/E3.4; AUT-M07-001; RULE-M07-005 | Có vị trí; chưa phê duyệt |
| FR-M07-02.10 | AUT-M07-001; AUT-M07-008; RULE-M07-001 | Có vị trí; chưa phê duyệt |
| FR-M07-02.11 | AUT-M07-001; RULE-M07-001 | Có vị trí; chưa phê duyệt |
| FR-M07-02.13 | AUT-M07-001 | Có vị trí; chưa phê duyệt |
| FR-M07-02.14 | SC-M07-006/M2; SC-M07-006/E2.1; SC-M07-006/E2.2; SC-M07-006/E14.1; SC-M07-006/E14.2; AUT-M07-001; AUT-M07-007 | Có vị trí; chưa phê duyệt |
| FR-M07-02.15 | SC-M07-006/M2; SC-M07-006/M3; SC-M07-006/M4; SC-M07-006/E2.2; SC-M07-006/E2.3; SC-M07-006/E2.4; SC-M07-006/E14.2; SC-M07-006/E14.3; SC-M07-006/E14.4 | Có vị trí; chưa phê duyệt |
| FR-M07-02.16 | SC-M07-006/M2; SC-M07-006/E1.1; SC-M07-006/E1.2; SC-M07-006/E2.2; SC-M07-006/E14.2 | Có vị trí; chưa phê duyệt |
| FR-M07-02.17 | AUT-M07-001; RULE-M07-001 | Có vị trí; chưa phê duyệt |
| FR-M07-02.18 | SC-M07-003/E6.1; AUT-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-02.19 | AUT-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-02.20 | SC-M07-003/E6.1; AUT-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-02.21 | AUT-M07-006 | Có vị trí; chưa phê duyệt |
| FR-M07-02.22 | AUT-M07-006 | Có vị trí; chưa phê duyệt |
| FR-M07-02.23 | AUT-M07-006 | Có vị trí; chưa phê duyệt |
| FR-M07-02.24 | SC-M07-001/E1.2; AUT-M07-001; AUT-M07-006; RULE-M07-001 | Có vị trí; chưa phê duyệt |
| FR-M07-02.25 | SC-M07-001/M2; SC-M07-001/E9.2; AUT-M07-001; RULE-M07-001 | Có vị trí; chưa phê duyệt; GAP001 ở causer bảo mật |
| FR-M07-02.26 | SC-M07-003/E7.1; SC-M07-003/E8.1; AUT-M07-001; RULE-M07-001 | Có vị trí; chưa phê duyệt |
| FR-M07-02.27 | AUT-M07-001; RULE-M07-001 | Có vị trí; chưa phê duyệt |
| FR-M07-02.28 | SC-M07-006/M2; SC-M07-006/M4; SC-M07-006/E1.2; SC-M07-006/E2.2; SC-M07-006/E2.4; SC-M07-006/E3.1; SC-M07-006/E8.2; SC-M07-006/E14.2; SC-M07-006/E14.4; AUT-M07-007 | Có vị trí; chưa phê duyệt |
| FR-M07-02.30 | SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E5.1; SC-M07-006/E10.2; SC-M07-006/E14.2; AUT-M07-001; AUT-M07-007 | Có vị trí; chưa phê duyệt |
| FR-M07-02.31 | SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E4.1; SC-M07-006/E9.2; SC-M07-006/E14.2; AUT-M07-007 | Có vị trí; chưa phê duyệt |
| FR-M07-02.32 | SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E5.1; SC-M07-006/E10.2; SC-M07-006/E14.2; AUT-M07-007 | Có vị trí; chưa phê duyệt |
| FR-M07-03.01 | SC-M07-001/M2; SC-M07-001/E9.2; AUT-M07-003 | Có vị trí; chưa phê duyệt |
| FR-M07-03.02 | SC-M07-001/M2; SC-M07-001/E9.2; AUT-M07-003 | Có vị trí; chưa phê duyệt |
| FR-M07-03.03 | SC-M07-003/E3.1; AUT-M07-003 | Có vị trí; chưa phê duyệt |
| FR-M07-03.04 | SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2; AUT-M07-003 | Có vị trí; chưa phê duyệt |
| FR-M07-04.01 | AUT-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-04.02 | AUT-M07-005 | Có vị trí; chưa phê duyệt |
| FR-M07-04.03 | AUT-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-04.04 | AUT-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-04.06 | AUT-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-04.08 | AUT-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-04.09 | AUT-M07-005 | Có vị trí; chưa phê duyệt |
| FR-M07-04.10 | AUT-M07-005 | Có vị trí; chưa phê duyệt |
| FR-M07-05.01 | SC-M07-003/M1; SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E2.1; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-05.02 | SC-M07-003/M2; SC-M07-003/E1.1; SC-M07-003/E1.2; SC-M07-003/E1.3; SC-M07-003/E1.4; SC-M07-003/E1.5; SC-M07-003/E1.6; SC-M07-003/E2.1; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.2; SC-M07-006/M1; SC-M07-006/M2; SC-M07-006/E2.1; SC-M07-006/E2.2; SC-M07-006/E8.1; SC-M07-006/E9.1; SC-M07-006/E10.1; SC-M07-006/E14.1; SC-M07-006/E14.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-05.03 | SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E1.4; SC-M07-003/E1.6; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-05.04 | SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E1.4; SC-M07-003/E1.6; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-05.05 | SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E1.4; SC-M07-003/E1.6; SC-M07-003/E2.1; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.2; SC-M07-004/M2; SC-M07-004/E1.1; SC-M07-004/E5.2; SC-M07-004/E6.2; SC-M07-004/E7.1; SC-M07-004/E10.2; SC-M07-005/M2; SC-M07-005/E1.1; SC-M07-005/E2.1; SC-M07-005/E5.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E8.2; SC-M07-006/E9.2; SC-M07-006/E10.2; SC-M07-006/E11.1; SC-M07-006/E14.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-05.06 | SC-M07-003/E9.1; SC-M07-003/E9.2; SC-M07-004/E9.1; SC-M07-004/E9.2; SC-M07-006/E13.1; SC-M07-006/E13.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-05.07 | SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E1.4; SC-M07-003/E1.6; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-05.09 | SC-M07-003/E7.1; SC-M07-003/E8.1; SC-M07-004/E8.1; SC-M07-005/E3.1; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-05.10 | SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E2.1; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-05.11 | SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-05.12 | SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-05.13 | SC-M07-004/M2; SC-M07-004/E2.1; SC-M07-004/E3.1; SC-M07-004/E4.1; SC-M07-004/E5.1; SC-M07-004/E5.2; SC-M07-004/E6.1; SC-M07-004/E6.2; SC-M07-004/E10.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-06.01 | SC-M07-004/M1; SC-M07-004/M2; SC-M07-004/E2.1; SC-M07-004/E3.1; SC-M07-004/E4.1; SC-M07-004/E5.1; SC-M07-004/E5.2; SC-M07-004/E6.1; SC-M07-004/E6.2; SC-M07-004/E10.1; SC-M07-004/E10.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-06.02 | SC-M07-004/M1; SC-M07-004/M2; SC-M07-004/E1.1; SC-M07-004/E5.1; SC-M07-004/E5.2; SC-M07-004/E6.1; SC-M07-004/E6.2; SC-M07-004/E10.1; SC-M07-004/E10.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-06.03 | SC-M07-005/M1; SC-M07-005/M2; SC-M07-005/E1.1; SC-M07-005/E5.1; SC-M07-005/E5.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-06.04 | SC-M07-004/M2; SC-M07-004/E1.1; SC-M07-004/E5.2; SC-M07-004/E6.2; SC-M07-004/E10.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-06.05 | SC-M07-005/M2; SC-M07-005/E1.1; SC-M07-005/E5.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-06.06 | SC-M07-004/E9.1; SC-M07-004/E9.2; SC-M07-005/M2; SC-M07-005/E3.1; SC-M07-005/E4.1; SC-M07-005/E4.2; SC-M07-005/E5.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| FR-M07-07.01 | SC-M07-007/M1; SC-M07-007/M2; SC-M07-007/E1.1; SC-M07-007/E2.1; SC-M07-007/E3.1; SC-M07-007/E5.1; SC-M07-007/E7.1; SC-M07-007/E7.2; AUT-M07-008 | Có vị trí; chưa phê duyệt |
| FR-M07-07.02 | SC-M07-007/M1; SC-M07-007/M2; SC-M07-007/E1.1; SC-M07-007/E2.1; SC-M07-007/E3.1; SC-M07-007/E4.1; SC-M07-007/E5.1; SC-M07-007/E7.1; SC-M07-007/E7.2; AUT-M07-008; RULE-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-07.03 | SC-M07-007/M2; SC-M07-007/E1.1; SC-M07-007/E1.2; SC-M07-007/E1.3; SC-M07-007/E2.1; SC-M07-007/E3.1; SC-M07-007/E5.1; SC-M07-007/E7.2; AUT-M07-008 | Có vị trí; chưa phê duyệt |
| FR-M07-07.04 | SC-M07-007/M2; SC-M07-007/E1.1; SC-M07-007/E2.1; SC-M07-007/E3.1; SC-M07-007/E5.1; SC-M07-007/E6.1; SC-M07-007/E6.2; SC-M07-007/E7.2; AUT-M07-008 | Có vị trí; chưa phê duyệt |
| FR-M07-07.05 | SC-M07-009/M2; SC-M07-009/E1.2; SC-M07-009/E2.2; SC-M07-009/E3.2; SC-M07-009/E6.2; SC-M07-010/M2; SC-M07-010/E1.2; SC-M07-010/E3.2; AUT-M07-008; RULE-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-07.06 | SC-M07-009/M2; SC-M07-009/E1.2; SC-M07-009/E2.2; SC-M07-009/E3.2; SC-M07-009/E6.2; SC-M07-010/M2; SC-M07-010/E1.2; SC-M07-010/E3.2; AUT-M07-008; RULE-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-07.07 | SC-M07-009/M2; SC-M07-009/E1.2; SC-M07-009/E2.2; SC-M07-009/E3.2; SC-M07-009/E6.2; SC-M07-010/M2; SC-M07-010/E1.2; SC-M07-010/E3.2; AUT-M07-008; RULE-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-08.01 | SC-M07-008/M1; SC-M07-008/M2; SC-M07-008/M4; SC-M07-008/E1.1; SC-M07-008/E3.1; SC-M07-008/E3.2; SC-M07-008/E3.4; RULE-M07-005 | Có vị trí; chưa phê duyệt |
| FR-M07-08.02 | SC-M07-008/M3; SC-M07-008/M4; SC-M07-008/E3.3; SC-M07-008/E3.4; RULE-M07-005 | Có vị trí; chưa phê duyệt |
| FR-M07-08.03 | SC-M07-008/M4; SC-M07-008/E1.2; SC-M07-008/E1.3; SC-M07-008/E3.4; RULE-M07-005 | Có vị trí; chưa phê duyệt |
| FR-M07-08.04 | SC-M07-008/M4; SC-M07-008/E1.3; SC-M07-008/E3.4; RULE-M07-005 | Có vị trí; chưa phê duyệt |
| FR-M07-08.05 | SC-M07-008/E2.1; SC-M07-008/E2.2; RULE-M07-005 | Có vị trí; chưa phê duyệt |
| FR-M07-09.01 | SC-M07-009/M1; SC-M07-009/M2; SC-M07-009/E3.1; SC-M07-009/E3.2; SC-M07-009/E6.1; SC-M07-009/E6.2; RULE-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-09.02 | SC-M07-009/M2; SC-M07-009/E1.1; SC-M07-009/E1.2; SC-M07-009/E2.1; SC-M07-009/E2.2; SC-M07-009/E3.2; SC-M07-009/E6.2; RULE-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-09.03 | SC-M07-007/E2.1; SC-M07-009/E1.2; SC-M07-009/E2.2; SC-M07-010/M1; SC-M07-010/M2; SC-M07-010/E3.1; SC-M07-010/E3.2; AUT-M07-009; RULE-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-09.04 | SC-M07-010/M2; SC-M07-010/E1.1; SC-M07-010/E1.2; SC-M07-010/E3.2; AUT-M07-009; RULE-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-09.05 | SC-M07-009/M2; SC-M07-009/E3.2; SC-M07-009/E4.1; SC-M07-009/E6.2; RULE-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-09.06 | SC-M07-009/E5.1; SC-M07-009/E5.2; SC-M07-010/E2.1; SC-M07-010/E2.2; RULE-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-09.07 | SC-M07-007/M2; SC-M07-007/E1.1; SC-M07-007/E2.1; SC-M07-007/E3.1; SC-M07-007/E5.1; SC-M07-007/E7.2; SC-M07-009/M2; SC-M07-009/E1.2; SC-M07-009/E2.2; SC-M07-009/E3.2; SC-M07-009/E6.2; SC-M07-010/M2; SC-M07-010/E1.2; SC-M07-010/E3.2; AUT-M07-008; RULE-M07-004 | Có vị trí; chưa phê duyệt |
| FR-M07-09.08 | AUT-M07-009; RULE-M07-004 | Có vị trí; chưa phê duyệt |
| BR-M07-01 | AUT-M07-001; RULE-M07-001 | Có vị trí; chưa phê duyệt; GAP001 ở causer bảo mật |
| BR-M07-02 | SC-M07-003/E2.1; SC-M07-007/M2; SC-M07-007/E1.1; SC-M07-007/E1.3; SC-M07-007/E2.1; SC-M07-007/E3.1; SC-M07-007/E4.1; SC-M07-007/E5.1; SC-M07-007/E7.2; AUT-M07-008; RULE-M07-004 | Có vị trí; chưa phê duyệt |
| BR-M07-03 | AUT-M07-004; RULE-M07-001 | Có vị trí; chưa phê duyệt; GAP001 ở causer bảo mật |
| BR-M07-04 | AUT-M07-004 | Có vị trí; chưa phê duyệt |
| BR-M07-05 | SC-M07-003/E6.1; AUT-M07-002 | Có vị trí; chưa phê duyệt |
| BR-M07-06 | SC-M07-008/M4; SC-M07-008/E3.4; AUT-M07-001; RULE-M07-001; RULE-M07-005 | Có vị trí; chưa phê duyệt |
| BR-M07-07 | SC-M07-008/M4; SC-M07-008/E1.3; SC-M07-008/E3.4; RULE-M07-005 | Có vị trí; chưa phê duyệt |
| BR-M07-08 | SC-M07-007/M2; SC-M07-007/E1.1; SC-M07-007/E2.1; SC-M07-007/E3.1; SC-M07-007/E5.1; SC-M07-007/E7.2; SC-M07-009/M2; SC-M07-009/E1.2; SC-M07-009/E2.2; SC-M07-009/E3.2; SC-M07-009/E6.2; SC-M07-010/M2; SC-M07-010/E1.2; SC-M07-010/E3.2; AUT-M07-008; AUT-M07-009; RULE-M07-004 | Có vị trí; chưa phê duyệt |
| BR-M07-09 | SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2; AUT-M07-003; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| BR-M07-10 | AUT-M07-003 | Có vị trí; chưa phê duyệt |
| BR-M07-11 | AUT-M07-004; AUT-M07-005 | Có vị trí; chưa phê duyệt |
| BR-M07-12 | SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E1.4; SC-M07-003/E1.6; SC-M07-003/E2.1; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| BR-M07-13 | SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E1.4; SC-M07-003/E1.6; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| BR-M07-14 | SC-M07-004/M2; SC-M07-004/E1.1; SC-M07-004/E5.2; SC-M07-004/E6.2; SC-M07-004/E10.2; SC-M07-005/M2; SC-M07-005/E1.1; SC-M07-005/E5.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| BR-M07-15 | SC-M07-001/M2; SC-M07-001/E1.2; SC-M07-001/E3.1; SC-M07-001/E4.1; SC-M07-001/E5.1; SC-M07-001/E6.1; SC-M07-001/E7.1; SC-M07-001/E9.2; SC-M07-002/E2.1; SC-M07-002/E3.1; RULE-M07-003 | Có vị trí; chưa phê duyệt; GAP002 ở bắt đầu follow DEACTIVATED |
| BR-M07-18 | AUT-M07-001; AUT-M07-006; RULE-M07-001 | Có vị trí; chưa phê duyệt |
| BR-M07-20 | SC-M07-006/M2; SC-M07-006/M4; SC-M07-006/E1.2; SC-M07-006/E2.2; SC-M07-006/E2.4; SC-M07-006/E4.1; SC-M07-006/E5.1; SC-M07-006/E9.2; SC-M07-006/E10.2; SC-M07-006/E14.2; SC-M07-006/E14.4; AUT-M07-007 | Có vị trí; chưa phê duyệt |
| BR-M07-21 | AUT-M07-001; RULE-M07-001 | Có vị trí; chưa phê duyệt |
| BR-M07-22 | SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E1.4; SC-M07-003/E1.6; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| BR-M07-23 | AUT-M07-006 | Có vị trí; chưa phê duyệt |
| BR-M07-24 | SC-M07-001/M2; SC-M07-001/E9.2; SC-M07-003/M2; SC-M07-003/E1.2; SC-M07-003/E3.1; SC-M07-003/E4.1; SC-M07-003/E5.1; SC-M07-003/E6.1; SC-M07-003/E7.1; SC-M07-003/E8.1; SC-M07-003/E10.2; SC-M07-006/M2; SC-M07-006/E2.2; SC-M07-006/E14.2; AUT-M07-001; RULE-M07-001; RULE-M07-002 | Có vị trí; chưa phê duyệt; GAP001 ở causer bảo mật |
| BR-M07-25 | SC-M07-001/M2; SC-M07-001/E2.1; SC-M07-001/E9.2; SC-M07-002/M2; SC-M07-002/E1.2; SC-M07-002/E2.1; SC-M07-002/E3.1; SC-M07-002/E5.2; RULE-M07-003 | Có vị trí; chưa phê duyệt |
| BR-M07-26 | AUT-M07-005 | Có vị trí; chưa phê duyệt |
| BR-M07-27 | SC-M07-004/M2; SC-M07-004/E2.1; SC-M07-004/E3.1; SC-M07-004/E4.1; SC-M07-004/E5.2; SC-M07-004/E6.2; SC-M07-004/E10.2; RULE-M07-002 | Có vị trí; chưa phê duyệt |
| BR-M07-28 | SC-M07-009/M2; SC-M07-009/E1.2; SC-M07-009/E2.2; SC-M07-009/E3.2; SC-M07-009/E6.2; SC-M07-010/M2; SC-M07-010/E1.2; SC-M07-010/E3.2; AUT-M07-008; RULE-M07-004 | Có vị trí; chưa phê duyệt |


| Mã đã bỏ | Cách xử lý |
|---|---|
| BR-M07-16 | Không tính vào122 mã hiệu lực, không khôi phục; xem owner và lý do bỏ trong FR/US |
| BR-M07-17 | Không tính vào122 mã hiệu lực, không khôi phục; xem owner và lý do bỏ trong FR/US |
| BR-M07-19 | Không tính vào122 mã hiệu lực, không khôi phục; xem owner và lý do bỏ trong FR/US |
| FR-M07-01.05 | Không tính vào122 mã hiệu lực, không khôi phục; xem owner và lý do bỏ trong FR/US |
| FR-M07-01.06 | Không tính vào122 mã hiệu lực, không khôi phục; xem owner và lý do bỏ trong FR/US |
| FR-M07-01.07 | Không tính vào122 mã hiệu lực, không khôi phục; xem owner và lý do bỏ trong FR/US |
| FR-M07-02.05 | Không tính vào122 mã hiệu lực, không khôi phục; xem owner và lý do bỏ trong FR/US |
| FR-M07-02.06 | Không tính vào122 mã hiệu lực, không khôi phục; xem owner và lý do bỏ trong FR/US |
| FR-M07-02.12 | Không tính vào122 mã hiệu lực, không khôi phục; xem owner và lý do bỏ trong FR/US |
| FR-M07-02.29 | Không tính vào122 mã hiệu lực, không khôi phục; xem owner và lý do bỏ trong FR/US |
| FR-M07-04.05 | Không tính vào122 mã hiệu lực, không khôi phục; xem owner và lý do bỏ trong FR/US |
| FR-M07-04.07 | Không tính vào122 mã hiệu lực, không khôi phục; xem owner và lý do bỏ trong FR/US |
| FR-M07-05.08 | Không tính vào122 mã hiệu lực, không khôi phục; xem owner và lý do bỏ trong FR/US |


| UC owner | Guard/lựa chọn | Nhánh | Đích |
|---|---|---|---|
| UC-M07-001 | Lan chọn theo dõi Topic thay người dùng | SC-M07-001/E1 | END:SUCCESS |
| UC-M07-001 | Theo dõi lại Bình sau khi đã bỏ theo dõi và cặp này đã từng được báo | SC-M07-001/E2 | END:SUCCESS |
| UC-M07-001 | Target là Tag | SC-M07-001/E3 | END:REJECTED |
| UC-M07-001 | Target là Group | SC-M07-001/E4 | END:REJECTED |
| UC-M07-001 | Target là bài viết | SC-M07-001/E5 | END:REJECTED |
| UC-M07-001 | Theo dõi chính mình | SC-M07-001/E6 | END:REJECTED |
| UC-M07-001 | Bắt đầu theo dõi tài khoản BANNED | SC-M07-001/E7 | END:REJECTED |
| UC-M07-002 | Lan bỏ theo dõi Topic đang theo dõi | SC-M07-002/E1 | END:SUCCESS |
| UC-M07-002 | Target đã chuyển BANNED nhưng quan hệ cũ vẫn còn | SC-M07-002/E2 | END:SUCCESS |
| UC-M07-002 | Target đã chuyển DEACTIVATED nhưng quan hệ cũ vẫn còn | SC-M07-002/E3 | END:SUCCESS |
| UC-M07-003 | Xem trang Thông báo và tải tới thông báo cũ nhất | SC-M07-003/E1 | END:SUCCESS |
| UC-M07-003 | Chưa có thông báo được lưu | SC-M07-003/E2 | END:SUCCESS |
| UC-M07-003 | Đẩy trước đó tới thiết bị hiện tại đã thất bại | SC-M07-003/E3 | END:SUCCESS |
| UC-M07-003 | Người gây N001 chuyển DEACTIVATED | SC-M07-003/E4 | END:SUCCESS |
| UC-M07-003 | Người gây N001 chuyển DELETED | SC-M07-003/E5 | END:SUCCESS |
| UC-M07-003 | Thông báo upvote đã đọc được gộp thêm trong cửa sổ5 phút | SC-M07-003/E6 | END:SUCCESS |
| UC-M07-003 | Lan ACTIVE trở lại sau thời gian DEACTIVATED hoặc BANNED | SC-M07-003/E7 | END:SUCCESS |
| UC-M07-003 | Người yêu cầu đang BANNED | SC-M07-003/E8 | END:REJECTED |
| UC-M07-004 | N003 vốn đã đọc | SC-M07-004/E1 | END:SUCCESS |
| UC-M07-004 | Đích không khả dụng: nội dung đã bị xóa | SC-M07-004/E2 | END:REJECTED |
| UC-M07-004 | Đích không khả dụng: nội dung bị ẩn, người mở không thuộc ngoại lệ chủ nội dung | SC-M07-004/E3 | END:REJECTED |
| UC-M07-004 | Đích không khả dụng: Lan rời nhóm Private nên không còn quyền xem đích | SC-M07-004/E4 | END:REJECTED |
| UC-M07-004 | Chủ bài mở thông báo kết quả xử lý về bài đã xóa hẳn của mình | SC-M07-004/E5 | END:SUCCESS |
| UC-M07-004 | Tác giả mở thông báo bình luận của mình bị ẩn | SC-M07-004/E6 | END:SUCCESS |
| UC-M07-004 | Yêu cầu trỏ thông báo của người khác | SC-M07-004/E7 | END:REJECTED |
| UC-M07-004 | Lan đang BANNED | SC-M07-004/E8 | END:REJECTED |
| UC-M07-005 | Tập thông báo đã đọc hết hoặc rỗng | SC-M07-005/E1 | END:SUCCESS |
| UC-M07-005 | Yêu cầu muốn đánh dấu dữ liệu của người khác | SC-M07-005/E2 | END:REJECTED |
| UC-M07-005 | Tài khoản không được truy cập thông báo vì BANNED | SC-M07-005/E3 | END:REJECTED |
| UC-M07-006 | Người nhận chọn Từ chối đề xuất còn hiệu lực | SC-M07-006/E1 | END:SUCCESS |
| UC-M07-006 | Người dùng USER chấp nhận đề xuất làm Admin do ADMIN gốc gửi | SC-M07-006/E2 | END:SUCCESS |
| UC-M07-006 | Đề xuất đã được trả lời sau lúc hiển thị, trước xử lý lựa chọn mới | SC-M07-006/E3 | END:REJECTED |
| UC-M07-006 | Đề xuất hết hạn sau lúc hiển thị, trước xử lý lựa chọn | SC-M07-006/E4 | END:REJECTED |
| UC-M07-006 | Đề xuất cũ bị thay sau lúc hiển thị, trước xử lý lựa chọn | SC-M07-006/E5 | END:REJECTED |
| UC-M07-006 | Vai trò không còn hợp lệ ở lúc chấp nhận | SC-M07-006/E6 | END:REJECTED |
| UC-M07-006 | Tài khoản không còn ACTIVE tại lúc chấp nhận | SC-M07-006/E7 | END:REJECTED |
| UC-M07-006 | Đề xuất đã trả lời trước khi mở danh sách | SC-M07-006/E8 | END:REJECTED |
| UC-M07-006 | Đề xuất đã hết hạn trước khi mở danh sách | SC-M07-006/E9 | END:REJECTED |
| UC-M07-006 | Đề xuất đã bị thay thế trước khi mở danh sách | SC-M07-006/E10 | END:REJECTED |
| UC-M07-006 | Thông báo đề xuất không thuộc người đang xem | SC-M07-006/E11 | END:REJECTED |
| UC-M07-006 | Người gửi lựa chọn khác người được đề xuất | SC-M07-006/E12 | END:REJECTED |
| UC-M07-023 | Lan chọn mở hộp thư từ biểu tượng sau khi kiểm tra số tin | SC-M07-007/E1 | END:SUCCESS |
| UC-M07-023 | Toàn bộ Chat bị mute hoặc các cuộc có tin đều mute riêng | SC-M07-007/E2 | END:SUCCESS |
| UC-M07-023 | Cờ Chat tắt | SC-M07-007/E3 | END:SUCCESS |
| UC-M07-023 | Chỉ nhóm cũ có tin mới sau lúc rời, không còn tin chưa đọc được thấy | SC-M07-007/E4 | END:SUCCESS |
| UC-M07-023 | Chỉ một cuộc nhận nhiều tin chưa đọc | SC-M07-007/E5 | END:SUCCESS |
| UC-M07-009 | Bài đang mute, Lan chọn nhận lại | SC-M07-008/E1 | END:SUCCESS |
| UC-M07-010 | Lan bật lại riêng C71; global mute=false | SC-M07-009/E1 | END:SUCCESS |
| UC-M07-010 | Lan bật lại riêng C71; global mute=true | SC-M07-009/E2 | END:SUCCESS |
| UC-M07-010 | Thành viên tắt popup cho nhóm chat thay cuộc1-1 | SC-M07-009/E3 | END:SUCCESS |
| UC-M07-010 | Lan không còn là thành viên cuộc | SC-M07-009/E4 | END:REJECTED |
| UC-M07-011 | Lan bỏ Tắt toàn bộ Chat để nhận lại theo từng cuộc | SC-M07-010/E1 | END:SUCCESS |


Truy vết ngược tại sources từng bước. E thay bước chính, E tại M1 thay toàn bộ theo actor; mọi đường chính hoàn tất chức năng với SYSTEM/SUCCESS. Mở thông báo có đích mất quyền kết thúc REJECTED đối với mở đích, nhưng hậu điều kiện vẫn ghi đã đọc/giữ bản; không biến trạng thái đọc thành rollback. Khác phân loại kết quả trong SC không thay phản ứng FR/US.

Các lớp tương đương độc lập không nhân mọi giá trị: target người/Topic trong follow, trạng thái causer trong hiển thị, loại lỗi đích cùng read-before-open, scope mute và read marker riêng. Tổ hợp thay kết quả đã xét: unread/read + đích mất quyền; đề xuất hết hạn/thay thế/role đổi sau lúc xem; global mute + bật riêng; thành viên cũ + tin trước/sau rời; mark-all + Chat unread; upvote gộp + đã đọc. Biên đồng thời và quy tắc chưa có nguồn không được tự lấp bằng thứ tự API/rollback.

## 7. GAP và giới hạn nguồn

| ID | Nguồn/phần ảnh hưởng | Điều chưa rõ và cách giữ phạm vi |
|---|---|---|
| GAP-SC-M07-001 | NOTE-M07-05; FR-M07-02.25/BR-M07-24 với FR-M01-04.05/08.05/09.12 | M01 yêu cầu thông báo cho chính chủ khi bảo mật thay đổi, nhưng chưa định nghĩa causer để áp lọc self. Cần M01/M07 đối chiếu trước triển khai nhánh tạo bảo mật; giữ kênh/email đã chốt, không gán causer tự động hoặc ngoại lệ self mới. Chặn kết luận đầy đủ phần lọc/tạo bảo mật, không chặn các SC cá nhân độc lập |
| GAP-SC-M07-002 | NOTE-M07-01; FR-M07-01.12/13 và BR-M07-15 so với Q-06 cũ | Chưa chốt rõ bắt đầu follow DEACTIVATED. Không thêm lệnh cấm mọi target không ACTIVE; chuẩn dùng target ACTIVE, BANNED bị cấm rõ, quan hệ cũ DEACTIVATED vẫn giữ. Chờ đối chiếu quyết định cho riêng lần bắt đầu follow DEACTIVATED |
| NOTE-M07-02 | Upvote cập nhật cùng bản và push chỉ trigger tạo mới | Bảo đảm dữ liệu gộp/unread/thứ tự; không khẳng định có hoặc không push lại mọi cập nhật gộp |
| NOTE-M07-03 | Quy tắc không hết hạn cũ đã bỏ | Dùng đủ 7×24 giờ theo M10; thay thế cùng loại không tự mang nhãn hết hạn |
| NOTE-M07-04 | Phân trang/nhiều thiết bị/read đồng thời | Giữ tải đủ và phạm vi mark-all theo người nhận; chưa chọn cursor/giao thức/biên concurrent events hoặc đồng bộ read tức thì |
| TBD nguồn | Không có OPEN/TBD từ phụ lục FR chạm M07 | Hai GAP này là phát hiện khi đối chiếu nguồn, không tự tạo/register một quyết định stakeholder mới |


Đầu ra ở trạng thái Đang soạn; chưa thể coi hai phần thiếu hợp đồng đã được giải quyết chỉ vì validator PASS. Báo cáo/lệnh và số lượng kiểm thực tế ở [QA-M07.md](QA-M07.md). Không sửa FR/US/register hay scenario module khác.


## Chuyển đổi ID nhánh sau QA-SC-01

Ngày 11/11/2026, các biến thể vai trò được đăng ký thành E tại M1 theo skill v1.4. Bảng này giữ ID lịch sử để đối chiếu các tài liệu đã dẫn V. Mỗi hàng ánh xạ cả nhánh và các bước cùng số thứ tự, ví dụ V1.2 sang bước .2 của E tương ứng.

| ID lịch sử | ID hiện hành | Điểm thay | Số bước | Nguồn |
| --- | --- | --- | --- | --- |
| SC-M07-001/V1 | SC-M07-001/E8 | M1 | 2 | FR-M07-01.03 |
| SC-M07-001/V2 | SC-M07-001/E9 | M1 | 2 | FR-M07-01.01, FR-M07-01.04, FR-M07-01.11, FR-M07-01.12, FR-M07-02.01, FR-M07-02.02, FR-M07-02.25, FR-M07-03.01, FR-M07-03.02, BR-M07-15, BR-M07-24, BR-M07-25 |
| SC-M07-002/V1 | SC-M07-002/E4 | M1 | 2 | FR-M07-01.03 |
| SC-M07-002/V2 | SC-M07-002/E5 | M1 | 2 | FR-M07-01.08, FR-M07-01.09, FR-M07-01.10, BR-M07-25 |
| SC-M07-003/V1 | SC-M07-003/E9 | M1 | 2 | FR-M07-05.06 |
| SC-M07-003/V2 | SC-M07-003/E10 | M1 | 2 | FR-M07-05.01, FR-M07-03.04, FR-M07-05.02, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24 |
| SC-M07-004/V1 | SC-M07-004/E9 | M1 | 2 | FR-M07-05.06, FR-M07-06.06 |
| SC-M07-004/V2 | SC-M07-004/E10 | M1 | 2 | FR-M07-06.01, FR-M07-06.02, FR-M07-05.05, FR-M07-05.13, FR-M07-06.04, BR-M07-14, BR-M07-27 |
| SC-M07-005/V1 | SC-M07-005/E4 | M1 | 2 | FR-M07-06.06 |
| SC-M07-005/V2 | SC-M07-005/E5 | M1 | 2 | FR-M07-06.03, FR-M07-05.05, FR-M07-06.05, FR-M07-06.06, BR-M07-14 |
| SC-M07-006/V1 | SC-M07-006/E13 | M1 | 2 | FR-M07-05.06 |
| SC-M07-006/V2 | SC-M07-006/E14 | M1 | 4 | FR-M07-05.02, FR-M07-02.14, FR-M07-03.04, FR-M07-05.01, FR-M07-05.03, FR-M07-05.04, FR-M07-05.05, FR-M07-05.07, FR-M07-05.10, FR-M07-05.11, FR-M07-05.12, BR-M07-09, BR-M07-12, BR-M07-13, BR-M07-22, BR-M07-24, FR-M07-02.15, FR-M07-02.16, FR-M07-02.28, FR-M07-02.30, FR-M07-02.31, FR-M07-02.32, BR-M07-20, FR-M10-07.05, FR-M10-03.02, FR-M10-03.09, FR-M10-03.10, FR-M10-03.11 |
| SC-M07-007/V1 | SC-M07-007/E6 | M1 | 2 | FR-M07-07.04 |
| SC-M07-007/V2 | SC-M07-007/E7 | M1 | 2 | FR-M07-07.01, FR-M07-07.02, FR-M07-07.03, FR-M07-07.04, FR-M07-09.07, BR-M07-02, BR-M07-08, FR-M16-07.10 |
| SC-M07-008/V1 | SC-M07-008/E2 | M1 | 2 | FR-M07-08.05 |
| SC-M07-008/V2 | SC-M07-008/E3 | M1 | 4 | FR-M07-08.01, FR-M07-08.02, FR-M07-08.03, FR-M07-08.04, FR-M07-02.07, FR-M07-02.08, FR-M07-02.09, BR-M07-06, BR-M07-07 |
| SC-M07-009/V1 | SC-M07-009/E5 | M1 | 2 | FR-M07-09.06 |
| SC-M07-009/V2 | SC-M07-009/E6 | M1 | 2 | FR-M07-09.01, FR-M07-09.02, FR-M07-09.05, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |
| SC-M07-010/V1 | SC-M07-010/E2 | M1 | 2 | FR-M07-09.06 |
| SC-M07-010/V2 | SC-M07-010/E3 | M1 | 2 | FR-M07-09.03, FR-M07-09.04, FR-M07-09.07, FR-M07-07.05, FR-M07-07.06, FR-M07-07.07, BR-M07-08, BR-M07-28 |
