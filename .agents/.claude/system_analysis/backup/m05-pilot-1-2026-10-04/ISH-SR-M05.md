# Tài liệu yêu cầu hệ thống — M05 Topic & Tag
<!-- [Vietnamese Doc] -->

| Mã tài liệu | ISH-SR-M05 |
|---|---|
| Dự án | iShare |
| Module | M05 — Topic & Tag |
| Trạng thái | Bản nháp |
| Phiên bản | 0.3 |
| Ngày | 2026-10-04 |
| Tác giả | Phạm Văn Đức |

## 1. Tổng quan

Tài liệu này quy định yêu cầu hệ thống của module Topic & Tag (M05) trong hệ thống iShare — nền tảng chia sẻ kiến thức có hỗ trợ AI cho học sinh trung học phổ thông.

### 1.1 Mục đích

Module Topic & Tag giúp người dùng phân loại bài viết theo lĩnh vực tri thức và theo từ khóa tự do, làm cơ sở cho việc duyệt nội dung, tìm kiếm và phát hiện nội dung thịnh hành trên hệ thống.

## 2. Thuật ngữ và viết tắt

### 2.1 Thuật ngữ

| Thuật ngữ | Mô tả |
|---|---|
| Topic | Lĩnh vực tri thức dùng để phân loại bài viết, chọn từ danh sách 11 giá trị cố định, cấu trúc một tầng duy nhất (không có Category riêng phía trên). |
| Tag | Từ khóa tự do do người dùng đặt cho bài viết, không theo danh sách cố định, không chứa khoảng trắng. |
| Trending | Mức độ thịnh hành của một Topic hoặc một Tag, tính theo hoạt động của các bài viết trong cửa sổ 7 ngày gần nhất. |
| Đã lỗi thời | Trạng thái của các Topic do AI gợi ý trên một bài viết, phát sinh khi nội dung bài viết đó bị thay đổi sau thời điểm gợi ý. |
| Mod | Vai trò kiểm duyệt; đối với Topic và Tag, có quyền sửa tên và gộp Topic, ẩn Tag trong tình huống khẩn cấp. |
| Admin | Vai trò quản trị cao nhất; có đầy đủ quyền của Mod đối với Topic và Tag. |
| Upvote | Lượt đánh giá tích cực của người dùng khác dành cho một bài viết, dùng trong công thức tính điểm Trending. |
| Theo dõi | Hành động của người dùng để nhận cập nhật về một Topic mà họ quan tâm. |

### 2.2 Viết tắt

| Viết tắt | Đầy đủ |
|---|---|
| SR | System Requirement |
| AI | Artificial Intelligence — Trí tuệ nhân tạo |

## 3. Thông tin đầu vào

### 3.1 Tài liệu đầu vào

| Mã | Tên | Phiên bản |
|---|---|---|
| DRAFT | iShare_modules.md §3 (Topic / Tag / Lớp-Khối Module), §4.5 (Follow / Quan tâm), §11.2 (AI Content Classification) | 2026-10-04 |
| DRAFT | iShare_dev_priority.md §3 (Giai đoạn 1, Giai đoạn 2) | 2026-10-04 |
| REG | decisions.md (DEC-047…052, DEC-090, DEC-093, DEC-099, DEC-008, DEC-140, DEC-141) | 2026-10-04 |
| REG | issue-queue.md (ISS-079…084, ISS-207…209) | 2026-10-04 |
| REG | qa-log.md (QA-101…108, QA-043, QA-267…269) | 2026-10-04 |
| REG | module-registry.md (dòng M05) | 2026-10-04 |

### 3.2 Tài liệu liên quan

| Mã | Tên | Phiên bản |
|---|---|---|
| — | Không có | — |

## 4. Tổng quan chức năng

Module Topic & Tag quy định cách hệ thống tổ chức và phân loại nội dung bài viết: Topic là lĩnh vực tri thức được chọn từ danh sách cố định, Tag là từ khóa tự do do người dùng đặt. Module này bao gồm việc gán Topic và Tag cho bài viết, gợi ý Topic bằng AI, các hành động quản trị của Mod và Admin đối với Topic và Tag, và việc tính điểm thịnh hành (Trending) cho Topic và Tag dựa trên hoạt động của bài viết.

### 4.1 Luật và tiêu chuẩn liên quan

Không có.

## 5. Yêu cầu chức năng

### 5.1 Tổng quan yêu cầu

| Tính năng | Yêu cầu cấp trên | Mức ưu tiên | Mốc | Ngoại lệ |
|---|---|---|---|---|
| Gán Topic cho bài viết | ISH-M05-001 | Must | P0 | — |
| AI gợi ý Topic | ISH-M05-002 | Must | AI-P0 | — |
| Quản trị Topic | ISH-M05-003 | Must | P0 | — |
| Gán Tag cho bài viết | ISH-M05-004 | Must | P0 | — |
| Quản trị Tag khẩn cấp | ISH-M05-005 | Must | P0 | — |
| Trending Topic & Tag | ISH-M05-006 | Must | P1 | — |
| Theo dõi Topic | ISH-M05-007 | Must | P1 | — |

### 5.2 Chuyển trạng thái

| Trạng thái hiện tại | Sự kiện hoặc điều kiện | Trạng thái mới | ID yêu cầu |
|---|---|---|---|
| Đang hoạt động | Khi Mod hoặc Admin ẩn Tag trong tình huống khẩn cấp | Đã ẩn | ISH-M05-005 |

### 5.3 Gán Topic cho bài viết

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-001 | Hệ thống phải cho phép người dùng gán Topic cho bài viết. |

**Lý do**

Topic dùng để tổ chức các lĩnh vực tri thức lớn, phù hợp đối tượng học sinh trung học phổ thông.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-001.1 | Hệ thống phải giới hạn mỗi bài viết có tối thiểu 1 Topic. |
| ISH-M05-001.2 | Hệ thống phải giới hạn mỗi bài viết có tối đa 3 Topic. |
| ISH-M05-001.3 | Khi người dùng xuất bản bài viết chưa gán Topic nào, hệ thống phải từ chối xuất bản bài viết đó. |
| ISH-M05-001.4 | Khi người dùng chọn Topic thứ 4 cho một bài viết, hệ thống phải từ chối lựa chọn đó. |
| ISH-M05-001.5 | Hệ thống phải giới hạn Topic trong danh sách 11 giá trị cố định: Toán học, Ngữ văn, Ngoại ngữ, Khoa học tự nhiên (Lý/Hóa/Sinh), Khoa học xã hội (Sử/Địa/KT&PL), Tin học, Kỹ năng mềm, Hướng nghiệp, Nghệ thuật & Sáng tạo, Góc Chill, Khác. |
| ISH-M05-001.6 | Khi người dùng chọn một giá trị Topic ngoài danh sách cố định, hệ thống phải từ chối lựa chọn đó. |

### 5.4 AI gợi ý Topic

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-002 | Khi người dùng bấm nút gợi ý Topic, hệ thống phải phân tích tiêu đề và nội dung văn bản của bài viết để gợi ý tối đa 3 Topic đã được đánh dấu sẵn trên bài viết. |

**Lý do**

Nguồn chưa nêu lý do.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-002.1 | Khi nội dung bài viết có ít hơn 20 từ, hệ thống phải từ chối gợi ý Topic. |
| ISH-M05-002.2 | Khi nội dung bài viết có ít hơn 20 từ, hệ thống phải báo cho người dùng biết nội dung chưa đủ để gợi ý Topic. |
| ISH-M05-002.3 | Hệ thống phải cho phép người dùng điều chỉnh tự do các Topic được gợi ý trước khi xuất bản bài viết. |
| ISH-M05-002.4 | Khi người dùng thay đổi nội dung bài viết sau khi được gợi ý Topic, hệ thống phải đánh dấu các Topic gợi ý trên bài viết đó là đã lỗi thời. |
| ISH-M05-002.5 | Khi Topic gợi ý trên bài viết đã lỗi thời, hệ thống phải hiển thị cảnh báo không chặn việc xuất bản bài viết. |
| ISH-M05-002.6 | Khi Topic gợi ý trên bài viết đã lỗi thời, hệ thống phải cho phép người dùng gợi ý lại Topic. |
| ISH-M05-002.7 | Trong khi tính năng gợi ý Topic bằng AI không khả dụng, hệ thống phải cho phép người dùng tự chọn Topic theo cách thủ công. |
| ISH-M05-002.8 | Nếu dịch vụ gợi ý Topic bằng AI không phản hồi sau khi thử lại, thì hệ thống phải hiển thị thông báo lỗi không chặn việc xuất bản bài viết. |
| ISH-M05-002.9 | Nếu kết quả gợi ý Topic bằng AI nằm ngoài danh sách 11 Topic hợp lệ, thì hệ thống phải hiển thị thông báo lỗi không chặn việc xuất bản bài viết. |

### 5.5 Quản trị Topic

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-003 | Hệ thống phải cho phép Mod hoặc Admin sửa tên hoặc gộp Topic. |

**Lý do**

Nguồn chưa nêu lý do.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-003.1 | Khi Mod hoặc Admin gộp hai Topic, hệ thống phải chuyển toàn bộ bài viết đang gắn Topic nguồn sang Topic đích. |
| ISH-M05-003.2 | Khi Mod hoặc Admin yêu cầu xóa Topic, hệ thống phải từ chối yêu cầu đó. |

### 5.6 Gán Tag cho bài viết

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-004 | Hệ thống phải cho phép người dùng gán Tag cho bài viết. |

**Lý do**

Nguồn chưa nêu lý do.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-004.1 | Hệ thống phải giới hạn mỗi bài viết có tối đa 5 Tag. |
| ISH-M05-004.2 | Khi người dùng chọn Tag thứ 6 cho một bài viết, hệ thống phải từ chối lựa chọn đó. |
| ISH-M05-004.3 | Hệ thống phải giới hạn mỗi Tag tối đa 30 ký tự. |
| ISH-M05-004.4 | Khi người dùng nhập Tag dài hơn 30 ký tự, hệ thống phải từ chối Tag đó. |
| ISH-M05-004.5 | Khi người dùng nhập một Tag chưa tồn tại, hệ thống phải tạo Tag đó mà không cần phê duyệt. |
| ISH-M05-004.6 | Khi người dùng nhập Tag chứa dấu cách, hệ thống phải từ chối Tag đó. |
| ISH-M05-004.7 | Khi người dùng nhập Tag trùng nội dung nhưng khác chữ hoa hoặc chữ thường với một Tag đã tồn tại, hệ thống phải coi đó là Tag đã tồn tại, không tạo Tag mới. |

### 5.7 Quản trị Tag khẩn cấp

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-005 | Hệ thống phải cho phép Mod hoặc Admin ẩn một Tag trong tình huống khẩn cấp. |

**Lý do**

Nguồn chưa nêu lý do.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-005.1 | Khi Mod hoặc Admin ẩn một Tag, hệ thống phải loại Tag đó khỏi gợi ý tự động, khỏi Trending, khỏi duyệt Tag. |
| ISH-M05-005.2 | Khi một Tag đã bị ẩn, hệ thống phải giữ nguyên liên kết của Tag đó với các bài viết đã gắn trước đó. |
| ISH-M05-005.3 | Khi một Tag đã bị ẩn, hệ thống phải loại bỏ Tag đó khỏi phần hiển thị của các bài viết đã gắn trước đó. |
| ISH-M05-005.4 | Khi người dùng nhập lại tên của một Tag đã bị ẩn, hệ thống phải hiển thị nội dung đó dưới dạng văn bản thường, không tạo thành Tag. |
| ISH-M05-005.5 | Hệ thống phải không cho phép Mod hoặc Admin sửa, gộp hoặc xóa Tag ngoài tình huống khẩn cấp. |

### 5.8 Trending Topic & Tag

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-006 | Hệ thống phải tính điểm Trending cho từng Topic và từng Tag dựa trên hoạt động của bài viết trong 7 ngày gần nhất. |

**Lý do**

Nguồn chưa nêu lý do.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-006.1 | Hệ thống phải tính điểm Trending của một Topic hoặc một Tag bằng tổng, trên mọi bài viết thuộc Topic hoặc Tag đó, của giá trị 1 cộng 2 lần số lượt upvote cộng số lượt bình luận của bài viết. |
| ISH-M05-006.2 | Hệ thống phải tính cửa sổ 7 ngày của Trending theo kiểu trượt tính từ thời điểm hiện tại, không theo tuần lịch cố định. |

### 5.9 Theo dõi Topic

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-007 | Hệ thống phải cho phép người dùng theo dõi một Topic. |

**Lý do**

Người dùng muốn nhận cập nhật về nội dung hoặc chủ đề mà họ quan tâm.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-007.1 | Hệ thống phải cho phép người dùng bỏ theo dõi một Topic đang theo dõi. |
| ISH-M05-007.2 | Hệ thống phải hiển thị số lượng người đang theo dõi của một Topic. |

### 5.10 Yêu cầu HMI

Sẽ bổ sung sau khi có thiết kế.

### 5.11 Chuyển màn hình

Sẽ bổ sung sau khi có thiết kế.

## 6. Lịch sử sửa đổi

| Phiên bản | Ngày | Mô tả | Người sửa |
|---|---|---|---|
| 0.1 | 2026-10-04 | Bản nháp đầu tiên | Phạm Văn Đức |
| 0.2 | 2026-10-04 | Sửa theo ISH-AUD-M05-r1: bổ sung nguồn DEC-140/ISS-207/QA-267 vào Phụ lục A (AUD-M05-01); thêm ISH-M05-002.9 xử lý AI trả Topic ngoài danh sách hợp lệ (AUD-M05-02); thêm tính năng Theo dõi Topic ISH-M05-007 (AUD-M05-03, xác nhận DEC-141/QA-268); ghi nhận ở routing R7 việc không làm AI gợi ý Tag (AUD-M05-04, xác nhận QA-269) | Phạm Văn Đức |
| 0.3 | 2026-10-04 | Sửa theo ISH-AUD-M05-r2 (hồi quy từ bản 0.2): thêm mục 2.1 định nghĩa "Theo dõi" (AUD-M05-06); thêm dòng routing R5 cho phần DEC-141 thuộc M07 (AUD-M05-05) | Phạm Văn Đức |

## Phụ lục A. Truy vết nguồn

| ID | Nguồn | Cơ sở | Ghi chú |
|---|---|---|---|
| ISH-M05-001 | DEC-047, ISS-079, QA-101 | Nói thẳng | |
| ISH-M05-001.1 | DEC-049, ISS-083 | Nói thẳng | |
| ISH-M05-001.2 | DEC-049, ISS-083 | Nói thẳng | |
| ISH-M05-001.3 | DEC-049 | Suy ra | "Min 1 (mandatory)" ⇒ từ chối xuất bản khi chưa chọn Topic nào (RULES §4.5) |
| ISH-M05-001.4 | DEC-049 | Suy ra | "Max 3" ⇒ từ chối lựa chọn vượt giới hạn (RULES §4.5) |
| ISH-M05-001.5 | DEC-048, ISS-080, QA-102, DEC-140, ISS-207, QA-267 | Nói thẳng | DEC-140/ISS-207/QA-267 là hồ sơ xác nhận cấu trúc Topic 1 tầng (flat), ghi đè QA-033/ISS-046 — xem routing R6 |
| ISH-M05-001.6 | DEC-048 | Suy ra | Danh sách cố định ⇒ từ chối giá trị ngoài danh sách (RULES §4.5) |
| ISH-M05-002 | DEC-050, ISS-081, QA-103 | Nói thẳng | |
| ISH-M05-002.1 | DEC-050 | Nói thẳng | |
| ISH-M05-002.2 | DEC-050 | Nói thẳng | |
| ISH-M05-002.3 | DEC-050 | Nói thẳng | |
| ISH-M05-002.4 | DEC-050, QA-104 | Nói thẳng | |
| ISH-M05-002.5 | DEC-050, QA-104 | Nói thẳng | |
| ISH-M05-002.6 | DEC-050, QA-104 | Nói thẳng | |
| ISH-M05-002.7 | DEC-050, DEC-008, DEC-093 | Nói thẳng | |
| ISH-M05-002.8 | DEC-099 | Nói thẳng | |
| ISH-M05-002.9 | DEC-132, ISS-194, QA-253 | Nói thẳng | |
| ISH-M05-003 | DEC-049, DEC-090, ISS-084, QA-107 | Nói thẳng | |
| ISH-M05-003.1 | DEC-049 | Nói thẳng | |
| ISH-M05-003.2 | DEC-049, ISS-084, QA-107 | Suy ra | "No delete" ⇒ yêu cầu xóa Topic bị từ chối (RULES §4.5) |
| ISH-M05-004 | DEC-047, DEC-051, ISS-079, ISS-082, QA-101 | Nói thẳng | |
| ISH-M05-004.1 | DEC-051, QA-105, DRAFT §3.2 | Nói thẳng | DRAFT §3.2 nói Tag "không giới hạn số lượng"; DEC-051/QA-105 (Phase 5) chốt tối đa 5 — viết theo register theo RULES §7.5, đã báo stakeholder ở mục bàn giao |
| ISH-M05-004.2 | DEC-051 | Suy ra | "Max 5 tags/post" ⇒ từ chối Tag vượt giới hạn (RULES §4.5) |
| ISH-M05-004.3 | DEC-051, QA-105 | Nói thẳng | |
| ISH-M05-004.4 | DEC-051 | Suy ra | "Max 30 chars/tag" ⇒ từ chối Tag vượt giới hạn (RULES §4.5) |
| ISH-M05-004.5 | DEC-051 | Nói thẳng | |
| ISH-M05-004.6 | DEC-047 | Suy ra | "No spaces" ⇒ từ chối Tag chứa khoảng trắng (RULES §4.5) |
| ISH-M05-004.7 | DEC-051 | Suy ra | Cột dữ liệu "name unique lowercase-normalized" ⇒ hai Tag chỉ khác hoa/thường được coi là một Tag |
| ISH-M05-005 | DEC-051, DEC-090, ISS-084, QA-107 | Nói thẳng | |
| ISH-M05-005.1 | DEC-051 | Nói thẳng | |
| ISH-M05-005.2 | DEC-051 | Nói thẳng | |
| ISH-M05-005.3 | DEC-051 | Nói thẳng | |
| ISH-M05-005.4 | DEC-051 | Nói thẳng | |
| ISH-M05-005.5 | DEC-051, QA-107 | Nói thẳng | |
| ISH-M05-006 | DEC-052, ISS-082 | Nói thẳng | |
| ISH-M05-006.1 | DEC-052, QA-106 | Nói thẳng | |
| ISH-M05-006.2 | DEC-052 | Nói thẳng | |
| ISH-M05-007 | QA-043, DEC-141, ISS-208, QA-268, DRAFT §4.5 | Nói thẳng | |
| ISH-M05-007.1 | QA-268, DEC-141 | Nói thẳng | |
| ISH-M05-007.2 | QA-268, DEC-141 | Nói thẳng | |

## Phụ lục B. Điểm cần làm rõ (tạm thời)

| ID | Nội dung | Loại | Trạng thái |
|---|---|---|---|
| OP-M05-01 | AI gợi ý Topic (5.4): nguồn chưa nêu lý do vì sao tính năng này cần tồn tại ngoài việc hỗ trợ phân loại nhanh hơn. | Đề xuất | Mở |
| OP-M05-02 | Quản trị Topic (5.5): nguồn chưa nêu lý do giới hạn Mod/Admin chỉ được sửa tên và gộp, không được xóa Topic. | Đề xuất | Mở |
| OP-M05-03 | Gán Tag (5.6): nguồn chưa nêu lý do chọn mốc tối đa 5 Tag/bài viết và tối đa 30 ký tự/Tag. | Đề xuất | Mở |
| OP-M05-04 | Quản trị Tag khẩn cấp (5.7): nguồn chưa nêu lý do chỉ cho phép ẩn Tag trong tình huống khẩn cấp mà không cho sửa/gộp/xóa trong điều kiện khác. | Đề xuất | Mở |
| OP-M05-05 | Trending (5.8): nguồn chưa nêu lý do chọn cửa sổ 7 ngày (thay vì một giá trị khác). | Đề xuất | Mở |
| OP-M05-06 | DEC-052 ghi chú Trending Topic/Tag "sẽ tích hợp như một mục trong Feed của M14" — tài liệu này mới chỉ viết yêu cầu tính điểm (ISH-M05-006), chưa viết yêu cầu hiển thị cho người dùng; đề xuất M05 sở hữu phần tính điểm, M14 sở hữu phần hiển thị khi SR của M14 được soạn, cần stakeholder xác nhận ranh giới này. | Đề xuất | Mở |
