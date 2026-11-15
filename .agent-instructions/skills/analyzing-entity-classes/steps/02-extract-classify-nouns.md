# Bước 2 — Trích danh từ và phân loại

Ứng với Step 2 + Step 3 của phương pháp:
"Extract all nouns… Each noun is counted only one time." và "Classify the nouns: a noun could become an entity class;
a noun could become an attribute of an entity class; reject a noun if it is too general, too abstract, or out of the
scope of the system."

## Mục đích

Mỗi danh từ có một kết luận có lý do. Kết quả là danh sách lớp ban đầu và thuộc tính của từng lớp, chưa có quan hệ.

## Đầu vào

Đoạn mô tả đã duyệt ở bước 1; `FR-Mxx.md`; `glossary.md`; các `EC-Myy.md` đã có.

## Việc làm

### 2.1 Xem các lớp đã có

Chạy `merge_ec.py --dir $D --list --exclude Mxx`. Lớp nào module khác đã định nghĩa thì dùng lại **đúng tên đó**.
Không tạo một lớp mới có cùng nghĩa với lớp đã có.

### 2.2 Trích danh từ từ đoạn mô tả

- Đi từng câu S1, S2… và ghi **mọi** danh từ và cụm danh từ vào sổ danh từ (mục 2.1 của EC), cột "Xuất hiện ở" ghi
  số câu đầu tiên nó xuất hiện.
- Mỗi danh từ chỉ một dòng. Đưa về số ít, bỏ từ chỉ lượng ("các", "những", "một").
- Hai danh từ cùng chỉ một thứ thì ghi chung một dòng, ngăn bởi dấu `/` ("tài khoản / người dùng").
- Cụm danh từ có nghĩa riêng thì giữ nguyên cụm ("thống kê phòng" khác "phòng").
- Hành động đã được viết thành danh từ ("lượt gợi ý Topic") cũng là danh từ.
- Không lọc trước. Danh từ rõ ràng sẽ bị loại ("hệ thống", "thông tin") vẫn phải có dòng và lý do.

### 2.3 Quét bổ sung trên FR

Đoạn mô tả ngắn nên thường thiếu thuộc tính. Đọc lần lượt các phần sau của FR và thêm vào sổ những danh từ chỉ
**dữ liệu hệ thống phải lưu hoặc phải tính** mà sổ chưa có. Cột "Xuất hiện ở" ghi `Quét: <mã>`, để người dùng thấy
danh từ nào không đến từ đoạn mô tả.

| Phần của FR | Tìm gì |
|---|---|
| Mục 2.1 Thuật ngữ | Khái niệm có dữ liệu riêng (ghi `Quét: TN:<thuật ngữ>`) |
| Yêu cầu cấp dưới của từng chức năng | Thứ được "lưu", "ghi", "gồm", "kèm"; "thời điểm…", "lý do…", "người thực hiện"; thứ được "hiển thị" mà phải có sẵn |
| Quy tắc nghiệp vụ | Thuộc tính mà quy tắc ràng buộc (tên, độ dài, tính duy nhất, mặc định); đại lượng được tính |
| Chuyển trạng thái | Mỗi thực thể có bảng trạng thái cho một thuộc tính trạng thái; tên các trạng thái là **giá trị**, không phải danh từ riêng |
| Giao tiếp với module khác | Đối tượng của module khác mà module này dùng |

Dấu hiệu dễ sót: mệnh đề "trong khi X đang/bị …" (một trạng thái phải được lưu); "nếu … đã …" (một dấu vết phải
được lưu); "lần gần nhất", "trong N ngày gần nhất" (một thời điểm phải được lưu).

Ở việc này **vẫn chưa** đọc mục "Dữ liệu nghiệp vụ" của FR.

### 2.4 Phân loại từng danh từ

Áp các phép thử **theo thứ tự**; dừng ở phép thử đầu tiên cho kết luận. Ghi kết luận vào cột Phân loại, Kết quả và
Lý do.

| # | Câu hỏi | Nếu đúng | Ghi |
|---|---|---|---|
| T1 | Hệ thống có phải lưu hoặc quản lý thông tin về nó không? | Không → loại | Loại bỏ. Lý do bắt đầu bằng một trong: `Trừu tượng`, `Chung chung`, `Ngoài phạm vi hệ thống`, `Giao diện`, `Hành động không lưu dấu vết` |
| T2 | Nó cùng nghĩa với một danh từ đã có trong sổ? | Gộp vào dòng kia | Không thêm dòng; thêm vào ô Danh từ của dòng kia sau dấu `/` |
| T3 | Nó là tác nhân hoặc vai trò của người dùng? | Vai trò có tài khoản → là lớp người dùng (lớp của module sở hữu tài khoản); vai trò chỉ là một giá trị phân quyền. Tác nhân không có tài khoản (Guest, Hệ thống) → loại | Lớp → tên lớp người dùng; hoặc Loại bỏ: `Không lưu: tác nhân không có dữ liệu` |
| T4 | FR ghi nó thuộc module khác? | Module này có quan hệ dữ liệu với nó → lớp ngoài. Không → loại | Lớp, và ở bảng lớp ghi Sở hữu = `Myy`; hoặc Loại bỏ: `Ngoài phạm vi module (Myy)` |
| T5 | Nó là giới hạn, ngưỡng, hằng số hay công thức của một quy tắc (tối đa 5, 30 ký tự, 7 ngày)? | Hằng số không lưu | Loại bỏ: `Hằng số của BR-…`; ghi con số vào cột Ràng buộc của thuộc tính liên quan. Ngoại lệ: giá trị FR cho phép Admin đổi lúc chạy → xét tiếp như dữ liệu |
| T6 | Nó là một giá trị trong một tập cố định (tên một trạng thái, một loại)? | Giá trị của thuộc tính | Loại bỏ: `Giá trị của <Lớp>.<thuộcTính>`; bảo đảm thuộc tính đó có ở bảng thuộc tính. Ngoại lệ: tập giá trị do người dùng thêm, sửa, xóa được → là lớp |
| T7 | Nó là số liệu tính ra từ dữ liệu khác (thống kê, tổng, điểm, thứ hạng, số đếm)? | Một nhóm số liệu theo một đối tượng hoặc một kỳ → lớp thống kê. Một giá trị gắn với một lớp → thuộc tính dẫn xuất | Lớp (Nhóm = Thống kê), hoặc Thuộc tính với Tính chất = Dẫn xuất |
| T8 | Nó có danh tính và vòng đời riêng: được tạo, sửa, xóa riêng; có nhiều đối tượng phân biệt được với nhau; và có từ hai thông tin riêng trở lên **hoặc** có trạng thái riêng? | Lớp | Lớp (Nhóm = Thực thể) |
| T9 | Nó chỉ là một giá trị mô tả một đối tượng khác? | Thuộc tính của lớp đó | Thuộc tính, Kết quả viết `Lớp.thuộcTính` |

Các điểm dễ sai:

- **Sự kiện, hành động** ("lượt gợi ý", "lần vô hiệu hóa") chỉ thành lớp khi FR yêu cầu lưu dấu vết của **từng lần**
  (ai, khi nào, kết quả). Hành động chỉ làm đổi trạng thái của đối tượng khác thì không thành lớp.
- **Giá trị là một đối tượng của lớp khác** ("tác giả của bài viết", "Topic của bài viết") không phải thuộc tính.
  Đó là quan hệ, để bước 3 xử lý. Ở sổ danh từ, danh từ đó được phân loại theo chính nó (tác giả → lớp người dùng).
- **Thuộc tính nhiều giá trị** ("các lựa chọn của poll") không để thành một thuộc tính dạng danh sách. Nếu mỗi giá
  trị có thông tin riêng hoặc được tham chiếu riêng → lớp riêng; quan hệ xét ở bước 3.
- **Số liệu tính ra: xem được lúc nào cũng tính lại, hay phải lưu?** T7 áp cho số liệu **tính lại được bất cứ lúc
  nào** từ dữ liệu khác (thống kê để xem, tổng, số đếm). Nếu FR yêu cầu **lưu kết quả thành bản ghi** (kết quả chốt
  theo kỳ, kết quả của lần tính gần nhất được hiển thị cho tới lần tính sau, giá trị không tính lại được về sau vì dữ
  liệu gốc thay đổi) thì đó là dữ liệu được lưu: phân loại ở T8 là lớp `Thực thể` với thuộc tính `Lưu`, ghi ở cột Lý
  do "kết quả tính được lưu theo <mã FR>". Trường hợp này luôn nêu ở cổng, vì theo phương pháp gốc lớp thống kê sẽ bị
  loại khỏi cơ sở dữ liệu ở bước cuối.
- **Kiểm bằng bất biến**: với mỗi lớp, chỉ ra được ít nhất một thuộc tính riêng hoặc một quy tắc BR nói về nó.
  Không chỉ ra được thì nhiều khả năng nó là thuộc tính của lớp khác, hoặc là một GAP loại Thiếu.
- **Không suy rộng**: FR nói "lưu thời điểm tạo" cho Tag thì chỉ Tag có thuộc tính đó.

### 2.5 Lập bảng lớp và bảng thuộc tính

- **Bảng lớp** (mục 2.2 của EC): tên theo QU-01; Nhóm là `Thực thể` hoặc `Thống kê` (lớp `Liên kết` chỉ xuất hiện ở
  bước 3); Sở hữu là mã module; Nguồn là mã FR.
- **Bảng thuộc tính** (mục 2.3 của EC): tên theo QU-03; Tính chất là `Lưu` hoặc `Dẫn xuất`; cột "Ràng buộc nguồn
  nêu" chép những gì FR nói về thuộc tính đó (độ dài tối đa, duy nhất, bắt buộc hay tùy chọn, tập giá trị, mặc
  định) kèm mã BR; Nguồn là mã FR.
- Không ghi `id`, không ghi thuộc tính kết thúc bằng `Id` (khóa ngoại), không ghi kiểu dữ liệu.
- Lớp ngoài: không liệt kê thuộc tính (xem `input/CONVENTIONS.md` mục 5).

### 2.6 Đối chiếu với mục "Dữ liệu nghiệp vụ" của FR

Bây giờ mới đọc mục "Dữ liệu nghiệp vụ" (bảng thực thể và ma trận CRUD). Lập bảng mục 2.4 của EC, mỗi thực thể của
FR một dòng (chép đúng tên ở cột Thực thể của FR):

| Tình huống | Xử lý |
|---|---|
| Thực thể của FR đã có lớp tương ứng, thuộc tính khớp | Ghi `Khớp` |
| FR có thực thể hoặc thuộc tính mà mô hình chưa có | Thêm qua sổ danh từ (Xuất hiện ở: `Quét: Dữ liệu nghiệp vụ`), rồi phân loại như mọi danh từ khác. Không thêm thẳng vào bảng lớp |
| Mô hình có lớp hoặc thuộc tính mà FR không liệt kê | Giữ nếu có nguồn ở yêu cầu hoặc BR; ghi `Mô hình có thêm: <lý do, mã nguồn>` và nêu ở cổng |
| FR gọi là thực thể nhưng phép thử cho ra thuộc tính (hoặc ngược lại) | Ghi `Lệch` kèm lý do, tạo câu hỏi loại Lệch ở mục 6 |

Dùng ma trận CRUD để kiểm: thực thể có ô Tạo là chức năng của module này thì module này sở hữu; ô ghi `Myy` thì
việc đó thuộc module khác.

### 2.7 Chạy tool

`check_ec.py --ec … --step 2 --fr … --others $D`.

## Ghi vào tệp EC

Mục 2.1, 2.2, 2.3, 2.4; mục 6 (câu hỏi mới).

## Tự kiểm trước cổng

- Đếm lại: mọi danh từ của đoạn mô tả đều có dòng trong sổ.
- Mỗi dòng Loại bỏ có lý do thuộc một trong các dạng ở T1–T6.
- Mỗi lớp có ít nhất một thuộc tính có nguồn. Lớp không có thì đã có câu hỏi loại Thiếu.
- Không thuộc tính nào có giá trị là đối tượng của lớp khác.
- Mỗi thuộc tính Dẫn xuất nêu được nó tính từ đâu (ghi ở cột Ràng buộc).
- Tên lớp trùng với lớp module khác đã có thì cùng nghĩa; cùng nghĩa thì cùng tên.

## Trình ở cổng

- Số danh từ: tổng, thành lớp, thành thuộc tính, bị loại; bao nhiêu đến từ lượt quét.
- **Danh từ bị loại và lý do** (phần người dùng hay phản biện nhất). Trình đủ, không rút gọn.
- Bảng lớp; với mỗi lớp, danh sách thuộc tính.
- Các dòng không `Khớp` ở bảng đối chiếu.
- Lớp ngoài và module sở hữu; tên nào còn là "tên tạm".
- GAP.

## Không làm

Chưa xét quan hệ, chưa tạo lớp liên kết. Không thêm thuộc tính FR không nói. Không sửa FR.
