# Quy tắc biên soạn và bao phủ scenario

[Vietnamese Doc]

## 1. Phân biệt UC, luồng nghiệp vụ, scenario và nhánh

- **UC chính + các UC con** mô tả cấu trúc và phạm vi. Core Summary như quản
  lý tài khoản không có nghĩa một người luôn đăng ký, đổi mật khẩu rồi xóa
  tài khoản trong cùng một lần chạy.
- **Luồng nghiệp vụ** là toàn bộ hành trình actor thực hiện một chức năng
  với hệ thống: actor bắt đầu → trao đổi dữ liệu/lựa chọn → hệ thống hoàn
  tất chức năng và trả kết quả cho actor. Một luồng có thể đi qua nhiều UC
  con. Một UC có thể có nhiều mục tiêu độc lập; cũng có thể chỉ hỗ trợ một
  bước trong luồng khác. Không suy ra số BF từ số UC hoặc nhánh kỹ thuật.
- **Scenario** đặc tả một luồng nghiệp vụ bằng sáu phần. Các sự kiện chính
  mô tả một đường đi chuẩn; các ngoại lệ mô tả những biến thể của đường đi
  đó. Luồng chính đạt mục tiêu chức năng đã chọn (`END:SUCCESS`); từ chối,
  lỗi, hủy nằm trong ngoại lệ, không dựng thành BF “bị từ chối” riêng.
- **Nhánh** là rẽ theo điều kiện hoặc lựa chọn trong một luồng. Sai dữ liệu
  rồi sửa, thay phương thức, khác quyền/trạng thái, hủy hoặc thử lại nằm ở
  mục 6 của cùng mục tiêu. Chỉ tách khi nguồn chứng minh mục tiêu chức năng
  độc lập của actor, có đầu–cuối hoàn chỉnh; khác chuỗi bước đơn thuần chưa đủ.

Mọi luồng nghiệp vụ cần có scenario riêng; mọi nhánh cần được mô tả tới kết
quả. Không thay chúng bằng danh sách test case hoặc chỉ một happy path/UC.

Trước khi viết, áp dụng [phép kiểm BF và ví dụ quản lý người dùng](../steps/03-business-flows.md).
Chốt actor chính, hành động bắt đầu, mục tiêu, kết quả nhận được, UC tham
gia và lý do độc lập. Dùng các nguyên tắc ranh giới sau:

- Không lấy tiền điều kiện để giấu một phần bắt buộc của chính chức năng:
  “Tạo mới” không được bắt đầu sau khi đã tạo bản ghi rồi chỉ báo thành công.
  Ngữ cảnh đã có trước chức năng (ví dụ đã đăng nhập) vẫn là tiền điều kiện
  hợp lệ nếu nguồn quy định, không ép lặp lại trong mọi scenario.
- Không kết thúc ở “mở form”, “gửi mã”, “kiểm quyền xong”, “gọi UC con”,
  “chuyển tới bước tiếp theo” khi actor còn phải làm để đạt mục tiêu đã nêu.
  Ví dụ gửi yêu cầu đặt lại mật khẩu phải đi tiếp đến kết quả đặt lại nếu
  chức năng đang xét là đặt lại mật khẩu, không dừng chỉ vì đã gửi email.
- Nếu nguồn quy định mục tiêu chính là gửi/ghi nhận một yêu cầu bất đồng bộ,
  actor nhận xác nhận ghi nhận là SUCCESS của mục tiêu đó; không khẳng định
  công việc phía sau đã xong. Tác vụ nền theo dõi bằng quy tắc/hiệu ứng nguồn.
- Tìm kiếm/xác thực/xác nhận chỉ có BF riêng khi actor thực sự yêu cầu chức
  năng độc lập đó. Khi là bước chọn dữ liệu/kiểm tra trong một chức năng lớn,
  triển khai tại chỗ, trả về hành trình bao chứa và không đếm thêm BF.
- Không gộp các chức năng độc lập thêm/sửa/xóa/xác thực vào một lần chạy
  chỉ vì chung UC chính “Quản lý”. Không nhân bản cùng hành trình ở cả core
  và sub. Bao phủ nhóm bằng mapping, không bằng scenario trùng lặp.

## 2. Một chủ thể cho mỗi sự kiện

`subject` là `SYSTEM` hoặc ID actor có trong danh mục nguồn. Ghi ID trong
cột chủ thể, tên vai trò trong câu hành động. Actor có thể là con người hoặc
dịch vụ ngoài boundary đã được US xác định; bộ xử lý nội bộ vẫn là SYSTEM.

- Một sự kiện là một **lượt tương tác cùng chủ thể**, không phải một lời gọi
  hàm. “Hệ thống kiểm tra dữ liệu, ghi nhận thay đổi và thông báo kết quả” có
  thể là một sự kiện nếu không có tương tác chủ thể khác xen vào.
- “Người dùng nhập và gửi dữ liệu” có thể cùng bước. “Người dùng gửi; hệ
  thống lưu” phải tách hai bước vì có hai chủ thể.
- Hai bước chính liền kề phải khác ID chủ thể. Thông thường là actor ↔
  SYSTEM. Nhiều actor có thể nối tiếp nếu **khác actor** và nguồn mô tả trao
  đổi đó; không coi tất cả actor là một chủ thể, không tự chèn hệ thống vào
  trao đổi ngoài đời chỉ để xen kẽ. Đừng thêm hành vi ngoài boundary nếu FR/US
  không mô tả; thông tin thu thập trước đó có thể là dữ liệu đầu vào.
- Không viết “actor xem/thấy thông báo” như một hành động giả để tách hai
  bước hệ thống. Xem/chọn/xác nhận chỉ là sự kiện khi nguồn có hành động đó.
- Không thêm đăng nhập ở đầu mọi scenario nếu đã là tiền điều kiện. Không
  tự thêm tên trang, vị trí nút, modal hay “OK”; tên chức năng và thông tin
  nghiệp vụ đủ để mô tả tương tác khi chưa có HMI.

**Tự động/Subfunction:** không tạo BF/SC độc lập chỉ SYSTEM, chỉ actor hoặc
chỉ trao đổi giữa SYSTEM với dịch vụ hỗ trợ. Gộp xử lý nội bộ vào lượt SYSTEM
trong hành trình actor bao chứa, giữ đầu vào/đầu ra và nguồn. Tác vụ theo
thời gian không có hành trình actor bao chứa được ghi tại bảng quy tắc nền
(trigger, điều kiện, hiệu ứng, nguồn), không dùng khối sáu phần “phụ”. Không
tạo “Scheduler” hoặc bước actor giả để qua kiểm tra. Việc các bước liền kề
khác chủ thể là điều kiện cần, chưa chứng minh luồng hợp lệ hay hoàn chỉnh.

## 3. Ngoại lệ và đường đi sau lựa chọn

Phân loại theo nơi phát sinh nhánh:

- `system`: kiểm tra dữ liệu/quyền/trạng thái, không có kết quả, xung đột,
  dịch vụ lỗi… **chỉ khi nguồn có**; không chỉ lỗi hạ tầng.
- `user-choice`: actor chọn hủy/quay lại/bỏ qua/phương thức khác… theo nguồn.

Quy ước duy nhất để không nhập nhằng: `at=M4` nghĩa nhánh **thay thế M4**,
không phải chạy xong M4 rồi mới chạy lại phản hồi hệ thống ở đầu nhánh.
Ví dụ M3 actor gửi → E1.1 SYSTEM từ chối → E1.2 actor sửa/gửi → M4 SYSTEM
kiểm lại. Nếu lựa chọn ở M3: M2 SYSTEM đưa lựa chọn → E2.1 actor hủy → E2.2
SYSTEM đóng thao tác. Bước đầu nhánh cùng chủ thể với bước nó thay thế.

Mỗi nhánh phải có:

1. Bước rẽ, điều kiện kích hoạt hoặc lựa chọn cụ thể và nguồn.
2. Các sự kiện riêng có số bước, chủ thể, dữ liệu, phản hồi.
3. Đích tiếp tục chính xác: một bước cùng scenario hoặc kết thúc có kết quả.
4. Hậu điều kiện tương ứng, gồm thay đổi/giữ nguyên dữ liệu và hiệu ứng phụ.

Một lỗi dẫn tới sửa hoặc hủy: viết riêng từng đường lựa chọn (có thể cùng
`at` nhưng guard khác), nêu rõ điều kiện lựa chọn tại bước actor trong nhánh.
Nếu nhánh lại phát sinh lỗi/lựa chọn, khai triển các đường khả thi hoặc chỉ
đúng bước lặp; không để “và các trường hợp khác”. Tránh lồng nhánh vô hạn.

`END:SUCCESS`, `END:REJECTED`, `END:CANCELLED`, `END:HANDED_OFF` là ký hiệu kết
thúc. Mỗi ký hiệu được dùng phải có một hậu điều kiện không rỗng. Chuyển giao
chỉ dùng cho nhánh chuyển sang mục tiêu khác có bên nhận/trigger/scenario
tiếp nối rõ ràng. Không kết thúc luồng chính bằng HANDED_OFF để chia một
chức năng dang dở thành các scenario con. Nếu bước tiếp theo vẫn bắt buộc
cho cùng mục tiêu, phải triển khai tiếp trong chính scenario hiện tại.

Từ chối cuối cùng là kết thúc hợp lệ nếu nguồn quy định dừng. Không nhất
thiết bịa thao tác xác nhận sau thông báo. Nếu nguồn cho phép sửa, viết đến
bước sửa/gửi và điểm kiểm tra lại. Nếu nguồn chưa nói, ghi GAP thay vì đoán.

## 4. Quan hệ UC và hành trình xuyên module

- `include`: giữ điều kiện/điểm gọi và đường trở về. Triển khai tương tác UC
  được gọi trong scenario bao chứa, dùng ID bước cục bộ và truy vết UC/FR.
  Không bắt buộc UC được gọi có scenario riêng. Nếu UC đó đồng thời là chức
  năng độc lập có SC, dẫn chiếu SC đó để đối soát nhưng vẫn viết đầy đủ lượt
  tương tác cần thiết trong luồng hiện tại; không dừng ở một câu gọi UC.
- `extend`: chỉ chèn khi đúng guard/extension point đã có trong US, có đường
  trở lại/kết thúc. Không gọi mọi nhánh lỗi là extend.
- Generalization: scenario chạy theo actor/phương thức cụ thể; core abstract
  được bao phủ qua các chuyên biệt, không dựng một lần chạy abstract.
- Module khác vẫn là phần của SYSTEM. Actor dịch vụ ngoài giữ ID đúng
  boundary US. Không đi sâu vào API, bảng dữ liệu hoặc hàm xử lý.
- Đối chiếu subject cuối trước khi gọi, subject đầu của phần chèn, subject
  cuối phần chèn và subject khi trở về; gộp lượt cùng chủ thể nếu cần.

## 5. Dữ liệu và nguồn

Mỗi bước ghi thông tin dùng/nhận/trả, tham chiếu bộ dữ liệu nếu dài. Các bộ
dữ liệu ghi giá trị giả lập, đơn vị, trạng thái trước/sau, quan hệ định danh
và BR kiểm tra. Dữ liệu chọn phải thỏa tiền điều kiện và kích hoạt đúng guard.

Ví dụ giá trị tên/email có thể tự tạo và gắn nhãn “giả lập”; không suy ra độ
dài tối đa, bắt buộc, giá mặc định hay quyền mới từ ví dụ. Không ghi token/
mật khẩu thật. “Không phát sinh dữ liệu mới; dùng đối tượng đã chọn” là mô tả
hợp lệ khi đúng nghiệp vụ; dấu gạch trống không thay được mô tả dữ liệu.

Nguồn mỗi bước/nhánh có mã FR chi tiết/BR. Ghi điểm US tương ứng ở bước hoặc
ở metadata/tên scenario khi toàn bộ scenario thuộc cùng đặc tả UC. Dùng mã
đầy đủ, không `FR-M01-08.01–.09`. Khi hệ thống thực hiện nhiều quy tắc trong
một lượt, ghi tất cả mã liên quan. Kiểm nguyên văn, không chỉ kiểm ID tồn tại.

## 6. Chứng minh bao phủ và giới hạn

Đối soát **hai chiều**: FR/BR + UC/nhánh nguồn → BF → SC/bước/ngoại lệ; và
mỗi hành vi trong scenario → nguồn hoặc nhãn dữ liệu minh họa. Kiểm cả core,
sub dùng chung, AUT/RULE liên quan, các lựa chọn ở mỗi quyết định và kết quả.
UC `embedded` phải chỉ rõ SC/bước/nhánh; `background` phải có ghi chú nguồn
và hiệu ứng. Bao phủ nguồn không đồng nghĩa mọi dòng nguồn cần một BF.

“Toàn bộ” là toàn bộ hành vi được nguồn hỗ trợ trong scope đã ghi. Với
vòng lặp, biểu diễn chu kỳ + điều kiện thoát; với nhánh độc lập, ghi các tổ
hợp khả thi và lý do lớp tương đương thay vì nhân mọi giá trị dữ liệu. Nếu
hai nhánh tương tác làm đổi kết quả, cần đường đi riêng. Không được tuyên bố
toàn bộ đường đi đã đủ chỉ vì mọi dòng trong một bảng do mình lập đã có SC.

Máy kiểm được số phần, có cả actor/hệ thống, điểm đầu/cuối, chủ thể hợp lệ,
cạnh nối và đường tới kết thúc. BA review phải kiểm actor thực sự theo đuổi
mục tiêu, chức năng đã hoàn tất, BF không bị phân mảnh/trùng, guard khả thi,
dữ liệu nhất quán, lựa chọn đủ và nguồn thật sự hỗ trợ hành vi. Điền một ô
`completion` hoặc qua validator chưa chứng minh chức năng hoàn chỉnh.
