# Bước 4 — Quy tắc, dữ liệu và trạng thái

## Mục đích

Tách các giới hạn, công thức, điều kiện thành quy tắc riêng; chỉ ra thực thể nghiệp vụ và vòng đời của chúng.
Phần này là đầu vào trực tiếp cho mô hình dữ liệu và state machine ở giai đoạn thiết kế, và để lộ chỗ hở
(thực thể không ai tạo, trạng thái không có đường vào).

## Đầu vào

Bảng C.1, các chức năng đã duyệt ở bước 3.

## Việc làm

1. **Quy tắc nghiệp vụ** (mục 5.n "Quy tắc nghiệp vụ"): mỗi giới hạn, hằng số, công thức, điều kiện, thứ tự
   sắp xếp mà nguồn nêu thành một dòng `BR-Mxx-nn`, viết một ý.
   Loại: Sự kiện (điều luôn đúng) · Ràng buộc (giới hạn) · Kích hoạt (điều kiện làm một hành động xảy ra) ·
   Suy diễn (nếu A thì B) · Tính toán (công thức).
2. **Ví dụ tính tay** cho mọi quy tắc có số, công thức, cửa sổ thời gian hoặc thứ tự: dùng số cụ thể, có ít nhất
   một trường hợp biên (đúng ngưỡng, vượt ngưỡng, thực thể ở rìa cửa sổ thời gian). Nếu không tính ra được một kết
   quả duy nhất từ lời văn nguồn thì đó là GAP loại **Mơ hồ**: ghi `[GAP]` và tạo `Q-nn`.
3. Mốc thời gian ("đăng", "gửi", "công khai"…) và đơn vị đếm (tiếng, ký tự, người dùng khác nhau…) xuất hiện
   trong quy tắc phải được định nghĩa ở mục 2.1.
4. **Dữ liệu nghiệp vụ**: thực thể và thuộc tính mà nguồn **đã nói tới**, ở mức nghiệp vụ. Nguồn ghi tên bảng hay
   cột (ví dụ `post_tags`, `is_active`) thì chuyển thành lời nghiệp vụ ("liên kết bài viết–Tag", "trạng thái hoạt động").
   Không thêm thuộc tính nguồn không nói.
5. **Ma trận CRUD**: với mỗi thực thể, ai tạo, đọc, sửa, xóa. Ô ghi `FR-Mxx-nn` (chức năng, bước 5 sẽ đổi thành
   ID cấp dưới), `Myy` (module khác làm), `Không có (lý do hoặc BR)` (đã quyết là không làm), hoặc `—` (chưa biết).
   Ô `—` thuộc module này và ảnh hưởng tới hành vi thì tạo `[GAP]` + `Q-nn`.
6. **Chuyển trạng thái**: chỉ cho thực thể mà nguồn nói có trạng thái (ví dụ Tag hoạt động / bị vô hiệu hóa).
   Một bảng mỗi thực thể; cột Yêu cầu để "—", bước 5 điền. Dòng đầu tiên từ `(bắt đầu)`.
7. Chạy `trace_check.py`. Ở bước này COV-04 (nguồn chưa dùng) và CRUD/STATE chưa có yêu cầu là bình thường;
   chỉ cần không có lỗi COV-01, COV-02, COV-08.
8. Phụ lục A: một dòng cho mỗi `BR-Mxx-nn`.

## Ghi vào tệp FR

Mục 2.1, 5.n Quy tắc nghiệp vụ, 5.n Dữ liệu nghiệp vụ (kèm CRUD), 5.n Chuyển trạng thái, Phụ lục A (BR),
Phụ lục B.1 (GAP mới), C.1 cột Dùng ở cho nguồn đã thành BR.

## Tự kiểm trước cổng

- Mỗi BR có nguồn; mỗi ví dụ tính lại đúng từ chính câu quy tắc.
- Không thuộc tính hay trạng thái nào thiếu nguồn.

## Trình ở cổng

- Danh sách quy tắc (ID, một dòng, ví dụ nếu có).
- Bảng thực thể và CRUD; các ô `—`.
- Bảng trạng thái; trạng thái không có đường vào hoặc ra.
- GAP mới phát sinh (sẽ hỏi ở bước 6).

## Không làm

Không thiết kế cơ sở dữ liệu (kiểu dữ liệu, khóa, chỉ mục). Không thêm trạng thái kỹ thuật nội bộ.
