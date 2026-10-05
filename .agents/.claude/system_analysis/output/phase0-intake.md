# Phase 0 — Intake & Gap Analysis

**Date:** 2026-09-20
**Status:** CLOSED — confirmed by stakeholder
**Agent:** Claude Sonnet 4.6
**Session:** https://claude.ai/code/session_01Mt7KDUP1rNRdUE7zsoQzPb

---

## Product Understanding (confirmed)

1. iShare is a Q&A and knowledge-sharing community platform for high school students (THPT) — Stack Overflow/Quora model; content is accumulated and evaluated long-term, not ephemeral like comments.
2. Real product for a real client (a THPT teacher); graduation thesis is a milestone, not the end goal. Team of 2 (BA/QA + FE+BE per module).
3. Single end-user type: high school students. No Teacher account type. 3 permission levels: USER, MODERATOR, ADMIN.
4. 3 content classification axes: Topic (domain), Lớp/Khối (grade 10/11/12), Tag (free keywords). Topic list not yet finalized — to be confirmed in BA.
5. Post is the central content unit: multiple types (Q&A, sharing, tutorial, review…), status machine, Edit History, Anonymous mode, Accepted Answer (author-only).
6. Group reuses the entire Forum mechanism — no rebuild; only adds `group_id` on Post and GroupMember table.
7. Messaging is text-only via WebSocket (separate architecture from REST). No voice/video/file transfer. [Amended: chat transport chốt = POST gửi + SSE nhận (QA-046), không dùng WebSocket — DEC-135]
8. Reward/Gamification: Reputation (Post Star ≠ Comment Star, different weights), Badge, Leaderboard (4 cycles), User Statistics.
9. AI is a mandatory support layer (5 features), calls third-party APIs, async processing, with fallback. AI does not make final decisions on sensitive cases.
10. Full scope committed — no optional/nice-to-have. Delivery order: P0 → P1 → P2.

---

## Module Map (tentatively approved — to be formally confirmed at Phase 3)

| # | Code | Module | Priority |
|---|---|---|---|
| 1 | `USR` | User & Account | P0 |
| 2 | `POST` | Post & Forum | P0 |
| 3 | `COMT` | Comment | P0 |
| 4 | `CLAS` | Classification (Topic/Tag/Lớp-Khối) | P0 |
| 5 | `INTR` | Interaction (Star, Bookmark, Follow, Mention) | P0+P1 |
| 6 | `GRP` | Group | P0 |
| 7 | `MSG` | Messaging | P0 |
| 8 | `DISC` | Discovery & Notification | P0+P1 |
| 9 | `REWD` | Reward & Stats | P0 |
| 10 | `ADMN` | Moderation & Admin | P0+P1 |
| 11 | `AI` | AI Assistance Layer | P0+P1 |

---

## Proposed Interview Agenda

| Phase | Scope |
|---|---|
| 0 | Intake ✅ CLOSED |
| 1 | Business context, goals, constraints, success metrics |
| 2 | Actors: USER / MOD / ADMIN — permission matrix |
| 3 | Module decomposition + MoSCoW (Gate: approval) |
| 4 | Feature decomposition per module (Gate: approval) |
| 5 | Feature deep dive (~63 features) |
| 6 | Cross-cutting concerns (auth/session, uploads, AI cross-concerns, i18n…) |
| 7 | Non-functional requicừtôirements |
| 8 | Data model & integrations |
| 9 | Open issue clearing round |

---

## Issue Queue Policy (confirmed by stakeholder)

Issues are explored **scope-driven**: issue queue for a scope is built when entering that scope, not front-loaded. Issues may grow throughout the interview as answers create new questions.

---

## Preliminary Observations (seed for scope-level issue queues, not formal ISS-### yet)

Topics to probe when entering each scope:
- USR: account deletion policy, session management, password policy
- POST: edit history visibility, rich content file attachments, status transition rules
- COMT: accepted answer changeability, anonymous post edge cases
- CLAS: Topic CRUD ownership, AI classification integration with user review
- INTR: mention limits, star on anonymous post
- GRP: private group approval, ownership transfer
- MSG: notification for messages, read receipts
- DISC: personalized feed fallback, semantic search UX
- REWD: reputation formula/weights, badge criteria configurability
- ADMN: report routing, audit log retention
- AI: moderation confidence thresholds, summarization trigger, eval loop actors

---

## Phase 1 — Business Context (CLOSED)

**Status:** CLOSED — confirmed by stakeholder
**QA entries:** QA-001 to QA-010
**Open issues carried forward:** ISS-026 (AI budget — open), ISS-029 (academic constraints/tech stack — partial)

### Key outcomes:
- **MS1 deadline:** Mid/late December 2026 (~3 months). No deploy required. DoD = dev complete + full feature demo + AI live.
- **Success metric:** Qualitative (feature completeness + demo quality). Seeded data for demo.
- **Competitive landscape:** No direct competitor. Main challenge = behavior change (HS currently use Facebook/Zalo/ChatGPT instead of community sharing).
- **Business Goals (BG-01 to BG-04):**
  - BG-01: Xây dựng văn hóa học tập cộng đồng — nơi chia sẻ học thuật và tâm tư
  - BG-02: Phát huy peer learning — "học thầy không tày học bạn"
  - BG-03: Gamification based on Expectancy Theory (Vroom, 1964)
  - BG-04: Không gian thảo luận đa chiều cho HS
- **AI cost:** < $0.01 for MS1 demo (70 posts, 30 users). Recommend $5 OpenAI credit. Stack: Moderation API (free) + gpt-4o-mini + text-embedding-3-small. ISS-026 OPEN.
- **Production-ready from day 1** — no shortcuts, no "demo-only" hacks.
- **Admin:** Super admin pattern — root seeded from DB, can promote others via UI (DEC-007).
- **Academic constraints:** None on content/scope. Tech stack TBD (ISS-029 OPEN).

---

## Phase 2 — Actors, Roles & Permissions (IN PROGRESS → PENDING CONFIRM)

**Status:** Queue empty — awaiting stakeholder confirmation
**QA entries:** QA-011 to QA-021

### Actors confirmed:

| Actor | Type |
|---|---|
| GUEST | Human — unauthenticated |
| USER | Human — default after registration |
| MODERATOR | Human — appointed by ADMIN |
| ADMIN | Human — root seeded from DB, can promote others |
| AI Moderation Worker | System — scans Post + Comment, real-time |
| AI Classification Worker | System — suggests Topic; logs user feedback |
| Notification Worker | System — background job |
| Badge/Reputation Engine | System — auto-award + auto-revoke |

### Role hierarchy:
USER < MODERATOR < ADMIN (single enum, ADMIN inherits all MOD permissions)

### Group roles (within Group):
Owner / Group Moderator / Member

### Key decisions:
- Anonymous post: author hidden from USER, visible to MOD + ADMIN
- Soft delete: ACTIVE → DEACTIVATED (14-day grace, email OTP reactivation) → DELETED
- Ban → BANNED state. AI warns, never bans. MOD + ADMIN ban/unban (system-wide).
- Warn system: 3 levels LIGHT/MEDIUM/HEAVY (counts 1-2/3-4/5-6). Probation auto-reduce (5/10/14 days). No account restrictions — indicator shown to others. AI confidence threshold lowers per warn level (sketch: 85%/75%/65%/55% — calibrate Phase 6).
- Appeal ("Khiếu nại" in UI): warn + ban only (original). **AMENDED in Phase 5 (DEC-115):** added a 3rd type, Content Deletion Appeal, scoped to Post only — see M09 Deep Dive. MOD reviews all except own actions. ADMIN reviews all including own actions.
- Group: public/private. Pre-moderation toggle (Owner). Flow: AI scan → Group Mod queue → live. System MOD/ADMIN can intervene anytime.
- AI Classification: suggests Topic only (not auto-assign). User confirms/adjusts → feedback loop. Tag always user-decided.

### Phase 4 backlog spawned:
- ISS-GRP-01: Public vs Private group deep dive
- ISS-GRP-02: Post flow within group (many sub-issues)
- ISS-REWD-01: Badge permanent vs revocable
- ISS-REWD-02: Warn level → trust/reputation display penalty
- ISS-ADMN-01: Warn escalation threshold count

### Phase 6 backlog spawned:
- ISS-AI-01: AI Moderation confidence threshold calibration


---

## Phase 3 — Scope Decomposition (Module Level) | Status: CLOSED ✓

### Module Registry (16 modules)

| ID | Module | MoSCoW | Dependencies |
|----|--------|---------|--------------|
| M01 | Authentication & Account | Must | — |
| M02 | User Profile | Must | M01 |
| M03 | Post & Content | Must | M01, M05 |
| M04 | Comment | Must | M01, M03 |
| M05 | Topic & Tag | Must | — |
| M06 | Search | Must | M13 |
| M07 | Notification | Must | M01 |
| M08 | Moderation | Must | M01, M13 |
| M09 | Appeal | Must | M01, M08 |
| M10 | Admin Panel | Must | M01, M08 |
| M11 | Group | Should | M01, M03, M08, M13 |
| M12 | Gamification | Should | M01, M03, M04 |
| M13 | AI Layer | Must | — |
| M14 | Feed & Discovery | Could | M03, M05, M13 |
| M15 | Analytics & Stats | Could | M01, M03, M08 |
| M16 | Chat & Messaging | Should | M01, M11 |

**Won't Have v1:** Video streaming, mobile native app, external integrations beyond OAuth.

### Key Decisions
- **DEC-008**: AI Layer Feature Flag — global toggle (Admin config UI hoặc env var). Fallback per module khi AI off.

### Search (M06)
- Semantic embedding cho Post body/title
- Exact/prefix match cho User và Tag
- Comment không được search
- Vector storage → OPEN-002 (Phase 8) [Resolved: PostgreSQL + pgvector — DEC-137]

### Chat (M16)
- DM (1-1 giữa user) + Group Chat (trong Group)
- Real-time → Phase 7 NFR

### Issues Resolved
- ISS-040 (Search scope) → Closed / QA-022
- ISS-041 (Chat scope) → Closed / QA-023
- ISS-042 (AI Layer priority) → Closed / QA-024

---

## Phase 4 — Feature Decomposition (ISS-043 to ISS-053)

### Authentication & OAuth (M01)
- Google OAuth (Sign in with Google)
- Auto-link by verified email (DEC-010): nếu email Google = email đã đăng ký → tự động link, gửi notification
- No manual confirmation required

### Post & Content Model (M03)
- **Rich text editor:** Tiptap (ProseMirror JSON) — `content_json JSONB` + `content_text TEXT` (search)
- **Media:** Attachment only — không có inline image
- **3-field status model (DEC-012):**
  - `publish_state`: draft / published / deleted (user controls)
  - `mod_state`: pending / active / under_review / removed (system/mod controls)
  - `lock_level`: none / author / mod (author locks comments on own posts; mod can also lock)
- **Soft delete (DEC-011):** `deleted_at` timestamp, 7-day recovery window, cron hard-delete
- **Edit history:** `post_revisions` table (post_id, version, title, content_json, content_text, edited_at, edited_by)
- **Pre-scan policy (DEC-013):** new post → `mod_state=pending` (hidden) until AI scan; edit → background re-scan; AI off → bypass; no retroactive scan on re-enable

### Comment (M04)
- 1 cấp nesting (reply to comment only, không nested deeper)
- `parent_comment_id` nullable; depth check enforced

### Classification (M05)
- 2 tầng: Category → Topic (AI gợi ý topic_id, user confirm)
- `grade_level` ENUM('10','11','12') NULL — field riêng biệt trên Post, độc lập với Category/Topic
- `grade_level` trên User Profile: optional, user tự update, system gửi annual reminder notification

### Search (M06)
- Post: semantic (pgvector embedding) + FTS (tsvector)
- User: pg_trgm (display name substring match — handles Vietnamese names correctly)
- Group: FTS (name + description)
- Comment: FTS only (tsvector) — không semantic embed (upvote model, no stable "accepted answer" entity)

### Gamification & Leaderboard (M12)
- **Points:** = tổng upvotes nhận được (thuần túy, không login streak/bookmark bonus)
- **Badges:** threshold-based (permanent, tự award khi đạt ngưỡng) + periodic top-N titles (reset mỗi chu kỳ)
- **Leaderboard:** Weekly / Monthly / All-time time windows (không reset score; sum upvotes trong window)
- **Grade filter:** 10 / 11 / 12 / all (all = include users không có grade)
- **Scope:** Global only (không per-group)

### Moderation — Report Categories (M08)
- 6 values: Spam / Nội dung không phù hợp / Sai lệch thông tin / Quấy rối / Bản quyền / Khác (+ free text note)

### Follow (M07)
- Follow targets: User / Topic / Post (không follow Group — join/leave đủ semantics)
- `follows` table: follower_id, target_type ENUM('user','topic','post'), target_id
- Follow Post → noti mọi update và comment mới

### Group (M11)
- **Anonymous posting (DEC-009):** Group Owner toggle (`F-GRP-10`), chỉ áp dụng cho post mới khi tắt
- **Private group:** Visible-but-gated (tìm thấy nhưng không thấy nội dung)
- **Join flow:** invite link (direct) + request join (Owner/Mod approval)
- **Join question:** `join_question TEXT NULL` (Group-level, optional custom question)
- **Join request:** `answer TEXT NULL` (nullable nếu không có câu hỏi)

### Chat (M16)
- **Send:** POST request
- **Receive:** SSE (Server-Sent Events) — `/chat/:id/stream`
- **Pub/sub:** In-memory `Map<chatId, Set<SSEConnection>>` (thesis scale, single server)

### Key Schema Additions (Phase 4)
```sql
-- Posts
publish_state   ENUM('draft','published','deleted')       DEFAULT 'draft'
deleted_at      TIMESTAMP NULL
mod_state       ENUM('pending','active','under_review','removed') DEFAULT 'pending'
moderated_by    UUID NULL
moderated_at    TIMESTAMP NULL
mod_note        TEXT NULL
lock_level      ENUM('none','author','mod')               DEFAULT 'none'
locked_by       UUID NULL
locked_at       TIMESTAMP NULL
ai_scanned_at   TIMESTAMP NULL
ai_scan_result  ENUM('clean','flagged','error') NULL
content_json    JSONB NOT NULL
content_text    TEXT NOT NULL
updated_at      TIMESTAMP
edit_count      INT DEFAULT 0
grade_level     ENUM('10','11','12') NULL

-- Post Revisions
post_id, version INT, title, content_json, content_text, edited_at, edited_by UUID

-- Users (addition)
grade_level     ENUM('10','11','12') NULL

-- Groups (addition)
join_question   TEXT NULL

-- Group Join Requests
group_id UUID, user_id UUID, answer TEXT NULL,
status ENUM('pending','approved','rejected'), requested_at TIMESTAMP

-- Follows
follower_id UUID, target_type ENUM('user','topic','post'), target_id UUID
```

### Decisions (Phase 4)
- **DEC-009**: Anonymous posting = Group-level toggle by Owner (F-GRP-10 in M11)
- **DEC-010**: OAuth Google + auto-link by verified email
- **DEC-011**: Soft delete, 7-day window
- **DEC-012**: 3-field post status model (publish_state / mod_state / lock_level)
- **DEC-013**: Pre-scan new posts, background re-scan edits, no retroactive scan on AI re-enable

### Issues Resolved (Phase 4)
- ISS-043 (OAuth + linking) → Closed / QA-026
- ISS-044 (Post content + status + scan) → Closed / QA-025, QA-027–QA-031
- ISS-045 (Comment nesting) → Closed / QA-032
- ISS-046 (Classification depth + grade_level) → Closed / QA-033, QA-034
- ISS-047 (Search scope) → Closed / QA-035–QA-037
- ISS-048 (Leaderboard) → Closed / QA-038, QA-039
- ISS-049 (Reward system) → Closed / QA-040, QA-041
- ISS-050 (Report categories) → Closed / QA-042
- ISS-051 (Follow scope) → Closed / QA-043
- ISS-052 (Private group) → Closed / QA-044, QA-045
- ISS-053 (Chat architecture) → Closed / QA-046

---

## Phase 5 — Feature Deep Dive · M01: Authentication & Account

### Registration Flow (DEC-014)
```
Step 1: email + password
Step 2: verify email (magic link, 1h, mandatory)
Step 3: setup — username (required) + display_name (required) + bio/grade_level/avatar (optional)

Google OAuth: skip Step 1+2 → Step 3 (display_name auto-fill, username required)
```
Progressive gate: login → check verify_level → redirect incomplete step.

### Identity Fields (DEC-015)
- `display_name`: free-form, any style, NOT unique
- `username`: unique, alphanumeric+underscore, min 3 / max 20 chars — for @mention only

### Email Flows (DEC-016)
- Verify: magic link **1 hour**, manual resend, 60s cooldown
- Forgot password: magic link **15 minutes** → revoke all other sessions → auto-login
- Change password (Settings): old+new+confirm, no revoke
- Google OAuth: no password → show redirect message

### Session Management (DEC-017)
- JWT, access token **1 hour**, refresh token **30 days** (rotating)
- `refresh_tokens` table in PostgreSQL
- Multi-device: allowed, each device = independent SSEConnection

### Account State Machine (DEC-018)
```sql
account_state  ENUM('ACTIVE','DEACTIVATED','DELETED','BANNED')    DEFAULT 'ACTIVE'
verify_level   ENUM('NONE','EMAIL_VERIFIED','SETUP_COMPLETED')     DEFAULT 'NONE'
```
Login gate: account_state (BANNED/DELETED → block) → verify_level (redirect if incomplete).

### Deactivation & Deletion (DEC-019)
- No direct delete — deactivate → **14-day window** → auto-DELETED
- Posts: hidden ("Nội dung không tồn tại")
- Comments: content visible, author → "Tài khoản tạm thời vô hiệu hoá"
- After DELETED: comments → "[Người dùng đã xóa]", PII wiped
- BANNED screen: reason + appeal time + appeal button + OK

### @Mention System (DEC-020)
- Trigger: `@` + 1 char, debounce 300ms, spaces allowed
- Search: pg_trgm on display_name + username
- Priority (Group): following > same group > global
- Priority (Post): following > common group > global
- Dropdown: top 5 | Item: avatar + display_name + @username (muted)
- Render: display_name + brand highlight (no @), stored as user_id
- Node atomic: no trim/label edit

### Issues Resolved (M01)
- ISS-054 → Closed (DEC-014, DEC-015, DEC-020)
- ISS-055 → Closed (DEC-017)
- ISS-056 → Closed (DEC-016)
- ISS-057 → Closed (DEC-018, DEC-019)

---
## Phase 5 — M02: User Profile Deep Dive

### Profile Page Route
- `/u/{username}` — dual-context (owner / visitor)

### Profile Fields
| Field | Detail |
|-------|--------|
| Avatar | Cloudinary; JPEG/PNG/WebP; max 10MB; no GIF |
| Display name | Free-form (M01) |
| Username | Unique; URL + @mention |
| Bio | Optional; 155 chars UI / 255 DB |
| Points | Display only (M12) |
| Badges | Display only (M12) |
| Followers/Following | Count + full list, public |

### Content Tabs
- Owner: Posts + Bookmarks
- Visitor: Posts only

### Dropped v1
- Social links (future extension)
- Username change history (extra table, low value)

### Issues Closed
ISS-058, ISS-059, ISS-060, ISS-061

---
## Phase 5 — M03: Post & Content Deep Dive

### Editor
Tiptap extensions: bold/italic/underline/strikethrough/highlight, H1-H3, lists (bullet/numbered/task), code+codeblock, LaTeX/KaTeX (raw), table, blockquote, hr, link+label. No inline image.

### Post Structure
- 1 type, no post_type field
- content_json (ProseMirror JSON) + content_text (search)
- Optional poll (separate polls table, FK post_id)
- Attachments: separate section below body

### Status Model
| Field | Values |
|-------|--------|
| publish_state | DRAFT / PENDING / PUBLISHED / HIDDEN / REJECTED / DELETED |
| mod_state | NORMAL / FLAGGED / HIDDEN |
| lock_level | NONE / COMMENT_LOCKED / FULLY_LOCKED |
| locked_by | NULL / AUTHOR / MOD |

Visible when: publish_state=PUBLISHED AND mod_state=NORMAL

### Pre-scan Flow
Submit → PENDING → AI scan → clean: PUBLISHED; flag: PENDING → mod → approve: PUBLISHED | reject: REJECTED

### Attachments
- Images (JPEG/PNG/WebP): 5MB/file, max 10
- Documents (PDF/DOCX/XLSX/PPTX): 20MB/file, max 3

### Poll Config
allow_change_vote, allow_multiple (→ all options), show_result_before_vote (default false); expires_at required; is_closed permanent.

### Edit History
- Post: full (post_edits table), public
- Comment: edited_at only

### Soft Delete
7-day window → author restore; cron hard delete after window.

### Issues Closed
ISS-062 through ISS-069

---
## Phase 5 — M04: Comment Deep Dive

### Editor
Bold, italic, inline code, LaTeX/KaTeX, link, @mention, blockquote. No attachments, no headings/tables.

### Threading
2 levels: root + child. Reply-to-child appends to same thread, @mention for context.

### Reactions
Upvote only.

### Sort (root comments)
Top (default) / Mới nhất / Cũ nhất. Child replies: always chronological.

### Edit/Delete
- Edit: unlimited, no time limit; "(đã chỉnh sửa)" badge
- Delete: permanent
  - Root + has replies → tombstone "[Bình luận đã bị xóa]"
  - Root + no replies → hard delete
  - Child → hard delete; child's replies show "reply to [bình luận đã bị xóa]"

### @Mention + Quote
- @mention: shared M01 logic, always triggers notification
- Quote-reply: blockquote auto-inserted on Reply click

### Issues Closed
ISS-070 through ISS-078

---
## Phase 5 — M05: Topic & Tag Deep Dive

### Topic vs Tag
- Topic: structured taxonomy, AI-assisted, filter/browse axis
- Tag: free #hashtag, user-driven, discovery axis

### Topic List (11, flat)
Toán học, Ngữ văn, Ngoại ngữ, Khoa học tự nhiên, Khoa học xã hội, Tin học, Kỹ năng mềm, Hướng nghiệp, Nghệ thuật & Sáng tạo, Góc Chill, Khác

### Topic Rules
Min 1 / max 3 per post. Mod/admin edit+merge, no delete.

### AI Suggest Flow
Button-triggered → suggest max 3 → user adjusts → publish. is_stale flag if content changes post-suggestion.

### Tag Model
tags + post_tags tables. Max 5/post, 30 chars/tag. Fully free; crisis soft-delete only.

### Trending
Rolling 7-day window, recalculated every 15-30min, score = Σ(1+upvotes×2+comments×1).

### Issues Closed
ISS-079 through ISS-084

---
## Phase 5 — M06: Search Deep Dive

### Scope (final)
Post (semantic/pgvector) + User + Tag + Topic + Group (pg_trgm). No Comment search. Full-text (Postgres FTS + unaccent) fallback when AI off.

### Trigger
Post: submit-only. User/Tag/Topic/Group: debounce (300ms) + submit.

### Ranking
final_score = relevance(0.8) + engagement(0.2); engagement = log(upvotes)×2 + log(comments)×1, normalized.

### Filters
Topic, Tag, date range, Following-only, Sort (Relevance/Newest/Most upvoted).

### Autocomplete
User/Tag/Topic/Group prefix match (pg_trgm), no Post titles.

### Search History
localStorage, max 10, clear button.

### Results Page
Mixed single scroll page. Post primary; User/Tag/Topic/Group supplementary (max 3 each).

### Snippet
No highlight, plain ~150 char snippet.

### Permission
Guest: normal search. Private group content: members-only. Private group entity: visible-but-gated (name shows, content gated).

### Rate Limiting
Guest 30(debounce)/10(submit) per min; User 45/20 per min.

### Pagination
Infinite scroll, 15/load, max 120 total, cursor-based.

### Issues Closed
ISS-085 through ISS-097 (13 issues; ISS-091 merged into ISS-089)

---
## Phase 5 — M07: Notification Deep Dive

### Event List + Channel
See DEC-065. Email restricted to security/account-deletion-warning/ban/ban-appeal only; everything else in-app only.

### Upvote Batching
5-minute rolling window batch, per post/comment.

### UI
Bell (dropdown + /notifications page) separate from Message icon (Chat, own unread badge).

### Delivery Architecture
- Email: queue table + cron scan every 1 min (async)
- In-app: DB write (source of truth) + best-effort WebSocket push; no retry needed, client fetch-on-load covers gaps [Amended: thông báo dùng SSE thay WebSocket — DEC-135/QA-257]

### Preferences
No global category toggles. Per-post mute (comment/reply/upvote, not @mention) + per-conversation chat mute + global chat toggle.

### Retention
None — kept indefinitely.

### Issues Closed
ISS-098 through ISS-103

---
## Phase 5 — M08: Moderation Deep Dive

### Report System
Entities: Post/Comment/User/Group, each with tailored reason list. Login required. Evidence max 3 images/5MB. Case grouping by target while open.

### Report Queue
Priority = MAX severity + report_count×2. Claim-based (30min timeout) for multi-mod division.

### AI Scan
- Post: pre-scan (blocks publish)
- Comment: post-scan, velocity-triggered (reply burst detection), scans whole unscanned thread

### Warning System (revised)
LIGHT(7d,none) / MEDIUM(10d,no-post) / HEAVY(15d,no-post-comment+search-downrank). Fully private status.

### Ban System
Temp: 30d→90d→permanent (auto-escalation by ban count). Permanent: manual override. Always human-triggered.

### Audit Log
Admin full access; mod own-actions default; cross-mod visibility only during appeal review.

### False Report Detection
target_concentration metric, 90-day rolling window, reference-only (no auto-punishment).

### Issues Closed
ISS-104 through ISS-112

---
## Phase 5 — M09: Appeal Deep Dive

### Submission
Message (required) + evidence (optional, max 3 images/5MB).

### Banned User Access
Login works normally; locked screen post-login with appeal CTA; all endpoints blocked except appeal submit. Ban email links directly to /appeal.

### Deadlines
Warning = probation duration (7/10/15d). Temp ban = ban duration (30/90d). Permanent ban = 90 days flat. Content Deletion Appeal (Post only, added later) = 30 days flat.

### One Appeal Per Action
No resubmission after rejection.

### Queue
3 appeal types exist: Warning, Ban, Content Deletion (Post only). Warning/Ban share one queue, separate from Report. Content Deletion Appeal has its own separate queue (reuses the same claim-based mechanism). Priority across all: Ban > Warning > Content Deletion, FIFO within tier. Claim-based 30min timeout. Own-actions auto-excluded; sole-mod escalates to admin.

### Outcome
Approved ban → immediate ACTIVE (log kept, overturned flag). Approved warning → restriction lifted + warn count decremented.

### Content Deletion Appeal (added in Phase 5, amends original Phase 2 scope — DEC-115)
Scoped to Post only (Comment excluded — its point loss on violation removal is permanent, no appeal). Precedent: Reddit (admin-removal appealable ~6mo, subreddit-mod-removal not — confirms DEC-109 unchanged for Group-level moderation) and YouTube (content removal appeal window 1yr); iShare uses a shorter 30-day window given its smaller scale. Success outcome: content restored + deducted points refunded (DEC-113) + any warning/ban issued alongside that removal reversed via the same mechanism as a direct warning/ban appeal.

### Issues Closed
ISS-113 through ISS-118, ISS-144 (amendment)

---
## Phase 5 — M10: Admin Panel Deep Dive

### Scope Split
Admin-only: role management, system config, full audit log, mod account management. Shared with mod: moderation actions (report/warn/ban/appeal), topic/tag management.

### Role Management
Promote = proposal + user accept/decline. Demote = direct admin action, no consent, no appeal.

### System Config
AI toggle (master+per-module), maintenance mode, registration toggle, Should/Could feature flags, announcement banner. No email toggle. Policy constants (durations/thresholds) hardcoded, not UI-configurable.

### AI Toggle
Two-tier: master overrides all; per-module (Search/Moderation/Topic) apply only when master ON.

### Audit
All admin actions logged, append-only, view-only even for admin.

### Issues Closed
ISS-119 through ISS-123

---
## Phase 5 — M13: AI Layer Deep Dive

### Models
Embedding: text-embedding-3-small (pgvector, 1536-dim, HNSW). Topic suggestion: GPT-4o-mini. Moderation: OpenAI Moderation API.

### Moderation Coverage
Covers: harassment, hate speech, sexual content, violence. Does NOT cover: spam, plagiarism, misinformation (manual report only).

### Symmetric Threshold Design
One Moderation call → two branches (Content Gate + Warning), both using score≥0.9 (auto-action) / 0.5-0.9 (mod review) / <0.5 (no action). Shared across Post and Comment. Values tunable.

### Failure Handling
Admin-off (deliberate) uses per-module fallbacks. Transient failure (timeout 5s/10s + 1 retry w/2s delay) degrades per-request, routes moderation failures to mod review as safety net.

### Rate Limiting
No dedicated system — reuses search limits; Topic Suggest button gets 10/min/user.

### Issues Closed
ISS-124 through ISS-129

---
## Phase 5 — M11: Group Deep Dive

### Group Creation
Any logged-in user creates freely. Rate limit 5 groups/day/user (anti-spam). No cap on total groups owned.

### Role Permission Matrix
Owner: full control (promote/demote Group Mod, kick Mod/Member, change settings, delete group). Group Mod: pre-mod queue review, hide/delete content, kick Member only. Member: post/comment/vote only. Strict hierarchy — no role acts on a peer or superior (Group Mod cannot kick another Group Mod).

### Join Flow
Matrix by visibility × join-question presence: Public+no-question = instant join; everything else (has question, or Private) = requires Owner/Mod approval based on the answer. Rejected requests can be resubmitted immediately, no cooldown (matches Facebook/LinkedIn/Discord); Owner/Mod use per-user block for spam requesters instead.

### Content Moderation vs System-Wide M08
Group's AI-scan → Group Mod queue → Live flow is an additional publishing gate layered on top of, not a replacement for, system Report (M08) and "Mod/Admin can intervene anytime". Per-group post: score≥0.9 auto-reject; 0.5–0.9 mandatory Group Mod/Owner review regardless of pre-mod toggle; <0.5 follows the toggle. Group has its own claim-based pending-publish queue, separate from Report queue.

### Deletion & Membership Churn
Group deleted (Owner): soft-delete, content hidden from everyone (not hard-deleted). Reputation preserved except points tied to upvotes on content that vanished with the group (those are deducted). Member leaves/kicked (group survives): post stays as group asset, author shown normally, no point change; kicked = same as voluntary leave.

### Ownership Succession
Voluntary leave requires designating a successor first (blocking action); sole-member Owner leaving deletes the group instead. Involuntary loss (ban/deactivate/delete): auto-promote active Group Mod (longest tenure) → longest-tenured Member → group deleted if Owner was the only member.

### Visibility Change (Public↔Private)
Owner can toggle anytime. Posts already surfaced to a user's feed stay visible to them (locked from interaction if now Private); new feed/search queries exclude them for non-members.

### Appeal
No appeal path for group-level moderation actions — Group Mod/Owner decisions are final (contrast with system-level actions via M09).

### Discovery & Invite
Private groups fully hidden from search; reachable only via invite/link. Any member (not just Mod/Owner) can invite. Uses the same join-flow mechanism above, no separate Invitation entity.

### Feed Cross-Posting
Group posts always appear in the group's own member feed. Public group posts additionally surface on the main feed like ordinary posts; Private group posts never do.

### Anonymous Posting
Opt-in per-post when the group's anonymous toggle is ON (not forced group-wide). Turning the toggle OFF does not retroactively reveal past anonymous posts. Group Mod/Owner see real identity (same pattern as system-wide MOD/ADMIN, DEC-004/005).

### Group Size
No cap — unlimited membership and unlimited ownership per user.

### Issues Closed
ISS-130 through ISS-141


---

## Phase 5 — M09 Amendment: Appeal Scope Extended

Appeal scope, originally warn + ban only (Phase 2), is amended to add a new appeal type: **Content Deletion Appeal**, scoped to Post only (Comment excluded — posts are the higher-value asset, comment volume would overload the queue, consistent with DEC-004's post > comment value stance). Deadline: 30 days, fixed (narrower than Reddit's 6-month admin-removal appeal or YouTube's 1-year window, reflecting iShare's smaller scale; Reddit's subreddit-mod-removal has no platform-level appeal either, matching DEC-109's group-moderation-is-final stance). Mechanism: its own queue, separate from Report and from Warning/Ban Appeal, reusing the existing 30-minute claim-based mechanism. Priority: lowest of the three appeal types (Ban > Warning > Content Deletion). Success → content restored, deducted points refunded, any accompanying warn/ban reversed via the existing ISS-117 outcome-reversal mechanism.

Decision: DEC-115.

### Issues Closed
ISS-144

---

## Phase 5 — M12: Gamification Deep Dive

### Points & Vote Rules
Points = tổng upvotes nhận được, với trọng số khác nhau: Post Star = 2, Comment Star = 1 (DEC-116) — khớp tinh thần chống spam-comment-farm-reputation của DEC-004. Upvote là toggle, rút lại được, điểm trừ ngay lập tức khi rút (DEC-119). Không cho tự vote nội dung của chính mình — nút vote bị ẩn/disable trên content của chính tác giả (DEC-120).

### Content-Tied Point Deduction
Points tied to content are deducted only on a *direct* loss — the author self-deletes it, or a Mod/Admin removes it for that content's own violation. An *indirect* loss deducts nothing (e.g. a group is deleted by its Owner while the author was only a Member; a comment is cascade-hidden because its parent post was removed, whatever the removal reason). Timing: self-delete → deduction deferred until the 7-day soft-delete window closes; Mod/Admin violation removal → deducted immediately. This replaces the DEC-105 group-deletion point exception — group deletion no longer deducts points at all. (DEC-113)

### Badges
Chỉ dựa trên tổng điểm (không theo số bài đăng, không theo chủ đề). 5 mốc: Người mới nổi (25đ) / Cây bút triển vọng (100đ) / Cây bút tích cực (300đ) / Chuyên gia cộng đồng (600đ) / Huyền thoại iShare (1000đ). Badge vĩnh viễn, không thu hồi dù điểm sau giảm dưới ngưỡng (DEC-114), kể cả do point deduction hợp lệ (DEC-113). Chỉ hiển thị sau khi đã đạt — không hiện thanh tiến độ trước đó.

### Periodic Top-N Title
"Ngôi sao tuần" — chỉ áp dụng Weekly (không Monthly/All-time), N=3 (top 3 mỗi tuần) (DEC-117). Nếu hòa ở đúng hạng cắt N=3, tất cả user hòa đều nhận title (N là số tối thiểu, không cắt cứng) (DEC-123). Lịch sử thắng lưu vĩnh viễn qua audit trail riêng mỗi chu kỳ (như badge, DEC-114).

### Leaderboard Computation
3 window: Weekly / Monthly / All-time. Dùng 1 cron job duy nhất, chạy mỗi 60 phút — vừa refresh ranking hiển thị (cache, cho xem tạm), vừa kiểm tra chu kỳ vừa đóng để finalize bằng query chính xác theo đúng mốc thời gian (không dùng cache) rồi award title + notify (DEC-121). Điểm cá nhân trên profile vẫn real-time, chỉ riêng ranking tổng hợp là batch. Không hỗ trợ xem lại đầy đủ leaderboard các chu kỳ cũ — chỉ trạng thái hiện tại.

### Tie Handling
Hai user bằng điểm trên leaderboard → đồng hạng (giống xếp hạng thể thao, người tiếp theo nhảy số hạng), không cần tie-break phức tạp (DEC-123).

### Warn/Ban — Leaderboard Visibility (amends DEC-079)
User ở mức **HEAVY** warning bị ẩn hoàn toàn khỏi leaderboard công khai trong suốt thời gian probation — exception có chủ đích, amend private scope gốc của DEC-079 (chỉ HEAVY, không áp dụng MEDIUM/LIGHT) (DEC-118). **BANNED** account cũng bị ẩn khỏi leaderboard tương tự (nhất quán với HEAVY, DEC-122), nhưng profile/post/comment vẫn hiển thị bình thường cho người khác (không tombstone) vì Ban khác Delete — có thể unban qua appeal, và nội dung vi phạm cụ thể đã được xử lý riêng qua M08. Nhãn **"Tài khoản đã bị khóa"** hiển thị ở mọi nơi tên tác giả bị ban xuất hiện (profile + cạnh tên trên từng bài post/comment) — khác nguyên tắc private tuyệt đối của Warn, vì Ban là chế tài mang tính công khai hơn.

### Issues Closed
ISS-142, ISS-143, ISS-REWD-01, ISS-145, ISS-146, ISS-152, ISS-REWD-02, ISS-147, ISS-148, ISS-149, ISS-150, ISS-151, ISS-153, ISS-154

---

## Next: Phase 5 (Feature deep dive) and Phase 6 (Cross-cutting concerns) are both now complete — see module-registry.md amendments for full detail (M14/M15/M16 module deep dives + Phase 6 cross-cutting: timezone/i18n/data-retention/file-upload/AI privacy-hallucination-logging/analytics-events). Open items carried forward, none blocking: OPEN-001 (AI budget), OPEN-002 (tech stack), OPEN-003 (M16 Block/Report), OPEN-004 (M15 CSV export), OPEN-005 (event-tracking infra). Next step per BA-AGENT.md 9-phase protocol: **Phase 7 — Non-functional requirements** (performance, scalability & expected load, availability, security, privacy & personal data, reliability & backup, maintainability, portability, browser/device/OS support matrix, accessibility level, observability/monitoring — every NFR needs a measurable target).
