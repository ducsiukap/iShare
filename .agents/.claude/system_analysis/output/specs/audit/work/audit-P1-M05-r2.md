# Tệp lượt — ISH-AUD-M05-r2 · lượt P1 (Độ phủ nguồn và ranh giới module)
<!-- [Vietnamese Doc] -->

| Trường | Giá trị |
|---|---|
| Module | M05 — Topic & Tag |
| Vòng | 2 |
| Lượt | P1 |
| SR được audit | ISH-SR-M05, phiên bản 0.2 (2026-10-05, Bản nháp) — trùng `snapshot-ISH-SR-M05-v0.2.md` |
| Routing | ISH-RT-M05, phiên bản 0.2 (2026-10-05) — trùng `snapshot-ISH-RT-M05-v0.2.md` |
| Báo cáo vòng trước | `specs/audit/ISH-AUD-M05-r1.md` (SR 0.1, kết luận Chưa đạt) |
| Tóm tắt Author đã nhận và không dùng | Không có (người gọi chỉ đưa mã module, vòng, lượt, gốc repo và đường dẫn báo cáo vòng 1) |
| Ma trận | `work/coverage-M05-r2.md` (phần A lập trước khi đọc thân SR/routing; phần B sau) |
| Inventory của lượt | `work/audit-inventory-P1-M05-r2.md/.json` |

**Phạm vi chạy lại ma trận (vòng 2, bước 4).** Đếm theo ID yêu cầu, so `snapshot-ISH-SR-M05-v0.1.md` với bản 0.2: thêm 17, bỏ 2 (ISH-M05-002.4, ISH-M05-010.4), đổi nội dung 13 → 32 trên 119 yêu cầu của bản mới (26,9 %, dưới một phần ba); không thêm yêu cầu cấp trên (vẫn 12). Nhưng tập OWNED đổi (76 → 100, thêm DEC-154…159, ISS-228…236, QA-288…296) nên thỏa điều kiện (c): **chạy lại toàn bộ ma trận** (P1.2, P1.4).

**Chênh inventory so với vòng 1.** OWNED 76 → 100 (+24 mục trên). REFERENCING 20 → 21 (DEC-065 nay nhắc DEC-155). Từ khóa của lượt này: `topic, tag, trending, chủ đề, thẻ, gợi ý, suggest, follow, theo dõi, phân loại, classification, merge, gộp, hashtag, category, chuyên mục, stale, khối lớp, grade` (tự chọn từ tên module, dòng module-registry L12, DRAFT §3, §4.5, §7.2, §11.2; không lấy từ tệp của Author) → KEYWORD 100, CROSS 42, DRAFT 30.

## 1. Phát hiện nháp

### P1-01 — Disposition vẫn gộp các mục KEYWORD/CROSS-CUTTING không liên quan vào một câu, và còn lý do cũ trái với SR/routing (AUD-M05-17 sửa chưa đủ)

| Lớp | DEFECT | Mức đề xuất | Thấp | Checklist | CL-A03 |
|---|---|---|---|---|---|

- **Vị trí:** `work/disposition-M05.md:69`, `:73`, `:80`, `:94`, `:54`; `work/selfcheck-M05.md:14`.
- **Bằng chứng trong tệp của Author:**
  - "các mục KEYWORD còn lại khớp từ khóa chung "follow/lớp/gộp/category/dropdown" trong ngữ cảnh module khác — không liên quan" (`disposition-M05.md:69`)
  - "## KEYWORD hits trong register (108 muc)" (`inventory-M05.md:155`) — inventory của chính Author. Đối chiếu bằng script với SR, routing và disposition: 26 mục KEYWORD không có ở đâu cả: DEC-015, DEC-020, DEC-025, DEC-067, DEC-104, ISS-059, ISS-099, ISS-161, ISS-162, ISS-164, ISS-179, QA-047, QA-067, QA-069, QA-128, QA-192, QA-219, QA-220, QA-222, QA-230, QA-239, QA-242, ISS-192, QA-251, QA-256, QA-258. Ví dụ: "- QA-230 (qa-log.md:934, Phase 5 — M14: Feed & Disco…) [tu khoa: follow] ISS-188: Tab Group hiện/ẩn theo điều kiện nào?" (`inventory-M05.md:241`); "- DEC-025 (decisions.md:167, Phase 5 — M02: User Profile) [tu khoa: follow] Followers / Following display" (`inventory-M05.md:161`).
  - CROSS-CUTTING: chỉ các DEC có dòng ("| DEC-128, DEC-129, DEC-130, DEC-131, DEC-134–138, OPEN-001…005, OPEN-007 | Cross-cutting khác | không liên quan |", `disposition-M05.md:130`); 24 bản ISS/QA tương ứng (ISS-189, ISS-191, ISS-193, ISS-196…204, ISS-206, QA-248, QA-250, QA-252, QA-255, QA-257, QA-259…261, QA-263, QA-264, QA-266) không có dòng.
  - Lý do cũ, nay trái với SR/routing 0.2:
    - "| QA-011 | … | SR | Phần Khối lớp → R5 M02/M03; "AI Classification trên post" không còn (DEC-050) |" (`disposition-M05.md:73`), trong khi SR viết "| ISH-M05-002.10 | QA-011 | Nói thẳng | Guest "Xem AI Classification trên post": phân loại hiển thị trên bài; …" (`ISH-SR-M05.md:479`).
    - "| QA-235, ISS-175 | Không ngưỡng tối thiểu vào Trending | R5 | M14 (hiển thị) |" (`disposition-M05.md:94`), trong khi SR có "| ISH-M05-008.18 | QA-235, ISS-175 | Nói thẳng |" (`ISH-SR-M05.md:551`).
    - "| DEC-065 | Danh sách sự kiện thông báo | R5 | Không có sự kiện "bài mới trong Topic đang theo dõi" — ghi chú cho M07 |" (`disposition-M05.md:80`), trong khi register nay có "| New post in a followed Topic **[Added 2026-10-05 — DEC-155]** | Yes | No |" (`decisions.md:392`).
    - "| DEC-124 | Trending Post (M14) dùng decay; DEC-052 giữ nguyên | R5 | M14 |" (`disposition-M05.md:54`), trong khi DEC-158 sửa DEC-052.
  - Selfcheck: "| CL-A03 | Đạt (r1: Không đạt, AUD-17) | disposition-M05.md nay có một dòng cho mỗi mục KEYWORD không ở SR/routing (30 mục thêm: DEC-066 … QA-262) |" (`selfcheck-M05.md:14`).
- **Bằng chứng trong quy tắc:** RULES §7.7 yêu cầu mục không liên quan "chỉ ghi ở `specs/audit/work/disposition-Mxx.md` (một dòng: ID, lý do một câu)", áp cho REFERENCING, KEYWORD và CROSS-CUTTING.
- **Vấn đề:** Author đã thêm dòng cho đúng 30 mục mà vòng 1 liệt kê, nhưng giữ cách gộp bằng một câu ở `disposition-M05.md:69` cho phần còn lại; inventory mới của Author (108 KEYWORD, từ khóa có thêm "lớp", "dropdown", "whitelist") làm lộ thêm 26 mục không có dòng. Nguyên nhân của AUD-M05-17 (gộp thay cho từng dòng) chưa được xử lý. Ngoài ra, bốn lý do trong disposition không còn đúng với SR/routing 0.2, nên disposition không còn là bản phân loại tin được cho các mục đó. Đã đọc lấy mẫu có chủ đích QA-230, DEC-025, ISS-162, QA-242, ISS-189, QA-264: đều thuộc module khác hoặc không liên quan, không thấy hành vi M05 nào bị sót.
- **Lý do mức:** CL-A03 mặc định Trung bình; giữ mức Thấp như vòng 1 vì mọi mục lấy mẫu đều không liên quan, phần bị sót chỉ là dấu vết phân loại.
- **Hệ quả nếu không sửa:** Không chứng minh được "không sót" cho 26 mục KEYWORD và 24 mục CROSS-CUTTING; bốn lý do cũ có thể dẫn người đọc (Auditor vòng sau, Author module khác) tới kết luận sai về chỗ đi của QA-011, QA-235, DEC-065, DEC-124.
- **Hướng xử lý (Author quyết cách viết):** Thêm một dòng (ID, lý do một câu) cho mỗi mục KEYWORD và CROSS-CUTTING không nằm ở SR/routing, theo inventory hiện hành; bỏ câu gộp ở dòng 69; cập nhật bốn lý do cũ; sửa lời khẳng định ở selfcheck.
- **Trạng thái so với vòng 1:** AUD-M05-17 — Sửa chưa đủ.

### P1-02 — Hai hàng R5 giao chủ sở hữu mà nguồn không nêu: ghi nhận lượt xem (M03) và danh sách Tag cho Guest (M14/M06)

| Lớp | OBSERVATION | Mức đề xuất | Thấp | Checklist | CL-E03 |
|---|---|---|---|---|---|

- **Vị trí:** routing R5 (`ISH-RT-M05.md:75`, `:64`); ISH-M05-001.3 (`ISH-SR-M05.md:152`); ISH-M05-008.14.
- **Bằng chứng trong routing/SR:**
  - "| DEC-158, QA-294 | Ghi nhận lượt mở trang chi tiết bài viết của người dùng đã đăng nhập (trang bài viết thuộc M03) | M03 — chưa có SR, ghi nguồn DEC-158; cách đếm người xem ở ISH-M05-008.14 |" (`ISH-RT-M05.md:75`)
  - "| DEC-047, DEC-051, DEC-151, QA-284, QA-011 | Duyệt danh sách bài viết theo một Topic hoặc một Tag, gồm danh sách Tag cho Guest (QA-011); Tag bị vô hiệu hóa không duyệt được | M14 hoặc M06 — chưa có SR, ghi nguồn DEC-151 |" (`ISH-RT-M05.md:64`)
  - "| ISH-M05-001.3 | Hệ thống phải cho phép mọi người dùng, kể cả Guest, xem danh sách Topic trong danh mục Topic. |" (`ISH-SR-M05.md:152`)
- **Bằng chứng trong nguồn:**
  - "Viewing data is recorded per view with its time (detail in Phase 8); no tracking of Guests." (`decisions.md:845`, DEC-158) — không nêu module ghi nhận.
  - "Browsing posts by Topic/Tag (the "browse" in DEC-047/DEC-051) is owned by M14 or M06 (to be fixed when those SRs are written), not M05." (`decisions.md:817`, DEC-151) — nói về duyệt *bài viết*, không nói về danh sách Tag.
  - "  - CLAS: Xem danh sách Topic / Tag / Khối lớp" (`qa-log.md:134`, QA-011) — một câu nguồn cho cả Topic và Tag.
- **Vấn đề:**
  - Ghi nhận lượt xem không có kết quả nào người dùng nhìn thấy ngoài điểm Trending (M05) và Trending Post (M14); theo quy tắc 4A (RULES §5 mục 1) chủ sở hữu chưa hiển nhiên là M03. Không có OP nào về chủ sở hữu này (tìm `OP-M05` có "người xem/lượt xem/lượt mở/M03": chỉ OP-M05-12, nói về hiển thị Topic/Tag trên bài). Nếu SR M03 không nhận hàng này, ISH-M05-008.14 không có dữ liệu để kiểm.
  - Cùng một câu QA-011, phần "danh sách Topic" nằm ở SR M05 (001.3) còn phần "danh sách Tag" đi R5 sang M14/M06 với nguồn là DEC-151, vốn chỉ nói về duyệt bài viết.
  - Không xếp DEFECT: cả hai hàng đều có chỗ đi và có module nhận; việc giao chủ sở hữu là lựa chọn hợp lý nhưng chưa có xác nhận (RULES §5 mục 2 cho phép đặt OP loại Đề xuất).
- **Hệ quả nếu không xử lý:** Có thể không module nào viết yêu cầu ghi nhận lượt xem; quyền Guest xem danh sách Tag và danh sách Topic có thể nằm ở hai module khác nhau mà không ai chủ ý.
- **Hướng xử lý (Author quyết cách viết):** Đặt OP loại Đề xuất cho chủ sở hữu của hai hàng này, hoặc nêu nguồn xác nhận.
- **Khuôn hỏi stakeholder:**
  - Vấn đề: Module nào ghi nhận lượt mở trang chi tiết bài viết của người dùng đã đăng nhập (dữ liệu cho người xem ở Trending), và module nào cho Guest xem danh sách Tag?
  - Nguồn: DEC-158 (`decisions.md:845`) "Viewing data is recorded per view with its time"; QA-011 (`qa-log.md:134`) "CLAS: Xem danh sách Topic / Tag / Khối lớp".
  - Lựa chọn: A) Ghi nhận lượt xem ở M03 (trang bài viết), danh sách Tag ở M14/M06 như routing hiện tại — hệ quả: SR M03 và SR M14/M06 phải nhận hai hàng R5 này. B) Cả hai ở M05 — hệ quả: thêm hai yêu cầu vào SR M05; danh sách Topic và danh sách Tag cùng một chỗ. C) Ghi nhận lượt xem ở M05, danh sách Tag ở M14/M06.
  - Đề xuất: C, vì kết quả nhìn thấy duy nhất của việc ghi nhận lượt xem là điểm Trending (M05 sở hữu theo quy tắc 4A), còn danh sách Tag gắn với việc duyệt theo Tag mà DEC-151 đã giao cho M14/M06.

### P1-03 — Câu cũ trong register chưa được đánh dấu sau DEC-158: QA-106 (OWNED), QA-226, ISS-171

| Lớp | OBSERVATION | Mức đề xuất | Thấp | Checklist | CL-A09 |
|---|---|---|---|---|---|

- **Vị trí:** Không nằm trong SR; SR đã viết theo DEC-158. SR và routing trích QA-106 làm nguồn ở ISH-M05-008 (`ISH-SR-M05.md:533`) và R2 (`ISH-RT-M05.md:27`).
- **Bằng chứng trong nguồn:**
  - "| QA-106 | Trending calculation? | Rolling 7-day window, score = Σ(1+upvotes×2+comments×1), recalc every 15-30min |" (`qa-log.md:745`) — không có nhãn.
  - "Trending Topic/Tag giữ nguyên DEC-052 (rolling 7-day hard window, không decay)." (`qa-log.md:930`, QA-226) — không có nhãn.
  - "Trending Topic/Tag giữ nguyên DEC-052; Trending Post là khái niệm mới, xem ISS-185" (`issue-queue.md:261`, ISS-171) — không có nhãn.
  - Đối chiếu: DEC-052 đã mang "**[Amended 2026-10-05 — DEC-158: engagement adds 1 × bookmarks + 0.1 × unique viewers; see also DEC-154]**" (`decisions.md:310`); tiền lệ QA-295: "Có — thêm ghi chú [Amended] trỏ tới DEC-048, QA-269, DEC-144, DEC-141; không xóa chữ cũ." (`qa-log.md:1030`).
- **Vấn đề:** DEC-158 sửa công thức của DEC-052 (thêm bookmark và người xem), nhưng ba câu cũ cùng nội dung vẫn nguyên văn, không nhãn. Đây cùng loại với AUD-M05-21 vòng 1, nay phát sinh mới do DEC-158. SR không bị ảnh hưởng: ISH-M05-008.13 viết theo DEC-158 và ghi cả DEC-052, DEC-158 ở cột Nguồn.
- **Hệ quả nếu không xử lý:** Người viết SR M14 hoặc người đọc Phụ lục A (ISH-M05-008 trích QA-106) có thể lấy công thức cũ.
- **Hướng xử lý:** Stakeholder quyết có áp tiền lệ QA-295 cho ba câu này không.
- **Khuôn hỏi stakeholder:**
  - Vấn đề: Có thêm nhãn [Amended] cho QA-106, QA-226, ISS-171 sau DEC-158 không?
  - Nguồn: `qa-log.md:745`, `qa-log.md:930`, `issue-queue.md:261`; DEC-158 (`decisions.md:845`).
  - Lựa chọn: A) Thêm nhãn trỏ tới DEC-158, không xóa chữ cũ — hệ quả: register nhất quán với cách đã làm ở QA-295. B) Giữ nguyên — hệ quả: SR M14 có thể trích công thức cũ.
  - Đề xuất: A, vì cùng loại với QA-295.

## 2. Kết quả checklist của lượt

| Mã | Kết quả | Finding / ghi chú |
|---|---|---|
| CL-A01 | Đạt | Mọi ý của DRAFT §3.1–§3.4 (mục DRAFT của M05) và các ý liên quan M05 ở §4.5, §7.1–§7.4, §8.1, §11.2, §11.5, dev_priority có chỗ đi (coverage phần B). DRAFT §7.2 nay ở 008 và 008.13 (`ISH-SR-M05.md:533`, `:546`) và R6 (`ISH-RT-M05.md:87`). Dấu vết yếu, không lập finding: R5 cho §7.3/§7.4/§8.1 ghi ID register thay vì mục DRAFT |
| CL-A02 | Đạt | `check_sr` không có COV-01, không có INV-01; COV-00: OWNED=100, trong SR=92, trong routing=34. Ma trận tay: 100/100 mục OWNED có chỗ đi, kể cả 24 mục mới |
| CL-A03 | Không đạt | P1-01 (26 KEYWORD và 24 CROSS-CUTTING không có dòng; bốn lý do cũ). REFERENCING 21/21 đã phân loại hợp lý |
| CL-A04 | Đạt | Không có COV-02, TRC-06; các nguồn ngoài inventory OWNED được trích (DEC-033, DEC-100, DEC-126, QA-011, QA-235…) đều có thật trong register |
| CL-A08 | Đạt | DRAFT §3.2/§3.4 ↔ DEC-143; DRAFT §7.2 ↔ DEC-158 ("Overrides the remaining Views/Bookmarks part of DRAFT §7.2", `decisions.md:845`); DRAFT §4.5 ↔ DEC-141; DRAFT §11.2 ↔ QA-269, DEC-144. Mỗi cặp: SR theo register, cột Nguồn có cả DRAFT và register, có QA đã hỏi stakeholder. AUD-M05-18 đã sửa |
| CL-A09 | Đạt | SR theo quyết định mới ở mọi chỗ register ghi rõ: DEC-147 (R6 `:82`), DEC-149 (R6 `:83`), DEC-158 (008.13), DEC-155 (R5 `:69`), DEC-140 (R6 `:81`). Mâu thuẫn QA-043 ↔ DEC-065 của vòng 1 đã giải bởi DEC-155 (`decisions.md:392`). P1-03 là OBSERVATION về register, không phải lỗi của SR |
| CL-A10 | Đạt | Đã kiểm tay 26 mục COV-03: phần ở SR và phần ở routing không trùng, không sót phần nào. DEC-145 đủ bốn hệ quả (002.2, 004.5, 011.6, 011.7); QA-011 đủ các phần; QA-235 tách SR/R5; DEC-158 tách SR/R1/R5 M14/R5 M03/R6 |
| CL-E01 | Đạt | Mục 4–5 không có bảng/trường, NFR hay giao diện; chu kỳ tính lại ở R2, lưu lượt xem ở R1, thông điệp ở R3 |
| CL-E02 | Đạt | Hiển thị Trending, lọc/tìm, duyệt, thông báo, Lớp/Khối, Trending Post đều ở R5; hiển thị Topic/Tag trên bài (002.10, 006.16) có OP-M05-12 về chủ sở hữu (RULES §5 mục 2) |
| CL-E03 | Đạt | Mọi hàng R5 có module và nguồn; R6 có "bị thay bởi"; R7 có lý do chấp nhận được, không chứa hành vi. Kèm OBSERVATION P1-02 (chủ sở hữu hai hàng R5 chưa có nguồn xác nhận). AUD-M05-05 đã sửa |
| CL-E04 | Đạt | 4.1 "Không có."; nội dung về người xem và Guest ("no tracking of Guests") lấy nguyên từ DEC-158/QA-294, không có luật hay thông tin riêng tư tự thêm |
| CL-F03 | Đạt | Mọi câu trả lời vòng 2 có ID register (ISS-228…236, QA-288…296, DEC-154…159) và SR khớp. Ngoại lệ mốc P1 mới (011.6, 011.7) suy từ mốc của tính năng theo dõi và Trending (dev_priority P1), cùng cách với 010.2, 011.3, 011.4, 012.3 đã có ở bản 0.1 — không phải quyết định mới |

## 3. Kết quả kiểm tra tự động

ERROR = 0, WARN = 0, INFO = 28. Lệnh đã chạy (từ gốc repo):

```
python .agent-instructions/system_analysis/shared/sr-tools/check_sr.py \
  --sr .agents/.claude/system_analysis/output/specs/ISH-SR-M05.md \
  --routing .agents/.claude/system_analysis/output/specs/routing/ISH-RT-M05.md \
  --inventory .agents/.claude/system_analysis/output/specs/audit/work/audit-inventory-P1-M05-r2.json \
  --json .agents/.claude/system_analysis/output/specs/audit/work/check-P1-M05-r2.json
```

- INFO COV-03 × 26: DEC-047, DEC-049, DEC-050, DEC-051, DEC-052, DEC-140, DEC-141, DEC-147, DEC-150, DEC-154, DEC-155, DEC-158, DEC-159, ISS-207, ISS-229, QA-101, QA-102, QA-104, QA-106, QA-107, QA-268, QA-278, QA-288, QA-289, QA-294, QA-296 — kiểm tay ở CL-A10, đạt.
- INFO COV-00: OWNED=100, trong SR=92, trong routing=34.
- INFO TST-99: không truyền `--tests` (đúng tham số của P1).
- Không có COV-01, COV-02, INV-01. Yêu cầu: 12 cấp trên, 107 cấp dưới.

## 4. Hồ sơ xác minh

**Trích đoạn của finding (mỗi trích đoạn một dòng, `grep -n -F`):**

- `grep -n -F "các mục KEYWORD còn lại khớp từ khóa chung" disposition-M05.md` → 1 (dòng 69)
- `grep -n -F '"AI Classification trên post" không còn (DEC-050)' disposition-M05.md` → 1 (dòng 73)
- `grep -n -F "| QA-235, ISS-175 | Không ngưỡng tối thiểu vào Trending | R5 | M14 (hiển thị) |" disposition-M05.md` → 1 (dòng 94)
- `grep -n -F 'Không có sự kiện "bài mới trong Topic đang theo dõi"' disposition-M05.md` → 1 (dòng 80)
- `grep -n -F "Trending Post (M14) dùng decay; DEC-052 giữ nguyên" disposition-M05.md` → 1 (dòng 54)
- `grep -n -F "disposition-M05.md nay có một dòng cho mỗi mục KEYWORD" selfcheck-M05.md` → 1 (dòng 14)
- `grep -n -F "## KEYWORD hits trong register (108 muc)" inventory-M05.md` → 1 (dòng 155); `grep -n -F -e "- QA-230 (qa-log.md:934" -e "- DEC-025 (decisions.md:167" -e "- ISS-162 (issue-queue.md:247" -e "- QA-242 (qa-log.md:951" inventory-M05.md` → dòng 241, 161, 193, 249
- `grep -n -F "| DEC-128, DEC-129, DEC-130" disposition-M05.md` → 1 (dòng 130)
- `grep -n -F "| ISH-M05-002.10 | QA-011 | Nói thẳng |" ISH-SR-M05.md` → 1 (dòng 479)
- `grep -n -F "| ISH-M05-008.18 | QA-235, ISS-175 | Nói thẳng |" ISH-SR-M05.md` → 1 (dòng 551)
- `grep -n -F "[Added 2026-10-05 — DEC-155]" decisions.md` → 1 (dòng 392)
- `grep -n -F "Ghi nhận lượt mở trang chi tiết bài viết của người dùng đã đăng nhập (trang bài viết thuộc M03)" ISH-RT-M05.md` → 1 (dòng 75)
- `grep -n -F "gồm danh sách Tag cho Guest (QA-011)" ISH-RT-M05.md` → 1 (dòng 64)
- `grep -n -F "kể cả Guest, xem danh sách Topic trong danh mục Topic" ISH-SR-M05.md` → 1 (dòng 152)
- `grep -n -F "Viewing data is recorded per view with its time (detail in Phase 8)" decisions.md` → 1 (dòng 845)
- `grep -n -F "Browsing posts by Topic/Tag" decisions.md` → 1 (dòng 817)
- `grep -n -F "CLAS: Xem danh sách Topic / Tag / Khối lớp" qa-log.md` → 1 (dòng 134)
- `grep -n -F "score = Σ(1+upvotes×2+comments×1), recalc every 15-30min" qa-log.md` → 1 (dòng 745)
- `grep -n -F "Trending Topic/Tag giữ nguyên DEC-052 (rolling 7-day hard window" qa-log.md` → 1 (dòng 930)
- `grep -n -F "Trending Topic/Tag giữ nguyên DEC-052; Trending Post là khái niệm mới" issue-queue.md` → 1 (dòng 261)
- `grep -n -F "**[Amended 2026-10-05 — DEC-158: engagement adds 1 × bookmarks" decisions.md` → 1 (dòng 310)
- `grep -n -F "Có — thêm ghi chú [Amended] trỏ tới DEC-048" qa-log.md` → 1 (dòng 1030)
- `grep -n -F "| DEC-052, DEC-142, DEC-158, QA-106, ISS-082" ISH-SR-M05.md` → 1 (dòng 533); `grep -n -F "| DEC-052, QA-106 | Điểm Trending Topic và Tag được tính lại" ISH-RT-M05.md` → 1 (dòng 27)

**Khẳng định vắng mặt (ít nhất hai cách):**

- P1-01: script đối chiếu ID của inventory Author (KEYWORD 108, CROSS 37) với tập ID trong SR, routing, disposition (có khai triển dải "…") → KEYWORD thiếu 26, CROSS thiếu 24. Kiểm lại từng ID mẫu bằng `grep -c -F`: QA-230, DEC-025, ISS-162, QA-242, ISS-189, QA-264 → disposition 0, SR 0, routing 0. Chạy cùng script với inventory của lượt này (KEYWORD 100, CROSS 42) → thiếu 18 và 28, giao với tập trên.
- P1-02: `grep -n -E "^\| OP-M05" ISH-SR-M05.md | grep -i -E "người xem|lượt xem|lượt mở|M03"` → 1 (OP-M05-12, nói về hiển thị Topic/Tag, không về lượt xem); `grep -c -F "danh sách Tag" ISH-SR-M05.md` → 0; `grep -n -i -E "record.*view|lượt xem" decisions.md qa-log.md` → chỉ DEC-158 (`decisions.md:845`) và QA-294 (`qa-log.md:1029`), không nêu module.
- P1-03: `sed -n 745p qa-log.md | grep -c -E "Amended|Clarified"` → 0; tương tự `qa-log.md:930` → 0, `issue-queue.md:261` → 0.

**Trạng thái finding vòng 1 thuộc mục của P1:**

| AUD vòng 1 | Mục | Trạng thái | Bằng chứng mới |
|---|---|---|---|
| AUD-M05-02 (CONFLICT, CL-A09) | A09 | Đã sửa (stakeholder trả lời ISS-229/QA-289/DEC-155) | Register: "| New post in a followed Topic **[Added 2026-10-05 — DEC-155]** | Yes | No |" (`decisions.md:392`). Routing: "sự kiện đã thêm vào DEC-065 theo DEC-155" (`ISH-RT-M05.md:69`). SR: "gồm thông báo khi có bài viết mới trong Topic." (`ISH-SR-M05.md:54`, `:302`) |
| AUD-M05-03 (phần CL-A10) | A10 | Đã sửa | "| ISH-M05-011.6 | Khi Mod hoặc Admin gộp Topic nguồn vào Topic đích, hệ thống phải loại Topic nguồn khỏi xếp hạng Trending. |" (`ISH-SR-M05.md:411`); "| ISH-M05-011.7 | Khi người dùng yêu cầu theo dõi một Topic đã bị loại khỏi danh mục Topic, hệ thống phải từ chối yêu cầu đó. |" (`:412`). Phần CL-B13/CL-B09 thuộc P3 |
| AUD-M05-04 (CL-A10) | A10 | Đã sửa (lý do cũ trong disposition chuyển vào P1-01) | "| ISH-M05-006.16 | Khi người dùng, kể cả Guest, xem một bài viết, hệ thống phải hiển thị các Tag hoạt động của bài viết đó. |" (`ISH-SR-M05.md:290`); ISH-M05-002.10 (`:180`); danh sách Tag → R5 (`ISH-RT-M05.md:64`, xem P1-02); OP-M05-12 (`ISH-SR-M05.md:598`) |
| AUD-M05-05 (CL-E03) | E03 | Đã sửa | "| ISH-M05-008.19 | Hệ thống phải đưa mọi Tag hoạt động vào xếp hạng Trending mà không đặt ngưỡng điểm tối thiểu. |" (`ISH-SR-M05.md:349`), 008.18 (`:348`); routing tách "Phần Trending Post: không đặt ngưỡng tối thiểu để bài vào Trending Post" (`ISH-RT-M05.md:67`); R4 provisional (`:55`) |
| AUD-M05-17 (CL-A03) | A03 | Sửa chưa đủ → P1-01 | 30 mục vòng 1 nay có dòng (`disposition-M05.md:97`–`:126`); câu gộp còn ở `:69`; 26 mục KEYWORD khác không có dòng |
| AUD-M05-18 (CL-A08) | A08 | Đã sửa (stakeholder trả lời ISS-234/QA-294/DEC-158) | "| ISH-M05-008.13 | DEC-158, QA-294, DEC-142, DRAFT §7.2 | Nói thẳng |" (`ISH-SR-M05.md:546`); "| DRAFT §7.2 | DEC-052, DEC-142, DEC-158 |" (`ISH-RT-M05.md:87`) |
| AUD-M05-21 (OBSERVATION, CL-A09) | A09 | Đã sửa (stakeholder trả lời QA-295) | `glossary.md:14` "**[Amended 2026-10-05 — DEC-048: 11 Topics, final]**"; `glossary.md:29` "**[Amended 2026-10-05 — QA-269: Topic only, no Tag suggestion; …]**"; DEC-125 "**[Amended 2026-10-05 — DEC-141: Follow of Topic is owned by M05; M07 owns the notification (DEC-155)]**" (`decisions.md:697`). Câu cũ mới phát sinh sau DEC-158 → P1-03 |

**Tìm hồi quy (vòng 2, bước 3) trong phạm vi P1.** Đã đọc lại 17 ID mới, 13 ID đổi nội dung, hai ID bị bỏ (002.4 → 002.5/002.6/002.11; 010.4 → 001.5) và các hàng routing đổi (diff `snapshot-ISH-RT-M05-v0.1.md` với bản 0.2: R1 +2 hàng, R2 sửa 1, R3 +1, R4 +2, R5 sửa 4 và +1, R6 sửa 1 và +1). Về độ phủ và ranh giới: không có hồi quy — mọi nguồn của ID bị bỏ vẫn có chỗ đi (DEC-049 ở 001.5, 002.5…002.8; DEC-156 ở 002.11), không yêu cầu mới nào mô tả hành vi của module khác ngoài 002.10/006.16 (đã có OP-M05-12). Hàng R5 mới (`ISH-RT-M05.md:75`) là nguồn của P1-02.

**Finding bị loại hoặc chỉnh:**

- Ứng viên "Thiếu R6 cho DEC-052 → DEC-158" bị loại: SR trích cả DEC-052 và DEC-158 ở 008/008.13, DEC-052 đã có nhãn Amended; RULES §6 chỉ đòi R6 khi mục bị ghi đè, còn DEC-052 bị sửa một phần và vẫn là nguồn của 008.8.
- Ứng viên "Ngoại lệ mốc P1 cho 011.6, 011.7 trái DEC-151 (gộp Topic = P0)" bị loại khỏi P1 (CL-F03): là suy luận từ mốc của tính năng phụ thuộc, không phải số liệu/quyền mới; việc so 5.1 với nguồn thuộc CL-C05 (P2) — ghi ở mục 6.
- Ứng viên "R1 chứa hàng của M13 (DEC-133)" bị loại: nội dung là mô hình dữ liệu (R1 đúng loại), hàng tự ghi "Thuộc M13"; vòng 1 cũng không lập finding.
- Ứng viên "Danh sách Tag cho Guest thiếu chỗ đi" (vòng 1 AUD-M05-04) hạ thành một phần của OBSERVATION P1-02: nay đã có chỗ đi ở R5, chỉ chủ sở hữu chưa có nguồn.

## 5. Phạm vi và giới hạn không kiểm được

- Đã đọc nguyên văn: DRAFT `iShare_modules.md` §3.1–§3.4, §4.5, §7.1–§7.4, §8.1, §11.2, §11.5; `iShare_dev_priority.md` (các dòng Topic/Tag/Follow/Trending/Feedback); `iShare_specs_general.md` §3, §6; toàn bộ 100 mục OWNED (`decisions.md:272`–`:312`, `:766`–`:851`; `issue-queue.md:101`–`:110`, `:324`–`:357`; `qa-log.md:736`–`:748`, `:998`–`:1031`); 12/21 mục REFERENCING đọc nguyên văn (DEC-008, DEC-065, DEC-090, DEC-093, DEC-095, DEC-099, DEC-124, DEC-125, DEC-132, ISS-171, QA-226, QA-237), số còn lại đọc theo tiêu đề; KEYWORD đọc có chủ đích khoảng 15 mục (QA-011, QA-017, QA-043, QA-123, QA-127, QA-231, QA-235, QA-236, QA-243, DEC-100, DEC-126, DEC-133, DEC-096 và mẫu của P1-01), phần còn lại theo tiêu đề; CROSS-CUTTING theo tiêu đề; `glossary.md` dòng 10–32.
- Không kiểm được việc stakeholder đã được báo ngoài register.
- Chưa có SR của M03, M06, M07, M10, M13, M14: các hàng R5 chỉ kiểm được nguồn, không kiểm được ID sở hữu hay việc module đích nhận hàng.
- Tệp của Author chỉ mở sau P1.4: `disposition-M05.md` (đọc đủ mọi mục REFERENCING, KEYWORD lấy mẫu có chủ đích) và các dòng mục P1 của `selfcheck-M05.md`. Không mở `tests-Mxx.md`, không mở tệp lượt P2/P3 của vòng 2.
- Một giới hạn nhỏ: lệnh `head -15` ở bước C0 cho thấy đoạn mục 1 Tổng quan của SR trước khi lập phần A (đoạn này chỉ liệt kê nhóm tính năng). Bảng 5.1 và mục 4 không được đọc trước phần A.

## 6. Chuyển lượt khác

- 2.1 "Thứ tự bảng chữ cái tiếng Việt" (`ISH-SR-M05.md:62`) chỉ liệt kê 29 chữ cái tiếng Việt; tên Tag có f, j, w, z, chữ số hay ký hiệu (ví dụ "Java", "C++", "KT&PL") không có thứ tự xác định khi phá hòa ở 008.12 — nên kiểm ở **P3** (CL-A11/CL-B08).
- DEC-154 (2) "a restored comment counts again": 008.17 chỉ nói "đang bị ẩn"; ca bình luận được khôi phục nên được dựng ở **P3**.
- ISH-M05-008.15 (không đếm Guest) có vẻ trùng ý với 008.14 (chỉ đếm "người dùng đã đăng nhập") — **P2** (CL-C02).
- Ngoại lệ mốc P1 mới cho ISH-M05-011.6, 011.7 so với DEC-151 "renaming and merging Topics … = P0" — **P2** (CL-C05).
- Ngoài phạm vi M05 (ghi để MERGE chuyển cho người viết SR M14): DEC-158 áp "within the rolling 7-day window" cho cả Trending Post (`decisions.md:845`) trong khi DEC-124 dùng suy giảm với mốc cắt 28 ngày (`decisions.md:694`); và không rõ Trending Post có giữ "1 +" của DEC-124 không.

## 7. Chỉ lượt P1 — ma trận

Ma trận ở `work/coverage-M05-r2.md` (phần A mong đợi, phần B thực tế, A.5 lệch nguồn). Các hàng có finding:

| Nguồn | Mong đợi | Thực tế | Kết quả | Finding |
|---|---|---|---|---|
| KEYWORD còn lại (inventory Author 108) và bản ISS/QA của CROSS-CUTTING | Một dòng disposition mỗi mục | 26 KEYWORD và 24 CROSS chỉ có câu gộp (`disposition-M05.md:69`) | Thiếu phân loại | P1-01 |
| QA-011, QA-235, DEC-065, DEC-124 (disposition) | Lý do khớp SR/routing | Lý do cũ (`disposition-M05.md:73`, `:94`, `:80`, `:54`) | Lý do sai | P1-01 |
| DEC-158 (ghi nhận lượt xem) | SR hoặc R1/R5 | R5 M03 (`ISH-RT-M05.md:75`), không có nguồn cho chủ sở hữu, không có OP | Khớp (chủ sở hữu chưa xác nhận) | P1-02 |
| QA-011 (danh sách Tag cho Guest) | SR hoặc R5 kèm chủ sở hữu | R5 M14/M06 (`ISH-RT-M05.md:64`), nguồn DEC-151 chỉ nói duyệt bài viết | Khớp (chủ sở hữu chưa xác nhận) | P1-02 |
| QA-106, QA-226, ISS-171 (register) | Nhãn sửa đổi theo DEC-158 | Không có nhãn | Lệch trong register | P1-03 |

Tổng: 100/100 OWNED có chỗ đi, 0 "Thiếu", 0 "Sai chỗ", 0 "Thiếu một phần".
