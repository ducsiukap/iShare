# Kiểm tra scenario — M10 Admin Panel

[Vietnamese Doc] — 2026-11-10 — Skill scenarios v1.3 — Đang soạn.

Tài liệu chính: [SC-M10.md](SC-M10.md).

| Hạng mục | Kết quả |
|---|---|
| UC/mapping | 4 chính + 18 con = 22 UC, 18 mapping; 9 quan hệ (7 include, 2 generalization), không extend/extension point |
| Disposition | 15 scenario, 3 embedded (009/014/018), 1 abstract (002), 3 aggregate |
| BF/SC | 15 chức năng actor hoàn chỉnh; không BF khởi tạo/đếm hạn/thu hồi do ban/ghi log |
| Nhánh E | 84 |
| Đường actor V | 49 |
| Hành vi nền | 4 AUT + 6 RULE, không tính BF/SC |
| Mã nguồn | 15 nhóm + 107 FR chi tiết + 30 BR = 152 hiệu lực; FR-M10-03.05 bỏ riêng |
| SVG nguồn | 5 SVG parse XML, tập UC khớp US; không sửa/render mới |
| Baseline | 13 nguồn có SHA-256; FR-M10 1.4 Đã chốt khớp byte bản làm việc; US/overview Chờ duyệt |
| GAP | 5 điểm theo NOTE01–05; TBD-M10-01 đã đóng, không mở lại |

## Chức năng đã triển khai

| SC | UC owner | Mục tiêu |
|---|---|---|
| [SC-M10-001](SC-M10.md#sc-m10-001) | UC-M10-001 | Tra cứu người dùng và thao tác quản trị áp dụng |
| [SC-M10-002](SC-M10.md#sc-m10-002) | UC-M10-003 | Gửi đề xuất nhận vai trò Mod |
| [SC-M10-003](SC-M10.md#sc-m10-003) | UC-M10-004 | Gửi đề xuất nhận vai trò Admin |
| [SC-M10-004](SC-M10.md#sc-m10-004) | UC-M10-005 | Trả lời một đề xuất nhận vai trò của mình |
| [SC-M10-005](SC-M10.md#sc-m10-005) | UC-M10-006 | Giáng cấp một Mod về User |
| [SC-M10-006](SC-M10.md#sc-m10-006) | UC-M10-007 | Thu hồi vai trò Admin của một Admin khác |
| [SC-M10-007](SC-M10.md#sc-m10-007) | UC-M10-008 | Tự từ chức vai trò sau xác nhận |
| [SC-M10-008](SC-M10.md#sc-m10-008) | UC-M10-010 | Điều chỉnh AI tổng hoặc một phạm vi AI riêng |
| [SC-M10-009](SC-M10.md#sc-m10-009) | UC-M10-011 | Bật hoặc tắt chế độ bảo trì |
| [SC-M10-010](SC-M10.md#sc-m10-010) | UC-M10-012 | Bật hoặc tắt tạm dừng đăng ký mới |
| [SC-M10-011](SC-M10.md#sc-m10-011) | UC-M10-013 | Bật hoặc tắt cờ Group, Chat hoặc Gamification |
| [SC-M10-012](SC-M10.md#sc-m10-012) | UC-M10-015 | Đặt mới hoặc sửa nội dung banner toàn trang |
| [SC-M10-013](SC-M10.md#sc-m10-013) | UC-M10-016 | Gỡ banner cho toàn hệ thống |
| [SC-M10-014](SC-M10.md#sc-m10-014) | UC-M10-017 | Xem và đóng riêng banner hiện tại |
| [SC-M10-015](SC-M10.md#sc-m10-015) | UC-M10-023 | Tra cứu nhật ký thao tác Admin theo tiêu chí |

Gửi Mod/Admin có mục tiêu role đích và hồ sơ/thông báo/vòng đời độc lập, có thể cùng hiệu lực cho một người; không tách chỉ vì quyền gốc và không thêm BF gửi abstract. Trả lời không bị kéo vào phiên gửi. Đặt/Sửa cùng việc công bố một nội dung duy nhất theo contract UC015; gỡ toàn trang và đóng cá nhân có chức năng khác. Bật/Tắt, loại công tắc riêng, role/lỗi/trạng thái là nhánh, không BF mới.

## Kiểm tra đã thực hiện

Validator skill PASS cho metadata, sáu phần, actor/sourceID, UC/mapping/BF, nhánh thay bước/đích nhập lại, luân phiên và khả năng tới terminal có hậu điều kiện. Main bắt đầu đúng actor chính và kết thúc SYSTEM/SUCCESS của chức năng; từ chối đề xuất hợp lệ là SUCCESS của trả lời, khác REJECTED của yêu cầu không hợp lệ; hủy từ chức CANCELLED giữ role.

V được kiểm riêng actor khởi tạo, tập subject, thứ tự/luân phiên, SYSTEM kết thúc và hậu điều kiện. Validator graph mặc định chỉ duyệt main/E; PASS không tự chứng minh V/đầy đủ ngữ nghĩa. Sources V vẫn đối chiếu. Root là guard trên ACT007, không actor mới; Mod không vào Panel nhưng trả lời Admin/từ chức/banner theo quyền cá nhân. Admin Lan Từ chối lời mời Mod cũ còn hiệu lực sau khi nhận Admin khác loại có đường riêng, không chạy guard chỉ dành Chấp nhận.

Đã đối chiếu 152 mã hiệu lực và một mã bỏ, 5 SVG, baseline FR chính thức/bản làm việc, hash nguồn và file/anchor ở đích. Đây là review agent, không phê duyệt stakeholder. Lệnh từ repo root:

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M10/SC-M10.md --fr docs/specs/fr/FR-M10.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M06.md --fr docs/specs/fr/FR-M07.md --fr docs/specs/fr/FR-M08.md --fr docs/specs/fr/FR-M09.md --fr docs/specs/fr/FR-M11.md --fr docs/specs/fr/FR-M12.md --fr docs/specs/fr/FR-M13.md --fr docs/specs/fr/FR-M14.md --fr docs/specs/fr/FR-M16.md --us docs/specs/us/US-M10.md
```

## Đối soát nghiệp vụ

| Phép kiểm | Kết quả/ranh giới |
|---|---|
| Tra cứu | Khớp username/display_name theo M06, lọc role/đủ trường/nhãn gốc; không bê giới hạn 3/chỉ ACTIVE vào Panel; Xem thao tác trả log M08 lọc đúng Mod, không KPI mới |
| Gửi đề xuất | Quyền/đích/ACTIVE/xong bước 3 trước thay bản; không điểm/uy tín/thâm niên; một hiệu lực mỗi loại/người, khác loại giữ; thay cũ trước lưu mới/N mới, không phong thẳng |
| Phản hồi | Owner/hiệu lực/một lần; Chấp nhận kiểm ACTIVE/role hiện tại, không quyền người gửi cũ/đăng ký mới; Từ chối giữ role và hiện lựa chọn; đúng hạn 7×24h từ chối, nguyên nhân bị thay không tự mang nhãn hết hạn |
| Role | Giáng Mod/thu hồi Admin về USER ngay, không đồng ý/khiếu nại; gốc bảo vệ, không quay về Mod cũ. Từ chức xác nhận một lần/hủy giữ role; ban Mod tự về USER, log Hệ thống, hết/gỡ/lật không tự trả Mod |
| AI | Tổng AND riêng, tóm tắt theo Tổng; lưu riêng khi Tổng off và dùng khi on lại; tắt chủ đích khác lỗi. Tạo bù Search theo owner khi đủ cờ/AI có kết quả, không hứa đã xong hoặc bù tóm tắt |
| Bảo trì/pause | Bảo trì cả phiên cũ người không Admin bị chặn; pause chỉ chặn account mới, còn liên kết Google/tiếp bước 2/3; không chính sách logout/tái chạy yêu cầu mới |
| Cờ tính năng | Đúng Group/Chat/Gamification, thông báo bận/lối vào/dữ liệu/việc nền/kiểm duyệt giữ, Admin vẫn theo quyền owner; không dừng cộng điểm/ẩn mọi bài nhóm khỏi feed, không bù thao tác đã từ chối |
| Banner | Một nội dung plain text; trim để đếm, ASCII 0/1/200/201; lỗi sửa rồi đến công bố. Đặt mới/Sửa nội dung khác hiện lại người đã đóng; gỡ toàn trang khác Guest C1 đóng; Markdown literal 13 ký tự không diễn giải |
| Audit | Đúng người gửi/nhận/từ chức/Hệ thống, lý do tùy chọn hoặc lấy bắt buộc từ owner; kiểm duyệt Admin song song M08, AI riêng; không log xem/nhận-nhả/ordinary action/role không đổi khi Từ chối |
| Đọc log | Mọi người làm, năm trường, mới nhất trước/UTC+7, lọc một hoặc giao hai tiêu chí; bất biến/vĩnh viễn, không log đọc, không nhãn DELETED tự mượn M08 |

## Phần chưa có hợp đồng

| GAP | Giới hạn |
|---|---|
| GAP-SC-M10-001 | Chấp nhận bị từ chối vì role không phù hợp/không ACTIVE đã rõ không đổi role; trạng thái đề xuất sau lỗi và khả năng thử lại chưa chốt. Viết phản hồi từ chối đã có nguồn, không tự đặt Đã từ chối/Hết hiệu lực/giữ Chưa trả lời hoặc tiêu thụ lượt; chưa viết tiếp đường thử lại dựa vào trạng thái chưa rõ. |
| GAP-SC-M10-002 | Nguồn chỉ chốt Guest đóng theo trình duyệt; người đăng nhập chưa chốt theo tài khoản/thiết bị, bao lâu/qua phiên và đồng bộ thế nào. Giữ kết quả đóng cho người xem và bản đổi nội dung hiện lại, không tự chọn kỹ thuật hoặc thời hạn. |
| GAP-SC-M10-003 | Chưa chốt đơn vị ký tự Unicode (grapheme/code point/UTF-16) hoặc Sửa nhưng nhập lại cùng nội dung có được coi là bản mới/reset dấu đóng không. Viết biên ASCII trống/1/200/201 và sửa khác nội dung/đặt mới; không gán chính sách cho emoji/ký tự tổ hợp hoặc chỉnh không thay đổi. |
| GAP-SC-M10-004 | Chưa chốt lỗi lưu/thông báo/audit, giao dịch nhiều thay đổi, đồng thời hoặc yêu cầu đang chạy. Giữ hợp đồng thành công và thứ tự kiểm→hết hiệu lực bản cũ→lưu mới; không thêm rollback/outbox/retry/khóa hoặc nhận thành công khi chức năng chưa trọn. |
| GAP-SC-M10-005 | Chưa liệt kê riêng tập trạng thái account được tìm quản trị, nhất là DELETED. Giữ cách khớp/role/trường đã chốt; không tự lọc chỉ ACTIVE/xong bước 3, giới hạn ba hoặc khẳng định tập đầy đủ tài khoản đã xóa. Mẫu minh họa các account ACTIVE, điều kiện đề xuất vẫn kiểm riêng. |

Giữ phản ứng từ chối Chấp nhận lỗi đã có nguồn và nêu rõ phần trạng thái chưa chốt (GAP001), không tự kéo dài sang thử lại. Các GAP còn lại không được lấp bằng đồng bộ banner, đơn vị Unicode, rollback/retry, tập account tìm quản trị hoặc cơ chế triển khai tự chọn. TBD01 cờ đã đóng theo owner; FR03.05 đề xuất vô hạn đã bỏ. Toàn bộ hành vi đủ căn cứ trong scope được triển khai/đối chiếu; chưa nhận các nhánh thiếu hợp đồng đã được chốt.
