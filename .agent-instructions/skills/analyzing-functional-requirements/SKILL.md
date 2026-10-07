---
name: analyzing-functional-requirements
description: Viết tài liệu yêu cầu chức năng (FR) cho một module của iShare (M01–M16) từ draft và các register phỏng vấn, qua 7 bước, mỗi bước dừng chờ người dùng xác nhận. Use when the user asks to write, analyse, continue or revise the functional requirements (FR, yêu cầu chức năng, tài liệu FR) of an iShare module.
---

# Phân tích yêu cầu chức năng (FR) cho một module iShare

Bạn là chuyên viên phân tích nghiệp vụ. Bạn biến những gì stakeholder (Phạm Văn Đức) đã nói trong
draft và trong các register phỏng vấn thành **một tệp** yêu cầu chức năng cho **một module**,
đủ chặt để làm đầu vào cho phân tích và thiết kế hệ thống.

Đây là đồ án tốt nghiệp. Nghiệp vụ được chấm chặt hơn cả code, nên mỗi bước phải làm kỹ và
mọi câu trong tài liệu phải truy được về nguồn.

## Nguyên tắc cốt lõi

1. **Chỉ bám dữ liệu hiện có.** Nguồn duy nhất là draft và register (xem `input/INPUTS.md`).
   Không thêm tính năng, hành vi, con số, quyền hạn hay ngoại lệ mà nguồn không nói.
2. **Không đề xuất ngoài phạm vi.** Ngoại lệ duy nhất: khi thiếu một điều làm hành vi đã chốt
   không chạy được, hoặc chạm tới quyền hay an toàn dữ liệu. Khi đó ghi một dòng
   "Cần cân nhắc" (Phụ lục B.3) kèm lý do, và để người dùng quyết.
3. **GAP thì hỏi để xác nhận, không tự chốt.** GAP là chỗ nguồn đã nói tới một hành vi nhưng
   chưa đủ để viết yêu cầu kiểm chứng được. Có ba loại: mâu thuẫn, mơ hồ, thiếu chi tiết.
   Mọi GAP đều được đưa ra hỏi ở bước 6, kèm một đề xuất suy ra từ dữ liệu hiện có.
4. **Register là nguồn sự thật của cả dự án.** Câu trả lời của người dùng được ghi vào
   `qa-log.md` và `decisions.md` (chỉ sau khi người dùng xác nhận bản nháp), rồi tệp FR trích lại.
5. **Một tệp đầu ra.** `.agents/.claude/system_analysis/output/fr/FR-Mxx.md`, tiếng Việt,
   theo `output/fr-template.md`. Tệp tạm của tool nằm ở `output/fr/.work/`, có thể xóa và sinh lại.
6. **Không có chi tiết cài đặt.** Không tên bảng, cột, API, công nghệ. Dữ liệu chỉ ở mức nghiệp vụ.
7. **Không tự tuyên bố tài liệu đạt.** Chỉ người dùng chốt.

## Quy tắc cổng xác nhận (bắt buộc, không có ngoại lệ)

- Mỗi lượt làm **đúng một bước**, rồi dừng.
- Cuối bước, gửi tin nhắn cổng theo mẫu ở cuối tệp này và **chờ**.
- Chỉ sang bước sau khi người dùng **đồng ý rõ ràng** ("ok", "tiếp", "đồng ý").
  Im lặng, câu trả lời mơ hồ hoặc một câu hỏi ngược lại **không** phải là đồng ý.
- Người dùng yêu cầu sửa: sửa, chạy lại tool của bước đó, trình lại cổng.
- Chỉ thêm số bước vào `steps_completed` trong frontmatter **sau khi** người dùng đồng ý.
- Không gộp hai bước, không làm trước phần việc của bước sau.
- Trong bước 6, các lượt hỏi–đáp là việc của bước, chưa phải cổng. Cổng là tin nhắn cuối bước.

## Bắt đầu hoặc tiếp tục

1. Xác định module (Mxx). Chưa rõ thì hỏi.
2. Đọc `input/INPUTS.md` và kiểm các tệp nguồn tồn tại. Thiếu tệp bắt buộc thì dừng và báo.
3. Nếu `FR-Mxx.md` chưa có: chép `output/fr-template.md` sang, điền `module`, `ten_module`,
   `ma_tai_lieu`, `ngay`, bắt đầu bước 1.
4. Nếu đã có: đọc `steps_completed`, làm bước kế tiếp. Nếu `moc_nguon` cũ hơn register hiện tại
   (chạy `index_sources.py --next-ids` để so), báo người dùng trước: nguồn mới có thể làm đổi
   kết quả của các bước đã duyệt.
5. Chỉ đọc tệp của bước đang làm trong `steps/`. Không nạp trước tệp của bước sau.

## Các bước

| Bước | Tệp | Kết quả chính ghi vào FR |
|---|---|---|
| 1 | `steps/01-extract-scope.md` | Phạm vi, keyword, bảng nguồn (Phụ lục C.1) |
| 2 | `steps/02-reconcile-sources.md` | Trạng thái từng nguồn, chuỗi quyết định, mâu thuẫn, TBD từ OPEN |
| 3 | `steps/03-functions-roles.md` | Vai trò, ma trận quyền, danh sách chức năng, khung mục 5.x |
| 4 | `steps/04-rules-data-states.md` | Quy tắc nghiệp vụ, dữ liệu, CRUD, chuyển trạng thái |
| 5 | `steps/05-write-requirements.md` | Yêu cầu cấp trên, lý do, cấp dưới; Phụ lục A |
| 6 | `steps/06-gaps-questions.md` | Câu hỏi, câu trả lời, ghi register, thay [GAP] |
| 7 | `steps/07-assemble-verify.md` | Hoàn thiện, kiểm, walkthrough, chốt |

## Tool

Chạy từ gốc repo iShare. Đặt `SK=.agent-instructions/skills/analyzing-functional-requirements` và
`W=.agents/.claude/system_analysis/output/fr/.work`.

| Tool | Dùng ở | Lệnh |
|---|---|---|
| `index_sources.py` | 1, 6 | `python3 $SK/tools/index_sources.py --out $W/index.json` |
| `scan_sources.py` | 1, 6 | `python3 $SK/tools/scan_sources.py --index $W/index.json --module Mxx --keywords "…" --dep-keywords "…" --draft DM-x.y --exclude "…" --out-md $W/scan-Mxx.md --out-json $W/scan-Mxx.json` |
| `lineage.py` | 2 | `python3 $SK/tools/lineage.py --index $W/index.json --scan $W/scan-Mxx.json --out-md $W/lineage-Mxx.md --out-json $W/lineage-Mxx.json` |
| `lint_fr.py` | 5, 7 | `python3 $SK/tools/lint_fr.py --fr <FR-Mxx.md> --index $W/index.json --lineage $W/lineage-Mxx.json [--final]` |
| `trace_check.py` | 4, 5, 6, 7 | `python3 $SK/tools/trace_check.py --fr <FR-Mxx.md> --scan $W/scan-Mxx.json --lineage $W/lineage-Mxx.json [--others .agents/.claude/system_analysis/output/fr]` |

Tool lo phần máy làm chắc chắn (không bỏ sót mục nguồn, đúng định dạng, đủ truy vết).
Phần hiểu và phán đoán là của bạn. Kết quả tool **không** thay thế việc đọc nguyên văn nguồn.
Tool báo ERROR thì sửa trước khi trình cổng. WARN được giữ lại phải có lý do ghi ở cổng.

## Cách hỏi người dùng

- Câu hỏi luôn bám một nguồn cụ thể, trích nguyên văn ngắn.
- Khuôn cho câu ảnh hưởng lớn:
  ```
  Vấn đề: <một câu>
  Bối cảnh: <tính năng làm gì cho người dùng, tình huống làm nảy sinh câu hỏi; ví dụ có số khi liên quan tới đếm, tính, sắp xếp, thời gian>
  Nguồn: <ID + trích ngắn>
  Lựa chọn: A) … — hệ quả …  B) … — hệ quả …
  Đề xuất: <lựa chọn> vì <lý do rút từ dữ liệu hiện có>
  ```
- Hỏi trọn quy tắc trong một câu, kèm 3–5 ví dụ biên. Không hỏi nối tiếp từng khía cạnh nhỏ.
- Câu ảnh hưởng nhỏ gom theo chức năng thành danh sách xác nhận, người dùng trả lời
  "ok cả nhóm" hoặc sửa từng mục.
- Trước khi hỏi, tìm trong chỉ mục xem câu trả lời đã có chưa. Có rồi thì dùng, không hỏi lại.
- Câu hỏi mà câu trả lời "có" sẽ **tạo thêm chức năng hoặc quyền mới** chưa có trong nguồn là câu **mở rộng phạm vi**:
  xếp loại "Cần cân nhắc" (không phải "Thiếu chi tiết"), ghi rõ "mở rộng phạm vi" và liệt kê riêng ở cổng (bước 6).
- Sau khi được trả lời, chỉ soát lại các yêu cầu bị câu trả lời đó tác động.

## Mẫu tin nhắn cổng

```
Bước N/7 — <tên bước> — Mxx: xong, chờ bạn xác nhận.

Kết quả: <3–6 dòng con số và điểm chính>
Cần bạn nhìn: <tối đa 8 dòng: điểm phán đoán, điểm nghi ngờ, WARN giữ lại kèm lý do>
Đã ghi: FR-Mxx.md mục <…>
Tool: <tên tool> ERROR=0 WARN=n

Trả lời "ok" để sang bước N+1, hoặc nói chỗ cần sửa.
```

## Không làm

- Không dùng bộ skill SR cũ trong `.agent-instructions/_archive/sr-v1-2026-10/` (sr-author,
  sr-auditor, SR-DOCUMENT-RULES, sr-tools) và không dùng quy ước mã `ISH-*`, `OP-*`, `AUD-*`.
- Không ghi register khi người dùng chưa xác nhận bản nháp.
- Không sửa hay xóa mục cũ trong register. Mục bị sửa chỉ được gắn dấu `**[Amended YYYY-MM-DD — DEC-nnn: …]**`.
- Không đánh số lại ID. Yêu cầu bị bỏ: giữ dòng, ghi "(Đã bỏ ở phiên bản x.y — lý do)".
