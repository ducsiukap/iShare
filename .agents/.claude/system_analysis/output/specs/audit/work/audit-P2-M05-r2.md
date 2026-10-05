# Tệp lượt — ISH-AUD-M05-r2 · lượt P2 (Chất lượng yêu cầu)
<!-- [Vietnamese Doc] -->

| Trường | Giá trị |
|---|---|
| Module | M05 |
| Vòng | 2 |
| Lượt | P2 |
| SR được audit | ISH-SR-M05, phiên bản 0.2 (2026-10-05, Bản nháp) |
| Routing | ISH-RT-M05, phiên bản 0.2 (2026-10-05) |
| Báo cáo vòng trước | `specs/audit/ISH-AUD-M05-r1.md` (Chưa đạt, 21 finding) |
| Tóm tắt Author đã nhận và không dùng | Không có. Người gọi chỉ đưa mã module, vòng, lượt, gốc repo và đường dẫn báo cáo vòng 1 |

Ghi chú phiên bản: `ISH-SR-M05.md` và `ISH-RT-M05.md` trùng hoàn toàn với `snapshot-ISH-SR-M05-v0.2.md` và `snapshot-ISH-RT-M05-v0.2.md` (`diff -q` không báo khác). Phần đã đổi được xác định bằng `diff snapshot-ISH-SR-M05-v0.1.md ISH-SR-M05.md`.

Số đếm thay đổi (theo ID, để MERGE và P1 đối chiếu): bản 0.2 có 12 cấp trên và 107 cấp dưới (119 yêu cầu). Thêm 17 ID (001.5, 002.10, 002.11, 005.4, 006.16, 008.13…008.19, 011.6…011.10); bỏ 2 ID (002.4, 010.4); sửa nội dung 13 ID (001, 002, 002.6, 003.11, 004, 005, 005.1, 006, 008.1, 008.2, 008.11, 008.12, 012). Tổng 32/119 (khoảng 27%), dưới một phần ba; không thêm yêu cầu cấp trên nào.

## 0. Kiểm finding vòng 1 thuộc mục của lượt P2

| AUD | Mục | Trạng thái | Bằng chứng mới |
|---|---|---|---|
| AUD-M05-06 | CL-A05, CL-C03 (phần CL-B08 thuộc P3) | Đã sửa | "đang ở trạng thái kiểm duyệt bình thường (không bị gắn cờ chờ xử lý, không bị Mod ẩn)" (`ISH-SR-M05.md:37`); khớp "Only posts that are currently public (publish_state PUBLISHED and mod_state NORMAL, DEC-033)" (`decisions.md:797`). Bài tự ẩn, bài bị gắn cờ nay đều bị loại rõ ràng |
| AUD-M05-07 | CL-B03, CL-C01 | Đã sửa | "mà không người dùng nào thêm hay xóa được Topic" (`ISH-SR-M05.md:140`). Chữ "cố định" đã bỏ; "xóa Topic" và "loại khỏi danh mục khi gộp" là hai thao tác nguồn tách riêng (DEC-049 dòng 285, DEC-145 dòng 793) |
| AUD-M05-08 | CL-C01, CL-A05 | Đã sửa | "hệ thống phải giữ nguyên trạng thái mới hoặc cũ của gợi ý đó" (`ISH-SR-M05.md:209`); trình tự "gợi ý → sửa tiêu đề → thêm tệp" nay cho gợi ý cũ ở cả 003.10 và 003.11 |
| AUD-M05-09 | CL-C04, CL-B01 | Đã sửa | "Khi tác giả gửi một bài viết có gợi ý Topic còn mới, hệ thống phải ghi nhận phản hồi gợi ý Topic cho bài viết đó." (`ISH-SR-M05.md:244`): đúng mẫu `Khi`, có điều kiện, không còn ngược 005.2/005.3 |
| AUD-M05-10 | CL-A05, CL-A06 | Đã sửa (chuyển stakeholder đã xong) | "\| ISH-M05-005.1 \| DEC-157, ISS-233, QA-293, DEC-050 \| Nói thẳng \|" (`ISH-SR-M05.md:505`); nguồn "compares only the latest suggestion with the final selection" (`decisions.md:841`) |
| AUD-M05-11 | CL-A05 | Đã sửa | "\| ISH-M05-006.12 \| DEC-144, QA-273 \| Suy ra \|" (`ISH-SR-M05.md:521`); 012.9, 012.10, 012.11 đổi sang `Suy ra` (`ISH-SR-M05.md:580`, `:581`, `:582`), mỗi dòng có phép suy luận. Đã cân nhắc 001.5 (trước là 010.4, vẫn `Nói thẳng`): không mở lại, xem mục 4 |
| AUD-M05-12 | CL-C04 | Đã sửa (có lỗi cùng loại mới ở các ID thêm, xem P2-02) | 010.4 bỏ, nội dung chuyển thành "\| ISH-M05-001.5 \| Khi người dùng yêu cầu xóa một Topic, hệ thống phải từ chối yêu cầu đó. \|" (`ISH-SR-M05.md:154`) dưới cấp trên 001 (`:140`); cấp trên 012 nay "Hệ thống phải giới hạn thao tác quản trị Tag ở việc Mod, Admin vô hiệu hóa, mở lại một Tag." (`:423`) bao quát 012.9…012.11 |
| AUD-M05-19 | CL-C05 | Đã sửa | "\| Chưa theo dõi Topic \| Người dùng đã đăng nhập theo dõi Topic \| Đang theo dõi Topic \| ISH-M05-007.1 \|" (`ISH-SR-M05.md:129`); dòng 130 (007.2), 131 (011.3), 132 (011.7, 011.8) |
| AUD-M05-20 | CL-C03 | Đã sửa | "\| Bài viết được tính \| Bài viết công khai không thuộc Group Private" (`ISH-SR-M05.md:38`); "Lượt đánh giá tích cực của người dùng cho một bài viết hoặc một bình luận." (`ISH-SR-M05.md:55`) |

Các finding vòng 1 khác (AUD-01…05, 13…18, 21) thuộc mục của P1 hoặc P3; lượt này không kiểm trạng thái của chúng.

## 1. Phát hiện nháp

### P2-01 — ISH-M05-007.1 chấp nhận theo dõi mọi Topic, trái với ISH-M05-011.7 từ chối theo dõi Topic đã bị loại khỏi danh mục

| Lớp | DEFECT | Nhãn | Hồi quy | Mức đề xuất | Trung bình | Checklist | CL-C01 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-007.1 (`ISH-SR-M05.md:308`), ISH-M05-011.7 (`ISH-SR-M05.md:412`); cấp trên ISH-M05-007 (`ISH-SR-M05.md:298`).
- **Bằng chứng trong SR:**
  - "Khi người dùng đã đăng nhập yêu cầu theo dõi một Topic chưa theo dõi, hệ thống phải ghi nhận người dùng đó đang theo dõi Topic đó." (`ISH-SR-M05.md:308`)
  - "Khi người dùng yêu cầu theo dõi một Topic đã bị loại khỏi danh mục Topic, hệ thống phải từ chối yêu cầu đó." (`ISH-SR-M05.md:412`)
  - "Hệ thống phải cho phép người dùng đã đăng nhập theo dõi một Topic." (`ISH-SR-M05.md:298`)
  - 5.2 giữ Topic nguồn tồn tại như một trạng thái: "Topic đã loại khỏi danh mục Topic (trạng thái cuối)" (`ISH-SR-M05.md:126`).
- **Bằng chứng trong nguồn:** "it can no longer be selected, suggested, ranked in Trending or followed" (`decisions.md:793`, DEC-145).
- **Vấn đề:** 011.7 được thêm ở bản 0.2 để xử lý AUD-M05-03, nhưng 007.1 và cấp trên 007 vẫn áp dụng cho "một Topic" bất kỳ, không giới hạn vào Topic thuộc danh mục. Ca kiểm: User A (đã đăng nhập, chưa theo dõi) yêu cầu theo dõi Topic nguồn đã bị gộp. Theo 007.1, hệ thống ghi nhận A đang theo dõi; theo 011.7, hệ thống từ chối. Hai yêu cầu cùng đối tượng, cùng sự kiện, khác kết quả. Báo cáo vòng 1 đã nêu hai hướng sửa ("thêm yêu cầu … gồm cả việc từ chối theo dõi; hoặc giới hạn phạm vi của 007 và 008 vào Topic trong danh mục"); bản sửa chỉ làm vế thứ nhất mà không giới hạn 007.1. Với Trending, 008.18 đã giới hạn "mọi Topic trong danh mục Topic" nên không có mâu thuẫn tương tự.
- **Lý do mức:** CL-C01 mặc định Cao; hạ một mức (như AUD-M05-08) vì ý của nguồn rõ, chỉ xảy ra với Topic đã bị gộp, và người đọc có thể hiểu 011.7 là ngoại lệ của 007.1.
- **Hệ quả nếu không sửa:** Ca kiểm chấp nhận cho "theo dõi Topic nguồn" có hai "Then" khác nhau tùy chọn yêu cầu nào.
- **Hướng xử lý (Author quyết cách viết):** Giới hạn 007.1 (và cấp trên 007 nếu cần) vào Topic thuộc danh mục Topic, hoặc đưa điều kiện loại trừ vào 007.1; cân nhắc chuyển 011.7 sang tính năng 5.9 (liên quan P2-02).

### P2-02 — Các yêu cầu cấp dưới mới thêm nằm ngoài câu cấp trên (ISH-M05-002.10, 002.11, 006.16, 011.7)

| Lớp | DEFECT | Nhãn | Hồi quy | Mức đề xuất | Trung bình | Checklist | CL-C04 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-002 (`ISH-SR-M05.md:162`) với 002.10 (`:180`), 002.11 (`:181`); ISH-M05-006 (`:265`) với 006.16 (`:290`); ISH-M05-011 (`:396`) với 011.7 (`:412`).
- **Bằng chứng trong SR:**
  - "Hệ thống phải yêu cầu mỗi bài viết đã gửi có từ 1 đến 3 Topic" (`ISH-SR-M05.md:162`)
  - "Khi người dùng, kể cả Guest, xem một bài viết, hệ thống phải hiển thị các Topic" (`ISH-SR-M05.md:180`)
  - "Hệ thống phải cho phép tác giả lưu bản nháp của bài viết khi bài viết chưa có Topic nào." (`ISH-SR-M05.md:181`)
  - "Hệ thống phải gắn cho mỗi bài viết từ 0 đến 5 Tag tự do do tác giả nhập." (`ISH-SR-M05.md:265`)
  - "hệ thống phải hiển thị các Tag hoạt động của bài viết đó" (`ISH-SR-M05.md:290`)
  - "hệ thống phải chuyển mọi bài viết đang gắn Topic nguồn sang Topic đích." (`ISH-SR-M05.md:396`)
  - "Khi người dùng yêu cầu theo dõi một Topic đã bị loại khỏi danh mục Topic" (`ISH-SR-M05.md:412`)
- **Vấn đề:** Cùng nguyên nhân với AUD-M05-12 (đã sửa cho 010.4 và 012.9…012.11), nay xuất hiện ở các ID thêm trong bản 0.2:
  - 002 là ràng buộc số Topic của bài viết **đã gửi**; 002.10 là hành vi hiển thị Topic cho người xem bài, 002.11 là hành vi với **bản nháp**. Cả hai nằm ngoài câu cấp trên.
  - 006 nói về việc gắn 0–5 Tag; 006.16 là hành vi hiển thị Tag cho người xem bài.
  - 011 chỉ nói về hệ quả "chuyển bài viết" của thao tác gộp; 011.7 là phản hồi cho một yêu cầu **theo dõi**, không phải thao tác gộp (011.6, 011.8…011.10 vẫn là hệ quả hoặc điều kiện của thao tác gộp nên không nêu ở đây).
- **Hệ quả nếu không sửa:** Cấp trên không cho người đọc biết tính năng gồm những hành vi nào; CL-C04 ("cấp dưới thêm hành vi cấp trên không nói là DEFECT").
- **Hướng xử lý (Author quyết cách viết):** Mở rộng câu cấp trên của 002, 006, 011 để bao quát; hoặc chuyển 002.10/006.16 về một tính năng có cấp trên phù hợp (lưu ý OP-M05-12 về chủ sở hữu hiển thị), chuyển 011.7 sang 5.9 Theo dõi Topic. Không đổi khung 12 tính năng của DEC-151 nếu chỉ sửa câu cấp trên.

### P2-03 — ISH-M05-005.4 đã quyết điều OP-M05-10 còn đang hỏi, và đề xuất mặc định của OP ngược với 005.4

| Lớp | DEFECT | Lớp phụ | GAP | Nhãn | Hồi quy | Mức đề xuất | Trung bình | Checklist | CL-F01 |
|---|---|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-005.4 (`ISH-SR-M05.md:257`); OP-M05-10 (`ISH-SR-M05.md:596`).
- **Bằng chứng trong SR:**
  - "hệ thống phải ghi đúng một phản hồi gợi ý Topic cho lần gửi đó" (`ISH-SR-M05.md:257`)
  - "Đề xuất mặc định: chỉ ghi ở lần gửi đầu tiên." (`ISH-SR-M05.md:596`), với câu hỏi "Bài viết bị từ chối rồi được tác giả gửi lại thì có ghi thêm phản hồi gợi ý Topic không".
- **Bằng chứng trong nguồn:**
  - "one record per submission" (`decisions.md:841`, DEC-157)
  - "Chỉ lần gợi ý gần nhất; một bản ghi mỗi lần gửi bài." (`qa-log.md:1028`, QA-293)
  - "REJECTED: mod rejected, author can fix and resubmit" (`decisions.md:198`, DEC-031)
- **Vấn đề:** 005.4 (thêm ở bản 0.2) viết "mỗi lần gửi có gợi ý còn mới → đúng một phản hồi cho lần gửi đó". Lần gửi lại sau khi bị từ chối cũng là một lần gửi, nên theo 005.4 hệ thống ghi thêm một phản hồi. OP-M05-10 vẫn Mở và đề xuất "chỉ ghi ở lần gửi đầu tiên". Ca kiểm: bài bị Mod từ chối, tác giả chỉ đổi tệp đính kèm (gợi ý vẫn còn mới, theo 003.11) rồi gửi lại. Theo 005.4: hai phản hồi; theo đề xuất của OP-M05-10: một phản hồi. Có hai khả năng và cả hai đều là lỗi hồ sơ: (a) DEC-157 "one record per submission" đã trả lời OP-M05-10 thì OP phải xóa (CL-F01 "không còn OP đã được trả lời") và đề xuất mặc định của nó sai; (b) DEC-157 chỉ nói "một bản ghi cho mỗi lần gửi thay vì mỗi lần gợi ý", không nói về gửi lại, thì 005.4 đã tự chọn một phương án trước khi stakeholder trả lời.
- **Hệ quả nếu không sửa:** Dữ liệu phản hồi cho vòng đánh giá AI (M13) có số bản ghi khác nhau tùy người cài đặt đọc 005.4 hay OP-M05-10.
- **Hướng xử lý (Author quyết cách viết):** Xác định DEC-157 có trả lời câu hỏi gửi lại hay không. Nếu có: xóa OP-M05-10, ghi Lịch sử. Nếu không: viết 005.4 ở dạng không quyết phần gửi lại (ví dụ giới hạn vào lần gửi đầu, hoặc ghi rõ phụ thuộc OP-M05-10) và giữ OP. Lớp phụ GAP: nếu Author không tự xác định được, hỏi stakeholder theo §8.3.

### P2-04 — ISH-M05-008.15 trùng ý với ISH-M05-008.14

| Lớp | DEFECT | Nhãn | Hồi quy | Mức đề xuất | Thấp | Checklist | CL-C02 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.14 (`ISH-SR-M05.md:344`), ISH-M05-008.15 (`ISH-SR-M05.md:345`).
- **Bằng chứng trong SR:**
  - "số người dùng đã đăng nhập khác nhau, không kể tác giả" (`ISH-SR-M05.md:344`)
  - "Hệ thống phải không đếm lượt mở trang chi tiết bài viết của Guest vào số người xem." (`ISH-SR-M05.md:345`)
- **Bằng chứng trong nguồn:** "Guest views are not counted" (`decisions.md:845`, DEC-158).
- **Vấn đề:** 008.14 đã giới hạn số người xem vào người dùng đã đăng nhập, và 2.1 định nghĩa Guest là người truy cập chưa đăng nhập. Mọi ca kiểm của 008.15 đều đã được 008.14 quyết định; 008.15 không thêm hành vi kiểm chứng được nào.
- **Hệ quả nếu không sửa:** Hai yêu cầu cho một hành vi; sửa một mà quên sửa yêu cầu kia sẽ sinh mâu thuẫn.
- **Hướng xử lý (Author quyết cách viết):** Gộp 008.15 vào 008.14 (ghi ID bị bỏ ở Lịch sử), hoặc giữ và ghi rõ ở Phụ lục A rằng 008.15 chỉ nhắc lại nguồn; RULES §10 CL-C02 coi nhắc lại là trùng.

### P2-05 — ISH-M05-002.11 dùng mẫu Phổ quát với điều kiện trạng thái đặt cuối câu

| Lớp | DEFECT | Nhãn | Hồi quy | Mức đề xuất | Thấp | Checklist | CL-B01 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-002.11 (`ISH-SR-M05.md:181`).
- **Bằng chứng trong SR:** "Hệ thống phải cho phép tác giả lưu bản nháp của bài viết khi bài viết chưa có Topic nào." (`ISH-SR-M05.md:181`)
- **Bằng chứng trong quy tắc:** RULES §4.6 bước 3: điều kiện là trạng thái kéo dài thì dùng `Trong khi …`; bước 2: sự kiện tức thời (tác giả lưu) thì dùng `Khi …`.
- **Vấn đề:** Câu có một trạng thái ("bài viết chưa có Topic nào") và một sự kiện (tác giả lưu bản nháp) nhưng viết theo mẫu Phổ quát, đặt "khi" ở cuối câu. Đây là cùng dạng lỗi mẫu câu đã nêu ở AUD-M05-09 cho 005. Script không bắt được (EARS-01…03 không báo). Các câu "… khi tính điểm Trending" ở 008.4…008.7, 008.17 là ngữ cảnh áp dụng của quy tắc phổ quát, không phải điều kiện, nên không tính.
- **Lý do mức:** CL-B01 mặc định Trung bình; hạ một mức vì câu vẫn chỉ đọc được một cách.
- **Hướng xử lý (Author quyết cách viết):** Viết lại theo mẫu `Khi …` hoặc `Trong khi …, khi …`.

### P2-06 — Dòng truy vết của ISH-M05-006.16 ghi `Nói thẳng` và dẫn "AI Classification trên post" cho việc hiển thị Tag

| Lớp | DEFECT | Nhãn | Hồi quy | Mức đề xuất | Trung bình | Checklist | CL-A05 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** Phụ lục A, ISH-M05-006.16 (`ISH-SR-M05.md:525`); yêu cầu ở `ISH-SR-M05.md:290`.
- **Bằng chứng trong SR:**
  - "\| ISH-M05-006.16 \| QA-011, DEC-051 \| Nói thẳng \|" (`ISH-SR-M05.md:525`), Ghi chú "Phân loại hiển thị trên bài (QA-011); Tag bị vô hiệu hóa ẩn (DEC-051)"
  - "hệ thống phải hiển thị các Tag hoạt động của bài viết đó" (`ISH-SR-M05.md:290`)
- **Bằng chứng trong nguồn:**
  - "AI: Xem AI Summary + AI Classification trên post" (`qa-log.md:137`, QA-011)
  - "Tag: user tự quyết định hoàn toàn, AI không can thiệp" (`qa-log.md:209`, QA-017)
  - "Phase 5 (DEC-050/051) đã thu hẹp phạm vi AI classification chỉ còn Topic" (`qa-log.md:1004`, QA-269)
  - "tag chip hidden from display" (`decisions.md:303`, DEC-051): chỉ nói về Tag bị vô hiệu hóa.
  - "it then shows again on the posts that carry it" (`decisions.md:813`, DEC-150): không có trong cột Nguồn của 006.16.
- **Vấn đề:** Hai nguồn ghi ở cột Nguồn không nêu rõ hành vi "hiển thị các Tag hoạt động trên bài viết cho mọi người dùng". Dòng "AI Classification trên post" của QA-011 chỉ áp dụng cho Topic (QA-017, QA-269). DEC-051 chỉ nói Tag bị vô hiệu hóa bị ẩn; việc Tag hoạt động được hiển thị là suy ra ngược từ câu đó. Phần "kể cả Guest" dựa vào dòng "POST: Xem/đọc post" (`qa-log.md:132`), dòng này không được dẫn trong Ghi chú. Hành vi có cơ sở (DEC-150 nói Tag mở lại "shows again on the posts"), nhưng cơ sở `Nói thẳng` và lời giải thích ở Ghi chú không đúng với nguồn được dẫn. Với 002.10 (hiển thị Topic) thì dẫn "AI Classification trên post" là hợp lệ, nên không lập finding.
- **Lý do mức:** CL-A05 mặc định Cao; hạ một mức (như AUD-M05-11) vì hành vi có nguồn, chỉ dòng truy vết dẫn sai.
- **Hệ quả nếu không sửa:** Người kiểm truy vết sẽ tìm thấy một nguồn nói về AI phân loại Topic làm căn cứ cho hiển thị Tag.
- **Hướng xử lý (Author quyết cách viết):** Sửa cột Nguồn (thêm DEC-150, dòng POST của QA-011) và Ghi chú; đổi sang `Suy ra` kèm phép suy luận nếu không có câu nguồn nêu thẳng.

### P2-07 — Lịch sử sửa đổi 0.2 không ghi các thay đổi ở mục 4 và mục 5.1

| Lớp | DEFECT | Mức đề xuất | Thấp | Checklist | CL-F02 |
|---|---|---|---|---|---|

- **Vị trí:** Lịch sử sửa đổi, dòng 0.2 (`ISH-SR-M05.md:458`); mục 4 (`:91`, `:95`); mục 5.1 (`:117`); mục 5.2 (`:132`).
- **Bằng chứng:**
  - Bản 0.1: "Topic là danh mục một tầng gồm các lĩnh vực tri thức cố định" (`snapshot-ISH-SR-M05-v0.1.md:85`). Bản 0.2: "gồm 11 lĩnh vực tri thức chốt sẵn, không ai thêm hay xóa được" (`ISH-SR-M05.md:91`), và câu ở `:95` thêm "từ upvote, bình luận, bookmark và người xem trong 7 ngày gần nhất".
  - Bản 0.1: "Gộp Topic | ISH-M05-011 | Must | P0 | ISH-M05-011.3, ISH-M05-011.4: P1" (`snapshot-ISH-SR-M05-v0.1.md:111`). Bản 0.2: "ISH-M05-011.3, ISH-M05-011.4, ISH-M05-011.6, ISH-M05-011.7: P1" (`ISH-SR-M05.md:117`).
  - Dòng Lịch sử chỉ ghi "5.2 thêm trạng thái theo dõi" (`ISH-SR-M05.md:458`). Dòng 5.2 mới "Người dùng yêu cầu theo dõi, hoặc Mod/Admin yêu cầu gộp với Topic đó" (`ISH-SR-M05.md:132`) gồm cả từ chối gộp, không chỉ trạng thái theo dõi.
  - Tìm "mục 4", "Tổng quan chức năng", "5.1", "Ngoại lệ" trong dòng 0.2: không có kết quả nói về mục 4 hay mục 5.1 (chuỗi "5.1" chỉ khớp ID "005.1" và "Lý do 5.12, 5.13"; xem mục 4 của tệp này).
- **Vấn đề:** CL-F02 yêu cầu mô tả đúng thay đổi thực tế ở chế độ sửa. Hai thay đổi nội dung ở mục 4 và một thay đổi mốc ở 5.1 không có trong Lịch sử.
- **Hướng xử lý:** Bổ sung vào dòng 0.2 (hoặc dòng của phiên bản kế tiếp) các thay đổi ở mục 4, 5.1 và hàng 5.2 về từ chối gộp.

## 2. Kết quả checklist của lượt

| Mã | Kết quả | Finding / ghi chú |
|---|---|---|
| CL-A05 | Không đạt | P2-06. Đã mở nguồn cho mọi dòng `Nói thẳng` mới hoặc đổi (001, 001.5, 002, 002.10, 002.11, 003.11, 004, 005, 005.1, 005.4, 006, 006.16, 007, 008, 008.1…008.3, 008.11…008.19, 011.6…011.10, 012): khớp, trừ 006.16. AUD-06, 10, 11 đã sửa |
| CL-A06 | Đạt | 22 dòng `Suy ra` được suy lại (002.5, 002.6, 002.8, 003.9, 005.3, 006.5, 006.7, 006.8, 006.10, 006.12, 007.6, 009.2, 010.1…010.3, 011.1, 011.5, 012.7…012.11); không tạo số liệu, ngoại lệ hay quyền mới. Phép suy của 012.9 ("vai trò thấp hơn không có quyền hơn Mod/Admin") chỉ dùng thứ bậc vai trò để từ chối, không cấp quyền |
| CL-A07 | Đạt | Mọi số có nguồn: 11 (DEC-048), 1–3 (DEC-049), 10 tiếng (DEC-147), 10/phút (DEC-100), 3 (DEC-050, DEC-152), 0–5 (DEC-143), 30 ký tự (DEC-051), 7 ngày/168 giờ (DEC-052), 2, 1, 0,1 (DEC-158, `decisions.md:845`); "thứ 4/6/11" là suy ra từ cận |
| CL-B01 | Không đạt | P2-05. AUD-09 đã sửa (005 nay mẫu `Khi`) |
| CL-B02 | Đạt | RULE-01/02/08 không báo. Đọc tay: 012 cấp trên dùng dấu phẩy ("Mod, Admin vô hiệu hóa, mở lại") là câu cấp trên nêu phạm vi, các hành vi có cấp dưới riêng (012.1, 012.5, 012.7, 012.8); 008.13 là một công thức |
| CL-B03 | Đạt | Không từ mơ hồ. "Cố định" ở 001 đã bỏ (AUD-07). Cấp trên 004 "xử lý … sao cho tác giả luôn chọn được Topic thuộc danh mục Topic" nêu kết quả quan sát được; chấp nhận ở cấp trên |
| CL-B04 | Đạt | RULE-03 không báo |
| CL-B05 | Đạt | RULE-05 không báo; `grep -w "nó\|chúng\|họ"` → 0; mọi "đó" có danh từ đi kèm |
| CL-B06 | Đạt | RULE-06/07 không báo; yêu cầu mới (008.13…008.16) mô tả hành vi đếm, chi tiết lưu lượt xem nằm ở R1 (`ISH-RT-M05.md:20`) |
| CL-B07 | Đạt | RULE-09 không báo; dấu "…" chỉ có trong khoảng ID ở Lịch sử, không phải placeholder |
| CL-B10 | Đạt | Mỗi cận một yêu cầu (002.5/002.7, 006.4/006.6, 003.3, 003.8); 011.8 gộp hai điều kiện (nguồn hoặc đích đã bị loại) cho cùng một kết quả theo đúng câu DEC-159, không phải hai nhánh luồng |
| CL-B11 | Đạt | Mọi thao tác theo vai trò có yêu cầu quyền: theo dõi (007.5), đổi Topic bài (009, 009.2), đổi tên (010.3), gộp (011.5), vô hiệu hóa/mở lại (012.7, 012.8), cấm sửa/gộp/xóa Tag (012.9…012.11), cấm xóa Topic (001.5) |
| CL-C01 | Không đạt | P2-01 (Hồi quy). AUD-07, AUD-08 đã sửa. Đã so các cặp: 002.6/009.1, 002.5/003.14/004.4, 003.10/003.11, 005/005.2/005.3, 007.1/011.7, 008.18/011.6, 008.19/012.3, 006.16/012.1, 001/011.2 |
| CL-C02 | Không đạt | P2-04 |
| CL-C03 | Đạt | Mọi thuật ngữ và vai trò dùng ở mục 5 có trong 2.1; mọi mục 2.1 được dùng (Bookmark, Người xem, Điểm tương tác, Trở thành công khai lần đầu, Thứ tự bảng chữ cái tiếng Việt ở 008.11…008.14). AUD-06 (phần C03), AUD-20 đã sửa. Câu hỏi về vị trí của f, j, w, z, chữ số, dấu thanh trong định nghĩa "Thứ tự bảng chữ cái tiếng Việt" chuyển P3 (mục 6) |
| CL-C04 | Không đạt | P2-02 (Hồi quy). AUD-09, AUD-12 đã sửa. "Lý do" của 5.6, 5.9, 5.12, 5.13 khớp lời văn nguồn (DEC-008, QA-043, DEC-049); 5.10 "Nguồn chưa nêu lý do." có OP-M05-01 |
| CL-C05 | Đạt | 5.1: Must khớp `module-registry.md:33` ("Must \| 10 \| M01–M10, M13"); mốc P0/P1/AI-P0/AI-P1 khớp `iShare_dev_priority.md` (Follow, Bookmark, Trending ở Giai đoạn 2 [P1]) và DEC-151; ngoại lệ 011.6, 011.7: P1 nhất quán với 007, 008. 5.2: mọi hàng trỏ ID có thật, không có trạng thái treo. AUD-19 đã sửa |
| CL-D01 | Đạt | HDR-01…08 không báo; Trạng thái Bản nháp, phiên bản 0.2, ngày 2026-10-05 |
| CL-D02 | Đạt | STR-01…09 không báo |
| CL-D03 | Đạt | REQ-00…04 không báo; 12 cấp trên, 107 cấp dưới, mỗi tính năng có Lý do |
| CL-D04 | Đạt | ID-01…06 không báo. So với bản 0.1: 002.4 và 010.4 bị bỏ, ghi ở Lịch sử, không dùng lại; ID mới lấy số kế tiếp; các ID sửa nội dung (004, 012, 003.11…) là sửa theo finding vòng 1 hoặc DEC mới và có ở Lịch sử |
| CL-D05 | Đạt | TRC-01…05, 07, 09, 10 không báo; 17 ID mới đều có một dòng Phụ lục A |
| CL-D06 | Đạt | REF-01/02 không báo; 3.2 "Không có."; không có tham chiếu ID của module khác |
| CL-F01 | Không đạt | P2-03 (Hồi quy). OPN-01…03 không báo; 11 OP (01, 02, 04…12) đều loại Đề xuất, trạng thái Mở; đã đối chiếu DEC-154…159: OP-M05-01, 02, 04…09, 11, 12 chưa được trả lời |
| CL-F02 | Không đạt | P2-07. Dòng cuối 0.2 trùng header |
| CL-F05 | Đạt | Mục 1–4 không có "phải" (`sed -n 13,100p \| grep phải` → 0). Mọi ID nguồn dẫn ở Phụ lục A, B và routing có trong 3.1 (script riêng ở scratchpad: 0 ID thiếu); TRC-11 không báo. 3.2 "Không có." |
| CL-F06 | Đạt | Có `[Vietnamese Doc]`; tiếng Anh chỉ ở thuật ngữ đã định nghĩa (Topic, Tag, Upvote, Bookmark, Trending, vai trò) |

Đủ 27 mục của lượt P2.

## 3. Kết quả kiểm tra tự động

ERROR = 0, WARN = 0, INFO = 2. Lệnh đã chạy (từ gốc repo):

```
python3 .agent-instructions/system_analysis/shared/sr-tools/check_sr.py \
  --sr .agents/.claude/system_analysis/output/specs/ISH-SR-M05.md \
  --routing .agents/.claude/system_analysis/output/specs/routing/ISH-RT-M05.md \
  --tests .agents/.claude/system_analysis/output/specs/audit/work/tests-M05.md \
  --json .agents/.claude/system_analysis/output/specs/audit/work/check-P2-M05-r2.json
```

- INFO COV-99: không truyền `--inventory` (COV thuộc P1).
- INFO TST-00: 168 ca cho 107 yêu cầu.
- Không có mã ERROR/WARN nào. Script không bắt được các lỗi ở P2-01…P2-07 (đều là lỗi ngữ nghĩa hoặc hồ sơ).

## 4. Hồ sơ xác minh

Mọi trích đoạn ở mục 0 và mục 1 đã được kiểm bằng `grep -n -F "<đoạn>" <tệp>`; số dòng khớp với số ghi trong finding:

- `grep -n -F "Khi người dùng đã đăng nhập yêu cầu theo dõi một Topic chưa theo dõi" ISH-SR-M05.md` → 1 (dòng 308)
- `grep -n -F "Khi người dùng yêu cầu theo dõi một Topic đã bị loại khỏi danh mục Topic" ISH-SR-M05.md` → 1 (dòng 412)
- `grep -n -F "Hệ thống phải cho phép người dùng đã đăng nhập theo dõi một Topic." ISH-SR-M05.md` → 1 (dòng 298)
- `grep -n -F "Topic đã loại khỏi danh mục Topic (trạng thái cuối)" ISH-SR-M05.md` → 1 (dòng 126)
- `grep -n -F "it can no longer be selected, suggested, ranked in Trending or followed" decisions.md` → 1 (dòng 793; vòng 1 ghi dòng 790, register đã dời dòng)
- `grep -n -F "Hệ thống phải yêu cầu mỗi bài viết đã gửi có từ 1 đến 3 Topic" ISH-SR-M05.md` → 1 (dòng 162)
- `grep -n -F "Khi người dùng, kể cả Guest, xem một bài viết, hệ thống phải hiển thị các Topic" ISH-SR-M05.md` → 1 (dòng 180)
- `grep -n -F "Hệ thống phải cho phép tác giả lưu bản nháp của bài viết khi bài viết chưa có Topic nào." ISH-SR-M05.md` → 1 (dòng 181)
- `grep -n -F "Hệ thống phải gắn cho mỗi bài viết từ 0 đến 5 Tag tự do do tác giả nhập." ISH-SR-M05.md` → 1 (dòng 265)
- `grep -n -F "hệ thống phải hiển thị các Tag hoạt động của bài viết đó" ISH-SR-M05.md` → 1 (dòng 290)
- `grep -n -F "hệ thống phải chuyển mọi bài viết đang gắn Topic nguồn sang Topic đích." ISH-SR-M05.md` → 1 (dòng 396)
- `grep -n -F "hệ thống phải ghi đúng một phản hồi gợi ý Topic cho lần gửi đó" ISH-SR-M05.md` → 1 (dòng 257)
- `grep -n -F "Đề xuất mặc định: chỉ ghi ở lần gửi đầu tiên." ISH-SR-M05.md` → 1 (dòng 596)
- `grep -n -F "one record per submission" decisions.md` → 1 (dòng 841)
- `grep -n -F "Chỉ lần gợi ý gần nhất; một bản ghi mỗi lần gửi bài." qa-log.md` → 1 (dòng 1028)
- `grep -n -F "REJECTED: mod rejected, author can fix and resubmit" decisions.md` → 1 (dòng 198)
- `grep -n -F "Guest views are not counted" decisions.md` → 1 (dòng 845)
- `grep -n -F "Hệ thống phải không đếm lượt mở trang chi tiết bài viết của Guest vào số người xem." ISH-SR-M05.md` → 1 (dòng 345)
- `grep -n -F "| ISH-M05-006.16 | QA-011, DEC-051 | Nói thẳng |" ISH-SR-M05.md` → 1 (dòng 525)
- `grep -n -F "AI: Xem AI Summary + AI Classification trên post" qa-log.md` → 1 (dòng 137)
- `grep -n -F "Tag: user tự quyết định hoàn toàn, AI không can thiệp" qa-log.md` → 1 (dòng 209)
- `grep -n -F "Phase 5 (DEC-050/051) đã thu hẹp phạm vi AI classification chỉ còn Topic" qa-log.md` → 1 (dòng 1004)
- `grep -n -F "tag chip hidden from display" decisions.md` → 1 (dòng 303)
- `grep -n -F "it then shows again on the posts that carry it" decisions.md` → 1 (dòng 813)
- `grep -n -F "POST: Xem/đọc post" qa-log.md` → 1 (dòng 132)
- `grep -n -F "gồm 11 lĩnh vực tri thức chốt sẵn, không ai thêm hay xóa được" ISH-SR-M05.md` → 1 (dòng 91)
- `grep -n -F "từ upvote, bình luận, bookmark và người xem trong 7 ngày gần nhất" ISH-SR-M05.md` → 1 (dòng 95)
- `grep -n -F "ISH-M05-011.3, ISH-M05-011.4, ISH-M05-011.6, ISH-M05-011.7: P1" ISH-SR-M05.md` → 1 (dòng 117)
- `grep -n -F "Gộp Topic | ISH-M05-011 | Must | P0 | ISH-M05-011.3, ISH-M05-011.4: P1" snapshot-ISH-SR-M05-v0.1.md` → 1 (dòng 111)
- `grep -n -F "Topic là danh mục một tầng gồm các lĩnh vực tri thức cố định" snapshot-ISH-SR-M05-v0.1.md` → 1 (dòng 85)
- `grep -n -F "5.2 thêm trạng thái theo dõi" ISH-SR-M05.md` → 1 (dòng 458)
- `grep -n -F "Người dùng yêu cầu theo dõi, hoặc Mod/Admin yêu cầu gộp với Topic đó" ISH-SR-M05.md` → 1 (dòng 132)
- Mục 0: dòng 37, 38, 55, 129, 130, 140, 154, 209, 244, 423, 505, 521, 580, 581, 582 của `ISH-SR-M05.md`; dòng 797, 841 của `decisions.md` → mỗi trích đoạn 1 kết quả, đúng dòng.

Khẳng định vắng mặt:

- P2-01: `grep -n "danh mục Topic" ISH-SR-M05.md` trong khoảng dòng 298–313 (tính năng 5.9) → 0. 007.1 và 007 không có điều kiện "thuộc danh mục Topic".
- P2-03: `grep -n -i "lần gửi\|resubmit\|gửi lại" ISH-SR-M05.md decisions.md` → SR chỉ có dòng 257 (005.4) và 596 (OP-M05-10); decisions.md chỉ có dòng 198, 214 (DEC-031, DEC-034) và hai dòng thuộc M09, M11 không liên quan. Không có DEC nào nói riêng về phản hồi khi gửi lại.
- P2-04: không cần (trùng ý, không phải vắng mặt).
- P2-05: `grep -n -E "^\| ISH-M05-[0-9.]+ \| Hệ thống phải .* khi " ISH-SR-M05.md` → 8 dòng (181, 199, 289, 334–337, 347). Chỉ 181 có "khi" dẫn một trạng thái của đối tượng; 199 ("chỉ tạo … khi tác giả yêu cầu") là ràng buộc phổ quát, đã được vòng 1 chấp nhận; các dòng còn lại là ngữ cảnh "khi tính điểm/kiểm độ dài".
- P2-06: `grep -n "DEC-150\|DRAFT §3.2" ISH-SR-M05.md` trên dòng 525 → 0; `grep -n -i "tag" qa-log.md` trong QA-011 (dòng 126–140) → chỉ dòng 134 ("Xem danh sách Topic / Tag / Khối lớp", là danh sách, không phải hiển thị trên bài).
- P2-07: `sed -n 458p ISH-SR-M05.md | grep -o "mục 4\|Tổng quan chức năng\|.5\.1.\|Ngoại lệ"` → 4 khớp, đều là "005.1" (hai lần), "5.12", "5.13"; 0 khớp cho mục 4 hay mục 5.1.

Finding bị loại hoặc chỉnh:

- **Loại:** "ISH-M05-001.5 ghi `Nói thẳng` cho cả Guest/User, cùng dạng AUD-M05-11". Lý do loại: nguồn Topic viết "No delete." thành câu độc lập không có chủ ngữ Mod/Admin ("- Mod/admin: edit (rename) + merge. No delete.", `decisions.md:285`) và "Topic: edit+merge, no delete." (`qa-log.md:746`); cùng với "11 giá trị cố định" (`qa-log.md:1002`), nguồn đọc được là quy tắc chung cho mọi người. Khác với Tag, nơi DEC-051 viết rõ "mod/admin do NOT edit/merge/delete". Vòng 1 cũng không lập finding cho 010.4 có cùng nội dung.
- **Loại:** "Định nghĩa 2.1 chứa quy tắc hành vi" (ví dụ "Bài viết được tính … chỉ các bài viết này góp vào điểm Trending"). Lý do: câu nhắc lại đúng 008.3, không có mục checklist nào bị vi phạm có hệ quả; không lập.
- **Loại:** "006.16 trùng ý với 012.1". Lý do: 006.16 là quy tắc hiển thị thường xuyên, 012.1 là hệ quả của sự kiện vô hiệu hóa; hai câu bổ sung nhau, không câu nào chứa trọn câu kia.
- **Chỉnh:** P2-02 ban đầu gồm cả 011.6, 011.8…011.10; đã bỏ vì đó là hệ quả hoặc điều kiện của chính thao tác gộp (cùng loại với 011.2…011.5 đã được vòng 1 chấp nhận).
- **Chỉnh:** P2-03 chọn CL-F01 làm mã chính; mặt "SR đã tự chọn trước câu trả lời" (CL-F04) thuộc P3, ghi ở mục 6.

## 5. Phạm vi và giới hạn không kiểm được

- Lượt này không đọc `tests-M05.md` (chỉ dùng số đếm TST-00 của script) và không đọc `disposition-M05.md`, theo đúng mốc của P2. `selfcheck-M05.md` chỉ được mở sau khi chấm xong (mục 7).
- Không kiểm độ phủ nguồn, routing và ranh giới module (P1), ca kiểm và mơ hồ của nguồn (P3).
- Các SR của module khác (M03, M07, M13, M14) chưa có, nên CL-D06 chỉ kiểm được việc SR không dẫn ID của module khác.
- "Đúng một cách đọc" của DEC-157 về lần gửi lại (P2-03) không suy được từ register; báo cáo chỉ nêu hai khả năng.

## 6. Chuyển lượt khác

- P3 (CL-A11/CL-B08): 2.1 "Thứ tự bảng chữ cái tiếng Việt" (`ISH-SR-M05.md:62`) liệt kê đúng 29 chữ; nguồn DEC-154 viết "(a ă â b c d đ e ê …)" (`decisions.md:829`). Tên Tag tự do có thể chứa f, j, w, z, chữ số, ký tự đặc biệt và dấu thanh (ví dụ "#java" và "#hoa"; "Hóa" và "Hoa") mà định nghĩa không xếp chỗ, nên phá hòa ở 008.12 có thể không xác định duy nhất.
- P3 (CL-F04): ISH-M05-005.4 đã chọn "mỗi lần gửi một phản hồi" trong khi OP-M05-10 còn mở (cùng sự việc với P2-03).
- P3 (CL-B13): đổi tên một Topic đã bị loại khỏi danh mục (ISH-M05-010) — DEC-159 chỉ nói về gộp; nguồn im lặng về đổi tên Topic nguồn sau gộp.
- P1 (CL-E02/CL-A10): 002.10 và 006.16 (hiển thị Topic/Tag trên trang bài viết) có OP-M05-12 về chủ sở hữu M05 hay M03; P1 kiểm có hàng R5 tương ứng hay không.
- P1 (CL-E03, hình thức): routing R2 ghi "ISH-M05-004.2…4.4" (`ISH-RT-M05.md:29`), ID cuối viết tắt.

## 7. Ghi chú về selfcheck (P2.3, mở sau khi chấm)

`selfcheck-M05.md` (phiên bản 0.2) ghi `Đạt` cho các mục lượt này chấm `Không đạt`:

- CL-A05 (`selfcheck-M05.md:16`): ghi đã "mở lại nguồn mọi dòng mới", gồm 006.16 — xem P2-06.
- CL-B01 (`:23`): "EARS-01…03 không báo" — xem P2-05.
- CL-C01 (`:36`): không nhắc cặp 007.1/011.7 — xem P2-01.
- CL-C02 (`:37`): còn dẫn ID đã bỏ "002.4" — xem P2-04.
- CL-C04 (`:39`): không nhắc 002.10, 002.11, 006.16, 011.7 — xem P2-02.
- CL-F01 (`:51`): ghi "9 OP" trong khi Phụ lục B có 11 OP (01, 02, 04…12) — xem P2-03.
- CL-F02 (`:52`): "Dòng 0.2 liệt kê ID thêm, sửa, bỏ" — không gồm mục 4, 5.1 — xem P2-07.
