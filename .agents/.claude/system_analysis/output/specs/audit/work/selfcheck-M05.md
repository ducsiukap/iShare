# Selfcheck — ISH-SR-M05 phiên bản 0.6
<!-- [Vietnamese Doc] -->

Ngày: 2026-10-05 · Tác giả: Phạm Văn Đức

Tệp làm việc của Author (RULES §10: Author không tự chấm 45 mục checklist; Auditor chấm). Bản này theo khuôn mới; nội dung cũ (45 mục, bản 0.4) đã được lưu ngoài thư mục làm việc.

## 1. Kết quả script

| Lệnh | Kết quả |
|---|---|
| `inventory.py` (chạy lại sau lần ghi register cuối) | OWNED=146, REFERENCING=22; ID kế tiếp: ISS-255, QA-315, DEC-170 |
| `check_sr.py --inventory … --registers … --tests …` | ERROR=0, WARN=0, INFO=35; 209 ca kiểm cho 116 yêu cầu cấp dưới |

## 2. Ca kiểm (RULES §11)

| Việc | Kết quả |
|---|---|
| Mọi yêu cầu cấp dưới có ít nhất một ca (TST-01) | 116/116 |
| Cột "Giả định cần thêm" còn nội dung | 0; T-199, T-200 đã bỏ cùng OP-M05-13, OP-M05-14 vì nguồn chưa nói (RULES §3.3) |
| Mỗi công thức, cửa sổ thời gian, hằng số có ví dụ số tính tay | Không đổi so với v0.4 (008.x); ca T-183/T-184 mới có số đếm cụ thể |
| Yêu cầu ở mục 5.2 có ca "Chuyển trạng thái" (TST-07) | 11/11 (T-201…T-211) |
| Đã đọc lại từng "Then" của ca mới và ca sửa (T-057, T-170, T-176, T-181, T-212): suy ra được duy nhất từ câu yêu cầu | Có |

## 3. Quét khung hành vi (RULES §4.7)

Mỗi tính năng một khối bảy dòng; loại ∈ {a nguồn nêu, b suy ra, c nguồn im lặng, d không áp dụng}. Các ô đổi ở v0.5 ghi "v0.5".

| Tính năng | Câu hỏi | Loại | Kết quả (ID yêu cầu, ID câu hỏi/`OP`, hoặc lý do) |
|---|---|---|---|
| 5.3 Danh mục Topic | 1 Ai được làm | a | Mọi người dùng kể cả Guest xem (ISH-M05-001.3) |
| 5.3 Danh mục Topic | 2 Ngữ cảnh | a | Khởi tạo hệ thống, xem danh sách (001.1, 001.3) |
| 5.3 Danh mục Topic | 3 Kết quả chính | a | 11 Topic một tầng (001.1, 001.2) |
| 5.3 Danh mục Topic | 4 Giới hạn và vi phạm | a | Đúng 11 khi khởi tạo; không thêm Topic (001.4) |
| 5.3 Danh mục Topic | 5 Hệ quả lên đối tượng liên quan | d | Danh mục chỉ đổi qua đổi tên/gộp, xét ở 5.12, 5.13 |
| 5.3 Danh mục Topic | 6 Vòng đời | a | Không thêm (001.4), không xóa (010.4), đổi tên (010), gộp (011) |
| 5.3 Danh mục Topic | 7 Bất thường | d | Không phụ thuộc dịch vụ ngoài |
| 5.4 Gán Topic | 1 Ai được làm | a | Tác giả (002.1, 002.9); Mod/Admin (009); người khác bị từ chối (009.2) |
| 5.4 Gán Topic | 2 Ngữ cảnh | c→hỏi | Khi tạo bài (DEC-049); khi sửa bài đã gửi — đã hỏi Q-3 → ISS-213/DEC-144 (002.9) |
| 5.4 Gán Topic | 3 Kết quả chính | a | Bài viết có 1–3 Topic từ danh mục (002, 002.2) |
| 5.4 Gán Topic | 4 Giới hạn và vi phạm | a/b | Min 1, max 3 (002.4, 002.7) và từ chối (002.5, 002.6, 002.8); lệch DRAFT §3.4 — đã hỏi Q-1 → ISS-211/DEC-143 |
| 5.4 Gán Topic | 5 Hệ quả lên đối tượng liên quan | a | Điểm Trending theo Topic hiện tại của bài (008.1) |
| 5.4 Gán Topic | 6 Vòng đời | a | Đổi khi sửa (002.9), Mod/Admin đổi (009) — Q-3 |
| 5.4 Gán Topic | 7 Bất thường | d | Chọn tay không phụ thuộc AI; nhánh AI ở 5.6 |
| 5.5 Gợi ý Topic bằng AI | 1 Ai được làm | a | Tác giả bài viết (003) |
| 5.5 Gợi ý Topic bằng AI | 2 Ngữ cảnh | a/c | Khi soạn bài mới, chỉ khi yêu cầu (003, 003.1); khi sửa bài đã gửi thì không có gợi ý (003.15, DEC-167; v0.5) |
| 5.5 Gợi ý Topic bằng AI | 3 Kết quả chính | c→hỏi | Topic gợi ý được chọn sẵn, thay thế lựa chọn đang có — Q-9 → ISS-219/DEC-148 (003.4) |
| 5.5 Gợi ý Topic bằng AI | 4 Giới hạn và vi phạm | c→hỏi | ≤3 Topic (003.3); ngưỡng 10 tiếng tiêu đề + nội dung — Q-8 → ISS-218/DEC-147 (003.6, 003.7); 10/phút (003.8, 003.9) |
| 5.5 Gợi ý Topic bằng AI | 5 Hệ quả lên đối tượng liên quan | c→hỏi | Sửa tiêu đề/nội dung làm gợi ý cũ, tệp đính kèm thì không — Q-10 → ISS-220/DEC-148 (003.10, 003.11) |
| 5.5 Gợi ý Topic bằng AI | 6 Vòng đời | a | Gợi ý lại khi cũ (003.13); không chặn gửi bài (003.14) |
| 5.5 Gợi ý Topic bằng AI | 7 Bất thường | a | Xem 5.6 |
| 5.6 AI không khả dụng | 1 Ai được làm | a | Tác giả tự chọn (004) |
| 5.6 AI không khả dụng | 2 Ngữ cảnh | a | AI tắt (004.1); lỗi sau thử lại (004.2) |
| 5.6 AI không khả dụng | 3 Kết quả chính | a | Thông báo, giữ lựa chọn, vẫn gửi được (004.2–004.4) |
| 5.6 AI không khả dụng | 4 Giới hạn và vi phạm | c→hỏi | Kết quả có Topic ngoài danh mục — Q-11 → ISS-221/DEC-149 (004.5, 004.6); hơn 3 Topic hợp lệ — Q-15 → ISS-225/DEC-152 (004.7) |
| 5.6 AI không khả dụng | 5 Hệ quả lên đối tượng liên quan | a | Không có phản hồi để ghi (005.3, T-056) |
| 5.6 AI không khả dụng | 6 Vòng đời | d | Không có đối tượng được tạo |
| 5.6 AI không khả dụng | 7 Bất thường | a | Chính là tính năng này (DEC-099, DEC-132) |
| 5.7 Phản hồi gợi ý | 1 Ai được làm | a | Hệ thống, khi tác giả gửi bài (005) |
| 5.7 Phản hồi gợi ý | 2 Ngữ cảnh | a/c | Lúc gửi bài (005.1); gửi lại sau khi bị từ chối → OP-M05-10 |
| 5.7 Phản hồi gợi ý | 3 Kết quả chính | a | Ghi gợi ý gần nhất và lựa chọn cuối (005.1) |
| 5.7 Phản hồi gợi ý | 4 Giới hạn và vi phạm | a/b | Chỉ khi gợi ý còn mới (005.2); không có gợi ý thì không ghi (005.3) |
| 5.7 Phản hồi gợi ý | 5 Hệ quả lên đối tượng liên quan | a | Dùng cho đánh giá AI → R5 M13 |
| 5.7 Phản hồi gợi ý | 6 Vòng đời | d | Bản ghi không có thao tác người dùng sau khi tạo |
| 5.7 Phản hồi gợi ý | 7 Bất thường | a | AI lỗi → không nhận gợi ý → không ghi (005.3) |
| 5.8 Gắn Tag | 1 Ai được làm | a | Tác giả; người khác (kể cả Mod/Admin) bị từ chối (006.12) — Q-3 |
| 5.8 Gắn Tag | 2 Ngữ cảnh | a | Khi tạo (006.1), khi sửa (006.11) |
| 5.8 Gắn Tag | 3 Kết quả chính | a | Gắn Tag, tạo Tag mới không cần duyệt (006.2) |
| 5.8 Gắn Tag | 4 Giới hạn và vi phạm | c→hỏi | 0–5 Tag — Q-2 → ISS-212/DEC-143 (006.3–006.5); không tính # — Q-13 → ISS-223/DEC-150 (006.6, 006.7); chuẩn hóa tên — Q-16 → ISS-226/DEC-152 (006.13–006.15); khoảng trắng (006.8 b) |
| 5.8 Gắn Tag | 5 Hệ quả lên đối tượng liên quan | a/c | Cùng Tag không phân biệt hoa thường (006.9), gắn lại giữ một lần (006.10 b); Tag vô hiệu hóa vẫn tính vào 5 (006.17); hiển thị chữ thường (006.18); ký tự cho phép (006.8) — DEC-166, v0.5 |
| 5.8 Gắn Tag | 6 Vòng đời | a | Tác giả đổi khi sửa (006.11); Tag không đổi tên/gộp/xóa (012.9–012.11) |
| 5.8 Gắn Tag | 7 Bất thường | d | Không phụ thuộc dịch vụ ngoài |
| 5.9 Theo dõi Topic | 1 Ai được làm | a | Người dùng đã đăng nhập (007); Guest bị từ chối (007.5) |
| 5.9 Theo dõi Topic | 2 Ngữ cảnh | a | Trên Topic (DEC-141), bất kỳ lúc nào |
| 5.9 Theo dõi Topic | 3 Kết quả chính | a | Trạng thái theo dõi, số người theo dõi (007.1–007.4) |
| 5.9 Theo dõi Topic | 4 Giới hạn và vi phạm | b | Không có giới hạn số lượng trong nguồn; theo dõi lặp không tăng số (007.6) |
| 5.9 Theo dõi Topic | 5 Hệ quả lên đối tượng liên quan | a/c | Thông báo bài mới → R5 M07; tab Following → R5 M14; số người theo dõi hiển thị cho mọi người (007.4), không tính tài khoản đã xóa (007.8) — DEC-168, v0.5 |
| 5.9 Theo dõi Topic | 6 Vòng đời | a | Bỏ theo dõi (007.2); gộp Topic chuyển người theo dõi (011.3) |
| 5.9 Theo dõi Topic | 7 Bất thường | d | Không phụ thuộc dịch vụ ngoài |
| 5.10 Trending | 1 Ai được làm | a | Hệ thống tính; người xem → R5 M14 (Guest xem được, DEC-126) |
| 5.10 Trending | 2 Ngữ cảnh | a | 168 giờ tính lùi từ lúc tính (008.8); chu kỳ 15–30 phút → R2 |
| 5.10 Trending | 3 Kết quả chính | c→hỏi | Thứ tự xếp hạng và phá hòa — Q-17 → ISS-227/DEC-153 (008.9–008.12) |
| 5.10 Trending | 4 Giới hạn và vi phạm | c→hỏi | Bài nào được tính — Q-6 → ISS-216/DEC-146 (008.3); tương tác nào — Q-7 → ISS-217/DEC-146 (008.4–008.7) |
| 5.10 Trending | 5 Hệ quả lên đối tượng liên quan | a | Tag vô hiệu hóa bị loại (012.3); Topic nguồn sau gộp bị loại (011.2) |
| 5.10 Trending | 6 Vòng đời | d | Không có thao tác người dùng trên bảng xếp hạng |
| 5.10 Trending | 7 Bất thường | d | Không phụ thuộc dịch vụ ngoài; lý do tính năng đã có (DEC-169, v0.5) |
| 5.11 Mod/Admin đổi Topic | 1 Ai được làm | a | Mod, Admin (009) — Q-3; Guest/User khác bị từ chối (009.2) |
| 5.11 Mod/Admin đổi Topic | 2 Ngữ cảnh | a | Mọi bài viết, bất kỳ lúc nào (DEC-144 "any post") |
| 5.11 Mod/Admin đổi Topic | 3 Kết quả chính | a | Topic mới thay Topic cũ (009.1) |
| 5.11 Mod/Admin đổi Topic | 4 Giới hạn và vi phạm | a | Giới hạn 1–3 áp dụng (002.6, 002.8, T-013, T-016) |
| 5.11 Mod/Admin đổi Topic | 5 Hệ quả lên đối tượng liên quan | c | Không đặc tả: thông báo cho tác giả khi Mod đổi Topic thuộc M07, ghi ở routing R5 (DEC-168, DEC-065); thông báo "bài mới" cho người theo dõi Topic đích: nguồn chưa nói |
| 5.11 Mod/Admin đổi Topic | 6 Vòng đời | d | Không tạo đối tượng mới |
| 5.11 Mod/Admin đổi Topic | 7 Bất thường | d | Không phụ thuộc dịch vụ ngoài |
| 5.12 Đổi tên Topic | 1 Ai được làm | a | Mod, Admin (010); Guest/User bị từ chối (010.3) |
| 5.12 Đổi tên Topic | 2 Ngữ cảnh | d | Nguồn không giới hạn thời điểm |
| 5.12 Đổi tên Topic | 3 Kết quả chính | a | Tên mới (010) |
| 5.12 Đổi tên Topic | 4 Giới hạn và vi phạm | c | Tên rỗng (010.7) hoặc trùng (010.8) bị từ chối — DEC-168; tên chỉ gồm ký tự trắng và cắt khoảng trắng đầu/cuối: nguồn chưa nói, không đặc tả |
| 5.12 Đổi tên Topic | 5 Hệ quả lên đối tượng liên quan | b | Bài viết và người theo dõi giữ nguyên (010.1, 010.2) |
| 5.12 Đổi tên Topic | 6 Vòng đời | a | Không xóa Topic (010.4) |
| 5.12 Đổi tên Topic | 7 Bất thường | d | Không phụ thuộc dịch vụ ngoài |
| 5.13 Gộp Topic | 1 Ai được làm | a | Mod, Admin (011); Guest/User bị từ chối (011.5) |
| 5.13 Gộp Topic | 2 Ngữ cảnh | d | Nguồn không giới hạn thời điểm |
| 5.13 Gộp Topic | 3 Kết quả chính | a | Bài chuyển sang Topic đích (011) |
| 5.13 Gộp Topic | 4 Giới hạn và vi phạm | b | Bài có cả hai Topic giữ đích một lần (011.1) |
| 5.13 Gộp Topic | 5 Hệ quả lên đối tượng liên quan | c→hỏi | Topic nguồn — Q-4 → ISS-214/DEC-145 (011.2); người theo dõi — Q-5 → ISS-215/DEC-145 (011.3, 011.4) |
| 5.13 Gộp Topic | 6 Vòng đời | a | Topic nguồn là trạng thái cuối (5.2) |
| 5.13 Gộp Topic | 7 Bất thường | d | Không phụ thuộc dịch vụ ngoài |
| 5.14 Vô hiệu hóa/mở lại Tag | 1 Ai được làm | a | Mod, Admin (012); Guest/User bị từ chối (012.7, 012.8) |
| 5.14 Vô hiệu hóa/mở lại Tag | 2 Ngữ cảnh | a | Tình huống khẩn cấp, do Mod/Admin đánh giá → R4 |
| 5.14 Vô hiệu hóa/mở lại Tag | 3 Kết quả chính | a | Ẩn trên bài (012.1), loại khỏi Trending (012.3) |
| 5.14 Vô hiệu hóa/mở lại Tag | 4 Giới hạn và vi phạm | a | Gõ lại tên không gắn (012.4) |
| 5.14 Vô hiệu hóa/mở lại Tag | 5 Hệ quả lên đối tượng liên quan | a/c | Liên kết giữ (012.2); autocomplete/duyệt → R5 M06/M14; Tag vô hiệu hóa vẫn tính vào 5 Tag (006.17, v0.5) |
| 5.14 Vô hiệu hóa/mở lại Tag | 6 Vòng đời | c→hỏi | Mở lại — Q-12 → ISS-222/DEC-150 (012.5, 012.6); không đổi tên/gộp/xóa (012.9–012.11) |
| 5.14 Vô hiệu hóa/mở lại Tag | 7 Bất thường | d | Không phụ thuộc dịch vụ ngoài |

Bổ sung v0.2 (các ô thay đổi so với bảng trên):

| Tính năng | Câu hỏi | Loại | Kết quả |
|---|---|---|---|
| 5.4 Gán Topic (v0.2) | 2 Ngữ cảnh | c→hỏi | Lưu nháp không Topic — AUD-16 → ISS-230/DEC-156 (002.11, 002.6) |
| 5.4 Gán Topic (v0.2) | 3 Kết quả chính | a | Hiển thị Topic trên bài cho mọi người kể cả Guest (002.10, QA-011); M05 sở hữu việc hiển thị (DEC-169, v0.5) |
| 5.6 Xử lý kết quả và sự cố (v0.2) | 3 Kết quả chính | a | Đổi tên tính năng; cấp trên bao quát 004.5–004.7 |
| 5.7 Phản hồi gợi ý (v0.2) | 3 Kết quả chính | c→hỏi | Gợi ý gần nhất, một bản ghi mỗi lần gửi — AUD-10 → ISS-233/DEC-157 (005.1, 005.4) |
| 5.8 Gắn Tag (v0.2) | 3 Kết quả chính | a | Hiển thị Tag hoạt động trên bài (006.16, QA-011) |
| 5.9 Theo dõi Topic (v0.2) | 5 Hệ quả lên đối tượng liên quan | c→hỏi | Thông báo bài mới — AUD-02 → ISS-229/DEC-155 (R5 M07) |
| 5.10 Trending (v0.2) | 4 Giới hạn và vi phạm | c→hỏi | Mốc bài mới — ISS-228; bình luận ẩn — ISS-231; người xem/bookmark — ISS-234 (008.13–008.17); không ngưỡng (008.18, 008.19) |
| 5.10 Trending (v0.2) | 3 Kết quả chính | c→hỏi | Thứ tự tên tiếng Việt — ISS-232/DEC-154 (008.11, 008.12) |
| 5.13 Gộp Topic (v0.2) | 4 Giới hạn và vi phạm | c→hỏi | Gộp với Topic đã loại hoặc trùng — ISS-236/DEC-159 (011.8–011.10) |
| 5.13 Gộp Topic (v0.2) | 5 Hệ quả lên đối tượng liên quan | a | Topic nguồn rời Trending (011.6), không theo dõi được (007.7) |
| 5.14 Vô hiệu hóa/mở lại Tag (v0.2) | 6 Vòng đời | a | Vô hiệu hóa Tag đã vô hiệu hóa, mở lại Tag đang hoạt động: trạng thái không đổi (T-166, T-167) |
| 5.9 Theo dõi Topic (v0.3) | 4 Giới hạn và vi phạm | a | Chỉ Topic trong danh mục (007, 007.1); Topic đã loại bị từ chối (007.7) |
| 5.10 Trending (v0.3) | 4 Giới hạn và vi phạm | c→hỏi | Tag chỉ có trên nháp/nhóm kín — ISS-238/DEC-161 (008.19); so tên — ISS-237/DEC-160 |
| 5.7 Phản hồi gợi ý (v0.3) | 2 Ngữ cảnh | c→hỏi | Gửi lại sau từ chối — ISS-239/DEC-162 (005, 005.5) |
| 5.12 Đổi tên Topic (v0.3) | 4 Giới hạn và vi phạm | b | Đổi tên Topic đã loại bị từ chối (010.5) |

| 5.5 Gợi ý Topic bằng AI (v0.5) | 4 Giới hạn và vi phạm | c→hỏi | Yêu cầu bị từ chối vì văn bản ngắn không tính vào 10 mỗi phút — OP-M05-11 → ISS-253/DEC-167 (003.16) |
| 5.5 Gợi ý Topic bằng AI (v0.6) | 2 Ngữ cảnh | a | Gợi ý cũ, cảnh báo, gợi ý lại chỉ với bài viết chưa gửi (003.10, 003.12, 003.13; DEC-167) |
| 5.8 Gắn Tag (v0.6) | 5 Hệ quả lên đối tượng liên quan | c | Không đặc tả: khi sửa bài, tác giả có thấy và gỡ được Tag bị vô hiệu hóa không (nguồn chưa nói; AUD-M05-40) |

## 4. Rà hồi quy (RULES §8.5)

Ô ∈ {Đạt, Không đạt, Không áp dụng} kèm bằng chứng ngắn. Lịch sử sửa đổi 0.6 được đối chiếu với `diff` bản chụp v0.5 (RG-6): mọi khác biệt ở SR và routing đã có trong dòng 0.6.

| ID | Thay đổi | RG-1 cấp trên | RG-2 cùng đối tượng | RG-3 "chỉ" | RG-4 OP mở | RG-5 tham chiếu ID bỏ | RG-6 Lịch sử | RG-7 ca kiểm |
|---|---|---|---|---|---|---|---|---|
| ISH-M05-003.15 | Mới | Đạt: dưới 003 ("soạn bài mới"), từ chối khi bài đã gửi | Đạt: so từng yêu cầu 003.1…003.14: 003.10, 003.12, 003.13 và hàng 5.2 đã giới hạn vào bài chưa gửi (0.6); 003.11 (giữ trạng thái khi đổi tệp) và 003.14 (gửi bài) không xảy ra thêm với bài đã gửi; 004.x, 005.x không mâu thuẫn | Không áp dụng | Đạt: không còn OP mở | Không áp dụng | Đạt: dòng 0.5, 0.6 | Đạt: T-182, T-212 |
| ISH-M05-003.10, 003.12, 003.13 | Đổi nội dung (ID giữ): thêm "chưa gửi" (0.6) | Đạt: dưới 003 | Đạt: so 003.15 và hàng 5.2 (hai hàng 003.10, 003.13 cũng đã đổi) | Không áp dụng | Đạt | Không áp dụng | Đạt: dòng 0.6 | Đạt: T-035, T-036, T-038, T-040, T-137, T-201, T-202, T-203 thêm "bài viết chưa gửi"; T-212 |
| ISH-M05-003.16 | Mới | Đạt: nằm cùng nhóm giới hạn 003.8, 003.9 | Đạt: so 003.6, 003.7 (từ chối ngắn) và 003.8 | Không áp dụng | Đạt | Không áp dụng | Đạt | Đạt: T-183, T-184 |
| ISH-M05-006.8 | Đổi nội dung (ID giữ; 0.5 đổi cơ sở, 0.6 viết lại câu) | Đạt: dưới 006 (tên Tag tự do) | Đạt: grep "tên Tag" so 006.6, 006.7, 006.9, 006.13, 006.14, 006.15 | Đạt: DEC-166 "chỉ" — "ít nhất một ký tự không thuộc nhóm" chỉ đọc được một cách; tên hợp lệ ở 006.1, 006.2 | Đạt: không còn OP mở | Không áp dụng | Đạt: dòng 0.5, 0.6 | Đạt: T-185, T-187 |
| ISH-M05-006.17 | Mới | Đạt: dưới 006; giới hạn 5 tách khỏi 006.4 | Đạt: so 006.4, 006.5, 012.2, 012.4, 012.5, 006.16 — mở lại Tag không vượt 5 | Không áp dụng | Đạt | Không áp dụng | Đạt | Đạt: T-190, T-191 |
| ISH-M05-006.18 | Mới | Đạt: dưới 006 ("đến lúc hiển thị") | Đạt: so 006.9, 006.16 | Không áp dụng | Đạt | Không áp dụng | Đạt | Đạt: T-192 |
| ISH-M05-007.4 | Đổi nội dung | Lưu ý: cấp trên 007 chỉ nói theo dõi; hiển thị số theo dõi đã có từ trước (không đổi phạm vi) | Đạt: so 007.3, 007.6, 011.4 | Không áp dụng | Đạt | Không áp dụng | Đạt | Đạt: T-193 |
| ISH-M05-007.8 | Mới | Đạt: dưới 007 | Đạt: so 007.4, 007.6, 011.3, 011.4 (người theo dõi cả hai tính một lần) | Đạt: DEC-168 "chỉ/trừ tài khoản đã xóa" — một yêu cầu có cả vế bao gồm lẫn loại trừ | Đạt | Không áp dụng | Đạt | Đạt: T-194 |
| ISH-M05-009.3 | Bỏ ID (0.6, AUD-37) | Không áp dụng | Không áp dụng | Không áp dụng | Không áp dụng | Đạt: grep "009.3" → 0 ở SR, routing, ca kiểm; hành vi chuyển sang hàng R5 M07 | Đạt: ghi ở dòng 0.6 vì ID nằm trong bản chụp v0.5 | Đạt: T-195 bỏ |
| ISH-M05-010.7 | Mới (0.5); 0.6 bỏ ghi chú OP ở Phụ lục A | Đạt: dưới 010 | Đạt: so 010.1…010.6 | Không áp dụng | Đạt: không còn OP mở | Không áp dụng | Đạt | Đạt: T-196; T-199 bỏ |
| ISH-M05-010.8 | Mới | Đạt: dưới 010 | Đạt: so 010.5, 011.1; Topic nguồn đã gộp không thuộc danh mục nên tên của nó không tính là trùng | Không áp dụng | Đạt | Không áp dụng | Đạt | Đạt: T-197, T-198 |
| ISH-M05-006.15, 008.5, 008.6, 008.7, 008.17 | Đổi diễn đạt (không đổi nghĩa) | Đạt | Đạt: nghĩa không đổi (RULE-10) | Không áp dụng | Đạt | Không áp dụng | Đạt | Đạt: ca cũ còn hợp lệ |
| Mục 2.1 (3 thuật ngữ tài khoản), 3.1, mục 5.10 Lý do | Mới / đổi | Không áp dụng | Đạt: thuật ngữ chỉ dùng ở 007.8; Lý do lấy từ DEC-169 | Không áp dụng | Đạt | Không áp dụng | Đạt | Không áp dụng |

## 5. WARN giữ lại

| Mã WARN | ID | Lý do giữ |
|---|---|---|
| — | — | Không có WARN giữ lại |

## 6. Điểm đã raise cho stakeholder

| OP / ISS / QA | Vấn đề | Trạng thái |
|---|---|---|
| ISS-211 / QA-271 | Số Topic mỗi bài (DRAFT §3.4 vs DEC-049) | Đã trả lời — DEC-143 |
| ISS-212 / QA-272 | Số Tag mỗi bài (DRAFT §3.2 vs DEC-051) | Đã trả lời — DEC-143 |
| ISS-213 / QA-273 | Đổi Topic/Tag sau khi gửi | Đã trả lời — DEC-144 |
| ISS-214 / QA-274 | Topic nguồn sau gộp | Đã trả lời — DEC-145 |
| ISS-215 / QA-275 | Người theo dõi Topic nguồn | Đã trả lời — DEC-145 |
| ISS-216 / QA-276 | Trending: bài được tính | Đã trả lời — DEC-146 |
| ISS-217 / QA-277 | Trending: tương tác được tính | Đã trả lời — DEC-146 |
| ISS-218 / QA-278 | Ngưỡng gợi ý Topic | Đã trả lời — DEC-147 (sửa DEC-050) |
| ISS-219 / QA-279 | Gợi ý thay thế hay cộng thêm | Đã trả lời — DEC-148 |
| ISS-220 / QA-280 | Thay đổi nào làm gợi ý cũ | Đã trả lời — DEC-148 |
| ISS-221 / QA-281 | AI trả về một phần hợp lệ | Đã trả lời — DEC-149 (sửa DEC-132) |
| ISS-222 / QA-282 | Mở lại Tag | Đã trả lời — DEC-150 |
| ISS-223 / QA-283 | 30 ký tự có tính # | Đã trả lời — DEC-150 |
| ISS-224 / QA-284 | Khung tính năng, sở hữu trang duyệt | Đã trả lời — DEC-151 |
| ISS-225 / QA-285 | AI trả về hơn 3 Topic (từ ca kiểm T-021) | Đã trả lời — DEC-152 |
| ISS-226 / QA-286 | Chuẩn hóa tên Tag (từ ca kiểm T-066) | Đã trả lời — DEC-152 |
| ISS-227 / QA-287 | Thứ tự xếp hạng Trending (từ selfcheck CL-A06) | Đã trả lời — DEC-153 |
| ISS-228…236 / QA-288…296 | 9 vấn đề từ ISH-AUD-M05-r1 (AUD-01, 02, 10, 13, 14, 15, 16, 18, 21) | Đã trả lời — DEC-154…159 |
| ISS-237…242 / QA-297…302 | 6 vấn đề từ ISH-AUD-M05-r2 (AUD-24, 26, 27, 31 hai phần, 32) | Đã trả lời — DEC-160…163 |
| ISS-243, 244 / QA-303, 304 | 2 vấn đề từ ISH-AUD-M05-v1 (AUD-34, AUD-33) | Đã trả lời — DEC-164, DEC-165 |
| ISS-245…254 / QA-305…314 | 10 OP đã duyệt (OP-M05-01, 02, 04…09, 11, 12): lý do Trending; gợi ý khi sửa bài; đổi tên Topic rỗng/trùng; Tag bị vô hiệu hóa tính vào 5; số người theo dõi; thông báo khi Mod đổi Topic; hiển thị Tag chữ thường; ký tự trong tên Tag; tính yêu cầu bị từ chối vào giới hạn; chủ sở hữu hiển thị Topic/Tag | Đã trả lời — DEC-166…169 |
| Không có OP | OP-M05-13, OP-M05-14 và AUD-M05-40 là điểm nguồn chưa nói: không đặc tả, không hỏi (RULES §3.3); ghi ở mục 3 | Đóng |
