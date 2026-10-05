# Báo cáo audit — ISH-AUD-M05-r2
<!-- [Vietnamese Doc] -->

| Mã báo cáo | ISH-AUD-M05-r2 |
| --- | --- |
| SR được audit | ISH-SR-M05, phiên bản 0.2 |
| Routing | ISH-RT-M05, phiên bản 0.2 |
| Vòng | 2 |
| Ngày | 2026-10-04 |
| Auditor | Agent Auditor độc lập |
| Kết luận | **Chưa đạt** |

## 1. Tóm tắt

Cả 4 finding của vòng 1 (AUD-M05-01…04) đã được Author sửa đúng và đủ: DEC-140/ISS-207/QA-267 đã vào cột Nguồn của Phụ lục A (ISH-M05-001.5); đã thêm ISH-M05-002.9 cho nhánh AI trả Topic ngoài whitelist; đã thêm tính năng mới "Theo dõi Topic" (ISH-M05-007, 007.1, 007.2) theo DEC-141/QA-268 (stakeholder đã trả lời: M05 sở hữu Follow cho Topic, không áp dụng Tag); đã thêm dòng routing R7 ghi nhận DRAFT §11.2 (AI gợi ý cả Tag) bị Phase 5 thu hẹp có chủ đích (QA-269). `check_sr.py` chạy lại với inventory mới (OWNED=28, tăng 5 mục so với vòng 1 do 5 mục nguồn mới DEC-141/ISS-208/ISS-209/QA-268/QA-269 được ghi sau khi trả lời) cho ERROR=0, WARN=0. Tuy nhiên bản sửa tạo ra hai DEFECT mới (hồi quy): (1) một phần nội dung của DEC-141 — thông báo cho người theo dõi khi Topic có bài mới thuộc trách nhiệm M07 — không có dòng routing R5 nào ghi nhận, nên không ai thấy được DEC-141 đã được xử lý hết; (2) thuật ngữ "theo dõi" được dùng 5 lần trong tài liệu (5.1, 5.9, ISH-M05-007/.1/.2) nhưng không có trong bảng 2.1 Thuật ngữ, trong khi Author tự chấm `Đạt` cho mục này. Vì còn 2 DEFECT mở sau vòng 2, kết luận là **Chưa đạt**, và theo quy tắc tối đa 2 vòng, các vấn đề còn lại chuyển cho stakeholder quyết hướng xử lý (mục 6), không mở vòng 3.

| Lớp \ Mức | Cao | Trung bình | Thấp |
|---|---|---|---|
| DEFECT | 0 | 1 | 1 |
| CONFLICT | 0 | 0 | 0 |
| GAP | 0 | 0 | 0 |
| OBSERVATION | 0 | 0 | 1 |

(Bảng trên chỉ tính finding còn mở của vòng này; AUD-M05-01…04 của vòng 1 đã Đã sửa — xem mục 8.)

## 2. Phạm vi và phương pháp

- Tệp đã đọc: `ISH-SR-M05.md` (v0.2, 2026-10-04), `ISH-RT-M05.md` (v0.2, 2026-10-04), báo cáo vòng 1 `ISH-AUD-M05-r1.md`, `decisions.md`, `issue-queue.md`, `qa-log.md`, `module-registry.md`, `open-issues.md`, `docs/_temp/iShare_modules.md`, `iShare_dev_priority.md`.
- Script: chạy lại `inventory.py` với tên tệp riêng vòng 2 (từ khóa: `topic,tag,chủ đề,thẻ,gộp,merge,trending,flat,phân loại,category,follow,theo dõi` — có thêm `follow,theo dõi` so với vòng 1 để bắt được các mục nguồn mới về Follow) → `WORK/audit-inventory-M05-r2.md/.json` (OWNED=28, so với vòng 1 là 23). `check_sr.py` → `WORK/check-M05-r2.json` (ERROR=0, WARN=0, INFO=6, toàn bộ INFO là COV-03 đã giải thích, giống vòng 1).
- Quy trình vòng 2: (a) chạy lại Bước 1 và Bước 3 đầy đủ; (b) kiểm từng finding vòng 1 theo bằng chứng mới; (c) dựng lại ma trận độ phủ cho các mục nguồn mới (DEC-140, DEC-141, ISS-207…209, QA-267…269) và cho các mục bị 4 finding vòng 1 chạm tới (DEC-132/ISS-194/QA-253, QA-043/ISS-051, DRAFT §4.5, DRAFT §11.2); (d) đọc lại toàn bộ yêu cầu có ID mới hoặc thay đổi (ISH-M05-002.9, ISH-M05-007/.1/.2, Phụ lục A dòng 001.5) và mọi yêu cầu liên quan để tìm hồi quy, áp lại checklist nhóm B/C/D cho phần đó. Không chạy lại toàn bộ Bước 2/4 vì SR chỉ đổi 3 yêu cầu cấp dưới mới trên tổng 40 (dưới một phần ba).
- Đã mở `disposition-M05.md` và `selfcheck-M05.md` của Author ở vòng này (hợp lệ theo quy trình vòng 2 — không phải lần dựng ma trận độc lập đầu tiên) để đối chiếu từng finding vòng 1 và kiểm các khẳng định `Đạt` của selfcheck.
- Người gọi không gửi kèm tóm tắt/nhận định nào của Author ngoài mã module, số vòng, đường dẫn gốc repo, báo cáo vòng 1.
- **Giới hạn không kiểm được:**
  - Không kiểm chứng được việc M07 (chưa có SR) sẽ thực sự tiếp nhận nội dung thông báo Follow-Topic của DEC-141 khi SR M07 được soạn — chỉ nêu đây là một khe hở routing hiện tại (AUD-M05-05).
  - Không audit M07/M14 — chỉ dùng module-registry dòng 118 (ghi chú Phase 3 về M14 "reuses Follow targets from M07") làm tham chiếu biên giới cho một OBSERVATION liên quan M05 (AUD-M05-07); không đánh giá tính đúng/sai của ghi chú đó đối với M14.
  - Không chạy ca kiểm thực tế; "viết được ca kiểm" (CL-B08) cho 3 yêu cầu mới (002.9, 007.1, 007.2) được thử bằng Given/When/Then trên giấy, không chạy hệ thống thật.
  - Không đọc lại toàn bộ 78 mục KEYWORD đã lấy mẫu ở vòng 1; ở vòng 2 chỉ đọc thêm các mục mới xuất hiện do từ khóa `follow`/`theo dõi` (DEC-020/025/104/126, ISS-059/162/164, QA-067/069/127/192/211/220/222 và các dòng M14 Feed liên quan) ở mức đủ để xác nhận phân loại "không liên quan" của `disposition-M05.md` hợp lý, không đọc chi tiết từng mục.

## 3. Kết quả kiểm tra tự động

ERROR = 0, WARN = 0, INFO = 6 (giảm từ ERROR=3 ở vòng 1 — 3 ERROR đó là COV-01 cho DEC-140/ISS-207/QA-267, nay đã hết).

- `COV-03` × 5 (INFO, không phải lỗi): DEC-049, DEC-050, DEC-051, DEC-052, QA-104 vừa ở SR vừa ở routing — không đổi so với vòng 1, đã xác nhận không trùng nội dung.
- `COV-00` (INFO): OWNED=28 (23 vòng 1 + 5 mục nguồn mới: DEC-141, ISS-208, ISS-209, QA-268, QA-269 — ghi sau khi stakeholder trả lời ISS-208/ISS-209), trong SR=25, trong routing=8.
- Không còn mã ERROR/WARN nào.

## 4. Ma trận độ phủ nguồn → yêu cầu (mục nguồn mới hoặc bị finding vòng 1 chạm tới)

| Nguồn | Mong đợi (Auditor) | Thực tế (SR / routing) | Kết quả | AUD |
|---|---|---|---|---|
| DEC-140, ISS-207, QA-267 | Phụ lục A (cột Nguồn của ISH-M05-001.5) | `ISH-SR-M05.md:265`: có trong cột Nguồn của ISH-M05-001.5, kèm Ghi chú giải thích | Khớp | (đóng AUD-M05-01) |
| DEC-132, ISS-194, QA-253 | SR: yêu cầu riêng cho nhánh AI trả Topic ngoài whitelist | `ISH-SR-M05.md:136,276`: ISH-M05-002.9 + Phụ lục A | Khớp | (đóng AUD-M05-02) |
| QA-043, DEC-141, ISS-208, QA-268 | SR: tính năng Follow Topic (M05), có nguồn rõ ràng | `ISH-SR-M05.md:222-239,297-299`: mục 5.9, ISH-M05-007/.1/.2 | Khớp | (đóng AUD-M05-03) |
| DRAFT §11.2, QA-269, ISS-209 | Routing R7 ghi nhận lệch nguồn đã xử lý chủ đích | `ISH-RT-M05.md:52`: R7 có dòng ghi rõ | Khớp | (đóng AUD-M05-04) |
| DEC-141 (phần "Notification delivery … remains M07's responsibility") | Routing R5 (hành vi module khác), kèm module M07 và nguồn DEC-141 | Không có ở R5 (R5 chỉ có 1 dòng grade_level); không có ở R7; không có ở SR | Thiếu một phần | 05 |
| DRAFT §4.5 ("Follow... Post/User/Topic/**Tag**/**Group**") vs QA-043/DEC-141 (chỉ User/Topic/Post) | Theo register (DEC-141) + ghi cả hai nguồn + dấu vết đã xử lý (RULES §7.5) | ISH-M05-007 Phụ lục A có cả DRAFT §4.5 và DEC-141/QA-268/QA-043 trong cột Nguồn; DEC-141 tự giải thích vì sao loại Tag/Group | Khớp (đủ dấu vết, không cần Ghi chú riêng vì DEC-141 đã tự giải thích) | — |
| "Theo dõi" (thuật ngữ dùng ở 5.1, 5.9, ISH-M05-007/.1/.2) | Có dòng trong bảng 2.1 Thuật ngữ | `ISH-SR-M05.md:23-33`: bảng 2.1 chỉ có Topic/Tag/Trending/Đã lỗi thời/Mod/Admin/Upvote, không có "Theo dõi" | Thiếu | 06 |
| module-registry.md:118 ("M14 Following … reuses Follow targets from M07") vs DEC-141 (M05 sở hữu Follow Topic, M07 chỉ gửi thông báo) | Không mâu thuẫn rõ ràng nhưng cần stakeholder xác nhận khi M07/M14 có SR | Không có dòng nào đối chiếu hai nguồn này | Lệch nguồn chưa xác nhận | 07 |

## 5. Phát hiện

### AUD-M05-05 — Một phần nội dung của DEC-141 (trách nhiệm thông báo của M07) không có chỗ đi trong routing

| Lớp | DEFECT | Mức | Trung bình | Checklist | CL-A10 |
|---|---|---|---|---|---|

- **Vị trí:** Routing `ISH-RT-M05.md` R5 (dòng 36-40) — thiếu một dòng.
- **Bằng chứng trong SR/routing:** `grep -n -F "DEC-141" ISH-RT-M05.md` → 0 kết quả. R5 hiện chỉ có đúng một dòng, về grade_level (`ISH-RT-M05.md:40`), không có dòng nào cho M07.
- **Bằng chứng trong nguồn:** "Notification delivery on new posts in a followed Topic remains M07's responsibility (per QA-043's own implication), M05 only owns the follow relationship and its surface on Topic." (`decisions.md:773`, DEC-141).
- **Vấn đề:** DEC-141 là một mục nguồn OWNED của M05 đã được xử lý một phần (hành vi Follow/Unfollow Topic → SR ISH-M05-007/.1/.2), nhưng câu cuối của DEC-141 xác định rõ một hành vi thuộc M07 (gửi thông báo khi Topic đang theo dõi có bài mới) — theo RULES §6.1 ("Hành vi do module khác sở hữu → R5, kèm module và ID sở hữu") và §2 quy tắc 4 (chưa có SR của M07 thì "ghi nguồn register (DEC-nnn) trong routing mục R5"), phần này phải có một dòng R5. Hiện tại không ai đọc `ISH-RT-M05.md` sẽ biết DEC-141 đã được xử lý hết, và người viết SR M07 sau này khó tìm thấy DEC-141 (nằm ở section "System Requirement — M05" của `decisions.md`, không phải section M07) nếu không có cầu nối từ routing M05.
- **Hệ quả nếu không sửa:** Khi M07 soạn SR, hành vi "gửi thông báo khi Topic theo dõi có bài mới" có nguy cơ bị bỏ sót vì nguồn duy nhất của nó (DEC-141) nằm trong section của M05 và không được routing M05 trỏ sang.
- **Hướng xử lý (Author quyết cách viết):** Thêm một dòng routing R5: Nguồn `DEC-141`, Nội dung "Gửi thông báo cho người theo dõi khi Topic đang theo dõi có bài viết mới", Module và ID sở hữu "M07 — Notification (chưa có SR, ghi nguồn DEC-141)".
- **Trạng thái (từ vòng 2):** Mở — chuyển stakeholder quyết (mục 6)

### AUD-M05-06 — Thuật ngữ "theo dõi" (Follow Topic) không có trong bảng 2.1 Thuật ngữ

| Lớp | DEFECT | Mức | Thấp | Checklist | CL-C03 |
|---|---|---|---|---|---|

- **Vị trí:** Mục 2.1 (`ISH-SR-M05.md:23-33`).
- **Bằng chứng trong SR:** "theo dõi" xuất hiện ở `ISH-SR-M05.md:81` (5.1, "Theo dõi Topic"), `:222` (tiêu đề 5.9), `:228,238,239` (ISH-M05-007, 007.1, 007.2) — 5 lần — nhưng bảng 2.1 Thuật ngữ (`ISH-SR-M05.md:25-33`) chỉ có Topic, Tag, Trending, Đã lỗi thời, Mod, Admin, Upvote, không có dòng "Theo dõi".
- **Bằng chứng trong nguồn:** Không áp dụng — đây là lỗi nội bộ của SR, không phải lệch với nguồn (RULES §3: "2.1 bảng Thuật ngữ | Mô tả cho **mọi** thuật ngữ và vai trò ... được dùng trong tài liệu — tài liệu phải tự chứa.").
- **Vấn đề:** Tính năng Follow Topic được thêm ở phiên bản 0.2 (sửa theo AUD-M05-03) nhưng thuật ngữ "theo dõi" không được bổ sung vào 2.1, trong khi các thuật ngữ khác có mức độ phổ thông tương đương (ví dụ "Upvote") vẫn có dòng riêng. **Selfcheck của Author ghi "Đạt" cho CL-C03** với lý do "'theo dõi' là từ phổ thông, không cần định nghĩa riêng" — RULES §3 không có ngoại lệ "từ phổ thông"; yêu cầu là **mọi** thuật ngữ dùng trong tài liệu.
- **Hệ quả nếu không sửa:** Tài liệu không tự chứa đầy đủ theo đúng yêu cầu cấu trúc của RULES §3; không chặn hiểu nội dung (vì "theo dõi" dễ hiểu) nhưng không khớp tiêu chuẩn SR đã áp dụng cho các thuật ngữ khác.
- **Hướng xử lý (Author quyết cách viết):** Thêm một dòng vào bảng 2.1: "Theo dõi | <định nghĩa ngắn, lấy từ DRAFT §4.5: 'muốn nhận cập nhật về nội dung hoặc chủ đề'>".
- **Trạng thái (từ vòng 2):** Mở — chuyển stakeholder quyết (mục 6)

### AUD-M05-07 — Ghi chú Phase 3 (module-registry) về M14 "reuses Follow targets from M07" chưa được đối chiếu với DEC-141 (M05 sở hữu Follow Topic)

| Lớp | OBSERVATION | Mức | Thấp | Checklist | CL-A09 |
|---|---|---|---|---|---|

- **Vị trí:** Không có vị trí trong SR/routing M05 — đây là một quan sát biên giới module, không phải lỗi của SR M05.
- **Bằng chứng trong nguồn 1:** "**Following** (chronological, reuses Follow targets from M07)" (`module-registry.md:118`, ghi chú deep-dive Phase 5 cho M14, không đánh dấu Superseded/Amended).
- **Bằng chứng trong nguồn 2:** "M05 (Topic & Tag) owns the Follow/Unfollow behaviour for Topic ... M05 only owns the follow relationship and its surface on Topic." (`decisions.md:773`, DEC-141, Phase "System Requirement — M05", muộn hơn).
- **Vấn đề:** Hai mục nguồn đều có thể đúng đồng thời (M05 sở hữu quan hệ Follow Topic; M07 là nơi M14 đọc tổng hợp các đối tượng đang được theo dõi để hiển thị tab Following) — không có bằng chứng mâu thuẫn trực tiếp, nhưng cũng không có DEC nào nói rõ hai mục này ăn khớp với nhau (RULES §7.6: chỉ được xem là không mâu thuẫn khi có xác nhận, còn lại nên hỏi). Vì M07 và M14 chưa có SR, đây chưa chặn bàn giao SR M05, chỉ là một điểm cần đối chiếu khi SR M07 hoặc M14 được soạn.
- **Hệ quả nếu không sửa:** Người viết SR M07/M14 có thể giả định sai về nơi lưu trữ/sở hữu quan hệ Follow Topic.
- **Hướng xử lý (Author quyết cách viết):** Không cần sửa SR M05; đề xuất ghi một ghi chú ngắn (ví dụ ở `disposition-M05.md` hoặc để lại cho Author của M07/M14) dẫn chiếu DEC-141 khi soạn SR M07/M14.
- **Trạng thái (từ vòng 2):** Mở — chuyển stakeholder quyết (mục 6)

## 6. Cần stakeholder quyết

```
Vấn đề: DEC-141 có một phần nội dung (M07 chịu trách nhiệm gửi thông báo khi Topic đang theo dõi có bài mới) chưa có dòng routing nào ghi nhận, trong khi SR M05 đã dùng xong phần "M05 sở hữu Follow Topic" của cùng DEC-141.
Nguồn: DEC-141 (decisions.md:773): "Notification delivery on new posts in a followed Topic remains M07's responsibility..."
Lựa chọn: A) Thêm một dòng routing R5 (Nguồn DEC-141, Module/ID sở hữu "M07, chưa có SR") — hệ quả: chỉ sửa file routing, không đổi SR, không cần vòng audit mới cho M05.
          B) Không cần ghi vì M07 chưa có SR nên chưa có gì để trỏ tới — hệ quả: rủi ro M07 bỏ sót DEC-141 khi soạn SR (nguồn nằm trong section "M05" của decisions.md, không nằm trong section M07).
Đề xuất: A, vì RULES §2 quy tắc 4 cho phép ghi nguồn register (không cần ID) ở R5 khi module đích chưa có SR, đúng là cơ chế dành cho tình huống này.
Liên quan: AUD-M05-05
```

```
Vấn đề: Thuật ngữ "theo dõi" (Follow Topic, thêm ở v0.2) không có trong bảng 2.1 Thuật ngữ, dù tài liệu đã đặt tiêu chuẩn định nghĩa cả các thuật ngữ phổ thông tương đương (Upvote). Author tự chấm CL-C03 "Đạt" với lý do khác tiêu chuẩn RULES §3.
Nguồn: ISH-SR-M05.md (dòng 81, 222, 228, 238, 239 dùng "theo dõi"; dòng 23-33 là toàn bộ bảng 2.1, không có "Theo dõi").
Lựa chọn: A) Thêm một dòng 2.1 định nghĩa "Theo dõi" — hệ quả: SR tự chứa đầy đủ, khớp RULES §3, sửa nhanh.
          B) Xác nhận ngoại lệ "từ phổ thông không cần định nghĩa" cho các lần sau — hệ quả: cần sửa RULES §3 để ghi rõ ngoại lệ này, áp dụng nhất quán cho mọi module sau, không chỉ M05.
Đề xuất: A, vì sửa tại chỗ đơn giản hơn và không làm thay đổi tiêu chuẩn chung đang áp dụng cho các SR khác.
Liên quan: AUD-M05-06
```

```
Vấn đề: Ghi chú Phase 3 ở module-registry ("M14 Following tab reuses Follow targets from M07") chưa được đối chiếu với DEC-141 (Phase SR, mới hơn: M05 sở hữu Follow Topic, M07 chỉ gửi thông báo) — không rõ có mâu thuẫn hay không khi M07/M14 được soạn SR.
Nguồn: module-registry.md:118; decisions.md:773 (DEC-141).
Lựa chọn: A) Xác nhận không mâu thuẫn (M07 là nơi M14 đọc dữ liệu tổng hợp qua lớp thông báo, M05 vẫn là nơi lưu quan hệ Follow Topic) — không cần hành động gì ở SR M05.
          B) Yêu cầu một DEC mới làm rõ ba module M05/M07/M14 trước khi viết SR của M07 hoặc M14.
Đề xuất: A, vì không có bằng chứng mâu thuẫn trực tiếp, chỉ là một điểm cần lưu ý cho module khác, không chặn M05.
Liên quan: AUD-M05-07
```

## 7. Kết quả checklist

| Mã | Kết quả | AUD / ghi chú |
|---|---|---|
| CL-A01 | Đạt | DRAFT §4.5 (Follow/Quan tâm) nay đã map vào ISH-M05-007 (v0.2); các mục khác không đổi so với vòng 1 |
| CL-A02 | Đạt | **Đã sửa (AUD-M05-01).** `check_sr` COV-01 = 0; DEC-140/ISS-207/QA-267 có mặt ở Phụ lục A (001.5) |
| CL-A03 | Đạt | **Đã sửa (AUD-M05-02/03).** `disposition-M05.md` đã cập nhật: DEC-132/ISS-194/QA-253 và QA-043/ISS-051 chuyển từ "không liên quan"/thiếu dòng sang "SR", lý do hợp lý |
| CL-A04 | Đạt | `check_sr` COV-02 = 0 |
| CL-A05 | Đạt | Đối chiếu nguyên văn DEC-132, DEC-141 với ISH-M05-002.9 và ISH-M05-007/.1/.2 — khớp nghĩa |
| CL-A06 | Đạt | Không có yêu cầu "Suy ra" mới ở v0.2 (002.9 và 007.x đều "Nói thẳng") |
| CL-A07 | Đạt | Không có số liệu mới; "11 Topic" ở 002.9 dùng lại danh sách đã có nguồn (DEC-048) |
| CL-A08 | Đạt | DRAFT §4.5 (Follow Post/User/Topic/Tag/Group) vs QA-043/DEC-141 (chỉ User/Topic/Post) — SR theo register, ghi cả hai nguồn ở Phụ lục A (007), DEC-141 tự giải thích lý do loại Tag/Group — đủ ba điều kiện RULES §7.5 |
| CL-A09 | Đạt | QA-033/ISS-046 → routing R6 "bị thay bởi DEC-140" (không đổi so với vòng 1) |
| CL-A10 | **Không đạt** | AUD-M05-05: phần M07 của DEC-141 không có chỗ đi ở routing |
| CL-B01 | Đạt | `check_sr` EARS-01…03 = 0; 002.9 dùng đúng mẫu "Nếu…, thì…" cho lỗi AI (không do hành động hợp lệ của người dùng) |
| CL-B02 | Đạt | `check_sr` RULE-01/02/08 = 0 |
| CL-B03 | Đạt | `check_sr` RULE-04 = 0 |
| CL-B04 | Đạt | `check_sr` RULE-03 = 0 |
| CL-B05 | Đạt | `check_sr` RULE-05 = 0 |
| CL-B06 | Đạt | `check_sr` RULE-06/07 = 0 |
| CL-B07 | Đạt | `check_sr` RULE-09 = 0 |
| CL-B08 | Đạt | Thử viết ca kiểm Given/When/Then cho 002.9, 007, 007.1, 007.2 — viết được cả 4 |
| CL-B09 | Đạt | **Đã sửa (AUD-M05-02).** ISH-M05-002.9 thêm nhánh AI trả Topic ngoài whitelist |
| CL-B10 | Đạt | 007.1 (bỏ theo dõi) và 007.2 (hiển thị số lượng) là hai hành vi tách biệt, không gộp |
| CL-B11 | Đạt | Follow (007) không có phân quyền đặc biệt — đúng nguồn (mọi User), không cần yêu cầu phân quyền riêng |
| CL-C01 | Đạt | Đọc lại 40 yêu cầu theo đối tượng (thêm Follow Topic) — không có cặp mâu thuẫn |
| CL-C02 | Đạt | Không có cấp dưới chỉ lặp lại cấp trên (007.1/007.2 là hành vi riêng) |
| CL-C03 | **Không đạt** | AUD-M05-06: "theo dõi" dùng 5 lần, không có trong 2.1. **Selfcheck ghi "Đạt"** với lý do không có trong RULES |
| CL-C04 | Đạt | "Lý do" của ISH-M05-007 khớp lời văn DRAFT §4.5 ("muốn nhận cập nhật về nội dung hoặc chủ đề") |
| CL-C05 | Đạt | 5.1 có đủ 7 dòng khớp 5.3-5.9; "Theo dõi Topic" gắn Must/P1 khớp `iShare_dev_priority.md` Giai đoạn 2 (Interaction: "Follow...") |
| CL-D01 | Đạt | `check_sr` HDR-01…08 = 0 |
| CL-D02 | Đạt | `check_sr` STR-01…09 = 0; số thứ tự 5.1-5.11 liên tục sau khi chèn 5.9 mới, HMI/Chuyển màn hình vẫn là hai mục cuối (5.10, 5.11) |
| CL-D03 | Đạt | `check_sr` REQ-00…04 = 0; tính năng 5.9 có đúng 1 cấp trên + 2 cấp dưới + Lý do |
| CL-D04 | Đạt | `check_sr` ID-01…06 = 0; ID cũ (001-006.x) không đổi nghĩa; ID mới (002.9, 007, 007.1, 007.2) lấy số tiếp theo chưa dùng |
| CL-D05 | Đạt | `check_sr` TRC-01…10 = 0; đếm tay 40/40 ID có dòng Phụ lục A |
| CL-D06 | Đạt | `check_sr` REF-01/02 = 0 |
| CL-E01 | Đạt | Không có tên bảng/trường/công nghệ/HMI trong các yêu cầu mới |
| CL-E02 | Đạt | SR không viết hành vi gửi thông báo (thuộc M07) — Follow Topic chỉ viết phần M05 sở hữu (nút, trạng thái, số lượng) |
| CL-E03 | **Không đạt** | Cùng nguyên nhân AUD-M05-05: R5 thiếu dòng cho phần M07 của DEC-141 |
| CL-E04 | Đạt | Không đổi — mục 4.1 vẫn "Không có." |
| CL-F01 | Đạt | `check_sr` OPN-01…03 = 0; Phụ lục B vẫn 6 OP (không đổi), không có OP nào cần đóng |
| CL-F02 | Đạt | `check_sr` REV-01…03 = 0; dòng cuối lịch sử (0.2) khớp header; mô tả đúng 4 thay đổi thực tế |
| CL-F03 | Đạt | **Đã sửa (AUD-M05-01).** ISS-207/QA-267/DEC-140 và ISS-208/QA-268/DEC-141, ISS-209/QA-269 đều có ID register khớp SR/routing |
| CL-F04 | Đạt | **Đã sửa (AUD-M05-03).** Follow Topic/Tag đã được raise và trả lời (QA-268/DEC-141), không còn là quyết định ngầm |
| CL-F05 | Đạt | Không đổi — mục 1-4 không sửa ở v0.2 |
| CL-F06 | Đạt | Không đổi |

## 8. Vòng trước

| AUD vòng 1 | Trạng thái vòng 2 | Bằng chứng |
|---|---|---|
| AUD-M05-01 (DEFECT Cao, CL-A02) | Đã sửa | DEC-140/ISS-207/QA-267 có trong cột Nguồn của Phụ lục A (`ISH-SR-M05.md:265`); `check_sr` COV-01 = 0 |
| AUD-M05-02 (DEFECT Trung bình, CL-B09) | Đã sửa | Thêm ISH-M05-002.9 (`ISH-SR-M05.md:136`), nguồn DEC-132/ISS-194/QA-253 (`ISH-SR-M05.md:276`) |
| AUD-M05-03 (GAP, CL-A03) | Đã sửa | Stakeholder trả lời qua DEC-141/QA-268 (ISS-208); SR thêm mục 5.9 (ISH-M05-007/.1/.2, `ISH-SR-M05.md:222-239`); `disposition-M05.md:43` ghi nhận chuyển sang SR |
| AUD-M05-04 (DEFECT Thấp, CL-A08) | Đã sửa | Routing R7 thêm dòng (`ISH-RT-M05.md:52`) ghi nhận DRAFT §11.2 vs DEC-050/051, xác nhận chủ đích qua QA-269 (ISS-209) |

Hồi quy mới: AUD-M05-05 (DEFECT Trung bình, CL-A10) và AUD-M05-06 (DEFECT Thấp, CL-C03) — cả hai phát sinh trực tiếp từ nội dung được thêm để sửa AUD-M05-03 (tính năng Follow Topic và nguồn DEC-141). AUD-M05-07 (OBSERVATION Thấp) không phải hồi quy của SR M05 mà là một điểm biên giới module phát sinh khi đối chiếu DEC-141 với module-registry.

## 9. Hồ sơ xác minh

- `grep -n -F "DEC-140, ISS-207, QA-267" ISH-SR-M05.md` → 1 kết quả (dòng 265, Phụ lục A của ISH-M05-001.5).
- `grep -n -F "DEC-141" ISH-RT-M05.md` → 0 kết quả (xác nhận AUD-M05-05).
- `grep -n -i -F "theo dõi" ISH-SR-M05.md` → 6 kết quả (dòng 81, 222, 228, 238, 239, 254); dòng 254 là Lịch sử sửa đổi (không tính là "dùng thuật ngữ trong yêu cầu"), 5 dòng còn lại là dùng thật trong nội dung — đối chiếu bảng 2.1 (dòng 23-33): không có "Theo dõi".
- `grep -n "reuses Follow targets" module-registry.md` → 1 kết quả (dòng 118) — dùng cho AUD-M05-07.
- `python3 check_sr.py ... --inventory audit-inventory-M05-r2.json` → ERROR=0, WARN=0, INFO=6 (file `WORK/check-M05-r2.json`).
- Không có finding nào bị loại ở Bước 6 trong vòng này — cả 3 finding mới (05, 06, 07) đều xác minh được bằng grep như trên.
- Mục đã xem xét nhưng **không** lập finding: lệch nguồn DRAFT §4.5 (Follow Post/User/Topic/Tag/Group) vs QA-043/DEC-141 (chỉ User/Topic/Post) — đủ ba điều kiện RULES §7.5 (theo register, ghi cả hai nguồn, có dấu vết xử lý qua DEC-141) nên không phải DEFECT, dù không có Ghi chú riêng ở Phụ lục A như cách làm ở 004.1; nội dung "cho phép chọn thủ công" của DEC-132 không có yêu cầu riêng ở 002.9 nhưng đã được bao phủ bởi năng lực chung ISH-M05-001 (gán Topic thủ công) — không lập finding vì không đổi nghĩa kiểm chứng được.
