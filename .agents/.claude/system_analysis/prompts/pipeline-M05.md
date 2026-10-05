Bạn là người điều phối quy trình SR của iShare. Thư mục hiện tại là gốc repo.
Đọc .agent-instructions/COMMON-RULES.md, rồi .agent-instructions/system_analysis/shared/SR-DOCUMENT-RULES.md (đặc biệt §8 và §10).
Chạy script bằng Python 3 (thử `python3`, nếu không có thì `python`).

Nhiệm vụ: đưa module M05 qua quy trình Author → Auditor vòng 1 → sửa → Auditor vòng 2.

Giai đoạn 1, Author: làm trực tiếp trong phiên này vì cần hỏi tôi. Đọc và làm theo
.agent-instructions/system_analysis/roles/sr-author/AGENT.md từ Bước 0 đến Bước 8.
Hỏi tôi mỗi lần MỘT vấn đề; chỉ ghi register sau khi tôi xác nhận.

Giai đoạn 2, Auditor vòng 1: sau Bước 8, khởi chạy MỘT subagent mới (ngữ cảnh sạch). Prompt gửi cho subagent chỉ gồm nội dung theo mẫu
.agent-instructions/system_analysis/shared/templates/audit-invocation-prompt.md (Mxx=M05, vòng 1, gốc repo là thư mục hiện tại).
TUYỆT ĐỐI không đưa vào prompt đó tóm tắt, nhận định, tên tệp làm việc hay bất kỳ nội dung nào từ phần Author.
Subagent chỉ được ghi vào specs/audit/. Khi nó trả về, tóm tắt báo cáo cho tôi (kết luận, số finding, các vấn đề cần tôi quyết).

Giai đoạn 3, sửa: nếu kết luận là Chưa đạt, quay lại chế độ sửa của sr-author trong phiên này.
DEFECT thì sửa; CONFLICT, GAP, OBSERVATION thì hỏi tôi từng cái một, ghi register sau khi tôi xác nhận, rồi sửa SR. Điền lại selfcheck, tăng phiên bản.

Giai đoạn 4, Auditor vòng 2: như giai đoạn 2, nhưng vòng 2 và nêu đường dẫn báo cáo vòng 1.

Dừng sau vòng 2, không mở vòng 3. Báo cho tôi kết quả cuối. Không tự đổi trạng thái sang Đã chốt, không chuyển tài liệu sang docs/approved.

Quy tắc điều phối: dừng và chờ tôi ở mọi câu hỏi và trước mọi lần ghi register. Sau mỗi giai đoạn, thêm mục "Phản hồi về skill": chỗ nào trong skill hoặc rules mơ hồ, thiếu chi tiết hoặc phải tự quyết.
