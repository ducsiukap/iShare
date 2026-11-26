# QA-M01 — Tái kiểm sau khắc phục

[Vietnamese Doc] — 11/11/2026, skill scenarios v1.4. Trạng thái Đang soạn theo nguồn nghiệp vụ.

## Kết quả hiện hành

| Kiểm tra | Kết quả |
| --- | --- |
| Validator chuẩn | PASS 25 UC, 11 BF, 11 SC, 221 nhánh E |
| Chuẩn hóa biến thể | M01 tiếp tục dùng 221 nhánh E đã đăng ký trong hợp đồng chuẩn |
| Bảo toàn nội dung | 990 bước main/E/V lịch sử được đối chiếu trước/sau, chỉ đổi ID nhánh, vị trí dẫn và dữ liệu đã xác nhận trong QA-SC-02/03 |
| Phạm vi kiểm máy | Actor/nguồn, guard đăng ký, điểm thay/điểm vào, đích bước, luân phiên, khả năng kết thúc và hậu điều kiện của toàn bộ main/E |
| GAP và phê duyệt | Các GAP nguồn còn mở được liệt kê trong SC và báo cáo tái kiểm toàn bộ, đầu ra giữ Đang soạn |


Bản hiện hành [SC-M01.md](SC-M01.md). Kết quả toàn bộ và các quyết định còn chờ ở [báo cáo khắc phục](../QA-M01-M16-2026-11-11-khac-phuc.md).

## Bằng chứng lần soạn trước

Phần dưới lưu báo cáo của chính module này trước ngày chuyển đổi. Các số E/V và nhận xét giới hạn validator trong phần lịch sử phản ánh công cụ lúc soạn. Số liệu và kết quả áp dụng hiện tại nằm ở mục Kết quả hiện hành, các biến thể đã được kiểm bằng hợp đồng E.

# Kết quả sửa scenario M01 theo scenarios v1.3

[Vietnamese Doc] — 2026-11-08 — Đang soạn để review, chưa phê duyệt.

Đầu ra chính: [SC-M01.md](SC-M01.md). Bản sửa xác định lại đơn vị luồng
theo chức năng actor thực hiện hoàn chỉnh với hệ thống; bảng đối chiếu ở
mục 6 giữ dấu vết của cả 60 ID scenario trước đây.

| Hạng mục | Kết quả |
|---|---|
| Catalog nguồn | 6 UC chính + 19 UC con; giữ 20 mapping |
| Cách xử lý | 11 UC sở hữu hành trình, 9 UC embedded, 4 aggregate, 1 abstract |
| Luồng chức năng | 11 BF / 11 scenario sáu phần |
| Ngoại lệ / đường thay thế | 221 đường có bước, dữ liệu và đích; gồm phương thức, ngữ cảnh, trạng thái, lỗi và lựa chọn |
| Hành vi nền | 12 mục quy tắc/hiển thị; không có scenario phụ chỉ SYSTEM |
| Truy vết | 172 FR chi tiết + 47 BR + 16 nhóm: đều có vị trí SC/bước/nhánh hoặc quy tắc nền |
| Giới hạn nguồn | Giữ 8 GAP-SC và TBD-M01-01/OPEN-008; chưa coi là hoàn chỉnh các đoạn thiếu nguồn |

Số nhánh không phải số chức năng. Các nhánh chứa đường thay thế đầy đủ để
đọc độc lập, có thể lặp phần chung; chúng không tạo thêm BF. Các snapshot
dữ liệu của những nhánh khác nhau không chạy đồng thời trong một lần thực thi.

## Các hành trình sau khi sửa

| Scenario | Chức năng actor hoàn thành |
|---|---|
| [SC-M01-001](SC-M01.md#sc-m01-001) | Đăng ký đến hoàn tất tài khoản; email/Google, xác minh, gửi lại và thiết lập nằm trong hành trình |
| [SC-M01-007](SC-M01.md#sc-m01-007) | Đăng nhập; xử lý phương thức, cổng trạng thái, liên kết Google, đăng ký còn dở và quyết định chính sách khi cần |
| [SC-M01-014](SC-M01.md#sc-m01-014) | Đăng xuất thiết bị hiện tại, giữ phiên thiết bị khác và xóa lịch sử tìm kiếm trình duyệt |
| [SC-M01-017](SC-M01.md#sc-m01-017) | Đổi mật khẩu khi có phiên |
| [SC-M01-018](SC-M01.md#sc-m01-018) | Lấy lại mật khẩu đến khi mật khẩu mới và phiên mới được xử lý; có nhánh BANNED |
| [SC-M01-022](SC-M01.md#sc-m01-022) | Tự vô hiệu hóa tài khoản đến khi trạng thái, phiên và hiển thị được cập nhật |
| [SC-M01-023](SC-M01.md#sc-m01-023) | Kích hoạt lại bằng OTP; gửi lại/sai/hết hạn nằm trong cùng hành trình |
| [SC-M01-025](SC-M01.md#sc-m01-025) | Mod/Admin yêu cầu và nhận bài ẩn/danh tính DEACTIVATED trong quyền cho phép |
| [SC-M01-034](SC-M01.md#sc-m01-034) | Chèn lượt nhắc vào bản soạn; ngữ cảnh bài/bình luận, trong/ngoài Group và thao tác khối là nhánh |
| [SC-M01-037](SC-M01.md#sc-m01-037) | Xem chính sách công khai, gồm đường đọc từ điểm đăng ký rồi trở về |
| [SC-M01-039](SC-M01.md#sc-m01-039) | Xử lý chính sách hiện hành: đồng ý, không hỏi lại, hoặc từ chối với các đường thoát cụ thể |

Không tái đánh số liên tục: giữ ID đại diện từ bản trước, các ID gộp được
ngừng dùng làm scenario độc lập. Danh mục UC embedded chỉ rõ vị trí thực
hiện trong các SC bao chứa. Không sửa mô hình hoặc trạng thái duyệt FR/US.

## Kiểm tra đã thực hiện

- Validator v1.1: PASS, 25 UC / 11 BF / 11 SC / 221 ngoại lệ; không có lỗi cấu trúc.
- Tất cả luồng chính bắt đầu từ actor chính, có cả actor và SYSTEM, kết thúc bằng SYSTEM/SUCCESS.
- Sáu phần, chủ thể, nhánh thay thế, điểm nhập lại, đường kết thúc, nguồn FR/BR và mapping UC được máy kiểm.
- Không còn marker scenario phụ AUT/RULE/email sáu phần; tác vụ nền ghi trigger, điều kiện, hiệu ứng và nguồn.
- 20 liên kết file/anchor trong tài liệu chính đã kiểm: không có đích hỏng.
- Review ranh giới mục tiêu: đăng ký không dừng ở gửi email; lấy lại mật khẩu không dừng ở gửi link; đăng nhập còn dở tiếp tục xác minh/thiết lập. Công khai nội dung và xét khiếu nại thuộc module sở hữu; không tuyên bố M01 đã hoàn tất các mục tiêu đó.

Lệnh kiểm tra từ repo root:

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M01/SC-M01.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M02.md --fr docs/specs/fr/FR-M06.md --fr docs/specs/fr/FR-M07.md --fr docs/specs/fr/FR-M09.md --us docs/specs/us/US-M01.md
```

## Các điểm còn cần chốt

Chi tiết nằm tại mục 8 của SC-M01: nhập lại mật khẩu lúc đăng ký;
phiên chuyển tiếp trước hoàn tất đăng ký; thứ tự side effect liên kết
Google với bảo trì; đúng ranh giới hết hạn; hiệu lực OTP cũ/bộ đếm sau gửi
lại; fuzzy/phá hòa gợi ý; lỗi/hủy Google; lỗi gửi email giao dịch.
TBD/OPEN còn câu chữ chính sách, liên hệ và yêu cầu bản sao dữ liệu.

PASS không chứng minh các GAP đã được giải quyết hoặc mọi nhánh đúng ngữ
nghĩa. Đặc biệt GAP phiên chuyển tiếp ảnh hưởng việc chốt tính đầy đủ của
đăng ký/đăng nhập còn dở. Bản này tiếp tục là bản soạn để người dùng review.
