# Bước 4 — Thêm thuộc tính đối tượng

Ứng với Step 4 của phương pháp: "Add the object attributes which correspond to the aggregation/composition
relationships", ví dụ: "Room is a component of Hotel, of type n-1 → Hotel has a list of Room"; "Client is a component
of Booking, of type 1-n → Booking has a Client."

## Mục đích

Mỗi quan hệ thành phần – toàn thể được thể hiện bằng **một** thuộc tính đối tượng ở lớp toàn thể. Sau bước này sơ đồ
lớp thiết kế hoàn chỉnh.

## Đầu vào

Mục 3.1 của `CD-Mxx.md` đã duyệt; `data-model/conventions.md` (QU-05).

## Việc làm

1. Với **mỗi** dòng ở mục 3.1, thêm một dòng vào mục 4 theo quy tắc:

   | Dạng (thành phần–toàn thể) | Đọc là | Thuộc tính thêm vào lớp toàn thể | Kiểu |
   |---|---|---|---|
   | `1-n` | 1 thành phần được n toàn thể dùng | Toàn thể có **một** thành phần | `ThànhPhần` |
   | `n-1` | n thành phần thuộc 1 toàn thể | Toàn thể có **danh sách** thành phần | `ThànhPhần[]` |
   | `1-1` | 1 thành phần – 1 toàn thể | Toàn thể có **một** thành phần | `ThànhPhần` |

   - Cột **Quan hệ** ghi mã `R-Mxx-nn`. Cột **Lớp chứa** là lớp toàn thể của quan hệ đó.
   - Cột **Quy tắc** ghi câu của phương pháp: "<Thành phần> là thành phần của <Toàn thể>, dạng <…> → <Toàn thể> có
     <một | danh sách> <Thành phần>".
   - **Chỉ một phía.** Lớp thành phần không có thuộc tính trỏ ngược về toàn thể (case study: Hotel có danh sách
     Room, Room không có Hotel).
2. **Đặt tên** theo QU-05:
   - Một đối tượng: tên lớp thành phần viết camelCase (`client`, `topic`).
   - Danh sách: số nhiều của tên lớp (`rooms`, `postTopics`).
   - Một lớp có hai thuộc tính đối tượng cùng kiểu thì đặt theo **vai trò** trong FR (`author` và `lockedBy` cùng
     kiểu `User`), không đánh số (`user1`, `user2`).
   - Không trùng tên với thuộc tính đã có của lớp.
3. **Thuộc tính đối tượng rơi vào lớp ngoài** (lớp toàn thể do module khác sở hữu): vẫn ghi dòng ở mục 4, và ghi
   thêm ở mục 6 Liên module, cột "Đề nghị cho module sở hữu" (ví dụ "Thêm `postTopics : PostTopic[]` (R-M05-01)").
   Không sửa `CD` của module kia. Lượt gộp hệ thống sẽ đưa thuộc tính này vào lớp.
4. **Thuộc tính đối tượng có kiểu là lớp ngoài** (lớp thành phần do module khác sở hữu, lớp toàn thể của module
   này): ghi bình thường ở mục 4; lớp ngoài đã có ở mục 1 và mục 6.
5. Điền mục 6 Liên module: mỗi lớp ngoài một dòng.
6. Chạy `gen_puml.py --cd …`. Tool ghi mã PlantUML vào tệp riêng `diagrams/CD-Mxx.puml` cạnh tài liệu, render
   thành `diagrams/CD-Mxx.png` và đặt ảnh kèm liên kết tới tệp `.puml` vào mục 5. Tài liệu không chứa mã PlantUML;
   không sửa tay tệp `.puml` hay ảnh. Tool trả mã 2 khi không render được: báo người dùng hướng dẫn tool in ra và
   hỏi cách xử lý (cài Java + `plantuml.jar`, cài lệnh `plantuml`, hoặc `--server`, tức là gửi nội dung sơ đồ lên
   máy chủ PlantUML). Không tự tải hay chạy phần mềm khác, không tự dùng `--server`.
7. Mở ảnh PNG để xem sơ đồ có đọc được không, rồi chạy `check_cd.py --cd … --final --ec …`.

## Ghi vào tệp CD

Mục 4, 5, 6; mục 7 và 8 nếu có. Tệp `diagrams/CD-Mxx.puml` và `diagrams/CD-Mxx.png` (tool sinh).

## Tự kiểm trước cổng

- Số dòng mục 4 bằng số dòng mục 3.1; mỗi mã quan hệ đúng một dòng.
- Với mỗi dòng: lớp chứa đúng là toàn thể; kiểu khớp dạng (`n-1` thì là danh sách).
- Không hai lớp nào giữ thuộc tính đối tượng trỏ vào nhau. Nếu có (hai quan hệ khác nhau giữa cùng hai lớp), nêu ở
  cổng và giải thích.
- Đọc lại từng lớp như một lớp Java: các thuộc tính đối tượng có đủ để từ một đối tượng đi tới dữ liệu mà các chức
  năng của FR cần hiển thị không? Thiếu đường đi là dấu hiệu chọn sai bên toàn thể ở bước 3 (sửa ở bước 3, không
  thêm thuộc tính thứ hai).
- Kế thừa và Phụ thuộc không có thuộc tính đối tượng.

## Trình ở cổng

- Bảng thuộc tính đối tượng kèm câu quy tắc.
- Ảnh sơ đồ lớp thiết kế (đường dẫn tệp PNG).
- Danh sách từng lớp với đủ thuộc tính (thường và đối tượng), tức nội dung của sơ đồ.
- Thuộc tính đề nghị cho lớp của module khác.
- Tên đặt theo vai trò (để người dùng kiểm vai trò).
- WARN giữ lại kèm lý do. Hỏi người dùng có chốt `CD-Mxx` không.

## Khi người dùng nói "Chốt CD-Mxx"

`trang_thai: Đã chốt`, `phien_ban: 1.0`, thêm `4` vào `steps_completed`, thêm dòng Lịch sử. Báo người dùng: module kế
tiếp làm bằng chính skill này; nếu đây là module cuối cùng thì việc kế tiếp là lượt gộp `CD-SYS`
(`steps/90-system-merge.md`), rồi mới sang skill `designing-database`.

## Không làm

Không thêm thuộc tính đối tượng ở cả hai phía. Không thêm thuộc tính `xxxId` (khóa ngoại là việc của thiết kế
CSDL). Không thêm phương thức.
