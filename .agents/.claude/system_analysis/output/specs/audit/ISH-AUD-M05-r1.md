# Báo cáo audit — ISH-AUD-M05-r1
<!-- [Vietnamese Doc] -->

| Mã báo cáo | ISH-AUD-M05-r1 |
| --- | --- |
| SR được audit | ISH-SR-M05, phiên bản 0.1 (2026-10-04, Bản nháp) |
| Routing | ISH-RT-M05, phiên bản 0.1 (2026-10-04) |
| Vòng | 1 |
| Lượt đã gộp | P1, P2, P3 (ba lượt chạy độc lập, mỗi lượt một ngữ cảnh) |
| Ngày | 2026-10-04 |
| Auditor | Agent Auditor độc lập (lượt MERGE) |
| Kết luận | **Chưa đạt** |

## 1. Tóm tắt

Kết luận **Chưa đạt**: còn 15 DEFECT và 1 CONFLICT mở; `check_sr.py` không còn ERROR hay WARN. Hình thức của SR đạt (nhóm D đạt hết, 135 ca kiểm phủ 92/92 yêu cầu cấp dưới). Lỗi nằm ở ngữ nghĩa: (1) mốc "đăng" trong điểm thưởng bài mới và phá hòa của Trending đọc được hai cách (GAP Cao); (2) hai nguồn đã đóng mâu thuẫn nhau về việc theo dõi Topic có tạo thông báo hay không, và chưa ai hỏi stakeholder (CONFLICT); (3) DEC-145 và QA-011 mới chỉ được đưa vào SR một phần; (4) định nghĩa "Bài viết công khai" rộng hơn DEC-146; (5) có các cặp yêu cầu mâu thuẫn nhau hoặc cấp trên không khớp cấp dưới (003.10/003.11, 005, 010, 012). Không còn mục OWNED nào bị bỏ sót hoàn toàn.

| Lớp \ Mức | Cao | Trung bình | Thấp |
|---|---|---|---|
| DEFECT | 0 | 11 | 4 |
| CONFLICT | 0 | 1 | 0 |
| GAP | 1 | 3 | 0 |
| OBSERVATION | 0 | 0 | 1 |

Tổng: 21 finding, gộp từ 23 finding nháp (P1: 7, P2: 9, P3: 7; hai cặp trùng được gộp lại, xem mục 9).

## 2. Phạm vi và phương pháp

- **Tệp đã đọc:** `ISH-SR-M05.md` v0.1 (555 dòng) và `ISH-RT-M05.md` v0.1, trùng hoàn toàn với `snapshot-ISH-SR-M05-v0.1.md` và `snapshot-ISH-RT-M05-v0.1.md` (`diff -q` không báo khác biệt). Ba lượt đều audit đúng phiên bản 0.1.
- **Tệp lượt đã gộp:** `work/audit-P1-M05-r1.md` (kèm `coverage-M05-r1.md`, `audit-inventory-P1-M05-r1.*`, `check-P1-M05-r1.json`); `work/audit-P2-M05-r1.md` (kèm `check-P2-M05-r1.json`); `work/audit-P3-M05-r1.md` (kèm `audit-tests-M05-r1.md` gồm 98 ca và bảng quét khung hành vi, `audit-inventory-P3-M05-r1.*`, `check-P3-M05-r1.json`).
- **Nguồn các lượt đã đọc:** DRAFT `iShare_modules.md` §3.1–§3.4 và các mục liên quan (§2.4, §4.5, §7.1–§7.4, §8.1, §9.5, §11.2, §11.5); `iShare_specs_general.md` §3, §6; `iShare_dev_priority.md` §2–§3; registers đọc ngày 2026-10-04 (`decisions.md`, `qa-log.md`, `issue-queue.md`, `module-registry.md`, `glossary.md`). Đã đọc nguyên văn đủ 76 mục OWNED và 20 mục REFERENCING. Mục KEYWORD được đọc có chủ đích (P1 đọc khoảng 25 mục). Mục CROSS-CUTTING được đọc theo tiêu đề.
- **Script đã chạy ở lượt MERGE:** `inventory.py` → `work/audit-inventory-M05-r1.md/.json` (OWNED 76, REFERENCING 20, KEYWORD 108, CROSS 40, DRAFT 34; tập OWNED trùng hoàn toàn với inventory của P1 và P3). `check_sr.py --inventory … --tests work/tests-M05.md` → `work/check-M05-r1.json`.
- **Tính độc lập:** P1 lập ma trận mong đợi trước khi đọc thân SR/routing. P3 dựng ca kiểm và bảng quét khung trước khi mở SR. Không lượt nào đọc tệp của lượt khác. Người gọi chỉ đưa mã module, vòng, lượt và gốc repo; không nhận tóm tắt nào của Author. Giới hạn nhỏ P3 tự ghi lại: lệnh `head -15` ở bước C0 cho thấy đoạn mục 1 Tổng quan trước khi dựng ca (đoạn này chỉ liệt kê nhóm tính năng).
- **Giới hạn (không kiểm được):**
  - "Stakeholder đã được báo" chỉ kiểm được qua register, không kiểm được trao đổi ngoài register.
  - Chưa có SR của module khác (M03, M06, M07, M10, M13, M14…), nên các hàng R5 chỉ kiểm được nguồn, không kiểm được ID sở hữu.
  - Mục KEYWORD không đọc hết nội dung; phần còn lại chỉ đọc tiêu đề.
  - Ý định của stakeholder ở các GAP (mốc "đăng", quy tắc so tên tiếng Việt, bình luận bị ẩn, lưu nháp không có Topic) không suy được; báo cáo chỉ nêu các lựa chọn.
  - Hành vi cài đặt thực (cửa sổ đếm 10 yêu cầu/phút, chu kỳ tính lại 15–30 phút) thuộc R2, không kiểm.
  - Trạng thái kiểm duyệt của bình luận và bài viết (DEC-031…033, DEC-077, DEC-083) lấy từ register của module khác, chưa có SR để đối chiếu.

## 3. Kết quả kiểm tra tự động

Lệnh của MERGE (từ gốc repo):

```
python3 .agent-instructions/system_analysis/shared/sr-tools/check_sr.py \
  --sr .agents/.claude/system_analysis/output/specs/ISH-SR-M05.md \
  --routing .agents/.claude/system_analysis/output/specs/routing/ISH-RT-M05.md \
  --inventory .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-M05-r1.json \
  --tests .agents/.claude/system_analysis/output/specs/audit/work/tests-M05.md \
  --json .agents/.claude/system_analysis/output/specs/audit/work/check-M05-r1.json
```

**ERROR = 0, WARN = 0, INFO = 19.** Có 12 yêu cầu cấp trên và 92 yêu cầu cấp dưới.

- INFO COV-03 × 17: DEC-047, DEC-049, DEC-050, DEC-051, DEC-052, DEC-140, DEC-141, DEC-147, DEC-150, ISS-207, QA-101, QA-102, QA-104, QA-106, QA-107, QA-268, QA-278. P1 đã kiểm tay ở CL-A10: phần ở SR và phần ở routing không trùng nhau; các chỗ thiếu một phần nằm ở AUD-M05-03 và AUD-M05-04.
- INFO COV-00: OWNED = 76, trong SR = 70, trong routing = 23.
- INFO TST-00: 135 ca cho 92 yêu cầu.

Không có INV-01 (inventory mới), không có COV-01. Ba lượt cũng cho kết quả 0 ERROR, 0 WARN. Script không bắt được lỗi mẫu câu của ISH-M05-005; lỗi này nằm ở AUD-M05-09.

## 4. Ma trận độ phủ nguồn → yêu cầu

Đầy đủ ở `work/coverage-M05-r1.md`: phần A là mong đợi, lập trước khi đọc SR; phần B là thực tế; phần C là các chỗ lệch nguồn. Bảng dưới liệt kê mọi nhóm mục OWNED, và ghi riêng các mục REFERENCING/KEYWORD có finding. Ký hiệu: `S:` là dòng của `ISH-SR-M05.md`, `R:` là dòng của `ISH-RT-M05.md`.

| Nguồn | Mong đợi (Auditor) | Thực tế (SR / routing) | Kết quả | AUD |
|---|---|---|---|---|
| DRAFT §3.1 | SR danh mục Topic (theo DEC-048) | Lý do 5.3; 001.1 (S:439) | Khớp | — |
| DRAFT §3.2 | SR 0–5 Tag theo DEC-143 + dấu vết lệch | 006 (DRAFT §3.2 + DEC-143); R6 (R:79) | Khớp | — |
| DRAFT §3.3 | R5 Lớp/Khối (M03, M02) | R5 (R:65), không ghi DRAFT §3.3; R6 (R:80) | Khớp (dấu vết yếu) | — |
| DRAFT §3.4 | SR 1–3 Topic + R5 Lớp/Khối | 002; R6 (R:79); R5 (R:65) | Khớp | — |
| DRAFT §4.5 | SR theo dõi Topic + R7 Tag + R5 thông báo | 007; R7 (R:87) | Khớp | — |
| DRAFT §7.2 | SR theo DEC-052 + dấu vết lệch DRAFT | 008 chỉ ghi register (S:503) | Lệch nguồn, thiếu dấu vết | 18 |
| DRAFT §7.1, §7.3, §7.4, §8.1, §9.5 | R5 (M14, M06, M07, M15) | R6 (R:80), R5 (R:56–58, R:64), disposition | Khớp | — |
| DRAFT §11.2, §11.5 | SR gợi ý Topic, phản hồi + R6 gợi ý Tag | 003, 005, 009; R6 (R:78); R5 M13 (R:69) | Khớp | — |
| dev_priority §3; module-registry M05 | Mốc ở 5.1; R1 | 5.1 (S:99–112); R1 (R:14) | Khớp | — |
| DEC-047, ISS-079, QA-101 | SR + R5 lọc/duyệt | 001, 006.1, 006.8; R3, R5, R7 | Khớp | — |
| DEC-048, DEC-140, ISS-080, ISS-207, QA-102, QA-267 | SR 11 Topic phẳng + R6 | 001.1, 001.2, 001.4; R4; R6 (R:75) | Khớp | 07 (lời văn cấp trên) |
| DEC-049, DEC-143, ISS-083, ISS-211, QA-271 | SR 1–3 Topic + từ chối | 002.4…002.8 | Khớp | 16 (bản nháp) |
| DEC-049, ISS-084, QA-107 (Topic) | SR đổi tên, gộp, cấm xóa | 010, 010.4, 011; R1 | Khớp | 12 (cấp trên) |
| DEC-050, DEC-147, DEC-148, ISS-081, ISS-218…220, QA-103, QA-278…280 | SR mỗi nhánh gợi ý + R3 | 002.3, 003.1…003.14, 004.1; R3, R4, R6 | Khớp | 08 |
| QA-104, QA-017 (phản hồi) | SR + R1/R5 M13 | 005.1…005.3; R1, R5 | Khớp | 09, 10 |
| DEC-149, DEC-132, ISS-221, QA-281; DEC-152 (1), ISS-225, QA-285 | SR | 004.5…004.7; R3, R5, R6 | Khớp | — |
| DEC-051, DEC-143, ISS-082, ISS-212, QA-105, QA-272; DEC-150 (2), DEC-152 (2), ISS-223, ISS-226, QA-283, QA-286 | SR giới hạn Tag | 006.2…006.15; R1 | Khớp | — |
| DEC-051 (khủng hoảng), QA-107 (Tag); DEC-150 (1), ISS-222, QA-282 | SR vô hiệu hóa, mở lại Tag + R5 | 012.1…012.11; R1, R3, R5 | Khớp | 11, 12 |
| DEC-144, ISS-213, QA-273 | SR quyền đổi Topic/Tag | 002.6, 002.9, 006.11, 006.12, 009 | Khớp | 11 |
| DEC-145, ISS-214, ISS-215, QA-274, QA-275 | SR: Topic nguồn không chọn, gợi ý, xếp Trending, theo dõi được; chuyển người theo dõi | 011.2…011.4; chọn (002.2) và gợi ý (004.5) có; Trending và theo dõi không có | Thiếu một phần | 03 |
| DEC-052, DEC-142, ISS-082, ISS-210, QA-106, QA-270 | SR công thức + R2 chu kỳ + R5 M14 | 008, 008.1, 008.2, 008.8; R2, R4, R5 | Khớp | 01 (mốc "đăng") |
| DEC-146, ISS-216, ISS-217, QA-276, QA-277 | SR | 008.3…008.7 | Khớp | 06, 14, 20 |
| DEC-153, ISS-227, QA-287 | SR | 008.9…008.12 | Khớp | 15 |
| DEC-141, ISS-208, QA-268 | SR theo dõi + R3 + R5 M07 | 007.1…007.4; R3, R5 (R:64), R7 | Khớp | 19 |
| ISS-209, QA-269; QA-108 | R6/R7 | R6 (R:78), R7 (R:86, R:88) | Khớp | — |
| DEC-151, ISS-224, QA-284 | 5.1 + R4 + R5 | 5.1; R4 (R:49); R5 (R:59) | Khớp | — |
| REF: DEC-008, DEC-093, DEC-099, DEC-090, DEC-124…126, DEC-132 | SR hoặc R5 | 004, 007.5; R2, R5 | Khớp | — |
| KEYWORD QA-011 | SR/R5: Guest xem Topic, Tag, Khối lớp; xem phân loại trên bài | Topic → 001.3; Khối lớp → R5; Tag và phân loại trên bài không có chỗ đi | Thiếu một phần | 04 |
| KEYWORD QA-235, ISS-175 | SR/OP (xếp hạng Topic/Tag thuộc M05) + R5 M14 | Toàn bộ → R5 M14 "hiển thị" (R:62) | Sai chỗ | 05 |
| KEYWORD QA-043, ISS-051 ↔ DEC-065 | CONFLICT hỏi stakeholder | Ghi chú ở R5 (R:64), chưa hỏi | Lệch nguồn | 02 |
| KEYWORD (30 mục, ví dụ ISS-168, QA-225) | Mỗi mục một dòng disposition | Một câu gộp (disposition:69) | Thiếu phân loại | 17 |
| glossary.md:14, :29; DEC-125 | Register nhất quán | Văn bản cũ chưa đánh dấu | Lệch trong register | 21 |
| Các KEYWORD/CROSS còn lại (DEC-053…060, DEC-096, DEC-127, DEC-133, QA-033, QA-034, QA-231, QA-236, QA-237, QA-243, OPEN-006, OPEN-008…) | R5/R6/không liên quan | R5, R6, R1 hoặc disposition | Khớp | — |

## 5. Phát hiện

### AUD-M05-01 — "Bài viết được đăng trong 7 ngày" (điểm thưởng bài mới và tiêu chí phá hòa) đọc được hai cách

| Lớp | GAP | Mức | Cao | Checklist | CL-A11 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.1, 008.2, 008.11, 008.12 (`ISH-SR-M05.md:317`, `:318`, `:327`, `:328`).
- **Bằng chứng trong SR:**
  - "cộng thêm số bài viết được tính của Topic đó được đăng trong 7 ngày gần nhất" (`ISH-SR-M05.md:317`)
  - 2.1 phân biệt "gửi" với "xuất bản": "Thao tác của tác giả chuyển bài viết từ bản nháp sang chờ xuất bản." (`ISH-SR-M05.md:36`). Từ "đăng" không có định nghĩa.
- **Bằng chứng trong nguồn:**
  - "the "+1" per post is a new-post bonus, given only to posts created within the window" (`decisions.md:778`, DEC-142)
  - "chỉ cộng cho bài được đăng trong 7 ngày" (`qa-log.md:1005`, QA-270)
  - "Ties are broken by the number of counted posts created within the rolling 7-day window" (`decisions.md:822`, DEC-153)
  - "- PENDING: submitted, under AI scan or mod review" (`decisions.md:195`, DEC-031)
  - "0.5≤score<0.9 → hold for mod review (Post stays PENDING" (`decisions.md:565`, DEC-098)
- **Vấn đề:** Một bài viết có ba mốc có thể cách nhau nhiều ngày: tạo bản nháp, gửi, và trở thành công khai sau khi quét AI hoặc Mod duyệt. Nguồn dùng "created" và "được đăng" mà không nói là mốc nào. Ca A-073: bài gửi lúc T−8 ngày, chờ Mod duyệt, công khai lúc T−6 ngày, chưa có tương tác. Tính theo mốc gửi hoặc mốc tạo, bài đóng góp 0 điểm; tính theo mốc công khai, bài đóng góp 1 điểm. Kết quả phá hòa ở 008.11 và 008.12 cũng đổi theo. SR chép nguyên chữ "được đăng", nên giữ nguyên chỗ mơ hồ. Không có ISS/QA/DEC hay OP nào về mốc này.
- **Hệ quả nếu không sửa:** Hai cách cài đặt cho điểm Trending và thứ hạng khác nhau mà người dùng nhìn thấy được; ca kiểm chấp nhận không có một "Then" duy nhất.
- **Hướng xử lý (Author quyết cách viết):** Hỏi stakeholder (mục 6), ghi register, rồi định nghĩa mốc ở 2.1 hoặc viết thẳng vào bốn yêu cầu; thêm ca kiểm cho bài chờ duyệt vắt qua ranh giới cửa sổ.
- **Trạng thái:** Mở.

### AUD-M05-02 — Theo dõi Topic có tạo thông báo hay không: QA-043 và DEC-141 mâu thuẫn với danh sách sự kiện của DEC-065, chưa được hỏi

| Lớp | CONFLICT | Mức | Trung bình | Checklist | CL-A09 |
|---|---|---|---|---|---|

- **Vị trí:** routing R5 (`ISH-RT-M05.md:64`); 2.1 "Theo dõi Topic" (`ISH-SR-M05.md:52`); Lý do 5.9 (`ISH-SR-M05.md:288`).
- **Bằng chứng trong nguồn:**
  - "Topic (nhận noti khi có post mới trong topic)" (`qa-log.md:521`, QA-043)
  - "Notification delivery on new posts in a followed Topic remains M07's responsibility" (`decisions.md:774`, DEC-141)
  - "### DEC-065: Notification event list + channel" (`decisions.md:375`): bảng sự kiện không có sự kiện "bài mới trong Topic đang theo dõi". QA-123 gọi bảng này là "Full notification event list?" (`qa-log.md:774`).
- **Bằng chứng trong SR/routing:**
  - "lưu ý DEC-065 chưa liệt kê sự kiện này" (`ISH-RT-M05.md:64`)
  - "muốn nhận cập nhật" (`ISH-SR-M05.md:52`)
  - "Người dùng theo dõi để nhận cập nhật về nội dung hoặc chủ đề mình quan tâm." (`ISH-SR-M05.md:288`)
- **Vấn đề:** Hai nguồn đã đóng cho hai kết luận khác nhau về cùng một vấn đề. Author đã thấy (có ghi chú ở R5) nhưng chưa hỏi stakeholder, trong khi RULES §7.6 yêu cầu xử lý như CONFLICT. Selfcheck ghi CL-A09 `Đạt`.
- **Hệ quả nếu không sửa:** Nếu M07 viết theo DEC-065, người theo dõi Topic không bao giờ nhận thông báo, trái QA-043 và DEC-141; M05 mô tả "nhận cập nhật" mà không module nào thực hiện.
- **Hướng xử lý:** Hỏi stakeholder (mục 6), ghi DEC; sửa 2.1 và Lý do 5.9 nếu câu trả lời là "không".
- **Trạng thái:** Mở.

### AUD-M05-03 — Hệ quả của gộp Topic: Topic nguồn vẫn có thể được xếp Trending và vẫn theo dõi được

| Lớp | DEFECT | Mức | Trung bình | Checklist | CL-A10, CL-B13, CL-B09 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-011.2 (`ISH-SR-M05.md:387`); ISH-M05-008 (`:307`); ISH-M05-007.1 (`:294`); 2.1 "Danh mục Topic" (`:28`); 5.2 (`:120`).
- **Bằng chứng trong nguồn:** "it can no longer be selected, suggested, ranked in Trending or followed" (`decisions.md:790`, DEC-145).
- **Bằng chứng trong SR:**
  - "hệ thống phải loại Topic nguồn khỏi danh mục Topic" (`ISH-SR-M05.md:387`)
  - "Tập Topic một tầng mà hệ thống cho phép chọn cho bài viết" (`ISH-SR-M05.md:28`)
  - "Hệ thống phải xếp hạng các Topic và các Tag theo điểm Trending tính trên 7 ngày gần nhất" (`ISH-SR-M05.md:307`)
  - "yêu cầu theo dõi một Topic chưa theo dõi" (`ISH-SR-M05.md:294`)
  - "| Topic trong danh mục Topic | Topic được gộp làm Topic nguồn |" (`ISH-SR-M05.md:120`): Topic nguồn vẫn tồn tại ở trạng thái "đã loại khỏi danh mục".
- **Vấn đề:** DEC-145 nêu bốn hệ quả cho Topic nguồn. Hai hệ quả đã có yêu cầu: không chọn được (002.2) và không gợi ý được (004.5). Hai hệ quả còn lại không có yêu cầu nào và cũng không nằm trong routing: không được xếp Trending và không theo dõi được. Vì 2.1 định nghĩa danh mục chỉ là tập Topic "cho phép chọn cho bài viết", ISH-M05-008 và ISH-M05-007.1 vẫn áp dụng cho Topic nguồn. Thiếu cả nhánh từ chối khi người dùng yêu cầu theo dõi Topic nguồn (CL-B09). Ca A-093 và A-094 có kết quả xác định theo nguồn, nhưng SR cho kết quả mơ hồ. Selfcheck ghi CL-A10 `Đạt` (`selfcheck-M05.md:115` suy kết quả từ 011.2).
- **Hệ quả nếu không sửa:** Topic nguồn (điểm 0) có thể vẫn hiện trong bảng Trending, và người dùng vẫn theo dõi được một Topic đã bị gộp.
- **Hướng xử lý (Author quyết cách viết):** Thêm yêu cầu cấp dưới (`Nói thẳng`, DEC-145) cho hai hệ quả này, gồm cả việc từ chối theo dõi; hoặc giới hạn phạm vi của 007 và 008 vào Topic trong danh mục. Cập nhật Phụ lục A và ca kiểm.
- **Trạng thái:** Mở.

### AUD-M05-04 — QA-011 chỉ được đưa một phần: Guest xem danh sách Tag và xem phân loại trên bài viết không có chỗ đi

| Lớp | DEFECT | Mức | Trung bình | Checklist | CL-A10 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-001.3 (`ISH-SR-M05.md:142`); Phụ lục A (`:441`); routing R5 (`ISH-RT-M05.md:65`).
- **Bằng chứng trong nguồn:** "CLAS: Xem danh sách Topic / Tag / Khối lớp" (`qa-log.md:134`); "AI: Xem AI Summary + AI Classification trên post" (`qa-log.md:137`), QA-011.
- **Bằng chứng trong SR/routing:**
  - "kể cả Guest, xem danh sách Topic trong danh mục Topic" (`ISH-SR-M05.md:142`)
  - "| ISH-M05-001.3 | QA-011 | Nói thẳng |" (`ISH-SR-M05.md:441`)
  - "danh sách Khối lớp cho Guest" (`ISH-RT-M05.md:65`)
  - Disposition ghi "AI Classification trên post" … "không còn (DEC-050)" (`disposition-M05.md:73`), nhưng DEC-050 không nói phân loại không còn hiển thị trên bài viết.
- **Vấn đề:** Hai phần của QA-011 không nằm trong SR cũng không nằm trong routing: phần "Tag" và phần "phân loại trên post". Các lần tìm vắng mặt cho kết quả 0 (xem mục 9). ISH-M05-012.1 và 012.5 ("ẩn" và "hiển thị lại" Tag trên bài viết) đang dựa trên một hành vi hiển thị chưa được viết ở đâu.
- **Hệ quả nếu không sửa:** Quyền của Guest xem Tag, và việc hiển thị Topic/Tag đã gắn trên bài viết, không có chủ sở hữu.
- **Hướng xử lý:** Đưa hai phần này vào SR nếu M05 sở hữu; nếu không, đưa vào R5 kèm module sở hữu, hoặc đặt OP loại Đề xuất về chủ sở hữu (RULES §5 mục 2). Sửa lý do trong disposition.
- **Trạng thái:** Mở.

### AUD-M05-05 — QA-235 (không đặt ngưỡng tối thiểu để vào Trending) bị chuyển hết sang M14 dù xếp hạng Topic/Tag thuộc M05

| Lớp | DEFECT | Mức | Trung bình | Checklist | CL-E03 |
|---|---|---|---|---|---|

- **Vị trí:** routing R5 (`ISH-RT-M05.md:62`); ISH-M05-008 (`ISH-SR-M05.md:307`).
- **Bằng chứng trong nguồn:**
  - "QA-235 | ISS-175: Có ngưỡng tối thiểu (min upvote/comment) để vào Trending không?" và "Không đặt ngưỡng cho MS1 — dataset demo nhỏ" (`qa-log.md:939`)
  - "**Trending** (3 sub-views: Post/Topic/Tag)" (`decisions.md:695`, DEC-125)
  - "Topics and Tags are ranked by Trending score, highest first." (`decisions.md:822`, DEC-153)
- **Bằng chứng trong routing:**
  - "Không đặt ngưỡng tối thiểu để vào Trending" … "M14 — chưa có SR, ghi nguồn QA-235, QA-236" (`ISH-RT-M05.md:62`)
  - "QA-235, ISS-175 | Không ngưỡng tối thiểu vào Trending | R5 | M14 (hiển thị)" (`disposition-M05.md:94`)
- **Vấn đề:** Ngưỡng để vào Trending quyết định Topic/Tag nào có mặt trong bảng xếp hạng. Đó là quy tắc xếp hạng, không phải quy tắc hiển thị, và xếp hạng Topic/Tag do M05 sở hữu. QA-235 không giới hạn câu trả lời ở Trending Post. SR không có yêu cầu nào cho phần này, cũng không có OP về chủ sở hữu.
- **Hệ quả nếu không sửa:** Không xác định được Topic/Tag có điểm thấp (kể cả 0) có vào bảng xếp hạng hay không.
- **Hướng xử lý:** Tách hàng routing: phần Trending Post giữ ở R5 M14; phần Topic/Tag đưa vào SR, hoặc đặt OP loại Đề xuất về chủ sở hữu.
- **Trạng thái:** Mở.

### AUD-M05-06 — Định nghĩa "Bài viết công khai" rộng hơn DEC-146: bài đang bị gắn cờ và bài tác giả tự ẩn

| Lớp | DEFECT | Mức | Trung bình | Checklist | CL-A05, CL-B08, CL-C03 |
|---|---|---|---|---|---|

- **Vị trí:** 2.1 (`ISH-SR-M05.md:37`), được dùng ở ISH-M05-008.3 (`:319`).
- **Bằng chứng trong SR:** "Bài viết đã xuất bản và không bị ẩn bởi kiểm duyệt" (`ISH-SR-M05.md:37`); "Hệ thống phải chỉ tính vào điểm Trending các bài viết công khai không thuộc Group Private." (`ISH-SR-M05.md:319`).
- **Bằng chứng trong nguồn:**
  - "Only posts that are currently public (publish_state PUBLISHED and mod_state NORMAL, DEC-033) and not in a Private group count." (`decisions.md:794`, DEC-146)
  - "Visibility rule: publish_state=PUBLISHED AND mod_state=NORMAL" (`decisions.md:211`)
  - "FLAGGED: AI/report flagged, awaiting mod" (`decisions.md:203`)
  - "HIDDEN: author self-hide (reversible)" (`decisions.md:197`)
- **Vấn đề:** Nguồn nêu chính xác điều kiện. Định nghĩa trong SR thì rộng hơn ở hai chỗ:
  - Ca A-091: bài đã xuất bản và đang bị gắn cờ, chờ Mod. Bài này "chưa bị ẩn bởi kiểm duyệt", nên theo SR được tính (5 điểm); theo nguồn đóng góp 0 điểm.
  - Ca A-092: bài tác giả tự ẩn. "Đã xuất bản" đọc được là "đã từng xuất bản" (5 điểm) hoặc "đang ở trạng thái xuất bản" (0 điểm).
- **Lý do mức:** Mức mặc định của CL-A05 là Cao; cả hai lượt (P2, P3) đề xuất Trung bình, vì ý của yêu cầu đúng, sai lệch chỉ xảy ra ở hai trạng thái biên, và cách sửa đã có sẵn trong nguồn.
- **Hệ quả nếu không sửa:** Bài đang bị báo cáo hoặc bị tác giả tự ẩn vẫn góp điểm Trending, trái DEC-146.
- **Hướng xử lý:** Viết lại định nghĩa theo điều kiện của DEC-146/DEC-033 bằng lời mô tả hành vi, không dùng tên trường; thêm ca kiểm cho bài bị gắn cờ và bài tự ẩn.
- **Trạng thái:** Mở.

### AUD-M05-07 — "các Topic cố định" ở ISH-M05-001 không đo được và trái với việc đổi tên, gộp Topic

| Lớp | DEFECT | Mức | Trung bình | Checklist | CL-B03, CL-C01 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-001 (`ISH-SR-M05.md:130`).
- **Bằng chứng trong SR:**
  - "Hệ thống phải cung cấp một danh mục Topic một tầng gồm các Topic cố định." (`ISH-SR-M05.md:130`)
  - "Khi Mod hoặc Admin đổi tên một Topic, hệ thống phải thay tên của Topic đó bằng tên mới." (`ISH-SR-M05.md:355`)
  - "hệ thống phải loại Topic nguồn khỏi danh mục Topic" (`ISH-SR-M05.md:387`)
- **Bằng chứng trong nguồn:** "it can no longer be selected, suggested, ranked in Trending or followed" (`decisions.md:790`).
- **Vấn đề:** "Cố định" không cho biết điều gì được giữ cố định. Nếu hiểu là tên không đổi, câu này trái với ISH-M05-010 (đổi tên). Nếu hiểu là tập Topic không đổi, câu này trái với ISH-M05-011.2 (sau gộp còn 10 Topic chứ không phải 11).
- **Lý do mức:** Mức Trung bình là mặc định của CL-B03. Mặt CL-C01 không được lấy làm mức, vì các yêu cầu cấp dưới đều đúng nguồn; mâu thuẫn chỉ nằm ở lời văn của câu cấp trên.
- **Hướng xử lý:** Viết câu cấp trên theo ý nguồn (người dùng không thêm được Topic), hoặc bỏ chữ "cố định".
- **Trạng thái:** Mở.

### AUD-M05-08 — ISH-M05-003.11 trái với ISH-M05-003.10 khi gợi ý đã cũ

| Lớp | DEFECT | Mức | Trung bình | Checklist | CL-C01, CL-A05 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-003.10 (`ISH-SR-M05.md:196`), ISH-M05-003.11 (`:197`).
- **Bằng chứng trong SR:** "hệ thống phải đánh dấu gợi ý đó là gợi ý cũ." (`:196`); "Khi tác giả thay đổi tệp đính kèm của bài viết sau khi nhận gợi ý Topic, hệ thống phải giữ gợi ý đó là gợi ý còn mới." (`:197`).
- **Bằng chứng trong nguồn:** "A suggestion becomes stale on any change to the title or the text content; attachment changes do not count." (`decisions.md:802`, DEC-148).
- **Vấn đề:** Nguồn nói thay đổi tệp đính kèm không ảnh hưởng trạng thái gợi ý. SR lại viết "giữ … còn mới" mà không có điều kiện. Trình tự kiểm: nhận gợi ý → sửa tiêu đề (003.10 đánh dấu gợi ý cũ) → thêm tệp đính kèm. Theo 003.11 gợi ý thành "còn mới"; theo 003.10 và theo nguồn, gợi ý vẫn cũ. Hai cách cho kết quả khác nhau ở cảnh báo của 003.12 và ở việc ghi phản hồi (005.1/005.2).
- **Lý do mức:** Mức mặc định của CL-C01 là Cao; hạ một mức vì mâu thuẫn chỉ xảy ra theo một trình tự thao tác và ý của nguồn rõ ràng.
- **Hướng xử lý:** Viết 003.11 theo ý "thay đổi tệp đính kèm không làm đổi trạng thái gợi ý", hoặc thêm điều kiện trạng thái.
- **Trạng thái:** Mở.

### AUD-M05-09 — Câu cấp trên ISH-M05-005 nói ghi phản hồi ở mọi lần gửi bài, trái với 005.2 và 005.3, và sai mẫu câu

| Lớp | DEFECT | Mức | Trung bình | Checklist | CL-C04, CL-B01 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-005 (`ISH-SR-M05.md:232`).
- **Bằng chứng trong SR:**
  - "Hệ thống phải ghi nhận phản hồi gợi ý Topic khi tác giả gửi bài viết." (`:232`)
  - "Trong khi gợi ý Topic của bài viết là gợi ý cũ, khi tác giả gửi bài viết đó, hệ thống phải không ghi nhận phản hồi gợi ý Topic." (`:243`)
  - "Khi tác giả gửi một bài viết chưa từng nhận gợi ý Topic, hệ thống phải không ghi nhận phản hồi gợi ý Topic." (`:244`)
- **Bằng chứng trong nguồn:** "Feedback (AI suggest vs final selection) only recorded when not stale" (`decisions.md:293`, DEC-050).
- **Vấn đề:** Câu cấp trên không có điều kiện, nên ngược với hai yêu cầu cấp dưới (CL-C04). Câu có sự kiện kích hoạt nhưng viết theo mẫu Phổ quát, đặt "khi" ở cuối câu, trái RULES §4.6 (CL-B01). Script không bắt được lỗi này.
- **Hệ quả nếu không sửa:** Ca kiểm viết từ câu cấp trên cho kết quả ngược với ISH-M05-005.3.
- **Hướng xử lý:** Viết lại theo mẫu `Khi …`, kèm điều kiện "có gợi ý còn mới".
- **Trạng thái:** Mở.

### AUD-M05-10 — ISH-M05-005.1 "từ gợi ý Topic gần nhất" được ghi `Nói thẳng` nhưng nguồn không nêu

| Lớp | DEFECT | Lớp phụ | GAP | Mức | Trung bình | Checklist | CL-A05, CL-A06 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-005.1 (`ISH-SR-M05.md:242`); Phụ lục A (`:477`).
- **Bằng chứng trong SR:** "hệ thống phải ghi nhận phản hồi gợi ý Topic từ gợi ý Topic gần nhất cùng các Topic tác giả chọn cuối cùng." (`:242`); "gợi ý gần nhất vì gợi ý trước đó đã bị thay thế (DEC-148)" (`:477`).
- **Bằng chứng trong nguồn:** "Feedback (AI suggest vs final selection) only recorded when not stale" (`decisions.md:293`); "Suggested topics replace the current selection, including topics the user ticked manually before requesting the suggestion." (`decisions.md:802`). DEC-148 nói gợi ý mới thay *lựa chọn Topic*, không nói phản hồi được lấy từ lần gợi ý nào.
- **Vấn đề:** Khi tác giả nhận nhiều gợi ý còn mới cho cùng một bài, nguồn không nói phản hồi ghi theo lần nào. "Gần nhất" là cách đọc tự nhiên nhưng không phải hệ quả bắt buộc của nguồn, vậy mà dòng truy vết ghi `Nói thẳng`. Đã tìm trong register, không có kết quả (mục 9).
- **Lý do mức:** Mức mặc định của CL-A05 là Cao; hạ một mức vì đây là cách đọc tự nhiên nhất và hệ quả chỉ nằm ở dữ liệu đánh giá AI.
- **Hướng xử lý:** Đổi sang `Suy ra` kèm phép suy luận nếu chứng minh được đây là hệ quả bắt buộc; nếu không, hỏi stakeholder hoặc đặt OP (mục 6).
- **Trạng thái:** Mở.

### AUD-M05-11 — Cơ sở `Nói thẳng` cho phần từ chối mà nguồn chỉ nói về Mod/Admin (ISH-M05-006.12, 012.9, 012.10, 012.11)

| Lớp | DEFECT | Mức | Trung bình | Checklist | CL-A05 |
|---|---|---|---|---|---|

- **Vị trí:** `ISH-SR-M05.md:273` / `:492`; `:416` / `:539`; `:417` / `:540`; `:418` / `:541`.
- **Bằng chứng trong SR:**
  - "Khi một người dùng khác tác giả của bài viết yêu cầu thay đổi Tag của bài viết đó, hệ thống phải từ chối yêu cầu đó." (`:273`), dòng truy vết "| ISH-M05-006.12 | DEC-144, QA-273 | Nói thẳng | Chỉ tác giả đổi Tag; Mod/Admin không đổi Tag của bài |" (`:492`)
  - "Khi người dùng yêu cầu đổi tên một Tag, hệ thống phải từ chối yêu cầu đó." (`:416`), truy vết ghi "Tag không có thao tác sửa cho người dùng nào" (`:539`)
  - "| ISH-M05-012.10 | DEC-051 | Nói thẳng |" (`:540`)
  - "| ISH-M05-012.11 | DEC-051, QA-107 | Nói thẳng |" (`:541`)
- **Bằng chứng trong nguồn:** "Fully free — mod/admin do NOT edit/merge/delete under normal conditions" (`decisions.md:302`); "A Mod or Admin does not change a post's Tags" (`decisions.md:786`).
- **Vấn đề:** Nguồn chỉ nói về Mod/Admin. Phần áp dụng cho Guest và User là suy ra theo dạng "chỉ X mới được làm Y", nên cơ sở đúng là `Suy ra`. Chính SR đã ghi như vậy cho yêu cầu cùng dạng: "| ISH-M05-009.2 | DEC-144 | Suy ra |" (`:518`).
- **Lý do mức:** Mức mặc định của CL-A05 là Cao; hạ một mức vì hành vi từ chối là phương án an toàn, chỉ cột Cơ sở bị ghi sai.
- **Hướng xử lý:** Đổi bốn dòng sang `Suy ra` kèm phép suy luận, hoặc tách phần Mod/Admin (`Nói thẳng`) khỏi phần Guest/User (`Suy ra`).
- **Trạng thái:** Mở.

### AUD-M05-12 — Yêu cầu cấp dưới vượt ra ngoài câu cấp trên (ISH-M05-010.4; ISH-M05-012.9 đến 012.11)

| Lớp | DEFECT | Mức | Trung bình | Checklist | CL-C04 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-010 (`:355`) với 010.4 (`:368`); ISH-M05-012 (`:398`) với 012.9…012.11 (`:416`–`:418`).
- **Bằng chứng trong SR:**
  - "Khi Mod hoặc Admin đổi tên một Topic, hệ thống phải thay tên của Topic đó bằng tên mới." (`:355`)
  - "Khi người dùng yêu cầu xóa một Topic, hệ thống phải từ chối yêu cầu đó." (`:368`)
  - "Hệ thống phải cho phép Mod và Admin thay đổi trạng thái hoạt động của một Tag." (`:398`)
  - "Khi người dùng yêu cầu gộp hai Tag" (`:417`)
- **Vấn đề:** Câu cấp trên chỉ nói về đổi tên Topic, hoặc đổi trạng thái hoạt động của Tag. Các yêu cầu cấp dưới lại thêm lệnh cấm xóa Topic, cấm đổi tên, gộp, xóa Tag. Các hành vi này có nguồn, nhưng cấp trên không bao quát.
- **Hướng xử lý:** Mở rộng câu cấp trên, hoặc chuyển các lệnh cấm sang tính năng có câu cấp trên phù hợp. Cách mở rộng câu cấp trên không làm đổi khung 12 tính năng đã duyệt ở DEC-151.
- **Trạng thái:** Mở.

### AUD-M05-13 — Ca kiểm của Author thiếu loại ca "thử chuyển từ trạng thái không cho phép"

| Lớp | DEFECT | Mức | Trung bình | Checklist | CL-B12 |
|---|---|---|---|---|---|

- **Vị trí:** `work/tests-M05.md` (các ca cho ISH-M05-011 và 012); bảng 5.2 (`ISH-SR-M05.md:118`, `:120`).
- **Bằng chứng:** "| Chuyển trạng thái | Chuyển hợp lệ; thử từ trạng thái không cho phép |" (`SR-DOCUMENT-RULES.md:503`); "| Tag hoạt động | Mod hoặc Admin vô hiệu hóa Tag | Tag bị vô hiệu hóa | ISH-M05-012.1 |" (`ISH-SR-M05.md:118`). Trong `tests-M05.md`, các ca có "bị vô hiệu hóa" chỉ là T-120, T-121 và T-124, không có ca nào chuyển từ trạng thái không cho phép.
- **Vấn đề:** Thiếu một loại ca bắt buộc theo §11.3. Thiếu loại ca này cũng che mất một câu hỏi có hệ quả: gộp vào một Topic đích đã bị loại khỏi danh mục, hoặc vô hiệu hóa một Tag đang bị vô hiệu hóa. Selfcheck ghi CL-B12 `Đạt`.
- **Hướng xử lý:** Thêm ca cho từng chuyển trạng thái không hợp lệ ở 5.2. Ca nào không viết được "Then" thì ghi vào "Giả định cần thêm" và hỏi stakeholder hoặc đặt OP.
- **Trạng thái:** Mở.

### AUD-M05-14 — Bình luận bị ẩn bởi kiểm duyệt có được tính vào điểm Trending không

| Lớp | GAP | Mức | Trung bình | Checklist | CL-A11 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.5, 008.7 (`ISH-SR-M05.md:321`, `:323`).
- **Bằng chứng trong SR:** "Hệ thống phải không đếm bình luận đã bị xóa khi tính điểm Trending." (`:323`).
- **Bằng chứng trong nguồn:**
  - "only interactions that still exist count (retracted upvotes and deleted comments are not counted)" (`decisions.md:794`)
  - "Comment needs a `mod_state` field similar to Post's (NORMAL | HIDDEN)" (`decisions.md:490`)
  - "- If AI flags → comment auto-hidden (author only sees it) + pushed into report queue for mod review" (`decisions.md:451`)
- **Vấn đề:** Bình luận bị ẩn vẫn "còn tồn tại" nhưng không công khai. Ca A-074: bài P1 có 3 bình luận trong cửa sổ, 1 bình luận bị ẩn. Nếu bình luận còn tồn tại thì được tính, P1 = 12 điểm; nếu chỉ tính bình luận công khai, P1 = 11 điểm.
- **Lý do mức:** Mức mặc định của CL-A11 ở công thức là Cao; hạ một mức vì chỉ ảnh hưởng trường hợp biên và nguồn đã có nguyên tắc chung "còn tồn tại".
- **Hướng xử lý:** Hỏi stakeholder (mục 6), rồi thêm một yêu cầu cấp dưới.
- **Trạng thái:** Mở.

### AUD-M05-15 — "Thứ tự chữ cái từ A đến Z" với tên tiếng Việt cho hai kết quả khác nhau

| Lớp | GAP | Mức | Trung bình | Checklist | CL-A11 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.11, 008.12 (`ISH-SR-M05.md:327`, `:328`).
- **Bằng chứng:** "rồi đến tên theo thứ tự chữ cái từ A đến Z" (`ISH-SR-M05.md:327`, `:328`); "then by name in alphabetical order (A→Z)" (`decisions.md:822`); "Khoa học tự nhiên (Lý/Hóa/Sinh)" (`decisions.md:281`). Ca của Author dùng tên không lộ khác biệt: '"Ngữ văn" xếp trước "Tin học" (N trước T)' (`tests-M05.md:142`).
- **Vấn đề:** Ca A-077: hai Topic "Khác" và "Khoa học tự nhiên" bằng điểm và bằng số bài. Theo bảng chữ cái tiếng Việt, "Khác" xếp trước; theo mã ký tự ("o" đứng trước "á"), "Khoa học tự nhiên" xếp trước. Với Tag, "đ" cũng xếp khác nhau giữa hai cách.
- **Hướng xử lý:** Hỏi stakeholder (mục 6), rồi nêu quy tắc so tên trong yêu cầu hoặc ở 2.1.
- **Trạng thái:** Mở.

### AUD-M05-16 — Tối thiểu 1 Topic áp dụng cả khi lưu bản nháp hay chỉ khi gửi; ca kiểm của Author đã ngầm chọn

| Lớp | GAP | Lớp phụ | DEFECT | Mức | Trung bình | Checklist | CL-A11, CL-F04, CL-B13 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-002.4, 002.5, 002.6 (`ISH-SR-M05.md:164`–`:166`); `tests-M05.md:20` (T-011).
- **Bằng chứng trong SR và ca kiểm:**
  - "Hệ thống phải yêu cầu mỗi bài viết có tối thiểu 1 Topic." (`:164`)
  - "Khi tác giả gửi một bài viết không có Topic nào, hệ thống phải từ chối việc gửi bài viết đó." (`:165`)
  - "Khi người dùng lưu một thay đổi làm bài viết không còn Topic nào" (`:166`)
  - "Bài viết nháp của User A có 0 Topic" (`tests-M05.md:20`)
- **Bằng chứng trong nguồn:** "- Min 1, max 3 topics/post (mandatory)" (`decisions.md:284`); "- DRAFT: composing, not submitted" (`decisions.md:194`).
- **Vấn đề:** Nguồn không nói ràng buộc "mandatory" áp dụng từ lúc lưu nháp hay từ lúc gửi. Ca A-006 (lưu nháp chưa có Topic) cho hai kết quả: từ chối hoặc chấp nhận. 002.4 ở dạng phổ quát (mọi bài viết, kể cả nháp), nhưng 002.5 chỉ từ chối khi gửi, nên SR đọc được cả hai cách. Ca T-011 đã ngầm chọn "được lưu nháp không có Topic" mà cột "Giả định cần thêm" ghi `—`. Đây là lớp phụ DEFECT, CL-F04.
- **Lý do mức:** CL-F04 mặc định Cao; hạ một mức vì lựa chọn ngầm chỉ nằm ở điều kiện đầu của ca kiểm, câu SR chưa chọn.
- **Hướng xử lý:** Hỏi stakeholder (mục 6), viết lại 002.4 theo câu trả lời, sửa T-011 nếu cần.
- **Trạng thái:** Mở.

### AUD-M05-17 — Disposition không có dòng riêng cho các mục KEYWORD không nằm ở SR hay routing

| Lớp | DEFECT | Mức | Thấp | Checklist | CL-A03 |
|---|---|---|---|---|---|

- **Vị trí:** `work/disposition-M05.md:69`.
- **Bằng chứng:** "các mục KEYWORD còn lại khớp từ khóa chung" (`disposition-M05.md:69`). Mục lấy mẫu: ISS-168 "M14 cần những tab/view nào cho Feed?" (`issue-queue.md:258`) và QA-225 (`qa-log.md:929`) không có trong disposition, SR hay routing.
- **Vấn đề:** RULES §7.7 yêu cầu mỗi mục không liên quan có một dòng riêng. Có 30 mục KEYWORD không có chỗ nào ghi: DEC-066, DEC-070, DEC-097, DEC-098, ISS-101, ISS-126, ISS-168, ISS-173, ISS-177, ISS-181, ISS-190, QA-004…007, QA-012, QA-022, QA-112, QA-149, QA-153, QA-194, QA-203, QA-211, QA-225, QA-232…234, QA-244, QA-249, QA-262.
- **Lý do mức:** CL-A03 mặc định Trung bình; hạ một mức vì các mục lấy mẫu đều thuộc module khác, không thấy hành vi M05 nào bị sót.
- **Hướng xử lý:** Thêm một dòng cho mỗi mục: ID và lý do một câu.
- **Trạng thái:** Mở.

### AUD-M05-18 — DRAFT §7.2 (tín hiệu Trending) lệch DEC-052 mà không có dấu vết

| Lớp | DEFECT | Lớp phụ | OBSERVATION | Mức | Thấp | Checklist | CL-A08 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** Phụ lục A, ISH-M05-008 (`ISH-SR-M05.md:503`).
- **Bằng chứng:**
  - DRAFT: "### 7.2 Trending / Popular" (`iShare_modules.md:333`), "- Views" (`:337`), "- Bookmarks" (`:340`)
  - DEC-052: "Score: Σ(1 + upvotes×2 + comments×1) across all posts in window" (`decisions.md:308`)
  - SR: "| ISH-M05-008 | DEC-052, DEC-142, QA-106, ISS-082, ISS-210, QA-270 | Nói thẳng | |" (`ISH-SR-M05.md:503`)
- **Vấn đề:** SR viết theo register (đúng §7.5), nhưng cột Nguồn không ghi DRAFT §7.2 và không có dấu vết đã báo stakeholder việc bỏ Views và Bookmarks khỏi công thức.
- **Hướng xử lý:** Thêm DRAFT §7.2 vào cột Nguồn; báo stakeholder phần OBSERVATION (mục 6).
- **Trạng thái:** Mở.

### AUD-M05-19 — Mục 5.2 thiếu trạng thái theo dõi Topic

| Lớp | DEFECT | Mức | Thấp | Checklist | CL-C05 |
|---|---|---|---|---|---|

- **Vị trí:** 5.2 (`ISH-SR-M05.md:116`–`:122`); ISH-M05-007.1…007.3 (`:294`–`:296`).
- **Bằng chứng:** "hệ thống phải ghi nhận người dùng đó đang theo dõi Topic đó." (`:294`); "hệ thống phải ghi nhận người dùng đó không còn theo dõi Topic đó." (`:295`); "trạng thái đang theo dõi hay chưa theo dõi của người dùng đó với mỗi Topic" (`:296`). Bảng 5.2 chỉ có các hàng cho Tag, Topic gộp và trạng thái gợi ý, không có hàng nào về theo dõi.
- **Vấn đề:** Thân tài liệu gọi theo dõi là một trạng thái, có hai chuyển trạng thái (007.1, 007.2) và một chuyển do gộp Topic (011.3). Bảng 5.2 không có các chuyển này.
- **Lý do mức:** CL-C05 mặc định Trung bình; hạ một mức vì hành vi đã được quy định đủ ở các yêu cầu, chỉ thiếu ở bảng tổng hợp.
- **Hướng xử lý:** Thêm các hàng chuyển trạng thái theo dõi, trỏ tới ID tương ứng.
- **Trạng thái:** Mở.

### AUD-M05-20 — Thuật ngữ chưa khớp 2.1: "bài viết được tính" chưa định nghĩa; "Upvote" chỉ định nghĩa cho bài viết

| Lớp | DEFECT | Mức | Thấp | Checklist | CL-C03 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.1, 008.2, 008.11, 008.12 (`:317`, `:318`, `:327`, `:328`); 2.1 "Upvote" (`:53`); ISH-M05-008.4 (`:320`).
- **Bằng chứng:**
  - "trên mọi bài viết được tính của Topic đó" (`:317`)
  - "| Upvote | Lượt đánh giá tích cực của người dùng cho một bài viết. |" (`:53`)
  - "không đếm upvote vào bình luận của bài viết" (`:320`)
  - Nguồn: "= upvotes on the post itself (comment upvotes excluded)" (`decisions.md:794`)
- **Vấn đề:** "Bài viết được tính" dùng ở bốn yêu cầu nhưng không có trong 2.1. Định nghĩa Upvote chỉ nói về bài viết, trong khi 008.4 nói về upvote vào bình luận.
- **Hướng xử lý:** Thêm thuật ngữ "bài viết được tính" vào 2.1; mở rộng định nghĩa Upvote cho cả bình luận, hoặc đổi cách gọi ở 008.4.
- **Trạng thái:** Mở.

### AUD-M05-21 — Văn bản cũ trong register chưa được đánh dấu theo quyết định muộn hơn

| Lớp | OBSERVATION | Mức | Thấp | Checklist | CL-A09 |
|---|---|---|---|---|---|

- **Vị trí:** Không nằm trong SR; SR đã viết theo quyết định muộn hơn.
- **Bằng chứng:**
  - "List to be finalized in BA." (`glossary.md:14`), trong khi DEC-048 ghi "Topic list (11, final)" (`decisions.md:280`)
  - "Suggests Topic and Tags for a Post automatically. User/Moderator reviews before publish." (`glossary.md:29`), trong khi DEC-144 ghi "A Mod or Admin does not change a post's Tags" (`decisions.md:786`)
  - DEC-125: "from Follow targets established in M07 — User/Topic/Post" (`decisions.md:695`), trong khi DEC-141 ghi "M05 (Topic & Tag) owns the Follow/Unfollow behaviour for Topic" (`decisions.md:774`)
- **Vấn đề:** Các câu cũ không mang nhãn `[Amended]`. Người viết SR của M07, M13 hay M14 có thể trích nhầm.
- **Hướng xử lý:** Stakeholder quyết (mục 6).
- **Trạng thái:** Mở.

## 6. Cần stakeholder quyết

Xếp vấn đề chặn trước. Các DEFECT cơ học (AUD-M05-03…09, 11…13, 17, 19, 20) không nằm ở đây; Author sửa thẳng.

**1.**
Vấn đề: Điểm thưởng "+1 bài mới" và tiêu chí phá hòa của Trending Topic/Tag tính theo mốc nào của bài viết?
Nguồn: DEC-142 (`decisions.md:778`) "given only to posts created within the window"; QA-270 (`qa-log.md:1005`) "chỉ cộng cho bài được đăng trong 7 ngày".
Lựa chọn: A) Mốc bài trở thành công khai lần đầu — hệ quả: bài chờ Mod duyệt lâu vẫn được thưởng khi lên; khớp DEC-146.   B) Mốc tác giả gửi bài — hệ quả: bài chờ duyệt quá 7 ngày không bao giờ được thưởng.   C) Mốc tạo bản nháp — hệ quả: bài soạn nháp lâu không được thưởng dù vừa lên.
Đề xuất: A, vì DEC-146 chỉ tính bài đang công khai, nên "bài mới" tính từ lúc người khác thấy được bài là tự nhiên nhất.
Liên quan: AUD-M05-01

**2.**
Vấn đề: Theo dõi một Topic có tạo thông báo in-app khi có bài mới trong Topic đó không?
Nguồn: QA-043 (`qa-log.md:521`) "Topic (nhận noti khi có post mới trong topic)"; DEC-141 (`decisions.md:774`); bảng sự kiện của DEC-065 (`decisions.md:375`) không có sự kiện này.
Lựa chọn: A) Có — thêm sự kiện vào DEC-065 (M07) — hệ quả: M07 cần quy tắc gộp hoặc giới hạn thông báo cho Topic đông bài.   B) Không — theo dõi Topic chỉ ảnh hưởng tab Following (M14) — hệ quả: sửa 2.1 và Lý do 5.9 của SR M05; QA-043 bị thay.
Đề xuất: A, vì DEC-141 là quyết định muộn nhất và khẳng định lại việc thông báo; cần một DEC sửa DEC-065.
Liên quan: AUD-M05-02

**3.**
Vấn đề: Bài viết ở trạng thái bản nháp có được lưu khi chưa có Topic nào không?
Nguồn: DEC-049 (`decisions.md:284`) "Min 1, max 3 topics/post (mandatory)"; DEC-031 (`decisions.md:194`) "DRAFT: composing, not submitted".
Lựa chọn: A) Được — tối thiểu 1 Topic chỉ kiểm khi gửi và khi sửa bài đã gửi — hệ quả: soạn nháp tự do, lỗi chỉ hiện lúc gửi.   B) Không — hệ quả: phải chọn Topic trước khi lưu nháp lần đầu.
Đề xuất: A, vì bản nháp là "composing, not submitted" và 002.5 đã chặn ở thao tác gửi.
Liên quan: AUD-M05-16

**4.**
Vấn đề: Bình luận đang bị ẩn bởi kiểm duyệt (AI hoặc Mod) có được đếm vào điểm Trending Topic/Tag không?
Nguồn: DEC-146 (`decisions.md:794`) "only interactions that still exist count (… deleted comments are not counted)"; DEC-083 (`decisions.md:490`): bình luận có trạng thái NORMAL | HIDDEN.
Lựa chọn: A) Không đếm — hệ quả: nhất quán với việc chỉ tính bài công khai; điểm tăng lại khi bình luận được khôi phục.   B) Đếm mọi bình luận chưa xóa — hệ quả: nội dung vi phạm vẫn góp điểm.
Đề xuất: A, vì DEC-146 chỉ tính nội dung đang công khai ở cấp bài viết.
Liên quan: AUD-M05-14

**5.**
Vấn đề: Khi phá hòa bằng tên A→Z, so tên tiếng Việt theo quy tắc nào?
Nguồn: DEC-153 (`decisions.md:822`) "then by name in alphabetical order (A→Z)".
Lựa chọn: A) Theo bảng chữ cái tiếng Việt (a ă â b c d đ e ê …) — hệ quả: "Khác" xếp trước "Khoa học tự nhiên"; đúng trực giác người dùng.   B) Theo mã ký tự — hệ quả: chữ có dấu và chữ "đ" xếp sau mọi chữ không dấu.
Đề xuất: A, vì người dùng và tên Topic đều là tiếng Việt (DEC-127, DEC-128 chỉ có locale `vi`).
Liên quan: AUD-M05-15

**6.** (Chỉ cần hỏi nếu Author không chứng minh được "gần nhất" là `Suy ra` hợp lệ.)
Vấn đề: Tác giả nhận nhiều gợi ý Topic còn mới cho cùng một bài thì phản hồi ghi theo lần gợi ý nào?
Nguồn: DEC-050 (`decisions.md:293`) "Feedback (AI suggest vs final selection) only recorded when not stale".
Lựa chọn: A) Chỉ lần gần nhất — hệ quả: dữ liệu gọn, mất các lần gợi ý trung gian.   B) Mọi lần còn mới — hệ quả: đủ dữ liệu để đo, một bài có nhiều bản ghi.
Đề xuất: A, vì mỗi lần gợi ý mới thay lựa chọn trước (DEC-148).
Liên quan: AUD-M05-10

**7.**
Vấn đề: DRAFT §7.2 gợi ý Trending có thể dựa trên Views, Stars, Comments, Bookmarks, Recency; DEC-052 chỉ dùng upvote, bình luận và điểm thưởng bài mới cho Trending Topic/Tag.
Nguồn: `iShare_modules.md:337` "- Views", `:340` "- Bookmarks"; DEC-052 (`decisions.md:308`).
Lựa chọn: A) Xác nhận DEC-052 ghi đè DRAFT §7.2 cho Trending Topic/Tag — hệ quả: chỉ thêm dấu vết, không đổi yêu cầu.   B) Thêm lượt xem và bookmark vào công thức — hệ quả: đổi 008.1/008.2, cần hệ số mới.
Đề xuất: A, vì DEC-052, DEC-142 và DEC-146 đã chốt công thức và các tương tác được tính.
Liên quan: AUD-M05-18

**8.**
Vấn đề: Có đánh dấu ghi đè các câu cũ ở glossary (Topic, AI Classification) và ở DEC-125 (chủ sở hữu Follow Topic) không?
Nguồn: `glossary.md:14`, `glossary.md:29`, `decisions.md:695`.
Lựa chọn: A) Đánh dấu `[Amended …]`, trỏ tới DEC-048, QA-269, DEC-144, DEC-141 — hệ quả: register nhất quán.   B) Giữ nguyên — hệ quả: SR của các module sau có thể trích nhầm.
Đề xuất: A.
Liên quan: AUD-M05-21

## 7. Kết quả checklist

| Mã | Kết quả | AUD / ghi chú |
|---|---|---|
| CL-A01 | Đạt | P1: mọi câu DRAFT của M05 có chỗ đi. Hàng R5 Lớp/Khối không ghi DRAFT §3.3 (dấu vết yếu, không lập finding) |
| CL-A02 | Đạt | Không có COV-01; OWNED 76, trong SR 70, trong routing 23 |
| CL-A03 | Không đạt | AUD-M05-17 |
| CL-A04 | Đạt | Không có COV-02, TRC-06 |
| CL-A05 | Không đạt | AUD-M05-06, 10, 11 |
| CL-A06 | Đạt | 18 dòng `Suy ra` được suy lại, không tạo số liệu hay quyền mới |
| CL-A07 | Đạt | Mọi con số có nguồn; "168 giờ" là đổi đơn vị của 7 ngày |
| CL-A08 | Không đạt | AUD-M05-18 |
| CL-A09 | Không đạt | AUD-M05-02, AUD-M05-21 |
| CL-A10 | Không đạt | AUD-M05-03, AUD-M05-04 |
| CL-A11 | Không đạt | AUD-M05-01, 14, 15, 16 |
| CL-B01 | Không đạt | AUD-M05-09 |
| CL-B02 | Đạt | RULE-01/02/08 không báo; đọc tay đạt |
| CL-B03 | Không đạt | AUD-M05-07 |
| CL-B04 | Đạt | RULE-03 không báo |
| CL-B05 | Đạt | RULE-05 không báo; mọi chữ "đó" có danh từ đi kèm |
| CL-B06 | Đạt | RULE-06/07 không báo; đọc tay đạt |
| CL-B07 | Đạt | RULE-09 không báo |
| CL-B08 | Không đạt | AUD-M05-06, AUD-M05-03 |
| CL-B09 | Không đạt | AUD-M05-03 (từ chối theo dõi Topic nguồn) |
| CL-B10 | Đạt | Mỗi cận có yêu cầu cấp dưới riêng |
| CL-B11 | Đạt | Mọi thao tác theo vai trò có yêu cầu quyền |
| CL-B12 | Không đạt | AUD-M05-13 |
| CL-B13 | Không đạt | AUD-M05-03, AUD-M05-16 |
| CL-C01 | Không đạt | AUD-M05-08, AUD-M05-07 |
| CL-C02 | Đạt | Không có cấp dưới chỉ nhắc lại cấp trên |
| CL-C03 | Không đạt | AUD-M05-20, AUD-M05-06 |
| CL-C04 | Không đạt | AUD-M05-09, AUD-M05-12 |
| CL-C05 | Không đạt | AUD-M05-19; 5.1 khớp module-registry, dev_priority và DEC-151 |
| CL-D01 | Đạt | HDR-01…08 không báo |
| CL-D02 | Đạt | STR-01…09 không báo |
| CL-D03 | Đạt | REQ-00…04 không báo; 12 cấp trên, 92 cấp dưới |
| CL-D04 | Đạt | ID-01…06 không báo; bản đầu, snapshot trùng bản hiện tại |
| CL-D05 | Đạt | TRC-01…05, 07, 09, 10 không báo |
| CL-D06 | Đạt | REF-01/02 không báo; 3.2 "Không có." |
| CL-E01 | Đạt | Không có mô hình dữ liệu, NFR hay HMI trong mục 4–5 |
| CL-E02 | Đạt | Hiển thị, tìm kiếm, thông báo, công tắc AI đều nằm ở R5 |
| CL-E03 | Không đạt | AUD-M05-05 |
| CL-E04 | Đạt | 4.1 "Không có."; không có luật hay số liệu tự thêm |
| CL-F01 | Đạt | OPN-01…03 không báo; 9 OP loại Đề xuất, trạng thái Mở |
| CL-F02 | Đạt | Dòng lịch sử cuối 0.1 trùng header |
| CL-F03 | Đạt | Mọi câu trả lời có ID register; không có quyết định chỉ tồn tại trong SR |
| CL-F04 | Không đạt | AUD-M05-16 (lớp phụ: T-011 ngầm chọn) |
| CL-F05 | Đạt | Mục 1–4 không có "phải"; 3.1 đủ nguồn (0 thiếu, 0 thừa) |
| CL-F06 | Đạt | Có `[Vietnamese Doc]`; tiếng Anh chỉ ở thuật ngữ bắt buộc |

Đủ 45 mã: P1 chấm 12, P2 chấm 27, P3 chấm 6. Không mã nào bỏ trống hoặc ghi `Không kiểm được`.

## 8. Vòng trước (chỉ vòng 2)

Không áp dụng — vòng 1.

## 9. Hồ sơ xác minh

**Kiểm lại bằng chứng bằng máy (MERGE bước 2).** Đã kiểm 106 trích đoạn có `tệp:dòng` của ba tệp lượt bằng script: đọc đúng dòng ghi trong tệp lượt và so chuỗi con nguyên văn. Kết quả: **106 khớp, 0 lệch**. Script nằm ở scratchpad của phiên, ngoài repo. Ví dụ:

- `decisions.md:790` "it can no longer be selected, suggested, ranked in Trending or followed" → khớp
- `ISH-SR-M05.md:317` "cộng thêm số bài viết được tính của Topic đó được đăng trong 7 ngày gần nhất" → khớp
- `qa-log.md:521`, `decisions.md:774`, `decisions.md:375`, `ISH-RT-M05.md:64` (AUD-02) → khớp
- `grep -n -F "Người dùng theo dõi để nhận cập nhật" ISH-SR-M05.md` → 1 (dòng 288)
- `grep -n -F 'Số "+1" là điểm thưởng bài mới, chỉ cộng cho bài được đăng trong 7 ngày' qa-log.md` → 1 (dòng 1005)

Các khẳng định vắng mặt đã được từng lượt tìm bằng ít nhất hai cách (ID và từ khóa); số kết quả ghi ở mục 4 của từng tệp lượt:

- AUD-04: `grep -i -c "danh sách Tag"` trên SR và routing → 0/0; tìm `Classification` → 0.
- AUD-05: `grep -n -i "ngưỡng" ISH-SR-M05.md` → chỉ dòng 459; QA-235 chỉ có ở mục 3.1.
- AUD-10: tìm `latest|most recent|gần nhất|last suggest` trong register, lọc theo gợi ý/phản hồi → 0.
- AUD-14: tìm "ẩn" hoặc "kiểm duyệt" ở dòng 301–329 → 0.
- AUD-15: tìm "tiếng Việt", "bảng chữ cái", "collation" → không có kết quả liên quan.
- AUD-16: tìm "nháp"/"draft" trong SR, routing và register → không có ISS/QA nào về bài viết nháp.
- AUD-18: `grep -c "§7"` trên SR và routing → 0/0.
- AUD-19: tìm "theo dõi" ở 5.2 → 0.
- AUD-20: tìm "được tính" ở 2.1 → 0.

**Gộp trùng (MERGE bước 3):**

- P1-01 (CL-A10) và P3-05 (CL-B13, CL-B09) có cùng nguyên nhân (DEC-145 chỉ được đưa một phần) và cùng chỗ sửa → AUD-M05-03, DEFECT Trung bình.
- P2-01 (CL-A05, CL-C03) và P3-04 (CL-B08) có cùng nguyên nhân (định nghĩa "Bài viết công khai") → AUD-M05-06, DEFECT Trung bình. Cả hai lượt đều hạ một mức so với mặc định Cao của CL-A05, cùng lý do.
- Không gộp P2-09 với AUD-M05-01: "bài viết được tính" (thiếu thuật ngữ) và mốc "đăng" (mơ hồ nguồn) là hai nguyên nhân khác nhau.

**Mức và lớp (MERGE bước 4):** Giữ mức đề xuất của các lượt. Mọi chỗ lệch một mức so với mặc định đều có lý do ghi trong finding (AUD-06, 08, 10, 11, 14, 16, 17, 19). P1-05 giữ dạng DEFECT Thấp với lớp phụ OBSERVATION, không tách thành một OBSERVATION Trung bình riêng như §7.5 gợi ý, vì MERGE không thêm finding; khối hỏi stakeholder có ở mục 6, mục 7.

**Finding bị loại ở MERGE:** không có. Các finding mà từng lượt đã tự loại hoặc chỉnh được ghi ở mục 4 của tệp lượt tương ứng.

**Ánh xạ ID nháp → AUD:** P3-01→01; P1-06→02; P1-01+P3-05→03; P1-02→04; P1-03→05; P2-01+P3-04→06; P2-02→07; P2-03→08; P2-04→09; P2-05→10; P2-06→11; P2-07→12; P3-07→13; P3-02→14; P3-03→15; P3-06→16; P1-04→17; P1-05→18; P2-08→19; P2-09→20; P1-07→21.
