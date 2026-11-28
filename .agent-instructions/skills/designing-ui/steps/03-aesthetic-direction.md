# Bước 3 — Hướng thẩm mỹ

[Vietnamese Doc]

## Mục đích

Chọn **bản sắc** của iShare bằng cách so 2–3 hướng khác hẳn nhau trên **cùng một màn hình mẫu**, với nội dung thật.
Đây là bước quyết định "dáng" của cả sản phẩm, nên mỗi hướng phải có lý do gắn với `PRODUCT.md` và `moodboard.md`.

Chế độ: **khám phá** (`input/CONVENTIONS.md` mục 5). Đọc lại `input/ANTI-PATTERNS.md` và `input/QUALITY-FLOOR.md`
trước khi bắt đầu.

## Đầu vào

- `PRODUCT.md`, `moodboard.md`, `DESIGN.md` mục 6 (`AP-P-nn`) đã duyệt.
- `FR-M03.md` (bài viết), `FR-M04.md` (bình luận), `FR-M05.md` (Topic/Tag), `FR-M12.md` (upvote, điểm, huy hiệu
  hiển thị trên bài), phần liên quan của `FR-M11.md` (ẩn danh trong nhóm); `SC-M03.md`, `SC-M04.md` (dữ liệu giả lập).

## Việc làm

### A. Chốt màn hình mẫu: "Chi tiết bài viết"

Màn hình này dồn đủ thứ khó nhất của iShare: chữ dài tiếng Việt, công thức, phân cấp nội dung, tương tác, bình luận
nhiều tầng. Chọn đúng màn hình mẫu thì hướng nào sống sót ở đây sẽ sống được ở các màn hình khác.

1. Lập **danh sách phần tử** của màn hình từ FR, mỗi phần tử kèm mã (FR/BR). Thường gồm (kiểm lại với FR hiện hành,
   bỏ hoặc thêm theo nguồn): tiêu đề; tác giả (tên, ảnh đại diện, thời điểm; hiển thị ẩn danh khi bài trong nhóm bật
   ẩn danh); Lớp/Khối; Topic; Tag; nội dung rich text có công thức LaTeX, khối code, bảng, trích dẫn; tệp đính kèm;
   poll nếu bài có; nút upvote (Post Star) và số lượng; dấu "đã sửa"/lịch sử; báo cáo; bình luận 2 cấp với upvote,
   trả lời, trích dẫn, sắp xếp Top / Mới nhất / Cũ nhất; ô soạn bình luận tối giản.
2. Ghi rõ những gì **không có** ở MS1 để không vẽ nhầm: Accepted Answer (BR-M04-11), ảnh bìa (BR-M03-50), downvote
   (BR-M12-01), và các mục "không làm" khác trong FR.
3. Nội dung mẫu lấy từ bộ dữ liệu giả lập của SC (bài P301 "Giải phương trình bậc hai" của U-LAN, poll Q301, bình
   luận…), bổ sung cho đủ dài: một bình luận dài, một tên người dùng dài, một công thức khối. Ghi bộ dữ liệu vào
   `DESIGN.md` mục 7 để các bước sau dùng lại.

### B. Soạn 2–3 hướng

Mỗi hướng là một "phiếu hướng" (ghi trong tin nhắn cổng; hướng được chọn chép vào `DESIGN.md` mục 2):

1. **Tên** ngắn, gợi hình (ví dụ "Vở ghi", "Tạp chí", "Bảng tin lớp" — chỉ là ví dụ cách đặt tên) và **một câu ý tưởng
   gốc**: hướng này lấy cảm hứng từ đâu trong bối cảnh iShare, vì sao hợp `PRODUCT.md` mục 6.
2. **Token plan sơ bộ:**
   - 4–6 màu, mỗi màu có **tên theo vai trò** (nền, mực chữ, chữ phụ, đường kẻ, màu chủ đạo, màu nhấn) và mã hex.
   - Cặp font: tiêu đề và thân bài (và mono cho code nếu khác mặc định), lý do chọn, đã có bộ ký tự tiếng Việt trên
     Google Fonts (hoặc nguồn font có giấy phép dùng web).
   - Thang chữ sơ bộ (4–5 cấp), line-height thân bài ≥ 1.5.
   - Ngôn ngữ hình khối: bo góc (mấy mức), viền hay bóng, độ dày đường kẻ.
   - Mật độ và nguyên tắc bố cục: số cột trên desktop, độ rộng dòng chữ bài viết, điểm nhấn của màn hình.
3. **Wireframe ASCII** của màn hình mẫu (desktop) trước khi vẽ, để thấy bố cục của hướng khác các hướng kia ra sao.
4. **Rủi ro** của hướng (ví dụ "dễ trông trẻ con", "đọc dài trên mobile có thể mệt").

Ràng buộc giữa các hướng:

- Khác nhau ít nhất **3 trục** trong: giọng chữ, nhiệt độ màu, mật độ, ngôn ngữ hình khối, cấu trúc bố cục
  (`ANTI-PATTERNS.md` mục 8).
- Không hướng nào vi phạm AP hay `AP-P-nn`. Hướng nào gần "mặc định mới" (AP-07, AP-10b) phải nói rõ lý do từ
  moodboard, nếu không thì bỏ.
- Tự đối chiếu từng hướng với `PRODUCT.md` mục 6 (muốn/không muốn) trước khi vẽ. Hướng nào trượt thì sửa hoặc bỏ.

### C. Test font

Chạy `font_test.py` cho mọi font ứng viên của các hướng (một artboard `font-test.dc.html` trên trang "Font" của canvas):

```
python3 $SK/tools/font_test.py --font "<Font A>:400;700" --font "<Font B>:400;600" … --out <root>/project/font-test.dc.html
```

Font nào để dấu chồng đè nhau, chạm dòng trên, hoặc rơi về font dự phòng ở ký tự có dấu → loại khỏi hướng, thay font
khác trước khi vẽ.

### D. Vẽ trên Claude Design

1. Tạo (lần đầu) canvas **"iShare — Khám phá"** từ type Design theo hướng dẫn của type đó. Ghi link vào frontmatter
   `DESIGN.md` (`canvas_kham_pha`). Thư mục gốc bản sao: `.agents/.claude/design/canvas/kham-pha/`.
2. **Không dùng design system nào** cho canvas này ở bước 3: nói rõ điều đó khi làm theo hướng dẫn của type, và dùng
   token plan của từng hướng. Không để canvas tự áp "mặc định" của type.
3. Trang (page) "Bước 3 — Hướng thẩm mỹ": mỗi hướng một artboard `huong-<n>--chi-tiet-bai--desktop.dc.html` (trang
   co giãn, rộng 1440); thêm `huong-<n>--chi-tiet-bai--mobile.dc.html` (rộng 390) **chỉ khi** `PRODUCT.md` mục 3 có hỗ
   trợ điện thoại; thêm `huong-<n>--chi-tiet-bai--desktop--dark.dc.html` khi `PRODUCT.md` có dark mode, để thấy hướng
   có sống được ở cả hai theme. Mỗi hàng một hướng, có ghi chú tiêu đề là tên hướng. Trang "Font": artboard font test.
4. Mỗi artboard: nội dung thật ở mục A; phần tử tương tác là `button`/`a`/`input` thật; icon là SVG nét (không emoji);
   chỉ font từ Google Fonts qua `<link>` trong `<helmet>`.
5. Lý do và so sánh viết trong tin nhắn cổng, không viết lên artboard.

### E. Tự kiểm trước khi trình

1. `check_ui.py` (chế độ khám phá) trên bản sao cục bộ, **trước khi gửi** lên canvas:
   `python3 $SK/tools/check_ui.py .agents/.claude/design/canvas/kham-pha/project --design $D/DESIGN.md`.
   ERROR = 0. WARN giữ lại phải có lý do trong tin nhắn cổng.
2. Kiểm nhanh tương phản các cặp chính của từng hướng:
   `python3 $SK/tools/contrast.py --fg "<mực chữ>" --bg "<nền>"` (và chữ phụ, chữ trên màu chủ đạo).
3. Checklist bằng mắt (`ANTI-PATTERNS.md` mục 9), gồm **brand test** cho từng hướng.

### F. Sau khi người dùng chọn

1. `DESIGN.md` mục 2: hướng được chọn (tên, ý tưởng gốc, token plan sơ bộ, lý do chọn, phần trộn từ hướng khác nếu
   có), và các hướng bị loại kèm một dòng lý do.
2. `DESIGN.md` mục 5: các `DD-UI-nn` phát sinh (font, màu chủ đạo, ngôn ngữ hình khối, mức gamification…).
3. Không xóa artboard của hướng bị loại (để tham khảo).

## Đầu ra

- Canvas "iShare — Khám phá": trang "Bước 3 — Hướng thẩm mỹ" (2–3 hướng × các bản theo `PRODUCT.md`: desktop, mobile
  nếu có, tối nếu có), trang "Font".
- Bản sao trong `.agents/.claude/design/canvas/kham-pha/`.
- `DESIGN.md` mục 2, 5, 7 (sau khi chọn).

## Trình ở cổng

- Mỗi hướng: tên, ý tưởng gốc, token plan rút gọn (cả bảng màu tối nếu có dark mode), điểm mạnh, rủi ro, link artboard.
- Đề xuất của mình (hướng nào, vì sao) — người dùng vẫn là người chọn.
- Kết quả tool và WARN giữ lại.
- Câu hỏi Q3-01 (chọn/trộn), Q3-02, Q3-03.

Sau khi người dùng chọn và đồng ý: thêm `3` vào `steps_completed`, `buoc_hien_tai: 4`.

## Không làm

- Không vẽ màn hình khác ngoài màn hình mẫu (và trang font).
- Không chốt tokens cuối cùng (bước 6 mới chốt).
- Không vẽ phần tử không có trong danh sách ở mục A.
