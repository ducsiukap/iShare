# Bước 1 — Mỗi lớp thực thể một bảng

Ứng với Step 1 của phương pháp: "For each entity class, create a corresponding table. The table name should have the
prefix 'tbl' + the name of the entity class."

Ở iShare, tên bảng theo QU-06 đã được người dùng chốt là **snake_case, số nhiều** (`PostTopic` → `post_topics`), không
dùng tiền tố `tbl`.

## Mục đích

Có danh sách bảng ban đầu, một-một với các lớp của module.

## Đầu vào

Mục 1 và mục 6 của `CD-Mxx.md` đã chốt; `data-model/conventions.md` (QU-06).

## Việc làm

1. Nếu đây là module đầu tiên làm skill này: trình các phần còn "Chờ xác nhận" của QU-08 (cách ghép tên khóa
   ngoại) và QU-09 (kiểu cột) ở cổng bước này, để người dùng xác nhận một lần cho mọi module. Ghi kết quả vào
   `data-model/conventions.md` sau khi được duyệt. Phần đã chốt (snake_case cho bảng và cột, tên bảng số nhiều) không hỏi lại.
2. Với **mỗi lớp của module này** ở mục 1 của CD (Sở hữu = module đang làm), thêm một dòng vào mục 1 của DB: tên
   bảng theo QU-06 (`PostTopic` → `post_topics`), cột "Từ lớp" là tên lớp viết đúng như CD, Nhóm và Sở hữu giữ nguyên.
   Khi register đã gọi tên bảng của đúng thực thể đó (ví dụ `post_topics`, `post_tags`), dùng lại tên ấy.
   - **Kể cả** lớp liên kết, lớp thống kê và lớp con. Chúng được xử lý ở các bước sau (lớp con ở bước 3–4; lớp
     thống kê ở bước 5). Không loại sớm.
3. Với **mỗi lớp ngoài** (Sở hữu là module khác): không tạo bảng. Thêm một dòng vào mục 7.1 "Bảng của module khác
   được tham chiếu": tên bảng theo QU-06 (hoặc tên đã có trong `DB-Myy.md` nếu module đó đã làm, xem
   `merge_db.py --list`), module sở hữu, module này dùng thế nào.
4. Chạy `check_db.py --db … --step 1 --cd …`.

## Ghi vào tệp DB

Frontmatter (`nguon`), mục 1, mục 7.1.

## Tự kiểm trước cổng

- Số bảng ở mục 1 bằng số lớp của module ở CD.
- Số dòng mục 7.1 bằng số lớp ngoài ở CD.
- Tên bảng đúng quy ước đã xác nhận.

## Trình ở cổng

- Bảng lớp → bảng.
- Bảng ngoài và module sở hữu; bảng nào chưa có `DB-Myy.md` để đối chiếu tên.
- Nếu là module đầu tiên: các phần còn chờ xác nhận của QU-08, QU-09.

## Không làm

Chưa có cột, chưa có khóa. Không bỏ bảng của lớp thống kê.
