# Inventory M05

Nguon: registers=.agents/.claude/system_analysis/output/registers | keywords=topic,tag,hashtag,trending,chủ đề,lớp,khối,grade,follow,theo dõi

ID ke tiep con trong (de ghi register): ISS-210, QA-270, DEC-142, OPEN-009

## OWNED (28 muc)

### decisions.md (8)

| ID | Dong | Section | Tieu de / noi dung rut gon |
|---|---|---|---|
| DEC-047 | 276 | Phase 5 — M05: Topic & Tag | Topic vs Tag |
| DEC-048 | 280 | Phase 5 — M05: Topic & Tag | Topic list (11, final) |
| DEC-049 | 283 | Phase 5 — M05: Topic & Tag | Topic rules |
| DEC-050 | 288 | Phase 5 — M05: Topic & Tag | AI suggest topic flow |
| DEC-051 | 297 | Phase 5 — M05: Topic & Tag | Tag data model + rules |
| DEC-052 | 304 | Phase 5 — M05: Topic & Tag | Trending (Topic + Tag) |
| DEC-140 | 768 | System Requirement — M05: Topic & Tag | Topic classification — flat confirmed, supersedes 2-tier scoping |
| DEC-141 | 772 | System Requirement — M05: Topic & Tag | Follow Topic ownership — M05, Topic only (not Tag) |

### issue-queue.md (9)

| ID | Dong | Section | Tieu de / noi dung rut gon |
|---|---|---|---|
| ISS-079 | 103 | Phase 5 — M05: Topic & Tag | Topic vs Tag distinction |
| ISS-080 | 104 | Phase 5 — M05: Topic & Tag | Topic taxonomy |
| ISS-081 | 105 | Phase 5 — M05: Topic & Tag | AI suggest topic flow |
| ISS-082 | 106 | Phase 5 — M05: Topic & Tag | Tag creation + limits + trending |
| ISS-083 | 107 | Phase 5 — M05: Topic & Tag | Topics per post limit |
| ISS-084 | 108 | Phase 5 — M05: Topic & Tag | Topic/tag edit/merge/delete |
| ISS-207 | 328 | System Requirement — M05: Topic & Tag | SR M05 — Topic classification: flat (DEC-047/048) hay 2 tầng Category→Topic (QA-033/ISS-046)? Register không ghi rõ ghi… |
| ISS-208 | 329 | System Requirement — M05: Topic & Tag | SR M05 — audit vòng 1: Follow Topic/Tag đã xác nhận trong phạm vi dự án nhưng chưa module nào nhận sở hữu; dev_priority… |
| ISS-209 | 330 | System Requirement — M05: Topic & Tag | SR M05 — audit vòng 1: DRAFT §11.2 từng nêu AI gợi ý cả Tag, DEC-050/051 (Phase 5) chỉ quyết AI gợi ý Topic — chủ đích … |

### qa-log.md (11)

| ID | Dong | Section | Tieu de / noi dung rut gon |
|---|---|---|---|
| QA-101 | 740 | Phase 5 — M05: Topic & Tag | Topic vs Tag format? |
| QA-102 | 741 | Phase 5 — M05: Topic & Tag | Topic taxonomy structure? |
| QA-103 | 742 | Phase 5 — M05: Topic & Tag | AI suggest topic limit? |
| QA-104 | 743 | Phase 5 — M05: Topic & Tag | Content changed after AI suggest? |
| QA-105 | 744 | Phase 5 — M05: Topic & Tag | Tag max count/length? |
| QA-106 | 745 | Phase 5 — M05: Topic & Tag | Trending calculation? |
| QA-107 | 746 | Phase 5 — M05: Topic & Tag | Topic/tag edit/delete by mod? |
| QA-108 | 747 | Phase 5 — M05: Topic & Tag | Comment tags? |
| QA-267 | 1002 | System Requirement — M05: Topic & Tag | ISS-207: Cấu trúc Topic trong SR M05 là flat hay 2 tầng Category→Topic? |
| QA-268 | 1003 | System Requirement — M05: Topic & Tag | ISS-208: Follow Topic/Tag thuộc module nào, và có áp dụng cho Tag không? |
| QA-269 | 1004 | System Requirement — M05: Topic & Tag | ISS-209: AI có nên gợi ý cả Tag như DRAFT §11.2 từng nêu không? |

### module-registry

- L12: | M05 | Topic & Tag | 11 flat topics, min1/max3 per post, AI suggest (max 3, is_stale handling), tag freeform (max5/post,30char), tags+post_tags tables, mod edit+merge topic only, trending rolling 7d window | Phase 5 Done |
- L21: | M14 | Feed & Discovery | Could | M03, M05 | 4 tabs: Trending (sub Post/Topic/Tag, decay DEC-124), Following, Group, Newest. **Amended Phase 5 (M14 deep dive):** dependency on M13 removed — no AI-driven personalization tab in current scope, see DEC-125 |

## REFERENCING (19 muc) - ung vien amendment / module khac, Author phai phan loai

| ID | File:dong | Section | Ly do | Rut gon |
|---|---|---|---|---|
| DEC-008 | decisions.md:28 | (preamble) | nhac M05 | - **ID:** DEC-008 - **Title:** AI Layer Feature Flag — global toggle on/off - **Decision:** Hệ thống có globa… |
| DEC-090 | decisions.md:522 | Phase 5 — M10: Admin Panel | nhac M05 | ### DEC-090: Admin panel scope split - Admin-only: Role management (promote/demote USER↔MOD), System config (… |
| DEC-093 | decisions.md:539 | Phase 5 — M10: Admin Panel | nhac M05 | ### DEC-093: AI toggle granularity Two-tier hierarchy: - Master "AI Layer" toggle: overrides everything OFF w… |
| DEC-095 | decisions.md:550 | Phase 5 — M13: AI Layer | nhac M05 | ### DEC-095: Embedding model + storage - Model: OpenAI `text-embedding-3-small` (same vendor as Moderation AP… |
| DEC-099 | decisions.md:568 | Phase 5 — M13: AI Layer | nhac M05 | ### DEC-099: AI failure handling (distinct from admin AI-off toggle) Two distinct scenarios: 1. **AI delibera… |
| DEC-124 | decisions.md:690 | Phase 5 — M14: Feed & Discove… | nhac M05; nhac DEC-052 | ### DEC-124: Trending Post — decay formula (new, distinct from DEC-052) DEC-052 (Trending Topic/Tag, M05) sta… |
| DEC-125 | decisions.md:693 | Phase 5 — M14: Feed & Discove… | nhac M05 | ### DEC-125: M14 Feed structure — 4 tabs, no AI-driven personalization tab M14 Feed consists of 4 tabs: **Tre… |
| ISS-171 | issue-queue.md:261 | Phase 5 — M14: Feed & Discove… | nhac DEC-052,QA-106 | / ISS-171 / Trending Section có tái dùng công thức QA-106/DEC-052 không? / Closed — superseded by ISS-185 / T… |
| ISS-185 | issue-queue.md:268 | Phase 5 — M14: Feed & Discove… | nhac DEC-052 | / ISS-185 / Trending Post dùng công thức/decay nào? / Closed / DEC-124 — exponential half-life decay 7 ngày: … |
| ISS-186 | issue-queue.md:269 | Phase 5 — M14: Feed & Discove… | nhac M05 | / ISS-186 / M14 có còn phụ thuộc M13 (AI Layer) không? / Closed / Bỏ dependency M13 cho scope hiện tại (chỉ c… |
| QA-024 | qa-log.md:326 | Phase 3 — Scope Decomposition | nhac M05 | ### QA-024 - **Issue:** ISS-042 - **Phase:** 3 - **Question:** AI Layer (M13) nên là Should hay Must? Vì M06/… |
| QA-226 | qa-log.md:930 | Phase 5 — M14: Feed & Discove… | nhac DEC-052 | / QA-226 / ISS-185: Trending Post dùng công thức/decay nào? / Trending Topic/Tag giữ nguyên DEC-052 (rolling … |
| QA-237 | qa-log.md:941 | Phase 5 — M14: Feed & Discove… | nhac DEC-052 | / QA-237 / ISS-177: Feed có tự cập nhật real-time khi có bài mới không? / Không auto-insert nội dung. Newest/… |
| QA-240 | qa-log.md:944 | Phase 5 — M14: Feed & Discove… | nhac M05 | / QA-240 / ISS-186: M14 có còn phụ thuộc M13 (AI Layer) không? / Bỏ dependency M13 khỏi M14 cho scope hiện tạ… |
| DEC-139 | decisions.md:757 | System Requirement prep — Doc… | nhac M05 | ### DEC-139: System Requirement (SR) documentation approach SR documents are written per module, in Vietnames… |
| ISS-205 | issue-queue.md:320 | System Requirement prep — Doc… | nhac M05 | / ISS-205 / Cách viết tài liệu System Requirement (SR) theo module: cấu trúc, ngôn ngữ, thời điểm, quy trình … |
| QA-265 | qa-log.md:994 | System Requirement prep — Doc… | nhac M05 | / QA-265 / ISS-205: Cách viết tài liệu SR theo module? / Stakeholder cung cấp tài liệu mẫu (cấu trúc mục 1–6,… |
| OPEN-006 | open-issues.md:14 | (preamble) | nhac M05 | / OPEN-006 / SEO / SSR chưa làm ở MS1 (ISS-197, DEC-134) — quyết định defer có chủ đích: MS1 chỉ đảm bảo core… |
| OPEN-008 | open-issues.md:16 | (preamble) | nhac M05 | / OPEN-008 / Privacy (ISS-204, DEC-138) — chưa định nghĩa chi tiết: danh mục dữ liệu cá nhân, quyền người dùn… |

## KEYWORD hits trong register (92 muc) - muc khong nhac M05 nhung khop tu khoa; Author phan loai

Theo section: Phase 5 — M06: Search: 15; Phase 5 — M14: Feed & Discovery (QA-225…: 11; (preamble): 8; Phase 5 — M14: Feed & Discovery | Statu…: 8; Phase 5 — M13: AI Layer: 7; Phase 3 — Scope Decomposition: 6; Phase 5 — M02: User Profile: 4; Phase 5 — M10: Admin Panel: 4; Phase 5 — M07: Notification: 3; Phase 5 — M16: Chat & Messaging | Statu…: 3; Phase 5 — M16: Chat & Messaging (QA-208…: 3; Phase 6 — Cross-cutting Concerns: 3; Phase 6 — Cross-cutting Concerns | Stat…: 3; Phase 6 — Cross-cutting Concerns (QA-24…: 3; Phase 5 — M15: Analytics & Stats | Stat…: 2; Phase 5 — M15: Analytics & Stats (QA-24…: 2; Phase 7 prep — Tech Stack (OPEN-002): 2; Phase 5 — M11: Group: 1; Phase 5 — M14: Feed & Discovery: 1; Phase 5 — M09 Amendment + M12: Gamifica…: 1; Phase 5 — M12: Gamification Deep Dive (…: 1; Phase 7 prep — Tech Stack (OPEN-002, pa…: 1

- DEC-014 (decisions.md:82, (preamble)) [tu khoa: grade] Registration Flow — 3-step progressive onboarding
- DEC-020 (decisions.md:136, (preamble)) [tu khoa: follow] @Mention System — search both fields, priority tiers, atomic node
- DEC-025 (decisions.md:167, Phase 5 — M02: User Profile) [tu khoa: follow] Followers / Following display
- DEC-053 (decisions.md:313, Phase 5 — M06: Search) [tu khoa: topic,tag] Search scope (final, supersedes Phase 3 ISS-040 partial scope)
- DEC-054 (decisions.md:322, Phase 5 — M06: Search) [tu khoa: topic,tag] Search trigger
- DEC-056 (decisions.md:335, Phase 5 — M06: Search) [tu khoa: topic,tag,follow] Filters (Post search)
- DEC-057 (decisions.md:338, Phase 5 — M06: Search) [tu khoa: topic,tag] Full-text fallback + Vietnamese diacritics
- DEC-058 (decisions.md:344, Phase 5 — M06: Search) [tu khoa: topic,tag] Autocomplete (debounce dropdown)
- DEC-060 (decisions.md:350, Phase 5 — M06: Search) [tu khoa: topic,tag] Results display
- DEC-065 (decisions.md:374, Phase 5 — M07: Notification) [tu khoa: follow] Notification event list + channel
- DEC-096 (decisions.md:555, Phase 5 — M13: AI Layer) [tu khoa: topic] Topic suggestion model
- DEC-100 (decisions.md:576, Phase 5 — M13: AI Layer) [tu khoa: topic] AI rate limiting
- DEC-104 (decisions.md:605, Phase 5 — M11: Group) [tu khoa: follow] Group content moderation layers on top of system-wide M08, does not replace it
- DEC-126 (decisions.md:696, Phase 5 — M14: Feed & Disco…) [tu khoa: trending,follow] Guest access to Feed tabs
- ISS-046 (issue-queue.md:41, (preamble)) [tu khoa: topic,tag,grade] Classification depth — category/topic/tag? grade_level logic?
- ISS-051 (issue-queue.md:46, (preamble)) [tu khoa: topic,follow] Follow scope — user/topic/post/group?
- ISS-059 (issue-queue.md:65, Phase 5 — M02: User Profile) [tu khoa: follow] Followers/Following visibility
- ISS-085 (issue-queue.md:115, Phase 5 — M06: Search) [tu khoa: topic,tag] Search scope (entities)
- ISS-086 (issue-queue.md:116, Phase 5 — M06: Search) [tu khoa: topic,tag] Semantic search UX / trigger
- ISS-088 (issue-queue.md:118, Phase 5 — M06: Search) [tu khoa: topic,tag,follow] Filter kết quả
- ISS-090 (issue-queue.md:120, Phase 5 — M06: Search) [tu khoa: topic,tag] Autocomplete/suggestion
- ISS-093 (issue-queue.md:123, Phase 5 — M06: Search) [tu khoa: topic,tag] Kết quả hiển thị tabs vs mixed
- ISS-119 (issue-queue.md:173, Phase 5 — M10: Admin Panel) [tu khoa: topic,tag] Admin-exclusive vs shared-with-mod scope
- ISS-122 (issue-queue.md:176, Phase 5 — M10: Admin Panel) [tu khoa: topic] AI toggle granularity
- ISS-125 (issue-queue.md:185, Phase 5 — M13: AI Layer) [tu khoa: topic] Topic suggestion model
- ISS-129 (issue-queue.md:189, Phase 5 — M13: AI Layer) [tu khoa: topic] AI call rate limiting
- ISS-161 (issue-queue.md:246, Phase 5 — M16: Chat & Messa…) [tu khoa: lớp] Rate limiting cho chat — có cần giới hạn số tin/phút không, mức nào?
- ISS-162 (issue-queue.md:247, Phase 5 — M16: Chat & Messa…) [tu khoa: lớp,follow] Ai nhắn tin (DM) được cho ai — mở hoàn toàn, cần mutual follow, hay message request như Messenger?
- ISS-164 (issue-queue.md:249, Phase 5 — M16: Chat & Messa…) [tu khoa: follow] Group Chat — cơ chế quản trị: role, add/remove member, đổi tên, kiểm duyệt, rời nhóm, kế nhiệm Admin, giới hạ…
- ISS-166 (issue-queue.md:256, Phase 5 — M14: Feed & Disco…) [tu khoa: trending,follow] Guest (chưa đăng nhập) xem feed gì?
- ISS-168 (issue-queue.md:258, Phase 5 — M14: Feed & Disco…) [tu khoa: topic,tag,trending,follow] M14 cần những tab/view nào cho Feed?
- ISS-169 (issue-queue.md:259, Phase 5 — M14: Feed & Disco…) [tu khoa: topic,tag,trending,follow] Tab Following rỗng (chưa follow ai/gì) hiện gì?
- ISS-172 (issue-queue.md:262, Phase 5 — M14: Feed & Disco…) [tu khoa: topic,tag,trending,chủ đề] Trending Post có filter theo Topic không?
- ISS-173 (issue-queue.md:263, Phase 5 — M14: Feed & Disco…) [tu khoa: trending] Bài Group Public cross-post có tính vào Newest/Trending Post không?
- ISS-175 (issue-queue.md:265, Phase 5 — M14: Feed & Disco…) [tu khoa: trending] Có ngưỡng tối thiểu để vào Trending không?
- ISS-176 (issue-queue.md:266, Phase 5 — M14: Feed & Disco…) [tu khoa: trending] Trending có loại bài BANNED/HEAVY-warn không?
- ISS-177 (issue-queue.md:267, Phase 5 — M14: Feed & Disco…) [tu khoa: trending,follow] Feed có tự cập nhật real-time khi có bài mới không?
- ISS-179 (issue-queue.md:278, Phase 5 — M15: Analytics & …) [tu khoa: lớp,khối,grade] User Stats dashboard gồm những chỉ số nào?
- ISS-180 (issue-queue.md:279, Phase 5 — M15: Analytics & …) [tu khoa: topic] Content Stats dashboard gồm những chỉ số nào?
- QA-005 (qa-log.md:49, (preamble)) [tu khoa: chủ đề] Business goals của hệ thống là gì? Đâu là mục tiêu ưu tiên nhất?
- QA-006 (qa-log.md:59, (preamble)) [tu khoa: chủ đề,follow] ### QA-006
- QA-011 (qa-log.md:126, (preamble)) [tu khoa: topic,tag,lớp,khối] Guest (chưa đăng nhập) có quyền gì trên iShare?
- QA-017 (qa-log.md:202, (preamble)) [tu khoa: topic,tag] Có actor hệ thống (background/automated) nào? Scope AI Moderation có bao gồm Comment không? AI Class
- QA-022 (qa-log.md:303, Phase 3 — Scope Decompositi…) [tu khoa: tag] Search nên dùng semantic hay full-text? Và search được entity nào?
- QA-033 (qa-log.md:417, Phase 3 — Scope Decompositi…) [tu khoa: topic,grade] Classification — 1 hay 2 tầng? Grade level tích hợp thế nào?
- QA-034 (qa-log.md:427, Phase 3 — Scope Decompositi…) [tu khoa: grade] grade_level trên User Profile — có tự động tăng theo năm không?
- QA-038 (qa-log.md:467, Phase 3 — Scope Decompositi…) [tu khoa: grade] Leaderboard — chu kỳ và filter như thế nào?
- QA-043 (qa-log.md:517, Phase 3 — Scope Decompositi…) [tu khoa: topic,follow] Follow scope — user/topic/post/group?
- QA-047 (qa-log.md:557, Phase 3 — Scope Decompositi…) [tu khoa: follow] Points có nên giảm theo thời gian (decay) không?
- QA-067 (qa-log.md:688, Phase 5 — M02: User Profile) [tu khoa: follow] Profile page info?
- QA-069 (qa-log.md:690, Phase 5 — M02: User Profile) [tu khoa: follow] Followers/following list hidden?
- QA-109 (qa-log.md:754, Phase 5 — M06: Search) [tu khoa: topic,tag] Search scope reconfirm — does it include Topic/Group?
- QA-112 (qa-log.md:757, Phase 5 — M06: Search) [tu khoa: trending] Engagement weighting in ranking?
- QA-113 (qa-log.md:758, Phase 5 — M06: Search) [tu khoa: topic,tag,follow] Search result filters?
- QA-115 (qa-log.md:760, Phase 5 — M06: Search) [tu khoa: topic,tag] Autocomplete dropdown content?
- QA-123 (qa-log.md:774, Phase 5 — M07: Notification) [tu khoa: follow] Full notification event list?
- QA-127 (qa-log.md:778, Phase 5 — M07: Notification) [tu khoa: follow] Follow-post (subscribe/watch) feature?
- QA-160 (qa-log.md:829, Phase 5 — M10: Admin Panel) [tu khoa: topic,tag] What's admin-exclusive vs shared with mod?
- QA-165 (qa-log.md:834, Phase 5 — M10: Admin Panel) [tu khoa: topic] AI toggle — single switch or per-module?
- QA-169 (qa-log.md:844, Phase 5 — M13: AI Layer) [tu khoa: topic] Which model for topic suggestion?
- QA-175 (qa-log.md:850, Phase 5 — M13: AI Layer) [tu khoa: topic] Timeout duration for AI calls?
- QA-178 (qa-log.md:853, Phase 5 — M13: AI Layer) [tu khoa: topic] Is there a dedicated AI rate limit system?
- QA-192 (qa-log.md:879, Phase 5 — M09 Amendment + M…) [tu khoa: theo dõi] ISS-143: Badge nên permanent hay revocable? Audit trail ra sao?
- QA-194 (qa-log.md:886, Phase 5 — M12: Gamification…) [tu khoa: chủ đề] ISS-REWD-01: Badge dựa trên tiêu chí gì — chỉ điểm, hay thêm số bài/chủ đề?
- QA-219 (qa-log.md:918, Phase 5 — M16: Chat & Messa…) [tu khoa: lớp] ISS-161: Rate limiting cho chat — có cần không, mức nào?
- QA-220 (qa-log.md:919, Phase 5 — M16: Chat & Messa…) [tu khoa: lớp,follow] ISS-162: Ai nhắn tin (DM) được cho ai — mở hoàn toàn, cần mutual follow, hay message request kiểu Messenger?
- QA-222 (qa-log.md:921, Phase 5 — M16: Chat & Messa…) [tu khoa: lớp,follow] ISS-164: Group Chat — quản trị ra sao (role, add/remove, kiểm duyệt, đổi tên, rời nhóm, kế nhiệm Admin, giới …
- QA-225 (qa-log.md:929, Phase 5 — M14: Feed & Disco…) [tu khoa: topic,tag,trending,follow] ISS-168: M14 Feed có những tab/view nào?
- QA-227 (qa-log.md:931, Phase 5 — M14: Feed & Disco…) [tu khoa: topic,tag,trending,follow] ISS-166: Guest (chưa đăng nhập) xem được gì trong Feed?
- QA-228 (qa-log.md:932, Phase 5 — M14: Feed & Disco…) [tu khoa: topic,tag,trending,follow] ISS-169: Tab Following rỗng (user chưa follow ai/gì) hiện gì?
- QA-230 (qa-log.md:934, Phase 5 — M14: Feed & Disco…) [tu khoa: follow] ISS-188: Tab Group hiện/ẩn theo điều kiện nào?
- QA-231 (qa-log.md:935, Phase 5 — M14: Feed & Disco…) [tu khoa: topic,trending,chủ đề] ISS-172: Trending Post có cần filter theo Topic không?
- QA-232 (qa-log.md:936, Phase 5 — M14: Feed & Disco…) [tu khoa: trending] ISS-173: Bài Group Public cross-post (DEC-111) có tính vào Newest/Trending Post không?
- QA-233 (qa-log.md:937, Phase 5 — M14: Feed & Disco…) [tu khoa: trending] ISS-173 (amend QA-232): phạm vi chính xác?
- QA-234 (qa-log.md:938, Phase 5 — M14: Feed & Disco…) [tu khoa: trending] ISS-174: Cơ chế phân trang cho cả 4 tab?
- QA-235 (qa-log.md:939, Phase 5 — M14: Feed & Disco…) [tu khoa: trending] ISS-175: Có ngưỡng tối thiểu (min upvote/comment) để vào Trending không?
- QA-236 (qa-log.md:940, Phase 5 — M14: Feed & Disco…) [tu khoa: trending] ISS-176: Trending có loại bài của user BANNED/HEAVY warn không?
- QA-239 (qa-log.md:943, Phase 5 — M14: Feed & Disco…) [tu khoa: follow] ISS-177 (amend): banner nên polling hay real-time (SSE)?
- QA-242 (qa-log.md:951, Phase 5 — M15: Analytics & …) [tu khoa: lớp,khối,grade] ISS-179: User Stats dashboard gồm những chỉ số nào?
- QA-243 (qa-log.md:952, Phase 5 — M15: Analytics & …) [tu khoa: topic] ISS-180: Content Stats dashboard gồm những chỉ số nào?
- DEC-128 (decisions.md:708, Phase 6 — Cross-cutting Con…) [tu khoa: tag] i18n/localisation scope
- DEC-132 (decisions.md:721, Phase 6 — Cross-cutting Con…) [tu khoa: topic,chủ đề] AI — Topic Suggestion hallucination handling
- DEC-133 (decisions.md:724, Phase 6 — Cross-cutting Con…) [tu khoa: topic] AI — raw output logging
- DEC-137 (decisions.md:741, Phase 7 prep — Tech Stack (…) [tu khoa: topic] Confirmed technology stack (closes OPEN-002)
- ISS-190 (issue-queue.md:290, Phase 6 — Cross-cutting Con…) [tu khoa: tag] i18n/localisation — site có cần hỗ trợ ngôn ngữ nào ngoài tiếng Việt không?
- ISS-194 (issue-queue.md:294, Phase 6 — Cross-cutting Con…) [tu khoa: topic,chủ đề] AI — Topic Suggestion (GPT-4o-mini) trả về ngoài danh sách 11 topic hợp lệ thì xử lý sao?
- ISS-195 (issue-queue.md:295, Phase 6 — Cross-cutting Con…) [tu khoa: topic] AI — có cần lưu log raw output (score Moderation, Topic suggestion) để audit/debug không?
- QA-249 (qa-log.md:963, Phase 6 — Cross-cutting Con…) [tu khoa: tag] ISS-190: i18n/localisation — site có cần hỗ trợ ngôn ngữ nào ngoài tiếng Việt không?
- QA-253 (qa-log.md:967, Phase 6 — Cross-cutting Con…) [tu khoa: topic,chủ đề] ISS-194: AI — Topic Suggestion (GPT-4o-mini) trả về ngoài danh sách 11 topic hợp lệ thì xử lý sao?
- QA-254 (qa-log.md:968, Phase 6 — Cross-cutting Con…) [tu khoa: topic] ISS-195: AI — có cần lưu log raw output (score Moderation, Topic suggestion) để audit/debug không?
- QA-256 (qa-log.md:975, Phase 7 prep — Tech Stack (…) [tu khoa: lớp] ISS-197: Tech stack — Backend/Frontend framework, và có cần SSR/SEO ở MS1 không?
- QA-258 (qa-log.md:977, Phase 7 prep — Tech Stack (…) [tu khoa: lớp] ISS-199: Email — thư viện và nguồn SMTP gửi mail?

## CROSS-CUTTING index (41 muc, chua nhac module) - doc lai tieu de, chon muc ap dung cho M05

- DEC-127 (decisions.md:705) Timezone & date handling
- DEC-129 (decisions.md:711) Data retention — audit log & chat messages (general hard-delete principle)
- DEC-130 (decisions.md:715) File/media upload — no virus/malware scanning
- DEC-131 (decisions.md:718) AI — third-party data privacy disclosure
- DEC-134 (decisions.md:732) Backend/Frontend stack and SSR deferral
- DEC-135 (decisions.md:735) Realtime channel — SSE only
- DEC-136 (decisions.md:738) Email delivery — Spring Mail over standard SMTP
- DEC-138 (decisions.md:749) Consent to Privacy Policy/ToS is mandatory at registration
- ISS-189 (issue-queue.md:289) Timezone & date handling — lưu trữ/tính toán theo múi giờ nào?
- ISS-191 (issue-queue.md:291) Data retention tổng quát — audit log và chat message có cần policy xóa/lưu trữ gì không?
- ISS-192 (issue-queue.md:292) File/media upload — có cần cơ chế scan virus/malware không?
- ISS-193 (issue-queue.md:293) AI — nội dung user gửi ra OpenAI (3rd party) có cần xử lý gì về privacy không?
- ISS-196 (issue-queue.md:296) Analytics events — có cần hạ tầng event-tracking chung (ngoài 3 dashboard M15) không?
- ISS-197 (issue-queue.md:302) Tech stack — Backend/Frontend framework, và có cần SSR/SEO ở MS1 không?
- ISS-198 (issue-queue.md:303) Kênh realtime — thống nhất SSE hay giữ WebSocket cho thông báo?
- ISS-199 (issue-queue.md:304) Email — thư viện và nguồn SMTP gửi magic-link / OTP / thông báo bảo mật?
- ISS-200 (issue-queue.md:305) Cờ `AI_ENABLED` (DEC-008) — lưu ở đâu: env var hay Admin config?
- ISS-201 (issue-queue.md:306) Hosting / deployment cho MS1
- ISS-202 (issue-queue.md:307) Ràng buộc học thuật về công nghệ (đóng ISS-029)
- ISS-203 (issue-queue.md:308) Xác nhận nhóm công nghệ ngầm định (PostgreSQL+pgvector, Cloudinary, OpenAI, Tiptap, JWT)
- ISS-204 (issue-queue.md:314) Đăng ký tài khoản có bắt buộc đồng ý Privacy Policy/ToS không, và privacy xây dựng thế nào?
- ISS-206 (issue-queue.md:321) Quy ước ID cho tài liệu SR
- QA-248 (qa-log.md:962) ISS-189: Timezone & date handling — lưu trữ/tính toán theo múi giờ nào?
- QA-250 (qa-log.md:964) ISS-191: Data retention tổng quát — audit log và chat message có cần policy xóa/lưu trữ gì không?
- QA-251 (qa-log.md:965) ISS-192: File/media upload — có cần cơ chế scan virus/malware không?
- QA-252 (qa-log.md:966) ISS-193: AI — nội dung user gửi ra OpenAI (3rd party) có cần xử lý gì về privacy không?
- QA-255 (qa-log.md:969) ISS-196: Analytics events — có cần hạ tầng event-tracking chung (ngoài 3 dashboard M15) không?
- QA-257 (qa-log.md:976) ISS-198: Kênh realtime — thống nhất SSE hay giữ WebSocket cho thông báo?
- QA-259 (qa-log.md:978) ISS-200: Cờ `AI_ENABLED` lưu ở đâu?
- QA-260 (qa-log.md:979) ISS-201: Hosting / deployment ở MS1?
- QA-261 (qa-log.md:980) ISS-202 (đóng ISS-029): Có ràng buộc học thuật nào về công nghệ không?
- QA-262 (qa-log.md:981) Phase 8 (Data model) — cách tiếp cận và độ sâu?
- QA-263 (qa-log.md:982) ISS-203: Xác nhận nhóm công nghệ ngầm định?
- QA-264 (qa-log.md:988) ISS-204: Có yêu cầu đồng ý Privacy Policy/ToS khi đăng ký không, và privacy xây dựng thế nào?
- QA-266 (qa-log.md:995) ISS-206: Quy ước ID cho tài liệu SR?
- OPEN-001 (open-issues.md:9) AI cost & budget chưa chốt chính thức (ISS-026) — hiện estimate <$0.01, recommend $5 OpenAI credit,…
- OPEN-002 (open-issues.md:10) Tech stack chưa quyết định (ISS-029) — ảnh hưởng đến academic constraints và AI provider choice
- OPEN-003 (open-issues.md:11) Chat (M16) — chưa có cơ chế Block hoặc Report cho tin nhắn ở MS1 (ISS-160) — quyết định defer có ch…
- OPEN-004 (open-issues.md:12) Analytics & Stats (M15) — chưa có export CSV cho 3 dashboard ở MS1 (ISS-184) — quyết định defer có …
- OPEN-005 (open-issues.md:13) Cross-cutting (Phase 6) — chưa xây hạ tầng event-tracking chung (ISS-196) — quyết định defer có chủ…
- OPEN-007 (open-issues.md:15) UI Kit (ISS-197, DEC-134) — thư viện nền chưa chốt; stakeholder nghiêng về MUI nhưng phải đợi có de…

## DRAFT hits (33)

| File | Dong | Muc | So lan khop |
|---|---|---|---|
| iShare_specs_general.md | 5-12 | 1. iShare là gì | 1 |
| iShare_specs_general.md | 18-29 | 3. Phạm vi nội dung | 9 |
| iShare_specs_general.md | 30-45 | 4. Bản đồ module | 5 |
| iShare_specs_general.md | 46-57 | 5. Nguyên tắc thiết kế cốt lõi | 6 |
| iShare_specs_general.md | 58-71 | 6. Phạm vi AI (bắt buộc triển khai) | 3 |
| iShare_specs_general.md | 72-78 | 7. Kiến trúc tổng quan | 1 |
| iShare_specs_general.md | 79-84 | 8. Quyết định phạm vi — Không làm (đã cân nhắc, có lý do) | 1 |
| iShare_modules.md | 15-28 | 1.2 Profile | 4 |
| iShare_modules.md | 51-91 | 2.1 Post | 4 |
| iShare_modules.md | 109-123 | 2.4 Post Type – Optional | 2 |
| iShare_modules.md | 124-125 | 3. Topic / Tag / Lớp-Khối Module | 4 |
| iShare_modules.md | 126-131 | 3.1 Topic / Category | 2 |
| iShare_modules.md | 132-152 | 3.2 Tag | 6 |
| iShare_modules.md | 153-162 | 3.3 Lớp / Khối | 12 |
| iShare_modules.md | 163-173 | 3.4 Quan hệ | 4 |
| iShare_modules.md | 176-189 | 4.1 Post Star | 1 |
| iShare_modules.md | 247-264 | 4.5 Follow / Quan tâm | 6 |
| iShare_modules.md | 323-332 | 7.1 Feed | 6 |
| iShare_modules.md | 333-342 | 7.2 Trending / Popular | 1 |
| iShare_modules.md | 343-354 | 7.3 Search | 4 |
| iShare_modules.md | 355-368 | 7.4 Filter / Sort | 4 |
| iShare_modules.md | 371-385 | 8.1 Notification Event | 5 |
| iShare_modules.md | 426-441 | 9.3 User Statistics | 2 |
| iShare_modules.md | 470-486 | 9.5 System Statistics | 2 |
| iShare_modules.md | 489-514 | 10.1 Report | 1 |
| iShare_modules.md | 551-554 | 11. AI Assistance Module (toàn bộ bắt buộc) | 1 |
| iShare_modules.md | 581-601 | 11.2 AI Content Classification | 4 |
| iShare_modules.md | 630-658 | 11.5 Feedback / Evaluation Loop | 1 |
| iShare_modules.md | 661-690 | Trong phạm vi | 7 |
| iShare_modules.md | 708-743 | 13. Kiến trúc tổng thể | 4 |
| iShare_dev_priority.md | 9-21 | 2. Priority Tags — nghĩa là thứ tự triển khai, không phải mức độ có thể cắt | 2 |
| iShare_dev_priority.md | 24-76 | Giai đoạn 1 — `[P0]` | 11 |
| iShare_dev_priority.md | 77-100 | Giai đoạn 2 — `[P1]` | 8 |
