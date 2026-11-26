---
ma_tai_lieu: QA-dot-C
phien_ban: 0.1
trang_thai: Bản nháp
ngay: 2026-11-26
tac_gia: Phạm Văn Đức
---
# Kiểm tra giao diện — Đợt C (Kiểm duyệt và quản trị)

[Vietnamese Doc]

## 1. Phạm vi

- Màn hình (27): SCR-SHARED-05, SCR-M08-02, SCR-SHARED-06, SCR-M03-05, SCR-M04-02, SCR-M05-02, SCR-M05-03, SCR-M05-04, SCR-M05-05, SCR-M08-01, SCR-M08-03, SCR-M08-04, SCR-M08-05, SCR-M08-06, SCR-M09-01, SCR-M09-02, SCR-M09-03, SCR-M09-04, SCR-M10-01, SCR-M10-02, SCR-M10-03, SCR-M10-04, SCR-M10-05, SCR-M10-06, SCR-M15-01, SCR-M15-02, SCR-M15-03.
- Artboard: 84 trạng thái (theme sáng) + 27 bản theme tối cho trạng thái `default` (DD-UI-15). Tổng 111.
- Trang canvas: "Đợt C — Kiểm duyệt và quản trị" trong canvas "iShare — Giao diện"
  (https://claude.ai/artifact/HAykztXFcJbkAiSCXKvift#page-dot-c). Bản sao: `canvas/giao-dien/project/`.
- Design system: giống đợt A (`project/ds/ishare/`, bản "iShare Design System" 1795613002-b5c9).
- Cách vẽ trạng thái: phần lớn cắt 1440 × 900 vì hàng chờ, bảng và trang thống kê vừa một khung nhìn; trọn trang cho chi tiết vụ báo cáo, chi tiết khiếu nại, cấu hình hệ thống và thống kê. Hộp thoại (báo cáo, gộp Chủ đề, đổi Chủ đề/Tag, lý do biện pháp, từ chức) vẽ trên nền trang gọi chúng. Người xem: Mod Minh, Admin Hòa, ADMIN gốc An.

## 2. Kết quả tool

| Tool | Lệnh | Kết quả |
|---|---|---|
| check_ui | `check_ui.py canvas/giao-dien/project --tokens output/tokens/tokens.json --design output/DESIGN.md` | ERROR=0 WARN=0 (cả canvas, 359 tệp) |
| check_inventory | `check_inventory.py --inventory output/screen-inventory.md --specs docs/specs --artboards canvas/giao-dien/project --batch C` | đủ 84/84; bản tối 27/84 (đúng DD-UI-15) |
| contrast | `contrast.py --tokens output/tokens/tokens.json --pairs output/tokens/contrast-pairs.csv` | 102/102 đạt (token không đổi từ bước 6) |

WARN giữ lại: không có.

## 3. Checklist bằng mắt

Rà trên ảnh chụp bản sao cục bộ (Chromium, 1440 px, font của design system), cả theme sáng và tối.

| Mục | Đạt | Ghi chú |
|---|---|---|
| ANTI-PATTERNS mục 9 (gồm brand test) | Đạt | Nút nguy hiểm (Ban, Xóa, Gỡ banner, Từ chức) dùng màu danger, chỉ một nút chính mỗi vùng; biểu đồ dùng bảng màu dữ liệu của design system, có bảng số liệu thay thế |
| QF-04 vùng bấm | Đạt | Nút, icon button cao ≥32 px (control-h-sm); hàng bảng, mục danh sách cao ≥44 px |
| QF-05 focus không bị che | Đạt | Hộp thoại có scrim và đệm trên space-8; khung quản trị không có thanh dính che nội dung |
| QF-13 tiếng Việt | Đạt | Lý do báo cáo dài và tên đối tượng dài trong bảng xuống dòng, không bị cắt |
| QF-14 nội dung dài | Đạt | Hàng chờ 5 vụ có đủ các trạng thái (mở, đang giữ, AI gắn cờ); nhật ký nhiều trang; biểu đồ 9 tháng |
| QF-16 trợ giúp/khiếu nại nhất quán | Đạt | Màn hình bị khóa có nút Gửi khiếu nại và hạn khiếu nại; Mức cảnh cáo có lối khiếu nại từng lần cảnh cáo |
| Nhất quán với các đợt trước | Đạt | Cùng khung trang người dùng của đợt A; khung quản trị thêm cột điều hướng nhóm "Kiểm duyệt" và "Quản trị" |

## 4. Lỗi

| Mã | Màn hình | Loại | Mô tả | Đề xuất | Mức | Đã sửa |
|---|---|---|---|---|---|---|
| QA-C-01 | SCR-M08-01 | Nhất quán | Hộp thoại báo cáo cao quá khung nhìn, nút Gửi bị đẩy khỏi màn hình | Đệm trên space-8, ô mô tả 2 dòng | Phải sửa | Đã sửa |
| QA-C-02 | SCR-M08-03 | Nhất quán | Bảng báo cáo tràn ngang vì cột "Chỉ số báo cáo sai" | Chuyển chỉ số sang cột phụ "Chỉ số báo cáo sai (90 ngày)" | Phải sửa | Đã sửa |
| QA-C-03 | SCR-M08-04 | Nguồn | Wireframe bước 5 ghi ban 7 ngày; BR-M08-34 quy định ban theo lịch sử: lần đầu 30 ngày, lần hai 90 ngày, sau đó vĩnh viễn | Theo nguồn BR-M08-34 | Phải sửa | Đã theo nguồn |

Thông điệp nguồn có chữ cụ thể được dùng nguyên văn: tên các lý do báo cáo, "Tài khoản đã bị khóa", "Hệ thống đang bận, vui lòng thử lại sau", banner "Bảo trì hệ thống lúc 22:00.". Phần còn lại (lỗi "Vui lòng nhập lý do", trạng thái rỗng của hàng chờ, xác nhận gộp Chủ đề, chú thích công tắc AI) viết theo giọng văn `PRODUCT.md`.

## 5. Đề xuất token / component mới

Không thêm token. Khung quản trị (cột điều hướng hai nhóm) đang dựng bằng token trong `<helmet>`; gộp vào đề xuất PageLayout của QA-dot-A (biến thể "admin").

## 6. Câu hỏi

| # | Câu hỏi | Trạng thái |
|---|---|---|
| — | Không có câu hỏi mới | — |
