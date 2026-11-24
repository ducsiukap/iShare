# Gộp hệ thống — Cơ sở dữ liệu toàn hệ thống (DB-SYS)

Chạy khi mọi module đã chốt `DB-Mxx.md` và `CD-SYS.md` đã chốt. Đây là lượt gộp cuối trong ba:
`EC-SYS.md` → `CD-SYS.md` → **`DB-SYS.md`**. Mỗi việc lớn (A, B, C) là một bước có cổng.

## Mục đích

Một lược đồ cơ sở dữ liệu cho cả hệ thống: mỗi bảng khai một lần; mọi khóa ngoại trỏ tới một bảng có thật, đúng
khóa chính, đúng kiểu; không còn dữ liệu dư thừa **xuyên module**; có sơ đồ quan hệ toàn hệ thống.

## Đầu vào

`CD-SYS.md` (Đã chốt); `EC-SYS.md` (bảng quyết định gộp `MD-nn`); mọi `DB-Mxx.md` (Đã chốt);
`data-model/conventions.md`.

## Việc làm

### A. Kiểm kê và tìm điểm lệch

1. Kiểm mọi module có `DB-Mxx.md` ở trạng thái Đã chốt và `nguon` khớp phiên bản `CD-Mxx.md` hiện tại (các CD có
   thể đã lên phiên bản sau hai lượt gộp trước). Module nào lệch thì cập nhật `DB` của module đó trước, qua cổng.
2. Chạy `merge_db.py --dir $M/db --out-md $M/db/.work/merge-db.md`. Tệp sinh ra có lược đồ hợp nhất (từ mục 6.1 của
   từng module), danh sách cột và bảng đã loại, danh sách cột dẫn xuất được giữ, và các điểm lệch.
3. Xét từng điểm lệch tool nêu, và tự tìm thêm:

   | Điểm lệch | Tool thấy? | Cách xét |
   |---|---|---|
   | Một bảng khai ở nhiều module | Có | Giữ ở module sở hữu lớp (theo `CD-SYS`); module kia chỉ tham chiếu |
   | Khóa ngoại trỏ tới bảng chưa module nào khai | Có | Thường do khác tên bảng, hoặc bảng đích đã bị loại ở bước 5 của module sở hữu |
   | Bảng ngoài được tham chiếu nhưng đã bị loại ở module sở hữu (bảng thống kê) | Có | Xét lại: module kia cần gì ở bảng đó; thường phải đổi sang tham chiếu bảng gốc |
   | Khóa ngoại lệch kiểu với khóa chính được tham chiếu | Có | Sửa về kiểu của khóa chính |
   | Khóa ngoại đề nghị cho bảng của module khác (mục 7.2) | Có (liệt kê, kèm đã có hay chưa) | Đưa cột vào bảng đích; kiểm không trùng tên và kiểu đúng |
   | Cột cùng tên ở nhiều bảng | Có (gợi ý) | Áp phép thử trùng lặp của bước 5: cùng đối tượng, cùng dữ liệu, lấy được qua khóa ngoại → loại một bên |
   | Cột khác tên nhưng cùng dữ liệu ở hai module | Không | Soát theo cột "Từ thuộc tính" và nghĩa của thuộc tính ở `CD-SYS` |
   | Cột dẫn xuất mà nguồn tính nằm ở **module khác** (bộ đếm ở module này tính từ bảng của module kia) | Không | Áp phép thử dẫn xuất của bước 5 trên lược đồ toàn hệ thống |
   | Cột được module này giữ như dẫn xuất-phải-lưu trong khi module kia đã lưu đúng dữ liệu đó | Không | Giữ một nơi |
   | Quan hệ 1-1 xuyên module có thể gộp bảng | Không | Áp tiêu chí gộp/tách của bước 3; mặc định tách khi khác module, ghi lý do |
   | Quyết định `MD-nn` của hai lượt gộp trước chưa được áp (đổi tên lớp → đổi tên bảng; quan hệ mới `R-SYS-nn` → khóa ngoại mới) | Không | Áp từng quyết định; quan hệ mới phải qua bước 3 và 4 |

4. Ghi mỗi điểm lệch thành một dòng ở mục 8 "Quyết định gộp" của `DB-SYS.md` (quyết định đã có ở lượt trước thì dẫn
   lại đúng mã `MD-nn`).

**Cổng A:** trình điểm lệch và đề xuất.

### B. Dựng bản hợp nhất

1. Tạo `DB-SYS.md` từ `output/db-system-template.md` (`module: SYS`). Số mục giữ giống tài liệu module (1, 2.1, 2.2,
   3, 4.1, 4.2, 5.1–5.4, 6) để tool đọc được.
2. Ghi các bảng sau khi áp quyết định. Ở bản hệ thống không còn bảng ngoài: mục 7.1 và 7.2 để trống; mọi khóa ngoại
   đề nghị đã nằm ở mục 4.2 của bảng đích.
3. Mục 5 gom lại toàn bộ cột và bảng đã loại ở các module, cộng những gì loại thêm ở lượt gộp (ghi rõ "loại khi gộp,
   `MD-nn`").
4. Chạy `build_schema.py --db $M/db/DB-SYS.md` (dựng mục 6.1, sinh `diagrams/DB-SYS.puml`, `.png` và nhúng ảnh vào
   mục 6.2) và
   `check_db.py --db $M/db/DB-SYS.md --system --final --cd $M/cd/CD-SYS.md`.

**Cổng B:** trình lược đồ toàn hệ thống (số bảng, số khóa ngoại), sơ đồ, và các thay đổi so với tài liệu module.

### C. Đưa thay đổi về tài liệu module và chốt

Liệt kê thay đổi cần làm ở từng `DB-Mxx.md`; người dùng đồng ý thì sửa từng tệp, tăng phiên bản, dẫn `MD-nn`, chạy
lại `build_schema.py` và `check_db.py --final` cho tệp đó. Người dùng nói "Chốt DB-SYS" thì chốt.

## Tự kiểm

- Mỗi lớp của `CD-SYS.md` có bảng, hoặc có dòng ở mục 5.2 nêu vì sao bị loại.
- Mỗi quan hệ thành phần – toàn thể của `CD-SYS.md` có đúng một khóa ngoại.
- Mọi khóa ngoại: bảng đích có trong lược đồ, cột đích là khóa chính, kiểu bằng nhau.
- Mọi dòng "Cách có lại giá trị" chỉ dùng cột có trong lược đồ cuối toàn hệ thống.
- Không còn bảng nào chỉ có khóa và một khóa ngoại.

## Không làm

Không tự quyết giữ hay loại cột dẫn xuất mà FR đòi lưu. Không sửa tài liệu module khi chưa được duyệt. Không viết
DDL, chỉ mục, trừ khi người dùng yêu cầu riêng.
