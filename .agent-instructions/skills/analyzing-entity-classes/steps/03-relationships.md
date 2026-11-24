# Bước 3 — Quan hệ số lượng và quan hệ đối tượng

Ứng với Step 4 + Step 5 của phương pháp:
"Consider the quantitative relationship among entity classes: 1-1 keep it or regroup two classes into one; 1-n keep
them; n-n should be divided into at least 2 relationships of type 1-n." và "Determine the object relationship among
entity classes: generalization, aggregation, composition, association, dependence."

## Mục đích

Mọi cặp lớp có liên quan được xét bội số theo cả hai chiều; không còn quan hệ n-n; mỗi quan hệ có một loại và một
chiều rõ ràng. Đây là bước dễ sai nhất (sai loại, sai chiều), nên mỗi kết luận phải dẫn được một câu của FR.

## Đầu vào

Bảng lớp và thuộc tính đã duyệt ở bước 2; `FR-Mxx.md` (yêu cầu cấp dưới, quy tắc nghiệp vụ, cột "Quan hệ" và ma trận
CRUD của mục "Dữ liệu nghiệp vụ", "Giao tiếp với module khác").

## Việc làm

### 3.1 Lập ma trận cặp lớp

Lập bảng vuông các lớp (mục 3.1 của EC), chỉ điền nửa trên. Mỗi ô ghi:

- `T`: hai lớp có quan hệ trực tiếp (FR có câu đặt hai đối tượng cạnh nhau: "bài viết có Topic", "Tag của bài viết");
- `G(X)`: chỉ liên hệ gián tiếp qua lớp X;
- để trống: không liên quan.

Xét cả: quan hệ của một lớp **với chính nó** (ví dụ phản hồi của một bình luận); quan hệ giữa lớp của module và lớp
ngoài. Không xét cặp hai lớp ngoài. Lớp thống kê không xét ở ma trận, xét riêng ở việc 3.4.

Ma trận để bảo đảm không cặp nào bị bỏ quên. Ô `G(X)` thừa là lỗi hay gặp: nếu A–X và X–B đã có thì không thêm A–B.

### 3.2 Viết quan hệ số lượng theo hai chiều

Với mỗi ô `T`, thêm một dòng vào mục 3.2 của EC, viết **hai câu** theo khuôn:

```
Một <A> có <thể | phải> có <bao nhiêu> <B> [ở các thời điểm khác nhau].
Một <B> <thuộc | ứng với | do> <bao nhiêu> <A>.
```

- Xét **trong suốt thời gian tồn tại** của đối tượng, không phải tại một thời điểm. (Case study: một phòng có thể
  được nhiều khách đặt *ở các thời điểm khác nhau* nên Client – Room là n-n.)
- Lấy số từ quy tắc nghiệp vụ: "từ 1 đến 3 Topic" → `1..3`; "tối đa 5 Tag, không bắt buộc" → `0..5`; "tùy chọn" →
  cận dưới 0; "bắt buộc", "đúng một" → `1`.
- FR không cho biết một đầu → câu hỏi loại Thiếu, kèm đề xuất rút từ các yêu cầu liên quan. Không tự chọn.
- Từ hai câu suy ra Dạng: `1-1`, `1-n`, `n-1` hoặc `n-n` (đọc theo thứ tự A–B).

### 3.3 Xử lý theo dạng

| Dạng | Xử lý | Ghi ở cột Xử lý |
|---|---|---|
| 1-n | Giữ | `Giữ nguyên` |
| 1-1 | **Gộp** hai lớp thành một khi: cùng module sở hữu, luôn được tạo và xóa cùng nhau, không lớp nào có quan hệ riêng với lớp thứ ba, và FR không gọi chúng là hai thứ có vòng đời khác nhau. **Giữ** khi: một đầu là tùy chọn (`0..1`), vòng đời khác nhau, khác module sở hữu, hoặc một bên là lớp thống kê | `Gộp vào <Lớp>: <lý do>` hoặc `Giữ: <lý do>` |
| n-n | **Tách** bằng một lớp ở giữa, thành hai quan hệ 1-n | `Tách: thêm lớp <X>` |

Cách tách n-n:

1. Tìm tên nghiệp vụ của "một lần A gắn với B" trong FR (ví dụ FR gọi "Liên kết bài viết–Topic", "Phiếu bình chọn",
   "Lượt theo dõi"). Đặt tên lớp theo QU-01. Không có tên nghiệp vụ thì ghép tên hai lớp.
2. Thêm lớp đó vào bảng lớp (mục 2.2) với Nhóm = `Liên kết`, và thêm một dòng ở mục 3.3 của EC. Nếu lớp đó đã có từ
   bước 2 (danh từ đã xuất hiện trong đoạn mô tả, như "phòng đã đặt" của case study) thì đổi Nhóm của nó thành
   `Liên kết`.
3. Chuyển vào lớp liên kết những thuộc tính **thuộc về cặp**: thời điểm gắn, số lượng, giá lúc đó, thứ tự, trạng
   thái của lần gắn. Phép thử: "giá trị này có đổi khi đổi A mà giữ B không? có đổi khi đổi B mà giữ A không?" Cả
   hai đều có thì nó thuộc cặp.
   Rồi đi qua 8 câu hỏi ở việc 2.5 của bước 2 cho lớp liên kết mới, như với mọi lớp: thuộc tính FR nêu ghi `Nguồn
   nêu`, thuộc tính FR không nêu nhưng chức năng cần thì ghi `Đề xuất` kèm lý do. Thêm các thuộc tính vào mục 2.3 và
   cột Thuộc tính của lớp đó ở mục 2.2. Lớp liên kết thật sự không có thuộc tính nào (chỉ nối hai lớp) thì ghi rõ vì
   sao ở cột "Thuộc tính riêng của liên kết" của mục 3.3, ví dụ "Không có: FR chỉ nêu bài viết và Topic".
4. Thêm hai dòng 1-n mới vào mục 3.2 (A – X và B – X) và viết đủ hai câu cho mỗi dòng.
5. **Xét lại lớp vừa thêm với các lớp còn lại.** Có thể lại gặp n-n và phải tách tiếp (case study: Client – Room →
   Booking; Booking – Room vẫn n-n → BookedRoom). Lặp tới khi không còn n-n.

Một lớp ở giữa có quan hệ riêng với lớp thứ ba, có vòng đời riêng và được FR gọi tên như một đối tượng độc lập
(Booking của case study) là lớp `Thực thể`, không phải `Liên kết`. Lớp `Liên kết` là lớp mà một cặp (A, B) xác định
duy nhất một đối tượng của nó (BookedRoom, UsedService).

### 3.4 Xác định loại quan hệ đối tượng

Với mỗi quan hệ còn lại, và với mỗi lớp thống kê, xét **theo thứ tự**; dừng ở loại đầu tiên đúng.

| Thứ tự | Loại | Điều kiện, tất cả phải có căn cứ trong FR | Bên chính |
|---|---|---|---|
| a | Kế thừa | "B là một loại A", B dùng lại **toàn bộ** thuộc tính của A và có thêm thuộc tính riêng. Lớp thống kê `XStat` dùng lại thuộc tính của lớp X → kế thừa X (theo phương pháp). Vai trò người dùng không có dữ liệu riêng thì **không** tạo lớp con | Lớp cha |
| b | Phụ thuộc | A cần B để tính hoặc để hoạt động, nhưng không giữ đối tượng B nào và không dùng lại thuộc tính của B. Thường gặp ở lớp thống kê không gắn với một lớp gốc (IncomeStat → Bill) | Lớp được dùng (B) |
| c | Liên kết (nửa của n-n đã tách) | Quan hệ 1-n giữa một lớp và lớp `Liên kết` sinh ra ở việc 3.3 | — |
| d | Hợp thành | Cả ba: (i) thành phần không được tạo khi chưa có toàn thể; (ii) mỗi thành phần thuộc **đúng một** toàn thể và không chuyển sang toàn thể khác; (iii) xóa toàn thể thì thành phần bị xóa theo | Lớp toàn thể |
| e | Kết tập | Có nghĩa "gồm", "chứa", "có", "của", "ghi lại", nhưng thành phần tồn tại độc lập, hoặc được nhiều toàn thể dùng chung, hoặc còn lại khi toàn thể bị xóa | Lớp toàn thể |
| f | Liên kết | Hai lớp có liên hệ nhưng không bên nào chứa bên nào | — |

Quy tắc đi kèm:

- **Hợp thành cần đủ căn cứ.** Điều (iii) phải dẫn được một câu của FR hoặc một ô của ma trận CRUD ("theo bài",
  "bị xóa cùng"). Thiếu căn cứ cho một trong ba điều thì ghi Kết tập, không ghi Hợp thành. Ở dòng Hợp thành, bội số
  phía toàn thể phải là đúng `1` (tool kiểm).
- **Bên toàn thể của Kết tập** là lớp "chứa thông tin" của lớp kia. Theo case study: với quan hệ 1-n mà phía n ghi
  lại phía 1 (lượt đặt phòng ghi khách hàng; hóa đơn ghi người lập), phía n là toàn thể. Khi phía 1 gồm nhiều phần
  tử phía n và FR nói theo hướng đó (khách sạn có các phòng), phía 1 là toàn thể.
- **Kiểm chiều bằng cách đọc thành câu** và so với FR: "<Toàn thể> gồm/chứa/ghi lại <thành phần>"; "<Con> là một
  loại <Cha>"; "<A> dùng <B> để tính". Câu đọc lên trái với FR thì chiều đang sai.
- Quan hệ của một lớp với chính nó: ghi Lớp A = Lớp B, bội số hai đầu, loại thường là Liên kết hoặc Kết tập.

### 3.5 Lập bảng quan hệ, sơ đồ, liên module

1. Ghi **bảng quan hệ** (mục 3.4 của EC): mỗi quan hệ một dòng, ID `R-Mxx-nn` tăng dần và không đánh lại. Cột:
   - Bội số A = số đối tượng A ứng với **một** đối tượng B (con số ghi ở đầu A trên sơ đồ); Bội số B tương tự.
   - Dạng đọc theo thứ tự A–B. Kế thừa và Phụ thuộc ghi `—` ở ba cột bội số và dạng.
   - Căn cứ: một câu vì sao chọn loại này (dẫn điều kiện ở bảng trên). Nguồn: mã FR.
2. Chạy `gen_puml.py --ec …` để sinh sơ đồ lớp phân tích. Tool ghi mã PlantUML vào tệp riêng
   `diagrams/EC-Mxx.puml` (cạnh tài liệu), render ra `diagrams/EC-Mxx.png`, và đặt **ảnh** vào mục 4 cùng liên kết
   tới tệp `.puml`. Tài liệu không chứa mã PlantUML. Lớp liên kết được vẽ theo ký pháp lớp liên kết (nối nét đứt vào
   đường liên kết), giống sơ đồ phân tích của case study. Không sửa tay tệp `.puml` hay ảnh; muốn đổi sơ đồ thì sửa
   bảng rồi chạy lại.
   - Tool trả mã thoát 2 khi không render được ảnh (thiếu Java, `plantuml.jar` hoặc lệnh `plantuml`); tệp `.puml` vẫn
     được ghi. Khi đó báo người dùng nguyên văn hướng dẫn tool in ra và hỏi họ chọn cách nào (cài `plantuml.jar`,
     cài lệnh `plantuml`, hoặc dùng `--server`, tức là gửi nội dung sơ đồ lên máy chủ PlantUML). Không tự dùng
     `--server` khi người dùng chưa đồng ý.
   - Mở ảnh PNG vừa render để nhìn lại: lớp nào đứng riêng, đường nào cắt chéo khó đọc thì nêu ở cổng.
3. Điền **mục 5 Liên module**: mỗi lớp ngoài một dòng (module sở hữu, module này dùng thế nào, thuộc tính module
   này bổ sung nếu có).
4. Chạy `check_ec.py --ec … --final --fr … --others $D`.

## Ghi vào tệp EC

Mục 2.2 và 2.3 (lớp liên kết và thuộc tính của nó), 3.1–3.4, 4 (ảnh sơ đồ), 5, 6. Tệp `diagrams/EC-Mxx.puml` và
`diagrams/EC-Mxx.png` cạnh tài liệu.

## Tự kiểm trước cổng

- Mọi ô `T` của ma trận có dòng ở mục 3.2; mọi dòng 3.2 dạng 1-n hoặc 1-1 được giữ có dòng ở mục 3.4.
- Không còn n-n ở mục 3.4.
- Đọc từng dòng của mục 3.4 thành câu theo khuôn ở việc 3.4; câu nào không dẫn được FR thì sửa hoặc đặt câu hỏi.
- Mỗi dòng Hợp thành trích được căn cứ cho cả ba điều.
- Mỗi lớp thống kê có đúng một dòng Kế thừa hoặc Phụ thuộc.
- Không lớp nào của module đứng một mình. Lớp mồ côi thật sự (ví dụ một lớp cấu hình) thì nêu lý do ở cổng.
- Thuộc tính đã chuyển vào lớp liên kết không còn nằm ở lớp cũ.

## Trình ở cổng

- Ảnh sơ đồ (gửi tệp PNG cho người dùng nếu có thể) và đường dẫn tệp `.puml`.

- Bảng quan hệ số lượng, nêu riêng các dòng n-n và cách tách, các dòng 1-1 và quyết định gộp hay giữ.
- Bảng quan hệ, mỗi dòng kèm câu đọc. Nêu riêng: mọi dòng Hợp thành (kèm căn cứ), mọi dòng mà bên toàn thể là
  phán đoán của bạn.
- Lớp liên kết mới và thuộc tính của nó (đánh dấu thuộc tính `Đề xuất`).
- Quan hệ với lớp ngoài.
- GAP; WARN giữ lại kèm lý do.
- Hỏi người dùng có chốt `EC-Mxx` không.

## Khi người dùng nói "Chốt EC-Mxx"

`trang_thai: Đã chốt`, `phien_ban: 1.0`, thêm `3` vào `steps_completed`, thêm dòng ở mục 7 Lịch sử. Báo người dùng:
module kế tiếp làm bằng chính skill này; nếu đây là module cuối cùng thì việc kế tiếp là lượt gộp hệ thống
(`steps/90-system-merge.md`), rồi mới sang skill `designing-entity-classes`.

## Không làm

Không chuyển Liên kết thành Kết tập hay Hợp thành để "cho gọn": việc đó thuộc bước 3 của skill thiết kế lớp.
Không thêm id hay khóa. Không sửa tài liệu của module khác.
