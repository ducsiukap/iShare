# Kịch bản nghiệp vụ — M14 Feed & Discovery

[Vietnamese Doc] — 11/11/2026 — Skill scenarios v1.3.

Tài liệu dùng FR và phân tích use case M14 để triển khai các mục tiêu actor khám phá nội dung đến kết quả. Đọc mục 3 để chọn luồng, mục 4 để theo sáu phần và từng đường, mục 5–7 để đối chiếu dữ liệu, nguồn và phần còn cần làm rõ.

Phạm vi gồm 4 UC chính, 5 UC con, 13 mapping, 7 include và 5 SVG nguồn. Có 6 BF tương ứng 6 scenario, 44 nhánh E và 27 đường V theo vai trò. UC003/004 triển khai tại lượt SYSTEM của các hành trình. Hai AUT và sáu RULE theo dõi tính Trending, phát hiện bài mới và chính sách xuyên UC.

Boundary là toàn iShare. ACT-001 Guest, ACT-002 người đăng nhập, ACT-008 Mod và ACT-007 Admin theo US-M14. Các module cung cấp bài, tương tác, quan hệ, cờ và quyền đều bên trong SYSTEM. Nguồn có các lối sang tìm kiếm/danh sách nhóm và cổng mở bài, các lựa chọn đó được viết tới kết quả hoặc chuyển giao mục tiêu tiếp theo đã xác định.

FR-M14 v1.1 Đã chốt ngày 24/10/2026, US-M14/US-overview Chờ duyệt. Đầu ra Đang soạn do 6 GAP theo NOTE-M14-01 đến NOTE-M14-06. TBD-M14-02/OPEN-006 về SSR/SEO đang hoãn mức Thấp theo nguồn. TBD-M14-01 về bookmark đã đóng bởi DEC-259 và trọng số 1 đã được sử dụng.

## 1. Module, baseline và dữ liệu

<!-- sc:document -->

| key | value |
|---|---|
| module | M14 |
| scope | ALL |
| skill_version | 1.3 |
| output_dir | docs/specs/scenarios/M14 |
| status | Đang soạn |
| completed_steps | 1, 2, 3, 4 |
| date | 2026-11-11 |
| approval_evidence | - |


| Nguồn từ repo root | Version | Ngày | Trạng thái | SHA-256 |
|---|---|---|---|---|
| [docs/specs/fr/FR-M14.md](../../fr/FR-M14.md) | 1.1 | 2026-10-24 | Đã chốt | 2dd6163664e86a1ebf9406a463764c2c592490ac0134acabf6df6b1383109e5c |
| [docs/specs/us/US-M14.md](../../us/US-M14.md) | US chưa ghi version tài liệu | 2026-11-02 | Chờ duyệt | a6c60bca2f349d7315ffd6a93983b1a4daa232200e96a0a09a6ec605ebdca358 |
| [docs/specs/us/US-overview.md](../../us/US-overview.md) | 1.1 | 2026-11-02 | Chờ duyệt | c1d624b7036ea2c7a9968eaa46c482c04fa1a15e2554d536cdfc12f177e26e33 |
| [docs/specs/fr/FR-M01.md](../../fr/FR-M01.md) | 1.10 | 2026-10-24 | Đã chốt | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a |
| [docs/specs/fr/FR-M02.md](../../fr/FR-M02.md) | 1.6 | 2026-10-24 | Đã chốt | e86aca71e0415ee2e121a4fdc3628261be335e9d266fcf6e9654b2fdf3cd357e |
| [docs/specs/fr/FR-M03.md](../../fr/FR-M03.md) | 1.10 | 2026-10-24 | Đã chốt | fc996ec5520b6485277fca6a3dbae018bfce02263aba8e15ea87871f35865980 |
| [docs/specs/fr/FR-M04.md](../../fr/FR-M04.md) | 1.4 | 2026-10-24 | Đã chốt | c2fe0e4f6c4bc6835af27585cb711ac03f9fed516d435e759d20ddd58bfd1039 |
| [docs/specs/fr/FR-M05.md](../../fr/FR-M05.md) | 1.7 | 2026-10-24 | Đã chốt | eb85b5dcb56995d791ed28a8d72a2f91c95588d8cd8d4fb1e74a8aabc2d701aa |
| [docs/specs/fr/FR-M06.md](../../fr/FR-M06.md) | 1.5 | 2026-10-24 | Đã chốt | 63606046efb11356276a2c9180f53cadad76f83e2e86502ed00341d915e0b084 |
| [docs/specs/fr/FR-M07.md](../../fr/FR-M07.md) | 1.5 | 2026-10-24 | Đã chốt | 05fb18237e049e3742d06c49b824e76e238c7587e7099b8dc4a84a2e1daf4f5b |
| [docs/specs/fr/FR-M08.md](../../fr/FR-M08.md) | 1.7 | 2026-10-24 | Đã chốt | a92e6e370038af300a9ddd735414dcb2c4fbffe07c81abaaa3c92dff447c25f0 |
| [docs/specs/fr/FR-M10.md](../../fr/FR-M10.md) | 1.4 | 2026-10-24 | Đã chốt | 3e1010a76db6ef4c5870f42765e669095efc8d38c202271d9b200d2da0823d2c |
| [docs/specs/fr/FR-M11.md](../../fr/FR-M11.md) | 1.3 | 2026-10-24 | Đã chốt | 1908d300f75d5f7fa0fd5b31b1d375bc6a63ccd42da254de6e9d0d7d9ef16307 |
| [docs/specs/fr/FR-M12.md](../../fr/FR-M12.md) | 1.1 | 2026-10-24 | Đã chốt | 7aa660866cf625220db602509c93775b713fb26e568cc1d9df2d9aaa399f2430 |


FR chính thức khớp byte với bản làm việc chung .agents/.claude/system_analysis/output/fr/FR-M14.md. US chưa ghi version tài liệu, skill_version=2.2 là phiên bản phương pháp US. Tổng quan hệ thống được dùng cho boundary, catalog M14 cung cấp toàn bộ core/sub trong scope. [Skill scenarios](../../../../.agent-instructions/skills/scenarios/SKILL.md)

<!-- sc:actors -->

| id | name | kind | source |
|---|---|---|---|
| ACT-001 | Guest | human | FR-M14-01.03, FR-M14-02.02, FR-M14-04.04, FR-M14-05.05, FR-M14-06.04 |
| ACT-002 | Người dùng đã đăng nhập | human | FR-M14-01.08, FR-M14-04.01, FR-M14-05.01 |
| ACT-008 | Mod hệ thống | human | FR-M14-01, FR-M14-02, FR-M14-04, FR-M14-05, FR-M14-06 |
| ACT-007 | Admin hệ thống | human | FR-M14-01.07, BR-M14-22, FR-M10-12.08, FR-M11-17.03, FR-M12-08.06 |


ACT-008 kế thừa người đăng nhập, ACT-007 kế thừa theo mô hình actor nguồn. Member/Owner/Group Mod là ngữ cảnh quyền nhóm, xử lý tự động dùng SYSTEM. Staff có cùng mục tiêu feed, quyền riêng tại owner được đối chiếu khi có lựa chọn liên quan.

| Bộ dữ liệu | Giá trị giả lập và ranh giới |
|---|---|
| D-TIME | T mở lượt=11/11/2026 10:10+07. K0 tính 10:00, K1 tính 10:20. Các mốc đều giờ Việt Nam. ID, tên, bài và số liệu trong tài liệu là giả lập để phân tích. Mỗi E/V là snapshot thay thế độc lập. |
| D-PEOPLE | An USER ACTIVE/SETUP_COMPLETED. Minh MODERATOR, Hòa ADMIN. U/V/W0–W3 là tác giả phân biệt trong D-SET. An theo dõi U và Topic Toán. Toán là nhãn ngắn của Toán học, Văn là Ngữ văn. An là Member thường GJ/GK/GH. |
| D45 | P01–P45, bài đều Đã đăng/Bình thường, đủ điều kiện. P02/P21 thuộc Public GJ, 43 bài còn lại ngoài nhóm. Mỗi bài có tác giả Axx riêng, A22 BANNED, A23 ACTIVE/HEAVY, còn lại ACTIVE. C=B=0. U và thời điểm đăng tại bảng bên dưới. P21 nhận thêm 17 upvote hiệu lực lúc 10:15. |
| D-SET | Q01–Q21 tại bảng bên dưới, U=C=B=0 để tách việc chọn tập khỏi tính điểm. Thời điểm mỗi dòng là mốc công bố có nghĩa với các bài đã công bố, dòng Nháp/Chờ duyệt/Bị từ chối dùng thời điểm dữ liệu minh họa để kiểm loại trạng thái. |
| D-TIME45 | R01–R45 là bộ riêng cho từng tab, thời điểm đăng R01=11/11 10:00, R(i)=R01−(i−1) phút. Mọi bài Đã đăng/Bình thường, tác giả ACTIVE. F gồm bài U/Văn trừ R21 Toán, G gồm GJ Public trừ R21 GK Private, N đều ngoài nhóm. Bài cuối đã trả là vị trí tải tiếp. |
| D-TOPIC/D-TAG | 23 Topic và 23 Tag đã có trong danh mục giả lập, điểm lần lượt 23→1, đều 1 bài mới, tên/ID theo bảng. Tag hoạt động, mục điểm 0 và bị vô hiệu hóa được mô tả riêng trong E. 23 là kích thước dữ liệu minh họa. |
| D-DIRECTORY | GJ tên “CLB Toán”, mô tả “Trao đổi bài Toán”, Public, tạo 10/11 07:00. GO “CLB Văn”, “Đọc và viết”, Public, tạo 11/11 08:00. GK “Lớp 12A”, “Nhóm lớp”, Private, tạo 11/11 09:00. Bộ này có nhóm còn hiển thị, quyền Private theo từng E. |
| D-NEW30 | O01–O45 là 45 bài cũ đã tải, O01 đăng 11/11 10:00, O(i)=O01−(i−1) phút, vị trí đọc O35. N01–N30 đăng 11/11 10:11:01–10:11:30, đều bài thường Đã đăng/Bình thường của tác giả ACTIVE. N thường ngoài nhóm, F của U/Toán ngoài nhóm/Public, G lẻ thuộc GJ Public/chẵn thuộc GK Private. Khi bấm, tập và quyền ổn định theo dữ liệu từng đường. |
| D-STAFF/D-ADMIN | Các ví dụ staff dùng S01/S02 bài thường, tác giả ACTIVE, đã công bố, thời điểm phân biệt, quyền nhóm được ghi trong V. Nội dung Sxx có tiêu đề “Bài Sxx”, chữ “Nội dung minh họa Sxx”, tác giả U, Lớp/Khối 11, Topic Toán, tệp/poll rỗng. Trường hợp quyền staff/ẩn danh/DEACTIVATED giao nhau giữ ở GAP004. |


### D45 và hai lần tính

| ID | Đăng UTC+7 | Nhóm | U tại K0 | S K0 | U tại K1 | S K1 | Tác giả |
|---|---|---|---|---|---|---|---|
| P01 | 10/11/2026 10:00 | ngoài nhóm | 45 | 82.420853 | 45 | 82.307579 | ACTIVE/LIGHT |
| P02 | 10/11/2026 09:59 | GJ Public | 44 | 80.603863 | 44 | 80.493086 | ACTIVE/LIGHT |
| P03 | 10/11/2026 09:58 | ngoài nhóm | 43 | 78.787123 | 43 | 78.678842 | ACTIVE/LIGHT |
| P04 | 10/11/2026 09:57 | ngoài nhóm | 42 | 76.970631 | 42 | 76.864847 | ACTIVE/LIGHT |
| P05 | 10/11/2026 09:56 | ngoài nhóm | 41 | 75.154389 | 41 | 75.051101 | ACTIVE/LIGHT |
| P06 | 10/11/2026 09:55 | ngoài nhóm | 40 | 73.338397 | 40 | 73.237605 | ACTIVE/LIGHT |
| P07 | 10/11/2026 09:54 | ngoài nhóm | 39 | 71.522654 | 39 | 71.424357 | ACTIVE/LIGHT |
| P08 | 10/11/2026 09:53 | ngoài nhóm | 38 | 69.707160 | 38 | 69.611359 | ACTIVE/LIGHT |
| P09 | 10/11/2026 09:52 | ngoài nhóm | 37 | 67.891916 | 37 | 67.798609 | ACTIVE/LIGHT |
| P10 | 10/11/2026 09:51 | ngoài nhóm | 36 | 66.076921 | 36 | 65.986108 | ACTIVE/LIGHT |
| P11 | 10/11/2026 09:50 | ngoài nhóm | 35 | 64.262175 | 35 | 64.173857 | ACTIVE/LIGHT |
| P12 | 10/11/2026 09:49 | ngoài nhóm | 34 | 62.447679 | 34 | 62.361854 | ACTIVE/LIGHT |
| P13 | 10/11/2026 09:48 | ngoài nhóm | 33 | 60.633432 | 33 | 60.550100 | ACTIVE/LIGHT |
| P14 | 10/11/2026 09:47 | ngoài nhóm | 32 | 58.819434 | 32 | 58.738595 | ACTIVE/LIGHT |
| P15 | 10/11/2026 09:46 | ngoài nhóm | 31 | 57.005685 | 31 | 56.927339 | ACTIVE/LIGHT |
| P16 | 10/11/2026 09:45 | ngoài nhóm | 30 | 55.192185 | 30 | 55.116332 | ACTIVE/LIGHT |
| P17 | 10/11/2026 09:44 | ngoài nhóm | 29 | 53.378935 | 29 | 53.305573 | ACTIVE/LIGHT |
| P18 | 10/11/2026 09:43 | ngoài nhóm | 28 | 51.565933 | 28 | 51.495064 | ACTIVE/LIGHT |
| P19 | 10/11/2026 09:42 | ngoài nhóm | 27 | 49.753181 | 27 | 49.684803 | ACTIVE/LIGHT |
| P20 | 10/11/2026 09:41 | ngoài nhóm | 26 | 47.940677 | 26 | 47.874790 | ACTIVE/LIGHT |
| P21 | 10/11/2026 09:40 | GJ Public | 25 | 46.128423 | 42 | 76.775045 | ACTIVE/LIGHT |
| P22 | 10/11/2026 09:39 | ngoài nhóm | 24 | 44.316418 | 24 | 44.255512 | BANNED |
| P23 | 10/11/2026 09:38 | ngoài nhóm | 23 | 42.504662 | 23 | 42.446245 | HEAVY |
| P24 | 10/11/2026 09:37 | ngoài nhóm | 22 | 40.693154 | 22 | 40.637228 | ACTIVE/LIGHT |
| P25 | 10/11/2026 09:36 | ngoài nhóm | 21 | 38.881896 | 21 | 38.828459 | ACTIVE/LIGHT |
| P26 | 10/11/2026 09:35 | ngoài nhóm | 20 | 37.070886 | 20 | 37.019938 | ACTIVE/LIGHT |
| P27 | 10/11/2026 09:34 | ngoài nhóm | 19 | 35.260126 | 19 | 35.211666 | ACTIVE/LIGHT |
| P28 | 10/11/2026 09:33 | ngoài nhóm | 18 | 33.449614 | 18 | 33.403642 | ACTIVE/LIGHT |
| P29 | 10/11/2026 09:32 | ngoài nhóm | 17 | 31.639351 | 17 | 31.595867 | ACTIVE/LIGHT |
| P30 | 10/11/2026 09:31 | ngoài nhóm | 16 | 29.829337 | 16 | 29.788341 | ACTIVE/LIGHT |
| P31 | 10/11/2026 09:30 | ngoài nhóm | 15 | 28.019571 | 15 | 27.981063 | ACTIVE/LIGHT |
| P32 | 10/11/2026 09:29 | ngoài nhóm | 14 | 26.210055 | 14 | 26.174033 | ACTIVE/LIGHT |
| P33 | 10/11/2026 09:28 | ngoài nhóm | 13 | 24.400787 | 13 | 24.367252 | ACTIVE/LIGHT |
| P34 | 10/11/2026 09:27 | ngoài nhóm | 12 | 22.591767 | 12 | 22.560719 | ACTIVE/LIGHT |
| P35 | 10/11/2026 09:26 | ngoài nhóm | 11 | 20.782997 | 11 | 20.754434 | ACTIVE/LIGHT |
| P36 | 10/11/2026 09:25 | ngoài nhóm | 10 | 18.974475 | 10 | 18.948397 | ACTIVE/LIGHT |
| P37 | 10/11/2026 09:24 | ngoài nhóm | 9 | 17.166202 | 9 | 17.142609 | ACTIVE/LIGHT |
| P38 | 10/11/2026 09:23 | ngoài nhóm | 8 | 15.358177 | 8 | 15.337069 | ACTIVE/LIGHT |
| P39 | 10/11/2026 09:22 | ngoài nhóm | 7 | 13.550401 | 7 | 13.531778 | ACTIVE/LIGHT |
| P40 | 10/11/2026 09:21 | ngoài nhóm | 6 | 11.742873 | 6 | 11.726734 | ACTIVE/LIGHT |
| P41 | 10/11/2026 09:20 | ngoài nhóm | 5 | 9.935594 | 5 | 9.921939 | ACTIVE/LIGHT |
| P42 | 10/11/2026 09:19 | ngoài nhóm | 4 | 8.128563 | 4 | 8.117392 | ACTIVE/LIGHT |
| P43 | 10/11/2026 09:18 | ngoài nhóm | 3 | 6.321781 | 3 | 6.313093 | ACTIVE/LIGHT |
| P44 | 10/11/2026 09:17 | ngoài nhóm | 2 | 4.515248 | 2 | 4.509042 | ACTIVE/LIGHT |
| P45 | 10/11/2026 09:16 | ngoài nhóm | 1 | 2.708962 | 1 | 2.705239 | ACTIVE/LIGHT |


Các chữ số thập phân ở bảng phục vụ đọc ví dụ. Thứ tự được kiểm từ giá trị tính đầy đủ, độ chính xác hiển thị sản phẩm thuộc giai đoạn thiết kế. K1 đầu danh sách là P01, P02, P03, P04, P21.

### D-SET và tập bài theo tab

| ID | Mốc dữ liệu 11/11 UTC+7 | Tác giả | Topic | Nhóm | Ẩn danh | Trạng thái đăng | Kiểm duyệt | Tài khoản |
|---|---|---|---|---|---|---|---|---|
| Q01 | 09:01 | U | Văn | - | Bài thường | Đã đăng | Bình thường | ACTIVE |
| Q02 | 09:02 | V | Toán | - | Bài thường | Đã đăng | Bình thường | ACTIVE |
| Q03 | 09:03 | U | Toán | - | Bài thường | Đã đăng | Bình thường | ACTIVE |
| Q04 | 09:04 | V | Văn | - | Bài thường | Đã đăng | Bình thường | ACTIVE |
| Q05 | 09:05 | U | Toán | GJ Public | Bài thường | Đã đăng | Bình thường | ACTIVE |
| Q06 | 09:06 | U | Toán | GK Private | Bài thường | Đã đăng | Bình thường | ACTIVE |
| Q07 | 09:07 | U | Văn | GJ Public | Có | Đã đăng | Bình thường | ACTIVE |
| Q08 | 09:08 | U | Toán | GJ Public | Có | Đã đăng | Bình thường | ACTIVE |
| Q09 | 09:09 | V | Toán | GO Public | Bài thường | Đã đăng | Bình thường | ACTIVE |
| Q10 | 09:10 | W0 | Toán | - | Bài thường | Đã đăng | Bình thường | DEACTIVATED |
| Q11 | 09:11 | W1 | Toán | - | Bài thường | Đã đăng | Bình thường | BANNED |
| Q12 | 09:12 | W2 | Toán | - | Bài thường | Đã đăng | Bình thường | ACTIVE/HEAVY |
| Q13 | 09:13 | U | Toán | - | Bài thường | Đã xóa | Bình thường | ACTIVE |
| Q14 | 09:14 | U | Toán | - | Bài thường | Đã đăng | Bị ẩn | ACTIVE |
| Q15 | 09:15 | U | Toán | GH Public bị ẩn | Bài thường | Đã đăng | Bình thường | ACTIVE |
| Q16 | 09:16 | U | Toán | GJ Public đã gỡ bài | Bài thường | Đã đăng | Bình thường | ACTIVE |
| Q17 | 09:17 | W3 | Toán | - | Bài thường | Đã đăng | Bình thường | DELETED |
| Q18 | 09:18 | U | Toán | - | Bài thường | Nháp | Bình thường | ACTIVE |
| Q19 | 09:19 | U | Toán | - | Bài thường | Chờ duyệt | Bình thường | ACTIVE |
| Q20 | 09:20 | U | Toán | - | Bài thường | Bị từ chối | Bình thường | ACTIVE |
| Q21 | 09:21 | U | Toán | - | Bài thường | Tự ẩn | Bình thường | ACTIVE |


| Tab | Kết quả theo thứ tự |
|---|---|
| Following | Q12, Q11, Q09, Q08, Q05, Q03, Q02, Q01 |
| Group | Q08, Q07, Q06, Q05 |
| Newest | Q12, Q11, Q04, Q03, Q02, Q01 |


### Danh sách mục do M05 cung cấp

| Topic ID | Tên Topic | Tag ID | Tên Tag | Điểm | Số bài mới |
|---|---|---|---|---|---|
| T01 | Chủ đề 01 | TG01 | #tag01 | 23 | 1 |
| T02 | Chủ đề 02 | TG02 | #tag02 | 22 | 1 |
| T03 | Chủ đề 03 | TG03 | #tag03 | 21 | 1 |
| T04 | Chủ đề 04 | TG04 | #tag04 | 20 | 1 |
| T05 | Chủ đề 05 | TG05 | #tag05 | 19 | 1 |
| T06 | Chủ đề 06 | TG06 | #tag06 | 18 | 1 |
| T07 | Chủ đề 07 | TG07 | #tag07 | 17 | 1 |
| T08 | Chủ đề 08 | TG08 | #tag08 | 16 | 1 |
| T09 | Chủ đề 09 | TG09 | #tag09 | 15 | 1 |
| T10 | Chủ đề 10 | TG10 | #tag10 | 14 | 1 |
| T11 | Chủ đề 11 | TG11 | #tag11 | 13 | 1 |
| T12 | Chủ đề 12 | TG12 | #tag12 | 12 | 1 |
| T13 | Chủ đề 13 | TG13 | #tag13 | 11 | 1 |
| T14 | Chủ đề 14 | TG14 | #tag14 | 10 | 1 |
| T15 | Chủ đề 15 | TG15 | #tag15 | 9 | 1 |
| T16 | Chủ đề 16 | TG16 | #tag16 | 8 | 1 |
| T17 | Chủ đề 17 | TG17 | #tag17 | 7 | 1 |
| T18 | Chủ đề 18 | TG18 | #tag18 | 6 | 1 |
| T19 | Chủ đề 19 | TG19 | #tag19 | 5 | 1 |
| T20 | Chủ đề 20 | TG20 | #tag20 | 4 | 1 |
| T21 | Chủ đề 21 | TG21 | #tag21 | 3 | 1 |
| T22 | Chủ đề 22 | TG22 | #tag22 | 2 | 1 |
| T23 | Chủ đề 23 | TG23 | #tag23 | 1 | 1 |


## 2. UC chính và UC con

<!-- sc:decomposition -->

| core | sub | source |
|---|---|---|
| UC-M14-020 | UC-M14-001 | FR-M14-02, FR-M14-07, BR-M14-05, BR-M14-13, BR-M14-19 |
| UC-M14-020 | UC-M14-002 | FR-M14-02.06, FR-M14-02.10, BR-M14-24, BR-M05-29, BR-M05-31 |
| UC-M14-020 | UC-M14-003 | FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, FR-M14-04, FR-M14-05, FR-M14-06, BR-M14-04, BR-M14-05, BR-M14-06, BR-M14-07, BR-M14-08, BR-M14-15, BR-M14-23 |
| UC-M14-020 | UC-M14-004 | FR-M14-07, FR-M14-02.10, BR-M14-16, BR-M14-19, BR-M14-24 |
| UC-M14-021 | UC-M14-003 | FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, FR-M14-04, FR-M14-05, FR-M14-06, BR-M14-04, BR-M14-05, BR-M14-06, BR-M14-07, BR-M14-08, BR-M14-15, BR-M14-23 |
| UC-M14-021 | UC-M14-004 | FR-M14-07, FR-M14-02.10, BR-M14-16, BR-M14-19, BR-M14-24 |
| UC-M14-021 | UC-M14-005 | FR-M14-08, BR-M14-17, BR-M14-18 |
| UC-M14-022 | UC-M14-003 | FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, FR-M14-04, FR-M14-05, FR-M14-06, BR-M14-04, BR-M14-05, BR-M14-06, BR-M14-07, BR-M14-08, BR-M14-15, BR-M14-23 |
| UC-M14-022 | UC-M14-004 | FR-M14-07, FR-M14-02.10, BR-M14-16, BR-M14-19, BR-M14-24 |
| UC-M14-022 | UC-M14-005 | FR-M14-08, BR-M14-17, BR-M14-18 |
| UC-M14-023 | UC-M14-003 | FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, FR-M14-04, FR-M14-05, FR-M14-06, BR-M14-04, BR-M14-05, BR-M14-06, BR-M14-07, BR-M14-08, BR-M14-15, BR-M14-23 |
| UC-M14-023 | UC-M14-004 | FR-M14-07, FR-M14-02.10, BR-M14-16, BR-M14-19, BR-M14-24 |
| UC-M14-023 | UC-M14-005 | FR-M14-08, BR-M14-17, BR-M14-18 |


<!-- sc:ucs -->

| id | name | treatment | scenarios | coverage | rationale | sources |
|---|---|---|---|---|---|---|
| UC-M14-020 | Khám phá nội dung thịnh hành | aggregate | SC-M14-001, SC-M14-002 | SC-M14-001/M2, SC-M14-002/M2 | Core Summary bao gồm khám phá Post và Topic/Tag, mỗi mục tiêu có hành trình actor riêng. | FR-M14-01, FR-M14-02, FR-M14-03, BR-M14-01, BR-M14-03, BR-M14-19, BR-M14-24 |
| UC-M14-021 | Xem bài từ người dùng và Topic đang theo dõi | scenario | SC-M14-003, SC-M14-006 | SC-M14-003/M2, SC-M14-006/E1.2 | Actor chủ động yêu cầu mục tiêu chức năng đến kết quả danh sách hoặc toàn bộ bài mới. Các lựa chọn dữ liệu/vai trò là E/V. | FR-M14-04, FR-M14-07, FR-M14-08, BR-M14-08, BR-M14-20 |
| UC-M14-022 | Xem bài từ các nhóm đã tham gia | scenario | SC-M14-004, SC-M14-006 | SC-M14-004/M2, SC-M14-006/E2.2 | Actor chủ động yêu cầu mục tiêu chức năng đến kết quả danh sách hoặc toàn bộ bài mới. Các lựa chọn dữ liệu/vai trò là E/V. | FR-M14-05, FR-M14-07, FR-M14-08, BR-M14-07, BR-M14-21 |
| UC-M14-023 | Xem bài mới toàn site | scenario | SC-M14-005, SC-M14-006 | SC-M14-005/M2, SC-M14-006/M2 | Actor chủ động yêu cầu mục tiêu chức năng đến kết quả danh sách hoặc toàn bộ bài mới. Các lựa chọn dữ liệu/vai trò là E/V. | FR-M14-06, FR-M14-07, FR-M14-08, BR-M14-06, BR-M14-09 |
| UC-M14-001 | Xem bài viết thịnh hành | scenario | SC-M14-001 | SC-M14-001/M2 | Actor chủ động yêu cầu mục tiêu chức năng đến kết quả danh sách hoặc toàn bộ bài mới. Các lựa chọn dữ liệu/vai trò là E/V. | FR-M14-02, FR-M14-07, BR-M14-05, BR-M14-13, BR-M14-19 |
| UC-M14-002 | Xem Topic và Tag thịnh hành | scenario | SC-M14-002 | SC-M14-002/M2 | Actor chủ động yêu cầu mục tiêu chức năng đến kết quả danh sách hoặc toàn bộ bài mới. Các lựa chọn dữ liệu/vai trò là E/V. | FR-M14-02.06, FR-M14-02.10, BR-M14-24, BR-M05-29, BR-M05-31 |
| UC-M14-003 | Chọn bài đúng phạm vi và quyền hiển thị | embedded | SC-M14-001, SC-M14-003, SC-M14-004, SC-M14-005, SC-M14-006 | SC-M14-001/M2, SC-M14-003/M2, SC-M14-004/M2, SC-M14-005/M2, SC-M14-006/M2 | Hỗ trợ ở từng lần cấp dữ liệu của hành trình bao chứa. UC003 chỉ chọn bài, UC004 cấp phần danh sách. Banner dùng UC003 để cấp toàn bộ bài mới. | FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, FR-M14-04, FR-M14-05, FR-M14-06, BR-M14-04, BR-M14-05, BR-M14-06, BR-M14-07, BR-M14-08, BR-M14-15, BR-M14-23 |
| UC-M14-004 | Tải danh sách theo con trỏ | embedded | SC-M14-001, SC-M14-002, SC-M14-003, SC-M14-004, SC-M14-005 | SC-M14-001/M2, SC-M14-002/M2, SC-M14-003/M2, SC-M14-004/M2, SC-M14-005/M2 | Hỗ trợ ở từng lần cấp dữ liệu của hành trình bao chứa. UC003 chỉ chọn bài, UC004 cấp phần danh sách. Banner dùng UC003 để cấp toàn bộ bài mới. | FR-M14-07, FR-M14-02.10, BR-M14-16, BR-M14-19, BR-M14-24 |
| UC-M14-005 | Chèn toàn bộ bài mới từ banner | scenario | SC-M14-006 | SC-M14-006/M2 | Actor chủ động yêu cầu mục tiêu chức năng đến kết quả danh sách hoặc toàn bộ bài mới. Các lựa chọn dữ liệu/vai trò là E/V. | FR-M14-08, BR-M14-17, BR-M14-18 |


| SVG nguồn | Số UC | Đối chiếu |
|---|---|---|
| C-M14 | 4 | Tập UC trong SVG khớp thành viên US |
| D-M14-020 | 5 | Tập UC trong SVG khớp thành viên US |
| D-M14-021 | 4 | Tập UC trong SVG khớp thành viên US |
| D-M14-022 | 4 | Tập UC trong SVG khớp thành viên US |
| D-M14-023 | 4 | Tập UC trong SVG khớp thành viên US |


Có 6 UC sở hữu scenario, 2 UC embedded, 1 UC aggregate. UC005 dùng chung cho ba tab thời gian có một SC riêng và các đường theo tab. UC004 nằm trong hành trình đọc và UC003 nằm trong mỗi lượt cấp bài hoặc chèn bài mới.

## 3. Danh mục luồng nghiệp vụ

<!-- sc:flows -->

| id | uc | primary | trigger | goal | completion | covered_ucs | rationale | scenario | sources |
|---|---|---|---|---|---|---|---|---|---|
| BF-M14-001 | UC-M14-001 | ACT-001 | Guest mở trang chủ iShare để đọc bài thịnh hành. | Đọc danh sách bài thịnh hành và tải tiếp trong một lượt Trending | Người xem nhận danh sách Trending Post đúng kết quả lúc mở lượt và phần tiếp nối được yêu cầu, tối đa 20 bài/lần. Đường chuẩn đọc hết 45 bài. Bài mất điều kiện bị loại tại lần tải. Kết quả mới được phục vụ khi mở lượt Trending mới hoặc tải lại trang. Nhãn BANNED theo tên được phép hiện, HEAVY giữ thứ hạng theo nguồn. | UC-M14-020, UC-M14-001, UC-M14-003, UC-M14-004 | Actor chủ động mở/chọn danh sách hoặc bấm nhận bài mới và nhận kết quả chức năng. Cuộn/loại mục/quan hệ/cờ/vai trò triển khai theo E/V. | SC-M14-001 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, FR-M14-02.06, FR-M14-02.10, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31, BR-M11-14, BR-M11-15, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |
| BF-M14-002 | UC-M14-002 | ACT-001 | Guest chọn Trending Topic. | Khám phá danh sách Topic hoặc Tag thịnh hành đến hết các mục | Người xem nhận mọi mục điểm dương của loại Topic/Tag đã chọn theo thứ tự M05, tối đa 20 mục mỗi lần tải và dừng khi hết. Các mục điểm 0 và Tag bị vô hiệu hóa thuộc phạm vi loại của M05. Phần giữ kết quả khi danh mục thay đổi tiếp tục theo GAP002. | UC-M14-020, UC-M14-002, UC-M14-004 | Actor chủ động mở/chọn danh sách hoặc bấm nhận bài mới và nhận kết quả chức năng. Cuộn/loại mục/quan hệ/cờ/vai trò triển khai theo E/V. | SC-M14-002 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| BF-M14-003 | UC-M14-021 | ACT-002 | An chọn tab Following. | Đọc bài từ người dùng và Topic chính mình đang theo dõi | An nhận dòng bài đúng quan hệ người dùng/Topic hiện tại và quyền hiển thị, mỗi bài một lần, thời điểm đăng sau trước. Bài ẩn danh đủ điều kiện qua Topic được hiển thị Ẩn danh. Tab rỗng có nút dẫn sang tìm kiếm. Tải tiếp dùng quan hệ hiện tại. | UC-M14-021, UC-M14-003, UC-M14-004 | Actor chủ động mở/chọn danh sách hoặc bấm nhận bài mới và nhận kết quả chức năng. Cuộn/loại mục/quan hệ/cờ/vai trò triển khai theo E/V. | SC-M14-003 | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M06-02.31, FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-05.08, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06, FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-03, BR-M10-19 |
| BF-M14-004 | UC-M14-022 | ACT-002 | An chọn tab Group. | Đọc bài từ mọi nhóm chính mình đang tham gia | An nhận bài đủ điều kiện của các nhóm hiện tham gia, Public/Private, theo thời điểm đăng sau trước. Tab rỗng có Khám phá Group. Từ lần tải sau khi rời nhóm, bài của nhóm đã rời bị loại. Cờ Group Tắt vẫn cho liệt kê tại feed theo nguồn. | UC-M14-022, UC-M14-003, UC-M14-004 | Actor chủ động mở/chọn danh sách hoặc bấm nhận bài mới và nhận kết quả chức năng. Cuộn/loại mục/quan hệ/cờ/vai trò triển khai theo E/V. | SC-M14-004 | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M11-03.11, FR-M11-03.16, FR-M11-03.17, FR-M11-17.07, FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06, FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-03, BR-M10-19 |
| BF-M14-005 | UC-M14-023 | ACT-001 | Guest chọn tab Newest. | Đọc dòng bài mới toàn site ngoài nhóm | Người xem nhận dòng bài ngoài nhóm theo thời điểm đăng, có thể tải tiếp sau vị trí đã có. Bài nhóm Public/Private nằm ngoài tập Newest. Bài mới được báo qua AUT002 và chèn khi actor chọn chức năng tại SC006. | UC-M14-023, UC-M14-003, UC-M14-004 | Actor chủ động mở/chọn danh sách hoặc bấm nhận bài mới và nhận kết quả chức năng. Cuộn/loại mục/quan hệ/cờ/vai trò triển khai theo E/V. | SC-M14-005 | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| BF-M14-006 | UC-M14-005 | ACT-002 | An bấm banner có bài mới ở Newest. | Nhận toàn bộ bài mới qua banner và tiếp tục tại chỗ đang đọc | Tất cả bài mới hơn mốc trên màn hình và còn thuộc tab được thêm lên đầu theo thời điểm đăng, mỗi bài một lần. Bộ 30 bài thêm đủ 30, vị trí đọc O35 được giữ theo nguồn. Banner thuộc Newest/Following/Group, polling tiếp tục theo AUT002 khi còn ở tab được phép. | UC-M14-021, UC-M14-022, UC-M14-023, UC-M14-005, UC-M14-003 | Actor chủ động mở/chọn danh sách hoặc bấm nhận bài mới và nhận kết quả chức năng. Cuộn/loại mục/quan hệ/cờ/vai trò triển khai theo E/V. | SC-M14-006 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-08, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-07, BR-M14-21, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10 |


Post và Topic/Tag có mục tiêu dữ liệu riêng trong core020. Topic/Tag cùng hợp đồng khám phá danh sách, chọn loại là nhánh. Following/Group/Newest là ba mục tiêu đọc các nguồn bài mà người xem chọn. Banner có trigger chủ động riêng và kết quả thêm toàn bộ bài mới, giữ chỗ đọc. Mở trang chủ triển khai tại hành trình Trending mặc định, tải tiếp nằm trong từng hành trình đọc. AUT001 tính kết quả và AUT002 phát hiện bài mới theo thời gian.

| Quan hệ US | Điểm chèn | Điều kiện | Điểm về |
|---|---|---|---|
| UC-M14-001 include UC-M14-004 | #uc-m14-001-main-3 | Mỗi lần mở/tải tiếp danh sách Post, lần cuộn tái sử dụng cùng ngữ cảnh. | #uc-m14-001-main-4 |
| UC-M14-002 include UC-M14-004 | #uc-m14-002-main-3 | Mỗi lần tải Topic hoặc Tag. | #uc-m14-002-main-4 |
| UC-M14-004 include UC-M14-003 | #uc-m14-004-main-2 | Loại danh sách là bài viết, nhánh Topic/Tag không gọi. | #uc-m14-004-main-3 |
| UC-M14-021 include UC-M14-004 | #uc-m14-021-main-3 | Đã qua kiểm đăng nhập, mở hoặc cuộn Following. | #uc-m14-021-main-4 |
| UC-M14-022 include UC-M14-004 | #uc-m14-022-main-3 | Đã qua kiểm đăng nhập, mở hoặc cuộn Group. | #uc-m14-022-main-4 |
| UC-M14-023 include UC-M14-004 | #uc-m14-023-main-3 | Mở hoặc cuộn Newest, Guest cũng được xem. | #uc-m14-023-main-4 |
| UC-M14-005 include UC-M14-003 | #uc-m14-005-main-2 | Bấm banner ở Newest/Following/Group đang được phép. | #uc-m14-005-main-3 |


UC001/002/021/022/023 chèn UC004 khi cấp trang. UC004 chèn UC003 khi danh sách là bài, loại Topic/Tag dùng dữ liệu M05. UC005 chèn UC003 để lọc toàn bộ bài mới trước chèn. Các điểm về được mở nội dung xử lý ngay tại lượt SYSTEM trong SC. [US-M14](../../us/US-M14.md)

## 4. Scenario sáu phần

<a id="sc-m14-001"></a>

<!-- sc:scenario SC-M14-001 -->

### SC-M14-001

#### 1. Tên kịch bản chuẩn

Đọc danh sách bài thịnh hành và tải tiếp trong một lượt Trending — BF-M14-001. Owner [UC-M14-001](../../us/US-M14.md#uc-m14-001).

#### 2. Actor thực hiện

ACT-001 khởi tạo đường chuẩn. Các đường V ghi actor khởi tạo khác theo cùng mục tiêu. Toàn iShare là SYSTEM, các quan hệ và dữ liệu owner được xử lý trong lượt SYSTEM.

#### 3. Tiền điều kiện

Guest truy cập iShare tại 11/11/2026 10:10+07. Đường chuẩn D45 có kết quả K0 tính lúc 10:00 và đủ 45 bài còn hiển thị, Group/Gamification Bật. Các tiền điều kiện dữ liệu này mô tả đường chuẩn, phần trước lần tính đầu tiên và lỗi tải được giữ tại GAP001/005. Lượt Trending kéo dài qua K1 lúc 10:20, quyền dữ liệu ổn định ở đường chuẩn.

#### 4. Hậu điều kiện

<!-- sc:post SC-M14-001 -->

| result | condition |
|---|---|
| SUCCESS | Người xem nhận danh sách Trending Post đúng kết quả lúc mở lượt và phần tiếp nối được yêu cầu, tối đa 20 bài/lần. Đường chuẩn đọc hết 45 bài. Bài mất điều kiện bị loại tại lần tải. Kết quả mới được phục vụ khi mở lượt Trending mới hoặc tải lại trang. Nhãn BANNED theo tên được phép hiện, HEAVY giữ thứ hạng theo nguồn. |
| REJECTED | Feed đã được liệt kê, lựa chọn mở bài nhóm bị cổng M11 từ chối khi Group Tắt hoặc quyền Private hiện tại chặn mở lại. Thông báo và nội dung cấp theo owner của thao tác mở. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M14-001 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-001 | Guest mở trang chủ iShare để đọc bài thịnh hành. | T=10:10, D45, kết quả hiện hành K0=10:00. | M2 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19 |
| M2 | SYSTEM | Hệ thống hiển thị đủ bốn tab Trending, Following, Group, Newest và ba mục Trending Post/Topic/Tag, mở Trending Post mặc định. Ghi nhận K0 cho lượt Trending. UC004/003 chọn bài đủ điều kiện ở K0 và trả 20 bài đầu theo điểm giảm dần, bằng điểm thì thời điểm đăng sau trước. Danh sách chung dùng kết quả đã tính và phạm vi feed chính. | D45 P01–P20, K0, vị trí tải tiếp=P20. P02 thuộc Public GJ. Khả năng chuyển ba mục Trending được cung cấp. Banner thuộc các tab thời gian. | M3 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| M3 | ACT-001 | Guest cuộn đến cuối 20 bài đầu ở 10:22 để đọc tiếp. | Đã tải P01–P20, K0. K1 được tính lúc 10:20 và P21 lên vị trí 5 ở K1. | M4 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| M4 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | Tiếp tục K0, P21 vẫn là phần tử 21 trong thứ tự K0. P22 có nhãn BANNED, P23 được hiển thị như bài thường. Bài trả về=P21, P22, P23, P24, P25, P26, P27, P28, P29, P30, P31, P32, P33, P34, P35, P36, P37, P38, P39, P40, số lượng=20, vị trí tải tiếp=P40. | M5 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| M5 | ACT-001 | Guest cuộn tiếp để đọc phần cuối danh sách. | Đã tải P01–P40, K0, còn P41–P45. | M6 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| M6 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | K0 còn 5 bài, hoàn tất tập 45 bài và dừng tải thêm khi đã hết. Bài trả về=P41, P42, P43, P44, P45, số lượng=5, vị trí tải tiếp=P45. | END:SUCCESS | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |


#### 6. Các ngoại lệ

E thay bước ở cột at, guard xác định snapshot dữ liệu của đường đó từ đầu. V thay toàn bộ từ hành động đầu khi actor khởi tạo khác. Mỗi đường kết thúc theo hậu điều kiện cùng mã tại mục 4. Những tình huống còn thiếu hợp đồng được nêu riêng ở GAP.

<!-- sc:exceptions SC-M14-001 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Guest chọn lại Trending từ một tab khác ở 10:25 | E1.1 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| E2 | user-choice | M1 | Guest tải lại trang ở 10:25 | E2.1 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| E3 | user-choice | M3 | Guest chỉ chuyển mục con rồi trở lại Post, vẫn ở cùng lượt Trending | E3.1 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.08, FR-M14-02.09, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-22, BR-M14-23, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27 |
| E4 | system | M4 | P21 bị xóa mềm trước lần tải tiếp | E4.1 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M03-15.02, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| E5 | system | M4 | P21 bị Mod ẩn trước lần tải tiếp | E5.1 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M03-07.01, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| E6 | system | M4 | Tác giả riêng của P21 chuyển DEACTIVATED trước lần tải tiếp | E6.1 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M01-13.01, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| E7 | system | M4 | Tác giả riêng của P21 chuyển DELETED trước lần tải tiếp | E7.1 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M01-13.01, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| E8 | system | M4 | GJ chuyển từ Public sang Private trước lần tải tiếp, Guest ngoài nhóm | E8.1 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, BR-M11-14, BR-M11-15, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| E9 | system | M2 | Dữ liệu của lần tính minh họa chỉ có 12 bài đủ điều kiện | E9.1 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| E10 | system | M2 | Mọi cờ Group/Chat/Gamification đều Tắt | E10.1 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10 |
| E11 | user-choice | M1 | Group Tắt, Guest chọn mở bài nhóm được liệt kê | E11.1 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |
| E12 | user-choice | M1 | Guest mở lại bằng link một bài GJ sau khi GJ đã chuyển Private | E12.1 | BR-M11-15, BR-M14-23, FR-M11-03.06 |


<!-- sc:branch SC-M14-001 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-001 | Guest rời tab cũ và mở lại Trending ở 10:25. | K1=10:20 là kết quả gần nhất, bắt đầu lượt mới. | E1.2 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23 |
| E1.2 | SYSTEM | Hệ thống thiết lập lượt Trending mới với K1, mở Trending Post và chèn UC004/003 kiểm quyền hiện tại. Trả 20 bài đầu theo thứ tự K1. | K1 đầu danh sách=P01, P02, P03, P04, P21, P05, P06, P07, P08, P09, P10, P11, P12, P13, P14, P15, P16, P17, P18, P19, P21 ở vị trí 5. | END:SUCCESS | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |


<!-- sc:branch SC-M14-001 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-001 | Guest tải lại trang chủ ở 10:25. | K1=10:20 là kết quả gần nhất. | E2.2 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19 |
| E2.2 | SYSTEM | Hệ thống mở Trending Post mặc định, bắt đầu lượt mới dùng K1, kiểm quyền và trả 20 bài đầu. | K1=P01, P02, P03, P04, P21, P05, P06, P07, P08, P09, P10, P11, P12, P13, P14, P15, P16, P17, P18, P19, vị trí tải tiếp=P19. | END:SUCCESS | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |


<!-- sc:branch SC-M14-001 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-001 | Guest chọn Trending Topic trong cùng lượt Trending. | Lượt gắn K0, danh sách D-TOPIC sẵn có và ổn định. | E3.2 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| E3.2 | SYSTEM | Hệ thống nhận danh sách Topic điểm dương/thứ tự M05, dùng UC004 trả 20 mục đầu D-TOPIC. | T01–T20, còn T21–T23. | E3.3 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| E3.3 | ACT-001 | Guest trở lại Trending Post và cuộn đọc phần sau P20. | Vẫn lượt Trending bắt đầu 10:10, K0. | E3.4 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| E3.4 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | K0, phần sau P20 dù K1 đã có. Bài trả về=P21, P22, P23, P24, P25, P26, P27, P28, P29, P30, P31, P32, P33, P34, P35, P36, P37, P38, P39, P40, số lượng=20, vị trí tải tiếp=P40. | END:SUCCESS | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |


<!-- sc:branch SC-M14-001 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | K0, P21 bị loại ở lần tải hiện tại do P21 bị xóa mềm trước lần tải tiếp. Bài trả về=P22, P23, P24, P25, P26, P27, P28, P29, P30, P31, P32, P33, P34, P35, P36, P37, P38, P39, P40, P41, số lượng=20, vị trí tải tiếp=P41. | E4.2 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M03-15.02, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| E4.2 | ACT-001 | Guest cuộn tiếp đến phần cuối còn hợp lệ. | Vị trí tải tiếp=P41, còn P42–P45. | E4.3 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E4.3 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | K0 còn 4 bài sau P41, kết thúc tập đủ điều kiện. Bài trả về=P42, P43, P44, P45, số lượng=4, vị trí tải tiếp=P45. | END:SUCCESS | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M03-15.02, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |


<!-- sc:branch SC-M14-001 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | K0, P21 bị loại ở lần tải hiện tại do P21 bị Mod ẩn trước lần tải tiếp. Bài trả về=P22, P23, P24, P25, P26, P27, P28, P29, P30, P31, P32, P33, P34, P35, P36, P37, P38, P39, P40, P41, số lượng=20, vị trí tải tiếp=P41. | E5.2 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M03-07.01, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| E5.2 | ACT-001 | Guest cuộn tiếp đến phần cuối còn hợp lệ. | Vị trí tải tiếp=P41, còn P42–P45. | E5.3 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E5.3 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | K0 còn 4 bài sau P41, kết thúc tập đủ điều kiện. Bài trả về=P42, P43, P44, P45, số lượng=4, vị trí tải tiếp=P45. | END:SUCCESS | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M03-07.01, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |


<!-- sc:branch SC-M14-001 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | K0, P21 bị loại ở lần tải hiện tại do Tác giả riêng của P21 chuyển DEACTIVATED trước lần tải tiếp. Bài trả về=P22, P23, P24, P25, P26, P27, P28, P29, P30, P31, P32, P33, P34, P35, P36, P37, P38, P39, P40, P41, số lượng=20, vị trí tải tiếp=P41. | E6.2 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M01-13.01, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| E6.2 | ACT-001 | Guest cuộn tiếp đến phần cuối còn hợp lệ. | Vị trí tải tiếp=P41, còn P42–P45. | E6.3 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E6.3 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | K0 còn 4 bài sau P41, kết thúc tập đủ điều kiện. Bài trả về=P42, P43, P44, P45, số lượng=4, vị trí tải tiếp=P45. | END:SUCCESS | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M01-13.01, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |


<!-- sc:branch SC-M14-001 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | K0, P21 bị loại ở lần tải hiện tại do Tác giả riêng của P21 chuyển DELETED trước lần tải tiếp. Bài trả về=P22, P23, P24, P25, P26, P27, P28, P29, P30, P31, P32, P33, P34, P35, P36, P37, P38, P39, P40, P41, số lượng=20, vị trí tải tiếp=P41. | E7.2 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M01-13.01, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| E7.2 | ACT-001 | Guest cuộn tiếp đến phần cuối còn hợp lệ. | Vị trí tải tiếp=P41, còn P42–P45. | E7.3 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E7.3 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | K0 còn 4 bài sau P41, kết thúc tập đủ điều kiện. Bài trả về=P42, P43, P44, P45, số lượng=4, vị trí tải tiếp=P45. | END:SUCCESS | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M01-13.01, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |


<!-- sc:branch SC-M14-001 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. P02 của GJ đã hiện trên màn hình từ trước khi đổi tiếp tục được đọc theo BR-M11-15, quyền tương tác xét tại owner. | K0, P21 bị loại ở lần tải hiện tại do GJ chuyển từ Public sang Private trước lần tải tiếp, Guest ngoài nhóm. Bài trả về=P22, P23, P24, P25, P26, P27, P28, P29, P30, P31, P32, P33, P34, P35, P36, P37, P38, P39, P40, P41, số lượng=20, vị trí tải tiếp=P41. | E8.2 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, BR-M11-14, BR-M11-15, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| E8.2 | ACT-001 | Guest cuộn tiếp đến phần cuối còn hợp lệ. | Vị trí tải tiếp=P41, còn P42–P45. | E8.3 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E8.3 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | K0 còn 4 bài sau P41, kết thúc tập đủ điều kiện. Bài trả về=P42, P43, P44, P45, số lượng=4, vị trí tải tiếp=P45. | END:SUCCESS | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, BR-M11-14, BR-M11-15, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |


<!-- sc:branch SC-M14-001 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống mở Trending Post mặc định với kết quả đã có, chèn UC004/003 và trả đủ 12 bài hợp lệ theo thứ tự nguồn, dừng khi đã hết. | D-SMALL P01–P12, vị trí tải tiếp=P12, tổng hợp lệ=12. | END:SUCCESS | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |


<!-- sc:branch SC-M14-001 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống vẫn mở trang chủ Trending Post và dùng K0, kiểm phạm vi/quyền để trả P01–P20, gồm bài Public GJ. Số upvote tiếp tục hiển thị, điểm K0 theo tương tác đã tính. M14 cung cấp lối vào bài nhóm, cổng mở bài do M11 xử lý. | P01–P20, Group/Chat/Gamification=Tắt, P02 vẫn có trong danh sách. | END:SUCCESS | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10 |


<!-- sc:branch SC-M14-001 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-001 | Guest mở Trending Post để đọc danh sách. | Group=Tắt, dữ liệu chuẩn của SC, bài P02 được phép liệt kê. | E11.2 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10 |
| E11.2 | SYSTEM | Hệ thống hiển thị đủ bốn tab Trending, Following, Group, Newest và ba mục Trending Post/Topic/Tag, mở Trending Post mặc định. Ghi nhận K0 cho lượt Trending. UC004/003 chọn bài đủ điều kiện ở K0 và trả 20 bài đầu theo điểm giảm dần, bằng điểm thì thời điểm đăng sau trước. Danh sách chung dùng kết quả đã tính và phạm vi feed chính. | D45 P01–P20, K0, vị trí tải tiếp=P20. P02 thuộc Public GJ. Khả năng chuyển ba mục Trending được cung cấp. Banner thuộc các tab thời gian. Cờ Group=Tắt trong snapshot này. | E11.3 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10 |
| E11.3 | ACT-001 | Guest chọn mở bài nhóm P02. | Group=Tắt, người thao tác khác ADMIN. | E11.4 | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.01, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |
| E11.4 | SYSTEM | Hệ thống chuyển yêu cầu mở tới cổng M11, từ chối và hiển thị “Hệ thống đang bận, vui lòng thử lại sau”. | P02, yêu cầu mở bị từ chối do Group=Tắt. | END:REJECTED | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.01, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |


<!-- sc:branch SC-M14-001 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | ACT-001 | Guest mở lại P02 bằng link sau khi GJ chuyển Private. | P02 từng được tải trên màn hình khi GJ Public, hiện Guest ngoài GJ Private. Group Bật. | E12.2 | BR-M11-15 |
| E12.2 | SYSTEM | Hệ thống kiểm quyền M11 hiện tại và hiển thị “Nội dung không tồn tại” cho lượt mở lại. | Yêu cầu mở lại P02 bị từ chối theo quyền Private hiện tại. | END:REJECTED | BR-M14-23, BR-M11-15, FR-M11-03.06 |


**V1 — thay toàn bộ M1 đến kết thúc.** An đã đăng nhập thực hiện chức năng, cùng quyền đọc feed. Actor khởi tạo ACT-002, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-001 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-002 | An mở trang chủ iShare để đọc bài thịnh hành. | T=10:10, D45, kết quả hiện hành K0=10:00. | V1.2 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19 |
| V1.2 | SYSTEM | Hệ thống hiển thị đủ bốn tab Trending, Following, Group, Newest và ba mục Trending Post/Topic/Tag, mở Trending Post mặc định. Ghi nhận K0 cho lượt Trending. UC004/003 chọn bài đủ điều kiện ở K0 và trả 20 bài đầu theo điểm giảm dần, bằng điểm thì thời điểm đăng sau trước. Danh sách chung dùng kết quả đã tính và phạm vi feed chính. | D45 P01–P20, K0, vị trí tải tiếp=P20. P02 thuộc Public GJ. Khả năng chuyển ba mục Trending được cung cấp. Banner thuộc các tab thời gian. | V1.3 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| V1.3 | ACT-002 | An cuộn đến cuối 20 bài đầu ở 10:22 để đọc tiếp. | Đã tải P01–P20, K0. K1 được tính lúc 10:20 và P21 lên vị trí 5 ở K1. | V1.4 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| V1.4 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | Tiếp tục K0, P21 vẫn là phần tử 21 trong thứ tự K0. P22 có nhãn BANNED, P23 được hiển thị như bài thường. Bài trả về=P21, P22, P23, P24, P25, P26, P27, P28, P29, P30, P31, P32, P33, P34, P35, P36, P37, P38, P39, P40, số lượng=20, vị trí tải tiếp=P40. | V1.5 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| V1.5 | ACT-002 | An cuộn tiếp để đọc phần cuối danh sách. | Đã tải P01–P40, K0, còn P41–P45. | V1.6 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| V1.6 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | K0 còn 5 bài, hoàn tất tập 45 bài và dừng tải thêm khi đã hết. Bài trả về=P41, P42, P43, P44, P45, số lượng=5, vị trí tải tiếp=P45. | END:SUCCESS | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |


**V2 — thay toàn bộ M1 đến kết thúc.** Minh đã đăng nhập thực hiện chức năng, cùng quyền đọc feed. Actor khởi tạo ACT-008, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-001 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-008 | Minh mở trang chủ iShare để đọc bài thịnh hành. | T=10:10, D45, kết quả hiện hành K0=10:00. | V2.2 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19 |
| V2.2 | SYSTEM | Hệ thống hiển thị đủ bốn tab Trending, Following, Group, Newest và ba mục Trending Post/Topic/Tag, mở Trending Post mặc định. Ghi nhận K0 cho lượt Trending. UC004/003 chọn bài đủ điều kiện ở K0 và trả 20 bài đầu theo điểm giảm dần, bằng điểm thì thời điểm đăng sau trước. Danh sách chung dùng kết quả đã tính và phạm vi feed chính. | D45 P01–P20, K0, vị trí tải tiếp=P20. P02 thuộc Public GJ. Khả năng chuyển ba mục Trending được cung cấp. Banner thuộc các tab thời gian. | V2.3 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| V2.3 | ACT-008 | Minh cuộn đến cuối 20 bài đầu ở 10:22 để đọc tiếp. | Đã tải P01–P20, K0. K1 được tính lúc 10:20 và P21 lên vị trí 5 ở K1. | V2.4 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| V2.4 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | Tiếp tục K0, P21 vẫn là phần tử 21 trong thứ tự K0. P22 có nhãn BANNED, P23 được hiển thị như bài thường. Bài trả về=P21, P22, P23, P24, P25, P26, P27, P28, P29, P30, P31, P32, P33, P34, P35, P36, P37, P38, P39, P40, số lượng=20, vị trí tải tiếp=P40. | V2.5 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| V2.5 | ACT-008 | Minh cuộn tiếp để đọc phần cuối danh sách. | Đã tải P01–P40, K0, còn P41–P45. | V2.6 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| V2.6 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | K0 còn 5 bài, hoàn tất tập 45 bài và dừng tải thêm khi đã hết. Bài trả về=P41, P42, P43, P44, P45, số lượng=5, vị trí tải tiếp=P45. | END:SUCCESS | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |


**V3 — thay toàn bộ M1 đến kết thúc.** Hòa đã đăng nhập thực hiện chức năng, cùng quyền đọc feed. Actor khởi tạo ACT-007, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-001 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-007 | Hòa mở trang chủ iShare để đọc bài thịnh hành. | T=10:10, D45, kết quả hiện hành K0=10:00. | V3.2 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19 |
| V3.2 | SYSTEM | Hệ thống hiển thị đủ bốn tab Trending, Following, Group, Newest và ba mục Trending Post/Topic/Tag, mở Trending Post mặc định. Ghi nhận K0 cho lượt Trending. UC004/003 chọn bài đủ điều kiện ở K0 và trả 20 bài đầu theo điểm giảm dần, bằng điểm thì thời điểm đăng sau trước. Danh sách chung dùng kết quả đã tính và phạm vi feed chính. | D45 P01–P20, K0, vị trí tải tiếp=P20. P02 thuộc Public GJ. Khả năng chuyển ba mục Trending được cung cấp. Banner thuộc các tab thời gian. | V3.3 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| V3.3 | ACT-007 | Hòa cuộn đến cuối 20 bài đầu ở 10:22 để đọc tiếp. | Đã tải P01–P20, K0. K1 được tính lúc 10:20 và P21 lên vị trí 5 ở K1. | V3.4 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| V3.4 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | Tiếp tục K0, P21 vẫn là phần tử 21 trong thứ tự K0. P22 có nhãn BANNED, P23 được hiển thị như bài thường. Bài trả về=P21, P22, P23, P24, P25, P26, P27, P28, P29, P30, P31, P32, P33, P34, P35, P36, P37, P38, P39, P40, số lượng=20, vị trí tải tiếp=P40. | V3.5 | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |
| V3.5 | ACT-007 | Hòa cuộn tiếp để đọc phần cuối danh sách. | Đã tải P01–P40, K0, còn P41–P45. | V3.6 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| V3.6 | SYSTEM | Hệ thống mở UC004 và chèn UC003 cho danh sách bài. Kiểm trạng thái bài/tác giả/nhóm, phạm vi và quyền hiện tại. Trả các bài trong dữ liệu của lần tải này theo thứ tự nguồn, vị trí tải tiếp là bài cuối đã trả. Tại tên tác giả được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ theo nguồn. | K0 còn 5 bài, hoàn tất tập 45 bài và dừng tải thêm khi đã hết. Bài trả về=P41, P42, P43, P44, P45, số lượng=5, vị trí tải tiếp=P45. | END:SUCCESS | FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.08, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-22, BR-M14-23, FR-M14-01.05, FR-M14-01.06, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16 |


**V4 — thay toàn bộ M1 đến kết thúc.** Hòa ADMIN chọn mở bài nhóm khi Group Tắt. Actor khởi tạo ACT-007, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-001 V4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V4.1 | ACT-007 | Hòa mở Trending Post. | D-ADMIN, S01 thuộc Public GJ, bài thường Đã đăng/Bình thường, Hòa là thành viên GJ và đang theo dõi Topic Toán, Group=Tắt. | V4.2 | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M14-02.03, FR-M14-02.04, FR-M14-02.05, FR-M14-02.07, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23 |
| V4.2 | SYSTEM | Hệ thống kiểm phạm vi/quyền của tab và liệt kê S01 như lối vào. Hòa có cùng quy tắc xếp danh sách feed. | S01, Group=Tắt, đủ điều kiện tab. Với Trending có kết quả đã tính cho S01. | V4.3 | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-02.03, FR-M14-02.04, FR-M14-02.07, FR-M14-02.09, FR-M14-02.11, FR-M14-02.12, BR-M14-05, BR-M14-13, BR-M14-14, BR-M14-19, BR-M14-23 |
| V4.3 | ACT-007 | Hòa chọn mở bài nhóm S01. | Hòa ADMIN, vẫn có quyền nội dung nhóm. | V4.4 | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.01, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |
| V4.4 | SYSTEM | Hệ thống áp ngoại lệ ADMIN của M10/M11, kiểm quyền bài và trả bài S01 được phép mở. Hiển thị tiêu đề “Bài S01”, nội dung “Nội dung minh họa S01”, tác giả U, Lớp/Khối 11 và ngữ cảnh nhóm GJ, dữ liệu bài này có tập tệp/poll rỗng. | S01 Đã đăng/Bình thường, tác giả ACTIVE, Hòa nhận nội dung theo quyền hiện hành. | END:SUCCESS | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.01, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |


<!-- sc:end SC-M14-001 -->

<a id="sc-m14-002"></a>

<!-- sc:scenario SC-M14-002 -->

### SC-M14-002

#### 1. Tên kịch bản chuẩn

Khám phá danh sách Topic hoặc Tag thịnh hành đến hết các mục — BF-M14-002. Owner [UC-M14-002](../../us/US-M14.md#uc-m14-002).

#### 2. Actor thực hiện

ACT-001 khởi tạo đường chuẩn. Các đường V ghi actor khởi tạo khác theo cùng mục tiêu. Toàn iShare là SYSTEM, các quan hệ và dữ liệu owner được xử lý trong lượt SYSTEM.

#### 3. Tiền điều kiện

Guest đang ở tab Trending và chọn loại danh sách. Chuẩn D-TOPIC có 23 Topic điểm dương với kết quả/thứ tự M05 đã cung cấp. Tất cả Tag của nhánh D-TAG đang hoạt động. Danh mục và thứ tự ổn định trong đường này, thay đổi kết quả/danh mục giữa các lần tải thuộc GAP002.

#### 4. Hậu điều kiện

<!-- sc:post SC-M14-002 -->

| result | condition |
|---|---|
| SUCCESS | Người xem nhận mọi mục điểm dương của loại Topic/Tag đã chọn theo thứ tự M05, tối đa 20 mục mỗi lần tải và dừng khi hết. Các mục điểm 0 và Tag bị vô hiệu hóa thuộc phạm vi loại của M05. Phần giữ kết quả khi danh mục thay đổi tiếp tục theo GAP002. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M14-002 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-001 | Guest chọn Trending Topic. | D-TOPIC, 23 mục có điểm >0. | M2 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| M2 | SYSTEM | Hệ thống nhận danh sách/thứ tự Topic M05 cung cấp, chỉ lấy mục điểm dương và Tag đang hoạt động nếu là Tag. UC004 trả phần sau vị trí đã tải, tối đa 20 mục, theo cùng ngữ cảnh lượt Trending. Danh sách mục sử dụng thứ tự M05. | Topic trả T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, số lượng=20, vị trí tải tiếp=T20. Còn 3 mục. | M3 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| M3 | ACT-001 | Guest cuộn đến cuối 20 Topic đầu để đọc tiếp. | Vị trí tải tiếp=T20, còn T21–T23. | M4 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| M4 | SYSTEM | Hệ thống nhận danh sách/thứ tự Topic M05 cung cấp, chỉ lấy mục điểm dương và Tag đang hoạt động nếu là Tag. UC004 trả phần sau vị trí đã tải, tối đa 20 mục, theo cùng ngữ cảnh lượt Trending. Danh sách mục sử dụng thứ tự M05. | Topic trả T21, T22, T23, số lượng=3, vị trí tải tiếp=T23. Đã hết 23 mục. | END:SUCCESS | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |


#### 6. Các ngoại lệ

E thay bước ở cột at, guard xác định snapshot dữ liệu của đường đó từ đầu. V thay toàn bộ từ hành động đầu khi actor khởi tạo khác. Mỗi đường kết thúc theo hậu điều kiện cùng mã tại mục 4. Những tình huống còn thiếu hợp đồng được nêu riêng ở GAP.

<!-- sc:exceptions SC-M14-002 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Guest chọn Trending Tag | E1.1 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| E2 | system | M2 | Danh sách M05 có mục điểm 0 hoặc Tag bị vô hiệu hóa từ trước lượt xem | E2.1 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| E3 | system | M2 | M05 cung cấp bốn Topic có điểm bằng nhau từng phần để đối soát thứ tự | E3.1 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| E4 | user-choice | M1 | Guest chọn Tag với danh mục đã loại Tag vô hiệu hóa trước lượt xem | E4.1 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |


<!-- sc:branch SC-M14-002 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-001 | Guest chọn Trending Tag. | D-TAG có 23 Tag hoạt động, điểm >0. | E1.2 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| E1.2 | SYSTEM | Hệ thống nhận danh sách/thứ tự Tag M05 cung cấp, chỉ lấy mục điểm dương và Tag đang hoạt động nếu là Tag. UC004 trả phần sau vị trí đã tải, tối đa 20 mục, theo cùng ngữ cảnh lượt Trending. Danh sách mục sử dụng thứ tự M05. | Tag trả TG01, TG02, TG03, TG04, TG05, TG06, TG07, TG08, TG09, TG10, TG11, TG12, TG13, TG14, TG15, TG16, TG17, TG18, TG19, TG20, số lượng=20, vị trí tải tiếp=TG20. Còn 3 mục. | E1.3 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| E1.3 | ACT-001 | Guest cuộn để đọc phần Tag còn lại. | Vị trí tải tiếp=TG20. | E1.4 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| E1.4 | SYSTEM | Hệ thống nhận danh sách/thứ tự Tag M05 cung cấp, chỉ lấy mục điểm dương và Tag đang hoạt động nếu là Tag. UC004 trả phần sau vị trí đã tải, tối đa 20 mục, theo cùng ngữ cảnh lượt Trending. Danh sách mục sử dụng thứ tự M05. | Tag trả TG21, TG22, TG23, số lượng=3, vị trí tải tiếp=TG23. Đã hết 23 mục. | END:SUCCESS | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |


<!-- sc:branch SC-M14-002 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống sử dụng tập M05 đang cung cấp gồm T01–T23 điểm dương, loại T00 điểm 0. Với nhánh Tag, TG-DISABLED bị vô hiệu hóa nằm ngoài danh sách M05 cung cấp. UC004 trả T01–T20 theo đúng thứ tự. | D-TOPIC T00=0, T01–T23>0. D-TAG TG-DISABLED bị vô hiệu hóa trước lượt, TG00=0. | E2.2 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| E2.2 | ACT-001 | Guest cuộn đến cuối phần đã tải. | Tải tiếp sau T20. | E2.3 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| E2.3 | SYSTEM | Hệ thống nhận danh sách/thứ tự Topic M05 cung cấp, chỉ lấy mục điểm dương và Tag đang hoạt động nếu là Tag. UC004 trả phần sau vị trí đã tải, tối đa 20 mục, theo cùng ngữ cảnh lượt Trending. Danh sách mục sử dụng thứ tự M05. | Topic trả T21, T22, T23, số lượng=3, vị trí tải tiếp=T23. Đã hết 23 mục. | END:SUCCESS | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |


<!-- sc:branch SC-M14-002 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống giữ nguyên danh sách và thứ tự M05 cung cấp. Trả 4 mục điểm dương trong bộ D-TIE, đã hết danh sách. | Ngữ văn 12 điểm/0 bài mới, Tin học 10/2, Hướng nghiệp 10/1, Toán học 10/1. Thứ tự Ngữ văn → Tin học → Hướng nghiệp → Toán học. | END:SUCCESS | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |


<!-- sc:branch SC-M14-002 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-001 | Guest chọn Trending Tag. | D-TAG có TG01–TG23 hoạt động/điểm dương. TG-DISABLED bị vô hiệu hóa, TG00 điểm 0. | E4.2 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| E4.2 | SYSTEM | Hệ thống nhận danh sách/thứ tự Tag M05 cung cấp, chỉ lấy mục điểm dương và Tag đang hoạt động nếu là Tag. UC004 trả phần sau vị trí đã tải, tối đa 20 mục, theo cùng ngữ cảnh lượt Trending. Danh sách mục sử dụng thứ tự M05. | Tag trả TG01, TG02, TG03, TG04, TG05, TG06, TG07, TG08, TG09, TG10, TG11, TG12, TG13, TG14, TG15, TG16, TG17, TG18, TG19, TG20, số lượng=20, vị trí tải tiếp=TG20. Còn 3 mục. | E4.3 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| E4.3 | ACT-001 | Guest cuộn xem Tag còn lại. | Sau TG20. | E4.4 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| E4.4 | SYSTEM | Hệ thống nhận danh sách/thứ tự Tag M05 cung cấp, chỉ lấy mục điểm dương và Tag đang hoạt động nếu là Tag. UC004 trả phần sau vị trí đã tải, tối đa 20 mục, theo cùng ngữ cảnh lượt Trending. Danh sách mục sử dụng thứ tự M05. | Tag trả TG21, TG22, TG23, số lượng=3, vị trí tải tiếp=TG23. Đã hết 23 mục. | END:SUCCESS | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |


**V1 — thay toàn bộ M1 đến kết thúc.** An đã đăng nhập thực hiện chức năng, cùng quyền đọc feed. Actor khởi tạo ACT-002, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-002 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-002 | An chọn Trending Topic. | D-TOPIC, 23 mục có điểm >0. | V1.2 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| V1.2 | SYSTEM | Hệ thống nhận danh sách/thứ tự Topic M05 cung cấp, chỉ lấy mục điểm dương và Tag đang hoạt động nếu là Tag. UC004 trả phần sau vị trí đã tải, tối đa 20 mục, theo cùng ngữ cảnh lượt Trending. Danh sách mục sử dụng thứ tự M05. | Topic trả T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, số lượng=20, vị trí tải tiếp=T20. Còn 3 mục. | V1.3 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| V1.3 | ACT-002 | An cuộn đến cuối 20 Topic đầu để đọc tiếp. | Vị trí tải tiếp=T20, còn T21–T23. | V1.4 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| V1.4 | SYSTEM | Hệ thống nhận danh sách/thứ tự Topic M05 cung cấp, chỉ lấy mục điểm dương và Tag đang hoạt động nếu là Tag. UC004 trả phần sau vị trí đã tải, tối đa 20 mục, theo cùng ngữ cảnh lượt Trending. Danh sách mục sử dụng thứ tự M05. | Topic trả T21, T22, T23, số lượng=3, vị trí tải tiếp=T23. Đã hết 23 mục. | END:SUCCESS | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |


**V2 — thay toàn bộ M1 đến kết thúc.** Minh đã đăng nhập thực hiện chức năng, cùng quyền đọc feed. Actor khởi tạo ACT-008, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-002 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-008 | Minh chọn Trending Topic. | D-TOPIC, 23 mục có điểm >0. | V2.2 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| V2.2 | SYSTEM | Hệ thống nhận danh sách/thứ tự Topic M05 cung cấp, chỉ lấy mục điểm dương và Tag đang hoạt động nếu là Tag. UC004 trả phần sau vị trí đã tải, tối đa 20 mục, theo cùng ngữ cảnh lượt Trending. Danh sách mục sử dụng thứ tự M05. | Topic trả T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, số lượng=20, vị trí tải tiếp=T20. Còn 3 mục. | V2.3 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| V2.3 | ACT-008 | Minh cuộn đến cuối 20 Topic đầu để đọc tiếp. | Vị trí tải tiếp=T20, còn T21–T23. | V2.4 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| V2.4 | SYSTEM | Hệ thống nhận danh sách/thứ tự Topic M05 cung cấp, chỉ lấy mục điểm dương và Tag đang hoạt động nếu là Tag. UC004 trả phần sau vị trí đã tải, tối đa 20 mục, theo cùng ngữ cảnh lượt Trending. Danh sách mục sử dụng thứ tự M05. | Topic trả T21, T22, T23, số lượng=3, vị trí tải tiếp=T23. Đã hết 23 mục. | END:SUCCESS | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |


**V3 — thay toàn bộ M1 đến kết thúc.** Hòa đã đăng nhập thực hiện chức năng, cùng quyền đọc feed. Actor khởi tạo ACT-007, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-002 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-007 | Hòa chọn Trending Topic. | D-TOPIC, 23 mục có điểm >0. | V3.2 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| V3.2 | SYSTEM | Hệ thống nhận danh sách/thứ tự Topic M05 cung cấp, chỉ lấy mục điểm dương và Tag đang hoạt động nếu là Tag. UC004 trả phần sau vị trí đã tải, tối đa 20 mục, theo cùng ngữ cảnh lượt Trending. Danh sách mục sử dụng thứ tự M05. | Topic trả T01, T02, T03, T04, T05, T06, T07, T08, T09, T10, T11, T12, T13, T14, T15, T16, T17, T18, T19, T20, số lượng=20, vị trí tải tiếp=T20. Còn 3 mục. | V3.3 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| V3.3 | ACT-007 | Hòa cuộn đến cuối 20 Topic đầu để đọc tiếp. | Vị trí tải tiếp=T20, còn T21–T23. | V3.4 | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| V3.4 | SYSTEM | Hệ thống nhận danh sách/thứ tự Topic M05 cung cấp, chỉ lấy mục điểm dương và Tag đang hoạt động nếu là Tag. UC004 trả phần sau vị trí đã tải, tối đa 20 mục, theo cùng ngữ cảnh lượt Trending. Danh sách mục sử dụng thứ tự M05. | Topic trả T21, T22, T23, số lượng=3, vị trí tải tiếp=T23. Đã hết 23 mục. | END:SUCCESS | FR-M14-02.01, FR-M14-02.02, FR-M14-02.06, FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, BR-M14-19, BR-M14-24, FR-M05-05.07, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |


<!-- sc:end SC-M14-002 -->

<a id="sc-m14-003"></a>

<!-- sc:scenario SC-M14-003 -->

### SC-M14-003

#### 1. Tên kịch bản chuẩn

Đọc bài từ người dùng và Topic chính mình đang theo dõi — BF-M14-003. Owner [UC-M14-021](../../us/US-M14.md#uc-m14-021).

#### 2. Actor thực hiện

ACT-002 khởi tạo đường chuẩn. Các đường V ghi actor khởi tạo khác theo cùng mục tiêu. Toàn iShare là SYSTEM, các quan hệ và dữ liệu owner được xử lý trong lượt SYSTEM.

#### 3. Tiền điều kiện

An đang mở feed với dữ liệu D-SET. Chuẩn An ACTIVE/SETUP_COMPLETED, đang theo dõi U và Topic Toán, là Member GJ Public/GK Private/GH bị ẩn. Các quan hệ do M07/M11 cung cấp tại lần tải. Những trường hợp chưa theo dõi được xử lý trong E, Guest trong V.

#### 4. Hậu điều kiện

<!-- sc:post SC-M14-003 -->

| result | condition |
|---|---|
| SUCCESS | An nhận dòng bài đúng quan hệ người dùng/Topic hiện tại và quyền hiển thị, mỗi bài một lần, thời điểm đăng sau trước. Bài ẩn danh đủ điều kiện qua Topic được hiển thị Ẩn danh. Tab rỗng có nút dẫn sang tìm kiếm. Tải tiếp dùng quan hệ hiện tại. |
| REJECTED | Guest được yêu cầu đăng nhập khi yêu cầu Following. Feed có thể đã được liệt kê trước lựa chọn mở bài nhóm, cổng M11 từ chối mở theo điều kiện cờ/quyền của owner. |
| HANDED_OFF | An chọn nút tìm kiếm từ trạng thái rỗng, iShare mở trang tìm kiếm M06 để nhận mục tiêu tìm kiếm tiếp theo. Kết quả Following rỗng đã được trả đúng nguồn. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M14-003 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | An chọn tab Following. | D-SET, follows={U,Toán}, các cờ Bật. | M2 | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15 |
| M2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và quan hệ theo dõi của chính người xem. Giữ bài ngoài nhóm/nhóm Public có tác giả được theo dõi hoặc Topic được theo dõi. Bài ẩn danh chỉ thỏa qua Topic, mọi bài Private bị loại. Mỗi bài chỉ được trả một lần, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-SET, Q03 thỏa cả U và Toán nên chỉ có một lần. Q08 hiện Ẩn danh. Q07 ẩn danh/Văn bị loại dù theo dõi U, Q06 Private bị loại dù An là thành viên. Q11 có nhãn BANNED, Q12 hiển thị bình thường, đã hết 8 bài. Bài trả về=Q12, Q11, Q09, Q08, Q05, Q03, Q02, Q01, số lượng=8, vị trí tải tiếp=Q01. | END:SUCCESS | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


#### 6. Các ngoại lệ

E thay bước ở cột at, guard xác định snapshot dữ liệu của đường đó từ đầu. V thay toàn bộ từ hành động đầu khi actor khởi tạo khác. Mỗi đường kết thúc theo hậu điều kiện cùng mã tại mục 4. Những tình huống còn thiếu hợp đồng được nêu riêng ở GAP.

<!-- sc:exceptions SC-M14-003 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Người xem đọc hết bộ 45 bài của Following qua các lần cuộn | E1.1 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27 |
| E2 | system | M1 | Có ba bài mới được đăng sau trang đầu, actor tiếp tục đọc phần cũ | E2.1 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27 |
| E3 | system | M1 | An đã bỏ theo dõi U trước lần tải kế tiếp, vẫn theo dõi Topic Toán | E3.1 | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27 |
| E4 | system | M2 | Cờ Group và Gamification Tắt, quan hệ D-SET còn hiệu lực | E4.1 | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E5 | system | M2 | An chưa theo dõi người dùng hoặc Topic nào | E5.1 | FR-M14-04.05, BR-M14-20 |
| E6 | user-choice | M2 | An chưa theo dõi người dùng hoặc Topic nào, An chọn tiếp lối tìm kiếm | E6.1 | FR-M14-04.05, BR-M14-20, FR-M06-02.31 |
| E7 | system | M2 | An đã theo dõi U/Toán nhưng snapshot này chưa có bài phù hợp | E7.1 | FR-M14-04.11, BR-M14-20 |
| E8 | user-choice | M2 | An đã theo dõi U/Toán nhưng snapshot này chưa có bài phù hợp, An chọn tiếp lối tìm kiếm | E8.1 | FR-M14-04.11, BR-M14-20, FR-M06-02.31 |
| E9 | user-choice | M1 | Group Tắt, An chọn mở bài nhóm được liệt kê | E9.1 | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-05.08, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |


<!-- sc:branch SC-M14-003 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | An mở Following. | D-TIME45-F, 45 bài của U, Topic Văn trừ R21 có Toán, An theo dõi U và Toán, thời điểm đăng R01>R02>…>R45. | E1.2 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15 |
| E1.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và quan hệ theo dõi của chính người xem. Giữ bài ngoài nhóm/nhóm Public có tác giả được theo dõi hoặc Topic được theo dõi. Bài ẩn danh chỉ thỏa qua Topic, mọi bài Private bị loại. Mỗi bài chỉ được trả một lần, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-TIME45-F, 45 bài của U, Topic Văn trừ R21 có Toán, An theo dõi U và Toán, lần đầu 20 bài. Bài trả về=R01, R02, R03, R04, R05, R06, R07, R08, R09, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, số lượng=20, vị trí tải tiếp=R20. | E1.3 | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E1.3 | ACT-002 | An cuộn đọc tiếp sau R20. | D-TIME45-F, 45 bài của U, Topic Văn trừ R21 có Toán, An theo dõi U và Toán, vị trí tải tiếp=R20. | E1.4 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E1.4 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và quan hệ theo dõi của chính người xem. Giữ bài ngoài nhóm/nhóm Public có tác giả được theo dõi hoặc Topic được theo dõi. Bài ẩn danh chỉ thỏa qua Topic, mọi bài Private bị loại. Mỗi bài chỉ được trả một lần, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-TIME45-F, 45 bài của U, Topic Văn trừ R21 có Toán, An theo dõi U và Toán, lần hai 20 bài. Bài trả về=R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, số lượng=20, vị trí tải tiếp=R40. | E1.5 | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E1.5 | ACT-002 | An cuộn đọc phần còn lại sau R40. | D-TIME45-F, 45 bài của U, Topic Văn trừ R21 có Toán, An theo dõi U và Toán, còn 5 bài. | E1.6 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E1.6 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và quan hệ theo dõi của chính người xem. Giữ bài ngoài nhóm/nhóm Public có tác giả được theo dõi hoặc Topic được theo dõi. Bài ẩn danh chỉ thỏa qua Topic, mọi bài Private bị loại. Mỗi bài chỉ được trả một lần, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-TIME45-F, 45 bài của U, Topic Văn trừ R21 có Toán, An theo dõi U và Toán, đã hết 45 bài và dừng tải thêm. Bài trả về=R41, R42, R43, R44, R45, số lượng=5, vị trí tải tiếp=R45. | END:SUCCESS | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


<!-- sc:branch SC-M14-003 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | An cuộn tiếp tab Following sau R20 đã tải. | D-TIME45-F, 45 bài của U, Topic Văn trừ R21 có Toán, An theo dõi U và Toán, R01 mới nhất đang hiện lúc 10:00. N01/N02/N03 mới hơn R01 và thuộc tab được đăng lúc 10:01:01–03. | E2.2 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E2.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và quan hệ theo dõi của chính người xem. Giữ bài ngoài nhóm/nhóm Public có tác giả được theo dõi hoặc Topic được theo dõi. Bài ẩn danh chỉ thỏa qua Topic, mọi bài Private bị loại. Mỗi bài chỉ được trả một lần, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-TIME45-F, 45 bài của U, Topic Văn trừ R21 có Toán, An theo dõi U và Toán, tải sau R20. AUT002 có thể báo ba bài mới theo hạn 60 giây, danh sách được trả ở lượt cuộn này tiếp tục R21–R40. Bài trả về=R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, số lượng=20, vị trí tải tiếp=R40. | END:SUCCESS | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


<!-- sc:branch SC-M14-003 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-002 | An cuộn tiếp Following sau R20 đã tải. | D-TIME45-F, M07 đã xóa follows(U), follows(Toán) còn. Chỉ R21 trong phần chưa tải gắn Toán. | E3.2 | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E3.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và quan hệ theo dõi của chính người xem. Giữ bài ngoài nhóm/nhóm Public có tác giả được theo dõi hoặc Topic được theo dõi. Bài ẩn danh chỉ thỏa qua Topic, mọi bài Private bị loại. Mỗi bài chỉ được trả một lần, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | Quan hệ hiện tại chỉ còn Toán, R21 vẫn thỏa nên được trả một lần. R22–R45 chỉ nhờ U đã bỏ nên bị loại, phần chưa tải đã hết. Bài trả về=R21, số lượng=1, vị trí tải tiếp=R21. | END:SUCCESS | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


<!-- sc:branch SC-M14-003 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và quan hệ theo dõi của chính người xem. Giữ bài ngoài nhóm/nhóm Public có tác giả được theo dõi hoặc Topic được theo dõi. Bài ẩn danh chỉ thỏa qua Topic, mọi bài Private bị loại. Mỗi bài chỉ được trả một lần, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | Q05/Q08/Q09 Public vẫn là lối vào, số upvote/nhãn BANNED tiếp tục hiển thị, mở bài nhóm theo M11. Group/Gamification=Tắt. Bài trả về=Q12, Q11, Q09, Q08, Q05, Q03, Q02, Q01, số lượng=8, vị trí tải tiếp=Q01. | END:SUCCESS | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


<!-- sc:branch SC-M14-003 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống kiểm phiên và quan hệ của An, xác định Following rỗng và hiển thị nút dẫn sang trang tìm kiếm. | An chưa theo dõi người dùng hoặc Topic nào, Following=[] cùng lối sang M06. | END:SUCCESS | FR-M14-04.05, BR-M14-20 |


<!-- sc:branch SC-M14-003 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống kiểm phiên và quan hệ của An, xác định Following rỗng và hiển thị nút dẫn sang trang tìm kiếm. | An chưa theo dõi người dùng hoặc Topic nào, Following=[] cùng lối sang M06. | E6.2 | FR-M14-04.05, BR-M14-20 |
| E6.2 | ACT-002 | An bấm nút dẫn sang trang tìm kiếm. | Chọn M06 từ trạng thái Following rỗng. | E6.3 | FR-M14-04.05, BR-M14-20 |
| E6.3 | SYSTEM | Hệ thống mở trang tìm kiếm M06 để tiếp nhận mục tiêu tìm kiếm của An. Dữ liệu minh họa chưa có truy vấn hoặc bộ lọc gửi đi. | M06 nhận ngữ cảnh trang tìm kiếm, query trống/filter trống nên chưa chạy tìm theo FR-M06-02.31. | END:HANDED_OFF | FR-M14-04.05, BR-M14-20, FR-M06-02.31 |


<!-- sc:branch SC-M14-003 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống kiểm phiên và quan hệ của An, xác định Following rỗng và hiển thị nút dẫn sang trang tìm kiếm. | An đã theo dõi U/Toán nhưng snapshot này chưa có bài phù hợp, Following=[] cùng lối sang M06. | END:SUCCESS | FR-M14-04.11, BR-M14-20 |


<!-- sc:branch SC-M14-003 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống kiểm phiên và quan hệ của An, xác định Following rỗng và hiển thị nút dẫn sang trang tìm kiếm. | An đã theo dõi U/Toán nhưng snapshot này chưa có bài phù hợp, Following=[] cùng lối sang M06. | E8.2 | FR-M14-04.11, BR-M14-20 |
| E8.2 | ACT-002 | An bấm nút dẫn sang trang tìm kiếm. | Chọn M06 từ trạng thái Following rỗng. | E8.3 | FR-M14-04.11, BR-M14-20 |
| E8.3 | SYSTEM | Hệ thống mở trang tìm kiếm M06 để tiếp nhận mục tiêu tìm kiếm của An. Dữ liệu minh họa chưa có truy vấn hoặc bộ lọc gửi đi. | M06 nhận ngữ cảnh trang tìm kiếm, query trống/filter trống nên chưa chạy tìm theo FR-M06-02.31. | END:HANDED_OFF | FR-M14-04.11, BR-M14-20, FR-M06-02.31 |


<!-- sc:branch SC-M14-003 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | ACT-002 | An mở Following để đọc danh sách. | Group=Tắt, dữ liệu chuẩn của SC, bài Q05 được phép liệt kê. | E9.2 | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-05.08, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10 |
| E9.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và quan hệ theo dõi của chính người xem. Giữ bài ngoài nhóm/nhóm Public có tác giả được theo dõi hoặc Topic được theo dõi. Bài ẩn danh chỉ thỏa qua Topic, mọi bài Private bị loại. Mỗi bài chỉ được trả một lần, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-SET, Q03 thỏa cả U và Toán nên chỉ có một lần. Q08 hiện Ẩn danh. Q07 ẩn danh/Văn bị loại dù theo dõi U, Q06 Private bị loại dù An là thành viên. Q11 có nhãn BANNED, Q12 hiển thị bình thường, đã hết 8 bài. Bài trả về=Q12, Q11, Q09, Q08, Q05, Q03, Q02, Q01, số lượng=8, vị trí tải tiếp=Q01. Cờ Group=Tắt trong snapshot này. | E9.3 | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-05.08, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10 |
| E9.3 | ACT-002 | An chọn mở bài nhóm Q05. | Group=Tắt, người thao tác khác ADMIN. | E9.4 | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.01, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |
| E9.4 | SYSTEM | Hệ thống chuyển yêu cầu mở tới cổng M11, từ chối và hiển thị “Hệ thống đang bận, vui lòng thử lại sau”. | Q05, yêu cầu mở bị từ chối do Group=Tắt. | END:REJECTED | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.01, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |


**V1 — thay toàn bộ M1 đến kết thúc.** Guest chọn Following. Actor khởi tạo ACT-001, kết thúc END:REJECTED.

<!-- sc:role-path SC-M14-003 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest chọn tab Following. | Tab vẫn hiện cho Guest. | V1.2 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-08, BR-M14-09, BR-M14-20, FR-M07-01.01, BR-M07-15 |
| V1.2 | SYSTEM | Hệ thống kiểm phiên và yêu cầu đăng nhập để xem Following. | Guest chưa nhận bài của Following. | END:REJECTED | FR-M14-04.04, BR-M14-02 |


**V2 — thay toàn bộ M1 đến kết thúc.** Minh xem Following theo các quan hệ của chính mình. Actor khởi tạo ACT-008, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-003 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-008 | Minh chọn Following. | D-STAFF, S02 đăng 09:02 > S01 09:01, tác giả ACTIVE, bài thường. S01 ngoài nhóm của U/Toán, S02 Public GJ của V/Toán, Minh theo dõi U/Toán. | V2.2 | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15 |
| V2.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và quan hệ theo dõi của chính người xem. Giữ bài ngoài nhóm/nhóm Public có tác giả được theo dõi hoặc Topic được theo dõi. Bài ẩn danh chỉ thỏa qua Topic, mọi bài Private bị loại. Mỗi bài chỉ được trả một lần, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-STAFF, S01 ngoài nhóm của U/Toán, S02 Public GJ của V/Toán, Minh theo dõi U/Toán, hai bài đủ điều kiện. Bài trả về=S02, S01, số lượng=2, vị trí tải tiếp=S01. | END:SUCCESS | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


**V3 — thay toàn bộ M1 đến kết thúc.** Hòa xem Following theo các quan hệ của chính mình. Actor khởi tạo ACT-007, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-003 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-007 | Hòa chọn Following. | D-STAFF, S02 đăng 09:02 > S01 09:01, tác giả ACTIVE, bài thường. S01 ngoài nhóm của U/Toán, S02 Public GJ của V/Toán, Hòa theo dõi U/Toán. | V3.2 | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15 |
| V3.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và quan hệ theo dõi của chính người xem. Giữ bài ngoài nhóm/nhóm Public có tác giả được theo dõi hoặc Topic được theo dõi. Bài ẩn danh chỉ thỏa qua Topic, mọi bài Private bị loại. Mỗi bài chỉ được trả một lần, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-STAFF, S01 ngoài nhóm của U/Toán, S02 Public GJ của V/Toán, Hòa theo dõi U/Toán, hai bài đủ điều kiện. Bài trả về=S02, S01, số lượng=2, vị trí tải tiếp=S01. | END:SUCCESS | FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


**V4 — thay toàn bộ M1 đến kết thúc.** Hòa ADMIN chọn mở bài nhóm khi Group Tắt. Actor khởi tạo ACT-007, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-003 V4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V4.1 | ACT-007 | Hòa mở Following. | D-ADMIN, S01 thuộc Public GJ, bài thường Đã đăng/Bình thường, Hòa là thành viên GJ và đang theo dõi Topic Toán, Group=Tắt. | V4.2 | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, FR-M07-01.01, BR-M07-15 |
| V4.2 | SYSTEM | Hệ thống kiểm phạm vi/quyền của tab và liệt kê S01 như lối vào. Hòa có cùng quy tắc xếp danh sách feed. | S01, Group=Tắt, đủ điều kiện tab. Với Trending có kết quả đã tính cho S01. | V4.3 | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-09, BR-M14-20, FR-M07-01.01, BR-M07-15 |
| V4.3 | ACT-007 | Hòa chọn mở bài nhóm S01. | Hòa ADMIN, vẫn có quyền nội dung nhóm. | V4.4 | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.01, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |
| V4.4 | SYSTEM | Hệ thống áp ngoại lệ ADMIN của M10/M11, kiểm quyền bài và trả bài S01 được phép mở. Hiển thị tiêu đề “Bài S01”, nội dung “Nội dung minh họa S01”, tác giả U, Lớp/Khối 11 và ngữ cảnh nhóm GJ, dữ liệu bài này có tập tệp/poll rỗng. | S01 Đã đăng/Bình thường, tác giả ACTIVE, Hòa nhận nội dung theo quyền hiện hành. | END:SUCCESS | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.01, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |


<!-- sc:end SC-M14-003 -->

<a id="sc-m14-004"></a>

<!-- sc:scenario SC-M14-004 -->

### SC-M14-004

#### 1. Tên kịch bản chuẩn

Đọc bài từ mọi nhóm chính mình đang tham gia — BF-M14-004. Owner [UC-M14-022](../../us/US-M14.md#uc-m14-022).

#### 2. Actor thực hiện

ACT-002 khởi tạo đường chuẩn. Các đường V ghi actor khởi tạo khác theo cùng mục tiêu. Toàn iShare là SYSTEM, các quan hệ và dữ liệu owner được xử lý trong lượt SYSTEM.

#### 3. Tiền điều kiện

An đang ở feed với D-SET, là Member GJ Public/GK Private và còn quan hệ thành viên GH bị ẩn. Chuẩn có phiên ACTIVE/SETUP_COMPLETED, Group Bật. Quyền thành viên, điều kiện bài/nhóm được kiểm trong lần tải. Nhánh chưa tham gia và đã tham gia nhưng rỗng có dữ liệu riêng.

#### 4. Hậu điều kiện

<!-- sc:post SC-M14-004 -->

| result | condition |
|---|---|
| SUCCESS | An nhận bài đủ điều kiện của các nhóm hiện tham gia, Public/Private, theo thời điểm đăng sau trước. Tab rỗng có Khám phá Group. Từ lần tải sau khi rời nhóm, bài của nhóm đã rời bị loại. Cờ Group Tắt vẫn cho liệt kê tại feed theo nguồn. |
| REJECTED | Guest được yêu cầu đăng nhập khi yêu cầu Group. Khi lựa chọn mở bài nhóm gặp cổng Group Tắt hoặc thiếu quyền, yêu cầu mở bị M11 từ chối theo nguồn. |
| HANDED_OFF | An chọn Khám phá Group từ trạng thái rỗng và nhận trang danh sách nhóm M11 đúng quyền, tên/mô tả/chế độ và thứ tự thời điểm tạo. Yêu cầu duyệt nguồn bài Group rỗng đã hoàn tất. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M14-004 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | An chọn tab Group. | D-SET, membership={GJ,GK,GH}. | M2 | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14 |
| M2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và nhóm người xem hiện tham gia, gồm Public/Private. Chỉ giữ bài thuộc nhóm hiện tham gia và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-SET, Q08/Q07 hiện Ẩn danh với An là Member thường, Q06 của Private GK được hiển thị, Q09 Public GO bị loại vì An ngoài nhóm. GH bị ẩn và bài đã gỡ khỏi GJ bị loại, đã hết 4 bài. Bài trả về=Q08, Q07, Q06, Q05, số lượng=4, vị trí tải tiếp=Q05. | END:SUCCESS | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


#### 6. Các ngoại lệ

E thay bước ở cột at, guard xác định snapshot dữ liệu của đường đó từ đầu. V thay toàn bộ từ hành động đầu khi actor khởi tạo khác. Mỗi đường kết thúc theo hậu điều kiện cùng mã tại mục 4. Những tình huống còn thiếu hợp đồng được nêu riêng ở GAP.

<!-- sc:exceptions SC-M14-004 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Người xem đọc hết bộ 45 bài của Group qua các lần cuộn | E1.1 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27 |
| E2 | system | M1 | Có ba bài mới được đăng sau trang đầu, actor tiếp tục đọc phần cũ | E2.1 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27 |
| E3 | system | M1 | An đã rời Public GJ trước lần tải kế tiếp, vẫn là thành viên Private GK | E3.1 | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27 |
| E4 | system | M2 | Cờ Group Tắt, thành viên D-SET còn hiệu lực | E4.1 | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E5 | system | M2 | An chưa tham gia nhóm nào | E5.1 | FR-M14-05.06, BR-M14-21 |
| E6 | user-choice | M2 | An chưa tham gia nhóm nào, An chọn Khám phá Group | E6.1 | FR-M14-05.06, BR-M14-21, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, FR-M11-03.11, FR-M11-03.16, FR-M11-03.17, FR-M11-17.07 |
| E7 | system | M2 | An đã tham gia GJ/GK nhưng snapshot này chưa có bài đủ điều kiện | E7.1 | FR-M14-05.07, BR-M14-21 |
| E8 | user-choice | M2 | An đã tham gia GJ/GK nhưng snapshot này chưa có bài đủ điều kiện, An chọn Khám phá Group | E8.1 | FR-M14-05.07, BR-M14-21, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, FR-M11-03.11, FR-M11-03.16, FR-M11-03.17, FR-M11-17.07 |
| E9 | user-choice | M1 | Group Tắt, An chọn mở bài nhóm được liệt kê | E9.1 | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |


<!-- sc:branch SC-M14-004 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | An mở Group. | D-TIME45-G, R21 thuộc Private GK, 44 bài còn lại thuộc Public GJ, An là thành viên cả hai, thời điểm đăng R01>R02>…>R45. | E1.2 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14 |
| E1.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và nhóm người xem hiện tham gia, gồm Public/Private. Chỉ giữ bài thuộc nhóm hiện tham gia và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-TIME45-G, R21 thuộc Private GK, 44 bài còn lại thuộc Public GJ, An là thành viên cả hai, lần đầu 20 bài. Bài trả về=R01, R02, R03, R04, R05, R06, R07, R08, R09, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, số lượng=20, vị trí tải tiếp=R20. | E1.3 | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E1.3 | ACT-002 | An cuộn đọc tiếp sau R20. | D-TIME45-G, R21 thuộc Private GK, 44 bài còn lại thuộc Public GJ, An là thành viên cả hai, vị trí tải tiếp=R20. | E1.4 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E1.4 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và nhóm người xem hiện tham gia, gồm Public/Private. Chỉ giữ bài thuộc nhóm hiện tham gia và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-TIME45-G, R21 thuộc Private GK, 44 bài còn lại thuộc Public GJ, An là thành viên cả hai, lần hai 20 bài. Bài trả về=R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, số lượng=20, vị trí tải tiếp=R40. | E1.5 | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E1.5 | ACT-002 | An cuộn đọc phần còn lại sau R40. | D-TIME45-G, R21 thuộc Private GK, 44 bài còn lại thuộc Public GJ, An là thành viên cả hai, còn 5 bài. | E1.6 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E1.6 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và nhóm người xem hiện tham gia, gồm Public/Private. Chỉ giữ bài thuộc nhóm hiện tham gia và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-TIME45-G, R21 thuộc Private GK, 44 bài còn lại thuộc Public GJ, An là thành viên cả hai, đã hết 45 bài và dừng tải thêm. Bài trả về=R41, R42, R43, R44, R45, số lượng=5, vị trí tải tiếp=R45. | END:SUCCESS | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


<!-- sc:branch SC-M14-004 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | An cuộn tiếp tab Group sau R20 đã tải. | D-TIME45-G, R21 thuộc Private GK, 44 bài còn lại thuộc Public GJ, An là thành viên cả hai, R01 mới nhất đang hiện lúc 10:00. N01/N02/N03 mới hơn R01 và thuộc tab được đăng lúc 10:01:01–03. | E2.2 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E2.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và nhóm người xem hiện tham gia, gồm Public/Private. Chỉ giữ bài thuộc nhóm hiện tham gia và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-TIME45-G, R21 thuộc Private GK, 44 bài còn lại thuộc Public GJ, An là thành viên cả hai, tải sau R20. AUT002 có thể báo ba bài mới theo hạn 60 giây, danh sách được trả ở lượt cuộn này tiếp tục R21–R40. Bài trả về=R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, số lượng=20, vị trí tải tiếp=R40. | END:SUCCESS | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


<!-- sc:branch SC-M14-004 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-002 | An cuộn tiếp Group sau R20 đã tải. | D-TIME45-G, M11 đã xóa membership(GJ), membership(GK) còn. | E3.2 | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E3.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và nhóm người xem hiện tham gia, gồm Public/Private. Chỉ giữ bài thuộc nhóm hiện tham gia và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | Chỉ R21 thuộc GK còn hợp lệ trong phần chưa tải. R22–R45 thuộc Public GJ đã rời nên bị loại, phần chưa tải đã hết. Bài trả về=R21, số lượng=1, vị trí tải tiếp=R21. | END:SUCCESS | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


<!-- sc:branch SC-M14-004 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và nhóm người xem hiện tham gia, gồm Public/Private. Chỉ giữ bài thuộc nhóm hiện tham gia và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | Tab Group còn hiện, Q08/Q07/Q06/Q05 vẫn được liệt kê như lối vào, mở bài theo cổng M11. Group=Tắt. Bài trả về=Q08, Q07, Q06, Q05, số lượng=4, vị trí tải tiếp=Q05. | END:SUCCESS | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


<!-- sc:branch SC-M14-004 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống kiểm phiên/thành viên và bài, trả trạng thái rỗng của Group kèm nút Khám phá Group. | An chưa tham gia nhóm nào, Group=[]. | END:SUCCESS | FR-M14-05.06, BR-M14-21 |


<!-- sc:branch SC-M14-004 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống kiểm phiên/thành viên và bài, trả trạng thái rỗng của Group kèm nút Khám phá Group. | An chưa tham gia nhóm nào, Group=[]. | E6.2 | FR-M14-05.06, BR-M14-21 |
| E6.2 | ACT-002 | An bấm Khám phá Group. | Đích là trang danh sách nhóm M11. | E6.3 | FR-M14-05.06, BR-M14-21 |
| E6.3 | SYSTEM | Hệ thống mở danh sách nhóm M11 theo quyền hiện tại, trả các nhóm Public và Private mà An là thành viên, mỗi mục có tên/mô tả/chế độ, nhóm tạo sau trước. | D-DIRECTORY cho ngữ cảnh này gồm GO Public, GJ Public, theo thời điểm tạo GO mới hơn GJ. GK Private bị loại vì An ngoài nhóm. Cờ Group có thể Bật hoặc Tắt vì đây là lối vào tại FR-M11-17.07. | END:HANDED_OFF | FR-M14-05.06, BR-M14-21, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, FR-M11-03.11, FR-M11-03.16, FR-M11-03.17, FR-M11-17.07 |


<!-- sc:branch SC-M14-004 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống kiểm phiên/thành viên và bài, trả trạng thái rỗng của Group kèm nút Khám phá Group. | An đã tham gia GJ/GK nhưng snapshot này chưa có bài đủ điều kiện, Group=[]. | END:SUCCESS | FR-M14-05.07, BR-M14-21 |


<!-- sc:branch SC-M14-004 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống kiểm phiên/thành viên và bài, trả trạng thái rỗng của Group kèm nút Khám phá Group. | An đã tham gia GJ/GK nhưng snapshot này chưa có bài đủ điều kiện, Group=[]. | E8.2 | FR-M14-05.07, BR-M14-21 |
| E8.2 | ACT-002 | An bấm Khám phá Group. | Đích là trang danh sách nhóm M11. | E8.3 | FR-M14-05.07, BR-M14-21 |
| E8.3 | SYSTEM | Hệ thống mở danh sách nhóm M11 theo quyền hiện tại, trả các nhóm Public và Private mà An là thành viên, mỗi mục có tên/mô tả/chế độ, nhóm tạo sau trước. | D-DIRECTORY cho ngữ cảnh này gồm GK Private, GO Public, GJ Public, theo thời điểm tạo GK mới nhất rồi GO rồi GJ. Cờ Group có thể Bật hoặc Tắt vì đây là lối vào tại FR-M11-17.07. | END:HANDED_OFF | FR-M14-05.07, BR-M14-21, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, FR-M11-03.11, FR-M11-03.16, FR-M11-03.17, FR-M11-17.07 |


<!-- sc:branch SC-M14-004 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | ACT-002 | An mở Group để đọc danh sách. | Group=Tắt, dữ liệu chuẩn của SC, bài Q06 được phép liệt kê. | E9.2 | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10 |
| E9.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và nhóm người xem hiện tham gia, gồm Public/Private. Chỉ giữ bài thuộc nhóm hiện tham gia và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-SET, Q08/Q07 hiện Ẩn danh với An là Member thường, Q06 của Private GK được hiển thị, Q09 Public GO bị loại vì An ngoài nhóm. GH bị ẩn và bài đã gỡ khỏi GJ bị loại, đã hết 4 bài. Bài trả về=Q08, Q07, Q06, Q05, số lượng=4, vị trí tải tiếp=Q05. Cờ Group=Tắt trong snapshot này. | E9.3 | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10 |
| E9.3 | ACT-002 | An chọn mở bài nhóm Q06. | Group=Tắt, người thao tác khác ADMIN. | E9.4 | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.01, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |
| E9.4 | SYSTEM | Hệ thống chuyển yêu cầu mở tới cổng M11, từ chối và hiển thị “Hệ thống đang bận, vui lòng thử lại sau”. | Q06, yêu cầu mở bị từ chối do Group=Tắt. | END:REJECTED | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.01, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |


**V1 — thay toàn bộ M1 đến kết thúc.** Guest chọn Group. Actor khởi tạo ACT-001, kết thúc END:REJECTED.

<!-- sc:role-path SC-M14-004 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest chọn tab Group. | Tab vẫn hiện cho Guest. | V1.2 | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, BR-M14-01, BR-M14-02, BR-M14-03, BR-M14-22, BR-M10-19, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-07, BR-M14-09, BR-M14-21, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14 |
| V1.2 | SYSTEM | Hệ thống kiểm phiên và yêu cầu đăng nhập để xem Group. | Guest chưa nhận bài của Group. | END:REJECTED | FR-M14-05.05, BR-M14-02 |


**V2 — thay toàn bộ M1 đến kết thúc.** Minh xem Group theo các quan hệ của chính mình. Actor khởi tạo ACT-008, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-004 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-008 | Minh chọn Group. | D-STAFF, S02 đăng 09:02 > S01 09:01, tác giả ACTIVE, bài thường. S01 Public GJ, S02 Private GK, Minh là thành viên cả hai. | V2.2 | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14 |
| V2.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và nhóm người xem hiện tham gia, gồm Public/Private. Chỉ giữ bài thuộc nhóm hiện tham gia và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-STAFF, S01 Public GJ, S02 Private GK, Minh là thành viên cả hai, hai bài đủ điều kiện. Bài trả về=S02, S01, số lượng=2, vị trí tải tiếp=S01. | END:SUCCESS | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


**V3 — thay toàn bộ M1 đến kết thúc.** Hòa xem Group theo các quan hệ của chính mình. Actor khởi tạo ACT-007, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-004 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-007 | Hòa chọn Group. | D-STAFF, S02 đăng 09:02 > S01 09:01, tác giả ACTIVE, bài thường. S01 Public GJ, S02 Private GK, Hòa là thành viên cả hai. | V3.2 | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14 |
| V3.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Kiểm phiên và nhóm người xem hiện tham gia, gồm Public/Private. Chỉ giữ bài thuộc nhóm hiện tham gia và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-STAFF, S01 Public GJ, S02 Private GK, Hòa là thành viên cả hai, hai bài đủ điều kiện. Bài trả về=S02, S01, số lượng=2, vị trí tải tiếp=S01. | END:SUCCESS | FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


**V4 — thay toàn bộ M1 đến kết thúc.** Hòa ADMIN chọn mở bài nhóm khi Group Tắt. Actor khởi tạo ACT-007, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-004 V4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V4.1 | ACT-007 | Hòa mở Group. | D-ADMIN, S01 thuộc Public GJ, bài thường Đã đăng/Bình thường, Hòa là thành viên GJ và đang theo dõi Topic Toán, Group=Tắt. | V4.2 | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14 |
| V4.2 | SYSTEM | Hệ thống kiểm phạm vi/quyền của tab và liệt kê S01 như lối vào. Hòa có cùng quy tắc xếp danh sách feed. | S01, Group=Tắt, đủ điều kiện tab. Với Trending có kết quả đã tính cho S01. | V4.3 | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, BR-M14-02, BR-M14-07, BR-M14-09, BR-M14-21, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14 |
| V4.3 | ACT-007 | Hòa chọn mở bài nhóm S01. | Hòa ADMIN, vẫn có quyền nội dung nhóm. | V4.4 | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.01, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |
| V4.4 | SYSTEM | Hệ thống áp ngoại lệ ADMIN của M10/M11, kiểm quyền bài và trả bài S01 được phép mở. Hiển thị tiêu đề “Bài S01”, nội dung “Nội dung minh họa S01”, tác giả U, Lớp/Khối 11 và ngữ cảnh nhóm GJ, dữ liệu bài này có tập tệp/poll rỗng. | S01 Đã đăng/Bình thường, tác giả ACTIVE, Hòa nhận nội dung theo quyền hiện hành. | END:SUCCESS | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M03-07.01, FR-M03-07.04, FR-M11-03.04, FR-M11-03.05, FR-M11-03.06 |


<!-- sc:end SC-M14-004 -->

<a id="sc-m14-005"></a>

<!-- sc:scenario SC-M14-005 -->

### SC-M14-005

#### 1. Tên kịch bản chuẩn

Đọc dòng bài mới toàn site ngoài nhóm — BF-M14-005. Owner [UC-M14-023](../../us/US-M14.md#uc-m14-023).

#### 2. Actor thực hiện

ACT-001 khởi tạo đường chuẩn. Các đường V ghi actor khởi tạo khác theo cùng mục tiêu. Toàn iShare là SYSTEM, các quan hệ và dữ liệu owner được xử lý trong lượt SYSTEM.

#### 3. Tiền điều kiện

Guest chọn Newest trong feed, đường chuẩn D-SET có bài hiển thị ngoài nhóm và kết quả trả thành công. Tab này công khai. Dữ liệu hiển thị rỗng riêng Newest hoặc lỗi tải được giữ tại GAP001/005.

#### 4. Hậu điều kiện

<!-- sc:post SC-M14-005 -->

| result | condition |
|---|---|
| SUCCESS | Người xem nhận dòng bài ngoài nhóm theo thời điểm đăng, có thể tải tiếp sau vị trí đã có. Bài nhóm Public/Private nằm ngoài tập Newest. Bài mới được báo qua AUT002 và chèn khi actor chọn chức năng tại SC006. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M14-005 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-001 | Guest chọn tab Newest. | D-SET, người xem chưa đăng nhập. | M2 | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09 |
| M2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Cho Guest hoặc người đăng nhập xem. Chỉ giữ bài ngoài mọi nhóm và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-SET chỉ trả bài ngoài nhóm. Q11 có nhãn BANNED, Q12 được hiển thị bình thường. Mọi bài nhóm Public/Private đều bị loại, đã hết 6 bài. Bài trả về=Q12, Q11, Q04, Q03, Q02, Q01, số lượng=6, vị trí tải tiếp=Q01. | END:SUCCESS | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


#### 6. Các ngoại lệ

E thay bước ở cột at, guard xác định snapshot dữ liệu của đường đó từ đầu. V thay toàn bộ từ hành động đầu khi actor khởi tạo khác. Mỗi đường kết thúc theo hậu điều kiện cùng mã tại mục 4. Những tình huống còn thiếu hợp đồng được nêu riêng ở GAP.

<!-- sc:exceptions SC-M14-005 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Người xem đọc hết bộ 45 bài của Newest qua các lần cuộn | E1.1 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27 |
| E2 | system | M1 | Có ba bài mới được đăng sau trang đầu, actor tiếp tục đọc phần cũ | E2.1 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27 |
| E3 | system | M2 | Các cờ Group/Chat/Gamification đều Tắt | E3.1 | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


<!-- sc:branch SC-M14-005 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-001 | Guest mở Newest. | D-TIME45-N, 45 bài ngoài nhóm, thời điểm đăng R01>R02>…>R45. | E1.2 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19, FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09 |
| E1.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Cho Guest hoặc người đăng nhập xem. Chỉ giữ bài ngoài mọi nhóm và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-TIME45-N, 45 bài ngoài nhóm, lần đầu 20 bài. Bài trả về=R01, R02, R03, R04, R05, R06, R07, R08, R09, R10, R11, R12, R13, R14, R15, R16, R17, R18, R19, R20, số lượng=20, vị trí tải tiếp=R20. | E1.3 | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E1.3 | ACT-001 | Guest cuộn đọc tiếp sau R20. | D-TIME45-N, 45 bài ngoài nhóm, vị trí tải tiếp=R20. | E1.4 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E1.4 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Cho Guest hoặc người đăng nhập xem. Chỉ giữ bài ngoài mọi nhóm và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-TIME45-N, 45 bài ngoài nhóm, lần hai 20 bài. Bài trả về=R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, số lượng=20, vị trí tải tiếp=R40. | E1.5 | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E1.5 | ACT-001 | Guest cuộn đọc phần còn lại sau R40. | D-TIME45-N, 45 bài ngoài nhóm, còn 5 bài. | E1.6 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E1.6 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Cho Guest hoặc người đăng nhập xem. Chỉ giữ bài ngoài mọi nhóm và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-TIME45-N, 45 bài ngoài nhóm, đã hết 45 bài và dừng tải thêm. Bài trả về=R41, R42, R43, R44, R45, số lượng=5, vị trí tải tiếp=R45. | END:SUCCESS | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


<!-- sc:branch SC-M14-005 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-001 | Guest cuộn tiếp tab Newest sau R20 đã tải. | D-TIME45-N, 45 bài ngoài nhóm, R01 mới nhất đang hiện lúc 10:00. N01/N02/N03 mới hơn R01 và thuộc tab được đăng lúc 10:01:01–03. | E2.2 | FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |
| E2.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Cho Guest hoặc người đăng nhập xem. Chỉ giữ bài ngoài mọi nhóm và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-TIME45-N, 45 bài ngoài nhóm, tải sau R20. AUT002 có thể báo ba bài mới theo hạn 60 giây, danh sách được trả ở lượt cuộn này tiếp tục R21–R40. Bài trả về=R21, R22, R23, R24, R25, R26, R27, R28, R29, R30, R31, R32, R33, R34, R35, R36, R37, R38, R39, R40, số lượng=20, vị trí tải tiếp=R40. | END:SUCCESS | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


<!-- sc:branch SC-M14-005 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Cho Guest hoặc người đăng nhập xem. Chỉ giữ bài ngoài mọi nhóm và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | M14 vẫn công khai, danh sách Newest ngoài nhóm và nhãn/số upvote tiếp tục theo nguồn. Bài trả về=Q12, Q11, Q04, Q03, Q02, Q01, số lượng=6, vị trí tải tiếp=Q01. | END:SUCCESS | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


**V1 — thay toàn bộ M1 đến kết thúc.** An đã đăng nhập thực hiện chức năng, cùng quyền đọc feed. Actor khởi tạo ACT-002, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-005 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-002 | An chọn Newest. | D-STAFF gồm S02 đăng 09:02 và S01 đăng 09:01, đều ngoài nhóm, tác giả ACTIVE, đủ quyền. | V1.2 | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09 |
| V1.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Cho Guest hoặc người đăng nhập xem. Chỉ giữ bài ngoài mọi nhóm và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-STAFF cùng chính sách Newest, đã hết hai bài. Bài trả về=S02, S01, số lượng=2, vị trí tải tiếp=S01. | END:SUCCESS | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


**V2 — thay toàn bộ M1 đến kết thúc.** Minh đã đăng nhập thực hiện chức năng, cùng quyền đọc feed. Actor khởi tạo ACT-008, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-005 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-008 | Minh chọn Newest. | D-STAFF gồm S02 đăng 09:02 và S01 đăng 09:01, đều ngoài nhóm, tác giả ACTIVE, đủ quyền. | V2.2 | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09 |
| V2.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Cho Guest hoặc người đăng nhập xem. Chỉ giữ bài ngoài mọi nhóm và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-STAFF cùng chính sách Newest, đã hết hai bài. Bài trả về=S02, S01, số lượng=2, vị trí tải tiếp=S01. | END:SUCCESS | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


**V3 — thay toàn bộ M1 đến kết thúc.** Hòa đã đăng nhập thực hiện chức năng, cùng quyền đọc feed. Actor khởi tạo ACT-007, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-005 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-007 | Hòa chọn Newest. | D-STAFF gồm S02 đăng 09:02 và S01 đăng 09:01, đều ngoài nhóm, tác giả ACTIVE, đủ quyền. | V3.2 | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09 |
| V3.2 | SYSTEM | Hệ thống mở UC004 và chèn UC003. Cho Guest hoặc người đăng nhập xem. Chỉ giữ bài ngoài mọi nhóm và còn được hiển thị, xếp thời điểm đăng sau trước. Kiểm trạng thái hiện hành của bài/tác giả/nhóm theo nguồn. Trả danh sách và vị trí tải tiếp. Tại tên được phép hiện, BANNED có nhãn “Tài khoản đã bị khóa”, mức cảnh cáo được bảo vệ. | D-STAFF cùng chính sách Newest, đã hết hai bài. Bài trả về=S02, S01, số lượng=2, vị trí tải tiếp=S01. | END:SUCCESS | FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06, BR-M14-09, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, BR-M14-16, BR-M14-19 |


<!-- sc:end SC-M14-005 -->

<a id="sc-m14-006"></a>

<!-- sc:scenario SC-M14-006 -->

### SC-M14-006

#### 1. Tên kịch bản chuẩn

Nhận toàn bộ bài mới qua banner và tiếp tục tại chỗ đang đọc — BF-M14-006. Owner [UC-M14-005](../../us/US-M14.md#uc-m14-005).

#### 2. Actor thực hiện

ACT-002 khởi tạo đường chuẩn. Các đường V ghi actor khởi tạo khác theo cùng mục tiêu. Toàn iShare là SYSTEM, các quan hệ và dữ liệu owner được xử lý trong lượt SYSTEM.

#### 3. Tiền điều kiện

An đang đọc Newest, đã tải 45 bài O01–O45 và đang ở O35. O01 mới nhất lúc 11/11 10:00. AUT002 đã hiện banner tại 10:11:45 sau lần kiểm trước 10:10:45. D-NEW30 gồm N01–N30 đăng lần lượt 10:11:01–10:11:30, đều ngoài nhóm và đủ quyền. An bấm lúc 10:12. Nội dung/quyền/tập bài ổn định trong call của đường chuẩn. Trạng thái tập mới rỗng hoặc có bài đến trong call nằm tại GAP003/005.

#### 4. Hậu điều kiện

<!-- sc:post SC-M14-006 -->

| result | condition |
|---|---|
| SUCCESS | Tất cả bài mới hơn mốc trên màn hình và còn thuộc tab được thêm lên đầu theo thời điểm đăng, mỗi bài một lần. Bộ 30 bài thêm đủ 30, vị trí đọc O35 được giữ theo nguồn. Banner thuộc Newest/Following/Group, polling tiếp tục theo AUT002 khi còn ở tab được phép. |
| REJECTED | Guest yêu cầu banner của Following/Group được yêu cầu đăng nhập, yêu cầu hiện tại kết thúc với quyền xem tab riêng chưa đạt. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M14-006 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | An bấm banner có bài mới ở Newest. | D-NEW30, O01 là mốc mới nhất đang hiện, vị trí đọc=O35, click lúc 10:12. | M2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18 |
| M2 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài ngoài mọi nhóm. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | D-NEW30 tất cả 30 bài mới thuộc Newest, 45 bài cũ vẫn trong phần đã tải. Bài thêm=N30, N29, N28, N27, N26, N25, N24, N23, N22, N21, N20, N19, N18, N17, N16, N15, N14, N13, N12, N11, N10, N09, N08, N07, N06, N05, N04, N03, N02, N01, tổng thêm=30, số cũ=45. O35 ở vị trí danh sách 65 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=75. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06 |


#### 6. Các ngoại lệ

E thay bước ở cột at, guard xác định snapshot dữ liệu của đường đó từ đầu. V thay toàn bộ từ hành động đầu khi actor khởi tạo khác. Mỗi đường kết thúc theo hậu điều kiện cùng mã tại mục 4. Những tình huống còn thiếu hợp đồng được nêu riêng ở GAP.

<!-- sc:exceptions SC-M14-006 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | An nhận bài mới trong Following | E1.1 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27 |
| E2 | user-choice | M1 | An nhận bài mới trong Group | E2.1 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27 |
| E3 | system | M2 | N01 bị xóa mềm và N02 bị Mod ẩn trước lúc An bấm, 28 bài còn lại hợp lệ | E3.1 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06 |
| E4 | system | M1 | An bỏ theo dõi U trước click nhưng vẫn theo dõi Toán, 29 bài mới còn thỏa Topic | E4.1 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27 |
| E5 | system | M1 | An rời GJ trước click, còn là thành viên GK, 15 bài mới còn hợp lệ | E5.1 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27 |
| E6 | user-choice | M1 | Chỉ có ba bài mới hợp lệ, actor chọn nhận | E6.1 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06 |
| E7 | system | M1 | Cờ Group Tắt, An nhận bài mới tại Group theo quyền thành viên | E7.1 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27 |


<!-- sc:branch SC-M14-006 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | An bấm banner có bài mới trong Following. | D-NEW30-F, An theo dõi U và Toán, N01–N30 của U/Toán ngoài nhóm hoặc Public, cùng bài thỏa hai điều kiện chỉ tính một lần, O01=10:00, đang đọc O35. | E1.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15 |
| E1.2 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài ngoài nhóm/nhóm Public thỏa người hoặc Topic đang theo dõi, ẩn danh chỉ qua Topic, Private bị loại. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | D-NEW30-F, An theo dõi U và Toán, N01–N30 của U/Toán ngoài nhóm hoặc Public, cùng bài thỏa hai điều kiện chỉ tính một lần. Bài thêm=N30, N29, N28, N27, N26, N25, N24, N23, N22, N21, N20, N19, N18, N17, N16, N15, N14, N13, N12, N11, N10, N09, N08, N07, N06, N05, N04, N03, N02, N01, tổng thêm=30, số cũ=45. O35 ở vị trí danh sách 65 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=75. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15 |


<!-- sc:branch SC-M14-006 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | An bấm banner có bài mới trong Group. | D-NEW30-G, N01/N03/…/N29 ở Public GJ, N02/N04/…/N30 ở Private GK, An là thành viên cả hai, O01=10:00, đang đọc O35. | E2.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14 |
| E2.2 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài của nhóm Public/Private người xem hiện là thành viên. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | D-NEW30-G, N01/N03/…/N29 ở Public GJ, N02/N04/…/N30 ở Private GK, An là thành viên cả hai. Bài thêm=N30, N29, N28, N27, N26, N25, N24, N23, N22, N21, N20, N19, N18, N17, N16, N15, N14, N13, N12, N11, N10, N09, N08, N07, N06, N05, N04, N03, N02, N01, tổng thêm=30, số cũ=45. O35 ở vị trí danh sách 65 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=75. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14 |


<!-- sc:branch SC-M14-006 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài ngoài mọi nhóm. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | Thay đổi tại 10:11:50 trước click. UC003 loại N01/N02, thêm N30–N03 đúng 28 bài còn hợp lệ. Bài thêm=N30, N29, N28, N27, N26, N25, N24, N23, N22, N21, N20, N19, N18, N17, N16, N15, N14, N13, N12, N11, N10, N09, N08, N07, N06, N05, N04, N03, tổng thêm=28, số cũ=45. O35 ở vị trí danh sách 63 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=73. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06 |


<!-- sc:branch SC-M14-006 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-002 | An bấm banner có bài mới ở Following. | D-NEW30-F2, N01 Topic Văn, N02–N30 Topic Toán. Ban đầu theo dõi U/Toán, tại 10:11:50 M07 đã bỏ U, Toán còn. Tất cả ngoài nhóm/Public. | E4.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15 |
| E4.2 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài ngoài nhóm/nhóm Public thỏa người hoặc Topic đang theo dõi, ẩn danh chỉ qua Topic, Private bị loại. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | Quan hệ hiện tại giữ N02–N30 qua Toán, N01 chỉ nhờ U bị loại trước chèn. Bài thêm=N30, N29, N28, N27, N26, N25, N24, N23, N22, N21, N20, N19, N18, N17, N16, N15, N14, N13, N12, N11, N10, N09, N08, N07, N06, N05, N04, N03, N02, tổng thêm=29, số cũ=45. O35 ở vị trí danh sách 64 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=74. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15 |


<!-- sc:branch SC-M14-006 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-002 | An bấm banner có bài mới ở Group. | D-NEW30-G, M11 đã ghi An rời GJ tại 10:11:50, membership(GK) còn. N lẻ ở GJ Public, N chẵn ở GK Private. | E5.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14 |
| E5.2 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài của nhóm Public/Private người xem hiện là thành viên. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | Chỉ N chẵn thuộc GK còn được tải, N lẻ GJ đã rời bị loại dù Public. Bài thêm=N30, N28, N26, N24, N22, N20, N18, N16, N14, N12, N10, N08, N06, N04, N02, tổng thêm=15, số cũ=45. O35 ở vị trí danh sách 50 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=60. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14 |


<!-- sc:branch SC-M14-006 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-002 | An bấm banner có bài mới ở Newest. | Snapshot D-NEW3 gồm N01–N03, O01=10:00, đang đọc O35. | E6.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18 |
| E6.2 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài ngoài mọi nhóm. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | Ba bài mới được đăng 10:11:01–03, tất cả ngoài nhóm. Bài thêm=N03, N02, N01, tổng thêm=3, số cũ=45. O35 ở vị trí danh sách 38 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=48. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06 |


<!-- sc:branch SC-M14-006 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | ACT-002 | An bấm banner có bài mới trong tab Group. | D-NEW30-G, membership GJ/GK còn, Group=Tắt, O35 đang đọc. | E7.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14, FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10 |
| E7.2 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài của nhóm Public/Private người xem hiện là thành viên. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | Feed vẫn liệt kê bài nhóm làm lối vào khi Group Tắt, thao tác mở bài được M11 kiểm riêng. Bài thêm=N30, N29, N28, N27, N26, N25, N24, N23, N22, N21, N20, N19, N18, N17, N16, N15, N14, N13, N12, N11, N10, N09, N08, N07, N06, N05, N04, N03, N02, N01, tổng thêm=30, số cũ=45. O35 ở vị trí danh sách 65 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=75. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14 |


**V1 — thay toàn bộ M1 đến kết thúc.** Guest nhận banner Newest. Actor khởi tạo ACT-001, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-006 V1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V1.1 | ACT-001 | Guest bấm banner có bài mới ở Newest. | D-NEW30, O01=10:00, đang đọc O35. | V1.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18 |
| V1.2 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài ngoài mọi nhóm. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | Guest đủ quyền Newest, 30 bài ngoài nhóm. Bài thêm=N30, N29, N28, N27, N26, N25, N24, N23, N22, N21, N20, N19, N18, N17, N16, N15, N14, N13, N12, N11, N10, N09, N08, N07, N06, N05, N04, N03, N02, N01, tổng thêm=30, số cũ=45. O35 ở vị trí danh sách 65 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=75. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06 |


**V2 — thay toàn bộ M1 đến kết thúc.** Minh nhận banner Newest. Actor khởi tạo ACT-008, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-006 V2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V2.1 | ACT-008 | Minh bấm banner có bài mới ở Newest. | D-NEW30, tất cả ngoài nhóm, O01=10:00, đang đọc O35, bài mới là bài thường. | V2.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18 |
| V2.2 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài ngoài mọi nhóm. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | D-NEW30, tất cả ngoài nhóm. Bài thêm=N30, N29, N28, N27, N26, N25, N24, N23, N22, N21, N20, N19, N18, N17, N16, N15, N14, N13, N12, N11, N10, N09, N08, N07, N06, N05, N04, N03, N02, N01, tổng thêm=30, số cũ=45. O35 ở vị trí danh sách 65 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=75. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06 |


**V3 — thay toàn bộ M1 đến kết thúc.** Hòa nhận banner Newest. Actor khởi tạo ACT-007, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-006 V3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V3.1 | ACT-007 | Hòa bấm banner có bài mới ở Newest. | D-NEW30, tất cả ngoài nhóm, O01=10:00, đang đọc O35, bài mới là bài thường. | V3.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18 |
| V3.2 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài ngoài mọi nhóm. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | D-NEW30, tất cả ngoài nhóm. Bài thêm=N30, N29, N28, N27, N26, N25, N24, N23, N22, N21, N20, N19, N18, N17, N16, N15, N14, N13, N12, N11, N10, N09, N08, N07, N06, N05, N04, N03, N02, N01, tổng thêm=30, số cũ=45. O35 ở vị trí danh sách 65 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=75. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, FR-M14-06.04, BR-M14-02, BR-M14-06 |


**V4 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu banner cũ của Following. Actor khởi tạo ACT-001, kết thúc END:REJECTED.

<!-- sc:role-path SC-M14-006 V4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V4.1 | ACT-001 | Guest gửi yêu cầu nhận bài mới của Following. | Ngữ cảnh hiện tại là Guest, yêu cầu banner tab riêng. | V4.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-04.04 |
| V4.2 | SYSTEM | Hệ thống kiểm phiên và yêu cầu đăng nhập theo quyền của tab Following. | Lượt yêu cầu của Guest kết thúc trước cấp dữ liệu riêng. | END:REJECTED | FR-M14-04.04, BR-M14-02 |


**V5 — thay toàn bộ M1 đến kết thúc.** Minh nhận banner Following. Actor khởi tạo ACT-008, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-006 V5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V5.1 | ACT-008 | Minh bấm banner có bài mới ở Following. | D-NEW30-F, theo dõi U/Toán của chính người xem, O01=10:00, đang đọc O35, bài mới là bài thường. | V5.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18 |
| V5.2 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài ngoài nhóm/nhóm Public thỏa người hoặc Topic đang theo dõi, ẩn danh chỉ qua Topic, Private bị loại. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | D-NEW30-F, theo dõi U/Toán của chính người xem. Bài thêm=N30, N29, N28, N27, N26, N25, N24, N23, N22, N21, N20, N19, N18, N17, N16, N15, N14, N13, N12, N11, N10, N09, N08, N07, N06, N05, N04, N03, N02, N01, tổng thêm=30, số cũ=45. O35 ở vị trí danh sách 65 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=75. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15 |


**V6 — thay toàn bộ M1 đến kết thúc.** Hòa nhận banner Following. Actor khởi tạo ACT-007, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-006 V6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V6.1 | ACT-007 | Hòa bấm banner có bài mới ở Following. | D-NEW30-F, theo dõi U/Toán của chính người xem, O01=10:00, đang đọc O35, bài mới là bài thường. | V6.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18 |
| V6.2 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài ngoài nhóm/nhóm Public thỏa người hoặc Topic đang theo dõi, ẩn danh chỉ qua Topic, Private bị loại. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | D-NEW30-F, theo dõi U/Toán của chính người xem. Bài thêm=N30, N29, N28, N27, N26, N25, N24, N23, N22, N21, N20, N19, N18, N17, N16, N15, N14, N13, N12, N11, N10, N09, N08, N07, N06, N05, N04, N03, N02, N01, tổng thêm=30, số cũ=45. O35 ở vị trí danh sách 65 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=75. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.04, FR-M14-04.05, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.11, FR-M14-04.12, FR-M14-04.13, BR-M14-02, BR-M14-08, BR-M14-20, BR-M14-22, FR-M07-01.01, BR-M07-15 |


**V7 — thay toàn bộ M1 đến kết thúc.** Guest yêu cầu banner cũ của Group. Actor khởi tạo ACT-001, kết thúc END:REJECTED.

<!-- sc:role-path SC-M14-006 V7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V7.1 | ACT-001 | Guest gửi yêu cầu nhận bài mới của Group. | Ngữ cảnh hiện tại là Guest, yêu cầu banner tab riêng. | V7.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-05.05 |
| V7.2 | SYSTEM | Hệ thống kiểm phiên và yêu cầu đăng nhập theo quyền của tab Group. | Lượt yêu cầu của Guest kết thúc trước cấp dữ liệu riêng. | END:REJECTED | FR-M14-05.05, BR-M14-02 |


**V8 — thay toàn bộ M1 đến kết thúc.** Minh nhận banner Group. Actor khởi tạo ACT-008, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-006 V8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V8.1 | ACT-008 | Minh bấm banner có bài mới ở Group. | D-NEW30-G, người xem là thành viên GJ/GK, O01=10:00, đang đọc O35, bài mới là bài thường. | V8.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18 |
| V8.2 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài của nhóm Public/Private người xem hiện là thành viên. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | D-NEW30-G, người xem là thành viên GJ/GK. Bài thêm=N30, N29, N28, N27, N26, N25, N24, N23, N22, N21, N20, N19, N18, N17, N16, N15, N14, N13, N12, N11, N10, N09, N08, N07, N06, N05, N04, N03, N02, N01, tổng thêm=30, số cũ=45. O35 ở vị trí danh sách 65 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=75. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14 |


**V9 — thay toàn bộ M1 đến kết thúc.** Hòa nhận banner Group. Actor khởi tạo ACT-007, kết thúc END:SUCCESS.

<!-- sc:role-path SC-M14-006 V9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| V9.1 | ACT-007 | Hòa bấm banner có bài mới ở Group. | D-NEW30-G, người xem là thành viên GJ/GK, O01=10:00, đang đọc O35, bài mới là bài thường. | V9.2 | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18 |
| V9.2 | SYSTEM | Hệ thống kiểm quyền tab và chèn UC003 để kiểm bài/nhóm/tác giả hiện tại. Chỉ lấy bài mới hơn O01 lúc 10:00 và thuộc phạm vi bài của nhóm Public/Private người xem hiện là thành viên. Chèn toàn bộ tập hợp lệ theo thời điểm đăng sau trước lên đầu, mỗi bài một lần. Giữ chỗ đọc tại O35 và phần bài cũ đã tải, hoàn tất lượt nhận bài mới. | D-NEW30-G, người xem là thành viên GJ/GK. Bài thêm=N30, N29, N28, N27, N26, N25, N24, N23, N22, N21, N20, N19, N18, N17, N16, N15, N14, N13, N12, N11, N10, N09, N08, N07, N06, N05, N04, N03, N02, N01, tổng thêm=30, số cũ=45. O35 ở vị trí danh sách 65 nhưng chỗ đọc trên màn hình vẫn tại O35. Tổng bài đã tải=75. | END:SUCCESS | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-09, BR-M14-17, BR-M14-18, FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, BR-M14-04, BR-M14-15, FR-M01-13.01, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M12-27, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-05.05, FR-M14-05.06, FR-M14-05.07, FR-M14-05.08, BR-M14-02, BR-M14-07, BR-M14-21, BR-M14-22, FR-M11-03.01, FR-M11-03.02, FR-M11-03.03, BR-M11-14 |


<!-- sc:end SC-M14-006 -->

## 5. Hành vi nền và dữ liệu đối soát

| ID | Trigger/điều kiện | Xử lý, kết quả và liên hệ SC | sources |
|---|---|---|---|
| AUT-M14-001 | Đến lần tính Trending Post, khoảng giữa hai lần 15–30 phút | SYSTEM lấy bài feed chính đủ điều kiện ở thời điểm tính, gồm ngoài nhóm/Public, tuổi liên tục t≤28 ngày. Lấy U upvote bài hiệu lực, C bình luận gốc và trả lời đang hiển thị bình thường, B bookmark đang có. Tính S=0,5^(t/7)×(1+2U+C+B), xếp điểm giảm dần, hòa điểm thì bài đăng sau trước. Mỗi tương tác tham gia kết quả mới nhất chậm nhất 30 phút. Kết quả hiện hành phục vụ lượt xem mới, lượt đã mở dùng kết quả của mình theo BR-M14-19 và kiểm quyền lúc tải. Cờ Gamification Tắt vẫn tính U đang có. D45/K0/K1 và D-SCORE triển khai dữ liệu trước/sau. | FR-M14-03.01, FR-M14-03.02, FR-M14-03.03, FR-M14-03.04, FR-M14-03.05, FR-M14-03.06, FR-M14-03.07, FR-M14-03.08, FR-M14-03.09, FR-M14-03.10, FR-M14-03.11, FR-M14-03.12, FR-M14-03.13, FR-M14-03.14, FR-M14-03.15, BR-M14-04, BR-M14-05, BR-M14-10, BR-M14-11, BR-M14-12, BR-M14-13, BR-M14-14, BR-M14-15, BR-M14-19, BR-M14-22, BR-M04-18, FR-M02-07.06, FR-M01-12.09 |
| AUT-M14-002 | Người xem đang ở Newest/Following/Group được phép xem | SYSTEM kiểm tra định kỳ cách nhau tối đa 60 giây, so với bài mới nhất đang hiện. Chỉ tính bài thuộc tab và mới hơn theo thời điểm đăng, hiện banner có bài mới chậm nhất 60 giây từ lúc bài được đăng. Danh sách được chèn sau thao tác actor bấm theo SC006. Polling tiếp tục khi còn ở tab được phép. Các lượt Trending dùng hợp đồng giữ kết quả riêng. D-POLL đối soát thời điểm, phạm vi và bài trên màn hình trước/sau. | FR-M14-08.01, FR-M14-08.02, FR-M14-08.05, FR-M14-08.06, FR-M14-02.07, BR-M14-17, BR-M14-18, BR-M14-19 |
| RULE-M14-001 | Mở trang chủ và chọn tab | Trang chủ có đúng bốn tab Trending/Following/Group/Newest, Trending có ba mục Post/Topic/Tag. Mọi actor mở trang chủ đều vào Trending Post. Guest thấy bốn tab và được đọc Trending/Newest, Following/Group yêu cầu đăng nhập. User/Mod/Admin dùng quan hệ theo dõi và thành viên của chính mình. Cổng tài khoản M01 quyết định người được vào hệ thống, tài khoản BANNED được M01 đưa tới màn hình bị khóa. Phạm vi M14 chỉ có bốn tab theo nguồn và kết quả chung hoặc các quan hệ người xem đã chọn. | FR-M14-01.01, FR-M14-01.02, FR-M14-01.03, FR-M14-01.04, FR-M14-01.05, FR-M14-01.06, FR-M14-01.07, FR-M14-01.08, FR-M14-01.09, FR-M14-02.01, FR-M14-02.02, FR-M14-04.04, FR-M14-05.05, FR-M14-06.04, BR-M14-01, BR-M14-02, BR-M14-03, BR-M01-18 |
| RULE-M14-002 | Mỗi lần cấp dữ liệu bài trong tab | Trending Post dùng feed chính ngoài nhóm/Public trong kết quả đã tính. Following dùng OR người/Topic theo dõi, loại Private dù người xem là thành viên, ẩn danh chỉ qua Topic và mỗi bài một lần. Group dùng nhóm hiện tham gia gồm Public/Private, loại nhóm đã rời hoặc chưa tham gia. Newest chỉ ngoài mọi nhóm. Ba tab thời gian dùng thời điểm đăng sau trước. D-SET và D-TIME45 kiểm phạm vi, OR, ẩn danh và cập nhật quan hệ ở lần tải sau. M07 cung cấp quan hệ người/Topic, M11 cung cấp thành viên. | FR-M14-02.04, FR-M14-02.09, FR-M14-04.01, FR-M14-04.02, FR-M14-04.03, FR-M14-04.06, FR-M14-04.07, FR-M14-04.09, FR-M14-04.10, FR-M14-04.13, FR-M14-05.01, FR-M14-05.02, FR-M14-05.03, FR-M14-05.04, FR-M14-06.01, FR-M14-06.02, FR-M14-06.03, BR-M14-05, BR-M14-06, BR-M14-07, BR-M14-08, BR-M14-09, BR-M14-23, FR-M07-01.01, BR-M07-15, BR-M11-14 |
| RULE-M14-003 | Dữ liệu điểm và danh sách thịnh hành | Tuổi Post=(lúc tính−lúc chuyển Đã đăng)/24 giờ, giữ phần lẻ. Đúng 28 ngày còn hợp lệ, >28 loại ở lần tính. Mọi bài trong phạm vi có mặt kể cả U=C=B=0. Tín hiệu chỉ gồm U/C/B đang có theo owner, C tính cả reply bình thường. Lượt xem thuộc tập tín hiệu ngoài công thức S. BANNED/HEAVY dùng cùng công thức. Topic/Tag do M05 cung cấp, dùng cửa sổ tương tác 7 ngày và thứ tự điểm, số bài mới, tên A–Z. M14 nhận mọi mục điểm dương, Tag còn hoạt động, tối đa 20 mục/lần. D-SCORE/D-CURRENT/D-TIE đối soát đầu vào và thứ tự. | FR-M14-03.01, FR-M14-03.02, FR-M14-03.03, FR-M14-03.04, FR-M14-03.05, FR-M14-03.06, FR-M14-03.07, FR-M14-03.08, FR-M14-03.09, FR-M14-03.10, FR-M14-03.11, FR-M14-03.12, FR-M14-03.13, FR-M14-03.14, FR-M14-03.15, FR-M14-02.06, FR-M14-02.10, BR-M14-10, BR-M14-11, BR-M14-12, BR-M14-13, BR-M14-14, BR-M14-15, BR-M14-24, BR-M04-18, BR-M05-26, BR-M05-29, BR-M05-30, BR-M05-31 |
| RULE-M14-004 | Lượt xem, tải tiếp và banner | UC004 dùng vị trí bài/mục cuối đã tải để cấp tối đa 20 phần tử tiếp theo, giữ ngữ cảnh tab/mục. Một lượt Trending kéo dài tới rời tab hoặc reload, dùng cùng kết quả và kiểm điều kiện hiện tại khi tải. Mở lại/reload nhận kết quả gần nhất, chuyển mục con trong cùng lượt giữ kết quả Post. Bài mới ở tab thời gian được báo theo AUT002, chỉ thêm khi bấm banner. UC005 thêm tất cả bài mới hợp lệ hơn mốc, giữ chỗ đọc. D45 minh họa 20+20+5, D-NEW30 thêm 30 và giữ O35. Nguồn yêu cầu bảo toàn danh sách và chỗ đọc, các chi tiết đồng thời/khóa phụ nằm tại GAP002/003/005. | FR-M14-02.07, FR-M14-02.10, FR-M14-02.11, FR-M14-02.12, FR-M14-07.01, FR-M14-07.02, FR-M14-07.03, FR-M14-07.04, FR-M14-07.05, FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-16, BR-M14-17, BR-M14-18, BR-M14-19, BR-M14-24 |
| RULE-M14-005 | Cờ tính năng và lối vào owner | M14 là trang chủ luôn có lối truy cập. Group Tắt vẫn liệt kê bài Public ở Trending/Following, bài theo thành viên ở Group và danh sách nhóm của M11. Người khác ADMIN chọn mở nhóm/bài nhóm/tương tác được M11 trả đúng thông báo bận. ADMIN được dùng M11 như cờ Bật nhưng vẫn chịu quyền Private/nội dung. Gamification Tắt vẫn hiển thị số upvote và nhãn BANNED, Trending Post dùng số U hiện có. Quyền upvote/rút tại M12 tuân theo cổng M12 và ngoại lệ ADMIN. Các thao tác bookmark/bình luận/theo dõi/báo cáo/thành viên/đánh giá tiếp tục theo hợp đồng owner, các lựa chọn mở bài trong SC đi đến kết quả được cấp hoặc từ chối. | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10, FR-M10-12.01, FR-M10-12.06, FR-M11-17.01, FR-M11-17.02, FR-M12-08.01, FR-M12-08.08 |
| RULE-M14-006 | Điều kiện bài, trạng thái tác giả và ẩn danh | Mỗi lần cấp bài dùng Đã đăng/Bình thường, còn hiển thị theo M03/M01/M11. Nhóm bị ẩn, bài bị gỡ/xóa/ẩn, tác giả DEACTIVATED/DELETED bị loại khỏi tập feed thông thường. Mức khóa chỉ giới hạn tương tác theo owner. Tác giả BANNED/HEAVY vẫn có bài và điểm như thường, nhãn ban đặt tại tên được phép hiện, mức cảnh cáo được bảo vệ. Member thường thấy Ẩn danh theo dữ liệu M14. Public→Private giữ quyền đọc phần đã hiện sẵn của người ngoài nhóm theo M11, các lần tải sau chỉ nhận bài đúng phạm vi hiện tại, mở lại bằng link dùng thông báo nguồn. Phạm vi staff và nhãn ban/ẩn danh giao nhau nằm tại GAP004. | FR-M14-01.05, FR-M14-01.06, FR-M14-02.05, FR-M14-02.09, FR-M14-04.09, FR-M14-04.10, FR-M14-04.13, BR-M14-04, BR-M14-05, BR-M14-08, BR-M14-15, BR-M14-23, FR-M01-13.01, FR-M01-13.05, BR-M01-41, FR-M03-07.01, FR-M03-15.02, BR-M08-32, BR-M11-15, BR-M11-17, BR-M12-27 |


| Bộ dữ liệu | Trước hoặc sự kiện | Sau và kết quả | sources |
|---|---|---|---|
| D-CURRENT | Bài age=1 ngày, U hiệu lực 3 trong 5 lượt gồm 2 đã rút. C gồm 6 nút A–F theo ví dụ M04. B=2 đang có, 1 bookmark đã bỏ | Số bình luận bằng 4 gồm B,C,D,F vì A là dấu xóa và E bị ẩn, trong đó B/C là 2 reply bình thường. Đầu vào công thức U=3,C=4,B=2, S=0,5^(1/7)×13≈11,774408. Lượt xem 1.000 thuộc dữ liệu ngoài công thức. | FR-M14-03.02, FR-M14-03.07, FR-M14-03.10, FR-M14-03.12, FR-M14-03.13, BR-M14-10, BR-M04-18 |
| D-AGE | Bài đăng 14/10/2026 10:00, tính 11/11 10:00 và lần kế 10:20 | Tại 10:00 t=28 ngày, bài đủ điều kiện còn trong lần tính. Tại 10:20 t>28 nên AUT001 loại khỏi kết quả mới dù nhiều tương tác. Cách phục vụ bài vượt tuổi trong lượt cũ tiếp tục ở GAP006. | FR-M14-03.01, FR-M14-03.05, FR-M14-03.12, BR-M14-11, BR-M14-19 |
| D-BATCH | K0=10:00, tương tác mới trên P21 tại 10:15 tăng U từ 25 lên 42, K1=10:20 | AUT001 dùng U42 tại K1, các bài khác cập nhật tuổi thêm 20 phút. Chu kỳ 20 phút nằm trong 15–30, tương tác được tính sau 5 phút. P21 từ vị trí 21 lên 5 ở K1. Guest đã mở K0 lúc 10:10 tải tiếp theo K0 tại 10:22, mở lại 10:25 mới dùng K1. | FR-M14-03.02, FR-M14-03.03, FR-M14-03.04, FR-M14-03.10, FR-M14-03.15, FR-M14-02.11, FR-M14-02.12, FR-M14-07.05, BR-M14-14, BR-M14-19 |
| D-POLL | Lần kiểm 10:10:45, N01–N30 đăng 10:11:01–10:11:30, lần kiểm tiếp 10:11:45 | Khoảng kiểm 60 giây. N01 chờ 44 giây, N30 chờ 15 giây, banner hiện trong 60 giây từ mỗi bài được đăng. Trước bấm lúc 10:12, phần O01–O45 và chỗ đọc O35 là ngữ cảnh đang xem. SC006 thêm 30 bài khi bấm và giữ chỗ đọc. | FR-M14-08.01, FR-M14-08.02, FR-M14-08.03, FR-M14-08.04, FR-M14-08.05, FR-M14-08.06, FR-M14-08.07, BR-M14-17, BR-M14-18 |
| D-POLL-SCOPE | Bài X mới hơn mốc nhưng X thuộc Private còn người xem ở Following/Newest, hoặc X ngoài nhóm trong tab Group | X nằm ngoài phạm vi tab tương ứng nên AUT002 loại khỏi tập phát hiện bài mới của tab ấy. Tập không có bài hợp lệ mới thì chưa có cơ sở hiện banner khẳng định có bài mới. Trạng thái tab ban đầu rỗng cần GAP003. | FR-M14-08.01, FR-M14-08.02, FR-M14-08.05, BR-M14-05, BR-M14-06, BR-M14-07, BR-M14-08, BR-M14-17 |
| D-SCORE-STATUS | Hai bài có cùng đầu vào tương tác/tuổi, một tác giả BANNED hoặc HEAVY | AUT001 dùng cùng S cho cả hai, feed giữ quyền hiển thị và thứ tự do dữ liệu nguồn. Tên BANNED có nhãn công khai, mức cảnh cáo được bảo vệ. Người bị ban truy cập hệ thống theo cổng riêng M01. | FR-M14-01.06, FR-M14-03.08, BR-M14-15, BR-M01-18, BR-M08-32, BR-M12-27 |
| D-FLAGS | Group/Gamification/Chat Tắt, các dữ liệu bài và quan hệ còn hiệu lực | Feed vẫn mở Trending Post mặc định. Bài Public và lối vào Group/Following tiếp tục theo phạm vi, U hiện có vẫn được tính và hiển thị. Người khác ADMIN mở bài nhóm được M11 báo bận, ADMIN đủ quyền có thể mở. Các tác vụ AUT duy trì ràng buộc nguồn. | FR-M14-01.07, FR-M14-02.08, FR-M14-03.11, FR-M14-04.12, FR-M14-05.08, BR-M14-22, FR-M10-12.03, FR-M10-12.04, FR-M10-12.05, FR-M10-12.08, FR-M11-17.03, FR-M11-17.07, FR-M11-17.08, FR-M12-08.06, FR-M12-08.10 |
| D-PRIVACY | GJ Public chuyển Private lúc 10:21, Guest đã tải P02, P21 chưa tải | P02 trên màn hình đã tải còn được đọc theo BR-M11-15. Tải tiếp lúc 10:22 loại P21. Mở lại P02 bằng link báo Nội dung không tồn tại. Following loại mọi Private kể cả thành viên, Group vẫn cấp cho thành viên theo nguồn. | FR-M14-02.09, FR-M14-04.13, FR-M14-05.01, BR-M14-23, BR-M11-14, BR-M11-15 |
| D-FOLLOW-EMPTY | Không có quan hệ theo dõi, hoặc có quan hệ nhưng tập bài rỗng | Following trả trạng thái rỗng và nút sang tìm kiếm M06. Actor chọn nút thì M06 nhận hành trình tìm kiếm tiếp theo, dữ liệu ví dụ chưa có truy vấn gửi. Group dùng nút Khám phá Group và danh sách M11 riêng. | FR-M14-04.05, FR-M14-04.11, FR-M14-05.06, FR-M14-05.07, BR-M14-20, BR-M14-21, FR-M06-02.31 |


| Bộ điểm | t ngày | U | C | B | S | Điều kiện |
|---|---|---|---|---|---|---|
| S0 | 0 | 0 | 0 | 0 | 1 | Bài mới chưa tương tác vẫn trong phạm vi |
| S7 | 7 | 3 | 2 | 0 | 4,5 | Sau 7 ngày trọng số 0,5 |
| S14 | 14 | 10 | 4 | 2 | 6,75 | Sau 14 ngày trọng số 0,25 |
| S28 | 28 | 20 | 0 | 0 | 2,5625 | Đúng 28 ngày vẫn có, trọng số 0,0625 |
| SF | 3.5 | 2 | 1 | 3 | ≈6,363961 | Tuổi 3,5 ngày, giữ phần lẻ |
| TIE-A | 7 | 1 | 0 | 0 | 1,5 | Bài này mới hơn TIE-B nên đứng trước |
| TIE-B | 14 | 2 | 1 | 0 | 1,5 | Đồng điểm với TIE-A |


Các bộ điểm và sự kiện là dữ liệu đối soát AUT/RULE. Nguồn quy định actor yêu cầu đọc hoặc bấm banner, SYSTEM tính/phát hiện theo trigger đã có. Các phép tính và deadline được kiểm riêng trong QA. [FR-M14](../../fr/FR-M14.md)

## 6. Truy vết và ma trận nhánh

| FR/BR hiệu lực | SC/bước/E/V hoặc AUT/RULE/dữ liệu | Kết quả |
|---|---|---|
| FR-M14-01 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-003/V1.1, SC-M14-004/V1.1, RULE-M14-001, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.2, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.2, SC-M14-003/M2, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-003/V4.2, SC-M14-004/M2, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-004/V4.2, SC-M14-005/M2, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, SC-M14-006/M2, SC-M14-006/E1.2, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.2, SC-M14-006/E5.2, SC-M14-006/E6.2, SC-M14-006/E7.2, SC-M14-006/V1.2, SC-M14-006/V2.2, SC-M14-006/V3.2, SC-M14-006/V5.2, SC-M14-006/V6.2, SC-M14-006/V8.2, SC-M14-006/V9.2, RULE-M14-006, D-SCORE-STATUS, SC-M14-001/E11.3, SC-M14-001/E11.4, SC-M14-001/V4.1, SC-M14-001/V4.3, SC-M14-001/V4.4, SC-M14-003/E9.1, SC-M14-003/E9.3, SC-M14-003/E9.4, SC-M14-003/V4.1, SC-M14-003/V4.3, SC-M14-003/V4.4, SC-M14-004/E9.1, SC-M14-004/E9.3, SC-M14-004/E9.4, SC-M14-004/V4.1, SC-M14-004/V4.3, SC-M14-004/V4.4, SC-M14-006/E7.1, RULE-M14-005, D-FLAGS | Có vị trí đối soát phần có hợp đồng |
| FR-M14-02 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E3.1, SC-M14-001/E3.2, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-002/M1, SC-M14-002/M2, SC-M14-002/M3, SC-M14-002/M4, SC-M14-002/E1.1, SC-M14-002/E1.2, SC-M14-002/E1.3, SC-M14-002/E1.4, SC-M14-002/E2.1, SC-M14-002/E2.2, SC-M14-002/E2.3, SC-M14-002/E3.1, SC-M14-002/E4.1, SC-M14-002/E4.2, SC-M14-002/E4.3, SC-M14-002/E4.4, SC-M14-002/V1.1, SC-M14-002/V1.2, SC-M14-002/V1.3, SC-M14-002/V1.4, SC-M14-002/V2.1, SC-M14-002/V2.2, SC-M14-002/V2.3, SC-M14-002/V2.4, SC-M14-002/V3.1, SC-M14-002/V3.2, SC-M14-002/V3.3, SC-M14-002/V3.4, SC-M14-003/V1.1, SC-M14-004/V1.1, RULE-M14-001, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2, RULE-M14-002, SC-M14-003/M2, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-003/V4.2, SC-M14-004/M2, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-004/V4.2, SC-M14-005/M2, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, SC-M14-006/M2, SC-M14-006/E1.2, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.2, SC-M14-006/E5.2, SC-M14-006/E6.2, SC-M14-006/E7.2, SC-M14-006/V1.2, SC-M14-006/V2.2, SC-M14-006/V3.2, SC-M14-006/V5.2, SC-M14-006/V6.2, SC-M14-006/V8.2, SC-M14-006/V9.2, RULE-M14-006, AUT-M14-002, RULE-M14-004, SC-M14-001/E11.3, SC-M14-001/E11.4, SC-M14-001/V4.3, SC-M14-001/V4.4, SC-M14-003/E9.1, SC-M14-003/E9.3, SC-M14-003/E9.4, SC-M14-003/V4.1, SC-M14-003/V4.3, SC-M14-003/V4.4, SC-M14-004/E9.1, SC-M14-004/E9.3, SC-M14-004/E9.4, SC-M14-004/V4.1, SC-M14-004/V4.3, SC-M14-004/V4.4, SC-M14-006/E7.1, RULE-M14-005, D-FLAGS, D-PRIVACY, D-BATCH, RULE-M14-003 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-03 | SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/E11.3, SC-M14-001/E11.4, SC-M14-001/V4.1, SC-M14-001/V4.2, SC-M14-001/V4.3, SC-M14-001/V4.4, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/E9.3, SC-M14-003/E9.4, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-003/V4.3, SC-M14-003/V4.4, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/E9.3, SC-M14-004/E9.4, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-004/V4.3, SC-M14-004/V4.4, SC-M14-006/E7.1, AUT-M14-001, RULE-M14-003, RULE-M14-005, D-FLAGS, D-AGE, D-CURRENT, D-BATCH, D-SCORE-STATUS | Có vị trí đối soát phần có hợp đồng |
| FR-M14-04 | SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/E11.3, SC-M14-001/E11.4, SC-M14-001/V4.1, SC-M14-001/V4.2, SC-M14-001/V4.3, SC-M14-001/V4.4, SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/E9.3, SC-M14-003/E9.4, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-003/V4.3, SC-M14-003/V4.4, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/E9.3, SC-M14-004/E9.4, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-004/V4.3, SC-M14-004/V4.4, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E7.1, SC-M14-006/V5.2, SC-M14-006/V6.2, RULE-M14-005, D-FLAGS, RULE-M14-002, SC-M14-003/V1.2, SC-M14-006/V4.1, SC-M14-006/V4.2, RULE-M14-001, SC-M14-003/E5.1, SC-M14-003/E6.1, SC-M14-003/E6.2, SC-M14-003/E6.3, D-FOLLOW-EMPTY, RULE-M14-006, SC-M14-003/E7.1, SC-M14-003/E8.1, SC-M14-003/E8.2, SC-M14-003/E8.3, D-PRIVACY | Có vị trí đối soát phần có hợp đồng |
| FR-M14-05 | SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/E11.3, SC-M14-001/E11.4, SC-M14-001/V4.1, SC-M14-001/V4.2, SC-M14-001/V4.3, SC-M14-001/V4.4, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/E9.3, SC-M14-003/E9.4, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-003/V4.3, SC-M14-003/V4.4, SC-M14-004/M1, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/E9.3, SC-M14-004/E9.4, SC-M14-004/V1.1, SC-M14-004/V2.1, SC-M14-004/V2.2, SC-M14-004/V3.1, SC-M14-004/V3.2, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-004/V4.3, SC-M14-004/V4.4, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V8.2, SC-M14-006/V9.2, RULE-M14-005, D-FLAGS, RULE-M14-002, D-PRIVACY, SC-M14-004/V1.2, SC-M14-006/V7.1, SC-M14-006/V7.2, RULE-M14-001, SC-M14-004/E5.1, SC-M14-004/E6.1, SC-M14-004/E6.2, SC-M14-004/E6.3, D-FOLLOW-EMPTY, SC-M14-004/E7.1, SC-M14-004/E8.1, SC-M14-004/E8.2, SC-M14-004/E8.3 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-06 | SC-M14-005/M1, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.1, SC-M14-005/V1.2, SC-M14-005/V2.1, SC-M14-005/V2.2, SC-M14-005/V3.1, SC-M14-005/V3.2, SC-M14-006/M2, SC-M14-006/E3.1, SC-M14-006/E6.2, SC-M14-006/V1.2, SC-M14-006/V2.2, SC-M14-006/V3.2, RULE-M14-002, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-07 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M5, SC-M14-001/M6, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.2, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.2, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.2, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.2, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.2, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.5, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.5, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.5, SC-M14-001/V3.6, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.3, SC-M14-003/E1.4, SC-M14-003/E1.5, SC-M14-003/E1.6, SC-M14-003/E2.1, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.3, SC-M14-004/E1.4, SC-M14-004/E1.5, SC-M14-004/E1.6, SC-M14-004/E2.1, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.3, SC-M14-005/E1.4, SC-M14-005/E1.5, SC-M14-005/E1.6, SC-M14-005/E2.1, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, RULE-M14-004, D-BATCH | Có vị trí đối soát phần có hợp đồng |
| FR-M14-08 | SC-M14-006/M1, SC-M14-006/M2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E6.1, SC-M14-006/E6.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V1.1, SC-M14-006/V1.2, SC-M14-006/V2.1, SC-M14-006/V2.2, SC-M14-006/V3.1, SC-M14-006/V3.2, SC-M14-006/V4.1, SC-M14-006/V5.1, SC-M14-006/V5.2, SC-M14-006/V6.1, SC-M14-006/V6.2, SC-M14-006/V7.1, SC-M14-006/V8.1, SC-M14-006/V8.2, SC-M14-006/V9.1, SC-M14-006/V9.2, AUT-M14-002, RULE-M14-004, D-POLL, D-POLL-SCOPE | Có vị trí đối soát phần có hợp đồng |
| FR-M14-01.01 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-003/V1.1, SC-M14-004/V1.1, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-01.02 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-003/V1.1, SC-M14-004/V1.1, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-01.03 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-003/V1.1, SC-M14-004/V1.1, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-01.04 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-003/V1.1, SC-M14-004/V1.1, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-01.05 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.2, SC-M14-003/M2, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-003/V4.2, SC-M14-004/M2, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V1.1, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-004/V4.2, SC-M14-005/M2, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, SC-M14-006/M2, SC-M14-006/E1.2, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.2, SC-M14-006/E5.2, SC-M14-006/E6.2, SC-M14-006/E7.2, SC-M14-006/V1.2, SC-M14-006/V2.2, SC-M14-006/V3.2, SC-M14-006/V5.2, SC-M14-006/V6.2, SC-M14-006/V8.2, SC-M14-006/V9.2, RULE-M14-001, RULE-M14-006 | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-004 |
| FR-M14-01.06 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.2, SC-M14-003/M2, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-003/V4.2, SC-M14-004/M2, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V1.1, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-004/V4.2, SC-M14-005/M2, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, SC-M14-006/M2, SC-M14-006/E1.2, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.2, SC-M14-006/E5.2, SC-M14-006/E6.2, SC-M14-006/E7.2, SC-M14-006/V1.2, SC-M14-006/V2.2, SC-M14-006/V3.2, SC-M14-006/V5.2, SC-M14-006/V6.2, SC-M14-006/V8.2, SC-M14-006/V9.2, RULE-M14-001, RULE-M14-006, D-SCORE-STATUS | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-004 |
| FR-M14-01.07 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/E11.3, SC-M14-001/E11.4, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-001/V4.1, SC-M14-001/V4.2, SC-M14-001/V4.3, SC-M14-001/V4.4, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/E9.3, SC-M14-003/E9.4, SC-M14-003/V1.1, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-003/V4.3, SC-M14-003/V4.4, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/E9.3, SC-M14-004/E9.4, SC-M14-004/V1.1, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-004/V4.3, SC-M14-004/V4.4, SC-M14-006/E7.1, RULE-M14-001, RULE-M14-005, D-FLAGS | Có vị trí đối soát phần có hợp đồng |
| FR-M14-01.08 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-003/V1.1, SC-M14-004/V1.1, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-01.09 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-003/V1.1, SC-M14-004/V1.1, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-02.01 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E3.1, SC-M14-001/E3.2, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-002/M1, SC-M14-002/M2, SC-M14-002/M3, SC-M14-002/M4, SC-M14-002/E1.1, SC-M14-002/E1.2, SC-M14-002/E1.3, SC-M14-002/E1.4, SC-M14-002/E2.1, SC-M14-002/E2.2, SC-M14-002/E2.3, SC-M14-002/E3.1, SC-M14-002/E4.1, SC-M14-002/E4.2, SC-M14-002/E4.3, SC-M14-002/E4.4, SC-M14-002/V1.1, SC-M14-002/V1.2, SC-M14-002/V1.3, SC-M14-002/V1.4, SC-M14-002/V2.1, SC-M14-002/V2.2, SC-M14-002/V2.3, SC-M14-002/V2.4, SC-M14-002/V3.1, SC-M14-002/V3.2, SC-M14-002/V3.3, SC-M14-002/V3.4, SC-M14-003/V1.1, SC-M14-004/V1.1, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-02.02 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E3.1, SC-M14-001/E3.2, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-002/M1, SC-M14-002/M2, SC-M14-002/M3, SC-M14-002/M4, SC-M14-002/E1.1, SC-M14-002/E1.2, SC-M14-002/E1.3, SC-M14-002/E1.4, SC-M14-002/E2.1, SC-M14-002/E2.2, SC-M14-002/E2.3, SC-M14-002/E3.1, SC-M14-002/E4.1, SC-M14-002/E4.2, SC-M14-002/E4.3, SC-M14-002/E4.4, SC-M14-002/V1.1, SC-M14-002/V1.2, SC-M14-002/V1.3, SC-M14-002/V1.4, SC-M14-002/V2.1, SC-M14-002/V2.2, SC-M14-002/V2.3, SC-M14-002/V2.4, SC-M14-002/V3.1, SC-M14-002/V3.2, SC-M14-002/V3.3, SC-M14-002/V3.4, SC-M14-003/V1.1, SC-M14-004/V1.1, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-02.03 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2 | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-001 |
| FR-M14-02.04 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2, RULE-M14-002 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-02.05 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2, SC-M14-003/M2, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-003/V4.2, SC-M14-004/M2, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-004/V4.2, SC-M14-005/M2, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, SC-M14-006/M2, SC-M14-006/E1.2, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.2, SC-M14-006/E5.2, SC-M14-006/E6.2, SC-M14-006/E7.2, SC-M14-006/V1.2, SC-M14-006/V2.2, SC-M14-006/V3.2, SC-M14-006/V5.2, SC-M14-006/V6.2, SC-M14-006/V8.2, SC-M14-006/V9.2, RULE-M14-006 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-02.06 | SC-M14-001/E3.1, SC-M14-001/E3.2, SC-M14-002/M1, SC-M14-002/M2, SC-M14-002/M3, SC-M14-002/M4, SC-M14-002/E1.1, SC-M14-002/E1.2, SC-M14-002/E1.3, SC-M14-002/E1.4, SC-M14-002/E2.1, SC-M14-002/E2.2, SC-M14-002/E2.3, SC-M14-002/E3.1, SC-M14-002/E4.1, SC-M14-002/E4.2, SC-M14-002/E4.3, SC-M14-002/E4.4, SC-M14-002/V1.1, SC-M14-002/V1.2, SC-M14-002/V1.3, SC-M14-002/V1.4, SC-M14-002/V2.1, SC-M14-002/V2.2, SC-M14-002/V2.3, SC-M14-002/V2.4, SC-M14-002/V3.1, SC-M14-002/V3.2, SC-M14-002/V3.3, SC-M14-002/V3.4, RULE-M14-003 | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-001 |
| FR-M14-02.07 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.1, SC-M14-001/E3.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2, SC-M14-002/M1, SC-M14-002/M2, SC-M14-002/M3, SC-M14-002/M4, SC-M14-002/E1.1, SC-M14-002/E1.2, SC-M14-002/E1.3, SC-M14-002/E1.4, SC-M14-002/E2.1, SC-M14-002/E2.2, SC-M14-002/E2.3, SC-M14-002/E3.1, SC-M14-002/E4.1, SC-M14-002/E4.2, SC-M14-002/E4.3, SC-M14-002/E4.4, SC-M14-002/V1.1, SC-M14-002/V1.2, SC-M14-002/V1.3, SC-M14-002/V1.4, SC-M14-002/V2.1, SC-M14-002/V2.2, SC-M14-002/V2.3, SC-M14-002/V2.4, SC-M14-002/V3.1, SC-M14-002/V3.2, SC-M14-002/V3.3, SC-M14-002/V3.4, AUT-M14-002, RULE-M14-004 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-02.08 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/E11.3, SC-M14-001/E11.4, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2, SC-M14-001/V4.3, SC-M14-001/V4.4, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/E9.3, SC-M14-003/E9.4, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-003/V4.3, SC-M14-003/V4.4, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/E9.3, SC-M14-004/E9.4, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-004/V4.3, SC-M14-004/V4.4, SC-M14-006/E7.1, RULE-M14-005, D-FLAGS | Có vị trí đối soát phần có hợp đồng |
| FR-M14-02.09 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2, RULE-M14-002, RULE-M14-006, D-PRIVACY | Có vị trí đối soát phần có hợp đồng |
| FR-M14-02.10 | SC-M14-001/E3.1, SC-M14-001/E3.2, SC-M14-002/M1, SC-M14-002/M2, SC-M14-002/M3, SC-M14-002/M4, SC-M14-002/E1.1, SC-M14-002/E1.2, SC-M14-002/E1.3, SC-M14-002/E1.4, SC-M14-002/E2.1, SC-M14-002/E2.2, SC-M14-002/E2.3, SC-M14-002/E3.1, SC-M14-002/E4.1, SC-M14-002/E4.2, SC-M14-002/E4.3, SC-M14-002/E4.4, SC-M14-002/V1.1, SC-M14-002/V1.2, SC-M14-002/V1.3, SC-M14-002/V1.4, SC-M14-002/V2.1, SC-M14-002/V2.2, SC-M14-002/V2.3, SC-M14-002/V2.4, SC-M14-002/V3.1, SC-M14-002/V3.2, SC-M14-002/V3.3, SC-M14-002/V3.4, RULE-M14-003, RULE-M14-004 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-02.11 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.1, SC-M14-001/E3.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2, SC-M14-002/M1, SC-M14-002/M2, SC-M14-002/M3, SC-M14-002/M4, SC-M14-002/E1.1, SC-M14-002/E1.2, SC-M14-002/E1.3, SC-M14-002/E1.4, SC-M14-002/E2.1, SC-M14-002/E2.2, SC-M14-002/E2.3, SC-M14-002/E3.1, SC-M14-002/E4.1, SC-M14-002/E4.2, SC-M14-002/E4.3, SC-M14-002/E4.4, SC-M14-002/V1.1, SC-M14-002/V1.2, SC-M14-002/V1.3, SC-M14-002/V1.4, SC-M14-002/V2.1, SC-M14-002/V2.2, SC-M14-002/V2.3, SC-M14-002/V2.4, SC-M14-002/V3.1, SC-M14-002/V3.2, SC-M14-002/V3.3, SC-M14-002/V3.4, RULE-M14-004, D-BATCH | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-002, GAP-SC-M14-006 |
| FR-M14-02.12 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.1, SC-M14-001/E3.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2, SC-M14-002/M1, SC-M14-002/M2, SC-M14-002/M3, SC-M14-002/M4, SC-M14-002/E1.1, SC-M14-002/E1.2, SC-M14-002/E1.3, SC-M14-002/E1.4, SC-M14-002/E2.1, SC-M14-002/E2.2, SC-M14-002/E2.3, SC-M14-002/E3.1, SC-M14-002/E4.1, SC-M14-002/E4.2, SC-M14-002/E4.3, SC-M14-002/E4.4, SC-M14-002/V1.1, SC-M14-002/V1.2, SC-M14-002/V1.3, SC-M14-002/V1.4, SC-M14-002/V2.1, SC-M14-002/V2.2, SC-M14-002/V2.3, SC-M14-002/V2.4, SC-M14-002/V3.1, SC-M14-002/V3.2, SC-M14-002/V3.3, SC-M14-002/V3.4, RULE-M14-004, D-BATCH | Có vị trí đối soát phần có hợp đồng |
| FR-M14-03.01 | AUT-M14-001, RULE-M14-003, D-AGE | Có vị trí đối soát phần có hợp đồng |
| FR-M14-03.02 | AUT-M14-001, RULE-M14-003, D-CURRENT, D-BATCH | Có vị trí đối soát phần có hợp đồng |
| FR-M14-03.03 | AUT-M14-001, RULE-M14-003, D-BATCH | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-005 |
| FR-M14-03.04 | AUT-M14-001, RULE-M14-003, D-BATCH | Có vị trí đối soát phần có hợp đồng |
| FR-M14-03.05 | AUT-M14-001, RULE-M14-003, D-AGE | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-006 |
| FR-M14-03.06 | AUT-M14-001, RULE-M14-003 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-03.07 | AUT-M14-001, RULE-M14-003, D-CURRENT | Có vị trí đối soát phần có hợp đồng |
| FR-M14-03.08 | AUT-M14-001, RULE-M14-003, D-SCORE-STATUS | Có vị trí đối soát phần có hợp đồng |
| FR-M14-03.09 | AUT-M14-001, RULE-M14-003 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-03.10 | AUT-M14-001, RULE-M14-003, D-CURRENT, D-BATCH | Có vị trí đối soát phần có hợp đồng |
| FR-M14-03.11 | SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/E11.3, SC-M14-001/E11.4, SC-M14-001/V4.1, SC-M14-001/V4.2, SC-M14-001/V4.3, SC-M14-001/V4.4, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/E9.3, SC-M14-003/E9.4, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-003/V4.3, SC-M14-003/V4.4, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/E9.3, SC-M14-004/E9.4, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-004/V4.3, SC-M14-004/V4.4, SC-M14-006/E7.1, AUT-M14-001, RULE-M14-003, RULE-M14-005, D-FLAGS | Có vị trí đối soát phần có hợp đồng |
| FR-M14-03.12 | AUT-M14-001, RULE-M14-003, D-CURRENT, D-AGE | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-006 |
| FR-M14-03.13 | AUT-M14-001, RULE-M14-003, D-CURRENT | Có vị trí đối soát phần có hợp đồng |
| FR-M14-03.14 | AUT-M14-001, RULE-M14-003 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-03.15 | AUT-M14-001, RULE-M14-003, D-BATCH | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-005 |
| FR-M14-04.01 | SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/V5.2, SC-M14-006/V6.2, RULE-M14-002 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-04.02 | SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/V5.2, SC-M14-006/V6.2, RULE-M14-002 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-04.03 | SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/V5.2, SC-M14-006/V6.2, RULE-M14-002 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-04.04 | SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V1.2, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/V4.1, SC-M14-006/V4.2, SC-M14-006/V5.2, SC-M14-006/V6.2, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-04.05 | SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E5.1, SC-M14-003/E6.1, SC-M14-003/E6.2, SC-M14-003/E6.3, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/V5.2, SC-M14-006/V6.2, D-FOLLOW-EMPTY | Có vị trí đối soát phần có hợp đồng |
| FR-M14-04.06 | SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/V5.2, SC-M14-006/V6.2, RULE-M14-002 | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-003 |
| FR-M14-04.07 | SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/V5.2, SC-M14-006/V6.2, RULE-M14-002 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-04.09 | SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/V5.2, SC-M14-006/V6.2, RULE-M14-002, RULE-M14-006 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-04.10 | SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/V5.2, SC-M14-006/V6.2, RULE-M14-002, RULE-M14-006 | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-004 |
| FR-M14-04.11 | SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E7.1, SC-M14-003/E8.1, SC-M14-003/E8.2, SC-M14-003/E8.3, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/V5.2, SC-M14-006/V6.2, D-FOLLOW-EMPTY | Có vị trí đối soát phần có hợp đồng |
| FR-M14-04.12 | SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/E11.3, SC-M14-001/E11.4, SC-M14-001/V4.1, SC-M14-001/V4.2, SC-M14-001/V4.3, SC-M14-001/V4.4, SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/E9.3, SC-M14-003/E9.4, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-003/V4.3, SC-M14-003/V4.4, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/E9.3, SC-M14-004/E9.4, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-004/V4.3, SC-M14-004/V4.4, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E7.1, SC-M14-006/V5.2, SC-M14-006/V6.2, RULE-M14-005, D-FLAGS | Có vị trí đối soát phần có hợp đồng |
| FR-M14-04.13 | SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/V5.2, SC-M14-006/V6.2, RULE-M14-002, RULE-M14-006, D-PRIVACY | Có vị trí đối soát phần có hợp đồng |
| FR-M14-05.01 | SC-M14-004/M1, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/V1.1, SC-M14-004/V2.1, SC-M14-004/V2.2, SC-M14-004/V3.1, SC-M14-004/V3.2, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V8.2, SC-M14-006/V9.2, RULE-M14-002, D-PRIVACY | Có vị trí đối soát phần có hợp đồng |
| FR-M14-05.02 | SC-M14-004/M1, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/V1.1, SC-M14-004/V2.1, SC-M14-004/V2.2, SC-M14-004/V3.1, SC-M14-004/V3.2, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V8.2, SC-M14-006/V9.2, RULE-M14-002 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-05.03 | SC-M14-004/M1, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/V1.1, SC-M14-004/V2.1, SC-M14-004/V2.2, SC-M14-004/V3.1, SC-M14-004/V3.2, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V8.2, SC-M14-006/V9.2, RULE-M14-002 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-05.04 | SC-M14-004/M1, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/V1.1, SC-M14-004/V2.1, SC-M14-004/V2.2, SC-M14-004/V3.1, SC-M14-004/V3.2, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V8.2, SC-M14-006/V9.2, RULE-M14-002 | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-003 |
| FR-M14-05.05 | SC-M14-004/M1, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/V1.1, SC-M14-004/V1.2, SC-M14-004/V2.1, SC-M14-004/V2.2, SC-M14-004/V3.1, SC-M14-004/V3.2, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V7.1, SC-M14-006/V7.2, SC-M14-006/V8.2, SC-M14-006/V9.2, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-05.06 | SC-M14-004/M1, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E5.1, SC-M14-004/E6.1, SC-M14-004/E6.2, SC-M14-004/E6.3, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/V1.1, SC-M14-004/V2.1, SC-M14-004/V2.2, SC-M14-004/V3.1, SC-M14-004/V3.2, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V8.2, SC-M14-006/V9.2, D-FOLLOW-EMPTY | Có vị trí đối soát phần có hợp đồng |
| FR-M14-05.07 | SC-M14-004/M1, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E7.1, SC-M14-004/E8.1, SC-M14-004/E8.2, SC-M14-004/E8.3, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/V1.1, SC-M14-004/V2.1, SC-M14-004/V2.2, SC-M14-004/V3.1, SC-M14-004/V3.2, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V8.2, SC-M14-006/V9.2, D-FOLLOW-EMPTY | Có vị trí đối soát phần có hợp đồng |
| FR-M14-05.08 | SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/E11.3, SC-M14-001/E11.4, SC-M14-001/V4.1, SC-M14-001/V4.2, SC-M14-001/V4.3, SC-M14-001/V4.4, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/E9.3, SC-M14-003/E9.4, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-003/V4.3, SC-M14-003/V4.4, SC-M14-004/M1, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/E9.3, SC-M14-004/E9.4, SC-M14-004/V1.1, SC-M14-004/V2.1, SC-M14-004/V2.2, SC-M14-004/V3.1, SC-M14-004/V3.2, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-004/V4.3, SC-M14-004/V4.4, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V8.2, SC-M14-006/V9.2, RULE-M14-005, D-FLAGS | Có vị trí đối soát phần có hợp đồng |
| FR-M14-06.01 | SC-M14-005/M1, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.1, SC-M14-005/V1.2, SC-M14-005/V2.1, SC-M14-005/V2.2, SC-M14-005/V3.1, SC-M14-005/V3.2, SC-M14-006/M2, SC-M14-006/E3.1, SC-M14-006/E6.2, SC-M14-006/V1.2, SC-M14-006/V2.2, SC-M14-006/V3.2, RULE-M14-002 | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-001 |
| FR-M14-06.02 | SC-M14-005/M1, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.1, SC-M14-005/V1.2, SC-M14-005/V2.1, SC-M14-005/V2.2, SC-M14-005/V3.1, SC-M14-005/V3.2, SC-M14-006/M2, SC-M14-006/E3.1, SC-M14-006/E6.2, SC-M14-006/V1.2, SC-M14-006/V2.2, SC-M14-006/V3.2, RULE-M14-002 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-06.03 | SC-M14-005/M1, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.1, SC-M14-005/V1.2, SC-M14-005/V2.1, SC-M14-005/V2.2, SC-M14-005/V3.1, SC-M14-005/V3.2, SC-M14-006/M2, SC-M14-006/E3.1, SC-M14-006/E6.2, SC-M14-006/V1.2, SC-M14-006/V2.2, SC-M14-006/V3.2, RULE-M14-002 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-06.04 | SC-M14-005/M1, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.1, SC-M14-005/V1.2, SC-M14-005/V2.1, SC-M14-005/V2.2, SC-M14-005/V3.1, SC-M14-005/V3.2, SC-M14-006/M2, SC-M14-006/E3.1, SC-M14-006/E6.2, SC-M14-006/V1.2, SC-M14-006/V2.2, SC-M14-006/V3.2, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-07.01 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M5, SC-M14-001/M6, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.2, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.2, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.2, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.2, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.2, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.5, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.5, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.5, SC-M14-001/V3.6, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.3, SC-M14-003/E1.4, SC-M14-003/E1.5, SC-M14-003/E1.6, SC-M14-003/E2.1, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.3, SC-M14-004/E1.4, SC-M14-004/E1.5, SC-M14-004/E1.6, SC-M14-004/E2.1, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.3, SC-M14-005/E1.4, SC-M14-005/E1.5, SC-M14-005/E1.6, SC-M14-005/E2.1, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, RULE-M14-004 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-07.02 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M5, SC-M14-001/M6, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.2, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.2, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.2, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.2, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.2, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.5, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.5, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.5, SC-M14-001/V3.6, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.3, SC-M14-003/E1.4, SC-M14-003/E1.5, SC-M14-003/E1.6, SC-M14-003/E2.1, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.3, SC-M14-004/E1.4, SC-M14-004/E1.5, SC-M14-004/E1.6, SC-M14-004/E2.1, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.3, SC-M14-005/E1.4, SC-M14-005/E1.5, SC-M14-005/E1.6, SC-M14-005/E2.1, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, RULE-M14-004 | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-001 |
| FR-M14-07.03 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M5, SC-M14-001/M6, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.2, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.2, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.2, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.2, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.2, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.5, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.5, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.5, SC-M14-001/V3.6, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.3, SC-M14-003/E1.4, SC-M14-003/E1.5, SC-M14-003/E1.6, SC-M14-003/E2.1, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.3, SC-M14-004/E1.4, SC-M14-004/E1.5, SC-M14-004/E1.6, SC-M14-004/E2.1, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.3, SC-M14-005/E1.4, SC-M14-005/E1.5, SC-M14-005/E1.6, SC-M14-005/E2.1, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, RULE-M14-004 | Có vị trí đối soát phần có hợp đồng |
| FR-M14-07.04 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M5, SC-M14-001/M6, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.2, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.2, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.2, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.2, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.2, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.5, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.5, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.5, SC-M14-001/V3.6, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.3, SC-M14-003/E1.4, SC-M14-003/E1.5, SC-M14-003/E1.6, SC-M14-003/E2.1, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.3, SC-M14-004/E1.4, SC-M14-004/E1.5, SC-M14-004/E1.6, SC-M14-004/E2.1, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.3, SC-M14-005/E1.4, SC-M14-005/E1.5, SC-M14-005/E1.6, SC-M14-005/E2.1, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, RULE-M14-004 | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-002 |
| FR-M14-07.05 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M5, SC-M14-001/M6, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.2, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.2, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.2, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.2, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.2, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.5, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.5, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.5, SC-M14-001/V3.6, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.3, SC-M14-003/E1.4, SC-M14-003/E1.5, SC-M14-003/E1.6, SC-M14-003/E2.1, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.3, SC-M14-004/E1.4, SC-M14-004/E1.5, SC-M14-004/E1.6, SC-M14-004/E2.1, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.3, SC-M14-005/E1.4, SC-M14-005/E1.5, SC-M14-005/E1.6, SC-M14-005/E2.1, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, RULE-M14-004, D-BATCH | Có vị trí đối soát phần có hợp đồng |
| FR-M14-08.01 | SC-M14-006/M1, SC-M14-006/M2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E6.1, SC-M14-006/E6.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V1.1, SC-M14-006/V1.2, SC-M14-006/V2.1, SC-M14-006/V2.2, SC-M14-006/V3.1, SC-M14-006/V3.2, SC-M14-006/V4.1, SC-M14-006/V5.1, SC-M14-006/V5.2, SC-M14-006/V6.1, SC-M14-006/V6.2, SC-M14-006/V7.1, SC-M14-006/V8.1, SC-M14-006/V8.2, SC-M14-006/V9.1, SC-M14-006/V9.2, AUT-M14-002, RULE-M14-004, D-POLL, D-POLL-SCOPE | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-005 |
| FR-M14-08.02 | SC-M14-006/M1, SC-M14-006/M2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E6.1, SC-M14-006/E6.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V1.1, SC-M14-006/V1.2, SC-M14-006/V2.1, SC-M14-006/V2.2, SC-M14-006/V3.1, SC-M14-006/V3.2, SC-M14-006/V4.1, SC-M14-006/V5.1, SC-M14-006/V5.2, SC-M14-006/V6.1, SC-M14-006/V6.2, SC-M14-006/V7.1, SC-M14-006/V8.1, SC-M14-006/V8.2, SC-M14-006/V9.1, SC-M14-006/V9.2, AUT-M14-002, RULE-M14-004, D-POLL, D-POLL-SCOPE | Có vị trí đối soát phần có hợp đồng |
| FR-M14-08.03 | SC-M14-006/M1, SC-M14-006/M2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E6.1, SC-M14-006/E6.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V1.1, SC-M14-006/V1.2, SC-M14-006/V2.1, SC-M14-006/V2.2, SC-M14-006/V3.1, SC-M14-006/V3.2, SC-M14-006/V4.1, SC-M14-006/V5.1, SC-M14-006/V5.2, SC-M14-006/V6.1, SC-M14-006/V6.2, SC-M14-006/V7.1, SC-M14-006/V8.1, SC-M14-006/V8.2, SC-M14-006/V9.1, SC-M14-006/V9.2, RULE-M14-004, D-POLL | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-003 |
| FR-M14-08.04 | SC-M14-006/M1, SC-M14-006/M2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E6.1, SC-M14-006/E6.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V1.1, SC-M14-006/V1.2, SC-M14-006/V2.1, SC-M14-006/V2.2, SC-M14-006/V3.1, SC-M14-006/V3.2, SC-M14-006/V4.1, SC-M14-006/V5.1, SC-M14-006/V5.2, SC-M14-006/V6.1, SC-M14-006/V6.2, SC-M14-006/V7.1, SC-M14-006/V8.1, SC-M14-006/V8.2, SC-M14-006/V9.1, SC-M14-006/V9.2, RULE-M14-004, D-POLL | Có vị trí đối soát phần có hợp đồng |
| FR-M14-08.05 | SC-M14-006/M1, SC-M14-006/M2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E6.1, SC-M14-006/E6.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V1.1, SC-M14-006/V1.2, SC-M14-006/V2.1, SC-M14-006/V2.2, SC-M14-006/V3.1, SC-M14-006/V3.2, SC-M14-006/V4.1, SC-M14-006/V5.1, SC-M14-006/V5.2, SC-M14-006/V6.1, SC-M14-006/V6.2, SC-M14-006/V7.1, SC-M14-006/V8.1, SC-M14-006/V8.2, SC-M14-006/V9.1, SC-M14-006/V9.2, AUT-M14-002, RULE-M14-004, D-POLL, D-POLL-SCOPE | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-003 |
| FR-M14-08.06 | SC-M14-006/M1, SC-M14-006/M2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E6.1, SC-M14-006/E6.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V1.1, SC-M14-006/V1.2, SC-M14-006/V2.1, SC-M14-006/V2.2, SC-M14-006/V3.1, SC-M14-006/V3.2, SC-M14-006/V4.1, SC-M14-006/V5.1, SC-M14-006/V5.2, SC-M14-006/V6.1, SC-M14-006/V6.2, SC-M14-006/V7.1, SC-M14-006/V8.1, SC-M14-006/V8.2, SC-M14-006/V9.1, SC-M14-006/V9.2, AUT-M14-002, RULE-M14-004, D-POLL | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-005 |
| FR-M14-08.07 | SC-M14-006/M1, SC-M14-006/M2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E6.1, SC-M14-006/E6.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V1.1, SC-M14-006/V1.2, SC-M14-006/V2.1, SC-M14-006/V2.2, SC-M14-006/V3.1, SC-M14-006/V3.2, SC-M14-006/V4.1, SC-M14-006/V5.1, SC-M14-006/V5.2, SC-M14-006/V6.1, SC-M14-006/V6.2, SC-M14-006/V7.1, SC-M14-006/V8.1, SC-M14-006/V8.2, SC-M14-006/V9.1, SC-M14-006/V9.2, RULE-M14-004, D-POLL | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-003 |
| BR-M14-01 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-003/V1.1, SC-M14-004/V1.1, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| BR-M14-02 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V1.2, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-004/M1, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/V1.1, SC-M14-004/V1.2, SC-M14-004/V2.1, SC-M14-004/V2.2, SC-M14-004/V3.1, SC-M14-004/V3.2, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-005/M1, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.1, SC-M14-005/V1.2, SC-M14-005/V2.1, SC-M14-005/V2.2, SC-M14-005/V3.1, SC-M14-005/V3.2, SC-M14-006/M2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E6.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V1.2, SC-M14-006/V2.2, SC-M14-006/V3.2, SC-M14-006/V4.2, SC-M14-006/V5.2, SC-M14-006/V6.2, SC-M14-006/V7.2, SC-M14-006/V8.2, SC-M14-006/V9.2, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| BR-M14-03 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-003/V1.1, SC-M14-004/V1.1, RULE-M14-001 | Có vị trí đối soát phần có hợp đồng |
| BR-M14-04 | SC-M14-001/M2, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.2, SC-M14-003/M2, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-003/V4.2, SC-M14-004/M2, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-004/V4.2, SC-M14-005/M2, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, SC-M14-006/M2, SC-M14-006/E1.2, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.2, SC-M14-006/E5.2, SC-M14-006/E6.2, SC-M14-006/E7.2, SC-M14-006/V1.2, SC-M14-006/V2.2, SC-M14-006/V3.2, SC-M14-006/V5.2, SC-M14-006/V6.2, SC-M14-006/V8.2, SC-M14-006/V9.2, AUT-M14-001, RULE-M14-006 | Có vị trí đối soát phần có hợp đồng |
| BR-M14-05 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2, AUT-M14-001, RULE-M14-002, RULE-M14-006, D-POLL-SCOPE | Có vị trí đối soát phần có hợp đồng |
| BR-M14-06 | SC-M14-005/M1, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.1, SC-M14-005/V1.2, SC-M14-005/V2.1, SC-M14-005/V2.2, SC-M14-005/V3.1, SC-M14-005/V3.2, SC-M14-006/M2, SC-M14-006/E3.1, SC-M14-006/E6.2, SC-M14-006/V1.2, SC-M14-006/V2.2, SC-M14-006/V3.2, RULE-M14-002, D-POLL-SCOPE | Có vị trí đối soát phần có hợp đồng |
| BR-M14-07 | SC-M14-004/M1, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/V1.1, SC-M14-004/V2.1, SC-M14-004/V2.2, SC-M14-004/V3.1, SC-M14-004/V3.2, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V8.2, SC-M14-006/V9.2, RULE-M14-002, D-POLL-SCOPE | Có vị trí đối soát phần có hợp đồng |
| BR-M14-08 | SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/V5.2, SC-M14-006/V6.2, RULE-M14-002, RULE-M14-006, D-POLL-SCOPE | Có vị trí đối soát phần có hợp đồng |
| BR-M14-09 | SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-004/M1, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/V1.1, SC-M14-004/V2.1, SC-M14-004/V2.2, SC-M14-004/V3.1, SC-M14-004/V3.2, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-005/M1, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.1, SC-M14-005/V1.2, SC-M14-005/V2.1, SC-M14-005/V2.2, SC-M14-005/V3.1, SC-M14-005/V3.2, SC-M14-006/M1, SC-M14-006/M2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E6.1, SC-M14-006/E6.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V1.1, SC-M14-006/V1.2, SC-M14-006/V2.1, SC-M14-006/V2.2, SC-M14-006/V3.1, SC-M14-006/V3.2, SC-M14-006/V4.1, SC-M14-006/V5.1, SC-M14-006/V5.2, SC-M14-006/V6.1, SC-M14-006/V6.2, SC-M14-006/V7.1, SC-M14-006/V8.1, SC-M14-006/V8.2, SC-M14-006/V9.1, SC-M14-006/V9.2, RULE-M14-002 | Có vị trí đối soát phần có hợp đồng |
| BR-M14-10 | AUT-M14-001, RULE-M14-003, D-CURRENT | Có vị trí đối soát phần có hợp đồng |
| BR-M14-11 | AUT-M14-001, RULE-M14-003, D-AGE | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-006 |
| BR-M14-12 | AUT-M14-001, RULE-M14-003 | Có vị trí đối soát phần có hợp đồng |
| BR-M14-13 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2, AUT-M14-001, RULE-M14-003 | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-002 |
| BR-M14-14 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2, AUT-M14-001, RULE-M14-003, D-BATCH | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-001 |
| BR-M14-15 | SC-M14-001/M2, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.2, SC-M14-003/M2, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-003/V4.2, SC-M14-004/M2, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-004/V4.2, SC-M14-005/M2, SC-M14-005/E1.2, SC-M14-005/E1.4, SC-M14-005/E1.6, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, SC-M14-006/M2, SC-M14-006/E1.2, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.2, SC-M14-006/E5.2, SC-M14-006/E6.2, SC-M14-006/E7.2, SC-M14-006/V1.2, SC-M14-006/V2.2, SC-M14-006/V3.2, SC-M14-006/V5.2, SC-M14-006/V6.2, SC-M14-006/V8.2, SC-M14-006/V9.2, AUT-M14-001, RULE-M14-003, RULE-M14-006, D-SCORE-STATUS | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-004 |
| BR-M14-16 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M5, SC-M14-001/M6, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.2, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.2, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.2, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.2, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.2, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.5, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.5, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.5, SC-M14-001/V3.6, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.3, SC-M14-003/E1.4, SC-M14-003/E1.5, SC-M14-003/E1.6, SC-M14-003/E2.1, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.3, SC-M14-004/E1.4, SC-M14-004/E1.5, SC-M14-004/E1.6, SC-M14-004/E2.1, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.3, SC-M14-005/E1.4, SC-M14-005/E1.5, SC-M14-005/E1.6, SC-M14-005/E2.1, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, RULE-M14-004 | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-002, GAP-SC-M14-005 |
| BR-M14-17 | SC-M14-006/M1, SC-M14-006/M2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E6.1, SC-M14-006/E6.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V1.1, SC-M14-006/V1.2, SC-M14-006/V2.1, SC-M14-006/V2.2, SC-M14-006/V3.1, SC-M14-006/V3.2, SC-M14-006/V4.1, SC-M14-006/V5.1, SC-M14-006/V5.2, SC-M14-006/V6.1, SC-M14-006/V6.2, SC-M14-006/V7.1, SC-M14-006/V8.1, SC-M14-006/V8.2, SC-M14-006/V9.1, SC-M14-006/V9.2, AUT-M14-002, RULE-M14-004, D-POLL, D-POLL-SCOPE | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-003 |
| BR-M14-18 | SC-M14-006/M1, SC-M14-006/M2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E3.1, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E6.1, SC-M14-006/E6.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V1.1, SC-M14-006/V1.2, SC-M14-006/V2.1, SC-M14-006/V2.2, SC-M14-006/V3.1, SC-M14-006/V3.2, SC-M14-006/V4.1, SC-M14-006/V5.1, SC-M14-006/V5.2, SC-M14-006/V6.1, SC-M14-006/V6.2, SC-M14-006/V7.1, SC-M14-006/V8.1, SC-M14-006/V8.2, SC-M14-006/V9.1, SC-M14-006/V9.2, AUT-M14-002, RULE-M14-004, D-POLL | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-003, GAP-SC-M14-005 |
| BR-M14-19 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M5, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.1, SC-M14-001/E3.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.2, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.2, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.2, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.2, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.2, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.5, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.5, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.5, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2, SC-M14-002/M1, SC-M14-002/M2, SC-M14-002/M3, SC-M14-002/M4, SC-M14-002/E1.1, SC-M14-002/E1.2, SC-M14-002/E1.3, SC-M14-002/E1.4, SC-M14-002/E2.1, SC-M14-002/E2.2, SC-M14-002/E2.3, SC-M14-002/E3.1, SC-M14-002/E4.1, SC-M14-002/E4.2, SC-M14-002/E4.3, SC-M14-002/E4.4, SC-M14-002/V1.1, SC-M14-002/V1.2, SC-M14-002/V1.3, SC-M14-002/V1.4, SC-M14-002/V2.1, SC-M14-002/V2.2, SC-M14-002/V2.3, SC-M14-002/V2.4, SC-M14-002/V3.1, SC-M14-002/V3.2, SC-M14-002/V3.3, SC-M14-002/V3.4, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.3, SC-M14-003/E1.4, SC-M14-003/E1.5, SC-M14-003/E1.6, SC-M14-003/E2.1, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.2, SC-M14-003/V2.2, SC-M14-003/V3.2, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.3, SC-M14-004/E1.4, SC-M14-004/E1.5, SC-M14-004/E1.6, SC-M14-004/E2.1, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.2, SC-M14-004/V2.2, SC-M14-004/V3.2, SC-M14-005/M2, SC-M14-005/E1.1, SC-M14-005/E1.2, SC-M14-005/E1.3, SC-M14-005/E1.4, SC-M14-005/E1.5, SC-M14-005/E1.6, SC-M14-005/E2.1, SC-M14-005/E2.2, SC-M14-005/E3.1, SC-M14-005/V1.2, SC-M14-005/V2.2, SC-M14-005/V3.2, AUT-M14-001, AUT-M14-002, RULE-M14-004, D-AGE, D-BATCH | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-002, GAP-SC-M14-006 |
| BR-M14-20 | SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E5.1, SC-M14-003/E6.1, SC-M14-003/E6.2, SC-M14-003/E6.3, SC-M14-003/E7.1, SC-M14-003/E8.1, SC-M14-003/E8.2, SC-M14-003/E8.3, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/V5.2, SC-M14-006/V6.2, D-FOLLOW-EMPTY | Có vị trí đối soát phần có hợp đồng |
| BR-M14-21 | SC-M14-004/M1, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E5.1, SC-M14-004/E6.1, SC-M14-004/E6.2, SC-M14-004/E6.3, SC-M14-004/E7.1, SC-M14-004/E8.1, SC-M14-004/E8.2, SC-M14-004/E8.3, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/V1.1, SC-M14-004/V2.1, SC-M14-004/V2.2, SC-M14-004/V3.1, SC-M14-004/V3.2, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V8.2, SC-M14-006/V9.2, D-FOLLOW-EMPTY | Có vị trí đối soát phần có hợp đồng |
| BR-M14-22 | SC-M14-001/M1, SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E2.1, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.1, SC-M14-001/E11.2, SC-M14-001/E11.3, SC-M14-001/E11.4, SC-M14-001/V1.1, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.1, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.1, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2, SC-M14-001/V4.3, SC-M14-001/V4.4, SC-M14-003/M1, SC-M14-003/M2, SC-M14-003/E1.1, SC-M14-003/E1.2, SC-M14-003/E1.4, SC-M14-003/E1.6, SC-M14-003/E2.2, SC-M14-003/E3.1, SC-M14-003/E3.2, SC-M14-003/E4.1, SC-M14-003/E9.1, SC-M14-003/E9.2, SC-M14-003/E9.3, SC-M14-003/E9.4, SC-M14-003/V1.1, SC-M14-003/V2.1, SC-M14-003/V2.2, SC-M14-003/V3.1, SC-M14-003/V3.2, SC-M14-003/V4.1, SC-M14-003/V4.2, SC-M14-003/V4.3, SC-M14-003/V4.4, SC-M14-004/M1, SC-M14-004/M2, SC-M14-004/E1.1, SC-M14-004/E1.2, SC-M14-004/E1.4, SC-M14-004/E1.6, SC-M14-004/E2.2, SC-M14-004/E3.1, SC-M14-004/E3.2, SC-M14-004/E4.1, SC-M14-004/E9.1, SC-M14-004/E9.2, SC-M14-004/E9.3, SC-M14-004/E9.4, SC-M14-004/V1.1, SC-M14-004/V2.1, SC-M14-004/V2.2, SC-M14-004/V3.1, SC-M14-004/V3.2, SC-M14-004/V4.1, SC-M14-004/V4.2, SC-M14-004/V4.3, SC-M14-004/V4.4, SC-M14-006/E1.1, SC-M14-006/E1.2, SC-M14-006/E2.1, SC-M14-006/E2.2, SC-M14-006/E4.1, SC-M14-006/E4.2, SC-M14-006/E5.1, SC-M14-006/E5.2, SC-M14-006/E7.1, SC-M14-006/E7.2, SC-M14-006/V5.2, SC-M14-006/V6.2, SC-M14-006/V8.2, SC-M14-006/V9.2, AUT-M14-001, RULE-M14-005, D-FLAGS | Có vị trí đối soát phần có hợp đồng |
| BR-M14-23 | SC-M14-001/M2, SC-M14-001/M3, SC-M14-001/M4, SC-M14-001/M6, SC-M14-001/E1.1, SC-M14-001/E1.2, SC-M14-001/E2.2, SC-M14-001/E3.3, SC-M14-001/E3.4, SC-M14-001/E4.1, SC-M14-001/E4.3, SC-M14-001/E5.1, SC-M14-001/E5.3, SC-M14-001/E6.1, SC-M14-001/E6.3, SC-M14-001/E7.1, SC-M14-001/E7.3, SC-M14-001/E8.1, SC-M14-001/E8.3, SC-M14-001/E9.1, SC-M14-001/E10.1, SC-M14-001/E11.2, SC-M14-001/E12.2, SC-M14-001/V1.2, SC-M14-001/V1.3, SC-M14-001/V1.4, SC-M14-001/V1.6, SC-M14-001/V2.2, SC-M14-001/V2.3, SC-M14-001/V2.4, SC-M14-001/V2.6, SC-M14-001/V3.2, SC-M14-001/V3.3, SC-M14-001/V3.4, SC-M14-001/V3.6, SC-M14-001/V4.1, SC-M14-001/V4.2, RULE-M14-002, RULE-M14-006, D-PRIVACY | Có vị trí đối soát phần có hợp đồng |
| BR-M14-24 | SC-M14-001/E3.1, SC-M14-001/E3.2, SC-M14-002/M1, SC-M14-002/M2, SC-M14-002/M3, SC-M14-002/M4, SC-M14-002/E1.1, SC-M14-002/E1.2, SC-M14-002/E1.3, SC-M14-002/E1.4, SC-M14-002/E2.1, SC-M14-002/E2.2, SC-M14-002/E2.3, SC-M14-002/E3.1, SC-M14-002/E4.1, SC-M14-002/E4.2, SC-M14-002/E4.3, SC-M14-002/E4.4, SC-M14-002/V1.1, SC-M14-002/V1.2, SC-M14-002/V1.3, SC-M14-002/V1.4, SC-M14-002/V2.1, SC-M14-002/V2.2, SC-M14-002/V2.3, SC-M14-002/V2.4, SC-M14-002/V3.1, SC-M14-002/V3.2, SC-M14-002/V3.3, SC-M14-002/V3.4, RULE-M14-003, RULE-M14-004 | Có vị trí đối soát phần có hợp đồng. Giới hạn tại GAP-SC-M14-002 |


| Mã đã bỏ | Quyết định áp dụng |
|---|---|
| FR-M14-04.08 | Đã bỏ ở nguồn, dùng FR-M14-04.13 loại mọi Private khỏi Following kể cả thành viên. Mã đã bỏ được tách khỏi 104 mã hiệu lực. |


| UC owner | Điều kiện/lựa chọn | SC/nhánh | Kết thúc |
|---|---|---|---|
| UC-M14-001 | Guest chọn lại Trending từ một tab khác ở 10:25 | SC-M14-001/E1 | END:SUCCESS |
| UC-M14-001 | Guest tải lại trang ở 10:25 | SC-M14-001/E2 | END:SUCCESS |
| UC-M14-001 | Guest chỉ chuyển mục con rồi trở lại Post, vẫn ở cùng lượt Trending | SC-M14-001/E3 | END:SUCCESS |
| UC-M14-001 | P21 bị xóa mềm trước lần tải tiếp | SC-M14-001/E4 | END:SUCCESS |
| UC-M14-001 | P21 bị Mod ẩn trước lần tải tiếp | SC-M14-001/E5 | END:SUCCESS |
| UC-M14-001 | Tác giả riêng của P21 chuyển DEACTIVATED trước lần tải tiếp | SC-M14-001/E6 | END:SUCCESS |
| UC-M14-001 | Tác giả riêng của P21 chuyển DELETED trước lần tải tiếp | SC-M14-001/E7 | END:SUCCESS |
| UC-M14-001 | GJ chuyển từ Public sang Private trước lần tải tiếp, Guest ngoài nhóm | SC-M14-001/E8 | END:SUCCESS |
| UC-M14-001 | Dữ liệu của lần tính minh họa chỉ có 12 bài đủ điều kiện | SC-M14-001/E9 | END:SUCCESS |
| UC-M14-001 | Mọi cờ Group/Chat/Gamification đều Tắt | SC-M14-001/E10 | END:SUCCESS |
| UC-M14-001 | Group Tắt, Guest chọn mở bài nhóm được liệt kê | SC-M14-001/E11 | END:REJECTED |
| UC-M14-001 | Guest mở lại bằng link một bài GJ sau khi GJ đã chuyển Private | SC-M14-001/E12 | END:REJECTED |
| UC-M14-002 | Guest chọn Trending Tag | SC-M14-002/E1 | END:SUCCESS |
| UC-M14-002 | Danh sách M05 có mục điểm 0 hoặc Tag bị vô hiệu hóa từ trước lượt xem | SC-M14-002/E2 | END:SUCCESS |
| UC-M14-002 | M05 cung cấp bốn Topic có điểm bằng nhau từng phần để đối soát thứ tự | SC-M14-002/E3 | END:SUCCESS |
| UC-M14-002 | Guest chọn Tag với danh mục đã loại Tag vô hiệu hóa trước lượt xem | SC-M14-002/E4 | END:SUCCESS |
| UC-M14-021 | Người xem đọc hết bộ 45 bài của Following qua các lần cuộn | SC-M14-003/E1 | END:SUCCESS |
| UC-M14-021 | Có ba bài mới được đăng sau trang đầu, actor tiếp tục đọc phần cũ | SC-M14-003/E2 | END:SUCCESS |
| UC-M14-021 | An đã bỏ theo dõi U trước lần tải kế tiếp, vẫn theo dõi Topic Toán | SC-M14-003/E3 | END:SUCCESS |
| UC-M14-021 | Cờ Group và Gamification Tắt, quan hệ D-SET còn hiệu lực | SC-M14-003/E4 | END:SUCCESS |
| UC-M14-021 | An chưa theo dõi người dùng hoặc Topic nào | SC-M14-003/E5 | END:SUCCESS |
| UC-M14-021 | An chưa theo dõi người dùng hoặc Topic nào, An chọn tiếp lối tìm kiếm | SC-M14-003/E6 | END:HANDED_OFF |
| UC-M14-021 | An đã theo dõi U/Toán nhưng snapshot này chưa có bài phù hợp | SC-M14-003/E7 | END:SUCCESS |
| UC-M14-021 | An đã theo dõi U/Toán nhưng snapshot này chưa có bài phù hợp, An chọn tiếp lối tìm kiếm | SC-M14-003/E8 | END:HANDED_OFF |
| UC-M14-021 | Group Tắt, An chọn mở bài nhóm được liệt kê | SC-M14-003/E9 | END:REJECTED |
| UC-M14-022 | Người xem đọc hết bộ 45 bài của Group qua các lần cuộn | SC-M14-004/E1 | END:SUCCESS |
| UC-M14-022 | Có ba bài mới được đăng sau trang đầu, actor tiếp tục đọc phần cũ | SC-M14-004/E2 | END:SUCCESS |
| UC-M14-022 | An đã rời Public GJ trước lần tải kế tiếp, vẫn là thành viên Private GK | SC-M14-004/E3 | END:SUCCESS |
| UC-M14-022 | Cờ Group Tắt, thành viên D-SET còn hiệu lực | SC-M14-004/E4 | END:SUCCESS |
| UC-M14-022 | An chưa tham gia nhóm nào | SC-M14-004/E5 | END:SUCCESS |
| UC-M14-022 | An chưa tham gia nhóm nào, An chọn Khám phá Group | SC-M14-004/E6 | END:HANDED_OFF |
| UC-M14-022 | An đã tham gia GJ/GK nhưng snapshot này chưa có bài đủ điều kiện | SC-M14-004/E7 | END:SUCCESS |
| UC-M14-022 | An đã tham gia GJ/GK nhưng snapshot này chưa có bài đủ điều kiện, An chọn Khám phá Group | SC-M14-004/E8 | END:HANDED_OFF |
| UC-M14-022 | Group Tắt, An chọn mở bài nhóm được liệt kê | SC-M14-004/E9 | END:REJECTED |
| UC-M14-023 | Người xem đọc hết bộ 45 bài của Newest qua các lần cuộn | SC-M14-005/E1 | END:SUCCESS |
| UC-M14-023 | Có ba bài mới được đăng sau trang đầu, actor tiếp tục đọc phần cũ | SC-M14-005/E2 | END:SUCCESS |
| UC-M14-023 | Các cờ Group/Chat/Gamification đều Tắt | SC-M14-005/E3 | END:SUCCESS |
| UC-M14-005 | An nhận bài mới trong Following | SC-M14-006/E1 | END:SUCCESS |
| UC-M14-005 | An nhận bài mới trong Group | SC-M14-006/E2 | END:SUCCESS |
| UC-M14-005 | N01 bị xóa mềm và N02 bị Mod ẩn trước lúc An bấm, 28 bài còn lại hợp lệ | SC-M14-006/E3 | END:SUCCESS |
| UC-M14-005 | An bỏ theo dõi U trước click nhưng vẫn theo dõi Toán, 29 bài mới còn thỏa Topic | SC-M14-006/E4 | END:SUCCESS |
| UC-M14-005 | An rời GJ trước click, còn là thành viên GK, 15 bài mới còn hợp lệ | SC-M14-006/E5 | END:SUCCESS |
| UC-M14-005 | Chỉ có ba bài mới hợp lệ, actor chọn nhận | SC-M14-006/E6 | END:SUCCESS |
| UC-M14-005 | Cờ Group Tắt, An nhận bài mới tại Group theo quyền thành viên | SC-M14-006/E7 | END:SUCCESS |


| Lớp dữ liệu hoặc tổ hợp | Bằng chứng và giới hạn |
|---|---|
| Trang chủ/quyền | Guest và người đăng nhập đều Trending/Post, bốn tab hiện. Guest bị chặn Following/Group và yêu cầu banner tab riêng. Mod/Admin đọc theo quan hệ của chính mình. |
| Danh sách | D45/K0/K1 giữ kết quả khi cuộn/chuyển mục con, reload/mở lại nhận mới. D-TIME45 tải 20+20+5 ở từng tab thời gian. D-TOPIC/D-TAG tải 20+3. |
| Phạm vi và quan hệ | D-SET đối soát 8 Following/4 Group/6 Newest, OR không trùng, Private chỉ vào Group thành viên, ẩn danh qua Topic. Bỏ U/rời GJ trước lượt tải chỉ giữ R21 còn đủ điều kiện. |
| Quyền thay đổi trước lần tải | P21 bị xóa/ẩn hoặc tác giả DEACTIVATED/DELETED bị loại trong K0. GJ chuyển Private giữ P02 đã hiện theo nguồn, loại P21 ở lượt tải sau. Tranh chấp trong call thuộc GAP005. |
| Cờ và owner | Feed vẫn liệt kê khi Group/Gamification/Chat Tắt, U/nhãn vẫn theo nguồn, mở nhóm khôngADMIN bị báo bận, ADMIN đủ quyền nhận bài. Thứ hạng feed theo cùng chính sách nguồn. |
| Banner | 30 bài mới thêm đủ30, O35 còn chỗ đọc và thành vị trí65. Các tab F/G có đường riêng, bộ giảm còn28/29/15 có lọc hiện tại trước click, bộ3 thêm3. Tập rỗng hoặc tới thêm trong call thuộc GAP003/005. |
| Điểm và biên | Decay liên tục 0/3,5/7/14/28 ngày, >28 loại ở batch, hòa điểm dùng mới trước, đầu vào chỉ U/C/B hiệu lực. K0/K1 cập nhật trong hạn, lượt cũ còn K0 theo nguồn. |


104 mã hiệu lực gồm 8 nhóm, 72 FR chi tiết và 24 BR đều có vị trí truy vết. Từng bước có nguồn ngược. Sáu GAP bên dưới giữ phần hợp đồng còn cần xác nhận theo US.

## 7. GAP và trạng thái bàn giao

| ID | Ghi chú US | FR/BR | Điều cần làm rõ | Phạm vi và cách triển khai phần độc lập |
|---|---|---|---|---|
| GAP-SC-M14-001 | NOTE-M14-01 | FR-M14-02.03, FR-M14-02.06, FR-M14-06.01, FR-M14-07.02, BR-M14-14 | Kết quả trước lần tính Trending đầu tiên, cách trình bày rỗng Trending/Newest/Topic/Tag, lỗi dữ liệu/tải và con trỏ mất hiệu lực. | SC001/002/005 và UC004. Các đường đủ dữ liệu đã có kết quả dùng để soạn, các tình huống khởi tạo/rỗng/lỗi cần hợp đồng bổ sung. Following/Group rỗng đã có nguồn riêng. |
| GAP-SC-M14-002 | NOTE-M14-02 | FR-M14-02.11, FR-M14-07.04, BR-M14-13, BR-M14-16, BR-M14-19, BR-M14-24, BR-M05-26, BR-M05-30, BR-M05-31 | Hòa cả điểm/thời điểm đăng, các bài cùng thời điểm ở tab thời gian, giao tiếp giữ kết quả M05 khi danh mục/thứ tự thay đổi. | SC001–005/UC004. Fixture dùng thời điểm phân biệt hoặc tie-break đã có, M05 cung cấp danh sách ổn định trong các đường Topic/Tag. Cơ chế bảo toàn kết quả khi có thay đổi cần làm rõ. |
| GAP-SC-M14-003 | NOTE-M14-03 | FR-M14-04.06, FR-M14-05.04, FR-M14-08.03, FR-M14-08.05, FR-M14-08.07, BR-M14-17, BR-M14-18 | Mốc bài mới khi ban đầu rỗng, bài cùng thời điểm, khôi phục/quan hệ đổi với bài cũ, tập mới rỗng trước click hoặc có bài tới trong lúc chèn. | SC003/004/006 và AUT002. Đường chèn dùng mốc O01 rõ, ít nhất một bài mới hợp lệ và dữ liệu ổn định trong call. Tập thay đổi trước click có đường loại bớt nhưng còn kết quả, các giao nhau còn lại cần nguồn. |
| GAP-SC-M14-004 | NOTE-M14-04 | FR-M14-01.05, FR-M14-01.06, FR-M14-04.10, BR-M14-15, FR-M01-13.05, BR-M01-41, BR-M11-17, BR-M12-27 | Phạm vi quyền staff đọc tác giả DEACTIVATED/danh tính ẩn danh trên feed chung và nhãn ban khi tác giả chỉ được hiện Ẩn danh. | UC003, các SC có bài và đường staff. Ví dụ staff dùng bài thường đủ quyền, Member thường dùng Ẩn danh, ban dùng tác giả hiện tên. Trường hợp giao nhau cần xác nhận phạm vi áp dụng. |
| GAP-SC-M14-005 | NOTE-M14-05 | FR-M14-03.03, FR-M14-03.15, FR-M14-08.01, FR-M14-08.06, BR-M14-16, BR-M14-18 | Lỗi tính/polling/tải/chèn, nhấp đồng thời, dữ liệu hoặc tư cách đổi trong lúc lấy trang, cách bảo đảm khi thất bại. | AUT001/002, SC001–006. Giữ deadline 15–30 phút/30 phút/60 giây và yêu cầu quyền hiện tại/bảo toàn danh sách. Bảo đảm khi lỗi/đồng thời cần hợp đồng bổ sung. |
| GAP-SC-M14-006 | NOTE-M14-06 | FR-M14-03.05, FR-M14-03.12, FR-M14-02.11, BR-M14-11, BR-M14-19 | Bài vượt 28 ngày trong lượt Trending đang giữ kết quả từ lần tính cũ. | SC001/AUT001. Biên tuổi áp tại mỗi lần tính theo nguồn. Fixture D45 cách xa biên, D-AGE kiểm kết quả hai lần tính, ưu tiên phục vụ trong lượt kéo dài cần làm rõ. |


TBD-M14-01 đã đóng, bookmark được tính trọng số 1. TBD-M14-02/OPEN-006 về SSR/SEO và xem trước chia sẻ ở MS1 giữ trạng thái hoãn mức Thấp theo nguồn. Bốn bước skill hoàn tất, tài liệu Đang soạn, sáu GAP còn mở được trình bày theo phạm vi ảnh hưởng. [QA-M14.md](QA-M14.md)
