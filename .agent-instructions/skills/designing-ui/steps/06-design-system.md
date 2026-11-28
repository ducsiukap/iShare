# Bước 6 — Design system và tokens

[Vietnamese Doc]

## Mục đích

Khóa mọi lựa chọn thị giác của hướng đã chọn thành **tokens có tên và vai trò**, cùng bộ **component lõi** có đủ trạng
thái. Từ cuối bước này, skill chuyển sang **chế độ thực thi**: mọi màn hình chỉ được dùng những gì có ở đây.

## Đầu vào

- `DESIGN.md` mục 2 (hướng đã chọn, token plan sơ bộ), mục 5, 6; `PRODUCT.md`; `flows.md` và wireframe (để biết
  component nào cần).
- `screen-inventory.md` (trạng thái nào xuất hiện nhiều → component cần biến thể đó).
- Q6-01 … Q6-05.

## Việc làm

### A. Tokens (`tokens/tokens.json`)

Định dạng là định dạng **Design System của Claude Design**: mỗi nhóm (trừ `type`) là `{"tokens":[{"name","value","usage"}]}`,
`color` có thêm `themes`. **Không** dùng dạng map DTCG trong tệp này (bản DTCG do `export_tokens.py` sinh ra). Tên token
`[A-Za-z0-9][A-Za-z0-9_.-]*`, không trùng giữa các nhóm. Mỗi token có `usage` nói dùng ở đâu.

1. **Màu** (`color`):
   - Theme `light` (và `dark` nếu `PRODUCT.md` có dark mode; theme chính đặt đầu).
   - Lớp gốc: các thang màu của hướng (`<tên>-<bậc>`, ví dụ `brand-50 … brand-900`, `neutral-…` pha sắc màu chủ đạo).
   - Lớp ngữ nghĩa (tên theo vai trò, không số): `bg`, `surface`, `surface-raised`, `ink`, `ink-muted`, `line`,
     `line-strong`, `primary`, `on-primary`, `accent`, `focus`, `success`, `warning`, `danger`, `info` và nền nhạt
     tương ứng (`success-soft`…). Trạng thái nghiệp vụ hay gặp (bị gắn cờ, chờ duyệt, bị khóa) dùng lại màu ngữ nghĩa
     + chữ/icon (QF-03), chỉ thêm token riêng khi thật cần.
   - Giá trị: hex, `rgb()`, `hsl()`, `oklch()`, hoặc bí danh `"{tên-token-khác}"`. Không dùng tên màu (`red`),
     `var()`, `color-mix()`.
2. **Chữ** (`type`): `fonts`/`families` (tiêu đề, thân bài, mono) và nhóm `styles`: `display`, `h1`, `h2`, `h3`,
   `body`, `body-sm`, `caption`, `label`, `code` — mỗi kiểu có `fontSize`, `lineHeight` (thân bài ≥ 1.5 × cỡ chữ),
   `fontWeight`. Ít nhất 2 độ đậm. Cỡ thân bài hài hòa với công thức KaTeX.
3. **Khoảng cách** (`spacing`): một thang theo bội số cố định (thường 4px): `space-1` = 4px, `space-2` = 8px…; mật độ
   theo Q6-02 (có thể có hai mức cho màn hình học sinh và màn hình quản trị — ghi rõ trong `usage`).
4. **Bo góc** (`radius`): tối đa 3 mức + `radius-full`, vai trò từng mức trong `usage` (AP-30).
5. **Bóng** (`shadow`): 2–3 mức độ nổi, dùng cho lớp nổi thật (menu, dialog, toast); không dùng bóng để "trang trí"
   card (AP-31).
6. **Chuyển động**: type Design System không có nhóm motion → ghi thời lượng và đường cong (2–3 giá trị) vào
   `DESIGN.md` mục 3, kèm nhánh `prefers-reduced-motion`.

### B. Kiểm tokens

1. `tokens/contrast-pairs.csv` (từ `output/contrast-pairs-template.csv`): mọi cặp chữ/nền và thành phần/nền sẽ xuất hiện
   (ink/bg, ink-muted/surface, on-primary/primary, danger/danger-soft, focus/bg, line-strong/surface…), ngưỡng 4.5 hoặc 3.
2. `python3 $SK/tools/contrast.py --tokens $D/tokens/tokens.json --pairs $D/tokens/contrast-pairs.csv` → mọi cặp đạt ở
   mọi theme. Cặp nào trượt thì chỉnh màu (không hạ ngưỡng).
3. `python3 $SK/tools/export_tokens.py --tokens $D/tokens/tokens.json --out-dir $D/tokens` → `tokens.css` (khối
   `@theme` cho Tailwind v4 + biến cho theme phụ) và `tokens.dtcg.json`. Không sửa tay hai tệp này.
4. Chạy lại `font_test.py` với đúng font, cỡ và line-height đã chốt (thêm `--sizes`, `--line-heights`), đặt vào
   design system (hoặc canvas khám phá, trang "Font") để người dùng xem.

### C. Bộ icon

Đề xuất 2 bộ icon SVG mã nguồn mở (giấy phép cho phép dùng trong sản phẩm), hợp ngôn ngữ hình khối của hướng; trình
mẫu 12 icon hay dùng (upvote, bình luận, trả lời, báo cáo, thông báo, chat, tìm kiếm, nhóm, đính kèm, công thức, khóa,
cài đặt). Người dùng chọn (Q6-04) → `DD-UI-nn`. Một bộ duy nhất, một độ dày nét, một lưới kích thước (AP-42).

### D. Component lõi

Danh sách mặc định (thêm/bớt theo inventory, Q6-05):

| Nhóm | Component |
|---|---|
| Hành động | Button (chính, phụ, nhẹ, nguy hiểm; cỡ), IconButton, Link |
| Nhập liệu | TextField, TextArea, Select, Checkbox, Radio, Switch, FileDrop (có nút chọn tệp — QF-10), SearchField |
| Hiển thị | Avatar (chữ cái đầu), Tag, TopicChip, GradeLabel (Lớp/Khối), Badge (huy hiệu M12), Counter |
| Nội dung | PostCard (dòng feed), PostBody (rich text + KaTeX + code + bảng), Poll, Attachment, Comment (2 cấp), UpvoteButton |
| Phản hồi | Toast, InlineAlert, Banner (bảo trì, cảnh cáo), EmptyState, Skeleton, ErrorState |
| Cấu trúc | AppHeader, NavBar (desktop), BottomNav (mobile, nếu DD-UI chọn), Tabs, Dialog, Drawer, Menu, Tooltip, Pagination/LoadMore |
| Soạn thảo | EditorToolbar (theo định dạng FR cho phép), CommentComposer |

Mỗi component: mọi trạng thái tương tác (mặc định, hover, focus-visible, active, disabled, đang xử lý) và biến thể
trạng thái nghiệp vụ liên quan (ví dụ PostCard `pending`, `flagged`, `locked`, `anonymous`). Chỉ dùng tokens.

### E. Tạo "iShare Design System" trên Claude Design

1. Tạo (lần đầu) artifact từ type **Design System**, tên "iShare Design System", theo hướng dẫn của type đó. Ghi link
   vào `DESIGN.md` (`design_system`). Bản sao tệp: `.agents/.claude/design/canvas/design-system/`.
2. `project/tokens.json` = đúng nội dung `tokens/tokens.json` của repo.
3. `project/README.md` = "brand book": nguyên tắc (từ `DESIGN.md` mục 2), giọng văn (từ `PRODUCT.md` mục 8), cách
   dùng màu/chữ/khoảng cách bằng tên token, bộ icon, danh sách AP và AP-P cần tránh, sàn chất lượng tóm tắt.
4. Mỗi component: `components/<Tên>/README.md` (câu đầu là tóm tắt; khi nào dùng, khi nào không, trạng thái, ghi chú
   a11y) và `components/<Tên>/preview.html` hiển thị các trạng thái. Không cần bundle React ở bước này.
5. `check_ui.py --tokens` trên bản sao các `preview.html` trước khi gửi: ERROR = 0.

### F. Ghi lại

- `DESIGN.md` mục 3 (tóm tắt tokens: font, thang chữ, màu chính, mật độ, bo góc, bóng, chuyển động), mục 4 (danh sách
  component và trạng thái), mục 5 (DD-UI mới).
- Chuyển `che_do: thuc-thi` trong frontmatter `DESIGN.md`.

## Đầu ra

- `tokens/tokens.json`, `tokens/contrast-pairs.csv`, `tokens/tokens.css`, `tokens/tokens.dtcg.json`.
- "iShare Design System" (link trong `DESIGN.md`); bản sao trong `canvas/design-system/`.
- `DESIGN.md` mục 3, 4, 5.

## Trình ở cổng

- Font (kèm artboard test tiếng Việt), bảng màu (tên, vai trò, mẫu), thang chữ, mật độ, bo góc, bóng, bộ icon.
- Danh sách component và link design system.
- Kết quả `contrast.py` (mọi cặp, mọi theme) và `check_ui.py`.
- Nhắc: từ bước sau, thêm bất kỳ giá trị thị giác mới nào cũng phải qua cổng.

Sau khi người dùng đồng ý: thêm `6` vào `steps_completed`, `buoc_hien_tai: 7`.

## Không làm

- Không thêm token "để dành" không vai trò.
- Không hạ ngưỡng tương phản để giữ màu.
- Không sửa tay `tokens.css`, `tokens.dtcg.json`.
