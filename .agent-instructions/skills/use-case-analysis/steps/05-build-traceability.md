# Bước 5 — Truy vết chi tiết và liên module

[Vietnamese Doc]

Dùng bảng marker của [template](../output/us-template.md) và
[công cụ](../tools/README.md).

1. Lập bảng kiểm kê nhóm FR để biết chức năng nào thuộc scope.
   Bổ sung đường truy vết FR → UC con → UC chính → tổng quan hệ thống;
   mục tổng quan trỏ về tài liệu module nguồn. Mọi sub có core trong bảng
   decomposition; FR biểu diễn bằng BR/AUT/bước vẫn ghi core liên quan nếu có.
2. Với **từng FR chi tiết và BR còn hiệu lực** trong scope, ghi một hoặc nhiều
   target là anchor UC/bước/nhánh/điều kiện/quy tắc/AUT, mức Đủ/Một phần/Chưa
   và lý do. Không coi đủ nhóm FR là đủ hành vi chi tiết.
3. Chiều ngược: mọi UC, quan hệ, bước và kết quả đều có căn cứ. Đọc lại nội dung
   nguồn, không chỉ kiểm mã tồn tại. Viết đầy đủ mã, không dùng khoảng rút gọn.
4. AUT/logic hiển thị có nội dung và anchor thật; nhãn “nền” không miễn đặc tả.
   Mã đã bỏ ghi riêng cùng bằng chứng và không đưa vào mẫu số yêu cầu hiện hành.
5. Đối chiếu owner, sự kiện và quyền ở FR liên module. Tái sử dụng UC ID chung;
   FR ngoài module không tạo thêm tính năng ngoài scope.
6. Chạy check_us.py ở chế độ phù hợp. Mã lỗi sửa trước; WARN ghi lý do và phần
   chưa kiểm. Với nguồn mới đổi, đánh dấu các mapping/bước/quan hệ bị ảnh hưởng.
7. Review bằng người/model nội dung từng mapping trước khi ghi Đủ. Tool không
   chứng minh target thực hiện đúng ý nghĩa yêu cầu.

Chốt module chỉ khi đủ cả nhóm lẫn chi tiết trong scope. Mode overview được
ghi “tham chiếu đặc tả module/chưa đặc tả”; không báo đầy đủ luồng chi tiết.
Phạm vi một phần ghi rõ và không dùng kết quả check giới hạn để kết luận toàn module.

Cập nhật tiến độ và trình cổng.

