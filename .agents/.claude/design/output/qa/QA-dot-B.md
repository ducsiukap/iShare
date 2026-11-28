---
ma_tai_lieu: QA-dot-B
phien_ban: 0.1
trang_thai: Bản nháp
ngay: 2026-11-26
tac_gia: Phạm Văn Đức
---
# Kiểm tra giao diện — Đợt B (Con người)

[Vietnamese Doc]

## 1. Phạm vi

- Màn hình (4): SCR-M02-01, SCR-M02-02, SCR-M02-03, SCR-M12-01.
- Artboard: 22 trạng thái (theme sáng) + 4 bản theme tối cho trạng thái `default` (DD-UI-15). Tổng 26.
- Trang canvas: "Đợt B — Con người" trong canvas "iShare — Giao diện"
  (https://claude.ai/artifact/HAykztXFcJbkAiSCXKvift#page-dot-b). Bản sao: `canvas/giao-dien/project/`.
- Design system: giống đợt A (`project/ds/ishare/`, bản "iShare Design System" 1795613002-b5c9).
- Cách vẽ trạng thái: trọn trang cho hồ sơ (chủ hồ sơ, người xem), sửa hồ sơ và bảng xếp hạng; cắt 1440 × 900 cho trạng thái chỉ khác phần đầu trang (đang tải, lỗi, hồ sơ bị khóa); hộp thoại người theo dõi (SCR-M02-02) vẽ trên nền trang hồ sơ.

## 2. Kết quả tool

| Tool | Lệnh | Kết quả |
|---|---|---|
| check_ui | `check_ui.py canvas/giao-dien/project --tokens output/tokens/tokens.json --design output/DESIGN.md` | ERROR=0 WARN=0 (cả canvas, 359 tệp) |
| check_inventory | `check_inventory.py --inventory output/screen-inventory.md --specs docs/specs --artboards canvas/giao-dien/project --batch B` | đủ 22/22; bản tối 4/22 (đúng DD-UI-15) |
| contrast | `contrast.py --tokens output/tokens/tokens.json --pairs output/tokens/contrast-pairs.csv` | 102/102 đạt (token không đổi từ bước 6) |

WARN giữ lại: không có.

## 3. Checklist bằng mắt

Rà trên ảnh chụp bản sao cục bộ (Chromium, 1440 px, font của design system), cả theme sáng và tối.

| Mục | Đạt | Ghi chú |
|---|---|---|
| ANTI-PATTERNS mục 9 (gồm brand test) | Đạt | Một điểm nhấn mỗi màn hình (Theo dõi hoặc Lưu thay đổi); huy hiệu dùng nhãn trung tính, không màu riêng; không emoji |
| QF-04 vùng bấm | Đạt | Nút, icon button cao ≥32 px (control-h-sm); hàng bảng, mục danh sách cao ≥44 px |
| QF-05 focus không bị che | Đạt | Hộp thoại người theo dõi nằm trên lớp riêng, có scrim; tab trong hộp thoại không bị che |
| QF-13 tiếng Việt | Đạt | Tên dài trong bảng xếp hạng và danh sách người theo dõi xuống dòng đủ dấu, không bị cắt |
| QF-14 nội dung dài | Đạt | Bio 155 ký tự, 5 huy hiệu, bảng xếp hạng có hạng bằng nhau (hai hạng 2), người chưa đặt Lớp |
| QF-16 trợ giúp/khiếu nại nhất quán | Đạt | Menu tài khoản giữ "Khiếu nại của tôi" như đợt A |
| Nhất quán với các đợt trước | Đạt | Cùng khung trang, thẻ bài, ô nhập với đợt A |

## 4. Lỗi

| Mã | Màn hình | Loại | Mô tả | Đề xuất | Mức | Đã sửa |
|---|---|---|---|---|---|---|
| QA-B-01 | SCR-M02-03 | Nhất quán | Tiền tố "@" đặt trong ô Username chồng lên chữ đang nhập | Bỏ tiền tố trong ô; gợi ý dưới ô ghi đường dẫn hồ sơ /u/… | Phải sửa | Đã sửa |
| QA-B-02 | SCR-M02-02 | Nội dung | Ngày bắt đầu theo dõi làm dòng phụ bị cắt bằng "…" | Bỏ ngày (nguồn không yêu cầu hiện) | Nên sửa | Đã sửa |
| QA-B-03 | SCR-M02-03 | Nguồn | Gợi ý và lỗi của ô Username ghi "chữ thường a–z"; FR-M01-03.05 cho phép cả A–Z và FR-M01-03.11 giữ nguyên hoa, thường | Sửa thành "chữ cái không dấu, chữ số và dấu _" (giống SCR-M01-03) | Phải sửa | Đã sửa (phát hiện khi rà gộp) |
| QA-B-04 | SCR-M02-01, SCR-M12-01 | Nguồn | Tên huy hiệu chỉ lấy từ nguồn (Người mới nổi, Cây bút triển vọng, Cây bút tích cực, Chuyên gia cộng đồng, Huyền thoại iShare), không đặt thêm tên | — | Ghi nhận | Giữ |

Thông điệp nguồn có chữ cụ thể được dùng nguyên văn: "Người dùng không tồn tại", "Tài khoản đã bị khóa", "Hệ thống đang bận, vui lòng thử lại sau". Phần còn lại (lỗi kiểm tra trường, trạng thái rỗng của tab Bài viết, Bình luận, Đã lưu) viết theo giọng văn `PRODUCT.md`.

## 5. Đề xuất token / component mới

Không thêm token, không thêm component.

## 6. Câu hỏi

| # | Câu hỏi | Trạng thái |
|---|---|---|
| — | Không có câu hỏi mới | — |
