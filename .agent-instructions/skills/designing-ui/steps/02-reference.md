# Bước 2 — Reference và moodboard (`moodboard.md`)

[Vietnamese Doc]

## Mục đích

Có **điểm tựa thật** để chọn hướng thẩm mỹ, thay vì để model tự rơi về mặc định. Reference cho ta *pattern có lý do*
(cách bố trí, cách tổ chức thông tin, cách xử lý một trạng thái), không cho ta giao diện để chép.

## Đầu vào

- `PRODUCT.md` đã duyệt (mục 2–6: người dùng, việc chính, cảm xúc).
- Câu trả lời Q2-01 … Q2-04; ảnh người dùng gửi.

## Việc làm

1. Chép `output/moodboard-template.md` → `moodboard.md`. Lưu ảnh người dùng gửi vào `moodboard/` tên `R-nn-<mô-tả>.png`.
2. **Ghi reference của người dùng trước** (thích và ghét), giữ nguyên lý do họ nói.
3. **Bổ sung reference** để đủ ít nhất **ba nhóm nguồn khác loại**, tổng 8–15 mục:
   - (a) Hỏi đáp và cộng đồng: cách đặt câu hỏi là nhân vật chính, vote cạnh nội dung, luồng bình luận gọn, tag dưới
     tiêu đề, trạng thái kiểm duyệt (ví dụ Stack Overflow, Reddit, Discourse, Quora).
   - (b) Đọc và viết nội dung dài: nhịp chữ, độ rộng dòng, cách trình bày công thức/code/bảng, trình soạn thảo tối
     giản (ví dụ ứng dụng đọc báo, Notion, Linear cho thanh công cụ và phím tắt).
   - (c) Học tập: cách gắn môn/lớp, lời giải từng bước, gamification tiết chế (ví dụ Quizlet, Duolingo — chỉ học cách
     thưởng, không học màu kẹo). Ứng dụng Việt học sinh đang dùng (Q2-03): chỉ ghi **thói quen người dùng**, không lấy
     làm reference thẩm mỹ.
   - (d) Tùy chọn — vật liệu ngoài màn hình liên quan bối cảnh (vở, giấy kiểm tra, bảng tin lớp, sách giáo khoa): mô tả
     bằng lời và ảnh tự chụp/ảnh người dùng gửi.
   Được tìm trên web (WebSearch/WebFetch) và đọc mô tả; chụp màn hình trang web chỉ khi người dùng đồng ý. Không tải
   ảnh có bản quyền về repo; ghi link.
4. **Không dùng làm reference thẩm mỹ:** shot Dribbble/Behance kiểu landing SaaS, template shadcn/Tailwind UI, trang
   do AI sinh, các "UI kit" bán sẵn. Đây chính là nguồn của dáng AI.
5. Với **mỗi** reference điền bảng (mục 2 của template): mã `R-nn`, nguồn (link hoặc ảnh), nhóm (a–d), **mượn gì**
   (một pattern cụ thể, nói rõ áp vào màn hình/việc nào của iShare), **vì sao** (gắn với `PRODUCT.md`: việc chính,
   cảm xúc, ràng buộc), **không mượn gì** (màu, font, logo, minh họa của họ…).
6. **Tổng hợp** (mục 3–4 của template):
   - Đặc điểm rút ra từ những gì người dùng thích (5–8 dòng, mỗi dòng dẫn `R-nn`).
   - Điều cần tránh rút ra từ những gì người dùng ghét → ghi thành `AP-P-nn` trong `DESIGN.md` mục 6 (bảng "Điều cần
     tránh riêng của dự án"). Đây là luật bổ sung cho `ANTI-PATTERNS.md`, áp từ bước 3.
7. Tự rà: không có reference nào chỉ ghi "đẹp"; mỗi reference có ít nhất một pattern cụ thể; ba nhóm nguồn đều có.

## Đầu ra

- `moodboard.md` (+ ảnh trong `moodboard/`).
- `DESIGN.md` mục 6: các dòng `AP-P-nn`.

## Trình ở cổng

- Số reference theo nhóm; 5–8 đặc điểm rút ra; các `AP-P-nn` mới.
- Hỏi: có reference nào bỏ hoặc thêm không; có đặc điểm nào hiểu sai ý người dùng không.
- Báo trước bước 3: sẽ vẽ 2–3 hướng trên màn hình mẫu "Chi tiết bài viết"; hỏi Q3-02 (mức "vui" của gamification)
  nếu cần.

Sau khi người dùng đồng ý: thêm `2` vào `steps_completed`, `buoc_hien_tai: 3`.

## Không làm

- Không chọn màu, font hay hướng thẩm mỹ ở bước này.
- Không chép giao diện, logo, minh họa của reference vào thiết kế.
