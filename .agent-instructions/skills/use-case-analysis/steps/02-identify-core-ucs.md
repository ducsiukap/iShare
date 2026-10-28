# Bước 2 — Mục tiêu và danh mục use case

[Vietnamese Doc]

Đọc phần mức mục tiêu/tách UC của [modeling-rules](../references/modeling-rules.md).

1. Từ mỗi actor, hỏi công việc/kết quả nào có giá trị; đọc FR để kiểm chứng.
2. Lập ứng viên, mức Summary / User goal / Subfunction, actor chính/hỗ trợ,
   owner, kết quả và căn cứ. Không đặt số lượng UC hoặc số FR tối thiểu.
3. Với từng nhóm FR, quyết định UC độc lập, bước, nhánh, điều kiện/BR hoặc AUT.
   Ghi lý do giữ/gộp/tách. Không tự dựng quan hệ UML ở bước này.
4. Giữ mục tiêu độc lập ở danh mục ngay cả khi ngắn: ví dụ Đăng xuất.
   “Quản lý mật khẩu” có thể là package; không tự ép thành cha của mọi thao tác.
5. Tái sử dụng ID trong overview/US liên quan; UC dùng chung có một owner.
   Ghi dependency liên module, không nhân bản UC theo view.
6. Điền catalog. Ghi một anchor đặc tả ổn định cho mỗi UC; Summary có thể chỉ
   cần brief hợp đồng/mục tiêu và tham chiếu, không buộc fully dressed.

Kiểm tra: các UC cùng view có mức phù hợp; mục tiêu không bị thay bằng nhập
trường/mở form; không mất UC độc lập vì không “đủ lớn”. Mỗi FR kiểm kê có
hướng biểu diễn nhưng chưa được ghi “Đủ” khi chưa có nội dung đích.

Cập nhật tiến độ và trình cổng. Sơ đồ chính thức thực hiện sau bước quan hệ.
