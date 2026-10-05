# Disposition — M05 (tệp làm việc của Author)

Phân loại từng mục nguồn không nằm trong SR/routing. Auditor đọc tệp này sau khi hoàn tất ma trận độc lập của mình (RULES §7.7, CL-A03).

## OWNED (20 mục) — đã xử lý hết, xem SR Phụ lục A + routing R1/R4

DEC-047…052, ISS-079…084, QA-101…108: toàn bộ 20 mục đã vào SR `ISH-SR-M05.md` Phụ lục A hoặc routing `ISH-RT-M05.md` (R1/R4). Xem `check_sr.py` COV-00/COV-01 = sạch.

## REFERENCING (19 mục)

| ID | Đích | Lý do |
|---|---|---|
| DEC-008 | SR | AI off fallback cho M05 — cited ISH-M05-002.7 |
| DEC-090 | SR | "Shared with Mod: Topic edit/merge, Tag crisis soft-delete" — cited ISH-M05-003, ISH-M05-005 |
| DEC-093 | SR | Per-module AI toggle cho Topic suggestion — cited ISH-M05-002.7 |
| DEC-095 | Không liên quan | Chỉ nhắc M05 như ví dụ tương tự ("mirrors is_stale pattern from M05") cho cơ chế recompute embedding của M13; không tạo nội dung mới cho M05 |
| DEC-099 | SR + R2 | AI failure handling cho Topic suggest — cited ISH-M05-002.8 (hành vi) + R2 (timeout/retry) |
| DEC-124 | Không liên quan | Thuộc M14 (Trending Post, decay formula mới); chỉ xác nhận DEC-052 (M05) giữ nguyên, không đổi |
| DEC-125 | Không liên quan | Thuộc M14 (cấu trúc 4 tab Feed); chỉ liệt kê M05 là dependency, không mô tả hành vi M05 |
| ISS-171 | Không liên quan | Thuộc M14; xác nhận Trending Topic/Tag (DEC-052) không đổi, Trending Post là khái niệm mới của M14 |
| ISS-185 | Không liên quan | Thuộc M14 (công thức decay Trending Post); nhắc lại DEC-052 không đổi |
| ISS-186 | Không liên quan | Thuộc M14 (bỏ dependency M13); giữ dependency M05 nhưng không mô tả hành vi mới của M05 |
| QA-024 | Không liên quan | Thuộc M13 (MoSCoW AI Layer); chỉ nhắc M05 là một lý do elevate M13 lên Must |
| QA-226 | Không liên quan | Thuộc M14; xác nhận Trending Topic/Tag (DEC-052) giữ nguyên |
| QA-237 | Không liên quan | Thuộc M14 (cơ chế polling của Feed); không liên quan hành vi M05 |
| QA-240 | Không liên quan | Thuộc M14 (bỏ dependency M13); không mô tả hành vi mới của M05 |
| DEC-139 | Không liên quan | Quy trình soạn tài liệu SR (meta), không phải nội dung nghiệp vụ của M05 |
| ISS-205 | Không liên quan | Quy trình soạn tài liệu SR (meta) |
| QA-265 | Không liên quan | Quy trình soạn tài liệu SR (meta) |
| OPEN-006 | Không liên quan | SEO/SSR hoãn ở MS1, thuộc phạm vi hiển thị Feed của M14; không tạo yêu cầu chức năng cho M05 |
| OPEN-008 | Không liên quan | Tự ghi rõ "Không block SR M05" |

## KEYWORD (lấy mẫu có chủ đích — các mục có từ khóa nghiệp vụ trùng M05)

| ID | Đích | Lý do |
|---|---|---|
| ISS-046, QA-033, QA-034 | R5 (phần grade_level) + R6 (phần 2 tầng, đã bị thay bởi DEC-140) | Xem routing R5/R6 |
| DEC-053…060, ISS-085/086/088/090/093, QA-109/112/113/115 (M06 Search) | Không liên quan | Search dùng Topic/Tag làm đối tượng tìm kiếm/lọc — thuộc M06, không mô tả hành vi của M05 |
| DEC-096 (Topic suggestion model) | Không liên quan | Chọn model AI (GPT-4o-mini) thuộc M13, là chi tiết công nghệ không vào SR của module nào theo nghiệp vụ; M05 chỉ cần hành vi "gợi ý bằng AI", không cần tên model |
| ISS-125, ISS-129, QA-169, QA-175, QA-178 (M13 AI Layer) | Không liên quan | Thuộc M13 (model, timeout, rate limit AI nói chung); chi tiết timeout/retry riêng cho Topic suggestion đã lấy từ DEC-099 |
| DEC-132, ISS-194, QA-253 | SR (sửa theo AUD-M05-02, vòng 1) | Nội dung chỉ nói riêng về whitelist 11-Topic của M05 (AI trả Topic ngoài danh sách → lỗi không chặn) — không áp dụng module khác. Đã sửa: thêm ISH-M05-002.9. (Trước đó bị gộp nhầm vào nhóm "không liên quan" cùng DEC-133 — Auditor vòng 1 chỉ ra đúng) |
| DEC-133, ISS-195, QA-254 (log raw output AI) | Không liên quan | Thuộc Phase 6 cross-cutting AI, áp dụng chung nhiều module (Moderation/Embedding/Topic Suggestion); không có quyết định riêng cho M05 |
| QA-043, ISS-051 (Follow scope) | SR (sửa theo AUD-M05-03, vòng 1) | Follow Topic xác nhận thuộc M05 (DEC-141/QA-268); đã thêm tính năng ISH-M05-007 |
| Các mục còn lại của KEYWORD hits (M10/M12/M15/M16, Phase 3 Scope Decomposition không liên quan grade/topic của M05) | Không liên quan | Khớp từ khóa ("topic", "lớp", "chủ đề"...) nhưng nội dung thuộc module khác, không mô tả hành vi M05 |

## Ghi chú biên giới module (AUD-M05-07, vòng 2 — không chặn bàn giao M05)

module-registry.md:118 (Phase 3/5, ghi chú deep-dive M14) nói tab Following của M14 "reuses Follow targets from M07". DEC-141 (Phase SR, muộn hơn) nói M05 sở hữu quan hệ Follow/Unfollow cho Topic, M07 chỉ gửi thông báo. Hai mục không mâu thuẫn trực tiếp (M05 lưu quan hệ Follow Topic; M07/M14 là nơi tổng hợp/hiển thị cho tab Following và gửi thông báo) nhưng chưa có DEC nào xác nhận rõ sự ăn khớp này. **Dành cho Author của M07 và M14**: khi soạn SR, đọc DEC-141 (section "System Requirement — M05" của `decisions.md`) và routing `ISH-RT-M05.md` R5 trước khi viết phần Follow/Notification/Following-tab, để tránh giả định sai nơi lưu trữ quan hệ Follow Topic.

## CROSS-CUTTING (41 mục, chỉ tiêu đề) — áp dụng mục nào cho M05?

Không mục nào trong CROSS-CUTTING (timezone, data retention, file upload scan, AI privacy, tech stack, SSE, email, consent, OPEN-001…005/007) tạo hành vi chức năng riêng cho M05. Lý do: Trending dùng cửa sổ trượt tuyệt đối (không phụ thuộc lịch/múi giờ — DEC-052 tự nêu rõ khác với leaderboard theo lịch); M05 không có bảng upload file, không gửi email, không có luồng consent riêng.
