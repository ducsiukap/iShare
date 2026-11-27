---
ma_tai_lieu: QA-final
phien_ban: 0.2
trang_thai: Chờ duyệt lần 2
ngay: 2026-11-27
tac_gia: Phạm Văn Đức
---
# Kiểm tra giao diện — Toàn bộ

[Vietnamese Doc]

## 1. Phạm vi

- Màn hình: 75 màn hình của 5 đợt (A 11, B 4, C 27, D 20, E 13) theo `screen-inventory.md`; 281 artboard sáng bắt buộc,
  356 artboard tính cả bản tối; trang canvas: https://claude.ai/artifact/HAykztXFcJbkAiSCXKvift (bản 1795712646-d582,
  sau DD-UI-43); sau khi sửa: bản 1795739150-e412.
- Cách soát: chạy 3 tool trên toàn bộ; dựng mọi artboard bằng Chromium ở bề rộng 1440 và 1280 để đo vùng bấm, chữ bị cắt,
  chữ ngắn xuống dòng, phần tử tràn khung, cuộn ngang, thứ tự heading, landmark; xem ảnh chụp các chỗ bị báo; brand test
  trên 6 màn hình của 5 đợt; đối chiếu nguồn bằng mẫu.

## 2. Kết quả tool

| Tool | Lệnh | Kết quả |
|---|---|---|
| check_ui | `check_ui.py canvas/giao-dien/project --tokens … --design …` | 359 tệp, ERROR=0 WARN=0 |
| check_inventory | `check_inventory.py … --artboards canvas/giao-dien/project --require-artboards` | 281/281 artboard; ERROR=0 WARN=0 INFO=1 (bản tối 75/281, đúng phạm vi bản tối đã chốt) |
| contrast | `contrast.py --tokens … --pairs …` | 116/116 đạt, 0 thiếu token |

Spec trong `docs/specs` không đổi từ 2026-11-11 (trước bước 4), nên không có màn hình bị ảnh hưởng do FR/US/SC đổi.

Chạy lại sau khi sửa (2026-11-27): check_ui 359 tệp ERROR=0 WARN=0; check_inventory 281/281 ERROR=0 WARN=0 INFO=1; contrast 116/116.
Soát DOM lại ở 1440 và 1280: không còn cuộn ngang, không còn phần tử tràn khung, không còn heading nhảy cấp; số thành viên và ngày giờ không còn tách dòng.
Còn lại, chấp nhận: 6 vùng bấm nhỏ nằm ở trang nền phía sau dialog (SCR-M05-05, SCR-M08-01); SCR-M03-04 và SCR-M04-01 là artboard cắt một phần trang (không có `h1`, `main` của trang đầy đủ).

WARN giữ lại: không có.

## 3. Checklist bằng mắt

| Mục | Đạt | Ghi chú |
|---|---|---|
| ANTI-PATTERNS mục 9 (gồm brand test) | Đạt | Brand test trên SCR-M06-01, SCR-M02-01, SCR-M11-03, SCR-M15-01, SCR-M16-01 (tối), SCR-M01-04: cùng một bảng màu xanh ngọc lá, chữ logo, góc gần vuông, một điểm nhấn mỗi màn; không có mẫu AP-P-01 |
| QF-04 vùng bấm | Đạt | 852 phần tử dưới 24px (tên tác giả, link phụ, nút gỡ Tag 20px…) đều đạt ngoại lệ khoảng cách của WCAG 2.5.8; 6 trường hợp bị báo nằm ở trang nền phía sau dialog (không bấm được khi dialog mở) |
| QF-05 focus không bị che | Đạt | Thanh trên cùng và thanh soạn không dính trong thiết kế. Ghi chú bàn giao: nếu khi code cho thanh trên cùng dính thì thêm `scroll-padding-top: var(--topbar-h)` |
| QF-09 đăng nhập, mật khẩu | Không đạt | QA-F-04 |
| QF-12 không cuộn ngang ở 1280px | Không đạt | QA-F-02 (1 artboard) |
| QF-13 tiếng Việt | Đạt | Không có chữ bị cắt dấu; chỉ các nhãn ẩn cho trình đọc màn hình (`is-sr`) và đoạn trích 2 dòng của PostCard (cố ý) bị cắt theo chiều dọc |
| QF-14 nội dung dài, công thức | Không đạt | QA-F-01, QA-F-02, QA-F-03 |
| QF-16 trợ giúp/khiếu nại nhất quán | Một phần | Báo cáo: nút trên ActionBar của bài, trong menu "…" của bình luận, hồ sơ, nhóm (chat không báo cáo được ở MS1, đúng FR-M08). Màn hình bị ban dẫn sang M09-01. Thiếu đường sang khiếu nại ở màn hình bị cảnh cáo: QA-F-08 |
| QF-17 tiêu đề, landmark | Không đạt | QA-F-05, QA-F-06, QA-F-07 |
| Nhất quán với các đợt trước | Đạt | 52 nhãn trạng thái, mỗi chữ chỉ dùng một biến thể StatusLabel; nút "Thử lại" theo đúng component chứa nó (Toast, EmptyState, ErrorState, InlineAlert); nút Hủy, Lưu thay đổi, Gửi báo cáo cùng biến thể ở mọi đợt |
| Đối chiếu nguồn (mẫu) | Đạt | SCR-M10-02, SCR-M11-08, SCR-M13-01, SCR-M15-01, SCR-M07-03 so với FR-M10, FR-M11, FR-M13, FR-M15, FR-M07: không có phần tử ngoài nguồn; các màn khác đã đối chiếu ở QA từng đợt |

## 4. Lỗi

| Mã | Màn hình | Loại (AP / QF / Nhất quán / Nguồn / Nội dung) | Mô tả | Đề xuất | Mức | Đã sửa |
|---|---|---|---|---|---|---|
| QA-F-01 | SCR-M11-01 (default, default tối, guest) | QF | Chân GroupCard: "128 thành viên" xuống 2 dòng; ở guest "12 thành viên", "46 thành viên" xuống 3 dòng và nút "Đăng nhập để tham gia" tràn khỏi mép thẻ 19px | Số thành viên không ngắt dòng; chân thẻ cho nút xuống hàng dưới khi thiếu chỗ (GroupCard trong design system) | Phải sửa | Có |
| QA-F-02 | SCR-M03-01 (long) | QF | Thẻ Chủ đề "Khoa học tự nhiên (Lý/Hóa/Sinh)" rộng hơn ô TagInput, tràn 62px, làm cả trang cuộn ngang 9px ở 1440 và 1280 | Thẻ trong TagInput tối đa bằng bề rộng ô, chữ dài xuống dòng trong thẻ | Phải sửa | Có |
| QA-F-03 | SCR-M16-01…M16-04, SCR-M16-06 (23 artboard có danh sách cuộc trò chuyện) | QF | ConversationItem: dòng tin nhắn cuối chạy vào dưới số tin chưa đọc (tràn 28px) | Dòng tin nhắn cuối một dòng, cắt bằng dấu "…", chừa chỗ cho số chưa đọc | Phải sửa | Có |
| QA-F-04 | SCR-M01-01, SCR-M01-04, SCR-M01-06, SCR-M01-07 (18 artboard) | QF | Ô mật khẩu không có nút Hiện/Ẩn mật khẩu, ô mật khẩu và email không có `autocomplete`; design system đã có biến thể mật khẩu của TextField | Dùng biến thể mật khẩu của TextField: nút icon "Hiện mật khẩu", `autocomplete` `current-password` / `new-password` / `email` | Phải sửa | Có |
| QA-F-05 | 34 màn hình, 102 artboard (Bảng tin, hồ sơ, nhóm, thông báo, thống kê, hàng chờ…) | QF | Heading nhảy từ h1 xuống h3: tiêu đề PostCard, GroupCard, biểu đồ… là h3 nằm ngay dưới h1 của trang | Thêm h2 cho vùng danh sách (hiện hoặc chỉ cho trình đọc màn hình), hoặc cho component nhận cấp heading theo ngữ cảnh | Nên sửa | Có |
| QA-F-06 | SCR-M01-01…M01-06, SCR-M01-08, SCR-M01-10, SCR-SHARED-03, SCR-SHARED-05 (35 artboard) | QF | Trang đăng ký, đăng nhập, đặt lại mật khẩu, trang bảo trì, trang tài khoản bị khóa có `header` nhưng không có `main` | Bọc khối nội dung giữa trang bằng `main` | Nên sửa | Có |
| QA-F-07 | SCR-M02-01 (loading), SCR-M03-02 (loading), SCR-M09-01 (submitted) | QF | Không có h1: tiêu đề bị thay bằng khối đang tải hoặc khung gửi thành công | Giữ h1 của trang (hiện, hoặc chỉ cho trình đọc màn hình khi đang tải) | Nên sửa | Có |
| QA-F-08 | SCR-M03-01 (warned), SCR-M04-01 (warned) | QF | Thông báo cảnh cáo nói rõ hạn chế nhưng không chỉ đường sang Khiếu nại; cảnh cáo khiếu nại được (FR-M09), đường dẫn khiếu nại hiện chỉ có trong thông báo cảnh cáo (FR-M08-09.05, FR-M08-10.03) | Thêm link "Khiếu nại cảnh cáo này" trong InlineAlert, mở cùng biểu mẫu SCR-M09-01 mà thông báo cảnh cáo dẫn tới | Nên sửa | Có |
| QA-F-09 | SCR-M03-02 (cột Thông tin bài), SCR-M08-03 (cột Tác giả) | Nội dung | Danh sách mô tả trong cột phải hẹp tách ngày và giờ ra hai dòng ("08/11/2026, / 08:30"), tách tên và username | Giữ ngày giờ liền một cụm; thu hẹp cột nhãn để cột giá trị rộng hơn | Nên sửa | Có |
| QA-F-10 | SCR-M11-01 (guest) | Nguồn | Tìm thấy khi đẩy lại Figma: Guest thấy nhãn "Đã tham gia" ở thẻ CLB Toán và phụ đề "nhóm Private bạn đã tham gia"; Guest chỉ xem nhóm Public, không tham gia nhóm (FR-M11, vai trò Guest) | Cả ba thẻ dùng "Đăng nhập để tham gia"; phụ đề "Nhóm Public · nhóm tạo sau đứng trước" | Phải sửa | Có |

## 5. Đề xuất token / component mới

| Đề xuất | Lý do | Màn hình cần | Quyết định |
|---|---|---|---|
| Không có token mới. Sửa trong component có sẵn: GroupCard (QA-F-01), TagInput (QA-F-02), ConversationItem (QA-F-03, thêm `is-convo__main`); PostCard, GroupCard, EmptyState, TrendChart lấy cấp tiêu đề theo ngữ cảnh (QA-F-05); DescriptionList thêm biến thể `is-dl--stack` (QA-F-09) | Lỗi nằm ở component dùng chung, sửa một lần áp cho mọi màn | Như bảng lỗi | Người dùng đồng ý sửa tất cả, 2026-11-27 |

## 6. Câu hỏi

| # | Câu hỏi | Trạng thái |
|---|---|---|
| 1 | QA-F-08 thêm một lối vào biểu mẫu khiếu nại có sẵn (ngoài thông báo cảnh cáo). Đồng ý thêm, hay giữ đúng một lối vào như FR? | Đồng ý bổ sung, 2026-11-27 (DD-UI-44) |
