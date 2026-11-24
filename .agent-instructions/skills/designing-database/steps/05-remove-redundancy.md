# Bước 5 — Loại thuộc tính dư thừa

Ứng với Step 5 của phương pháp: "Loại bỏ các thuộc tính gây dư thừa dữ liệu. Có hai loại: thuộc tính bị trùng lặp
(thuộc tính của cùng một đối tượng, không phải thuộc tính khóa, nhưng xuất hiện ở hai bảng khác nhau) và thuộc tính
dẫn xuất (có thể tính toán cơ học từ các thuộc tính khác trong CSDL; thuộc tính xuất thân từ các lớp thực thể thống
kê thường là dẫn xuất). Sau khi loại, nếu xuất hiện bảng nào không còn thuộc tính nào nữa ngoài 1 khóa ngoại thì có
thể loại bỏ luôn bảng đấy."

## Mục đích

Lược đồ cuối không lưu hai lần cùng một dữ liệu và không lưu thứ tính lại được, trừ khi FR yêu cầu lưu. Mọi thứ bị
loại đều ghi lại cách có lại giá trị.

## Đầu vào

Mục 1–4 của `DB-Mxx.md`; cột Tính chất ở mục 2.1 của `CD-Mxx.md`; cột "Ràng buộc nguồn nêu" của `EC-Mxx.md` (công
thức của thuộc tính dẫn xuất); `FR-Mxx.md` (quy tắc nghiệp vụ).

## Việc làm

### 5.1 Thuộc tính dẫn xuất

Ứng viên là: mọi cột đến từ thuộc tính có Tính chất = `Dẫn xuất` ở CD, và mọi cột của bảng lớp thống kê. Với từng
cột, áp phép thử: **"Giá trị này có tính lại được một cách cơ học, bất cứ lúc nào, chỉ từ các cột khác còn lại
trong cơ sở dữ liệu không?"**

| Kết quả phép thử | Xử lý |
|---|---|
| Tính lại được, và FR không yêu cầu lưu | **Loại**: ghi ở mục 5.1, Loại dư thừa = `Dẫn xuất`; cột "Cách có lại giá trị" ghi công thức hoặc cách truy vấn bằng tên bảng và cột của lược đồ, dẫn mã BR |
| Tính lại được, nhưng FR yêu cầu **lưu kết quả** (kết quả tính định kỳ và hiển thị từ bản đã lưu; cần cho sắp xếp, tìm kiếm trên dữ liệu lớn theo một yêu cầu của FR) | **Không tự quyết.** Đề xuất ở cổng: giữ (ghi ở mục 5.3 kèm mã FR đòi lưu) hoặc loại. Người dùng quyết; ghi `DD-Mxx-nn` |
| **Không** tính lại được về sau: dữ liệu gốc có thể đổi hoặc mất (giá tại thời điểm giao dịch; tổng điểm trong khi bản ghi gốc bị xóa theo tài khoản) | Không phải dẫn xuất theo nghĩa của bước này. **Giữ**, ghi ở mục 5.4 "Đã xét nhưng không coi là dư thừa" kèm lý do. Nếu CD đang ghi thuộc tính đó là Dẫn xuất thì nêu ở cổng: bản phân tích nên sửa Tính chất |

Không loại cột khóa chính, khóa ngoại ở mục 5.1. Khóa mất theo bảng khi cả bảng bị loại.

### 5.2 Thuộc tính trùng lặp

Tìm cột **không phải khóa** mang cùng một dữ liệu của cùng một đối tượng nhưng nằm ở hai bảng:

- So tên cột và cột "Từ thuộc tính" giữa các bảng của module, và với bảng của các module đã làm
  (`merge_db.py --list`).
- **Cùng tên không có nghĩa là trùng lặp.** `clients.full_name` và `users.full_name` là của hai đối tượng khác
  nhau. `booked_rooms.price` (giá lúc đặt) và `rooms.price` (giá niêm yết hiện tại) là hai dữ liệu khác nhau.
  Chỉ là trùng lặp khi một bên luôn bằng bên kia và có thể lấy qua khóa ngoại.
- Trùng lặp thật: giữ cột ở bảng của đối tượng sở hữu dữ liệu, loại cột ở bảng kia; ghi ở mục 5.1 với Loại dư thừa
  = `Trùng lặp`, "Cách có lại giá trị" ghi đường đi qua khóa ngoại.
- Cặp cột đã xét mà kết luận không trùng lặp: ghi ở mục 5.4, để người dùng thấy đã xét.

### 5.3 Bảng bị loại

Sau khi loại cột, xét từng bảng:

| Tình trạng của bảng sau khi loại cột | Xử lý |
|---|---|
| Không còn cột nào ngoài khóa và có nhiều nhất **một** khóa ngoại (điển hình: bảng lớp thống kê) | Loại bảng: ghi ở mục 5.2 kèm lý do |
| Bảng liên kết chỉ còn khóa chính và **hai** khóa ngoại (ví dụ liên kết bài viết–Topic) | **Giữ**: bảng này lưu chính mối liên kết |
| Bảng bị gộp vào bảng khác do quan hệ 1-1 `Gộp` ở bước 3 | Ghi ở mục 5.2 với lý do "Gộp vào <bảng> theo R-…"; các cột của nó đã chuyển sang bảng được giữ |

Bảng bị loại không được còn bảng nào tham chiếu tới (tool kiểm). Bảng khác đang tham chiếu tới nó thì xem lại: hoặc
bảng đó không nên bị loại, hoặc khóa ngoại kia cũng phải được xử lý (nêu ở cổng).

### 5.4 Dựng lược đồ cuối

1. Chạy `build_schema.py --db …`: tool dựng mục 6.1 (bảng và cột cuối cùng) từ mục 1, 2.1, 4.1, 4.2 trừ đi 5.1,
   5.2; ghi mã PlantUML của sơ đồ quan hệ vào tệp riêng `diagrams/DB-Mxx.puml`, render thành `diagrams/DB-Mxx.png`
   và đặt ảnh kèm liên kết tới tệp `.puml` vào mục 6.2. Tài liệu không chứa mã PlantUML. Không sửa tay mục 6, tệp
   `.puml` hay ảnh.
   Tool trả mã 2 khi không render được: báo người dùng hướng dẫn tool in ra và hỏi cách xử lý (cài Java +
   `plantuml.jar`, cài lệnh `plantuml`, hoặc `--server`, tức là gửi nội dung sơ đồ lên máy chủ PlantUML). Không tự
   tải hay chạy phần mềm khác, không tự dùng `--server`.
2. Mở ảnh PNG để xem sơ đồ có đọc được không, rồi chạy `check_db.py --db … --final --cd …`.

## Ghi vào tệp DB

Mục 5.1, 5.2, 5.3, 5.4, 6 (do tool), 8 (quyết định thiết kế), 9 (câu hỏi). Tệp `diagrams/DB-Mxx.puml` và
`diagrams/DB-Mxx.png` (tool sinh).

## Tự kiểm trước cổng

- Mỗi thuộc tính Dẫn xuất của CD nằm ở đúng một trong: 5.1 (loại), 5.3 (giữ, có mã FR), hoặc bảng của nó ở 5.2.
- Với mỗi dòng 5.1: thử tính lại giá trị theo "Cách có lại giá trị" chỉ bằng các cột **có trong mục 6.1**. Công thức
  dùng tới cột đã bị loại thì chưa xong.
- Mỗi bảng còn lại có khóa chính; không bảng nào chỉ còn một khóa ngoại.
- Không khóa ngoại nào trỏ tới bảng đã loại.
- Đọc mục 6.1 từng bảng: mỗi chức năng Tạo/Đọc/Sửa/Xóa trong ma trận CRUD của FR có dữ liệu để làm không?

## Trình ở cổng

- Cột bị loại, theo hai nhóm (dẫn xuất, trùng lặp), kèm cách có lại giá trị.
- **Các cột dẫn xuất mà FR yêu cầu lưu**: từng cột, mã FR, đề xuất giữ hay loại. Đây là quyết định của người dùng.
- Các cặp đã xét nhưng không coi là dư thừa.
- Bảng bị loại và lý do.
- Lược đồ cuối: số bảng, danh sách bảng và cột; ảnh sơ đồ quan hệ (đường dẫn tệp PNG).
- WARN giữ lại kèm lý do. Hỏi người dùng có chốt `DB-Mxx` không.

## Khi người dùng nói "Chốt DB-Mxx"

`trang_thai: Đã chốt`, `phien_ban: 1.0`, thêm `5` vào `steps_completed`, thêm dòng Lịch sử. Báo người dùng: module kế
tiếp làm bằng chính skill này; nếu đây là module cuối cùng thì việc kế tiếp là lượt gộp `DB-SYS`
(`steps/90-system-merge.md`).

## Không làm

Không loại cột chỉ vì "có thể suy ra gần đúng". Không giữ cột dẫn xuất mà không có mã FR đòi lưu và không có quyết
định của người dùng. Không sửa tay mục 6.
