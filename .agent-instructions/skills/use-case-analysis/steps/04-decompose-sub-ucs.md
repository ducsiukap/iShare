# Bước 4 — Tách hành vi và chứng minh quan hệ

[Vietnamese Doc]

Đọc phần quan hệ của [modeling-rules](../references/modeling-rules.md) và
[ví dụ](../references/worked-example.md). Không dùng US-M01 cũ làm đáp án chuẩn.

1. Review các bước/nhánh đã viết: chỉ tách UC khi có mục tiêu độc lập, tái sử
   dụng hoặc lợi ích rõ về độ hiểu/độ phức tạp; ghi cả quyết định “giữ trong luồng”.
2. UC hỗ trợ mới có ID ổn định, nguồn, hợp đồng và đặc tả; không cần actor
   trực tiếp khởi tạo hoặc tạo thêm actor giả.
3. Xét include: chỉ ra bước gọi hành vi, đích và cách tiếp tục. Phân biệt với
   tiền điều kiện và quan hệ thứ tự.
4. Xét extend: khai báo extension point của base, vị trí bước, guard, phần bổ
   sung và điểm trở lại/kết thúc; giải thích vì sao alternative flow chưa đủ.
5. Xét generalization: xác định cha abstract/concrete, phần hợp đồng/hành vi
   chung, phần chuyên biệt và quyền. Package/CRUD không tự sinh kế thừa.
6. Lập association actor–UC theo tương tác thực tế. Actor generalization nếu
   có phải được giải thích và đối chiếu quyền, không tự coi là RBAC.
7. Ghi quan hệ ở bảng riêng có source/target độc lập với nhãn “chính/con”.
   Không cần dùng đủ include/extend/generalization. Quan hệ không chứng minh
   được: giữ luồng hoặc ghi gap, không chọn loại gần đúng để đủ sơ đồ.
8. Đồng bộ đặc tả sau tách: thay bước tương ứng bằng lời gọi có điểm vào/ra;
   tránh mô tả hai lần có kết quả mâu thuẫn.

Kiểm tra: đúng chiều; không include login chỉ vì cần có phiên; không extend
logout từ login đã kết thúc; không “Gõ @” thành UC theo mặc định; không cho
actor rộng quyền vào mọi specialized UC. Review cycle và giả định kế thừa.

Cập nhật tiến độ và trình cổng.
