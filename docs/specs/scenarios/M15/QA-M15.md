# QA-M15 — Tái kiểm sau khắc phục

[Vietnamese Doc] — 11/11/2026, skill scenarios v1.4. Trạng thái Đang soạn theo nguồn nghiệp vụ.

## Kết quả hiện hành

| Kiểm tra | Kết quả |
| --- | --- |
| Validator chuẩn | PASS 11 UC, 3 BF, 3 SC, 38 nhánh E |
| Chuẩn hóa biến thể | 10 nhánh từ ID V lịch sử đã đăng ký E tại M1, bảng chuyển đổi ở cuối SC |
| Bảo toàn nội dung | 77 bước main/E/V lịch sử được đối chiếu trước/sau, chỉ đổi ID nhánh, vị trí dẫn và dữ liệu đã xác nhận trong QA-SC-02/03 |
| Phạm vi kiểm máy | Actor/nguồn, guard đăng ký, điểm thay/điểm vào, đích bước, luân phiên, khả năng kết thúc và hậu điều kiện của toàn bộ main/E |
| GAP và phê duyệt | Các GAP nguồn còn mở được liệt kê trong SC và báo cáo tái kiểm toàn bộ, đầu ra giữ Đang soạn |


Bản hiện hành [SC-M15.md](SC-M15.md). Kết quả toàn bộ và các quyết định còn chờ ở [báo cáo khắc phục](../QA-M01-M16-2026-11-11-khac-phuc.md).

## Bằng chứng lần soạn trước

Phần dưới lưu báo cáo của chính module này trước ngày chuyển đổi. Các số E/V và nhận xét giới hạn validator trong phần lịch sử phản ánh công cụ lúc soạn. Số liệu và kết quả áp dụng hiện tại nằm ở mục Kết quả hiện hành, các biến thể đã được kiểm bằng hợp đồng E.

# QA — M15 Analytics & Stats

[Vietnamese Doc] — 11/11/2026 — Skill scenarios v1.3.

[SC-M15.md](SC-M15.md) Đang soạn. FR-M15 v1.1 Đã chốt, US-M15/overview và hợp đồng tham chiếu M13 Chờ duyệt. Bốn GAP và hai TBD hoãn mức Thấp được giữ đúng nguồn.

## Kết quả kiểm tra

| Hạng mục | Phương pháp | Kết quả thực tế |
|---|---|---|
| Nguồn và mô hình | Đối chiếu FR/US, catalog, decomposition, relations và SVG | 10 UC M15 +1 UC tham chiếu M13, 12 mapping, 12 include, 4 SVG khớp thành viên |
| Phạm vi FR/BR | Trích định nghĩa trước Phụ lục A và đối soát trace | 93 mã M15 =3 nhóm+68 FR chi tiết+22 BR, đủ vị trí, 0 mã bỏ |
| M/E | Validator skill trên nội dung xuất bản | {'use_cases': 11, 'flows': 3, 'scenarios': 3, 'exceptions': 28}, PASS cấu trúc |
| V | Đọc bảng đã render, kiểm actor mở đầu, chủ thể, luân phiên, next và hậu điều kiện | 10 đường, 20 bước, PASS |
| BF | Walkthrough Admin mở/đổi đến đủ số liệu từng trang | 3 BF/3 SC, 3 UC sở hữu SC, 8 embedded, 7 RULE |
| Dữ liệu người dùng | Đếm độc lập theo trạng thái/eligibility và cohort | Toàn thời gian 16 tài khoản, 10 đủ điều kiện ba phân bố. Hôm nay 9, eligible4. A17 làm số hôm nay tăng10 ở lượt 10:01 |
| Dữ liệu nội dung | Tách thời điểm tạo/đăng, kiểm Nháp/Topic/ẩn/xóa và tỷ lệ | Toàn thời gian 15 bài cơ cấu, 13 bài đã đăng theo lịch sử, 10 bình luận. Hôm nay cơ cấu9/bài mới10. Gộp T01 nhận3 bài. Tỷ lệ 8/13,5/6,6/8,7/12 |
| Dữ liệu kiểm duyệt | Đếm từng báo cáo và lịch sử sự kiện, từng khiếu nại | 12 báo cáo/7 vụ, cảnh cáo LIGHT2/MEDIUM4/HEAVY2, ban8 tạm+2 vĩnh, gỡ2, khiếu nại8. V02 xử lý làm báo cáo All 2/4/6 |
| Lưới và biên | Tính từ UTC+7, kiểm hai đầu kỳ và độ hạt | Hôm nay11 cột,7 ngày7 cột,30 ngày30 cột. Ví dụ All9 cột 03…11, mốc thực tế giữ GAP002 |
| Baseline/liên kết | Đọc hai file đã ghi, kiểm file/anchor và SHA-256 | 38 liên kết, 14 nguồn, 28 ô SHA-256, FR chính thức khớp bản làm việc chung |
| Đối soát tệp đầu ra | Đọc lại Markdown và tính độc lập từ từng bảng dữ liệu đã ghi | 87 bản ghi đầu vào, 48 phân bố và 36 chuỗi biểu đồ khớp phép tính độc lập, PASS |
| Giới hạn | Đối chiếu NOTE-M15-01…04 và hai TBD | Thông báo/lỗi/đồng thời, mốc All, dữ liệu lịch sử/nhãn AI, mẫu số 0 còn cần nguồn. Kiểm cấu trúc có phạm vi riêng với review nghiệp vụ |


## Lệnh kiểm tra

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M15/SC-M15.md --fr docs/specs/fr/FR-M15.md --us docs/specs/us/US-M15.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M02.md --fr docs/specs/fr/FR-M03.md --fr docs/specs/fr/FR-M04.md --fr docs/specs/fr/FR-M05.md --fr docs/specs/fr/FR-M08.md --fr docs/specs/fr/FR-M09.md --fr docs/specs/fr/FR-M10.md --fr docs/specs/fr/FR-M11.md --fr docs/specs/fr/FR-M13.md
```

## Quyết định triển khai và dữ liệu cần review

Ba trang là ba mục tiêu độc lập của Admin. Chọn khoảng, chia cột, tổng hợp và tỷ lệ là phần của hành trình nhận số liệu trang. UC-M13-010 được chèn đến kết quả hiển thị và giữ owner M13. Các quy tắc được triển khai trong lượt SYSTEM tính trực tiếp theo trigger mở/đổi.

D-U/D-C/D-M là ba bộ dữ liệu giả lập độc lập. D-CALENDAR dùng ví dụ đã biết mốc 03/2026 để diễn đạt lưới tháng, mốc thực tế và All rỗng giữ GAP002. D-M cung cấp mức đạt ngay sau cảnh cáo, thời điểm gỡ và nhãn lý do AI để minh họa phép đếm, giao tiếp owner giữ GAP003. Các đường chuẩn giả lập dữ liệu ổn định trong lượt, thay đổi trước lượt có nhánh tính lại, giao nhau trong lượt giữ GAP001.

| GAP | Nguồn | Phạm vi |
|---|---|---|
| GAP-SC-M15-001 | NOTE-M15-01 | Nội dung thông báo/đích chuyển khi từ chối, lỗi hoặc kết quả một phần, quyền/dữ liệu đổi giữa các phép đếm trong cùng lượt. |
| GAP-SC-M15-002 | NOTE-M15-02 | Mốc đầu lưới tháng Toàn thời gian khi triển khai hoặc toàn hệ thống chưa có dữ liệu. |
| GAP-SC-M15-003 | NOTE-M15-03 | Giao tiếp mức đạt ngay sau cảnh cáo, thời điểm gỡ thủ công kể cả về sau ban bị lật, chuẩn hóa nhóm AI sang nhãn lý do theo loại. |
| GAP-SC-M15-004 | NOTE-M15-04 / NOTE-M13-04 | Có phản hồi trong khoảng nhưng tổng số Topic gợi ý bằng 0. |


## Baseline

| Nguồn từ repo root | Version | Ngày | Trạng thái | SHA-256 |
|---|---|---|---|---|
| [docs/specs/fr/FR-M15.md](../../fr/FR-M15.md) | 1.1 | 2026-10-24 | Đã chốt | a35e509a64d314b76ddb49a2c077b360e6a70dd6366123b7900917f19780d3a1 |
| [docs/specs/us/US-M15.md](../../us/US-M15.md) | US chưa ghi version tài liệu | 2026-11-02 | Chờ duyệt | 7f861bd4f533d75062c5fcb82485fb0668ecb153d8383853758c3c86c712f16d |
| [docs/specs/us/US-overview.md](../../us/US-overview.md) | 1.1 | 2026-11-02 | Chờ duyệt | c1d624b7036ea2c7a9968eaa46c482c04fa1a15e2554d536cdfc12f177e26e33 |
| [docs/specs/us/US-M13.md](../../us/US-M13.md) | US chưa ghi version tài liệu | 2026-11-02 | Chờ duyệt | ab7f1efb8e3fcb725bf83defa29a2e28967520f4c685d57c72322bd84c3b231a |
| [docs/specs/fr/FR-M01.md](../../fr/FR-M01.md) | 1.10 | 2026-10-24 | Đã chốt | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a |
| [docs/specs/fr/FR-M02.md](../../fr/FR-M02.md) | 1.6 | 2026-10-24 | Đã chốt | e86aca71e0415ee2e121a4fdc3628261be335e9d266fcf6e9654b2fdf3cd357e |
| [docs/specs/fr/FR-M03.md](../../fr/FR-M03.md) | 1.10 | 2026-10-24 | Đã chốt | fc996ec5520b6485277fca6a3dbae018bfce02263aba8e15ea87871f35865980 |
| [docs/specs/fr/FR-M04.md](../../fr/FR-M04.md) | 1.4 | 2026-10-24 | Đã chốt | c2fe0e4f6c4bc6835af27585cb711ac03f9fed516d435e759d20ddd58bfd1039 |
| [docs/specs/fr/FR-M05.md](../../fr/FR-M05.md) | 1.7 | 2026-10-24 | Đã chốt | eb85b5dcb56995d791ed28a8d72a2f91c95588d8cd8d4fb1e74a8aabc2d701aa |
| [docs/specs/fr/FR-M08.md](../../fr/FR-M08.md) | 1.7 | 2026-10-24 | Đã chốt | a92e6e370038af300a9ddd735414dcb2c4fbffe07c81abaaa3c92dff447c25f0 |
| [docs/specs/fr/FR-M09.md](../../fr/FR-M09.md) | 1.2 | 2026-10-24 | Đã chốt | 8ad8ae5e148c6e446f4bfec7f6e74ba9566c54747a0eda37a3930e94ab96faea |
| [docs/specs/fr/FR-M10.md](../../fr/FR-M10.md) | 1.4 | 2026-10-24 | Đã chốt | 3e1010a76db6ef4c5870f42765e669095efc8d38c202271d9b200d2da0823d2c |
| [docs/specs/fr/FR-M11.md](../../fr/FR-M11.md) | 1.3 | 2026-10-24 | Đã chốt | 1908d300f75d5f7fa0fd5b31b1d375bc6a63ccd42da254de6e9d0d7d9ef16307 |
| [docs/specs/fr/FR-M13.md](../../fr/FR-M13.md) | 1.3 | 2026-10-24 | Đã chốt | 54630715cc1e391b9ea361247784af26200fc2f01c1b1da96ea56ed1f75f9982 |


Số liệu minh họa và metadata nguồn được kiểm theo đúng phiên bản đã đọc. Bốn bước skill hoàn tất, phê duyệt theo trạng thái và bằng chứng trong SC.
