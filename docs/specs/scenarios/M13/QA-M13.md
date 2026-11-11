# QA-M13 — Tái kiểm sau khắc phục

[Vietnamese Doc] — 11/11/2026, skill scenarios v1.4. Trạng thái Đang soạn theo nguồn nghiệp vụ.

## Kết quả hiện hành

| Kiểm tra | Kết quả |
| --- | --- |
| Validator chuẩn | PASS 15 UC, 8 BF, 8 SC, 153 nhánh E |
| Chuẩn hóa biến thể | 30 nhánh từ ID V lịch sử đã đăng ký E tại M1, bảng chuyển đổi ở cuối SC |
| Bảo toàn nội dung | 466 bước main/E/V lịch sử được đối chiếu trước/sau, chỉ đổi ID nhánh, vị trí dẫn và dữ liệu đã xác nhận trong QA-SC-02/03 |
| Phạm vi kiểm máy | Actor/nguồn, guard đăng ký, điểm thay/điểm vào, đích bước, luân phiên, khả năng kết thúc và hậu điều kiện của toàn bộ main/E |
| GAP và phê duyệt | Các GAP nguồn còn mở được liệt kê trong SC và báo cáo tái kiểm toàn bộ, đầu ra giữ Đang soạn |


Bản hiện hành [SC-M13.md](SC-M13.md). Kết quả toàn bộ và các quyết định còn chờ ở [báo cáo khắc phục](../QA-M01-M16-2026-11-11-khac-phuc.md).

## Bằng chứng lần soạn trước

Phần dưới lưu báo cáo của chính module này trước ngày chuyển đổi. Các số E/V và nhận xét giới hạn validator trong phần lịch sử phản ánh công cụ lúc soạn. Số liệu và kết quả áp dụng hiện tại nằm ở mục Kết quả hiện hành, các biến thể đã được kiểm bằng hợp đồng E.

# QA — M13 AI Layer

[Vietnamese Doc] — 11/11/2026 — Skill scenarios v1.3.

[SC-M13.md](SC-M13.md) mang trạng thái Đang soạn. FR-M13 v1.3 Đã chốt, US-M13/overview Chờ duyệt. Sáu GAP nguồn còn mở theo phạm vi nêu trong SC, TBD ngân sách hoãn mức Thấp.

## Phạm vi và kết quả

| Hạng mục | Phương pháp kiểm | Kết quả thực tế |
|---|---|---|
| Mô hình đầu vào | Đối chiếu catalog, decomposition, relations và tập UC của SVG | 15 UC, 13 mapping, 8 include, 6 SVG khớp thành viên US |
| Nguồn hiệu lực | Trích định nghĩa trước Phụ lục A, đối chiếu trace từng mã | 124 mã = 10 nhóm + 85 FR chi tiết + 29 BR, đủ vị trí đối soát, 0 mã bỏ |
| Cấu trúc và đồ thị M/E | Validator của skill chạy trên nội dung xuất bản | {'use_cases': 15, 'flows': 8, 'scenarios': 8, 'exceptions': 123}, PASS |
| Đường V | Đọc lại bảng đã render, kiểm actor mở đầu, chủ thể đơn, luân phiên, next, SYSTEM kết thúc và hậu điều kiện | 30 đường, 82 bước, PASS |
| Mục tiêu BF | Walkthrough actor khởi tạo đến kết quả caller | 8 BF/8 SC, có đủ actor/SYSTEM, kết thúc chức năng tại caller |
| UC hỗ trợ | Đối chiếu 7 embedded với vị trí M thực tế, UC003 với AUT001/002 | 6 UC sở hữu SC, 7 embedded, 1 aggregate, 1 background |
| Hành vi nền | Đọc 4 AUT, 6 RULE và BG-M13-COMMENT, đối soát bộ dữ liệu | Quét bình luận, vector/hàng bù, log, cache và phản hồi có trigger/đầu ra/nguồn |
| Dữ liệu tính toán | Python tính độc lập word count, tỷ lệ, mốc ngày, TTL và điểm tìm kiếm | 368 từ chuẩn, 299/300 biên. Tỷ lệ 8/13, 5/6, 6/8, 7/12. TTL 24 giờ. Điểm tìm 0,72/0,56 hoặc 0,80/0,80 |
| Ngữ nghĩa caller | Đọc M03/M05/M06/M08/M09/M10/M11/M15/M16 và username M01 | Quét mới khác quét lại, Owner khác thành viên, ADMIN miễn quét, log giới hạn M09, tỷ lệ giới hạn ADMIN |
| Liên kết và baseline | Đọc hai file đã ghi, kiểm đích liên kết/anchor và SHA-256 từng dòng baseline | 40 liên kết hợp lệ, 26 ô SHA-256 khớp 13 nguồn |
| Giới hạn kiểm tra | Đối chiếu 6 NOTE và TBD nguồn | PASS cấu trúc chỉ xác nhận hợp đồng máy kiểm. Các tình huống GAP còn mở tiếp tục cần quyết định nghiệp vụ |


## Lệnh validator

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M13/SC-M13.md --fr docs/specs/fr/FR-M13.md --us docs/specs/us/US-M13.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M03.md --fr docs/specs/fr/FR-M05.md --fr docs/specs/fr/FR-M06.md --fr docs/specs/fr/FR-M08.md --fr docs/specs/fr/FR-M09.md --fr docs/specs/fr/FR-M10.md --fr docs/specs/fr/FR-M11.md --fr docs/specs/fr/FR-M15.md --fr docs/specs/fr/FR-M16.md
```

## Các quyết định triển khai cần review

Ba mục tiêu tác giả qua M03 được đặt trong UC020 đã có. M06 và M05 được triển khai inline đến danh sách tìm kiếm và lựa chọn Topic trên bản soạn. UC010 dùng hành trình Admin mở/đổi lọc tại M15. UC003 và quét bình luận theo kích hoạt M08 được triển khai tại AUT/RULE và dữ liệu đối soát. Các quyết định này áp dụng phép kiểm luồng actor hoàn chỉnh của skill.

Dữ liệu đều giả lập. P-TOPIC đã có định danh để làm rõ log của đường có đủ căn cứ, bản soạn chưa có định danh tiếp tục là GAP006. Các call trong đường chuẩn dùng nội dung/quyền/cờ ổn định, các tổ hợp thay đổi trong call tiếp tục ở GAP002/003/005. Các giá trị phần trăm làm tròn chỉ nhằm đọc ví dụ.

| GAP | Nguồn | Phạm vi |
|---|---|---|
| GAP-SC-M13-001 | NOTE-M13-01 | Đầu ra AI thiếu điểm, sai kiểu/range, vector/Topic/tóm tắt sai hợp đồng hoặc transport thành công nhưng raw chưa dùng được. |
| GAP-SC-M13-002 | NOTE-M13-02 | Sửa bài trong lúc tạo embedding/tóm tắt, hai cache miss đồng thời, cách dùng vector cũ khi bản hiện tại còn thiếu. |
| GAP-SC-M13-003 | NOTE-M13-03 | Cờ đổi giữa hai attempts/giữa kiểm và trả cache, phản hồi muộn, quyền đọc đổi lúc đang chờ. |
| GAP-SC-M13-004 | NOTE-M13-04 | Tập phản hồi có bản ghi nhưng tổng số Topic gợi ý bằng 0. |
| GAP-SC-M13-005 | NOTE-M13-05 | Cadence/ưu tiên tạo bù, mục chờ có bài đổi trạng thái, cờ hoặc AI đổi trong khi bù. |
| GAP-SC-M13-006 | NOTE-M13-06 | Liên kết log với bản soạn chưa có định danh bền và loại log khi cờ chặn trước outbound. |


## Baseline

| Nguồn từ repo root | Version | Ngày | Trạng thái | SHA-256 |
|---|---|---|---|---|
| [docs/specs/fr/FR-M13.md](../../fr/FR-M13.md) | 1.3 | 2026-10-24 | Đã chốt | 54630715cc1e391b9ea361247784af26200fc2f01c1b1da96ea56ed1f75f9982 |
| [docs/specs/us/US-M13.md](../../us/US-M13.md) | US chưa ghi version tài liệu | 2026-11-02 | Chờ duyệt | ab7f1efb8e3fcb725bf83defa29a2e28967520f4c685d57c72322bd84c3b231a |
| [docs/specs/us/US-overview.md](../../us/US-overview.md) | 1.1 | 2026-11-02 | Chờ duyệt | c1d624b7036ea2c7a9968eaa46c482c04fa1a15e2554d536cdfc12f177e26e33 |
| [docs/specs/fr/FR-M01.md](../../fr/FR-M01.md) | 1.10 | 2026-10-24 | Đã chốt | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a |
| [docs/specs/fr/FR-M03.md](../../fr/FR-M03.md) | 1.10 | 2026-10-24 | Đã chốt | fc996ec5520b6485277fca6a3dbae018bfce02263aba8e15ea87871f35865980 |
| [docs/specs/fr/FR-M05.md](../../fr/FR-M05.md) | 1.7 | 2026-10-24 | Đã chốt | eb85b5dcb56995d791ed28a8d72a2f91c95588d8cd8d4fb1e74a8aabc2d701aa |
| [docs/specs/fr/FR-M06.md](../../fr/FR-M06.md) | 1.5 | 2026-10-24 | Đã chốt | 63606046efb11356276a2c9180f53cadad76f83e2e86502ed00341d915e0b084 |
| [docs/specs/fr/FR-M08.md](../../fr/FR-M08.md) | 1.7 | 2026-10-24 | Đã chốt | a92e6e370038af300a9ddd735414dcb2c4fbffe07c81abaaa3c92dff447c25f0 |
| [docs/specs/fr/FR-M09.md](../../fr/FR-M09.md) | 1.2 | 2026-10-24 | Đã chốt | 8ad8ae5e148c6e446f4bfec7f6e74ba9566c54747a0eda37a3930e94ab96faea |
| [docs/specs/fr/FR-M10.md](../../fr/FR-M10.md) | 1.4 | 2026-10-24 | Đã chốt | 3e1010a76db6ef4c5870f42765e669095efc8d38c202271d9b200d2da0823d2c |
| [docs/specs/fr/FR-M11.md](../../fr/FR-M11.md) | 1.3 | 2026-10-24 | Đã chốt | 1908d300f75d5f7fa0fd5b31b1d375bc6a63ccd42da254de6e9d0d7d9ef16307 |
| [docs/specs/fr/FR-M15.md](../../fr/FR-M15.md) | 1.1 | 2026-10-24 | Đã chốt | a35e509a64d314b76ddb49a2c077b360e6a70dd6366123b7900917f19780d3a1 |
| [docs/specs/fr/FR-M16.md](../../fr/FR-M16.md) | 1.0 | 2026-10-24 | Đã chốt | c8ef96e52479806637b0eac334bbe57fa9fe4f73bdacc73913467960050f0671 |


SHA-256 được tính từ byte nguồn đọc khi tạo tài liệu. FR-M13 chính thức khớp bản làm việc chung. Kiểm liên kết, anchor, đường V và hash được thực hiện trên cả SC và QA đã ghi. Kết quả cuối gồm 40 liên kết hợp lệ, 26 ô SHA-256 khớp 13 nguồn, 30 đường V và 82 bước V đạt kiểm tra độc lập.
