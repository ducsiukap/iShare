# Bước 2 — Thêm kiểu cho mọi thuộc tính

Ứng với Step 2 của phương pháp: "Add the type of each attribute in all classes."

## Mục đích

Mỗi thuộc tính có một kiểu, tính bắt buộc và các ràng buộc mà nguồn đã nêu. Đây là đầu vào trực tiếp để chọn kiểu
cột ở skill `designing-database`.

## Đầu vào

Mục 2.1 của `CD-Mxx.md` sau bước 1; mục 2.3 của `EC-Mxx.md` (cột "Ràng buộc nguồn nêu", Nguồn); `FR-Mxx.md` để đọc
nguyên văn; `data-model/conventions.md` (QU-04); kết quả `merge_cd.py --list`.

## Việc làm

1. Chạy `merge_cd.py --dir $M/cd --list --exclude Mxx` để xem kiểu và kiểu liệt kê các module khác đã dùng. Cùng một
   loại dữ liệu (thời điểm, điểm số, nội dung giàu định dạng) phải dùng cùng một kiểu ở mọi module.
2. Với **mỗi** thuộc tính ở mục 2.1 (kể cả thuộc tính Dẫn xuất và thuộc tính của lớp Thống kê), chọn kiểu theo bảng,
   dùng bộ kiểu của QU-04:

   | Bản chất của thuộc tính (theo nguồn) | Kiểu | Ghi ở cột Ràng buộc |
   |---|---|---|
   | Tên, tiêu đề, mô tả, nội dung chữ | `String` | Độ dài tối đa nếu nguồn nêu, kèm đơn vị (ký tự, từ); tập ký tự cho phép; duy nhất |
   | Số đếm, số lượng, thứ tự, ngưỡng nhỏ | `int` | Khoảng giá trị nếu nguồn nêu |
   | Số có thể rất lớn; định danh | `long` | — |
   | Tỷ lệ, điểm có phần thập phân | `double` | — |
   | Có/không, cờ | `boolean` | Mặc định nếu nguồn nêu |
   | Ngày không kèm giờ | `LocalDate` | — |
   | Thời điểm (tạo, sửa, hết hạn, tính) | `Instant` | Lưu UTC, hiển thị giờ Việt Nam (DEC-127) |
   | Một trong một tập giá trị cố định mà nguồn **liệt kê đủ** (trạng thái, loại) | Kiểu liệt kê mới, đặt tên PascalCase | Giá trị mặc định nếu nguồn nêu |
   | Dữ liệu có cấu trúc do thư viện sinh (nội dung giàu định dạng) | `String` | Ghi định dạng nguồn nêu |

   Quy tắc khi chọn:
   - **Căn cứ kiểu** ghi mã FR/BR quyết định kiểu (ví dụ quy tắc nêu độ dài, bảng trạng thái nêu tập giá trị), hoặc
     `QU-04` khi kiểu chỉ theo quy ước.
   - **Bắt buộc**: `Có` khi nguồn nói thuộc tính luôn có; `Không` khi nguồn nói "tùy chọn", "nếu có", hoặc thuộc tính
     chỉ có giá trị ở một số trạng thái (lý do từ chối chỉ có khi bị từ chối). Nguồn không nói → đặt câu hỏi gom
     nhóm ở cổng, kèm đề xuất; không tự chọn im lặng.
   - **Không đoán** độ dài, khoảng giá trị, mặc định. Nguồn không nêu thì cột Ràng buộc ghi `—`.
   - **Tính chất** (`Lưu`, `Dẫn xuất`) giữ nguyên như EC.
3. **Kiểu liệt kê** (mục 2.2): mỗi tập giá trị cố định một kiểu.
   - Tên kiểu theo nghĩa nghiệp vụ (`TagStatus`, không phải `Status1`).
   - Giá trị viết HOA_GẠCH_DƯỚI, ngăn bởi dấu phẩy; lấy **đúng và đủ** từ bảng "Chuyển trạng thái" hoặc quy tắc của
     FR. Nếu register đã đặt tên giá trị (ví dụ `ACTIVE`, `BANNED`) thì dùng tên đó.
   - Một tập giá trị đã được module khác khai (xem kết quả `--list`) thì dùng lại đúng tên kiểu đó, không khai kiểu
     mới.
   - Chỉ tạo kiểu liệt kê khi nguồn liệt kê đủ các giá trị. Tập giá trị do người dùng quản lý là một lớp (đã xử lý
     ở bước phân tích), không phải kiểu liệt kê.
4. Thuộc tính mà hai cách chọn kiểu cho **hành vi khác nhau** (ví dụ lưu "tuần đạt danh hiệu" bằng ngày đầu tuần hay
   bằng số tuần) → câu hỏi ở mục 8, kèm lựa chọn và đề xuất. Người dùng quyết thì ghi `DD-Mxx-nn` ở mục 7.
5. Chạy `check_cd.py --cd … --step 2 --ec …`.

## Ghi vào tệp CD

Mục 2.1 (Kiểu, Bắt buộc, Ràng buộc, Căn cứ kiểu), mục 2.2, mục 7 và 8 nếu có.

## Tự kiểm trước cổng

- Không thuộc tính nào còn kiểu `—`.
- Không thuộc tính nào có kiểu là tên một lớp hoặc `Lớp[]`: thuộc tính đối tượng chỉ xuất hiện ở bước 4.
- Mỗi kiểu liệt kê: đối chiếu từng giá trị với bảng trạng thái hoặc quy tắc của FR, đủ và không thừa.
- Mỗi con số ở cột Ràng buộc dẫn được mã BR.
- Cùng một loại dữ liệu dùng cùng một kiểu trong cả tài liệu và giống các module đã làm.

## Trình ở cổng

- Bảng thuộc tính theo từng lớp.
- Các kiểu liệt kê và giá trị.
- Danh sách xác nhận gom nhóm: các thuộc tính mà tính bắt buộc là suy ra; các thuộc tính kiểu chỉ theo quy ước.
- Nếu là module đầu tiên: QU-04 cần xác nhận (bộ kiểu, nhất là kiểu thời điểm và kiểu số thực).
- Câu hỏi về kiểu có ảnh hưởng tới hành vi.

## Không làm

Không thêm thuộc tính mới. Không chọn kiểu cột của cơ sở dữ liệu (`varchar`, `bigint`): việc đó thuộc
`designing-database`.
