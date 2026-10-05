# Báo cáo audit — ISH-AUD-M05-rel2
<!-- [Vietnamese Doc] -->

| Mã báo cáo | ISH-AUD-M05-rel2 |
| --- | --- |
| SR được audit | ISH-SR-M05, phiên bản 0.6 (2026-10-05, Bản nháp) |
| Routing | ISH-RT-M05, phiên bản 0.6 (2026-10-05) |
| Vòng | rel2 (xác minh phát hành; phiên bản đã audit gần nhất: 0.5, báo cáo ISH-AUD-M05-rel1) |
| Lượt đã gộp | RELEASE (một Auditor, ngữ cảnh sạch) |
| Ngày | 2026-10-05 |
| Auditor | Agent Auditor độc lập (lượt RELEASE) |
| Kết luận | **Chưa đạt** — chuyển stakeholder quyết. `rel2` là lượt RELEASE cuối của lần phát hành này (RULES §8.6), không mở `rel3` |

## 1. Tóm tắt

Kết luận là **Chưa đạt** vì còn đúng một DEFECT mức Thấp (AUD-M05-41). Lỗi này nằm ở tệp ca kiểm của Author, không nằm ở SR hay routing.

- **SR và routing 0.6 không còn lỗi trong phần đã đổi.** Năm DEFECT còn mở của ISH-AUD-M05-rel1 (AUD-M05-35…39) đều đã sửa đúng nguyên nhân.
- **AUD-M05-40 được đóng theo RULES §3.3 hiện hành.** Báo cáo rel1 xếp điểm này là GAP. RULES được sửa sau rel1 và nay coi nguồn im lặng là OBSERVATION Thấp, không chặn kết luận. Author đã áp dụng đúng: không viết yêu cầu, không đặt `OP`, ghi loại (c) ở selfcheck.
- **Kiểm tự động:** `check_sr.py` cho 0 ERROR, 0 WARN. OWNED vẫn là 146 mục và registers không đổi kể từ rel1.
- **Phát hiện mới duy nhất (AUD-M05-41, `Hồi quy`):** bản sửa 0.6 cập nhật `tests-M05.md` chưa đủ ở hai chỗ:
  - ca chuyển trạng thái T-202 không được viết lại theo hàng 5.2 đã đổi;
  - ca mới T-212 nằm sau một dòng trống, nên rơi ra ngoài bảng ca kiểm.
- Không có finding mức Cao, Trung bình. Không có CONFLICT, GAP hay OBSERVATION cần stakeholder trả lời về nội dung.

| Lớp \ Mức | Cao | Trung bình | Thấp |
|---|---|---|---|
| DEFECT | 0 | 0 | 1 |
| CONFLICT | 0 | 0 | 0 |
| GAP | 0 | 0 | 0 |
| OBSERVATION | 0 | 0 | 0 |

Bảng đếm các finding còn mở sau lượt này: một finding mới, cộng với các finding của rel1 chưa đóng (không còn finding nào như vậy).

## 2. Phạm vi và phương pháp

- **Tệp đã đọc:**
  - `ISH-SR-M05.md` v0.6 và `routing/ISH-RT-M05.md` v0.6. Cả hai trùng hoàn toàn với `work/snapshot-ISH-SR-M05-v0.6.md` và `work/snapshot-ISH-RT-M05-v0.6.md` (`diff -q` không báo khác biệt).
  - Báo cáo gần nhất `ISH-AUD-M05-rel1.md` (phiên bản đã audit 0.5).
  - Bản chụp của phiên bản đã audit: `work/snapshot-ISH-SR-M05-v0.5.md`, `work/snapshot-ISH-RT-M05-v0.5.md`.
  - `RULES` (toàn bộ), `TPL/audit-report-template.md`, `EX/worked-example-audit.md`, `EX/worked-example-tests.md`, `TPL/audit-invocation-prompt.md`.
- **Phần đã đổi** (`diff` bản chụp v0.5 với bản hiện tại):
  - SR:
    - header phiên bản;
    - 5.2 hai hàng gợi ý (`S:130`, `S:131`);
    - 003.10, 003.12, 003.13 thêm "bài viết chưa gửi" (`S:211`, `S:213`, `S:214`);
    - 006.8 viết lại (`S:287`);
    - bỏ ID 009.3;
    - dòng Lịch sử 0.4 được bổ sung, thêm dòng 0.6 (`S:472`, `S:474`);
    - Phụ lục A: 003.10, 003.12, 003.13 thêm DEC-167, ISS-246, QA-306 (`S:507`, `S:509`, `S:510`), bỏ dòng 009.3, sửa ghi chú 010.7 (`S:584`);
    - Phụ lục B bỏ OP-M05-13, OP-M05-14, nay là `Không có.` (`S:611`).
  - Routing: header phiên bản; R5 thêm một hàng (`R:71`).
  - Không có ID mới. ID bị bỏ: ISH-M05-009.3.
  - Mục 2.1, 3.1, 4 và 5.1 không đổi.
- **Yêu cầu cùng đối tượng đã đọc thêm:** toàn bộ 5.2, 5.5 (003…003.16), 5.7 (005…005.5), 5.8 (006…006.18), 5.11 (009…009.2), 5.12; mục 2.1 (Tag, Tên Tag, Gợi ý cũ, Gửi bài viết); Phụ lục A và B.
- **Nguồn đã đọc** (registers ngày 2026-10-05, `registers_sha` `275497dc…`, không đổi so với rel1):
  - DEC-167 (`decisions.md:885`), DEC-166 (`:881`), DEC-168 (`:889`);
  - DEC-148 (`:806`), DEC-150 (`:814`), DEC-152 (`:822`), DEC-162 (`:865`), DEC-047 và DEC-051 (`:278`, `:304`);
  - ISS-246, ISS-250 (`issue-queue.md:367`, `:371`); QA-306, QA-310 (`qa-log.md:1041`, `:1045`).
- **Script đã chạy:**
  - `inventory.py` → `work/audit-inventory-M05-rel2.md/.json`;
  - `check_sr.py --inventory … --tests …` → `work/check-M05-rel2.json` (mục 3).
- **Tính độc lập:**
  - Người gọi chỉ đưa mã module, vòng, lượt, gốc repo, đường dẫn báo cáo gần nhất và phiên bản đã audit. Không nhận tóm tắt nào của Author.
  - RG-1…RG-7 được chấm bằng bằng chứng của tôi (mục 4.2). Bảng "Rà hồi quy" của Author (`selfcheck-M05.md:140–158`) chỉ được đọc sau đó để đối chiếu.
  - **Giới hạn độc lập:** tôi đã dựng các ca R2-01…R2-14 từ nguồn trước khi đọc kỹ `tests-M05.md`. Tuy vậy, trước đó tôi đã thấy một phần các dòng ca của ID đổi qua một lệnh `grep` dùng để định vị ca theo ID. Lượt RELEASE cũng phải đọc `diff` trước khi viết ca. Vì vậy ca kiểm không hoàn toàn mù với lời văn SR và ca kiểm của Author.
- **Thay đổi quy tắc giữa rel1 và rel2:**
  - `SR-DOCUMENT-RULES.md` có thời điểm sửa 2026-10-05 15:54, sau báo cáo rel1 (15:41).
  - RULES hiện hành có ba điểm liên quan trực tiếp:
    - §3.3: nguồn im lặng thì không hỏi, không đặt `OP`; Auditor chỉ ghi OBSERVATION Thấp (`RULES:138`);
    - Phụ lục B chỉ còn `OP` loại Mơ hồ hoặc Mâu thuẫn (`RULES:142`);
    - §5 mục 2: chủ sở hữu dự kiến ghi ở R5, không đặt `OP` (`RULES:260`).
  - Báo cáo này áp dụng RULES hiện hành. Hệ quả: AUD-M05-40 đổi lớp (mục 8), và việc bỏ OP-M05-13, OP-M05-14 là đúng quy tắc.
- **Giới hạn (không kiểm được):**
  - Chưa có SR của M03, M06, M07, M10, M13, M14. Hàng R5 mới (`R:71`, M07) chỉ kiểm được nguồn, chưa kiểm được việc SR M07 sẽ nhận hàng này.
  - Lượt RELEASE không chạy lại ma trận độ phủ toàn bộ và không tìm chủ động ngoài phần đã đổi (RULES §8.6). Kết quả checklist của phần không đổi giữ như các báo cáo trước.
  - "Chỉ đạo của stakeholder" nêu ở dòng Lịch sử 0.6 không có ID ở register (registers không đổi kể từ rel1). Tôi chỉ đối chiếu được chỉ đạo này với nội dung RULES §3.3 hiện hành, không đối chiếu được với một quyết định đã ghi.
- **Chênh lệch tồn kho so với rel1:**
  - OWNED 146, REFERENCING 22, CROSS 42, DRAFT 30, không đổi.
  - `registers_sha` của tôi trùng với rel1 và với `inventory-M05.json` của Author. Tập OWNED và REFERENCING trùng hoàn toàn (so bằng script).
  - Từ khóa giữ như rel1.

## 3. Kết quả kiểm tra tự động

Lệnh chạy (từ gốc repo):

```
python3 .agent-instructions/system_analysis/shared/sr-tools/inventory.py \
  --registers .agents/.claude/system_analysis/output/registers --draft docs/_temp --module M05 \
  --keywords "topic,tag,trending,chủ đề,thẻ,gợi ý,suggest,follow,theo dõi,phân loại,classification,merge,gộp,hashtag,category,chuyên mục,stale,khối lớp,grade,rename,đổi tên,follower" \
  --out .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-M05-rel2.md \
  --json .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-M05-rel2.json
→ OWNED=146 REFERENCING=22 CROSS=42 DRAFT=30

python3 .agent-instructions/system_analysis/shared/sr-tools/check_sr.py \
  --sr .agents/.claude/system_analysis/output/specs/ISH-SR-M05.md \
  --routing .agents/.claude/system_analysis/output/specs/routing/ISH-RT-M05.md \
  --inventory .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-M05-rel2.json \
  --tests .agents/.claude/system_analysis/output/specs/audit/work/tests-M05.md \
  --json .agents/.claude/system_analysis/output/specs/audit/work/check-M05-rel2.json
```

**ERROR = 0, WARN = 0, INFO = 35.** Mã thoát 0. SR có 12 yêu cầu cấp trên và 116 cấp dưới (bỏ 009.3, không thêm ID).

- **INFO COV-03 × 33:** gồm DEC-168, nay có ở Phụ lục A (007.4, 007.8, 010.7, 010.8) và ở R5 (`R:71`). Tôi kiểm tay: phần (1) và (2) của DEC-168 nằm ở SR, phần (3) (không thông báo cho tác giả) nằm ở R5. Hai phần không trùng nhau.
- **INFO COV-00:** OWNED 146; 130 mục có trong SR (rel1: 132), 49 mục có trong routing (rel1: 46).
  - Hai mục rời SR là ISS-250 và QA-310. Cả hai chỉ nói về thông báo cho tác giả (`issue-queue.md:371`, `qa-log.md:1045`) và nay nằm ở R5 (`R:71`).
- **INFO TST-00:** 209 ca cho 116 yêu cầu. Rel1 có 211 ca; 0.6 bỏ T-195, T-199, T-200 và thêm T-212.

WARN TST-03 của rel1 (T-199, T-200) đã hết vì hai ca này bị bỏ cùng OP-M05-13, OP-M05-14. Script không bắt được AUD-M05-41: dòng trống trước T-212 không làm script bỏ sót ca, và T-202 là lỗi ngữ nghĩa.

## 4. Ma trận độ phủ nguồn → yêu cầu

Ma trận đầy đủ: Không áp dụng — xác minh phát hành. Ma trận đầy đủ gần nhất là `work/coverage-M05-r2.md`, đã được cập nhật ở ISH-AUD-M05-v1 và rel1. Không có mục OWNED mới. Bảng dưới chỉ ghi các mục có chỗ đi đã đổi ở 0.6.

| Nguồn | Mong đợi (Auditor) | Thực tế (SR / routing) | Kết quả | AUD |
|---|---|---|---|---|
| DEC-167, ISS-246, QA-306 | SR: gợi ý chỉ khi soạn bài mới (003), từ chối khi bài đã gửi (003.15); các yêu cầu về gợi ý cũ và hàng 5.2 giới hạn tương ứng | 003 (`S:192`), 003.15 (`S:216`); 003.10, 003.12, 003.13 (`S:211`, `S:213`, `S:214`) và 5.2 (`S:130`, `S:131`) thêm "bài viết chưa gửi"; Phụ lục A cite DEC-167 (`S:507`, `S:509`, `S:510`) | Khớp | 35 đã sửa |
| DEC-166 (3), ISS-252, QA-312 | SR: chỉ chữ cái (kể cả có dấu), chữ số, gạch dưới; từ chối ký tự khác | 006.8 (`S:287`) | Khớp; câu chỉ đọc được một cách | 36 đã sửa |
| DEC-168 (3), ISS-250, QA-310, DEC-065 | R5 M07 (thông báo do M07 sở hữu) | R5 (`R:71`), "M07 — chưa có SR, ghi nguồn DEC-168, DEC-065"; 009.3 đã bỏ | Khớp | 37 đã sửa |
| DEC-168 (1), ISS-247, QA-307 | SR: từ chối tên rỗng | 010.7; Phụ lục A bỏ ghi chú OP-M05-13 (`S:584`) | Khớp | — |

### 4.1 Ca kiểm độc lập cho phần đã đổi (RELEASE bước 3)

Ca được dựng từ nguồn (giới hạn độc lập ở mục 2). Cột "Author" ghi ca tương ứng của Author, được đọc sau.

| ID ca | Nguồn | Loại | Given | When | Then theo nguồn | Nguồn xác định? | ID yêu cầu SR | SR xác định? | Author | Đối chiếu |
|---|---|---|---|---|---|---|---|---|---|---|
| R2-01 | DEC-167, DEC-148 | Thường | Bài chưa gửi lần nào, gợi ý còn mới | Tác giả sửa một chữ trong tiêu đề | Gợi ý thành gợi ý cũ; có cảnh báo gợi ý cũ | Có | 003.10, 003.12 | Có | T-035, T-038, T-201 | Trùng |
| R2-02 | DEC-167, DEC-162 | Vi phạm | Bài đã gửi, từng nhận gợi ý (còn mới lúc gửi), bị Mod từ chối | Tác giả sửa nội dung rồi yêu cầu gợi ý | Từ chối yêu cầu; không có cảnh báo gợi ý cũ, không có nút gợi ý lại | Có | 003.15; 003.10, 003.12, 003.13 không áp dụng (bài đã gửi) | Có | T-212 | Trùng (lỗi định dạng của T-212 ở AUD-41) |
| R2-03 | DEC-167 | Biên | Bản nháp đã lưu, chưa gửi lần nào, gợi ý cũ, 40 tiếng | Tác giả mở lại và yêu cầu gợi ý lại | Chấp nhận; nhận gợi ý mới → gợi ý còn mới | Có | 003.13, 003.4, 5.2 (`S:131`) | Có | T-040, T-203 | Trùng |
| R2-04 | DEC-167, DEC-148 | Biên | Bài gửi lần đầu khi gợi ý đã là gợi ý cũ, bị Mod từ chối | Tác giả mở sửa bài | Không có cảnh báo gợi ý cũ (gợi ý không khả dụng khi sửa bài đã gửi) | Có | 003.12 (giới hạn "chưa gửi") | Có | Không có ca riêng | Không lập finding |
| R2-05 | DEC-167, DEC-162 | Thường | Như R2-02 | Tác giả gửi lại | Không ghi thêm phản hồi gợi ý | Có | 005.5 | Có | T-170 (đã sửa) | Trùng; AUD-35 phần T-170 đã sửa |
| R2-06 | DEC-167 | Chuyển trạng thái | Hàng 5.2 "Gợi ý cũ → Gợi ý còn mới" chỉ cho bài chưa gửi | Tác giả yêu cầu gợi ý lại, nhận gợi ý mới (bài chưa gửi) | Chuyển sang gợi ý còn mới | Có | 003.4, 003.13, 5.2 | Có | T-202 (Given không nêu "chưa gửi"), T-203 | T-203 Trùng; T-202 chưa viết lại theo hàng đã đổi → AUD-41 |
| R2-07 | DEC-166 (3) | Thường | Đang gắn Tag | Nhập "xác_suất_2024" | Chấp nhận | Có | 006.8 | Có | T-187 | Trùng |
| R2-08 | DEC-166 (3), DEC-150, DEC-152 | Biên | Đang gắn Tag | Nhập "#bayes" | Chấp nhận: "#" không thuộc tên Tag ("does not count the "#" sign"; "after removing "#"") | Có | 006.8 cùng 2.1 "Tên Tag … không gồm dấu #" (`S:32`) | Có | T-185…T-189 (đều nhập dạng "#…") | Trùng |
| R2-09 | DEC-166 (3) | Vi phạm | Đang gắn Tag | Nhập "c++", "kt&pl", "bayes!", "toán😀" | Từ chối cả bốn | Có | 006.8 | Có | T-185, T-186, T-188, T-189 | Trùng |
| R2-10 | DEC-166 (3), DEC-152 | Vi phạm / Biên | Đang gắn Tag | Nhập "bay es"; nhập "  bayes  " | "bay es" bị từ chối; "  bayes  " được chấp nhận sau khi bỏ ký tự trắng ở đầu và cuối | Có | 006.8, 006.13 | Có | T-067 | Trùng |
| R2-11 | DEC-168 (3), DEC-065 | Thường | Mod M đổi Topic bài của User A | — | A không nhận thông báo; hành vi thuộc M07 | Có | R5 (`R:71`) | Không áp dụng (routing) | T-195 đã bỏ | Khớp routing |
| R2-12 | DEC-168 (1) | Vi phạm | Topic "Tin học" | Đổi tên thành "" | Từ chối | Có | 010.7 | Có | T-196 | Trùng |
| R2-13 | DEC-168 (1) | Biên | Topic "Tin học" | Đổi tên thành "   " | Nguồn im lặng (chuẩn hóa chuỗi) → loại (c) theo §3.3 | Không (im lặng) | — | Không (đúng §3.3) | T-199 đã bỏ | Không lập finding; selfcheck ghi loại (c) (`selfcheck-M05.md:97`) |
| R2-14 | DEC-166 (1), DEC-051 | Biên | Bài có 4 Tag hoạt động và "spam" bị vô hiệu hóa | Tác giả sửa bài, muốn gỡ "spam" | Nguồn im lặng → loại (c) | Không (im lặng) | — | Không (đúng §3.3) | Không có ca | AUD-40 đóng; selfcheck ghi loại (c) (`selfcheck-M05.md:138`) |

### 4.2 Quét khung hành vi (phần đã đổi) và RG-1…RG-7 do Auditor chấm

Quét bảy câu hỏi của RULES §4.7, từ nguồn, cho các tính năng có thay đổi:
- **5.5:**
  - Câu 2 (ngữ cảnh) → (a) DEC-167. Đã phản ánh ở 003, 003.15 và ở 003.10, 003.12, 003.13, 5.2.
  - Câu 5 → (a) DEC-162: không ghi thêm phản hồi khi gửi lại (005.5).
- **5.8:**
  - Câu 4 → (a) DEC-166 (3): tập ký tự (006.8).
  - Câu 5, 6 → (c): Tag bị vô hiệu hóa có hiện khi sửa bài không. Đúng §3.3, selfcheck ghi (`:138`).
- **5.11:**
  - Câu 5 → (a) DEC-168 (3): thông báo cho tác giả, M07 sở hữu, nay ở R5.
  - Câu 5 (người theo dõi Topic đích) → (c). Selfcheck ghi (`:91`).
- **5.12:**
  - Câu 4 → (a) tên rỗng, tên trùng (010.7, 010.8).
  - Câu 4 (tên chỉ gồm ký tự trắng) → (c). Selfcheck ghi (`:97`).

RG-1…RG-7 (RULES §8.5), chấm cho mọi ID và dòng đã đổi:

| ID / dòng | RG-1 | RG-2 | RG-3 | RG-4 | RG-5 | RG-6 | RG-7 |
|---|---|---|---|---|---|---|---|
| 003.10, 003.12, 003.13 | Đạt: cấp trên 003 "trong lúc soạn bài viết mới" bao quát "bài viết chưa gửi" | Đạt: so 003.4, 003.11, 003.14, 003.15, 005.2, 005.5, 2.1 "Gợi ý cũ" — không cặp nào trái nhau (mục 9, ứng viên loại) | Đạt: DEC-167 "only" có cả vế bao gồm (003, 003.13) lẫn loại trừ (003.15) | Đạt: Phụ lục B `Không có.` | Không áp dụng | Đạt: dòng 0.6 nêu AUD-35 | Đạt: T-035, T-036, T-038, T-039, T-040, T-137, T-201, T-203 thêm "(bài viết chưa gửi)"; T-212 mới |
| 5.2 hàng `S:130`, `S:131` | Không áp dụng | Đạt: trỏ 003.10, 003.4, 003.13 có thật và cùng phạm vi | Không áp dụng | Đạt | Không áp dụng | Đạt | **Không đạt:** ca chuyển trạng thái T-202 của hàng `S:131` chưa viết lại; T-212 nằm ngoài bảng (AUD-41) |
| 006.8 | Đạt: dưới 006 | Đạt: so 006.6, 006.7, 006.9, 006.13, 006.14, 006.15, 006.18 và 2.1 "Tên Tag" — không mâu thuẫn ("#" ngoài tên Tag theo 2.1) | Đạt: vế loại trừ (006.8) cùng 006.1, 006.2 | Đạt | Không áp dụng | Đạt | Đạt: T-067, T-185…T-189 vẫn hợp lệ với câu mới |
| 009.3 (bỏ) | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Đạt: `009\.3` chỉ còn ở dòng Lịch sử `S:473`, `S:474`; routing, Phụ lục A, `tests-M05.md` → 0 | Đạt: dòng 0.6 ghi bỏ ID (ID có trong bản chụp v0.5) | Đạt: T-195 đã bỏ |
| 010.7 (Phụ lục A) | Không áp dụng | Đạt: câu yêu cầu không đổi | Không áp dụng | Đạt | Đạt: `OP-M05-1[34]` chỉ còn ở dòng Lịch sử | Đạt: dòng 0.6 "010.7 chỉ từ chối tên rỗng" | Đạt: T-196; T-199 đã bỏ |
| Phụ lục B (bỏ OP-M05-13, 14) | Không áp dụng | Không áp dụng | Không áp dụng | Đạt | Đạt: không còn tham chiếu ở SR (ngoài Lịch sử), routing, `tests-M05.md` | Đạt | Đạt: T-199, T-200 đã bỏ |
| R5 hàng mới (`R:71`) | Không áp dụng | Đạt: cùng dạng hàng `R:70` (M07) | Không áp dụng | Đạt | Không áp dụng | Đạt: dòng 0.6 "R5 thêm hàng DEC-168, DEC-065 cho M07" | Không áp dụng |
| Lịch sử 0.4 (bổ sung) | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Đạt: nay nêu thay đổi R3 và 3.1 của 0.4; dòng 0.6 ghi "AUD-39: bổ sung dòng 0.4" | Không áp dụng |

RG-6 tổng thể: mọi khác biệt của `diff` v0.5 → v0.6 (SR và routing) đều có trong dòng 0.6. Cập nhật Phụ lục A đi kèm nội dung đã ghi (003.10, 003.12, 003.13, 009.3, 010.7), cùng thước với rel1.

Đối chiếu với bảng "Rà hồi quy" của Author (đọc sau):
- Ô RG-7 của dòng 003.10, 003.12, 003.13 (`selfcheck-M05.md:147`) liệt kê T-201, T-203 nhưng không nêu T-202, là ca chuyển trạng thái của hàng 5.2 đã đổi. Phần này đã nằm ở AUD-41.
- Bảng không có dòng riêng cho hàng 5.2. Đây là tệp làm việc nên không lập finding riêng.

## 5. Phát hiện

### AUD-M05-41 — Bản sửa 0.6 cập nhật `tests-M05.md` chưa đủ: T-202 không viết lại theo hàng 5.2 đã đổi; T-212 nằm ngoài bảng ca kiểm

| Lớp | DEFECT | Nhãn | Hồi quy (hàng 5.2 `S:131` đổi; ca T-212 mới) | Mức | Thấp | Checklist | CL-B12 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** `tests-M05.md:208` (T-202), `:218` (dòng trống), `:219` (T-212); 5.2 (`ISH-SR-M05.md:131`).
- **Bằng chứng trong SR:**
  - "| Gợi ý cũ | Tác giả yêu cầu gợi ý lại (bài viết chưa gửi) và nhận gợi ý mới | Gợi ý còn mới |" (`ISH-SR-M05.md:131`). Ở bản chụp v0.5, hàng này chưa có "(bài viết chưa gửi)" (`snapshot-ISH-SR-M05-v0.5.md:131`).
  - "Trong khi gợi ý Topic của bài viết chưa gửi là gợi ý cũ, hệ thống phải cho phép tác giả yêu cầu gợi ý Topic lại." (`ISH-SR-M05.md:214`)
  - "Khi tác giả yêu cầu gợi ý Topic cho một bài viết đã gửi, hệ thống phải từ chối yêu cầu đó." (`ISH-SR-M05.md:216`)
- **Bằng chứng trong tệp ca kiểm:**
  - "| T-202 | ISH-M05-003.4 | Chuyển trạng thái | Gợi ý Topic của bài viết đang là gợi ý cũ | Tác giả yêu cầu gợi ý lại và nhận gợi ý mới |" (`tests-M05.md:208`)
  - Ca anh em của cùng hàng 5.2 đã được viết lại: "(tổng tiêu đề cộng nội dung ít nhất 10 tiếng) (bài viết chưa gửi)" (`tests-M05.md:209`, T-203).
  - `sed -n 218p tests-M05.md` → dòng trống. "| T-212 | ISH-M05-003.15 | Vi phạm |" (`tests-M05.md:219`) đứng sau dòng trống đó, nên không thuộc bảng mở ở `tests-M05.md:8`.
  - Rà hồi quy của Author: "Đạt: T-035, T-036, T-038, T-040, T-137, T-201, T-203 thêm "bài viết chưa gửi"; T-212" (`selfcheck-M05.md:147`) không nêu T-202.
- **Bằng chứng trong nguồn:** "AI Topic suggestion is available only while composing a new post; it is not available when the author edits an already-submitted post" (`decisions.md:885`, DEC-167).
- **Vấn đề:**
  - RG-7 (RULES §8.5) yêu cầu viết lại ca "Chuyển trạng thái" của hàng 5.2 đã đổi. Hàng `S:131` có hai ca (T-202 cho 003.4, T-203 cho 003.13), nhưng chỉ T-203 được viết lại.
  - Given của T-202 vẫn bao cả bài đã gửi có gợi ý cũ (gợi ý thành cũ trước lần gửi đầu, rồi bài bị từ chối). Với Given đó, 003.15 từ chối yêu cầu, nên ca không còn khớp với phạm vi của hàng 5.2 mà nó kiểm.
  - RULES §11.2 quy định tệp ca kiểm là "một bảng". Dòng trống ở `:218` tách T-212, ca duy nhất kiểm việc không có cảnh báo gợi ý cũ cho bài đã gửi, ra khỏi bảng. Khi hiển thị Markdown, T-212 không xuất hiện như một hàng của bảng. `check_sr.py` vẫn đếm ca này (TST-00: 209 ca), nên script không bắt được lỗi.
- **Lý do mức:** CL-B12 mặc định Trung bình. Hạ một mức vì đây là tệp làm việc, SR và routing không sai, When của T-202 ("nhận gợi ý mới") ngầm loại trường hợp bị từ chối, và cách sửa là cơ học. Cùng thước với AUD-M05-38 ở rel1.
- **Hệ quả nếu không sửa:** Người đọc bảng ca kiểm không thấy T-212, và ca chuyển trạng thái của hàng 5.2 không phản ánh giới hạn "bài viết chưa gửi" vừa thêm.
- **Hướng xử lý (Author quyết cách viết):** Bỏ dòng trống trước T-212. Viết lại Given của T-202 theo hàng 5.2 đã đổi (bài viết chưa gửi), như đã làm với T-203.
- **Trạng thái:** Mở.

## 6. Cần stakeholder quyết

Không có GAP, CONFLICT hay OBSERVATION nào cần stakeholder trả lời về nội dung SR.

AUD-M05-41 là DEFECT cơ học trên tệp làm việc (RULES §8.4), nên không được đưa thành khối lựa chọn ở đây. Tuy vậy, vì kết luận là `Chưa đạt` và `rel2` là lượt RELEASE tối đa của lần phát hành này (RULES §8.6), stakeholder cần quyết bước tiếp theo:
- cho Author sửa AUD-M05-41 rồi chấp nhận SR 0.6 mà không chạy thêm lượt audit; hoặc
- chọn cách khác theo thẩm quyền của stakeholder.

Auditor không đề xuất mở thêm lượt.

Ba điểm nguồn im lặng đã được Author ghi loại (c) theo RULES §3.3 và không cần quyết:
- Tag bị vô hiệu hóa khi sửa bài (AUD-M05-40 cũ);
- tên Topic chỉ gồm ký tự trắng (OP-M05-13 cũ);
- thông báo cho người theo dõi Topic đích khi Mod đổi Topic (OP-M05-14 cũ).

Stakeholder chỉ xem lại các điểm này nếu muốn bổ sung nguồn.

## 7. Kết quả checklist

Lượt RELEASE chấm lại các mục chạm tới phần đã đổi (0.5 → 0.6) và các finding còn mở của ISH-AUD-M05-rel1. Mục không chạm tới phần đã đổi ghi `Không áp dụng — xác minh phát hành` kèm kết quả gần nhất.

| Mã | Kết quả | AUD / ghi chú |
|---|---|---|
| CL-A01 | Không áp dụng — xác minh phát hành | DRAFT không đổi (30 mục); các báo cáo trước Đạt |
| CL-A02 | Đạt | Không có COV-01, INV-01; OWNED 146 không đổi; ISS-250, QA-310 chuyển sang R5 (`R:71`) |
| CL-A03 | Không áp dụng — xác minh phát hành | REFERENCING 22 không đổi, trùng inventory của Author |
| CL-A04 | Đạt | Không có COV-02, TRC-06 |
| CL-A05 | Đạt | 003.10, 003.12, 003.13 (`Nói thẳng`, thêm DEC-167) khớp "only while composing a new post" (`decisions.md:885`); 006.8 khớp DEC-166 (3) (`:881`) |
| CL-A06 | Đạt | Không có `Suy ra` mới hay đổi |
| CL-A07 | Đạt | Không có số mới trong phần đã đổi |
| CL-A08 | Không áp dụng — xác minh phát hành | Không có lệch DRAFT ↔ register mới |
| CL-A09 | Đạt | Registers không đổi kể từ rel1 (`registers_sha` trùng) |
| CL-A10 | Đạt | DEC-168 tách đúng: (1), (2) ở SR, (3) ở R5 (`R:71`). AUD-37 đã sửa |
| CL-A11 | Đạt | Không có nguồn mới; ca R2-01…R2-12 xác định một kết quả |
| CL-B01 | Đạt | 006.8 mẫu `Khi …`; 003.12, 003.13 mẫu `Trong khi …`; EARS không báo |
| CL-B02 | Đạt | RULE-01/02/08 không báo; 006.8 một hành vi |
| CL-B03 | Đạt | AUD-36 đã sửa: phạm vi phủ định của 006.8 chỉ đọc được một cách |
| CL-B04 | Đạt | RULE-03 không báo |
| CL-B05 | Đạt | RULE-05 không báo |
| CL-B06 | Đạt | Phần đã đổi không có tên bảng, trường hay cơ chế |
| CL-B07 | Đạt | RULE-09 không báo |
| CL-B08 | Đạt | R2-02, R2-04 (003.x với bài đã gửi) và R2-07…R2-10 (006.8) xác định; AUD-35, AUD-36 đã sửa |
| CL-B09 | Đạt | Nhánh vi phạm đủ: 003.15, 006.8, 010.7 |
| CL-B10 | Đạt | Không có ID gộp hai giới hạn hoặc hai nhánh |
| CL-B11 | Đạt | 5.11 vẫn có 009.1 (Mod/Admin), 009.2 (từ chối người khác) |
| CL-B12 | Không đạt | AUD-M05-41 (T-202, T-212). AUD-38 đã sửa |
| CL-B13 | Đạt | Điểm (a) của phần đã đổi có yêu cầu; ba điểm (c) không viết thành yêu cầu và đã ghi ở selfcheck (`:91`, `:97`, `:138`) theo §3.3 |
| CL-C01 | Đạt | AUD-35 đã sửa; 003.10…003.15 và 5.2 không còn cặp trái nhau |
| CL-C02 | Đạt | Không trùng ý mới |
| CL-C03 | Đạt | "bài viết chưa gửi" là phần bù của "đã gửi" (đã dùng ở 002.6, 002.9, 003.15, 006.11) và dựa trên "Gửi bài viết" ở 2.1 (`S:36`); "Tên Tag" (`S:32`) dùng nhất quán ở 006.8 |
| CL-C04 | Đạt | Cấp trên 003, 006, 009 vẫn bao quát cấp dưới sau khi đổi và bỏ |
| CL-C05 | Đạt | 5.1 không đổi; 5.2 trỏ ID có thật, phạm vi khớp 003.10, 003.13 |
| CL-D01 | Đạt | HDR không báo; phiên bản 0.6 khớp dòng Lịch sử cuối |
| CL-D02 | Đạt | STR không báo |
| CL-D03 | Đạt | REQ không báo; 5.11 còn hai cấp dưới |
| CL-D04 | Đạt | Bỏ 009.3 có ghi Lịch sử, không dùng lại số; 006.8 giữ ID, đổi lời văn không đổi nghĩa |
| CL-D05 | Đạt | TRC không báo; Phụ lục A không còn dòng 009.3 |
| CL-D06 | Đạt | REF không báo |
| CL-E01 | Đạt | Phần đã đổi không có NFR, HMI hay mô hình dữ liệu |
| CL-E02 | Đạt | AUD-37 đã sửa: hành vi thông báo của M07 không còn ở SR |
| CL-E03 | Đạt | Hàng R5 mới có module và nguồn sở hữu ("M07 — chưa có SR, ghi nguồn DEC-168, DEC-065") |
| CL-E04 | Đạt | Không có luật hay số liệu tự thêm |
| CL-F01 | Đạt | Phụ lục B `Không có.` (`S:611`) |
| CL-F02 | Đạt | AUD-39 đã sửa; dòng 0.6 khớp `diff` v0.5 → v0.6 |
| CL-F03 | Đạt | Phần đã đổi chỉ dùng DEC-166, 167, 168 đã có ID register; không có quyết định chỉ tồn tại trong SR |
| CL-F04 | Đạt | Không còn `OP` mở; SR không chọn trước điểm nguồn im lặng; cột "Giả định cần thêm" đều `—` |
| CL-F05 | Đạt | 3.1 có DEC-065, DEC-166…168, ISS-207…254, QA-267…314; TRC-11 không báo |
| CL-F06 | Đạt | Có `[Vietnamese Doc]` |

Đủ 45 mã: 41 `Đạt`, 1 `Không đạt` (B12), 3 `Không áp dụng — xác minh phát hành` (A01, A03, A08). Không mục nào `Không kiểm được`.

## 8. Vòng trước (finding còn mở của ISH-AUD-M05-rel1)

| AUD | Trạng thái | Bằng chứng mới |
|---|---|---|
| AUD-M05-35 (DEFECT TB, CL-C01, CL-B12) | Đã sửa | "Khi tác giả thay đổi tiêu đề hoặc nội dung văn bản của bài viết chưa gửi sau khi nhận gợi ý Topic, hệ thống phải đánh dấu gợi ý đó là gợi ý cũ." (`ISH-SR-M05.md:211`); 003.12, 003.13 "Trong khi gợi ý Topic của bài viết chưa gửi là gợi ý cũ" (`:213`, `:214`); 5.2 (`:130`, `:131`); Phụ lục A cite DEC-167 (`:507`, `:509`, `:510`); T-170 sửa: "Như T-169, User A sửa nội dung bài viết (bài đã gửi nên không nhận được gợi ý mới)" (`tests-M05.md:179`); thêm T-212 (`:219`). Phần ca kiểm còn sót (T-202) và lỗi định dạng của T-212 lập finding mới AUD-41, không mở lại AUD-35 vì SR đã đúng |
| AUD-M05-36 (DEFECT TB, CL-B08, CL-B03) | Đã sửa | "Khi tên Tag mà tác giả nhập có ít nhất một ký tự không thuộc nhóm sau: chữ cái (kể cả chữ cái có dấu tiếng Việt), chữ số, dấu gạch dưới, hệ thống phải từ chối Tag đó." (`ISH-SR-M05.md:287`). Chỉ đọc được một cách; "#" nằm ngoài "Tên Tag" theo 2.1 (`:32`) |
| AUD-M05-37 (DEFECT TB, CL-E02, CL-A10) | Đã sửa | 009.3 bỏ, ghi ở dòng 0.6 (`ISH-SR-M05.md:474`); R5 "| DEC-168, ISS-250, QA-310, DEC-065 | Khi Mod hoặc Admin đổi Topic …" (`ISH-RT-M05.md:71`). Author chọn hướng R5; hướng `OP` Đề xuất của rel1 không còn trong RULES hiện hành (`RULES:142`, `:260`) |
| AUD-M05-38 (DEFECT Thấp, CL-B12) | Đã sửa | T-057 "Tag hiển thị là "xácsuất" (006.18)" (`tests-M05.md:66`); T-176 "Tag "c" và "c_" cùng 1 điểm" (`:185`); T-181 "Tag "_a", "1a", "a" cùng 1 điểm" (`:190`). Tên Tag đều hợp lệ theo 006.8 |
| AUD-M05-39 (DEFECT Thấp, CL-F02) | Đã sửa | Dòng 0.4 nay có "Bổ sung (AUD-39): routing R3 thêm DEC-165, QA-304 …" (`ISH-SR-M05.md:472`); dòng 0.6 ghi "AUD-39: bổ sung dòng 0.4" (`:474`) |
| AUD-M05-40 (GAP Thấp, CL-B13) | Đã sửa theo RULES §3.3 (phân loại lại) | RULES hiện hành (sửa sau rel1): nguồn im lặng thì "Author không hỏi, không viết yêu cầu, không đặt `OP` … Auditor chỉ ghi OBSERVATION mức Thấp, không lập GAP" (`RULES:138`). Author xử lý đúng: dòng 0.6 "AUD-40 (Tag bị vô hiệu hóa khi sửa bài): nguồn chưa nói, không đặc tả" (`ISH-SR-M05.md:474`); selfcheck ghi loại (c) (`selfcheck-M05.md:138`); không có yêu cầu hay `OP` mới. Theo RULES hiện hành, lớp đúng của điểm này là OBSERVATION Thấp, không chặn `Đạt`. Đóng, không đếm ở bảng mục 1 |

Tổng: 6/6 đóng (5 Đã sửa, 1 Đã sửa theo phân loại lại), 0 Sửa chưa đủ, 0 Chưa sửa.

**Hồi quy mới:** AUD-M05-41 (tệp ca kiểm). Không có hồi quy trong SR hay routing.

## 9. Hồ sơ xác minh

**Trích đoạn** (mỗi lệnh `grep -n -F` khớp đúng số dòng ghi trong báo cáo; đường dẫn tính từ `.agents/.claude/system_analysis/output/`):

- **SR (`specs/ISH-SR-M05.md`):**
  - `"của bài viết chưa gửi sau khi nhận gợi ý Topic, hệ thống phải đánh dấu gợi ý đó là gợi ý cũ."` → `:211`
  - `"Trong khi gợi ý Topic của bài viết chưa gửi là gợi ý cũ, hệ thống phải hiển thị cảnh báo gợi ý cũ cho tác giả."` → `:213`
  - `"Trong khi gợi ý Topic của bài viết chưa gửi là gợi ý cũ, hệ thống phải cho phép tác giả yêu cầu gợi ý Topic lại."` → `:214`
  - `"Khi tác giả yêu cầu gợi ý Topic cho một bài viết đã gửi, hệ thống phải từ chối yêu cầu đó."` → `:216`
  - `"| Gợi ý còn mới | Tác giả thay đổi tiêu đề hoặc nội dung văn bản của bài viết chưa gửi | Gợi ý cũ |"` → `:130`
  - `"| Gợi ý cũ | Tác giả yêu cầu gợi ý lại (bài viết chưa gửi) và nhận gợi ý mới | Gợi ý còn mới |"` → `:131`
  - `"có ít nhất một ký tự không thuộc nhóm sau: chữ cái (kể cả chữ cái có dấu tiếng Việt), chữ số, dấu gạch dưới"` → `:287`
  - `"| Tên Tag | Phần chữ của Tag, không gồm dấu #. |"` → `:32`
  - `"Gửi bài viết | Thao tác của tác giả chuyển bài viết từ bản nháp sang chờ xuất bản."` → `:36`
  - `"Gợi ý cũ | Gợi ý Topic mà sau khi nhận, tác giả đã thay đổi tiêu đề hoặc nội dung văn bản của bài viết"` → `:52`
  - `"Bổ sung (AUD-39): routing R3 thêm DEC-165, QA-304"` → `:472`
  - `"AUD-37: bỏ ID ISH-M05-009.3 (ID đã có trong bản chụp v0.5)"` → `:474`
  - `"AUD-40 (Tag bị vô hiệu hóa khi sửa bài): nguồn chưa nói, không đặc tả"` → `:474`
  - `"chỉ bài viết chưa gửi (DEC-167: gợi ý Topic chỉ khi soạn bài mới)"` → `:507`, `:509`, `:510`
  - `"| ISH-M05-010.7 | DEC-168, ISS-247, QA-307 | Nói thẳng | Từ chối tên rỗng |"` → `:584`
  - `grep -n -x "Không có."` → `:90`, `:102`, `:611` (`:611` là Phụ lục B)
- **Routing (`specs/routing/ISH-RT-M05.md`):** `"| DEC-168, ISS-250, QA-310, DEC-065 | Khi Mod hoặc Admin đổi Topic"` → `:71`
- **Bản chụp:** `"| Gợi ý cũ | Tác giả yêu cầu gợi ý lại và nhận gợi ý mới | Gợi ý còn mới |" specs/audit/work/snapshot-ISH-SR-M05-v0.5.md` → `:131`
- **Register (`registers/`):**
  - `"AI Topic suggestion is available only while composing a new post"` decisions.md → `:885`
  - `"A Tag name may contain only letters (including Vietnamese letters with diacritics), digits and the underscore"` → `:881`
  - `"The 30-character limit applies to the Tag name and does not count the "#" sign."` → `:814`
  - `"an empty name (after removing "#" and whitespace) is rejected"` → `:822`
  - `"When a Mod or Admin changes the Topics of a post, the author is not notified"` → `:889`
  - `"A suggestion becomes stale on any change to the title or the text content"` → `:806`
  - `"Feedback is recorded only on the first submission of a post"` → `:865`
  - `ISS-250` issue-queue.md → `:371`; `QA-310` qa-log.md → `:1045`; `ISS-246` → `:367`; `QA-306` → `:1041`
- **Tệp làm việc (`specs/audit/work/`):**
  - `"Như T-169, User A sửa nội dung bài viết (bài đã gửi nên không nhận được gợi ý mới)" tests-M05.md` → `:179`
  - `"User A nhập Tag "XácSuất" | Bài viết có Tag; Tag hiển thị là "xácsuất" (006.18)"` → `:66`
  - `"Tag "c" và "c_" cùng 1 điểm"` → `:185`
  - `"Tag "_a", "1a", "a" cùng 1 điểm"` → `:190`
  - `"| T-202 | ISH-M05-003.4 | Chuyển trạng thái | Gợi ý Topic của bài viết đang là gợi ý cũ | Tác giả yêu cầu gợi ý lại và nhận gợi ý mới |"` → `:208`
  - `"(tổng tiêu đề cộng nội dung ít nhất 10 tiếng) (bài viết chưa gửi)"` → `:209`
  - `sed -n 218p tests-M05.md | cat -A` → `$` (dòng trống)
  - `"| T-212 | ISH-M05-003.15 | Vi phạm |"` → `:219`
  - `"User A nhập "#xác_suất_2024""` → `:196`
  - `selfcheck-M05.md`:
    - `"Đạt: T-035, T-036, T-038, T-040, T-137, T-201, T-203 thêm "bài viết chưa gửi"; T-212"` → `:147`
    - `"Không đặc tả: khi sửa bài, tác giả có thấy và gỡ được Tag bị vô hiệu hóa không"` → `:138`
    - `"tên chỉ gồm ký tự trắng và cắt khoảng trắng đầu/cuối: nguồn chưa nói, không đặc tả"` → `:97`
    - `"thông báo "bài mới" cho người theo dõi Topic đích: nguồn chưa nói"` → `:91`
- **RULES (`.agent-instructions/system_analysis/shared/SR-DOCUMENT-RULES.md`):**
  - `"Nguồn im lặng** (số liệu"` → `:138`
  - `"Hệ quả: Phụ lục B chỉ còn"` → `:142`
  - `"ghi chủ sở hữu dự kiến ở routing R5 (không đặt `OP`"` → `:260`

**Khẳng định vắng mặt:**
- **RG-5 (009.3):**
  - `grep -n -E "009\.3"` trên SR, routing, `tests-M05.md` → chỉ `ISH-SR-M05.md:473`, `:474` (Lịch sử).
  - `grep -n -E "^\| ISH-M05-009"` → `:366`, `:376`, `:377`, `:575`, `:576`, `:577` (không còn 009.3).
- **RG-5 (OP):** `grep -n -E "OP-M05-1[34]"` trên SR, routing, `tests-M05.md` → chỉ `ISH-SR-M05.md:473`, `:474`.
- **Ca đã bỏ:** `grep -n -E "T-(195|199|200)\b"` trên `tests-M05.md` → 0. ISS-250, QA-310 trên SR → 0 (chỉ `R:71`).
- **AUD-41:**
  - `grep -n -F "(bài viết chưa gửi)" tests-M05.md` → `:44`, `:45`, `:47`, `:48`, `:49`, `:146`, `:207`, `:209`; không có `:208` (T-202).
  - `grep -c "^| T-" tests-M05.md` → 209, trùng TST-00. Script đếm cả dòng `:219` dù dòng này nằm ngoài bảng.
- **Tồn kho:** `owned`, `referencing`, `all_ids`, `next_ids` của `audit-inventory-M05-rel2.json` trùng hoàn toàn với `audit-inventory-M05-rel1.json` và `inventory-M05.json` (so bằng script). `registers_sha` `275497dc69b9…` trùng cả ba.

**Ứng viên đã cân nhắc và loại:**
- **006.8 có thể từ chối mọi Tag nhập kèm "#" (vì "#" không thuộc nhóm ký tự cho phép).** Loại: 2.1 định nghĩa "Tên Tag | Phần chữ của Tag, không gồm dấu #." (`S:32`), nên "tên Tag mà tác giả nhập" không gồm "#". Câu này khớp DEC-150 (`decisions.md:814`) và DEC-152 (`:822`); ca R2-08 xác định.
- **2.1 "Gợi ý cũ" (mọi thay đổi sau khi nhận) và 003.10 (chỉ đánh dấu với bài chưa gửi).** Loại:
  - 003.10 không phải câu "chỉ", nên không loại trừ trường hợp khác.
  - Với bài đã gửi, trạng thái gợi ý không còn hệ quả nhìn thấy được: 003.12, 003.13 giới hạn vào bài chưa gửi; 003.15 từ chối gợi ý; 005, 005.5 chỉ ghi phản hồi ở lần gửi đầu (DEC-162, `decisions.md:865`); 003.14 cho gửi trong mọi trường hợp.
  - Không có cặp yêu cầu nào cho hai kết quả quan sát được khác nhau.
- **003.11, 003.14 không giới hạn "chưa gửi".** Loại: hai yêu cầu không mâu thuẫn với 003.15 (giữ nguyên trạng thái; cho phép gửi), và Author đã nêu ở RG-2 (`selfcheck-M05.md:146`).
- **"bài viết chưa gửi" chưa có ở 2.1.** Loại: đây là phần bù của "đã gửi", vốn đã dùng ổn định từ 0.2 và đã được chấm Đạt ở các báo cáo trước. Hai cụm này đều dựa trên "Gửi bài viết" (`S:36`). Bài bị Mod từ chối là bài đã gửi, khớp nguồn "already-submitted post" (`decisions.md:885`), T-170 và T-212.
- **Hàng R5 mới ghi "bài viết do người khác viết", hẹp hơn DEC-168 "the Topics of a post".** Loại: cột Nội dung là câu tóm tắt. Trường hợp Mod đổi Topic bài của chính mình không có tác giả nào khác để thông báo, nên không có hệ quả nhìn thấy.
- **Lời văn dòng Lịch sử 0.6 "nêu rõ tập ký tự bị từ chối" (thực tế nêu tập được phép rồi từ chối phần còn lại).** Loại: cùng nghĩa, không phải thay đổi bị ghi thiếu.
- **"Chỉ đạo của stakeholder" ở dòng 0.6 không có ID register.** Loại: đây là chỉ đạo về quy trình, đã thể hiện ở RULES §3.3, không phải quyết định nghiệp vụ trong SR. Phần đã đổi không chứa quyết định nào thiếu nguồn (CL-F03). Điểm này đã ghi ở mục 2 (giới hạn).

**Mức và lớp:**
- AUD-41: CL-B12 mặc định Trung bình, hạ một mức (lý do trong finding).
- AUD-40 (rel1) đổi lớp từ GAP sang OBSERVATION Thấp theo RULES §3.3 hiện hành, và đóng vì Author đã xử lý đúng §3.3.
