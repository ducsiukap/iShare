# Sàn chất lượng (quality floor)

[Vietnamese Doc]

Mức tối thiểu mọi màn hình phải đạt, bất kể hướng thẩm mỹ. Mã `QF-xx`. Chuẩn tham chiếu: WCAG 2.2 mức AA (W3C
Recommendation, 10/2023) và Vercel Web Interface Guidelines. Cột "Kiểm" ghi tool hoặc "Mắt".

Một thiết kế tĩnh vẫn phải "đúng như sẽ code": dùng `<button>`, `<a href>`, `<input>` + `<label>` thật trong artboard,
không dùng `div` bấm được.

## 1. Thị giác

| Mã | Yêu cầu | Kiểm |
|---|---|---|
| QF-01 | Tương phản chữ ≥ 4.5:1; chữ lớn (≥ 24px, hoặc ≥ 18.66px đậm) ≥ 3:1. Áp cho mọi theme, kể cả chữ phụ, placeholder, chữ trên nút, chữ trên badge. 4.3:1 vẫn là trượt | `contrast.py` |
| QF-02 | Thành phần không phải chữ cần nhận ra (viền ô nhập, vòng focus, icon mang nghĩa, đường biểu đồ) ≥ 3:1 với nền kề | `contrast.py`; Mắt |
| QF-03 | Không chỉ dùng màu để truyền thông tin: trạng thái (lỗi, bị khóa, chờ duyệt, bị gắn cờ) luôn có chữ hoặc icon kèm. Màu cần phân biệt thì khác nhau cả độ sáng; ưu tiên cặp xanh dương/cam hơn đỏ/xanh lá | Mắt |
| QF-04 | Vùng bấm ≥ 24×24 CSS px (WCAG 2.5.8); hành động chính trên mobile ≥ 44×44 (nút vote, nút gửi, mục điều hướng) | Mắt |

## 2. Tương tác và bàn phím

| Mã | Yêu cầu | Kiểm |
|---|---|---|
| QF-05 | Focus nhìn thấy rõ (`focus-visible`), đạt QF-02, và không bị header dính, thanh soạn bình luận dính hay banner che (WCAG 2.4.11) | Mắt |
| QF-06 | Mọi thao tác làm được bằng bàn phím, thứ tự hợp lý; dialog giữ focus bên trong, đóng bằng Esc, trả focus về chỗ cũ | Mắt (ghi chú trên artboard) |
| QF-07 | Phần tử tương tác là phần tử thật (`button`, `a href`, `input` + `label`); nút chỉ có icon có `aria-label`; SVG trang trí có `aria-hidden="true"` | `UI-A11Y-CLICKDIV` ERROR, `UI-A11Y-IMG-ALT` ERROR, `UI-A11Y-ICON-BUTTON` WARN |
| QF-08 | Form: nhãn luôn thấy (không chỉ placeholder), gợi ý định dạng trước khi nhập, lỗi cụ thể nằm cạnh ô và nói cách sửa, không xóa dữ liệu đã nhập khi lỗi; không bắt nhập lại thông tin đã nhập trong cùng luồng (WCAG 3.3.7), ví dụ đăng ký 3 bước | `UI-A11Y-INPUT-LABEL` WARN; Mắt |
| QF-09 | Đăng nhập/đăng ký không đòi giải đố nhận thức; cho dán mật khẩu, hỗ trợ trình quản lý mật khẩu (`autocomplete`), có nút hiện mật khẩu (WCAG 3.3.8) | Mắt |
| QF-10 | Thao tác kéo-thả (đính kèm tệp, sắp xếp lựa chọn poll) luôn có cách thay bằng nút (WCAG 2.5.7) | Mắt |
| QF-11 | Chuyển động có nhánh `prefers-reduced-motion`; không nhấp nháy quá 3 lần/giây; không tự chạy nội dung chuyển động dài | `UI-NO-REDUCED-MOTION` WARN |

## 3. Bố cục và nội dung

| Mã | Yêu cầu | Kiểm |
|---|---|---|
| QF-12 | Ở bề rộng nhỏ nhất mà `PRODUCT.md` hỗ trợ (390px nếu có điện thoại; chỉ máy tính thì 1280px) không cuộn ngang toàn trang (bảng rộng, công thức dài, khối code cuộn trong khung riêng); dùng được khi zoom 200% | Mắt |
| QF-13 | **Tiếng Việt hiển thị đúng:** font đã qua `font_test.py` (dấu chồng như "ấ ặ ử ỗ" không đè nhau, không chạm dòng trên); line-height thân bài ≥ 1.5, tiêu đề ≥ 1.2; không cắt dấu bởi `overflow: hidden` + line-height chật; không viết hoa đoạn dài; văn bản Unicode NFC; `lang="vi"` | `UI-LINE-HEIGHT` WARN; `font_test.py`; Mắt |
| QF-14 | **Nội dung dài và công thức:** tiêu đề dài tối đa theo FR, tên người dùng dài, nhiều tag, bảng rộng, khối code, công thức KaTeX lớn đều không vỡ bố cục; công thức inline không làm lệch dòng; công thức khối dài cuộn ngang trong khung | Trạng thái `long`; Mắt |
| QF-15 | **Đủ trạng thái:** mỗi màn hình có các trạng thái trong `screen-inventory.md`, tối thiểu `default`, `loading`, `empty` (hoặc `no-result`), `error` khi màn hình tải dữ liệu; thêm các trạng thái nghiệp vụ lấy từ nhánh ngoại lệ của SC (`forbidden`, `locked`, `banned`, `pending`, `flagged`…). Mỗi phần tử tương tác có: mặc định, hover, focus-visible, active, disabled, đang xử lý | `check_inventory.py --require-artboards`; Mắt |
| QF-16 | Trợ giúp, báo cáo, khiếu nại nằm ở vị trí nhất quán giữa các trang (WCAG 3.2.6). Màn hình bị cảnh cáo/khóa/ban nói lý do bằng giọng tôn trọng và chỉ đường sang Khiếu nại (M09) | Mắt |
| QF-17 | Mỗi trang có tiêu đề rõ, vùng chính có landmark (`header`, `nav`, `main`), thứ tự heading không nhảy cấp | Mắt |
| QF-18 | Nếu brief chọn có dark mode: mọi mục trên áp cho cả hai theme, mọi cặp màu trong `contrast-pairs.csv` kiểm ở cả hai | `contrast.py` |

## 4. Đặc thù iShare (nhắc từ nguồn, không phải yêu cầu mới)

- Nội dung người dùng có định dạng rich text (tiêu đề phụ, code, bảng, trích dẫn) và LaTeX hiển thị bằng KaTeX: thang
  chữ thân bài phải hài hòa chiều cao chữ x với công thức.
- Ẩn danh (M11) và các trạng thái kiểm duyệt (M08) phải hiển thị rõ cho đúng người được thấy, không lộ danh tính.
- Học sinh 15–18 tuổi: tránh giao diện "trẻ con hóa" (màu kẹo, mascot, emoji), tránh cả giao diện "doanh nghiệp lạnh".
  Gamification (M12) gắn với hành vi học thật, trình bày tiết chế.
