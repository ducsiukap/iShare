# Gộp hệ thống — Lớp thực thể toàn hệ thống (EC-SYS)

Chạy khi mọi module đã chốt `EC-Mxx.md`, **trước khi** bắt đầu skill `designing-entity-classes` (xem
`input/CONVENTIONS.md` mục 1). Các quyết định gộp ở đây (`MD-nn`) được đưa về tài liệu module, nên skill sau làm
trên tên lớp, thuộc tính và quan hệ đã thống nhất. Hai lượt gộp sau (`CD-SYS.md`, `DB-SYS.md`) dẫn lại đúng các mã
`MD-nn` này.

Lượt gộp cũng có cổng: mỗi việc lớn dưới đây (A, B, C) là một bước, làm xong thì dừng chờ người dùng xác nhận.

## Mục đích

Một danh sách lớp, thuộc tính và quan hệ thống nhất cho cả hệ thống: mỗi lớp một tên, một module sở hữu, một bộ
thuộc tính; mỗi quan hệ ghi một lần; không còn n-n; có sơ đồ lớp phân tích toàn hệ thống.

## Đầu vào

Mọi `EC-Mxx.md` (trạng thái Đã chốt) trong `data-model/ec/`; `glossary.md`.

## Việc làm

### A. Kiểm kê và tìm điểm lệch

1. Kiểm mọi module trong `module-registry.md` đã có `EC-Mxx.md` ở trạng thái Đã chốt. Thiếu thì dừng và báo, trừ khi
   người dùng yêu cầu gộp thử.
2. Chạy `merge_ec.py --dir $D --out-md $D/.work/merge-ec.md`. Tệp sinh ra có: bảng lớp, thuộc tính, lớp liên kết,
   quan hệ hợp nhất, và danh sách **điểm lệch**.
3. Đọc từng điểm lệch do tool nêu và tự tìm thêm những điểm tool không thấy được:

   | Điểm lệch | Tool thấy? | Cách xét |
   |---|---|---|
   | Một lớp có nhiều module sở hữu | Có | Một module giữ quyền sở hữu, module kia chuyển thành tham chiếu; hoặc hai lớp khác nghĩa thì đổi tên một lớp |
   | Lớp được tham chiếu nhưng module sở hữu không khai | Có | Thường do khác tên: tìm lớp cùng nghĩa ở module sở hữu |
   | Một nghĩa nhiều tên (đồng nghĩa) | Một phần (tên gần giống, cùng tên tiếng Việt) | So mô tả và thuộc tính của các lớp; chọn một tên theo `glossary.md` |
   | Một tên nhiều nghĩa (đồng âm) | Không | Đọc mô tả của lớp ở từng module; khác nghĩa thì đổi tên |
   | Thuộc tính khai ở nhiều module | Có | Cùng nghĩa thì giữ ở module sở hữu; khác ràng buộc thì hỏi |
   | Thuộc tính cùng nghĩa khác tên trong một lớp | Một phần | So tên tiếng Việt và nguồn |
   | Quan hệ khai ở nhiều module | Có | Bội số, loại, bên chính phải giống nhau; khác thì hỏi, dẫn mã FR của hai bên |
   | Quan hệ gián tiếp bị ghi thành trực tiếp sau khi gộp | Không | Sau khi gộp, A–B đã đi qua X ở module khác thì bỏ A–B trực tiếp |
   | Quan hệ n-n lộ ra khi nhìn toàn hệ thống | Không | Hai module mỗi bên ghi một chiều 1-n của cùng một cặp, ngược nhau → thực chất là n-n, phải tách |
   | Lớp 1-1 khác module có thể gộp | Không | Áp tiêu chí gộp/giữ ở bước 3 |
   | Thuộc tính "module bổ sung" cho lớp ngoài | Có (liệt kê) | Đưa vào lớp của module sở hữu |
   | Thuộc tính `Tham chiếu` mà module sở hữu chưa khai | Có | Module này cần đọc hoặc ghi thông tin mà lớp chưa có: thêm vào lớp của module sở hữu (Căn cứ `Nguồn nêu` hoặc `Đề xuất`), hoặc hỏi nếu hai bên hiểu khác nhau |
   | Thuộc tính `Đề xuất` | Có (liệt kê) | Rà lại cả nhóm: đề xuất của module này có trùng nghĩa với thuộc tính module khác đã có không |

4. Lập bảng **quyết định gộp** (mục 8 của `EC-SYS.md`), mỗi điểm lệch một dòng `MD-nn`: vấn đề, các module liên
   quan, phương án, đề xuất. Điểm nào quyết định được bằng quy ước (QU) hoặc glossary thì đề xuất luôn; điểm nào là
   chuyện nghiệp vụ (bội số khác nhau, nghĩa khác nhau) thì hỏi theo khuôn hỏi, dẫn mã FR của từng bên.

**Cổng A:** trình danh sách điểm lệch và đề xuất cho từng `MD-nn`. Chờ người dùng quyết.

### B. Dựng bản hợp nhất

1. Tạo `EC-SYS.md` từ `output/ec-system-template.md`. Frontmatter: `module: SYS`, `nguon` liệt kê mọi `EC-Mxx` kèm
   phiên bản. Số mục của bản hệ thống **giữ giống tài liệu module** (2.2, 2.3, 3.3, 3.4, 4) để tool đọc được.
2. Áp các quyết định `MD-nn` đã duyệt lên dữ liệu của `merge-ec.md` và ghi:
   - Bảng lớp (mục 2.2): mỗi lớp một dòng, cột Sở hữu là module sở hữu duy nhất, thêm cột "Module tham chiếu".
   - Bảng thuộc tính (mục 2.3): hợp của thuộc tính ở module sở hữu và thuộc tính các module khác bổ sung; cột Nguồn
     giữ mã FR kèm mã module; giữ cột Căn cứ (`Nguồn nêu`, `Đề xuất`). Bản hệ thống không còn dòng `Tham chiếu`: mỗi
     thuộc tính tham chiếu đã có ở lớp của module sở hữu (hoặc đã được thêm theo một `MD-nn`). Cột Thuộc tính ở bảng
     lớp liệt kê đủ thuộc tính của lớp.
   - Bảng lớp liên kết (mục 3.3) và bảng quan hệ (mục 3.4): mỗi quan hệ một dòng, **giữ ID `R-Mxx-nn` gốc**; quan hệ
     trùng thì giữ ID của module sở hữu lớp phía n và ghi ID kia ở cột Căn cứ; quan hệ chỉ sinh ra khi gộp thì đặt
     `R-SYS-nn`.
3. Soát lại toàn cục theo tự kiểm của bước 3: không n-n, mỗi Hợp thành đủ căn cứ, không lớp mồ côi, mỗi lớp thống
   kê có một quan hệ Kế thừa hoặc Phụ thuộc.
4. Chạy `gen_puml.py --ec $D/EC-SYS.md` (ghi `diagrams/EC-SYS.puml`, render `diagrams/EC-SYS.png`, đặt ảnh vào mục 4)
   và `check_ec.py --ec $D/EC-SYS.md --system --final`.

**Cổng B:** trình số lớp, số thuộc tính, số quan hệ trước và sau gộp; các thay đổi so với tài liệu module.

### C. Đưa thay đổi về tài liệu module và chốt

1. Mỗi `MD-nn` làm đổi nội dung của một module (đổi tên lớp, đổi module sở hữu, sửa bội số) được ghi vào cột
   "Áp dụng cho". **Không tự sửa tài liệu module.** Trình danh sách thay đổi cần làm ở từng `EC-Mxx.md`; người dùng
   đồng ý thì sửa từng tệp (tăng phiên bản, ghi Lịch sử, dẫn `MD-nn`) và chạy lại `check_ec.py --final` cho tệp đó.
2. Nếu `CD-Mxx.md` hoặc `DB-Mxx.md` của một module đã tồn tại (ví dụ khi phải gộp lại sau khi đã làm skill sau), ghi
   rõ `MD-nn` nào kéo theo thay đổi ở đó, để làm lại các bước bị ảnh hưởng.
3. Người dùng nói "Chốt EC-SYS": `trang_thai: Đã chốt`, phiên bản `1.0`.

## Tự kiểm

- Mỗi lớp của mọi `EC-Mxx.md` có mặt trong `EC-SYS.md`, hoặc có một `MD-nn` giải thích vì sao bị gộp hay đổi tên.
- Mỗi thuộc tính và mỗi quan hệ của module có mặt, hoặc có `MD-nn`.
- Không thêm lớp, thuộc tính, quan hệ nào không có ở tài liệu module (ngoài lớp liên kết sinh ra do tách n-n mới
  lộ, có `MD-nn`).

## Không làm

Không tự quyết điểm lệch về nghiệp vụ. Không sửa tài liệu module khi chưa được duyệt. Không gộp khi còn module chưa
chốt mà không báo.
