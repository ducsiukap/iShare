# Routing — ISH-RT-M05 Topic & Tag
<!-- [Vietnamese Doc] -->

| Mã tài liệu | ISH-RT-M05 |
|---|---|
| Liên kết SR | ISH-SR-M05 |
| Phiên bản | 0.6 |
| Ngày | 2026-10-05 |

## R1. Mô hình dữ liệu (Phase 8)

| Nguồn | Nội dung | Ghi chú |
|---|---|---|
| DEC-051 | Tag lưu ở bảng riêng (mã, tên duy nhất đã chuẩn hóa chữ thường, thời điểm tạo, không lưu người tạo) và bảng nối bài viết–Tag; cờ hoạt động/vô hiệu hóa của Tag | Hành vi tương ứng ở ISH-M05-006, ISH-M05-012 |
| DEC-049 | Quan hệ bài viết–Topic là bảng nối; gộp Topic chuyển các dòng nối từ Topic nguồn sang Topic đích | Hành vi ở ISH-M05-011 |
| DEC-050, QA-104 | Trạng thái "gợi ý cũ" được lưu thành cờ trên bản nháp gợi ý của bài viết | Hành vi ở ISH-M05-003.10 |
| QA-043 | Quan hệ theo dõi lưu người theo dõi, loại đối tượng (user, topic, post) và mã đối tượng | Hành vi theo dõi Topic ở ISH-M05-007 |
| DEC-133, ISS-195, QA-254 | Mỗi lần gọi AI gợi ý Topic lưu phản hồi thô vào nhật ký quyết định AI, gắn với bài viết | Thuộc M13; ghi ở đây vì áp dụng cho gợi ý Topic |
| DEC-150 | Mở lại Tag là đổi cờ hoạt động, liên kết bài viết–Tag không đổi | Hành vi ở ISH-M05-012.5 |
| DEC-158, QA-294 | Lưu từng lượt mở trang chi tiết bài viết của người dùng đã đăng nhập (người xem, bài viết, thời điểm); lưu thời điểm tạo bookmark | Phục vụ ISH-M05-008.14, ISH-M05-008.16; không lưu lượt xem của Guest |
| DEC-154, QA-288 | Lưu thời điểm bài viết trở thành công khai lần đầu | Phục vụ ISH-M05-008.1, ISH-M05-008.11 |

## R2. Yêu cầu phi chức năng (Phase 7)

| Nguồn | Nội dung | Ghi chú |
|---|---|---|
| DEC-052, QA-106 | Điểm Trending Topic và Tag được tính lại định kỳ mỗi 15–30 phút từ dữ liệu đã lưu tạm, không truy vấn trực tiếp mỗi lần xem | Độ trễ cập nhật bảng xếp hạng là chỉ tiêu Phase 7 |
| DEC-100, ISS-129, QA-178 | Cửa sổ đếm của giới hạn 10 yêu cầu gợi ý Topic mỗi phút (cửa sổ trượt hay theo phút lịch) | Giá trị 10/phút ở ISH-M05-003.8; việc yêu cầu bị từ chối vì văn bản ngắn không bị tính là hệ quả người dùng thấy, đã thành yêu cầu ISH-M05-003.16 (DEC-167) |
| DEC-099, QA-175 | Gợi ý Topic chờ tối đa 10 giây, thử lại đúng 1 lần sau 2 giây trước khi coi là không trả về kết quả | Hành vi khi thất bại ở ISH-M05-004.2, ISH-M05-004.3, ISH-M05-004.4 |

## R3. HMI và thiết kế giao diện

| Nguồn | Nội dung | Ghi chú |
|---|---|---|
| DEC-050 | Nút "Gợi ý topic"; Topic gợi ý hiển thị dạng ô đã tick sẵn; người dùng chọn Topic từ danh sách thả xuống | |
| DEC-050, DEC-147 | Văn bản thông báo nội dung quá ngắn ("content too short") | Hành vi ở ISH-M05-003.7 |
| DEC-050, QA-104 | Hình thức cảnh báo nhẹ khi gợi ý cũ và nút gợi ý lại | Hành vi ở ISH-M05-003.12, ISH-M05-003.13 |
| DEC-132, QA-253, DEC-099 | Văn bản lỗi "Không thể gợi ý chủ đề lúc này, vui lòng chọn thủ công", hiển thị không chặn thao tác | Hành vi ở ISH-M05-004.2 |
| DEC-051, QA-107 | Tên Tag bị vô hiệu hóa khi gõ lại được hiển thị dạng văn bản thường, không thành chip Tag; chip Tag bị ẩn trên bài cũ | Hành vi ở ISH-M05-012.1, ISH-M05-012.4 |
| DEC-047, QA-101 | Tag hiển thị dạng #hashtag | |
| DEC-141, QA-268 | Nút Theo dõi / Bỏ theo dõi Topic và vị trí hiển thị số người theo dõi | Hành vi ở ISH-M05-007 |
| DEC-159, QA-296, DEC-165, QA-304 | Văn bản thông báo "Topic không tồn tại" khi gộp hoặc đổi tên Topic đã bị loại; thông báo khi gộp Topic vào chính nó | Hành vi ở ISH-M05-011.9, ISH-M05-011.10, ISH-M05-010.6 |

## R4. Ghi chú quy trình và phạm vi (không phải yêu cầu hệ thống)

| Nguồn | Nội dung | Ghi chú |
|---|---|---|
| QA-102 | 11 Topic được nhóm theo chương trình giáo dục 2018 cùng các nhóm phi học thuật | Lý do chọn danh sách |
| DEC-051, QA-107 | "Tình huống khẩn cấp" để vô hiệu hóa Tag do Mod/Admin tự đánh giá, hệ thống không kiểm điều kiện này | |
| DEC-052 | Cửa sổ Trending trượt theo thời điểm hiện tại, khác với tuần lịch cố định của Leaderboard | Lý do thiết kế |
| DEC-147, QA-278 | Giữ ngưỡng tối thiểu (không bỏ) vì Topic gợi ý được chọn sẵn, văn bản quá ngắn dễ gắn sai Topic | Lý do thiết kế |
| DEC-151, QA-284, ISS-224 | Khung 12 tính năng của SR M05 và mốc triển khai được stakeholder duyệt | Mốc ghi ở mục 5.1 của SR |
| DEC-140, ISS-207 | Xác nhận Topic một tầng cho SR M05 | Hành vi ở ISH-M05-001.2 |
| ISS-235, QA-295, ISS-242, QA-302 | Đánh dấu [Amended] các câu cũ ở glossary (Topic, AI Classification), DEC-125 (QA-295) và QA-106, QA-226, ISS-171 theo DEC-158 (QA-302) | Việc sửa register, không tạo hành vi |
| QA-235 | Câu trả lời "không đặt ngưỡng" là tạm thời (provisional), có thể xem lại khi dữ liệu đủ lớn | Hành vi hiện tại ở ISH-M05-008.18, ISH-M05-008.19 |
| DEC-169, ISS-254, QA-314 | Việc hiển thị Topic và Tag trên trang bài viết do M05 sở hữu; M03 (trang bài viết) tham chiếu, không viết lại | Hành vi ở ISH-M05-002.10, ISH-M05-006.16 |

## R5. Thuộc module khác

| Nguồn | Nội dung | Module và ID sở hữu |
|---|---|---|
| DEC-047, DEC-056, ISS-088, QA-113 | Lọc kết quả tìm bài viết theo Topic và theo Tag | M06 — chưa có SR, ghi nguồn DEC-056 |
| DEC-053, DEC-054, DEC-060, ISS-085, ISS-086, ISS-093, QA-109 | Tìm kiếm thực thể Topic và Tag (khớp chính xác hoặc tiền tố), hiển thị bổ sung trong trang kết quả | M06 — chưa có SR, ghi nguồn DEC-053 |
| DEC-051, DEC-058, ISS-090, QA-115 | Gợi ý tự hoàn thành tên Topic và Tag; Tag bị vô hiệu hóa không xuất hiện trong gợi ý tự hoàn thành | M06 — chưa có SR, ghi nguồn DEC-058, DEC-051 |
| DEC-047, DEC-051, DEC-151, QA-284, QA-011, DEC-163, ISS-241, QA-301 | Duyệt danh sách bài viết theo một Topic hoặc một Tag; "danh sách Tag" cho Guest của QA-011 được đáp ứng bởi Trending Tag và duyệt theo Tag (DEC-163); Tag bị vô hiệu hóa không duyệt được | M14 hoặc M06 — chưa có SR, ghi nguồn DEC-151, DEC-163 |
| DEC-052, DEC-125, DEC-126, ISS-166, QA-227, QA-237 | Hiển thị bảng xếp hạng Trending Topic và Trending Tag thành hai mục con của tab Trending trong Feed; Guest xem được; tự làm mới theo chu kỳ tính lại | M14 — chưa có SR, ghi nguồn DEC-125 |
| DEC-124, ISS-185, QA-226, DEC-158, QA-294 | Trending Post dùng công thức suy giảm riêng; phần điểm gốc thêm bookmark (1) và người xem (0,1) như Trending Topic/Tag | M14 — chưa có SR, ghi nguồn DEC-124, DEC-158 |
| QA-235, ISS-175, QA-236, ISS-176 | Phần Trending Post: không đặt ngưỡng tối thiểu để bài vào Trending Post; không loại bài của người dùng BANNED hoặc cảnh cáo nặng. Phần Trending Topic/Tag nằm ở ISH-M05-008.3, ISH-M05-008.18, ISH-M05-008.19 | M14 — chưa có SR, ghi nguồn QA-235, QA-236 |
| DEC-125, QA-043 | Tab Following hiển thị bài mới từ các Topic người dùng đang theo dõi | M14 — chưa có SR, ghi nguồn DEC-125 |
| DEC-141, QA-043, ISS-051, DEC-065, QA-123, DEC-155, ISS-229, QA-289 | Thông báo in-app khi có bài mới trong Topic đang theo dõi; sự kiện đã thêm vào DEC-065 theo DEC-155; quy tắc gộp thông báo do M07 quyết | M07 — chưa có SR, ghi nguồn DEC-155 |
| DEC-168, ISS-250, QA-310, DEC-065 | Khi Mod hoặc Admin đổi Topic của một bài viết do người khác viết, tác giả không nhận thông báo về thay đổi đó (sự kiện không có trong danh sách sự kiện thông báo DEC-065) | M07 — chưa có SR, ghi nguồn DEC-168, DEC-065 |
| DEC-140, QA-034, QA-011 | Lớp/Khối trên bài viết và trên hồ sơ người dùng; danh sách Khối lớp cho Guest | M03 (F-POST-09), M02 — chưa có SR, ghi nguồn DEC-140 |
| DEC-008, DEC-093, ISS-122, QA-165, DEC-090, ISS-119, QA-160 | Công tắc AI chung và công tắc gợi ý Topic trong cấu hình hệ thống; phân chia quyền Admin và Mod | M10 — chưa có SR, ghi nguồn DEC-093, DEC-090 |
| DEC-099, QA-175, DEC-096, ISS-125, QA-169 | Gọi dịch vụ AI gợi ý Topic: mô hình, thời gian chờ, thử lại | M13 — chưa có SR, ghi nguồn DEC-099, DEC-096 |
| DEC-132, ISS-194, QA-253 | Kiểm kết quả AI theo danh mục Topic ở tầng AI | M13 — chưa có SR, ghi nguồn DEC-132; hành vi người dùng thấy ở ISH-M05-004.5, ISH-M05-004.6 |
| QA-017, DEC-050 | Đo độ chính xác của gợi ý Topic từ phản hồi đã ghi nhận (vòng đánh giá AI) | M13 — chưa có SR, ghi nguồn QA-017; ghi nhận phản hồi ở ISH-M05-005 |
| DEC-158, QA-294, DEC-163, ISS-240, QA-300 | Ghi nhận lượt mở trang chi tiết bài viết của người dùng đã đăng nhập | M03 — chưa có SR, ghi nguồn DEC-163; cách đếm người xem ở ISH-M05-008.14 |

## R6. Đã bị thay thế

| Nguồn | Bị thay bởi | Ghi chú |
|---|---|---|
| QA-033, ISS-046 | DEC-140 | Phân loại 2 tầng Category → Topic được thay bằng Topic một tầng |
| DEC-050 | DEC-147 | Ngưỡng "<20 words" thay bằng 10 tiếng trên tiêu đề + nội dung; phần còn lại của DEC-050 vẫn hiệu lực |
| DEC-132 | DEC-149 | Kết quả có một phần Topic không hợp lệ: bỏ phần không hợp lệ thay vì coi cả lần gợi ý thất bại |
| DRAFT §11.2 | QA-269, ISS-209 | DRAFT §11.2 nêu AI gợi ý cả Tag và Moderator xem lại; QA-269 xác nhận Tag không có gợi ý AI; phần Moderator xem lại Topic thay bằng DEC-144 |
| DRAFT §3.2, DRAFT §3.4 | DEC-143 | Tag không giới hạn (§3.2) và một Topic mỗi bài (§3.4) được thay bằng giới hạn 0–5 Tag và 1–3 Topic của register |
| DRAFT §3.3, DRAFT §7.1 | DEC-125 | Personalized Feed ưu tiên Lớp/Khối (§3.3 nhắc, §7.1 mô tả) được thay bằng Feed 4 tab không có tab cá nhân hóa |
| DRAFT §7.2 | DEC-052, DEC-142, DEC-158 | Danh sách tín hiệu "có thể" (Views, Stars, Comments, Bookmarks, Recency) được chốt thành công thức: upvote, bình luận, bookmark, người xem và thưởng bài mới (ISH-M05-008.13) |

## R7. Không đưa vào SR

| Nguồn | Nội dung | Lý do |
|---|---|---|
| QA-108 | Bình luận không gắn Tag | Stakeholder loại khỏi phạm vi: bình luận theo ngữ cảnh Topic/Tag của bài viết |
| DEC-141, QA-268 | Theo dõi Tag | Stakeholder loại: Tag không phải đối tượng theo dõi |
| ISS-209, QA-269 | AI gợi ý Tag | Stakeholder loại: Tag hoàn toàn tự do |
| DEC-047 | Topic nhiều tầng | Hoãn ("nested deferred"), chưa chốt cho giai đoạn này |
