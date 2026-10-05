# Knowledge Sharing Platform – Project Modules (Updated — Full Scope Committed)

> Toàn bộ module dưới đây đã được XÁC NHẬN đưa vào phạm vi chính thức của dự án — không còn khái niệm "làm nếu còn thời gian". Xem thứ tự triển khai (không phải mức độ ưu tiên có thể cắt) tại `iShare_dev_priority.md`.

## 1. User Module

### 1.1 Account

- Register
- Login / Logout
- Forgot password
- Change password
- Email verification

### 1.2 Profile

- Avatar
- Username
- Bio
- Lớp/Khối (10/11/12) — tùy chọn, dùng để lọc nội dung và cá nhân hóa feed
- Joined date
- User posts
- Stars received
- Stars given
- Reputation
- Badges
- Followers / Following

### 1.3 Role & Permission

- `USER`
- `MODERATOR`
- `ADMIN`

Permissions:

- Create / edit / delete post
- Create / edit / delete comment
- Report content
- Review reports
- Moderate content
- Manage users
- Manage badges

> Không có loại tài khoản Giáo viên/Học sinh riêng biệt — đã cân nhắc (ưu tiên hiển thị, leaderboard/badge riêng) nhưng quyết định không triển khai, ngoài phạm vi dự án. Chi tiết lý do tại `iShare_specs_general.md`.

---

## 2. Post / Forum Module

### 2.1 Post

Post là đơn vị nội dung trung tâm của hệ thống.

Các dạng nội dung có thể được thể hiện bằng cùng một Post:

- Knowledge sharing
- Tutorial / guide
- Experience
- Discussion
- Review
- Resource / document
- News / information

Thông tin chính:

- Title
- Content
- Author
- Cover image
- Tags
- Topic / Category (nếu sử dụng)
- Lớp/Khối (10/11/12) — tùy chọn
- `is_anonymous` — ẩn danh tác giả với người xem khác; hệ thống vẫn lưu identity thật để Moderator xử lý report
- `accepted_comment_id` — câu trả lời tốt nhất, do chính tác giả Post chọn (xem 4.2.1)
- View count
- Star count
- Comment count
- Created time
- Updated time
- Status

Post status:

- `DRAFT`
- `PENDING_REVIEW`
- `PUBLISHED`
- `HIDDEN`
- `LOCKED`
- `DELETED`

### 2.2 Rich Content

- Markdown / rich text
- Code block
- Image
- Link
- Quote
- Table
- File attachment

### 2.3 Post Edit History

- Version history
- Editor
- Updated time
- Change history

### 2.4 Post Type – Optional

Không cần thêm Post Type ngay từ đầu.

Chỉ nên có khi từng loại Post dẫn tới behavior hoặc workflow khác nhau, ví dụ:

- Review có rating riêng
- Resource có file/external link riêng
- Tutorial có cấu trúc riêng
- News có metadata riêng

Nếu các loại chỉ khác nhau về cách hiển thị, **Tag/Topic là đủ**.

---

## 3. Topic / Tag / Lớp-Khối Module

### 3.1 Topic / Category

Dùng để tổ chức các lĩnh vực tri thức lớn, phù hợp đối tượng học sinh THPT.

> Danh sách topic cụ thể **chưa cố định** — sẽ được xác định và hoàn thiện trong giai đoạn phân tích yêu cầu (BA), không giới hạn cứng theo môn học trong chương trình. Ví dụ gợi ý ban đầu: Toán học, Văn học, Khoa học tự nhiên, Khoa học xã hội, Công nghệ thông tin, Kinh tế, Giáo dục, Tâm lý học đường, Lịch sử, Địa lý, Triết học, Ngoại ngữ, Nghệ thuật, Kỹ năng sống, Môi trường, Nghề nghiệp/Định hướng nghề nghiệp.

### 3.2 Tag

Một Post có thể có nhiều Tag, không giới hạn số lượng.

```text
Post:
Ứng dụng xác suất Bayes trong Machine Learning

Topic:
Toán học

Lớp/Khối:
12

Tags:
#XácSuất
#ThốngKê
#Bayes
#MachineLearning
```

### 3.3 Lớp / Khối

Trục phân loại bổ sung, song song với Topic:

- **Topic** = lĩnh vực/chủ đề nội dung
- **Lớp/Khối** = cấp học (10/11/12) — cùng một Topic nhưng nội dung Lớp 10 và Lớp 12 có thể khác hẳn nhau
- **Tag** = từ khóa tự do, chi tiết hơn Topic

Gắn cả trên Post và trên Profile người dùng (tùy chọn), dùng để lọc nội dung và làm tiêu chí ưu tiên trong Personalized Feed (xem 7.1).

### 3.4 Quan hệ

```text
Post
 ├── Topic / Category
 ├── Lớp / Khối (tùy chọn)
 └── N Tags
```

---

## 4. Interaction Module

### 4.1 Post Star

User có thể:

- Star post
- Unstar post

Theo dõi:

- Stars received
- Stars given

Post Star là một signal chính để đánh giá mức độ hữu ích của nội dung.

### 4.2 Comment / Reply

- Comment
- Reply
- Edit
- Delete
- Mention
- Report

#### 4.2.1 Accepted Answer

Với bài loại câu hỏi, **chỉ tác giả của Post** được đánh dấu một comment là câu trả lời tốt nhất (giống mô hình Stack Overflow):

```text
Comment
      ↓
Tác giả Post bấm "Accept"
      ↓
Post.accepted_comment_id = comment.id
      ↓
Cộng thêm reputation riêng cho người trả lời được chọn
```

- AI và Moderator **không** tự động chọn hoặc thay tác giả chọn Accepted Answer.
- Moderator chỉ có quyền **gỡ** đánh dấu nếu phát hiện gian lận (vd. tự accept câu trả lời rác để đẩy điểm) — xem 10.2.

### 4.3 Comment Star

Nên có và **phân biệt với Post Star**.

```text
Post Star
→ đánh giá mức độ hữu ích của toàn bộ bài viết

Comment Star
→ đánh giá mức độ hữu ích của một phản hồi
```

Nên lưu riêng:

- `PostStar`
- `CommentStar`

Có thể dùng cả hai cho Reputation nhưng nên áp trọng số khác nhau để hạn chế việc spam comment để tăng điểm.

### 4.4 Bookmark

Ý nghĩa:

> Lưu bài để đọc / tham khảo lại.

MVP:

- Bookmark
- Unbookmark
- My Bookmarks

### 4.5 Follow / Quan tâm

Ý nghĩa:

> Muốn nhận cập nhật về nội dung hoặc chủ đề.

Có thể Follow:

- Post
- User
- Topic
- Tag
- Group (xem Module 5)

Follow có thể kích hoạt notification khi có hoạt động phù hợp.

---

## 5. Group Module

Không gian nhóm dạng cộng đồng, tương tự group Facebook. Tái dùng gần như toàn bộ cơ chế của Forum, không xây lại từ đầu.

### 5.1 Group

- Tên, mô tả nhóm
- `public` hoặc `private` (private cần được duyệt khi tham gia)
- Người tạo / owner

### 5.2 GroupMember

- Thành viên nhóm, vai trò trong nhóm (owner/member)
- Join tự do (nhóm public) hoặc cần duyệt/mời (nhóm private)

### 5.3 Đăng nội dung trong Group

- Post trong Group dùng field `group_id` (tùy chọn) trên Post hiện có — **không tạo bảng Post riêng cho Group**
- Toàn bộ Comment, Star, Report, Moderation, AI Moderation, Notification dùng chung cơ chế của Forum, chỉ lọc thêm theo quyền xem nếu Group ở chế độ private

### 5.4 Quan hệ

```text
Group
 ├── N GroupMember
 └── N Post (qua field group_id)
```

> Cố tình không xây leaderboard hay công thức reputation riêng theo từng Group, để tránh phình phạm vi không cần thiết.

---

## 6. Nhắn tin Module

Chat 1-1 và group chat, **chỉ dạng văn bản** — không hỗ trợ gọi thoại, gọi video hay gửi file trong phạm vi đồ án.

### 6.1 Conversation

- 1-1: giữa 2 user
- Group chat: nhiều thành viên

### 6.2 Message

- Nội dung dạng văn bản
- Thời gian gửi, trạng thái đã đọc/chưa đọc

### 6.3 Report tin nhắn

Tái dùng cơ chế Report chung (Module 10), thêm giá trị `target_type = MESSAGE` — không xây luồng report riêng cho chat.

### 6.4 Ghi chú kiến trúc

Module Nhắn tin dùng kênh **real-time riêng bằng WebSocket**, khác bản chất request–response REST của các module còn lại. Đây là điểm cần lưu ý khi phân công và thiết kế kiến trúc (xem `iShare_specs_general.md`, mục 7).

---

## 7. Discovery / Search Module

### 7.1 Feed

Các feed chính:

- Latest
- Popular
- Trending
- Following
- **Personalized** — ưu tiên hiển thị bài đúng Lớp/Khối của user và đúng Topic/Group đang theo dõi. Không cần AI; đây là tiêu chí cụ thể thay cho cách hiểu mơ hồ trước đây.

### 7.2 Trending / Popular

Có thể dựa trên:

- Views
- Stars
- Comments
- Bookmarks
- Recency

### 7.3 Search

Tìm theo:

- Title
- Content
- Author
- Topic
- Tag
- Lớp/Khối
- Ngữ nghĩa (Semantic Search — xem 11.3, bắt buộc)

### 7.4 Filter / Sort

- Newest
- Oldest
- Most starred
- Most viewed
- Most commented
- Topic
- Tag
- Lớp/Khối
- Author

---

## 8. Notification Module

### 8.1 Notification Event

- Post nhận star
- Comment mới trên post
- Reply vào comment
- Mention
- Comment được đánh dấu Accepted Answer
- User mới follow
- Post mới từ user đang follow
- Nội dung mới trong topic/tag/group đang follow
- Nhận badge
- Tin nhắn mới
- Report được xử lý
- Post hoàn tất moderation

### 8.2 Notification Management

- Read / unread
- Mark as read
- Mark all as read

---

## 9. Reward / Reputation / Statistics Module

### 9.1 Reputation

Nguồn reputation có thể gồm:

- Post Star received
- Comment Star received
- Accepted Answer received
- Contribution milestones
- Community contribution

Nên thiết kế thành rule/configuration.

### 9.2 Badge / Achievement

Các nhóm chính:

- Contribution
- Engagement
- Milestone
- Community

Ví dụ:

- First Post
- Knowledge Sharer
- Helpful Contributor
- Popular Contributor
- Active Member
- Community Helper

### 9.3 User Statistics

Mỗi user có thể có:

- Total posts
- Total comments
- Post stars received
- Comment stars received
- Stars given
- Accepted answers received
- Views
- Followers
- Following
- Reputation
- Badges

### 9.4 User Leaderboard

**Leaderboard là chức năng chính của Reward/Statistics module.**

Các bảng xếp hạng:

- Weekly
- Monthly
- Yearly
- All Time

Có thể xây leaderboard theo:

- Reputation
- Stars received
- Contribution score

Có thể hiển thị:

- Rank
- User
- Score
- Reputation
- Stars received
- Contribution statistics

> Không xây leaderboard riêng nào khác ngoài 4 chu kỳ trên (không có leaderboard riêng theo Group, theo loại tài khoản, v.v. — xem lý do tại `iShare_specs_general.md`).

### 9.5 System Statistics

Admin có thể xem:

- Total users
- Active users
- Total posts
- Posts per day
- Comments per day
- Stars per day
- Popular topics
- Popular tags
- Reports
- Moderation statistics

---

## 10. Moderation / Administration Module

### 10.1 Report

Có thể report:

- Post
- Comment
- User
- Message (tin nhắn — xem Module 6.3)

Report reason:

- Spam
- Harassment
- Inappropriate
- Off-topic
- Copyright
- Misinformation
- Other

Report status:

- `OPEN`
- `IN_REVIEW`
- `RESOLVED`
- `REJECTED`

### 10.2 Content Moderation

Moderator/Admin có thể:

- Hide post
- Lock post
- Delete post
- Hide comment
- Delete comment
- Gỡ đánh dấu Accepted Answer sai (xem 4.2.1)
- Warn user
- Suspend account
- Ban account

### 10.3 User Management

Admin có thể:

- View user
- Change role
- Disable account
- Suspend account
- Ban account

### 10.4 Audit Log

Lưu:

- Actor
- Action
- Target
- Reason
- Timestamp

---

## 11. AI Assistance Module (toàn bộ bắt buộc)

> AI chỉ là lớp hỗ trợ. Không yêu cầu xây model, fine-tune hoặc tự phát triển thuật toán AI. **Nguyên tắc xuyên suốt: AI không tự quyết định tuyệt đối với case nhạy cảm, không tự chọn Accepted Answer, không tự cộng/trừ reputation.** Cả 5 năng lực dưới đây (11.1–11.5) đều đã được xác nhận là **bắt buộc triển khai**, không còn phân biệt optional/nice-to-have như bản nháp ban đầu.

### 11.1 AI Content Moderation

Mục tiêu:

- Phát hiện spam
- Toxic / abusive content
- Inappropriate content
- Advertising
- Một số loại vi phạm quy định

Flow:

```text
Post / Comment
      ↓
AI Moderation API
      ↓
Prediction + Confidence
      ↓
Rule / Moderation Policy
      ↓
Publish / Review / Reject
```

AI không nên là quyết định duy nhất đối với trường hợp nhạy cảm.

### 11.2 AI Content Classification

AI đề xuất:

- Topic / Category
- Tags

Flow:

```text
Post
 ↓
Classification API
 ↓
Topic + Tags
 ↓
User / Moderator review
```

Có thể cho user chỉnh kết quả trước khi publish.

### 11.3 Semantic Search

```text
Query
 ↓
Embedding API
 ↓
Vector Search
 ↓
Relevant Posts
```

Dùng PostgreSQL + pgvector.

### 11.4 Summarization

Bao gồm cả tóm tắt bài viết dài (Post Summarization) và tóm tắt thảo luận dài (Comment-thread Summarization).

```text
Long Post / Long Comment Thread
 ↓
Summarization API
 ↓
Short Summary / Key Points
```

Không cần tóm tắt mọi bài — chỉ áp dụng khi nội dung đủ dài hoặc user yêu cầu.

### 11.5 Feedback / Evaluation Loop

Flow:

```text
AI Prediction
      ↓
Moderator / Trusted User
      ↓
Correct / Incorrect
      ↓
Expected Result + Feedback
```

Dùng để đo và theo dõi theo thời gian:

- Accuracy
- Precision
- Recall
- F1-score
- False Positive
- False Negative

Kết quả dùng để tinh chỉnh ngưỡng/rule kiểm duyệt và phân loại theo thời gian — **không phải để tự train lại model**. Mục tiêu là đánh giá chất lượng AI API integration.

> **Related Posts** (gợi ý bài viết liên quan bằng embedding) KHÔNG nằm trong phạm vi chính thức — có thể tận dụng chung hạ tầng Semantic Search nếu thuận tiện, nhưng không tính là cam kết của dự án.

---

## 12. Phạm vi dự án (đã chốt)

### Trong phạm vi

```text
User
Post (Accepted Answer, Anonymous Post)
Comment
Star (Post Star, Comment Star)
Topic / Tag / Lớp-Khối
Group
Nhắn tin (chat 1-1, group chat, chỉ văn bản)
Feed (Latest, Popular, Trending, Following, Personalized)
Search / Filter / Sort
Bookmark
Follow
Notification
Report
Moderation
Reputation
Badge
Statistics
Leaderboard
Admin
Audit Log
AI Content Moderation
AI Content Classification
Semantic Search
Summarization (Post + Comment-thread)
AI Feedback / Evaluation Loop
```

### Ngoài phạm vi

```text
Chưng cất Q&A thành kho tri thức
Định tuyến câu hỏi chưa trả lời tới người dùng uy tín
Related Posts
Phân biệt tài khoản Giáo viên/Học sinh
Gọi thoại / gọi video / gửi file trong Nhắn tin
Liên kết thư viện số của trường
AI tự viết bài/comment
AI tự quyết định reputation / badge / Accepted Answer
Chatbot / RAG phức tạp / Multi-agent
Train / fine-tune model riêng
```

---

## 13. Kiến trúc tổng thể

```text
                         Frontend
                            │
                            ▼
                       Backend API
                            │
     ┌───────────┬──────────┼──────────┬───────────┐
     │           │          │          │           │
     ▼           ▼          ▼          ▼           ▼
   User        Forum       Group     Reward     Nhắn tin
                 │                                 │
        ┌────────┼────────┐                (kênh real-time
        │        │        │                  riêng, WebSocket)
       Post   Comment    Star
        │
   Topic/Tag/Lớp-Khối
        │
  Discovery/Search
        │
        ▼
   Moderation/Admin
        │
        ▼
      AI Layer
        │
 ┌──────┬──────┬──────┬──────┐
 │      │      │      │      │
Moderation Classification Embedding Summarization Feedback
 │      │      │      │      │
 └──────┴──────┴──────┴──────┘
        ▼
   AI Provider API
```

### Nguyên tắc kiến trúc

- Core Forum/Group không phụ thuộc cứng vào AI.
- AI được tách thành service/layer riêng.
- Provider AI có thể thay đổi.
- Có fallback khi AI API lỗi.
- Các tác vụ AI có latency cao (Classification, Summarization, Embedding) xử lý asynchronous.
- Nhắn tin dùng kiến trúc real-time (WebSocket) riêng biệt với phần REST còn lại — cần phân công rõ ai nắm phần này khi làm SA.
