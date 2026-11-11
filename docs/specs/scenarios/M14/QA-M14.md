# QA — M14 Feed & Discovery

[Vietnamese Doc] — 11/11/2026 — Skill scenarios v1.3.

[SC-M14.md](SC-M14.md) đang Đang soạn. FR-M14 v1.1 Đã chốt, US-M14/overview Chờ duyệt. Sáu GAP còn mở từ NOTE nguồn. TBD SSR/SEO giữ trạng thái hoãn mức Thấp, TBD bookmark đã đóng và trọng số 1 được áp dụng.

## Kết quả kiểm tra

| Hạng mục | Phương pháp | Kết quả thực tế |
|---|---|---|
| Mô hình đầu vào | Đọc FR/US, đối chiếu catalog/decomposition/relations và SVG | 9 UC, 13 mapping, 7 include, 5 SVG khớp tập UC |
| Nguồn | Trích định nghĩa trước Phụ lục A và loại mã đã bỏ | 104 mã hiệu lực =8 nhóm+72 FR chi tiết+24 BR, đủ vị trí. FR-M14-04.08 đã bỏ, dùng FR-M14-04.13 |
| M/E | Validator của skill trên nội dung xuất bản | {'use_cases': 9, 'flows': 6, 'scenarios': 6, 'exceptions': 44}, PASS cấu trúc |
| V | Đọc bảng đã render, kiểm actor bắt đầu, chủ thể, luân phiên, next và hậu điều kiện | 27 đường, 78 bước, PASS |
| BF | Walkthrough từ hành động actor tới danh sách/nhận toàn bộ bài mới | 6 BF/6 SC, 6 UC sở hữu SC, 2 embedded, 1 aggregate |
| Dữ liệu | Python tính lại công thức, tập theo tab, thứ tự, chia trang, thời gian | D45 20+20+5, Topic/Tag20+3, P21 từ vị trí21 ở K0 lên5 ở K1. D-SET Following8/Group4/Newest6. Banner30 thêm đủ30, O35 giữ chỗ đọc |
| AUT/RULE | Đối chiếu 2 AUT/6 RULE và lớp dữ liệu | Chu kỳ 15–30 phút, tương tác vào batch trong30 phút, polling cách≤60 giây và banner≤60 giây, tuổi liên tục/biên28, U/C/B hiệu lực |
| Liên kết/baseline | Kiểm đích file/anchor và hash từng dòng baseline trên hai file đã ghi | PASS, 39 liên kết, 14 nguồn và 28 ô SHA-256, FR chính thức khớp bản làm việc chung |
| Đối soát đầu ra | Đọc lại bảng Markdown đã ghi và tính độc lập tập/thứ tự/điểm/số lượng | 45 dòng điểm, 21 dòng điều kiện bài, 48 dòng kết quả phân trang và 15 dòng kết quả chèn banner đạt kiểm tra dữ liệu |
| Ngữ nghĩa owner | Đọc phần liên quan của 11 FR giao tiếp | Phạm vi bài, ẩn danh, cờ Group/Gamification, ngoại lệ ADMIN, lối tìm kiếm/danh sách nhóm được truy vết |
| Giới hạn | Đối chiếu NOTE-M14-01 đến NOTE-M14-06 | Các đường đủ hợp đồng đã triển khai. Khởi tạo/rỗng/lỗi/đồng thời/khóa phụ/giao tiếp M05/quyền staff/tuổi trong lượt kéo dài tiếp tục theo GAP |


## Lệnh kiểm tra

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M14/SC-M14.md --fr docs/specs/fr/FR-M14.md --us docs/specs/us/US-M14.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M02.md --fr docs/specs/fr/FR-M03.md --fr docs/specs/fr/FR-M04.md --fr docs/specs/fr/FR-M05.md --fr docs/specs/fr/FR-M06.md --fr docs/specs/fr/FR-M07.md --fr docs/specs/fr/FR-M08.md --fr docs/specs/fr/FR-M10.md --fr docs/specs/fr/FR-M11.md --fr docs/specs/fr/FR-M12.md
```

## Các quyết định triển khai cần review

Tách 6 mục tiêu actor theo dữ liệu và trigger nghiệp vụ. Topic/Tag là một SC với hai lựa chọn, cuộn là phần của hành trình đọc. UC005 có một SC dùng chung ba tab thời gian. Tính Trending và phát hiện bài mới được triển khai ở AUT/RULE, có dữ liệu đối soát riêng. Mở trang chủ nằm trong Trending mặc định.

Dữ liệu hoàn toàn giả lập. Fixture có kết quả đã tính và danh mục ổn định cho các đường phục vụ thành công, các trường hợp khởi tạo hoặc danh mục thay đổi nằm tại GAP001/002. Ví dụ staff dùng bài thường đủ quyền, điều kiện giao nhau với ẩn danh/DEACTIVATED còn ở GAP004. Tập mới của banner ổn định trong call và còn phần tử hợp lệ, các tình huống khác nằm tại GAP003/005. Các nhánh chuyển sang M06/M11 được ghi HANDED_OFF khi actor chọn mục tiêu tiếp theo từ trạng thái rỗng.

| GAP | Nguồn | Phạm vi |
|---|---|---|
| GAP-SC-M14-001 | NOTE-M14-01 | Kết quả trước lần tính Trending đầu tiên, cách trình bày rỗng Trending/Newest/Topic/Tag, lỗi dữ liệu/tải và con trỏ mất hiệu lực. |
| GAP-SC-M14-002 | NOTE-M14-02 | Hòa cả điểm/thời điểm đăng, các bài cùng thời điểm ở tab thời gian, giao tiếp giữ kết quả M05 khi danh mục/thứ tự thay đổi. |
| GAP-SC-M14-003 | NOTE-M14-03 | Mốc bài mới khi ban đầu rỗng, bài cùng thời điểm, khôi phục/quan hệ đổi với bài cũ, tập mới rỗng trước click hoặc có bài tới trong lúc chèn. |
| GAP-SC-M14-004 | NOTE-M14-04 | Phạm vi quyền staff đọc tác giả DEACTIVATED/danh tính ẩn danh trên feed chung và nhãn ban khi tác giả chỉ được hiện Ẩn danh. |
| GAP-SC-M14-005 | NOTE-M14-05 | Lỗi tính/polling/tải/chèn, nhấp đồng thời, dữ liệu hoặc tư cách đổi trong lúc lấy trang, cách bảo đảm khi thất bại. |
| GAP-SC-M14-006 | NOTE-M14-06 | Bài vượt 28 ngày trong lượt Trending đang giữ kết quả từ lần tính cũ. |


## Baseline

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


SHA-256 được tính từ byte nguồn. Kiểm cấu trúc xác nhận hợp đồng máy kiểm, phần ngữ nghĩa được đối chiếu theo FR/US và từng dữ liệu minh họa. Trạng thái phê duyệt tiếp tục theo metadata của SC.
