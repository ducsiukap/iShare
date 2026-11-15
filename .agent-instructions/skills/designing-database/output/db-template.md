---
module: Mxx
ten_module: <Tên module>
ma_tai_lieu: DB-Mxx
phien_ban: 0.1
trang_thai: Bản nháp
ngay: YYYY-MM-DD
tac_gia: Phạm Văn Đức
nguon: CD-Mxx v<phiên bản>
steps_completed: []
---
# Thiết kế cơ sở dữ liệu — Mxx <Tên module>

<!-- [Vietnamese Doc] Tài liệu tiếng Việt; tên bảng, cột, kiểu viết tiếng Anh. -->

| Mã tài liệu | DB-Mxx |
|---|---|
| Dự án | iShare |
| Module | Mxx — <Tên module> |
| Đầu vào | CD-Mxx phiên bản <…> |
| Trạng thái | Bản nháp |
| Phiên bản | 0.1 |
| Ngày | YYYY-MM-DD |
| Tác giả | Phạm Văn Đức |

<!-- Quy ước chung cho mọi bảng dưới đây:
     - Không đổi tên cột, không xóa cột, không đổi số mục: tool đọc bảng theo số mục và tên cột.
     - Ô không có nội dung ghi "—". Mục chưa tới bước làm thì để dòng "(Chưa làm — bước N)".
     - Bảng chỉ sinh từ lớp, cột chỉ sinh từ thuộc tính, khóa ngoại chỉ sinh từ quan hệ (giữ mã R-Mxx-nn).
     - Mục 6 do build_schema.py sinh; không sửa tay. -->

## 1. Bảng

<!-- Mỗi lớp của module một bảng, kể cả lớp liên kết, lớp thống kê, lớp con. Lớp của module khác ghi ở mục 7.1.
     Tên bảng: snake_case của tên lớp (QU-06). Cột "Từ lớp" giữ tên lớp PascalCase. -->

| Bảng | Từ lớp | Nhóm | Sở hữu | Ghi chú |
|---|---|---|---|---|
| (Chưa làm — bước 1) | | | | |

## 2. Cột

### 2.1 Cột từ thuộc tính

<!-- Mỗi thuộc tính thường ở mục 2.1 của CD một dòng, kể cả thuộc tính dẫn xuất. Null: Có | Không. Duy nhất: Có | Không.
     Cột: snake_case của tên thuộc tính (QU-07). Từ thuộc tính: Lớp.thuộcTính, viết đúng như CD (camelCase). -->

| Bảng | Cột | Kiểu | Null | Duy nhất | Từ thuộc tính | Ghi chú |
|---|---|---|---|---|---|---|
| (Chưa làm — bước 2) | | | | | | |

### 2.2 Thuộc tính đối tượng không chuyển

| Lớp | Thuộc tính | Kiểu | Lý do không chuyển |
|---|---|---|---|
| (Chưa làm — bước 2) | | | |

## 3. Quan hệ giữa các bảng

<!-- ID: đúng mã của CD. Dạng đọc theo thứ tự Bảng A–Bảng B; quan hệ 1-n viết bảng phía 1 ở cột Bảng A.
     Xử lý: Tách riêng | Gộp | Cha–con. Quan hệ 1-1 luôn ghi lý do ở cột Ghi chú. Không được có n-n. -->

| ID | Bảng A | Bảng B | Dạng | Xử lý | Ghi chú |
|---|---|---|---|---|---|
| (Chưa làm — bước 3) | | | | | |

## 4. Khóa

### 4.1 Khóa chính

<!-- Bảng con: khóa chính là khóa ngoại tới bảng cha. Bảng thống kê không có id: ghi "Không có". -->

| Bảng | Khóa chính | Ghi chú |
|---|---|---|
| (Chưa làm — bước 4) | | |

### 4.2 Khóa ngoại

<!-- Tên cột khóa ngoại viết snake_case, kết thúc bằng _id. Tham chiếu viết dạng tên_bảng(cột), ví dụ posts(id).
     Kiểu bằng kiểu khóa chính được tham chiếu. Từ quan hệ: mã R-Mxx-nn. -->

| Bảng | Cột | Kiểu | Null | Duy nhất | Tham chiếu | Từ quan hệ | Ghi chú |
|---|---|---|---|---|---|---|---|
| (Chưa làm — bước 4) | | | | | | | |

## 5. Loại dư thừa

### 5.1 Cột bị loại

<!-- Loại dư thừa: Dẫn xuất | Trùng lặp. Cách có lại giá trị: công thức hoặc cách truy vấn bằng bảng và cột của lược đồ cuối. -->

| Bảng | Cột | Loại dư thừa | Căn cứ | Cách có lại giá trị |
|---|---|---|---|---|
| (Chưa làm — bước 5) | | | | |

### 5.2 Bảng bị loại

| Bảng | Lý do |
|---|---|
| (Chưa làm — bước 5) | |

### 5.3 Dẫn xuất nhưng giữ lại

<!-- Chỉ ghi khi FR yêu cầu lưu và người dùng đã quyết giữ. Nguồn: mã FR-/BR- đòi lưu và mã DD-Mxx-nn. -->

| Bảng | Cột | Lý do giữ | Nguồn |
|---|---|---|---|
| (Chưa làm — bước 5) | | | |

### 5.4 Đã xét nhưng không coi là dư thừa

| Bảng | Cột | Vì sao không dư thừa |
|---|---|---|
| (Chưa làm — bước 5) | | |

## 6. Lược đồ cuối

### 6.1 Bảng và cột

<!-- BEGIN:SCHEMA -->
(Chưa làm — bước 5)
<!-- END:SCHEMA -->

### 6.2 Sơ đồ quan hệ

<!-- BEGIN:PUML -->
(Chưa làm — bước 5)
<!-- END:PUML -->

## 7. Liên module

### 7.1 Bảng của module khác được tham chiếu

| Bảng ngoài | Module sở hữu | Dùng thế nào |
|---|---|---|
| (Chưa làm — bước 1) | | |

### 7.2 Khóa ngoại đề nghị cho bảng của module khác

<!-- Khi bảng của module khác là phía n của một quan hệ với bảng của module này. -->

| Bảng của module khác | Cột | Kiểu | Tham chiếu | Từ quan hệ |
|---|---|---|---|---|
| (Chưa làm — bước 4) | | | | |

## 8. Quyết định thiết kế

| Mã | Quyết định | Lý do |
|---|---|---|
| — | — | — |

## 9. Câu hỏi và điểm chưa chốt

| Mã | Loại | Câu hỏi | Trả lời | Ghi vào |
|---|---|---|---|---|
| — | — | — | — | — |

## 10. Lịch sử sửa đổi

| Phiên bản | Ngày | Nội dung | Người sửa |
|---|---|---|---|
| 0.1 | YYYY-MM-DD | Tạo mới | Phạm Văn Đức |
