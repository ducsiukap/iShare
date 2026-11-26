# Bước 1 — Xác định module

[Vietnamese Doc]

1. Lấy Mxx/tên module từ yêu cầu và module-registry. Nếu người dùng nêu UC,
   suy module từ owner của UC. Chỉ hỏi khi vẫn có nhiều phạm vi hợp lý.
2. Đọc [đầu vào](../input/INPUTS.md); ghi mục tiêu hệ thống, boundary, scope
   toàn module hoặc danh sách UC được chọn, out-of-scope và baseline.
3. Đọc tổng quan hệ thống, tổng quan module, danh mục actor và các quyền liên
   quan. M01–M16 là phần bên trong iShare, không phải actor bên ngoài.
4. Kiểm tra trạng thái FR/US, mâu thuẫn, GAP đã có và bản scenario đang làm.
   Nguồn Chờ duyệt chỉ cho scenario nháp; không sửa dấu phê duyệt của nguồn.
5. Xác định gốc bộ đầu vào và thư mục `scenarios` cùng cấp với `fr`/`us`
   theo [đầu vào](../input/INPUTS.md), rồi chọn thư mục con `Mxx` theo mã FR.
   Chỉ tạo thư mục của module đang triển khai khi cần ghi đầu ra, không tạo
   sẵn thư mục các module khác; tìm bản đang làm
   tại đích chung trước khi xét bản workspace cũ. Ghi `output_dir` vào metadata.
6. Tạo/tiếp tục một file từ [template](../output/scenario-template.md), ghi
   phạm vi chưa đủ dữ liệu. Tài liệu mẫu dùng để đối chiếu ranh giới hành
   trình actor và cách trình bày, không cung cấp yêu cầu sản phẩm mới.

Đạt khi module/owner và phạm vi rõ, xác định được nguồn sẽ dùng và những phần
còn thiếu. Khi một UC bị chặn, vẫn có thể làm bước sau cho các UC độc lập.
