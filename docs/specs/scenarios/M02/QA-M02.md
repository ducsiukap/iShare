# QA-M02 — Tái kiểm sau khắc phục

[Vietnamese Doc] — 11/11/2026, skill scenarios v1.4. Trạng thái Đang soạn theo nguồn nghiệp vụ.

## Kết quả hiện hành

| Kiểm tra | Kết quả |
| --- | --- |
| Validator chuẩn | PASS 11 UC, 7 BF, 7 SC, 48 nhánh E |
| Chuẩn hóa biến thể | 8 nhánh từ ID V lịch sử đã đăng ký E tại M1, bảng chuyển đổi ở cuối SC |
| Bảo toàn nội dung | 89 bước main/E/V lịch sử được đối chiếu trước/sau, chỉ đổi ID nhánh, vị trí dẫn và dữ liệu đã xác nhận trong QA-SC-02/03 |
| Phạm vi kiểm máy | Actor/nguồn, guard đăng ký, điểm thay/điểm vào, đích bước, luân phiên, khả năng kết thúc và hậu điều kiện của toàn bộ main/E |
| GAP và phê duyệt | Các GAP nguồn còn mở được liệt kê trong SC và báo cáo tái kiểm toàn bộ, đầu ra giữ Đang soạn |


Bản hiện hành [SC-M02.md](SC-M02.md). Kết quả toàn bộ và các quyết định còn chờ ở [báo cáo khắc phục](../QA-M01-M16-2026-11-11-khac-phuc.md).

## Bằng chứng lần soạn trước

Phần dưới lưu báo cáo của chính module này trước ngày chuyển đổi. Các số E/V và nhận xét giới hạn validator trong phần lịch sử phản ánh công cụ lúc soạn. Số liệu và kết quả áp dụng hiện tại nằm ở mục Kết quả hiện hành, các biến thể đã được kiểm bằng hợp đồng E.

# Kết quả triển khai và kiểm tra scenario M02 User Profile

[Vietnamese Doc] — 2026-11-08 — Skill scenarios v1.3 — Đang soạn để review.

Đầu ra chính: [SC-M02.md](SC-M02.md). Phạm vi là toàn bộ catalog và phân rã
US-M02, theo FR-M02 v1.6 đã chốt; US-M02 và US-overview vẫn Chờ duyệt.

| Hạng mục | Kết quả |
|---|---|
| Mô hình nguồn | 3 UC chính, 8 UC con, 9 mapping |
| Cách bao phủ | 3 aggregate, 7 UC sở hữu mục tiêu actor, 1 embedded (UC008) |
| Hành trình chức năng | 7 BF / 7 scenario, mỗi scenario đủ sáu phần |
| Nhánh cùng actor chính | 40 đường E, có dữ liệu và bước tiếp nối/đích |
| Đường thay thế actor Guest | 8 đường V, thay toàn bộ đường chính của cùng chức năng; không tạo BF mới |
| Quy tắc nền/giao tiếp | 3 AUT và 4 RULE, không có scenario chỉ SYSTEM |
| Truy vết M02 | 116 mã: 7 nhóm + 72 FR chi tiết + 37 BR, đều có vị trí triển khai |
| Sơ đồ nguồn | Đã đối chiếu tập ID UC trong 4 SVG với bảng uc:diagrams; khớp |
| Vị trí đầu ra | docs/specs/scenarios/M02/; chỉ tạo thư mục module đang làm |

## Các hành trình

| Scenario | Ranh giới chức năng |
|---|---|
| [SC-M02-001](SC-M02.md#sc-m02-001) | Actor yêu cầu hồ sơ → hệ thống phân giải, lọc nội dung và trả hồ sơ đúng ngữ cảnh; gồm các nhánh Guest, người khác, trạng thái đích, tab Đã xóa và mở rộng xem mạng lưới |
| [SC-M02-002](SC-M02.md#sc-m02-002) | Actor chọn số theo dõi → nhận danh sách đúng hướng, lọc trạng thái và thứ tự; không thực hiện Follow/Unfollow |
| [SC-M02-003](SC-M02.md#sc-m02-003) | Actor mở sửa → nhập dữ liệu/có bộ đếm → gửi → hệ thống kiểm tra, lưu và trả kết quả; có đường sửa lỗi và nhập lại |
| [SC-M02-004](SC-M02.md#sc-m02-004) | Actor gửi ảnh → hệ thống kiểm, lưu gốc, đặt avatar, xóa ảnh tải lên cũ sau thành công và trả avatar mới |
| [SC-M02-005](SC-M02.md#sc-m02-005) | Actor chọn lưu → hệ thống tạo đúng một bookmark cá nhân và trả kết quả; không bật thông báo |
| [SC-M02-006](SC-M02.md#sc-m02-006) | Actor chọn bỏ lưu → hệ thống xóa bookmark của chính actor, giữ bài gốc; gồm dòng thay thế và bài Khóa toàn bộ |
| [SC-M02-007](SC-M02.md#sc-m02-007) | Actor mở Bookmark → hệ thống kiểm chủ, lọc/giữ dòng thay thế và trả danh sách theo thời điểm lưu; có mở rộng bỏ lưu ngay trong danh sách |

UC008 được khai triển trong lượt SYSTEM của SC001/007. Hai quan hệ extend
được giữ: UC002 → UC001 tại EP-PROFILE-FOLLOW; UC006 → UC007 tại
EP-BOOKMARK-REMOVE. Cả hai điểm gọi có các bước actor/hệ thống tại chỗ,
không dừng ở câu “thực hiện UC-X”. Các chức năng xem mạng lưới và bỏ lưu
vẫn có scenario độc lập vì được yêu cầu riêng theo nguồn.

## Kiểm tra

Validator của skill kiểm 7 SC và 40 nhánh E: **PASS, không có lỗi cấu trúc**.
Các luồng chính bắt đầu bằng actor chính, có tương tác hai phía và kết thúc
bằng SYSTEM trả SUCCESS. Bước lỗi/sửa có đích quay lại đúng bước kiểm;
nhánh từ chối kết thúc theo US, không tự thêm thao tác OK/thử lại.

Tám đường V xử lý thay đổi actor khởi tạo sang Guest. Chúng được viết ngay
trong mục 6 của scenario bao chứa, giữ các bước có chủ thể/dữ liệu/đích/nguồn
riêng; không nối một bước Guest vào giữa đường chính đang có User. Đã kiểm
riêng đường V bắt đầu ACT-001, trả SYSTEM, chủ thể liền kề khác nhau và có
hậu điều kiện tương ứng. **Validator graph mặc định chỉ duyệt bảng E/main;
kết quả PASS không tự chứng minh graph của các bảng V.** Nguồn ID trong bảng
V vẫn được validator đối chiếu cùng các bảng nguồn khác.

Các đối soát khác: hash FR chính thức khớp bản làm việc chung; 116 mã M02 có
đích SC/bước/nhánh/quy tắc; bốn SVG không thiếu/thừa ID thành viên; link
file/anchor tại vị trí đầu ra được kiểm trước bàn giao. Đây là kiểm kỹ thuật
và review của agent, chưa phải phê duyệt nghiệp vụ độc lập.

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M02/SC-M02.md --fr docs/specs/fr/FR-M02.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M03.md --fr docs/specs/fr/FR-M11.md --fr docs/specs/fr/FR-M12.md --fr docs/specs/fr/FR-M16.md --us docs/specs/us/US-M02.md
```

## Các lớp dữ liệu và giới hạn

| Trường hợp | Cách bao phủ |
|---|---|
| Hồ sơ chủ/người khác/Guest | Nội dung, tab và Nhắn tin khác nhau trong cùng mục tiêu xem; không nhân BF theo quyền |
| Username URL | Khác hoa/thường vẫn phân giải; tên cũ chưa ai nhận trả không tồn tại; đã được nhận lại mở chủ hiện hành |
| Bài ở hồ sơ | Bài công khai/Private được phép và bài riêng của chủ được lọc cụ thể; không dùng placeholder Bookmark cho Bài viết |
| Theo dõi | Hai hướng quan hệ, lọc BANNED/DEACTIVATED, ACTIVE trở lại, danh sách rỗng; thời điểm bắt đầu theo dõi không bị thay |
| Bio/tên/Lớp | Bio 156 bị từ chối rồi sửa 155; trim/emoji/xuống dòng, trống và bỏ chọn Lớp; tên đúng quy tắc M01, không tự hạn chế số lần đổi |
| Avatar | PNG/JPEG/WebP hợp lệ đến 5 MB; GIF/loại khác và ảnh quá 5 MB bị từ chối; ảnh gốc tách với hiển thị cắt tròn |
| Bookmark | Lưu mới/trùng, Khóa toàn bộ vẫn lưu/bỏ được; dòng tạm không xem được khác với xóa hẳn hoặc tác giả DELETED; phục hồi khả năng xem giữ thời điểm lưu |
| Cờ Group/Chat | Giữ lối vào/danh sách theo FR-M02 5.11; mở bài/trò chuyện do module sở hữu xử lý, không tự ẩn/xóa dữ liệu vì cờ tắt |

GAP-SC-M02-001: chưa rõ bộ đếm lúc đang gõ có trim tức thời hay không;
con số 12 trong dữ liệu là số dùng kiểm khi lưu. Đường nhập/sửa/lưu được
viết đầy đủ, chưa tự chốt cách bộ đếm hiển thị chuỗi có khoảng trắng đầu/cuối.

Hình thức avatar mặc định, retry/rollback lưu ảnh, UX lỗi mạng và bỏ lưu
bookmark vốn không tồn tại chưa có hợp đồng nguồn. Không tự thêm chúng.
Không có chức năng Mod/Admin sửa/gỡ bio hoặc avatar người khác, cũng không
triển khai đăng nhập, Follow, Chat, khôi phục bài, tính điểm hoặc Trending
trong M02. Các giá trị hiển thị/ảnh/thời điểm đều là dữ liệu giả lập.

Phê duyệt: **Chưa có**. Giữ bản soạn tại đích người dùng đã yêu cầu.
