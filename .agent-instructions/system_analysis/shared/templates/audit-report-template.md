# Báo cáo audit — ISH-AUD-Mxx-r<n>
<!-- [Vietnamese Doc] -->

| Mã báo cáo | ISH-AUD-Mxx-r<n> |
| --- | --- |
| SR được audit | ISH-SR-Mxx, phiên bản x.y |
| Routing | ISH-RT-Mxx, phiên bản x.y |
| Vòng | n (hoặc v1 cho đợt xác minh, rel<n> cho xác minh phát hành) |
| Lượt đã gộp | P1, P2, P3 (hoặc `PASS=ALL` — ba lượt không độc lập hoàn toàn; hoặc VERIFY, hoặc RELEASE) |
| Ngày | YYYY-MM-DD |
| Auditor | Agent Auditor độc lập |
| Kết luận | Đạt | Chưa đạt |

## 1. Tóm tắt

<Ba–năm câu: kết luận và lý do chính.>

| Lớp \ Mức | Cao | Trung bình | Thấp |
|---|---|---|---|
| DEFECT | 0 | 0 | 0 |
| CONFLICT | 0 | 0 | 0 |
| GAP | 0 | 0 | 0 |
| OBSERVATION | 0 | 0 | 0 |

## 2. Phạm vi và phương pháp

- Tệp đã đọc (kèm phiên bản/ngày): …
- Nguồn đã đọc: DRAFT §…; registers (ngày đọc); các mục OWNED/REFERENCING/KEYWORD đã đọc.
- Script đã chạy: `inventory.py`, `check_sr.py` (kèm đường dẫn đầu ra).
- Tính độc lập: ma trận độ phủ lập trước khi đọc Phụ lục A/routing; có/không nhận được thông tin từ Author (và đã không dùng).
- Giới hạn: những gì **không** kiểm được và lý do.

## 3. Kết quả kiểm tra tự động

ERROR = n, WARN = n, INFO = n. Các mã còn ERROR/WARN: …

## 4. Ma trận độ phủ nguồn → yêu cầu

| Nguồn | Mong đợi (Auditor) | Thực tế (SR / routing) | Kết quả | AUD |
|---|---|---|---|---|

Mục OWNED liệt kê đủ; mục REFERENCING/KEYWORD gom theo loại, ghi riêng mục có finding.

## 5. Phát hiện

### AUD-Mxx-01 — <tiêu đề ngắn>

| Lớp | DEFECT | Lớp phụ | — (bỏ nếu không có) | Mức | Cao | Checklist | CL-A02 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-Mxx-nnn.k (`ISH-SR-Mxx.md:dòng`)
- **Bằng chứng trong SR/routing:** "<trích nguyên văn>" (`tệp:dòng`)
- **Bằng chứng trong nguồn:** "<trích nguyên văn>" (`tệp:dòng`, ID nguồn)
- **Vấn đề:** <một–hai câu>
- **Hệ quả nếu không sửa:** <một câu>
- **Hướng xử lý (Author quyết cách viết):** <một–hai câu>
- **Trạng thái (từ vòng 2):** Mở | Đã sửa | Sửa chưa đủ | Chưa sửa | Chuyển stakeholder

## 6. Cần stakeholder quyết

Mỗi vấn đề một khối theo khuôn §8.3; xếp vấn đề chặn trước.

Vấn đề: …
Nguồn: …
Lựa chọn: A) … — hệ quả …   B) … — hệ quả …
Đề xuất: … vì …
Liên quan: AUD-Mxx-nn

## 7. Kết quả checklist

| Mã | Kết quả | AUD / ghi chú |
|---|---|---|
| CL-A01 | Đạt | |
| … | | |

## 8. Vòng trước (chỉ vòng 2)

| AUD vòng 1 | Trạng thái vòng 2 | Bằng chứng |
|---|---|---|

Hồi quy mới: …

## 9. Hồ sơ xác minh

- Lệnh `grep` đã chạy cho từng finding (`lệnh → số kết quả`).
- Finding bị loại hoặc chỉnh sửa ở Bước 6 và lý do.
- Mục chuyển lượt (từ mục 6 của ba tệp lượt): dòng nào đã thành finding (mã `AUD-Mxx-nn`), dòng nào bị loại và lý do.
