# Bước 6 — Các view và xác minh ký pháp

[Vietnamese Doc]

Đọc [diagram-rules](../references/diagram-rules.md).

1. Chọn renderer sẵn có, ghi phiên bản. Dùng UML chính thức cho bản nghiệm thu;
   flowchart minh họa phải có nhãn giới hạn.
2. Sinh overview dự án/module theo phạm vi, giữ mức mục tiêu phù hợp và owner.
3. Chọn view chi tiết cần thiết; không ép mọi UC phải có UC con hoặc dồn toàn
   module vào một hình. Giữ ID/định nghĩa xuyên view.
4. Actor ngoài boundary. Association thể hiện tương tác; quan hệ UC–UC lấy từ
   bảng quan hệ đã review, đúng source/target và ký pháp.
5. Kiểm consistency giữa catalog, đặc tả, bảng relation và mọi view; không tự
   thêm node/quan hệ chỉ trong sơ đồ.
6. Chạy parser/render thực tế theo diagram-rules; xem hình xuất, kiểm nhãn tiếng
   Việt, đầu tam giác generalization, nội dung bị cắt và chồng lấp.
7. Ghi renderer/lệnh/kết quả/đường dẫn hình trong QA. Không có renderer thì báo
   chưa kiểm tra; không ghi pass hoặc phê duyệt thay người dùng.

Kiểm tra unique ID theo **từng view**, không cấm cùng UC xuất hiện ở view khác.
Ngữ nghĩa không được đánh giá chỉ bằng parse thành công.

Cập nhật tiến độ và trình cổng.
