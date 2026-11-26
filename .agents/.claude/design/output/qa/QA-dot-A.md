---
ma_tai_lieu: QA-dot-A
phien_ban: 0.1
trang_thai: Bản nháp
ngay: 2026-11-26
tac_gia: Phạm Văn Đức
---
# Kiểm tra giao diện — Đợt A (Đọc và viết)

[Vietnamese Doc]

## 1. Phạm vi

- Màn hình (11): SCR-SHARED-01, SCR-SHARED-02, SCR-SHARED-04, SCR-M14-01, SCR-M05-01, SCR-M03-02, SCR-M04-01,
  SCR-M13-01, SCR-M03-03, SCR-M03-04, SCR-M03-01.
- Artboard: 59 trạng thái (theme sáng) + 11 bản theme tối cho trạng thái `default` (DD-UI-15) + 1 mục lục
  (`Main.dc.html`). Tổng 71.
- Trang canvas: "Đợt A — Đọc và viết" trong canvas "iShare — Giao diện"
  (https://claude.ai/artifact/HAykztXFcJbkAiSCXKvift#page-dot-a). Bản sao: `canvas/giao-dien/project/`.
- Design system cài vào canvas: `project/ds/ishare/` (tokens.json, tokens.css, components/bundle.css, fonts), bản
  "iShare Design System" 1795613002-b5c9.
- Cách vẽ trạng thái:
  - Trọn trang (cao theo nội dung): trạng thái chính của trang chủ, chi tiết bài, trình soạn, danh sách Chủ đề, lịch sử.
  - Cắt theo khung nhìn 1440 × 900: trạng thái chỉ khác phần đầu trang (chờ duyệt, bị từ chối, menu mở, ngăn tóm tắt…).
  - Cắt vùng (rộng 900): SCR-M04-01 (khu bình luận) và SCR-M03-04 (khối bình chọn), vì cả hai nằm trong SCR-M03-02.

## 2. Kết quả tool

| Tool | Lệnh | Kết quả |
|---|---|---|
| check_ui | `check_ui.py canvas/giao-dien/project --tokens output/tokens/tokens.json --design output/DESIGN.md` | ERROR=0 WARN=0 |
| check_inventory | `check_inventory.py --inventory output/screen-inventory.md --specs docs/specs --artboards canvas/giao-dien/project --batch A` | đủ 59/59; bản tối 11/59 (đúng DD-UI-15) |
| contrast | `contrast.py --tokens output/tokens/tokens.json --pairs output/tokens/contrast-pairs.csv` | 102/102 đạt (token không đổi từ bước 6) |

WARN giữ lại: không có.

## 3. Checklist bằng mắt

Rà trên ảnh chụp bản sao cục bộ (Chromium, 1440 px, font của design system), cả theme sáng và tối.

| Mục | Đạt | Ghi chú |
|---|---|---|
| ANTI-PATTERNS mục 9 (gồm brand test) | Đạt | Một điểm nhấn mỗi màn hình (nút chính màu primary); không gradient, không viền trái dày, không emoji; logo chữ "iShare" |
| QF-04 vùng bấm | Đạt | Nút, icon button cao ≥32 px (control-h-sm) trên desktop; mục danh sách cao 52 px |
| QF-05 focus không bị che | Đạt | Menu, popover, ngăn tóm tắt nằm trên lớp riêng; không có thanh dính che nội dung |
| QF-13 tiếng Việt | Đạt | Dấu đủ ở mọi cỡ chữ; tên dài (Nguyễn Thị Phương Thảo Nguyên, Hoàng Lê Bảo Ngọc Khánh Linh) không bị cắt |
| QF-14 nội dung dài, công thức | Đạt | Tiêu đề 150 ký tự, banner 196 ký tự, bình luận dài, 3 Chủ đề, 5 Tag, 3 tài liệu; công thức hiển thị bằng MathML |
| QF-16 trợ giúp/khiếu nại nhất quán | Đạt | Lối khiếu nại ở menu tài khoản "Khiếu nại của tôi" trên mọi trang có thanh trên cùng |
| Nhất quán với các đợt trước | — | Đợt đầu tiên; bám màn hình mẫu bước 3 và wireframe bước 5 (khác biệt ở mục 4) |

## 4. Lỗi

| Mã | Màn hình | Loại | Mô tả | Đề xuất | Mức | Đã sửa |
|---|---|---|---|---|---|---|
| QA-A-01 | SCR-M03-02 | Nhất quán | Dòng tác giả xuống hàng xấu khi có nhãn "Tài khoản đã bị khóa"; nút "…" rơi xuống dòng riêng | Tách nút "…" khỏi dòng tác giả | Phải sửa | Đã sửa |
| QA-A-02 | SCR-M04-01 | AP | Trả lời nằm dưới dấu "[Bình luận đã bị xóa]" bị in nghiêng, nhạt theo | Chỉ in nghiêng dòng dấu | Phải sửa | Đã sửa |
| QA-A-03 | SCR-M03-02 | Nội dung | Chú thích của ảnh đính kèm nằm dưới tệp PDF | Đặt chú thích ngay dưới ảnh | Phải sửa | Đã sửa |
| QA-A-04 | SCR-M03-01 | Nhất quán | Ô Lớp/Khối dạng nút chọn đoạn (segmented) không vừa cột phải 260 px: "Không chọn" xuống hai dòng | Dùng Select của design system | Phải sửa | Đã sửa — người dùng duyệt 2026-11-26 (DD-UI-38) |
| QA-A-05 | SCR-M03-02 | Nhất quán | Khối bình luận rộng hơn khối bài 16 px | Cùng chiều rộng tối đa content-max | Phải sửa | Đã sửa |
| QA-A-06 | SCR-M03-04 | AP | Số thứ tự lựa chọn lệch cột | Cố định độ rộng cột số | Nên sửa | Đã sửa |
| QA-A-07 | SCR-M03-04, SCR-M03-01 | Nội dung | Ô ngày giờ dùng `datetime-local` nên hiển thị theo ngôn ngữ trình duyệt (trình duyệt tiếng Anh ra MM/DD/YYYY) | Giữ control gốc như DateTimeField của design system; ghi chú cho lập trình | Ghi nhận | Giữ |
| QA-A-08 | SCR-M03-02, SCR-M03-03 | Nguồn | MAU-01 ghi bài sửa lúc 09:00; SC-M03-012 có hai lần sửa (09:00 và 10:00) | Theo SC: "Sửa lần cuối 08/11/2026, 10:00"; cập nhật MAU-01 khi duyệt | Nên sửa | Đã theo SC; MAU-01 đã sửa (DESIGN.md 0.6) |
| QA-A-09 | SCR-SHARED-04 và mọi ErrorState, EmptyState | Nhất quán | Trang lỗi căn trái, khác trang trống căn giữa; nút trong trang trống, trang lỗi có nền đặc | Căn giữa; nút chữ đậm không nền, không viền: màu chủ đạo cho việc chính, màu chữ chính cho việc phụ (DD-UI-36) | Phải sửa | Đã sửa — theo ý kiến duyệt 2026-11-26 |
| QA-A-10 | SCR-M04-01, SCR-M03-01 (và chat SCR-M16-02) | Tương tác | Ô bình luận và vùng soạn bài cao cố định, có tay kéo | Tự giãn theo nội dung tới mức giới hạn rồi cuộn trong ô (DD-UI-37) | Phải sửa | Đã sửa — người dùng duyệt mức giới hạn 2026-11-26 (DD-UI-37) |
| QA-A-11 | Mọi màn hình | Nhất quán | Khung trang, khối, mục lục, danh sách nhãn – giá trị, tiêu đề dựng bằng lớp `pg-*` riêng trong `<helmet>` của artboard | Chuyển thành component của design system (DD-UI-40); so ảnh chụp trước và sau: không đổi giao diện | Nên sửa | Đã sửa — người dùng duyệt 2026-11-26 |
| QA-A-12 | SCR-SHARED-01 và mọi trang có thanh trên cùng | Token | Số đếm trên chuông, Tin nhắn và chữ tắt trong avatar ở thanh trên cùng hiện bằng font mặc định của trình duyệt (IconButton, nút avatar thiếu `font: inherit`); phát hiện khi đẩy sang Figma | Thêm `font: inherit` cho `is-iconbtn`, `is-avbtn` trong design system | Phải sửa | Đã sửa 2026-11-26 |

Thông điệp hệ thống lấy đúng chữ của nguồn: "Hệ thống đang bận, vui lòng thử lại sau", "Nội dung không tồn tại",
"Người dùng không tồn tại", "Tài khoản đã bị khóa", "Không thể gợi ý chủ đề lúc này, vui lòng chọn thủ công",
"Tóm tắt chưa bao gồm nội dung tệp đính kèm", "[Bình luận đã bị xóa]", "trả lời [bình luận đã bị xóa]"; lý do từ chối
"Nội dung cần bổ sung căn cứ" (SC-M03-006); banner "Bảo trì hệ thống lúc 22:00." (D-BANNER, thêm dấu).

Thông điệp nguồn không có chữ cụ thể, viết theo giọng văn `PRODUCT.md` (nói việc gì xảy ra và làm gì tiếp):
tiêu đề quá 150 ký tự, chưa chọn Chủ đề, bình luận quá 1.000 từ, hạn kết thúc trước hiện tại, lựa chọn trống, lưu nháp
lỗi, mức cảnh cáo MEDIUM (trình soạn) và HEAVY (bình luận), bài chờ duyệt, bài tự ẩn, bài đã xóa và hạn khôi phục,
đang kiểm tra bài khi gửi, các trạng thái rỗng, phụ đề trang lỗi.

## 5. Đề xuất token / component mới

Không thêm token. Ba khối dưới đây đã có ở màn hình mẫu bước 3 nhưng chưa thành component trong design system; artboard
đang dựng chúng bằng token (lớp `pg-*` trong `<helmet>`), không dùng giá trị ngoài token.

| Đề xuất | Lý do | Màn hình cần | Quyết định |
|---|---|---|---|
| PageLayout — khung trang: cột điều hướng 200 px, nội dung, cột phụ 260 px (hoặc hai cột, nội dung tối đa 820 px) | Mọi trang đều dùng; nên có tên để lập trình dựng một lần | Mọi màn hình | Đồng ý — đã thêm, 6 biến thể (DD-UI-40) |
| SectionCard — khối nền surface, viền line, bo radius-sm (khu bình luận, khối "Phân loại", "Gửi bài", "Thông tin bài") | Dùng ở chi tiết bài, trình soạn, cột phụ | SCR-M03-01, SCR-M03-02, SCR-M04-01 | Đồng ý — đã thêm (DD-UI-40) |
| TableOfContents — danh sách "Trong bài này", mục đang đọc tô màu primary | Có ở màn hình mẫu bước 3 | SCR-M03-02 | Đồng ý — đã thêm (DD-UI-40) |

## 6. Câu hỏi

| # | Câu hỏi | Trạng thái |
|---|---|---|
| 1 | Ô Lớp/Khối trong trình soạn đổi từ nút chọn đoạn (màn hình mẫu bước 3) sang Select (QA-A-04) — đồng ý? | Đồng ý, 2026-11-26 (DD-UI-38) |
| 2 | Ba khối ở mục 5: đưa vào design system (thêm component) hay giữ là khung trang của artboard? | Đồng ý, 2026-11-26: thêm cả PageHeader, DescriptionList (DD-UI-40) |
| 3 | SCR-M03-01 `pending` được hiểu là lúc vừa bấm Gửi bài, hệ thống đang kiểm tra bài (FR-M03-04.01); bài Chờ duyệt không sửa được (BR-M03-47) nên không có trình soạn cho bài đang chờ duyệt. Đúng ý? | Đồng ý, 2026-11-26 |
| 4 | Thông điệp nguồn không có chữ cụ thể được viết theo giọng văn `PRODUCT.md` (mục 4) — chấp nhận? | Đồng ý, 2026-11-26 |
| 5 | QA-A-08: ghi "Sửa lần cuối 08/11/2026, 10:00" theo SC-M03-012 và sửa dữ liệu mẫu MAU-01 cho khớp? | Đồng ý, 2026-11-26: đã sửa MAU-01 |
