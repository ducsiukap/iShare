# Tệp lượt — ISH-AUD-Mxx-r<n> · lượt P<k> (<tên lượt>)
<!-- [Vietnamese Doc] -->

| Trường | Giá trị |
|---|---|
| Module | Mxx |
| Vòng | n |
| Lượt | P1 / P2 / P3 |
| SR được audit | ISH-SR-Mxx, phiên bản x.y (ngày) |
| Routing | ISH-RT-Mxx, phiên bản x.y |
| Tóm tắt Author đã nhận và không dùng | Không có / Có (đã bỏ qua) |

## 1. Phát hiện nháp

Mỗi finding: ID nháp `P<k>-nn` (MERGE sẽ đặt `AUD-Mxx-nn`).

### P<k>-01 — <tiêu đề ngắn>

| Lớp | DEFECT | Lớp phụ | — (bỏ nếu không có) | Mức đề xuất | Cao | Checklist | CL-A02 |
|---|---|---|---|---|---|---|---|

- **Vị trí:** ISH-Mxx-nnn.k (`ISH-SR-Mxx.md:dòng`) hoặc "không có vị trí — chính là vấn đề".
- **Bằng chứng trong SR/routing:** "<trích một dòng>" (`tệp:dòng`) hoặc kết quả tìm vắng mặt.
- **Bằng chứng trong nguồn:** "<trích một dòng>" (`tệp:dòng`).
- **Vấn đề:** …
- **Hệ quả nếu không sửa:** …
- **Hướng xử lý (Author quyết cách viết):** …
- **Khuôn hỏi stakeholder** (chỉ GAP mơ hồ và CONFLICT): Vấn đề / Nguồn / Lựa chọn + hệ quả / Đề xuất.

## 2. Kết quả checklist của lượt

| Mã | Kết quả | Finding / ghi chú |
|---|---|---|
| CL-… | Đạt / Không đạt / Không áp dụng / Không kiểm được | P<k>-nn hoặc bằng chứng ngắn |

(đủ **mọi** mục của lượt, theo bảng ở `RULES` §8.6)

## 3. Kết quả kiểm tra tự động

ERROR = n, WARN = n, INFO = n. Lệnh đã chạy: `…`. Mỗi mã còn ERROR/WARN: …

## 4. Hồ sơ xác minh

- `grep -n -F "…" <tệp>` → n kết quả (dòng …)
- Finding bị loại hoặc chỉnh: …

## 5. Phạm vi và giới hạn không kiểm được

…

## 6. Chuyển lượt khác

(Mỗi dòng: vấn đề một câu + lượt nên chấm + mã `CL-xxx` + trích đoạn nguyên văn kèm `tệp:dòng`, để MERGE kiểm chứng và lập finding. Không lập finding, không chấm mục của lượt khác.)

## 7. Chỉ lượt P1 — ma trận

Ma trận ở `WORK/coverage-Mxx-r<n>.md`; tóm tắt các hàng có finding: …

## 8. Chỉ lượt P3 — bảng ca kiểm độc lập

Tệp `WORK/audit-tests-Mxx-r<n>.md`, một bảng, cột cố định:

| ID ca | Nguồn | Loại | Given | When | Then theo nguồn | Nguồn xác định? | ID yêu cầu SR | SR xác định? | Then theo ca kiểm của Author | Đối chiếu |
|---|---|---|---|---|---|---|---|---|---|---|
| A-001 | DEC-051 | Biên | Bài có 5 thẻ | Thêm thẻ thứ 6 | Nguồn chỉ nói "tối đa 5": từ chối là suy ra bắt buộc | Có | ISH-M05-004.2 | Có | Từ chối thẻ thứ 6 | Trùng |

`Nguồn xác định?`/`SR xác định?` ∈ {Có, Mơ hồ, Không}; `Đối chiếu` ∈ {Trùng, Khác, Không có ca của Author}. Hàng `Mơ hồ` ghi hai kết quả ở cột "Then theo nguồn" (ví dụ "cách 1: 0 điểm; cách 2: 30 điểm").

## 9. Chỉ lượt P3 — quét khung hành vi

Phần thêm vào `WORK/audit-tests-Mxx-r<n>.md`, một bảng, cột cố định:

| Tính năng | Câu hỏi (1–7, RULES §4.7) | Nguồn nói gì | Loại (a/b/c/d) | SR (ID yêu cầu hoặc "—") | Selfcheck của Author (loại) | Kết luận |
|---|---|---|---|---|---|---|
| Quản trị Chuyên mục | 5 Hệ quả lên đối tượng liên quan: Chuyên mục nguồn sau gộp | Nguồn im lặng | c | — | c (không đặc tả) | Không phải finding (RULES §3.3) |
