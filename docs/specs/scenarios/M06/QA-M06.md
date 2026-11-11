# QA-M06 — Tái kiểm sau khắc phục

[Vietnamese Doc] — 11/11/2026, skill scenarios v1.4. Trạng thái Đang soạn theo nguồn nghiệp vụ.

## Kết quả hiện hành

| Kiểm tra | Kết quả |
| --- | --- |
| Validator chuẩn | PASS 12 UC, 6 BF, 6 SC, 88 nhánh E |
| Chuẩn hóa biến thể | 18 nhánh từ ID V lịch sử đã đăng ký E tại M1, bảng chuyển đổi ở cuối SC |
| Bảo toàn nội dung | 215 bước main/E/V lịch sử được đối chiếu trước/sau, chỉ đổi ID nhánh, vị trí dẫn và dữ liệu đã xác nhận trong QA-SC-02/03 |
| Phạm vi kiểm máy | Actor/nguồn, guard đăng ký, điểm thay/điểm vào, đích bước, luân phiên, khả năng kết thúc và hậu điều kiện của toàn bộ main/E |
| GAP và phê duyệt | Các GAP nguồn còn mở được liệt kê trong SC và báo cáo tái kiểm toàn bộ, đầu ra giữ Đang soạn |


Bản hiện hành [SC-M06.md](SC-M06.md). Kết quả toàn bộ và các quyết định còn chờ ở [báo cáo khắc phục](../QA-M01-M16-2026-11-11-khac-phuc.md).

## Bằng chứng lần soạn trước

Phần dưới lưu báo cáo của chính module này trước ngày chuyển đổi. Các số E/V và nhận xét giới hạn validator trong phần lịch sử phản ánh công cụ lúc soạn. Số liệu và kết quả áp dụng hiện tại nằm ở mục Kết quả hiện hành, các biến thể đã được kiểm bằng hợp đồng E.

# Kết quả kiểm tra scenario M06 Search

[Vietnamese Doc] — 2026-11-09 — Skill scenarios v1.3 — Đang soạn để review.

Đầu ra chính: [SC-M06.md](SC-M06.md).

| Hạng mục | Kết quả |
|---|---|
| Mô hình | 3 UC chính, 9 UC con, 11 mapping, 9 quan hệ |
| Disposition | 2 aggregate; 5 UC sở hữu chức năng (core020, UC001/004/005/009); 5 embedded (UC002/003/006/007/008) |
| BF/SC | 6 hành trình hoàn chỉnh; UC005 có chức năng xem và gửi lại độc lập |
| Nhánh E | 70 |
| Đường actor V | 18 |
| Quy tắc nền | 2 AUT +3 RULE nguồn +3 hợp đồng rate/rank/filter được mở rộng từ nguồn, không BF mới |
| Truy vết | 5 nhóm +85 FR chi tiết +25 BR =115 mã |
| Sơ đồ nguồn | 4 SVG khớp tập ID gồm node tham chiếu, không tuyên bố render mới |
| Baseline | FR 1.5 Đã chốt, khớp byte bản làm việc; US/overview Chờ duyệt |
| Đích | docs/specs/scenarios/M06, chỉ tạo thư mục module đang làm |

## Sáu chức năng actor

| SC | Mục tiêu |
|---|---|
| [SC-M06-001](SC-M06.md#sc-m06-001) | Tra cứu nhanh tên thực thể khi gõ |
| [SC-M06-002](SC-M06.md#sc-m06-002) | Gửi truy vấn và khai thác trang kết quả tìm kiếm |
| [SC-M06-003](SC-M06.md#sc-m06-003) | Lọc, sắp xếp và xem bài theo Topic hoặc Tag |
| [SC-M06-004](SC-M06.md#sc-m06-004) | Xem lịch sử tìm kiếm trên trình duyệt |
| [SC-M06-005](SC-M06.md#sc-m06-005) | Gửi lại truy vấn được chọn từ lịch sử |
| [SC-M06-006](SC-M06.md#sc-m06-006) | Xóa toàn bộ lịch sử tìm kiếm trên trình duyệt |

## Kiểm tra thực hiện

Validator skill PASS cho main/E: đủ 6 phần, UC/actor/source ID, mapping, BF/SC, điểm thay bước, luân phiên và đích kết thúc có hậu điều kiện. Main bắt đầu actor chính và kết thúc SYSTEM/SUCCESS. Đã kiểm riêng V theo actor khởi tạo, tập actor, thứ tự bước/luân phiên và terminal; graph validator mặc định không duyệt V nên PASS main/E không tự chứng minh V.

Đối chiếu 115 mã nguồn với vị trí và nội dung, byte/hash FR chính thức/bản làm việc, 4 SVG khớp ID/mapping, liên kết file/anchor ở đích. Phép tính raw/norm/điểm final dữ liệu mẫu được tính lại, đoạn trích 150 giữa từ kiểm vị trí. Review nghiệp vụ dựa FR/US, không là phê duyệt stakeholder. Không sửa nguồn/skill hoặc module khác.

Kiểm tra bổ sung: **18 đường V**, **26 liên kết file/anchor**, **11 SHA-256 nguồn** và **115 mã truy vết** đều đạt. Dữ liệu full-text dùng từ “toán” chữ thường trong title P601 để minh họa bỏ dấu mà không suy thêm quy tắc phân biệt hoa/thường chưa được FR full-text nêu rõ.

Lệnh từ repo root:

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M06/SC-M06.md --fr docs/specs/fr/FR-M06.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M03.md --fr docs/specs/fr/FR-M04.md --fr docs/specs/fr/FR-M05.md --fr docs/specs/fr/FR-M07.md --fr docs/specs/fr/FR-M10.md --fr docs/specs/fr/FR-M11.md --fr docs/specs/fr/FR-M13.md --us docs/specs/us/US-M06.md
```

## Các điểm nghiệp vụ đã đối soát

| Điều kiện | Đường hoàn tất |
|---|---|
| Chưa gửi | Gợi ý sau 300 ms từ 1 ký tự, tối đa 3 mỗi loại, không bài/AI/history |
| Có chữ | Một trang bài+tên phụ, Guest full-text; User semantic nếu 2 cờ bật; chỉ 1 lượt gửi |
| AI lỗi | 5 giây/lần, 1 retry sau 2 giây; full-text riêng query, lượt sau semantic khi đủ điều kiện |
| Full-text | Bỏ dấu cả 2 phía, ≥1 từ khớp; độ liên quan theo tỷ lệ từ, không comment/tệp |
| Quyền | Private chỉ thành viên cả với Mod/Admin; tài khoản chỉ ACTIVE+xong Bước 3; Tag vô hiệu không tên |
| BANNED/HEAVY | Bài BANNED giữ/nhãn khi hiện tên, tài khoản không tìm được; HEAVY ×0.5 chỉ Liên quan/không lộ |
| Lọc/sort | AND, 1 mỗi loại; Following tác giả hoặc Topic, ẩn danh chỉ Topic; không lọc tên phụ |
| Top 120 | Theo liên quan trước sort, không đổi sang 120 bài upvote nhất; vẫn giữ NOTE 01 về lọc |
| Rỗng có lọc | Mọi bài khớp, Mới nhất mặc định, Upvote được, không AI/Liên quan/trần 120/tên phụ |
| Cuộn | 15/lô, không trùng/thiếu; đủ 120 rồi cuộn tiếp mới báo thu hẹp; rỗng có lọc tải đến 130 |
| Rate | Guest IP 30 gợi ý/10 gửi; tài khoản 45/20; 60 giây trượt, cuộn không lượt, từ chối riêng lượt |
| History | 10 chuỗi trên trình duyệt, trùng lên đầu, mục 11 bỏ cũ nhất, chọn gửi ngay; cập nhật theo sự kiện kể cả rate từ chối; logout/xóa toàn bộ xóa ở trình duyệt này |

Xem history được hoàn tất bằng danh sách; gửi lại chỉ hoàn tất sau trang kết quả, không dừng ở điền ô/gọi UC. UC009 không có ngoại lệ nguồn: không bịa modal/hủy/retry/xóa riêng từng mục. Lỗi độ giống/tệp/bình luận không tạo nhánh từ chối sản phẩm mới; chỉ giới hạn đúng phạm vi tìm.

## Phần còn giới hạn từ nguồn

NOTE-M06-01 chưa chốt lọc so với Top 120; NOTE 02 so trùng history không chốt case/trim/dấu; NOTE 03 ổn định phân trang và khóa hòa cuối; NOTE 04 dùng Following FR 1.5 thay phụ lục Q12 cũ; TBD 01 hoãn SEO/SSR. Không quy định HMI/lỗi ghi cục bộ nên không tự thêm. Các ràng buộc đã chốt vẫn được viết, nhưng tài liệu chưa thay đặc tả thiết kế/API và chưa được duyệt cuối.
