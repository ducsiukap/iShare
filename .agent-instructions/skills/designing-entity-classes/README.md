# Skill: designing-entity-classes

Skill này giúp agent **thiết kế lớp thực thể** cho từng module của iShare từ bản phân tích lớp thực thể đã chốt
(`EC-Mxx.md`), theo bốn bước của phương pháp: thêm id → thêm kiểu thuộc tính → chuyển quan hệ liên kết thành kết
tập/hợp thành → thêm thuộc tính đối tượng. Đầu ra là `CD-Mxx.md` cho mỗi module và `CD-SYS.md` cho toàn hệ thống.

Đây là skill thứ hai trong bộ ba skill mô hình dữ liệu. Tổng quan cả bộ và quy ước chung: xem
[README của analyzing-entity-classes](../analyzing-entity-classes/README.md) và
[`CONVENTIONS.md`](../analyzing-entity-classes/input/CONVENTIONS.md).

## Nguyên tắc

- **Đầu vào duy nhất là `EC-Mxx.md` đã chốt.** Skill này không thêm, bỏ hay đổi tên lớp, thuộc tính, quan hệ. Thiếu
  ở bản phân tích thì quay lại sửa bản phân tích.
- **Kiểu phải có căn cứ**: một mã FR/BR hoặc một quy ước `QU-nn`. Không đoán độ dài hay tập giá trị.
- **Mỗi quan hệ một thuộc tính đối tượng, ở một phía.**
- **Mỗi bước dừng chờ bạn xác nhận.**

## Làm một module

```
Dùng skill designing-entity-classes cho module M05.
Làm bước 1 rồi dừng ở cổng xác nhận.
```

Ở module **đầu tiên**, bạn sẽ được hỏi xác nhận các quy ước dùng cho mọi module: QU-02 (kiểu của id) ở cổng bước 1,
QU-04 (bộ kiểu thuộc tính) ở cổng bước 2, QU-05 (cách đặt tên thuộc tính đối tượng) ở cổng bước 4. Kết quả được ghi
vào `.agents/.claude/system_analysis/output/data-model/conventions.md`.

Bốn bước và việc của bạn ở từng cổng:

| Bước | Agent làm | Bạn kiểm ở cổng |
|---|---|---|
| 1. Thêm id | Lập bảng lớp; thêm `id` cho lớp không kế thừa; lớp con dùng id của lớp cha; lớp thống kê không kế thừa không có id | Lớp nào có id, lớp nào không; kiểu của id |
| 2. Thêm kiểu | Chọn kiểu, tính bắt buộc, ràng buộc cho mọi thuộc tính; khai kiểu liệt kê | Kiểu liệt kê và giá trị; các thuộc tính mà tính bắt buộc là suy ra |
| 3. Chuyển quan hệ | Với mỗi lớp liên kết "A + B → C": chọn lớp chứa C và lớp được C tham chiếu; chuyển các quan hệ Liên kết còn lại; mặc định Kết tập | Bên toàn thể của các quan hệ vừa chuyển; dòng nào ghi Hợp thành |
| 4. Thuộc tính đối tượng | Mỗi quan hệ một thuộc tính ở lớp toàn thể (một đối tượng hoặc danh sách); sinh sơ đồ | Tên và kiểu thuộc tính đối tượng; thuộc tính đề nghị cho lớp của module khác; nói `Chốt CD-M05` khi đồng ý |

Cách trả lời ở cổng, cách tiếp tục ở phiên mới và cách sửa sau khi chốt giống skill `analyzing-entity-classes`
(thay `EC` bằng `CD`).

**Sau khi chốt `CD-Mxx`**, làm module kế tiếp bằng chính skill này. Xong mọi module thì chạy lượt gộp `CD-SYS`, rồi
mới sang `designing-database`.

## Gộp toàn hệ thống

Khi mọi module đã chốt `CD-Mxx.md`:

```
Dùng skill designing-entity-classes, chạy lượt gộp hệ thống (steps/90-system-merge.md).
Làm việc A rồi dừng ở cổng.
```

## Đầu vào và đầu ra

| | Đường dẫn |
|---|---|
| Đầu vào | `.agents/.claude/system_analysis/output/data-model/ec/EC-Mxx.md` (Đã chốt) |
| Đầu ra của module | `.agents/.claude/system_analysis/output/data-model/cd/CD-Mxx.md` |
| Bản gộp | `.agents/.claude/system_analysis/output/data-model/cd/CD-SYS.md` |
| Tệp tạm của tool | `.agents/.claude/system_analysis/output/data-model/cd/.work/` |

## Cấu trúc tệp CD

1. Lớp và id
2. Thuộc tính và kiểu; kiểu liệt kê
3. Chuyển quan hệ: quan hệ thành phần – toàn thể; quan hệ giữ nguyên (kế thừa, phụ thuộc)
4. Thuộc tính đối tượng
5. Sơ đồ lớp thiết kế (mã PlantUML, do tool sinh)
6. Liên module
7. Quyết định thiết kế (`DD-Mxx-nn`)
8. Câu hỏi và điểm chưa chốt
9. Lịch sử sửa đổi

Mẫu: `output/cd-template.md`. Ví dụ đầy đủ (case study quản lý khách sạn): `output/example.md`.

## Cấu trúc skill

```
designing-entity-classes/
├── SKILL.md
├── README.md
├── input/INPUTS.md
├── steps/            01-add-id, 02-add-types, 03-convert-relationships, 04-object-attributes, 90-system-merge
├── output/           cd-template.md, cd-system-template.md, example.md
└── tools/            check_cd.py, gen_puml.py, merge_cd.py, mdtab.py
```

`tools/mdtab.py` giống hệt tệp cùng tên ở hai skill kia; sửa ở một nơi thì chép sang hai nơi còn lại.

## Tool

```bash
SK=.agent-instructions/skills/designing-entity-classes
M=.agents/.claude/system_analysis/output/data-model

# Kiểu id, kiểu thuộc tính, kiểu liệt kê các module khác đã dùng
python3 $SK/tools/merge_cd.py --dir $M/cd --list --exclude M05

# Kiểm tới bước N, hoặc kiểm đầy đủ; luôn kèm --ec để đối chiếu với bản phân tích
python3 $SK/tools/check_cd.py --cd $M/cd/CD-M05.md --step 2 --ec $M/ec/EC-M05.md
python3 $SK/tools/check_cd.py --cd $M/cd/CD-M05.md --final  --ec $M/ec/EC-M05.md

# Sinh sơ đồ lớp thiết kế
python3 $SK/tools/gen_puml.py --cd $M/cd/CD-M05.md --inplace

# Lượt gộp hệ thống
python3 $SK/tools/merge_cd.py --dir $M/cd --out-md $M/cd/.work/merge-cd.md
python3 $SK/tools/check_cd.py --cd $M/cd/CD-SYS.md --system --final --ec $M/ec/EC-SYS.md
```

Thử nhanh trên ví dụ:
`python3 $SK/tools/check_cd.py --cd $SK/output/example.md --final --ec .agent-instructions/skills/analyzing-entity-classes/output/example.md`.

## Câu hỏi thường gặp

**Vì sao lớp thống kê không có id?** Theo phương pháp, chỉ lớp không kế thừa mới thêm id, và lớp thống kê không kế
thừa (IncomeStat của case study) cũng không có id vì nó không được lưu: các thuộc tính của nó là dẫn xuất và sẽ bị
loại ở bước 5 của thiết kế CSDL. Kết quả tính mà FR yêu cầu **lưu** thành bản ghi (ví dụ kết quả chốt theo kỳ) đã
được bước phân tích xếp là lớp Thực thể, nên có id như mọi lớp khác; nếu thấy một lớp thống kê cần lưu, agent sẽ
báo để sửa bản phân tích.

**Vì sao mặc định là Kết tập?** Hợp thành kéo theo "xóa toàn thể thì xóa thành phần". Skill chỉ ghi Hợp thành khi FR
nói rõ điều đó; không thì ghi Kết tập để không tự thêm hành vi xóa theo.

**Ký pháp `Room[]` là gì?** Là "danh sách Room", theo cách viết của phương pháp. Khi cài bằng Java, đó là một
`List<Room>`.

**Thuộc tính đối tượng rơi vào lớp của module khác?** Agent ghi thành đề nghị ở mục 6 và không sửa tài liệu của
module kia. Lượt gộp hệ thống sẽ đưa thuộc tính đó vào đúng lớp.
