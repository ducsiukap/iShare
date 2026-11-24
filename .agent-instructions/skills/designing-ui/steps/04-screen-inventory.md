# Bước 4 — Danh mục màn hình (`screen-inventory.md`)

[Vietnamese Doc]

## Mục đích

Biết chính xác **phải vẽ những màn hình nào, mỗi màn hình có những trạng thái nào, ai thấy**, không thiếu và không bịa.
Danh mục này là hợp đồng của bước 5, 7, 8: tool kiểm truy vết và kiểm đủ artboard dựa trên nó.

## Đầu vào

- Mỗi `US-Mxx.md`: `<!-- uc:actors -->`, `<!-- uc:catalog -->`, `<!-- uc:decomposition -->`.
- Mỗi `SC-Mxx.md`: `<!-- sc:flows -->` (BF), `<!-- sc:main … -->`, `<!-- sc:exceptions … -->` và
  `<!-- sc:branch … -->` (nhánh E → trạng thái, thông điệp).
- FR: quy tắc hiển thị, giới hạn (độ dài, số lượng), vai trò được xem; `DB-Mxx.md` khi cần biết trường.
- `PRODUCT.md` mục 2–4 (vai trò, thiết bị, việc chính).
- `input/CONVENTIONS.md` mục 3 (mã), mục 4 (slug trạng thái).

## Việc làm

1. Chép `output/screen-inventory-template.md` → `screen-inventory.md`.
2. **Đi từng module M01 → M16.** Với mỗi UC con (`tier = sub`) trong `uc:catalog`:
   - UC mục tiêu người dùng (`User goal`) → thường là một màn hình riêng, hoặc một hộp thoại/ngăn trượt có việc
     riêng.
   - UC chức năng phụ (`Subfunction`) → thường là một phần của màn hình khác; ghi UC đó vào cột `uc` của màn hình
     chứa nó.
   - UC chỉ do hệ thống/AI thực hiện (quét AI, tác vụ định kỳ) → **không** có màn hình riêng; hiệu ứng nhìn thấy được
     của nó (bài bị gắn cờ, thông báo) thành trạng thái của màn hình khác. Ghi UC vào bảng `ui:no-screen` kèm lý do
     và "hiện ở đâu".
   - Một màn hình = một đường dẫn trang riêng, hoặc một hộp thoại/ngăn trượt có việc riêng đủ lớn. Đừng tách mỗi nút
     thành một màn hình; đừng gộp hai việc khác vai trò vào một màn hình chỉ vì giống nhau.
3. **Màn hình dùng chung** (`SCR-SHARED-nn`, cột `module` ghi `SHARED`): khung ứng dụng (header, điều hướng, chuông
   thông báo, biểu tượng chat), khung quản trị, banner thông báo/bảo trì của hệ thống, trang lỗi
   (`not-found`, `forbidden`, `error`), màn hình tài khoản bị khóa/ban (dẫn sang khiếu nại). Chỉ thêm khi nguồn có
   (ghi mã nguồn).
4. Với **mỗi màn hình** điền đủ cột:
   - `id` (`SCR-Mxx-nn`), `name` (tiếng Việt, đúng thuật ngữ glossary), `module`.
   - `roles`: vai trò thấy màn hình (ACT-xxx hoặc tên vai trò theo US).
   - `uc`, `sc`: các UC-Mxx-nnn và SC-Mxx-nnn liên quan (cách nhau bằng dấu phẩy).
   - `sources`: mã FR/BR chính quy định nội dung hiển thị.
   - `states`: slug trạng thái (`CONVENTIONS.md` mục 4). Lấy từ: tối thiểu `default`; `loading`, `empty`/`no-result`,
     `error` nếu màn hình tải dữ liệu; `long` nếu hiện nội dung người dùng; `validation` nếu có form; trạng thái nghiệp
     vụ từ các nhánh E của SC liên quan (`forbidden`, `locked`, `pending`, `flagged`, `banned`…); biến thể theo vai
     trò (`owner`, `visitor`, `guest`, `mod`) nếu cùng màn hình khác nhau theo người xem.
   - `devices`: `desktop` hoặc `desktop, mobile` (theo `PRODUCT.md` mục 3 và Q4-03).
   - `batch`: đợt vẽ (bước 6 sau).
   - `notes`: phần tử đặc biệt, phụ thuộc màn hình khác, câu hỏi.
5. **Truy vết ngược:** mọi UC con trong phạm vi phải xuất hiện ở ít nhất một màn hình hoặc ở `ui:no-screen`. SC nào
   không được màn hình nào nhắc tới thì xem lại.
6. **Chia đợt** (bảng `ui:batches`). Đề xuất mặc định, chỉnh theo danh mục thật và mốc của người dùng (Q1-08):
   - A — Đọc và viết: khung ứng dụng, feed, chi tiết bài viết, soạn bài, bình luận, Topic/Tag.
   - B — Con người: hồ sơ, theo dõi, gamification (điểm, huy hiệu, bảng xếp hạng).
   - C — Kiểm duyệt và quản trị: báo cáo, hàng chờ Mod, cảnh cáo/ban, khiếu nại, admin, thống kê.
   - D — Cộng đồng và liên lạc: nhóm, thông báo, chat.
   - E — Vào hệ thống và tìm kiếm: đăng ký, đăng nhập, quên mật khẩu, xác minh email, tìm kiếm.
   Đợt A đi đầu vì nó dùng màn hình mẫu đã chọn ở bước 3 và tạo ra phần lớn component.
7. Chạy tool, sửa đến khi ERROR = 0:
   ```
   python3 $SK/tools/check_inventory.py --inventory $D/screen-inventory.md --specs docs/specs
   ```
   Tool kiểm: mã đúng dạng và không trùng; UC/SC/FR/BR được dẫn có tồn tại; slug trạng thái thuộc từ vựng; mọi UC con
   đã có chỗ; cột bắt buộc không trống; đợt hợp lệ.
8. Ghi số liệu tóm tắt ở mục 1 của tệp: số màn hình theo module, số artboard dự kiến (màn hình × trạng thái ×
   thiết bị) theo đợt.

## Đầu ra

- `screen-inventory.md` (bảng `ui:screens`, `ui:no-screen`, `ui:batches`, mục câu hỏi mở).

## Trình ở cổng

- Tổng số màn hình, theo module; số artboard dự kiến theo đợt (để người dùng thấy khối lượng).
- UC không có màn hình riêng và lý do.
- Chỗ nguồn chưa rõ ảnh hưởng màn hình (câu hỏi mở).
- Q4-01, Q4-02, Q4-03.
- Kết quả `check_inventory.py`.

Sau khi người dùng đồng ý: thêm `4` vào `steps_completed`, `buoc_hien_tai: 5`.

## Không làm

- Không thêm màn hình, trạng thái hay vai trò không có nguồn.
- Không vẽ gì ở bước này.
