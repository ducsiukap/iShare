---
ma_tai_lieu: UI-KIT
phien_ban: 1.0
trang_thai: Đã chốt
ngay: 2026-11-28
tac_gia: Phạm Văn Đức
---
# Đặc tả UI Kit — iShare

[Vietnamese Doc] — Bàn giao cho phase Coding (React, Vite). Tên component, props, token viết tiếng Anh. Đọc kèm
`routes.md` (màn hình → đường dẫn trang → component chính → frame Figma).

| Tài nguyên | Vị trí |
|---|---|
| Design system "iShare Design System" | https://claude.ai/artifact/VhNBYBjrD4Rng8CtynS7pp — mỗi component có `components/<Tên>/README.md` và `preview.html` (mọi trạng thái, cả hai theme); bản trong repo: `docs/resources/design/canvas/design-system/project/` |
| Canvas "iShare — Giao diện" | https://claude.ai/artifact/HAykztXFcJbkAiSCXKvift — 75 màn hình, 356 artboard; bản trong repo: `docs/resources/design/canvas/giao-dien/project/` |
| Figma "iShare — UI" | https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m — 5 page (đợt A–E), 356 frame; chỉ là bản lưu của canvas, không sửa trên Figma (DD-UI-41) |
| Tokens | `tokens/tokens.json` (nguồn), `handoff/css/tokens.vars.css` (nạp vào app) |
| CSS component | `handoff/css/components.css` (class `is-*`, chỉ dùng biến từ tokens) |
| Font | `handoff/css/fonts/` (7 tệp woff2 và 2 giấy phép OFL) |

## 1. Dùng tokens và CSS (không dùng Tailwind — DD-UI-45)

- Repo frontend không dùng Tailwind (Q9-01). CSS gốc của app nạp theo thứ tự:

  ```css
  @import "./tokens.vars.css";  /* biến CSS hai theme, @font-face, lớp kiểu chữ */
  @import "./components.css";   /* class is-* của design system */
  /* CSS riêng của app đặt sau, chỉ dùng var(--…) */
  ```

- `css/tokens.vars.css` là biến CSS thuần, tên ngắn (`--ink`, `--surface`, `--space-4`, `--topbar-h`), khai báo trên
  `:root, [data-theme="light"]` và `[data-theme="dark"]`. Đây là tệp `tokens.css` mà design system sinh từ
  `tokens.json`, giống hệt tệp canvas dùng (`ds/ishare/tokens.css`). Không sửa tay; khi `tokens.json` đổi thì đăng lại
  design system và lấy lại tệp này.
- `tokens/tokens.css` (khối `@theme` của Tailwind v4, tên `--color-*`, `--spacing-*`, `--size-*`, `--text-*`) và
  `tokens/tokens.dtcg.json` (định dạng DTCG cho công cụ token) giữ lại để đồng bộ công cụ, **không nạp vào app**:
  không có Tailwind thì trình duyệt bỏ qua cả khối `@theme`. Hai tệp này đang ghi sai giá trị bóng có hai theme
  (`shadow-1`, `shadow-2`); lấy giá trị bóng ở `tokens.vars.css` hoặc `tokens.json`.
- Bảng tên giữa các tệp (khi đọc `tokens.json` hoặc nếu sau này đổi sang Tailwind):

  | Nhóm | `tokens.vars.css` (app, `components.css`) | `tokens/tokens.css` (Tailwind) | `tokens.json` |
  |---|---|---|---|
  | Màu | `--ink`, `--primary-soft`, `--console-bg` | `--color-ink`, `--color-primary-soft`, `--color-console-bg` | `color` |
  | Khoảng cách | `--space-0-5` … `--space-16` | `--spacing-0-5` … `--spacing-16` | `spacing` |
  | Bo góc | `--radius-sm`, `--radius-full` | như bên trái | `radius` |
  | Bóng | `--shadow-1`, `--shadow-2` (đổi theo theme) | `--shadow-*` (đang sai, xem trên) | `shadow` |
  | Kích thước | `--control-h`, `--row-h-sm`, `--topbar-h`, `--dialog-w`… | `--size-control-h`, `--size-topbar-h`… | `size` |
  | Họ font | `--font-sans`, `--font-mono` | như bên trái | `type` |
  | Kiểu chữ | lớp `.display`, `.h1`…`.code` (14 kiểu); component dùng `is-h1`, `is-h2`, `is-label` | `--text-<kiểu>` kèm `--line-height`, `--font-weight` | `type` |

- Lớp kiểu chữ tên ngắn trong `tokens.vars.css` (`.body`, `.label`, `.code`, `.ui`…) không artboard nào dùng; nếu
  trùng lớp khác của app thì bỏ qua chúng — component chỉ dựa vào class `is-*` và biến.
- Theme: đặt `data-theme="light"` hoặc `data-theme="dark"` trên `<html>`; không đặt thì là theme sáng. Mọi màn hình,
  mọi trạng thái phải chạy được ở cả hai theme (DD-UI-15). Nguồn chưa nói người dùng chọn theme ở đâu (theo hệ điều
  hành hay một công tắc) — artboard không có công tắc theme, để phase Coding quyết.
- Font: Be Vietnam Pro 400, 600, 700 và bản nghiêng; JetBrains Mono biến thiên 100–800 (cả hai giấy phép OFL).
  `@font-face` trong `tokens.vars.css` trỏ `./fonts/`, nên giữ `fonts/` cạnh tệp. Không tải thêm độ đậm khác.
- Icon: Material Symbols Sharp (Apache-2.0), gói `@material-symbols/svg-400@0.48.3`; Upvote chưa bấm dùng bản
  `shift` của `@material-symbols/svg-600@0.48.3` (DD-UI-11, DD-UI-28). Chèn SVG trực tiếp, class `is-ic` (24px),
  `is-ic--sm` (20px), `is-ic--xs` (16px), `fill: currentColor`; bản `-fill` cho trạng thái đang bật (đã upvote, đã
  lưu, Ngôi sao tuần). Danh sách 84 icon và việc dùng của từng icon: design system › Icons.
- Chuyển động: nhanh 120ms (hover, focus, nút), vừa 200ms (menu, popover, toast, tab), chậm 280ms (dialog, ngăn trượt);
  vào `cubic-bezier(0.2, 0, 0, 1)`, ra `cubic-bezier(0.4, 0, 1, 1)`; `prefers-reduced-motion: reduce` tắt hết (đã có ở
  cuối `components.css`).
- Focus: `:focus-visible` viền 2px màu `focus`, cách 2px; trong AdminShell dùng `console-accent`. Class `is-focus`
  trong `components.css` chỉ để vẽ trạng thái focus tĩnh trên canvas; app dựa vào `:focus-visible`.

## 2. Đề xuất nền tảng (người dùng quyết ở phase Coding)

| Việc | Đề xuất | Lý do | Lưu ý chống "dáng mặc định" |
|---|---|---|---|
| Thành phần có a11y sẵn (Dialog, Drawer, Menu, Popover, Tooltip, Tabs, Select, Combobox, Switch, SegmentedControl) | Base UI hoặc React Aria (dạng headless) | Có sẵn bàn phím, quản lý focus, ARIA; không kèm giao diện | Không giữ màu, bo góc mặc định của bất kỳ thư viện nào; nếu dùng shadcn CLI để sinh khung thì xóa toàn bộ màu, bo góc mặc định ngay từ đầu; render đúng class `is-*` |
| Cách viết CSS | `components.css` nạp toàn cục, hoặc tách theo component (CSS Modules) giữ nguyên tên class | Không dùng Tailwind (Q9-01); class `is-*` đã dùng trên mọi artboard | Chỉ dùng `var(--…)`; không viết mã màu, cỡ, khoảng cách cứng |
| Công thức | KaTeX | Theo FR | Cỡ chữ công thức theo token `body` |
| Editor | Tiptap | Theo FR | EditorToolbar chỉ có các định dạng FR cho phép |
| Biểu đồ thống kê (TrendChart) | SVG tự vẽ theo README, hoặc một thư viện vẽ không kèm giao diện | Một kiểu biểu đồ cột theo thời gian, tối đa 3 chuỗi | Màu `chart-1…3`, lưới `line`, chữ trục `ink-muted`; luôn có bảng số liệu tương đương |

## 3. Quy ước (DD-UI-45)

- Tên component: PascalCase, không tiền tố (`PostCard`, `Button`, `AdminShell`) (Q9-02); trùng tên thư mục trong
  design system và tên mục 4.
- Class CSS giữ tiền tố `is-` theo kiểu BEM: khối `is-postcard`, phần tử `is-postcard__title`, biến thể
  `is-btn--primary`. Component React render đúng các class này để dùng chung `components.css`.
- Props tiếng Anh, camelCase; sự kiện `onXxx`; giá trị biến thể là chuỗi trùng hậu tố của class biến thể
  (`variant="primary"` → `is-btn--primary`).
- Chữ hiển thị tiếng Việt, đúng thuật ngữ của FR và glossary (Chủ đề, Tag, Lớp/Khối, Upvote, Ẩn danh…); không tự đặt
  từ mới.
- Trạng thái chung của control: mặc định, hover, focus-visible, active, disabled, đang xử lý (`aria-busy`); trạng thái
  nghiệp vụ ghi ở từng component.
- Cấp tiêu đề theo ngữ cảnh (QF-17): PostCard, GroupCard, EmptyState, TrendChart nhận `headingLevel`.
- Máy tính trước: artboard rộng 1440, bố cục co giãn không vỡ ở 1280; chưa có bản điện thoại (DD-UI-02).

## 4. Component

68 component, xếp theo nhóm của design system. Tên component (PascalCase, không tiền tố) trùng tên thư mục `components/<Tên>/` trong design system; props là đề xuất, kiểu dữ liệu nghiệp vụ (`PostSummary`, `UserSummary`…) chốt theo API ở phase Coding. "Dùng ở" lấy từ các artboard sáng trên canvas (màn hình mở trên trang khác chỉ tính phần hộp thoại, ngăn hoặc ô nổi của nó); "Figma" là một frame ví dụ có component đó.

| Nhóm | Component |
|---|---|
| Hiển thị | [Avatar](#avatar), [Tag](#tag), [TopicChip](#topicchip), [GradeLabel](#gradelabel), [Badge](#badge), [Counter](#counter), [StatusLabel](#statuslabel) |
| Nội dung | [PostCard](#postcard), [PostBody](#postbody), [ActionBar](#actionbar), [UpvoteButton](#upvotebutton), [Poll](#poll), [PollEditor](#polleditor), [Attachment](#attachment), [Comment](#comment) |
| Hành động | [Button](#button), [IconButton](#iconbutton), [Link](#link), [GoogleButton](#googlebutton) |
| Nhập liệu | [TextField](#textfield), [TextArea](#textarea), [Select](#select), [Checkbox](#checkbox), [Radio](#radio), [Switch](#switch), [FileDrop](#filedrop), [SearchField](#searchfield), [TagInput](#taginput), [SegmentedControl](#segmentedcontrol), [Combobox](#combobox), [DateTimeField](#datetimefield), [AvatarUpload](#avatarupload) |
| Danh sách | [ListItem](#listitem), [UserRow](#userrow), [GroupCard](#groupcard), [LeaderboardRow](#leaderboardrow) |
| Thông báo và chat | [NotificationItem](#notificationitem), [ConversationItem](#conversationitem), [MessageBubble](#messagebubble), [NewMessagePopup](#newmessagepopup) |
| Quản trị | [DataTable](#datatable), [FilterBar](#filterbar), [StatTile](#stattile), [TrendChart](#trendchart) |
| Cấu trúc | [PageLayout](#pagelayout), [AdminShell](#adminshell), [PageHeader](#pageheader), [SectionCard](#sectioncard), [TableOfContents](#tableofcontents), [DescriptionList](#descriptionlist), [AppHeader](#appheader), [NavBar](#navbar), [Tabs](#tabs), [Dialog](#dialog), [Drawer](#drawer), [Menu](#menu), [Popover](#popover), [Tooltip](#tooltip), [Pagination](#pagination), [StepIndicator](#stepindicator) |
| Phản hồi | [Toast](#toast), [InlineAlert](#inlinealert), [Banner](#banner), [EmptyState](#emptystate), [Skeleton](#skeleton), [ErrorState](#errorstate) |
| Soạn thảo | [EditorToolbar](#editortoolbar), [CommentComposer](#commentcomposer) |

### 4.1 Hiển thị

#### Avatar

- **Mục đích:** Ảnh đại diện tròn; chưa có ảnh thì hiện chữ cái đầu của tên hiển thị.
- **Dùng khi:** cạnh tên người ở bài, bình luận (DD-UI-12), danh sách, tin nhắn, menu tài khoản, trang hồ sơ.
- **Không dùng khi:** trang trí không gắn với người nào.
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `name` | `string` | — | Tên hiển thị; lấy chữ cái đầu khi chưa có ảnh |
  | `src` | `string?` | — | Ảnh đại diện |
  | `size` | `'sm' \| 'md' \| 'lg'` | `'md'` | 28 / 40 / 96px (`avatar-*`) |
  | `anonymous` | `boolean` | `false` | Avatar trung tính cho bài ẩn danh |

- **Biến thể và trạng thái:**
  - Cỡ: nhỏ 28px (bình luận, tin nhắn, dòng bảng), vừa 40px (tác giả bài, danh sách), lớn 96px (hồ sơ).
  - Chữ cái đầu trên nền `primary-soft`, chữ `primary`; có ảnh thì ảnh phủ kín vòng tròn.
  - Ẩn danh và "[Người dùng đã xóa]": nền `surface-hover`, icon người, chữ `ink-muted` (`--muted`).
- **Dữ liệu cần có:**
  - Tên hiển thị để lấy chữ cái đầu (tối đa 2 chữ: chữ đầu họ và chữ đầu tên gọi); URL ảnh nếu có.
- **A11y:**
  - Đứng cạnh tên đã hiển thị thì `aria-hidden`; đứng một mình (nút menu tài khoản) thì nhãn ở nút.
- **Class CSS** (`components.css`): `is-avatar`, `is-avatar--sm`, `is-avatar--lg`, `is-avatar--muted`
- **Token:** `primary-soft`, `primary`, `surface-hover`, `avatar-sm`, `avatar-md`, `avatar-lg`, `radius-full`
- **Dùng ở:** 57/75 màn hình (gần như mọi trang)
- **Preview:** design system › `components/Avatar/preview.html` · **Figma:** [SCR-SHARED-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=96-2)

#### Tag

- **Mục đích:** Nhãn Tag của bài, viết có dấu # đứng trước, bấm mở Kết quả tìm kiếm lọc theo Tag đó.
- **Dùng khi:** dưới tiêu đề bài, trong ô TagInput, danh sách Tag, chip bộ lọc đang áp dụng (có nút gỡ).
- **Không dùng khi:** Chủ đề (dùng TopicChip) hoặc trạng thái (dùng StatusLabel).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `name` | `string` | — | Không kèm #; component tự thêm |
  | `href` | `string?` | — | Mặc định `/search?tag={name}` |
  | `onRemove` | `() => void` | — | Có thì hiện nút gỡ (trong TagInput) |
  | `off` | `boolean` | `false` | Tag đã gỡ khỏi bài (gạch ngang) |

- **Biến thể và trạng thái:**
  - Liên kết (rê chuột: viền `line-strong`, chữ `ink`), có nút gỡ, đã vô hiệu hóa (gạch ngang, chỉ thấy trong Quản lý Tag).
- **Dữ liệu cần có:**
  - Tên Tag có dấu #; đích liên kết `/search?tag=`.
- **A11y:**
  - Nút gỡ có `aria-label` "Gỡ Tag #…".
- **Class CSS** (`components.css`): `is-tag`, `is-tag__x`, `is-tag--off`
- **Token:** `line`, `line-strong`, `ink-muted`, `radius-sm`
- **Dùng ở:** SCR-M02-01, SCR-M03-01, SCR-M03-02, SCR-M05-01, SCR-M05-05, SCR-M06-02, SCR-M11-03, SCR-M14-01, SCR-M16-03
- **Preview:** design system › `components/Tag/preview.html` · **Figma:** [SCR-M02-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=203-2)

#### TopicChip

- **Mục đích:** Chip Chủ đề của bài, nền nhấn nhạt để phân biệt với Tag.
- **Dùng khi:** dòng Chủ đề của bài (1–3), danh sách Chủ đề, ô chọn Chủ đề; biến thể nét đứt cho Gợi ý chủ đề của AI.
- **Không dùng khi:** Tag (dùng Tag).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `name` | `string` | — |  |
  | `href` | `string?` | — | Mặc định `/search?topic={id}` |
  | `variant` | `'default' \| 'suggest'` | `'default'` | `suggest` = gợi ý của AI, viền nét đứt, bấm để thêm |
  | `onRemove` | `() => void` | — | Trong TagInput |

- **Biến thể và trạng thái:**
  - Liên kết (rê chuột: viền `primary`), tĩnh, gợi ý (nét đứt, có icon thêm).
- **Dữ liệu cần có:**
  - Tên Chủ đề trong danh mục; đích `/search?topic=`.
- **A11y:**
  - Chip gợi ý là `<button>` "Thêm Chủ đề …".
- **Class CSS** (`components.css`): `is-topic`, `is-topic--suggest`
- **Token:** `primary-soft`, `primary`, `radius-sm`
- **Dùng ở:** SCR-M02-01, SCR-M03-01, SCR-M03-02, SCR-M05-05, SCR-M06-02, SCR-M11-03, SCR-M14-01
- **Preview:** design system › `components/TopicChip/preview.html` · **Figma:** [SCR-M02-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=203-2)

#### GradeLabel

- **Mục đích:** Nhãn Lớp/Khối của bài hoặc của người dùng.
- **Dùng khi:** dòng meta của bài, UserRow, hồ sơ, bảng xếp hạng.
- **Không dùng khi:** khi Lớp/Khối là "Chưa khai" — không hiện nhãn.
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `grade` | `10 \| 11 \| 12` | — | Hiện "Lớp 10"… |

- **Biến thể và trạng thái:**
  - Một dạng duy nhất, viền `line`, chữ `ink-muted` đậm.
- **Dữ liệu cần có:**
  - Giá trị 10, 11 hoặc 12.
- **A11y:**
  - Chữ đầy đủ "Lớp 10", không viết tắt.
- **Class CSS** (`components.css`): `is-grade`
- **Token:** `line`, `ink-muted`
- **Dùng ở:** SCR-M02-01, SCR-M03-02, SCR-M06-02, SCR-M11-03, SCR-M14-01
- **Preview:** design system › `components/GradeLabel/preview.html` · **Figma:** [SCR-M02-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=203-2)

#### Badge

- **Mục đích:** Huy hiệu đã đạt (5 mốc điểm, BR-M12-11) và dấu Ngôi sao tuần, trình bày tiết chế (DD-UI-05).
- **Dùng khi:** trang hồ sơ (huy hiệu kèm ngày đạt), bảng xếp hạng tab Tuần (Ngôi sao tuần).
- **Không dùng khi:** hiện huy hiệu chưa đạt hay tiến độ tới huy hiệu — FR cấm (BR-M12-13).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `kind` | `'milestone' \| 'weekly-star'` | — | Huy hiệu mốc điểm hoặc Ngôi sao tuần |
  | `name` | `string` | — |  |
  | `achievedAt` | `Date?` | — | Dòng "Đạt dd/mm/yyyy" |

- **Biến thể và trạng thái:**
  - Huy hiệu: icon, tên, ngày đạt — không ghi ngưỡng điểm (BR-M12-12).
  - Ngôi sao tuần: icon ngôi sao tô đặc màu `primary` + chữ "Ngôi sao tuần".
- **Dữ liệu cần có:**
  - Tên huy hiệu: Người mới nổi, Cây bút triển vọng, Cây bút tích cực, Chuyên gia cộng đồng, Huyền thoại iShare; ngày đạt đầu tiên.
- **A11y:**
  - Icon `aria-hidden`; chữ đã đủ nghĩa.
- **Class CSS** (`components.css`): `is-badge`, `is-badge__ic`, `is-badge__name`, `is-badge__date`, `is-star`
- **Token:** `primary`, `line`, `ink-muted`
- **Dùng ở:** SCR-M02-01
- **Preview:** design system › `components/Badge/preview.html` · **Figma:** [SCR-M02-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=203-2)

#### Counter

- **Mục đích:** Số đếm nhỏ cho mục chưa đọc hoặc số lượng trong tab.
- **Dùng khi:** chuông thông báo, biểu tượng Tin nhắn (số cuộc trò chuyện có tin chưa đọc), cuộc trò chuyện, tab có số lượng.
- **Không dùng khi:** số liệu chính của trang (dùng StatTile).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `value` | `number` | — | Quá 99 hiện "99+"; bằng 0 thì ẩn |
  | `muted` | `boolean` | `false` | `--muted`: số lượng trong tab |
  | `label` | `string` | — | Nhãn đầy đủ cho trình đọc màn hình, ví dụ "3 thông báo chưa đọc" |

- **Biến thể và trạng thái:**
  - Nhấn mạnh: nền `primary`, chữ `on-primary` (chưa đọc).
  - Trầm (`--muted`): số lượng trong tab.
  - Trên 99 hiện "99+"; bằng 0 thì ẩn.
- **Dữ liệu cần có:**
  - Số nguyên.
- **A11y:**
  - Số đếm phải có trong nhãn của nút chứa nó; bản thân Counter `aria-hidden`.
- **Class CSS** (`components.css`): `is-counter`, `is-counter--muted`, `is-dot`
- **Token:** `primary`, `on-primary`, `surface-hover`, `radius-full`
- **Dùng ở:** SCR-SHARED-01, SCR-SHARED-04, SCR-M01-07, SCR-M02-01, SCR-M02-03, SCR-M03-01, SCR-M03-02, SCR-M03-03, SCR-M04-02, SCR-M05-01, SCR-M06-02, SCR-M07-02, SCR-M08-05, SCR-M09-01, SCR-M09-02, SCR-M10-03, SCR-M11-01, SCR-M11-02, SCR-M11-03, SCR-M11-05, SCR-M11-06, SCR-M11-08, SCR-M11-10, SCR-M11-11, SCR-M12-01, SCR-M14-01, SCR-M16-01, SCR-M16-02, SCR-M16-05
- **Preview:** design system › `components/Counter/preview.html` · **Figma:** [SCR-SHARED-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=96-2)

#### StatusLabel

- **Mục đích:** Nhãn trạng thái nghiệp vụ, luôn có chữ (và icon khi có) — không bao giờ chỉ là một chấm màu (QF-03).
- **Dùng khi:** trạng thái bài (Chờ duyệt, Bị từ chối, Bị ẩn, Tự ẩn, Bình luận đã khóa), bài/bình luận Bị gắn cờ, nhãn tài khoản (Tài khoản đã bị khóa, Tài khoản tạm thời vô hiệu hoá), vai trò (Mod, Admin, Tác giả), trạng thái vụ và khiếu nại.
- **Không dùng khi:** huy hiệu thành tích (dùng Badge) hoặc Tag, Chủ đề.
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `tone` | `'neutral' \| 'info' \| 'success' \| 'warning' \| 'danger'` | `'neutral'` |  |
  | `plain` | `boolean` | `false` | `--plain`: chỉ chữ và icon, không nền (dòng meta) |
  | `icon` | `IconName?` | — | Icon Material Symbols Sharp |
  | `children` | `ReactNode` | — | Chữ trạng thái đúng thuật ngữ FR |

- **Biến thể và trạng thái:**
  - `--success`: Đã đăng, Đã xử lý, Chấp nhận.
  - `--warning`: Chờ duyệt, Chờ xét, cảnh cáo LIGHT/MEDIUM.
  - `--danger`: Bị từ chối, Bị gắn cờ, Tài khoản đã bị khóa, HEAVY.
  - `--info`: vai trò Mod, Admin, ADMIN gốc.
  - Trung tính (mặc định): Bị ẩn, Tự ẩn, Bình luận đã khóa, Ẩn danh, Tác giả, Nháp.
  - `--plain`: chỉ chữ và icon, không nền — trong dòng meta.
- **Dữ liệu cần có:**
  - Chữ đúng thuật ngữ của FR; icon theo nghĩa (schedule, block, visibility_off, lock, flag, shield_person).
- **A11y:**
  - Icon `aria-hidden`; chữ đọc được trên nền nhạt ở cả hai theme (≥ 4.5:1).
- **Class CSS** (`components.css`): `is-status`, `is-status--success|warning|danger|info|plain`
- **Token:** `success`, `warning`, `danger`, `info` và `*-soft`, `surface-hover`, `ink-muted`, `icon-xs`
- **Dùng ở:** SCR-M02-01, SCR-M03-01, SCR-M03-02, SCR-M03-03, SCR-M03-04, SCR-M04-01, SCR-M04-02, SCR-M05-04, SCR-M07-01, SCR-M07-02, SCR-M08-02, SCR-M08-03, SCR-M08-05, SCR-M09-02, SCR-M09-03, SCR-M09-04, SCR-M10-01, SCR-M10-02, SCR-M10-05, SCR-M11-01, SCR-M11-03, SCR-M11-05, SCR-M11-06, SCR-M11-10, SCR-M11-11, SCR-M14-01, SCR-M16-02
- **Preview:** design system › `components/StatusLabel/preview.html` · **Figma:** [SCR-M03-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=194-2)

### 4.2 Nội dung

#### PostCard

- **Mục đích:** Một bài trong danh sách (trang chủ, kết quả tìm kiếm, hồ sơ, trang nhóm): tác giả, tiêu đề, trích đoạn 2 dòng, Chủ đề, Tag, số upvote và bình luận chỉ để xem (DD-UI-13).
- **Dùng khi:** mọi danh sách bài.
- **Không dùng khi:** kết quả phụ (người dùng, nhóm) của trang tìm kiếm — dùng UserRow, GroupCard.
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `post` | `PostSummary` | — | Tiêu đề, trích đoạn, tác giả hoặc ẩn danh, thời điểm, Lớp/Khối, nhóm, Chủ đề, Tag, số upvote, số bình luận |
  | `status` | `'draft' \| 'pending' \| 'rejected' \| …?` | — | Nhãn trạng thái ở hồ sơ chủ tài khoản |
  | `headingLevel` | `2 \| 3` | `2` | Cấp tiêu đề theo ngữ cảnh (QF-17) |
  | `showGroup` | `boolean` | `true` | Dòng "trong {nhóm}" |

- **Biến thể và trạng thái:**
  - Các thẻ nằm chung một khối `is-feed`, ngăn bằng đường kẻ `line` — không lồng thẻ trong thẻ (AP-23).
  - Rê chuột: nền `surface-hover`; cả thẻ bấm được qua liên kết tiêu đề.
  - Biến thể: trong nhóm (dòng meta có "trong CLB Toán"), ẩn danh (avatar trung tính, "Ẩn danh"), có nhãn trạng thái (Chờ duyệt, Bị từ chối, Nháp ở hồ sơ chủ tài khoản), tiêu đề dài 2 dòng.
- **Dữ liệu cần có:**
  - Tiêu đề ≤150 ký tự, trích đoạn (cắt 2 dòng), tác giả hoặc Ẩn danh, thời điểm, Lớp/Khối, nhóm, Chủ đề, Tag, số upvote, số bình luận.
- **A11y:**
  - Mỗi thẻ là `<article>`; tiêu đề lấy cấp theo ngữ cảnh: `h2` khi danh sách nằm ngay dưới `h1` của trang, `h3` khi danh sách nằm trong một mục có `h2` (QF-17). Con số kèm chữ ẩn "upvote", "bình luận".
- **Class CSS** (`components.css`): `is-feed`, `is-postcard`, `is-meta`, `is-postcard__title`, `is-postcard__excerpt`, `is-stat--up`
- **Token:** `surface`, `line`, `surface-hover`, `primary`, `ink-muted`
- **Dùng ở:** SCR-M02-01, SCR-M03-03, SCR-M03-05, SCR-M06-02, SCR-M07-02, SCR-M08-03, SCR-M11-03, SCR-M11-06, SCR-M11-10, SCR-M14-01
- **Preview:** design system › `components/PostCard/preview.html` · **Figma:** [SCR-M02-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=203-2)

#### PostBody

- **Mục đích:** Phần đầu và nội dung bài ở trang chi tiết: tiêu đề `display`, dòng tác giả, Chủ đề, Tag, rồi nội dung giàu định dạng theo BR-M03-03.
- **Dùng khi:** trang Chi tiết bài viết, bản xem trước trong trình soạn, nội dung bài trong hàng chờ duyệt, Lịch sử sửa bài, trang Privacy Policy/ToS (chỉ phần nội dung).
- **Không dùng khi:** trích đoạn trong danh sách (dùng PostCard).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `post` | `PostDetail` | — | Tiêu đề, tác giả, Chủ đề, Tag, nội dung HTML đã lọc, sửa lần cuối |
  | `anonymous` | `boolean` | `false` |  |
  | `renderMath` | `boolean` | `true` | Chạy KaTeX trên nội dung |

- **Biến thể và trạng thái:**
  - Định dạng: đậm, nghiêng, gạch chân, gạch ngang, tô sáng (`mark`); tiêu đề mục H1–H3 (`post-h1/2/3`); danh sách chấm, số, việc cần làm; code trong dòng và khối code tô màu cú pháp (`syntax-*`, JetBrains Mono, tắt ký tự ghép); công thức KaTeX trong dòng và khối (1.1em, khối dài cuộn ngang); bảng (cuộn ngang trong khung); trích dẫn; đường kẻ ngang; liên kết có nhãn; @nhắc tên.
  - Trạng thái trang (Bị ẩn, Chờ duyệt, Bị khóa bình luận, Ẩn danh) hiện bằng StatusLabel cạnh dòng tác giả và InlineAlert phía trên nội dung.
  - Bản nhỏ (`is-prose--sm`, 16/1.6 như `body-comment`) cho nội dung đặt trong thẻ, ví dụ từng phiên bản ở Lịch sử sửa bài.
- **Dữ liệu cần có:**
  - HTML đã làm sạch từ trình soạn; LaTeX dạng mã để KaTeX dựng (bản preview tải KaTeX 0.16.11 từ jsDelivr).
- **A11y:**
  - Tiêu đề bài là `h1` của trang; H1–H3 trong bài là `h2`–`h4` để không nhảy cấp (QF-17).
  - Bảng, công thức khối, khối code cuộn trong khung riêng, trang không cuộn ngang (QF-12, QF-14).
- **Class CSS** (`components.css`): `is-post`, `is-post__title`, `is-prose`, `is-prose--sm`, `tok-k|s|n|f|c`, `is-mention`
- **Token:** `body`, `body-comment`, `post-h1`, `post-h2`, `post-h3`, `code`, `mark`, `syntax-*`, `primary-soft`, `bg`, `line`
- **Dùng ở:** SCR-M03-02
- **Preview:** design system › `components/PostBody/preview.html` · **Figma:** [SCR-M03-02--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=659-2)

#### ActionBar

- **Mục đích:** Thanh thao tác dưới bài: Upvote · Bình luận · Tóm tắt · Lưu, Báo cáo ở cuối (DD-UI-10).
- **Dùng khi:** dưới nội dung bài ở trang chi tiết.
- **Không dùng khi:** danh sách bài — số upvote và bình luận chỉ để xem (DD-UI-13).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `upvoted / upvotes` | `boolean / number` | `false / 0` |  |
  | `comments` | `number` | `0` | Bình luận là liên kết tới khu bình luận |
  | `saved` | `boolean` | `false` | "Đã lưu", icon tô đặc |
  | `own` | `boolean` | `false` | Bài của mình: Upvote tắt, giữ chỗ |
  | `commentsLocked` | `boolean` | `false` | Chữ "đã khóa" + icon khóa |
  | `canSummarize` | `boolean` | `false` | Bài từ 300 từ và AI bật; mở ngăn Tóm tắt |
  | `guest` | `boolean` | `false` | Bấm Upvote, Lưu, Báo cáo: mở lời mời đăng nhập |
  | `onUpvote / onSummarize / onSave / onReport` | `() => void` | — |  |

- **Biến thể và trạng thái:**
  - Mọi nút trơn như nhau (không viền, không nền); Upvote nổi bật bằng màu `primary`, chữ đậm 700 và icon nét dày (DD-UI-11).
  - Đã upvote: icon tô đặc, số tăng; đã lưu: icon tô đặc, chữ "Đã lưu", màu `primary`.
  - Tóm tắt chỉ có khi bài từ 300 từ và AI bật; mở ngăn Tóm tắt (Drawer).
  - Bài của chính mình: Upvote tắt (BR-M12-03), giữ chỗ để thanh không nhảy; bình luận đã khóa: chữ "đã khóa" + icon khóa.
  - Guest bấm Upvote, Lưu, Báo cáo: mở lời mời đăng nhập.
- **Dữ liệu cần có:**
  - Số upvote, số bình luận, trạng thái đã upvote/đã lưu của người xem, bài có đủ 300 từ không, bình luận có bị khóa không.
- **A11y:**
  - `role="group"` có nhãn; Upvote và Lưu là nút bật/tắt với `aria-pressed`; Bình luận là liên kết tới khu bình luận.
- **Class CSS** (`components.css`): `is-actions`, `is-act`, `is-act--up`, `is-act--end`
- **Token:** `primary`, `ink-muted`, `surface-hover`, `line`, `control-h`
- **Dùng ở:** SCR-M03-02
- **Preview:** design system › `components/ActionBar/preview.html` · **Figma:** [SCR-M03-02--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=659-2)

#### UpvoteButton

- **Mục đích:** Nút Upvote bật/tắt cho bài viết (trong ActionBar) và cho bình luận (cỡ nhỏ).
- **Dùng khi:** bài viết và bình luận; không có downvote (BR-M12-01).
- **Không dùng khi:** danh sách bài — chỉ hiện số (Stat).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `pressed` | `boolean` | `false` | `aria-pressed`; đã upvote: icon tô đặc |
  | `count` | `number` | `0` | Nhãn đọc "Upvote, 12" |
  | `size` | `'md' \| 'sm'` | `'md'` | `sm` cho bình luận |
  | `disabled` | `boolean` | `false` | Nội dung của chính mình (BR-M12-03) |
  | `onToggle` | `() => void` | — | Guest bấm: mở lời mời đăng nhập |

- **Biến thể và trạng thái:**
  - Chưa upvote: icon nét dày (Material Symbols weight 600), chữ đậm, màu `primary`.
  - Đã upvote: icon tô đặc, số +1.
  - Nội dung của chính mình: tắt, màu `ink-muted` (BR-M12-03).
  - Bình luận: cỡ nhỏ `--sm`, chỉ số không kèm chữ "Upvote" nhưng có nhãn ẩn.
- **Dữ liệu cần có:**
  - Số upvote đang có hiệu lực, trạng thái của người xem.
- **A11y:**
  - `aria-pressed`; nhãn đọc được "Upvote, 12".
- **Class CSS** (`components.css`): `is-act`, `is-act--up`, `is-act--sm`
- **Token:** `primary`, `ink-muted`
- **Dùng ở:** SCR-M03-02, SCR-M04-01
- **Preview:** design system › `components/UpvoteButton/preview.html` · **Figma:** [SCR-M03-02--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=659-2)

#### Poll

- **Mục đích:** Bình chọn đóng trong bài: chọn một hoặc nhiều, có hạn kết thúc (BR-M03-09…13).
- **Dùng khi:** dưới nội dung bài có bình chọn.
- **Không dùng khi:** khảo sát mở cho người đọc thêm lựa chọn — FR không có.
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `options` | `PollOption[]` | — | 2–10 lựa chọn: nhãn, số phiếu |
  | `multiple` | `boolean` | `true` | Checkbox khi chọn nhiều, radio khi chọn một |
  | `endsAt` | `Date` | — | Hạn kết thúc |
  | `state` | `'open' \| 'voted' \| 'closed'` | `'open'` | `voted`: thanh kết quả, "Bạn đã chọn"; `closed`: "Đã kết thúc", chỉ còn kết quả |
  | `showResultsBeforeVote` | `boolean` | `false` | Tác giả bật thì hiện kết quả khi chưa bình chọn |
  | `isAuthor` | `boolean` | `false` | Nút Quản lý bình chọn |
  | `onVote` | `(ids: string[]) => void` | — |  |

- **Biến thể và trạng thái:**
  - Chưa bình chọn: danh sách lựa chọn (checkbox khi chọn nhiều, radio khi chọn một), nút Bình chọn; kết quả ẩn nếu tác giả không bật "hiện kết quả trước khi bình chọn".
  - Đã bình chọn: thanh kết quả với phần trăm và số phiếu, lựa chọn của mình có dấu kiểm và chữ "Bạn đã chọn".
  - Đã đóng: nhãn "Đã kết thúc", chỉ còn kết quả.
  - Tác giả: thêm nút Quản lý bình chọn (PollEditor).
- **Dữ liệu cần có:**
  - Câu hỏi (tiêu đề bài), lựa chọn 2–10, chế độ chọn một/nhiều, hạn kết thúc, số phiếu, lựa chọn của người xem.
- **A11y:**
  - `fieldset` + `legend`; thanh kết quả có chữ phần trăm, không chỉ dựa vào độ dài thanh.
- **Class CSS** (`components.css`): `is-poll`, `is-poll__opt`, `is-poll__res`, `is-bar`, `is-bar__fill`, `is-poll__mine`
- **Token:** `primary`, `surface-hover`, `line-strong`, `radius-full`
- **Dùng ở:** SCR-M03-02
- **Preview:** design system › `components/Poll/preview.html` · **Figma:** [SCR-M03-02--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=659-2)

#### PollEditor

- **Mục đích:** Khối tạo và quản lý bình chọn trong trình soạn bài và ở bài đã đăng (chỉ tác giả).
- **Dùng khi:** trình soạn (SCR-M03-01) khi bấm nút Bình chọn trên EditorToolbar; Quản lý bình chọn (SCR-M03-04).
- **Không dùng khi:** người đọc bình chọn (dùng Poll).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `value` | `PollDraft` | — | Lựa chọn 2–10, chọn nhiều (mặc định bật), hiện kết quả trước khi bình chọn (mặc định tắt), hạn kết thúc bắt buộc |
  | `mode` | `'draft' \| 'published'` | `'draft'` | `published`: chỉ Đổi hạn, Kết thúc ngay, Thêm lựa chọn (tổng ≤10); lựa chọn cũ chỉ đọc |
  | `errors` | `Record<string, string>?` | — | Thiếu lựa chọn, thiếu hạn, hạn trước hiện tại |
  | `onChange` | `(v: PollDraft) => void` | — |  |

- **Biến thể và trạng thái:**
  - Bài nháp: sửa được mọi lựa chọn, chế độ, hạn; nút Bỏ bình chọn.
  - Bài đã đăng: ba thao tác riêng — Đổi hạn kết thúc, Kết thúc ngay, Thêm lựa chọn (tổng ≤10); lựa chọn cũ chỉ đọc (SC-M03-009, -019, -020).
  - Lỗi: thiếu lựa chọn (cần 2–10), thiếu hạn, hạn trước hiện tại.
- **Dữ liệu cần có:**
  - Danh sách lựa chọn, chế độ chọn một/nhiều (mặc định nhiều), hiện kết quả trước khi bình chọn (mặc định tắt), hạn kết thúc bắt buộc.
- **A11y:**
  - Mỗi ô lựa chọn có nhãn "Lựa chọn 1"…; nút gỡ có `aria-label`.
- **Class CSS** (`components.css`): `is-poll`, `is-field`, `is-input`, `is-check`
- **Token:** như TextField
- **Dùng ở:** SCR-M03-01, SCR-M03-04
- **Preview:** design system › `components/PollEditor/preview.html` · **Figma:** [SCR-M03-04--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=154-2)

#### Attachment

- **Mục đích:** Tệp đính kèm của bài: ảnh (xem trước) và tài liệu (tên, loại, dung lượng, nút tải).
- **Dùng khi:** cuối nội dung bài, trong trình soạn sau khi thêm tệp, bằng chứng của báo cáo và khiếu nại.
- **Không dùng khi:** ảnh đại diện (dùng AvatarUpload).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `files` | `AttachmentFile[]` | — | Ảnh (xem trước) hoặc tài liệu (tên, loại, dung lượng) |
  | `editable` | `boolean` | `false` | Trong trình soạn: có nút gỡ |
  | `onRemove` | `(id: string) => void` | — |  |

- **Biến thể và trạng thái:**
  - Ảnh: lưới ô 4:3 xem trước, bấm để phóng to.
  - Tài liệu: icon loại tệp, tên cắt bằng dấu …, dung lượng, nút Tải về.
  - Trong trình soạn: đang tải lên (thanh tiến độ, nút Hủy), lỗi (viền `danger`, câu lỗi, nút Thử lại), nút Gỡ.
- **Dữ liệu cần có:**
  - Tên tệp, loại, dung lượng (định dạng Việt Nam: 1,2 MB), URL xem trước.
- **A11y:**
  - Ảnh có `alt` (tên tệp nếu tác giả không nhập mô tả); thanh tiến độ `role="progressbar"` có giá trị.
- **Class CSS** (`components.css`): `is-att`, `is-att__thumb`, `is-att__name`, `is-att__meta`, `is-progress`, `is-imgph`
- **Token:** `line`, `surface-hover`, `primary`, `danger`
- **Dùng ở:** SCR-M03-01, SCR-M03-02
- **Preview:** design system › `components/Attachment/preview.html` · **Figma:** [SCR-M03-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=194-2)

#### Comment

- **Mục đích:** Bình luận và trả lời (2 cấp) có avatar cạnh tên (DD-UI-12), dòng trích khi trả lời, Upvote cỡ nhỏ.
- **Dùng khi:** khu bình luận của bài (SCR-M04-01), xem lại bình luận đã bị xử lý (SCR-M04-02).
- **Không dùng khi:** tin nhắn chat (dùng MessageBubble).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `comment` | `CommentData` | — | Tác giả, thời điểm, nội dung, số upvote, "(đã chỉnh sửa)", dòng trích khi trả lời |
  | `level` | `1 \| 2` | `1` | Bình luận gốc hoặc trả lời |
  | `isPostAuthor` | `boolean` | `false` | Nhãn "Tác giả" cạnh tên |
  | `own` | `boolean` | `false` | Menu "…" có Sửa, Xóa; Upvote tắt |
  | `removed` | `boolean` | `false` | `--removed`: chữ nghiêng thay nội dung, không có thao tác |
  | `canReply` | `boolean` | `true` | Tắt khi bình luận bị khóa |
  | `children` | `ReactNode` | — | Các trả lời |

- **Biến thể và trạng thái:**
  - Bình luận gốc và trả lời thụt vào một cột avatar; trả lời có dòng trích "tên người được trả lời: đầu bình luận…" (BR-M04-04).
  - Nhãn "Tác giả" cạnh tên tác giả bài; "(đã chỉnh sửa)"; Upvote cỡ nhỏ (tắt với bình luận của chính mình).
  - Đã bị gỡ/xóa: chữ nghiêng `ink-muted` thay nội dung, không có thao tác.
  - Menu "…": Sửa, Xóa (không hỏi lại — SC-M04), Báo cáo.
- **Dữ liệu cần có:**
  - Tác giả, thời điểm, nội dung (định dạng BR-M04-01), số upvote, trạng thái của người xem, dòng trích.
- **A11y:**
  - Mỗi bình luận là một mục danh sách; nút "…" có `aria-label` nêu tên tác giả.
- **Class CSS** (`components.css`): `is-comment`, `is-comment__head`, `is-comment__body`, `is-quote`, `is-comment__replies`, `is-comment--removed`
- **Token:** `body-comment`, `avatar-sm`, `ink-muted`, `line-strong`
- **Dùng ở:** SCR-M03-02, SCR-M04-01, SCR-M04-02
- **Preview:** design system › `components/Comment/preview.html` · **Figma:** [SCR-M03-02--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=659-2)

### 4.3 Hành động

#### Button

- **Mục đích:** Nút bấm cho một hành động; nhãn là động từ rõ nghĩa, không có mũi tên ở cuối.
- **Dùng khi:** người dùng thực hiện một việc: gửi, lưu, nhận xử lý, tham gia nhóm.
- **Không dùng khi:** chỉ để đi tới trang khác (dùng Link) hoặc chỉ có icon (dùng IconButton).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `variant` | `'primary' \| 'secondary' \| 'ghost' \| 'danger' \| 'text-primary' \| 'text'` | `'secondary'` | Tối đa một nút `primary` mỗi vùng; `text-primary`, `text` chỉ trong EmptyState, ErrorState |
  | `size` | `'md' \| 'sm'` | `'md'` | 40 / 32px |
  | `icon` | `IconName?` | — | Icon đứng trước nhãn |
  | `busy` | `boolean` | `false` | `aria-busy`, khóa bấm, icon xoay, nhãn dạng tiếp diễn |
  | `disabled` | `boolean` | `false` |  |
  | `href` | `string?` | — | Có thì render `<a>` |
  | `fullWidth` | `boolean` | `false` | Trang đăng nhập, đăng ký |

- **Biến thể và trạng thái:**
  - **Chính** (`--primary`): tối đa một nút mỗi vùng, cho việc chính của màn hình: Đăng bài, Gửi khiếu nại, Nhận xử lý.
  - **Phụ** (mặc định): việc phụ đứng cạnh nút chính: Lưu nháp, Hủy trong form.
  - **Nhẹ** (`--ghost`): việc ít quan trọng trong dải nút: Hủy trong dialog, Bỏ qua.
  - **Nguy hiểm** (`--danger`): việc không hoàn tác được: Ban, Xóa nhóm, Vô hiệu hóa tài khoản.
  - **Chữ chính** (`--text-primary`) và **chữ phụ** (`--text`): nút chữ, không nền, không viền; chữ đậm 700 màu chủ đạo hoặc màu chữ chính, rê chuột hiện nền nhạt. Chỉ dùng cho nút trong EmptyState và ErrorState.
  - Cỡ vừa (40px, mặc định) và nhỏ (`--sm`, 32px) cho bảng, bộ lọc khu quản trị và dòng thông báo.
  - Trạng thái: mặc định, rê chuột, focus (vòng 2px `focus`, cách 2px), đang nhấn, tắt (`disabled`), đang xử lý (`aria-busy`, icon xoay, nhãn đổi thành dạng tiếp diễn).
- **Dữ liệu cần có:**
  - Nhãn tiếng Việt, viết hoa chữ đầu: "Đăng bài", không "ĐĂNG BÀI".
  - Icon (tùy chọn) đặt trước nhãn, cỡ `icon-sm`.
- **A11y:**
  - Dùng `<button type="button">` (hoặc `submit` trong form); link điều hướng dùng `<a>`.
  - Đang xử lý: `aria-busy="true"` và tắt bấm lại; nhãn mô tả việc đang làm.
  - Nút tắt vẫn đọc được (chữ `ink-muted`); nếu tắt vì thiếu điều kiện, nói lý do cạnh nút.
- **Class CSS** (`components.css`): `is-btn`, `is-btn--primary`, `is-btn--ghost`, `is-btn--danger`, `is-btn--text-primary`, `is-btn--text`, `is-btn--sm`
- **Token:** `primary`, `primary-hover`, `primary-soft`, `on-primary`, `ink`, `danger`, `danger-hover`, `on-danger`, `line-strong`, `surface-hover`, `radius-sm`, `control-h`, `control-h-sm`
- **Dùng ở:** 72/75 màn hình (gần như mọi trang)
- **Preview:** design system › `components/Button/preview.html` · **Figma:** [SCR-SHARED-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=96-2)

#### IconButton

- **Mục đích:** Nút chỉ có icon, luôn kèm nhãn ẩn cho trình đọc màn hình.
- **Dùng khi:** hành động quen thuộc ở vị trí cố định: chuông thông báo, tin nhắn, menu "…", đóng dialog, nút trên thanh soạn thảo.
- **Không dùng khi:** hành động quan trọng hoặc lạ với người dùng — dùng Button có chữ.
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `icon` | `IconName` | — |  |
  | `label` | `string` | — | Bắt buộc: `aria-label` |
  | `size` | `'md' \| 'sm'` | `'md'` | 40 / 32px |
  | `outline` | `boolean` | `false` | `--outline`: có viền |
  | `pressed / expanded` | `boolean?` | — | Đang bật hoặc đang mở: nền `primary-soft` |
  | `badge` | `number?` | — | Counter ở góc (chuông, tin nhắn) |

- **Biến thể và trạng thái:**
  - Mặc định trong suốt, icon `ink-muted`; rê chuột nền `surface-hover`, icon `ink`.
  - Đang bật hoặc đang mở (`aria-pressed`, `aria-expanded`): nền `primary-soft`, icon `primary`.
  - Có số đếm (Counter) ở góc: chuông, tin nhắn.
  - Cỡ vừa 40px, nhỏ 32px (thanh soạn thảo, thẻ Tag, dòng bảng); biến thể có viền `--outline`.
- **Dữ liệu cần có:**
  - `aria-label` bằng tiếng Việt mô tả việc: "Thông báo, 3 chưa đọc", "Thêm thao tác", "Đóng".
- **A11y:**
  - Vùng bấm tối thiểu 32×32 (QF-04).
  - Số đếm nằm trong `aria-label`, không chỉ trong phần hiển thị.
- **Class CSS** (`components.css`): `is-iconbtn`, `is-iconbtn--sm`, `is-iconbtn--outline`
- **Token:** `ink-muted`, `surface-hover`, `primary-soft`, `primary`, `control-h`, `control-h-sm`
- **Dùng ở:** 64/75 màn hình (gần như mọi trang)
- **Preview:** design system › `components/IconButton/preview.html` · **Figma:** [SCR-SHARED-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=96-2)

#### Link

- **Mục đích:** Liên kết điều hướng tới trang hoặc nội dung khác.
- **Dùng khi:** đi tới trang khác: "Xem lịch sử", tên tác giả, tiêu đề bài, "Chính sách và Điều khoản" ở chân cột menu.
- **Không dùng khi:** thực hiện thao tác thay đổi dữ liệu (dùng Button).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `href` | `string` | — | `href` thật |
  | `quiet` | `boolean` | `false` | `--quiet`: tên người, tiêu đề bài trong danh sách |
  | `children` | `ReactNode` | — | Nhãn nói rõ đích tới |

- **Biến thể và trạng thái:**
  - Mặc định: màu `primary`, gạch chân 1px — trong đoạn văn luôn gạch chân để không chỉ dựa vào màu (QF-03).
  - Rê chuột: gạch chân dày 2px.
  - Trầm (`--quiet`): tên người, tiêu đề bài trong danh sách — màu chữ thường, gạch chân khi rê chuột.
- **Dữ liệu cần có:**
  - `href` thật; nhãn nói rõ đích tới.
- **A11y:**
  - Dùng `<a href>`; focus hiện vòng `focus`.
- **Class CSS** (`components.css`): `is-link`, `is-link--quiet`
- **Token:** `primary`, `ink`, `focus`
- **Dùng ở:** SCR-SHARED-06, SCR-M01-01, SCR-M01-04, SCR-M01-05, SCR-M01-10, SCR-M02-01, SCR-M02-02, SCR-M03-01, SCR-M03-02, SCR-M03-03, SCR-M05-01, SCR-M06-01, SCR-M06-02, SCR-M07-01, SCR-M07-03, SCR-M08-02, SCR-M08-05, SCR-M08-06, SCR-M09-02, SCR-M09-03, SCR-M10-01, SCR-M11-05, SCR-M11-07, SCR-M11-11, SCR-M12-01
- **Preview:** design system › `components/Link/preview.html` · **Figma:** [SCR-SHARED-06--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=516-2)

#### GoogleButton

- **Mục đích:** Nút đăng ký hoặc đăng nhập bằng tài khoản Google (FR-M01).
- **Dùng khi:** màn hình Đăng ký (SCR-M01-01) và Đăng nhập (SCR-M01-04), đặt trên form email.
- **Không dùng khi:** liên kết tài khoản trong Cài đặt — FR không có thao tác này.
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `busy` | `boolean` | `false` | Đang chuyển sang Google: icon xoay thay logo |
  | `onClick` | `() => void` | — | Nhãn cố định "Tiếp tục với Google" ở cả đăng ký và đăng nhập |

- **Biến thể và trạng thái:**
  - Dáng nút phụ (nền `surface`, viền `line-strong`) với logo chữ G bốn màu của Google, không đổi màu logo.
  - Nhãn: "Tiếp tục với Google" ở cả hai màn hình (Google tự liên kết tài khoản cùng email, FR-M01).
  - Đang chuyển sang Google: `aria-busy`, icon xoay thay logo.
- **Dữ liệu cần có:**
  - Logo lấy từ `assets/Google/google-g.svg`; giữ đúng tỉ lệ, cỡ 20px, có khoảng trống quanh logo.
  - Theo hướng dẫn thương hiệu của Google Identity; nếu triển khai bằng nút do Google cung cấp thì dùng nút đó thay cho component này.
- **A11y:**
  - Logo có `alt=""` vì nhãn đã nói đủ.
- **Class CSS** (`components.css`): `is-btn`, `is-btn--block`, `is-btn__logo`
- **Token:** `surface`, `line-strong`, `ink`, `control-h`
- **Dùng ở:** SCR-M01-01, SCR-M01-04
- **Preview:** design system › `components/GoogleButton/preview.html` · **Figma:** [SCR-M01-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=732-2)

### 4.4 Nhập liệu

#### TextField

- **Mục đích:** Ô nhập một dòng có nhãn luôn hiện, gợi ý định dạng và lỗi nằm ngay dưới ô.
- **Dùng khi:** nhập email, username, tên hiển thị, tiêu đề, mã kích hoạt, tên nhóm; biến thể mật khẩu và chỉ đọc có nút Sao chép (link mời nhóm).
- **Không dùng khi:** nhập nhiều dòng (dùng TextArea) hoặc chọn trong danh sách cố định (Select, Radio).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `label` | `string` | — | Luôn hiện |
  | `type` | `'text' \| 'email' \| 'password' \| 'url'` | `'text'` | `password` có nút Hiện/Ẩn mật khẩu |
  | `autoComplete` | `string?` | — | `email`, `current-password`, `new-password`, `username`… |
  | `hint` | `string?` | — | Gợi ý định dạng dưới ô |
  | `error` | `string?` | — | `aria-invalid`, `aria-describedby` |
  | `maxLength` | `number?` | — | Có thì hiện bộ đếm |
  | `optional` | `boolean` | `false` | "(không bắt buộc)" |
  | `readOnly / copyable` | `boolean` | `false` | Chỉ đọc có nút Sao chép (link mời) |
  | `size` | `'md' \| 'sm'` | `'md'` |  |

- **Biến thể và trạng thái:**
  - Mặc định, rê chuột (viền `ink-muted`), focus (viền và vòng `focus`), lỗi (`aria-invalid`, viền `danger`, thông báo lỗi có icon), tắt, chỉ đọc (nền `bg`).
  - Bộ đếm ký tự khi FR có giới hạn (username 3–20, tiêu đề ≤150).
  - Mật khẩu: nút Hiện/Ẩn mật khẩu (QF-09); cho dán, `autocomplete` đúng loại.
  - Chỉ đọc kèm nút Sao chép (link mời nhóm, link mời nhóm chat).
  - Cỡ nhỏ `--sm` cho bộ lọc khu quản trị.
- **Dữ liệu cần có:**
  - Nhãn, gợi ý định dạng trước khi nhập, thông báo lỗi nói cách sửa (lấy đúng câu của SC).
  - Ô bắt buộc ghi rõ "(bắt buộc)" hoặc ô tùy chọn ghi "(không bắt buộc)" — chọn một cách cho cả form.
- **A11y:**
  - `<label for>` gắn với ô; gợi ý và lỗi nối bằng `aria-describedby`.
  - Không xóa dữ liệu đã nhập khi lỗi (QF-08).
- **Class CSS** (`components.css`): `is-field`, `is-field__label`, `is-field__hint`, `is-field__error`, `is-field__count`, `is-input`, `is-inputwrap`
- **Token:** `line-strong`, `focus`, `danger`, `ink-muted`, `bg`, `control-h`
- **Dùng ở:** SCR-M01-01, SCR-M01-03, SCR-M01-04, SCR-M01-05, SCR-M01-06, SCR-M01-07, SCR-M01-08, SCR-M02-03, SCR-M03-01, SCR-M03-04, SCR-M05-02, SCR-M11-02, SCR-M11-07, SCR-M11-08, SCR-M16-03, SCR-M16-04, SCR-M16-06
- **Preview:** design system › `components/TextField/preview.html` · **Figma:** [SCR-M01-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=732-2)

#### TextArea

- **Mục đích:** Ô nhập nhiều dòng có bộ đếm khi FR giới hạn độ dài.
- **Dùng khi:** bio (≤155 ký tự), mô tả báo cáo, lời giải thích khiếu nại, lý do biện pháp, nội dung banner (≤200 ký tự), câu hỏi tham gia nhóm.
- **Không dùng khi:** soạn bài hay bình luận có định dạng (dùng trình soạn với EditorToolbar, CommentComposer).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `label` | `string` | — |  |
  | `rows` | `number` | `4` |  |
  | `maxLength` | `number?` | — | Bộ đếm |
  | `hint / error` | `string?` | — |  |
  | `optional` | `boolean` | `false` |  |

- **Biến thể và trạng thái:**
  - Cùng trạng thái với TextField; cao tối thiểu 104px, kéo giãn theo chiều dọc.
  - Bộ đếm đổi sang `danger` kèm chữ khi vượt giới hạn.
- **Dữ liệu cần có:**
  - Nhãn, giới hạn độ dài theo FR, câu lỗi của SC ("Vui lòng nhập lý do").
- **A11y:**
  - Bộ đếm có `aria-live="polite"` để đọc khi gần chạm giới hạn.
- **Class CSS** (`components.css`): `is-field`, `is-input` (trên `textarea`), `is-field__count`
- **Token:** như TextField
- **Dùng ở:** SCR-M01-03, SCR-M02-03, SCR-M03-02, SCR-M03-05, SCR-M04-01, SCR-M05-05, SCR-M08-01, SCR-M08-04, SCR-M09-01, SCR-M09-04, SCR-M10-05, SCR-M11-02, SCR-M11-04, SCR-M11-08, SCR-M11-10, SCR-M16-01, SCR-M16-02
- **Preview:** design system › `components/TextArea/preview.html` · **Figma:** [SCR-M01-03--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=447-2)

#### Select

- **Mục đích:** Chọn một giá trị trong danh sách ngắn, cố định.
- **Dùng khi:** Lớp/Khối (10, 11, 12, Chưa khai), sắp xếp (Liên quan / Mới nhất / Nhiều upvote nhất), lý do báo cáo trong bộ lọc.
- **Không dùng khi:** dưới 4 lựa chọn cần thấy ngay (dùng Radio hoặc SegmentedControl) hoặc danh sách dài cần tìm (dùng Combobox).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `label` | `string` | — |  |
  | `options` | `{value, label}[]` | — | Danh sách ngắn, cố định |
  | `value` | `string` | — |  |
  | `size` | `'md' \| 'sm'` | `'md'` | `sm` trong bộ lọc quản trị |
  | `error` | `string?` | — |  |

- **Biến thể và trạng thái:**
  - Mặc định, focus, tắt; cỡ nhỏ `--sm` trong bộ lọc.
  - Dùng `<select>` thật, mũi tên là icon trang trí.
- **Dữ liệu cần có:**
  - Nhãn và các lựa chọn bằng tiếng Việt; lựa chọn mặc định theo FR.
- **A11y:**
  - `<label for>`; mũi tên `aria-hidden`.
- **Class CSS** (`components.css`): `is-selectwrap`, `is-input is-select`
- **Token:** `line-strong`, `ink-muted`, `focus`
- **Dùng ở:** SCR-M01-03, SCR-M02-03, SCR-M03-01, SCR-M05-03, SCR-M06-02, SCR-M08-02, SCR-M08-06, SCR-M09-03, SCR-M10-01, SCR-M10-06, SCR-M11-09
- **Preview:** design system › `components/Select/preview.html` · **Figma:** [SCR-M01-03--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=447-2)

#### Checkbox

- **Mục đích:** Bật hoặc tắt một lựa chọn độc lập, hoặc chọn nhiều trong một nhóm.
- **Dùng khi:** đồng ý chính sách khi đăng ký, chọn nhiều lựa chọn của bình chọn, "chỉ nội dung đang theo dõi" trong bộ lọc, danh sách việc cần làm trong bài.
- **Không dùng khi:** bật/tắt có hiệu lực ngay (dùng Switch).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `label` | `ReactNode` | — | Nhãn bấm được |
  | `checked` | `boolean` | `false` |  |
  | `indeterminate` | `boolean` | `false` | Chọn tất cả dòng trong bảng |
  | `description` | `string?` | — |  |

- **Biến thể và trạng thái:**
  - Chưa chọn, đã chọn, focus, tắt; màu `primary` qua `accent-color`.
  - Nhóm dùng `fieldset` + `legend`.
- **Dữ liệu cần có:**
  - Nhãn đứng sau ô, bấm vào nhãn cũng chọn được.
- **A11y:**
  - `<input type="checkbox">` thật trong `<label>`.
- **Class CSS** (`components.css`): `is-check`, `is-fieldset`
- **Token:** `primary`, `line-strong`
- **Dùng ở:** SCR-M01-01, SCR-M03-01, SCR-M03-02, SCR-M06-02
- **Preview:** design system › `components/Checkbox/preview.html` · **Figma:** [SCR-M01-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=732-2)

#### Radio

- **Mục đích:** Chọn đúng một trong vài lựa chọn luôn hiện.
- **Dùng khi:** lý do báo cáo, Public/Private khi tạo nhóm, chọn một của bình chọn, hình thức ban.
- **Không dùng khi:** nhiều hơn 6 lựa chọn (dùng Select) hoặc chuyển chế độ xem (dùng SegmentedControl, Tabs).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `name` | `string` | — |  |
  | `options` | `{value, label, description?}[]` | — | Bọc trong `fieldset` + `legend` |
  | `value` | `string` | — |  |

- **Biến thể và trạng thái:**
  - Chưa chọn, đã chọn, focus, tắt.
  - Lựa chọn có giải thích: dòng phụ `caption` dưới nhãn.
- **Dữ liệu cần có:**
  - `fieldset` với `legend` là câu hỏi; mỗi lựa chọn một nhãn.
- **A11y:**
  - `<input type="radio">` cùng `name`; di chuyển bằng phím mũi tên.
- **Class CSS** (`components.css`): `is-fieldset`, `is-check`
- **Token:** `primary`
- **Dùng ở:** SCR-M03-01, SCR-M08-01, SCR-M08-04, SCR-M09-04, SCR-M11-02, SCR-M11-08
- **Preview:** design system › `components/Radio/preview.html` · **Figma:** [SCR-M08-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=684-2)

#### Switch

- **Mục đích:** Công tắc bật/tắt có hiệu lực ngay, không cần nút Lưu.
- **Dùng khi:** công tắc cấu hình hệ thống (AI tổng, Search, Moderation, Topic suggestion, bảo trì, tạm dừng đăng ký, cờ Group/Chat/Gamification), bật/tắt popup Chat, duyệt trước khi đăng trong nhóm.
- **Không dùng khi:** lựa chọn trong form chỉ có hiệu lực khi bấm Lưu (dùng Checkbox).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `label` | `string` | — | Nói điều được bật, không nói trạng thái |
  | `description` | `string?` | — | Hậu quả khi bật |
  | `checked` | `boolean` | `false` | Có hiệu lực ngay, không cần nút Lưu |
  | `disabled` | `boolean` | `false` |  |

- **Biến thể và trạng thái:**
  - Tắt: viền `line-strong`, núm `ink-muted`; bật: nền `primary`, núm `on-primary`; focus; tắt hẳn (disabled).
  - Có dòng mô tả hậu quả dưới nhãn khi cần ("Chỉ tài khoản ADMIN dùng được hệ thống").
- **Dữ liệu cần có:**
  - Nhãn nói điều được bật, không phải trạng thái ("Chế độ bảo trì", không "Đang bật").
- **A11y:**
  - `<button role="switch" aria-checked>`; trạng thái đọc được, không chỉ dựa vào màu (vị trí núm).
- **Class CSS** (`components.css`): `is-switch`, `is-switch__track`, `is-switch__thumb`
- **Token:** `primary`, `on-primary`, `line-strong`, `ink-muted`, `radius-full`
- **Dùng ở:** SCR-M03-01, SCR-M06-02, SCR-M10-04, SCR-M11-02, SCR-M11-08, SCR-M16-04
- **Preview:** design system › `components/Switch/preview.html` · **Figma:** [SCR-M10-04--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=597-2)

#### FileDrop

- **Mục đích:** Vùng thêm tệp: có nút Chọn tệp, kéo-thả chỉ là cách thêm (QF-10).
- **Dùng khi:** đính kèm ảnh, tài liệu vào bài; ảnh bằng chứng của báo cáo, khiếu nại.
- **Không dùng khi:** chọn ảnh đại diện (dùng AvatarUpload).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `accept` | `string` | — | Loại tệp FR cho phép |
  | `maxSize` | `number` | — | Byte |
  | `multiple` | `boolean` | `true` |  |
  | `error` | `string?` | — |  |
  | `onFiles` | `(f: File[]) => void` | — | Từ nút Chọn tệp hoặc kéo-thả |

- **Biến thể và trạng thái:**
  - Mặc định (viền nét đứt), đang kéo tệp vào (`is-dragover`, nền `primary-soft`), lỗi (viền `danger` + câu lỗi).
  - Tệp đã thêm hiện bằng Attachment ngay dưới vùng, có nút gỡ.
- **Dữ liệu cần có:**
  - Giới hạn theo FR ngay trong vùng: ảnh JPEG/PNG/WebP ≤5 MB, tối đa 10 ảnh; tài liệu PDF/DOCX/XLSX/PPTX ≤20 MB, tối đa 3 tệp.
  - Câu lỗi nói rõ tệp nào và vì sao ("anh-bai-tap.gif: chỉ nhận JPEG, PNG hoặc WebP").
- **A11y:**
  - Nút Chọn tệp là `<button>` mở `<input type="file">`; lỗi nối bằng `aria-describedby`.
- **Class CSS** (`components.css`): `is-drop`, `is-drop.is-dragover`, `is-drop__ic`
- **Token:** `line-strong`, `primary`, `primary-soft`, `danger`
- **Dùng ở:** SCR-M03-01, SCR-M08-01, SCR-M09-01
- **Preview:** design system › `components/FileDrop/preview.html` · **Figma:** [SCR-M03-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=194-2)

#### SearchField

- **Mục đích:** Ô tìm kiếm bo tròn hai đầu trên thanh trên cùng (DD-UI-09).
- **Dùng khi:** tìm bài viết, người dùng, Tag, Chủ đề, nhóm từ mọi trang; ô lọc danh sách trong khu quản trị dùng TextField có icon.
- **Không dùng khi:** lọc theo giá trị cố định (dùng FilterBar).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `value` | `string` | — |  |
  | `placeholder` | `string` | `"Tìm bài viết, Chủ đề, Tag, người dùng, nhóm"` |  |
  | `onSubmit` | `(q: string) => void` | — | Đi tới `/search?q=` |
  | `suggestions` | `ReactNode?` | — | Popover gợi ý khi gõ (SCR-M06-01) |

- **Biến thể và trạng thái:**
  - Mặc định (nền `bg`), rê chuột, focus (nền `surface`, viền `focus`) mở gợi ý (Combobox), có chữ (nút Xóa), lỗi giới hạn tần suất (dòng lỗi trong gợi ý).
  - Rộng tối đa 560px, nằm giữa logo và nhóm nút bên phải.
- **Dữ liệu cần có:**
  - Placeholder gợi ý phạm vi tìm: "Tìm bài viết, Chủ đề, Tag, người dùng, nhóm".
- **A11y:**
  - `role="search"` trên form; `<label class="is-sr">`; khi mở gợi ý dùng mẫu combobox (xem Combobox).
- **Class CSS** (`components.css`): `is-search`, `is-search__clear`
- **Token:** `bg`, `surface`, `line-strong`, `focus`, `radius-full`, `control-h`
- **Dùng ở:** 32/75 màn hình (gần như mọi trang)
- **Preview:** design system › `components/SearchField/preview.html` · **Figma:** [SCR-SHARED-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=96-2)

#### TagInput

- **Mục đích:** Chọn nhiều giá trị thành chip trong một ô: Tag (gõ tự do, có gợi ý) hoặc Chủ đề (chọn trong danh mục, có gợi ý của AI).
- **Dùng khi:** gắn Tag (≤5) và Chủ đề (1–3) khi viết bài, khi Mod đổi Chủ đề/Tag; chọn thành viên khi tạo nhóm chat.
- **Không dùng khi:** chọn một giá trị (dùng Select hoặc Combobox).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `mode` | `'tag' \| 'topic'` | `'tag'` |  |
  | `value` | `string[]` | `[]` |  |
  | `max` | `number` | — | Tag ≤5, Chủ đề 1–3 |
  | `suggestions` | `Option[]` | — | Gợi ý khi gõ; Chủ đề: gợi ý của AI |
  | `aiEnabled` | `boolean` | `true` | Ẩn dòng Gợi ý chủ đề khi AI tắt |
  | `error` | `string?` | — |  |

- **Biến thể và trạng thái:**
  - Chế độ Tag: chip Tag có nút gỡ, ô gõ còn lại; gõ ra danh sách gợi ý (Combobox).
  - Chế độ Chủ đề: chip TopicChip; dòng "Gợi ý chủ đề" với chip nét đứt bấm để thêm — ẩn khi AI tắt (FR-M05).
  - Đã đủ số lượng: ô gõ tắt, gợi ý "Đã đủ 5 Tag"; lỗi thiếu Chủ đề: viền `danger` + câu lỗi.
  - Chip không rộng quá ô; tên dài ("Khoa học tự nhiên (Lý/Hóa/Sinh)") xuống dòng trong chip, không tràn ô (QA-F-02).
- **Dữ liệu cần có:**
  - Danh sách đã chọn, giới hạn theo FR, nguồn gợi ý.
- **A11y:**
  - Mỗi chip có nút gỡ với `aria-label` "Gỡ Tag #daiso"; Backspace ở ô trống gỡ chip cuối.
- **Class CSS** (`components.css`): `is-taginput`, `is-tag`, `is-tag__x`, `is-topic`, `is-topic--suggest`
- **Token:** `line-strong`, `focus`, `primary`, `primary-soft`, `danger`
- **Dùng ở:** SCR-M03-01, SCR-M05-05, SCR-M16-03
- **Preview:** design system › `components/TagInput/preview.html` · **Figma:** [SCR-M03-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=194-2)

#### SegmentedControl

- **Mục đích:** Nhóm 2–5 lựa chọn liền nhau, chọn đúng một, đổi ngay cách xem dữ liệu.
- **Dùng khi:** khoảng thời gian của trang Thống kê (Hôm nay, 7 ngày, 30 ngày, Toàn thời gian), lọc Lớp/Khối ở Bảng xếp hạng, sắp xếp bình luận (Top / Mới nhất / Cũ nhất).
- **Không dùng khi:** chuyển giữa các trang con có nội dung khác hẳn (dùng Tabs).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `options` | `{value, label}[]` | — | 2–5 lựa chọn |
  | `value` | `string` | — |  |
  | `label` | `string` | — | Nhãn nhóm (`radiogroup`) |

- **Biến thể và trạng thái:**
  - Đã chọn: nền `primary-soft`, chữ `primary`; rê chuột; focus.
- **Dữ liệu cần có:**
  - Nhãn ngắn; lựa chọn mặc định theo FR (Thống kê mở sẵn Toàn thời gian).
- **A11y:**
  - `role="radiogroup"` + `role="radio"` với `aria-checked`; phím mũi tên chuyển lựa chọn.
- **Class CSS** (`components.css`): `is-seg`, `is-seg__opt`
- **Token:** `primary-soft`, `primary`, `line-strong`, `control-h-sm`
- **Dùng ở:** SCR-M03-02, SCR-M04-01, SCR-M12-01, SCR-M15-01, SCR-M15-02, SCR-M15-03
- **Preview:** design system › `components/SegmentedControl/preview.html` · **Figma:** [SCR-M03-02--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=659-2)

#### Combobox

- **Mục đích:** Ô gõ kèm danh sách gợi ý thả xuống; chọn bằng chuột hoặc phím mũi tên.
- **Dùng khi:** gợi ý khi gõ ở ô tìm kiếm (người dùng, Tag, Chủ đề, nhóm + 10 truy vấn gần nhất), @nhắc tên trong trình soạn, mời vào nhóm, thêm thành viên nhóm chat, gõ Tag.
- **Không dùng khi:** danh sách ngắn cố định (dùng Select).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `label` | `string` | — |  |
  | `value` | `string` | — |  |
  | `options` | `Option[]` | — | Có thể tải theo chữ gõ |
  | `allowCreate` | `boolean` | `false` | Tạo Tag mới |
  | `emptyText` | `string` | — | "Không có kết quả" |

- **Biến thể và trạng thái:**
  - Lịch sử (ô trống): 10 truy vấn gần nhất, nút "Xóa toàn bộ".
  - Gợi ý theo nhóm (Người dùng, Tag, Chủ đề, Nhóm), phần khớp in đậm; mục đang trỏ nền `surface-hover`.
  - Không có kết quả: một dòng "Không có gợi ý cho …"; lỗi giới hạn tần suất: dòng lỗi `danger`.
- **Dữ liệu cần có:**
  - Danh sách gợi ý theo FR-M06; mỗi mục có icon hoặc avatar nhận diện loại.
- **A11y:**
  - Mẫu combobox ARIA: ô `role="combobox"` `aria-expanded` `aria-controls`, danh sách `role="listbox"`, mục `role="option"` với `aria-selected`; Esc đóng.
- **Class CSS** (`components.css`): `is-pop`, `is-pop__group`, `is-opt`, `is-opt__ic`, `is-opt__sub`
- **Token:** `surface-raised`, `shadow-1`, `surface-hover`, `ink-muted`
- **Dùng ở:** SCR-M06-01
- **Preview:** design system › `components/Combobox/preview.html` · **Figma:** [SCR-M06-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=477-2)

#### DateTimeField

- **Mục đích:** Chọn ngày và giờ, hiển thị theo giờ Việt Nam.
- **Dùng khi:** hạn kết thúc bình chọn khi tạo và khi đổi hạn (FR-M03-03.07, FR-M03-09.01).
- **Không dùng khi:** khoảng thời gian cố định của Thống kê (dùng SegmentedControl).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `label` | `string` | — |  |
  | `value` | `Date` | — | Hiển thị giờ Việt Nam |
  | `min / max` | `Date?` | — | Ví dụ hạn bình chọn |
  | `error` | `string?` | — |  |

- **Biến thể và trạng thái:**
  - Mặc định, focus, lỗi (hạn trước thời điểm hiện tại), tắt (bình chọn đã đóng).
  - Dùng ô `datetime-local` của trình duyệt; theme tối nhờ `color-scheme`.
  - Ô gốc hiện ngày theo ngôn ngữ của trình duyệt; nếu cần cố định dd/mm/yyyy cho mọi máy, thay bằng bộ chọn ngày ở bước code nhưng giữ nhãn, gợi ý, lỗi như trên.
- **Dữ liệu cần có:**
  - Giá trị mặc định nếu FR có; câu lỗi của FR: "Hạn kết thúc phải sau thời điểm hiện tại".
- **A11y:**
  - `<label for>`; định dạng hiển thị dd/mm/yyyy, hh:mm nêu trong gợi ý.
- **Class CSS** (`components.css`): `is-field`, `is-input`
- **Token:** như TextField
- **Dùng ở:** SCR-M03-01, SCR-M03-04
- **Preview:** design system › `components/DateTimeField/preview.html` · **Figma:** [SCR-M03-04--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=154-2)

#### AvatarUpload

- **Mục đích:** Chọn ảnh đại diện, xem trước dạng tròn ngay tại chỗ.
- **Dùng khi:** bước Thiết lập tài khoản (SCR-M01-03) và trang Sửa hồ sơ (SCR-M02-03).
- **Không dùng khi:** đính kèm ảnh vào bài (dùng FileDrop).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `src` | `string?` | — |  |
  | `name` | `string` | — | Chữ cái đầu khi chưa có ảnh |
  | `maxSize` | `number` | — |  |
  | `onChange` | `(f: File \| null) => void` | — | Chọn ảnh, gỡ ảnh |
  | `error` | `string?` | — |  |

- **Biến thể và trạng thái:**
  - Chưa có ảnh: avatar chữ cái đầu; có ảnh: xem trước tròn và nút Gỡ ảnh; lỗi định dạng/dung lượng.
- **Dữ liệu cần có:**
  - Giới hạn FR: JPEG, PNG hoặc WebP, ≤5 MB; ảnh hiển thị cắt tròn (FR-M02).
- **A11y:**
  - Nút Chọn ảnh mở `<input type="file" accept>`; ảnh xem trước có `alt` "Ảnh đại diện mới".
- **Class CSS** (`components.css`): `is-avup`, `is-avatar--lg`
- **Token:** `avatar-lg`, `radius-full`, `primary-soft`
- **Dùng ở:** SCR-M01-03, SCR-M02-03
- **Preview:** design system › `components/AvatarUpload/preview.html` · **Figma:** [SCR-M01-03--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=447-2)

### 4.5 Danh sách

#### ListItem

- **Mục đích:** Dòng danh sách chung: phần đầu (icon hoặc avatar), tiêu đề, dòng phụ, thao tác bên phải.
- **Dùng khi:** danh sách Chủ đề và Tag (nút Theo dõi), các phiên bản ở Lịch sử sửa bài, danh sách chặn tham gia nhóm, yêu cầu tham gia chờ duyệt, mục cài đặt.
- **Không dùng khi:** người dùng (dùng UserRow), bài (PostCard), dữ liệu nhiều cột cần sắp xếp (DataTable).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `leading` | `ReactNode?` | — | Icon hoặc Avatar |
  | `title` | `ReactNode` | — |  |
  | `subtitle` | `ReactNode?` | — |  |
  | `actions` | `ReactNode?` | — | Nút ở cuối dòng |
  | `href` | `string?` | — | Cả dòng là liên kết |
  | `compact` | `boolean` | `false` | `--compact` (`row-h-sm` 38px) cho khu quản trị |
  | `current` | `boolean` | `false` | `aria-current`, nền `primary-soft` |

- **Biến thể và trạng thái:**
  - Mật độ vừa (cao tối thiểu `row-h` 52px) và gọn (`--compact`, `row-h-sm` 38px) cho khu quản trị.
  - Cả dòng là liên kết (rê chuột `surface-hover`) hoặc dòng tĩnh có nút ở cuối; đang chọn `aria-current` nền `primary-soft`.
- **Dữ liệu cần có:**
  - Tiêu đề, dòng phụ (cắt bằng …), icon hoặc avatar, thao tác.
- **A11y:**
  - Danh sách là `<ul>`; dòng là `<li>`; một liên kết chính mỗi dòng, các nút phụ có nhãn riêng.
- **Class CSS** (`components.css`): `is-list`, `is-li`, `is-li--compact`, `is-li__lead`, `is-li__main`, `is-li__title`, `is-li__sub`, `is-li__end`
- **Token:** `row-h`, `row-h-sm`, `line`, `surface-hover`, `primary-soft`
- **Dùng ở:** SCR-M02-01, SCR-M02-02, SCR-M03-01, SCR-M03-04, SCR-M05-01, SCR-M11-05, SCR-M11-07, SCR-M11-11, SCR-M12-01, SCR-M16-04, SCR-M16-06
- **Preview:** design system › `components/ListItem/preview.html` · **Figma:** [SCR-M02-02--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=214-2)

#### UserRow

- **Mục đích:** Dòng một người dùng: avatar, tên hiển thị, @username, Lớp/Khối, nhãn vai trò, thao tác.
- **Dùng khi:** người theo dõi / đang theo dõi, thành viên nhóm, kết quả tìm người, mời vào nhóm, thành viên nhóm chat.
- **Không dùng khi:** bảng quản trị người dùng nhiều cột (dùng DataTable).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `user` | `UserSummary` | — | Avatar, tên, @username, Lớp/Khối, vai trò |
  | `actions` | `ReactNode?` | — | Theo dõi, nhắn tin, gỡ khỏi nhóm… |
  | `roleLabel` | `string?` | — | Owner, Group Mod, Mod, Admin |

- **Biến thể và trạng thái:**
  - Thao tác theo ngữ cảnh: Theo dõi / Đang theo dõi, Nhắn tin, menu "…" (Bổ nhiệm Group Mod, Giáng, Kick).
  - Nhãn vai trò bằng StatusLabel: Owner, Group Mod, Mod, Admin; nhãn tài khoản: Tài khoản đã bị khóa.
  - Tài khoản đã xóa: "[Người dùng đã xóa]", avatar trung tính, không liên kết.
- **Dữ liệu cần có:**
  - Tên hiển thị, username, Lớp/Khối (nếu có), vai trò trong ngữ cảnh, quan hệ theo dõi.
- **A11y:**
  - Tên là liên kết tới hồ sơ; nút Theo dõi có `aria-pressed`.
- **Class CSS** (`components.css`): `is-li` + `is-avatar` + `is-status`
- **Token:** như ListItem
- **Dùng ở:** SCR-M02-02, SCR-M11-05, SCR-M11-07, SCR-M11-11, SCR-M16-04, SCR-M16-06
- **Preview:** design system › `components/UserRow/preview.html` · **Figma:** [SCR-M02-02--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=214-2)

#### GroupCard

- **Mục đích:** Thẻ một nhóm: Public/Private, tên, mô tả 2 dòng, số thành viên, nút tham gia theo trạng thái.
- **Dùng khi:** Danh sách nhóm (SCR-M11-01), kết quả phụ "Nhóm" của trang tìm kiếm.
- **Không dùng khi:** trang nhóm (đầu trang nhóm dựng từ cùng thành phần nhưng rộng hơn).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `group` | `GroupSummary` | — | Tên, mô tả, Public/Private, số thành viên |
  | `relation` | `'none' \| 'pending' \| 'member' \| 'guest'` | `'none'` | Tham gia (Public) / Gửi yêu cầu (Private), Rút yêu cầu, Đã tham gia; Guest: "Đăng nhập để tham gia" |
  | `locked` | `boolean` | `false` | Nhóm bị Mod khóa: StatusLabel "Bị khóa", không có nút tham gia |
  | `headingLevel` | `2 \| 3` | `2` | Theo ngữ cảnh (QF-17) |
  | `onAction` | `() => void` | — |  |

- **Biến thể và trạng thái:**
  - Nút theo quan hệ: Tham gia (Public), Gửi yêu cầu (Private), Rút yêu cầu (đang chờ), Đã tham gia (thành viên, mở menu Rời nhóm).
  - Nhóm bị Mod khóa: StatusLabel "Bị khóa", không có nút tham gia.
  - Chân thẻ: số thành viên luôn một dòng; thiếu chỗ thì nút xuống hàng dưới, không tràn khỏi thẻ (QA-F-01).
- **Dữ liệu cần có:**
  - Tên, mô tả, Public/Private, số thành viên, quan hệ của người xem.
- **A11y:**
  - Thẻ là `<article>`; tên nhóm là `h2` khi danh sách nằm ngay dưới `h1`, `h3` trong một mục có `h2` (QF-17); nút nói rõ việc ("Gửi yêu cầu tham gia CLB Toán").
- **Class CSS** (`components.css`): `is-group`, `is-group__name`, `is-group__desc`, `is-group__foot`
- **Token:** `surface`, `line`, `radius-sm`
- **Dùng ở:** SCR-M11-01
- **Preview:** design system › `components/GroupCard/preview.html` · **Figma:** [SCR-M11-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=698-2)

#### LeaderboardRow

- **Mục đích:** Một dòng bảng xếp hạng: thứ hạng, avatar, tên kèm username, dấu Ngôi sao tuần (chỉ tab Tuần), điểm trong chu kỳ (BR-M12-29).
- **Dùng khi:** Bảng xếp hạng (SCR-M12-01), trình bày tiết chế (DD-UI-05): không cúp, không màu vàng bạc đồng.
- **Không dùng khi:** danh sách người theo dõi (dùng UserRow).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `rank` | `number` | — | Đồng hạng hiện cùng số |
  | `user` | `UserSummary` | — | Tên hiển thị, username |
  | `points` | `number` | — | Điểm trong chu kỳ |
  | `weeklyStar` | `boolean` | `false` | Chỉ tab Tuần |
  | `me` | `boolean` | `false` | Dòng của người đang xem |
  | `deleted` | `boolean` | `false` | "[Người dùng đã xóa]" |

- **Biến thể và trạng thái:**
  - Đồng hạng hiện cùng số; dòng của người đang xem nền `primary-soft`.
  - Tài khoản đã xóa sau khi chốt: "[Người dùng đã xóa]", chữ `ink-muted` (BR-M12-21).
- **Dữ liệu cần có:**
  - Thứ hạng, tên hiển thị, username, điểm trong chu kỳ, có Ngôi sao tuần không.
- **A11y:**
  - Danh sách có thứ tự `<ol>`; điểm có chữ "điểm".
- **Class CSS** (`components.css`): `is-rank`, `is-rank__n`, `is-rank__score`, `is-rank--me`, `is-rank--deleted`, `is-star`
- **Token:** `primary-soft`, `primary`, `ink-muted`
- **Dùng ở:** SCR-M12-01
- **Preview:** design system › `components/LeaderboardRow/preview.html` · **Figma:** [SCR-M12-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=223-2)

### 4.6 Thông báo và chat

#### NotificationItem

- **Mục đích:** Một thông báo: ai hoặc hệ thống, việc gì, lúc nào; bấm đi tới nội dung (FR-M07).
- **Dùng khi:** ngăn thông báo (Popover, 10 mục gần nhất) và trang Thông báo (tải thêm 20).
- **Không dùng khi:** thông báo tức thời sau thao tác của chính người dùng (dùng Toast).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `notification` | `NotificationData` | — | Người gây sự kiện hoặc hệ thống, nội dung, thời điểm, đích |
  | `unread` | `boolean` | `false` |  |
  | `actions` | `ReactNode?` | — | Chấp nhận/Từ chối đề xuất vai trò; Khiếu nại |
  | `expired` | `boolean` | `false` | "Đã hết hạn" |

- **Biến thể và trạng thái:**
  - Chưa đọc: chữ đậm 600 + chấm `primary` có nhãn "Chưa đọc"; đã đọc: chữ thường.
  - Thông báo của hệ thống (kiểm duyệt, huy hiệu): ô icon trung tính thay avatar.
  - Đề xuất làm Mod/Admin: hai nút Chấp nhận / Từ chối ngay trên dòng; hết hạn: chữ "Đề xuất đã hết hạn" thay nút (SCR-M07-02).
  - Thông báo xử lý (cảnh cáo, ẩn bài): giọng tôn trọng, có lý do và nút Khiếu nại khi được phép (PRODUCT.md mục 8).
- **Dữ liệu cần có:**
  - Chủ thể, hành động, đối tượng, thời điểm, đã đọc chưa, đích liên kết.
- **A11y:**
  - Mỗi thông báo là một liên kết; nút trong dòng không lồng trong liên kết (dòng có nút dùng `div`).
- **Class CSS** (`components.css`): `is-noti`, `is-noti--unread`, `is-noti__ic`, `is-noti__text`, `is-noti__time`, `is-noti__acts`, `is-dot`
- **Token:** `primary`, `surface-hover`, `ink-muted`
- **Dùng ở:** SCR-M07-01, SCR-M07-02
- **Preview:** design system › `components/NotificationItem/preview.html` · **Figma:** [SCR-M07-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=340-2)

#### ConversationItem

- **Mục đích:** Một cuộc trò chuyện trong Hộp thư Chat: tên (người hoặc nhóm chat), tin gần nhất, thời điểm, số tin chưa đọc.
- **Dùng khi:** Hộp thư Chat (SCR-M16-01), mới nhất ở trên.
- **Không dùng khi:** thông báo (dùng NotificationItem).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `conversation` | `ConversationSummary` | — | Tên, avatar, tin gần nhất ("Bạn: …"), thời điểm |
  | `unread` | `number` | `0` | Counter |
  | `current` | `boolean` | `false` | `aria-current` |
  | `muted` | `boolean` | `false` | Đã tắt popup cuộc này |

- **Biến thể và trạng thái:**
  - Có tin chưa đọc: tin gần nhất đậm + Counter; đang mở: nền `primary-soft`; đã tắt popup cuộc này: icon chuông gạch.
  - Tên và tin gần nhất mỗi thứ một dòng, dài thì cắt bằng dấu "…", không chạy vào cột thời điểm và số chưa đọc (QA-F-03).
- **Dữ liệu cần có:**
  - Tên, avatar (nhóm chat: chữ cái đầu tên nhóm), tin gần nhất ("Bạn: …" nếu của mình), thời điểm, số chưa đọc.
- **A11y:**
  - Mỗi dòng là liên kết; số chưa đọc có nhãn đầy đủ.
- **Class CSS** (`components.css`): `is-convo`, `is-convo--unread`, `is-convo__main`, `is-convo__name`, `is-convo__last`, `is-convo__end`
- **Token:** `primary-soft`, `primary`, `ink-muted`
- **Dùng ở:** SCR-M16-01, SCR-M16-02
- **Preview:** design system › `components/ConversationItem/preview.html` · **Figma:** [SCR-M16-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=701-2)

#### MessageBubble

- **Mục đích:** Tin nhắn trong cuộc trò chuyện: tin của người khác bên trái, của mình bên phải nền `primary-soft`.
- **Dùng khi:** Cuộc trò chuyện 1-1 và nhóm chat (SCR-M16-02).
- **Không dùng khi:** bình luận bài (dùng Comment).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `message` | `Message` | — | Người gửi, nội dung, thời điểm |
  | `mine` | `boolean` | `false` | Tin của mình (`--out`) |
  | `showSender` | `boolean` | `false` | Nhóm chat: tên người gửi ở tin đầu chuỗi |
  | `recalled` | `boolean` | `false` | "Tin nhắn đã được thu hồi", khung nét đứt |
  | `seen` | `boolean` | `false` | "Đã xem" dưới tin mới nhất của mình |
  | `system` | `boolean` | `false` | Tin hệ thống căn giữa |

- **Biến thể và trạng thái:**
  - Nhóm chat: tên người gửi trên tin đầu của chuỗi; 1-1: không có tên.
  - "Đã xem" dưới tin mới nhất của mình; tin đã thu hồi (trong 5 phút): khung nét đứt, chữ nghiêng "Tin nhắn đã được thu hồi".
  - Tin hệ thống (thêm thành viên, đổi tên nhóm) căn giữa; dải ngày ngăn theo ngày.
  - Đang đọc tin cũ mà có tin mới: nút "Tin mới" để nhảy xuống (SC-M16-003).
- **Dữ liệu cần có:**
  - Nội dung, người gửi, thời điểm, đã xem, đã thu hồi.
- **A11y:**
  - Danh sách tin có `role="log"` và `aria-live="polite"`; thời điểm đọc được.
- **Class CSS** (`components.css`): `is-msgs`, `is-msg`, `is-msg--out`, `is-bubble`, `is-msg__meta`, `is-msg--recalled`, `is-sysmsg`, `is-datesep`
- **Token:** `primary-soft`, `surface`, `line`, `bg`, `body-comment`
- **Dùng ở:** SCR-M16-01, SCR-M16-02
- **Preview:** design system › `components/MessageBubble/preview.html` · **Figma:** [SCR-M16-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=701-2)

#### NewMessagePopup

- **Mục đích:** Popup nhỏ góc dưới phải khi có tin nhắn mới lúc người dùng ở trang khác (SCR-M07-03).
- **Dùng khi:** mọi trang trừ trang Chat; tắt được cho từng cuộc hoặc toàn bộ Chat.
- **Không dùng khi:** thông báo không phải tin nhắn (dùng ngăn thông báo).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `conversation` | `ConversationSummary` | — |  |
  | `preview` | `string` | — |  |
  | `onOpen / onDismiss` | `() => void` | — |  |

- **Biến thể và trạng thái:**
  - Một popup mỗi lúc, tin mới thay tin cũ; tự ẩn sau một lúc; nút Đóng; bấm vào mở cuộc trò chuyện.
- **Dữ liệu cần có:**
  - Người gửi, nhóm chat (nếu có), đầu tin nhắn.
- **A11y:**
  - `role="status"`, không cướp focus; nút Đóng có nhãn.
- **Class CSS** (`components.css`): `is-popup`
- **Token:** `surface-raised`, `shadow-1`, `radius-sm`
- **Dùng ở:** SCR-M07-03
- **Preview:** design system › `components/NewMessagePopup/preview.html` · **Figma:** [SCR-M07-03--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=351-2)

### 4.7 Quản trị

#### DataTable

- **Mục đích:** Bảng dữ liệu nhiều cột của khu kiểm duyệt và quản trị: tiêu đề cột sắp xếp được, dòng chọn được, chân bảng có phân trang.
- **Dùng khi:** Hàng chờ báo cáo, duyệt bài, khiếu nại; Nhật ký kiểm duyệt, Nhật ký Admin; Người dùng; Quản lý Chủ đề, Tag; số liệu theo nhóm ở Thống kê.
- **Không dùng khi:** danh sách cho học sinh (dùng PostCard, ListItem).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `columns` | `Column[]` | — | Tiêu đề, căn số phải, sắp xếp được |
  | `rows` | `T[]` | — |  |
  | `sort` | `{key, dir}?` | — | `aria-sort` |
  | `selectable` | `boolean` | `false` | Ô chọn mỗi dòng |
  | `density` | `'compact'` | `'compact'` | Dòng 38px (DD-UI-30) |
  | `footer` | `ReactNode?` | — | Pagination |
  | `emptyState / loading` | `ReactNode / boolean` | — |  |

- **Biến thể và trạng thái:**
  - Mật độ gọn (`--compact`, dòng 38px, chữ 14px) là mặc định ở khu kiểm duyệt và quản trị (DD-UI-30); mật độ vừa (dòng 52px) khi bảng đứng trong trang của học sinh.
  - Cột đang sắp xếp: `aria-sort` + mũi tên; rê chuột dòng `surface-hover`; dòng đang chọn (mở chi tiết ở ngăn phải) `primary-soft`.
  - Trống: EmptyState trong khung bảng; đang tải: Skeleton dòng; không có kết quả lọc: câu "Không có vụ nào khớp bộ lọc" + Xóa bộ lọc.
  - Số căn phải, chữ số đều (tabular); chữ dài cắt bằng … và có đầy đủ khi mở chi tiết.
- **Dữ liệu cần có:**
  - Cột, dòng, cách sắp xếp mặc định theo FR (hàng chờ: ưu tiên giảm dần), tổng số, trang.
- **A11y:**
  - `<table>` thật có `caption` (có thể ẩn), `th scope="col"`; nút sắp xếp trong `th`; bảng rộng cuộn ngang trong khung (QF-12).
- **Class CSS** (`components.css`): `is-tablebox`, `is-table`, `is-table--compact`, `is-num`, `is-trunc`, `is-sort`, `is-tablefoot`
- **Token:** `row-h`, `row-h-sm`, `bg`, `line`, `surface-hover`, `primary-soft`
- **Dùng ở:** SCR-M05-02, SCR-M05-04, SCR-M08-02, SCR-M08-03, SCR-M08-05, SCR-M08-06, SCR-M09-02, SCR-M09-03, SCR-M10-01, SCR-M10-06, SCR-M15-01, SCR-M15-02, SCR-M15-03
- **Preview:** design system › `components/DataTable/preview.html` · **Figma:** [SCR-M05-02--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=529-2)

#### FilterBar

- **Mục đích:** Hàng bộ lọc phía trên danh sách hoặc bảng; lọc có hiệu lực ngay, chip bộ lọc đang áp dụng có nút gỡ.
- **Dùng khi:** Kết quả tìm kiếm (Chủ đề, Tag, thời gian, chỉ nội dung đang theo dõi, sắp xếp), nhật ký và hàng chờ khu quản trị.
- **Không dùng khi:** chuyển chế độ xem (dùng Tabs, SegmentedControl).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `filters` | `ReactNode` | — | Select, SegmentedControl, ô tìm |
  | `active` | `{key, label}[]` | `[]` | Chip đang áp dụng, có nút gỡ |
  | `onClear` | `() => void` | — | "Xóa bộ lọc" |

- **Biến thể và trạng thái:**
  - Select cỡ nhỏ, Checkbox hoặc Switch, ô tìm có icon; nút "Xóa bộ lọc" khi có bộ lọc khác mặc định.
  - Hàng chip bộ lọc đang áp dụng (Tag có nút gỡ).
- **Dữ liệu cần có:**
  - Bộ lọc và giá trị theo FR: thời gian Hôm nay / Tuần này / Tháng này / Tất cả; sắp xếp Liên quan / Mới nhất / Nhiều upvote nhất.
- **A11y:**
  - Mỗi bộ lọc có nhãn; vùng kết quả cập nhật thông báo số kết quả qua `aria-live`.
- **Class CSS** (`components.css`): `is-filters`, `is-field`, `is-input--sm`, `is-check`
- **Token:** `control-h-sm`, `ink-muted`
- **Dùng ở:** SCR-M08-02, SCR-M08-06, SCR-M09-03, SCR-M10-01, SCR-M10-06
- **Preview:** design system › `components/FilterBar/preview.html` · **Figma:** [SCR-M08-02--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=511-2)

#### StatTile

- **Mục đích:** Ô một chỉ số: nhãn, con số lớn, dòng phụ.
- **Dùng khi:** trang Thống kê (M15): số tài khoản theo trạng thái, vai trò, Lớp/Khối, mức cảnh cáo; số bài theo trạng thái; số báo cáo, khiếu nại theo nhóm.
- **Không dùng khi:** trang của học sinh — không đặt dải thống kê trang trí (AP-24).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `label` | `string` | — | Có thể là tên trạng thái FR (ACTIVE, BANNED…) |
  | `value` | `number \| string` | — |  |
  | `sub` | `string?` | — | Dòng phụ |

- **Biến thể và trạng thái:**
  - Lưới 3 cột; nhóm 0 hiện "0" (FR-M15-01.11); không có dữ liệu cho tỷ lệ: "Chưa có dữ liệu" thay phần trăm (FR-M15-02.08).
  - Đang tải: Skeleton cùng kích thước.
- **Dữ liệu cần có:**
  - Nhãn đúng thuật ngữ FR, giá trị (định dạng số Việt Nam: 1.284), dòng phụ (khoảng thời gian).
- **A11y:**
  - Nhóm ô là danh sách định nghĩa hoặc `role="group"` có nhãn; con số không chỉ thể hiện bằng màu.
- **Class CSS** (`components.css`): `is-tiles`, `is-tile`, `is-tile__label`, `is-tile__value`, `is-tile__sub`
- **Token:** `h1` (con số 26px), `ink-muted`, `line`
- **Dùng ở:** SCR-M15-01, SCR-M15-02, SCR-M15-03
- **Preview:** design system › `components/StatTile/preview.html` · **Figma:** [SCR-M15-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=608-2)

#### TrendChart

- **Mục đích:** Biểu đồ cột xu hướng theo thời gian của trang Thống kê; tối đa 3 chuỗi chồng nhau, khác nhau bằng độ sáng của cùng một sắc.
- **Dùng khi:** xu hướng đăng ký mới, bài viết mới, bình luận mới (một chuỗi `chart-2`); cảnh cáo theo mức LIGHT/MEDIUM/HEAVY (`chart-1/2/3`); ban tạm thời / vĩnh viễn (`chart-1/2`).
- **Không dùng khi:** so sánh các nhóm không theo thời gian (dùng StatTile hoặc DataTable).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `title` | `string` | — | Heading theo ngữ cảnh |
  | `series` | `{name, values}[]` | — | Tối đa 3 chuỗi, `chart-1…3` |
  | `buckets` | `string[]` | — | Cột theo giờ, ngày hoặc tháng tùy khoảng thời gian (FR-M15-01.19) |
  | `headingLevel` | `2 \| 3` | `2` |  |
  | `state` | `'ready' \| 'empty' \| 'loading'` | `'ready'` | Nút "Xem bảng số liệu"; bảng tương đương trong `details` |

- **Biến thể và trạng thái:**
  - Chia cột theo giờ (Hôm nay), ngày (7 hoặc 30 ngày), tháng (Toàn thời gian) — FR-M15-01.19.
  - Chú thích luôn có chữ; nút "Xem bảng số liệu" mở bảng cùng dữ liệu (không chỉ dựa vào màu, QF-03).
  - Trống: trục và dòng "Chưa có dữ liệu trong khoảng này"; đang tải: Skeleton khối.
- **Dữ liệu cần có:**
  - Nhãn trục thời gian, các chuỗi số đếm, tên chuỗi.
- **A11y:**
  - SVG `role="img"` với tiêu đề (heading theo ngữ cảnh, `h2` khi nằm ngay dưới `h1` của trang); bảng số liệu tương đương trong `details`; cột ≥ 3:1 trên `surface`.
- **Class CSS** (`components.css`): `is-chart`, `is-chart__grid`, `is-chart__axis`, `is-chart__s1|s2|s3`, `is-legend`
- **Token:** `chart-1`, `chart-2`, `chart-3`, `line`, `ink-muted`
- **Dùng ở:** SCR-M15-01, SCR-M15-02, SCR-M15-03
- **Preview:** design system › `components/TrendChart/preview.html` · **Figma:** [SCR-M15-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=608-2)

### 4.8 Cấu trúc

#### PageLayout

- **Mục đích:** Khung chia cột của một trang desktop, nằm dưới AppHeader. Mọi màn hình dùng một trong sáu biến thể này, nên khi lập trình chỉ dựng khung một lần.
- **Dùng khi:** mọi trang. Ba cột (mặc định): chi tiết bài, trình soạn, kết quả tìm kiếm, hồ sơ. Hai cột (`--two`): trang chủ, Thông báo, lịch sử sửa bài, trang không có cột phụ. Quản trị (`--admin`, `--admin3` khi có cột phụ): vùng nội dung bên trong AdminShell của khu kiểm duyệt và quản trị. Chat (`--chat`): Tin nhắn. Giữa trang (`--center`): đăng ký, đăng nhập, mật khẩu, kích hoạt lại, bảo trì, đồng ý chính sách.
- **Không dùng khi:** chia cột bên trong một khối (dùng `is-grid2`, `is-grid3`).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `variant` | `'three' \| 'two' \| 'admin' \| 'admin3' \| 'chat' \| 'center'` | `'three'` | `three` = ba cột (không có class biến thể); `admin*` chỉ nằm trong AdminShell |
  | `aside` | `ReactNode?` | — | Cột phụ `aside-w` 260px |
  | `children` | `ReactNode` | — | Vùng `main` |

- **Biến thể và trạng thái:**
  - Ba cột: `nav-w` 200 · nội dung co giãn · `aside-w` 260; cách nhau `space-10`; đệm `space-8` hai bên, `space-16` dưới.
  - Hai cột: nội dung tối đa `content-max` 820.
  - Quản trị: nằm trong AdminShell (DD-UI-42), không có cột điều hướng riêng; nội dung trải hết bề ngang, SectionCard bỏ giới hạn 820px; `--admin3` thêm cột phụ `aside-w` 260.
  - Chat: điều hướng · hộp thư `inbox-w` 340 · cuộc trò chuyện.
  - Giữa trang: một khối ở giữa, đệm trên `space-16`; khối rộng `dialog-w` hoặc `content-max`.
  - Không vỡ ở 1280px (DD-UI-02): cột nội dung co lại, hai cột bên giữ bề rộng.
- **Dữ liệu cần có:**
  - Biến thể; nội dung từng cột.
- **A11y:**
  - Cột nội dung là `<main>`, cột phụ là `<aside>`, điều hướng là `<nav>` có nhãn; thứ tự trong mã giống thứ tự đọc: điều hướng, nội dung, cột phụ.
- **Class CSS** (`components.css`): `is-layout`, `is-layout--two`, `is-layout--admin`, `is-layout--admin3`, `is-layout--chat`, `is-layout--center`, `is-layout__main`, `is-layout__aside`
- **Token:** `nav-w`, `nav-w-wide`, `aside-w`, `inbox-w`, `content-max`, `topbar-h`, `space-8`, `space-10`, `space-16`
- **Dùng ở:** 58/75 màn hình (gần như mọi trang)
- **Preview:** design system › `components/PageLayout/preview.html` · **Figma:** [SCR-SHARED-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=96-2)

#### AdminShell

- **Mục đích:** Khung riêng của khu kiểm duyệt và quản trị (DD-UI-42): cột menu nền sẫm cao hết trang có logo "iShare", thanh trên riêng chỉ có vị trí trang và vài nút, nội dung trải hết bề ngang cho bảng. Nhìn vào là biết đang ở khu quản trị, khác trang học sinh.
- **Dùng khi:** mọi màn hình của Mod và Admin trong khu kiểm duyệt và quản trị: các hàng chờ, chi tiết vụ báo cáo, chi tiết khiếu nại, Quản lý Tag, Nhật ký kiểm duyệt, Người dùng, Vai trò, Chủ đề, Cấu hình hệ thống, Banner, Nhật ký Admin, Thống kê.
- **Không dùng khi:** màn hình phía người dùng, kể cả khi người xem là Mod hay Admin (dùng AppHeader + NavBar): trang bài viết với hộp thoại đổi Chủ đề, Tag; Mức cảnh cáo của tôi; Gửi khiếu nại; Khiếu nại của tôi.
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `role` | `'mod' \| 'admin'` | — | Mod chỉ thấy nhóm Kiểm duyệt |
  | `current` | `string` | — | Mục menu đang xem |
  | `crumb` | `{group, page}` | — | Vị trí trang |
  | `user` | `UserSummary` | — |  |
  | `banner` | `ReactNode?` | — | Banner toàn trang dưới thanh |

- **Biến thể và trạng thái:**
  - **Admin:** menu có hai nhóm Kiểm duyệt và Quản trị.
  - **Mod:** menu chỉ có nhóm Kiểm duyệt.
  - Cột menu: rộng `nav-w-wide` 240px, nền `console-bg`, viền phải `console-line`; ô logo cao `topbar-h`, chữ "i" `console-ink`, "Share" `console-accent`; menu là NavBar `--console`.
  - Thanh trên: cao `topbar-h`, nền `surface`; trái là vị trí trang (nhóm › trang đang xem, chữ 14px); phải là "Về iShare" (Button ghost, là liên kết), chuông Thông báo, avatar mở menu tài khoản. Không có ô tìm kiếm, Viết bài, Tin nhắn.
  - Vùng nội dung: PageLayout `--admin` (một cột) hoặc `--admin3` (thêm cột phụ 260px); banner toàn trang (nếu có) nằm ngay dưới thanh.
  - Cột menu kéo dài hết chiều cao trang; mật độ gọn của khu quản trị giữ theo DD-UI-30.
- **Dữ liệu cần có:**
  - Vai trò người xem (Mod hoặc Admin), mục đang xem và nhóm của nó, tên và chữ cái đầu người xem.
- **A11y:**
  - Cột menu là `<nav>` nhãn "Khu kiểm duyệt", mục đang xem `aria-current="page"`; vị trí trang là `<nav>` nhãn "Vị trí trang" chứa `<ol>`; thanh là `<header>`, nội dung là `<main>`.
  - Vòng focus trên cột menu dùng `console-accent` để vẫn thấy trên nền sẫm (≥ 3:1).
- **Class CSS** (`components.css`): `is-console`, `is-console__side`, `is-console__brand`, `is-console__body`, `is-console__bar`, `is-console__where`, `is-console__crumb`, `is-console__end`, `is-nav--console`
- **Token:** `console-bg`, `console-hover`, `console-active`, `console-ink`, `console-ink-muted`, `console-accent`, `console-line`, `nav-w-wide`, `topbar-h`, `surface`, `line`
- **Dùng ở:** SCR-SHARED-06, SCR-M03-05, SCR-M05-02, SCR-M05-04, SCR-M08-02, SCR-M08-03, SCR-M08-06, SCR-M09-03, SCR-M09-04, SCR-M10-01, SCR-M10-02, SCR-M10-04, SCR-M10-05, SCR-M10-06, SCR-M15-01, SCR-M15-02, SCR-M15-03
- **Preview:** design system › `components/AdminShell/preview.html` · **Figma:** [SCR-SHARED-06--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=516-2)

#### PageHeader

- **Mục đích:** Dòng tiêu đề: tiêu đề (kèm dòng phụ) bên trái, nút hoặc bộ chọn bên phải; xuống dòng khi hẹp.
- **Dùng khi:** đầu mỗi trang (tiêu đề `is-h1` + dòng phụ + nút chính); đầu một khối hay khu vực trong trang (tiêu đề `is-h2` hoặc `is-label` + bộ sắp xếp, nhãn trạng thái).
- **Không dùng khi:** tiêu đề trong bài viết (dùng kiểu chữ `post-h1/2/3` của PostBody).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `title` | `string` | — | `h1` |
  | `subtitle` | `string?` | — |  |
  | `actions` | `ReactNode?` | — | Nút hoặc bộ chọn bên phải |

- **Biến thể và trạng thái:**
  - Đầu trang: `is-h1` (26/700), dòng phụ `ink-muted`, nút căn đáy dòng.
  - Đầu khu vực: `is-h2` (22/700) — ví dụ "5 bình luận" + SegmentedControl sắp xếp.
  - Đầu khối nhỏ: `is-label` (15/600) — ví dụ "Mức hiện tại" + StatusLabel.
- **Dữ liệu cần có:**
  - Tiêu đề, dòng phụ (tùy chọn), hành động (tùy chọn).
- **A11y:**
  - Mỗi trang đúng một `h1`; tiêu đề khu vực dùng `h2`, không nhảy cấp.
- **Class CSS** (`components.css`): `is-pagehead`, `is-h1`, `is-h2`, `is-label`
- **Token:** `ink-muted`, `space-4`
- **Dùng ở:** 39/75 màn hình (gần như mọi trang)
- **Preview:** design system › `components/PageHeader/preview.html` · **Figma:** [SCR-M01-07--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=744-2)

#### SectionCard

- **Mục đích:** Khối nền `surface`, viền `line` mảnh, bo `radius-sm`: gom một phần nội dung thành một tờ giấy trên nền trang (hướng "Sổ tay").
- **Dùng khi:** khu bình luận, form trong trang (sửa hồ sơ, cài đặt), khối thông tin trong khu quản trị; bản gọn (`--compact`) cho các khối ở cột phụ: "Phân loại", "Gửi bài", "Thông tin bài", bộ lọc.
- **Không dùng khi:** thẻ bài trong danh sách (dùng PostCard), hộp thoại (dùng Dialog), thông báo (dùng InlineAlert).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `title` | `string?` | — | `h2` theo ngữ cảnh |
  | `compact` | `boolean` | `false` | Padding nhỏ ở cột phụ |
  | `children` | `ReactNode` | — |  |

- **Biến thể và trạng thái:**
  - Thường: đệm `space-8`, rộng tối đa `content-max`.
  - Gọn (`--compact`): đệm `space-5`, rộng theo cột chứa.
  - Tiêu đề khối: PageHeader với `is-h2` (khối thường) hoặc `is-label` (khối gọn).
- **Dữ liệu cần có:**
  - Tiêu đề (tùy chọn) và nội dung.
- **A11y:**
  - Khối có tiêu đề nên là `<section aria-labelledby>`; khối chỉ để trang trí thì dùng `<div>`.
- **Class CSS** (`components.css`): `is-card`, `is-card--compact`
- **Token:** `surface`, `line`, `radius-sm`, `space-8`, `space-5`, `content-max`
- **Dùng ở:** 41/75 màn hình (gần như mọi trang)
- **Preview:** design system › `components/SectionCard/preview.html` · **Figma:** [SCR-SHARED-03--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=436-2)

#### TableOfContents

- **Mục đích:** Mục lục "Trong bài này" ở cột phụ: các tiêu đề của bài, mục đang đọc tô màu chủ đạo.
- **Dùng khi:** chi tiết bài có từ hai tiêu đề trở lên; trang Privacy Policy/ToS.
- **Không dùng khi:** điều hướng giữa các trang (dùng NavBar, Tabs).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `items` | `{id, label}[]` | — | Tiêu đề trong bài |
  | `current` | `string?` | — | `aria-current` |

- **Biến thể và trạng thái:**
  - Mục thường `ink-muted`; rê chuột `ink`; mục đang đọc `primary`, đậm 600 (`aria-current="true"`).
  - Vạch trái `line-strong` 1px nối các mục.
- **Dữ liệu cần có:**
  - Danh sách tiêu đề và mục đang đọc.
- **A11y:**
  - Đặt trong `<nav aria-label="Trong bài này">`; mỗi mục là liên kết tới tiêu đề trong bài.
- **Class CSS** (`components.css`): `is-toc`
- **Token:** `ink-muted`, `ink`, `primary`, `line-strong`
- **Dùng ở:** SCR-M01-09, SCR-M03-02
- **Preview:** design system › `components/TableOfContents/preview.html` · **Figma:** [SCR-M01-09--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=472-2)

#### DescriptionList

- **Mục đích:** Danh sách cặp nhãn – giá trị, nhãn `ink-muted` bên trái, giá trị bên phải.
- **Dùng khi:** thông tin bài, thông tin nhóm, chi tiết vụ báo cáo và khiếu nại, hồ sơ trong khu quản trị, cài đặt tài khoản.
- **Không dùng khi:** dữ liệu nhiều cột so sánh được (dùng DataTable).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `items` | `{term, detail}[]` | — | `dl`/`dt`/`dd` |
  | `stack` | `boolean` | `false` | Nhãn trên giá trị cho cột phụ hẹp (QA-F-09) |

- **Biến thể và trạng thái:**
  - Cỡ chữ 14px; cột nhãn vừa nội dung, cột giá trị co giãn và xuống dòng.
  - Biến thể `is-dl--stack` cho cột phụ hẹp (thông tin bài, cột Tác giả của vụ báo cáo): nhãn nằm trên giá trị, để ngày giờ và tên không bị tách dòng (QA-F-09).
- **Dữ liệu cần có:**
  - Các cặp nhãn – giá trị.
- **A11y:**
  - Dùng `<dl>`, `<dt>`, `<dd>` để trình đọc màn hình đọc đúng cặp.
- **Class CSS** (`components.css`): `is-dl`, `is-dl--stack`
- **Token:** `ink-muted`, `space-2`, `space-3`
- **Dùng ở:** SCR-SHARED-05, SCR-M01-07, SCR-M03-02, SCR-M04-02, SCR-M08-03, SCR-M09-01, SCR-M09-02, SCR-M09-04, SCR-M10-02, SCR-M10-03, SCR-M11-03, SCR-M11-05
- **Preview:** design system › `components/DescriptionList/preview.html` · **Figma:** [SCR-SHARED-05--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=509-2)

#### AppHeader

- **Mục đích:** Thanh trên cùng cố định của mọi trang (DD-UI-20): chữ "iShare", ô tìm kiếm ở giữa khoảng còn lại, nhóm nút bên phải.
- **Dùng khi:** mọi trang của người dùng và khách.
- **Không dùng khi:** khu kiểm duyệt và quản trị: dùng thanh riêng của AdminShell (DD-UI-42).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `user` | `UserSummary \| null` | — | null = Guest: nút Đăng nhập, Đăng ký |
  | `unreadNotifications` | `number` | `0` |  |
  | `unreadMessages` | `number` | `0` |  |
  | `role` | `'user' \| 'mod' \| 'admin'` | `'user'` | Menu tài khoản có lối vào khu quản trị |

- **Biến thể và trạng thái:**
  - Đã đăng nhập: Viết bài, chuông Thông báo (Counter), Tin nhắn (Counter), avatar mở menu tài khoản (Hồ sơ, Cài đặt tài khoản, Khiếu nại của tôi, Khu kiểm duyệt cho Mod/Admin, Đăng xuất).
  - Guest: Đăng nhập, Đăng ký thay cho chuông, tin nhắn, avatar.
  - Logo: "i" màu `ink`, "Share" màu `primary`, chữ Be Vietnam Pro 700 — không có tệp logo (DD-UI-03).
- **Dữ liệu cần có:**
  - Người xem (tên, chữ cái đầu), số thông báo chưa đọc, số cuộc trò chuyện chưa đọc, vai trò.
- **A11y:**
  - `<header>` landmark; ô tìm kiếm `role="search"`; liên kết bỏ qua tới nội dung chính đứng trước thanh.
- **Class CSS** (`components.css`): `is-topbar`, `is-logo`, `is-topbar__mid`, `is-topbar__end`, `is-avbtn`
- **Token:** `topbar-h`, `surface`, `line`, `primary`
- **Dùng ở:** 41/75 màn hình (gần như mọi trang)
- **Preview:** design system › `components/AppHeader/preview.html` · **Figma:** [SCR-SHARED-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=96-2)

#### NavBar

- **Mục đích:** Cột điều hướng trái 200px (DD-UI-21); khu kiểm duyệt và quản trị dùng biến thể `--console` nền sẫm trong AdminShell (DD-UI-42).
- **Dùng khi:** mọi trang desktop.
- **Không dùng khi:** điều hướng trong một trang (dùng Tabs).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `items` | `{href, label, icon}[]` | — |  |
  | `current` | `string` | — | `aria-current="page"` |
  | `variant` | `'default' \| 'console'` | `'default'` | `console` trong AdminShell |
  | `footer` | `ReactNode` | — | "Chính sách và Điều khoản" (DD-UI-43) |

- **Biến thể và trạng thái:**
  - Người dùng: Trang chủ, Chủ đề, Nhóm, Bảng xếp hạng; dòng chân "Chính sách và Điều khoản" (liên kết tới trang Privacy Policy/ToS); rộng `nav-w` 200px.
  - Mục đang xem: nền `primary-soft`, chữ và icon `primary`; rê chuột `surface-hover`.
  - Khu kiểm duyệt và quản trị (`--console`, nằm trong cột `is-console__side` rộng `nav-w-wide` 240px của AdminShell): nhóm Kiểm duyệt (Hàng chờ báo cáo, Hàng chờ duyệt bài, Hàng chờ khiếu nại, Quản lý Tag, Nhật ký kiểm duyệt), nhóm Quản trị chỉ Admin thấy (Người dùng, Chủ đề, Cấu hình hệ thống, Banner, Nhật ký Admin, ba trang Thống kê); mỗi mục có icon. Chữ `console-ink`, icon và tên nhóm `console-ink-muted`; rê chuột `console-hover`; mục đang xem nền `console-active`, chữ và icon `console-accent`. Lối "Về iShare" nằm trên thanh của AdminShell.
- **Dữ liệu cần có:**
  - Danh sách mục theo vai trò, mục hiện tại.
- **A11y:**
  - `<nav>` có nhãn; mục hiện tại `aria-current="page"`.
- **Class CSS** (`components.css`): `is-nav`, `is-nav--console`, `is-nav__item`, `is-nav__group`, `is-nav__foot`
- **Token:** `nav-w`, `nav-w-wide`, `primary-soft`, `primary`, `surface-hover`, `console-*`
- **Dùng ở:** 48/75 màn hình (gần như mọi trang)
- **Preview:** design system › `components/NavBar/preview.html` · **Figma:** [SCR-SHARED-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=96-2)

#### Tabs

- **Mục đích:** Chuyển giữa các phần cùng cấp trong một trang; tab đang chọn gạch chân `primary`.
- **Dùng khi:** bốn tab trang chủ (Thịnh hành / Đang theo dõi / Nhóm / Mới nhất) với mục con của Thịnh hành (Bài viết / Chủ đề / Tag), tab hồ sơ, Người theo dõi / Đang theo dõi, chu kỳ Bảng xếp hạng.
- **Không dùng khi:** lọc dữ liệu (dùng SegmentedControl, FilterBar).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `tabs` | `{id, label, count?}[]` | — | `tablist`, phím mũi tên; `count` hiện Counter trầm |
  | `value` | `string` | — |  |
  | `variant` | `'tabs' \| 'sub'` | `'tabs'` | `sub` = mục con dạng chip (`is-subtabs`) |
  | `asLinks` | `boolean` | `false` | Tab đổi URL khi FR có (`/?tab=following`) |

- **Biến thể và trạng thái:**
  - Tab chính: chữ `label`, gạch chân 2px khi chọn; có thể kèm Counter trầm.
  - Mục con: chip nhỏ (`is-subtab`), chọn thì nền `primary-soft`.
  - Trạng thái tab đặt vào URL khi FR có (`/?tab=following`).
- **Dữ liệu cần có:**
  - Nhãn tab, tab mặc định.
- **A11y:**
  - `role="tablist"`, `role="tab"` với `aria-selected`, `aria-controls`; phím mũi tên chuyển tab.
- **Class CSS** (`components.css`): `is-tabs`, `is-tab`, `is-subtabs`, `is-subtab`
- **Token:** `primary`, `primary-soft`, `line`, `ink-muted`
- **Dùng ở:** SCR-M01-07, SCR-M02-01, SCR-M02-02, SCR-M08-05, SCR-M10-03, SCR-M11-03, SCR-M11-05, SCR-M11-06, SCR-M11-10, SCR-M11-11, SCR-M12-01, SCR-M14-01
- **Preview:** design system › `components/Tabs/preview.html` · **Figma:** [SCR-M01-07--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=744-2)

#### Dialog

- **Mục đích:** Hộp thoại giữa màn hình, nền mờ phía sau, cho thao tác ngắn cần tập trung (DD-UI-24).
- **Dùng khi:** Báo cáo, lý do biện pháp, tạo nhóm chat, thêm thành viên, gửi yêu cầu tham gia, mời vào nhóm, rời nhóm, đổi Chủ đề/Tag, gộp Chủ đề, người theo dõi, từ chức, tài khoản bị khóa khi đang dùng.
- **Không dùng khi:** nội dung xem kèm trang (dùng Drawer) hoặc xác nhận mà SC không có — không tự thêm bước hỏi lại (SC-M03-014, SC-M04).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `open` | `boolean` | — |  |
  | `title` | `string` | — | Tiêu đề `h3`, `aria-labelledby` |
  | `onClose` | `() => void` | — | Esc, nút Đóng |
  | `footer` | `ReactNode` | — | Nút chính bên phải; nguy hiểm thì `danger` |
  | `width` | `'default' \| 'wide'` | `'default'` | `dialog-w` 520px; `wide` = `content-max` cho dialog có danh sách |

- **Biến thể và trạng thái:**
  - Thường (520px) và rộng (`content-max`) cho dialog có danh sách; tiêu đề `h3`, nút đóng, thân, chân với nút chính bên phải.
  - Nguy hiểm: nút chính `--danger` (Rời nhóm khi là thành viên cuối, Ban).
- **Dữ liệu cần có:**
  - Tiêu đề nêu việc, nội dung form, nhãn nút là động từ.
- **A11y:**
  - `role="dialog"` `aria-modal="true"` `aria-labelledby`; giữ focus trong hộp, Esc đóng, trả focus về nút đã mở (QF-06).
- **Class CSS** (`components.css`): `is-scrim`, `is-dialog`, `is-dialog__head`, `is-dialog__title`, `is-dialog__body`, `is-dialog__foot`
- **Token:** `scrim`, `surface-raised`, `shadow-2`, `dialog-w`
- **Dùng ở:** SCR-M02-02, SCR-M05-03, SCR-M05-05, SCR-M08-01, SCR-M08-04, SCR-M10-03, SCR-M11-04, SCR-M11-07, SCR-M11-09, SCR-M16-03, SCR-M16-06
- **Preview:** design system › `components/Dialog/preview.html` · **Figma:** [SCR-M02-02--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=214-2)

#### Drawer

- **Mục đích:** Ngăn trượt bên phải 420px cho nội dung xem kèm, không rời trang (DD-UI-24).
- **Dùng khi:** Tóm tắt bài (SCR-M13-01), thông tin nhóm chat (SCR-M16-04), vai trò của một người dùng (SCR-M10-02), chi tiết dòng nhật ký.
- **Không dùng khi:** thao tác ngắn cần quyết định (dùng Dialog).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `open` | `boolean` | — |  |
  | `title` | `string` | — |  |
  | `onClose` | `() => void` | — |  |
  | `children` | `ReactNode` | — | `drawer-w` 420px |

- **Biến thể và trạng thái:**
  - Đầu ngăn: tiêu đề + nút đóng; thân cuộn riêng.
  - Tóm tắt: đang tải (Skeleton), lỗi (ErrorState nhỏ + Thử lại), ghi chú "Tóm tắt do AI tạo, có thể chưa chính xác".
- **Dữ liệu cần có:**
  - Tiêu đề, nội dung.
- **A11y:**
  - `role="dialog"` `aria-labelledby`; Esc đóng; trả focus về nút đã mở.
- **Class CSS** (`components.css`): `is-drawerwrap`, `is-drawer`
- **Token:** `drawer-w`, `surface-raised`, `shadow-2`, `scrim`
- **Dùng ở:** SCR-M13-01, SCR-M16-04
- **Preview:** design system › `components/Drawer/preview.html` · **Figma:** [SCR-M13-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=673-2)

#### Menu

- **Mục đích:** Danh sách thao tác thả xuống từ một nút ("…", avatar).
- **Dùng khi:** menu tài khoản, menu "…" của bài (Sửa, Tự ẩn, Khóa bình luận, Quản lý bình chọn, Tắt thông báo bài, Xóa), của bình luận, của thành viên nhóm.
- **Không dùng khi:** chọn giá trị cho form (dùng Select) hoặc nội dung nhiều thông tin (dùng Popover).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `trigger` | `ReactNode` | — | IconButton "…" hoặc avatar |
  | `items` | `{label, icon?, onSelect, danger?, divider?}[]` | — | `menu`/`menuitem`, phím mũi tên |

- **Biến thể và trạng thái:**
  - Mục thường, mục có icon, mục đang bật (`aria-checked`), mục nguy hiểm `danger` (Xóa, Ban — đặt cuối, sau vạch ngăn), mục tắt.
  - Menu tài khoản có đầu menu: tên và @username.
- **Dữ liệu cần có:**
  - Danh sách mục theo quyền của người xem; mục không có quyền thì không hiện.
- **A11y:**
  - `role="menu"`, `role="menuitem"`; phím mũi tên di chuyển, Esc đóng, trả focus về nút mở.
- **Class CSS** (`components.css`): `is-menu`, `is-mi`, `is-mi--danger`, `is-menu__sep`, `is-menu__head`
- **Token:** `surface-raised`, `shadow-1`, `surface-hover`, `danger`
- **Dùng ở:** SCR-SHARED-01, SCR-M03-02, SCR-M07-01
- **Preview:** design system › `components/Menu/preview.html` · **Figma:** [SCR-SHARED-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=96-2)

#### Popover

- **Mục đích:** Ngăn nổi gắn với một nút, chứa nội dung giàu hơn menu: ngăn thông báo, gợi ý tìm kiếm.
- **Dùng khi:** chuông → ngăn 10 thông báo gần nhất, cuối ngăn "Xem tất cả" tới `/notifications` (DD-UI-23).
- **Không dùng khi:** danh sách thao tác (dùng Menu).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `trigger` | `ReactNode` | — |  |
  | `title` | `string?` | — |  |
  | `children` | `ReactNode` | — | Ngăn thông báo (SCR-M07-01), lời mời đăng nhập của Guest |
  | `open / onOpenChange` | `boolean / (open: boolean) => void` | — |  |

- **Biến thể và trạng thái:**
  - Đầu ngăn có tiêu đề và thao tác (Đánh dấu tất cả đã đọc); thân là danh sách; chân có liên kết.
  - Trống: "Bạn chưa có thông báo nào"; đang tải: Skeleton dòng; phiên hết hạn: lời mời đăng nhập lại.
- **Dữ liệu cần có:**
  - Nội dung, nút gắn.
- **A11y:**
  - Nút mở có `aria-expanded`, `aria-controls`; Esc đóng; focus vào ngăn khi mở bằng bàn phím.
- **Class CSS** (`components.css`): `is-pop`, `is-pop__head`, `is-pop__title`, `is-pop__foot`
- **Token:** `surface-raised`, `shadow-1`, `line`
- **Dùng ở:** SCR-M05-01, SCR-M06-01
- **Preview:** design system › `components/Popover/preview.html` · **Figma:** [SCR-M05-01--guest--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=117-2)

#### Tooltip

- **Mục đích:** Chú thích ngắn khi rê chuột hoặc focus vào một nút, nền `ink`, chữ `surface`.
- **Dùng khi:** nhắc tên nút chỉ có icon trên thanh soạn thảo ("In đậm (Ctrl+B)"), giải thích vì sao nút bị tắt.
- **Không dùng khi:** thông tin cần để làm việc — phải hiện sẵn trên trang.
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `content` | `string` | — | Chữ ngắn |
  | `children` | `ReactElement` | — | Hiện khi rê chuột và khi focus |

- **Biến thể và trạng thái:**
  - Hiện sau 300ms rê chuột, ngay khi focus; ẩn khi Esc.
- **Dữ liệu cần có:**
  - Một câu ngắn.
- **A11y:**
  - `role="tooltip"` nối bằng `aria-describedby`; không đặt nội dung tương tác trong tooltip.
- **Class CSS** (`components.css`): `is-tip`
- **Token:** `ink`, `surface`, `shadow-1`, `radius-sm`
- **Dùng ở:** chưa có artboard nào dùng (chỉ có trong design system)
- **Preview:** design system › `components/Tooltip/preview.html` · **Figma:** —

#### Pagination

- **Mục đích:** Tải thêm cho danh sách của học sinh (cuộn tải 20 mục) và phân trang số cho bảng khu quản trị.
- **Dùng khi:** trang chủ, kết quả tìm kiếm (tối đa 120), thông báo, bảng xếp hạng: Tải thêm; bảng quản trị: trang số.
- **Không dùng khi:** danh sách ngắn hiện đủ một lần.
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `mode` | `'load-more' \| 'pages'` | — | Học sinh: tải thêm 20 mục; khu quản trị: số trang |
  | `page / total` | `number` | — |  |
  | `onLoadMore / onPage` | `…` | — |  |

- **Biến thể và trạng thái:**
  - Tải thêm: nút phụ, đang tải (`aria-busy`), hết ("Đã hiện tất cả kết quả").
  - Trang số: trang hiện tại `primary-soft`, nút trước/sau tắt ở đầu/cuối.
- **Dữ liệu cần có:**
  - Còn mục để tải không, trang hiện tại, tổng số trang.
- **A11y:**
  - Phân trang là `<nav aria-label="Phân trang">`; trang hiện tại `aria-current="page"`; khi tải thêm, đưa focus vào mục đầu tiên mới.
- **Class CSS** (`components.css`): `is-more`, `is-pager`, `is-page`
- **Token:** `primary-soft`, `primary`, `control-h-sm`
- **Dùng ở:** SCR-M08-02, SCR-M08-06, SCR-M10-01
- **Preview:** design system › `components/Pagination/preview.html` · **Figma:** [SCR-M08-02--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=511-2)

#### StepIndicator

- **Mục đích:** Chỉ báo các bước của luồng nhiều bước: Đăng ký gồm Tài khoản → Xác minh email → Thiết lập hồ sơ.
- **Dùng khi:** SCR-M01-01, -02, -03.
- **Không dùng khi:** luồng một bước.
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `steps` | `string[]` | — | Tài khoản, Xác minh email, Thiết lập hồ sơ |
  | `current` | `number` | — | `aria-current="step"` |

- **Biến thể và trạng thái:**
  - Bước đã xong và bước hiện tại: thanh `primary`; bước sau: thanh `line`; nhãn bước hiện tại đậm `ink`.
- **Dữ liệu cần có:**
  - Danh sách bước, bước hiện tại.
- **A11y:**
  - `<ol>`; bước hiện tại `aria-current="step"`; chữ "Bước 2 · …" nói rõ vị trí, không chỉ dựa vào màu.
- **Class CSS** (`components.css`): `is-steps`, `is-step`, `is-step--done`, `is-step--current`
- **Token:** `primary`, `line`, `radius-full`
- **Dùng ở:** SCR-M01-01, SCR-M01-02, SCR-M01-03
- **Preview:** design system › `components/StepIndicator/preview.html` · **Figma:** [SCR-M01-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=732-2)

### 4.9 Phản hồi

#### Toast

- **Mục đích:** Thông báo ngắn góc dưới trái sau một thao tác của chính người dùng, tự ẩn sau vài giây.
- **Dùng khi:** Đã lưu bài, Đã sao chép link mời, Đã gửi báo cáo, lỗi mạng khi gửi.
- **Không dùng khi:** lỗi của ô nhập (để cạnh ô), thông báo phải đọc kỹ hoặc cần quyết định (dùng InlineAlert, Dialog).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `tone` | `'success' \| 'info' \| 'warning' \| 'danger'` | `'success'` | Chữ luôn `ink`, icon và màu theo tone |
  | `message` | `string` | — |  |
  | `action` | `{label, onClick}?` | — | Một nút, ví dụ Thử lại |
  | `duration` | `number?` | — | Tự ẩn sau vài giây (số cụ thể chốt ở phase Coding); lỗi không tự ẩn |

- **Biến thể và trạng thái:**
  - Thành công, thông tin, cảnh báo, lỗi — icon và màu theo tone, chữ luôn `ink`.
  - Có thể kèm một nút ("Thử lại"); lỗi không tự ẩn.
- **Dữ liệu cần có:**
  - Một câu: chuyện gì xảy ra (+ làm gì tiếp nếu lỗi), theo giọng văn PRODUCT.md mục 8.
- **A11y:**
  - `role="status"` (lỗi: `role="alert"`); không cướp focus; nút Đóng có nhãn.
- **Class CSS** (`components.css`): `is-toast`, `is-toast__ic`, `is-tone-*`
- **Token:** `surface-raised`, `shadow-1`, `success`, `info`, `warning`, `danger`
- **Dùng ở:** SCR-M02-03, SCR-M03-01, SCR-M04-01, SCR-M10-04, SCR-M16-02
- **Preview:** design system › `components/Toast/preview.html` · **Figma:** [SCR-M02-03--error--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=222-2)

#### InlineAlert

- **Mục đích:** Khối thông báo nằm trong trang, ngay chỗ liên quan; không tự ẩn.
- **Dùng khi:** bài đang chờ duyệt hoặc bị từ chối (kèm lý do), tài khoản ở mức cảnh cáo MEDIUM/HEAVY khi soạn bài, Đăng ký đang tạm dừng, lỗi gửi form.
- **Không dùng khi:** phản hồi nhanh sau thao tác (dùng Toast) hoặc thông báo toàn trang của Admin (dùng Banner).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `tone` | `'info' \| 'success' \| 'warning' \| 'danger'` | `'info'` | `danger` dùng `role="alert"` |
  | `title` | `string` | — |  |
  | `children` | `ReactNode` | — | Mô tả |
  | `actions` | `ReactNode?` | — | Ví dụ "Khiếu nại cảnh cáo này" (DD-UI-44) |

- **Biến thể và trạng thái:**
  - Bốn tone: thông tin, thành công, cảnh báo, lỗi; nền `*-soft`, chữ `ink`, icon màu tone.
  - Có thể kèm nút: Khiếu nại, Sửa bài, Đăng nhập.
- **Dữ liệu cần có:**
  - Tiêu đề ngắn, câu giải thích nêu lý do và thời hạn nếu có, hành động tiếp theo.
- **A11y:**
  - `role="alert"` cho lỗi, `role="status"` cho phần còn lại; nút có nhãn rõ.
- **Class CSS** (`components.css`): `is-alert`, `is-alert--success|warning|danger`, `is-alert__title`, `is-alert__acts`
- **Token:** `info-soft`, `success-soft`, `warning-soft`, `danger-soft`, `ink`
- **Dùng ở:** SCR-M01-01, SCR-M01-02, SCR-M01-04, SCR-M01-05, SCR-M01-06, SCR-M01-07, SCR-M01-08, SCR-M02-01, SCR-M03-01, SCR-M03-02, SCR-M03-05, SCR-M04-01, SCR-M07-02, SCR-M08-03, SCR-M08-05, SCR-M10-02, SCR-M10-03, SCR-M11-03, SCR-M11-08, SCR-M13-01, SCR-M16-05, SCR-M16-06
- **Preview:** design system › `components/InlineAlert/preview.html` · **Figma:** [SCR-M08-05--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=554-2)

#### Banner

- **Mục đích:** Thông báo toàn trang của Admin: một dải dưới thanh trên cùng, văn bản thuần ≤200 ký tự, người xem đóng được (FR-M10).
- **Dùng khi:** SCR-SHARED-02 trên mọi trang, cho mọi người kể cả Guest; nội dung mới thì hiện lại.
- **Không dùng khi:** thông báo riêng cho một người (dùng InlineAlert, thông báo).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `message` | `string` | — | Văn bản thuần ≤200 ký tự, dài thì xuống dòng |
  | `tone` | `'info' \| 'warning'` | `'info'` | `warning` cho thông báo bảo trì sắp tới |
  | `onDismiss` | `() => void` | — | Người xem đóng được |

- **Biến thể và trạng thái:**
  - Tone thông tin (mặc định); tone cảnh báo cho thông báo bảo trì sắp tới.
  - Văn bản dài xuống dòng, không cắt.
- **Dữ liệu cần có:**
  - Nội dung banner Admin nhập.
- **A11y:**
  - `role="region"` có nhãn "Thông báo"; nút Đóng có nhãn.
- **Class CSS** (`components.css`): `is-banner`, `is-banner--warning`
- **Token:** `info-soft`, `warning-soft`, `ink`, `line`
- **Dùng ở:** SCR-SHARED-02, SCR-M10-05
- **Preview:** design system › `components/Banner/preview.html` · **Figma:** [SCR-SHARED-02--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=101-2)

#### EmptyState

- **Mục đích:** Trạng thái trống: chưa có gì để hiện, nói vì sao và gợi bước tiếp theo.
- **Dùng khi:** tab Đang theo dõi chưa theo dõi ai (nút sang tìm kiếm), tab Nhóm chưa vào nhóm nào (nút Khám phá Group), không có kết quả tìm, hàng chờ trống, chưa có thông báo.
- **Không dùng khi:** lỗi tải dữ liệu (dùng ErrorState).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `icon` | `IconName` | — | Trung tính |
  | `title` | `string` | — | Heading theo ngữ cảnh |
  | `description` | `string` | — |  |
  | `actions` | `ReactNode?` | — | Tối đa hai nút chữ |
  | `headingLevel` | `2 \| 3` | `2` |  |

- **Biến thể và trạng thái:**
  - Icon trung tính, tiêu đề, một câu, tối đa hai nút. Không minh họa, không mascot (PRODUCT.md mục 6).
  - Nút dạng chữ, không nền, không viền: việc chính dùng Button chữ chính (`--text-primary`), việc phụ dùng chữ phụ (`--text`).
- **Dữ liệu cần có:**
  - Câu theo SC; nút dẫn tới việc làm được ngay.
- **A11y:**
  - Tiêu đề là heading theo ngữ cảnh: `h2` khi trạng thái trống nằm ngay dưới `h1`, `h3` trong một mục có `h2` (QF-17).
- **Class CSS** (`components.css`): `is-empty`, `is-empty__ic`, `is-empty__title`, `is-empty__text`, `is-empty__acts`
- **Token:** `ink-muted`
- **Dùng ở:** 30/75 màn hình (gần như mọi trang)
- **Preview:** design system › `components/EmptyState/preview.html` · **Figma:** [SCR-M02-01--empty--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=211-2)

#### Skeleton

- **Mục đích:** Khung xám giữ chỗ trong lúc tải, cùng bố cục với nội dung thật để trang không nhảy.
- **Dùng khi:** trạng thái `loading` của danh sách bài, bình luận, bảng, Tóm tắt, Thống kê.
- **Không dùng khi:** thao tác đang chạy trên một nút (dùng Button `aria-busy`).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `shape` | `'line' \| 'title' \| 'avatar' \| 'block'` | `'line'` |  |
  | `width / height` | `string?` | — |  |

- **Biến thể và trạng thái:**
  - Dòng chữ, tiêu đề, avatar, khối; nhấp nháy nhẹ 1,6 giây, đứng yên khi `prefers-reduced-motion`.
- **Dữ liệu cần có:**
  - Số dòng gần với nội dung thật (3 thẻ bài, 5 dòng bảng).
- **A11y:**
  - Vùng đang tải có `aria-busy="true"` và chữ ẩn "Đang tải…"; các khối `aria-hidden`.
- **Class CSS** (`components.css`): `is-skel`, `is-skel--line`, `is-skel--title`, `is-skel--avatar`
- **Token:** `surface-hover`, `radius-sm`, `avatar-md`
- **Dùng ở:** SCR-M02-01, SCR-M02-02, SCR-M03-02, SCR-M03-03, SCR-M03-05, SCR-M04-01, SCR-M05-01, SCR-M06-02, SCR-M07-01, SCR-M07-02, SCR-M08-02, SCR-M08-06, SCR-M09-02, SCR-M10-01, SCR-M10-06, SCR-M11-01, SCR-M12-01, SCR-M13-01, SCR-M14-01, SCR-M15-01, SCR-M15-02, SCR-M15-03, SCR-M16-01, SCR-M16-02
- **Preview:** design system › `components/Skeleton/preview.html` · **Figma:** [SCR-M02-01--loading--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=212-2)

#### ErrorState

- **Mục đích:** Trang hoặc vùng báo lỗi: không tìm thấy, không có quyền, lỗi tải, hệ thống bận, bảo trì (SCR-SHARED-03, SCR-SHARED-04).
- **Dùng khi:** khi không hiện được nội dung vì lỗi hoặc quyền.
- **Không dùng khi:** danh sách trống bình thường (dùng EmptyState).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `kind` | `'not-found' \| 'forbidden' \| 'error' \| 'busy' \| 'maintenance'` | — | Chữ đúng nguồn |
  | `title / description` | `string` | — |  |
  | `actions` | `ReactNode?` | — | Về trang chủ, Thử lại |
  | `fullPage` | `boolean` | `false` | Trang lỗi chung hay vùng lỗi trong trang |

- **Biến thể và trạng thái:**
  - Không tìm thấy: "Nội dung không tồn tại" / "Người dùng không tồn tại".
  - Không có quyền: nói vì sao (bài trong nhóm Private, chỉ Admin).
  - Lỗi tải, hệ thống bận (cờ tính năng tắt): "Hệ thống đang bận, vui lòng thử lại sau" + Thử lại.
  - Bảo trì: trang riêng, chỉ ADMIN dùng được hệ thống.
  - Căn giữa vùng nội dung như EmptyState; nút dạng chữ: Button chữ chính (việc chính) và chữ phụ (việc phụ), không nền, không viền.
- **Dữ liệu cần có:**
  - Câu đúng như SC; hành động tiếp theo (Thử lại, Về trang chủ, Đăng nhập).
- **A11y:**
  - Tiêu đề `h1` khi là cả trang; trong vùng nhỏ dùng heading đúng cấp.
- **Class CSS** (`components.css`): `is-errorpage`, `is-errorpage__code`, `is-errorpage__title`, `is-errorpage__text`, `is-errorpage__acts`
- **Token:** `h1`, `ink-muted`
- **Dùng ở:** SCR-SHARED-03, SCR-SHARED-04, SCR-M02-01, SCR-M03-02, SCR-M03-03, SCR-M04-02, SCR-M08-03, SCR-M09-01, SCR-M09-04, SCR-M11-03, SCR-M11-10, SCR-M16-05
- **Preview:** design system › `components/ErrorState/preview.html` · **Figma:** [SCR-SHARED-03--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=436-2)

### 4.10 Soạn thảo

#### EditorToolbar

- **Mục đích:** Thanh công cụ của trình soạn: đúng các định dạng FR cho phép, nhóm bằng vạch ngăn.
- **Dùng khi:** trình soạn bài (BR-M03-03) và bản tối giản cho bình luận, trả lời (BR-M04-01: đậm, nghiêng, code trong dòng, LaTeX, liên kết, nhắc tên, trích dẫn).
- **Không dùng khi:** định dạng FR không có — không thêm màu chữ, cỡ chữ, căn lề.
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `editor` | `Editor (Tiptap)` | — | Trạng thái nút theo vùng chọn |
  | `formats` | `Format[]` | — | Đúng các định dạng FR cho phép |
  | `disabled` | `boolean` | `false` |  |

- **Biến thể và trạng thái:**
  - Nút đang áp dụng ở vị trí con trỏ: `aria-pressed`, nền `primary-soft`.
  - Nút tắt khi không dùng được (đã đủ 10 ảnh, đã có bình chọn).
  - Mỗi nút có Tooltip kèm phím tắt.
- **Dữ liệu cần có:**
  - Bộ định dạng theo loại trình soạn; trạng thái của vùng chọn.
- **A11y:**
  - `role="toolbar"` có nhãn; Tab vào thanh rồi dùng phím mũi tên giữa các nút; mọi nút có `aria-label`.
- **Class CSS** (`components.css`): `is-toolbar`, `is-toolbar__sep`, `is-iconbtn--sm`
- **Token:** `line-strong`, `line`, `primary-soft`, `control-h-sm`
- **Dùng ở:** SCR-M03-01, SCR-M03-02, SCR-M04-01
- **Preview:** design system › `components/EditorToolbar/preview.html` · **Figma:** [SCR-M03-01--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=194-2)

#### CommentComposer

- **Mục đích:** Ô soạn bình luận, trả lời và tin nhắn chat.
- **Dùng khi:** cuối khu bình luận, dưới bình luận khi bấm Trả lời (có dòng trích), sửa bình luận; biến thể chat ở chân cuộc trò chuyện.
- **Không dùng khi:** soạn bài (trình soạn đầy đủ với EditorToolbar bài viết).
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|
  | `mode` | `'comment' \| 'reply' \| 'chat' \| 'post'` | `'comment'` | Cao 3 dòng giãn tới 10 (bình luận, trả lời); 1 dòng giãn tới 5 (chat); `post` = vùng soạn bài 280–560px |
  | `value` | `string` | — |  |
  | `maxWords` | `number?` | — | Bình luận ≤1.000 từ; vượt thì bộ đếm `danger`, Gửi tắt |
  | `replyTo` | `{name, excerpt}?` | — | Dòng trích "Trả lời …" và nút Hủy |
  | `blockedReason` | `string?` | — | Guest, bình luận đã khóa, tài khoản bị khóa: thay ô bằng dòng giải thích |
  | `onSubmit` | `(v: string) => void` | — | Chat: Enter gửi, Shift+Enter xuống dòng |

- **Biến thể và trạng thái:**
  - Bình luận: avatar người xem, ô nhập, thanh định dạng tối giản, bộ đếm từ (≤1.000 từ), nút Gửi.
  - Trả lời: dòng trích "Trả lời Trần Minh Đức: …" và nút Hủy.
  - Lỗi: vượt 1.000 từ (bộ đếm `danger`, Gửi tắt).
  - Guest, bình luận đã khóa, tài khoản bị khóa: thay ô bằng một dòng giải thích (+ Đăng nhập cho Guest).
  - Chat: ô nhiều dòng + nút gửi chỉ icon; Enter gửi, Shift+Enter xuống dòng.
  - Ô tự giãn theo nội dung, không có tay kéo: bình luận và trả lời cao 3 dòng, giãn tới 10 dòng rồi cuộn trong ô; chat 1 dòng, giãn tới 5 dòng. Dùng `field-sizing: content`; trình duyệt chưa hỗ trợ thì đặt chiều cao theo `scrollHeight` bằng JS.
  - Vùng soạn bài (`is-composer__doc`, dùng cùng EditorToolbar bài viết): cao 280px, giãn theo nội dung tới 560px rồi cuộn trong ô, thanh công cụ luôn nhìn thấy.
- **Dữ liệu cần có:**
  - Người xem, đối tượng trả lời, giới hạn từ.
- **A11y:**
  - Ô có nhãn (ẩn) "Viết bình luận"; bộ đếm `aria-live`; nút Gửi có chữ (bản chat có `aria-label`).
- **Class CSS** (`components.css`): `is-composer`, `is-composer__box`, `is-composer__text`, `is-composer__doc`, `is-composer__bar`, `is-chatbox`
- **Token:** `line-strong`, `focus`, `danger`, `body-comment`
- **Dùng ở:** SCR-M03-02, SCR-M04-01, SCR-M16-01, SCR-M16-02
- **Preview:** design system › `components/CommentComposer/preview.html` · **Figma:** [SCR-M03-02--default--desktop](https://www.figma.com/design/yEi02SPwmNAfYwKX2gMN8m?node-id=659-2)
