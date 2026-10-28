# Bước 1 — Trích xuất Chức năng con

**Mục tiêu:** Đọc FR-Mxx.md và xây dựng Mục 1 (Bảng tổng hợp chức năng con).

## Làm gì

1. Đọc metadata của `FR-Mxx.md` (tên module, phiên bản, ngày lập, các mốc register căn cứ).
2. Điền bảng metadata vào phần đầu `US-Mxx.md`.
3. Đọc mục **4.4 Danh sách chức năng** trong FR để lấy tất cả mã `FR-Mxx-nn`.
4. Với mỗi mã, đọc mục **5.nn** tương ứng để hiểu phạm vi và bản chất xử lý nghiệp vụ, rồi viết mô tả ngắn gọn (1–2 câu, súc tích, bao hàm bản chất nghiệp vụ và trạng thái xử lý).
5. Ghi vào **Mục 1** của `US-Mxx.md` theo cấu trúc bảng chuẩn:

```markdown
| STT | Mã chức năng | Tên chức năng con | Mô tả ngắn gọn phạm vi & nghiệp vụ |
|:---:|:---:|---|---|
| 1 | **FR-Mxx-01** | <tên> | <mô tả 1–2 câu súc tích> |
...
```

## Kiểm tra trước khi trình cổng

- [ ] Số dòng trong bảng = số chức năng trong mục 4.4 của FR (không thiếu, không thừa).
- [ ] Mỗi mô tả ngắn gọn, rõ ràng phạm vi, không quá dài dòng.
- [ ] Mã chức năng đúng định dạng chuẩn `FR-Mxx-nn` (hai chữ số).
- [ ] **Khóa chặt phạm vi:** Xác nhận danh sách này là hàng rào phạm vi (Scope Boundary) tuyệt đối; các Use Case con ở Bước 4 chỉ được lấy từ các chức năng này (giữ nguyên hoặc gộp), cấm tự suy diễn thêm.

## Cổng xác nhận

Gửi tin nhắn theo mẫu trong SKILL.md và chờ.

