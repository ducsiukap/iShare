# Routing — ISH-RT-M05 Topic & Tag
<!-- [Vietnamese Doc] -->

| Mã tài liệu | ISH-RT-M05 |
|---|---|
| Liên kết SR | ISH-SR-M05 |
| Phiên bản | 0.3 |
| Ngày | 2026-10-04 |

## R1. Mô hình dữ liệu (Phase 8)

| Nguồn | Nội dung | Ghi chú |
|---|---|---|
| DEC-051 | Tag lưu trong bảng riêng (id, tên chuẩn hóa chữ thường duy nhất, thời điểm tạo, không có người tạo) cùng một bảng liên kết Tag–bài viết. | Chi tiết lưu trữ, phần hành vi (giới hạn số lượng/độ dài, tự tạo không duyệt) đã vào SR mục 5.6. |
| DEC-049 | Khi gộp Topic, liên kết bài viết–Topic được cập nhật lại ở bảng liên kết tương ứng. | Hành vi "chuyển bài viết sang Topic đích" đã vào SR ISH-M05-003.1; đây chỉ là cơ chế lưu trữ. |
| DEC-050, QA-104 | Phản hồi của người dùng so với Topic do AI gợi ý (giữ nguyên hay đổi) được ghi nhận, chỉ khi Topic gợi ý chưa lỗi thời. | Dùng để đánh giá độ chính xác của AI, không phải hành vi người dùng quan sát được. |

## R2. Yêu cầu phi chức năng (Phase 7)

| Nguồn | Nội dung | Ghi chú |
|---|---|---|
| DEC-052 | Điểm Trending được tính lại theo chu kỳ 15-30 phút và lưu đệm, không tính trực tiếp theo thời gian thực mỗi lần có người xem. | Hiệu năng/cơ chế tính lại, không phải quy tắc nghiệp vụ của điểm số (đã vào SR). |
| DEC-099 | Lệnh gọi AI gợi ý Topic có thời gian chờ tối đa 10 giây; nếu hết hạn thì thử lại đúng 1 lần sau 2 giây. | Thông số kỹ thuật của cơ chế gọi AI, không phải hành vi chức năng. |

## R3. HMI và thiết kế giao diện

| Nguồn | Nội dung | Ghi chú |
|---|---|---|

## R4. Ghi chú quy trình và phạm vi (không phải yêu cầu hệ thống)

| Nguồn | Nội dung | Ghi chú |
|---|---|---|
| QA-108 | Bình luận không có Topic/Tag riêng — dùng chung ngữ cảnh Topic/Tag của bài viết cha. | Xác nhận phạm vi: không cần yêu cầu riêng cho Comment (M04) về Topic/Tag. |

## R5. Thuộc module khác

| Nguồn | Nội dung | Module và ID sở hữu |
|---|---|---|
| DRAFT §3.3, DRAFT §3.4, ISS-046, QA-033, QA-034 | Trường Lớp/Khối (grade_level) trên bài viết và trên hồ sơ người dùng là trục phân loại độc lập song song với Topic, không thuộc Topic/Tag. | M03 — Post (F-POST-09, module-registry dòng 66) cho Post; M02 — User Profile cho hồ sơ người dùng (QA-034) |
| DEC-141 | Gửi thông báo cho người theo dõi khi Topic đang theo dõi có bài viết mới. | M07 — Notification (chưa có SR, ghi nguồn DEC-141 chờ M07 tiếp nhận) |

## R6. Đã bị thay thế

| Nguồn | Bị thay bởi | Ghi chú |
|---|---|---|
| ISS-046, QA-033 | DEC-140 (xem QA-267) | Phần "2 tầng: Category → Topic" của ISS-046/QA-033 (Phase 3/4) bị thay bởi quyết định Phase 5 (DEC-047/048): Topic là 1 tầng duy nhất cho M05. Phần grade_level của hai mục này không bị thay thế — xem R5. |

## R7. Không đưa vào SR

| Nguồn | Nội dung | Lý do |
|---|---|---|
| DRAFT §11.2, QA-269, ISS-209 | DRAFT §11.2 từng nêu AI đề xuất cả Topic/Category và Tags. Phase 5 (DEC-050/051) chỉ quyết AI gợi ý Topic; Tag giữ hoàn toàn tự do. | Đã xác nhận chủ đích, không phải thiếu sót — QA-269: Tag "fully free" mâu thuẫn triết lý với việc để AI gợi ý. |
