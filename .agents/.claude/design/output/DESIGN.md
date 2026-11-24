---
ma_tai_lieu: DESIGN
phien_ban: 0.2
trang_thai: Bản nháp
ngay: 2026-11-24
tac_gia: Phạm Văn Đức
steps_completed: [1, 2, 3]
buoc_hien_tai: 4
che_do: kham-pha
dot_da_duyet: []
dot_da_day_figma: []
canvas_kham_pha: https://claude.ai/artifact/K2ZxJDPyzjGKHCw8rZZKrs
canvas_giao_dien:
design_system:
figma_file:
---
# Thiết kế giao diện — iShare (DESIGN.md)

[Vietnamese Doc] — Trạng thái quy trình (frontmatter) và mọi quyết định thiết kế. Đọc tệp này đầu tiên khi tiếp tục.
`che_do`: `kham-pha` (bước 1–5) hoặc `thuc-thi` (từ cuối bước 6).

## 1. Tóm tắt

| Mục | Giá trị |
|---|---|
| Bước hiện tại | 4 — Danh mục màn hình |
| Hướng thẩm mỹ | "Sổ tay" (DD-UI-08) |
| Số màn hình / artboard | (bước 4) |
| Đợt đã duyệt | — |

## 2. Hướng thẩm mỹ đã chọn (bước 3)

- **Tên:** Sổ tay
- **Ý tưởng gốc:** Trang vở ghi gọn gàng của học sinh: bố cục 3 cột rõ ràng, giữ tinh thần "đơn giản, trực quan" người
  dùng thích ở R-01 nhưng không sao chép (AP-P-01); màu xanh ngọc lá dịu, góc gần vuông như mép giấy. Hợp với cảm xúc
  "gọn gàng, đáng tin, có chất học trò" và tránh "trẻ con, rối, lạnh lùng kiểu công nghệ" (PRODUCT.md mục 6).
- **Token plan sơ bộ** (bước 6 mới chốt):
  - Màu — bộ "Xanh ngọc lá". Sáng: nền `#f5f5f1`, bề mặt `#ffffff`, chữ `#1f2523`, chữ phụ `#5a6360`, kẻ mảnh `#e2e3dd`,
    kẻ đậm/viền ô nhập `#828a86`, chủ đạo `#2a6f63`, chữ trên chủ đạo `#ffffff`, nền nhấn nhạt `#e3efec`. Tối: nền
    `#101514`, bề mặt `#171e1c`, chữ `#e6ece9`, chữ phụ `#a6b2ad`, kẻ mảnh `#2a3431`, kẻ đậm `#6e7c77`, chủ đạo
    `#7cc3b4`, chữ trên chủ đạo `#0c1a17`, nền nhấn nhạt `#1c2b28`. Mọi cặp chính đạt WCAG AA ở cả hai theme.
  - Chữ — một họ Be Vietnam Pro (400/600/700). Thang tạm: 30 tiêu đề bài · 26 tiêu đề trang · 22 tiêu đề mục ·
    19 tiêu đề thẻ bài, ô tiêu đề · 17 nội dung bài (dòng 1.7) · 16 bình luận · 15 giao diện · 14 phụ · 13 ghi chú.
  - Hình khối — bo góc 2px cho khối, nút, ô nhập, chip; ngoại lệ: ô tìm kiếm bo tròn hai đầu, avatar tròn. Viền 1px,
    không đổ bóng.
  - Mật độ — vừa. Bố cục máy tính 1440: thanh trên cùng; lưới 200 (điều hướng) | nội dung | 260 (cột phụ) khi trang có
    nội dung phụ, hoặc 200 | nội dung tối đa 820.
- **Điểm nhận diện có chủ đích:** chữ "iShare" với "Share" màu chủ đạo; Upvote nổi bật trong thanh thao tác trơn chỉ bằng
  màu chủ đạo, chữ đậm và icon nét dày; góc 2px nhất quán, chỉ ô tìm kiếm bo tròn; dòng trích tên và đầu bình luận khi
  trả lời.
- **Phần trộn từ hướng khác:** bộ màu "Xanh ngọc lá", ô tìm kiếm bo tròn và thanh thao tác dưới bài lấy từ hướng 2;
  bo góc 2px lấy từ hướng 3.
- **Lý do chọn:** người dùng chọn ngày 2026-11-24 (Q3-01): lấy thiết kế hướng 1, tùy biến màu, ô tìm kiếm, bo góc theo
  hướng 2 và 3; xem thử trên 4 màn hình (chi tiết bài, trang chủ, hồ sơ, viết bài) rồi duyệt.

Các hướng bị loại:

| Hướng | Lý do loại | Artboard |
|---|---|---|
| Hướng 2 — Bảng tin | Người dùng chỉ lấy bộ màu, ô tìm kiếm và thanh thao tác; không lấy bố cục thẻ và cặp chữ Bricolage Grotesque + Source Sans 3 | `huong-2--chi-tiet-bai--desktop[--dark]` |
| Hướng 3 — Giấy kiểm tra | Người dùng chỉ lấy bo góc 2px; không lấy chữ có chân, bố cục một cột, màu mực xanh + đỏ | `huong-3--chi-tiet-bai--desktop[--dark]` |

Artboard của hướng đã chọn: `huong-4--{chi-tiet-bai,trang-chu,ho-so,viet-bai}--desktop[--dark]` (trang "Hướng đã
chọn — 4 màn hình" trên canvas khám phá).

## 3. Tokens tóm tắt (bước 6)

Nguồn sự thật: `tokens/tokens.json`. Mục này chỉ tóm tắt để đọc nhanh.

- Font: <tiêu đề / thân bài / mono>
- Thang chữ: <…>
- Màu chính: <tên — vai trò>
- Mật độ: <…>
- Bo góc: <…>
- Bóng: <…>
- Chuyển động: <thời lượng, đường cong; nhánh prefers-reduced-motion>
- Bộ icon: <tên, giấy phép, độ dày nét, lưới>

## 4. Component (bước 6)

| Component | Biến thể | Trạng thái | Ghi chú |
|---|---|---|---|

## 5. Quyết định thiết kế

| Mã | Quyết định | Lý do | Nguồn / câu hỏi | Bước | Ngày |
|---|---|---|---|---|---|
| DD-UI-01 | Hỗ trợ hai theme sáng và tối từ MS1; mọi cặp màu kiểm tương phản ở cả hai theme | Người dùng yêu cầu | Q1-04 | 1 | 2026-11-24 |
| DD-UI-02 | Thiết kế cho máy tính: artboard desktop rộng 1440, bố cục co giãn không vỡ ở 1280; chưa vẽ bản điện thoại | Người dùng ưu tiên máy tính; điện thoại chưa cần ở giai đoạn này | Q1-05, Q1-07 | 1 | 2026-11-24 |
| DD-UI-03 | Logo tạm là chữ "iShare" (wordmark), không có biểu tượng riêng | Chưa có nhận diện thương hiệu | Q1-01 | 1 | 2026-11-24 |
| DD-UI-04 | Thuật ngữ hiển thị: giữ "Tag", "Upvote"; Việt hóa "Chủ đề" (Topic), "Huy hiệu" (Badge); bốn tab trang chủ "Thịnh hành / Đang theo dõi / Nhóm / Mới nhất" | Học sinh quen "Tag", "Upvote"; phần còn lại có từ tiếng Việt tự nhiên | PRODUCT.md câu hỏi mở #3 | 1 | 2026-11-24 |
| DD-UI-05 | Gamification (điểm, huy hiệu, Ngôi sao tuần, bảng xếp hạng) trình bày tiết chế: gọn, không màu mè, không mascot | Cảm xúc "không muốn: trẻ con" (PRODUCT.md mục 6) | Q3-02 | 2 | 2026-11-24 |
| DD-UI-06 | Vị trí Upvote: chấp nhận cột trái cạnh nội dung (kiểu R-01) hoặc thanh hành động dưới bài (kiểu R-12); thử cả hai ở bước 3 rồi chốt | Người dùng chấp nhận cả hai | Ý kiến bước 2 | 2 | 2026-11-24 |
| DD-UI-07 | Bước 3: hai hướng dùng hai sắc xanh lá nhẹ khác nhau + một hướng màu khác để đối chứng; thêm một bảng nhiều bộ màu áp lên cùng một mẫu nhỏ để chọn màu độc lập với bố cục | Người dùng thích xanh lá nhẹ; muốn xem thêm vài bộ màu | Ý kiến bước 2 | 2 | 2026-11-24 |
| DD-UI-08 | Hướng thẩm mỹ "Sổ tay": khung hướng 1 (3 cột, Be Vietnam Pro), bộ màu "Xanh ngọc lá" của hướng 2, bo góc 2px của hướng 3 | Người dùng chọn | Q3-01 | 3 | 2026-11-24 |
| DD-UI-09 | Ô tìm kiếm bo tròn hai đầu, rộng tối đa 560px, nằm giữa khoảng từ logo đến nhóm nút bên phải (không căn giữa trang) | Người dùng yêu cầu | Ý kiến bước 3 | 3 | 2026-11-24 |
| DD-UI-10 | Upvote bài viết nằm trong thanh thao tác dưới bài, thứ tự Upvote · Bình luận · Tóm tắt · Lưu, Báo cáo ở cuối thanh. Chốt DD-UI-06 | Người dùng chọn | Ý kiến bước 3 | 3 | 2026-11-24 |
| DD-UI-11 | Upvote là nút trơn như các nút bên cạnh (không viền, không nền), nổi bật bằng màu chủ đạo, chữ đậm, icon nét dày; đã upvote thì icon tô đặc. Upvote bình luận làm cùng cách | Người dùng yêu cầu; trạng thái đã upvote do Claude đề xuất, duyệt cùng bước 3 | Ý kiến bước 3 | 3 | 2026-11-24 |
| DD-UI-12 | Bình luận và trả lời có avatar tròn cạnh tên người viết | Người dùng yêu cầu | Ý kiến bước 3 | 3 | 2026-11-24 |
| DD-UI-13 | Danh sách bài (trang chủ, hồ sơ): thẻ có trích đoạn 2 dòng; số upvote và bình luận chỉ để xem, không bấm upvote tại danh sách. Trang chủ không có cột phụ vì FR-M14 không có nội dung phụ cho trang chủ | Claude đề xuất, duyệt cùng bước 3 | — | 3 | 2026-11-24 |

## 6. Anti-pattern: ngoại lệ và điều cần tránh riêng

### 6.1 Ngoại lệ đã duyệt

`check_ui.py --design` đọc bảng này: cảnh báo của mã AP trong phạm vi tệp khớp `scope` (mẫu glob trên tên tệp; `*` là
mọi tệp) được hạ xuống INFO. Chỉ thêm dòng khi người dùng đã duyệt.

<!-- ui:ap-exceptions -->
| ap | scope | reason | dd |
|---|---|---|---|

### 6.2 Điều cần tránh riêng của dự án (từ bước 2)

<!-- ui:project-avoid -->
| id | avoid | source | reason |
|---|---|---|---|
| AP-P-01 | Sao chép y nguyên hoặc làm giống hệt giao diện của bất kỳ reference nào (bố cục toàn trang, màu, font, icon, logo, khoảng cách đặc trưng); chỉ mượn pattern ghi trong moodboard. Kiểm: đặt cạnh reference, che logo — nhận nhầm là vi phạm | moodboard.md R-01, R-10 và mọi reference | Người dùng cấm tuyệt đối (Q2, 2026-11-24) |

## 7. Dữ liệu mẫu

Dùng chung cho mọi màn hình. Ưu tiên bộ dữ liệu giả lập của SC.

| Mã | Dữ liệu | Nguồn |
|---|---|---|
| MAU-01 | Bài P301 "Giải phương trình bậc hai" — tác giả Phạm Ngọc Lan (@lan_12; hướng 1–3 lỡ ghi @lan_pham), đăng 08/11/2026 08:30, sửa lúc 09:00 ("đã chỉnh sửa" + "Xem lịch sử"); Lớp 10; Chủ đề Toán; Tag #daiso, #phuongtrinh; 24 upvote; 5 bình luận. Nội dung 301 từ (đủ ngưỡng nút Tóm tắt), có công thức trong dòng, một công thức khối, danh sách đánh số 3 câu hỏi | SC-M03 D-POST, D-HISTORY; BR-M03-27; FR-M13-07; độ dài bổ sung ở bước 3 |
| MAU-02 | Tệp đính kèm: bang-bien-thien.png (820 KB), de-cuong-on-tap-hk1.pdf (1,2 MB) | Bổ sung ở bước 3 (tên tệp minh họa) |
| MAU-03 | Bình chọn Q301: "Phương pháp thế" / "Phân tích nhân tử" / "Dùng công thức"; chọn một hoặc nhiều; kết quả hiện sau khi bình chọn; kết thúc 10:00, 09/11/2026 | SC-M03 D-POLL |
| MAU-04 | Bình luận gốc: Trần Minh Đức (12 upvote, có công thức) với 2 trả lời — Phạm Ngọc Lan (nhãn "Tác giả", 3 upvote) và Nguyễn Thị Phương Thảo Nguyên (tên dài, 0 upvote); Hà Thu (7 upvote, đã chỉnh sửa); Lê Văn Bình (2 upvote). Trả lời có dòng trích: tên người được trả lời + đầu bình luận | SC-M04 D-ROOT, D-REPLY; BR-M04-04; tên dài bổ sung ở bước 3 |
| MAU-05 | Người đang xem: Mai Anh (chữ tắt MA) | Bổ sung ở bước 3 |
| MAU-06 | Trang chủ, tab Thịnh hành › Bài viết: 6 bài — P301 (Toán học, Lớp 10, 24 upvote, 5 bình luận); "Phân tích nhân vật Mị: mở bài gián tiếp thế này đã ổn chưa?" (Hà Thu, Ngữ văn, Lớp 12, 19/11); "Đề luyện tập hình học không gian tuần này (có lời giải)" (Trần Minh Đức, trong CLB Toán, Lớp 11, 15/4); "Áp lực ôn thi cuối kỳ…" (Ẩn danh, trong CLB Văn, Kỹ năng mềm, Lớp 12, 13/14); "Mẹo nhớ nhanh tính chất các nhóm A…" (Lê Văn Bình, Khoa học tự nhiên (Lý/Hóa/Sinh), Lớp 10, 12/6); "Viết vòng lặp for trong Python…" (Nguyễn Thị Phương Thảo Nguyên, Tin học, Lớp 11, 8/3) | Tên nhóm CLB Toán, CLB Văn và Chủ đề theo SC-M14 D-DIRECTORY, SC-M05 D-CAT; tiêu đề, trích đoạn, số liệu bổ sung ở bước 3 |
| MAU-07 | Hồ sơ Phạm Ngọc Lan do Mai Anh xem: @lan_12, bio "Thích Toán", Lớp 11, tham gia 01/09/2026, 150 điểm, huy hiệu Người mới nổi (đạt 15/09/2026) và Cây bút triển vọng (đạt 28/10/2026), Ngôi sao tuần, 2 người theo dõi, 2 đang theo dõi; tab Bài viết: P301 và 2 bài bổ sung | SC-M02 D-PROFILE (display_name "Lan" được viết dài thành "Phạm Ngọc Lan"; bỏ emoji 📐 trong bio vì check_ui coi emoji là lỗi); ngày đạt huy hiệu bổ sung |
| MAU-08 | Viết bài: nháp P501 "Vận dụng định lý Bayes" của Lan, Lớp 12, Chủ đề Toán học, Tag #bayes #xácsuất, tệp bayes.pdf (1 MB), chưa có bình chọn; nội dung SC kèm một công thức LaTeX dạng mã và một câu ví dụ | SC-M05 D-POST, D-TAG; công thức và câu ví dụ bổ sung ở bước 3 |

## 8. Đề nghị bổ sung (ngoài nguồn — không vẽ)

| # | Đề nghị | Liên quan | Lý do | Trạng thái |
|---|---|---|---|---|

## 9. Lịch sử thay đổi

| Phiên bản | Ngày | Thay đổi |
|---|---|---|
| 0.1 | 2026-11-24 | Tạo tệp ở bước 1; bước 1 được duyệt (DD-UI-01…04); bước 2 được duyệt (AP-P-01, DD-UI-05…07); bước 3: vẽ 3 hướng + bảng màu + font test trên canvas "iShare — Khám phá", thêm dữ liệu mẫu MAU-01…05; người dùng chọn trộn (khung hướng 1, màu hướng 2, ô tìm kiếm hướng 2, bo góc hướng 3, thanh thao tác hướng 2) — vẽ thử 4 màn hình, dữ liệu MAU-06…08 |
| 0.2 | 2026-11-24 | Bước 3 được duyệt: hướng "Sổ tay" (mục 2, DD-UI-08…13); thêm dữ liệu mẫu MAU-06…08 |
