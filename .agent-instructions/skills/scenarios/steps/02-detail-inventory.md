# Bước 2 — Xác định các nhóm use case chi tiết

[Vietnamese Doc]

1. Lấy toàn bộ core/sub từ catalog của US module, rồi đối chiếu decomposition,
   đặc tả và từng sơ đồ chi tiết. “UC chi tiết” trong yêu cầu này là một nhóm
   gồm **UC chính và các UC con chức năng**; scenario vẫn mang `uc` owner cụ thể.
2. Với mỗi core, liệt kê các sub, actor, mục tiêu, trigger, điều kiện trước/sau,
   FR/BR và điểm gọi/mở rộng. Giữ bảng core → sub, kể cả nhiều core cùng một sub.
3. Ghi từng UC vào bảng kiểm kê với một cách xử lý:
   - `scenario`: sở hữu mục tiêu chức năng độc lập của actor, có một hoặc
     nhiều hành trình hoàn chỉnh actor–hệ thống;
   - `embedded`: UC con/hỗ trợ được thực hiện trong scenario bao chứa;
     ghi SC và bước/nhánh cụ thể tại cột `coverage`, không tạo BF/SC riêng;
   - `aggregate`: core Summary tổng hợp các scenario con, không ép chạy mọi
     chức năng trong một giao dịch;
   - `abstract`: hợp đồng trừu tượng, trỏ tới các scenario chuyên biệt;
   - `background`: tác vụ tự động không có hành trình actor bao chứa trong
     scope; ghi nguồn, trigger, hiệu ứng và lý do ở phần quy tắc nền, không
     dựng scenario sáu phần hoặc tính vào số BF/SC;
   - `gap`: chưa xác định được mục tiêu, actor, điểm bắt đầu/kết thúc hoặc
     mâu thuẫn nguồn, ghi GAP và mức ảnh hưởng.
4. Nhãn User goal/Subfunction trong US là đầu vào để xét, không tự quyết định
   số scenario. Dùng phép kiểm ở bước 3. Một core và sub mô tả cùng hành trình
   chỉ có một SC; core dẫn tới SC đó. Một sub có thể hỗ trợ nhiều chức năng
   và phải được triển khai tại từng điểm gọi tương ứng. Một sub có mục tiêu
   độc lập thật sự vẫn có SC riêng, đồng thời có thể tham gia luồng khác.
5. Giữ mọi ID và mapping của UC dùng chung. Không tạo BF từ việc gọi hàm,
   kiểm quyền, xác thực dữ liệu hay chuyển trạng thái nội bộ. AUT/RULE được
   gắn vào bước, điều kiện, hậu điều kiện hoặc ghi chú nền có truy vết.
   Không thêm actor, nút bấm hoặc khối sáu phần phụ để hợp thức hóa tác vụ nền.

Đạt khi mọi core/sub thuộc scope đều có cách xử lý, không mất UC chỉ vì nó
không xuất hiện trên hình tổng quan toàn hệ thống. Bảng phân rã không tạo
quan hệ include/extend mới; giữ mô hình từ US.
