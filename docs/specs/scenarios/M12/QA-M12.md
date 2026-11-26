# QA-M12 — Tái kiểm sau khắc phục

[Vietnamese Doc] — 11/11/2026, skill scenarios v1.4. Trạng thái Đang soạn theo nguồn nghiệp vụ.

## Kết quả hiện hành

| Kiểm tra | Kết quả |
| --- | --- |
| Validator chuẩn | PASS 13 UC, 3 BF, 3 SC, 87 nhánh E |
| Chuẩn hóa biến thể | 19 nhánh từ ID V lịch sử đã đăng ký E tại M1, bảng chuyển đổi ở cuối SC |
| Bảo toàn nội dung | 176 bước main/E/V lịch sử được đối chiếu trước/sau, chỉ đổi ID nhánh, vị trí dẫn và dữ liệu đã xác nhận trong QA-SC-02/03 |
| Phạm vi kiểm máy | Actor/nguồn, guard đăng ký, điểm thay/điểm vào, đích bước, luân phiên, khả năng kết thúc và hậu điều kiện của toàn bộ main/E |
| GAP và phê duyệt | Các GAP nguồn còn mở được liệt kê trong SC và báo cáo tái kiểm toàn bộ, đầu ra giữ Đang soạn |


Bản hiện hành [SC-M12.md](SC-M12.md). Kết quả toàn bộ và các quyết định còn chờ ở [báo cáo khắc phục](../QA-M01-M16-2026-11-11-khac-phuc.md).

## Bằng chứng lần soạn trước

Phần dưới lưu báo cáo của chính module này trước ngày chuyển đổi. Các số E/V và nhận xét giới hạn validator trong phần lịch sử phản ánh công cụ lúc soạn. Số liệu và kết quả áp dụng hiện tại nằm ở mục Kết quả hiện hành, các biến thể đã được kiểm bằng hợp đồng E.

# Kiểm tra scenario — M12 Gamification

[Vietnamese Doc] — 2026-11-11 — Skill scenarios v1.3 — Đang soạn.

Tài liệu chính: [SC-M12.md](SC-M12.md).

| Hạng mục | Kết quả |
|---|---|
| UC/mapping | 3 chính+10 con=13 UC,12 mapping,11 include; không extend/generalization UC |
| Disposition | 3 UC sở hữu scenario(020/021/022),10 embedded; giữ level/tier trong US, không tạo mô hình mới |
| BF/SC | 3 chức năng actor hoàn chỉnh; không BF kiểm/ghi/cộng điểm/trao/tính/chốt/nhãn |
| Nhánh E | 68 |
| Đường actor V | 19 đường/38 bước |
| Mã nguồn | 8 nhóm+106 FR chi tiết+29 BR=143 hiệu lực, không mã bỏ |
| Hành vi nền | 6 AUT+6 RULE,13 bộ dữ liệu đối soát D-LOSS |
| Nguồn/SVG | 16 baseline có SHA-256;4 SVG parse/tập UC khớp US; FR chính thức/bản chung khớp byte |
| GAP | 6 điểm từ NOTE01/02/03/04/06/07; NOTE05 đã đối chiếu, không phải GAP mới |

## Chức năng đã triển khai

| SC | UC owner | Mục tiêu |
|---|---|---|
| [SC-M12-001](SC-M12.md#sc-m12-001) | UC-M12-020 | Đánh giá nội dung bằng upvote hoặc rút đánh giá của mình |
| [SC-M12-002](SC-M12.md#sc-m12-002) | UC-M12-021 | Tra cứu bảng xếp hạng theo chu kỳ và Lớp/Khối |
| [SC-M12-003](SC-M12.md#sc-m12-003) | UC-M12-022 | Xem điểm và thành tích được công bố qua hồ sơ |

Upvote/rút cùng hợp đồng bật/tắt, Post/Comment là loại đích/trọng số; không tách BF theo trạng thái. Tab/bộ lọc/cuộn là nhánh đọc bảng;45 dòng đi20+20+5, không dừng ở Top 20. Core022 Summary có hành trình actor xem phần đóng góp qua M02 hiện có; scenario mở phần M12 tới kết quả hiển thị, không tạo UC/trang hồ sơ mới hoặc gọi UC009 như một thao tác người dùng. Tác vụ thuần tự động có trigger/dữ liệu/hậu quả/nguồn ở AUT, không thêm actor scheduler/AI.

## Kiểm tra thực hiện

Validator skill PASS cho metadata/sáu phần, actor/source ID, UC/mapping/BF/coverage, E thay đúng at, luân phiên chủ thể và đường tới terminal có hậu điều kiện. Main bắt đầu actor chính, kết thúc SYSTEM/SUCCESS của chức năng. Rút hợp lệ hoặc tập lọc rỗng trên bảng đã có là SUCCESS, khác từ chối quyền/bảng ngoài scope. Không dựng hủy/lỗi lưu/retry không có nguồn.

V được kiểm riêng người khởi tạo/tập chủ thể, bước/đích tuần tự, luân phiên và SYSTEM kết thúc với result có hậu điều kiện. Graph validator mặc định chỉ duyệt main/E, PASS không tự chứng minh V hoặc ngữ nghĩa. Đã đối chiếu nguồn, dữ liệu, quyền, mốc và tất cả143 mã;4 SVG và link/hash được kiểm trước ghi. Đây là review agent, không phê duyệt stakeholder. Lệnh thực tế từ repo root:

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M12/SC-M12.md --fr docs/specs/fr/FR-M12.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M02.md --fr docs/specs/fr/FR-M03.md --fr docs/specs/fr/FR-M04.md --fr docs/specs/fr/FR-M05.md --fr docs/specs/fr/FR-M06.md --fr docs/specs/fr/FR-M07.md --fr docs/specs/fr/FR-M08.md --fr docs/specs/fr/FR-M09.md --fr docs/specs/fr/FR-M10.md --fr docs/specs/fr/FR-M11.md --fr docs/specs/fr/FR-M14.md --fr docs/specs/fr/FR-M15.md --us docs/specs/us/US-M12.md
```

## Đối soát nghiệp vụ

| Phép kiểm | Kết quả và giới hạn |
|---|---|
| Bật/tắt | Một lượt hiệu lực/người/nội dung, bấm lại rút, bật lại thời điểm mới; count và tổng 2/1 đúng trước/sau, không downvote hoặc nhận/chỉnh điểm tay |
| Quyền | HEAVY vẫn vote; BANNED chịu M01; không self-vote/Guest. Khóa toàn bộ chặn mới/rút bài+bình luận, nhóm Private/Khóa/cờ Group vẫn kiểm; ADMIN không bypass |
| Badge/điểm | Tức thời khác batch60 phút;5 mốc đúng, vượt nhiều trao tất cả chưa có/ngày đầu; giảm điểm giữ badge; không nguồn điểm khác/progress/thu hồi, DELETED không hiện badge |
| Trừ/hoàn | D-LOSS13 bộ phân biệt trực tiếp/gián tiếp, bài7 ngày/bình luận ngay, AI0.9 so với0.5–<0.9 chờ kết luận; ghi đúng khoản lần gỡ, không lặp/hoàn bình luận hoặc theo upvote hiện tại |
| Chu kỳ | Tuần/tháng lịch UTC+7 nửa mở, timestamp upvote quyết kỳ, upvote sau 00:00 không vào tuần cũ; bảngđã chốt không đổi; sự kiện giáp cuối kỳ còn GAP002 |
| Bảng | Đúngtab/bộ lọc snapshot; hạng 1,2,2,4/username A–Z; không nén do ẩn/không trao lại danh hiệu khi lọc;45 dòng đủ trường20+20+5; trạng thái giao nhau còn GAP004 |
| Danh hiệu | Mọi hạng 1–3 kể cả hòa, có thể>3 hoặc<3/0, người bị loại không chiếm suất; chốt≤60 phút; chỉ tuần, tháng không trao/báo; lịch sử chỉ lưu, hiện W tới chốt sau |
| Hồsơ/nhãn | M02 kiểm đích, M12 cung cấp tổng/badge/ngày/danh hiệu hiện hành/nhãn, cờ Tắt vẫn hiện. BANNED không tự ẩn hồ sơ; DEACTIVATED/DELETED M02 không cung cấp hồ sơ; không lộ tác giả ẩn danh/người cho đã xóa để gắn nhãn |
| Thông báo/cờ | Cùng sự kiện nghiệp vụ không phát hai lần do mô tả nhiều UC; rút giữ thông báo, bật lại cùng người/cửa sổ không đếm thêm; badge=mốc điểm một thông báo/mỗi huy hiệu, không email; cờ Tắt nền vẫn chạy, không bù yêu cầu bị chặn |
| Giới hạn | Sáu GAP giữ chính xác phần chưa đủ hợp đồng; không nhận mọi tổ hợp/lỗi kỹ thuật đã chốt chỉ vì đủ mã nguồn |

## Phần cần làm rõ

| GAP | Nguồn | Giới hạn |
|---|---|---|
| GAP-SC-M12-001 | NOTE-M12-01; FR-M12-04.01, FR-M12-05.01, FR-M12-05.08, BR-M12-22, BR-M12-25 | SC002/UC005: tab mặc định, trước lần tính/chốt đầu và khoảng cuối kỳ→batch chưa đủ hợp đồng hiển thị. Yêu cầu chọn rõ tab trong scenario, giữ bảng hiện hành tới chốt sau; không tự đặt bảng0/trang lỗi hoặc gán thành công cho dữ liệu chưa có. |
| GAP-SC-M12-002 | NOTE-M12-02; FR-M12-05.01, BR-M12-15, BR-M12-16, BR-M12-20, BR-M12-23, BR-M12-25 | AUT004/005: sự kiện rút/trừ/hoàn/đổi status giữa cuối kỳ và lần batch đầu chưa có đầy đủ cách xác định số liệu. Giữ upvote theo mốc khoảng, status/Lớp theo thời điểm nguồn nêu; không tự đồng nhất timestamp/chọn cơ chế lưu lịch sử. |
| GAP-SC-M12-003 | NOTE-M12-03; FR-M12-02.12, FR-M12-02.18, BR-M12-05, BR-M12-07, BR-M12-10 | SC001/UC003 và AUT001/002: nhiều lần gỡ/trừ/hoàn hoặc rút trên nội dung đã trừ nhưng đọc được trong ngữ cảnh staff chưa chốt đầy đủ. Không tự cấp quyền rút/tạo khoản âm/trừ lặp/hoàn theo upvote hiện tại. |
| GAP-SC-M12-004 | NOTE-M12-04; BR-M12-16, BR-M12-20, BR-M12-21, FR-M12-06.08, FR-M12-04.18 | SC002/UC006/007: lọc theo snapshot rồi áp ẩn dòng là diễn giải US cần review để giữ đồng thời đánh lại hạng bộ lọc và không nén do ẩn. DELETED đồng thời HEAVY chưa chốt ưu tiên; không tự đặt cho/ẩn trường hợp giao nhau. |
| GAP-SC-M12-005 | NOTE-M12-06; BR-M12-27, FR-M11-03.09, FR-M11-03.10, FR-M01-12.09 | SC001/003 và UC010: cách hiện nhãn ban cạnh Ẩn danh hoặc cập nhật thông báo người cho đã xóa chưa chốt. Chỉ gắn nhãn ở tên được phép hiện, không lộ tác giả/người cho cũ để hợp thức hóa nhãn. |
| GAP-SC-M12-006 | NOTE-M12-07; FR-M12-01.03, FR-M12-01.13, BR-M12-07, BR-M12-25 | SC001/AUT: trùng/đồng thời/lỗi lưu hoặc giao thông báo, gián đoạn batch chưa có hợp đồng xử lý. Giữ một lượt/tức thời/deadline60 phút; không tự viết rollback/retry/atomicity/outbox/cron/backfill hoặc thông báo lỗi mới. |

NOTE05 được áp theo FR chi tiết/BR24: không công bố lịch sử danh hiệu. Không sửa FR/US/register/skill hoặc module trước, không phê duyệt hộ người dùng.
