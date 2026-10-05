# Tệp lượt — ISH-AUD-M05-r2 · lượt P3 (Ca kiểm độc lập, mơ hồ và hành vi còn thiếu)
<!-- [Vietnamese Doc] -->

| Trường | Giá trị |
|---|---|
| Module | M05 — Topic & Tag |
| Vòng | 2 |
| Lượt | P3 |
| SR được audit | ISH-SR-M05, phiên bản 0.2 (2026-10-05), trạng thái Bản nháp |
| Routing | ISH-RT-M05, phiên bản 0.2 (2026-10-05) |
| Tóm tắt Author đã nhận và không dùng | Không có. Người gọi chỉ đưa mã module, vòng, lượt, gốc repo và đường dẫn báo cáo vòng 1 |
| Tệp đi kèm | `audit-tests-M05-r2.md` (119 ca, bảng quét khung hành vi phần đổi), `audit-inventory-P3-M05-r2.md/.json`, `check-P3-M05-r2.json` |

Thứ tự đã làm: C0 (đọc RULES, ví dụ, báo cáo `ISH-AUD-M05-r1.md`) → P3.1 inventory vòng 2 và đọc nguyên văn các mục OWNED mới (DEC-154…159, ISS-228…236, QA-288…296), các mục Phase 5 của M05, DRAFT §3, §4.5, §7.2, §11.2, §11.5, cùng các nguồn liên quan (DEC-031…034, DEC-065, DEC-099, DEC-124…126, DEC-132, QA-201, QA-235) → P3.2/P3.2b ghi ca mới/đổi và các ô quét đổi vào `audit-tests-M05-r2.md` **trước khi** mở SR/routing v0.2 → P3.3 mở SR, routing → P3.4 chạy `check_sr.py --tests`, mở `selfcheck-M05.md` (bảng quét, các mục của lượt) và `tests-M05.md` → P3.5/P3.6 phân loại, chấm. Không mở `disposition-M05.md`, `inventory-M05.*` và không mở tệp của P1, P2 vòng 2. Giới hạn về tính độc lập: báo cáo vòng 1 (bắt buộc đọc ở C0) có trích đoạn của SR v0.1, nên trước P3.3 tôi đã biết lời văn v0.1 ở các chỗ có finding.

## 1. Phát hiện nháp

Tóm tắt: 2 finding, cả hai là GAP mức Trung bình. Không có DEFECT.

### P3-01 — Thứ tự bảng chữ cái tiếng Việt khi phá hòa chưa nói chữ số, ký tự ngoài chữ cái và dấu thanh đứng ở đâu

| Lớp | GAP | Mức đề xuất | Trung bình | Checklist | CL-A11, CL-B13 |
|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.12 (`ISH-SR-M05.md:342`); ISH-M05-008.11 (`:341`); 2.1 "Thứ tự bảng chữ cái tiếng Việt" (`:62`).
- **Bằng chứng trong SR:**
  - "| Thứ tự bảng chữ cái tiếng Việt | Thứ tự chữ cái a ă â b c d đ e ê g h i k l m n o ô ơ p q r s t u ư v x y, không phân biệt chữ hoa, chữ thường. |" (`ISH-SR-M05.md:62`)
  - "rồi đến tên theo thứ tự bảng chữ cái tiếng Việt" (`ISH-SR-M05.md:342`)
  - "Tên Tag được chứa những ký tự nào ngoài chữ và số" (`ISH-SR-M05.md:595`, OP-M05-09; đề xuất mặc định của Author cho phép mọi ký tự trừ ký tự trắng và dấu #, nên tên Tag có chữ số).
- **Bằng chứng trong nguồn:**
  - "(3) The name tie-break uses Vietnamese alphabetical order (a ă â b c d đ e ê …), case-insensitive." (`registers/decisions.md:829`, DEC-154)
  - "Theo bảng chữ cái tiếng Việt (a ă â b c d đ e ê …), không phân biệt chữ hoa–thường" (`registers/qa-log.md:1027`, QA-292)
- **Vấn đề:** Câu trả lời của stakeholder (DEC-154) đã đóng câu hỏi AUD-M05-15 của vòng 1 cho chữ cái. Câu trả lời đó vẫn chưa nói ba điều, và mỗi điều cho thứ hạng khác nhau mà người dùng nhìn thấy được:
  - Chữ số và ký tự ngoài chữ cái. Ca A-109: Tag "2k8" và "anh" cùng 1 điểm và cùng 1 bài mới. Nếu chữ số đứng trước chữ cái thì "2k8" xếp trước; nếu đứng sau thì "anh" xếp trước.
  - Dấu thanh. Ca A-110: "nghỉhè" và "nghĩhè" chỉ khác nhau ở dấu hỏi và dấu ngã. Có từ điển xếp hỏi trước ngã, có từ điển xếp ngã trước hỏi.
  - Hai Tag bằng nhau cả về điểm lẫn số bài mới là chuyện thường gặp. Ví dụ, mọi Tag chỉ có một bài mới và không có tương tác đều có 1 điểm. Vì vậy tiêu chí thứ ba quyết định thứ tự của nhiều Tag. Nếu M14 chỉ hiện N mục đầu, nó còn quyết định Tag nào được hiện.
  - Với 11 Topic thì không có cặp nào lộ ra khác biệt (tôi đã so từng cặp có chữ cái đầu chung). Chỗ mơ hồ chỉ nằm ở Tag.
  - SR chép phần chữ cái và cũng không nêu ba điểm trên.
  - Ca của Author (T-158 ở `tests-M05.md:167`, T-159 ở `:168`) chỉ dùng tên khác nhau ở chữ cái, nên không lộ chỗ mơ hồ này.
  - Selfcheck ghi ô này là `c→hỏi` (ISS-232) (`selfcheck-M05.md:160`), không nhắc phần còn lại.
  - Không có ISS/QA/DEC hay `OP` nào về điểm này (xem mục 4).
- **Lý do mức:** CL-A11 mặc định Cao khi mơ hồ nằm ở công thức hoặc số liệu. Hạ một mức vì đây là tiêu chí phá hòa thứ ba, chỉ áp dụng cho Tag, và phần chính của quy tắc đã xác định.
- **Hệ quả nếu không sửa:** Hai cách cài đặt cho hai thứ tự khác nhau trên bảng Trending Tag. Ca kiểm chấp nhận của 008.12 không có một "Then" duy nhất khi tên Tag có chữ số, ký tự đặc biệt hoặc chỉ khác nhau ở dấu thanh.
- **Hướng xử lý (Author quyết cách viết):** Hỏi stakeholder theo khuôn dưới, ghi register, rồi bổ sung định nghĩa ở 2.1 và thêm ca kiểm có chữ số và dấu thanh. Nếu chưa hỏi ngay thì ghi một `OP` ở Phụ lục B. Có thể hỏi chung với OP-M05-09, vì tập ký tự được phép quyết định phạm vi của câu hỏi này.
- **Khuôn hỏi stakeholder:**
  - Vấn đề: Khi phá hòa bằng tên theo bảng chữ cái tiếng Việt, chữ số, ký tự ngoài chữ cái và dấu thanh được xếp thế nào?
  - Nguồn: DEC-154 (`decisions.md:829`): "Vietnamese alphabetical order (a ă â b c d đ e ê …), case-insensitive".
  - Lựa chọn:
    - A) Chữ số 0–9 và ký tự khác đứng trước chữ cái. So chữ cái trước; nếu chữ cái giống nhau thì so dấu thanh theo thứ tự ngang, huyền, hỏi, ngã, sắc, nặng. Hệ quả: "2k8" xếp trước "anh"; "nghỉhè" xếp trước "nghĩhè". Đây là quy ước phổ biến nên dễ cài đặt.
    - B) Chữ số và ký tự khác đứng sau chữ cái, dấu thanh như A. Hệ quả: Tag chữ cái lên trước; "2k8" xếp sau "ỹ…".
    - C) Bỏ qua chữ số và ký tự khác khi so. Hệ quả: một số tên bị coi là bằng nhau, và cần thêm một tiêu chí phá hòa thứ tư.
  - Đề xuất: A, vì đây là cách sắp xếp quen thuộc và cho thứ tự xác định với mọi tên.

### P3-02 — Tag chưa có bài viết nào được tính (chỉ nằm trên bản nháp, trong Group Private hoặc trên bài chưa công khai) có vào xếp hạng Trending Tag không

| Lớp | GAP | Mức đề xuất | Trung bình | Checklist | CL-A11, CL-B13 | Nhãn | Hồi quy (ISH-M05-008.19 là yêu cầu mới của v0.2) |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-M05-008.19 (`ISH-SR-M05.md:349`); ISH-M05-006.2 (`:276`).
- **Bằng chứng trong SR:**
  - "Hệ thống phải đưa mọi Tag hoạt động vào xếp hạng Trending mà không đặt ngưỡng điểm tối thiểu." (`ISH-SR-M05.md:349`)
  - "Khi tác giả gắn một tên Tag chưa tồn tại cho bài viết, hệ thống phải tạo Tag mới với tên đó mà không cần phê duyệt." (`ISH-SR-M05.md:276`). Câu này không giới hạn thời điểm, nên tính cả lúc gắn Tag trên bản nháp.
- **Bằng chứng trong nguồn:**
  - "Không đặt ngưỡng cho MS1 — dataset demo nhỏ (~70 bài, 30 user), đặt ngưỡng dễ khiến Trending trống/gần trống lúc demo." (`registers/qa-log.md:939`, QA-235). Câu hỏi là "min upvote/comment".
  - "- Auto-created, no approval" (`registers/decisions.md:300`, DEC-051). Nguồn không nói Tag được tạo vào thời điểm nào.
  - "and not in a Private group count" (`registers/decisions.md:797`, DEC-146)
  - "Guest (unauthenticated) can view Newest and the full Trending tab (all 3 sub-views) without restriction" (`registers/decisions.md:700`, DEC-126)
- **Vấn đề:** QA-235 bỏ ngưỡng tối thiểu về upvote và bình luận để bảng Trending không trống. Nguồn không nói gì về Tag chưa có bài viết nào được tính. Có hai cách đọc hợp lý, cho hai kết quả quan sát được khác nhau (ca A-119). Ví dụ Tag "đềthi12a1" mới được tạo, chỉ gắn trên hai bài trong một Group Private, hoặc chỉ trên một bản nháp chưa gửi:
  - Cách 1, cách SR v0.2 đang chọn ("mọi Tag hoạt động"): Tag có mặt trong bảng xếp hạng với 0 điểm, và Guest xem được.
  - Cách 2 (chỉ Tag có ít nhất một bài viết được tính): Tag không có mặt.
  - Theo cách 1, tên Tag dùng trong Group Private hoặc trong bản nháp sẽ hiện công khai, trái với tinh thần của DEC-146 (không tính bài trong Group Private).
  - Ca của Author T-153 (`tests-M05.md:162`) cho "anova" 0 điểm vào bảng nhưng không nêu Tag đó có bài nào được tính hay không.
  - Bảng quét của Author ghi 5.10, câu 5, loại `a`, chỉ nhắc Tag bị vô hiệu hóa và Topic nguồn (`selfcheck-M05.md:117`).
  - Không có ISS/QA/DEC hay `OP` nào về điểm này (xem mục 4).
  - Với Topic thì không có vấn đề này: 11 Topic là danh mục công khai.
- **Lý do mức:** CL-A11 mặc định Cao khi mơ hồ liên quan phạm vi dữ liệu. Hạ một mức vì chỉ lộ tên Tag ở 0 điểm, không lộ nội dung bài, và số mục hiển thị do M14 quyết.
- **Hệ quả nếu không sửa:** Tên Tag từ nội dung riêng tư hoặc chưa đăng có thể xuất hiện trên bảng Trending Tag công khai. Nếu Author không viết theo cách 1 thì người cài đặt phải tự chọn cách đọc.
- **Hướng xử lý (Author quyết cách viết):** Hỏi stakeholder theo khuôn dưới, ghi register, sửa 008.19 theo câu trả lời và thêm ca kiểm cho Tag chỉ có trên bài Group Private hoặc bản nháp. Nếu chưa hỏi ngay thì ghi `OP` ở Phụ lục B, kèm ghi chú rằng 008.19 đang ở dạng chưa chốt.
- **Khuôn hỏi stakeholder:**
  - Vấn đề: Tag chưa có bài viết nào được tính (chỉ nằm trên bản nháp, trong Group Private hoặc trên bài chưa công khai) có xuất hiện trong bảng xếp hạng Trending Tag không?
  - Nguồn: QA-235 (`qa-log.md:939`) "Không đặt ngưỡng cho MS1"; DEC-051 (`decisions.md:300`) "Auto-created, no approval"; DEC-146 (`decisions.md:797`) không tính bài trong Group Private.
  - Lựa chọn:
    - A) Chỉ xếp hạng Tag có ít nhất một bài viết được tính, kể cả khi điểm là 0. Hệ quả: không lộ tên Tag từ bản nháp hay Group Private; vẫn không đặt ngưỡng điểm, đúng QA-235.
    - B) Xếp hạng mọi Tag hoạt động (như SR v0.2). Hệ quả: tên Tag trong bản nháp và Group Private hiện công khai với 0 điểm.
    - C) Chỉ tạo Tag khi bài viết trở thành công khai. Hệ quả: đổi cả thời điểm Tag xuất hiện trong gợi ý tự hoàn thành (M06) và trong việc kiểm giới hạn Tag.
  - Đề xuất: A, vì giữ đúng ý "không ngưỡng" mà không làm lộ nội dung không công khai, và không đổi hành vi tạo Tag.

## 2. Kết quả checklist của lượt

| Mã | Kết quả | Finding / ghi chú |
|---|---|---|
| CL-A11 | Không đạt | P3-01, P3-02. Bốn mơ hồ của vòng 1 đã được stakeholder trả lời và SR làm theo đúng câu trả lời: AUD-01 (DEC-154 (1) → 2.1 `:39`, 008.1 `:331`), AUD-14 (DEC-154 (2) → 008.17 `:347`), AUD-15 (DEC-154 (3) → 2.1 `:62`), AUD-16 (DEC-156 → 002.11 `:181`) |
| CL-B08 | Đạt | Có ca cho mọi yêu cầu có ID mới hoặc đổi (A-099…A-119 và các ca viết lại). Mọi ca có nguồn xác định đều có SR xác định; chỉ còn `Mơ hồ` ở A-109, A-110, nơi chính nguồn mơ hồ (GAP P3-01, không phải DEFECT). Định nghĩa "Bài viết công khai" (`:37`) nay cho kết quả đúng nguồn ở A-091, A-092 (AUD-06 đã sửa). Ví dụ tính tay A-068 (22,5) và A-102 (0,3) ra cùng kết quả khi tính theo nguồn và theo SR. Quan hệ 007.1/011.7 đã chuyển P2 |
| CL-B09 | Đạt | Mọi giới hạn có yêu cầu từ chối: 1–3 Topic (002.5, 002.6, 002.8); 0–5 Tag (006.5); 30 ký tự (006.7); khoảng trắng (006.8); 10 tiếng (003.6); 10 yêu cầu/phút (003.9); theo dõi Topic đã gộp (011.7, `:412`); gộp với Topic đã bị loại hoặc gộp vào chính nó (011.8, 011.10); các thao tác chỉ dành cho một vai trò (009.2, 010.3, 011.5, 012.7…012.11). Nhánh vi phạm của AUD-03 đã có |
| CL-B12 | Đạt | `check_sr.py --tests`: 168 ca cho 107 yêu cầu, không có TST-01…05. Đã có ca thao tác không hợp lệ cho bảng 5.2: T-136, T-137, T-161…T-168 (`tests-M05.md:145`, `:146`, `:170`–`:177`) (AUD-13 đã sửa). Cột "Giả định cần thêm" đều là `—`. Ca công thức có ví dụ số với thực thể ngoài lề (T-145 là bài cũ chỉ có người xem; T-084 là Topic không có bài). Ca thời gian có thực thể cũ có hoạt động mới (T-082 P2, T-147) và thực thể mới chưa có hoạt động (T-083). Thiếu ca chữ số/dấu thanh ở 008.12 là hệ quả của mơ hồ nguồn, đã nằm ở P3-01 |
| CL-B13 | Không đạt | P3-01, P3-02 (nguồn im lặng, hệ quả quan sát được khác nhau, chưa hỏi, chưa có `OP`). Các điểm (a)/(b) của nguồn mới đều đã thành yêu cầu hoặc nằm ở routing: DEC-154 → 008.1, 008.2, 008.11, 008.12, 008.17; DEC-155 → R5 M07 (`ISH-RT-M05.md:69`); DEC-156 → 002.5, 002.6, 002.11; DEC-157 → 005.1, 005.4; DEC-158 → 008.13…008.16, R1 (`:20`), R5 M03, M14 (`:66`, `:75`); DEC-159 → 011.8…011.10, R3 (`:42`). Hệ quả của gộp Topic (AUD-03) đã có ở 011.6, 011.7 |
| CL-F04 | Đạt | Không thấy chỗ SR hoặc ca kiểm chọn ngầm một phương án mà nguồn chưa chọn. T-011 nay khớp DEC-156 (`tests-M05.md:20`), nên lớp phụ CL-F04 của AUD-16 đã xử lý. Mọi "Giả định cần thêm" là `—`; các điểm (c) khác đều có `OP` (OP-M05-02, 04…12). 008.19 đọc QA-235 theo nghĩa đen; tôi ghi chỗ này là GAP (P3-02), không phải quyết định ngầm |

## 3. Kết quả kiểm tra tự động

Lệnh (từ gốc repo): `python .agent-instructions/system_analysis/shared/sr-tools/check_sr.py --sr .agents/.claude/system_analysis/output/specs/ISH-SR-M05.md --routing .agents/.claude/system_analysis/output/specs/routing/ISH-RT-M05.md --tests .agents/.claude/system_analysis/output/specs/audit/work/tests-M05.md --json .agents/.claude/system_analysis/output/specs/audit/work/check-P3-M05-r2.json`

**ERROR = 0, WARN = 0, INFO = 2** (COV-99: không truyền `--inventory`; TST-00: 168 ca cho 107 yêu cầu). Có 12 yêu cầu cấp trên và 107 yêu cầu cấp dưới. Không có mã ERROR/WARN nào.

Inventory: `python …/inventory.py --registers … --draft docs/_temp --module M05 --keywords "topic,tag,trending,gộp,merge,flat,chủ đề,thẻ,gợi ý,suggest,is_stale,follow,theo dõi,lớp,khối,grade,phân loại,classification" --out WORK/audit-inventory-P3-M05-r2.md --json WORK/audit-inventory-P3-M05-r2.json`. Kết quả: OWNED 100, REFERENCING 21, CROSS 40, DRAFT 34. **Chênh so với vòng 1:** thêm 24 mục OWNED (DEC-154…159, ISS-228…236, QA-288…296); REFERENCING thêm DEC-065 (nhắc DEC-155); các DEC-140…153 dời dòng (+2/+3) do có thêm dòng `[Amended]`.

## 4. Hồ sơ xác minh

**Trích đoạn (mỗi đoạn đã chạy `grep -n -F`, số dòng khớp):**

- `grep -n -F "(3) The name tie-break uses Vietnamese alphabetical order (a ă â b c d đ e ê …), case-insensitive." registers/decisions.md` → 1 (dòng 829)
- `grep -n -F "Theo bảng chữ cái tiếng Việt (a ă â b c d đ e ê …), không phân biệt chữ hoa–thường" registers/qa-log.md` → 1 (dòng 1027)
- `grep -n -F "| Thứ tự bảng chữ cái tiếng Việt | Thứ tự chữ cái a ă â b c d đ e ê g h i k l m n o ô ơ p q r s t u ư v x y, không phân biệt chữ hoa, chữ thường. |" ISH-SR-M05.md` → 1 (dòng 62)
- `grep -n -F "rồi đến tên theo thứ tự bảng chữ cái tiếng Việt" ISH-SR-M05.md` → 2 (dòng 341, 342)
- `grep -n -F "Tên Tag được chứa những ký tự nào ngoài chữ và số" ISH-SR-M05.md` → 1 (dòng 595)
- `grep -n -F "Không đặt ngưỡng cho MS1 — dataset demo nhỏ" registers/qa-log.md` → 1 (dòng 939)
- `grep -n -F -- "- Auto-created, no approval" registers/decisions.md` → 1 (dòng 300)
- `grep -n -F "and not in a Private group count" registers/decisions.md` → 1 (dòng 797)
- `grep -n -F "Guest (unauthenticated) can view Newest and the full Trending tab (all 3 sub-views)" registers/decisions.md` → 1 (dòng 700)
- `grep -n -F "Hệ thống phải đưa mọi Tag hoạt động vào xếp hạng Trending mà không đặt ngưỡng điểm tối thiểu." ISH-SR-M05.md` → 1 (dòng 349)
- `grep -n -F "Khi tác giả gắn một tên Tag chưa tồn tại cho bài viết, hệ thống phải tạo Tag mới với tên đó mà không cần phê duyệt." ISH-SR-M05.md` → 1 (dòng 276)
- `grep -n -F "| 5.10 Trending | 5 Hệ quả lên đối tượng liên quan | a |" selfcheck-M05.md` → 1 (dòng 117); `"| 5.10 Trending (v0.2) | 3 Kết quả chính | c→hỏi |"` → 1 (dòng 160)
- `grep -n -F "| T-153 |" tests-M05.md` → dòng 162; `"| T-158 |"` → dòng 167; `"| T-159 |"` → dòng 168

**Khẳng định vắng mặt:**

- P3-01, tìm trong SR (gồm cả Phụ lục B) và routing: `chữ số` → 0/0; `dấu thanh` → 0/0; `0–9` → 0/0; `ký tự khác chữ` → 0/0. `thứ tự` trong Phụ lục B (dòng 584–598) → 0. Trong register: `digit|chữ số|numeric` → chỉ có DEC-093 dòng 93 và QA dòng 590 (username, không liên quan). Không có ISS/QA/DEC nào sau QA-292 về chữ số hay dấu thanh.
- P3-02, tìm trong SR và routing: `ít nhất một bài` → 0/0; `chỉ gắn trên` → 0/0; `Tag mới được tạo` → 0/0; `bài viết được tính gắn Tag` → 1/0 (chỉ ở 008.2 dòng 332, không ở 008.19). `Group Private` trong SR → dòng 38, 40, 333 (không có dòng nào về xếp hạng Tag). Trong register, tìm `tag` cùng `private|draft|nháp|riêng tư` → không có quy tắc nào về Tag của bài không công khai trong Trending.

**Kiểm từng finding vòng 1 thuộc lượt P3:**

| AUD (nháp vòng 1) | Mục | Trạng thái | Bằng chứng mới |
|---|---|---|---|
| AUD-M05-01 (P3-01) | CL-A11 | Đã sửa (stakeholder trả lời: ISS-228, DEC-154) | "| Trở thành công khai lần đầu | Thời điểm bài viết lần đầu trở thành bài viết công khai. |" (`ISH-SR-M05.md:39`); "trở thành công khai lần đầu trong 7 ngày gần nhất" (`:331`, `:332`, `:341`, `:342`); A-073 và T-154 trùng nhau |
| AUD-M05-03 (phần P3-05: CL-B13, CL-B09) | CL-B13, CL-B09 | Đã sửa | "hệ thống phải loại Topic nguồn khỏi xếp hạng Trending." (`:411`); "Khi người dùng yêu cầu theo dõi một Topic đã bị loại khỏi danh mục Topic, hệ thống phải từ chối yêu cầu đó." (`:412`); "Hệ thống phải đưa mọi Topic trong danh mục Topic vào xếp hạng Trending" (`:348`) |
| AUD-M05-06 (phần P3-04: CL-B08) | CL-B08 | Đã sửa | "đang ở trạng thái kiểm duyệt bình thường (không bị gắn cờ chờ xử lý, không bị Mod ẩn)" (`:37`); A-091 và A-092 ra 0, trùng T-156 và T-157 |
| AUD-M05-13 (P3-07) | CL-B12 | Đã sửa | `tests-M05.md:171` "| T-162 | ISH-M05-011.8 | Vi phạm |", `:175` "| T-166 | ISH-M05-012.1 | Vi phạm |", `:177` "| T-168 | ISH-M05-007.2 | Vi phạm |". Câu hỏi lộ ra đã được hỏi: "If the source or the target has already been removed from the catalog (by an earlier merge), the merge is rejected" (`decisions.md:849`, DEC-159) |
| AUD-M05-14 (P3-02) | CL-A11 | Đã sửa (ISS-231, DEC-154) | "Hệ thống phải không đếm bình luận đang bị ẩn bởi kiểm duyệt khi tính điểm Trending." (`:347`); A-074 trùng T-150, T-151 |
| AUD-M05-15 (P3-03) | CL-A11 | Đã sửa (ISS-232, DEC-154) | 2.1 dòng 62 (trích ở trên); A-077 trùng T-158. Phần câu trả lời còn để ngỏ (chữ số, dấu thanh) là finding mới P3-01, dựa trên nguồn mới DEC-154 |
| AUD-M05-16 (P3-06) | CL-A11, CL-F04, CL-B13 | Đã sửa (ISS-230, DEC-156) | "Hệ thống phải cho phép tác giả lưu bản nháp của bài viết khi bài viết chưa có Topic nào." (`:181`); "Khi người dùng lưu một thay đổi làm một bài viết đã gửi không còn Topic nào" (`:176`); "| T-011 | ISH-M05-002.5 | Vi phạm | Bài viết nháp của User A có 0 Topic |" (`tests-M05.md:20`), khớp DEC-156 |

**Tìm hồi quy (vòng 2, bước 3):** `diff` các dòng yêu cầu giữa `snapshot-ISH-SR-M05-v0.1.md` và v0.2 khớp với dòng Lịch sử 0.2 (`ISH-SR-M05.md:458`): thêm 17 ID, đổi 13 ID, bỏ 2 ID (002.4, 010.4). Bản v0.2 hiện tại trùng `snapshot-ISH-SR-M05-v0.2.md` và `snapshot-ISH-RT-M05-v0.2.md` (`diff -q` không báo khác). Mọi ID mới hoặc đổi đều có ca của tôi (xem đầu `audit-tests-M05-r2.md`), và các yêu cầu tham chiếu chúng (2.1, 5.2, Phụ lục A) đã được đọc lại. Hồi quy trong phạm vi lượt P3: chỉ có P3-02 (008.19 mới). Các điểm thuộc nhóm C, D chuyển P2 ở mục 6.

**Finding cân nhắc rồi loại:**

- Bình luận của chính tác giả được đếm trong khi người xem và bookmark của tác giả bị loại: loại, vì nguồn xác định ("all root comments and replies", `decisions.md:797`); hai cách đọc không cùng hợp lý.
- Upvote của tác giả: loại, vì không thể phát sinh (QA-201 cấm tự vote, `decisions.md:675`).
- Vô hiệu hóa Tag đang bị vô hiệu hóa, mở lại Tag đang hoạt động (T-166, T-167): loại, vì từ chối hay bỏ qua đều cho cùng trạng thái quan sát được.
- Gửi lại sau khi bị từ chối có ghi thêm phản hồi không (A-060): không lập finding vì đã có OP-M05-10. Chỗ OP này có thể đã được QA-293 trả lời đã chuyển P2.
- Thứ tự tên Topic: loại khỏi P3-01, vì 11 tên hiện có không có cặp nào lộ khác biệt giữa các cách đọc.

## 5. Phạm vi và giới hạn không kiểm được

- Ý định của stakeholder ở P3-01 và P3-02 không suy ra được; tôi chỉ nêu lựa chọn.
- Bảng Trending của M14 hiển thị bao nhiêu mục (để biết Tag 0 điểm có thực sự hiện ra không) chưa có SR M14 để đối chiếu.
- Mục KEYWORD (98) không đọc lại hết ở vòng 2. Chỉ đọc các mục liên quan đến hành vi đang dựng ca (QA-201, QA-235, DEC-124, DEC-126). Phân loại KEYWORD thuộc P1.
- Ca A-001…A-098 không đổi nguồn được giữ từ vòng 1 (dựng từ nguồn trước khi mở SR v0.1). Ở vòng 2 tôi chỉ kiểm lại rằng ID yêu cầu còn tồn tại và nguồn không có mục mới làm rõ. Không dựng lại từng ca từ đầu.
- Như đã nói ở đầu tệp, khi dựng ca vòng 2 tôi đã biết lời văn SR v0.1 ở các chỗ có finding, qua báo cáo vòng 1.
- Chu kỳ tính lại và cách lưu lượt xem (R1, R2) không kiểm.

## 6. Chuyển lượt khác

- P2 (CL-C01): ISH-M05-007.1 (`ISH-SR-M05.md:308`) cho theo dõi "một Topic chưa theo dõi" mà không giới hạn trong danh mục Topic; ISH-M05-011.7 (`:412`) từ chối theo dõi Topic đã bị loại. Với Topic nguồn chưa theo dõi, hai câu cho hai kết quả nếu không áp dụng quy tắc "riêng thắng chung". P2 nên xét có cần giới hạn phạm vi của 007.1 không.
- P2 (CL-F01): OP-M05-10 (`ISH-SR-M05.md:596`, mặc định "chỉ ghi ở lần gửi đầu tiên") có thể đã được QA-293 trả lời ("một bản ghi mỗi lần gửi bài", `qa-log.md:1028`), và mặc định của OP trái với ISH-M05-005.4 (`:257`, ghi một phản hồi "cho lần gửi đó").
