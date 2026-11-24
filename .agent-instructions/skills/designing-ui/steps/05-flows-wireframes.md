# Bước 5 — Luồng và wireframe (`flows.md`)

[Vietnamese Doc]

## Mục đích

Chốt **bố cục và điều hướng** trước khi lo phần đẹp: người dùng đi từ đâu tới đâu, mỗi màn hình đặt cái gì ở đâu. Sửa
ở mức khung xám rẻ hơn nhiều so với sửa ở hi-fi.

Chế độ: **khám phá**, nhưng wireframe không có màu và không có font thương hiệu.

## Đầu vào

- `screen-inventory.md` đã duyệt.
- `SC-Mxx.md` của các luồng chính (`sc:main`, `sc:branch`); `DB-Mxx.md` cho trường của form.
- `PRODUCT.md` (thiết bị, việc chính), `DESIGN.md` mục 2 (hướng đã chọn — chỉ để biết mật độ và cấu trúc bố cục).
- Q5-01, Q5-02.

## Việc làm

1. Chép `output/flows-template.md` → `flows.md`.
2. **Sơ đồ trang (mục 1):** liệt kê đường dẫn trang cho mọi `SCR-*` có đường dẫn riêng (`/`, `/p/{id}`,
   `/u/{username}` theo FR-M02…). Đường dẫn nào FR đã định thì dùng đúng; còn lại đề xuất theo một quy tắc nhất quán
   và đánh dấu "đề xuất". URL phản ánh trạng thái cần chia sẻ (tab feed, bộ lọc tìm kiếm) nếu FR có các trạng thái đó.
3. **Mô hình điều hướng (mục 2):** desktop (thanh trên, cột trái…), mobile (thanh dưới hay menu — Q5-01), khu quản
   trị (Mod/Admin), vị trí cố định của thông báo, chat, trợ giúp/báo cáo/khiếu nại (QF-16). Mỗi lựa chọn là một
   `DD-UI-nn` trong `DESIGN.md`.
4. **Luồng chính (mục 3):** tối thiểu các luồng sau (bỏ luồng nào nguồn không có, thêm luồng nào SC nhấn mạnh):
   - Đăng ký nhiều bước và xác minh email (M01).
   - Soạn bài → gửi → đã đăng / chờ duyệt / bị từ chối (M03).
   - Đọc bài → bình luận, trả lời → upvote (M04, M12).
   - Báo cáo → Mod xử lý → cảnh cáo/ẩn/ban → người bị xử lý khiếu nại (M08, M09).
   - Tìm và tham gia nhóm (công khai / cần duyệt), đăng bài trong nhóm, ẩn danh (M11).
   - Nhận thông báo → đi tới nội dung (M07).
   - Chat 1-1 và nhóm (M16).
   - Tìm kiếm có bộ lọc (M06).
   Mỗi luồng: bảng bước gồm màn hình (`SCR-*`), hành động người dùng, phản hồi hệ thống, bước SC tương ứng
   (`SC-Mxx-nnn/Mk` hoặc nhánh `Ek`), điểm rẽ nhánh và lối ra (thành công, lỗi, hủy).
5. **Wireframe:** trên canvas "iShare — Khám phá", trang "Bước 5 — Wireframe". Artboard tên
   `wf--<luồng>--<SCR-id>--<thiết bị>.dc.html`. Quy tắc:
   - Chỉ xám (nền, khối, đường kẻ), một font hệ thống trung tính cho khung; không màu, không ảnh, không bóng.
     (Ngoại lệ có chủ đích với AP-10: wireframe không mang bản sắc. Ghi một dòng ngoại lệ phạm vi `wf--*` vào
     `DESIGN.md` mục 6.)
   - Chữ là **nội dung thật** (tiêu đề bài thật, thông điệp lỗi thật từ SC), không "Tiêu đề ở đây".
   - Bản desktop cho mọi màn hình trong luồng; bản mobile cho màn hình đánh dấu `mobile` trong inventory.
   - Có thể nối các artboard thành luồng bấm được (prototype) theo hướng dẫn của type Design, nếu người dùng muốn.
6. `check_ui.py` (chế độ khám phá) trên bản sao: ERROR = 0 (sau khi áp ngoại lệ wireframe).
7. Tự rà: mọi màn hình trong luồng có trong inventory; mọi nhánh E quan trọng của SC có lối ra; vị trí trợ giúp/khiếu
   nại nhất quán.

## Đầu ra

- `flows.md` (sơ đồ trang, điều hướng, luồng).
- Canvas "iShare — Khám phá", trang "Bước 5 — Wireframe"; bản sao trong `canvas/kham-pha/`.
- `DESIGN.md` mục 5 (DD-UI điều hướng), mục 6 (ngoại lệ wireframe).

## Trình ở cổng

- Sơ đồ trang (rút gọn), mô hình điều hướng desktop/mobile, danh sách luồng kèm link artboard.
- Chỗ phải quyết: điều hướng mobile, đường dẫn đề xuất, chỗ SC mơ hồ.
- Kết quả tool.

Sau khi người dùng đồng ý: thêm `5` vào `steps_completed`, `buoc_hien_tai: 6`.

## Không làm

- Không tô màu, không chọn font thương hiệu, không trang trí.
- Không thêm bước hay màn hình ngoài SC và inventory.
