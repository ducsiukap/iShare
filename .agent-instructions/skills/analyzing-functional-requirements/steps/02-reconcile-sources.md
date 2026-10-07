# Bước 2 — Hợp nhất nguồn

## Mục đích

Từ nhiều mục nguồn có thể đã sửa nhau qua nhiều phase, xác định **điều đang có hiệu lực** cho module.
Không làm bước này thì tài liệu sẽ trích quyết định cũ đã bị thay.

## Đầu vào

`index.json`, `scan-Mxx.json`, bảng C.1 đã được duyệt ở bước 1.

## Việc làm

1. Chạy `lineage.py --scan $W/scan-Mxx.json`. Tool chỉ liệt kê các dấu sửa đổi tìm thấy.
2. Với mỗi cạnh tool tìm được: đọc nguyên văn cả hai mục, xác nhận cạnh đúng hay sai, và sửa **toàn bộ** hay
   **một phần** (đa số DEC "amend" chỉ sửa một phần, ví dụ thêm ngoại lệ).
3. Tìm sửa đổi không có dấu: so các mục Sở hữu và Phụ thuộc **cùng chủ đề** (cùng giới hạn, cùng công thức, cùng
   quyền). Mục sau nói khác mục trước về cùng một điều là sửa đổi, dù không ghi "amended".
4. Gắn **Trạng thái** ở C.1:
   - Hiện hành
   - Sửa một phần bởi X (ghi phần nào ở C.2)
   - Bị thay bởi X
   - Trùng với X (cùng nội dung, giữ mục có nhiều thông tin hơn làm hiện hành)
   - Mâu thuẫn với X
5. Áp thứ tự ưu tiên ở `input/INPUTS.md` cho các cặp nói khác nhau về cùng một điều. Cặp không tự giải được
   (cùng cấp, không rõ mục nào mới hơn, hoặc mục mới không nói rõ có thay mục cũ không) thì ghi
   "Mâu thuẫn với X" và tạo câu hỏi `Q-nn` loại **Mâu thuẫn** ở B.1.
6. Mục `OPEN-nnn` liên quan tới module: ghi `TBD-Mxx-nn` ở B.2, lý do "OPEN-nnn hoãn có chủ đích",
   ảnh hưởng theo đánh giá của bạn. Không hỏi lại điểm đã hoãn có chủ đích.
7. Ghi chuỗi quyết định ở C.2: mỗi chuỗi một dòng, nêu phần nào còn hiệu lực.

## Ghi vào tệp FR

Phụ lục C.1 (cột Trạng thái), C.2; Phụ lục B.1 (câu hỏi Mâu thuẫn), B.2 (TBD từ OPEN).

## Tự kiểm trước cổng

- Mọi cạnh tool tìm được đã được xác nhận hoặc bác bỏ.
- Không còn mục Sở hữu nào để "Hiện hành" mà thực ra đã bị mục khác trong bảng nguồn sửa.
- Mỗi "Bị thay bởi X" và "Sửa một phần bởi X" đều có X trong C.1.

## Trình ở cổng

- Bảng chuỗi quyết định (C.2) dạng ngắn.
- Các mục bị thay, bị sửa một phần, trùng.
- Các cạnh tool tìm được nhưng bạn bác bỏ, kèm lý do.
- Mâu thuẫn: mỗi cái một câu hỏi theo khuôn ở SKILL.md. Người dùng có thể trả lời ngay hoặc để bước 6.
  Trả lời ngay thì ghi vào B.1, việc ghi register vẫn làm ở bước 6.
- TBD sinh từ OPEN.

## Không làm

Không đặt câu hỏi cho chỗ nguồn **chưa nói**; đó là GAP, gom ở bước 3–5 và hỏi ở bước 6.
