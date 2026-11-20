# Quy ước mô hình dữ liệu đã xác nhận

<!-- [Vietnamese Doc] Mẫu của tệp `.agents/.claude/system_analysis/output/data-model/conventions.md`.
     Tệp này chỉ ghi những quy ước người dùng ĐÃ xác nhận ở cổng. Giá trị ở đây thắng giá trị mặc định trong
     `.agent-instructions/skills/analyzing-entity-classes/input/CONVENTIONS.md` (mục 4).
     Quy ước chưa có dòng ở đây thì chưa được xác nhận: skill phải trình ở cổng trước khi dùng cho cả dự án.
     Không sửa một dòng đã xác nhận; quy ước đổi thì thêm dòng mới ghi rõ thay cho dòng nào, và rà lại các tài liệu
     đã chốt bị ảnh hưởng. -->

| Mã | Về việc gì | Giá trị đã xác nhận | Xác nhận ở | Ngày |
|---|---|---|---|---|
| QU-01 | Tên lớp | PascalCase, tiếng Anh, số ít | Người dùng chốt khi dựng skill | 2026-11-15 |
| QU-02 | Thuộc tính định danh | Tên `id`, kiểu `long`; chỉ lớp không kế thừa (lớp liên kết cũng có id riêng); register chưa có quyết định nào về kiểu định danh | Người dùng xác nhận trước khi làm CD-M01 | 2026-11-20 |
| QU-03 | Tên thuộc tính | camelCase, tiếng Anh | Người dùng chốt khi dựng skill | 2026-11-15 |
| QU-04 | Kiểu thuộc tính (Java) | Chữ: `String` (kể cả nội dung giàu định dạng JSON của Tiptap). Số nguyên: `int` (đếm, thứ tự, ngưỡng nhỏ), `long` (id, số có thể rất lớn). Số thực (điểm, tỷ lệ): `double`. Đúng/sai: `boolean`. Thời điểm: `Instant` (lưu UTC, tính mốc và hiển thị theo giờ Việt Nam, DEC-127). Ngày không giờ (mốc đầu tuần, tháng; ngày đạt) cũng ghi `Instant` là mốc 00:00 giờ Việt Nam, không dùng `LocalDate`, cho thống nhất (người dùng chọn khi trả lời CD-M12 Q-01, 2026-11-20). Tập giá trị cố định nguồn liệt kê đủ: kiểu liệt kê (enum) PascalCase, giá trị HOA_GẠCH_DƯỚI. Mở rộng: vector embedding `float[]` (pgvector); số liệu thống kê đếm theo nhóm `Map<K, Integer>` (K là kiểu liệt kê hoặc kiểu của nhóm); xu hướng theo thời gian `Map<Instant, Integer>` (mốc đầu mỗi giờ, ngày hoặc tháng → số lượng). Tool báo WARN "kiểu lạ" cho `float[]`, `Map<…>`: giữ lại, lý do QU-04 | Người dùng xác nhận trước khi làm CD-M01 | 2026-11-20 |
| QU-05 | Thuộc tính đối tượng | camelCase. Một đối tượng: tên lớp thành phần (`client : Client`). Danh sách: kiểu **`List<X>`** (thay ký pháp `X[]` của phương pháp), tên số nhiều (`postTopics : List<PostTopic>`). Hai thuộc tính cùng kiểu trong một lớp thì đặt theo vai trò trong FR (`author`, `lockedBy`), không đánh số; không trùng tên thuộc tính đã có. `check_cd.py`, `merge_cd.py` chấp nhận `List<X>` | Người dùng xác nhận trước khi làm CD-M01 | 2026-11-20 |
| QU-06 | Tên bảng | snake_case của tên lớp, số nhiều (`PostTopic` → `post_topics`) | Người dùng chốt khi dựng skill | 2026-11-15 |
| QU-07 | Tên cột | snake_case của tên thuộc tính | Người dùng chốt khi dựng skill | 2026-11-15 |
| QU-08 | Tên khóa ngoại | snake_case, kết thúc bằng `_id`; cách ghép tên: (chờ xác nhận ở cổng bước 1, DB-Mxx) | Người dùng chốt snake_case khi dựng skill | 2026-11-15 |
| QU-09 | Kiểu cột (PostgreSQL) | | Cổng bước 1, DB-Mxx | |
| QU-10 | Sơ đồ | Mã PlantUML do tool `gen_puml.py` sinh từ các bảng; không viết tay, không sửa tay | Cổng bước 1, EC-M05 | 2026-11-16 |
| QU-11 | Bội số | Viết `1`, `0..1`, `0..*`, `1..*`, hoặc khoảng cụ thể (`1..3`) khi quy tắc nghiệp vụ nêu số | Cổng bước 1, EC-M05 | 2026-11-16 |
| QU-10 | Sơ đồ (thay dòng QU-10 ngày 2026-11-16) | Tool sinh mã PlantUML từ các bảng vào tệp riêng `diagrams/<mã tài liệu>.puml` cạnh tài liệu, render thành `diagrams/<mã tài liệu>.png`; tài liệu chỉ nhúng ảnh PNG kèm liên kết tới tệp `.puml`, không chép mã PlantUML; không viết tay, không sửa tay | Góp ý của người dùng sau lần chạy thử EC-M05 | 2026-11-17 |
