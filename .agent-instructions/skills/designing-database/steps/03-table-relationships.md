# Bước 3 — Quan hệ số lượng giữa các bảng

Ứng với Step 3 của phương pháp: "Consider the quantity relationships among entity classes. These relationships will
be those among corresponding tables: 1-1 → the two related tables should be regrouped into one (in some particular
situation they could be kept separated); 1-n → separated; n-n → create intermediate tables… (it should back to
analyze phase to correct this relationship)."

## Mục đích

Mỗi quan hệ giữa hai lớp trở thành một quan hệ giữa hai bảng, có dạng và cách xử lý rõ ràng. Bước 4 dựa vào bảng
này để đặt khóa ngoại.

## Đầu vào

Mục 3.1 và 3.2 của `CD-Mxx.md`; mục 1 và 7.1 của `DB-Mxx.md`.

## Việc làm

1. Với **mỗi** dòng ở mục 3.1 của CD, thêm một dòng vào mục 3 của DB, **giữ đúng mã `R-Mxx-nn`**. Đổi từ "thành
   phần–toàn thể" sang "Bảng A–Bảng B", viết bảng phía 1 trước:

   | Dạng ở CD (thành phần–toàn thể) | Bảng A (phía 1) | Bảng B | Dạng ở DB |
   |---|---|---|---|
   | `n-1` | bảng của lớp toàn thể | bảng của lớp thành phần | `1-n` |
   | `1-n` | bảng của lớp thành phần | bảng của lớp toàn thể | `1-n` |
   | `1-1` | bảng của lớp toàn thể | bảng của lớp thành phần | `1-1` |

   Bảng của lớp ngoài dùng tên ở mục 7.1.
2. Điền cột **Xử lý**:

   | Dạng | Xử lý | Điều kiện |
   |---|---|---|
   | `1-n` | `Tách riêng` | Luôn luôn |
   | `1-1` | `Gộp` | Mặc định của phương pháp: hai bảng gộp thành một. Chỉ gộp khi cả hai bảng thuộc module này |
   | `1-1` | `Tách riêng` | Khi có lý do: một bên là tùy chọn (bội số `0..1`), hai bên có vòng đời khác nhau, một bên thuộc module khác, hoặc một bên chỉ được dùng trong một số trường hợp. Ghi lý do ở cột Ghi chú |
   | n-n | Dừng | Không được xuất hiện: `CD` chỉ có quan hệ đã tách. Nếu gặp, dừng bước này, báo người dùng và quay lại skill `analyzing-entity-classes` |

   Quan hệ 1-1 **luôn** phải có nội dung ở cột Ghi chú (vì sao gộp, hoặc vì sao tách). Khi `Gộp`: ghi rõ bảng nào
   được giữ; các cột của bảng kia sẽ chuyển sang bảng được giữ ở bước 5 (ghi ở mục 5.2 bảng bị loại do gộp, và sửa
   cột Bảng của các dòng liên quan ở mục 2.1, có ghi chú "chuyển từ <bảng> do gộp R-…").
3. Với mỗi dòng **Kế thừa** ở mục 3.2 của CD: thêm một dòng, Bảng A = bảng cha, Bảng B = bảng con, Dạng `1-1`,
   Xử lý `Cha–con`, Ghi chú nêu bảng con không có id riêng và dùng khóa của bảng cha. (Theo case study của phương
   pháp: các bảng con không có khóa chính `id` riêng.)
4. Dòng **Phụ thuộc** ở mục 3.2 của CD **không** sinh quan hệ giữa các bảng. Ghi một câu dưới bảng: quan hệ nào
   không sinh quan hệ bảng và vì sao.
5. Chạy `check_db.py --db … --step 3 --cd …`.

## Ghi vào tệp DB

Mục 3.

## Tự kiểm trước cổng

- Mỗi mã quan hệ ở mục 3.1 của CD và mỗi dòng Kế thừa ở mục 3.2 có đúng một dòng ở mục 3 của DB.
- Với mỗi dòng `1-n`: đọc "một <Bảng A> ứng với nhiều <Bảng B>" và so với bội số ở CD.
- Không dòng `Gộp` nào có bảng của module khác.

## Trình ở cổng

- Bảng quan hệ giữa các bảng.
- Nêu riêng mọi quan hệ 1-1 và đề xuất gộp hay tách kèm lý do (đây là quyết định của người dùng; ghi `DD-Mxx-nn` khi
  được duyệt).
- Quan hệ cha–con; quan hệ phụ thuộc không sinh quan hệ bảng.

## Không làm

Chưa đặt khóa. Không tạo bảng trung gian mới.
