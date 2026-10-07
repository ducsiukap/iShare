# Decision Log

> Decisions taken during the interview, with options considered and rationale.
> Format: DEC-### | Decision | Options considered | Rationale | Who decided

| ID | Decision | Options considered | Rationale | Decided by |
|---|---|---|---|---|
| DEC-001 | No Teacher account type | A: Teacher role / B: No distinction | Too few teachers for meaningful leaderboard; doubles Reward system cost for a 2-person team | Stakeholder (in draft) |
| DEC-002 | Messaging: text-only, no file/voice/video | A: Full media / B: Text-only | WebRTC/media server out of scope for 2-person team | Stakeholder (in draft) |
| DEC-003 | Group reuses Forum mechanism (no rebuild) | A: Separate Post table / B: Shared + group_id | Avoids duplication, consistent behavior | Stakeholder (in draft) |
| DEC-004 | Post Star ≠ Comment Star (separate weights) | A: Unified star / B: Separate | Prevents spam-comment-to-farm-reputation | Stakeholder (in draft) |
| DEC-005 | AI as support layer only — no autonomous decisions on sensitive cases | A: Full auto / B: Human-in-the-loop | AI quality unpredictable; trust requires human oversight | Stakeholder (in draft) |
| DEC-006 | All 5 AI features are mandatory (not optional) | A: Only AI Moderation / B: All 5 | Product differentiator; thesis requirement | Stakeholder (updated draft) |


---

### DEC-007
- **ID:** DEC-007
- **Title:** Super Admin Pattern — ADMIN có thể promote user khác lên ADMIN
- **Decision:** Hệ thống áp dụng super admin pattern: 1 root ADMIN được seed từ DB (không qua UI đăng ký); ADMIN có thể promote/demote user thành ADMIN khác qua giao diện quản trị. Dev team giữ root credential, bàn giao operational admin cho client sau MS1 qua flow trong UI.
- **Source:** QA-009 / ISS-028
- **Rationale:** Cho phép bàn giao vận hành linh hoạt mà không cần dev team can thiệp DB. Production-ready từ đầu.

---

### DEC-008
- **ID:** DEC-008
- **Title:** AI Layer Feature Flag — global toggle on/off
- **Decision:** Hệ thống có global toggle `AI_ENABLED` (Admin config UI hoặc env var ở deploy level). Mỗi module có fallback rõ ràng khi AI tắt: M06 Search → full-text keyword; M08 Moderation → manual queue only; M05 Topic → user tự chọn topic, không có gợi ý. Tech stack lưu flag defer sang Phase 8 (OPEN-002). **[Clarified: nơi lưu/đổi flag đã được giải quyết bởi DEC-092/093 — Admin Panel (M10) có System config gồm AI master + per-module toggle; flag lưu bền (DB) để đổi lúc đang chạy, không cần redeploy. Không có quyết định mới — ISS-200/QA-259]**
- **Source:** QA-024 / ISS-042
- **Rationale:** Hệ thống phải hoạt động độc lập khi AI off (per DEC-005). Feature flag cho phép toggle linh hoạt mà không cần redeploy.

---

### DEC-009
- **ID:** DEC-009
- **Title:** Anonymous Post — Group-level toggle, not system-level
- **Decision:** Anonymous posting được bật/tắt ở cấp Group bởi Group Owner (không phải per-post toggle cho mọi user). Khi toggle bị tắt, chỉ áp dụng cho post mới (existing anonymous posts giữ nguyên). Feature này thuộc M11 (Group), không phải M03 (Post). Removed F-POST-05 from M03; added F-GRP-10 in M11.
- **Source:** QA-025 / ISS-043 (partial) / ISS-GRP-01
- **Rationale:** Anonymous post gắn liền với context Group; không phải feature của Post độc lập. Toggle ở Group Owner level đảm bảo kiểm soát cộng đồng rõ ràng.

---

### DEC-010
- **ID:** DEC-010
- **Title:** Account Linking — Auto-link by verified Google email
- **Decision:** Khi user đăng nhập bằng Google OAuth, hệ thống tự động link account nếu email Google khớp với email đã đăng ký (verified). Notification được gửi sau khi link thành công. Không cần manual confirmation.
- **Source:** QA-026 / ISS-043
- **Rationale:** Đảm bảo đồng nhất account, tránh duplicate. Auto-link là practice phổ biến (Google, GitHub, Facebook đều làm vậy với verified email).

---

### DEC-011
- **ID:** DEC-011
- **Title:** Post Soft Delete — 7-day recovery window
- **Decision:** Post bị xóa sử dụng soft delete: set `deleted_at` timestamp, `publish_state = 'deleted'`. Cron job hard-delete sau 7 ngày. User có thể khôi phục trong 7 ngày nếu mod chưa removed. Sau 7 ngày không thể khôi phục.
- **Source:** QA-027 / ISS-044
- **Rationale:** 7 ngày đủ để user nhận ra lỡ tay xóa mà không tích lũy data rác lâu dài.

---

### DEC-012
- **ID:** DEC-012
- **Title:** Post Status Model — 3 independent fields
- **Decision:** Post status được tách thành 3 trường độc lập: `publish_state` (draft/published/deleted — user controls), `mod_state` (pending/active/under_review/removed — system/mod controls), `lock_level` (none/author/mod — author locks comments; mod can also lock). Author có thể lock comments của bài mình; Mod có quyền lock thêm. User không tự xóa bài — chỉ set `publish_state=deleted`; Mod set `mod_state=removed` để kiểm soát nội dung.
- **Source:** QA-028, QA-029 / ISS-044
- **Rationale:** Separation of concerns rõ ràng. Tránh trạng thái xung đột. Pattern theo Discourse/Reddit.

---

### DEC-013
- **ID:** DEC-013
- **Title:** Content Scan Policy — Pre-scan new posts, background re-scan edits
- **Decision:** Post mới → pre-scan (ẩn với public cho đến khi AI scan xong, `mod_state=pending`). Edit post → background re-scan (không ẩn, nếu flagged thì chuyển `under_review`). AI off → bypass scan, post active ngay. Không retroactive scan khi AI re-enable (Option C: chỉ scan post mới từ đó trở đi).
- **Source:** QA-030, QA-031 / ISS-044
- **Rationale:** Platform phục vụ học sinh — pre-scan cần thiết để kiểm soát nội dung. Edit pre-scan gây UX tệ cho đã-vetted content. Retroactive scan khi re-enable gây burst load không kiểm soát được.

---

### DEC-014
- **ID:** DEC-014
- **Title:** Registration Flow — 3-step progressive onboarding
- **Decision:** Step 1: email + password. Step 2: verify email (magic link, 1h, mandatory). Step 3: setup username (required) + display_name (required) + bio/grade_level/avatar (optional, skippable). Google OAuth: skip Step 1+2, display_name auto-fill, must set username at Step 3. Login gate: redirect to last incomplete step.
- **Source:** QA-048, QA-049, QA-053 / ISS-054
- **Rationale:** Minimal friction at registration (2 fields), defer identity setup post-verify. Google OAuth already verified email so steps collapse.

---

### DEC-015
- **ID:** DEC-015
- **Title:** Identity Fields — display_name (free, not unique) + username (unique, for @mention)
- **Decision:** `display_name`: free-form, any style (nickname/full name/creative), NOT unique. `username`: unique, alphanumeric + underscore, min 3 / max 20 chars — used ONLY for @mention trigger and search, never displayed as primary identity. Display_name shown everywhere; username shown muted in mention dropdown.
- **Source:** QA-050, QA-051, QA-052 / ISS-054
- **Rationale:** Forum community norm (free display name) + mention usability (unique handle without spaces).

---

### DEC-016
- **ID:** DEC-016
- **Title:** Email flows — verify (1h) + forgot password (15min) + change password (in-app)
- **Decision:** Verify email: magic link 1h, manual resend (banner), 60s cooldown. Forgot password: magic link 15min → revoke all other sessions → auto-login new session. Change password (Settings, logged in): old+new+confirm, no session revoke. Google OAuth accounts: no password flow — show redirect message.
- **Source:** QA-049, QA-059, QA-060, QA-061 / ISS-054, ISS-056
- **Rationale:** Reset = security event (revoke); change = normal update (no revoke). 15min for reset = tighter security window.

---

### DEC-017
- **ID:** DEC-017
- **Title:** Session Management — JWT + rotating refresh token, multi-device allowed
- **Decision:** JWT (stateless). Access token 1 hour. Refresh token 30 days, rotating (new token each use, old invalidated). `refresh_tokens` table in PostgreSQL. Multi-device: allowed — each device independent JWT + SSE connection. SSE pub/sub naturally handles multi-device (multiple SSEConnections per user in Set).
- **Source:** QA-057, QA-058 / ISS-055
- **Rationale:** JWT simple for thesis scale. Rotating refresh token adds security without Redis overhead. Multi-device doesn't complicate SSE architecture.

---

### DEC-018
- **ID:** DEC-018
- **Title:** Account State Machine — account_state (4) + verify_level (3)
- **Decision:** Two separate fields: `account_state` ENUM('ACTIVE','DEACTIVATED','DELETED','BANNED') DEFAULT 'ACTIVE'; `verify_level` ENUM('NONE','EMAIL_VERIFIED','SETUP_COMPLETED') DEFAULT 'NONE'. Login gate checks account_state first (BANNED/DELETED → block), then verify_level (redirect to appropriate step). Google OAuth starts at EMAIL_VERIFIED.
- **Source:** QA-062 / ISS-057
- **Rationale:** Separation of concerns: lifecycle state vs onboarding progress. Cleaner than single expanded ENUM.

---

### DEC-019
- **ID:** DEC-019
- **Title:** Deactivation — 14-day window, post hidden, comment tombstone, auto-delete
- **Decision:** No direct delete — user must deactivate first. Window: 14 days → auto-DELETED. Posts: hidden (URL → "Nội dung không tồn tại"). Comments: content visible, author → "Tài khoản tạm thời vô hiệu hoá", avatar → placeholder. After auto-DELETED: comments → "[Người dùng đã xóa]", PII wiped. BANNED screen: reason + appeal time + appeal button (if within window) + OK.
- **Source:** QA-063, QA-064, QA-065, QA-066 / ISS-057
- **Rationale:** Posts are standalone → safe to hide. Comments are part of others' threads → tombstone preserves thread integrity. 14 days sufficient for accidental deactivation recovery.

---

### DEC-020
- **ID:** DEC-020
- **Title:** @Mention System — search both fields, priority tiers, atomic node
- **Decision:** Trigger: @ + min 1 char, debounce 300ms, spaces allowed in query. Search: pg_trgm on display_name AND username. Priority (Group): following > same group > global. Priority (Post, no group): following > common group > global. Dropdown: top 5. Each item: avatar + display_name + @username (muted). Render: display_name + brand highlight (no @ shown). Stored: user_id (auto-updates on name change). Node atomic: no trim/edit label.
- **Source:** QA-054, QA-055, QA-056 / ISS-054
- **Rationale:** pg_trgm handles Vietnamese names + spaces naturally. Priority tiers surface relevant people first. Atomic node prevents misrepresentation via label editing.

---
## Phase 5 — M02: User Profile

### DEC-021: Avatar upload
- CDN: Cloudinary (backed by AWS S3)
- Allowed types: JPEG, PNG, WebP only (no animated GIF)
- Max size: 5 MB
- On upload: old avatar deleted from CDN
- Display: circular crop rendered by UI; original stored

### DEC-022: Bio field
- DB: VARCHAR(255)
- UI character limit: 155 chars (live counter)
- Optional; empty bio renders nothing

### DEC-023: Profile URL
- Route: `/u/{username}`, dual-context
- Owner: Edit Profile button, tabs = Posts + Bookmarks
- Visitor: read-only, tabs = Posts only
- Conditional on `request.user === profile.user`

### DEC-024: Profile content tabs
- Owner: Posts | Bookmarks (default: Posts)
- Visitor: Posts only

### DEC-025: Followers / Following display
- Count shown on profile
- Full list public (no privacy restriction)

### DEC-026: Username change history
- NOT displayed on profile — no history table in v1

### DEC-027: Social links
- DROPPED for v1 — future extension
- Concerns: malicious links, off-platform traffic

### DEC-028: Points + badges on profile
- Display only; M12 handles logic/calculation

---
## Phase 5 — M03: Post & Content

### DEC-029: Tiptap editor extensions
Bold, italic, underline, strikethrough, highlight; Heading H1–H3; Bullet/numbered/task list; Inline code + code block (syntax highlight); LaTeX/KaTeX (raw input, no visual editor v1); Table; Blockquote; Horizontal rule; Link with custom label. No inline image.

### DEC-030: Post structure
- 1 post type (no post_type field)
- Fields: title, content_json (ProseMirror JSON), content_text (plain text for search)
- Optional poll (separate table), attachment section below body

### DEC-031: publish_state machine
DRAFT | PENDING | PUBLISHED | HIDDEN | REJECTED | DELETED
- DRAFT: composing, not submitted
- PENDING: submitted, under AI scan or mod review
- PUBLISHED: public
- HIDDEN: author self-hide (reversible)
- REJECTED: mod rejected, author can fix and resubmit
- DELETED: soft delete, 7-day recovery window

### DEC-032: mod_state
NORMAL | FLAGGED | HIDDEN
- FLAGGED: AI/report flagged, awaiting mod
- HIDDEN: mod-hidden, author cannot self-unhide, must appeal (M09)

### DEC-033: lock_level + locked_by
- lock_level: NONE | COMMENT_LOCKED | FULLY_LOCKED
- COMMENT_LOCKED: author OR mod can set (blocks new comments)
- FULLY_LOCKED: mod only (blocks comments + reactions)
- locked_by: NULL | AUTHOR | MOD — if MOD, author cannot override
- Visibility rule: publish_state=PUBLISHED AND mod_state=NORMAL

### DEC-034: Pre-scan flow
Submit → PENDING → AI scan → clean: PUBLISHED; flagged: stay PENDING → mod review → approve: PUBLISHED | reject: REJECTED + reason → author resubmit → PENDING

### DEC-035: Attachments
- Images (JPEG/PNG/WebP): 5MB/file, max 10 files
- Documents (PDF/DOCX/XLSX/PPTX): 20MB/file, max 3 files
- CDN: Cloudinary (same as avatar)
- Avatar size updated to 5MB (see DEC-021)

### DEC-036: Poll (table: polls, FK → posts)
- Optional, max 1 per post; options min 2 max 10
- Owner config: allow_change_vote, allow_multiple (if true: select up to all options), show_result_before_vote (default false)
- expires_at: NOT NULL (required)
- is_closed: boolean — force-close early; extend by updating expires_at
- Once closed: cannot reopen
- After close: always show result % regardless of show_result_before_vote

### DEC-037: Edit history
- Post: full history in post_edits table; public badge "(đã chỉnh sửa)" + "Xem lịch sử"
- Comment: edited_at timestamp only; badge "(đã chỉnh sửa)"; no history UI

### DEC-038: Soft delete
- DELETED: hidden from feed
- 7-day window: author can recover → PUBLISHED (tab "Đã xóa" on profile)
- After 7 days: cron job hard deletes

---
## Phase 5 — M04: Comment

### DEC-039: Comment editor extensions
Bold, italic, inline code, LaTeX/KaTeX, link, @mention, blockquote (for quote-reply). No heading, table, task list, attachments.

### DEC-040: Threading model
2 levels only — root comment + child replies. Reply to child → appended to same thread (no deeper nesting). @mention used for context when replying to a specific child.

### DEC-041: Reactions
Upvote only — no downvote/dislike. Bad content → report (M08).

### DEC-042: Comment sort
- Top (default): by upvotes
- Mới nhất: newest first
- Cũ nhất: oldest first
Child replies always sort chronological (oldest first) regardless of filter.

### DEC-043: Edit/Delete
- Edit: author can edit anytime, no time limit; badge "(đã chỉnh sửa)" shown
- Delete: permanent (no soft delete, no recovery window)
- Root with replies → tombstone "[Bình luận đã bị xóa]"; replies remain
- Root without replies → hard delete
- Child → hard delete; replies of child show "reply to [bình luận đã bị xóa]"

### DEC-044: Attachments
Not supported in comments. Share files via post instead.

### DEC-045: @Mention + Notification
@mention uses shared M01 logic. Always triggers notification regardless of mention location (post or comment).

### DEC-046: Quote-reply
Click Reply → editor auto-inserts blockquote with original content + author name. Uses Tiptap blockquote extension.

---
## Phase 5 — M05: Topic & Tag

### DEC-047: Topic vs Tag
- Topic: structured taxonomy, AI suggest + user confirm, used for filter/browse. Flat structure (nested deferred).
- Tag: free-form #hashtag, user-typed, no fixed list, no spaces.

### DEC-048: Topic list (11, final)
Toán học, Ngữ văn, Ngoại ngữ, Khoa học tự nhiên (Lý/Hóa/Sinh), Khoa học xã hội (Sử/Địa/KT&PL), Tin học, Kỹ năng mềm, Hướng nghiệp, Nghệ thuật & Sáng tạo, Góc Chill, Khác

### DEC-049: Topic rules
- Min 1, max 3 topics/post (mandatory)
- Mod/admin: edit (rename) + merge. No delete.
- Merge auto re-points post_topics from source to target

### DEC-050: AI suggest topic flow
- "Gợi ý topic" button (not automatic) → AI analyzes text only (title + content_text, no attachment processing) → suggest max 3 topics, pre-ticked
- Content <20 words → no suggestion, shown "content too short"
- User adjusts freely → publish
- Content changed after suggest → flag is_stale, soft warning + re-suggest button, does not block publish
- Feedback (AI suggest vs final selection) only recorded when not stale
- User manually picks topic from start → skips AI flow entirely
- AI off → user picks from dropdown, no suggest

### DEC-051: Tag data model + rules
- Tables: tags (id, name unique lowercase-normalized, created_at — no created_by) + post_tags junction
- Auto-created, no approval
- Max 5 tags/post, max 30 chars/tag
- Fully free — mod/admin do NOT edit/merge/delete under normal conditions
- Crisis case: mod/admin soft-delete (is_active=false) → hidden from autocomplete/trending/browse; old posts keep post_tags record but tag chip hidden from display; if user retypes a disabled tag name, it's NOT tagified — rendered as plain text

### DEC-052: Trending (Topic + Tag)
- Rolling 7-day window (sliding from now, unlike leaderboard's fixed calendar week)
- Recalculated every 15-30 min (cached, not live query)
- Score: Σ(1 + upvotes×2 + comments×1) across all posts in window
- To be integrated as a dedicated Feed section (note for M14)

---
## Phase 5 — M06: Search

### DEC-053: Search scope (final, supersedes Phase 3 ISS-040 partial scope)
- Post: semantic search via embedding (pgvector)
- User: exact/prefix match on display_name + username (pg_trgm, shared with M01 @mention)
- Tag: exact/prefix match (pg_trgm)
- Topic: exact/prefix match (pg_trgm)
- Group: exact/prefix match (pg_trgm); visible-but-gated for private groups (name+description shown, content gated per M11)
- Comment: NOT searchable (too many, low value)
- Fallback: full-text (Postgres FTS) when AI off

### DEC-054: Search trigger
- Post (semantic): submit-only (Enter/click), no debounce — expensive compute
- User/Tag/Topic/Group: debounce (300ms live suggestion) + also works on submit

### DEC-055: Ranking (Post search)
```
relevance_score = cosine similarity from embedding, normalized 0-1
engagement_raw = log(1+upvotes)×2 + log(1+comments)×1
engagement_score = normalize(engagement_raw) to 0-1 within candidate set
final_score = relevance_score × 0.8 + engagement_score × 0.2
```
Top N candidates by relevance first (vector search), then re-rank by final_score.

### DEC-056: Filters (Post search)
Topic, Tag, date range (Today/This week/This month/All), Following-only toggle, Sort (Relevance default / Newest / Most upvoted)

### DEC-057: Full-text fallback + Vietnamese diacritics
- Postgres FTS: tsvector/tsquery
- unaccent extension strips Vietnamese diacritics before indexing (solves "tìm không dấu")
- pg_trgm for prefix/fuzzy match on Tag/User/Topic/Group
- Generated column: content_search = to_tsvector('simple', unaccent(title || ' ' || content_text))

### DEC-058: Autocomplete (debounce dropdown)
Shows User/Tag/Topic/Group prefix matches only (pg_trgm). No Post title suggestions (Post is submit-only).

### DEC-059: Search history
localStorage only (no DB). Max 10 recent searches. Shown on search box focus. "Clear history" button.

### DEC-060: Results display
Mixed, single scrollable page (no tabs). Post results are primary (by final_score). User/Tag/Topic/Group shown as supplementary (max 3 each, sidebar/bottom).

### DEC-061: Snippet
No keyword highlighting. Plain snippet, first ~150 chars of content_text. Same approach for both semantic and full-text modes.

### DEC-062: Search permission
- Guest: search normally (same as public browse)
- Private group content (posts): only shown if searcher is a member of that group
- Private group entity (name/description): visible-but-gated — shows in Group search results regardless of membership (per M11), but content inside stays gated

### DEC-063: Rate limiting
| | Debounce | Submit search |
|---|----------|----------------|
| Guest (by IP) | 30/min | 10/min |
| User (by user_id) | 45/min | 20/min |
429 Too Many Requests when exceeded, no captcha/long-term block.

### DEC-064: Pagination
Infinite scroll, 15 results/load, max 120 total results (8 loads), cursor-based (not offset). Beyond max: "Thu hẹp tìm kiếm để có kết quả chính xác hơn"

---
## Phase 5 — M07: Notification

### DEC-065: Notification event list + channel
| Event | In-app | Email |
|-------|--------|-------|
| Password changed | Yes | Yes |
| DEACTIVATED auto-delete warning | No (can't login) | Yes |
| New follower | Yes | No |
| Post published/rejected/hidden/poll ended | Yes | No |
| Upvote (post + comment), batched | Yes | No |
| New comment / reply / @mention | Yes | No |
| Report result / warning received | Yes | No |
| Ban/unban | Yes | Yes |
| Appeal — ban-related | Yes | Yes |
| Appeal — post/comment/warn-related | Yes | No |
| Group: invite/join/approve/promote/kick | Yes | No |
| Badge / point milestone / weekly top | Yes | No |
| DM / Group chat message | Yes | No |
Email limited to: security (password change), account-deletion warning, ban/unban, ban-related appeals only. No digest email.

### DEC-066: Upvote notification batching
Batch upvotes (post + comment) within a 5-minute rolling window into one notification ("A và N người khác đã upvote..."). Single upvote shows the voter's name directly.

### DEC-067: In-app notification UI
- Bell icon: dropdown (5-10 most recent) + dedicated page /notifications (full list)
- Separate Message icon (navbar): DM + Group chat, own unread badge, links to Chat inbox — NOT mixed with bell
- Mark read: click item → auto mark read + navigate; "Mark all as read" button

### DEC-068: Email delivery architecture
Event → write to email_queue table → cron scans every 1 minute → sends. Async, no blocking, no message broker needed for v1 scope.

### DEC-069: In-app delivery architecture
Event → write to notifications table (source of truth) → best-effort WebSocket push to online clients. No cron/retry needed for in-app — client fetches unread from DB on page load/bell click regardless of WebSocket push success. [Amended: thông báo dùng SSE thay WebSocket — DEC-135/QA-257]

### DEC-070: Notification preferences — no global category toggle
No granular global preference settings page for v1. Instead:
- Per-post mute: toggle on each post ("Tắt thông báo cho bài này") mutes comment/reply/upvote notifications from that post specifically. @Mention still fires even when post is muted (deliberate address to user).
- Per-conversation mute (Chat): mute individual DM/Group chat threads.
- Global chat toggle: "Tắt thông báo cho toàn bộ Chat" setting, mutes all DM+Group chat notifications; coexists with per-conversation mute for finer override.

### DEC-071: Notification retention
No auto-deletion / no retention policy — notifications kept indefinitely, consistent with Facebook/Twitter/Discord/GitHub approach. No cron cleanup.

---
## Phase 5 — M08: Moderation

### DEC-072: Report entities + reasons
- Post (8): Spam/Quảng cáo, Nội dung sai/hiểu nhầm, Đạo văn/Vi phạm bản quyền, Quấy rối/Bắt nạt, Ngôn từ thù ghét/Phân biệt, Nội dung người lớn/Không phù hợp, Bạo lực/Đe dọa, Khác
- Comment (7): same minus Đạo văn
- User (2): Quấy rối/Bắt nạt có hệ thống, Khác
- Group (4): Nội dung người lớn/Không phù hợp, Group giả mạo, Quấy rối/Bắt nạt có hệ thống, Khác
- Only logged-in users can report (no guest reporting)

### DEC-073: Report submission
- Evidence: max 3 images, 5MB/file (shared with platform image limit)
- Description text: optional, REQUIRED only when reason = "Khác"

### DEC-074: Report outcome notification (split by recipient)
- Reporter: vague outcome only ("đã xử lý — nội dung vi phạm đã gỡ/ẩn" or "không phát hiện vi phạm"), never sees punishment details of reported user
- Reported/offending user: detailed — resolution_reason, punishment level (warning level or ban), link to Appeal (M09)

### DEC-075: Report queue mechanics
- Priority score = MAX(severity_weight across reasons in case) + report_count × 2
- Claim-based assignment: mod clicks "Nhận xử lý" to lock a case; auto-unlock after 30 min inactivity
- No SLA deadline, processed by priority order

### DEC-076: Report grouping (case model)
- Group by (target_type, target_id) while status=OPEN into one "case"; each individual report row keeps its own data (reporter_id, reason, evidence, description)
- Case resolved → all open reports under it move to RESOLVED together; reporter notifications sent to all reporters in case (same generic outcome)
- New report on an already-RESOLVED target → opens a NEW case (no reopening), but mod sees full report history (past cases + outcomes) for that target as context
- Mod sets `resolution_reason` independently when resolving — mod's own determination, not necessarily matching reporters' stated reasons
- report status: OPEN → RESOLVED (action_taken | dismissed)

### DEC-077: Comment AI scan (post-scan, velocity-triggered)
- Unlike Post's pre-scan (blocks publish), Comment publishes immediately, no default scan
- Trigger: reply velocity crosses threshold within a sliding time window (exact numbers TBD, needs real usage data to tune) — e.g. placeholder "10 replies in 5 min"
- On trigger: scan entire thread (root + all replies) not yet scanned with current content version
- Re-trigger: velocity threshold crossed again AND content not yet scanned with current version (edit alone does not trigger — waits for next velocity trigger)
- If AI flags → comment auto-hidden (author only sees it) + pushed into report queue for mod review
- Report system works independently of velocity/scan status at all times

### DEC-078: Warning issuance mechanism
- AI high confidence → auto-issues warning directly, no mod involved (user can appeal via M09 if wrong)
- AI low confidence/borderline → escalates to mod queue, mod manually decides
- Mod can also independently issue warning when resolving a report case
- Ban always requires human (MOD/ADMIN) — AI never auto-bans, regardless of confidence

### DEC-079: Warning levels + probation (updated durations + restrictions)
| Level | Warns | Probation | Restriction |
|-------|-------|-----------|-------------|
| LIGHT | 1-2 | 7 days (was 5) | None — tracking window only |
| MEDIUM | 3-4 | 10 days | Cannot create new posts; comments OK |
| HEAVY | 5-6 | 15 days (was 14) | Cannot create posts or comments (read/vote only); existing content search-downranked ×0.5 |
Warning status is fully PRIVATE — visible only to the user themselves and to mods; never shown publicly on posts/comments/profile (prevents bullying of warned students).

> **AMENDED by DEC-118 and DEC-122 (Phase 5, M12):** the private scope above is narrowed by one deliberate, explicit public exception — a user at HEAVY warning level, or a BANNED user, is excluded from the public leaderboard for the duration of that state. This is the only public-facing consequence carved out of DEC-079's privacy guarantee; LIGHT/MEDIUM warn levels remain unaffected, and for BANNED users specifically, their profile/post/comment content stays visible as normal (see DEC-122) — only leaderboard eligibility is affected.

### DEC-080: Ban types + escalation
- Temporary ban (auto-escalating): 1st ban = 30 days, 2nd ban = 90 days, 3rd+ ban = permanent
- Permanent ban (manual): mod/admin can directly issue for severe first-offense violations, bypassing escalation
- Auto-ban trigger: user violates again while already at HEAVY warning level (warn #7+) → escalates to ban instead of another warning cycle
- 2 separate mod UI actions: "Ban" (auto-escalating duration) vs "Ban vĩnh viễn" (manual permanent override)
- Both always require MOD/ADMIN — never AI-triggered

### DEC-081: Moderation audit log
- Log fields: actor_id (mod/AI), action_type (warn/ban/hide/resolve), target_id, reason, timestamp
- Admin: full audit log access, all mods, all actions
- Mod (default): sees only their own resolved case list
- Mod (appeal review exception): can see another mod's action details specifically when reviewing an appeal referencing that action (per QA-021 policy)

### DEC-082: False/malicious report handling
- No automated punishment — false positives risk discouraging legitimate reporting
- Metric shown to mod as reference: target_concentration = (dismissed reports targeting the same single target) / (total resolved reports by that reporter), calculated over reports resolved in the last 90 days
- High concentration = signal of targeted harassment via report system (not honest mistake, which shows spread-out low-concentration pattern)
- Mod uses judgment to manually issue warning to abusive reporter via existing warning mechanism — no separate automated system

### DEC-083: Comment schema update (M04 cross-reference, added during M08 deep dive)
Comment needs a `mod_state` field similar to Post's (NORMAL | HIDDEN) to support AI auto-scan flagging (DEC-077) and mod report resolution. Not present in original M04 decisions (DEC-039-046) — added here as a retroactive schema requirement for M04.

---
## Phase 5 — M09: Appeal

### DEC-084: Appeal submission
Message (required, explanation text) + evidence (optional, max 3 images, 5MB/file — shared limits with report system).

### DEC-085: Banned user access
Banned users can still log in normally. Post-login they see only a "account banned" screen with reason + "Gửi khiếu nại" button (if within appeal window). All other API endpoints blocked (403) except appeal submission endpoint. Ban notification email includes direct "Appeal" link to protected /appeal route (redirects through login if needed).

### DEC-086: Appeal deadline
- Warning: appeal window = entire probation duration (7/10/15 days matching DEC-079)
- Temporary ban: appeal window = entire ban duration (30/90 days matching DEC-080)
- Permanent ban: appeal window = 90 days from ban date, then appeal right permanently expires

### DEC-087: One appeal per action
Each resolved report action, warning, or ban may be appealed exactly once. A rejected appeal cannot be resubmitted for the same underlying action.

### DEC-088: Appeal queue (separate from report queue)
- Separate queue from M08's report queue — different assignment rule needed (mod cannot review appeals of their own actions, per QA-021)
- Priority: Ban appeals > Warning appeals; FIFO within same tier
- Claim-based (30-min inactivity timeout, same mechanic as report queue)
- Mod's own actions are automatically excluded from their queue view (not just skipped — hidden entirely)
- Sole-mod edge case: if the only available mod is the action's author, auto-escalate to ADMIN

### DEC-089: Appeal outcome (reversal)
- Ban approved: account_state reverts to ACTIVE immediately; ban record kept in log marked overturned=true for audit, no longer in effect
- Warning approved: restriction lifted immediately; warn count decremented (treated as if warning never happened) to keep LIGHT/MEDIUM/HEAVY escalation math accurate

---
## Phase 5 — M10: Admin Panel

### DEC-090: Admin panel scope split
- Admin-only: Role management (promote/demote USER↔MOD), System config (AI toggle etc.), full audit log view, MOD account management (performance, revoke)
- Shared with Mod: report/warning/ban/appeal handling, Topic edit/merge (M05), Tag crisis soft-delete (M05)
- Policy constants (warning durations, ban durations, thresholds) are NOT admin-configurable via UI — hardcoded in code, changed via deployment + notify if needed

### DEC-091: Role management flow
- Promote: Admin sends a proposal ("Đề xuất làm Mod") to a user (no eligibility conditions — admin free choice) → user receives notification with Accept/Decline → Accept sets role=MOD immediately; Decline does nothing (admin can re-propose later)
- Demote: Admin executes directly and immediately, no consent needed, no appeal right (role management, not punishment — different from M09 appeal scope)

### DEC-092: System config list (Admin Panel)
1. AI toggle (master + per-module, see DEC-093)
2. Maintenance mode (locks site to admin-only access)
3. Registration toggle (pause new signups)
4. Feature flags for Should/Could modules (Group, Chat, Gamification)
5. Site-wide announcement banner
(Email service toggle explicitly excluded — not needed for v1)

### DEC-093: AI toggle granularity
Two-tier hierarchy:
- Master "AI Layer" toggle: overrides everything OFF when disabled
- Per-module toggles (only apply when master is ON): Search (semantic embedding, M06), Moderation (pre-scan+comment auto-scan+auto-warn, M08), Topic suggestion (M05)

### DEC-094: Admin action audit log
All admin actions (promote/demote, config toggles, ban/warn actions) logged. Append-only — admin can view but cannot edit or delete entries. Ensures transparency even over admin's own actions.

---
## Phase 5 — M13: AI Layer

### DEC-095: Embedding model + storage
- Model: OpenAI `text-embedding-3-small` (same vendor as Moderation API, cheap ~$0.02/1M tokens, multilingual incl. Vietnamese)
- Storage: pgvector extension, `posts.embedding vector(1536)` column, HNSW index
- Computed once at publish time (or alongside pre-scan); recomputed if content edited significantly (mirrors is_stale pattern from M05)

### DEC-096: Topic suggestion model
GPT-4o-mini — sufficient for simple 11-topic classification task, low cost.

### DEC-097: Moderation category mapping + coverage limits
- OpenAI Moderation API covers: Quấy rối (harassment), Ngôn từ thù ghét (hate), Người lớn (sexual), Bạo lực (violence) — maps directly to report reason categories
- NOT covered by AI: Spam, Đạo văn/Vi phạm bản quyền, Nội dung sai/gây hiểu nhầm — these rely entirely on manual report, no AI detection exists for them

### DEC-098: Confidence threshold — symmetric 2-branch design
One Moderation API call drives two independent decision branches from the same category scores:
- **Branch A (Content Gate)**: score≥0.9 → AI auto-reject (Post) / auto-hide (Comment), skip mod; 0.5≤score<0.9 → hold for mod review (Post stays PENDING, Comment stays hidden+queued); <0.5 → publish/show normally
- **Branch B (Warning)**: score≥0.9 → AI auto-issues warning; 0.5≤score<0.9 → mod decides during their review; <0.5 → no warning
Same 0.9/0.5 thresholds shared across Post and Comment. Values are placeholder/tunable pending real usage data.

### DEC-099: AI failure handling (distinct from admin AI-off toggle)
Two distinct scenarios:
1. **AI deliberately OFF** (M10 admin toggle): uses each module's defined fallback — Search→full-text (M06), Topic→manual dropdown (M05), Moderation→no scan, content publishes directly, relies on report only (M03/M08)
2. **AI transient failure** (timeout/error while AI is ON): per-request degradation, not a state change
   - Timeout thresholds: Fast APIs (Moderation, Embedding) = 5s; LLM generation (Topic suggestion) = 10s
   - Retry: exactly 1 retry, sequential (wait for first attempt to fail/timeout, then 2s delay, then retry once)
   - If retry also fails: Search→fallback full-text for that query only; Topic suggest→show non-blocking error, no action taken; Moderation (Post pre-scan)→route to mod review queue (treat as safety-net, do NOT auto-publish); Moderation (Comment)→leave as-is, log error for admin

### DEC-100: AI rate limiting
No dedicated AI-specific rate limit system. Relies on existing limits: Search (M06 DEC-063). New limit added: Topic Suggest button — 10 requests/min/user (only AI-triggered action lacking a natural rate limiter). Pre-scan/auto-scan are system-triggered, not user-invoked repeatedly, so no separate limit needed.

---
## Phase 5 — M11: Group

### DEC-101: Group creation — open access, rate-limited
Any logged-in user can create a group freely. Rate limit: 5 groups/day/user (anti-spam). No cap on total groups a user can own.

### DEC-102: Group role permission matrix
| Quyền | Owner | Group Mod | Member |
|-------|-------|-----------|--------|
| Đăng bài/comment/vote | ✓ | ✓ | ✓ |
| Duyệt pre-mod queue (nếu toggle bật) | ✓ | ✓ | ✗ |
| Ẩn/xóa post-comment trong group | ✓ | ✓ | ✗ |
| Duyệt/kick Member | ✓ | ✓ | ✗ |
| Promote/demote Group Mod | ✓ | ✗ | ✗ |
| Kick Group Mod khác | ✓ | ✗ | ✗ |
| Đổi setting group (public/private, pre-mod, anonymous, join question) | ✓ | ✗ | ✗ |
| Xóa group | ✓ | ✗ | ✗ |
Strict hierarchy: no role acts on a peer or superior (Group Mod cannot kick another Group Mod — Owner only).

### DEC-103: Group join flow matrix
|  | Không có join question | Có join question |
|---|---|---|
| Public | Join ngay lập tức | Cần duyệt (Owner/Mod xem câu trả lời) |
| Private | Cần duyệt | Cần duyệt (kèm câu trả lời) |
Rejected join requests can be resubmitted immediately, no cooldown (matches Facebook/LinkedIn/Discord group behavior). Owner/Mod use per-user block for persistent spam requesters instead of a system cooldown.

### DEC-104: Group content moderation layers on top of system-wide M08, does not replace it
Report (M08) and "System Mod/Admin can intervene anytime" (Phase 2, QA-016) remain fully in effect for group content. The group's AI-scan → Group Mod queue → Live flow is an additional publishing gate, not a substitute for system oversight. For posts belonging to a group: score≥0.9 → auto-reject (skips everyone); 0.5≤score<0.9 → mandatory Group Mod/Owner review regardless of pre-mod toggle state; score<0.5 → follows the group's pre-mod toggle (ON=review, OFF=publish direct). Group and System Mod each get their own claim-based "pending publish" queue (30-min timeout), separate from the Report queue. Posts not in any group keep the original M03/M13 flow unchanged.

### DEC-105: Group deletion & member departure — content and point handling
Group deleted by Owner: soft-delete (content hidden from everyone including ex-members, not hard-deleted in DB). User's overall reputation is fully preserved — **AMENDED by DEC-113: the original exception deducting points tied to content lost with the group has been removed.** Group deletion is an indirect cause from the member's perspective (they didn't choose it, didn't violate anything), so no point deduction applies, consistent with DEC-113's direct-vs-indirect principle.
Member leaves or is kicked (group NOT deleted): their posts/comments remain exactly as-is, treated as the group's asset; author shown with real name; no point deduction. Kicked is treated identically to voluntary leave.

### DEC-106: Group size — no membership or ownership cap
A user may join unlimited groups and be Owner of unlimited groups simultaneously.

### DEC-107: Group ownership succession
Voluntary leave: Owner MUST designate a successor before leaving is allowed (blocking UI action). If the Owner is the group's only member, leaving deletes the group instead (with a warning shown).
Involuntary loss (ban/deactivate/delete — no chance to designate): auto-promote in order — (1) currently-active Group Moderator with longest tenure as Mod (a demoted ex-Mod doesn't count); (2) if none, longest-tenured Member; (3) if Owner was the sole member, the group is soft-deleted.

### DEC-108: Group visibility change (Public↔Private) — feed/post retention
Owner can change visibility anytime. Posts already delivered to a given user's feed remain visible to that user (not retroactively pulled) but become non-interactive once the group goes Private (comment/vote/report → error). New feed/search queries by non-members exclude these posts going forward.

### DEC-109: No appeal path for group-level moderation
Actions taken by Group Mod/Owner within a group (e.g. pre-mod rejection, content removal) are final — no appeal mechanism, unlike system-level MOD/ADMIN actions which go through the Appeal module (M09).

### DEC-110: Private group discovery & invite permissions
Private groups are fully hidden from search/discovery; reachable only via invite/link. Any group member (Member, Group Mod, or Owner alike) can invite others — not restricted to Mod/Owner. Join flow reuses the mechanism established in DEC-103 (no separate targeted Invitation entity with accept/decline).

### DEC-111: Group post cross-posting to main feed
A group post always appears in the feed of that group's own members, whether the group is Public or Private. For Public groups specifically, the post additionally appears on the main feed like an ordinary post (visible to non-members). Private group posts never surface on the main feed.

### DEC-112: Anonymous posting in group — opt-in, sticky, visible to Group staff
When a group's anonymous-posting toggle is ON, each member chooses per-post whether to post anonymously (not forced group-wide). If the Owner later turns the toggle OFF, previously-anonymous posts stay anonymous (the toggle only gates new posts, it does not retroactively reveal authors). Group Mod and Owner can see the real identity of an anonymous post's author, consistent with the system-wide MOD/ADMIN pattern (DEC-004, DEC-005).

## Phase 5 — M09 Amendment + M12: Gamification

### DEC-113: Content-tied point deduction — direct vs indirect principle, supersedes DEC-105's group exception
Points earned from upvotes on a piece of content are deducted ONLY when the content's disappearance is a DIRECT consequence of the point-holder's own action or own violation:
- Self-delete (post or comment, by its own author) → deducted
- Removed by Mod/Admin for that specific content's own violation → deducted
Points are PRESERVED when the disappearance is INDIRECT — caused by someone else's action, not the point-holder's own choice or fault:
- Group deleted by its Owner (a Member's content vanishes as a side effect, not their own action) — supersedes and removes DEC-105's original exception
- A comment cascade-hidden because its parent post was removed (for any reason) — the comment author didn't delete it themselves nor did their comment violate anything
Timing: self-delete → deduction applied only after the 7-day soft-delete window ends (hard-delete); if restored within the window, no deduction ever occurs (no separate refund mechanic needed). Mod/Admin removal for violation → deducted immediately, no waiting period.

### DEC-114: Badge permanence and audit trail
Badges are permanent once earned and are never revoked, even if the user's points later drop below the badge's threshold (including via a legitimate DEC-113 deduction). Rationale: a badge represents an achieved milestone (a historical fact), not a live status — consistent with common platform convention (Stack Overflow, Duolingo); avoids penalizing users for point changes outside their control; avoids the added complexity of live threshold recheck-and-revoke logic. Badge UI displays the date earned rather than re-displaying the threshold value, to avoid the appearance of inconsistency when current points sit below it.
Audit trail: threshold-based permanent badges get a single audit entry (the date first achieved — they cannot be "re-earned"). Periodic top-N titles (e.g. "Ngôi sao tuần", reset each cycle) get multiple audit entries — one per cycle win, since the same title can be won again in a later cycle.

### DEC-115: Content Deletion Appeal — new appeal type, Post only (amends Phase 2 Appeal scope)
Amends the original Phase 2 decision that Appeal (M09) covers only Warning and Ban. A third appeal type, "Content Deletion Appeal," is added for content removed by Mod/Admin due to violation — **scoped to Post only, explicitly excluding Comment** (posts are higher-value assets; comment volume is too high for a sustainable appeal queue; consistent with DEC-004 treating posts as higher-value than comments).
Precedent reviewed: Reddit distinguishes admin-level content removal (formal appeal, ~6-month window) from subreddit-moderator removal (no platform-wide appeal — this maps to and confirms DEC-109's "no appeal for group-level moderation" staying unchanged); YouTube allows content-removal appeals within 1 year, strikes within 6 months. Given iShare's much smaller scale, a shorter fixed window of 30 days from removal is used instead.
Mechanism: a separate "Content Deletion Appeal" queue (distinct from Report and from Warning/Ban Appeal), reusing the existing claim-based 30-minute-timeout mechanism. Priority ranks lowest among the three appeal types: Ban > Warning > Content Deletion Appeal.
Outcome on success: (1) the content is restored, (2) any points deducted under DEC-113 are refunded, (3) any warning or ban issued together with that specific removal is also reversed, reusing the existing appeal-outcome mechanism from ISS-117 (warning: restriction lifted + warn count decremented; ban: immediate unban, log kept with an overturned flag).
Comments have no equivalent appeal path — points deducted for a Mod/Admin-removed comment remain permanently deducted.


## Phase 5 — M12: Gamification Deep Dive

### DEC-116: Point weight — Post Star vs Comment Star
Post Star = 2, Comment Star = 1. A stronger 2:1 ratio (rather than a softer 3:2) was chosen specifically because it better serves DEC-004's original anti-farming rationale ("prevents spam-comment-to-farm-reputation") — a bigger gap makes comment-spamming clearly less rewarding than posting, and stays consistent with DEC-001 (content depth over breadth). The formula: `points = 2 × post_upvotes_received + 1 × comment_upvotes_received`.

### DEC-117: Periodic top-N title — cadence and N
The periodic top-N title ("Ngôi sao tuần") applies to the **Weekly** window only (not Monthly/All-time), with **N = 3** (top 3 users each week receive the title). N is a floor, not a hard cap: if multiple users tie exactly at the cutoff rank, all tied users receive the title that week (see DEC-123 for the tie mechanism) rather than applying a secondary tie-break rule.

### DEC-118: HEAVY warn — leaderboard exclusion (amends DEC-079)
A user at **HEAVY** warning level is excluded from the public leaderboard for the duration of their probation period. This is a deliberate, explicit exception carved into DEC-079's "fully private" warning-status guarantee — the only public-facing consequence of a warning. Does not apply to LIGHT or MEDIUM levels. Rationale: losing leaderboard visibility functions as an additional privilege loss at the most severe warning tier (consistent with HEAVY already losing posting/commenting rights per DEC-079), and the stakeholder accepted the trade-off that this may let observant peers infer a HEAVY warning is in effect, despite DEC-079's original bullying-prevention intent — deemed an acceptable, bounded exception rather than a full reversal of that principle.

### DEC-119: Vote retraction
Upvotes are toggleable — a user can retract their own upvote by clicking again. The recipient's point total is deducted immediately upon retraction, symmetric with how it was added.

### DEC-120: Self-vote prohibition
Self-voting is not permitted. The vote button is hidden/disabled on a user's own post or comment, blocking the fraud vector at the source rather than allowing the click and silently discounting it.

### DEC-121: Leaderboard computation — single periodic job
Leaderboard ranking (across all three windows — Weekly/Monthly/All-time) is computed by a single cron job running every 60 minutes, not real-time per vote. Each run does two things: (1) refreshes the cached ranking used for live in-progress display, and (2) checks whether a cycle boundary (week/month) has closed since the last run — if so, it computes that cycle's final ranking using an exact date-range query (not the display cache) and triggers title award + notification for it. This keeps the architecture to one mechanism instead of two separate jobs, at the cost of up to 60 minutes of delay between a cycle's true close and its title-award notification — the winner computed is always correct because the finalization query is boundary-exact regardless of when the job happens to run.
Individual point totals (on a user's own profile) remain real-time, unaffected by this batching — only the aggregate ranked list is batched.
No historical full-leaderboard view is provided for past cycles (only the current state of each window is shown); past periodic-title wins remain permanently visible through the title/badge audit trail (DEC-114), which is a much narrower record than a full historical ranking snapshot.

### DEC-122: Banned account — display treatment (extends DEC-118's exception to DEC-079)
A **BANNED** account is also excluded from the public leaderboard for the duration of the ban, consistent with the HEAVY-warn treatment in DEC-118 (a ban is a more severe sanction than a HEAVY warning). Unlike a HEAVY warning, however, a banned user's profile, posts and comments remain visible to other users as normal — not hidden or tombstoned — because a ban is reversible (via appeal, DEC-089) and distinct from account deletion (DEC-019); any specific violating content is handled separately through the existing M08 report/moderation flow, independent of the account-level ban action. A **"Tài khoản đã bị khóa"** ("Account has been locked") label is shown everywhere the banned user's name appears — on their profile page and next to their author name on every post/comment they've made — a deliberately public label, unlike the strict privacy DEC-079 applies to warning status, since a ban is treated as a more transparent, public-facing sanction.

### DEC-123: Leaderboard/title tie handling
Two mechanisms, kept consistent with each other:
- **Leaderboard display ranking**: users with equal points share the same displayed rank (standard competition ranking, e.g. two users tied at rank 3 both show "3", the next user shows rank 5) — no secondary tie-break criterion needed.
- **Weekly top-N title cutoff**: if multiple users tie exactly at the N=3 cutoff, all of them receive the title for that week (N acts as a floor, not a hard cap) — same "no arbitrary tie-break" philosophy as the display ranking.

---
## Phase 5 — M14: Feed & Discovery

### DEC-124: Trending Post — decay formula (new, distinct from DEC-052)
DEC-052 (Trending Topic/Tag, M05) stays unchanged — rolling 7-day hard window, no decay. Trending Post (new sub-view under M14's Trending tab) uses a separate, smoother formula: exponential half-life decay, `weight = 0.5^(age_days / 7)` (weight halves every 7 days), hard cutoff at 28 days (4 weeks) — posts older than that are excluded entirely regardless of residual weight. Base engagement score unchanged: `Σ(weight × (1 + upvotes×2 + comments×1))`, recalculated every 15-30 min (same cadence as DEC-052). 28-day cutoff chosen as a clean multiple of the 7-day half-life (residual weight ≈6.25% at cutoff — negligible, avoids an abrupt "cliff" effect vs. shorter windows like 21 days which would cut off content still at 12.5% weight).

### DEC-125: M14 Feed structure — 4 tabs, no AI-driven personalization tab
M14 Feed consists of 4 tabs: **Trending** (3 sub-views: Post/Topic/Tag), **Following** (chronological, from Follow targets established in M07 — User/Topic/Post), **Group** (chronological, aggregated from all groups — Public+Private — the user has joined), **Newest** (chronological, site-wide, excluding Group-sourced posts). There is no separate algorithmic "For You" personalized-ranking tab — this simplifies scope and removes M14's dependency on M13 (AI Layer); M14 now depends only on M03 (Post) and M05 (Topic & Tag). Group Public posts cross-posted to the main feed (per DEC-111) are included in Trending Post and the Group tab, but excluded from Newest (Newest is kept as a pure non-group content stream).

### DEC-126: Guest access to Feed tabs
Guest (unauthenticated) can view Newest and the full Trending tab (all 3 sub-views) without restriction — consistent with the existing Guest browse permissions (QA-011) and the SEO/discoverability rationale behind them. The Following and Group tabs remain visible to Guest but are gated behind login. All interactions (upvote, report, bookmark, follow, join) require login regardless of tab, per the existing Guest permission matrix (QA-011).

### Issues Closed
ISS-166 through ISS-177, ISS-185 through ISS-188 (see issue-queue.md / qa-log.md Phase 5 — M14 section for full detail)

---
## Phase 6 — Cross-cutting Concerns

### DEC-127: Timezone & date handling
All timestamps stored as UTC in the database (standard practice). All date/week boundary calculations (Weekly leaderboard reset — M12, 30-day appeal deadline — M09, warn probation 5/10/15 days — M08, Today/7d/30d presets — M15, 7-day post soft-delete window — M03, etc.) and all UI display are computed against **Asia/Ho_Chi_Minh (UTC+7)**, fixed, no DST (Vietnam does not observe daylight saving). Chosen because the entire target user base is Vietnamese students with no multi-timezone need, and a fixed +7 offset introduces no technical edge cases year-round.

### DEC-128: i18n/localisation scope
Vietnamese-only at MS1 (no language switcher), but the UI is built with an i18n-ready architecture — UI strings externalized via an i18n key library (e.g. i18next-style), with a single active locale `vi`. This avoids a full UI-string refactor if another language is added later. Important distinction clarified during interview: UI i18n only localizes the "chrome" (labels, buttons, system messages) — it does NOT translate user-generated content (posts/comments remain in whichever language the author wrote them). Multilingual CONTENT support (translation, content-language tagging/filtering) is a materially different feature, outside the original draft's scope — noted as an open future idea, not built at MS1.

### DEC-129: Data retention — audit log & chat messages (general hard-delete principle)
Audit/mod action log and chat message content are both kept indefinitely — no hard-delete, no archival/cleanup cron — consistent with the existing Notification retention decision (DEC-071: "no retention policy"). Rationale: log/audit-type data is conventionally never deleted in production systems (compliance/transparency/trace value), unlike user content which users may legitimately want removed. Additional technical reason: many other tables reference audit log/chat message rows via FK (reports reference message_id, warn actions reference report rows, etc.) — hard-deleting them risks breaking referential integrity or losing investigative context.
**General principle established for all future hard-delete decisions in this project:** hard-delete only when it is genuinely safe — i.e. there is a clear justification (privacy/PII that must be erased, or cleaning up content a user deliberately deleted with a sensible UX reason) AND it does not break referential integrity with other tables that reference it. Existing hard-delete decisions (Post 7-day soft-delete then hard-delete — DEC-011; Comment permanent delete — DEC-038; Account PII wipe on DELETED — DEC-019) all satisfy this principle and remain unchanged.

### DEC-130: File/media upload — no virus/malware scanning
No dedicated malware scan layer is added. The existing per-feature type/size whitelist (image formats only — JPEG/PNG/WebP, size caps per feature) combined with CDN-side (Cloudinary) image re-encoding/transcoding on upload (which naturally strips malicious payloads hidden in image files) is considered sufficient for MS1, given upload scope is image-only (no executable file types accepted).

### DEC-131: AI — third-party data privacy disclosure
A public Privacy Policy / Terms of Service page is added, explicitly disclosing that publicly posted content (posts/comments) is processed by a third-party AI service (OpenAI — Moderation API for content scanning, Embedding API for semantic search). Linked from the footer and/or the registration flow. Low-cost (a single static content page) but materially increases transparency — judged especially important given the user base includes minors (THPT students).

### DEC-132: AI — Topic Suggestion hallucination handling
Topic Suggestion (GPT-4o-mini) output is validated against the system's fixed 11-topic whitelist. If the returned topic does not match, it is treated as a suggestion failure: a non-blocking error is shown ("Không thể gợi ý chủ đề lúc này, vui lòng chọn thủ công") and the user selects manually. This deliberately reuses the exact same UX pattern already established for AI transient failure (DEC-099: timeout/retry exhausted) — even though the underlying technical cause differs (hallucination vs. timeout), the user-facing experience is identical, requiring no new UI pattern.

### DEC-133: AI — raw output logging
Every AI call (Moderation API, Embedding, Topic Suggestion) has its raw response logged to a dedicated `ai_decision_log` table, linked to the relevant post/comment. Distinct from the existing admin/mod action audit log (DEC-081/094), which logs human actions — this logs AI-made decisions specifically. Serves two purposes: (1) provides real usage data to tune the currently-placeholder 0.9/0.5 confidence thresholds (DEC-098), (2) gives Moderators/Admins an evidence trail when handling a Content Deletion Appeal (M09/DEC-115) where a user disputes an AI-driven rejection.

### Issues Closed
ISS-189 through ISS-196 (see issue-queue.md / qa-log.md Phase 6 section for full detail). One item deferred: **OPEN-005** — no general event-tracking infrastructure for MS1 (formalizes the implicit decision already made at M15/QA-242).

## Phase 7 prep — Tech Stack (OPEN-002, partial)

### DEC-134: Backend/Frontend stack and SSR deferral
Backend is Java + Spring Boot. Frontend is ReactJS built with Vite as a client-side SPA (no server-side rendering) for MS1. SEO/SSR is deliberately deferred and tracked as **OPEN-006**; it does not change Guest read access (QA-011), which stays as decided. QA-234/ISS-174 SSR note is amended accordingly. Rationale: MS1 is demo-only and prioritises core features (QA-002/QA-008); the team has not used Next.js and a self-built or learned SSR layer is a schedule risk across 16 modules. Known consequences: weaker search-engine indexing and no link-preview metadata when sharing URLs (e.g. Zalo/Facebook) until OPEN-006 is resolved. Mitigation (approach, not a requirement): keep API calls in a separate layer and components presentational so a later move to Next.js or another SSR framework is cheaper. UI Kit: a shared in-app UI Kit (component library) will be built for the whole application after the design phase; it is an internal implementation approach inside the frontend codebase, not a separately submitted deliverable and not a new module or scope item (it must respect i18n keys, DEC-128, and the display timezone, DEC-127). The Kit's core requirement is a unified set of common UI components used across the app; building it on top of an existing base library is acceptable (stakeholder: either is fine, the common UI set is what matters). The base library will be chosen after the design is available (**OPEN-007**); the stakeholder currently leans towards MUI (a preference, not a decision). Not decided here: the final base library, and the remaining OPEN-002 items (email provider, AI_ENABLED storage, realtime channel, hosting, confirmation of implied technologies, academic constraints).

### DEC-135: Realtime channel — SSE only
Server-to-client realtime uses Server-Sent Events (SSE) for both chat (M16) and in-app notifications (M07); WebSocket is not used. Chat sending remains a normal POST; read receipts remain POST + SSE (QA-212). Notifications keep DB write as source of truth with best-effort push, now over SSE (QA-131 amended). Feed new-post banner stays on polling (QA-239). Rationale: no feature requires true two-way low-latency communication, and a single mechanism is simpler in a 3-month schedule. Online/offline presence was raised (client heartbeat ping) and explicitly dropped; it is not a requirement. Known limit: in-memory pub/sub supports a single server instance, accepted at demo scale (to be recorded in Phase 7 NFRs).

### DEC-136: Email delivery — Spring Mail over standard SMTP
Outgoing email (magic-link, reactivation OTP, security/ban notices; scope unchanged from M07) is sent with Spring Mail (`spring-boot-starter-mail` / `JavaMailSender`) over standard SMTP, with host/port/credentials supplied via environment configuration. For MS1 the SMTP source is the free tier of an email provider; the specific provider is chosen at implementation time and does not affect the spec. Gmail SMTP may be used in local development only. Sender-domain authentication (SPF/DKIM) is required before real production use, not for the MS1 demo. Switching provider is a configuration change, not a code change.

### DEC-137: Confirmed technology stack (closes OPEN-002)
Technology stack for iShare, confirmed by the stakeholder: Backend Java + Spring Boot (DEC-134); Frontend ReactJS with Vite as a client-side SPA, no SSR at MS1 (DEC-134, OPEN-006), with an in-app shared UI Kit whose base library is chosen after design (OPEN-007); Database PostgreSQL with pgvector (plus the already-decided pg_trgm and `to_tsvector('simple', unaccent())` full-text search); Cloudinary for avatars/attachments; OpenAI for Moderation API, text-embedding-3-small and GPT-4o-mini (Topic Suggestion); Tiptap/ProseMirror editor storing JSON content; JWT authentication with rotating refresh tokens (existing Session decision); Spring Mail over standard SMTP (DEC-136); SSE for all server-to-client realtime (DEC-135); AI toggle lives in the Admin Panel system config (DEC-092/093); no hosting/deployment at MS1 (QA-002, ISS-201). No academic technology constraints (ISS-202). Additions to the stack will be discussed when needed.

### Issues Closed
ISS-197 through ISS-203 and ISS-029 (see issue-queue.md / qa-log.md QA-256–QA-263). OPEN-002 closed. Deferred: **OPEN-006** (SEO/SSR), **OPEN-007** (UI Kit base library). OPEN-001 (AI budget) is now unblocked. Deferred: **OPEN-006** (SEO/SSR), **OPEN-007** (UI Kit base library).

## System Requirement prep — Privacy & Consent

### DEC-138: Consent to Privacy Policy/ToS is mandatory at registration
A user cannot register unless they explicitly consent to the Privacy Policy/ToS (the public page decided in DEC-131). Privacy is a mandatory part of the product; its detailed scope (personal-data inventory, user rights, handling of users under 18, legal basis, and how permanent retention in DEC-129 relates to PII erasure on account deletion) is deliberately deferred and tracked as **OPEN-008**. Source: QA-264.

### Issues Closed
ISS-204 (partial; see OPEN-008).

## System Requirement prep — Documentation approach

### DEC-139: System Requirement (SR) documentation approach
SR documents are written per module, in Vietnamese (English kept for necessary technical terms), following the structure of the stakeholder's reference sample: 1 Overview, 2 Terms and Abbreviations (terms used in that document), 3 Input Information, 4 Functional Overview (4.1 laws/standards only if the stakeholder names them, otherwise 'Không có'), 5 Functional Requirements (per feature: upper-level requirement, rationale, lower-level requirements; State Transitions where the module has statuses; HMI Requirements and Screen Transitions are placeholders until design), 6 Revision History. Each document is self-contained for terms and role-based permissions. A behaviour is written in exactly one owner module; other modules reference it by ID. Source and Basis (Stated/Derived) are kept in a traceability appendix, not in the body. Milestone and priority are stated once in section 5.1, with labels only on exceptional requirements. Header: document ID, project, module, status, version, date, author (Phạm Văn Đức); no reviewer/approver field. Files are saved under `.agents/.claude/system_analysis/output/specs/` (audit reports under `specs/audit/`). Process: an Author agent drafts; an independent Auditor agent only audits (source-to-requirement coverage matrix plus a rule checklist, partly machine-checked) and never edits; the Author fixes per the report; at most 2 rounds, then the stakeholder decides. Every GAP, ambiguity or suggestion is raised to the stakeholder one at a time; answers are recorded in the registers (QA/DEC) and the Author updates the SR accordingly. SR is written now; Phase 7 and 8 follow. First run is a pilot on one module (proposed: M05). Requirement ID convention: see the amendment below. This decision deliberately departs from two rules in BA-INTERVIEW-RULES (English-only output; no spec before Phase 9). Source: QA-265.

**[Amended 2026-10-04 — QA-266]** Details fixed for the pilot: (1) ID convention — project prefix `ISH`; document `ISH-SR-Mxx` (routing file `ISH-RT-Mxx`); upper-level requirement `ISH-Mxx-nnn`, lower-level `ISH-Mxx-nnn.k`; open point `OP-Mxx-nn` (temporary, Appendix B only); audit finding `AUD-Mxx-nn`; source items keep their ISS/QA/DEC/OPEN IDs; IDs are permanent (never renumbered or reused, gaps allowed); section numbers 5.x are not IDs. (2) Requirement sentences use Vietnamese EARS templates with 'hệ thống' as the only subject of 'phải', plus INCOSE-style rules (atomic, measurable, no escape clauses, no pronouns, no solution or data-model terms). (3) Content that is not a functional requirement (data model → Phase 8, NFR → Phase 7, HMI, process notes, other-module behaviour, superseded items, omissions) goes to a per-module routing file `specs/routing/ISH-RT-Mxx.md`, not into the SR; every source item of the module must appear either in SR Appendix A or in the routing file. (4) Appendix A = traceability (ID | Source | Basis Stated/Derived | Note); Appendix B = temporary open points. (5) Normative rules live in `.agent-instructions/system_analysis/shared/SR-DOCUMENT-RULES.md`; Author role `.agent-instructions/system_analysis/roles/sr-author/AGENT.md` (Auditor role `roles/sr-auditor/` later); helper scripts `inventory.py` and `check_sr.py` live in `.agent-instructions/system_analysis/shared/sr-tools/`. [Layout updated 2026-10-04 when the instruction set was restructured into roles/ and shared/.] Source: QA-266.

**[To be superseded 2026-10-07 — stakeholder]** The process and convention parts of DEC-139 and its QA-266 amendment are marked to be superseded by the new Functional Requirement skill and will be replaced by a new DEC when that skill is confirmed: the Author/Auditor process and audit rounds, raising every GAP one at a time, the `ISH-*`, `OP-*` and `AUD-*` ID convention, the Vietnamese EARS sentence rules, the routing file and Appendices A/B, the `specs/` file locations, and the references to SR-DOCUMENT-RULES, the sr-author/sr-auditor roles and the sr-tools scripts. The M05 pilot run was discarded. Still in force until then: one document per module, self-contained terms and permissions; Vietnamese with English kept for necessary technical terms; requirements written now, before Phase 7/8; the reference-sample section structure; one owner module per behaviour, other modules reference it; sources kept out of the body; milestone/priority stated once; header fields.

### Issues Closed
ISS-205.
