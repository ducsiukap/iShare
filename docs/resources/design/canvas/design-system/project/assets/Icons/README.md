# Icons

Bộ **Material Symbols Sharp** (Google, giấy phép Apache-2.0), gói `@material-symbols/svg-400@0.48.3`; riêng `shift-w600.svg` lấy từ `@material-symbols/svg-600@0.48.3` (DD-UI-28).

- Lưới 24px, `viewBox="0 -960 960 960"`, một màu (tệp không đặt `fill`, nên hiện màu đen khi xem bằng `<img>`). Khi dùng trong giao diện, chèn SVG trực tiếp và tô `fill: currentColor` để icon theo màu chữ (`ink`, `ink-muted`, `primary`…).
- Cỡ dùng: `icon` 24px, `icon-sm` 20px (nút, thanh thao tác, menu), `icon-xs` 16px (nhãn trạng thái, dòng meta).
- Tệp `-fill` là bản tô đặc cho trạng thái đang bật: đã upvote (`shift-fill`), đã lưu (`bookmark-fill`), Ngôi sao tuần (`star-fill`).
- `shift-w600.svg` là icon Upvote nét dày — ngoại lệ duy nhất về độ dày nét, theo DD-UI-11.
- Cần icon mới: lấy từ cùng bộ Sharp weight 400, không trộn bộ khác (AP-42).

| Tệp | Dùng cho |
|---|---|
| `shift` / `shift-fill` / `shift-w600` | Upvote (chưa / đã upvote) |
| `chat_bubble` | Bình luận |
| `reply` | Trả lời |
| `flag` | Báo cáo, Bị gắn cờ |
| `notifications`, `notifications_off` | Thông báo, tắt thông báo |
| `forum` | Tin nhắn (Chat) |
| `search` | Tìm kiếm |
| `group` | Nhóm |
| `attach_file`, `image`, `description`, `upload`, `download` | Tệp đính kèm |
| `function` | Công thức LaTeX |
| `lock` | Khóa (bình luận, nhóm, tài khoản bị khóa) |
| `settings` | Cài đặt |
| `bookmark` / `bookmark-fill` | Lưu / Đã lưu |
| `summarize` | Tóm tắt |
| `home`, `category`, `tag`, `leaderboard` | Điều hướng: Trang chủ, Chủ đề, Tag, Bảng xếp hạng |
| `flag`, `rate_review`, `gavel`, `receipt_long`, `manage_accounts`, `campaign`, `history`, `bar_chart`, `admin_panel_settings`, `shield_person` | Khu kiểm duyệt và quản trị |
| `format_*`, `ink_highlighter`, `checklist`, `code`, `code_blocks`, `table`, `horizontal_rule`, `link`, `ballot`, `alternate_email` | Thanh soạn thảo |
| `check`, `check_circle`, `error`, `warning`, `info`, `schedule`, `block`, `visibility`, `visibility_off` | Trạng thái và phản hồi |
| `add`, `close`, `edit`, `edit_note`, `delete`, `more_horiz`, `content_copy`, `send`, `refresh`, `logout`, `person`, `star`, `workspace_premium`, `keyboard_arrow_down`, `chevron_left`, `chevron_right`, `arrow_back`, `arrow_downward`, `build`, `progress_activity` | Thao tác chung |
