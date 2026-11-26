# Đánh giá ngữ cảnh và lựa chọn thiết kế skill

[Vietnamese Doc] — cập nhật 2026-11-08. Phạm vi: thiết kế skill, không sửa yêu cầu sản
phẩm và không tạo bộ scenario chính thức cho toàn bộ iShare.

## Ngữ cảnh repository

iShare là nền tảng hỏi đáp/chia sẻ tri thức cho học sinh THPT. Tài liệu hiện
có 16 module, bao gồm tài khoản, nội dung, tìm kiếm, nhóm, thông báo, kiểm
duyệt, AI và chat. Xem [intake](../../../../.agents/.claude/system_analysis/output/phase0-intake.md)
và [module-registry](../../../../.agents/.claude/system_analysis/output/registers/module-registry.md).
Intake có mô tả lịch sử: FR/BR và quyết định hiện hành mới là căn cứ của luồng.

Đã kiểm kê FR-M01–M16 trong `docs/specs/fr/`, bản làm việc FR trong workspace
chung, US-M01–M16 và US-overview trong `docs/specs/us/`. Việc file tồn tại
không chứng minh đã phê duyệt. Mẫu kiểm tra nội dung M01: FR v1.10 ghi Đã
chốt, US ghi Chờ duyệt; M06 cũng Chờ duyệt. Skill phải đọc trạng thái từng
nguồn ở thời điểm thực hiện thay vì hard-code tình trạng này.

[US-overview](../../../../docs/specs/us/US-overview.md) v1.1 ghi lựa chọn 51
trong 64 UC chính. Bởi vậy, việc không có UC trên hình tổng quan không cho
phép bỏ scenario của nó. Catalog/decomposition và đặc tả module là căn cứ
kiểm kê toàn bộ nhóm chi tiết, giữ nguyên các ID đã có.

## Các skill đã có và phần cần bổ sung

| Skill | Đã giải quyết | Phần scenario cần tiếp nối |
|---|---|---|
| [ba-interview](../../ba-interview/SKILL.md) | Phỏng vấn, register, quyền, dữ liệu, luồng và điểm chưa rõ | Giải quyết GAP mới; không lặp lại phỏng vấn đã chốt |
| [analyzing-functional-requirements](../../analyzing-functional-requirements/SKILL.md) | FR/BR theo module, trạng thái, dữ liệu, truy vết, bảy bước | Cung cấp hợp đồng hành vi và ràng buộc; không phải danh mục scenario |
| [use-case-analysis](../../use-case-analysis/SKILL.md) | Core/sub, phân rã, actor, luồng chính/nhánh, UML, trace | Bước 3 có một luồng chính và bảng nhánh; chưa bắt buộc scenario sáu phần cho từng luồng độc lập, dữ liệu cụ thể và kiểm chủ thể/đường nhập lại |
| [technical-design](../../technical-design/SKILL.md) | Kiến trúc, dữ liệu, API | Là bước sau; không đưa lớp, DAO hoặc endpoint vào sự kiện nghiệp vụ |

Chọn **một skill điều phối với bốn bước và tài nguyên dùng chung**. Các bước
phụ thuộc cùng baseline/ID/coverage; tách thành nhiều skill độc lập sẽ dễ
lệch dữ liệu và trùng luật. Bộ gồm entry point, hướng dẫn người dùng, đầu
vào, bốn bước, quy tắc, template, ví dụ và validator.

Ví dụ đối chiếu thật: US-M01 định danh Đăng xuất là UC-M01-006, thuộc core
UC-M01-021; FR-M01-07.01 yêu cầu kết thúc phiên thiết bị hiện tại và
FR-M01-07.02 giữ phiên thiết bị khác. Bảng luồng US dùng cột “Tương tác
actor–iShare”, không tách chủ thể riêng. Vì vậy scenario phải diễn giải lại
thành lượt actor yêu cầu và lượt SYSTEM kết thúc phiên, kèm dữ liệu thiết
bị/phiên; không sao chép nguyên một bảng US và coi đã thỏa quy tắc mới.
Các trigger từ màn hình khóa/chính sách phải được xét như ngữ cảnh/nhánh
của mục tiêu actor, không tự động tách thành BF riêng cho từng điểm gọi.
Ví dụ phương pháp Đăng xuất cũ của
skill US có ID minh họa khác, không được dùng để đổi ID đang có trong M01.

## Đối chiếu PDF người dùng cung cấp

Nguồn đã đọc: `G:/documents/season7/httt/B22DCCN195-Nguyễn Đức Đạt-Báo cáo tổng hợp.pdf`,
42 trang. Đã trích văn bản; render trang 7–12 và kiểm tra hình các trang chứa
đầu bảng, ngoại lệ và kết thúc. Phần dùng làm mẫu là mục 2, **Kịch bản chuẩn
và ngoại lệ**, trang PDF 7–12:

| Trường của PDF | Trường áp dụng trong skill |
|---|---|
| Scenario | 1. Tên kịch bản chuẩn |
| Actor | 2. Actor thực hiện |
| Pre-condition | 3. Tiền điều kiện |
| Post-condition | 4. Hậu điều kiện |
| Main-events | 5. Các sự kiện chính |
| Exception | 6. Các ngoại lệ |

Mẫu có danh sách sự kiện đánh số, dữ liệu nhập/kết quả cụ thể và nhánh gắn
số bước. Bản Markdown giữ đủ sáu trường dưới sáu mục, dùng bảng cho danh
sách bước dài thay vì nhồi bảng lồng vào một ô. Nguồn/truy vết là metadata
ngoài sáu phần, không thay cấu trúc người dùng yêu cầu.

Đọc lại phần UC trang 3–6 cùng phần scenario trang 7–12 cho thấy đơn vị
hành trình phải bám chức năng actor thực hiện, không bám từng oval:

- Trang 7–8, bảng mang tên “Quản lý thông tin nguyên liệu” nhưng đường chính
  thực tế đi từ nhân viên thao tác đến thêm nguyên liệu thành công. Vì vậy
  nên đặt tên BF theo chức năng **Thêm nguyên liệu**, không suy ra cả thêm,
  sửa, xóa đã được bao phủ bởi tiêu đề quản lý.
- Trang 8–10, **Nhập nguyên liệu từ nhà cung cấp** đi qua chọn/tìm nhà cung
  cấp, chọn/tìm nguyên liệu, nhập số lượng/đơn giá, lưu và xác nhận rồi mới
  nhận kết quả nhập thành công (bước 24). Không tách “hệ thống cập nhật thông
  tin chọn” hoặc “xác nhận nội bộ” thành scenario độc lập. Ngoại lệ thêm nhà
  cung cấp/nguyên liệu trang 10–11 phải nối lại luồng nhập và đi đến kết quả.
- Trang 11–12, **Xem thống kê** có actor chọn tiêu chí, hệ thống trả danh
  sách, actor chọn chi tiết và hệ thống trả chi tiết; không có scenario chỉ
  gồm hệ thống tổng hợp số liệu. Mẫu chưa đủ để kết luận mọi luồng đã đủ.

Điều chỉnh v1.1 theo yêu cầu người dùng: các chức năng độc lập như thêm,
cập nhật, xác thực, xóa có luồng riêng; phần hỗ trợ, guard, trạng thái và
tác vụ tự động nằm đúng vị trí trong hành trình hoặc ghi chú nền. Không
biến PDF thành nguồn luật sản phẩm, không sao chép các chỗ thiếu của mẫu.

Giới hạn quan sát được: mẫu thống kê ở trang 11 bỏ trống hậu điều kiện;
trang 12 ngoại lệ chỉ nêu danh sách trống; nhánh đăng nhập ở trang 8 chưa
chỉ điểm nhập lại theo ID bước. Vì yêu cầu hiện tại đòi hỏi kết thúc luồng
rõ, skill phải bổ sung quy tắc hậu điều kiện và đường tiếp nối, không sao
chép những chỗ thiếu này. Mẫu nhiều actor có trao đổi giữa nhân viên và nhà
cung cấp: quy tắc so **đúng chủ thể**, không gom mọi actor thành một chủ thể.

Không dùng “kịch bản v.2/v.3” ở các phần giao tiếp/tuần tự sau đó làm mẫu:
chúng đưa lớp/View/DAO/hàm làm chủ thể, trái yêu cầu chỉ actor/hệ thống.
Không chuyển nghiệp vụ nguyên liệu, nhà cung cấp hoặc số liệu PDF vào iShare.

## Quyết định quan trọng

- Một BF độc lập có một SC; nhánh của BF được triển khai ở mục 6. Phải xét
  mọi UC chính thực thi và UC con, không chỉ viết một scenario tổng quát/core.
- Core Summary/abstract có bảng bao phủ qua scenario cụ thể; không bịa một
  giao dịch chạy tất cả UC con. Subfunction hỗ trợ là `embedded`, có SC/bước
  bao chứa; tác vụ nền không có actor là `background`, không có BF/SC riêng.
- Bỏ quy tắc v1.0 cho phép scenario một bước SYSTEM. Mỗi BF phải có actor
  chính khởi đầu, tương tác cả hai phía và kết quả hoàn tất chức năng. Khác
  quyền/trạng thái/phương thức chưa đủ để tách BF. Không dùng chuyển giao
  để dừng ở giữa chức năng. Xem phép kiểm đầu–cuối của bước 3.
- Ngoại lệ thay thế một bước cụ thể; việc này tránh lỗi hai phản hồi SYSTEM
  liên tiếp khi đọc nhánh như phần chạy sau bước lỗi.
- Giá trị giả lập được phép, ràng buộc nghiệp vụ mới thì không. Thiếu quy
  trình sửa/thử lại/hủy có nguồn là GAP, không tự thêm để làm đủ mẫu.
- Bốn bước mặc định thực hiện liên tục; phê duyệt tài liệu tách khỏi quyền
  triển khai. Tôn trọng yêu cầu làm từng bước khi người dùng nêu rõ.
- Validator là kiểm tra cấu trúc/đường đi; không tự xác nhận đã bao phủ hết
  nguồn hoặc đúng nghiệp vụ. Ví dụ kiểm thử là dữ liệu giả, không phải FR mới.

## Cách kiểm chứng

Chạy quick_validate cho skill; kiểm link; chạy validator trên ví dụ hoàn
chỉnh; thử các lỗi thực tế (cùng subject, nhánh bỏ lửng, quay về sai bước,
chu trình không có kết thúc, thiếu scenario/nguồn). Review đối chiếu tám
nhóm yêu cầu của người dùng với hợp đồng SKILL.md và bốn bước.

Kết quả kiểm tra được ghi cùng lần bàn giao bộ skill, không phải bằng chứng
phê duyệt scenario sản phẩm. Validator cần Python chuẩn; các thư viện dùng
để đọc PDF trong lần tạo skill chỉ là công cụ tạm, không phải phụ thuộc của
skill khi sử dụng về sau.
