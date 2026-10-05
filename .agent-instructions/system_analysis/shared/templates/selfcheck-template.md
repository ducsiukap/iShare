# Selfcheck — ISH-SR-Mxx phiên bản x.y
<!-- [Vietnamese Doc] -->

Ngày: YYYY-MM-DD · Tác giả: Phạm Văn Đức

Tệp làm việc của Author (RULES §10: Author không tự chấm 45 mục checklist; Auditor chấm). Tệp này ghi bốn phần việc của Author và các điểm cần stakeholder biết.

## 1. Kết quả script

| Lệnh | Kết quả |
|---|---|
| `inventory.py` (chạy lại sau lần ghi register cuối) | OWNED=n, REFERENCING=n, ID kế tiếp: ISS-nnn, QA-nnn, DEC-nnn |
| `check_sr.py --inventory … --tests …` | ERROR=0, WARN=n, INFO=n; n ca kiểm cho n yêu cầu cấp dưới |

## 2. Ca kiểm (RULES §11)

| Việc | Kết quả |
|---|---|
| Mọi yêu cầu cấp dưới có ít nhất một ca (TST-01) | n/n |
| Cột "Giả định cần thêm" còn nội dung | 0; điều nguồn chưa nói đã bỏ khỏi yêu cầu và ghi ở mục 3 |
| Mỗi công thức, cửa sổ thời gian, hằng số có ví dụ số tính tay (hai thực thể, một thực thể ngoài lề) | Liệt kê ID yêu cầu và ID ca |
| Yêu cầu ở mục 5.2 có ca "Chuyển trạng thái" (TST-07) | n/n |
| Đã đọc lại từng "Then": suy ra được duy nhất từ câu yêu cầu, không cần giả định | Có / ngoại lệ: … |

## 3. Quét khung hành vi (RULES §4.7)

Mỗi tính năng một khối bảy dòng; loại ∈ {a nguồn nêu, b suy ra, c nguồn im lặng, d không áp dụng}.

| Tính năng | Câu hỏi | Loại | Kết quả (ID yêu cầu, ID câu hỏi/`OP`, hoặc lý do) |
|---|---|---|---|
| 5.3 Gán Topic | 1 Ai được làm | a | ISH-M05-001 (mọi người dùng) |
| 5.3 Gán Topic | 5 Hệ quả lên đối tượng liên quan | c | Không đặc tả: nguồn chưa nói (RULES §3.3) |

## 4. Rà hồi quy (chỉ khi sửa; RULES §8.5)

Một dòng cho mỗi ID mới, đổi nội dung hoặc bị bỏ. Ô ∈ {Đạt, Không đạt, Không áp dụng} kèm bằng chứng ngắn; không ghi `Đạt` cho ô chưa làm.

| ID | Thay đổi | RG-1 cấp trên | RG-2 cùng đối tượng | RG-3 "chỉ" | RG-4 OP mở | RG-5 tham chiếu ID bỏ | RG-6 Lịch sử | RG-7 ca kiểm |
|---|---|---|---|---|---|---|---|---|
| ISH-M05-007.7 | Mới | Đạt: cấp trên 007 bao quát | Đạt: so 011.8, 007.1 | Không áp dụng | Đạt | Không áp dụng | Đạt | Đạt: T-0nn |

## 5. WARN giữ lại

| Mã WARN | ID | Lý do giữ |
|---|---|---|

## 6. Điểm đã raise cho stakeholder

| OP / ISS / QA | Vấn đề | Trạng thái |
|---|---|---|
