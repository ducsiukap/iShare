# Bước 1 — Mô tả chức năng của module trong một đoạn văn

Ứng với Step 1 của phương pháp: "Describe the functions of the system in a short and complete paragraph."

## Mục đích

Có một đoạn văn ngắn nhưng đủ, nói module làm gì, cho ai, trên những đối tượng dữ liệu nào. Mọi danh từ của bước 2
được trích từ đoạn này, nên đối tượng nào không được nhắc ở đây sẽ dễ bị sót ở các bước sau.

## Đầu vào

`FR-Mxx.md` đã chốt: mục 1.1, 1.2, 4.2, 4.4, yêu cầu cấp trên và lý do của từng chức năng, mục "Giao tiếp với module
khác". Ở bước này **chưa** đọc mục "Dữ liệu nghiệp vụ".

## Việc làm

1. Kiểm `FR-Mxx.md` có `trang_thai: Đã chốt`. Ghi `nguon: FR-Mxx v<phiên bản>` vào frontmatter của `EC-Mxx.md`.
2. Nếu đây là module đầu tiên làm skill này: đọc `input/CONVENTIONS.md` mục 4. Quy ước đã chốt (QU-01 tên lớp
   PascalCase, QU-03 tên thuộc tính camelCase) dùng luôn. Trình các quy ước còn "Chờ xác nhận" mà skill này dùng
   (QU-10, QU-11) ở cổng, rồi tạo `data-model/conventions.md` từ `output/conventions-template.md` sau khi được duyệt.
3. Viết **đoạn mô tả** (mục 1.1 của EC) theo các quy tắc sau.

   **Hình thức**
   - Một đoạn văn tiếng Việt, mỗi câu đánh số `(S1)`, `(S2)`… ở đầu câu.
   - Ngắn nhưng đủ: mỗi câu có tác nhân, hành động và đối tượng dữ liệu. Module nhỏ thường 5–8 câu, module lớn có
     thể hơn 15 câu. Không có trần số câu; có câu nào không mang thông tin về dữ liệu thì bỏ câu đó.

   **Nội dung phải có**
   - Câu mở nói module quản lý hoặc xử lý những đối tượng nào (như câu đầu của case study: hệ thống quản lý thông tin
     về khách sạn, phòng, khách hàng).
   - Các câu sau đi theo từng tác nhân ở mục 4.2: "Hệ thống cho phép <vai trò> <làm gì> <trên đối tượng nào>."
   - **Mỗi chức năng ở mục 4.4 của FR được ít nhất một câu nói tới.** Nhiều chức năng cùng tác nhân, cùng đối tượng
     thì gộp vào một câu.
   - **Thông tin được ghi lại khi một việc xảy ra**, nếu FR yêu cầu lưu: ai làm, lúc nào, lý do, kết quả. Đây là nơi
     sinh ra thuộc tính và lớp liên kết (như câu cuối của case study: hóa đơn được tạo với thông tin về khách hàng,
     các phòng đã đặt, dịch vụ đã dùng).
   - **Số liệu module tính ra hoặc thống kê** (điểm, thứ hạng, độ thịnh hành, bảng thống kê): gọi tên từng loại.
     Đây là nguồn của các lớp thống kê.
   - Đối tượng của module khác mà module này dùng: gọi đúng tên, chỉ nói phần module này chạm tới.

   **Cách dùng từ**
   - Mỗi đối tượng gọi bằng **một tên duy nhất**, đúng thuật ngữ ở mục 2.1 của FR. Không lúc "bài viết" lúc "bài
     đăng".
   - Không dùng đại từ ("nó", "chúng", "cái đó") thay cho đối tượng: bước 2 trích danh từ theo mặt chữ.
   - Hành động cần lưu dấu vết thì viết thành danh từ: "một lượt gợi ý Topic", "một lần vô hiệu hóa Tag".

   **Không đưa vào**
   - Giao diện: nút, màn hình, câu thông báo.
   - Con số giới hạn và công thức (tối đa 5 Tag, 30 ký tự, trọng số): để bước 2 ghi vào ràng buộc của thuộc tính.
   - Điều FR đã quyết là không làm, điểm hoãn (TBD), chi tiết kỹ thuật của AI.
   - Bất cứ điều gì FR không nói.

4. Lập **bảng truy vết câu** (mục 1.2): mỗi câu một dòng, cột Nguồn ghi mã chức năng hoặc yêu cầu của FR mà câu đó
   dựa vào (`FR-Mxx-nn`, `FR-Mxx-nn.mm`).
5. Chạy `check_ec.py --ec … --step 1 --fr …`. Tool kiểm: câu đã đánh số, mỗi câu có dòng truy vết và nguồn, nguồn
   có thật trong FR, mỗi chức năng ở mục 4.4 được ít nhất một câu nói tới.

## Ghi vào tệp EC

Frontmatter (`nguon`), mục 1.1, mục 1.2.

## Tự kiểm trước cổng

- Đọc lại từng chức năng ở mục 4.4 của FR: có đối tượng dữ liệu nào chức năng đó tạo, sửa hay ghi lại mà đoạn mô tả
  chưa gọi tên không?
- Mỗi câu chỉ nói điều FR nói. Không câu nào dựa vào hiểu biết chung về diễn đàn.
- Không có đại từ thay cho đối tượng; không có hai tên cho một đối tượng.

## Trình ở cổng

- Nguyên văn đoạn mô tả.
- Bảng chức năng → câu (để người dùng thấy không chức năng nào bị bỏ).
- Những thứ cố ý không đưa vào đoạn (đã hoãn, không làm, thuộc module khác) kèm lý do một dòng.
- Nếu là module đầu tiên: các quy ước QU cần xác nhận.

## Không làm

Chưa trích danh từ, chưa nêu lớp. Không đọc trước tệp của bước 2.
