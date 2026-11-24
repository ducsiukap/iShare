---
name: designing-entity-classes
description: Thiết kế lớp thực thể cho một module của iShare từ bản phân tích lớp thực thể đã chốt (EC-Mxx.md), qua 4 bước có cổng xác nhận - thêm id, thêm kiểu thuộc tính, chuyển quan hệ liên kết thành kết tập/hợp thành, thêm thuộc tính đối tượng; sau khi mọi module xong thì gộp thành sơ đồ lớp thiết kế toàn hệ thống. Use when the user asks to design entity classes, add ids/types/object attributes, or produce the design class diagram (thiết kế lớp thực thể, sơ đồ lớp thiết kế, kiểu thuộc tính, thuộc tính đối tượng) of an iShare module, or to merge them for the whole system.
---

# Thiết kế lớp thực thể cho một module iShare

Bạn là người thiết kế hệ thống. Bạn nhận bản phân tích lớp thực thể đã chốt của **một module** (`EC-Mxx.md`) và biến
nó thành sơ đồ lớp thiết kế, theo đúng bốn bước của phương pháp:

1. Thêm thuộc tính `id` cho các lớp **không kế thừa** lớp khác.
2. Thêm kiểu cho mọi thuộc tính.
3. Chuyển mọi quan hệ liên kết (association) thành kết tập hoặc hợp thành.
4. Thêm thuộc tính đối tượng ứng với các quan hệ kết tập, hợp thành.

Đây là skill thứ hai trong chuỗi ba skill mô hình dữ liệu:
`analyzing-entity-classes` (EC) → **`designing-entity-classes` (CD)** → `designing-database` (DB).
Skill này bắt đầu khi mọi module đã chốt `EC-Mxx.md` và `EC-SYS.md`, và chạy cho lần lượt
từng module.
Quy ước chung của cả ba (nơi lưu, mã, QU-01…11, liên module) nằm ở
`../analyzing-entity-classes/input/CONVENTIONS.md`. Đọc tệp đó trước khi làm.

## Nguyên tắc cốt lõi

1. **Đầu vào duy nhất là `EC-Mxx.md` đã chốt.** Tập lớp, tập thuộc tính, tập quan hệ và mã quan hệ (`R-Mxx-nn`) giữ
   nguyên như bản phân tích. Skill này chỉ **thêm** id, kiểu, thuộc tính đối tượng, và **đổi loại** các quan hệ
   Liên kết.
2. **Thiếu lớp, thiếu thuộc tính, sai bội số là lỗi của bản phân tích.** Không vá ở đây: dừng, báo người dùng, sửa
   `EC-Mxx.md` bằng skill `analyzing-entity-classes` (tăng phiên bản, qua cổng) rồi mới làm tiếp.
3. **Kiểu của thuộc tính phải có căn cứ**: một mã FR/BR (qua cột "Ràng buộc nguồn nêu" của EC) hoặc một quy ước
   `QU-nn`. Không đoán độ dài, khoảng giá trị hay tập giá trị mà nguồn không nêu.
4. **Mỗi quan hệ chỉ sinh một thuộc tính đối tượng, ở một phía** (lớp toàn thể). Không tạo tham chiếu hai chiều.
5. **Quy ước dùng chung phải thống nhất giữa các module.** Đọc `data-model/conventions.md` trước; chưa có giá trị
   đã xác nhận thì trình ở cổng, không tự chọn rồi áp cho cả dự án.
6. **Không có gì của cơ sở dữ liệu.** Không tên bảng, khóa ngoại, kiểu cột.
7. **Không tự tuyên bố tài liệu đạt.** Chỉ người dùng chốt.

## Quy tắc cổng xác nhận (bắt buộc)

Giống `analyzing-entity-classes` (mục "Quy tắc cổng xác nhận" trong `SKILL.md` của skill đó): mỗi lượt đúng một
bước rồi dừng; chỉ đi tiếp khi người dùng đồng ý rõ ràng; chỉ ghi `steps_completed` sau khi được đồng ý; người dùng
nói rõ cho làm liền nhiều bước thì làm đúng các bước đó rồi dừng.

## Bắt đầu hoặc tiếp tục

1. Xác định module. Đọc `input/INPUTS.md` và `../analyzing-entity-classes/input/CONVENTIONS.md`.
2. Kiểm `EC-Mxx.md` có `trang_thai: Đã chốt`. Chưa chốt thì dừng và báo.
3. Nếu `CD-Mxx.md` chưa có: chép `output/cd-template.md` sang
   `.agents/.claude/system_analysis/output/data-model/cd/CD-Mxx.md`, điền frontmatter (`nguon: EC-Mxx v<phiên bản>`),
   bắt đầu bước 1.
4. Nếu đã có: đọc `steps_completed`, làm bước kế tiếp. Nếu `nguon` ghi phiên bản EC cũ hơn EC hiện tại thì báo
   người dùng trước.
5. Chỉ đọc tệp của bước đang làm trong `steps/`. Đọc `output/example.md` một lần để thấy hình dạng kết quả.

## Các bước

| Bước | Tệp | Ứng với phương pháp | Kết quả ghi vào CD-Mxx.md |
|---|---|---|---|
| 1 | `steps/01-add-id.md` | Step 1 | Mục 1: bảng lớp và id; dòng `id` ở mục 2.1 |
| 2 | `steps/02-add-types.md` | Step 2 | Mục 2: kiểu của mọi thuộc tính, kiểu liệt kê |
| 3 | `steps/03-convert-relationships.md` | Step 3 | Mục 3: quan hệ thành phần – toàn thể, quan hệ giữ nguyên |
| 4 | `steps/04-object-attributes.md` | Step 4 | Mục 4–6: thuộc tính đối tượng, sơ đồ, liên module; chốt |
| Gộp | `steps/90-system-merge.md` | — | `CD-SYS.md` (chạy khi mọi module đã chốt `CD-Mxx.md`, trước khi sang skill sau) |

## Tool

Chạy từ gốc repo iShare. Đặt `SK=.agent-instructions/skills/designing-entity-classes` và
`M=.agents/.claude/system_analysis/output/data-model`.

| Tool | Dùng ở | Lệnh |
|---|---|---|
| `merge_cd.py --list` | 1, 2 | `python3 $SK/tools/merge_cd.py --dir $M/cd --list --exclude Mxx` (kiểu id, kiểu thuộc tính, kiểu liệt kê các module khác đã dùng) |
| `check_cd.py` | 1–4 | `python3 $SK/tools/check_cd.py --cd $M/cd/CD-Mxx.md --step N --ec $M/ec/EC-Mxx.md` |
| `gen_puml.py` | 4 | `python3 $SK/tools/gen_puml.py --cd $M/cd/CD-Mxx.md` (ghi `diagrams/CD-Mxx.puml`, render `.png`, nhúng ảnh vào mục 5; `--no-render` chỉ ghi `.puml`) |
| `check_cd.py --final` | 4 | `python3 $SK/tools/check_cd.py --cd $M/cd/CD-Mxx.md --final --ec $M/ec/EC-Mxx.md` |
| `merge_cd.py` | Gộp | `python3 $SK/tools/merge_cd.py --dir $M/cd --out-md $M/cd/.work/merge-cd.md` |

Tool bắt lỗi cơ học: lớp thiếu id hoặc thừa id, thuộc tính thiếu kiểu, kiểu lạ, kiểu liệt kê chưa khai, còn quan hệ
Liên kết, dạng lệch bội số, thuộc tính đối tượng sai phía hoặc sai kiểu, tham chiếu vòng, và mọi chỗ lệch với
`EC-Mxx.md` (thiếu hoặc thừa lớp, thuộc tính, quan hệ), và sơ đồ: mục 5 chứa mã PlantUML, thiếu ảnh, tệp `.puml`
lệch bảng hoặc ảnh cũ hơn `.puml`. ERROR phải sửa trước khi trình cổng; WARN giữ lại phải có lý do.

Render ảnh dùng chung cách của skill `analyzing-entity-classes` (Java + `plantuml.jar` đặt ở
`.agent-instructions/skills/analyzing-entity-classes/tools/vendor/` hoặc biến `PLANTUML_JAR`; lệnh `plantuml`; hoặc
`--server` khi người dùng đồng ý). `gen_puml.py` trả mã 2 khi không render được: báo người dùng, không tự tìm cách
khác.

## Cách hỏi người dùng

Theo mục "Cách hỏi người dùng" của skill `analyzing-functional-requirements`. Phân biệt ba loại câu trả lời theo
`CONVENTIONS.md` mục 6: quy ước chung → `data-model/conventions.md`; quyết định riêng của module → bảng Quyết định
thiết kế (`DD-Mxx-nn`); yêu cầu mới → không ghi vào mô hình, báo cập nhật FR.

## Mẫu tin nhắn cổng

```
Bước N/4 — <tên bước> — CD-Mxx: xong, chờ bạn xác nhận.

Kết quả: <3–6 dòng con số và điểm chính>
Cần bạn nhìn: <tối đa 8 dòng: chỗ phán đoán, quy ước cần xác nhận, WARN giữ lại kèm lý do>
Đã ghi: CD-Mxx.md mục <…>
Tool: check_cd ERROR=0 WARN=n

Trả lời "ok" để sang bước N+1, hoặc nói chỗ cần sửa.
```

Ở cổng bước 4, câu cuối là: `Trả lời "Chốt CD-Mxx" để chốt, hoặc nói chỗ cần sửa.`

## Sửa sau khi đã chốt

Tăng phiên bản, trạng thái về Bản nháp, làm lại từ bước bị ảnh hưởng, vẫn qua cổng. Khi `EC-Mxx.md` lên phiên bản
mới: sửa `nguon`, chạy `check_cd.py --ec` để thấy chỗ lệch, làm lại từ bước sớm nhất bị ảnh hưởng. Sau khi CD đổi,
báo người dùng rằng `DB-Mxx.md` (nếu đã có) phải làm lại từ bước bị ảnh hưởng.

## Không làm

- Không thêm, bỏ, đổi tên lớp hay thuộc tính so với `EC-Mxx.md`.
- Không thêm phương thức (operation): phương pháp chỉ thiết kế lớp thực thể.
- Không thiết kế bảng, khóa, chỉ mục.
- Không sửa `CD-Myy.md` của module khác; thuộc tính đối tượng rơi vào lớp của module khác thì ghi thành đề nghị.
