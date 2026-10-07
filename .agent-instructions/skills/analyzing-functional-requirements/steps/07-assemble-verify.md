# Bước 7 — Hoàn thiện, kiểm và chốt

## Mục đích

Đưa tài liệu về trạng thái đọc được từ đầu đến cuối, kiểm lần cuối bằng tool và đọc lại theo từng chức năng
trước khi người dùng chốt.

## Việc làm

1. Hoàn thiện:
   - 1.1 mục đích, 1.2 phạm vi;
   - 2.1 mọi thuật ngữ dùng trong tài liệu, gồm mốc thời gian, đơn vị đếm, tên trạng thái; 2.2 viết tắt;
   - 3.1 mốc nguồn khớp `moc_nguon`; 3.2 module liên quan khớp mục Giao tiếp;
   - 4.1 "Không có." trừ khi người dùng đã nêu luật hoặc tiêu chuẩn;
   - HMI và Chuyển màn hình để "Chưa có — chờ giai đoạn thiết kế.";
   - mục 6 Lịch sử sửa đổi.
2. Chạy `lint_fr.py --final` và `trace_check.py --others .agents/.claude/system_analysis/output/fr`.
   Sửa và chạy lại, tối đa hai vòng. Lỗi còn lại sau hai vòng thì trình ở cổng, không tự che.
3. **Đối chiếu chéo module** (khi đã có FR của module khác): mỗi dòng "Dùng Myy" phải khớp một dòng
   "Cung cấp Mxx" ở FR-Myy và ngược lại; một hành vi không được viết ở cả hai tài liệu. Lệch thì ghi ở cổng,
   không tự sửa tài liệu của module khác.
4. **Đọc lại theo từng chức năng**: luồng chính và ngoại lệ đủ; ví dụ của quy tắc tính lại đúng; quyền khớp 4.3;
   không chi tiết cài đặt; mỗi câu đọc ra một nghĩa.
5. Khi người dùng nói "chốt": `trang_thai: Đã chốt`, phiên bản `1.0`, thêm dòng Lịch sử, thêm `7` vào
   `steps_completed`.

## Sửa sau khi đã chốt

Tăng phiên bản (1.1, 1.2…), trạng thái về Bản nháp, làm lại từ bước bị ảnh hưởng (nguồn mới → bước 1; đổi quyết
định → bước 2 hoặc 5), vẫn qua cổng như thường. ID không đánh lại; yêu cầu bị bỏ giữ dòng và ghi
"(Đã bỏ ở phiên bản x.y — lý do)".

## Trình ở cổng

Kết quả hai tool; WARN giữ lại kèm lý do; TBD còn lại và ảnh hưởng; kết quả đối chiếu chéo module; những chỗ bạn
thấy còn yếu khi đọc lại. Hỏi người dùng có chốt không.

## Không làm

Không đổi trạng thái sang Đã chốt khi người dùng chưa nói chốt. Không sửa tệp FR của module khác.
