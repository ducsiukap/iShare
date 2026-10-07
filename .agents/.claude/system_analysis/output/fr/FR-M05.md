---
module: M05
ten_module: Topic & Tag
ma_tai_lieu: FR-M05
phien_ban: 1.1
trang_thai: Đã chốt
ngay: 2026-10-07
tac_gia: Phạm Văn Đức
moc_nguon: DEC-146, QA-291, ISS-231, OPEN-009
steps_completed: [1, 2, 3, 4, 5, 6, 7]
---
# Tài liệu yêu cầu chức năng — M05 Topic & Tag

| Mã tài liệu | FR-M05 |
|---|---|
| Dự án | iShare |
| Module | M05 — Topic & Tag |
| Trạng thái | Đã chốt |
| Phiên bản | 1.1 |
| Ngày | 2026-10-07 |
| Tác giả | Phạm Văn Đức |

<!-- Quy ước chung cho mọi bảng dưới đây:
     - Thân tài liệu không ghi nguồn. Nguồn của mọi ID nằm ở Phụ lục A.
     - Ô không có nội dung ghi "—". Không xóa cột.
     - Mục chưa tới bước làm thì để dòng "(Chưa làm — bước N)". -->

## 1. Tổng quan

### 1.1 Mục đích

Module Topic & Tag giúp người dùng phân loại bài viết theo hai trục: Topic là lĩnh vực nội dung lấy từ một danh mục
do Admin quản lý, dùng để lọc và duyệt; Tag là từ khóa tự do, chi tiết hơn Topic. Khi đăng hoặc sửa bài, người dùng có thể nhờ AI
gợi ý Topic rồi tự quyết định lựa chọn cuối cùng. Module cũng tính mức độ thịnh hành (Trending) của Topic và Tag để các
phần khám phá nội dung sử dụng.

### 1.2 Phạm vi

**Trong phạm vi:**

- Danh mục Topic cấu trúc phẳng; gán Topic cho bài viết (số lượng tối thiểu và tối đa mỗi bài).
- Gợi ý Topic bằng AI khi soạn bài và khi tác giả sửa bài đã gửi: kích hoạt bằng nút, điều kiện độ dài nội dung, cảnh báo khi nội dung đổi sau
  gợi ý, xử lý khi gợi ý thất bại hoặc sai danh mục, giới hạn tần suất, ghi nhận phản hồi từ lựa chọn cuối của
  người dùng.
- Hành vi khi tính năng gợi ý Topic bị tắt: người dùng tự chọn Topic từ danh mục.
- Tag tự do: tự tạo khi người dùng gắn, giới hạn số Tag mỗi bài và độ dài mỗi Tag, chuẩn hóa tên.
- Admin quản lý danh mục Topic: thêm Topic, gộp Topic, xóa Topic không có bài viết nào ngoài bài nháp.
- Mod và Admin vô hiệu hóa Tag trong tình huống khủng hoảng, và hệ quả với bài cũ và lần gắn sau; kích hoạt lại Tag
  đã vô hiệu hóa.
- Tác giả đổi Topic, Tag khi sửa bài viết đã gửi; Mod và Admin đổi Topic, Tag trên bài viết của người khác.
- Tính điểm và thứ tự Trending Topic, Trending Tag.
- Ghi nhật ký các thao tác của Mod, Admin lên Tag và lên Topic, Tag của bài người khác.
- Xem danh sách Topic và Tag, gồm cả Guest.

**Ngoài phạm vi:**

- Hiển thị tab Trending và các sub-view Topic/Tag trong Feed — M14 Feed & Discovery.
- Tìm kiếm, autocomplete, lọc bài theo Topic và Tag — M06 Search. Xem các bài viết của một Topic hoặc Tag được
  làm qua bộ lọc của M06; M05 không có trang liệt kê bài viết riêng theo Topic/Tag.
- Theo dõi (Follow) Topic và thông báo khi có bài mới trong Topic đang theo dõi — M07 Notification.
- Lớp/Khối trên bài viết — M03 Post & Content; trên hồ sơ — M02 User Profile. Draft gom Lớp/Khối vào module
  Topic/Tag, nhưng register đặt trường này ở M03.
- Công tắc bật/tắt AI (tổng và riêng cho gợi ý Topic) — M10 Admin Panel; thời gian chờ, thử lại, ghi log kết quả AI,
  đánh giá chất lượng AI — M13 AI Layer.
- Chọn và trình bày Topic, Tag trong trình soạn bài — M03 Post & Content (M05 chỉ đặt quy tắc).
- Thống kê phân bố bài theo Topic — M15 Analytics & Stats.
- Đã quyết là không làm: AI gợi ý Tag; Mod duyệt kết quả gợi ý Topic; đổi tên Topic; xóa Topic có bài viết ngoài bài nháp; thông báo cho tác giả khi Mod, Admin đổi Topic, Tag trên bài;
  sửa, gộp, xóa Tag trong điều kiện bình thường; Topic/Tag cho Comment; cấu trúc Topic lồng nhau (hoãn);
  badge theo chủ đề; lượt xem trong Trending (hoãn ở MS1).

## 2. Thuật ngữ và viết tắt

### 2.1 Thuật ngữ

| Thuật ngữ | Định nghĩa |
|---|---|
| Topic | Lĩnh vực nội dung lấy từ danh mục Topic, dùng để lọc và duyệt bài viết. Mỗi bài viết khi gửi có từ 1 đến 3 Topic. |
| Danh mục Topic | Danh sách mọi Topic đang có trong hệ thống: 11 Topic ban đầu và các Topic Admin thêm sau. Cấu trúc phẳng, không có Topic con. |
| Tag | Từ khóa tự do do tác giả nhập cho bài viết, chi tiết hơn Topic, không có danh sách cố định. Tên chỉ gồm chữ cái, chữ số và "_". Hiển thị bằng tên chuẩn hóa chữ thường với dấu "#" phía trước, ví dụ #bayes. |
| Tên Tag chuẩn hóa | Tên Tag sau khi chuyển toàn bộ về chữ thường. Hai Tag có cùng tên chuẩn hóa là một Tag. |
| Tag hoạt động, Tag bị vô hiệu hóa | Hai trạng thái của Tag. Tag bị vô hiệu hóa là Tag Mod hoặc Admin đã ngừng hiển thị trong tình huống khủng hoảng; Tag vẫn tồn tại và có thể được kích hoạt lại. |
| Tình huống khủng hoảng | Trường hợp Mod hoặc Admin đánh giá một Tag cần ngừng hiển thị trên toàn hệ thống. Nguồn không nêu tiêu chí cụ thể; việc đánh giá thuộc về Mod hoặc Admin. |
| Gợi ý Topic | Việc AI đề xuất tối đa 3 Topic từ tiêu đề và nội dung chữ của bài viết đang soạn hoặc đang sửa, chỉ chạy khi tác giả bấm nút "Gợi ý topic". Draft gọi là AI Classification. |
| Gợi ý lỗi thời | Gợi ý Topic mà sau đó tiêu đề hoặc nội dung chữ của bài viết đã thay đổi. |
| Phản hồi gợi ý | Bản ghi so sánh các Topic AI gợi ý với các Topic tác giả chọn cuối cùng khi gửi bài viết hoặc lưu bản sửa, dùng để đánh giá chất lượng AI. |
| Nội dung chữ | Phần văn bản thuần của bài viết, không gồm định dạng và tệp đính kèm. |
| Gửi bài viết | Thao tác tác giả nộp bài viết để đăng, làm bài rời trạng thái nháp (M03). |
| Bài nháp | Bài viết tác giả đang soạn và chưa gửi (M03). |
| Bài mới (trong Trending) | Bài viết được đăng trong cửa sổ 7 ngày. |
| Feed chính | Dòng bài viết chung của hệ thống (M14), gồm bài đã đăng, không bị ẩn bởi kiểm duyệt, kể cả bài của nhóm Public, không gồm bài của nhóm Private. |
| Nhật ký kiểm duyệt | Nhật ký ghi thao tác của Mod và Admin (M08): người thực hiện, loại thao tác, đối tượng, lý do, thời điểm. |
| Sửa bài viết | Thao tác thay đổi một bài viết đã gửi, do tác giả, Mod hoặc Admin thực hiện. |
| Tương tác | Một trong các sự kiện được tính vào điểm Trending: bài viết được đăng, upvote cho bài viết, comment, bookmark. |
| Upvote | Lượt đánh giá tích cực cho một bài viết (Post Star). |
| Bookmark | Việc người dùng lưu một bài viết để đọc lại. Riêng tư, chỉ chủ tài khoản thấy. |
| Cửa sổ 7 ngày | Khoảng 7 × 24 giờ tính ngược từ thời điểm tính điểm Trending. Cửa sổ trượt theo thời điểm tính, không theo tuần lịch. |
| Điểm Trending | Tổng điểm tương tác của một Topic hoặc Tag trong cửa sổ 7 ngày, theo BR-M05-29. |
| Từ | Đơn vị đếm độ dài khi xét điều kiện gợi ý Topic: mỗi cụm ký tự cách nhau bởi khoảng trắng là một từ, nên mỗi âm tiết tiếng Việt là một từ. Ví dụ "Định lý Bayes là gì" là 5 từ. |
| Ký tự | Đơn vị đếm độ dài tên Tag. Mỗi chữ cái (kể cả chữ có dấu), chữ số hoặc "_" là một ký tự; dấu "#" phía trước không được tính. |
| Giờ hệ thống | Mọi thời điểm hiển thị cho người dùng theo giờ Việt Nam (UTC+7), không đổi theo mùa. |

### 2.2 Viết tắt

| Viết tắt | Đầy đủ |
|---|---|
| FR | Functional Requirement — yêu cầu chức năng |

## 3. Thông tin đầu vào

### 3.1 Tài liệu đầu vào

| Tài liệu | Phiên bản / mốc |
|---|---|
| Draft: docs/_temp/iShare_modules.md, iShare_specs_general.md | Theo ngày sửa tệp (2026-09-19) |
| Register: decisions, qa-log, issue-queue, open-issues, glossary, module-registry | DEC-146, QA-291, ISS-231, OPEN-009 (khớp `moc_nguon`) |

### 3.2 Tài liệu liên quan

| Module | Liên quan ở điểm nào |
|---|---|
| M01 Authentication & Account | Trang Chính sách quyền riêng tư nêu việc gửi nội dung bài cho AI khi gợi ý Topic. |
| M02 User Profile | Bookmark của người dùng, một tương tác được tính vào Trending. |
| M03 Post & Content | Bài viết là đối tượng được gán Topic và Tag; trình soạn bài là nơi chọn Topic, gắn Tag và bấm gợi ý; trạng thái bài (nháp, đã đăng…); upvote bài viết; sở hữu Lớp/Khối trên bài. |
| M04 Comment | Comment và reply, tương tác được tính vào Trending. |
| M06 Search | Tìm Topic và Tag, autocomplete, lọc bài theo Topic và Tag; Tag bị vô hiệu hóa không hiện trong autocomplete. |
| M07 Notification | Theo dõi Topic và thông báo bài mới trong Topic đang theo dõi; lượt theo dõi đổi theo khi gộp hoặc xóa Topic. |
| M08 Moderation | Nhật ký kiểm duyệt ghi thao tác Tag và việc đổi Topic, Tag trên bài người khác. |
| M10 Admin Panel | Công tắc AI tổng và công tắc riêng cho gợi ý Topic; nhật ký thao tác của Admin. |
| M12 Gamification | Upvote bài viết (điểm thưởng), tương tác được tính vào Trending. |
| M13 AI Layer | Thực hiện gợi ý Topic, thời gian chờ, thử lại, ghi log kết quả AI, vòng phản hồi đánh giá AI. |
| M14 Feed & Discovery | Hiển thị Trending Topic và Trending Tag trong tab Trending, kể cả cho Guest. |
| M15 Analytics & Stats | Dùng phân bố bài theo Topic cho thống kê nội dung. |

## 4. Tổng quan chức năng

### 4.1 Luật, tiêu chuẩn liên quan

Không có.

### 4.2 Vai trò

| Vai trò | Mô tả trong module này |
|---|---|
| Guest | Người chưa đăng nhập. Xem danh sách Topic, Tag và Topic, Tag trên bài viết. Không gán Topic, Tag. |
| User | Người dùng đã đăng nhập. Khi là tác giả bài viết thì gán Topic, gắn Tag và dùng gợi ý Topic cho bài của mình. |
| Mod | Có mọi quyền của User. Thêm quyền đổi Topic, Tag trên bài viết của người khác, vô hiệu hóa Tag trong tình huống khủng hoảng và kích hoạt lại Tag. |
| Admin | Có mọi quyền của Mod. Thêm quyền quản lý danh mục Topic: thêm, gộp, xóa Topic không có bài viết nào ngoài bài nháp. |
| Tác giả bài viết | Vai trò theo ngữ cảnh: User, Mod hoặc Admin đang soạn, gửi hoặc sửa bài viết của chính mình. |
| Hệ thống | Tác nhân của việc tính Trending Topic và Trending Tag định kỳ, và ghi nhận phản hồi cho gợi ý Topic. |

### 4.3 Ma trận quyền

| Hành động | Guest | User | Mod | Admin | Yêu cầu |
|---|---|---|---|---|---|
| Gán Topic cho bài viết của mình khi gửi | ✗ | ✓ (của mình) | ✓ (của mình) | ✓ (của mình) | FR-M05-01.02, FR-M05-01.08 |
| Yêu cầu AI gợi ý Topic cho bài viết đang soạn | ✗ | ✓ (của mình) | ✓ (của mình) | ✓ (của mình) | FR-M05-02.01, FR-M05-02.18 |
| Gắn Tag cho bài viết của mình khi gửi | ✗ | ✓ (của mình) | ✓ (của mình) | ✓ (của mình) | FR-M05-03.01, FR-M05-03.12 |
| Đổi Topic, Tag của bài viết của mình sau khi đã gửi | ✗ | ✓ (của mình) | ✓ (của mình) | ✓ (của mình) | FR-M05-01.06, FR-M05-03.10, FR-M05-01.08, FR-M05-03.12 |
| Đổi Topic, Tag trên bài viết của người khác | ✗ | ✗ | ✓ | ✓ | FR-M05-11.01, FR-M05-11.02, FR-M05-11.04 |
| Xem danh sách Topic và Tag | ✓ | ✓ | ✓ | ✓ | FR-M05-04.01, FR-M05-04.02 |
| Xem Topic, Tag trên bài viết | ✓ | ✓ | ✓ | ✓ | FR-M05-04.04 |
| Thêm Topic vào danh mục | ✗ | ✗ | ✗ | ✓ | FR-M05-06.01, FR-M05-06.03 |
| Gộp hai Topic | ✗ | ✗ | ✗ | ✓ | FR-M05-07.01, FR-M05-07.03 |
| Xóa Topic không có bài viết ngoài bài nháp | ✗ | ✗ | ✗ | ✓ | FR-M05-08.01, FR-M05-08.03 |
| Vô hiệu hóa Tag | ✗ | ✗ | ✓ | ✓ | FR-M05-09.01, FR-M05-09.04 |
| Kích hoạt lại Tag đã vô hiệu hóa | ✗ | ✗ | ✓ | ✓ | FR-M05-10.01, FR-M05-10.04 |

<!-- Ô suy ra: hàng 1–3 cột Guest (Guest không đăng bài); hàng 1–3 cột Mod/Admin (Mod/Admin cũng là tác giả bài của mình);
     hàng 5 cột User (Topic/Tag do tác giả chọn); hàng 6–7 cột User/Mod/Admin (Guest đã xem được thì vai trò cao hơn cũng xem được);
     hàng 8–10 cột Guest/User (chỉ Admin); hàng 11–12 cột Guest/User (chỉ Mod/Admin). Hàng 4–5 theo DEC-142. -->

### 4.4 Danh sách chức năng

| ID | Chức năng | Tác nhân chính | Kích hoạt |
|---|---|---|---|
| FR-M05-01 | Gán Topic cho bài viết | Tác giả bài viết | Tác giả chọn Topic khi soạn và gửi bài viết, hoặc khi sửa bài viết đã gửi |
| FR-M05-02 | Gợi ý Topic bằng AI | Tác giả bài viết | Tác giả bấm nút "Gợi ý topic" khi soạn bài hoặc khi sửa bài đã gửi |
| FR-M05-03 | Gắn Tag cho bài viết | Tác giả bài viết | Tác giả nhập Tag khi soạn và gửi bài viết, hoặc khi sửa bài viết đã gửi |
| FR-M05-04 | Xem danh sách Topic và Tag | Guest, User, Mod, Admin | Người dùng mở danh sách Topic hoặc Tag |
| FR-M05-05 | Tính Trending Topic và Trending Tag | Hệ thống | Đến chu kỳ tính lại định kỳ |
| FR-M05-06 | Thêm Topic | Admin | Admin tạo Topic mới trong danh mục |
| FR-M05-07 | Gộp Topic | Admin | Admin chọn Topic nguồn và Topic đích để gộp |
| FR-M05-08 | Xóa Topic | Admin | Admin chọn xóa một Topic |
| FR-M05-09 | Vô hiệu hóa Tag | Mod, Admin | Mod hoặc Admin chọn vô hiệu hóa một Tag trong tình huống khủng hoảng |
| FR-M05-10 | Kích hoạt lại Tag | Mod, Admin | Mod hoặc Admin chọn kích hoạt lại một Tag đã vô hiệu hóa |
| FR-M05-11 | Đổi Topic, Tag trên bài viết của người khác | Mod, Admin | Mod hoặc Admin chọn đổi Topic, Tag của một bài viết không phải của mình |

### 4.5 Mốc và ưu tiên

Toàn bộ yêu cầu của module thuộc MS1, ưu tiên **Must** (bảng MoSCoW Summary của module-registry: Must gồm M01–M10, M13;
cột MoSCoW ở dòng M05 của bảng Module List bị lệch nên không dùng). Không có yêu cầu ngoại lệ về ưu tiên.

## 5. Yêu cầu chức năng

### 5.1 FR-M05-01 Gán Topic cho bài viết

**Yêu cầu cấp trên:** Hệ thống phải cho phép tác giả gán cho bài viết của mình từ 1 đến 3 Topic thuộc danh mục Topic, khi gửi bài viết và khi sửa bài viết đã gửi.

**Lý do:** Topic là cách phân loại có cấu trúc, dùng để lọc và duyệt bài viết, tổ chức các lĩnh vực tri thức lớn cho học sinh THPT; danh mục được nhóm theo chương trình 2018 và các chủ đề ngoài học tập.

**Yêu cầu cấp dưới:**

| ID | Yêu cầu |
|---|---|
| FR-M05-01.01 | Khi tác giả chọn Topic cho bài viết, hệ thống phải chỉ cho chọn trong các Topic thuộc danh mục Topic. |
| FR-M05-01.02 | Khi tác giả gửi bài viết có từ 1 đến 3 Topic khác nhau, hệ thống phải lưu các Topic đó cho bài viết. |
| FR-M05-01.03 | Nếu tác giả gửi bài viết không có Topic nào, hệ thống phải từ chối gửi bài viết đó. |
| FR-M05-01.04 | Nếu tác giả chọn Topic thứ tư cho một bài viết, hệ thống phải từ chối Topic thứ tư đó. |
| FR-M05-01.05 | Nếu tác giả chọn lại một Topic bài viết đã có, hệ thống phải giữ Topic đó một lần cho bài viết. |
| FR-M05-01.06 | Khi tác giả sửa bài viết đã gửi, hệ thống phải cho phép tác giả thêm hoặc bỏ Topic của bài viết đó. |
| FR-M05-01.07 | Nếu sau khi sửa, bài viết không còn Topic nào hoặc có hơn 3 Topic, hệ thống phải từ chối lưu thay đổi đó. |
| FR-M05-01.08 | Nếu người chưa đăng nhập gán hoặc đổi Topic cho bài viết, hệ thống phải từ chối. |
| FR-M05-01.09 | Nếu Topic tác giả đã chọn bị xóa khỏi danh mục trước khi bài viết được gửi, hệ thống phải từ chối Topic đó. |
| FR-M05-01.10 | Khi tác giả lưu bài nháp, hệ thống phải cho phép bài nháp có từ 0 đến 3 Topic. |

### 5.2 FR-M05-02 Gợi ý Topic bằng AI

**Yêu cầu cấp trên:** Ở nơi gợi ý Topic được bật, hệ thống phải cho phép tác giả yêu cầu AI gợi ý tối đa 3 Topic cho bài viết đang soạn hoặc đang sửa, và tác giả luôn quyết định Topic cuối cùng.

**Lý do:** Topic do AI gợi ý và người dùng xác nhận; AI chỉ gợi ý, con người quyết định cuối cùng; lựa chọn cuối cùng của người dùng là phản hồi để đánh giá AI.

**Yêu cầu cấp dưới:**

| ID | Yêu cầu |
|---|---|
| FR-M05-02.01 | Khi tác giả bấm nút "Gợi ý topic", hệ thống phải gửi tiêu đề và nội dung chữ của bài viết đang soạn, không gồm tệp đính kèm, để AI gợi ý Topic. |
| FR-M05-02.02 | Hệ thống phải không tự gợi ý Topic khi tác giả chưa bấm nút "Gợi ý topic". |
| FR-M05-02.03 | Khi AI trả về Topic hợp lệ, hệ thống phải hiển thị tối đa 3 Topic được gợi ý ở trạng thái đã chọn sẵn. |
| FR-M05-02.04 | Khi tác giả bỏ chọn hoặc chọn thêm Topic sau khi có gợi ý, hệ thống phải áp dụng lựa chọn của tác giả trong giới hạn của FR-M05-01. |
| FR-M05-02.05 | Nếu tiêu đề cộng nội dung chữ của bài viết có ít hơn 20 từ, hệ thống phải không gợi ý và báo nội dung quá ngắn. |
| FR-M05-02.06 | Nếu mọi Topic AI trả về đều không thuộc danh mục Topic hiện tại, hệ thống phải coi lần gợi ý đó là thất bại. |
| FR-M05-02.07 | Nếu lần gợi ý thất bại khi AI đang bật, hệ thống phải hiển thị thông báo không chặn "Không thể gợi ý chủ đề lúc này, vui lòng chọn thủ công". |
| FR-M05-02.08 | Nếu lần gợi ý thất bại, hệ thống phải không tự chọn Topic nào cho bài viết. |
| FR-M05-02.09 | Khi tiêu đề hoặc nội dung chữ thay đổi sau lần gợi ý, hệ thống phải đánh dấu gợi ý đó là lỗi thời. |
| FR-M05-02.10 | Trong khi gợi ý gần nhất đang lỗi thời, hệ thống phải hiển thị cảnh báo nhẹ kèm nút gợi ý lại. |
| FR-M05-02.11 | Trong khi gợi ý gần nhất đang lỗi thời, hệ thống phải vẫn cho phép tác giả gửi bài viết. |
| FR-M05-02.12 | Khi tác giả gửi bài viết hoặc lưu bản sửa mà gợi ý gần nhất chưa lỗi thời, hệ thống phải ghi phản hồi gợi ý gồm các Topic đã gợi ý và các Topic tác giả chọn cuối cùng. |
| FR-M05-02.13 | Nếu gợi ý gần nhất đã lỗi thời khi tác giả gửi bài viết hoặc lưu bản sửa, hệ thống phải không ghi phản hồi gợi ý. |
| FR-M05-02.14 | Nếu tác giả gửi bài viết mà không dùng gợi ý Topic, hệ thống phải không ghi phản hồi gợi ý. |
| FR-M05-02.15 | Nếu một người dùng yêu cầu gợi ý Topic lần thứ 11 trong vòng 60 giây gần nhất, hệ thống phải từ chối yêu cầu đó. |
| FR-M05-02.16 | Trong khi công tắc AI tổng hoặc công tắc gợi ý Topic đang tắt, hệ thống phải không cung cấp gợi ý Topic. |
| FR-M05-02.17 | Trong khi công tắc AI tổng hoặc công tắc gợi ý Topic đang tắt, hệ thống phải cho tác giả chọn Topic thủ công từ danh mục Topic. |
| FR-M05-02.18 | Nếu người chưa đăng nhập yêu cầu gợi ý Topic, hệ thống phải từ chối. |
| FR-M05-02.19 | Nếu một phần Topic AI trả về không thuộc danh mục Topic hiện tại, hệ thống phải bỏ các Topic đó và chỉ hiển thị các Topic hợp lệ. |
| FR-M05-02.20 | Khi tác giả sửa bài viết đã gửi, hệ thống phải cho tác giả dùng gợi ý Topic theo cùng các quy tắc như khi soạn bài. |
| FR-M05-02.21 | Khi Mod hoặc Admin đổi Topic trên bài viết của người khác, hệ thống phải không cung cấp gợi ý Topic. |

### 5.3 FR-M05-03 Gắn Tag cho bài viết

**Yêu cầu cấp trên:** Hệ thống phải cho phép tác giả gắn tối đa 5 Tag tự do cho bài viết của mình khi gửi bài viết và khi sửa bài viết đã gửi; Tag chưa tồn tại được tự tạo.

**Lý do:** Tag là từ khóa tự do do người dùng tự quyết hoàn toàn, chi tiết hơn Topic, không có danh sách cố định.

**Yêu cầu cấp dưới:**

| ID | Yêu cầu |
|---|---|
| FR-M05-03.01 | Khi tác giả gửi bài viết có từ 0 đến 5 Tag hợp lệ, hệ thống phải lưu các Tag đó cho bài viết. |
| FR-M05-03.02 | Khi tác giả gắn một Tag chưa tồn tại, hệ thống phải tạo Tag đó ở trạng thái hoạt động mà không cần ai duyệt. |
| FR-M05-03.03 | Khi tác giả gắn một Tag có cùng tên chuẩn hóa với một Tag đã có, hệ thống phải dùng Tag đã có. |
| FR-M05-03.04 | Nếu tác giả gắn Tag thứ sáu cho một bài viết, hệ thống phải từ chối Tag thứ sáu đó. |
| FR-M05-03.05 | Nếu tên Tag, không tính dấu "#", dài hơn 30 ký tự, hệ thống phải từ chối Tag đó. |
| FR-M05-03.06 | Nếu tên Tag chứa ký tự ngoài chữ cái, chữ số và dấu gạch dưới, hệ thống phải từ chối Tag đó. |
| FR-M05-03.07 | Nếu tên Tag không có chữ cái nào, hệ thống phải từ chối Tag đó. |
| FR-M05-03.08 | Nếu tác giả gắn cùng một Tag hai lần cho một bài viết, hệ thống phải giữ Tag đó một lần cho bài viết. |
| FR-M05-03.09 | Nếu tác giả nhập tên của một Tag đang bị vô hiệu hóa, hệ thống phải hiển thị phần nhập đó như văn bản, không gắn Tag đó cho bài viết. |
| FR-M05-03.10 | Khi tác giả sửa bài viết đã gửi, hệ thống phải cho phép tác giả thêm hoặc bỏ Tag của bài viết đó trong giới hạn 5 Tag. |
| FR-M05-03.11 | Hệ thống phải không dùng AI để gợi ý hay gắn Tag. |
| FR-M05-03.12 | Nếu người chưa đăng nhập gắn hoặc đổi Tag cho bài viết, hệ thống phải từ chối. |
| FR-M05-03.13 | Hệ thống phải không cho gắn Topic hay Tag cho comment. |
| FR-M05-03.14 | Hệ thống phải hiển thị mọi Tag bằng tên chuẩn hóa chữ thường, có dấu "#" phía trước. |

### 5.4 FR-M05-04 Xem danh sách Topic và Tag

**Yêu cầu cấp trên:** Hệ thống phải cho mọi người, kể cả Guest, xem danh sách Topic, danh sách Tag đang hoạt động, và Topic, Tag của từng bài viết.

**Lý do:** Topic dùng để lọc và duyệt bài viết; Guest được xem danh sách Topic và Tag theo quyền Guest đã chốt.

**Yêu cầu cấp dưới:**

| ID | Yêu cầu |
|---|---|
| FR-M05-04.01 | Khi một người, kể cả Guest, mở danh sách Topic, hệ thống phải hiển thị mọi Topic trong danh mục Topic. |
| FR-M05-04.02 | Khi một người, kể cả Guest, mở danh sách Tag, hệ thống phải hiển thị các Tag đang hoạt động. |
| FR-M05-04.03 | Hệ thống phải không hiển thị Tag bị vô hiệu hóa trong danh sách Tag. |
| FR-M05-04.04 | Khi một người xem một bài viết, hệ thống phải hiển thị các Topic và các Tag đang hoạt động của bài viết đó. |
| FR-M05-04.05 | Nếu một Tag của bài viết đang bị vô hiệu hóa, hệ thống phải không hiển thị Tag đó trên bài viết. |
| FR-M05-04.06 | Hệ thống phải có sẵn trong danh mục Topic 11 Topic ban đầu theo BR-M05-02. |

### 5.5 FR-M05-05 Tính Trending Topic và Trending Tag

**Yêu cầu cấp trên:** Hệ thống phải định kỳ tính điểm Trending cho mỗi Topic và mỗi Tag đang hoạt động từ các tương tác trong cửa sổ 7 ngày, và cung cấp danh sách xếp hạng cho Feed.

**Lý do:** Trending Topic và Trending Tag là phần riêng của Feed để người dùng xem nội dung đang được quan tâm theo chủ đề.

**Yêu cầu cấp dưới:**

| ID | Yêu cầu |
|---|---|
| FR-M05-05.01 | Khi đến chu kỳ tính lại, hệ thống phải tính điểm Trending của mỗi Topic và mỗi Tag đang hoạt động theo BR-M05-29. |
| FR-M05-05.02 | Hệ thống phải đưa mọi tương tác vào điểm Trending chậm nhất 30 phút sau khi tương tác xảy ra. |
| FR-M05-05.03 | Hệ thống phải chỉ tính các tương tác xảy ra trong cửa sổ 7 ngày tính ngược từ thời điểm tính. |
| FR-M05-05.04 | Hệ thống phải tính tương tác trên một bài viết bất kể bài viết đó được đăng lúc nào. |
| FR-M05-05.05 | Nếu một tương tác đã bị rút lại trước thời điểm tính, hệ thống phải không tính tương tác đó. |
| FR-M05-05.06 | Khi một bài viết có nhiều Topic hoặc Tag, hệ thống phải cộng điểm tương tác của bài viết đó cho từng Topic và từng Tag của bài. |
| FR-M05-05.07 | Hệ thống phải không tính điểm Trending cho Tag bị vô hiệu hóa. |
| FR-M05-05.08 | Hệ thống phải không tính lượt xem bài viết vào điểm Trending. |
| FR-M05-05.09 | Hệ thống phải xếp danh sách Trending Topic và Trending Tag theo điểm Trending giảm dần, rồi theo số bài mới giảm dần, rồi theo tên từ A đến Z. |
| FR-M05-05.10 | Trong khi chưa đến lần tính kế tiếp, hệ thống phải cung cấp kết quả của lần tính gần nhất. |
| FR-M05-05.11 | Hệ thống phải chỉ tính tương tác trên các bài viết đang hiển thị trên feed chính: đã đăng, không bị ẩn bởi kiểm duyệt, gồm bài của nhóm Public và không gồm bài của nhóm Private. |
| FR-M05-05.12 | Hệ thống phải không tính upvote cho comment vào điểm Trending. |
| FR-M05-05.13 | Khi tính comment vào điểm Trending, hệ thống phải tính cả reply của comment. |
| FR-M05-05.14 | Hệ thống phải chỉ đưa vào danh sách Trending các Topic và Tag có điểm Trending lớn hơn 0. |

### 5.6 FR-M05-06 Thêm Topic

**Yêu cầu cấp trên:** Hệ thống phải cho phép Admin thêm Topic mới vào danh mục Topic.

**Lý do:** Nguồn chưa nêu lý do.

**Yêu cầu cấp dưới:**

| ID | Yêu cầu |
|---|---|
| FR-M05-06.01 | Khi Admin thêm một Topic có tên chưa trùng với Topic nào trong danh mục, hệ thống phải thêm Topic đó vào danh mục Topic. |
| FR-M05-06.02 | Nếu tên Topic mới trùng tên một Topic đã có trong danh mục, hệ thống phải từ chối thêm Topic đó. |
| FR-M05-06.03 | Nếu người thêm Topic không là Admin, hệ thống phải từ chối. |
| FR-M05-06.04 | Khi một Topic mới được thêm, hệ thống phải cho phép chọn Topic đó khi gán Topic và khi AI gợi ý Topic. |
| FR-M05-06.05 | Khi một Topic mới được thêm, hệ thống phải không tự gán Topic đó cho bài viết đã có. |
| FR-M05-06.06 | Hệ thống phải không giới hạn số lượng Topic trong danh mục Topic. |
| FR-M05-06.07 | Khi Admin thêm một Topic, hệ thống phải đặt Topic đó ngang cấp với mọi Topic khác trong danh mục, không làm Topic con của Topic nào. |
| FR-M05-06.08 | Khi so trùng tên Topic, hệ thống phải không phân biệt chữ hoa, chữ thường và bỏ qua khoảng trắng thừa ở đầu, cuối và giữa tên, nhưng phân biệt dấu. |

### 5.7 FR-M05-07 Gộp Topic

**Yêu cầu cấp trên:** Hệ thống phải cho phép Admin gộp một Topic nguồn vào một Topic đích, chuyển mọi bài viết của Topic nguồn sang Topic đích.

**Lý do:** Nguồn chưa nêu lý do.

**Yêu cầu cấp dưới:**

| ID | Yêu cầu |
|---|---|
| FR-M05-07.01 | Khi Admin gộp Topic nguồn vào Topic đích, hệ thống phải chuyển mọi bài viết đang có Topic nguồn sang có Topic đích thay cho Topic nguồn. |
| FR-M05-07.02 | Nếu một bài viết đã có cả Topic nguồn và Topic đích, hệ thống phải giữ Topic đích một lần cho bài viết đó sau khi gộp. |
| FR-M05-07.03 | Nếu người gộp Topic không là Admin, hệ thống phải từ chối. |
| FR-M05-07.04 | Nếu Topic nguồn và Topic đích là cùng một Topic, hệ thống phải từ chối gộp. |
| FR-M05-07.05 | Khi gộp xong, hệ thống phải xóa Topic nguồn khỏi danh mục Topic. |
| FR-M05-07.06 | Khi gộp xong, hệ thống phải chuyển người đang theo dõi Topic nguồn sang theo dõi Topic đích, trừ người đã theo dõi Topic đích. |

### 5.8 FR-M05-08 Xóa Topic

**Yêu cầu cấp trên:** Hệ thống phải cho phép Admin xóa một Topic khỏi danh mục Topic khi Topic đó không có bài viết nào ngoài bài nháp.

**Lý do:** Nguồn chưa nêu lý do.

**Yêu cầu cấp dưới:**

| ID | Yêu cầu |
|---|---|
| FR-M05-08.01 | Khi Admin xóa một Topic không có bài viết nào ngoài bài nháp, hệ thống phải xóa Topic đó khỏi danh mục Topic. |
| FR-M05-08.02 | Nếu Topic có ít nhất một bài viết ngoài bài nháp, kể cả bài đã xóa còn trong thời gian khôi phục, hệ thống phải từ chối xóa Topic đó. |
| FR-M05-08.03 | Nếu người xóa Topic không là Admin, hệ thống phải từ chối. |
| FR-M05-08.04 | Khi một Topic bị xóa, hệ thống phải không cho chọn Topic đó khi gán Topic và khi AI gợi ý Topic. |
| FR-M05-08.05 | Khi một Topic bị xóa, hệ thống phải bỏ Topic đó khỏi các bài nháp đang có nó. |
| FR-M05-08.06 | Khi một Topic bị xóa, hệ thống phải bỏ mọi lượt theo dõi Topic đó. |

### 5.9 FR-M05-09 Vô hiệu hóa Tag

**Yêu cầu cấp trên:** Hệ thống phải cho phép Mod và Admin vô hiệu hóa một Tag trong tình huống khủng hoảng, làm Tag ngừng hiển thị trên toàn hệ thống mà không xóa Tag.

**Lý do:** Nguồn chưa nêu lý do.

**Yêu cầu cấp dưới:**

| ID | Yêu cầu |
|---|---|
| FR-M05-09.01 | Khi Mod hoặc Admin vô hiệu hóa một Tag đang hoạt động, hệ thống phải chuyển Tag đó sang trạng thái bị vô hiệu hóa. |
| FR-M05-09.02 | Trong khi một Tag bị vô hiệu hóa, hệ thống phải không hiển thị Tag đó trong gợi ý tự động khi nhập. |
| FR-M05-09.03 | Trong khi một Tag bị vô hiệu hóa, hệ thống phải giữ liên kết giữa Tag đó và các bài viết đã gắn nó. |
| FR-M05-09.04 | Nếu người vô hiệu hóa Tag không là Mod hoặc Admin, hệ thống phải từ chối. |
| FR-M05-09.05 | Nếu Tag đã ở trạng thái bị vô hiệu hóa, hệ thống phải giữ nguyên trạng thái đó khi có yêu cầu vô hiệu hóa lần nữa. |
| FR-M05-09.06 | Hệ thống phải không cho Mod hoặc Admin sửa tên, gộp hay xóa Tag. |
| FR-M05-09.07 | Khi Mod hoặc Admin vô hiệu hóa một Tag, hệ thống phải ghi thao tác đó vào nhật ký kiểm duyệt gồm người thực hiện, loại thao tác, Tag, lý do nếu có và thời điểm. |

### 5.10 FR-M05-10 Kích hoạt lại Tag

**Yêu cầu cấp trên:** Hệ thống phải cho phép Mod và Admin kích hoạt lại một Tag đã bị vô hiệu hóa.

**Lý do:** Nguồn chưa nêu lý do.

**Yêu cầu cấp dưới:**

| ID | Yêu cầu |
|---|---|
| FR-M05-10.01 | Khi Mod hoặc Admin kích hoạt lại một Tag bị vô hiệu hóa, hệ thống phải chuyển Tag đó sang trạng thái hoạt động. |
| FR-M05-10.02 | Khi một Tag được kích hoạt lại, hệ thống phải hiển thị lại Tag đó trong gợi ý tự động, Trending Tag, danh sách Tag và trên các bài viết còn liên kết với nó. |
| FR-M05-10.03 | Khi một Tag được kích hoạt lại, hệ thống phải không tự chuyển phần chữ đã nhập trong thời gian Tag bị vô hiệu hóa thành Tag. |
| FR-M05-10.04 | Nếu người kích hoạt lại Tag không là Mod hoặc Admin, hệ thống phải từ chối. |
| FR-M05-10.05 | Nếu Tag đang hoạt động, hệ thống phải giữ nguyên trạng thái đó khi có yêu cầu kích hoạt lại. |
| FR-M05-10.06 | Khi Mod hoặc Admin kích hoạt lại một Tag, hệ thống phải ghi thao tác đó vào nhật ký kiểm duyệt gồm người thực hiện, loại thao tác, Tag, lý do nếu có và thời điểm. |

### 5.11 FR-M05-11 Đổi Topic, Tag trên bài viết của người khác

**Yêu cầu cấp trên:** Hệ thống phải cho phép Mod và Admin đổi Topic và Tag trên bài viết của người khác, trong cùng giới hạn áp cho tác giả.

**Lý do:** Nguồn chưa nêu lý do.

**Yêu cầu cấp dưới:**

| ID | Yêu cầu |
|---|---|
| FR-M05-11.01 | Khi Mod hoặc Admin đổi Topic của bài viết của người khác thành từ 1 đến 3 Topic thuộc danh mục, hệ thống phải lưu các Topic đó cho bài viết. |
| FR-M05-11.02 | Khi Mod hoặc Admin đổi Tag của bài viết của người khác thành tối đa 5 Tag hợp lệ, hệ thống phải lưu các Tag đó cho bài viết. |
| FR-M05-11.03 | Nếu thay đổi làm bài viết không còn Topic nào, có hơn 3 Topic hoặc có hơn 5 Tag, hệ thống phải từ chối thay đổi đó. |
| FR-M05-11.04 | Nếu người đổi Topic hoặc Tag của một bài viết không là tác giả, Mod hoặc Admin, hệ thống phải từ chối. |
| FR-M05-11.05 | Khi Mod hoặc Admin đổi Topic hoặc Tag trên bài viết của người khác, hệ thống phải không gửi thông báo cho tác giả. |
| FR-M05-11.06 | Khi Mod hoặc Admin đổi Topic hoặc Tag trên bài viết của người khác, hệ thống phải không ghi thay đổi đó vào lịch sử sửa bài viết. |
| FR-M05-11.07 | Khi Mod hoặc Admin đổi Topic hoặc Tag trên bài viết của người khác, hệ thống phải ghi thao tác đó vào nhật ký kiểm duyệt gồm người thực hiện, loại thao tác, bài viết, lý do nếu có và thời điểm. |

### 5.12 Quy tắc nghiệp vụ

| ID | Loại | Quy tắc | Ví dụ |
|---|---|---|---|
| BR-M05-01 | Sự kiện | Danh mục Topic có cấu trúc phẳng: không Topic nào là Topic con của Topic khác. | — |
| BR-M05-02 | Sự kiện | Danh mục Topic ban đầu gồm 11 Topic: Toán học, Ngữ văn, Ngoại ngữ, Khoa học tự nhiên (Lý/Hóa/Sinh), Khoa học xã hội (Sử/Địa/KT&PL), Tin học, Kỹ năng mềm, Hướng nghiệp, Nghệ thuật & Sáng tạo, Góc Chill, Khác. | — |
| BR-M05-03 | Ràng buộc | Mỗi bài viết khi gửi có ít nhất 1 và tối đa 3 Topic, các Topic khác nhau và đều thuộc danh mục Topic. Bài nháp được có từ 0 đến 3 Topic. | Gửi bài không có Topic: từ chối. Lưu nháp không có Topic: hợp lệ. Gửi với Toán học, Tin học, Khác: hợp lệ. Đã chọn 3 Topic, chọn thêm Góc Chill: Góc Chill bị từ chối, bài vẫn giữ 3 Topic. |
| BR-M05-04 | Ràng buộc | Khi sửa bài viết đã gửi, bài viết vẫn phải có 1–3 Topic và tối đa 5 Tag, dù người sửa là tác giả, Mod hay Admin. | Bài có đúng 1 Topic là Tin học; người sửa bỏ Tin học mà không chọn Topic khác: lưu bị từ chối. Bài có 5 Tag, thêm Tag thứ 6: Tag thứ 6 bị từ chối. |
| BR-M05-05 | Ràng buộc | Tên Topic không được trùng tên một Topic khác trong danh mục. Khi so trùng: không phân biệt chữ hoa, chữ thường; bỏ khoảng trắng thừa ở đầu, cuối và giữa; dấu được giữ. | "Tin học", "tin học", " Tin  học ": trùng nhau. "Tin hoc" và "Tin học": không trùng. Đã có "Tin học", Admin thêm "tin học": từ chối. |
| BR-M05-06 | Ràng buộc | Danh mục Topic không giới hạn số lượng Topic. | — |
| BR-M05-07 | Suy diễn | Topic mới được thêm vào danh mục không tự được gán cho bài viết đã có. | Admin thêm "Tài chính cá nhân"; 20 bài cũ đang ở "Khác" vẫn giữ "Khác" cho tới khi được sửa. |
| BR-M05-08 | Ràng buộc | Chỉ xóa được Topic không có bài viết nào ngoài bài nháp. Bài chờ duyệt, đã đăng, tự ẩn, bị từ chối và bài đã xóa còn trong 7 ngày khôi phục đều được đếm. Khi Topic bị xóa, các bài nháp có Topic đó mất Topic này, và mọi lượt theo dõi Topic đó bị bỏ. | Topic chỉ có 2 bài nháp: xóa được; 2 bài nháp còn 0 Topic. Topic có 1 bài đã xóa 2 ngày trước (còn khôi phục được): từ chối xóa. |
| BR-M05-09 | Kích hoạt | Khi Admin gộp Topic nguồn vào Topic đích, mọi bài viết đang có Topic nguồn chuyển sang có Topic đích thay cho Topic nguồn; một bài viết không có cùng một Topic hai lần. Sau đó Topic nguồn bị xóa khỏi danh mục, và người đang theo dõi Topic nguồn chuyển sang theo dõi Topic đích. | Gộp "Tin hoc" (12 bài, 30 người theo dõi) vào "Tin học": 12 bài có "Tin học"; "Tin hoc" không còn trong danh mục; 30 người theo dõi "Tin học" (ai đã theo dõi rồi thì giữ nguyên). Bài Y có {Tin hoc, Tin học, Toán học}: sau gộp có {Tin học, Toán học}. |
| BR-M05-10 | Kích hoạt | Gợi ý Topic chỉ chạy khi tác giả bấm nút "Gợi ý topic", không tự chạy; dùng được khi soạn bài và khi tác giả sửa bài đã gửi. Tác giả chọn Topic thủ công từ đầu thì không qua gợi ý. Mod, Admin đổi Topic trên bài của người khác không dùng gợi ý. | — |
| BR-M05-11 | Ràng buộc | Gợi ý Topic chỉ dựa trên tiêu đề và nội dung chữ của bài viết; tệp đính kèm không được xét. | — |
| BR-M05-12 | Ràng buộc | Nếu tiêu đề cộng nội dung chữ có ít hơn 20 từ, hệ thống không gợi ý và báo nội dung quá ngắn. | Tiêu đề "Cách giải phương trình bậc hai có tham số m" (10 từ) và nội dung "Mình làm mãi không ra, mọi người giúp với" (9 từ): 19 từ, không gợi ý. Thêm một từ vào nội dung: 20 từ, gợi ý. |
| BR-M05-13 | Ràng buộc | Mỗi lần gợi ý trả về tối đa 3 Topic, các Topic này được chọn sẵn; tác giả bỏ chọn hoặc chọn thêm tự do trong giới hạn BR-M05-03. | AI gợi ý Toán học, Tin học; tác giả bỏ Tin học, thêm Hướng nghiệp: bài gửi với Toán học, Hướng nghiệp. |
| BR-M05-14 | Ràng buộc | Topic được gợi ý phải thuộc danh mục Topic hiện tại. Topic ngoài danh mục bị bỏ, các Topic hợp lệ được giữ; chỉ khi không còn Topic hợp lệ nào thì lần gợi ý được coi là thất bại. | AI trả về {Toán học, Vật lý, Tin học}, "Vật lý" không có trong danh mục: hiển thị Toán học, Tin học. AI trả về {Vật lý}: gợi ý thất bại. Danh mục vừa có "Tài chính cá nhân": AI gợi ý được Topic này. |
| BR-M05-15 | Suy diễn | Nếu tiêu đề hoặc nội dung chữ thay đổi sau khi gợi ý, gợi ý trở thành lỗi thời: hệ thống hiện cảnh báo nhẹ và nút gợi ý lại, không chặn việc gửi bài. | Gợi ý lúc 10:00, tác giả thêm một đoạn lúc 10:02: hiện cảnh báo; tác giả vẫn gửi được. |
| BR-M05-16 | Suy diễn | Phản hồi gợi ý chỉ được ghi khi gửi bài viết hoặc lưu bản sửa mà gợi ý gần nhất chưa lỗi thời. Gợi ý lỗi thời, hoặc tác giả không dùng gợi ý, thì không ghi phản hồi. | Gợi ý {Toán học, Tin học}, nội dung không đổi, gửi với {Toán học}: ghi phản hồi. Gợi ý xong rồi sửa nội dung, gửi luôn: không ghi. |
| BR-M05-17 | Ràng buộc | Mỗi người dùng được yêu cầu gợi ý Topic tối đa 10 lần trong 60 giây gần nhất. | 10 lần trong 10:00:30–10:00:59: đều được. Lần thứ 11 lúc 10:01:10: từ chối (60 giây gần nhất đã có 10 lần). Lần thứ 11 lúc 10:01:31: được. |
| BR-M05-18 | Suy diễn | Khi công tắc AI tổng hoặc công tắc gợi ý Topic đang tắt, hệ thống không gợi ý Topic; tác giả tự chọn Topic từ danh mục. | Công tắc tổng bật, công tắc gợi ý Topic tắt: không có gợi ý. Công tắc tổng tắt: không có gợi ý, dù công tắc gợi ý Topic đang bật. |
| BR-M05-19 | Suy diễn | Khi AI đang bật mà gợi ý thất bại (quá thời gian chờ sau lần thử lại, lỗi, hoặc theo BR-M05-14), hệ thống báo lỗi không chặn "Không thể gợi ý chủ đề lúc này, vui lòng chọn thủ công" và không tự chọn Topic nào. | — |
| BR-M05-20 | Ràng buộc | Tag là từ khóa tự do, không có danh sách cố định. Tên Tag chỉ gồm chữ cái (kể cả chữ tiếng Việt có dấu), chữ số và dấu gạch dưới "_", và có ít nhất một chữ cái. | #XácSuất, #đạo_hàm, #lớp12, #covid19: hợp lệ. #Xác Suất (khoảng trắng), #covid-19, #node.js, #c++: không hợp lệ. #12, #2024, #___ (không có chữ cái): không hợp lệ. |
| BR-M05-21 | Kích hoạt | Tag chưa tồn tại được tự tạo khi tác giả gắn nó cho bài viết, không cần ai duyệt. | Chưa có #Bayes; tác giả gắn #Bayes: Tag #Bayes được tạo. |
| BR-M05-22 | Ràng buộc | Mỗi bài viết có tối đa 5 Tag; bài viết không bắt buộc có Tag. | 0 Tag: hợp lệ. 5 Tag: hợp lệ. Tag thứ 6: từ chối. |
| BR-M05-23 | Ràng buộc | Tên mỗi Tag dài tối đa 30 ký tự, không tính dấu "#" phía trước. | "#" cộng 30 ký tự: hợp lệ. "#" cộng 31 ký tự: từ chối. |
| BR-M05-24 | Suy diễn | Hai Tag có cùng tên chuẩn hóa là một Tag; việc chuẩn hóa chỉ đổi chữ hoa thành chữ thường, không bỏ dấu. Mọi nơi hiển thị Tag bằng tên chuẩn hóa. | Tác giả gõ #MachineLearning, người khác gõ #machinelearning: cùng một Tag, hiển thị #machinelearning. #XácSuất và #xacsuat: hai Tag khác nhau (#xácsuất và #xacsuat). |
| BR-M05-25 | Ràng buộc | Mod và Admin không sửa, gộp hay xóa Tag; với Tag, Mod và Admin chỉ vô hiệu hóa (trong tình huống khủng hoảng) và kích hoạt lại. | — |
| BR-M05-26 | Suy diễn | Tag bị vô hiệu hóa không hiện trong gợi ý tự động khi nhập, Trending Tag và danh sách Tag; bài viết cũ giữ liên kết với Tag nhưng Tag không hiển thị trên bài; nếu người dùng nhập lại tên Tag đó, phần nhập được hiển thị như văn bản, không thành Tag. | #abc bị vô hiệu hóa; bài X có #abc: X không hiện #abc. Tác giả bài Y nhập "#abc": Y hiện "#abc" như văn bản, Y không có Tag #abc. |
| BR-M05-27 | Suy diễn | Khi Tag được kích hoạt lại, Tag hiện lại trong gợi ý tự động, Trending Tag, danh sách Tag và trên các bài viết còn liên kết với nó; phần chữ đã nhập trong thời gian Tag bị vô hiệu hóa không tự thành Tag. | Kích hoạt lại #abc: X hiện lại #abc. Y (nhập "#abc" lúc Tag bị vô hiệu hóa) vẫn hiện "#abc" như văn bản cho tới khi được sửa. |
| BR-M05-28 | Ràng buộc | Comment không có Topic hay Tag riêng; comment thuộc ngữ cảnh Topic, Tag của bài viết. | — |
| BR-M05-29 | Tính toán | Điểm Trending của một Topic hoặc Tag = tổng điểm các tương tác xảy ra trong cửa sổ 7 ngày trên các bài viết có Topic hoặc Tag đó, bất kể bài viết được đăng lúc nào: bài viết được đăng = 1, mỗi upvote cho bài = 2, mỗi comment (kể cả reply) = 1, mỗi bookmark = 1. Chỉ tính bài đang hiển thị trên feed chính. Tương tác đã bị rút lại, upvote cho comment và lượt xem không được tính. Bài viết có nhiều Topic hoặc Tag góp điểm cho tất cả. Tag bị vô hiệu hóa không có điểm Trending. | Tính lúc 07/10 10:00, cửa sổ từ 30/09 10:00. Topic Toán học: bài A đăng 05/10, có 3 upvote, 2 comment, 1 bookmark trong cửa sổ: 1 + 6 + 2 + 1 = 10. Bài B đăng 20/09: 2 upvote trong cửa sổ = 4; 1 upvote lúc 29/09 không tính; 1 comment đã bị xóa không tính. Bài C đăng 30/09 09:00 (ngay trước cửa sổ): không có điểm đăng bài; 1 comment ngày 01/10 = 1. Bài D trong nhóm Private có 20 upvote: không tính. Tổng Toán học = 15. Nếu bài A có thêm Topic Tin học, Tin học cũng nhận 10 từ bài A. |
| BR-M05-30 | Kích hoạt | Điểm Trending được tính lại định kỳ với chu kỳ từ 15 đến 30 phút; mọi tương tác có mặt trong điểm chậm nhất 30 phút sau khi xảy ra; người xem thấy kết quả của lần tính gần nhất. | Upvote lúc 10:05: điểm hiển thị lúc 10:35 phải đã có upvote này; lúc 10:20 có thể chưa có. |
| BR-M05-31 | Suy diễn | Danh sách Trending Topic và Trending Tag chỉ gồm mục có điểm lớn hơn 0, xếp theo điểm giảm dần; bằng điểm thì mục có nhiều bài mới hơn xếp trước; vẫn bằng thì xếp theo tên từ A đến Z. Mỗi mục một hạng riêng. | Ngữ văn 12 điểm (0 bài mới), Tin học 10 (2 bài mới), Hướng nghiệp 10 (1), Toán học 10 (1), Góc Chill 0: thứ tự 1 Ngữ văn, 2 Tin học, 3 Hướng nghiệp, 4 Toán học; Góc Chill không xuất hiện. |

### 5.13 Dữ liệu nghiệp vụ

| Thực thể | Thuộc tính nguồn đã nêu | Quan hệ |
|---|---|---|
| Topic | Tên (không trùng trong danh mục) | Gắn với nhiều bài viết qua Liên kết bài viết–Topic |
| Liên kết bài viết–Topic | Bài viết, Topic | Mỗi bài viết đã gửi có 1–3 liên kết, bài nháp có 0–3; thuộc một bài viết (M03) và một Topic |
| Tag | Tên chuẩn hóa (duy nhất), thời điểm tạo, trạng thái (hoạt động hoặc bị vô hiệu hóa). Không lưu người tạo. | Gắn với nhiều bài viết qua Liên kết bài viết–Tag |
| Liên kết bài viết–Tag | Bài viết, Tag | Mỗi bài viết có 0–5 liên kết; được giữ khi Tag bị vô hiệu hóa |
| Lượt gợi ý Topic | Bài viết đang soạn hoặc đang sửa, các Topic được gợi ý (tối đa 3), tình trạng lỗi thời | Thuộc một tác giả và một bài viết; sinh ra một Phản hồi gợi ý khi đủ điều kiện |
| Phản hồi gợi ý | Các Topic AI gợi ý, các Topic tác giả chọn cuối cùng | Thuộc một Lượt gợi ý Topic; được M13 dùng để đánh giá AI |
| Điểm Trending | Topic hoặc Tag, điểm, thời điểm tính | Một Topic hoặc một Tag hoạt động có một Điểm Trending ở mỗi lần tính |

**Ma trận CRUD:**

| Thực thể | Tạo | Đọc | Sửa | Xóa |
|---|---|---|---|---|
| Topic | FR-M05-06.01 (11 Topic ban đầu: BR-M05-02) | FR-M05-04.01, FR-M05-01.01 | Không có (không hỗ trợ đổi tên Topic) | FR-M05-08.01, FR-M05-07.05 |
| Liên kết bài viết–Topic | FR-M05-01.02, FR-M05-01.10 | FR-M05-04.04, M03 | FR-M05-01.06, FR-M05-07.01, FR-M05-11.01 | FR-M05-01.06, FR-M05-11.01, FR-M05-08.05; khi bài viết bị xóa: M03 |
| Tag | FR-M05-03.02 | FR-M05-04.02 | FR-M05-09.01, FR-M05-10.01 (chỉ trạng thái); tên: Không có (BR-M05-25) | Không có (BR-M05-25) |
| Liên kết bài viết–Tag | FR-M05-03.01 | FR-M05-04.04, M03 | Không có (chỉ thêm hoặc bỏ liên kết) | FR-M05-03.10, FR-M05-11.02; khi bài viết bị xóa: M03 |
| Lượt gợi ý Topic | FR-M05-02.03 | FR-M05-02.03 | FR-M05-02.09 | — |
| Phản hồi gợi ý | FR-M05-02.12 | M13 | Không có | — |
| Điểm Trending | FR-M05-05.01 | M14 | FR-M05-05.01 | Không có (được thay ở lần tính kế tiếp, BR-M05-30) |

<!-- Ô "—" ở cột Xóa của Lượt gợi ý Topic và Phản hồi gợi ý: nguồn không nói thời gian lưu; không ảnh hưởng hành vi người dùng thấy,
     nên không tạo GAP. Việc lưu giữ dữ liệu cá nhân thuộc OPEN-008. -->

### 5.14 Chuyển trạng thái

#### Tag

| Từ | Sự kiện | Điều kiện | Sang | Yêu cầu |
|---|---|---|---|---|
| (bắt đầu) | Tác giả gắn một Tag chưa tồn tại cho bài viết | Tên Tag hợp lệ (BR-M05-20, BR-M05-23) | Hoạt động | FR-M05-03.02 |
| Hoạt động | Mod hoặc Admin vô hiệu hóa Tag | Tình huống khủng hoảng | Bị vô hiệu hóa | FR-M05-09.01 |
| Bị vô hiệu hóa | Mod hoặc Admin kích hoạt lại Tag | — | Hoạt động | FR-M05-10.01 |

Tag không có trạng thái kết thúc: Tag không bị xóa (BR-M05-25).

#### Lượt gợi ý Topic

| Từ | Sự kiện | Điều kiện | Sang | Yêu cầu |
|---|---|---|---|---|
| (bắt đầu) | Tác giả bấm "Gợi ý topic" và AI trả về Topic hợp lệ | AI đang bật; tiêu đề cộng nội dung đủ 20 từ; chưa đủ 10 lần trong 60 giây gần nhất | Còn hiệu lực | FR-M05-02.03 |
| Còn hiệu lực | Tiêu đề hoặc nội dung chữ thay đổi | — | Lỗi thời | FR-M05-02.09 |
| Còn hiệu lực | Tác giả gửi bài viết hoặc lưu bản sửa | — | (kết thúc, ghi phản hồi gợi ý) | FR-M05-02.12 |
| Lỗi thời | Tác giả gửi bài viết hoặc lưu bản sửa | — | (kết thúc, không ghi phản hồi) | FR-M05-02.13 |
| Lỗi thời | Tác giả bấm gợi ý lại | Như dòng đầu | (kết thúc; một Lượt gợi ý mới bắt đầu) | FR-M05-02.10 |

### 5.15 Giao tiếp với module khác

| Hướng | Module | Nội dung ở mức nghiệp vụ | Yêu cầu |
|---|---|---|---|
| Cung cấp | M03 | Quy tắc chọn Topic (1–3, thuộc danh mục) và gắn Tag (tối đa 5, ký tự hợp lệ) khi tác giả soạn, gửi và sửa bài viết; nút "Gợi ý topic" trong trình soạn bài | FR-M05-01.02, FR-M05-03.01, FR-M05-02.01 |
| Dùng | M03 | Thao tác gửi bài, sửa bài, trạng thái nháp, hiển thị bài viết; khi bài viết bị xóa thì liên kết bài viết–Topic, bài viết–Tag đi theo bài | — |
| Cung cấp | M06 | Danh sách Topic và Tag đang hoạt động để tìm kiếm, gợi ý tự động khi nhập và lọc bài viết; Tag bị vô hiệu hóa không có trong gợi ý tự động | FR-M05-04.02, FR-M05-09.02 |
| Cung cấp | M07 | Danh mục Topic để người dùng theo dõi Topic; khi gộp Topic, người theo dõi Topic nguồn chuyển sang Topic đích; khi xóa Topic, lượt theo dõi bị bỏ | FR-M05-04.01, FR-M05-07.06, FR-M05-08.06 |
| Dùng | M10 | Công tắc AI tổng và công tắc gợi ý Topic; nhật ký thao tác của Admin ghi việc thêm, gộp, xóa Topic | FR-M05-02.16 |
| Dùng | M13 | Thực hiện gợi ý Topic (thời gian chờ, thử lại một lần), ghi kết quả thô của AI; dùng phản hồi gợi ý để đánh giá chất lượng AI | FR-M05-02.01, FR-M05-02.12 |
| Dùng | M03, M04, M12, M02 | Các tương tác dùng cho Trending: upvote bài viết, comment, bookmark, kèm thời điểm và việc rút lại | FR-M05-05.01 |
| Cung cấp | M14 | Danh sách Trending Topic và Trending Tag kèm điểm, theo thứ tự của BR-M05-31, cho tab Trending (kể cả Guest) | FR-M05-05.09, FR-M05-05.14 |
| Dùng | M08 | Nhật ký kiểm duyệt: ghi việc vô hiệu hóa, kích hoạt lại Tag và việc đổi Topic, Tag trên bài người khác | FR-M05-09.07, FR-M05-10.06, FR-M05-11.07 |
| Dùng | M01 | Trang Chính sách quyền riêng tư nêu việc tiêu đề và nội dung bài đang soạn, kể cả chưa đăng, được gửi cho dịch vụ AI bên thứ ba khi bấm "Gợi ý topic" | FR-M05-02.01 |
| Cung cấp | M15 | Liên kết bài viết–Topic để thống kê phân bố bài viết theo Topic | FR-M05-01.02 |

### 5.16 AI hỗ trợ và hành vi khi tắt AI

Module dùng AI cho một việc duy nhất: gợi ý Topic (FR-M05-02). AI không gợi ý và không gắn Tag (FR-M05-03.11).

- Khi AI được bật: FR-M05-02.01 đến FR-M05-02.15, FR-M05-02.19 đến FR-M05-02.21 (gợi ý khi bấm nút, kể cả khi tác giả sửa bài; tối đa 3 Topic chọn sẵn; gợi ý lỗi thời; ghi phản hồi; giới hạn 10 lần trong 60 giây).
- Khi AI bị tắt (công tắc tổng hoặc công tắc gợi ý Topic): FR-M05-02.16, FR-M05-02.17 — không có gợi ý, tác giả chọn Topic thủ công từ danh mục.
- Khi AI đang bật nhưng lỗi (quá thời gian chờ sau lần thử lại, lỗi, hoặc mọi Topic trả về đều ngoài danh mục): FR-M05-02.06 đến FR-M05-02.08 — báo lỗi không chặn, không tự chọn Topic.

### 5.17 Yêu cầu HMI

Chưa có — chờ giai đoạn thiết kế.

### 5.18 Chuyển màn hình

Chưa có — chờ giai đoạn thiết kế.

## 6. Lịch sử sửa đổi

| Phiên bản | Ngày | Nội dung | Người sửa |
|---|---|---|---|
| 0.1 | 2026-10-07 | Tạo mới | Phạm Văn Đức |
| 1.0 | 2026-10-07 | Chốt sau 7 bước; ghi register DEC-140–146, QA-267–291, ISS-207–231, OPEN-009 | Phạm Văn Đức |
| 1.1 | 2026-10-07 | Cập nhật Phụ lục C.2 và ghi chú, trạng thái ở C.1 theo DEC-140–146 (C.2 còn ghi trước bước 6 và công thức Trending cũ); thân tài liệu không đổi; thêm DEC-092 vào chuỗi DEC-008. Chốt bản 1.1 | Phạm Văn Đức |

## Phụ lục A. Truy vết

| ID | Nguồn | Căn cứ | Ghi chú |
|---|---|---|---|
| FR-M05-01 | DEC-047, DEC-048, DEC-049, DEC-140, DEC-141, DEC-142, QA-102, DM-3.1, DM-3.4 | Nói thẳng | Lý do lấy từ DEC-047 "used for filter/browse", DM-3.1, QA-102 |
| FR-M05-01.01 | DEC-048, DEC-049 | Nói thẳng | — |
| FR-M05-01.02 | DEC-049 | Nói thẳng | — |
| FR-M05-01.03 | DEC-049 | Suy ra | DEC-049 "Min 1 … (mandatory)" ⇒ bài không có Topic bị từ chối gửi |
| FR-M05-01.04 | DEC-049 | Suy ra | DEC-049 "max 3 topics/post" ⇒ Topic thứ tư bị từ chối |
| FR-M05-01.05 | DEC-049 | Suy ra | Bài có 1–3 Topic khác nhau (BR-M05-03) ⇒ chọn trùng không tạo Topic thứ hai |
| FR-M05-01.06 | DEC-142 | Nói thẳng | — |
| FR-M05-01.07 | DEC-049, DEC-142 | Nói thẳng | DEC-142 "within the same limits" |
| FR-M05-01.08 | QA-011 | Suy ra | QA-011 không cho Guest đăng hay tương tác ⇒ Guest không gán, đổi Topic |
| FR-M05-01.09 | DEC-049, DEC-141 | Suy ra | Topic phải thuộc danh mục (BR-M05-03) ⇒ Topic không còn trong danh mục bị từ chối |
| FR-M05-01.10 | DEC-142 | Nói thẳng | — |
| FR-M05-02 | DEC-050, DEC-140, DEC-142, DEC-144, QA-017, QA-103, DEC-008, DEC-093, DEC-099, DEC-100, DEC-132, DM-11.2, DG-6, DG-5 | Nói thẳng | Lý do lấy từ DEC-047 "AI suggest + user confirm", DG-5, QA-017 |
| FR-M05-02.01 | DEC-050 | Nói thẳng | — |
| FR-M05-02.02 | DEC-050 | Nói thẳng | — |
| FR-M05-02.03 | DEC-050, QA-103 | Nói thẳng | — |
| FR-M05-02.04 | DEC-050 | Nói thẳng | — |
| FR-M05-02.05 | DEC-050, DEC-144 | Nói thẳng | — |
| FR-M05-02.06 | DEC-132, DEC-141, DEC-144 | Nói thẳng | — |
| FR-M05-02.07 | DEC-099, DEC-132 | Nói thẳng | — |
| FR-M05-02.08 | DEC-099 | Nói thẳng | DEC-099 "no action taken" |
| FR-M05-02.09 | DEC-050 | Nói thẳng | — |
| FR-M05-02.10 | DEC-050 | Nói thẳng | — |
| FR-M05-02.11 | DEC-050 | Nói thẳng | DEC-050 "does not block publish" |
| FR-M05-02.12 | DEC-050, DEC-142, QA-017 | Nói thẳng | DEC-142: gợi ý khi sửa bài có ghi phản hồi |
| FR-M05-02.13 | DEC-050, DEC-142 | Nói thẳng | — |
| FR-M05-02.14 | DEC-050 | Suy ra | DEC-050 "picks topic manually from start → skips AI flow entirely" ⇒ không có gợi ý để so sánh |
| FR-M05-02.15 | DEC-100, DEC-144 | Suy ra | DEC-144 "sliding 60-second window" ⇒ lần thứ 11 trong 60 giây bị từ chối |
| FR-M05-02.16 | DEC-008, DEC-093, DEC-099, DM-x04 | Nói thẳng | — |
| FR-M05-02.17 | DEC-008, DEC-050, DEC-093, DEC-099 | Nói thẳng | DEC-050 "AI off → user picks from dropdown" |
| FR-M05-02.18 | QA-011 | Suy ra | QA-011 không cho Guest đăng bài ⇒ Guest không có bài để gợi ý |
| FR-M05-02.19 | DEC-144 | Nói thẳng | — |
| FR-M05-02.20 | DEC-142 | Nói thẳng | — |
| FR-M05-02.21 | DEC-142 | Nói thẳng | — |
| FR-M05-03 | DEC-047, DEC-051, DEC-143, DEC-142, QA-017, DM-3.2, DM-3.4, DG-3, DEC-140  | Nói thẳng | Lý do lấy từ DEC-047, DG-3, QA-017 |
| FR-M05-03.01 | DEC-051 | Nói thẳng | Không bắt buộc có Tag: nguồn chỉ nêu tối đa (BR-M05-22) |
| FR-M05-03.02 | DEC-051 | Nói thẳng | "Auto-created, no approval" |
| FR-M05-03.03 | DEC-051 | Suy ra | "name unique lowercase-normalized" ⇒ cùng tên chuẩn hóa là một Tag (BR-M05-24) |
| FR-M05-03.04 | DEC-051 | Suy ra | "Max 5 tags/post" ⇒ Tag thứ sáu bị từ chối |
| FR-M05-03.05 | DEC-051, DEC-143 | Suy ra | "max 30 chars/tag" và "# not counted" ⇒ tên 31 ký tự bị từ chối |
| FR-M05-03.06 | DEC-143 | Nói thẳng | — |
| FR-M05-03.07 | DEC-143 | Nói thẳng | — |
| FR-M05-03.08 | DEC-051 | Suy ra | Cùng tên chuẩn hóa là một Tag ⇒ không gắn hai lần |
| FR-M05-03.09 | DEC-051 | Nói thẳng | "NOT tagified — rendered as plain text" |
| FR-M05-03.10 | DEC-142 | Nói thẳng | — |
| FR-M05-03.11 | QA-017, DEC-140 | Nói thẳng | — |
| FR-M05-03.12 | QA-011 | Suy ra | QA-011 không cho Guest đăng hay tương tác ⇒ Guest không gắn Tag |
| FR-M05-03.13 | QA-108 | Nói thẳng | — |
| FR-M05-03.14 | DEC-143 | Nói thẳng | — |
| FR-M05-04 | QA-011, DEC-047, DEC-048, DEC-051, DEC-142, DEC-140  | Nói thẳng | Xem bài viết theo Topic/Tag thuộc bộ lọc M06 (DEC-142) |
| FR-M05-04.01 | QA-011, DEC-047, DEC-140  | Nói thẳng | — |
| FR-M05-04.02 | QA-011, DEC-051 | Nói thẳng | — |
| FR-M05-04.03 | DEC-051 | Nói thẳng | "hidden from … browse" |
| FR-M05-04.04 | QA-011, DEC-051 | Suy ra | QA-011 cho Guest "Xem AI Classification trên post" ⇒ Topic hiển thị trên bài cho mọi người; Tag chip theo DEC-051 |
| FR-M05-04.05 | DEC-051 | Nói thẳng | "tag chip hidden from display" |
| FR-M05-04.06 | DEC-048 | Nói thẳng | — |
| FR-M05-05 | DEC-052, DEC-145, QA-231 | Nói thẳng | Lý do lấy từ DEC-052 "dedicated Feed section", QA-231 "Trending Topic riêng … để xem theo chủ đề" |
| FR-M05-05.01 | DEC-145 | Nói thẳng | — |
| FR-M05-05.02 | DEC-145 | Nói thẳng | — |
| FR-M05-05.03 | DEC-052, DEC-145 | Nói thẳng | — |
| FR-M05-05.04 | DEC-145 | Nói thẳng | — |
| FR-M05-05.05 | DEC-145 | Nói thẳng | — |
| FR-M05-05.06 | DEC-145 | Nói thẳng | — |
| FR-M05-05.07 | DEC-051 | Nói thẳng | "hidden from … trending" |
| FR-M05-05.08 | DEC-145 | Nói thẳng | Xem TBD-M05-02 |
| FR-M05-05.09 | DEC-145 | Nói thẳng | — |
| FR-M05-05.10 | DEC-052, DEC-145  | Nói thẳng | "cached, not live query" |
| FR-M05-05.11 | DEC-145 | Nói thẳng | — |
| FR-M05-05.12 | DEC-145 | Nói thẳng | — |
| FR-M05-05.13 | DEC-145 | Nói thẳng | "comment (replies included)" |
| FR-M05-05.14 | DEC-145 | Nói thẳng | — |
| FR-M05-06 | DEC-141, DEC-048 | Nói thẳng | — |
| FR-M05-06.01 | DEC-141 | Nói thẳng | — |
| FR-M05-06.02 | DEC-141 | Suy ra | "Topic names are unique" ⇒ tên trùng bị từ chối |
| FR-M05-06.03 | DEC-141 | Suy ra | "Only ADMIN can add" ⇒ Guest, User, Mod bị từ chối |
| FR-M05-06.04 | DEC-141 | Nói thẳng | "validates against the current catalog" |
| FR-M05-06.05 | DEC-141 | Nói thẳng | — |
| FR-M05-06.06 | DEC-141 | Nói thẳng | — |
| FR-M05-06.07 | DEC-047, DEC-140 | Nói thẳng | DEC-047 "Flat structure (nested deferred)" |
| FR-M05-06.08 | DEC-141 | Nói thẳng | — |
| FR-M05-07 | DEC-049, DEC-141 | Nói thẳng | — |
| FR-M05-07.01 | DEC-049 | Nói thẳng | "Merge auto re-points post_topics from source to target" |
| FR-M05-07.02 | DEC-049 | Suy ra | Bài có các Topic khác nhau (BR-M05-03) ⇒ sau gộp chỉ còn một Topic đích |
| FR-M05-07.03 | DEC-141 | Suy ra | "Merge is ADMIN only" ⇒ Guest, User, Mod bị từ chối |
| FR-M05-07.04 | DEC-049 | Suy ra | Gộp là chuyển bài giữa hai Topic ⇒ gộp một Topic vào chính nó không có nghĩa |
| FR-M05-07.05 | DEC-141 | Nói thẳng | — |
| FR-M05-07.06 | DEC-141 | Nói thẳng | — |
| FR-M05-08 | DEC-141 | Nói thẳng | — |
| FR-M05-08.01 | DEC-141, DEC-129 | Nói thẳng | Nhất quán DEC-129: chỉ xóa cứng khi không còn dữ liệu tham chiếu |
| FR-M05-08.02 | DEC-141 | Suy ra | "only when the Topic has no non-draft post" ⇒ Topic có bài không phải nháp bị từ chối xóa |
| FR-M05-08.03 | DEC-141 | Suy ra | "Delete is ADMIN only" ⇒ Guest, User, Mod bị từ chối |
| FR-M05-08.04 | DEC-141, DEC-132 | Suy ra | Topic phải thuộc danh mục hiện tại ⇒ Topic đã xóa không chọn được |
| FR-M05-08.05 | DEC-141 | Nói thẳng | — |
| FR-M05-08.06 | DEC-141 | Nói thẳng | — |
| FR-M05-09 | DEC-051, DEC-090, DEC-146 | Nói thẳng | — |
| FR-M05-09.01 | DEC-051, DEC-090 | Nói thẳng | "Crisis case: mod/admin soft-delete" |
| FR-M05-09.02 | DEC-051 | Nói thẳng | "hidden from autocomplete" |
| FR-M05-09.03 | DEC-051 | Nói thẳng | "old posts keep post_tags record" |
| FR-M05-09.04 | DEC-051, DEC-090 | Suy ra | "mod/admin soft-delete" ⇒ Guest, User bị từ chối |
| FR-M05-09.05 | DEC-051 | Suy ra | Thao tác lặp ⇒ không đổi trạng thái |
| FR-M05-09.06 | DEC-051 | Nói thẳng | "mod/admin do NOT edit/merge/delete" |
| FR-M05-09.07 | DEC-146, DEC-081 | Nói thẳng | — |
| FR-M05-10 | DEC-143 | Nói thẳng | — |
| FR-M05-10.01 | DEC-143 | Nói thẳng | — |
| FR-M05-10.02 | DEC-143 | Nói thẳng | — |
| FR-M05-10.03 | DEC-143 | Nói thẳng | — |
| FR-M05-10.04 | DEC-143 | Suy ra | "MOD and ADMIN may re-activate" ⇒ Guest, User bị từ chối |
| FR-M05-10.05 | DEC-051 | Suy ra | Thao tác lặp ⇒ không đổi trạng thái |
| FR-M05-10.06 | DEC-146, DEC-081 | Nói thẳng | — |
| FR-M05-11 | DEC-142, DEC-146 | Nói thẳng | — |
| FR-M05-11.01 | DEC-142 | Nói thẳng | — |
| FR-M05-11.02 | DEC-142 | Nói thẳng | — |
| FR-M05-11.03 | DEC-142 | Nói thẳng | "within the same limits" |
| FR-M05-11.04 | DEC-142 | Suy ra | Chỉ tác giả, Mod, Admin được đổi ⇒ User khác và Guest bị từ chối |
| FR-M05-11.05 | DEC-142 | Nói thẳng | — |
| FR-M05-11.06 | DEC-142, DEC-037 | Nói thẳng | — |
| FR-M05-11.07 | DEC-146, DEC-081 | Nói thẳng | — |
| BR-M05-01 | DEC-047, DEC-140 | Nói thẳng | — |
| BR-M05-02 | DEC-048 | Nói thẳng | — |
| BR-M05-03 | DEC-049, DEC-048, DEC-142 | Nói thẳng | "Các Topic khác nhau" suy ra từ ý chọn 1–3 Topic trong danh mục |
| BR-M05-04 | DEC-049, DEC-051, DEC-142 | Nói thẳng | — |
| BR-M05-05 | DEC-141 | Nói thẳng | — |
| BR-M05-06 | DEC-141 | Nói thẳng | — |
| BR-M05-07 | DEC-141 | Nói thẳng | — |
| BR-M05-08 | DEC-141 | Nói thẳng | — |
| BR-M05-09 | DEC-049, DEC-141 | Nói thẳng | — |
| BR-M05-10 | DEC-050, DEC-142, QA-017 | Nói thẳng | — |
| BR-M05-11 | DEC-050 | Nói thẳng | — |
| BR-M05-12 | DEC-050, DEC-144 | Nói thẳng | — |
| BR-M05-13 | DEC-050, QA-103 | Nói thẳng | — |
| BR-M05-14 | DEC-132, DEC-141, DEC-144 | Nói thẳng | — |
| BR-M05-15 | DEC-050 | Nói thẳng | "Content changed" hiểu là tiêu đề hoặc nội dung chữ, vì gợi ý chỉ dựa trên hai phần này (BR-M05-11) |
| BR-M05-16 | DEC-050, QA-017 | Nói thẳng | — |
| BR-M05-17 | DEC-100, DEC-144 | Nói thẳng | — |
| BR-M05-18 | DEC-008, DEC-093, DEC-099 | Nói thẳng | — |
| BR-M05-19 | DEC-099, DEC-132 | Nói thẳng | — |
| BR-M05-20 | DEC-047, DEC-143, DEC-140  | Nói thẳng | — |
| BR-M05-21 | DEC-051 | Nói thẳng | — |
| BR-M05-22 | DEC-051 | Nói thẳng | "Không bắt buộc có Tag" suy ra: nguồn chỉ nêu giới hạn tối đa, không nêu tối thiểu |
| BR-M05-23 | DEC-051, DEC-143 | Nói thẳng | — |
| BR-M05-24 | DEC-051, DEC-143 | Nói thẳng | Không bỏ dấu: nguồn chỉ nói "lowercase-normalized" |
| BR-M05-25 | DEC-051, DEC-090, DEC-143 | Nói thẳng | — |
| BR-M05-26 | DEC-051 | Nói thẳng | — |
| BR-M05-27 | DEC-143 | Nói thẳng | — |
| BR-M05-28 | QA-108 | Nói thẳng | — |
| BR-M05-29 | DEC-145, DEC-051 | Nói thẳng | "Tag bị vô hiệu hóa không có điểm" từ DEC-051, DEC-145 |
| BR-M05-30 | DEC-052, DEC-145 | Nói thẳng | — |
| BR-M05-31 | DEC-145 | Nói thẳng | — |

## Phụ lục B. Câu hỏi, giả định và TBD

### B.1 Câu hỏi đã hỏi

| Mã | Loại | Câu hỏi | Trả lời | Ghi vào register |
|---|---|---|---|---|
| Q-01 | Mâu thuẫn | AI có gợi ý Tag không? Draft (DM-11.2, DG-6, GL:AI Classification) nói có; QA-017 nói Tag do người dùng tự quyết hoàn toàn. | Xác nhận: AI không gợi ý Tag, chỉ gợi ý Topic. | QA-267, DEC-140 |
| Q-02 | Mâu thuẫn | Có bước Mod duyệt kết quả AI Classification không? Draft nói "User / Moderator review"; DEC-050 chỉ có người dùng tự chỉnh rồi đăng. | Xác nhận: không có bước Mod duyệt. | QA-268, DEC-140 |
| Q-03 | Mâu thuẫn | Topic phẳng hay 2 tầng Category → Topic? QA-033 nói 2 tầng; DEC-047 chốt phẳng. | Xác nhận: Topic phẳng, không chia 2 tầng. | QA-269, DEC-140 |
| Q-04 | Thiếu chi tiết | Stakeholder yêu cầu cho thêm Topic mới (thay đổi DEC-048 "11, final"). Cần chốt: ai được thêm; quyền đổi tên/gộp; có cho xóa Topic không; tên trùng; AI gợi ý theo danh mục nào; bài cũ có tự gán Topic mới không; danh mục có trần số lượng không. | (1) Chỉ Admin được thêm Topic. (2) Gộp Topic chỉ Admin (thay phần "dùng chung với Mod" của DEC-090); không hỗ trợ đổi tên Topic (xem Q-06). Xóa mềm Tag khi khủng hoảng vẫn dùng chung Mod và Admin. (3) Admin được xóa Topic, chỉ khi Topic chưa có bài nào. (4) Tên Topic không được trùng. (5) AI gợi ý dựa trên toàn bộ danh mục Topic hiện tại. (6) Bài cũ không tự được gán Topic mới. (7) Danh mục Topic không giới hạn số lượng. | QA-270, DEC-141 |
| Q-05 | Thiếu chi tiết | Stakeholder yêu cầu đổi công thức Trending Topic/Tag (thay đổi DEC-052). Cần chốt: cửa sổ tính theo bài hay theo tương tác; có decay không; tiêu chí và trọng số mới; lượt xem; Trending Post có đổi theo không. | (1) Điểm của Topic/Tag = tổng tương tác xảy ra trong 7 ngày gần nhất trên các bài thuộc Topic/Tag đó, bất kể bài đăng lúc nào. (2) Bài được đăng trong 7 ngày đó được +1. (3) Tương tác đã rút lại (bỏ upvote, xóa comment, bỏ bookmark) không tính. (4) Bài có nhiều Topic/Tag góp điểm cho tất cả. (5) Không decay. (6) Trọng số: đăng bài 1, upvote 2, comment 1, bookmark 1. (7) Chưa thêm lượt xem ở MS1. (8) Trending Post (M14) có thêm bookmark không: tạo OPEN mới, hướng đang được chấp nhận là thêm bookmark với cùng trọng số, review ở M14. | QA-271, DEC-145, OPEN-009 |
| Q-06 | Cần cân nhắc | Có nên giữ quyền đổi tên Topic (Admin) không? Stakeholder nêu ra để trao đổi. | Không hỗ trợ đổi tên Topic. Muốn sửa tên thì Admin thêm Topic mới, gộp Topic cũ vào, rồi xóa Topic cũ (khi đã không còn bài). | QA-272, DEC-141 |
| Q-07 | Thiếu chi tiết | DEC-049 bắt buộc mỗi bài 1–3 Topic, DEC-051 giới hạn 5 Tag; M03 có sửa bài kèm lịch sử sửa (DEC-037). Khi tác giả sửa bài viết đã gửi, có được đổi Topic, Tag không? | Có. Tác giả đổi được Topic, Tag của bài mình; Mod và Admin cũng đổi được (xem Q-08). | QA-273, DEC-142 |
| Q-08 | Thiếu chi tiết | DEC-090 cho Mod/Admin quyền với danh mục Topic và xóa mềm Tag, nhưng không nói về Topic, Tag trên từng bài. Mod, Admin có được đổi Topic, Tag trên bài viết của người khác (ví dụ bài gắn sai Topic) không? | Có (trả lời cùng Q-07). | QA-274, DEC-142 |
| Q-09 | Thiếu chi tiết | DEC-047 nói Topic "used for filter/browse", DEC-051 nói Tag bị vô hiệu hóa ẩn khỏi "browse", QA-011 cho Guest "xem danh sách Topic / Tag". "Browse" chỉ là xem danh sách Topic/Tag, hay gồm cả trang liệt kê bài viết theo một Topic hoặc Tag? | Chỉ xem danh sách Topic/Tag ở M05; xem bài viết theo Topic/Tag qua bộ lọc của M06. | QA-275, DEC-142 |
| Q-10 | Cần cân nhắc | DEC-051 cho Mod/Admin vô hiệu hóa Tag nhưng không nói có kích hoạt lại được không; nếu không thì Tag vô hiệu hóa nhầm không có cách khôi phục. | Mod và Admin được kích hoạt lại Tag đã vô hiệu hóa. | QA-276, DEC-143 |
| Q-11 | Mơ hồ | DEC-049 bắt buộc 1–3 Topic; M03 có trạng thái nháp (DEC-031). Bài viết lưu nháp (chưa gửi) có bắt buộc đủ 1–3 Topic không? | A: chỉ bắt buộc 1–3 Topic khi gửi bài; bài nháp được có 0 Topic (vẫn tối đa 3 Topic, 5 Tag). | QA-277, DEC-142 |
| Q-12 | Mơ hồ | Q-04 (4) chốt tên Topic không trùng. "Trùng" so sánh thế nào: "Tin học" và "tin học", "Tin hoc", "Tin  học" (hai khoảng trắng) có bị coi là trùng không? | Đồng ý đề xuất: so trùng không phân biệt hoa/thường, bỏ khoảng trắng thừa (đầu, cuối, giữa); khác dấu là khác tên. | QA-278, DEC-141 |
| Q-13 | Mơ hồ | Q-04 (3) chỉ cho xóa Topic chưa có bài viết. Bài nháp, bài đã xóa còn trong 7 ngày khôi phục (DEC-038), bài bị ẩn, bị từ chối có được tính là "có bài viết" không? | Đếm mọi bài không phải nháp (chờ duyệt, đã đăng, tự ẩn, bị từ chối, đã xóa còn trong 7 ngày khôi phục). Bài nháp không được đếm; khi Topic bị xóa, bài nháp có Topic đó mất Topic này (nháp được có 0 Topic theo Q-11). | QA-279, DEC-141 |
| Q-14 | Thiếu chi tiết | DEC-049 chỉ nói gộp chuyển bài sang Topic đích. Sau khi gộp, Topic nguồn còn trong danh mục không (Q-06 mô tả Admin xóa Topic cũ sau khi gộp)? Người đang theo dõi Topic nguồn (M07) có được chuyển sang Topic đích không? | (a) Topic nguồn tự bị xóa khỏi danh mục sau khi gộp. (b) Người đang follow Topic nguồn tự chuyển sang follow Topic đích (ai đã follow Topic đích thì giữ nguyên). Kèm: khi Admin xóa một Topic, các lượt follow Topic đó bị bỏ. | QA-280, DEC-141 |
| Q-15 | Mơ hồ | DEC-050: nội dung dưới 20 từ thì không gợi ý. 20 từ đếm trên nội dung chữ hay cả tiêu đề? "Từ" đếm theo khoảng trắng (mỗi âm tiết tiếng Việt là một từ) hay cách khác? | A: giữ ngưỡng 20 từ, đếm trên tiêu đề cộng nội dung chữ; mỗi cụm ký tự cách nhau bởi khoảng trắng là một từ. | QA-281, DEC-144 |
| Q-16 | Mơ hồ | DEC-132: kết quả ngoài danh mục là gợi ý thất bại. Nếu AI trả về 3 Topic mà chỉ 1 Topic ngoài danh mục, bỏ Topic sai và giữ 2 Topic đúng, hay coi cả lần gợi ý thất bại? | Đồng ý đề xuất: bỏ Topic ngoài danh mục, giữ Topic hợp lệ; chỉ khi không còn Topic hợp lệ nào mới coi là gợi ý thất bại. | QA-282, DEC-144 |
| Q-17 | Mơ hồ | DEC-100: 10 lần/phút/người dùng. Tính theo phút đồng hồ (10:00:00–10:00:59) hay 60 giây gần nhất? | Đồng ý đề xuất: tính theo 60 giây gần nhất. | QA-283, DEC-144 |
| Q-18 | Mơ hồ | DEC-051: Tag tối đa 30 ký tự, tên chuẩn hóa chữ thường. Dấu "#" có tính vào 30 ký tự không? Tag hiển thị theo chữ tác giả nhập (#XácSuất) hay chữ thường (#xácsuất)? Tag được chứa ký tự nào (chữ có dấu, số, gạch dưới, ký tự đặc biệt)? | Hiển thị chung theo tên chuẩn hóa chữ thường ở mọi nơi; dấu "#" chỉ để hiển thị, không tính vào 30 ký tự. Tập ký tự: chữ cái (kể cả có dấu), chữ số, "_", có ít nhất một chữ cái. | QA-284, DEC-143 |
| Q-19 | Thiếu chi tiết | Q-05 chốt công thức Trending. Những bài viết và tương tác nào được tính: bài trong nhóm riêng tư (M11), bài đang chờ duyệt hoặc bị ẩn, reply của comment, upvote cho comment? | A: chỉ tính bài đang hiển thị trên feed chính (đã đăng, không bị Mod ẩn; gồm bài nhóm Public, không gồm nhóm Private); upvote chỉ tính upvote cho bài; comment gồm cả reply; bài không còn hiển thị không đóng góp điểm. | QA-285, DEC-145 |
| Q-20 | Mơ hồ | DEC-052: tính lại mỗi 15–30 phút. Để kiểm chứng được, yêu cầu là "điểm hiển thị không cũ hơn 30 phút" hay một chu kỳ cố định? | A: mọi tương tác phải có mặt trong điểm Trending chậm nhất 30 phút sau khi xảy ra; chu kỳ tính lại do đội phát triển chọn trong khoảng 15–30 phút. | QA-286, DEC-145 |
| Q-21 | Thiếu chi tiết | Nguồn không nói thứ tự khi bằng điểm, và Topic/Tag có điểm 0 có xuất hiện trong Trending không (QA-235 chỉ nói không đặt ngưỡng tối thiểu). | Chỉ hiện Topic/Tag có điểm lớn hơn 0. Thứ tự: điểm Trending giảm dần; bằng điểm thì số bài mới (bài được đăng trong cửa sổ 7 ngày) nhiều hơn xếp trước; vẫn bằng thì theo tên A–Z. Mỗi mục một hạng riêng (tên không trùng nên không có cùng hạng). | QA-287, DEC-145 |
| Q-22 | Thiếu chi tiết | Q-07 cho đổi Topic khi sửa bài viết đã gửi. Lúc sửa bài, tác giả có dùng được nút gợi ý Topic không? | A: tác giả dùng được gợi ý Topic khi sửa bài đã gửi, cùng quy tắc như lúc soạn, có ghi phản hồi; Mod/Admin đổi Topic trên bài người khác không dùng gợi ý. | QA-288, DEC-142 |
| Q-23 | Thiếu chi tiết | Q-07, Q-08 cho Mod/Admin đổi Topic, Tag trên bài người khác. Khi đó tác giả có được thông báo không (M07), và thay đổi có được ghi vào lịch sử sửa bài công khai (DEC-037) không? | Không gửi thông báo cho tác giả; không ghi thay đổi Topic, Tag vào lịch sử sửa bài. | QA-289, DEC-142 |

### B.2 TBD

| ID | Nội dung | Ảnh hưởng | Lý do chưa chốt |
|---|---|---|---|
| TBD-M05-01 | Trang công khai có Topic/Tag (danh sách, Trending Topic/Tag cho Guest) chưa được tối ưu để công cụ tìm kiếm index và hiển thị xem trước khi chia sẻ link. | Thấp | OPEN-006 hoãn có chủ đích (không làm SSR/SEO ở MS1) |
| TBD-M05-02 | Lượt xem chưa là tiêu chí tính Trending Topic/Tag ở MS1. | Thấp | DEC-145 hoãn: cần hạ tầng ghi sự kiện, đang hoãn có chủ đích ở OPEN-005 |

### B.3 Cần cân nhắc (ngoài dữ liệu hiện có)

| Mã | Điểm cần cân nhắc | Vì sao cần | Quyết định |
|---|---|---|---|
| CC-01 | Ghi nhật ký khi Mod vô hiệu hóa hoặc kích hoạt lại Tag, và khi Mod đổi Topic, Tag trên bài người khác. | Chạm tới quyền: đây là thao tác của Mod lên dữ liệu chung hoặc bài của người khác. Thao tác Admin đã được ghi (nhật ký Admin, M10), nhưng nhật ký kiểm duyệt (M08) chỉ liệt kê warn, ban, hide, resolve. | Chấp nhận: ghi vào nhật ký kiểm duyệt — QA-290, DEC-146 |
| CC-02 | Trang Chính sách quyền riêng tư nêu thêm rằng tiêu đề và nội dung bài viết được gửi cho dịch vụ AI bên thứ ba khi tác giả bấm "Gợi ý topic". | Chạm tới an toàn dữ liệu: trang công bố hiện chỉ nêu Moderation và Embedding, trong khi gợi ý Topic cũng gửi nội dung bài (của học sinh, có thể chưa đủ 18 tuổi) ra ngoài. | Chấp nhận: bổ sung trang Chính sách quyền riêng tư — QA-291, DEC-146 |

## Phụ lục C. Sổ nguồn

**Owner keywords:** M05, topic, chủ đề, tag, hashtag, trending, is_stale, gợi ý topic, topic suggestion, post_topics, post_tags, tagif, merge topic, phân loại, classification
**Dependency keywords:** post, bài viết, search, notification, feed, follow, AI_ENABLED, AI off, moderation, timezone, grade_level, Lớp/Khối, audit log
**Mục draft của module:** DM-3 (gồm DM-3.1–3.4), DM-7.2, DM-11.2
**Loại khỏi bảng nguồn (khớp nhầm):** QA-005, QA-006 (mục tiêu kinh doanh, "chủ đề" theo nghĩa chung), DM-10.1 (lý do report "Off-topic"), ISS-190, QA-249 ("tag" nội dung theo ngôn ngữ, i18n)

### C.1 Bảng nguồn

| Nguồn | Nhãn | Trạng thái | Dùng ở | Ghi chú |
|---|---|---|---|---|
| DEC-047 | Sở hữu | Hiện hành | FR-M05-01, FR-M05-03, FR-M05-04, FR-M05-04.01, FR-M05-06.07, BR-M05-01, BR-M05-20 | Nhóm A |
| DEC-048 | Sở hữu | Sửa một phần bởi DEC-141 | FR-M05-01, FR-M05-01.01, FR-M05-04, FR-M05-04.06, FR-M05-06, BR-M05-02, BR-M05-03 | Nhóm A |
| DEC-049 | Sở hữu | Sửa một phần bởi DEC-141, DEC-142 | FR-M05-01, FR-M05-01.01, FR-M05-01.02, FR-M05-01.03, FR-M05-01.04, FR-M05-01.05, FR-M05-01.07, FR-M05-01.09, FR-M05-07, FR-M05-07.01, FR-M05-07.02, FR-M05-07.04, BR-M05-03, BR-M05-04, BR-M05-09 | Nhóm A |
| DEC-050 | Sở hữu | Sửa một phần bởi DEC-142, DEC-144 | FR-M05-02, FR-M05-02.01, FR-M05-02.02, FR-M05-02.03, FR-M05-02.04, FR-M05-02.05, FR-M05-02.09, FR-M05-02.10, FR-M05-02.11, FR-M05-02.12, FR-M05-02.13, FR-M05-02.14, FR-M05-02.17, BR-M05-10, BR-M05-11, BR-M05-12, BR-M05-13, BR-M05-15, BR-M05-16 | Nhóm A |
| DEC-051 | Sở hữu | Sửa một phần bởi DEC-143, DEC-146 | FR-M05-03, FR-M05-03.01, FR-M05-03.02, FR-M05-03.03, FR-M05-03.04, FR-M05-03.05, FR-M05-03.08, FR-M05-03.09, FR-M05-04, FR-M05-04.02, FR-M05-04.03, FR-M05-04.04, FR-M05-04.05, FR-M05-05.07, FR-M05-09, FR-M05-09.01, FR-M05-09.02, FR-M05-09.03, FR-M05-09.04, FR-M05-09.05, FR-M05-09.06, FR-M05-10.05, BR-M05-04, BR-M05-21, BR-M05-22, BR-M05-23, BR-M05-24, BR-M05-25, BR-M05-26, BR-M05-29 | Nhóm A |
| DEC-052 | Sở hữu | Sửa một phần bởi DEC-145 | FR-M05-05, FR-M05-05.03, FR-M05-05.10, BR-M05-30 | Nhóm A. Phần tính điểm; hiển thị ở M14 |
| DM-11.2 | Sở hữu | Sửa một phần bởi QA-017, DEC-050, DEC-140 | FR-M05-02 | Nhóm A. Draft; ý "AI gợi ý cả Tag" và "Mod review" bị thay |
| DM-3 | Nhắc tới | Hiện hành | Không áp dụng: Chỉ là tiêu đề mục draft | Nhóm A. Chỉ là tiêu đề mục draft |
| DM-3.1 | Sở hữu | Sửa một phần bởi DEC-048 | FR-M05-01 | Nhóm A. Draft; danh sách topic gợi ý ban đầu |
| DM-3.2 | Sở hữu | Sửa một phần bởi DEC-051 | FR-M05-03 | Nhóm A. Draft; ý "không giới hạn số Tag" bị thay bởi DEC-051 |
| DM-3.3 | Phụ thuộc | Hiện hành | Chuyển M03 | Nhóm A. Lớp/Khối thuộc M03 (F-POST-09) và M02 |
| DM-3.4 | Sở hữu | Sửa một phần bởi DEC-049 | FR-M05-01, FR-M05-03 | Nhóm A. Draft; quan hệ Post–Topic–Tag |
| DM-7.2 | Sở hữu | Bị thay bởi DEC-052, DEC-145 | — | Nhóm A. Draft mục Discovery; tiêu chí Trending bị thay |
| ISS-079 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-047 | Nhóm A. Đã có DEC-047 |
| ISS-080 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-048 | Nhóm A. Đã có DEC-048 |
| ISS-081 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-050 | Nhóm A. Đã có DEC-050 |
| ISS-082 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-051, DEC-052 | Nhóm A. Đã có DEC-051, DEC-052 |
| ISS-083 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-049 | Nhóm A. Đã có DEC-049 |
| ISS-084 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-049, DEC-051 | Nhóm A. Đã có DEC-049, DEC-051 |
| QA-101 | Sở hữu | Trùng với DEC-047 | — | Nhóm A |
| QA-102 | Sở hữu | Hiện hành | FR-M05-01 | Nhóm A. Cùng nội dung DEC-047/048, thêm lý do nhóm theo chương trình 2018 — giữ Hiện hành |
| QA-103 | Sở hữu | Hiện hành | FR-M05-02, FR-M05-02.03, BR-M05-13 | Nhóm A. Cùng nội dung DEC-050, thêm lý do khớp trần 3 Topic/bài — giữ Hiện hành |
| QA-104 | Sở hữu | Trùng với DEC-050 | — | Nhóm A |
| QA-105 | Sở hữu | Trùng với DEC-051 | — | Nhóm A |
| QA-106 | Sở hữu | Trùng với DEC-052 | — | Nhóm A |
| QA-107 | Sở hữu | Trùng với DEC-051 | — | Nhóm A. Có ý "tên Tag bị khóa thành tên dành riêng". Phần Topic trùng DEC-049 |
| QA-108 | Sở hữu | Hiện hành | FR-M05-03.13, BR-M05-28 | Nhóm A. Comment không có Topic/Tag |
| MR-M05 | Sở hữu | Sửa một phần bởi DEC-141, DEC-145 | Mục 4.5 | Nhóm A. Cột MoSCoW lệch; ưu tiên lấy từ bảng MoSCoW Summary. Tóm tắt DEC-047–052 |
| DEC-008 | Sở hữu | Sửa một phần bởi DEC-093 | FR-M05-02, FR-M05-02.16, FR-M05-02.17, BR-M05-18 | Nhóm B. Phần fallback M05 khi tắt AI |
| DEC-053 | Phụ thuộc | Hiện hành | Chuyển M06 | Nhóm B. M06: tìm Tag/Topic |
| DEC-054 | Nhắc tới | Hiện hành | Không áp dụng: M06: cách kích hoạt tìm kiếm | Nhóm B. M06: cách kích hoạt tìm kiếm |
| DEC-056 | Phụ thuộc | Hiện hành | Chuyển M06 | Nhóm B. M06: lọc bài theo Topic/Tag |
| DEC-057 | Nhắc tới | Hiện hành | Không áp dụng: M06: kỹ thuật tìm kiếm | Nhóm B. M06: kỹ thuật tìm kiếm |
| DEC-058 | Phụ thuộc | Hiện hành | Chuyển M06 | Nhóm B. M06: autocomplete có Tag/Topic |
| DEC-060 | Nhắc tới | Hiện hành | Không áp dụng: M06: hiển thị kết quả | Nhóm B. M06: hiển thị kết quả |
| DEC-090 | Sở hữu | Sửa một phần bởi DEC-141 | FR-M05-09, FR-M05-09.01, FR-M05-09.04, BR-M05-25 | Nhóm B. Phần Mod dùng chung: sửa/gộp Topic, xóa mềm Tag |
| DEC-093 | Phụ thuộc | Hiện hành | FR-M05-02, FR-M05-02.16, FR-M05-02.17, BR-M05-18 | Nhóm B. M10: công tắc AI riêng cho Topic suggestion |
| DEC-095 | Nhắc tới | Hiện hành | Không áp dụng: M13: chỉ so sánh với mẫu is_stale | Nhóm B. M13: chỉ so sánh với mẫu is_stale |
| DEC-096 | Phụ thuộc | Hiện hành | Chuyển M13 | Nhóm B. M13: mô hình gợi ý topic (chi tiết công nghệ) |
| DEC-099 | Sở hữu | Hiện hành | FR-M05-02, FR-M05-02.07, FR-M05-02.08, FR-M05-02.16, FR-M05-02.17, BR-M05-18, BR-M05-19 | Nhóm B. Phần gợi ý topic khi AI tắt/lỗi; timeout và retry thuộc M13 |
| DEC-100 | Sở hữu | Sửa một phần bởi DEC-144 | FR-M05-02, FR-M05-02.15, BR-M05-17 | Nhóm B. Giới hạn 10 lần/phút/user cho nút gợi ý topic |
| DEC-124 | Nhắc tới | Hiện hành | Không áp dụng: M14: xác nhận DEC-052 giữ nguyên | Nhóm B. M14: xác nhận DEC-052 giữ nguyên |
| DEC-125 | Phụ thuộc | Hiện hành | Chuyển M14 | Nhóm B. M14: tab Trending có sub-view Topic/Tag |
| DEC-126 | Phụ thuộc | Hiện hành | Chuyển M14 | Nhóm B. M14: Guest xem Trending Topic/Tag |
| DEC-132 | Sở hữu | Sửa một phần bởi DEC-141, DEC-144 | FR-M05-02, FR-M05-02.06, FR-M05-02.07, FR-M05-08.04, BR-M05-14, BR-M05-19 | Nhóm B. Kết quả gợi ý ngoài 11 topic |
| DEC-133 | Phụ thuộc | Hiện hành | Chuyển M13 | Nhóm B. M13: ghi log đầu ra AI |
| DEC-137 | Nhắc tới | Hiện hành | Không áp dụng: Tech stack | Nhóm B. Tech stack |
| DEC-139 | Nhắc tới | Sửa một phần bởi QA-266 | Không áp dụng: Cách viết tài liệu; đã phản ánh trong mẫu | Nhóm B. Cách viết tài liệu; đã phản ánh trong mẫu |
| DG-3 | Sở hữu | Sửa một phần bởi DEC-048 | FR-M05-03, Mục 2.1 | Nhóm B. Draft; ba trục phân loại |
| DG-4 | Nhắc tới | Hiện hành | Không áp dụng: Bản đồ module | Nhóm B. Bản đồ module |
| DG-5 | Phụ thuộc | Hiện hành | FR-M05-02 | Nhóm B. Nguyên tắc: AI chỉ gợi ý, người quyết định |
| DG-6 | Sở hữu | Sửa một phần bởi QA-017, DEC-050, DEC-140 | FR-M05-02 | Nhóm B. Draft; ý "AI gợi ý Topic/Tag, User/Mod review" bị thay |
| DM-11.5 | Phụ thuộc | Hiện hành | Chuyển M13 | Nhóm B. M13: vòng phản hồi đánh giá AI |
| DM-13 | Nhắc tới | Hiện hành | Không áp dụng: Sơ đồ kiến trúc | Nhóm B. Sơ đồ kiến trúc |
| DM-2.1 | Phụ thuộc | Sửa một phần bởi DEC-049 | Chuyển M03 | Nhóm B. M03: Post có Tags, Topic |
| DM-2.4 | Nhắc tới | Hiện hành | Không áp dụng: "Tag/Topic là đủ" thay Post Type | Nhóm B. "Tag/Topic là đủ" thay Post Type |
| DM-4.5 | Phụ thuộc | Sửa một phần bởi QA-043 | Chuyển M07 | Nhóm B. M07: Follow Topic/Tag; Tag và Group bị bỏ khỏi đối tượng theo dõi (QA-043) |
| DM-7.1 | Nhắc tới | Bị thay bởi DEC-125 | — | Nhóm B. Danh sách feed cũ, M14 đã thay |
| DM-7.3 | Phụ thuộc | Hiện hành | Chuyển M06 | Nhóm B. M06: tìm theo Topic/Tag |
| DM-7.4 | Phụ thuộc | Hiện hành | Chuyển M06 | Nhóm B. M06: lọc theo Topic/Tag |
| DM-8.1 | Phụ thuộc | Sửa một phần bởi QA-043 | Chuyển M07 | Nhóm B. M07: thông báo nội dung mới trong topic/tag đang follow |
| DM-x02 | Nhắc tới | Hiện hành | Không áp dụng: Danh sách phạm vi dự án | Nhóm B. Danh sách phạm vi dự án |
| DM-x04 | Phụ thuộc | Hiện hành | FR-M05-02.16 | Nhóm B. Nguyên tắc AI: không phụ thuộc cứng, có fallback |
| GL:AI Classification | Sở hữu | Sửa một phần bởi QA-017, DEC-050, DEC-140 | Mục 2.1 | Nhóm B. Định nghĩa nói gợi ý cả Tags — đối chiếu QA-017 |
| GL:Lớp/Khối | Phụ thuộc | Hiện hành | Chuyển M03 | Nhóm B. M03/M02 |
| GL:Tag | Sở hữu | Sửa một phần bởi DEC-143 | Mục 2.1 | Nhóm B |
| GL:Topic | Sở hữu | Sửa một phần bởi DEC-048, DEC-141 | Mục 2.1 | Nhóm B. "List to be finalized" — đã có DEC-048 |
| ISS-046 | Nhắc tới | Hiện hành | Không áp dụng: Đã có QA-033, QA-034 | Nhóm B. Đã có QA-033, QA-034 |
| ISS-051 | Nhắc tới | Hiện hành | Không áp dụng: Đã có QA-043 | Nhóm B. Đã có QA-043 |
| ISS-085 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-053 | Nhóm B. Đã có DEC-053 |
| ISS-086 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-054 | Nhóm B. Đã có DEC-054 |
| ISS-088 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-056 | Nhóm B. Đã có DEC-056 |
| ISS-090 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-058 | Nhóm B. Đã có DEC-058 |
| ISS-093 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-060 | Nhóm B. Đã có DEC-060 |
| ISS-119 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-090 | Nhóm B. Đã có DEC-090 |
| ISS-122 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-093 | Nhóm B. Đã có DEC-093 |
| ISS-125 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-096 | Nhóm B. Đã có DEC-096 |
| ISS-129 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-100 | Nhóm B. Đã có DEC-100 |
| ISS-166 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-126 | Nhóm B. Đã có DEC-126 |
| ISS-168 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-125 | Nhóm B. Đã có DEC-125 |
| ISS-169 | Nhắc tới | Hiện hành | Không áp dụng: Đã có QA-228 | Nhóm B. Đã có QA-228 |
| ISS-171 | Nhắc tới | Bị thay bởi ISS-185 | — | Nhóm B. Đã có ISS-185, DEC-124 |
| ISS-172 | Nhắc tới | Hiện hành | Không áp dụng: Trending Post (M14) | Nhóm B. Trending Post (M14) |
| ISS-173 | Nhắc tới | Hiện hành | Không áp dụng: Trending Post (M14) | Nhóm B. Trending Post (M14) |
| ISS-175 | Nhắc tới | Hiện hành | Không áp dụng: Đã có QA-235 | Nhóm B. Đã có QA-235 |
| ISS-176 | Nhắc tới | Hiện hành | Không áp dụng: Đã có QA-236 | Nhóm B. Đã có QA-236 |
| ISS-177 | Nhắc tới | Hiện hành | Không áp dụng: Đã có QA-237 | Nhóm B. Đã có QA-237 |
| ISS-180 | Nhắc tới | Hiện hành | Không áp dụng: Đã có QA-243 | Nhóm B. Đã có QA-243 |
| ISS-185 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-124 | Nhóm B. Đã có DEC-124 |
| ISS-186 | Nhắc tới | Hiện hành | Không áp dụng: Đã có QA-240 | Nhóm B. Đã có QA-240 |
| ISS-194 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-132 | Nhóm B. Đã có DEC-132 |
| ISS-195 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-133 | Nhóm B. Đã có DEC-133 |
| ISS-205 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-139 | Nhóm B. Đã có DEC-139 |
| ISS-REWD-01 | Nhắc tới | Hiện hành | Không áp dụng: M12; không có badge theo chủ đề | Nhóm B. M12; không có badge theo chủ đề |
| OPEN-006 | Nhắc tới | Hiện hành | TBD-M05-01 | Nhóm B. SSR/SEO hoãn; không phải hành vi chức năng |
| OPEN-008 | Nhắc tới | Hiện hành | Không áp dụng: Ghi rõ không chặn M05 | Nhóm B. Ghi rõ không chặn M05 |
| QA-007 | Nhắc tới | Hiện hành | Không áp dụng: Ngân sách AI (M13) | Nhóm B. Ngân sách AI (M13) |
| QA-011 | Sở hữu | Hiện hành | FR-M05-01.08, FR-M05-02.18, FR-M05-03.12, FR-M05-04, FR-M05-04.01, FR-M05-04.02, FR-M05-04.04 | Nhóm B. Guest xem danh sách Topic/Tag và AI Classification trên bài |
| QA-017 | Sở hữu | Sửa một phần bởi DEC-050 | FR-M05-02, FR-M05-02.12, FR-M05-03, FR-M05-03.11, BR-M05-10, BR-M05-16 | Nhóm B. AI chỉ gợi ý Topic, Tag do user quyết; phản hồi = lựa chọn cuối |
| QA-022 | Nhắc tới | Bị thay bởi DEC-053 | — | Nhóm B. Đã được DEC-053 thay |
| QA-024 | Nhắc tới | Hiện hành | Không áp dụng: MoSCoW M13; sinh DEC-008 | Nhóm B. MoSCoW M13; sinh DEC-008 |
| QA-033 | Sở hữu | Sửa một phần bởi DEC-047, DEC-140 | Chuyển M03 | Nhóm B. Phần 2 tầng và một topic_id bị thay; phần grade_level độc lập còn hiệu lực (M03) |
| QA-043 | Phụ thuộc | Hiện hành | Chuyển M07 | Nhóm B. M07: Follow Topic; Tag không có trong phạm vi follow |
| QA-109 | Nhắc tới | Trùng với DEC-053 | — | Nhóm B. M06 |
| QA-112 | Nhắc tới | Hiện hành | Không áp dụng: M06; trọng số giống công thức trending | Nhóm B. M06; trọng số giống công thức trending |
| QA-113 | Nhắc tới | Trùng với DEC-056 | — | Nhóm B. M06 |
| QA-115 | Nhắc tới | Trùng với DEC-058 | — | Nhóm B. M06 |
| QA-160 | Sở hữu | Trùng với DEC-090 | — | Nhóm B. Mod dùng chung quản lý topic/tag |
| QA-165 | Phụ thuộc | Trùng với DEC-093 | — | Nhóm B. M10: công tắc AI per-module |
| QA-169 | Nhắc tới | Trùng với DEC-096 | — | Nhóm B. M13: mô hình |
| QA-175 | Phụ thuộc | Trùng với DEC-099 | — | Nhóm B. M13: timeout gợi ý topic 10s |
| QA-178 | Sở hữu | Trùng với DEC-100 | — | Nhóm B. Giới hạn 10 lần/phút/user cho nút gợi ý topic |
| QA-194 | Nhắc tới | Hiện hành | Không áp dụng: M12; không có badge theo chủ đề | Nhóm B. M12; không có badge theo chủ đề |
| QA-225 | Phụ thuộc | Bị thay bởi DEC-125 | — | Nhóm B. M14: tab Trending sub Topic/Tag |
| QA-226 | Nhắc tới | Hiện hành | Không áp dụng: M14: xác nhận DEC-052 giữ nguyên | Nhóm B. M14: xác nhận DEC-052 giữ nguyên |
| QA-227 | Phụ thuộc | Hiện hành | Chuyển M14 | Nhóm B. M14: Guest xem Trending Topic/Tag |
| QA-228 | Phụ thuộc | Hiện hành | Chuyển M14 | Nhóm B. M14/M07: Tag không phải đối tượng follow |
| QA-231 | Nhắc tới | Hiện hành | Không áp dụng: Trending Post (M14) | Nhóm B. Trending Post (M14) |
| QA-232 | Nhắc tới | Sửa một phần bởi QA-233 | Không áp dụng: Trending Post (M14) | Nhóm B. Trending Post (M14) |
| QA-233 | Nhắc tới | Hiện hành | Không áp dụng: Trending Post (M14) | Nhóm B. Trending Post (M14) |
| QA-234 | Nhắc tới | Sửa một phần bởi QA-256 | Không áp dụng: M14: phân trang feed | Nhóm B. M14: phân trang feed |
| QA-235 | Phụ thuộc | Hiện hành | Chuyển M14 | Nhóm B. M14: không ngưỡng tối thiểu vào Trending; với Trending Topic/Tag, DEC-145 chỉ hiện mục có điểm lớn hơn 0 |
| QA-236 | Phụ thuộc | Hiện hành | Chuyển M14 | Nhóm B. M14: không loại bài BANNED/HEAVY khỏi Trending; khớp DEC-145 (bài còn hiển thị thì vẫn tính) |
| QA-237 | Nhắc tới | Hiện hành | Không áp dụng: M14: Trending tự làm mới theo chu kỳ DEC-052 | Nhóm B. M14: Trending tự làm mới theo chu kỳ DEC-052 |
| QA-240 | Nhắc tới | Hiện hành | Không áp dụng: M14 phụ thuộc M05 | Nhóm B. M14 phụ thuộc M05 |
| QA-243 | Nhắc tới | Hiện hành | Không áp dụng: M15 dùng phân bố Post theo Topic — ghi ở Giao tiếp | Nhóm B. M15 dùng phân bố Post theo Topic — ghi ở Giao tiếp |
| QA-253 | Sở hữu | Trùng với DEC-132 | — | Nhóm B. Trùng nội dung DEC-132 |
| QA-254 | Phụ thuộc | Trùng với DEC-133 | — | Nhóm B. M13: ghi log đầu ra AI |
| QA-265 | Nhắc tới | Hiện hành | Không áp dụng: Cách viết tài liệu | Nhóm B. Cách viết tài liệu |
| MR-A02 | Nhắc tới | Hiện hành | Không áp dụng: Tóm tắt M14 | Nhóm B. Tóm tắt M14 |
| MR-A03 | Nhắc tới | Hiện hành | Không áp dụng: Tóm tắt M15 | Nhóm B. Tóm tắt M15 |
| MR-A04 | Nhắc tới | Hiện hành | Không áp dụng: Tóm tắt Phase 6 | Nhóm B. Tóm tắt Phase 6 |
| MR-FB-M05 | Sở hữu | Trùng với DEC-008 | — | Nhóm B. Fallback khi tắt AI |
| MR-M06 | Nhắc tới | Hiện hành | Không áp dụng: chỉ nhắc tới, không quy định hành vi M05 | Nhóm B |
| MR-M13 | Nhắc tới | Hiện hành | Không áp dụng: chỉ nhắc tới, không quy định hành vi M05 | Nhóm B |
| MR-M14 | Nhắc tới | Hiện hành | Không áp dụng: chỉ nhắc tới, không quy định hành vi M05 | Nhóm B |
| DEC-127 | Phụ thuộc | Hiện hành | Mục 2.1 | Nhóm D. Múi giờ cho cửa sổ 7 ngày của Trending |
| DEC-128 | Nhắc tới | Hiện hành | Không áp dụng: i18n giao diện | Nhóm D. i18n giao diện |
| DEC-129 | Phụ thuộc | Hiện hành | FR-M05-08.01 | Nhóm D. Nguyên tắc chỉ xóa cứng khi an toàn |
| DEC-130 | Nhắc tới | Hiện hành | Không áp dụng: chỉ nhắc tới, không quy định hành vi M05 | Nhóm D |
| DEC-131 | Phụ thuộc | Sửa một phần bởi DEC-146 | Không áp dụng: không quy định hành vi M05; xem CC-02 ở B.3 | Nhóm D. Công bố xử lý nội dung bởi AI bên thứ ba; chưa nêu Topic suggestion |
| DEC-134 | Nhắc tới | Hiện hành | Không áp dụng: chỉ nhắc tới, không quy định hành vi M05 | Nhóm D |
| DEC-135 | Nhắc tới | Hiện hành | Không áp dụng: chỉ nhắc tới, không quy định hành vi M05 | Nhóm D |
| DEC-136 | Nhắc tới | Hiện hành | Không áp dụng: chỉ nhắc tới, không quy định hành vi M05 | Nhóm D |
| DEC-138 | Nhắc tới | Hiện hành | Không áp dụng: chỉ nhắc tới, không quy định hành vi M05 | Nhóm D |
| ISS-189 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; đã có QA/DEC trả lời | Nhóm D. Dùng chung; đã có QA/DEC trả lời |
| ISS-191 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; đã có QA/DEC trả lời | Nhóm D. Dùng chung; đã có QA/DEC trả lời |
| ISS-192 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; đã có QA/DEC trả lời | Nhóm D. Dùng chung; đã có QA/DEC trả lời |
| ISS-193 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; đã có QA/DEC trả lời | Nhóm D. Dùng chung; đã có QA/DEC trả lời |
| ISS-196 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; đã có QA/DEC trả lời | Nhóm D. Dùng chung; đã có QA/DEC trả lời |
| ISS-197 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; đã có QA/DEC trả lời | Nhóm D. Dùng chung; đã có QA/DEC trả lời |
| ISS-198 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; đã có QA/DEC trả lời | Nhóm D. Dùng chung; đã có QA/DEC trả lời |
| ISS-199 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; đã có QA/DEC trả lời | Nhóm D. Dùng chung; đã có QA/DEC trả lời |
| ISS-200 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; đã có QA/DEC trả lời | Nhóm D. Dùng chung; đã có QA/DEC trả lời |
| ISS-201 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; đã có QA/DEC trả lời | Nhóm D. Dùng chung; đã có QA/DEC trả lời |
| ISS-202 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; đã có QA/DEC trả lời | Nhóm D. Dùng chung; đã có QA/DEC trả lời |
| ISS-203 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; đã có QA/DEC trả lời | Nhóm D. Dùng chung; đã có QA/DEC trả lời |
| ISS-204 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; đã có QA/DEC trả lời | Nhóm D. Dùng chung; đã có QA/DEC trả lời |
| ISS-206 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; đã có QA/DEC trả lời | Nhóm D. Dùng chung; đã có QA/DEC trả lời |
| QA-248 | Phụ thuộc | Trùng với DEC-127 | — | Nhóm D. Trùng nội dung DEC-127 |
| QA-250 | Phụ thuộc | Trùng với DEC-129 | — | Nhóm D. Trùng nội dung DEC-129 |
| QA-251 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; không quy định hành vi M05 | Nhóm D. Dùng chung; không quy định hành vi M05 |
| QA-252 | Phụ thuộc | Trùng với DEC-131 | — | Nhóm D. Trùng nội dung DEC-131 |
| QA-255 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; không quy định hành vi M05 | Nhóm D. Dùng chung; không quy định hành vi M05 |
| QA-256 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; không quy định hành vi M05 | Nhóm D. Dùng chung; không quy định hành vi M05 |
| QA-257 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; không quy định hành vi M05 | Nhóm D. Dùng chung; không quy định hành vi M05 |
| QA-258 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; không quy định hành vi M05 | Nhóm D. Dùng chung; không quy định hành vi M05 |
| QA-259 | Phụ thuộc | Hiện hành | Chuyển M10 | Nhóm D. Cờ AI nằm ở Admin Panel (M10) |
| QA-260 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; không quy định hành vi M05 | Nhóm D. Dùng chung; không quy định hành vi M05 |
| QA-261 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; không quy định hành vi M05 | Nhóm D. Dùng chung; không quy định hành vi M05 |
| QA-262 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; không quy định hành vi M05 | Nhóm D. Dùng chung; không quy định hành vi M05 |
| QA-263 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; không quy định hành vi M05 | Nhóm D. Dùng chung; không quy định hành vi M05 |
| QA-264 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; không quy định hành vi M05 | Nhóm D. Dùng chung; không quy định hành vi M05 |
| QA-266 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; không quy định hành vi M05 | Nhóm D. Dùng chung; không quy định hành vi M05 |
| MR-A05 | Nhắc tới | Hiện hành | Không áp dụng: Dùng chung; không quy định hành vi M05 | Nhóm D. Dùng chung; không quy định hành vi M05 |
| DEC-140 | Sở hữu | Hiện hành | FR-M05-01, FR-M05-02, FR-M05-03, FR-M05-03.11, FR-M05-04, FR-M05-04.01, FR-M05-06.07, BR-M05-01, BR-M05-20 | Nhóm A. AI chỉ gợi ý Topic; không Mod duyệt; Topic phẳng |
| DEC-141 | Sở hữu | Hiện hành | FR-M05-01, FR-M05-01.09, FR-M05-02.06, FR-M05-06, FR-M05-06.01, FR-M05-06.02, FR-M05-06.03, FR-M05-06.04, FR-M05-06.05, FR-M05-06.06, FR-M05-06.08, FR-M05-07, FR-M05-07.03, FR-M05-07.05, FR-M05-07.06, FR-M05-08, FR-M05-08.01, FR-M05-08.02, FR-M05-08.03, FR-M05-08.04, FR-M05-08.05, FR-M05-08.06, BR-M05-05, BR-M05-06, BR-M05-07, BR-M05-08, BR-M05-09, BR-M05-14 | Nhóm A. Quản lý danh mục Topic chỉ Admin |
| DEC-142 | Sở hữu | Hiện hành | FR-M05-01, FR-M05-01.06, FR-M05-01.07, FR-M05-01.10, FR-M05-02, FR-M05-02.12, FR-M05-02.13, FR-M05-02.20, FR-M05-02.21, FR-M05-03, FR-M05-03.10, FR-M05-04, FR-M05-11, FR-M05-11.01, FR-M05-11.02, FR-M05-11.03, FR-M05-11.04, FR-M05-11.05, FR-M05-11.06, BR-M05-03, BR-M05-04, BR-M05-10 | Nhóm A. Topic, Tag trên bài: nháp, sửa bài, Mod/Admin sửa bài người khác, browse |
| DEC-143 | Sở hữu | Hiện hành | FR-M05-03, FR-M05-03.05, FR-M05-03.06, FR-M05-03.07, FR-M05-03.14, FR-M05-10, FR-M05-10.01, FR-M05-10.02, FR-M05-10.03, FR-M05-10.04, BR-M05-20, BR-M05-23, BR-M05-24, BR-M05-25, BR-M05-27 | Nhóm A. Tag: ký tự, hiển thị, kích hoạt lại |
| DEC-144 | Sở hữu | Hiện hành | FR-M05-02, FR-M05-02.05, FR-M05-02.06, FR-M05-02.15, FR-M05-02.19, BR-M05-12, BR-M05-14, BR-M05-17 | Nhóm A. Chi tiết gợi ý Topic |
| DEC-145 | Sở hữu | Hiện hành | FR-M05-05, FR-M05-05.01, FR-M05-05.02, FR-M05-05.03, FR-M05-05.04, FR-M05-05.05, FR-M05-05.06, FR-M05-05.08, FR-M05-05.09, FR-M05-05.10, FR-M05-05.11, FR-M05-05.12, FR-M05-05.13, FR-M05-05.14, BR-M05-29, BR-M05-30, BR-M05-31 | Nhóm A. Công thức Trending Topic/Tag mới |
| DEC-146 | Sở hữu | Hiện hành | FR-M05-09, FR-M05-09.07, FR-M05-10.06, FR-M05-11, FR-M05-11.07 | Nhóm A. Nhật ký thao tác Mod; công bố AI |
| ISS-207 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-140 | Nhóm A. Đã có DEC-140 |
| ISS-208 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-140 | Nhóm A. Đã có DEC-140 |
| ISS-209 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-140 | Nhóm A. Đã có DEC-140 |
| ISS-210 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-141 | Nhóm A. Đã có DEC-141 |
| ISS-211 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-145 | Nhóm A. Đã có DEC-145 |
| ISS-212 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-141 | Nhóm A. Đã có DEC-141 |
| ISS-213 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-142 | Nhóm A. Đã có DEC-142 |
| ISS-214 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-142 | Nhóm A. Đã có DEC-142 |
| ISS-215 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-142 | Nhóm A. Đã có DEC-142 |
| ISS-216 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-143 | Nhóm A. Đã có DEC-143 |
| ISS-217 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-142 | Nhóm A. Đã có DEC-142 |
| ISS-218 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-141 | Nhóm A. Đã có DEC-141 |
| ISS-219 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-141 | Nhóm A. Đã có DEC-141 |
| ISS-220 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-141 | Nhóm A. Đã có DEC-141 |
| ISS-221 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-144 | Nhóm A. Đã có DEC-144 |
| ISS-222 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-144 | Nhóm A. Đã có DEC-144 |
| ISS-223 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-144 | Nhóm A. Đã có DEC-144 |
| ISS-224 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-143 | Nhóm A. Đã có DEC-143 |
| ISS-225 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-145 | Nhóm A. Đã có DEC-145 |
| ISS-226 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-145 | Nhóm A. Đã có DEC-145 |
| ISS-227 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-145 | Nhóm A. Đã có DEC-145 |
| ISS-228 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-142 | Nhóm A. Đã có DEC-142 |
| ISS-229 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-142 | Nhóm A. Đã có DEC-142 |
| ISS-230 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-146 | Nhóm A. Đã có DEC-146 |
| ISS-231 | Nhắc tới | Hiện hành | Không áp dụng: Đã có DEC-146 | Nhóm A. Đã có DEC-146 |
| QA-267 | Sở hữu | Trùng với DEC-140 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-268 | Sở hữu | Trùng với DEC-140 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-269 | Sở hữu | Trùng với DEC-140 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-270 | Sở hữu | Trùng với DEC-141 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-271 | Sở hữu | Trùng với DEC-145 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-272 | Sở hữu | Trùng với DEC-141 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-273 | Sở hữu | Trùng với DEC-142 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-274 | Sở hữu | Trùng với DEC-142 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-275 | Sở hữu | Trùng với DEC-142 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-276 | Sở hữu | Trùng với DEC-143 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-277 | Sở hữu | Trùng với DEC-142 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-278 | Sở hữu | Trùng với DEC-141 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-279 | Sở hữu | Trùng với DEC-141 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-280 | Sở hữu | Trùng với DEC-141 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-281 | Sở hữu | Trùng với DEC-144 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-282 | Sở hữu | Trùng với DEC-144 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-283 | Sở hữu | Trùng với DEC-144 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-284 | Sở hữu | Trùng với DEC-143 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-285 | Sở hữu | Trùng với DEC-145 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-286 | Sở hữu | Trùng với DEC-145 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-287 | Sở hữu | Trùng với DEC-145 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-288 | Sở hữu | Trùng với DEC-142 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-289 | Sở hữu | Trùng với DEC-142 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-290 | Sở hữu | Trùng với DEC-146 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| QA-291 | Sở hữu | Trùng với DEC-146 | — | Nhóm A. Câu trả lời của stakeholder, nội dung nằm trong DEC |
| DEC-081 | Phụ thuộc | Sửa một phần bởi DEC-146 | FR-M05-09.07, FR-M05-10.06, FR-M05-11.07 | Nhóm B. M08: nhật ký kiểm duyệt |
| OPEN-009 | Phụ thuộc | Hiện hành | Chuyển M14 | Nhóm B. M14: Trending Post có thêm bookmark không |
| DEC-037 | Phụ thuộc | Hiện hành | FR-M05-11.06 | Nhóm C. M03: lịch sử sửa bài; đổi Topic/Tag của Mod không ghi vào đây |
| DEC-094 | Phụ thuộc | Hiện hành | Chuyển M10 | Nhóm C. M10: nhật ký thao tác Admin |
| OPEN-005 | Phụ thuộc | Hiện hành | TBD-M05-02 | Nhóm C. Hạ tầng ghi sự kiện hoãn; lượt xem trong Trending phụ thuộc vào đây |

### C.2 Chuỗi quyết định

| Chuỗi | Nội dung hiện hành |
|---|---|
| QA-033 → DEC-047 → DEC-140 | Danh mục Topic phẳng, không có Topic con (lồng nhau hoãn). Phần "2 tầng Category → Topic" và "mỗi bài một topic" của QA-033 bị thay. Ý "Lớp/Khối là trường độc lập trên bài, không đối chiếu với Topic" vẫn hiệu lực nhưng thuộc M03. Cạnh lineage "DEC-140 thay DEC-047" bị bác bỏ: DEC-140 xác nhận DEC-047. |
| DM-3.1, DG-3, GL:Topic → DEC-048 → DEC-141 | 11 Topic của DEC-048 là danh mục ban đầu. Chỉ Admin thêm Topic; danh mục không giới hạn số lượng; tên Topic không trùng (không phân biệt hoa/thường, bỏ khoảng trắng thừa, giữ dấu); Topic mới không tự gán cho bài cũ. Phần mục đích của draft (tổ chức lĩnh vực tri thức cho học sinh THPT, không bó theo môn học) vẫn hiệu lực. |
| DEC-049, DEC-090, QA-107, QA-160 → DEC-141 | Thêm, gộp, xóa Topic chỉ Admin; Mod không còn sửa hay gộp Topic; không hỗ trợ đổi tên Topic. Gộp chuyển bài sang Topic đích, rồi Topic nguồn tự bị xóa và người theo dõi Topic nguồn chuyển sang Topic đích. Xóa Topic chỉ khi không có bài viết nào ngoài bài nháp; bài nháp mất Topic đó, lượt theo dõi Topic đó bị bỏ. Xóa mềm Tag khi khủng hoảng vẫn dùng chung Mod và Admin. |
| DM-3.4, DM-2.1 → DEC-049 → DEC-142 | Mỗi bài khi gửi có 1–3 Topic, thay cho "một Topic" (DM-3.4) và "Topic nếu sử dụng" (DM-2.1); bài nháp được có 0–3 Topic. Tác giả đổi Topic, Tag khi sửa bài đã gửi; Mod, Admin đổi được trên bài người khác, không thông báo tác giả, không ghi vào lịch sử sửa bài. Xem bài theo Topic/Tag qua bộ lọc M06. Quan hệ bài có nhiều Tag vẫn hiệu lực. |
| DM-3.2 → DEC-051 → DEC-143 | Tối đa 5 Tag mỗi bài, thay cho "không giới hạn số lượng". Tên Tag tối đa 30 ký tự, không tính "#"; chỉ gồm chữ cái (kể cả có dấu), chữ số, "_", có ít nhất một chữ cái; hiển thị chung bằng tên chuẩn hóa chữ thường. Mod, Admin vô hiệu hóa Tag khi khủng hoảng và kích hoạt lại được; không sửa, gộp, xóa Tag. Ý "một bài có nhiều Tag" của draft vẫn hiệu lực. |
| DM-11.2, DG-6, GL:AI Classification → QA-017 → DEC-050 → DEC-140, DEC-142, DEC-144 | AI chỉ gợi ý Topic, không gợi ý Tag; không có bước Mod duyệt. Gợi ý chạy khi tác giả bấm nút, khi soạn bài và khi sửa bài đã gửi; Mod, Admin sửa bài người khác không dùng gợi ý. Ngưỡng 20 từ đếm trên tiêu đề cộng nội dung chữ. Phản hồi gợi ý chỉ ghi khi gợi ý chưa lỗi thời, lúc gửi bài hoặc lưu bản sửa. Các phần khác của DG-6 (5 năng lực AI bắt buộc) không thuộc M05. |
| DEC-008 → DEC-092, DEC-093; DEC-099; DEC-132 → DEC-141, DEC-144 | Khi tắt AI, tác giả tự chọn Topic từ danh mục, không có gợi ý. Nơi bật/tắt: cấu hình hệ thống ở Admin Panel (DEC-092), gồm công tắc tổng và công tắc riêng cho gợi ý Topic; công tắc riêng chỉ có tác dụng khi công tắc tổng bật (DEC-093). Lỗi tạm thời khi AI đang bật được xử lý khác với tắt AI. Topic AI trả về được đối chiếu với danh mục hiện tại: Topic ngoài danh mục bị bỏ, chỉ khi không còn Topic hợp lệ nào mới coi là thất bại (xử lý như lỗi tạm thời). |
| DEC-100 → DEC-144 | Mỗi người dùng tối đa 10 lần yêu cầu gợi ý Topic trong 60 giây gần nhất. |
| DM-7.2 → DEC-052 → DEC-145 | Tiêu chí Views/Bookmarks/Recency của draft bị thay. Công thức hiện hành là của DEC-145 (BR-M05-29): tổng tương tác xảy ra trong cửa sổ 7 ngày trượt, bất kể bài đăng lúc nào; bài được đăng = 1, upvote cho bài = 2, comment (kể cả reply) = 1, bookmark = 1; không decay; chỉ tính bài trên feed chính; tương tác đã rút lại, upvote cho comment và lượt xem không tính. Công thức Σ(1 + upvotes×2 + comments×1) trên các bài đăng trong cửa sổ của DEC-052 bị thay. |
| DEC-052, QA-106 → DEC-145 | Phần còn hiệu lực của DEC-052: cửa sổ 7 ngày trượt theo thời điểm tính (không theo tuần lịch), chu kỳ tính lại 15–30 phút, Trending Topic/Tag là phần riêng của Feed. DEC-145 thêm: mọi tương tác có mặt trong điểm chậm nhất 30 phút; chỉ hiện mục có điểm lớn hơn 0; thứ tự theo điểm, rồi số bài mới, rồi tên A–Z. |
| ISS-171 → ISS-185, DEC-124; DEC-145 | Công thức decay của DEC-124 chỉ áp cho Trending Post (M14). Trending Topic/Tag không dùng decay và theo DEC-145. Việc Trending Post có thêm bookmark hay không nằm ở OPEN-009. |
| DEC-124 → OPEN-009 | Trending Post (M14) có thêm bookmark hay không còn mở; hướng đang được chấp nhận là thêm với cùng trọng số, review ở M14. Không thuộc yêu cầu M05. |
| DM-7.1 → QA-225 → DEC-125 | Feed gồm 4 tab; tab Trending có sub-view Topic và Tag (M14 hiển thị, M05 cung cấp). Feed Latest/Popular/Personalized của draft bị thay. |
| DM-4.5, DM-8.1 → QA-043 | Chỉ theo dõi được User, Topic, Post; Tag và Group không phải đối tượng theo dõi (QA-228 nhắc lại cho Tag). Thuộc M07. |
| QA-022 → DEC-053 | Tìm kiếm gồm cả Tag và Topic (khớp chính xác hoặc tiền tố). Thuộc M06. |
| DEC-081, DEC-131 → DEC-146 | Nhật ký kiểm duyệt ghi thêm việc vô hiệu hóa, kích hoạt lại Tag và việc đổi Topic, Tag trên bài người khác, cho cả Mod và Admin. Trang Chính sách quyền riêng tư nêu thêm việc gửi tiêu đề và nội dung bài đang soạn, kể cả chưa đăng, cho AI khi gợi ý Topic. |
| QA-232 → QA-233; QA-234 → QA-256; DEC-139 → QA-266 | Không ảnh hưởng hành vi M05 (Trending Post, SSR, quy ước tài liệu). |
