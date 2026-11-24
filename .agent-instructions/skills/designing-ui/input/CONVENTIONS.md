# Quy ước của skill designing-ui

[Vietnamese Doc]

Tệp này là quy ước chung cho mọi bước. Bước nào cần quy ước nào sẽ dẫn về mục tương ứng ở đây.

## 1. Nhánh và nguồn

- Làm trên nhánh `docs/ui-design`, tách từ `docs/all-data` (= `main` + `docs/use-case` + `docs/scenario` +
  `docs/entity-class-design`).
- Nguồn chức năng: `docs/specs/fr/`, `docs/specs/us/`, `docs/specs/scenarios/`; trường dữ liệu:
  `.agents/.claude/system_analysis/output/data-model/db/`. Chi tiết: `INPUTS.md`.

## 2. Nơi lưu

```
.agents/.claude/design/
├── output/                         ← tài liệu thiết kế (bản làm việc, được commit)
│   ├── PRODUCT.md                  ← bước 1
│   ├── DESIGN.md                   ← trạng thái quy trình + mọi quyết định thiết kế (từ bước 1, bổ sung dần)
│   ├── moodboard.md                ← bước 2
│   ├── moodboard/                  ← ảnh reference người dùng đưa hoặc tự chụp (đặt tên R-nn-<mô-tả>.png)
│   ├── screen-inventory.md         ← bước 4
│   ├── flows.md                    ← bước 5
│   ├── tokens/                     ← bước 6
│   │   ├── tokens.json             ← nguồn sự thật của tokens (định dạng Design System của Claude Design)
│   │   ├── contrast-pairs.csv      ← các cặp chữ/nền phải đạt tương phản
│   │   ├── tokens.css              ← sinh bằng export_tokens.py (không sửa tay)
│   │   └── tokens.dtcg.json        ← sinh bằng export_tokens.py (không sửa tay)
│   ├── qa/                         ← QA-dot-A.md … QA-dot-E.md (bước 7), QA-final.md (bước 8)
│   └── handoff/                    ← UI-KIT.md, routes.md (bước 9)
└── canvas/                         ← bản sao các canvas Claude Design (để chạy tool và lưu lịch sử)
    ├── kham-pha/project/…          ← canvas "iShare — Khám phá" (bước 3, 5)
    ├── giao-dien/project/…         ← canvas "iShare — Giao diện" (bước 7)
    └── design-system/project/…     ← bản sao các tệp của "iShare Design System" (bước 6)
```

- Bản sao canvas giữ đúng đường dẫn trong canvas (`project/canvas.json`, `project/<artboard>.dc.html`). Khi file tool
  của agent ghi thẳng được vào repo thì dùng `canvas/<tên>/` làm thư mục gốc khi gửi lên canvas; khi không (agent chạy
  trên máy khác repo), viết ở thư mục tạm, gửi lên canvas, rồi chép bản đã gửi về `canvas/<tên>/`.
- Người dùng sửa tay trên canvas → lần sau đọc lại tệp từ canvas trước khi sửa, rồi cập nhật bản sao.
- Sau nghiệm thu (bước 9), bản chốt được chép sang `docs/specs/design/` (giữ cấu trúc `output/`, không chép `canvas/`).
- Ảnh và tệp lớn (> 5 MB) không commit; ghi link.

## 3. Mã và tên

| Mã | Dùng cho | Ví dụ |
|---|---|---|
| `SCR-Mxx-nn` | Màn hình của module Mxx | `SCR-M03-02` (Chi tiết bài viết) |
| `SCR-SHARED-nn` | Khung và màn hình dùng chung | `SCR-SHARED-01` (khung ứng dụng: header, điều hướng) |
| `DD-UI-nn` | Quyết định thiết kế trong `DESIGN.md` | `DD-UI-07` (điều hướng dưới trên mobile) |
| `R-nn` | Reference trong `moodboard.md` | `R-04` |
| `AP-xx` | Anti-pattern (`ANTI-PATTERNS.md`); `AP-P-nn` là điều cần tránh riêng của dự án (từ moodboard) | `AP-03`, `AP-P-02` |
| `QF-xx` | Mục sàn chất lượng (`QUALITY-FLOOR.md`) | `QF-04` |
| `QA-<đợt>-nn` | Lỗi trong báo cáo QA | `QA-B-03`, `QA-F-12` (QA-final) |
| Đợt `A`–`E` | Nhóm màn hình vẽ hi-fi ở bước 7 (chốt ở bước 4) | `A` |

**Tên artboard** (tệp `.dc.html`): `<mã màn hình>--<trạng thái>--<thiết bị>[--dark].dc.html`, ví dụ
`SCR-M03-02--default--desktop.dc.html`, `SCR-M03-02--empty--mobile.dc.html`, `SCR-M03-02--default--desktop--dark.dc.html`
(bản theme tối; không ghi gì là theme sáng). Trạng thái lấy từ mục 4; thiết bị là
`desktop` hoặc `mobile`. Artboard không thuộc màn hình nào (hướng thẩm mỹ, font test, wireframe) đặt tên
tên bắt đầu bằng loại (không bắt đầu bằng `SCR-`), ví dụ `huong-1--chi-tiet-bai--desktop.dc.html` (bước 3),
`font-test.dc.html`, `wf--dang-ky--SCR-M01-01--mobile.dc.html` (bước 5: `wf--<luồng>--<mã màn hình>--<thiết bị>`).
Chỉ dùng chữ không dấu, số, `-`, `.`; không khoảng trắng.

**Tên canvas và design system:** "iShare — Khám phá", "iShare — Giao diện", "iShare Design System". File Figma:
"iShare — UI", một page mỗi đợt.

**Kích thước artboard:** màn hình ứng dụng là trang co giãn (PAGE trong type Design): desktop rộng 1440, mobile rộng
390. Desktop bắt buộc cho mọi màn hình; mobile chỉ khi `PRODUCT.md` mục 3 có hỗ trợ điện thoại, cho màn hình mà
`screen-inventory.md` đánh dấu `mobile`. Bản tối (`--dark`) khi `PRODUCT.md` có dark mode, theo phạm vi chốt ở bước 4
(toàn bộ hay màn hình đại diện).

## 4. Từ vựng trạng thái (slug dùng trong `screen-inventory.md` và tên artboard)

| Slug | Nghĩa | Nguồn thường gặp |
|---|---|---|
| `default` | Có dữ liệu bình thường | Luồng chính SC (M1…) |
| `loading` | Đang tải (skeleton, không spinner che toàn trang) | QF-15 |
| `empty` | Chưa có dữ liệu lần đầu | QF-15 |
| `no-result` | Lọc/tìm không ra kết quả | M06, bộ lọc |
| `error` | Lỗi mạng hoặc máy chủ, có cách thử lại | QF-15 |
| `forbidden` | Không có quyền xem/làm | Nhánh E của SC |
| `not-found` | Nội dung không tồn tại hoặc đã bị xóa hẳn | Nhánh E của SC |
| `long` | Nội dung cực dài: tiêu đề tối đa, tên dài, nhiều tag, công thức/bảng rộng | QF-13, QF-14 |
| `validation` | Form có lỗi nhập | Nhánh E của SC |
| `pending` | Chờ duyệt (bài, thành viên nhóm, yêu cầu) | M03, M08, M11 |
| `rejected` | Bị từ chối | M03, M08 |
| `flagged` | Bị AI/hệ thống gắn cờ | M08, M13 |
| `hidden` | Bị ẩn (tự ẩn hoặc Mod ẩn) | M03, M04, M08 |
| `locked` | Bị khóa (bài, bình luận, nhóm) | M03, M08 |
| `deleted` | Đã xóa mềm / tombstone | M03, M04 |
| `warned` | Tài khoản đang bị cảnh cáo | M08 |
| `banned` | Tài khoản bị ban / màn hình khóa | M01, M08, M09 |
| `maintenance` | Hệ thống bảo trì | M10 |
| `anonymous` | Hiển thị ẩn danh | M11 |
| `owner` / `visitor` | Cùng màn hình nhìn từ chủ sở hữu / người khác | M02 |
| `guest` | Người chưa đăng nhập | ACT-001 |
| `mod` / `admin` | Cùng màn hình nhìn từ Mod / Admin | ACT-003 |
| `expired` | Liên kết, mã hoặc đề xuất đã hết hạn | FR-M01-02, FR-M01-09, FR-M01-11, FR-M10-03 |
| `paused` | Chức năng đang tạm dừng (tạm dừng đăng ký) | FR-M10-11 |
| `submitted` | Đã gửi xong, chờ bước sau ở nơi khác (email, người xét) | FR-M01-09, FR-M08-01, FR-M09-01 |

Cần trạng thái mới: thêm dòng vào bảng này (slug chữ thường, nối bằng `-`) và ghi nguồn. Không đặt slug tùy tiện
trong inventory.

## 5. Hai chế độ làm việc

| | Khám phá (bước 1–5) | Thực thi (bước 6–9) |
|---|---|---|
| Được làm | Đề xuất 2–3 phương án; thử font, màu, bố cục; hỏi nhiều | Áp tokens và component đã chốt lên màn hình |
| Không được làm | Rơi vào anti-pattern; vẽ ngoài màn hình mẫu (bước 3) | Thêm màu, cỡ chữ, khoảng cách, bóng, bo góc, hiệu ứng, phần tử không có trong tokens/component |
| `check_ui.py` | Không truyền `--tokens`: kiểm danh sách cấm | Truyền `--tokens`: kiểm thêm mọi giá trị ngoài tokens (ERROR) |
| Cần cái mới | Cứ đề xuất | Dừng, đề xuất ở cổng; duyệt xong cập nhật tokens/component rồi mới vẽ |

## 6. Nguồn sự thật theo thời gian

| Thứ | Trước bước 6 | Từ bước 6 | Sau khi có code |
|---|---|---|---|
| Chức năng | FR/US/SC | FR/US/SC | FR/US/SC |
| Quyết định thị giác | `DESIGN.md` | `DESIGN.md` + `tokens/tokens.json` | tokens trong repo frontend (sinh từ `tokens.json`) |
| Màn hình | canvas Claude Design | canvas Claude Design | code; canvas để tham chiếu |
| Figma | — | bản lưu từng đợt đã duyệt | bản lưu + Code Connect |

`tokens.json` trong repo và tokens của "iShare Design System" phải giống nhau. Sửa ở repo trước, chạy tool, rồi cập
nhật Design System.

## 7. Trạng thái và phiên bản tài liệu

- `trang_thai`: `Bản nháp` → `Chờ duyệt` (đang ở cổng) → `Đã chốt` (sau nghiệm thu bước 9). Chỉ người dùng chốt.
- `phien_ban`: bắt đầu `0.1`; tăng phần lẻ mỗi lần sửa sau khi đã duyệt một bước; lên `1.0` khi nghiệm thu.
- `steps_completed` trong frontmatter của `DESIGN.md` là nơi duy nhất ghi bước đã duyệt; `dot_da_duyet` ghi các đợt
  hi-fi đã duyệt.

## 8. Ngôn ngữ và nội dung

- Tài liệu: tiếng Việt, có dòng `[Vietnamese Doc]`. Tên token, component, tệp, mã: tiếng Anh/ASCII.
- Nội dung trên giao diện: tiếng Việt chuẩn, có dấu, Unicode NFC. Xưng hô và giọng văn theo `PRODUCT.md`.
- Dữ liệu mẫu: dùng bộ dữ liệu giả lập của SC (ví dụ D-POST, D-POLL, U-LAN, Mod Minh) để màn hình khớp kịch bản; cần
  thêm thì ghi vào mục "Dữ liệu mẫu" của `DESIGN.md` để mọi màn hình dùng chung.
- Tên người mẫu là tên Việt thật thường gặp (không dùng "Nguyễn Văn A", "John Doe"); ảnh đại diện mẫu dùng chữ cái
  đầu hoặc hình minh họa tự vẽ, không dùng ảnh người thật.
