# Báo cáo audit — ISH-AUD-M05-r1
<!-- [Vietnamese Doc] -->

| Mã báo cáo | ISH-AUD-M05-r1 |
| --- | --- |
| SR được audit | ISH-SR-M05, phiên bản 0.1 |
| Routing | ISH-RT-M05, phiên bản 0.1 |
| Vòng | 1 |
| Ngày | 2026-10-04 |
| Auditor | Agent Auditor độc lập |
| Kết luận | **Chưa đạt** |

## 1. Tóm tắt

SR M05 có chất lượng viết yêu cầu tốt (EARS, đo được, hạt yêu cầu, truy vết — toàn bộ nhóm B/D tự động sạch) và xử lý đúng hai trường hợp lệch nguồn kinh điển (Tag "không giới hạn" của DRAFT vs "tối đa 5" của register; flat vs 2-tầng Topic). Tuy nhiên `check_sr.py` còn 3 ERROR (COV-01): ba mục nguồn chính là bằng chứng "đã hỏi stakeholder" cho chính quyết định flat-Topic (DEC-140, ISS-207, QA-267) không có mặt ở Phụ lục A cũng như ở cột Nguồn của routing — chỉ được nhắc trong văn bản tự do, không ở vị trí script/Auditor tính là "đã xử lý". Ngoài ra có hai hành vi nguồn đã chốt chưa có chỗ đi: xử lý khi AI gợi ý Topic trả về giá trị ngoài danh sách 11 Topic hợp lệ (DEC-132, bị `disposition-M05.md` phân loại nhầm "không liên quan") và tính năng Follow Topic/Tag đã được xác nhận trong phạm vi dự án (QA-043, `iShare_dev_priority.md`) nhưng chưa có module nào — kể cả M05 — nhận sở hữu, không có OP nào được lập. Vì còn DEFECT Cao mở (COV-01) và ERROR > 0, kết luận là **Chưa đạt**.

| Lớp \ Mức | Cao | Trung bình | Thấp |
|---|---|---|---|
| DEFECT | 1 | 1 | 1 |
| CONFLICT | 0 | 0 | 0 |
| GAP | 0 | 1 | 0 |
| OBSERVATION | 0 | 1 | 0 |

## 2. Phạm vi và phương pháp

- Tệp đã đọc: `ISH-SR-M05.md` (v0.1, 2026-10-04), `ISH-RT-M05.md` (v0.1, 2026-10-04), `decisions.md`, `issue-queue.md`, `qa-log.md`, `module-registry.md`, `open-issues.md`, `docs/_temp/iShare_modules.md`, `iShare_specs_general.md`, `iShare_dev_priority.md`.
- Script: `inventory.py` (từ khóa riêng: `topic,tag,chủ đề,thẻ,gộp,merge,trending,flat,phân loại,category`) → `WORK/audit-inventory-M05-r1.md/.json`; `check_sr.py` → `WORK/check-M05-r1.json` (ERROR=3, WARN=0, INFO=6).
- Tính độc lập: ma trận độ phủ (`WORK/coverage-M05-r1.md`) lập xong trước khi mở `ISH-SR-M05.md`/`ISH-RT-M05.md`; chỉ đọc bảng header của hai tệp này trước đó. `disposition-M05.md` và `selfcheck-M05.md` chỉ mở sau khi hoàn tất Bước 4 (đối chiếu ma trận với SR/routing).
- Người gọi không gửi kèm tóm tắt/nhận định nào của Author ngoài mã module, số vòng, đường dẫn gốc repo — không có phần nào cần bỏ qua.
- **Giới hạn không kiểm được:**
  - Không kiểm chứng được việc các module khác (M02, M03, M06, M07, M13, M14) có thực sự tiếp nhận các mục routing R5 (Lớp/Khối, Follow) khi SR của chúng được soạn — các SR đó chưa tồn tại tại thời điểm audit.
  - Không audit các module khác, chỉ dùng chúng làm tham chiếu biên giới cho M05.
  - Không chạy được ca kiểm thực tế (không có hệ thống) — "viết được ca kiểm" (CL-B08) được đánh giá bằng cách tự viết Given/When/Then trên giấy cho một mẫu có chủ đích (8/36 yêu cầu cấp dưới), không phải toàn bộ 36.
  - Việc lấy mẫu KEYWORD (78 mục) có chủ đích, không đọc toàn bộ 78 mục chi tiết — tập trung vào các mục có khả năng mô tả hành vi Topic/Tag thật (AI Topic Suggestion, Follow, Search dùng Topic/Tag làm entity). Các mục còn lại (M06 Search chi tiết, M13 AI Layer model/timeout, M09/M10/M12/M15/M16) chỉ đọc tiêu đề.

## 3. Kết quả kiểm tra tự động

ERROR = 3, WARN = 0, INFO = 6.

- `COV-01` × 3: `DEC-140`, `ISS-207`, `QA-267` chưa được xử lý (không có trong Phụ lục A, cũng không trong cột Nguồn của routing) → xem AUD-M05-01.
- `COV-03` × 5 (INFO, không phải lỗi): `DEC-049`, `DEC-050`, `DEC-051`, `DEC-052`, `QA-104` vừa ở SR vừa ở routing — đã đọc tay cả hai phần, xác nhận không trùng nội dung (SR giữ hành vi quan sát được, routing giữ cơ chế lưu trữ/hiệu năng) → không lập finding, đúng CL-A10.
- `COV-00` (INFO): OWNED=23, trong SR=19, trong routing=6.

## 4. Ma trận độ phủ nguồn → yêu cầu

Ma trận đầy đủ ở `WORK/coverage-M05-r1.md`. Tóm tắt các dòng có finding (mục OWNED còn lại khớp đầy đủ, xem Phụ lục A của SR):

| Nguồn | Mong đợi (Auditor) | Thực tế (SR / routing) | Kết quả | AUD |
|---|---|---|---|---|
| DEC-140, ISS-207, QA-267 | Phụ lục A (một dòng Nguồn cho ISH-M05-001.5/001.6) hoặc hàng routing riêng | Chỉ xuất hiện ở SR §3.1 (danh sách tài liệu đầu vào) và routing R6 cột "Bị thay bởi" (không phải cột Nguồn) | Thiếu | 01 |
| DEC-132 (+ ISS-194, QA-253) | SR (nhánh bổ sung của 5.4 AI gợi ý Topic: xử lý khi AI trả về Topic ngoài danh sách 11 giá trị) | `disposition-M05.md` ghi "Không liên quan" — không có trong SR, không có trong routing | Thiếu | 02 |
| QA-043, ISS-051 (Follow scope), `iShare_dev_priority.md` §3 Giai đoạn 2 (Follow Topic/Tag) | OP-M05-nn (Đề xuất, chủ sở hữu chưa xác định) hoặc routing R5 nếu Author xác định module khác sở hữu | Không có trong SR, routing, Phụ lục B, hay `disposition-M05.md` | Thiếu | 03 |
| DRAFT iShare_modules.md §11.2 ("AI đề xuất: Topic/Category, **Tags**") | SR theo register (chỉ Topic được AI gợi ý — DEC-050; Tag hoàn toàn tự do — DEC-051), kèm cả hai nguồn và dấu vết đã báo stakeholder (RULES §7.5) | SR chỉ có AI gợi ý Topic (đúng theo register), nhưng không có dòng nào ghi nhận đã thấy và xử lý lệch với DRAFT §11.2 | Lệch nguồn chưa đủ dấu vết | 04 |

## 5. Phát hiện

### AUD-M05-01 — Ba mục nguồn xác nhận "Topic phẳng" (DEC-140, ISS-207, QA-267) không có trong Phụ lục A cũng không trong cột Nguồn của routing

| Lớp | DEFECT | Mức | Cao | Checklist | CL-A02 |
|---|---|---|---|---|---|

- **Vị trí:** Phụ lục A của `ISH-SR-M05.md` (dòng 236-273); routing `ISH-RT-M05.md` R6 (dòng 42-46).
- **Bằng chứng trong SR/routing:** routing chỉ nhắc "DEC-140 (xem QA-267)" ở cột **Bị thay bởi**, không ở cột **Nguồn**: `| ISS-046, QA-033 | DEC-140 (xem QA-267) | Phần "2 tầng: Category → Topic"...` (`ISH-RT-M05.md:46`). SR §3.1 chỉ liệt kê DEC-140/QA-267 trong danh sách tài liệu đầu vào (`ISH-SR-M05.md:50,52`), không phải Phụ lục A. `ISS-207` không xuất hiện ở bất kỳ đâu trong hai tệp (xác nhận bằng `grep -n -F "ISS-207" ISH-SR-M05.md ISH-RT-M05.md` → 0 kết quả).
- **Bằng chứng trong nguồn:** "Phase 5 (DEC-047/048...) is confirmed as final for M05's SR... This explicitly supersedes the Phase 3/4 '2 tầng: Category → Topic' scoping in QA-033/ISS-046, which register had not previously marked as amended." (`decisions.md:768-769`, DEC-140); "SR M05 — Topic classification: flat (DEC-047/048) hay 2 tầng Category→Topic (QA-033/ISS-046)? Register không ghi rõ ghi đè | Closed | Flat thắng, xem DEC-140 → QA-267" (`issue-queue.md:328`, ISS-207); "Flat — DEC-047/048... là quyết định cuối, ghi đè QA-033/ISS-046..." (`qa-log.md:1002`, QA-267).
- **Vấn đề:** Ba mục này chính là hồ sơ "đã hỏi và đã trả lời stakeholder" cho câu hỏi flat-vs-2-tầng — đúng loại bằng chứng mà CL-A08/CL-A09/CL-F03 yêu cầu phải có ID register khớp trong SR. Vì chúng không có dòng Phụ lục A hay dòng Nguồn trong routing, `check_sr.py` không thể xác nhận tự động rằng SR đã xử lý hết mục OWNED, và người đọc SR độc lập không thấy được dấu vết quyết định đã được hỏi/trả lời — dù nội dung "flat, không Category" đã được viết đúng ở ISH-M05-001.5/.6.
- **Hệ quả nếu không sửa:** `check_sr.py` tiếp tục báo ERROR (chặn bàn giao theo RULES §8.4); SR "Đã chốt" sau này sẽ thiếu bằng chứng tự chứa cho quyết định flat-Topic.
- **Hướng xử lý (Author quyết cách viết):** Thêm DEC-140/ISS-207/QA-267 vào cột Nguồn của Phụ lục A cho ISH-M05-001.5 và/hoặc ISH-M05-001.6 (bên cạnh DEC-048/ISS-080/QA-102), hoặc thêm một dòng routing R4 riêng ghi nhận quá trình hỏi-trả lời này.
- **Trạng thái (từ vòng 2):** Mở

### AUD-M05-02 — Thiếu yêu cầu xử lý khi AI gợi ý Topic trả về giá trị ngoài danh sách 11 Topic hợp lệ

| Lớp | DEFECT | Mức | Trung bình | Checklist | CL-B09 |
|---|---|---|---|---|---|

- **Vị trí:** SR mục 5.4 (ISH-M05-002, dòng 111-134) — thiếu một yêu cầu cấp dưới.
- **Bằng chứng trong SR:** 5.4 chỉ có 8 yêu cầu cấp dưới (002.1 nội dung ngắn, 002.2 thông báo, 002.3 chỉnh tự do, 002.4-.6 is_stale, 002.7 AI không khả dụng, 002.8 AI không phản hồi sau thử lại) — không có yêu cầu nào cho trường hợp AI **có** phản hồi nhưng giá trị trả về nằm ngoài 11 Topic hợp lệ. Yêu cầu gần nhất về "ngoài danh sách" là ISH-M05-001.6 (`ISH-SR-M05.md:109`) nhưng đó là khi **người dùng** tự chọn giá trị ngoài danh sách, không phải khi **AI** trả về giá trị ngoài danh sách.
- **Bằng chứng trong nguồn:** "Topic Suggestion (GPT-4o-mini) output is validated against the system's fixed 11-topic whitelist. If the returned topic does not match, it is treated as a suggestion failure: a non-blocking error is shown ('Không thể gợi ý chủ đề lúc này, vui lòng chọn thủ công') and the user selects manually." (`decisions.md:722`, DEC-132).
- **Vấn đề:** Đây là một nhánh luồng khác với các nhánh đã có ở 5.4 (khác "nội dung ngắn", khác "AI timeout/không khả dụng") — theo RULES §4.3 mỗi nhánh luồng cần một yêu cầu cấp dưới riêng. `disposition-M05.md` (dòng 41) phân loại DEC-132 là "Không liên quan" với lý do "Thuộc Phase 6 cross-cutting AI, áp dụng chung nhiều module; không có quyết định riêng cho M05" — lý do này không đúng với nội dung DEC-132: quyết định chỉ nói về whitelist 11-Topic của M05 và hành vi hiển thị lỗi trên luồng gợi ý Topic của M05, không áp dụng cho module nào khác (khác với DEC-133 cùng nhóm, thực sự áp dụng chung Moderation/Embedding/Topic Suggestion nên phân loại "không liên quan" cho DEC-133 là hợp lý).
- **Hệ quả nếu không sửa:** Hành vi khi AI "ảo giác" ra một Topic không hợp lệ không được kiểm chứng được từ SR; dev có thể bỏ sót việc validate kết quả AI theo whitelist.
- **Hướng xử lý (Author quyết cách viết):** Thêm một yêu cầu cấp dưới ISH-M05-002.x (mẫu "Nếu…, thì…" vì đây là lỗi/ngoại lệ không do hành động hợp lệ của người dùng, theo RULES §4.6.4): khi kết quả AI gợi ý nằm ngoài danh sách 11 Topic hợp lệ, hệ thống phải hiển thị lỗi không chặn xuất bản và cho chọn thủ công — nguồn DEC-132 (+ ISS-194, QA-253 cùng nội dung). Cập nhật lại `disposition-M05.md` cho DEC-132/ISS-194/QA-253 (tách khỏi nhóm "không liên quan" của DEC-133/ISS-195/QA-254).
- **Trạng thái (từ vòng 2):** Mở

### AUD-M05-03 — Tính năng Follow Topic/Tag đã được xác nhận trong phạm vi dự án nhưng chưa có module nào nhận sở hữu, không có điểm mở nào được lập

| Lớp | GAP | Mức | Trung bình | Checklist | CL-A03 |
|---|---|---|---|---|---|

- **Vị trí:** Không có vị trí trong SR/routing — đây chính là vấn đề (không có chỗ đi).
- **Bằng chứng trong SR/routing/disposition:** `grep -n -i -E "theo d[oõ]i|follow" ISH-SR-M05.md ISH-RT-M05.md disposition-M05.md selfcheck-M05.md` → 0 kết quả liên quan ở cả bốn tệp.
- **Bằng chứng trong nguồn:** "Follow scope — user/topic/post/group?" → "Follow: User (nhận noti khi họ post), Topic (nhận noti khi có post mới trong topic), Post... Không follow Group" (`qa-log.md:520-521`, QA-043, trả lời cho ISS-051); "Follow (User / Post / Topic / Tag / Group)" nằm trong Giai đoạn 2 `[P1]` mục Interaction, tức đã được stakeholder xác nhận đưa vào phạm vi chính thức (`docs/_temp/iShare_dev_priority.md:83`, cùng lời khẳng định "Toàn bộ module/tính năng liệt kê trong tài liệu này đã được XÁC NHẬN đưa vào phạm vi chính thức", dòng 5).
- **Vấn đề:** Topic và Tag là hai đối tượng có thể được follow theo nguồn, nhưng không có quyết định Phase 5 nào (của M05 hay module nào khác đã được audit) vận hành hoá hành vi này (nút Follow, trạng thái đang follow, số người follow...). Theo RULES §5.2, khi chưa chắc module nào sở hữu một hành vi, Author phải viết ở module đang làm kèm `OP-Mxx-nn` loại Đề xuất để stakeholder chốt chủ sở hữu — M05 không làm điều này, và cũng không ghi "không liên quan" có lý do trong `disposition-M05.md` như với các mục KEYWORD khác.
- **Hệ quả nếu không sửa:** Hành vi Follow Topic/Tag có nguy cơ không module nào nhận, không bao giờ được viết thành yêu cầu ở bất kỳ SR nào.
- **Hướng xử lý (Author quyết cách viết):** Thêm `OP-M05-07` loại Đề xuất ở Phụ lục B nêu rõ câu hỏi "Module nào sở hữu hành vi Follow Topic/Tag — M05 (vì Topic/Tag là đối tượng bị follow) hay một module Follow/Notification chung?", hoặc bổ sung dòng disposition "không liên quan vì sẽ do module X xử lý" nếu Author có cơ sở xác định module khác.
- **Trạng thái (từ vòng 2):** Mở

### AUD-M05-04 — Lệch nguồn chưa ghi nhận: DRAFT nói AI gợi ý cả Tag, register chỉ quyết AI gợi ý Topic

| Lớp | DEFECT | Mức | Thấp | Checklist | CL-A08 |
|---|---|---|---|---|---|

- **Vị trí:** SR mục 5.4/5.6 (không có dòng nào xử lý điểm lệch này); routing (không có dòng R6/R7 nào cho DRAFT §11.2).
- **Bằng chứng trong SR/routing:** `grep -n -i -E "AI.*[Tt]ag|[Tt]ag.*AI" ISH-SR-M05.md ISH-RT-M05.md` → 0 kết quả liên quan đến "AI gợi ý Tag". SR chỉ có AI gợi ý Topic (ISH-M05-002) và Tag hoàn toàn thủ công (ISH-M05-004.5: "Khi người dùng nhập một Tag chưa tồn tại, hệ thống phải tạo Tag đó mà không cần phê duyệt." — `ISH-SR-M05.md:175`).
- **Bằng chứng trong nguồn:** "AI đề xuất: Topic / Category, Tags" (`docs/_temp/iShare_modules.md:583-586`, §11.2) — DRAFT nói AI gợi ý cả Tag; nhưng "Tag data model + rules... Fully free — mod/admin do NOT edit/merge/delete under normal conditions" + "Auto-created, no approval" (`decisions.md:297-301`, DEC-051) và "AI suggest topic flow" (`decisions.md:288`, DEC-050, chỉ nói Topic) không hề nhắc AI với Tag.
- **Vấn đề:** Đây là một lệch nguồn theo đúng khuôn RULES §7.5 (DRAFT nói một đằng, Phase-5 cụ thể hơn nói khác) nhưng không có QA/DEC nào nói rõ ràng "AI không gợi ý Tag" — SR âm thầm theo register (hợp lý, vì Tag "fully free" khó đi cùng gợi ý AI) nhưng không ghi cả hai nguồn, không có dấu vết đã nhận diện và báo stakeholder.
- **Hệ quả nếu không sửa:** Nếu register thực ra chưa chốt rõ việc này (chỉ là thiếu sót khi viết DEC-050/051, không phải quyết định tường minc "bỏ AI-Tag"), SR sẽ âm thầm cắt một tính năng DRAFT từng nêu mà chưa ai xác nhận.
- **Hướng xử lý (Author quyết cách viết):** Thêm một dòng Phụ lục A hoặc routing R7 ghi nhận: DRAFT §11.2 từng nêu AI gợi ý cả Tag; DEC-050/051 (Phase 5, cụ thể hơn) chỉ quyết AI gợi ý Topic, Tag hoàn toàn tự do — và nêu ở mục bàn giao như một OBSERVATION để stakeholder xác nhận đây là chủ đích, không phải bỏ sót.
- **Trạng thái (từ vòng 2):** Mở

## 6. Cần stakeholder quyết

```
Vấn đề: Tính năng Follow Topic/Tag (đã xác nhận trong phạm vi dự án ở Giai đoạn 2) chưa có module nào nhận sở hữu.
Nguồn: QA-043 (qa-log.md:520-521): "Follow: User..., Topic (nhận noti khi có post mới trong topic)..."; iShare_dev_priority.md:83: "Follow (User / Post / Topic / Tag / Group)".
Lựa chọn: A) M05 sở hữu (nút Follow/Unfollow Topic/Tag, đếm số người follow) vì Topic/Tag là đối tượng bị follow — hệ quả: M05 cần thêm một tính năng mới (5.x) trước khi "Đã chốt".
          B) Một module Follow/Notification chung (chưa xác định Mxx) sở hữu toàn bộ cơ chế Follow (User/Post/Topic/Tag), M05 chỉ tham chiếu — hệ quả: cần xác định module đó trước khi M05 có thể đóng Phụ lục B.
Đề xuất: B, vì Follow áp dụng đồng thời trên 4 loại đối tượng (User/Post/Topic/Tag) theo QA-043 — một cơ chế chung nhất quán hơn là chia nhỏ theo từng module sở hữu đối tượng.
Liên quan: AUD-M05-03
```

```
Vấn đề: DRAFT (§11.2) từng nêu AI gợi ý cả Tag, nhưng Phase 5 (DEC-050/051) chỉ quyết AI gợi ý Topic; chưa rõ đây là quyết định chủ đích bỏ AI khỏi Tag hay là thiếu sót khi đặc tả Phase 5.
Nguồn: iShare_modules.md:583-586 ("AI đề xuất: Topic/Category, Tags"); decisions.md:297-301 (DEC-051: Tag "Fully free", "Auto-created, no approval", không nhắc AI).
Lựa chọn: A) Xác nhận Tag hoàn toàn không có AI gợi ý (giữ nguyên SR hiện tại) — hệ quả: không đổi SR, chỉ cần ghi chú nguồn.
          B) Bổ sung AI gợi ý Tag (như DRAFT ban đầu) — hệ quả: M05 cần thêm một nhánh luồng AI-suggest-Tag tương tự 5.4.
Đề xuất: A, vì DEC-051 mô tả Tag theo hướng hoàn toàn tự do/không kiểm duyệt, mâu thuẫn về triết lý với việc để AI gợi ý.
Liên quan: AUD-M05-04
```

## 7. Kết quả checklist

| Mã | Kết quả | AUD / ghi chú |
|---|---|---|
| CL-A01 | Đạt | DRAFT §3.1→ISH-M05-001.5 (qua DEC-048); §3.2→ISH-M05-004.1 (ghi cả 2 nguồn); §3.3/§3.4→routing R5; specs_general §3/§4→SR §3.1 (tài liệu đầu vào) |
| CL-A02 | **Không đạt** | AUD-M05-01 (COV-01 × 3: DEC-140, ISS-207, QA-267). **Selfcheck ghi "Đạt"** (dựa trên lần chạy `check_sr.py` cũ, trước khi các mục "System Requirement — M05" được thêm vào register) |
| CL-A03 | **Không đạt** | AUD-M05-02 (DEC-132 có dòng disposition nhưng lý do "không liên quan" không đúng nội dung nguồn); AUD-M05-03 (QA-043/ISS-051, Follow Topic/Tag — không có dòng disposition nào) |
| CL-A04 | Đạt | `check_sr` COV-02 = 0 |
| CL-A05 | Đạt | Đối chiếu nguyên văn DEC-047…052, DEC-090, DEC-099, DEC-008 với SR — khớp nghĩa |
| CL-A06 | Đạt | Mọi dòng "Suy ra" (001.3/.4/.6, 003.2, 004.2/.4/.6/.7) có Ghi chú nêu phép suy luận hợp lệ theo RULES §4.5, không tạo số liệu/ngoại lệ mới |
| CL-A07 | Đạt | Số liệu (1, 3, 11, 20, 5, 30, 7, công thức 1+2×upvote+comment) đều trace được tới nguồn qua `grep` |
| CL-A08 | **Không đạt** | AUD-M05-04 (lệch DRAFT §11.2 "AI gợi ý Tag" vs DEC-050/051 chưa ghi nhận). Trường hợp Tag "không giới hạn" (DRAFT §3.2) vs DEC-051 ("tối đa 5") thì **Đạt** — SR có ghi cả hai nguồn ở ISH-M05-004.1 kèm ghi chú xử lý đúng RULES §7.5 |
| CL-A09 | Đạt | QA-033/ISS-046 (2 tầng) được routing R6 ghi rõ "bị thay bởi DEC-140" |
| CL-A10 | Đạt | COV-03 (DEC-049/050/051/052, QA-104): đọc tay xác nhận SR giữ hành vi, routing giữ cơ chế lưu trữ/hiệu năng, không trùng lặp |
| CL-B01 | Đạt | `check_sr` EARS-01…03 = 0 |
| CL-B02 | Đạt | `check_sr` RULE-01/02/08 = 0; đọc tay xác nhận một ý một yêu cầu |
| CL-B03 | Đạt | `check_sr` RULE-04 = 0; không còn từ mơ hồ ngoài danh sách |
| CL-B04 | Đạt | `check_sr` RULE-03 = 0 |
| CL-B05 | Đạt | `check_sr` RULE-05 = 0 |
| CL-B06 | Đạt | `check_sr` RULE-06/07 = 0; đọc tay không thấy tên bảng/cột/API lọt vào SR |
| CL-B07 | Đạt | `check_sr` RULE-09 = 0 |
| CL-B08 | Đạt | Thử viết ca kiểm Given/When/Then cho mẫu 8/36 yêu cầu cấp dưới (001.4, 002.8, 003.1, 004.2, 004.7, 005.1, 005.4, 006.1) — mọi ca đều viết được |
| CL-B09 | **Không đạt** | AUD-M05-02 (thiếu nhánh "AI trả về Topic ngoài whitelist") |
| CL-B10 | Đạt | Mỗi giới hạn độc lập một yêu cầu cấp dưới riêng (min/max Topic tách; max-count/max-length Tag tách) |
| CL-B11 | Đạt | Quyền Mod/Admin viết thành yêu cầu riêng (ISH-M05-003, ISH-M05-005) |
| CL-C01 | Đạt | Đọc 36 yêu cầu theo đối tượng (Topic/Tag/Trending) — không thấy cặp mâu thuẫn |
| CL-C02 | Đạt | Không có cấp dưới chỉ lặp lại cấp trên |
| CL-C03 | Đạt | Mọi thuật ngữ 2.1 (Topic, Tag, Trending, Đã lỗi thời, Mod, Admin, Upvote) được dùng trong mục 5; Mod/Admin viết hoa nhất quán |
| CL-C04 | Đạt | "Lý do" của ISH-M05-001 lấy từ DRAFT §3.1; các tính năng còn lại ghi đúng "Nguồn chưa nêu lý do." kèm OP tương ứng |
| CL-C05 | Đạt | 5.1 đủ 6 dòng khớp 5.3-5.8; Must khớp module-registry (nhóm Must 10); P0/AI-P0/P1 khớp hợp lý với `iShare_dev_priority.md` §3; 5.2 trỏ đúng ISH-M05-005 |
| CL-D01 | Đạt | `check_sr` HDR-01…08 = 0 |
| CL-D02 | Đạt | `check_sr` STR-01…09 = 0 |
| CL-D03 | Đạt | `check_sr` REQ-00…04 = 0 |
| CL-D04 | Đạt | `check_sr` ID-01…06 = 0 (bản đầu, không có ID cũ) |
| CL-D05 | Đạt | `check_sr` TRC-01…10 = 0; đếm tay 36/36 ID có dòng Phụ lục A |
| CL-D06 | Đạt | `check_sr` REF-01/02 = 0; SR không tham chiếu ID module khác trong thân yêu cầu |
| CL-E01 | Đạt | Không có tên bảng/trường/công nghệ/HMI trong mục 4-5; đã chuyển đúng R1/R2/R3 |
| CL-E02 | Đạt | Lớp/Khối chỉ ở routing R5 (không viết hành vi trong SR); ranh giới hiển thị Trending với M14 được để ở OP-M05-06, không tự quyết |
| CL-E03 | Đạt | `check_sr` RT-01…04 = 0; R5 có module+ID sở hữu; R6 có "bị thay bởi"; R3/R7 trống hợp lý (không có nội dung HMI hay mục bị loại khỏi phạm vi) |
| CL-E04 | Đạt | Mục 4.1 "Không có."; không có nội dung pháp lý/riêng tư tự thêm |
| CL-F01 | Đạt | `check_sr` OPN-01…03 = 0; 6 OP đều loại Đề xuất, trạng thái Mở, hợp lệ với trạng thái "Bản nháp" |
| CL-F02 | Đạt | `check_sr` REV-01…03 = 0; dòng cuối lịch sử (0.1) khớp header |
| CL-F03 | **Không đạt** | Liên quan AUD-M05-01: câu trả lời stakeholder cho ISS-207/QA-267/DEC-140 đã có ID register nhưng SR không khớp (không có trong Phụ lục A) |
| CL-F04 | **Không đạt** | AUD-M05-03: Follow Topic/Tag là một điểm chưa rõ ràng chưa được raise cho stakeholder (không có OP) |
| CL-F05 | Đạt | `grep "phải"` trong mục 1-4 → 0 kết quả |
| CL-F06 | Đạt | `[Vietnamese Doc]` có ở cả hai tệp; tiếng Anh chỉ giữ cho Topic/Tag/Trending/Upvote/AI theo đúng cách dùng của register |

## 8. Vòng trước (chỉ vòng 2)

Không áp dụng — đây là vòng 1.

## 9. Hồ sơ xác minh

- `grep -n -F "DEC-140" ISH-SR-M05.md` → 1 kết quả (dòng 50, trong §3.1, không phải Phụ lục A).
- `grep -n -F "ISS-207" ISH-SR-M05.md ISH-RT-M05.md` → 0 kết quả.
- `grep -n -F "QA-267" ISH-SR-M05.md ISH-RT-M05.md` → 1 kết quả (SR dòng 52, §3.1); `grep -n -F "DEC-140" ISH-RT-M05.md` → 1 kết quả (dòng 46, cột "Bị thay bởi" của R6, không phải cột Nguồn).
- `grep -n -F "DEC-132" ISH-SR-M05.md ISH-RT-M05.md` → 0 kết quả; `grep -n -F "DEC-132" disposition-M05.md` → 1 kết quả (dòng 41, phân loại "Không liên quan").
- `grep -n -i -E "theo d[oõ]i|follow"` trên `ISH-SR-M05.md`, `ISH-RT-M05.md`, `disposition-M05.md`, `selfcheck-M05.md` → 0 kết quả ở cả bốn tệp (đã tìm bằng hai cách: "theo dõi" và "follow").
- `grep -n -i -E "AI.*[Tt]ag|[Tt]ag.*AI" ISH-SR-M05.md ISH-RT-M05.md` → 0 kết quả liên quan đến AI gợi ý Tag.
- `awk 'NR==13,NR==68' ISH-SR-M05.md | grep -n "phải"` → 0 kết quả (xác nhận CL-F05).
- Không có finding nào bị loại ở Bước 6 trong vòng này — cả 4 finding dự kiến đều xác minh được bằng grep như trên.
- Mục đã xem xét nhưng **không** lập finding: DEC-133/ISS-195/QA-254 (log raw output AI) — disposition phân loại "không liên quan" là hợp lý vì nội dung thực sự áp dụng chung Moderation/Embedding/Topic Suggestion, không riêng M05; DEC-095 (embedding model) — chỉ nhắc M05 như ví dụ loại suy ("mirrors is_stale pattern"), không tạo nội dung mới, disposition phân loại đúng.
