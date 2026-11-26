# Bước 4 — Viết và kiểm tra scenario

[Vietnamese Doc]

1. Với **mỗi BF**, điền một scenario theo đúng sáu phần của
   [template](../output/scenario-template.md). Tên cụ thể mục tiêu/phương thức,
   actor đúng US, tiền điều kiện không giấu các lỗi cần xét, hậu điều kiện
   phân biệt từng kết quả. Bước đầu là hành động của actor chính trong BF;
   bước cuối luồng chính là SYSTEM trả kết quả hoàn tất mục tiêu SUCCESS.
   Kiểm lại phép kiểm BF ở bước 3 trước khi viết, không viết sáu phần cho
   ứng viên `embedded`/`background` chỉ để bao phủ ID.
2. Viết luồng chính theo một bộ dữ liệu hợp lệ. Mỗi sự kiện một chủ thể, nêu
   hành động, dữ liệu và phản hồi/hiệu ứng quan sát được. Gộp các xử lý liên
   tiếp cùng chủ thể thành một lượt; không thêm hành động giả để xen kẽ.
3. Mỗi nhánh hệ thống hoặc lựa chọn người dùng trong mục 6 có bước bị thay
   thế (`at`), guard, các sự kiện tiếp nối, đích nhập lại/kết thúc. Rà các
   lựa chọn tiếp sau lỗi; không bỏ lửng nhánh hủy hoặc thử lại.
4. Đi từ đầu đến cuối từng đường: tiền điều kiện → bước → guard → nhánh →
   nhập lại → hậu điều kiện. Kiểm luân phiên cả ở điểm rẽ và nhập lại.
   Kiểm dữ liệu được nhập/hiển thị/lưu còn cùng một đối tượng và đúng BR.
   Tự hỏi “Actor còn bắt buộc làm gì để xong chức năng đã đặt tên?” Nếu còn,
   triển khai tiếp; không dùng END:SUCCESS/HANDED_OFF cho trạng thái giữa.
5. Mở rộng các lời gọi UC con vào đường đi khi cần kiểm; không dùng câu
   “thực hiện UC-X” để che hết tương tác. Kiểm cả return thành công và thất
   bại từ UC được gọi; xem [quy tắc](../references/scenario-rules.md).
6. Chạy [validator](../tools/README.md) với FR/US đã dùng. Sửa lỗi cấu trúc,
   subject, đích bước và coverage. Tool không chứng minh nguồn đủ ngữ nghĩa:
   đối chiếu lại mọi FR/BR, UC, BF và từng lựa chọn với các bảng truy vết.
7. Ghi số UC scenario/embedded/aggregate/abstract/background/GAP, BF, SC và
   nhánh. Tách số quy tắc nền khỏi số scenario. Nêu phần thiếu,
   các tổ hợp loại trừ/lớp tương đương, kết quả tool và review nghiệp vụ.
   Lưu SC và QA (nếu có) vào `<base>/scenarios/Mxx/`; gốc scenarios cùng cấp với FR/US đầu vào,
   kể cả bản soạn; giữ đúng trạng thái, không phê duyệt hộ người dùng. Khi
   đưa bản cũ từ workspace sang đích, cập nhật và kiểm các link tương đối
   tới FR/US/skill/QA theo vị trí mới. Bàn giao bằng link file tại đích đó.

Kết quả hoàn chỉnh đòi hỏi: tất cả UC trong scope có disposition; tất cả BF
là chức năng actor–hệ thống hoàn chỉnh và có scenario; tất cả nhánh có đường
kết thúc; sáu phần và dữ liệu đầy đủ;
không có hành vi mới vô nguồn; không có GAP chặn bị che bằng câu chung chung.
