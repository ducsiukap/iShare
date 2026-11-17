---
module: M00
ten_module: Ví dụ — Quản lý khách sạn
ma_tai_lieu: DB-M00
phien_ban: 1.0
trang_thai: Đã chốt
ngay: 2026-11-15
tac_gia: (ví dụ)
nguon: CD-M00 v1.0
steps_completed: [1, 2, 3, 4, 5]
---
# Thiết kế cơ sở dữ liệu — M00 Ví dụ: Quản lý khách sạn

<!-- Case study của phương pháp, viết lại theo đúng mẫu db-template.md.
     Đầu vào là ví dụ của skill designing-entity-classes (output/example.md, tức CD-M00).
     Độ dài varchar lấy theo hình kết quả của case study.
     Tên bảng và cột viết snake_case theo quy ước của dự án (QU-06…08); hình gốc của case study dùng tiền tố tbl và camelCase. -->

## 1. Bảng

| Bảng | Từ lớp | Nhóm | Sở hữu | Ghi chú |
|---|---|---|---|---|
| hotels | Hotel | Thực thể | M00 | — |
| rooms | Room | Thực thể | M00 | — |
| clients | Client | Thực thể | M00 | — |
| users | User | Thực thể | M00 | — |
| bookings | Booking | Thực thể | M00 | — |
| booked_rooms | BookedRoom | Liên kết | M00 | — |
| bills | Bill | Thực thể | M00 | — |
| services | Service | Thực thể | M00 | — |
| used_services | UsedService | Liên kết | M00 | — |
| hotel_stats | HotelStat | Thống kê | M00 | — |
| room_stats | RoomStat | Thống kê | M00 | — |
| client_stats | ClientStat | Thống kê | M00 | — |
| service_stats | ServiceStat | Thống kê | M00 | — |
| income_stats | IncomeStat | Thống kê | M00 | — |

## 2. Cột

### 2.1 Cột từ thuộc tính

| Bảng | Cột | Kiểu | Null | Duy nhất | Từ thuộc tính | Ghi chú |
|---|---|---|---|---|---|---|
| hotels | id | integer | Không | Có | Hotel.id | — |
| hotels | name | varchar(50) | Không | Không | Hotel.name | — |
| hotels | star_level | integer | Không | Không | Hotel.starLevel | — |
| hotels | address | varchar(250) | Không | Không | Hotel.address | — |
| hotels | description | varchar(500) | Có | Không | Hotel.description | — |
| rooms | id | integer | Không | Có | Room.id | — |
| rooms | name | varchar(50) | Không | Không | Room.name | — |
| rooms | type | varchar(50) | Không | Không | Room.type | — |
| rooms | price | real | Không | Không | Room.price | — |
| rooms | description | varchar(250) | Có | Không | Room.description | — |
| clients | id | integer | Không | Có | Client.id | — |
| clients | id_card | varchar(20) | Không | Không | Client.idCard | — |
| clients | full_name | varchar(50) | Không | Không | Client.fullName | — |
| clients | address | varchar(250) | Không | Không | Client.address | — |
| clients | email | varchar(50) | Có | Không | Client.email | — |
| clients | tel | varchar(20) | Không | Không | Client.tel | — |
| clients | note | varchar(250) | Có | Không | Client.note | — |
| users | id | integer | Không | Có | User.id | — |
| users | username | varchar(25) | Không | Không | User.username | — |
| users | password | varchar(25) | Không | Không | User.password | — |
| users | full_name | varchar(50) | Không | Không | User.fullName | — |
| users | position | varchar(50) | Không | Không | User.position | — |
| bookings | id | integer | Không | Có | Booking.id | — |
| bookings | book_day | date | Không | Không | Booking.bookDay | — |
| bookings | total_amount | real | Không | Không | Booking.totalAmount | — |
| bookings | note | varchar(250) | Có | Không | Booking.note | — |
| booked_rooms | id | integer | Không | Có | BookedRoom.id | — |
| booked_rooms | checkin | date | Không | Không | BookedRoom.checkin | — |
| booked_rooms | checkout | date | Không | Không | BookedRoom.checkout | — |
| booked_rooms | price | real | Không | Không | BookedRoom.price | — |
| booked_rooms | note | varchar(250) | Có | Không | BookedRoom.note | — |
| booked_rooms | amount | real | Không | Không | BookedRoom.amount | — |
| booked_rooms | is_checked_in | boolean | Không | Không | BookedRoom.isCheckedIn | — |
| bills | id | integer | Không | Có | Bill.id | — |
| bills | payment_date | date | Không | Không | Bill.paymentDate | — |
| bills | amount | real | Không | Không | Bill.amount | — |
| bills | payment_type | varchar(50) | Không | Không | Bill.paymentType | — |
| bills | note | varchar(250) | Có | Không | Bill.note | — |
| services | id | integer | Không | Có | Service.id | — |
| services | name | varchar(50) | Không | Không | Service.name | — |
| services | unity | varchar(50) | Không | Không | Service.unity | — |
| services | price | real | Không | Không | Service.price | — |
| used_services | id | integer | Không | Có | UsedService.id | — |
| used_services | price | real | Không | Không | UsedService.price | — |
| used_services | quantity | integer | Không | Không | UsedService.quantity | — |
| used_services | total_amount | real | Không | Không | UsedService.totalAmount | — |
| hotel_stats | revenue | real | Không | Không | HotelStat.revenue | — |
| hotel_stats | fill_rate | real | Không | Không | HotelStat.fillRate | — |
| room_stats | fill_day | integer | Không | Không | RoomStat.fillDay | — |
| room_stats | fill_rate | real | Không | Không | RoomStat.fillRate | — |
| room_stats | revenue | real | Không | Không | RoomStat.revenue | — |
| client_stats | day | integer | Không | Không | ClientStat.day | — |
| client_stats | payment | real | Không | Không | ClientStat.payment | — |
| service_stats | amount | integer | Không | Không | ServiceStat.amount | — |
| service_stats | revenue | real | Không | Không | ServiceStat.revenue | — |
| income_stats | period | varchar(50) | Không | Không | IncomeStat.period | — |
| income_stats | client | integer | Không | Không | IncomeStat.client | — |
| income_stats | revenue | real | Không | Không | IncomeStat.revenue | — |

### 2.2 Thuộc tính đối tượng không chuyển

| Lớp | Thuộc tính | Kiểu | Lý do không chuyển |
|---|---|---|---|
| Hotel | rooms | Room[] | Thuộc tính đối tượng; được thay bằng khóa ngoại rooms.hotel_id ở bước 4 |
| Booking | client | Client | Thuộc tính đối tượng; được thay bằng khóa ngoại bookings.client_id ở bước 4 |
| Booking | bookedRooms | BookedRoom[] | Thuộc tính đối tượng; được thay bằng khóa ngoại booked_rooms.booking_id ở bước 4 |
| Booking | user | User | Thuộc tính đối tượng; được thay bằng khóa ngoại bookings.user_id ở bước 4 |
| BookedRoom | room | Room | Thuộc tính đối tượng; được thay bằng khóa ngoại booked_rooms.room_id ở bước 4 |
| BookedRoom | usedServices | UsedService[] | Thuộc tính đối tượng; được thay bằng khóa ngoại used_services.booked_room_id ở bước 4 |
| Bill | booking | Booking | Thuộc tính đối tượng; được thay bằng khóa ngoại bills.booking_id ở bước 4 |
| Bill | user | User | Thuộc tính đối tượng; được thay bằng khóa ngoại bills.user_id ở bước 4 |
| UsedService | service | Service | Thuộc tính đối tượng; được thay bằng khóa ngoại used_services.service_id ở bước 4 |

## 3. Quan hệ giữa các bảng

"Dạng" đọc theo thứ tự Bảng A – Bảng B.

| ID | Bảng A | Bảng B | Dạng | Xử lý | Ghi chú |
|---|---|---|---|---|---|
| R-M00-01 | hotels | rooms | 1-n | Tách riêng | — |
| R-M00-02 | clients | bookings | 1-n | Tách riêng | — |
| R-M00-03 | bookings | booked_rooms | 1-n | Tách riêng | — |
| R-M00-04 | rooms | booked_rooms | 1-n | Tách riêng | — |
| R-M00-05 | bookings | bills | 1-n | Tách riêng | — |
| R-M00-06 | users | bills | 1-n | Tách riêng | — |
| R-M00-07 | users | bookings | 1-n | Tách riêng | — |
| R-M00-08 | booked_rooms | used_services | 1-n | Tách riêng | — |
| R-M00-09 | services | used_services | 1-n | Tách riêng | — |
| R-M00-10 | hotels | hotel_stats | 1-1 | Cha–con | Kế thừa: bảng con không có id riêng, dùng khóa của bảng cha |
| R-M00-11 | rooms | room_stats | 1-1 | Cha–con | Kế thừa: bảng con không có id riêng, dùng khóa của bảng cha |
| R-M00-12 | services | service_stats | 1-1 | Cha–con | Kế thừa: bảng con không có id riêng, dùng khóa của bảng cha |
| R-M00-13 | clients | client_stats | 1-1 | Cha–con | Kế thừa: bảng con không có id riêng, dùng khóa của bảng cha |

R-M00-14 (IncomeStat phụ thuộc Bill) không sinh quan hệ giữa các bảng. Không có quan hệ n-n.

## 4. Khóa

### 4.1 Khóa chính

| Bảng | Khóa chính | Ghi chú |
|---|---|---|
| hotels | id | — |
| rooms | id | — |
| clients | id | — |
| users | id | — |
| bookings | id | — |
| booked_rooms | id | — |
| bills | id | — |
| services | id | — |
| used_services | id | — |
| hotel_stats | hotel_id | Bảng con: khóa chính là khóa ngoại tới bảng cha |
| room_stats | room_id | Bảng con: khóa chính là khóa ngoại tới bảng cha |
| client_stats | client_id | Bảng con: khóa chính là khóa ngoại tới bảng cha |
| service_stats | service_id | Bảng con: khóa chính là khóa ngoại tới bảng cha |
| income_stats | Không có | Lớp thống kê không có id; bảng bị loại ở bước 5 |

### 4.2 Khóa ngoại

| Bảng | Cột | Kiểu | Null | Duy nhất | Tham chiếu | Từ quan hệ | Ghi chú |
|---|---|---|---|---|---|---|---|
| rooms | hotel_id | integer | Không | Không | hotels(id) | R-M00-01 | 1 hotels – n rooms |
| bookings | client_id | integer | Không | Không | clients(id) | R-M00-02 | 1 clients – n bookings |
| booked_rooms | booking_id | integer | Không | Không | bookings(id) | R-M00-03 | 1 bookings – n booked_rooms |
| booked_rooms | room_id | integer | Không | Không | rooms(id) | R-M00-04 | 1 rooms – n booked_rooms |
| bills | booking_id | integer | Không | Không | bookings(id) | R-M00-05 | 1 bookings – n bills |
| bills | user_id | integer | Không | Không | users(id) | R-M00-06 | 1 users – n bills |
| bookings | user_id | integer | Không | Không | users(id) | R-M00-07 | 1 users – n bookings |
| used_services | booked_room_id | integer | Không | Không | booked_rooms(id) | R-M00-08 | 1 booked_rooms – n used_services |
| used_services | service_id | integer | Không | Không | services(id) | R-M00-09 | 1 services – n used_services |
| hotel_stats | hotel_id | integer | Không | Có | hotels(id) | R-M00-10 | Cha–con |
| room_stats | room_id | integer | Không | Có | rooms(id) | R-M00-11 | Cha–con |
| service_stats | service_id | integer | Không | Có | services(id) | R-M00-12 | Cha–con |
| client_stats | client_id | integer | Không | Có | clients(id) | R-M00-13 | Cha–con |

## 5. Loại dư thừa

### 5.1 Cột bị loại

| Bảng | Cột | Loại dư thừa | Căn cứ | Cách có lại giá trị |
|---|---|---|---|---|
| bookings | total_amount | Dẫn xuất | Thuộc tính dẫn xuất ở CD-M00 | Cộng thành tiền của các booked_rooms và used_services thuộc lượt đặt |
| booked_rooms | amount | Dẫn xuất | Thuộc tính dẫn xuất ở CD-M00 | price × số ngày giữa checkin và checkout |
| used_services | total_amount | Dẫn xuất | Thuộc tính dẫn xuất ở CD-M00 | quantity × price |
| hotel_stats | revenue | Dẫn xuất | Thuộc tính của lớp thống kê | Tổng bills.amount của các lượt đặt có phòng thuộc khách sạn |
| hotel_stats | fill_rate | Dẫn xuất | Thuộc tính của lớp thống kê | Số ngày-phòng có khách (từ booked_rooms) chia tổng số ngày-phòng của khách sạn |
| room_stats | fill_day | Dẫn xuất | Thuộc tính của lớp thống kê | Tổng số ngày giữa checkin và checkout của booked_rooms theo phòng |
| room_stats | fill_rate | Dẫn xuất | Thuộc tính của lớp thống kê | fill_day chia số ngày của kỳ thống kê |
| room_stats | revenue | Dẫn xuất | Thuộc tính của lớp thống kê | Tổng thành tiền của booked_rooms theo phòng |
| client_stats | day | Dẫn xuất | Thuộc tính của lớp thống kê | Tổng số ngày lưu trú từ booked_rooms của các lượt đặt của khách |
| client_stats | payment | Dẫn xuất | Thuộc tính của lớp thống kê | Tổng bills.amount của các lượt đặt của khách |
| service_stats | amount | Dẫn xuất | Thuộc tính của lớp thống kê | Tổng used_services.quantity theo dịch vụ |
| service_stats | revenue | Dẫn xuất | Thuộc tính của lớp thống kê | Tổng quantity × price của used_services theo dịch vụ |
| income_stats | period | Dẫn xuất | Thuộc tính của lớp thống kê | Nhóm bills.payment_date theo kỳ |
| income_stats | client | Dẫn xuất | Thuộc tính của lớp thống kê | Đếm khách khác nhau có bills trong kỳ |
| income_stats | revenue | Dẫn xuất | Thuộc tính của lớp thống kê | Tổng bills.amount trong kỳ |

### 5.2 Bảng bị loại

| Bảng | Lý do |
|---|---|
| hotel_stats | Sau khi loại cột dẫn xuất chỉ còn một khóa ngoại |
| room_stats | Sau khi loại cột dẫn xuất chỉ còn một khóa ngoại |
| client_stats | Sau khi loại cột dẫn xuất chỉ còn một khóa ngoại |
| service_stats | Sau khi loại cột dẫn xuất chỉ còn một khóa ngoại |
| income_stats | Sau khi loại cột dẫn xuất không còn cột nào |

### 5.3 Dẫn xuất nhưng giữ lại

Không có.

| Bảng | Cột | Lý do giữ | Nguồn |
|---|---|---|---|
| — | — | — | — |

### 5.4 Đã xét nhưng không coi là dư thừa

| Bảng | Cột | Vì sao không dư thừa |
|---|---|---|
| booked_rooms | price | Giá tại thời điểm đặt; rooms.price là giá niêm yết hiện tại và có thể đã đổi, nên không tính lại được |
| used_services | price | Đơn giá tại thời điểm dùng; services.price là giá niêm yết hiện tại |
| clients, users | full_name | Cùng tên cột nhưng của hai đối tượng khác nhau (khách hàng, người dùng) |
| bills | amount | Số tiền thực trả của một lần thanh toán; một lượt đặt có thể trả nhiều lần nên không suy ra được từ tổng tiền |

## 6. Lược đồ cuối

### 6.1 Bảng và cột

<!-- BEGIN:SCHEMA -->
| Bảng | Cột | Kiểu | Khóa | Null | Duy nhất | Tham chiếu |
|---|---|---|---|---|---|---|
| hotels | id | integer | PK | Không | Có | — |
| hotels | name | varchar(50) | — | Không | Không | — |
| hotels | star_level | integer | — | Không | Không | — |
| hotels | address | varchar(250) | — | Không | Không | — |
| hotels | description | varchar(500) | — | Có | Không | — |
| rooms | id | integer | PK | Không | Có | — |
| rooms | name | varchar(50) | — | Không | Không | — |
| rooms | type | varchar(50) | — | Không | Không | — |
| rooms | price | real | — | Không | Không | — |
| rooms | description | varchar(250) | — | Có | Không | — |
| rooms | hotel_id | integer | FK | Không | Không | hotels(id) |
| clients | id | integer | PK | Không | Có | — |
| clients | id_card | varchar(20) | — | Không | Không | — |
| clients | full_name | varchar(50) | — | Không | Không | — |
| clients | address | varchar(250) | — | Không | Không | — |
| clients | email | varchar(50) | — | Có | Không | — |
| clients | tel | varchar(20) | — | Không | Không | — |
| clients | note | varchar(250) | — | Có | Không | — |
| users | id | integer | PK | Không | Có | — |
| users | username | varchar(25) | — | Không | Không | — |
| users | password | varchar(25) | — | Không | Không | — |
| users | full_name | varchar(50) | — | Không | Không | — |
| users | position | varchar(50) | — | Không | Không | — |
| bookings | id | integer | PK | Không | Có | — |
| bookings | book_day | date | — | Không | Không | — |
| bookings | note | varchar(250) | — | Có | Không | — |
| bookings | client_id | integer | FK | Không | Không | clients(id) |
| bookings | user_id | integer | FK | Không | Không | users(id) |
| booked_rooms | id | integer | PK | Không | Có | — |
| booked_rooms | checkin | date | — | Không | Không | — |
| booked_rooms | checkout | date | — | Không | Không | — |
| booked_rooms | price | real | — | Không | Không | — |
| booked_rooms | note | varchar(250) | — | Có | Không | — |
| booked_rooms | is_checked_in | boolean | — | Không | Không | — |
| booked_rooms | booking_id | integer | FK | Không | Không | bookings(id) |
| booked_rooms | room_id | integer | FK | Không | Không | rooms(id) |
| bills | id | integer | PK | Không | Có | — |
| bills | payment_date | date | — | Không | Không | — |
| bills | amount | real | — | Không | Không | — |
| bills | payment_type | varchar(50) | — | Không | Không | — |
| bills | note | varchar(250) | — | Có | Không | — |
| bills | booking_id | integer | FK | Không | Không | bookings(id) |
| bills | user_id | integer | FK | Không | Không | users(id) |
| services | id | integer | PK | Không | Có | — |
| services | name | varchar(50) | — | Không | Không | — |
| services | unity | varchar(50) | — | Không | Không | — |
| services | price | real | — | Không | Không | — |
| used_services | id | integer | PK | Không | Có | — |
| used_services | price | real | — | Không | Không | — |
| used_services | quantity | integer | — | Không | Không | — |
| used_services | booked_room_id | integer | FK | Không | Không | booked_rooms(id) |
| used_services | service_id | integer | FK | Không | Không | services(id) |
<!-- END:SCHEMA -->

### 6.2 Sơ đồ quan hệ

<!-- BEGIN:DIAGRAM -->
![Sơ đồ quan hệ — DB-M00](diagrams/DB-M00.png)

Mã nguồn sơ đồ: [diagrams/DB-M00.puml](diagrams/DB-M00.puml). Ảnh và tệp .puml do `build_schema.py` sinh từ các bảng của tài liệu này; muốn đổi sơ đồ thì sửa bảng rồi chạy lại tool, không sửa tay.
<!-- END:DIAGRAM -->

## 7. Liên module

Ví dụ chỉ có một module.

### 7.1 Bảng của module khác được tham chiếu

| Bảng ngoài | Module sở hữu | Dùng thế nào |
|---|---|---|
| — | — | — |

### 7.2 Khóa ngoại đề nghị cho bảng của module khác

| Bảng của module khác | Cột | Kiểu | Tham chiếu | Từ quan hệ |
|---|---|---|---|---|
| — | — | — | — | — |

## 8. Quyết định thiết kế

| Mã | Quyết định | Lý do |
|---|---|---|
| DD-M00-01 | Tên bảng, cột, khóa ngoại viết snake_case: `hotels`, `star_level`, `hotel_id` | Theo QU-06, QU-07, QU-08 của dự án. Hình kết quả của case study gốc dùng tiền tố tbl cho bảng, camelCase cho cột, và đặt khóa ngoại không thống nhất |
| DD-M00-02 | Không có cột selloff | Hình CSDL của case study có cột selloff nhưng sơ đồ lớp thiết kế không có thuộc tính này; cột chỉ được sinh từ thuộc tính |

## 9. Câu hỏi và điểm chưa chốt

| Mã | Loại | Câu hỏi | Trả lời | Ghi vào |
|---|---|---|---|---|
| — | — | — | — | — |

## 10. Lịch sử sửa đổi

| Phiên bản | Ngày | Nội dung | Người sửa |
|---|---|---|---|
| 1.0 | 2026-11-15 | Dựng từ case study quản lý khách sạn | (ví dụ) |
