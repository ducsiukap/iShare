---
ma_tai_lieu: DESIGN
phien_ban: 0.1
trang_thai: Bản nháp
ngay: 2026-11-24
tac_gia: Phạm Văn Đức
steps_completed: [1, 2]
buoc_hien_tai: 3
che_do: kham-pha
dot_da_duyet: []
dot_da_day_figma: []
canvas_kham_pha:
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
| Bước hiện tại | 3 — Hướng thẩm mỹ |
| Hướng thẩm mỹ | (bước 3) |
| Số màn hình / artboard | (bước 4) |
| Đợt đã duyệt | — |

## 2. Hướng thẩm mỹ đã chọn (bước 3)

- **Tên:** <…>
- **Ý tưởng gốc:** <một câu; lấy cảm hứng từ đâu, vì sao hợp PRODUCT.md mục 6>
- **Token plan sơ bộ:** <màu có tên và vai trò; cặp font; thang chữ; ngôn ngữ hình khối; mật độ; bố cục>
- **Điểm nhận diện có chủ đích:** <chi tiết lặp lại nhất quán>
- **Phần trộn từ hướng khác (nếu có):** <…>
- **Lý do chọn:** <…>

Các hướng bị loại:

| Hướng | Lý do loại | Artboard |
|---|---|---|

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

## 8. Đề nghị bổ sung (ngoài nguồn — không vẽ)

| # | Đề nghị | Liên quan | Lý do | Trạng thái |
|---|---|---|---|---|

## 9. Lịch sử thay đổi

| Phiên bản | Ngày | Thay đổi |
|---|---|---|
| 0.1 | 2026-11-24 | Tạo tệp ở bước 1; bước 1 được duyệt (DD-UI-01…04); bước 2 được duyệt (AP-P-01, DD-UI-05…07) |
