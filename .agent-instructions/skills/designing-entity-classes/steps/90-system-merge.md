# Gộp hệ thống — Thiết kế lớp toàn hệ thống (CD-SYS)

Chạy khi mọi module đã chốt `CD-Mxx.md` và `EC-SYS.md` đã chốt, **trước khi** bắt đầu skill `designing-database`
(xem `../analyzing-entity-classes/input/CONVENTIONS.md` mục 1). Mỗi việc lớn (A, B, C) là một bước có cổng.

## Mục đích

Một sơ đồ lớp thiết kế cho cả hệ thống: tập lớp, thuộc tính, quan hệ đúng như `EC-SYS.md`; kiểu thống nhất; mỗi quan
hệ thành phần – toàn thể một thuộc tính đối tượng; thuộc tính đối tượng mà các module đề nghị cho lớp của module
khác đã nằm đúng lớp.

## Đầu vào

`EC-SYS.md` (Đã chốt) kèm bảng quyết định gộp `MD-nn`; mọi `CD-Mxx.md` (Đã chốt); `data-model/conventions.md`.

## Việc làm

### A. Kiểm kê và tìm điểm lệch

1. Kiểm mọi module có `CD-Mxx.md` ở trạng thái Đã chốt và `nguon` khớp phiên bản `EC-Mxx.md` hiện tại (các EC có
   thể đã lên phiên bản sau lượt gộp EC). Module nào lệch thì cập nhật `CD` của module đó trước, qua cổng.
2. Chạy `merge_cd.py --dir $M/cd --out-md $M/cd/.work/merge-cd.md`.
3. Xét từng điểm lệch tool nêu, và tự tìm thêm:

   | Điểm lệch | Tool thấy? | Cách xét |
   |---|---|---|
   | Kiểu id không thống nhất | Có | Phải về một kiểu theo QU-02 |
   | Một thuộc tính khai ở nhiều module, khác kiểu | Có | Chọn theo module sở hữu lớp; khác biệt có nghĩa thì hỏi |
   | Kiểu liệt kê cùng tên khác giá trị | Có | Hợp các giá trị nếu cùng một tập; khác tập thì đổi tên một kiểu |
   | Cùng loại dữ liệu khác kiểu giữa các module (thời điểm lúc `Instant` lúc `LocalDate`) | Không | Soát theo QU-04 |
   | Kiểu liệt kê khác tên nhưng cùng tập giá trị | Không | Gộp thành một kiểu |
   | Thuộc tính đối tượng đề nghị cho lớp của module khác | Có | Đưa vào lớp của module sở hữu; kiểm không trùng tên |
   | Tham chiếu vòng qua nhiều module (A chứa B ở module này, B chứa A ở module kia) | Có | Xét lại bên toàn thể của một trong hai quan hệ |
   | Quan hệ khai ở nhiều module, khác bên toàn thể hoặc loại | Có | Một quan hệ một dòng; chọn theo căn cứ FR, hỏi nếu hai bên đều có căn cứ |
   | Quyết định `MD-nn` của `EC-SYS` chưa được áp (đổi tên lớp, gộp lớp, đổi module sở hữu, quan hệ mới `R-SYS-nn`) | Không | Áp từng `MD-nn`; quan hệ `R-SYS-nn` phải qua bước 3 và 4 như mọi quan hệ |

4. Ghi mỗi điểm lệch thành một dòng ở mục 7 "Quyết định gộp" của `CD-SYS.md` (mã `MD-nn` tiếp nối số của `EC-SYS`; quyết định đã có ở
   `EC-SYS` thì dẫn lại mã cũ, không tạo mã mới).

**Cổng A:** trình điểm lệch và đề xuất.

### B. Dựng bản hợp nhất

1. Tạo `CD-SYS.md` từ `output/cd-system-template.md` (`module: SYS`, `nguon: EC-SYS v…` và danh sách `CD-Mxx`).
   Số mục giữ giống tài liệu module (1, 2.1, 2.2, 3.1, 3.2, 4, 5) để tool đọc được.
2. Áp các quyết định đã duyệt và ghi các bảng. Ở bản hệ thống mọi lớp đều "của hệ thống": cột Sở hữu ghi module sở
   hữu, cột id chỉ còn `Có`, `Kế thừa` hoặc `Không` (không còn `Ngoài`).
3. Lớp, thuộc tính, quan hệ phải khớp `EC-SYS.md`. Quan hệ `R-SYS-nn` mới: làm đủ bước 3 (chọn thành phần – toàn
   thể, loại) và bước 4 (thuộc tính đối tượng).
4. Chạy `gen_puml.py --cd $M/cd/CD-SYS.md --inplace` và
   `check_cd.py --cd $M/cd/CD-SYS.md --system --final --ec $M/ec/EC-SYS.md`.

**Cổng B:** trình bản hợp nhất và các thay đổi so với tài liệu module.

### C. Đưa thay đổi về tài liệu module và chốt

Như lượt gộp EC: liệt kê thay đổi cần làm ở từng `CD-Mxx.md` (và ở `DB-Mxx.md` nếu đã tồn tại); người dùng
đồng ý thì sửa từng tệp, tăng phiên bản, dẫn `MD-nn`. Người dùng nói "Chốt CD-SYS" thì chốt.

## Tự kiểm

- Mỗi lớp, thuộc tính, quan hệ của `EC-SYS.md` có mặt; không có gì `EC-SYS.md` không có (ngoài id và thuộc tính đối
  tượng).
- Mọi đề nghị ở mục 6 của các `CD-Mxx.md` đã được đưa vào lớp, hoặc có `MD-nn` nêu vì sao không.
- Một kiểu id; một kiểu cho mỗi loại dữ liệu; mỗi kiểu liệt kê một tên.

## Không làm

Không sửa tài liệu module khi chưa được duyệt. Không tự quyết điểm lệch có ảnh hưởng tới nghiệp vụ.
