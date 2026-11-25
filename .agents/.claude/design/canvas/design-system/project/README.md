iShare là diễn đàn hỏi đáp và chia sẻ tri thức cho học sinh THPT (15–18 tuổi), dùng trên máy tính. Hướng thiết kế là **"Sổ tay"**: trang vở ghi gọn gàng — ba cột rõ ràng, xanh ngọc lá dịu, góc gần vuông như mép giấy, phân nhóm bằng khoảng trắng và đường kẻ mảnh. Cảm giác cần có: **gọn gàng, đáng tin, có chất học trò**; tránh **trẻ con, rối, lạnh lùng kiểu công nghệ**.

Mọi giá trị nằm trong `tokens.json`; component dùng class `is-*` trong `components/bundle.css`. Từ đây, thêm bất kỳ giá trị thị giác mới nào (màu, cỡ chữ, khoảng cách, bo góc, bóng, icon) đều phải qua duyệt và vào `tokens.json` trước.

## Giọng văn

- Gọi người dùng là **"bạn"**; hệ thống không xưng "tôi", "chúng tôi".
- Thân thiện, ngắn, rõ; không suồng sã, không tiếng lóng, không giọng quảng cáo, không câu sáo rỗng.
- Lỗi nói **chuyện gì xảy ra + làm gì tiếp**: "Chưa tải được bài viết. Kiểm tra kết nối rồi thử lại."
- Thông báo kiểm duyệt tôn trọng, nêu lý do và thời hạn, chỉ đường khiếu nại khi được phép: "Bài viết của bạn đã bị ẩn vì ⟨lý do⟩. Nếu bạn cho rằng quyết định chưa đúng, bạn có thể khiếu nại trước ⟨hạn⟩."
- Thuật ngữ hiển thị: bài viết, bình luận, **Chủ đề**, **Tag**, Lớp/Khối, nhóm, **Upvote**, điểm, **Huy hiệu**, "Ngôi sao tuần", cảnh cáo, ban, khiếu nại; tab trang chủ **Thịnh hành / Đang theo dõi / Nhóm / Mới nhất**.
- Viết hoa chữ đầu câu và tên riêng, không viết hoa toàn bộ nhãn. Không dùng emoji trong giao diện.
- Ngày giờ theo kiểu Việt Nam: `08/11/2026, 08:30`; số có dấu chấm ngăn nghìn: `1.284`; dung lượng `1,2 MB`.

## Màu

Hai theme **Sáng** (mặc định) và **Tối**, cùng tên token; component chỉ dùng token ngữ nghĩa, không dùng thẳng lớp gốc `neutral-*`, `teal-*`.

- Nền trang `bg`; khối nội dung `surface` có viền `line` 1px, không đổ bóng. Lớp nổi (menu, popover, dialog, ngăn trượt, toast) dùng `surface-raised` + `shadow-1`/`shadow-2`, không viền.
- Chữ `ink`; chữ phụ `ink-muted`. Cả hai đạt ≥ 4.5:1 trên `bg`, `surface`, `surface-raised`, `surface-hover`, `primary-soft` ở cả hai theme.
- `primary` (xanh ngọc lá) cho hành động chính, liên kết, Upvote, mục đang chọn, Chủ đề. Chữ trên nền `primary` là `on-primary` — ở theme tối là màu tối, không phải trắng. Nền nhấn nhạt là `primary-soft`.
- Viền ô nhập, checkbox, nút phụ dùng `line-strong` (≥ 3:1); đường kẻ trang trí dùng `line`.
- Vòng focus: viền 2px `focus`, cách thành phần 2px, ≥ 3:1 trên mọi nền.
- Trạng thái `success`, `warning`, `danger`, `info` + nền `*-soft`; luôn kèm chữ hoặc icon, không chỉ dựa vào màu. `success` lệch về phía xanh dương để khác `danger` (đỏ cam) với người mù màu đỏ–xanh lá.
- Nút nguy hiểm: nền `danger`, chữ `on-danger`.
- Nội dung bài: tô sáng `mark` (chữ `ink`); tô màu cú pháp `syntax-keyword`, `syntax-string`, `syntax-number`, `syntax-function`, `syntax-comment` trên nền `bg` của khối code.
- Biểu đồ: `chart-1`, `chart-2`, `chart-3` là thang một sắc, khác nhau bằng độ sáng (LIGHT → MEDIUM → HEAVY); biểu đồ một chuỗi dùng `chart-2`. Luôn có chú thích chữ và bảng số liệu.
- Lớp phủ sau dialog: `scrim`.

## Chữ

- Một họ chữ **Be Vietnam Pro** (400, 600, 700, có nghiêng) cho giao diện và nội dung; **JetBrains Mono** cho code, tắt ký tự ghép (`font-variant-ligatures: none`) để `=>`, `!=` hiện đúng ký tự.
- Thang: `display` 30 (tiêu đề bài) · `h1` 26 (tiêu đề trang) · `h2` 22 (mục) · `h3` 19 (tiêu đề bài trong danh sách, tiêu đề dialog) · `body` 17/1.7 (nội dung bài) · `body-comment` 16/1.6 (bình luận, tin nhắn) · `ui` và `label` 15 (giao diện, nhãn) · `body-sm` 14 (chữ phụ, bảng gọn) · `caption` 13 (ghi chú, thời gian) · `code` 15/1.6.
- Tiêu đề mục trong bài: `post-h1` 22, `post-h2` 19, `post-h3` 17 đậm.
- Tiếng Việt cần dòng thoáng: chữ ≤ 20px có line-height ≥ 1.5; tiêu đề ≥ 1.3. Không cắt chữ bằng `overflow: hidden` khi line-height chật (dấu chồng "ấ ặ ử ỗ" bị mất).
- Công thức KaTeX trong bài cỡ 1.1em theo `body`; công thức khối dài cuộn ngang trong khung riêng.

## Khoảng cách và mật độ

- Thang bội số 4px: `space-1` 4 · `space-2` 8 · `space-3` 12 · `space-4` 16 · `space-5` 20 · `space-6` 24 · `space-8` 32 · `space-10` 40 · `space-12` 48 · `space-16` 64; `space-0-5` 2 cho khe rất nhỏ.
- **Màn hình của học sinh: mật độ vừa** — nút, ô nhập cao `control-h` 40px, dòng danh sách `row-h` 52px, chữ 15px.
- **Khu kiểm duyệt và quản trị: mật độ gọn** — bảng `row-h-sm` 38px, chữ 14px, nút và bộ lọc `control-h-sm` 32px.
- Bố cục desktop 1440, không vỡ ở 1280: thanh trên cùng `topbar-h` 64px; cột điều hướng `nav-w` 200px; cột phụ `aside-w` 260px khi trang có nội dung phụ, nếu không thì cột nội dung tối đa `content-max` 820px.
- Phân nhóm bằng khoảng trắng và đường kẻ, không lồng khung trong khung.

## Bo góc, viền, bóng

- `radius-sm` 2px cho mọi khối: thẻ, nút, ô nhập, chip, dialog, menu, toast, khối code.
- `radius-full` chỉ cho ô tìm kiếm (bo tròn hai đầu), avatar, số đếm, công tắc, thanh kết quả bình chọn.
- Khối nội dung: viền 1px `line`, không bóng. Bóng chỉ cho lớp nổi thật: `shadow-1` (menu, popover, toast, tooltip), `shadow-2` (dialog, ngăn trượt); không kèm viền.

## Chuyển động

- Nhanh 120ms cho hover, focus, nút; vừa 200ms cho menu, popover, toast, tab; chậm 280ms cho dialog, ngăn trượt.
- Vào: `cubic-bezier(0.2, 0, 0, 1)`; ra: `cubic-bezier(0.4, 0, 1, 1)`. Không nảy, không đàn hồi.
- `prefers-reduced-motion: reduce`: tắt mọi chuyển động và nhấp nháy (Skeleton đứng yên, icon xoay đứng yên).

## Icon

- Bộ duy nhất **Material Symbols Sharp** weight 400, lưới 24px (`assets/Icons`); cỡ `icon` 24, `icon-sm` 20, `icon-xs` 16; tô bằng màu chữ (`currentColor`).
- Bản tô đặc (`-fill`) cho trạng thái đang bật: đã upvote, đã lưu, Ngôi sao tuần.
- Upvote chưa bấm dùng icon nét dày `shift-w600` — ngoại lệ duy nhất về độ dày nét (DD-UI-11).
- Icon trang trí `aria-hidden`; nút chỉ có icon luôn có `aria-label`. Không dùng emoji làm icon.

## Logo

Không có tệp logo: chữ **"iShare"** bằng Be Vietnam Pro 700, 22px, "i" màu `ink`, "Share" màu `primary` (xem AppHeader).

## Quy tắc nền tảng

- Mọi trạng thái (lỗi, bị khóa, chờ duyệt, bị gắn cờ) có chữ hoặc icon kèm màu.
- Vùng bấm ≥ 24×24px; focus luôn nhìn thấy và không bị thanh dính che.
- Phần tử tương tác là phần tử thật (`button`, `a href`, `input` + `label`).
- Form: nhãn luôn hiện, gợi ý định dạng trước khi nhập, lỗi cụ thể cạnh ô và nói cách sửa, không xóa dữ liệu đã nhập.
- Cho dán mật khẩu, có nút hiện mật khẩu, hỗ trợ trình quản lý mật khẩu.
- Kéo-thả luôn có nút thay thế.
- Mỗi màn hình tải dữ liệu có đủ `default`, `loading`, `empty` hoặc `no-result`, `error` và các trạng thái nghiệp vụ.
- Trợ giúp, báo cáo, khiếu nại ở vị trí cố định giữa các trang.
- Theme tối: mọi quy tắc trên áp dụng như theme sáng.

## Tránh

- Màu tím, gradient, chữ gradient; font mặc định (Inter, Roboto, Arial…) làm font chính.
- Bố cục landing page trong màn hình ứng dụng; thẻ lồng thẻ; dải viền trái màu trên thẻ; glassmorphism.
- Mọi thứ cùng một bo góc lớn và một bóng mềm; viền 1px kèm bóng rộng trên cùng khối.
- Emoji làm icon; trộn nhiều bộ icon; mũi tên "→" cuối mọi nút; ô màu chứa icon trên mỗi thẻ.
- Dải thống kê, cụm chip trang trí không mang thông tin chính; mascot, màu kẹo, huy hiệu lòe loẹt.
- **Sao chép y nguyên hoặc làm giống hệt giao diện của bất kỳ trang tham khảo nào** (bố cục toàn trang, màu, font, icon, logo, khoảng cách đặc trưng) — chỉ mượn pattern.

## Dùng component

- Nạp `tokens.css` (sinh từ `tokens.json`) rồi `components/bundle.css`; đặt `data-theme="light"` hoặc `data-theme="dark"` trên `<html>`.
- Mỗi component có `components/<Tên>/README.md` (khi dùng, trạng thái, dữ liệu cần, khả năng truy cập, class và token) và `preview.html` (mọi trạng thái).
- Không có bundle React ở giai đoạn này; khi viết frontend, dựng component theo README và class `is-*`, hoặc chuyển giá trị sang Tailwind bằng `tokens.css`.
