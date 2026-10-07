---
module: M05
ten_module: Topic & Tag
ma_tai_lieu: FR-M05
phien_ban: 0.1
trang_thai: Bản nháp
ngay: 2026-10-07
tac_gia: Phạm Văn Đức
moc_nguon: DEC-139, QA-266, ISS-206, OPEN-008
steps_completed: [1, 2, 3, 4, 5]
---
# Tài liệu yêu cầu chức năng — M05 Topic & Tag (VÍ DỤ ĐỊNH DẠNG)

> Tệp này chỉ minh họa cách viết **một** chức năng sau bước 5, dùng dữ liệu thật của DEC-048 và DEC-049.
> Nó không phải tài liệu M05 đã chốt và cố ý bỏ trống các phần không liên quan tới chức năng mẫu.

| Mã tài liệu | FR-M05 |
|---|---|
| Dự án | iShare |
| Module | M05 — Topic & Tag |
| Trạng thái | Bản nháp |
| Phiên bản | 0.1 |
| Ngày | 2026-10-07 |
| Tác giả | Phạm Văn Đức |

## 1. Tổng quan

### 1.1 Mục đích

(Lược bỏ trong ví dụ.)

## 4. Tổng quan chức năng

### 4.3 Ma trận quyền

| Hành động | Guest | User | Mod | Admin | Yêu cầu |
|---|---|---|---|---|---|
| Gán Topic cho bài viết của mình khi gửi | ✗ | ✓ (của mình) | ✓ (của mình) | ✓ (của mình) | FR-M05-01.01 |

### 4.4 Danh sách chức năng

| ID | Chức năng | Tác nhân chính | Kích hoạt |
|---|---|---|---|
| FR-M05-01 | Gán Topic cho bài viết | Tác giả bài viết | Tác giả gửi bài viết |

## 5. Yêu cầu chức năng

### 5.1 FR-M05-01 Gán Topic cho bài viết

**Yêu cầu cấp trên:** Hệ thống phải cho phép tác giả gán cho mỗi bài viết từ 1 đến 3 Topic thuộc danh sách Topic cố định.

**Lý do:** Topic là cách phân loại có cấu trúc, dùng để lọc và duyệt bài viết.

**Yêu cầu cấp dưới:**

| ID | Yêu cầu |
|---|---|
| FR-M05-01.01 | Khi tác giả gửi một bài viết có từ 1 đến 3 Topic thuộc danh sách Topic, hệ thống phải lưu các Topic đó cho bài viết. |
| FR-M05-01.02 | Nếu tác giả gửi một bài viết không có Topic nào, hệ thống phải từ chối gửi bài viết đó. |
| FR-M05-01.03 | Nếu tác giả chọn Topic thứ tư cho một bài viết, hệ thống phải từ chối Topic thứ tư đó. |

[GAP: bài viết lưu ở trạng thái bản nháp có bắt buộc đủ 1–3 Topic không — Q-01]

### 5.2 Quy tắc nghiệp vụ

| ID | Loại | Quy tắc | Ví dụ |
|---|---|---|---|
| BR-M05-01 | Ràng buộc | Mỗi bài viết được gửi có ít nhất 1 và tối đa 3 Topic. | Đã chọn Toán học, Tin học, Khác; chọn thêm Góc Chill thì Góc Chill bị từ chối, bài vẫn giữ 3 Topic. |

### 5.3 Dữ liệu nghiệp vụ

| Thực thể | Thuộc tính nguồn đã nêu | Quan hệ |
|---|---|---|
| Topic | Tên (một trong 11 Topic cố định) | Gắn với nhiều bài viết |
| Bài viết | (thuộc M03) | Có 1–3 Topic |

**Ma trận CRUD:**

| Thực thể | Tạo | Đọc | Sửa | Xóa |
|---|---|---|---|---|
| Liên kết bài viết–Topic | FR-M05-01.01 | M03 | Ngoài ví dụ | Ngoài ví dụ |

### 5.4 Giao tiếp với module khác

| Hướng | Module | Nội dung ở mức nghiệp vụ | Yêu cầu |
|---|---|---|---|
| Dùng | M03 | Thao tác gửi bài viết của tác giả | FR-M05-01.01 |

## 6. Lịch sử sửa đổi

| Phiên bản | Ngày | Nội dung | Người sửa |
|---|---|---|---|
| 0.1 | 2026-10-07 | Ví dụ định dạng | Phạm Văn Đức |

## Phụ lục A. Truy vết

| ID | Nguồn | Căn cứ | Ghi chú |
|---|---|---|---|
| FR-M05-01 | DEC-047, DEC-049 | Nói thẳng | Lý do lấy từ DEC-047 "used for filter/browse" |
| FR-M05-01.01 | DEC-048, DEC-049 | Nói thẳng | — |
| FR-M05-01.02 | DEC-049 | Suy ra | DEC-049 "Min 1 … (mandatory)" ⇒ bài không có Topic bị từ chối gửi |
| FR-M05-01.03 | DEC-049 | Suy ra | DEC-049 "max 3 topics/post" ⇒ Topic thứ tư bị từ chối |
| BR-M05-01 | DEC-049 | Nói thẳng | — |

## Phụ lục B. Câu hỏi, giả định và TBD

### B.1 Câu hỏi đã hỏi

| Mã | Loại | Câu hỏi | Trả lời | Ghi vào register |
|---|---|---|---|---|
| Q-01 | Thiếu chi tiết | DEC-049 nói mỗi bài 1–3 Topic (bắt buộc), DEC-031 có trạng thái bản nháp. Khi lưu bản nháp, có bắt buộc đủ 1–3 Topic không? Đề xuất: A) chỉ bắt buộc khi gửi, bản nháp có thể chưa có Topic. | Chờ bước 6 | — |

### B.2 TBD

| ID | Nội dung | Ảnh hưởng | Lý do chưa chốt |
|---|---|---|---|

## Phụ lục C. Sổ nguồn

### C.1 Bảng nguồn

| Nguồn | Nhãn | Trạng thái | Dùng ở | Ghi chú |
|---|---|---|---|---|
| DEC-047 | Sở hữu | Hiện hành | FR-M05-01 | Phần Tag ngoài ví dụ |
| DEC-048 | Sở hữu | Hiện hành | FR-M05-01.01 | — |
| DEC-049 | Sở hữu | Hiện hành | FR-M05-01.01, FR-M05-01.02, FR-M05-01.03, BR-M05-01 | Phần đổi tên, gộp ngoài ví dụ |
| DEC-031 | Phụ thuộc | Hiện hành | Chuyển M03 | Dùng làm bối cảnh cho Q-01 |

### C.2 Chuỗi quyết định

| Chuỗi | Nội dung hiện hành |
|---|---|
| — | Không có sửa đổi nào chạm tới DEC-047…049 |
