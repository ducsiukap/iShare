---
ma_tai_lieu: QA-dot-D
phien_ban: 0.1
trang_thai: Bản nháp
ngay: 2026-11-26
tac_gia: Phạm Văn Đức
---
# Kiểm tra giao diện — Đợt D (Cộng đồng và liên lạc)

[Vietnamese Doc]

## 1. Phạm vi

- Màn hình (20): SCR-M07-01, SCR-M07-02, SCR-M07-03, SCR-M11-01, SCR-M11-02, SCR-M11-03, SCR-M11-04, SCR-M11-05, SCR-M11-06, SCR-M11-07, SCR-M11-08, SCR-M11-09, SCR-M11-10, SCR-M11-11, SCR-M16-01, SCR-M16-02, SCR-M16-03, SCR-M16-04, SCR-M16-05, SCR-M16-06.
- Artboard: 76 trạng thái (theme sáng) + 20 bản theme tối cho trạng thái `default` (DD-UI-15). Tổng 96.
- Trang canvas: "Đợt D — Cộng đồng và liên lạc" trong canvas "iShare — Giao diện"
  (https://claude.ai/artifact/HAykztXFcJbkAiSCXKvift#page-dot-d). Bản sao: `canvas/giao-dien/project/`.
- Design system: giống đợt A (`project/ds/ishare/`, bản "iShare Design System" 1795613002-b5c9).
- Cách vẽ trạng thái: phần lớn cắt 1440 × 900; trọn trang cho trang Thông báo, trang nhóm, tạo nhóm, cài đặt nhóm. Ngăn thông báo, popup tin nhắn, hộp thoại nhóm và nhóm chat vẽ trên nền trang gọi chúng. Chat dùng khung ba cột: điều hướng, hộp thư 340 px, cuộc trò chuyện.

## 2. Kết quả tool

| Tool | Lệnh | Kết quả |
|---|---|---|
| check_ui | `check_ui.py canvas/giao-dien/project --tokens output/tokens/tokens.json --design output/DESIGN.md` | ERROR=0 WARN=0 (cả canvas, 359 tệp) |
| check_inventory | `check_inventory.py --inventory output/screen-inventory.md --specs docs/specs --artboards canvas/giao-dien/project --batch D` | đủ 76/76; bản tối 20/76 (đúng DD-UI-15) |
| contrast | `contrast.py --tokens output/tokens/tokens.json --pairs output/tokens/contrast-pairs.csv` | 102/102 đạt (token không đổi từ bước 6) |

WARN giữ lại: không có.

## 3. Checklist bằng mắt

Rà trên ảnh chụp bản sao cục bộ (Chromium, 1440 px, font của design system), cả theme sáng và tối.

| Mục | Đạt | Ghi chú |
|---|---|---|
| ANTI-PATTERNS mục 9 (gồm brand test) | Đạt | Tin nhắn của mình dùng nền primary-soft, không gradient; nhãn Public/Private dùng chip trung tính có icon; nút Rời nhóm, Xóa nhóm dùng danger |
| QF-04 vùng bấm | Đạt | Nút, icon button cao ≥32 px (control-h-sm); hàng bảng, mục danh sách cao ≥44 px |
| QF-05 focus không bị che | Đạt | Ngăn thông báo, popup tin nhắn và ngăn thông tin nhóm chat nằm trên lớp riêng; ô soạn tin không bị lớp nào che |
| QF-13 tiếng Việt | Đạt | Tên nhóm, tên thành viên và tin nhắn dài xuống dòng đủ dấu |
| QF-14 nội dung dài | Đạt | Nhóm chat 100 thành viên (giới hạn), 20 thông báo một trang, tin nhắn đã thu hồi, thông báo gom nhóm "và 6 người khác" |
| QF-16 trợ giúp/khiếu nại nhất quán | Đạt | Menu tài khoản giữ "Khiếu nại của tôi"; bài bị từ chối trong nhóm có lý do |
| Nhất quán với các đợt trước | Đạt | Cùng khung trang, thẻ bài, hộp thoại với đợt A và C |

## 4. Lỗi

| Mã | Màn hình | Loại | Mô tả | Đề xuất | Mức | Đã sửa |
|---|---|---|---|---|---|---|
| QA-D-01 | SCR-M07-01 | Token | Vị trí ngăn thông báo viết `right: 120px` | Dùng `var(--space-16)` | Phải sửa | Đã sửa |

Thông điệp nguồn có chữ cụ thể được dùng nguyên văn (tin nhắn đã thu hồi, "Hệ thống đang bận, vui lòng thử lại sau", nội dung thông báo theo mẫu của M07). Phần còn lại (xác nhận rời nhóm, lỗi câu trả lời tham gia, trạng thái rỗng của hộp thư và danh sách chặn) viết theo giọng văn `PRODUCT.md`.

## 5. Đề xuất token / component mới

Không thêm token. Khung chat ba cột dựng bằng token; gộp vào đề xuất PageLayout của QA-dot-A (biến thể "chat").

## 6. Câu hỏi

| # | Câu hỏi | Trạng thái |
|---|---|---|
| — | Không có câu hỏi mới | — |
