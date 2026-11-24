# Bước 7 — Hi-fi theo đợt

[Vietnamese Doc]

## Mục đích

Vẽ toàn bộ màn hình thật, **từng đợt** (A–E theo `screen-inventory.md`), mỗi màn hình đủ trạng thái và thiết bị, chỉ
dùng tokens và component đã chốt. Đợt nào được duyệt thì đẩy sang Figma làm bản lưu.

Chế độ: **thực thi** (`input/CONVENTIONS.md` mục 5). Đọc lại `input/ANTI-PATTERNS.md`, `input/QUALITY-FLOOR.md` và
README của "iShare Design System" ở đầu mỗi phiên.

Mỗi lượt làm **một đợt** rồi dừng ở cổng. Đợt chưa duyệt thì không sang đợt sau.

## Đầu vào

- `screen-inventory.md` (màn hình, trạng thái, thiết bị của đợt), `flows.md`, wireframe bước 5.
- `tokens/tokens.json`, "iShare Design System", `DESIGN.md` (mục 3–7).
- FR/SC/DB của các module trong đợt: nội dung, giới hạn, thông điệp, trường dữ liệu.
- Q7-01 (dữ liệu mẫu thật), Q7-02 (lưu ý của đợt).

## Việc làm (cho một đợt)

1. **Chuẩn bị:** liệt kê màn hình × trạng thái × thiết bị của đợt (số artboard). Đọc phần FR/SC/DB liên quan từng
   màn hình: phần tử, thông điệp lỗi đúng chữ của SC, giới hạn hiển thị. Hỏi Q7-02 nếu cần.
2. **Canvas:** dùng canvas **"iShare — Giao diện"** (tạo ở đợt đầu, link vào `DESIGN.md` `canvas_giao_dien`), một
   trang mỗi đợt ("Đợt A — Đọc và viết"…). **Cài "iShare Design System"** vào canvas theo hướng dẫn của type Design, để
   artboard dùng tokens và component thật, không tự vẽ lại. Bản sao: `.agents/.claude/design/canvas/giao-dien/`.
3. **Vẽ artboard** theo tên `<SCR-id>--<state>--<device>.dc.html` (`CONVENTIONS.md` mục 3):
   - Bố cục theo wireframe đã duyệt; thay đổi bố cục so với wireframe thì nói ở cổng.
   - Nội dung: dữ liệu mẫu của `DESIGN.md` mục 7 và SC; thông điệp hệ thống đúng nguồn, giọng văn theo `PRODUCT.md`.
   - Trạng thái: vẽ trọn màn hình cho trạng thái chính; trạng thái chỉ khác một vùng nhỏ (ví dụ `validation` của một
     ô) được vẽ ở dạng cắt vùng đó, tên artboard giữ đúng quy ước.
   - Phần tử tương tác thật (`button`, `a`, `input` + `label`); icon từ bộ đã chọn; không emoji.
   - Cần giá trị thị giác chưa có token, hoặc component chưa có → **dừng vẽ phần đó**, ghi đề xuất, trình ở cổng
     (không tự thêm).
4. **Kiểm trước khi gửi** từng artboard (trên bản sao cục bộ):
   ```
   python3 $SK/tools/check_ui.py <tệp> --tokens $D/tokens/tokens.json --design $D/DESIGN.md
   ```
   ERROR = 0 thì mới gửi. Cuối đợt chạy cho cả thư mục.
5. **Kiểm đủ:**
   ```
   python3 $SK/tools/check_inventory.py --inventory $D/screen-inventory.md --specs docs/specs --artboards .agents/.claude/design/canvas/giao-dien/project --batch <X>
   ```
   Mọi trạng thái × thiết bị của đợt có artboard.
6. Checklist bằng mắt (`ANTI-PATTERNS.md` mục 9) và các mục QF "Mắt" liên quan tới đợt (focus, vùng bấm, nội dung dài,
   tiếng Việt, trợ giúp nhất quán).
7. Viết `qa/QA-dot-<X>.md` (từ `output/qa-template.md`): kết quả tool, checklist, WARN giữ lại kèm lý do, đề xuất token
   hay component mới, câu hỏi.
8. **Trình cổng** (xem dưới). Người dùng sửa → sửa trên canvas, chạy lại 4–7, trình lại.

### Sau khi đợt được duyệt: đẩy sang Figma

1. Gom việc để tiết kiệm lượt gọi (giới hạn 200 lượt/ngày, 10/phút). Kiểm quyền bằng `whoami` nếu gặp lỗi.
2. Làm theo skill của chính Figma MCP trước khi gọi tool (`figma-use`; `figma-generate-design` cho việc đưa giao diện
   từ HTML/code vào Figma). Gọi `create_session` trước mọi tool làm việc với file.
3. File **"iShare — UI"** trong team vduczz (tạo ở đợt đầu; link vào `DESIGN.md` `figma_file`), một page mỗi đợt, tên
   frame trùng tên artboard (bỏ `.dc.html`).
4. Đợt đầu tiên: sau khi đẩy, hỏi người dùng (Q7-03) bản trên Figma có giữ đủ chất lượng không (chữ, khoảng cách,
   layer sửa được). Kém → ghi `DD-UI` về cách xử lý (ví dụ chỉ đẩy ảnh chụp kèm link canvas) trước khi làm đợt sau.
5. Ghi đợt vào `dot_da_duyet` và `dot_da_day_figma` trong frontmatter `DESIGN.md`.

## Đầu ra

- Canvas "iShare — Giao diện", trang của đợt; bản sao trong `canvas/giao-dien/`.
- `qa/QA-dot-<X>.md`.
- Page của đợt trong file Figma "iShare — UI".
- `DESIGN.md`: `dot_da_duyet`, `dot_da_day_figma`; mục 5 nếu có DD-UI mới; mục 8 "Đề nghị bổ sung" nếu có.

## Trình ở cổng

```
Bước 7/9 — Hi-fi — Đợt X (<tên>): xong, chờ bạn duyệt.

Kết quả: <số màn hình, số artboard, link trang canvas>
Cần bạn quyết: <thay đổi so với wireframe; đề xuất token/component mới; chỗ nguồn mơ hồ>
Input còn thiếu: <…>
Đã ghi: qa/QA-dot-X.md
Tool: check_ui ERROR=0 WARN=n · check_inventory đủ n/n artboard

Trả lời "ok" để đẩy đợt X sang Figma và làm đợt kế tiếp, hoặc nói chỗ cần sửa.
```

Khi mọi đợt đã duyệt và đẩy Figma: thêm `7` vào `steps_completed`, `buoc_hien_tai: 8`.

## Không làm

- Không dùng giá trị thị giác hay component ngoài design system.
- Không vẽ đợt sau khi đợt trước chưa duyệt.
- Không sửa trên Figma; mọi sửa đổi làm trên canvas rồi đẩy lại.
