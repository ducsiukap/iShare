---
module: M00
ten_module: Ví dụ — Quản lý khách sạn
ma_tai_lieu: CD-M00
phien_ban: 1.0
trang_thai: Đã chốt
ngay: 2026-11-15
tac_gia: (ví dụ)
nguon: EC-M00 v1.0
steps_completed: [1, 2, 3, 4]
---
# Thiết kế lớp thực thể — M00 Ví dụ: Quản lý khách sạn

<!-- Case study của phương pháp, viết lại theo đúng mẫu cd-template.md.
     Đầu vào là ví dụ của skill analyzing-entity-classes (output/example.md, tức EC-M00).
     Ví dụ không có FR nên cột "Căn cứ kiểu" ghi "CS" (theo hình kết quả của case study).
     Với module thật, cột này ghi mã FR-/BR- hoặc mã quy ước QU-xx. -->

## 1. Lớp và id

| Lớp | Nhóm | Sở hữu | Lớp cha | id | Ghi chú |
|---|---|---|---|---|---|
| Hotel | Thực thể | M00 | — | Có | — |
| Room | Thực thể | M00 | — | Có | — |
| Client | Thực thể | M00 | — | Có | — |
| User | Thực thể | M00 | — | Có | — |
| Booking | Thực thể | M00 | — | Có | — |
| BookedRoom | Liên kết | M00 | — | Có | — |
| Bill | Thực thể | M00 | — | Có | — |
| Service | Thực thể | M00 | — | Có | — |
| UsedService | Liên kết | M00 | — | Có | — |
| HotelStat | Thống kê | M00 | Hotel | Kế thừa | Dùng id của Hotel |
| RoomStat | Thống kê | M00 | Room | Kế thừa | Dùng id của Room |
| ClientStat | Thống kê | M00 | Client | Kế thừa | Dùng id của Client |
| ServiceStat | Thống kê | M00 | Service | Kế thừa | Dùng id của Service |
| IncomeStat | Thống kê | M00 | — | Không | Lớp thống kê không kế thừa: không lưu, không cần định danh |

## 2. Thuộc tính và kiểu

### 2.1 Thuộc tính

| Lớp | Thuộc tính | Kiểu | Bắt buộc | Ràng buộc | Tính chất | Căn cứ kiểu |
|---|---|---|---|---|---|---|
| Hotel | id | int | Có | Duy nhất | Khóa | QU-02 |
| Hotel | name | String | Có | — | Lưu | CS |
| Hotel | starLevel | int | Có | — | Lưu | CS |
| Hotel | address | String | Có | — | Lưu | CS |
| Hotel | description | String | Không | — | Lưu | CS |
| Room | id | int | Có | Duy nhất | Khóa | QU-02 |
| Room | name | String | Có | — | Lưu | CS |
| Room | type | String | Có | — | Lưu | CS |
| Room | price | float | Có | — | Lưu | CS |
| Room | description | String | Không | — | Lưu | CS |
| Client | id | int | Có | Duy nhất | Khóa | QU-02 |
| Client | idCard | String | Có | — | Lưu | CS |
| Client | fullName | String | Có | — | Lưu | CS |
| Client | address | String | Có | — | Lưu | CS |
| Client | email | String | Không | — | Lưu | CS |
| Client | tel | String | Có | — | Lưu | CS |
| Client | note | String | Không | — | Lưu | CS |
| User | id | int | Có | Duy nhất | Khóa | QU-02 |
| User | username | String | Có | — | Lưu | CS |
| User | password | String | Có | — | Lưu | CS |
| User | fullName | String | Có | — | Lưu | CS |
| User | position | String | Có | — | Lưu | CS |
| Booking | id | int | Có | Duy nhất | Khóa | QU-02 |
| Booking | bookDay | Date | Có | — | Lưu | CS |
| Booking | totalAmount | float | Có | — | Dẫn xuất | CS |
| Booking | note | String | Không | — | Lưu | CS |
| BookedRoom | id | int | Có | Duy nhất | Khóa | QU-02 |
| BookedRoom | checkin | Date | Có | — | Lưu | CS |
| BookedRoom | checkout | Date | Có | — | Lưu | CS |
| BookedRoom | price | float | Có | — | Lưu | CS |
| BookedRoom | note | String | Không | — | Lưu | CS |
| BookedRoom | amount | float | Có | — | Dẫn xuất | CS |
| BookedRoom | isCheckedIn | boolean | Có | — | Lưu | CS |
| Bill | id | int | Có | Duy nhất | Khóa | QU-02 |
| Bill | paymentDate | Date | Có | — | Lưu | CS |
| Bill | amount | float | Có | — | Lưu | CS |
| Bill | paymentType | String | Có | — | Lưu | CS |
| Bill | note | String | Không | — | Lưu | CS |
| Service | id | int | Có | Duy nhất | Khóa | QU-02 |
| Service | name | String | Có | — | Lưu | CS |
| Service | unity | String | Có | — | Lưu | CS |
| Service | price | float | Có | — | Lưu | CS |
| UsedService | id | int | Có | Duy nhất | Khóa | QU-02 |
| UsedService | price | float | Có | — | Lưu | CS |
| UsedService | quantity | int | Có | — | Lưu | CS |
| UsedService | totalAmount | float | Có | — | Dẫn xuất | CS |
| HotelStat | revenue | float | Có | — | Dẫn xuất | CS |
| HotelStat | fillRate | float | Có | — | Dẫn xuất | CS |
| RoomStat | fillDay | int | Có | — | Dẫn xuất | CS |
| RoomStat | fillRate | float | Có | — | Dẫn xuất | CS |
| RoomStat | revenue | float | Có | — | Dẫn xuất | CS |
| ClientStat | day | int | Có | — | Dẫn xuất | CS |
| ClientStat | payment | float | Có | — | Dẫn xuất | CS |
| ServiceStat | amount | int | Có | — | Dẫn xuất | CS |
| ServiceStat | revenue | float | Có | — | Dẫn xuất | CS |
| IncomeStat | period | String | Có | — | Dẫn xuất | CS |
| IncomeStat | client | int | Có | — | Dẫn xuất | CS |
| IncomeStat | revenue | float | Có | — | Dẫn xuất | CS |

### 2.2 Kiểu liệt kê

Case study không dùng kiểu liệt kê (User.position là String).

| Kiểu | Giá trị | Dùng ở | Nguồn |
|---|---|---|---|
| — | — | — | — |

## 3. Chuyển quan hệ

### 3.1 Quan hệ thành phần – toàn thể

"Dạng" đọc theo thứ tự thành phần–toàn thể: `n-1` là n thành phần thuộc 1 toàn thể; `1-n` là 1 thành phần được n toàn
thể dùng.

| ID | Thành phần | Toàn thể | Bội số thành phần | Bội số toàn thể | Dạng | Loại | Loại ở phân tích | Căn cứ |
|---|---|---|---|---|---|---|---|---|
| R-M00-01 | Room | Hotel | 0..* | 1 | n-1 | Hợp thành | Hợp thành | Giữ nguyên từ phân tích |
| R-M00-02 | Client | Booking | 1 | 0..* | 1-n | Kết tập | Kết tập | Giữ nguyên từ phân tích |
| R-M00-03 | BookedRoom | Booking | 1..* | 1 | n-1 | Kết tập | Liên kết | Room + Booking → BookedRoom: lượt đặt phòng là nơi tạo và chứa các phòng đã đặt, nên BookedRoom là thành phần của Booking |
| R-M00-04 | Room | BookedRoom | 1 | 0..* | 1-n | Kết tập | Liên kết | Room + Booking → BookedRoom: phòng có sẵn từ trước và được tham chiếu, nên Room là thành phần của BookedRoom |
| R-M00-05 | Booking | Bill | 1 | 0..* | 1-n | Kết tập | Kết tập | Giữ nguyên từ phân tích |
| R-M00-06 | User | Bill | 1 | 0..* | 1-n | Kết tập | Kết tập | Giữ nguyên từ phân tích |
| R-M00-07 | User | Booking | 1 | 0..* | 1-n | Kết tập | Kết tập | Giữ nguyên từ phân tích |
| R-M00-08 | UsedService | BookedRoom | 0..* | 1 | n-1 | Kết tập | Liên kết | BookedRoom + Service → UsedService: phòng đã đặt là nơi phát sinh và chứa các dịch vụ đã dùng |
| R-M00-09 | Service | UsedService | 1 | 0..* | 1-n | Kết tập | Liên kết | BookedRoom + Service → UsedService: dịch vụ có sẵn từ trước và được tham chiếu |

### 3.2 Quan hệ giữ nguyên

| ID | Loại | Lớp | Lớp đích | Ghi chú |
|---|---|---|---|---|
| R-M00-10 | Kế thừa | HotelStat | Hotel | — |
| R-M00-11 | Kế thừa | RoomStat | Room | — |
| R-M00-12 | Kế thừa | ServiceStat | Service | — |
| R-M00-13 | Kế thừa | ClientStat | Client | — |
| R-M00-14 | Phụ thuộc | IncomeStat | Bill | IncomeStat chỉ dùng Bill để tính, không giữ đối tượng Bill |

## 4. Thuộc tính đối tượng

| Quan hệ | Lớp chứa | Thuộc tính | Kiểu | Quy tắc |
|---|---|---|---|---|
| R-M00-01 | Hotel | rooms | Room[] | Room là thành phần của Hotel, dạng n-1 → Hotel có danh sách Room |
| R-M00-02 | Booking | client | Client | Client là thành phần của Booking, dạng 1-n → Booking có một Client |
| R-M00-03 | Booking | bookedRooms | BookedRoom[] | BookedRoom là thành phần của Booking, dạng n-1 → Booking có danh sách BookedRoom |
| R-M00-04 | BookedRoom | room | Room | Room là thành phần của BookedRoom, dạng 1-n → BookedRoom có một Room |
| R-M00-05 | Bill | booking | Booking | Booking là thành phần của Bill, dạng 1-n → Bill có một Booking |
| R-M00-06 | Bill | user | User | User là thành phần của Bill, dạng 1-n → Bill có một User |
| R-M00-07 | Booking | user | User | User là thành phần của Booking, dạng 1-n → Booking có một User |
| R-M00-08 | BookedRoom | usedServices | UsedService[] | UsedService là thành phần của BookedRoom, dạng n-1 → BookedRoom có danh sách UsedService |
| R-M00-09 | UsedService | service | Service | Service là thành phần của UsedService, dạng 1-n → UsedService có một Service |

## 5. Sơ đồ lớp thiết kế

<!-- BEGIN:DIAGRAM -->
![Sơ đồ lớp thiết kế — CD-M00](diagrams/CD-M00.png)

Mã nguồn sơ đồ: [diagrams/CD-M00.puml](diagrams/CD-M00.puml). Ảnh và tệp .puml do `gen_puml.py` sinh từ các bảng của tài liệu này; muốn đổi sơ đồ thì sửa bảng rồi chạy lại tool, không sửa tay.
<!-- END:DIAGRAM -->

## 6. Liên module

Ví dụ chỉ có một module.

| Lớp | Module sở hữu | Module này dùng thế nào | Đề nghị cho module sở hữu |
|---|---|---|---|
| — | — | — | — |

## 7. Quyết định thiết kế

| Mã | Quyết định | Lý do |
|---|---|---|
| DD-M00-01 | Mọi id kiểu int, kể cả Room | Case study gốc để Room.id kiểu String; ví dụ dùng một kiểu cho thống nhất |
| DD-M00-02 | Quan hệ chuyển từ Liên kết đều ghi Kết tập | Case study không nói thành phần bị xóa theo toàn thể; hình kết quả vẽ hình thoi rỗng |
| DD-M00-03 | Tên thuộc tính danh sách dùng số nhiều (rooms, bookedRooms, usedServices) | Theo QU-05; case study gốc đặt listRoom, rooms, usedService không thống nhất |

## 8. Câu hỏi và điểm chưa chốt

| Mã | Loại | Câu hỏi | Trả lời | Ghi vào |
|---|---|---|---|---|
| — | — | — | — | — |

## 9. Lịch sử sửa đổi

| Phiên bản | Ngày | Nội dung | Người sửa |
|---|---|---|---|
| 1.0 | 2026-11-15 | Dựng từ case study quản lý khách sạn | (ví dụ) |
