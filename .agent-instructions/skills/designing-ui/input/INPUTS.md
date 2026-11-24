# Đầu vào của skill designing-ui

[Vietnamese Doc]

Ba nhóm đầu vào: tài liệu dự án (đọc từ repo), câu trả lời và tài nguyên của người dùng (hỏi theo `QUESTIONS.md`),
và công cụ (Claude Design, Figma). Tài liệu dự án là nguồn sự thật về chức năng; người dùng là nguồn sự thật về mong
muốn và thẩm mỹ.

## 1. Tài liệu dự án

Tất cả nằm trên nhánh `docs/ui-design` (tách từ `docs/all-data`).

| Tài liệu | Đường dẫn | Dùng để | Đọc ở bước |
|---|---|---|---|
| FR (đã chốt) | `docs/specs/fr/FR-Mxx.md` (M01–M16), `docs/specs/fr/review-cross-module.md` | Phạm vi chức năng, vai trò, quy tắc hiển thị, giới hạn (độ dài, số lượng, kích thước tệp), thông điệp, những gì **không** làm ở MS1 | 1 (mục phạm vi), 3 (FR-M03, FR-M04), 4, 5, 7 |
| Use case | `docs/specs/us/US-Mxx.md`, `docs/specs/us/US-overview.md` | Actor và quyền (`<!-- uc:actors -->`), danh mục UC (`<!-- uc:catalog -->`), phân rã chính–con, truy vết FR | 1, 4 |
| Scenario | `docs/specs/scenarios/Mxx/SC-Mxx.md` | Luồng từng bước (`<!-- sc:main … -->`), nhánh ngoại lệ (`<!-- sc:branch … -->`) → trạng thái màn hình và thông điệp; bộ dữ liệu giả lập (D-POST, U-LAN…) | 4, 5, 7 |
| Mô hình dữ liệu | `.agents/.claude/system_analysis/output/data-model/db/DB-Mxx.md`, `DB-SYS.md` (và `cd/CD-Mxx.md`) | Trường trên form và trên màn hình hiển thị, kiểu, độ dài, bắt buộc hay không | 5, 7 |
| Thuật ngữ | `.agents/.claude/system_analysis/output/registers/glossary.md` | Tên gọi hiển thị thống nhất (bài viết, bình luận, sao, huy hiệu…) | 1, 7 |
| Quyết định | `.agents/.claude/system_analysis/output/registers/decisions.md` | Lý do của các giới hạn; kiểm một ý tưởng đã bị loại chưa (ví dụ DEC-169 bỏ Accepted Answer) | Khi cần |
| Danh mục module | `.agents/.claude/system_analysis/output/registers/module-registry.md` | Tóm tắt 16 module, mức ưu tiên, phụ thuộc | 1, 4 |
| Draft của khách hàng | `docs/_temp/*.md` (chỉ đọc) | Bối cảnh, mô tả sản phẩm ban đầu. Không phải nguồn yêu cầu khi đã có FR | 1 |

Quy tắc đọc:

- FR thắng khi nguồn mâu thuẫn (US/SC hiện ở trạng thái "Chờ duyệt"). Mâu thuẫn ảnh hưởng tới giao diện → ghi vào
  "Câu hỏi mở" của `PRODUCT.md` hoặc `screen-inventory.md` và hỏi ở cổng.
- Ghi phiên bản và ngày của từng nguồn đã dùng vào mục "Nguồn" của `PRODUCT.md` (bước 1) để phát hiện khi nguồn đổi.
- Không đọc toàn bộ tài liệu một lần. Mỗi bước nói rõ đọc phần nào.
- Tài liệu dài: dùng `grep` theo các marker `<!-- uc:… -->`, `<!-- sc:… -->` và mã (`UC-Mxx-nnn`, `SC-Mxx-nnn`,
  `FR-Mxx-nn.nn`, `BR-Mxx-nn`).

## 2. Từ người dùng

Toàn bộ câu hỏi, lý do và phương án mặc định nằm ở `QUESTIONS.md`. Tóm tắt những gì người dùng cần chuẩn bị:

| Cần gì | Để làm gì | Trước bước |
|---|---|---|
| Tên, logo, màu có sẵn (nếu có); mong muốn của cô giáo về giao diện | Ràng buộc thương hiệu | 1 |
| 3 từ cảm giác muốn, 3 từ không muốn | Tiêu chí chọn hướng và brand test | 1 |
| Thiết bị học sinh dùng nhiều; có làm dark mode không; xưng hô | Ưu tiên responsive, phạm vi theme, giọng văn | 1 |
| 3–5 app/web thích và 3 cái ghét, kèm lý do (ảnh chụp càng tốt) | Moodboard | 2 |
| Ảnh chụp app học tập học sinh đang dùng (nếu có) | Thói quen người dùng | 2 |
| Chọn hướng thẩm mỹ | Bản sắc | 3 |
| Duyệt phạm vi màn hình và chia đợt | Kế hoạch vẽ | 4 |
| Duyệt font, màu, mật độ, bo góc | Tokens | 6 |
| Dữ liệu mẫu thật: câu hỏi thật, môn, lớp, công thức hay gặp (nếu có) | Nội dung hi-fi | 7 |
| Cấu trúc repo frontend, quy ước đặt tên (nếu đã có) | Bàn giao | 9 |

Ảnh người dùng gửi: lưu vào `.agents/.claude/design/output/moodboard/` với tên `R-nn-<mô-tả>.png`.

## 3. Công cụ

| Công cụ | Trạng thái (11/2026) | Ghi chú |
|---|---|---|
| Claude Design — canvas (type "Design") | Có trong phiên Claude | Định dạng artboard `.dc.html`; xem hướng dẫn của type khi tạo canvas |
| Claude Design — Design System (type "Design System") | Có trong phiên Claude | `tokens.json` dạng danh sách `{"tokens":[{"name","value","usage"}]}`, không phải DTCG |
| Figma MCP | Đã kết nối: tài khoản vduczz, team "vduczz", gói Education (student), seat Full | 200 lượt gọi/ngày, 10/phút. Kiểm lại bằng `whoami` nếu gặp lỗi quyền hoặc giới hạn |
| Python 3 | Có trên máy người dùng | Chạy các tool trong `tools/` |

Thiếu công cụ nào thì báo ngay ở đầu bước cần nó, kèm cách thay thế (xem `SKILL.md` mục "Công cụ thiết kế").
