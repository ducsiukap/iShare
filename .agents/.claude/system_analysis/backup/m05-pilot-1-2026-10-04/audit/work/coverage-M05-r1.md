# Ma trận độ phủ độc lập — M05 (Auditor, vòng 1)

Lập **trước khi** đọc Phụ lục A / routing của Author. Cột Mong đợi là kỳ vọng của Auditor dựa trên RULES, chưa đối chiếu SR.

## A. OWNED — decisions.md

| Nguồn | Nội dung ngắn | Mong đợi | Lý do mong đợi |
|---|---|---|---|
| DEC-047 (decisions.md:276-278) | Topic = structured taxonomy, AI suggest+user confirm, filter/browse, flat (nested deferred). Tag = free #hashtag, user-typed, no fixed list, no spaces | SR (2.1 thuật ngữ) + SR (yêu cầu: cấu trúc phẳng, AI suggest) | Định nghĩa thuật ngữ bắt buộc ở 2.1; "flat" và "AI suggest" là hành vi/ràng buộc kiểm chứng được |
| DEC-048 (decisions.md:280-281) | Danh sách 11 topic cố định (Toán học … Khác) | SR (yêu cầu: giá trị hợp lệ của Topic) | Giá trị cụ thể từ nguồn, cần trong yêu cầu chọn Topic |
| DEC-049 (decisions.md:283-286) | Min1/max3 topic/post bắt buộc; Mod/Admin edit(rename)+merge, không xóa; merge tự re-point post_topics sang đích | SR (giới hạn 1-3 + từ chối ngoài khoảng, quyền edit/merge) + R1 (chi tiết bảng post_topics) | Giới hạn → yêu cầu + Suy ra từ chối vi phạm (§4.5); quyền là yêu cầu riêng (§4.2.9); cơ chế bảng là R1 |
| DEC-050 (decisions.md:288-295) | Nút "Gợi ý topic" (không tự động) → AI phân tích title+content_text → gợi ý tối đa 3, pre-tick; nội dung <20 từ → không gợi ý, hiện "nội dung quá ngắn"; user tự chỉnh → publish; nội dung đổi sau gợi ý → is_stale, soft warning + nút gợi ý lại, không chặn publish; feedback (AI gợi ý vs lựa chọn cuối) chỉ ghi khi không stale; user tự chọn từ đầu → bỏ qua AI; AI off → dropdown, không gợi ý | SR (nhiều yêu cầu cấp dưới, mỗi nhánh một yêu cầu theo §4.3) | Mỗi nhánh luồng là một yêu cầu cấp dưới riêng; không nêu giải pháp (API) |
| DEC-051 (decisions.md:297-302) | Bảng tags+post_tags; tự tạo không duyệt; max5 tag/post, max30 ký tự/tag; mod/admin KHÔNG edit/merge/delete trong điều kiện thường; khủng hoảng: soft-delete (is_active=false) → ẩn khỏi autocomplete/trending/browse; bài cũ giữ post_tags nhưng ẩn chip; nếu user gõ lại tên tag đã khóa → không tagify, hiển thị văn bản thường | SR (giới hạn 5/30 + từ chối vượt, quyền, 3 nhánh khủng hoảng) + R1 (bảng tags/post_tags) | Giới hạn → Suy ra từ chối; mỗi nhánh khủng hoảng là một yêu cầu cấp dưới (§4.3); tên bảng → R1 |
| DEC-052 (decisions.md:304-308) | Trending Topic+Tag: cửa sổ trượt 7 ngày; tính lại mỗi 15-30 phút (cache, không live); điểm = Σ(1+upvote×2+comment×1) trên toàn bộ bài trong cửa sổ; tích hợp vào Feed thuộc M14 | SR (công thức điểm + cửa sổ 7 ngày là hành vi quan sát được) + R2 (chu kỳ tính lại 15-30 phút, cache = NFR/cơ chế) + R5 (tích hợp Feed → M14) | Công thức/điểm xếp hạng là hành vi nghiệp vụ quan sát được; "cache, không live" và chu kỳ tính là chi tiết hiệu năng/cơ chế → R2; phần Feed display thuộc M14 |
| DEC-140 (decisions.md:768-770) | Topic classification: phẳng (DEC-047/048) là quyết định cuối cho SR M05, không có Category riêng; ghi đè rõ ràng QA-033/ISS-046 (2 tầng); grade_level vẫn ngoài phạm vi M05 (thuộc M03 F-POST-09, M02) | SR (theo flat, không Category) + routing R6 (QA-033/ISS-046 "đã bị thay thế") + routing R5 (grade_level → M03/M02) | Ghi đè rõ ràng trong register (§7.6) nên không phải CONFLICT; grade_level là hành vi module khác (quy tắc 4A) |

## B. OWNED — issue-queue.md (Phase 5 — M05)

| Nguồn | Nội dung ngắn | Mong đợi | Lý do |
|---|---|---|---|
| ISS-079 (issue-queue.md:103) | Topic vs Tag distinction — Closed | SR (2.1, cùng DEC-047) | Trùng DEC-047 |
| ISS-080 (issue-queue.md:104) | Topic taxonomy — 11 topics flat — Closed | SR (cùng DEC-048) | Trùng DEC-048 |
| ISS-081 (issue-queue.md:105) | AI suggest topic flow — Closed | SR (cùng DEC-050) | Trùng DEC-050 |
| ISS-082 (issue-queue.md:106) | Tag creation + limits + trending — Closed | SR (cùng DEC-051/052) | Trùng DEC-051/052 |
| ISS-083 (issue-queue.md:107) | Topics per post limit — Closed | SR (cùng DEC-049) | Trùng DEC-049 |
| ISS-084 (issue-queue.md:108) | Topic/tag edit/merge/delete — Closed | SR (cùng DEC-049/051) | Trùng DEC-049/051 |
| ISS-207 (issue-queue.md:328) | SR M05 — flat hay 2 tầng? Register không ghi rõ ghi đè — Closed: Flat thắng (DEC-140) | SR (theo DEC-140) + Phụ lục A/lịch sử ghi nhận đã xử lý xung đột | Đây chính là hồ sơ "đã báo stakeholder" cho CL-A08 |

## C. OWNED — qa-log.md (Phase 5 — M05) + System Requirement — M05

| Nguồn | Nội dung ngắn | Mong đợi | Lý do |
|---|---|---|---|
| QA-101 (qa-log.md:740) | Topic=structured category; Tag=free #hashtag no spaces | SR 2.1 | Định nghĩa |
| QA-102 (qa-log.md:741) | Flat, 11 topics (theo chương trình 2018 + non-academic) | SR | Cùng DEC-048 |
| QA-103 (qa-log.md:742) | AI suggest topic limit = max 3 (khớp max 3 topic/post) | SR | Cùng DEC-050 |
| QA-104 (qa-log.md:743) | Nội dung đổi sau AI suggest → is_stale, soft warning, feedback chỉ ghi khi không stale | SR | Cùng DEC-050 |
| QA-105 (qa-log.md:744) | Tag max 5/post, 30 ký tự/tag | SR | Cùng DEC-051 |
| QA-106 (qa-log.md:745) | Trending: cửa sổ 7 ngày trượt, điểm Σ(1+upvote×2+comment×1), tính lại 15-30p | SR + R2 | Cùng DEC-052 |
| QA-107 (qa-log.md:746) | Topic: mod edit+merge không xóa. Tag: tự do, soft-delete chỉ khủng hoảng (tên thành reserved, không tagify lại) | SR | Cùng DEC-049/051 |
| QA-108 (qa-log.md:747) | Comment không cần tag riêng — kế thừa topic/tag của post cha | SR hoặc R4 (ghi chú phạm vi) | Xác nhận biên phạm vi: Comment không có Tag/Topic riêng — cần có chỗ đi (ít nhất một dòng) |
| QA-267 (qa-log.md:1002) | ISS-207: Flat thắng — DEC-047/048 là quyết định cuối, đè QA-033/ISS-046; chỉ 1 tầng, 11 giá trị cố định | SR (theo DEC-140) + bằng chứng đã xử lý CL-A08/A09 | Nguồn "đã báo stakeholder" |

## D. OWNED — module-registry.md

| Nguồn | Nội dung ngắn | Mong đợi | Lý do |
|---|---|---|---|
| L12 (module-registry.md:12) | 11 flat topics, min1/max3/post, AI suggest(max3, is_stale), tag freeform(max5/post,30char), tags+post_tags tables, mod edit+merge topic only, trending rolling 7d | SR (mọi phần hành vi) + R1 (tên bảng tags/post_tags) | Tóm tắt trùng các DEC trên; tên bảng → R1 |
| L42 (module-registry.md:42, AI Module Fallback) | M05 Topic: AI off → user tự chọn topic, không gợi ý AI | SR (yêu cầu khi AI off) | Hành vi quan sát được khi tắt AI, trùng nhánh cuối DEC-050 |
| L49 (module-registry.md:49, ISS-042) | AI Layer nâng lên Must vì M06/M08/M05 phụ thuộc | R4 (ghi chú quy trình) hoặc không cần trong SR | Không phải hành vi của M05, chỉ là lý do ưu tiên MoSCoW của M13 |

## E. REFERENCING — phân loại

| Nguồn | Vì sao được liệt kê | Phân loại kỳ vọng |
|---|---|---|
| DEC-008 (decisions.md:28) | Nhắc M05 (AI Layer toggle) | Module khác (M13) — M05 chỉ tham chiếu khi nói "AI off" (đã có ở L42/DEC-050 nhánh cuối) |
| DEC-090 (decisions.md:522) | Nhắc M05 (Admin panel scope) | Module khác (M10) — không liên quan hành vi M05 |
| DEC-093 (decisions.md:539) | Nhắc M05 (AI toggle granularity) | Module khác (M10/M13) — nền cho "AI off" nhưng cơ chế toggle không thuộc M05 |
| DEC-095 (decisions.md:550) | Nhắc M05 (embedding model) | Không liên quan — embedding cho Search/AI, không phải Topic/Tag |
| DEC-099 (decisions.md:568) | Nhắc M05 (AI failure handling) | Liên quan một phần — DEC-132 (bên dưới) tái dùng đúng UX pattern của DEC-099 cho M05; DEC-099 gốc thuộc M13, M05 chỉ kế thừa pattern UI khi suggest thất bại |
| DEC-124 (decisions.md:690) | Nhắc M05 + DEC-052 (Trending Post, khác Trending Topic/Tag) | Module khác (M14) — DEC-052 (M05) không đổi, chỉ bị M14 tham chiếu |
| DEC-125 (decisions.md:693) | Nhắc M05 (M14 cấu trúc 4 tab, bỏ phụ thuộc M13) | Module khác (M14) — không tạo hành vi mới cho M05 |
| ISS-171 (issue-queue.md:261) | Nhắc DEC-052, QA-106 | Module khác (M14) — Closed, superseded by ISS-185, không đổi M05 |
| ISS-185 (issue-queue.md:268) | Nhắc DEC-052 | Module khác (M14) — Trending Post riêng, DEC-124 |
| ISS-186 (issue-queue.md:269) | Nhắc M05 (M14 bỏ phụ thuộc M13) | Module khác (M14) |
| QA-024 (qa-log.md:326) | Nhắc M05 (AI Layer MoSCoW) | R4 hoặc không liên quan — chỉ là lý do ưu tiên, không phải hành vi M05 |
| QA-226 (qa-log.md:930) | Nhắc DEC-052 (Trending Topic/Tag giữ nguyên) | Xác nhận DEC-052 không đổi — không cần hành vi mới, chỉ là bằng chứng M14 không sửa M05 |
| QA-237 (qa-log.md:941) | Nhắc DEC-052/124 (Trending tự refresh theo chu kỳ 15-30p) | Module khác (M14) — UI banner của Feed |
| QA-240 (qa-log.md:944) | Nhắc M05 (M14 bỏ phụ thuộc M13) | Module khác (M14) |
| DEC-139 (decisions.md:757) | Nhắc M05 (pilot module cho quy trình SR) | R4 (ghi chú quy trình) hoặc không liên quan nội dung — là quyết định về quy trình viết SR, không phải hành vi Topic/Tag |
| ISS-205 (issue-queue.md:320) | Nhắc M05 (pilot) | R4/không liên quan — quy trình |
| QA-265 (qa-log.md:994) | Nhắc M05 (pilot) | R4/không liên quan — quy trình |
| OPEN-006 (open-issues.md:14) | Nhắc M05 (SEO/SSR defer) | Không liên quan trực tiếp — cross-cutting kỹ thuật, không phải hành vi M05 |
| OPEN-008 (open-issues.md:16) | Nhắc M05 (Privacy chưa chi tiết) | Không liên quan trực tiếp — cross-cutting, không có hành vi riêng của M05 nêu trong OPEN-008 |

## F. KEYWORD — mẫu có chủ đích (các mục có khả năng liên quan M05 thật)

| Nguồn | Nội dung | Mong đợi | Lý do |
|---|---|---|---|
| QA-033 (qa-log.md:417-423) / ISS-046 | 2 tầng Category→Topic + grade_level (Phase 4, SUPERSEDED) | Routing R6 "đã bị thay thế" (bị thay bởi DEC-140) | Rule §7.6: quyết định mới hơn ghi đè rõ ràng |
| QA-043 (qa-log.md:520-523) / ISS-051 | Follow scope: User/Topic/Post (không Group); bảng `follows` follower_id/target_type/target_id; M07 cần filter theo follow type | Không rõ chủ sở hữu — khả năng module khác (M02/M07) hoặc OP-M05-xx nếu Author cho là liên quan M05 | Phase 5 M05 (DEC-047-052) không hề nhắc "theo dõi Topic"; hành vi "Follow Topic" có kết quả nhìn thấy (nút Follow trên Topic, thông báo bài mới trong topic đang follow — DRAFT §8.1) nhưng chưa được vận hành hoá ở Phase 5 bất kỳ module nào. Theo §5.2 RULES, module chưa chắc chủ sở hữu phải có OP-Mxx-nn đề xuất; đây là điểm cần kiểm khi đọc SR/disposition |
| iShare_dev_priority.md:83 | Giai đoạn 2 [P1] — Interaction: "Follow (User/Post/Topic/Tag/Group)" | Cùng vấn đề như QA-043 — xác nhận Follow Topic/Tag thực sự trong phạm vi dự án, chưa gán module | Cùng lý do trên |
| DEC-132 (decisions.md:721) | AI Topic Suggestion hallucination: output ngoài whitelist 11 topic → lỗi không chặn "Không thể gợi ý chủ đề lúc này, vui lòng chọn thủ công", user chọn tay | SR (M05) — nhánh bổ sung của DEC-050 AI suggest flow | Kết quả quan sát được nằm trên luồng chọn Topic của M05; đây là một nhánh luồng khác DEC-050 đã nêu (input ngoài danh sách hợp lệ), cần yêu cầu riêng theo §4.3 |
| DEC-133 (decisions.md:724) | Mọi AI call (gồm Topic Suggestion) log raw output vào `ai_decision_log` | R1 (bảng dữ liệu) hoặc R5 (M13 sở hữu cơ chế log) | Không có hành vi người dùng nhìn thấy ở M05; là cơ chế lưu trữ/observability chung |
| ISS-194 (issue-queue.md:294) / QA-253 | Topic Suggestion trả về ngoài 11 topic hợp lệ → xử lý sao? | Cùng DEC-132 | Trùng nội dung |
| ISS-195 (issue-queue.md:295) / QA-254 | Log raw output AI để audit/debug | Cùng DEC-133 | Trùng nội dung |
| DEC-053 (decisions.md:313) | Search: Tag/Topic exact/prefix match (pg_trgm) | Module khác (M06) — M05 chỉ là entity được search | Hành vi Search thuộc M06; M05 không cần yêu cầu riêng |
| ISS-046 (issue-queue.md:41) | Classification depth — category/topic/tag? grade_level? | Đã xử lý ở DEC-140/QA-033 (xem trên) | — |

(Các mục KEYWORD còn lại — M06 Search, M07 Notification, M09/M10/M12/M13/M15/M16, Phase 6/7 cross-cutting khác — đọc tiêu đề, không có hành vi Topic/Tag trực tiếp nào ngoài các mục đã liệt kê trên; coi là không liên quan M05.)

## G. DRAFT — mục thuộc module M05 (iShare_modules.md §3) và bối cảnh liên quan

| Nguồn | Nội dung | Mong đợi | Lý do |
|---|---|---|---|
| DRAFT iShare_modules.md:126-130 (§3.1 Topic/Category) | "Danh sách topic cụ thể chưa cố định... Ví dụ gợi ý ban đầu: Toán học, Văn học, KHTN..." | Đã được thay bằng DEC-048 (danh sách 11, final) — không cần chỗ đi riêng ngoài việc Phụ lục A dẫn DEC-048 | Câu nguồn là phiên bản sơ bộ, đã chốt ở Phase 5; không phải lệch nguồn (§7.5) vì đây là tiến trình chốt dần, không phải mâu thuẫn giữ nguyên hiệu lực |
| DRAFT iShare_modules.md:134 (§3.2 Tag) | "Một Post có thể có nhiều Tag, **không giới hạn số lượng**." | **SR phải theo register (DEC-051: max 5)**, cột Nguồn SR phải có cả DRAFT §3.2 và DEC-051, và phải có dấu vết đã báo stakeholder (OBSERVATION) nếu register không tự nói rõ là ghi đè DRAFT | Đây là trường hợp lệch nguồn kinh điển của RULES §7.5 (ví dụ minh họa trong worked-example dùng đúng cặp này) — **cần kiểm tay khi mở SR** |
| DRAFT iShare_modules.md:153-162 (§3.3 Lớp/Khối) | Lớp/Khối là trục phân loại song song Topic, gắn Post + Profile, dùng cho Personalized Feed | Module khác (M03 F-POST-09, M02) → routing R5, dẫn DEC-140 (xác nhận ngoài phạm vi M05) | DEC-140 đã nói rõ: "grade_level ... thuộc M03 (F-POST-09) và M02 ... không bị ảnh hưởng bởi quyết định này" — SR M05 không được định nghĩa hành vi Lớp/Khối |
| DRAFT iShare_modules.md:163-170 (§3.4 Quan hệ) | Post → Topic/Category, Lớp/Khối (optional), N Tags | R1 (quan hệ Post-Topic, Post-Tag) + R5 (quan hệ Post-Lớp/Khối, module khác) | Mô hình dữ liệu — thuộc Phase 8; phần Lớp/Khối thuộc module khác |
| DRAFT iShare_specs_general.md:18-28 (§3 Phạm vi nội dung) | Ba trục Topic/Lớp-Khối/Tag dùng song song; danh sách Topic chưa cố định lúc viết DRAFT | SR §3.1 (tài liệu đầu vào, liệt kê DRAFT đã dùng) — không tạo yêu cầu riêng | Bối cảnh tổng quan, không phải yêu cầu; đã chốt cụ thể ở DEC-047-052 |
| DRAFT iShare_specs_general.md:34-36 (§4 Bản đồ module) | "3. Topic/Tag/Lớp-Khối — phân loại nội dung" | SR §3.1 (liệt kê tài liệu nguồn) | Chỉ là mục lục tổng quan |
| DRAFT iShare_modules.md:581-600 (§11.2 AI Content Classification) | "AI đề xuất: Topic/Category, **Tags**" — Flow Post→Classification API→Topic+Tags→User/Mod review; có thể cho user chỉnh trước publish | **Lệch nguồn khả năng:** DRAFT nói AI gợi ý cả Tags, nhưng DEC-050 (Phase 5, cụ thể hơn) chỉ nói AI suggest **Topic**; DEC-051 mô tả Tag là "Fully free — mod/admin KHÔNG edit/merge/delete", tự tạo không duyệt, không nhắc AI. Mong đợi: SR theo register (AI chỉ gợi ý Topic, Tag thuần tự do, không AI) và có dấu vết đã nhận diện, xử lý theo §7.5 | Cần kiểm tay: SR có vô tình thêm "AI gợi ý Tag" (sai, theo DRAFT cũ) không, hoặc có bỏ sót việc ghi nhận lệch này |
| DRAFT iShare_modules.md:371-380 (§8.1 Notification Event) | "Nội dung mới trong topic/tag/group đang follow" | Module khác (M07) — M05 chỉ là nguồn dữ liệu (topic/tag tồn tại), không viết hành vi thông báo | Hành vi gửi thông báo thuộc M07, tham chiếu Topic/Tag theo ID |
| DRAFT iShare_modules.md:343-364 (§7.3 Search, §7.4 Filter/Sort) | Tìm/lọc theo Topic, Tag | Module khác (M06) | Hành vi Search/Filter thuộc M06, M05 chỉ là entity |
| DRAFT iShare_modules.md:333-341 (§7.2 Trending/Popular, Views/Stars/Comments/Bookmarks/Recency) | Tiêu chí trending tổng quát cho Feed | Module khác (M14, DEC-124 Trending Post) — không phải Trending Topic/Tag (DEC-052 đã là nguồn riêng, không trùng) | Đây là trending cho Post trong Feed, khác đối tượng với DEC-052 (Topic/Tag) |

## Mâu thuẫn và lệch nguồn ghi nhận khi đọc (trước khi mở SR)

1. **DRAFT §3.2 "Tag không giới hạn số lượng" vs DEC-051 "Max 5 tags/post".** Lệch nguồn kinh điển theo RULES §7.5 — cần kiểm SR có theo register, có ghi đủ 2 nguồn, có dấu vết báo stakeholder không. (Xem bảng G)
2. **DRAFT §11.2 "AI đề xuất Topic/Category, Tags" vs DEC-050 (chỉ Topic) + DEC-051 (Tag fully free, không có vai trò AI).** Có khả năng là lệch nguồn thứ hai, chưa thấy QA/DEC nào nói rõ "AI không gợi ý Tag" — cần kiểm SR xử lý ra sao; nếu không có dấu vết thì là CL-A08 vi phạm (thiếu một trong hai điều kiện) hoặc CONFLICT nếu không có QA/DEC chọn phía.
3. **QA-033/ISS-046 (2 tầng Category→Topic) bị DEC-140 ghi đè rõ ràng, nêu đích danh.** Không phải CONFLICT (đã có ghi đè rõ theo §7.6) — kỳ vọng SR theo flat, routing R6 ghi QA-033/ISS-046 "bị thay bởi DEC-140".
4. **Follow Topic/Tag (QA-043, dev_priority P1) chưa được vận hành hoá ở bất kỳ module nào trong Phase 5.** Không rõ M05 có phải chủ sở hữu "nút Follow Topic" hay không — nguồn không nói rõ. Cần kiểm SR/disposition có OP-M05-xx cho điểm này hay bỏ sót hoàn toàn (không SR, không routing, không disposition "không liên quan" có lý do).
