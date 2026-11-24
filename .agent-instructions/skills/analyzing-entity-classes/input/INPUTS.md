# Đầu vào của skill analyzing-entity-classes

Mọi đường dẫn tính từ gốc repo iShare. Thiếu một tệp **bắt buộc** thì dừng và báo người dùng.

## Nguồn

| Tệp | Vai trò | Bắt buộc |
|---|---|---|
| `.agents/.claude/system_analysis/output/fr/FR-Mxx.md` | Nguồn duy nhất của lớp, thuộc tính, quan hệ. Phải có `trang_thai: Đã chốt` | Có |
| `.agents/.claude/system_analysis/output/registers/glossary.md` | Tên tiếng Anh thống nhất của các khái niệm (QU-01) | Có |
| `.agents/.claude/system_analysis/output/data-model/ec/EC-Myy.md` của các module đã làm | Dùng lại đúng tên lớp đã có; đối chiếu lớp ngoài | Không |
| `.agents/.claude/system_analysis/output/data-model/conventions.md` | Quy ước đã được người dùng xác nhận; thắng mặc định ở `CONVENTIONS.md` | Không (tạo ở module đầu tiên) |
| `input/CONVENTIONS.md` (trong skill này) | Quy ước mặc định, nơi lưu, mã, quy tắc liên module | Có |

Register (`decisions.md`, `qa-log.md`…) và draft **không** là nguồn trực tiếp của skill này: mọi thứ trong đó đã đi
qua tài liệu FR. Chỉ mở register khi cần đọc nguyên văn một quyết định mà FR dẫn tới, hoặc để tìm quyết định về kiểu
định danh (QU-02).

## Phần nào của FR dùng ở bước nào

Số mục 5.x khác nhau giữa các module (mục "Dữ liệu nghiệp vụ" là 5.13 ở M05 nhưng 5.19 ở M03), nên tìm mục theo
**tên**, không theo số.

| Mục của FR | Dùng ở bước | Để làm gì |
|---|---|---|
| 1.1 Mục đích, 1.2 Phạm vi (phần "Trong phạm vi") | 1 | Câu mở của đoạn mô tả; biết cái gì không thuộc module |
| 4.2 Vai trò | 1, 2 | Tác nhân trong đoạn mô tả; danh từ chỉ vai trò |
| 4.4 Danh sách chức năng | 1 | Mỗi chức năng phải được ít nhất một câu nói tới (tool kiểm) |
| 5.x từng chức năng: yêu cầu cấp trên | 1 | Nội dung chính của từng câu |
| 2.1 Thuật ngữ | 2 | Quét bổ sung: tên gọi thống nhất, khái niệm có dữ liệu |
| 5.x từng chức năng: yêu cầu cấp dưới | 2, 3 | Quét bổ sung thuộc tính; căn cứ của quan hệ |
| Quy tắc nghiệp vụ (BR) | 2, 3 | Ràng buộc của thuộc tính; bội số của quan hệ (ví dụ "1–3 Topic mỗi bài") |
| Chuyển trạng thái | 2 | Thuộc tính trạng thái và tập giá trị |
| Dữ liệu nghiệp vụ (bảng thực thể, ma trận CRUD) | 2 (chỉ ở việc đối chiếu), 3 | Đối chiếu sau khi phân loại; cột "Quan hệ" là căn cứ bổ sung ở bước 3; CRUD cho biết module sở hữu và việc xóa theo |
| Giao tiếp với module khác | 1, 3 | Lớp ngoài và quan hệ liên module |
| Phụ lục B (TBD, câu hỏi) | 2 | Thứ FR đã hoãn thì không đưa vào mô hình; ghi chú ở cổng |

Thân tài liệu FR không ghi nguồn register; cột Nguồn của EC ghi **mã trong FR** (`FR-Mxx-nn`, `FR-Mxx-nn.mm`,
`BR-Mxx-nn`) hoặc `TN:<thuật ngữ>` cho một dòng ở mục 2.1 của FR. Từ mã đó, Phụ lục A của FR dẫn tiếp về register.

## Lưu ý về dữ liệu hiện tại

- Mục "Dữ liệu nghiệp vụ" của FR viết ở mức nghiệp vụ, tên tiếng Việt, và gộp nhiều thuộc tính trong một ô, ngăn
  bởi dấu chấm phẩy. Một ô có thể chứa cả thuộc tính lưu, thuộc tính tính ra và tham chiếu tới lớp khác ("tác giả").
- Một số FR ghi thực thể của module khác kèm mã, ví dụ "Người dùng (M01, M02, M08) — phần M12 dùng". Đó là lớp ngoài.
- FR có các chú thích HTML (`<!-- … -->`) ghi những thuộc tính draft từng nêu nhưng **không** đưa vào. Tôn trọng
  các chú thích đó: không đưa lại vào mô hình.
- `FR-Mxx.md` có thể đã lên phiên bản 1.1, 1.2 sau đợt rà soát chéo module. Luôn ghi đúng phiên bản vào `nguon`.
