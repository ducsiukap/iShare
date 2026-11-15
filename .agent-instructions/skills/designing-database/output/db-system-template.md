---
module: SYS
ten_module: Toàn hệ thống iShare
ma_tai_lieu: DB-SYS
phien_ban: 0.1
trang_thai: Bản nháp
ngay: YYYY-MM-DD
tac_gia: Phạm Văn Đức
nguon: CD-SYS v…; DB-M01 v…, DB-M02 v…, …
steps_completed: []
---
# Thiết kế cơ sở dữ liệu — Toàn hệ thống iShare

<!-- [Vietnamese Doc] Bản gộp từ các DB-Mxx.md, khớp với CD-SYS.md.
     Số mục giữ giống tài liệu module để tool đọc được. Ở bản hệ thống không còn bảng ngoài: mục 7.1, 7.2 để trống. -->

## 1. Bảng

| Bảng | Từ lớp | Nhóm | Sở hữu | Ghi chú |
|---|---|---|---|---|
| | | | | |

## 2. Cột

### 2.1 Cột từ thuộc tính

| Bảng | Cột | Kiểu | Null | Duy nhất | Từ thuộc tính | Ghi chú |
|---|---|---|---|---|---|---|
| | | | | | | |

### 2.2 Thuộc tính đối tượng không chuyển

| Lớp | Thuộc tính | Kiểu | Lý do không chuyển |
|---|---|---|---|
| | | | |

## 3. Quan hệ giữa các bảng

| ID | Bảng A | Bảng B | Dạng | Xử lý | Ghi chú |
|---|---|---|---|---|---|
| | | | | | |

## 4. Khóa

### 4.1 Khóa chính

| Bảng | Khóa chính | Ghi chú |
|---|---|---|
| | | |

### 4.2 Khóa ngoại

| Bảng | Cột | Kiểu | Null | Duy nhất | Tham chiếu | Từ quan hệ | Ghi chú |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

## 5. Loại dư thừa

### 5.1 Cột bị loại

<!-- Gồm cột đã loại ở từng module và cột loại thêm khi gộp (ghi "loại khi gộp, MD-nn" ở cột Căn cứ). -->

| Bảng | Cột | Loại dư thừa | Căn cứ | Cách có lại giá trị |
|---|---|---|---|---|
| | | | | |

### 5.2 Bảng bị loại

| Bảng | Lý do |
|---|---|
| | |

### 5.3 Dẫn xuất nhưng giữ lại

| Bảng | Cột | Lý do giữ | Nguồn |
|---|---|---|---|
| | | | |

### 5.4 Đã xét nhưng không coi là dư thừa

| Bảng | Cột | Vì sao không dư thừa |
|---|---|---|
| | | |

## 6. Lược đồ cuối

### 6.1 Bảng và cột

<!-- BEGIN:SCHEMA -->
<!-- END:SCHEMA -->

### 6.2 Sơ đồ quan hệ toàn hệ thống

<!-- BEGIN:PUML -->
<!-- END:PUML -->

## 7. Liên module

### 7.1 Bảng của module khác được tham chiếu

| Bảng ngoài | Module sở hữu | Dùng thế nào |
|---|---|---|
| — | — | — |

### 7.2 Khóa ngoại đề nghị cho bảng của module khác

| Bảng của module khác | Cột | Kiểu | Tham chiếu | Từ quan hệ |
|---|---|---|---|---|
| — | — | — | — | — |

## 8. Quyết định gộp

<!-- Quyết định đã có ở EC-SYS, CD-SYS thì dẫn lại đúng mã MD-nn; quyết định mới của lượt gộp này đánh số tiếp. -->

| Mã | Vấn đề | Các module | Quyết định | Áp dụng cho |
|---|---|---|---|---|
| | | | | |

## 9. Câu hỏi và điểm chưa chốt

| Mã | Loại | Câu hỏi | Trả lời | Ghi vào |
|---|---|---|---|---|
| — | — | — | — | — |

## 10. Lịch sử sửa đổi

| Phiên bản | Ngày | Nội dung | Người sửa |
|---|---|---|---|
| 0.1 | YYYY-MM-DD | Tạo mới | Phạm Văn Đức |
