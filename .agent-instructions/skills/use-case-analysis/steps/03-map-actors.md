# Bước 3 — Đặc tả luồng và kết quả

[Vietnamese Doc]

Dùng cấu trúc đặc tả của [template](../output/us-template.md) và phần luồng
trong [modeling-rules](../references/modeling-rules.md).

1. Với mỗi UC chính, viết mục tiêu bao quát, giá trị, actor, ranh giới và quy
   trình tổng quát liên hệ các UC con; không mặc định mọi con đều chạy nối tiếp.
   Với từng UC con thuộc scope chi tiết: ghi mục tiêu, subject, actor chính/
   hỗ trợ, trigger, tiền điều kiện, kết quả thành công và khi thất bại có nguồn.
2. Viết một luồng chính thành công với ID bước/anchor, ai làm gì, thông tin
   trao đổi và kết quả. Mọi bước có nguồn FR/BR hoặc diễn giải trực tiếp từ nguồn.
3. Viết nhánh thay thế/ngoại lệ: bước rẽ, guard, xử lý, nơi quay lại hoặc END
   kèm kết quả. Phương thức Email/Google không gọi là thực thi song song.
4. Đối chiếu từ chối quyền, trạng thái tài khoản/nội dung/nhóm, giới hạn,
   token/link hết hạn, AI bật/tắt/lỗi… chỉ khi FR có yêu cầu liên quan.
5. Viết BR/điều kiện dùng chung và AUT với trigger, trước/sau, quy tắc dữ liệu.
   Không tự chọn cron, giao thức, SQL, màn hình hoặc chính sách rollback.
6. Thiếu dữ liệu cần để kết luận thì ghi gap; không coi “không áp dụng” hoặc
   đoán một kết quả là cách hoàn tất template.
7. Overview hệ thống chỉ dùng brief các UC chính lấy từ module nguồn và link
   tới phân rã/đặc tả UC con, không sao chép toàn bộ luồng chi tiết.

Kiểm tra: điều kiện và trigger khác nhau; không giấu lỗi trong tiền điều kiện;
nhánh có kết thúc/quay lại; quyền/nguồn đúng; UI ở mức FR quy định. Subfunction
được tách ở bước 4 cũng phải được đặc tả tương ứng trước khi hoàn tất.

Cập nhật tiến độ và trình cổng.

