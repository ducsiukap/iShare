# Bước 5 — Viết yêu cầu

## Mục đích

Viết cho mỗi chức năng: yêu cầu cấp trên, lý do, và đủ yêu cầu cấp dưới cho cả luồng chính lẫn mọi điều kiện
ngoại lệ mà nguồn cho phép viết.

## Đầu vào

Mục 4.x, quy tắc, dữ liệu, trạng thái đã duyệt; bảng C.1.

## Việc làm

1. Với mỗi chức năng `FR-Mxx-nn`:
   - **Yêu cầu cấp trên**: một câu nêu năng lực của chức năng.
   - **Lý do**: lấy từ lời văn nguồn (DEC/QA của chức năng → mục tiêu module ở draft → mô tả ở module-registry).
     Không có thì ghi "Nguồn chưa nêu lý do." Không tự viết lý do.
2. **Yêu cầu cấp dưới**, ID `FR-Mxx-nn.mm`, mỗi câu một hành vi, theo mẫu EARS tiếng Việt ở `output/fr-template.md`.
   Thứ tự: luồng chính trước, rồi các điều kiện ngoại lệ. Quét đủ các điều kiện sau cho từng chức năng:
   - người thực hiện không có quyền (đối chiếu 4.3);
   - dữ liệu nhập không hợp lệ hoặc vượt giới hạn (đối chiếu BR);
   - đối tượng đang ở trạng thái không cho phép (đối chiếu bảng trạng thái);
   - đối tượng không tồn tại, đã bị xóa hoặc đã bị loại;
   - thao tác lặp lại hoặc trùng;
   - AI không khả dụng hoặc bị tắt (chỉ với chức năng có AI).
3. Với mỗi điều kiện, đúng một trong bốn cách:
   - nguồn nói → viết, căn cứ **Nói thẳng**;
   - suy ra bắt buộc → viết, căn cứ **Suy ra**, ghi phép suy luận ở Phụ lục A;
   - nguồn không nói nhưng hành vi đó đã có trong nguồn và hệ quả có thể khác nhau → không cấp ID, ghi
     `[GAP: … — Q-nn]` dưới bảng và thêm câu hỏi ở B.1 (kèm đề xuất suy từ dữ liệu hiện có);
   - không áp dụng cho chức năng này → bỏ qua.
4. **Được suy ra**: vi phạm "tối đa / tối thiểu / chỉ" ⇒ từ chối; "chỉ X được làm" ⇒ người khác bị từ chối;
   hệ quả trực tiếp của một quan hệ đã nêu (gộp A vào B ⇒ bài của A thuộc B).
   **Không được suy ra**: con số, ngưỡng, thời hạn, quyền mới, ngoại lệ mới, thông điệp hiển thị cụ thể.
5. Điền các cột còn trống: 4.3 cột Yêu cầu, CRUD (đổi ID chức năng thành ID cấp dưới cụ thể), cột Yêu cầu của
   bảng trạng thái, mục 5.n Giao tiếp với module khác (Cung cấp / Dùng, dựa vào mục Phụ thuộc và dependency
   keywords), mục AI (hoặc "Không áp dụng.").
6. Phụ lục A cho **mọi** ID mới. C.1 cột Dùng ở cho mọi nguồn Sở hữu hiện hành; nguồn chuyển sang module khác ghi
   "Chuyển Myy"; nguồn không dùng ghi "Không áp dụng: <lý do>".
7. Chạy `lint_fr.py` (không `--final`) và `trace_check.py`. Sửa hết ERROR. WARN giữ lại phải có lý do.

## Ghi vào tệp FR

Mục 4.3, 5.x, 5.n (CRUD, trạng thái, giao tiếp, AI), Phụ lục A, B.1, C.1.

## Tự kiểm trước cổng

- Mỗi ô ✗ ở 4.3 có một yêu cầu từ chối.
- Mỗi BR được ít nhất một yêu cầu dùng tới.
- Mỗi chuyển trạng thái có yêu cầu.
- Không câu nào có chi tiết cài đặt hay từ mơ hồ (lint REQ-03, REQ-04).

## Trình ở cổng

Đi theo từng chức năng: số yêu cầu cấp dưới, các yêu cầu **Suy ra** (để người dùng xác nhận phép suy luận),
các `[GAP]` mới. Sau đó kết quả hai tool và WARN giữ lại kèm lý do.

## Không làm

Không tự điền chỗ `[GAP]`. Không viết yêu cầu cho hành vi mà nguồn không hề nhắc tới.
