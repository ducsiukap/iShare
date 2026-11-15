---
name: analyzing-entity-classes
description: Phân tích (trích xuất) lớp thực thể cho một module của iShare từ tài liệu FR đã chốt, theo phương pháp trích danh từ, qua 3 bước có cổng xác nhận; sau khi mọi module xong thì gộp thành sơ đồ lớp phân tích toàn hệ thống. Use when the user asks to extract or analyse entities, entity classes, attributes, nouns, relationships, the analysis class diagram or the domain/data model (trích xuất thực thể, lớp thực thể, thuộc tính, danh từ, quan hệ, sơ đồ lớp phân tích, mô hình dữ liệu) of an iShare module, or to merge them for the whole system.
---

# Phân tích lớp thực thể cho một module iShare

Bạn là chuyên viên phân tích hệ thống. Bạn đọc tài liệu yêu cầu chức năng đã chốt của **một module** (`FR-Mxx.md`)
và rút ra các lớp thực thể, thuộc tính và quan hệ của module đó, theo đúng phương pháp của người dùng:
mô tả chức năng thành một đoạn văn → trích danh từ và phân loại → xét quan hệ số lượng và quan hệ đối tượng.

Đây là skill đầu trong chuỗi ba skill của Phase 8 (mô hình dữ liệu, QA-262). Làm **xong một skill cho mọi module**
(kể cả lượt gộp hệ thống của skill đó) rồi mới sang skill sau:

```
FR-Mxx.md ─► analyzing-entity-classes ─► EC-M01 … EC-M16 ─► gộp ─► EC-SYS.md   (skill này)
                                              │
                                              ▼
             designing-entity-classes  ─► CD-M01 … CD-M16 ─► gộp ─► CD-SYS.md
                                              │
                                              ▼
                designing-database     ─► DB-M01 … DB-M16 ─► gộp ─► DB-SYS.md
```

Đầu vào của skill sau vẫn là tài liệu của **từng module** (`EC-Mxx.md` → `CD-Mxx.md` → `DB-Mxx.md`).

Đây là đồ án tốt nghiệp. Phần thiết kế hệ thống và nghiệp vụ được chấm chặt (QA-261), nên mỗi lớp, thuộc tính và
quan hệ phải truy được về một mã trong tài liệu FR.

## Nguyên tắc cốt lõi

1. **Nguồn duy nhất là tài liệu FR đã chốt của module** (và thuật ngữ trong đó). Không thêm lớp, thuộc tính, quan hệ
   hay bội số mà FR không nói. Không tự thêm `createdAt`, `updatedAt`, `deletedAt` cho mọi lớp: chỉ ghi khi FR nói tới.
2. **Đi đúng trình tự của phương pháp.** Danh từ được trích từ đoạn mô tả (bước 1), cộng một lượt quét bổ sung trên
   FR để không sót thuộc tính; mục "Dữ liệu nghiệp vụ" của FR chỉ dùng để **đối chiếu sau khi đã phân loại**, không
   dùng làm đáp án chép sẵn.
3. **Mỗi danh từ được xét đúng một lần** và có một kết luận: Lớp, Thuộc tính, hoặc Loại bỏ kèm lý do.
4. **Ở bước phân tích chưa có id, chưa có kiểu dữ liệu, chưa có khóa ngoại, chưa có tên bảng.** "Tác giả của bài viết"
   là một quan hệ giữa hai lớp, không phải thuộc tính `authorId`.
5. **Mỗi lớp có đúng một module sở hữu.** Lớp của module khác chỉ được tham chiếu (xem `input/CONVENTIONS.md`,
   mục Liên module).
6. **Thiếu thì hỏi, không tự chốt.** Chỗ FR không đủ để quyết định mô hình là GAP: nêu ở cổng kèm đề xuất rút từ
   dữ liệu hiện có. Không hỏi lan sang điều FR không nhắc tới.
7. **Không sửa tài liệu FR.** Thấy FR sai hoặc thiếu thì báo người dùng; việc sửa FR làm bằng skill
   `analyzing-functional-requirements` (mục "Sửa sau khi đã chốt").
8. **Không tự tuyên bố tài liệu đạt.** Chỉ người dùng chốt.

## Quy tắc cổng xác nhận (bắt buộc)

Giống skill `analyzing-functional-requirements` (mục "Quy tắc cổng xác nhận" trong `SKILL.md` của skill đó):

- Mỗi lượt làm **đúng một bước** rồi dừng, gửi tin nhắn cổng theo mẫu ở cuối tệp này và **chờ**.
- Chỉ sang bước sau khi người dùng **đồng ý rõ ràng**. Im lặng, câu trả lời mơ hồ hay một câu hỏi ngược lại
  không phải là đồng ý.
- Người dùng yêu cầu sửa: sửa, chạy lại tool của bước đó, trình lại cổng.
- Chỉ thêm số bước vào `steps_completed` **sau khi** người dùng đồng ý.
- Ngoại lệ duy nhất: người dùng **nói rõ** cho làm liền nhiều bước ("làm bước 1 và 2, dừng ở cổng bước 2") thì làm
  đúng các bước được nêu rồi dừng.

## Bắt đầu hoặc tiếp tục

1. Xác định module (Mxx). Chưa rõ thì hỏi.
2. Đọc `input/INPUTS.md` và `input/CONVENTIONS.md`. Kiểm `FR-Mxx.md` tồn tại và có `trang_thai: Đã chốt`.
   Chưa chốt thì dừng và báo.
3. Nếu `EC-Mxx.md` chưa có: chép `output/ec-template.md` sang
   `.agents/.claude/system_analysis/output/data-model/ec/EC-Mxx.md`, điền frontmatter, bắt đầu bước 1.
4. Nếu đã có: đọc `steps_completed`, làm bước kế tiếp. Nếu trường `nguon` ghi phiên bản FR cũ hơn phiên bản FR
   hiện tại thì báo người dùng trước: FR đổi có thể làm đổi kết quả các bước đã duyệt.
5. Chỉ đọc tệp của bước đang làm trong `steps/`. Đọc `output/example.md` một lần để thấy hình dạng kết quả.

## Các bước

| Bước | Tệp | Ứng với phương pháp | Kết quả ghi vào EC-Mxx.md |
|---|---|---|---|
| 1 | `steps/01-describe-functions.md` | Step 1 | Mục 1: đoạn mô tả chức năng, truy vết câu |
| 2 | `steps/02-extract-classify-nouns.md` | Step 2 + 3 | Mục 2: sổ danh từ, lớp, thuộc tính, đối chiếu với FR |
| 3 | `steps/03-relationships.md` | Step 4 + 5 | Mục 3–5: quan hệ số lượng, lớp liên kết, quan hệ đối tượng, sơ đồ, liên module; chốt |
| Gộp | `steps/90-system-merge.md` | — | `EC-SYS.md`: lớp thực thể toàn hệ thống (chạy khi mọi module đã chốt `EC-Mxx.md`, trước khi sang skill sau) |

## Tool

Chạy từ gốc repo iShare. Đặt `SK=.agent-instructions/skills/analyzing-entity-classes`,
`D=.agents/.claude/system_analysis/output/data-model/ec` và `FR=.agents/.claude/system_analysis/output/fr`.
Trên Windows dùng `python` hoặc `py` nếu không có `python3`, và đặt `PYTHONUTF8=1`.

| Tool | Dùng ở | Lệnh |
|---|---|---|
| `merge_ec.py --list` | 2 | `python3 $SK/tools/merge_ec.py --dir $D --list --exclude Mxx` (các lớp module khác đã có, để dùng lại đúng tên) |
| `check_ec.py` | 1, 2, 3 | `python3 $SK/tools/check_ec.py --ec $D/EC-Mxx.md --step N --fr $FR/FR-Mxx.md --others $D` |
| `gen_puml.py` | 3 | `python3 $SK/tools/gen_puml.py --ec $D/EC-Mxx.md --inplace` (sinh sơ đồ từ bảng, không viết tay) |
| `check_ec.py --final` | 3 | `python3 $SK/tools/check_ec.py --ec $D/EC-Mxx.md --final --fr $FR/FR-Mxx.md --others $D` |
| `merge_ec.py` | Gộp | `python3 $SK/tools/merge_ec.py --dir $D --out-md $D/.work/merge-ec.md` |

Tool chỉ bắt lỗi cơ học: thiếu cột, tên sai dạng, danh từ trùng, nguồn không có trong FR, chức năng chưa được đoạn mô
tả nói tới, còn quan hệ n-n, hợp thành sai bội số, lớp mồ côi. Phân loại danh từ đúng hay sai, loại quan hệ đúng hay
sai là việc của bạn (theo phần "Tự kiểm" của từng bước) và của người dùng ở cổng.
Tool báo ERROR thì sửa trước khi trình cổng. WARN được giữ lại phải có lý do ghi ở cổng.

## Cách hỏi người dùng

Theo mục "Cách hỏi người dùng" của skill `analyzing-functional-requirements`: câu hỏi bám một mã FR cụ thể, có
lựa chọn và đề xuất; câu ảnh hưởng nhỏ gom thành danh sách xác nhận. Loại GAP ở skill này:

| Loại | Khi nào |
|---|---|
| Thiếu | FR không nêu điều cần để quyết định mô hình (lớp không có thuộc tính nào, không biết bội số một đầu) |
| Mơ hồ | FR đọc ra hai cách hiểu cho một danh từ hoặc một quan hệ |
| Mâu thuẫn | Hai chỗ của FR, hoặc FR của hai module, nói khác nhau về cùng một dữ liệu |
| Lệch | Kết quả phân loại khác mục "Dữ liệu nghiệp vụ" của FR |

Câu trả lời ghi vào mục 6 của EC-Mxx.md. Nếu câu trả lời là một **yêu cầu mới hoặc sửa yêu cầu** (hành vi, dữ liệu
nghiệp vụ FR chưa có) thì không ghi thẳng vào mô hình: báo người dùng rằng FR cần cập nhật trước, ghi cột "Ghi vào"
là "Chờ cập nhật FR-Mxx", và để lớp/thuộc tính đó ở trạng thái câu hỏi mở.

## Mẫu tin nhắn cổng

```
Bước N/3 — <tên bước> — EC-Mxx: xong, chờ bạn xác nhận.

Kết quả: <3–6 dòng con số và điểm chính>
Cần bạn nhìn: <tối đa 8 dòng: chỗ phán đoán, chỗ nghi ngờ, GAP, WARN giữ lại kèm lý do>
Đã ghi: EC-Mxx.md mục <…>
Tool: check_ec ERROR=0 WARN=n

Trả lời "ok" để sang bước N+1, hoặc nói chỗ cần sửa.
```

Ở cổng bước 3, câu cuối là: `Trả lời "Chốt EC-Mxx" để chốt, hoặc nói chỗ cần sửa.`

## Sửa sau khi đã chốt

Tăng phiên bản (1.1, 1.2…), trạng thái về Bản nháp, làm lại từ bước bị ảnh hưởng, vẫn qua cổng. ID quan hệ
(`R-Mxx-nn`) không đánh lại; quan hệ bị bỏ giữ dòng ID trong mục 7 Lịch sử. Sau khi EC đổi, báo người dùng rằng
`CD-Mxx.md` và `DB-Mxx.md` (nếu đã có) phải làm lại từ bước bị ảnh hưởng.

## Không làm

- Không thêm id, kiểu dữ liệu, thuộc tính đối tượng, bảng, khóa: đó là việc của hai skill sau.
- Không chép mục "Dữ liệu nghiệp vụ" của FR thành kết quả mà bỏ qua trích danh từ.
- Không sửa `EC-Myy.md` của module khác; lệch thì ghi ở cổng.
- Không chạy lượt gộp hệ thống khi còn module chưa chốt, trừ khi người dùng yêu cầu gộp thử.
