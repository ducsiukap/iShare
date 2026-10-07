# QA Log Register

> Every question asked and its recorded answer.
> This is the primary traceability source for functional requirements.
> Format: structured entries below — one block per QA pair.

---

### QA-001
- **Issue ref:** ISS-021
- **Phase:** 1 — Business Context
- **Question:** Timeline và deadline cho toàn bộ dự án, cụ thể là MS1 là khi nào?
- **Answer (stakeholder):** Còn khoảng 3 tháng — deadline MS1 là giữa/cuối tháng 12 năm 2026. Thời gian này được đánh giá là đủ để hoàn thành toàn bộ project.
- **Implication:** MS1 = mid/late December 2026. Đây là mốc cứng duy nhất tính đến thời điểm BA. Kế hoạch phát triển các phase tiếp theo cần fit trong ~3 tháng còn lại.
- **Traceability note:** Timeline 3 tháng cho 11 module + AI layer là áp lực cao. Cần phân tích MoSCoW kỹ ở phase Requirements để đảm bảo P0 deliverable đúng hạn.

---

### QA-002
- **Issue ref:** ISS-022
- **Phase:** 1 — Business Context
- **Question:** Definition of Done cho MS1 là gì? Tiêu chí chấp nhận được (acceptance) và tiêu chí lý tưởng (nice-to-have)?
- **Answer (stakeholder):** Chấp nhận được: hoàn thành giai đoạn dev, có sản phẩm demo, đầy đủ full chức năng. Nice-to-have/khuyến khích: hoàn thành thêm giai đoạn testing, có output test hoặc test cho một số chức năng core (chức năng/module nào được test sẽ quyết định khi dev xong). Deploy không bắt buộc cho MS1.
- **Implication:** DoD MS1 = dev complete + demo-ready + full feature. Testing là bonus. No deployment required. Điều này cho phép team tập trung vào feature completeness thay vì infra/devops cho MS1.
- **Traceability note:** "Full feature" ở đây bao gồm cả AI layer hoạt động live (confirmed QA-007). Demo sẽ dùng seeded data nhưng AI phải xử lý real-time khi có action mới.

---

### QA-003
- **Issue ref:** ISS-023
- **Phase:** 1 — Business Context
- **Question:** Success metric cho MS1 là gì và đo bằng cách nào?
- **Answer (stakeholder):** Chọn mô hình A — đủ tài liệu, demo, sản phẩm hoàn thiện. Vì demo cần data, có thể cần product metric — dự tính sẽ dump/seed data để tạo số liệu demo. Product metric thực tế sẽ không đo được ở MS1 vì chưa deploy.
- **Implication:** Success metric của MS1 là qualitative (feature completeness, demo quality) chứ không phải quantitative (DAU, post count thực tế). Seeded data phục vụ mục đích demo trực quan.
- **Traceability note:** Cần thiết kế seeder script đủ mạnh để tạo data demo phong phú (users, posts, comments, interactions, badges) — đây là deliverable phụ nhưng quan trọng cho ngày demo.

---

### QA-004
- **Issue ref:** ISS-024
- **Phase:** 1 — Business Context
- **Question:** Landscape cạnh tranh hiện tại — HS đang dùng gì để trao đổi học thuật?
- **Answer (stakeholder):** Hiện tại chủ yếu là Facebook (group/chat) và Zalo (chat/group chat). Forum học thuật chính thức hầu như không có. Quora tồn tại nhưng chỉ ở dạng Q&A thông thường, ít được dùng. Đáng chú ý: HS hiện ít có tinh thần chia sẻ — xu hướng là tự tìm lời giải hoặc hỏi AI (ChatGPT, etc.) thay vì chia sẻ cộng đồng.
- **Implication:** iShare không có competitor trực tiếp trong phân khúc HS Việt Nam. Thách thức lớn nhất không phải cạnh tranh mà là thay đổi hành vi (behavior change): từ "hỏi AI cá nhân" sang "chia sẻ cộng đồng". Gamification (BG-03) trở nên đặc biệt quan trọng để tạo động lực ban đầu.
- **Traceability note:** Insight "HS hay hỏi AI thay vì share cộng đồng" là cơ sở để thiết kế AI layer không phải thay thế mà là hỗ trợ và kéo user vào tương tác cộng đồng. AI gợi ý → user xem post → user tham gia thảo luận.

---

### QA-005
- **Issue ref:** ISS-025 (phần 1)
- **Phase:** 1 — Business Context
- **Question:** Business goals của hệ thống là gì? Đâu là mục tiêu ưu tiên nhất?
- **Answer (stakeholder — phần 1):** Quan trọng nhất là tạo văn hóa học tập cộng đồng. HS cần có nơi trao đổi về học thuật, tâm tư, tâm lý. Đề nghị BA gợi ý bổ sung thêm.
- **BA proposed (pending confirm):** Đề xuất 6 goals (A–F): A) Cộng đồng học tập; B) Peer review chất lượng; C) Safe space cho chủ đề nhạy cảm; D) Gamification/phần thưởng; E) Peer learning "học thầy không tày học bạn"; F) AI tăng hiệu quả vận hành.
- **Implication (partial):** Xem QA-006 cho kết quả cuối.

---

### QA-006
- **Issue ref:** ISS-025 (phần 2 — confirm goals)
- **Phase:** 1 — Business Context
- **Question (follow-up):** Confirm và tinh chỉnh danh sách business goals từ QA-005.
- **Answer (stakeholder):** Bỏ ý F (AI goal). Tinh chỉnh: D (gamification/phần thưởng) rất hay — cơ sở lý thuyết là Expectancy Theory (Vroom, 1964): con người hành động hiệu quả hơn khi biết sẽ có phần thưởng/kết quả rõ ràng khi đạt mục tiêu. E (peer learning) chính là tinh thần "học thầy không tày học bạn" — một trong số tinh thần cốt lõi của hệ thống. C mở rộng hơn safe space cho nhạy cảm — không gian thảo luận đa chiều cho HS. Cấu trúc cuối: A+E = 1 goal, D = 1 goal, C = 1 goal riêng (mở rộng), E = 1 goal riêng.
- **Confirmed Business Goals:**
  - **BG-01:** Xây dựng văn hóa học tập cộng đồng — tạo không gian chia sẻ học thuật và tâm tư cho HS (A)
  - **BG-02:** Phát huy tinh thần peer learning — "học thầy không tày học bạn"; tôn vinh giá trị tri thức từ bạn bè đồng trang lứa (E)
  - **BG-03:** Thúc đẩy đóng góp tích cực qua gamification — dựa trên Expectancy Theory (Vroom, 1964): người dùng hành động hiệu quả hơn khi thấy phần thưởng/kết quả rõ ràng từ đóng góp của mình (D)
  - **BG-04:** Tạo không gian thảo luận đa chiều cho HS — không chỉ học thuật mà cả tâm tư, đời sống, các chủ đề đa dạng phù hợp lứa tuổi (C mở rộng)
- **Implication:** 4 business goals này là nền tảng cho toàn bộ feature set. Gamification (BG-03) phải được thiết kế có chiều sâu lý thuyết. Peer learning spirit (BG-02) ảnh hưởng đến UX — cần tôn vinh người đóng góp rõ ràng.
- **Traceability note:** BG-03 có thể dùng trực tiếp trong phần "cơ sở lý thuyết" của báo cáo luận văn — Expectancy Theory là framework học thuật được công nhận rộng rãi (Vroom, V.H. 1964. Work and Motivation. New York: Wiley). BG-02 gắn với tục ngữ dân gian Việt Nam — có thể dùng làm trích dẫn văn hóa trong phần giới thiệu đề tài.

---

### QA-007
- **Issue ref:** ISS-026
- **Phase:** 1 — Business Context
- **Question:** AI budget hợp lý cho MS1 là bao nhiêu? Tính toán chi phí thực tế cho 5 AI features bắt buộc ở scale demo.
- **Answer (stakeholder):** Phạm vi demo: ~20–30 users, tổng 50–70 posts (không phải per day). Summarization chỉ áp dụng cho Post (không phải Comment thread). AI phải hoạt động live khi có action mới (không phải dummy/seeded AI response).
- **BA calculation (confirmed):**
  - Scale: 70 posts × embedding + 70 classifications + 70 moderations + 70 summarizations + ~200 semantic searches
  - AI Moderation: OpenAI Moderation API → **$0.00** (free dedicated endpoint)
  - AI Classification: gpt-4o-mini → ~$0.002
  - Semantic Search: text-embedding-3-small → ~$0.001
  - Summarization (Post only): gpt-4o-mini → ~$0.003
  - Feedback/Eval Loop: minimal overhead → ~$0.001
  - **Total: < $0.01** — khuyến nghị nạp $5 OpenAI credit để có buffer thoải mái
  - **Provider stack đề xuất:** OpenAI (Moderation API free + gpt-4o-mini + text-embedding-3-small)
- **Status:** OPEN — budget chưa chốt chính thức, $5 credit là estimate an toàn.
- **Traceability note:** AI cost ở đây là cho MS1 demo only. Production scale sẽ cần recalculate khi có số liệu thực. OpenAI Moderation API miễn phí là lợi thế lớn — loại bỏ cost cho feature quan trọng nhất (content safety).

---

### QA-008
- **Issue ref:** ISS-027
- **Phase:** 1 — Business Context
- **Question:** Kỳ vọng về production-readiness — hệ thống có cần sẵn sàng scale lên production sau MS1 không?
- **Answer (stakeholder):** MS1 là demo only. Nhưng hệ thống vẫn cần được xây đúng chuẩn production ngay từ đầu — sau deploy đỡ phải sửa nhiều. Tư duy: build for production, demo ở MS1.
- **Decision triggered:** Ngầm định production-ready architecture — không workaround, không hack for demo.
- **Implication:** Toàn bộ design decisions (DB schema, API design, auth, AI integration) phải theo production standard. Không được phép dùng shortcut "chỉ để demo" trừ khi được ghi rõ là technical debt.
- **Traceability note:** Điều này ảnh hưởng đến lựa chọn tech stack (stability > novelty), DB design (normalized, indexed đúng chuẩn), và AI integration (proper error handling, fallback khi AI unavailable).

---

### QA-009
- **Issue ref:** ISS-028
- **Phase:** 1 — Business Context
- **Question:** Sau khi bàn giao, ai giữ role ADMIN? Dev team, giáo viên/client, hay cả hai?
- **Context:** Câu hỏi ảnh hưởng trực tiếp đến thiết kế hệ thống: nếu chỉ dev team thì ADMIN là role kỹ thuật thuần túy, không cần flow bàn giao trong UI. Nếu cả hai thì cần "super admin pattern" — ADMIN có thể promote user khác lên ADMIN thông qua giao diện.
- **Answer (stakeholder):** Chọn C — cả hai. Dev team giữ quyền root ở cấp DB (không qua UI), đồng thời trong hệ thống có cơ chế ADMIN promote account khác thành ADMIN để bàn giao quyền vận hành (operation handover). Mục đích: sau MS1 có thể bàn giao operational admin cho giáo viên hoặc người được chỉ định mà không cần dev team can thiệp trực tiếp vào DB.
- **Decision triggered:** DEC-007 (Super Admin pattern — ADMIN có thể cấp quyền ADMIN cho user khác qua UI)
- **Implication:** Module ADMN cần thiết kế flow promote/demote ADMIN trong giao diện quản trị; dev team seed 1 root admin account từ DB khi khởi tạo hệ thống (via migration/seeder script).
- **Traceability note:** Pattern này phổ biến trong các hệ thống SaaS và forum (Discourse, Stack Overflow for Teams). Root admin được tạo qua migration/seeder, không expose qua UI đăng ký. Phù hợp với mô hình bàn giao học thuật: dev bàn giao credential root, client tự quản lý admin operation về sau.

---

### QA-010
- **Issue ref:** ISS-029
- **Phase:** 1 — Business Context
- **Question:** Có ràng buộc học thuật nào từ hội đồng/nhà trường về nội dung, scope, tài liệu, hoặc công nghệ không?
- **Answer (stakeholder — partial):** Không có ràng buộc đặc biệt về nội dung, scope hay tài liệu bắt buộc. Tech stack chưa được quyết định tại thời điểm này — sẽ xác nhận ở phase sau.
- **Status:** PARTIAL — ISS-029 giữ OPEN, chờ tech stack được chốt.
- **Traceability note:** Đây là điểm cần trace lại khi vào phase Architecture/Tech Stack — ràng buộc học thuật (nếu có) sẽ ảnh hưởng đến lựa chọn công nghệ và cấu trúc tài liệu nộp hội đồng.

---

### QA-011
- **Issue ref:** ISS-030
- **Phase:** 2 — Actors, Roles & Permissions
- **Question:** Guest (chưa đăng nhập) có quyền gì trên iShare?
- **Answer (stakeholder — confirmed):**
  - USR: Đăng ký, Đăng nhập
  - POST: Xem/đọc post (public + nội dung public group)
  - COMT: Xem comment
  - CLAS: Xem danh sách Topic / Tag / Khối lớp
  - GRP: Xem danh sách + mô tả + nội dung Group công khai; Private group ẩn hoàn toàn
  - REWD: Xem Leaderboard, Badges, Reputation score của user
  - AI: Xem AI Summary + AI Classification trên post
  - Report (POST/COMT): Không
  - Semantic Search: Không
  - INTR / MSG / ADMN: Không
- **Decision triggered:** Group có phân loại Public / Private. Guest chỉ tiếp cận Public group content.
- **New issue spawned:** ISS-GRP-01 (Phase 4 backlog) — deep dive Public vs Private group: ai tạo được private group, ai thấy private group tồn tại, cơ chế join private group, v.v.
- **Traceability note:** Cho Guest xem post + comment là quyết định quan trọng về SEO và discoverability — content iShare sẽ được index bởi search engine, tạo organic traffic. Không cho Guest dùng Semantic Search bảo vệ AI cost budget (ISS-026). Report yêu cầu auth để đảm bảo accountability và chống spam.

---

### QA-012
- **Issue ref:** ISS-031
- **Phase:** 2 — Actors, Roles & Permissions
- **Question:** USER trở thành MODERATOR bằng cách nào? Ai phong? Điều kiện gì?
- **Answer (stakeholder):** Do ADMIN chỉ định thủ công. Không có điều kiện bắt buộc (reputation, thâm niên, v.v.) — ADMIN toàn quyền quyết định.
- **Implication:** Module ADMN cần flow: ADMIN chọn user → promote thành MODERATOR. Không cần automated suggestion hay eligibility check.
- **Traceability note:** Mô hình đơn giản, phù hợp giai đoạn đầu của platform khi cộng đồng còn nhỏ. Nếu platform scale lên, có thể bổ sung reputation threshold sau — nhưng không thuộc scope MS1.

---

### QA-013
- **Issue ref:** ISS-032
- **Phase:** 2 — Actors, Roles & Permissions
- **Question:** MODERATOR mất role bằng cách nào?
- **Answer (stakeholder):** Chọn B + C — ba cơ chế:
  1. ADMIN revoke thủ công
  2. Auto-revoke khi MODERATOR bị ban (business rule bắt buộc — tránh lỗi logic role/state)
  3. MODERATOR tự từ chức (self-resign) — trigger flow tương tự ADMIN revoke nhưng do chính MODERATOR thực hiện
- **Implication:** Module ADMN cần 2 flow: (1) ADMIN revoke; (2) MODERATOR self-resign. Auto-revoke on ban là side-effect của ban action — cần ghi vào spec của feature Ban User.
- **Traceability note:** Self-resign có chi phí implement thấp nhưng giá trị UX cao — phù hợp với đối tượng HS có lịch học biến động. Auto-revoke on ban là business rule không thể thiếu để đảm bảo data consistency giữa role và account status.

---

### QA-014
- **Issue ref:** ISS-033
- **Phase:** 2 — Actors, Roles & Permissions
- **Question:** Một user có thể vừa là MODERATOR vừa là ADMIN không?
- **Answer (stakeholder):** Không cần — ADMIN đã có full quyền. Role là hierarchy đơn: USER < MODERATOR < ADMIN. ADMIN kế thừa toàn bộ quyền MODERATOR.
- **Decision triggered:** Role model = single-value hierarchy, không phải multi-role set.
- **Implication:** DB column `role` là enum đơn (USER/MODERATOR/ADMIN). Permission check: if role >= MODERATOR → có quyền mod; if role == ADMIN → có full quyền. Không cần role array hay junction table.
- **Traceability note:** Mô hình này (role hierarchy) phổ biến trong forum platforms (Discourse, phpBB). Đơn giản hơn RBAC thuần túy, phù hợp với scope 3 role cố định của iShare.

---

### QA-015
- **Issue ref:** ISS-034
- **Phase:** 2 — Actors, Roles & Permissions
- **Question:** Anonymous Post — danh tính ẩn với ai?
- **Answer (stakeholder):** Ẩn với USER thường. MODERATOR và ADMIN đều thấy danh tính thật — vì MOD có quyền ban/warn account, cần biết ai đăng để xử lý vi phạm.
- **Implication:** DB vẫn lưu `author_id` đầy đủ cho mọi post kể cả anonymous. UI hiển thị "Ẩn danh" với USER; MODERATOR/ADMIN thấy tên thật + link profile. API cần filter field `author` theo role người gọi.
- **Traceability note:** Quyết định này đảm bảo anonymous post không trở thành lỗ hổng kiểm duyệt. Pattern phổ biến: lưu đủ ở DB, ẩn ở presentation layer theo permission.

---

### QA-016
- **Issue ref:** ISS-035 + ISS-039
- **Phase:** 2 — Actors, Roles & Permissions
- **Question:** GroupMember có role riêng trong Group không? Group có toggle kiểm duyệt và quan hệ với system moderation như thế nào?
- **Answer (stakeholder):** 3 level trong Group: Owner / Group Moderator / Member. Group có toggle pre-moderation (Owner bật/tắt). Luồng moderation chọn Luồng 1: Submit → AI Moderation (auto, real-time) → nếu AI pass → vào queue Group Mod (nếu toggle ON) → Group Mod approve → Live. System MODERATOR và ADMIN vẫn có quyền can thiệp vào content trong group bất kỳ lúc nào — group không phải vùng tự trị.
- **Implication:** GRP module cần: (1) role field riêng trong GroupMember table (owner/moderator/member); (2) setting `pre_moderation: boolean` trên Group; (3) post trong group có thêm trạng thái `pending_group_approval` trong state machine; (4) Group Mod queue UI.
- **New issues spawned (Phase 4 GRP backlog):** ISS-GRP-01 (Public vs Private), ISS-GRP-02 (chi tiết flow post trong group — nhiều sub-issues).
- **Traceability note:** AI làm bộ lọc vi phạm nghiêm trọng (tự động, real-time); Group Mod tập trung vào curation chất lượng nội dung của group. Hai tầng có vai trò khác nhau, không chồng chéo. System MOD/ADMIN là tầng override cuối cùng — đảm bảo platform không có "vùng cấm" với kiểm duyệt hệ thống.

---

### QA-017
- **Issue ref:** ISS-036
- **Phase:** 2 — Actors, Roles & Permissions
- **Question:** Có actor hệ thống (background/automated) nào? Scope AI Moderation có bao gồm Comment không? AI Classification hoạt động theo cơ chế nào?
- **Answer (stakeholder — confirmed):**
  - AI Moderation scan cả Post lẫn Comment (OpenAI Moderation API free → không có lý do cost để giới hạn)
  - AI Classification: gợi ý Topic (không auto-gán) — user review và chọn lại nếu cần. Kết quả cuối cùng (user chọn gì) là feedback cho AI → đây chính là cơ chế Feedback/Evaluation Loop cho classification feature
  - Tag: user tự quyết định hoàn toàn, AI không can thiệp
- **Confirmed system actors:**
  1. **AI Moderation Worker** — scan Post + Comment mới, real-time
  2. **AI Classification Worker** — gợi ý Topic khi user tạo Post; nhận feedback từ lựa chọn cuối của user
  3. **Notification Worker** — gửi notification theo event (reply, vote, badge, mention, v.v.)
  4. **Badge/Reputation Engine** — tính điểm và trao badge tự động khi đủ điều kiện
- **Key insight:** Feedback/Evaluation Loop (AI feature thứ 5) được hiện thực hóa tự nhiên trong classification flow — không cần UI riêng. User chọn/sửa topic sau AI suggestion → system log delta → training signal.
- **Implication:** 4 system actors trên cần được document trong architecture. Notification Worker và Badge Engine là background jobs (queue-based hoặc event-driven). AI workers gọi OpenAI API sync hoặc async tùy latency requirement (cần clarify Phase 6).
- **Traceability note:** Feedback loop từ user behavior (implicit feedback) là pattern phổ biến trong recommender systems — không cần user "rate AI" explicitly. Delta giữa AI suggestion và user final choice là signal chất lượng tự nhiên nhất.

---

### QA-018
- **Issue ref:** ISS-037
- **Phase:** 2 — Actors, Roles & Permissions
- **Question:** User tự xóa tài khoản — data xử lý thế nào?
- **Answer (stakeholder — confirmed):**
  - Xóa tài khoản = soft delete, không hard delete
  - Account state machine:
    - ACTIVE → [user request delete] → DEACTIVATED (grace period: 14 ngày)
    - DEACTIVATED → [trong 14 ngày: vào trang kích hoạt + confirm email OTP] → ACTIVE
    - DEACTIVATED → [sau 14 ngày không kích hoạt] → DELETED (auto, vĩnh viễn)
    - ACTIVE → [mod warn] → ACTIVE (có flag cảnh báo)
    - ACTIVE → [admin/mod ban] → BANNED
    - BANNED → [admin unban] → ACTIVE
  - Login khi DEACTIVATED không tự kích hoạt lại — phải vào trang kích hoạt riêng + confirm email OTP
  - Profile của DEACTIVATED/DELETED user → hiển thị "người dùng không tồn tại"
  - Post của deleted account: vẫn hiển thị nội dung, author → "[Người dùng đã xóa tài khoản]"
  - Comment của deleted account: tombstone "[Bình luận từ tài khoản đã xóa]", giữ vị trí trong thread
  - Leaderboard: kỳ hiện tại giữ nhưng grayed out + nhãn "[Tài khoản đã xóa]"; kỳ tiếp loại khỏi tính toán
  - Badge: orphaned trong DB, không hiển thị khi account deleted
  - Admin/Mod không có quyền "xóa tài khoản" — chỉ warn hoặc ban
- **Implication:** USR module cần: (1) status enum trên account (ACTIVE/DEACTIVATED/DELETED/BANNED/WARNED); (2) scheduled job auto-delete sau 14 ngày DEACTIVATED; (3) reactivation flow với email OTP; (4) API filter author display theo account status.
- **Traceability note:** Grace period 14 ngày cân bằng giữa UX (cho phép đổi ý) và data hygiene (không giữ zombie accounts mãi). Email OTP để kích hoạt lại là bước xác thực quan trọng — tránh kích hoạt vô tình và đảm bảo chỉ owner tài khoản mới restore được.

---

### QA-019
- **Issue ref:** ISS-038
- **Phase:** 2 — Actors, Roles & Permissions
- **Question:** Ban user — ai có quyền, phạm vi, thời hạn, warn, AI authority, và appeal system?
- **Answer (stakeholder — confirmed):**
  - Ban/Unban: cả MOD và ADMIN, phạm vi toàn hệ thống
  - Ban có thời hạn (temporary) và vĩnh viễn (permanent) — period appeal thay đổi theo loại
  - Ban notification: email + link appeal; banned user vẫn login được, thấy màn hình thông báo + nút khiếu nại
  - AI authority: AI CÓ quyền warn trực tiếp (auto, cho borderline content); AI KHÔNG auto-ban; khi account đạt ngưỡng warn → AI escalate tạo ticket cho MOD/ADMIN review
  - Ngưỡng warn để escalate: TBD → Phase 4 ADMN backlog (ISS-ADMN-01)
  - Appeal system: build trang riêng trong hệ thống, 2 loại:
    1. Warn appeal → MOD hoặc ADMIN review
    2. Ban appeal → chỉ ADMIN review (MOD không tự review appeal của ban mình đã thực hiện)
  - Post/comment bị xóa: KHÔNG có appeal — nếu user thấy sai thì report MOD lên ADMIN
- **AI authority table confirmed:**
  - Flag content (internal): AI ✓
  - Warn account: AI ✓ (auto), MOD ✓, ADMIN ✓
  - Escalate warn threshold → ticket: AI ✓ (auto)
  - Ban/Unban: MOD ✓, ADMIN ✓; AI ✗
  - Review appeal: MOD ✓ (warn), ADMIN ✓ (warn + ban); AI ✗
  - Override AI warn: MOD ✓, ADMIN ✓
- **Implication:** ADMN module cần: appeal page (2 forms: warn/ban); ticket system cho AI escalation; ban notification email; banned user redirect flow; logic "MOD không review appeal của chính mình".
- **Traceability note:** Không cho appeal post/comment xóa giúp giữ moderation đơn giản và có thẩm quyền. Pattern "AI warns, human bans" là best practice trong content moderation — giữ human-in-the-loop cho quyết định nghiêm trọng, đồng thời tận dụng AI cho scale. Tham khảo: Discord auto-mod warns, human mod bans.

---

### QA-020
- **Issue ref:** ISS-038 (bổ sung) + ISS-AI-01 (sketch)
- **Phase:** 2 — Actors, Roles & Permissions
- **Question:** Warn system — levels, thresholds, probation, AI confidence threshold theo warn status?
- **Answer (stakeholder — confirmed):**
  - 3 warn levels: LIGHT (count 1–2) / MEDIUM (count 3–4) / HEAVY (count 5–6)
  - Warn mới không tăng level → chỉ reset probation timer
  - Probation auto-reduce level (không cần confirm): HEAVY 14 ngày → MEDIUM; MEDIUM 10 ngày → LIGHT; LIGHT 5 ngày → Clean
  - Account bị warn vẫn hoạt động bình thường — có indicator hiển thị theo level cho người khác thấy
  - Warn level ảnh hưởng đến AI confidence threshold (user warn nhiều → AI nhạy hơn, ngưỡng thấp hơn)
  - AI threshold sketch (số cụ thể negotiate Phase 6): Clean ~85% / LIGHT ~75% / MEDIUM ~65% / HEAVY ~55%
  - Threshold phụ thuộc vào LEVEL (không phải số lần warn active)
  - MOD có thể review appeal (warn + ban), trừ action của chính mình
  - Post/comment bị xóa: không có appeal
- **Issues spawned:**
  - ISS-AI-01 (Phase 6): AI confidence threshold calibration theo OpenAI Moderation API score range
  - ISS-REWD-02 (Phase 4): Warn level ảnh hưởng đến trust/reputation display — penalty % và recovery
- **Traceability note:** Dynamic confidence threshold theo user history là pattern phổ biến trong content moderation (trust & safety systems). "Repeat offender penalty" — người đã vi phạm nhiều lần được AI giám sát chặt hơn — cân bằng giữa fairness (first-time có lợi ích nghi ngờ) và safety (repeat offender ít khoan nhượng hơn). Số cụ thể phụ thuộc vào OpenAI Moderation API score distribution — cần empirical calibration ở Phase 6.

---

### QA-021
- **Issue ref:** ISS-038 (correction)
- **Phase:** 2 — Actors, Roles & Permissions
- **Correction:** Appeal review permissions — MOD không review được appeal từ action của chính mình (conflict of interest → escalate lên ADMIN). ADMIN review được TẤT CẢ appeal kể cả action ADMIN tự thực hiện — vì ADMIN là cấp cao nhất, không có cấp trên để escalate.
- **Implication:** Appeal routing logic: if appeal.issued_by == current_mod → redirect to ADMIN queue. ADMIN queue nhận tất cả không lọc.

---

## Phase 3 — Scope Decomposition

### QA-022
- **Issue:** ISS-040
- **Phase:** 3
- **Question:** Search nên dùng semantic hay full-text? Và search được entity nào?
- **Context:** Cần xác định loại search engine và phạm vi entity cho M06.
- **Answer:** Semantic search (embedding) cho Post body/title; exact/prefix match cho User và Tag. Comment không đưa vào search (quá nhiều, ít giá trị). Fallback full-text keyword khi AI off.
- **Decision triggered:** DEC-008 (AI Feature Flag covers M06 fallback)
- **Implication:** M06 depends on M13 (AI Layer); cần vector storage — flag vào OPEN-002 để resolve ở Phase 8.

---

### QA-023
- **Issue:** ISS-041
- **Phase:** 3
- **Question:** Chat scope: chỉ DM (1-1) hay bao gồm Group Chat?
- **Context:** Real-time chat chưa được đề cập trước Phase 3.
- **Answer:** Cả hai — DM giữa 2 user và Group Chat trong Group đều in scope. → M16 Chat & Messaging (Should).
- **Decision triggered:** M16 thêm vào module registry.
- **Implication:** M16 depends on M01 (auth) và M11 (group). Real-time infrastructure sẽ được flag ở Phase 7 (NFR).
- **AMENDED Phase 5 (M16 deep dive, 2026-09-30):** "Group Chat trong Group" là scoping sai — Group Chat là conversation multi-party độc lập hoàn toàn, không liên quan Group/M11. Dependency M16→M11 đã được gỡ bỏ. Xem ISS-163 / QA-221.

---

### QA-024
- **Issue:** ISS-042
- **Phase:** 3
- **Question:** AI Layer (M13) nên là Should hay Must? Vì M06/M08/M05 đều phụ thuộc vào nó.
- **Context:** M06 cần embedding, M08 cần OpenAI Moderation API, M05 cần topic suggestion — tất cả là Must.
- **Answer:** M13 AI Layer → **Must**. Nhưng vẫn là layer riêng biệt. Global feature flag (DEC-008) đảm bảo graceful degradation khi AI off.
- **Decision triggered:** DEC-008
- **Implication:** M13 là shared infrastructure cho M05, M06, M08. Cần thiết kế AI Layer như một service độc lập từ đầu.

---

### QA-025
- **Issue:** ISS-044 (partial)
- **Phase:** 4
- **Question:** Post content: inline image hay chỉ attachment?
- **Answer:** Không hỗ trợ inline image. Tất cả media phải là attachment (file đính kèm). Inline image làm phức tạp storage và scan.
- **Decision triggered:** F-POST-06 (attachment only, no inline image)
- **Implication:** Editor không có "insert image" inline. Upload → file list bên dưới bài viết.

---

### QA-026
- **Issue:** ISS-043
- **Phase:** 4
- **Question:** OAuth provider nào? Account linking strategy?
- **Answer:** Google OAuth (Sign in with Google). Auto-link by verified email khi email Google khớp email đăng ký. Gửi notification sau link. Không manual confirmation.
- **Decision triggered:** DEC-010
- **Implication:** M01 cần Google OAuth flow + email-match auto-link logic + notification trigger.

---

### QA-027
- **Issue:** ISS-044
- **Phase:** 4
- **Question:** Soft delete — window bao lâu?
- **Answer:** 7 ngày. `deleted_at` timestamp. Cron hard-delete sau 7 ngày. User tự khôi phục trong window nếu mod chưa removed.
- **Decision triggered:** DEC-011
- **Implication:** Cần cron job + recovery endpoint + UI "Bài viết đã xóa" trong profile.

---

### QA-028
- **Issue:** ISS-044
- **Phase:** 4
- **Question:** Post status model — ai quyết định trạng thái nào?
- **Answer:** 3 trường độc lập: `publish_state` (user), `mod_state` (system/mod), `lock_level` (author hoặc mod). Author lock comments của bài mình; Mod có thể lock thêm. User "xóa" = set publish_state=deleted; Mod "gỡ" = set mod_state=removed.
- **Decision triggered:** DEC-012
- **Implication:** Schema post cần 3 field + audit trail cho mod actions.

---

### QA-029
- **Issue:** ISS-044
- **Phase:** 4
- **Question:** mod_state: 'hide' vs 'remove' khác gì?
- **Answer:** Chỉ dùng `under_review` (tạm ẩn, AI/mod đang xét) và `removed` (đã gỡ vĩnh viễn bởi mod). Không có 'hide' riêng — under_review là trạng thái ẩn tạm thời.
- **Decision triggered:** DEC-012
- **Implication:** `mod_state` enum = pending / active / under_review / removed.

---

### QA-030
- **Issue:** ISS-044
- **Phase:** 4
- **Question:** Scan policy: pre-scan hay post-scan cho bài mới?
- **Answer:** Pre-scan cho post mới (ẩn với public, `mod_state=pending`, cho đến khi AI scan xong → active hoặc under_review). Background re-scan cho edit (không ẩn, nếu flagged → under_review).
- **Decision triggered:** DEC-013
- **Implication:** New post flow: save → mod_state=pending → hidden → AI scan → active/under_review. Cần pending state visible cho author.

---

### QA-031
- **Issue:** ISS-044
- **Phase:** 4
- **Question:** Khi AI được re-enable, có retroactive scan không?
- **Answer:** Không (Option C). Chỉ scan post mới từ thời điểm AI re-enable. Không scan lại existing posts.
- **Decision triggered:** DEC-013
- **Implication:** Đơn giản hóa re-enable flow. Admin cần được thông báo rõ khi re-enable: "posts created while AI was off won't be rescanned."

---

### QA-032
- **Issue:** ISS-045
- **Phase:** 4
- **Question:** Comment nesting — bao nhiêu cấp?
- **Answer:** 1 cấp duy nhất (reply to comment). Không có reply to reply. Tiktok pattern.
- **Decision triggered:** —
- **Implication:** M04 Comment: parent_comment_id nullable; depth check = 1 level max.

---

### QA-033
- **Issue:** ISS-046
- **Phase:** 4
- **Question:** Classification — 1 hay 2 tầng? Grade level tích hợp thế nào?
- **Answer:** 2 tầng: Category → Topic. `grade_level` là field độc lập trên Post (optional, user chọn). Không cross-validate grade với Category/Topic.
- **Decision triggered:** —
- **Implication:** Post schema: `category_id`, `topic_id`, `grade_level` (3 field riêng). AI gợi ý topic_id, user confirm. grade_level = user's explicit choice.

---

### QA-034
- **Issue:** ISS-046
- **Phase:** 4
- **Question:** grade_level trên User Profile — có tự động tăng theo năm không?
- **Answer:** Không tự động. User tự update. Hệ thống có thể gửi notification nhắc nhở đầu năm học. `grade_level` trên User và trên Post là 2 field độc lập, đều optional.
- **Decision triggered:** —
- **Implication:** User profile schema: `grade_level` ENUM('10','11','12') NULL. Notification template cho school-year reminder.

---

### QA-035
- **Issue:** ISS-047
- **Phase:** 4
- **Question:** Search scope — entity nào support search type nào?
- **Answer:** Post: semantic (pgvector) + FTS (tsvector). User: pg_trgm (display name substring). Group: FTS (name + description). Comment: không được search.
- **Decision triggered:** —
- **Implication:** M06 cần 3 search strategies: embedding, tsvector, pg_trgm. Không cần Elasticsearch.

---

### QA-036
- **Issue:** ISS-047
- **Phase:** 4
- **Question:** Tại sao dùng pg_trgm cho User thay vì prefix hay semantic?
- **Answer:** Vietnamese names: "Nam" không match prefix cho "Nguyễn Văn Nam". Semantic overkill cho name matching. pg_trgm handles substring match natively trong PostgreSQL.
- **Decision triggered:** —
- **Implication:** `CREATE EXTENSION pg_trgm;` trong DB schema. Index `gin(display_name gin_trgm_ops)`.

---

### QA-037
- **Issue:** ISS-047
- **Phase:** 4
- **Question:** Comment có search không? Accepted answer có embed không?
- **Answer:** Comment: FTS only (tsvector). Không semantic embed vì: upvote-based system (không có clean "accepted answer" entity đủ ổn định để embed); overhead dynamic top-N embedding không worth it. FTS đủ cho thesis scale.
- **Decision triggered:** —
- **Implication:** Comment tsvector index. Không cần comment embedding pipeline.

---

### QA-038
- **Issue:** ISS-048
- **Phase:** 4
- **Question:** Leaderboard — chu kỳ và filter như thế nào?
- **Answer:** Time windows: Weekly / Monthly / All-time (không reset score, chỉ sum upvotes trong window). Grade filter: 10 / 11 / 12 / all (all bao gồm cả users không có grade). Scope: global only (không per-group).
- **Decision triggered:** —
- **Implication:** Leaderboard query: `SUM(upvotes_received) WHERE created_at IN [window]`, optional grade filter.

---

### QA-039
- **Issue:** ISS-048
- **Phase:** 4
- **Question:** Leaderboard có per-group không?
- **Answer:** Không. Chỉ global.
- **Decision triggered:** —
- **Implication:** M12 không cần group-scoped leaderboard logic.

---

### QA-040
- **Issue:** ISS-049
- **Phase:** 4
- **Question:** Points tính theo gì? Badge loại nào?
- **Answer:** Points = tổng upvotes nhận được (thuần túy). Badges: threshold-based (ví dụ: 10 upvotes → "Người mới nổi") + periodic top-N title (ví dụ: "Ngôi sao tuần" cho top N người trong weekly leaderboard). Danh hiệu periodic reset mỗi chu kỳ.
- **Decision triggered:** —
- **Implication:** M12: `user_points` = cumulative upvotes. Badge engine: periodic cron check top-N + threshold check on each upvote event.

---

### QA-041
- **Issue:** ISS-049
- **Phase:** 4
- **Question:** "Người phát sao" là cá nhân top 1 hay top N?
- **Answer:** Top N (không chỉ 1 người). Số N chính xác sẽ được xác định khi design M12.
- **Decision triggered:** —
- **Implication:** Periodic title = top-N set, không phải winner-takes-all.

---

### QA-042
- **Issue:** ISS-050
- **Phase:** 4
- **Question:** Report categories — những loại nào?
- **Answer:** 5 categories + Khác: Spam / Nội dung không phù hợp / Sai lệch thông tin / Quấy rối / Bản quyền / Khác (free text).
- **Decision triggered:** —
- **Implication:** `report_category` ENUM với 6 values. Khác → `report_note` text field.

---

### QA-043
- **Issue:** ISS-051
- **Phase:** 4
- **Question:** Follow scope — user/topic/post/group?
- **Answer:** Follow: User (nhận noti khi họ post), Topic (nhận noti khi có post mới trong topic), Post (nhận noti mọi update/comment của post đó). Không follow Group (join/leave đã đủ semantics).
- **Decision triggered:** —
- **Implication:** `follows` table: `follower_id`, `target_type` ENUM('user','topic','post'), `target_id`. M07 Notification cần filter theo follow type.

---

### QA-044
- **Issue:** ISS-052
- **Phase:** 4
- **Question:** Private group có visible khi search không? Join flow như thế nào?
- **Answer:** Visible-but-gated: user tìm thấy group, thấy tên/description, nhưng không thấy nội dung cho đến khi join. Có thể join qua invite link (direct approve) hoặc request join (cần approval từ Owner/Moderator).
- **Decision triggered:** —
- **Implication:** Group listing cần `privacy` field. Content query phải check membership. Invite link có token.

---

### QA-045
- **Issue:** ISS-052
- **Phase:** 4
- **Question:** Private group có câu hỏi khi request join không?
- **Answer:** Có 1 field `join_question` (TEXT NULL) trong Group. Owner tự custom câu hỏi hoặc để null (không cần trả lời). User request join điền `answer` TEXT NULL trong join request.
- **Decision triggered:** —
- **Implication:** `groups.join_question TEXT NULL`. `group_join_requests.answer TEXT NULL`. Simple 1-field approach.

---

### QA-046
- **Issue:** ISS-053
- **Phase:** 4
- **Question:** Chat transport: WebSocket hay SSE? Pub/sub model?
- **Answer:** POST để gửi tin (đảm bảo delivery), SSE để nhận tin (server push, auto-reconnect, simpler infra). Pub/sub: in-memory `Map<chatId, Set<SSEConnection>>` (thesis scale). Không cần Redis pub/sub.
- **Decision triggered:** —
- **Implication:** M16: REST POST endpoint để gửi + SSE endpoint `/chat/:id/stream` để receive. In-memory pub/sub đủ cho 1 server instance.

---

### QA-047
- **Issue:** ISS-049 (follow-up)
- **Phase:** 4
- **Question:** Points có nên giảm theo thời gian (decay) không?
- **Answer:** Không. Points = cumulative upvotes, không decay. Time-window leaderboard (weekly/monthly) đã giải quyết bài toán freshness. Decay thêm complexity không cần thiết và counter-intuitive với user.
- **Decision triggered:** —
- **Implication:** Không cần cron job tính lại điểm. All-time score = tổng đóng góp suốt đời, dùng cho badge threshold. Leaderboard ranking dựa trên sum trong window, không phải total score.

---

## Phase 5 — M01: Authentication & Account

### QA-048
- **Issue:** ISS-054 | **Phase:** 5
- **Question:** Registration fields bắt buộc lúc đăng ký?
- **Answer:** email + password (Step 1 only). display_name + username required nhưng ở Step 3 sau verify.
- **Decision triggered:** DEC-014

### QA-049
- **Issue:** ISS-054 | **Phase:** 5
- **Question:** Email verification có bắt buộc không? Chưa verify làm được gì?
- **Answer:** Mandatory. Chưa verify → redirect Step 2 khi login. Google OAuth = đã verify, bỏ qua step này.
- **Decision triggered:** DEC-014, DEC-018

### QA-050
- **Issue:** ISS-054 | **Phase:** 5
- **Question:** Display name — nickname hay full name?
- **Answer:** Free-form. User tự chọn style — nickname, tên thật, sáng tạo tùy ý. Không unique.
- **Decision triggered:** DEC-015

### QA-051
- **Issue:** ISS-054 | **Phase:** 5
- **Question:** Có cần @username riêng ngoài display_name không?
- **Answer:** Có. Community platform cần mention, mention cần unique handle không có space. username: unique, min 3 max 20, alphanumeric+underscore.
- **Decision triggered:** DEC-015

### QA-052
- **Issue:** ISS-054 | **Phase:** 5
- **Question:** Display_name có unique không?
- **Answer:** Không. Username mới unique.
- **Decision triggered:** DEC-015

### QA-053
- **Issue:** ISS-054 | **Phase:** 5
- **Question:** Google OAuth — user có cần đặt username không?
- **Answer:** Có — Google không có username concept. display_name auto-fill từ Google (đổi được), username user tự đặt ở Step 3.
- **Decision triggered:** DEC-014

### QA-054
- **Issue:** ISS-054 | **Phase:** 5
- **Question:** Mention search — username hay display_name hay cả 2? Có support khoảng trắng trong query không?
- **Answer:** Cả 2 (pg_trgm). Spaces cho phép trong query. Trigger sau 1 char, debounce 300ms. Priority tiers theo context (Group vs Post).
- **Decision triggered:** DEC-020

### QA-055
- **Issue:** ISS-054 | **Phase:** 5
- **Question:** Mention render — hiện @ không? Stored như nào?
- **Answer:** Không hiện @. Chỉ display_name + brand highlight. Stored bằng user_id → auto-update nếu display_name thay đổi.
- **Decision triggered:** DEC-020

### QA-056
- **Issue:** ISS-054 | **Phase:** 5
- **Question:** Cho phép trim/edit label mention sau khi chọn không?
- **Answer:** Không. Node atomic — backspace xóa cả node. Tránh misrepresentation và complexity.
- **Decision triggered:** DEC-020

### QA-057
- **Issue:** ISS-055 | **Phase:** 5
- **Question:** Token strategy? Duration?
- **Answer:** JWT. Access token 1 giờ. Refresh token 30 ngày, rotating. refresh_tokens table trong PostgreSQL.
- **Decision triggered:** DEC-017

### QA-058
- **Issue:** ISS-055 | **Phase:** 5
- **Question:** Multi-device có làm SSE phức tạp hơn không?
- **Answer:** Không. Mỗi device = 1 SSEConnection độc lập trong Set<SSEConnection>. Pub/sub tự nhiên handle multi-device.
- **Decision triggered:** DEC-017

### QA-059
- **Issue:** ISS-056 | **Phase:** 5
- **Question:** Change password flow (biết pass cũ)?
- **Answer:** Old pass + new pass + confirm (trong Settings). Không revoke session khác — bình thường, không phải security event.
- **Decision triggered:** DEC-016

### QA-060
- **Issue:** ISS-056 | **Phase:** 5
- **Question:** Forgot password flow?
- **Answer:** Email → magic link 15 phút → nhập pass mới + confirm → revoke all other sessions → auto-login session mới.
- **Decision triggered:** DEC-016

### QA-061
- **Issue:** ISS-056 | **Phase:** 5
- **Question:** Google OAuth user nhấn "Quên mật khẩu"?
- **Answer:** Hiện thông báo "Tài khoản này đăng nhập qua Google, vui lòng dùng Google để đăng nhập".
- **Decision triggered:** DEC-016

### QA-062
- **Issue:** ISS-057 | **Phase:** 5
- **Question:** Account states đầy đủ là gì? Có state cho onboarding không?
- **Answer:** 2 fields: account_state ENUM(ACTIVE/DEACTIVATED/DELETED/BANNED) + verify_level ENUM(NONE/EMAIL_VERIFIED/SETUP_COMPLETED). Login gate check account_state trước, rồi verify_level.
- **Decision triggered:** DEC-018

### QA-063
- **Issue:** ISS-057 | **Phase:** 5
- **Question:** BANNED screen hiện gì?
- **Answer:** Lý do ban + thời gian khiếu nại còn lại (nếu còn) + nút khiếu nại (nếu còn) + nút OK.
- **Decision triggered:** DEC-019

### QA-064
- **Issue:** ISS-057 | **Phase:** 5
- **Question:** Deactivation window bao lâu? User có thể xóa thẳng không?
- **Answer:** 14 ngày window → auto-DELETED. Không có nút xóa trực tiếp — bắt buộc qua deactivate trước.
- **Decision triggered:** DEC-019

### QA-065
- **Issue:** ISS-057 | **Phase:** 5
- **Question:** Post/comment của user deactivated hiển thị như nào?
- **Answer:** Post → ẩn ("Nội dung không tồn tại"). Comment → content giữ nguyên, author name → "Tài khoản tạm thời vô hiệu hoá", avatar → placeholder.
- **Decision triggered:** DEC-019

### QA-066
- **Issue:** ISS-057 | **Phase:** 5
- **Question:** Sau khi hết 14 ngày auto-DELETED, comment hiển thị như nào?
- **Answer:** Tombstone đổi → "[Người dùng đã xóa]", PII bị wipe. Post vẫn ẩn như cũ.
- **Decision triggered:** DEC-019

---
## Phase 5 — M02: User Profile

| ID | Question | Answer |
|----|----------|--------|
| QA-067 | Profile page info? | Avatar, display_name, username, bio, points, badges, followers/following count+list, content tabs |
| QA-068 | Content tabs owner vs visitor? | Owner: Posts+Bookmarks; Visitor: Posts only |
| QA-069 | Followers/following list hidden? | No — fully public |
| QA-070 | Username change history on profile? | No — dropped, extra table not worth v1 |
| QA-071 | Avatar CDN + types? | Cloudinary; JPEG/PNG/WebP; max 10MB; old deleted on update |
| QA-072 | Animated GIF avatar? | No — complex CDN config, not worth it |
| QA-073 | Bio char limit? | UI 155 chars, DB VARCHAR(255) |
| QA-074 | Why 155 not 255? | Product UX decision; 155 ≈ meta description sweet spot |
| QA-075 | /u/{username} — one route or two? | One route, dual-context conditional rendering |
| QA-076 | Social links? | Dropped v1 — malicious link risk + off-platform pull |
| QA-077 | Points+badges on profile? | Display only; M12 handles logic |

---
## Phase 5 — M03: Post & Content

| ID | Question | Answer |
|----|----------|--------|
| QA-078 | LaTeX support + visual editor? | LaTeX/KaTeX raw input only; visual editor future extension |
| QA-079 | Inline image in editor? | No — all media as attachments below post |
| QA-080 | Post types needed? | 1 type only; poll as optional separate table |
| QA-081 | Poll: open or closed? | Closed poll — owner defines options, users vote only |
| QA-082 | publish_state values? | DRAFT/PENDING/PUBLISHED/HIDDEN/REJECTED/DELETED |
| QA-083 | mod_state values? | NORMAL/FLAGGED/HIDDEN |
| QA-084 | lock_level — who can set? | COMMENT_LOCKED: author or mod; FULLY_LOCKED: mod only; locked_by tracks who |
| QA-085 | Pre-scan: block or flag? | Block publish — stays PENDING until mod approves |
| QA-086 | Attachment types + limits? | Images 5MB×10; Docs 20MB×3 |
| QA-087 | Avatar size updated? | Yes — 5MB (down from 10MB) for consistency with attachment images |
| QA-088 | Poll expiry required? | Yes — expires_at NOT NULL; can extend or force-close with is_closed |
| QA-089 | Poll reopen after close? | No — permanent |
| QA-090 | Edit history for comments? | edited_at only; no full history UI |
| QA-091 | Soft delete recovery? | 7-day window; author sees "Đã xóa" tab on profile; restore → PUBLISHED |

---
## Phase 5 — M04: Comment

| ID | Question | Answer |
|----|----------|--------|
| QA-092 | Comment editor scope? | Minimal: bold/italic/inline-code/LaTeX/link/@mention/blockquote |
| QA-093 | Threading depth? | 2 levels only; reply-to-child stays in same thread |
| QA-094 | Downvote on comment? | No — upvote only; report for bad content |
| QA-095 | Comment sort options? | Top/Mới nhất/Cũ nhất; child always chronological |
| QA-096 | Comment edit time limit? | No limit |
| QA-097 | Comment delete behavior? | Permanent; root tombstoned if has replies; child hard deleted |
| QA-098 | Comment attachments? | Not supported |
| QA-099 | @Mention in comment triggers notification? | Yes, always |
| QA-100 | Quote-reply support? | Yes — blockquote auto-inserted on Reply click |

---
## Phase 5 — M05: Topic & Tag

| ID | Question | Answer |
|----|----------|--------|
| QA-101 | Topic vs Tag format? | Topic = structured category; Tag = free #hashtag, no spaces |
| QA-102 | Topic taxonomy structure? | Flat, 11 topics (grouped per 2018 curriculum + non-academic) |
| QA-103 | AI suggest topic limit? | Max 3 (matches max 3 topics/post cap) |
| QA-104 | Content changed after AI suggest? | Flag is_stale, soft warning, feedback only recorded when not stale |
| QA-105 | Tag max count/length? | Max 5 tags/post, 30 chars/tag |
| QA-106 | Trending calculation? | Rolling 7-day window, score = Σ(1+upvotes×2+comments×1), recalc every 15-30min |
| QA-107 | Topic/tag edit/delete by mod? | Topic: edit+merge, no delete. Tag: fully free, soft-delete only for crisis (name becomes reserved, non-tagifiable) |
| QA-108 | Comment tags? | Not needed — comments inherit parent post's topic/tag context |

---
## Phase 5 — M06: Search

| ID | Question | Answer |
|----|----------|--------|
| QA-109 | Search scope reconfirm — does it include Topic/Group? | Yes, expanded: Post+User+Tag+Topic+Group. Original Phase 3 (QA-022) only covered Post+User+Tag |
| QA-110 | User search — pgvector or pg_trgm? | pg_trgm on display_name+username, shared with M01 @mention. pgvector reserved for Post semantic search only |
| QA-111 | Post search trigger timing? | Submit-only (no debounce, too expensive) |
| QA-112 | Engagement weighting in ranking? | Upvotes weighted 2x vs comments 1x, consistent with trending formula |
| QA-113 | Search result filters? | Topic, Tag, date range, Following-only, Sort |
| QA-114 | Full-text fallback tech? | Postgres tsvector/tsquery + unaccent + pg_trgm |
| QA-115 | Autocomplete dropdown content? | User/Tag/Topic/Group prefix matches; no Post titles |
| QA-116 | Search history storage? | localStorage, not DB — max 10 entries |
| QA-117 | Results page layout? | Mixed single page, Post primary, others supplementary |
| QA-118 | Snippet highlighting complexity? | Semantic search has no literal keyword match to highlight reliably — skip highlighting entirely for simplicity |
| QA-119 | Guest search access? | Same as public browse |
| QA-120 | Private group in search? | Group entity (name) visible-but-gated always; group content (posts) only visible to members |
| QA-121 | Rate limit guest vs user? | Guest stricter (30/10) than logged-in user (45/20) — accountability difference |
| QA-122 | Pagination style? | Infinite scroll preferred over page numbers; capped at 120 total results |

---
## Phase 5 — M07: Notification

| ID | Question | Answer |
|----|----------|--------|
| QA-123 | Full notification event list? | Password/deactivation/follow/post lifecycle/upvote/comment/mention/report/warning/ban/appeal/group/gamification/chat — see DEC-065 table |
| QA-124 | Which events get email? | Only: password changed, deactivation warning, ban/unban, ban-related appeal. Rest in-app only |
| QA-125 | Digest email needed? | No |
| QA-126 | Upvote notify per-vote or milestone? | Per-vote, but batched within 5-min window to avoid spam |
| QA-127 | Follow-post (subscribe/watch) feature? | Not added — bookmark stays save-only, no notify subscription |
| QA-128 | Bell UI structure? | Dropdown (recent) + dedicated /notifications page |
| QA-129 | Chat notification UI? | Separate Message icon in navbar, not mixed with bell |
| QA-130 | Email delivery timing? | Async via queue table + cron every 1 min (not blocking, not real synchronous send) |
| QA-131 | In-app delivery mechanism? | DB write (source of truth) + best-effort WebSocket push; no retry cron needed (client fetch-on-load covers gaps) [Amended: thông báo dùng SSE thay WebSocket — DEC-135/QA-257] |
| QA-132 | Granular notification preferences? | Skipped for v1 — replaced by per-post mute + chat mute (global + per-conversation) |
| QA-133 | Notification retention policy? | None — kept indefinitely, matches Facebook/Twitter/Discord/GitHub practice |

---
## Phase 5 — M08: Moderation

| ID | Question | Answer |
|----|----------|--------|
| QA-134 | Report reasons same across entities? | No — tailored per entity (Post 8, Comment 7, User 2, Group 4) |
| QA-135 | Can guest report? | No, login required |
| QA-136 | Evidence upload for report? | Max 3 images, 5MB each; description optional except for "Khác" |
| QA-137 | Report outcome — who sees what? | Reporter: vague outcome only. Offender: detailed reason + punishment + appeal link |
| QA-138 | Multiple mods — how to divide report queue? | Claim-based lock system, 30-min auto-release on inactivity |
| QA-139 | Priority calc when case has mixed reasons? | MAX severity among reasons in case, not sum |
| QA-140 | Duplicate reports on same content? | Grouped into 1 case while open; each report keeps own data; resolved case's new reports open fresh case |
| QA-141 | Does comment need AI scan like post? | Yes but different mechanism — post-scan triggered by reply velocity, not pre-scan block |
| QA-142 | Scan scope on velocity trigger? | Whole thread (root+replies) not yet scanned with current content |
| QA-143 | Does edit alone re-trigger comment scan? | No — needs both edit AND next velocity trigger together |
| QA-144 | Can AI auto-issue warnings? | Yes, when confidence high; low confidence escalates to mod. AI never bans |
| QA-145 | LIGHT warning restrictions? | None — just a tracking/probation window |
| QA-146 | Warning status visibility? | Fully private — user + mod only, never public |
| QA-147 | Ban duration determination? | Escalation formula: 30d→90d→permanent based on ban count, or manual permanent override |
| QA-148 | Who can view moderation logs? | Admin: all. Mod: own actions, plus cross-mod visibility only when reviewing appeals |
| QA-149 | How to detect malicious/false reporting? | target_concentration metric (same-target dismissed report ratio) over rolling 90-day window, mod judgment only |

---
## Phase 5 — M09: Appeal

| ID | Question | Answer |
|----|----------|--------|
| QA-150 | What does an appeal submission contain? | Required message + optional evidence (max 3 images/5MB), same as report system |
| QA-151 | How does a banned user reach the appeal page? | Still logs in normally; sees locked "banned" screen with appeal button; all other endpoints blocked |
| QA-152 | Does ban email link directly to appeal? | Yes, protected route /appeal, redirects through login if needed |
| QA-153 | Appeal deadline for warning vs ban? | Warning: full probation period. Temp ban: full ban duration. Permanent ban: 90 days flat |
| QA-154 | Why not unlimited appeal window for permanent ban? | Practical concern — old cases years later lose context, mod turnover, no clean resolution path |
| QA-155 | Can the same action be appealed multiple times? | No — exactly once, rejected appeals are final for that action |
| QA-156 | Appeal queue shared with report queue? | No, separate — different assignment rule (exclude mod's own actions) |
| QA-157 | Appeal priority ordering? | Ban appeals prioritized over warning appeals, FIFO within tier |
| QA-158 | What happens when mod's own action is up for appeal? | Automatically hidden from their queue; if sole mod, escalates to admin |
| QA-159 | What happens on appeal approval? | Ban: immediate ACTIVE + log marked overturned. Warning: restriction lifted + warn count decremented |

---
## Phase 5 — M10: Admin Panel

| ID | Question | Answer |
|----|----------|--------|
| QA-160 | What's admin-exclusive vs shared with mod? | Admin: role mgmt/config/full-audit/mod-mgmt. Shared: moderation actions, topic/tag mgmt |
| QA-161 | Should policy constants be admin-configurable? | No — hardcoded, changed via deployment |
| QA-162 | Can admin promote any user to mod freely? | Yes, no eligibility conditions, but user can decline the proposal |
| QA-163 | Does demote need mod's consent? | No — direct, immediate, no appeal (not a punishment) |
| QA-164 | What system configs does admin panel need? | AI toggle, maintenance mode, registration toggle, feature flags, announcement banner |
| QA-165 | AI toggle — single switch or per-module? | Both — master toggle + granular per-module (search/moderation/topic) |
| QA-166 | Are admin's own actions logged? | Yes, append-only, viewable but not editable even by admin |

---
## Phase 5 — M13: AI Layer

| ID | Question | Answer |
|----|----------|--------|
| QA-167 | Which embedding model? | text-embedding-3-small (OpenAI, cheap, multilingual) |
| QA-168 | Where are embeddings stored? | pgvector, posts.embedding vector(1536), HNSW index |
| QA-169 | Which model for topic suggestion? | GPT-4o-mini |
| QA-170 | Does Moderation API cover all report reasons? | No — only harassment/hate/sexual/violence; spam/plagiarism/misinformation are manual-report-only |
| QA-171 | Does AI auto-reject content, not just flag? | Yes — score≥0.9 triggers auto-reject (post)/auto-hide (comment), skipping mod entirely |
| QA-172 | Same threshold for content gate and warning? | Yes, symmetric — both use 0.9/0.5 thresholds |
| QA-173 | Are thresholds final? | No — placeholder, needs tuning with real usage data |
| QA-174 | Admin-off vs transient AI failure — same handling? | No — admin-off uses defined module fallbacks; transient failure is per-request degradation with retry |
| QA-175 | Timeout duration for AI calls? | Fast APIs (moderation/embedding) 5s; LLM generation (topic) 10s |
| QA-176 | Retry behavior on AI failure? | Exactly 1 retry, sequential, 2s delay before retry |
| QA-177 | Failed pre-scan — auto-publish or hold? | Hold for mod review (safer than auto-publish) |
| QA-178 | Is there a dedicated AI rate limit system? | No — reuses existing search limits; only new limit is 10/min/user for Topic Suggest button |

---
## Phase 5 — M11: Group

| ID | Question | Answer |
|----|----------|--------|
| QA-179 | ISS-130: Group creation — ai tạo được, giới hạn gì? | Mọi user đã login tạo group tự do; rate limit 5 group/ngày/user (chống spam); không giới hạn tổng số group sở hữu |
| QA-180 | ISS-131: Role permissions matrix (Owner/Group Mod/Member)? | Owner full quyền (kick Mod/Member, promote/demote Mod, đổi setting, xóa group); Group Mod duyệt pre-mod queue, ẩn/xóa post-comment, kick Member (KHÔNG kick Mod khác/không promote); Member chỉ đăng bài/comment/vote |
| QA-181 | ISS-132: Join flow — public/private, join question xử lý sao? | Public+no-question=join ngay; mọi case khác (có question, hoặc private)=cần duyệt Owner/Mod theo câu trả lời. Reject xong cho gửi lại ngay (không cooldown, theo pattern Facebook/LinkedIn/Discord); Owner/Mod dùng block riêng cho case spam request |
| QA-182 | ISS-133: Group content moderation quan hệ với M08 system-wide thế nào? | System Mod/Admin vẫn giám sát toàn bộ qua Report (M08) + can intervene anytime (không bypass); AI scan/Group Mod queue chỉ là publishing gate bổ sung. Score≥0.9→auto-reject; 0.5-0.9→bắt buộc Group Mod/Owner xử lý (dù pre-mod ON/OFF); <0.5→theo toggle pre-mod. Group có queue "chờ duyệt publish" riêng, tách Report queue, cùng cơ chế claim-based 30 phút |
| QA-183 | ISS-134: Group deletion (Owner xóa) và member rời group: nội dung xử lý sao? | Xóa group: soft-delete (nội dung ẩn khỏi mọi user kể cả ex-member, không hard-delete DB); reputation tổng giữ nguyên; NGOẠI LỆ: point từ upvote content đã mất theo group bị trừ. Member rời/bị kick: post cũ giữ nguyên (tài sản group), tác giả hiện tên thật, point không đổi; kick = rời tự nguyện |
| QA-184 | ISS-136: Group size limit — số group tối đa 1 user tham gia/sở hữu? | Không giới hạn — join bao nhiêu group cũng được, làm Owner bao nhiêu group cũng được |
| QA-185 | ISS-137: Owner rời/mất khả năng thao tác: group chuyển quyền sở hữu thế nào? | Owner rời tự nguyện: bắt buộc chỉ định successor trước (blocking action); group chỉ còn 1 member (chính Owner) rời → group bị xóa. Owner bị block/deactivate/xóa (involuntary): tự động promote Group Mod active senior nhất → nếu không có Mod thì Member senior nhất → nếu chỉ còn Owner thì xóa group |
| QA-186 | ISS-138: Đổi visibility Public↔Private: post cũ trên main feed xử lý sao? | Đổi visibility bất kỳ lúc nào (Owner). Post đã hiện với user nào rồi thì giữ hiện (không rút lại) nhưng khóa tương tác nếu chuyển Private; feed/search query MỚI loại post này khỏi kết quả cho user không phải member |
| QA-187 | ISS-139: Group Mod/Owner xóa post (pre-mod) có qua Appeal (M09) không? | Không — hành động moderation cấp group không có cơ chế appeal, quyết định Group Mod/Owner là cuối cùng (khác hành động system Mod/Admin, vẫn qua M09 bình thường) |
| QA-188 | ISS-140: Private group: có hiện trong search/discovery không? Ai được invite? | Ẩn hoàn toàn khỏi search/discovery, chỉ vào được qua invite/link. Bất kỳ member nào (Member/Mod/Owner) đều invite được, không giới hạn riêng cho Mod/Owner. Join flow dùng lại cơ chế đã chốt ở ISS-132 (không có entity Invitation riêng) |
| QA-189 | ISS-141: Post trong group có cross-post ra main feed không? | Post luôn hiện trong feed của member group (Public/Private). Riêng Public group: post CÒN hiện như post thường trên main feed (visible non-member). Private group: không bao giờ lộ ra main feed |
| QA-190 | ISS-135: Anonymous posting trong group — cơ chế cụ thể? | Khi toggle bật: user tự chọn ẩn danh hoặc không cho từng post (opt-in per-post, không bắt buộc toàn bộ). Khi Owner tắt toggle: post đã đăng ẩn danh trước đó VẪN giữ ẩn danh (không bị de-anonymize retroactively). Group Mod/Owner thấy được real identity của anonymous author (giống pattern system-wide MOD/ADMIN, DEC-004/005) |

---
## Phase 5 — M09 Amendment + M12: Gamification (QA-191 → QA-193)

| ID | Question | Answer |
|----|----------|--------|
| QA-191 | ISS-142: Content-tied point deduction — trường hợp nào trừ, thời điểm nào? | Nguyên tắc trực tiếp/gián tiếp: trừ điểm CHỈ khi content mất đi do hành động trực tiếp của chính chủ (tự xóa post/comment của mình) hoặc do chính content đó bị Mod/Admin xóa vì vi phạm. KHÔNG trừ nếu content mất đi gián tiếp do hành động của người khác (group bị Owner xóa dù mình chỉ là Member; comment bị cascade-ẩn vì post cha bị xóa — dù post cha bị xóa vì lý do gì). Thời điểm trừ: tự xóa → trừ SAU KHI hết cửa sổ soft-delete 7 ngày (hard-delete xong) — nếu khôi phục trong 7 ngày thì chưa từng bị trừ, không cần cơ chế hoàn riêng; Mod/Admin xóa do vi phạm → trừ NGAY lập tức. Quyết định này thay thế ngoại lệ group trong DEC-105 (group deletion trước đây có trừ điểm, nay bỏ ngoại lệ đó — điểm được bảo toàn hoàn toàn khi group bị xóa) |
| QA-192 | ISS-143: Badge nên permanent hay revocable? Audit trail ra sao? | Permanent — không thu hồi badge dù điểm sau đó giảm xuống dưới ngưỡng (kể cả do case trừ điểm hợp lệ ở QA-191). Lý do: badge là cột mốc lịch sử đã đạt được (giống Stack Overflow/Duolingo), không phải chỉ số theo dõi liên tục; tránh phạt user vì lý do ngoài tầm kiểm soát; đơn giản hơn khi build (không cần logic recheck-revoke). Badge UI hiển thị kèm ngày đạt được thay vì chỉ số ngưỡng, tránh gây hiểu lầm khi điểm hiện tại thấp hơn ngưỡng. Audit: badge theo ngưỡng (permanent, 1 lần đạt) → 1 bản ghi audit (ngày đạt đầu tiên); danh hiệu periodic top-N (VD "Ngôi sao tuần", reset mỗi chu kỳ) → nhiều bản ghi audit (mỗi chu kỳ thắng là 1 sự kiện riêng) |
| QA-193 | ISS-144: Có nên mở appeal cho content bị xóa do vi phạm không? Phạm vi, deadline, cơ chế, outcome thế nào? | Có — amend lại quyết định Phase 2 (trước đây Appeal chỉ có Warning+Ban, KHÔNG có content deletion). Tiền lệ tham khảo: Reddit phân biệt admin-removal (có appeal chính thức, cửa sổ 6 tháng) vs subreddit-mod-removal (không có appeal chính thức cấp platform — khớp với DEC-109 Group-level moderation không đổi); YouTube: content removal appeal trong 1 năm, strike 6 tháng. Vì iShare quy mô nhỏ hơn nhiều, chọn deadline ngắn hơn: 30 ngày cố định. Phạm vi: CHỈ Post, KHÔNG áp dụng Comment (post là tài sản quan trọng hơn; comment volume cao dễ quá tải queue; nhất quán với Post Star ≠ Comment Star DEC-004 coi post có giá trị cao hơn). Cơ chế: queue riêng "Content Deletion Appeal" (tách khỏi Report và Warning/Ban Appeal), nhưng tái dùng cơ chế claim-based 30 phút đã có. Priority: thấp nhất trong 3 loại appeal (Ban > Warning > Content Deletion). Outcome khi thành công: (1) khôi phục content, (2) hoàn point đã trừ, (3) đảo ngược warn/ban đi kèm lần xóa đó nếu có — tái dùng đúng cơ chế outcome reversal đã có ở ISS-117 (warn: gỡ restriction + giảm warn_count; ban: unban ngay, log giữ overturned flag). Comment bị xóa do vi phạm: point bị trừ vẫn vĩnh viễn, không có đường khiếu nại |

## Phase 5 — M12: Gamification Deep Dive (QA-194 → QA-207)

| ID | Question | Answer |
|----|----------|--------|
| QA-194 | ISS-REWD-01: Badge dựa trên tiêu chí gì — chỉ điểm, hay thêm số bài/chủ đề? | Chỉ dựa trên tổng điểm (points). Không có badge theo số bài đăng hay theo chủ đề ở v1 |
| QA-195 | ISS-REWD-01: Danh sách badge cụ thể — bao nhiêu mốc, ngưỡng, tên gọi? | 5 mốc: Người mới nổi (25đ) / Cây bút triển vọng (100đ) / Cây bút tích cực (300đ) / Chuyên gia cộng đồng (600đ) / Huyền thoại iShare (1000đ). Ngưỡng đầu chỉnh khó hơn theo yêu cầu stakeholder (từ đề xuất ban đầu 10/50/150/400/1000) |
| QA-196 | ISS-145: Post Star vs Comment Star — trọng số cụ thể? | Post Star = 2, Comment Star = 1 |
| QA-197 | ISS-146: Periodic top-N title gắn chu kỳ nào, N bao nhiêu? | Chỉ Weekly ("Ngôi sao tuần"), N=3 |
| QA-198 | ISS-152: Hòa điểm ở đúng hạng cắt N=3 thì xử lý sao? | Cho tất cả user hòa ở hạng cắt đều nhận title (N là số tối thiểu, có thể vượt lên nếu hòa), không cần tie-break riêng |
| QA-199 | ISS-REWD-02: Warn level có ảnh hưởng hiển thị leaderboard/reputation không? | Có — nhưng chỉ HEAVY: ẩn hoàn toàn khỏi leaderboard công khai trong suốt thời gian probation. Đây là exception có chủ đích, amend DEC-079 (private scope gốc chỉ nói posts/comments/profile, nay thêm leaderboard eligibility là ngoại lệ công khai duy nhất). MEDIUM/LIGHT không bị ảnh hưởng |
| QA-200 | ISS-147: Upvote rút lại được không? Điểm xử lý ra sao? | Có — vote là toggle (bấm lại để hủy). Điểm người nhận trừ ngay lập tức khi rút, đối xứng với lúc cộng |
| QA-201 | ISS-148: Tự vote nội dung của chính mình có được phép không? | Không — hệ thống ẩn/disable nút vote trên chính content của tác giả, chặn gian lận từ gốc |
| QA-202 | ISS-153: Có cho xem lại leaderboard đầy đủ của các chu kỳ trước không? | Không — chỉ hiển thị trạng thái hiện tại của Weekly/Monthly/All-time (không lưu snapshot lịch sử). Lịch sử "từng đạt danh hiệu gì" vẫn giữ qua title/badge audit trail (DEC-114) |
| QA-203 | ISS-149: Leaderboard ranking tính real-time hay batch/cache định kỳ? | Batch — gộp thành 1 cron job duy nhất, chạy mỗi 60 phút. Job này vừa refresh ranking hiển thị (cho xem tạm), vừa kiểm tra "có chu kỳ nào vừa đóng chưa" — nếu có, tính lại ranking cuối cùng bằng query chính xác theo đúng mốc thời gian chu kỳ (không dùng số liệu cache), rồi award title + gửi notification. Trễ tối đa 60 phút so với giờ đóng chu kỳ thực, nhưng người thắng luôn đúng |
| QA-204 | ISS-154: Tài khoản bị BAN — có ẩn khỏi leaderboard không? Profile/post/comment còn hiển thị cho người khác không? | Ẩn khỏi leaderboard trong suốt thời gian bị ban (nhất quán với HEAVY warn, mở rộng DEC-118). Nhưng profile/post/comment vẫn hiển thị bình thường cho người khác (không tombstone, không ẩn) — vì Ban khác Delete: có thể unban qua appeal, và nội dung vi phạm cụ thể đã được xử lý riêng qua M08 Report/Moderation, không liên quan đến việc khóa tài khoản |
| QA-205 | ISS-154 (bổ sung): Nhãn "tài khoản bị khóa" hiển thị ở đâu? | Ở MỌI nơi tên tác giả xuất hiện — trang profile, và cạnh tên tác giả trên từng bài post/comment họ từng đăng. Nhãn: "Tài khoản đã bị khóa" (khác với "Tài khoản tạm thời vô hiệu hoá" dùng cho Deactivate — DEC-019). Khác nguyên tắc private tuyệt đối của Warn (DEC-079) — Ban là mức phạt nặng hơn, mang tính công khai |
| QA-206 | ISS-150: Hai user bằng điểm nhau trên leaderboard thì xếp hạng thế nào? | Đồng hạng — cả hai cùng hiển thị chung 1 thứ hạng, người tiếp theo nhảy số hạng (giống xếp hạng thể thao/Olympic). Không cần tie-break riêng, nhất quán với nguyên tắc đã chốt ở ISS-152 |
| QA-207 | ISS-151: Badge chưa đạt có hiển thị tiến độ (VD "150/300 điểm") không? | Không — chỉ hiện badge sau khi đã đạt được, không hiện thanh tiến độ trước đó |

---

## Phase 5 — M16: Chat & Messaging (QA-208 → QA-224)

| ID | Question | Answer |
|----|----------|--------|
| QA-208 | ISS-155: Trạng thái tin nhắn có cần lưu field/enum riêng trên message không? | Không — "đã xem" không phải thuộc tính của riêng tin nhắn mà là quan hệ giữa tin nhắn và người đọc, suy ra bằng cách so `id`/`created_at` của tin với mốc đọc gần nhất của người nhận. 2 trạng thái hiển thị ở tầng UI (computed, không lưu DB): "Đã gửi" (mặc định) và "Đã xem" (chỉ hiện ở tin nhắn cuối cùng trong conversation, không rải theo từng tin lịch sử) |
| QA-209 | ISS-155: Mốc đọc ("last read") lưu ở đâu, dùng timestamp hay message id? | Lưu `last_read_message_id` (FK tới `messages.id`, không dùng timestamp để tránh lệch đồng hồ client/server) trên bảng `conversation_members` (1 dòng/user/conversation) — dùng chung cho cả DM và Group chat. Update qua `UPDATE ... SET last_read_message_id = GREATEST(last_read_message_id, :new_id)` để chống trường hợp request đến lệch thứ tự làm lùi mốc đã đọc. Không cần bảng riêng lưu "đã đọc tin nào" theo từng dòng tin/user (sẽ phình theo N tin × M thành viên) |
| QA-210 | ISS-155: Trigger nào cập nhật mốc đã đọc khi có tin nhắn mới tới lúc đang mở sẵn conversation? | Kết hợp 2 điều kiện qua client: (1) tab/window đang focus — dùng Page Visibility API (`document.hidden`), nếu tab ẩn thì đợi tới khi `visibilitychange` bắn lại mới tính; (2) đang ở đáy danh sách tin nhắn — dùng `IntersectionObserver` trên 1 sentinel ở cuối danh sách, nếu đang cuộn đọc tin cũ thì tin mới KHÔNG tự cuộn xuống, chỉ hiện badge "tin nhắn mới", đợi user tự cuộn xuống chạm đáy mới mark-as-read. Khi cả 2 điều kiện đúng, debounce ~500ms–1s trước khi gọi API mark-as-read (tránh gọi dồn dập khi tin đến liên tục) |
| QA-211 | ISS-155: Group chat "đã xem" hiển thị kiểu nào — avatar từng người (Messenger) hay ẩn hoàn toàn chỉ dùng nội bộ (Slack)? | Chọn kiểu Messenger — hiện avatar của (các) thành viên đã đọc kịp **tin nhắn mới nhất** ngay dưới tin đó (nhiều người cùng mốc thì gộp avatar). Thành viên nào chưa đọc kịp tin mới nhất thì không hiện avatar ở đâu cả (không rải theo lịch sử, chỉ áp dụng cho tin cuối cùng — nhất quán với QA-208). Cách này loại bỏ luôn nhu cầu xử lý case "mốc đọc trỏ tới tin chưa được load/phân trang", vì tin mới nhất luôn có sẵn ngay khi mở conversation. DM dùng chung 1 cơ chế (chỉ là trường hợp đặc biệt 1 avatar duy nhất) |
| QA-212 | ISS-155: Khi 1 người bấm đã đọc, những người còn lại trong conversation có cần được báo real-time không? Cơ chế nào? | Có, bắt buộc — nếu không thì avatar "đã xem" phía người khác không tự cập nhật (phải F5 mới thấy). Tái dùng hạ tầng SSE + pub/sub `Map<chatId, Set<SSEConnection>>` đã có sẵn cho tin nhắn (QA-046) — không mở kết nối riêng. Server sau khi update `last_read_message_id` thành công sẽ broadcast 1 event kiểu mới (`event: read_receipt`, data `{user_id, last_read_message_id}`) tới các connection khác đang subscribe conversation đó; không cần debounce thêm ở server vì tần suất đã được kiểm soát từ debounce phía client (QA-210) |
| QA-213 | ISS-158: Tin nhắn có cho phép sửa nội dung sau khi gửi không? | Không — không cho sửa tin nhắn dưới bất kỳ hình thức nào sau khi đã gửi |
| QA-214 | ISS-158: Tin nhắn có cho xóa không? Nếu có, soft-delete (tombstone) hay hard-delete? | Cho xóa — chọn soft-delete kiểu tombstone: nội dung gốc bị xóa hẳn (không giữ lại kể cả cho mod xem lại, vì chat là kênh riêng tư, không thuộc phạm vi moderation như Post/Comment), thay bằng placeholder "Tin nhắn đã bị thu hồi" giữ nguyên vị trí trong luồng chat — nhất quán UX với Messenger/Zalo mà học sinh đã quen dùng, tránh hụt ngữ cảnh hội thoại so với hard-delete không dấu vết |
| QA-215 | ISS-158: Thu hồi tin nhắn áp dụng cho 1 phía hay cả 2 phía? Có cần thêm kiểu "xóa chỉ mình tôi thấy" riêng không? | Chỉ 1 kiểu xóa duy nhất — thu hồi luôn cho CẢ 2 phía cùng lúc. Không có thêm tùy chọn "xóa chỉ ở phía tôi" tách biệt, giữ scope đơn giản cho MS1 |
| QA-216 | ISS-158: Giới hạn thời gian cho phép thu hồi tin nhắn là bao lâu? | 5 phút kể từ lúc gửi (`now() - created_at <= 5 minutes`) — đủ để xử lý tình huống phổ biến nhất (gửi nhầm người/nội dung, phát hiện gần như ngay lập tức), đồng thời đủ ngắn để tránh phá vỡ mạch hội thoại khi tin đã được đọc/phản hồi. Sau 5 phút, tin nhắn không còn cách nào xóa/ẩn được nữa — vĩnh viễn |
| QA-217 | ISS-159: Tin nhắn hỗ trợ nội dung gì — text only, hay thêm emoji/đính kèm ảnh-file? | Text + emoji cho MS1. Đính kèm ảnh/file: ngoài phạm vi MS1, để mở rộng ở phase sau. Không có AI Moderation quét nội dung chat (khác Post/Comment) vì chat là kênh riêng tư |
| QA-218 | ISS-160: Không có AI Moderation, chat cũng không nằm trong Report system (M08) — vậy harassment/quấy rối qua DM xử lý thế nào? | Sau khi cân nhắc trade-off giữa Report-only (chỉ xử lý được sau, không ngăn tin nhắn tiếp tục trong lúc chờ mod) và Block (kiểm soát tức thời nhưng phát sinh câu hỏi scope: level nào, ảnh hưởng content/leaderboard/group chat hay không) — quyết định: KHÔNG làm Block, KHÔNG làm Report cho tin nhắn ở MS1. Đánh dấu OPEN-003, để lại xử lý ở phase sau |
| QA-219 | ISS-161: Rate limiting cho chat — có cần không, mức nào? | Có — 30 tin nhắn/phút theo từng cặp (người gửi, conversation). Mục đích khác Search (không phải giới hạn chi phí AI — chat không gọi AI) mà để chặn spam/bot flood, bảo vệ server, và là lớp chặn kỹ thuật tối thiểu bù cho việc chưa có Block/Report (OPEN-003). Chọn per-conversation (không phải global) để chặn đúng trọng tâm (1 người spam 1 target cụ thể) mà không cản trở họ nhắn ở chat khác. 30 tin/phút nhanh hơn tốc độ gõ người thật, không ảnh hưởng use case hợp lệ |
| QA-220 | ISS-162: Ai nhắn tin (DM) được cho ai — mở hoàn toàn, cần mutual follow, hay message request kiểu Messenger? | Mở hoàn toàn — bất kỳ user nào cũng nhắn DM được cho bất kỳ user nào khác, không cần follow, không có cơ chế message request riêng. Làm rộng thêm bề mặt rủi ro đã ghi ở OPEN-003, nhưng đã có rate limit (QA-219) làm lớp chặn tối thiểu |
| QA-221 | ISS-163: Group Chat có phải kênh gắn liền với Group (M11) không? | Không — correction so với QA-023 (Phase 3 scoping ban đầu ghi nhầm "Group Chat within Group"). Group Chat là loại conversation multi-party (3+ người) hoàn toàn độc lập, ai cũng tạo được, không liên quan gì tới việc có chung Group/cộng đồng nào hay không. Đã cập nhật module-registry.md: bỏ dependency M16→M11 |
| QA-222 | ISS-164: Group Chat — quản trị ra sao (role, add/remove, kiểm duyệt, đổi tên, rời nhóm, kế nhiệm Admin, giới hạn size)? | Follow: mở, giống DM (QA-220). Role: Admin (người tạo) + Member. Add: cả 2 role đều add được. Remove: chỉ Admin xóa được thành viên, Member không xóa được ai. Kiểm duyệt: Admin bật/tắt toggle; bật thì thêm thành viên mới cần Admin duyệt (không phải Member). Đổi tên nhóm: mọi thành viên. Rời nhóm: tự do, tách biệt hoàn toàn với bị Admin xóa. Admin rời: bắt buộc chủ động chuyển quyền cho người khác trước (không có auto-promote hệ thống như Owner ở Group M11/QA-185). Giới hạn: 100 thành viên/Group Chat — đủ cho use case thực tế (nhóm lớp, CLB, nhóm ôn thi) mà không biến Group Chat thành kênh broadcast giả |
| QA-223 | ISS-165: Tin nhắn mới có gửi email notification không? | Không — chỉ in-app, khớp mặc định đã chốt ở QA-124 (email chỉ dành cho password/deactivation/ban/appeal), không thêm ngoại lệ riêng cho chat |
| QA-224 | ISS-165: Pagination lịch sử chat — cơ chế và số lượng/lần load? | Infinite scroll (cuộn lên trên để load tin cũ hơn), 20 tin/lần, cursor-based theo `message_id` (nhất quán pattern Search QA-097). Khác Search: KHÔNG có giới hạn tổng số tin tối đa — user phải cuộn được tới tận tin nhắn đầu tiên của conversation, không có khái niệm "hết mức độ liên quan" như kết quả search |

## Phase 5 — M14: Feed & Discovery (QA-225 → QA-240)

| ID | Question | Answer |
|----|----------|--------|
| QA-225 | ISS-168: M14 Feed có những tab/view nào? | 3 tab ban đầu: Trending (sub Post/Topic/Tag) + Following (chronological, theo Follow M07) + Newest (chronological toàn site). Không có tab "For You" thuật toán cá nhân hóa riêng. (Sau đó mở rộng thành 4 tab — xem QA-229) |
| QA-226 | ISS-185: Trending Post dùng công thức/decay nào? | Trending Topic/Tag giữ nguyên DEC-052 (rolling 7-day hard window, không decay). Trending Post dùng công thức mới — DEC-124: exponential half-life decay, `weight=0.5^(age_days/7)`, cắt hẳn về 0 sau 28 ngày (4 tuần). Lý do chọn 4 tuần: bội số sạch của half-life 7 ngày (4 nửa chu kỳ → còn 6.25%, gần như không đáng kể), nhất quán thuật ngữ "theo tuần" dùng xuyên suốt hệ thống, tránh số lẻ như 1 tháng (30/7≈4.29) |
| QA-227 | ISS-166: Guest (chưa đăng nhập) xem được gì trong Feed? | Guest xem đầy đủ Newest + Trending (cả 3 sub, không giới hạn riêng sub nào vì Trending Topic/Tag còn công khai hơn cả Post). Tab Following/Group vẫn hiện nhưng bấm vào yêu cầu đăng nhập. Mọi tương tác (upvote, report, bookmark, follow...) đều cần login — nhất quán QA-011 (permission matrix Guest, Phase 2: INTR=Không, Report=Không). Mặc định guest vào tab Trending |
| QA-228 | ISS-169: Tab Following rỗng (user chưa follow ai/gì) hiện gì? | Empty state + CTA dẫn sang trang Search (tìm theo User/Topic/Post) — Search đúng phạm vi 3 loại follow target (M07), trong khi Trending có cả sub Tag (không phải đối tượng follow được) nên dẫn sang đó sẽ lạc đề |
| QA-229 | ISS-187: Có nên thêm tab Group (feed tổng hợp từ group đã join) không? | Có — thêm tab thứ 4 "Group", tổng hợp bài từ mọi group (Public+Private) mà user đã join, hiển thị chronological (khác với việc vào từng group riêng lẻ đã có sẵn ở M11/DEC-111) |
| QA-230 | ISS-188: Tab Group hiện/ẩn theo điều kiện nào? | Luôn hiện cho user đã login (nhất quán cách xử lý Following, QA-228); Guest thấy tab nhưng gate giống Following (QA-227). Chưa join group nào → empty state + CTA "Khám phá Group" (dẫn sang trang danh sách/tìm Group) |
| QA-231 | ISS-172: Trending Post có cần filter theo Topic không? | Không — chỉ 1 danh sách global duy nhất. Đã có Trending Topic riêng (1 trong 3 sub) để xem theo chủ đề, filter thêm trong Trending Post sẽ dư thừa |
| QA-232 | ISS-173: Bài Group Public cross-post (DEC-111) có tính vào Newest/Trending Post không? | Ban đầu: Có, tính vào cả 2. **AMENDED ngay trong cùng phiên — xem QA-233**: loại khỏi Newest, vẫn giữ trong Trending Post |
| QA-233 | ISS-173 (amend QA-232): phạm vi chính xác? | Group Public cross-post vẫn tính vào Trending Post (và tất nhiên vào tab Group) nhưng **loại khỏi Newest** — lý do: Trending xếp hạng theo độ hot nên gộp mọi nguồn hợp lý, còn Newest là "dòng thời gian nội dung chung của site" nên giữ thuần không-thuộc-group |
| QA-234 | ISS-174: Cơ chế phân trang cho cả 4 tab? | Infinite scroll, cursor-based (theo post_id/created_at tùy tab), 20 bài/lần load — nhất quán pattern đã dùng cho Chat (QA-224). Note kỹ thuật: cần SSR cho batch đầu để đảm bảo SEO crawlability cho nội dung Guest xem được (Newest/Trending) — lý do Guest được xem post/comment từ đầu là vì SEO/discoverability (QA-011) **[Amended: phần SSR hoãn ở MS1 — xem QA-256/DEC-134, OPEN-006]** |
| QA-235 | ISS-175: Có ngưỡng tối thiểu (min upvote/comment) để vào Trending không? | Không đặt ngưỡng cho MS1 — dataset demo nhỏ (~70 bài, 30 user), đặt ngưỡng dễ khiến Trending trống/gần trống lúc demo. Provisional — có thể bổ sung ngưỡng sau khi dataset đủ lớn, cần revisit |
| QA-236 | ISS-176: Trending có loại bài của user BANNED/HEAVY warn không? | Không loại, không chỉnh score. Theo đúng precedent đã chốt ở DEC-118/DEC-122 (M12): ngoại lệ ẩn khỏi khu vực công khai CHỈ áp dụng riêng cho Leaderboard, còn lại (profile/post/comment, và nay thêm Trending) vẫn hiển thị bình thường. BANNED tự có label công khai "Tài khoản đã bị khóa" (QA-205) hiện cả trên Trending nếu bài lọt vào — đủ giải quyết vấn đề minh bạch mà không cần rule loại trừ riêng. HEAVY warn giữ private tuyệt đối (DEC-079), không hiện gì đặc biệt, nhất quán khắp nơi khác |
| QA-237 | ISS-177: Feed có tự cập nhật real-time khi có bài mới không? | Không auto-insert nội dung. Newest/Following/Group dùng banner "có bài mới" (polling định kỳ ~30-60s), bấm vào chỉ fetch phần mới rồi prepend lên đầu — giữ nguyên vị trí cuộn hiện tại, không reload toàn bộ. Trending không cần banner — tự refresh theo đúng chu kỳ tính lại decay (15-30 phút, DEC-052/124) |
| QA-238 | ISS-177 (bổ sung): banner reload có mất vị trí cuộn không? | Không — bấm banner chỉ fetch đúng phần bài mới (so với cursor cuối cùng) rồi chèn thêm vào đầu, không reload lại toàn bộ, không ép về đầu trang. Vị trí đang đọc ở dưới (nếu có) giữ nguyên |
| QA-239 | ISS-177 (amend): banner nên polling hay real-time (SSE)? | Giữ polling, không chuyển sang real-time cho MS1. Lý do: khác Chat (pub/sub theo đúng 1 chatId, biết chính xác ai cần nhận), Following/Group cần lọc cá nhân hóa theo từng connection (follow/membership của từng user) mới biết có nên đẩy tín hiệu không — phức tạp hơn hẳn broadcast đơn thuần, chưa đáng effort cho module Could-priority ở MS1 |
| QA-240 | ISS-186: M14 có còn phụ thuộc M13 (AI Layer) không? | Bỏ dependency M13 khỏi M14 cho scope hiện tại — chỉ còn phụ thuộc M03 (Post), M05 (Topic/Tag). Lý do: dependency gốc đặt ra từ lúc còn tab "For You" cá nhân hóa AI, nay đã bỏ (xem QA-225). Không bỏ vĩnh viễn — có thể tái thêm M13 nếu mở rộng tính năng cá nhân hóa AI sau MS1 |

## Phase 5 — M15: Analytics & Stats (QA-241 → QA-247)

| ID | Question | Answer |
|----|----------|--------|
| QA-241 | ISS-178: M15 Analytics & Stats — ai truy cập được, ADMIN-only hay có mở cho MOD? | Chỉ ADMIN truy cập được cả 3 dashboard. Đã cân nhắc phương án mở thêm cho MOD xem Moderation Stats (lọc riêng theo hoạt động của MOD đó) kèm ý tưởng bổ sung bảng xếp hạng Top-N MOD xử lý nhiều report nhất — nhưng việc lọc số liệu cá nhân hóa theo từng MOD làm tăng độ phức tạp đáng kể so với query tổng toàn hệ thống, trong khi đây là module Could-priority. Quyết định cuối: giữ đơn giản, chỉ ADMIN xem, bỏ hẳn ý tưởng Top-N MOD |
| QA-242 | ISS-179: User Stats dashboard gồm những chỉ số nào? | Tổng user theo trạng thái tài khoản (ACTIVE/DEACTIVATED/BANNED) · trend đăng ký mới theo thời gian (biểu đồ) · phân bố theo vai trò (USER/MOD/ADMIN) · phân bố theo Lớp/Khối (grade_level, F-POST-09) · phân bố theo mức warn (Clean/LIGHT/MEDIUM/HEAVY/BANNED). Tất cả derive từ dữ liệu sẵn có (bảng user + warn level), không cần tracking infra mới như DAU/WAU/MAU (yêu cầu activity-log riêng — bị loại vì tốn thêm effort không cần thiết cho MS1, trong khi tổng user theo mốc thời gian đã đủ thông tin cho mục đích demo/báo cáo) |
| QA-243 | ISS-180: Content Stats dashboard gồm những chỉ số nào? | Tổng Post theo publish_state · breakdown theo mod_state (pending/active/under_review/removed) · trend bài đăng mới theo thời gian · phân bố Post theo Topic · trend Comment mới theo thời gian. Đã cân nhắc thêm tỉ lệ Group-post/độc lập và tỉ lệ bài ẩn danh nhưng loại bỏ — không cần thiết, thêm nhiễu cho dashboard mà không phục vụ mục đích vận hành rõ ràng |
| QA-244 | ISS-181: Moderation Stats dashboard gồm những chỉ số nào? | Tổng Report theo trạng thái (pending/resolved/dismissed...) + theo category (5 category + Khác, ISS-050) · Warn issued theo level theo thời gian · Ban/Unban theo thời gian · Appeal theo loại + outcome. Chọn phương án "thêm được nhiều thì càng tốt" (mọi chỉ số đều derive free từ dữ liệu Report/Warn/Ban/Appeal đã có ở M08/M09) thay vì phương án tối giản chỉ đếm tổng Report |
| QA-245 | ISS-182: Filter thời gian cho cả 3 dashboard — custom range hay preset? | Preset cố định: Hôm nay / 7 ngày / 30 ngày / Toàn thời gian (all-time). Không có custom date range picker cho MS1 — đơn giản hóa UI và truy vấn |
| QA-246 | ISS-183: Cách tính toán — real-time query hay batch/cache? | Real-time — query trực tiếp mỗi lần admin load dashboard (COUNT/GROUP BY đơn giản theo preset thời gian), không cache/batch. Khác Leaderboard (M12, cần batch vì ranking + tie-break phức tạp, DEC-123), lượng truy cập admin vào Analytics thấp hơn nhiều so với traffic user thông thường nên real-time query không tạo áp lực đáng kể lên hệ thống |
| QA-247 | ISS-184: Có export dữ liệu (CSV) không? | Không làm cho MS1. Đánh dấu **OPEN-004** (để ngỏ xem xét lại sau khi các module core hoàn thiện), theo đúng pattern đã dùng cho OPEN-003 — đây là quyết định defer có chủ đích, không phải unknown bỏ sót |

## Phase 6 — Cross-cutting Concerns (QA-248 → QA-255)

| ID | Question | Answer |
|----|----------|--------|
| QA-248 | ISS-189: Timezone & date handling — lưu trữ/tính toán theo múi giờ nào? | Lưu timestamp dạng UTC trong DB (chuẩn phổ biến). Mọi tính toán ranh giới ngày/tuần (reset leaderboard weekly M12, deadline appeal 30 ngày M09, probation warn 5/10/15 ngày M08, preset Hôm nay/7 ngày/30 ngày M15, soft-delete window 7 ngày M03...) và hiển thị trên UI đều quy về **Asia/Ho_Chi_Minh (UTC+7)** — cố định, không có DST vì Việt Nam không đổi giờ mùa hè. Lý do chọn: 100% target user là học sinh VN, không cần multi-timezone, và việc cố định offset +7 không phát sinh edge case kỹ thuật nào |
| QA-249 | ISS-190: i18n/localisation — site có cần hỗ trợ ngôn ngữ nào ngoài tiếng Việt không? | Vietnamese-only ở MS1 (không có language switcher), nhưng tổ chức theo kiến trúc i18n-ready — string UI externalize qua i18n key (thư viện kiểu i18next), chỉ có 1 locale `vi` active. Lý do: dễ mở rộng sau mà không cần refactor lại toàn bộ UI string. Lưu ý quan trọng: i18n UI chỉ dịch được phần "chrome" (nhãn, nút, thông báo hệ thống) — KHÔNG dịch được nội dung do user tạo ra (post/comment vẫn mãi ở ngôn ngữ writer viết). Việc hỗ trợ nội dung đa ngôn ngữ (dịch/tag content theo ngôn ngữ) là 1 tính năng hoàn toàn khác, ngoài scope draft gốc — ghi nhận là ý tưởng mở, không build ở MS1 |
| QA-250 | ISS-191: Data retention tổng quát — audit log và chat message có cần policy xóa/lưu trữ gì không? | Giữ vĩnh viễn, không hard-delete/archive — nhất quán với Notification (DEC-071: "no retention policy"). Research xác nhận: log/audit data thường không bị xóa trong thực tế (vì mục đích compliance/minh bạch/trace), khác bản chất với content user có thể chủ động xóa. Thêm lý do kỹ thuật: nhiều bảng khác tham chiếu tới audit log/message (FK — report trỏ message_id, warn trỏ report...), hard-delete dễ phá referential integrity. Nguyên tắc tổng quát rút ra áp dụng cho mọi quyết định hard-delete từ đây về sau: **chỉ hard-delete khi thật sự an toàn** (có lý do rõ ràng — privacy/PII cần xóa, hoặc dọn rác content do chính user chủ động xóa có UX hợp lý — VÀ không phá referential integrity với bảng khác tham chiếu). Các quyết định hard-delete đã chốt trước đó (Post 7 ngày DEC-011, Comment permanent DEC-038, Account PII wipe DEC-019) đều thỏa nguyên tắc này nên không đổi gì |
| QA-251 | ISS-192: File/media upload — có cần cơ chế scan virus/malware không? | Không — chỉ giữ whitelist type/size đã có (ảnh JPEG/PNG/WebP, giới hạn size theo từng feature: avatar 5MB, report evidence 5MB/file). Dựa vào CDN (Cloudinary) tự re-encode/transcode ảnh khi upload — quá trình này tự nhiên loại bỏ payload độc hại ẩn trong file ảnh, đủ an toàn cho scope chỉ-cho-upload-ảnh (không file thực thi) ở MS1 |
| QA-252 | ISS-193: AI — nội dung user gửi ra OpenAI (3rd party) có cần xử lý gì về privacy không? | Có — thêm 1 trang Privacy Policy/ToS công khai, nêu rõ nội dung đăng công khai (post/comment) được xử lý bởi dịch vụ AI bên thứ 3 (OpenAI Moderation API + Embedding) cho mục đích kiểm duyệt và tìm kiếm ngữ nghĩa. Link hiện ở footer và/hoặc registration flow. Lý do: chi phí gần như bằng 0 (chỉ 1 trang nội dung tĩnh) nhưng tăng minh bạch đáng kể, đặc biệt quan trọng vì đối tượng user là học sinh (có thể vị thành niên) |
| QA-253 | ISS-194: AI — Topic Suggestion (GPT-4o-mini) trả về ngoài danh sách 11 topic hợp lệ thì xử lý sao? | Validate output theo whitelist 11 topic cố định của hệ thống; nếu AI trả về topic không khớp → coi như suggestion fail, hiển thị non-blocking error ("Không thể gợi ý chủ đề lúc này, vui lòng chọn thủ công") và để user tự chọn thủ công. Dùng CHUNG đúng 1 UX pattern với case AI transient-failure đã chốt ở DEC-099 (timeout/retry hết hạn) — dù nguyên nhân kỹ thuật khác nhau (timeout vs hallucination), người dùng không cần phân biệt, trải nghiệm giống hệt nhau |
| QA-254 | ISS-195: AI — có cần lưu log raw output (score Moderation, Topic suggestion) để audit/debug không? | Có — mỗi lần gọi AI (Moderation API, Embedding, Topic Suggestion) lưu raw response vào bảng `ai_decision_log` riêng, gắn với post/comment liên quan (khác với audit log hành động admin/mod đã có ở DEC-081/094 — đây là log quyết định do chính AI đưa ra). Phục vụ 2 mục đích: (1) debug/tinh chỉnh threshold 0.9/0.5 hiện là placeholder (DEC-098) bằng dữ liệu thật thay vì đoán, (2) làm cơ sở xử lý Content Deletion Appeal (M09/DEC-115) khi user khiếu nại bị AI xử oan — mod/admin cần xem lại được "tại sao AI quyết định vậy" |
| QA-255 | ISS-196: Analytics events — có cần hạ tầng event-tracking chung (ngoài 3 dashboard M15) không? | Không xây cho MS1 — formalize lại quyết định đã ngầm chọn lúc deep-dive M15 (QA-242: từ chối DAU/WAU/MAU vì cần activity-log/event-tracking riêng), áp dụng thành nguyên tắc chung cho toàn hệ thống thay vì chỉ riêng M15, tránh việc module khác sau này tự ý thêm event-tracking rải rác không nhất quán. Đánh dấu **OPEN-005** — để ngỏ xem xét lại sau khi các module core hoàn thiện, theo đúng pattern của OPEN-003/OPEN-004 (quyết định defer có chủ đích, không phải unknown bỏ sót) |

## Phase 7 prep — Tech Stack (OPEN-002)

| ID | Question | Answer |
|----|----------|--------|
| QA-256 | ISS-197: Tech stack — Backend/Frontend framework, và có cần SSR/SEO ở MS1 không? | Backend: Java + Spring Boot. Frontend: ReactJS. Stakeholder làm rõ: "chỉ cần đảm bảo core, MS1 chưa cần SEO, SSR gì cả". Đã giải thích: SSR (server dựng sẵn HTML, khác SSE = server đẩy realtime); Next.js là React framework có SSR sẵn nhưng team chưa dùng; React thuần + thư viện không có SSR sẵn. Kết luận: React + Vite chạy phía trình duyệt, không SSR ở MS1; SEO/SSR ghi thành OPEN-006 (xem lại trước deploy thật). Hệ quả đã nêu: Google index kém tin cậy hơn, preview khi dán link vào Zalo/Facebook không có. Để dễ chuyển Next.js về sau: tách lớp gọi API, giữ component thiên về hiển thị (hướng làm, không cam kết chi phí). UI Kit dùng chung cho toàn app, làm sau khi có design: stakeholder xác nhận chỉ dùng trong application (nội bộ, không phải sản phẩm nộp riêng, không thêm module/scope); phải tuân thủ i18n key (DEC-128) và timezone hiển thị (DEC-127). Yêu cầu cốt lõi: có một bộ common UI thống nhất dùng trong app; được phép xây trên thư viện nền có sẵn (stakeholder: tự viết hay dùng nền đều được, quan trọng là có bộ common UI). Chọn thư viện nền: chắc chắn đợi có design; hiện stakeholder nghiêng về MUI (xu hướng, chưa chốt) → ghi **OPEN-007**. |
| QA-257 | ISS-198: Kênh realtime — thống nhất SSE hay giữ WebSocket cho thông báo? | Stakeholder nghiêng về SSE và hỏi app có cần giao tiếp hai chiều không. Đã rà register: chat = POST gửi + SSE nhận (đã xem cũng qua POST + SSE, QA-212); thông báo chỉ server→client; feed banner = polling (QA-239); AI = request/response; leaderboard = cron (QA-203); không có typing indicator/presence/collab. Stakeholder đề xuất online/offline bằng FE ping định kỳ (heartbeat) rồi quyết định bỏ qua — không đưa vào yêu cầu. Kết luận: dùng SSE cho cả chat và thông báo, bỏ WebSocket; QA-131 và các ghi chú WebSocket liên quan được amend. Lưu ý: pub/sub in-memory (không Redis) chỉ chạy 1 instance — đã chấp nhận ở scale demo (ghi lại ở Phase 7). |
| QA-258 | ISS-199: Email — thư viện và nguồn SMTP gửi mail? | Stakeholder đề xuất Spring Mail. Đã giải thích SMTP (giao thức gửi mail; app giao thư cho máy chủ SMTP) và tách 2 lớp: code gửi (Spring Mail) vs nguồn SMTP phía sau (chỉ là host/port/user/password trong config). Chọn phương án A: Spring Mail + SMTP của nhà cung cấp có gói miễn phí; nhà cụ thể chọn khi triển khai, không ảnh hưởng spec. Gmail SMTP chỉ dùng ở dev. Xác thực tên miền gửi (SPF/DKIM) cần khi chạy thật, chưa cần cho demo 20–30 người. |
| QA-259 | ISS-200: Cờ `AI_ENABLED` lưu ở đâu? | Assistant đưa phương án A (env var) / B (DB + admin UI) / C — nhưng stakeholder chỉ ra đã chốt từ đầu có màn hình admin cấu hình các mục này. Kiểm tra lại: đúng — DEC-092 (System config list: AI toggle, maintenance, registration, feature flags, banner) và DEC-093 (AI master + per-module) đã chốt trong M10. Phân biệt: QA-161 chỉ nói *hằng số chính sách* (ngưỡng, thời hạn) không chỉnh được qua UI, khác với *system config toggle*. Kết luận: không có quyết định mới, cờ AI nằm trong Admin Panel (lưu bền trong DB). |
| QA-260 | ISS-201: Hosting / deployment ở MS1? | Stakeholder xác nhận: "ở MS1 ta chưa cần deploy gì cả". Nhất quán QA-002 (DoD: dev complete + demo-ready, deploy không bắt buộc). Hosting = N/A ở MS1; nhà cung cấp và cách đóng gói (Docker chỉ là ý tưởng, chưa chốt) để khi cần deploy thật. Không có quyết định mới. |
| QA-261 | ISS-202 (đóng ISS-029): Có ràng buộc học thuật nào về công nghệ không? | Stakeholder: không có yêu cầu gì, tự do khi implement code. Bổ sung: đồ án rất nặng về "design system" (hiểu là thiết kế hệ thống — chưa xác nhận, không phải UI Kit) — từ thiết kế DB, models tới luồng đi qua từng class, phản hồi như thế nào..., nặng nghiệp vụ nên phần đó cần làm cực kỳ kỹ. Cập nhật QA-010: không có ràng buộc công nghệ; kỳ vọng chiều sâu thiết kế/nghiệp vụ cao. Không có quyết định mới về công nghệ. |
| QA-262 | Phase 8 (Data model) — cách tiếp cận và độ sâu? | Stakeholder chọn đi từng module (không gộp một lượt), sau đó tổng hợp thành hệ thống. Quy trình: (1) trích xuất danh từ → đối tượng (entity) và thuộc tính cho từng module; (2) tổng hợp thành sơ đồ thực thể (ERD) toàn hệ thống; (3) tiếp theo là thiết kế database (giai đoạn thiết kế, sau BA), rồi các bước sau. Lý do: đồ án nặng về thiết kế hệ thống/nghiệp vụ nên cần kỹ (QA-261). Áp dụng khi vào Phase 8. |
| QA-263 | ISS-203: Xác nhận nhóm công nghệ ngầm định? | Stakeholder: "xác nhận tất, và sau này có cần thêm gì ta sẽ bàn sau". Xác nhận PostgreSQL + pgvector, Cloudinary, OpenAI (Moderation / text-embedding-3-small / GPT-4o-mini), Tiptap/ProseMirror (JSON), JWT. Đóng OPEN-002. |

## System Requirement prep — Privacy & Consent

| ID | Question | Answer |
|----|----------|--------|
| QA-264 | ISS-204: Có yêu cầu đồng ý Privacy Policy/ToS khi đăng ký không, và privacy xây dựng thế nào? | Stakeholder: "yêu cầu đồng ý chắc chắn phải có mới register được"; "ta sẽ xây dựng privacy sau nhưng chắc chắn phải có privacy". Assistant nêu các chỗ chưa có trong register: danh mục dữ liệu cá nhân, quyền của người dùng (xem/tải/xóa dữ liệu), xử lý học sinh dưới 18 tuổi, cơ sở pháp lý, và câu hỏi DEC-129 (giữ chat và log vĩnh viễn) so với việc xóa sạch PII khi xóa tài khoản. Tất cả để sau, ghi OPEN-008. |

## System Requirement prep — Documentation approach

| ID | Question | Answer |
|----|----------|--------|
| QA-265 | ISS-205: Cách viết tài liệu SR theo module? | Stakeholder cung cấp tài liệu mẫu (cấu trúc mục 1–6, mỗi chức năng gồm yêu cầu cấp trên / lý do / yêu cầu cấp dưới) và chốt: mỗi module một tài liệu, tự chứa thuật ngữ và quyền; tiếng Việt (giữ tiếng Anh cho thuật ngữ bắt buộc); văn phong chuyên nghiệp dễ hiểu; viết SR ngay ở phase này, Phase 7/8 làm sau; một hành vi chỉ ở một module sở hữu, module khác tham chiếu bằng ID (điểm 4A); Nguồn/Basis ở phụ lục truy vết, thân tài liệu sạch (điểm 6B); milestone/ưu tiên ghi một lần ở mục 5.1, chỉ gắn nhãn ngoại lệ, bỏ bảng áp dụng kiểu automotive (điểm 10B); mục 4.1 chỉ ghi luật/tiêu chuẩn do stakeholder nêu, nếu không có thì 'Không có'; phần đầu có mã tài liệu, dự án, module, trạng thái, phiên bản, ngày, tác giả Phạm Văn Đức, bỏ mục người duyệt; lưu ở .agents/.claude/system_analysis/output/specs/ (báo cáo audit ở specs/audit/); hai agent Author (viết) và Auditor (chỉ kiểm tra, không sửa; kiểm độ bao quát bằng ma trận nguồn–yêu cầu và checklist quy tắc), Author sửa theo báo cáo, tối đa 2 vòng rồi đưa stakeholder quyết; mọi GAP/mơ hồ/đề xuất raise cho stakeholder từng việc; câu trả lời ghi vào register (QA/DEC) và Author phải sửa/bổ sung vào SR; chạy thử một module trước (đề xuất M05); HMI Requirements và Screen Transitions để placeholder đến khi có design. Ghi nhận: quyết định này khác hai quy tắc trong BA-INTERVIEW-RULES (output tiếng Anh; chỉ sinh spec sau Phase 9). |
| QA-266 | ISS-206: Quy ước ID cho tài liệu SR? | Stakeholder chốt tạm: tiền tố dự án `ISH`; tài liệu `ISH-SR-Mxx`; yêu cầu cấp trên `ISH-Mxx-nnn`, cấp dưới `ISH-Mxx-nnn.k`; điểm mở `OP-Mxx-nn` (tạm thời, chỉ ở Phụ lục B); phát hiện audit `AUD-Mxx-nn`; mục nguồn dùng lại ID ISS/QA/DEC/OPEN; ID vĩnh viễn (không đánh số lại/dùng lại, cho phép khoảng trống); số mục 5.x không phải ID. Kèm yêu cầu: xây skill Author và sửa các file trong .agent-instructions liên quan, sau đó stakeholder review |
