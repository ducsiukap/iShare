# Báo cáo audit — ISH-AUD-M05-rel1
<!-- [Vietnamese Doc] -->

| Mã báo cáo | ISH-AUD-M05-rel1 |
| --- | --- |
| SR được audit | ISH-SR-M05, phiên bản 0.5 (2026-10-05, Bản nháp) |
| Routing | ISH-RT-M05, phiên bản 0.5 (2026-10-05) |
| Vòng | rel1 (xác minh phát hành; phiên bản đã audit gần nhất: 0.3, báo cáo ISH-AUD-M05-v1) |
| Lượt đã gộp | RELEASE (một Auditor, ngữ cảnh sạch) |
| Ngày | 2026-10-05 |
| Auditor | Agent Auditor độc lập (lượt RELEASE) |
| Kết luận | **Chưa đạt** — chuyển stakeholder quyết; chỉ chạy `rel2` khi stakeholder cho sửa tiếp (RULES §8.6) |

## 1. Tóm tắt

Kết luận là **Chưa đạt** vì còn ba DEFECT mức Trung bình và hai DEFECT mức Thấp, cả năm đều nằm trong phần đã đổi từ 0.3 đến 0.5 (nhãn `Hồi quy`).

- **Ba finding còn mở của ISH-AUD-M05-v1 đều đã sửa đúng nguyên nhân:** AUD-M05-27 (thêm 008.20 theo DEC-161), AUD-M05-33 (DEC-165, 010.5 đổi sang `Nói thẳng`, thêm 010.6), AUD-M05-34 (DEC-164, 2.1 viết lại theo hai bước).
- **Kiểm tự động:** `check_sr.py` cho 0 ERROR, 2 WARN (TST-03 ở T-199, T-200, đã có OP-M05-13, OP-M05-14 và được Author giải thích). 30 mục OWNED mới (DEC-164…169, ISS-243…254, QA-303…314) đều có chỗ đi.
- **Phát hiện mới quan trọng nhất (AUD-M05-35):** yêu cầu mới 003.15 (DEC-167: không gợi ý Topic khi sửa bài đã gửi) va với các yêu cầu cũ về gợi ý cũ 003.10, 003.12, 003.13 và hàng 5.2, vốn không giới hạn vào lúc soạn bài mới. Ca T-170 của Author vẫn cho tác giả nhận gợi ý mới sau khi bài bị từ chối.
- **Các phát hiện mới khác:** câu 006.8 viết lại đọc được theo hai cách, một cách từ chối cả chữ số và dấu gạch dưới (AUD-M05-36); 009.3 viết hành vi thông báo của M07 ở M05 mà không có hàng R5 hay OP chủ sở hữu (AUD-M05-37); ca kiểm cũ dùng tên Tag mà 006.8 mới từ chối (AUD-M05-38); dòng Lịch sử 0.4 thiếu thay đổi routing R3 (AUD-M05-39); và một điểm nguồn im lặng do 006.17 mở ra: Tag bị vô hiệu hóa còn chiếm chỗ trong giới hạn 5 nhưng bị ẩn, tác giả có thấy và gỡ được khi sửa bài không (AUD-M05-40, GAP).
- Không có finding mức Cao. Không có CONFLICT.

| Lớp \ Mức | Cao | Trung bình | Thấp |
|---|---|---|---|
| DEFECT | 0 | 3 | 2 |
| CONFLICT | 0 | 0 | 0 |
| GAP | 0 | 0 | 1 |
| OBSERVATION | 0 | 0 | 0 |

Còn mở 6 finding, đều mới (AUD-M05-35…40). Chờ stakeholder: 1 GAP (AUD-M05-40), cộng hai OP Author đã mở ở Phụ lục B (OP-M05-13, OP-M05-14), không phải finding.

## 2. Phạm vi và phương pháp

- **Tệp đã đọc:**
  - `ISH-SR-M05.md` v0.5 và `routing/ISH-RT-M05.md` v0.5. Cả hai trùng hoàn toàn với `work/snapshot-ISH-SR-M05-v0.5.md` và `work/snapshot-ISH-RT-M05-v0.5.md` (`diff -q` không báo khác biệt).
  - Báo cáo gần nhất `ISH-AUD-M05-v1.md` (phiên bản đã audit 0.3).
  - Bản chụp của phiên bản đã audit: `work/snapshot-ISH-SR-M05-v0.3.md`, `work/snapshot-ISH-RT-M05-v0.3.md`; thêm các bản chụp trung gian v0.4 để đối chiếu từng dòng Lịch sử 0.4 và 0.5.
  - `RULES` (`SR-DOCUMENT-RULES.md`, toàn bộ), `TPL/audit-report-template.md`, `EX/worked-example-audit.md`, `EX/worked-example-tests.md`.
- **Xác định phần đã đổi** (`diff` v0.3 → hiện tại, rồi tách v0.3 → v0.4 → v0.5 để đối chiếu với từng dòng Lịch sử):
  - 0.4: thêm 008.20, 010.6; 010.5 đổi cơ sở sang `Nói thẳng` (DEC-165); 2.1 "Thứ tự bảng chữ cái tiếng Việt" (DEC-164); 3.1; Phụ lục A 008.11, 008.12, 008.20, 010.5, 010.6; routing R3 (`R:42`).
  - 0.5: thêm 003.15, 003.16, 006.17, 006.18, 007.8, 009.3, 010.7, 010.8; đổi nội dung 006.8, 007.4; đổi diễn đạt 006.15, 008.5, 008.6, 008.7, 008.17; 2.1 thêm ba thuật ngữ tài khoản; Lý do 5.10; 3.1; Phụ lục A tương ứng; Phụ lục B xóa OP-M05-01, 02, 04…09, 11, 12 và thêm OP-M05-13, 14; routing R2 (`R:28`), R4 (`R:56`).
  - Không có ID bị bỏ ở 0.4 và 0.5.
  - Đã đọc thêm mọi yêu cầu cùng đối tượng: toàn bộ 5.2, 5.5, 5.7, 5.8, 5.9, 5.10, 5.11, 5.12, 5.13, 5.14; 2.1; 5.1; Phụ lục A, B.
- **Nguồn đã đọc:** registers ngày 2026-10-05, nguyên văn DEC-164…169 (`decisions.md:872–894`), ISS-243…254 (`issue-queue.md:364–375`), QA-303…314 (`qa-log.md:1038–1049`); các nhãn Clarified mới ở DEC-047 (`:279`), DEC-051 (`:302`), DEC-160 (`:857`); DEC-018, DEC-019, DEC-085 (định nghĩa tài khoản); DEC-050, DEC-144, DEC-148, DEC-155, DEC-065 (liên quan các finding).
- **Script đã chạy:** `inventory.py` → `work/audit-inventory-M05-rel1.md/.json`; `check_sr.py --inventory … --tests …` → `work/check-M05-rel1.json` (mục 3).
- **Tính độc lập:**
  - Người gọi chỉ đưa mã module, vòng, lượt, gốc repo, đường dẫn báo cáo gần nhất và phiên bản đã audit. Không nhận tóm tắt nào của Author.
  - Ca kiểm của phần đã đổi (mục 4.1) và bảng quét khung hành vi được viết từ nguồn **trước** khi mở `tests-M05.md` và `selfcheck-M05.md`. RG-1…RG-7 chấm bằng bằng chứng của tôi (mục 4.2), bảng "Rà hồi quy" của Author chỉ đọc sau đó để đối chiếu.
  - Giới hạn: lượt RELEASE phải đọc `diff` trước khi viết ca, nên ca kiểm không hoàn toàn mù với lời văn SR.
- **Giới hạn (không kiểm được):**
  - Chưa có SR của M03, M06, M07, M10, M13, M14. Các hàng R5 chỉ kiểm được nguồn, chưa kiểm được việc module đích nhận hàng đó. Riêng AUD-M05-37 phụ thuộc cách M07 sẽ viết danh sách sự kiện thông báo.
  - Lượt RELEASE không chạy lại ma trận độ phủ toàn bộ và không tìm chủ động ngoài phần đã đổi (RULES §8.6). Kết quả checklist của phần không đổi giữ như ISH-AUD-M05-v1.
  - Ý định của stakeholder ở AUD-M05-40 không suy được; báo cáo chỉ nêu lựa chọn.
- **Chênh lệch tồn kho so với ISH-AUD-M05-v1:**
  - OWNED tăng từ 116 lên 146: thêm đúng DEC-164…169, ISS-243…254, QA-303…314. Không mục nào bị bỏ.
  - REFERENCING giữ 22.
  - `registers_sha` của tôi trùng với inventory của Author (`275497dc…`), nghĩa là registers không đổi kể từ lúc Author bàn giao 0.5. Tập OWNED và REFERENCING của tôi trùng hoàn toàn với của Author.
  - Từ khóa tôi dùng như đợt xác minh, thêm "rename, đổi tên, follower".

## 3. Kết quả kiểm tra tự động

Lệnh chạy (từ gốc repo):

```
python3 .agent-instructions/system_analysis/shared/sr-tools/inventory.py \
  --registers .agents/.claude/system_analysis/output/registers --draft docs/_temp --module M05 \
  --keywords "topic,tag,trending,chủ đề,thẻ,gợi ý,suggest,follow,theo dõi,phân loại,classification,merge,gộp,hashtag,category,chuyên mục,stale,khối lớp,grade,rename,đổi tên,follower" \
  --out .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-M05-rel1.md \
  --json .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-M05-rel1.json
→ OWNED=146 REFERENCING=22 CROSS=42 DRAFT=30

python3 .agent-instructions/system_analysis/shared/sr-tools/check_sr.py \
  --sr .agents/.claude/system_analysis/output/specs/ISH-SR-M05.md \
  --routing .agents/.claude/system_analysis/output/specs/routing/ISH-RT-M05.md \
  --inventory .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-M05-rel1.json \
  --tests .agents/.claude/system_analysis/output/specs/audit/work/tests-M05.md \
  --json .agents/.claude/system_analysis/output/specs/audit/work/check-M05-rel1.json
```

**ERROR = 0, WARN = 2, INFO = 34.** Mã thoát 0. Có 12 yêu cầu cấp trên và 117 cấp dưới (thêm 10 ID, không bỏ ID nào so với 0.3).

- **WARN TST-03 × 2:** T-199 (`tests-M05.md:208`, "OP-M05-13") và T-200 (`:209`, "OP-M05-14"). Cả hai giả định đã có OP ở Phụ lục B (`ISH-SR-M05.md:614`, `:615`) và được Author giải thích ở `selfcheck-M05.md:161`. Không lập finding (AGENT "Kiểm tra tự động").
- **INFO COV-03 × 32:** 27 mục của đợt xác minh, cộng DEC-165, DEC-169, ISS-254, QA-304, QA-314 (mỗi mục có ở Phụ lục A và ở R3 hoặc R4). Tôi kiểm tay: DEC-165 ở SR là hành vi từ chối (010.5, 010.6), ở R3 là văn bản thông báo; DEC-169 ở SR là Lý do 5.10 và chủ sở hữu hiển thị (002.10, 006.16), ở R4 là ghi chú phạm vi. Không trùng nhau.
- **INFO COV-00:** OWNED = 146; 132 mục có trong SR, 46 mục có trong routing.
- **INFO TST-00:** 211 ca cho 117 yêu cầu.

Không có COV-01, COV-02, INV-01 hay TST-01, 02, 04, 05. Script không bắt được finding nào ở mục 5, vì cả sáu là lỗi ngữ nghĩa hoặc hồ sơ.

## 4. Ma trận độ phủ nguồn → yêu cầu

Ma trận đầy đủ: Không áp dụng — xác minh phát hành. Ma trận đầy đủ gần nhất nằm ở `work/coverage-M05-r2.md`, cập nhật cho đợt xác minh ở mục 4 của ISH-AUD-M05-v1. Bảng dưới chỉ ghi các mục OWNED mới (30 mục) và các mục có chỗ đi đã đổi.

| Nguồn | Mong đợi (Auditor) | Thực tế (SR / routing) | Kết quả | AUD |
|---|---|---|---|---|
| DEC-164, ISS-243, QA-303 | SR: 2.1 (so chữ cái trước, dấu thanh sau; ký hiệu trước chữ số); 008.11, 008.12 tham chiếu | 2.1 (`S:65`); Phụ lục A 008.11, 008.12 (`S:566`, `S:567`) | Khớp | 38 (ca kiểm) |
| DEC-165, ISS-244, QA-304 | SR: từ chối đổi tên Topic đã loại; thông báo "không tồn tại"; văn bản thông báo ở R3 | 010.5 (`S:399`), 010.6 (`S:400`); R3 (`R:42`) | Khớp | 39 (Lịch sử) |
| DEC-166 (1), ISS-248, QA-308 | SR: Tag bị vô hiệu hóa tính vào giới hạn 5 | 006.17 (`S:296`) | Khớp; mở ra một điểm nguồn im lặng | 40 |
| DEC-166 (2), ISS-251, QA-311 | SR: hiển thị tên Tag chữ thường | 006.18 (`S:297`) | Khớp | 38 (ca T-057) |
| DEC-166 (3), ISS-252, QA-312 | SR: chỉ chữ cái (kể cả có dấu), chữ số, gạch dưới; từ chối ký tự khác | 006.8 (`S:287`) | Khớp ý, câu đọc được hai cách | 36 |
| DEC-167, ISS-246, QA-306 | SR: chỉ gợi ý khi soạn bài mới; từ chối khi sửa bài đã gửi; các yêu cầu gợi ý cũ giới hạn tương ứng | 003 (`S:192`), 003.15 (`S:216`); 003.10…003.13 và 5.2 (`S:131`) chưa giới hạn | Thiếu một phần (vế giới hạn ở các yêu cầu liền kề) | 35 |
| DEC-167, ISS-253, QA-313 | SR: yêu cầu bị từ chối vì văn bản ngắn không tính vào 10/phút | 003.16; R2 (`R:28`) cập nhật | Khớp | — |
| DEC-168 (1), ISS-247, QA-307 | SR: từ chối tên rỗng; từ chối tên trùng (không phân biệt hoa–thường) | 010.7 (`S:401`), 010.8 (`S:402`); OP-M05-13 cho tên chỉ gồm ký tự trắng | Khớp | — |
| DEC-168 (2), ISS-249, QA-309 | SR: hiển thị số người theo dõi cho mọi người kể cả Guest; không tính tài khoản đã xóa | 007.4, 007.8 (`S:322`); 2.1 ba thuật ngữ tài khoản | Khớp | — |
| DEC-168 (3), ISS-250, QA-310 | Thông báo thuộc M07 (DEC-065): R5 M07, hoặc yêu cầu ở M05 kèm OP chủ sở hữu (§5.2) | 009.3 (`S:378`); không có hàng R5, không có OP | Sai chỗ | 37 |
| DEC-169 (1), ISS-245, QA-305 | SR: Lý do 5.10 | Lý do 5.10 (`S:334`); Phụ lục A 008 | Khớp | — |
| DEC-169 (2), ISS-254, QA-314 | SR: M05 sở hữu hiển thị Topic, Tag trên trang bài viết; R4 ghi chú | 002.10, 006.16 (Phụ lục A); R4 (`R:56`) | Khớp | — |
| DEC-161 (vế "chỉ") | SR: loại Tag không gắn trên bài viết được tính | 008.20 (`S:358`), Phụ lục A (`S:574`) | Khớp | — |

### 4.1 Ca kiểm độc lập cho các yêu cầu đã đổi (RELEASE bước 3)

Các ca được viết từ nguồn trước khi mở `tests-M05.md`. Cột "Author" ghi ca tương ứng của Author, đọc sau.

| ID ca | Nguồn | Loại | Given | When | Then theo nguồn | Nguồn xác định? | ID yêu cầu SR | SR xác định? | Author | Đối chiếu |
|---|---|---|---|---|---|---|---|---|---|---|
| R-01 | DEC-164 | Công thức | Tag "ban" và "bá" bằng điểm, bằng số bài mới | Xếp hạng Tag | "bá" trước "ban" | Có | 2.1, 008.12 | Có | T-180 | Trùng |
| R-02 | DEC-164 | Công thức | "nghỉhè" và "nghĩhè" bằng nhau ở hai tiêu chí đầu | Xếp hạng Tag | "nghỉhè" trước | Có | 2.1, 008.12 | Có | T-175 | Trùng |
| R-03 | DEC-164 | Công thức | Tag "toán" và "toanhoc" bằng nhau ở hai tiêu chí đầu | Xếp hạng Tag | "toán" trước (bước 1: "toan" là phần đầu của "toanhoc") | Có | 2.1 | Có | Không có ca | Không lập finding |
| R-04 | DEC-164, DEC-160, DEC-166 | Công thức | Tag "_a", "1a", "a" bằng nhau ở hai tiêu chí đầu ("_" là ký hiệu duy nhất được phép trong tên Tag) | Xếp hạng Tag | "_a", "1a", "a" | Có | 2.1 | Có | T-181 dùng "+a", tên mà 006.8 từ chối | Khác Given → AUD-38 |
| R-05 | DEC-161 | Vi phạm | Tag "đềthi12a1" chỉ gắn trên bản nháp và bài trong Group Private | Xếp hạng Tag | Không có trong bảng | Có | 008.20 | Có | T-173, T-177 | Trùng; AUD-27 đã sửa |
| R-06 | DEC-161 | Thời gian | "toánvui" chỉ gắn trên P30; P30 bị tác giả tự ẩn lúc T−1 giờ | Xếp hạng Tag tại T | Không có trong bảng | Có | 008.20 | Có | T-178 (bài bị Mod ẩn) | Trùng (cùng dạng) |
| R-07 | DEC-161 | Biên | "bayes" gắn trên một bài công khai đăng 30 ngày trước, 0 tương tác trong 7 ngày | Xếp hạng Tag | Có trong bảng, 0 điểm ("counted post" không có điều kiện thời gian) | Có | 008.19 | Có | T-153 (Given đã sửa) | Trùng |
| R-08 | DEC-167 | Vi phạm | Bài đã gửi, 40 tiếng | Tác giả sửa bài rồi yêu cầu gợi ý | Từ chối | Có | 003.15 | Có | T-182 | Trùng |
| R-09 | DEC-167, DEC-050, DEC-148 | Vi phạm | Bài gửi lần đầu với gợi ý còn mới, bị Mod từ chối; tác giả sửa nội dung (gợi ý thành gợi ý cũ) | Tác giả yêu cầu gợi ý lại | Từ chối ("not available when the author edits an already-submitted post") | Có | 003.15 và 003.13 | **Không**: 003.15 từ chối, 003.13 "cho phép tác giả yêu cầu gợi ý Topic lại" trong khi gợi ý cũ | T-170: tác giả "nhận gợi ý mới (còn mới)" | Khác → AUD-35 |
| R-10 | DEC-167 | Biên | Bản nháp đã lưu, chưa gửi lần nào | Tác giả mở lại và yêu cầu gợi ý | Chấp nhận (vẫn là soạn bài mới) | Có | 003, 003.15 | Có | Không có ca | Không lập finding |
| R-11 | DEC-167 | Biên | 9 yêu cầu hợp lệ và 5 yêu cầu bị từ chối vì dưới 10 tiếng trong cùng phút | Yêu cầu hợp lệ thứ 10 | Chấp nhận | Có | 003.16, 003.9 | Có | T-183 | Trùng |
| R-12 | DEC-167 | Biên | Như R-11, yêu cầu thứ 10 đã được chấp nhận | Yêu cầu hợp lệ thứ 11 | Từ chối | Có | 003.9, 003.16 | Có | T-184 | Trùng |
| R-13 | DEC-166 | Thường | Đang gắn Tag | Nhập "#đềthi12a1" | Chấp nhận (chữ có dấu, chữ số) | Có | 006.8 | **Mơ hồ**: cách đọc 1 chấp nhận; cách đọc 2 ("có chứa [ký tự không phải chữ cái (kể cả chữ có dấu)], [chữ số] hoặc [dấu gạch dưới]") từ chối | T-187 ("xác_suất_2024" được chấp nhận) | Then của Author lấy theo ý nguồn, câu SR đọc được hai cách → AUD-36 |
| R-14 | DEC-166 | Vi phạm | Đang gắn Tag | Nhập "#bay-es", "#c++", "#a b" | Từ chối cả ba | Có | 006.8 | Có (cả hai cách đọc) | T-185, T-067 | Trùng |
| R-15 | DEC-166 | Biên | Bài có 4 Tag hoạt động và "spam" bị vô hiệu hóa | Tác giả thêm Tag thứ 5 hiển thị | Từ chối (đã đủ 5) | Có | 006.17, 006.5 | Có | T-190 | Trùng |
| R-16 | DEC-166, DEC-051 | Biên | Như R-15 | Tác giả sửa bài, muốn gỡ "spam" để thêm Tag khác | Nguồn im lặng: cách 1 tác giả thấy và gỡ được "spam" trong lúc sửa, thêm được Tag mới; cách 2 "spam" bị ẩn cả khi sửa, tác giả không gỡ được, bài kẹt ở 4 Tag hiển thị | **Mơ hồ** | 006.17, 012.1, 006.11 | Không | Không có ca | → AUD-40 |
| R-17 | DEC-166 | Thường | Tác giả nhập "#Bayes" | Guest mở bài | Hiển thị "#bayes" | Có | 006.18 | Có | T-192; T-057 vẫn ghi Then "Bài viết có Tag "XácSuất"" | T-192 Trùng; T-057 Khác → AUD-38 |
| R-18 | DEC-168 | Quyền | "Tin học" có 3 người theo dõi | Guest xem danh mục | Thấy 3 | Có | 007.4 | Có | T-193 | Trùng |
| R-19 | DEC-168 | Thường | Người theo dõi: A hoạt động, B bị vô hiệu hóa, C bị cấm, D đã xóa | Xem số người theo dõi | 3 | Có | 007.8 | Có | T-194 | Trùng |
| R-20 | DEC-168, DEC-019 | Thời gian | Như R-19; 14 ngày sau B bị hệ thống xóa | Xem số người theo dõi | 2 | Có | 007.8, 2.1 | Có | Không có ca | Không lập finding |
| R-21 | DEC-168 | Thường | Mod đổi Topic bài của User A | — | A không nhận thông báo | Có | 009.3 | Có | T-195 | Trùng; chủ sở hữu → AUD-37 |
| R-22 | DEC-165 | Vi phạm | "Góc Chill" đã gộp | Mod đổi tên "Góc Chill" | Từ chối; báo "không tồn tại" | Có | 010.5, 010.6 | Có | T-172, T-179 | Trùng; AUD-33 đã sửa |
| R-23 | DEC-168 | Vi phạm | Danh mục có "Toán học", "Tin học" | Đổi tên "Tin học" thành "toán học" | Từ chối | Có | 010.8 | Có | T-197 | Trùng |
| R-24 | DEC-168 | Biên | "Góc Chill" đã gộp (ngoài danh mục) | Đổi tên "Khác" thành "Góc Chill" | Chấp nhận ("another Topic in the catalog") | Có | 010.8 | Có | Không có ca (selfcheck nêu ở RG-2, `selfcheck-M05.md:153`) | Không lập finding |
| R-25 | DEC-168 | Vi phạm | — | Đổi tên thành "" | Từ chối | Có | 010.7 | Có | T-196 | Trùng; "   " ở OP-M05-13 (T-199) |

### 4.2 Quét khung hành vi (phần đã đổi) và RG-1…RG-7 do Auditor chấm

Quét bảy câu hỏi của RULES §4.7 cho các tính năng có ID đổi, từ nguồn:
- 5.5: câu 2 (ngữ cảnh) → (a) DEC-167; các yêu cầu gợi ý cũ phải theo cùng ngữ cảnh (AUD-35). Câu 4: yêu cầu bị từ chối vì lý do khác văn bản ngắn (bài đã gửi, chức năng tắt) có tính vào 10/phút không → (c) nhỏ; giao diện sửa bài không có gợi ý nên hệ quả hầu như không quan sát được; ghi chú, không lập finding.
- 5.8: câu 4 → (a) DEC-166 (3) (AUD-36 về lời văn). Câu 5, 6 → (c): Tag bị vô hiệu hóa tính vào 5 nhưng bị ẩn; tác giả có thấy và gỡ được khi sửa bài không (AUD-40).
- 5.9: câu 1, 5 → (a) DEC-168 (2).
- 5.10: câu 4, 5 → (a) DEC-161, DEC-164.
- 5.11: câu 5 → (a) DEC-168 (3) cho tác giả (AUD-37 về chủ sở hữu); người theo dõi → (c) đã có OP-M05-14.
- 5.12: câu 4 → (a) DEC-165, DEC-168 (1); tên chỉ gồm ký tự trắng → (c) đã có OP-M05-13. Giới hạn độ dài tên Topic: nguồn im lặng, ghi chú nhỏ, không lập finding.

RG-1…RG-7 (RULES §8.5), chấm cho mọi ID mới hoặc đổi:

| ID | RG-1 | RG-2 | RG-3 | RG-4 | RG-5 | RG-6 | RG-7 |
|---|---|---|---|---|---|---|---|
| 003.15 | Đạt (vế loại trừ của 003) | **Không đạt**: va 003.10, 003.12, 003.13, 5.2 (AUD-35) | Đạt: 003 (bao gồm) + 003.15 (loại trừ) | Đạt | — | Đạt | **Không đạt**: T-170 chưa sửa (AUD-35) |
| 003.16 | Đạt | Đạt (003.6, 003.8, 003.9) | Không áp dụng | Đạt | — | Đạt | Đạt (T-183, T-184) |
| 006.8 | Đạt | Đạt (006.6, 006.7, 006.13…006.15) | Đạt: từ chối + 006.1, 006.2 | Đạt | — | Đạt | **Không đạt**: T-176, T-181 dùng tên bị 006.8 từ chối (AUD-38); lời văn mơ hồ (AUD-36, chấm CL-B08) |
| 006.17 | Đạt | Đạt (006.4, 006.5, 012.2, 012.5) | Không áp dụng | Đạt | — | Đạt | Đạt (T-190, T-191); điểm (c) ở AUD-40 |
| 006.18 | Đạt | Đạt (006.9, 006.16) | Không áp dụng | Đạt | — | Đạt | **Không đạt**: T-057 (AUD-38) |
| 007.4, 007.8 | Đạt | Đạt (007.6, 011.3, 011.4) | Đạt: 007.8 có cả vế bao gồm lẫn loại trừ | Đạt | — | Đạt | Đạt (T-193, T-194) |
| 008.20 | Đạt | Đạt (008.19, 012.3 bổ sung nhau) | Đạt: DEC-161 "only" có cả 008.19 và 008.20 | Đạt | — | Đạt | Đạt (T-153 sửa Given, T-177, T-178) |
| 009.3 | Đạt (hệ quả của 009.1) | Đạt (009.1, 009.2, OP-M05-14 nói người theo dõi) | Không áp dụng | Đạt | — | Đạt | Đạt (T-195); chủ sở hữu ở AUD-37 (CL-E02) |
| 010.5, 010.6 | Đạt | Đạt (011.8, 011.9 cùng dạng) | Không áp dụng | Đạt | — | **Không đạt**: hàng R3 đổi ở 0.4 không có trong Lịch sử (AUD-39) | Đạt (T-172, T-179) |
| 010.7, 010.8 | Đạt | Đạt (010.5, 2.1) | Không áp dụng | Đạt: không chọn trước OP-M05-13 | — | Đạt | Đạt (T-196…T-199) |
| 2.1 thứ tự tên | Không áp dụng | Đạt (008.11, 008.12) | Không áp dụng | Đạt | — | Đạt | **Không đạt**: T-181 (AUD-38) |
| 006.15, 008.5…008.7, 008.17 (diễn đạt) | Đạt | Đạt: nghĩa không đổi (so `diff`) | Không áp dụng | Đạt | — | Đạt | Không áp dụng |
| OP-M05-01, 02, 04…09, 11, 12 (xóa) | — | — | — | — | Đạt: chỉ còn ở dòng Lịch sử (`S:471`, `S:472`, `S:474`); `tests-M05.md` và routing → 0 | Đạt | — |

Bảng "Rà hồi quy" của Author (`selfcheck-M05.md:138–155`) chỉ có các ID đổi ở 0.5; không có dòng cho 008.20, 010.5, 010.6 và 2.1 (đổi ở 0.4). RG-2 của 003.15 ghi "so 003.1, 003.9, 004.x, 005.x" (`selfcheck-M05.md:144`), không so 003.10…003.14. Đây là tệp làm việc nên không lập finding riêng; các hệ quả đã nằm ở AUD-35, AUD-39.

## 5. Phát hiện

Thứ tự trình bày: DEFECT Trung bình, rồi DEFECT Thấp, rồi GAP Thấp. Cả sáu finding nằm trong phần đã đổi từ 0.3 đến 0.5 nên đều gắn nhãn `Hồi quy`.

### AUD-M05-35 — 003.15 (không gợi ý khi sửa bài đã gửi) chưa được phản ánh ở các yêu cầu gợi ý cũ 003.10, 003.12, 003.13 và hàng 5.2; ca T-170 trái 003.15

| Lớp | DEFECT | Nhãn | Hồi quy (ID mới 003.15) | Mức | Trung bình | Checklist | CL-C01, CL-B12 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-003.15 (`ISH-SR-M05.md:216`); ISH-M05-003.10, 003.12, 003.13 (`:211`, `:213`, `:214`); 5.2 (`:131`); `tests-M05.md:179` (T-170).
- **Bằng chứng trong SR/routing:**
  - "Khi tác giả yêu cầu gợi ý Topic cho một bài viết đã gửi, hệ thống phải từ chối yêu cầu đó." (`ISH-SR-M05.md:216`)
  - "Khi tác giả thay đổi tiêu đề hoặc nội dung văn bản của bài viết sau khi nhận gợi ý Topic, hệ thống phải đánh dấu gợi ý đó là gợi ý cũ." (`ISH-SR-M05.md:211`)
  - "Trong khi gợi ý Topic của bài viết là gợi ý cũ, hệ thống phải hiển thị cảnh báo gợi ý cũ cho tác giả." (`ISH-SR-M05.md:213`)
  - "Trong khi gợi ý Topic của bài viết là gợi ý cũ, hệ thống phải cho phép tác giả yêu cầu gợi ý Topic lại." (`ISH-SR-M05.md:214`)
  - "| Gợi ý cũ | Tác giả yêu cầu gợi ý lại và nhận gợi ý mới | Gợi ý còn mới |" (`ISH-SR-M05.md:131`)
  - Ca của Author: "Như T-169, User A sửa nội dung, nhận gợi ý mới (còn mới), rồi gửi lại" (`tests-M05.md:179`, T-170), trong khi T-169 là bài đã gửi và bị Mod từ chối (`tests-M05.md:178`).
  - Rà hồi quy của Author: "Đạt: grep "gợi ý Topic" so 003.1, 003.9, 004.x, 005.x" (`selfcheck-M05.md:144`), không so 003.10…003.14.
- **Bằng chứng trong nguồn:**
  - "AI Topic suggestion is available only while composing a new post; it is not available when the author edits an already-submitted post" (`decisions.md:885`, DEC-167)
  - "Content changed after suggest → flag is_stale, soft warning + re-suggest button, does not block publish" (`decisions.md:293`, DEC-050): luồng gợi ý cũ thuộc luồng soạn bài.
- **Vấn đề:**
  - 003.10, 003.12, 003.13 và hàng 5.2 không giới hạn vào lúc soạn bài viết mới. Khi tác giả sửa nội dung một bài đã gửi từng nhận gợi ý, 003.10 đánh dấu gợi ý cũ, 003.12 bắt hiển thị cảnh báo gợi ý cũ, 003.13 bắt "cho phép" yêu cầu gợi ý lại, còn 003.15 bắt từ chối (ca R-09).
  - Có thể đọc 003.13 là "gợi ý cũ không chặn việc gợi ý lại" để dung hòa với 003.15, nhưng khi đó 003.12 vẫn bắt hiển thị một cảnh báo mời gợi ý lại cho một bài không được gợi ý, và hàng 5.2 mô tả một chuyển trạng thái không thể xảy ra với bài đã gửi.
  - Ca T-170 (005.5) được viết từ trước DEC-167 và vẫn cho tác giả "nhận gợi ý mới" sau khi bài bị từ chối, trái T-182 và 003.15 (CL-B12).
- **Lý do mức:** CL-C01 mặc định Cao. Hạ một mức vì nguồn (DEC-167) đã quyết rõ, có cách đọc dung hòa cho 003.13, và việc sửa chỉ là giới hạn phạm vi các yêu cầu liền kề, không cần câu trả lời mới.
- **Hệ quả nếu không sửa:** Cài đặt làm đúng 003.12, 003.13 sẽ hiện cảnh báo và nút gợi ý lại trên màn hình sửa bài đã gửi, đúng điều DEC-167 loại; ca kiểm T-170 và T-182 cho hai kết quả trái nhau.
- **Hướng xử lý (Author quyết cách viết):** Giới hạn 003.10…003.13 (và hàng 5.2 tương ứng) vào bài viết chưa gửi hoặc lúc soạn bài viết mới, theo DEC-167, kèm Phụ lục A; sửa hoặc bỏ T-170 (005.5 vẫn kiểm được bằng T-169) và thêm ca "bài đã gửi có gợi ý cũ".
- **Trạng thái:** Mở.

### AUD-M05-36 — Câu 006.8 viết lại đọc được theo hai cách cho kết quả trái nhau với chữ số và dấu gạch dưới

| Lớp | DEFECT | Nhãn | Hồi quy (006.8 đổi nội dung) | Mức | Trung bình | Checklist | CL-B08, CL-B03 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-006.8 (`ISH-SR-M05.md:287`); Phụ lục A (`:535`).
- **Bằng chứng trong SR:**
  - "Khi tác giả nhập tên Tag có chứa ký tự không phải chữ cái (kể cả chữ cái có dấu tiếng Việt), chữ số hoặc dấu gạch dưới, hệ thống phải từ chối Tag đó." (`ISH-SR-M05.md:287`)
  - Phụ lục A nêu đúng ý: "Chỉ chữ cái, chữ số và dấu gạch dưới" (`ISH-SR-M05.md:535`).
- **Bằng chứng trong nguồn:** "A Tag name may contain only letters (including Vietnamese letters with diacritics), digits and the underscore; a name containing any other character (whitespace, "+", "&", punctuation, symbols) is rejected." (`decisions.md:881`, DEC-166)
- **Vấn đề:** Cụm "có chứa ký tự không phải chữ cái (kể cả chữ cái có dấu tiếng Việt), chữ số hoặc dấu gạch dưới" có hai cách tách:
  - **Cách 1 (đúng ý nguồn):** có chứa ký tự không phải [chữ cái, chữ số hoặc dấu gạch dưới] → "#đềthi12a1", "#xác_suất_2024" được chấp nhận.
  - **Cách 2:** có chứa [ký tự không phải chữ cái, kể cả chữ cái có dấu], [chữ số] hoặc [dấu gạch dưới] → cả "#đềthi12a1" (chữ có dấu, chữ số) lẫn "#xác_suất" (gạch dưới) bị từ chối. "kể cả" đặt ngay sau "không phải chữ cái" càng làm cách đọc này tự nhiên.
  - Ca R-13 không suy ra được một "Then" duy nhất từ câu yêu cầu; T-187 của Author lấy "Then" theo ý nguồn chứ không theo lời văn.
- **Hệ quả nếu không sửa:** Một cài đặt theo cách 2 từ chối phần lớn Tag tiếng Việt và Tag có số mà vẫn thỏa câu chữ của SR.
- **Hướng xử lý (Author quyết cách viết):** Viết lại 006.8 để phạm vi phủ định không thể hiểu sai (ví dụ nêu tập ký tự được phép trước rồi từ chối ký tự ngoài tập đó), có thể tách thành hai yêu cầu cấp dưới (tập ký tự được phép; từ chối khi có ký tự khác), kèm Phụ lục A.
- **Trạng thái:** Mở.

### AUD-M05-37 — 009.3 viết hành vi thông báo (M07 sở hữu theo DEC-065) ở M05 mà không có hàng R5 hay OP chủ sở hữu

| Lớp | DEFECT | Nhãn | Hồi quy (ID mới 009.3) | Mức | Trung bình | Checklist | CL-E02, CL-A10 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-009.3 (`ISH-SR-M05.md:378`); Phụ lục A (`:578`); routing R5 (`ISH-RT-M05.md:70`).
- **Bằng chứng trong SR/routing:**
  - "Khi Mod hoặc Admin lưu thay đổi Topic của một bài viết do người khác viết, hệ thống phải không gửi thông báo về thay đổi đó cho tác giả." (`ISH-SR-M05.md:378`)
  - "| ISH-M05-009.3 | DEC-168, ISS-250, QA-310, DEC-065 | Nói thẳng |" (`ISH-SR-M05.md:578`)
  - Cùng SR coi thông báo là của M07: "người theo dõi có nhận thông báo "bài mới trong Topic" (DEC-155, M07 sở hữu) không" (`ISH-SR-M05.md:615`, OP-M05-14); R5 chuyển thông báo bài mới cho M07: "Thông báo in-app khi có bài mới trong Topic đang theo dõi" (`ISH-RT-M05.md:70`).
  - OP gốc ở bản 0.3 đã ghi chủ sở hữu: "tác giả có được thông báo không (thuộc M07)" (`snapshot-ISH-SR-M05-v0.3.md:594`, OP-M05-07).
- **Bằng chứng trong nguồn:**
  - "When a Mod or Admin changes the Topics of a post, the author is not notified (not an event in the DEC-065 list)." (`decisions.md:889`, DEC-168)
  - DEC-065 nằm ở "## Phase 5 — M07: Notification" (`decisions.md:375`); "M07 owns delivery and any batching rule." (`decisions.md:835`, DEC-155)
- **Vấn đề:**
  - Kết quả người dùng nhìn thấy (có hay không có thông báo) nằm ở M07, và lý do của DEC-168 (3) chính là danh sách sự kiện DEC-065 mà M07 sở hữu. Theo RULES §5 mục 1, 5 phần này phải là hàng R5 cho M07; nếu Author cho rằng M05 sở hữu thì §5 mục 2 yêu cầu một `OP` loại Đề xuất để stakeholder chốt chủ sở hữu.
  - Hiện SR không có cả hai: `grep -n -E "009\.3|DEC-168|ISS-250|QA-310" ISH-RT-M05.md` → 0; Phụ lục B chỉ có OP-M05-13, OP-M05-14.
  - Cách xử lý hai câu cùng loại trong một SR không nhất quán: thông báo cho người theo dõi được coi là của M07, thông báo cho tác giả lại viết thành yêu cầu M05.
- **Lý do mức:** CL-E02 mặc định Cao. Hạ một mức vì đây là yêu cầu phủ định, không mâu thuẫn với danh sách sự kiện của M07, và §5 mục 2 cho phép giữ ở M05 nếu kèm OP.
- **Hệ quả nếu không sửa:** Khi viết SR M07, không có dấu vết nào cho biết sự kiện "Mod đổi Topic" đã được quyết là không thông báo; hai SR có thể cùng viết hoặc cùng bỏ hành vi này.
- **Hướng xử lý (Author quyết cách viết):** Hoặc chuyển phần thông báo sang hàng R5 (M07, chưa có SR, ghi nguồn DEC-168) và bỏ ID 009.3 theo thủ tục §8.5 (ID đã nằm trong bản chụp v0.5 nên phải ghi Lịch sử), hoặc giữ 009.3 và thêm `OP` loại Đề xuất về chủ sở hữu.
- **Trạng thái:** Mở.

### AUD-M05-38 — Ca kiểm cũ chưa cập nhật theo 006.8 và 006.18 mới: T-176, T-181 dùng tên Tag bị từ chối; T-057 kỳ vọng tên Tag giữ chữ hoa

| Lớp | DEFECT | Nhãn | Hồi quy (006.8, 006.18, 2.1) | Mức | Thấp | Checklist | CL-B12 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** `tests-M05.md:185` (T-176), `:190` (T-181), `:66` (T-057); ISH-M05-006.8 (`ISH-SR-M05.md:287`), 006.18 (`:297`), 2.1 (`:65`).
- **Bằng chứng:**
  - "Tại T: Tag "c" và "c++" cùng 1 điểm" (`tests-M05.md:185`, T-176)
  - "Tại T: Tag "+a", "1a", "a" cùng 1 điểm" (`tests-M05.md:190`, T-181), Then "ký hiệu trước chữ số, chữ số trước chữ cái".
  - "Bài viết có Tag "XácSuất"" (`tests-M05.md:66`, T-057)
  - Ca của chính Author cho 006.8: "Hệ thống từ chối Tag "c++" (có ký tự "+")" (`tests-M05.md:194`, T-185).
  - Nguồn: "A Tag name may contain only letters (including Vietnamese letters with diacritics), digits and the underscore" và "(2) A Tag name is displayed in lowercase" (`decisions.md:881`, DEC-166).
- **Vấn đề:** Ba ca có Given hoặc Then không còn xảy ra được theo SR 0.5. T-176 và T-181 là ca của 2.1 và 008.12 nhưng dùng tên Tag mà 006.8 từ chối; ca "ký hiệu trước chữ số" của Tag vì thế không có Given hợp lệ (ký hiệu duy nhất còn được phép là "_", ca R-04). T-057 kỳ vọng tên Tag giữ "XácSuất" trong khi 006.18 hiển thị chữ thường.
- **Lý do mức:** CL-B12 mặc định Trung bình. Hạ một mức vì đây là tệp làm việc, SR không sai, và cách sửa là cơ học.
- **Hệ quả nếu không sửa:** Bộ ca kiểm chứa ca không thực hiện được và ca trái yêu cầu, làm giảm giá trị kiểm chứng của 2.1 và 006.18.
- **Hướng xử lý (Author quyết cách viết):** Đổi Given của T-176, T-181 sang tên Tag hợp lệ (ví dụ dùng "_"); sửa Then của T-057 theo 006.18 hoặc ghi rõ ca chỉ kiểm việc gắn Tag.
- **Trạng thái:** Mở.

### AUD-M05-39 — Dòng Lịch sử 0.4 thiếu thay đổi ở routing R3 (DEC-165, 010.6)

| Lớp | DEFECT | Nhãn | Hồi quy (RG-6) | Mức | Thấp | Checklist | CL-F02 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** Lịch sử 0.4 (`ISH-SR-M05.md:473`); routing R3 (`ISH-RT-M05.md:42`).
- **Bằng chứng:**
  - Routing 0.3: "| DEC-159, QA-296 | Văn bản thông báo "Topic không tồn tại" khi gộp với Topic đã bị loại" (`snapshot-ISH-RT-M05-v0.3.md:42`).
  - Routing 0.4 và hiện tại: "| DEC-159, QA-296, DEC-165, QA-304 | Văn bản thông báo "Topic không tồn tại" khi gộp hoặc đổi tên Topic đã bị loại" (`snapshot-ISH-RT-M05-v0.4.md:42`, `ISH-RT-M05.md:42`).
  - Dòng 0.4 chỉ nêu "AUD-27: thêm 008.20 … AUD-34: 2.1 … AUD-33: 010.5 đổi cơ sở sang Nói thẳng theo DEC-165 (ISS-244, QA-304); thêm 010.6 (thông báo Topic không tồn tại)" (`ISH-SR-M05.md:473`); `sed -n 473p | grep -c -E "R3|[Rr]outing"` → 0.
  - Dòng 0.5 có ghi routing: "Routing: R2 (003.8 đã thành yêu cầu 003.16), R4 thêm hàng DEC-169" (`ISH-SR-M05.md:474`), không nhắc R3.
- **Vấn đề:** RG-6 yêu cầu mọi khác biệt ở routing có trong dòng Lịch sử sinh từ `diff`. Thay đổi hàng R3 ở 0.4 không có trong dòng Lịch sử nào. Dòng 0.4 cũng không nêu cập nhật 3.1; dòng 0.5 đã bù bằng câu "3.1 cập nhật khoảng DEC-140…169", nên phần 3.1 không lập finding.
- **Hệ quả nếu không sửa:** Lịch sử không cho người đọc biết bản 0.4 đã đổi routing.
- **Hướng xử lý (Author quyết cách viết):** Bổ sung thay đổi R3 vào dòng 0.4 (hoặc dòng của phiên bản kế tiếp, ghi rõ là bổ sung cho 0.4).
- **Trạng thái:** Mở.

### AUD-M05-40 — Tag bị vô hiệu hóa chiếm chỗ trong giới hạn 5 nhưng bị ẩn: tác giả có thấy và gỡ được Tag đó khi sửa bài không

| Lớp | GAP | Nhãn | Hồi quy (ID mới 006.17) | Mức | Thấp | Checklist | CL-B13 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-006.17 (`ISH-SR-M05.md:296`); 012.1 (`:446`); 006.11 (`:290`).
- **Bằng chứng trong SR:**
  - "Hệ thống phải tính Tag bị vô hiệu hóa còn gắn trên một bài viết vào giới hạn tối đa 5 Tag của bài viết đó." (`ISH-SR-M05.md:296`)
  - "Khi Mod hoặc Admin vô hiệu hóa một Tag, hệ thống phải ẩn Tag đó trên mọi bài viết đang gắn Tag đó." (`ISH-SR-M05.md:446`)
  - "Khi tác giả sửa một bài viết đã gửi, hệ thống phải cho phép tác giả thay đổi Tag của bài viết đó." (`ISH-SR-M05.md:290`)
- **Bằng chứng trong nguồn:**
  - "A disabled Tag still attached to a post counts toward that post's limit of 5 Tags, so that re-enabling the Tag never pushes a post above 5." (`decisions.md:881`, DEC-166)
  - "old posts keep post_tags record but tag chip hidden from display" (`decisions.md:304`, DEC-051)
- **Vấn đề:** Trước DEC-166, Tag bị vô hiệu hóa bị ẩn nhưng không ảnh hưởng gì tới tác giả. Nay Tag đó chiếm một chỗ trong giới hạn 5, nên câu hỏi "khi sửa bài, tác giả có thấy và gỡ được Tag bị vô hiệu hóa không" có hai câu trả lời với hệ quả khác nhau (ca R-16, bài có 4 Tag hiển thị và "spam" bị vô hiệu hóa):
  - **A) Thấy và gỡ được trong lúc sửa bài:** tác giả gỡ "spam" rồi thêm Tag khác; khi "spam" được mở lại, bài không còn "spam".
  - **B) Bị ẩn cả khi sửa, không gỡ được:** tác giả chỉ thấy 4 Tag nhưng mọi Tag thứ 5 đều bị từ chối, không có cách tự giải phóng chỗ cho tới khi Mod hoặc Admin mở lại "spam".
  - Tôi tìm trong SR, routing và register các cụm "vô hiệu hóa" cùng "sửa bài", "gỡ", "trình soạn", và "disabled"/"hidden" cùng "edit", "editor", "remove": 0 kết quả liên quan. Không có OP về điểm này; bảng quét của Author (`selfcheck-M05.md:70`, `:71`) không nêu.
- **Lý do mức:** CL-B13 mặc định Trung bình. Hạ một mức vì chỉ xảy ra với bài đã đủ 5 Tag mà có Tag bị vô hiệu hóa trong tình huống khẩn cấp.
- **Hệ quả nếu không xử lý:** Hai cài đặt khác nhau đều thỏa SR; ca R-16 không có "Then" duy nhất.
- **Hướng xử lý:** Stakeholder quyết (mục 6); hoặc Author ghi một `OP` loại Đề xuất ở Phụ lục B kèm đề xuất mặc định. Sau khi có câu trả lời: ghi register, thêm yêu cầu cấp dưới ở 5.8 hoặc 5.14 và ca kiểm.
- **Trạng thái:** Mở.

## 6. Cần stakeholder quyết

AUD-M05-35…39 là DEFECT có hướng sửa theo nguồn đã có, nên không nằm ở đây: Author sửa thẳng. Riêng AUD-M05-37 Author có hai cách sửa; nếu Author chọn giữ 009.3 thì `OP` về chủ sở hữu sẽ được đưa cho stakeholder theo §5 mục 2.

Ngoài khối dưới đây, Phụ lục B của SR còn hai `OP` loại Đề xuất do Author mở ở 0.5 và đang chờ stakeholder duyệt: OP-M05-13 (tên Topic chỉ gồm ký tự trắng; bỏ ký tự trắng đầu và cuối trước khi so trùng) và OP-M05-14 (người theo dõi Topic đích có nhận thông báo "bài mới" khi Mod đổi Topic của bài không). Hai `OP` này đúng khuôn, không phải finding của báo cáo này.

**1.**
Vấn đề: Khi sửa một bài viết có Tag đã bị vô hiệu hóa, tác giả có thấy và gỡ được Tag đó không?
Bối cảnh: Từ DEC-166, Tag bị vô hiệu hóa vẫn chiếm một chỗ trong giới hạn 5 Tag của bài, nhưng theo DEC-051 Tag đó bị ẩn trên bài. Ví dụ: bài của User A có 4 Tag hiển thị và Tag "spam" đã bị vô hiệu hóa; A sửa bài và muốn thêm Tag "anova".
Nguồn: DEC-166 (`decisions.md:881`) "A disabled Tag still attached to a post counts toward that post's limit of 5 Tags"; DEC-051 (`decisions.md:304`) "old posts keep post_tags record but tag chip hidden from display".
Lựa chọn:
- A) Khi sửa bài, tác giả thấy Tag bị vô hiệu hóa (đánh dấu là đã bị vô hiệu hóa) và gỡ được. Hệ quả: A gỡ "spam" rồi thêm "anova"; nếu sau đó "spam" được mở lại, bài của A không còn "spam".
- B) Tag bị vô hiệu hóa bị ẩn cả khi sửa, tác giả không gỡ được. Hệ quả: A thấy 4 Tag nhưng "anova" bị từ chối vì đã đủ 5; A chỉ thêm được Tag khi Mod hoặc Admin mở lại "spam" và A gỡ nó.
Đề xuất: A, vì tác giả là người duy nhất được đổi Tag của bài (DEC-144) và không nên bị chặn bởi một Tag mình không thấy; khi Tag được mở lại, giới hạn 5 vẫn giữ.
Liên quan: AUD-M05-40

## 7. Kết quả checklist

Lượt RELEASE chấm lại các mục chạm tới phần đã đổi (0.3 → 0.5) và các finding còn mở của ISH-AUD-M05-v1. Mục không chạm tới phần đã đổi ghi `Không áp dụng — xác minh phát hành` kèm kết quả gần nhất.

| Mã | Kết quả | AUD / ghi chú |
|---|---|---|
| CL-A01 | Không áp dụng — xác minh phát hành | DRAFT không đổi (30 mục); vòng 2 Đạt |
| CL-A02 | Đạt | Không có COV-01, INV-01; 30 mục OWNED mới đều có chỗ đi (mục 4) |
| CL-A03 | Không áp dụng — xác minh phát hành | REFERENCING giữ 22 mục, trùng inventory của Author; v1 Đạt |
| CL-A04 | Đạt | Không có COV-02, TRC-06 |
| CL-A05 | Đạt | Các dòng `Nói thẳng` mới hoặc đổi (003.15, 003.16, 006.8 theo ý, 006.17, 006.18, 007.4, 007.8, 008.20, 009.3, 010.5…010.8) khớp nguyên văn DEC-164…169, DEC-161. Lời văn 006.8 chấm ở CL-B08 |
| CL-A06 | Đạt | Không có `Suy ra` mới; 010.5 đã đổi sang `Nói thẳng` (DEC-165) |
| CL-A07 | Đạt | Số mới: 14 ngày (DEC-019), 5 (DEC-166), 10 (DEC-167) đều có nguồn |
| CL-A08 | Không áp dụng — xác minh phát hành | Không có lệch DRAFT ↔ register mới |
| CL-A09 | Đạt | DEC-164…169 là Clarified; nhãn ở DEC-047 (`decisions.md:279`), DEC-051 (`:302`), DEC-160 (`:857`); SR theo bản mới |
| CL-A10 | Không đạt | AUD-M05-37 (phần M07 của DEC-168 (3) không có hàng R5). DEC-165, DEC-167, DEC-169 tách đúng |
| CL-A11 | Đạt | AUD-M05-34 đã giải bằng DEC-164; nguồn mới không còn chỗ đọc hai cách |
| CL-B01 | Đạt | ID mới đúng mẫu; 006.15, 008.5…008.7, 008.17 đổi sang `Khi …` |
| CL-B02 | Đạt | RULE-01/02/08 không báo; mỗi ID mới một hành vi |
| CL-B03 | Không đạt | AUD-M05-36 (cụm phủ định của 006.8 mơ hồ) |
| CL-B04 | Đạt | RULE-03 không báo |
| CL-B05 | Đạt | RULE-05 không báo |
| CL-B06 | Đạt | Không có tên bảng, trạng thái kỹ thuật (DELETED, BANNED) hay cơ chế trong câu yêu cầu |
| CL-B07 | Đạt | RULE-09 không báo |
| CL-B08 | Không đạt | AUD-M05-36 (R-13), AUD-M05-35 (R-09) |
| CL-B09 | Đạt | Nhánh vi phạm có đủ: 003.15, 006.8, 006.17 (qua 006.5), 010.5, 010.7, 010.8, 008.20 |
| CL-B10 | Đạt | Mỗi ID mới một giới hạn hoặc một nhánh |
| CL-B11 | Đạt | 010.7, 010.8 nêu Mod/Admin; 007.4 nêu Guest |
| CL-B12 | Không đạt | AUD-M05-38 (T-176, T-181, T-057), AUD-M05-35 (T-170). Mọi ID mới có ca |
| CL-B13 | Không đạt | AUD-M05-40 (điểm (c) do 006.17 mở ra, chưa hỏi, chưa có OP) |
| CL-C01 | Không đạt | AUD-M05-35 (003.15 với 003.10, 003.12, 003.13, 5.2) |
| CL-C02 | Đạt | 008.19 và 008.20 bổ sung nhau; 010.6 và 011.9 khác thao tác |
| CL-C03 | Đạt | Ba thuật ngữ tài khoản mới dùng ở 007.8; không có thuật ngữ mới ngoài 2.1 |
| CL-C04 | Đạt | Lý do 5.10 lấy từ DEC-169; cấp trên bao quát ID mới (mục 4.2 RG-1) |
| CL-C05 | Đạt | 5.1 không đổi và vẫn đúng mốc; 5.2 trỏ ID có thật (phạm vi của hàng `S:131` chấm ở CL-C01) |
| CL-D01 | Đạt | HDR-01…08 không báo; phiên bản 0.5 khớp dòng Lịch sử cuối |
| CL-D02 | Đạt | STR-01…09 không báo |
| CL-D03 | Đạt | REQ-00…04 không báo |
| CL-D04 | Đạt | ID mới lấy số kế tiếp chưa dùng (003.15, 003.16, 006.17, 006.18, 007.8, 008.20, 009.3, 010.6…010.8); 006.8 đổi nội dung theo DEC-166, ghi Lịch sử |
| CL-D05 | Đạt | TRC-01…05, 07, 09, 10 không báo |
| CL-D06 | Đạt | REF-01/02 không báo |
| CL-E01 | Đạt | Phần đã đổi không có NFR, HMI hay mô hình dữ liệu; văn bản thông báo của 010.6 ở R3 |
| CL-E02 | Không đạt | AUD-M05-37 (009.3) |
| CL-E03 | Đạt | Hàng R2 (`R:28`), R3 (`R:42`), R4 (`R:56`) đã đổi phân loại đúng; thiếu hàng R5 cho 009.3 chấm ở CL-A10, CL-E02 |
| CL-E04 | Đạt | Không có luật hay số liệu tự thêm; định nghĩa tài khoản theo DEC-019, DEC-085 |
| CL-F01 | Đạt | OP-M05-13, 14 có loại và trạng thái; không còn OP đã trả lời |
| CL-F02 | Không đạt | AUD-M05-39 |
| CL-F03 | Đạt | DEC-164…169 có ID register và SR khớp ý (lời văn 006.8 ở CL-B08); AUD-M05-27 đã sửa |
| CL-F04 | Đạt | SR không chọn trước điểm nào nguồn chưa chọn; AUD-40 là điểm SR còn im lặng (CL-B13) |
| CL-F05 | Đạt | 3.1 có DEC-140…169, ISS-207…254, QA-267…314, DEC-018, DEC-019, DEC-085; TRC-11 không báo |
| CL-F06 | Đạt | Có `[Vietnamese Doc]` |

Đủ 45 mã: 34 `Đạt`, 8 `Không đạt` (A10, B03, B08, B12, B13, C01, E02, F02), 3 `Không áp dụng — xác minh phát hành` (A01, A03, A08); không mục nào `Không kiểm được`.

Selfcheck của Author ghi `Đạt` cho RG-2 và RG-7 của 003.15 (`selfcheck-M05.md:144`), và không có dòng rà hồi quy cho các ID đổi ở 0.4 (008.20, 010.5, 010.6, 2.1).

## 8. Vòng trước (finding còn mở của ISH-AUD-M05-v1)

| AUD | Trạng thái | Bằng chứng mới |
|---|---|---|
| AUD-M05-27 (DEFECT TB, CL-B08, CL-F03, CL-B12) | Đã sửa | "Hệ thống phải loại khỏi xếp hạng Trending mọi Tag không gắn trên bài viết được tính nào." (`ISH-SR-M05.md:358`, 008.20); Phụ lục A "includes only active Tags currently attached to at least one counted post" (`:574`); T-153 sửa Given: "Tag hoạt động "anova" gắn trên một bài viết được tính, điểm 0" (`tests-M05.md:162`); thêm T-177, T-178 |
| AUD-M05-33 (OBSERVATION Thấp, CL-A06) | Đã sửa (ISS-244, QA-304, DEC-165) | DEC-165 (`decisions.md:877`); "| ISH-M05-010.5 | DEC-165, ISS-244, QA-304 | Nói thẳng |" (`ISH-SR-M05.md:583`); thêm 010.6 (`:400`) và R3 (`ISH-RT-M05.md:42`) |
| AUD-M05-34 (GAP Thấp, CL-A11) | Đã sửa (ISS-243, QA-303, DEC-164) | DEC-164 (`decisions.md:873`); 2.1 "Bước 1: bỏ qua dấu thanh, so từng ký tự từ trái sang phải" (`ISH-SR-M05.md:65`); T-180 "bá" trước "ban". Câu hỏi nhỏ ký hiệu/chữ số đã trả lời ("ký hiệu không phải chữ cái, rồi chữ số"). Ca T-181 dùng tên Tag không hợp lệ: lập finding mới AUD-M05-38, không mở lại AUD-34 |

Tổng: 3 Đã sửa, 0 Sửa chưa đủ, 0 Chưa sửa.

**Hồi quy mới:** AUD-M05-35…40, cả sáu do bản sửa 0.4, 0.5 gây ra hoặc mở ra.

## 9. Hồ sơ xác minh

**Trích đoạn (`grep -n -F`, mỗi lệnh khớp đúng số dòng ghi trong báo cáo; đường dẫn tính từ `.agents/.claude/system_analysis/output/`):**

- **SR (`specs/ISH-SR-M05.md`):**
  - `"Hệ thống phải loại khỏi xếp hạng Trending mọi Tag không gắn trên bài viết được tính nào."` → `:358`
  - `"| ISH-M05-010.5 | DEC-165, ISS-244, QA-304 | Nói thẳng |"` → `:583`
  - `"Khi hệ thống từ chối đổi tên vì Topic đã bị loại khỏi danh mục Topic"` → `:400`
  - `"Bước 1: bỏ qua dấu thanh, so từng ký tự từ trái sang phải"` → `:65`
  - `"Khi tác giả yêu cầu gợi ý Topic cho một bài viết đã gửi, hệ thống phải từ chối yêu cầu đó."` → `:216`
  - `"Khi tác giả thay đổi tiêu đề hoặc nội dung văn bản của bài viết sau khi nhận gợi ý Topic, hệ thống phải đánh dấu"` → `:211`
  - `"Trong khi gợi ý Topic của bài viết là gợi ý cũ, hệ thống phải hiển thị cảnh báo gợi ý cũ cho tác giả."` → `:213`
  - `"Trong khi gợi ý Topic của bài viết là gợi ý cũ, hệ thống phải cho phép tác giả yêu cầu gợi ý Topic lại."` → `:214`
  - `"| Gợi ý cũ | Tác giả yêu cầu gợi ý lại và nhận gợi ý mới | Gợi ý còn mới |"` → `:131`
  - `"Khi tác giả yêu cầu gợi ý Topic trong lúc soạn bài viết mới"` → `:192`
  - `"có chứa ký tự không phải chữ cái (kể cả chữ cái có dấu tiếng Việt), chữ số hoặc dấu gạch dưới"` → `:287`
  - `"Chỉ chữ cái, chữ số và dấu gạch dưới"` → `:535`
  - `"Hệ thống phải tính Tag bị vô hiệu hóa còn gắn trên một bài viết vào giới hạn tối đa 5 Tag"` → `:296`
  - `"Khi Mod hoặc Admin vô hiệu hóa một Tag, hệ thống phải ẩn Tag đó trên mọi bài viết đang gắn Tag đó."` → `:446`
  - `"Khi tác giả sửa một bài viết đã gửi, hệ thống phải cho phép tác giả thay đổi Tag của bài viết đó."` → `:290`
  - `"hệ thống phải không gửi thông báo về thay đổi đó cho tác giả."` → `:378`
  - `"| ISH-M05-009.3 | DEC-168, ISS-250, QA-310, DEC-065 | Nói thẳng |"` → `:578`
  - `"(DEC-155, M07 sở hữu)"` → `:615`
  - `"| 0.4 | 2026-10-05 | Sửa sau đợt xác minh ISH-AUD-M05-v1"` → `:473`
  - `"Routing: R2 (003.8 đã thành yêu cầu 003.16), R4 thêm hàng DEC-169"` → `:474`
  - `"Cho người dùng thấy lĩnh vực và từ khóa"` → `:334`
- **Routing và bản chụp:**
  - `"| DEC-159, QA-296, DEC-165, QA-304 |" specs/routing/ISH-RT-M05.md` → `:42`; cùng chuỗi trong `snapshot-ISH-RT-M05-v0.4.md` → `:42`
  - `"| DEC-159, QA-296 | Văn bản thông báo" snapshot-ISH-RT-M05-v0.3.md` → `:42`; trong `snapshot-ISH-RT-M05-v0.4.md` → 0
  - `"Thông báo in-app khi có bài mới trong Topic đang theo dõi" specs/routing/ISH-RT-M05.md` → `:70`
  - `"tác giả có được thông báo không (thuộc M07)" snapshot-ISH-SR-M05-v0.3.md` → `:594`
- **Register (`registers/decisions.md`):**
  - `"it is not available when the author edits an already-submitted post"` → `:885`
  - `"A Tag name may contain only letters (including Vietnamese letters with diacritics), digits and the underscore"` → `:881`
  - `"A disabled Tag still attached to a post counts toward that post's limit of 5 Tags"` → `:881`
  - `"old posts keep post_tags record but tag chip hidden from display"` → `:304`
  - `"When a Mod or Admin changes the Topics of a post, the author is not notified"` → `:889`
  - `"## Phase 5 — M07: Notification"` → `:375`
  - `"M07 owns delivery and any batching rule."` → `:835`
  - `"Content changed after suggest → flag is_stale, soft warning + re-suggest button"` → `:293`
  - `"Names are compared first on base letters only"` → `:873`
  - `"A Mod or Admin request to rename a Topic that has been removed from the catalog"` → `:877`
  - `"includes only active Tags currently attached to at least one counted post"` → `:861` (dòng này dời từ `:859` ở đợt xác minh do register thêm nhãn Clarified)
- **Tệp làm việc (`specs/audit/work/`):**
  - `"Như T-169, User A sửa nội dung, nhận gợi ý mới (còn mới), rồi gửi lại" tests-M05.md` → `:179`
  - `"Tag "c" và "c++" cùng 1 điểm" tests-M05.md` → `:185`
  - `"Tag "+a", "1a", "a" cùng 1 điểm" tests-M05.md` → `:190`
  - `"Bài viết có Tag "XácSuất"" tests-M05.md` → `:66`
  - `"Tag hoạt động "anova" gắn trên một bài viết được tính, điểm 0" tests-M05.md` → `:162`
  - `"User A sửa bài viết đó rồi yêu cầu gợi ý Topic" tests-M05.md` → `:191`
  - `"Tag "xác_suất_2024" được chấp nhận" tests-M05.md` → `:196`
  - `"Đạt: grep "gợi ý Topic" so 003.1, 003.9, 004.x, 005.x" selfcheck-M05.md` → `:144`

**Khẳng định vắng mặt:**
- **AUD-35:** `sed -n 207,216p ISH-SR-M05.md | grep -c -E "soạn|chưa gửi|bản nháp"` → 0 (không yêu cầu nào trong 003.4…003.15 giới hạn vào lúc soạn); `grep -n -E "chưa gửi|trong lúc soạn" ISH-SR-M05.md` → chỉ `:192` (câu cấp trên 003).
- **AUD-37:** `grep -n -E "009\.3|DEC-168|ISS-250|QA-310" ISH-RT-M05.md` → 0; `grep -n -i -E "thông báo[^|]*tác giả|tác giả[^|]*thông báo" ISH-RT-M05.md` → 0; `grep -n -E "OP-M05[^|]*(009\.3|chủ sở hữu|M07)" ISH-SR-M05.md` → 0 (OP-M05-14 nhắc M07 nhưng hỏi về người theo dõi, không về chủ sở hữu của 009.3).
- **AUD-39:** `sed -n 473p ISH-SR-M05.md | grep -c -E "R3|[Rr]outing"` → 0; dòng 0.5 chỉ nêu R2, R4.
- **AUD-40:** `grep -n -i -E "vô hiệu hóa[^|]*(sửa bài|gỡ|bỏ Tag|trình soạn)|(sửa bài|gỡ|trình soạn)[^|]*vô hiệu hóa"` trên SR và routing → 0; `grep -n -i -E "disabled[^|]*(edit|remove|editor)|(edit|remove|editor)[^|]*disabled"` và `"tag[^|]{0,80}(ẩn|hidden)[^|]{0,80}(sửa|edit|editor|soạn)"` trên decisions.md, qa-log.md, issue-queue.md → 0.
- **RG-5 (OP đã xóa):** `grep -n -E "OP-M05-(0[1-9]|1[0-2])"` trên SR, routing, `tests-M05.md` → chỉ các dòng Lịch sử `:471`, `:472`, `:474`.
- **Tồn kho:** tập OWNED và REFERENCING của tôi trùng hoàn toàn với `inventory-M05.json` của Author (so bằng script ở thư mục tạm của phiên); `registers_sha` trùng (`275497dc…`).

**Ứng viên đã cân nhắc và loại:**
- **5.2 không có hàng cho đổi tên Topic đã loại (010.5).** Loại vì từ chối không đổi trạng thái; ISH-AUD-M05-v1 đã loại cùng lý do.
- **Định nghĩa "Tài khoản bị cấm" ở 2.1 ("vẫn đăng nhập được") so với DEC-018 ("BANNED/DELETED → block").** Loại: DEC-085 và DEC-019 ("BANNED screen") cho thấy "block" là chặn mọi chức năng trừ màn hình bị cấm; không hành vi nào của M05 phụ thuộc chi tiết này (007.8 tính tài khoản bị cấm bất kể đăng nhập).
- **006.18 áp cho mọi chỗ hiển thị Tag, kể cả bảng Trending Tag (M14) và tự hoàn thành (M06).** Loại: DEC-166 (2) là quy tắc chung về tên Tag; M05 sở hữu Tag.
- **Lịch sử 0.4 không nêu cập nhật 3.1 và nguồn Phụ lục A của 008.11, 008.12.** Loại: dòng 0.5 đã nêu "3.1 cập nhật khoảng DEC-140…169"; cập nhật nguồn Phụ lục A đi kèm nội dung đã ghi, cùng thước với đợt xác minh. Chỉ thay đổi routing R3 lập finding (AUD-39).
- **Yêu cầu gợi ý bị từ chối vì lý do khác văn bản ngắn (bài đã gửi, chức năng tắt) có tính vào 10/phút không.** Ghi chú nhỏ ở mục 4.2: DEC-167 chỉ nói văn bản ngắn; hệ quả gần như không quan sát được vì màn hình sửa bài không có gợi ý. Không lập finding.
- **Giới hạn độ dài tên Topic khi đổi tên; thứ tự giữa các ký hiệu với nhau ở 2.1.** Nguồn im lặng, hệ quả nhỏ (danh mục 11 Topic cố định, tên Tag chỉ còn "_" là ký hiệu). Không lập finding.
- **WARN TST-03 (T-199, T-200).** Không lập finding: đã có OP và giải thích (`selfcheck-M05.md:161`).
- **Selfcheck thiếu dòng rà hồi quy cho ID đổi ở 0.4 và còn nhắc 010.4 đã bỏ (`selfcheck-M05.md:99`).** Tệp làm việc; tôi tự chấm RG-1…RG-7 ở mục 4.2. Không lập finding riêng.

**Mức và lớp:**
- AUD-35: CL-C01 mặc định Cao, hạ một mức (lý do trong finding).
- AUD-36: CL-B08 mặc định Trung bình, giữ.
- AUD-37: CL-E02 mặc định Cao, hạ một mức (lý do trong finding).
- AUD-38: CL-B12 mặc định Trung bình, hạ một mức.
- AUD-39: CL-F02 mặc định Thấp, giữ.
- AUD-40: CL-B13 mặc định Trung bình, hạ một mức; lớp GAP vì nguồn im lặng và cần câu trả lời mới.
