# Quy tắc quyết định mô hình use case

[Vietnamese Doc]

Đọc ở bước 1–4 và khi review ngữ nghĩa. Quy ước ID/cổng do [SKILL.md](../SKILL.md)
sở hữu; không lặp lại ở từng bước.

## Boundary, actor và mức mục tiêu

Chọn subject: toàn iShare, subsystem hoặc bối cảnh nghiệp vụ. Module nội bộ
không thành actor ngoài iShare vì có lời gọi liên module. Dịch vụ ngoài có
trong FR có thể là actor hỗ trợ. “Hệ thống” trong FR thường là tác nhân thực thi
nội bộ; không sao chép máy móc thành actor của chính subject.

Actor là vai trò tương tác; không đồng nhất với tài khoản/RBAC. Phân biệt người
có mục tiêu (primary) với người/dịch vụ hỗ trợ (supporting). BANNED, chủ sở hữu
nội dung và thành viên nhóm thường là điều kiện ngữ cảnh; chỉ tách actor khi có
vai trò tương tác đáng phân biệt. Actor generalization cần khả năng thay thế
vai trò chung trong tương tác kế thừa; quyền vẫn đối chiếu FR.

| Mức | Tiêu chí | Sử dụng |
|---|---|---|
| Summary | Đặt nhiều mục tiêu vào bối cảnh | UC tổng quát có mục tiêu hoặc package; không ép thành cha UML |
| User goal | Một công việc gắn kết, kết quả có giá trị với actor | Trọng tâm danh mục và đặc tả |
| Subfunction | Hành vi hỗ trợ đáng tách để hiểu/tái sử dụng | Cần lý do tách, không cần actor trực tiếp khởi tạo |

Không dùng số FR, số màn hình hoặc độ phức tạp tối thiểu để công nhận một UC.
Hành trình nhiều phiên có thể hợp lệ; ghi ranh giới và mức mục tiêu. Không bắt
buộc UI: tác nhân ngoài có thể tương tác bằng sự kiện/dữ liệu.

## Giữ trong luồng hay tách UC?

Với từng hành vi, xác định mục tiêu/kết quả, nguồn và cách biểu diễn đơn giản
nhất vẫn bảo toàn yêu cầu:

- UC độc lập cho mục tiêu riêng; không bắt buộc có UC con.
- Bước/subflow cho thao tác thuộc cùng công việc.
- Alternative/exception flow cho phương thức khác, lỗi hoặc từ chối.
- Tiền/hậu điều kiện, BR, quy tắc hiển thị/dữ liệu.
- Tác vụ tự động theo thời gian/sự kiện; không tự chọn cron/JWT/CSDL nếu FR
  không ràng buộc cách cài đặt.

Chỉ tách UC hỗ trợ khi có lợi rõ cho tái sử dụng, độ rõ hoặc quản lý độ phức
tạp. Gõ @, mở form, kiểm tra định dạng và hiện lỗi thường là bước/quy tắc.
Có mã FR chứng minh căn cứ, không tự chứng minh cần oval.

FR↔UC là nhiều–nhiều: giữ, gộp, tách hoặc phân bổ. Tên dùng cụm động từ phản ánh
mục tiêu gắn kết; “Đăng nhập bằng email và mật khẩu” hợp lệ. “Quản lý…” không
tự chứng minh mức User goal hay quan hệ kế thừa.

## Luồng và hợp đồng

Luồng chính là một đường thành công cụ thể: bước có ID, ai làm gì, thông tin
trao đổi và kết quả. Không bắt buộc actor/system xen kẽ cứng nhắc. Chỉ nêu UI
nếu FR ràng buộc; không tự thiết kế màn hình hoặc vị trí nút.

Nhánh ghi bước rẽ, điều kiện, hành vi, nơi quay lại hoặc kết thúc. Phương thức
thay thế không đồng nghĩa thực thi song song. Tiền điều kiện được giả định
trước khi bắt đầu; kiểm tra có thể thất bại trong luồng cần nhánh tương ứng.
Không dùng tiền điều kiện để giấu một trường hợp FR yêu cầu xử lý.

Kết quả thất bại chỉ ghi bảo đảm có căn cứ FR. Thiếu quy tắc giao dịch,
rollback/retry có ảnh hưởng nghiệp vụ thì ghi gap, không tự điền yêu cầu mới.

## Quan hệ

### Association

Actor–UC thể hiện tham gia tương tác, không phải thứ tự gọi, đường dẫn màn
hình hay cơ chế cấp quyền. Nối tới UC độc lập/chuyên biệt nếu phù hợp; không
nối mọi actor tới cha rộng rồi mặc định được thực hiện mọi UC con.

### Include

Nguồn: UC bao hàm; đích: UC được bao hàm. Ghi bước gọi và cách quay lại/thoát
khi lỗi. Chèn hành vi không tương đương “B xảy ra trước A” hoặc “A cần trạng
thái B tạo”. Đã đăng nhập trước Đổi mật khẩu là tiền điều kiện nếu FR mô tả
như vậy; không bắt đăng nhập lại bằng include.

Tái sử dụng là lý do thường gặp, không phải yêu cầu có ít nhất hai nơi gọi.
Cần giải thích việc tách. Include không quyết định thứ tự giữa các phần được
bao hàm; ghi thứ tự và xử lý lỗi trong luồng.

### Extend

Nguồn: UC mở rộng; đích: UC cơ sở. Cơ sở phải có ý nghĩa và đủ mô tả mà không
cần đọc phần mở rộng. Extension point thuộc **cơ sở**, trỏ tới bước luồng.
Quan hệ ghi guard, phần hành vi chèn và điểm quay lại/kết thúc.

Có điều kiện, ngoại lệ, nút cùng trang hoặc link điều hướng chưa đủ để tạo
extend. Mặc định viết nhánh; chỉ tách nếu cần quản lý phần bổ sung độc lập.
Khi guard đúng, extension có thể phải thực hiện; không diễn giải thành luôn
tùy ý người dùng. Đăng xuất khi lần đăng nhập đã kết thúc là UC riêng.
Re-consent có trigger cả khi phiên còn hiệu lực, không chỉ khi đăng nhập mới.

### Generalization

Nguồn: UC chuyên biệt; đích: UC tổng quát. Ghi hợp đồng chung, cấu trúc/hành vi
được kế thừa, phần chuyên biệt và ràng buộc. Cha có thể concrete hoặc abstract;
nếu abstract, nêu phần chưa hoàn chỉnh để con cụ thể hóa. Không dùng kế thừa
chỉ để gom CRUD cùng đối tượng.

Email/Google có thể là alternative flows trong Đăng nhập, hoặc UC chuyên
biệt nếu cần quản lý luồng riêng và hợp đồng chung rõ. Không ép một đáp án.
Các con không phải bước nối tiếp của cha; package không sinh quan hệ UML.

## Liên module và hành vi tự động

UC có owner rõ, một ID trên mọi view, được nhiều UC sử dụng. Đối chiếu sự kiện,
quyền xem và kết quả ở cả hai bên giao tiếp. Không thêm việc vì sơ đồ còn trống.

AUT ghi trigger thời gian/sự kiện, điều kiện/trạng thái trước, kết quả/trạng thái
sau, quy tắc dữ liệu và nguồn. Không dựng clock/scheduler actor giả. Có thể dùng
UC theo sự kiện khi boundary/tương tác ngoài phù hợp; nếu không, AUT hoặc quy
tắc chuyển trạng thái đủ để đặc tả. Không bỏ mất yêu cầu chỉ vì chạy tự động.

FR chi tiết trỏ đến anchor bước/nhánh/điều kiện/BR/AUT. Đủ nhóm FR không chứng
minh đủ hành vi. “Đủ” cần BA đọc nội dung; tool chỉ kiểm cấu trúc/tham chiếu.

## Nguồn phương pháp

Các nguồn cung cấp phương pháp, không thay FR cung cấp tính năng:

- [OMG UML 2.5.1](https://www.omg.org/spec/UML/2.5.1), chương 18 UseCases.
- [Jacobson & Cockburn — Use-Case Foundation](https://www.ivarjacobson.com/publications/use-case-foundation).
- [NTNU — Use Case Levels](https://ttm4115.iik.ntnu.no/unit-4-req/preparation-1.html).
- [IBM — Include](https://www.ibm.com/docs/en/rsas/7.5.0?topic=diagrams-include-relationships).
- [RUP — Extend](https://www.cin.ufpe.br/~if682/RUP/process/modguide/md_exrel.htm)
  và [RUP — Generalization](https://home.iscte-iul.pt/~hro/RUPSmallProjects/core.base_rup/guidances/guidelines/use-case_generalization_B301F53B.html)
  (tài liệu Rational/IBM lưu tại trường đại học).
- [IBM — Use case specification outline](https://www.ibm.com/docs/en/engineering-lifecycle-management-suite/doors-next/7.2.0?topic=cases-use-case-specification-outline).

ID, bảng, số bước và cổng là quy ước iShare, không phải luật UML. Nếu có rubric
giảng viên, ghi riêng để đối chiếu, không đổi ngữ nghĩa UML để khớp ví dụ.
