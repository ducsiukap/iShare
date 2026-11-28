---
ma_tai_lieu: UI-KIT
phien_ban: 0.1
trang_thai: Bản nháp
ngay: YYYY-MM-DD
tac_gia: Phạm Văn Đức
---
# Đặc tả UI Kit — iShare

[Vietnamese Doc] — Bàn giao cho phase Coding. Tên component, props, token viết tiếng Anh.

## 1. Dùng tokens

- Nguồn: `tokens/tokens.json` (không sửa `tokens.css`, `tokens.dtcg.json` bằng tay; sinh lại bằng `export_tokens.py`).
- Tailwind v4: trong CSS gốc của app, `@import "tailwindcss";` rồi import `tokens.css`. Lớp tiện ích sinh từ token:
  <ví dụ: `bg-surface`, `text-ink`, `border-line`, `rounded-md`, `p-4`, `text-body`, `font-body`, `shadow-1`>.
- Theme phụ (nếu có): đặt `data-theme="<id>"` trên `<html>`.
- Không Tailwind: dùng trực tiếp biến CSS (`var(--color-ink)`…).
- Font: <cách tải; chỉ các độ đậm cần dùng>.

## 2. Đề xuất nền tảng (người dùng quyết ở phase Coding)

| Việc | Đề xuất | Lý do | Lưu ý chống "dáng mặc định" |
|---|---|---|---|
| Thành phần có a11y sẵn | <Base UI / React Aria> | | Không giữ màu, bo góc mặc định của bất kỳ thư viện nào |
| Công thức | KaTeX | Theo FR | Cỡ chữ công thức theo token `body` |
| Editor | Tiptap | Theo FR | Thanh công cụ đúng định dạng FR cho phép |

## 3. Component

### <TênComponent>

- **Mục đích:** <…> · **Dùng khi / không dùng khi:** <…>
- **Props đề xuất:**

  | Prop | Kiểu | Mặc định | Ghi chú |
  |---|---|---|---|

- **Biến thể:** <…> · **Trạng thái:** mặc định, hover, focus-visible, active, disabled, đang xử lý, <nghiệp vụ>
- **Token:** <…>
- **A11y:** <vai trò, nhãn, bàn phím, focus>
- **Dùng ở:** <SCR-…> · **Preview:** <link design system> · **Figma:** <frame>
