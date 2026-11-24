---
module: M00
ten_module: Ví dụ — Quản lý khách sạn
ma_tai_lieu: EC-M00
phien_ban: 1.0
trang_thai: Đã chốt
ngay: 2026-11-15
tac_gia: (ví dụ)
nguon: Case study quản lý khách sạn
steps_completed: [1, 2, 3]
---
# Phân tích lớp thực thể — M00 Ví dụ: Quản lý khách sạn

<!-- Đây là case study của phương pháp, viết lại theo đúng mẫu ec-template.md để agent thấy hình dạng kết quả.
     Ví dụ không có tài liệu FR nên cột Nguồn ghi số câu ("Câu 2") hoặc "CS" (hình kết quả của case study).
     Với module thật của iShare, cột Nguồn phải ghi mã FR-/BR- hoặc "TN:<thuật ngữ>" (mục 2.1 của FR).
     Đoạn mô tả của case study gần như không nêu thuộc tính, nên phần lớn thuộc tính ở mục 2.3 là "Đề xuất":
     mỗi đề xuất ghi chức năng nào cần nó. Các đề xuất này trùng với hình kết quả của case study. -->

## 1. Mô tả chức năng

### 1.1 Đoạn mô tả

Hệ thống hỗ trợ quản lý thông tin về khách sạn, phòng của khách sạn và khách hàng đặt phòng tại khách sạn. Hệ thống
cho phép người quản lý khách sạn quản lý thông tin khách sạn và phòng, và xem các báo cáo thống kê: thống kê phòng,
thống kê khách sạn, thống kê khách hàng, thống kê dịch vụ và thống kê doanh thu.

Hệ thống cho phép quản trị viên quản lý tài khoản cho người dùng của hệ thống khi có yêu cầu. Hệ thống cho phép nhân
viên bán hàng tạo lượt đặt phòng và hủy lượt đặt phòng cho khách hàng ở xa qua điện thoại. Hệ thống cho phép lễ tân
tạo lượt đặt phòng, hủy lượt đặt phòng, làm thủ tục nhận phòng, trả phòng và xử lý thanh toán cho khách hàng tại quầy
lễ tân. Mỗi khi một lần thanh toán được xử lý, hệ thống tạo một hóa đơn gồm thông tin về khách hàng, các phòng đã đặt
và các dịch vụ khách hàng đã dùng trong thời gian lưu trú.

### 1.2 Truy vết câu

| Câu | Nội dung câu | Nguồn |
|---|---|---|
| 1 | Hệ thống hỗ trợ quản lý thông tin về khách sạn, phòng của khách sạn và khách hàng đặt phòng tại khách sạn. | CS |
| 2 | Hệ thống cho phép người quản lý khách sạn quản lý thông tin khách sạn và phòng, và xem các báo cáo thống kê: thống kê phòng, thống kê khách sạn, thống kê khách hàng, thống kê dịch vụ và thống kê doanh thu. | CS |
| 3 | Hệ thống cho phép quản trị viên quản lý tài khoản cho người dùng của hệ thống khi có yêu cầu. | CS |
| 4 | Hệ thống cho phép nhân viên bán hàng tạo lượt đặt phòng và hủy lượt đặt phòng cho khách hàng ở xa qua điện thoại. | CS |
| 5 | Hệ thống cho phép lễ tân tạo lượt đặt phòng, hủy lượt đặt phòng, làm thủ tục nhận phòng, trả phòng và xử lý thanh toán cho khách hàng tại quầy lễ tân. | CS |
| 6 | Mỗi khi một lần thanh toán được xử lý, hệ thống tạo một hóa đơn gồm thông tin về khách hàng, các phòng đã đặt và các dịch vụ khách hàng đã dùng trong thời gian lưu trú. | CS |

## 2. Danh từ và phân loại

### 2.1 Sổ danh từ

| # | Danh từ | Xuất hiện ở | Phân loại | Kết quả | Lý do |
|---|---|---|---|---|---|
| 1 | hệ thống | Câu 1 | Loại bỏ | — | Trừu tượng: chỉ chính phần mềm |
| 2 | thông tin | Câu 1 | Loại bỏ | — | Chung chung: không chỉ một đối tượng cụ thể |
| 3 | khách sạn | Câu 1 | Lớp | Hotel | Cần được quản lý (thêm, sửa, xem) |
| 4 | phòng | Câu 1 | Lớp | Room | Cần được quản lý |
| 5 | khách hàng | Câu 1 | Lớp | Client | Cần được quản lý |
| 6 | người quản lý | Câu 2 | Lớp | User | Một loại người dùng của hệ thống; phân biệt bằng User.position |
| 7 | báo cáo thống kê | Câu 2 | Loại bỏ | — | Chung chung: từng loại thống kê cụ thể xét ở dòng 8–12 |
| 8 | thống kê phòng | Câu 2 | Lớp | RoomStat | Lớp thống kê: số liệu tính từ dữ liệu phòng |
| 9 | thống kê khách sạn | Câu 2 | Lớp | HotelStat | Lớp thống kê |
| 10 | thống kê khách hàng | Câu 2 | Lớp | ClientStat | Lớp thống kê |
| 11 | thống kê dịch vụ | Câu 2 | Lớp | ServiceStat | Lớp thống kê |
| 12 | thống kê doanh thu | Câu 2 | Lớp | IncomeStat | Lớp thống kê |
| 13 | quản trị viên | Câu 3 | Lớp | User | Một loại người dùng |
| 14 | tài khoản / người dùng | Câu 3 | Lớp | User | Cần được quản lý; "tài khoản" và "người dùng" chỉ cùng một đối tượng |
| 15 | yêu cầu | Câu 3 | Loại bỏ | — | Chung chung: không phải dữ liệu hệ thống lưu |
| 16 | nhân viên bán hàng | Câu 4 | Lớp | User | Một loại người dùng |
| 17 | lượt đặt phòng | Câu 4 | Lớp | Booking | Hệ thống phải lưu từng lần đặt để hủy, nhận phòng, thanh toán |
| 18 | điện thoại | Câu 4 | Loại bỏ | — | Ngoài phạm vi hệ thống: kênh liên lạc, hệ thống không lưu |
| 19 | lễ tân | Câu 5 | Lớp | User | Một loại người dùng |
| 20 | lần thanh toán / hóa đơn | Câu 5 | Lớp | Bill | Mỗi lần thanh toán được lưu thành một hóa đơn |
| 21 | quầy lễ tân | Câu 5 | Loại bỏ | — | Ngoài phạm vi hệ thống: nơi chốn, hệ thống không lưu |
| 22 | phòng đã đặt | Câu 6 | Lớp | BookedRoom | Một phòng trong một lượt đặt, có ngày nhận, ngày trả, giá riêng |
| 23 | dịch vụ | Câu 6 | Lớp | Service | Cần được quản lý |
| 24 | thời gian lưu trú | Câu 6 | Loại bỏ | — | Không lưu riêng: suy ra từ BookedRoom.checkin và BookedRoom.checkout |

### 2.2 Lớp

| Lớp | Tên tiếng Việt | Nhóm | Sở hữu | Mô tả | Thuộc tính | Nguồn |
|---|---|---|---|---|---|---|
| Hotel | Khách sạn | Thực thể | M00 | Khách sạn được quản lý trong hệ thống | name, starLevel, address, description | Câu 1, Câu 2 |
| Room | Phòng | Thực thể | M00 | Phòng của một khách sạn | name, type, price, description | Câu 1, Câu 2 |
| Client | Khách hàng | Thực thể | M00 | Người đặt phòng | idCard, fullName, address, email, tel, note | Câu 1, Câu 4, Câu 5 |
| User | Người dùng | Thực thể | M00 | Tài khoản của người quản lý, quản trị viên, nhân viên bán hàng, lễ tân | username, password, fullName, position | Câu 2, Câu 3, Câu 4, Câu 5 |
| Booking | Lượt đặt phòng | Thực thể | M00 | Một lần khách hàng đặt một hoặc nhiều phòng | bookDay, /totalAmount, note | Câu 4, Câu 5 |
| BookedRoom | Phòng đã đặt | Liên kết | M00 | Một phòng trong một lượt đặt phòng | checkin, checkout, price, note, /amount, isCheckedIn | Câu 6 |
| Bill | Hóa đơn | Thực thể | M00 | Kết quả của một lần thanh toán cho một lượt đặt phòng | paymentDate, amount, paymentType, note | Câu 5, Câu 6 |
| Service | Dịch vụ | Thực thể | M00 | Dịch vụ khách sạn cung cấp | name, unity, price | Câu 6 |
| UsedService | Dịch vụ đã dùng | Liên kết | M00 | Một dịch vụ được dùng trong một phòng đã đặt | price, quantity, /totalAmount | Câu 6 |
| HotelStat | Thống kê khách sạn | Thống kê | M00 | Số liệu thống kê theo khách sạn | /revenue, /fillRate | Câu 2 |
| RoomStat | Thống kê phòng | Thống kê | M00 | Số liệu thống kê theo phòng | /fillDay, /fillRate, /revenue | Câu 2 |
| ClientStat | Thống kê khách hàng | Thống kê | M00 | Số liệu thống kê theo khách hàng | /day, /payment | Câu 2 |
| ServiceStat | Thống kê dịch vụ | Thống kê | M00 | Số liệu thống kê theo dịch vụ | /amount, /revenue | Câu 2 |
| IncomeStat | Thống kê doanh thu | Thống kê | M00 | Doanh thu theo kỳ | /period, /client, /revenue | Câu 2 |

### 2.3 Thuộc tính

| Lớp | Thuộc tính | Tên tiếng Việt | Tính chất | Căn cứ | Ràng buộc nguồn nêu | Nguồn | Ghi chú |
|---|---|---|---|---|---|---|---|
| Hotel | name | Tên | Lưu | Đề xuất | — | Câu 2 | Câu 2: người quản lý quản lý thông tin khách sạn; cần tên để phân biệt các khách sạn và hiện trên thống kê khách sạn |
| Hotel | starLevel | Hạng sao | Lưu | Đề xuất | — | Câu 2 | Câu 2: thông tin khách sạn được quản lý; hạng sao là thông tin mô tả khách sạn |
| Hotel | address | Địa chỉ | Lưu | Đề xuất | — | Câu 2 | Câu 2: thông tin khách sạn được quản lý; khách hàng cần biết nơi ở |
| Hotel | description | Mô tả | Lưu | Đề xuất | Không bắt buộc | Câu 2 | Câu 2: thông tin giới thiệu khách sạn |
| Room | name | Tên phòng | Lưu | Đề xuất | — | Câu 2 | Câu 2: quản lý phòng; Câu 6: hóa đơn liệt kê các phòng đã đặt, cần tên để nhận ra phòng |
| Room | type | Loại phòng | Lưu | Đề xuất | — | Câu 2 | Câu 2: quản lý phòng; khách đặt phòng theo loại |
| Room | price | Giá niêm yết | Lưu | Đề xuất | — | Câu 6 | Câu 6: thanh toán cần giá phòng |
| Room | description | Mô tả | Lưu | Đề xuất | Không bắt buộc | Câu 2 | Câu 2: thông tin giới thiệu phòng |
| Client | idCard | Số giấy tờ tùy thân | Lưu | Đề xuất | — | Câu 5 | Câu 5: lễ tân làm thủ tục nhận phòng cho khách tại quầy, cần giấy tờ để nhận diện khách |
| Client | fullName | Họ tên | Lưu | Đề xuất | — | Câu 6 | Câu 6: hóa đơn gồm thông tin về khách hàng |
| Client | address | Địa chỉ | Lưu | Đề xuất | — | Câu 6 | Câu 6: hóa đơn gồm thông tin về khách hàng |
| Client | email | Email | Lưu | Đề xuất | Không bắt buộc | Câu 4 | Câu 4: liên lạc với khách ở xa |
| Client | tel | Số điện thoại | Lưu | Đề xuất | — | Câu 4 | Câu 4: nhân viên bán hàng đặt phòng cho khách ở xa qua điện thoại |
| Client | note | Ghi chú | Lưu | Đề xuất | Không bắt buộc | Câu 1 | Câu 1: thông tin khách hàng được quản lý; ghi chú thêm về khách |
| User | username | Tên đăng nhập | Lưu | Đề xuất | — | Câu 3 | Câu 3: quản trị viên quản lý tài khoản; tài khoản cần tên đăng nhập |
| User | password | Mật khẩu | Lưu | Đề xuất | — | Câu 3 | Câu 3: tài khoản cần mật khẩu để đăng nhập |
| User | fullName | Họ tên | Lưu | Đề xuất | — | Câu 3 | Câu 3: tài khoản của một người cụ thể; hóa đơn ghi người lập |
| User | position | Vị trí | Lưu | Nguồn nêu | Giá trị: người quản lý, quản trị viên, nhân viên bán hàng, lễ tân | Câu 2, Câu 3, Câu 4, Câu 5 | — |
| Booking | bookDay | Ngày đặt | Lưu | Đề xuất | — | Câu 4 | Câu 4, Câu 5: tạo lượt đặt phòng; cần biết lượt đặt được tạo ngày nào |
| Booking | totalAmount | Tổng tiền | Dẫn xuất | Đề xuất | Tính từ các BookedRoom và UsedService của lượt đặt | Câu 6 | Câu 6: thanh toán cần tổng tiền của lượt đặt |
| Booking | note | Ghi chú | Lưu | Đề xuất | Không bắt buộc | Câu 4 | Câu 4: yêu cầu riêng của khách khi đặt qua điện thoại |
| BookedRoom | checkin | Ngày nhận phòng | Lưu | Nguồn nêu | — | Câu 5 | — |
| BookedRoom | checkout | Ngày trả phòng | Lưu | Nguồn nêu | — | Câu 5 | — |
| BookedRoom | price | Giá lúc đặt | Lưu | Đề xuất | Giá tại thời điểm đặt, có thể khác Room.price hiện tại | Câu 6 | Câu 6: hóa đơn tính theo giá đã thỏa thuận khi đặt, không theo giá niêm yết lúc thanh toán |
| BookedRoom | note | Ghi chú | Lưu | Đề xuất | Không bắt buộc | Câu 5 | Câu 5: ghi chú khi làm thủ tục |
| BookedRoom | amount | Thành tiền | Dẫn xuất | Đề xuất | Tính từ price, checkin, checkout | Câu 6 | Câu 6: hóa đơn gồm các phòng đã đặt, mỗi phòng một số tiền |
| BookedRoom | isCheckedIn | Đã nhận phòng | Lưu | Nguồn nêu | — | Câu 5 | — |
| Bill | paymentDate | Ngày thanh toán | Lưu | Đề xuất | — | Câu 6 | Câu 6: mỗi lần thanh toán một hóa đơn; cần ngày để thống kê doanh thu theo kỳ (Câu 2) |
| Bill | amount | Số tiền | Lưu | Đề xuất | — | Câu 6 | Câu 6: số tiền của lần thanh toán |
| Bill | paymentType | Hình thức thanh toán | Lưu | Đề xuất | — | Câu 5 | Câu 5: lễ tân xử lý thanh toán; cần biết trả bằng hình thức nào |
| Bill | note | Ghi chú | Lưu | Đề xuất | Không bắt buộc | Câu 6 | Câu 6: ghi chú trên hóa đơn |
| Service | name | Tên dịch vụ | Lưu | Đề xuất | — | Câu 6 | Câu 6: hóa đơn liệt kê dịch vụ đã dùng |
| Service | unity | Đơn vị tính | Lưu | Đề xuất | — | Câu 6 | Câu 6: dịch vụ được tính theo số lượng, cần đơn vị |
| Service | price | Đơn giá niêm yết | Lưu | Đề xuất | — | Câu 6 | Câu 6: thanh toán cần đơn giá dịch vụ |
| UsedService | price | Đơn giá lúc dùng | Lưu | Đề xuất | Giá tại thời điểm dùng | Câu 6 | Câu 6: hóa đơn tính theo giá lúc dùng |
| UsedService | quantity | Số lượng | Lưu | Đề xuất | — | Câu 6 | Câu 6: khách có thể dùng một dịch vụ nhiều lần |
| UsedService | totalAmount | Thành tiền | Dẫn xuất | Đề xuất | quantity × price | Câu 6 | Câu 6: số tiền của dịch vụ trên hóa đơn |
| HotelStat | revenue | Doanh thu | Dẫn xuất | Đề xuất | — | Câu 2 | Câu 2: thống kê khách sạn |
| HotelStat | fillRate | Tỷ lệ lấp đầy | Dẫn xuất | Đề xuất | — | Câu 2 | Câu 2: thống kê khách sạn |
| RoomStat | fillDay | Số ngày có khách | Dẫn xuất | Đề xuất | — | Câu 2 | Câu 2: thống kê phòng |
| RoomStat | fillRate | Tỷ lệ lấp đầy | Dẫn xuất | Đề xuất | — | Câu 2 | Câu 2: thống kê phòng |
| RoomStat | revenue | Doanh thu | Dẫn xuất | Đề xuất | — | Câu 2 | Câu 2: thống kê phòng |
| ClientStat | day | Số ngày lưu trú | Dẫn xuất | Đề xuất | — | Câu 2 | Câu 2: thống kê khách hàng |
| ClientStat | payment | Tổng thanh toán | Dẫn xuất | Đề xuất | — | Câu 2 | Câu 2: thống kê khách hàng |
| ServiceStat | amount | Số lượng đã bán | Dẫn xuất | Đề xuất | — | Câu 2 | Câu 2: thống kê dịch vụ |
| ServiceStat | revenue | Doanh thu | Dẫn xuất | Đề xuất | — | Câu 2 | Câu 2: thống kê dịch vụ |
| IncomeStat | period | Kỳ thống kê | Dẫn xuất | Đề xuất | — | Câu 2 | Câu 2: thống kê doanh thu theo kỳ |
| IncomeStat | client | Số khách | Dẫn xuất | Đề xuất | — | Câu 2 | Câu 2: thống kê doanh thu |
| IncomeStat | revenue | Doanh thu | Dẫn xuất | Đề xuất | — | Câu 2 | Câu 2: thống kê doanh thu |

### 2.4 Đối chiếu với mục Dữ liệu nghiệp vụ của FR

Ví dụ không có tài liệu FR nên không có gì để đối chiếu.

| Thực thể trong FR | Trong mô hình | Xử lý |
|---|---|---|
| — | — | — |

## 3. Quan hệ giữa các lớp

### 3.1 Ma trận cặp lớp

Ô ghi: `T` = có quan hệ trực tiếp; `G(X)` = chỉ liên hệ gián tiếp qua lớp X; để trống = không liên quan.
Chỉ điền nửa trên. Lớp thống kê xét riêng ở cuối mục 3.2.

| | Room | Client | User | Booking | BookedRoom | Bill | Service | UsedService |
|---|---|---|---|---|---|---|---|---|
| Hotel | T | | | | | | | |
| Room | | G(Booking) | | G(BookedRoom) | T | | | |
| Client | | | | T | | G(Booking) | G(Booking) | |
| User | | | | T | | T | | |
| Booking | | | | | T | T | | |
| BookedRoom | | | | | | | G(UsedService) | T |
| Bill | | | | | | | | |
| Service | | | | | | | | T |

### 3.2 Quan hệ số lượng

| Cặp | Câu A → B | Câu B → A | Dạng | Xử lý |
|---|---|---|---|---|
| Hotel – Room | Một khách sạn có thể có nhiều phòng. | Một phòng chỉ thuộc một khách sạn. | 1-n | Giữ nguyên |
| Client – Room | Một khách hàng có thể đặt nhiều phòng. | Một phòng có thể được nhiều khách hàng đặt ở các thời điểm khác nhau. | n-n | Tách: thêm lớp Booking giữa hai lớp; xét tiếp Client – Booking và Booking – Room |
| Client – Booking | Một khách hàng có thể có nhiều lượt đặt phòng ở các thời điểm khác nhau. | Một lượt đặt phòng thuộc đúng một khách hàng. | 1-n | Giữ nguyên |
| Booking – Room | Một lượt đặt phòng có thể gồm nhiều phòng (khách đoàn). | Một phòng có thể nằm trong nhiều lượt đặt phòng ở các thời điểm khác nhau. | n-n | Tách: thêm lớp liên kết BookedRoom; một Booking và một Room xác định duy nhất một BookedRoom |
| Booking – BookedRoom | Một lượt đặt phòng gồm ít nhất một phòng đã đặt. | Một phòng đã đặt thuộc đúng một lượt đặt phòng. | 1-n | Giữ nguyên |
| Room – BookedRoom | Một phòng có thể ứng với nhiều phòng đã đặt ở các thời điểm khác nhau. | Một phòng đã đặt ứng với đúng một phòng. | 1-n | Giữ nguyên |
| Booking – Bill | Một lượt đặt phòng có thể được thanh toán nhiều lần, mỗi lần một hóa đơn. | Một hóa đơn thuộc đúng một lượt đặt phòng. | 1-n | Giữ nguyên |
| User – Bill | Một người dùng (lễ tân) có thể lập nhiều hóa đơn. | Một hóa đơn do đúng một người dùng lập. | 1-n | Giữ nguyên |
| User – Booking | Một người dùng (nhân viên bán hàng, lễ tân) có thể tạo nhiều lượt đặt phòng. | Một lượt đặt phòng do đúng một người dùng tạo. | 1-n | Giữ nguyên |
| BookedRoom – Service | Một phòng đã đặt có thể dùng nhiều dịch vụ. | Một dịch vụ có thể được dùng ở nhiều phòng đã đặt. | n-n | Tách: thêm lớp liên kết UsedService |
| BookedRoom – UsedService | Một phòng đã đặt có thể có nhiều dịch vụ đã dùng. | Một dịch vụ đã dùng thuộc đúng một phòng đã đặt. | 1-n | Giữ nguyên |
| Service – UsedService | Một dịch vụ có thể ứng với nhiều dịch vụ đã dùng. | Một dịch vụ đã dùng ứng với đúng một dịch vụ. | 1-n | Giữ nguyên |

Lớp thống kê không có quan hệ số lượng: HotelStat, RoomStat, ServiceStat, ClientStat dùng lại thuộc tính của lớp thực
thể tương ứng (kế thừa); IncomeStat không dùng lại thuộc tính của lớp nào, chỉ tính từ Bill (phụ thuộc).

### 3.3 Lớp liên kết

| Lớp liên kết | Tách từ quan hệ n-n | Thuộc tính riêng của liên kết | Nguồn |
|---|---|---|---|
| BookedRoom | Room – Booking | checkin, checkout, price, note, amount, isCheckedIn | Câu 5, Câu 6 |
| UsedService | BookedRoom – Service | price, quantity, totalAmount | Câu 6 |

### 3.4 Quan hệ

| ID | Lớp A | Bội số A | Lớp B | Bội số B | Dạng | Loại | Bên chính | Căn cứ | Nguồn |
|---|---|---|---|---|---|---|---|---|---|
| R-M00-01 | Hotel | 1 | Room | 0..* | 1-n | Hợp thành | Hotel | Phòng không tồn tại ngoài khách sạn, thuộc đúng một khách sạn, bị xóa theo khách sạn | Câu 1 |
| R-M00-02 | Client | 1 | Booking | 0..* | 1-n | Kết tập | Booking | Lượt đặt phòng chứa thông tin khách hàng; khách hàng tồn tại độc lập và dùng cho nhiều lượt đặt | Câu 4, Câu 5 |
| R-M00-03 | Booking | 1 | BookedRoom | 1..* | 1-n | Liên kết | — | Nửa thứ nhất của quan hệ n-n Room – Booking đã tách qua lớp liên kết BookedRoom | Câu 6 |
| R-M00-04 | Room | 1 | BookedRoom | 0..* | 1-n | Liên kết | — | Nửa thứ hai của quan hệ n-n Room – Booking đã tách qua lớp liên kết BookedRoom | Câu 6 |
| R-M00-05 | Booking | 1 | Bill | 0..* | 1-n | Kết tập | Bill | Hóa đơn chứa thông tin lượt đặt phòng; lượt đặt phòng tồn tại trước và độc lập với hóa đơn | Câu 6 |
| R-M00-06 | User | 1 | Bill | 0..* | 1-n | Kết tập | Bill | Hóa đơn ghi người lập; người dùng tồn tại độc lập | Câu 5 |
| R-M00-07 | User | 1 | Booking | 0..* | 1-n | Kết tập | Booking | Lượt đặt phòng ghi người tạo; người dùng tồn tại độc lập | Câu 4, Câu 5 |
| R-M00-08 | BookedRoom | 1 | UsedService | 0..* | 1-n | Liên kết | — | Nửa thứ nhất của quan hệ n-n BookedRoom – Service đã tách qua lớp liên kết UsedService | Câu 6 |
| R-M00-09 | Service | 1 | UsedService | 0..* | 1-n | Liên kết | — | Nửa thứ hai của quan hệ n-n BookedRoom – Service đã tách qua lớp liên kết UsedService | Câu 6 |
| R-M00-10 | Hotel | — | HotelStat | — | — | Kế thừa | Hotel | HotelStat dùng lại mọi thuộc tính của Hotel và thêm số liệu thống kê | Câu 2 |
| R-M00-11 | Room | — | RoomStat | — | — | Kế thừa | Room | RoomStat dùng lại mọi thuộc tính của Room và thêm số liệu thống kê | Câu 2 |
| R-M00-12 | Service | — | ServiceStat | — | — | Kế thừa | Service | ServiceStat dùng lại mọi thuộc tính của Service và thêm số liệu thống kê | Câu 2 |
| R-M00-13 | Client | — | ClientStat | — | — | Kế thừa | Client | ClientStat dùng lại mọi thuộc tính của Client và thêm số liệu thống kê | Câu 2 |
| R-M00-14 | IncomeStat | — | Bill | — | — | Phụ thuộc | Bill | IncomeStat không dùng lại thuộc tính của lớp nào; số liệu của nó chỉ tính từ Bill | Câu 2 |

## 4. Sơ đồ lớp phân tích

<!-- BEGIN:DIAGRAM -->
![Sơ đồ lớp phân tích — EC-M00](diagrams/EC-M00.png)

Mã nguồn sơ đồ: [diagrams/EC-M00.puml](diagrams/EC-M00.puml). Ảnh và tệp .puml do `gen_puml.py` sinh từ các bảng của tài liệu này; muốn đổi sơ đồ thì sửa bảng rồi chạy lại tool, không sửa tay.
<!-- END:DIAGRAM -->

## 5. Liên module

Ví dụ chỉ có một module nên không có lớp của module khác.

| Lớp | Module sở hữu | Module này dùng thế nào | Thuộc tính module này bổ sung |
|---|---|---|---|
| — | — | — | — |

## 6. Câu hỏi và điểm chưa chốt

| Mã | Loại | Câu hỏi | Trả lời | Ghi vào |
|---|---|---|---|---|
| Q-01 | Thiếu | Sơ đồ phân tích gốc của case study không vẽ quan hệ User – Booking, nhưng đoạn mô tả nói nhân viên bán hàng và lễ tân tạo lượt đặt phòng, và bước thiết kế của case study có "Booking has an User". Có ghi quan hệ này ở bước phân tích không? | Có: thêm R-M00-07. | EC-M00 mục 3.4 |

## 7. Lịch sử sửa đổi

| Phiên bản | Ngày | Nội dung | Người sửa |
|---|---|---|---|
| 1.0 | 2026-11-15 | Dựng từ case study quản lý khách sạn | (ví dụ) |
