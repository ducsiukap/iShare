# Bước 2 — Thuộc tính không phải đối tượng thành cột

Ứng với Step 2 của phương pháp: "For each entity class, transfer all NON-OBJECT attributes to contribute as the
columns of the corresponding table." Ví dụ của phương pháp: lớp Hotel có `listRoom : Room[]` là thuộc tính đối tượng
nên bị bỏ; các thuộc tính còn lại (id, name, starLevel, address, description) thành cột của `tblHotel`.

## Mục đích

Mỗi bảng có các cột ứng với thuộc tính thường của lớp, kèm kiểu cột, tính null và tính duy nhất.

## Đầu vào

Mục 2.1, 2.2 và 4 của `CD-Mxx.md`; mục 1 của `DB-Mxx.md` sau bước 1; `data-model/conventions.md` (QU-07, QU-09).

## Việc làm

1. Với **mỗi** dòng ở mục 2.1 của CD thuộc lớp của module này, thêm một dòng vào mục 2.1 của DB:

   | Cột của DB | Lấy từ |
   |---|---|
   | Bảng | Bảng của lớp đó (mục 1) |
   | Cột | Tên theo QU-07: snake_case của tên thuộc tính (`starLevel` → `star_level`, `isCheckedIn` → `is_checked_in`) |
   | Kiểu | Đổi từ kiểu của thuộc tính theo QU-09 (bảng dưới) |
   | Null | `Không` nếu thuộc tính Bắt buộc = Có; `Có` nếu Bắt buộc = Không |
   | Duy nhất | `Có` nếu cột Ràng buộc của CD ghi duy nhất (và với `id`); còn lại `Không` |
   | Từ thuộc tính | `Lớp.thuộcTính`, viết đúng như CD (tool dùng cột này để đối chiếu) |
   | Ghi chú | Ràng buộc khác chép từ CD: tập ký tự, khoảng giá trị, mặc định; với kiểu liệt kê: các giá trị cho phép |

   Kiểu cột theo QU-09 (mặc định; giá trị đã xác nhận trong `data-model/conventions.md` thắng):

   | Kiểu thuộc tính | Kiểu cột | Ghi chú |
   |---|---|---|
   | `String`, nguồn nêu độ dài tối đa **bằng ký tự** | `varchar(n)` | n đúng bằng con số của nguồn |
   | `String`, nguồn không nêu độ dài, hoặc nêu bằng đơn vị khác (từ) | `text` | Không tự đặt n |
   | `int` | `integer` | |
   | `long` | `bigint` | |
   | `double` | `double precision` | |
   | `boolean` | `boolean` | |
   | `LocalDate` | `date` | |
   | `Instant` | `timestamptz` | |
   | Kiểu liệt kê | `varchar(30)` | Cột Ghi chú liệt kê giá trị cho phép, chép từ mục 2.2 của CD |

2. **Kể cả** thuộc tính Dẫn xuất và thuộc tính của lớp thống kê: vẫn thành cột ở bước này. Bước 5 mới loại.
3. **Thuộc tính đối tượng** (mọi dòng ở mục 4 của CD mà lớp chứa là lớp của module này) **không** thành cột. Ghi
   từng thuộc tính vào mục 2.2 của DB "Thuộc tính đối tượng không chuyển", cột lý do ghi nó sẽ được thay bằng khóa
   ngoại nào ở bước 4 (ghi tên bảng; tên cột khóa ngoại có thể điền sau bước 4).
4. Lớp con (có lớp cha): chỉ chuyển thuộc tính **riêng** của lớp con. Thuộc tính thừa kế nằm ở bảng cha.
5. Chạy `check_db.py --db … --step 2 --cd …`.

## Ghi vào tệp DB

Mục 2.1, 2.2.

## Tự kiểm trước cổng

- Số dòng mục 2.1 của DB bằng số dòng mục 2.1 của CD thuộc lớp của module.
- Không cột nào có kiểu là tên lớp hoặc danh sách.
- Mỗi `varchar(n)`: n dẫn được về một con số ở cột Ràng buộc của CD.
- Mỗi thuộc tính đối tượng của module có dòng ở mục 2.2.

## Trình ở cổng

- Bảng cột theo từng bảng.
- Cột nào dùng `text` vì nguồn không nêu độ dài (để người dùng biết, không phải để đặt thêm giới hạn).
- Thuộc tính đối tượng không chuyển.

## Không làm

Chưa thêm khóa ngoại (bước 4). Chưa loại cột dẫn xuất (bước 5). Không thêm cột lớp không có.
