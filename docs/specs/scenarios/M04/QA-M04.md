# Kết quả kiểm tra scenario M04 Comment

[Vietnamese Doc] — 2026-11-09 — Skill scenarios v1.3 — Đang soạn để review.

Đầu ra chính: [SC-M04.md](SC-M04.md).

| Hạng mục | Kết quả |
|---|---|
| Mô hình | 3 UC chính,7 UC con,8 mapping |
| Cách bao phủ | 2 aggregate,1 abstract (core020),6 UC sở hữu mục tiêu actor,1 embedded (UC007) |
| Hành trình | 6 BF/SC sáu phần |
| Nhánh E | 67 |
| Đường thay actor V | 14 |
| Quy tắc nền | 6 |
| Truy vết | 6 nhóm +70 FR chi tiết +23 BR =99 mã; không mã thiếu đích |
| Sơ đồ | 4 SVG khớp ID với bảng US |
| Nguồn | FR1.4 đã chốt, khớp bản làm việc; US/overview Chờ duyệt |

## Sáu hành trình hoàn chỉnh

| SC | Chức năng |
|---|---|
| [SC-M04-001](SC-M04.md#sc-m04-001) | Đọc và sắp xếp luồng bình luận của bài |
| [SC-M04-002](SC-M04.md#sc-m04-002) | Viết và gửi bình luận gốc dưới bài |
| [SC-M04-003](SC-M04.md#sc-m04-003) | Trả lời bình luận trong luồng hai cấp |
| [SC-M04-004](SC-M04.md#sc-m04-004) | Sửa nội dung bình luận của mình |
| [SC-M04-005](SC-M04.md#sc-m04-005) | Xóa bình luận của mình khỏi luồng người dùng |
| [SC-M04-006](SC-M04.md#sc-m04-006) | Xem lại nội dung bình luận mình đã bị xử lý |

## Kiểm tra đã thực hiện

Validator skill PASS, không lỗi cấu trúc cho main/E: sáu phần, nguồn ID, actor, UC/mapping/BF, bước/đích, luân phiên và đường kết thúc. Main bắt đầu actor chính, có cả actor/SYSTEM, kết thúc SYSTEM/SUCCESS. Các điểm UC007 đã được triển khai ngay trong luồng gửi/sửa.

Đường V thay toàn bộ theo Guest/Mod/Admin nằm trong mục6 của SC bao chứa; kiểm riêng actor khởi tạo, luân phiên và terminal có hậu điều kiện. Validator graph mặc định không duyệt V; PASS của graph chỉ bao gồm main/E, không tự chứng minh toàn bộ V. Sources ở V vẫn được validator đối chiếu.

Đã kiểm byte/hash FR chính thức so với bản làm việc, 99 mã có vị trí và4 SVG khớp tập UC. File/anchor được kiểm tại vị trí đầu ra trước khi ghi. Đây là review của agent, chưa là phê duyệt stakeholder.

Lệnh từ repo root:

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M04/SC-M04.md --fr docs/specs/fr/FR-M04.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M03.md --fr docs/specs/fr/FR-M08.md --fr docs/specs/fr/FR-M09.md --fr docs/specs/fr/FR-M11.md --us docs/specs/us/US-M04.md
```

## Ma trận nghiệp vụ đã đối soát

| Điều kiện | Tạo gốc/trả lời | Sửa | Xóa | Đọc luồng |
|---|---|---|---|---|
| Khóa bình luận/toàn bộ | Từ chối | Từ chối | Được nếu điều kiện khác đạt | Bình luận cũ vẫn hiện theo quyền |
| HEAVY | Từ chối | Được nếu điều kiện khác đạt | Được nếu điều kiện khác đạt | Theo quyền bài |
| Bị ẩn | Không trả lời trực tiếp đích bị ẩn | Từ chối | Từ chối | Không ai thấy body, kể cả tác giả/Mod |
| Gốc hiện dấu, trả lời đích vẫn bình thường | Được trả lời đích đó, vẫn cấp hai | Theo trạng thái bình luận muốn sửa | Theo trạng thái bình luận muốn xóa | Giữ dấu gốc khi còn trả lời bình thường |
| Rời/kick Private | Không có quyền bình luận nhóm | Từ chối | Từ chối | Theo M11 |
| Đã xóa bình luận | Không trả lời trực tiếp đích này | Từ chối | Không xóa lại | Không hiện body; không khôi phục |

Các ô Được không miễn sở hữu, quyền nhóm, phiên hoặc điều kiện khác. Sửa bình luận giữ mốc đăng/vị trí/kiểm duyệt, chỉ ghi lần sửa gần nhất; không áp cách lưu lịch sử/sửa khi khóa của bài M03.

Số đếm mẫu gốc3+trả lời2=5; xóa/ẩn gốc có2 trả lời thì4; xóa/ẩn trả lời còn trả lời trỏ tới nó thì thay trích, không cascade; hết trả lời bình thường thì bỏ dấu gốc. Top hòa upvote dùng mốc đăng trước; mọi cách sắp gốc giữ thứ tự trả lời cũ→mới.

## Giới hạn nguồn

TBD-M04-01 đã đóng: lật cảnh cáo/ban vẫn giữ Bị ẩn. Câu chữ nhãn xem lại và cách bố trí/cắt một dòng trích để thiết kế, không tự ấn định số ký tự. Lỗi mạng/gửi/lưu và transaction chưa có hợp đồng đầy đủ, không thêm retry/rollback. Không có GAP nghiệp vụ mới cần tự giải quyết; các NOTE nguồn được giữ ở mục7 của SC.

Bản soạn chưa được phê duyệt. Không mở thêm phạm vi AI, báo cáo, khiếu nại, upvote/điểm, nhóm, thông báo hoặc tìm kiếm/Trending của module khác.
