# Ma trận độ phủ độc lập — M05 · vòng 1 (lượt P1)
<!-- [Vietnamese Doc] -->

Lập từ `audit-inventory-P1-M05-r1.md` (OWNED 76, REFERENCING 20, KEYWORD 82, CROSS-CUTTING 42, DRAFT 27), DRAFT `iShare_modules.md` §3 (dòng 124–170) và các mục liên quan (§2.4, §4.5, §7.1–7.4, §8.1, §9.5, §11.2, §11.5), `iShare_specs_general.md` §3, `iShare_dev_priority.md` §3. Cột **Mong đợi** được điền **trước khi** mở thân SR/routing (P1.2). Cột **Thực tế** và **Kết quả** điền ở P1.4 (phần B).

## A. Ma trận mong đợi (lập trước khi đọc SR)

| # | Nguồn | Nội dung ngắn | Mong đợi | Lý do mong đợi |
|---|---|---|---|---|
| 1 | DRAFT §3.1 (modules.md:126–130) | Topic tổ chức lĩnh vực tri thức; danh sách chưa cố định | SR (danh mục Topic, theo DEC-048) + R6/R4 (câu "chưa cố định" bị DEC-048 thay) | Danh sách cụ thể đã chốt ở register |
| 2 | DRAFT §3.2 (modules.md:134) | Post có nhiều Tag, không giới hạn số lượng | SR (0–5 Tag theo DEC-143) + dấu vết lệch DRAFT ở Phụ lục A | §7.5: register thắng, DEC-143 ghi rõ ghi đè |
| 3 | DRAFT §3.3 (modules.md:153–161) | Lớp/Khối là trục phân loại song song; gắn Post và Profile; dùng lọc/Personalized Feed | module khác (M03 F-POST-09, M02) — R5 | DEC-140: grade_level ngoài phạm vi M05 |
| 4 | DRAFT §3.4 (modules.md:163–169) | Post → Topic/Category, Lớp/Khối, N Tags | SR (1–3 Topic theo DEC-143) + R5 (Lớp/Khối) | DEC-143 ghi đè sơ đồ một Topic |
| 5 | DRAFT §2.4 (modules.md:120) | Loại bài chỉ khác hiển thị thì Tag/Topic là đủ | R4 hoặc module khác (M03) | Ghi chú phạm vi, không tạo hành vi M05 |
| 6 | DRAFT §4.5 (modules.md:247–261) | Follow Topic, Tag (cùng Post, User, Group) | SR (Follow Topic) + R6/R7 (Tag không theo dõi, DEC-141) + R5 (Post/User → M07?; notification → M07) | DEC-141 |
| 7 | DRAFT §7.1 (modules.md:331) | Personalized Feed ưu tiên đúng Topic đang theo dõi | module khác (M14) — R5 | Feed thuộc M14; DEC-125 bỏ tab cá nhân hóa |
| 8 | DRAFT §7.2 (modules.md:333–341) | Trending có thể dựa trên Views/Stars/Comments/Bookmarks/Recency | SR (công thức theo DEC-052/142) + dấu vết lệch DRAFT; phần Trending Post → M14 | DRAFT lệch register (views, bookmarks không có trong DEC-052) |
| 9 | DRAFT §7.3, §7.4 (modules.md:343–365) | Tìm/lọc theo Topic, Tag | module khác (M06) — R5 | DEC-053/056 thuộc M06 |
| 10 | DRAFT §8.1 (modules.md:380) | Thông báo nội dung mới trong topic/tag đang follow | module khác (M07) — R5 | DEC-141: thông báo thuộc M07 |
| 11 | DRAFT §9.5 (modules.md:480–481) | Admin xem Popular topics / Popular tags | module khác (M15) — R5 | QA-243 (Topic distribution) thuộc M15 |
| 12 | DRAFT §11.2 (modules.md:581–600) | AI đề xuất Topic + Tags; User/Moderator review; user chỉnh trước khi publish | SR (gợi ý Topic, người dùng chỉnh) + R6/R7 (gợi ý Tag bị loại, QA-269) + SR (Mod đổi Topic, DEC-144) | QA-269, DEC-144 |
| 13 | DRAFT §11.5 (modules.md:630–653) | Feedback/Evaluation loop đo accuracy… | SR (ghi nhận phản hồi gợi ý Topic, DEC-050/QA-017) + module khác (M13: đo chỉ số) | DEC-151: mốc AI-P1 |
| 14 | specs_general §3 (specs_general.md:22–28) | Ba trục Topic / Lớp-Khối / Tag | SR (thuật ngữ) + R5 (Lớp/Khối) | — |
| 15 | specs_general §6 mục 2 (specs_general.md:63) | AI Classification gợi ý Topic/Tag, review trước publish | SR (Topic) + R6/R7 (Tag) | QA-269 |
| 16 | dev_priority §3 (dev_priority.md:36, 75, 83, 86, 99) | Tag, Topic P0; AI Classification AI-P0; Follow Topic/Tag P1; Trending Feed P1; Feedback loop AI-P1 | 5.1 (mốc) | Nguồn mốc cho 5.1 |
| 17 | module-registry L12 | Dòng M05 | SR (tổng) + R1 (tags+post_tags) | — |
| 18 | ISS-079, QA-101, DEC-047 | Topic: danh mục cấu trúc, AI gợi ý + người dùng xác nhận, dùng lọc/duyệt; flat. Tag: #hashtag tự do, gõ tay, không danh sách, không khoảng trắng | SR (Tag không khoảng trắng → giới hạn + từ chối) + R5 (lọc/duyệt → M06/M14, DEC-151) | "no spaces" là giới hạn kiểm chứng được |
| 19 | ISS-080, QA-102, DEC-048, DEC-140, ISS-207, QA-267 | 11 Topic phẳng, danh sách cố định; ghi đè 2 tầng | SR (danh mục 11 Topic) + R6 (QA-033/ISS-046 bị thay) | — |
| 20 | ISS-083, DEC-049 (dòng 284), DEC-143, ISS-211, QA-271 | 1–3 Topic mỗi bài, bắt buộc | SR (giới hạn dưới + trên) + SR (từ chối 0, từ chối thứ 4) | §4.2 mục 8 |
| 21 | DEC-049 (dòng 285–286), ISS-084, QA-107 (phần Topic) | Mod/Admin đổi tên + gộp Topic; không xóa; gộp chuyển bài sang Topic đích | SR (quyền đổi tên, gộp, chuyển bài, từ chối xóa) + R1 (post_topics) | — |
| 22 | ISS-081, QA-103, DEC-050, DEC-147, DEC-148, ISS-218–220, QA-278–280 | Nút gợi ý; AI đọc tiêu đề + nội dung văn bản, không xử lý đính kèm; tối đa 3, chọn sẵn; <10 tiếng → không gợi ý, báo quá ngắn; thay thế lựa chọn; người dùng sửa tự do; đổi tiêu đề/nội dung → cũ (stale), cảnh báo mềm + nút gợi ý lại, không chặn đăng; tự chọn từ đầu → bỏ luồng AI; AI tắt → chọn từ danh sách | SR (mỗi nhánh một yêu cầu) + R3 (nút, thông điệp, cảnh báo) | — |
| 23 | QA-104, DEC-050 (dòng 293), QA-017 | Phản hồi (gợi ý vs lựa chọn cuối) chỉ ghi khi không stale | SR (ghi nhận phản hồi, mốc AI-P1) + R1/R5 (M13 lưu, đo) | DEC-151 |
| 24 | DEC-149, ISS-221, QA-281, DEC-132 (REFERENCING) | Bỏ Topic không thuộc danh mục; giữ phần hợp lệ; không còn hợp lệ → thất bại, lỗi không chặn, chọn thủ công | SR + R3 (văn bản lỗi DEC-132) | DEC-149 sửa DEC-132 |
| 25 | DEC-152 (1), ISS-225, QA-285 | Hơn 3 Topic hợp lệ → giữ 3 đầu theo thứ tự trả về | SR | — |
| 26 | ISS-082, QA-105, DEC-051 (dòng 299–301), DEC-143, ISS-212, QA-272 | Tag tự tạo không duyệt; tối đa 5 Tag/bài; tối đa 30 ký tự; 0–5, không bắt buộc; tên duy nhất chuẩn hóa chữ thường | SR (tự tạo; giới hạn 5; từ chối thứ 6; 30 ký tự; từ chối 31; Tag trùng tên khác hoa/thường là một Tag) + R1 (bảng tags/post_tags, created_at) | Chuẩn hóa chữ thường có hệ quả quan sát được |
| 27 | DEC-150 (câu 2), ISS-223, QA-283; DEC-152 (2), ISS-226, QA-286 | 30 ký tự không tính "#"; bỏ khoảng trắng đầu/cuối; từ chối tên rỗng; mỗi chữ có dấu tính 1 | SR (mỗi quy tắc một yêu cầu) | — |
| 28 | DEC-051 (dòng 302–303), ISS-084, QA-107 (phần Tag) | Mod/Admin không sửa/gộp/xóa Tag thông thường; khủng hoảng: vô hiệu hóa → ẩn khỏi autocomplete/trending/browse; bài cũ ẩn chip; gõ lại tên bị vô hiệu → văn bản thường | SR (quyền vô hiệu hóa; ẩn chip; ẩn khỏi Trending; không tag hóa) + R5 (autocomplete → M06; browse → M06/M14) + R1 (is_active, giữ post_tags) | Tách theo câu |
| 29 | DEC-150 (câu 1), ISS-222, QA-282 | Mod/Admin mở lại Tag; Tag hiện lại trên bài cũ, dùng lại bình thường | SR | — |
| 30 | DEC-144, ISS-213, QA-273 | Tác giả đổi Topic + Tag khi sửa bài; Mod/Admin đổi Topic bất kỳ bài; Mod/Admin không đổi Tag; giới hạn áp dụng mọi lần đổi | SR (mỗi quyền một yêu cầu, từ chối Mod đổi Tag) | — |
| 31 | DEC-145, ISS-214, ISS-215, QA-274, QA-275 | Sau gộp: Topic nguồn rời danh mục (không chọn, gợi ý, Trending, theo dõi); người theo dõi chuyển sang Topic đích, tính một lần | SR | — |
| 32 | ISS-082 (phần trending), QA-106, DEC-052, DEC-142, ISS-210, QA-270 | Trending: cửa sổ trượt 7 ngày; tính lại mỗi 15–30 phút; điểm = Σ(2×upvote trong cửa sổ + bình luận trong cửa sổ) + số bài tạo trong cửa sổ; tích hợp Feed (M14) | SR (công thức, cửa sổ) + R2 (chu kỳ tính lại/cache, hoặc SR nếu là hành vi) + R5 (hiển thị trong Feed → M14) | Tách theo câu |
| 33 | DEC-146, ISS-216, ISS-217, QA-276, QA-277 | Chỉ bài công khai (PUBLISHED + NORMAL), không Group Private; không loại theo trạng thái tài khoản; upvote vào bài; mọi bình luận + trả lời; chỉ tương tác còn tồn tại | SR | — |
| 34 | DEC-153, ISS-227, QA-287 | Xếp điểm giảm dần; hòa → nhiều bài trong 7 ngày hơn; vẫn hòa → tên A→Z | SR | — |
| 35 | DEC-141, ISS-208, QA-268 | M05 sở hữu Follow/Unfollow Topic (nút, trạng thái, số người theo dõi); Tag không theo dõi; thông báo thuộc M07 | SR (theo dõi, bỏ theo dõi, số người theo dõi) + R3 (nút) + R5 (thông báo → M07) | Tách theo câu |
| 36 | ISS-209, QA-269 | AI không gợi ý Tag | R4/R7 (hoặc SR phủ định) + dấu vết lệch DRAFT §11.2 | — |
| 37 | QA-108 | Bình luận không có Topic/Tag riêng | R4/R7 | Câu hỏi đã đóng, không tạo hành vi |
| 38 | DEC-151, ISS-224, QA-284 | 12 tính năng; duyệt theo Topic/Tag thuộc M14/M06; mốc phản hồi = AI-P1; hành động Mod/Admin = P0 | 5.1 (mốc) + R4 (khung) + R5 (duyệt → M14/M06) | — |
| 39 | ISS-084 / QA-107 "name becomes reserved, non-tagifiable" | Tên bị vô hiệu thành tên dành riêng | SR (cùng #28) | — |
| 40 | DEC-008 (REF), DEC-093 (REF), DEC-099 mục 1 (REF) | AI tắt (master hoặc toggle Topic suggestion) → người dùng tự chọn Topic, không gợi ý | SR (fallback) + R5 (bật/tắt → M10) | M05 sở hữu hệ quả nhìn thấy |
| 41 | DEC-099 mục 2 (REF) | Lỗi tạm thời: timeout 10 s, thử lại 1 lần sau 2 s; hết lượt → lỗi không chặn, không làm gì | SR (lỗi không chặn) + R2 (timeout, retry) + R3 (văn bản) | Tách theo câu |
| 42 | DEC-100 (KEYWORD), ISS-129, QA-178 | Nút Gợi ý Topic: 10 lần/phút/người dùng | SR (giới hạn + từ chối khi vượt) + R2 (cơ chế đếm) | §6.1: hành vi → SR, chi tiết → R2 |
| 43 | DEC-090 (REF), ISS-119, QA-160 | Sửa/gộp Topic, vô hiệu hóa Tag dùng chung Mod và Admin | SR (vai trò Mod/Admin trong yêu cầu quyền) | — |
| 44 | DEC-096 (KEYWORD), ISS-125, QA-169 | Mô hình GPT-4o-mini | R2 hoặc R5 (M13) hoặc không liên quan | Công nghệ |
| 45 | QA-175 (KEYWORD) | Timeout 10 s LLM (Topic) | R2 (cùng #41) | — |
| 46 | DEC-133 (KEYWORD), ISS-195, QA-254 | Log raw output Topic Suggestion | R1/R5 (M13) | — |
| 47 | DEC-124, ISS-171, ISS-185, QA-226 (REF) | Trending Post decay; Trending Topic/Tag giữ DEC-052 | module khác (M14) — R5 hoặc không liên quan; xác nhận DEC-052 không đổi | — |
| 48 | DEC-125, QA-225, ISS-168 (REF/KEYWORD) | Tab Trending có sub Topic/Tag; Following theo Follow User/Topic/Post | R5 (M14 hiển thị) | — |
| 49 | DEC-126, QA-227, ISS-166 (KEYWORD) | Guest xem Trending Topic/Tag; mọi tương tác (follow) cần đăng nhập | SR (Guest không theo dõi Topic) hoặc R5 (M14 hiển thị) | Follow Topic thuộc M05 → quyền Guest là của M05 |
| 50 | QA-011 (KEYWORD) | Guest xem danh sách Topic / Tag; xem AI Classification trên bài | SR (Guest xem danh mục Topic) hoặc R5 | Quyền xem danh mục |
| 51 | QA-235, ISS-175 (KEYWORD) | Không đặt ngưỡng tối thiểu để vào Trending (MS1, tạm) | SR (không ngưỡng) hoặc R5 (M14) — cần phân loại | "Trending" chung, có thể áp dụng Topic/Tag |
| 52 | QA-236, ISS-176 (KEYWORD) | Trending không loại bài BANNED/HEAVY | SR (cùng #33, DEC-146 dẫn lại) | — |
| 53 | QA-237, ISS-177 (REF/KEYWORD) | Trending tự refresh theo chu kỳ 15–30 phút | R5 (M14) | — |
| 54 | QA-231, ISS-172 (KEYWORD) | Trending Post không lọc theo Topic | M14 — không liên quan M05 | — |
| 55 | QA-228, ISS-169 (KEYWORD) | Tag không phải đối tượng theo dõi | xác nhận DEC-141 | — |
| 56 | QA-043, ISS-051 (KEYWORD) | Follow Topic → nhận thông báo khi có bài mới trong Topic | SR (quan hệ theo dõi) + R5 (thông báo → M07) + R1 (`follows`) | — |
| 57 | QA-033, ISS-046 (KEYWORD) | 2 tầng Category→Topic | R6 (bị DEC-140 thay) | — |
| 58 | QA-034 (KEYWORD) | grade_level profile | R5 (M02) hoặc không liên quan | — |
| 59 | QA-017 (KEYWORD) | AI Classification gợi ý Topic, không tự gán; lựa chọn cuối là feedback; Tag do user quyết | SR (#22, #23) | — |
| 60 | DEC-053/054/056/057/058/060, QA-109/113/115, ISS-085/086/088/090/093 (KEYWORD) | Search/autocomplete/filter Topic, Tag | R5 (M06) hoặc không liên quan | — |
| 61 | QA-243, ISS-180 (KEYWORD) | Thống kê phân bố Post theo Topic | R5 (M15) hoặc không liên quan | — |
| 62 | DEC-127 (CROSS) | Múi giờ Asia/Ho_Chi_Minh cho tính ngày | xét áp dụng cho cửa sổ 7 ngày (trượt, không phải lịch) | — |
| 63 | OPEN-006 (REF) | SSR/SEO hoãn — liệt kê "Guest feed (M05/Feed tabs)" | R4/R5 hoặc không liên quan | — |
| 64 | DEC-139, ISS-205, QA-265, OPEN-008 (REF) | Quy trình SR; privacy | không liên quan / 4.1 (OPEN-008) | — |
| 65 | glossary.md:14, :15, :29 | Topic "List to be finalized"; AI Classification "Suggests Topic and Tags" | Lệch register-register (glossary chưa cập nhật) | — |

## B. Đối chiếu với SR v0.1 và routing v0.1 (P1.4)

Đọc theo thứ tự: header → mục 1–4 → 5.1, 5.2 → 5.3…5.14 → Phụ lục A → Phụ lục B → routing → lịch sử. `S:` = `ISH-SR-M05.md:dòng`; `R:` = `ISH-RT-M05.md:dòng`.

| # | Nguồn | Thực tế (SR / routing) | Kết quả | Finding |
|---|---|---|---|---|
| 1 | DRAFT §3.1 | Lý do 5.3 (S:134); ISH-M05-001.1 ghi DRAFT §3.1 ở Phụ lục A (S:439) | Khớp | — |
| 2 | DRAFT §3.2 | ISH-M05-006 (S:480, cột Nguồn có DRAFT §3.2 + DEC-143); R6 (R:79) | Khớp | — |
| 3 | DRAFT §3.3 | Topic/Tag → 2.1, ISH-M05-006.1 (S:481); Lớp/Khối → R5 (R:65, không ghi DRAFT §3.3); Personalized Feed → R6 (R:80) | Khớp (dấu vết của phần Lớp/Khối yếu: hàng R5 không ghi DRAFT §3.3; không lập finding vì nội dung hàng R5 bao được ý) | — |
| 4 | DRAFT §3.4 | ISH-M05-002 (S:443); R6 (R:79); Lớp/Khối → R5 (R:65) | Khớp | — |
| 5 | DRAFT §2.4 | Không có trong SR/routing; mục DRAFT của M03 | Khớp (không liên quan M05) | — |
| 6 | DRAFT §4.5 | ISH-M05-007 (S:496 ghi DRAFT §4.5); Tag → R7 (R:87) | Khớp | — |
| 7 | DRAFT §7.1 | R6 (R:80) qua DRAFT §3.3 | Khớp (M14) | — |
| 8 | DRAFT §7.2 | ISH-M05-008 chỉ ghi register (S:503); không có DRAFT §7.2 ở SR/routing/disposition | Lệch nguồn (thiếu dấu vết) | P1-05 |
| 9 | DRAFT §7.3, §7.4 | R5 M06 (R:56–58) | Khớp | — |
| 10 | DRAFT §8.1 | R5 M07 (R:64); Tag → R7 (R:87) | Khớp | — |
| 11 | DRAFT §9.5 | Không có; QA-243 ghi "không liên quan — M15" trong disposition | Khớp (module khác) | — |
| 12 | DRAFT §11.2 | ISH-M05-003.5 (S:191); ISH-M05-009 (S:516); R6 (R:78) | Khớp | — |
| 13 | DRAFT §11.5 | ISH-M05-005 (qua DEC-050/QA-017); R5 M13 (R:69) | Khớp | — |
| 14–15 | specs_general §3, §6 | 2.1; R6 (R:78) | Khớp | — |
| 16 | dev_priority §3 | 5.1 (S:99–112) | Khớp (chấm chi tiết thuộc P2, CL-C05) | — |
| 17 | module-registry L12 | ISH-M05-001…012; R1 (R:14) | Khớp | — |
| 18 | DEC-047, ISS-079, QA-101 | ISH-M05-001, 006.1, 006.8; R3 (R:38); R5 (R:56, R:59); R7 (R:89) | Khớp | — |
| 19 | DEC-048, DEC-140, ISS-080, ISS-207, QA-102, QA-267 | ISH-M05-001.1, 001.2, 001.4; R4 (R:45, R:50); R6 (R:75) | Khớp | — |
| 20 | DEC-049, DEC-143, ISS-083, ISS-211, QA-271 | ISH-M05-002.4…002.8 | Khớp | — |
| 21 | DEC-049, ISS-084, QA-107 (Topic) | ISH-M05-010, 010.4, 011; R1 (R:15) | Khớp | — |
| 22 | DEC-050, DEC-147, DEC-148, ISS-081, ISS-218…220, QA-103, QA-278…280 | ISH-M05-002.3, 003.1…003.14, 004.1; R3 (R:33–35); R4 (R:48); R6 (R:76) | Khớp | — |
| 23 | QA-104, QA-017 | ISH-M05-005.1…005.3; R1 (R:16); R5 (R:69) | Khớp | — |
| 24 | DEC-149, DEC-132, ISS-221, QA-281 | ISH-M05-004.5, 004.6; R3 (R:36); R5 (R:68); R6 (R:77) | Khớp | — |
| 25 | DEC-152 (1), ISS-225, QA-285 | ISH-M05-004.7 | Khớp | — |
| 26 | DEC-051, DEC-143, ISS-082, ISS-212, QA-105, QA-272 | ISH-M05-006.2…006.10; R1 (R:14) | Khớp | — |
| 27 | DEC-150 (2), DEC-152 (2), ISS-223, ISS-226, QA-283, QA-286 | ISH-M05-006.6, 006.13…006.15 | Khớp | — |
| 28 | DEC-051 (khủng hoảng), QA-107 (Tag) | ISH-M05-012.1…012.4, 012.9…012.11; R1; R3 (R:37); R5 (R:58, R:59) | Khớp | — |
| 29 | DEC-150 (1), ISS-222, QA-282 | ISH-M05-012.5, 012.6 | Khớp | — |
| 30 | DEC-144, ISS-213, QA-273 | ISH-M05-002.6, 002.9, 006.11, 006.12, 009 | Khớp | — |
| 31 | DEC-145, ISS-214, ISS-215, QA-274, QA-275 | ISH-M05-011.2 (loại khỏi danh mục), 011.3, 011.4; không có yêu cầu nào nói Topic nguồn không còn được xếp Trending hay theo dõi | Thiếu một phần | P1-01 |
| 32 | DEC-052, DEC-142, ISS-082, ISS-210, QA-106, QA-270 | ISH-M05-008, 008.1, 008.2, 008.8; R2 (R:25); R4 (R:47); R5 (R:60) | Khớp | — |
| 33 | DEC-146, ISS-216, ISS-217, QA-276, QA-277 | ISH-M05-008.3…008.7 | Khớp | — |
| 34 | DEC-153, ISS-227, QA-287 | ISH-M05-008.9…008.12 | Khớp | — |
| 35 | DEC-141, ISS-208, QA-268 | ISH-M05-007.1…007.4; R3 (R:39); R5 (R:64); R7 (R:87) | Khớp | — |
| 36 | ISS-209, QA-269 | R6 (R:78); R7 (R:88) | Khớp | — |
| 37 | QA-108 | R7 (R:86) | Khớp | — |
| 38 | DEC-151, ISS-224, QA-284 | 5.1; R4 (R:49); R5 (R:59) | Khớp | — |
| 40 | DEC-008, DEC-093, DEC-099 (1) | ISH-M05-004, 004.1; R5 M10 (R:66) | Khớp | — |
| 41 | DEC-099 (2), QA-175 | ISH-M05-004.2…004.4; R2 (R:27); R5 M13 (R:67) | Khớp | — |
| 42 | DEC-100, ISS-129, QA-178 | ISH-M05-003.8, 003.9; R2 (R:26) | Khớp (hàng R2 chứa câu hỏi mở — chuyển P3) | — |
| 43 | DEC-090, ISS-119, QA-160 | ISH-M05-010, 011, 012 (Phụ lục A); R5 M10 (R:66) | Khớp | — |
| 44–46 | DEC-096, DEC-133 và ISS/QA | R5 M13 (R:67); R1 (R:18) | Khớp | — |
| 47–48 | DEC-124, DEC-125, ISS-185, QA-226 | R5 M14 (R:60, R:61, R:63) | Khớp | — |
| 49 | DEC-126, QA-227 | ISH-M05-007.5; R5 (R:60) | Khớp | — |
| 50 | QA-011 | ISH-M05-001.3 (chỉ Topic, S:142); Khối lớp → R5 (R:65); phần "danh sách Tag" và "AI Classification trên post" không có chỗ đi | Thiếu một phần | P1-02 |
| 51 | QA-235, ISS-175 | R5 M14 "hiển thị" (R:62); xếp hạng Topic/Tag (cái quyết định mục nào "vào Trending") là của M05 | Sai chỗ | P1-03 |
| 52 | QA-236, ISS-176 | R5 M14 (R:62); hệ quả cho Topic/Tag đã nằm trong DEC-146 → ISH-M05-008.3 | Khớp | — |
| 53 | QA-237 | R5 M14 (R:60) | Khớp | — |
| 54–55 | QA-231, QA-228 | disposition "không liên quan" | Khớp | — |
| 56 | QA-043, ISS-051 | ISH-M05-007; R1 (R:17); R5 M07 (R:64) — kèm ghi chú DEC-065 chưa có sự kiện | Lệch nguồn (QA-043/DEC-141 ↔ DEC-065), chưa hỏi stakeholder | P1-06 |
| 57 | QA-033, ISS-046 | R6 (R:75) | Khớp | — |
| 58 | QA-034 | R5 (R:65) | Khớp | — |
| 59 | QA-017 | ISH-M05-003, 003.1, 005 | Khớp | — |
| 60 | DEC-053…060, QA-109/113/115, ISS-085…093 | R5 M06 (R:56–58); DEC-057, ISS-091 → disposition "không liên quan" | Khớp | — |
| 61 | QA-243, ISS-180 | disposition "không liên quan — M15" | Khớp | — |
| 62 | DEC-127 | disposition "không liên quan" (cửa sổ trượt, không theo ranh giới ngày); ISH-M05-008.8 = 168 giờ | Khớp | — |
| 63–64 | OPEN-006, OPEN-008, DEC-139, ISS-205, QA-265 | disposition "không liên quan"; 4.1 "Không có." | Khớp | — |
| 65 | glossary.md:14, :29; DEC-125 (decisions.md:695) | SR theo quyết định muộn hơn (DEC-048, QA-269, DEC-144, DEC-141) | Lệch nguồn trong register (văn bản cũ chưa đánh dấu) | P1-07 |
| — | KEYWORD không có dòng disposition (30 mục theo inventory P1, ví dụ ISS-168, QA-225) | Disposition chỉ có câu gộp "các mục KEYWORD còn lại … không liên quan" | Thiếu phân loại từng mục | P1-04 |

## C. Mâu thuẫn và lệch nguồn thấy được (P1.2)

- DRAFT §3.2 "Một Post có thể có nhiều Tag, không giới hạn số lượng." (`iShare_modules.md:134`) ↔ DEC-051 "Max 5 tags/post" (`decisions.md:301`) — đã xử lý: DEC-143, QA-272.
- DRAFT §3.4 sơ đồ một Topic (`iShare_modules.md:167`) ↔ DEC-049 "Min 1, max 3" (`decisions.md:284`) — đã xử lý: DEC-143, QA-271.
- DRAFT §11.2 "AI đề xuất … Tags" (`iShare_modules.md:586`) ↔ QA-269 — đã xử lý.
- DRAFT §4.5 Follow Tag (`iShare_modules.md:258`) ↔ DEC-141 — đã xử lý.
- DRAFT §7.2 "Có thể dựa trên: Views … Bookmarks" (`iShare_modules.md:335–340`) ↔ DEC-052 công thức chỉ có upvote, bình luận, thưởng bài mới (`decisions.md:308`) — chưa có dấu vết (P1-05).
- QA-043 "Topic (nhận noti khi có post mới trong topic)" (`qa-log.md:521`) và DEC-141 (`decisions.md:774`) ↔ DEC-065 bảng sự kiện thông báo không có sự kiện này (`decisions.md:375–390`) — chưa hỏi (P1-06).
- QA-033 "2 tầng" ↔ DEC-047/048 — đã xử lý: DEC-140 ghi rõ supersede.
- DEC-050 "<20 words" ↔ DEC-147 — đã đánh dấu `[Amended]`. DEC-132 ↔ DEC-149 — đã đánh dấu `[Amended]`.
- glossary.md:14 ("List to be finalized in BA"), glossary.md:29 ("Suggests Topic and Tags … User/Moderator reviews") và DEC-125 ("Follow targets established in M07") chưa cập nhật theo DEC-048, QA-269, DEC-144, DEC-141 (P1-07).
