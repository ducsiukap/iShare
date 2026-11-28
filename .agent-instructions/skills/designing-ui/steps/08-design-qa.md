# Bước 8 — Kiểm tra toàn bộ (`qa/QA-final.md`)

[Vietnamese Doc]

## Mục đích

Bắt lỗi **xuyên đợt** trước khi bàn giao: nhất quán giữa 5 đợt, đủ trạng thái, sàn chất lượng, anti-pattern, bản sắc.
Mỗi đợt đã được kiểm riêng ở bước 7; bước này nhìn toàn bộ như một sản phẩm.

## Đầu vào

- Toàn bộ canvas "iShare — Giao diện" (đọc lại tệp từ canvas trước, vì người dùng có thể đã sửa tay; cập nhật bản
  sao trong `canvas/giao-dien/`).
- `tokens/`, "iShare Design System", `screen-inventory.md`, `flows.md`, `qa/QA-dot-*.md`, `DESIGN.md`, `PRODUCT.md`.

## Việc làm

1. **Tool trên toàn bộ:**
   ```
   python3 $SK/tools/check_ui.py .agents/.claude/design/canvas/giao-dien/project --tokens $D/tokens/tokens.json --design $D/DESIGN.md
   python3 $SK/tools/check_inventory.py --inventory $D/screen-inventory.md --specs docs/specs --artboards .agents/.claude/design/canvas/giao-dien/project --require-artboards
   python3 $SK/tools/contrast.py --tokens $D/tokens/tokens.json --pairs $D/tokens/contrast-pairs.csv
   ```
   `check_inventory.py` cũng báo màn hình bị ảnh hưởng nếu FR/US/SC đã đổi so với lúc lập danh mục.
2. **Sàn chất lượng** (`QUALITY-FLOOR.md`): đi từng mục QF có cột "Mắt", ghi đạt / không đạt / không áp dụng theo
   màn hình. Chú ý QF-05 (focus bị header dính che), QF-04 (vùng bấm nút upvote, nút "…"), QF-13/14 (tiếng Việt,
   nội dung dài, công thức), QF-16 (vị trí trợ giúp/khiếu nại).
3. **Nhất quán xuyên đợt:** cùng component trông và hoạt động giống nhau ở mọi đợt; cùng loại thông điệp dùng cùng
   giọng; nhịp khoảng cách; cách hiển thị cùng một trạng thái nghiệp vụ (ví dụ `flagged` ở bài viết, bình luận, hàng
   chờ Mod).
4. **Bản sắc:** brand test trên 5 màn hình chọn ngẫu nhiên từ các đợt khác nhau; checklist `ANTI-PATTERNS.md` mục 9
   trên toàn bộ.
5. **Đối chiếu nguồn:** chọn mẫu ít nhất 2 màn hình mỗi module, so phần tử và thông điệp với FR/SC; không có phần tử
   ngoài nguồn.
6. Viết `qa/QA-final.md` (từ `output/qa-template.md`): bảng lỗi `QA-F-nn` gồm màn hình, loại (AP, QF, Nhất quán, Nguồn,
   Nội dung), mô tả, đề xuất sửa, mức (**Phải sửa** / **Nên sửa**).
7. Tùy chọn, chỉ khi người dùng muốn: chụp màn hình các artboard ở các bề rộng 390/768/1440 bằng trình duyệt để xem
   thực tế; hoặc nhờ một agent khác chưa từng vẽ đọc toàn bộ và phản biện. Hỏi trước, không tự làm.
8. **Trình cổng lần 1** (danh sách lỗi). Người dùng duyệt danh sách → sửa trên canvas → chạy lại bước 1 → cập nhật
   `QA-final.md` (cột "Đã sửa") → đẩy lại Figma các artboard đã sửa → **trình cổng lần 2** để chốt.

## Đầu ra

- `qa/QA-final.md`.
- Canvas, bản sao và Figma đã cập nhật theo các lỗi đã sửa.

## Trình ở cổng

- Lần 1: tổng số lỗi theo loại và mức; 5–10 lỗi quan trọng nhất; đề xuất sửa; kết quả tool.
- Lần 2: lỗi đã sửa, lỗi để lại (và lý do), kết quả tool sau sửa. Câu cuối:
  `Trả lời "Chốt thiết kế" để chốt, hoặc nói chỗ cần sửa.`

Sau khi người dùng nói "Chốt thiết kế": thêm `8` vào `steps_completed`, `buoc_hien_tai: 9`.

## Không làm

- Không tự sửa lỗi "Nên sửa" khi người dùng chưa duyệt danh sách.
- Không thêm tính năng khi sửa lỗi.
