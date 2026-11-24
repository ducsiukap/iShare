# Skill: designing-ui

[Vietnamese Doc]

Skill này giúp agent **dẫn dắt việc thiết kế giao diện** cho iShare, từ các tài liệu phân tích đã có (FR, use case,
scenario, mô hình dữ liệu) tới bộ màn hình hoàn chỉnh và bàn giao cho frontend React. Agent là người điều khiển: nói
bạn cần đưa gì và lúc nào, đề xuất phương án có lý do, vẽ, tự kiểm, rồi dừng chờ bạn duyệt ở mỗi bước.

Mục tiêu đặc biệt: giao diện **không mang dáng "AI-generated"** (font Inter, gradient tím, ba card có icon, bo góc và
bóng giống hệt nhau, câu chữ sáo rỗng…). Skill làm được điều đó bằng quy trình: brief → reference thật → chọn hướng
thẩm mỹ trên một màn hình mẫu → khóa tokens → mới vẽ hàng loạt → kiểm bằng tool và bằng mắt.

## Công cụ

| Công cụ | Vai trò |
|---|---|
| Claude Design (canvas) | Nơi vẽ: thử hướng thẩm mỹ, wireframe, màn hình hi-fi. Đây là **bản gốc** của màn hình |
| Claude Design (Design System) | "iShare Design System": tokens, brand book, component |
| Figma (team vduczz, Education) | **Bản lưu** của các đợt đã duyệt, để cô giáo và thầy hướng dẫn xem, comment; sau này nối component với code |
| Tool Python trong `tools/` | Kiểm anti-pattern, tương phản màu, danh mục màn hình; xuất tokens cho Tailwind |

Sửa màn hình luôn sửa trên Claude Design rồi đẩy lại Figma, không sửa trực tiếp trên Figma.

## Chín bước

| Bước | Agent làm | Bạn chuẩn bị / duyệt |
|---|---|---|
| 1. Brief | Đọc FR/US/SC, viết `PRODUCT.md`: người dùng, bối cảnh, việc chính, ràng buộc, giọng văn | Logo/màu có sẵn, mong muốn của cô giáo, 3 từ muốn và 3 từ không muốn, thiết bị chính, dark mode, xưng hô |
| 2. Reference | Lập moodboard: mỗi reference ghi mượn gì, vì sao, không mượn gì | 3–5 app thích, 3 app ghét kèm lý do; ảnh app học tập học sinh đang dùng |
| 3. Hướng thẩm mỹ | 2–3 hướng khác hẳn nhau, vẽ trên cùng màn hình mẫu "Chi tiết bài viết" (desktop; thêm mobile, bản tối nếu brief có) | Chọn một hướng hoặc trộn |
| 4. Danh mục màn hình | Liệt kê mọi màn hình của 16 module, truy vết FR/UC/SC, trạng thái cần vẽ, chia đợt | Phạm vi, chia đợt |
| 5. Luồng và wireframe | Sơ đồ trang, điều hướng, khung xám cho các luồng chính | Luồng, điều hướng |
| 6. Design system | Tokens (màu, chữ, khoảng cách, bo góc, bóng), test font tiếng Việt, component lõi | Font, màu, mật độ, bo góc, bộ icon |
| 7. Hi-fi theo đợt | Vẽ từng đợt (A–E), đủ trạng thái, chỉ dùng tokens; đẩy đợt đã duyệt sang Figma | Duyệt từng đợt; dữ liệu mẫu thật nếu có |
| 8. Kiểm tra | Chạy tool trên toàn bộ, rà WCAG 2.2 AA, trạng thái, nhất quán, brand test; báo cáo lỗi | Duyệt danh sách sửa; nói "Chốt thiết kế" |
| 9. Bàn giao | `tokens.css` cho Tailwind v4, đặc tả UI Kit, bảng màn hình → route, Figma bản cuối | Nói "Nghiệm thu" |

Từ bước 6 agent chuyển sang **chế độ thực thi**: chỉ dùng tokens và component đã chốt, không tự thêm màu, cỡ chữ,
khoảng cách mới. Cần thêm thì agent đề xuất ở cổng.

## Dùng skill

Bắt đầu:

```
Dùng skill designing-ui. Làm bước 1 rồi dừng ở cổng.
```

Tiếp tục ở phiên mới (agent đọc trạng thái trong `DESIGN.md`):

```
Dùng skill designing-ui, làm tiếp.
```

Ở bước 7, mỗi lượt là một đợt:

```
Dùng skill designing-ui, vẽ đợt B.
```

Trả lời ở cổng: `ok` để sang bước sau, hoặc nói chỗ cần sửa. Câu trả lời mơ hồ hay câu hỏi ngược lại không được tính
là đồng ý.

## Kết quả nằm ở đâu

| | Đường dẫn |
|---|---|
| Tài liệu thiết kế (bản làm việc) | `.agents/.claude/design/output/` (`PRODUCT.md`, `DESIGN.md`, `moodboard.md`, `screen-inventory.md`, `flows.md`, `tokens/`, `qa/`, `handoff/`) |
| Bản sao canvas Claude Design | `.agents/.claude/design/canvas/` |
| Bản đã nghiệm thu | `docs/specs/design/` |
| Màn hình | Canvas "iShare — Khám phá", "iShare — Giao diện"; design system "iShare Design System"; file Figma "iShare — UI" (link ghi trong frontmatter của `DESIGN.md`) |

## Tool

Chạy từ gốc repo, chỉ cần Python 3. Xem bảng lệnh trong [SKILL.md](SKILL.md#tool). Tự thử tool với dữ liệu mẫu:

```
python3 .agent-instructions/skills/designing-ui/tools/check_ui.py .agent-instructions/skills/designing-ui/tools/fixtures/slop.dc.html
python3 .agent-instructions/skills/designing-ui/tools/check_ui.py .agent-instructions/skills/designing-ui/tools/fixtures/clean.dc.html --tokens .agent-instructions/skills/designing-ui/tools/fixtures/tokens.sample.json
```

Tệp đầu phải báo nhiều ERROR, tệp sau phải sạch.

## Cấu trúc skill

```
designing-ui/
├── SKILL.md          ← hướng dẫn chính cho agent
├── README.md         ← tệp này (cho người dùng)
├── input/            ← INPUTS, CONVENTIONS, ANTI-PATTERNS, QUALITY-FLOOR, QUESTIONS
├── steps/            ← 01-brief … 09-handoff
├── output/           ← template của các tài liệu đầu ra
└── tools/            ← check_ui, contrast, check_inventory, export_tokens, font_test (+ fixtures)
```

## Nguồn tham khảo

Phương pháp tổng hợp và diễn đạt lại từ các nguồn sau (không chép nguyên văn):

- Anthropic — [Improving frontend design through Skills](https://claude.com/resources/articles/improving-frontend-design-through-skills)
  và skill [`frontend-design`](https://github.com/anthropics/skills) (Apache-2.0): khái niệm *distributional
  convergence*, token plan trước khi vẽ, vòng plan → review → build → critique, danh sách cliché thế hệ mới.
- Paul Bakaus — [Impeccable](https://github.com/pbakaus/impeccable) (Apache-2.0): tách sự thật sản phẩm (PRODUCT.md)
  với hướng thị giác (DESIGN.md), bộ phát hiện anti-pattern tất định.
- OpenAI — các hướng dẫn prompt frontend cho GPT-5.x: tách chế độ khám phá và thực thi, không tự đặt tokens khi đã có
  design system, nội dung thật, "brand test".
- Vercel — [Web Interface Guidelines](https://vercel.com/design/guidelines): chất lượng tương tác, focus, form.
- W3C — [WCAG 2.2](https://www.w3.org/TR/WCAG22/); Design Tokens Community Group — định dạng DTCG 2025.10.
- Donny Trương — [Vietnamese Typography](https://vietnamesetypography.com/): hiển thị dấu tiếng Việt.
