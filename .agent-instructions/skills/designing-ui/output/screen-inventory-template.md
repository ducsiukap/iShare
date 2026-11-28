---
ma_tai_lieu: SCREEN-INVENTORY
phien_ban: 0.1
trang_thai: Bản nháp
ngay: YYYY-MM-DD
tac_gia: Phạm Văn Đức
---
# Danh mục màn hình — iShare

[Vietnamese Doc] — Hợp đồng của bước 5, 7, 8. Các bảng có marker `<!-- ui:… -->` được `check_inventory.py` đọc: giữ
đúng tên cột. Nhiều giá trị trong một ô cách nhau bằng dấu phẩy. Slug trạng thái theo `CONVENTIONS.md` mục 4.

## 1. Tóm tắt

| Module | Số màn hình | Số artboard dự kiến |
|---|---|---|

## 2. Màn hình

Cột: `id` (SCR-Mxx-nn / SCR-SHARED-nn) · `name` · `module` (Mxx hoặc SHARED) · `roles` · `uc` · `sc` · `sources`
(FR/BR) · `states` · `devices` (desktop, mobile) · `batch` (A–E) · `notes`.

<!-- ui:screens -->
| id | name | module | roles | uc | sc | sources | states | devices | batch | notes |
|---|---|---|---|---|---|---|---|---|---|---|

## 3. UC không có màn hình riêng

<!-- ui:no-screen -->
| uc | reason | shown_as |
|---|---|---|

## 4. Chia đợt

<!-- ui:batches -->
| batch | name | order_reason |
|---|---|---|
| A | Đọc và viết | Dùng màn hình mẫu bước 3, tạo phần lớn component |
| B | Con người | |
| C | Kiểm duyệt và quản trị | |
| D | Cộng đồng và liên lạc | |
| E | Vào hệ thống và tìm kiếm | |

## 5. Nguồn đã dùng

`check_inventory.py` so cột `version` với tài liệu hiện tại để báo màn hình bị ảnh hưởng khi nguồn đổi. FR: giá trị
`phien_ban`; US, SC: giá trị `date` trong bảng tài liệu.

<!-- ui:sources -->
| path | version |
|---|---|

## 6. Câu hỏi mở

| # | Câu hỏi | Màn hình | Trạng thái |
|---|---|---|---|
