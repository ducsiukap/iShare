---
ma_tai_lieu: QA-<dot-X | final>
phien_ban: 0.1
trang_thai: Bản nháp
ngay: YYYY-MM-DD
tac_gia: Phạm Văn Đức
---
# Kiểm tra giao diện — <Đợt X (tên) | Toàn bộ>

[Vietnamese Doc]

## 1. Phạm vi

- Màn hình: <danh sách SCR-*>; artboard: <số>; trang canvas: <link>.

## 2. Kết quả tool

| Tool | Lệnh | Kết quả |
|---|---|---|
| check_ui | `check_ui.py … --tokens … --design …` | ERROR=0 WARN=n |
| check_inventory | `check_inventory.py … --artboards … [--batch X] [--require-artboards]` | đủ n/n |
| contrast | `contrast.py --tokens … --pairs …` | n/n đạt |

WARN giữ lại:

| Luật | Tệp | Lý do giữ |
|---|---|---|

## 3. Checklist bằng mắt

| Mục | Đạt | Ghi chú |
|---|---|---|
| ANTI-PATTERNS mục 9 (gồm brand test) | | |
| QF-04 vùng bấm | | |
| QF-05 focus không bị che | | |
| QF-13 tiếng Việt | | |
| QF-14 nội dung dài, công thức | | |
| QF-16 trợ giúp/khiếu nại nhất quán | | |
| Nhất quán với các đợt trước | | |

## 4. Lỗi

| Mã | Màn hình | Loại (AP / QF / Nhất quán / Nguồn / Nội dung) | Mô tả | Đề xuất | Mức | Đã sửa |
|---|---|---|---|---|---|---|
| QA-X-01 | | | | | Phải sửa | |

## 5. Đề xuất token / component mới

| Đề xuất | Lý do | Màn hình cần | Quyết định |
|---|---|---|---|

## 6. Câu hỏi

| # | Câu hỏi | Trạng thái |
|---|---|---|
