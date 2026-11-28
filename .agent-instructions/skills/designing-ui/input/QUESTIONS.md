# Ngân hàng câu hỏi cho người dùng

[Vietnamese Doc]

Chỉ hỏi câu của bước đang làm, và chỉ câu nào tài liệu chưa trả lời. Mỗi lượt tối đa khoảng 8 câu. Luôn kèm phương án
đề xuất để người dùng có thể trả lời "ok". Câu trả lời được ghi vào tệp ở cột "Ghi vào"; câu đã có trả lời thì không
hỏi lại.

Cách đặt câu hỏi: một câu một ý, nói vì sao cần, đưa đề xuất và cho phép "chưa biết". Ví dụ:

> **Q1-04 — Dark mode.** Có làm giao diện tối không? Làm thêm thì mọi màu phải kiểm ở hai theme và số artboard tăng
> gần gấp đôi. Đề xuất: **không làm ở MS1**, để token sẵn sàng thêm sau.

## Bước 1 — Brief

| Mã | Câu hỏi | Vì sao cần | Nếu người dùng chưa có / mặc định đề xuất | Ghi vào |
|---|---|---|---|---|
| Q1-01 | Đã có tên hiển thị, logo, màu nhận diện nào chưa (của nhóm, của trường, của cô giáo)? | Ràng buộc thương hiệu, tránh vẽ rồi phải đổi | Dùng chữ "iShare" dạng wordmark tạm, màu do bước 3 chọn | PRODUCT.md mục 7 |
| Q1-02 | Cô giáo (khách hàng) có nói gì về giao diện mong muốn hoặc sản phẩm cô thích không? | Người duyệt cuối có kỳ vọng riêng | Không có; ghi "chưa có ý kiến" | PRODUCT.md mục 7 |
| Q1-03 | 3 từ mô tả cảm giác **muốn** giao diện gợi ra, và 3 từ **không muốn**? | Tiêu chí chọn hướng, brand test | Đề xuất từ brief, ví dụ muốn "gọn, đáng tin, có chất học trò"; không muốn "trẻ con, rối, công nghệ lạnh" | PRODUCT.md mục 6 |
| Q1-04 | Có làm dark mode ở MS1 không? | Gấp đôi việc kiểm màu và artboard | Không làm ở MS1; tokens đặt tên theo vai trò để thêm sau | PRODUCT.md mục 5; DESIGN.md DD-UI |
| Q1-05 | Học sinh dùng điện thoại hay máy tính nhiều hơn? Admin/Mod dùng gì? | Ưu tiên responsive, quyết định màn hình nào bắt buộc có bản mobile | Học sinh: điện thoại trước; Mod/Admin: máy tính | PRODUCT.md mục 3 |
| Q1-06 | Giao diện xưng hô thế nào ("bạn", "mình", không xưng)? Giọng trang trọng hay thân mật? | Giọng văn mọi thông điệp | "Bạn", thân thiện nhưng không suồng sã; thông báo kiểm duyệt trang trọng, tôn trọng | PRODUCT.md mục 5 |
| Q1-07 | Có trình duyệt/thiết bị cấu hình thấp cần hỗ trợ không? | Hạn chế hiệu ứng, ảnh, font nặng | Điện thoại Android tầm trung; hạn chế hiệu ứng và số font tải | PRODUCT.md mục 4 |
| Q1-08 | Có hạn nộp hay mốc review nào ảnh hưởng thứ tự vẽ không? | Chia đợt ở bước 4 | Theo thứ tự ưu tiên trong module-registry | PRODUCT.md mục 4 |

## Bước 2 — Reference

| Mã | Câu hỏi | Vì sao cần | Mặc định | Ghi vào |
|---|---|---|---|---|
| Q2-01 | 3–5 app/web bạn **thích** về giao diện, mỗi cái một dòng lý do (ảnh chụp càng tốt). Không cần là app học tập | Điểm tựa thật thay cho mặc định | Agent đề xuất danh sách để bạn chọn | moodboard.md |
| Q2-02 | 3 app/web bạn **ghét** về giao diện, kèm lý do | Biết phải tránh gì, thành `AP-P-nn` | Không có | moodboard.md; DESIGN.md mục 6 |
| Q2-03 | Học sinh đang dùng app học tập/hỏi đáp nào (ví dụ Hoidap247, OLM, Hocmai, nhóm Facebook)? Có ảnh chụp không? | Thói quen: cách gắn môn/lớp, hiển thị lời giải | Agent tự tìm ảnh công khai và mô tả, không lấy làm reference thẩm mỹ | moodboard.md |
| Q2-04 | Có thể hỏi nhanh 5–10 học sinh của cô (2–3 câu) không? | Kiểm giả định về đối tượng | Không; ghi giả định là chưa kiểm | PRODUCT.md mục 9 |

## Bước 3 — Hướng thẩm mỹ

| Mã | Câu hỏi | Vì sao cần | Mặc định | Ghi vào |
|---|---|---|---|---|
| Q3-01 | Chọn hướng nào (1, 2, 3) hay trộn (ví dụ chữ của hướng 1 với màu của hướng 2)? | Bản sắc | — (bắt buộc người dùng chọn) | DESIGN.md mục 2 |
| Q3-02 | Mức "vui" của gamification: tiết chế (chỉ số và huy hiệu gọn) hay nổi bật? | Ảnh hưởng ngôn ngữ hình ảnh M12 | Tiết chế | DESIGN.md DD-UI |
| Q3-03 | Có muốn xem hướng nào ở thêm một màn hình khác trước khi chọn không? | Giảm rủi ro chọn sai | Không | — |

## Bước 4 — Danh mục màn hình

| Mã | Câu hỏi | Vì sao cần | Mặc định | Ghi vào |
|---|---|---|---|---|
| Q4-01 | Duyệt danh sách màn hình; có màn hình nào để sau MS1 không? | Phạm vi vẽ | Vẽ hết những gì FR/US/SC có | screen-inventory.md |
| Q4-02 | Chia đợt và thứ tự đợt như đề xuất được chưa? | Kế hoạch bước 7 | Đợt A–E theo đề xuất | screen-inventory.md mục 4 |
| Q4-03 | Màn hình quản trị (M10, M15) có cần bản mobile không? | Số artboard | Không | screen-inventory.md |

## Bước 5 — Luồng và wireframe

| Mã | Câu hỏi | Vì sao cần | Mặc định | Ghi vào |
|---|---|---|---|---|
| Q5-01 | Điều hướng chính trên mobile: thanh dưới hay menu? | Khung ứng dụng | Thanh dưới cho 4–5 mục chính | DESIGN.md DD-UI; flows.md |
| Q5-02 | Đường dẫn trang (URL) có quy ước nào nhóm đã định chưa (ngoài `/u/{username}` trong FR-M02)? | Sơ đồ trang | Agent đề xuất theo FR | flows.md mục 1 |

## Bước 6 — Design system

| Mã | Câu hỏi | Vì sao cần | Mặc định | Ghi vào |
|---|---|---|---|---|
| Q6-01 | Font nào (sau khi xem trang test tiếng Việt)? | Giọng và khả năng đọc | Đề xuất từ hướng đã chọn | tokens.json; DESIGN.md |
| Q6-02 | Mật độ: thoáng hay gọn? Có khác nhau giữa màn hình học sinh và màn hình quản trị không? | Khoảng cách, cỡ chữ, chiều cao hàng | Học sinh: vừa; quản trị: gọn | tokens.json; DESIGN.md |
| Q6-03 | Bo góc: vuông vức, vừa hay tròn? | Ngôn ngữ hình khối | Theo hướng đã chọn | tokens.json |
| Q6-04 | Bộ icon (đề xuất 2 lựa chọn kèm ảnh): chọn bộ nào? | Một bộ icon duy nhất | Đề xuất từ hướng | DESIGN.md DD-UI |
| Q6-05 | Danh sách component lõi đã đủ chưa? | Phạm vi design system | Danh sách ở bước 6 | DESIGN.md mục 4 |

## Bước 7 — Hi-fi

| Mã | Câu hỏi | Vì sao cần | Mặc định | Ghi vào |
|---|---|---|---|---|
| Q7-01 | Có câu hỏi/bài thật, môn, lớp, công thức học sinh hay hỏi để làm dữ liệu mẫu không? | Nội dung thật | Dữ liệu giả lập của SC + câu hỏi do agent soạn theo chương trình THPT | DESIGN.md mục 7 |
| Q7-02 | (Đầu mỗi đợt) Có gì cần lưu ý riêng cho đợt này không? | Tránh vẽ lại | Không | qa/QA-dot-X.md |
| Q7-03 | (Đợt đầu tiên đẩy sang Figma) Bản trên Figma có giữ đủ chất lượng để cô/thầy xem không? | Kiểm cách chuyển Claude Design → Figma | — | DESIGN.md DD-UI |

## Bước 9 — Bàn giao

| Mã | Câu hỏi | Vì sao cần | Mặc định | Ghi vào |
|---|---|---|---|---|
| Q9-01 | Repo frontend đã có chưa, cấu trúc thư mục thế nào? Có dùng Tailwind v4 không? | Định dạng xuất tokens | Tailwind v4 + CSS variables; `tokens.css` đặt ở `src/styles/` | handoff/UI-KIT.md |
| Q9-02 | Quy ước đặt tên component (PascalCase, tiền tố)? | Đặc tả UI Kit | PascalCase, không tiền tố | handoff/UI-KIT.md |
