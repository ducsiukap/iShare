---
ma_tai_lieu: ROUTES
phien_ban: 1.0
trang_thai: Đã chốt
ngay: 2026-11-28
tac_gia: Phạm Văn Đức
---
# Màn hình → đường dẫn trang — iShare (routes.md)

[Vietnamese Doc] — Bảng bàn giao cho phase Coding: mỗi màn hình của `screen-inventory.md` với đường dẫn trang (từ
`flows.md` mục 1), vai trò truy cập, khung trang, component chính, artboard trên canvas và frame Figma. Đặc tả từng
component: `UI-KIT.md`.

- 75 màn hình: 49 có đường dẫn riêng; 26 hiện trên một trang khác (khung, hộp thoại, ngăn phải, ô nổi, một mục
  trong trang) — cột Đường dẫn ghi "—" kèm nơi hiện.
- Đường dẫn trong `flows.md` phần lớn là đề xuất (đã định: `/u/{username}`); phase Coding có thể đổi tên nhưng giữ cấu
  trúc và tham số.
- Vai trò: theo cột "Vai trò truy cập" của `flows.md`; màn hình không có đường dẫn riêng lấy theo actor của
  `screen-inventory.md`.
- Khung: AppHeader và NavBar ở phía người dùng; AdminShell ở khu kiểm duyệt và quản trị (DD-UI-42); PageLayout với
  biến thể bố cục (DD-UI-40). Trang không có cột menu (đăng ký, đăng nhập…) dùng `--center`.
- Component chính: component của design system có trong artboard mặc định (theme sáng), bỏ phần khung và các thành
  phần có ở hầu hết trang (Button, IconButton, Link, Avatar, Counter, ô tìm kiếm, PageHeader, SectionCard); hộp thoại,
  ngăn và ô nổi chỉ tính phần nổi.
- Artboard: tên artboard mặc định trên canvas "iShare — Giao diện" (https://claude.ai/artifact/HAykztXFcJbkAiSCXKvift);
  các trạng thái khác cùng dạng `SCR-…--<trạng thái>--desktop` (danh sách trạng thái ở `screen-inventory.md`). Chỉ có
  bản desktop (DD-UI-02).
- Figma: frame mặc định theme sáng và tối trong "iShare — UI" (https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m);
  mỗi page một đợt, mỗi màn hình một hàng có nhãn.

## Bảng màn hình


### SHARED

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-SHARED-01 Khung ứng dụng (thanh trên cùng, điều hướng trái, menu tài khoản) | — (khung của mọi trang phía người dùng) | Guest, Người dùng, Mod/Admin | AppHeader · NavBar · PageLayout `--two` | Menu | `SCR-SHARED-01--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=96-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=97-2) |
| SCR-SHARED-02 Banner thông báo toàn trang | — (dưới thanh trên cùng, mọi trang) | Guest, Người dùng, Mod/Admin | AppHeader · NavBar · PageLayout `--two` | Banner | `SCR-SHARED-02--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=101-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=102-2) |
| SCR-SHARED-03 Trang bảo trì | — (thay mọi trang khi bật bảo trì (trừ tài khoản ADMIN)) | Guest, Người dùng, Mod | AppHeader · PageLayout `--center` | ErrorState | `SCR-SHARED-03--default--desktop` (chỉ mặc định) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=436-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=437-2) |
| SCR-SHARED-04 Trang lỗi chung | — (mọi đường dẫn không tìm thấy, không có quyền hoặc lỗi tải) | Guest, Người dùng, Mod/Admin | AppHeader · NavBar · PageLayout `--two` | ErrorState | `SCR-SHARED-04--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=104-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=105-2) |
| SCR-SHARED-05 Màn hình tài khoản bị khóa (ban) | `/banned` | Tài khoản BANNED | AppHeader · PageLayout `--center` | DescriptionList | `SCR-SHARED-05--default--desktop` (chỉ mặc định) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=509-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=510-2) |
| SCR-SHARED-06 Khung quản trị (Admin Panel, công cụ Mod) | — (khung của `/mod/*` và `/admin/*`) | Mod, Admin | AdminShell · PageLayout `--admin` | AdminShell, NavBar `--console` | `SCR-SHARED-06--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=516-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=517-2) |

### M01

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M01-01 Đăng ký (bước 1: email, mật khẩu, đồng ý chính sách) | `/register` | Guest | AppHeader · PageLayout `--center` | GoogleButton, TextField, Checkbox, StepIndicator | `SCR-M01-01--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=732-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=733-2) |
| SCR-M01-02 Chờ xác minh email (bước 2) | `/register/verify`; magic link `/verify-email?token=…` | Guest | AppHeader · PageLayout `--center` | StepIndicator | `SCR-M01-02--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=443-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=444-2) |
| SCR-M01-03 Thiết lập tài khoản (bước 3) | `/register/setup` | Chủ tài khoản đã xác minh | AppHeader · PageLayout `--center` | TextField, TextArea, Select, AvatarUpload, StepIndicator | `SCR-M01-03--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=447-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=448-2) |
| SCR-M01-04 Đăng nhập | `/login` | Guest | AppHeader · PageLayout `--center` | GoogleButton, TextField | `SCR-M01-04--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=737-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=738-2) |
| SCR-M01-05 Quên mật khẩu | `/forgot-password` | Guest | AppHeader · PageLayout `--center` | TextField | `SCR-M01-05--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=454-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=455-2) |
| SCR-M01-06 Đặt mật khẩu mới qua liên kết | `/reset-password?token=…` | Người có link | AppHeader · PageLayout `--center` | TextField | `SCR-M01-06--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=741-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=742-2) |
| SCR-M01-07 Cài đặt tài khoản | `/settings` | Người dùng | AppHeader · NavBar · PageLayout `--two` | TextField, DescriptionList, Tabs | `SCR-M01-07--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=744-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=745-2) |
| SCR-M01-08 Kích hoạt lại tài khoản (trang riêng, nhập mã email) | `/reactivate` | Chủ tài khoản DEACTIVATED | AppHeader · PageLayout `--center` | TextField | `SCR-M01-08--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=468-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=469-2) |
| SCR-M01-09 Trang Privacy Policy/ToS | `/policy` | Mọi người | AppHeader · NavBar · PageLayout ba cột | TableOfContents | `SCR-M01-09--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=472-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=473-2) |
| SCR-M01-10 Đồng ý lại chính sách mới | — (chặn mọi trang tới khi đồng ý phiên bản mới) | Người dùng, Mod/Admin | AppHeader · PageLayout `--center` | SectionCard | `SCR-M01-10--default--desktop` (chỉ mặc định) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=475-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=476-2) |

### M02

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M02-01 Hồ sơ người dùng (/u/{username}) | `/u/{username}`; tab chủ hồ sơ `?tab=bookmark\|deleted` | Mọi người | AppHeader · NavBar · PageLayout `--two` | Tag, TopicChip, GradeLabel, Badge, PostCard, Tabs | `SCR-M02-01--default--desktop` (+9 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=203-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=204-2) |
| SCR-M02-02 Người theo dõi / đang theo dõi (hộp thoại) | — (hộp thoại trong `/u/{username}`) | Guest, Người dùng, Mod/Admin | AppHeader · NavBar · PageLayout `--two` | ListItem, UserRow, Tabs, Dialog | `SCR-M02-02--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=214-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=215-2) |
| SCR-M02-03 Sửa hồ sơ (trang sửa) | `/profile/edit` | Chủ hồ sơ | AppHeader · NavBar · PageLayout `--two` | TextField, TextArea, Select, AvatarUpload | `SCR-M02-03--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=219-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=220-2) |

### M03

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M03-01 Viết bài / sửa bài (trình soạn) | `/write` (trong nhóm `?group={id}`); `/p/{id}/edit` | Người dùng; sửa: tác giả | AppHeader · NavBar · PageLayout ba cột | Tag, TopicChip, StatusLabel, Attachment, TextField, Select, FileDrop, TagInput, EditorToolbar | `SCR-M03-01--default--desktop` (+7 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=194-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=195-2) |
| SCR-M03-02 Chi tiết bài viết | `/p/{id}` | Mọi người theo quyền xem | AppHeader · NavBar · PageLayout ba cột | Tag, TopicChip, GradeLabel, StatusLabel, PostBody, ActionBar, UpvoteButton, Poll, Attachment, Comment, TextArea, Checkbox, SegmentedControl, TableOfContents, DescriptionList, EditorToolbar, CommentComposer | `SCR-M03-02--default--desktop` (+14 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=659-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=660-2) |
| SCR-M03-03 Lịch sử sửa bài | `/p/{id}/history` | Người xem được bài | AppHeader · NavBar · PageLayout `--two` | StatusLabel, PostCard | `SCR-M03-03--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=192-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=193-2) |
| SCR-M03-04 Quản lý bình chọn (trong khối bình chọn, chỉ tác giả) | — (trong khối bình chọn của `/p/{id}`) | Người dùng, Mod/Admin | — (artboard chỉ vẽ phần này) | StatusLabel, PollEditor, TextField, DateTimeField, ListItem | `SCR-M03-04--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=154-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=155-2) |
| SCR-M03-05 Hàng chờ duyệt bài (Mod/Admin) | `/mod/review` | Mod, Admin | AdminShell · PageLayout `--admin` | PostCard, TextArea | `SCR-M03-05--default--desktop` (+4 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=519-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=520-2) |

### M04

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M04-01 Khu bình luận (trong chi tiết bài) | — (trong `/p/{id}`; bình luận `/p/{id}#c-{id}`) | Mọi người theo quyền xem | — (artboard chỉ vẽ phần này) | StatusLabel, UpvoteButton, Comment, TextArea, SegmentedControl, EditorToolbar, CommentComposer | `SCR-M04-01--default--desktop` (+9 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=180-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=181-2) |
| SCR-M04-02 Xem lại bình luận đã bị xử lý (chỉ đọc) | `/c/{id}` | Tác giả bình luận | AppHeader · NavBar · PageLayout `--two` | StatusLabel, Comment, DescriptionList | `SCR-M04-02--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=525-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=526-2) |

### M05

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M05-01 Danh sách Chủ đề và Tag | `/topics`; danh sách Tag `?tab=tag` | Mọi người | AppHeader · NavBar · PageLayout `--two` | Tag, ListItem | `SCR-M05-01--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=115-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=116-2) |
| SCR-M05-02 Quản lý Chủ đề (Admin) | `/admin/topics` | Admin | AdminShell · PageLayout `--admin` | TextField, DataTable | `SCR-M05-02--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=529-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=530-2) |
| SCR-M05-03 Gộp Chủ đề (hộp thoại) | — (hộp thoại trong `/admin/topics`) | Admin | AdminShell · PageLayout `--admin` | Select, Dialog | `SCR-M05-03--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=532-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=533-2) |
| SCR-M05-04 Quản lý Tag (Mod/Admin) | `/mod/tags` | Mod, Admin | AdminShell · PageLayout `--admin` | StatusLabel, DataTable | `SCR-M05-04--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=535-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=536-2) |
| SCR-M05-05 Đổi Chủ đề, Tag của bài (hộp thoại Mod/Admin) | — (hộp thoại trong `/p/{id}`) | Mod, Admin | AppHeader · NavBar · PageLayout ba cột | Tag, TopicChip, TextArea, TagInput, Dialog | `SCR-M05-05--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=681-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=682-2) |

### M06

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M06-01 Gợi ý khi gõ và lịch sử tìm kiếm (ô tìm kiếm) | — (ô tìm kiếm trên thanh trên cùng) | Guest, Người dùng, Mod/Admin | AppHeader · NavBar · PageLayout `--two` | Combobox | `SCR-M06-01--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=477-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=478-2) |
| SCR-M06-02 Kết quả tìm kiếm | `/search?q=&topic=&tag=&time=&following=&sort=`; trang Chủ đề/Tag: `?topic={id}` hoặc `?tag={name}` với `q` rỗng | Mọi người | AppHeader · NavBar · PageLayout ba cột | Tag, TopicChip, GradeLabel, PostCard, Select, Checkbox, SearchField | `SCR-M06-02--default--desktop` (+5 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=482-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=483-2) |

### M07

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M07-01 Ngăn thông báo (bấm chuông) | — (ngăn mở từ chuông trên thanh trên cùng) | Người dùng, Mod/Admin | AppHeader · NavBar · PageLayout `--two` | NotificationItem, Menu | `SCR-M07-01--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=340-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=341-2) |
| SCR-M07-02 Trang Thông báo | `/notifications` | Người dùng | AppHeader · NavBar · PageLayout `--two` | NotificationItem | `SCR-M07-02--default--desktop` (+4 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=345-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=346-2) |
| SCR-M07-03 Popup tin nhắn mới và biểu tượng Tin nhắn | — (popup góc dưới phải, mọi trang; số chưa đọc trên thanh trên cùng) | Người dùng, Mod/Admin | AppHeader · NavBar · PageLayout `--two` | NewMessagePopup | `SCR-M07-03--default--desktop` (chỉ mặc định) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=351-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=352-2) |

### M08

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M08-01 Báo cáo vi phạm (hộp thoại) | — (hộp thoại trên bài, bình luận, hồ sơ, trang nhóm) | Người dùng, Mod/Admin | AppHeader · NavBar · PageLayout ba cột | TextArea, Radio, FileDrop, Dialog | `SCR-M08-01--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=684-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=685-2) |
| SCR-M08-02 Hàng chờ báo cáo (Mod/Admin) | `/mod/reports` | Mod, Admin | AdminShell · PageLayout `--admin` | StatusLabel, Select, DataTable, FilterBar, Pagination | `SCR-M08-02--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=511-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=512-2) |
| SCR-M08-03 Chi tiết vụ báo cáo | `/mod/reports/{id}` | Mod, Admin | AdminShell · PageLayout `--admin3` | StatusLabel, PostCard, DataTable, DescriptionList | `SCR-M08-03--default--desktop` (+4 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=688-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=689-2) |
| SCR-M08-04 Lý do cho biện pháp và kết luận vụ (hộp thoại) | — (hộp thoại trong `/mod/reports/{id}`) | Mod, Admin | AdminShell · PageLayout `--admin3` | TextArea, Radio, Dialog | `SCR-M08-04--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=693-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=694-2) |
| SCR-M08-05 Mức cảnh cáo của tôi | — (một mục trong `/settings`) | Người dùng | AppHeader · NavBar · PageLayout `--two` | StatusLabel, DataTable, Tabs, InlineAlert | `SCR-M08-05--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=554-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=555-2) |
| SCR-M08-06 Nhật ký kiểm duyệt | `/mod/logs`; `?actor={username}` | Mod (của mình), Admin | AdminShell · PageLayout `--admin` | Select, DataTable, FilterBar, Pagination | `SCR-M08-06--default--desktop` (+4 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=558-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=559-2) |

### M09

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M09-01 Gửi khiếu nại | `/appeals/new?ref={mã xử lý}` | Người bị xử lý | AppHeader · NavBar · PageLayout `--two` | TextArea, FileDrop, DescriptionList | `SCR-M09-01--default--desktop` (+4 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=564-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=565-2) |
| SCR-M09-02 Khiếu nại của tôi | `/appeals`; chi tiết `/appeals/{id}` | Người dùng | AppHeader · NavBar · PageLayout `--two` | StatusLabel, DataTable | `SCR-M09-02--default--desktop` (+4 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=570-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=571-2) |
| SCR-M09-03 Hàng chờ khiếu nại (Mod/Admin) | `/mod/appeals` | Mod, Admin | AdminShell · PageLayout `--admin` | StatusLabel, Select, DataTable, FilterBar | `SCR-M09-03--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=576-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=577-2) |
| SCR-M09-04 Chi tiết khiếu nại | `/mod/appeals/{id}` | Mod, Admin | AdminShell · PageLayout `--admin3` | StatusLabel, TextArea, Radio, DescriptionList | `SCR-M09-04--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=581-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=582-2) |

### M10

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M10-01 Người dùng (Admin Panel) | `/admin/users` | Admin | AdminShell · PageLayout `--admin` | StatusLabel, Select, DataTable, FilterBar, Pagination | `SCR-M10-01--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=586-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=587-2) |
| SCR-M10-02 Vai trò của một người dùng (đề xuất, giáng, thu hồi) | — (ngăn phải trong `/admin/users`) | Admin | AdminShell · PageLayout `--admin` | StatusLabel, DescriptionList | `SCR-M10-02--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=590-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=591-2) |
| SCR-M10-03 Tự từ chức vai trò (hộp thoại) | — (hộp thoại trong `/settings`) | Mod, Admin | AppHeader · NavBar · PageLayout `--two` | Dialog | `SCR-M10-03--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=594-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=595-2) |
| SCR-M10-04 Cấu hình hệ thống | `/admin/settings` | Admin | AdminShell · PageLayout `--admin` | Switch | `SCR-M10-04--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=597-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=598-2) |
| SCR-M10-05 Banner toàn trang (đặt, sửa, gỡ) | `/admin/banner` | Admin | AdminShell · PageLayout `--admin` | StatusLabel, TextArea, Banner | `SCR-M10-05--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=600-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=601-2) |
| SCR-M10-06 Nhật ký thao tác Admin | `/admin/logs` | Admin | AdminShell · PageLayout `--admin` | Select, DataTable, FilterBar | `SCR-M10-06--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=604-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=605-2) |

### M11

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M11-01 Danh sách nhóm | `/groups` | Mọi người | AppHeader · NavBar · PageLayout `--two` | StatusLabel, GroupCard | `SCR-M11-01--default--desktop` (+4 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=698-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=699-2) |
| SCR-M11-02 Tạo nhóm | `/groups/new` | Người dùng | AppHeader · NavBar · PageLayout `--two` | TextField, TextArea, Radio, Switch | `SCR-M11-02--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=359-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=360-2) |
| SCR-M11-03 Trang nhóm | `/g/{id}`; link mời `?invite={mã}` | Theo chế độ nhóm | AppHeader · NavBar · PageLayout ba cột | Tag, TopicChip, GradeLabel, StatusLabel, PostCard, DescriptionList, Tabs | `SCR-M11-03--default--desktop` (+11 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=362-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=363-2) |
| SCR-M11-04 Gửi yêu cầu tham gia (hộp thoại câu hỏi tham gia) | — (hộp thoại trong `/g/{id}`) | Người dùng, Mod/Admin | AppHeader · NavBar · PageLayout `--two` | TextArea, Dialog | `SCR-M11-04--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=375-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=376-2) |
| SCR-M11-05 Thành viên nhóm | `/g/{id}/members` | Theo quyền xem nhóm | AppHeader · NavBar · PageLayout ba cột | StatusLabel, ListItem, UserRow, DescriptionList, Tabs | `SCR-M11-05--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=379-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=380-2) |
| SCR-M11-06 Yêu cầu tham gia chờ duyệt | `/g/{id}/requests` | Owner, Group Mod | AppHeader · NavBar · PageLayout `--two` | StatusLabel, PostCard, Tabs | `SCR-M11-06--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=384-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=385-2) |
| SCR-M11-07 Mời vào nhóm (hộp thoại) | — (hộp thoại trong `/g/{id}`) | Thành viên nhóm, Group Mod, Owner nhóm | AppHeader · NavBar · PageLayout ba cột | TextField, ListItem, UserRow, Dialog | `SCR-M11-07--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=387-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=388-2) |
| SCR-M11-08 Cài đặt nhóm | `/g/{id}/settings` | Owner | AppHeader · NavBar · PageLayout `--two` | TextField, TextArea, Radio, Switch | `SCR-M11-08--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=390-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=391-2) |
| SCR-M11-09 Rời nhóm (hộp thoại) | — (hộp thoại trong `/g/{id}`) | Thành viên nhóm, Group Mod, Owner nhóm | AppHeader · NavBar · PageLayout ba cột | Dialog | `SCR-M11-09--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=394-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=395-2) |
| SCR-M11-10 Hàng chờ duyệt bài của nhóm | `/g/{id}/queue` | Owner, Group Mod | AppHeader · NavBar · PageLayout `--two` | StatusLabel, PostCard, TextArea, Tabs | `SCR-M11-10--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=397-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=398-2) |
| SCR-M11-11 Danh sách chặn tham gia | `/g/{id}/blocked` | Owner, Group Mod | AppHeader · NavBar · PageLayout `--two` | StatusLabel, ListItem, UserRow, Tabs | `SCR-M11-11--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=402-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=403-2) |

### M12

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M12-01 Bảng xếp hạng | `/leaderboard`; `?period=week\|month\|all&grade=10\|11\|12` | Mọi người | AppHeader · NavBar · PageLayout `--two` | SegmentedControl, LeaderboardRow, Tabs | `SCR-M12-01--default--desktop` (+4 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=223-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=224-2) |

### M13

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M13-01 Tóm tắt bài viết (ngăn hiển thị) | — (ngăn phải trong `/p/{id}`) | Người dùng, Mod/Admin | AppHeader · NavBar · PageLayout ba cột | Drawer | `SCR-M13-01--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=673-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=674-2) |

### M14

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M14-01 Trang chủ (bảng tin) | `/`; `?tab=following\|group\|newest`, `?sub=topic\|tag` | Mọi người | AppHeader · NavBar · PageLayout `--two` | Tag, TopicChip, GradeLabel, PostCard, Tabs | `SCR-M14-01--default--desktop` (+5 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=108-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=109-2) |

### M15

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M15-01 Thống kê người dùng | `/admin/stats/users`; `?range=today\|7d\|30d\|all` | Admin | AdminShell · PageLayout `--admin` | SegmentedControl, DataTable, StatTile, TrendChart | `SCR-M15-01--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=608-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=609-2) |
| SCR-M15-02 Thống kê nội dung | `/admin/stats/content`; `?range=…` | Admin | AdminShell · PageLayout `--admin` | SegmentedControl, DataTable, StatTile, TrendChart | `SCR-M15-02--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=612-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=613-2) |
| SCR-M15-03 Thống kê kiểm duyệt | `/admin/stats/moderation`; `?range=…` | Admin | AdminShell · PageLayout `--admin` | SegmentedControl, DataTable, StatTile, TrendChart | `SCR-M15-03--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=616-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=617-2) |

### M16

| Màn hình | Đường dẫn | Vai trò | Khung | Component chính | Artboard | Figma |
|---|---|---|---|---|---|---|
| SCR-M16-01 Hộp thư Chat | `/messages` | Người dùng | AppHeader · NavBar · PageLayout `--chat` | TextArea, ConversationItem, MessageBubble, CommentComposer | `SCR-M16-01--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=701-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=702-2) |
| SCR-M16-02 Cuộc trò chuyện (1-1 hoặc nhóm chat) | `/messages/{id}` | Thành viên | AppHeader · NavBar · PageLayout `--chat` | TextArea, ConversationItem, MessageBubble, CommentComposer | `SCR-M16-02--default--desktop` (+7 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=703-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=704-2) |
| SCR-M16-03 Tạo nhóm chat (hộp thoại) | — (hộp thoại trong `/messages`) | Người dùng, Mod/Admin | AppHeader · NavBar · PageLayout `--chat` | Tag, TextField, TagInput, Dialog | `SCR-M16-03--default--desktop` (+1 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=712-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=713-2) |
| SCR-M16-04 Thông tin nhóm chat | — (ngăn phải trong `/messages/{id}`) | Thành viên cuộc trò chuyện, Admin nhóm chat | AppHeader · NavBar · PageLayout `--chat` | TextField, ListItem, UserRow, Drawer | `SCR-M16-04--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=715-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=716-2) |
| SCR-M16-05 Xin gia nhập nhóm chat qua link mời | `/chat-invite/{mã}` | Người dùng | AppHeader · NavBar · PageLayout `--two` | SectionCard | `SCR-M16-05--default--desktop` (+3 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=427-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=428-2) |
| SCR-M16-06 Thêm thành viên vào nhóm chat (hộp thoại) | — (hộp thoại trong `/messages/{id}`) | Thành viên cuộc trò chuyện, Admin nhóm chat | AppHeader · NavBar · PageLayout `--chat` | TextField, ListItem, UserRow, Dialog | `SCR-M16-06--default--desktop` (+2 trạng thái) | [sáng](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=720-2) · [tối](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=721-2) |
