# Tệp lượt — ISH-AUD-M05-r1 · lượt P2 (Chất lượng yêu cầu)
<!-- [Vietnamese Doc] -->

| Trường | Giá trị |
|---|---|
| Module | M05 |
| Vòng | 1 |
| Lượt | P2 |
| SR được audit | ISH-SR-M05, phiên bản 0.1 (2026-10-04), trạng thái Bản nháp |
| Routing | ISH-RT-M05, phiên bản 0.1 (2026-10-04) |
| Tóm tắt Author đã nhận và không dùng | Không có (người gọi chỉ đưa mã module, vòng, lượt, gốc repo) |
| Kết luận của lượt | Chưa đạt: còn 9 DEFECT mở (7 Trung bình, 2 Thấp); `check_sr.py` ERROR = 0 |

Đường dẫn viết tắt: `SR` = `.agents/.claude/system_analysis/output/specs/ISH-SR-M05.md`; `RT` = `.agents/.claude/system_analysis/output/specs/routing/ISH-RT-M05.md`; `DEC` = `.agents/.claude/system_analysis/output/registers/decisions.md`; `QA` = `.agents/.claude/system_analysis/output/registers/qa-log.md`.

Ghi chú: `snapshot-ISH-SR-M05-v0.1.md` và `snapshot-ISH-RT-M05-v0.1.md` trùng hoàn toàn với SR và routing hiện tại (`diff` không ra khác biệt), nên lượt này audit đúng bản 0.1 đã bàn giao.

## 1. Phát hiện nháp

### P2-01 — Định nghĩa "Bài viết công khai" lệch điều kiện của DEC-146 nên tập bài viết tính Trending đọc được hai cách

| Lớp | DEFECT | Lớp phụ | — | Mức đề xuất | Trung bình | Checklist | CL-A05, CL-C03 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** mục 2.1, thuật ngữ "Bài viết công khai" (`SR:37`), được dùng trong ISH-M05-008.3 (`SR:319`).
- **Bằng chứng trong SR:** "| Bài viết công khai | Bài viết đã xuất bản và không bị ẩn bởi kiểm duyệt. |" (`SR:37`); "Hệ thống phải chỉ tính vào điểm Trending các bài viết công khai không thuộc Group Private." (`SR:319`).
- **Bằng chứng trong nguồn:** "Only posts that are currently public (publish_state PUBLISHED and mod_state NORMAL, DEC-033) and not in a Private group count." (`DEC:794`, DEC-146); "- Visibility rule: publish_state=PUBLISHED AND mod_state=NORMAL" (`DEC:211`, DEC-033); "- FLAGGED: AI/report flagged, awaiting mod" (`DEC:203`, DEC-032); "- HIDDEN: author self-hide (reversible)" (`DEC:197`, DEC-031).
- **Vấn đề:** Nguồn chỉ tính bài *đang* ở PUBLISHED **và** NORMAL. Định nghĩa trong SR dùng hai cụm rộng hơn: (1) "đã xuất bản" cũng đúng với bài từng xuất bản rồi bị tác giả tự ẩn (publish_state HIDDEN); (2) "không bị ẩn bởi kiểm duyệt" cũng đúng với bài đã xuất bản đang bị gắn cờ chờ Mod (mod_state FLAGGED), vì bài đó chưa bị Mod ẩn. Ca kiểm: một bài PUBLISHED + FLAGGED có 5 upvote trong 7 ngày → theo nguồn đóng góp 0 điểm; theo SR có thể đóng góp 10 điểm. Ở đây SR làm mơ hồ một điều kiện mà nguồn nêu chính xác (không phải mơ hồ có sẵn từ nguồn).
- **Lý do chỉnh mức:** Mặc định của CL-A05 là Cao. Hạ một mức vì ý của yêu cầu đúng, độ lệch chỉ xảy ra ở hai trạng thái biên, và cách sửa đã có sẵn trong nguồn.
- **Hệ quả nếu không sửa:** điểm Trending của Topic hoặc Tag có bài bị gắn cờ hay bị tác giả tự ẩn không kiểm chứng được duy nhất; người cài đặt có thể đếm cả những bài người dùng không nhìn thấy.
- **Hướng xử lý (Author quyết cách viết):** viết lại định nghĩa theo đúng điều kiện của DEC-146/DEC-033 bằng ngôn ngữ hành vi: bài đang xuất bản, đang ở trạng thái kiểm duyệt bình thường, không bị gắn cờ, không bị ẩn. Không dùng tên trường.

### P2-02 — "các Topic cố định" ở ISH-M05-001 không đo được và trái với đổi tên, gộp Topic

| Lớp | DEFECT | Lớp phụ | — | Mức đề xuất | Trung bình | Checklist | CL-B03, CL-C01 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-001 (`SR:130`).
- **Bằng chứng trong SR:** "Hệ thống phải cung cấp một danh mục Topic một tầng gồm các Topic cố định." (`SR:130`); "hệ thống phải loại Topic nguồn khỏi danh mục Topic." (`SR:387`, ISH-M05-011.2); "Khi Mod hoặc Admin đổi tên một Topic, hệ thống phải thay tên của Topic đó bằng tên mới." (`SR:355`, ISH-M05-010).
- **Bằng chứng trong nguồn:** "After a merge, the source Topic is removed from the Topic catalog: it can no longer be selected, suggested, ranked in Trending or followed; …" (`DEC:790`, DEC-145).
- **Vấn đề:** "cố định" không cho biết điều gì được giữ cố định: không thêm Topic mới (ISH-M05-001.4), tên không đổi, hay tập Topic không đổi. Hai cách đọc sau cùng trái với ISH-M05-010 (đổi tên) và ISH-M05-011.2 (gộp làm danh mục mất Topic nguồn). Một người kiểm theo câu cấp trên sẽ kỳ vọng sau khi gộp danh mục vẫn đủ 11 Topic, trong khi ISH-M05-011.2 cho 10 Topic.
- **Lý do chọn mức:** Mức Trung bình là mặc định của CL-B03. Mặt CL-C01 (mặc định Cao) không được lấy làm mức vì các yêu cầu cấp dưới đều đúng với nguồn; mâu thuẫn chỉ nằm ở lời văn của câu cấp trên.
- **Hệ quả nếu không sửa:** câu cấp trên không kiểm chứng được và có một cách đọc mâu thuẫn với ISH-M05-011.2.
- **Hướng xử lý:** viết câu cấp trên theo đúng ý nguồn đã chốt (danh mục do hệ thống quản lý, người dùng không thêm được Topic), hoặc bỏ "cố định" và để ISH-M05-001.1 và 001.4 mang nội dung đó.

### P2-03 — ISH-M05-003.11 trái với ISH-M05-003.10 khi gợi ý đã cũ

| Lớp | DEFECT | Lớp phụ | — | Mức đề xuất | Trung bình | Checklist | CL-C01 (kèm CL-A05) |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-003.11 (`SR:197`) so với ISH-M05-003.10 (`SR:196`).
- **Bằng chứng trong SR:** "hệ thống phải đánh dấu gợi ý đó là gợi ý cũ." (`SR:196`); "Khi tác giả thay đổi tệp đính kèm của bài viết sau khi nhận gợi ý Topic, hệ thống phải giữ gợi ý đó là gợi ý còn mới." (`SR:197`).
- **Bằng chứng trong nguồn:** "A suggestion becomes stale on any change to the title or the text content; attachment changes do not count." (`DEC:802`, DEC-148).
- **Vấn đề:** Nguồn nói thay đổi tệp đính kèm *không ảnh hưởng* trạng thái gợi ý. SR viết thành "giữ … là gợi ý còn mới", mà câu này không có điều kiện "gợi ý đang còn mới". Ca kiểm: nhận gợi ý → sửa tiêu đề (003.10: gợi ý cũ) → thêm một tệp đính kèm. Theo 003.11 gợi ý là "còn mới"; theo 003.10 và theo nguồn, gợi ý vẫn cũ. Kết quả quan sát được khác nhau: cảnh báo ở 003.12 có hiện hay không, và phản hồi ở 005.1 hay 005.2 có được ghi hay không.
- **Lý do chỉnh mức:** Mặc định của CL-C01 là Cao. Hạ một mức vì chỉ xảy ra theo một trình tự thao tác cụ thể và ý của nguồn rõ.
- **Hệ quả nếu không sửa:** hai yêu cầu cho hai trạng thái khác nhau với cùng một trình tự thao tác; ghi nhận phản hồi cho AI có thể ghi nhầm cả gợi ý đã cũ.
- **Hướng xử lý:** viết 003.11 theo ý "thay đổi tệp đính kèm không làm đổi trạng thái gợi ý", hoặc thêm điều kiện trạng thái để không chồng với 003.10.

### P2-04 — Câu cấp trên ISH-M05-005 nói ghi phản hồi ở mọi lần gửi bài, trái với 005.2, 005.3 và sai mẫu câu

| Lớp | DEFECT | Lớp phụ | — | Mức đề xuất | Trung bình | Checklist | CL-C04, CL-B01 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-005 (`SR:232`).
- **Bằng chứng trong SR:** "Hệ thống phải ghi nhận phản hồi gợi ý Topic khi tác giả gửi bài viết." (`SR:232`); "Trong khi gợi ý Topic của bài viết là gợi ý cũ, khi tác giả gửi bài viết đó, hệ thống phải không ghi nhận phản hồi gợi ý Topic." (`SR:243`); "Khi tác giả gửi một bài viết chưa từng nhận gợi ý Topic, hệ thống phải không ghi nhận phản hồi gợi ý Topic." (`SR:244`).
- **Bằng chứng trong nguồn:** "- Feedback (AI suggest vs final selection) only recorded when not stale" (`DEC:293`, DEC-050).
- **Vấn đề:** (1) Câu cấp trên không có điều kiện: theo câu này, mọi lần gửi bài đều ghi phản hồi, trong khi hai yêu cầu cấp dưới nói không ghi trong hai trường hợp. Cấp trên không nêu đúng mục tiêu mà cấp dưới bao quát (CL-C04). (2) Câu có sự kiện kích hoạt ("khi tác giả gửi bài viết") nhưng viết theo mẫu Phổ quát, vế "khi" đặt cuối câu, trong khi RULES §4.1 và §4.6 yêu cầu mẫu `Khi …, hệ thống phải …` (CL-B01). `check_sr.py` không bắt lỗi này (EARS-01..03 không báo).
- **Hệ quả nếu không sửa:** một ca kiểm viết từ câu cấp trên (gửi bài chưa từng nhận gợi ý → có bản ghi phản hồi) cho kết quả ngược với ISH-M05-005.3.
- **Hướng xử lý:** viết lại câu cấp trên theo mẫu sự kiện, kèm điều kiện "chỉ khi có gợi ý còn mới" đúng như nguồn.

### P2-05 — ISH-M05-005.1 "từ gợi ý Topic gần nhất" được ghi là Nói thẳng nhưng nguồn không nêu

| Lớp | DEFECT | Lớp phụ | GAP | Mức đề xuất | Trung bình | Checklist | CL-A05, CL-A06 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-005.1 (`SR:242`); Phụ lục A (`SR:477`).
- **Bằng chứng trong SR:** "hệ thống phải ghi nhận phản hồi gợi ý Topic từ gợi ý Topic gần nhất cùng các Topic tác giả chọn cuối cùng." (`SR:242`); "| ISH-M05-005.1 | DEC-050, QA-017 | Nói thẳng | "Feedback (AI suggest vs final selection)"; gợi ý gần nhất vì gợi ý trước đó đã bị thay thế (DEC-148) |" (`SR:477`).
- **Bằng chứng trong nguồn:** "- Feedback (AI suggest vs final selection) only recorded when not stale" (`DEC:293`); "Suggested topics replace the current selection, including topics the user ticked manually before requesting the suggestion." (`DEC:802`, DEC-148). DEC-148 nói Topic được gợi ý thay *lựa chọn Topic*, không nói về việc phản hồi lấy từ lần gợi ý nào.
- **Vấn đề:** Khi tác giả yêu cầu gợi ý nhiều lần (ví dụ hai lần liền nhau, không sửa văn bản, nên cả hai đều còn mới), nguồn không nói phản hồi ghi theo lần gần nhất, theo mọi lần, hay theo lần đầu. "Gần nhất" là cách đọc tự nhiên nhưng không phải hệ quả bắt buộc của nguồn, mà lại được ghi `Nói thẳng`. Đã tìm `latest|most recent|gần nhất|last suggest` cùng `suggest|gợi ý|feedback|phản hồi` trong decisions, qa-log, issue-queue: 0 kết quả.
- **Lý do chỉnh mức:** Mặc định của CL-A05 là Cao. Hạ một mức vì cách đọc Author chọn là cách tự nhiên nhất, và hệ quả chỉ nằm ở dữ liệu đánh giá AI (M13), không ở màn hình người dùng.
- **Hệ quả nếu không sửa:** truy vết khẳng định nguồn đã nói một điều nguồn chưa nói; bộ dữ liệu phản hồi dùng để đo độ chính xác có thể khác với điều stakeholder kỳ vọng.
- **Hướng xử lý:** Author chọn một trong hai: (a) đổi cơ sở sang `Suy ra` và ghi phép suy luận đủ chặt, nếu chứng minh được đây là hệ quả bắt buộc; (b) nếu không chứng minh được thì đặt `OP` hoặc hỏi stakeholder.
- **Khuôn hỏi stakeholder (nếu đi theo b):**
  - Vấn đề: tác giả nhận nhiều gợi ý Topic còn mới cho cùng một bài thì phản hồi ghi theo lần gợi ý nào.
  - Nguồn: DEC-050 (`DEC:293`) "Feedback (AI suggest vs final selection) only recorded when not stale".
  - Lựa chọn: A) chỉ lần gần nhất — dữ liệu gọn, mất các lần gợi ý trung gian; B) mọi lần còn mới — đủ dữ liệu đo, một bài có nhiều bản ghi.
  - Đề xuất: A, vì mỗi lần gợi ý mới thay lựa chọn trước (DEC-148).

### P2-06 — Cơ sở `Nói thẳng` cho phần từ chối mà nguồn chỉ nói về Mod/Admin (ISH-M05-006.12, 012.9, 012.10, 012.11)

| Lớp | DEFECT | Lớp phụ | — | Mức đề xuất | Trung bình | Checklist | CL-A05 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-006.12 (`SR:273`, Phụ lục A `SR:492`); ISH-M05-012.9 (`SR:416`, `SR:539`); ISH-M05-012.10 (`SR:417`, `SR:540`); ISH-M05-012.11 (`SR:418`, `SR:541`).
- **Bằng chứng trong SR:** "Khi một người dùng khác tác giả của bài viết yêu cầu thay đổi Tag của bài viết đó, hệ thống phải từ chối yêu cầu đó." (`SR:273`), Phụ lục A "| ISH-M05-006.12 | DEC-144, QA-273 | Nói thẳng | Chỉ tác giả đổi Tag; Mod/Admin không đổi Tag của bài |" (`SR:492`); "Khi người dùng yêu cầu đổi tên một Tag, hệ thống phải từ chối yêu cầu đó." (`SR:416`), Phụ lục A "… Nói thẳng | "mod/admin do NOT edit"; Tag không có thao tác sửa cho người dùng nào |" (`SR:539`); "Khi người dùng yêu cầu gộp hai Tag, hệ thống phải từ chối yêu cầu đó." (`SR:417`), "| ISH-M05-012.10 | DEC-051 | Nói thẳng |" (`SR:540`); "Khi người dùng yêu cầu xóa một Tag, hệ thống phải từ chối yêu cầu đó." (`SR:418`), "| ISH-M05-012.11 | DEC-051, QA-107 | Nói thẳng |" (`SR:541`).
- **Bằng chứng trong nguồn:** "- Fully free — mod/admin do NOT edit/merge/delete under normal conditions" (`DEC:302`, DEC-051); "A Mod or Admin does not change a post's Tags" (`DEC:786`, DEC-144).
- **Vấn đề:** Nguồn chỉ nói rõ về Mod/Admin. Các yêu cầu áp dụng cho "người dùng" (gồm cả Guest và User) hoặc "người dùng khác tác giả". Phần áp dụng cho Guest/User là suy ra theo dạng "chỉ X mới được làm Y" (RULES §4.5), nên cơ sở đúng là `Suy ra` kèm phép suy luận. Chính SR đã làm như vậy với yêu cầu cùng dạng ISH-M05-009.2: "| ISH-M05-009.2 | DEC-144 | Suy ra |" (`SR:518`).
- **Lý do chỉnh mức:** Mặc định của CL-A05 là Cao. Hạ một mức vì hành vi (từ chối) là phương án an toàn và suy ra được; sai lệch nằm ở cột Cơ sở.
- **Hệ quả nếu không sửa:** truy vết ghi sai mức chắc chắn của nguồn; Auditor và stakeholder không thấy được phần nào đã qua suy luận.
- **Hướng xử lý:** đổi cơ sở của bốn dòng sang `Suy ra` kèm phép suy luận, hoặc tách phần Mod/Admin (`Nói thẳng`) khỏi phần Guest/User (`Suy ra`).

### P2-07 — Yêu cầu cấp dưới vượt ra ngoài câu cấp trên (ISH-M05-010.4; ISH-M05-012.9 đến 012.11)

| Lớp | DEFECT | Lớp phụ | — | Mức đề xuất | Trung bình | Checklist | CL-C04 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-010.4 (`SR:368`) dưới ISH-M05-010 (`SR:355`); ISH-M05-012.9, 012.10, 012.11 (`SR:416`–`SR:418`) dưới ISH-M05-012 (`SR:398`).
- **Bằng chứng trong SR:** "Khi Mod hoặc Admin đổi tên một Topic, hệ thống phải thay tên của Topic đó bằng tên mới." (`SR:355`) và "Khi người dùng yêu cầu xóa một Topic, hệ thống phải từ chối yêu cầu đó." (`SR:368`); "Hệ thống phải cho phép Mod và Admin thay đổi trạng thái hoạt động của một Tag." (`SR:398`) và "Khi người dùng yêu cầu đổi tên một Tag, hệ thống phải từ chối yêu cầu đó." (`SR:416`), "Khi người dùng yêu cầu gộp hai Tag, …" (`SR:417`), "Khi người dùng yêu cầu xóa một Tag, …" (`SR:418`).
- **Vấn đề:** RULES §10, CL-C04: "cấp dưới thêm hành vi cấp trên không nói là DEFECT". Câu cấp trên của 5.12 chỉ nói về đổi tên Topic, nhưng 010.4 là việc cấm xóa Topic. Câu cấp trên của 5.14 chỉ nói về đổi trạng thái hoạt động, nhưng 012.9 đến 012.11 là việc cấm đổi tên, gộp, xóa Tag. Bản thân các hành vi này có nguồn (DEC-049 "No delete", DEC-051).
- **Hệ quả nếu không sửa:** cấu trúc tính năng không phản ánh đúng phạm vi. Người đọc câu cấp trên (và mục 5.1) không biết rằng tính năng còn chứa các lệnh cấm.
- **Hướng xử lý:** mở rộng câu cấp trên cho bao quát các lệnh cấm, hoặc chuyển các lệnh cấm sang tính năng có câu cấp trên phù hợp. Khung 12 tính năng đã được duyệt (DEC-151), nên cách mở rộng câu cấp trên không đổi khung.

### P2-08 — Mục 5.2 thiếu trạng thái theo dõi Topic

| Lớp | DEFECT | Lớp phụ | — | Mức đề xuất | Thấp | Checklist | CL-C05 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** mục 5.2 (`SR:116`–`SR:122`); ISH-M05-007.1, 007.2, 007.3 (`SR:294`–`SR:296`).
- **Bằng chứng trong SR:** "hệ thống phải ghi nhận người dùng đó đang theo dõi Topic đó." (`SR:294`); "hệ thống phải ghi nhận người dùng đó không còn theo dõi Topic đó." (`SR:295`); "trạng thái đang theo dõi hay chưa theo dõi của người dùng đó với mỗi Topic" (`SR:296`). Bảng 5.2 có hàng cho Tag (`SR:118`), Topic gộp và gợi ý cũ/mới, nhưng `sed -n 114,123p SR | grep -c "theo dõi"` → 0.
- **Vấn đề:** Thân tài liệu tự gọi "đang theo dõi / chưa theo dõi" là trạng thái và có hai chuyển trạng thái (007.1, 007.2), cộng một chuyển do gộp Topic (011.3). Bảng 5.2 không có các chuyển này, nên 5.2 không khớp thân tài liệu.
- **Lý do chỉnh mức:** Mặc định của CL-C05 là Trung bình. Hạ một mức vì hành vi đã được quy định đủ ở các yêu cầu, chỉ thiếu ở bảng tổng hợp; sửa cơ học.
- **Hướng xử lý:** thêm các hàng chuyển trạng thái theo dõi (theo dõi, bỏ theo dõi, chuyển do gộp) trỏ tới ID tương ứng.

### P2-09 — Thuật ngữ chưa khớp 2.1: "bài viết được tính" chưa định nghĩa; "Upvote" định nghĩa chỉ cho bài viết

| Lớp | DEFECT | Lớp phụ | — | Mức đề xuất | Thấp | Checklist | CL-C03 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.1, 008.2, 008.11, 008.12 (`SR:317`, `SR:318`, `SR:327`, `SR:328`); 2.1 "Upvote" (`SR:53`) so với ISH-M05-008.4 (`SR:320`).
- **Bằng chứng trong SR:** "trên mọi bài viết được tính của Topic đó" (`SR:317`); "số bài viết được tính đăng trong 7 ngày gần nhất" (`SR:327`); "| Upvote | Lượt đánh giá tích cực của người dùng cho một bài viết. |" (`SR:53`); "không đếm upvote vào bình luận của bài viết" (`SR:320`).
- **Bằng chứng trong nguồn:** "\"upvotes\" = upvotes on the post itself (comment upvotes excluded)" (`DEC:794`, DEC-146), tức nguồn coi bình luận cũng có upvote.
- **Vấn đề:** (1) "Bài viết được tính" là thuật ngữ chuyên dùng cho công thức, xuất hiện ở bốn yêu cầu nhưng không có trong 2.1 (`sed -n 23,57p SR | grep -c "được tính"` → 0). Nghĩa của thuật ngữ chỉ đoán được từ ISH-M05-008.3. (2) 2.1 định nghĩa Upvote là đánh giá "cho một bài viết", nhưng 008.4 nói về "upvote vào bình luận"; một khái niệm có hai phạm vi.
- **Hướng xử lý:** thêm "Bài viết được tính" vào 2.1 (trỏ về điều kiện của 008.3), và mở rộng định nghĩa Upvote cho cả bài viết lẫn bình luận, hoặc đổi cách gọi ở 008.4.

## 2. Kết quả checklist của lượt

| Mã | Kết quả | Finding / ghi chú |
|---|---|---|
| CL-A05 | Không đạt | P2-01, P2-05, P2-06. Các dòng `Nói thẳng` khác đã so nguyên văn với DEC-047…052, DEC-099, DEC-100, DEC-126, DEC-132, DEC-140…153, QA-011, QA-017: khớp nghĩa |
| CL-A06 | Đạt | Đã suy luận lại đủ 18 dòng `Suy ra` (002.5, 002.6, 002.8, 003.9, 005.3, 006.5, 006.7, 006.8, 006.10, 007.6, 009.2, 010.1, 010.2, 010.3, 011.1, 011.5, 012.7, 012.8): đều có Ghi chú, không tạo số liệu hay quyền mới. Trường hợp 005.1 bị ghi sai là `Nói thẳng` được tính ở CL-A05 (P2-05) |
| CL-A07 | Đạt | Số trong SR: 11, 1, 3, 4 (suy ra), 10 tiếng, 10/phút, 11 (suy ra), 5, 6 (suy ra), 30, 0, 2, 7 ngày, 3 Topic đầu: đều có trong nguồn ở cột Nguồn. "168 giờ" (008.8, 2.1) là đổi đơn vị của "7-day" (DEC-052), cùng nghĩa; `grep "168"` trong registers không có kết quả liên quan |
| CL-B01 | Không đạt | P2-04 (ISH-M05-005). Các yêu cầu khác dùng đúng mẫu; 004.5–004.7 dùng `Nếu … thì` cho đầu ra bất thường của dịch vụ ngoài, đúng §4.6 |
| CL-B02 | Đạt | RULE-01/02/08 không báo. Đọc tay: không có yêu cầu nào hai hành vi độc lập. 008.11 và 008.12 nêu một khóa sắp xếp ghép (điểm → số bài → tên), coi là một quy tắc thứ tự |
| CL-B03 | Không đạt | P2-02 ("cố định"). Không có từ cấm trong danh sách §4.2 |
| CL-B04 | Đạt | RULE-03 không báo; đọc tay không có cụm thoát |
| CL-B05 | Đạt | RULE-05 không báo; các chỗ "đó" đều có danh từ đi kèm ("bài viết đó", "Topic đó", "Tag đó") |
| CL-B06 | Đạt | RULE-06/07 không báo; đọc tay không có tên bảng, trường hay công nghệ. "liên kết" (012.2) và "Bản ghi" (2.1) là ngôn ngữ nghiệp vụ, chấp nhận được |
| CL-B07 | Đạt | RULE-09 không báo |
| CL-B10 | Đạt | Mỗi cận có yêu cầu cấp dưới riêng: Topic 002.4/002.7; Tag 006.3/006.4; độ dài 006.6; gợi ý 003.3; tần suất 003.8. 008.1 dài 60 tiếng (đúng ngưỡng ~60) nhưng là một công thức |
| CL-B11 | Đạt | Mọi thao tác có vai trò đều có yêu cầu quyền: 001.3, 007.5, 009.2, 010.3, 011.5, 012.7, 012.8, 006.12 |
| CL-C01 | Không đạt | P2-03 (003.10 / 003.11); mặt mâu thuẫn của P2-02. Các cặp khác đã so: 002.2/011.2, 002.6/011, 003.4/004.3, 006.2/012.4, 006.12/012.1, 007.6/011.4: không mâu thuẫn |
| CL-C02 | Đạt | Không thấy cấp dưới chỉ nhắc lại cấp trên. 002.3 và 004.4 chồng một phần nhưng kiểm hai tình huống khác nhau (chưa từng gợi ý / gợi ý thất bại) |
| CL-C03 | Không đạt | P2-09. Vai trò viết hoa nhất quán (Guest, User, Mod, Admin); mọi mục 2.1 đều được dùng ở mục 4–5 hoặc ở 2.1 |
| CL-C04 | Không đạt | P2-04, P2-07. Mọi "Lý do" có nguồn: 5.3 DRAFT §3.1 + DEC-047; 5.5 QA-017; 5.6 DEC-008; 5.9 DRAFT §4.5; 5.10 "Nguồn chưa nêu lý do." kèm OP-M05-01 đúng khuôn |
| CL-C05 | Không đạt | P2-08. 5.1: đủ 12 tính năng; Must khớp module-registry (Must: M01–M10, M13); mốc P0/AI-P0/AI-P1/P1 khớp `iShare_dev_priority.md` (Follow, Trending ở P1) và DEC-151; các ngoại lệ 010.2, 011.3, 011.4 (theo dõi) và 012.3 (Trending) hợp với mốc P1 của hai tính năng đó |
| CL-D01 | Đạt | HDR-01…08: 0 ERROR/WARN |
| CL-D02 | Đạt | STR-01…09: 0 ERROR/WARN |
| CL-D03 | Đạt | REQ-00…04: 0 ERROR/WARN; 12 cấp trên, 92 cấp dưới |
| CL-D04 | Đạt | ID-01…06: 0 ERROR/WARN. Bản 0.1 đầu tiên; snapshot v0.1 trùng bản hiện tại, không có ID đổi nghĩa |
| CL-D05 | Đạt | TRC-01…05, 07, 09, 10: 0 ERROR/WARN |
| CL-D06 | Đạt | REF-01/02: 0 ERROR/WARN; 3.2 "Không có."; SR không tham chiếu ID của module khác |
| CL-F01 | Đạt | OPN-01…03: 0 ERROR/WARN; 9 OP đều có loại "Đề xuất" và trạng thái "Mở"; không thấy OP nào đã có câu trả lời trong register (đã đối chiếu DEC-140…153, QA-267…287) |
| CL-F02 | Đạt | Dòng lịch sử cuối 0.1 trùng header; bản đầu, không ở chế độ sửa |
| CL-F05 | Đạt | Mục 1–4 không có "phải" (`sed -n 13,94p SR | grep -n "phải"` → 0). 3.1: mọi ID cite ở Phụ lục A, B và routing đều có mặt (đối chiếu bằng script: 0 thiếu, 0 thừa), kèm ngày 2026-10-04 |
| CL-F06 | Đạt | Có `<!-- [Vietnamese Doc] -->`; tiếng Anh chỉ còn ở thuật ngữ bắt buộc (Topic, Tag, Trending, Upvote, Group Private, vai trò) |

## 3. Kết quả kiểm tra tự động

ERROR = 0, WARN = 0, INFO = 2.

Lệnh đã chạy (gốc repo): `python3 .agent-instructions/system_analysis/shared/sr-tools/check_sr.py --sr .agents/.claude/system_analysis/output/specs/ISH-SR-M05.md --routing .agents/.claude/system_analysis/output/specs/routing/ISH-RT-M05.md --tests .agents/.claude/system_analysis/output/specs/audit/work/tests-M05.md --json .agents/.claude/system_analysis/output/specs/audit/work/check-P2-M05-r1.json` → mã thoát 0.

INFO: `COV-99` (không truyền `--inventory`, đúng quy định của P2; COV thuộc P1); `TST-00` (135 ca cho 92 yêu cầu). Không còn mã ERROR hay WARN nào.

Script không bắt được lỗi mẫu câu của ISH-M05-005 (P2-04), nên lỗi này được lập finding riêng.

## 4. Hồ sơ xác minh

Mọi trích đoạn ở mục 1 đã được kiểm bằng `grep -n -F` (đường dẫn tính từ `.agents/.claude/system_analysis/output/`):

- `grep -n -F "Bài viết đã xuất bản và không bị ẩn bởi kiểm duyệt" specs/ISH-SR-M05.md` → 1 (dòng 37)
- `grep -n -F "chỉ tính vào điểm Trending các bài viết công khai" specs/ISH-SR-M05.md` → 1 (319)
- `grep -n -F "publish_state PUBLISHED and mod_state NORMAL" registers/decisions.md` → 1 (794)
- `grep -n -F "Visibility rule: publish_state=PUBLISHED AND mod_state=NORMAL" registers/decisions.md` → 1 (211)
- `grep -n -F "FLAGGED: AI/report flagged, awaiting mod" registers/decisions.md` → 1 (203)
- `grep -n -F "HIDDEN: author self-hide (reversible)" registers/decisions.md` → 1 (197)
- `grep -n -F "gồm các Topic cố định" specs/ISH-SR-M05.md` → 1 (130)
- `grep -n -F "hệ thống phải loại Topic nguồn khỏi danh mục Topic" specs/ISH-SR-M05.md` → 1 (387)
- `grep -n -F "hệ thống phải thay tên của Topic đó bằng tên mới" specs/ISH-SR-M05.md` → 1 (355)
- `grep -n -F "the source Topic is removed from the Topic catalog" registers/decisions.md` → 1 (790)
- `grep -n -F "hệ thống phải đánh dấu gợi ý đó là gợi ý cũ" specs/ISH-SR-M05.md` → 1 (196)
- `grep -n -F "hệ thống phải giữ gợi ý đó là gợi ý còn mới" specs/ISH-SR-M05.md` → 1 (197)
- `grep -n -F "attachment changes do not count" registers/decisions.md` → 1 (802)
- `grep -n -F "Hệ thống phải ghi nhận phản hồi gợi ý Topic khi tác giả gửi bài viết" specs/ISH-SR-M05.md` → 1 (232)
- `grep -n -F "hệ thống phải không ghi nhận phản hồi gợi ý Topic" specs/ISH-SR-M05.md` → 2 (243, 244)
- `grep -n -F "từ gợi ý Topic gần nhất" specs/ISH-SR-M05.md` → 1 (242)
- `grep -n -F "gợi ý gần nhất vì gợi ý trước đó đã bị thay thế" specs/ISH-SR-M05.md` → 1 (477)
- `grep -n -F "Feedback (AI suggest vs final selection) only recorded when not stale" registers/decisions.md` → 1 (293)
- `grep -n -F "Suggested topics replace the current selection" registers/decisions.md` → 1 (802)
- Tìm vắng mặt cho P2-05: `grep -n -i -E "latest|most recent|gần nhất|last suggest" registers/{decisions,qa-log,issue-queue}.md | grep -i -E "suggest|gợi ý|feedback|phản hồi"` → 0; `grep -n -i -E "feedback|phản hồi" registers/{decisions,qa-log}.md | grep -i -E "topic|suggest|gợi ý"` → 7 dòng (DEC:293, DEC:814, QA:208, 212, 215, 217, 743), không dòng nào nêu phản hồi lấy từ lần gợi ý nào
- `grep -n -F "Khi một người dùng khác tác giả của bài viết yêu cầu thay đổi Tag" specs/ISH-SR-M05.md` → 1 (273)
- `grep -n -F "Chỉ tác giả đổi Tag; Mod/Admin không đổi Tag của bài" specs/ISH-SR-M05.md` → 1 (492)
- `grep -n -F "A Mod or Admin does not change a post's Tags" registers/decisions.md` → 1 (786)
- `grep -n -F "Khi người dùng yêu cầu đổi tên một Tag" specs/ISH-SR-M05.md` → 1 (416); `"Khi người dùng yêu cầu gộp hai Tag"` → 1 (417); `"Khi người dùng yêu cầu xóa một Tag"` → 1 (418)
- `grep -n -F "Tag không có thao tác sửa cho người dùng nào" specs/ISH-SR-M05.md` → 1 (539); `"| ISH-M05-012.10 | DEC-051 | Nói thẳng |"` → 1 (540); `"| ISH-M05-012.11 | DEC-051, QA-107 | Nói thẳng |"` → 1 (541)
- `grep -n -F "Fully free — mod/admin do NOT edit/merge/delete under normal conditions" registers/decisions.md` → 1 (302)
- `grep -n -F "| ISH-M05-009.2 | DEC-144 | Suy ra |" specs/ISH-SR-M05.md` → 1 (518)
- `grep -n -F "Hệ thống phải cho phép Mod và Admin thay đổi trạng thái hoạt động của một Tag" specs/ISH-SR-M05.md` → 1 (398)
- `grep -n -F "Khi người dùng yêu cầu xóa một Topic" specs/ISH-SR-M05.md` → 1 (368)
- `grep -n -F "trạng thái đang theo dõi hay chưa theo dõi" specs/ISH-SR-M05.md` → 1 (296); `"ghi nhận người dùng đó đang theo dõi Topic đó"` → 1 (294); `"ghi nhận người dùng đó không còn theo dõi Topic đó"` → 1 (295)
- `grep -n -F "| Tag hoạt động | Mod hoặc Admin vô hiệu hóa Tag |" specs/ISH-SR-M05.md` → 1 (118)
- Tìm vắng mặt cho P2-08: `sed -n 114,123p specs/ISH-SR-M05.md | grep -c "theo dõi"` → 0
- `grep -n -F "Lượt đánh giá tích cực của người dùng cho một bài viết" specs/ISH-SR-M05.md` → 1 (53)
- `grep -n -F "không đếm upvote vào bình luận của bài viết" specs/ISH-SR-M05.md` → 1 (320)
- `grep -n -F "trên mọi bài viết được tính của Topic đó" specs/ISH-SR-M05.md` → 1 (317); `"số bài viết được tính đăng trong 7 ngày gần nhất"` → 2 (327, 328)
- Tìm vắng mặt cho P2-09: `grep -n "được tính" specs/ISH-SR-M05.md` → 4 (317, 318, 327, 328), không dòng nào trong 2.1; `sed -n 23,57p … | grep -c "được tính"` → 0
- `grep -n -F "\"upvotes\" = upvotes on the post itself (comment upvotes excluded)" registers/decisions.md` → 1 (794)
- Kiểm F05: so tập ID ở mục 3.1 (đã mở các dải `…`) với mọi ID DEC/ISS/QA cite ở Phụ lục A và routing: thiếu 0, thừa 0.

Finding đã cân nhắc rồi loại hoặc chỉnh:

- *Loại:* "168 giờ" không có trong nguồn (CL-A07). Đây là đổi đơn vị của "Rolling 7-day window", cùng nghĩa.
- *Loại:* "trong cùng một phút" ở 003.9. Cửa sổ đếm đã được chuyển R2 (`RT:26`), đúng RULES §6.1. Phần có thể quan sát được nêu ở "Chuyển lượt khác".
- *Loại:* 008.11 và 008.12 có hai tầng phá hòa trong một câu (CL-B10/B02). Coi là một khóa sắp xếp ghép duy nhất, không phải hai nhánh luồng.
- *Loại:* ISH-M05-004 dùng `Trong khi` cho cả lỗi tạm thời, trong khi DEC-099 nói lỗi tạm thời là "per-request degradation, not a state change". Đây là câu cấp trên tổng hợp hai luồng, các cấp dưới dùng đúng mẫu, không có hệ quả kiểm chứng khác nhau.
- *Loại:* "Lý do" của 5.11 lấy từ DRAFT §11.2, trong khi routing R6 ghi phần Moderator xem lại của §11.2 được làm rõ bởi DEC-144. Ý của lý do vẫn đúng với DEC-144; không vi phạm điều kiện CL-C04.
- *Chỉnh:* P2-02 ban đầu dự định xếp CL-C01 mức Cao, sau chuyển sang CL-B03 (Trung bình) làm mã chính, vì các yêu cầu cấp dưới đều nhất quán.

## 5. Phạm vi và giới hạn không kiểm được

- Đã đọc toàn bộ SR (`SR:1`–`SR:555`) và routing (`RT:1`–`RT:89`). Đã so nguyên văn mọi dòng `Nói thẳng` với nguồn ghi ở cột Nguồn trong `decisions.md`, `qa-log.md`, `issue-queue.md`, `module-registry.md`, `docs/_temp/iShare_modules.md` §3.1–3.4, §4.5, §7.2, §11.2, §11.5 và `iShare_dev_priority.md` §2–3.
- Không chạy `inventory.py` (P2 không cần ma trận; độ phủ thuộc P1). Không mở `tests-M05.md` và `disposition-M05.md` theo quy định của P2. `tests-M05.md` chỉ được truyền cho `check_sr.py --tests`, không đọc nội dung.
- Mọi mục checklist của P2 đều đã chấm; không có mục nào `Không kiểm được`.
- Lượt P2 không đánh giá các mơ hồ có sẵn trong nguồn (CL-A11), độ đủ của hành vi bất thường (CL-B09) hay khung hành vi (CL-B13); các mục đó thuộc P3.

## 6. Chuyển lượt khác

- P3 (CL-A11/CL-B08): ISH-M05-008.1/008.2 dùng "được đăng trong 7 ngày", DEC-142 dùng "posts created within the window". Bài tạo nháp 10 ngày trước, gửi và xuất bản 2 ngày trước thì có được +1 hay không?
- P3 (CL-A11/CL-B08): ISH-M05-008.11/008.12 "theo thứ tự chữ cái từ A đến Z": chưa rõ thứ tự với chữ tiếng Việt có dấu (Đ, Ư, Â…) và với chữ hoa, chữ thường của tên Tag.
- P3 hoặc P1 (CL-B08/CL-E03): giới hạn 10 yêu cầu gợi ý mỗi phút (003.8/003.9). Việc yêu cầu bị từ chối vì văn bản ngắn hoặc khi AI tắt có bị đếm hay không là hệ quả người dùng thấy được, nhưng đang nằm ở R2 (`RT:26`).
- P3 (CL-B13/CL-B09): DEC-145 (`DEC:790`) nói Topic nguồn sau khi gộp "can no longer be selected, suggested, ranked in Trending or followed". SR chỉ có 011.2 "loại khỏi danh mục"; cần kiểm có yêu cầu cho việc từ chối theo dõi Topic đã gộp và loại Topic đó khỏi xếp hạng Trending hay chưa.
- P1 (CL-A01/CL-A02): QA-011 cho Guest "Xem danh sách Topic / Tag / Khối lớp"; SR có 001.3 cho Topic, chưa thấy chỗ đi cho danh sách Tag.
- P1 (CL-A10/CL-E03): DEC-146 (`DEC:794`, thuộc M05) có câu "Posts are not excluded by the author's account status (QA-236 unchanged)", nhưng routing đưa QA-236 sang R5 M14 (`RT:62`). Cần kiểm phần này có thuộc công thức của M05 hay không.
- P1 (CL-A01): DRAFT `iShare_modules.md` §7.2 Trending/Popular (Views, Stars, Comments, Bookmarks, Recency) không có trong 3.1, Phụ lục A hay routing (`grep "7.2"` trên SR và RT → 0 kết quả liên quan).

## 7. Ghi chú P2.3 — đối chiếu với selfcheck của Author (mở sau khi đã chấm)

Mở `selfcheck-M05.md` sau khi đã chấm xong mục 2. Không mở `tests-M05.md` và `disposition-M05.md`. Các mục selfcheck ghi `Đạt` nhưng lượt này chấm `Không đạt`:

| Mã | Selfcheck (Author) | P2 (Auditor) | Ghi chú |
|---|---|---|---|
| CL-A05 | Đạt (selfcheck dòng 14; tự lưu ý 012.9 hiểu "do NOT edit" là đổi tên Tag) | Không đạt | Author chưa xét phạm vi vai trò (Mod/Admin → mọi người dùng) và chữ "gần nhất" ở 005.1; định nghĩa "Bài viết công khai" chưa được đối chiếu với DEC-146 (P2-01, P2-05, P2-06) |
| CL-B01 | Đạt (dòng 21) | Không đạt | Selfcheck dựa vào việc EARS-01…03 không báo; ISH-M05-005 lọt qua script (P2-04) |
| CL-B03 | Đạt (dòng 23) | Không đạt | Selfcheck chỉ xét RULE-04 và 008.11/008.12; chưa xét "cố định" ở 001 (P2-02) |
| CL-C01 | Đạt (dòng 34) | Không đạt | Selfcheck đã xét 001.1 với 011.2, nhưng chưa xét câu cấp trên 001 và cặp 003.10/003.11 (P2-02, P2-03) |
| CL-C03 | Đạt (dòng 36) | Không đạt | "Bài viết được tính" không có ở 2.1; định nghĩa Upvote chỉ cho bài viết, trái với 008.4 (P2-09) |
| CL-C04 | Đạt (dòng 37) | Không đạt | Selfcheck chỉ kiểm "Lý do", chưa kiểm cấp trên với cấp dưới (P2-04, P2-07) |
| CL-C05 | Đạt (dòng 38) | Không đạt | 5.2 thiếu trạng thái theo dõi (P2-08) |

Khác biệt nhỏ: selfcheck ghi CL-D04 là `Không áp dụng`, lượt này ghi `Đạt` (ID-01…06 không báo và snapshot trùng bản hiện tại); hai cách ghi không dẫn tới finding.
