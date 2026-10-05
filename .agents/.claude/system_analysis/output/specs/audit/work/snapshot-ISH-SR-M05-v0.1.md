# Tài liệu yêu cầu hệ thống — M05 Topic & Tag
<!-- [Vietnamese Doc] -->

| Mã tài liệu | ISH-SR-M05 |
|---|---|
| Dự án | iShare |
| Module | M05 — Topic & Tag |
| Trạng thái | Bản nháp |
| Phiên bản | 0.1 |
| Ngày | 2026-10-04 |
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
| Danh mục Topic | Tập Topic một tầng mà hệ thống cho phép chọn cho bài viết. |
| Topic nguồn | Topic bị gộp vào một Topic khác. |
| Topic đích | Topic nhận các bài viết của Topic nguồn khi gộp. |
| Tag | Từ khóa tự do dạng #hashtag do người dùng nhập, chi tiết hơn Topic; không có danh sách cố định. |
| Tên Tag | Phần chữ của Tag, không gồm dấu #. |
| Tag bị vô hiệu hóa | Tag mà Mod hoặc Admin đã vô hiệu hóa trong tình huống khẩn cấp; ngược lại là Tag hoạt động. |
| Bài viết | Nội dung do người dùng đăng, gồm tiêu đề, nội dung văn bản và tệp đính kèm. |
| Tác giả | Người dùng đã tạo bài viết. |
| Gửi bài viết | Thao tác của tác giả chuyển bài viết từ bản nháp sang chờ xuất bản. |
| Bài viết công khai | Bài viết đã xuất bản và không bị ẩn bởi kiểm duyệt. |
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
| Theo dõi Topic | Quan hệ giữa một người dùng đã đăng nhập và một Topic mà người dùng đó muốn nhận cập nhật. |
| Upvote | Lượt đánh giá tích cực của người dùng cho một bài viết. |
| Bình luận | Bình luận gốc hoặc trả lời trong một bài viết. |
| Điểm Trending | Điểm xếp hạng mức độ sôi nổi của một Topic hoặc một Tag trong 7 ngày gần nhất. |
| 7 ngày gần nhất | Khoảng 168 giờ tính lùi từ thời điểm tính điểm Trending. |

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
| DRAFT | iShare_modules.md §3.1, §3.2, §3.3, §3.4, §4.5, §11.2 | 2026-10-04 |
| DRAFT | iShare_dev_priority.md §3 (mốc triển khai) | 2026-10-04 |
| REG | decisions.md: DEC-008, DEC-033, DEC-047…054, DEC-056, DEC-058, DEC-060, DEC-065, DEC-090, DEC-093, DEC-096, DEC-099, DEC-100, DEC-124…126, DEC-132, DEC-133, DEC-140…153 | 2026-10-04 |
| REG | issue-queue.md: ISS-046, ISS-051, ISS-079…086, ISS-088, ISS-090, ISS-093, ISS-119, ISS-122, ISS-125, ISS-129, ISS-166, ISS-175, ISS-176, ISS-185, ISS-194, ISS-195, ISS-207…227 | 2026-10-04 |
| REG | qa-log.md: QA-011, QA-017, QA-033, QA-034, QA-043, QA-101…109, QA-113, QA-115, QA-123, QA-160, QA-165, QA-169, QA-175, QA-178, QA-226, QA-227, QA-235…237, QA-253, QA-254, QA-267…287 | 2026-10-04 |
| REG | module-registry.md (dòng M05) | 2026-10-04 |

### 3.2 Tài liệu liên quan

Không có.

## 4. Tổng quan chức năng

Module M05 quản lý hai trục phân loại bài viết. Topic là danh mục một tầng gồm các lĩnh vực tri thức cố định; mỗi bài viết thuộc từ một đến ba Topic. Tag là từ khóa tự do do người dùng nhập, tối đa năm Tag mỗi bài viết, tự tạo khi được dùng lần đầu.

Khi soạn bài viết, tác giả có thể tự chọn Topic hoặc yêu cầu AI gợi ý Topic từ tiêu đề và nội dung. Gợi ý chỉ mang tính đề xuất; tác giả luôn quyết định cuối cùng, và khi AI tắt hoặc lỗi thì tác giả vẫn tự chọn Topic để đăng bài. Lựa chọn cuối cùng so với gợi ý được ghi nhận làm phản hồi cho AI.

Người dùng đã đăng nhập có thể theo dõi Topic. Module tính điểm Trending cho Topic và Tag trên 7 ngày gần nhất để module Feed hiển thị. Mod và Admin đổi Topic của bài viết, đổi tên và gộp Topic (không xóa Topic), và vô hiệu hóa hoặc mở lại Tag khi khẩn cấp.

### 4.1 Luật và tiêu chuẩn liên quan

Không có.

## 5. Yêu cầu chức năng

### 5.1 Tổng quan yêu cầu

| Tính năng | Yêu cầu cấp trên | Mức ưu tiên | Mốc | Ngoại lệ |
|---|---|---|---|---|
| Danh mục Topic | ISH-M05-001 | Must | P0 | — |
| Gán Topic cho bài viết | ISH-M05-002 | Must | P0 | — |
| Gợi ý Topic bằng AI | ISH-M05-003 | Must | AI-P0 | — |
| Gợi ý Topic khi AI không khả dụng | ISH-M05-004 | Must | AI-P0 | — |
| Ghi nhận phản hồi gợi ý Topic | ISH-M05-005 | Must | AI-P1 | — |
| Gắn Tag cho bài viết | ISH-M05-006 | Must | P0 | — |
| Theo dõi Topic | ISH-M05-007 | Must | P1 | — |
| Trending Topic và Tag | ISH-M05-008 | Must | P1 | — |
| Đổi Topic của bài viết bởi Mod và Admin | ISH-M05-009 | Must | P0 | — |
| Đổi tên Topic | ISH-M05-010 | Must | P0 | ISH-M05-010.2: P1 |
| Gộp Topic | ISH-M05-011 | Must | P0 | ISH-M05-011.3, ISH-M05-011.4: P1 |
| Vô hiệu hóa và mở lại Tag | ISH-M05-012 | Must | P0 | ISH-M05-012.3: P1 |

### 5.2 Chuyển trạng thái

| Trạng thái hiện tại | Sự kiện hoặc điều kiện | Trạng thái mới | ID yêu cầu |
|---|---|---|---|
| Tag hoạt động | Mod hoặc Admin vô hiệu hóa Tag | Tag bị vô hiệu hóa | ISH-M05-012.1 |
| Tag bị vô hiệu hóa | Mod hoặc Admin mở lại Tag | Tag hoạt động | ISH-M05-012.5 |
| Topic trong danh mục Topic | Topic được gộp làm Topic nguồn | Topic đã loại khỏi danh mục Topic (trạng thái cuối) | ISH-M05-011.2 |
| Gợi ý còn mới | Tác giả thay đổi tiêu đề hoặc nội dung văn bản | Gợi ý cũ | ISH-M05-003.10 |
| Gợi ý cũ | Tác giả yêu cầu gợi ý lại và nhận gợi ý mới | Gợi ý còn mới | ISH-M05-003.4, ISH-M05-003.13 |

### 5.3 Danh mục Topic

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-001 | Hệ thống phải cung cấp một danh mục Topic một tầng gồm các Topic cố định. |

**Lý do**

Topic dùng để tổ chức các lĩnh vực tri thức lớn, phù hợp đối tượng học sinh THPT. Topic là phân loại có cấu trúc, dùng để lọc và duyệt nội dung.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-001.1 | Hệ thống phải khởi tạo danh mục Topic với đúng 11 Topic sau: Toán học, Ngữ văn, Ngoại ngữ, Khoa học tự nhiên (Lý/Hóa/Sinh), Khoa học xã hội (Sử/Địa/KT&PL), Tin học, Kỹ năng mềm, Hướng nghiệp, Nghệ thuật & Sáng tạo, Góc Chill, Khác. |
| ISH-M05-001.2 | Hệ thống phải tổ chức danh mục Topic thành một tầng, không có tầng phân loại cha phía trên Topic. |
| ISH-M05-001.3 | Hệ thống phải cho phép mọi người dùng, kể cả Guest, xem danh sách Topic trong danh mục Topic. |
| ISH-M05-001.4 | Hệ thống phải không cho phép thêm Topic mới vào danh mục Topic. |

### 5.4 Gán Topic cho bài viết

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-002 | Hệ thống phải yêu cầu mỗi bài viết có từ 1 đến 3 Topic thuộc danh mục Topic. |

**Lý do**

Topic là phân loại có cấu trúc, bắt buộc cho mỗi bài viết, dùng để lọc và duyệt nội dung.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-002.1 | Khi tác giả tạo bài viết, hệ thống phải cho phép tác giả chọn Topic cho bài viết đó từ danh mục Topic. |
| ISH-M05-002.2 | Khi người dùng chọn Topic cho một bài viết, hệ thống phải chỉ chấp nhận Topic có trong danh mục Topic. |
| ISH-M05-002.3 | Hệ thống phải cho phép tác giả chọn Topic cho bài viết mà không cần yêu cầu gợi ý Topic. |
| ISH-M05-002.4 | Hệ thống phải yêu cầu mỗi bài viết có tối thiểu 1 Topic. |
| ISH-M05-002.5 | Khi tác giả gửi một bài viết không có Topic nào, hệ thống phải từ chối việc gửi bài viết đó. |
| ISH-M05-002.6 | Khi người dùng lưu một thay đổi làm bài viết không còn Topic nào, hệ thống phải từ chối thay đổi đó. |
| ISH-M05-002.7 | Hệ thống phải giới hạn mỗi bài viết tối đa 3 Topic. |
| ISH-M05-002.8 | Khi người dùng chọn Topic thứ 4 cho một bài viết, hệ thống phải từ chối lựa chọn đó. |
| ISH-M05-002.9 | Khi tác giả sửa một bài viết đã gửi, hệ thống phải cho phép tác giả thay đổi Topic của bài viết đó. |

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
| ISH-M05-003.11 | Khi tác giả thay đổi tệp đính kèm của bài viết sau khi nhận gợi ý Topic, hệ thống phải giữ gợi ý đó là gợi ý còn mới. |
| ISH-M05-003.12 | Trong khi gợi ý Topic của bài viết là gợi ý cũ, hệ thống phải hiển thị cảnh báo gợi ý cũ cho tác giả. |
| ISH-M05-003.13 | Trong khi gợi ý Topic của bài viết là gợi ý cũ, hệ thống phải cho phép tác giả yêu cầu gợi ý Topic lại. |
| ISH-M05-003.14 | Trong khi gợi ý Topic của bài viết là gợi ý cũ, hệ thống phải cho phép tác giả gửi bài viết. |

### 5.6 Gợi ý Topic khi AI không khả dụng

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-004 | Trong khi không gợi ý được Topic bằng AI, hệ thống phải cho phép tác giả tự chọn Topic để gửi bài viết. |

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
| ISH-M05-005 | Hệ thống phải ghi nhận phản hồi gợi ý Topic khi tác giả gửi bài viết. |

**Lý do**

Lựa chọn cuối cùng của người dùng sau gợi ý là phản hồi cho AI, dùng làm cơ chế đánh giá lại chất lượng gợi ý.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-005.1 | Khi tác giả gửi một bài viết có gợi ý Topic còn mới, hệ thống phải ghi nhận phản hồi gợi ý Topic từ gợi ý Topic gần nhất cùng các Topic tác giả chọn cuối cùng. |
| ISH-M05-005.2 | Trong khi gợi ý Topic của bài viết là gợi ý cũ, khi tác giả gửi bài viết đó, hệ thống phải không ghi nhận phản hồi gợi ý Topic. |
| ISH-M05-005.3 | Khi tác giả gửi một bài viết chưa từng nhận gợi ý Topic, hệ thống phải không ghi nhận phản hồi gợi ý Topic. |

### 5.8 Gắn Tag cho bài viết

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-006 | Hệ thống phải cho phép tác giả gắn từ 0 đến 5 Tag tự do cho mỗi bài viết. |

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

### 5.9 Theo dõi Topic

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-007 | Hệ thống phải cho phép người dùng đã đăng nhập theo dõi một Topic. |

**Lý do**

Người dùng theo dõi để nhận cập nhật về nội dung hoặc chủ đề mình quan tâm.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-007.1 | Khi người dùng đã đăng nhập yêu cầu theo dõi một Topic chưa theo dõi, hệ thống phải ghi nhận người dùng đó đang theo dõi Topic đó. |
| ISH-M05-007.2 | Khi người dùng đã đăng nhập yêu cầu bỏ theo dõi một Topic đang theo dõi, hệ thống phải ghi nhận người dùng đó không còn theo dõi Topic đó. |
| ISH-M05-007.3 | Hệ thống phải hiển thị cho người dùng đã đăng nhập trạng thái đang theo dõi hay chưa theo dõi của người dùng đó với mỗi Topic. |
| ISH-M05-007.4 | Hệ thống phải hiển thị số người đang theo dõi của mỗi Topic. |
| ISH-M05-007.5 | Khi Guest yêu cầu theo dõi một Topic, hệ thống phải từ chối yêu cầu đó. |
| ISH-M05-007.6 | Khi người dùng đã đăng nhập yêu cầu theo dõi một Topic đang theo dõi, hệ thống phải giữ số người theo dõi của Topic đó không đổi. |

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
| ISH-M05-008.1 | Hệ thống phải tính điểm Trending của một Topic bằng tổng, trên mọi bài viết được tính của Topic đó, của 2 lần số upvote phát sinh trong 7 ngày gần nhất cộng số bình luận phát sinh trong 7 ngày gần nhất, cộng thêm số bài viết được tính của Topic đó được đăng trong 7 ngày gần nhất. |
| ISH-M05-008.2 | Hệ thống phải tính điểm Trending của một Tag bằng tổng, trên mọi bài viết được tính của Tag đó, của 2 lần số upvote phát sinh trong 7 ngày gần nhất cộng số bình luận phát sinh trong 7 ngày gần nhất, cộng thêm số bài viết được tính của Tag đó được đăng trong 7 ngày gần nhất. |
| ISH-M05-008.3 | Hệ thống phải chỉ tính vào điểm Trending các bài viết công khai không thuộc Group Private. |
| ISH-M05-008.4 | Hệ thống phải chỉ đếm upvote vào chính bài viết, không đếm upvote vào bình luận của bài viết, khi tính điểm Trending. |
| ISH-M05-008.5 | Hệ thống phải đếm mọi bình luận gốc cùng mọi trả lời của bài viết khi tính số bình luận cho điểm Trending. |
| ISH-M05-008.6 | Hệ thống phải không đếm upvote đã bị rút khi tính điểm Trending. |
| ISH-M05-008.7 | Hệ thống phải không đếm bình luận đã bị xóa khi tính điểm Trending. |
| ISH-M05-008.8 | Hệ thống phải xác định 7 ngày gần nhất là 168 giờ tính lùi từ thời điểm tính điểm Trending. |
| ISH-M05-008.9 | Hệ thống phải xếp Topic có điểm Trending cao hơn trước Topic có điểm Trending thấp hơn. |
| ISH-M05-008.10 | Hệ thống phải xếp Tag có điểm Trending cao hơn trước Tag có điểm Trending thấp hơn. |
| ISH-M05-008.11 | Khi hai Topic có cùng điểm Trending, hệ thống phải xếp trước Topic có số bài viết được tính đăng trong 7 ngày gần nhất lớn hơn, rồi đến tên theo thứ tự chữ cái từ A đến Z. |
| ISH-M05-008.12 | Khi hai Tag có cùng điểm Trending, hệ thống phải xếp trước Tag có số bài viết được tính đăng trong 7 ngày gần nhất lớn hơn, rồi đến tên theo thứ tự chữ cái từ A đến Z. |

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

Topic dùng để tổ chức các lĩnh vực tri thức lớn, phù hợp đối tượng học sinh THPT.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-010.1 | Khi Mod hoặc Admin đổi tên một Topic, hệ thống phải giữ nguyên các bài viết đang gắn Topic đó. |
| ISH-M05-010.2 | Khi Mod hoặc Admin đổi tên một Topic, hệ thống phải giữ nguyên những người đang theo dõi Topic đó. |
| ISH-M05-010.3 | Khi Guest hoặc User yêu cầu đổi tên một Topic, hệ thống phải từ chối yêu cầu đó. |
| ISH-M05-010.4 | Khi người dùng yêu cầu xóa một Topic, hệ thống phải từ chối yêu cầu đó. |

### 5.13 Gộp Topic

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-011 | Khi Mod hoặc Admin gộp một Topic nguồn vào một Topic đích, hệ thống phải chuyển mọi bài viết đang gắn Topic nguồn sang Topic đích. |

**Lý do**

Topic dùng để tổ chức các lĩnh vực tri thức lớn, phù hợp đối tượng học sinh THPT.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-011.1 | Khi Mod hoặc Admin gộp Topic nguồn vào Topic đích, hệ thống phải giữ Topic đích đúng một lần trên mỗi bài viết đã gắn cả Topic nguồn lẫn Topic đích. |
| ISH-M05-011.2 | Khi Mod hoặc Admin gộp Topic nguồn vào Topic đích, hệ thống phải loại Topic nguồn khỏi danh mục Topic. |
| ISH-M05-011.3 | Khi Mod hoặc Admin gộp Topic nguồn vào Topic đích, hệ thống phải chuyển mọi người đang theo dõi Topic nguồn sang theo dõi Topic đích. |
| ISH-M05-011.4 | Khi Mod hoặc Admin gộp Topic nguồn vào Topic đích, hệ thống phải tính mỗi người đang theo dõi cả Topic nguồn lẫn Topic đích đúng một lần trong số người theo dõi Topic đích. |
| ISH-M05-011.5 | Khi Guest hoặc User yêu cầu gộp Topic, hệ thống phải từ chối yêu cầu đó. |

### 5.14 Vô hiệu hóa và mở lại Tag

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-012 | Hệ thống phải cho phép Mod và Admin thay đổi trạng thái hoạt động của một Tag. |

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

## Phụ lục A. Truy vết nguồn

| ID | Nguồn | Cơ sở | Ghi chú |
|---|---|---|---|
| ISH-M05-001 | DEC-047, DEC-048, DEC-140, ISS-079, ISS-080, ISS-207, QA-101, QA-102, QA-267 | Nói thẳng | |
| ISH-M05-001.1 | DEC-048, ISS-080, QA-102, DRAFT §3.1 | Nói thẳng | DRAFT §3.1 nói danh sách chưa cố định, chốt ở BA; DEC-048 là danh sách chốt |
| ISH-M05-001.2 | DEC-140, DEC-047, QA-267 | Nói thẳng | Phẳng, không Category riêng; ghi đè 2 tầng của QA-033 |
| ISH-M05-001.3 | QA-011 | Nói thẳng | Guest "Xem danh sách Topic / Tag / Khối lớp" |
| ISH-M05-001.4 | DEC-048, QA-267 | Nói thẳng | "Topic list (11, final)"; "11 giá trị cố định" |
| ISH-M05-002 | DEC-049, ISS-083, DEC-143, ISS-211, QA-271, DRAFT §3.4 | Nói thẳng | Register ghi đè sơ đồ một Topic ở DRAFT §3.4 (DEC-143) |
| ISH-M05-002.1 | DEC-050, DEC-047 | Nói thẳng | "user picks from dropdown"; Topic do người dùng xác nhận |
| ISH-M05-002.2 | DEC-047, QA-267 | Nói thẳng | Danh mục cố định; Topic chọn từ danh mục |
| ISH-M05-002.3 | DEC-050 | Nói thẳng | "User manually picks topic from start → skips AI flow entirely" |
| ISH-M05-002.4 | DEC-049, ISS-083 | Nói thẳng | "Min 1 … (mandatory)" |
| ISH-M05-002.5 | DEC-049 | Suy ra | Giới hạn tối thiểu 1 ⇒ từ chối gửi bài khi có 0 Topic (RULES §4.5) |
| ISH-M05-002.6 | DEC-049, DEC-144 | Suy ra | Giới hạn tối thiểu 1 áp dụng cho mọi lần đổi (DEC-144) ⇒ từ chối thay đổi làm còn 0 Topic (RULES §4.5) |
| ISH-M05-002.7 | DEC-049, ISS-083, QA-103 | Nói thẳng | "max 3 topics/post" |
| ISH-M05-002.8 | DEC-049 | Suy ra | Giới hạn tối đa 3 ⇒ từ chối Topic thứ 4 (RULES §4.5) |
| ISH-M05-002.9 | DEC-144, ISS-213, QA-273 | Nói thẳng | |
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
| ISH-M05-003.11 | DEC-148, QA-280 | Nói thẳng | "attachment changes do not count" |
| ISH-M05-003.12 | DEC-050, QA-104 | Nói thẳng | "soft warning" |
| ISH-M05-003.13 | DEC-050 | Nói thẳng | "re-suggest button" |
| ISH-M05-003.14 | DEC-050 | Nói thẳng | "does not block publish" |
| ISH-M05-004 | DEC-008, DEC-099 | Nói thẳng | |
| ISH-M05-004.1 | DEC-008, DEC-093, DEC-050, ISS-122, QA-165 | Nói thẳng | "AI off → user picks from dropdown, no suggest"; công tắc tổng và công tắc gợi ý Topic (DEC-093) |
| ISH-M05-004.2 | DEC-099 | Nói thẳng | "Topic suggest→show non-blocking error" |
| ISH-M05-004.3 | DEC-099 | Nói thẳng | "no action taken" |
| ISH-M05-004.4 | DEC-099, DEC-132 | Nói thẳng | Lỗi "non-blocking"; "the user selects manually" |
| ISH-M05-004.5 | DEC-132, DEC-149, ISS-194, ISS-221, QA-253, QA-281 | Nói thẳng | Kiểm theo danh mục; bỏ phần không hợp lệ (DEC-149) |
| ISH-M05-004.6 | DEC-132, DEC-149 | Nói thẳng | Không còn Topic hợp lệ ⇒ coi như gợi ý thất bại |
| ISH-M05-004.7 | DEC-152, ISS-225, QA-285 | Nói thẳng | |
| ISH-M05-005 | DEC-050, QA-104, QA-017 | Nói thẳng | |
| ISH-M05-005.1 | DEC-050, QA-017 | Nói thẳng | "Feedback (AI suggest vs final selection)"; gợi ý gần nhất vì gợi ý trước đó đã bị thay thế (DEC-148) |
| ISH-M05-005.2 | DEC-050, QA-104 | Nói thẳng | "only recorded when not stale" |
| ISH-M05-005.3 | DEC-050 | Suy ra | "manually picks topic from start → skips AI flow entirely" ⇒ không có gợi ý nên không có phản hồi để ghi |
| ISH-M05-006 | DEC-051, DEC-143, ISS-082, ISS-212, QA-105, QA-272, DRAFT §3.2 | Nói thẳng | Register ghi đè "không giới hạn" của DRAFT §3.2 (DEC-143) |
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
| ISH-M05-006.12 | DEC-144, QA-273 | Nói thẳng | Chỉ tác giả đổi Tag; Mod/Admin không đổi Tag của bài |
| ISH-M05-006.13 | DEC-152, ISS-226, QA-286 | Nói thẳng | |
| ISH-M05-006.14 | DEC-152, QA-286 | Nói thẳng | |
| ISH-M05-006.15 | DEC-152, QA-286 | Nói thẳng | |
| ISH-M05-007 | DEC-141, ISS-208, QA-268, QA-043, ISS-051, DRAFT §4.5 | Nói thẳng | |
| ISH-M05-007.1 | DEC-141, QA-043 | Nói thẳng | "Follow/Unfollow behaviour for Topic" |
| ISH-M05-007.2 | DEC-141, QA-268 | Nói thẳng | "nút Follow/Unfollow" |
| ISH-M05-007.3 | DEC-141, QA-268 | Nói thẳng | "follow state" |
| ISH-M05-007.4 | DEC-141, QA-268 | Nói thẳng | "follower count" |
| ISH-M05-007.5 | DEC-126, QA-227, QA-011 | Nói thẳng | "All interactions (… follow …) require login" |
| ISH-M05-007.6 | DEC-141 | Suy ra | Theo dõi là một trạng thái có hoặc không ⇒ theo dõi lần nữa không tăng số người theo dõi |
| ISH-M05-008 | DEC-052, DEC-142, QA-106, ISS-082, ISS-210, QA-270 | Nói thẳng | |
| ISH-M05-008.1 | DEC-142, QA-270, DEC-052 | Nói thẳng | Score = Σ(2 × upvotes in window + comments in window) + số bài đăng trong cửa sổ |
| ISH-M05-008.2 | DEC-142, QA-270, DEC-052 | Nói thẳng | Cùng công thức cho Tag |
| ISH-M05-008.3 | DEC-146, ISS-216, QA-276, DEC-033 | Nói thẳng | |
| ISH-M05-008.4 | DEC-146, ISS-217, QA-277 | Nói thẳng | |
| ISH-M05-008.5 | DEC-146, QA-277 | Nói thẳng | |
| ISH-M05-008.6 | DEC-146, QA-277 | Nói thẳng | "only interactions that still exist count" |
| ISH-M05-008.7 | DEC-146, QA-277 | Nói thẳng | "only interactions that still exist count" |
| ISH-M05-008.8 | DEC-052 | Nói thẳng | "Rolling 7-day window (sliding from now…)" |
| ISH-M05-008.9 | DEC-153, ISS-227, QA-287 | Nói thẳng | |
| ISH-M05-008.10 | DEC-153, QA-287 | Nói thẳng | |
| ISH-M05-008.11 | DEC-153, QA-287 | Nói thẳng | |
| ISH-M05-008.12 | DEC-153, QA-287 | Nói thẳng | |
| ISH-M05-009 | DEC-144, ISS-213, QA-273, DRAFT §11.2 | Nói thẳng | |
| ISH-M05-009.1 | DEC-144, QA-273 | Nói thẳng | |
| ISH-M05-009.2 | DEC-144 | Suy ra | Chỉ tác giả, Mod, Admin được đổi Topic ⇒ từ chối người khác (RULES §4.5) |
| ISH-M05-010 | DEC-049, ISS-084, QA-107, DEC-090, ISS-119, QA-160 | Nói thẳng | "Mod/admin: edit (rename)" |
| ISH-M05-010.1 | DEC-049 | Suy ra | Đổi tên giữ nguyên Topic, chỉ đổi tên ⇒ các bài viết vẫn gắn Topic đó |
| ISH-M05-010.2 | DEC-049, DEC-141 | Suy ra | Đổi tên giữ nguyên Topic ⇒ quan hệ theo dõi vẫn giữ |
| ISH-M05-010.3 | DEC-049, DEC-090 | Suy ra | Chỉ Mod/Admin được đổi tên ⇒ từ chối người khác (RULES §4.5) |
| ISH-M05-010.4 | DEC-049, ISS-084, QA-107 | Nói thẳng | "No delete" |
| ISH-M05-011 | DEC-049, DEC-090 | Nói thẳng | "Merge auto re-points post_topics from source to target" |
| ISH-M05-011.1 | DEC-049 | Suy ra | Chuyển liên kết từ nguồn sang đích ⇒ bài có cả hai chỉ còn Topic đích một lần |
| ISH-M05-011.2 | DEC-145, ISS-214, QA-274 | Nói thẳng | |
| ISH-M05-011.3 | DEC-145, ISS-215, QA-275 | Nói thẳng | |
| ISH-M05-011.4 | DEC-145, QA-275 | Nói thẳng | "a user who followed both counts once" |
| ISH-M05-011.5 | DEC-049, DEC-090 | Suy ra | Chỉ Mod/Admin được gộp ⇒ từ chối người khác (RULES §4.5) |
| ISH-M05-012 | DEC-051, DEC-150, QA-107, DEC-090, ISS-084 | Nói thẳng | |
| ISH-M05-012.1 | DEC-051 | Nói thẳng | "tag chip hidden from display" |
| ISH-M05-012.2 | DEC-051 | Nói thẳng | "old posts keep post_tags record" |
| ISH-M05-012.3 | DEC-051 | Nói thẳng | "hidden from … trending" |
| ISH-M05-012.4 | DEC-051, QA-107 | Nói thẳng | "if user retypes a disabled tag name, it's NOT tagified" |
| ISH-M05-012.5 | DEC-150, ISS-222, QA-282 | Nói thẳng | |
| ISH-M05-012.6 | DEC-150, QA-282 | Nói thẳng | "can be used normally" |
| ISH-M05-012.7 | DEC-051, DEC-090 | Suy ra | Chỉ Mod/Admin vô hiệu hóa ⇒ từ chối người khác (RULES §4.5) |
| ISH-M05-012.8 | DEC-150 | Suy ra | Chỉ Mod/Admin mở lại ⇒ từ chối người khác (RULES §4.5) |
| ISH-M05-012.9 | DEC-051, ISS-084, QA-107 | Nói thẳng | "mod/admin do NOT edit"; Tag không có thao tác sửa cho người dùng nào |
| ISH-M05-012.10 | DEC-051 | Nói thẳng | "do NOT … merge" |
| ISH-M05-012.11 | DEC-051, QA-107 | Nói thẳng | "do NOT … delete"; chỉ vô hiệu hóa khi khẩn cấp |

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
| OP-M05-10 | Bài viết bị từ chối rồi được tác giả gửi lại thì có ghi thêm phản hồi gợi ý Topic không (ISH-M05-005). Đề xuất mặc định: chỉ ghi ở lần gửi đầu tiên. | Đề xuất | Mở |
