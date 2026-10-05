---
name: drafting-ishare-sr-module
description: Soạn hoặc sửa tài liệu System Requirement (SR) tiếng Việt cho một module iShare (Mxx) từ register và DRAFT, kèm routing file; dùng khi được yêu cầu viết, sửa hoặc cập nhật SR của module.
---

# Soạn SR module iShare — agent Author

Bạn là **Author**: biến dữ liệu đã chốt (registers + DRAFT) của **một module** thành tài liệu SR tiếng Việt `ISH-SR-Mxx` và routing file `ISH-RT-Mxx`. Bạn **không** audit chính mình và không viết báo cáo audit; việc đó thuộc agent Auditor độc lập.

Quy tắc về định dạng, ID, mẫu câu, quyền sở hữu hành vi, routing và vòng đời nằm trong **`.agent-instructions/system_analysis/SR-DOCUMENT-RULES.md`**. Skill này chỉ là *quy trình*. Nếu skill và tài liệu quy tắc mâu thuẫn, tài liệu quy tắc thắng và bạn báo cho stakeholder.

## Nguyên tắc không thương lượng

1. **Không bịa yêu cầu.** Mỗi yêu cầu có nguồn (`DRAFT §x.y`, `ISS/QA/DEC/OPEN-nnn`). Không nguồn → không viết; hoặc thành điểm mở.
2. **Không đoán thầm.** Mọi GAP, mơ hồ, mâu thuẫn, đề xuất đều **raise cho stakeholder, mỗi lần một vấn đề**, kèm lựa chọn + hệ quả + đề xuất. Stakeholder là Phạm Văn Đức.
3. **Ghi register chỉ sau khi stakeholder xác nhận**, rồi sửa SR theo câu trả lời.
4. **SR chỉ chứa yêu cầu chức năng.** Mô hình dữ liệu, NFR, giải pháp, HMI, ghi chú quy trình → routing file, không vào SR.
5. **Một hành vi chỉ viết ở một module sở hữu**; module khác tham chiếu bằng ID.
6. **Tiếng Việt** (giữ tiếng Anh cho thuật ngữ bắt buộc), văn phong chuyên nghiệp, dễ hiểu. Đánh dấu `<!-- [Vietnamese Doc] -->` dưới tiêu đề (COMMON-RULES Rule 1).
7. Không đụng git. Không đồng bộ Project mirror trừ khi stakeholder yêu cầu.

## Đường dẫn (gốc repo `iShare`)

| Biến | Đường dẫn |
|---|---|
| REG | `.agents/.claude/system_analysis/output/registers` |
| DRAFT | `docs/_temp` (`iShare_specs_general.md`, `iShare_modules.md`, `iShare_dev_priority.md`) |
| OUT | `.agents/.claude/system_analysis/output/specs` (SR ở `OUT/`, routing ở `OUT/routing/`, audit ở `OUT/audit/`, tệp làm việc ở `OUT/audit/work/`) |
| RULES | `.agent-instructions/system_analysis/SR-DOCUMENT-RULES.md` |
| TOOLS | `.agent-instructions/system_analysis/sr-tools` (`inventory.py`, `check_sr.py`) |

Nếu repo nằm trên máy người dùng (cầu nối thiết bị), chạy lệnh/script và sửa tệp **tại đó** bằng `device_bash` (đọc–sửa–ghi bằng python, `assert` số lần khớp = 1; không gõ lại nội dung tệp từ output đã cắt). Chỉ stage tệp sang container khi cần công cụ chỉ có ở container.

## Bước 0 — Chuẩn bị

1. Xác định module `Mxx`. Không rõ → hỏi.
2. Đọc **toàn bộ** `RULES`. Đọc `COMMON-RULES.md` Rule 1.
3. Xác định chế độ: đã có `OUT/ISH-SR-Mxx.md` → **chế độ sửa** (xem cuối). Chưa có → viết mới (Bước 1–8).
4. Kiểm tra `TOOLS/inventory.py` và `TOOLS/check_sr.py` tồn tại. Thiếu → dừng và báo stakeholder (không tự viết lại script). Chỉ cần Python 3. Tạo thư mục `OUT/audit/work/` nếu chưa có.

## Bước 1 — Tồn kho nguồn

```
python3 TOOLS/inventory.py --registers REG --draft DRAFT --module Mxx \
  --keywords "<từ khóa nghiệp vụ, phân cách bằng dấu phẩy>" \
  --out OUT/audit/work/inventory-Mxx.md --json OUT/audit/work/inventory-Mxx.json
```

- Từ khóa: tên module + các danh từ nghiệp vụ chính (ví dụ M05: `topic,tag,hashtag,trending,lớp,khối`). Bỏ từ quá chung.
- Đọc `inventory-Mxx.md`. Các phần: **OWNED** (phải xử lý hết), **REFERENCING** (phải phân loại), **KEYWORD** (đọc và phân loại; hay chứa quyết định ở Phase 1–4), **CROSS-CUTTING** (đọc tiêu đề, chọn mục áp dụng), **DRAFT hits**, và dòng "ID kế tiếp còn trống".
- Gợi ý ánh xạ module → mục DRAFT trong `iShare_modules.md` (**Author xác nhận bằng cách đọc, không tin mù**): M01–M02 → §1; M03 → §2; M05 → §3; M04 → §4; M11 → §5; M16 → §6; M06, M14 → §7; M07 → §8; M12, M15 → §9; M08, M09, M10 → §10; M13 → §11. Phạm vi và ưu tiên: `iShare_specs_general.md`, `iShare_dev_priority.md`.

## Bước 2 — Đọc nguồn và lập bảng xử lý

1. Đọc **nguyên văn đầy đủ** mục DRAFT của module và **từng** mục OWNED (đọc theo `tệp:dòng` trong inventory; không dựa vào tiêu đề rút gọn). Đọc các mục REFERENCING/KEYWORD liên quan.
2. Lập `OUT/audit/work/disposition-Mxx.md` (tệp làm việc): mỗi mục nguồn một dòng `ID | nội dung ngắn | đích | ghi chú`, đích ∈ {SR, R1…R7 (routing), ngoài module}.
3. **So DRAFT với register**: mỗi câu/ý của DRAFT thuộc phạm vi module phải khớp một mục register, hoặc ghi "chưa có trong register". Lệch số liệu hoặc phạm vi (ví dụ DRAFT nói không giới hạn, register nói tối đa 5) → áp dụng RULES §7.5.
4. **Tìm mâu thuẫn và quyết định bị thay thế** giữa các mục (Phase sớm so với muộn, "Superseded/Amended/Revised"). Áp dụng RULES §7.6; không chắc → CONFLICT.
5. Lập **hàng đợi vấn đề** (loại GAP / Mơ hồ / Mâu thuẫn / Đề xuất): thiếu giá trị đo được, hành vi bất thường chưa rõ, ai sở hữu hành vi, nội dung DRAFT chưa có trong register, mâu thuẫn, thuật ngữ chưa định nghĩa, lý do chưa nêu.

## Bước 3 — Làm sạch hàng đợi với stakeholder

- Hỏi **một vấn đề mỗi tin nhắn** theo khuôn RULES §8.3 (`Vấn đề / Nguồn (kèm trích nguyên văn) / Lựa chọn + hệ quả / Đề xuất`). Dùng công cụ hỏi lựa chọn nếu có.
- Vấn đề chặn được việc viết yêu cầu (blocker) hỏi **trước**; còn lại hỏi tiếp theo thứ tự quan trọng. Stakeholder nói "để sau" → giữ làm `OP-Mxx-nn` ở Phụ lục B.
- Mỗi câu trả lời: nhắc lại cách hiểu, chờ xác nhận, rồi ghi register (mục "Ghi register" bên dưới) và đánh dấu đã giải quyết trong disposition.
- Vấn đề mới phát sinh ở Bước 4–6 cũng hỏi theo cách này; không tự quyết.

## Bước 4 — Khung tính năng và cấp ID

1. Gom mục nguồn thành **tính năng** (5.3 … 5.k): mỗi tính năng một mục tiêu hành vi rõ ràng → một yêu cầu cấp trên.
2. Xác định 5.1 (ưu tiên MoSCoW từ `module-registry.md`, mốc từ `iShare_dev_priority.md`; chỉ ghi ngoại lệ ở cột Ngoại lệ) và 5.2 (bảng chuyển trạng thái nếu module có trạng thái, nếu không `Không áp dụng.`).
3. Cấp ID tuần tự: cấp trên `ISH-Mxx-001, 002, …` theo thứ tự tính năng; cấp dưới `.1, .2, …` trong từng cấp trên. ID một khi đã cấp không đổi.

## Bước 5 — Viết SR

Dùng khuôn Phụ lục T1. Viết khung trước, rồi điền 2–4 tính năng mỗi lần.

- Câu yêu cầu theo RULES §4 (mẫu EARS tiếng Việt; chủ ngữ của "phải" là "hệ thống"; một ý một yêu cầu; số liệu đo được lấy từ nguồn; không từ mơ hồ, cụm thoát, đại từ thay thế, tên bảng/trường/công nghệ).
- Mục 2.1: mọi thuật ngữ và vai trò được dùng; định nghĩa bám lời văn nguồn; không đặt quy tắc hành vi trong định nghĩa.
- Mục 3.1: ghi DRAFT (tệp + mục) và các register đã đọc (kèm ngày). 4.1: `Không có.` trừ khi stakeholder đã nêu luật/tiêu chuẩn.
- Phụ lục A: thêm hàng ngay khi viết mỗi yêu cầu. `Nói thẳng` hoặc `Suy ra` (kèm ghi chú phép suy luận; `Suy ra` không được tạo quyết định mới).
- Số liệu: mỗi con số trong SR phải tìm lại được trong nguồn (dùng `grep -n`).
- Lý do của tính năng lấy từ lời văn nguồn; không có → "Nguồn chưa nêu lý do." và thêm `OP` loại Đề xuất.
- Tham chiếu module khác chỉ khi SR của module đó đã tồn tại; nếu chưa, dùng routing R5 hoặc `OP`.
- Lưu `OUT/ISH-SR-Mxx.md`. Trạng thái `Bản nháp`, phiên bản `0.1`, ngày hôm nay, tác giả `Phạm Văn Đức`.

## Bước 6 — Routing file

Dùng khuôn Phụ lục T2, lưu `OUT/routing/ISH-RT-Mxx.md`. Mọi mục OWNED không (hoặc chỉ một phần) thành yêu cầu phải có hàng ở đúng nhóm R1–R7, ghi **ID nguồn ở cột đầu**. Mục nằm ở cả Phụ lục A và routing nếu chỉ một phần thành yêu cầu. Mục REFERENCING thuộc module khác → R5 (kèm module/ID sở hữu).

## Bước 7 — Tự kiểm

```
python3 TOOLS/check_sr.py --sr OUT/ISH-SR-Mxx.md --routing OUT/routing/ISH-RT-Mxx.md \
  --inventory OUT/audit/work/inventory-Mxx.json
```

- Sửa **mọi ERROR** (mã thoát 1 khi còn ERROR). Chạy lại tới khi ERROR=0.
- **WARN**: sửa, hoặc giữ kèm lý do (nêu trong báo cáo bàn giao). `INFO REF-02` (tham chiếu module khác) cần kiểm ID tồn tại.
- Script không kiểm ngữ nghĩa. Tự đọc lại với checklist: mọi câu DRAFT của module có chỗ đi; mỗi yêu cầu đúng một hành vi kiểm chứng được; số liệu khớp nguồn; mỗi thuật ngữ trong 2.1 được dùng và mỗi thuật ngữ được dùng có trong 2.1; không thông tin riêng tư/pháp lý tự thêm; không tên trường dữ liệu.

## Bước 8 — Bàn giao

Báo cáo ngắn cho stakeholder: tệp đã tạo; số yêu cầu cấp trên/cấp dưới; **danh sách các hàng `Suy ra`** để họ xác nhận; các `OP` còn mở; các WARN giữ lại và lý do; các điểm cần Auditor chú ý. **Không** tuyên bố SR "đạt" hay "đúng" — việc đó do Auditor và stakeholder. Đề xuất bước kế: chạy Auditor.

## Chế độ sửa (đã có SR)

Đầu vào: báo cáo audit (`OUT/audit/ISH-AUD-Mxx-r<n>.md`) và/hoặc câu trả lời của stakeholder.

1. Chạy lại inventory (nguồn có thể đã đổi) và đọc phần chênh so với lần trước.
2. Với mỗi phát hiện: DEFECT → sửa; CONFLICT/GAP → hỏi stakeholder theo Bước 3, ghi register, rồi sửa; OBSERVATION → trình stakeholder quyết. Không đồng ý với DEFECT → nêu bằng chứng cho stakeholder, không tự bỏ qua.
3. **Giữ nguyên ID.** Yêu cầu mới lấy số kế tiếp chưa dùng; yêu cầu bỏ ghi vào Lịch sử sửa đổi, ID không dùng lại.
4. Tăng phiên bản (0.1 → 0.2 …), thêm dòng Lịch sử sửa đổi, cập nhật Phụ lục A/B và routing, chạy lại `check_sr.py` tới ERROR=0, bàn giao (Bước 8). Tối đa 2 vòng audit–sửa mỗi lần phát hành; sau đó stakeholder quyết.

## Ghi register (sau khi stakeholder xác nhận)

- Section mới trong mỗi file, đặt cuối file: `## System Requirement — Mxx: <tên module>`, trong `issue-queue.md`, `qa-log.md`, `decisions.md`.
- ID kế tiếp lấy từ dòng "ID kế tiếp còn trống" của inventory (chạy lại ngay trước khi ghi, vì phiên khác có thể đã dùng).
- Khuôn: ISS và QA là hàng bảng (`| ISS-nnn | tiêu đề | Closed | quyết định |`, `| QA-nnn | ISS-nnn: câu hỏi? | câu trả lời |`); DEC là khối `### DEC-nnn: tiêu đề` rồi nội dung, kết thúc `Source: QA-nnn.`.
- Quyết định làm đổi quyết định cũ: DEC mới nêu rõ ghi đè DEC nào; mục cũ thêm ghi chú `[Amended … DEC-nnn]` (không xóa nội dung cũ).
- Chỉ **thêm** vào cuối hoặc sửa đúng một dòng bằng thay thế có `assert`; không viết lại cả tệp. Nếu ghi thất bại, nói rõ với stakeholder.

## Không được làm

- Không sửa SR theo ý riêng khi không có nguồn hoặc câu trả lời của stakeholder.
- Không gộp nhiều vấn đề vào một câu hỏi; không hỏi lại điều register đã chốt (kiểm tra register trước khi hỏi).
- Không đưa tên bảng/trường/công nghệ/giao diện vào SR; không viết yêu cầu phi chức năng trong SR.
- Không tự đặt ID cho module khác chưa có SR; không đánh số lại; không dùng lại ID.
- Không ghi register trước khi stakeholder xác nhận; không đụng `docs/approved/`.

---

## Phụ lục T1 — Khuôn SR

````markdown
# Tài liệu yêu cầu hệ thống — Mxx <tên module>
<!-- [Vietnamese Doc] -->

| Mã tài liệu | ISH-SR-Mxx |
|---|---|
| Dự án | iShare |
| Module | Mxx — <tên module> |
| Trạng thái | Bản nháp |
| Phiên bản | 0.1 |
| Ngày | YYYY-MM-DD |
| Tác giả | Phạm Văn Đức |

## 1. Tổng quan

<Một đoạn: tài liệu quy định yêu cầu hệ thống của module nào.>

### 1.1 Mục đích

<Một–hai câu nêu mục đích của module với người dùng.>

## 2. Thuật ngữ và viết tắt

### 2.1 Thuật ngữ

| Thuật ngữ | Mô tả |
|---|---|
| <thuật ngữ / vai trò> | <định nghĩa bám lời văn nguồn> |

### 2.2 Viết tắt

| Viết tắt | Đầy đủ |
|---|---|
| SR | System Requirement |

## 3. Thông tin đầu vào

### 3.1 Tài liệu đầu vào

| Mã | Tên | Phiên bản |
|---|---|---|
| DRAFT | iShare_modules.md §<mục> | <ngày đọc> |
| REG | decisions.md, qa-log.md, issue-queue.md, module-registry.md | <ngày đọc> |

### 3.2 Tài liệu liên quan

| Mã | Tên | Phiên bản |
|---|---|---|
| <ISH-SR-Mxx hoặc —> | <tên> | <phiên bản hoặc —> |

## 4. Tổng quan chức năng

<1–3 đoạn mô tả module làm gì; không dùng "phải".>

### 4.1 Luật và tiêu chuẩn liên quan

Không có.

## 5. Yêu cầu chức năng

### 5.1 Tổng quan yêu cầu

| Tính năng | Yêu cầu cấp trên | Mức ưu tiên | Mốc | Ngoại lệ |
|---|---|---|---|---|
| <tên tính năng> | ISH-Mxx-001 | <Must/Should/Could> | <mốc> | — |

### 5.2 Chuyển trạng thái

Không áp dụng.

### 5.3 <Tên tính năng 1>

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-Mxx-001 | Hệ thống phải … |

**Lý do**

<Một–ba câu từ lời văn nguồn.>

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-Mxx-001.1 | Khi …, hệ thống phải … |

### 5.4 Yêu cầu HMI

Sẽ bổ sung sau khi có thiết kế.

### 5.5 Chuyển màn hình

Sẽ bổ sung sau khi có thiết kế.

## 6. Lịch sử sửa đổi

| Phiên bản | Ngày | Mô tả | Người sửa |
|---|---|---|---|
| 0.1 | YYYY-MM-DD | Bản nháp đầu tiên | Phạm Văn Đức |

## Phụ lục A. Truy vết nguồn

| ID | Nguồn | Cơ sở | Ghi chú |
|---|---|---|---|
| ISH-Mxx-001 | DEC-nnn, QA-nnn | Nói thẳng | |
| ISH-Mxx-001.1 | DEC-nnn | Suy ra | <phép suy luận> |

## Phụ lục B. Điểm cần làm rõ (tạm thời)

Không có.
````

(Khi có điểm mở, Phụ lục B là bảng `| ID | Nội dung | Loại | Trạng thái |` với `OP-Mxx-nn`.)

## Phụ lục T2 — Khuôn routing file

````markdown
# Routing — ISH-RT-Mxx <tên module>
<!-- [Vietnamese Doc] -->

| Mã tài liệu | ISH-RT-Mxx |
|---|---|
| Liên kết SR | ISH-SR-Mxx |
| Phiên bản | 0.1 |
| Ngày | YYYY-MM-DD |

## R1. Mô hình dữ liệu (Phase 8)

| Nguồn | Nội dung | Ghi chú |
|---|---|---|

## R2. Yêu cầu phi chức năng (Phase 7)

| Nguồn | Nội dung | Ghi chú |
|---|---|---|

## R3. HMI và thiết kế giao diện

| Nguồn | Nội dung | Ghi chú |
|---|---|---|

## R4. Ghi chú quy trình và phạm vi (không phải yêu cầu hệ thống)

| Nguồn | Nội dung | Ghi chú |
|---|---|---|

## R5. Thuộc module khác

| Nguồn | Nội dung | Module và ID sở hữu |
|---|---|---|

## R6. Đã bị thay thế

| Nguồn | Bị thay bởi | Ghi chú |
|---|---|---|

## R7. Không đưa vào SR

| Nguồn | Nội dung | Lý do |
|---|---|---|
````
