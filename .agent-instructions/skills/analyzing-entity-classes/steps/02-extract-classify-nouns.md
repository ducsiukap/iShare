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

- Đi lần lượt từng câu ở bảng 1.2 và ghi **mọi** danh từ và cụm danh từ vào sổ danh từ (mục 2.1 của EC), cột
  "Xuất hiện ở" ghi câu đầu tiên nó xuất hiện, dạng `Câu 3`.
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
| T4 | FR ghi nó thuộc module khác? | Là đối tượng mà module này có quan hệ dữ liệu → lớp ngoài. Là **thông tin của một lớp ngoài** mà module này đọc hoặc ghi (tiêu đề bài viết dùng để gợi ý; lý do ghi vào nhật ký kiểm duyệt) → thuộc tính của lớp ngoài đó, Căn cứ = `Tham chiếu`. Không dính tới dữ liệu của module này → loại | Lớp (Sở hữu = `Myy`); hoặc Thuộc tính `LớpNgoài.thuộcTính`; hoặc Loại bỏ: `Ngoài phạm vi module (Myy)` |
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

### 2.5 Lập bảng lớp và đưa ra đủ thuộc tính cho từng lớp

**Khi một danh từ được kết luận là lớp, đưa ra luôn các thuộc tính của lớp đó.** Người duyệt phải thấy được mỗi lớp
"trông như thế nào"; một lớp chỉ có tên hoặc không có thuộc tính nào thì không duyệt được. Thuộc tính đến từ ba
nguồn, ghi ở cột **Căn cứ** của mục 2.3:

| Căn cứ | Khi nào | Cột Nguồn | Cột Ghi chú |
|---|---|---|---|
| `Nguồn nêu` | FR nói tới thông tin đó (yêu cầu, quy tắc, thuật ngữ, bảng trạng thái, mục Dữ liệu nghiệp vụ) | Mã FR/BR nêu nó | Không bắt buộc |
| `Đề xuất` | FR không gọi tên, nhưng một chức năng hoặc quy tắc của FR **không chạy được** nếu thiếu nó | Mã chức năng hoặc quy tắc cần nó | **Bắt buộc**: vì sao cần, ví dụ "FR-M05-04.01 hiển thị danh sách Topic → cần tên" |
| `Tham chiếu` | Thuộc tính của **lớp ngoài** mà module này đọc hoặc ghi; module sở hữu lớp đó định nghĩa nó | Mã FR của module này nói tới việc đọc/ghi | **Bắt buộc**: module này dùng nó làm gì |

Với **mỗi lớp của module**, đi qua danh sách câu hỏi sau để tìm thuộc tính, rồi ghi đủ vào mục 2.3:

| # | Câu hỏi | Thường cho ra |
|---|---|---|
| 1 | Chức năng xem, danh sách, tìm kiếm của FR hiện gì về đối tượng này? | Tên, tiêu đề, nội dung, mô tả |
| 2 | Người dùng hoặc quy tắc phân biệt hai đối tượng bằng gì? Có quy tắc "không trùng" không? | Tên, mã, khóa nghiệp vụ |
| 3 | Đối tượng có bảng chuyển trạng thái, hoặc FR có câu "trong khi … đang/bị …", "đã … chưa"? | `status` hoặc cờ |
| 4 | FR có sắp xếp theo thời gian, cửa sổ "N ngày gần nhất", "lần gần nhất", thời hạn, hết hạn, khôi phục trong N ngày? | Các thời điểm `xxxAt` |
| 5 | Có giá trị phải giữ nguyên dù nguồn của nó đổi về sau (giá lúc đặt, tên lúc gửi, kết quả lúc tính)? | Thuộc tính chụp tại thời điểm |
| 6 | Quy tắc nêu con số tính trên đối tượng (đếm, tổng, điểm, thứ hạng)? | Thuộc tính `Dẫn xuất` (ghi công thức ở cột Ràng buộc) |
| 7 | Thao tác trên đối tượng có nhập lý do, ghi chú, người thực hiện? | `reason`, `note`; người thực hiện là quan hệ, xét ở bước 3 |
| 8 | Dữ liệu người dùng nhập khi tạo hoặc sửa đối tượng (theo các yêu cầu cấp dưới)? | Các trường nhập |

Quy tắc khi đề xuất:

- Mỗi đề xuất phải dẫn được về **một chức năng hoặc quy tắc đã có** của FR. Không đề xuất thuộc tính chỉ vì "diễn đàn
  nào cũng có", không thêm `createdAt`, `updatedAt` cho mọi lớp: chỉ thêm khi câu hỏi 4 trả lời có.
- Đề xuất không được tạo **hành vi mới** (thứ người dùng thấy hoặc nhập mà FR không nói). Thấy cần hành vi mới thì đó
  là GAP của FR: ghi câu hỏi ở mục 6, không đề xuất.
- Thuộc tính có giá trị là một đối tượng của lớp khác ("tác giả", "Topic của bài viết") **không** ghi ở đây: đó là
  quan hệ, xét ở bước 3.
- Không ghi `id`, không ghi thuộc tính kết thúc bằng `Id` (khóa ngoại), không ghi kiểu dữ liệu.

Với **lớp ngoài**: ghi các thuộc tính mà module này đọc hoặc ghi, Căn cứ = `Tham chiếu` (ví dụ M05 đọc tiêu đề và nội
dung chữ của bài viết để gợi ý Topic; M05 ghi lý do và thời điểm vào dòng nhật ký kiểm duyệt). Không liệt kê thuộc
tính khác của lớp ngoài. Thuộc tính mà **FR của module này định nghĩa** nhưng nằm trên lớp ngoài thì Căn cứ là
`Nguồn nêu` hoặc `Đề xuất`, và ghi thêm ở mục 5 Liên module (cột "Thuộc tính module này bổ sung").

Rồi điền hai bảng:

- **Bảng lớp** (mục 2.2): tên theo QU-01; Nhóm là `Thực thể` hoặc `Thống kê` (lớp `Liên kết` chỉ xuất hiện ở bước 3);
  Sở hữu là mã module; cột **Thuộc tính** liệt kê tên mọi thuộc tính của lớp ở mục 2.3, thuộc tính dẫn xuất có `/`
  phía trước (ví dụ `name, status, /rank`), để người đọc thấy lớp và thuộc tính trên cùng một dòng; Nguồn là mã FR.
- **Bảng thuộc tính** (mục 2.3): xếp theo lớp; tên theo QU-03; Tính chất `Lưu` hoặc `Dẫn xuất`; Căn cứ; cột "Ràng
  buộc nguồn nêu" chép những gì FR nói về thuộc tính (độ dài tối đa, duy nhất, bắt buộc hay tùy chọn, tập giá trị,
  mặc định) kèm mã BR, đề xuất mà FR không nêu ràng buộc thì ghi `—`; Nguồn; Ghi chú.

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
- Mỗi lớp của module đã qua đủ 8 câu hỏi ở việc 2.5; mỗi lớp có thuộc tính đủ để người đọc hình dung nó. Lớp vẫn
  không có thuộc tính nào thì xem lại nó có phải thuộc tính của lớp khác không, hoặc đặt câu hỏi loại Thiếu.
- Mỗi đề xuất có Ghi chú dẫn tới một chức năng hoặc quy tắc cụ thể; không đề xuất nào tạo hành vi mới.
- Mỗi lớp ngoài có các thuộc tính Tham chiếu mà module này thật sự đọc hoặc ghi.
- Cột Thuộc tính ở mục 2.2 khớp mục 2.3 (tool kiểm).
- Không thuộc tính nào có giá trị là đối tượng của lớp khác.
- Mỗi thuộc tính Dẫn xuất nêu được nó tính từ đâu (ghi ở cột Ràng buộc).
- Tên lớp trùng với lớp module khác đã có thì cùng nghĩa; cùng nghĩa thì cùng tên.

## Trình ở cổng

- Số danh từ: tổng, thành lớp, thành thuộc tính, bị loại; bao nhiêu đến từ lượt quét.
- **Danh từ bị loại và lý do** (phần người dùng hay phản biện nhất). Trình đủ, không rút gọn.
- Với **từng lớp**: tên, mô tả, rồi danh sách thuộc tính, mỗi thuộc tính một dòng ngắn kèm Căn cứ. Đánh dấu rõ các
  thuộc tính `Đề xuất` và lý do, gom thành danh sách để người dùng trả lời một lần ("ok cả nhóm", hoặc bỏ/sửa từng
  dòng).
- Các dòng không `Khớp` ở bảng đối chiếu.
- Lớp ngoài và module sở hữu; tên nào còn là "tên tạm".
- GAP.

## Không làm

Chưa xét quan hệ, chưa tạo lớp liên kết. Không thêm thuộc tính không dẫn được về một chức năng hoặc quy tắc của FR;
không đề xuất hành vi mới. Không sửa FR.
