# use-case-analysis — Hướng dẫn sử dụng

Skill này đọc tài liệu Yêu cầu Chức năng (FR) đã duyệt của một module iShare
và tạo ra tài liệu Đặc tả Use Case (US) tương ứng.

## Khi nào dùng

Dùng sau khi tài liệu `FR-Mxx.md` đã được phê duyệt và lưu vào `docs/specs/fr/`.

## Cách kích hoạt

Nói với agent:

> "Tạo tài liệu use case cho module M02"
> hoặc "Phân tích use case từ file docs/specs/fr/FR-M02.md"
> hoặc "Viết US-M03"

Agent sẽ tự tìm file FR tương ứng và bắt đầu quy trình 7 bước.

## Đầu vào bắt buộc

| Mục | Nơi chứa |
|---|---|
| Tài liệu FR của module | `docs/specs/fr/FR-Mxx.md` |

## Đầu ra

| Mục | Nơi chứa |
|---|---|
| Tài liệu US của module | `docs/specs/us/US-Mxx.md` |

## Quy trình (7 bước — có cổng xác nhận)

| Bước | Nội dung | Kết quả |
|---|---|---|
| 1 | Trích xuất chức năng con | Bảng tổng hợp (Mục 1) — Khóa hàng rào phạm vi |
| 2 | Xác định Use Case Chính | Danh sách UC + Macro Diagram (Mục 2.1–2.2) |
| 3 | Ánh xạ Actor & Quy trình | Mô tả nghiệp vụ hoàn chỉnh (Mục 2.3) |
| 4 | Phân rã Use Case con | Phân rã strictly trong phạm vi FR (giữ nguyên hoặc gộp, đơn nghiệp vụ) + Per-UC Diagrams + Bảng quan hệ (Mục 3) |
| 5 | Xây dựng ma trận truy vết | 100% FR → UC (Mục 4.1) |
| 6 | Vẽ sơ đồ tổng hợp | Full module diagram (Mục 4.2) |
| 7 | Kiểm tra & hoàn thiện | Tài liệu US hoàn chỉnh |

Mỗi bước dừng chờ xác nhận trước khi sang bước tiếp theo.

## Nguyên tắc cốt lõi cần nhớ
- **Strictly trong phạm vi FR:** Không tự suy diễn hay bịa thêm Use Case con ngoài phạm vi tài liệu FR.
- **Hai cơ chế tạo Use Case con:** Giữ nguyên chức năng FR (1-1) hoặc Gộp các chức năng liên quan mật thiết (N-1).
- **Đơn nghiệp vụ (Single Business Responsibility):** Mỗi Use Case con BẮT BUỘC chỉ đảm nhiệm đúng duy nhất 1 nghiệp vụ xác định cụ thể.
- **Tên Use Case chuẩn BA:** Cấu trúc `[1 Động từ duy nhất] + [Cụm danh từ]`, tuyệt đối không ghép nhiều động từ ("và", "&", "/", "hoặc").
- **3 quan hệ chuẩn UML:** `<<include>>`, `<<extend>>`, và `Generalization` (Kế thừa / Cha-Con).
- **Mermaid an toàn:** Luôn bọc nhãn mũi tên trong nháy kép `|"<<include>>"|`, không dùng `\n` hay placeholder `{{}}`.

## Tài liệu mẫu

- Xem `docs/specs/us/US-M01.md` để biết cấu trúc đầu ra chuẩn.
- Xem `output/us-template.md` để biết template có placeholder.

