# Bước 4 — Khóa chính và khóa ngoại

Ứng với Step 4 của phương pháp: "Khóa chính: bảng nào có thuộc tính id thì thiết lập thuộc tính đó làm khóa chính.
Khóa ngoại: nếu hai bảng tblA và tblB có quan hệ 1-n (1 tblA có n tblB) thì trong bảng tblB phải có khóa ngoại tham
chiếu đến khóa chính của bảng tblA."

## Mục đích

Mỗi bảng có khóa chính; mỗi quan hệ giữa hai bảng được thể hiện bằng đúng một khóa ngoại ở đúng bảng.

## Đầu vào

Mục 1, 2.1, 3, 7.1 của `DB-Mxx.md`; mục 3.1 của `CD-Mxx.md` (bội số); `data-model/conventions.md` (QU-08);
`merge_db.py --list` (khóa chính và kiểu của bảng ngoài).

## Việc làm

### 4.1 Khóa chính

Mỗi bảng ở mục 1 một dòng ở mục 4.1:

| Bảng | Khóa chính |
|---|---|
| Có cột `id` | `id` |
| Bảng con (quan hệ `Cha–con` ở mục 3) | Chính là khóa ngoại tới bảng cha (ghi tên cột khóa ngoại đó) |
| Bảng của lớp thống kê không có id và không có lớp cha | Ghi `Không có`, Ghi chú: bảng sẽ bị loại ở bước 5 |

Một bảng **còn lại** sau bước 5 mà không có khóa chính là lỗi (tool kiểm ở bước 5).

### 4.2 Khóa ngoại

Với mỗi dòng ở mục 3 có Xử lý `Tách riêng` hoặc `Cha–con`, thêm một dòng vào mục 4.2:

| Dạng (Bảng A–Bảng B) | Khóa ngoại nằm ở | Tham chiếu |
|---|---|---|
| `1-n` | Bảng B (phía n) | Khóa chính của Bảng A |
| `1-1`, Tách riêng | Một trong hai bảng: bảng của bên tùy chọn, hoặc bảng được tạo sau; cột Duy nhất = `Có` | Khóa chính của bảng kia |
| `1-1`, Cha–con | Bảng con; khóa ngoại này cũng là khóa chính của bảng con; Duy nhất = `Có` | Khóa chính của bảng cha |

Điền các cột:

- **Cột**: tên theo QU-08, viết snake_case và kết thúc bằng `_id`. Mặc định: tên thuộc tính đối tượng tương ứng ở
  CD + `_id` (`client` → `client_id`, `author` → `author_id`). Khi thuộc tính đối tượng là danh sách nằm ở phía 1
  (`Hotel.rooms`), dùng tên lớp phía 1 + `_id` (`hotel_id`). Hai khóa ngoại của một bảng cùng trỏ tới một bảng thì
  phân biệt bằng vai trò (`author_id`, `locked_by_id`).
- **Kiểu**: **đúng bằng** kiểu của khóa chính được tham chiếu. Bảng ngoài: lấy kiểu từ `DB-Myy.md` nếu đã có
  (`merge_db.py --list`); chưa có thì dùng kiểu cột của id theo QU-02/QU-09 và ghi chú "chờ đối chiếu DB-Myy".
- **Null**: theo cận dưới của bội số **phía 1** ở CD. Cận dưới `0` (ví dụ `0..1`) → `Có`; cận dưới `1` → `Không`.
- **Duy nhất**: `Không` với 1-n; `Có` với 1-1.
- **Tham chiếu**: viết dạng `tên_bảng(cột)`, ví dụ `posts(id)`.
- **Từ quan hệ**: mã `R-Mxx-nn`.

Sau đó quay lại mục 2.2 và điền tên khóa ngoại thay cho từng thuộc tính đối tượng.

### 4.3 Khóa ngoại liên module

- Khóa ngoại nằm ở **bảng của module này** và trỏ tới bảng ngoài: ghi bình thường ở mục 4.2; bảng ngoài phải có ở
  mục 7.1.
- Khóa ngoại phải nằm ở **bảng ngoài** (bảng ngoài là phía n của quan hệ): không ghi ở mục 4.2. Ghi thành **đề
  nghị** ở mục 7.2 (bảng của module khác, tên cột, kiểu, tham chiếu, mã quan hệ). Không sửa `DB-Myy.md`; lượt gộp hệ
  thống sẽ đưa cột đó vào bảng.

### 4.4 Quan hệ của một bảng với chính nó

Khóa ngoại nằm trong chính bảng đó, tham chiếu khóa chính của nó; tên cột theo vai trò (`parent_comment_id`); Null
thường là `Có` (đối tượng gốc không có cha).

Chạy `check_db.py --db … --step 4 --cd …`.

## Ghi vào tệp DB

Mục 4.1, 4.2, 7.2; cập nhật mục 2.2.

## Tự kiểm trước cổng

- Mỗi dòng `Tách riêng` và `Cha–con` ở mục 3 có đúng một khóa ngoại (ở 4.2 hoặc đề nghị ở 7.2).
- Với mỗi khóa ngoại: đọc "nhiều <bảng có khóa ngoại> ứng với một <bảng được tham chiếu>" và so với mục 3.
- Kiểu khóa ngoại bằng kiểu khóa chính được tham chiếu.
- Không có cột khóa ngoại nào được tạo ở bước 2 (bước 2 chỉ có cột từ thuộc tính thường).
- Mỗi thuộc tính đối tượng ở mục 2.2 dẫn tới đúng một khóa ngoại.

## Trình ở cổng

- Bảng khóa chính; bảng khóa ngoại kèm câu đọc.
- Khóa ngoại cho phép null và căn cứ bội số.
- Khóa ngoại trỏ tới bảng ngoài; khóa ngoại đề nghị cho bảng của module khác.
- Khóa ngoại đặt tên theo vai trò.

## Không làm

Không thêm chỉ mục, ràng buộc kiểm tra, hành vi khi xóa (cascade): ngoài phạm vi năm bước. Nếu FR có quy định xóa
theo, ghi một dòng ở cột Ghi chú của khóa ngoại, dẫn mã FR, không thiết kế thêm.
