# Báo cáo audit — ISH-AUD-M05-r2
<!-- [Vietnamese Doc] -->

| Mã báo cáo | ISH-AUD-M05-r2 |
| --- | --- |
| SR được audit | ISH-SR-M05, phiên bản 0.2 (2026-10-05, Bản nháp) |
| Routing | ISH-RT-M05, phiên bản 0.2 (2026-10-05) |
| Vòng | 2 |
| Lượt đã gộp | P1, P2, P3 (ba lượt chạy độc lập, mỗi lượt một ngữ cảnh) |
| Ngày | 2026-10-05 |
| Auditor | Agent Auditor độc lập (lượt MERGE) |
| Kết luận | **Chưa đạt** — Chuyển stakeholder quyết (còn GAP chưa trả lời), sau đó Author sửa rồi chạy đợt xác minh |

## 1. Tóm tắt

Kết luận **Chưa đạt**. Còn 8 DEFECT mở: 4 mức Trung bình, 4 mức Thấp. Không còn CONFLICT, và `check_sr.py` không còn ERROR hay WARN. Bản 0.2 đã xử lý xong 20/21 finding của vòng 1. Cả năm vấn đề lớn của vòng 1 đã được stakeholder trả lời (DEC-154…159) và SR làm theo đúng câu trả lời: mốc "đăng", thông báo khi theo dõi Topic, bình luận bị ẩn, tên tiếng Việt, bản nháp không có Topic. AUD-M05-17 (disposition) mới sửa chưa đủ. Phần lớn lỗi còn lại là **hồi quy** do chính các bản sửa gây ra:
- 007.1 mâu thuẫn với 011.7 mới thêm.
- Các ID mới nằm ngoài câu cấp trên.
- 005.4 đã chọn trước điều mà OP-M05-10 còn đang hỏi.
- Dòng truy vết của 006.16 ghi sai nguồn.
- 008.15 trùng ý với 008.14.

Hai GAP mới cần stakeholder trả lời trước khi Author sửa: quy tắc so chữ số và dấu thanh khi phá hòa bằng tên Tag, và Tag chỉ có trên bài không công khai có được xếp hạng Trending hay không. Không có finding mức Cao.

| Lớp \ Mức | Cao | Trung bình | Thấp |
|---|---|---|---|
| DEFECT | 0 | 4 | 4 |
| CONFLICT | 0 | 0 | 0 |
| GAP | 0 | 2 | 0 |
| OBSERVATION | 0 | 0 | 2 |

Tổng: 12 finding còn mở. Gồm 11 finding mới (AUD-M05-22…32) và 1 finding vòng 1 mở lại (AUD-M05-17, Sửa chưa đủ). Gộp từ 12 finding nháp: P1 có 3, P2 có 7, P3 có 2. Không có cặp nào trùng nguyên nhân giữa các lượt (xem mục 9). Bảy trong 11 finding mới là `Hồi quy`.

## 2. Phạm vi và phương pháp

- **Tệp đã đọc:**
  - `ISH-SR-M05.md` v0.2 và `ISH-RT-M05.md` v0.2. Hai tệp trùng hoàn toàn với `work/snapshot-ISH-SR-M05-v0.2.md` và `work/snapshot-ISH-RT-M05-v0.2.md` (`diff -q` không báo khác biệt).
  - Ba lượt đều ghi đúng phiên bản 0.2.
  - Báo cáo vòng 1: `ISH-AUD-M05-r1.md`.
- **Tệp lượt đã gộp:**
  - `work/audit-P1-M05-r2.md`, kèm `coverage-M05-r2.md` (chạy lại toàn bộ ma trận vì tập OWNED đổi 76 → 100), `audit-inventory-P1-M05-r2.*` và `check-P1-M05-r2.json`.
  - `work/audit-P2-M05-r2.md`, kèm `check-P2-M05-r2.json`.
  - `work/audit-P3-M05-r2.md`, kèm `audit-tests-M05-r2.md` (119 ca và bảng quét khung hành vi cho phần đã đổi), `audit-inventory-P3-M05-r2.*` và `check-P3-M05-r2.json`.
- **Phạm vi thay đổi** (P1 và P2 đếm độc lập, ra cùng số): bản 0.2 có 12 yêu cầu cấp trên và 107 cấp dưới.
  - Thêm 17 ID, bỏ 2 ID (002.4, 010.4), đổi nội dung 13 ID: tổng 32/119 (khoảng 27 %).
  - Không thêm yêu cầu cấp trên nào.
  - P1 vẫn chạy lại toàn bộ ma trận theo điều kiện (c), vì có thêm 24 mục OWNED: DEC-154…159, ISS-228…236, QA-288…296.
- **Nguồn các lượt đã đọc:**
  - DRAFT `iShare_modules.md` §3.1–§3.4, §4.5, §7.1–§7.4, §8.1, §11.2, §11.5; `iShare_specs_general.md` §3, §6; `iShare_dev_priority.md`.
  - Registers đọc ngày 2026-10-05, gồm đủ 100 mục OWNED, đọc nguyên văn.
  - REFERENCING: 12/21 mục đọc nguyên văn, các mục còn lại đọc theo tiêu đề. KEYWORD đọc có chủ đích. CROSS-CUTTING đọc theo tiêu đề.
- **Script của lượt MERGE:**
  - `inventory.py` → `work/audit-inventory-M05-r2.md/.json`. Kết quả: OWNED 100, REFERENCING 21, KEYWORD 100, CROSS 42, DRAFT 30.
  - Tập OWNED và `registers_sha` trùng hoàn toàn với inventory của P1 và P3, tức là registers không đổi trong lúc các lượt chạy.
  - `check_sr.py --inventory … --tests work/tests-M05.md` → `work/check-M05-r2.json`.
- **Tính độc lập:**
  - Người gọi chỉ đưa mã module, vòng, lượt, gốc repo và đường dẫn báo cáo vòng 1. Không lượt nào nhận tóm tắt của Author.
  - Không lượt nào đọc tệp lượt vòng 2 của lượt khác.
  - P1 lập phần A của ma trận trước khi đọc thân SR. P3 ghi ca kiểm mới hoặc đã đổi và bảng quét trước khi mở SR v0.2.
  - Giới hạn các lượt tự ghi lại:
    - P1: lệnh `head -15` ở bước C0 cho thấy đoạn mục 1 Tổng quan của SR trước khi lập phần A.
    - P3: báo cáo vòng 1 (bắt buộc đọc) có trích lời văn v0.1, nên P3 đã biết lời văn đó ở các chỗ có finding trước khi dựng ca. P3 giữ nguyên ca A-001…A-098 của vòng 1 cho các nguồn không đổi.
- **Giới hạn (không kiểm được):**
  - "Stakeholder đã được báo" chỉ kiểm được qua register.
  - Chưa có SR của M03, M06, M07, M10, M13, M14. Các hàng R5 chỉ kiểm được nguồn, không kiểm được ID sở hữu hay việc module đích có nhận hàng đó hay không. Riêng AUD-M05-31 phụ thuộc vào điểm này.
  - Bảng Trending của M14 hiển thị bao nhiêu mục chưa xác định, nên chưa biết Tag 0 điểm ở AUD-M05-27 có thật sự hiện ra hay không.
  - Câu DEC-157 có áp cho lần gửi lại hay không không suy được từ register (AUD-M05-24).
  - Ý định của stakeholder ở các GAP không suy được. Báo cáo chỉ nêu các lựa chọn.
  - Chu kỳ tính lại điểm và cách lưu lượt xem (R1, R2) không kiểm.
  - KEYWORD: P1 đọc nội dung khoảng 15 mục, P3 đọc 4 mục; các mục còn lại chỉ đọc tiêu đề.
- **Ngoài phạm vi M05.** P1 ghi lại hai điểm sau để chuyển cho người viết SR M14; chúng không phải finding của SR M05:
  - DEC-158 áp "within the rolling 7-day window" cho cả Trending Post (`decisions.md:845`), trong khi DEC-124 dùng suy giảm với mốc cắt 28 ngày (`decisions.md:694`).
  - Câu "DEC-052 … stays unchanged" trong DEC-124 vẫn giữ nguyên chữ.

## 3. Kết quả kiểm tra tự động

Lệnh của MERGE (từ gốc repo):

```
python .agent-instructions/system_analysis/shared/sr-tools/inventory.py \
  --registers .agents/.claude/system_analysis/output/registers --draft docs/_temp --module M05 \
  --keywords "topic,tag,trending,chủ đề,thẻ,gợi ý,suggest,follow,theo dõi,phân loại,classification,merge,gộp,hashtag,category,chuyên mục,stale,khối lớp,grade" \
  --out .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-M05-r2.md \
  --json .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-M05-r2.json

python .agent-instructions/system_analysis/shared/sr-tools/check_sr.py \
  --sr .agents/.claude/system_analysis/output/specs/ISH-SR-M05.md \
  --routing .agents/.claude/system_analysis/output/specs/routing/ISH-RT-M05.md \
  --inventory .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-M05-r2.json \
  --tests .agents/.claude/system_analysis/output/specs/audit/work/tests-M05.md \
  --json .agents/.claude/system_analysis/output/specs/audit/work/check-M05-r2.json
```

**ERROR = 0, WARN = 0, INFO = 28.** Mã thoát 0. Có 12 yêu cầu cấp trên và 107 cấp dưới.

- INFO COV-03 × 26: DEC-047, 049, 050, 051, 052, 140, 141, 147, 150, 154, 155, 158, 159; ISS-207, ISS-229; QA-101, 102, 104, 106, 107, 268, 278, 288, 289, 294, 296. P1 đã kiểm tay ở CL-A10: phần nằm ở SR và phần nằm ở routing không trùng nhau, không phần nào bị sót.
- INFO COV-00: OWNED = 100; 92 mục có trong SR, 34 mục có trong routing.
- INFO TST-00: 168 ca cho 107 yêu cầu.

Không có COV-01, COV-02, INV-01 hay TST-01…05. Ba lượt cũng cho kết quả 0 ERROR, 0 WARN. Script không bắt được lỗi nào trong các finding ở mục 5: tất cả là lỗi ngữ nghĩa hoặc lỗi hồ sơ.

## 4. Ma trận độ phủ nguồn → yêu cầu

Bản đầy đủ nằm ở `work/coverage-M05-r2.md`:
- Phần A: mong đợi, lập trước khi đọc SR.
- Phần B: thực tế.
- Mục A.5: lệch nguồn.

P1 chạy lại toàn bộ ma trận. Kết quả: **100/100 mục OWNED có chỗ đi**, không có mục Thiếu, Sai chỗ hay Thiếu một phần. 21/21 mục REFERENCING đã được phân loại.

Bảng dưới ghi các mục nguồn mới, các mục mà finding vòng 1 chạm tới, và các hàng có finding. `S:` là số dòng trong `ISH-SR-M05.md`, `R:` là số dòng trong `ISH-RT-M05.md`.

| Nguồn | Mong đợi (Auditor) | Thực tế (SR / routing) | Kết quả | AUD |
|---|---|---|---|---|
| DEC-154, ISS-228, ISS-231, ISS-232, QA-288, QA-291, QA-292 | SR (mốc công khai lần đầu, bình luận bị ẩn, thứ tự tiếng Việt) | 2.1 (S:39, S:62); 008.1, 008.2, 008.11, 008.12, 008.17; R1 (R:21) | Khớp | 26 (phần nguồn còn để ngỏ) |
| DEC-155, ISS-229, QA-289 | R5 M07 + mô tả | R5 M07 (R:69); 2.1 (S:54); Lý do 5.9 (S:302) | Khớp | — |
| DEC-156, ISS-230, QA-290 | SR | 002 (S:162), 002.5, 002.6, 002.11 | Khớp | 23, 29 (lời văn) |
| DEC-157, ISS-233, QA-293 | SR | 005.1, 005.4 | Khớp | 24 |
| DEC-158, ISS-234, QA-294 | SR + R1 + R5 M14 + dấu vết DRAFT §7.2 | 008.13…008.16; R1 (R:20); R5 M14 (R:66); R5 M03 (R:75); R6 (R:87) | Khớp | 28; 31 (chủ sở hữu R:75) |
| DEC-159, ISS-236, QA-296 | SR + R3 | 011.8…011.10; R3 (R:42) | Khớp | — |
| ISS-235, QA-295 | R4 | R4 (R:54) | Khớp | — |
| DEC-145, ISS-214, ISS-215, QA-274, QA-275 | SR đủ bốn hệ quả | 002.2, 004.5, 011.6 (S:411), 011.7 (S:412); 5.2 (S:131, S:132) | Khớp | 22, 23 (hồi quy của bản sửa) |
| DEC-146, ISS-216, ISS-217, QA-276, QA-277 | SR | 2.1 (S:37, S:38), 008.3…008.7 | Khớp | — |
| DRAFT §7.2 ↔ DEC-052 | SR theo register + dấu vết | 008 (S:533), 008.13 (S:546) ghi DRAFT §7.2 + DEC-158; R6 (R:87) | Khớp | — |
| DEC-052, QA-106 | SR + R2 + R5 | 008, 008.8; R2 (R:27); R5 (R:65) | Khớp | 32 (QA-106 chưa có nhãn, nằm ở register) |
| KEYWORD QA-011 | SR/R5 | Topic → 001.3; Topic trên bài → 002.10; Tag trên bài → 006.16; danh sách Tag → R5 M14/M06 (R:64); Khối lớp → R5 (R:70) | Khớp | 25 (truy vết 006.16); 31 (chủ sở hữu R:64); 17 (lý do cũ ở disposition) |
| KEYWORD QA-235, ISS-175 | SR/OP + R5 | 008.18, 008.19 (S:348, S:349); R4 (R:55); R5 (R:67) | Khớp | 27 (008.19 mới); 17 (lý do cũ ở disposition) |
| KEYWORD còn lại (inventory Author 108) và bản ISS/QA của CROSS-CUTTING | Mỗi mục một dòng disposition | 26 KEYWORD và 24 CROSS chỉ có câu gộp (disposition:69) | Thiếu phân loại | 17 |
| QA-106, QA-226, ISS-171 (register) | Nhãn sửa đổi theo DEC-158 | Không có nhãn | Lệch trong register | 32 |
| Các mục OWNED còn lại (DRAFT §3.x, DEC-047…052, DEC-140…153 và các ISS/QA tương ứng) | Như vòng 1 | Như `coverage-M05-r2.md` phần B | Khớp | — |

## 5. Phát hiện

Thứ tự: mức Trung bình trước, mức Thấp sau. Trong cùng một mức, xếp theo lớp (DEFECT, GAP, OBSERVATION). AUD-M05-17 là finding vòng 1 được mở lại; nó giữ ID cũ và đứng ở vị trí theo mức của nó.

### AUD-M05-22 — ISH-M05-007.1 chấp nhận theo dõi mọi Topic, trái với ISH-M05-011.7 (từ chối theo dõi Topic đã bị loại khỏi danh mục)

| Lớp | DEFECT | Nhãn | Hồi quy | Mức | Trung bình | Checklist | CL-C01 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-007.1 (`ISH-SR-M05.md:308`), ISH-M05-011.7 (`ISH-SR-M05.md:412`); cấp trên ISH-M05-007 (`ISH-SR-M05.md:298`).
- **Bằng chứng trong SR:**
  - "Khi người dùng đã đăng nhập yêu cầu theo dõi một Topic chưa theo dõi, hệ thống phải ghi nhận người dùng đó đang theo dõi Topic đó." (`ISH-SR-M05.md:308`)
  - "Khi người dùng yêu cầu theo dõi một Topic đã bị loại khỏi danh mục Topic, hệ thống phải từ chối yêu cầu đó." (`ISH-SR-M05.md:412`)
  - "Hệ thống phải cho phép người dùng đã đăng nhập theo dõi một Topic." (`ISH-SR-M05.md:298`)
  - "Topic đã loại khỏi danh mục Topic (trạng thái cuối)" (`ISH-SR-M05.md:126`)
- **Bằng chứng trong nguồn:** "it can no longer be selected, suggested, ranked in Trending or followed" (`decisions.md:793`, DEC-145).
- **Vấn đề:** Bản 0.2 thêm 011.7 để xử lý AUD-M05-03. Nhưng 007.1 và câu cấp trên 007 vẫn áp dụng cho "một Topic" bất kỳ, không giới hạn vào Topic trong danh mục. Ca kiểm: User A đã đăng nhập, chưa theo dõi, yêu cầu theo dõi Topic nguồn đã bị gộp. Theo 007.1, hệ thống ghi nhận A đang theo dõi; theo 011.7, hệ thống từ chối. Hai yêu cầu có cùng đối tượng và cùng sự kiện nhưng cho kết quả khác nhau. Với Trending thì không có mâu thuẫn tương tự, vì 008.18 đã giới hạn vào "mọi Topic trong danh mục Topic".
- **Lý do mức:** CL-C01 mặc định Cao. Hạ một mức, như AUD-M05-08, vì ý của nguồn rõ, mâu thuẫn chỉ xảy ra với Topic đã bị gộp, và người đọc có thể hiểu 011.7 là ngoại lệ của 007.1.
- **Hệ quả nếu không sửa:** Ca kiểm chấp nhận cho việc theo dõi Topic nguồn có hai "Then" khác nhau.
- **Hướng xử lý (Author quyết cách viết):** Giới hạn 007.1 (và câu cấp trên 007 nếu cần) vào Topic thuộc danh mục Topic, hoặc thêm điều kiện loại trừ vào 007.1. Xem thêm AUD-M05-23 về vị trí của 011.7.
- **Trạng thái:** Mở.

### AUD-M05-23 — Các yêu cầu cấp dưới mới thêm nằm ngoài câu cấp trên (ISH-M05-002.10, 002.11, 006.16, 011.7)

| Lớp | DEFECT | Nhãn | Hồi quy | Mức | Trung bình | Checklist | CL-C04 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-002 (`ISH-SR-M05.md:162`) với 002.10 (`:180`) và 002.11 (`:181`); ISH-M05-006 (`:265`) với 006.16 (`:290`); ISH-M05-011 (`:396`) với 011.7 (`:412`).
- **Bằng chứng trong SR:**
  - "Hệ thống phải yêu cầu mỗi bài viết đã gửi có từ 1 đến 3 Topic" (`ISH-SR-M05.md:162`)
  - "Khi người dùng, kể cả Guest, xem một bài viết, hệ thống phải hiển thị các Topic" (`ISH-SR-M05.md:180`)
  - "Hệ thống phải cho phép tác giả lưu bản nháp của bài viết khi bài viết chưa có Topic nào." (`ISH-SR-M05.md:181`)
  - "Hệ thống phải gắn cho mỗi bài viết từ 0 đến 5 Tag tự do do tác giả nhập." (`ISH-SR-M05.md:265`)
  - "hệ thống phải hiển thị các Tag hoạt động của bài viết đó" (`ISH-SR-M05.md:290`)
  - "hệ thống phải chuyển mọi bài viết đang gắn Topic nguồn sang Topic đích." (`ISH-SR-M05.md:396`)
  - "Khi người dùng yêu cầu theo dõi một Topic đã bị loại khỏi danh mục Topic" (`ISH-SR-M05.md:412`)
- **Vấn đề:** Đây là cùng loại lỗi với AUD-M05-12. Lỗi đó đã được sửa cho 010.4 và 012.9…012.11, nhưng nay xuất hiện lại ở các ID mới của bản 0.2:
  - Câu cấp trên 002 là ràng buộc số Topic của bài viết **đã gửi**. 002.10 là hành vi hiển thị Topic, còn 002.11 là hành vi với **bản nháp**.
  - Câu cấp trên 006 nói về việc gắn 0–5 Tag. 006.16 là hành vi hiển thị Tag.
  - Câu cấp trên 011 nói về việc chuyển bài viết khi gộp Topic. 011.7 là phản hồi cho một yêu cầu **theo dõi**.
- **Hệ quả nếu không sửa:** Câu cấp trên không cho người đọc biết tính năng gồm những hành vi nào. Theo CL-C04, yêu cầu cấp dưới thêm hành vi mà câu cấp trên không nói là DEFECT.
- **Hướng xử lý (Author quyết cách viết):** Mở rộng câu cấp trên của 002, 006 và 011, hoặc chuyển yêu cầu: 002.10 và 006.16 sang một tính năng có câu cấp trên phù hợp (lưu ý OP-M05-12 về chủ sở hữu việc hiển thị), 011.7 sang 5.9 Theo dõi Topic. Nếu chỉ sửa câu cấp trên thì khung 12 tính năng của DEC-151 không đổi.
- **Trạng thái:** Mở.

### AUD-M05-24 — ISH-M05-005.4 đã quyết điều mà OP-M05-10 còn đang hỏi, và đề xuất mặc định của OP ngược với 005.4

| Lớp | DEFECT | Lớp phụ | GAP | Nhãn | Hồi quy | Mức | Trung bình | Checklist | CL-F01 (mặt CL-F04, xem Vấn đề) |
|---|---|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-005.4 (`ISH-SR-M05.md:257`); OP-M05-10 (`ISH-SR-M05.md:596`).
- **Bằng chứng trong SR:**
  - "hệ thống phải ghi đúng một phản hồi gợi ý Topic cho lần gửi đó" (`ISH-SR-M05.md:257`)
  - "Đề xuất mặc định: chỉ ghi ở lần gửi đầu tiên." (`ISH-SR-M05.md:596`), cho câu hỏi về bài viết bị từ chối rồi được gửi lại.
- **Bằng chứng trong nguồn:**
  - "one record per submission" (`decisions.md:841`, DEC-157)
  - "Chỉ lần gợi ý gần nhất; một bản ghi mỗi lần gửi bài." (`qa-log.md:1028`, QA-293)
  - "REJECTED: mod rejected, author can fix and resubmit" (`decisions.md:198`, DEC-031)
- **Vấn đề:** 005.4 mới thêm ở bản 0.2 viết: mỗi lần gửi có gợi ý còn mới thì ghi đúng một phản hồi. Lần gửi lại sau khi bị từ chối cũng là một lần gửi, nên theo 005.4 hệ thống ghi thêm một phản hồi. Trong khi đó OP-M05-10 vẫn ở trạng thái Mở, với đề xuất "chỉ ghi ở lần gửi đầu tiên".

  Ca kiểm: bài bị Mod từ chối, tác giả chỉ đổi tệp đính kèm (gợi ý vẫn còn mới theo 003.11) rồi gửi lại. Theo 005.4 có hai phản hồi; theo đề xuất của OP-M05-10 chỉ có một.

  Dù đọc DEC-157 theo cách nào thì hồ sơ vẫn có lỗi:
  - Nếu DEC-157 đã trả lời câu hỏi của OP-M05-10: OP phải được xóa (CL-F01, "không còn OP đã được trả lời"), và đề xuất mặc định của nó sai.
  - Nếu DEC-157 không nói gì về việc gửi lại: 005.4 đã tự chọn một phương án trước khi stakeholder trả lời. Đây là mặt CL-F04 (quyết định ngầm). P2 nêu mặt này và chuyển cho P3; P3 thì chấm CL-F04 trước khi xét 005.4 (xem mục 7).
- **Hệ quả nếu không sửa:** Dữ liệu phản hồi cho việc đánh giá AI (M13) có số bản ghi khác nhau, tùy người cài đặt đọc theo 005.4 hay theo OP-M05-10.
- **Hướng xử lý (Author quyết cách viết):** Trước hết xác định DEC-157 có trả lời câu hỏi về lần gửi lại hay không.
  - Nếu có: xóa OP-M05-10 và ghi Lịch sử.
  - Nếu không: viết 005.4 sao cho không quyết phần gửi lại, và giữ OP.
  - Nếu Author không tự xác định được: hỏi stakeholder (mục 6, khối 3).
- **Trạng thái:** Mở.

### AUD-M05-25 — Dòng truy vết của ISH-M05-006.16 ghi `Nói thẳng` và dẫn "AI Classification trên post" cho việc hiển thị Tag

| Lớp | DEFECT | Nhãn | Hồi quy | Mức | Trung bình | Checklist | CL-A05 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** Phụ lục A, dòng ISH-M05-006.16 (`ISH-SR-M05.md:525`); yêu cầu ở `ISH-SR-M05.md:290`.
- **Bằng chứng trong SR:**
  - "| ISH-M05-006.16 | QA-011, DEC-051 | Nói thẳng |" (`ISH-SR-M05.md:525`)
  - "hệ thống phải hiển thị các Tag hoạt động của bài viết đó" (`ISH-SR-M05.md:290`)
- **Bằng chứng trong nguồn:**
  - "AI: Xem AI Summary + AI Classification trên post" (`qa-log.md:137`, QA-011)
  - "Tag: user tự quyết định hoàn toàn, AI không can thiệp" (`qa-log.md:209`, QA-017)
  - "Phase 5 (DEC-050/051) đã thu hẹp phạm vi AI classification chỉ còn Topic" (`qa-log.md:1004`, QA-269)
  - "tag chip hidden from display" (`decisions.md:303`, DEC-051): câu này chỉ nói về Tag bị vô hiệu hóa.
  - "it then shows again on the posts that carry it" (`decisions.md:813`, DEC-150): nguồn này không có trong cột Nguồn của 006.16.
  - "POST: Xem/đọc post" (`qa-log.md:132`): nguồn này không được dẫn trong Ghi chú.
- **Vấn đề:** Hai nguồn trong cột Nguồn không nêu thẳng hành vi "hiển thị Tag hoạt động trên bài viết cho mọi người dùng":
  - "AI Classification trên post" chỉ áp dụng cho Topic.
  - DEC-051 chỉ nói Tag bị vô hiệu hóa thì bị ẩn.

  Hành vi này có cơ sở ở DEC-150, nhưng cơ sở `Nói thẳng` và lời giải thích trong Ghi chú không khớp với các nguồn đang được dẫn. Với 002.10 (hiển thị Topic), dẫn "AI Classification trên post" là hợp lệ.
- **Lý do mức:** CL-A05 mặc định Cao. Hạ một mức, như AUD-M05-11, vì hành vi có nguồn; chỉ dòng truy vết dẫn sai.
- **Hệ quả nếu không sửa:** Người kiểm truy vết sẽ thấy một nguồn nói về AI phân loại Topic được dùng làm căn cứ cho việc hiển thị Tag.
- **Hướng xử lý (Author quyết cách viết):** Sửa cột Nguồn (thêm DEC-150 và dòng POST của QA-011) và sửa Ghi chú. Nếu không có câu nguồn nào nêu thẳng hành vi này, đổi sang `Suy ra` kèm phép suy luận.
- **Trạng thái:** Mở.

### AUD-M05-26 — Thứ tự bảng chữ cái tiếng Việt khi phá hòa chưa nói chữ số, ký tự ngoài chữ cái và dấu thanh xếp ở đâu

| Lớp | GAP | Mức | Trung bình | Checklist | CL-A11, CL-B13 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.12 (`ISH-SR-M05.md:342`); ISH-M05-008.11 (`:341`); định nghĩa "Thứ tự bảng chữ cái tiếng Việt" ở 2.1 (`:62`).
- **Bằng chứng trong SR:**
  - "Thứ tự chữ cái a ă â b c d đ e ê g h i k l m n o ô ơ p q r s t u ư v x y, không phân biệt chữ hoa, chữ thường." (`ISH-SR-M05.md:62`)
  - "rồi đến tên theo thứ tự bảng chữ cái tiếng Việt" (`ISH-SR-M05.md:342`)
  - "Tên Tag được chứa những ký tự nào ngoài chữ và số" (`ISH-SR-M05.md:595`, OP-M05-09)
- **Bằng chứng trong nguồn:**
  - "(3) The name tie-break uses Vietnamese alphabetical order (a ă â b c d đ e ê …), case-insensitive." (`decisions.md:829`, DEC-154)
  - "Theo bảng chữ cái tiếng Việt (a ă â b c d đ e ê …), không phân biệt chữ hoa–thường" (`qa-log.md:1027`, QA-292)
- **Vấn đề:** DEC-154 đã đóng câu hỏi AUD-M05-15 phần chữ cái, nhưng chưa nói ba điều. Mỗi điều cho thứ hạng khác nhau mà người dùng nhìn thấy được:
  - **Chữ số và ký tự ngoài chữ cái.** Ca A-109: hai Tag "2k8" và "anh" bằng điểm và bằng số bài mới. Chữ số đứng trước chữ cái thì "2k8" xếp trước; đứng sau thì "anh" xếp trước.
  - **Dấu thanh.** Ca A-110: "nghỉhè" và "nghĩhè" chỉ khác nhau ở dấu hỏi và dấu ngã.
  - **Mức độ thường gặp.** Hai Tag bằng nhau ở cả hai tiêu chí đầu là chuyện thường: mọi Tag chỉ có một bài mới và không có tương tác đều có 1 điểm. Vì vậy tiêu chí thứ ba quyết định thứ tự của nhiều Tag.

  Với 11 Topic thì không có cặp nào làm lộ khác biệt này. Ca của Author (T-158, T-159) chỉ dùng các tên khác nhau ở chữ cái. Không có ISS/QA/DEC hay OP nào về điểm này.
- **Lý do mức:** CL-A11 mặc định Cao khi chỗ mơ hồ nằm ở công thức. Hạ một mức vì đây là tiêu chí phá hòa thứ ba, chỉ áp dụng cho Tag, và phần chính của quy tắc đã xác định.
- **Hệ quả nếu không sửa:** Hai cách cài đặt cho hai thứ tự khác nhau trên bảng Trending Tag. Ca kiểm của 008.12 không có một "Then" duy nhất.
- **Hướng xử lý:** Hỏi stakeholder (mục 6, khối 1); có thể hỏi chung với OP-M05-09. Ghi câu trả lời vào register, bổ sung định nghĩa ở 2.1, và thêm ca kiểm có chữ số và dấu thanh. Nếu chưa hỏi ngay thì ghi một `OP` vào Phụ lục B.
- **Trạng thái:** Mở.

### AUD-M05-27 — Tag chưa có bài viết nào được tính (chỉ có trên bản nháp, trong Group Private hoặc trên bài chưa công khai) có vào xếp hạng Trending không

| Lớp | GAP | Nhãn | Hồi quy | Mức | Trung bình | Checklist | CL-A11, CL-B13 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.19 (`ISH-SR-M05.md:349`, yêu cầu mới của bản 0.2); ISH-M05-006.2 (`:276`).
- **Bằng chứng trong SR:**
  - "Hệ thống phải đưa mọi Tag hoạt động vào xếp hạng Trending mà không đặt ngưỡng điểm tối thiểu." (`ISH-SR-M05.md:349`)
  - "Khi tác giả gắn một tên Tag chưa tồn tại cho bài viết, hệ thống phải tạo Tag mới với tên đó mà không cần phê duyệt." (`ISH-SR-M05.md:276`)
- **Bằng chứng trong nguồn:**
  - "Không đặt ngưỡng cho MS1 — dataset demo nhỏ (~70 bài, 30 user), đặt ngưỡng dễ khiến Trending trống/gần trống lúc demo." (`qa-log.md:939`, QA-235)
  - "- Auto-created, no approval" (`decisions.md:300`, DEC-051)
  - "and not in a Private group count" (`decisions.md:797`, DEC-146)
  - "Guest (unauthenticated) can view Newest and the full Trending tab (all 3 sub-views)" (`decisions.md:700`, DEC-126)
- **Vấn đề:** QA-235 bỏ ngưỡng tối thiểu về upvote và bình luận. Nguồn không nói gì về Tag chưa có bài viết nào được tính. Ca A-119: Tag "đềthi12a1" chỉ gắn trên bài trong một Group Private, hoặc chỉ trên một bản nháp. Có hai cách đọc hợp lý:
  - Cách 1, cách bản 0.2 đang viết ("mọi Tag hoạt động"): Tag có mặt trong bảng với 0 điểm, và Guest cũng thấy.
  - Cách 2, chỉ xếp hạng Tag có ít nhất một bài viết được tính: Tag không có mặt.

  Theo cách 1, tên Tag dùng trong Group Private hoặc trong bản nháp sẽ hiện công khai, trái với tinh thần của DEC-146. Không có ISS/QA/DEC hay OP nào về điểm này.
- **Lý do mức:** CL-A11 mặc định Cao khi chỗ mơ hồ liên quan phạm vi dữ liệu. Hạ một mức vì chỉ lộ tên Tag ở 0 điểm, không lộ nội dung bài, và số mục hiển thị do M14 quyết.
- **Hệ quả nếu không sửa:** Tên Tag lấy từ nội dung riêng tư hoặc chưa đăng có thể hiện trên bảng Trending Tag công khai.
- **Hướng xử lý:** Hỏi stakeholder (mục 6, khối 2), ghi câu trả lời vào register, sửa 008.19 và thêm ca kiểm. Nếu chưa hỏi ngay thì ghi `OP` vào Phụ lục B.
- **Trạng thái:** Mở.

### AUD-M05-17 — Disposition vẫn gộp các mục KEYWORD/CROSS-CUTTING không liên quan vào một câu, và còn lý do cũ trái với SR/routing 0.2

| Lớp | DEFECT | Mức | Thấp | Checklist | CL-A03 |
|---|---|---|---|---|---|

- **Vị trí:** `work/disposition-M05.md:69`, `:73`, `:80`, `:94`, `:54`; `work/selfcheck-M05.md:14`.
- **Bằng chứng:**
  - Câu gộp: "các mục KEYWORD còn lại khớp từ khóa chung "follow/lớp/gộp/category/dropdown" trong ngữ cảnh module khác — không liên quan" (`disposition-M05.md:69`).
  - Inventory của chính Author: "## KEYWORD hits trong register (108 muc)" (`inventory-M05.md:155`). Có 26 mục KEYWORD không có dòng ở SR, routing hay disposition: DEC-015, DEC-020, DEC-025, DEC-067, DEC-104, ISS-059, ISS-099, ISS-161, ISS-162, ISS-164, ISS-179, ISS-192, QA-047, QA-067, QA-069, QA-128, QA-192, QA-219, QA-220, QA-222, QA-230, QA-239, QA-242, QA-251, QA-256, QA-258.
  - CROSS-CUTTING: chỉ các DEC có dòng ("| DEC-128, DEC-129, DEC-130", `disposition-M05.md:130`). 24 mục ISS/QA tương ứng không có dòng: ISS-189, 191, 193, 196…204, 206; QA-248, 250, 252, 255, 257, 259…261, 263, 264, 266.
  - Bốn lý do cũ, nay trái với SR và routing 0.2:
    - `disposition-M05.md:73` ghi '"AI Classification trên post" không còn (DEC-050)', trong khi 002.10 dẫn chính dòng đó (`ISH-SR-M05.md:479`).
    - `disposition-M05.md:94` ghi "| QA-235, ISS-175 | Không ngưỡng tối thiểu vào Trending | R5 | M14 (hiển thị) |", trong khi SR có "| ISH-M05-008.18 | QA-235, ISS-175 | Nói thẳng |" (`ISH-SR-M05.md:551`).
    - `disposition-M05.md:80` ghi 'Không có sự kiện "bài mới trong Topic đang theo dõi"', trong khi register nay có "[Added 2026-10-05 — DEC-155]" (`decisions.md:392`).
    - `disposition-M05.md:54` ghi "Trending Post (M14) dùng decay; DEC-052 giữ nguyên", trong khi DEC-158 đã sửa DEC-052.
  - Selfcheck ghi CL-A03 Đạt: "disposition-M05.md nay có một dòng cho mỗi mục KEYWORD" (`selfcheck-M05.md:14`).
- **Vấn đề:** Author đã thêm dòng cho đúng 30 mục mà vòng 1 liệt kê, nhưng vẫn giữ câu gộp cho phần còn lại. Nguyên nhân của AUD-M05-17 (gộp nhiều mục vào một câu thay vì mỗi mục một dòng, RULES §7.7) vì vậy chưa được xử lý. Ngoài ra còn bốn lý do đã cũ. P1 đọc lấy mẫu có chủ đích QA-230, DEC-025, ISS-162, QA-242, ISS-189, QA-264: tất cả thuộc module khác hoặc không liên quan.
- **Lý do mức:** CL-A03 mặc định Trung bình. Giữ mức Thấp như vòng 1 vì mọi mục lấy mẫu đều không liên quan đến M05.
- **Hệ quả nếu không sửa:** Không chứng minh được "không sót" cho 50 mục; bốn lý do cũ có thể dẫn người đọc tới kết luận sai.
- **Hướng xử lý (Author quyết cách viết):** Thêm một dòng cho mỗi mục KEYWORD và CROSS-CUTTING chưa có chỗ đi, theo inventory hiện hành. Bỏ câu gộp ở dòng 69, cập nhật bốn lý do cũ và sửa lời khẳng định ở selfcheck.
- **Trạng thái:** Sửa chưa đủ (mở lại từ vòng 1).

### AUD-M05-28 — ISH-M05-008.15 trùng ý với ISH-M05-008.14

| Lớp | DEFECT | Nhãn | Hồi quy | Mức | Thấp | Checklist | CL-C02 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.14 (`ISH-SR-M05.md:344`), ISH-M05-008.15 (`ISH-SR-M05.md:345`).
- **Bằng chứng:** "số người dùng đã đăng nhập khác nhau, không kể tác giả" (`ISH-SR-M05.md:344`); "Hệ thống phải không đếm lượt mở trang chi tiết bài viết của Guest vào số người xem." (`ISH-SR-M05.md:345`); nguồn: "Guest views are not counted" (`decisions.md:845`, DEC-158).
- **Vấn đề:** 008.14 đã giới hạn số người xem vào người dùng đã đăng nhập, và 2.1 định nghĩa Guest là người chưa đăng nhập. Vì vậy mọi ca kiểm của 008.15 đều đã được 008.14 quyết định.
- **Hệ quả nếu không sửa:** Một hành vi được viết ở hai yêu cầu. Sửa một yêu cầu mà quên yêu cầu kia sẽ sinh mâu thuẫn.
- **Hướng xử lý (Author quyết cách viết):** Gộp 008.15 vào 008.14 và ghi ID bị bỏ vào Lịch sử, hoặc giải thích ở Phụ lục A.
- **Trạng thái:** Mở.

### AUD-M05-29 — ISH-M05-002.11 dùng mẫu Phổ quát, đặt điều kiện trạng thái ở cuối câu

| Lớp | DEFECT | Nhãn | Hồi quy | Mức | Thấp | Checklist | CL-B01 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-002.11 (`ISH-SR-M05.md:181`).
- **Bằng chứng:** "Hệ thống phải cho phép tác giả lưu bản nháp của bài viết khi bài viết chưa có Topic nào." (`ISH-SR-M05.md:181`). RULES §4.6: trạng thái kéo dài dùng `Trong khi …`, sự kiện tức thời dùng `Khi …`.
- **Vấn đề:** Câu có một trạng thái ("bài viết chưa có Topic nào") và một sự kiện (tác giả lưu bản nháp), nhưng viết theo mẫu Phổ quát và đặt "khi" ở cuối câu. Đây cùng dạng lỗi với AUD-M05-09. Script không bắt được lỗi này.
- **Lý do mức:** CL-B01 mặc định Trung bình. Hạ một mức vì câu vẫn chỉ đọc được một cách.
- **Hướng xử lý:** Viết lại theo mẫu `Khi …` hoặc `Trong khi …, khi …`.
- **Trạng thái:** Mở.

### AUD-M05-30 — Lịch sử sửa đổi 0.2 không ghi các thay đổi ở mục 4 và mục 5.1

| Lớp | DEFECT | Mức | Thấp | Checklist | CL-F02 |
|---|---|---|---|---|---|

- **Vị trí:** dòng Lịch sử 0.2 (`ISH-SR-M05.md:458`); mục 4 (`:91`, `:95`); 5.1 (`:117`); 5.2 (`:132`).
- **Bằng chứng:**
  - Mục 4: bản 0.1 viết "Topic là danh mục một tầng gồm các lĩnh vực tri thức cố định" (`snapshot-ISH-SR-M05-v0.1.md:85`). Bản 0.2 viết "gồm 11 lĩnh vực tri thức chốt sẵn, không ai thêm hay xóa được" (`ISH-SR-M05.md:91`) và thêm "từ upvote, bình luận, bookmark và người xem trong 7 ngày gần nhất" (`ISH-SR-M05.md:95`).
  - Mục 5.1: bản 0.1 ghi "Gộp Topic | ISH-M05-011 | Must | P0 | ISH-M05-011.3, ISH-M05-011.4: P1" (`snapshot-ISH-SR-M05-v0.1.md:111`). Bản 0.2 ghi "ISH-M05-011.3, ISH-M05-011.4, ISH-M05-011.6, ISH-M05-011.7: P1" (`ISH-SR-M05.md:117`).
  - Lịch sử chỉ ghi "5.2 thêm trạng thái theo dõi" (`ISH-SR-M05.md:458`). Hàng 5.2 mới "Người dùng yêu cầu theo dõi, hoặc Mod/Admin yêu cầu gộp với Topic đó" (`ISH-SR-M05.md:132`) có cả việc từ chối gộp.
- **Vấn đề:** Hai thay đổi nội dung ở mục 4 và một thay đổi mốc ở 5.1 không được ghi ở Lịch sử.
- **Hướng xử lý:** Bổ sung các thay đổi này vào dòng 0.2, hoặc vào dòng của phiên bản kế tiếp.
- **Trạng thái:** Mở.

### AUD-M05-31 — Hai hàng R5 giao chủ sở hữu mà nguồn không nêu: ghi nhận lượt xem (M03) và danh sách Tag cho Guest (M14/M06)

| Lớp | OBSERVATION | Mức | Thấp | Checklist | CL-E03 |
|---|---|---|---|---|---|

- **Vị trí:** routing R5 (`ISH-RT-M05.md:75`, `:64`); ISH-M05-001.3 (`ISH-SR-M05.md:152`); ISH-M05-008.14.
- **Bằng chứng:**
  - "Ghi nhận lượt mở trang chi tiết bài viết của người dùng đã đăng nhập (trang bài viết thuộc M03)" (`ISH-RT-M05.md:75`)
  - "gồm danh sách Tag cho Guest (QA-011)" (`ISH-RT-M05.md:64`)
  - "kể cả Guest, xem danh sách Topic trong danh mục Topic" (`ISH-SR-M05.md:152`)
  - Nguồn:
    - "Viewing data is recorded per view with its time (detail in Phase 8)" (`decisions.md:845`, DEC-158): không nêu module nào ghi nhận lượt xem.
    - "Browsing posts by Topic/Tag" (`decisions.md:817`, DEC-151): chỉ nói về duyệt bài viết.
    - "CLAS: Xem danh sách Topic / Tag / Khối lớp" (`qa-log.md:134`, QA-011).
- **Vấn đề:** Hai việc giao chủ sở hữu ở R5 chưa có nguồn xác nhận và chưa có OP:
  - **Ghi nhận lượt xem.** Kết quả người dùng nhìn thấy của việc này chỉ là điểm Trending (M05) và Trending Post (M14). Vì vậy theo quy tắc 4A, chủ sở hữu chưa hiển nhiên là M03.
  - **Danh sách Tag cho Guest.** Cùng một câu của QA-011, phần danh sách Topic ở SR M05 (001.3), còn phần danh sách Tag đi sang M14/M06 với nguồn là DEC-151.

  Không xếp DEFECT vì cả hai hàng đều có chỗ đi và có module nhận.
- **Hệ quả nếu không xử lý:** Có thể không module nào viết yêu cầu ghi nhận lượt xem, và khi đó 008.14 không có dữ liệu để kiểm.
- **Hướng xử lý:** Đặt OP loại Đề xuất về chủ sở hữu (RULES §5 mục 2), hoặc nêu nguồn xác nhận. Stakeholder quyết (mục 6, khối 4).
- **Trạng thái:** Mở.

### AUD-M05-32 — Câu cũ trong register chưa được đánh dấu sau DEC-158: QA-106 (OWNED), QA-226, ISS-171

| Lớp | OBSERVATION | Mức | Thấp | Checklist | CL-A09 |
|---|---|---|---|---|---|

- **Vị trí:** Không nằm trong SR. SR đã viết theo DEC-158 và dẫn QA-106 ở ISH-M05-008 (`ISH-SR-M05.md:533`) và ở R2 (`ISH-RT-M05.md:27`).
- **Bằng chứng:**
  - "score = Σ(1+upvotes×2+comments×1), recalc every 15-30min" (`qa-log.md:745`, QA-106)
  - "Trending Topic/Tag giữ nguyên DEC-052 (rolling 7-day hard window" (`qa-log.md:930`, QA-226)
  - "Trending Topic/Tag giữ nguyên DEC-052; Trending Post là khái niệm mới" (`issue-queue.md:261`, ISS-171)
  - Đối chiếu: "**[Amended 2026-10-05 — DEC-158: engagement adds 1 × bookmarks" (`decisions.md:310`) và tiền lệ "Có — thêm ghi chú [Amended] trỏ tới DEC-048" (`qa-log.md:1030`, QA-295).
- **Vấn đề:** Đây là cùng loại với AUD-M05-21, nay phát sinh mới do DEC-158. SR không bị ảnh hưởng.
- **Hệ quả nếu không xử lý:** Người viết SR M14, hoặc người đọc Phụ lục A, có thể lấy nhầm công thức cũ.
- **Hướng xử lý:** Stakeholder quyết (mục 6, khối 5).
- **Trạng thái:** Mở.

## 6. Cần stakeholder quyết

Vấn đề chặn được xếp trước. Các DEFECT cơ học không nằm ở đây; Author sửa thẳng các finding: AUD-M05-17, 22, 23, 25, 28, 29, 30. AUD-M05-24 chỉ cần hỏi khi Author không tự xác định được nghĩa của DEC-157.

**1. (chặn)**
Vấn đề: Khi phá hòa bằng tên theo bảng chữ cái tiếng Việt, chữ số, ký tự ngoài chữ cái và dấu thanh được xếp thế nào?
Nguồn: DEC-154 (`decisions.md:829`) "Vietnamese alphabetical order (a ă â b c d đ e ê …), case-insensitive"; OP-M05-09 (tập ký tự được phép trong tên Tag).
Lựa chọn:
- A) Chữ số 0–9 và ký tự khác đứng trước chữ cái. So chữ cái trước; nếu chữ cái giống nhau thì so dấu thanh theo thứ tự ngang, huyền, hỏi, ngã, sắc, nặng. Hệ quả: "2k8" xếp trước "anh"; "nghỉhè" xếp trước "nghĩhè".
- B) Chữ số và ký tự khác đứng sau chữ cái; dấu thanh như A. Hệ quả: Tag bằng chữ cái lên trước.
- C) Bỏ qua chữ số và ký tự khác khi so. Hệ quả: một số tên bị coi là bằng nhau, nên cần thêm tiêu chí phá hòa thứ tư.

Đề xuất: A, vì đây là quy ước quen thuộc và cho thứ tự xác định với mọi tên.
Liên quan: AUD-M05-26

**2. (chặn)**
Vấn đề: Tag chưa có bài viết nào được tính (chỉ có trên bản nháp, trong Group Private hoặc trên bài chưa công khai) có xuất hiện trong bảng xếp hạng Trending Tag không?
Nguồn: QA-235 (`qa-log.md:939`) "Không đặt ngưỡng cho MS1"; DEC-051 (`decisions.md:300`) "Auto-created, no approval"; DEC-146 (`decisions.md:797`) không tính bài trong Group Private.
Lựa chọn:
- A) Chỉ xếp hạng Tag có ít nhất một bài viết được tính, kể cả khi điểm là 0. Hệ quả: không lộ tên Tag từ bản nháp hay Group Private; vẫn không đặt ngưỡng điểm.
- B) Xếp hạng mọi Tag hoạt động, như bản 0.2 đang viết. Hệ quả: tên Tag trong bản nháp và Group Private hiện công khai với 0 điểm.
- C) Chỉ tạo Tag khi bài viết trở thành công khai. Hệ quả: đổi cả thời điểm Tag xuất hiện trong gợi ý tự hoàn thành (M06) và trong việc kiểm giới hạn Tag.

Đề xuất: A, vì cách này giữ đúng ý "không ngưỡng" mà không làm lộ nội dung không công khai.
Liên quan: AUD-M05-27

**3. (chỉ hỏi nếu Author không tự xác định được)**
Vấn đề: Câu "one record per submission" của DEC-157 có áp dụng cho lần gửi lại sau khi bài bị Mod từ chối không?
Nguồn: DEC-157 (`decisions.md:841`) "one record per submission"; QA-293 (`qa-log.md:1028`); OP-M05-10 (`ISH-SR-M05.md:596`) "Đề xuất mặc định: chỉ ghi ở lần gửi đầu tiên."
Lựa chọn:
- A) Có: mỗi lần gửi, kể cả gửi lại, ghi một phản hồi nếu gợi ý còn mới. Hệ quả: giữ 005.4, xóa OP-M05-10.
- B) Chỉ ghi ở lần gửi đầu tiên. Hệ quả: sửa 005.4, đóng OP-M05-10 theo đề xuất hiện tại.

Đề xuất: A, vì DEC-157 viết "per submission" mà không loại trừ lần gửi lại. Đây là cách đọc nghĩa đen; MERGE không suy ra được ý định của stakeholder.
Liên quan: AUD-M05-24

**4.**
Vấn đề: Module nào ghi nhận lượt mở trang chi tiết bài viết của người dùng đã đăng nhập (dữ liệu để đếm người xem cho Trending), và module nào cho Guest xem danh sách Tag?
Nguồn: DEC-158 (`decisions.md:845`) "Viewing data is recorded per view with its time"; QA-011 (`qa-log.md:134`) "CLAS: Xem danh sách Topic / Tag / Khối lớp"; DEC-151 (`decisions.md:817`).
Lựa chọn:
- A) Lượt xem ở M03, danh sách Tag ở M14/M06, như routing hiện tại. Hệ quả: SR M03 và SR M14/M06 phải nhận hai hàng R5 này.
- B) Cả hai ở M05. Hệ quả: thêm hai yêu cầu vào SR M05.
- C) Lượt xem ở M05, danh sách Tag ở M14/M06.

Đề xuất: C, vì kết quả nhìn thấy duy nhất của việc ghi nhận lượt xem là điểm Trending (M05 sở hữu theo quy tắc 4A), còn danh sách Tag gắn với việc duyệt theo Tag mà DEC-151 đã giao cho M14/M06.
Liên quan: AUD-M05-31

**5.**
Vấn đề: Có thêm nhãn [Amended] cho QA-106, QA-226, ISS-171 sau DEC-158 không?
Nguồn: `qa-log.md:745`, `qa-log.md:930`, `issue-queue.md:261`; DEC-158 (`decisions.md:845`); tiền lệ QA-295 (`qa-log.md:1030`).
Lựa chọn:
- A) Thêm nhãn trỏ tới DEC-158, không xóa chữ cũ. Hệ quả: register nhất quán, giống cách đã làm ở QA-295.
- B) Giữ nguyên. Hệ quả: SR M14 có thể trích công thức cũ.

Đề xuất: A, vì cùng loại với QA-295.
Liên quan: AUD-M05-32

## 7. Kết quả checklist

| Mã | Kết quả | AUD / ghi chú |
|---|---|---|
| CL-A01 | Đạt | P1: mọi ý của DRAFT §3.1–§3.4 và các ý liên quan M05 có chỗ đi. DRAFT §7.2 nay ở 008, 008.13 và R6 |
| CL-A02 | Đạt | Không có COV-01, INV-01; ma trận tay cho 100/100 OWNED có chỗ đi |
| CL-A03 | Không đạt | AUD-M05-17 (Sửa chưa đủ). REFERENCING 21/21 đã phân loại hợp lý |
| CL-A04 | Đạt | Không có COV-02, TRC-06; các nguồn ngoài OWNED được trích đều có thật |
| CL-A05 | Không đạt | AUD-M05-25. AUD-06, 10, 11 đã sửa |
| CL-A06 | Đạt | 22 dòng `Suy ra` được suy lại; không tạo số liệu, ngoại lệ hay quyền mới |
| CL-A07 | Đạt | Mọi con số có nguồn, gồm 2, 1, 1, 0,1 của DEC-158 |
| CL-A08 | Đạt | DRAFT §3.2, §3.4, §4.5, §7.2, §11.2 ↔ register: SR theo register, ghi cả hai nguồn, có QA đã hỏi. AUD-18 đã sửa |
| CL-A09 | Đạt | SR theo quyết định mới ở mọi chỗ register ghi rõ. AUD-02 đã giải bởi DEC-155. Có OBSERVATION AUD-M05-32 về register, không phải lỗi của SR |
| CL-A10 | Đạt | 26 mục COV-03 đã kiểm tay; DEC-145 đủ bốn hệ quả; QA-011, QA-235, DEC-158 tách đúng. AUD-03, AUD-04 đã sửa |
| CL-A11 | Không đạt | AUD-M05-26, AUD-M05-27. Bốn mơ hồ của vòng 1 (AUD-01, 14, 15, 16) đã được trả lời và SR làm theo |
| CL-B01 | Không đạt | AUD-M05-29. AUD-09 đã sửa |
| CL-B02 | Đạt | RULE-01/02/08 không báo; đọc tay đạt |
| CL-B03 | Đạt | Không có từ mơ hồ; chữ "cố định" ở 001 đã bỏ (AUD-07) |
| CL-B04 | Đạt | RULE-03 không báo |
| CL-B05 | Đạt | RULE-05 không báo; mọi chữ "đó" có danh từ đi kèm |
| CL-B06 | Đạt | RULE-06/07 không báo; chi tiết lưu lượt xem nằm ở R1 |
| CL-B07 | Đạt | RULE-09 không báo |
| CL-B08 | Đạt | P3: có ca cho mọi ID mới hoặc đổi; chỉ còn `Mơ hồ` ở A-109, A-110 do nguồn mơ hồ (GAP AUD-26). Ghi chú MERGE: cặp 007.1/011.7 cho hai "Then" và đã được chấm ở CL-C01 (AUD-M05-22) |
| CL-B09 | Đạt | Mọi giới hạn có yêu cầu từ chối, kể cả theo dõi Topic đã gộp (011.7) và gộp không hợp lệ (011.8, 011.10) |
| CL-B10 | Đạt | Mỗi cận một yêu cầu; 011.8 theo đúng câu DEC-159 |
| CL-B11 | Đạt | Mọi thao tác theo vai trò có yêu cầu quyền |
| CL-B12 | Đạt | 168 ca cho 107 yêu cầu, không có TST-01…05; đã có ca chuyển trạng thái không hợp lệ (T-136, T-137, T-161…T-168). AUD-13 đã sửa |
| CL-B13 | Không đạt | AUD-M05-26, AUD-M05-27 |
| CL-C01 | Không đạt | AUD-M05-22 (Hồi quy). AUD-07, AUD-08 đã sửa |
| CL-C02 | Không đạt | AUD-M05-28 |
| CL-C03 | Đạt | Mọi thuật ngữ ở mục 5 có trong 2.1 và ngược lại. AUD-06, AUD-20 đã sửa |
| CL-C04 | Không đạt | AUD-M05-23 (Hồi quy). AUD-09, AUD-12 đã sửa |
| CL-C05 | Đạt | 5.1 khớp module-registry, dev_priority và DEC-151; ngoại lệ P1 của 011.6, 011.7 nhất quán với 007, 008; 5.2 không có trạng thái treo. AUD-19 đã sửa |
| CL-D01 | Đạt | HDR-01…08 không báo |
| CL-D02 | Đạt | STR-01…09 không báo |
| CL-D03 | Đạt | REQ-00…04 không báo; 12 cấp trên, 107 cấp dưới |
| CL-D04 | Đạt | ID-01…06 không báo; 002.4 và 010.4 bị bỏ, có ghi Lịch sử, không bị dùng lại |
| CL-D05 | Đạt | TRC-01…05, 07, 09, 10 không báo; 17 ID mới đều có dòng Phụ lục A |
| CL-D06 | Đạt | REF-01/02 không báo; 3.2 "Không có." |
| CL-E01 | Đạt | Không có mô hình dữ liệu, NFR hay HMI trong mục 4–5 |
| CL-E02 | Đạt | Hiển thị, tìm kiếm, duyệt, thông báo, Trending Post đều ở R5; hiển thị Topic/Tag trên bài có OP-M05-12 |
| CL-E03 | Đạt | Mọi hàng R5 có module và nguồn. Có OBSERVATION AUD-M05-31. AUD-05 đã sửa |
| CL-E04 | Đạt | 4.1 "Không có."; nội dung về Guest lấy nguyên từ DEC-158 |
| CL-F01 | Không đạt | AUD-M05-24 (Hồi quy) |
| CL-F02 | Không đạt | AUD-M05-30 |
| CL-F03 | Đạt | Mọi câu trả lời vòng 2 có ID register và SR khớp |
| CL-F04 | Đạt | P3: không thấy quyết định ngầm. T-011 nay khớp DEC-156 (lớp phụ của AUD-16 đã xử lý). Ghi chú MERGE: P3 chấm mục này trước khi xét 005.4; mặt CL-F04 của 005.4 nằm trong AUD-M05-24 và phụ thuộc vào nghĩa của DEC-157 |
| CL-F05 | Đạt | Mục 1–4 không có "phải"; 3.1 đủ nguồn; TRC-11 không báo |
| CL-F06 | Đạt | Có `[Vietnamese Doc]`; tiếng Anh chỉ ở thuật ngữ đã định nghĩa |

Đủ 45 mã: P1 chấm 12, P2 chấm 27, P3 chấm 6. Không mã nào bỏ trống hoặc ghi `Không kiểm được`.

Selfcheck của Author ghi `Đạt` cho tám mục mà các lượt chấm `Không đạt`: CL-A03, CL-A05, CL-B01, CL-C01, CL-C02, CL-C04, CL-F01, CL-F02 (dẫn chứng ở mục 4 của tệp P1 và mục 7 của tệp P2).

## 8. Vòng trước (chỉ vòng 2)

| AUD vòng 1 | Trạng thái vòng 2 | Bằng chứng |
|---|---|---|
| AUD-M05-01 (GAP Cao, CL-A11) | Đã sửa (stakeholder trả lời ISS-228, DEC-154) | 2.1 "Trở thành công khai lần đầu" (`ISH-SR-M05.md:39`); "trở thành công khai lần đầu trong 7 ngày gần nhất" (`:331`, `:332`, `:341`, `:342`) |
| AUD-M05-02 (CONFLICT TB, CL-A09) | Đã sửa (ISS-229, QA-289, DEC-155) | "[Added 2026-10-05 — DEC-155]" (`decisions.md:392`); R5 M07 (`ISH-RT-M05.md:69`) |
| AUD-M05-03 (DEFECT TB, CL-A10/B13/B09) | Đã sửa; bản sửa gây hồi quy AUD-M05-22, 23 | 011.6 (`ISH-SR-M05.md:411`), 011.7 (`:412`), 008.18 (`:348`) |
| AUD-M05-04 (DEFECT TB, CL-A10) | Đã sửa; lý do cũ trong disposition chuyển vào AUD-M05-17; chủ sở hữu danh sách Tag ở AUD-M05-31 | 006.16 (`:290`), 002.10 (`:180`), R5 (`ISH-RT-M05.md:64`), OP-M05-12 |
| AUD-M05-05 (DEFECT TB, CL-E03) | Đã sửa | 008.18, 008.19 (`:348`, `:349`); R5 tách phần Trending Post (`ISH-RT-M05.md:67`) |
| AUD-M05-06 (DEFECT TB, CL-A05/B08/C03) | Đã sửa | "đang ở trạng thái kiểm duyệt bình thường (không bị gắn cờ chờ xử lý, không bị Mod ẩn)" (`:37`) |
| AUD-M05-07 (DEFECT TB, CL-B03/C01) | Đã sửa | "mà không người dùng nào thêm hay xóa được Topic" (`:140`) |
| AUD-M05-08 (DEFECT TB, CL-C01/A05) | Đã sửa | "hệ thống phải giữ nguyên trạng thái mới hoặc cũ của gợi ý đó" (`:209`) |
| AUD-M05-09 (DEFECT TB, CL-C04/B01) | Đã sửa | "Khi tác giả gửi một bài viết có gợi ý Topic còn mới, hệ thống phải ghi nhận phản hồi gợi ý Topic cho bài viết đó." (`:244`) |
| AUD-M05-10 (DEFECT TB, CL-A05/A06) | Đã sửa (ISS-233, QA-293, DEC-157) | Phụ lục A 005.1 dẫn DEC-157 (`:505`); "compares only the latest suggestion with the final selection" (`decisions.md:841`) |
| AUD-M05-11 (DEFECT TB, CL-A05) | Đã sửa | 006.12, 012.9…012.11 đổi sang `Suy ra` (`:521`, `:580`–`:582`) |
| AUD-M05-12 (DEFECT TB, CL-C04) | Đã sửa; cùng loại lỗi xuất hiện lại ở các ID mới → AUD-M05-23 | 010.4 chuyển thành 001.5 (`:154`); cấp trên 012 (`:423`) |
| AUD-M05-13 (DEFECT TB, CL-B12) | Đã sửa | T-162 (`tests-M05.md:171`), T-166 (`:175`), T-168 (`:177`); câu hỏi lộ ra đã được giải bởi DEC-159 (`decisions.md:849`) |
| AUD-M05-14 (GAP TB, CL-A11) | Đã sửa (ISS-231, DEC-154) | 008.17 (`ISH-SR-M05.md:347`) |
| AUD-M05-15 (GAP TB, CL-A11) | Đã sửa (ISS-232, DEC-154); phần nguồn còn để ngỏ → AUD-M05-26 | 2.1 (`:62`) |
| AUD-M05-16 (GAP TB, CL-A11/F04/B13) | Đã sửa (ISS-230, DEC-156) | 002.11 (`:181`); 002.6 (`:176`); T-011 (`tests-M05.md:20`) |
| AUD-M05-17 (DEFECT Thấp, CL-A03) | **Sửa chưa đủ** — mở lại | 30 mục vòng 1 nay có dòng (`disposition-M05.md:97`–`:126`); câu gộp còn ở `:69`; 26 KEYWORD và 24 CROSS chưa có dòng |
| AUD-M05-18 (DEFECT Thấp, CL-A08) | Đã sửa (ISS-234, QA-294, DEC-158) | Phụ lục A 008.13 ghi DRAFT §7.2 (`ISH-SR-M05.md:546`); R6 (`ISH-RT-M05.md:87`) |
| AUD-M05-19 (DEFECT Thấp, CL-C05) | Đã sửa | 5.2 có các hàng theo dõi (`ISH-SR-M05.md:129`–`:132`) |
| AUD-M05-20 (DEFECT Thấp, CL-C03) | Đã sửa | 2.1 "Bài viết được tính" (`:38`); Upvote cho bài viết hoặc bình luận (`:55`) |
| AUD-M05-21 (OBSERVATION Thấp, CL-A09) | Đã sửa (QA-295) | Nhãn Amended ở `glossary.md:14`, `:29`, `decisions.md:697`; câu cũ mới phát sinh sau DEC-158 → AUD-M05-32 |

Tổng: 20 Đã sửa, 1 Sửa chưa đủ, 0 Chưa sửa.

**Hồi quy mới:** AUD-M05-22, 23, 24, 25, 27, 28, 29. Bảy lỗi này nằm ở các ID mới hoặc đã đổi của bản 0.2 (011.7, 002.10, 002.11, 006.16, 005.4, 008.15, 008.19). Các lượt đã đọc lại 17 ID mới, 13 ID đổi nội dung, 2 ID bị bỏ và các yêu cầu tham chiếu chúng. Riêng AUD-M05-30 cũng do bản sửa sinh ra (Lịch sử 0.2) nhưng lượt P2 không gắn nhãn Hồi quy.

## 9. Hồ sơ xác minh

**Kiểm lại bằng chứng bằng máy (MERGE bước 2).** Một script ở scratchpad (ngoài repo) đọc ba tệp lượt và tách mọi trích đoạn dạng `"…" (`tệp:dòng`)`. Với mỗi trích đoạn, script đọc đúng dòng ghi trong tệp đích và so chuỗi con nguyên văn (trích đoạn rút gọn bằng "…" được so từng phần). Kết quả:

- Tổng 111 trích đoạn. Script xác nhận 103.
- 8 trích đoạn script tách sai: dòng có nhiều trích đoạn liền nhau, hoặc tham chiếu viết tắt `(:dòng)` trỏ về tệp nêu trước đó. Cả 8 được kiểm lại bằng `sed -n '<dòng>p' <tệp> | grep -c -F` → mỗi lệnh ra 1:
  - `glossary.md:14`, `glossary.md:29`, `decisions.md:697` (P1, AUD-21)
  - `qa-log.md:132` "POST: Xem/đọc post"
  - `decisions.md:285` "No delete." và `qa-log.md:1002` "11 giá trị cố định" (lý do P2 loại một ứng viên)
  - `ISH-SR-M05.md:62`, `:347`, `:181`, `:176`, `:39`, `:331`, `:332`, `:341`, `:342`, `:348`, `:411` (P3 mục 4)
  - `tests-M05.md:171`, `:175`, `:177`, `:20`
  - `decisions.md:849`
- **0 trích đoạn lệch. Không finding nào bị loại vì bằng chứng.**
- Số dòng của register đã dời so với vòng 1, do các dòng `[Amended]` mới chèn vào (ví dụ DEC-145: dòng 790 → 793; DEC-146: 794 → 797). Các lượt vòng 2 đều dùng số dòng mới, và script đã xác nhận các số dòng đó.

**Khẳng định vắng mặt.** Các lượt đã tìm mỗi khẳng định bằng ít nhất hai cách; kết quả ghi ở mục 4 của từng tệp lượt. Tóm tắt:

- AUD-17: script đối chiếu ID của inventory Author với SR, routing và disposition → thiếu 26 KEYWORD và 24 CROSS. Kiểm lại từng ID mẫu bằng `grep -c -F` (QA-230, DEC-025, ISS-162, QA-242, ISS-189, QA-264) → 0/0/0.
- AUD-22: `grep "danh mục Topic"` trong các dòng 298–313 → 0.
- AUD-24: tìm `lần gửi|resubmit|gửi lại` trong SR và decisions → SR chỉ có dòng 257 và 596; decisions không có DEC nào về phản hồi khi gửi lại.
- AUD-25: tìm `DEC-150|DRAFT §3.2` trên dòng 525 → 0.
- AUD-26: tìm `chữ số`, `dấu thanh`, `0–9`, `ký tự khác chữ` trong SR và routing → 0/0; tìm `digit|chữ số|numeric` trong register → chỉ có kết quả không liên quan (username).
- AUD-27: tìm `ít nhất một bài`, `chỉ gắn trên`, `Tag mới được tạo` → 0/0; tìm tag cùng `private|draft|nháp` trong register → không có quy tắc nào.
- AUD-30: tìm `mục 4|Tổng quan chức năng|5.1|Ngoại lệ` ở dòng 458 → chỉ khớp "005.1", "5.12", "5.13".
- AUD-31: tìm OP-M05 có `người xem|lượt xem|lượt mở|M03` → chỉ OP-M05-12 (về hiển thị); `grep -c "danh sách Tag"` trong SR → 0.
- AUD-32: tìm `Amended|Clarified` ở `qa-log.md:745`, `:930`, `issue-queue.md:261` → 0.

**Gộp trùng (MERGE bước 3):**
- Không có hai finding nháp nào của các lượt khác nhau trùng nguyên nhân. Các ghi chú "Chuyển lượt khác" đã được lượt nhận xử lý thành finding riêng:
  - P1 → P2 (008.15) thành P2-04.
  - P1, P2 → P3 (thứ tự chữ số, dấu thanh) thành P3-01.
  - P3 → P2 (007.1/011.7) thành P2-01.
  - P3 → P2 (OP-M05-10) thành P2-03.
  - P2 → P1 (R5 cho 002.10, 006.16) được chấm ở CL-E02.
  - P1 → P2 (mốc P1 của 011.6, 011.7) được chấm ở CL-C05.
  - P1 → P3 (bình luận được khôi phục) đã có ca A-074.
- Không gộp P2-01 với P2-02 dù cùng chạm 011.7: một bên là mâu thuẫn giữa hai yêu cầu (CL-C01, sửa 007.1), bên kia là cấp trên không bao quát (CL-C04, sửa câu cấp trên hoặc chuyển 011.7). Hai lỗi có nguyên nhân và chỗ sửa khác nhau.
- Không gộp P2-06 với P1-02: một bên là cột truy vết của 006.16, bên kia là chủ sở hữu hai hàng R5.
- P1-01 không lập ID mới: P1 xác định đây là AUD-M05-17 sửa chưa đủ (cùng nguyên nhân, cùng chỗ sửa), nên giữ ID AUD-M05-17 với trạng thái "Sửa chưa đủ".

**Mức và lớp (MERGE bước 4).** Giữ mức và lớp mà các lượt đề xuất. Mọi chỗ lệch một mức so với mặc định đều có lý do ghi trong finding: AUD-17 (TB → Thấp), AUD-22 (Cao → TB), AUD-25 (Cao → TB), AUD-26 (Cao → TB), AUD-27 (Cao → TB), AUD-29 (TB → Thấp). AUD-24 giữ lớp chính DEFECT, vì trong cả hai cách đọc DEC-157, Author đều tự sửa được; lớp phụ là GAP.

**Ánh xạ ID nháp → AUD:** P2-01→22; P2-02→23; P2-03→24; P2-06→25; P3-01→26; P3-02→27; P1-01→17 (mở lại); P2-04→28; P2-05→29; P2-07→30; P1-02→31; P1-03→32.

**Điều MERGE thấy nhưng không lượt nào chấm (không lập finding, chỉ nêu ở bàn giao):**
- P2 chuyển cho P3 câu hỏi CL-B13 "đổi tên một Topic đã bị loại khỏi danh mục" (ISH-M05-010; DEC-159 chỉ nói về gộp). P3 không dựng ca cho điểm này. Câu hỏi chưa được kiểm.
- P2 chuyển cho P1 việc routing R2 viết tắt ID "ISH-M05-004.2…4.4" (`ISH-RT-M05.md:29`). P1 không ghi nhận.
- Mặt CL-F04 của 005.4: P2 chuyển cho P3, còn P3 chấm CL-F04 mà không xét 005.4 (chuyển ngược về P2). Mặt này nằm trong AUD-M05-24 dưới dạng lớp phụ; điểm CL-F04 = Đạt là của P3.
