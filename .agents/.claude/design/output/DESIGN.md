---
ma_tai_lieu: DESIGN
phien_ban: 0.10
trang_thai: Bản nháp
ngay: 2026-11-26
tac_gia: Phạm Văn Đức
steps_completed: [1, 2, 3, 4, 5, 6, 7]
buoc_hien_tai: 8
che_do: thuc-thi
dot_da_duyet: [A, B, C, D, E]
dot_da_day_figma: [A, B, C, D, E]
canvas_kham_pha: https://claude.ai/artifact/K2ZxJDPyzjGKHCw8rZZKrs
canvas_giao_dien: https://claude.ai/artifact/HAykztXFcJbkAiSCXKvift
design_system: https://claude.ai/artifact/VhNBYBjrD4Rng8CtynS7pp
figma_file: https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m
---
# Thiết kế giao diện — iShare (DESIGN.md)

[Vietnamese Doc] — Trạng thái quy trình (frontmatter) và mọi quyết định thiết kế. Đọc tệp này đầu tiên khi tiếp tục.
`che_do`: `kham-pha` (bước 1–5) hoặc `thuc-thi` (từ cuối bước 6).

## 1. Tóm tắt

| Mục | Giá trị |
|---|---|
| Bước hiện tại | 8 — Kiểm tra toàn bộ |
| Hướng thẩm mỹ | "Sổ tay" (DD-UI-08) |
| Số màn hình / artboard | 75 màn hình; 281 artboard sáng + 75 tối = 356 (screen-inventory.md, DD-UI-14, DD-UI-15) |
| Đợt đã duyệt | A, B, C, D, E — đã đẩy sang Figma "iShare — UI" (5 page, 356 frame) |

## 2. Hướng thẩm mỹ đã chọn (bước 3)

- **Tên:** Sổ tay
- **Ý tưởng gốc:** Trang vở ghi gọn gàng của học sinh: bố cục 3 cột rõ ràng, giữ tinh thần "đơn giản, trực quan" người
  dùng thích ở R-01 nhưng không sao chép (AP-P-01); màu xanh ngọc lá dịu, góc gần vuông như mép giấy. Hợp với cảm xúc
  "gọn gàng, đáng tin, có chất học trò" và tránh "trẻ con, rối, lạnh lùng kiểu công nghệ" (PRODUCT.md mục 6).
- **Token plan sơ bộ** (bước 6 mới chốt):
  - Màu — bộ "Xanh ngọc lá". Sáng: nền `#f5f5f1`, bề mặt `#ffffff`, chữ `#1f2523`, chữ phụ `#5a6360`, kẻ mảnh `#e2e3dd`,
    kẻ đậm/viền ô nhập `#828a86`, chủ đạo `#2a6f63`, chữ trên chủ đạo `#ffffff`, nền nhấn nhạt `#e3efec`. Tối: nền
    `#101514`, bề mặt `#171e1c`, chữ `#e6ece9`, chữ phụ `#a6b2ad`, kẻ mảnh `#2a3431`, kẻ đậm `#6e7c77`, chủ đạo
    `#7cc3b4`, chữ trên chủ đạo `#0c1a17`, nền nhấn nhạt `#1c2b28`. Mọi cặp chính đạt WCAG AA ở cả hai theme.
  - Chữ — một họ Be Vietnam Pro (400/600/700). Thang tạm: 30 tiêu đề bài · 26 tiêu đề trang · 22 tiêu đề mục ·
    19 tiêu đề thẻ bài, ô tiêu đề · 17 nội dung bài (dòng 1.7) · 16 bình luận · 15 giao diện · 14 phụ · 13 ghi chú.
  - Hình khối — bo góc 2px cho khối, nút, ô nhập, chip; ngoại lệ: ô tìm kiếm bo tròn hai đầu, avatar tròn. Viền 1px,
    không đổ bóng.
  - Mật độ — vừa. Bố cục máy tính 1440: thanh trên cùng; lưới 200 (điều hướng) | nội dung | 260 (cột phụ) khi trang có
    nội dung phụ, hoặc 200 | nội dung tối đa 820.
- **Điểm nhận diện có chủ đích:** chữ "iShare" với "Share" màu chủ đạo; Upvote nổi bật trong thanh thao tác trơn chỉ bằng
  màu chủ đạo, chữ đậm và icon nét dày; góc 2px nhất quán, chỉ ô tìm kiếm bo tròn; dòng trích tên và đầu bình luận khi
  trả lời.
- **Phần trộn từ hướng khác:** bộ màu "Xanh ngọc lá", ô tìm kiếm bo tròn và thanh thao tác dưới bài lấy từ hướng 2;
  bo góc 2px lấy từ hướng 3.
- **Lý do chọn:** người dùng chọn ngày 2026-11-24 (Q3-01): lấy thiết kế hướng 1, tùy biến màu, ô tìm kiếm, bo góc theo
  hướng 2 và 3; xem thử trên 4 màn hình (chi tiết bài, trang chủ, hồ sơ, viết bài) rồi duyệt.

Các hướng bị loại:

| Hướng | Lý do loại | Artboard |
|---|---|---|
| Hướng 2 — Bảng tin | Người dùng chỉ lấy bộ màu, ô tìm kiếm và thanh thao tác; không lấy bố cục thẻ và cặp chữ Bricolage Grotesque + Source Sans 3 | `huong-2--chi-tiet-bai--desktop[--dark]` |
| Hướng 3 — Giấy kiểm tra | Người dùng chỉ lấy bo góc 2px; không lấy chữ có chân, bố cục một cột, màu mực xanh + đỏ | `huong-3--chi-tiet-bai--desktop[--dark]` |

Artboard của hướng đã chọn: `huong-4--{chi-tiet-bai,trang-chu,ho-so,viet-bai}--desktop[--dark]` (trang "Hướng đã
chọn — 4 màn hình" trên canvas khám phá).

## 3. Tokens tóm tắt (bước 6)

Nguồn sự thật: `tokens/tokens.json` (định dạng Design System của Claude Design; `tokens.css`, `tokens.dtcg.json` sinh bằng
`export_tokens.py`). Design system: "iShare Design System" (link ở frontmatter), bản sao trong `canvas/design-system/`.

- Font: **Be Vietnam Pro** 400/600/700 có nghiêng cho giao diện và nội dung; **JetBrains Mono** cho code, tắt ký tự ghép
  (DD-UI-29). Tệp WOFF2 (OFL) nằm trong design system.
- Thang chữ: `display` 30/1.3 · `h1` 26/1.3 · `h2` 22/1.45 · `h3` 19/1.5 · trong bài `post-h1` 22, `post-h2` 19, `post-h3`
  17 đậm · `body` 17/1.7 · `body-comment` 16/1.6 · `ui`, `label` 15/1.5 · `body-sm` 14/1.5 · `caption` 13/1.5 · `code` 15/1.6
  (DD-UI-33).
- Màu: lớp gốc `neutral-0…950`, `teal-50…950` (giá trị bước 3); ngữ nghĩa `bg`, `surface`, `surface-raised`,
  `surface-hover`, `ink`, `ink-muted`, `line`, `line-strong`, `primary` (+ `primary-hover`, `on-primary`, `primary-soft`),
  `focus`; trạng thái `success`, `warning`, `danger`, `info` + `*-soft`, `danger-hover`, `on-danger`; nội dung bài `mark`,
  `syntax-*`; biểu đồ `chart-1…3`; `scrim` (DD-UI-32). `contrast.py`: 51 cặp × 2 theme = 102 phép kiểm, 0 trượt.
- Mật độ: vừa cho màn hình học sinh (`control-h` 40, `row-h` 52, chữ 15); gọn cho khu kiểm duyệt và quản trị
  (`control-h-sm` 32, `row-h-sm` 38, chữ 14) (DD-UI-30). Thang khoảng cách 4px: `space-0-5` 2 … `space-16` 64.
- Khung quản trị (DD-UI-42): `console-bg`, `console-hover`, `console-active`, `console-ink`, `console-ink-muted`, `console-accent`, `console-line`.
- Bố cục: `topbar-h` 64, `nav-w` 200 (khu quản trị `nav-w-wide` 240), `aside-w` 260, `content-max` 820, `drawer-w` 420,
  `dialog-w` 520, `inbox-w` 340 (cột hộp thư Chat, DD-UI-40).
- Bo góc: `radius-sm` 2px cho mọi khối; `radius-full` cho ô tìm kiếm, avatar, số đếm, công tắc, thanh kết quả bình chọn.
- Bóng: khối nội dung không bóng (viền `line`); `shadow-1` cho menu, popover, toast, tooltip; `shadow-2` cho dialog, ngăn
  trượt; lớp nổi không kèm viền (DD-UI-34).
- Chuyển động (không có nhóm token, ghi ở đây và đầu `bundle.css`): nhanh 120ms (hover, focus, nút), vừa 200ms (menu,
  popover, toast, tab), chậm 280ms (dialog, ngăn trượt); vào `cubic-bezier(0.2, 0, 0, 1)`, ra `cubic-bezier(0.4, 0, 1, 1)`;
  `prefers-reduced-motion: reduce` tắt mọi chuyển động (DD-UI-34).
- Bộ icon: **Material Symbols Sharp** weight 400 (Google, Apache-2.0, gói `@material-symbols/svg-400@0.48.3`), lưới 24,
  cỡ `icon` 24 / `icon-sm` 20 / `icon-xs` 16, tô bằng màu chữ; bản `-fill` cho trạng thái đang bật; Upvote nét dày dùng bản
  weight 600 (DD-UI-11, DD-UI-28). 84 icon trong nhóm tài sản Icons của design system.

## 4. Component (bước 6)

68 component (62 ở DD-UI-31 + 5 component bố cục ở DD-UI-40 + AdminShell ở DD-UI-42). Mỗi component có `README.md` và `preview.html` (mọi trạng thái, cả hai theme) trong design system;
class `is-*` trong `components/bundle.css`. Trạng thái tương tác chung cho phần tử bấm được: mặc định, rê chuột, focus
(vòng `focus` 2px), đang nhấn, tắt; cột "Trạng thái" chỉ ghi phần riêng.

| Component | Biến thể | Trạng thái | Ghi chú |
|---|---|---|---|
| Button | chính, phụ, nhẹ, nguy hiểm, chữ chính, chữ phụ; cỡ 40/32 | đang xử lý (`aria-busy`) | tối đa một nút chính mỗi vùng; hai kiểu chữ chỉ dùng trong EmptyState, ErrorState (DD-UI-36) |
| IconButton | trong suốt, có viền; cỡ 40/32; có Counter | đang bật/đang mở (`aria-pressed`, `aria-expanded`) | luôn có `aria-label` |
| Link | thường (gạch chân), trầm | — | trong đoạn văn luôn gạch chân |
| GoogleButton | một dạng | đang chuyển sang Google | logo G của Google giữ nguyên màu (tài sản Google) |
| TextField | thường, mật khẩu (hiện/ẩn), chỉ đọc + Sao chép; cỡ nhỏ | lỗi, chỉ đọc, bộ đếm ký tự | nhãn luôn hiện, lỗi cạnh ô |
| TextArea | một dạng | lỗi, bộ đếm, vượt giới hạn | bio ≤155, banner ≤200 ký tự |
| Select | vừa, nhỏ | lỗi | `<select>` thật |
| Checkbox | đơn, nhóm | đã chọn | `accent-color: primary` |
| Radio | nhóm có `legend` | đã chọn | — |
| Switch | có/không dòng mô tả | bật, tắt hẳn khi đang bật | hiệu lực ngay, không cần Lưu |
| FileDrop | một dạng | đang kéo tệp vào, lỗi | luôn có nút Chọn tệp (QF-10) |
| SearchField | thanh trên cùng | có chữ (nút Xóa), mở gợi ý | bo tròn hai đầu, tối đa 560px |
| TagInput | Tag, Chủ đề (có Gợi ý chủ đề của AI) | đủ số lượng, lỗi thiếu Chủ đề | Gợi ý ẩn khi AI tắt; chip dài xuống dòng trong chip, không tràn ô |
| SegmentedControl | 2–5 lựa chọn | đã chọn | khoảng thời gian Thống kê, sắp xếp bình luận |
| Combobox | nhóm gợi ý, lịch sử | mục đang trỏ, không có gợi ý, lỗi giới hạn tần suất | mẫu combobox ARIA |
| DateTimeField | một dạng | lỗi hạn trước hiện tại | hạn kết thúc bình chọn |
| AvatarUpload | chưa có ảnh, có ảnh | lỗi định dạng/dung lượng | xem trước tròn |
| Avatar | 28/40/96; chữ cái đầu; ẩn danh, đã xóa | — | — |
| Tag | liên kết, có nút gỡ, đã vô hiệu hóa | — | có dấu # |
| TopicChip | liên kết, tĩnh, gợi ý (nét đứt) | — | nền `primary-soft` |
| GradeLabel | một dạng | — | "Lớp 10/11/12" |
| Badge | huy hiệu + ngày đạt; Ngôi sao tuần | — | tiết chế (DD-UI-05), không hiện tiến độ |
| Counter | nhấn mạnh, trầm; chấm chưa đọc | 99+, ẩn khi 0 | `aria-hidden`, số nằm trong nhãn nút |
| StatusLabel | success, warning, danger, info, trung tính, chỉ chữ | — | luôn có chữ (QF-03) |
| PostCard | thường, trong nhóm, ẩn danh, có nhãn trạng thái | rê chuột | số liệu chỉ để xem (DD-UI-13); cấp tiêu đề theo ngữ cảnh: h2 ngay dưới h1, h3 trong mục có h2 (QF-17) |
| PostBody | đầu bài + nội dung giàu định dạng | trạng thái bài qua StatusLabel, InlineAlert | BR-M03-03, KaTeX, tô màu cú pháp |
| ActionBar | một dạng | đã upvote, đã lưu, bài của mình, dưới 300 từ, bình luận đã khóa | DD-UI-10, DD-UI-11 |
| UpvoteButton | bài viết, bình luận (nhỏ) | đã upvote, tắt với nội dung của mình | nét dày khi chưa bấm |
| Poll | chọn một, chọn nhiều | chưa bình chọn, đã bình chọn, đã kết thúc | thanh kết quả có chữ % |
| PollEditor | bài nháp, bài đã đăng | lỗi số lựa chọn, hạn | 3 thao tác riêng ở bài đã đăng |
| Attachment | ảnh, tài liệu | đang tải lên, lỗi | dung lượng kiểu Việt Nam |
| Comment | bình luận gốc, trả lời có dòng trích | đã chỉnh sửa, đã bị gỡ | avatar cạnh tên (DD-UI-12) |
| ListItem | liên kết, tĩnh có nút; vừa/gọn | đang chọn | Chủ đề, lịch sử sửa, danh sách chặn |
| UserRow | theo ngữ cảnh thao tác; nhãn vai trò | tài khoản bị khóa, đã xóa | — |
| GroupCard | Public, Private | Tham gia / Gửi yêu cầu / Rút yêu cầu / Đã tham gia, bị khóa | số thành viên một dòng, nút xuống hàng khi thiếu chỗ; cấp tiêu đề theo ngữ cảnh |
| LeaderboardRow | có/không Ngôi sao tuần | người đang xem, đã xóa | không cúp, không vàng bạc đồng |
| NotificationItem | người, hệ thống; có nút Chấp nhận/Từ chối | chưa đọc, hết hạn | giọng tôn trọng khi xử lý |
| ConversationItem | 1-1, nhóm chat | chưa đọc, đang mở, tắt popup | tên và tin gần nhất một dòng, cắt bằng dấu "…" |
| MessageBubble | đến, đi, hệ thống; dải ngày | đã xem, đã thu hồi, có tin mới | `role="log"` |
| NewMessagePopup | một dạng | — | `role="status"`, không cướp focus |
| DataTable | gọn (mặc định khu quản trị), vừa | sắp xếp, rê chuột, đang chọn, trống, đang tải | `table` thật, cuộn ngang trong khung |
| FilterBar | Select, Checkbox, chip bộ lọc | có bộ lọc khác mặc định | — |
| StatTile | lưới 3 cột | 0, chưa có dữ liệu, đang tải | M15 |
| TrendChart | 1–3 chuỗi chồng | trống, đang tải | `chart-1…3` + bảng số liệu |
| Toast | success, info, warning, danger; có nút | — | lỗi không tự ẩn |
| InlineAlert | 4 tone; có nút | — | chờ duyệt, bị từ chối, cảnh cáo |
| Banner | info, warning | văn bản dài | banner Admin ≤200 ký tự |
| EmptyState | có/không nút | — | không minh họa, không mascot; nút chữ đậm, không nền, không viền (DD-UI-36); cấp tiêu đề theo ngữ cảnh |
| Skeleton | dòng, tiêu đề, avatar | — | đứng yên khi giảm chuyển động |
| ErrorState | không tìm thấy, không có quyền, lỗi, bảo trì | — | câu theo SC; căn giữa như EmptyState, nút chữ đậm (DD-UI-36) |
| AppHeader | đã đăng nhập, Guest | — | DD-UI-20 |
| NavBar | người dùng (200px), khu quản trị `--console` (240px, nền sẫm, trong AdminShell) | mục đang xem | DD-UI-21, DD-UI-42 |
| PageLayout | ba cột, hai cột (`--two`), quản trị (`--admin`, `--admin3`, nằm trong AdminShell), chat (`--chat`), giữa trang (`--center`) | — | khung cột dưới AppHeader; mọi màn hình dùng một biến thể (DD-UI-40) |
| AdminShell | Admin (hai nhóm menu), Mod (chỉ nhóm Kiểm duyệt) | mục menu đang xem, rê chuột | khung riêng của khu kiểm duyệt và quản trị: cột menu nền sẫm có logo, thanh trên chỉ có vị trí trang, Về iShare, chuông, avatar; nội dung trải hết bề ngang (DD-UI-42) |
| PageHeader | đầu trang (`is-h1`), đầu khu vực (`is-h2`), đầu khối nhỏ (`is-label`) | — | tiêu đề trái, hành động phải (DD-UI-40) |
| SectionCard | thường, gọn (`--compact`, cột phụ) | — | khối giấy trên nền trang (DD-UI-40) |
| TableOfContents | một dạng | mục đang đọc | "Trong bài này", trang chính sách (DD-UI-40) |
| DescriptionList | thường; `--stack` cho cột phụ hẹp (nhãn nằm trên giá trị) | — | cặp nhãn – giá trị (DD-UI-40) |
| Tabs | tab chính, mục con, có số | đã chọn | trạng thái vào URL khi FR có |
| Dialog | thường, rộng, nguy hiểm | — | giữ focus, Esc đóng (QF-06) |
| Drawer | một dạng | đang tải, lỗi | Tóm tắt, thông tin nhóm chat, vai trò |
| Menu | thường, có icon, đang bật, nguy hiểm; đầu menu | mục tắt | mục không có quyền thì không hiện |
| Popover | ngăn thông báo | trống, đang tải | "Xem tất cả" ở chân |
| Tooltip | một dạng | — | không chứa nội dung tương tác |
| Pagination | Tải thêm, trang số | đang tải, đã hết | — |
| StepIndicator | 3 bước đăng ký | đã xong, hiện tại, chưa tới | `aria-current="step"` |
| EditorToolbar | bài viết (BR-M03-03), bình luận (BR-M04-01) | đang áp dụng, tắt | chỉ định dạng FR cho phép |
| CommentComposer | bình luận, trả lời có dòng trích, chat; vùng soạn bài | vượt 1.000 từ, bình luận đã khóa | tự giãn theo nội dung rồi cuộn trong ô (DD-UI-37) |

## 5. Quyết định thiết kế

| Mã | Quyết định | Lý do | Nguồn / câu hỏi | Bước | Ngày |
|---|---|---|---|---|---|
| DD-UI-01 | Hỗ trợ hai theme sáng và tối từ MS1; mọi cặp màu kiểm tương phản ở cả hai theme | Người dùng yêu cầu | Q1-04 | 1 | 2026-11-24 |
| DD-UI-02 | Thiết kế cho máy tính: artboard desktop rộng 1440, bố cục co giãn không vỡ ở 1280; chưa vẽ bản điện thoại | Người dùng ưu tiên máy tính; điện thoại chưa cần ở giai đoạn này | Q1-05, Q1-07 | 1 | 2026-11-24 |
| DD-UI-03 | Logo tạm là chữ "iShare" (wordmark), không có biểu tượng riêng | Chưa có nhận diện thương hiệu | Q1-01 | 1 | 2026-11-24 |
| DD-UI-04 | Thuật ngữ hiển thị: giữ "Tag", "Upvote"; Việt hóa "Chủ đề" (Topic), "Huy hiệu" (Badge); bốn tab trang chủ "Thịnh hành / Đang theo dõi / Nhóm / Mới nhất" | Học sinh quen "Tag", "Upvote"; phần còn lại có từ tiếng Việt tự nhiên | PRODUCT.md câu hỏi mở #3 | 1 | 2026-11-24 |
| DD-UI-05 | Gamification (điểm, huy hiệu, Ngôi sao tuần, bảng xếp hạng) trình bày tiết chế: gọn, không màu mè, không mascot | Cảm xúc "không muốn: trẻ con" (PRODUCT.md mục 6) | Q3-02 | 2 | 2026-11-24 |
| DD-UI-06 | Vị trí Upvote: chấp nhận cột trái cạnh nội dung (kiểu R-01) hoặc thanh hành động dưới bài (kiểu R-12); thử cả hai ở bước 3 rồi chốt | Người dùng chấp nhận cả hai | Ý kiến bước 2 | 2 | 2026-11-24 |
| DD-UI-07 | Bước 3: hai hướng dùng hai sắc xanh lá nhẹ khác nhau + một hướng màu khác để đối chứng; thêm một bảng nhiều bộ màu áp lên cùng một mẫu nhỏ để chọn màu độc lập với bố cục | Người dùng thích xanh lá nhẹ; muốn xem thêm vài bộ màu | Ý kiến bước 2 | 2 | 2026-11-24 |
| DD-UI-08 | Hướng thẩm mỹ "Sổ tay": khung hướng 1 (3 cột, Be Vietnam Pro), bộ màu "Xanh ngọc lá" của hướng 2, bo góc 2px của hướng 3 | Người dùng chọn | Q3-01 | 3 | 2026-11-24 |
| DD-UI-09 | Ô tìm kiếm bo tròn hai đầu, rộng tối đa 560px, nằm giữa khoảng từ logo đến nhóm nút bên phải (không căn giữa trang) | Người dùng yêu cầu | Ý kiến bước 3 | 3 | 2026-11-24 |
| DD-UI-10 | Upvote bài viết nằm trong thanh thao tác dưới bài, thứ tự Upvote · Bình luận · Tóm tắt · Lưu, Báo cáo ở cuối thanh. Chốt DD-UI-06 | Người dùng chọn | Ý kiến bước 3 | 3 | 2026-11-24 |
| DD-UI-11 | Upvote là nút trơn như các nút bên cạnh (không viền, không nền), nổi bật bằng màu chủ đạo, chữ đậm, icon nét dày; đã upvote thì icon tô đặc. Upvote bình luận làm cùng cách | Người dùng yêu cầu; trạng thái đã upvote do Claude đề xuất, duyệt cùng bước 3 | Ý kiến bước 3 | 3 | 2026-11-24 |
| DD-UI-12 | Bình luận và trả lời có avatar tròn cạnh tên người viết | Người dùng yêu cầu | Ý kiến bước 3 | 3 | 2026-11-24 |
| DD-UI-13 | Danh sách bài (trang chủ, hồ sơ): thẻ có trích đoạn 2 dòng; số upvote và bình luận chỉ để xem, không bấm upvote tại danh sách. Trang chủ không có cột phụ vì FR-M14 không có nội dung phụ cho trang chủ | Claude đề xuất, duyệt cùng bước 3 | — | 3 | 2026-11-24 |
| DD-UI-14 | Vẽ hết 75 màn hình trong danh mục, không để màn hình nào sau MS1; 5 đợt theo thứ tự A → B → C → D → E | Người dùng chọn | Q4-01, Q4-02 | 4 | 2026-11-25 |
| DD-UI-15 | Theme tối: sản phẩm hỗ trợ mọi màn hình, mọi trạng thái (màu từ tokens). Artboard `--dark` chỉ vẽ cho trạng thái `default` của mỗi màn hình (75); bước 6 kiểm tương phản mọi cặp màu ở cả hai theme; bước 8 tự bật theme tối cho mọi trạng thái còn lại để soát | Người dùng đồng ý đề xuất | PRODUCT.md câu hỏi mở #4 | 4 | 2026-11-25 |
| DD-UI-16 | Nút Theo dõi / Bỏ theo dõi Chủ đề đặt ở Danh sách Chủ đề và ở đầu trang Kết quả tìm kiếm khi lọc theo đúng một Chủ đề | Nguồn có thao tác (SC-M07-001) nhưng không nói nơi đặt; người dùng đồng ý đề xuất | screen-inventory.md câu hỏi #1 | 4 | 2026-11-25 |
| DD-UI-17 | Trang Cài đặt tài khoản (mở từ menu avatar) gom: đổi mật khẩu, mức cảnh cáo của mình, từ chức (Mod/Admin), vô hiệu hóa tài khoản | Nguồn không nói nơi đặt; người dùng đồng ý | screen-inventory.md câu hỏi #2 | 4 | 2026-11-25 |
| DD-UI-18 | Gỡ ban: Mod/Admin xem hồ sơ tài khoản đang bị ban có nút Gỡ ban (SC-M08-011: gỡ trực tiếp trên tài khoản, không qua vụ) | Người dùng đồng ý | screen-inventory.md câu hỏi #3 | 4 | 2026-11-25 |
| DD-UI-19 | Mẫu email hệ thống (xác minh, đặt lại mật khẩu, mã kích hoạt, ban/gỡ ban, thông báo qua email) chưa nằm trong phạm vi vẽ; định dạng email quyết sau | Người dùng hoãn | screen-inventory.md câu hỏi #5 | 4 | 2026-11-25 |
| DD-UI-20 | Thanh trên cùng (desktop): chữ "iShare" về `/` · ô tìm kiếm nằm giữa logo và nhóm nút (DD-UI-09) · Viết bài · chuông Thông báo · Tin nhắn có số chưa đọc · avatar → menu Hồ sơ, Cài đặt tài khoản, Khiếu nại của tôi, Khu kiểm duyệt (Mod/Admin), Đăng xuất. Guest thấy Đăng nhập, Đăng ký thay cho chuông, tin nhắn, avatar | Claude đề xuất, người dùng duyệt ở bước 5 | flows.md mục 2 | 5 | 2026-11-25 |
| DD-UI-21 | Cột trái 200px: Trang chủ · Chủ đề · Nhóm · Bảng xếp hạng (mục đang xem tô nền nhạt); Tin nhắn không lặp ở cột trái. Dòng chân cuối cột trái dẫn tới Privacy Policy/ToS (SC-M01-037) | Claude đề xuất, người dùng duyệt ở bước 5 | flows.md mục 2 | 5 | 2026-11-25 |
| DD-UI-22 | Khu kiểm duyệt và quản trị: vào từ mục "Khu kiểm duyệt" trong menu avatar; giữ thanh trên cùng, cột trái đổi sang menu quản trị (nhóm Kiểm duyệt cho Mod và Admin, nhóm Quản trị chỉ Admin) và có lối "Về iShare" | Claude đề xuất (nguồn không nói lối vào), người dùng duyệt ở bước 5 | flows.md mục 2, mục 4 #1 | 5 | 2026-11-25 |
| DD-UI-23 | Vị trí cố định: Thông báo (chuông → ngăn 10 thông báo → "Xem tất cả" `/notifications`); Chat (biểu tượng → `/messages`, popup tin mới góc dưới phải); Báo cáo (cuối thanh thao tác bài, menu "…" của bình luận, hồ sơ, trang nhóm); Khiếu nại (nút trong thông báo xử lý, màn hình tài khoản bị khóa, menu avatar → Khiếu nại của tôi) | Claude đề xuất, người dùng duyệt ở bước 5 | flows.md mục 2; QF-16 | 5 | 2026-11-25 |
| DD-UI-24 | Thao tác ngắn mở hộp thoại giữa màn hình (nền mờ, đóng bằng Esc hoặc nút Đóng); nội dung xem kèm trang mở ngăn trượt bên phải, không rời trang (Tóm tắt bài, thông tin nhóm chat, vai trò người dùng) | Claude đề xuất, người dùng duyệt ở bước 5 | flows.md mục 2 | 5 | 2026-11-25 |
| DD-UI-25 | Wireframe bước 5 chỉ xám, một font hệ thống trung tính, không màu, không ảnh, không bóng; ngoại lệ AP-10 phạm vi `wf--*` (mục 6.1) | Theo bước 5 của skill (wireframe không mang bản sắc); người dùng duyệt ở bước 5 | steps/05 mục 5 | 5 | 2026-11-25 |
| DD-UI-26 | Quy tắc đường dẫn: chữ thường tiếng Anh ngắn, không dấu; tiền tố một chữ cái cho đối tượng có trang riêng (`/p/` bài, `/u/` người dùng, `/g/` nhóm); trạng thái cần chia sẻ (tab, bộ lọc, chu kỳ) nằm trong query string; khu kiểm duyệt `/mod/…` (Mod, Admin), khu chỉ Admin `/admin/…`; hộp thoại, ngăn trượt, popup không có đường dẫn riêng. `/u/{username}` giữ đúng FR-M02 | Người dùng đồng ý đề xuất | Q5-02; flows.md mục 1 | 5 | 2026-11-25 |
| DD-UI-27 | Prototype bấm được làm sau khi xong thiết kế hi-fi (nối artboard hi-fi), không nối wireframe bước 5 | Người dùng chọn | Câu hỏi prototype ở bước 5 | 5 | 2026-11-25 |
| DD-UI-28 | Bộ icon Material Symbols Sharp (weight 400, Apache-2.0) cho toàn giao diện, lưới 24, cỡ 24/20/16; bản tô đặc cho trạng thái đang bật; Upvote chưa bấm dùng bản weight 600 — ngoại lệ duy nhất về độ dày nét theo DD-UI-11 | Người dùng chọn (bộ B) | Q6-04; artboard `b6--bo-icon--desktop` | 6 | 2026-11-25 |
| DD-UI-29 | Font code JetBrains Mono (OFL, có bộ chữ tiếng Việt), tắt ký tự ghép để `=>`, `!=` hiện đúng ký tự; font giao diện và nội dung giữ Be Vietnam Pro (DD-UI-08) | Người dùng đồng ý đề xuất | Q6-01; artboard `b6--font-mono--desktop` | 6 | 2026-11-25 |
| DD-UI-30 | Mật độ: vừa cho màn hình học sinh (nút, ô nhập 40px, dòng 52px, chữ 15px); gọn cho khu kiểm duyệt và quản trị (nút, bộ lọc 32px, dòng bảng 38px, chữ 14px) | Người dùng đồng ý đề xuất | Q6-02; artboard `b6--mat-do--desktop` | 6 | 2026-11-25 |
| DD-UI-31 | Bộ component lõi 62 cái: danh sách mặc định của skill (bỏ BottomNav vì không có điện thoại) + thêm theo danh mục màn hình và FR: TagInput, SegmentedControl, StatusLabel, ActionBar, PollEditor, UserRow, GroupCard, LeaderboardRow, NotificationItem, ConversationItem, MessageBubble, NewMessagePopup, DataTable, FilterBar, StatTile, TrendChart, StepIndicator, và sau khi rà lại: GoogleButton, AvatarUpload, Combobox, DateTimeField, Popover, ListItem | Người dùng duyệt danh sách 56, giao rà lại; Claude thêm 6 component có nguồn | Q6-05; mục 4 | 6 | 2026-11-25 |
| DD-UI-32 | Màu thêm ở bước 6 (giữ nguyên 18 giá trị của bước 3): `surface-raised`, `surface-hover`, `primary-hover`; trạng thái `success` (= màu chủ đạo, lệch xanh dương), `warning` nâu hổ phách, `danger` đỏ cam, `info` xanh dương + nền nhạt, `danger-hover`, `on-danger`; `mark` vàng nhạt; `syntax-*`; `chart-1…3` thang một sắc theo độ sáng; `scrim` | Claude đề xuất, người dùng duyệt ở bước 6 | contrast-pairs.csv; FR-M15-03.04 (3 chuỗi); BR-M03-03 (tô sáng, tô màu cú pháp) | 6 | 2026-11-25 |
| DD-UI-33 | Thang chữ chốt từ thang tạm bước 3 + tiêu đề mục trong bài `post-h1/2/3` (22/19/17 đậm, dùng lại cỡ của thang) | Claude đề xuất, người dùng duyệt ở bước 6 | BR-M03-03 (H1–H3 trong bài) | 6 | 2026-11-25 |
| DD-UI-34 | Bóng chỉ cho lớp nổi (`shadow-1` menu/popover/toast/tooltip, `shadow-2` dialog/ngăn trượt), không kèm viền; chuyển động 120/200/280ms, không nảy, tắt khi giảm chuyển động | Claude đề xuất, người dùng duyệt ở bước 6 | AP-31, QF-11 | 6 | 2026-11-25 |
| DD-UI-35 | Khu kiểm duyệt và quản trị dùng cột điều hướng rộng 240px (`nav-w-wide`) vì nhãn mục dài; cột của người dùng giữ 200px (DD-UI-21) | Claude đề xuất, người dùng duyệt ở bước 6 | Wireframe khu quản trị bước 5 | 6 | 2026-11-25 |
| DD-UI-36 | Trang trống và trang lỗi: nội dung căn giữa (ErrorState căn giữa như EmptyState, gồm cả trang bảo trì SCR-SHARED-03); nút dạng chữ, không nền, không viền, chữ đậm 700 — việc chính màu chủ đạo (`is-btn--text-primary`), việc phụ màu chữ chính (`is-btn--text`); rê chuột hiện nền nhạt; nút nguy hiểm giữ nguyên | Người dùng yêu cầu khi duyệt gộp đợt A–E | Ý kiến duyệt SCR-SHARED-04 | 7 | 2026-11-26 |
| DD-UI-37 | Ô soạn tự giãn theo nội dung, không có tay kéo: bình luận, trả lời cao 3 dòng, giãn tới 10 dòng rồi cuộn trong ô; chat 1 dòng, giãn tới 5 dòng; vùng soạn bài cao 280px, giãn tới 560px rồi cuộn trong ô để thanh công cụ luôn nhìn thấy. Lập trình: `field-sizing: content`, trình duyệt chưa hỗ trợ thì đặt chiều cao theo `scrollHeight` | Người dùng yêu cầu; mức giới hạn do Claude đề xuất, người dùng đồng ý (giữ trần 560px cho vùng soạn bài, chat cũng tự giãn) | Ý kiến duyệt ô bình luận, trình soạn | 7 | 2026-11-26 |
| DD-UI-38 | Ô Lớp/Khối trong trình soạn bài dùng Select (Không chọn, Lớp 10, Lớp 11, Lớp 12) thay cho nút chọn đoạn của màn hình mẫu bước 3, vì nút chọn đoạn không vừa cột phải 260px | Claude đề xuất, người dùng duyệt | QA-A-04 | 7 | 2026-11-26 |
| DD-UI-39 | Trang kích hoạt lại hiện số lần nhập mã còn lại ("Bạn còn N lần thử", đếm từ 5 theo BR-M01-22); sai lần thứ 5 thì hiện trạng thái mã hết hiệu lực | Claude đề xuất, người dùng duyệt | QA-dot-E câu hỏi 2 | 7 | 2026-11-26 |
| DD-UI-40 | Khối lặp lại thành component của design system: PageLayout (6 biến thể bố cục chung), PageHeader, SectionCard, TableOfContents, DescriptionList; kiểu chữ tiêu đề `is-h1`, `is-h2`, `is-label`; PostBody thêm bản nhỏ `is-prose--sm`; token mới `inbox-w` 340px cho cột hộp thư Chat. Artboard dùng class của design system, `<helmet>` chỉ còn lớp riêng của artboard (khung cắt, lớp phủ, khung mục lục canvas) | Claude đề xuất (QA-dot-A mục 5), người dùng đồng ý: "khối lặp lại chuyển thành component, làm sao dễ quản lý" | QA-dot-A câu hỏi 2 | 7 | 2026-11-26 |
| DD-UI-41 | Bản Figma "iShare — UI" là bản lưu, canvas là nguồn gốc (không sửa trên Figma). Mỗi artboard đẩy bằng `html_to_figma` từ bản HTML tự chứa (font nhúng); chỉ trong bản Figma: công thức MathML chuyển thành chữ Unicode (dòng) hoặc phân số dựng bằng HTML (khối), nhãn trục biểu đồ đặt lại font Be Vietnam Pro, số dòng của từng đoạn chữ chỉnh khớp với trình duyệt (ô nhập một dòng thì cắt phần thừa như trình duyệt); mỗi page một đợt, mỗi màn hình một hàng có nhãn, frame tên theo artboard | Claude đề xuất cách đẩy; người dùng duyệt chất lượng đợt A và cho đẩy hết: "cứ đẩy hết đi nhé" | Q7-03 | 7 | 2026-11-26 |
| DD-UI-42 | Khu kiểm duyệt và quản trị dùng khung riêng AdminShell, thay phần "giữ thanh trên cùng, đổi cột trái" của DD-UI-22 và cột menu của DD-UI-35: cột menu nền sẫm `console-bg` cao hết trang, logo vẫn là "iShare", mỗi mục có icon, Mod chỉ thấy nhóm Kiểm duyệt; thanh trên riêng chỉ có vị trí trang (nhóm › trang), "Về iShare", chuông Thông báo, avatar, bỏ ô tìm kiếm, Viết bài, Tin nhắn; nội dung trải hết bề ngang (bỏ giới hạn 820px của SectionCard trong khu này). Thêm 7 token màu `console-*` và 3 màu gốc `teal-850`, `teal-875`, `teal-925` (đạt tương phản, 116/116 cặp); component mới AdminShell, NavBar thêm biến thể `--console`. Màn hình phía người dùng của Mod, Admin giữ AppHeader + NavBar | Người review góp ý trang quản trị "vẫn dùng giao diện như của user thường", muốn mẫu riêng chủ yếu là bảng; Claude đề xuất, người dùng chọn phương án khung riêng cho cả Mod và Admin, giữ chữ logo, duyệt 2 màn mẫu (M10-01, M08-02) | QA-dot-C | 8 | 2026-11-26 |
| DD-UI-43 | Dòng chân cột menu (NavBar phía người dùng và NavBar `--console` trong AdminShell) ghi "Chính sách và Điều khoản" thay cho "Privacy Policy/ToS", vẫn dẫn tới trang SCR-M01-09 (SC-M01-037). Cột người dùng 200px: chữ xuống hai dòng "Chính sách và / Điều khoản" (giữ cụm bằng khoảng trắng không ngắt); cột quản trị 240px: một dòng. Tên trang "Privacy Policy/ToS" trong spec và tiêu đề trang giữ nguyên | Người dùng hỏi đổi chữ sang tiếng Việt và chọn "Chính sách và Điều khoản" trong 3 phương án | — | 8 | 2026-11-27 |
| DD-UI-44 | Màn hình bị cảnh cáo (soạn bài SCR-M03-01, khu bình luận SCR-M04-01) có nút "Khiếu nại cảnh cáo này" trong InlineAlert, mở cùng biểu mẫu SCR-M09-01 mà thông báo cảnh cáo dẫn tới (FR-M08-09.05, FR-M08-10.03) | QA-F-08 (QF-16); người dùng đồng ý bổ sung | QA-final | 8 | 2026-11-27 |

## 6. Anti-pattern: ngoại lệ và điều cần tránh riêng

### 6.1 Ngoại lệ đã duyệt

`check_ui.py --design` đọc bảng này: cảnh báo của mã AP trong phạm vi tệp khớp `scope` (mẫu glob trên tên tệp; `*` là
mọi tệp) được hạ xuống INFO. Chỉ thêm dòng khi người dùng đã duyệt.

<!-- ui:ap-exceptions -->
| ap | scope | reason | dd |
|---|---|---|---|
| AP-10 | wf--* | Wireframe bước 5 chỉ xám, dùng font hệ thống trung tính, không mang bản sắc (theo bước 5 của skill) | DD-UI-25 |

### 6.2 Điều cần tránh riêng của dự án (từ bước 2)

<!-- ui:project-avoid -->
| id | avoid | source | reason |
|---|---|---|---|
| AP-P-01 | Sao chép y nguyên hoặc làm giống hệt giao diện của bất kỳ reference nào (bố cục toàn trang, màu, font, icon, logo, khoảng cách đặc trưng); chỉ mượn pattern ghi trong moodboard. Kiểm: đặt cạnh reference, che logo — nhận nhầm là vi phạm | moodboard.md R-01, R-10 và mọi reference | Người dùng cấm tuyệt đối (Q2, 2026-11-24) |

## 7. Dữ liệu mẫu

Dùng chung cho mọi màn hình. Ưu tiên bộ dữ liệu giả lập của SC.

| Mã | Dữ liệu | Nguồn |
|---|---|---|
| MAU-01 | Bài P301 "Giải phương trình bậc hai" — tác giả Phạm Ngọc Lan (@lan_12; hướng 1–3 lỡ ghi @lan_pham), đăng 08/11/2026 08:30, sửa lúc 09:00 và 10:00 theo SC-M03-012, hiển thị "Sửa lần cuối 08/11/2026, 10:00" ("đã chỉnh sửa" + "Xem lịch sử"); Lớp 10; Chủ đề Toán; Tag #daiso, #phuongtrinh; 24 upvote; 5 bình luận. Nội dung 301 từ (đủ ngưỡng nút Tóm tắt), có công thức trong dòng, một công thức khối, danh sách đánh số 3 câu hỏi | SC-M03 D-POST, D-HISTORY; BR-M03-27; FR-M13-07; độ dài bổ sung ở bước 3 |
| MAU-02 | Tệp đính kèm: bang-bien-thien.png (820 KB), de-cuong-on-tap-hk1.pdf (1,2 MB) | Bổ sung ở bước 3 (tên tệp minh họa) |
| MAU-03 | Bình chọn Q301: "Phương pháp thế" / "Phân tích nhân tử" / "Dùng công thức"; chọn một hoặc nhiều; kết quả hiện sau khi bình chọn; kết thúc 10:00, 09/11/2026 | SC-M03 D-POLL |
| MAU-04 | Bình luận gốc: Trần Minh Đức (12 upvote, có công thức) với 2 trả lời — Phạm Ngọc Lan (nhãn "Tác giả", 3 upvote) và Nguyễn Thị Phương Thảo Nguyên (tên dài, 0 upvote); Hà Thu (7 upvote, đã chỉnh sửa); Lê Văn Bình (2 upvote). Trả lời có dòng trích: tên người được trả lời + đầu bình luận | SC-M04 D-ROOT, D-REPLY; BR-M04-04; tên dài bổ sung ở bước 3 |
| MAU-05 | Người đang xem: Mai Anh (chữ tắt MA) | Bổ sung ở bước 3 |
| MAU-06 | Trang chủ, tab Thịnh hành › Bài viết: 6 bài — P301 (Toán học, Lớp 10, 24 upvote, 5 bình luận); "Phân tích nhân vật Mị: mở bài gián tiếp thế này đã ổn chưa?" (Hà Thu, Ngữ văn, Lớp 12, 19/11); "Đề luyện tập hình học không gian tuần này (có lời giải)" (Trần Minh Đức, trong CLB Toán, Lớp 11, 15/4); "Áp lực ôn thi cuối kỳ…" (Ẩn danh, trong CLB Văn, Kỹ năng mềm, Lớp 12, 13/14); "Mẹo nhớ nhanh tính chất các nhóm A…" (Lê Văn Bình, Khoa học tự nhiên (Lý/Hóa/Sinh), Lớp 10, 12/6); "Viết vòng lặp for trong Python…" (Nguyễn Thị Phương Thảo Nguyên, Tin học, Lớp 11, 8/3) | Tên nhóm CLB Toán, CLB Văn và Chủ đề theo SC-M14 D-DIRECTORY, SC-M05 D-CAT; tiêu đề, trích đoạn, số liệu bổ sung ở bước 3 |
| MAU-07 | Hồ sơ Phạm Ngọc Lan do Mai Anh xem: @lan_12, bio "Thích Toán", Lớp 11, tham gia 01/09/2026, 150 điểm, huy hiệu Người mới nổi (đạt 15/09/2026) và Cây bút triển vọng (đạt 28/10/2026), Ngôi sao tuần, 2 người theo dõi, 2 đang theo dõi; tab Bài viết: P301 và 2 bài bổ sung | SC-M02 D-PROFILE (display_name "Lan" được viết dài thành "Phạm Ngọc Lan"; bỏ emoji 📐 trong bio vì check_ui coi emoji là lỗi); ngày đạt huy hiệu bổ sung |
| MAU-08 | Viết bài: nháp P501 "Vận dụng định lý Bayes" của Lan, Lớp 12, Chủ đề Toán học, Tag #bayes #xácsuất, tệp bayes.pdf (1 MB), chưa có bình chọn; nội dung SC kèm một công thức LaTeX dạng mã và một câu ví dụ | SC-M05 D-POST, D-TAG; công thức và câu ví dụ bổ sung ở bước 3 |

## 8. Đề nghị bổ sung (ngoài nguồn — không vẽ)

| # | Đề nghị | Liên quan | Lý do | Trạng thái |
|---|---|---|---|---|

## 9. Lịch sử thay đổi

| Phiên bản | Ngày | Thay đổi |
|---|---|---|
| 0.1 | 2026-11-24 | Tạo tệp ở bước 1; bước 1 được duyệt (DD-UI-01…04); bước 2 được duyệt (AP-P-01, DD-UI-05…07); bước 3: vẽ 3 hướng + bảng màu + font test trên canvas "iShare — Khám phá", thêm dữ liệu mẫu MAU-01…05; người dùng chọn trộn (khung hướng 1, màu hướng 2, ô tìm kiếm hướng 2, bo góc hướng 3, thanh thao tác hướng 2) — vẽ thử 4 màn hình, dữ liệu MAU-06…08 |
| 0.2 | 2026-11-24 | Bước 3 được duyệt: hướng "Sổ tay" (mục 2, DD-UI-08…13); thêm dữ liệu mẫu MAU-06…08 |
| 0.3 | 2026-11-25 | Bước 4 được duyệt: screen-inventory.md (75 màn hình, rà soát lại theo SC); DD-UI-14…19 |
| 0.4 | 2026-11-25 | Bước 5 được duyệt: flows.md (46 đường dẫn, 8 luồng), 28 wireframe trên canvas trang "Bước 5 — Wireframe"; DD-UI-20…27; ngoại lệ AP-10 cho `wf--*` |
| 0.5 | 2026-11-25 | Bước 6 được duyệt: tokens (tokens.json, contrast-pairs.csv, tokens.css, tokens.dtcg.json), "iShare Design System" (62 component, 84 icon Material Symbols Sharp, font Be Vietnam Pro + JetBrains Mono); mục 3, 4; DD-UI-28…35; chuyển sang chế độ thực thi |
| 0.6 | 2026-11-26 | Bước 7 (chờ duyệt gộp đợt A–E): DD-UI-36…40 (nút chữ ở trang trống/lỗi, ErrorState căn giữa, ô soạn tự giãn, Lớp/Khối dùng Select, đếm số lần nhập mã, 5 component bố cục); token `inbox-w`; MAU-01 theo SC-M03-012 |
| 0.7 | 2026-11-26 | Bước 7 được duyệt: đợt A–E đã duyệt và đẩy sang Figma "iShare — UI" (5 page, 356 frame); DD-UI-41 (cách đẩy và chỉnh bản Figma); chuyển sang bước 8 |
| 0.8 | 2026-11-26 | DD-UI-42: khung quản trị riêng AdminShell cho khu kiểm duyệt và quản trị (token `console-*`, 68 component); đăng lại canvas, design system, đẩy lại page đợt C trên Figma |
| 0.9 | 2026-11-27 | DD-UI-43: dòng chân cột menu đổi thành "Chính sách và Điều khoản"; đăng lại canvas, design system, sửa chữ trên cả 5 page Figma |
| 0.10 | 2026-11-27 | Bước 8 lần 1: QA-final, sửa QA-F-01…10 trên canvas, design system (GroupCard, TagInput, ConversationItem, DescriptionList `--stack`, ô mật khẩu Hiện/Ẩn, cấp tiêu đề theo ngữ cảnh, `main` cho trang không có cột menu) và Figma; DD-UI-44 |
