# Bước 9 — Bàn giao (`handoff/`)

[Vietnamese Doc]

## Mục đích

Chuẩn bị mọi thứ để phase Coding hiện thực giao diện bằng React (Vite) và xây UI Kit nội bộ **mà không phải đoán**:
tokens dùng được ngay, đặc tả component, bảng màn hình → đường dẫn trang, file Figma bản cuối.

## Đầu vào

- Mọi kết quả bước 1–8 đã duyệt; `qa/QA-final.md` đã chốt.
- Q9-01 (repo frontend, Tailwind), Q9-02 (quy ước tên component).

## Việc làm

1. **Tokens:** chạy lại `export_tokens.py` để `tokens.css` và `tokens.dtcg.json` khớp `tokens.json` cuối. Ghi trong
   `UI-KIT.md` cách dùng: import `tokens.css` sau Tailwind (`@import "tailwindcss";` rồi tokens), lớp tiện ích sinh
   từ token (`bg-surface`, `text-ink`, `rounded-md`, `p-4`…), theme phụ bằng `data-theme`. Nếu repo không dùng
   Tailwind: các biến CSS trong `tokens.css` vẫn dùng trực tiếp được.
2. **`handoff/UI-KIT.md`** (từ `output/ui-kit-template.md`) cho mỗi component trong design system:
   - mục đích, khi dùng/không dùng; biến thể và thuộc tính (props) đề xuất; trạng thái; token sử dụng; yêu cầu a11y
     (vai trò, nhãn, bàn phím, focus); màn hình dùng nó (`SCR-*`).
   - Ghi chú nền tảng (đề xuất cho phase Coding, người dùng quyết ở phase đó): dùng thành phần "headless" có a11y sẵn
     (ví dụ Base UI hoặc React Aria) rồi tự áp tokens; nếu dùng shadcn CLI để sinh khung thì xóa toàn bộ màu, bo góc
     mặc định ngay từ đầu; KaTeX cho công thức; Tiptap cho editor với thanh công cụ đúng định dạng FR cho phép.
3. **`handoff/routes.md`:** bảng `SCR-*` → đường dẫn trang (từ `flows.md`) → vai trò truy cập → component chính →
   link artboard (desktop/mobile) → frame Figma.
4. **Figma:** kiểm mọi đợt đã có trong "iShare — UI" và khớp bản cuối trên canvas (theo `dot_da_day_figma`). Code
   Connect để sang phase Coding khi đã có component React.
5. **Chuyển bản chốt:** sau khi người dùng nói "Nghiệm thu", chép `output/` (trừ `canvas/`) sang `docs/specs/design/`,
   đặt `trang_thai: Đã chốt`, `phien_ban: 1.0` cho `DESIGN.md`, `PRODUCT.md`, `screen-inventory.md`, `flows.md`,
   `UI-KIT.md`.
6. Đề xuất cập nhật bảng skill/phase trong `.agent-instructions/README.md` (phase Design) nếu người dùng muốn; không
   tự sửa.

## Đầu ra

- `handoff/UI-KIT.md`, `handoff/routes.md`; `tokens/tokens.css`, `tokens/tokens.dtcg.json` bản cuối.
- Sau nghiệm thu: `docs/specs/design/` (bản chốt).

## Trình ở cổng

- Danh sách tệp bàn giao và vị trí; số component đã đặc tả; số màn hình có route; link Figma.
- Câu cuối: `Trả lời "Nghiệm thu" để chuyển tài liệu sang docs/specs/design/, hoặc nói chỗ cần sửa.`

Sau khi người dùng nói "Nghiệm thu": thêm `9` vào `steps_completed`, thực hiện việc 5.

## Không làm

- Không viết code React của ứng dụng; không tạo repo frontend.
- Không chọn thay người dùng thư viện component cho phase Coding (chỉ đề xuất).
