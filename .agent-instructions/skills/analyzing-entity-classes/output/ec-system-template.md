---
module: SYS
ten_module: Toàn hệ thống iShare
ma_tai_lieu: EC-SYS
phien_ban: 0.1
trang_thai: Bản nháp
ngay: YYYY-MM-DD
tac_gia: Phạm Văn Đức
nguon: EC-M01 v…, EC-M02 v…, …
steps_completed: []
---
# Phân tích lớp thực thể — Toàn hệ thống iShare

<!-- [Vietnamese Doc] Bản gộp từ các EC-Mxx.md. Số mục giữ giống tài liệu module (2.2, 2.3, 3.3, 3.4, 4) để tool đọc được;
     các mục chỉ có ở tài liệu module (1.1, 1.2, 2.1, 2.4, 3.1, 3.2, 5) không có ở đây. -->

## 1. Tài liệu nguồn

| Tài liệu | Module | Phiên bản | Trạng thái |
|---|---|---|---|
| EC-M01 | M01 | | |

## 2. Lớp và thuộc tính

### 2.2 Lớp

<!-- Sở hữu: đúng một module. Cột "Module tham chiếu": các module khác có dùng lớp này. -->

| Lớp | Tên tiếng Việt | Nhóm | Sở hữu | Mô tả | Thuộc tính | Nguồn | Module tham chiếu |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

### 2.3 Thuộc tính

<!-- Nguồn ghi mã FR, có thể kèm mã module khi thuộc tính do module khác bổ sung (ví dụ "M12: FR-M12-03.01").
     Căn cứ: Nguồn nêu | Đề xuất. Bản hệ thống không còn dòng Tham chiếu: thuộc tính mà một module đọc của lớp
     module khác đã nằm ở lớp đó (hoặc là điểm lệch cần quyết định). -->

| Lớp | Thuộc tính | Tên tiếng Việt | Tính chất | Căn cứ | Ràng buộc nguồn nêu | Nguồn | Ghi chú |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 3. Quan hệ giữa các lớp

### 3.3 Lớp liên kết

| Lớp liên kết | Tách từ quan hệ n-n | Thuộc tính riêng của liên kết | Nguồn |
|---|---|---|---|
| | | | |

### 3.4 Quan hệ

<!-- Giữ ID R-Mxx-nn của module. Quan hệ chỉ sinh ra khi gộp: R-SYS-nn. -->

| ID | Lớp A | Bội số A | Lớp B | Bội số B | Dạng | Loại | Bên chính | Căn cứ | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | |

## 4. Sơ đồ lớp phân tích toàn hệ thống

<!-- BEGIN:DIAGRAM -->
<!-- END:DIAGRAM -->

## 7. Bảng tra nghĩa

<!-- Ghi chú ngắn để tra cứu nhanh: mỗi lớp, mỗi thuộc tính, mỗi quan hệ một dòng với ý nghĩa của nó. Ràng buộc, nguồn FR
     ở mục 2.3; căn cứ chọn loại quan hệ ở mục 3.4. Thuộc tính dẫn xuất có "/" phía trước. Lập ở việc C, trước khi chốt. -->

### 7.1 Lớp

| Lớp | Tên tiếng Việt | Ý nghĩa |
|---|---|---|
| | | |

### 7.2 Thuộc tính

| Lớp | Thuộc tính | Ý nghĩa |
|---|---|---|
| | | |

### 7.3 Quan hệ

| ID | Quan hệ (bội số) | Loại | Ý nghĩa |
|---|---|---|---|
| | | | |

## 8. Quyết định gộp

<!-- Mỗi điểm lệch giữa các module một dòng. "Áp dụng cho": tài liệu module phải sửa theo (EC-Mxx, và CD-Mxx, DB-Mxx nếu bị kéo theo).
     CD-SYS và DB-SYS áp dụng lại đúng các quyết định này. -->

| Mã | Vấn đề | Các module | Quyết định | Áp dụng cho |
|---|---|---|---|---|
| MD-01 | | | | |

## 9. Lịch sử sửa đổi

| Phiên bản | Ngày | Nội dung | Người sửa |
|---|---|---|---|
| 0.1 | YYYY-MM-DD | Tạo mới | Phạm Văn Đức |
