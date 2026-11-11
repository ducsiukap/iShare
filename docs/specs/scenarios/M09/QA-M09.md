# QA-M09 — Tái kiểm sau khắc phục

[Vietnamese Doc] — 11/11/2026, skill scenarios v1.4. Trạng thái Đang soạn theo nguồn nghiệp vụ.

## Kết quả hiện hành

| Kiểm tra | Kết quả |
| --- | --- |
| Validator chuẩn | PASS 15 UC, 6 BF, 6 SC, 155 nhánh E |
| Chuẩn hóa biến thể | 30 nhánh từ ID V lịch sử đã đăng ký E tại M1, bảng chuyển đổi ở cuối SC |
| Bảo toàn nội dung | 497 bước main/E/V lịch sử được đối chiếu trước/sau, chỉ đổi ID nhánh, vị trí dẫn và dữ liệu đã xác nhận trong QA-SC-02/03 |
| Phạm vi kiểm máy | Actor/nguồn, guard đăng ký, điểm thay/điểm vào, đích bước, luân phiên, khả năng kết thúc và hậu điều kiện của toàn bộ main/E |
| GAP và phê duyệt | Các GAP nguồn còn mở được liệt kê trong SC và báo cáo tái kiểm toàn bộ, đầu ra giữ Đang soạn |


Bản hiện hành [SC-M09.md](SC-M09.md). Kết quả toàn bộ và các quyết định còn chờ ở [báo cáo khắc phục](../QA-M01-M16-2026-11-11-khac-phuc.md).

## Bằng chứng lần soạn trước

Phần dưới lưu báo cáo của chính module này trước ngày chuyển đổi. Các số E/V và nhận xét giới hạn validator trong phần lịch sử phản ánh công cụ lúc soạn. Số liệu và kết quả áp dụng hiện tại nằm ở mục Kết quả hiện hành, các biến thể đã được kiểm bằng hợp đồng E.

# Kiểm tra scenario — M09 Appeal

[Vietnamese Doc] — 2026-11-10 — Skill scenarios v1.3 — Đang soạn.

Tài liệu chính: [SC-M09.md](SC-M09.md).

| Hạng mục | Kết quả |
|---|---|
| UC/mapping | 3 chính + 12 con = 15 UC, 12 mapping; 17 quan hệ (13 include, 4 generalization), không extend/extension point |
| Disposition | 6 scenario, 7 embedded, 1 aggregate, 1 abstract |
| BF/SC | 6 chức năng actor hoàn chỉnh; không BF chỉ SYSTEM lật xử lý |
| Nhánh E | 125 |
| Đường actor V | 30 |
| Hành vi nền | 3 AUT + 4 RULE, không tính BF/SC |
| Mã nguồn | 7 nhóm + 83 FR chi tiết + 29 BR = 119 hiệu lực; 2 mã bỏ riêng |
| SVG nguồn | 4 SVG parse XML, tập UC khớp US; không sửa/render mới |
| Baseline | 12 nguồn có SHA-256, FR-M09 1.2 Đã chốt khớp byte bản làm việc; US/overview Chờ duyệt |
| GAP | 4 điểm từ NOTE01–04; NOTE05/TBD01 đã đối chiếu/đã đóng, snapshot nội dung MS1 không làm |

## Chức năng đã triển khai

| SC | UC owner | Mục tiêu |
|---|---|---|
| [SC-M09-001](SC-M09.md#sc-m09-001) | UC-M09-001 | Gửi khiếu nại về một lần xử lý của mình |
| [SC-M09-002](SC-M09.md#sc-m09-002) | UC-M09-002 | Xem hồ sơ khiếu nại và nội dung liên quan của mình |
| [SC-M09-003](SC-M09.md#sc-m09-003) | UC-M09-004 | Tra cứu hàng chờ và căn cứ của một khiếu nại |
| [SC-M09-004](SC-M09.md#sc-m09-004) | UC-M09-005 | Nhận quyền xử lý duy nhất một khiếu nại |
| [SC-M09-005](SC-M09.md#sc-m09-005) | UC-M09-021 | Giải quyết hoàn chỉnh một khiếu nại |
| [SC-M09-006](SC-M09.md#sc-m09-006) | UC-M09-006 | Kết luận một khiếu nại đang giữ và thi hành hệ quả |

UC005 có END nhận quyền và UC006 có END kết luận riêng trong US; SC004/006 triển khai đến kết quả đó. SC005 giải quyết toàn hồ sơ vẫn mở đủ nhận–điều tra–kết luận–hệ quả, không dừng ở nhận hoặc gọi ca lật. UC009–012 chỉ chạy từ Chấp nhận/caller liên kết, không có actor tự gọi lật; giữ embedded cùng contract abstract core022, không tạo bốn BF thuần SYSTEM hoặc đếm lặp theo loại xử lý.

## Kiểm tra đã thực hiện

Validator skill PASS cho metadata/sáu phần, actor/sourceID, UC/mapping/BF, bước thay thế/đích, luân phiên và khả năng tới terminal có hậu điều kiện. Main bắt đầu đúng actor chính, kết thúc SYSTEM/SUCCESS của mục tiêu. Từ chối khiếu nại có lý do là hoàn tất quyết định (SUCCESS), khác hệ thống từ chối yêu cầu sai quyền/thiếu dữ liệu (REJECTED).

Đường V được kiểm riêng actor khởi tạo/tập subject, thứ tự, luân phiên, SYSTEM kết thúc và hậu điều kiện; graph validator mặc định chỉ duyệt main/E. Sources V vẫn được đối chiếu. V email triển khai cả đăng nhập rồi gửi đến tiếp nhận, gồm sai mật khẩu sửa đúng, hết hạn, sai người và tài khoản không đăng nhập được; ACT001→ACT002 là cùng Lan sau xác thực, không đổi người. Admin có đường tự xét và xét người từng Mod, không mượn lệnh cấm tự xử lý M08.

Đã đối soát 119 mã hiệu lực và 2 mã bỏ, 4 SVG, baseline FR chính thức/bản làm việc, hash nguồn và liên kết/anchor hai đầu ra. PASS cấu trúc không thay review nghiệp vụ, chứng minh lỗi liên module hoặc phê duyệt stakeholder.

Lệnh thực tế từ repo root:

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M09/SC-M09.md --fr docs/specs/fr/FR-M09.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M03.md --fr docs/specs/fr/FR-M04.md --fr docs/specs/fr/FR-M07.md --fr docs/specs/fr/FR-M08.md --fr docs/specs/fr/FR-M10.md --fr docs/specs/fr/FR-M11.md --fr docs/specs/fr/FR-M12.md --fr docs/specs/fr/FR-M13.md --us docs/specs/us/US-M09.md
```

## Đối soát nghiệp vụ

| Phép kiểm | Kết quả |
|---|---|
| Gửi | Đúng chủ/whitelist/lối vào; lời giải thích, 3 ảnh ≤5MB; lỗi sửa rồi kiểm lại; một lần mỗi xử lý, gộp cả hai, không rút/sửa/gửi lại |
| Hạn | Từ chính lần xử lý, warning giữ 7/10/15 theo mức lần đó; ban tạm 30/90, vĩnh viễn 90, bài gỡ 30, AI không warning 3; đủ N×24h, đúng hạn từ chối |
| Đọc | Chính chủ chỉ đọc, không dữ liệu tố cáo; staff đọc không cần giữ, retained content và log AI đúng hồ sơ, không snapshot mới hoặc gọi AI |
| Hàng chờ/quyền | Ban→Warning→Bài, cùng loại gửi trước trước, lọc; Mod cấm tự xét/role lịch sử Mod, Admin được tự xét; không escalation riêng |
| Giữ | Một người giữ, 30 phút từ mở xem/kết luận của chính người giữ; người khác không gia hạn; mất quyền từ chối hoặc nhận lại hợp lệ trước gửi lại kết luận |
| Ban | Bị lật/giữ record/loại lịch sử; chính ban còn hiệu lực ACTIVE, ban cũ không gỡ ban mới; không khôi phục Mod |
| Cảnh cáo | Giảm số lần hiện tại sàn 0, tính mức/áp hạn chế, giữ hạn; 6→5 vẫn HEAVY, 0 giữ 0; đã Bị lật no-op, Đã bỏ còn GAP002 |
| Bài gỡ | Đổi kiểm duyệt đúng lần gỡ, giữ xóa/Tự ẩn, hoàn đúng 5 điểm đã trừ được ghi nhận thay vì tính lại vote; lật từng chế tài cùng lần đủ quyền, không lật record đã Từ chối riêng hoặc lặp Bị lật |
| AI từ chối | Chưa gửi lại: ngoài nhóm đăng ngay, nhóm qua cổng bật/tắt/Owner; đã gửi lại giữ trạng thái/lần mới; lật đúng warning cùng lần nếu có; không quét kiểm duyệt lại |
| Kết luận/kênh | Hai lựa chọn đều cần lý do; Từ chối giữ nguyên cả bài/warning gộp. Ban app+email, warning/post app; M07 giao, không hứa thiết bị nhận, không AI quyết |
| Tổ hợp | BANNED chỉ gửi ban; post gửi sau gỡ ban khi ACTIVE; hồ sơ gửi trong hạn xét sau hết/gỡ/decay; hai hồ sơ liên kết có thể kết luận khác nhưng tác động mỗi record một lần |

## Phần còn thiếu hợp đồng

| GAP | Giới hạn |
|---|---|
| GAP-SC-M09-001 | Lối vào và phạm vi chỉ đọc hồ sơ ban đã gửi khi người gửi vẫn BANNED chưa rõ so với màn khóa M01. Đã viết BANNED gửi chính ban và kết quả Ban app+email; xem hồ sơ chuẩn dùng ACTIVE. Không thêm portal/lịch sử rộng hoặc gán một phản ứng từ chối mới cho phần nguồn còn thiếu. |
| GAP-SC-M09-002 | Warning đã Đã bỏ do staff override AI trước khi hồ sơ Chờ xét được Chấp nhận: M08 đã giảm, M09 chưa chốt có giảm nữa/no-op/đổi record thế nào. Không tự chọn; ca known dùng Đang tính hoặc đã Bị lật theo BR29. Số lần hiện 0 vì decay có sàn 0 rõ, đã viết, khác warning Đã bỏ. |
| GAP-SC-M09-003 | Chưa có hợp đồng lỗi giữa lưu kết luận, lật record, hoàn điểm, trạng thái bài/account và phát kết quả. Scenario triển khai kết quả chức năng khi các phần thành công; không thêm transaction/outbox/rollback/retry, không coi kết luận đã lưu nhưng hệ quả lỗi là thành công trọn mục tiêu. Cần hợp đồng lỗi/thiết kế để hoàn thiện đường lỗi này. |
| GAP-SC-M09-004 | Bài còn lần gỡ khác hiệu lực hoặc nhóm đã khóa/ẩn/mất điều kiện khi xét chưa có quy tắc phối hợp đầy đủ M09–M03–M11. Đường hợp lệ giữ đúng một lần xử lý, lớp xóa/Tự ẩn, lần gửi lại và cổng nhóm đang hoạt động/đủ quyền. Không tự ghi đè lần gỡ khác, phát công khai hoặc vượt khóa/ẩn; các tổ hợp chồng này chưa thể nhận đã khép. |

Bốn GAP không được thay bằng từ chối, hủy hay chuyển giao giả. NOTE05 dùng ngoại lệ Admin chi tiết; TBD01 comment vẫn ẩn đã đóng; K-01 snapshot nội dung không làm MS1. Không tự chọn giao dịch/rollback/retry, mở portal BANNED, giảm thêm warning Đã bỏ hoặc vượt trạng thái/lần gỡ chồng/cổng nhóm. Toàn bộ hành vi đủ căn cứ đã được triển khai/đối chiếu trong scope; các phần thiếu nêu rõ, chưa nhận đã chốt toàn bộ M09.
