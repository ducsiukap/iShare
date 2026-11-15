# Đầu vào của skill designing-entity-classes

Mọi đường dẫn tính từ gốc repo iShare. Thiếu một tệp **bắt buộc** thì dừng và báo người dùng.

| Tệp | Vai trò | Bắt buộc |
|---|---|---|
| `.agents/.claude/system_analysis/output/data-model/ec/EC-Mxx.md` | Đầu vào duy nhất về lớp, thuộc tính, quan hệ. Phải có `trang_thai: Đã chốt` | Có |
| `.agent-instructions/skills/analyzing-entity-classes/input/CONVENTIONS.md` | Quy ước mặc định QU-02, QU-04, QU-05; quy tắc liên module | Có |
| `.agents/.claude/system_analysis/output/data-model/conventions.md` | Quy ước đã được người dùng xác nhận; thắng giá trị mặc định | Không (bổ sung ở module đầu tiên) |
| `.agents/.claude/system_analysis/output/fr/FR-Mxx.md` | Đọc nguyên văn một yêu cầu hoặc quy tắc khi cột "Ràng buộc nguồn nêu" của EC chưa đủ để chọn kiểu | Có |
| `.agents/.claude/system_analysis/output/data-model/cd/CD-Myy.md` của các module đã làm | Dùng lại kiểu id, kiểu liệt kê, kiểu thuộc tính cho thống nhất | Không |
| `.agents/.claude/system_analysis/output/registers/decisions.md` | Chỉ để tìm quyết định đã có về kiểu định danh, múi giờ (DEC-127), định dạng nội dung | Không |

## Phần nào của EC dùng ở bước nào

| Mục của EC-Mxx.md | Dùng ở bước | Để làm gì |
|---|---|---|
| 2.2 Lớp (Nhóm, Sở hữu) | 1 | Lập bảng lớp; biết lớp nào là lớp ngoài, lớp thống kê |
| 3.4 Quan hệ, các dòng Kế thừa | 1 | Lớp con không thêm id |
| 2.3 Thuộc tính (Tính chất, Ràng buộc nguồn nêu, Nguồn) | 2 | Chọn kiểu, tính bắt buộc, ràng buộc |
| 3.3 Lớp liên kết | 3 | Mẫu chuyển "A + B → C" |
| 3.4 Quan hệ (bội số, loại, bên chính) | 3, 4 | Chuyển loại; xác định dạng thành phần–toàn thể |
| 5 Liên module | 1, 4 | Lớp ngoài; thuộc tính đối tượng rơi vào lớp ngoài |

## Lưu ý

- Bội số ở EC ghi theo "Lớp A / Lớp B". Ở CD, bội số ghi theo "thành phần / toàn thể". Khi chuyển, giữ nguyên con
  số, chỉ đổi cột; tool đối chiếu lại với EC.
- Thuộc tính Dẫn xuất và lớp Thống kê **vẫn được giữ** ở bước thiết kế lớp, kèm kiểu. Chúng chỉ bị loại ở bước 5 của
  skill `designing-database`.
