# Ma trận độ phủ — ISH-AUD-M05-r2 · lượt P1
<!-- [Vietnamese Doc] -->

| Trường | Giá trị |
|---|---|
| Module | M05 — Topic & Tag |
| Vòng | 2 |
| Inventory | `audit-inventory-P1-M05-r2.md/.json` (OWNED 100, REFERENCING 21, KEYWORD 100, CROSS 42, DRAFT 30) |
| Chênh so với vòng 1 | OWNED 76 → 100: thêm 24 mục (DEC-154…DEC-159, ISS-228…ISS-236, QA-288…QA-296). REFERENCING 20 → 21 (thêm DEC-065, nay nhắc DEC-155). Tập OWNED đổi ⇒ chạy lại toàn bộ ma trận (vòng 2, điều kiện c) |
| Thời điểm lập phần A | Trước khi đọc thân SR và routing (chỉ đọc header: SR 0.2, 2026-10-05; RT 0.2, 2026-10-05) |

Ký hiệu cột **Mong đợi**: `SR` = yêu cầu trong ISH-SR-M05 (Phụ lục A); `R1`…`R7` = hàng routing; `Myy` = module khác (R5). Các mục ISS/QA chỉ là câu hỏi–trả lời dẫn tới một DEC được đặt cùng hàng với DEC đó (mỗi ID ghi rõ ở cột Nguồn).

## A. Mong đợi (lập từ nguồn, trước khi đọc SR)

### A.1 DRAFT

| Nguồn | Nội dung ngắn | Mong đợi | Lý do mong đợi |
|---|---|---|---|
| DRAFT §3.1 (`iShare_modules.md:126-131`) | Topic tổ chức lĩnh vực tri thức; danh sách "chưa cố định" | SR (danh mục Topic theo DEC-048) + R6/dấu vết (danh sách đã chốt) | DEC-048 chốt 11 Topic |
| DRAFT §3.2 (`:132-152`) | Một Post nhiều Tag, "không giới hạn số lượng" | SR (0–5 Tag) + R6 phần "không giới hạn" | DEC-143 ghi rõ register ghi đè DRAFT |
| DRAFT §3.3 (`:153-162`) | Lớp/Khối trên Post và Profile, dùng lọc và Personalized Feed | R5 (M03, M02, M14) | DEC-140: `grade_level` ngoài phạm vi M05 |
| DRAFT §3.4 (`:163-173`) | Post → một Topic/Category, Lớp/Khối, N Tags | SR (1–3 Topic) + R6 (một Topic) + R5 (Lớp/Khối) | DEC-143 |
| DRAFT §4.5 (`:247-264`) | Follow Post/User/Topic/Tag/Group; Follow kích hoạt notification | SR (theo dõi Topic) + R6/R7 (Tag, Group) + R5 (Post/User → module khác; thông báo → M07) | DEC-141, DEC-155 |
| DRAFT §7.1 (`:323-332`) | Feed Latest/Popular/Trending/Following/Personalized | R5 M14 | Hiển thị feed thuộc M14 |
| DRAFT §7.2 (`:333-342`) | Trending dựa trên Views, Stars, Comments, Bookmarks, Recency | SR (công thức theo DEC-052/142/158, ghi DRAFT §7.2 ở cột Nguồn) | DEC-158 ghi đè phần còn lại của DRAFT §7.2 |
| DRAFT §7.3, §7.4 (`:343-368`) | Tìm/lọc theo Topic, Tag | R5 M06/M14 | DEC-151: duyệt/lọc thuộc M14/M06 |
| DRAFT §8.1 (`:371-385`) | "Nội dung mới trong topic/tag/group đang follow" | R5 M07 | DEC-155 |
| DRAFT §11.2 (`:581-601`) | AI đề xuất Topic và Tags; User/Moderator review; user chỉnh trước publish | SR (gợi ý Topic; tác giả chỉnh; Mod/Admin đổi Topic) + R6 (gợi ý Tag, QA-269) | DEC-050, DEC-144, QA-269 |
| DRAFT §11.5 (`:630-658`) | Feedback loop đo accuracy/precision/recall | SR (ghi nhận phản hồi gợi ý Topic) + R5 M13 (đo chỉ số) | QA-017, DEC-050, DEC-157 |
| `iShare_dev_priority.md` §3 (`:36`, `:75`, `:83`, `:86`, `:99`) | Tag/Topic P0; AI Classification AI-P0; Follow P1; Trending P1; Feedback AI-P1 | 5.1 (mốc) | RULES §3 mục 5.1 |
| `iShare_specs_general.md` §3, §6 | Ba trục phân loại; AI gợi ý Topic/Tag | Như DRAFT §3, §11.2 | Trùng ý |
| module-registry L12 | Tóm tắt M05; "tags+post_tags tables" | 5.1 (Must) + R1 (bảng) | — |

### A.2 OWNED — Phase 5 (DEC-047…052, ISS-079…084, QA-101…108)

| Nguồn | Nội dung ngắn | Mong đợi | Lý do mong đợi |
|---|---|---|---|
| DEC-047, ISS-079, QA-101 | Topic: danh mục có cấu trúc, AI gợi ý + người dùng xác nhận, dùng lọc/duyệt, một tầng. Tag: #hashtag tự do, người dùng gõ, không danh sách cố định, không khoảng trắng | SR (Topic một tầng; Tag tự tạo; Tag không chứa khoảng trắng + từ chối) + R5 (lọc/duyệt → M14/M06) | "no spaces" là giới hạn ⇒ cần nhánh vi phạm |
| DEC-048, ISS-080, QA-102 | Danh sách 11 Topic | SR | Giá trị cụ thể |
| DEC-049, ISS-083, ISS-084 (phần Topic) | 1–3 Topic/bài; Mod/Admin đổi tên + gộp; không xóa; gộp chuyển bài sang đích | SR (mỗi cận + từ chối; đổi tên; gộp; từ chối xóa; chuyển bài) + R1 (post_topics) | — |
| DEC-050, ISS-081, QA-103, QA-104 | Nút gợi ý (không tự động); AI đọc tiêu đề + nội dung văn bản; tối đa 3, chọn sẵn; nội dung ngắn → không gợi ý; tác giả chỉnh tự do; nội dung đổi → gợi ý cũ, cảnh báo mềm, nút gợi ý lại, không chặn; phản hồi chỉ khi không cũ; tự chọn từ đầu → bỏ qua AI; AI tắt → chọn tay | SR (mỗi nhánh) + R3 (nút, chữ "content too short", cảnh báo) + R6 ("<20 words" bị DEC-147 thay) | — |
| DEC-051, ISS-082, ISS-084 (phần Tag), QA-105, QA-107 | Bảng tags/post_tags; tự tạo không duyệt; tối đa 5 Tag, 30 ký tự; Mod/Admin không sửa/gộp/xóa; khủng hoảng: vô hiệu hóa → ẩn khỏi autocomplete/trending/duyệt; bài cũ giữ liên kết nhưng ẩn chip; gõ lại tên bị vô hiệu → văn bản thường | SR (tự tạo; 5 + từ chối; 30 + từ chối; từ chối sửa/gộp/xóa; vô hiệu hóa; loại khỏi Trending; ẩn trên bài; không tạo Tag từ tên bị vô hiệu) + R1 (bảng, is_active) + R3 (chip) + R5 (autocomplete → M06; duyệt → M14/M06) | — |
| DEC-052, QA-106 | Cửa sổ trượt 7 ngày; tính lại 15–30 phút; công thức Σ(1 + 2×upvote + bình luận); mục Feed riêng (M14) | SR (cửa sổ, công thức) + R2 (chu kỳ, cache) + R5 M14 (mục Feed) | — |
| QA-108 | Bình luận không có Tag; bình luận thừa hưởng ngữ cảnh của bài | R4/R7 (không có hành vi kiểm chứng) | Câu hỏi đã đóng không tạo hành vi |

### A.3 OWNED — System Requirement (DEC-140…159, ISS-207…236, QA-267…296)

| Nguồn | Nội dung ngắn | Mong đợi | Lý do mong đợi |
|---|---|---|---|
| DEC-140, ISS-207, QA-267 | Topic một tầng, không Category; thay QA-033/ISS-046; `grade_level` thuộc M03/M02 | SR (một tầng) + R6 (QA-033/ISS-046) + R5 (M03/M02) | Tách theo câu |
| DEC-141, ISS-208, QA-268 | M05 sở hữu theo dõi Topic (nút, trạng thái, số người theo dõi); Tag không theo dõi được; dòng dev_priority không có thẩm quyền; thông báo bài mới thuộc M07 | SR (theo dõi, bỏ theo dõi, trạng thái, số người theo dõi) + R3 (nút) + R6/R7 (Tag, Group) + R5 M07 | — |
| DEC-142, ISS-210, QA-270 | Mọi bài được xét; chỉ đếm upvote/bình luận trong cửa sổ; +1 cho bài "created" trong cửa sổ; bài cũ không tương tác = 0 | SR | Công thức |
| DEC-143, ISS-211, ISS-212, QA-271, QA-272 | 1–3 Topic ghi đè DRAFT §3.4; tối đa 5 Tag ghi đè DRAFT §3.2; 0–5 Tag, không bắt buộc | SR + R6 (phía DRAFT) | — |
| DEC-144, ISS-213, QA-273 | Tác giả đổi Topic và Tag khi sửa bài; Mod/Admin đổi Topic của mọi bài; Mod/Admin không đổi Tag; giới hạn áp dụng mọi lần đổi | SR (quyền + từ chối) | — |
| DEC-145, ISS-214, ISS-215, QA-274, QA-275 | Topic nguồn sau gộp bị loại khỏi danh mục: không chọn, không gợi ý, không xếp Trending, không theo dõi được; bài đã chuyển; người theo dõi chuyển sang đích, theo dõi cả hai tính một lần | SR (đủ bốn hệ quả + chuyển người theo dõi + đếm một lần) | Vòng 1 AUD-M05-03 |
| DEC-146, ISS-216, ISS-217, QA-276, QA-277 | Chỉ bài đang công khai (PUBLISHED + NORMAL) và không thuộc Group Private; không loại theo trạng thái tài khoản tác giả; upvote vào chính bài; mọi bình luận gốc và trả lời; chỉ tương tác còn tồn tại | SR (mỗi điều kiện) + R1 (tên trường) | — |
| DEC-147, ISS-218, QA-278 | Từ chối gợi ý khi tiêu đề + nội dung < 10 tiếng (tách bằng khoảng trắng) | SR (ngưỡng + từ chối) | — |
| DEC-148, ISS-219, ISS-220, QA-279, QA-280 | Gợi ý thay lựa chọn hiện tại; gợi ý cũ khi đổi tiêu đề/nội dung; đổi tệp đính kèm không tính | SR | — |
| DEC-149, ISS-221, QA-281 | Bỏ Topic ngoài danh mục, giữ và chọn sẵn Topic hợp lệ; không còn Topic hợp lệ → thất bại, lỗi không chặn | SR + R3 (chữ thông báo) | — |
| DEC-150, ISS-222, ISS-223, QA-282, QA-283 | Mod/Admin mở lại Tag; Tag hiện lại trên bài và dùng lại được; 30 ký tự không tính "#" | SR | — |
| DEC-151, ISS-224, QA-284 | 12 tính năng; duyệt bài theo Topic/Tag thuộc M14/M06; mốc: phản hồi = AI-P1, thao tác Mod/Admin = P0 | 5.1 + R4 + R5 (M14/M06) | — |
| DEC-152, ISS-225, ISS-226, QA-285, QA-286 | Hơn 3 Topic hợp lệ → giữ 3 Topic đầu; chuẩn hóa tên Tag: bỏ khoảng trắng đầu/cuối, từ chối tên rỗng, mỗi chữ nhìn thấy tính một ký tự | SR | — |
| DEC-153, ISS-227, QA-287 | Xếp theo điểm giảm dần; hòa → nhiều bài được tính "created" trong cửa sổ hơn; vẫn hòa → tên A→Z | SR | — |
| DEC-154, ISS-228, ISS-231, ISS-232, QA-288, QA-291, QA-292 | (1) "Bài mới" = công khai lần đầu trong cửa sổ, dùng cho +1 và phá hòa; (2) bình luận đang bị ẩn không đếm, được khôi phục thì đếm lại; (3) so tên theo bảng chữ cái tiếng Việt, không phân biệt hoa–thường | SR (cả ba phần) | Trả lời AUD-M05-01, 14, 15 |
| DEC-155, ISS-229, QA-289 | Theo dõi Topic tạo thông báo in-app khi có bài mới trong Topic; thêm vào bảng DEC-065; M07 gửi và gộp | R5 M07 + SR chỉ ở mức mô tả (2.1/Lý do) | Trả lời AUD-M05-02; kết quả nhìn thấy thuộc M07 |
| DEC-156, ISS-230, QA-290 | Tối thiểu 1 Topic chỉ kiểm khi gửi bài và khi lưu thay đổi bài đã gửi; bản nháp lưu được khi chưa có Topic | SR | Trả lời AUD-M05-16 |
| DEC-157, ISS-233, QA-293 | Nhiều gợi ý còn mới → phản hồi chỉ so gợi ý gần nhất với lựa chọn cuối; một bản ghi mỗi lần gửi | SR | Trả lời AUD-M05-10 |
| DEC-158, ISS-234, QA-294 | Trending Topic/Tag (và Trending Post) thêm 1 × bookmark + 0,1 × người xem; người xem = người dùng đăng nhập khác nhau, khác tác giả, mở trang chi tiết bài trong cửa sổ, Guest không tính; bookmark = tạo trong cửa sổ, còn tồn tại, không tính của tác giả; ghi đè DRAFT §7.2; lưu từng lượt xem theo thời điểm (Phase 8); không theo dõi Guest | SR (hệ số, định nghĩa người xem, định nghĩa bookmark) + R5 M14 (Trending Post) + R1 (lưu lượt xem) + SR hoặc R1/R5 (không ghi nhận Guest) + dấu vết DRAFT §7.2 | Trả lời AUD-M05-18. Tách theo câu |
| DEC-159, ISS-236, QA-296 | Gộp chỉ giữa hai Topic khác nhau đều trong danh mục; nguồn/đích đã bị loại → từ chối, báo Mod/Admin Topic không tồn tại; nguồn trùng đích → từ chối; danh mục và bài giữ nguyên | SR (điều kiện chấp nhận + hai nhánh từ chối + giữ nguyên) + R3 (chữ thông báo) | Trả lời AUD-M05-13 |
| ISS-235, QA-295 | Đánh dấu [Amended] ở glossary và DEC-125, không xóa chữ cũ | R4 (việc register, không tạo hành vi) | Trả lời AUD-M05-21 |
| ISS-209, QA-269 | AI không gợi ý Tag | R6 (DRAFT §11.2 phần Tag) hoặc R7 | — |

### A.4 REFERENCING (21) và KEYWORD được chọn

| Nguồn | Nội dung ngắn | Mong đợi | Lý do mong đợi |
|---|---|---|---|
| DEC-008, DEC-093, QA-024 | Cờ AI; công tắc riêng "Topic suggestion (M05)"; AI tắt → chọn tay | SR (AI tắt → không gợi ý, chọn tay) + R5 M10 (công tắc) | — |
| DEC-099 | Lỗi tạm thời: 10 s, thử lại 1 lần; lỗi không chặn, không làm gì | SR (lỗi không chặn) + R2 (10 s, retry) | — |
| DEC-132 | Kiểm kết quả AI theo danh sách 11 Topic; lỗi không chặn; [Amended DEC-149] | SR + R3 (chữ thông báo) | — |
| DEC-090 | Mod dùng chung với Admin: sửa/gộp Topic, vô hiệu hóa Tag | SR (quyền Mod và Admin) | — |
| DEC-065 | Bảng sự kiện thông báo, thêm "New post in a followed Topic" (DEC-155) | R5 M07 | — |
| DEC-124 | Trending Post (M14), [Amended DEC-158] | R5 M14 | — |
| DEC-125 | Feed 4 tab, Trending 3 sub-view; [Amended DEC-141/155] | R5 M14 | — |
| ISS-171, ISS-185, QA-226 | Trending Post dùng công thức riêng; Topic/Tag giữ DEC-052 | R5 M14 / R6 (ISS-171 superseded) | — |
| QA-237, ISS-186, QA-240 | Feed không tự chèn; M14 không phụ thuộc M13 | R5 M14 / không liên quan | — |
| DEC-095 | Embedding (M13), "mirrors is_stale pattern from M05" | Không liên quan | Chỉ so sánh mẫu |
| DEC-139, ISS-205, QA-265 | Cách viết SR | Không liên quan (quy trình) | — |
| OPEN-006, OPEN-008 | SEO; Privacy chưa định nghĩa | Không liên quan; 4.1 "Không có." | — |
| KEYWORD QA-011 | Guest: xem danh sách Topic / Tag / Khối lớp; xem AI Classification trên post | SR (Guest xem Topic, Tag) hoặc R5 kèm module sở hữu; Khối lớp → R5; phân loại trên bài → SR/R5 | Vòng 1 AUD-M05-04 |
| KEYWORD QA-017 | Gợi ý Topic không tự gán; lựa chọn cuối là phản hồi; Tag do người dùng quyết | SR (phản hồi) + R5 M13 | — |
| KEYWORD QA-043, ISS-051 | Follow User/Topic/Post, Topic → thông báo khi có bài mới | SR (theo dõi Topic) + R5 M07; nay thống nhất với DEC-065 qua DEC-155 | Vòng 1 AUD-M05-02 |
| KEYWORD DEC-100 | Nút gợi ý Topic giới hạn 10 yêu cầu/phút/người dùng | SR (giới hạn + từ chối) + R2 (cơ chế đếm) | Giới hạn kiểm chứng được |
| KEYWORD DEC-096, DEC-133, ISS-194/195, QA-253/254 | Mô hình GPT-4o-mini; ghi log thô | R5 M13 / R1 | — |
| KEYWORD QA-235, ISS-175 | Không đặt ngưỡng tối thiểu để vào Trending (MS1) | SR hoặc OP về chủ sở hữu (phần Topic/Tag) + R5 M14 (Trending Post) | Vòng 1 AUD-M05-05 |
| KEYWORD QA-236, ISS-176 | Không loại bài theo trạng thái người dùng | SR (qua DEC-146) | — |
| KEYWORD DEC-126, QA-227 | Guest xem cả tab Trending (3 sub-view) | R5 M14 | — |
| KEYWORD QA-231, ISS-172 | Trending Post không lọc theo Topic | R5 M14 | — |
| KEYWORD QA-033, ISS-046, QA-034 | 2 tầng Category→Topic; grade_level | R6 (→ DEC-140) + R5 M02/M03 | — |
| KEYWORD DEC-053…060, ISS-085…093, QA-109…115 | Tìm kiếm Topic/Tag, autocomplete | R5 M06 / không liên quan | — |
| KEYWORD QA-243, ISS-180 | Thống kê phân bố Post theo Topic | R5 M15 | — |
| KEYWORD QA-127 | Bookmark chỉ để lưu, không đăng ký nhận tin | Không liên quan (hoặc nguồn phụ cho bookmark) | — |
| KEYWORD còn lại (≈70) | Khớp từ khóa chung (follow người dùng, category của moderation, gộp chat…) | Không liên quan / disposition | Lấy mẫu có chủ đích ở P1.5 |

### A.5 Mâu thuẫn và lệch nguồn thấy khi lập phần A

| # | Lệch | Bằng chứng | Xử lý theo RULES |
|---|---|---|---|
| L1 | DRAFT §3.2 "không giới hạn số lượng" ↔ DEC-051 tối đa 5 | `iShare_modules.md:134`; DEC-143 (`decisions.md:785`) ghi rõ ghi đè | §7.5: theo register, ghi cả hai nguồn |
| L2 | DRAFT §3.4 một Topic ↔ DEC-049 1–3 | DEC-143 ghi rõ | Như L1 |
| L3 | DRAFT §7.2 (Views, Bookmarks, Recency) ↔ DEC-052 | DEC-158 (`decisions.md:845`) "Overrides the remaining Views/Bookmarks part of DRAFT §7.2" | Nay register ghi rõ; SR phải ghi DRAFT §7.2 + DEC-158 |
| L4 | DRAFT §4.5, dev_priority: Follow Tag, Group ↔ QA-043/DEC-141 | DEC-141 ghi rõ không có thẩm quyền | R6 |
| L5 | QA-043 (Topic → thông báo) ↔ DEC-065 (không có sự kiện) | Đã giải bởi DEC-155; DEC-065 có hàng "[Added 2026-10-05 — DEC-155]" (`decisions.md:392`) | Không còn mâu thuẫn |
| L6 | glossary "List to be finalized", "Suggests Topic and Tags" ↔ DEC-048, QA-269 | Đã đánh dấu `[Amended 2026-10-05 …]` (`glossary.md:14`, `:29`) theo QA-295 | Không còn mâu thuẫn |
| L7 | DEC-124 "DEC-052 … stays unchanged" ↔ DEC-158 sửa DEC-052 | DEC-124 đã mang nhãn "[Amended 2026-10-05 — DEC-158 …]" (`decisions.md:694`) nhưng câu "DEC-052 (Trending Topic/Tag, M05) stays unchanged" vẫn nguyên | Chỉ là chữ cũ được giữ theo cách đánh dấu; thuộc M14 |
| L8 | DEC-158 áp "within the rolling 7-day window" cho cả Trending Post trong khi DEC-124 dùng cửa sổ 28 ngày có suy giảm | `decisions.md:845` ↔ `decisions.md:694` | Thuộc M14 (R5); không phải lỗi của SR M05 — ghi chú chuyển lượt khác |

## B. Thực tế (sau khi đọc SR 0.2 và routing 0.2) và kết quả

Ký hiệu: `S:` = dòng của `ISH-SR-M05.md`; `R:` = dòng của `ISH-RT-M05.md`. Cả hai tệp trùng hoàn toàn với `snapshot-ISH-SR-M05-v0.2.md` và `snapshot-ISH-RT-M05-v0.2.md` (`diff -q` không báo khác biệt).

| Nguồn | Mong đợi | Thực tế (SR / routing) | Kết quả | Finding |
|---|---|---|---|---|
| DRAFT §3.1 | SR + dấu vết | 001.1 ghi DRAFT §3.1 + DEC-048 (S:465) | Khớp | — |
| DRAFT §3.2 | SR 0–5 + R6 | 006 (S:509) ghi DRAFT §3.2 + DEC-143; R6 (R:85) | Khớp | — |
| DRAFT §3.3 | R5 M03/M02 | R5 (R:70, ghi DEC-140); R6 (R:86, ghi DRAFT §3.3) | Khớp | — |
| DRAFT §3.4 | SR 1–3 + R6 + R5 | 002 (S:470) ghi DRAFT §3.4; R6 (R:85); R5 (R:70) | Khớp | — |
| DRAFT §4.5 | SR + R7 + R5 M07 | 007 (S:526) ghi DRAFT §4.5; R7 Tag (R:94); R5 M07 (R:69) | Khớp | — |
| DRAFT §7.1 | R5 M14 / R6 | R6 (R:86); R5 M14 (R:65, R:68) | Khớp | — |
| DRAFT §7.2 | SR + dấu vết | 008 (S:533), 008.13 (S:546) ghi DRAFT §7.2 + DEC-158; R6 (R:87) | Khớp | — (AUD-M05-18 đã sửa) |
| DRAFT §7.3, §7.4 | R5 M06/M14 | R5 (R:61–R:64) theo ID register; không ghi DRAFT §7.3/§7.4 | Khớp (dấu vết qua register) | — |
| DRAFT §8.1 | R5 M07 | R5 (R:69) theo DEC-155 | Khớp | — |
| DRAFT §11.2 | SR + R6 | 003, 009 (S:553 ghi DRAFT §11.2); R6 (R:84) | Khớp | — |
| DRAFT §11.5 | SR + R5 M13 | 005 (qua QA-017, S:481, S:504); R5 M13 (R:74) | Khớp (không ghi DRAFT §11.5) | — |
| dev_priority, module-registry L12 | 5.1 + R1 | 5.1 (S:105–S:118); R1 (R:14) | Khớp | — |
| DEC-047, ISS-079, QA-101 | SR + R3 + R5 + R7 | 001, 001.2, 002.2, 006.1, 006.8; R3 (R:40); R5 (R:61, R:64); R7 (R:96) | Khớp | — |
| DEC-048, ISS-080, QA-102 | SR | 001.1, 001.4; R4 (R:48) | Khớp | — |
| DEC-049, ISS-083, ISS-084 | SR + R1 | 001.5, 002, 002.5…002.8, 010, 011, 011.1; R1 (R:15) | Khớp | — |
| DEC-050, ISS-081, QA-103, QA-104 | SR + R3 + R6 | 002.3, 003.1…003.14, 004.1, 005…005.3; R1 (R:16); R3 (R:35–R:37); R6 (R:82) | Khớp | — |
| DEC-051, ISS-082, QA-105, QA-107 | SR + R1 + R3 + R5 | 006.2, 006.4…006.7, 006.9, 012.1…012.4, 012.9…012.11; R1 (R:14); R3 (R:39); R4 (R:49); R5 (R:63, R:64) | Khớp | — |
| DEC-052, QA-106 | SR + R2 + R5 | 008, 008.8; R2 (R:27); R4 (R:50); R5 (R:65) | Khớp | P1-03 (QA-106 chưa đánh dấu, ở register) |
| QA-108 | R4/R7 | R7 (R:93) | Khớp | — |
| DEC-140, ISS-207, QA-267 | SR + R6 + R5 | 001.2; R4 (R:53); R5 (R:70); R6 (R:81) | Khớp | — |
| DEC-141, ISS-208, QA-268 | SR + R3 + R5 + R7 | 007.1…007.4, 007.6; R3 (R:41); R5 (R:69); R7 (R:94) | Khớp | — |
| DEC-142, ISS-210, QA-270 | SR | 008.1, 008.2, 008.13 | Khớp | — |
| DEC-143, ISS-211, ISS-212, QA-271, QA-272 | SR + R6 | 002, 006, 006.3; R6 (R:85) | Khớp | — |
| DEC-144, ISS-213, QA-273 | SR | 002.6, 002.9, 006.11, 006.12, 009, 009.1, 009.2 | Khớp | — |
| DEC-145, ISS-214, ISS-215, QA-274, QA-275 | SR đủ bốn hệ quả + người theo dõi | 002.2 (chọn), 004.5 (gợi ý), 011.6 (S:411, Trending), 011.7 (S:412, theo dõi), 011.2…011.4; 5.2 (S:131, S:132) | Khớp | — (AUD-M05-03 phần CL-A10 đã sửa) |
| DEC-146, ISS-216, ISS-217, QA-276, QA-277 | SR | 2.1 (S:37, S:38), 008.3…008.7 | Khớp | — |
| DEC-147, ISS-218, QA-278 | SR | 003.6, 003.7; R3 (R:36); R4 (R:51); R6 (R:82) | Khớp | — |
| DEC-148, ISS-219, ISS-220, QA-279, QA-280 | SR | 003.4, 003.10, 003.11 | Khớp | — |
| DEC-149, ISS-221, QA-281 | SR + R3 | 004.5, 004.6; R3 (R:38); R6 (R:83) | Khớp | — |
| DEC-150, ISS-222, ISS-223, QA-282, QA-283 | SR | 006.6, 012.5, 012.6, 012.8; R1 (R:19) | Khớp | — |
| DEC-151, ISS-224, QA-284 | 5.1 + R4 + R5 | 5.1; R4 (R:52); R5 (R:64) | Khớp | — |
| DEC-152, ISS-225, ISS-226, QA-285, QA-286 | SR | 004.7, 006.13…006.15 | Khớp | — |
| DEC-153, ISS-227, QA-287 | SR | 008.9…008.12 | Khớp | — |
| DEC-154, ISS-228, ISS-231, ISS-232, QA-288, QA-291, QA-292 | SR (ba phần) | 2.1 (S:39, S:62); 008.1, 008.2, 008.11, 008.12, 008.17; R1 (R:21) | Khớp | — |
| DEC-155, ISS-229, QA-289 | R5 M07 + mô tả | R5 M07 (R:69); 2.1 (S:54); Lý do 5.9 (S:302); Phụ lục A 007 (S:526) | Khớp | — (AUD-M05-02 đã giải bởi DEC-155) |
| DEC-156, ISS-230, QA-290 | SR | 002 (S:162), 002.5, 002.6, 002.11 | Khớp | — |
| DEC-157, ISS-233, QA-293 | SR | 005.1, 005.4 | Khớp | — |
| DEC-158, ISS-234, QA-294 | SR + R5 M14 + R1 + dấu vết | 008.13…008.16; R1 (R:20); R5 M14 (R:66); R5 M03 (R:75); R6 (R:87) | Khớp | P1-02 (chủ sở hữu ở R:75 không có nguồn) |
| DEC-159, ISS-236, QA-296 | SR + R3 | 011.8…011.10; R3 (R:42) | Khớp | — |
| ISS-235, QA-295 | R4 | R4 (R:54) | Khớp | — |
| ISS-209, QA-269 | R6/R7 | R6 (R:84); R7 (R:95) | Khớp | — |
| REF DEC-008, DEC-093, QA-024 | SR + R5 M10 | 004, 004.1; R5 (R:71); QA-024 ở disposition (không liên quan) | Khớp | — |
| REF DEC-099 | SR + R2 | 004.2…004.4; R2 (R:29); R5 (R:72) | Khớp | — |
| REF DEC-132 | SR + R3 | 004.5, 004.6; R3 (R:38); R5 (R:73); R6 (R:83) | Khớp | — |
| REF DEC-090 | SR | 010, 011, 012 (Phụ lục A); R5 (R:71) | Khớp | — |
| REF DEC-065 | R5 M07 | R5 (R:69) | Khớp | — |
| REF DEC-124, DEC-125, ISS-185, QA-226, QA-237 | R5 M14 | R5 (R:65, R:66, R:68) | Khớp | — |
| REF ISS-171, ISS-186, QA-240, DEC-095, DEC-139, ISS-205, QA-265, OPEN-006, OPEN-008 | Không liên quan | disposition (dòng 52–67) | Khớp | — |
| KEYWORD QA-011 | SR/R5 | Topic → 001.3 (S:152); Tag trên bài → 006.16; Topic trên bài → 002.10; danh sách Tag → R5 M14/M06 (R:64); Khối lớp → R5 (R:70); chủ sở hữu hiển thị → OP-M05-12 | Khớp | P1-02 (chủ sở hữu "danh sách Tag" ở R:64); P1-01 (lý do cũ ở disposition:73) — AUD-M05-04 đã sửa |
| KEYWORD QA-017, QA-043, ISS-051 | SR + R5 | 003, 005, 007; R1 (R:17); R5 (R:69, R:74) | Khớp | — |
| KEYWORD DEC-100, ISS-129, QA-178 | SR + R2 | 003.8, 003.9; R2 (R:28) | Khớp | — |
| KEYWORD DEC-096, DEC-133, ISS-125, ISS-194, ISS-195, QA-169, QA-253, QA-254 | R5 M13 / R1 | R1 (R:18); R5 (R:72, R:73) | Khớp | — |
| KEYWORD QA-235, ISS-175 | SR/OP + R5 | 008.18, 008.19 (S:348, S:349); R4 (R:55); R5 (R:67) | Khớp | — (AUD-M05-05 đã sửa) ; P1-01 (lý do cũ ở disposition:94) |
| KEYWORD QA-236, ISS-176 | SR qua DEC-146 | 008.3 (Phụ lục A S:536); R5 (R:67) | Khớp | — |
| KEYWORD DEC-126, QA-227, ISS-166 | R5 M14 + SR (Guest không theo dõi) | 007.5; R5 (R:65) | Khớp | — |
| KEYWORD QA-033, ISS-046, QA-034 | R6 + R5 | R6 (R:81); R5 (R:70) | Khớp | — |
| KEYWORD DEC-053…060, ISS-085…093, QA-109…115 | R5 M06 / không liên quan | R5 (R:61–R:63); DEC-057, ISS-091 ở disposition | Khớp | — |
| KEYWORD QA-231, ISS-172, QA-243, ISS-180, QA-127 | Không liên quan / module khác | disposition (dòng 93, 96, 127) | Khớp | — |
| KEYWORD còn lại của inventory Author (108 mục) | Mỗi mục một dòng disposition | 26 mục không có dòng nào (chỉ câu gộp ở disposition:69) | Thiếu phân loại | P1-01 |
| CROSS ISS-189…206, QA-248…266 (bản ISS/QA của các DEC cross-cutting) | Một dòng disposition | Chỉ DEC tương ứng có dòng (disposition:129, :130) | Thiếu phân loại (cùng nguyên nhân) | P1-01 |

### B.1 Kết quả tổng

- 100/100 mục OWNED có chỗ đi (Phụ lục A hoặc routing); không có mục "Thiếu" hay "Sai chỗ".
- Mọi mục OWNED mới của vòng 2 (DEC-154…159, ISS-228…236, QA-288…296) có chỗ đi đúng mong đợi.
- 21/21 mục REFERENCING đã phân loại.
- Lệch nguồn ở phần A.5: L1–L4 xử lý đúng RULES §7.5; L5, L6 đã được register giải; L7, L8 thuộc M14 (ghi ở "Chuyển lượt khác" của tệp lượt).
