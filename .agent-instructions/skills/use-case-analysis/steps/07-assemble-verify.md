# Bước 7 — Review và trình phê duyệt

[Vietnamese Doc]

1. Kiểm baseline: FR còn đúng phiên bản, scope không trôi; có đánh giá tác động
   nguồn đổi và mọi quyết định cần làm rõ được xử lý/ghi giới hạn.
2. Review actor/boundary/mức mục tiêu; không quota UC, không phân rã thao tác
   UI máy móc; owner/ID dùng chung nhất quán.
   Mỗi module đủ core và sub, mỗi core có sub, không sub mồ côi; decomposition
   có lý do/nguồn và tách biệt relation UML. Overview chỉ gồm core lấy nguyên
   từ các module nguồn, không thiếu/thừa hoặc đổi ID/tên/owner.
3. Review hợp đồng từng UC chi tiết: trigger, điều kiện, luồng chính, lỗi/thay
   thế, kết quả; mọi nhánh có điểm rẽ và nơi tiếp tục/kết thúc.
4. Review từng relation theo modeling-rules: điểm gọi include, extension point/
   guard/return của extend, hợp đồng chung của generalization. Review association
   và actor hierarchy riêng với quyền FR.
5. Đọc lại nguồn để xác nhận mapping đúng nghĩa, đủ nhóm/FR chi tiết/BR/AUT
   thuộc scope; không có hành vi ngoài nguồn. Rà giao tiếp liên module.
6. Chạy check_us.py --final; ghi scope thực tế, lệnh, số lỗi/cảnh báo và giới hạn.
   Công cụ này không render sơ đồ và không chứng minh đầy đủ ngữ nghĩa.
7. Kiểm parser, hình xuất và consistency sơ đồ theo diagram-rules; ghi trạng
   thái thực tế, không đánh dấu pass nếu chưa thực hiện.
   Kiểm các view bắt buộc: core cho tổng quan module/hệ thống; sub cho chi
   tiết module. Có link overview ↔ module và truy vết chính–con.
   Có đúng một view detail chính cho từng core, trong hình có node core và
   đủ sub liên quan. Đối chiếu từng cạnh core–sub/sub–sub của bảng relation
   với hình; không bỏ cạnh giữa các sub hoặc vẽ thêm cạnh chưa phân tích.
8. Kiểm link tương đối, ngôn ngữ, trường còn trống và tiến độ. Không ghi metadata
   tên người thực hiện giả hoặc thời điểm phê duyệt không có bằng chứng.

Chỉ trình bản hoàn chỉnh khi không còn lỗi bắt buộc trong scope; thiếu renderer
hoặc thiếu nguồn ảnh hưởng tính đúng phải nêu rõ phần chưa hoàn tất.
Overview không được nhận là đã đặc tả sâu toàn hệ thống.

Sau review, ghi completed_steps có 7 và trạng thái **Chờ duyệt**. Gửi kết quả,
các quyết định/giới hạn còn lại và chờ xác nhận cuối. Chỉ sau người dùng đồng ý
mới ghi approved_steps có 7 và **Đã duyệt**, kèm tham chiếu xác nhận.
