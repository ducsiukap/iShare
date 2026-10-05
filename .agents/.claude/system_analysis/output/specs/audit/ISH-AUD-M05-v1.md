# Báo cáo audit — ISH-AUD-M05-v1
<!-- [Vietnamese Doc] -->

| Mã báo cáo | ISH-AUD-M05-v1 |
| --- | --- |
| SR được audit | ISH-SR-M05, phiên bản 0.3 (2026-10-05, Bản nháp) |
| Routing | ISH-RT-M05, phiên bản 0.3 (2026-10-05) |
| Vòng | v1 (đợt xác minh sau vòng 2) |
| Lượt đã gộp | VERIFY (một Auditor, ngữ cảnh sạch) |
| Ngày | 2026-10-05 |
| Auditor | Agent Auditor độc lập (lượt VERIFY) |
| Kết luận | **Chưa đạt** — chuyển stakeholder quyết; không mở thêm đợt nào (RULES §8.6) |

## 1. Tóm tắt

Kết luận là **Chưa đạt** vì còn một DEFECT mở: AUD-M05-27, mức Trung bình, trạng thái Sửa chưa đủ.
- Stakeholder đã trả lời rằng chỉ xếp hạng Tag có ít nhất một bài viết được tính (DEC-161).
- ISH-M05-008.19 mới chỉ nêu những Tag *phải có mặt* trong bảng. Chưa yêu cầu nào loại Tag chỉ gắn trên bản nháp hoặc trên bài trong Group Private, nên cách làm cũ của bản 0.2 vẫn thỏa SR 0.3.

Các điểm còn lại của bản 0.3:
- **Finding vòng 2:** 11/12 đã sửa đúng nguyên nhân. Năm câu hỏi đã được stakeholder trả lời và ghi register (DEC-160…163, QA-302); SR làm theo các câu trả lời đó, trừ phần nêu trên của 008.19.
- **Kiểm tự động:** `check_sr.py` còn 0 ERROR, 0 WARN. Mọi mục OWNED mới đều có chỗ đi.
- **Phát hiện mới:** hai phát hiện mức Thấp, đều trong phần đã đổi:
  - AUD-M05-33 (OBSERVATION): yêu cầu mới ISH-M05-010.5 suy ra việc từ chối đổi tên Topic đã bị loại bằng cách mở rộng DEC-159. DEC-159 chỉ nói về gộp.
  - AUD-M05-34 (GAP): DEC-160 và mục 2.1 chưa nói dấu thanh được so theo từng vị trí ký tự hay sau khi so hết các chữ cái của tên. Hai cách cho thứ tự khác nhau, ví dụ "ban" và "bá".
- Không có finding mức Cao.

| Lớp \ Mức | Cao | Trung bình | Thấp |
|---|---|---|---|
| DEFECT | 0 | 1 | 0 |
| CONFLICT | 0 | 0 | 0 |
| GAP | 0 | 0 | 1 |
| OBSERVATION | 0 | 0 | 1 |

Còn mở 3 finding: AUD-M05-27 (vòng 2, mở lại), AUD-M05-33 và AUD-M05-34 (mới, gắn nhãn `Hồi quy` vì nằm trong phần đã đổi).

## 2. Phạm vi và phương pháp

- **Tệp đã đọc:**
  - `ISH-SR-M05.md` v0.3 và `routing/ISH-RT-M05.md` v0.3. Cả hai trùng hoàn toàn với `work/snapshot-ISH-SR-M05-v0.3.md` và `work/snapshot-ISH-RT-M05-v0.3.md` (`diff -q` không báo khác biệt).
  - Báo cáo vòng 2: `ISH-AUD-M05-r2.md`.
  - Bản chụp của phiên bản đã audit ở vòng 2: `work/snapshot-ISH-SR-M05-v0.2.md` và `work/snapshot-ISH-RT-M05-v0.2.md`.
- **Xác định phần đã đổi:** chạy `diff` giữa snapshot v0.2 và bản hiện tại (SR và routing), rồi đối chiếu từng khác biệt với dòng Lịch sử 0.3 (`ISH-SR-M05.md:459`). Phần đã đổi gồm:
  - ID thêm: 005.5, 007.7, 010.5.
  - ID bỏ: 005.4, 008.15, 011.7.
  - ID đổi nội dung: 002, 002.11, 005, 006, 007, 007.1, 008.19.
  - Định nghĩa 2.1 "Thứ tự bảng chữ cái tiếng Việt"; 3.1; 5.1; 5.2 (`:132`).
  - Dòng Lịch sử 0.2 được bổ sung và dòng 0.3 mới.
  - Phụ lục A: các dòng 002, 005, 005.5, 006, 006.16, 007, 007.1, 007.7, 008.11, 008.12, 008.14, 008.19, 010.5. Phụ lục B: bỏ OP-M05-10.
  - Routing: R2 (`:29`), R4 (`:54`), R5 (`:64`, `:75`).
  - Đã đọc lại các yêu cầu liền kề: toàn bộ 5.4, 5.7, 5.8, 5.9, 5.10, 5.12, 5.13; 5.1; 5.2; 2.1.
- **Nguồn đã đọc:**
  - Registers ngày 2026-10-05, gồm nguyên văn của DEC-145, DEC-049, DEC-051, DEC-150, DEC-154, DEC-157…163, ISS-237…242, QA-297…302 và QA-011 (dòng 128–140).
  - Nhãn Amended của QA-106, QA-226, ISS-171.
  - `disposition-M05.md` (232 dòng), dùng để kiểm AUD-M05-17.
  - `tests-M05.md`, đọc sau khi đã dựng ca kiểm độc lập ở mục 4.
  - `selfcheck-M05.md`, đọc sau khi đã chấm.
- **Script đã chạy:** `inventory.py` cho ra `work/audit-inventory-M05-v1.md/.json`; `check_sr.py --inventory … --tests …` cho ra `work/check-M05-v1.json` (mục 3).
- **Tính độc lập:**
  - Người gọi chỉ đưa mã module, vòng, lượt, gốc repo và đường dẫn báo cáo vòng 2. Không nhận tóm tắt nào của Author.
  - Ca kiểm của phần đã đổi (mục 4) được viết từ nguồn trước khi mở `tests-M05.md`.
  - Giới hạn: báo cáo vòng 2 (bắt buộc đọc) và bản `diff` cho tôi biết lời văn SR trước khi viết ca, nên ca kiểm không hoàn toàn mù với SR.
- **Giới hạn (không kiểm được):**
  - Chưa có SR của M03, M06, M07, M10, M13, M14. Các hàng R5 (kể cả hai hàng theo DEC-163) chỉ kiểm được nguồn, chưa kiểm được việc module đích nhận hàng đó.
  - Đợt xác minh không chạy lại toàn bộ ma trận độ phủ (RULES §8.6). Riêng các mục OWNED mới đã được kiểm từng mục (mục 4).
  - Ý định của stakeholder ở AUD-M05-33 và AUD-M05-34 không suy được. Báo cáo chỉ nêu các lựa chọn.
  - Phần ngoài phạm vi thay đổi không được audit lại. Kết quả checklist của phần đó giữ nguyên như vòng 2 (mục 7).
- **Chênh lệch tồn kho so với vòng 2:**
  - OWNED tăng từ 100 lên 116, thêm DEC-160…163, ISS-237…242, QA-297…302. Không mục nào bị bỏ.
  - REFERENCING tăng từ 21 lên 22, thêm QA-235, mục này đã có trong SR.
  - `registers_sha` của tôi trùng với inventory của Author (`4d78568a…`), nghĩa là registers không đổi kể từ lúc Author bàn giao.
  - Từ khóa "grade" của tôi bắt thêm hai mục KEYWORD mà inventory của Author không có. Cả hai không liên quan đến M05 nên không lập finding:
    - DEC-014: luồng đăng ký.
    - QA-038: chu kỳ và bộ lọc của Leaderboard.

## 3. Kết quả kiểm tra tự động

Lệnh chạy (từ gốc repo):

```
python .agent-instructions/system_analysis/shared/sr-tools/inventory.py \
  --registers .agents/.claude/system_analysis/output/registers --draft docs/_temp --module M05 \
  --keywords "topic,tag,trending,chủ đề,thẻ,gợi ý,suggest,follow,theo dõi,phân loại,classification,merge,gộp,hashtag,category,chuyên mục,stale,khối lớp,grade" \
  --out .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-M05-v1.md \
  --json .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-M05-v1.json
→ OWNED=116 REFERENCING=22 CROSS=42 DRAFT=30

python .agent-instructions/system_analysis/shared/sr-tools/check_sr.py \
  --sr .agents/.claude/system_analysis/output/specs/ISH-SR-M05.md \
  --routing .agents/.claude/system_analysis/output/specs/routing/ISH-RT-M05.md \
  --inventory .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-M05-v1.json \
  --tests .agents/.claude/system_analysis/output/specs/audit/work/tests-M05.md \
  --json .agents/.claude/system_analysis/output/specs/audit/work/check-M05-v1.json
```

**ERROR = 0, WARN = 0, INFO = 29.** Mã thoát 0. Có 12 yêu cầu cấp trên và 107 cấp dưới (bỏ 3 ID, thêm 3 ID).

- **INFO COV-03 × 27:** đủ 26 mục của vòng 2, cộng mục mới DEC-163. DEC-163 nằm ở Phụ lục A dòng 008.14 (`ISH-SR-M05.md:549`) và ở hai hàng R5 (`ISH-RT-M05.md:64`, `:75`). Tôi kiểm tay hai phần này: phần SR chỉ là cách đếm người xem, phần R5 là việc ghi nhận lượt xem và "danh sách Tag", nên không trùng nhau.
- **INFO COV-00:** OWNED = 116; 102 mục có trong SR, 41 mục có trong routing.
- **INFO TST-00:** 176 ca cho 107 yêu cầu.

Không có COV-01, COV-02, INV-01 hay TST-01…05. Script không bắt được finding nào ở mục 5, vì cả ba đều là lỗi ngữ nghĩa.

## 4. Ma trận độ phủ nguồn → yêu cầu

Ma trận đầy đủ: Không áp dụng — đợt xác minh. Ma trận đầy đủ của vòng 2 nằm ở `work/coverage-M05-r2.md`. Bảng dưới chỉ ghi các mục OWNED mới và các mục có chỗ đi đã đổi.

| Nguồn | Mong đợi (Auditor) | Thực tế (SR / routing) | Kết quả | AUD |
|---|---|---|---|---|
| DEC-160, ISS-237, QA-297 | SR (2.1 và 008.11, 008.12) | 2.1 (`S:62`); Phụ lục A 008.11, 008.12 (`S:546`, `S:547`) | Khớp | 34 (nguồn còn để ngỏ) |
| DEC-161, ISS-238, QA-298 | SR: chỉ xếp hạng Tag có bài viết được tính; không ngưỡng | 008.19 (`S:349`), Phụ lục A (`S:553`) | Thiếu một phần: thiếu phần "chỉ" | 27 |
| DEC-162, ISS-239, QA-299 | SR: chỉ lần gửi đầu; gửi lại không ghi thêm | 005 (`S:244`), 005.5 (`S:257`); OP-M05-10 đã xóa | Khớp | — |
| DEC-163, ISS-240, ISS-241, QA-300, QA-301 | R5 M03 (ghi nhận lượt xem); R5 M14/M06 ("danh sách Tag"); 008.14 tham chiếu | R5 (`R:75`, `R:64`); Phụ lục A 008.14 (`S:549`) | Khớp | — |
| ISS-242, QA-302 | R4 (sửa register) | R4 (`R:54`); nhãn có ở `qa-log.md:745`, `:930`, `issue-queue.md:261` | Khớp | — |
| DEC-145 (theo dõi), QA-274 | SR 007.7 thay cho 011.7 | 007.7 (`S:314`), Phụ lục A (`S:534`) | Khớp | — |
| DEC-145, DEC-159 (đổi tên Topic đã loại) | Nguồn không nêu → hỏi hoặc OP | 010.5 `Suy ra` (`S:389`, `S:561`) | Có yêu cầu dựa trên suy luận tương tự | 33 |
| KEYWORD và CROSS-CUTTING (AUD-17) | Mỗi mục một dòng | Script đối chiếu: 282/282 mục của inventory Author có chỗ đi | Khớp | — |

### 4.1 Ca kiểm độc lập cho các yêu cầu đã đổi (VERIFY bước 3)

Các ca được viết từ nguồn. Cột "Author" ghi ca tương ứng trong `tests-M05.md`.

| ID ca | Nguồn | Loại | Given | When | Then theo nguồn | Nguồn xác định? | ID yêu cầu SR | SR xác định? | Author | Đối chiếu |
|---|---|---|---|---|---|---|---|---|---|---|
| V-01 | DEC-156 | Thường | Bản nháp chưa có Topic | Tác giả lưu bản nháp | Lưu được, bài có 0 Topic | Có | 002.11 | Có | T-139 | Trùng |
| V-02 | DEC-156, DEC-049 | Vi phạm | Bản nháp có 0 Topic | Tác giả gửi bài | Bị từ chối | Có | 002.5 | Có | T-140 | Trùng |
| V-03 | DEC-162 | Thường | Gợi ý còn mới, lần gửi đầu | Gửi bài | Có 1 phản hồi | Có | 005 | Có | T-141 | Trùng |
| V-04 | DEC-162 | Vi phạm | Như V-03, rồi bài bị Mod từ chối, tác giả không sửa | Gửi lại | Vẫn 1 phản hồi | Có | 005.5 | Có | T-169 | Trùng |
| V-05 | DEC-162 | Biên | Lần gửi đầu với gợi ý cũ (0 phản hồi); bị từ chối; tác giả yêu cầu gợi ý lại, nhận gợi ý còn mới | Gửi lại | 0 phản hồi ("only on the first submission") | Có | 005, 005.5 | Có: 005 không áp dụng vì không phải lần đầu; 005.5 cấm ghi khi gửi lại | Không có ca (T-170 chỉ có trường hợp lần đầu đã có phản hồi) | Không lập finding; có thể thêm ca |
| V-06 | DEC-051, DEC-150, QA-011 | Quyền | Bài công khai có Tag "bayes" hoạt động và "spam" bị vô hiệu hóa | Guest mở bài | Thấy "bayes", không thấy "spam" | Có | 006.16 | Có | T-143 | Trùng |
| V-07 | DEC-145 | Vi phạm | "Góc Chill" đã bị gộp | User A yêu cầu theo dõi "Góc Chill" | Bị từ chối | Có | 007.7; 007.1 không áp dụng | Có | T-161 | Trùng; hết mâu thuẫn của AUD-22 |
| V-08 | DEC-141 | Thường | "Tin học" trong danh mục, A chưa theo dõi | A theo dõi | A đang theo dõi; số người theo dõi +1 | Có | 007.1 | Có | T-075, T-171 | Trùng |
| V-09 | DEC-158 | Biên | P21 có 30 lượt mở của Guest, 0 lượt của người dùng đã đăng nhập | Tính số người xem | 0 | Có | 008.14 | Có | T-148 | Trùng |
| V-10 | DEC-158 | Công thức | B mở P21 5 lần, C mở 1 lần, tác giả mở 3 lần, đều trong 7 ngày | Tính phần điểm người xem | 2 người xem, 0,2 điểm | Có | 008.14, 008.13 | Có | T-146 | Trùng |
| V-11 | DEC-161 | Vi phạm | Tag "đềthi12a1" hoạt động, chỉ gắn trên một bản nháp và một bài trong Group Private | Xếp hạng Tag | Không có trong bảng | Có | 008.19, 008 | **Không**: 008.19 chỉ bắt buộc đưa vào Tag có bài được tính; câu cấp trên 008 xếp hạng "các Tag"; không yêu cầu nào loại Tag này | T-173: "không có" (Then lấy từ DEC-161, không từ câu SR) | Khác nguồn gốc → AUD-27 |
| V-12 | DEC-161, QA-235 | Biên | Tag "bayes" gắn trên một bài được tính, 0 điểm | Xếp hạng Tag | Có trong bảng, 0 điểm | Có | 008.19 | Có | T-173 | Trùng |
| V-13 | DEC-161 | Thời gian | "toánvui" chỉ gắn trên bài P30; P30 công khai lúc T−2 ngày, bị tác giả tự ẩn lúc T−1 giờ | Xếp hạng Tag tại T | Không có trong bảng ("currently attached") | Có | 008.19 | **Không** (cùng lý do V-11) | Không có ca | → AUD-27 |
| V-14 | DEC-161 | Công thức | Tag "anova" hoạt động, 0 điểm; Given không nói Tag có gắn trên bài được tính hay không | Xếp hạng Tag | Phụ thuộc điều kiện không có trong Given | — | 008.19 | — | T-153: "anova có trong bảng" | Ca của Author thiếu điều kiện trong Given → AUD-27 |
| V-15 | DEC-160 | Công thức | "2k8", "anh", "java", "kotlin" bằng điểm, bằng số bài mới | Xếp hạng Tag | 2k8, anh, java, kotlin | Có | 2.1, 008.12 | Có | T-174 | Trùng |
| V-16 | DEC-160 | Công thức | "nghỉhè" và "nghĩhè" bằng nhau ở hai tiêu chí đầu | Xếp hạng Tag | nghỉhè trước (hỏi trước ngã) | Có | 2.1, 008.12 | Có | T-175 | Trùng |
| V-17 | DEC-160 | Công thức | "ban" và "bá" bằng nhau ở hai tiêu chí đầu | Xếp hạng Tag | Cách 1 (so từng vị trí): vị trí 2 là "a" (ngang) và "á" (sắc), nên "ban" trước. Cách 2 (so hết chữ cái rồi mới so dấu): "ba" là tiền tố của "ban", nên "bá" trước | **Mơ hồ** | 2.1, 008.12 | Mơ hồ | Không có ca (T-176 ghi "so từng ký tự" cho ca "c"/"c++", không có dấu thanh) | → AUD-34 |
| V-18 | DEC-160, OP-M05-09 | Công thức | Nếu tên Tag được chứa "+": "c++" và "c1" bằng nhau ở hai tiêu chí đầu | Xếp hạng Tag | Thứ tự giữa "+" và "1" không được nêu | Mơ hồ (phụ thuộc OP-M05-09) | 2.1 | Mơ hồ | Không có ca | Điểm nhỏ, ghi trong AUD-34 |
| V-19 | DEC-159 (chỉ nói về gộp), DEC-049 | Vi phạm | "Góc Chill" đã bị gộp vào "Kỹ năng mềm" | Admin yêu cầu đổi tên "Góc Chill" | Nguồn không nêu. Cách 1: từ chối (coi như "không tồn tại", theo DEC-159). Cách 2: chấp nhận, nhưng không ai thấy tên mới | Không | 010.5 | Có (từ chối) | T-172 | Trùng với SR; cơ sở là suy luận → AUD-33 |

Quét khung hành vi cho phần đã đổi (bảy câu hỏi của RULES §4.7):
- 5.7: câu 2 (ngữ cảnh gửi lại) đã được DEC-162 trả lời → loại (a).
- 5.9: câu 4 (theo dõi Topic đã loại) → loại (a), DEC-145.
- 5.10: câu 4 (Tag không có bài được tính) → loại (a), DEC-161; SR mới thể hiện một phần (AUD-27). Câu 3 (thứ tự theo tên) → loại (c) còn lại (AUD-34).
- 5.12: câu 4 (đổi tên Topic đã loại) → tôi xếp loại (c), Author xếp loại (b) (`selfcheck-M05.md:167`). Xem AUD-33.

## 5. Phát hiện

Thứ tự trình bày: DEFECT Trung bình, rồi GAP Thấp, rồi OBSERVATION Thấp.

### AUD-M05-27 — ISH-M05-008.19 chưa loại Tag không gắn trên bài viết được tính khỏi xếp hạng Trending (DEC-161)

| Lớp | DEFECT | Lớp gốc (vòng 2) | GAP, đã được trả lời bởi DEC-161 | Mức | Trung bình | Checklist | CL-B08, CL-F03, CL-B12 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.19 (`ISH-SR-M05.md:349`); câu cấp trên ISH-M05-008 (`:322`); Phụ lục A (`:553`); `tests-M05.md:162` (T-153).
- **Bằng chứng trong SR:**
  - "Hệ thống phải đưa vào xếp hạng Trending mọi Tag hoạt động đang gắn trên ít nhất một bài viết được tính, mà không đặt ngưỡng điểm tối thiểu." (`ISH-SR-M05.md:349`)
  - "Hệ thống phải xếp hạng các Topic và các Tag theo điểm Trending tính trên 7 ngày gần nhất." (`ISH-SR-M05.md:322`)
  - Phụ lục A ghi đúng ý nguồn nhưng thân yêu cầu không có ý này: "chỉ Tag có ít nhất một bài viết được tính (DEC-161)" (`ISH-SR-M05.md:553`).
  - Bản 0.2: "Hệ thống phải đưa mọi Tag hoạt động vào xếp hạng Trending mà không đặt ngưỡng điểm tối thiểu." (`snapshot-ISH-SR-M05-v0.2.md:349`)
  - Ca của Author: "Tag hoạt động "anova" có điểm 0; Tag "spam" bị vô hiệu hóa" (`tests-M05.md:162`).
- **Bằng chứng trong nguồn:** "The Trending Tag ranking includes only active Tags currently attached to at least one counted post (public, not in a Private group). … This prevents Tag names used only on drafts or in Private groups from appearing publicly." (`decisions.md:859`, DEC-161)
- **Vấn đề:**
  - 008.19 bản 0.3 chỉ nêu những Tag *bắt buộc có mặt*. Không yêu cầu nào loại Tag không gắn trên bài viết được tính. Yêu cầu loại Tag duy nhất là 012.3, và nó chỉ áp cho Tag bị vô hiệu hóa (`:435`). Câu cấp trên 008 lại xếp hạng "các Tag".
  - Vì vậy, một cài đặt xếp hạng mọi Tag hoạt động (đúng cách bản 0.2 viết) vẫn thỏa SR 0.3. Ca V-11 (Tag chỉ có trên bản nháp và trong Group Private) và ca V-13 (bài duy nhất của Tag vừa bị tác giả ẩn) không suy ra được "Then" từ câu yêu cầu. "Then" của T-173 lấy từ DEC-161, không lấy từ SR.
  - Câu trả lời đã có trong register và trong Ghi chú Phụ lục A, nhưng thân SR chưa khớp (CL-F03).
  - Ca T-153 vẫn ghi "anova có trong bảng" mà không nói "anova" có gắn trên bài viết được tính hay không. Theo DEC-161, "Then" của ca này phụ thuộc vào điều kiện đó (CL-B12).
- **Lý do mức:** CL-F03 mặc định Cao. Hạ một mức vì hướng sửa đã được stakeholder quyết và Phụ lục A đã ghi đúng; chỉ còn thiếu vế loại trừ ở thân yêu cầu.
- **Hệ quả nếu không sửa:** Tên Tag chỉ dùng trong bản nháp hoặc Group Private vẫn có thể hiện công khai trên bảng Trending Tag mà cài đặt vẫn đạt SR. Đây đúng là điều DEC-161 muốn tránh.
- **Hướng xử lý (Author quyết cách viết):** Thêm vế "chỉ" hoặc một yêu cầu cấp dưới loại khỏi xếp hạng Trending các Tag không gắn trên bài viết được tính nào, kèm dòng Phụ lục A. Sửa Given của T-153 và thêm ca kiểm cho trường hợp bài viết duy nhất của Tag không còn được tính.
- **Trạng thái:** Sửa chưa đủ (mở lại từ vòng 2).

### AUD-M05-34 — Thứ tự so tên chưa nói dấu thanh được so theo từng vị trí hay sau khi so hết chữ cái của tên

| Lớp | GAP | Nhãn | Hồi quy (phần đã đổi: 2.1) | Mức | Thấp | Checklist | CL-A11 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** 2.1 "Thứ tự bảng chữ cái tiếng Việt" (`ISH-SR-M05.md:62`); ISH-M05-008.11, 008.12 (`:342`, `:343`); OP-M05-09 (`:596`).
- **Bằng chứng trong SR:**
  - "cùng chữ cái thì so dấu thanh theo thứ tự ngang, huyền, hỏi, ngã, sắc, nặng" (`ISH-SR-M05.md:62`)
  - "ký tự không phải chữ cái và chữ số (0 đến 9) đứng trước mọi chữ cái" (`ISH-SR-M05.md:62`)
  - "Đề xuất mặc định: mọi ký tự trừ ký tự trắng và dấu #." (`ISH-SR-M05.md:596`, OP-M05-09)
  - Ca của Author: "so từng ký tự; tên hết ký tự trước xếp trước" (`tests-M05.md:185`, T-176)
- **Bằng chứng trong nguồn:** "for the same base letter, tone marks sort as level, grave (huyền), hook (hỏi), tilde (ngã), acute (sắc), dot below (nặng)" và "characters that are not letters, and digits (0→9), sort before all letters" (`decisions.md:855`, DEC-160).
- **Vấn đề:** DEC-160 đã trả lời AUD-M05-26 về vị trí của chữ số và thứ tự dấu thanh. Câu "for the same base letter" vẫn đọc được theo hai cách, và hai cách cho thứ tự khác nhau (ca V-17, hai Tag "ban" và "bá" bằng điểm và bằng số bài mới):
  - **Cách 1, so từng vị trí:** ở ký tự thứ hai, "a" (ngang) đứng trước "á" (sắc), nên "ban" xếp trước. Ca T-176 của Author ngầm theo cách này.
  - **Cách 2, so hết các chữ cái trước rồi mới so dấu** (cách xếp của từ điển tiếng Việt): "ba" là tiền tố của "ban", nên "bá" xếp trước.
  - Tôi tìm trong SR, routing và register bằng các cụm "từng ký tự", "theo vị trí", "toàn bộ tên", "per character", "whole name": không có câu nào chọn giữa hai cách. Cũng không có OP nào về điểm này.
  - Điểm nhỏ (không lập finding riêng): thứ tự giữa ký tự không phải chữ cái và chữ số chưa được nêu (ca V-18, "c++" và "c1"). Điểm này chỉ phát sinh nếu OP-M05-09 cho phép ký tự như "+"; đề xuất mặc định của OP-M05-09 hiện cho phép.
- **Lý do mức:** Đây là mơ hồ về quy tắc thứ tự, không nằm trong công thức điểm, nên CL-A11 mặc định là Trung bình. Hạ một mức vì đây là tiêu chí phá hòa thứ ba, chỉ áp cho Tag, và chỉ đổi kết quả khi hai tên có cùng chữ cái tới vị trí có dấu khác nhau mà một tên còn chữ cái phía sau.
- **Hệ quả nếu không xử lý:** Hai cách cài đặt có thể cho hai thứ tự khác nhau trên bảng Trending Tag, và ca kiểm "ban"/"bá" không có một "Then" duy nhất.
- **Hướng xử lý:** Stakeholder quyết (mục 6, khối 1); có thể hỏi chung với OP-M05-09. Sau khi có câu trả lời: ghi register, bổ sung định nghĩa ở 2.1, thêm ca kiểm. Nếu chưa hỏi ngay thì ghi một `OP` ở Phụ lục B.
- **Trạng thái:** Mở.

### AUD-M05-33 — ISH-M05-010.5 suy ra việc từ chối đổi tên Topic đã bị loại bằng cách mở rộng DEC-159, trong khi DEC-159 chỉ nói về gộp

| Lớp | OBSERVATION | Nhãn | Hồi quy (ID mới 010.5) | Mức | Thấp | Checklist | CL-A06 (mặt CL-F04) |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-010.5 (`ISH-SR-M05.md:389`); Phụ lục A (`:561`); `tests-M05.md:181` (T-172); `selfcheck-M05.md:167`.
- **Bằng chứng trong SR:**
  - "Khi Mod hoặc Admin yêu cầu đổi tên một Topic đã bị loại khỏi danh mục Topic, hệ thống phải từ chối yêu cầu đó." (`ISH-SR-M05.md:389`)
  - "| ISH-M05-010.5 | DEC-145, DEC-159 | Suy ra |", với Ghi chú: Topic đã loại "được coi là "không tồn tại" (DEC-159) ⇒ không còn Topic để đổi tên" (`ISH-SR-M05.md:561`).
  - Bảng quét của Author xếp điểm này loại (b): "Đổi tên Topic đã loại bị từ chối (010.5)" (`selfcheck-M05.md:167`).
- **Bằng chứng trong nguồn:**
  - "A merge is accepted only between two different Topics that are both in the Topic catalog. If the source or the target has already been removed from the catalog (by an earlier merge), the merge is rejected and the Mod/Admin is told that the Topic does not exist." (`decisions.md:851`, DEC-159)
  - "it can no longer be selected, suggested, ranked in Trending or followed" (`decisions.md:793`, DEC-145): danh sách này không có "renamed".
  - "- Mod/admin: edit (rename) + merge. No delete." (`decisions.md:285`, DEC-049)
- **Vấn đề:**
  - RULES §4.5 chỉ cho phép suy ra "phải có A mới được B" khi một câu nguồn nêu điều kiện đó. Không câu nào nêu "đổi tên chỉ áp dụng cho Topic trong danh mục".
  - DEC-159 đặt điều kiện "both in the Topic catalog" cho **gộp**. DEC-145 liệt kê bốn việc không còn làm được với Topic nguồn, và đổi tên không có trong danh sách.
  - Vì vậy 010.5 dựa trên suy luận tương tự hơn là hệ quả logic bắt buộc. Tôi tìm `rename`/`đổi tên` cùng `removed`/`đã loại`/`đã gộp`/`merged` trong decisions.md và qa-log.md: 0 kết quả. Không có OP nào về điểm này; OP-M05-04 chỉ nói tên rỗng hoặc trùng.
  - Điểm này chính là câu hỏi CL-B13 mà MERGE vòng 2 ghi là "chưa được kiểm" (`ISH-AUD-M05-r2.md:562`).
- **Lý do xếp OBSERVATION, mức Thấp:**
  - Cách đọc của Author khớp với cách DEC-159 gọi Topic đã loại là "không tồn tại".
  - Topic đã loại không còn hiện ở đâu với người dùng (không ở danh mục, không trên bài viết, không ở Trending, không theo dõi được). Hệ quả quan sát được chỉ là phản hồi mà Mod hoặc Admin nhận được.
  - Nếu stakeholder cho rằng suy luận này không đủ, điểm này trở thành GAP chưa có OP (CL-A06, CL-F04) và Author phải hỏi hoặc ghi OP.
- **Hệ quả nếu không xử lý:** SR chứa một quy tắc từ chối mà stakeholder chưa trực tiếp quyết.
- **Hướng xử lý:** Stakeholder xác nhận (mục 6, khối 2). Nếu không xác nhận: Author đổi 010.5 sang OP loại Đề xuất ở Phụ lục B, kèm đề xuất mặc định là từ chối.
- **Trạng thái:** Mở.

## 6. Cần stakeholder quyết

Vấn đề chặn được xếp trước. AUD-M05-27 là DEFECT có hướng sửa hiển nhiên theo DEC-161, nên không nằm ở đây: Author sửa thẳng.

**1.**
Vấn đề: Khi phá hòa bằng tên, dấu thanh được so ngay tại vị trí ký tự đầu tiên khác dấu, hay chỉ sau khi đã so hết các chữ cái (không dấu) của cả tên?
Nguồn: DEC-160 (`decisions.md:855`) "for the same base letter, tone marks sort as level, grave (huyền), hook (hỏi), tilde (ngã), acute (sắc), dot below (nặng)".
Lựa chọn:
- A) So hết chữ cái của cả tên trước, chỉ khi giống hệt mới so dấu (cách xếp của từ điển tiếng Việt). Hệ quả: "bá" xếp trước "ban"; "toán" xếp trước "toanhoc".
- B) So từng vị trí; gặp chữ cái giống nhau nhưng khác dấu thì quyết ngay bằng dấu. Hệ quả: "ban" xếp trước "bá"; khớp cách ca T-176 đang viết.

Kèm câu hỏi nhỏ (chỉ cần nếu OP-M05-09 cho phép ký tự ngoài chữ và số): giữa ký tự không phải chữ cái (ví dụ "+", "&") và chữ số, nhóm nào đứng trước?

Đề xuất: A, vì đây là thứ tự người đọc tiếng Việt quen dùng. Câu hỏi nhỏ: ký tự khác đứng trước chữ số, theo cách nguồn liệt kê "characters that are not letters, and digits".
Liên quan: AUD-M05-34

**2.**
Vấn đề: Mod hoặc Admin yêu cầu đổi tên một Topic đã bị gộp (đã bị loại khỏi danh mục) thì hệ thống từ chối hay chấp nhận?
Nguồn: DEC-159 (`decisions.md:851`) chỉ nói về gộp: "the merge is rejected and the Mod/Admin is told that the Topic does not exist"; DEC-145 (`decisions.md:793`) không nhắc đổi tên.
Lựa chọn:
- A) Từ chối, như ISH-M05-010.5 đang viết. Hệ quả: nhất quán với việc coi Topic đã loại là "không tồn tại"; cần xác nhận này làm nguồn.
- B) Chấp nhận. Hệ quả: tên mới không hiện ở đâu với người dùng; phải bỏ 010.5.

Đề xuất: A, vì cách này nhất quán với DEC-159 và không làm Topic đã loại hiện lại.
Liên quan: AUD-M05-33

## 7. Kết quả checklist

Đợt xác minh chấm lại các mục chạm tới phần đã đổi và các finding còn mở của vòng 2. Mục không chạm tới phần đã đổi ghi `Không áp dụng — đợt xác minh` kèm kết quả vòng 2.

| Mã | Kết quả | AUD / ghi chú |
|---|---|---|
| CL-A01 | Không áp dụng — đợt xác minh | DRAFT không đổi (30 mục, như vòng 2); vòng 2 Đạt |
| CL-A02 | Đạt | Không có COV-01, INV-01; 16 mục OWNED mới đều có chỗ đi (mục 4) |
| CL-A03 | Đạt | AUD-M05-17 đã sửa: câu gộp đã bỏ; 282/282 mục trong inventory của Author có dòng ở SR, routing hoặc disposition; bốn lý do cũ đã cập nhật |
| CL-A04 | Đạt | Không có COV-02, TRC-06 |
| CL-A05 | Đạt | Các dòng `Nói thẳng` đã đổi (002, 005, 005.5, 007, 007.1, 007.7, 008.11, 008.12, 008.14, 008.19) khớp nguyên văn nguồn. Phần thiếu của 008.19 chấm ở CL-B08. AUD-25 đã sửa |
| CL-A06 | Đạt | 006.16 suy ra hợp lệ (DEC-051 "hidden from display", DEC-150 "shows again"). 010.5: OBSERVATION AUD-M05-33 |
| CL-A07 | Đạt | Số mới (0–9; 1; 3; 5) đều có trong DEC-160, DEC-162 |
| CL-A08 | Không áp dụng — đợt xác minh | Không có lệch DRAFT ↔ register mới; vòng 2 Đạt |
| CL-A09 | Đạt | AUD-M05-32 đã sửa (QA-302; nhãn ở `qa-log.md:745`, `:930`, `issue-queue.md:261`); DEC-160…163 là Clarified, SR theo bản mới |
| CL-A10 | Đạt | DEC-163 tách đúng: 008.14 ở SR, phần ghi nhận lượt xem và "danh sách Tag" ở R5 |
| CL-A11 | Không đạt | AUD-M05-34. AUD-26, AUD-27 (phần mơ hồ) đã được trả lời |
| CL-B01 | Đạt | 002.11, 005, 005.5, 007.7, 010.5 đúng mẫu `Khi …`. AUD-29 đã sửa |
| CL-B02 | Đạt | RULE-01/02/08 không báo; các câu đổi chỉ có một hành vi |
| CL-B03 | Đạt | Không có từ mơ hồ trong các câu đổi |
| CL-B04 | Đạt | RULE-03 không báo |
| CL-B05 | Đạt | RULE-05 không báo |
| CL-B06 | Đạt | Không có tên bảng hay cơ chế trong các câu đổi |
| CL-B07 | Đạt | RULE-09 không báo |
| CL-B08 | Không đạt | AUD-M05-27 (ca V-11, V-13). Các yêu cầu đổi khác đều viết được ca có một "Then" (mục 4.1) |
| CL-B09 | Đạt | Nhánh vi phạm có đủ: 005.5, 007.7, 010.5, 002.5 cho bản nháp |
| CL-B10 | Đạt | Cấp trên 002 nêu "từ 1 đến 3", và mỗi cận có yêu cầu cấp dưới (002.5, 002.7, 002.8) |
| CL-B11 | Đạt | 010.5 và 007.7 nêu vai trò; quyền không đổi |
| CL-B12 | Không đạt | AUD-M05-27 (Given của T-153 chưa đủ theo 008.19 mới). Mọi ID mới có ca (T-161, T-169…T-176); không có TST-01…05 |
| CL-B13 | Đạt | Phần đã đổi: các điểm loại (a) đã thành yêu cầu; điểm loại (c) còn lại ở AUD-34 (chấm CL-A11) và AUD-33 (OBSERVATION) |
| CL-C01 | Đạt | AUD-M05-22 đã sửa: 007/007.1 giới hạn vào danh mục, 007.7 từ chối. Cặp 010/010.5 cùng dạng với 011/011.8, mà vòng 2 đã chấp nhận ("đổi tên" so với "yêu cầu đổi tên") |
| CL-C02 | Đạt | AUD-M05-28 đã sửa (008.15 bỏ); 005.5 không trùng câu cấp trên 005 |
| CL-C03 | Đạt | Không có thuật ngữ mới ngoài 2.1 |
| CL-C04 | Đạt | AUD-M05-23 đã sửa: cấp trên 002, 006 bao quát soạn và hiển thị; 011.7 chuyển thành 007.7 |
| CL-C05 | Đạt | 5.1 bỏ ngoại lệ của 011.7 (007.7 thuộc tính năng P1); 5.2 (`:132`) trỏ 007.7, 011.8 |
| CL-D01 | Đạt | HDR-01…08 không báo; phiên bản 0.3 khớp Lịch sử |
| CL-D02 | Đạt | STR-01…09 không báo |
| CL-D03 | Đạt | REQ-00…04 không báo |
| CL-D04 | Đạt | Bỏ 005.4, 008.15, 011.7, có ghi Lịch sử và không dùng lại. ID mới lấy số kế tiếp chưa dùng (005.5, 007.7, 010.5; 010.4 đã bỏ ở 0.2 và không bị dùng lại) |
| CL-D05 | Đạt | TRC-01…05, 07, 09, 10 không báo |
| CL-D06 | Đạt | REF-01/02 không báo |
| CL-E01 | Đạt | Phần đã đổi không có NFR, HMI hay mô hình dữ liệu |
| CL-E02 | Đạt | Ghi nhận lượt xem ở R5 M03 theo DEC-163 |
| CL-E03 | Đạt | AUD-M05-31 đã sửa (DEC-163); R2 (`R:29`) ghi đủ ID |
| CL-E04 | Đạt | Không có luật hay số liệu tự thêm |
| CL-F01 | Đạt | AUD-M05-24 đã sửa: OP-M05-10 đã xóa; 10 OP còn mở đều có loại và trạng thái |
| CL-F02 | Đạt | AUD-M05-30 đã sửa (bổ sung vào dòng 0.2, `:458`). Dòng 0.3 (`:459`) khớp `diff`; phần cập nhật Phụ lục A đi kèm nội dung đã đổi, cùng thước với vòng 2 |
| CL-F03 | Không đạt | AUD-M05-27: SR chưa khớp đủ DEC-161. DEC-160, 162, 163 và QA-302 khớp |
| CL-F04 | Đạt | Mặt CL-F04 của 005.4 đã giải bởi DEC-162. 010.5: xem AUD-M05-33 |
| CL-F05 | Đạt | 3.1 có DEC-140…163, ISS-207…242, QA-267…302; TRC-11 không báo |
| CL-F06 | Đạt | Có `[Vietnamese Doc]` |

Đủ 45 mã. Có hai mục `Không áp dụng — đợt xác minh` (A01, A08); không mục nào `Không kiểm được`.

Selfcheck của Author ghi `Đạt` cho ba mục mà tôi chấm `Không đạt`:
- CL-A11 (`selfcheck-M05.md:22`)
- CL-B12
- CL-F03

## 8. Vòng trước (finding còn mở của vòng 2)

| AUD vòng 2 | Trạng thái | Bằng chứng mới |
|---|---|---|
| AUD-M05-17 (DEFECT Thấp, CL-A03) | Đã sửa | Câu gộp đã bỏ, thay bằng mục "### Mục KEYWORD và CROSS-CUTTING còn lại (thêm ở v0.3, AUD-M05-17)" (`disposition-M05.md:138`). Script đối chiếu cho 0 mục thiếu, kể cả 26 KEYWORD và 24 CROSS mà vòng 2 liệt kê. Bốn lý do cũ đã cập nhật (`:54`, `:73`, `:80`, `:94`) |
| AUD-M05-22 (DEFECT TB, CL-C01) | Đã sửa | "theo dõi một Topic trong danh mục Topic mà người dùng đó chưa theo dõi" (`ISH-SR-M05.md:308`); cấp trên (`:298`) |
| AUD-M05-23 (DEFECT TB, CL-C04) | Đã sửa | Cấp trên 002 (`:162`) và 006 (`:265`) nêu "từ lúc soạn đến lúc hiển thị bài viết"; 011.7 bỏ, thành 007.7 (`:314`) |
| AUD-M05-24 (DEFECT TB, CL-F01) | Đã sửa (ISS-239, QA-299, DEC-162) | "Khi tác giả gửi lần đầu một bài viết có gợi ý Topic còn mới" (`:244`); 005.5 (`:257`); OP-M05-10 chỉ còn được nhắc ở Lịch sử (`:459`) |
| AUD-M05-25 (DEFECT TB, CL-A05) | Đã sửa | "| ISH-M05-006.16 | DEC-051, DEC-150, QA-011 | Suy ra |" (`:526`) |
| AUD-M05-26 (GAP TB, CL-A11) | Đã sửa (ISS-237, QA-297, DEC-160); phần nguồn còn để ngỏ → AUD-M05-34 | 2.1 (`:62`); T-174, T-175 |
| AUD-M05-27 (GAP TB, CL-A11) | **Sửa chưa đủ**: stakeholder đã trả lời (DEC-161) nhưng SR chỉ ghi vế "đưa vào", chưa ghi vế "chỉ" | 008.19 (`:349`); mục 5 |
| AUD-M05-28 (DEFECT Thấp, CL-C02) | Đã sửa | 008.15 bỏ; trích đoạn "Guest views are not counted" chuyển vào Phụ lục A 008.14 (`:549`) |
| AUD-M05-29 (DEFECT Thấp, CL-B01) | Đã sửa | "Khi tác giả lưu bản nháp của một bài viết chưa có Topic nào, hệ thống phải chấp nhận việc lưu bản nháp đó." (`:181`) |
| AUD-M05-30 (DEFECT Thấp, CL-F02) | Đã sửa | Dòng 0.2 thêm "Mục 4: Topic "11 lĩnh vực chốt sẵn…"… Mục 5.1… Mục 5.2…" (`:458`) |
| AUD-M05-31 (OBSERVATION Thấp, CL-E03) | Đã sửa (ISS-240, ISS-241, QA-300, QA-301, DEC-163) | R5 lượt xem → M03 (`ISH-RT-M05.md:75`); "danh sách Tag" cho Guest → Trending Tag và duyệt theo Tag (`:64`) |
| AUD-M05-32 (OBSERVATION Thấp, CL-A09) | Đã sửa (ISS-242, QA-302) | "[Amended 2026-10-05 — DEC-158" ở `qa-log.md:745`, `:930`, `issue-queue.md:261`; R4 (`ISH-RT-M05.md:54`) |

Tổng: 11 Đã sửa, 1 Sửa chưa đủ, 0 Chưa sửa.

**Hồi quy mới:** AUD-M05-33 (010.5) và AUD-M05-34 (2.1). Hai điểm MERGE vòng 2 ghi "chưa được kiểm" nay đã có kết quả:
- "Đổi tên Topic đã bị loại": Author xử lý bằng 010.5, tôi đánh giá ở AUD-M05-33.
- R2 viết tắt ID: đã sửa ở `ISH-RT-M05.md:29`.

## 9. Hồ sơ xác minh

**Trích đoạn (`grep -n -F`, mỗi lệnh khớp đúng số dòng ghi trong báo cáo):**

- **SR:**
  - `"mọi Tag hoạt động đang gắn trên ít nhất một bài viết được tính" ISH-SR-M05.md` → `:349`
  - `"Hệ thống phải xếp hạng các Topic và các Tag theo điểm Trending" ISH-SR-M05.md` → `:322`
  - `"chỉ Tag có ít nhất một bài viết được tính (DEC-161)" ISH-SR-M05.md` → `:553`
  - `"cùng chữ cái thì so dấu thanh theo thứ tự ngang, huyền, hỏi, ngã, sắc, nặng" ISH-SR-M05.md` → `:62`
  - `"Đề xuất mặc định: mọi ký tự trừ ký tự trắng và dấu #." ISH-SR-M05.md` → `:596`
  - `"yêu cầu đổi tên một Topic đã bị loại khỏi danh mục Topic" ISH-SR-M05.md` → `:389`
  - `"| ISH-M05-010.5 | DEC-145, DEC-159 | Suy ra |" ISH-SR-M05.md` → `:561`
  - `"| ISH-M05-006.16 | DEC-051, DEC-150, QA-011 | Suy ra |" ISH-SR-M05.md` → `:526`
  - `"Trong khi một Tag bị vô hiệu hóa, hệ thống phải loại Tag đó khỏi xếp hạng Trending." ISH-SR-M05.md` → `:435`
- **Register (`decisions.md`):**
  - `"includes only active Tags currently attached to at least one counted post"` → `:859`
  - `"for the same base letter, tone marks sort as level"` → `:855`
  - `"A merge is accepted only between two different Topics that are both in the Topic catalog."` → `:851`
  - `"it can no longer be selected, suggested, ranked in Trending or followed"` → `:793`
  - `"Mod/admin: edit (rename) + merge. No delete."` → `:285`
  - `"Feedback is recorded only on the first submission of a post"` → `:863`
- **Tệp làm việc:**
  - `"Tag hoạt động "anova" có điểm 0" tests-M05.md` → `:162`
  - `"so từng ký tự; tên hết ký tự trước xếp trước" tests-M05.md` → `:185`
  - `"Admin D yêu cầu đổi tên "Góc Chill"" tests-M05.md` → `:181`
  - `"Hệ thống phải đưa mọi Tag hoạt động vào xếp hạng Trending mà không đặt ngưỡng điểm tối thiểu." snapshot-ISH-SR-M05-v0.2.md` → `:349`
  - `"Đổi tên Topic đã loại bị từ chối (010.5)" selfcheck-M05.md` → `:167`
  - `"### Mục KEYWORD và CROSS-CUTTING còn lại (thêm ở v0.3, AUD-M05-17)" disposition-M05.md` → `:138`
  - Các dòng `:94`, `:80`, `:54`, `:73` của `disposition-M05.md` đều khớp.

**Khẳng định vắng mặt:**
- **AUD-27:**
  - `grep -n -E "chỉ đưa|chỉ xếp hạng|không đưa vào xếp hạng|ít nhất một bài"` trên SR và routing → chỉ `S:349` (thân 008.19, không có "chỉ") và `S:553` (Phụ lục A).
  - `grep -n "khỏi xếp hạng Trending" ISH-SR-M05.md` → chỉ `:412` (011.6, Topic nguồn) và `:435` (012.3, Tag bị vô hiệu hóa).
- **AUD-34:**
  - `grep -n -i -E "từng ký tự|theo vị trí|toàn bộ tên|cả tên|so chữ cái trước"` trên SR và routing → 0.
  - `grep -n -i -E "character by character|per character|whole name|position"` trên register → chỉ `decisions.md:855` ("Latin-alphabet positions", không liên quan).
  - `grep -n -E "giữa chữ số và ký tự|ký tự khác và chữ số" ISH-SR-M05.md` → 0.
- **AUD-33:**
  - `grep -n -i -E "rename|đổi tên"` trên decisions.md và qa-log.md, lọc tiếp bằng `removed|đã loại|đã gộp|merged` → 0.
  - `grep -n -E "OP-M05.*(đổi tên|010)" ISH-SR-M05.md` → chỉ `:591` (OP-M05-04: tên rỗng hoặc trùng).
- **AUD-17:**
  - Một script ở scratchpad đọc 282 ID dòng của `inventory-M05.md` (Author) và tìm từng ID, có mở rộng dải "…" và danh sách rút gọn, trong SR, routing và disposition → 0 thiếu.
  - Inventory của tôi có thêm DEC-014 và QA-038 (từ khóa "grade"). Tôi đọc tiêu đề của hai mục này: không liên quan đến M05.
- **ID đã bỏ:** `grep -n -E "011\.7|005\.4|008\.15|OP-M05-10"` trên SR, routing và tests → chỉ dòng Lịch sử (`:458`, `:459`) và Phụ lục A 007.7 ("thay cho ISH-M05-011.7 đã bỏ", `:534`). `tests-M05.md` → 0. `selfcheck-M05.md` còn nhắc 011.7 như hiện hành ở `:21`, `:40`. Đây là tệp làm việc nên không lập finding.

**Ứng viên đã cân nhắc và loại:**
- **CL-F02, Lịch sử 0.3 không liệt kê cập nhật nguồn ở Phụ lục A** (thêm DEC-145 cho 007/007.1, DEC-160 cho 008.11/008.12, DEC-163 cho 008.14) và việc mở rộng dải nguồn ở 3.1. Loại vì đây là cập nhật đi kèm nội dung đã ghi ở Lịch sử, và vòng 2 dùng cùng thước này.
- **CL-C01, cặp 010/010.5.** Loại vì cùng dạng với cặp 011/011.8 mà vòng 2 đã chấp nhận.
- **CL-B08, ca V-05** (lần gửi đầu không có phản hồi, gửi lại với gợi ý còn mới). Loại vì 005.5 cấm ghi khi gửi lại, nên SR vẫn xác định được kết quả.
- **5.2 không có hàng cho 010.5.** Loại vì từ chối đổi tên không làm đổi trạng thái của Topic.

**Mức và lớp:**
- AUD-27 đổi lớp từ GAP sang DEFECT, vì câu hỏi đã được trả lời và việc còn lại là Author sửa. Mức hạ từ Cao (CL-F03) xuống Trung bình, lý do ghi trong finding.
- AUD-34: CL-A11 với mơ hồ ngoài công thức có mặc định Trung bình; hạ xuống Thấp.
- AUD-33: xếp OBSERVATION Thấp, lý do ghi trong finding.
