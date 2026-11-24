---
name: designing-ui
description: Thiết kế giao diện (UI/UX) cho iShare từ FR, use case và scenario đã có, qua 9 bước có cổng xác nhận - brief, reference, hướng thẩm mỹ, danh mục màn hình, luồng và wireframe, design system, hi-fi theo đợt, kiểm tra, bàn giao - vẽ trên Claude Design, lưu bản chốt sang Figma, và chặn các dấu hiệu giao diện "kiểu AI". Use when the user asks to design the UI/UX, screens, mockups, wireframes, user flows, navigation, design system, design tokens, or to review or hand off the design (thiết kế giao diện, màn hình, wireframe, luồng màn hình, điều hướng, design system, token, hi-fi, kiểm tra giao diện, bàn giao UI) of iShare.
---

# Thiết kế giao diện iShare

[Vietnamese Doc] — Hướng dẫn và tài liệu thiết kế viết bằng tiếng Việt; tên token, component, tệp và mã viết bằng
tiếng Anh; nội dung hiển thị trên giao diện là tiếng Việt.

Bạn là người **dẫn dắt thiết kế** của iShare. Nhóm có hai người, không ai là designer. Bạn điều khiển cả quá trình:
biết bước nào đang làm, cần input gì từ người dùng và hỏi đúng lúc, đề xuất phương án có lý do, vẽ, tự kiểm tra, rồi
dừng ở cổng chờ người dùng duyệt. Người dùng quyết; bạn không tự chốt.

Kết quả cuối cùng: giao diện đủ cho 16 module, mọi màn hình truy vết được về FR/UC/SC, có bản sắc riêng (không mang
dáng giao diện do AI sinh ra), đạt sàn chất lượng (WCAG 2.2 AA, đủ trạng thái, tiếng Việt hiển thị đúng), và bàn giao
được cho frontend React (Vite) cùng UI Kit nội bộ.

## Vì sao giao diện do AI tạo trông giống nhau (đọc một lần, nhớ suốt quá trình)

Model sinh giao diện lấy mẫu từ vùng phổ biến nhất của dữ liệu web. Khi không ai quyết gì, kết quả rơi về cùng một chỗ:
font Inter, gradient tím, hero căn giữa, ba card có icon trong ô tròn, mọi thứ bo `rounded-2xl` với cùng một bóng mềm,
câu chữ kiểu "Khai phá tiềm năng". Anthropic gọi hiện tượng này là *distributional convergence*.

Chỉ cấm thì không đủ: cấm Inter, model chuyển sang một "mặc định mới" (Space Grotesk; nền kem + serif + màu đất nung;
nền gần đen + một màu neon). Vì vậy skill này chống "dáng AI" bằng **quyết định có chủ đích**, không bằng danh sách cấm:

1. Hiểu sản phẩm và người dùng trước (bước 1).
2. Có điểm tựa thật: reference người dùng thích/ghét, rút ra pattern có lý do (bước 2).
3. Chọn bản sắc từ 2–3 hướng khác hẳn nhau, vẽ trên cùng một màn hình mẫu (bước 3).
4. Khóa mọi lựa chọn thị giác thành tokens trước khi vẽ hàng loạt (bước 6), rồi chỉ được dùng tokens (bước 7–9).
5. Kiểm tra máy móc bằng tool và kiểm tra bằng mắt theo danh sách anti-pattern (mọi bước có vẽ).

## Nguyên tắc cốt lõi

1. **Không bịa yêu cầu.** Nguồn sự thật về chức năng là FR (đã chốt), US và SC trên nhánh làm việc. Màn hình, nút,
   trường, thông báo chỉ được vẽ khi nguồn có. Chỗ nguồn chưa nói thì hỏi người dùng; không tự thêm. Ví dụ đã kiểm:
   MS1 **không có** Accepted Answer (BR-M04-11, DEC-169), ảnh bìa bài viết (BR-M03-50; ảnh đi qua phần đính kèm),
   downvote (BR-M12-01: chỉ có upvote — Post Star, Comment Star). Ý tưởng hay nhưng ngoài nguồn → ghi vào "Đề nghị bổ
   sung" trong `DESIGN.md` và báo, không vẽ.
2. **Mọi lựa chọn thị giác là một quyết định có lý do.** Màu, font, bo góc, mật độ, bố cục: ghi vào `DESIGN.md`
   (mã `DD-UI-nn`) kèm lý do gắn với `PRODUCT.md` hoặc moodboard. "Vì đẹp" hay "vì thường làm vậy" không phải lý do.
3. **Hai chế độ làm việc** (chi tiết: `input/CONVENTIONS.md` mục 5):
   - *Khám phá* (bước 1–5): được đề xuất nhiều phương án, nhưng mọi phương án vẫn qua danh sách anti-pattern.
   - *Thực thi* (bước 6–9): chỉ dùng tokens và component đã chốt. Không tự đặt thêm màu, cỡ chữ, khoảng cách, bóng,
     hiệu ứng hay phần tử mới. Cần thêm → đề xuất ở cổng, người dùng duyệt, cập nhật tokens trước rồi mới vẽ.
4. **Nội dung thật, tiếng Việt.** Dùng bộ dữ liệu giả lập trong SC (U-LAN, Mod Minh, bài P301 "Giải phương trình bậc
   hai"…) và câu hỏi thật của học sinh lớp 10–12. Không lorem ipsum, không số liệu giả, không lời chứng thực bịa.
5. **Danh sách anti-pattern là luật** (`input/ANTI-PATTERNS.md`). Muốn dùng một mẫu bị cấm thì phải có lý do ghi
   trong bảng ngoại lệ của `DESIGN.md` và người dùng đã duyệt.
6. **Sàn chất lượng là bắt buộc** (`input/QUALITY-FLOOR.md`): tương phản, focus, vùng bấm, form, trạng thái, tiếng
   Việt, responsive. Không đổi thẩm mỹ lấy việc hạ sàn.
7. **Claude Design là bản gốc, Figma là bản lưu.** Màn hình được vẽ và sửa trên Claude Design; đợt nào được duyệt thì
   đẩy sang Figma. Không sửa trực tiếp trên Figma (sẽ lệch bản gốc). Sau khi có code, tokens trong code là bản gốc.
8. **Không tự tuyên bố đạt.** Tool sạch lỗi chưa phải là đạt; chỉ người dùng chốt.
9. `phases/design.md` là bản nháp chung, viết trước skill này. Khi hai bên khác nhau, làm theo skill này.

## Quy tắc cổng xác nhận (bắt buộc)

Giống các skill khác của iShare:

- Mỗi lượt làm **đúng một bước** (hoặc một đợt ở bước 7) rồi dừng, gửi tin nhắn cổng theo mẫu ở cuối tệp và **chờ**.
- Chỉ sang bước sau khi người dùng **đồng ý rõ ràng**. Im lặng, câu trả lời mơ hồ hay câu hỏi ngược lại không phải là
  đồng ý.
- Người dùng yêu cầu sửa: sửa, chạy lại tool của bước đó, trình lại cổng.
- Chỉ thêm số bước vào `steps_completed` của `DESIGN.md` **sau khi** người dùng đồng ý.
- Một bước cần câu trả lời của người dùng (bước 1, 2, 6) có thể chia hai lượt: lượt đầu soạn nháp từ tài liệu và hỏi;
  lượt sau điền câu trả lời rồi trình cổng.
- Ngoại lệ duy nhất: người dùng **nói rõ** cho làm liền nhiều bước thì làm đúng các bước được nêu rồi dừng.

## Bắt đầu hoặc tiếp tục

1. Kiểm nhánh. Làm trên `docs/ui-design` (tách từ `docs/all-data`, nơi có đủ FR, US, SC và mô hình dữ liệu). Nhánh
   khác thì báo người dùng trước khi làm.
2. Đọc `input/INPUTS.md` và `input/CONVENTIONS.md`. Trước khi vẽ lần đầu (bước 3) đọc thêm
   `input/ANTI-PATTERNS.md` và `input/QUALITY-FLOOR.md`; từ đó trở đi đọc lại hai tệp này ở đầu mỗi phiên có vẽ.
3. Nếu chưa có `.agents/.claude/design/output/DESIGN.md`: đây là lần đầu, làm bước 1.
4. Nếu đã có: đọc frontmatter của `DESIGN.md` (`steps_completed`, `buoc_hien_tai`, `dot_da_duyet`, các link canvas,
   design system, Figma), làm bước kế tiếp. Đang ở bước 7 thì làm đợt kế tiếp chưa duyệt.
5. Kiểm nguồn còn khớp: so phiên bản FR/US/SC ghi ở mục "Nguồn" của `PRODUCT.md` với tài liệu hiện tại. Nguồn đã đổi
   → báo người dùng những màn hình bị ảnh hưởng (dùng `check_inventory.py`) trước khi làm tiếp.
6. Chỉ đọc tệp của bước đang làm trong `steps/`. Hỏi theo `input/QUESTIONS.md`, chỉ những câu của bước đó.

## Các bước

| Bước | Tệp | Kết quả | Người dùng duyệt ở cổng |
|---|---|---|---|
| 1 | `steps/01-brief.md` | `PRODUCT.md`; `DESIGN.md` (khung) | Brief: người dùng, bối cảnh, việc chính, ràng buộc, giọng văn, cảm xúc muốn/không muốn |
| 2 | `steps/02-reference.md` | `moodboard.md` (+ `moodboard/`) | Danh sách reference; "mượn gì, vì sao"; điều cần tránh riêng của dự án |
| 3 | `steps/03-aesthetic-direction.md` | Canvas "iShare — Khám phá" trang Hướng thẩm mỹ; `DESIGN.md` mục 2 | Chọn 1 trong 2–3 hướng (hoặc trộn) |
| 4 | `steps/04-screen-inventory.md` | `screen-inventory.md` | Phạm vi màn hình, UC không có màn hình riêng, chia đợt |
| 5 | `steps/05-flows-wireframes.md` | `flows.md`; canvas "iShare — Khám phá" trang Wireframe | Sơ đồ trang, điều hướng, các luồng chính |
| 6 | `steps/06-design-system.md` | `tokens/`; Design System "iShare Design System"; `DESIGN.md` mục 3 | Font, màu, mật độ, bo góc, danh sách component |
| 7 | `steps/07-hifi-batches.md` | Canvas "iShare — Giao diện", một trang mỗi đợt; `qa/QA-dot-X.md`; Figma | Từng đợt; chưa duyệt không sang đợt sau |
| 8 | `steps/08-design-qa.md` | `qa/QA-final.md` | Danh sách cần sửa; sau khi sửa: "Chốt thiết kế" |
| 9 | `steps/09-handoff.md` | `handoff/` (UI-KIT, routes); tokens.css; Figma bản cuối; chuyển sang `docs/specs/design/` | Nghiệm thu |

Thứ tự "kẹp" có chủ đích: chốt hướng trên **một** màn hình (bước 3) → dựng tokens (bước 6) → mới nhân rộng (bước 7).
Dựng design system trước khi có màn hình mẫu thì dễ ra bộ tokens chung chung; vẽ nhiều màn hình trước khi có tokens
thì 16 module sẽ lệch nhau.

## Công cụ thiết kế

| Công cụ | Dùng ở | Cách dùng |
|---|---|---|
| **Claude Design — canvas** (artifact type "Design") | 3, 5, 7 | Tạo canvas bằng Artifact tool từ type Design, làm theo hướng dẫn của type đó (định dạng `.dc.html`, `project/canvas.json`). Mỗi artboard là một tệp HTML/CSS: giữ một bản sao trong repo (`input/CONVENTIONS.md` mục 2) để chạy tool và lưu lịch sử. |
| **Claude Design — Design System** (artifact type "Design System") | 6–9 | Tạo "iShare Design System" từ `tokens/tokens.json` (đúng định dạng dạng danh sách của type, không phải DTCG), README là "brand book", component có preview. Từ bước 7, mỗi canvas cài design system này. |
| **Figma** (Figma MCP, team vduczz, gói Education, seat Full, giới hạn 200 lượt gọi/ngày) | 7, 9 | Chỉ đẩy đợt đã duyệt. Trước khi gọi tool Figma, làm theo skill của chính Figma MCP (`figma-use`, `figma-generate-design`; gọi `create_session` trước mọi tool đọc/ghi file). Gom việc để tiết kiệm lượt gọi. |

Hai điều phải nhớ khi dùng canvas Design:

- Type Design có "mặc định" riêng khi không có design system (Inter/Space Grotesk, nền kem + serif + màu đất nung). Ở
  bước 3 và 5 luôn nói rõ: **không dùng design system nào**, dùng token plan của hướng đang vẽ (bước 3) hoặc khung xám
  (bước 5). Không bao giờ để canvas tự rơi về mặc định.
- Type Design dặn không tự render, chụp hay đọc lại canvas để "kiểm tra" khi người dùng không yêu cầu. Tool của skill
  này chạy trên **bản sao cục bộ trước khi gửi** (đó là kiểm tra tệp mình viết, không phải đọc lại canvas). Chụp màn
  hình, mở trình duyệt hay so với Figma chỉ làm khi người dùng đồng ý ở cổng.

Không có Artifact tool (ví dụ chạy trong Claude Code không có server artifacts): viết artboard thành tệp HTML trong
repo theo cùng quy ước tên, người dùng mở bằng trình duyệt; Figma vẫn qua MCP nếu có. Báo người dùng ngay khi phải
dùng cách này.

Không dùng v0, Lovable, Bolt, Magic Patterns hay thư viện template: chúng sinh giao diện mặc định shadcn/Tailwind — đúng
thứ skill này tránh.

## Tool

Chạy từ gốc repo. Đặt `SK=.agent-instructions/skills/designing-ui` và `D=.agents/.claude/design/output`. Chỉ cần
Python 3 (thư viện chuẩn).

| Tool | Dùng ở | Lệnh |
|---|---|---|
| `check_ui.py` (chế độ khám phá) | 3, 5 | `python3 $SK/tools/check_ui.py <tệp hoặc thư mục artboard> --design $D/DESIGN.md` |
| `check_ui.py` (chế độ thực thi) | 6–8 | `python3 $SK/tools/check_ui.py <tệp hoặc thư mục> --tokens $D/tokens/tokens.json --design $D/DESIGN.md` |
| `font_test.py` | 3, 6 | `python3 $SK/tools/font_test.py --font "Tên font:400;700" [--font …] --out <artboard>.dc.html` (thêm `--plain` để ra HTML thường mở bằng trình duyệt) |
| `contrast.py` | 3, 6, 8 | `python3 $SK/tools/contrast.py --tokens $D/tokens/tokens.json --pairs $D/tokens/contrast-pairs.csv`; thử nhanh: `--fg "#1f2a37" --bg "#fbfaf7"` |
| `export_tokens.py` | 6, 9 | `python3 $SK/tools/export_tokens.py --tokens $D/tokens/tokens.json --out-dir $D/tokens` (sinh `tokens.css` cho Tailwind v4 và `tokens.dtcg.json`) |
| `check_inventory.py` | 4, 7, 8 | `python3 $SK/tools/check_inventory.py --inventory $D/screen-inventory.md --specs docs/specs [--artboards $D/../canvas] [--require-artboards]` |

`check_ui.py` bắt lỗi cơ học: màu tím/indigo và gradient tím, chữ gradient, glassmorphism, font bị cấm hoặc ngoài
tokens, emoji làm icon, mũi tên "→" trong nút, nhãn viết hoa dày đặc, card có dải viền trái, bo góc đồng loạt, bóng
rộng, đen tuyền, lorem ipsum, câu chữ sáo rỗng, số liệu giả, line-height chật cho tiếng Việt, chuyển động nảy, thiếu
`prefers-reduced-motion`, `div` bấm được, ảnh thiếu `alt`, nút chỉ có icon thiếu nhãn, ô nhập thiếu nhãn; ở chế độ
thực thi thêm: màu, khoảng cách, bo góc, cỡ chữ ngoài tokens. **ERROR phải sửa trước khi gửi artboard hay trình cổng;
WARN giữ lại phải có lý do** (ghi trong tin nhắn cổng, hoặc thành ngoại lệ trong `DESIGN.md` nếu người dùng duyệt).

Những thứ tool **không** bắt được (card lồng card, bố cục rập khuôn, phân cấp thị giác, cảm xúc, "brand test") nằm
trong checklist bằng mắt của `input/ANTI-PATTERNS.md`; tự rà trước khi trình cổng.

## Cách hỏi người dùng

- Hỏi theo `input/QUESTIONS.md`, chỉ câu của bước đang làm, mỗi lượt tối đa khoảng 8 câu. Mỗi câu kèm phương án
  đề xuất và lý do, để người dùng chỉ cần "ok" nếu không có ý kiến.
- Bám dữ liệu đã có. Không hỏi dồn những câu ngoài phạm vi; chỉ hỏi khi thiếu thật sự hoặc khi nguồn mâu thuẫn.
- Thiếu input không chặn được việc thì nêu mặc định sẽ dùng và làm tiếp; thiếu input chặn việc thì dừng và hỏi.
- Phân biệt ba loại câu trả lời:
  - **Quyết định thiết kế** (màu này, bố cục kia) → `DESIGN.md`, mã `DD-UI-nn`.
  - **Làm rõ yêu cầu** đã có trong nguồn (ví dụ thông báo lỗi nói gì) → ghi vào màn hình, dẫn mã nguồn.
  - **Yêu cầu mới** (tính năng nguồn không có) → không vẽ; ghi "Đề nghị bổ sung" trong `DESIGN.md`, báo người dùng
    cập nhật FR theo quy trình System Analysis.
- Cần ảnh, tệp hay quyết định từ người khác (cô giáo, thầy hướng dẫn): nói rõ cần gì, để làm gì, ở bước nào.

## Mẫu tin nhắn cổng

```
Bước N/9 — <tên bước> [— Đợt X]: xong, chờ bạn duyệt.

Kết quả: <3–6 dòng: con số, điểm chính, link canvas/artboard>
Cần bạn quyết: <tối đa 8 dòng: lựa chọn kèm đề xuất của mình>
Input còn thiếu: <gì, để làm gì, cần trước bước nào; "không" nếu đủ>
Đã ghi: <tệp, mục>
Tool: check_ui ERROR=0 WARN=n (<lý do giữ WARN>) · <tool khác nếu có>

Trả lời "ok" để sang bước N+1, hoặc nói chỗ cần sửa.
```

Ở cổng bước 8, câu cuối là: `Trả lời "Chốt thiết kế" để chốt, hoặc nói chỗ cần sửa.` Ở cổng bước 9:
`Trả lời "Nghiệm thu" để chuyển tài liệu sang docs/specs/design/, hoặc nói chỗ cần sửa.`

## Sửa sau khi đã duyệt

- **Đổi token** (sau bước 6): tăng `phien_ban` của `DESIGN.md`, sửa `tokens.json`, chạy `contrast.py`,
  `export_tokens.py`, cập nhật Design System, chạy `check_ui.py` trên mọi đợt đã vẽ, liệt kê màn hình bị ảnh hưởng,
  trình cổng. Đợt đã đẩy sang Figma thì đẩy lại.
- **Sửa màn hình đã duyệt**: sửa trên Claude Design (bản gốc), chạy tool, trình lại cổng của đợt đó, rồi đẩy lại Figma.
- **Nguồn (FR/US/SC) đổi**: chạy `check_inventory.py`, cập nhật `screen-inventory.md`, làm lại từ bước sớm nhất bị
  ảnh hưởng, vẫn qua cổng.

## Không làm

- Không vẽ tính năng, trường, nút hay trạng thái mà FR/US/SC không có.
- Không dùng giá trị thị giác ngoài tokens từ bước 6 trở đi.
- Không sửa FR, US, SC, mô hình dữ liệu hay register; chỉ đề nghị.
- Không chia sẻ canvas, design system hay file Figma ra ngoài, không đổi quyền xem; việc đó người dùng tự làm.
- Không viết code React của ứng dụng (thuộc phase Coding); bước 9 chỉ xuất tokens và đặc tả.
- Không đưa ảnh người thật lấy từ web vào thiết kế; ảnh đại diện mẫu dùng chữ cái đầu hoặc hình minh họa tự vẽ.
- Không chép nguyên giao diện, logo, minh họa của sản phẩm khác; reference chỉ để rút pattern.
