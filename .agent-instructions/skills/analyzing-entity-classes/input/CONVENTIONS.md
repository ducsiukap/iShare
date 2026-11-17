# Quy ước chung của ba skill mô hình dữ liệu

Tệp này là nơi duy nhất ghi các quy ước dùng chung cho `analyzing-entity-classes`, `designing-entity-classes` và
`designing-database`. Hai skill sau trỏ về đây, không chép lại.

## 1. Trình tự làm việc

- Làm **xong một skill cho mọi module rồi mới sang skill sau**: phân tích lớp thực thể (EC) cho lần lượt từng
  module → thiết kế lớp thực thể (CD) cho lần lượt từng module → thiết kế cơ sở dữ liệu (DB) cho lần lượt từng
  module. Mỗi skill cho một tài liệu riêng của từng module.
- **Gộp hệ thống** (`steps/90-system-merge.md` của từng skill): chạy ngay khi mọi module đã chốt tài liệu
  của skill đó, **trước khi sang skill sau** (người dùng đã chốt 2026-11-15). Tức là: mọi `EC-Mxx` → `EC-SYS` → mọi `CD-Mxx` → `CD-SYS` → mọi
  `DB-Mxx` → `DB-SYS`. Lý do: điểm lệch giữa các module (một lớp hai tên, hai module cùng nhận sở hữu một lớp, bội số
  khác nhau) được sửa ở tài liệu module trước khi skill sau lấy chúng làm đầu vào.
- Đầu vào của skill sau **vẫn là tài liệu của từng module** (`EC-Mxx.md` → `CD-Mxx.md` → `DB-Mxx.md`), đã cập nhật
  theo quyết định gộp nếu có. Bản `…-SYS.md` là bản tổng hợp toàn hệ thống, không thay tài liệu module.
- Thứ tự module gợi ý, giống thứ tự viết FR (module nền trước, để module sau dùng lại tên lớp đã có):
  M01 → M02 → M03 → M04 → M05 → M06 → M07 → M08 → M09 → M10 → M13, rồi M11 → M12 → M16, rồi M14 → M15.
- Lỗi của tầng trên được sửa ở tầng trên: thiết kế lớp thấy thiếu thuộc tính thì quay lại sửa EC (tăng phiên bản,
  qua cổng), không vá ở CD; thiết kế CSDL thấy quan hệ n-n thì quay lại EC; EC thấy FR thiếu thì báo để sửa FR.

## 2. Nơi lưu và mã

Mọi đường dẫn tính từ gốc repo iShare.

| Tài liệu | Đường dẫn | Mã |
|---|---|---|
| Phân tích lớp thực thể của module | `.agents/.claude/system_analysis/output/data-model/ec/EC-Mxx.md` | `EC-Mxx` |
| Thiết kế lớp thực thể của module | `.agents/.claude/system_analysis/output/data-model/cd/CD-Mxx.md` | `CD-Mxx` |
| Thiết kế CSDL của module | `.agents/.claude/system_analysis/output/data-model/db/DB-Mxx.md` | `DB-Mxx` |
| Bản gộp toàn hệ thống | cùng thư mục: `EC-SYS.md`, `CD-SYS.md`, `DB-SYS.md` | `EC-SYS`… |
| Quy ước đã được người dùng xác nhận | `.agents/.claude/system_analysis/output/data-model/conventions.md` | `QU-nn` |
| Tệp tạm của tool | thư mục `.work/` trong `ec/`, `cd/`, `db/` (xóa được, chạy lại sẽ sinh lại) | — |

| Mã | Nghĩa |
|---|---|
| `R-Mxx-nn` | Quan hệ giữa hai lớp, sinh ở EC; CD và DB **dùng lại đúng mã này** để truy vết xuyên ba tài liệu |
| `Q-nn` | Câu hỏi trong một tài liệu |
| `DD-Mxx-nn` | Quyết định thiết kế riêng của module (ở CD và DB) |
| `MD-nn` | Quyết định gộp ở bản hệ thống (ở `EC-SYS.md`; CD-SYS và DB-SYS áp dụng lại) |
| `R-SYS-nn` | Quan hệ chỉ xuất hiện khi gộp hệ thống |

Mã không bao giờ đánh lại.

Trạng thái tài liệu: `Bản nháp` → `Đã chốt` (phiên bản 1.0 khi chốt lần đầu). Trường `nguon` trong frontmatter ghi
tài liệu đầu vào kèm phiên bản, ví dụ `nguon: FR-M05 v1.0`, `nguon: EC-M05 v1.0`.

## 3. Ngôn ngữ

Tài liệu viết bằng tiếng Việt, vì danh từ được trích từ tài liệu FR tiếng Việt và người đọc là hội đồng chấm đồ án.
Tên lớp, thuộc tính, kiểu, bảng, cột viết bằng tiếng Anh. Mẫu tài liệu mang dấu `[Vietnamese Doc]` theo
COMMON-RULES Rule 1.

## 4. Bảng quy ước (QU)

Cột "Trạng thái" cho biết quy ước đã được người dùng chốt hay còn chờ:

- **Đã chốt**: dùng luôn, không hỏi lại.
- **Chờ xác nhận**: cột "Giá trị" là mặc định của skill. Skill nào dùng tới quy ước đó thì trình nó ở cổng bước 1 của
  **module đầu tiên**, để người dùng xác nhận hoặc đổi một lần cho mọi module. Kết quả ghi vào
  `data-model/conventions.md` (mẫu: `output/conventions-template.md`). Các module sau đọc tệp đó trước khi làm; giá
  trị trong tệp đó thắng giá trị ở bảng này.

| Mã | Về việc gì | Giá trị | Trạng thái |
|---|---|---|---|
| QU-01 | Tên lớp (entity) | PascalCase, tiếng Anh, số ít. Lấy tên trong `registers/glossary.md` nếu có (Post, Comment, Topic, Tag, Group…). Lớp liên kết: lấy tên nghiệp vụ nếu FR có, không thì ghép tên hai lớp (`PostTopic`). Lớp thống kê: tên lớp gốc + `Stat` | **Đã chốt** (PascalCase, 2026-11-15) |
| QU-02 | Thuộc tính định danh | Tên `id`, kiểu `long`. Kiểm `registers/decisions.md` xem đã có quyết định về kiểu định danh chưa trước khi trình | Chờ xác nhận (case study dùng `int`) |
| QU-03 | Tên thuộc tính của lớp | camelCase, tiếng Anh. Nếu register đã gọi tên một trường (ví dụ `grade_level`) thì dùng tên đó đổi sang camelCase (`gradeLevel`) | **Đã chốt** (camelCase, 2026-11-15) |
| QU-04 | Kiểu thuộc tính (Java) | Chữ: `String`. Số nguyên: `int` (đếm, giới hạn nhỏ), `long` (id, số lớn). Số thực: `double`. Đúng/sai: `boolean`. Ngày không giờ: `LocalDate`. Thời điểm: `Instant` (lưu UTC theo DEC-127). Tập giá trị cố định nguồn đã liệt kê: kiểu liệt kê (enum) đặt tên PascalCase | Chờ xác nhận (case study dùng `float`, `Date`) |
| QU-05 | Thuộc tính đối tượng | camelCase. Một đối tượng: tên lớp (`client : Client`). Danh sách: kiểu `X[]`, tên số nhiều (`rooms : Room[]`). Hai thuộc tính cùng kiểu trong một lớp thì đặt theo vai trò (`author`, `lockedBy`) | Chờ xác nhận (`X[]` là ký pháp "danh sách X" của phương pháp) |
| QU-06 | Tên bảng | snake_case của tên lớp, **số nhiều** như register đang dùng: `PostTopic` → `post_topics`, `Tag` → `tags`. Register đã gọi tên bảng của đúng thực thể đó thì dùng lại tên ấy | **Đã chốt** (2026-11-15: snake_case, số nhiều; thay cho `tbl` + tên lớp của phương pháp gốc) |
| QU-07 | Tên cột | snake_case của tên thuộc tính: `starLevel` → `star_level` | **Đã chốt** (2026-11-15) |
| QU-08 | Tên khóa ngoại | snake_case, kết thúc bằng `_id`. Tên thuộc tính đối tượng tương ứng + `_id` (`client` → `client_id`, `author` → `author_id`). Khi thuộc tính đối tượng là danh sách ở phía kia thì dùng tên lớp phía 1 + `_id` (`hotel_id`) | snake_case: **Đã chốt**. Cách ghép tên: Chờ xác nhận |
| QU-09 | Kiểu cột (PostgreSQL) | `String` → `varchar(n)` khi nguồn nêu độ dài tối đa tính bằng ký tự, `text` khi không. `int` → `integer`. `long` → `bigint`. `double` → `double precision`. `boolean` → `boolean`. `LocalDate` → `date`. `Instant` → `timestamptz`. Kiểu liệt kê → `varchar(30)` kèm danh sách giá trị cho phép ở cột Ghi chú | Chờ xác nhận (tech stack: PostgreSQL, DEC-134–137) |
| QU-10 | Sơ đồ | Tool sinh mã PlantUML từ các bảng vào tệp riêng `diagrams/<mã tài liệu>.puml` cạnh tài liệu, render thành `diagrams/<mã tài liệu>.png`; tài liệu chỉ nhúng ảnh PNG và liên kết tới tệp `.puml`, không chép mã PlantUML. Không viết tay, không sửa tay tệp `.puml` hay ảnh | **Đã chốt** (2026-11-17, góp ý của người dùng sau lần chạy thử M05) |
| QU-11 | Bội số | Viết `1`, `0..1`, `0..*`, `1..*`, hoặc khoảng cụ thể `1..3` khi quy tắc nghiệp vụ nêu số | Chờ xác nhận |

Tóm tắt cách đặt tên qua ba tài liệu: lớp `PostTopic`, thuộc tính `createdAt` (EC, CD) → bảng `post_topics`, cột
`created_at`, khóa ngoại `post_id` (DB). Cột "Từ lớp" và "Từ thuộc tính" của tài liệu DB giữ tên gốc để truy vết.

## 5. Liên module

Một module thường chạm tới dữ liệu của module khác (M05 gán Topic cho **bài viết** của M03). Quy tắc:

1. **Mỗi lớp có đúng một module sở hữu**: module mà FR của nó định nghĩa thực thể đó ở mục "Dữ liệu nghiệp vụ" mà
   không ghi chú mã module khác, và có chức năng Tạo trong ma trận CRUD. Thực thể FR ghi kèm "(Myy)" là của Myy.
2. **Lớp của module khác (lớp ngoài)** vẫn được ghi ở bảng lớp của module đang làm, với cột Sở hữu = `Myy`, để
   quan hệ có hai đầu. Thuộc tính của lớp ngoài chỉ ghi hai loại:
   - Thuộc tính module này **đọc hoặc ghi** (M05 đọc tiêu đề bài viết để gợi ý Topic; M05 ghi lý do vào dòng nhật ký
     kiểm duyệt): Căn cứ = `Tham chiếu`. Module sở hữu lớp đó định nghĩa chúng; lượt gộp kiểm module sở hữu đã có
     chưa.
   - Thuộc tính mà **FR của module đang làm định nghĩa** nhưng nằm trên lớp ngoài: Căn cứ = `Nguồn nêu` hoặc
     `Đề xuất`, và ghi ở mục Liên module (cột "Thuộc tính module này bổ sung").
   Không liệt kê các thuộc tính khác của lớp ngoài. Các skill sau (CD, DB) không chép thuộc tính của lớp ngoài.
3. **Tên lớp ngoài**: chạy `merge_ec.py --list` để lấy đúng tên nếu module sở hữu đã có EC; chưa có thì lấy theo
   `glossary.md` và ghi chú "tên tạm, chờ EC-Myy".
4. **Quan hệ giữa lớp của module này và lớp ngoài** được ghi ở module mà FR của nó nói tới quan hệ đó. Hai module
   cùng ghi một quan hệ thì lượt gộp sẽ khử trùng và đối chiếu bội số.
5. **Không ghi quan hệ giữa hai lớp ngoài.**
6. Ở CD: thuộc tính đối tượng rơi vào lớp ngoài thì vẫn ghi ở mục 4 và ghi thành **đề nghị** ở mục Liên module;
   module sở hữu không bị sửa, lượt gộp sẽ đưa thuộc tính đó vào lớp.
7. Ở DB: bảng của module khác không tạo lại, chỉ ghi ở mục 7.1. Khóa ngoại nằm ở bảng của module này và trỏ tới bảng
   ngoài thì ghi bình thường ở 4.2. Khóa ngoại phải nằm **ở bảng ngoài** (bảng ngoài là phía n) thì ghi thành đề
   nghị ở mục 7.2.
8. Không sửa tài liệu của module khác. Lệch thì ghi ở cổng.

## 6. Câu hỏi về thiết kế và câu hỏi về yêu cầu

| Câu trả lời của người dùng là… | Ghi ở đâu |
|---|---|
| Một quy ước dùng cho mọi module (kiểu id, tiền tố bảng…) | `data-model/conventions.md`, kèm mã QU |
| Một quyết định thiết kế riêng của module (chọn kiểu, gộp hay tách bảng 1-1, giữ cột dẫn xuất) | Bảng Quyết định thiết kế của tài liệu đó (`DD-Mxx-nn`) |
| Duyệt một thuộc tính `Đề xuất` (FR không gọi tên, nhưng chức năng hoặc quy tắc đã có của FR cần nó) | Giữ trong tài liệu với Căn cứ `Đề xuất` và lý do; không cần sửa FR |
| Một yêu cầu mới hoặc sửa yêu cầu (hành vi, dữ liệu nghiệp vụ FR chưa có) | Không ghi thẳng vào mô hình. Báo người dùng cập nhật FR bằng skill `analyzing-functional-requirements`; tài liệu đang làm ghi câu hỏi ở trạng thái "Chờ cập nhật FR-Mxx" |

Ranh giới giữa hai dòng cuối: đề xuất chỉ làm cho hành vi FR **đã có** chạy được (cần tên để hiện danh sách, cần
thời điểm để xét "7 ngày gần nhất"). Thứ người dùng sẽ thấy hoặc nhập mà FR chưa nói là yêu cầu mới.
