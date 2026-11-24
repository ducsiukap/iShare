# Ví dụ phương pháp — từ luồng đến quan hệ

[Vietnamese Doc]

**Fixture giả lập M99, không phải yêu cầu iShare hoặc tài liệu US để bàn giao.**
Không đưa các UC/mã nguồn dưới đây vào catalog dự án. Đây là ví dụ đọc tay,
không khai báo đã render và không dùng check_us.py với FR dự án cho M99.

## Nguồn giả lập đã cho

| Mã fixture | Hành vi |
|---|---|
| FR-M99-01.01 | Người có phiên yêu cầu xem hồ sơ; mỗi yêu cầu phải kiểm quyền đọc hiện tại. Không có quyền thì từ chối, không lộ nội dung. |
| FR-M99-01.02 | Được phép thì trả nội dung hồ sơ; không cần mở lịch sử để đạt mục tiêu đọc. |
| FR-M99-01.03 | Sau khi nội dung đã hiển thị, người đọc có thể yêu cầu xem lịch sử được phép rồi quay về hồ sơ. |
| FR-M99-01.04 | Hồ sơ lưu trữ tuân thủ cùng hợp đồng xem/kiểm quyền/không lộ dữ liệu; hiển thị thêm nhãn lưu trữ và phiên bản được lưu. |

Actor A là người dùng ngoài subject. “Có phiên” là precondition; kiểm quyền
hiện tại là hành vi trong luồng vì nguồn yêu cầu từ chối khi không đạt.

## Catalog và phân rã giả lập

| ID | Tên | Tier / level | Phạm vi/kết quả |
|---|---|---|---|
| UC-M99-020 | Tra cứu hồ sơ | core / Summary | Bao quát đọc hồ sơ thường/lưu trữ và lịch sử theo quyền; không bắt mọi con chạy cùng lượt |
| UC-M99-001 | Xem hồ sơ | sub / User goal | Nhận nội dung được phép hoặc kết quả từ chối không lộ nội dung |
| UC-M99-002 | Kiểm tra quyền đọc hồ sơ | sub / Subfunction | Trả quyết định quyền cho caller; tách để hợp đồng kiểm quyền dễ review |
| UC-M99-003 | Xem lịch sử hồ sơ | sub / User goal | Nhận lịch sử được phép sau yêu cầu riêng |
| UC-M99-004 | Xem hồ sơ lưu trữ | sub / User goal | Bảo toàn hợp đồng UC001, thêm nhãn và phiên bản lưu theo FR01.04 |

Mapping: UC020 → UC001, UC002, UC003, UC004. Đây là bảng đóng góp nghiệp vụ,
không phải bốn mũi tên include. Core bao quát nhiều mục tiêu, sub có kết quả
cụ thể. Một nơi gọi vẫn có thể tách hành vi có lý do rõ, không cần bịa nơi gọi thứ hai.

## Luồng và hợp đồng

**UC001:** Trigger yêu cầu xem hồ sơ; precondition có phiên và định danh hồ sơ.
Success nội dung được phép đã trả; failure từ chối không lộ nội dung theo nguồn.

1. Nhận yêu cầu và hồ sơ cần đọc.
2. Include UC002: caller cung cấp ngữ cảnh người đọc/hồ sơ; UC002 trả được phép
   hoặc không được phép. Được phép đi bước 3; không được phép END từ chối không
   lộ nội dung. Không tự thêm retry hoặc rollback.
3. Trả nội dung được phép. EP-READ-HISTORY tại sau hiển thị nội dung.
4. END đạt mục tiêu đọc. Không yêu cầu lịch sử vẫn đạt success.

**UC003:** Trigger yêu cầu lịch sử tại EP; guard đã xem nội dung, đang có quyền
xem lịch sử theo fixture. Trả lịch sử rồi quay UC001 bước 4. Không dùng chỉ
“cùng màn hình” làm bằng chứng extend. Quy tắc quyền lịch sử chi tiết ngoài
fixture được ghi thiếu nếu muốn đặc tả sâu, không suy ai cũng đọc được.

**UC004:** Kế thừa hợp đồng UC001 gồm kiểm quyền và kết quả không lộ nội dung khi
từ chối; chuyên biệt hóa bước trả nội dung bằng nhãn và phiên bản lưu. Không
nới quyền hoặc bỏ bước 2; cha UC001 concrete vẫn hợp lệ.

## Quyết định quan hệ

| Source → target | Loại | Chứng cứ/điểm chèn | Điều kiện và return |
|---|---|---|---|
| UC001 → UC002 | include | FR01.01; bước 2 bắt buộc gọi hợp đồng quyền | Không guard tùy chọn; được phép quay bước 3, từ chối END theo nguồn |
| UC003 → UC001 | extend | FR01.02–03; base đọc hoàn chỉnh độc lập, EP sau bước 3 | Người đọc yêu cầu lịch sử và có quyền; quay bước 4 |
| UC004 → UC001 | generalization | FR01.04; cùng hợp đồng quyền/kết quả, thêm nhãn/phiên bản | Không dùng EP/return của extend cho kế thừa |
| UC020 với các sub | Không suy cạnh từ mapping | Core chỉ đặt ngữ cảnh bao quát | Giữ node core và bảng phân rã |

Association A–UC001/UC003/UC004 là tham gia mục tiêu tương ứng; không tự vẽ
A–UC002 như một công việc độc lập chỉ vì caller truyền ngữ cảnh actor.

## Walkthrough và phản ví dụ

| Đường đi | Kết quả kiểm |
|---|---|
| UC001 → UC002 cho phép → bước 3 → bước 4 | Đạt đọc, không cần lịch sử |
| UC001 → UC002 từ chối → END | Đạt failure guarantee, không lộ nội dung |
| UC001 bước 3 → UC003 → bước 4 | Có guard/EP/return; success của base giữ nguyên |
| UC004 kế thừa luồng quyền → trả bản lưu | Bảo toàn hợp đồng UC001, không cấp thêm quyền |
| “Đã đăng nhập” nên UC001 include Đăng nhập | Sai suy luận: trạng thái có trước không chứng minh gọi hành vi |
| Mọi sub generalize UC020 vì cùng thuộc module | Sai suy luận: phân rã không phải hợp đồng kế thừa |

Khi sản xuất US thật, thay toàn bộ fixture bằng nguồn đã chốt, dùng đầy đủ ID
FR, anchor hợp lệ và bảng associations/relations theo template; render và kiểm
mỗi SVG thật trước khi khai báo pass. Ví dụ này không thay các bước đó.
