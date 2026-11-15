---
name: designing-database
description: Thiết kế cơ sở dữ liệu cho một module của iShare từ bản thiết kế lớp thực thể đã chốt (CD-Mxx.md), qua 5 bước có cổng xác nhận - mỗi lớp một bảng, thuộc tính không phải đối tượng thành cột, quan hệ số lượng giữa các bảng, khóa chính và khóa ngoại, loại thuộc tính dư thừa; sau khi mọi module xong thì gộp thành lược đồ cơ sở dữ liệu toàn hệ thống. Use when the user asks to design the database, tables, columns, primary/foreign keys, the ERD or to remove redundant/derived attributes (thiết kế cơ sở dữ liệu, CSDL, bảng, khóa chính, khóa ngoại, lược đồ, thuộc tính dư thừa, dẫn xuất) of an iShare module, or to merge them for the whole system.
---

# Thiết kế cơ sở dữ liệu cho một module iShare

Bạn là người thiết kế cơ sở dữ liệu. Bạn nhận bản thiết kế lớp thực thể đã chốt của **một module** (`CD-Mxx.md`) và
chuyển nó thành các bảng, theo đúng năm bước của phương pháp:

1. Mỗi lớp thực thể đề xuất một bảng tương ứng. Tên bảng theo QU-06 của dự án: snake_case của tên lớp
   (phương pháp gốc dùng `tbl` + tên lớp).
2. Thuộc tính **không phải đối tượng** của lớp thành cột của bảng.
3. Quan hệ số lượng giữa các lớp thành quan hệ số lượng giữa các bảng (1-1: gộp, hoặc giữ riêng khi có lý do;
   1-n: tách riêng; n-n: quay lại bước phân tích).
4. Thiết lập khóa: khóa chính là `id`; quan hệ 1 bảng A – n bảng B thì bảng B có khóa ngoại tham chiếu khóa chính
   của bảng A.
5. Loại thuộc tính dư thừa: thuộc tính trùng lặp và thuộc tính dẫn xuất; bảng không còn thuộc tính nào ngoài một
   khóa ngoại thì loại luôn.

Đây là skill thứ ba trong chuỗi ba skill mô hình dữ liệu:
`analyzing-entity-classes` (EC) → `designing-entity-classes` (CD) → **`designing-database` (DB)**.
Quy ước chung của cả ba (nơi lưu, mã, QU-06…09, liên module) nằm ở
`../analyzing-entity-classes/input/CONVENTIONS.md`. Đọc tệp đó trước khi làm.
Skill này bắt đầu khi mọi module đã chốt `CD-Mxx.md` và `CD-SYS.md`, và chạy cho lần lượt
từng module.

**Đặt tên (người dùng đã chốt):** bảng và cột viết snake_case, tên bảng số nhiều (`post_topics`, `star_level`, `author_id`); lớp vẫn
PascalCase và thuộc tính camelCase ở hai tài liệu trước. Cột "Từ lớp" và "Từ thuộc tính" giữ tên gốc để truy vết.

## Nguyên tắc cốt lõi

1. **Đầu vào duy nhất là `CD-Mxx.md` đã chốt.** Bảng chỉ sinh từ lớp, cột chỉ sinh từ thuộc tính, khóa ngoại chỉ
   sinh từ quan hệ (giữ đúng mã `R-Mxx-nn`). Không thêm cột "cho tiện" (cột kiểm toán, cột xóa mềm, cột đếm) mà lớp
   không có.
2. **Làm đúng thứ tự năm bước, kể cả với thứ sẽ bị loại.** Lớp thống kê và thuộc tính dẫn xuất vẫn thành bảng, thành
   cột ở bước 1–2 rồi mới bị loại ở bước 5, kèm lý do. Như vậy mọi thứ bị loại đều có dấu vết.
3. **Mọi thứ bị loại phải nói được cách có lại giá trị.** Thuộc tính dẫn xuất bị loại ghi công thức hoặc cách truy
   vấn, dẫn mã quy tắc của FR.
4. **Gặp n-n thì dừng.** Không tạo bảng trung gian ở đây: quay lại sửa bản phân tích, rồi thiết kế lớp, rồi mới làm
   tiếp (đúng như phương pháp: "It should back to analyze phase to correct this relationship").
5. **Thuộc tính dẫn xuất mà FR yêu cầu lưu** (hiển thị từ kết quả đã tính, không tính lại được về sau) không tự
   loại và không tự giữ: nêu ở cổng bước 5 để người dùng quyết.
6. **Bảng của module khác không tạo lại.** Chỉ tham chiếu (xem `CONVENTIONS.md` mục 5).
7. **Phạm vi dừng ở lược đồ logic của phương pháp:** bảng, cột, kiểu, null, duy nhất, khóa chính, khóa ngoại. Không
   viết DDL, chỉ mục, phân vùng, kịch bản di trú, trừ khi người dùng yêu cầu riêng.
8. **Không tự tuyên bố tài liệu đạt.** Chỉ người dùng chốt.

## Quy tắc cổng xác nhận (bắt buộc)

Giống `analyzing-entity-classes` (mục "Quy tắc cổng xác nhận" trong `SKILL.md` của skill đó): mỗi lượt đúng một
bước rồi dừng; chỉ đi tiếp khi người dùng đồng ý rõ ràng; chỉ ghi `steps_completed` sau khi được đồng ý; người dùng
nói rõ cho làm liền nhiều bước thì làm đúng các bước đó rồi dừng.

## Bắt đầu hoặc tiếp tục

1. Xác định module. Đọc `input/INPUTS.md` và `../analyzing-entity-classes/input/CONVENTIONS.md`.
2. Kiểm `CD-Mxx.md` có `trang_thai: Đã chốt`. Chưa chốt thì dừng và báo.
3. Nếu `DB-Mxx.md` chưa có: chép `output/db-template.md` sang
   `.agents/.claude/system_analysis/output/data-model/db/DB-Mxx.md`, điền frontmatter (`nguon: CD-Mxx v<phiên bản>`),
   bắt đầu bước 1.
4. Nếu đã có: đọc `steps_completed`, làm bước kế tiếp. Nếu `nguon` ghi phiên bản CD cũ hơn CD hiện tại thì báo
   người dùng trước.
5. Chỉ đọc tệp của bước đang làm trong `steps/`. Đọc `output/example.md` một lần để thấy hình dạng kết quả.

## Các bước

| Bước | Tệp | Ứng với phương pháp | Kết quả ghi vào DB-Mxx.md |
|---|---|---|---|
| 1 | `steps/01-tables.md` | Step 1 | Mục 1: bảng; mục 7.1: bảng của module khác |
| 2 | `steps/02-columns.md` | Step 2 | Mục 2: cột từ thuộc tính; thuộc tính đối tượng không chuyển |
| 3 | `steps/03-table-relationships.md` | Step 3 | Mục 3: quan hệ giữa các bảng |
| 4 | `steps/04-keys.md` | Step 4 | Mục 4: khóa chính, khóa ngoại; mục 7.2 |
| 5 | `steps/05-remove-redundancy.md` | Step 5 | Mục 5: cột và bảng bị loại; mục 6: lược đồ cuối và sơ đồ; chốt |
| Gộp | `steps/90-system-merge.md` | — | `DB-SYS.md` (chạy khi mọi module đã chốt `DB-Mxx.md`) |

## Tool

Chạy từ gốc repo iShare. Đặt `SK=.agent-instructions/skills/designing-database` và
`M=.agents/.claude/system_analysis/output/data-model`.

| Tool | Dùng ở | Lệnh |
|---|---|---|
| `merge_db.py --list` | 1, 4 | `python3 $SK/tools/merge_db.py --dir $M/db --list --exclude Mxx` (bảng các module khác đã có, khóa chính và kiểu) |
| `check_db.py` | 1–5 | `python3 $SK/tools/check_db.py --db $M/db/DB-Mxx.md --step N --cd $M/cd/CD-Mxx.md` |
| `build_schema.py` | 5 | `python3 $SK/tools/build_schema.py --db $M/db/DB-Mxx.md --inplace` (dựng lược đồ cuối và sơ đồ từ các bảng bước 1–5) |
| `check_db.py --final` | 5 | `python3 $SK/tools/check_db.py --db $M/db/DB-Mxx.md --final --cd $M/cd/CD-Mxx.md` |
| `merge_db.py` | Gộp | `python3 $SK/tools/merge_db.py --dir $M/db --out-md $M/db/.work/merge-db.md` |

`check_db.py` mặc định kiểm tên bảng, cột, khóa ngoại theo snake_case (QU-06…08; tên bảng số
nhiều). Nếu quy ước đổi: `--table-style tbl` (kiểu phương pháp gốc) hoặc `--table-style none` (không kiểm tên).

Tool bắt lỗi cơ học: lớp chưa có bảng, thuộc tính chưa thành cột, thuộc tính đối tượng bị chuyển thành cột, quan hệ
chưa thành quan hệ giữa bảng, n-n, bảng thiếu khóa chính, quan hệ 1-n thiếu khóa ngoại hoặc khóa ngoại đặt sai
phía, khóa ngoại lệch kiểu với khóa chính, thuộc tính dẫn xuất chưa xử lý, bảng chỉ còn một khóa ngoại, lược đồ
cuối lệch với các bảng bước. ERROR phải sửa trước khi trình cổng; WARN giữ lại phải có lý do.

## Cách hỏi người dùng

Theo mục "Cách hỏi người dùng" của skill `analyzing-functional-requirements`. Phân biệt ba loại câu trả lời theo
`CONVENTIONS.md` mục 6: quy ước chung → `data-model/conventions.md`; quyết định riêng của module → bảng Quyết định
thiết kế (`DD-Mxx-nn`); yêu cầu mới → không ghi vào lược đồ, báo cập nhật FR.

## Mẫu tin nhắn cổng

```
Bước N/5 — <tên bước> — DB-Mxx: xong, chờ bạn xác nhận.

Kết quả: <3–6 dòng con số và điểm chính>
Cần bạn nhìn: <tối đa 8 dòng: chỗ phán đoán, quy ước cần xác nhận, WARN giữ lại kèm lý do>
Đã ghi: DB-Mxx.md mục <…>
Tool: check_db ERROR=0 WARN=n

Trả lời "ok" để sang bước N+1, hoặc nói chỗ cần sửa.
```

Ở cổng bước 5, câu cuối là: `Trả lời "Chốt DB-Mxx" để chốt, hoặc nói chỗ cần sửa.`

## Sửa sau khi đã chốt

Tăng phiên bản, trạng thái về Bản nháp, làm lại từ bước bị ảnh hưởng, vẫn qua cổng. Khi `CD-Mxx.md` lên phiên bản
mới: sửa `nguon`, chạy `check_db.py --cd` để thấy chỗ lệch, làm lại từ bước sớm nhất bị ảnh hưởng, rồi chạy lại
`build_schema.py --inplace`.

## Không làm

- Không thêm bảng, cột, khóa không sinh từ `CD-Mxx.md`.
- Không xử lý n-n ở đây.
- Không sửa `DB-Myy.md` của module khác; khóa ngoại phải nằm ở bảng của module khác thì ghi thành đề nghị (mục 7.2).
- Không sửa tay mục 6: luôn chạy `build_schema.py`.
