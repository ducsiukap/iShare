---
ma_tai_lieu: DESIGN
phien_ban: 0.1
trang_thai: Bản nháp
ngay: YYYY-MM-DD
tac_gia: Phạm Văn Đức
steps_completed: []
buoc_hien_tai: 1
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
| Bước hiện tại | 1 — Brief |
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
| DD-UI-01 | | | | | |

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
| 0.1 | YYYY-MM-DD | Tạo tệp ở bước 1 |
