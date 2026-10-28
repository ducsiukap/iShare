# Bước 7 — Rà soát Toàn diện & Hoàn thiện Tài liệu (Final Assemble & Verify)

**Mục tiêu:** Chạy checklist kiểm thử chất lượng toàn diện, cập nhật trạng thái sang `Hoàn thành` và bàn giao tài liệu `docs/specs/us/US-Mxx.md`.

## Danh mục Kiểm tra Toàn diện (Final Quality Checklist)

### 1. Tính đầy đủ & Cấu trúc (Completeness & Structure)
- [ ] Bảng Metadata đầu trang đầy đủ: Mã tài liệu, Tên module, Link nguồn FR-Mxx.md, Mốc register căn cứ, Ngày lập.
- [ ] Mục 1: Bảng tổng hợp chức năng con có số lượng dòng khớp 100% với mục 4.4 của tài liệu FR.
- [ ] Mục 2.1: Nêu rõ 3 tiêu chí phân rã và danh sách các Use Case Chính (tên UC Chính bao quát, chuẩn format).
- [ ] Mục 2.2: Sơ đồ tổng quan Macro Use Case Diagram (`flowchart LR`) đầy đủ Actor và UC Chính.
- [ ] Mục 2.3: Mô tả quy trình nghiệp vụ hoàn chỉnh cho tất cả các UC Chính (theo chuỗi bước tuần tự hoặc theo các nhánh song song Nhánh 1 / Nhánh 2, nêu rõ Actor từng nhánh).
- [ ] Mục 3: Có đầy đủ các tiểu mục (3.1, 3.2, ...) cho từng UC Chính, bao gồm Sơ đồ phân rã (`flowchart TB`) và Bảng quan hệ chi tiết.
- [ ] Mục 4.1: Ma trận truy vết FR $\to$ UC bao phủ 100% các chức năng con, ghi nhận đúng `*(Tiến trình ngầm)*` và `*(Tầng hiển thị)*`.
- [ ] Mục 4.2: Sơ đồ Use Case Chi tiết Toàn Module bao quát tất cả Actor, UC Chính và UC con.

### 2. Chuẩn mực UML & Tính logic Nghiệp vụ (UML Semantics & Logic)
- [ ] **100% trong phạm vi FR (Không vẽ thêm Use Case con):** Tất cả các Use Case con đều có căn cứ từ tài liệu FR (giữ nguyên từ chức năng FR hoặc gộp từ các chức năng liên quan). Tuyệt đối KHÔNG có Use Case con nào do agent tự suy diễn hoặc bịa ra ngoài phạm vi tài liệu FR.
- [ ] **Đơn nghiệp vụ (Single Business Responsibility):** Mỗi Use Case con (dù giữ nguyên hay gộp) chỉ đảm nhiệm đúng duy nhất 1 nghiệp vụ xác định cụ thể, không đa nhiệm, không gom tạp nham các nghiệp vụ khác biệt.
- [ ] **Quy tắc đặt tên Use Case:** 100% Use Case Chính và Use Case con đều tuân thủ cấu trúc `[1 Động từ duy nhất] + [Cụm danh từ]`, tuyệt đối không dùng nhiều động từ nối nhau ("và", "&", "/", "hoặc").
- [ ] **Quan hệ `<<include>>`:** Thể hiện đúng các bước nghiệp vụ tiên quyết, bắt buộc phải có. Chiều mũi tên từ UC Chính sang UC con.
- [ ] **Quan hệ `<<extend>>`:** Thể hiện đúng các nhánh tùy chọn, mở rộng, phương thức thay thế, ngoại lệ hoặc nhánh nghiệp vụ song song. Chiều mũi tên từ UC con về UC Chính.
- [ ] **Quan hệ `Generalization`:** Thể hiện đúng quan hệ cha - con (chuyên biệt hóa / kế thừa). Chiều mũi tên nét liền từ UC con chuyên biệt về UC cha tổng quát.
- [ ] Các Actor gắn với use case đều là tác nhân chủ động trực tiếp thực hiện hoặc tương tác.
- [ ] Không biến các tiến trình ngầm (cron job, token rotation) hoặc tầng hiển thị (bộ lọc ẩn/hiện) thành use case tương tác người dùng.

### 3. Cú pháp Mermaid Diagram (Diagram Rendering Safety)
- [ ] Tất cả các nhãn mũi tên chứa ký tự đặc biệt đều được bọc trong cặp nháy kép `|"<<include>>"|`, `|"<<extend>>"|`, `|"<<generalization>>"|`.
- [ ] Không có ký tự xuống dòng `\n` trong nhãn mũi tên.
- [ ] Tất cả các label node có chứa dấu ngoặc đơn `()` đều được bọc trong dấu nháy kép `(["..."])` hoặc `["..."]`.
- [ ] Không dùng các thẻ HTML formatting như `<b>`, `<i>` trong nội dung node.
- [ ] Không chứa ký tự placeholder `{{` hoặc `}}` bên trong code block Mermaid.
- [ ] Node ID là duy nhất trên toàn bộ file.

### 4. Ngôn ngữ & Định dạng (Language & Conventions)
- [ ] Ngôn ngữ chính: Tiếng Việt văn phong kỹ thuật chuẩn mực, rõ ràng, mạch lạc.
- [ ] Thuật ngữ chuyên môn và các trạng thái hệ thống giữ nguyên tiếng Anh chuẩn (`ACTIVE`, `BANNED`, `username`, `JWT`, `OAuth`, `Generalization`, v.v.).
- [ ] Đường dẫn file tuân thủ định dạng markdown link `file:///...`.

## Hoàn tất quy trình

1. Cập nhật dòng **Trạng thái** trong bảng Metadata ở đầu file từ `Đang thực hiện` thành `Hoàn thành`.
2. Thông báo với người dùng tài liệu Use Case đã hoàn tất và sẵn sàng phục vụ cho giai đoạn thiết kế kỹ thuật tiếp theo.
