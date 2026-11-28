---
ma_tai_lieu: PRODUCT
phien_ban: 1.0
trang_thai: Đã chốt
ngay: 2026-11-28
tac_gia: Phạm Văn Đức
nhanh: docs/ui-design
---
# Brief sản phẩm — iShare (PRODUCT.md)

[Vietnamese Doc] — "Sự thật bền vững" về sản phẩm cho việc thiết kế giao diện. Không chứa quyết định thị giác (màu,
font, bố cục): những thứ đó nằm ở `DESIGN.md`. Mọi ý có nguồn trong ngoặc: mã tài liệu, "Qx-xx" (người dùng trả lời)
hoặc "giả định". Câu trả lời Q1 của người dùng ngày 2026-11-24.

## 1. iShare là gì

iShare là nền tảng cộng đồng để học sinh THPT chia sẻ, khám phá và thảo luận tri thức, có AI hỗ trợ kiểm duyệt, phân
loại, tìm kiếm ngữ nghĩa và tóm tắt (mô tả dự án; glossary "iShare"; FR-M13 §1.1).

Điều làm iShare khác "một forum có bình luận": bài viết là đơn vị nội dung có chiều sâu (một loại bài dùng cho chia sẻ
kiến thức, hướng dẫn, kinh nghiệm, thảo luận, đánh giá, tài liệu, tin tức; nội dung giàu định dạng có công thức toán —
FR-M03 §1.1); đóng góp được ghi nhận bằng upvote, điểm, huy hiệu và "Ngôi sao tuần" (FR-M12 §1.1); có cộng đồng con
(nhóm, FR-M11), trò chuyện (FR-M16), và quy trình kiểm duyệt – khiếu nại đầy đủ để giữ nội dung phù hợp học sinh
(FR-M08, FR-M09). AI chỉ hỗ trợ; lõi hệ thống chạy đủ khi AI tắt (mô tả dự án; FR-M13).

## 2. Người dùng và vai trò

| Vai trò | Actor | Ai trong thực tế | Việc làm nhiều nhất | Tần suất | Thiết bị chính | Nguồn |
|---|---|---|---|---|---|---|
| Khách | ACT-001 | Người chưa đăng nhập: học sinh mới, người mở link được chia sẻ | Đọc bài công khai, xem trang chủ, tìm kiếm, xem hồ sơ/nhóm công khai | Thỉnh thoảng (giả định) | Máy tính (Q1-05) | US-overview §3; FR-M14 §1.1; FR-M06 §1.1; FR-M02 §1.1 |
| Người dùng | ACT-002 | Chủ yếu học sinh THPT lớp 10–12; giáo viên dùng chung loại tài khoản này (không có tài khoản Giáo viên riêng) | Đọc trang chủ, đặt câu hỏi/chia sẻ bài, bình luận, upvote, tìm kiếm, theo dõi, nhóm, chat | Hằng ngày (giả định) | Máy tính (Q1-05) | FR-M01 §1.1–1.2; FR-M03–M07, M11, M12, M16 |
| Vai trò trong nhóm | ACT-009, ACT-010, ACT-011 | Thành viên, Group Mod, Owner của một nhóm cụ thể | Đăng bài trong nhóm; duyệt thành viên và bài trong nhóm | Theo nhóm | Máy tính (Q1-05) | US-overview §3; FR-M11 |
| Vai trò trong chat | ACT-012, ACT-013, ACT-014 | Thành viên cuộc trò chuyện, Admin nhóm chat, thành viên cũ | Nhắn tin; quản lý nhóm chat | Hằng ngày (giả định) | Máy tính (Q1-05) | US-overview §3; FR-M16 |
| Mod hệ thống | ACT-008 | Người được Admin đề xuất làm Mod | Xử lý hàng chờ báo cáo, duyệt bài chờ đăng, cảnh cáo/ban, giải quyết khiếu nại | Hằng ngày khi có báo cáo (giả định) | Máy tính (Q1-05) | FR-M08, FR-M09; FR-M03-06 |
| Admin hệ thống | ACT-007 | Người vận hành (nhóm phát triển, có thể cả cô giáo) | Vai trò, cấu hình hệ thống, banner, danh mục Topic, thống kê | Theo nhu cầu | Máy tính (Q1-05) | FR-M10, FR-M05, FR-M15 |

Vai trò kế thừa: Admin → Mod → Người dùng; Owner → Group Mod → Thành viên → Người dùng (US-overview §3). Admin hệ thống
không mặc nhiên xem được nhóm Private hay chat (US-overview §3).

## 3. Bối cảnh dùng

- Thiết bị: **máy tính** (trình duyệt trên laptop/PC) cho mọi vai trò. Giai đoạn này chưa thiết kế cho điện thoại
  (Q1-05, Q1-07).
- Lúc nào, ở đâu (giả định): học sinh đọc và hỏi bài buổi tối khi tự học ở nhà, soạn bài dài có công thức; Mod/Admin
  làm việc theo phiên trên máy tính.
- Thiết bị yếu: không cần tối ưu riêng cho điện thoại tầm trung (Q1-07).
- Thói quen từ app khác: học sinh quen mạng xã hội (Facebook, nhóm lớp), các trang hỏi đáp bài tập (giả định; bước 2 sẽ
  thu thập từ người dùng — Q2-03).

## 4. Việc chính (top jobs)

| # | Việc | Ai | UC | Màn hình phải làm tốt điều gì |
|---|---|---|---|---|
| 1 | Đọc và khám phá bài qua trang chủ 4 tab (Trending, Following, Group, Newest) và trang chi tiết bài | Khách, Người dùng | UC-M14-020 … 023, UC-M03-021, UC-M13-023 | Lướt nhanh nhiều bài; đọc bài dài có công thức, bảng, code không vỡ bố cục |
| 2 | Đặt câu hỏi / chia sẻ bài: nội dung giàu định dạng có công thức, tệp đính kèm, bình chọn, Lớp/Khối, Topic, Tag; theo dõi trạng thái bài (chờ duyệt, bị từ chối…) | Người dùng | UC-M03-020, UC-M03-022, UC-M05-023 | Viết công thức dễ, xem trước được; luôn biết bài đang ở trạng thái nào và vì sao |
| 3 | Thảo luận và ghi nhận: bình luận hai cấp, trả lời, trích dẫn, nhắc tên, upvote; xem điểm, huy hiệu, bảng xếp hạng | Người dùng | UC-M04-020, UC-M04-030, UC-M12-020, UC-M12-021 | Luồng bình luận dễ theo; upvote một chạm; thành tích hiển thị tiết chế |
| 4 | Tìm bài, người, Topic, Tag, nhóm | Khách, Người dùng | UC-M06-020, UC-M05-021 | Tìm được cả khi gõ không dấu; lọc theo Topic/Tag/thời gian |
| 5 | Kết nối cộng đồng: theo dõi, thông báo, nhóm, chat | Người dùng | UC-M07-020, UC-M07-021, UC-M11-030 … 033, UC-M16-030 … 033 | Biết ngay có gì mới; vào nhóm, vào cuộc trò chuyện nhanh |
| 6 | Giữ cộng đồng an toàn: báo cáo, kiểm duyệt, cảnh cáo/ban, khiếu nại | Người dùng, Mod, Admin | UC-M08-020 … 025, UC-M09-020, UC-M09-021, UC-M11-034 | Mod xử lý nhanh từ hàng chờ; người bị xử lý hiểu lý do và biết cách khiếu nại |
| 7 | Vận hành: vai trò, cấu hình, banner toàn trang, danh mục Topic, thống kê | Admin | UC-M10-020 … 023, UC-M05-022, UC-M15-020 … 022 | Thao tác cấu hình rõ hậu quả; số liệu đọc nhanh |

## 5. Ràng buộc

| Loại | Ràng buộc | Nguồn |
|---|---|---|
| Kỹ thuật | Ứng dụng web React dạng SPA (Vite); không SSR/SEO ở MS1 | Quyết định stack của nhóm; FR-M06 §1.2 (SEO/SSR hoãn) |
| Kỹ thuật | Nội dung bài giàu định dạng, công thức LaTeX viết dạng mã thô và được hiển thị; không có trình soạn LaTeX trực quan; bình luận dùng trình soạn tối giản (có công thức, trích dẫn) | FR-M03 §1.1–1.2; SC-M03 (M2); FR-M04 §1.1 |
| Kỹ thuật | Ảnh và tài liệu chỉ qua phần đính kèm dưới bài; không chèn ảnh trong nội dung; bình luận không có đính kèm | FR-M03 §1.2, BR-M03-50; FR-M04 §1.2 |
| AI | AI chỉ hỗ trợ, có công tắc tổng và theo module; khi AI tắt vẫn tìm được bằng từ khóa (kể cả không dấu), không có gợi ý Topic, không có tóm tắt → mọi màn hình phải dùng được khi AI tắt | FR-M10 §1.1–1.2; FR-M13 §1.1; FR-M06 §1.1 |
| Vận hành | Admin có thể bật chế độ bảo trì, tạm dừng đăng ký, banner toàn trang, và **tắt Group, Chat, Gamification** bằng cờ tính năng → giao diện phải có trạng thái khi các phần này tắt | FR-M10 §1.2 |
| Đối tượng | Người dùng là học sinh (vị thành niên): kiểm duyệt nội dung; ẩn danh khi nhóm cho phép; đăng ký bằng cam kết trong ô đồng ý (không hỏi tuổi, không xác nhận phụ huynh ở MS1) | FR-M08 §1.1; FR-M11; FR-M01 §1.2 |
| Ngôn ngữ | Giao diện tiếng Việt | Bối cảnh dự án |
| Phạm vi MS1 không có | Accepted Answer; ảnh bìa; chèn ảnh trong bài; nhiều loại bài; downvote; đếm lượt xem; tìm bình luận; email tổng hợp và trang cài đặt thông báo theo loại; tab "For You"; theo dõi nhóm/Tag/bài; gửi tệp, ảnh, gọi thoại/video, sửa tin nhắn trong chat; xuất CSV và khoảng thời gian tùy ý trong thống kê; phân biệt tài khoản Giáo viên/Học sinh | FR-M03, M04, M05, M06, M07, M11, M12, M14, M15, M16, M01 §1.2 |
| Thiết kế giao diện | Mục "Yêu cầu HMI" của cả 16 FR đều ghi "Chưa có — chờ giai đoạn thiết kế": thiết kế này sẽ là nguồn để bổ sung mục đó (đề nghị cập nhật FR sau khi chốt, theo quy trình System Analysis) | FR-M01 … M16 §5 "Yêu cầu HMI" |
| Theme | Hỗ trợ hai theme **sáng và tối** từ MS1 | Q1-04 |
| Thiết bị | Chỉ máy tính ở giai đoạn này; chưa thiết kế bản điện thoại | Q1-05, Q1-07 |
| Mốc thời gian | Không có mốc riêng; thứ tự vẽ theo mức ưu tiên module | Q1-08 (mặc định) |

## 6. Cảm xúc

Người dùng đồng ý (Q1-03):

| Muốn | Nghĩa trong iShare | | Không muốn | Nghĩa trong iShare |
|---|---|---|---|---|
| Gọn gàng | Đọc bài và bình luận không bị nhiễu; mỗi màn hình rõ việc chính | | Trẻ con | Màu kẹo, mascot, emoji, huy hiệu lòe loẹt — học sinh 15–18 tuổi thấy bị coi thường |
| Đáng tin | Nội dung học tập nghiêm túc; kiểm duyệt minh bạch, có lý do | | Rối | Nhiều khung, nhiều nút, nhiều màu tranh nhau sự chú ý |
| Có chất học trò | Gần gũi đời sống lớp học Việt Nam, không phải công cụ doanh nghiệp | | Lạnh lùng kiểu công nghệ | Giao diện SaaS chung chung, tối và neon, không có giọng riêng |

## 7. Thương hiệu có sẵn

- Tên hiển thị: iShare (glossary). Chưa có logo và màu nhận diện; dùng chữ "iShare" làm logo (wordmark) (Q1-01).
- Màu người dùng thích: **xanh lá cây, nhưng sắc độ nhẹ nhàng** — không dùng xanh lá gắt, bão hòa mạnh (Q1-01). Đây là
  sở thích để bước 3 cân nhắc, chưa phải quyết định màu.
- Ý kiến của khách hàng (cô giáo): chưa có (Q1-02).

## 8. Giọng văn

- Xưng hô: gọi người dùng là "bạn"; hệ thống không xưng ngôi thứ nhất (Q1-06).
- Mức trang trọng: thân thiện, ngắn, rõ; không suồng sã, không dùng tiếng lóng.
- Thông báo lỗi: nói chuyện gì xảy ra + làm gì tiếp. Ví dụ: "Chưa tải được bài viết. Kiểm tra kết nối rồi thử lại."
- Thông báo kiểm duyệt (cảnh cáo, ẩn, khóa, ban): tôn trọng, nêu lý do cụ thể và thời hạn, chỉ đường khiếu nại khi được
  phép (FR-M09 §1.1: mỗi xử lý chỉ khiếu nại một lần, có thời hạn). Ví dụ khung: "Bài viết của bạn đã bị ẩn vì ⟨lý do⟩.
  Nếu bạn cho rằng quyết định chưa đúng, bạn có thể khiếu nại trước ⟨hạn⟩."
- Thuật ngữ hiển thị (câu hỏi mở #3, DD-UI-04): bài viết, bình luận, **Chủ đề** (Topic), **Tag**, Lớp/Khối, nhóm,
  **Upvote**, điểm, **Huy hiệu** (Badge), "Ngôi sao tuần", cảnh cáo, ban, khiếu nại; bốn tab trang chủ: **Thịnh hành /
  Đang theo dõi / Nhóm / Mới nhất**. Tài liệu kỹ thuật vẫn dùng thuật ngữ của FR.
- Không dùng: câu sáo rỗng (AP-51), giọng quảng cáo (AP-54), emoji trong giao diện (AP-40).

## 9. Thước đo thành công của giao diện

Đề xuất; chưa kiểm với người dùng thật (Q2-04).

| # | Tiêu chí kiểm được | Giả định đã kiểm với người dùng thật? |
|---|---|---|
| 1 | Học sinh đặt được một câu hỏi có công thức và xem trước công thức trước khi gửi, không phải rời trình soạn | Chưa |
| 2 | Từ trang chủ mở một bài và đọc hết nội dung + bình luận; công thức, bảng, code không làm vỡ bố cục ở bề rộng laptop nhỏ (1280px) | Chưa |
| 3 | Người bị cảnh cáo hoặc bị ẩn bài hiểu lý do và tới được nút khiếu nại trong một bước từ thông báo | Chưa |
| 4 | Mod xử lý xong một báo cáo (xem nội dung, ra quyết định) mà không phải rời hàng chờ | Chưa |
| 5 | Ứng dụng vẫn dùng được trọn vẹn khi AI tắt hoặc khi Group, Chat, Gamification bị tắt | Chưa |
| 6 | Mọi màn hình đọc tốt và đạt tương phản ở cả theme sáng và tối | Chưa |

## 10. Nguồn

| Tài liệu | Phiên bản / ngày | Trạng thái |
|---|---|---|
| docs/specs/fr/FR-M01.md | 1.10 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M02.md | 1.6 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M03.md | 1.10 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M04.md | 1.4 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M05.md | 1.7 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M06.md | 1.5 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M07.md | 1.5 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M08.md | 1.7 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M09.md | 1.2 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M10.md | 1.4 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M11.md | 1.3 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M12.md | 1.1 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M13.md | 1.3 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M14.md | 1.1 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M15.md | 1.1 / 2026-10-24 | Đã chốt |
| docs/specs/fr/FR-M16.md | 1.0 / 2026-10-24 | Đã chốt |
| docs/specs/us/US-overview.md | 2026-11-02 | Chờ duyệt |
| docs/specs/us/US-M01 … US-M16 | 2026-10-29 … 2026-11-02 | Chờ duyệt |
| docs/specs/scenarios/Mxx/SC-M01 … SC-M16 | 2026-11-11 | Đang soạn |
| .agents/.claude/system_analysis/output/registers/glossary.md | — | Register |
| docs/_temp/iShare_specs_general.md | — | Draft (chỉ đọc) |

## 11. Câu hỏi mở

| # | Câu hỏi | Ảnh hưởng | Trạng thái |
|---|---|---|---|
| 1 | Glossary (register) vẫn ghi Comment "được chấp nhận làm câu trả lời" (Accepted Answer), còn FR-M04/BR-M04-11 và DEC-169 nói MS1 không có. Thiết kế theo FR (không vẽ Accepted Answer). Đề nghị cập nhật glossary theo quy trình System Analysis | Không vẽ nhầm tính năng | Theo FR — chỉ báo |
| 2 | US đang "Chờ duyệt", SC đang "Đang soạn". Thiết kế dựa trên bản hiện tại; khi các tài liệu này đổi, `check_inventory.py` sẽ báo màn hình bị ảnh hưởng | Có thể phải vẽ lại một phần | Đã trả lời: người dùng xác nhận bản US/SC hiện tại là bản cuối (2026-11-24) |
| 3 | Thuật ngữ tiếng Anh trên giao diện: "Upvote", "Topic", "Tag", "Badge", "Trending/Following/Group/Newest" — giữ nguyên hay Việt hóa (ví dụ "Chủ đề", "Thẻ", "Huy hiệu", "Thịnh hành / Đang theo dõi / Nhóm / Mới nhất")? | Nhãn trên mọi màn hình | Đã trả lời: đồng ý đề xuất (DD-UI-04) |
| 4 | Dark mode cho mọi màn hình: vẽ bản tối cho toàn bộ artboard hay chỉ các màn hình đại diện (tokens vẫn kiểm tương phản đủ hai theme)? | Số artboard gần gấp đôi | Đã trả lời ở bước 4 (2026-11-25): bản tối cho trạng thái default của mỗi màn hình; các trạng thái khác soát tự động ở bước 8 (DD-UI-15) |
