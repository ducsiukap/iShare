# Skill: designing-database

Skill này giúp agent **thiết kế cơ sở dữ liệu** cho từng module của iShare từ bản thiết kế lớp thực thể đã chốt
(`CD-Mxx.md`), theo năm bước của phương pháp: mỗi lớp một bảng → thuộc tính không phải đối tượng thành cột → quan hệ
số lượng giữa các bảng → khóa chính và khóa ngoại → loại thuộc tính dư thừa. Đầu ra là `DB-Mxx.md` cho mỗi module và
`DB-SYS.md` cho toàn hệ thống.

Đây là skill thứ ba trong bộ ba skill mô hình dữ liệu. Tổng quan cả bộ và quy ước chung: xem
[README của analyzing-entity-classes](../analyzing-entity-classes/README.md) và
[`CONVENTIONS.md`](../analyzing-entity-classes/input/CONVENTIONS.md).

## Nguyên tắc

- **Đầu vào duy nhất là `CD-Mxx.md` đã chốt.** Bảng chỉ sinh từ lớp, cột chỉ sinh từ thuộc tính, khóa ngoại chỉ sinh
  từ quan hệ. Không thêm cột lớp không có.
- **Đúng thứ tự năm bước, kể cả với thứ sẽ bị loại.** Lớp thống kê và thuộc tính dẫn xuất vẫn thành bảng, thành cột
  rồi mới bị loại ở bước 5, có ghi lý do và cách có lại giá trị.
- **Gặp quan hệ n-n thì quay lại bước phân tích**, không tạo bảng trung gian ở đây.
- **Thuộc tính dẫn xuất mà FR yêu cầu lưu** do bạn quyết giữ hay loại; agent chỉ đề xuất.
- **Dừng ở lược đồ logic**: bảng, cột, kiểu, null, duy nhất, khóa chính, khóa ngoại. Không DDL, chỉ mục, di trú.
- **Mỗi bước dừng chờ bạn xác nhận.**

## Làm một module

```
Dùng skill designing-database cho module M05.
Làm bước 1 rồi dừng ở cổng xác nhận.
```

Quy ước đặt tên của cơ sở dữ liệu (bạn đã chốt snake_case cho cả bảng và cột, tên bảng số nhiều):

| Mã | Về việc gì | Giá trị | Trạng thái |
|---|---|---|---|
| QU-06 | Tên bảng | snake_case của tên lớp: `PostTopic` → `post_topics` | Đã chốt: snake_case, số nhiều |
| QU-07 | Tên cột | snake_case của tên thuộc tính: `starLevel` → `star_level` | Đã chốt |
| QU-08 | Tên khóa ngoại | snake_case, kết thúc bằng `_id`: `client_id`, `author_id` | Cách ghép tên hỏi ở cổng bước 1 của module đầu tiên |
| QU-09 | Kiểu cột | Ánh xạ sang kiểu PostgreSQL | Hỏi ở cổng bước 1 của module đầu tiên |

Phương pháp gốc đặt bảng là `tbl` + tên lớp; ở dự án này quy ước snake_case thay cho cách đó. Thứ tự năm bước không đổi.

Kết quả được ghi vào `.agents/.claude/system_analysis/output/data-model/conventions.md`.

Năm bước và việc của bạn ở từng cổng:

| Bước | Agent làm | Bạn kiểm ở cổng |
|---|---|---|
| 1. Bảng | Mỗi lớp của module một bảng; lớp của module khác ghi là bảng ngoài | Tên bảng; bảng ngoài |
| 2. Cột | Thuộc tính thường thành cột, có kiểu, null, duy nhất; thuộc tính đối tượng không chuyển | Kiểu cột; cột nào là `text` vì nguồn không nêu độ dài |
| 3. Quan hệ giữa các bảng | Mỗi quan hệ của CD thành quan hệ bảng; 1-n tách riêng; 1-1 đề xuất gộp hay tách; kế thừa thành cha–con | **Mọi quan hệ 1-1: gộp hay tách** |
| 4. Khóa | Khóa chính; khóa ngoại ở bảng phía n; khóa ngoại liên module | Vị trí khóa ngoại; khóa ngoại cho phép null; khóa ngoại đề nghị cho bảng của module khác |
| 5. Loại dư thừa | Loại cột dẫn xuất và trùng lặp, kèm cách có lại giá trị; loại bảng chỉ còn một khóa ngoại; dựng lược đồ cuối và sơ đồ | **Cột dẫn xuất mà FR yêu cầu lưu: giữ hay loại**; lược đồ cuối; nói `Chốt DB-M05` khi đồng ý |

Cách trả lời ở cổng, cách tiếp tục ở phiên mới và cách sửa sau khi chốt giống skill `analyzing-entity-classes`
(thay `EC` bằng `DB`).

## Gộp toàn hệ thống

Khi mọi module đã chốt `DB-Mxx.md`:

```
Dùng skill designing-database, chạy lượt gộp hệ thống (steps/90-system-merge.md).
Làm việc A rồi dừng ở cổng.
```

Lượt gộp này tìm thêm dữ liệu dư thừa **xuyên module** (cột trùng lặp ở hai module, cột dẫn xuất tính từ bảng của
module khác), kiểm mọi khóa ngoại liên module, và dựng `DB-SYS.md`.

## Đầu vào và đầu ra

| | Đường dẫn |
|---|---|
| Đầu vào | `.agents/.claude/system_analysis/output/data-model/cd/CD-Mxx.md` (Đã chốt) |
| Đầu ra của module | `.agents/.claude/system_analysis/output/data-model/db/DB-Mxx.md` |
| Bản gộp | `.agents/.claude/system_analysis/output/data-model/db/DB-SYS.md` |
| Tệp tạm của tool | `.agents/.claude/system_analysis/output/data-model/db/.work/` |

## Cấu trúc tệp DB

1. Bảng
2. Cột: cột từ thuộc tính; thuộc tính đối tượng không chuyển
3. Quan hệ giữa các bảng
4. Khóa: khóa chính; khóa ngoại
5. Loại dư thừa: cột bị loại; bảng bị loại; dẫn xuất nhưng giữ lại; đã xét nhưng không coi là dư thừa
6. Lược đồ cuối: bảng và cột; sơ đồ quan hệ (do tool sinh)
7. Liên module: bảng ngoài; khóa ngoại đề nghị
8. Quyết định thiết kế (`DD-Mxx-nn`)
9. Câu hỏi và điểm chưa chốt
10. Lịch sử sửa đổi

Mẫu: `output/db-template.md`. Ví dụ đầy đủ (case study quản lý khách sạn, ra đúng 9 bảng): `output/example.md`.

## Cấu trúc skill

```
designing-database/
├── SKILL.md
├── README.md
├── input/INPUTS.md
├── steps/            01-tables, 02-columns, 03-table-relationships, 04-keys, 05-remove-redundancy, 90-system-merge
├── output/           db-template.md, db-system-template.md, example.md
└── tools/            check_db.py, build_schema.py, merge_db.py, mdtab.py
```

## Tool

```bash
SK=.agent-instructions/skills/designing-database
M=.agents/.claude/system_analysis/output/data-model

# Bảng các module khác đã có, khóa chính và kiểu
python3 $SK/tools/merge_db.py --dir $M/db --list --exclude M05

# Kiểm tới bước N, hoặc kiểm đầy đủ; luôn kèm --cd để đối chiếu với bản thiết kế lớp
python3 $SK/tools/check_db.py --db $M/db/DB-M05.md --step 4 --cd $M/cd/CD-M05.md
python3 $SK/tools/check_db.py --db $M/db/DB-M05.md --final  --cd $M/cd/CD-M05.md

# Dựng lược đồ cuối (mục 6.1) và sơ đồ quan hệ (mục 6.2) từ các bảng bước 1–5
python3 $SK/tools/build_schema.py --db $M/db/DB-M05.md --inplace

# Lượt gộp hệ thống
python3 $SK/tools/merge_db.py --dir $M/db --out-md $M/db/.work/merge-db.md
python3 $SK/tools/check_db.py --db $M/db/DB-SYS.md --system --final --cd $M/cd/CD-SYS.md
```

`check_db.py` mặc định kiểm tên theo snake_case. Đổi quy ước thì dùng `--table-style tbl` (kiểu phương pháp gốc) hoặc
`--table-style none` (không kiểm tên).

Thử nhanh trên ví dụ:
`python3 $SK/tools/check_db.py --db $SK/output/example.md --final --cd .agent-instructions/skills/designing-entity-classes/output/example.md`.

## Câu hỏi thường gặp

**Vì sao tạo bảng cho lớp thống kê rồi lại loại?** Để đi đúng năm bước của phương pháp và để mọi thứ bị loại có dấu
vết: cột nào bị loại, vì sao, và tính lại bằng cách nào. Phần "Cách có lại giá trị" chính là đầu vào cho các truy vấn
thống kê lúc cài đặt.

**"Dẫn xuất nhưng giữ lại" là gì?** Theo phương pháp, thuộc tính tính lại được thì bị loại. Nhưng một số yêu cầu của
FR đòi kết quả được **lưu** (ví dụ số liệu tính lại định kỳ và hiển thị từ bản đã lưu). Agent không tự quyết: nó nêu
từng cột kèm mã FR, bạn chọn giữ hay loại, và quyết định được ghi lại.

**Giá lúc đặt và giá niêm yết có trùng lặp không?** Không. Giá trị chụp tại một thời điểm không tính lại được khi dữ
liệu gốc đổi, nên không phải dư thừa. Các cặp đã xét như vậy được ghi ở mục 5.4.

**Skill có sinh câu lệnh `CREATE TABLE` không?** Không. Phương pháp dừng ở lược đồ logic. Nếu bạn cần DDL
PostgreSQL từ `DB-SYS.md`, yêu cầu riêng sau khi đã chốt.

**Khác gì với skill `technical-design` (Task 2: Database Schema)?** `technical-design` mô tả việc thiết kế CSDL ở mức
chung (ER, DDL, chỉ mục, hiệu năng). Bộ ba skill này làm phần mô hình dữ liệu theo đúng phương pháp của đồ án, từng
module, có cổng. Chỉ mục, DDL và hiệu năng nếu cần vẫn thuộc `technical-design`, làm sau khi `DB-SYS.md` đã chốt.
