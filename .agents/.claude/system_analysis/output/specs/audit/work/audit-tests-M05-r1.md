# Ca kiểm độc lập — ISH-AUD-M05-r1 · lượt P3
<!-- [Vietnamese Doc] -->

| Trường | Giá trị |
|---|---|
| Module | M05 — Topic & Tag |
| Vòng | 1 |
| Lượt | P3 |
| Nguồn xác định | DRAFT `iShare_modules.md` §3 (dòng 124–172), §4.5, §7.1, §7.2, §11.2, §11.5; OWNED: DEC-047…052, DEC-140…153, ISS-079…084, ISS-207…227, QA-101…108, QA-267…287; REFERENCING dùng làm nguồn liên quan: DEC-008, DEC-031, DEC-033, DEC-090, DEC-093, DEC-099, DEC-100, DEC-126, DEC-132, QA-011, QA-043, QA-235, QA-236 |
| Inventory của lượt | `audit-inventory-P3-M05-r1.md/.json` (OWNED 76, REFERENCING 20) |
| Thứ tự làm | Bảng ca (cột 1–7) và bảng quét khung hành vi (cột 1–4) được dựng **trước khi** mở nội dung SR/routing; các cột "ID yêu cầu SR", "SR xác định?", "Then theo ca kiểm của Author", "Đối chiếu" và "SR", "Selfcheck", "Kết luận" điền ở P3.3–P3.4 |

Quy ước thời gian trong ca: `T` = thời điểm tính lại điểm Trending; "T−3n" = 3 ngày trước `T`.

## 1. Bảng ca kiểm (P3.2)

| ID ca | Nguồn | Loại | Given | When | Then theo nguồn | Nguồn xác định? | ID yêu cầu SR | SR xác định? | Then theo ca kiểm của Author | Đối chiếu |
|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | DEC-048, DEC-140 | Thường | Hệ thống mới khởi tạo | Người dùng xem danh mục Topic | Đúng 11 Topic: Toán học, Ngữ văn, Ngoại ngữ, Khoa học tự nhiên (Lý/Hóa/Sinh), Khoa học xã hội (Sử/Địa/KT&PL), Tin học, Kỹ năng mềm, Hướng nghiệp, Nghệ thuật & Sáng tạo, Góc Chill, Khác; một tầng, không có Category | Có | ISH-M05-001.1, 001.2 | Có | T-001: đúng 11 Topic như nguồn | Trùng |
| A-002 | QA-011 | Quyền | Guest chưa đăng nhập | Guest xem danh sách Topic và danh sách Tag | Được xem (CLAS: "Xem danh sách Topic / Tag / Khối lớp") | Có | ISH-M05-001.3 (chỉ Topic) | Có (Topic); Không (Tag: không có yêu cầu, không có hàng routing) | T-003: Guest thấy 11 Topic; không có ca cho danh sách Tag | Trùng (Topic); Không có ca của Author (Tag), chuyển P1 |
| A-003 | DEC-049, DEC-143 | Biên | User soạn bài, chọn 1 Topic | Gửi bài | Chấp nhận | Có | ISH-M05-002.4 | Có | T-010: gửi được với 1 Topic | Trùng |
| A-004 | DEC-049 | Biên | Bài đã chọn 3 Topic | Chọn Topic thứ 4 | Từ chối Topic thứ 4 (suy ra từ "max 3"); bài vẫn 3 Topic | Có | ISH-M05-002.8 | Có | T-015: từ chối, vẫn 3 Topic | Trùng |
| A-005 | DEC-049 | Vi phạm | Bài chưa chọn Topic nào | Gửi bài | Từ chối gửi (suy ra từ "Min 1 … (mandatory)") | Có | ISH-M05-002.5 | Có | T-011: từ chối gửi, vẫn bản nháp | Trùng |
| A-006 | DEC-049, DEC-031 | Thời gian | User đang soạn bài (DRAFT — "composing, not submitted"), chưa chọn Topic | Lưu bản nháp | Cách 1: từ chối (tối thiểu 1 áp dụng cho mọi lần lưu). Cách 2: chấp nhận, tối thiểu 1 chỉ kiểm khi gửi bài | Mơ hồ | ISH-M05-002.4, 002.5, 002.6 | Mơ hồ (002.4 phổ quát cho mọi bài viết; 002.5 chỉ kiểm khi gửi) | T-011 Given "Bài viết nháp của User A có 0 Topic": ngầm chọn cách 2 | Khác (P3-06) |
| A-007 | DEC-145 | Thường | Topic S đã bị gộp vào T | User chọn Topic khi soạn bài | S không có trong danh sách chọn | Có | ISH-M05-011.2, 002.2 | Có | T-008: từ chối "Góc Chill" | Trùng |
| A-008 | DEC-143 | Biên | Bài không có Tag | Gửi bài | Chấp nhận (0–5 Tag, Tag không bắt buộc) | Có | ISH-M05-006.3 | Có | T-060: gửi với 0 Tag | Trùng |
| A-009 | DEC-051, DEC-143 | Biên | Bài có 4 Tag | Thêm Tag thứ 5 | Chấp nhận; bài có 5 Tag | Có | ISH-M05-006.4 | Có | T-061 | Trùng |
| A-010 | DEC-051 | Vi phạm | Bài có 5 Tag | Thêm Tag thứ 6 | Từ chối Tag thứ 6 (suy ra); bài vẫn 5 Tag | Có | ISH-M05-006.5 | Có | T-062: từ chối, vẫn 5 Tag | Trùng |
| A-011 | DEC-051, DEC-150 | Biên | — | Nhập "#" + tên 30 ký tự | Chấp nhận ("#" không tính) | Có | ISH-M05-006.6 | Có | T-064: chấp nhận, 30 ký tự | Trùng |
| A-012 | DEC-051 | Vi phạm | — | Nhập tên Tag 31 ký tự | Từ chối (suy ra từ "max 30 chars/tag") | Có | ISH-M05-006.7 | Có | T-065: từ chối | Trùng |
| A-013 | DEC-152 | Định dạng | — | Nhập tên 30 chữ tiếng Việt có dấu (ví dụ "xácsuất…") | Mỗi chữ nhìn thấy tính 1 ký tự; 30 chữ được chấp nhận | Có | ISH-M05-006.15 | Có | T-130: chấp nhận 30 chữ có dấu | Trùng |
| A-014 | DEC-152 | Định dạng | — | Nhập "  #bayes  " | Bỏ khoảng trắng đầu/cuối, Tag "bayes" được chấp nhận | Có | ISH-M05-006.13 | Có | T-129: "bayes" được chấp nhận | Trùng |
| A-015 | DEC-152 | Rỗng | — | Nhập "#" hoặc "#   " | Từ chối (tên rỗng sau khi bỏ "#" và khoảng trắng) | Có | ISH-M05-006.14 | Có | T-066, T-128: từ chối | Trùng |
| A-016 | DEC-047, QA-101 | Định dạng | — | Nhập "#xác suất" (khoảng trắng giữa tên) | Từ chối (suy ra từ "no spaces"; nguồn không nêu hệ quả khác) | Có | ISH-M05-006.8 | Có | T-067: từ chối | Trùng |
| A-017 | DEC-051 | Chữ hoa–thường | Đã có Tag do User A tạo bằng "#Bayes" | User B nhập "#bayes" | Cùng một Tag (tên duy nhất, chuẩn hóa chữ thường); không tạo Tag mới | Có | ISH-M05-006.9 | Có | T-068: gắn Tag "bayes" đã có | Trùng |
| A-018 | DEC-051 | Thường | Tên "#dayso" chưa tồn tại | User gắn "#dayso" và gửi bài | Tag mới được tạo tự động, không cần duyệt | Có | ISH-M05-006.2 | Có | T-058: tạo ngay, không chờ duyệt | Trùng |
| A-019 | QA-108 | Thường | Bài có Topic A và Tag x | User viết bình luận | Bình luận không có Topic/Tag riêng; mang ngữ cảnh Topic/Tag của bài | Có | R7 (QA-108) | Có (không có hành vi) | — | Không cần ca |
| A-020 | DEC-051, DEC-090 | Quyền | Tag x đang hoạt động, gắn trên bài P | Mod vô hiệu hóa x | x bị ẩn khỏi autocomplete, Trending, trang duyệt; P giữ liên kết nhưng chip x bị ẩn | Có | ISH-M05-012.1, 012.2, 012.3; R5 (autocomplete, duyệt) | Có | T-117, T-118, T-119 | Trùng |
| A-021 | DEC-051, DEC-090 | Quyền | như A-020 | Admin vô hiệu hóa x | Như A-020 | Có | ISH-M05-012.1 | Có | Không có ca Admin vô hiệu hóa (chỉ T-121 Admin mở lại) | Không có ca của Author |
| A-022 | DEC-051 | Quyền | Tag x đang hoạt động | User thường yêu cầu vô hiệu hóa x | Từ chối (suy ra: chỉ Mod/Admin) | Có | ISH-M05-012.7 | Có | T-123: từ chối | Trùng |
| A-023 | DEC-051, QA-107 | Thường | x đã bị vô hiệu hóa | User gõ "#x" khi gắn Tag | x không được tạo thành Tag (không "tagified"), hiển thị dạng văn bản thường. Kết quả trên bài sau khi gửi: Cách 1: bài không có Tag x và không có chữ "#x"; Cách 2: chữ "#x" hiện dạng văn bản thường trên bài | Mơ hồ (phần sau khi gửi) | ISH-M05-012.4; R3 | Có (không gắn); số phận chữ "#x" sau khi gửi chưa nêu | T-120: không gắn | Trùng (phần chính); ghi chú nhỏ |
| A-024 | DEC-051, DEC-143, DEC-144 | Biên | Bài P có 5 Tag, trong đó x bị vô hiệu hóa (chip ẩn, liên kết giữ) | Tác giả sửa bài, thêm Tag y | Cách 1: từ chối (x vẫn tính, đã đủ 5). Cách 2: chấp nhận (chỉ tính Tag đang hoạt động; P có 6 liên kết) | Mơ hồ | ISH-M05-006.4, 012.2; OP-M05-05 | Mơ hồ, đã có OP-M05-05 (phần đếm giới hạn) | — | Không có ca của Author; đã có OP (không lập finding) |
| A-025 | DEC-150 | Thường | x bị vô hiệu hóa, gắn trên P | Mod/Admin mở lại x | x hiện lại trên P, dùng lại bình thường (gắn được, xuất hiện ở autocomplete/Trending) | Có | ISH-M05-012.5, 012.6 | Có | T-121, T-122 | Trùng |
| A-026 | DEC-051, ISS-084 | Quyền | Tag x | Mod/Admin yêu cầu đổi tên, gộp hoặc xóa x | Không có thao tác đó (Tag "fully free — mod/admin do NOT edit/merge/delete") | Có | ISH-M05-012.9, 012.10, 012.11 | Có | T-125, T-126, T-127: từ chối | Trùng |
| A-027 | DEC-144 | Quyền | Bài P của User A có Topic {Toán học} | A sửa bài, đổi Topic thành {Tin học, Khác} | Lưu thay đổi | Có | ISH-M05-002.9 | Có | T-017 | Trùng |
| A-028 | DEC-144 | Quyền | Bài P của A có Tag {x} | A sửa bài, đổi Tag thành {y, z} | Lưu thay đổi | Có | ISH-M05-006.11 | Có | T-071 | Trùng |
| A-029 | DEC-144 | Quyền | Bài P của A | Mod (rồi Admin) đổi Topic của P | Lưu thay đổi | Có | ISH-M05-009.1 | Có | T-100, T-101 | Trùng |
| A-030 | DEC-144 | Quyền | Bài P của A | Mod đổi Tag của P | Từ chối (suy ra: "A Mod or Admin does not change a post's Tags") | Có | ISH-M05-006.12 | Có | T-073: từ chối | Trùng |
| A-031 | DEC-144 | Quyền | Bài P của A | User B (không phải tác giả, không phải Mod/Admin) đổi Topic của P | Từ chối (suy ra) | Có | ISH-M05-009.2 | Có | T-102: từ chối | Trùng |
| A-032 | DEC-144 | Biên | Bài P có 1 Topic | Mod bỏ Topic duy nhất của P | Từ chối (1–3 áp dụng cho mọi lần đổi) | Có | ISH-M05-002.6 | Có | T-013: từ chối | Trùng |
| A-033 | DEC-144 | Biên | Bài P có 5 Tag | Tác giả sửa bài, thêm Tag thứ 6 | Từ chối | Có | ISH-M05-006.5, 006.11 | Có | Chỉ có ca khi tạo bài (T-062) | Không có ca của Author (ngữ cảnh sửa bài) |
| A-034 | DEC-050 | Thường | AI bật; tiêu đề + nội dung 40 tiếng; chưa bấm nút | User soạn bài | Không có gợi ý tự động (chỉ khi bấm "Gợi ý topic") | Có | ISH-M05-003.1 | Có | T-018 | Trùng |
| A-035 | DEC-050, DEC-147 | Thường | AI bật; tiêu đề + nội dung ≥ 10 tiếng | Bấm "Gợi ý topic" | Hệ thống phân tích tiêu đề + nội dung văn bản (không xử lý tệp đính kèm), trả tối đa 3 Topic được chọn sẵn | Có | ISH-M05-003, 003.2, 003.3, 003.4 | Có | T-019, T-020, T-023 | Trùng |
| A-036 | DEC-147 | Biên | Tiêu đề 3 tiếng + nội dung 6 tiếng = 9 | Bấm "Gợi ý topic" | Từ chối gợi ý, báo nội dung quá ngắn | Có | ISH-M05-003.6, 003.7 | Có | T-025, T-030: từ chối, báo quá ngắn | Trùng |
| A-037 | DEC-147 | Biên | Tiêu đề 3 tiếng + nội dung 7 tiếng = 10 | Bấm "Gợi ý topic" | Thực hiện gợi ý | Có | ISH-M05-003.6 | Có | T-026: chấp nhận | Trùng |
| A-038 | DEC-147 | Định dạng | Nội dung "x = 2 ?" (4 cụm ngăn bởi khoảng trắng) + tiêu đề 6 tiếng | Bấm "Gợi ý topic" | Đếm 10 tiếng → thực hiện gợi ý (mỗi cụm ngăn bởi khoảng trắng là một tiếng) | Có | ISH-M05-003.6; 2.1 "Tiếng" | Có | T-029 (nhiều dấu cách, xuống dòng) | Trùng |
| A-039 | DEC-050, DEC-147 | Biên | Tiêu đề 4 tiếng, nội dung văn bản rỗng, có tệp PDF dài | Bấm "Gợi ý topic" | Từ chối (tệp đính kèm không được phân tích, 4 < 10) | Có | ISH-M05-003.2, 003.6 | Có | — | Không có ca của Author |
| A-040 | DEC-148 | Thường | User đã tự tick {Toán học} | Bấm gợi ý; AI trả {Tin học, Khác} | Lựa chọn thành {Tin học, Khác} (thay thế, kể cả Topic đã tự tick) | Có | ISH-M05-003.4 | Có | T-022 | Trùng |
| A-041 | DEC-050 | Thường | Gợi ý {Tin học, Khác} | User bỏ "Khác", tick "Toán học", gửi bài | Bài có {Tin học, Toán học}; được gửi | Có | ISH-M05-003.5 | Có | T-024 | Trùng |
| A-042 | DEC-050, DEC-148 | Thời gian | Đã có gợi ý | User sửa một chữ trong tiêu đề | Gợi ý thành cũ: cảnh báo nhẹ + nút gợi ý lại; không chặn gửi bài | Có | ISH-M05-003.10, 003.12, 003.13, 003.14 | Có | T-035, T-038, T-041 | Trùng |
| A-043 | DEC-148 | Thời gian | Đã có gợi ý | User chỉ thêm/xóa tệp đính kèm | Gợi ý không thành cũ | Có | ISH-M05-003.11 | Có | T-037 | Trùng |
| A-044 | DEC-148 | Thời gian | Đã có gợi ý | User sửa một chữ rồi sửa về đúng văn bản cũ | Cách 1: thành cũ (đã có thay đổi). Cách 2: không thành cũ (văn bản giống lúc gợi ý). Khác nhau ở cảnh báo và việc ghi phản hồi | Mơ hồ (nhỏ) | ISH-M05-003.10 | Mơ hồ (nhỏ) | — | Không có ca của Author; ghi chú nhỏ |
| A-045 | DEC-149 | Lỗi | — | AI trả {Toán học, "Vật lý", Tin học} | Bỏ "Vật lý"; giữ và chọn sẵn {Toán học, Tin học} | Có | ISH-M05-004.5 | Có | T-048 | Trùng |
| A-046 | DEC-149, DEC-132, DEC-099 | Lỗi | User đang chọn {Ngữ văn} | AI trả {"Vật lý", "Hóa"} (không Topic hợp lệ) | Gợi ý thất bại: báo lỗi không chặn; lựa chọn {Ngữ văn} giữ nguyên ("no action taken"); User chọn thủ công | Có | ISH-M05-004.6, 004.2, 004.3 | Có | T-049 | Trùng |
| A-047 | DEC-152 | Biên | — | AI trả 5 Topic hợp lệ theo thứ tự [Tin học, Toán học, Ngữ văn, Khác, Hướng nghiệp] | Giữ 3 Topic đầu [Tin học, Toán học, Ngữ văn] | Có | ISH-M05-004.7 | Có | T-021 (4 Topic, giữ 3 đầu) | Trùng |
| A-048 | DEC-152, DEC-149 | Biên | — | AI trả [Toán học, "Vật lý", Tin học, Khác, Ngữ văn] | Bỏ "Vật lý" trước, rồi giữ 3 đầu: [Toán học, Tin học, Khác] | Có | ISH-M05-004.5, 004.7 | Có | — | Không có ca của Author |
| A-049 | DEC-145, DEC-149 | Lỗi | S đã gộp vào T | AI trả {S, Tin học} | Bỏ S (không còn trong danh mục), giữ {Tin học} | Có | ISH-M05-011.2, 004.5 | Có | — | Không có ca của Author |
| A-050 | DEC-099 | Lỗi | AI bật | Lần gọi đầu hết thời gian, lần thử lại cũng lỗi | Báo lỗi không chặn, không thay đổi lựa chọn; vẫn gửi bài được | Có | ISH-M05-004.2, 004.3, 004.4 | Có | T-045, T-046, T-047 | Trùng |
| A-051 | DEC-099 | Lỗi | AI bật | Lần đầu lỗi, lần thử lại thành công | Hiển thị gợi ý của lần thử lại | Có | R2 (thử lại); ISH-M05-003 | Có | — | Không có ca của Author |
| A-052 | DEC-008, DEC-099 | Cấu hình | Công tắc AI tổng TẮT | User soạn bài | Không có gợi ý; User chọn Topic từ danh sách | Có | ISH-M05-004.1, 004 | Có | T-042 | Trùng |
| A-053 | DEC-093 | Cấu hình | AI tổng BẬT, công tắc "Topic suggestion" TẮT | User soạn bài | Như A-052 | Có | ISH-M05-004.1 | Có | T-043 | Trùng |
| A-054 | DEC-100 | Vi phạm | User đã gửi 10 yêu cầu gợi ý trong 1 phút | Gửi yêu cầu thứ 11 trong cùng phút | Từ chối (suy ra từ "10 requests/min/user"); cửa sổ đếm là chi tiết R2 | Có | ISH-M05-003.9; R2 | Có | T-032 | Trùng |
| A-055 | DEC-050, DEC-144 | Thời gian | Bài P đã đăng; tác giả mở sửa bài | Tác giả muốn dùng "Gợi ý topic" | Cách 1: có gợi ý khi sửa (luồng DEC-050 áp dụng cả khi sửa). Cách 2: không (luồng DEC-050 chỉ mô tả lúc tạo rồi publish) | Mơ hồ | ISH-M05-003 ("bài viết mới"); OP-M05-02 | Mơ hồ, đã có OP-M05-02 | — | Đã có OP (không lập finding) |
| A-056 | DEC-050 | Thường | Gợi ý {Tin học, Khác}, chưa thành cũ | User gửi bài với {Tin học, Toán học} | Ghi phản hồi: gợi ý {Tin học, Khác} so với lựa chọn cuối {Tin học, Toán học} | Có | ISH-M05-005.1 | Có | T-051 | Trùng |
| A-057 | DEC-050, QA-104 | Thời gian | Gợi ý đã thành cũ | User gửi bài | Không ghi phản hồi | Có | ISH-M05-005.2 | Có | T-053 | Trùng |
| A-058 | DEC-050 | Thường | User tự chọn Topic, không bấm gợi ý | Gửi bài | Không có luồng AI, không ghi phản hồi | Có | ISH-M05-005.3 | Có | T-054 | Trùng |
| A-059 | DEC-050 | Thời gian | Gợi ý thành cũ, User bấm gợi ý lại (gợi ý mới) | Gửi bài | Ghi phản hồi theo gợi ý mới (không còn cũ) | Có | ISH-M05-005.1 | Có | T-052 | Trùng |
| A-060 | DEC-050, DEC-144 | Thời gian | Bài đã gửi kèm phản hồi; sau đó tác giả hoặc Mod đổi Topic | — | Cách 1: phản hồi giữ theo lần gửi đầu. Cách 2: cập nhật theo lựa chọn mới. Khác nhau ở số liệu đánh giá AI | Mơ hồ (nhỏ) | ISH-M05-005 ("khi tác giả gửi"); OP-M05-10 (gửi lại sau từ chối) | Có (SR chỉ ghi khi gửi, khớp "final selection" của DEC-050) | — | Ghi chú nhỏ |
| A-061 | DEC-141, QA-043 | Thường | User U chưa theo dõi Topic A (A có 5 người theo dõi) | U theo dõi A | U ở trạng thái đang theo dõi; số người theo dõi A = 6 | Có | ISH-M05-007.1, 007.4 | Có | T-075 | Trùng |
| A-062 | DEC-141 | Thường | U đang theo dõi A (6 người) | U bỏ theo dõi | U không theo dõi; số = 5 | Có | ISH-M05-007.2 | Có | T-076 | Trùng |
| A-063 | QA-011, DEC-126 | Quyền | Guest | Bấm theo dõi Topic | Từ chối, yêu cầu đăng nhập ("All interactions (… follow …) require login") | Có | ISH-M05-007.5 | Có | T-080 | Trùng |
| A-064 | DEC-141 | Số đếm | Topic có 0 / 1 / 37 người theo dõi | Xem Topic | Hiển thị 0 / 1 / 37 | Có | ISH-M05-007.4 | Có | T-078 (0), T-075 (1), T-079 (25) | Trùng |
| A-065 | DEC-141 | Vi phạm | Tag x | User muốn theo dõi x | Không có thao tác theo dõi Tag | Có | R7 (DEC-141) | Có | — | Không cần ca |
| A-066 | DEC-145 | Công thức | U1 theo dõi S; U2 theo dõi S và T; U3 theo dõi T | Mod gộp S vào T | T có 3 người theo dõi {U1, U2, U3}; U2 tính một lần; S không theo dõi được | Có | ISH-M05-011.3, 011.4 | Có | T-114, T-115 (5 + 8 − 2 = 11) | Trùng |
| A-067 | QA-043, DEC-141 | Thường | U theo dõi A | Có bài mới thuộc A | Thông báo thuộc M07 (không phải hành vi M05) | Có | R5 (M07) | Có | — | Không cần ca |
| A-068 | DEC-142, DEC-146 | Công thức | Topic A: P1 công khai, tạo T−3n, 4 upvote còn tồn tại (đều trong cửa sổ) + 1 upvote đã rút, 3 bình luận (2 gốc + 1 trả lời) lúc T−1n; P2 công khai, tạo T−20n, 5 upvote lúc T−10n + 2 upvote lúc T−1n, 1 bình luận lúc T−1n; P3 thuộc Group Private, tạo T−1n, 10 upvote; P4 mod_state HIDDEN, tạo T−2n, 6 upvote | Tính điểm A | P1 = 2×4 + 3 + 1 = 12; P2 = 2×2 + 1 + 0 = 5; P3 = 0; P4 = 0 → A = **17** | Có | ISH-M05-008.1, 008.3, 008.6 | Có | T-082 (K = 17), T-087, T-093 | Trùng (cùng phương pháp, khác số liệu) |
| A-069 | DEC-142 | Công thức | Topic B: P5 công khai tạo T−2n không tương tác; P6 công khai tạo T−30n không tương tác trong cửa sổ | Tính điểm B | P5 = 1 (thưởng bài mới), P6 = 0 → B = **1**; thứ hạng A (17) trên B (1) | Có | ISH-M05-008.1, 008.9 | Có | T-083 (L = 1), T-082 P3 = 0 | Trùng |
| A-070 | DEC-142 | Công thức | P1 (A-068) gắn cả Topic A và Topic B | Tính điểm A và B | P1 đóng góp 12 cho A và 12 cho B ("every post of the Topic/Tag counts") | Có | ISH-M05-008.1 | Có | T-085 | Trùng |
| A-071 | DEC-146 | Công thức | P1 có một bình luận được 3 upvote | Tính điểm | Upvote của bình luận không tính | Có | ISH-M05-008.4 | Có | T-091 | Trùng |
| A-072 | DEC-146, DEC-033 | Công thức | Bài ở DRAFT / PENDING / HIDDEN (tác giả ẩn) / REJECTED / DELETED / mod_state HIDDEN; bài Group Public; bài của User BANNED | Tính điểm | Chỉ bài PUBLISHED + NORMAL, không thuộc Group Private được tính → bài Group Public và bài của User BANNED được tính, các bài kia không | Có | ISH-M05-008.3; 2.1 "Bài viết công khai" | Mơ hồ với bài FLAGGED và bài tác giả tự ẩn (A-091, A-092); Có với các trường hợp còn lại | T-088, T-089, T-090 (không có bài FLAGGED hay tự ẩn) | Trùng một phần (P3-04) |
| A-073 | DEC-142 | Thời gian, Công thức | P7: bản nháp tạo T−10n, gửi T−2n, công khai T−2n, không tương tác | Tính điểm Topic của P7 | Cách 1 ("created" = lúc tạo bản nháp): 0. Cách 2 ("created" = lúc gửi/công khai): 1. Ảnh hưởng cả tiêu chí phá hòa DEC-153 | Mơ hồ | ISH-M05-008.1, 008.2, 008.11, 008.12 | Mơ hồ ("được đăng": lúc gửi hay lúc công khai; 2.1 không định nghĩa) | T-082 "đăng 2 ngày trước": không phân biệt | Khác, Author không nhận ra (P3-01) |
| A-074 | DEC-146 | Công thức | P1 có 3 bình luận, 1 bình luận bị ẩn (mod_state HIDDEN của bình luận, do AI hoặc Mod) | Tính điểm | Cách 1: bình luận bị ẩn vẫn "còn tồn tại" → P1 = 12. Cách 2: bình luận không công khai không tính → P1 = 11 | Mơ hồ | ISH-M05-008.5, 008.7 | Mơ hồ (chỉ nêu "đã bị xóa") | T-094 chỉ có bình luận đã xóa | Không có ca của Author (P3-02) |
| A-075 | DEC-146 | Công thức | P1 có bình luận gốc đã xóa (còn tombstone vì có trả lời) và 1 trả lời còn tồn tại | Tính điểm | Bình luận gốc đã xóa không tính; trả lời tính 1 | Có | ISH-M05-008.5, 008.7 | Có | T-094 (một phần) | Trùng |
| A-076 | DEC-153 | Thứ tự | Topic C điểm 10, 3 bài tính được tạo trong cửa sổ; Topic D điểm 10, 1 bài | Xếp hạng | C trên D | Có | ISH-M05-008.11 | Có | T-133 | Trùng |
| A-077 | DEC-153 | Thứ tự | "Khác" và "Khoa học tự nhiên (Lý/Hóa/Sinh)" cùng điểm, cùng số bài | Xếp hạng | Cách 1 (thứ tự chữ cái tiếng Việt, a < o): "Khác" trước. Cách 2 (thứ tự mã ký tự, "o" U+006F < "á" U+00E1): "Khoa học tự nhiên" trước. Tương tự Tag "đạohàm" và "elip" | Mơ hồ | ISH-M05-008.11, 008.12 | Mơ hồ (chép nguyên "A đến Z") | T-134, T-135 chỉ dùng tên khác nhau ở chữ cái không dấu | Khác, ca của Author không lộ mơ hồ (P3-03) |
| A-078 | DEC-051, DEC-150 | Thường | Tag x có điểm cao nhất, rồi bị vô hiệu hóa; sau đó mở lại | Tính điểm sau mỗi lần | Khi vô hiệu: x không có trong xếp hạng Tag. Khi mở lại: x xếp hạng lại | Có | ISH-M05-012.3, 008.2 | Có | T-119 (vô hiệu hóa); không có ca mở lại rồi xếp hạng | Trùng một phần |
| A-079 | DEC-145, DEC-049 | Công thức | S gộp vào T; bài Q gắn {S, T} tạo T−1n | Tính điểm T | S không xếp hạng; Q tính một lần cho T (Q còn 1 Topic là T) | Có (suy ra) | ISH-M05-011.1, 008.1 | Có | T-110, T-113 | Trùng |
| A-080 | DEC-052 | Thời gian | Upvote mới vào P1 lúc T+1 phút | Xem điểm trước lần tính lại kế tiếp | Điểm chưa đổi cho tới lần tính lại (15–30 phút; chi tiết chu kỳ thuộc R2) | Có | R2 | Có | — | Không cần ca |
| A-081 | QA-235, DEC-052 | Số đếm | Tag z điểm 0 | Xem xếp hạng Trending Tag | Cách 1: z có trong xếp hạng (không đặt ngưỡng). Cách 2: chỉ mục điểm > 0. Phần hiển thị thuộc M14 | Mơ hồ (nhỏ, có thể thuộc M14) | R5 (QA-235, M14) | Mơ hồ (nhỏ, phần hiển thị thuộc M14) | — | Ghi chú nhỏ |
| A-082 | DEC-049, DEC-090 | Quyền | Topic "Góc Chill" | Mod (rồi Admin) đổi tên thành "Góc thư giãn" | Danh mục và mọi bài dùng tên mới | Có | ISH-M05-010, 010.1 | Có | T-104 | Trùng |
| A-083 | DEC-049 | Quyền | — | User thường đổi tên Topic | Từ chối (suy ra) | Có | ISH-M05-010.3 | Có | T-106 | Trùng |
| A-084 | DEC-049 | Vi phạm | Có Topic "Tin học" | Mod đổi tên "Khác" thành "Tin học" (trùng) hoặc thành tên rỗng | Cách 1: từ chối. Cách 2: chấp nhận (hai Topic cùng tên / Topic không tên). Nguồn không nêu ràng buộc tên Topic | Mơ hồ | ISH-M05-010; OP-M05-04 | Mơ hồ, đã có OP-M05-04 | — | Đã có OP (không lập finding) |
| A-085 | DEC-049, DEC-145 | Thường | S có 4 bài, 2 người theo dõi | Mod gộp S vào T | 4 bài chuyển sang T; S biến khỏi danh mục (không chọn, gợi ý, xếp hạng, theo dõi được); người theo dõi chuyển sang T | Có | ISH-M05-011, 011.2, 011.3 | Có | T-111, T-112, T-114 | Trùng |
| A-086 | DEC-049 | Biên | Bài Q gắn {S, T, U} | Gộp S vào T | Q còn {T, U} | Có (suy ra) | ISH-M05-011 | Có | — | Không có ca của Author |
| A-087 | DEC-049 | Quyền | — | User thường gộp Topic | Từ chối (suy ra) | Có | ISH-M05-011.5 | Có | T-116 | Trùng |
| A-088 | DEC-049, ISS-084 | Vi phạm | — | Mod/Admin xóa Topic | Không có thao tác xóa / từ chối ("No delete") | Có | ISH-M05-010.4 | Có | T-108, T-109 | Trùng |
| A-089 | DEC-140 | Thường | — | User chọn Lớp/Khối cho bài | Không thuộc M05 (M03 F-POST-09, M02) | Có | R5 (M03, M02) | Có | — | Không cần ca |
| A-090 | QA-269 | Thường | AI bật | User bấm gợi ý | Không gợi ý Tag (chỉ Topic) | Có | R7 (QA-269) | Có | — | Không cần ca |
| A-091 | DEC-146, DEC-032, DEC-033 | Công thức | P15 publish_state PUBLISHED, mod_state FLAGGED (bị báo cáo, chờ Mod), tạo T−1n, 2 upvote | Tính điểm Topic của P15 | Không tính ("publish_state PUBLISHED and mod_state NORMAL") → 0 | Có | ISH-M05-008.3; 2.1 "Bài viết công khai" | Mơ hồ: theo 2.1 ("đã xuất bản và không bị ẩn bởi kiểm duyệt") P15 chưa bị ẩn → tính 2×2 + 1 = 5 | Không có ca (T-089 chỉ có "P7 bị Mod ẩn") | Không có ca của Author (P3-04) |
| A-092 | DEC-146, DEC-031 | Công thức | P16 tác giả tự ẩn (publish_state HIDDEN), trước đó đã công khai, tạo T−1n, 2 upvote | Tính điểm | Không tính (không phải PUBLISHED) → 0 | Có | ISH-M05-008.3; 2.1 | Mơ hồ: "đã xuất bản" đọc được là "đã từng xuất bản" → 5 | Không có ca | Không có ca của Author (P3-04) |
| A-093 | DEC-145 | Vi phạm | S đã gộp vào T | User yêu cầu theo dõi S | Không theo dõi được ("can no longer be … followed") → từ chối | Có | ISH-M05-007.1, 011.2 | Mơ hồ: 007.1 không giới hạn Topic trong danh mục; 2.1 chỉ định nghĩa danh mục là tập Topic "cho phép chọn cho bài viết" | Không có ca | Không có ca của Author (P3-05) |
| A-094 | DEC-145, QA-235 | Thường | S đã gộp vào T; không ngưỡng tối thiểu vào Trending | Xếp hạng Topic | S không có trong xếp hạng ("can no longer be … ranked in Trending") | Có | ISH-M05-008, 011.2 | Mơ hồ: 008 xếp hạng "các Topic", không giới hạn trong danh mục; S còn tồn tại ở trạng thái "đã loại khỏi danh mục" (5.2) với điểm 0 | T-113: "Góc Chill" không có trong bảng xếp hạng (Author suy từ 011.2) | Trùng kết quả, nhưng SR không nêu (P3-05) |
| A-095 | DEC-048, QA-267 (cho yêu cầu ISH-M05-001.4) | Vi phạm | Admin | Thêm Topic thứ 12 | Không có thao tác thêm ("11, final"; "11 giá trị cố định") | Có | ISH-M05-001.4 | Có | T-005 | Trùng |
| A-096 | DEC-051 (cho yêu cầu ISH-M05-006.10 Suy ra) | Lặp | Bài có 5 Tag gồm "bayes" | Gắn thêm "BAYES" | Bài vẫn 5 Tag, không vượt giới hạn | Có (suy ra) | ISH-M05-006.10 | Có | T-069, T-070 | Trùng |
| A-097 | DEC-141 (cho yêu cầu ISH-M05-007.6 Suy ra) | Lặp | U đang theo dõi A (1 người) | U theo dõi A lần nữa | Vẫn 1 người | Có (suy ra) | ISH-M05-007.6 | Có | T-081 | Trùng |
| A-098 | DEC-049 (cho ISH-M05-010.1, 010.2 Suy ra) | Thường | "Góc Chill" có 15 bài, 12 người theo dõi | Đổi tên | Cùng 15 bài, cùng 12 người | Có (suy ra) | ISH-M05-010.1, 010.2 | Có | T-104, T-105 | Trùng |

Ghi chú ca: A-091…A-094 được thêm ở P3.3 khi mở SR (ca nguồn cho hệ quả SR diễn đạt khác nguồn); A-095…A-098 là ca cho các yêu cầu `Suy ra`/`Nói thẳng` không có ca nguồn tương ứng ở P3.2, đều hợp lý.

Tổng: 98 ca; nguồn `Mơ hồ`: A-006, A-023 (phần sau khi gửi), A-024, A-044, A-055, A-060, A-073, A-074, A-077, A-081, A-084. Trong đó đã có `OP` ở Phụ lục B: A-024 (OP-M05-05), A-055 (OP-M05-02), A-084 (OP-M05-04). Nguồn xác định mà SR `Mơ hồ`: A-072/A-091/A-092, A-093, A-094.

## 2. Quét khung hành vi (P3.2b, đối chiếu P3.3–P3.4)

Cột 1–4 dựng từ nguồn trước khi mở SR; cột 5–7 điền sau. Cột "Selfcheck" lấy bảng "Quét khung hành vi" của `selfcheck-M05.md` (tính năng theo số mục của SR).

| Tính năng | Câu hỏi (1–7, RULES §4.7) | Nguồn nói gì | Loại (a/b/c/d) | SR (ID yêu cầu hoặc "—") | Selfcheck của Author (loại) | Kết luận |
|---|---|---|---|---|---|---|
| F1 Danh mục Topic | 1 Ai | Mọi người xem; Guest xem danh sách Topic **và Tag** (QA-011) | a | 001.3 (chỉ Topic) | 5.3 Q1: a (chỉ Topic) | Phần Tag không có chỗ đi: chuyển P1 (CL-A10) |
| F1 | 3 Kết quả | 11 Topic phẳng cố định (DEC-048, DEC-140) | a | 001.1, 001.2, 001.4 | a | Khớp |
| F1 | 6 Sửa/xóa/ẩn | Đổi tên, gộp; không xóa (DEC-049) | a | 010, 011, 010.4 | a | Khớp |
| F2 Gắn Topic | 1 Ai | Tác giả khi soạn bài | a | 002.1 | a | Khớp |
| F2 | 2 Thời điểm | "mandatory": khi lưu bản nháp hay khi gửi (A-006) | c | 002.4 (phổ quát), 002.5 (khi gửi) | 5.4 Q2: "c→hỏi" chỉ về sửa bài sau khi gửi; không nhắc bản nháp | GAP (P3-06) |
| F2 | 4 Giới hạn | 1–3; vi phạm → từ chối | a, b | 002.4–002.8 | a/b | Khớp |
| F3 Gắn Tag | 4 Giới hạn | 0–5; 30 ký tự không tính "#"; không khoảng trắng; chuẩn hóa | a, b | 006.3–006.8, 006.13–006.15 | c→hỏi (đã có DEC) | Khớp |
| F3 | 3 Kết quả | Tự tạo không duyệt; tên duy nhất không phân biệt hoa thường | a | 006.2, 006.9 | a | Khớp |
| F3 | 5 Đối tượng liên quan | Tag vô hiệu hóa có tính vào 5 khi sửa bài; còn gắn sau khi sửa không (A-024) | c | — | 5.8 Q5: c → OP-M05-05 (chỉ phần đếm) | Đã có OP (phần đếm); phần "còn gắn sau khi sửa" ghi chú nhỏ |
| F3 | 5 | Số phận "#x" của Tag vô hiệu hóa sau khi gửi (A-023) | c (nhỏ) | 012.4; R3 | a | Ghi chú nhỏ |
| F4 Gợi ý Topic AI | 1, 2 Ai/khi nào | Bấm nút khi soạn bài; không tự động | a | 003, 003.1 | a | Khớp |
| F4 | 2 | Dùng được khi sửa bài đã đăng không (A-055) | c | 003 ("bài viết mới") | 5.5 Q2: a/c → OP-M05-02 | Đã có OP |
| F4 | 4 Giới hạn | ≥10 tiếng; tối đa 3; 10 lần/phút | a, b | 003.3, 003.6–003.9, 004.7 | c→hỏi (đã có DEC) | Khớp |
| F4 | 5 Đối tượng liên quan | Thay thế lựa chọn; thành cũ khi đổi tiêu đề/nội dung | a | 003.4, 003.10, 003.11 | c→hỏi (đã có DEC) | Khớp |
| F4 | 7 AI không đáp ứng | Tắt → chọn tay; lỗi → báo lỗi không chặn; Topic ngoài danh mục → bỏ | a | 004.1–004.7 | a | Khớp |
| F5 Phản hồi gợi ý | 3 Kết quả | Ghi khi không thành cũ | a | 005.1–005.3 | a | Khớp |
| F5 | 5 | Đổi Topic sau khi gửi có cập nhật phản hồi (A-060) | c (nhỏ) | 005 (khi gửi) | 5.7 Q2: a/c → OP-M05-10 | Ghi chú nhỏ |
| F6 Theo dõi Topic | 1 Ai | User đăng nhập; Guest phải đăng nhập | a, b | 007, 007.5 | a | Khớp |
| F6 | 3 Kết quả | Trạng thái, số người theo dõi | a | 007.1–007.4 | a | Khớp |
| F6 | 5 | Gộp → chuyển người theo dõi, tính một lần; Topic nguồn không theo dõi được nữa (DEC-145); thông báo → M07 | a | 011.3, 011.4; R5 M07; **—** cho "không theo dõi được Topic nguồn" | 5.9 Q6: a (011.3); không nhắc Topic nguồn | DEFECT (P3-05) |
| F7 Điểm Trending | 3 Công thức | DEC-142, DEC-146 xác định | a | 008.1–008.8 | c→hỏi (đã có DEC) | Khớp, trừ định nghĩa "bài viết công khai" (P3-04) |
| F7 | 4 Cửa sổ | "posts created in window" / "được đăng": thời điểm nào (A-073) | c | 008.1, 008.2, 008.11, 008.12 (chép "được đăng") | 5.10 Q2: a | GAP (P3-01) |
| F7 | 5 | Bình luận bị ẩn có "còn tồn tại" không (A-074) | c | 008.7 (chỉ "đã bị xóa") | 5.10 Q4: c→hỏi (DEC-146), không nhắc bình luận bị ẩn | GAP (P3-02) |
| F7 | 3 Thứ tự | A→Z với tên tiếng Việt (A-077) | c | 008.11, 008.12 (chép nguyên) | 5.10 Q3: c→hỏi (DEC-153) | GAP (P3-03) |
| F7 | 5 | Topic nguồn sau gộp không xếp hạng (DEC-145) | a | **—** (008 không giới hạn trong danh mục) | 5.10 Q5: a "Topic nguồn sau gộp bị loại (011.2)" | DEFECT (P3-05) |
| F8 Đổi tên Topic | 1 Ai | Mod/Admin | a, b | 010, 010.3 | a | Khớp |
| F8 | 4 Giới hạn | Tên trùng/rỗng (A-084) | c | — | 5.12 Q4: c → OP-M05-04 | Đã có OP |
| F9 Gộp Topic | 3, 5 | Bài chuyển sang đích; nguồn biến khỏi danh mục; người theo dõi chuyển | a | 011, 011.1–011.4 | a, c→hỏi | Khớp (trừ P3-05) |
| F9 | 6 | Không xóa Topic | a, b | 010.4 | a | Khớp |
| F10 Đổi Topic/Tag sau khi gửi | 1 Ai | Tác giả: Topic + Tag; Mod/Admin: chỉ Topic | a, b | 002.9, 006.11, 006.12, 009, 009.1, 009.2 | a | Khớp |
| F10 | 4 | Giới hạn áp dụng mọi lần đổi | a | 002.6, 002.8, 006.5 | a | Khớp |
| F11 Vô hiệu hóa/mở lại Tag | 1 Ai | Mod/Admin | a, b | 012, 012.7, 012.8 | a | Khớp |
| F11 | 5 | Ẩn khỏi autocomplete/Trending/duyệt; chip ẩn; gõ lại không gắn; mở lại hiện lại | a | 012.1–012.6; R5 (autocomplete, duyệt) | a | Khớp |
| F11 | 6 | Không sửa/gộp/xóa Tag | a | 012.9–012.11 | c→hỏi | Khớp |

Điểm nhỏ (ghi chú, không lập finding riêng): A-044 (sửa rồi hoàn nguyên văn bản có làm gợi ý thành cũ); A-060 (đổi Topic sau khi gửi có cập nhật phản hồi); A-081 (Tag điểm 0 có trong xếp hạng, phần hiển thị thuộc M14); A-023 (chữ "#x" của Tag bị vô hiệu hóa có còn trên bài sau khi gửi); A-024 phần thứ hai (bài đang mang Tag bị vô hiệu hóa được tác giả sửa: liên kết với Tag đó còn giữ không — có thể gộp vào OP-M05-05); Tag mới được tạo lúc gắn khi soạn nháp hay lúc gửi. Các điểm đã có OP: A-024 (OP-M05-05), A-055 (OP-M05-02), A-084 (OP-M05-04), hiển thị chữ hoa thường của Tag (OP-M05-08), số người theo dõi hiển thị cho ai (OP-M05-06).
