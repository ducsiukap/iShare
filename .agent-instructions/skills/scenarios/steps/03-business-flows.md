# Bước 3 — Xác định hành trình hoàn chỉnh của actor

[Vietnamese Doc]

Đọc mục 1 của [quy tắc kịch bản](../references/scenario-rules.md). Đơn vị
đếm BF là **một chức năng actor thực hiện đến kết quả**, không phải một UC
oval, trạng thái, guard, lời gọi include hoặc đường chạy kỹ thuật.

## Cách xác định trong từng module và nhóm UC chi tiết

1. Từ mục tiêu module, xét từng nhóm **UC chính + các UC con**. Đọc FR/BR,
   mô tả, actor, quan hệ và hậu điều kiện để liệt kê những việc actor thực
   sự muốn hoàn thành. Đặt tên bằng động từ + đối tượng/kết quả nghiệp vụ.
2. Với từng ứng viên, viết một câu: **“Actor [vai trò] yêu cầu [chức năng],
   trao đổi [dữ liệu/lựa chọn] với hệ thống, đến khi nhận [kết quả chức năng]”.**
   Xác định điểm actor bắt đầu, điểm hệ thống trả kết quả và toàn bộ UC
   tham gia giữa hai điểm. Không lấy trạng thái ở giữa làm điểm kết thúc.
3. Áp dụng phép kiểm bắt buộc dưới đây trước khi gán BF/SC. Gộp ứng viên là
   bước con vào luồng bao chứa; chuyển biến thể sang mục ngoại lệ; ghi tác
   vụ thuần tự động ở quy tắc nền. Không loại khỏi truy vết FR/UC.
4. Với mỗi ứng viên đạt, gán BF-Mxx-nnn và SC-Mxx-nnn. Bảng `sc:flows` ghi
   `uc` owner, `primary` actor, `trigger` là hành động bắt đầu, `goal` là
   chức năng, `completion` là kết quả trả cho actor, `covered_ucs` gồm owner
   và UC tham gia, `rationale` giải thích tính độc lập, `sources` FR/US.
   `covered_ucs` là bao phủ hành trình, không tạo quan hệ UML include mới.
5. Dựng một đường chuẩn hoàn tất mục tiêu. Tại mỗi quyết định, xét các quyền,
   trạng thái, dữ liệu, phương thức, lỗi và lựa chọn **có trong nguồn**.
   Viết từng đường thay thế ở mục 6 đến điểm nhập lại hoặc kết thúc rõ ràng.
   Khác phương thức chỉ tách BF nếu nguồn chứng minh đó là một chức năng
   actor yêu cầu độc lập, có đầu–cuối riêng; không tách máy móc email/Google,
   loại tài khoản, còn/hết hạn, đúng/sai dữ liệu thành những BF riêng.
6. Đối soát hai chiều: mỗi mục tiêu actor có BF; mỗi UC hỗ trợ và mỗi FR/BR
   có SC/bước/nhánh/điều kiện hoặc ghi chú nền/GAP. Kiểm không còn chức năng
   dang dở và không đếm lặp cùng hành trình ở core, sub và từng điểm gọi.

## Phép kiểm để một ứng viên được gọi là BF

Ứng viên phải đồng thời đáp ứng:

- Có actor chính từ US đang theo đuổi mục tiêu nghiệp vụ; dịch vụ hỗ trợ,
  callback, bộ định thời hoặc tiến trình nội bộ không thay thế actor đó.
- Có hành động khởi đầu của actor và tương tác hai phía actor–hệ thống thực
  sự. Không bổ sung bước “xem thông báo” giả chỉ để đủ hai phía.
- Hoàn thành **toàn bộ chức năng đang xét**: gồm các bước chọn/nhập/gửi,
  xử lý/kiểm tra và phản hồi cần thiết theo nguồn. Không ép một số bước tối
  thiểu; yêu cầu → kết quả hai bước vẫn đủ nếu đó là toàn bộ chức năng.
- Kết quả có ý nghĩa với actor và được hệ thống phản hồi. Chỉ hoàn thành
  kiểm tra, mở form, gửi mã, gọi UC hoặc chuyển sang một bước bắt buộc khác
  chưa hoàn thành mục tiêu lớn đang mô tả.
- Độc lập với các BF còn lại: có lý do nghiệp vụ từ nguồn để actor yêu cầu
  chức năng này riêng, không chỉ một bộ dữ liệu/trạng thái khác của cùng việc.

Nếu thiếu nguồn để kết luận, ghi GAP; không tự biến ứng viên thành BF, cũng
không tự thêm thao tác sản phẩm để làm ứng viên đạt phép kiểm.

## Ví dụ phân rã theo yêu cầu người dùng

Ví dụ phương pháp, không bổ sung yêu cầu iShare. UC chính **Quản lý người
dùng**, các UC chức năng **Tạo mới, Cập nhật, Xác thực, Xóa người dùng**:

| BF hợp lệ | Ranh giới tương tác | Thành phần không tách thành BF riêng |
|---|---|---|
| Thêm mới người dùng | Actor yêu cầu tạo → hệ thống cung cấp dữ liệu cần nhập → actor nhập/gửi → hệ thống kiểm tra, tạo và trả kết quả | Kiểm tra dữ liệu, ghi bản ghi, báo thành công |
| Cập nhật thông tin người dùng | Actor chọn người dùng/yêu cầu sửa → hệ thống trả thông tin → actor sửa/gửi → hệ thống kiểm tra, cập nhật và phản hồi | Tải bản ghi, kiểm quyền, lưu thay đổi |
| Xác thực người dùng | Actor yêu cầu xác thực → hệ thống đưa yêu cầu xác thực → actor cung cấp thông tin → hệ thống xác minh và trả kết quả | So khớp thông tin, đánh dấu trạng thái |
| Xóa người dùng | Actor chọn người dùng/yêu cầu xóa → trao đổi/xác nhận nếu nguồn có → hệ thống thực hiện và trả kết quả | Kiểm điều kiện xóa, xóa bản ghi |

Xác thực trong bảng là chức năng actor chủ động yêu cầu. Nếu nguồn chỉ mô
tả “kiểm tra xác thực” bên trong tạo/cập nhật thì đó là bước `embedded` của
luồng đó. Tên UC giống nhau không đủ để quyết định tách.

Không tạo một BF “Quản lý người dùng” bắt actor làm nối tiếp cả bốn việc.
Không tạo BF “Actor nhập thông tin” hoặc “Hệ thống lưu người dùng”. Các
trường hợp nhập sai, trùng dữ liệu, thiếu quyền, hủy… thuộc ngoại lệ của
chức năng tương ứng nếu nguồn quy định, có đầy đủ bước tiếp nối.

Vòng lặp biểu diễn một chu kỳ và điều kiện lặp/thoát; không nhân bản vô hạn.
Tổ hợp không thể xảy ra cùng nhau được ghi lý do loại trừ. Hai nhánh tương
tác làm đổi kết quả cần đường ngoại lệ riêng, không tự động thành BF mới.

Đạt khi từng BF vượt phép kiểm trên, mọi mục tiêu actor có luồng và mọi
quy tắc/nhánh nguồn được gắn đúng chỗ. Không dùng số BF bằng số UC hoặc số
trạng thái làm bằng chứng đầy đủ.
