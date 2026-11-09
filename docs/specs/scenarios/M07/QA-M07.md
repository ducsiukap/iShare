# Kết quả kiểm tra scenario M07 Notification

[Vietnamese Doc] — 2026-11-09 — Skill scenarios v1.3 — Đang soạn để review.

Tài liệu chính: [SC-M07.md](SC-M07.md).

| Hạng mục | Kết quả |
|---|---|
| Mô hình | 4 UC chính, 11 UC con, 11 mapping, 4 quan hệ |
| Disposition | 3 aggregate; 10 UC sở hữu chức năng (core023 và 9 sub); 2 embedded (UC007/008) |
| BF/SC | 10 hành trình actor hoàn chỉnh, không BF thuần SYSTEM/email |
| Nhánh E | 52 |
| Đường actor V | 20 |
| Quy tắc nền | 9 AUT +5 RULE, không tính vào BF/SC |
| Mã hiệu lực | 9 nhóm +88 FR chi tiết +25 BR =122; 13 mã đã bỏ ghi riêng |
| Sơ đồ nguồn | 5 SVG khớp tập ID với US/mapping; không tuyên bố render mới |
| Nguồn | FR 1.5 Đã chốt, khớp byte bản làm việc; US/overview Chờ duyệt |
| GAP | 2 điểm thiếu hợp đồng: causer bảo mật và bắt đầu follow DEACTIVATED |

## Các chức năng actor

| SC | Mục tiêu |
|---|---|
| [SC-M07-001](SC-M07.md#sc-m07-001) | Theo dõi người dùng hoặc Topic |
| [SC-M07-002](SC-M07.md#sc-m07-002) | Bỏ theo dõi người dùng hoặc Topic |
| [SC-M07-003](SC-M07.md#sc-m07-003) | Xem chuông và danh sách thông báo của mình |
| [SC-M07-004](SC-M07.md#sc-m07-004) | Đọc một thông báo và mở nội dung liên quan |
| [SC-M07-005](SC-M07.md#sc-m07-005) | Đánh dấu tất cả thông báo của mình đã đọc |
| [SC-M07-006](SC-M07.md#sc-m07-006) | Phản hồi đề xuất làm Mod hoặc Admin |
| [SC-M07-007](SC-M07.md#sc-m07-007) | Kiểm tra số cuộc trò chuyện chưa đọc và mở hộp thư |
| [SC-M07-008](SC-M07.md#sc-m07-008) | Bật hoặc tắt nhận thông báo tương tác theo bài |
| [SC-M07-009](SC-M07.md#sc-m07-009) | Bật hoặc tắt popup riêng của một cuộc trò chuyện |
| [SC-M07-010](SC-M07.md#sc-m07-010) | Bật hoặc tắt popup toàn bộ Chat |

## Kiểm tra đã thực hiện

Validator skill PASS cho main/E: sáu phần, metadata, actor/source ID, UC/mapping/BF, bước thay thế/đích, luân phiên và khả năng tới terminal có hậu điều kiện. Main bắt đầu actor chính, kết thúc SYSTEM/SUCCESS. UC007 được mở đúng cả phạm vi một/tất cả; UC008 tính cuộc theo tin được thấy; phản hồi đề xuất đi tới kết quả vai trò, không dừng ở chuyển M10.

Đường V trong mục 6 thay toàn bộ theo Guest/Mod/Admin được kiểm riêng actor khởi tạo, tập actor, luân phiên/thứ tự và terminal có hậu điều kiện. Graph validator mặc định không duyệt V; PASS main/E không tự chứng minh V hoặc độ đầy đủ nghiệp vụ. Sources của V vẫn được đối chiếu. Đề xuất Admin hợp lệ cho Mod được dùng ở V thay vì sao chép đề xuất Mod cho người đã là Mod.

Đã đối chiếu 122 mã hiệu lực, loại đúng 13 mã bỏ khỏi mẫu số; 5 SVG khớp node, hash FR chính thức/bản làm việc, file/anchor tại đích. Đây là review agent, không phê duyệt nguồn/kết quả.

Lệnh từ repo root:

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M07/SC-M07.md --fr docs/specs/fr/FR-M07.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M03.md --fr docs/specs/fr/FR-M04.md --fr docs/specs/fr/FR-M05.md --fr docs/specs/fr/FR-M09.md --fr docs/specs/fr/FR-M10.md --fr docs/specs/fr/FR-M16.md --us docs/specs/us/US-M07.md
```

## Các điểm nghiệp vụ được kiểm

| Điều kiện | Kết quả |
|---|---|
| Follow/unfollow | User/Topic, timestamp; báo người mới một lần/cặp; unfollow không báo; không bắt đầu BANNED, quan hệ cũ BANNED/DEACTIVATED giữ |
| Xem/read | Chuông 10, trang 20/lần, 55 tải 20+20+15; unread 3 gồm N011 ngoài chuông; mở chuông vẫn3, mark-all→0, Chat vẫn3 |
| Đích không tồn tại | Đánh dấu read trước, giữ bản và báo đúng câu; chủ nội dung chỉ đọc theo M03/M04, không cấp quyền chung |
| Đề xuất | Một lựa chọn, 7×24 giờ, proposal mới cùng loại khóa cũ; chấp nhận role ngay, từ chối giữ role; kiểm lại role/tài khoản khi chọn |
| Popup/badge | 5+2+1 tin được thấy thuộc3 cuộc→badge 3; tin sau rời không tính; per/global mute không đổi badge |
| Mute | Global không ngoại lệ, bỏ global giữ per; bật riêng không vượt global; rời/kick nhóm reset per, vào lại vẫn chịu global |
| Kênh/email | Chỉ whitelist, cảnh báo tự xóa chỉ email; lần đầu+3 retry mỗi 60 giây, push lỗi không retry |
| Upvote | Cửa sổ cố định 5 phút riêng từng bài/comment; người mới cập nhật unread/thứ tự, bỏ/re-upvote không thêm người, đúng t0+5 phút mở cửa sổ mới |

## Điểm còn thiếu và giới hạn

**GAP-SC-M07-001:** chưa chốt causer sự kiện bảo mật để hòa hợp quy tắc self-filter M07 với thông báo cho chính chủ theo M01. Giữ yêu cầu/kênh đã chốt, chưa khẳng định hoàn tất nhánh tạo bảo mật; cần owner M01/M07 đối chiếu.

**GAP-SC-M07-002:** chưa chốt rõ bắt đầu follow DEACTIVATED giữa FR/BR hiện hành và Q-06 cũ. Không tự cấm mọi tài khoản không ACTIVE; đã viết trường hợp target ACTIVE, cấm BANNED và giữ quan hệ cũ theo nguồn.

NOTE02 không chốt push khi cập nhật gộp; NOTE03 theo hạn 7 ngày hiện hành; NOTE04 không tự chọn giao thức/read realtime/biên đồng thời. FR không có TBD từ OPEN chạm M07; không biến các GAP thành quyết định stakeholder hoặc tự sửa register. Bộ scenario hoàn thành phần hành vi đủ căn cứ, còn ở Đang soạn và không được nhận đầy đủ hai phạm vi thiếu hợp đồng.
