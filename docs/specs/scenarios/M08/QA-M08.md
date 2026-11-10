# Kiểm tra scenario — M08 Moderation

[Vietnamese Doc] — 2026-11-10 — Skill scenarios v1.3 — Đang soạn.

Tài liệu chính: [SC-M08.md](SC-M08.md).

| Hạng mục | Kết quả |
|---|---|
| UC/mapping | 6 chính + 17 con = 23 UC; 22 mapping; 25 quan hệ (19 include, 6 extend), 2 extension point |
| Disposition | 15 UC sở hữu scenario (UC015 có 2 SC), 5 embedded, 3 aggregate |
| BF/SC | 16 chức năng actor hoàn chỉnh; không BF chỉ SYSTEM/AI |
| Nhánh E | 124 |
| Đường actor V | 68 |
| Hành vi nền | 8 AUT + 6 RULE, không tính BF/SC |
| Truy vết nguồn | 18 nhóm + 166 FR chi tiết + 55 BR = 239 mã, không mã bỏ |
| Sơ đồ | 7 SVG parse XML, tập UC khớp danh mục US; không vẽ/render mới |
| Baseline | 12 nguồn có SHA-256; FR-M08 1.7 Đã chốt khớp byte bản làm việc, US/overview Chờ duyệt |
| GAP/TBD | 6 GAP nghiệp vụ; report Chat hoãn; 10 reply/5 phút và 0.9/0.5 vẫn tạm |

## Chức năng đã triển khai

| SC | UC owner | Mục tiêu |
|---|---|---|
| [SC-M08-001](SC-M08.md#sc-m08-001) | UC-M08-020 | Gửi báo cáo vi phạm một đối tượng |
| [SC-M08-002](SC-M08.md#sc-m08-002) | UC-M08-003 | Tra cứu hàng chờ và điều tra chi tiết vụ |
| [SC-M08-003](SC-M08.md#sc-m08-003) | UC-M08-004 | Nhận quyền xử lý duy nhất của một vụ |
| [SC-M08-004](SC-M08.md#sc-m08-004) | UC-M08-021 | Giải quyết hoàn chỉnh một vụ báo cáo |
| [SC-M08-005](SC-M08.md#sc-m08-005) | UC-M08-005 | Kết luận một vụ đang giữ |
| [SC-M08-006](SC-M08.md#sc-m08-006) | UC-M08-007 | Xét và quyết định nội dung đang chờ sau AI |
| [SC-M08-007](SC-M08.md#sc-m08-007) | UC-M08-008 | Ẩn một bài viết hoặc bình luận vi phạm trong vụ |
| [SC-M08-008](SC-M08.md#sc-m08-008) | UC-M08-009 | Cảnh cáo người vi phạm được xác định trong vụ |
| [SC-M08-009](SC-M08.md#sc-m08-009) | UC-M08-010 | Bỏ một cảnh cáo do AI ra |
| [SC-M08-010](SC-M08.md#sc-m08-010) | UC-M08-011 | Ban người vi phạm trong vụ theo quyết định con người |
| [SC-M08-011](SC-M08.md#sc-m08-011) | UC-M08-012 | Gỡ sớm một ban đang hiệu lực |
| [SC-M08-012](SC-M08.md#sc-m08-012) | UC-M08-013 | Xem mức cảnh cáo và hạn thử thách được phép |
| [SC-M08-013](SC-M08.md#sc-m08-013) | UC-M08-015 | Ẩn nhóm vi phạm và toàn bộ nội dung của nhóm |
| [SC-M08-014](SC-M08.md#sc-m08-014) | UC-M08-015 | Khóa hoạt động một nhóm vi phạm |
| [SC-M08-015](SC-M08.md#sc-m08-015) | UC-M08-016 | Mở khóa nhóm để hoạt động theo quyền thông thường |
| [SC-M08-016](SC-M08.md#sc-m08-016) | UC-M08-025 | Tra cứu nhật ký kiểm duyệt trong phạm vi được phép |

## Kiểm tra cấu trúc và đường đi

Validator skill PASS cho metadata, sáu phần, actor/sourceID, UC/mapping/BF, nhánh thay bước/đích nhập lại, luân phiên và khả năng đến terminal có hậu điều kiện. Main bắt đầu đúng actor chính và kết thúc SYSTEM/SUCCESS của mục tiêu chức năng. E nhập lại mở đầy đủ lựa chọn tiếp; không kết thúc thành công khi mới claim trong BF giải quyết toàn vụ.

V thay toàn bộ theo actor khởi tạo; kiểm riêng actor đầu, tập subject, thứ tự, luân phiên và SYSTEM kết thúc với hậu điều kiện tương ứng. Validator graph mặc định chỉ duyệt main/E; PASS không tự chứng minh V hoặc đầy đủ ngữ nghĩa. Sources V vẫn đối chiếu với FR. Admin–Mod dùng người giữ Admin nhất quán; User/Owner/Group Mod không có quyền staff; role Mod/Admin của M08 không dùng ACT003 gộp.

Đã đối soát 239 mã nguồn và 7 SVG, hash FR chính thức/bản làm việc, liên kết/anchor trong hai đầu ra. Đây là review agent, không phê duyệt của stakeholder.

Lệnh thực tế từ repo root:

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M08/SC-M08.md --fr docs/specs/fr/FR-M08.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M03.md --fr docs/specs/fr/FR-M04.md --fr docs/specs/fr/FR-M07.md --fr docs/specs/fr/FR-M09.md --fr docs/specs/fr/FR-M10.md --fr docs/specs/fr/FR-M11.md --fr docs/specs/fr/FR-M12.md --fr docs/specs/fr/FR-M13.md --us docs/specs/us/US-M08.md
```

## Review nghiệp vụ

| Phép kiểm | Kết quả/ranh giới |
|---|---|
| Mục tiêu actor | Nhận quyền, kết luận và biện pháp độc lập theo hợp đồng US; SC004 bắt đầu vụ và đi đến đóng mọi báo cáo. Không lấy gom vụ, tính ưu tiên, kiểm quyền hoặc quét AI làm BF |
| Vòng biện pháp | EP-CASE-ACTION mở thao tác và trở M5 để chọn tiếp hoặc kết luận; Bác bỏ chuẩn chưa áp biện pháp, Có xử lý sau biện pháp đúng target. Không tự đóng sau ẩn/cảnh cáo/ban |
| Báo cáo | 4 loại target, một lý do đúng loại, Khác cần mô tả, tối đa 3 ảnh ≤5MB; lỗi nhập có sửa/gửi lại, trùng theo actor/cùng vụ Mở; không rút/sửa; Admin miễn theo nguồn |
| Điều tra | Ưu tiên=max trọng số+2×số báo cáo, hòa theo mở trước; đọc không cần giữ, nội dung lưu giữ chỉ đúng ngữ cảnh; chỉ số 90×24h tham khảo, không tự phạt |
| Quyền giữ | Một người giữ, tự nhả đủ 30 phút từ hoạt động cuối của chính người giữ; mất quyền bị từ chối hoặc nhận lại khi còn Mở/chưa giữ rồi gửi lại yêu cầu; không nút nhả/log nhận |
| Quyền role | Mod không xem/nhận vụ post/comment/account mình/Mod, Admin xử lý Mod khác mình; không ai cảnh cáo/ban Admin; không mở rộng tự nhắm sang nhóm chưa chốt |
| Nội dung và chế tài | Post gắn cờ được giữ/ẩn; comment trung bình hiện lại/giữ ẩn, cảnh cáo là lựa chọn riêng; HEAVY không cảnh cáo mới, con người quyết Ban; không tự phục hồi comment ẩn cao/staff ẩn |
| AI | Hai cờ, trigger reply, bản hiện tại, max 4 nhóm, ngưỡng tạm, tối đa 2 lần thử; không quét ngay khi đăng/sửa, Admin bỏ quét, không AI ban, không quét Chat/Spam/đạo văn/sai thông tin |
| Cảnh cáo | Thêm reset đúng 7/10/15×24h, giảm về 4/2/0 và nối thử thách; bỏ AI giữ record/hạn, không mượn sàn 0 M09; riêng tư/search/BXH/feed đúng phạm vi |
| Ban | 30/90 ngày/vĩnh viễn theo mọi ban từng hiệu lực trừ Bị lật; vĩnh viễn thủ công bỏ leo thang, không chồng; gỡ trước ban lại có đủ bước; gỡ/hết hạn ACTIVE không phục hồi Mod |
| Nhóm | Ẩn không bỏ ẩn; Khóa đầy đủ BR-M11-28 kể cả quản trị và Owner rời, vẫn đọc/bookmark/report/Member rời/chuyển Owner; mở khóa trực tiếp; không tự phạt Owner |
| Kết quả/log | Reporter chỉ kết quả chung, AI không nhận; target chỉ chi tiết khi Có xử lý, không xem tố cáo; khiếu nại chỉ cảnh cáo/ban/bài ẩn; log bất biến vĩnh viễn, phạm vi vụ mình xử lý/đúng thao tác appeal hiện tại/Admin toàn bộ |

## Các phần còn thiếu hợp đồng

| GAP | Giới hạn |
|---|---|
| GAP-SC-M08-001 | Mẫu số chỉ số tập trung bằng 0 chưa có cách hiển thị/xử lý. Đường điều tra minh họa dùng mẫu số dương, không gán 0/100%, báo lỗi hoặc từ chối xem do agent đặt. Chưa thể khép riêng nhánh chỉ số này; các quyền/chi tiết độc lập vẫn giữ. |
| GAP-SC-M08-002 | Số lần hiện tại 0 nhưng còn cảnh cáo AI lịch sử: chưa chốt record nào còn được trừ/sàn hay điều kiện bỏ. Chỉ viết đường số lần dương, không mượn sàn 0 M09, không tạo âm hoặc từ chối mới. Cần owner chốt trước hoàn thiện nhánh này. |
| GAP-SC-M08-003 | Nhiều nội dung cùng tác giả trong một lô quét qua biên HEAVY chưa chốt thứ tự đồng thời. Giữ mỗi nội dung một cảnh cáo khi đủ điều kiện và guard đã HEAVY không tăng; không tự định serialization, cảnh cáo thứ 7 hoặc AI ban. |
| GAP-SC-M08-004 | Self-report/self-handle vụ nhóm của chính staff chưa được nêu như post/comment/account. Dùng Owner khác actor trong đường hợp lệ; không tự cho phép hoặc cấm rộng mọi nhóm Owner Mod. Nhóm Owner Admin không được report đã chốt riêng. Cần chốt phần tự nhắm nhóm, không mở lại quyền đã rõ. |
| GAP-SC-M08-005 | Sau khi đã áp biện pháp rồi chọn Bác bỏ, hoặc chỉ cảnh cáo reporter ác ý nhưng kết luận về người bị báo cáo: chưa chốt ý nghĩa kết luận/hệ quả. Không rollback, tự ép Có xử lý hoặc tự báo target vi phạm. Luồng chuẩn Bác bỏ chưa có biện pháp, Có xử lý sau biện pháp đúng target; cảnh cáo reporter có mục tiêu độc lập, riêng kết luận phần này còn thiếu hợp đồng. |
| GAP-SC-M08-006 | Ban Owner khiến M11 chuyển Owner ngay (hoặc xóa mềm nhóm nếu chỉ có Owner), kể cả nhóm đang khóa. M08 chưa nêu mốc ràng buộc Owner trong hồ sơ vụ: Owner lúc báo cáo/xử lý hay Owner hiện tại, và người nhận/mức chi tiết kết luận sau thay đổi. Đã viết Ban Owner đến hiệu lực cùng chuyển quyền theo M11; chưa tự chốt kết luận toàn vụ sau thay đổi Owner, không gán thông báo/kết tội Owner mới hoặc giả định giữ snapshot Owner cũ. Phần giải quyết toàn vụ ở tổ hợp này cần hợp đồng M08–M11; nhánh Khóa + cảnh cáo Owner không đổi quyền vẫn viết đầy đủ. |

TBD-M08-01 report Chat hoãn MS1; TBD04/05 còn ngưỡng tạm, không coi chốt. NOTE05 và TBD02/03 không mở lại quyền hiện lại comment. Không đưa unknown branch vào REJECTED giả; giữ nhánh dương có nguồn và ghi thiếu. Các lớp tương đương/biên đã đối soát tại mục5/6 tài liệu chính; chưa quyết ordering/giao dịch hoặc mọi tổ hợp thiếu nguồn. Hoàn tất viết phần đủ căn cứ không đồng nghĩa sáu GAP đã được giải quyết.

Biến thể target của SC004/006 chọn đúng vụ ngay từ đầu rồi nhận/điều tra trước khi quyết định; không đổi từ vụ P81 sang C81/G81 giữa hành trình. Vụ nhóm có đường khóa + cảnh cáo Owner + kết luận với đủ bước, biện pháp Owner là lựa chọn riêng.

Xét bài gắn cờ chọn Ẩn có log/trừ điểm ngay và chọn cảnh cáo riêng. Ban Owner riêng có hiệu lực cùng chuyển quyền theo M11; kết luận toàn vụ sau khi Owner đổi còn GAP006, không dùng một đường thành công giả để che hợp đồng thiếu. Bỏ AI từ số lần 1 xuống 0 là đường đã có hợp đồng, khác GAP002 khi số lần đã 0 trước thao tác.
