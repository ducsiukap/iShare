# Priority Overview (Updated — Full Scope Committed)

## 1. Trạng thái phạm vi

Toàn bộ module/tính năng liệt kê trong tài liệu này đã được **XÁC NHẬN** đưa vào phạm vi chính thức của dự án. Không còn khái niệm "cắt nếu deadline gấp" như bản nháp ban đầu — nếu có tính năng nào cần cắt trong quá trình làm thực tế, sẽ cập nhật lại file này khi đó, không suy đoán trước.

Chi tiết đầy đủ từng module (fields, flow, quan hệ dữ liệu) nằm ở `iShare_modules.md`. File này chỉ tập trung vào **thứ tự triển khai**.

## 2. Priority Tags — nghĩa là thứ tự triển khai, không phải mức độ có thể cắt

- `[P0]` — Triển khai trước tiên, làm nền tảng cho các phần còn lại.
- `[P1]` — Triển khai sau khi các phần P0 đã ổn định.
- `[P2]` — Triển khai sau cùng, chủ yếu hoàn thiện trải nghiệm.

Đối với AI:

- `[AI-P0]` — Triển khai trước.
- `[AI-P1]` — Triển khai sau khi các AI-P0 đã ổn định.

> Không còn tag `AI-P2` (nice-to-have) — toàn bộ 5 năng lực AI trong dự án đã được xác nhận là bắt buộc (xem mục 3, Giai đoạn 1 và 2).

## 3. Toàn bộ phạm vi đã chốt, theo thứ tự triển khai

### Giai đoạn 1 — `[P0]`

#### User
- Register / Login / Logout, quên/đổi mật khẩu, xác thực email
- Profile cơ bản (kèm Lớp/Khối tùy chọn)
- Role / Permission (User / Moderator / Admin)
- Admin user management cơ bản

#### Forum
- Create / Edit / Delete / View Post
- Post status
- Rich content cơ bản
- Tag, Topic, Lớp/Khối
- Accepted Answer (chỉ tác giả câu hỏi được chọn)
- Anonymous Post (cho chủ đề nhạy cảm)

#### Comment
- Create / Edit / Delete Comment
- Reply cơ bản

#### Interaction
- Post Star / Unstar
- Stars received / given

#### Group
- Tạo / tham gia nhóm (public hoặc cần duyệt)
- Đăng bài / bình luận / star trong nhóm (dùng chung cơ chế Forum)

#### Nhắn tin
- Chat 1-1 và group chat, chỉ dạng văn bản
- Report tin nhắn vi phạm

#### Search
- Keyword Search
- Filter theo Topic / Tag / Lớp-Khối

#### Moderation
- Report Post / Comment / User / Message
- Moderator review
- Hide / Delete / Lock content
- Gỡ đánh dấu Accepted Answer sai
- Basic user warning / suspend / ban

#### Reward
- Reputation + rule cấu hình được (Post Star và Comment Star tách trọng số riêng)
- Basic badges
- User statistics
- Leaderboard: Weekly, Monthly, Yearly, All-time

#### AI
- `[AI-P0]` AI Content Moderation
- `[AI-P0]` AI Content Classification

### Giai đoạn 2 — `[P1]`

#### Interaction
- Comment Star / Unstar
- Mention
- Bookmark
- Follow (User / Post / Topic / Tag / Group)

#### Discovery
- Latest / Popular / Trending Feed
- Personalized Feed (ưu tiên theo Lớp/Khối và đang follow)

#### Notification
- In-app notification đầy đủ: star, comment/reply, mention, Accepted Answer, follow, badge, tin nhắn mới, report được xử lý

#### Administration
- Audit Log
- Admin statistics dashboard

#### AI
- `[AI-P1]` Semantic Search
- `[AI-P1]` Summarization (bài viết dài và thảo luận dài)
- `[AI-P1]` Feedback / Evaluation Loop (đo accuracy/precision/recall, tinh chỉnh ngưỡng theo thời gian)

### Giai đoạn 3 — `[P2]`

- Hoàn thiện UI/UX, tối ưu hiệu năng
- Mở rộng thêm badge / rule reputation nếu cần
- Polish trải nghiệm Nhắn tin, Group

## 4. Ngoài phạm vi (đã cân nhắc, quyết định không làm)

- Chưng cất Q&A thành kho tri thức riêng — ý tưởng đề xuất, chưa xác nhận.
- Định tuyến câu hỏi chưa trả lời tới người dùng uy tín — ý tưởng đề xuất, chưa xác nhận.
- Related Posts — có thể tận dụng chung hạ tầng Semantic Search nếu thuận tiện, nhưng không tính vào cam kết.
- Phân biệt tài khoản Giáo viên/Học sinh, ưu tiên hiển thị, leaderboard/badge riêng cho giáo viên.
- Gọi thoại, gọi video, gửi file trong Nhắn tin.
- Liên kết bài viết tới thư viện số của trường.
- AI tự viết bài/comment, AI tự quyết định reputation/badge/Accepted Answer, chatbot/RAG phức tạp, multi-agent, train/fine-tune model riêng.

## 5. Toàn bộ phạm vi tối thiểu để bảo vệ đồ án

Vì toàn bộ scope ở mục 3 đều đã chốt (không phải "tối thiểu"), phần bảo vệ đồ án dùng chính Giai đoạn 1 (`[P0]`) làm cột mốc demo đầu tiên nếu cần trình bày sớm — không phải một scope thu gọn riêng biệt. Concept xuyên suốt vẫn là:

```text
Create → Share → Interact → Evaluate → Reward → Moderate
```

áp dụng cho cả Forum lẫn Group, có thêm Nhắn tin làm kênh giao tiếp trực tiếp giữa các bước đó.
