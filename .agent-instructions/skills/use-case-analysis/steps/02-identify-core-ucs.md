# Bước 2 — Xác định UC chính và UC con ứng viên trên từng module

[Vietnamese Doc]

Đọc phần mức mục tiêu/phân rã của [modeling-rules](../references/modeling-rules.md).

1. Với từng module trong scope, tìm các mục tiêu/năng lực nghiệp vụ bao quát từ
   actor và FR, ghi thành **UC chính** (tier=core), actor, giá trị, kết quả,
   ranh giới, owner và nguồn. Đây là các UC dùng để tổng hợp toàn hệ thống.
2. Đề xuất các **UC con** (tier=sub) cụ thể hóa từng UC chính: mục tiêu/hành vi
   gắn kết có nguồn, không phải từng nút/field UI. Mỗi module phải có hai tầng;
   không đặt quota số UC chính hoặc số UC con.
3. Ghi level Summary / User goal / Subfunction riêng với tier. Không mặc định
   core=Summary, sub=Subfunction. Giữ các mục tiêu độc lập như Đăng xuất ở tầng
   phù hợp; có thể thuộc UC chính quản lý phiên nhưng không extend Đăng nhập.
4. Lập bảng decomposition ứng viên core → sub. Mỗi core có ít nhất một sub,
   mỗi sub thuộc ít nhất một core. Giải thích đóng góp vào mục tiêu; mapping
   không tự sinh quan hệ include/extend/generalization.
5. Tái sử dụng UC dùng chung bằng một ID và nhiều dòng mapping; có owner rõ.
   Phân biệt hành vi cần đặc tả bằng bước, điều kiện/BR/AUT với UC con thật.
6. Điền catalog có tier và level, anchor ổn định. Ghi brief/quy trình tổng quát
   cho core; chuẩn bị đặc tả chi tiết các sub ở bước 3.
7. Nếu đang tổng hợp overview, lấy các dòng core từ US module đã xác định,
   giữ nguyên ID/tên/owner và ghi module-models; không phân tích lại thành bộ
   core khác. Module chưa có mô hình được ghi thiếu, không bịa thay thế.

Kiểm tra: từng module có cả core/sub, core có mục tiêu rõ, sub có căn cứ,
mapping đủ hai chiều; không biến quota hoặc package thành luật UML.

Cập nhật tiến độ và trình cổng.
