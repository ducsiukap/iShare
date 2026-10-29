# Bước 4 — Chốt UC con của từng UC chính và quan hệ UML

[Vietnamese Doc]

Đọc phần quan hệ của [modeling-rules](../references/modeling-rules.md) và
[ví dụ](../references/worked-example.md).

1. Review từng core và các sub ứng viên sau khi viết luồng. Chốt danh sách
   UC con cụ thể hóa mục tiêu core; mỗi core có sub, không để sub mồ côi.
2. Cập nhật bảng decomposition core → sub có nguồn và lý do. UC con dùng
   chung giữ một ID, có thể thuộc nhiều core; không nhân bản theo vị trí.
3. Phân biệt mapping chính–con với quan hệ UML. “Thuộc core” không tự thành
   include/extend/generalization; có thể tổ chức bằng package hoặc bảng phân rã.
4. Chỉ giữ một thao tác làm UC con khi có mục tiêu/hành vi đáng đặc tả riêng.
   Các phần còn lại là bước, nhánh, điều kiện/BR/AUT với truy vết đầy đủ.
5. Xét include: bước gọi, hành vi đích và nơi tiếp tục; phân biệt tiền điều kiện.
6. Xét extend: extension point thuộc base, guard, phần chèn và điểm quay lại/
   kết thúc; giải thích vì sao không chỉ dùng alternative flow.
7. Xét generalization: cha abstract/concrete, hợp đồng chung, phần chuyên biệt
   và quyền. Không dùng kế thừa chỉ vì sơ đồ có hai tầng chính–con.
8. Ghi bảng relation tách khỏi decomposition. Không cần dùng đủ ba quan hệ,
   nhưng vẫn bắt buộc đủ catalog core/sub và mapping phân rã.
   Với từng core, rà **hai nhóm cặp**: core với từng sub và các sub liên quan
   với nhau. Từ luồng, xác định UC nào gọi hành vi nào, mở rộng UC nào tại đâu,
   hoặc chuyên biệt hóa UC nào. Base/including/general có thể là một sub.
   Không mặc định mọi quan hệ đều có một đầu là core. UC con dùng chung/liên
   core được giữ cùng ID và thêm vào view như tham chiếu khi cần thấy quan hệ.
   Ghi bảng quyết định cho các cặp đã xem xét nhưng không có quan hệ UML,
   gồm lý do và cách thể hiện (nhóm, luồng hoặc tham chiếu); không bịa mũi tên.
9. Đồng bộ brief core, mọi đặc tả sub và association actor–UC; không suy quyền
   của sub chỉ từ actor gắn với core. Review cycle và nguồn.

Kiểm tra: mỗi module có hai tầng rõ; mọi sub có đặc tả; cùng ID xuyên view;
relation có bằng chứng độc lập với việc phân rã.
Mỗi core có tập node và danh sách cạnh dự kiến cho sơ đồ chi tiết của chính
core đó, bao gồm cả cạnh core–sub và sub–sub; đối chiếu nguồn và luồng cho từng cạnh.

Cập nhật tiến độ và trình cổng.
