# Tệp lượt — ISH-AUD-M05-r1 · lượt P3 (Ca kiểm độc lập, mơ hồ và hành vi còn thiếu)
<!-- [Vietnamese Doc] -->

| Trường | Giá trị |
|---|---|
| Module | M05 — Topic & Tag |
| Vòng | 1 |
| Lượt | P3 |
| SR được audit | ISH-SR-M05, phiên bản 0.1 (2026-10-04), trạng thái Bản nháp |
| Routing | ISH-RT-M05, phiên bản 0.1 (2026-10-04) |
| Tóm tắt Author đã nhận và không dùng | Không có (người gọi chỉ đưa mã module, vòng, lượt, gốc repo) |
| Tệp đi kèm | `audit-tests-M05-r1.md` (98 ca, bảng quét khung hành vi), `audit-inventory-P3-M05-r1.md/.json`, `check-P3-M05-r1.json` |

Thứ tự đã làm: P3.1 inventory + đọc nguồn → P3.2/P3.2b dựng ca và quét khung **trước khi** mở nội dung SR/routing → P3.3 mở SR/routing → P3.4 chạy `check_sr.py --tests`, mở `selfcheck-M05.md` (bảng quét, các mục của lượt) và `tests-M05.md` → P3.5/P3.6 phân loại, chấm. Không mở `disposition-M05.md`, `inventory-M05.*` của Author và không mở tệp của lượt P1, P2.

## 1. Phát hiện nháp

Tóm tắt: 7 finding — GAP 4 (Cao 1, Trung bình 3), DEFECT 3 (Trung bình 3).

### P3-01 — "Bài viết được đăng trong 7 ngày" (điểm thưởng bài mới và tiêu chí phá hòa) đọc được hai cách

| Lớp | GAP | Mức đề xuất | Cao | Checklist | CL-A11 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.1, 008.2, 008.11, 008.12 (`ISH-SR-M05.md:317`, `:318`, `:327`, `:328`); 2.1 không có thuật ngữ cho "đăng".
- **Bằng chứng trong SR:** "cộng thêm số bài viết được tính của Topic đó được đăng trong 7 ngày gần nhất" (`ISH-SR-M05.md:317`); "Gửi bài viết | Thao tác của tác giả chuyển bài viết từ bản nháp sang chờ xuất bản." (`ISH-SR-M05.md:36`) — 2.1 phân biệt "gửi" với "xuất bản" nhưng câu yêu cầu dùng "đăng", không định nghĩa.
- **Bằng chứng trong nguồn:**
  - "the "+1" per post is a new-post bonus, given only to posts created within the window" (`registers/decisions.md:778`, DEC-142)
  - "Số "+1" là điểm thưởng bài mới, chỉ cộng cho bài được đăng trong 7 ngày" (`registers/qa-log.md:1005`, QA-270)
  - "Ties are broken by the number of counted posts created within the rolling 7-day window" (`registers/decisions.md:822`, DEC-153)
  - "- PENDING: submitted, under AI scan or mod review" (`registers/decisions.md:195`, DEC-031); "0.5≤score<0.9 → hold for mod review (Post stays PENDING" (`registers/decisions.md:565`, DEC-098)
- **Vấn đề:** Nguồn dùng "created" (DEC-142, DEC-153) và "được đăng" (QA-270) cho cùng một mốc; vòng đời bài viết có ba mốc khác nhau (tạo bản nháp, gửi, công khai sau khi quét AI hoặc Mod duyệt — có thể cách nhau nhiều ngày). Ca A-073 (`audit-tests-M05-r1.md`): bài gửi lúc T−8n, chờ Mod duyệt, công khai lúc T−6n, không tương tác → cách 1 (mốc gửi/tạo): đóng góp 0; cách 2 (mốc công khai): đóng góp 1; đồng thời đổi kết quả phá hòa ở 008.11/008.12. SR chép "được đăng" nên giữ nguyên mơ hồ. Không có ISS/QA/DEC hay `OP` nào về mốc này (đã tìm, xem mục 4). Ca của Author T-082 ("đăng 2 ngày trước") không phân biệt ba mốc nên không lộ mơ hồ.
- **Hệ quả nếu không sửa:** Hai cách cài đặt cho điểm Trending và thứ hạng khác nhau quan sát được; ca kiểm chấp nhận không có "Then" duy nhất.
- **Hướng xử lý (Author quyết cách viết):** hỏi stakeholder theo khuôn dưới, ghi register, rồi định nghĩa mốc "đăng" ở 2.1 hoặc viết thẳng vào 008.1/008.2/008.11/008.12; thêm ca kiểm cho bài chờ duyệt vắt qua ranh giới cửa sổ.
- **Khuôn hỏi stakeholder:**
  - Vấn đề: Điểm thưởng "+1 bài mới" và tiêu chí phá hòa của Trending Topic/Tag tính theo mốc nào của bài viết.
  - Nguồn: DEC-142 "given only to posts created within the window"; QA-270 "chỉ cộng cho bài được đăng trong 7 ngày".
  - Lựa chọn: A) Mốc bài viết trở thành công khai (lần đầu) — hệ quả: bài chờ Mod duyệt lâu vẫn được thưởng khi lên; khớp với việc chỉ bài công khai được tính (DEC-146). B) Mốc tác giả gửi bài — hệ quả: bài chờ duyệt quá 7 ngày không bao giờ được thưởng. C) Mốc tạo bản nháp — hệ quả: bài soạn nháp lâu không được thưởng dù vừa lên.
  - Đề xuất: A vì DEC-146 chỉ tính bài đang công khai, nên "bài mới" tự nhiên tính từ lúc người dùng khác thấy được bài.

### P3-02 — Bình luận bị ẩn bởi kiểm duyệt có được tính vào điểm Trending không

| Lớp | GAP | Mức đề xuất | Trung bình | Checklist | CL-A11 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.5, 008.7 (`ISH-SR-M05.md:321`, `:323`).
- **Bằng chứng trong SR:** "Hệ thống phải không đếm bình luận đã bị xóa khi tính điểm Trending." (`ISH-SR-M05.md:323`); mục 5.10 (dòng 301–329) không có từ "ẩn" hay "kiểm duyệt".
- **Bằng chứng trong nguồn:**
  - "only interactions that still exist count (retracted upvotes and deleted comments are not counted)" (`registers/decisions.md:794`, DEC-146)
  - "Comment needs a `mod_state` field similar to Post's (NORMAL | HIDDEN)" (`registers/decisions.md:490`, DEC-083)
  - "- If AI flags → comment auto-hidden (author only sees it) + pushed into report queue for mod review" (`registers/decisions.md:451`, DEC-077)
- **Vấn đề:** Bình luận bị AI hoặc Mod ẩn vẫn "còn tồn tại" nhưng không công khai. Ca A-074: P1 có 3 bình luận trong cửa sổ, 1 bị ẩn → cách 1 (còn tồn tại thì tính): P1 = 12; cách 2 (chỉ bình luận công khai): P1 = 11. DEC-146 lọc bài theo trạng thái công khai nhưng với bình luận chỉ nói "deleted". Không có ca của Author cho trường hợp này.
- **Lý do lệch mức:** mặc định CL-A11 ở công thức là Cao; hạ một mức vì chỉ ảnh hưởng bình luận đang bị ẩn (trường hợp biên) và câu DEC-146 đã cho nguyên tắc chung "còn tồn tại".
- **Hệ quả nếu không sửa:** Bình luận vi phạm bị ẩn có thể đẩy Topic/Tag lên Trending, hoặc ngược lại tùy cách cài đặt.
- **Hướng xử lý:** hỏi stakeholder, ghi register, thêm một yêu cầu cấp dưới cho bình luận bị ẩn.
- **Khuôn hỏi stakeholder:**
  - Vấn đề: Bình luận đang bị ẩn bởi kiểm duyệt (AI hoặc Mod) có được đếm vào điểm Trending Topic/Tag không.
  - Nguồn: DEC-146 "only interactions that still exist count (… deleted comments are not counted)"; DEC-083 bình luận có trạng thái kiểm duyệt NORMAL | HIDDEN.
  - Lựa chọn: A) Không đếm bình luận đang bị ẩn — hệ quả: nhất quán với việc chỉ tính bài công khai; điểm có thể tăng lại khi bình luận được khôi phục. B) Đếm mọi bình luận chưa xóa — hệ quả: nội dung vi phạm vẫn góp điểm.
  - Đề xuất: A vì DEC-146 chỉ tính nội dung đang công khai ở cấp bài viết.

### P3-03 — "Thứ tự chữ cái từ A đến Z" với tên tiếng Việt cho hai kết quả khác nhau

| Lớp | GAP | Mức đề xuất | Trung bình | Checklist | CL-A11 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.11, 008.12 (`ISH-SR-M05.md:327`, `:328`).
- **Bằng chứng trong SR:** "rồi đến tên theo thứ tự chữ cái từ A đến Z" (`ISH-SR-M05.md:327`, `:328`).
- **Bằng chứng trong nguồn:** "then by name in alphabetical order (A→Z)" (`registers/decisions.md:822`, DEC-153); danh mục có "Khoa học tự nhiên (Lý/Hóa/Sinh)" và "Khác" (`registers/decisions.md:281`, DEC-048).
- **Vấn đề:** Ca A-077: "Khác" và "Khoa học tự nhiên (Lý/Hóa/Sinh)" cùng điểm, cùng số bài → cách 1 (thứ tự bảng chữ cái tiếng Việt, "á" thuộc chữ a, a trước o): "Khác" xếp trước; cách 2 (thứ tự mã ký tự, "o" U+006F trước "á" U+00E1): "Khoa học tự nhiên" xếp trước. Với Tag (chữ thường), "đạohàm" và "elip" cũng đảo thứ tự (đ sau d trong tiếng Việt, sau mọi chữ Latin cơ bản theo mã). SR chép nguyên; ca của Author T-134 ("Ngữ văn" trước "Tin học") và T-135 chỉ dùng tên khác nhau ở chữ cái không dấu nên không lộ mơ hồ. Đã tìm "tiếng Việt", "bảng chữ cái", "collation", "đối chiếu" trong SR và routing: chỉ một kết quả không liên quan (006.15).
- **Hệ quả nếu không sửa:** Thứ hạng khi hòa không kiểm chứng được; hai cách cài đặt cho thứ tự khác nhau với chính tên Topic trong danh mục.
- **Hướng xử lý:** hỏi stakeholder (có thể kèm câu hỏi P3-01 hoặc gửi riêng), ghi register, nêu quy tắc so tên trong 008.11/008.12 hoặc 2.1.
- **Khuôn hỏi stakeholder:**
  - Vấn đề: Khi phá hòa bằng tên A→Z, so tên tiếng Việt theo quy tắc nào.
  - Nguồn: DEC-153 "then by name in alphabetical order (A→Z)".
  - Lựa chọn: A) Theo bảng chữ cái tiếng Việt (a ă â b c d đ e ê …, chữ cái gốc trước dấu thanh) — hệ quả: "Khác" trước "Khoa học tự nhiên"; đúng trực giác người dùng. B) Theo mã ký tự — hệ quả: chữ có dấu và "đ" xếp sau mọi chữ không dấu.
  - Đề xuất: A vì toàn bộ người dùng và tên Topic là tiếng Việt (DEC-127, DEC-128 chỉ có locale `vi`).

### P3-04 — Định nghĩa "Bài viết công khai" rộng hơn nguồn: bài FLAGGED và bài tác giả tự ẩn

| Lớp | DEFECT | Mức đề xuất | Trung bình | Checklist | CL-B08 |
|---|---|---|---|---|---|

- **Vị trí:** 2.1 "Bài viết công khai" (`ISH-SR-M05.md:37`), dùng ở ISH-M05-008.3 (`ISH-SR-M05.md:319`).
- **Bằng chứng trong SR:** "Bài viết công khai | Bài viết đã xuất bản và không bị ẩn bởi kiểm duyệt." (`ISH-SR-M05.md:37`); "Hệ thống phải chỉ tính vào điểm Trending các bài viết công khai không thuộc Group Private." (`ISH-SR-M05.md:319`).
- **Bằng chứng trong nguồn:**
  - "Only posts that are currently public (publish_state PUBLISHED and mod_state NORMAL, DEC-033)" (`registers/decisions.md:794`, DEC-146)
  - "- FLAGGED: AI/report flagged, awaiting mod" (`registers/decisions.md:203`, DEC-032)
  - "- HIDDEN: author self-hide (reversible)" (`registers/decisions.md:197`, DEC-031)
  - "- Visibility rule: publish_state=PUBLISHED AND mod_state=NORMAL" (`registers/decisions.md:211`, DEC-033)
- **Vấn đề:** Nguồn xác định: chỉ bài đang ở PUBLISHED **và** NORMAL. Định nghĩa trong SR cho hai kết quả khác nguồn hoặc đọc được hai cách: (1) ca A-091 — bài PUBLISHED đang FLAGGED (bị báo cáo, chờ Mod) "chưa bị ẩn bởi kiểm duyệt" theo 2.1 nên được tính (5 điểm) trong khi nguồn cho 0; (2) ca A-092 — bài tác giả tự ẩn (publish_state HIDDEN) "đã xuất bản" đọc được là "đã từng xuất bản" (5 điểm) hoặc "đang ở trạng thái xuất bản" (0). Ca của Author T-089 chỉ có "bị Mod ẩn", "đã bị xóa", "đang chờ duyệt", "bản nháp" nên không lộ khác biệt.
- **Hệ quả nếu không sửa:** Bài đang bị báo cáo hoặc bị tác giả ẩn vẫn góp điểm Trending, trái DEC-146.
- **Hướng xử lý:** sửa định nghĩa ở 2.1 (hoặc 008.3) cho khớp quy tắc hiển thị của DEC-033/DEC-146 bằng lời mô tả hành vi (không dùng tên trường); thêm ca kiểm cho bài FLAGGED và bài tự ẩn.

### P3-05 — Hệ quả của gộp Topic lên Topic nguồn: "không xếp hạng Trending" và "không theo dõi được" chưa thành yêu cầu

| Lớp | DEFECT | Mức đề xuất | Trung bình | Checklist | CL-B13, CL-B09 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-011.2 (`ISH-SR-M05.md:387`), ISH-M05-008 (`:307`), ISH-M05-007.1 (`:294`); 2.1 "Danh mục Topic" (`:28`).
- **Bằng chứng trong SR:** "hệ thống phải loại Topic nguồn khỏi danh mục Topic." (`ISH-SR-M05.md:387`); "Danh mục Topic | Tập Topic một tầng mà hệ thống cho phép chọn cho bài viết." (`ISH-SR-M05.md:28`); "Hệ thống phải xếp hạng các Topic và các Tag theo điểm Trending tính trên 7 ngày gần nhất." (`ISH-SR-M05.md:307`); "Khi người dùng đã đăng nhập yêu cầu theo dõi một Topic chưa theo dõi, hệ thống phải ghi nhận người dùng đó đang theo dõi Topic đó." (`ISH-SR-M05.md:294`). Vắng mặt: mục 5.9 và 5.10 (dòng 278–329) có 0 lần "danh mục", "Topic nguồn" hoặc "gộp".
- **Bằng chứng trong nguồn:** "it can no longer be selected, suggested, ranked in Trending or followed" (`registers/decisions.md:790`, DEC-145).
- **Vấn đề:** DEC-145 nêu bốn hệ quả. "Không chọn được" có ở 002.2 và "không gợi ý được" có ở 004.5 vì cả hai gắn với danh mục. Hai hệ quả còn lại không suy ra được từ câu SR: 2.1 định nghĩa danh mục chỉ là tập Topic "cho phép chọn cho bài viết"; 008 xếp hạng "các Topic" và 007.1 cho theo dõi "một Topic" mà không giới hạn trong danh mục; bảng 5.2 (`ISH-SR-M05.md:120`) cho thấy Topic nguồn vẫn tồn tại ở trạng thái "đã loại khỏi danh mục". Ca A-093 (theo dõi Topic nguồn sau gộp) và A-094 (Topic nguồn điểm 0 có trong xếp hạng khi không có ngưỡng — QA-235) có "Then" xác định theo nguồn nhưng SR `Mơ hồ`. Selfcheck ghi "Topic nguồn sau gộp bị loại (011.2)" (`selfcheck-M05.md:115`) và ca T-113 suy kết quả từ 011.2 — đó là suy diễn của Author, câu SR không nói. Hành vi từ chối theo dõi Topic nguồn cũng là nhánh vi phạm của giới hạn "can no longer be … followed" (CL-B09).
- **Hệ quả nếu không sửa:** Cài đặt có thể vẫn hiện Topic nguồn (điểm 0) trong bảng xếp hạng hoặc cho theo dõi Topic không còn bài nào.
- **Hướng xử lý:** thêm yêu cầu cấp dưới (Nói thẳng, DEC-145) cho hai hệ quả, hoặc định nghĩa lại phạm vi xếp hạng và theo dõi theo danh mục; thêm ca kiểm A-093/A-094 tương ứng.

### P3-06 — Tối thiểu 1 Topic áp dụng khi lưu bản nháp hay chỉ khi gửi; ca kiểm của Author ngầm chọn

| Lớp | GAP | Lớp phụ | DEFECT (ca kiểm ngầm chọn) | Mức đề xuất | Trung bình | Checklist | CL-A11, CL-F04, CL-B13 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-002.4, 002.5, 002.6 (`ISH-SR-M05.md:164`, `:165`, `:166`); `tests-M05.md:20` (T-011).
- **Bằng chứng trong SR:** "Hệ thống phải yêu cầu mỗi bài viết có tối thiểu 1 Topic." (`ISH-SR-M05.md:164`); "Khi tác giả gửi một bài viết không có Topic nào, hệ thống phải từ chối việc gửi bài viết đó." (`ISH-SR-M05.md:165`); "Khi người dùng lưu một thay đổi làm bài viết không còn Topic nào" (`ISH-SR-M05.md:166`); ca của Author: "Bài viết nháp của User A có 0 Topic" (`tests-M05.md:20`).
- **Bằng chứng trong nguồn:** "- Min 1, max 3 topics/post (mandatory)" (`registers/decisions.md:284`, DEC-049); "- DRAFT: composing, not submitted" (`registers/decisions.md:194`, DEC-031).
- **Vấn đề:** Nguồn không nói ràng buộc "mandatory" áp dụng từ lúc lưu bản nháp hay lúc gửi. Ca A-006: lưu bản nháp chưa có Topic → cách 1: từ chối; cách 2: chấp nhận. SR để 002.4 dạng phổ quát (mọi bài viết, kể cả bản nháp) nhưng 002.5 chỉ từ chối khi gửi và 002.6 chỉ khi "không còn" Topic, nên đọc được cả hai cách. Ca T-011 của Author lấy làm điều kiện đầu một bản nháp 0 Topic — tức đã ngầm chọn cách 2 — trong khi cột "Giả định cần thêm" ghi `—` và không có ISS/QA/DEC hay `OP` nào về bản nháp (đã tìm "nháp", "draft" trong SR, routing và register M05: chỉ có tham chiếu "DRAFT §" của tài liệu nguồn). Selfcheck 5.4 câu 2 (`selfcheck-M05.md:70`) chỉ xét ngữ cảnh sửa bài sau khi gửi.
- **Lý do mức:** CL-F04 mặc định Cao; đề xuất Trung bình vì lựa chọn ngầm chỉ nằm ở điều kiện đầu của ca kiểm, câu SR chưa chọn, và hệ quả giới hạn ở thao tác lưu nháp.
- **Hệ quả nếu không sửa:** Người dùng có thể bị chặn lưu nháp (hoặc không) tùy cài đặt; 002.4 mâu thuẫn tiềm ẩn với ca T-011.
- **Hướng xử lý:** hỏi stakeholder, ghi register, viết lại 002.4 theo câu trả lời (ví dụ thành điều kiện gắn với thao tác gửi) và sửa T-011 nếu cần.
- **Khuôn hỏi stakeholder:**
  - Vấn đề: Bài viết ở trạng thái bản nháp có được lưu khi chưa có Topic nào không.
  - Nguồn: DEC-049 "Min 1, max 3 topics/post (mandatory)"; DEC-031 "DRAFT: composing, not submitted".
  - Lựa chọn: A) Được lưu nháp không Topic; tối thiểu 1 kiểm khi gửi và khi sửa bài đã gửi — hệ quả: soạn nháp tự do, lỗi chỉ hiện lúc gửi. B) Không được lưu nháp nếu chưa có Topic — hệ quả: phải chọn Topic trước khi lưu lần đầu.
  - Đề xuất: A vì bản nháp là "composing, not submitted" và 002.5 đã chặn ở thao tác gửi.

### P3-07 — Ca kiểm của Author thiếu loại ca "thử chuyển từ trạng thái không cho phép"

| Lớp | DEFECT | Mức đề xuất | Trung bình | Checklist | CL-B12 |
|---|---|---|---|---|---|

- **Vị trí:** `tests-M05.md` (các ca cho ISH-M05-011, 012); bảng 5.2 (`ISH-SR-M05.md:118`, `:120`).
- **Bằng chứng:** RULES §11.3 "| Chuyển trạng thái | Chuyển hợp lệ; thử từ trạng thái không cho phép |" (`.agent-instructions/system_analysis/shared/SR-DOCUMENT-RULES.md:503`); SR có chuyển trạng thái "| Tag hoạt động | Mod hoặc Admin vô hiệu hóa Tag | Tag bị vô hiệu hóa | ISH-M05-012.1 |" (`ISH-SR-M05.md:118`) và "| Topic trong danh mục Topic | Topic được gộp làm Topic nguồn |" (`ISH-SR-M05.md:120`). Vắng mặt: các ca có "bị vô hiệu hóa" trong `tests-M05.md` chỉ là T-120 (gõ lại tên), T-121 (mở lại hợp lệ), T-124 (User mở lại — ca quyền); không có ca vô hiệu hóa một Tag đang bị vô hiệu hóa, mở lại một Tag đang hoạt động, đổi tên/gộp một Topic đã bị gộp, hoặc gộp vào một Topic đích đã bị loại khỏi danh mục.
- **Vấn đề:** CL-B12 yêu cầu đủ loại ca bắt buộc của §11.3. Thiếu loại ca này che mất câu hỏi có hệ quả quan sát được: gộp Topic S vào một Topic R đã bị loại khỏi danh mục sẽ để các bài viết mang Topic không còn trong danh mục; SR không có yêu cầu từ chối tương ứng (nguồn DEC-145 "can no longer be selected" có thể là cơ sở `Suy ra`). Selfcheck CL-B12 ghi `Đạt` (`selfcheck-M05.md:32`).
- **Hệ quả nếu không sửa:** Hành vi ở trạng thái không hợp lệ không kiểm chứng được; có thể thiếu yêu cầu từ chối.
- **Hướng xử lý:** thêm ca cho từng chuyển trạng thái không hợp lệ ở bảng 5.2; với ca nào không viết được "Then" thì ghi "Giả định cần thêm" và hỏi stakeholder hoặc đặt `OP`.

## 2. Kết quả checklist của lượt

| Mã | Kết quả | Finding / ghi chú |
|---|---|---|
| CL-A11 | Không đạt | P3-01 (mốc "đăng" trong công thức, Cao), P3-02 (bình luận bị ẩn), P3-03 (thứ tự A→Z tiếng Việt), P3-06 (tối thiểu 1 Topic khi lưu nháp). Các mơ hồ khác của nguồn đã có ID register (ISS-210…227) hoặc `OP` (OP-M05-02, 04, 05). Selfcheck ghi `Đạt` (`selfcheck-M05.md:20`) |
| CL-B08 | Không đạt | P3-04 (2.1 "Bài viết công khai" cho kết quả khác nguồn với bài FLAGGED/tự ẩn); P3-05 (hai hệ quả DEC-145 SR `Mơ hồ`). 98 ca: nguồn xác định mà SR `Mơ hồ` ở A-072/A-091/A-092, A-093, A-094; các ca còn lại SR `Có` hoặc đã có OP. Selfcheck ghi `Đạt` (`selfcheck-M05.md:28`) |
| CL-B09 | Không đạt | P3-05: thiếu nhánh từ chối theo dõi Topic nguồn sau gộp ("can no longer be … followed"). Các giới hạn khác đều có yêu cầu vi phạm: 002.5, 002.6, 002.8, 003.6, 003.9, 004.7, 006.5, 006.7, 006.8, 006.14, 007.5, 009.2, 010.3, 010.4, 011.5, 012.4, 012.7–012.11 |
| CL-B12 | Không đạt | P3-07. Phần còn lại đạt: `check_sr` TST không báo; 135 ca phủ 92/92 yêu cầu cấp dưới; có biên, vi phạm, quyền, thời gian (167 giờ 59 phút / 168 giờ 1 phút), công thức có ví dụ số với bài cũ có hoạt động mới (T-082 P2) và bài mới chưa hoạt động (T-083), số đếm 0/1/nhiều, hành động lặp; cột "Giả định cần thêm" toàn `—`. Ghi nhận thêm: ca T-134/T-135 và T-082 chọn dữ liệu không lộ mơ hồ (P3-01, P3-03) |
| CL-B13 | Không đạt | P3-05 (nguồn nêu, SR thiếu); P3-06 (điểm (c) chưa hỏi, chưa có OP). Bảng quét của Author đủ 12 × 7 ô; khác biệt so với bảng của Auditor ghi ở `audit-tests-M05-r1.md` mục 2. Không thấy câu yêu cầu cụt thiếu tác nhân/ngữ cảnh mà nguồn đã nêu |
| CL-F04 | Không đạt | P3-06: ca T-011 ngầm chọn cách đọc "được lưu nháp không Topic" mà chưa raise. Không thấy câu SR nào khác tự chọn phương án khi nguồn chưa chọn; các điểm còn lại đã có ISS/QA/DEC hoặc OP-M05-01, 02, 04…10. Selfcheck ghi `Đạt` (`selfcheck-M05.md:52`) |

## 3. Kết quả kiểm tra tự động

ERROR = 0, WARN = 0, INFO = 2. Lệnh đã chạy (từ thư mục `.agents/.claude/system_analysis/output`): `python3 <TOOLS>/check_sr.py --sr specs/ISH-SR-M05.md --routing specs/routing/ISH-RT-M05.md --tests specs/audit/work/tests-M05.md --json specs/audit/work/check-P3-M05-r1.json`. INFO: COV-99 (không truyền `--inventory`, đúng quy định lượt P3), TST-00 (135 ca cho 92 yêu cầu). Không có ERROR/WARN nên không lập finding từ script.

Inventory của lượt: `python3 <TOOLS>/inventory.py --registers <REG> --draft docs/_temp --module M05 --keywords "topic,tag,trending,gộp,merge,flat,chủ đề,thẻ,gợi ý,suggest,is_stale,follow,theo dõi,lớp,khối,grade,phân loại,classification" --out WORK/audit-inventory-P3-M05-r1.md --json WORK/audit-inventory-P3-M05-r1.json` → OWNED 76, REFERENCING 20, KEYWORD 99, CROSS 40, DRAFT 34. Mọi mục OWNED (DEC-047…052, DEC-140…153, ISS-079…084, ISS-207…227, QA-101…108, QA-267…287, dòng module-registry) đã đọc nguyên văn và có ca hoặc lý do không có hành vi kiểm chứng (ISS/QA là bản tóm tắt của DEC tương ứng; QA-102 "grouped per 2018 curriculum" là lý do, không có hành vi).

## 4. Hồ sơ xác minh

Mọi trích đoạn trên đã chạy `grep -n -F` (thư mục `.agents/.claude/system_analysis/output`):

- `grep -n -F 'the "+1" per post is a new-post bonus, given only to posts created within the window' registers/decisions.md` → 1 (dòng 778)
- `grep -n -F 'chỉ cộng cho bài được đăng trong 7 ngày' registers/qa-log.md` → 1 (dòng 1005)
- `grep -n -F 'Ties are broken by the number of counted posts created within the rolling 7-day window' registers/decisions.md` → 1 (dòng 822)
- `grep -n -F 'PENDING: submitted, under AI scan or mod review' registers/decisions.md` → 1 (dòng 195)
- `grep -n -F '0.5≤score<0.9 → hold for mod review (Post stays PENDING' registers/decisions.md` → 1 (dòng 565)
- `grep -n -F 'cộng thêm số bài viết được tính của Topic đó được đăng trong 7 ngày gần nhất' specs/ISH-SR-M05.md` → 1 (dòng 317)
- `grep -n -F 'Thao tác của tác giả chuyển bài viết từ bản nháp sang chờ xuất bản' specs/ISH-SR-M05.md` → 1 (dòng 36)
- Vắng mặt (P3-01): `grep -n "| Đăng\|thời điểm đăng\|xuất bản" specs/ISH-SR-M05.md` → chỉ dòng 36, 37 (định nghĩa "Gửi", "Bài viết công khai"), không có định nghĩa "đăng"; `grep -c "được đăng\|thời điểm đăng\|Đăng bài"` → 2 dòng (317, 318, chính là câu bị nêu); Phụ lục B (9 OP) không có OP về mốc này; register M05: `grep -n "created"` chỉ ở DEC-142, DEC-153
- `grep -n -F 'only interactions that still exist count (retracted upvotes and deleted comments are not counted)' registers/decisions.md` → 1 (dòng 794)
- ``grep -n -F 'Comment needs a `mod_state` field similar to Post' registers/decisions.md`` → 1 (dòng 490, DEC-083)
- `grep -n -F 'If AI flags → comment auto-hidden (author only sees it)' registers/decisions.md` → 1 (dòng 451, DEC-077)
- `grep -n -F 'Hệ thống phải không đếm bình luận đã bị xóa khi tính điểm Trending.' specs/ISH-SR-M05.md` → 1 (dòng 323)
- Vắng mặt (P3-02): `sed -n 301,329p specs/ISH-SR-M05.md | grep -c -i "ẩn\|kiểm duyệt"` → 0; `grep -n -i "bình luận.*ẩn\|ẩn.*bình luận"` trên SR, routing, `tests-M05.md` → 0
- `grep -n -F 'then by name in alphabetical order (A→Z)' registers/decisions.md` → 1 (dòng 822)
- `grep -n -F 'Khoa học tự nhiên (Lý/Hóa/Sinh)' registers/decisions.md` → 1 (dòng 281)
- `grep -n -F 'rồi đến tên theo thứ tự chữ cái từ A đến Z' specs/ISH-SR-M05.md` → 2 (dòng 327, 328)
- Vắng mặt (P3-03): `grep -n -i "tiếng Việt\|bảng chữ cái\|collation\|đối chiếu"` trên SR, routing → 1 (dòng 276, ISH-M05-006.15, không liên quan thứ tự); `grep -n -F '"Ngữ văn" xếp trước "Tin học" (N trước T)' tests-M05.md` → 1 (dòng 142)
- `grep -n -F 'Only posts that are currently public (publish_state PUBLISHED and mod_state NORMAL, DEC-033)' registers/decisions.md` → 1 (dòng 794)
- `grep -n "FLAGGED: AI/report flagged, awaiting mod\|HIDDEN: author self-hide (reversible)\|Visibility rule: publish_state=PUBLISHED AND mod_state=NORMAL" registers/decisions.md` → dòng 203, 197, 211
- `grep -n -F 'Bài viết đã xuất bản và không bị ẩn bởi kiểm duyệt.' specs/ISH-SR-M05.md` → 1 (dòng 37); `grep -n -F 'Hệ thống phải chỉ tính vào điểm Trending các bài viết công khai không thuộc Group Private.'` → 1 (dòng 319)
- Vắng mặt (P3-04): `grep -c -i "FLAGGED\|gắn cờ\|chờ kiểm duyệt\|tự ẩn" specs/ISH-SR-M05.md` → 0; cùng mẫu trên `tests-M05.md` → 0; T-089 ở dòng 103
- `grep -n -F 'it can no longer be selected, suggested, ranked in Trending or followed' registers/decisions.md` → 1 (dòng 790)
- `grep -n -F 'Tập Topic một tầng mà hệ thống cho phép chọn cho bài viết.' specs/ISH-SR-M05.md` → 1 (dòng 28); `'hệ thống phải loại Topic nguồn khỏi danh mục Topic.'` → 1 (dòng 387); `'Hệ thống phải xếp hạng các Topic và các Tag theo điểm Trending tính trên 7 ngày gần nhất.'` → 1 (dòng 307); `'Khi người dùng đã đăng nhập yêu cầu theo dõi một Topic chưa theo dõi'` → 1 (dòng 294)
- Vắng mặt (P3-05): `sed -n 278,329p specs/ISH-SR-M05.md | grep -c "danh mục\|Topic nguồn\|gộp"` → 0; `grep -n "Topic nguồn\|đã loại khỏi danh mục" specs/ISH-SR-M05.md` → dòng 29, 30, 120, 376, 386–389 (chỉ mục 2.1, 5.2, 5.13); `grep -n -i "theo dõi.*nguồn\|nguồn.*theo dõi" tests-M05.md` → không có ca theo dõi Topic nguồn sau gộp; T-113 ở dòng 127
- `grep -n -F -- '- Min 1, max 3 topics/post (mandatory)' registers/decisions.md` → 1 (dòng 284); `'- DRAFT: composing, not submitted'` → 1 (dòng 194)
- `grep -n -F` ba câu 002.4, 002.5, 002.6 trên SR → dòng 164, 165, 166; `'Bài viết nháp của User A có 0 Topic'` trên `tests-M05.md` → 1 (dòng 20)
- Vắng mặt (P3-06): `grep -n -i "bản nháp\|nháp"` trên SR, routing → chỉ dòng 8 (trạng thái tài liệu), 36 (định nghĩa Gửi), 432 (lịch sử), RT:16 (gợi ý cũ); `grep -n -i "nháp\|draft"` trên `issue-queue.md`, `qa-log.md` lọc "topic" → chỉ các dòng nhắc "DRAFT §" (tài liệu nguồn), không có ISS/QA về bài viết nháp
- `grep -n -F '| Chuyển trạng thái | Chuyển hợp lệ; thử từ trạng thái không cho phép |' SR-DOCUMENT-RULES.md` → 1 (dòng 503); `grep -n -F '| Tag hoạt động | Mod hoặc Admin vô hiệu hóa Tag | Tag bị vô hiệu hóa | ISH-M05-012.1 |' specs/ISH-SR-M05.md` → 1 (dòng 118); dòng 120 cho chuyển trạng thái Topic nguồn
- Vắng mặt (P3-07): `grep -n -i "đã bị vô hiệu hóa\|bị vô hiệu hóa" tests-M05.md` → T-120, T-121, T-124 (không có ca chuyển không hợp lệ); `grep -c -i "gộp.*đã gộp\|vào chính\|Topic đã gộp" tests-M05.md` → 0
- Selfcheck: `grep -n "^| CL-A11\|^| CL-B08\|^| CL-B09\|^| CL-B12\|^| CL-B13\|^| CL-F04" selfcheck-M05.md` → dòng 20, 28, 29, 32, 33, 52 (đều `Đạt`); dòng 70 (5.4 câu 2), 115 (5.10 câu 5)

Finding bị loại hoặc chỉnh ở bước xác minh:

- Ứng viên "gợi ý Topic khi sửa bài đã đăng" (A-055), "tên Topic trùng/rỗng" (A-084), "Tag vô hiệu hóa có tính vào giới hạn 5" (A-024 phần đếm): loại — đã có OP-M05-02, OP-M05-04, OP-M05-05 ở Phụ lục B.
- Ứng viên "Tag điểm 0 có trong xếp hạng" (A-081): loại — phần hiển thị thuộc M14 (R5 có QA-235), chỉ ghi chú.
- Ứng viên "trùng Tag trong một bài: từ chối hay gộp": loại — hai cách cho cùng kết quả quan sát trên bài (một Tag); SR có 006.10.
- Ứng viên "phản hồi gợi ý có cập nhật khi đổi Topic sau khi gửi" (A-060): loại — SR chọn mốc gửi khớp "final selection … → publish" của DEC-050, không phải quyết định ngầm.
- P3-02 hạ một mức (Cao → Trung bình), P3-06 hạ một mức so với CL-F04 (Cao → Trung bình), lý do ghi trong finding.
- P3-05 ban đầu định lớp GAP; chỉnh thành DEFECT vì nguồn (DEC-145) đã nêu rõ hai hệ quả, Author tự sửa được.

## 5. Phạm vi và giới hạn không kiểm được

- Lượt P3 không chấm các mục của P1, P2; không mở `disposition-M05.md`, `inventory-M05.*` của Author, và không mở tệp lượt P1, P2.
- Khi kiểm header SR ở C0 (lệnh `head -15`), Auditor đọc được đoạn mục 1 Tổng quan (dòng 15, chỉ liệt kê nhóm tính năng) trước khi dựng ca; không ảnh hưởng đáng kể đến tính độc lập của ca kiểm.
- Trạng thái kiểm duyệt của bình luận (DEC-077, DEC-083) và quy tắc hiển thị bài viết (DEC-031…033) lấy từ register của M03/M04/M08; các module đó chưa có SR nên không đối chiếu được với yêu cầu của module sở hữu.
- Không kiểm được ý định của stakeholder về quy tắc so tên tiếng Việt (P3-03) và mốc "đăng" (P3-01) — chỉ nêu lựa chọn.
- Không kiểm được hành vi cài đặt thực (cửa sổ đếm 10 yêu cầu/phút, chu kỳ 15–30 phút): thuộc R2.

## 6. Chuyển lượt khác

- QA-011 (CLAS) "Xem danh sách Topic / Tag / Khối lớp" cho Guest: phần Topic ở ISH-M05-001.3, phần Khối lớp ở R5 (RT dòng 65), phần **Tag** không có yêu cầu và không có hàng routing → P1 (CL-A10, CL-A03).
- "Lý do" của 5.12 và 5.13 chép nguyên "Lý do" chung của 5.3, không nêu lý do của đổi tên/gộp (DEC-049, ISS-084) → P2 (CL-C04).
- ISH-M05-004.5, 004.6, 004.7 (xử lý kết quả AI có Topic ngoài danh mục, hơn 3 Topic) nằm trong tính năng "Gợi ý Topic khi AI không khả dụng" dù 004.5, 004.7 áp dụng cả khi AI trả kết quả thành công; cấp trên ISH-M05-004 không bao quát → P2 (CL-C04).
- R6 ghi "DRAFT §3.3 → DEC-125" cho Personalized Feed; nội dung Personalized Feed nằm ở DRAFT §7.1 (§3.3 chỉ nhắc "Personalized Feed (xem 7.1)") → P1 (CL-E03).
- R5 dòng 62 xếp QA-236 (không loại bài của người dùng BANNED) vào M14, trong khi DEC-146 (OWNED M05) nhắc lại quy tắc này cho Trending Topic/Tag; Phụ lục A của 008.3 không ghi QA-236 → P1 (CL-A10).
