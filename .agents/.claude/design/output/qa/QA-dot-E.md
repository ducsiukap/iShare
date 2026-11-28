---
ma_tai_lieu: QA-dot-E
phien_ban: 0.1
trang_thai: Bản nháp
ngay: 2026-11-26
tac_gia: Phạm Văn Đức
---
# Kiểm tra giao diện — Đợt E (Vào hệ thống và tìm kiếm)

[Vietnamese Doc]

## 1. Phạm vi

- Màn hình (13): SCR-SHARED-03, SCR-M01-01, SCR-M01-02, SCR-M01-03, SCR-M01-04, SCR-M01-05, SCR-M01-06, SCR-M01-07, SCR-M01-08, SCR-M01-09, SCR-M01-10, SCR-M06-01, SCR-M06-02.
- Artboard: 40 trạng thái (theme sáng) + 13 bản theme tối cho trạng thái `default` (DD-UI-15). Tổng 53.
- Trang canvas: "Đợt E — Vào hệ thống và tìm kiếm" trong canvas "iShare — Giao diện"
  (https://claude.ai/artifact/HAykztXFcJbkAiSCXKvift#page-dot-e). Bản sao: `canvas/giao-dien/project/`.
- Design system: giống đợt A (`project/ds/ishare/`, bản "iShare Design System" 1795613002-b5c9).
- Cách vẽ trạng thái: trang đăng ký, đăng nhập, mật khẩu, kích hoạt lại, bảo trì và đồng ý chính sách là một khối giữa trang dưới thanh trên cùng chỉ có logo, cắt 1440 × 900 (riêng đăng ký `validation`, `paused` và bước 3 trọn trang vì cao hơn 900); gợi ý tìm kiếm là danh sách thả xuống trên nền Trang chủ; Cài đặt tài khoản dùng chung khung tab với SCR-M08-05 và SCR-M10-03 (đợt C); kết quả tìm kiếm và trang chính sách trọn trang.

## 2. Kết quả tool

| Tool | Lệnh | Kết quả |
|---|---|---|
| check_ui | `check_ui.py canvas/giao-dien/project --tokens output/tokens/tokens.json --design output/DESIGN.md` | ERROR=0 WARN=0 (cả canvas, 359 tệp) |
| check_inventory | `check_inventory.py --inventory output/screen-inventory.md --specs docs/specs --artboards canvas/giao-dien/project --batch E` | đủ 40/40; bản tối 13/40 (đúng DD-UI-15) |
| contrast | `contrast.py --tokens output/tokens/tokens.json --pairs output/tokens/contrast-pairs.csv` | 102/102 đạt (token không đổi từ bước 6) |

WARN giữ lại: không có.

## 3. Checklist bằng mắt

Rà trên ảnh chụp bản sao cục bộ (Chromium, 1440 px, font của design system), cả theme sáng và tối.

| Mục | Đạt | Ghi chú |
|---|---|---|
| ANTI-PATTERNS mục 9 (gồm brand test) | Đạt | Mỗi trang vào hệ thống chỉ một nút chính; nút Google theo DS GoogleButton (logo là tệp ảnh của canvas); không emoji |
| QF-04 vùng bấm | Đạt | Nút, icon button cao ≥32 px (control-h-sm); hàng bảng, mục danh sách cao ≥44 px |
| QF-05 focus không bị che | Đạt | Danh sách gợi ý nằm trên lớp riêng dưới ô tìm kiếm, không che ô đang gõ; ô có `role=combobox`, `aria-expanded`, `aria-controls` |
| QF-13 tiếng Việt | Đạt | Câu đồng ý chính sách 2 dòng, nhãn bước đăng ký, lịch sử tìm kiếm không dấu hiển thị đúng |
| QF-14 nội dung dài | Đạt | Trang chính sách đủ 2 phần, 12 mục; trang Chủ đề nhiều bài và đang tải thêm; ô tìm kiếm có truy vấn dài |
| QF-16 trợ giúp/khiếu nại nhất quán | Đạt | Màn hình khóa tài khoản dẫn tới khiếu nại (SCR-M01-05 `banned`); Cài đặt tài khoản `warned` dẫn tới Mức cảnh cáo |
| Nhất quán với các đợt trước | Đạt | Cùng khung trang, ô nhập, Alert, EmptyState với các đợt trước |

## 4. Lỗi

| Mã | Màn hình | Loại | Mô tả | Đề xuất | Mức | Đã sửa |
|---|---|---|---|---|---|---|
| QA-E-01 | SCR-M01-01 | Nhất quán | Nhãn bước "Bước 2 · Xác minh email" xuống hai dòng trong khối rộng 480 px | Rút thành "1. Tài khoản", "2. Xác minh email", "3. Hồ sơ" | Phải sửa | Đã sửa |
| QA-E-02 | SCR-M06-02 | Nội dung | Trạng thái không có kết quả, đang tải, lỗi vẫn ghi "3 bài viết" | Ghi "0 bài viết", "Đang tìm…", để trống khi lỗi | Phải sửa | Đã sửa |
| QA-E-03 | SCR-M01-03 | Nguồn | Màn hình mẫu bước 3 ghi username chỉ chữ thường; FR-M01-03.05 cho cả A–Z, FR-M01-03.11 giữ nguyên hoa, thường | Theo FR; dữ liệu mẫu A01 dùng "An_12A1" | Phải sửa | Đã theo FR |
| QA-E-04 | SCR-M01-05 | Nguồn | Kho màn hình ghi `banned`: "tài khoản BANNED không lấy lại mật khẩu được"; FR-M01-09.01, FR-M01-09.16 và BF-M01-018 cho đặt lại, xong chỉ vào màn hình tài khoản bị khóa | Vẽ theo FR: báo đã đổi mật khẩu và dẫn sang màn hình bị khóa; sửa ghi chú kho màn hình khi duyệt | Phải sửa | Đã theo FR — người dùng duyệt 2026-11-26; đã sửa ghi chú kho màn hình |
| QA-E-05 | SCR-M01-04 | Ghi nhận | `error` vẽ nhánh email chỉ có Google (câu nguyên văn của FR-M01-09.07); các nhánh sai mật khẩu, DEACTIVATED, bảo trì dùng cùng khối Alert ở vị trí đó | — | Ghi nhận | Giữ |
| QA-E-06 | SCR-M06-02 | Ghi nhận | `long` là trang Chủ đề (lọc đúng một Chủ đề, ô tìm rỗng, nút Đang theo dõi, không giới hạn 120 — BR-M06-16). Thông báo "Thu hẹp tìm kiếm để có kết quả chính xác hơn" (FR-M06-02.19) hiện ở cuối danh sách khi truy vấn có chữ đủ 120 kết quả, không vẽ artboard riêng | — | Ghi nhận | Giữ |
| QA-E-07 | SCR-M01-09 | Nội dung | BR-M01-42 ghi "câu chữ cụ thể viết sau"; các mục nguồn có nội dung (4 nhóm dữ liệu, dịch vụ bên ngoài, thời gian lưu, quyền của bạn) viết theo FR-M01-15, các mục khác để chỗ trống "[Câu chữ do nhóm dự án viết sau.]" | — | Ghi nhận | Giữ |
| QA-E-08 | SCR-M01-06 | Nội dung | Trạng thái `expired` không hiện khối báo "Liên kết đã hết hạn hoặc đã được dùng" (lỗi dựng artboard) | Hiện lại khối báo; nút đổi thành "Yêu cầu liên kết mới", dẫn về Quên mật khẩu với email điền sẵn, vì SC-M01-018 xin liên kết mới qua bước nhập email | Phải sửa | Đã sửa (phát hiện khi trả lời câu hỏi về mã hết hiệu lực) |

Thông điệp nguồn có chữ cụ thể được dùng nguyên văn: câu đồng ý "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý." (FR-M01-01.13), "Liên kết đã được gửi, vui lòng kiểm tra email của bạn" (FR-M01-09.13), "Tài khoản này đăng nhập qua Google, vui lòng dùng Google để đăng nhập" (FR-M01-09.07), "Hệ thống đang bận, vui lòng thử lại sau", "Tìm kiếm thông minh" (FR-M06-02.24), "Tài khoản đã bị khóa".

Thông điệp nguồn không có chữ cụ thể, viết theo giọng văn `PRODUCT.md`: lỗi định dạng email, mật khẩu 8–64 ký tự, chưa đồng ý, email đã có tài khoản, tạm dừng đăng ký, liên kết xác minh hết hạn, username đã có người dùng, thiếu tên hiển thị, hai mật khẩu chưa khớp, mật khẩu hiện tại chưa đúng, mã kích hoạt sai (kèm số lần còn lại), mã hết hiệu lực, trang bảo trì, đồng ý lại chính sách, "Quá nhiều yêu cầu tìm kiếm" (BR-M06-21 chỉ nói "thông báo quá nhiều yêu cầu"), không có gợi ý, không tìm thấy bài.

## 5. Đề xuất token / component mới

Không thêm token. Thanh bước đăng ký dùng DS StepIndicator; danh sách gợi ý dùng DS Combobox (`is-pop`, `is-opt`). Không có component mới.

## 6. Câu hỏi

| # | Câu hỏi | Trạng thái |
|---|---|---|
| 1 | SCR-M01-05 `banned`: vẽ theo FR (BANNED đặt lại được mật khẩu, xong chỉ vào màn hình bị khóa) thay vì ghi chú kho màn hình "không lấy lại mật khẩu được" (QA-E-04). Đồng ý, và sửa ghi chú kho màn hình? | Đồng ý, 2026-11-26; screen-inventory.md 0.3 |
| 2 | Mã kích hoạt sai hiện thêm "Bạn còn N lần thử" (FR-M01-11.08 chỉ nói sai lần thứ 5 thì mã mất hiệu lực). Giữ hay bỏ số lần còn lại? | Giữ, 2026-11-26 (DD-UI-39) |
