# Tài liệu yêu cầu hệ thống — M05 Topic & Tag
<!-- [Vietnamese Doc] -->

| Mã tài liệu | ISH-SR-M05 |
|---|---|
| Dự án | iShare |
| Module | M05 — Topic & Tag |
| Trạng thái | Bản nháp |
| Phiên bản | 0.4 |
| Ngày | 2026-10-05 |
| Tác giả | Phạm Văn Đức |

## 1. Tổng quan

Tài liệu này quy định các yêu cầu chức năng của module M05 — Topic & Tag của iShare: danh mục Topic, việc gắn Topic và Tag cho bài viết, gợi ý Topic bằng AI, theo dõi Topic, điểm Trending của Topic và Tag, và các thao tác quản trị Topic, Tag của Mod và Admin.

### 1.1 Mục đích

Phân loại bài viết theo lĩnh vực tri thức (Topic) và theo từ khóa tự do chi tiết hơn (Tag), để người dùng tổ chức, lọc, duyệt và theo dõi nội dung phù hợp với học sinh THPT.

## 2. Thuật ngữ và viết tắt

### 2.1 Thuật ngữ

| Thuật ngữ | Mô tả |
|---|---|
| Topic | Lĩnh vực hoặc chủ đề nội dung của bài viết; phân loại có cấu trúc, chọn từ danh mục Topic, dùng để lọc và duyệt nội dung. |
| Danh mục Topic | Tập Topic một tầng đang có hiệu lực của hệ thống; Topic nguồn sau khi gộp không còn thuộc danh mục Topic. |
| Topic nguồn | Topic bị gộp vào một Topic khác. |
| Topic đích | Topic nhận các bài viết của Topic nguồn khi gộp. |
| Tag | Từ khóa tự do dạng #hashtag do người dùng nhập, chi tiết hơn Topic; không có danh sách cố định. |
| Tên Tag | Phần chữ của Tag, không gồm dấu #. |
| Tag bị vô hiệu hóa | Tag mà Mod hoặc Admin đã vô hiệu hóa trong tình huống khẩn cấp; ngược lại là Tag hoạt động. |
| Bài viết | Nội dung do người dùng đăng, gồm tiêu đề, nội dung văn bản và tệp đính kèm. |
| Tác giả | Người dùng đã tạo bài viết. |
| Gửi bài viết | Thao tác của tác giả chuyển bài viết từ bản nháp sang chờ xuất bản. |
| Bài viết công khai | Bài viết đã xuất bản (không ở bản nháp, chờ duyệt, bị từ chối, bị tác giả tự ẩn hay đã xóa) và đang ở trạng thái kiểm duyệt bình thường (không bị gắn cờ chờ xử lý, không bị Mod ẩn). |
| Bài viết được tính | Bài viết công khai không thuộc Group Private; chỉ các bài viết này góp vào điểm Trending. |
| Trở thành công khai lần đầu | Thời điểm bài viết lần đầu trở thành bài viết công khai. |
| Group Private | Nhóm riêng tư; nội dung chỉ thành viên nhóm xem được. |
| Guest | Người truy cập chưa đăng nhập. |
| User | Người dùng đã đăng nhập với vai trò thông thường. |
| Mod | Người dùng có vai trò kiểm duyệt viên (Moderator). |
| Admin | Người dùng có vai trò quản trị hệ thống. |
| Người dùng | Bất kỳ người truy cập nào, gồm Guest, User, Mod và Admin. |
| Người dùng đã đăng nhập | User, Mod hoặc Admin. |
| Dịch vụ AI | Dịch vụ phân tích văn bản bên ngoài mà hệ thống dùng để tạo gợi ý Topic. |
| Gợi ý Topic | Danh sách Topic do dịch vụ AI đề xuất cho một bài viết khi tác giả yêu cầu. |
| Gợi ý cũ | Gợi ý Topic mà sau khi nhận, tác giả đã thay đổi tiêu đề hoặc nội dung văn bản của bài viết; ngược lại là gợi ý còn mới. |
| Chức năng gợi ý Topic bị tắt | Trạng thái khi Admin tắt công tắc AI chung hoặc tắt riêng công tắc gợi ý Topic. |
| Dịch vụ AI không trả về kết quả | Yêu cầu gợi ý Topic hết thời gian chờ hoặc gặp lỗi, kể cả sau lần thử lại. |
| Tiếng | Đơn vị đếm độ dài văn bản: một cụm ký tự liền nhau ngăn cách bởi ký tự trắng (dấu cách, tab, xuống dòng). |
| Phản hồi gợi ý Topic | Bản ghi gồm các Topic được gợi ý và các Topic tác giả chọn cuối cùng cho một bài viết. |
| Theo dõi Topic | Quan hệ giữa một người dùng đã đăng nhập và một Topic mà người dùng đó muốn nhận cập nhật, gồm thông báo khi có bài viết mới trong Topic. |
| Upvote | Lượt đánh giá tích cực của người dùng cho một bài viết hoặc một bình luận. |
| Bookmark | Thao tác người dùng lưu một bài viết vào danh sách đã lưu của mình. |
| Người xem | Người dùng đã đăng nhập, khác tác giả, đã mở trang chi tiết của một bài viết. |
| Điểm tương tác | Điểm của một bài viết trong 7 ngày gần nhất, dùng để tính điểm Trending. |
| Bình luận | Bình luận gốc hoặc trả lời trong một bài viết. |
| Điểm Trending | Điểm xếp hạng mức độ sôi nổi của một Topic hoặc một Tag trong 7 ngày gần nhất. |
| 7 ngày gần nhất | 168 giờ tính lùi từ thời điểm tính điểm Trending. |
| Thứ tự bảng chữ cái tiếng Việt | Thứ tự so tên, không phân biệt chữ hoa, chữ thường. Bước 1: bỏ qua dấu thanh, so từng ký tự từ trái sang phải theo thứ tự: ký hiệu không phải chữ cái, rồi chữ số 0 đến 9, rồi chữ cái a ă â b c d đ e ê f g h i j k l m n o ô ơ p q r s t u ư v w x y z; tên là phần đầu của tên kia thì xếp trước. Bước 2: chỉ khi hai tên giống hệt ở bước 1, so dấu thanh từ trái sang phải theo thứ tự ngang, huyền, hỏi, ngã, sắc, nặng. |

### 2.2 Viết tắt

| Viết tắt | Đầy đủ |
|---|---|
| SR | System Requirement |
| AI | Artificial Intelligence |
| THPT | Trung học phổ thông |

## 3. Thông tin đầu vào

### 3.1 Tài liệu đầu vào

| Mã | Tên | Phiên bản |
|---|---|---|
| DRAFT | iShare_modules.md §3.1, §3.2, §3.3, §3.4, §4.5, §7.1, §7.2, §11.2 | 2026-10-05 |
| DRAFT | iShare_dev_priority.md §3 (mốc triển khai) | 2026-10-04 |
| REG | decisions.md: DEC-008, DEC-033, DEC-047…054, DEC-056, DEC-058, DEC-060, DEC-065, DEC-090, DEC-093, DEC-096, DEC-099, DEC-100, DEC-124…126, DEC-132, DEC-133, DEC-140…165 | 2026-10-05 |
| REG | issue-queue.md: ISS-046, ISS-051, ISS-079…086, ISS-088, ISS-090, ISS-093, ISS-119, ISS-122, ISS-125, ISS-129, ISS-166, ISS-175, ISS-176, ISS-185, ISS-194, ISS-195, ISS-207…244 | 2026-10-05 |
| REG | qa-log.md: QA-011, QA-017, QA-033, QA-034, QA-043, QA-101…109, QA-113, QA-115, QA-123, QA-160, QA-165, QA-169, QA-175, QA-178, QA-226, QA-227, QA-235…237, QA-253, QA-254, QA-267…304 | 2026-10-05 |
| REG | module-registry.md (dòng M05) | 2026-10-05 |

### 3.2 Tài liệu liên quan

Không có.

## 4. Tổng quan chức năng

Module M05 quản lý hai trục phân loại bài viết. Topic là danh mục một tầng gồm 11 lĩnh vực tri thức chốt sẵn, không ai thêm hay xóa được; mỗi bài viết đã gửi thuộc từ một đến ba Topic. Tag là từ khóa tự do do người dùng nhập, tối đa năm Tag mỗi bài viết, tự tạo khi được dùng lần đầu.

Khi soạn bài viết, tác giả có thể tự chọn Topic hoặc yêu cầu AI gợi ý Topic từ tiêu đề và nội dung. Gợi ý chỉ mang tính đề xuất; tác giả luôn quyết định cuối cùng, và khi AI tắt hoặc lỗi thì tác giả vẫn tự chọn Topic để đăng bài. Lựa chọn cuối cùng so với gợi ý được ghi nhận làm phản hồi cho AI.

Người dùng đã đăng nhập có thể theo dõi Topic. Module tính điểm Trending cho Topic và Tag từ upvote, bình luận, bookmark và người xem trong 7 ngày gần nhất để module Feed hiển thị. Mod và Admin đổi Topic của bài viết, đổi tên và gộp Topic (không xóa Topic), và vô hiệu hóa hoặc mở lại Tag khi khẩn cấp.

### 4.1 Luật và tiêu chuẩn liên quan

Không có.

## 5. Yêu cầu chức năng

### 5.1 Tổng quan yêu cầu

| Tính năng | Yêu cầu cấp trên | Mức ưu tiên | Mốc | Ngoại lệ |
|---|---|---|---|---|
| Danh mục Topic | ISH-M05-001 | Must | P0 | — |
| Gán Topic cho bài viết | ISH-M05-002 | Must | P0 | — |
| Gợi ý Topic bằng AI | ISH-M05-003 | Must | AI-P0 | — |
| Xử lý kết quả và sự cố của gợi ý Topic | ISH-M05-004 | Must | AI-P0 | — |
| Ghi nhận phản hồi gợi ý Topic | ISH-M05-005 | Must | AI-P1 | — |
| Gắn Tag cho bài viết | ISH-M05-006 | Must | P0 | — |
| Theo dõi Topic | ISH-M05-007 | Must | P1 | — |
| Trending Topic và Tag | ISH-M05-008 | Must | P1 | — |
| Đổi Topic của bài viết bởi Mod và Admin | ISH-M05-009 | Must | P0 | — |
| Đổi tên Topic | ISH-M05-010 | Must | P0 | ISH-M05-010.2: P1 |
| Gộp Topic | ISH-M05-011 | Must | P0 | ISH-M05-011.3, ISH-M05-011.4, ISH-M05-011.6: P1 |
| Vô hiệu hóa và mở lại Tag | ISH-M05-012 | Must | P0 | ISH-M05-012.3: P1 |

### 5.2 Chuyển trạng thái

| Trạng thái hiện tại | Sự kiện hoặc điều kiện | Trạng thái mới | ID yêu cầu |
|---|---|---|---|
| Tag hoạt động | Mod hoặc Admin vô hiệu hóa Tag | Tag bị vô hiệu hóa | ISH-M05-012.1 |
| Tag bị vô hiệu hóa | Mod hoặc Admin mở lại Tag | Tag hoạt động | ISH-M05-012.5 |
| Topic trong danh mục Topic | Topic được gộp làm Topic nguồn | Topic đã loại khỏi danh mục Topic (trạng thái cuối) | ISH-M05-011.2 |
| Gợi ý còn mới | Tác giả thay đổi tiêu đề hoặc nội dung văn bản | Gợi ý cũ | ISH-M05-003.10 |
| Gợi ý cũ | Tác giả yêu cầu gợi ý lại và nhận gợi ý mới | Gợi ý còn mới | ISH-M05-003.4, ISH-M05-003.13 |
| Chưa theo dõi Topic | Người dùng đã đăng nhập theo dõi Topic | Đang theo dõi Topic | ISH-M05-007.1 |
| Đang theo dõi Topic | Người dùng bỏ theo dõi Topic | Chưa theo dõi Topic | ISH-M05-007.2 |
| Đang theo dõi Topic nguồn | Topic nguồn được gộp vào Topic đích | Đang theo dõi Topic đích | ISH-M05-011.3 |
| Topic đã loại khỏi danh mục Topic | Người dùng yêu cầu theo dõi, hoặc Mod/Admin yêu cầu gộp với Topic đó | Không đổi (bị từ chối) | ISH-M05-007.7, ISH-M05-011.8 |

### 5.3 Danh mục Topic

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-001 | Hệ thống phải cung cấp một danh mục Topic một tầng mà không người dùng nào thêm hay xóa được Topic. |

**Lý do**

Topic dùng để tổ chức các lĩnh vực tri thức lớn, phù hợp đối tượng học sinh THPT. Topic là phân loại có cấu trúc, dùng để lọc và duyệt nội dung.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-001.1 | Hệ thống phải khởi tạo danh mục Topic với đúng 11 Topic sau: Toán học, Ngữ văn, Ngoại ngữ, Khoa học tự nhiên (Lý/Hóa/Sinh), Khoa học xã hội (Sử/Địa/KT&PL), Tin học, Kỹ năng mềm, Hướng nghiệp, Nghệ thuật & Sáng tạo, Góc Chill, Khác. |
| ISH-M05-001.2 | Hệ thống phải tổ chức danh mục Topic thành một tầng, không có tầng phân loại cha phía trên Topic. |
| ISH-M05-001.3 | Hệ thống phải cho phép mọi người dùng, kể cả Guest, xem danh sách Topic trong danh mục Topic. |
| ISH-M05-001.4 | Hệ thống phải không cho phép thêm Topic mới vào danh mục Topic. |
| ISH-M05-001.5 | Khi người dùng yêu cầu xóa một Topic, hệ thống phải từ chối yêu cầu đó. |

### 5.4 Gán Topic cho bài viết

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-002 | Hệ thống phải phân loại mỗi bài viết theo Topic thuộc danh mục Topic, từ lúc soạn đến lúc hiển thị bài viết, với từ 1 đến 3 Topic cho bài viết đã gửi. |

**Lý do**

Topic là phân loại có cấu trúc, bắt buộc cho mỗi bài viết, dùng để lọc và duyệt nội dung.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-002.1 | Khi tác giả tạo bài viết, hệ thống phải cho phép tác giả chọn Topic cho bài viết đó từ danh mục Topic. |
| ISH-M05-002.2 | Khi người dùng chọn Topic cho một bài viết, hệ thống phải chỉ chấp nhận Topic có trong danh mục Topic. |
| ISH-M05-002.3 | Hệ thống phải cho phép tác giả chọn Topic cho bài viết mà không cần yêu cầu gợi ý Topic. |
| ISH-M05-002.5 | Khi tác giả gửi một bài viết không có Topic nào, hệ thống phải từ chối việc gửi bài viết đó. |
| ISH-M05-002.6 | Khi người dùng lưu một thay đổi làm một bài viết đã gửi không còn Topic nào, hệ thống phải từ chối thay đổi đó. |
| ISH-M05-002.7 | Hệ thống phải giới hạn mỗi bài viết tối đa 3 Topic. |
| ISH-M05-002.8 | Khi người dùng chọn Topic thứ 4 cho một bài viết, hệ thống phải từ chối lựa chọn đó. |
| ISH-M05-002.9 | Khi tác giả sửa một bài viết đã gửi, hệ thống phải cho phép tác giả thay đổi Topic của bài viết đó. |
| ISH-M05-002.10 | Khi người dùng, kể cả Guest, xem một bài viết, hệ thống phải hiển thị các Topic của bài viết đó. |
| ISH-M05-002.11 | Khi tác giả lưu bản nháp của một bài viết chưa có Topic nào, hệ thống phải chấp nhận việc lưu bản nháp đó. |

### 5.5 Gợi ý Topic bằng AI

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-003 | Khi tác giả yêu cầu gợi ý Topic trong lúc soạn bài viết mới, hệ thống phải gợi ý tối đa 3 Topic thuộc danh mục Topic dựa trên tiêu đề và nội dung văn bản của bài viết đó. |

**Lý do**

AI chỉ gợi ý Topic, không tự gán; người dùng xem lại và chọn lại nếu cần.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-003.1 | Hệ thống phải chỉ tạo gợi ý Topic khi tác giả yêu cầu gợi ý. |
| ISH-M05-003.2 | Khi tạo gợi ý Topic cho một bài viết, hệ thống phải không dùng tệp đính kèm của bài viết đó. |
| ISH-M05-003.3 | Hệ thống phải giới hạn mỗi gợi ý Topic tối đa 3 Topic. |
| ISH-M05-003.4 | Khi hệ thống trả về gợi ý Topic cho một bài viết, hệ thống phải thay lựa chọn Topic hiện tại của bài viết đó bằng các Topic được gợi ý. |
| ISH-M05-003.5 | Khi tác giả thay đổi lựa chọn Topic sau khi nhận gợi ý Topic, hệ thống phải lưu lựa chọn mới của tác giả. |
| ISH-M05-003.6 | Khi tác giả yêu cầu gợi ý Topic cho một bài viết có tổng số tiếng của tiêu đề cộng nội dung văn bản ít hơn 10, hệ thống phải từ chối yêu cầu gợi ý đó. |
| ISH-M05-003.7 | Khi hệ thống từ chối yêu cầu gợi ý Topic vì văn bản ít hơn 10 tiếng, hệ thống phải thông báo cho tác giả rằng nội dung quá ngắn. |
| ISH-M05-003.8 | Hệ thống phải giới hạn mỗi người dùng tối đa 10 yêu cầu gợi ý Topic trong mỗi phút. |
| ISH-M05-003.9 | Khi người dùng gửi yêu cầu gợi ý Topic thứ 11 trong cùng một phút, hệ thống phải từ chối yêu cầu đó. |
| ISH-M05-003.10 | Khi tác giả thay đổi tiêu đề hoặc nội dung văn bản của bài viết sau khi nhận gợi ý Topic, hệ thống phải đánh dấu gợi ý đó là gợi ý cũ. |
| ISH-M05-003.11 | Khi tác giả thay đổi tệp đính kèm của bài viết sau khi nhận gợi ý Topic, hệ thống phải giữ nguyên trạng thái mới hoặc cũ của gợi ý đó. |
| ISH-M05-003.12 | Trong khi gợi ý Topic của bài viết là gợi ý cũ, hệ thống phải hiển thị cảnh báo gợi ý cũ cho tác giả. |
| ISH-M05-003.13 | Trong khi gợi ý Topic của bài viết là gợi ý cũ, hệ thống phải cho phép tác giả yêu cầu gợi ý Topic lại. |
| ISH-M05-003.14 | Trong khi gợi ý Topic của bài viết là gợi ý cũ, hệ thống phải cho phép tác giả gửi bài viết. |

### 5.6 Xử lý kết quả và sự cố của gợi ý Topic

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-004 | Hệ thống phải xử lý kết quả của dịch vụ AI sao cho tác giả luôn chọn được Topic thuộc danh mục Topic để gửi bài viết. |

**Lý do**

Hệ thống cần hoạt động độc lập khi AI tắt; mỗi module có cách xử lý dự phòng rõ ràng, với Topic là người dùng tự chọn, không có gợi ý.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-004.1 | Trong khi chức năng gợi ý Topic bị tắt, hệ thống phải không cung cấp gợi ý Topic cho tác giả. |
| ISH-M05-004.2 | Nếu dịch vụ AI không trả về kết quả gợi ý Topic, thì hệ thống phải thông báo cho tác giả rằng không gợi ý được Topic. |
| ISH-M05-004.3 | Nếu dịch vụ AI không trả về kết quả gợi ý Topic, thì hệ thống phải giữ nguyên lựa chọn Topic hiện tại của bài viết. |
| ISH-M05-004.4 | Nếu dịch vụ AI không trả về kết quả gợi ý Topic, thì hệ thống phải cho phép tác giả gửi bài viết với các Topic tự chọn. |
| ISH-M05-004.5 | Nếu kết quả gợi ý có Topic không thuộc danh mục Topic, thì hệ thống phải bỏ Topic không thuộc danh mục Topic khỏi gợi ý. |
| ISH-M05-004.6 | Nếu kết quả gợi ý không có Topic nào thuộc danh mục Topic, thì hệ thống phải xử lý yêu cầu như khi dịch vụ AI không trả về kết quả gợi ý Topic. |
| ISH-M05-004.7 | Nếu kết quả gợi ý có hơn 3 Topic thuộc danh mục Topic, thì hệ thống phải giữ 3 Topic đầu tiên theo thứ tự dịch vụ AI trả về. |

### 5.7 Ghi nhận phản hồi gợi ý Topic

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-005 | Khi tác giả gửi lần đầu một bài viết có gợi ý Topic còn mới, hệ thống phải ghi nhận phản hồi gợi ý Topic cho bài viết đó. |

**Lý do**

Lựa chọn cuối cùng của người dùng sau gợi ý là phản hồi cho AI, dùng làm cơ chế đánh giá lại chất lượng gợi ý.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-005.1 | Khi ghi nhận phản hồi gợi ý Topic, hệ thống phải lấy gợi ý Topic gần nhất của bài viết cùng các Topic tác giả chọn cuối cùng. |
| ISH-M05-005.2 | Trong khi gợi ý Topic của bài viết là gợi ý cũ, khi tác giả gửi bài viết đó, hệ thống phải không ghi nhận phản hồi gợi ý Topic. |
| ISH-M05-005.3 | Khi tác giả gửi một bài viết chưa từng nhận gợi ý Topic, hệ thống phải không ghi nhận phản hồi gợi ý Topic. |
| ISH-M05-005.5 | Khi tác giả gửi lại một bài viết sau khi bài viết đó bị từ chối, hệ thống phải không ghi thêm phản hồi gợi ý Topic. |

### 5.8 Gắn Tag cho bài viết

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-006 | Hệ thống phải phân loại mỗi bài viết theo từ 0 đến 5 Tag tự do do tác giả nhập, từ lúc soạn đến lúc hiển thị bài viết. |

**Lý do**

Tag là từ khóa tự do do người dùng nhập, chi tiết hơn Topic, không có danh sách cố định.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-006.1 | Khi tác giả tạo bài viết, hệ thống phải cho phép tác giả nhập tên Tag tự do cho bài viết đó mà không giới hạn trong một danh sách có sẵn. |
| ISH-M05-006.2 | Khi tác giả gắn một tên Tag chưa tồn tại cho bài viết, hệ thống phải tạo Tag mới với tên đó mà không cần phê duyệt. |
| ISH-M05-006.3 | Hệ thống phải cho phép tác giả gửi bài viết không có Tag nào. |
| ISH-M05-006.4 | Hệ thống phải giới hạn mỗi bài viết tối đa 5 Tag. |
| ISH-M05-006.5 | Khi tác giả gắn Tag thứ 6 cho một bài viết, hệ thống phải từ chối Tag thứ 6 đó. |
| ISH-M05-006.6 | Hệ thống phải giới hạn tên Tag tối đa 30 ký tự, không tính dấu #. |
| ISH-M05-006.7 | Khi tác giả nhập tên Tag dài hơn 30 ký tự, hệ thống phải từ chối Tag đó. |
| ISH-M05-006.8 | Khi tác giả nhập tên Tag có chứa ký tự trắng ở giữa tên, hệ thống phải từ chối Tag đó. |
| ISH-M05-006.9 | Hệ thống phải coi hai tên Tag chỉ khác nhau về chữ hoa, chữ thường là cùng một Tag. |
| ISH-M05-006.10 | Khi tác giả gắn một Tag đã có trên bài viết, hệ thống phải giữ Tag đó trên bài viết đúng một lần. |
| ISH-M05-006.11 | Khi tác giả sửa một bài viết đã gửi, hệ thống phải cho phép tác giả thay đổi Tag của bài viết đó. |
| ISH-M05-006.12 | Khi một người dùng khác tác giả của bài viết yêu cầu thay đổi Tag của bài viết đó, hệ thống phải từ chối yêu cầu đó. |
| ISH-M05-006.13 | Khi tác giả nhập tên Tag, hệ thống phải bỏ ký tự trắng ở đầu và cuối tên Tag trước khi kiểm tên Tag. |
| ISH-M05-006.14 | Khi tác giả nhập tên Tag rỗng sau khi bỏ dấu # cùng ký tự trắng ở đầu và cuối, hệ thống phải từ chối Tag đó. |
| ISH-M05-006.15 | Hệ thống phải tính mỗi ký tự nhìn thấy, kể cả chữ có dấu tiếng Việt, là một ký tự khi kiểm độ dài tên Tag. |
| ISH-M05-006.16 | Khi người dùng, kể cả Guest, xem một bài viết, hệ thống phải hiển thị các Tag hoạt động của bài viết đó. |

### 5.9 Theo dõi Topic

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-007 | Hệ thống phải cho phép người dùng đã đăng nhập theo dõi một Topic trong danh mục Topic. |

**Lý do**

Người dùng theo dõi để nhận cập nhật về nội dung hoặc chủ đề mình quan tâm, gồm thông báo khi có bài viết mới trong Topic.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-007.1 | Khi người dùng đã đăng nhập yêu cầu theo dõi một Topic trong danh mục Topic mà người dùng đó chưa theo dõi, hệ thống phải ghi nhận người dùng đó đang theo dõi Topic đó. |
| ISH-M05-007.2 | Khi người dùng đã đăng nhập yêu cầu bỏ theo dõi một Topic đang theo dõi, hệ thống phải ghi nhận người dùng đó không còn theo dõi Topic đó. |
| ISH-M05-007.3 | Hệ thống phải hiển thị cho người dùng đã đăng nhập trạng thái đang theo dõi hay chưa theo dõi của người dùng đó với mỗi Topic. |
| ISH-M05-007.4 | Hệ thống phải hiển thị số người đang theo dõi của mỗi Topic. |
| ISH-M05-007.5 | Khi Guest yêu cầu theo dõi một Topic, hệ thống phải từ chối yêu cầu đó. |
| ISH-M05-007.6 | Khi người dùng đã đăng nhập yêu cầu theo dõi một Topic đang theo dõi, hệ thống phải giữ số người theo dõi của Topic đó không đổi. |
| ISH-M05-007.7 | Khi người dùng yêu cầu theo dõi một Topic đã bị loại khỏi danh mục Topic, hệ thống phải từ chối yêu cầu đó. |

### 5.10 Trending Topic và Tag

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-008 | Hệ thống phải xếp hạng các Topic và các Tag theo điểm Trending tính trên 7 ngày gần nhất. |

**Lý do**

Nguồn chưa nêu lý do.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-008.1 | Hệ thống phải tính điểm Trending của một Topic bằng tổng điểm tương tác của mọi bài viết được tính thuộc Topic đó, cộng số bài viết được tính thuộc Topic đó trở thành công khai lần đầu trong 7 ngày gần nhất. |
| ISH-M05-008.2 | Hệ thống phải tính điểm Trending của một Tag bằng tổng điểm tương tác của mọi bài viết được tính gắn Tag đó, cộng số bài viết được tính gắn Tag đó trở thành công khai lần đầu trong 7 ngày gần nhất. |
| ISH-M05-008.3 | Hệ thống phải chỉ tính vào điểm Trending các bài viết công khai không thuộc Group Private. |
| ISH-M05-008.4 | Hệ thống phải chỉ đếm upvote vào chính bài viết, không đếm upvote vào bình luận của bài viết, khi tính điểm Trending. |
| ISH-M05-008.5 | Hệ thống phải đếm mọi bình luận gốc cùng mọi trả lời của bài viết khi tính số bình luận cho điểm Trending. |
| ISH-M05-008.6 | Hệ thống phải không đếm upvote đã bị rút khi tính điểm Trending. |
| ISH-M05-008.7 | Hệ thống phải không đếm bình luận đã bị xóa khi tính điểm Trending. |
| ISH-M05-008.8 | Hệ thống phải xác định 7 ngày gần nhất là 168 giờ tính lùi từ thời điểm tính điểm Trending. |
| ISH-M05-008.9 | Hệ thống phải xếp Topic có điểm Trending cao hơn trước Topic có điểm Trending thấp hơn. |
| ISH-M05-008.10 | Hệ thống phải xếp Tag có điểm Trending cao hơn trước Tag có điểm Trending thấp hơn. |
| ISH-M05-008.11 | Khi hai Topic có cùng điểm Trending, hệ thống phải xếp trước Topic có số bài viết được tính trở thành công khai lần đầu trong 7 ngày gần nhất lớn hơn, rồi đến tên theo thứ tự bảng chữ cái tiếng Việt. |
| ISH-M05-008.12 | Khi hai Tag có cùng điểm Trending, hệ thống phải xếp trước Tag có số bài viết được tính trở thành công khai lần đầu trong 7 ngày gần nhất lớn hơn, rồi đến tên theo thứ tự bảng chữ cái tiếng Việt. |
| ISH-M05-008.13 | Hệ thống phải tính điểm tương tác của một bài viết bằng 2 lần số upvote, cộng số bình luận, cộng số bookmark, cộng 0,1 lần số người xem, mỗi số chỉ đếm phần phát sinh trong 7 ngày gần nhất. |
| ISH-M05-008.14 | Hệ thống phải đếm số người xem của một bài viết là số người dùng đã đăng nhập khác nhau, không kể tác giả, đã mở trang chi tiết bài viết đó trong 7 ngày gần nhất. |
| ISH-M05-008.16 | Hệ thống phải chỉ đếm bookmark do người dùng khác tác giả tạo trong 7 ngày gần nhất mà người dùng đó vẫn còn giữ. |
| ISH-M05-008.17 | Hệ thống phải không đếm bình luận đang bị ẩn bởi kiểm duyệt khi tính điểm Trending. |
| ISH-M05-008.18 | Hệ thống phải đưa mọi Topic trong danh mục Topic vào xếp hạng Trending mà không đặt ngưỡng điểm tối thiểu. |
| ISH-M05-008.19 | Hệ thống phải đưa vào xếp hạng Trending mọi Tag hoạt động đang gắn trên ít nhất một bài viết được tính, mà không đặt ngưỡng điểm tối thiểu. |
| ISH-M05-008.20 | Hệ thống phải loại khỏi xếp hạng Trending mọi Tag không gắn trên bài viết được tính nào. |

### 5.11 Đổi Topic của bài viết bởi Mod và Admin

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-009 | Hệ thống phải cho phép Mod và Admin thay đổi Topic của mọi bài viết. |

**Lý do**

Kết quả phân loại bài viết được người dùng và Mod xem lại.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-009.1 | Khi Mod hoặc Admin lưu thay đổi Topic của một bài viết do người khác viết, hệ thống phải thay Topic của bài viết đó bằng các Topic mới. |
| ISH-M05-009.2 | Khi Guest hoặc một User khác tác giả của bài viết yêu cầu thay đổi Topic của bài viết đó, hệ thống phải từ chối yêu cầu đó. |

### 5.12 Đổi tên Topic

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-010 | Khi Mod hoặc Admin đổi tên một Topic, hệ thống phải thay tên của Topic đó bằng tên mới. |

**Lý do**

Topic dùng để tổ chức các lĩnh vực tri thức lớn, phù hợp đối tượng học sinh THPT; Mod và Admin duy trì danh mục Topic bằng đổi tên và gộp, không xóa Topic.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-010.1 | Khi Mod hoặc Admin đổi tên một Topic, hệ thống phải giữ nguyên các bài viết đang gắn Topic đó. |
| ISH-M05-010.2 | Khi Mod hoặc Admin đổi tên một Topic, hệ thống phải giữ nguyên những người đang theo dõi Topic đó. |
| ISH-M05-010.3 | Khi Guest hoặc User yêu cầu đổi tên một Topic, hệ thống phải từ chối yêu cầu đó. |
| ISH-M05-010.5 | Khi Mod hoặc Admin yêu cầu đổi tên một Topic đã bị loại khỏi danh mục Topic, hệ thống phải từ chối yêu cầu đó. |
| ISH-M05-010.6 | Khi hệ thống từ chối đổi tên vì Topic đã bị loại khỏi danh mục Topic, hệ thống phải thông báo cho Mod hoặc Admin rằng Topic không tồn tại. |

### 5.13 Gộp Topic

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-011 | Khi Mod hoặc Admin gộp một Topic nguồn vào một Topic đích, hệ thống phải chuyển mọi bài viết đang gắn Topic nguồn sang Topic đích. |

**Lý do**

Topic dùng để tổ chức các lĩnh vực tri thức lớn, phù hợp đối tượng học sinh THPT; Mod và Admin duy trì danh mục Topic bằng đổi tên và gộp, không xóa Topic.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-011.1 | Khi Mod hoặc Admin gộp Topic nguồn vào Topic đích, hệ thống phải giữ Topic đích đúng một lần trên mỗi bài viết đã gắn cả Topic nguồn lẫn Topic đích. |
| ISH-M05-011.2 | Khi Mod hoặc Admin gộp Topic nguồn vào Topic đích, hệ thống phải loại Topic nguồn khỏi danh mục Topic. |
| ISH-M05-011.3 | Khi Mod hoặc Admin gộp Topic nguồn vào Topic đích, hệ thống phải chuyển mọi người đang theo dõi Topic nguồn sang theo dõi Topic đích. |
| ISH-M05-011.4 | Khi Mod hoặc Admin gộp Topic nguồn vào Topic đích, hệ thống phải tính mỗi người đang theo dõi cả Topic nguồn lẫn Topic đích đúng một lần trong số người theo dõi Topic đích. |
| ISH-M05-011.5 | Khi Guest hoặc User yêu cầu gộp Topic, hệ thống phải từ chối yêu cầu đó. |
| ISH-M05-011.6 | Khi Mod hoặc Admin gộp Topic nguồn vào Topic đích, hệ thống phải loại Topic nguồn khỏi xếp hạng Trending. |
| ISH-M05-011.8 | Khi Mod hoặc Admin yêu cầu gộp với một Topic nguồn hay Topic đích đã bị loại khỏi danh mục Topic, hệ thống phải từ chối thao tác gộp đó. |
| ISH-M05-011.9 | Khi hệ thống từ chối thao tác gộp vì Topic đã bị loại khỏi danh mục Topic, hệ thống phải thông báo cho Mod hoặc Admin rằng Topic không tồn tại. |
| ISH-M05-011.10 | Khi Mod hoặc Admin yêu cầu gộp một Topic vào chính Topic đó, hệ thống phải từ chối thao tác gộp đó. |

### 5.14 Vô hiệu hóa và mở lại Tag

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-012 | Hệ thống phải giới hạn thao tác quản trị Tag ở việc Mod, Admin vô hiệu hóa, mở lại một Tag. |

**Lý do**

Tag hoàn toàn tự do; Mod và Admin không sửa, gộp hay xóa Tag trong điều kiện bình thường, chỉ vô hiệu hóa Tag trong tình huống khẩn cấp.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-012.1 | Khi Mod hoặc Admin vô hiệu hóa một Tag, hệ thống phải ẩn Tag đó trên mọi bài viết đang gắn Tag đó. |
| ISH-M05-012.2 | Khi Mod hoặc Admin vô hiệu hóa một Tag, hệ thống phải giữ liên kết giữa Tag đó với các bài viết đang gắn Tag đó. |
| ISH-M05-012.3 | Trong khi một Tag bị vô hiệu hóa, hệ thống phải loại Tag đó khỏi xếp hạng Trending. |
| ISH-M05-012.4 | Trong khi một Tag bị vô hiệu hóa, khi tác giả nhập tên Tag đó cho một bài viết, hệ thống phải không gắn Tag đó vào bài viết. |
| ISH-M05-012.5 | Khi Mod hoặc Admin mở lại một Tag bị vô hiệu hóa, hệ thống phải hiển thị lại Tag đó trên mọi bài viết đang gắn Tag đó. |
| ISH-M05-012.6 | Khi Mod hoặc Admin mở lại một Tag bị vô hiệu hóa, hệ thống phải cho phép tác giả gắn Tag đó cho bài viết. |
| ISH-M05-012.7 | Khi Guest hoặc User yêu cầu vô hiệu hóa một Tag, hệ thống phải từ chối yêu cầu đó. |
| ISH-M05-012.8 | Khi Guest hoặc User yêu cầu mở lại một Tag, hệ thống phải từ chối yêu cầu đó. |
| ISH-M05-012.9 | Khi người dùng yêu cầu đổi tên một Tag, hệ thống phải từ chối yêu cầu đó. |
| ISH-M05-012.10 | Khi người dùng yêu cầu gộp hai Tag, hệ thống phải từ chối yêu cầu đó. |
| ISH-M05-012.11 | Khi người dùng yêu cầu xóa một Tag, hệ thống phải từ chối yêu cầu đó. |

### 5.15 Yêu cầu HMI

Sẽ bổ sung sau khi có thiết kế.

### 5.16 Chuyển màn hình

Sẽ bổ sung sau khi có thiết kế.

## 6. Lịch sử sửa đổi

| Phiên bản | Ngày | Mô tả | Người sửa |
|---|---|---|---|
| 0.1 | 2026-10-04 | Bản nháp đầu tiên (chu kỳ audit mới, sau khi thay bộ skill; câu trả lời của stakeholder ghi ở ISS-211…227, QA-271…287, DEC-143…153) | Phạm Văn Đức |
| 0.2 | 2026-10-05 | Sửa theo ISH-AUD-M05-r1 và câu trả lời ISS-228…236 (DEC-154…159). Thêm: 001.5, 002.10, 002.11, 005.4, 006.16, 008.13…008.19, 011.6…011.10. Sửa nội dung: 001, 002, 002.6 (chỉ bài đã gửi), 003.11, 004 (đổi tên tính năng thành "Xử lý kết quả và sự cố của gợi ý Topic"), 005, 005.1, 006, 008.1, 008.2, 008.11, 008.12, 012; Lý do 5.9, 5.12, 5.13; 2.1 (Danh mục Topic, Bài viết công khai, Upvote, Theo dõi Topic, 7 ngày gần nhất; thêm Bài viết được tính, Trở thành công khai lần đầu, Bookmark, Người xem, Điểm tương tác, Thứ tự bảng chữ cái tiếng Việt); 5.2 thêm trạng thái theo dõi. Bỏ: ISH-M05-002.4 (thay bằng 002.5, 002.6 và 002.11 theo DEC-156; câu cũ áp dụng cả bản nháp); ISH-M05-010.4 (chuyển thành ISH-M05-001.5 để cấp trên bao quát). Cơ sở 005.3 giữ; 006.12, 012.9…012.11 đổi sang Suy ra; 005.1 theo DEC-157. Thêm OP-M05-11, OP-M05-12. Mục 4: Topic "11 lĩnh vực chốt sẵn, không ai thêm hay xóa được", bài "đã gửi" có 1–3 Topic, Trending tính cả bookmark và người xem. Mục 5.1: ngoại lệ mốc P1 cho 011.6, 011.7. Mục 5.2: thêm hàng từ chối theo dõi/gộp Topic đã loại | Phạm Văn Đức |
| 0.3 | 2026-10-05 | Sửa theo ISH-AUD-M05-r2 và câu trả lời ISS-237…242 (DEC-160…163). Thêm: 005.5, 007.7, 010.5. Sửa nội dung: 002 và 006 (cấp trên bao quát soạn và hiển thị), 002.11 (mẫu câu), 005 (lần gửi đầu), 007 và 007.1 (Topic trong danh mục), 008.19 (chỉ Tag có bài viết được tính, DEC-161); 2.1 Thứ tự bảng chữ cái tiếng Việt (DEC-160); 5.1 bỏ ngoại lệ của 011.7; 5.2 trỏ 007.7. Bỏ: ISH-M05-005.4 (thay bằng cấp trên 005 "gửi lần đầu" và 005.5 theo DEC-162), ISH-M05-008.15 (trùng ý với 008.14), ISH-M05-011.7 (chuyển thành ISH-M05-007.7 để cấp trên bao quát). Xóa OP-M05-10 (đã trả lời ở DEC-162). Truy vết 006.16 đổi sang Suy ra | Phạm Văn Đức |
| 0.4 | 2026-10-05 | Sửa sau đợt xác minh ISH-AUD-M05-v1 (Chưa đạt), theo quyết định của stakeholder, ngoài chu kỳ audit: bản này chưa được Auditor kiểm lại. AUD-27: thêm 008.20 (vế "chỉ" của DEC-161). AUD-34: 2.1 "Thứ tự bảng chữ cái tiếng Việt" theo DEC-164 (ISS-243, QA-303). AUD-33: 010.5 đổi cơ sở sang Nói thẳng theo DEC-165 (ISS-244, QA-304); thêm 010.6 (thông báo Topic không tồn tại) | Phạm Văn Đức |

## Phụ lục A. Truy vết nguồn

| ID | Nguồn | Cơ sở | Ghi chú |
|---|---|---|---|
| ISH-M05-001 | DEC-047, DEC-048, DEC-140, DEC-049, ISS-079, ISS-080, ISS-207, QA-101, QA-102, QA-267 | Nói thẳng | Danh mục chốt ("final", "cố định"); không xóa Topic (DEC-049) |
| ISH-M05-001.1 | DEC-048, ISS-080, QA-102, DRAFT §3.1 | Nói thẳng | DRAFT §3.1 nói danh sách chưa cố định, chốt ở BA; DEC-048 là danh sách chốt |
| ISH-M05-001.2 | DEC-140, DEC-047, QA-267 | Nói thẳng | Phẳng, không Category riêng; ghi đè 2 tầng của QA-033 |
| ISH-M05-001.3 | QA-011 | Nói thẳng | Guest "Xem danh sách Topic / Tag / Khối lớp" |
| ISH-M05-001.4 | DEC-048, QA-267 | Nói thẳng | "Topic list (11, final)"; "11 giá trị cố định" |
| ISH-M05-001.5 | DEC-049, ISS-084, QA-107 | Nói thẳng | "No delete" (thay cho ISH-M05-010.4 đã bỏ) |
| ISH-M05-002 | DEC-049, ISS-083, DEC-143, ISS-211, QA-271, DEC-156, ISS-230, QA-290, QA-011, DRAFT §3.4 | Nói thẳng | Register ghi đè sơ đồ một Topic ở DRAFT §3.4 (DEC-143); 1–3 cho bài đã gửi (DEC-156); hiển thị trên bài (QA-011) |
| ISH-M05-002.1 | DEC-050, DEC-047 | Nói thẳng | "user picks from dropdown"; Topic do người dùng xác nhận |
| ISH-M05-002.2 | DEC-047, QA-267 | Nói thẳng | Danh mục cố định; Topic chọn từ danh mục |
| ISH-M05-002.3 | DEC-050 | Nói thẳng | "User manually picks topic from start → skips AI flow entirely" |
| ISH-M05-002.5 | DEC-049, DEC-156 | Suy ra | Giới hạn tối thiểu 1, kiểm khi gửi (DEC-156) ⇒ từ chối gửi bài khi có 0 Topic (RULES §4.5) |
| ISH-M05-002.6 | DEC-049, DEC-144, DEC-156 | Suy ra | Giới hạn tối thiểu 1 áp dụng cho mọi lần đổi (DEC-144) ⇒ từ chối thay đổi làm còn 0 Topic (RULES §4.5) |
| ISH-M05-002.7 | DEC-049, ISS-083, QA-103 | Nói thẳng | "max 3 topics/post" |
| ISH-M05-002.8 | DEC-049 | Suy ra | Giới hạn tối đa 3 ⇒ từ chối Topic thứ 4 (RULES §4.5) |
| ISH-M05-002.9 | DEC-144, ISS-213, QA-273 | Nói thẳng | |
| ISH-M05-002.10 | QA-011 | Nói thẳng | Guest "Xem AI Classification trên post": phân loại hiển thị trên bài; chủ sở hữu hiển thị ở OP-M05-12 |
| ISH-M05-002.11 | DEC-156, ISS-230, QA-290 | Nói thẳng | |
| ISH-M05-003 | DEC-050, ISS-081, QA-103, QA-017 | Nói thẳng | |
| ISH-M05-003.1 | DEC-050, QA-017 | Nói thẳng | "button (not automatic)"; "không auto-gán" |
| ISH-M05-003.2 | DEC-050, ISS-081 | Nói thẳng | "AI analyzes text only (title + content_text, no attachment processing)" |
| ISH-M05-003.3 | DEC-050, QA-103 | Nói thẳng | "suggest max 3 topics" |
| ISH-M05-003.4 | DEC-050, DEC-148, ISS-219, QA-279 | Nói thẳng | "pre-ticked"; thay thế lựa chọn đang có (DEC-148) |
| ISH-M05-003.5 | DEC-050 | Nói thẳng | "User adjusts freely → publish" |
| ISH-M05-003.6 | DEC-147, ISS-218, QA-278, DEC-050 | Nói thẳng | Ngưỡng 10 tiếng trên tiêu đề + nội dung, sửa "<20 words" của DEC-050 |
| ISH-M05-003.7 | DEC-050, DEC-147 | Nói thẳng | "shown 'content too short'"; văn bản cụ thể ở routing R3 |
| ISH-M05-003.8 | DEC-100, ISS-129, QA-178 | Nói thẳng | "Topic Suggest button — 10 requests/min/user" |
| ISH-M05-003.9 | DEC-100 | Suy ra | Giới hạn tối đa 10 mỗi phút ⇒ từ chối yêu cầu thứ 11 (RULES §4.5); cửa sổ đếm ở routing R2 |
| ISH-M05-003.10 | DEC-050, DEC-148, ISS-220, QA-104, QA-280 | Nói thẳng | "Content changed after suggest → flag is_stale"; tiêu đề hoặc nội dung (DEC-148) |
| ISH-M05-003.11 | DEC-148, QA-280 | Nói thẳng | "attachment changes do not count": trạng thái gợi ý không đổi |
| ISH-M05-003.12 | DEC-050, QA-104 | Nói thẳng | "soft warning" |
| ISH-M05-003.13 | DEC-050 | Nói thẳng | "re-suggest button" |
| ISH-M05-003.14 | DEC-050 | Nói thẳng | "does not block publish" |
| ISH-M05-004 | DEC-008, DEC-099, DEC-132, DEC-149, DEC-152 | Nói thẳng | |
| ISH-M05-004.1 | DEC-008, DEC-093, DEC-050, ISS-122, QA-165 | Nói thẳng | "AI off → user picks from dropdown, no suggest"; công tắc tổng và công tắc gợi ý Topic (DEC-093) |
| ISH-M05-004.2 | DEC-099 | Nói thẳng | "Topic suggest→show non-blocking error" |
| ISH-M05-004.3 | DEC-099 | Nói thẳng | "no action taken" |
| ISH-M05-004.4 | DEC-099, DEC-132 | Nói thẳng | Lỗi "non-blocking"; "the user selects manually" |
| ISH-M05-004.5 | DEC-132, DEC-149, ISS-194, ISS-221, QA-253, QA-281 | Nói thẳng | Kiểm theo danh mục; bỏ phần không hợp lệ (DEC-149) |
| ISH-M05-004.6 | DEC-132, DEC-149 | Nói thẳng | Không còn Topic hợp lệ ⇒ coi như gợi ý thất bại |
| ISH-M05-004.7 | DEC-152, ISS-225, QA-285 | Nói thẳng | |
| ISH-M05-005 | DEC-050, QA-104, QA-017, DEC-162 | Nói thẳng | "only recorded when not stale"; chỉ lần gửi đầu (DEC-162) |
| ISH-M05-005.1 | DEC-157, ISS-233, QA-293, DEC-050 | Nói thẳng | "compares only the latest suggestion with the final selection" |
| ISH-M05-005.2 | DEC-050, QA-104 | Nói thẳng | "only recorded when not stale" |
| ISH-M05-005.3 | DEC-050 | Suy ra | "manually picks topic from start → skips AI flow entirely" ⇒ không có gợi ý nên không có phản hồi để ghi |
| ISH-M05-005.5 | DEC-162, ISS-239, QA-299 | Nói thẳng | "only on the first submission"; cùng cấp trên 005 bảo đảm tối đa một bản ghi mỗi bài |
| ISH-M05-006 | DEC-051, DEC-143, ISS-082, ISS-212, QA-105, QA-272, DRAFT §3.2 | Nói thẳng | Register ghi đè "không giới hạn" của DRAFT §3.2 (DEC-143); phần hiển thị xem ISH-M05-006.16 |
| ISH-M05-006.1 | DEC-047, QA-101, DRAFT §3.3 | Nói thẳng | "user-typed, no fixed list" |
| ISH-M05-006.2 | DEC-051 | Nói thẳng | "Auto-created, no approval" |
| ISH-M05-006.3 | DEC-143, QA-272 | Nói thẳng | Tag không bắt buộc, 0 Tag hợp lệ |
| ISH-M05-006.4 | DEC-051, QA-105, DEC-143 | Nói thẳng | "Max 5 tags/post" |
| ISH-M05-006.5 | DEC-051 | Suy ra | Giới hạn tối đa 5 ⇒ từ chối Tag thứ 6 (RULES §4.5) |
| ISH-M05-006.6 | DEC-051, QA-105, DEC-150, ISS-223, QA-283 | Nói thẳng | "max 30 chars/tag"; không tính "#" (DEC-150) |
| ISH-M05-006.7 | DEC-051 | Suy ra | Giới hạn tối đa 30 ký tự ⇒ từ chối tên dài hơn (RULES §4.5) |
| ISH-M05-006.8 | DEC-047, QA-101 | Suy ra | "no spaces" ⇒ từ chối tên có khoảng trắng (RULES §4.2 mục 8) |
| ISH-M05-006.9 | DEC-051 | Nói thẳng | "name unique lowercase-normalized" |
| ISH-M05-006.10 | DEC-051 | Suy ra | Tag duy nhất theo tên ⇒ cùng một Tag trên một bài viết chỉ là một Tag; không quyết định cách thể hiện |
| ISH-M05-006.11 | DEC-144, ISS-213, QA-273 | Nói thẳng | |
| ISH-M05-006.12 | DEC-144, QA-273 | Suy ra | Nguồn: chỉ tác giả đổi Tag, Mod/Admin không đổi Tag của bài ⇒ mọi người dùng khác tác giả bị từ chối ("chỉ X mới được làm Y", RULES §4.5) |
| ISH-M05-006.13 | DEC-152, ISS-226, QA-286 | Nói thẳng | |
| ISH-M05-006.14 | DEC-152, QA-286 | Nói thẳng | |
| ISH-M05-006.15 | DEC-152, QA-286 | Nói thẳng | |
| ISH-M05-006.16 | DEC-051, DEC-150, QA-011 | Suy ra | DEC-051 ẩn chip Tag bị vô hiệu hóa "from display" và DEC-150 "shows again" khi mở lại ⇒ Tag hoạt động được hiển thị trên bài; QA-011 cho Guest xem bài viết. Chủ sở hữu hiển thị ở OP-M05-12 |
| ISH-M05-007 | DEC-141, ISS-208, QA-268, QA-043, ISS-051, DEC-155, ISS-229, QA-289, DEC-145, DRAFT §4.5 | Nói thẳng | Thông báo bài mới do M07 gửi (DEC-155, routing R5); chỉ Topic trong danh mục (DEC-145) |
| ISH-M05-007.1 | DEC-141, QA-043, DEC-145 | Nói thẳng | "Follow/Unfollow behaviour for Topic" |
| ISH-M05-007.2 | DEC-141, QA-268 | Nói thẳng | "nút Follow/Unfollow" |
| ISH-M05-007.3 | DEC-141, QA-268 | Nói thẳng | "follow state" |
| ISH-M05-007.4 | DEC-141, QA-268 | Nói thẳng | "follower count" |
| ISH-M05-007.5 | DEC-126, QA-227, QA-011 | Nói thẳng | "All interactions (… follow …) require login" |
| ISH-M05-007.6 | DEC-141 | Suy ra | Theo dõi là một trạng thái có hoặc không ⇒ theo dõi lần nữa không tăng số người theo dõi |
| ISH-M05-007.7 | DEC-145, QA-274 | Nói thẳng | "can no longer be … followed" (thay cho ISH-M05-011.7 đã bỏ) |
| ISH-M05-008 | DEC-052, DEC-142, DEC-158, QA-106, ISS-082, ISS-210, ISS-234, QA-270, QA-294, DRAFT §7.2 | Nói thẳng | DRAFT §7.2 nêu tín hiệu "có thể"; register chốt công thức (DEC-052, DEC-142, DEC-158), stakeholder đã xác nhận (QA-294) |
| ISH-M05-008.1 | DEC-142, QA-270, DEC-052, DEC-154, ISS-228, QA-288, DEC-158 | Nói thẳng | Tổng điểm tương tác + số bài mới; "created" = trở thành công khai lần đầu (DEC-154) |
| ISH-M05-008.2 | DEC-142, QA-270, DEC-052, DEC-154, DEC-158 | Nói thẳng | Cùng công thức cho Tag |
| ISH-M05-008.3 | DEC-146, ISS-216, QA-276, DEC-033, QA-236 | Nói thẳng | Không loại theo trạng thái tác giả (QA-236, nhắc lại ở DEC-146) |
| ISH-M05-008.4 | DEC-146, ISS-217, QA-277 | Nói thẳng | |
| ISH-M05-008.5 | DEC-146, QA-277 | Nói thẳng | |
| ISH-M05-008.6 | DEC-146, QA-277 | Nói thẳng | "only interactions that still exist count" |
| ISH-M05-008.7 | DEC-146, QA-277 | Nói thẳng | "only interactions that still exist count" |
| ISH-M05-008.8 | DEC-052 | Nói thẳng | "Rolling 7-day window (sliding from now…)" |
| ISH-M05-008.9 | DEC-153, ISS-227, QA-287 | Nói thẳng | |
| ISH-M05-008.10 | DEC-153, QA-287 | Nói thẳng | |
| ISH-M05-008.11 | DEC-153, QA-287, DEC-154, ISS-232, QA-292, DEC-160, ISS-237, QA-297, DEC-164, ISS-243, QA-303 | Nói thẳng | Thứ tự so tên ở 2.1 (DEC-160, DEC-164) |
| ISH-M05-008.12 | DEC-153, QA-287, DEC-154, QA-292, DEC-160, QA-297, DEC-164, QA-303 | Nói thẳng | Thứ tự so tên ở 2.1 (DEC-160, DEC-164) |
| ISH-M05-008.13 | DEC-158, QA-294, DEC-142, DRAFT §7.2 | Nói thẳng | 2 × upvote + bình luận + bookmark + 0,1 × người xem |
| ISH-M05-008.14 | DEC-158, QA-294, DEC-163 | Nói thẳng | "distinct logged-in users other than the author who opened the post detail page"; "Guest views are not counted"; ghi nhận lượt mở trang do M03 (DEC-163) |
| ISH-M05-008.16 | DEC-158, QA-294 | Nói thẳng | "created within the window that still exist, excluding the author's own" |
| ISH-M05-008.17 | DEC-154, ISS-231, QA-291 | Nói thẳng | |
| ISH-M05-008.18 | QA-235, ISS-175 | Nói thẳng | "Không đặt ngưỡng cho MS1" (provisional) |
| ISH-M05-008.19 | QA-235, ISS-175, DEC-161, ISS-238, QA-298, DEC-051 | Nói thẳng | Không ngưỡng điểm; chỉ Tag có ít nhất một bài viết được tính (DEC-161); Tag bị vô hiệu hóa đã loại theo ISH-M05-012.3 |
| ISH-M05-008.20 | DEC-161, QA-298 | Nói thẳng | "includes only active Tags currently attached to at least one counted post" |
| ISH-M05-009 | DEC-144, ISS-213, QA-273, DRAFT §11.2 | Nói thẳng | |
| ISH-M05-009.1 | DEC-144, QA-273 | Nói thẳng | |
| ISH-M05-009.2 | DEC-144 | Suy ra | Chỉ tác giả, Mod, Admin được đổi Topic ⇒ từ chối người khác (RULES §4.5) |
| ISH-M05-010 | DEC-049, ISS-084, QA-107, DEC-090, ISS-119, QA-160 | Nói thẳng | "Mod/admin: edit (rename)" |
| ISH-M05-010.1 | DEC-049 | Suy ra | Đổi tên giữ nguyên Topic, chỉ đổi tên ⇒ các bài viết vẫn gắn Topic đó |
| ISH-M05-010.2 | DEC-049, DEC-141 | Suy ra | Đổi tên giữ nguyên Topic ⇒ quan hệ theo dõi vẫn giữ |
| ISH-M05-010.3 | DEC-049, DEC-090 | Suy ra | Chỉ Mod/Admin được đổi tên ⇒ từ chối người khác (RULES §4.5) |
| ISH-M05-010.5 | DEC-165, ISS-244, QA-304 | Nói thẳng | |
| ISH-M05-010.6 | DEC-165, QA-304 | Nói thẳng | Văn bản thông báo ở routing R3 |
| ISH-M05-011 | DEC-049, DEC-090 | Nói thẳng | "Merge auto re-points post_topics from source to target" |
| ISH-M05-011.1 | DEC-049 | Suy ra | Chuyển liên kết từ nguồn sang đích ⇒ bài có cả hai chỉ còn Topic đích một lần |
| ISH-M05-011.2 | DEC-145, ISS-214, QA-274 | Nói thẳng | |
| ISH-M05-011.3 | DEC-145, ISS-215, QA-275 | Nói thẳng | |
| ISH-M05-011.4 | DEC-145, QA-275 | Nói thẳng | "a user who followed both counts once" |
| ISH-M05-011.5 | DEC-049, DEC-090 | Suy ra | Chỉ Mod/Admin được gộp ⇒ từ chối người khác (RULES §4.5) |
| ISH-M05-011.6 | DEC-145, QA-274 | Nói thẳng | "can no longer be … ranked in Trending" |
| ISH-M05-011.8 | DEC-159, ISS-236, QA-296 | Nói thẳng | |
| ISH-M05-011.9 | DEC-159, QA-296 | Nói thẳng | Văn bản thông báo ở routing R3 |
| ISH-M05-011.10 | DEC-159, QA-296 | Nói thẳng | |
| ISH-M05-012 | DEC-051, DEC-150, QA-107, DEC-090, ISS-084 | Nói thẳng | "mod/admin do NOT edit/merge/delete under normal conditions"; chỉ vô hiệu hóa, mở lại |
| ISH-M05-012.1 | DEC-051 | Nói thẳng | "tag chip hidden from display" |
| ISH-M05-012.2 | DEC-051 | Nói thẳng | "old posts keep post_tags record" |
| ISH-M05-012.3 | DEC-051 | Nói thẳng | "hidden from … trending" |
| ISH-M05-012.4 | DEC-051, QA-107 | Nói thẳng | "if user retypes a disabled tag name, it's NOT tagified" |
| ISH-M05-012.5 | DEC-150, ISS-222, QA-282 | Nói thẳng | |
| ISH-M05-012.6 | DEC-150, QA-282 | Nói thẳng | "can be used normally" |
| ISH-M05-012.7 | DEC-051, DEC-090 | Suy ra | Chỉ Mod/Admin vô hiệu hóa ⇒ từ chối người khác (RULES §4.5) |
| ISH-M05-012.8 | DEC-150 | Suy ra | Chỉ Mod/Admin mở lại ⇒ từ chối người khác (RULES §4.5) |
| ISH-M05-012.9 | DEC-051, ISS-084, QA-107 | Suy ra | Nguồn: Mod/Admin không sửa Tag; vai trò thấp hơn không có quyền hơn Mod/Admin ⇒ mọi người dùng bị từ chối |
| ISH-M05-012.10 | DEC-051 | Suy ra | Nguồn: Mod/Admin không gộp Tag ⇒ mọi người dùng bị từ chối (như 012.9) |
| ISH-M05-012.11 | DEC-051, QA-107 | Suy ra | Nguồn: Mod/Admin không xóa Tag, chỉ vô hiệu hóa khi khẩn cấp ⇒ mọi người dùng bị từ chối (như 012.9) |

## Phụ lục B. Điểm cần làm rõ (tạm thời)

| ID | Nội dung | Loại | Trạng thái |
|---|---|---|---|
| OP-M05-01 | Tính năng Trending Topic và Tag (ISH-M05-008) chưa có lý do trong nguồn. Đề xuất mặc định: "Cho người dùng thấy lĩnh vực và từ khóa đang được thảo luận nhiều trong tuần qua." | Đề xuất | Mở |
| OP-M05-02 | Gợi ý Topic khi sửa bài viết đã gửi có được dùng không (ISH-M05-003 hiện chỉ nêu bài viết mới). Đề xuất mặc định: có, cùng quy tắc như khi soạn bài viết mới. | Đề xuất | Mở |
| OP-M05-04 | Đổi tên Topic thành tên rỗng hoặc trùng tên một Topic khác (ISH-M05-010). Đề xuất mặc định: từ chối cả hai trường hợp. | Đề xuất | Mở |
| OP-M05-05 | Tag bị vô hiệu hóa còn gắn trên bài viết có tính vào giới hạn 5 Tag của bài viết đó không (ISH-M05-006.4, ISH-M05-012.2). Đề xuất mặc định: không tính. | Đề xuất | Mở |
| OP-M05-06 | Số người theo dõi Topic (ISH-M05-007.4) hiển thị cho ai và có tính tài khoản bị khóa hoặc đã xóa không. Đề xuất mặc định: hiển thị cho mọi người kể cả Guest; không tính tài khoản đã xóa. | Đề xuất | Mở |
| OP-M05-07 | Khi Mod hoặc Admin đổi Topic của bài viết (ISH-M05-009.1), tác giả có được thông báo không (thuộc M07). Đề xuất mặc định: không thông báo ở phạm vi hiện tại. | Đề xuất | Mở |
| OP-M05-08 | Tên Tag hiển thị theo chữ thường hay theo cách viết lần đầu (liên quan ISH-M05-006.9). Đề xuất mặc định: hiển thị bằng chữ thường, khớp tên đã chuẩn hóa. | Đề xuất | Mở |
| OP-M05-09 | Tên Tag được chứa những ký tự nào ngoài chữ và số (ví dụ "C++", "KT&PL"). Đề xuất mặc định: mọi ký tự trừ ký tự trắng và dấu #. | Đề xuất | Mở |
| OP-M05-11 | Yêu cầu gợi ý Topic bị từ chối vì văn bản ít hơn 10 tiếng có bị tính vào giới hạn 10 yêu cầu mỗi phút không (ISH-M05-003.8). Đề xuất mặc định: không tính. | Đề xuất | Mở |
| OP-M05-12 | Việc hiển thị Topic và Tag trên trang bài viết (ISH-M05-002.10, ISH-M05-006.16) thuộc M05 hay M03 (trang bài viết). Đề xuất mặc định: M05 sở hữu, M03 tham chiếu. | Đề xuất | Mở |
