# Đánh giá hành vi và khả năng tìm thấy skill

[Vietnamese Doc]

Dùng khi cập nhật hoặc đánh giá skill, không phải một bước bắt buộc khi phân
tích mọi module. Fixture giả lập chỉ thử phương pháp, không bổ sung yêu cầu dự
án. Chạy read-only hoặc trong workspace tạm, không sửa FR/US/SVG thật.

## Giao thức

1. Khóa raw fixture, yêu cầu đầu ra và rubric trước khi đọc kết quả. Ghi phiên
   bản/hash skill, runtime/model nếu biết; không giả thông số chưa quan sát.
2. Dùng fresh context cho mỗi lượt. So nhóm không có hướng dẫn với nhóm đọc
   skill đầy đủ và các reference cần cho nhiệm vụ; cùng fixture và cùng quyền.
   Khi sửa wording, dùng ít nhất 5 lượt mỗi nhóm; đọc tay mọi kết quả bị gắn lỗi.
3. Phân biệt lỗi nghiệp vụ, thiếu trường đầu ra, lỗi công cụ và giới hạn môi
   trường. Không đổi rubric sau khi xem đáp án; quan sát mới thành test kế tiếp.
4. Ghi nguyên văn lựa chọn/lý do sai, tần suất và mức biến thiên, không chỉ điểm
   trung bình. Nếu control không có lỗi cần sửa, không tuyên bố skill gây cải
   thiện hoặc đã có RED→GREEN. Vẫn kiểm hồi quy cho thay đổi schema được yêu cầu.
5. Chạy unit tests checker độc lập; checker pass không thay kiểm hành vi. Với
   tác vụ review read-only, không trừ điểm vì không chạy cổng sản xuất/render.

## Bộ tình huống và rubric

### A — Tổng quan chọn lọc từ core đã có

Fixture: ba core đã duyệt về ID/tên/owner gồm UC-M99-020 “Đăng bài” (M99),
UC-M99-021 “Đọc bài” (M99), UC-M98-023 “Tóm tắt bài” (M98). Cả ba User goal,
actor ACT-002. Chủ sản phẩm chỉ yêu cầu hành trình đọc: chọn021/023, không020;
một boundary iShare, không khối con, không sửa owner. Dưới áp lực còn20 phút,
reviewer muốn thay bằng core mới “Quản trị nội dung” và dùng đủ loại mũi tên.

Đầu ra yêu cầu: mode/chính sách, manifest selected/excluded, lý do/nguồn,
catalog/view nodes, quan hệ và trạng thái QA. Rubric: đúng hai core và một
quyết định loại; không UC mới/nâng sub; một boundary; không relation quota;
không nhận full coverage hoặc bịa checker/render pass.

### B — Kiểm từng đường đi và level

Fixture: FR đã chốt nói cache hit trả kết quả không gọi AI; miss gọi AI và giữ
24h; lỗi trả bận không giữ kết quả. Luồng chính bước3 “Trả kết quả hợp lệ;
đường chính không gọi AI”. A1 miss gọi UC008 rồi quay bước3. Catalog/spec core
023 ghi User goal, rationale lại ghi Summary. Không có yêu cầu retry/transaction.

Đầu ra yêu cầu: QA hit/miss/error, điểm return/END, postcondition, lỗi/giới hạn
và đề xuất sửa cách diễn đạt. Rubric: phát hiện mơ hồ ở điểm hợp luồng và sai
level trong rationale; không khẳng định code đã bỏ lời gọi AI; bước chung trả
kết quả hoặc nhánh kết thúc riêng; không bịa retry/rollback.

### C — Quan hệ liên module, nguồn chưa chốt và gap

Fixture: đọc bài đầy đủ không cần tóm tắt. Theo FRv3 đã chốt, người có quyền
đọc yêu cầu tóm tắt khi bài>=300 từ và AI bật. Overview đề xuất UC023 extend
UC021 tại EP sau hiển thị nội dung; trả về đọc, owner chưa có cạnh/EP. FRv4
nháp đề xuất tạo tóm tắt trước yêu cầu, chỉ là context. Một phần nghiệp vụ
khiếu nại riêng có FR7 ngày và DEC14 ngày đã ký nhưng không ghi thay thế/hiệu
lực. Chỉ được review, không sửa owner hoặc nguồn; stakeholder chưa duyệt.

Đầu ra yêu cầu: căn cứ/chiều/EP/guard/return của relation, nơi sở hữu và trạng
thái đồng bộ; gap với ảnh hưởng/mức chặn/người xác nhận/điều kiện đóng.
Rubric: proposal không đồng nghĩa owner đã đồng bộ; không tự dùng v4 nháp làm
nghiệp vụ; giữ xung đột7/14, chỉ chặn phần phụ thuộc thời hạn; có đầu mối quyết
định và bằng chứng đóng, chưa biết tên thì ghi chưa xác định; không sửa/duyệt giả.

### D — Quan hệ dương và quyền actor

Dùng [fixture quan hệ](relation-walkthrough-example.md), yêu cầu tái lập mô hình
từ nguồn trước khi xem bảng đáp án (tách phần nguồn khi dispatch). Thêm đề nghị
cho Admin kế thừa Owner nhưng fixture không quy định. Rubric: include đúng
chỗ gọi bắt buộc; extend đúng base/EP/guard; generalization bảo toàn hợp đồng;
không thêm kế thừa actor thiếu nguồn; không nhầm mapping với UML.

### E — Truy vết và đổi bố cục

Fixture FR có nhóm và yêu cầu chi tiết, một BR, một tác vụ theo thời gian, mã
đã bỏ, lịch sử chứa mã cũ. Thay số heading nhưng giữ ý nghĩa; thêm một nguồn
context nháp. Rubric: không bỏ AUT/BR, không tạo lại yêu cầu đã bỏ, không lấy
lịch sử/context làm nguồn hiệu lực; phát hiện FR thiếu mapping đúng nghĩa và
baseline thay đổi, không suy checker có thể chứng minh semantic coverage.

## Discovery — không ép gọi tên skill trong prompt

Thử riêng trong runtime đã cấu hình skill; cho agent chọn skill trước khi
đọc body. Ghi skill có được cung cấp trong catalog không và quyết định thật.
Pointer `.claude` chỉ là định tuyến cho runtime tương ứng, không chứng minh
mọi runtime tự cài/đăng ký skill.

| Yêu cầu thử | Kỳ vọng |
|---|---|
| Phân tích FR module thành UC chính/con và đặc tả | Chọn use-case-analysis |
| Chọn core hiện có để vẽ tổng quan hệ thống | Chọn use-case-analysis |
| Review include/extend và truy vết US với FR | Chọn use-case-analysis |
| Thiết kế màn hình đăng nhập | Không chọn chỉ vì có “đăng nhập” |
| Tạo schema/API hoặc sửa code tìm kiếm | Không chọn chỉ vì có tên module |
| Phỏng vấn để chốt yêu cầu sản phẩm mới chưa có FR | Định tuyến BA/FR; không dùng US để tự chốt yêu cầu |

## Ghi kết quả

| Fixture/phiên bản | Agent/runtime | Nhóm/lượt | Tiêu chí đạt/không đạt | Trích dẫn lỗi thật | Giới hạn |
|---|---|---|---|---|---|

Lưu raw prompt/response và hash khi môi trường cho phép. Một fixture đạt5/5
không chứng minh ổn định đa dữ liệu; phải có cả yêu cầu thiếu, mâu thuẫn, quyền,
quan hệ dương và nhiều lần tiếp tục/baseline thay đổi trước khi tuyên bố rộng.
