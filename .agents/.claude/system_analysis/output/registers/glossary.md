# Glossary

> Every domain term and acronym used in the project, as the stakeholder defines it.
> Seeded from the draft documents. Updated throughout the interview.

| Term / Abbreviation | Meaning | Source |
|---|---|---|
| iShare | The platform name — knowledge-sharing forum with AI assistance for high school students | Draft |
| THPT | Trung học phổ thông — Vietnamese high school (grades 10–12) | Draft |
| Post | The central content unit of the platform. Can represent a question, knowledge share, tutorial, discussion, review, resource, or news item. | Draft |
| Comment | A response or reply to a Post. Can be starred, reported, and accepted as an answer. | Draft |
| Accepted Answer | A Comment marked by the Post author as the best response. Only the Post author can set this (not AI, not Moderators). | Draft |
| Anonymous Post | A Post where the author's identity is hidden from other users. The system retains the real identity for moderation purposes. | Draft |
| Topic | A broad subject-area classification for Posts (e.g. Mathematics, Life Skills). Not limited to school curriculum. List to be finalized in BA. | Draft |
| Tag | A free-form keyword attached to a Post. More granular than Topic. A Post can have multiple Tags. | Draft |
| Lớp/Khối | Grade level classification: 10, 11, or 12. Applied to both Posts and user Profiles optionally. Used to personalize feed. | Draft |
| Post Star | An upvote/like action on a Post. Distinct from Comment Star; different weight in Reputation calculation. | Draft |
| Comment Star | An upvote/like action on a Comment. Distinct from Post Star; different weight in Reputation calculation. | Draft |
| Reputation | A numeric score reflecting a user's contribution quality. Calculated from Post Stars, Comment Stars, Accepted Answers received, and configurable rules. | Draft |
| Badge | An achievement awarded to a user for reaching milestones or contribution thresholds. | Draft |
| Leaderboard | A ranking of users by Reputation or contribution score. Available in 4 time periods: Weekly, Monthly, Yearly, All-time. | Draft |
| Group | A community space within the platform. Reuses Forum mechanics (Post/Comment/Star/Report). Can be public or private. | Draft |
| GroupMember | A user who has joined a Group, with a role within that group (owner / member). | Draft |
| Moderator (MOD) | A platform role with content moderation capabilities: hide/lock/delete posts and comments, review reports, warn/suspend/ban users. | Draft |
| Admin (ADMIN) | The highest platform role. All Moderator capabilities plus user management, role assignment, and system statistics. | Draft |
| USER | The standard member role. Can create content, interact, and report. | Draft |
| AI Assistance Layer | The set of 5 mandatory AI-powered features that support (not replace) human decision-making on the platform. Calls third-party AI APIs. | Draft |
| AI Moderation | Automated content screening for spam, toxic content, and policy violations. Returns prediction + confidence score. | Draft |
| AI Classification | Suggests Topic and Tags for a Post automatically. User/Moderator reviews before publish. | Draft |
| Semantic Search | Search using vector embeddings to find conceptually related content, not just keyword matches. Uses PostgreSQL + pgvector. | Draft |
| Summarization | AI-generated summary of a long Post or a long Comment thread. | Draft |
| Feedback / Evaluation Loop | System for tracking AI prediction accuracy over time (precision, recall, F1). Used to tune moderation thresholds — not to retrain models. | Draft |
| pgvector | PostgreSQL extension for storing and querying vector embeddings. Used for Semantic Search. | Draft |
| P0 | Delivery priority 0 — implemented first; forms the foundation for everything else. | Draft |
| P1 | Delivery priority 1 — implemented after P0 is stable. | Draft |
| P2 | Delivery priority 2 — polish and UX improvement phase. | Draft |
| BA | Business Analysis — this current phase. Produces system specification files. | Project |
| FR | Functional Requirement — a single verifiable behaviour the system must exhibit. | Project |
| BR | Business Rule — a constraint or rule governing system behaviour. | Project |
| AC | Acceptance Criterion — a testable condition in Given/When/Then format. | Project |
| NFR | Non-Functional Requirement — a quality attribute with a measurable target. | Project |
| MoSCoW | Prioritization framework: Must / Should / Could / Won't-for-now. | Project |


---

**Appeal (Khiếu nại):** Quy trình cho phép user phản đối một quyết định kiểm duyệt (warn hoặc ban). Trong code/spec dùng thuật ngữ `appeal`; trong UI hiển thị là "Khiếu nại". Chỉ áp dụng cho warn và ban — không áp dụng cho post/comment bị xóa.
