# Bước 1 — Brief (`PRODUCT.md`)

[Vietnamese Doc]

## Mục đích

Chốt **thiết kế cho ai, để làm gì, trong ràng buộc nào** trước khi nghĩ tới màu hay chữ. `PRODUCT.md` là "sự thật bền
vững" về sản phẩm, đọc lại ở mọi bước sau; hướng thẩm mỹ được chọn từ đây chứ không từ sở thích chung chung.

## Đầu vào

- `module-registry.md`; `docs/specs/us/US-overview.md` (actor, UC chính toàn hệ thống).
- Mỗi `FR-Mxx.md`: frontmatter (phiên bản, trạng thái), mục phạm vi và "không làm ở MS1", mục vai trò. **Chưa** đọc
  chi tiết từng yêu cầu.
- `glossary.md` (tên gọi hiển thị).
- `docs/_temp/iShare_specs_general.md`, mô tả dự án (bối cảnh).
- Câu trả lời Q1-01 … Q1-08 (`input/QUESTIONS.md`).

## Việc làm

1. Tạo `.agents/.claude/design/output/` (và `moodboard/`, `tokens/`, `qa/`, `handoff/`) nếu chưa có. Chép
   `output/product-template.md` → `PRODUCT.md`, `output/design-template.md` → `DESIGN.md`. Điền ngày, tác giả, nhánh.
2. **Mục 10 — Nguồn:** liệt kê từng FR, US-overview, SC đã đọc với phiên bản, ngày, trạng thái. Lấy từ frontmatter
   (FR) hoặc bảng `sc:document` / `uc:document`.
3. **Soạn nháp `PRODUCT.md` từ tài liệu** (mỗi ý có mã nguồn trong ngoặc):
   - Mục 1: iShare là gì, một câu; điều làm nó khác "một forum có bình luận" (theo mô tả dự án).
   - Mục 2: người dùng và vai trò. Dùng actor của US (ACT-001 Khách, ACT-002 Người dùng, ACT-003 Mod/Admin…). Ghi rõ:
     học sinh và giáo viên dùng chung loại tài khoản người dùng (không có loại tài khoản giáo viên riêng). Với mỗi vai
     trò: việc làm nhiều nhất, tần suất, thiết bị (sau khi có Q1-05).
   - Mục 3: bối cảnh dùng: lúc nào, ở đâu, thiết bị nào, mức thành thạo. Chỗ nào là giả định thì ghi "giả định".
   - Mục 4: 5–7 việc chính (jobs) toàn hệ thống, mỗi việc dẫn UC. Đây là thứ màn hình phải làm tốt nhất.
   - Mục 5: ràng buộc: kỹ thuật (React SPA dựng bằng Vite, không SSR/SEO ở MS1; editor Tiptap; LaTeX hiển thị bằng
     KaTeX; giới hạn tệp/ảnh theo FR), ngôn ngữ (tiếng Việt), đối tượng vị thành niên (an toàn nội dung, ẩn danh trong
     nhóm), phạm vi MS1 **không có** (liệt kê từ FR: Accepted Answer, ảnh bìa, downvote, gọi thoại/video, xuất báo cáo…),
     dark mode (Q1-04), thiết bị yếu (Q1-07).
   - Mục 6: cảm xúc muốn / không muốn (Q1-03). Viết thành 3 + 3 từ, mỗi từ một câu giải thích nghĩa trong iShare.
   - Mục 7: thương hiệu có sẵn (Q1-01, Q1-02).
   - Mục 8: giọng văn: xưng hô (Q1-06), mức trang trọng, cách viết thông báo lỗi, thông báo kiểm duyệt (tôn trọng,
     nêu lý do, chỉ đường khiếu nại), câu chữ không dùng (xem AP-51, AP-54).
   - Mục 9: thước đo thành công của giao diện, đề xuất 3–5 tiêu chí kiểm được (ví dụ: học sinh đặt được câu hỏi có
     công thức trên điện thoại mà không phải zoom; Mod xử lý một báo cáo không cần rời hàng chờ). Ghi giả định chưa
     kiểm với người dùng thật (Q2-04).
   - Mục 11: câu hỏi mở: mâu thuẫn giữa nguồn, chỗ nguồn chưa nói mà ảnh hưởng giao diện.
4. **Hỏi người dùng** các câu Q1-xx chưa có trả lời, mỗi câu kèm đề xuất (lượt đầu của bước). Dừng chờ trả lời.
5. Điền câu trả lời vào `PRODUCT.md`. Quyết định thiết kế phát sinh (ví dụ không làm dark mode) → thêm `DD-UI-nn`
   vào `DESIGN.md` mục 5.
6. Tự rà: mọi ý trong `PRODUCT.md` có nguồn (mã tài liệu hoặc "người dùng trả lời Qx-xx" hoặc "giả định"); không
   có ý nào về màu, font, bố cục (đó là bước 3, 6).
7. Đặt `DESIGN.md`: `buoc_hien_tai: 1`, `trang_thai: Chờ duyệt`. Trình cổng.

## Đầu ra

- `.agents/.claude/design/output/PRODUCT.md` (đủ 11 mục).
- `.agents/.claude/design/output/DESIGN.md` (frontmatter + mục 5 nếu có DD-UI).

## Trình ở cổng

- Tóm tắt: vai trò, 5–7 việc chính, ràng buộc lớn nhất, 3 + 3 từ cảm xúc, xưng hô.
- Câu hỏi mở cần người dùng quyết.
- Input cần cho bước 2: danh sách thích/ghét (Q2-01, Q2-02), ảnh app học tập (Q2-03).

Sau khi người dùng đồng ý: thêm `1` vào `steps_completed`, `buoc_hien_tai: 2`.

## Không làm

- Không bàn màu, font, bố cục, phong cách.
- Không thêm việc chính hay ràng buộc không có nguồn.
- Không đọc chi tiết toàn bộ 16 FR ở bước này.
