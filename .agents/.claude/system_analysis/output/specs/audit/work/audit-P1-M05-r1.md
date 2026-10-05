# Tệp lượt — ISH-AUD-M05-r1 · lượt P1 (Độ phủ nguồn và ranh giới module)
<!-- [Vietnamese Doc] -->

| Trường | Giá trị |
|---|---|
| Module | M05 |
| Vòng | 1 |
| Lượt | P1 |
| SR được audit | ISH-SR-M05, phiên bản 0.1 (2026-10-04), trạng thái Bản nháp |
| Routing | ISH-RT-M05, phiên bản 0.1 (2026-10-04) |
| Tóm tắt Author đã nhận và không dùng | Không có (lời gọi chỉ gồm module, vòng, lượt, gốc repo) |
| Ngày audit | 2026-10-04 |
| Kết luận của lượt | **Chưa đạt** — còn 5 DEFECT và 1 CONFLICT mở |

Đầu ra kèm: `WORK/audit-inventory-P1-M05-r1.md` / `.json`, `WORK/coverage-M05-r1.md`, `WORK/check-P1-M05-r1.json`.

Trình tự đã làm: inventory riêng (P1.1) → đọc nguyên văn DRAFT §3 và các mục DRAFT liên quan, đọc từng mục OWNED (76) và REFERENCING (20), đọc có chủ đích KEYWORD → lập cột Mong đợi của ma trận **trước khi** mở thân SR/routing (P1.2; chỉ đọc header SR/routing trước mốc này) → `check_sr.py` (P1.3) → đối chiếu (P1.4) → mở `disposition-M05.md` và các dòng P1 của `selfcheck-M05.md` (P1.5) → chấm (P1.6). Không mở `tests-M05.md`; không đọc tệp lượt P2/P3.

## 1. Phát hiện nháp

### P1-01 — DEC-145 chỉ được đưa một phần: Topic nguồn sau khi gộp vẫn có thể được xếp Trending và được theo dõi

| Lớp | DEFECT | Mức đề xuất | Trung bình | Checklist | CL-A10 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-011.2 (`ISH-SR-M05.md:387`); ISH-M05-008 (`ISH-SR-M05.md:307`); ISH-M05-007.1 (`ISH-SR-M05.md:294`).
- **Bằng chứng trong nguồn:** "After a merge, the source Topic is removed from the Topic catalog: it can no longer be selected, suggested, ranked in Trending or followed; …" (`decisions.md:790`, DEC-145).
- **Bằng chứng trong SR:**
  - "Khi Mod hoặc Admin gộp Topic nguồn vào Topic đích, hệ thống phải loại Topic nguồn khỏi danh mục Topic." (`ISH-SR-M05.md:387`)
  - Định nghĩa: "| Danh mục Topic | Tập Topic một tầng mà hệ thống cho phép chọn cho bài viết. |" (`ISH-SR-M05.md:28`) — danh mục được định nghĩa theo việc *chọn cho bài viết*.
  - "Hệ thống phải xếp hạng các Topic và các Tag theo điểm Trending tính trên 7 ngày gần nhất." (`ISH-SR-M05.md:307`) — không giới hạn ở Topic trong danh mục.
  - "Khi người dùng đã đăng nhập yêu cầu theo dõi một Topic chưa theo dõi, hệ thống phải ghi nhận người dùng đó đang theo dõi Topic đó." (`ISH-SR-M05.md:294`) — không giới hạn ở Topic trong danh mục.
- **Vấn đề:** Bốn hệ quả DEC-145 nêu cho Topic nguồn: (1) không chọn được — có ISH-M05-002.2 qua định nghĩa danh mục; (2) không gợi ý được — có ISH-M05-004.5; (3) không xếp Trending và (4) không theo dõi được — không có yêu cầu hay hàng routing nào. Với định nghĩa ở 2.1, "loại khỏi danh mục Topic" chỉ chặn việc chọn cho bài viết; ISH-M05-008 và ISH-M05-007.1 vẫn áp dụng cho Topic nguồn. Selfcheck ghi CL-A10 `Đạt`.
- **Hệ quả nếu không sửa:** Topic nguồn có thể vẫn xuất hiện trong bảng Trending Topic (điểm 0) và người dùng vẫn theo dõi được một Topic đã bị gộp; ca kiểm cho hai hệ quả này không viết được từ SR.
- **Hướng xử lý (Author quyết cách viết):** thêm yêu cầu (Nói thẳng, DEC-145) cho phần "ranked in Trending" và "followed", hoặc sửa định nghĩa danh mục và các yêu cầu 007/008 để chỉ áp dụng cho Topic trong danh mục; cập nhật Phụ lục A.

### P1-02 — QA-011 chỉ được đưa một phần: Guest xem danh sách Tag và xem phân loại trên bài viết không có chỗ đi

| Lớp | DEFECT | Mức đề xuất | Trung bình | Checklist | CL-A10 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-001.3 (`ISH-SR-M05.md:142`); Phụ lục A (`ISH-SR-M05.md:441`); routing R5 (`ISH-RT-M05.md:65`).
- **Bằng chứng trong nguồn:**
  - "  - CLAS: Xem danh sách Topic / Tag / Khối lớp" (`qa-log.md:134`, QA-011)
  - "  - AI: Xem AI Summary + AI Classification trên post" (`qa-log.md:137`, QA-011)
- **Bằng chứng trong SR/routing:**
  - "Hệ thống phải cho phép mọi người dùng, kể cả Guest, xem danh sách Topic trong danh mục Topic." (`ISH-SR-M05.md:142`)
  - Phụ lục A của chính yêu cầu đó trích đủ ba đối tượng: "| ISH-M05-001.3 | QA-011 | Nói thẳng | Guest "Xem danh sách Topic / Tag / Khối lớp" |" (`ISH-SR-M05.md:441`)
  - Routing chỉ nhận phần Khối lớp: "… danh sách Khối lớp cho Guest | M03 (F-POST-09), M02 — …" (`ISH-RT-M05.md:65`)
  - Disposition: "\"AI Classification trên post\" không còn (DEC-050)" (`disposition-M05.md:73`) — DEC-050 không nói phân loại không còn hiển thị trên bài viết.
- **Vấn đề:** Phần "Tag" của "Xem danh sách Topic / Tag / Khối lớp" và phần "AI Classification trên post" (Guest thấy Topic đã gắn của bài viết) không nằm ở SR cũng không ở routing. Tìm vắng mặt: `grep -n -i -c "danh sách Tag"` trên SR và routing → 0 và 0; `grep -n -i -E "hiển thị (các )?(Topic|Tag) (của|trên) bài"` → 0; `grep -n -i "Classification"` → 0. Selfcheck ghi CL-A10 `Đạt`.
- **Hệ quả nếu không sửa:** Quyền Guest xem Tag và xem Topic/Tag đã gắn trên bài viết không có chủ sở hữu; ISH-M05-012.1/012.5 ("ẩn"/"hiển thị lại" Tag trên bài viết) dựa trên một hành vi hiển thị chưa được viết ở đâu.
- **Hướng xử lý (Author quyết cách viết):** đặt hai phần còn lại vào SR (nếu M05 sở hữu) hoặc routing R5 kèm module sở hữu (M03 cho trang bài viết; M14/M06 cho danh sách Tag), hoặc OP loại Đề xuất nếu chưa chắc chủ sở hữu (RULES §5 mục 2); sửa lý do trong disposition.

### P1-03 — QA-235 (không đặt ngưỡng tối thiểu để vào Trending) bị chuyển hết sang M14 dù xếp hạng Topic/Tag thuộc M05

| Lớp | DEFECT | Mức đề xuất | Trung bình | Checklist | CL-E03 |
|---|---|---|---|---|---|

- **Vị trí:** routing R5 (`ISH-RT-M05.md:62`); ISH-M05-008 (`ISH-SR-M05.md:307`).
- **Bằng chứng trong nguồn:**
  - "| QA-235 | ISS-175: Có ngưỡng tối thiểu (min upvote/comment) để vào Trending không? | Không đặt ngưỡng cho MS1 — dataset demo nhỏ …" (`qa-log.md:939`)
  - Tab Trending gồm cả Topic và Tag: "M14 Feed consists of 4 tabs: **Trending** (3 sub-views: Post/Topic/Tag), …" (`decisions.md:695`, DEC-125)
  - Xếp hạng Topic/Tag là quyết định của M05: "Topics and Tags are ranked by Trending score, highest first. …" (`decisions.md:822`, DEC-153, section M05)
- **Bằng chứng trong routing/disposition:**
  - "| QA-235, ISS-175, QA-236, ISS-176 | Không đặt ngưỡng tối thiểu để vào Trending; không loại bài của người dùng BANNED hoặc cảnh cáo nặng | M14 — chưa có SR, ghi nguồn QA-235, QA-236 |" (`ISH-RT-M05.md:62`)
  - "| QA-235, ISS-175 | Không ngưỡng tối thiểu vào Trending | R5 | M14 (hiển thị) |" (`disposition-M05.md:94`)
- **Vấn đề:** "Ngưỡng để vào Trending" quyết định Topic/Tag nào có mặt trong bảng xếp hạng — đó là quy tắc xếp hạng, không phải hiển thị; xếp hạng Topic/Tag do M05 sở hữu (ISH-M05-008, DEC-052/153). QA-235 không nói rõ chỉ áp dụng cho Trending Post. Phần QA-236 đã có hệ quả cho Topic/Tag qua DEC-146 (ISH-M05-008.3) nên không lỗi; phần QA-235 thì SR không có yêu cầu nào và không có OP về chủ sở hữu. Tìm vắng mặt: `grep -n -i "ngưỡng" ISH-SR-M05.md` → chỉ dòng 459 (ngưỡng 10 tiếng của gợi ý Topic); `grep -n "QA-235\|ISS-175" ISH-SR-M05.md` → chỉ dòng 75–76 (mục 3.1), không có ở Phụ lục A. Selfcheck ghi CL-E03 `Đạt`.
- **Hệ quả nếu không sửa:** Không xác định được Topic/Tag có điểm thấp (kể cả 0) có vào bảng xếp hạng không; M14 sẽ nhận một quy tắc xếp hạng mà nó không sở hữu.
- **Hướng xử lý (Author quyết cách viết):** theo RULES §5 mục 2: viết phần áp dụng cho Topic/Tag ở M05 và ghi OP loại Đề xuất để stakeholder chốt chủ sở hữu, hoặc tách hàng routing: phần Trending Post → R5 M14, phần Topic/Tag → SR/OP.

### P1-04 — Disposition không có dòng riêng cho các mục KEYWORD không nằm ở SR/routing

| Lớp | DEFECT | Mức đề xuất | Thấp | Checklist | CL-A03 |
|---|---|---|---|---|---|

- **Vị trí:** `disposition-M05.md:69` (tiêu đề nhóm KEYWORD).
- **Bằng chứng:** "## KEYWORD và CROSS-CUTTING (chỉ ghi mục đã đọc và có liên hệ; các mục KEYWORD còn lại khớp từ khóa chung "follow/lớp/gộp/category/dropdown" trong ngữ cảnh module khác — không liên quan)" (`disposition-M05.md:69`).
- **Bằng chứng nguồn (mẫu có chủ đích):** ISS-168 "M14 cần những tab/view nào cho Feed? | Closed | 4 tab: Trending (sub Post/Topic/Tag) …" (`issue-queue.md:258`) và QA-225 (`qa-log.md:929`) có từ khóa nghiệp vụ topic/tag/trending, có trong inventory của chính Author (`inventory-M05.md:172`, `inventory-M05.md:214`), nhưng `grep -c "ISS-168\|QA-225"` trên disposition, SR, routing → 0, 0, 0.
- **Vấn đề:** RULES §7.7 yêu cầu mục không liên quan ghi "một dòng: ID, lý do một câu". Đối chiếu với inventory P1: 30 mục KEYWORD không có trong SR, routing hay disposition (DEC-066, DEC-070, DEC-097, DEC-098, ISS-101, ISS-126, ISS-168, ISS-173, ISS-177, ISS-181, QA-004…007, QA-012, QA-022, QA-112, QA-149, QA-153, QA-194, QA-203, QA-211, QA-225, QA-232…234, QA-244, ISS-190, QA-249, QA-262). Lý do gộp không chứa "trending/topic/tag", nên không bao được ISS-168/QA-225. Selfcheck ghi CL-A03 `Đạt`.
- **Mức:** hạ một mức từ Trung bình xuống Thấp vì các mục lấy mẫu (ISS-168, QA-225, ISS-173, QA-232…234, ISS-177, QA-022, QA-112, DEC-097/098, QA-244) đọc nội dung thì đều thuộc module khác hoặc trùng ý với DEC-125 đã có ở R5; không thấy mục bị sót hành vi M05.
- **Hướng xử lý (Author quyết cách viết):** thêm một dòng cho mỗi mục KEYWORD trong inventory của Author mà không nằm ở SR/routing.

### P1-05 — Lệch DRAFT §7.2 (tín hiệu Trending) với DEC-052 không có dấu vết

| Lớp | DEFECT | Lớp phụ | OBSERVATION | Mức đề xuất | Thấp | Checklist | CL-A08 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008, Phụ lục A (`ISH-SR-M05.md:503`).
- **Bằng chứng trong nguồn:**
  - "### 7.2 Trending / Popular" (`iShare_modules.md:333`), liệt kê "- Views" (`iShare_modules.md:337`) và "- Bookmarks" (`iShare_modules.md:340`) dưới "Có thể dựa trên".
  - "- Score: Σ(1 + upvotes×2 + comments×1) across all posts in window …" (`decisions.md:308`, DEC-052) — không có lượt xem hay bookmark.
- **Bằng chứng trong SR:** "| ISH-M05-008 | DEC-052, DEC-142, QA-106, ISS-082, ISS-210, QA-270 | Nói thẳng | |" (`ISH-SR-M05.md:503`). Tìm vắng mặt: `grep -c "§7"` trên SR, routing → 0, 0; `grep -i -c "view\|lượt xem\|bookmark"` → 0, 0; `grep "§7.2\|7\.2" disposition-M05.md` → 0; `grep "§7.2\|Bookmarks\|views"` trên registers → không có ISS/QA nào hỏi về lệch này.
- **Vấn đề:** SR theo register (đúng §7.5) nhưng cột Nguồn không có DRAFT §7.2 và không có dấu vết đã báo stakeholder việc bỏ Views/Bookmarks khỏi điểm Trending Topic/Tag. Ghi chú: DRAFT dùng "Có thể dựa trên", và QA-277 đã chốt "upvotes"/"comments" gồm gì, nên khả năng cao chỉ cần xác nhận hình thức. Selfcheck ghi CL-A08 `Đạt` (chỉ xét §3.1, §3.2, §3.4).
- **Hệ quả nếu không sửa:** Người đọc DRAFT không thấy vì sao Views/Bookmarks không có trong công thức.
- **Hướng xử lý (Author quyết cách viết):** thêm DRAFT §7.2 vào cột Nguồn của ISH-M05-008 (và 008.1/008.2), ghi lệch vào Phụ lục B hoặc báo stakeholder như OBSERVATION (khối dưới).
- **Khuôn hỏi stakeholder (lớp phụ OBSERVATION):**
  - Vấn đề: DRAFT §7.2 gợi ý Trending có thể dựa trên Views, Stars, Comments, Bookmarks, Recency; DEC-052 chỉ dùng upvote, bình luận và thưởng bài mới cho Trending Topic/Tag.
  - Nguồn: `iShare_modules.md:337` "- Views", `iShare_modules.md:340` "- Bookmarks"; `decisions.md:308` DEC-052.
  - Lựa chọn: A) Xác nhận DEC-052 ghi đè DRAFT §7.2 cho Trending Topic/Tag — hệ quả: chỉ thêm dấu vết, không đổi yêu cầu. B) Thêm lượt xem/bookmark vào công thức — hệ quả: đổi ISH-M05-008.1/008.2 và cần hệ số mới.
  - Đề xuất: A, vì DEC-052/142/146 đã chốt công thức và các tương tác được tính.

### P1-06 — Thông báo khi có bài mới trong Topic đang theo dõi: QA-043/DEC-141 mâu thuẫn với danh sách sự kiện DEC-065, chưa được hỏi

| Lớp | CONFLICT | Mức đề xuất | Trung bình | Checklist | CL-A09 |
|---|---|---|---|---|---|

- **Vị trí:** routing R5 (`ISH-RT-M05.md:64`); 2.1 "Theo dõi Topic" (`ISH-SR-M05.md:52`); Lý do 5.9 (`ISH-SR-M05.md:288`).
- **Bằng chứng trong nguồn:**
  - "- **Answer:** Follow: User (nhận noti khi họ post), Topic (nhận noti khi có post mới trong topic), …" (`qa-log.md:521`, QA-043, Phase 4)
  - DEC-141 (muộn nhất): "… Notification delivery on new posts in a followed Topic remains M07's responsibility (per QA-043's own implication), …" (`decisions.md:774`)
  - "### DEC-065: Notification event list + channel" (`decisions.md:375`); bảng sự kiện (`decisions.md:376–390`) không có sự kiện bài mới trong Topic đang theo dõi (`awk 'NR>=375 && NR<=392' decisions.md | grep -i -c topic` → 0); QA-123 gọi đó là "Full notification event list?" (`qa-log.md:774`).
- **Bằng chứng trong SR/routing:**
  - "| DEC-141, QA-043, ISS-051, DEC-065, QA-123 | Thông báo khi có bài mới trong Topic đang theo dõi; lưu ý DEC-065 chưa liệt kê sự kiện này | M07 — chưa có SR, ghi nguồn QA-043, DEC-141 |" (`ISH-RT-M05.md:64`)
  - "| Theo dõi Topic | Quan hệ giữa một người dùng đã đăng nhập và một Topic mà người dùng đó muốn nhận cập nhật. |" (`ISH-SR-M05.md:52`)
  - Không có ISS/QA/DEC hay OP nào nêu mâu thuẫn: `grep -n "DEC-065" issue-queue.md qa-log.md` → chỉ QA-123 (`qa-log.md:774`); `grep -n "OP-M05" ISH-SR-M05.md | grep -i "thông báo"` → chỉ OP-M05-07 (thông báo khi Mod đổi Topic, vấn đề khác).
- **Vấn đề:** Hai nguồn đã đóng kết luận khác nhau về cùng một vấn đề (theo dõi Topic có tạo thông báo không). Author đã thấy (ghi chú ở R5) nhưng không hỏi; RULES §7.6 yêu cầu coi là CONFLICT. Phần thông báo thuộc M07, nhưng hệ quả quan sát được của "Theo dõi Topic" ở M05 (2.1 và Lý do 5.9 nói "nhận cập nhật") phụ thuộc vào câu trả lời. Selfcheck ghi CL-A09 `Đạt` ("Không còn cặp cùng vấn đề kết luận khác chưa hỏi").
- **Hệ quả nếu không sửa:** Người theo dõi Topic có thể không bao giờ nhận thông báo (nếu M07 viết theo DEC-065), trái với QA-043/DEC-141; M05 mô tả "nhận cập nhật" mà không module nào thực hiện.
- **Khuôn hỏi stakeholder:**
  - Vấn đề: Theo dõi một Topic có tạo thông báo in-app khi có bài mới trong Topic đó không?
  - Nguồn: QA-043 (`qa-log.md:521`) "Topic (nhận noti khi có post mới trong topic)"; DEC-141 (`decisions.md:774`); DEC-065 (`decisions.md:375`) bảng sự kiện đầy đủ không có sự kiện này.
  - Lựa chọn: A) Có — thêm sự kiện "bài mới trong Topic đang theo dõi" vào DEC-065 (M07) — hệ quả: M07 cần quy tắc gộp/giới hạn thông báo cho Topic đông bài. B) Không — theo dõi Topic chỉ ảnh hưởng tab Following (M14) — hệ quả: sửa 2.1 và Lý do 5.9 của SR M05, ghi QA-043 là bị thay.
  - Đề xuất: A, vì DEC-141 là quyết định muộn nhất và khẳng định lại việc thông báo; cần stakeholder chốt và ghi DEC sửa DEC-065.

### P1-07 — Văn bản cũ trong register chưa cập nhật theo quyết định muộn hơn

| Lớp | OBSERVATION | Mức đề xuất | Thấp | Checklist | CL-A09 |
|---|---|---|---|---|---|

- **Vị trí:** không có vị trí trong SR — SR đã theo quyết định muộn hơn.
- **Bằng chứng trong nguồn:**
  - "| Topic | A broad subject-area classification for Posts (e.g. Mathematics, Life Skills). Not limited to school curriculum. List to be finalized in BA. | Draft |" (`glossary.md:14`) ↔ DEC-048 "Topic list (11, final)" (`decisions.md:280`).
  - "| AI Classification | Suggests Topic and Tags for a Post automatically. User/Moderator reviews before publish. | Draft |" (`glossary.md:29`) ↔ QA-269 (Tag không có gợi ý AI, `qa-log.md:1004`) và DEC-144 (`decisions.md:786`).
  - DEC-125: "**Following** (chronological, from Follow targets established in M07 — User/Topic/Post)" (`decisions.md:695`) ↔ DEC-141 "M05 (Topic & Tag) owns the Follow/Unfollow behaviour for Topic" (`decisions.md:774`).
- **Vấn đề:** Các câu cũ không mang nhãn `[Amended]`/`[Clarified]`. SR viết đúng theo quyết định muộn hơn nên không phải DEFECT của SR; rủi ro là người viết SR M07/M13/M14 đọc glossary hoặc DEC-125 và hiểu sai.
- **Khuôn hỏi stakeholder:**
  - Vấn đề: Có đánh dấu ghi đè các câu cũ ở glossary (Topic, AI Classification) và DEC-125 (chủ sở hữu Follow Topic) không?
  - Nguồn: `glossary.md:14`, `glossary.md:29`, `decisions.md:695`.
  - Lựa chọn: A) Đánh dấu `[Amended …]` trỏ tới DEC-048, QA-269, DEC-144, DEC-141 — hệ quả: register nhất quán. B) Giữ nguyên — hệ quả: SR các module sau có thể trích nhầm.
  - Đề xuất: A.

## 2. Kết quả checklist của lượt

| Mã | Kết quả | Finding / ghi chú |
|---|---|---|
| CL-A01 | Đạt | Mọi câu của DRAFT §3.1–§3.4 và các câu M05 ở §4.5, §11.2, §11.5, §8.1 có chỗ đi (ma trận hàng 1–15). Ghi chú: hàng R5 Lớp/Khối (`ISH-RT-M05.md:65`) không ghi DRAFT §3.3 làm nguồn — dấu vết yếu, nội dung vẫn bao được ý; không lập finding. DRAFT §7.2 xem CL-A08 |
| CL-A02 | Đạt | `check_sr.py` không có COV-01; COV-00: OWNED=76, SR=70, routing=23. Ma trận xác nhận vị trí từng mục OWNED; các chỗ chỉ đưa một phần được chấm ở CL-A10 |
| CL-A03 | Không đạt | P1-04. REFERENCING 20/20 có phân loại hợp lý; KEYWORD lấy mẫu có chủ đích: QA-011 phân loại thiếu phần (P1-02), QA-235 sai chỗ (P1-03, chấm ở CL-E03), 30 mục không có dòng riêng |
| CL-A04 | Đạt | Không có COV-02, TRC-06. Kiểm tay: DEC-065 (`decisions.md:375`), QA-123 (`qa-log.md:774`), DEC-033 (`decisions.md:206`) tồn tại; "DRAFT §3.3" ở ISH-M05-006.1 khớp `iShare_modules.md:159` |
| CL-A08 | Không đạt | P1-05. §3.1, §3.2, §3.4, §4.5, §11.2 đã xử lý đúng §7.5 (DEC-143, QA-269, DEC-141, DEC-144) |
| CL-A09 | Không đạt | P1-06 (CONFLICT chưa hỏi); P1-07 (OBSERVATION). QA-033→DEC-140, DEC-050→DEC-147, DEC-132→DEC-149 xử lý đúng (R6, có nhãn ghi đè) |
| CL-A10 | Không đạt | P1-01 (DEC-145), P1-02 (QA-011). 17 nguồn COV-03 còn lại đã kiểm: phần SR và phần routing không trùng, không sót |
| CL-E01 | Đạt | Mục 4 không có "phải"; mục 5 không có bảng/trường, thời gian phản hồi, bố cục; chu kỳ tính lại → R2 (`ISH-RT-M05.md:25`), thông điệp → R3 |
| CL-E02 | Đạt | Không có yêu cầu mô tả kết quả nhìn thấy ở module khác: hiển thị Trending → R5 M14; tìm/lọc/autocomplete → R5 M06; thông báo → R5 M07; công tắc AI → R5 M10; Lớp/Khối → R5 M03/M02 |
| CL-E03 | Không đạt | P1-03. Các hàng R5 khác có module và "chưa có SR, ghi nguồn"; R6 có "bị thay bởi"; R7 có lý do |
| CL-E04 | Đạt | 4.1 "Không có." (`ISH-SR-M05.md:93`); không có luật, quyền riêng tư hay số liệu tự thêm (168 giờ = 7 ngày trượt của DEC-052) |
| CL-F03 | Đạt | Mọi câu trả lời của stakeholder có ID (ISS-207…227, QA-267…287, DEC-140…153) và SR khớp; không thấy số liệu, ngoại lệ hay quyền hạn chỉ tồn tại trong SR |

So với selfcheck của Author (P1.5): Author ghi `Đạt` cho CL-A03, CL-A08, CL-A09, CL-A10, CL-E03; lượt này chấm `Không đạt` cho cả năm mục (P1-01…P1-06).

## 3. Kết quả kiểm tra tự động

ERROR = 0, WARN = 0, INFO = 19. Lệnh đã chạy:

```
python3 .agent-instructions/system_analysis/shared/sr-tools/check_sr.py \
  --sr .agents/.claude/system_analysis/output/specs/ISH-SR-M05.md \
  --routing .agents/.claude/system_analysis/output/specs/routing/ISH-RT-M05.md \
  --inventory .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-P1-M05-r1.json \
  --json .agents/.claude/system_analysis/output/specs/audit/work/check-P1-M05-r1.json
```

Không có ERROR/WARN. INFO: COV-03 × 17 (DEC-047, DEC-049, DEC-050, DEC-051, DEC-052, DEC-140, DEC-141, DEC-147, DEC-150, ISS-207, QA-101, QA-102, QA-104, QA-106, QA-107, QA-268, QA-278 — đã kiểm tay, xem CL-A10); COV-00 (OWNED=76, SR=70, routing=23); TST-99 (không truyền `--tests`, đúng cho P1). Không có INV-01 (inventory mới). Yêu cầu cấp trên = 12, cấp dưới = 92.

Inventory riêng: `inventory.py --module M05 --keywords "topic,tag,chủ đề,thẻ,trending,gộp,merge,flat,is_stale,stale,gợi ý,suggest,suggestion,freeform,hashtag,follow topic,theo dõi topic,post_tags,rolling,phân loại,classification,category"` → OWNED=76, REFERENCING=20, CROSS=42, DRAFT=27, KEYWORD=82. Từ khóa lấy từ tên module, dòng M05 ở `module-registry.md:12` và hành vi liền kề ở DRAFT (§4.5, §7.2, §11.2); không lấy từ tệp của Author. Module phụ thuộc đã quét: M14 (liệt kê M05 làm dependency), M13, M10, M06, M07, M03/M02.

## 4. Hồ sơ xác minh

Mọi trích đoạn ở mục 1 đã chạy `grep -n -F` hoặc `Grep` và khớp số dòng:

- P1-01: `grep -n -F "it can no longer be selected, suggested, ranked in Trending or followed" decisions.md` → 1 (dòng 790); `grep -n -F "hệ thống phải loại Topic nguồn khỏi danh mục Topic" ISH-SR-M05.md` → 1 (387); `… "Tập Topic một tầng mà hệ thống cho phép chọn cho bài viết"` → 1 (28); `… "Hệ thống phải xếp hạng các Topic và các Tag theo điểm Trending"` → 1 (307); `… "yêu cầu theo dõi một Topic chưa theo dõi"` → 1 (294). Vắng mặt: `grep -n "Topic nguồn" ISH-SR-M05.md` → 8 dòng (29, 30, 120, 376, 386–389), không dòng nào thuộc ISH-M05-007/008; `grep -n -i "danh mục" ISH-SR-M05.md | grep -E "ISH-M05-00(7|8)"` → 0.
- P1-02: `grep -n -F "CLAS: Xem danh sách Topic / Tag / Khối lớp" qa-log.md` → 1 (134); `… "AI: Xem AI Summary + AI Classification trên post"` → 1 (137); `… "kể cả Guest, xem danh sách Topic" ISH-SR-M05.md` → 1 (142); `… "danh sách Khối lớp cho Guest" ISH-RT-M05.md` → 1 (65); `… "\"AI Classification trên post\" không còn (DEC-050)" disposition-M05.md` → 1 (73). Vắng mặt: `grep -i -c "danh sách Tag"` SR → 0, routing → 0; `grep -i -E "hiển thị (các )?(Topic|Tag) (của|trên) bài"` → 0; `grep -i "Classification"` SR+routing → 0; `grep -n "QA-011"` → chỉ dòng 76, 441, 501 (SR) và 65 (routing).
- P1-03: `grep -n -F "QA-235 | ISS-175: Có ngưỡng tối thiểu (min upvote/comment) để vào Trending không?" qa-log.md` → 1 (939); `… "Không đặt ngưỡng cho MS1 — dataset demo nhỏ"` → 939; `… "Không đặt ngưỡng tối thiểu để vào Trending" ISH-RT-M05.md` → 1 (62); `… "**Trending** (3 sub-views: Post/Topic/Tag)" decisions.md` → 1 (695); `… "Topics and Tags are ranked by Trending score, highest first."` → 1 (822); `… "QA-235, ISS-175 | Không ngưỡng tối thiểu vào Trending | R5 | M14 (hiển thị)" disposition-M05.md` → 1 (94). Vắng mặt: `grep -n -i "ngưỡng" ISH-SR-M05.md` → 1 (459, ngưỡng gợi ý Topic); `grep -n "QA-235\|ISS-175" ISH-SR-M05.md` → 75, 76 (mục 3.1).
- P1-04: `grep -n -F "các mục KEYWORD còn lại khớp từ khóa chung" disposition-M05.md` → 1 (69); `grep -n -F "| ISS-168 |" issue-queue.md` → 258; `grep -n -F "QA-225 | ISS-168" qa-log.md` → 929; `grep -n "ISS-168\|QA-225" inventory-M05.md` → 172, 214; `grep -c "ISS-168\|QA-225"` disposition/SR/routing → 0/0/0. Danh sách 30 mục do script Python đối chiếu inventory P1 với tập ID có trong SR, routing, disposition (có mở rộng dải `…`).
- P1-05: `grep -n -F "### 7.2 Trending / Popular" iShare_modules.md` → 333; `grep -n -F -- "- Views"` → 337 (và 436, mục khác); `grep -n -F -- "- Bookmarks"` → 340; `grep -n -F "Score: Σ(1 + upvotes×2 + comments×1)" decisions.md` → 308; `grep -n -F "| ISH-M05-008 | DEC-052, DEC-142, QA-106, ISS-082, ISS-210, QA-270 | Nói thẳng | |" ISH-SR-M05.md` → 503. Vắng mặt: `grep -c "§7"` SR/routing → 0/0; `grep -i -c "view\|lượt xem\|bookmark"` → 0/0; `grep "§7.2\|7\.2" disposition-M05.md` → 0; `grep "§7.2\|Bookmarks\|views" registers/*.md` → chỉ các dòng Profile/Bookmarks và DEC-125/126, không có ISS/QA về lệch.
- P1-06: `grep -n -F "Topic (nhận noti khi có post mới trong topic)" qa-log.md` → 521; `grep -n -F "### DEC-065: Notification event list + channel" decisions.md` → 375; `awk 'NR>=375 && NR<=392' decisions.md | grep -i -c topic` → 0; `Grep "Notification delivery on new posts in a followed Topic remains M07's responsibility|from Follow targets established in M07 — User/Topic/Post" decisions.md` → 2 (774, 695); `grep -n -F "lưu ý DEC-065 chưa liệt kê sự kiện này" ISH-RT-M05.md` → 64; `grep -n -F "muốn nhận cập nhật" ISH-SR-M05.md` → 52; `grep -n -F "Người dùng theo dõi để nhận cập nhật" ISH-SR-M05.md` → 288; `grep -n "DEC-065" issue-queue.md qa-log.md` → chỉ `qa-log.md:774` (QA-123).
- P1-07: `Grep "^\| (Topic|AI Classification) \|" glossary.md` → 14, 29; `decisions.md:695` như trên; DEC-048 tiêu đề ở `decisions.md:280`.

Finding bị loại hoặc chỉnh:

- (Loại) "R6 phân loại cả DRAFT §3.3 là bị thay thế" — đọc lại `ISH-RT-M05.md:80`: hàng R6 chỉ nói phần Personalized Feed; phần Lớp/Khối đã có hàng R5 (`ISH-RT-M05.md:65`). Chỉ còn thiếu trích DRAFT §3.3 ở hàng R5 → ghi chú ở CL-A01, không lập finding.
- (Loại) "DEC-133 nằm ở R1 thay vì R5" — hàng R1 (`ISH-RT-M05.md:18`) ghi rõ "Thuộc M13"; chi tiết bảng nhật ký đúng là R1; không có hệ quả.
- (Chỉnh) P1-04 hạ từ Trung bình xuống Thấp (lý do ghi trong finding).
- (Chỉnh) P1-06 chọn lớp CONFLICT thay vì OBSERVATION vì việc tiếp theo là stakeholder chọn giữa hai quyết định đã đóng (RULES §7.6, §8.4).

## 5. Phạm vi và giới hạn không kiểm được

- KEYWORD: đọc nội dung khoảng 25 mục có từ khóa nghiệp vụ M05 (topic/tag/trending/follow/suggest); các mục còn lại chỉ đọc tiêu đề trong inventory. CROSS-CUTTING đọc tiêu đề và chọn mục áp dụng (DEC-127, DEC-131, DEC-133) như RULES §7 mục 4 cho phép.
- "Stakeholder đã được báo" chỉ kiểm được qua register (ISS/QA/DEC), không kiểm được trao đổi ngoài register.
- Không kiểm SR của module khác (chưa có SR nào khác trong `specs/`), nên các hàng R5 chỉ kiểm được nguồn, không kiểm ID sở hữu.
- Không mở `tests-M05.md` (ngoài phạm vi P1). `selfcheck-M05.md` chỉ đọc các dòng mục của P1.
- Không đánh giá mức ưu tiên/mốc ở 5.1 (CL-C05 thuộc P2).

## 6. Chuyển lượt khác

- 2.1 "Bài viết công khai | Bài viết đã xuất bản và không bị ẩn bởi kiểm duyệt" (`ISH-SR-M05.md:37`) có đúng nghĩa "publish_state PUBLISHED and mod_state NORMAL" của DEC-146 (`decisions.md:794`) không, nhất là bài đang chờ duyệt lại — P2 (CL-A05, CL-C03).
- ISH-M05-001.4 "không cho phép thêm Topic mới" ghi `Nói thẳng` từ "Topic list (11, final)" — P2 (CL-A05/A06).
- ISH-M05-012.9 "Khi người dùng yêu cầu đổi tên một Tag … từ chối" so với DEC-051 "do NOT edit … under normal conditions" — P2 (CL-A05).
- "Lý do" của 5.12 và 5.13 (`ISH-SR-M05.md:359`, `ISH-SR-M05.md:380`) lặp câu mục đích của DRAFT §3.1, không nói về đổi tên/gộp — P2 (CL-C04).
- Dòng M05 ở `module-registry.md:12` không có giá trị ở cột MoSCoW (cột bị lệch); 5.1 ghi Must cho mọi tính năng — P2 (CL-C05).
- Hàng R2 DEC-100 (`ISH-RT-M05.md:26`) chứa câu hỏi mở có hệ quả quan sát được (yêu cầu bị từ chối vì văn bản ngắn có bị đếm vào giới hạn 10/phút không) nhưng không có OP — P3 (CL-F04, CL-B13).
- Không có yêu cầu nào nói bài viết hiển thị các Topic và Tag đã gắn, trong khi ISH-M05-012.1/012.5 giả định có — P3 (CL-B13; liên quan P1-02).
- Topic/Tag có điểm Trending 0 có xuất hiện trong bảng xếp hạng không — P3 (CL-B13; liên quan P1-03).

## 7. Chỉ lượt P1 — ma trận

Ma trận ở `WORK/coverage-M05-r1.md` (phần A: mong đợi lập trước khi đọc SR; phần B: thực tế và kết quả; phần C: mâu thuẫn và lệch nguồn). Tóm tắt các hàng có finding:

| Nguồn | Mong đợi | Thực tế | Kết quả | Finding |
|---|---|---|---|---|
| DEC-145 | SR: Topic nguồn không chọn, gợi ý, xếp Trending, theo dõi được; người theo dõi chuyển sang đích | ISH-M05-011.2…011.4; chọn (002.2) và gợi ý (004.5) có; Trending và theo dõi không có | Thiếu một phần | P1-01 |
| QA-011 | SR/R5: Guest xem danh sách Topic, Tag, Khối lớp; xem phân loại trên bài | Topic → 001.3; Khối lớp → R5; Tag và phân loại trên bài không có chỗ đi | Thiếu một phần | P1-02 |
| QA-235 | SR hoặc OP (xếp hạng Topic/Tag thuộc M05) + R5 M14 (Trending Post) | Toàn bộ → R5 M14 "hiển thị" | Sai chỗ | P1-03 |
| KEYWORD (30 mục) | Mỗi mục một dòng disposition | Một câu gộp | Thiếu phân loại | P1-04 |
| DRAFT §7.2 | SR theo DEC-052 + dấu vết DRAFT | Chỉ register | Lệch nguồn | P1-05 |
| QA-043 / DEC-141 ↔ DEC-065 | CONFLICT hỏi stakeholder | Ghi chú ở R5, chưa hỏi | Lệch nguồn | P1-06 |
| glossary.md:14, :29; DEC-125 | Register nhất quán | Văn bản cũ chưa đánh dấu | Lệch nguồn | P1-07 |
