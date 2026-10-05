# Module Registry
> Phase 3 — Scope Decomposition | Status: **CLOSED (confirmed)**

## Module List

| ID | Module | MoSCoW | Dependencies | Notes |
|----|--------|---------|--------------|-------|
| M01 | Authentication & Account | Must | — | Registration (3-step onboarding), Google OAuth, email verify (magic link 1h), forgot password (magic link 15min), JWT + refresh token (1h/30d rotating), account_state (ACTIVE/DEACTIVATED/DELETED/BANNED) + verify_level (NONE/EMAIL_VERIFIED/SETUP_COMPLETED), deactivation 14d window, @mention system |
| M02 | User Profile | Avatar (Cloudinary/JPEG/PNG/WebP/10MB), bio 155ch, /u/{username} dual-context, tabs (owner: Posts+Bookmarks; visitor: Posts), followers/following public, points+badges display | Phase 5 Done |
| M03 | Post & Content | Tiptap editor (LaTeX/KaTeX/no-inline-img), 1 post type, optional poll (separate table), publish_state(6)/mod_state(3)/lock_level, pre-scan, attachments (img 5MB×10/doc 20MB×3), edit history, soft delete 7d | Phase 5 Done |
| M04 | Comment | 2-level threading, minimal editor (bold/italic/code/LaTeX/link/@mention/blockquote), upvote-only, 3-sort, edit unlimited, delete permanent (root tombstone if has replies), quote-reply, no attachments | Phase 5 Done |
| M05 | Topic & Tag | 11 flat topics, min1/max3 per post, AI suggest (max 3, is_stale handling), tag freeform (max5/post,30char), tags+post_tags tables, mod edit+merge topic only, trending rolling 7d window | Phase 5 Done |
| M06 | Search | Scope: Post(semantic/pgvector)+User+Tag+Topic+Group(pg_trgm), no Comment; ranking relevance(.8)+engagement(.2); filters(topic/tag/date/following); FTS+unaccent fallback; localStorage history; mixed results page; rate-limited; infinite scroll max120 | Phase 5 Done |
| M07 | Notification | Full event list (post/comment/mod/group/gamification/chat); email limited to security+ban only; upvote batched 5min; bell+page UI, separate chat icon; async email queue+cron; in-app DB+WebSocket best-effort; per-post/per-conversation mute (no global prefs); no retention policy | Phase 5 Done [Amended: thông báo dùng SSE thay WebSocket — DEC-135/QA-257] |
| M08 | Moderation | Report system (4 entities, tailored reasons, case grouping, claim-based queue); AI scan (post pre-scan, comment velocity post-scan); warning (AI auto+mod, 3 levels revised durations, private status); ban (temp escalation 30/90/permanent + manual permanent); audit log (admin full, mod own+appeal exception); false-report metric | Phase 5 Done |
| M09 | Appeal | Message+evidence submission; banned user locked-screen access; deadlines tied to punishment duration (perm ban=90d); 1 appeal/action; separate queue (ban>warning priority, own-action excluded, sole-mod escalate admin); reversal (ban→active, warning→count decrement) | Phase 5 Done |
| M10 | Admin Panel | Role mgmt (promote=proposal/accept, demote=direct); system config (AI master+per-module toggle, maintenance, registration, feature flags, banner); policy constants hardcoded not configurable; admin action log append-only | Phase 5 Done |
| M11 | Group | Should | M01, M03, M08, M13 | Public/Private group (visible-but-gated for private); Group roles (Owner/Moderator/Member); pre-moderation toggle; anonymous posting toggle (F-GRP-10, Owner-only); join question (optional). **Amended Phase 5 (M16 deep dive):** Group Chat is NOT part of Group — it is an independent multi-party chat feature, see M16 / ISS-163 |
| M12 | Gamification | Should | M01, M03, M04 | Points (Post Star=2, Comment Star=1; self-vote blocked; vote retractable); badge (5 mốc theo điểm: 25/100/300/600/1000 — permanent, never revoked, no progress bar); periodic top-N title (Weekly only, N=3, tie=all get it); leaderboard (Weekly/Monthly/All-time, single 60-min cron job, tied ranks share position, no historical view); HEAVY warn + BANNED excluded from leaderboard (amends DEC-079); BANNED shows public "Tài khoản đã bị khóa" label everywhere — Phase 5 Done |
| M13 | AI Layer | text-embedding-3-small(pgvector/HNSW)+GPT-4o-mini(topic)+Moderation API(4 categories only); symmetric 0.9/0.5 threshold (content-gate + warning branches); timeout 5s/10s+1retry; admin-off vs transient-failure distinct handling; AI-off fallbacks per module | Phase 5 Done |
| M14 | Feed & Discovery | Could | M03, M05 | 4 tabs: Trending (sub Post/Topic/Tag, decay DEC-124), Following, Group, Newest. **Amended Phase 5 (M14 deep dive):** dependency on M13 removed — no AI-driven personalization tab in current scope, see DEC-125 |
| M15 | Analytics & Stats | Could | M01, M03, M08 | ADMIN-only, 3 dashboard (User/Content/Moderation Stats), real-time query, preset time filter (Today/7d/30d/All-time), no export in MS1 (OPEN-004) |
| M16 | Chat & Messaging | Should | M01 | DM (1-1, open — any user can message any user, no follow required) + Group Chat (independent multi-party conversation, 3+ members, created freely by any user — NOT tied to Group/M11 membership in any way). **Amended Phase 5 (M16 deep dive):** original Phase 3 scoping said "Group Chat within Group" — corrected, see ISS-163. Dependency on M11 removed accordingly |

## Won't Have (v1)
- Video upload / streaming
- Mobile native app
- External integrations beyond OAuth

## MoSCoW Summary
| Priority | Count | Modules |
|----------|-------|---------|
| Must | 10 | M01–M10, M13 |
| Should | 3 | M11, M12, M16 |
| Could | 2 | M14, M15 |

## AI Module Fallback (DEC-008)
| Module | Fallback khi AI off |
|--------|-------------------|
| M06 Search | Full-text keyword search |
| M08 Moderation | Manual moderation queue only |
| M05 Topic | User tự chọn topic, không có gợi ý AI |

## Issues Resolved This Phase
| Issue | Summary | Resolution |
|-------|---------|------------|
| ISS-040 | Search scope & type | Semantic (post); exact match (user, tag); no comment search → QA-022 |
| ISS-041 | Chat scope | DM + Group Chat in scope → M16 → QA-023 (amended Phase 5, Group Chat is independent of Group/M11 — see ISS-163) |
| ISS-042 | AI Layer MoSCoW | Elevated to Must (M06/M08/M05 depend on it) → QA-024 |

## Decisions
- **DEC-008**: AI Layer Feature Flag — global toggle via Admin config or env var; defined fallback per module when AI is off.

## Phase 4 Feature Details

### M03 — Post & Content (updated)
| Feature | Description |
|---------|-------------|
| F-POST-01 | CRUD post (title, content_json, content_text) |
| F-POST-02 | Attachment upload (files only, no inline image) |
| F-POST-03 | Rich text editor (Tiptap / ProseMirror JSON) |
| F-POST-04 | Edit history (post_revisions table) |
| F-POST-06 | Soft delete (publish_state=deleted, deleted_at, 7d recovery) |
| F-POST-07 | 3-field status model (publish_state / mod_state / lock_level) |
| F-POST-08 | Pre-scan moderation (new post: pending → AI scan → active/under_review) |
| F-POST-09 | grade_level field (optional, user-selected, ENUM 10/11/12) |
| ~~F-POST-05~~ | ~~Anonymous post toggle~~ → moved to F-GRP-10 in M11 (DEC-009) |

### M11 — Group (updated)
| Feature | Description |
|---------|-------------|
| F-GRP-01 | Create / Edit / Delete group |
| F-GRP-02 | Group roles (Owner / Moderator / Member) |
| F-GRP-03 | Join public group |
| F-GRP-04 | Group pre-moderation toggle |
| F-GRP-05 | ~~Group Chat (via M16)~~ — REMOVED, see amendment below. Group Chat is independent of Group, not a Group feature |
| F-GRP-06 | Private group — visible-but-gated |
| F-GRP-07 | Invite link (direct join) |
| F-GRP-08 | Request join + Owner/Mod approval |
| F-GRP-09 | Optional join question (join_question TEXT NULL) |
| F-GRP-10 | Anonymous posting toggle (Owner-only, applies to new posts only) |

### Issues Resolved (Phase 4)
| Issue | Summary | Resolution |
|-------|---------|------------|
| ISS-043 | OAuth provider + account linking | Google OAuth + auto-link verified email → DEC-010 |
| ISS-044 | Post content types, status, scan policy | Tiptap, attachment-only, 3-field status, pre-scan → DEC-011/012/013 |
| ISS-045 | Comment nesting | 1 level only → QA-032 |
| ISS-046 | Classification depth + grade_level | 2 tiers (Category→Topic) + grade_level independent → QA-033/034 |
| ISS-047 | Search scope per entity | Post=pgvector+FTS, User=pg_trgm, Group=FTS, Comment=FTS → QA-035/036/037 |
| ISS-048 | Leaderboard period + filter | Weekly/Monthly/All-time windows, grade filter, global only → QA-038/039 |
| ISS-049 | Reward system | Points=upvotes, threshold badges, periodic top-N titles → QA-040/041 |
| ISS-050 | Report categories | 5 categories + Khác → QA-042 |
| ISS-051 | Follow scope | User / Topic / Post (not Group) → QA-043 |
| ISS-052 | Private group details | Visible-but-gated, invite link + request, 1 optional custom question → QA-044/045 |
| ISS-053 | Chat architecture | POST send + SSE receive, in-memory pub/sub → QA-046 |

### Decisions (Phase 4)
- **DEC-009**: Anonymous post = Group-level toggle by Owner (moved to M11)
- **DEC-010**: Google OAuth + auto-link verified email
- **DEC-011**: Soft delete, 7-day recovery window
- **DEC-012**: 3-field post status (publish_state / mod_state / lock_level)
- **DEC-013**: Pre-scan new posts; background re-scan edits; no retroactive scan on AI re-enable


---

## Amendment — Phase 5, M16 Chat & Messaging Deep Dive (2026-09-30)

M16 (Chat & Messaging) deep dive completed. Key correction: the original Phase 3/4 scoping described Group Chat as a feature *within* Group (M11) — this was wrong. Group Chat is a fully independent multi-party (3+) conversation feature, unrelated to Group/community membership. M16's dependency on M11 has been removed (M16 now depends only on M01). See `issue-queue.md` ISS-155–ISS-165 and `qa-log.md` QA-208–QA-224 for the full deep dive (message status/read-receipts, edit/delete policy, content scope, rate limiting, DM open-messaging policy, Group Chat governance, pagination/notification). One item remains open: **OPEN-003** — no Block or Report mechanism for chat messages in MS1 (deferred to a later phase).

M16 status: deep-dive substantially complete.

---

## Amendment — Phase 5, M14 Feed & Discovery Deep Dive (2026-10-01)

M14 (Feed & Discovery) deep dive completed. Feature list expanded from the original Phase 3 one-liner ("Personalized feed, trending posts") into 4 concrete tabs: **Trending** (3 sub-views — Post/Topic/Tag; Topic/Tag reuse DEC-052 unchanged, Post uses a new decay formula DEC-124), **Following** (chronological, reuses Follow targets from M07), **Group** (new — chronological feed aggregated from all groups the user has joined, Public+Private), **Newest** (chronological, site-wide, excludes Group-sourced posts). No algorithmic/AI-personalized "For You" tab was added — this removed M14's dependency on M13 (AI Layer); M14 now depends only on M03 (Post) and M05 (Topic & Tag), see DEC-125. Guest access, pagination (infinite scroll, 20/load, cursor-based), new-content notification (polling-based banner, not real-time), and BANNED/HEAVY-warn content visibility (not excluded, relies on existing label/privacy mechanisms) were also settled — see `issue-queue.md` ISS-166–ISS-188 and `qa-log.md` QA-225–QA-240 for the full deep dive.

M14 status: deep-dive complete, no open issues.

---

## Amendment — Phase 5, M15 Analytics & Stats Deep Dive (2026-10-01)

M15 (Analytics & Stats) deep dive completed. Feature list expanded from the original Phase 3 one-liner into 3 concrete ADMIN-only dashboards: **User Stats** (account status breakdown, registration trend, role breakdown, grade/Khối breakdown, warn-level breakdown), **Content Stats** (Post by publish_state/mod_state, post creation trend, Topic distribution, Comment trend), **Moderation Stats** (Report by status/category, Warn issued over time, Ban/Unban over time, Appeal by type/outcome). All metrics are derived from existing data — no new tracking infrastructure (DAU/WAU/MAU-style metrics were explicitly considered and dropped). Access is ADMIN-only (MOD access and a per-MOD "top report handler" leaderboard idea were both considered and dropped for complexity vs. Could-priority value). Time filter uses fixed presets (Today/7d/30d/All-time), no custom range. Computation is real-time (query-on-load), not batched — unlike Leaderboard (M12), admin traffic is low enough that this is not a performance concern. CSV export was explicitly deferred — see **OPEN-004**. See `issue-queue.md` ISS-178–ISS-184 and `qa-log.md` QA-241–QA-247 for the full deep dive.

M15 status: deep-dive complete. Open item: OPEN-004 (CSV export, deferred).

---

**Phase 5 status: all 16 modules' deep-dive interviews are now complete** (M01–M13 completed in earlier sessions; M11 amendment, M09 amendment, M12, M14, M15, M16 completed in this and the prior session). Remaining open items carried forward: OPEN-001 (AI budget), OPEN-002 (tech stack), OPEN-003 (M16 Block/Report), OPEN-004 (M15 CSV export) — none block spec writing for their respective modules; all are deliberate defers, not unresolved unknowns.

---

## Amendment — Phase 6: Cross-cutting Concerns (2026-10-01)

Phase 6 (Cross-cutting concerns) completed. Scope checked against the full BA-INTERVIEW-RULES.md Phase 6 checklist (auth/session, authorization, account lifecycle, audit logging, notification framework, search, file/media upload, moderation & reporting, i18n, timezone, config/feature flags, analytics events, data retention, plus the AI/LLM sub-checklist) — most items were found to already be resolved by individual module deep dives (M01 session/auth, M06 Search, M07 Notification, M08 Moderation, M10 Admin config, M13 AI Layer all cover their respective cross-cutting topic in depth already). Only genuinely open cross-cutting items were raised as new issues: **timezone & date handling** (DEC-127 — UTC storage, Asia/Ho_Chi_Minh business timezone, applies retroactively to every existing "N days/weeks" computation across M03/M08/M09/M12/M15), **i18n readiness** (DEC-128 — Vietnamese-only but i18n-key-ready architecture), **general data-retention principle** (DEC-129 — audit log & chat kept indefinitely; "only hard-delete when genuinely safe" principle formalized for the whole project), **file upload virus scanning** (DEC-130 — not needed, image-only + CDN transcode), and 4 AI/LLM-specific gaps not covered by M13's deep dive: **third-party data privacy disclosure** (DEC-131 — ToS/Privacy Policy page), **Topic Suggestion hallucination handling** (DEC-132), **AI decision output logging** (DEC-133 — new `ai_decision_log` table), and **analytics event-tracking infrastructure** (formalized as **OPEN-005**, deferred — no event-tracking beyond existing business-data-derived dashboards for MS1). See `issue-queue.md` ISS-189–ISS-196, `qa-log.md` QA-248–QA-255, and `decisions.md` DEC-127–DEC-133 for the full deep dive.

Phase 6 status: complete. Open item: OPEN-005 (event-tracking infra, deferred).

---

**Phase 6 complete. Per the BA-AGENT.md 9-phase protocol, next is Phase 7 — Non-functional requirements** (performance, scalability, availability, security, privacy, reliability/backup, maintainability, portability, browser/device/OS support matrix, accessibility, observability — each with a measurable target).

## Amendment — Phase 7 prep: Tech Stack confirmed (2026-10-04)

Tech stack confirmed (DEC-134–137, closes OPEN-002): Java + Spring Boot; React + Vite SPA (no SSR at MS1, OPEN-006) with shared UI Kit (base library OPEN-007); PostgreSQL + pgvector; Cloudinary; OpenAI; Tiptap JSON; JWT; Spring Mail + SMTP; SSE for all realtime (supersedes the WebSocket notes in M07); AI toggle in Admin Panel (DEC-092/093); no deployment at MS1. Next: Phase 7 (NFR) and Phase 8 (data model, per-module noun extraction → entities → system ERD, QA-262) — order to be confirmed.
