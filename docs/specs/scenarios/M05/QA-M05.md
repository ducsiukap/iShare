# QA-M05 — Tái kiểm sau khắc phục

[Vietnamese Doc] — 11/11/2026, skill scenarios v1.4. Trạng thái Đang soạn theo nguồn nghiệp vụ.

## Kết quả hiện hành

| Kiểm tra | Kết quả |
| --- | --- |
| Validator chuẩn | PASS 15 UC, 9 BF, 9 SC, 115 nhánh E |
| Chuẩn hóa biến thể | 22 nhánh từ ID V lịch sử đã đăng ký E tại M1, bảng chuyển đổi ở cuối SC |
| Bảo toàn nội dung | 341 bước main/E/V lịch sử được đối chiếu trước/sau, chỉ đổi ID nhánh, vị trí dẫn và dữ liệu đã xác nhận trong QA-SC-02/03 |
| Phạm vi kiểm máy | Actor/nguồn, guard đăng ký, điểm thay/điểm vào, đích bước, luân phiên, khả năng kết thúc và hậu điều kiện của toàn bộ main/E |
| GAP và phê duyệt | Các GAP nguồn còn mở được liệt kê trong SC và báo cáo tái kiểm toàn bộ, đầu ra giữ Đang soạn |


Bản hiện hành [SC-M05.md](SC-M05.md). Kết quả toàn bộ và các quyết định còn chờ ở [báo cáo khắc phục](../QA-M01-M16-2026-11-11-khac-phuc.md).

## Bằng chứng lần soạn trước

Phần dưới lưu báo cáo của chính module này trước ngày chuyển đổi. Các số E/V và nhận xét giới hạn validator trong phần lịch sử phản ánh công cụ lúc soạn. Số liệu và kết quả áp dụng hiện tại nằm ở mục Kết quả hiện hành, các biến thể đã được kiểm bằng hợp đồng E.

# Kết quả kiểm tra scenario M05 Topic & Tag

[Vietnamese Doc] — 2026-11-09 — Skill scenarios v1.3 — Đang soạn để review.

Đầu ra chính: [SC-M05.md](SC-M05.md).

| Hạng mục | Kết quả |
|---|---|
| Mô hình | 4 UC chính, 11 UC con, 12 mapping, 6 quan hệ |
| Disposition | 3 aggregate (core Summary), 3 embedded (core020 User goal, UC002, UC012), 9 UC sở hữu chức năng |
| Luồng | 9 BF/SC sáu phần, không BF thuần SYSTEM/AI |
| Nhánh E | 93 |
| Đường actor V | 22 |
| Quy tắc nền | 4 AUT +4 RULE; không tính vào số BF/SC |
| Truy vết | 11 nhóm +106 FR chi tiết +31 BR =148 mã; không mã thiếu vị trí |
| SVG nguồn | 5 SVG khớp ID catalog/mapping; không tuyên bố render mới |
| Baseline | FR 1.7 Đã chốt, byte/hash khớp bản làm việc; US/overview Chờ duyệt |
| Output | docs/specs/scenarios/M05, không tạo trước module khác |

## Chức năng actor đã triển khai

| Scenario | Chức năng |
|---|---|
| [SC-M05-001](SC-M05.md#sc-m05-001) | Gán và chốt Topic cho bài viết của mình |
| [SC-M05-002](SC-M05.md#sc-m05-002) | Gắn và chốt Tag tự do cho bài viết của mình |
| [SC-M05-003](SC-M05.md#sc-m05-003) | Xem danh mục và nhãn phân loại Topic, Tag |
| [SC-M05-004](SC-M05.md#sc-m05-004) | Thêm Topic mới vào danh mục hệ thống |
| [SC-M05-005](SC-M05.md#sc-m05-005) | Gộp Topic nguồn vào Topic đích |
| [SC-M05-006](SC-M05.md#sc-m05-006) | Xóa Topic không có bài viết ngoài nháp |
| [SC-M05-007](SC-M05.md#sc-m05-007) | Vô hiệu hóa Tag trong tình huống khủng hoảng |
| [SC-M05-008](SC-M05.md#sc-m05-008) | Kích hoạt lại Tag đã vô hiệu hóa |
| [SC-M05-009](SC-M05.md#sc-m05-009) | Đổi Topic và Tag trên bài viết của người khác |

## Kiểm tra đã thực hiện

Validator skill PASS cho main/E: sáu phần, metadata, UC/mapping/BF, actor/source ID, bước và đích, thay bước đúng chủ thể, luân phiên và đường đến terminal có hậu điều kiện. Main khởi đầu actor chính, kết thúc SYSTEM/SUCCESS của chức năng. UC002 gợi ý đi tiếp qua actor quyết tập cuối và lưu/gửi; UC012 được mở tại mọi điểm gọi, không che bằng câu gọi helper.

Các V nằm trong mục 6 của cùng scenario, thay toàn bộ đường theo Guest/User/Mod/Admin; kiểm riêng actor khởi tạo, tập actor hợp lệ, luân phiên và terminal có hậu điều kiện. Graph validator mặc định không đi V, nên PASS main/E không tự chứng minh các V. Sources trong V vẫn được validator đối chiếu.

Đã kiểm 148 mã có vị trí và từng dòng FR/BR/US với bước/quy tắc; so byte/hash FR hai vị trí; đọc năm SVG nguồn để đối chiếu tập UC; kiểm file/anchor ở thư mục đích. Không đổi FR/US/register/skill hoặc scenario module khác. Review này chưa là phê duyệt.

Lệnh chạy tại repo root:

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M05/SC-M05.md --fr docs/specs/fr/FR-M05.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M03.md --fr docs/specs/fr/FR-M06.md --fr docs/specs/fr/FR-M07.md --fr docs/specs/fr/FR-M08.md --fr docs/specs/fr/FR-M10.md --fr docs/specs/fr/FR-M13.md --fr docs/specs/fr/FR-M14.md --us docs/specs/us/US-M05.md
```

## Ma trận nghiệp vụ quan trọng

| Điều kiện | Kết quả đã viết |
|---|---|
| Gửi/lưu sửa Topic | 1–3 khác nhau, thuộc danh mục; 0/>3 hoặc Topic đã xóa không chốt hợp lệ |
| Lưu nháp | 0–3 Topic; gợi ý chưa cũ cũng không ghi phản hồi chỉ vì lưu nháp |
| Gợi ý AI | Bấm nút, ≥20 từ, ≤10/60 giây trượt, hai cờ bật, title+chữ không tệp; lọc danh mục |
| Gợi ý thất bại/tắt | Lỗi sau 2 lần thử10 giây cách 2 giây hoặc mọi Topic sai: báo lỗi không chặn/chọn thủ công; cờ tắt không gọi AI/không coi là lỗi |
| Phản hồi | Chỉ gửi/lưu sửa với lượt gần nhất chưa cũ; stale không ghi; DELETED giữ không danh tính |
| Tag | 0–5; ≤30 ký tự không#, chữ/số/_, có chữ; chuẩn hóa hoa thường giữ dấu; trùng dùng một; Tag mới hoạt động không duyệt |
| Tag vô hiệu | Không hiển thị/gợi ý/tìm/Trending; liên kết cũ giữ; nhập lại là chữ |
| Tag kích hoạt lại | Hiện liên kết cũ, không chuyển chữ thành Tag; Trending vẫn điểm>0/kỳ tính |
| Quyền Admin | Chỉ ACT007 thêm/gộp/xóa Topic; Mod không có quyền danh mục |
| Gộp/xóa Topic | Gộp mọi bài/follow không trùng rồi bỏ nguồn; xóa độc lập chỉ không bài ngoài nháp, bỏ liên kết nháp/follow |
| Điều phối bài người khác | Không dùng AI, không báo tác giả/không lịch sử sửa; log kiểm duyệt, Admin thêm log Admin |
| Trending | 7×24 giờ; bài+1, upvote bài+2, comment/reply+1, bookmark+1; chỉ feed chính; mỗi nhãn đủ điểm; không tính lượt xem/upvote comment/đã rút/Tag vô hiệu |

Các biến thể trạng thái/phương thức/quyền không tạo BF mới. Nhánh lỗi dữ liệu có sửa khi nguồn hỗ trợ, nhánh từ chối được US cho kết thúc thì dừng REJECTED, không bịa thử lại/hủy. Các guard độc lập áp lại khi kiểm tập cuối; không tuyên bố thứ tự báo lỗi cho tổ hợp nhiều lỗi chưa có nguồn. Ví dụ Trending được tính lại bằng các số cụ thể tại mục 5 của SC.

## Giới hạn còn giữ từ nguồn

NOTE-M05-01 chưa chốt UI hòa giải tập Topic cũ với gợi ý mới: bản soạn chỉ nêu gợi ý chọn sẵn và tập cuối do actor chốt, không tự cam kết thay/hợp tập. NOTE-M05-02 giữ kỳ tính/điểm dương; NOTE03 tách gộp và xóa; NOTE04 theo M07 hiện hành không thông báo bài Topic; NOTE05 không tự thêm log lần lặp không đổi, retry/rollback lỗi lưu/log. TBD01 SEO/SSR/preview và TBD02 view ngoài MS1. Không phát sinh quyết định mới hoặc che GAP chặn; nguồn US và kết quả vẫn cần review/phê duyệt.
