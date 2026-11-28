# Anti-pattern: dấu hiệu giao diện "kiểu AI" phải tránh

[Vietnamese Doc]

Đây là luật, không phải gợi ý. Mỗi dấu hiệu có mã `AP-xx`, lý do, cách kiểm và cách làm thay. Cột "Kiểm" ghi mã luật
của `tools/check_ui.py` (mức ERROR hoặc WARN), hoặc "Mắt" nếu chỉ kiểm được bằng mắt theo checklist ở mục 9.

Nguồn tổng hợp: bài "Improving frontend design through Skills" của Anthropic (11/2025), skill `frontend-design`
(anthropics/skills, Apache-2.0), Impeccable (pbakaus/impeccable, Apache-2.0), hướng dẫn frontend của OpenAI cho
GPT-5.x, Vercel Web Interface Guidelines và các bài phân tích "AI slop" năm 2025–2026. Ý tưởng được diễn đạt lại cho
iShare; không chép nguyên văn.

## Nguyên tắc dùng danh sách này

1. **Danh sách cấm không tạo ra bản sắc.** Nó chỉ chặn mặc định. Bản sắc đến từ quyết định có lý do (mục 8).
2. **Cẩn thận "mặc định mới".** Né một mẫu bị cấm bằng mẫu phổ biến kế tiếp vẫn là dáng AI (AP-07, AP-10).
3. **Ngoại lệ có thể có, nhưng phải được ghi.** Muốn dùng một mẫu trong danh sách (ví dụ thương hiệu trường thật sự
   màu tím), ghi vào bảng ngoại lệ của `DESIGN.md` (mục 6) gồm mã AP, phạm vi tệp, lý do, mã DD-UI, và người dùng đã
   duyệt. `check_ui.py --design` đọc bảng đó và hạ cảnh báo tương ứng xuống INFO.
4. **ERROR phải sửa trước khi gửi artboard. WARN phải có lý do nếu giữ.**

## 1. Màu

| Mã | Dấu hiệu | Vì sao tránh | Kiểm | Làm thay |
|---|---|---|---|---|
| AP-01 | Tím, indigo, violet làm màu chủ đạo hoặc nhấn; gradient tím→xanh (`#667eea → #764ba2`, `indigo-500 #6366f1`, `violet-500`, `purple-500`) | Màu "mặc định" của giao diện AI (bắt nguồn từ Tailwind UI và các gradient phổ biến) | `UI-PURPLE-KNOWN` ERROR, `UI-PURPLE-HUE` WARN | Màu xuất phát từ hướng thẩm mỹ đã chốt và moodboard; có tên và vai trò |
| AP-02 | Gradient làm nền hoặc trang trí (gradient wash, đốm màu mờ phía sau nội dung) | Trang trí không mang thông tin, làm rối, dấu hiệu nhận ra ngay | `UI-GRADIENT` WARN | Nền phẳng có sắc; nhấn bằng tương phản, khoảng trắng, chữ |
| AP-03 | Chữ gradient (`background-clip: text`, `bg-clip-text`) | Dấu hiệu AI rõ nhất; khó đọc; tương phản không xác định | `UI-GRADIENT-TEXT` ERROR | Nhấn bằng độ đậm, cỡ chữ, một màu nhấn đặc |
| AP-04 | Glow neon, viền phát sáng, bóng màu quanh chữ/nút; bật nền tối theo phản xạ | Mặc định "công nghệ" không hợp học sinh đọc bài dài | `UI-GLOW` WARN | Dark mode chỉ khi brief chọn; độ sâu bằng bóng trung tính có kiểm soát |
| AP-05 | Đen tuyền `#000` cho chữ/nền lớn; xám trung tính không pha sắc | Gắt, "chưa ai chọn"; xám thuần làm giao diện vô hồn | `UI-PURE-BLACK` WARN | Neutral pha nhẹ sắc của màu chủ đạo; mực chữ đậm nhưng không đen tuyền |
| AP-06 | Chữ xám trên nền màu; chữ phụ quá nhạt | Hay trượt chuẩn tương phản | `contrast.py`; Mắt | Mỗi cặp chữ/nền nằm trong `contrast-pairs.csv` và đạt QF-01 |
| AP-07 | "Mặc định mới": nền kem + serif hiển thị + điểm nhấn đất nung/sage; hoặc nền gần đen + một màu acid | Là nơi model trượt tới khi bị cấm tím/Inter | Mắt (brand test) | Chỉ dùng nếu bắt nguồn từ moodboard và có DD-UI ghi lý do |

## 2. Chữ

| Mã | Dấu hiệu | Vì sao tránh | Kiểm | Làm thay |
|---|---|---|---|---|
| AP-10 | Font mặc định làm font chính: Inter, Roboto, Poppins, Geist, Open Sans, Lato, Montserrat, Arial, Helvetica, `system-ui` | Không ai chọn; giao diện không có giọng | `UI-FONT-BANNED` ERROR | Chọn font có lý do (giọng, khả năng đọc tiếng Việt), đã qua `font_test.py` |
| AP-10b | "Font AI thế hệ mới": Space Grotesk, DM Sans, Manrope, Plus Jakarta Sans, Outfit, Sora | Đang thành mặc định mới | `UI-FONT-OVERUSED` WARN | Được dùng nếu có lý do ghi trong DD-UI |
| AP-11 | Một độ đậm cho mọi cấp chữ; thang chữ không rõ cấp | Không có phân cấp, mọi thứ "phẳng" như nhau | `UI-ONE-WEIGHT` WARN | Thang chữ có chủ đích (bước 6), ít nhất 2 độ đậm, vai trò từng cấp rõ |
| AP-12 | Nhãn nhỏ VIẾT HOA giãn chữ (eyebrow) phía trên mọi tiêu đề | Thói quen landing page; với tiếng Việt viết hoa còn làm dấu khó đọc | `UI-EYEBROW` WARN | Dùng khi thật sự cần phân nhóm; thường bỏ |
| AP-13 | Hero căn giữa với badge dạng pill ("✨ Mới có AI") | Mẫu landing page điển hình | Mắt; `UI-EMOJI` | Màn hình ứng dụng mở thẳng vào nội dung |
| AP-14 | Viết hoa cả đoạn hoặc nút dài bằng tiếng Việt | Dấu chồng khó đọc, cảm giác la hét | Mắt | Viết hoa đầu câu |

## 3. Bố cục

| Mã | Dấu hiệu | Vì sao tránh | Kiểm | Làm thay |
|---|---|---|---|---|
| AP-20 | Bố cục landing page trong màn hình ứng dụng: hero → lưới 3 card tính năng có icon → bento grid → hàng bước "1 · 2 · 3" → bảng giá 3 cột | iShare là ứng dụng dùng hằng ngày, không phải trang quảng cáo | Mắt | Bố cục theo việc chính của màn hình (đọc, viết, duyệt, trò chuyện) |
| AP-21 | Đối xứng tuyệt đối, mọi khối cùng trọng lượng, không có điểm nhấn | Không biết nhìn vào đâu trước | Mắt | Một điểm nhấn rõ mỗi màn hình; bất đối xứng có lý do |
| AP-22 | Mật độ sai: khoảng trắng kiểu marketing cho danh sách dùng hằng ngày, hoặc nhồi nhét không nhịp | Học sinh lướt trên điện thoại cần đọc nhanh; mod cần thấy nhiều mục | Mắt | Mật độ chốt ở bước 6 theo từng loại màn hình |
| AP-23 | Card lồng card; khung trong khung | Tầng tầng viền và bóng, nặng nề | Mắt | Phân nhóm bằng khoảng cách và đường kẻ mảnh, không lồng khung |
| AP-24 | Cụm pill/chip, dải thống kê, hàng icon rải khắp | Rối, không mang thông tin chính | Mắt | Chỉ hiện thông tin có trong FR và cần cho việc chính |

## 4. Component

| Mã | Dấu hiệu | Vì sao tránh | Kiểm | Làm thay |
|---|---|---|---|---|
| AP-30 | Mọi thứ cùng một bo góc lớn (`rounded-2xl`) và cùng một bóng mềm | "Dáng shadcn mặc định" | `UI-RADIUS-UNIFORM` WARN | Bo góc theo vai trò (tối đa 3 mức + tròn hẳn), chốt ở bước 6 |
| AP-31 | Viền xám 1px kèm bóng rộng trên cùng một khối | Hai cách tách lớp chồng nhau | `UI-SHADOW-WIDE` WARN | Chọn một: viền hoặc bóng |
| AP-32 | Card có dải viền trái 3–6px màu | Dấu hiệu AI phổ biến | `UI-LEFT-STRIPE` WARN | Biểu thị trạng thái bằng nhãn có chữ + icon |
| AP-33 | Glassmorphism, `backdrop-filter: blur` không lý do | Trang trí, giảm tương phản, nặng máy yếu | `UI-GLASS` WARN | Nền đặc |
| AP-34 | Lớp màu mặc định của Tailwind/shadcn để nguyên (`slate-*`, `zinc-*`, `gray-*`, `indigo-*`; radius `0.625rem`) | Không ai chọn | `UI-TW-DEFAULT` WARN; chế độ thực thi: `UI-TOK-*` | Chỉ tên token của iShare |

## 5. Icon

| Mã | Dấu hiệu | Vì sao tránh | Kiểm | Làm thay |
|---|---|---|---|---|
| AP-40 | Emoji làm icon, bullet, trong nút hoặc tiêu đề (✨ 🚀 ✅ ⭐ 🔥 💡…) | Dấu hiệu AI rõ; hiển thị khác nhau giữa máy | `UI-EMOJI` ERROR | Một bộ icon SVG duy nhất, chốt ở bước 6 |
| AP-41 | Ô vuông/tròn màu chứa icon đặt trên mỗi tiêu đề hoặc card | Mẫu "feature card" | Mắt | Icon chỉ khi giúp nhận diện hành động |
| AP-42 | Trộn nhiều bộ icon, độ dày nét khác nhau | Thiếu nhất quán | Mắt | Một bộ, một độ dày, một lưới kích thước |
| AP-43 | Mũi tên "→" ở cuối mọi nút/link | Thói quen landing page | `UI-ARROW` WARN | Nhãn nút là động từ rõ nghĩa |

## 6. Nội dung chữ

| Mã | Dấu hiệu | Vì sao tránh | Kiểm | Làm thay |
|---|---|---|---|---|
| AP-50 | Lorem ipsum, "Tiêu đề ở đây", "Nội dung mẫu", "Text" | Không thử được bố cục với nội dung thật | `UI-LOREM` ERROR | Dữ liệu giả lập của SC; câu hỏi thật của học sinh |
| AP-51 | Câu sáo rỗng: "Khai phá tiềm năng", "Nâng tầm", "Bứt phá", "Trải nghiệm liền mạch", "mạnh mẽ", "Unlock", "Elevate", "Supercharge", "Seamless" | Tính từ thay cho sự thật | `UI-CLICHE` WARN | Nói cụ thể việc người dùng làm được |
| AP-52 | Số liệu giả ("nhanh hơn 10x", "99,9%", "1M+ người dùng"), lời chứng thực bịa, logo "được tin dùng bởi" | Sai sự thật, iShare chưa có số liệu | `UI-FAKE-STAT` WARN | Không hiện số liệu không có nguồn |
| AP-53 | Tên mẫu giả: "Nguyễn Văn A", "John Doe", "User 1", "Người dùng 123" | Không thử được tên dài, tên Việt thật | `UI-FAKE-NAME` WARN | Tên Việt thường gặp, có tên dài để thử bố cục |
| AP-54 | "Không chỉ là X, mà là Y"; mọi thứ theo bộ ba; giọng quảng cáo trong thông báo hệ thống | Giọng văn AI | Mắt | Giọng văn theo `PRODUCT.md`: ngắn, rõ, tôn trọng |

## 7. Chuyển động và tính đặc thù ứng dụng

| Mã | Dấu hiệu | Vì sao tránh | Kiểm | Làm thay |
|---|---|---|---|---|
| AP-60 | Nảy/đàn hồi khi hover, hiệu ứng vi mô rải rác không mục đích | Rối, gây mệt | `UI-BOUNCE` WARN | Chuyển động ngắn, có mục đích (phản hồi, chuyển trạng thái) |
| AP-61 | Chuyển động không tôn trọng `prefers-reduced-motion` | QF-11 | `UI-NO-REDUCED-MOTION` WARN | Luôn có nhánh giảm chuyển động |
| AP-70 | Chỉ có happy path với dữ liệu đẹp | Màn hình thật luôn có rỗng, lỗi, đang tải, bị khóa… | `check_inventory.py --require-artboards`; Mắt | Mọi trạng thái trong inventory có artboard |
| AP-71 | Không thử nội dung dài, tiếng Việt nhiều dấu, công thức rộng | Vỡ bố cục khi dùng thật | `UI-LINE-HEIGHT` WARN; Mắt | Trạng thái `long` cho màn hình có nội dung người dùng |
| AP-80 | Giá trị ngoài tokens (chế độ thực thi) | Thiết kế trôi, 16 module lệch nhau | `UI-TOK-COLOR`, `UI-TOK-FONT` ERROR; `UI-TOK-SPACE`, `UI-TOK-RADIUS`, `UI-TOK-SIZE` WARN | Dùng token; thiếu thì đề xuất thêm token ở cổng |

## 8. Cách tạo bản sắc (thay vì chỉ né)

1. **Đi từ chất liệu của bối cảnh thật**, không đi từ catalog phong cách. Bối cảnh của iShare: học sinh THPT Việt Nam,
   hỏi đáp và chia sẻ kiến thức, đọc bài có công thức, học nhóm. Hạt giống ý tưởng (để khơi gợi, không phải đáp án;
   chọn hạt giống nào cũng phải có lý do từ brief và moodboard):
   - Trong trường: vở ô ly/kẻ ngang, giấy kiểm tra, bảng tin lớp, lề sách giáo khoa có ghi chú, bảng phấn, sổ tay ôn thi.
   - Ngoài trường: tạp chí khoa học phổ thông, ứng dụng đọc sách, thư viện, bản đồ/sơ đồ tư duy, bảng điều khiển gọn
     của công cụ làm việc.
2. **Các hướng ở bước 3 phải khác nhau ít nhất 3 trục** trong: giọng chữ (serif/sans/hỗn hợp, độ tương phản nét), nhiệt
   độ màu, mật độ, ngôn ngữ hình khối (bo góc, viền, bóng), cấu trúc bố cục (cột, nhịp, điểm nhấn).
3. **Chữ là phần lớn bản sắc.** Diễn đàn đọc nhiều chữ: chọn font thân bài cho việc đọc tiếng Việt dài; font tiêu đề
   cho giọng. Kiểm bằng `font_test.py`.
4. **Bảng màu giới hạn**: một màu chủ đạo, một màu nhấn, các màu ngữ nghĩa (thành công, cảnh báo, nguy hiểm, thông
   tin), neutral pha sắc. Mỗi màu có tên và vai trò.
5. **Một chi tiết nhận diện có chủ đích** (cách trình bày công thức, cách hiện điểm/huy hiệu, nhịp của danh sách bài),
   lặp lại nhất quán. Không rải trang trí.
6. **Brand test**: che logo và thanh điều hướng, màn hình vẫn phải nhận ra là iShare. Không nhận ra → bản sắc quá yếu.

## 9. Checklist bằng mắt (tự rà trước mỗi cổng có vẽ)

- [ ] Không có mẫu nào ở cột "Mắt" của các bảng trên (AP-07, 13, 14, 20–24, 41, 42, 54, 70, 71).
- [ ] Brand test đạt (mục 8.6).
- [ ] Nheo mắt nhìn: thấy ngay một điểm nhấn và thứ tự đọc; không phải một mặt phẳng đều.
- [ ] Mọi màu, font, bo góc, bóng đều truy được về DD-UI hoặc token có tên.
- [ ] Nội dung là dữ liệu giả lập của SC, tiếng Việt có dấu, có trường hợp dài.
- [ ] Không có gì người dùng đã nói "ghét" ở bước 2 (`AP-P-nn` trong `DESIGN.md`).
