# Disposition — M05 Topic & Tag
<!-- [Vietnamese Doc] -->

Tệp làm việc của Author (RULES §7.7, sr-author Bước 2). Ngày: 2026-10-04. Inventory: `inventory-M05.md` (OWNED 31, REFERENCING 19, KEYWORD 96, CROSS 37).
Đích ∈ {SR, R1…R7, không liên quan}. "Q-n" = câu hỏi trong hàng đợi vấn đề (cuối tệp).

## OWNED

| ID | Nội dung ngắn | Đích | Ghi chú |
|---|---|---|---|
| DEC-047 | Topic = taxonomy có cấu trúc, AI gợi ý + user xác nhận, dùng lọc/duyệt, phẳng; Tag = #hashtag tự do, không danh sách cố định, không khoảng trắng | SR, R5 | Lọc theo Topic → R5 M06 (DEC-056); "duyệt" → Q-14 (sở hữu) |
| DEC-048 | Danh sách 11 Topic (final) | SR | Lệch DRAFT §3.1 (danh sách chưa cố định, 16 ví dụ) — DRAFT tự nói chốt ở BA, không mâu thuẫn |
| DEC-049 | Min 1, max 3 Topic/bài; Mod/Admin đổi tên + gộp, không xóa; gộp chuyển liên kết bài | SR | Topic nguồn sau gộp → Q-4; người theo dõi → Q-5; lệch DRAFT §3.4 (một Topic) → Q-1 |
| DEC-050 | Luồng gợi ý Topic bằng AI (nút, chỉ văn bản, tối đa 3, chọn sẵn, <20 từ, is_stale, phản hồi, chọn tay, AI tắt) | SR, R3 | Thông điệp "content too short", nút gợi ý lại → R3; đếm 20 từ → Q-8; chọn sẵn vs lựa chọn đang có → Q-9; "content changed" → Q-10 |
| DEC-051 | Tag: bảng tags/post_tags; tự tạo; max 5/bài, 30 ký tự; Mod/Admin không sửa/gộp/xóa; vô hiệu hóa khi khẩn cấp | SR, R1, R5 | Bảng/cột/is_active → R1; ẩn khỏi autocomplete → R5 M06; lệch DRAFT §3.2 (không giới hạn) → Q-2; mở lại Tag → Q-12; cách đếm 30 ký tự → Q-13 |
| DEC-052 | Trending Topic/Tag: cửa sổ trượt 7 ngày, tính lại 15–30 phút, công thức, đưa vào Feed | SR, R2, R5 | Chu kỳ tính lại (cache) → R2; hiển thị trong Feed → R5 M14; bài nào được tính → Q-6; tương tác nào → Q-7 |
| DEC-140 | Topic phẳng, ghi đè 2 tầng QA-033/ISS-046; grade_level ngoài M05 | SR, R5, R6 | grade_level → R5 M03/M02; QA-033 → R6 |
| DEC-141 | M05 sở hữu Follow Topic (nút, trạng thái, số người theo dõi); không áp dụng Tag; thông báo bài mới → M07 | SR, R5, R7 | Thông báo → R5 M07; Follow Tag → R7 |
| DEC-142 | Làm rõ công thức Trending: tương tác trong cửa sổ trên mọi bài + thưởng 1 cho bài đăng trong cửa sổ | SR | |
| ISS-079 | Phân biệt Topic/Tag | SR | Cùng DEC-047 |
| ISS-080 | 11 Topic phẳng | SR | Cùng DEC-048 |
| ISS-081 | Luồng gợi ý Topic | SR | Cùng DEC-050 |
| ISS-082 | Giới hạn Tag + trending | SR | Cùng DEC-051/052 |
| ISS-083 | Min 1 max 3 Topic | SR | Cùng DEC-049 |
| ISS-084 | Sửa/gộp/xóa Topic/Tag | SR | Cùng DEC-049/051 |
| ISS-207 | Flat hay 2 tầng | SR | Cùng DEC-140 |
| ISS-208 | Sở hữu Follow Topic | SR | Cùng DEC-141 |
| ISS-209 | AI gợi ý Tag? | R7 | Chủ đích không gợi ý Tag (QA-269) |
| ISS-210 | Cửa sổ Trending | SR | Cùng DEC-142 |
| QA-101 | Topic có cấu trúc; Tag #hashtag không khoảng trắng | SR | |
| QA-102 | Phẳng 11 Topic (nhóm theo chương trình 2018 + phi học thuật) | SR, R4 | Lý do nhóm → R4 |
| QA-103 | Gợi ý tối đa 3 | SR | |
| QA-104 | Nội dung đổi sau gợi ý → is_stale | SR | |
| QA-105 | Max 5 Tag, 30 ký tự | SR | |
| QA-106 | Công thức Trending | SR, R2 | |
| QA-107 | Topic sửa+gộp không xóa; Tag vô hiệu hóa khi khẩn cấp, tên thành "reserved" | SR | |
| QA-108 | Bình luận không có Tag | R7 | |
| QA-267 | Flat, 11 giá trị cố định | SR | |
| QA-268 | Follow Topic thuộc M05, không Tag | SR, R7 | |
| QA-269 | Không có AI gợi ý Tag | R7 | |
| QA-270 | Cửa sổ và "+1" | SR | |
| module-registry L12 | Dòng M05 | SR, R1 | "tags+post_tags tables" → R1 |
| module-registry L21 | M14 phụ thuộc M05; Trending sub Topic/Tag | R5 | M14 |

## REFERENCING

| ID | Nội dung ngắn | Đích | Ghi chú |
|---|---|---|---|
| DEC-008 | AI tắt → M05 user tự chọn Topic | SR, R5 | Nơi lưu cờ → R5 M10 |
| DEC-090 | Mod dùng chung với Admin: sửa/gộp Topic, vô hiệu hóa Tag | SR, R5 | Phần còn lại của DEC-090 → M10 |
| DEC-093 | Công tắc AI tổng + công tắc gợi ý Topic | SR, R5 | Công tắc → R5 M10 |
| DEC-095 | Embedding, "mirrors is_stale pattern" | không liên quan | Nói về embedding của M06/M13, chỉ mượn tên khái niệm |
| DEC-099 | Lỗi tạm thời AI: timeout 10 s, 1 lần thử lại, Topic → báo lỗi không chặn | SR, R2, R5 | Timeout/retry → R5 M13 + R2 |
| DEC-124 | Trending Post (M14) dùng decay; điểm gốc thêm bookmark và người xem (DEC-158) | R5 | M14 |
| DEC-125 | Feed 4 tab; Trending sub Topic/Tag; Following theo đối tượng theo dõi | R5 | M14 |
| ISS-171 | Trending Section tái dùng DEC-052? (superseded by ISS-185) | không liên quan | Nội bộ M14, đã thay bởi ISS-185 |
| ISS-185 | Công thức Trending Post | R5 | Gộp hàng DEC-124 |
| ISS-186 | M14 bỏ phụ thuộc M13 | không liên quan | Phụ thuộc của M14 |
| QA-024 | AI Layer là Must vì M05/M06/M08 cần | không liên quan | Ưu tiên của M13 |
| QA-226 | Trending Post decay; Topic/Tag giữ DEC-052 | R5 | Gộp hàng DEC-124 |
| QA-237 | Trending tự làm mới theo chu kỳ tính lại | R5 | M14 |
| QA-240 | M14 bỏ phụ thuộc M13 | không liên quan | Như ISS-186 |
| DEC-139 | Cách viết SR | không liên quan | Quy trình tài liệu |
| ISS-205 | Cách viết SR | không liên quan | Quy trình tài liệu |
| QA-265 | Cách viết SR | không liên quan | Quy trình tài liệu |
| OPEN-006 | SEO/SSR defer | không liên quan | Không hành vi M05 |
| OPEN-008 | Privacy chưa định nghĩa | không liên quan | Mục 4.1 = Không có |

## KEYWORD và CROSS-CUTTING (mỗi mục một dòng; mục không nằm ở SR hay routing ghi "không liên quan" kèm lý do — RULES §7.7)

| ID | Nội dung ngắn | Đích | Ghi chú |
|---|---|---|---|
| QA-011 | Guest xem danh sách Topic/Tag/Khối lớp, xem bài viết và phân loại trên bài; không tương tác | SR, R5 | Danh sách Topic → ISH-M05-001.3; Topic/Tag trên bài → ISH-M05-002.10, 006.16; danh sách Tag → R5 (DEC-163); Khối lớp → R5 M02/M03 |
| QA-017 | AI gợi ý Topic, không auto-gán; Tag không AI; lựa chọn cuối là phản hồi | SR | |
| QA-033 | 2 tầng Category→Topic | R6 | Bị thay bởi DEC-140 |
| ISS-046 | Classification depth | R6 | Bị thay bởi DEC-140 |
| QA-034 | grade_level trên Profile | R5 | M02 |
| QA-043 | Follow User/Topic/Post, thông báo bài mới trong Topic | SR, R5 | Follow Topic → SR; thông báo → R5 M07; Follow User/Post → module khác |
| ISS-051 | Follow scope | SR | Cùng QA-043 |
| DEC-065 | Danh sách sự kiện thông báo | R5 | Sự kiện "bài mới trong Topic đang theo dõi" đã thêm theo DEC-155 |
| QA-123 | Như DEC-065 | R5 | Gộp hàng DEC-065 |
| DEC-053, DEC-054, DEC-056, DEC-058, DEC-060, ISS-085, ISS-086, ISS-088, ISS-090, ISS-093, QA-109, QA-113, QA-115 | Tìm/lọc/autocomplete Topic và Tag | R5 | M06 |
| DEC-057, ISS-091 | FTS không dấu | không liên quan | Kỹ thuật tìm kiếm của M06 |
| DEC-096, ISS-125, QA-169 | Mô hình gợi ý Topic GPT-4o-mini | R5 | M13 |
| QA-175 | Timeout 10 s cho gợi ý Topic | R2, R5 | M13 |
| DEC-100, ISS-129, QA-178 | Giới hạn 10 lần/phút/người dùng cho nút gợi ý Topic | SR, R2 | Cửa sổ đếm → R2 |
| DEC-132, ISS-194, QA-253 | AI trả Topic ngoài 11 Topic → coi như lỗi gợi ý | SR, R3 | Văn bản thông báo → R3; trả về một phần hợp lệ → Q-11 |
| DEC-133, ISS-195, QA-254 | Lưu raw output AI | R1, R5 | M13 |
| ISS-119, QA-160 | Mod dùng chung quản lý Topic/Tag | SR | |
| ISS-122, QA-165 | Công tắc AI theo module | SR | |
| DEC-126, ISS-166, QA-227 | Guest xem Trending Topic/Tag; theo dõi cần đăng nhập | SR, R5 | Hiển thị tab → R5 M14 |
| QA-228, ISS-169 | Tab Following rỗng | không liên quan | M14; xác nhận Tag không theo dõi được |
| QA-231, ISS-172 | Trending Post không lọc Topic | không liên quan | M14 |
| QA-235, ISS-175 | Không ngưỡng tối thiểu vào Trending | SR, R5 | Topic/Tag → ISH-M05-008.18, 008.19 (DEC-161); Trending Post → R5 M14 |
| QA-236, ISS-176 | Trending không loại bài của user BANNED/HEAVY warn | R5 | Dùng làm ngữ cảnh cho Q-6 |
| QA-243, ISS-180 | Thống kê phân bố Post theo Topic | không liên quan | M15 sở hữu |
| DEC-066 | Gộp thông báo upvote trong 5 phút | không liên quan | Quy tắc thông báo của M07, không đổi hành vi Topic/Tag |
| DEC-070 | Không có tùy chọn tắt thông báo theo nhóm | không liên quan | Cấu hình thông báo M07; khớp từ khóa "category" |
| DEC-097 | Ánh xạ nhóm vi phạm của AI kiểm duyệt | không liên quan | M13/M08; "category" là nhóm vi phạm, không phải Topic |
| DEC-098 | Ngưỡng tin cậy 0,9/0,5 của AI kiểm duyệt | không liên quan | M13/M08; không dùng cho gợi ý Topic |
| ISS-101 | Tùy chọn thông báo | không liên quan | Như DEC-070 |
| ISS-126 | Ánh xạ nhóm vi phạm | không liên quan | Như DEC-097 |
| ISS-168 | Các tab của Feed M14 | không liên quan | Đã xử lý qua DEC-125 ở routing R5 |
| ISS-173 | Bài Group Public chia sẻ ra feed có tính vào Newest/Trending Post | không liên quan | Chỉ về Trending Post (M14); Trending Topic/Tag theo DEC-146 |
| ISS-177 | Feed tự cập nhật bài mới | không liên quan | M14; phần Trending đã ở routing R5 qua QA-237 |
| ISS-181 | Chỉ số dashboard kiểm duyệt | không liên quan | M15 |
| ISS-190 | Đa ngôn ngữ | không liên quan | Khớp từ khóa "tag" trong từ khác; không hành vi M05 |
| QA-004 | Bối cảnh cạnh tranh | không liên quan | Phase 1, không hành vi |
| QA-005 | Mục tiêu kinh doanh | không liên quan | Phase 1, không hành vi riêng của M05 |
| QA-006 | Xác nhận mục tiêu kinh doanh | không liên quan | Phase 1, không hành vi riêng của M05 |
| QA-007 | Ngân sách AI | không liên quan | Chi phí, thuộc OPEN-001 |
| QA-012 | Cách phong Mod | không liên quan | M10; khớp từ khóa "suggest" |
| QA-022 | Phạm vi tìm kiếm Phase 3 | không liên quan | Bị thay bởi QA-109 (M06), đã ở routing R5 |
| QA-112 | Trọng số tương tác trong xếp hạng tìm kiếm | không liên quan | Công thức xếp hạng tìm kiếm của M06, khác điểm Trending |
| QA-149 | Phát hiện báo cáo sai | không liên quan | M08; cửa sổ 90 ngày không liên quan Trending |
| QA-153 | Hạn kháng nghị | không liên quan | M09; khớp từ khóa "flat" |
| QA-194 | Tiêu chí huy hiệu | không liên quan | M12 |
| QA-203 | Bảng xếp hạng tính định kỳ | không liên quan | M12; khớp từ khóa "gộp" |
| QA-211 | Trạng thái "đã xem" của group chat | không liên quan | M16 |
| QA-225 | Các tab của Feed M14 | không liên quan | Như ISS-168 |
| QA-232 | Bài Group Public chia sẻ ra feed | không liên quan | Như ISS-173 |
| QA-233 | Làm rõ QA-232 | không liên quan | Như ISS-173 |
| QA-234 | Phân trang Feed | không liên quan | M14 |
| QA-244 | Chỉ số dashboard kiểm duyệt | không liên quan | Như ISS-181 |
| QA-249 | Đa ngôn ngữ | không liên quan | Như ISS-190 |
| QA-262 | Cách tiếp cận Phase 8 | không liên quan | Quy trình mô hình dữ liệu |
| QA-127 | Không có follow-post | không liên quan | M07; mâu thuẫn với QA-043 về Post là việc của M07 |
| DEC-031, DEC-032, DEC-033, DEC-034 | Trạng thái bài viết, quy tắc hiển thị | không liên quan | Đọc làm ngữ cảnh Q-6, Q-3; M03 sở hữu |
| DEC-127 | Múi giờ UTC+7 cho ranh giới ngày | không liên quan | Cửa sổ Trending trượt từ thời điểm hiện tại (DEC-052), không theo ranh giới ngày |
| DRAFT §3.1 | Topic tổ chức lĩnh vực tri thức; danh sách chưa cố định | SR | Lý do; danh sách theo DEC-048 |
| DRAFT §3.2 | Nhiều Tag, không giới hạn số lượng | SR | Lệch DEC-051 → Q-2 |
| DRAFT §3.3 | Lớp/Khối; Personalized Feed | R5, R6 | Khối lớp → M02/M03 (DEC-140); Personalized Feed → R6 bởi DEC-125 |
| DRAFT §3.4 | Post → một Topic, Khối lớp tùy chọn, N Tag | SR | Lệch DEC-049 → Q-1 |
| DRAFT §4.5 | Follow Post/User/Topic/Tag/Group | SR, R5, R7 | Topic → SR; Tag → R7 (DEC-141) |
| DRAFT §11.2 | AI gợi ý Topic + Tag; User/Moderator review | SR, R6 | Tag → R6 (QA-269); Moderator review → Q-3 |
| iShare_dev_priority.md | Tag/Topic P0; AI Classification AI-P0; Follow P1; Feedback loop AI-P1 | SR (5.1) | Mốc theo tính năng → Q-14 |

### Mục KEYWORD và CROSS-CUTTING còn lại (thêm ở v0.3, AUD-M05-17)

| ID | Nội dung ngắn | Đích | Ghi chú |
|---|---|---|---|
| DEC-025 | Followers / Following display | không liên quan | Thuộc section "Phase 5 — M02: User Profile"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| DEC-067 | In-app notification UI | không liên quan | Thuộc section "Phase 5 — M07: Notification"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| DEC-104 | Group content moderation layers on top of system-wide M08, does not replace it | không liên quan | Thuộc section "Phase 5 — M11: Group"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| ISS-059 | Followers/Following visibility | không liên quan | Thuộc section "Phase 5 — M02: User Profile"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| ISS-099 | In-app UI (bell/page, mark read) | không liên quan | Thuộc section "Phase 5 — M07: Notification"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| ISS-161 | Rate limiting cho chat — có cần giới hạn số tin/phút không, mức nào? | không liên quan | Thuộc section "Phase 5 — M16: Chat & Messa"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| ISS-162 | Ai nhắn tin (DM) được cho ai — mở hoàn toàn, cần mutual follow, hay message request như Me | không liên quan | Thuộc section "Phase 5 — M16: Chat & Messa"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| ISS-164 | Group Chat — cơ chế quản trị: role, add/remove member, đổi tên, kiểm duyệt, rời nhóm, kế n | không liên quan | Thuộc section "Phase 5 — M16: Chat & Messa"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| ISS-179 | User Stats dashboard gồm những chỉ số nào? | không liên quan | Thuộc section "Phase 5 — M15: Analytics &"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-047 | Points có nên giảm theo thời gian (decay) không? | không liên quan | Thuộc section "Phase 3 — Scope Decompositi"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-067 | Profile page info? | không liên quan | Thuộc section "Phase 5 — M02: User Profile"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-069 | Followers/following list hidden? | không liên quan | Thuộc section "Phase 5 — M02: User Profile"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-128 | Bell UI structure? | không liên quan | Thuộc section "Phase 5 — M07: Notification"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-192 | ISS-143: Badge nên permanent hay revocable? Audit trail ra sao? | không liên quan | Thuộc section "Phase 5 — M09 Amendment + M"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-219 | ISS-161: Rate limiting cho chat — có cần không, mức nào? | không liên quan | Thuộc section "Phase 5 — M16: Chat & Messa"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-220 | ISS-162: Ai nhắn tin (DM) được cho ai — mở hoàn toàn, cần mutual follow, hay message reque | không liên quan | Thuộc section "Phase 5 — M16: Chat & Messa"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-222 | ISS-164: Group Chat — quản trị ra sao (role, add/remove, kiểm duyệt, đổi tên, rời nhóm, kế | không liên quan | Thuộc section "Phase 5 — M16: Chat & Messa"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-230 | ISS-188: Tab Group hiện/ẩn theo điều kiện nào? | không liên quan | Thuộc section "Phase 5 — M14: Feed & Disco"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-239 | ISS-177 (amend): banner nên polling hay real-time (SSE)? | không liên quan | Thuộc section "Phase 5 — M14: Feed & Disco"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-242 | ISS-179: User Stats dashboard gồm những chỉ số nào? | không liên quan | Thuộc section "Phase 5 — M15: Analytics &"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| DEC-137 | Confirmed technology stack (closes OPEN-002) | không liên quan | Thuộc section "Phase 7 prep — Tech Stack ("; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| ISS-192 | File/media upload — có cần cơ chế scan virus/malware không? | không liên quan | Thuộc section "Phase 6 — Cross-cutting Con"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-251 | ISS-192: File/media upload — có cần cơ chế scan virus/malware không? | không liên quan | Thuộc section "Phase 6 — Cross-cutting Con"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-256 | ISS-197: Tech stack — Backend/Frontend framework, và có cần SSR/SEO ở MS1 không? | không liên quan | Thuộc section "Phase 7 prep — Tech Stack ("; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-258 | ISS-199: Email — thư viện và nguồn SMTP gửi mail? | không liên quan | Thuộc section "Phase 7 prep — Tech Stack ("; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| ISS-204 | Quy ước ID cho tài liệu SR | không liên quan | Thuộc section "và privacy xây dựng thế nào?
- ISS-206 (issue-queue.md:321"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| QA-248 | ISS-206: Quy ước ID cho tài liệu SR? | không liên quan | Thuộc section "và privacy xây dựng thế nào?
- QA-266 (qa-log.md:995"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| OPEN-003 | — thư viện nền chưa chốt; stakeholder nghiêng về MUI nhưng phải đợi có de… | không liên quan | Thuộc section "DEC-134"; không có hành vi Topic/Tag của M05 (khớp từ khóa chung) |
| DEC-135 | Realtime channel — SSE only | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| DEC-136 | Email delivery — Spring Mail over standard SMTP | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| DEC-138 | Consent to Privacy Policy/ToS is mandatory at registration | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| ISS-189 | Timezone & date handling — lưu trữ/tính toán theo múi giờ nào? | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| ISS-191 | Data retention tổng quát — audit log và chat message có cần policy xóa/lưu trữ gì không? | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| ISS-193 | AI — nội dung user gửi ra OpenAI (3rd party) có cần xử lý gì về privacy không? | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| ISS-196 | Analytics events — có cần hạ tầng event-tracking chung (ngoài 3 dashboard M15) không? | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| ISS-198 | Kênh realtime — thống nhất SSE hay giữ WebSocket cho thông báo? | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| ISS-200 | Cờ `AI_ENABLED` (DEC-008) — lưu ở đâu: env var hay Admin config? | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| ISS-201 | Hosting / deployment cho MS1 | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| ISS-202 | Ràng buộc học thuật về công nghệ (đóng ISS-029) | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| ISS-203 | Xác nhận nhóm công nghệ ngầm định (PostgreSQL+pgvector, Cloudinary, OpenAI, Tiptap, JWT) | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| QA-250 | ISS-191: Data retention tổng quát — audit log và chat message có cần policy xóa/lưu trữ gì | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| QA-252 | ISS-193: AI — nội dung user gửi ra OpenAI (3rd party) có cần xử lý gì về privacy không? | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| QA-255 | ISS-196: Analytics events — có cần hạ tầng event-tracking chung (ngoài 3 dashboard M15) kh | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| QA-257 | ISS-198: Kênh realtime — thống nhất SSE hay giữ WebSocket cho thông báo? | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| QA-259 | ISS-200: Cờ `AI_ENABLED` lưu ở đâu? | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| QA-260 | ISS-201: Hosting / deployment ở MS1? | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| QA-261 | ISS-202 (đóng ISS-029): Có ràng buộc học thuật nào về công nghệ không? | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| QA-263 | ISS-203: Xác nhận nhóm công nghệ ngầm định? | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| QA-264 | ISS-204: Có yêu cầu đồng ý Privacy Policy/ToS khi đăng ký không, và privacy xây dựng thế n | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| OPEN-004 | Analytics & Stats (M15) — chưa có export CSV cho 3 dashboard ở MS1 (ISS-184) — quyết định  | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| OPEN-005 | Cross-cutting (Phase 6) — chưa xây hạ tầng event-tracking chung (ISS-196) — quyết định def | không liên quan | CROSS-CUTTING (Phase 6/7 prep, SR prep); không có hành vi Topic/Tag của M05 |
| DEC-128 | i18n/localisation scope | không liên quan | Mục chung (cross-cutting hoặc module khác); không có hành vi Topic/Tag của M05 |
| DEC-130 | File/media upload — no virus/malware scanning | không liên quan | Mục chung (cross-cutting hoặc module khác); không có hành vi Topic/Tag của M05 |
| DEC-129 | Data retention — audit log & chat messages (general hard-delete principle) | không liên quan | Mục chung (cross-cutting hoặc module khác); không có hành vi Topic/Tag của M05 |
| DEC-131 | AI — third-party data privacy disclosure | không liên quan | Mục chung (cross-cutting hoặc module khác); không có hành vi Topic/Tag của M05 |
| OPEN-007 | UI Kit (ISS-197, DEC-134) — thư viện nền chưa chốt; stakeholder nghiêng về MUI nhưng phải  | không liên quan | Mục chung (cross-cutting hoặc module khác); không có hành vi Topic/Tag của M05 |
| DEC-015 | Trường định danh display_name, username | không liên quan | M01; khớp từ khóa "dropdown" |
| DEC-020 | Hệ thống @mention | không liên quan | M01/M04; khớp từ khóa "follow", "dropdown" (ưu tiên người đang theo dõi người dùng), không liên quan theo dõi Topic |

## Hàng đợi vấn đề

| Q | Loại | Vấn đề | Trạng thái |
|---|---|---|---|
| Q-1 | Mâu thuẫn (DRAFT↔register) | DRAFT §3.4 một Topic/bài, DEC-049 1–3 | Đã trả lời — ISS-211/QA-271/DEC-143 |
| Q-2 | Mâu thuẫn (DRAFT↔register) | DRAFT §3.2 Tag không giới hạn, DEC-051 tối đa 5; tối thiểu? | Đã trả lời — ISS-212/QA-272/DEC-143 |
| Q-3 | GAP | Đổi Topic/Tag sau khi gửi bài: ai, khi nào (DRAFT §11.2 nhắc Moderator review) | Đã trả lời — ISS-213/QA-273/DEC-144 |
| Q-4 | GAP | Topic nguồn sau khi gộp | Đã trả lời — ISS-214/QA-274/DEC-145 |
| Q-5 | GAP | Người theo dõi Topic nguồn sau khi gộp | Đã trả lời — ISS-215/QA-275/DEC-145 |
| Q-6 | Mơ hồ | Trending: bài ở trạng thái nào được tính | Đã trả lời — ISS-216/QA-276/DEC-146 |
| Q-7 | Mơ hồ | Trending: "upvotes", "comments" gồm những gì | Đã trả lời — ISS-217/QA-277/DEC-146 |
| Q-8 | Mơ hồ | Ngưỡng 20 từ đếm trên phần nào, đếm thế nào | Đã trả lời — ISS-218/QA-278/DEC-147 |
| Q-9 | GAP | Chọn sẵn Topic gợi ý khi đã có Topic được chọn tay | Đã trả lời — ISS-219/QA-279/DEC-148 |
| Q-10 | Mơ hồ | "Content changed" gồm thay đổi tiêu đề? | Đã trả lời — ISS-220/QA-280/DEC-148 |
| Q-11 | Mơ hồ | AI trả về một phần Topic hợp lệ | Đã trả lời — ISS-221/QA-281/DEC-149 |
| Q-12 | GAP | Mở lại Tag đã vô hiệu hóa | Đã trả lời — ISS-222/QA-282/DEC-150 |
| Q-13 | Mơ hồ | 30 ký tự có tính dấu # | Đã trả lời — ISS-223/QA-283/DEC-150 |
| Q-14 | Đề xuất | Khung tính năng, sở hữu "duyệt theo Topic/Tag", mốc phần ghi nhận phản hồi | Đã trả lời — ISS-224/QA-284/DEC-151 |
| Q-15 | Mơ hồ (ca kiểm T-021) | AI trả về hơn 3 Topic hợp lệ | Đã trả lời — ISS-225/QA-285/DEC-152 |
| Q-16 | Mơ hồ (ca kiểm T-066) | Chuẩn hóa tên Tag khi nhập | Đã trả lời — ISS-226/QA-286/DEC-152 |
| Q-17 | GAP (selfcheck CL-A06) | Thứ tự xếp hạng Trending, phá hòa | Đã trả lời — ISS-227/QA-287/DEC-153 |

## Mục register mới của SR M05 (sau phiên hỏi)

| ID | Đích | Ghi chú |
|---|---|---|
| ISS-211…227, QA-271…287 | SR, R4, R6 | Câu hỏi/trả lời Q-1…Q-17 |
| DEC-143…153 | SR, R4, R5, R6 | DEC-151 → R4/R5 (khung, duyệt theo Topic/Tag thuộc M14/M06) |
| Q-18…Q-26 | Audit vòng 1 | AUD-M05-01, 02, 10, 13, 14, 15, 16, 18, 21 | Đã trả lời — ISS-228…236 / QA-288…296 / DEC-154…159 |
| Q-27…Q-32 | Audit vòng 2 | AUD-M05-24, 26, 27, 31 (hai phần), 32 | Đã trả lời — ISS-237…242 / QA-297…302 / DEC-160…163 |
