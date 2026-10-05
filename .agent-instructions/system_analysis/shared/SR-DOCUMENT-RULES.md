# SR-DOCUMENT-RULES — Quy tắc tài liệu System Requirement (SR) của iShare

> [Vietnamese Doc] — Theo COMMON-RULES Rule 1: tài liệu này viết bằng tiếng Việt theo yêu cầu của stakeholder (DEC-139 / QA-265).
> Đây là **nguồn quy tắc duy nhất** cho định dạng, ID, cách viết yêu cầu và quy trình của SR. Vai trò Author (`roles/sr-author`) và Auditor (`roles/sr-auditor`) chỉ mô tả *quy trình*, không lặp lại quy tắc; nếu mâu thuẫn, tài liệu này thắng.

---

## 0. Phạm vi và thẩm quyền

- SR là tài liệu **yêu cầu chức năng theo từng module**, viết từ dữ liệu đã chốt trong `registers/` và DRAFT. Mỗi module một tài liệu `ISH-SR-Mxx`.
- SR **không** chứa: mô hình dữ liệu/bảng/trường (→ Phase 8), yêu cầu phi chức năng (→ Phase 7), giải pháp công nghệ, thiết kế giao diện (→ HMI sau khi có design).
- Quy tắc này **khác có chủ đích** hai quy tắc trong vai trò `ba-interview` (`../roles/ba-interview/AGENT.md`) (output chỉ tiếng Anh; không sinh spec trước Phase 9) — xem DEC-139. Mọi quy tắc khác của BA (không bịa yêu cầu, truy vết, mỗi lần một vấn đề, ghi register) vẫn áp dụng.
- Nguồn sự thật duy nhất: DRAFT (`docs/_temp/iShare_*.md`, trích dẫn `DRAFT §x.y`) và các mục đã chốt trong registers (`ISS-nnn`, `QA-nnn`, `DEC-nnn`, `OPEN-nnn`). Không có nguồn thì không có yêu cầu.

## 1. Tệp và vị trí

Thư mục gốc: `.agents/.claude/system_analysis/output/specs/`

| Tệp | Đường dẫn | Ai viết | Ghi chú |
|---|---|---|---|
| SR module | `specs/ISH-SR-Mxx.md` | Author | Thân tài liệu sạch, không có nhãn nguồn |
| Routing module | `specs/routing/ISH-RT-Mxx.md` | Author | Mọi mục nguồn không thành yêu cầu chức năng |
| Báo cáo audit | `specs/audit/ISH-AUD-Mxx-r<n>.md` (vòng 1, 2); `ISH-AUD-Mxx-v1.md` (đợt xác minh); `ISH-AUD-Mxx-rel<n>.md` (xác minh phát hành) | Auditor (lượt MERGE, VERIFY hoặc RELEASE) | Báo cáo chính thức; các lượt P1/P2/P3 chỉ ghi tệp làm việc |
| Tệp làm việc của Author | `specs/audit/work/inventory-Mxx.md/.json`, `disposition-Mxx.md`, `tests-Mxx.md`, `selfcheck-Mxx.md`, `snapshot-ISH-SR-Mxx-v<x.y>.md` và `snapshot-ISH-RT-Mxx-v<x.y>.md` | Author (script) | Có thể tạo lại. Auditor chỉ được đọc **sau khi** hoàn tất ma trận độc lập của mình |
| Tệp làm việc của Auditor | `specs/audit/work/audit-inventory-P<k>-Mxx-r<n>.*` (mỗi lượt một bản) và `audit-inventory-Mxx-r<n>.*` (MERGE), `coverage-Mxx-r<n>.md`, `check-P<k>-Mxx-r<n>.json`, `check-Mxx-r<n>.json`, `audit-P1-Mxx-r<n>.md`, `audit-P2-Mxx-r<n>.md`, `audit-P3-Mxx-r<n>.md`, `audit-tests-Mxx-r<n>.md` | Auditor | Tên khác tên tệp của Author; mỗi lượt chỉ ghi tệp của lượt mình |

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
4. Tham chiếu chéo module dùng ID yêu cầu của module sở hữu (`ISH-M03-007`). Chưa có SR của module đó thì ghi tham chiếu dạng ID dự kiến **không được phép** — thay bằng ghi nguồn register (`DEC-nnn`) trong routing mục R5.

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
| 5.1 Tổng quan yêu cầu | Bảng `Tính năng \| Yêu cầu cấp trên \| Mức ưu tiên (MoSCoW) \| Mốc \| Ngoại lệ`. Ưu tiên/mốc ghi **một lần** ở đây. Mức ưu tiên ∈ Must/Should/Could/Won't theo `module-registry.md`; **Mốc** là giai đoạn `P0`/`P1`/`P2` (năng lực AI: `AI-P0`/`AI-P1`) theo `iShare_dev_priority.md`, không dùng mã mốc khác; cột Ngoại lệ liệt kê ID cấp dưới có mức/mốc khác module | Nhãn ưu tiên rải trong từng yêu cầu |
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

<Một–ba câu, lấy từ lời văn của nguồn. Tìm lần lượt: lý do ghi trong DEC/QA của tính năng; mục tiêu của module ở DRAFT; dòng mô tả module ở `module-registry.md`. Chỉ khi cả ba không có mới ghi "Nguồn chưa nêu lý do." (không đặt `OP`, §3.3).>

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
  - `Suy ra` — hệ quả logic bắt buộc của nguồn (ví dụ: nguồn nói "tối đa 3" ⇒ hành vi từ chối khi chọn thứ 4). **Bắt buộc** có Ghi chú nêu phép suy luận. `Suy ra` không được tạo quyết định mới (số liệu, ngoại lệ, quyền hạn): nếu có thì không viết yêu cầu đó (§3.3).
- Mục nguồn nào chỉ đưa một phần vào SR thì phần còn lại phải nằm trong routing.

### 3.3 Phạm vi bám phỏng vấn (quy tắc cao nhất về nội dung)

SR chỉ chứa **điều stakeholder đã nói** (DEC, QA, ISS, DRAFT) và hệ quả logic bắt buộc của nó (§4.5). Điều nguồn chưa nói thì SR không viết, và không hỏi stakeholder chỉ để lấp chỗ trống đó.

- **Nguồn im lặng** (số liệu, ngoại lệ, quyền hạn, hệ quả lên đối tượng liên quan, thứ tự phá hòa, chuẩn hóa chuỗi, chủ sở hữu hành vi, lý do của tính năng mà nguồn chưa nêu): Author không hỏi, không viết yêu cầu, không đặt `OP`. Author ghi một dòng ở selfcheck mục 3 (loại c) để người đọc sau biết điểm đó chưa được đặc tả. Auditor chỉ ghi OBSERVATION mức Thấp, không lập GAP, và OBSERVATION này không chặn kết luận `Đạt`.
- **Vẫn phải hỏi, chỉ hai loại:** (1) mâu thuẫn: hai nguồn nói trái nhau; (2) mơ hồ trong điều đã nói: một câu nguồn có hai cách đọc hợp lý cho kết quả khác nhau (CL-A11). Cả hai hỏi từng vấn đề một theo §8.3.
- Yêu cầu đã viết mà "Then" buộc phải chọn thêm một điều nguồn chưa nói: không hỏi để lấp. Sửa câu yêu cầu cho chỉ nói đúng điều nguồn đã nói, hoặc bỏ yêu cầu đó, rồi ghi điểm ấy ở selfcheck mục 3.
- Khi stakeholder tự bổ sung hoặc đổi quyết định, câu trả lời đó là nguồn mới và được ghi register như thường lệ.
- Hệ quả: Phụ lục B chỉ còn `OP` loại Mơ hồ hoặc Mâu thuẫn; không còn loại GAP hay Đề xuất ở `OP`.

## 4. Quy tắc viết yêu cầu

### 4.1 Mẫu câu (EARS bằng tiếng Việt)

Chủ ngữ của "phải" **luôn là "hệ thống"**. Người dùng/vai trò chỉ xuất hiện trong vế điều kiện.

| Loại | Mẫu | Dùng khi |
|---|---|---|
| Phổ quát | `Hệ thống phải <hành vi>.` | Luôn đúng, không điều kiện |
| Theo trạng thái | `Trong khi <trạng thái kéo dài>, hệ thống phải <hành vi>.` | Hành vi gắn với một trạng thái |
| Theo sự kiện | `Khi <sự kiện>, hệ thống phải <hành vi>.` | Có tác nhân kích hoạt tức thời |
| Tính năng tùy chọn | `Đối với <tính năng/cấu hình>, hệ thống phải <hành vi>.` | Chỉ áp dụng khi tính năng/cấu hình có mặt |
| Bất thường | `Nếu <điều kiện bất thường>, thì hệ thống phải <hành vi>.` | Lỗi hoặc ngoại lệ không do hành động hợp lệ của người dùng (xem §4.6). Từ chối vì người dùng vi phạm giới hạn dùng mẫu `Khi` |
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
8. **Đủ hành vi bất thường.** Mỗi giới hạn nguồn nêu bằng "tối đa / tối thiểu / không quá / chỉ khi" phải có yêu cầu cho trường hợp vi phạm. Quy tắc suy ra: vi phạm giới hạn ⇒ "hệ thống phải từ chối <giá trị hoặc hành động vi phạm>" là `Suy ra` hợp lệ (ghi phép suy luận ở Phụ lục A). **Cách thể hiện** việc từ chối (chặn nhập, thông báo lỗi, vị trí hiển thị) không viết trong SR — đưa vào routing R3. Chỉ khi nguồn cho thấy hệ quả *khác* từ chối (cắt bớt, tự sửa, chuyển trạng thái) hoặc hai nguồn mâu thuẫn về hệ quả thì mới là GAP/CONFLICT phải hỏi. Thiếu cả yêu cầu từ chối lẫn GAP được hỏi là DEFECT.
9. **Phân quyền là yêu cầu.** Ai được làm gì viết thành yêu cầu riêng ở module sở hữu, không viết thành bảng quyền ngoài yêu cầu.
10. **Nêu đủ ngữ cảnh. Khi nguồn nêu, câu yêu cầu cho biết *ai* (tác nhân), *làm gì với đối tượng nào*, và *trong ngữ cảnh hoặc thời điểm nào* (khi tạo bài, khi sửa bài, khi xuất bản…). Câu cụt như "hệ thống phải cho phép gán Topic" mà nguồn đã nói rõ thời điểm là câu thiếu chi tiết (xem §4.7).

### 4.3 Hạt yêu cầu (granularity)

- Mỗi giá trị giới hạn độc lập (số tối thiểu, số tối đa, độ dài) → một yêu cầu cấp dưới.
- Mỗi nhánh của một luồng (ví dụ: nội dung < 20 từ; nội dung đã đổi sau khi gợi ý) → một yêu cầu cấp dưới.
- Tính năng tổng hợp nhiều luồng thì cấp trên nêu mục tiêu hành vi, cấp dưới chia nhỏ từng luồng.

### 4.4 Cặp ví dụ sai → đúng

Các ví dụ dưới đây dùng đối tượng và số liệu **minh họa**, không phải nguồn của dự án. Mục đích là hiệu chỉnh cách viết và cách chấm; không chép số liệu sang SR thật.

| # | Câu sai | Câu đúng hoặc đích | Lỗi |
|---|---|---|---|
| 1 | Bình luận phải được gửi khi người dùng bấm gửi. | Khi người dùng gửi một bình luận không rỗng, hệ thống phải thêm bình luận đó vào bài viết. | Câu bị động, chủ ngữ của "phải" không phải "hệ thống"; thiếu điều kiện đo được |
| 2 | Hệ thống nên cho phép sửa bình luận trong một khoảng thời gian hợp lý. | Khi người dùng sửa bình luận của mình trong vòng 15 phút sau khi đăng, hệ thống phải lưu nội dung đã sửa. (Số 15 phải có nguồn; không có thì không viết yêu cầu này, §3.3.) | "nên" thay cho "phải"; "hợp lý" không đo được |
| 3 | Hệ thống phải lưu và hiển thị bình luận. | Hai yêu cầu: "Khi người dùng gửi một bình luận không rỗng, hệ thống phải thêm bình luận đó vào bài viết." và "Khi người dùng mở một bài viết, hệ thống phải hiển thị các bình luận của bài viết đó." | Hai hành vi trong một câu |
| 4 | Hệ thống phải cho phép sửa và/hoặc xóa bình luận của mình. | Hai yêu cầu riêng cho sửa và cho xóa. | "và/hoặc" |
| 5 | Hệ thống phải ghi bình luận vào bảng `comments`. | Khi người dùng gửi một bình luận không rỗng, hệ thống phải thêm bình luận đó vào bài viết. Chi tiết bảng/trường chuyển sang routing R1. | Tên bảng là giải pháp |
| 6 | Hệ thống phải gửi thông báo nếu cần thiết. | Khi có người trả lời bình luận của User A, hệ thống phải gửi thông báo cho User A. | Cụm thoát "nếu cần thiết" |
| 7 | Khi người dùng xóa bài viết, hệ thống phải ẩn nó khỏi danh sách. | … hệ thống phải ẩn bài viết đó khỏi danh sách. | Đại từ "nó" |
| 8 | Bình luận nên dài vừa phải. | Hai yêu cầu: "Hệ thống phải giới hạn mỗi bình luận tối đa 500 ký tự." và "Khi người dùng gửi bình luận dài hơn 500 ký tự, hệ thống phải từ chối bình luận đó." (Số 500 có nguồn.) | Mơ hồ; thiếu hành vi khi vi phạm giới hạn |
| 9 | Khi bài viết đang ở trạng thái Khóa, hệ thống phải từ chối bình luận mới. | Trong khi bài viết ở trạng thái Khóa, hệ thống phải từ chối bình luận mới. | "đang ở" là trạng thái kéo dài → mẫu "Trong khi" |
| 10 | Mod có thể xóa bình luận. | Khi Mod yêu cầu xóa một bình luận, hệ thống phải xóa bình luận đó. | Chủ ngữ sai; "có thể" mơ hồ |
| 11 | Hệ thống phải trả kết quả trong vòng 2 giây. | Không viết trong SR. Ghi vào routing R2 kèm nguồn. | Yêu cầu phi chức năng |
| 12 | Nút Gửi phải màu xanh và nằm dưới ô nhập. | Không viết trong SR. Ghi vào routing R3. | Thiết kế giao diện |
| 13 | Hệ thống phải cho phép người dùng gắn nhãn cho bài viết. | Hệ thống phải cho phép người dùng gắn nhãn cho bài viết khi tạo hoặc chỉnh sửa bài viết. (Chỉ khi nguồn nêu thời điểm; nguồn không nêu thì không tự thêm, §3.3.) | Câu cụt: thiếu ngữ cảnh mà nguồn đã nói |
| 14 | Hệ thống phải cho phép Mod gộp hai nhãn. | Hai yêu cầu: "Khi Mod gộp hai nhãn, hệ thống phải chuyển toàn bộ bài viết đang gắn nhãn nguồn sang nhãn đích." và (sau khi stakeholder trả lời) một yêu cầu cho nhãn nguồn sau khi gộp. | Chỉ nêu hành động, thiếu hệ quả lên đối tượng liên quan mà người dùng nhìn thấy |

### 4.5 Danh mục `Suy ra` được phép và không được phép

`Suy ra` chỉ hợp lệ khi là hệ quả logic bắt buộc của một câu nguồn (§3.2). Danh mục này giúp Author và Auditor chấm cùng một thước.

Được phép (ghi `Suy ra` kèm phép suy luận ở cột Ghi chú):

- Giới hạn trên hoặc dưới ("tối đa", "tối thiểu", "không quá", "ít nhất") ⇒ hệ thống từ chối giá trị nằm ngoài khoảng. Không nêu cách thể hiện (§4.2 mục 8).
- "Chỉ X mới được làm Y" ⇒ hệ thống từ chối khi người không phải X yêu cầu Y.
- "Phải có A mới được B" ⇒ hệ thống từ chối B khi thiếu A.

Không được suy ra. Nếu cần thì phải là `Nói thẳng`, nếu không thì không viết (§3.3):

- giá trị mặc định; thông điệp hay nội dung thông báo cụ thể (→ R3); thời gian chờ, thời hạn, số lần thử lại;
- thứ tự sắp xếp, phân trang, số mục mỗi trang;
- hành vi khi dữ liệu rỗng hoặc xử lý đồng thời;
- xóa hay giữ lại dữ liệu liên quan khi một đối tượng bị xóa;
- quyền của vai trò mà nguồn không nhắc ("Admin chắc cũng được");
- tính năng "thường thấy ở diễn đàn khác".

### 4.6 Chọn mẫu câu

Đi theo thứ tự câu hỏi, dừng ở câu đầu tiên trả lời "có":

1. Hành vi luôn đúng, không điều kiện? → Phổ quát (`Hệ thống phải …`).
2. Điều kiện là **sự kiện tức thời** (người dùng gửi, bấm, đăng; hết hạn)? → `Khi …`. Việc vi phạm một giới hạn do hành động của người dùng cũng là sự kiện: `Khi người dùng gửi bình luận dài hơn 500 ký tự, hệ thống phải từ chối …`.
3. Điều kiện là **trạng thái kéo dài** (bài viết đang Khóa, người dùng đang đăng nhập)? → `Trong khi …`.
4. Điều kiện là **lỗi hoặc ngoại lệ không do hành động hợp lệ của người dùng** (dịch vụ không phản hồi, dữ liệu không nhất quán)? → `Nếu …, thì …`.
5. Chỉ áp dụng khi tính năng hoặc cấu hình có mặt? → `Đối với …`.
6. Hai điều kiện (một trạng thái và một sự kiện)? → Phức hợp. Từ ba điều kiện trở lên thì tách thành nhiều yêu cầu hoặc đưa một điều kiện vào định nghĩa trạng thái ở mục 5.2.

### 4.7 Độ chi tiết vừa đủ: khung quét hành vi

Mục tiêu: mỗi tính năng cho người đọc biết *ai* làm *gì* với *đối tượng nào*, *khi nào*, và *hệ quả nhìn thấy*; không dài hơn nguồn cho phép và không phải bản phỏng vấn đầy đủ. Với **mỗi tính năng**, Author quét bảy câu hỏi dưới đây (Auditor quét độc lập ở lượt P3) và ghi kết quả vào bảng "Quét khung hành vi" của selfcheck:

| # | Câu hỏi | Ví dụ gợi ý |
|---|---|---|
| 1 | Ai được làm (vai trò)? | Chỉ Mod hoặc Admin; mọi người dùng; Guest có được không |
| 2 | Trong ngữ cảnh hoặc thời điểm nào? | Khi tạo bài, khi sửa bài, trước khi xuất bản |
| 3 | Kết quả chính nhìn thấy là gì? | Bài chuyển sang Topic đích |
| 4 | Giới hạn nào và vi phạm thì sao? | Tối đa 5; thẻ thứ 6 bị từ chối |
| 5 | Hệ quả lên đối tượng liên quan? | Đối tượng nguồn sau khi gộp; bài đã gắn trước đó; người đang theo dõi |
| 6 | Sau khi tạo, còn sửa, xóa hoặc ẩn được không, ai làm? | Không xóa Topic; chỉ ẩn Tag khi khẩn cấp |
| 7 | Khi dịch vụ ngoài (AI) hoặc điều kiện bất thường không đáp ứng thì sao? | AI không khả dụng; hết thời gian chờ |

Mỗi câu trả lời thuộc **đúng một** trong bốn loại:

- **(a) Nguồn nêu** → viết thành yêu cầu (`Nói thẳng`).
- **(b) Suy ra được** theo §4.5 → viết thành yêu cầu (`Suy ra`, kèm phép suy luận).
- **(c) Nguồn im lặng** → không viết, không hỏi, không đặt `OP` (§3.3). Chỉ ghi một dòng ở selfcheck mục 3 để người đọc sau biết điểm này chưa được đặc tả.
- **(d) Không áp dụng** → ghi lý do một câu (ví dụ "không có thao tác sửa sau khi tạo").

Ví dụ giả định (M99): nguồn nói "Mod có thể gộp hai Chuyên mục; không xóa Chuyên mục". Quét: (1) Mod → (a) yêu cầu quyền; (3) bài chuyển sang Chuyên mục đích → (a); (6) không xóa → (a) và `Suy ra` từ chối yêu cầu xóa; (5) Chuyên mục nguồn sau khi gộp còn hiển thị hay không → **(c)**; (5) người đang theo dõi Chuyên mục nguồn thì sao → **(c)**. Kết quả: ba yêu cầu viết ngay, hai điểm (c) chỉ ghi ở selfcheck, không hỏi và không đặt `OP`; không có yêu cầu nào tự bịa.

Phạm vi: khung này chỉ nhằm tìm *hành vi người dùng quan sát được* còn thiếu. Nó không cho phép viết thêm tính năng "thường thấy ở diễn đàn khác", thông điệp cụ thể (→ R3) hay cách cài đặt (→ R1/R2).

## 5. Quyền sở hữu hành vi và tham chiếu chéo (quy tắc 4A)

1. Một hành vi chỉ được **viết ở đúng một module sở hữu** — module có kết quả nhìn thấy được bởi người dùng. Module khác chỉ **tham chiếu** bằng ID yêu cầu.
2. Khi chưa chắc module nào sở hữu: theo `DEC` đã có và `module-registry.md`; nếu nguồn không chỉ ra thì viết ở module đang làm và ghi chủ sở hữu dự kiến ở routing R5 (không đặt `OP`, §3.3).
3. Một mục nguồn có thể liên quan nhiều module (ví dụ DEC-124 tham chiếu DEC-052): module nào sở hữu hành vi thì viết yêu cầu; module khác ghi vào routing mục R5 kèm module/ID sở hữu.
4. Mục nguồn **sửa đổi** (amend) mục của module đang viết nhưng nằm ở section module khác (ví dụ M14 sửa dependency của M05) vẫn phải được Author phân loại: hoặc vào SR (nếu đổi hành vi của module này), hoặc routing R5/R6.
5. **Tách theo câu.** Một mục nguồn thường gộp nhiều hành vi có chủ sở hữu khác nhau (ví dụ "tính điểm Trending" của M05 và "hiển thị trong Feed" của M14; "quan hệ theo dõi Topic" của M05 và "gửi thông báo khi có bài mới" của M07). Với **mỗi mục OWNED**, đọc từng câu của nguồn và hỏi "ai sở hữu kết quả người dùng nhìn thấy?". Phần của module đang viết → SR; phần của module khác → một hàng R5 riêng (kèm module và ID sở hữu, hoặc "chưa có SR, ghi nguồn <ID>"). Cùng một ID nguồn nằm ở cả Phụ lục A và R5 là hợp lệ (`check_sr` báo INFO COV-03). Thiếu hàng R5 cho phần thuộc module khác là DEFECT (CL-A10, CL-E03).

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

### 6.1 Chọn đích routing

| Nội dung của mục nguồn | Đích |
|---|---|
| Bảng, trường, kiểu dữ liệu, khóa, chỉ mục, quan hệ giữa thực thể, cờ xóa mềm là một cột | R1 |
| Thời gian phản hồi, dung lượng, bảo mật, khả năng mở rộng, tính sẵn sàng; chi tiết kỹ thuật của giới hạn tần suất (cửa sổ đếm, cơ chế) | R2 |
| Bố cục, màu, nhãn nút, vị trí, hoạt ảnh, văn bản thông báo cụ thể | R3 |
| Lý do chọn phương án, thứ tự triển khai, ghi chú cho nhóm, câu hỏi đã đóng mà không tạo hành vi | R4 |
| Hành vi do module khác sở hữu (quy tắc 4A) | R5, kèm module và ID sở hữu |
| Mục đã bị một quyết định muộn hơn ghi đè | R6, kèm ID thay thế |
| Mục stakeholder đã loại khỏi phạm vi, tính năng giai đoạn sau chưa chốt, mục trùng ý đã có chỗ khác | R7, kèm lý do |
| Một mục vừa có hành vi của module này vừa có hành vi của module khác (tính toán/lưu ở đây, hiển thị hoặc thông báo ở nơi khác) | Tách theo quy tắc 4A mục 5: phần của module này → SR; phần của module khác → R5. Ghi mục ở cả Phụ lục A và routing |
| Một mục vừa có hành vi vừa có chi tiết thuộc R1–R3 (ví dụ "tối đa 5 thẻ, lưu ở bảng riêng") | Tách: hành vi → SR; chi tiết → R1–R3. Ghi mục ở cả Phụ lục A và routing |

Cột **Nội dung** của mỗi hàng routing là một câu tóm tắt ý của nguồn, đủ để người đọc hiểu mà không phải mở nguồn; không dùng "x", "…" hoặc chỉ lặp lại ID. Hàng routing giữ chỗ bị `check_sr.py` báo ERROR (RT-03).

## 7. Cơ sở dữ liệu nguồn và cách đọc

1. Mục `OWNED` = mục nằm trong section `## … Mxx …` của `decisions.md`, `issue-queue.md`, `qa-log.md` (+ dòng module-registry). Phải xử lý **tất cả**.
2. Mục `REFERENCING` = nhắc `Mxx` hoặc ID của mục OWNED ở section khác. Phải phân loại từng mục: SR / R5 / R6 / "không liên quan".
3. Mục `KEYWORD` = khớp từ khóa nghiệp vụ nhưng không nhắc module (thường nằm ở Phase 1–4, ví dụ ISS-046 "grade_level"). Phải đọc và phân loại.
4. Mục `CROSS-CUTTING` (Phase 6, prep): đọc tiêu đề; áp dụng mục liên quan (quy tắc chung như rate limit, múi giờ, xóa mềm) bằng cách ghi nguồn trong Phụ lục A hoặc routing R5.
5. **DRAFT** là nguồn gốc; register là bản đã chốt. Khi DRAFT và register lệch nhau (ví dụ DRAFT nói Tag "không giới hạn số lượng", DEC-051 nói tối đa 5): **register thắng nếu có QA/DEC ghi quyết định đó** — viết theo register, ghi cả DRAFT và register vào cột Nguồn, và báo stakeholder như một OBSERVATION nếu register không nói rõ là ghi đè DRAFT. Khi audit (CL-A08): SR theo register + ghi cả hai nguồn + đã báo → không có finding; theo register nhưng thiếu một trong hai điều kia → DEFECT Thấp; SR theo DRAFT trái register → DEFECT Cao; không có QA/DEC nào chọn giữa hai phía → CONFLICT. Lệch mà register không nói rõ là ghi đè và chưa có xác nhận của stakeholder → thêm một OBSERVATION Trung bình để stakeholder xác nhận.
6. Quyết định muộn hơn ghi đè quyết định sớm hơn **chỉ** khi register ghi rõ (Superseded/Amended/Revised) hoặc cùng một vấn đề với kết luận khác. Còn lại là CONFLICT phải hỏi stakeholder.
7. **Nơi ghi phân loại.** Mục OWNED → Phụ lục A hoặc routing. Mục REFERENCING, KEYWORD, CROSS-CUTTING: thuộc module khác → routing R5; bị thay thế → R6; được chọn áp dụng cho module → Phụ lục A hoặc routing; mục **không liên quan** chỉ ghi ở `specs/audit/work/disposition-Mxx.md` (một dòng: ID, lý do một câu). Auditor đọc tệp này sau khi hoàn tất ma trận độc lập (CL-A03).

## 8. Vòng đời, vai trò và xử lý vấn đề

### 8.1 Vai trò

| Vai trò | Được làm | Không được làm |
|---|---|---|
| **Author** | Tạo/sửa SR và routing; chạy script; đặt `OP-Mxx-nn`; hỏi stakeholder; sau khi stakeholder xác nhận thì ghi register và cập nhật SR | Tự tuyên bố SR đã đạt; viết báo cáo audit; quyết thay stakeholder |
| **Auditor** (agent độc lập, `roles/sr-auditor`, chạy theo lượt P1/P2/P3/MERGE/VERIFY/RELEASE — §8.6) | Đọc SR + routing + register + DRAFT; chạy script; tự lập ma trận nguồn→yêu cầu và ca kiểm **từ nguồn, trước khi** đọc phần truy vết và ca kiểm của Author; ghi báo cáo audit | Sửa SR/routing/register; hỏi stakeholder trực tiếp; đọc lập luận hay tệp làm việc của Author trước khi hoàn tất ma trận độc lập |
| **Stakeholder** (Phạm Văn Đức) | Trả lời, chốt, duyệt | — |

### 8.2 Trạng thái SR

`Bản nháp` (Author đang viết) → `Đã audit` (báo cáo audit gần nhất — vòng, VERIFY hoặc RELEASE — kết luận `Đạt`) → `Đã chốt` (stakeholder đồng ý, Phụ lục B = `Không có.`).

Ai đổi trạng thái và khi nào:

- Author đặt `Bản nháp` khi tạo mới và mỗi khi sửa nội dung.
- Khi báo cáo audit gần nhất có kết luận `Đạt` và SR chưa đổi nội dung kể từ đó, Author đổi sang `Đã audit` và thêm một dòng ở Lịch sử sửa đổi ("Đã audit theo ISH-AUD-Mxx-r<n>", hoặc `-v1`, `-rel<n>`), không đổi nội dung. Nội dung SR đổi sau một báo cáo `Đạt` (ví dụ trả lời một `OP`) thì trạng thái về `Bản nháp` và cần một lượt `RELEASE` mới để quay lại `Đã audit`.
- `Đã chốt` chỉ khi stakeholder nói rõ là chốt. Author đổi trạng thái, đặt phiên bản `1.0` và ghi Lịch sử. Việc chuyển tài liệu sang `docs/approved/` do stakeholder quyết (COMMON-RULES Rule 3).
- Sửa nội dung sau khi `Đã chốt`: tăng phiên bản (`1.1`, `1.2` …), trạng thái về `Bản nháp`, audit lại phần đã đổi.

### 8.3 Điểm cần làm rõ và cách hỏi

Chỉ hai loại điểm được hỏi stakeholder (§3.3): **mâu thuẫn giữa các nguồn** và **mơ hồ trong điều nguồn đã nói**. Mỗi lần **một vấn đề**, theo khuôn:

```
Vấn đề: <một câu>
Bối cảnh: <một hai câu bằng lời thường: tính năng này làm gì cho người dùng và tình huống cụ thể làm nảy sinh câu hỏi; kèm một ví dụ có số khi vấn đề liên quan đến đếm, tính hoặc sắp xếp>
Nguồn: <ID + trích đoạn ngắn nguyên văn>
Lựa chọn: A) … — hệ quả …   B) … — hệ quả …   (C) …)
Đề xuất: <lựa chọn> vì <lý do>
```

- Trong lúc chờ trả lời: ghi `OP-Mxx-nn` ở Phụ lục B (cột `Loại` = Mơ hồ | Mâu thuẫn; `Trạng thái` = Mở | Đã trả lời), viết yêu cầu liên quan ở dạng an toàn nhất **hoặc** chưa viết, và nói rõ chọn cách nào.
- Khi stakeholder trả lời: (1) ghi register **sau khi stakeholder xác nhận** — ISS/QA/DEC mới ở section `## System Requirement — Mxx: <tên>` trong `issue-queue.md`, `qa-log.md`, `decisions.md` (ID kế tiếp lấy từ script inventory); (2) sửa/bổ sung SR và Phụ lục A; (3) xóa `OP-Mxx-nn`; (4) ghi Lịch sử sửa đổi.
- Quyết định mới **làm đổi** quyết định đã có: ghi DEC mới nói rõ ghi đè DEC nào và đánh dấu mục cũ `[Amended …]`.

**Cách hỏi để mỗi vấn đề chỉ cần một lượt trả lời** (lý do: ở M05, một quy tắc sắp xếp mất bốn lượt hỏi; "ngày đăng" mất thêm một vòng; stakeholder phải hỏi lại vì thiếu bối cảnh):

- **Hỏi trọn quy tắc.** Khi vấn đề liên quan đến một quy tắc tính toán (sắp xếp, đếm, công thức, mốc thời gian, chuẩn hóa chuỗi), nêu cả quy tắc và **4–5 ví dụ biên** trong một câu hỏi, gồm cả thực thể ngoài lề (cũ, trống, bị ẩn, chữ có dấu, ký tự đặc biệt); mỗi lựa chọn kèm kết quả của chính các ví dụ đó. Không hỏi nối tiếp từng khía cạnh ("chữ cái" rồi "chữ số" rồi "dấu").
- **Nói bằng lời trước, hộp chọn sau.** Câu hỏi về công thức hoặc dữ liệu: mô tả bối cảnh và ví dụ bằng lời; chỉ dùng hộp chọn để chốt sau khi stakeholder đã hiểu các lựa chọn.
- **Mốc thời gian và đơn vị đếm có tên chuẩn.** Mọi mốc thời gian ("đăng", "tạo", "gửi", "công khai") và mọi đơn vị đếm (tiếng, ký tự, người dùng khác nhau) xuất hiện trong câu hỏi phải được định nghĩa ở 2.1 ngay sau khi stakeholder trả lời.
- **Không hỏi điểm nguồn chưa nói.** Chuẩn hóa chuỗi, biên đếm nhỏ, thứ tự phá hòa, quyền hạn hay ngoại lệ mà nguồn không nêu: không hỏi, không đặt `OP`, không viết yêu cầu (§3.3). Chỉ khi một câu nguồn đã nói có hai cách đọc cho kết quả khác nhau ở dữ liệu thường gặp thì mới hỏi.

### 8.4 Phân loại phát hiện của Auditor

| Loại | Nghĩa | Ai xử lý |
|---|---|---|
| DEFECT | SR sai quy tắc hoặc sai/ thiếu so với nguồn | Author sửa |
| CONFLICT | Hai nguồn mâu thuẫn, hoặc SR mâu thuẫn nguồn mà Author không thể tự quyết | Author hỏi stakeholder → ghi register → sửa |
| GAP | Câu nguồn **đã nói** nhưng mơ hồ: hai cách đọc hợp lý cho kết quả khác nhau (nguồn im lặng không phải GAP, §3.3) | Author hỏi stakeholder |
| OBSERVATION | Nhận xét, kể cả điểm nguồn chưa nói; không bắt buộc sửa, không chặn `Đạt` | Stakeholder xem; không hỏi lại trừ khi muốn bổ sung |

**Một finding một lớp chính.** Chọn lớp theo *việc phải làm tiếp*: cần câu trả lời mới của stakeholder → GAP hoặc CONFLICT; Author tự sửa được → DEFECT; chỉ ghi nhận → OBSERVATION. Nếu một vấn đề thật sự có hai mặt (ví dụ lệch nguồn vừa vi phạm quy tắc vừa cần stakeholder xác nhận), ghi thêm **Lớp phụ** ở bảng đầu finding; bảng tổng hợp chỉ đếm lớp chính. Không tách một vấn đề thành hai finding chỉ để đủ hai lớp.

**DEFECT cơ học** (chỉ có một cách sửa hiển nhiên, không cần quyết định nghiệp vụ — ví dụ thiếu một dòng routing, thiếu một thuật ngữ ở 2.1) Author sửa thẳng, **không** đưa vào danh sách "cần stakeholder quyết". Danh sách đó chỉ chứa GAP, CONFLICT, OBSERVATION và các lựa chọn nghiệp vụ.

Tối đa **2 vòng** audit–sửa cho mỗi lần phát hành, cộng **một đợt xác minh** (§8.6) sau vòng 2; còn tồn đọng sau đợt xác minh → chuyển stakeholder quyết. Bằng chứng của Auditor phải là trích đoạn nguyên văn kèm `tệp:dòng`, đã kiểm bằng grep. Khẳng định "nguồn không nêu X" phải kèm danh sách từ khóa đã tìm.

**Mức nghiêm trọng** (mỗi finding một mức):

| Mức | Nghĩa | Ví dụ |
|---|---|---|
| Cao | Chặn bàn giao: SR sai nguồn, thiếu hành vi nguồn đã chốt, hai yêu cầu mâu thuẫn, số liệu sai, hành vi thuộc module khác | Thiếu yêu cầu của một mục OWNED; số tối đa khác nguồn |
| Trung bình | Yêu cầu không kiểm chứng được hoặc mơ hồ; sai phân loại routing có hệ quả; trùng ý | "Nhiều thẻ" không số; ca kiểm không viết được |
| Thấp | Diễn đạt, thuật ngữ, thứ tự; không đổi nghĩa | Viết hoa vai trò không nhất quán |

**Kết luận của một vòng audit** chỉ có hai giá trị: `Đạt` (không còn DEFECT hoặc CONFLICT mở; GAP và OBSERVATION còn lại đã nằm trong Phụ lục B hoặc chuyển stakeholder) và `Chưa đạt` (còn ít nhất một DEFECT hoặc CONFLICT mở, hoặc `check_sr.py` còn ERROR). Kết luận `Đạt` là điều kiện để SR chuyển `Đã audit` (§8.2); nó không thay thế việc stakeholder chốt.

### 8.5 Chế độ sửa (revision)

Khi SR đã tồn tại hoặc Auditor đã có báo cáo: Author **không** viết lại từ đầu. Chỉ sửa mục bị nêu, giữ nguyên ID, tăng phiên bản (0.1 → 0.2 …), thêm dòng Lịch sử sửa đổi, cập nhật Phụ lục A, chạy lại `check_sr.py`.

**Rà hồi quy (bắt buộc).** Ở M05, 7 trong 11 finding mới của vòng 2 và 2 trong 3 finding của đợt xác minh là lỗi do chính bản sửa gây ra. Vì vậy mỗi ID **mới, đổi nội dung hoặc bị bỏ** phải qua bảy kiểm tra dưới đây và Author ghi kết quả vào bảng "Rà hồi quy" của selfcheck (một dòng cho mỗi ID; ô ghi `Đạt`/`Không đạt`/`Không áp dụng` kèm bằng chứng ngắn, không ghi `Đạt` cho ô chưa làm):

| # | Kiểm tra | Mã checklist |
|---|---|---|
| RG-1 | So với câu cấp trên của tính năng: cấp trên bao quát ID này, và cấp trên không hứa điều mà cấp dưới nào cũng không có | CL-C04 |
| RG-2 | Dùng `grep` tìm **mọi** yêu cầu cùng đối tượng hoặc cùng tác nhân rồi so từng cặp với ID này: không mâu thuẫn, không trùng ý | CL-C01, CL-C02 |
| RG-3 | Quyết định nguồn có từ "chỉ", "only", "không … ngoài": phải có **cả** yêu cầu bao gồm lẫn yêu cầu loại trừ | CL-B09, CL-A05 |
| RG-4 | So với mọi `OP` đang mở ở Phụ lục B: yêu cầu không chọn trước điều mà `OP` còn đang hỏi | CL-F04 |
| RG-5 | ID bị bỏ hoặc chuyển: không còn tham chiếu nào ở 5.1, 5.2, Phụ lục A, routing, `tests-Mxx.md`, thuật ngữ | CL-D05, CL-F02 |
| RG-6 | Lịch sử sửa đổi sinh từ `diff` với bản chụp trước (không từ trí nhớ): mọi khác biệt ở 2.1, 3.1, 4, 5.1, 5.2, Phụ lục A/B và routing đều có trong dòng Lịch sử | CL-F02 |
| RG-7 | Ca kiểm của mọi ID mới hoặc đổi được viết lại (kể cả ca "Chuyển trạng thái" nếu có ở 5.2); ca của ID bị bỏ được xóa | CL-B08, CL-B12 |

**Thủ tục ID khi sửa.** (1) Chuyển một yêu cầu sang tính năng khác (ví dụ vì cấp trên cũ không bao quát nó): **bỏ ID cũ** (ghi Lịch sử) và **cấp ID mới** dưới cấp trên mới; không giữ ID cũ ở chỗ mới. (2) ID cấp trong lượt sửa **chưa bàn giao** (chưa nằm trong bản chụp nào) được bỏ tự do mà không cần ghi Lịch sử, nhưng số đó vẫn không dùng lại. (3) ID đã nằm trong một bản chụp đã bàn giao: bỏ thì phải ghi Lịch sử, không dùng lại (§2 quy tắc 1).

### 8.6 Cấu trúc một vòng audit và đợt xác minh

**Một vòng audit gồm bốn lượt**, mỗi lượt do một Auditor chạy trong ngữ cảnh sạch, chỉ nhận mã module, số vòng, tên lượt và đường dẫn repo:

| Lượt | Tên | Mục checklist | Đầu ra (trong `specs/audit/work/`) |
|---|---|---|---|
| P1 | Độ phủ và ranh giới | A01–A04, A08–A10, E01–E04, F03 | `audit-P1-Mxx-r<n>.md` |
| P2 | Chất lượng yêu cầu | A05–A07, B01–B07, B10, B11, C01–C05, D01–D06, F01, F02, F05, F06 | `audit-P2-Mxx-r<n>.md` |
| P3 | Ca kiểm, mơ hồ và hành vi còn thiếu | A11, B08, B09, B12, B13, F04 | `audit-P3-Mxx-r<n>.md` và `audit-tests-Mxx-r<n>.md` |
| MERGE | Gộp | Không chấm thêm; kiểm lại bằng chứng, gộp trùng, đặt `AUD-Mxx-nn`, kết luận | `specs/audit/ISH-AUD-Mxx-r<n>.md` |

P1, P2, P3 độc lập với nhau (không đọc đầu ra của nhau) nên có thể chạy song song; MERGE chạy sau cả ba. Lý do tách: mỗi lượt chỉ giữ một câu hỏi trong đầu, và mọi mục checklist đều có một lượt chịu trách nhiệm. Mục nào không lượt nào chấm là lỗi quy trình.

**Mục chuyển lượt.** Vì ba lượt chạy song song nên một lượt không thể nhờ lượt khác chấm. Lượt thấy lỗi ngoài phạm vi của mình ghi một dòng "Chuyển lượt khác" cuối tệp, **kèm mã `CL-xxx`, trích đoạn nguyên văn và `tệp:dòng`**. Lượt MERGE xử lý từng dòng: kiểm lại bằng chứng bằng máy; nếu khớp và chưa có finding cùng nguyên nhân thì **lập finding** (ghi nguồn "chuyển lượt P<k>, MERGE đã kiểm chứng"); nếu không khớp thì loại và ghi vào Hồ sơ xác minh. MERGE không tự tìm lỗi mới ngoài các dòng chuyển lượt.

**Đợt xác minh (`VERIFY`).** Sau vòng 2, nếu chỉ còn DEFECT (không còn CONFLICT/GAP chưa trả lời), Author sửa theo báo cáo vòng 2, rồi **một** Auditor ngữ cảnh sạch chạy đợt xác minh: kiểm (a) từng finding còn mở của vòng 2, (b) mọi yêu cầu và dòng routing/Phụ lục đã đổi cùng các yêu cầu liền kề, (c) `check_sr.py` và `--tests`, (d) ca kiểm của các yêu cầu đã đổi. Phát hiện mới nằm ngoài phần đã đổi chỉ được ghi OBSERVATION. Đầu ra `specs/audit/ISH-AUD-Mxx-v1.md`, kết luận `Đạt`/`Chưa đạt` theo §8.4. **Chu kỳ audit mới.** Khi phương pháp audit đổi (checklist, lượt, ca kiểm) và stakeholder đồng ý mở chu kỳ mới, báo cáo cũ được lưu nguyên ở `specs/audit/pilot-<k>/`, vòng đánh lại từ `r1`, nhưng số `AUD-Mxx-nn` **tiếp tục** (ID vĩnh viễn, không dùng lại).

Đợt xác minh không phải vòng 3 và chỉ chạy **một lần**; `Chưa đạt` sau đó → chuyển stakeholder quyết. Nếu vòng 2 còn CONFLICT hoặc GAP chưa trả lời thì chưa chạy đợt xác minh: Author hỏi stakeholder trước, rồi sửa, rồi xác minh.

**Xác minh phát hành (`RELEASE`).** Lượt ngắn cho "chặng cuối": khi báo cáo audit gần nhất (vòng 2, `VERIFY` hoặc một `RELEASE` trước) là `Chưa đạt`, stakeholder đã quyết xong mọi GAP, CONFLICT, OBSERVATION còn lại và Author đã sửa theo (kèm rà hồi quy §8.5 và bản chụp mới); hoặc khi nội dung SR đổi sau một báo cáo `Đạt` (§8.2). **Một** Auditor ngữ cảnh sạch chỉ kiểm: (a) từng finding còn mở của báo cáo gần nhất, (b) mọi ID và dòng đã đổi cùng yêu cầu liền kề, kể cả RG-1…RG-7 chấm độc lập, (c) `check_sr.py` và `--tests`, (d) ca kiểm viết lại độc lập cho ID đổi. Không tìm kiếm chủ động ngoài phần đã đổi; điều tình cờ thấy ngoài phần đó chỉ ghi OBSERVATION. Đầu ra `specs/audit/ISH-AUD-Mxx-rel<n>.md`, kết luận `Đạt`/`Chưa đạt` theo §8.4; `Đạt` thì Author đổi SR sang `Đã audit` (§8.2). `Chưa đạt` → chuyển stakeholder quyết; chỉ chạy `rel<n+1>` khi stakeholder cho sửa tiếp, **tối đa `rel2`** cho mỗi lần phát hành, sau đó stakeholder quyết. `RELEASE` không phải vòng audit mới và không thay thế `VERIFY`.

## 9. Kiểm tra tự động

Vai trò Author nằm ở `.agent-instructions/system_analysis/roles/sr-author/AGENT.md`, vai trò Auditor ở `.agent-instructions/system_analysis/roles/sr-auditor/AGENT.md`. Script nằm ở `.agent-instructions/system_analysis/shared/sr-tools/`: `inventory.py` (gom nguồn theo module từ register + DRAFT) và `check_sr.py` (cấu trúc, header, ID, EARS, từ cấm, truy vết, bao phủ nguồn, độ mới của inventory, độ phủ ca kiểm khi truyền `--tests`). Khuôn (SR, routing, selfcheck, báo cáo audit, lời gọi Auditor) nằm ở `shared/templates/`, ví dụ hoàn chỉnh ở `shared/examples/`. Chỉ cần Python 3, không thư viện ngoài. `check_sr.py` thoát mã 1 nếu còn ERROR. WARN không chặn nhưng phải xử lý hoặc giải thích. Script không thay thế việc đọc: ngữ nghĩa (đúng nguồn? đủ? mâu thuẫn?) do Auditor và stakeholder kiểm.

## 10. Checklist chất lượng SR (dùng chung cho Author và Auditor)

Đây là **danh sách mục kiểm duy nhất**. Author dùng nó làm **tài liệu tham chiếu khi viết** (biết trước Auditor sẽ chấm gì) và **không tự chấm cả 45 mục**: ở M05, mọi finding của cả ba đợt audit đều nằm ở mục mà selfcheck đã ghi `Đạt`, nghĩa là tự chấm không bắt được lỗi nào (người viết có cùng điểm mù với lúc viết). Phần Author tự làm là phần có tác dụng thật: kết quả script, ca kiểm dựng từ nguồn (§11), bảng quét khung hành vi (§4.7) và bảng rà hồi quy (§8.5). Auditor dùng đúng danh sách này để audit. Mỗi finding của Auditor phải trích **mã mục** (`CL-xxx`) bị vi phạm; mục nào vi phạm mà chưa có mã thì đó là dấu hiệu checklist thiếu — Auditor ghi OBSERVATION đề xuất thêm mục, không tự đặt mã mới.

Cột **Tự động** là mã của `check_sr.py` bao phủ mục đó. Mục có mã tự động vẫn cần đọc khi script chỉ bao phủ một phần (ghi "một phần"). Mục `—` chỉ kiểm bằng đọc nguồn và đọc SR; script không làm thay được.

**Cách điền.** Mục tự động đầy đủ: ghi một dòng kết quả script cho cả nhóm. Mục đọc tay: ghi `Đạt`, `Không đạt` hoặc `Không áp dụng` kèm bằng chứng ngắn (ID yêu cầu, ID nguồn, `tệp:dòng`). Không được ghi `Đạt` cho mục chưa kiểm. Auditor điền ở mục 7 của báo cáo audit. Author ghi phần việc của mình vào `specs/audit/work/selfcheck-Mxx.md` (khuôn `shared/templates/selfcheck-template.md`: kết quả script, ca kiểm, quét khung hành vi, rà hồi quy, WARN giữ lại, điểm đã raise).

### Nhóm A — Truy vết và độ phủ nguồn

| Mã | Điều phải đúng | Tự động | Cách kiểm đọc tay |
|---|---|---|---|
| CL-A01 | Mọi câu/ý của DRAFT thuộc phạm vi module có chỗ đi: thành yêu cầu (Phụ lục A) hoặc nằm trong routing | — | Đi từng câu của mục DRAFT của module, tìm ID/nguồn tương ứng; câu không có chỗ đi là DEFECT (sót) |
| CL-A02 | Mọi mục OWNED nằm ở Phụ lục A hoặc routing | COV-01, INV-01 | Đối chiếu danh sách OWNED của inventory với Phụ lục A + routing |
| CL-A03 | Mọi mục REFERENCING và KEYWORD đã được phân loại (SR / R5 / R6 / không liên quan) và phân loại hợp lý | — | Mục không nằm trong SR/routing phải có dòng trong `disposition-Mxx.md` (§7.7) kèm lý do hợp lý. Đọc đủ mọi mục REFERENCING; KEYWORD kiểm lấy mẫu có chủ đích (mục có từ khóa nghiệp vụ trùng module). Không có `disposition` thì `Không đạt` |
| CL-A04 | ID nguồn có thật trong register hoặc đúng dạng `DRAFT §x.y` | COV-02, TRC-06 | — |
| CL-A05 | Cơ sở `Nói thẳng`: nguồn nêu rõ đúng hành vi/giá trị đó | — | Mở nguồn ghi ở cột Nguồn, so nguyên văn với yêu cầu; diễn đạt khác nhưng cùng nghĩa là đạt |
| CL-A06 | Cơ sở `Suy ra`: Ghi chú nêu phép suy luận; không tạo số liệu, ngoại lệ hoặc quyền hạn mới | TRC-08 (một phần) | Thử suy luận lại từ nguồn; nếu cần thêm giả định ngoài nguồn thì không phải `Suy ra` và không được viết (§3.3) |
| CL-A07 | Mỗi con số, giới hạn, đơn vị trong SR tìm thấy trong nguồn ghi ở cột Nguồn | — | `grep -n` từng con số; số không có nguồn là DEFECT |
| CL-A08 | DRAFT lệch register xử lý đúng §7.5: viết theo register, cả hai nguồn nằm ở cột Nguồn, stakeholder đã được báo | — | So số liệu DRAFT và register; kiểm Phụ lục A/B và lịch sử có dấu vết đã báo |
| CL-A09 | Quyết định bị thay thế xử lý đúng §7.6: chỉ theo quyết định mới khi register ghi rõ ghi đè; còn lại là CONFLICT đã được hỏi | — | Tìm `Superseded/Amended/Revised` và các cặp cùng vấn đề kết luận khác |
| CL-A10 | Mục nguồn chỉ một phần thành yêu cầu thì phần còn lại nằm ở routing | COV-03 (INFO, một phần) | Với mục nằm ở cả hai nơi, xác nhận hai phần không trùng và không bỏ sót phần nào |
| CL-A11 | Không còn **mơ hồ kế thừa từ nguồn**: mọi điều kiện, công thức, cửa sổ thời gian, đơn vị, đối tượng áp dụng của nguồn OWNED chỉ đọc được một cách; chỗ có từ hai cách đọc hợp lý đã được hỏi stakeholder (có ISS/QA/DEC) hoặc đang ở Phụ lục B | — | Dựng ví dụ số hoặc tình huống **từ nguồn** (không từ SR), theo §11.3. Nếu hai người đọc cùng câu có thể cho hai kết quả khác nhau thì là GAP — kể cả khi SR chép đúng nguồn |

### Nhóm B — Chất lượng từng yêu cầu

| Mã | Điều phải đúng | Tự động | Cách kiểm đọc tay |
|---|---|---|---|
| CL-B01 | Đúng mẫu EARS (§4.1), chủ ngữ của "phải" là "hệ thống" | EARS-01, EARS-02, EARS-03 | Mẫu được chọn phải đúng loại (sự kiện / trạng thái / bất thường …) |
| CL-B02 | Một ý một yêu cầu; không "và/hoặc" | RULE-01, RULE-02, RULE-08 | Một yêu cầu có hai hành vi kiểm chứng độc lập thì tách |
| CL-B03 | Đo được: giá trị cụ thể kèm đơn vị; không từ mơ hồ | RULE-04 (một phần) | Từ ngoài danh sách cấm nhưng mơ hồ về nghĩa cũng tính |
| CL-B04 | Không cụm thoát | RULE-03 | — |
| CL-B05 | Không đại từ thay thế | RULE-05 | Kiểm "này/đó/kia" có chỉ rõ đối tượng không |
| CL-B06 | Không nêu giải pháp, tên bảng/trường, công nghệ, cơ chế cài đặt | RULE-06, RULE-07 (một phần) | Từ ngoài danh sách (ví dụ "lưu vào", "đồng bộ qua") cũng tính |
| CL-B07 | Không placeholder | RULE-09 | — |
| CL-B08 | Kiểm chứng được và **xác định duy nhất**: viết được ca kiểm chấp nhận (điều kiện đầu, tác nhân, kết quả quan sát được) cho **100%** yêu cầu cấp dưới, và kết quả mong đợi suy ra được từ câu yêu cầu mà không cần giả định thêm | TST-01, TST-02, TST-05 (một phần) | Không lấy mẫu. Yêu cầu có số liệu, công thức hoặc thời gian phải có ví dụ số tính tay (§11.3). Không viết được, hoặc phải chọn một cách đọc của nguồn để viết, là DEFECT hoặc GAP |
| CL-B09 | Đủ hành vi bất thường: mỗi giới hạn/điều kiện của nguồn có yêu cầu từ chối/xử lý nếu suy ra bắt buộc; nếu không suy ra được thì không viết (§3.3) | — | Với mỗi "tối đa/tối thiểu/chỉ khi", hỏi "vi phạm thì sao?" và tìm câu trả lời trong SR |
| CL-B10 | Hạt đúng §4.3: mỗi giới hạn độc lập và mỗi nhánh luồng một yêu cầu cấp dưới | — | Áp dụng cho yêu cầu cấp dưới: một yêu cầu cấp dưới chứa hai giá trị giới hạn hoặc hai nhánh là DEFECT. Yêu cầu cấp trên được nêu mục tiêu tổng quát (ví dụ "từ 1 đến 3 chủ đề") với điều kiện mỗi cận có yêu cầu cấp dưới riêng |
| CL-B11 | Phân quyền viết thành yêu cầu riêng ở module sở hữu, không dựa vào bảng quyền ngoài yêu cầu | — | Tìm câu có vai trò (Guest/User/Mod/Admin) mà không có yêu cầu quyền tương ứng |
| CL-B12 | Tệp ca kiểm của Author (`tests-Mxx.md`) đúng khuôn §11.2 và đủ: mọi yêu cầu cấp dưới có ít nhất một ca; có đủ loại ca bắt buộc theo §11.3 (biên, vi phạm, quyền, thời gian, công thức); mọi "Giả định cần thêm" đã được hỏi stakeholder hoặc nằm ở Phụ lục B | TST-01…05 | Đọc tệp ca kiểm cạnh từng yêu cầu; ca "Then" mơ hồ ("hợp lý", "đúng") hoặc không có số khi yêu cầu có số là không đạt |
| CL-B13 | Đủ ngữ cảnh và hành vi liên quan: mỗi tính năng đã quét khung hành vi §4.7; điểm nguồn nêu hoặc suy ra được đã thành yêu cầu; điểm nguồn im lặng không được viết thành yêu cầu và được ghi ở selfcheck mục 3; câu yêu cầu nêu đủ tác nhân, đối tượng, ngữ cảnh khi nguồn nêu | — | Quét bảy câu hỏi §4.7 từ nguồn cho từng tính năng, rồi so với SR và bảng quét trong selfcheck. Nguồn nêu mà SR thiếu: DEFECT. Nguồn im lặng: không phải finding (tối đa OBSERVATION Thấp) |

### Nhóm C — Chất lượng cả bộ yêu cầu

| Mã | Điều phải đúng | Tự động | Cách kiểm đọc tay |
|---|---|---|---|
| CL-C01 | Không hai yêu cầu nào mâu thuẫn (cùng đối tượng, khác giá trị hoặc hành vi) | — | Gom yêu cầu theo đối tượng (bài viết, thẻ, chủ đề …) rồi so từng cặp |
| CL-C02 | Không trùng ý giữa các yêu cầu, kể cả cấp trên và cấp dưới | — | Cấp dưới chỉ nói lại cấp trên là trùng |
| CL-C03 | Thuật ngữ nhất quán: mỗi thuật ngữ/vai trò được dùng có trong 2.1, mỗi mục của 2.1 được dùng; một khái niệm một tên; vai trò viết hoa nhất quán | — | Liệt kê danh từ riêng và vai trò xuất hiện trong mục 5 rồi đối chiếu 2.1 |
| CL-C04 | Cấp trên nêu đúng mục tiêu và các cấp dưới bao quát đủ, không vượt ra ngoài; "Lý do" khớp lời văn của nguồn | — | Đọc "Lý do" cạnh nguồn; cấp dưới thêm hành vi cấp trên không nói là DEFECT |
| CL-C05 | Mục 5.1 và 5.2 khớp thân tài liệu: mọi tính năng có hàng ở 5.1; ưu tiên/mốc khớp `module-registry.md` và `iShare_dev_priority.md`; bảng chuyển trạng thái trỏ đúng ID và không có trạng thái "treo" | STR-09 (một phần) | Đối chiếu ba nơi |

### Nhóm D — Cấu trúc, ID, phân cấp (tự động)

| Mã | Điều phải đúng | Tự động | Cách kiểm đọc tay |
|---|---|---|---|
| CL-D01 | Header đúng: mã, tác giả, trạng thái, phiên bản, ngày, không có người duyệt | HDR-01…08 | — |
| CL-D02 | Cấu trúc mục đúng thứ tự, đủ mục con; HMI và Chuyển màn hình là hai mục cuối của mục 5; mục 5.1 có bảng đúng khuôn; có `[Vietnamese Doc]` | STR-01…09 | — |
| CL-D03 | Mỗi tính năng có đúng một yêu cầu cấp trên, ít nhất một cấp dưới và có "Lý do" | REQ-00…04 | — |
| CL-D04 | ID đúng dạng, không trùng, thuộc module, cấp dưới thuộc cấp trên; ở chế độ sửa: ID cũ không đổi nghĩa, không đánh số lại, không dùng lại | ID-01…06 (một phần) | So với phiên bản trước và lịch sử sửa đổi |
| CL-D05 | Phụ lục A đủ hai chiều: mọi ID yêu cầu một dòng; mọi dòng trỏ ID có thật; cột đủ và hợp lệ | TRC-01…05, TRC-07, TRC-09, TRC-10 | — |
| CL-D06 | Tham chiếu ID tồn tại; tham chiếu module khác chỉ khi SR của module đó đã có | REF-01, REF-02 | Với REF-02, mở SR đích kiểm ID |

### Nhóm E — Ranh giới và quyền sở hữu

| Mã | Điều phải đúng | Tự động | Cách kiểm đọc tay |
|---|---|---|---|
| CL-E01 | SR không chứa mô hình dữ liệu, NFR, HMI, giải pháp hoặc ghi chú quy trình; những thứ đó nằm đúng ở R1–R4 | — | Đọc mục 4 và 5 tìm nội dung thuộc Phase 7/8 hoặc giao diện |
| CL-E02 | Mỗi hành vi chỉ viết ở module sở hữu (quy tắc 4A); hành vi của module khác chỉ được tham chiếu | — | Tìm yêu cầu mô tả kết quả mà người dùng nhìn thấy ở module khác |
| CL-E03 | Routing phân loại đúng R1–R7; R5 có module/ID sở hữu; R6 có "bị thay bởi"; R7 có lý do chấp nhận được | RT-01…04 (một phần) | Đọc từng hàng routing và nguồn của nó; mục "không đưa vào SR" mà thực ra có hành vi là DEFECT |
| CL-E04 | Không thông tin riêng tư/pháp lý, số liệu hay luật do Author tự thêm; mục 4.1 chỉ ghi luật stakeholder đã nêu | — | Xem OPEN-008; truy từng luật, quy định nêu trong SR về nguồn |

### Nhóm F — Hồ sơ và quy trình

| Mã | Điều phải đúng | Tự động | Cách kiểm đọc tay |
|---|---|---|---|
| CL-F01 | Phụ lục B đúng: mỗi `OP` có loại và trạng thái; không còn OP đã được trả lời; bản `Đã chốt` ghi `Không có.` | OPN-01…03 | — |
| CL-F02 | Lịch sử sửa đổi có dòng cuối trùng phiên bản; mô tả đúng thay đổi thực tế (chế độ sửa) | REV-01…03 (một phần) | So nội dung thay đổi với mô tả |
| CL-F03 | Mọi câu trả lời của stakeholder đã có ID trong register và SR khớp; không có quyết định chỉ tồn tại trong SR | — | Tìm số liệu/ngoại lệ/quyền hạn trong SR mà không có nguồn là QA/DEC |
| CL-F04 | Mọi mơ hồ và mâu thuẫn trong điều nguồn đã nói đã được raise cho stakeholder; SR không chứa điều nguồn chưa nói | — | Tìm chỗ SR chọn một phương án hoặc thêm một hành vi khi nguồn chưa nói: DEFECT, Author bỏ khỏi SR |
| CL-F05 | Mục 1, 3, 4 đúng nội dung: 1 và 4 không có yêu cầu hay "phải"; 3.1 liệt kê đủ nguồn đã dùng kèm ngày; 3.2 đúng | TRC-11 (WARN, một phần) | Mọi ID nguồn cite ở Phụ lục A, Phụ lục B và routing có mặt ở 3.1 |
| CL-F06 | Tiếng Việt, có `[Vietnamese Doc]`, văn phong chuyên nghiệp, chỉ giữ tiếng Anh cho thuật ngữ bắt buộc | STR-08, RT-04 (một phần) | Văn phong và thuật ngữ tiếng Anh đọc tay |

## 11. Ca kiểm và phát hiện mơ hồ

### 11.1 Vì sao cần

Đối chiếu SR với nguồn **không** lộ ra chỗ mơ hồ nằm sẵn trong nguồn: SR chép đúng chỗ mơ hồ nên trông "khớp". Mơ hồ chỉ lộ ra khi có người phải **tính ra một kết quả cụ thể**. Vì vậy ca kiểm là công cụ phát hiện, không chỉ là bước kiểm chứng sau cùng.

Ví dụ giả định (không phải module thật): nguồn viết "Điểm Hot của Chuyên mục = Σ(1 + 3 × lượt thích) trên mọi bài trong cửa sổ 7 ngày". Ca kiểm: "Chuyên mục K chỉ có bài B đăng 20 ngày trước, hôm qua B nhận 10 lượt thích; điểm Hot của K bây giờ là bao nhiêu?". Có hai kết quả hợp lý (0 hoặc 30) tùy "trong cửa sổ" áp dụng cho ngày đăng hay ngày thích. Ca kiểm không viết được một "Then" duy nhất → GAP: hỏi stakeholder. Số "1" mỗi bài cũng là một câu hỏi riêng nếu nguồn không giải thích.

### 11.2 Tệp `tests-Mxx.md` (Author)

Tệp làm việc ở `specs/audit/work/tests-Mxx.md`, một bảng, cột cố định:

| ID ca | ID yêu cầu | Loại | Given | When | Then | Giả định cần thêm |
|---|---|---|---|---|---|---|
| T-001 | ISH-M99-001.2 | Biên | Bài đã có 3 Chuyên mục | Người dùng chọn Chuyên mục thứ 4 | Hệ thống từ chối lựa chọn; bài vẫn có 3 Chuyên mục | — |

- **Loại** ∈ {Thường, Biên, Vi phạm, Quyền, Thời gian, Công thức, Lỗi, Chuyển trạng thái}. `Chuyển trạng thái` dành cho các yêu cầu có mặt ở mục 5.2: một ca chuyển hợp lệ và một ca thử chuyển từ trạng thái không cho phép (`check_sr.py` TST-07).
- **Then** là kết quả quan sát được, có số cụ thể khi có số; không dùng "hợp lý", "đúng", "như mong đợi".
- **Giả định cần thêm**: ghi bất cứ điều gì bạn phải *chọn* để viết được "Then" mà nguồn và yêu cầu chưa nói. Cột này **phải trống (`—`) trước khi bàn giao**: mỗi dòng có nội dung phải được xử lý theo §3.3 (bỏ điều nguồn chưa nói khỏi yêu cầu; chỉ khi là mơ hồ của câu nguồn đã nói thì hỏi theo §8.3). Không tự chọn một cách đọc rồi ghi `—`.
- Mọi yêu cầu cấp dưới có ít nhất một ca. `check_sr.py --tests` kiểm TST-01…05.

### 11.3 Bộ ca bắt buộc theo dạng yêu cầu

| Yêu cầu có | Ca bắt buộc (mỗi ca một hàng) |
|---|---|
| Giới hạn số lượng (tối thiểu/tối đa) | Đúng cận dưới, đúng cận trên, vượt cận trên một đơn vị; dưới cận dưới nếu có nghĩa |
| Độ dài hoặc định dạng | Rỗng, đúng giới hạn, vượt một ký tự, ký tự đặc biệt/khoảng trắng, chữ hoa–thường |
| Cửa sổ thời gian hoặc hết hạn | Sự kiện trong cửa sổ, sát ranh giới, ngoài cửa sổ; **thực thể cũ có hoạt động mới**; **thực thể mới chưa có hoạt động**. Với cửa sổ liên tục (ví dụ "7 ngày gần nhất" = 168 giờ), dùng ranh giới ±1 phút (trong cửa sổ: 167 giờ 59 phút; ngoài: 168 giờ 1 phút) và chỉ thêm ca "đúng ranh giới" khi nguồn nói rõ đầu mút có gồm hay không |
| Công thức hoặc điểm số | **Ví dụ số tính tay** với ít nhất hai thực thể, gồm một thực thể "ngoài lề" (cũ, trống, bị ẩn); ghi kết quả bằng số. Mỗi hằng số trong công thức (ví dụ "1 +") phải giải thích được thuộc về cái gì |
| Quyền theo vai trò | Mỗi vai trò liên quan: được làm; bị từ chối |
| Chuyển trạng thái | Chuyển hợp lệ; thử từ trạng thái không cho phép |
| Nhánh lỗi hoặc ngoại lệ | Mỗi nhánh một ca, kể cả "có chặn hay không chặn thao tác chính" |
| Hành động lặp hoặc trùng | Lần thứ hai cùng thao tác, cùng giá trị |
| Số đếm hoặc hiển thị số | Khi 0, 1 và nhiều |

### 11.4 Cách dùng trong quy trình

- **Author** viết `tests-Mxx.md` sau mỗi tính năng (vòng viết, bước 5 của `sr-author`) và xử lý mọi "Giả định cần thêm" trước khi chuyển tính năng kế tiếp. Với mục nguồn có giới hạn, công thức, cửa sổ thời gian hoặc quy tắc sắp xếp, Author viết **ca nháp ngay ở Bước 2** (lập hàng đợi) để chỗ không tính ra một kết quả duy nhất được hỏi **một lần, trọn quy tắc** (§8.3) thay vì lộ ra ở cuối.
- **Auditor lượt P3** dựng ca kiểm của mình **từ nguồn** (không từ SR, không từ ca kiểm của Author) cho mọi mục OWNED rồi mới đối chiếu: với mỗi ca ghi "Nguồn xác định kết quả?" ∈ {Có, Mơ hồ, Không}, "SR xác định kết quả?" ∈ {Có, Mơ hồ, Không}; sau cùng mở `tests-Mxx.md` của Author và so từng "Then".
- Cùng lúc dựng ca kiểm, Auditor quét bảy câu hỏi §4.7 cho từng tính năng **từ nguồn** để chấm CL-B13.
- Phân loại: nguồn **Mơ hồ** → GAP (CL-A11). Nguồn xác định mà SR không → DEFECT (CL-B08). Nguồn và SR xác định nhưng "Then" của Author khác → DEFECT (CL-A05) hoặc CL-C01 tùy nguyên nhân. Thiếu nhánh vi phạm → DEFECT (CL-B09). `tests-Mxx.md` thiếu hoặc sơ sài → CL-B12.
