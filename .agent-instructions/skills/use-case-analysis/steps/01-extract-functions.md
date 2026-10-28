# Bước 1 — Baseline, boundary, actor và kiểm kê

[Vietnamese Doc]

Đọc [INPUTS](../input/INPUTS.md), phần boundary/actor trong
[modeling-rules](../references/modeling-rules.md).

1. Xác nhận mode module/overview/một phần; ghi rõ yêu cầu trong và ngoài scope.
2. Kiểm tra trạng thái và phiên bản FR. Ghi nguồn, phiên bản, mốc register và
   baseline thực tế. Chỉ đọc thêm FR cần thiết để hiểu giao tiếp.
3. Xác định subject/boundary; phân biệt iShare, subsystem và dịch vụ ngoài.
4. Lập danh mục actor: ID, vai trò, loại human/external-system, quan hệ với
   boundary, nguồn. Phân biệt trạng thái/quyền với vai trò tương tác.
5. Kiểm kê nhóm FR và từng FR chi tiết/BR còn hiệu lực. Đánh dấu mã đã bỏ có
   bằng chứng; chưa phân rã tất cả thành UC.
6. Tạo/cập nhật US theo template, điền metadata, bảng nguồn/actor/phạm vi.
   Chưa có đủ dữ liệu thì ghi gap có ID, nguồn và ảnh hưởng.

Kiểm tra: đúng phạm vi; không thiếu nguồn; actor ngoài subject; không tự tạo
dịch vụ/scheduler; không sửa FR để khớp mô hình. Mode overview ghi rõ danh mục
module, không tự coi đã đặc tả chi tiết mọi UC.

Cập nhật tiến độ và trình cổng theo SKILL.md.

