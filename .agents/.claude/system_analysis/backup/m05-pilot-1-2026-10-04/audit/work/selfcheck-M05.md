# Selfcheck — ISH-SR-M05 phiên bản 0.3
<!-- [Vietnamese Doc] -->

Ngày: 2026-10-04 · Tác giả: Phạm Văn Đức · check_sr (inventory chạy lại sau khi ghi register mới): ERROR=0, WARN=0, INFO=7 (7× COV-03: nguồn vừa ở SR vừa ở routing — hợp lệ, giải thích ở routing)

Bản v0.1 qua `ISH-AUD-M05-r1` (Chưa đạt, 4 finding) → sửa thành v0.2 → v0.2 qua `ISH-AUD-M05-r2` (Chưa đạt, 2 DEFECT hồi quy + 1 OBSERVATION, cả 4 finding vòng 1 xác nhận đã sửa đúng) → sửa thành v0.3. Theo RULES §8.4, tối đa 2 vòng audit — không mở vòng 3; 2 DEFECT hồi quy của vòng 2 là lỗi máy móc (thiếu dòng routing, thiếu mục 2.1) nên đã tự sửa thẳng; OBSERVATION (ranh giới M05/M07/M14) đã ghi chú cho Author sau, không cần sửa SR.

| Mã | Kết quả | Bằng chứng / ghi chú |
|---|---|---|
| CL-A01 | Đạt | DRAFT §3.1→001; §3.2→004.1; §3.3/§3.4→R5; §4.5→007; §11.2→R7 (DEC-050/051 chỉ Topic, không Tag) |
| CL-A02 | Đạt | **Sửa theo AUD-M05-01.** Nguyên nhân v0.1: `check_sr` chạy với `inventory-M05.json` cũ (sinh trước khi ghi ISS-207/QA-267/DEC-140 vào register) nên không thấy 3 ERROR COV-01 — tự kiểm bằng inventory cũ là sai quy trình (RULES: "luôn chạy lại inventory khi tiếp tục"). Đã chạy lại inventory sau khi ghi mọi register mới; `check_sr` hiện ERROR=0 (OWNED=28) |
| CL-A03 | Đạt | **Sửa theo AUD-M05-02/03.** `disposition-M05.md` đã cập nhật: DEC-132/ISS-194/QA-253 chuyển từ "không liên quan" sang SR (lý do cũ sai — nội dung chỉ riêng M05, không áp dụng module khác); QA-043/ISS-051 (Follow) thêm dòng, chuyển sang SR |
| CL-A04 | Đạt | `check_sr` COV-02 = 0 |
| CL-A05 | Đạt | Đối chiếu nguyên văn DEC-047…052/090/093/099/008/132/141, QA-043 — khớp nghĩa |
| CL-A06 | Đạt | Mọi dòng "Suy ra" có Ghi chú; `check_sr` TRC-08 không WARN |
| CL-A07 | Đạt | Số liệu cũ đã grep-khớp (xem lịch sử v0.1); số liệu mới (11 Topic trong whitelist của 002.9) dùng lại đúng danh sách DEC-048, không có số liệu mới cần kiểm thêm |
| CL-A08 | Đạt | Tag "không giới hạn" (DRAFT §3.2) vs "tối đa 5" (DEC-051) — ghi cả hai nguồn ở 004.1, đã xử lý từ v0.1 |
| CL-A09 | Đạt | QA-033/ISS-046 (2 tầng) → routing R6, "bị thay bởi" DEC-140 |
| CL-A10 | Đạt | **Sửa theo AUD-M05-05 (vòng 2).** Thêm dòng routing R5 cho phần DEC-141 thuộc M07 (gửi thông báo khi Topic theo dõi có bài mới); COV-03 (DEC-049/050/051/052/141, QA-104) — SR giữ hành vi, routing giữ phần thuộc module khác/cơ chế lưu trữ, không trùng |
| CL-B01 | Đạt | `check_sr` EARS-01/02/03 = 0 |
| CL-B02 | Đạt | `check_sr` RULE-01/02/08 = 0 |
| CL-B03 | Đạt | `check_sr` RULE-04 = 0 |
| CL-B04 | Đạt | `check_sr` RULE-03 = 0 |
| CL-B05 | Đạt | `check_sr` RULE-05 = 0 |
| CL-B06 | Đạt | `check_sr` RULE-06/07 = 0 |
| CL-B07 | Đạt | `check_sr` RULE-09 = 0 |
| CL-B08 | Đạt | Ca kiểm Given/When/Then thử cho mẫu có chủ đích gồm cả 3 yêu cầu mới (002.9, 007, 007.1, 007.2) — viết được |
| CL-B09 | Đạt | **Sửa theo AUD-M05-02.** Đã thêm ISH-M05-002.9 cho nhánh "AI trả Topic ngoài danh sách 11 giá trị hợp lệ" (nguồn DEC-132), nhánh còn thiếu duy nhất mà Auditor vòng 1 chỉ ra |
| CL-B10 | Đạt | Mỗi giới hạn độc lập một yêu cầu cấp dưới riêng; 007.1/007.2 là hai hành vi tách biệt (bỏ theo dõi, hiển thị số lượng), không gộp |
| CL-B11 | Đạt | Quyền Mod/Admin viết riêng (003, 005); Follow (007) không có phân quyền đặc biệt — mọi User đều theo dõi được, đúng nguồn |
| CL-C01 | Đạt | Đọc lại 40 yêu cầu (sau khi thêm 002.9, 007, 007.1, 007.2) theo đối tượng — không có cặp mâu thuẫn |
| CL-C02 | Đạt | Không câu nào chỉ lặp lại cấp trên |
| CL-C03 | Đạt | **Sửa theo AUD-M05-06 (vòng 2).** Nhận định v0.2 ("từ phổ thông không cần định nghĩa") sai so với RULES §3 (yêu cầu **mọi** thuật ngữ dùng trong tài liệu, không có ngoại lệ phổ thông) — đã thêm dòng "Theo dõi" vào 2.1 |
| CL-C04 | Đạt | "Lý do" của ISH-M05-007 lấy từ DRAFT §4.5 ("Muốn nhận cập nhật về nội dung hoặc chủ đề") |
| CL-C05 | Đạt | 5.1 có đủ 7 dòng khớp 5.3-5.9; Theo dõi Topic gắn Must/P1 (khớp `iShare_dev_priority.md` Giai đoạn 2, Interaction: "Follow (...)"); 5.2 không đổi |
| CL-D01 | Đạt | `check_sr` HDR-01…08 = 0 |
| CL-D02 | Đạt | `check_sr` STR-01…09 = 0 (đã kiểm lại số thứ tự 5.1-5.11 liên tục sau khi chèn 5.9 mới) |
| CL-D03 | Đạt | `check_sr` REQ-00…04 = 0 |
| CL-D04 | Đạt | `check_sr` ID-01…06 = 0; ID cũ (001-006, .x) giữ nguyên không đổi nghĩa; ID mới (002.9, 007, 007.1, 007.2) lấy số tiếp theo chưa dùng |
| CL-D05 | Đạt | `check_sr` TRC-01…10 = 0; 40/40 ID có dòng Phụ lục A |
| CL-D06 | Đạt | `check_sr` REF-01/02 = 0 |
| CL-E01 | Đạt | Không có tên bảng/trường/công nghệ/giao diện trong các yêu cầu mới |
| CL-E02 | Đạt | Follow Topic viết đúng ở M05 (module sở hữu Topic) theo xác nhận stakeholder (DEC-141), không viết Follow cho Tag (ngoài phạm vi theo QA-268) |
| CL-E03 | Đạt | **Sửa theo AUD-M05-05 (vòng 2).** R5 nay có 2 dòng (grade_level→M03/M02; thông báo Follow→M07); R7 có lý do cụ thể (QA-269) |
| CL-E04 | Đạt | Không đổi |
| CL-F01 | Đạt | `check_sr` OPN-01…03 = 0; Phụ lục B vẫn 6 OP (không đổi, các finding vòng 1 không tạo OP mới — đã xử lý thẳng bằng DEC/QA) |
| CL-F02 | Đạt | Dòng cuối Lịch sử (0.2) khớp header (0.2); dòng 0.2 mô tả đúng 4 thay đổi thực tế |
| CL-F03 | Đạt | **Sửa theo AUD-M05-01.** ISS-207/QA-267/DEC-140 giờ có mặt ở Phụ lục A (001.5); ISS-208/QA-268/DEC-141 và ISS-209/QA-269 có mặt ở Phụ lục A (007) / routing R7 |
| CL-F04 | Đạt | **Sửa theo AUD-M05-03.** Follow Topic/Tag đã raise cho stakeholder (câu hỏi riêng), ghi QA-268/DEC-141, không còn là quyết định ngầm |
| CL-F05 | Đạt | `grep "phải"` mục 1-4 → 0 kết quả (không đổi, mục 1-4 không sửa) |
| CL-F06 | Đạt | Không đổi |

## WARN giữ lại

| Mã WARN | ID | Lý do giữ |
|---|---|---|
| (không có — check_sr WARN=0) | | |

## Điểm đã raise cho stakeholder

| OP / ISS / QA | Vấn đề | Trạng thái |
|---|---|---|
| ISS-207 / QA-267 / DEC-140 | Topic flat hay 2 tầng Category→Topic | Đã trả lời — Flat (A) |
| ISS-208 / QA-268 / DEC-141 | Follow Topic/Tag thuộc module nào, áp dụng cho Tag không | Đã trả lời — M05 sở hữu, chỉ Topic (không Tag) |
| ISS-209 / QA-269 | AI có nên gợi ý cả Tag không | Đã trả lời — Không, Tag giữ hoàn toàn tự do |
| OP-M05-01…05 | Lý do chưa nêu cho 5 tính năng gốc (F2-F6) | Mở — đã báo ở Bước 8 vòng 1, chưa cần quyết định ngay |
| OP-M05-06 | Ranh giới M05/M14 cho hiển thị Trending | Mở — không chặn bàn giao M05 |
| (không có ID riêng) | DRAFT §3.2 ("Tag không giới hạn") lệch DEC-051/QA-105 ("tối đa 5") | Đã xử lý theo RULES §7.5; đã báo ở Bước 8 vòng 1 |
| AUD-M05-07 (OBSERVATION, vòng 2) | module-registry ("M14 Following reuses Follow targets from M07") chưa đối chiếu với DEC-141 | Không sửa SR M05 (không chặn bàn giao); đã ghi chú dẫn chiếu DEC-141 ở `disposition-M05.md` cho Author M07/M14 sau này đọc trước khi viết SR của họ |
