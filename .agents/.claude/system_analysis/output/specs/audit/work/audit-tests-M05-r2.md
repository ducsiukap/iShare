# Ca kiểm độc lập — ISH-AUD-M05-r2 · lượt P3
<!-- [Vietnamese Doc] -->

| Trường | Giá trị |
|---|---|
| Module | M05 — Topic & Tag |
| Vòng | 2 |
| Lượt | P3 |
| SR / routing | ISH-SR-M05 v0.2 (2026-10-05) / ISH-RT-M05 v0.2 (2026-10-05); trùng `snapshot-…-v0.2.md` (`diff -q` không báo khác) |
| Nguồn xác định | Như vòng 1 (DRAFT `iShare_modules.md` §3, §4.5, §7.1, §7.2, §11.2, §11.5; OWNED DEC-047…052, DEC-140…153, ISS-079…084, ISS-207…227, QA-101…108, QA-267…287) **cộng 24 mục OWNED mới**: DEC-154…159, ISS-228…236, QA-288…296; REFERENCING mới: DEC-065 [Added — DEC-155]; nguồn liên quan: DEC-031…034, DEC-099, DEC-100, DEC-124, DEC-126, DEC-132, QA-011, QA-201 (cấm tự vote), QA-235 |
| Inventory | `audit-inventory-P3-M05-r2.md/.json` (OWNED 100, REFERENCING 21, KEYWORD 98, CROSS 40, DRAFT 34) |
| Thứ tự làm | Ca mới/đổi và các ô quét đổi được ghi vào tệp này **trước khi** mở SR/routing v0.2 (bản đầu, chỉ có cột nguồn). Sau đó mới mở SR, điền cột SR và Author, rồi ghi đè bằng bản đầy đủ này |

Quy ước: `T` = thời điểm tính điểm Trending; "T−3n" = 3 ngày trước `T`. Ca A-001…A-098 lấy từ `audit-tests-M05-r1.md` (dựng từ nguồn không đổi). Các ca có nguồn mới hoặc ID SR đổi được viết lại: A-002, 003, 006, 060, 067, 068, 072, 073, 074, 077, 081, 088, 091…094. Ca mới A-099…A-119 phủ mọi yêu cầu có ID mới hoặc đổi ở v0.2 (001, 001.5, 002, 002.6, 002.10, 002.11, 003.11, 004, 005, 005.1, 005.4, 006, 006.16, 008.1, 008.2, 008.11…008.19, 011.6…011.10, 012) và mọi mục nguồn mới. Cột ID yêu cầu của các hàng giữ nguyên đã được kiểm bằng script: mọi ID còn tồn tại ở v0.2 (chỉ 002.4 và 010.4 bị bỏ; các hàng liên quan đã viết lại).

## 1. Bảng ca kiểm

| ID ca | Nguồn | Loại | Given | When | Then theo nguồn | Nguồn xác định? | ID yêu cầu SR | SR xác định? | Then theo ca kiểm của Author | Đối chiếu |
|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | DEC-048, DEC-140 | Thường | Hệ thống mới khởi tạo | Người dùng xem danh mục Topic | Đúng 11 Topic: Toán học, Ngữ văn, Ngoại ngữ, Khoa học tự nhiên (Lý/Hóa/Sinh), Khoa học xã hội (Sử/Địa/KT&PL), Tin học, Kỹ năng mềm, Hướng nghiệp, Nghệ thuật & Sáng tạo, Góc Chill, Khác; một tầng, không có Category | Có | ISH-M05-001.1, 001.2 | Có | T-001: đúng 11 Topic như nguồn | Trùng |
| A-002 | QA-011 | Quyền | Guest chưa đăng nhập | Guest xem danh sách Topic và danh sách Tag | Được xem ("Xem danh sách Topic / Tag / Khối lớp") | Có | ISH-M05-001.3 (Topic); R5 M14/M06 (danh sách Tag cho Guest, `ISH-RT-M05.md:64`) | Có | T-003: Guest thấy 11 Topic | Trùng (Topic); phần Tag nằm ở R5 |
| A-003 | DEC-049, DEC-143 | Biên | User soạn bài, chọn 1 Topic | Gửi bài | Chấp nhận | Có | ISH-M05-002, 002.5 | Có | T-010: gửi được với 1 Topic | Trùng |
| A-004 | DEC-049 | Biên | Bài đã chọn 3 Topic | Chọn Topic thứ 4 | Từ chối Topic thứ 4 (suy ra từ "max 3"); bài vẫn 3 Topic | Có | ISH-M05-002.8 | Có | T-015: từ chối, vẫn 3 Topic | Trùng |
| A-005 | DEC-049 | Vi phạm | Bài chưa chọn Topic nào | Gửi bài | Từ chối gửi (suy ra từ "Min 1 … (mandatory)") | Có | ISH-M05-002.5 | Có | T-011: từ chối gửi, vẫn bản nháp | Trùng |
| A-006 | DEC-156 | Thời gian | User soạn bài mới, chưa chọn Topic | Lưu bản nháp | Chấp nhận ("a draft can be saved with no Topic") | Có | ISH-M05-002.11 | Có | T-139: bản nháp được lưu với 0 Topic | Trùng (r1: Mơ hồ → đã hỏi, ISS-230) |
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
| A-060 | DEC-157, QA-293, DEC-034 | Thời gian | Bài bị từ chối; lần gửi đầu đã ghi 1 phản hồi; gợi ý gần nhất vẫn còn mới (tác giả chỉ đổi tệp đính kèm) | Tác giả gửi lại | QA-293 "một bản ghi mỗi lần gửi bài": thêm 1 bản ghi cho lần gửi lại | Có (đọc theo chữ của QA-293) | ISH-M05-005.4; OP-M05-10 | Có theo 005.4 (thêm 1 bản ghi); OP-M05-10 còn mở với mặc định ngược lại ("chỉ ghi ở lần gửi đầu tiên") | Không có ca (T-141 chỉ gửi một lần) | Đã có OP (không lập finding); chuyển P2 (CL-F01) |
| A-061 | DEC-141, QA-043 | Thường | User U chưa theo dõi Topic A (A có 5 người theo dõi) | U theo dõi A | U ở trạng thái đang theo dõi; số người theo dõi A = 6 | Có | ISH-M05-007.1, 007.4 | Có | T-075 | Trùng |
| A-062 | DEC-141 | Thường | U đang theo dõi A (6 người) | U bỏ theo dõi | U không theo dõi; số = 5 | Có | ISH-M05-007.2 | Có | T-076 | Trùng |
| A-063 | QA-011, DEC-126 | Quyền | Guest | Bấm theo dõi Topic | Từ chối, yêu cầu đăng nhập ("All interactions (… follow …) require login") | Có | ISH-M05-007.5 | Có | T-080 | Trùng |
| A-064 | DEC-141 | Số đếm | Topic có 0 / 1 / 37 người theo dõi | Xem Topic | Hiển thị 0 / 1 / 37 | Có | ISH-M05-007.4 | Có | T-078 (0), T-075 (1), T-079 (25) | Trùng |
| A-065 | DEC-141 | Vi phạm | Tag x | User muốn theo dõi x | Không có thao tác theo dõi Tag | Có | R7 (DEC-141) | Có | — | Không cần ca |
| A-066 | DEC-145 | Công thức | U1 theo dõi S; U2 theo dõi S và T; U3 theo dõi T | Mod gộp S vào T | T có 3 người theo dõi {U1, U2, U3}; U2 tính một lần; S không theo dõi được | Có | ISH-M05-011.3, 011.4 | Có | T-114, T-115 (5 + 8 − 2 = 11) | Trùng |
| A-067 | DEC-155, QA-289 | Thường | U theo dõi Topic A | Bài mới thuộc A trở thành khả dụng | Thông báo in-app, không email; M07 gửi, M07 quyết quy tắc gộp | Có | R5 M07 (`ISH-RT-M05.md:69`); Lý do 5.9 | Có | — | Không cần ca (hành vi của M07) |
| A-068 | DEC-142, DEC-146, DEC-154, DEC-158 | Công thức | Topic A: P1 công khai lần đầu T−3n; trong cửa sổ 4 upvote còn + 1 upvote đã rút; 3 bình luận còn (2 gốc + 1 trả lời) + 1 bình luận đang bị ẩn; bookmark: 1 của User khác tạo T−2n, 1 tạo T−10n, 1 của tác giả; 25 User khác tác giả mở trang chi tiết (1 người mở 3 lần), tác giả mở 5 lần, 40 lượt Guest. P2 công khai lần đầu T−20n; trong cửa sổ 2 upvote, 1 bình luận, 10 người xem; 1 bookmark tạo T−15n. P3 thuộc Group Private, T−1n, 10 upvote. P4 đang bị gắn cờ, T−2n. P5 công khai lần đầu T−1n, không tương tác | Tính điểm A | P1 = 2×4 + 3 + 1 + 0,1×25 + 1 = 15,5; P2 = 2×2 + 1 + 0 + 0,1×10 + 0 = 6; P3 = 0; P4 = 0; P5 = 1 → A = **22,5** | Có | ISH-M05-008.1, 008.3, 008.6, 008.13…008.17 | Có (tính theo SR cũng ra 22,5) | T-082 (17), T-144 (14), T-145 (0,7): cùng phương pháp | Trùng |
| A-069 | DEC-142 | Công thức | Topic B: P5 công khai tạo T−2n không tương tác; P6 công khai tạo T−30n không tương tác trong cửa sổ | Tính điểm B | P5 = 1 (thưởng bài mới), P6 = 0 → B = **1**; thứ hạng A (17) trên B (1) | Có | ISH-M05-008.1, 008.9 | Có | T-083 (L = 1), T-082 P3 = 0 | Trùng |
| A-070 | DEC-142 | Công thức | P1 (A-068) gắn cả Topic A và Topic B | Tính điểm A và B | P1 đóng góp 12 cho A và 12 cho B ("every post of the Topic/Tag counts") | Có | ISH-M05-008.1 | Có | T-085 | Trùng |
| A-071 | DEC-146 | Công thức | P1 có một bình luận được 3 upvote | Tính điểm | Upvote của bình luận không tính | Có | ISH-M05-008.4 | Có | T-091 | Trùng |
| A-072 | DEC-146, DEC-033 | Công thức | Bài ở bản nháp / chờ duyệt / tác giả tự ẩn / bị từ chối / đã xóa / bị Mod ẩn / đang bị gắn cờ; bài Group Public; bài của User bị khóa | Tính điểm | Chỉ bài PUBLISHED + NORMAL, không thuộc Group Private được tính → bài Group Public và bài của User bị khóa được tính, các bài kia không | Có | ISH-M05-008.3; 2.1 "Bài viết công khai" (`ISH-SR-M05.md:37`) | Có | T-088, T-089, T-090, T-156, T-157 | Trùng (r1: SR mơ hồ, AUD-06 → đã sửa) |
| A-073 | DEC-154, QA-288 | Thời gian, Công thức | P7: nháp T−10n, gửi T−8n, chờ Mod, công khai lần đầu T−6n, không tương tác; Topic chỉ có P7 | Tính điểm Topic | +1 (mốc công khai lần đầu trong cửa sổ) → 1; P7 được đếm ở tiêu chí phá hòa | Có (r1: Mơ hồ → DEC-154) | ISH-M05-008.1, 008.11; 2.1 "Trở thành công khai lần đầu" (`:39`) | Có | T-154: K = 1 | Trùng |
| A-074 | DEC-154, QA-291 | Công thức | P1 có 3 bình luận trong cửa sổ, 1 bình luận đang bị ẩn bởi kiểm duyệt; sau đó bình luận được khôi phục | Tính trước và sau khôi phục | Trước: 2 bình luận; sau: 3 | Có (r1: Mơ hồ → DEC-154) | ISH-M05-008.17 | Có | T-150 (2), T-151 (3) | Trùng |
| A-075 | DEC-146 | Công thức | P1 có bình luận gốc đã xóa (còn tombstone vì có trả lời) và 1 trả lời còn tồn tại | Tính điểm | Bình luận gốc đã xóa không tính; trả lời tính 1 | Có | ISH-M05-008.5, 008.7 | Có | T-094 (một phần) | Trùng |
| A-076 | DEC-153 | Thứ tự | Topic C điểm 10, 3 bài tính được tạo trong cửa sổ; Topic D điểm 10, 1 bài | Xếp hạng | C trên D | Có | ISH-M05-008.11 | Có | T-133 | Trùng |
| A-077 | DEC-154, QA-292 | Thứ tự | "Khác" và "Khoa học tự nhiên (Lý/Hóa/Sinh)" cùng điểm, cùng số bài | Xếp hạng | "Khác" trước (a < o theo bảng chữ cái tiếng Việt) | Có (r1: Mơ hồ → DEC-154) | ISH-M05-008.11; 2.1 (`:62`) | Có | T-158: "Khác" trước | Trùng |
| A-078 | DEC-051, DEC-150 | Thường | Tag x có điểm cao nhất, rồi bị vô hiệu hóa; sau đó mở lại | Tính điểm sau mỗi lần | Khi vô hiệu: x không có trong xếp hạng Tag. Khi mở lại: x xếp hạng lại | Có | ISH-M05-012.3, 008.2 | Có | T-119 (vô hiệu hóa); không có ca mở lại rồi xếp hạng | Trùng một phần |
| A-079 | DEC-145, DEC-049 | Công thức | S gộp vào T; bài Q gắn {S, T} tạo T−1n | Tính điểm T | S không xếp hạng; Q tính một lần cho T (Q còn 1 Topic là T) | Có (suy ra) | ISH-M05-011.1, 008.1 | Có | T-110, T-113 | Trùng |
| A-080 | DEC-052 | Thời gian | Upvote mới vào P1 lúc T+1 phút | Xem điểm trước lần tính lại kế tiếp | Điểm chưa đổi cho tới lần tính lại (15–30 phút; chi tiết chu kỳ thuộc R2) | Có | R2 | Có | — | Không cần ca |
| A-081 | QA-235, DEC-052 | Số đếm | Tag z hoạt động, gắn trên một bài công khai đăng T−20n, không tương tác trong cửa sổ → điểm 0 | Xếp hạng Trending Tag | z có trong xếp hạng ("Không đặt ngưỡng") | Có | ISH-M05-008.19 | Có | T-153: "anova" điểm 0 có trong bảng | Trùng (Tag không có bài được tính nào: xem A-119) |
| A-082 | DEC-049, DEC-090 | Quyền | Topic "Góc Chill" | Mod (rồi Admin) đổi tên thành "Góc thư giãn" | Danh mục và mọi bài dùng tên mới | Có | ISH-M05-010, 010.1 | Có | T-104 | Trùng |
| A-083 | DEC-049 | Quyền | — | User thường đổi tên Topic | Từ chối (suy ra) | Có | ISH-M05-010.3 | Có | T-106 | Trùng |
| A-084 | DEC-049 | Vi phạm | Có Topic "Tin học" | Mod đổi tên "Khác" thành "Tin học" (trùng) hoặc thành tên rỗng | Cách 1: từ chối. Cách 2: chấp nhận (hai Topic cùng tên / Topic không tên). Nguồn không nêu ràng buộc tên Topic | Mơ hồ | ISH-M05-010; OP-M05-04 | Mơ hồ, đã có OP-M05-04 | — | Đã có OP (không lập finding) |
| A-085 | DEC-049, DEC-145 | Thường | S có 4 bài, 2 người theo dõi | Mod gộp S vào T | 4 bài chuyển sang T; S biến khỏi danh mục (không chọn, gợi ý, xếp hạng, theo dõi được); người theo dõi chuyển sang T | Có | ISH-M05-011, 011.2, 011.3 | Có | T-111, T-112, T-114 | Trùng |
| A-086 | DEC-049 | Biên | Bài Q gắn {S, T, U} | Gộp S vào T | Q còn {T, U} | Có (suy ra) | ISH-M05-011 | Có | — | Không có ca của Author |
| A-087 | DEC-049 | Quyền | — | User thường gộp Topic | Từ chối (suy ra) | Có | ISH-M05-011.5 | Có | T-116 | Trùng |
| A-088 | DEC-049, ISS-084 | Vi phạm | — | Mod/Admin xóa Topic | Từ chối ("No delete") | Có | ISH-M05-001.5 | Có | T-108, T-109 | Trùng |
| A-089 | DEC-140 | Thường | — | User chọn Lớp/Khối cho bài | Không thuộc M05 (M03 F-POST-09, M02) | Có | R5 (M03, M02) | Có | — | Không cần ca |
| A-090 | QA-269 | Thường | AI bật | User bấm gợi ý | Không gợi ý Tag (chỉ Topic) | Có | R7 (QA-269) | Có | — | Không cần ca |
| A-091 | DEC-146, DEC-032, DEC-033 | Công thức | P15 đã xuất bản, đang bị gắn cờ chờ Mod, T−1n, 2 upvote | Tính điểm Topic của P15 | 0 | Có | ISH-M05-008.3; 2.1 (`:37`) | Có | T-156: K = 0 | Trùng (r1: AUD-06 → đã sửa) |
| A-092 | DEC-146, DEC-031 | Công thức | P16 tác giả tự ẩn, trước đó đã công khai, T−1n, 2 upvote | Tính điểm | 0 | Có | ISH-M05-008.3; 2.1 (`:37`) | Có | T-157: K = 0 | Trùng (r1: AUD-06 → đã sửa) |
| A-093 | DEC-145 | Vi phạm | S đã gộp vào T | User yêu cầu theo dõi S | Từ chối ("can no longer be … followed") | Có | ISH-M05-011.7 (ngoại lệ cụ thể của 007.1) | Có | T-161: từ chối | Trùng (r1: AUD-03 → đã sửa); quan hệ 007.1/011.7 chuyển P2 |
| A-094 | DEC-145, QA-235 | Thường | S đã gộp vào T | Xếp hạng Topic | S không có trong xếp hạng | Có | ISH-M05-011.6, 008.18 ("mọi Topic trong danh mục Topic") | Có | T-160: "Góc Chill" không có trong bảng | Trùng (r1: AUD-03 → đã sửa) |
| A-095 | DEC-048, QA-267 (cho yêu cầu ISH-M05-001.4) | Vi phạm | Admin | Thêm Topic thứ 12 | Không có thao tác thêm ("11, final"; "11 giá trị cố định") | Có | ISH-M05-001.4 | Có | T-005 | Trùng |
| A-096 | DEC-051 (cho yêu cầu ISH-M05-006.10 Suy ra) | Lặp | Bài có 5 Tag gồm "bayes" | Gắn thêm "BAYES" | Bài vẫn 5 Tag, không vượt giới hạn | Có (suy ra) | ISH-M05-006.10 | Có | T-069, T-070 | Trùng |
| A-097 | DEC-141 (cho yêu cầu ISH-M05-007.6 Suy ra) | Lặp | U đang theo dõi A (1 người) | U theo dõi A lần nữa | Vẫn 1 người | Có (suy ra) | ISH-M05-007.6 | Có | T-081 | Trùng |
| A-098 | DEC-049 (cho ISH-M05-010.1, 010.2 Suy ra) | Thường | "Góc Chill" có 15 bài, 12 người theo dõi | Đổi tên | Cùng 15 bài, cùng 12 người | Có (suy ra) | ISH-M05-010.1, 010.2 | Có | T-104, T-105 | Trùng |
| A-099 | DEC-156 | Biên | Bài đã gửi (chờ duyệt), 1 Topic | Tác giả bỏ Topic duy nhất rồi lưu | Từ chối thay đổi; bài giữ Topic | Có | ISH-M05-002.6 | Có | T-012: từ chối | Trùng |
| A-100 | DEC-157, QA-293 | Thường | Gợi ý G1 {Toán học, Tin học} rồi G2 {Tin học, Khác}, cả hai còn mới | Gửi bài với {Tin học} | 1 bản ghi: G2 so với {Tin học}; G1 không ghi | Có | ISH-M05-005.1, 005.4 | Có | T-142, T-141 | Trùng |
| A-101 | DEC-157, DEC-148 | Thời gian | G1, G2 còn mới; sau G2 tác giả sửa tiêu đề | Gửi bài | Mọi gợi ý đều cũ → 0 bản ghi | Có | ISH-M05-005.2 | Có | T-053 (một gợi ý) | Trùng |
| A-102 | DEC-142, DEC-158 | Công thức | Topic B chỉ có P6 công khai lần đầu T−30n; trong cửa sổ chỉ có 3 người xem | Tính điểm B; xếp hạng cùng A (A-068) | B = 0,3 (thực thể cũ, chỉ có lượt xem); A (22,5) trên B | Có | ISH-M05-008.13, 008.9 | Có | T-145: L = 0,7 | Trùng |
| A-103 | DEC-158 | Thời gian | V mở trang chi tiết P lúc T−8n và T−1n; W chỉ mở lúc T−8n | Tính phần người xem của P | V tính 1 (0,1); W không tính | Có | ISH-M05-008.14 | Có | T-147 | Trùng |
| A-104 | DEC-158 | Quyền | Tác giả mở bài của mình; Guest mở bài | Tính số người xem | Không tính cả hai | Có | ISH-M05-008.14, 008.15 | Có | T-146, T-148 | Trùng |
| A-105 | DEC-158 | Thời gian | Bookmark của User khác tạo T−2n, bị bỏ T−1n | Tính số bookmark | 0 (không còn giữ) | Có | ISH-M05-008.16 | Có | T-149 (User C) | Trùng |
| A-106 | DEC-158 | Thời gian | Bookmark tạo T−10n, còn giữ | Tính số bookmark | 0 (tạo ngoài cửa sổ) | Có | ISH-M05-008.16 | Có | T-149 (User G) | Trùng |
| A-107 | DEC-154, DEC-031 | Thời gian | P8 công khai lần đầu T−10n, tác giả tự ẩn T−9n, hiện lại T−2n; 1 bình luận lúc T−1n | Tính điểm | Không +1; bình luận được tính → 1 | Có | ISH-M05-008.1, 008.13 | Có | T-155 (bị Mod ẩn rồi khôi phục): 0 | Trùng |
| A-108 | DEC-154 | Thứ tự | Tag "đạohàm" và "elip" cùng điểm, cùng số bài | Xếp hạng | "đạohàm" trước (đ < e) | Có | ISH-M05-008.12; 2.1 (`:62`) | Có | T-159 ("d" trước "đ") | Trùng |
| A-109 | DEC-154, QA-292, DEC-153 | Thứ tự | Tag "2k8" và "anh" cùng 1 điểm, cùng 1 bài được tính trở thành công khai lần đầu trong cửa sổ | Xếp hạng Trending Tag | Cách 1 (chữ số trước chữ cái): "2k8" trước. Cách 2 (chữ số sau chữ cái): "anh" trước. Bảng "a ă â b c d đ e ê …" không có chữ số | **Mơ hồ** | ISH-M05-008.12; 2.1 (`:62`) | Mơ hồ (2.1 chỉ liệt kê 29 chữ cái) | Không có ca | Không có ca của Author (P3-01) |
| A-110 | DEC-154, QA-292 | Thứ tự | Tag "nghỉhè" và "nghĩhè" (khác nhau chỉ ở dấu hỏi/ngã) cùng điểm, cùng số bài | Xếp hạng | Cách 1 (hỏi trước ngã): "nghỉhè" trước. Cách 2 (ngã trước hỏi, thứ tự của một số từ điển): "nghĩhè" trước. Nguồn chỉ liệt kê chữ cái, không nêu dấu thanh | **Mơ hồ** (nhỏ) | ISH-M05-008.12; 2.1 (`:62`) | Mơ hồ | Không có ca | Không có ca của Author (P3-01) |
| A-111 | DEC-159 | Chuyển trạng thái | S đã gộp vào T | Mod gộp U vào S (đích đã bị loại) | Từ chối; báo Topic không tồn tại; danh mục và bài viết giữ nguyên | Có | ISH-M05-011.8, 011.9 | Có | T-162, T-164 | Trùng |
| A-112 | DEC-159 | Chuyển trạng thái | S đã gộp vào T | Admin gộp S vào U (nguồn đã bị loại) | Từ chối; danh mục và bài viết giữ nguyên | Có | ISH-M05-011.8 | Có | T-163 | Trùng |
| A-113 | DEC-159 | Vi phạm | — | Mod gộp T vào T | Từ chối; không đổi | Có | ISH-M05-011.10 | Có | T-165 | Trùng |
| A-114 | DEC-142, DEC-158 | Công thức | Tag x gắn trên P1 (A-068) và P6 (A-102) | Tính điểm x | 15,5 + 0,3 = 15,8 | Có | ISH-M05-008.2, 008.13 | Có | T-086 (cùng phương pháp) | Trùng |
| A-115 | QA-011 | Quyền | Bài công khai có Topic {Toán học, Tin học} | Guest mở bài | Thấy hai Topic ("Xem … AI Classification trên post") | Có | ISH-M05-002.10 (chủ sở hữu: OP-M05-12) | Có | T-138 | Trùng |
| A-116 | DEC-148 | Thời gian | Gợi ý đã cũ (đã sửa tiêu đề) | Tác giả thêm tệp đính kèm | Gợi ý vẫn cũ (đổi tệp đính kèm không tính) | Có | ISH-M05-003.11 | Có | T-136 | Trùng (r1: AUD-08 → đã sửa) |
| A-117 | QA-011, DEC-051 | Quyền | Bài công khai có Tag "bayes" (hoạt động) và "spam" (bị vô hiệu hóa) | Guest mở bài | Thấy "bayes"; không thấy "spam" | Có | ISH-M05-006.16 | Có | T-143 | Trùng |
| A-118 | QA-235 | Số đếm | Topic "Góc Chill" trong danh mục, điểm 0 | Xếp hạng Topic | Có mặt (không ngưỡng) | Có | ISH-M05-008.18 | Có | T-152 | Trùng |
| A-119 | QA-235, DEC-051, DEC-146, DEC-126 | Phạm vi dữ liệu | Tag "đềthi12a1" mới tạo, chỉ gắn trên 2 bài trong một Group Private (hoặc chỉ trên một bản nháp chưa gửi) | Guest xem xếp hạng Trending Tag | Cách 1: "đềthi12a1" có trong xếp hạng với điểm 0 (mọi Tag tồn tại, không ngưỡng). Cách 2: không có (chỉ Tag có ít nhất một bài viết được tính). Nguồn không nói Tag được tạo lúc nào và "không ngưỡng" có áp dụng cho Tag không có bài nào được tính hay không | **Mơ hồ** | ISH-M05-008.19, 006.2 | Có: SR chọn cách 1 ("mọi Tag hoạt động"; Tag tạo ngay khi gắn, kể cả trên bản nháp) | T-153 không nêu nguồn gốc Tag | Không có ca của Author (P3-02) |

Tổng: 119 ca. Nguồn còn `Mơ hồ`: A-023 (nhỏ), A-024 (OP-M05-05), A-044 (nhỏ), A-055 (OP-M05-02), A-084 (OP-M05-04), **A-109 và A-110 (P3-01)**, **A-119 (P3-02)**. Các ca nguồn `Mơ hồ` ở vòng 1 nay đã xác định nhờ DEC-154…157: A-006, A-060, A-073, A-074, A-077, A-081. Ca có nguồn xác định mà SR `Mơ hồ` hoặc `Không`: không còn (vòng 1 có A-072, A-091…A-094).

## 2. Quét khung hành vi

Bảng đầy đủ của vòng 1 (`audit-tests-M05-r1.md` mục 2) vẫn dùng cho các ô không đổi. Dưới đây là các ô đổi ở vòng 2. Cột 1–4 dựng từ nguồn trước khi mở SR v0.2; cột 5–7 điền sau.

| Tính năng | Câu hỏi (1–7, RULES §4.7) | Nguồn nói gì | Loại (a/b/c/d) | SR (ID yêu cầu hoặc "—") | Selfcheck của Author (loại) | Kết luận |
|---|---|---|---|---|---|---|
| F1 Danh mục Topic | 1 Ai | Guest xem danh sách Topic và Tag (QA-011) | a | 001.3; phần Tag ở R5 (`ISH-RT-M05.md:64`) | a | Khớp (AUD-04 vòng 1 đã xử lý) |
| F2 Gắn Topic | 2 Thời điểm | Tối thiểu 1 Topic kiểm khi gửi và khi lưu thay đổi của bài đã gửi; bản nháp lưu được khi chưa có Topic (DEC-156) | a | 002, 002.5, 002.6, 002.11 | c→hỏi (ISS-230) | Khớp (AUD-16 đã sửa) |
| F2 | 3 Kết quả | Topic hiển thị trên bài, kể cả cho Guest (QA-011) | a | 002.10; chủ sở hữu ở OP-M05-12 | a | Khớp |
| F4 Gợi ý Topic | 5 | Đổi tệp đính kèm không làm đổi trạng thái gợi ý (DEC-148) | a | 003.11 | c→hỏi | Khớp |
| F5 Phản hồi | 3 | Chỉ lấy gợi ý gần nhất; một bản ghi mỗi lần gửi (DEC-157) | a | 005.1, 005.4 | c→hỏi (ISS-233) | Khớp; quan hệ với OP-M05-10 chuyển P2 |
| F6 Theo dõi Topic | 5 | Bài mới trong Topic → thông báo in-app (DEC-155), M07 gửi | a | R5 M07 (`ISH-RT-M05.md:69`) | c→hỏi (ISS-229) | Khớp |
| F6 | 4 | Topic nguồn sau khi gộp không theo dõi được (DEC-145) | a/b | 011.7 | a | Khớp (AUD-03 đã sửa) |
| F7 Trending | 3 Công thức | Cộng 1 × bookmark và 0,1 × người xem; định nghĩa người xem và bookmark (DEC-158) | a | 008.13…008.16 | c→hỏi (ISS-234) | Khớp (tính tay ở A-068, A-102) |
| F7 | 4 Cửa sổ | Mốc trở thành công khai lần đầu (DEC-154) | a | 008.1, 008.2, 008.11, 008.12; 2.1 | c→hỏi (ISS-228) | Khớp (AUD-01 đã sửa) |
| F7 | 5 | Bình luận đang bị ẩn không tính; được khôi phục thì tính lại (DEC-154) | a | 008.17 | c→hỏi (ISS-231) | Khớp (AUD-14 đã sửa) |
| F7 | 5 | Bài được tính = PUBLISHED + NORMAL, không thuộc Group Private (DEC-146) | a | 008.3; 2.1 (`:37`, `:38`) | c→hỏi | Khớp (AUD-06 đã sửa) |
| F7 | 3 Thứ tự | Bảng chữ cái tiếng Việt, không phân biệt hoa–thường (DEC-154). **Chưa nêu vị trí chữ số, ký tự ngoài chữ cái và thứ tự dấu thanh** (A-109, A-110) | a; **c** | 008.11, 008.12; 2.1 (`:62`) | c→hỏi (ISS-232); không nhắc phần còn lại | **GAP (P3-01)** |
| F7 | 5 Đối tượng liên quan | "Không ngưỡng" (QA-235) cộng Tag tự tạo (DEC-051): Tag chỉ có trên bản nháp, trên bài Group Private hay bài chưa công khai có vào xếp hạng không (A-119) | **c** | 008.19 ("mọi Tag hoạt động"), 006.2 | a (chỉ nhắc Tag vô hiệu hóa và Topic nguồn, `selfcheck-M05.md:117`) | **GAP (P3-02)** |
| F7 | 5 | Topic nguồn sau khi gộp không được xếp hạng (DEC-145) | a | 011.6, 008.18 | a | Khớp (AUD-03 đã sửa) |
| F9 Gộp Topic | 4 Giới hạn | Chỉ gộp hai Topic khác nhau còn trong danh mục; vi phạm thì từ chối, không đổi gì, báo Topic không tồn tại (DEC-159) | a, b | 011.8, 011.9, 011.10; R3 | c→hỏi (ISS-236) | Khớp |
| F11 Tag | 6 | Vô hiệu hóa Tag đang bị vô hiệu hóa, mở lại Tag đang hoạt động | d (từ chối hay bỏ qua đều cho cùng trạng thái quan sát được) | 012.1, 012.5 | a (T-166, T-167) | Không phải finding |

Điểm nhỏ (ghi chú, không lập finding riêng): A-044 (sửa văn bản rồi hoàn nguyên); A-023 (chữ "#x" của Tag bị vô hiệu hóa sau khi gửi); A-024 phần thứ hai (gần OP-M05-05); hai cách bỏ dấu của cùng một tiếng ("hoá"/"hóa") tạo hai Tag khác nhau (gần OP-M05-09). Bình luận của chính tác giả vẫn được đếm (DEC-146 "all root comments and replies", khác với người xem và bookmark ở DEC-158 có loại tác giả): nguồn xác định, chỉ ghi nhận. Upvote của tác giả không phát sinh vì tự vote bị cấm (QA-201).
