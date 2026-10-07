# Skill: analyzing-functional-requirements

Skill này giúp agent (chủ yếu là Claude) viết **tài liệu yêu cầu chức năng (FR)** cho từng module của iShare,
từ draft và các register phỏng vấn đã có. Đầu ra là **một tệp** cho mỗi module, đủ chặt để dùng cho phân tích
và thiết kế hệ thống (use case, mô hình dữ liệu, state machine).

## Nguyên tắc

- **Chỉ bám dữ liệu hiện có.** Không thêm tính năng, con số, quyền hay ngoại lệ mà draft và register chưa nói.
- **Không đề xuất ngoài phạm vi**, trừ khi thiếu một điều làm hành vi đã chốt không chạy được hoặc chạm tới
  quyền hay an toàn dữ liệu. Khi đó agent chỉ ghi "Cần cân nhắc" và để bạn quyết.
- **GAP luôn được hỏi để bạn xác nhận.** GAP là chỗ nguồn đã nói tới một hành vi nhưng chưa đủ để viết thành
  yêu cầu kiểm chứng được (mâu thuẫn, mơ hồ, thiếu chi tiết). Agent kèm đề xuất suy ra từ dữ liệu hiện có.
- **Mỗi bước dừng chờ bạn xác nhận.** Không có bước nào tự chạy tiếp.
- **Câu trả lời của bạn được ghi vào register** (`qa-log.md`, `decisions.md`) sau khi bạn duyệt bản nháp,
  để module sau đọc được.

## Chuẩn bị (làm một lần)

1. **Mở đúng thư mục.** Mở gốc repo `iShare` (trong VS Code: File → Open Folder; trong terminal: `cd` tới gốc repo
   rồi chạy `claude`). Claude Code tìm `CLAUDE.md` và `.claude/skills/` theo thư mục đang mở; mở thư mục con thì
   agent không thấy skill.
2. **Kiểm Python 3.** Tool của skill là script Python 3, chỉ dùng thư viện chuẩn. Trên Windows lệnh thường là `python`
   hoặc `py` thay cho `python3`.
3. **Trên Windows, đặt biến môi trường `PYTHONUTF8=1`** rồi mở lại VS Code/terminal, để tool in được tiếng Việt.
4. **Chọn model** (lệnh `/model` hoặc bộ chọn model trong panel):

   | Bước | Model đề xuất |
   |---|---|
   | 1, 2, 5, 6 (lọc nguồn, hợp nhất quyết định, viết yêu cầu, chọn câu hỏi) | Opus 5.5, effort High |
   | 3, 4, 7 (chức năng, quy tắc/dữ liệu/trạng thái, hoàn thiện) | Opus 5.5, effort Medium là đủ |

   Đổi model giữa các bước không sao, vì trạng thái nằm trong tệp FR.

## Làm một module

Mỗi lần làm **một module**. Mỗi lượt agent làm **một bước** rồi dừng ở cổng, gửi một tin nhắn tóm tắt kết quả và
những điểm cần bạn nhìn. Bạn không cần dán nội dung register hay draft vào chat: agent tự đọc từ repo, và chỉ như
vậy nó mới truy vết được nguồn. Quy tắc cũng đã nằm trong skill, không cần nhắc lại trong prompt.

**Bắt đầu:**

```
Dùng skill analyzing-functional-requirements để viết tài liệu FR cho module M05 (Topic & Tag).
Làm bước 1 rồi dừng ở cổng xác nhận. Chưa sang bước 2.
```

Lần đầu agent chạy tool, Claude Code sẽ hỏi quyền chạy lệnh `python …/tools/…` và quyền ghi `FR-Mxx.md`.
Chọn cho phép (có thể cho phép luôn trong project này để khỏi bị hỏi lại).

**Ở mỗi cổng**, đọc tin nhắn cổng rồi trả lời một trong ba cách:

| Bạn muốn | Gõ |
|---|---|
| Đồng ý, sang bước sau | `ok. Ghi bước 2 vào steps_completed, rồi làm bước 3 và dừng ở cổng.` |
| Đồng ý kèm một chỉnh nhỏ | `ok, nhưng DM-3.3 đổi nhãn thành Phụ thuộc (M03). Sửa xong thì ghi bước 1 vào steps_completed và làm bước 2.` |
| Sửa trước khi đi tiếp | `Sửa bước 3: FR-M05-04 và FR-M05-05 trùng mục tiêu, gộp lại. Chạy lại tool của bước 3 và trình lại cổng.` |

Câu hỏi ngược lại hay câu trả lời mơ hồ **không** được tính là đồng ý; agent sẽ chờ.

Bảy bước và việc của bạn ở từng cổng:

| Bước | Agent làm | Bạn kiểm ở cổng |
|---|---|---|
| 1. Khoanh phạm vi | Lập keyword, quét register và draft, gắn nhãn từng mục nguồn | Phạm vi trong/ngoài đúng chưa; có sót hay thừa nguồn không; các mục ngoài section module bị kéo vào |
| 2. Hợp nhất nguồn | Xác định quyết định nào còn hiệu lực, nào bị thay; tìm mâu thuẫn | Chuỗi sửa đổi; mâu thuẫn (trả lời ngay hoặc để bước 6) |
| 3. Chức năng và vai trò | Danh sách chức năng, vai trò, ma trận quyền | Đủ chức năng chưa; quyền đúng chưa |
| 4. Quy tắc, dữ liệu, trạng thái | Quy tắc nghiệp vụ kèm ví dụ tính tay, thực thể, CRUD, chuyển trạng thái | Quy tắc và ví dụ đúng chưa; vòng đời đủ chưa |
| 5. Viết yêu cầu | Yêu cầu cấp trên, lý do, cấp dưới (luồng chính và ngoại lệ), truy vết | Các yêu cầu "Suy ra"; các chỗ GAP mới |
| 6. Hỏi xác nhận GAP | Gom GAP, hỏi bạn, ghi câu trả lời vào register, hoàn thiện yêu cầu | Trả lời câu hỏi; duyệt bản nháp register trước khi ghi |
| 7. Hoàn thiện và chốt | Điền nốt, chạy kiểm, đối chiếu module khác, đọc lại | Nói "chốt" khi đồng ý |

**Ở bước 6**, agent gửi câu hỏi có phương án A/B/C kèm đề xuất, và các danh sách xác nhận theo chức năng. Trả lời
gọn trong một tin nhắn:

```
1A, 2B, 3: chỉ Admin được làm, Mod thì không. Nhóm câu xác nhận của FR-M05-03: ok cả nhóm.
Câu 4 ngoài phạm vi, bỏ.
Lập bản nháp register (ISS/QA/DEC) cho tôi duyệt trước khi ghi.
```

Agent trình bản nháp các dòng sẽ thêm vào `issue-queue`, `qa-log`, `decisions`. Xem xong:

```
Bản nháp register ổn, ghi đi. Cập nhật FR-M05.md theo câu trả lời rồi trình cổng bước 6.
```

**Chốt:** ở cổng bước 7, khi đã đồng ý, gõ `Chốt FR-M05.` Tài liệu chuyển sang Đã chốt, phiên bản 1.0.

## Tiếp tục ở phiên mới

Phiên mới không nhớ cuộc trò chuyện cũ, nhưng không cần: mọi kết quả nằm trong `FR-Mxx.md` và `output/fr/.work/`.

Nếu bước trước **đã được duyệt**:

```
Dùng skill analyzing-functional-requirements, tiếp tục FR M05.
Đọc steps_completed trong FR-M05.md, so moc_nguon với register hiện tại và báo nếu nguồn đã đổi, rồi làm bước kế tiếp và dừng ở cổng.
```

Nếu phiên cũ **dừng ở cổng mà bạn chưa duyệt** (bước đã làm xong nhưng chưa vào `steps_completed`), nói rõ, để
agent không làm lại bước đó:

```
Dùng skill analyzing-functional-requirements cho M05. Bước 3 đã làm xong trong FR-M05.md và tôi duyệt.
Ghi bước 3 vào steps_completed, rồi làm bước 4 và dừng ở cổng.
```

Không chạy hai phiên cùng lúc trên cùng một module: hai bên có thể ghi đè tệp của nhau.

## Sau khi chốt

**Sửa tài liệu đã chốt:**

```
FR-M05 cần đổi: <điều cần đổi, kèm lý do hoặc nguồn mới>.
Làm theo skill: tăng phiên bản, đưa về Bản nháp, làm lại từ bước bị ảnh hưởng và dừng ở cổng.
```

**Đối chiếu khi có thêm module:**

```
Đã có thêm FR-M06. Chạy lại phần đối chiếu chéo module của bước 7 cho FR-M05 (trace_check --others), chỉ báo các chỗ lệch, không sửa tệp của module khác.
```

**Thứ tự module gợi ý** (module nền trước, để bước 7 của module sau đối chiếu được với tài liệu đã chốt):
M01 → M02 → M03 → M04 → M05 → M06 → M07 → M08 → M09 → M10 → M13 (Must), rồi M11 → M12 → M16 (Should),
rồi M14 → M15 (Could).

## Đầu vào và đầu ra

| | Đường dẫn |
|---|---|
| Nguồn yêu cầu | `docs/_temp/iShare_modules.md`, `docs/_temp/iShare_specs_general.md`, các register trong `.agents/.claude/system_analysis/output/registers/` |
| Chỉ tham khảo | `docs/_temp/iShare_dev_priority.md`, tài liệu mẫu `docs/_temp/system_requirement_demo/` (lấy cấu trúc) |
| Đầu ra | `.agents/.claude/system_analysis/output/fr/FR-Mxx.md` |
| Tệp tạm của tool | `.agents/.claude/system_analysis/output/fr/.work/` (xóa được, chạy lại sẽ sinh lại) |

Chi tiết từng nguồn và các lưu ý về dữ liệu hiện tại: `input/INPUTS.md`.

## Cấu trúc tệp FR

Theo tài liệu mẫu của stakeholder (DEC-139):

1. Tổng quan
2. Thuật ngữ và viết tắt
3. Thông tin đầu vào
4. Tổng quan chức năng: luật/tiêu chuẩn, vai trò, ma trận quyền, danh sách chức năng, ưu tiên
5. Yêu cầu chức năng: mỗi chức năng có yêu cầu cấp trên, lý do, yêu cầu cấp dưới; sau đó là quy tắc nghiệp vụ,
   dữ liệu và CRUD, chuyển trạng thái, giao tiếp với module khác, AI và hành vi khi tắt AI, HMI (chờ thiết kế)
6. Lịch sử sửa đổi

Phụ lục A truy vết, Phụ lục B câu hỏi/TBD, Phụ lục C sổ nguồn. Thân tài liệu không ghi nguồn.
Mẫu đầy đủ: `output/fr-template.md`. Muốn xem một tài liệu đã hoàn chỉnh, mở `FR-M05.md` trong
`.agents/.claude/system_analysis/output/fr/` (module đầu tiên chạy đủ 7 bước).

Quy ước mã:

| Mã | Nghĩa |
|---|---|
| `FR-M05-01` | Chức năng (yêu cầu cấp trên) |
| `FR-M05-01.01` | Yêu cầu cấp dưới |
| `BR-M05-01` | Quy tắc nghiệp vụ |
| `TBD-M05-01` | Điểm chưa chốt |
| `Q-01` | Câu hỏi trong tài liệu |

Mã không bao giờ đánh lại.

## Cấu trúc skill

Skill nằm ở `.agent-instructions/skills/analyzing-functional-requirements/`. Thư mục
`.claude/skills/analyzing-functional-requirements/` chỉ có một tệp trỏ về đây để Claude Code tự nhận skill.

```
analyzing-functional-requirements/
├── SKILL.md        hướng dẫn chính cho agent: nguyên tắc, quy tắc cổng, cách hỏi, tool
├── README.md       tệp này, dành cho người dùng
├── input/INPUTS.md nguồn đầu vào và lưu ý về dữ liệu
├── steps/          01 … 07, mỗi bước một tệp; agent chỉ đọc tệp của bước đang làm
├── output/         fr-template.md (mẫu tệp FR)
└── tools/          script Python 3, chỉ dùng thư viện chuẩn; tools/fixtures/ là dữ liệu kiểm thử tool
```

## Tool

Chạy từ gốc repo. Agent tự chạy; bạn chạy tay khi muốn tự kiểm.

```bash
SK=.agent-instructions/skills/analyzing-functional-requirements
W=.agents/.claude/system_analysis/output/fr/.work

# Lập chỉ mục mọi mục nguồn (DEC, QA, ISS, OPEN, glossary, registry, draft)
python3 $SK/tools/index_sources.py --out $W/index.json
python3 $SK/tools/index_sources.py --next-ids          # ID kế tiếp

# Lọc nguồn cho một module
python3 $SK/tools/scan_sources.py --index $W/index.json --module M05 \
  --keywords "topic,chủ đề,tag,hashtag,trending" --dep-keywords "post,bài viết,search" \
  --draft DM-3.1,DM-3.2 --out-md $W/scan-M05.md --out-json $W/scan-M05.json

# Chuỗi sửa đổi giữa các quyết định
python3 $SK/tools/lineage.py --index $W/index.json --scan $W/scan-M05.json \
  --out-md $W/lineage-M05.md --out-json $W/lineage-M05.json

# Kiểm tệp FR
python3 $SK/tools/lint_fr.py --fr .agents/.claude/system_analysis/output/fr/FR-M05.md \
  --index $W/index.json --lineage $W/lineage-M05.json [--final]
python3 $SK/tools/trace_check.py --fr .agents/.claude/system_analysis/output/fr/FR-M05.md \
  --scan $W/scan-M05.json --lineage $W/lineage-M05.json [--others .agents/.claude/system_analysis/output/fr]
```

`lint_fr.py` và `trace_check.py` trả mã thoát 1 khi có ERROR.

Sau khi sửa tool, chạy thử trên `tools/fixtures/example.md` (kết quả mong đợi: không ERROR) và trên một bản sao
cố ý làm hỏng của tệp đó, để chắc tool vẫn bắt được lỗi.

## Xử lý sự cố

| Hiện tượng | Cách xử lý |
|---|---|
| Agent không nhận ra skill | Kiểm VS Code/terminal đang mở **gốc** repo; gọi đúng tên `analyzing-functional-requirements` |
| `python3: command not found` | Nhắn agent: "dùng `python` thay cho `python3`" |
| `UnicodeEncodeError` khi chạy tool | Đặt `PYTHONUTF8=1` rồi mở lại; hoặc nhắn agent chạy tool kèm biến này |
| Agent làm luôn sang bước sau mà chưa chờ | Nhắc: "Theo quy tắc cổng của skill, chỉ làm một bước rồi dừng"; kiểm `steps_completed` không ghi bước bạn chưa duyệt |
| Agent làm lại một bước đã làm | Dùng prompt "bước N đã làm xong và tôi duyệt" ở mục Tiếp tục ở phiên mới |

## Câu hỏi thường gặp

**Sao agent hỏi nhiều?** Mỗi câu hỏi phải bám một nguồn cụ thể và chỉ hỏi chỗ nguồn đã nhắc tới mà chưa đủ.
Câu ảnh hưởng nhỏ được gom thành danh sách để bạn trả lời "ok cả nhóm". Nếu thấy câu hỏi đi ra ngoài dữ liệu
hiện có, nói "ngoài phạm vi" để agent bỏ.

**Register thay đổi sau khi đã làm vài bước thì sao?** Agent so `moc_nguon` trong tệp FR với register hiện tại
và báo bạn trước khi làm tiếp.

**Muốn sửa tài liệu đã chốt?** Nói rõ điều cần đổi. Agent tăng phiên bản, đưa về Bản nháp và làm lại từ bước bị
ảnh hưởng, vẫn qua cổng như thường.

**Skill sau (đánh giá phụ thuộc, khả thi kỹ thuật) dùng gì từ đây?** Mục "Giao tiếp với module khác",
dependency keywords và Phụ lục C cho phân tích phụ thuộc; mục 5 và mục AI cho đánh giá khả thi.
