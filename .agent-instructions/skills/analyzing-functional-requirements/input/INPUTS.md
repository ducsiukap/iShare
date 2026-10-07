# Đầu vào của skill

Mọi đường dẫn tính từ gốc repo iShare. Thiếu một tệp **bắt buộc** thì dừng và báo người dùng, không làm tiếp.

## Nguồn yêu cầu (được trích trong tài liệu FR)

| Tệp | Vai trò | Mã nguồn trong chỉ mục | Bắt buộc |
|---|---|---|---|
| `.agents/.claude/system_analysis/output/registers/decisions.md` | Quyết định của stakeholder. Có 3 kiểu ghi: bảng (DEC-001…006), khối có trường (DEC-007…020), tiêu đề `### DEC-nnn: …` | `DEC-nnn` | Có |
| `.agents/.claude/system_analysis/output/registers/qa-log.md` | Câu hỏi và câu trả lời phỏng vấn | `QA-nnn` | Có |
| `.agents/.claude/system_analysis/output/registers/issue-queue.md` | Vấn đề đã nêu trong phỏng vấn (một ID có thể xuất hiện hai lần: backlog và đã đóng) | `ISS-nnn`, `ISS-XXX-nn` | Có |
| `.agents/.claude/system_analysis/output/registers/open-issues.md` | Điểm hoãn có chủ đích; dùng để ghi TBD, không hỏi lại | `OPEN-nnn` | Có |
| `.agents/.claude/system_analysis/output/registers/glossary.md` | Thuật ngữ của dự án | `GL:<thuật ngữ>` | Có |
| `.agents/.claude/system_analysis/output/registers/module-registry.md` | Danh sách module, MoSCoW, các đợt sửa phạm vi, bảng tính năng, bảng AI fallback | `MR-Mxx`, `MR-Ann`, `F-XXX-nn`, `MR-FB-Mxx` | Có |
| `.agents/.claude/system_analysis/output/registers/assumptions.md` | Giả định đã được xác nhận (hiện trống) | `ASM-nnn` | Không |
| `docs/_temp/iShare_modules.md` | Draft: module và tính năng | `DM-<số mục>` | Có |
| `docs/_temp/iShare_specs_general.md` | Draft: tổng quan dự án, nguyên tắc, phạm vi AI, những gì không làm | `DG-<số mục>` | Có |

Thứ tự ưu tiên khi nguồn nói khác nhau về **cùng một điều**: DEC mới > DEC cũ > câu trả lời QA > ISS > draft.
Khác phạm vi thì không phải mâu thuẫn, cả hai cùng hiện hành.

## Chỉ để tham khảo (không trích làm nguồn yêu cầu)

| Tệp | Dùng để |
|---|---|
| `docs/_temp/system_requirement_demo/system_requirement_demo.md` | Tài liệu mẫu của stakeholder; chỉ lấy cấu trúc mục (đã phản ánh trong `output/fr-template.md`) |
| `docs/_temp/iShare_dev_priority.md` | Tham khảo thứ tự làm; không phải nguồn yêu cầu, không phải nguồn ưu tiên. Ưu tiên lấy từ cột MoSCoW của module-registry |
| Các tệp `FR-Myy.md` khác trong `output/fr/` | Đối chiếu phần giao tiếp module ở bước 7 |

## Lưu ý về dữ liệu hiện tại

- Cột MoSCoW và Dependencies của `module-registry.md` bị lệch ở các dòng M02–M10 và M13. Không dựa vào cột
  Dependencies để sinh dependency keyword. Ưu tiên không đọc được thì ghi TBD ở mục 4.5 và báo ở cổng.
- Register theo phase cũ (Phase 0–4) không có section theo module, nên nhiều quyết định của một module nằm ở
  section khác. Đây là lý do bước 1 quét cả theo keyword.
- Ghi chú sửa đổi trong register có nhiều kiểu (`[Amended …]`, `AMENDED by`, `supersedes`, `[Clarified …]`,
  câu "… is amended"). `lineage.py` nhận các kiểu này; sửa đổi viết bằng lời thường thì agent phải tự phát hiện.

## Không dùng

- Bộ skill SR cũ đã lưu trữ: `.agent-instructions/_archive/sr-v1-2026-10/`.
- Phần quy trình và quy ước mã của DEC-139 (đã đánh dấu sẽ bị thay). Phần còn hiệu lực của DEC-139
  (mỗi module một tài liệu, tiếng Việt, cấu trúc theo tài liệu mẫu, một hành vi một module sở hữu, nguồn ở phụ lục)
  đã được đưa vào mẫu đầu ra.
- Thư mục `_to_delete/`.
