# Skill: analyzing-entity-classes

Skill này giúp agent (chủ yếu là Claude) **phân tích lớp thực thể** cho từng module của iShare từ tài liệu FR đã
chốt, theo phương pháp trích danh từ: mô tả chức năng thành một đoạn văn → trích danh từ và phân loại → xét quan hệ
số lượng và quan hệ đối tượng. Đầu ra là **một tệp** `EC-Mxx.md` cho mỗi module, và `EC-SYS.md` cho toàn hệ thống.

Đây là skill đầu trong bộ ba skill mô hình dữ liệu (Phase 8, QA-262):

| Thứ tự | Skill | Đầu vào | Đầu ra của module | Bản gộp hệ thống |
|---|---|---|---|---|
| 1 | `analyzing-entity-classes` (skill này) | `FR-Mxx.md` | `EC-Mxx.md` | `EC-SYS.md` |
| 2 | [`designing-entity-classes`](../designing-entity-classes/README.md) | `EC-Mxx.md` | `CD-Mxx.md` | `CD-SYS.md` |
| 3 | [`designing-database`](../designing-database/README.md) | `CD-Mxx.md` | `DB-Mxx.md` | `DB-SYS.md` |

**Làm xong một skill cho mọi module rồi mới sang skill sau**: chạy skill này cho lần lượt từng module, gộp thành
`EC-SYS.md`, rồi mới bắt đầu `designing-entity-classes`; tương tự với skill thứ ba.

## Nguyên tắc

- **Chỉ bám tài liệu FR đã chốt.** Không thêm lớp, thuộc tính, quan hệ FR không nói. Không tự thêm `createdAt`,
  `updatedAt` cho mọi lớp.
- **Đúng trình tự của phương pháp.** Danh từ lấy từ đoạn mô tả, cộng một lượt quét bổ sung trên FR để không sót
  thuộc tính (những danh từ này được ghi rõ "Quét: …"). Mục "Dữ liệu nghiệp vụ" của FR chỉ dùng để đối chiếu sau.
- **Mỗi bước dừng chờ bạn xác nhận.** Không bước nào tự chạy tiếp, trừ khi bạn nói rõ cho làm liền nhiều bước.
- **Thiếu thì hỏi.** Chỗ FR không đủ để quyết định mô hình được nêu ở cổng kèm đề xuất.
- **Không sửa FR.** FR thiếu hoặc sai thì agent báo; bạn sửa FR bằng skill `analyzing-functional-requirements`.

## Chuẩn bị

Giống skill FR: mở **gốc** repo `iShare`; có Python 3 (trên Windows có thể là `python` hoặc `py`); đặt
`PYTHONUTF8=1` để tool in được tiếng Việt.

Model gợi ý: bước 2 và 3 (phân loại danh từ, loại quan hệ) cần phán đoán nhiều, nên dùng model mạnh nhất bạn có với
effort High; bước 1 dùng effort Medium là đủ.

## Làm một module

**Bắt đầu:**

```
Dùng skill analyzing-entity-classes cho module M05 (Topic & Tag).
Làm bước 1 rồi dừng ở cổng xác nhận. Chưa sang bước 2.
```

Tên lớp viết PascalCase và tên thuộc tính viết camelCase (bạn đã chốt). Ở module **đầu tiên**, cổng bước 1 có thêm
phần xác nhận hai quy ước còn chờ (QU-10 sơ đồ PlantUML, QU-11 cách viết bội số, trong `input/CONVENTIONS.md`). Bạn
xác nhận hoặc đổi một lần; kết quả được ghi vào `.agents/.claude/system_analysis/output/data-model/conventions.md` và
dùng cho mọi module sau.

**Ở mỗi cổng**, trả lời một trong ba cách:

| Bạn muốn | Gõ |
|---|---|
| Đồng ý, sang bước sau | `ok. Ghi bước 1 vào steps_completed, rồi làm bước 2 và dừng ở cổng.` |
| Đồng ý kèm một chỉnh nhỏ | `ok, nhưng "lượt gợi ý" phải là lớp, không loại. Sửa xong thì ghi bước 2 và làm bước 3.` |
| Sửa trước khi đi tiếp | `Sửa bước 3: R-M05-02 là Kết tập, không phải Hợp thành. Chạy lại tool và trình lại cổng.` |

Muốn nhanh hơn, bạn có thể cho làm liền: `Làm bước 1 và 2, dừng ở cổng bước 2.`

Ba bước và việc của bạn ở từng cổng:

| Bước | Agent làm | Bạn kiểm ở cổng |
|---|---|---|
| 1. Mô tả chức năng | Viết một đoạn văn đánh số câu, phủ mọi chức năng ở mục 4.4 của FR | Đoạn văn đã gọi tên đủ các đối tượng dữ liệu chưa; có câu nào nói điều FR không nói không |
| 2. Danh từ và phân loại | Trích mọi danh từ, quét bổ sung trên FR, phân loại: Lớp, Thuộc tính, Loại bỏ; lập bảng lớp và thuộc tính; đối chiếu với mục Dữ liệu nghiệp vụ của FR | **Danh từ bị loại và lý do**; lớp nào thật ra là thuộc tính (hoặc ngược lại); thuộc tính dẫn xuất; các dòng lệch với FR |
| 3. Quan hệ | Ma trận cặp lớp; mỗi quan hệ viết hai câu theo hai chiều; tách n-n bằng lớp liên kết; xét gộp 1-1; chọn loại quan hệ; sinh sơ đồ | Bội số hai đầu; lớp liên kết mới; các dòng Hợp thành; bên toàn thể; nói `Chốt EC-M05` khi đồng ý |

**Sau khi chốt `EC-Mxx`**, làm module kế tiếp bằng chính skill này. Xong mọi module thì chạy lượt gộp `EC-SYS`, rồi
mới sang `designing-entity-classes`.

## Tiếp tục ở phiên mới

Mọi kết quả nằm trong `EC-Mxx.md`, nên phiên mới không cần nhớ cuộc trò chuyện cũ.

```
Dùng skill analyzing-entity-classes, tiếp tục EC M05.
Đọc steps_completed trong EC-M05.md, so phiên bản FR ghi ở trường nguon với FR-M05.md hiện tại và báo nếu FR đã đổi,
rồi làm bước kế tiếp và dừng ở cổng.
```

Nếu phiên cũ dừng ở cổng mà bạn chưa duyệt:

```
Dùng skill analyzing-entity-classes cho M05. Bước 2 đã làm xong trong EC-M05.md và tôi duyệt.
Ghi bước 2 vào steps_completed, rồi làm bước 3 và dừng ở cổng.
```

Không chạy hai phiên cùng lúc trên cùng một module.

## Gộp toàn hệ thống

Khi mọi module đã chốt `EC-Mxx.md`:

```
Dùng skill analyzing-entity-classes, chạy lượt gộp hệ thống (steps/90-system-merge.md).
Làm việc A (kiểm kê và tìm điểm lệch) rồi dừng ở cổng.
```

Lượt gộp có ba cổng: A (danh sách điểm lệch và đề xuất), B (bản hợp nhất `EC-SYS.md`), C (đưa thay đổi về tài liệu
module và chốt). Chốt `EC-SYS` xong thì bắt đầu `designing-entity-classes` cho module đầu tiên.

Gộp ngay sau khi xong skill giúp các điểm lệch giữa module (một lớp hai tên, hai module cùng nhận sở hữu một lớp, bội
số khác nhau) được sửa trước khi skill sau dùng tài liệu module làm đầu vào.

## Sau khi chốt

```
EC-M05 cần đổi: <điều cần đổi, kèm lý do hoặc phiên bản FR mới>.
Làm theo skill: tăng phiên bản, đưa về Bản nháp, làm lại từ bước bị ảnh hưởng và dừng ở cổng.
```

EC đổi thì `CD-Mxx` và `DB-Mxx` của module đó cũng phải làm lại từ bước bị ảnh hưởng; agent sẽ nhắc.

## Đầu vào và đầu ra

| | Đường dẫn |
|---|---|
| Nguồn | `.agents/.claude/system_analysis/output/fr/FR-Mxx.md` (Đã chốt), `registers/glossary.md` |
| Đầu ra của module | `.agents/.claude/system_analysis/output/data-model/ec/EC-Mxx.md` |
| Bản gộp | `.agents/.claude/system_analysis/output/data-model/ec/EC-SYS.md` |
| Quy ước đã xác nhận | `.agents/.claude/system_analysis/output/data-model/conventions.md` |
| Tệp tạm của tool | `.agents/.claude/system_analysis/output/data-model/ec/.work/` (xóa được) |

## Cấu trúc tệp EC

1. Mô tả chức năng: đoạn mô tả, truy vết câu
2. Danh từ và phân loại: sổ danh từ, lớp, thuộc tính, đối chiếu với FR
3. Quan hệ: ma trận cặp lớp, quan hệ số lượng, lớp liên kết, bảng quan hệ
4. Sơ đồ lớp phân tích (mã PlantUML, do tool sinh)
5. Liên module
6. Câu hỏi và điểm chưa chốt
7. Lịch sử sửa đổi

Mẫu: `output/ec-template.md`. Ví dụ đầy đủ (case study quản lý khách sạn): `output/example.md`.

| Mã | Nghĩa |
|---|---|
| `EC-M05` | Tài liệu phân tích lớp thực thể của M05 |
| `R-M05-01` | Quan hệ giữa hai lớp; hai skill sau dùng lại đúng mã này |
| `Q-01` | Câu hỏi trong tài liệu |
| `MD-01` | Quyết định gộp ở `EC-SYS.md` |

## Cấu trúc skill

```
analyzing-entity-classes/
├── SKILL.md              hướng dẫn chính cho agent
├── README.md             tệp này
├── input/
│   ├── INPUTS.md         nguồn đầu vào, phần nào của FR dùng ở bước nào
│   └── CONVENTIONS.md    quy ước chung của cả ba skill: nơi lưu, mã, QU-01…11, liên module
├── steps/                01, 02, 03 và 90-system-merge
├── output/               ec-template.md, ec-system-template.md, example.md
└── tools/                script Python 3, chỉ dùng thư viện chuẩn
```

`.claude/skills/analyzing-entity-classes/SKILL.md` chỉ là tệp trỏ về đây.

## Tool

Chạy từ gốc repo. Agent tự chạy; bạn chạy tay khi muốn tự kiểm.

```bash
SK=.agent-instructions/skills/analyzing-entity-classes
D=.agents/.claude/system_analysis/output/data-model/ec
FR=.agents/.claude/system_analysis/output/fr

# Các lớp module khác đã có (để dùng lại đúng tên)
python3 $SK/tools/merge_ec.py --dir $D --list --exclude M05

# Kiểm tài liệu tới bước N, hoặc kiểm đầy đủ trước khi chốt
python3 $SK/tools/check_ec.py --ec $D/EC-M05.md --step 2 --fr $FR/FR-M05.md --others $D
python3 $SK/tools/check_ec.py --ec $D/EC-M05.md --final  --fr $FR/FR-M05.md --others $D

# Sinh sơ đồ lớp phân tích (PlantUML) từ các bảng
python3 $SK/tools/gen_puml.py --ec $D/EC-M05.md --inplace

# Lượt gộp hệ thống
python3 $SK/tools/merge_ec.py --dir $D --out-md $D/.work/merge-ec.md
python3 $SK/tools/check_ec.py --ec $D/EC-SYS.md --system --final
```

`check_ec.py` trả mã thoát 1 khi có ERROR. Thử nhanh trên ví dụ:
`python3 $SK/tools/check_ec.py --ec $SK/output/example.md --final`.

## Câu hỏi thường gặp

**Tool kiểm được gì và không kiểm được gì?** Tool bắt lỗi cơ học: thiếu cột, danh từ trùng, danh từ bị loại không
có lý do, nguồn không có trong FR, chức năng chưa được đoạn mô tả nói tới, tên sai dạng, còn quan hệ n-n, hợp thành
sai bội số, lớp mồ côi, sơ đồ lệch bảng. Tool không biết một danh từ nên là lớp hay thuộc tính, và không biết một
quan hệ là kết tập hay hợp thành: phần đó do agent tự kiểm theo từng bước và do bạn duyệt.

**Vì sao có danh từ ghi "Quét: …"?** Đoạn mô tả ngắn nên thường thiếu thuộc tính (tên, thời điểm, trạng thái…).
Agent đọc thêm thuật ngữ, yêu cầu cấp dưới, quy tắc và bảng trạng thái của FR để bổ sung, và đánh dấu để bạn thấy
danh từ nào không đến từ đoạn mô tả. Nếu bạn muốn làm đúng nguyên bản phương pháp (chỉ lấy từ đoạn mô tả), nói:
`Không quét bổ sung; chỉ trích danh từ từ đoạn mô tả.` Khi đó đoạn mô tả ở bước 1 phải viết đầy đủ hơn.

**Lớp của module khác thì sao?** Vẫn có mặt trong bảng lớp với cột Sở hữu là module kia, để quan hệ có hai đầu, nhưng
không liệt kê thuộc tính. Lượt gộp hệ thống sẽ nối chúng lại.

**FR đổi sau khi đã làm vài bước?** Agent so phiên bản FR ghi ở `nguon` với FR hiện tại và báo trước khi làm tiếp.

## Xử lý sự cố

| Hiện tượng | Cách xử lý |
|---|---|
| Agent không nhận ra skill | Kiểm đang mở **gốc** repo; gọi đúng tên `analyzing-entity-classes` |
| `python3: command not found` | Nhắn agent: "dùng `python` thay cho `python3`" |
| `UnicodeEncodeError` khi chạy tool | Đặt `PYTHONUTF8=1` rồi mở lại |
| Tool báo "bảng thiếu cột" | Có cột bị đổi tên hoặc xóa; khôi phục theo `output/ec-template.md` |
| Agent làm luôn sang bước sau | Nhắc: "Theo quy tắc cổng của skill, chỉ làm một bước rồi dừng" |
| Agent chép mục Dữ liệu nghiệp vụ của FR thành kết quả | Nhắc: "Theo bước 2, mục đó chỉ dùng để đối chiếu ở việc 2.6" |
