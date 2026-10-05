# iShare — Tổng quan Dự án (General Specs)

> Tài liệu tham chiếu tổng quan, dùng xuyên suốt dự án — không phải bản tóm tắt để đăng ký đồ án. Khi có thay đổi phạm vi/quyết định thiết kế trong quá trình BA hoặc phát triển, cập nhật lại file này để nó luôn phản ánh đúng trạng thái hiện tại.

## 1. iShare là gì

Một nền tảng cộng đồng hỏi – đáp và chia sẻ tri thức dành cho học sinh THPT (mô hình gần với Stack Overflow/Quora), tích hợp thêm không gian nhóm, nhắn tin, và một lớp AI hỗ trợ. Điểm khác biệt cốt lõi so với "forum cho user comment và tương tác" thông thường: nội dung được **tích lũy, đánh giá và tái sử dụng lâu dài** qua cơ chế uy tín/xếp hạng/kiểm duyệt, thay vì trôi đi như bình luận.

**Bối cảnh:** đây là sản phẩm thật, nhóm phát triển cho khách hàng là một giáo viên THPT, có định hướng dùng lâu dài (không chỉ để bảo vệ đồ án tốt nghiệp — đồ án là một cột mốc của dự án, không phải mục tiêu cuối).

**Team:** 2 người — Phạm Văn Đức (BA chính), Nguyễn Đức Đạt (QA chính). Cả hai cùng làm SA; UI/UX kết hợp công cụ AI; Frontend/Backend chia theo module, mỗi người ôm trọn FE+BE của phần mình.

## 2. Người dùng

- Người dùng cuối duy nhất: **học sinh THPT**. Giáo viên là khách hàng đặt hàng, không phải người dùng trong hệ thống — hệ thống **không** có loại tài khoản Giáo viên/Học sinh riêng biệt (xem mục 8 — lý do).
- Ba cấp phân quyền: `USER`, `MODERATOR`, `ADMIN`.

## 3. Phạm vi nội dung

"Chia sẻ tri thức" **không** bó buộc theo môn học trong chương trình. Nội dung xoay quanh các **Topic** phù hợp với học sinh THPT (học tập, kỹ năng sống, định hướng nghề nghiệp, tâm lý học đường...) — danh sách Topic cụ thể **chưa cố định**, sẽ chốt trong giai đoạn BA.

Ba trục phân loại nội dung, dùng song song:

| Trục | Ý nghĩa |
|---|---|
| Topic | Lĩnh vực/chủ đề nội dung |
| Lớp/Khối (10/11/12) | Cấp học — cùng Topic nhưng khác cấp có thể khác hẳn nội dung |
| Tag | Từ khóa tự do, chi tiết hơn Topic |

## 4. Bản đồ module

Chi tiết đầy đủ từng module (fields, flow, quan hệ dữ liệu) nằm ở `iShare_modules.md`. Đây là danh sách tổng quan:

1. **User & Phân quyền** — tài khoản, hồ sơ, 3 cấp quyền
2. **Forum** — Post, Comment, Accepted Answer, Anonymous Post
3. **Topic / Tag / Lớp-Khối** — phân loại nội dung
4. **Interaction** — Post Star, Comment Star, Bookmark, Follow, Mention
5. **Group** — không gian nhóm dạng cộng đồng, tái dùng cơ chế Forum
6. **Nhắn tin** — chat 1-1 và group chat, chỉ văn bản
7. **Discovery / Search** — tìm kiếm, filter, các luồng feed
8. **Notification**
9. **Reward / Reputation / Statistics / Leaderboard**
10. **Report / Moderation / Admin**
11. **AI Assistance Layer** — xem chi tiết phạm vi ở mục 6 bên dưới

## 5. Nguyên tắc thiết kế cốt lõi

Các nguyên tắc này chi phối cách thiết kế chi tiết ở giai đoạn BA — giữ nhất quán, không đảo ngược tùy tiện:

- **Con người luôn quyết định cuối cùng, AI/hệ thống chỉ gợi ý hoặc hỗ trợ.** Áp dụng cho: Accepted Answer (chỉ tác giả câu hỏi được chọn, AI/Mod không tự chọn — Mod chỉ được gỡ nếu phát hiện gian lận), AI Moderation (đưa ra prediction + confidence, không tự quyết tuyệt đối với case nhạy cảm), Reputation (không có cơ chế nào tự động cộng/trừ ngoài rule đã cấu hình).
- **Post Star tách khỏi Comment Star**, trọng số tính reputation khác nhau — chặn spam comment để "cày điểm".
- **Không phân biệt tài khoản Giáo viên/Học sinh.** Đã cân nhắc (ưu tiên hiển thị câu trả lời giáo viên, leaderboard/badge riêng) nhưng quyết định không làm: số giáo viên thực tế quá ít để một leaderboard riêng có ý nghĩa, trong khi chi phí gần như nhân đôi hệ Reward — không tương xứng với team 2 người.
- **Group tái dùng gần như toàn bộ cơ chế Forum** (Post/Comment/Star/Report), chỉ thêm `Group`, `GroupMember`, field `group_id` tùy chọn trên Post. Không có leaderboard/reputation riêng theo Group.
- **Nhắn tin chỉ dạng văn bản** — không gọi thoại, gọi video, gửi file trong phạm vi hiện tại (đòi hỏi WebRTC/media server/object storage, không tương xứng năng lực team). Dùng kênh real-time riêng (WebSocket), kiến trúc khác hẳn phần REST còn lại. Report tin nhắn tái dùng cơ chế Report chung.
- **Lớp/Khối** là trục phân loại mới, gắn cả Post và Profile — nhờ đó Personalized Feed có tiêu chí cụ thể (ưu tiên đúng lớp/khối + đang theo dõi), không cần AI để làm việc này.
- **Anonymous Post**: học sinh có thể ẩn danh với chủ đề nhạy cảm; hệ thống vẫn lưu danh tính thật để Moderator xử lý report.

## 6. Phạm vi AI (bắt buộc triển khai)

Khác với bản nháp phạm vi AI ban đầu trong `iShare_dev_priority.md` (nơi chỉ AI Moderation là bắt buộc, còn lại là should-have/nice-to-have), quyết định hiện tại của dự án là: **toàn bộ 5 năng lực AI dưới đây đều là phần bắt buộc phải triển khai**, không phải "làm nếu còn thời gian":

1. **AI Content Moderation** — tự động kiểm duyệt nội dung công khai (spam, toxic, vi phạm quy định), trả về prediction + confidence.
2. **AI Content Classification** — gợi ý Topic/Tag khi đăng bài, người dùng/Mod review trước khi publish.
3. **Semantic Search** — tìm kiếm theo ngữ nghĩa bằng embedding (có thể dùng PostgreSQL + pgvector).
4. **Summarization** — tóm tắt bài viết dài hoặc thảo luận (comment thread) dài.
5. **Feedback / Evaluation loop** — đối chiếu lại dự đoán của AI theo thời gian để đo accuracy/precision/recall, dùng kết quả đó để tinh chỉnh ngưỡng/rule kiểm duyệt và phân loại theo thời gian (cải thiện liên tục dựa trên feedback thực tế — không phải tự train lại model từ đầu).

Nguyên tắc không đổi dù mở rộng phạm vi: dùng API AI của bên thứ ba (không tự xây/train model), lớp AI tách riêng khỏi core, xử lý bất đồng bộ, có fallback khi lỗi/timeout.

> Related Posts (gợi ý bài liên quan) có thể tận dụng chung hạ tầng embedding với Semantic Search gần như miễn phí về công sức, nhưng không nằm trong danh sách bắt buộc ở trên — làm thêm nếu thuận tiện.

## 7. Kiến trúc tổng quan

- Backend RESTful API cho Forum, Group, Reward, Moderation — lớp AI tách riêng khỏi phần lõi.
- Nhắn tin dùng kênh real-time riêng bằng WebSocket — khác kiến trúc request–response với phần còn lại; cả 2 thành viên cần nắm được cả hai kiểu kiến trúc khi làm SA.
- CSDL: PostgreSQL, mở rộng pgvector cho Semantic Search.
- AI Layer: gọi API bên thứ ba, xử lý bất đồng bộ, có fallback khi lỗi/timeout, kèm vòng phản hồi đo lại độ chính xác theo thời gian (mục 6.5).

## 8. Quyết định phạm vi — Không làm (đã cân nhắc, có lý do)

- **Gọi thoại, gọi video, gửi file trong Nhắn tin** — cần WebRTC/TURN-STUN/media server/object storage, vượt khả năng team 2 người trong thời gian dự án.
- **Phân biệt tài khoản Giáo viên/Học sinh**, ưu tiên hiển thị, leaderboard/badge riêng cho giáo viên — số lượng giáo viên thực tế quá nhỏ để có ý nghĩa, chi phí xây gần như nhân đôi hệ Reward.
- **Liên kết bài viết tới thư viện số của trường** — thư viện số chưa xây xong, để ngỏ cho giai đoạn sau.
- **AI tự viết bài/comment, AI tự quyết định reputation/badge/Accepted Answer, chatbot/RAG phức tạp, multi-agent, tự train/fine-tune model** — ngoài phạm vi năng lực và mục tiêu của lớp AI hỗ trợ trong dự án này.