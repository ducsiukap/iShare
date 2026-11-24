# Đầu vào của skill designing-database

Mọi đường dẫn tính từ gốc repo iShare. Thiếu một tệp **bắt buộc** thì dừng và báo người dùng.

| Tệp | Vai trò | Bắt buộc |
|---|---|---|
| `.agents/.claude/system_analysis/output/data-model/cd/CD-Mxx.md` | Đầu vào duy nhất về lớp, thuộc tính, kiểu, quan hệ. Phải có `trang_thai: Đã chốt` | Có |
| `.agent-instructions/skills/analyzing-entity-classes/input/CONVENTIONS.md` | Quy ước mặc định QU-06…QU-09; quy tắc liên module | Có |
| `.agents/.claude/system_analysis/output/data-model/conventions.md` | Quy ước đã được người dùng xác nhận; thắng giá trị mặc định | Không (bổ sung ở module đầu tiên) |
| `.agents/.claude/system_analysis/output/data-model/ec/EC-Mxx.md` | Cột "Ràng buộc nguồn nêu" của thuộc tính dẫn xuất (công thức), dùng ở bước 5 | Có |
| `.agents/.claude/system_analysis/output/fr/FR-Mxx.md` | Đọc nguyên văn quy tắc khi cần xác định một thuộc tính dẫn xuất có bị FR yêu cầu lưu không | Có |
| `.agents/.claude/system_analysis/output/data-model/db/DB-Myy.md` của các module đã làm | Tên bảng, khóa chính và kiểu của bảng ngoài | Không |

## Phần nào của CD dùng ở bước nào

| Mục của CD-Mxx.md | Dùng ở bước | Để làm gì |
|---|---|---|
| 1 Lớp và id (Nhóm, Sở hữu, Lớp cha, id) | 1, 4 | Mỗi lớp của module một bảng; lớp ngoài thành bảng ngoài; lớp con dùng khóa của lớp cha |
| 2.1 Thuộc tính (Kiểu, Bắt buộc, Ràng buộc, Tính chất) | 2, 5 | Cột, kiểu cột, null, duy nhất; thuộc tính Dẫn xuất |
| 2.2 Kiểu liệt kê | 2 | Giá trị cho phép của cột |
| 3.1 Quan hệ thành phần – toàn thể (bội số, dạng) | 3, 4 | Quan hệ giữa các bảng; vị trí và tính null của khóa ngoại |
| 3.2 Quan hệ giữ nguyên | 3, 4 | Kế thừa → bảng cha–con; Phụ thuộc → không sinh quan hệ bảng |
| 4 Thuộc tính đối tượng | 2 | Không chuyển thành cột; ghi lại ở mục 2.2 của DB |
| 6 Liên module | 1, 4 | Bảng ngoài; khóa ngoại đề nghị |

## Lưu ý

- "Dạng" ở CD đọc theo thứ tự **thành phần–toàn thể**. Ở DB, "Dạng" đọc theo thứ tự **Bảng A–Bảng B** và luôn viết
  bảng phía 1 trước cho quan hệ 1-n. Bảng dưới đây dùng để đổi:

  | Dạng ở CD (thành phần–toàn thể) | Bảng phía 1 | Bảng phía n (có khóa ngoại) |
  |---|---|---|
  | `n-1` | bảng của lớp toàn thể | bảng của lớp thành phần |
  | `1-n` | bảng của lớp thành phần | bảng của lớp toàn thể |

- Register của dự án có sẵn một số tên bảng, cột kiểu snake_case từ giai đoạn phỏng vấn (`post_topics`,
  `conversation_members`, `last_read_message_id`). Quy ước của dự án cũng là snake_case, nên khi một lớp hoặc thuộc
  tính ứng đúng với thứ register đã gọi tên thì dùng lại tên đó. Nhưng register **không** là đầu vào để thêm bảng hay
  cột: bảng chỉ sinh từ lớp, cột chỉ sinh từ thuộc tính của `CD-Mxx.md`.
