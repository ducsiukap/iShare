# Bước 3 — Chuyển quan hệ liên kết thành kết tập hoặc hợp thành

Ứng với Step 3 của phương pháp: "Convert all association relationships to correspond aggregation/composition
relationships", ví dụ: "Room + Booking → BookedRoom is converted to: Room is a component of BookedRoom, BookedRoom is
a component of Booking."

## Mục đích

Sau bước này mỗi quan hệ (trừ Kế thừa và Phụ thuộc) nói rõ **lớp nào là thành phần, lớp nào là toàn thể**. Bước 4 sẽ
dựa vào đó để đặt thuộc tính đối tượng vào đúng một phía.

## Đầu vào

Mục 3.3 và 3.4 của `EC-Mxx.md`; `FR-Mxx.md` để đọc căn cứ.

## Việc làm

### 3.1 Quan hệ giữ nguyên

Mỗi dòng **Kế thừa** và **Phụ thuộc** ở mục 3.4 của EC được chép sang mục 3.2 của CD, giữ nguyên ID:

- Kế thừa: Lớp = lớp con, Lớp đích = lớp cha.
- Phụ thuộc: Lớp = lớp phụ thuộc, Lớp đích = lớp được dùng.

Hai loại này không sinh thuộc tính đối tượng.

### 3.2 Quan hệ đã là Hợp thành hoặc Kết tập ở bản phân tích

Chép sang mục 3.1 của CD, **giữ nguyên loại và bên toàn thể** (cột "Bên chính" của EC là Toàn thể; lớp còn lại là
Thành phần). Căn cứ ghi `Giữ nguyên từ phân tích`.

### 3.3 Quan hệ Liên kết sinh ra từ một n-n đã tách (có lớp liên kết)

Mỗi dòng ở mục 3.3 của EC là một mẫu "A + B → C" (C là lớp liên kết), ứng với hai dòng Liên kết A–C và B–C. Chuyển
theo mẫu của phương pháp: **một lớp gốc là thành phần của C, và C là thành phần của lớp gốc còn lại.**

Chọn lớp gốc nào chứa C (lớp "chứa") và lớp gốc nào được C tham chiếu (lớp "danh mục"):

| Dấu hiệu trong FR | Lớp đó là |
|---|---|
| Đối tượng C được tạo ra **trong lúc thao tác trên** lớp này (gán Topic khi soạn bài viết; thêm phòng khi lập lượt đặt phòng) | Lớp chứa |
| Người dùng xem, sửa, xóa các C **qua** lớp này; xóa đối tượng lớp này thì các C của nó đi theo | Lớp chứa |
| Lớp này có sẵn từ trước, tồn tại độc lập, được nhiều C trỏ tới (phòng, dịch vụ, Topic trong danh mục) | Lớp danh mục |

Kết quả là hai dòng ở mục 3.1 của CD:

- `C` là thành phần của lớp chứa, dạng `n-1` (nhiều C thuộc một lớp chứa).
- Lớp danh mục là thành phần của `C`, dạng `1-n` (một đối tượng danh mục được nhiều C dùng).

Hai lớp gốc đều "chứa" như nhau (FR cho thao tác từ cả hai phía, không phía nào có sẵn trước) → chọn theo phía mà
chức năng **tạo** C xuất phát, ghi lý do, và nêu ở cổng như một điểm phán đoán.

### 3.4 Quan hệ Liên kết còn lại (không có lớp liên kết)

Quan hệ 1-n hoặc 1-1 ghi là Liên kết ở bản phân tích cũng phải chuyển:

- Dạng 1-n: mặc định **phía 1 là thành phần của phía n** (phía n giữ một tham chiếu tới phía 1), như "Client is a
  component of Booking" của case study. Chỉ chọn ngược lại (phía 1 là toàn thể, giữ danh sách phía n) khi FR mô tả
  phía n như các phần của phía 1 và luôn truy cập chúng qua phía 1.
- Dạng 1-1: toàn thể là lớp được tạo sau, hoặc lớp có thao tác chính; ghi lý do.
- Quan hệ của một lớp với chính nó (bình luận – phản hồi): thành phần và toàn thể cùng là lớp đó; ghi rõ vai trò ở
  cột Căn cứ ("phản hồi giữ tham chiếu tới bình luận gốc").

### 3.5 Chọn Kết tập hay Hợp thành cho quan hệ vừa chuyển

Mặc định là **Kết tập**. Chỉ ghi **Hợp thành** khi FR cho căn cứ của cả ba điều (như ở bước phân tích): thành phần
không tồn tại ngoài toàn thể; thuộc đúng một toàn thể và không chuyển sang toàn thể khác; bị xóa theo toàn thể. Với
dòng Hợp thành, bội số phía toàn thể phải là đúng `1` (tool kiểm). Thiếu một căn cứ thì giữ Kết tập.

### 3.6 Điền các cột của mục 3.1

- **ID**: đúng mã `R-Mxx-nn` của EC. Không tạo mã mới.
- **Bội số thành phần** = số thành phần ứng với một toàn thể. **Bội số toàn thể** = số toàn thể ứng với một thành
  phần. Lấy đúng con số của EC (chỉ đổi cột A/B sang thành phần/toàn thể).
- **Dạng** đọc theo thứ tự thành phần–toàn thể: `n-1` (n thành phần – 1 toàn thể), `1-n` (1 thành phần – n toàn
  thể), `1-1`.
- **Loại ở phân tích**: loại của quan hệ này ở EC.
- **Căn cứ**: vì sao chọn bên toàn thể và loại, dẫn mã FR khi là phán đoán.

Chạy `check_cd.py --cd … --step 3 --ec …`.

## Ghi vào tệp CD

Mục 3.1, 3.2; mục 7 (quyết định thiết kế) và 8 (câu hỏi) nếu có.

## Tự kiểm trước cổng

- Mọi mã quan hệ của EC có mặt ở mục 3.1 hoặc 3.2; không có mã nào EC không có.
- Không còn dòng nào mang loại Liên kết.
- Với mỗi lớp liên kết: đúng một lớp gốc chứa nó, lớp gốc kia là thành phần của nó.
- Đọc từng dòng thành câu "<Thành phần> là thành phần của <Toàn thể>, dạng …" và so với FR.
- Không cặp lớp nào chứa lẫn nhau qua hai quan hệ khác nhau mà không có lý do.

## Trình ở cổng

- Bảng quan hệ thành phần – toàn thể, mỗi dòng kèm câu đọc.
- Nêu riêng: các dòng chuyển từ Liên kết (đây là phán đoán của bước này); các dòng ghi Hợp thành kèm căn cứ; các
  quan hệ mà hai phía đều có thể là lớp chứa.
- Quan hệ giữ nguyên (Kế thừa, Phụ thuộc).

## Không làm

Chưa thêm thuộc tính đối tượng. Không đổi bội số. Không đổi loại hoặc bên toàn thể của quan hệ đã là Kết tập, Hợp
thành ở bản phân tích; thấy sai thì quay lại sửa `EC-Mxx.md`.
