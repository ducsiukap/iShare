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
| QU-02 | Thuộc tính định danh | | Cổng bước 1, CD-Mxx | |
| QU-03 | Tên thuộc tính | camelCase, tiếng Anh | Người dùng chốt khi dựng skill | 2026-11-15 |
| QU-04 | Kiểu thuộc tính (Java) | | Cổng bước 2, CD-Mxx | |
| QU-05 | Thuộc tính đối tượng | | Cổng bước 4, CD-Mxx | |
| QU-06 | Tên bảng | snake_case của tên lớp, số nhiều (`PostTopic` → `post_topics`) | Người dùng chốt khi dựng skill | 2026-11-15 |
| QU-07 | Tên cột | snake_case của tên thuộc tính | Người dùng chốt khi dựng skill | 2026-11-15 |
| QU-08 | Tên khóa ngoại | snake_case, kết thúc bằng `_id`; cách ghép tên: (chờ xác nhận ở cổng bước 1, DB-Mxx) | Người dùng chốt snake_case khi dựng skill | 2026-11-15 |
| QU-09 | Kiểu cột (PostgreSQL) | | Cổng bước 1, DB-Mxx | |
| QU-10 | Sơ đồ | | Cổng bước 1, EC-Mxx | |
| QU-11 | Bội số | | Cổng bước 1, EC-Mxx | |
