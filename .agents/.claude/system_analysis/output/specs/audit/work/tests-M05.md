# Ca kiểm — ISH-SR-M05 phiên bản 0.6
<!-- [Vietnamese Doc] -->

Tệp làm việc của Author (`specs/audit/work/tests-M05.md`). Quy tắc: `RULES` §11. Một dòng một ca; mọi yêu cầu cấp dưới có ít nhất một ca; cột "Giả định cần thêm" phải là `—` trước khi bàn giao.

Dữ liệu dùng chung: "thời điểm T" là lúc hệ thống tính điểm Trending; "User A" là tác giả, "User B" là một User khác; Mod M, Admin D. Trong các ca Trending, "đăng X trước" nghĩa là bài trở thành công khai lần đầu X trước T (DEC-154); trừ khi ca ghi khác, bài không có bookmark và không có người xem.

| ID ca | ID yêu cầu | Loại | Given | When | Then | Giả định cần thêm |
|---|---|---|---|---|---|---|
| T-001 | ISH-M05-001.1 | Biên | Hệ thống vừa khởi tạo, chưa có thao tác gộp hay đổi tên Topic | Người dùng xem danh mục Topic | Danh mục có đúng 11 Topic: Toán học, Ngữ văn, Ngoại ngữ, Khoa học tự nhiên (Lý/Hóa/Sinh), Khoa học xã hội (Sử/Địa/KT&PL), Tin học, Kỹ năng mềm, Hướng nghiệp, Nghệ thuật & Sáng tạo, Góc Chill, Khác | — |
| T-002 | ISH-M05-001.2 | Thường | Danh mục Topic như T-001 | User A mở danh sách chọn Topic khi tạo bài viết | 11 Topic hiện cùng một cấp; không có mục cha nào để chọn trước Topic | — |
| T-003 | ISH-M05-001.3 | Quyền | Guest chưa đăng nhập | Guest xem danh sách Topic | Guest thấy đủ 11 Topic | — |
| T-004 | ISH-M05-001.3 | Quyền | User A đã đăng nhập | User A xem danh sách Topic | User A thấy đủ 11 Topic | — |
| T-005 | ISH-M05-001.4 | Vi phạm | Admin D đăng nhập; danh mục có 11 Topic | Admin D tìm cách thêm Topic "Âm nhạc" vào danh mục | Hệ thống không có thao tác thêm Topic, yêu cầu thêm bị từ chối; danh mục vẫn 11 Topic, không có "Âm nhạc" | — |
| T-006 | ISH-M05-002.1 | Thường | User A đang tạo bài viết mới | User A chọn Topic "Toán học" từ danh mục rồi gửi bài | Bài viết được gửi với đúng 1 Topic "Toán học" | — |
| T-007 | ISH-M05-002.2 | Vi phạm | User A đang tạo bài viết | Yêu cầu gửi bài kèm Topic "Âm nhạc" (không có trong danh mục) | Hệ thống từ chối Topic "Âm nhạc"; bài viết không có Topic "Âm nhạc" | — |
| T-008 | ISH-M05-002.2 | Biên | Topic "Góc Chill" đã bị gộp vào "Kỹ năng mềm" (không còn trong danh mục) | User A chọn "Góc Chill" cho bài viết mới | Hệ thống từ chối "Góc Chill" | — |
| T-009 | ISH-M05-002.3 | Thường | User A tạo bài viết, không bấm gợi ý Topic | User A tự chọn "Tin học" và "Hướng nghiệp" rồi gửi bài | Bài viết được gửi với 2 Topic "Tin học", "Hướng nghiệp"; không có gợi ý Topic nào được tạo | — |
| T-010 | ISH-M05-002.5 | Biên | Bài viết nháp của User A có đúng 1 Topic "Ngữ văn" | User A gửi bài | Bài viết được gửi với 1 Topic | — |
| T-011 | ISH-M05-002.5 | Vi phạm | Bài viết nháp của User A có 0 Topic | User A gửi bài | Hệ thống từ chối việc gửi; bài viết vẫn ở trạng thái bản nháp | — |
| T-012 | ISH-M05-002.6 | Vi phạm | Bài viết đã gửi của User A có 1 Topic "Ngữ văn" | User A sửa bài, bỏ "Ngữ văn", lưu thay đổi | Hệ thống từ chối thay đổi; bài viết vẫn có Topic "Ngữ văn" | — |
| T-013 | ISH-M05-002.6 | Vi phạm | Bài viết của User A có 1 Topic "Ngữ văn" | Mod M bỏ "Ngữ văn" khỏi bài viết rồi lưu | Hệ thống từ chối thay đổi; bài viết vẫn có Topic "Ngữ văn" | — |
| T-014 | ISH-M05-002.7 | Biên | Bài viết nháp của User A có 3 Topic | User A gửi bài | Bài viết được gửi với 3 Topic | — |
| T-015 | ISH-M05-002.8 | Vi phạm | Bài viết của User A đã có 3 Topic "Toán học", "Tin học", "Hướng nghiệp" | User A chọn thêm Topic thứ 4 "Kỹ năng mềm" | Hệ thống từ chối lựa chọn; bài viết vẫn có 3 Topic ban đầu | — |
| T-016 | ISH-M05-002.8 | Vi phạm | Bài viết của User A có 3 Topic | Mod M chọn thêm Topic thứ 4 cho bài viết | Hệ thống từ chối lựa chọn; bài viết vẫn có 3 Topic | — |
| T-017 | ISH-M05-002.9 | Thường | Bài viết đã gửi của User A có Topic "Toán học" | User A sửa bài, đổi "Toán học" thành "Tin học", lưu | Bài viết có Topic "Tin học", không còn "Toán học" | — |
| T-018 | ISH-M05-003.1 | Thường | User A soạn bài viết mới 30 tiếng, không bấm gợi ý | User A tiếp tục soạn và chọn Topic | Không có gợi ý Topic nào được tạo; lựa chọn Topic chỉ gồm Topic User A tự chọn | — |
| T-019 | ISH-M05-003.2 | Thường | Bài viết có tiêu đề + nội dung 40 tiếng và 1 tệp đính kèm PDF | User A yêu cầu gợi ý Topic | Dữ liệu dùng để tạo gợi ý chỉ gồm tiêu đề và nội dung văn bản; tệp PDF không được dùng | — |
| T-020 | ISH-M05-003.3 | Biên | Bài viết đủ 10 tiếng; dịch vụ AI trả về 3 Topic hợp lệ | User A yêu cầu gợi ý | Gợi ý gồm đúng 3 Topic | — |
| T-021 | ISH-M05-004.7 | Biên | Bài viết đủ 10 tiếng; dịch vụ AI trả về 4 Topic hợp lệ "Toán học", "Tin học", "Hướng nghiệp", "Khác" theo thứ tự đó | User A yêu cầu gợi ý | Gợi ý gồm 3 Topic "Toán học", "Tin học", "Hướng nghiệp" (3 Topic đầu); "Khác" bị bỏ | — |
| T-022 | ISH-M05-003.4 | Thường | User A đã tự chọn "Toán học"; AI trả về "Tin học", "Kỹ năng mềm" | User A yêu cầu gợi ý | Lựa chọn Topic của bài viết thành "Tin học", "Kỹ năng mềm"; "Toán học" bị bỏ chọn | — |
| T-023 | ISH-M05-003.4 | Thường | User A chưa chọn Topic nào; AI trả về "Ngữ văn" | User A yêu cầu gợi ý | Lựa chọn Topic là "Ngữ văn" (được chọn sẵn) | — |
| T-024 | ISH-M05-003.5 | Thường | Lựa chọn sau gợi ý là "Tin học", "Kỹ năng mềm" | User A bỏ "Kỹ năng mềm", chọn thêm "Toán học" | Lựa chọn được lưu là "Tin học", "Toán học" | — |
| T-025 | ISH-M05-003.6 | Biên | Tiêu đề 4 tiếng, nội dung 5 tiếng (tổng 9) | User A yêu cầu gợi ý | Hệ thống từ chối yêu cầu; không gọi dịch vụ AI; lựa chọn Topic không đổi | — |
| T-026 | ISH-M05-003.6 | Biên | Tiêu đề 4 tiếng, nội dung 6 tiếng (tổng 10) | User A yêu cầu gợi ý | Hệ thống chấp nhận yêu cầu và tạo gợi ý | — |
| T-027 | ISH-M05-003.6 | Biên | Tiêu đề 10 tiếng, nội dung rỗng | User A yêu cầu gợi ý | Hệ thống chấp nhận yêu cầu (tổng 10 tiếng) | — |
| T-028 | ISH-M05-003.6 | Biên | Tiêu đề rỗng, nội dung rỗng | User A yêu cầu gợi ý | Hệ thống từ chối yêu cầu (tổng 0 tiếng) | — |
| T-029 | ISH-M05-003.6 | Công thức | Tiêu đề "Hỏi  về   xác suất" (nhiều dấu cách liền nhau, 4 tiếng), nội dung 5 tiếng ngăn bởi xuống dòng | User A yêu cầu gợi ý | Tổng đếm được 9 tiếng; hệ thống từ chối yêu cầu | — |
| T-030 | ISH-M05-003.7 | Biên | Tổng 9 tiếng như T-025 | User A yêu cầu gợi ý | Hệ thống hiển thị thông báo nội dung quá ngắn cho User A | — |
| T-031 | ISH-M05-003.8 | Biên | User A gửi 10 yêu cầu gợi ý hợp lệ trong 30 giây đầu tiên | User A gửi yêu cầu thứ 10 | Cả 10 yêu cầu được chấp nhận | — |
| T-032 | ISH-M05-003.9 | Vi phạm | User A đã gửi 10 yêu cầu gợi ý trong 30 giây | User A gửi yêu cầu thứ 11 ở giây thứ 40 | Hệ thống từ chối yêu cầu thứ 11 | — |
| T-033 | ISH-M05-003.9 | Thời gian | User A gửi 10 yêu cầu trong giây 0–9, không gửi thêm | User A gửi yêu cầu tiếp theo ở giây thứ 125 | Hệ thống chấp nhận yêu cầu (ngoài phút của 10 yêu cầu trước) | — |
| T-034 | ISH-M05-003.9 | Quyền | User A đã dùng hết 10 yêu cầu trong 30 giây | User B gửi yêu cầu gợi ý đầu tiên của mình ở giây thứ 31 | Hệ thống chấp nhận yêu cầu của User B (giới hạn tính theo từng người dùng) | — |
| T-035 | ISH-M05-003.10 | Thường | Gợi ý còn mới cho bài viết của User A (bài viết chưa gửi) | User A sửa một chữ trong tiêu đề | Gợi ý thành gợi ý cũ | — |
| T-036 | ISH-M05-003.10 | Thường | Gợi ý còn mới (bài viết chưa gửi) | User A thêm một câu vào nội dung | Gợi ý thành gợi ý cũ | — |
| T-037 | ISH-M05-003.11 | Thường | Gợi ý còn mới | User A thêm một tệp đính kèm | Gợi ý vẫn là gợi ý còn mới | — |
| T-038 | ISH-M05-003.12 | Thường | Gợi ý đã thành gợi ý cũ như T-035 (bài viết chưa gửi) | User A xem trang soạn bài | Hệ thống hiển thị cảnh báo gợi ý cũ | — |
| T-039 | ISH-M05-003.12 | Thường | Gợi ý còn mới (bài viết chưa gửi) | User A xem trang soạn bài | Không có cảnh báo gợi ý cũ | — |
| T-040 | ISH-M05-003.13 | Thường | Gợi ý cũ; lựa chọn hiện tại "Tin học"; AI trả về "Hướng nghiệp" (bài viết chưa gửi) | User A yêu cầu gợi ý lại | Lựa chọn thành "Hướng nghiệp"; gợi ý mới là gợi ý còn mới; cảnh báo gợi ý cũ biến mất | — |
| T-041 | ISH-M05-003.14 | Thường | Gợi ý cũ; bài viết có 2 Topic | User A gửi bài | Bài viết được gửi với 2 Topic | — |
| T-042 | ISH-M05-004.1 | Lỗi | Admin tắt công tắc AI chung | User A soạn bài 30 tiếng và tìm cách yêu cầu gợi ý Topic | Không có gợi ý Topic; User A tự chọn "Toán học" và gửi bài thành công | — |
| T-043 | ISH-M05-004.1 | Lỗi | Công tắc AI chung bật, công tắc gợi ý Topic tắt | User A tìm cách yêu cầu gợi ý Topic | Không có gợi ý Topic | — |
| T-044 | ISH-M05-004.1 | Thường | Công tắc AI chung bật, công tắc gợi ý Topic bật | User A yêu cầu gợi ý cho bài 30 tiếng | Hệ thống tạo gợi ý Topic | — |
| T-045 | ISH-M05-004.2 | Lỗi | Dịch vụ AI hết thời gian chờ ở cả lần gọi đầu và lần thử lại | User A yêu cầu gợi ý | Hệ thống thông báo không gợi ý được Topic | — |
| T-046 | ISH-M05-004.3 | Lỗi | User A đã chọn "Toán học"; dịch vụ AI báo lỗi sau lần thử lại | User A yêu cầu gợi ý | Lựa chọn Topic vẫn là "Toán học" | — |
| T-047 | ISH-M05-004.4 | Lỗi | Dịch vụ AI không trả về kết quả như T-045; User A đã chọn "Tin học" | User A gửi bài | Bài viết được gửi với Topic "Tin học" | — |
| T-048 | ISH-M05-004.5 | Lỗi | AI trả về "Toán học", "Vật lý lượng tử", "Tin học" | User A yêu cầu gợi ý | Gợi ý gồm "Toán học", "Tin học" và được chọn sẵn; "Vật lý lượng tử" bị bỏ | — |
| T-049 | ISH-M05-004.6 | Lỗi | User A đã chọn "Ngữ văn"; AI trả về chỉ "Vật lý lượng tử" | User A yêu cầu gợi ý | Hệ thống thông báo không gợi ý được Topic; lựa chọn vẫn là "Ngữ văn" | — |
| T-050 | ISH-M05-004.6 | Lỗi | AI trả về danh sách rỗng | User A yêu cầu gợi ý | Hệ thống thông báo không gợi ý được Topic; lựa chọn không đổi | — |
| T-051 | ISH-M05-005.1 | Thường | AI gợi ý "Tin học", "Kỹ năng mềm"; User A đổi thành "Tin học", "Toán học"; không sửa tiêu đề hay nội dung | User A gửi bài | Hệ thống ghi một phản hồi: gợi ý = {Tin học, Kỹ năng mềm}, lựa chọn cuối = {Tin học, Toán học} | — |
| T-052 | ISH-M05-005.1 | Thường | Gợi ý lần 1 "Ngữ văn" thành cũ; User A gợi ý lại, nhận "Hướng nghiệp" (còn mới) | User A gửi bài với "Hướng nghiệp" | Hệ thống ghi một phản hồi: gợi ý = {Hướng nghiệp}, lựa chọn cuối = {Hướng nghiệp} | — |
| T-053 | ISH-M05-005.2 | Thường | Gợi ý đã thành cũ (User A sửa nội dung sau khi nhận gợi ý) | User A gửi bài | Không có phản hồi gợi ý Topic nào được ghi cho bài viết | — |
| T-054 | ISH-M05-005.3 | Thường | User A tự chọn Topic, không yêu cầu gợi ý | User A gửi bài | Không có phản hồi gợi ý Topic nào được ghi | — |
| T-055 | ISH-M05-005.3 | Lỗi | User A yêu cầu gợi ý nhưng bị từ chối vì 9 tiếng, rồi tự chọn Topic | User A gửi bài | Không có phản hồi gợi ý Topic nào được ghi | — |
| T-056 | ISH-M05-005.3 | Lỗi | User A yêu cầu gợi ý nhưng dịch vụ AI không trả về kết quả | User A gửi bài với Topic tự chọn | Không có phản hồi gợi ý Topic nào được ghi | — |
| T-057 | ISH-M05-006.1 | Thường | User A tạo bài viết | User A nhập Tag "XácSuất" | Bài viết có Tag; Tag hiển thị là "xácsuất" (006.18) | — |
| T-058 | ISH-M05-006.2 | Thường | Chưa có Tag nào tên "bayesnet" | User A gắn Tag "bayesnet" cho bài viết và gửi | Tag "bayesnet" được tạo ngay, không chờ duyệt; bài viết có Tag "bayesnet" | — |
| T-059 | ISH-M05-006.2 | Thường | Tag "bayesnet" đã được User A tạo như T-058 | User B gắn Tag "bayesnet" cho bài viết của mình | Bài viết của User B gắn Tag "bayesnet" đã có; không tạo Tag thứ hai | — |
| T-060 | ISH-M05-006.3 | Biên | Bài viết nháp của User A có 1 Topic, 0 Tag | User A gửi bài | Bài viết được gửi với 0 Tag | — |
| T-061 | ISH-M05-006.4 | Biên | Bài viết có 4 Tag | User A gắn Tag thứ 5 | Tag thứ 5 được gắn; bài viết có 5 Tag | — |
| T-062 | ISH-M05-006.5 | Vi phạm | Bài viết có 5 Tag | User A gắn Tag thứ 6 "thongke" | Hệ thống từ chối "thongke"; bài viết vẫn có 5 Tag | — |
| T-063 | ISH-M05-006.6 | Biên | User A đang tạo bài viết | User A nhập tên Tag gồm đúng 30 chữ cái không dấu | Tag được chấp nhận | — |
| T-064 | ISH-M05-006.6 | Biên | User A đang tạo bài viết | User A nhập "#" theo sau là 30 chữ cái không dấu | Tag được chấp nhận; tên Tag dài 30 ký tự (dấu # không tính) | — |
| T-065 | ISH-M05-006.7 | Vi phạm | User A đang tạo bài viết | User A nhập tên Tag gồm 31 chữ cái không dấu | Hệ thống từ chối Tag | — |
| T-066 | ISH-M05-006.14 | Biên | User A đang tạo bài viết | User A nhập tên Tag rỗng (chỉ có dấu "#") | Hệ thống từ chối Tag | — |
| T-128 | ISH-M05-006.14 | Biên | User A đang tạo bài viết | User A nhập "#" theo sau là 3 dấu cách | Sau khi bỏ "#" và ký tự trắng, tên rỗng; hệ thống từ chối Tag | — |
| T-129 | ISH-M05-006.13 | Biên | User A đang tạo bài viết | User A nhập " bayes " (dấu cách đầu và cuối) | Tag được chấp nhận với tên "bayes"; không bị từ chối vì khoảng trắng | — |
| T-130 | ISH-M05-006.15 | Biên | User A đang tạo bài viết | User A nhập tên Tag 30 chữ có dấu, ví dụ "XácSuấtThốngKê" lặp đến đủ 30 chữ | Tag được chấp nhận (30 ký tự) | — |
| T-131 | ISH-M05-006.15 | Vi phạm | User A đang tạo bài viết | User A nhập tên Tag 31 chữ có dấu | Hệ thống từ chối Tag | — |
| T-132 | ISH-M05-006.15 | Thường | User A đang tạo bài viết | User A nhập "XácSuấtThốngKê" | Tên Tag dài 14 ký tự, được chấp nhận | — |
| T-067 | ISH-M05-006.8 | Vi phạm | User A đang tạo bài viết | User A nhập tên Tag "machine learning" (dấu cách ở giữa) | Hệ thống từ chối Tag | — |
| T-068 | ISH-M05-006.9 | Thường | Đã có Tag "bayes" | User A gắn Tag "Bayes" cho bài viết | Bài viết gắn Tag "bayes" đã có; không có Tag mới được tạo | — |
| T-069 | ISH-M05-006.10 | Thường | Bài viết đã có Tag "bayes", tổng 1 Tag | User A gắn thêm "bayes" | Bài viết vẫn có đúng 1 Tag "bayes" | — |
| T-070 | ISH-M05-006.10 | Biên | Bài viết có 5 Tag, trong đó có "bayes" | User A gắn thêm "BAYES" | Bài viết vẫn có 5 Tag; không bị từ chối vì vượt giới hạn | — |
| T-071 | ISH-M05-006.11 | Thường | Bài viết đã gửi của User A có Tag "bayes" | User A sửa bài, bỏ "bayes", thêm "thongke", lưu | Bài viết có Tag "thongke", không còn "bayes" | — |
| T-072 | ISH-M05-006.12 | Quyền | Bài viết của User A có Tag "bayes" | User B yêu cầu bỏ Tag "bayes" | Hệ thống từ chối; bài viết vẫn có "bayes" | — |
| T-073 | ISH-M05-006.12 | Quyền | Bài viết của User A có Tag "bayes" | Mod M yêu cầu thêm Tag "spam" vào bài viết | Hệ thống từ chối; bài viết không đổi Tag | — |
| T-074 | ISH-M05-006.12 | Quyền | Bài viết của User A | Guest yêu cầu thay đổi Tag | Hệ thống từ chối | — |
| T-075 | ISH-M05-007.1 | Thường | Topic "Tin học" có 0 người theo dõi; User A chưa theo dõi | User A theo dõi "Tin học" | User A đang theo dõi "Tin học"; số người theo dõi là 1 | — |
| T-076 | ISH-M05-007.2 | Thường | User A đang theo dõi "Tin học" (1 người theo dõi) | User A bỏ theo dõi | User A không còn theo dõi; số người theo dõi là 0 | — |
| T-077 | ISH-M05-007.3 | Thường | User A theo dõi "Tin học", không theo dõi "Ngữ văn" | User A xem hai Topic | "Tin học" hiện đang theo dõi; "Ngữ văn" hiện chưa theo dõi | — |
| T-078 | ISH-M05-007.4 | Biên | "Ngữ văn" có 0 người theo dõi | User A xem "Ngữ văn" | Số người theo dõi hiển thị 0 | — |
| T-079 | ISH-M05-007.4 | Thường | "Toán học" có 25 người theo dõi | User A xem "Toán học" | Số người theo dõi hiển thị 25 | — |
| T-080 | ISH-M05-007.5 | Quyền | Guest chưa đăng nhập | Guest yêu cầu theo dõi "Tin học" | Hệ thống từ chối; số người theo dõi không đổi | — |
| T-081 | ISH-M05-007.6 | Thường | User A đang theo dõi "Tin học" (1 người theo dõi) | User A yêu cầu theo dõi "Tin học" lần nữa | User A vẫn đang theo dõi; số người theo dõi vẫn là 1 | — |
| T-082 | ISH-M05-008.1 | Công thức | Tại T, Topic K có: P1 công khai, đăng 2 ngày trước, 3 upvote và 2 bình luận phát sinh trong 7 ngày; P2 công khai, đăng 20 ngày trước, 4 upvote phát sinh hôm qua, 1 bình luận phát sinh 10 ngày trước; P3 công khai, đăng 30 ngày trước, không tương tác trong 7 ngày | Hệ thống tính điểm Trending của K tại T | P1 = 2×3 + 2 + 1 (đăng trong 7 ngày) = 9; P2 = 2×4 + 0 = 8 (bài cũ có hoạt động mới, không có điểm thưởng bài mới); P3 = 0; điểm K = 17 | — |
| T-083 | ISH-M05-008.1 | Công thức | Topic L chỉ có P5 công khai, đăng 3 giờ trước T, 0 upvote, 0 bình luận | Tính điểm L tại T | Điểm L = 1 (bài mới chưa có hoạt động) | — |
| T-084 | ISH-M05-008.1 | Công thức | Topic M không có bài viết nào | Tính điểm M tại T | Điểm M = 0 | — |
| T-085 | ISH-M05-008.1 | Công thức | P1 của T-082 gắn cả Topic K và Topic L; L còn có P5 của T-083 | Tính điểm L tại T | Điểm L = 9 (P1) + 1 (P5) = 10; P1 cũng vẫn đóng góp 9 cho K | — |
| T-086 | ISH-M05-008.2 | Công thức | Tag "bayes" gắn trên P1 và P2 của T-082; Tag "thongke" chỉ gắn trên P3 | Tính điểm hai Tag tại T | "bayes" = 9 + 8 = 17; "thongke" = 0 | — |
| T-087 | ISH-M05-008.3 | Công thức | Topic K có P1 (9 điểm như T-082) và P4 đăng 1 ngày trước trong một Group Private, 5 upvote trong 7 ngày | Tính điểm K | P4 không được tính; K = 9 | — |
| T-088 | ISH-M05-008.3 | Công thức | Topic K có P6 trong một Group Public, công khai, đăng 1 ngày trước, 1 upvote | Tính điểm K chỉ với P6 | K = 2×1 + 0 + 1 = 3 | — |
| T-089 | ISH-M05-008.3 | Công thức | Topic K có P7 bị Mod ẩn, P8 đã bị xóa, P9 đang chờ duyệt, P10 bản nháp; mỗi bài đăng 1 ngày trước với 2 upvote | Tính điểm K chỉ với P7–P10 | K = 0 (không bài nào là bài viết công khai) | — |
| T-090 | ISH-M05-008.3 | Công thức | Topic K có P11 công khai của một người dùng đang bị khóa tài khoản, đăng 1 ngày trước, 1 bình luận | Tính điểm K chỉ với P11 | K = 0×2 + 1 + 1 = 2 (không loại theo trạng thái tác giả) | — |
| T-091 | ISH-M05-008.4 | Công thức | P1 có 3 upvote vào bài và một bình luận của P1 có 5 upvote, tất cả trong 7 ngày; 0 bình luận khác | Tính phần đóng góp của P1 (đăng 2 ngày trước) | 2×3 + 1 (bình luận đó) + 1 = 8; 5 upvote vào bình luận không được tính | — |
| T-092 | ISH-M05-008.5 | Công thức | P12 công khai, đăng 10 ngày trước; trong 7 ngày có 1 bình luận gốc và 2 trả lời | Tính đóng góp của P12 | 0×2 + 3 = 3 | — |
| T-093 | ISH-M05-008.6 | Công thức | P12 nhận 4 upvote trong 7 ngày, 1 người đã rút upvote | Tính đóng góp của P12 (không bình luận) | 2×3 = 6 | — |
| T-094 | ISH-M05-008.7 | Công thức | P12 có 3 bình luận trong 7 ngày, 1 bình luận đã bị xóa | Tính đóng góp của P12 (không upvote) | 2 | — |
| T-095 | ISH-M05-008.8 | Thời gian | P13 công khai, đăng 167 giờ 59 phút trước T, 0 tương tác | Tính đóng góp của P13 | 1 (trong 7 ngày gần nhất) | — |
| T-096 | ISH-M05-008.8 | Thời gian | P14 công khai, đăng 168 giờ 1 phút trước T, 0 tương tác | Tính đóng góp của P14 | 0 (ngoài 7 ngày gần nhất) | — |
| T-097 | ISH-M05-008.8 | Thời gian | P14 như T-096 nhận 1 upvote 167 giờ trước T và 1 upvote 169 giờ trước T | Tính đóng góp của P14 | 2×1 = 2 (chỉ upvote trong 168 giờ) | — |
| T-098 | ISH-M05-008.9 | Công thức | Điểm tại T: K = 17, L = 10, M = 0 | Hệ thống xếp hạng Topic | Thứ tự: K, L, M | — |
| T-099 | ISH-M05-008.10 | Công thức | Điểm tại T: "bayes" = 17, "thongke" = 0, "xacsuat" = 4 | Hệ thống xếp hạng Tag | Thứ tự: "bayes", "xacsuat", "thongke" | — |
| T-100 | ISH-M05-009.1 | Quyền | Bài viết của User A có Topic "Toán học" | Mod M đổi Topic thành "Tin học" và lưu | Bài viết có Topic "Tin học", không còn "Toán học" | — |
| T-101 | ISH-M05-009.1 | Quyền | Bài viết của User A có Topic "Ngữ văn" | Admin D đổi Topic thành "Ngữ văn", "Hướng nghiệp" và lưu | Bài viết có 2 Topic "Ngữ văn", "Hướng nghiệp" | — |
| T-102 | ISH-M05-009.2 | Quyền | Bài viết của User A có Topic "Toán học" | User B yêu cầu đổi Topic thành "Tin học" | Hệ thống từ chối; bài viết vẫn có "Toán học" | — |
| T-103 | ISH-M05-009.2 | Quyền | Bài viết của User A | Guest yêu cầu đổi Topic | Hệ thống từ chối | — |
| T-104 | ISH-M05-010.1 | Thường | Topic "Góc Chill" gắn trên 15 bài viết | Mod M đổi tên "Góc Chill" thành "Góc Thư giãn" | Topic có tên "Góc Thư giãn"; 15 bài viết vẫn gắn Topic này và hiển thị tên mới; danh mục vẫn 11 Topic | — |
| T-105 | ISH-M05-010.2 | Thường | "Góc Chill" có 12 người theo dõi | Admin D đổi tên thành "Góc Thư giãn" | "Góc Thư giãn" có 12 người theo dõi, cùng 12 người đó | — |
| T-106 | ISH-M05-010.3 | Quyền | User A đăng nhập | User A yêu cầu đổi tên "Tin học" | Hệ thống từ chối; tên vẫn là "Tin học" | — |
| T-107 | ISH-M05-010.3 | Quyền | Guest | Guest yêu cầu đổi tên "Tin học" | Hệ thống từ chối | — |
| T-108 | ISH-M05-001.5 | Vi phạm | Admin D đăng nhập | Admin D yêu cầu xóa Topic "Khác" | Hệ thống từ chối; "Khác" vẫn trong danh mục | — |
| T-109 | ISH-M05-001.5 | Vi phạm | Mod M đăng nhập | Mod M yêu cầu xóa Topic "Góc Chill" | Hệ thống từ chối | — |
| T-110 | ISH-M05-011.1 | Thường | Bài P gắn "Góc Chill" và "Kỹ năng mềm" (2 Topic) | Mod M gộp "Góc Chill" (nguồn) vào "Kỹ năng mềm" (đích) | P có đúng 1 Topic "Kỹ năng mềm" | — |
| T-111 | ISH-M05-011.1 | Thường | Bài Q chỉ gắn "Góc Chill" | Mod M gộp như T-110 | Q có Topic "Kỹ năng mềm" | — |
| T-112 | ISH-M05-011.2 | Thường | Danh mục 11 Topic | Admin D gộp "Góc Chill" vào "Kỹ năng mềm" | Danh mục còn 10 Topic, không có "Góc Chill"; "Góc Chill" không chọn được cho bài viết | — |
| T-113 | ISH-M05-011.2 | Thường | Sau khi gộp như T-112; điểm Trending đang được tính | Hệ thống xếp hạng Topic | "Góc Chill" không có trong bảng xếp hạng; các bài trước đây của "Góc Chill" đóng góp vào "Kỹ năng mềm" | — |
| T-114 | ISH-M05-011.3 | Thường | User X chỉ theo dõi "Góc Chill" | Mod M gộp "Góc Chill" vào "Kỹ năng mềm" | User X đang theo dõi "Kỹ năng mềm" | — |
| T-115 | ISH-M05-011.4 | Công thức | "Góc Chill" có 5 người theo dõi, "Kỹ năng mềm" có 8, trong đó 2 người theo dõi cả hai | Mod M gộp "Góc Chill" vào "Kỹ năng mềm" | "Kỹ năng mềm" có 5 + 8 − 2 = 11 người theo dõi | — |
| T-116 | ISH-M05-011.5 | Quyền | User A đăng nhập | User A yêu cầu gộp "Góc Chill" vào "Khác" | Hệ thống từ chối; danh mục không đổi | — |
| T-117 | ISH-M05-012.1 | Thường | Tag "spam" gắn trên 3 bài viết | Mod M vô hiệu hóa "spam" | Tag "spam" không hiển thị trên cả 3 bài viết | — |
| T-118 | ISH-M05-012.2 | Thường | Như T-117 | Mod M vô hiệu hóa "spam" | Liên kết giữa "spam" và 3 bài viết vẫn còn (thấy lại khi mở lại ở T-121) | — |
| T-119 | ISH-M05-012.3 | Thường | "spam" có điểm Trending 50, cao nhất trong các Tag | Mod M vô hiệu hóa "spam"; hệ thống xếp hạng Tag | "spam" không có trong bảng xếp hạng Trending | — |
| T-120 | ISH-M05-012.4 | Vi phạm | "spam" đang bị vô hiệu hóa | User A nhập "SPAM" làm Tag cho bài viết mới | "SPAM" không được gắn vào bài viết; bài viết không có Tag "spam" | — |
| T-121 | ISH-M05-012.5 | Thường | "spam" bị vô hiệu hóa, vẫn liên kết 3 bài viết | Admin D mở lại "spam" | "spam" hiển thị lại trên cả 3 bài viết | — |
| T-122 | ISH-M05-012.6 | Thường | "spam" đã được mở lại | User A gắn "spam" cho bài viết mới | Bài viết có Tag "spam" | — |
| T-123 | ISH-M05-012.7 | Quyền | User A đăng nhập | User A yêu cầu vô hiệu hóa "bayes" | Hệ thống từ chối; "bayes" vẫn hoạt động | — |
| T-124 | ISH-M05-012.8 | Quyền | "spam" bị vô hiệu hóa | User A yêu cầu mở lại "spam" | Hệ thống từ chối; "spam" vẫn bị vô hiệu hóa | — |
| T-125 | ISH-M05-012.9 | Vi phạm | Mod M đăng nhập | Mod M yêu cầu đổi tên Tag "bayes" thành "bayesian" | Hệ thống từ chối; tên Tag vẫn "bayes" | — |
| T-126 | ISH-M05-012.10 | Vi phạm | Admin D đăng nhập | Admin D yêu cầu gộp "bayes" vào "xacsuat" | Hệ thống từ chối; hai Tag không đổi | — |
| T-133 | ISH-M05-008.11 | Công thức | Tại T: Topic K = 10 điểm với 2 bài được tính đăng trong 7 ngày; Topic L = 10 điểm với 0 bài đăng trong 7 ngày | Hệ thống xếp hạng Topic | K xếp trước L | — |
| T-134 | ISH-M05-008.11 | Công thức | Tại T: "Tin học" và "Ngữ văn" cùng 6 điểm, cùng 1 bài đăng trong 7 ngày | Hệ thống xếp hạng Topic | "Ngữ văn" xếp trước "Tin học" (N trước T) | — |
| T-135 | ISH-M05-008.12 | Công thức | Tại T: Tag "bayes" = 5 điểm (0 bài mới), "xacsuat" = 5 điểm (1 bài mới), "anova" = 5 điểm (1 bài mới) | Hệ thống xếp hạng Tag | Thứ tự: "anova", "xacsuat", "bayes" | — |
| T-127 | ISH-M05-012.11 | Vi phạm | Mod M đăng nhập | Mod M yêu cầu xóa Tag "bayes" | Hệ thống từ chối; "bayes" vẫn tồn tại | — |
| T-136 | ISH-M05-003.11 | Thường | Gợi ý đã thành gợi ý cũ (User A sửa tiêu đề) | User A thêm một tệp đính kèm | Gợi ý vẫn là gợi ý cũ; cảnh báo gợi ý cũ vẫn hiển thị | — |
| T-137 | ISH-M05-003.10 | Thường | Gợi ý đã là gợi ý cũ (bài viết chưa gửi) | User A sửa nội dung lần nữa | Gợi ý vẫn là gợi ý cũ | — |
| T-138 | ISH-M05-002.10 | Quyền | Bài viết công khai của User A có Topic "Toán học", "Tin học" | Guest mở bài viết | Bài viết hiển thị hai Topic "Toán học", "Tin học" | — |
| T-139 | ISH-M05-002.11 | Thường | User A soạn bài viết mới, chưa chọn Topic nào | User A lưu bản nháp | Bản nháp được lưu với 0 Topic | — |
| T-140 | ISH-M05-002.11 | Vi phạm | Bản nháp đã lưu với 0 Topic như T-139 | User A gửi bài | Hệ thống từ chối việc gửi (ISH-M05-002.5); bản nháp vẫn còn | — |
| T-141 | ISH-M05-005.1 | Thường | User A nhận gợi ý "Tin học" (còn mới), giữ nguyên lựa chọn | User A gửi bài một lần | Có đúng 1 phản hồi gợi ý Topic cho lần gửi đó | — |
| T-142 | ISH-M05-005.1 | Thường | User A yêu cầu gợi ý, nhận "Toán học"; không sửa gì, yêu cầu lại, nhận "Tin học", "Toán học" (cả hai còn mới) | User A gửi bài với "Toán học" | Phản hồi ghi gợi ý = {Tin học, Toán học} (lần gần nhất), lựa chọn cuối = {Toán học}; không ghi gợi ý lần đầu | — |
| T-143 | ISH-M05-006.16 | Quyền | Bài viết công khai có Tag "bayes" (hoạt động) và "spam" (bị vô hiệu hóa) | Guest mở bài viết | Bài viết hiển thị Tag "bayes"; không hiển thị "spam" | — |
| T-144 | ISH-M05-008.13 | Công thức | Topic K chỉ có P20 công khai, đăng 2 ngày trước; trong 7 ngày: 3 upvote, 2 bình luận, 1 bookmark, 40 người xem | Tính điểm K tại T | Điểm tương tác P20 = 2×3 + 2 + 1 + 0,1×40 = 13; điểm K = 13 + 1 (bài mới) = 14 | — |
| T-145 | ISH-M05-008.13 | Công thức | Topic L chỉ có P21 công khai, đăng 20 ngày trước; trong 7 ngày: 0 upvote, 0 bình luận, 0 bookmark, 7 người xem | Tính điểm L tại T | Điểm L = 0,1×7 = 0,7 (bài cũ chỉ có người xem) | — |
| T-146 | ISH-M05-008.14 | Công thức | Trong 7 ngày: User B mở P21 5 lần, User C mở 1 lần, tác giả mở 3 lần | Tính số người xem của P21 | Số người xem = 2 (B và C); phần người xem = 0,2 | — |
| T-147 | ISH-M05-008.14 | Thời gian | User D mở P21 lần duy nhất 8 ngày trước T; User E mở P21 8 ngày trước và mở lại 1 ngày trước T | Tính số người xem của P21 | Số người xem = 1 (E); D ngoài 7 ngày gần nhất | — |
| T-148 | ISH-M05-008.14 | Biên | P21 có 30 lượt mở trang chi tiết của Guest trong 7 ngày, không có người dùng đã đăng nhập nào mở | Tính số người xem của P21 | Số người xem = 0 | — |
| T-149 | ISH-M05-008.16 | Công thức | Trong 7 ngày: User B, C, F bookmark P22; User C đã bỏ bookmark; tác giả tự bookmark P22; User G bookmark P22 9 ngày trước và vẫn giữ | Tính số bookmark của P22 | Số bookmark = 2 (B và F) | — |
| T-150 | ISH-M05-008.17 | Công thức | P23 công khai, đăng 10 ngày trước; 3 bình luận trong 7 ngày, 1 bình luận đang bị Mod ẩn | Tính điểm tương tác P23 | 2 | — |
| T-151 | ISH-M05-008.17 | Thường | Như T-150; Mod khôi phục bình luận bị ẩn | Tính lại điểm tương tác P23 | 3 | — |
| T-152 | ISH-M05-008.18 | Công thức | Topic "Góc Chill" có điểm Trending 0; danh mục có 11 Topic | Hệ thống xếp hạng Topic | Bảng xếp hạng có đủ 11 Topic, "Góc Chill" có mặt | — |
| T-153 | ISH-M05-008.19 | Công thức | Tag hoạt động "anova" gắn trên một bài viết được tính, điểm 0; Tag "spam" bị vô hiệu hóa | Hệ thống xếp hạng Tag | "anova" có trong bảng xếp hạng; "spam" không có | — |
| T-154 | ISH-M05-008.1 | Thời gian | P24 gửi 8 ngày trước T, chờ Mod duyệt, trở thành công khai lần đầu 6 ngày trước T, 0 tương tác; Topic K chỉ có P24 | Tính điểm K | K = 1 (bài mới theo mốc công khai lần đầu) | — |
| T-155 | ISH-M05-008.1 | Thời gian | P25 công khai lần đầu 9 ngày trước T, bị Mod ẩn 5 ngày trước, khôi phục 2 ngày trước T, 0 tương tác; Topic K chỉ có P25 | Tính điểm K | K = 0 (lần công khai đầu tiên ngoài 7 ngày, không có điểm thưởng) | — |
| T-156 | ISH-M05-008.3 | Công thức | Topic K có P26 đã xuất bản nhưng đang bị gắn cờ chờ Mod xử lý, đăng 1 ngày trước, 2 upvote | Tính điểm K chỉ với P26 | K = 0 (P26 không phải bài viết công khai) | — |
| T-157 | ISH-M05-008.3 | Công thức | Topic K có P27 bị tác giả tự ẩn, đăng 1 ngày trước, 2 upvote | Tính điểm K chỉ với P27 | K = 0 | — |
| T-158 | ISH-M05-008.11 | Công thức | Tại T: "Khác" và "Khoa học tự nhiên" cùng 4 điểm, cùng 0 bài mới | Hệ thống xếp hạng Topic | "Khác" xếp trước "Khoa học tự nhiên" (theo bảng chữ cái tiếng Việt: "a" trước "o") | — |
| T-159 | ISH-M05-008.12 | Công thức | Tại T: Tag "đạisố", "dãysố", "Bayes", "anova" cùng 2 điểm, cùng 0 bài mới | Hệ thống xếp hạng Tag | Thứ tự: "anova", "Bayes", "dãysố", "đạisố" (không phân biệt hoa–thường; "d" trước "đ") | — |
| T-160 | ISH-M05-011.6 | Thường | "Góc Chill" có điểm 8 trước khi gộp | Mod M gộp "Góc Chill" vào "Kỹ năng mềm"; hệ thống xếp hạng Topic | "Góc Chill" không có trong bảng xếp hạng | — |
| T-161 | ISH-M05-007.7 | Vi phạm | "Góc Chill" đã bị gộp vào "Kỹ năng mềm" | User A yêu cầu theo dõi "Góc Chill" | Hệ thống từ chối; User A không theo dõi "Góc Chill" | — |
| T-162 | ISH-M05-011.8 | Vi phạm | "Góc Chill" đã bị gộp vào "Kỹ năng mềm" | Mod M yêu cầu gộp "Khác" vào "Góc Chill" | Hệ thống từ chối; "Khác" vẫn trong danh mục, bài viết của "Khác" không đổi | — |
| T-163 | ISH-M05-011.8 | Vi phạm | "Góc Chill" đã bị gộp vào "Kỹ năng mềm" | Admin D yêu cầu gộp "Góc Chill" vào "Khác" | Hệ thống từ chối; danh mục không đổi | — |
| T-164 | ISH-M05-011.9 | Vi phạm | Như T-162 | Mod M yêu cầu gộp "Khác" vào "Góc Chill" | Hệ thống thông báo cho Mod M rằng Topic không tồn tại | — |
| T-165 | ISH-M05-011.10 | Vi phạm | Danh mục có "Tin học" | Mod M yêu cầu gộp "Tin học" vào "Tin học" | Hệ thống từ chối; danh mục và bài viết không đổi | — |
| T-166 | ISH-M05-012.1 | Vi phạm | "spam" đã bị vô hiệu hóa, gắn trên 3 bài | Mod M vô hiệu hóa "spam" lần nữa | "spam" vẫn bị vô hiệu hóa; vẫn ẩn trên 3 bài | — |
| T-167 | ISH-M05-012.5 | Vi phạm | "bayes" đang hoạt động, gắn trên 2 bài | Admin D mở lại "bayes" | "bayes" vẫn hoạt động; vẫn hiển thị trên 2 bài | — |
| T-168 | ISH-M05-007.2 | Vi phạm | User A chưa theo dõi "Ngữ văn" (3 người theo dõi) | User A yêu cầu bỏ theo dõi "Ngữ văn" | User A vẫn chưa theo dõi; số người theo dõi vẫn là 3 | — |
| T-169 | ISH-M05-005.5 | Vi phạm | Bài của User A gửi lần đầu với gợi ý còn mới (đã ghi 1 phản hồi), bị Mod từ chối; User A không sửa tiêu đề, nội dung | User A gửi lại bài | Không ghi thêm phản hồi; bài viết vẫn có đúng 1 phản hồi gợi ý Topic | — |
| T-170 | ISH-M05-005.5 | Biên | Như T-169, User A sửa nội dung bài viết (bài đã gửi nên không nhận được gợi ý mới) | User A gửi lại bài | Không ghi thêm phản hồi; bài viết vẫn có đúng 1 phản hồi (của lần gửi đầu) | — |
| T-171 | ISH-M05-007.1 | Thường | "Tin học" trong danh mục; User A chưa theo dõi | User A theo dõi "Tin học" | User A đang theo dõi "Tin học" | — |
| T-172 | ISH-M05-010.5 | Vi phạm | "Góc Chill" đã bị gộp vào "Kỹ năng mềm" | Admin D yêu cầu đổi tên "Góc Chill" thành "Thư giãn" | Hệ thống từ chối; danh mục không có "Thư giãn" | — |
| T-173 | ISH-M05-008.19 | Công thức | Tag "đềthi12a1" (hoạt động) chỉ gắn trên một bản nháp và một bài trong Group Private; Tag "bayes" gắn trên một bài viết được tính, 0 điểm | Hệ thống xếp hạng Tag | "bayes" có trong bảng xếp hạng (0 điểm); "đềthi12a1" không có | — |
| T-174 | ISH-M05-008.12 | Công thức | Tại T: Tag "anh", "2k8", "java", "kotlin" cùng 1 điểm, cùng 0 bài mới | Hệ thống xếp hạng Tag | Thứ tự: "2k8", "anh", "java", "kotlin" (chữ số trước chữ cái; j trước k) | — |
| T-175 | ISH-M05-008.12 | Công thức | Tại T: Tag "nghỉhè" và "nghĩhè" cùng 1 điểm, cùng 0 bài mới | Hệ thống xếp hạng Tag | "nghỉhè" (hỏi) xếp trước "nghĩhè" (ngã) | — |
| T-176 | ISH-M05-008.12 | Công thức | Tại T: Tag "c" và "c_" cùng 1 điểm, cùng 0 bài mới | Hệ thống xếp hạng Tag | "c" xếp trước "c_" (so từng ký tự; tên hết ký tự trước xếp trước, theo thứ tự từ điển) | — |
| T-177 | ISH-M05-008.20 | Công thức | Tag hoạt động "đềthi12a1" chỉ gắn trên một bài đang chờ duyệt và một bài trong Group Private | Hệ thống xếp hạng Tag | "đềthi12a1" không có trong bảng xếp hạng | — |
| T-178 | ISH-M05-008.20 | Công thức | Tag "xacsuat" gắn trên một bài viết được tính; bài đó bị Mod ẩn | Hệ thống xếp hạng Tag lần tiếp theo | "xacsuat" không còn trong bảng xếp hạng (không còn bài viết được tính) | — |
| T-179 | ISH-M05-010.6 | Vi phạm | "Góc Chill" đã bị gộp vào "Kỹ năng mềm" | Mod M yêu cầu đổi tên "Góc Chill" | Hệ thống thông báo cho Mod M rằng Topic không tồn tại | — |
| T-180 | ISH-M05-008.12 | Công thức | Tại T: Tag "ban" và "bá" cùng 1 điểm, cùng 0 bài mới | Hệ thống xếp hạng Tag | "bá" xếp trước "ban" (bước 1 so "ba" với "ban"; "ba" là phần đầu) | — |
| T-181 | ISH-M05-008.12 | Công thức | Tại T: Tag "_a", "1a", "a" cùng 1 điểm, cùng 0 bài mới | Hệ thống xếp hạng Tag | Thứ tự: "_a", "1a", "a" (ký hiệu trước chữ số, chữ số trước chữ cái) | — |
| T-182 | ISH-M05-003.15 | Vi phạm | Bài viết đã gửi của User A, tiêu đề cộng nội dung 40 tiếng | User A sửa bài viết đó rồi yêu cầu gợi ý Topic | Hệ thống từ chối yêu cầu; không gọi dịch vụ AI; Topic của bài viết không đổi | — |
| T-183 | ISH-M05-003.16 | Biên | User A đã gửi 9 yêu cầu gợi ý hợp lệ và 5 yêu cầu bị từ chối vì văn bản ít hơn 10 tiếng, tất cả trong cùng một phút | User A gửi yêu cầu gợi ý hợp lệ thứ 10 trong phút đó | Yêu cầu được chấp nhận (5 yêu cầu bị từ chối vì văn bản ngắn không tính vào giới hạn) | — |
| T-184 | ISH-M05-003.16 | Biên | Như T-183 và yêu cầu hợp lệ thứ 10 đã được chấp nhận | User A gửi yêu cầu gợi ý hợp lệ thứ 11 trong cùng phút | Yêu cầu bị từ chối vì đã đủ 10 yêu cầu hợp lệ; 5 yêu cầu bị từ chối vì văn bản ngắn không làm tăng số đếm | — |
| T-185 | ISH-M05-006.8 | Vi phạm | User A đang gắn Tag cho bài viết | User A nhập "#c++" | Hệ thống từ chối Tag "c++" (có ký tự "+") | — |
| T-186 | ISH-M05-006.8 | Vi phạm | User A đang gắn Tag cho bài viết | User A nhập "#kt&pl" | Hệ thống từ chối Tag "kt&pl" (có ký tự "&") | — |
| T-187 | ISH-M05-006.8 | Thường | User A đang gắn Tag cho bài viết | User A nhập "#xác_suất_2024" | Tag "xác_suất_2024" được chấp nhận (chữ có dấu, dấu gạch dưới và chữ số) | — |
| T-188 | ISH-M05-006.8 | Vi phạm | User A đang gắn Tag cho bài viết | User A nhập "#bayes!" | Hệ thống từ chối Tag "bayes!" (có dấu chấm than) | — |
| T-189 | ISH-M05-006.8 | Vi phạm | User A đang gắn Tag cho bài viết | User A nhập "#toán😀" | Hệ thống từ chối Tag (có biểu tượng cảm xúc) | — |
| T-190 | ISH-M05-006.17 | Biên | Bài viết của User A có 4 Tag hoạt động và Tag "spam" đã bị vô hiệu hóa (chip ẩn, liên kết còn) | User A sửa bài, thêm Tag "anova" | Hệ thống từ chối "anova" vì bài đã có 5 Tag kể cả "spam"; bài vẫn có 5 Tag | — |
| T-191 | ISH-M05-006.17 | Biên | Bài viết của User A có 3 Tag hoạt động và Tag "spam" đã bị vô hiệu hóa (tổng 4 Tag) | User A thêm Tag "anova"; sau đó Mod M mở lại "spam" | "anova" được chấp nhận (tổng 5 Tag); sau khi mở lại, bài hiển thị đúng 5 Tag, không vượt 5 | — |
| T-192 | ISH-M05-006.18 | Thường | User A nhập "#Bayes" khi gắn Tag cho bài viết công khai | Guest mở bài viết | Guest thấy Tag hiển thị "#bayes" | — |
| T-193 | ISH-M05-007.4 | Quyền | Topic "Tin học" có 3 người đang theo dõi | Guest xem danh sách Topic | Guest thấy số người đang theo dõi của "Tin học" là 3 | — |
| T-194 | ISH-M05-007.8 | Thường | Topic "Tin học" có 4 người theo dõi: User A (hoạt động), User B (tài khoản bị vô hiệu hóa), User C (tài khoản bị cấm), User D (tài khoản đã xóa) | Người dùng xem số người đang theo dõi "Tin học" | Số hiển thị là 3 (A, B, C); D không được đếm | — |
| T-196 | ISH-M05-010.7 | Vi phạm | Mod M đăng nhập; Topic "Tin học" trong danh mục | Mod M đổi tên "Tin học" thành tên rỗng | Hệ thống từ chối; tên vẫn là "Tin học" | — |
| T-197 | ISH-M05-010.8 | Vi phạm | Mod M đăng nhập; danh mục có "Toán học" và "Tin học" | Mod M đổi tên "Tin học" thành "TOÁN HỌC" | Hệ thống từ chối vì trùng "Toán học" (không phân biệt chữ hoa, chữ thường); tên vẫn là "Tin học" | — |
| T-198 | ISH-M05-010.8 | Thường | Mod M đăng nhập; danh mục có "Toán học" và "Tin học" | Mod M đổi tên "Tin học" thành "Tin học 2" | Đổi tên được chấp nhận; Topic tên "Tin học 2" | — |
| T-201 | ISH-M05-003.10 | Chuyển trạng thái | Tác giả vừa nhận gợi ý Topic (gợi ý còn mới) (bài viết chưa gửi) | Tác giả sửa tiêu đề bài viết | Gợi ý chuyển sang gợi ý cũ; cảnh báo gợi ý cũ hiển thị | — |
| T-202 | ISH-M05-003.4 | Chuyển trạng thái | Gợi ý Topic của bài viết chưa gửi đang là gợi ý cũ | Tác giả yêu cầu gợi ý lại và nhận gợi ý mới | Lựa chọn Topic được thay bằng gợi ý mới; gợi ý chuyển sang gợi ý còn mới; cảnh báo gợi ý cũ không còn hiển thị | — |
| T-203 | ISH-M05-003.13 | Chuyển trạng thái | Gợi ý Topic của bài viết đang là gợi ý cũ (tổng tiêu đề cộng nội dung ít nhất 10 tiếng) (bài viết chưa gửi) | Tác giả yêu cầu gợi ý Topic lại | Yêu cầu được chấp nhận, không bị từ chối vì gợi ý cũ | — |
| T-204 | ISH-M05-007.1 | Chuyển trạng thái | User A đã đăng nhập, chưa theo dõi "Tin học" | User A yêu cầu theo dõi "Tin học" | User A chuyển sang đang theo dõi "Tin học"; số người theo dõi tăng thêm 1 | — |
| T-205 | ISH-M05-007.2 | Chuyển trạng thái | User A đang theo dõi "Tin học" | User A yêu cầu bỏ theo dõi "Tin học" | User A chuyển sang chưa theo dõi; số người theo dõi giảm 1 | — |
| T-206 | ISH-M05-007.7 | Chuyển trạng thái | Topic "Góc Chill" đã bị gộp vào "Kỹ năng mềm" (đã loại khỏi danh mục) | User A yêu cầu theo dõi "Góc Chill" | Hệ thống từ chối; User A không theo dõi "Góc Chill" | — |
| T-207 | ISH-M05-011.2 | Chuyển trạng thái | Danh mục có 11 Topic gồm "Góc Chill" và "Kỹ năng mềm" | Mod M gộp "Góc Chill" vào "Kỹ năng mềm" | "Góc Chill" bị loại khỏi danh mục (trạng thái cuối); danh mục còn 10 Topic | — |
| T-208 | ISH-M05-011.3 | Chuyển trạng thái | User B đang theo dõi "Góc Chill" | Mod M gộp "Góc Chill" vào "Kỹ năng mềm" | User B đang theo dõi "Kỹ năng mềm" và không còn theo dõi "Góc Chill" | — |
| T-209 | ISH-M05-011.8 | Chuyển trạng thái | "Góc Chill" đã bị loại khỏi danh mục | Mod M yêu cầu gộp "Góc Chill" vào "Tin học" | Hệ thống từ chối thao tác gộp; "Tin học" và danh mục không đổi | — |
| T-210 | ISH-M05-012.1 | Chuyển trạng thái | Tag "spam" đang hoạt động, gắn trên 3 bài viết | Mod M vô hiệu hóa "spam" | "spam" chuyển sang bị vô hiệu hóa; không hiển thị trên cả 3 bài viết | — |
| T-211 | ISH-M05-012.5 | Chuyển trạng thái | Tag "spam" đang bị vô hiệu hóa, gắn trên 3 bài viết | Admin D mở lại "spam" | "spam" chuyển sang hoạt động; hiển thị lại trên cả 3 bài viết | — |
| T-212 | ISH-M05-003.15 | Vi phạm | Bài viết đã gửi của User A từng nhận gợi ý Topic; tiêu đề cộng nội dung 40 tiếng | User A sửa nội dung bài viết đó rồi yêu cầu gợi ý Topic | Hệ thống từ chối yêu cầu; không hiển thị cảnh báo gợi ý cũ; không gọi dịch vụ AI | — |
