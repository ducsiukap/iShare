# Kiểm soát chất lượng mô hình và vòng đời quyết định

[Vietnamese Doc]

Đọc cùng modeling-rules khi chốt catalog, luồng, quan hệ và review cuối.
Đây là quy trình kiểm chứng, không cung cấp tính năng sản phẩm.

## 1. Hợp đồng phạm vi và tổng quan

Ghi mode, module, baseline, đầu ra được yêu cầu và quyền sửa file. Với overview,
chọn một chính sách `overview_selection`:

| Chính sách | Tập UC được vẽ | Điều kiện hoàn tất |
|---|---|---|
| full | Toàn bộ core của các module trong module-models | Mọi core nguồn có mặt, giữ ID/tên/owner/level/actor/nguồn |
| selected | Tập con core nguồn theo mục tiêu người dùng | Mỗi core nguồn có quyết định selected/excluded, lý do và căn cứ; catalog/view đúng tập selected |

Bảng `overview-selection` kiểm kê cả core không vẽ; không coi core không vẽ là
nghiệp vụ bị xóa. Lý do chọn xét mục tiêu actor, kết quả nghiệp vụ, mức tổng
quan và độ dễ đọc. Không tạo core thay thế, nâng sub hoặc đổi endpoint của
relation chỉ để hiện trên hình. Muốn đổi phạm vi core nguồn là việc riêng.

Selected chỉ truy vết phạm vi được biểu diễn. Phần không vẽ trỏ về module và
quyết định excluded, không tự đánh Đủ cho toàn bộ FR. Các nhóm FR nằm ở core
nguồn được chọn phải có mapping; cùng một nhóm FR có thể được chia giữa nhiều
core, nên BA phải đọc phần hành vi thực sự được chọn, không suy bao phủ từ mã.

Tổng quan hệ thống dùng đúng một boundary iShare, actor bên ngoài, oval bên
trong, không package/khối module con. Quan hệ có endpoint không chọn vẫn ở
module owner; ghi tham chiếu ngoài hình. Không đủ dữ liệu nguồn thì ghi thiếu.

## 2. Actor–mục tiêu và chất lượng phân rã

Với mỗi ứng viên, ghi actor khởi phát/nhận giá trị, trigger, kết quả quan sát
được, nguồn và ranh giới công việc. Phân biệt vai trò với trạng thái tài khoản,
RBAC và quan hệ thành viên; không suy quyền Owner từ Admin hệ thống.

Với mỗi core/sub, đối chiếu **goal, trigger, kết quả và phạm vi**:

- Sub đóng góp phần nào cho mục tiêu core? Có thể giải thích bằng hành vi nguồn?
- Core có phạm vi/giá trị bao quát thực sự hay chỉ đổi từ đồng nghĩa của sub?
- Hai UC có cùng actor, trigger, kết quả và cùng phạm vi thì rà gộp/trùng lặp.
- Các phần khác nhau chỉ vì nút/form/API thường ở luồng; kết quả khác biệt có
  thể cần UC riêng. Không gộp mọi CRUD chỉ vì chung đối tượng.
- Mapping 1:1 không tự sai; phải ghi khác biệt phạm vi hoặc lý do quy ước hai
  tầng. Không tìm được khác biệt có căn cứ thì ghi vấn đề mô hình cần review,
  không bịa thêm hành vi để đủ sub.

Tên UC phản ánh hợp đồng thật; đối chiếu quy chuẩn tên hiện có và trạng thái
phê duyệt. Không đổi scope chỉ để làm tên ngắn. Review cùng ID ở catalog,
brief/spec, bảng quyết định, trace và SVG; rationale phải dùng đúng level.

## 3. Walkthrough từng đường đi

Trước khi `semantic_review=pass`, đi qua đường chính và từng nhánh có nguồn:

`Trigger → Preconditions → bước/điểm rẽ → include/extend nếu có → return/END → Postconditions`.

Ghi bảng QA gồm đường đi/anchor, trạng thái và quyền đầu vào, kết quả dự kiến,
nguồn, kết luận và gap. Không cần tạo tổ hợp trạng thái mà nguồn không yêu cầu.

Kiểm tra mỗi đường:

1. Trigger và preconditions tương thích; không giả định đã qua phép kiểm mà FR
   yêu cầu xử lý khi thất bại.
2. Guard xác định lúc rẽ; bước tiếp theo/END tồn tại và hợp lý với trạng thái
   của nhánh. Không đòi các guard luôn loại trừ nhau nếu nghiệp vụ cho phép
   nhiều điều kiện cùng đúng; khi thứ tự ưu tiên cần thiết mà thiếu thì ghi gap.
3. Điểm hợp luồng chỉ khẳng định điều đúng cho mọi nhánh đi vào. Ví dụ cache
   miss vừa gọi AI không quay vào lời khẳng định toàn lượt “không gọi AI”; bước
   chung chỉ trả kết quả, lời khẳng định cache hit nằm ở nhánh tương ứng.
4. Mỗi END đáp ứng success hoặc failure guarantee tương ứng. Không tự suy
   rollback, tính nguyên tử, retry hay xử lý race khi nguồn chưa quyết định.
5. Hợp đồng UC được gọi, điểm gọi và return nhất quán giữa caller/callee;
   extend không phá ý nghĩa độc lập của base; chuyên biệt bảo toàn hợp đồng cha.

## 4. Hồ sơ quyết định quan hệ và nơi sở hữu

Mapping phân rã và UML là hai bảng độc lập. Mỗi relation có endpoint, loại,
hướng, nguồn hành vi, điểm chèn/EP/hợp đồng, return nếu áp dụng và lý do chọn.
Xét cả core–sub và sub–sub từ luồng; cặp không có quan hệ giữ kết luận không có.

Rà cạnh trùng chính xác; cùng cặp có nhiều loại quan hệ là tín hiệu cần review,
không tự kết luận tất cả trường hợp đó đều sai. Hướng ngược cũng phải có căn cứ
riêng, không tạo cạnh đối xứng để nối hình.

Quan hệ liên module cần ghi một nơi khai báo chính, module/UC chịu trách nhiệm,
baseline nguồn, hợp đồng bên gọi/bên nhận và các view chịu tác động. Tổng quan
có thể phát hiện relation từ hành vi nguồn nhưng chưa có trong owner: ghi
proposal/cần đồng bộ, nguồn và EP; không tuyên bố owner đã đồng bộ. Nếu ngoài
scope sửa, giữ impact record/backlink đề xuất, không tự sửa các module.

## 5. Gap và quyết định nguồn

| Trường bắt buộc | Nội dung |
|---|---|
| ID, nguồn/baseline | Mã vấn đề và các chứng cứ xung đột/thiếu |
| Ảnh hưởng | UC/đường đi/quan hệ/quyền/postcondition bị ảnh hưởng |
| Mức chặn | blocking hoặc nonblocking, kèm lý do |
| Người xác nhận | Vai trò/đầu mối có quyền quyết định; chưa biết thì ghi chưa xác định |
| Register | ISS/OPEN/QA/DEC có sẵn hoặc đề xuất ghi register, không bịa mã đã tồn tại |
| Trạng thái | open / pending-confirmation / resolved, không tự đóng bằng giả định |
| Đóng vấn đề | Quyết định, bằng chứng chấp thuận, FR/baseline cần cập nhật và phần phải làm lại |

Blocking khi chưa thể kết luận phạm vi, quyền, kết quả hoặc loại quan hệ của
phần đang bàn giao. Không báo hoàn tất phần bị chặn; tiếp tục phần độc lập.
Nonblocking được giữ mở với giới hạn rõ, không làm thay đổi hành vi đã quyết.
Hai nguồn đã chốt mâu thuẫn nhưng không có quy tắc ưu tiên/hiệu lực thì ghi cả
hai, không tự chọn bản mới hơn hoặc người có chức danh cao hơn.

Câu trả lời cần đi vào register theo quy trình System Analysis. Chỉ cập nhật
FR/US/register trong phạm vi được phép; quyền phân tích không tự cho phép sửa
nguồn. Sau khi quyết định được chấp thuận, đánh giá tác động rồi cập nhật
baseline và chạy lại các kiểm tra bị ảnh hưởng.

## 6. Ba lớp bằng chứng

| Lớp | Chứng minh được | Không chứng minh được |
|---|---|---|
| Checker | Schema, ID/anchor, nguồn tồn tại, tập node khai báo, artifact SVG | Mục tiêu hợp lý, nội dung nguồn–đích tương đương, flow đúng nghiệp vụ |
| Parser/render/kiểm hình | UML parse được, hình đọc được, node/cạnh/hướng đúng mô hình | Mô hình có căn cứ hoặc bao phủ hết FR |
| BA walkthrough | Hành vi, quyền, kết quả và relation phù hợp nguồn trong scope đã đọc | Phê duyệt thay stakeholder hoặc phần ngoài scope |

Ghi kiểm tra thực tế, cảnh báo, phần chưa làm và trạng thái duyệt riêng. Không
đánh pass dựa trên tên công cụ hay một cột `result=pass` tự khai báo.
