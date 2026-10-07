---
module: Mxx
ten_module: <Tên module>
ma_tai_lieu: FR-Mxx
phien_ban: 0.1
trang_thai: Bản nháp
ngay: YYYY-MM-DD
tac_gia: Phạm Văn Đức
moc_nguon: DEC-xxx, QA-xxx, ISS-xxx, OPEN-xxx
steps_completed: []
---
# Tài liệu yêu cầu chức năng — Mxx <Tên module>

| Mã tài liệu | FR-Mxx |
|---|---|
| Dự án | iShare |
| Module | Mxx — <Tên module> |
| Trạng thái | Bản nháp |
| Phiên bản | 0.1 |
| Ngày | YYYY-MM-DD |
| Tác giả | Phạm Văn Đức |

<!-- Quy ước chung cho mọi bảng dưới đây:
     - Thân tài liệu không ghi nguồn. Nguồn của mọi ID nằm ở Phụ lục A.
     - Ô không có nội dung ghi "—". Không xóa cột.
     - Mục chưa tới bước làm thì để dòng "(Chưa làm — bước N)". -->

## 1. Tổng quan

### 1.1 Mục đích

<Một đến ba câu: module này giúp ai làm được gì. Lấy từ lời văn của draft và register.>

### 1.2 Phạm vi

**Trong phạm vi:**

- <Chức năng hoặc nhóm hành vi thuộc module này.>

**Ngoài phạm vi:**

- <Hành vi liên quan nhưng thuộc module khác, ghi kèm module sở hữu, hoặc điều đã quyết là không làm.>

## 2. Thuật ngữ và viết tắt

### 2.1 Thuật ngữ

| Thuật ngữ | Định nghĩa |
|---|---|
| <Thuật ngữ> | <Định nghĩa dùng trong tài liệu này. Mốc thời gian, đơn vị đếm, trạng thái phải được định nghĩa ở đây.> |

### 2.2 Viết tắt

| Viết tắt | Đầy đủ |
|---|---|
| FR | Functional Requirement — yêu cầu chức năng |

## 3. Thông tin đầu vào

### 3.1 Tài liệu đầu vào

| Tài liệu | Phiên bản / mốc |
|---|---|
| Draft: docs/_temp/iShare_modules.md, iShare_specs_general.md | Theo ngày sửa tệp |
| Register: decisions, qa-log, issue-queue, open-issues, glossary, module-registry | DEC-xxx, QA-xxx, ISS-xxx, OPEN-xxx (khớp `moc_nguon`) |

### 3.2 Tài liệu liên quan

| Module | Liên quan ở điểm nào |
|---|---|
| Myy <Tên> | <Một câu> |

## 4. Tổng quan chức năng

### 4.1 Luật, tiêu chuẩn liên quan

Không có.

### 4.2 Vai trò

| Vai trò | Mô tả trong module này |
|---|---|
| Guest | <…> |
| User | <…> |
| Mod | <…> |
| Admin | <…> |

### 4.3 Ma trận quyền

| Hành động | Guest | User | Mod | Admin | Yêu cầu |
|---|---|---|---|---|---|
| <Hành động> | ✗ | ✓ | ✓ | ✓ | FR-Mxx-01.02 |

<!-- ✓ được làm · ✗ bị từ chối · "✓ (của mình)" khi có điều kiện sở hữu. Mỗi ô ✗ phải có yêu cầu từ chối. -->

### 4.4 Danh sách chức năng

| ID | Chức năng | Tác nhân chính | Kích hoạt |
|---|---|---|---|
| FR-Mxx-01 | <Tên chức năng ở mức mục tiêu người dùng> | <Vai trò> | <Sự kiện hoặc thao tác bắt đầu> |

### 4.5 Mốc và ưu tiên

<Ghi một lần cho cả module, lấy từ cột MoSCoW của module-registry. Chỉ gắn nhãn riêng cho yêu cầu ngoại lệ.>

## 5. Yêu cầu chức năng

<!-- Mỗi chức năng một mục 5.x, đúng ID ở 4.4. Câu yêu cầu cấp dưới theo mẫu EARS tiếng Việt:
     Hệ thống phải …                      (luôn luôn)
     Khi <sự kiện>, hệ thống phải …       (sự kiện)
     Trong khi <trạng thái>, hệ thống phải …   (trạng thái kéo dài)
     Nếu <điều kiện bất thường>, hệ thống phải …   (ngoại lệ, lỗi, vi phạm)
     Ở nơi <tính năng được bật>, hệ thống phải …   (tùy chọn, ví dụ khi bật AI)
     Mỗi câu một hành vi, chủ ngữ của "phải" luôn là "hệ thống".
     Chỗ nguồn chưa đủ để viết: KHÔNG cấp ID, ghi một dòng ngay dưới bảng
       [GAP: <điều còn thiếu> — Q-nn]
     và thêm câu hỏi Q-nn vào Phụ lục B.1. Sau khi bạn trả lời ở bước 6, dòng [GAP] được thay bằng yêu cầu có ID. -->

### 5.1 FR-Mxx-01 <Tên chức năng>

**Yêu cầu cấp trên:** <Một câu mô tả năng lực của chức năng.>

**Lý do:** <Lấy từ lời văn của nguồn. Nguồn không nêu thì ghi "Nguồn chưa nêu lý do.">

**Yêu cầu cấp dưới:**

| ID | Yêu cầu |
|---|---|
| FR-Mxx-01.01 | Khi <…>, hệ thống phải <…>. |
| FR-Mxx-01.02 | Nếu <…>, hệ thống phải từ chối <…>. |

### 5.n Quy tắc nghiệp vụ

| ID | Loại | Quy tắc | Ví dụ |
|---|---|---|---|
| BR-Mxx-01 | Ràng buộc | <Giới hạn, công thức, điều kiện> | <Ví dụ tính tay khi có số, công thức, thời gian hoặc thứ tự; còn lại "—"> |

<!-- Loại: Sự kiện · Ràng buộc · Kích hoạt · Suy diễn · Tính toán -->

### 5.n Dữ liệu nghiệp vụ

| Thực thể | Thuộc tính nguồn đã nêu | Quan hệ |
|---|---|---|
| <Thực thể> | <Chỉ thuộc tính nguồn nói tới, ở mức nghiệp vụ, không kiểu dữ liệu> | <Thực thể khác> |

**Ma trận CRUD:**

| Thực thể | Tạo | Đọc | Sửa | Xóa |
|---|---|---|---|---|
| <Thực thể> | FR-Mxx-01.01 | FR-Mxx-02.01 | — | Không có (BR-Mxx-03) |

<!-- Ô ghi ID yêu cầu; "Myy" nếu module khác làm; "Không có (lý do hoặc BR)" nếu đã quyết là không làm; "—" là chưa biết và sẽ bị trace_check báo. -->

### 5.n Chuyển trạng thái

#### <Thực thể>

| Từ | Sự kiện | Điều kiện | Sang | Yêu cầu |
|---|---|---|---|---|
| (bắt đầu) | <Sự kiện> | — | <Trạng thái> | FR-Mxx-01.01 |

### 5.n Giao tiếp với module khác

| Hướng | Module | Nội dung ở mức nghiệp vụ | Yêu cầu |
|---|---|---|---|
| Cung cấp | Myy | <Module này cung cấp gì cho Myy> | FR-Mxx-… |
| Dùng | Myy | <Module này dùng gì của Myy> | — |

### 5.n AI hỗ trợ và hành vi khi tắt AI

<Chỉ có ở module dùng AI. Ghi các yêu cầu "Ở nơi AI được bật…" và "Nếu AI không khả dụng…" bằng ID ở mục 5.x tương ứng. Module không dùng AI ghi "Không áp dụng.">

### 5.n Yêu cầu HMI

Chưa có — chờ giai đoạn thiết kế.

### 5.n Chuyển màn hình

Chưa có — chờ giai đoạn thiết kế.

## 6. Lịch sử sửa đổi

| Phiên bản | Ngày | Nội dung | Người sửa |
|---|---|---|---|
| 0.1 | YYYY-MM-DD | Tạo mới | Phạm Văn Đức |

## Phụ lục A. Truy vết

| ID | Nguồn | Căn cứ | Ghi chú |
|---|---|---|---|
| FR-Mxx-01.01 | DEC-xxx, QA-xxx | Nói thẳng | — |
| FR-Mxx-01.02 | DEC-xxx | Suy ra | <Phép suy luận: nguồn nói "tối đa 3" ⇒ từ chối cái thứ 4> |

<!-- Căn cứ chỉ có hai giá trị: Nói thẳng | Suy ra. Suy ra bắt buộc có ghi chú.
     Mọi ID ở mục 4.4, 5.x (cấp trên và cấp dưới) và BR phải có dòng ở đây. -->

## Phụ lục B. Câu hỏi, giả định và TBD

### B.1 Câu hỏi đã hỏi

| Mã | Loại | Câu hỏi | Trả lời | Ghi vào register |
|---|---|---|---|---|
| Q-01 | Thiếu chi tiết | <…> | <…> | QA-xxx, DEC-xxx |

<!-- Loại: Mâu thuẫn · Mơ hồ · Thiếu chi tiết · Cần cân nhắc -->

### B.2 TBD

| ID | Nội dung | Ảnh hưởng | Lý do chưa chốt |
|---|---|---|---|
| TBD-Mxx-01 | <…> | Thấp | <Ví dụ: OPEN-007 hoãn có chủ đích> |

<!-- Ảnh hưởng: Cao · Trung bình · Thấp. Bản chốt không được còn TBD ảnh hưởng Cao. -->

### B.3 Cần cân nhắc (ngoài dữ liệu hiện có)

| Mã | Điểm cần cân nhắc | Vì sao cần | Quyết định |
|---|---|---|---|

## Phụ lục C. Sổ nguồn

**Owner keywords:** <từ khóa, phân tách bằng dấu phẩy>
**Dependency keywords:** <từ khóa>
**Mục draft của module:** <DM-x.y, …>
**Loại khỏi bảng nguồn (khớp nhầm):** <ID, …>

### C.1 Bảng nguồn

| Nguồn | Nhãn | Trạng thái | Dùng ở | Ghi chú |
|---|---|---|---|---|
| DEC-xxx | Sở hữu | Hiện hành | FR-Mxx-01.01, BR-Mxx-01 | — |
| DEC-yyy | Sở hữu | Bị thay bởi DEC-zzz | — | Chỉ trích DEC-zzz |
| QA-xxx | Phụ thuộc | Hiện hành | Chuyển M07 | Ghi ở 5.n Giao tiếp |
| ISS-xxx | Nhắc tới | Hiện hành | Không áp dụng: chỉ là câu hỏi đã có DEC trả lời | — |

<!-- Nhãn: Sở hữu · Phụ thuộc · Nhắc tới · Loại (khớp nhầm)
     Trạng thái: Hiện hành · Sửa một phần bởi X · Bị thay bởi X · Trùng với X · Mâu thuẫn với X
     Dùng ở: ID trong tài liệu · "Chuyển Myy" · "Không áp dụng: <lý do>" · "—" (chỉ khi Nhãn là Loại hoặc Trạng thái là Bị thay/Trùng) -->

### C.2 Chuỗi quyết định

| Chuỗi | Nội dung hiện hành |
|---|---|
| DEC-050 → DEC-xxx | <Phần nào của DEC-050 còn hiệu lực, phần nào bị thay> |
