# Bước 3 — Chức năng và vai trò

## Mục đích

Chia module thành các chức năng ở mức mục tiêu người dùng và chốt ai được làm gì.
Danh sách này cũng là danh sách use case cho giai đoạn thiết kế.

## Đầu vào

Bảng C.1 sau bước 2 (chỉ dùng mục Sở hữu và Phụ thuộc có trạng thái Hiện hành hoặc Sửa một phần).

## Việc làm

1. Gom các mục Sở hữu thành **chức năng**: một tác nhân chính, một mục tiêu, hoàn thành trong một lần dùng
   (ví dụ "Gán Topic cho bài viết", "Gộp hai Topic"). Không tạo chức năng mà nguồn không nhắc tới.
   Hành vi hệ thống tự chạy (ví dụ tính Trending định kỳ) cũng là một chức năng, tác nhân là "Hệ thống".
2. Đặt ID `FR-Mxx-nn` theo thứ tự xuất hiện trong nghiệp vụ. Mục 4.4: ID, tên, tác nhân chính, kích hoạt.
3. Mục 4.2 vai trò: Guest, User, Mod, Admin, và vai trò theo ngữ cảnh (tác giả bài viết, chủ nhóm…) chỉ khi
   nguồn nói tới.
4. Mục 4.3 ma trận quyền, một dòng cho mỗi hành động:
   - ✓ hoặc ✗ khi nguồn nói thẳng, hoặc suy ra bắt buộc ("chỉ Mod/Admin được…" ⇒ User và Guest bị từ chối).
   - "✓ (của mình)" khi có điều kiện sở hữu.
   - Ô nguồn không nói mà ảnh hưởng tới hành vi: ghi `?` và tạo `[GAP]` + câu hỏi `Q-nn` (loại Thiếu chi tiết).
   - Cột Yêu cầu để "—", bước 5 điền.
5. Mục 4.5: ưu tiên MoSCoW lấy từ `MR-Mxx`. Không đọc được thì ghi TBD.
6. Tạo khung mục `### 5.x FR-Mxx-nn <Tên>` cho từng chức năng, đúng thứ tự 4.4, chỉ có dòng
   "Yêu cầu cấp trên" và "Lý do" để trống (bước 5 viết).
7. Phụ lục A: một dòng cho mỗi `FR-Mxx-nn` với các nguồn tạo nên chức năng đó.
8. Cập nhật 1.2 nếu ranh giới thay đổi.

## Ghi vào tệp FR

Mục 1.2, 4.2, 4.3, 4.4, 4.5, khung 5.x, Phụ lục A (dòng cấp trên), Phụ lục B.1 (GAP về quyền).

## Tự kiểm trước cổng

- Mỗi mục Sở hữu hiện hành thuộc ít nhất một chức năng, hoặc bạn ghi rõ nó sẽ thành quy tắc ở bước 4.
- Không chức năng nào thiếu nguồn.
- Hai chức năng không chồng nhau (cùng tác nhân, cùng mục tiêu).

## Trình ở cổng

- Bảng chức năng (ID, tên, tác nhân, kích hoạt).
- Ma trận quyền, đánh dấu các ô suy ra và các ô `?`.
- Nguồn Sở hữu chưa gắn vào chức năng nào, kèm dự định xử lý.
- Chức năng bạn **cân nhắc nhưng không tạo** vì nguồn không nói (nếu có), để người dùng biết.

## Không làm

Không viết yêu cầu cấp dưới. Không thêm chức năng "thường thấy ở diễn đàn khác".
