# SR-DOCUMENT-RULES — Quy tắc tài liệu System Requirement (SR) của iShare

> [Vietnamese Doc] — Theo COMMON-RULES Rule 1: tài liệu này viết bằng tiếng Việt theo yêu cầu của stakeholder (DEC-139 / QA-265).
> Đây là **nguồn quy tắc duy nhất** cho định dạng, ID, cách viết yêu cầu và quy trình của SR. Skill Author và skill Auditor chỉ mô tả *quy trình*, không lặp lại quy tắc; nếu mâu thuẫn, tài liệu này thắng.

---

## 0. Phạm vi và thẩm quyền

- SR là tài liệu **yêu cầu chức năng theo từng module**, viết từ dữ liệu đã chốt trong `registers/` và DRAFT. Mỗi module một tài liệu `ISH-SR-Mxx`.
- SR **không** chứa: mô hình dữ liệu/bảng/trường (→ Phase 8), yêu cầu phi chức năng (→ Phase 7), giải pháp công nghệ, thiết kế giao diện (→ HMI sau khi có design).
- Quy tắc này **khác có chủ đích** hai quy tắc trong `BA-INTERVIEW-RULES.md` (output chỉ tiếng Anh; không sinh spec trước Phase 9) — xem DEC-139. Mọi quy tắc khác của BA (không bịa yêu cầu, truy vết, mỗi lần một vấn đề, ghi register) vẫn áp dụng.
- Nguồn sự thật duy nhất: DRAFT (`docs/_temp/iShare_*.md`, trích dẫn `DRAFT §x.y`) và các mục đã chốt trong registers (`ISS-nnn`, `QA-nnn`, `DEC-nnn`, `OPEN-nnn`). Không có nguồn thì không có yêu cầu.

## 1. Tệp và vị trí

Thư mục gốc: `.agents/.claude/system_analysis/output/specs/`

| Tệp | Đường dẫn | Ai viết | Ghi chú |
|---|---|---|---|
| SR module | `specs/ISH-SR-Mxx.md` | Author | Thân tài liệu sạch, không có nhãn nguồn |
| Routing module | `specs/routing/ISH-RT-Mxx.md` | Author | Mọi mục nguồn không thành yêu cầu chức năng |
| Báo cáo audit | `specs/audit/ISH-AUD-Mxx-r<n>.md` | Auditor | Auditor chỉ ghi file này |
| Tồn kho nguồn (làm việc) | `specs/audit/work/inventory-Mxx.md/.json` | Script | Có thể tạo lại bất cứ lúc nào |

Tên module trong tiêu đề: `Mxx — <tên module theo module-registry>`. Số module M01–M16 theo `module-registry.md`.

## 2. Quy ước ID (đã chốt)

Tiền tố dự án: `ISH` (iShare). Số module hai chữ số `Mxx`. Số thứ tự ba chữ số.

| Đối tượng | Dạng | Ví dụ | Quy tắc |
|---|---|---|---|
| Mã tài liệu SR | `ISH-SR-Mxx` | `ISH-SR-M05` | Một SR mỗi module |
| Mã tài liệu routing | `ISH-RT-Mxx` | `ISH-RT-M05` | Đi kèm SR |
| Yêu cầu cấp trên | `ISH-Mxx-nnn` | `ISH-M05-004` | nnn tăng dần theo module (001, 002, …) |
| Yêu cầu cấp dưới | `ISH-Mxx-nnn.k` | `ISH-M05-004.1` | k tăng dần trong từng cấp trên |
| Điểm cần làm rõ | `OP-Mxx-nn` | `OP-M05-01` | **Tạm thời**, chỉ ở Phụ lục B; xóa khi đã trả lời |
| Phát hiện audit | `AUD-Mxx-nn` | `AUD-M05-03` | Do Auditor đặt, trong báo cáo audit |
| Mục nguồn | `ISS-nnn`, `QA-nnn`, `DEC-nnn`, `OPEN-nnn` | `DEC-051` | Dùng nguyên ID có sẵn trong registers |

Quy tắc ID:

1. ID **vĩnh viễn**: không đánh số lại, không dùng lại, cho phép có khoảng trống. Yêu cầu bị bỏ → ghi vào Lịch sử sửa đổi ("ISH-M05-007 bị bỏ vì …"), ID đó không bao giờ dùng lại.
2. Yêu cầu mới trong lần sửa lấy số kế tiếp chưa dùng, kể cả khi chèn vào giữa một tính năng.
3. Số mục `5.x` là số trình bày, **không phải ID**; mọi tham chiếu dùng ID yêu cầu.
4. Tham chiếu chéo module dùng ID yêu cầu của module sở hữu (`ISH-M03-007`). Chưa có SR của module đó thì ghi tham chiếu dạng ID dự kiến **không được phép** — thay bằng điểm mở `OP-Mxx-nn` hoặc ghi nguồn register (`DEC-nnn`) trong routing mục R5.

## 3. Cấu trúc tài liệu SR

Cấu trúc bám tài liệu mẫu của stakeholder (mục 1–6), thêm hai phụ lục. Tiêu đề và thứ tự **cố định** (script `check_sr.py` kiểm tra).

```
# Tài liệu yêu cầu hệ thống — Mxx <tên module>
<!-- [Vietnamese Doc] -->
| Mã tài liệu | ISH-SR-Mxx |
| Dự án | iShare |
| Module | Mxx — <tên> |
| Trạng thái | Bản nháp | Đã audit | Đã chốt |
| Phiên bản | 0.1 |
| Ngày | YYYY-MM-DD |
| Tác giả | Phạm Văn Đức |

## 1. Tổng quan
### 1.1 Mục đích
## 2. Thuật ngữ và viết tắt
### 2.1 Thuật ngữ
### 2.2 Viết tắt
## 3. Thông tin đầu vào
### 3.1 Tài liệu đầu vào
### 3.2 Tài liệu liên quan
## 4. Tổng quan chức năng
### 4.1 Luật và tiêu chuẩn liên quan
## 5. Yêu cầu chức năng
### 5.1 Tổng quan yêu cầu
### 5.2 Chuyển trạng thái
### 5.3 … 5.k  <Tên tính năng>        (mỗi tính năng một mục)
### 5.k+1 Yêu cầu HMI
### 5.k+2 Chuyển màn hình
## 6. Lịch sử sửa đổi
## Phụ lục A. Truy vết nguồn
## Phụ lục B. Điểm cần làm rõ (tạm thời)
```

Header: **không** có người duyệt/thẩm định/phê duyệt. Tác giả luôn là `Phạm Văn Đức`.

| Mục | Nội dung bắt buộc | Không được chứa |
|---|---|---|
| 1 Tổng quan | Một đoạn nêu tài liệu quy định điều gì cho module nào. 1.1 Mục đích: một–hai câu nêu mục đích của module với người dùng (từ DRAFT) | Yêu cầu, số liệu |
| 2 Thuật ngữ | 2.1 bảng `Thuật ngữ \| Mô tả` cho **mọi** thuật ngữ và **vai trò** (Guest, User, Mod, Admin…) được dùng trong tài liệu — tài liệu phải tự chứa. 2.2 bảng `Viết tắt \| Đầy đủ`. Định nghĩa lấy theo lời văn của nguồn | Quy tắc hành vi (chuyển thành yêu cầu), thuật ngữ không dùng |
| 3 Thông tin đầu vào | 3.1 các tài liệu nguồn đã dùng: tên tệp + mục (DRAFT) và các register (kèm ngày đọc). 3.2 SR của module khác được tham chiếu; không có thì ghi `Không có` | — |
| 4 Tổng quan chức năng | Mô tả ngắn module làm gì, 1–3 đoạn, không có "phải". 4.1: chỉ ghi luật/tiêu chuẩn mà **stakeholder đã nêu**; nếu không có ghi đúng `Không có.` | Thông tin quyền riêng tư/pháp lý do Author tự thêm (xem OPEN-008) |
| 5.1 Tổng quan yêu cầu | Bảng `Tính năng \| Yêu cầu cấp trên \| Mức ưu tiên (MoSCoW) \| Mốc \| Ngoại lệ`. Ưu tiên/mốc ghi **một lần** ở đây; cột Ngoại lệ liệt kê ID cấp dưới có mức/mốc khác module | Nhãn ưu tiên rải trong từng yêu cầu |
| 5.2 Chuyển trạng thái | Nếu module có trạng thái: bảng `Trạng thái hiện tại \| Sự kiện hoặc điều kiện \| Trạng thái mới \| ID yêu cầu`. Nếu không: `Không áp dụng.` | — |
| 5.3 … 5.k | Mỗi tính năng đúng ba phần, theo đúng thứ tự dưới đây | — |
| HMI, Chuyển màn hình | Giữ chỗ: `Sẽ bổ sung sau khi có thiết kế.` | Mô tả giao diện |
| 6 Lịch sử | Bảng `Phiên bản \| Ngày \| Mô tả \| Người sửa`; dòng cuối trùng phiên bản header | — |
| Phụ lục A | Bảng `ID \| Nguồn \| Cơ sở \| Ghi chú` — **mọi** ID yêu cầu (cấp trên và cấp dưới) đúng một dòng | — |
| Phụ lục B | Bảng `ID \| Nội dung \| Loại \| Trạng thái` với `OP-Mxx-nn`, hoặc `Không có.` Bản `Đã chốt` bắt buộc `Không có.` | — |

### 3.1 Mẫu một tính năng (5.3 … 5.k)

```
### 5.3 <Tên tính năng>

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M05-001 | Hệ thống phải … |

**Lý do**

<Một–ba câu, lấy từ lời văn của nguồn; nguồn không nêu thì ghi "Nguồn chưa nêu lý do." và đưa vào Phụ lục B loại Đề xuất.>

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M05-001.1 | Khi …, hệ thống phải … |
```

Mỗi tính năng có **đúng một** yêu cầu cấp trên và **ít nhất một** yêu cầu cấp dưới. Cần hai yêu cầu cấp trên thì tách thành hai tính năng.

### 3.2 Phụ lục A — cột

- **Nguồn**: một hoặc nhiều mục, phân tách bằng dấu phẩy: `DEC-051`, `QA-105`, `ISS-082`, `DRAFT §3.2`.
- **Cơ sở**: đúng một trong hai giá trị
  - `Nói thẳng` — nguồn nêu rõ hành vi/giá trị này.
  - `Suy ra` — hệ quả logic bắt buộc của nguồn (ví dụ: nguồn nói "tối đa 3" ⇒ hành vi từ chối khi chọn thứ 4). **Bắt buộc** có Ghi chú nêu phép suy luận. `Suy ra` không được tạo quyết định mới (số liệu, ngoại lệ, quyền hạn): nếu có thì đó là GAP, phải hỏi stakeholder.
- Mục nguồn nào chỉ đưa một phần vào SR thì phần còn lại phải nằm trong routing.

## 4. Quy tắc viết yêu cầu

### 4.1 Mẫu câu (EARS bằng tiếng Việt)

Chủ ngữ của "phải" **luôn là "hệ thống"**. Người dùng/vai trò chỉ xuất hiện trong vế điều kiện.

| Loại | Mẫu | Dùng khi |
|---|---|---|
| Phổ quát | `Hệ thống phải <hành vi>.` | Luôn đúng, không điều kiện |
| Theo trạng thái | `Trong khi <trạng thái kéo dài>, hệ thống phải <hành vi>.` | Hành vi gắn với một trạng thái |
| Theo sự kiện | `Khi <sự kiện>, hệ thống phải <hành vi>.` | Có tác nhân kích hoạt tức thời |
| Tính năng tùy chọn | `Đối với <tính năng/cấu hình>, hệ thống phải <hành vi>.` | Chỉ áp dụng khi tính năng/cấu hình có mặt |
| Bất thường | `Nếu <điều kiện bất thường>, thì hệ thống phải <hành vi>.` | Lỗi, từ chối, ngoại lệ |
| Phức hợp | `Trong khi <A>, khi <B>, hệ thống phải <C>.` | Kết hợp tối đa hai điều kiện |

Ví dụ đúng: `Khi người dùng chọn chủ đề thứ 4 cho một bài viết, hệ thống phải từ chối lựa chọn đó.`
Ví dụ sai: `Người dùng không được chọn quá nhiều chủ đề.` (chủ ngữ sai, "nhiều" mơ hồ).

### 4.2 Quy tắc nội dung (INCOSE rút gọn)

1. **Một ý một yêu cầu.** Một câu, một hành vi kiểm chứng được. Không "và/hoặc". Không trộn "và" với "hoặc" trong một câu. Tách khi có hơn một "phải" hoặc dài hơn ~60 từ.
2. **Đo được.** Giá trị cụ thể kèm đơn vị lấy từ nguồn (5 thẻ, 30 ký tự, 7 ngày). Cấm từ mơ hồ: nhanh chóng, dễ dàng, thân thiện, phù hợp, thích hợp, hợp lý, đầy đủ, khoảng, một số, nhiều, linh hoạt, tối ưu, thông thường, tương tự, v.v., vân vân.
3. **Không cụm thoát.** Cấm: nếu có thể, nếu cần, khi cần thiết, nếu phù hợp, tùy trường hợp, bao gồm nhưng không giới hạn.
4. **Không đại từ thay thế.** Cấm "nó", "chúng", "họ"; nhắc lại danh từ. Hạn chế "này/đó/kia".
5. **Không nêu giải pháp.** Không tên bảng/trường/cột (kể cả dạng `snake_case`), API, thư viện, công nghệ (PostgreSQL, Redis, SSE, JWT…), cơ chế cài đặt (cache, queue, cron, index). Mô tả *hành vi quan sát được*. Giá trị cấu hình của stakeholder (ví dụ khung 7 ngày) được giữ ở dạng số liệu nghiệp vụ.
6. **Thuật ngữ nhất quán.** Mỗi khái niệm một tên, trùng 2.1; viết hoa vai trò nhất quán (Guest, User, Mod, Admin).
7. **Không placeholder.** Cấm TBD, TODO, `??`, `<…>` chưa điền, `[…]`.
8. **Đủ hành vi bất thường.** Với mỗi giới hạn/điều kiện nguồn nêu, có yêu cầu "Nếu/Khi … từ chối/xử lý …" nếu hệ quả đó **suy ra bắt buộc** (ghi `Suy ra`); nếu hệ quả không suy ra được từ nguồn (không biết từ chối hay cắt bớt) → GAP.
9. **Phân quyền là yêu cầu.** Ai được làm gì viết thành yêu cầu riêng ở module sở hữu, không viết thành bảng quyền ngoài yêu cầu.

### 4.3 Hạt yêu cầu (granularity)

- Mỗi giá trị giới hạn độc lập (số tối thiểu, số tối đa, độ dài) → một yêu cầu cấp dưới.
- Mỗi nhánh của một luồng (ví dụ: nội dung < 20 từ; nội dung đã đổi sau khi gợi ý) → một yêu cầu cấp dưới.
- Tính năng tổng hợp nhiều luồng thì cấp trên nêu mục tiêu hành vi, cấp dưới chia nhỏ từng luồng.

## 5. Quyền sở hữu hành vi và tham chiếu chéo (quy tắc 4A)

1. Một hành vi chỉ được **viết ở đúng một module sở hữu** — module có kết quả nhìn thấy được bởi người dùng. Module khác chỉ **tham chiếu** bằng ID yêu cầu.
2. Khi chưa chắc module nào sở hữu: viết ở module đang làm, ghi điểm mở `OP-Mxx-nn` loại **Đề xuất** để stakeholder chốt chủ sở hữu.
3. Một mục nguồn có thể liên quan nhiều module (ví dụ DEC-124 tham chiếu DEC-052): module nào sở hữu hành vi thì viết yêu cầu; module khác ghi vào routing mục R5 kèm module/ID sở hữu.
4. Mục nguồn **sửa đổi** (amend) mục của module đang viết nhưng nằm ở section module khác (ví dụ M14 sửa dependency của M05) vẫn phải được Author phân loại: hoặc vào SR (nếu đổi hành vi của module này), hoặc routing R5/R6.

## 6. Routing file `ISH-RT-Mxx`

Mục đích: mọi mục nguồn OWNED không thành yêu cầu chức năng đều có chỗ đi ghi rõ — để Auditor chứng minh "không sót". Cấu trúc cố định:

```
# Routing — ISH-RT-Mxx <tên module>
<!-- [Vietnamese Doc] -->
| Mã tài liệu | ISH-RT-Mxx |
| Liên kết SR | ISH-SR-Mxx |
| Phiên bản | 0.1 |
| Ngày | YYYY-MM-DD |

## R1. Mô hình dữ liệu (Phase 8)          | Nguồn | Nội dung | Ghi chú |
## R2. Yêu cầu phi chức năng (Phase 7)    | Nguồn | Nội dung | Ghi chú |
## R3. HMI và thiết kế giao diện          | Nguồn | Nội dung | Ghi chú |
## R4. Ghi chú quy trình / phạm vi (không phải yêu cầu hệ thống) | Nguồn | Nội dung | Ghi chú |
## R5. Thuộc module khác                  | Nguồn | Nội dung | Module và ID sở hữu |
## R6. Đã bị thay thế                     | Nguồn | Bị thay bởi (ID) | Ghi chú |
## R7. Không đưa vào SR                   | Nguồn | Nội dung | Lý do |
```

Mỗi hàng ghi **ID nguồn** ở cột đầu (một ID hoặc nhiều, ngăn bằng dấu phẩy). Một mục có thể ở cả Phụ lục A và routing khi chỉ một phần nội dung thành yêu cầu. R6 dùng khi quyết định sau ghi đè quyết định trước (ví dụ DEC-048 "11 chủ đề phẳng" ghi đè QA-033 "2 tầng Category→Topic"): Author chọn quyết định **mới nhất**, nhưng phải báo stakeholder nếu hai mục có vẻ mâu thuẫn mà register không ghi rõ là ghi đè → xem mục 8.

## 7. Cơ sở dữ liệu nguồn và cách đọc

1. Mục `OWNED` = mục nằm trong section `## … Mxx …` của `decisions.md`, `issue-queue.md`, `qa-log.md` (+ dòng module-registry). Phải xử lý **tất cả**.
2. Mục `REFERENCING` = nhắc `Mxx` hoặc ID của mục OWNED ở section khác. Phải phân loại từng mục: SR / R5 / R6 / "không liên quan".
3. Mục `KEYWORD` = khớp từ khóa nghiệp vụ nhưng không nhắc module (thường nằm ở Phase 1–4, ví dụ ISS-046 "grade_level"). Phải đọc và phân loại.
4. Mục `CROSS-CUTTING` (Phase 6, prep): đọc tiêu đề; áp dụng mục liên quan (quy tắc chung như rate limit, múi giờ, xóa mềm) bằng cách ghi nguồn trong Phụ lục A hoặc routing R5.
5. **DRAFT** là nguồn gốc; register là bản đã chốt. Khi DRAFT và register lệch nhau (ví dụ DRAFT nói Tag "không giới hạn số lượng", DEC-051 nói tối đa 5): **register thắng nếu có QA/DEC ghi quyết định đó** — viết theo register, ghi cả DRAFT và register vào cột Nguồn, và báo stakeholder như một OBSERVATION nếu register không nói rõ là ghi đè DRAFT.
6. Quyết định muộn hơn ghi đè quyết định sớm hơn **chỉ** khi register ghi rõ (Superseded/Amended/Revised) hoặc cùng một vấn đề với kết luận khác. Còn lại là CONFLICT phải hỏi stakeholder.

## 8. Vòng đời, vai trò và xử lý vấn đề

### 8.1 Vai trò

| Vai trò | Được làm | Không được làm |
|---|---|---|
| **Author** | Tạo/sửa SR và routing; chạy script; đặt `OP-Mxx-nn`; hỏi stakeholder; sau khi stakeholder xác nhận thì ghi register và cập nhật SR | Tự tuyên bố SR đã đạt; viết báo cáo audit; quyết thay stakeholder |
| **Auditor** (agent độc lập, skill riêng) | Đọc SR + routing + register + DRAFT; chạy script; lập ma trận nguồn→yêu cầu; ghi báo cáo audit | Sửa SR/routing/register; hỏi stakeholder trực tiếp |
| **Stakeholder** (Phạm Văn Đức) | Trả lời, chốt, duyệt | — |

### 8.2 Trạng thái SR

`Bản nháp` (Author đang viết) → `Đã audit` (vòng audit gần nhất không còn DEFECT/CONFLICT mở) → `Đã chốt` (stakeholder đồng ý, Phụ lục B = `Không có.`).

### 8.3 Điểm cần làm rõ và cách hỏi

Mọi **GAP, mơ hồ, mâu thuẫn, đề xuất** trong lúc viết đều phải hỏi stakeholder, **mỗi lần một vấn đề**, theo khuôn:

```
Vấn đề: <một câu>
Nguồn: <ID + trích đoạn ngắn nguyên văn>
Lựa chọn: A) … — hệ quả …   B) … — hệ quả …   (C) …)
Đề xuất: <lựa chọn> vì <lý do>
```

- Trong lúc chờ trả lời: ghi `OP-Mxx-nn` ở Phụ lục B (cột `Loại` = GAP | Mơ hồ | Mâu thuẫn | Đề xuất; `Trạng thái` = Mở | Đã trả lời), viết yêu cầu liên quan ở dạng an toàn nhất **hoặc** chưa viết, và nói rõ chọn cách nào.
- Khi stakeholder trả lời: (1) ghi register **sau khi stakeholder xác nhận** — ISS/QA/DEC mới ở section `## System Requirement — Mxx: <tên>` trong `issue-queue.md`, `qa-log.md`, `decisions.md` (ID kế tiếp lấy từ script inventory); (2) sửa/bổ sung SR và Phụ lục A; (3) xóa `OP-Mxx-nn`; (4) ghi Lịch sử sửa đổi.
- Quyết định mới **làm đổi** quyết định đã có: ghi DEC mới nói rõ ghi đè DEC nào và đánh dấu mục cũ `[Amended …]`.

### 8.4 Phân loại phát hiện của Auditor

| Loại | Nghĩa | Ai xử lý |
|---|---|---|
| DEFECT | SR sai quy tắc hoặc sai/ thiếu so với nguồn | Author sửa |
| CONFLICT | Hai nguồn mâu thuẫn, hoặc SR mâu thuẫn nguồn mà Author không thể tự quyết | Author hỏi stakeholder → ghi register → sửa |
| GAP | Nguồn thiếu để viết yêu cầu kiểm chứng được | Author hỏi stakeholder |
| OBSERVATION | Nhận xét/đề xuất, không bắt buộc sửa | Stakeholder quyết |

Tối đa **2 vòng** audit–sửa cho mỗi lần phát hành; còn tồn đọng sau vòng 2 → chuyển stakeholder quyết. Bằng chứng của Auditor phải là trích đoạn nguyên văn kèm `tệp:dòng`, đã kiểm bằng grep.

### 8.5 Chế độ sửa (revision)

Khi SR đã tồn tại hoặc Auditor đã có báo cáo: Author **không** viết lại từ đầu. Chỉ sửa mục bị nêu, giữ nguyên ID, tăng phiên bản (0.1 → 0.2 …), thêm dòng Lịch sử sửa đổi, cập nhật Phụ lục A, chạy lại `check_sr.py`.

## 9. Kiểm tra tự động

Skill Author nằm ở `.agent-instructions/system_analysis/skills/drafting-ishare-sr-module/SKILL.md` (skill Auditor sẽ thêm vào cùng thư mục `skills/`). Script nằm ở `.agent-instructions/system_analysis/sr-tools/`: `inventory.py` (gom nguồn theo module từ register + DRAFT) và `check_sr.py` (cấu trúc, header, ID, EARS, từ cấm, truy vết, bao phủ nguồn). Chỉ cần Python 3, không thư viện ngoài. `check_sr.py` thoát mã 1 nếu còn ERROR. WARN không chặn nhưng phải xử lý hoặc giải thích. Script không thay thế việc đọc: ngữ nghĩa (đúng nguồn? đủ? mâu thuẫn?) do Auditor và stakeholder kiểm.
