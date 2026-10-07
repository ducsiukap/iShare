# Bước 6 — Hỏi để xác nhận GAP

## Mục đích

Đưa mọi chỗ còn thiếu trong phạm vi dữ liệu hiện có ra để người dùng xác nhận, ghi câu trả lời vào register,
rồi hoàn thiện yêu cầu.

## Đầu vào

Phụ lục B.1 (câu hỏi đã gom từ bước 2–5), mọi dòng `[GAP]`, ô `?` ở 4.3, ô `—` ở CRUD, Phụ lục B.3.

## Việc làm

1. **Lọc**:
   - Bỏ câu hỏi về hành vi mà không nguồn nào nhắc tới. Chỉ giữ lại nếu thiếu nó làm hành vi đã chốt không chạy
     được, hoặc chạm tới quyền hay an toàn dữ liệu; khi đó chuyển sang B.3 "Cần cân nhắc" kèm lý do.
   - Tìm trong `index.json` (đọc nguyên văn các mục có từ khóa liên quan) xem câu trả lời đã có chưa.
     Có rồi thì dùng, cập nhật yêu cầu, không hỏi.
   - **Câu mở rộng phạm vi**: nếu câu trả lời "có" sẽ tạo thêm một chức năng hoặc một quyền mới mà nguồn chưa có
     (ví dụ "Mod có được đổi Topic trên bài người khác không?" khi nguồn chưa nói Mod làm việc này), thì xếp loại
     **Cần cân nhắc**, ghi rõ "mở rộng phạm vi" trong câu hỏi, và tách thành nhóm riêng khi hỏi. Không xếp loại
     "Thiếu chi tiết".
2. **Xếp theo ảnh hưởng**:
   - **Cao**: làm đổi dữ liệu, trạng thái, quyền, phạm vi, hoặc điều người dùng thấy ở tình huống thường gặp;
     mọi mâu thuẫn. Hỏi riêng từng câu theo khuôn ở SKILL.md.
   - **Thấp**: chi tiết biên ít gặp. Gom theo chức năng thành danh sách xác nhận, mỗi dòng một đề xuất.
3. **Hỏi**: một tin nhắn gồm tối đa 5 câu ảnh hưởng cao cộng các danh sách xác nhận. Còn nhiều hơn thì chia
   thành nhiều lượt, mỗi lượt một nhóm chức năng. Đề xuất luôn suy từ dữ liệu hiện có, không đưa phương án mới
   ngoài phạm vi.
4. **Sau khi người dùng trả lời**, lập **bản nháp register** và trình cho người dùng:
   - `issue-queue.md`: thêm section `## Functional Requirement — Mxx: <Tên module>` (nếu chưa có), dòng
     `| ISS-nnn | <vấn đề> | Closed | Xem DEC-nnn |`.
   - `qa-log.md`: cùng tên section, dòng `| QA-nnn | ISS-nnn: <câu hỏi> | <câu trả lời, giữ lời người dùng> |`.
   - `decisions.md`: cùng tên section, khối `### DEC-nnn: <tiêu đề>` + nội dung + `Source: QA-nnn`.
     Nhiều câu trả lời cùng chủ đề có thể gộp một DEC.
   - Câu trả lời làm đổi một mục cũ: thêm dấu `**[Amended YYYY-MM-DD — DEC-nnn: <tóm tắt>]**` vào cuối mục cũ.
   - ID lấy từ `index_sources.py --next-ids`. Câu xác nhận theo đề xuất ("ok cả nhóm") vẫn được ghi, mỗi
     danh sách một QA.
5. **Chỉ ghi register sau khi người dùng xác nhận bản nháp.** Sau đó chạy lại `index_sources.py` và
   `scan_sources.py` (nguồn mới thuộc section mới sẽ vào nhóm A).
6. Cập nhật tệp FR:
   - thay mỗi `[GAP]` bằng yêu cầu có ID, căn cứ Nói thẳng, nguồn là QA/DEC mới;
   - B.1 điền cột Trả lời và Ghi vào register;
   - C.1 thêm dòng cho nguồn mới; `moc_nguon` cập nhật;
   - chạy lại `lineage.py` (register vừa có thêm dấu `[Amended …]`), rồi cập nhật cột Trạng thái của C.1 cho các
     nguồn bị DEC mới sửa ("Sửa một phần bởi DEC-nnn", "Bị thay bởi DEC-nnn");
   - viết lại **C.2** cho mọi chuỗi bị câu trả lời tác động: viết ở thì hiện tại (không còn "Sẽ …"), nêu nội dung
     đang hiệu lực sau DEC mới, và nội dung đó phải khớp với quy tắc và yêu cầu trong thân tài liệu
     (ví dụ công thức Trending ở C.2 phải giống BR tương ứng);
   - chỉ soát lại các yêu cầu bị câu trả lời tác động. Không mở GAP mới ngoài phạm vi câu trả lời. Nếu câu trả
     lời buộc phải có thêm một chi tiết mới viết được, hỏi tiếp đúng chi tiết đó và nói rõ vì sao.
7. Chạy `lint_fr.py --lineage …` và `trace_check.py --lineage …`. Cảnh báo C2-01, C2-02 nghĩa là C.2 chưa cập nhật.

## Tự kiểm trước cổng

- Không còn `[GAP]` nào chưa hỏi. GAP người dùng muốn để sau thì thành `TBD-Mxx-nn` ở B.2 với ảnh hưởng đúng mức.
- Mọi câu trả lời đã có trong register và được trích ở Phụ lục A.

## Trình ở cổng

Bảng câu hỏi – trả lời – ID register đã ghi; các câu **mở rộng phạm vi** đã được chấp nhận (liệt kê riêng);
các yêu cầu mới hoặc đã sửa; các dòng C.2 đã viết lại; TBD còn lại; kết quả tool.

## Không làm

Không ghi register trước khi người dùng xác nhận bản nháp. Không hỏi lại điều đã có câu trả lời trong register.
