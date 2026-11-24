# Bước 1 — Thêm id

Ứng với Step 1 của phương pháp: "Add the id attribute for the classes which DO NOT inherit from other class."

## Mục đích

Mỗi lớp cần được lưu có một thuộc tính định danh. Lớp con dùng định danh của lớp cha.

## Đầu vào

`EC-Mxx.md` đã chốt (mục 2.2, 3.4); `data-model/conventions.md` (QU-02) nếu đã có.

## Việc làm

1. Chép tập lớp từ mục 2.2 của `EC-Mxx.md` sang mục 1 của `CD-Mxx.md` (Lớp, Nhóm, Sở hữu giữ nguyên).
2. Điền cột **Lớp cha**: với mỗi dòng Kế thừa ở mục 3.4 của EC, lớp con ghi tên lớp cha; các lớp khác ghi `—`.
3. Điền cột **id** theo bảng:

   | Lớp | Cột id | Thuộc tính `id` |
   |---|---|---|
   | Của module này, không kế thừa lớp nào, Nhóm là Thực thể hoặc Liên kết | `Có` | Thêm một dòng `id` vào mục 2.1 |
   | Của module này, có lớp cha | `Kế thừa` | Không thêm: dùng id của lớp cha |
   | Lớp thống kê không có lớp cha (như IncomeStat của case study) | `Không` | Không thêm: lớp này không được lưu nên không cần định danh |
   | Lớp ngoài (Sở hữu là module khác) | `Ngoài` | Không thêm ở đây: id được thêm ở `CD` của module sở hữu |

   Lớp liên kết **vẫn có id riêng** như mọi lớp không kế thừa (case study: BookedRoom, UsedService đều có id).
4. Với mỗi lớp `Có`, thêm vào mục 2.1 một dòng: Thuộc tính = `id`, Tính chất = `Khóa`, Bắt buộc = `Có`,
   Ràng buộc = `Duy nhất`. Cột Kiểu và Căn cứ kiểu:
   - `data-model/conventions.md` đã có QU-02 được xác nhận → dùng kiểu đó, Căn cứ kiểu = `QU-02`.
   - Chưa có (module đầu tiên): tìm trong `registers/decisions.md` xem đã có quyết định nào về kiểu định danh chưa.
     Có thì đề xuất theo quyết định đó; không có thì đề xuất mặc định của `CONVENTIONS.md` (`long`). Trình ở cổng;
     người dùng xác nhận rồi mới ghi vào `data-model/conventions.md`.
5. Chép các thuộc tính còn lại từ mục 2.3 của EC sang mục 2.1 (Lớp, Thuộc tính, Tính chất), để cột Kiểu là `—`: bước
   2 sẽ điền. Làm vậy để tool đối chiếu được với EC ngay từ bước này.
   - Chép mọi dòng có Căn cứ `Nguồn nêu` hoặc `Đề xuất` của lớp module này (thuộc tính đề xuất đã được duyệt ở cổng
     bước 2 của EC, nên là thuộc tính thật của lớp).
   - **Không chép** dòng Căn cứ `Tham chiếu` và thuộc tính của lớp ngoài: module sở hữu thiết kế chúng. Thuộc tính
     module này bổ sung trên lớp ngoài (mục 5 của EC) ghi ở mục 6 Liên module, cột "Đề nghị cho module sở hữu".
6. Chạy `check_cd.py --cd … --step 1 --ec …`.

## Ghi vào tệp CD

Frontmatter (`nguon`), mục 1, các dòng `id` và khung thuộc tính ở mục 2.1.

## Tự kiểm trước cổng

- Số lớp ở mục 1 bằng số lớp ở mục 2.2 của EC; không lớp nào bị đổi tên.
- Mỗi lớp con (có dòng Kế thừa ở EC) ghi đúng lớp cha và không có id riêng.
- Không lớp ngoài nào được thêm id, và mục 2.1 không có thuộc tính của lớp ngoài.

## Trình ở cổng

- Bảng lớp với cột id; đếm theo từng giá trị (Có, Kế thừa, Không, Ngoài).
- Kiểu của id và căn cứ. Nếu là module đầu tiên: nêu rõ đây là quy ước QU-02 áp cho mọi module, cần người dùng xác
  nhận.
- Lớp thống kê nào mà FR yêu cầu **lưu** kết quả: đó là lỗi phân loại của bản phân tích (lớp được lưu phải có Nhóm =
  Thực thể để có id). Không tự đổi ở đây; báo người dùng để sửa `EC-Mxx.md`.

## Không làm

Chưa chọn kiểu cho các thuộc tính khác. Không thêm khóa ngoại. Không thêm lớp.
