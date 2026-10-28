---
name: use-case-analysis
description: >
  Xác định actor và use case tổng quan, đặc tả use case chi tiết từ FR đã duyệt
  của iShare cho một module hoặc phạm vi toàn dự án, kèm truy vết và kiểm tra UML.
  Dùng khi tạo, sửa hoặc review tài liệu US và mô hình use case; không dùng để
  thiết kế UI, CSDL hoặc bổ sung yêu cầu sản phẩm.
---

# Phân tích use case iShare

[Vietnamese Doc] — Hướng dẫn và tài liệu US viết bằng tiếng Việt, giữ thuật ngữ cần thiết.

Chuyển FR đã duyệt thành mô hình mục tiêu–hành vi và đặc tả phục vụ thiết kế,
kiểm thử. Tuân theo [hướng dẫn repository](../../README.md) và
[System Analysis](../../phases/system-analysis.md). Bảy bước dưới đây áp dụng
khi sản xuất US; khi review hoặc sửa chính bộ skill, không chạy các cổng sản xuất US.

## Phạm vi và đầu ra

- Đọc [input/INPUTS.md](input/INPUTS.md); FR liên module được đọc khi có giao tiếp
  liên quan. Không suy yêu cầu sản phẩm từ ví dụ hoặc tài liệu phương pháp.
- Một module: `docs/specs/us/US-Mxx.md`. Tổng quan dự án:
  `docs/specs/us/US-overview.md`, danh mục actor/UC chung và view tổng quan;
  chỉ đặc tả sâu UC thuộc phạm vi được yêu cầu, không tự tạo lại mọi US module.
- Dùng [output/us-template.md](output/us-template.md). Tái sử dụng ID đã duyệt.
  US-M01–M04 hiện có cần được đối chiếu; **không phải chuẩn vàng**.
- Ví dụ có giới hạn phạm vi: [references/worked-example.md](references/worked-example.md).

## Quyết định phân tích

1. **Boundary trước actor.** Actor là vai trò ngoài subject, có thể là người hoặc
   hệ thống khác. Phân biệt actor chính/hỗ trợ với quyền truy cập. Không biến
   chính iShare hoặc module nội bộ thành actor ngoài iShare.
2. **Mục tiêu trước chức năng.** Ghi mức Summary / User goal / Subfunction.
   Không ấn định số UC, số UC con hoặc số FR tối thiểu mỗi UC. Package/nhóm
   chức năng không tự trở thành UC cha.
3. **Mục tiêu gắn kết, không phải từng thao tác UI.** FR có thể được giữ, gộp,
   tách hoặc phân bổ vào UC, bước, nhánh, điều kiện, BR và tác vụ tự động.
   Không bắt buộc mỗi FR tạo oval. Tên dùng động từ và đối tượng, không đếm
   máy móc động từ hoặc cấm từ nối trong cụm danh từ.
4. **Đặc tả trước quan hệ.** Viết trigger, điều kiện, luồng chính, thay thế/ngoại
   lệ và kết quả trước khi tách UC hỗ trợ. UC có thể không có quan hệ UC–UC.
5. **Quan hệ có bằng chứng.** Theo
   [references/modeling-rules.md](references/modeling-rules.md):
   include là chèn hành vi, không phải tiền điều kiện/thứ tự; extend cần
   extension point và không tự phát sinh từ mọi nhánh; generalization cần
   hành vi chung và chuyên biệt hóa, không bắt buộc cha abstract.
6. **Nguồn kiểm chứng được.** Truy vết tới mã FR chi tiết và BR còn hiệu lực,
   đọc đúng nội dung mã. Mọi hành vi/quan hệ có căn cứ; bất đồng/thiếu nguồn
   ghi vào điểm cần làm rõ, chuyển về phân tích yêu cầu, không tự bù giả định.
7. **Hành vi tự động vẫn được đặc tả.** Phân biệt hạ tầng kỹ thuật với tác vụ
   nghiệp vụ theo sự kiện/thời gian. Ghi trigger, điều kiện, kết quả và quy
   tắc dữ liệu, không chỉ gắn nhãn “tiến trình ngầm” để coi đã bao phủ.
8. **ID ổn định.** UC mới: `UC-M01-001`; actor: `ACT-001`; tác vụ:
   `AUT-M01-001`; quy tắc: `RULE-M01-001`. Giữ ID qua đổi tên/view.
   UC dùng chung có một ID, không đặt ID theo cha hoặc loại quan hệ.
9. **Tool không thay BA review.** Theo [tools/README.md](tools/README.md)
   và [references/diagram-rules.md](references/diagram-rules.md). Phân biệt
   tham chiếu tồn tại, render thành công và đúng nghiệp vụ.

## Bảy bước và cổng xác nhận

| Bước | Đọc khi thực hiện | Kết quả |
|---|---|---|
| 1 | [01-extract-functions.md](steps/01-extract-functions.md) | Baseline, boundary, actor, kiểm kê FR |
| 2 | [02-identify-core-ucs.md](steps/02-identify-core-ucs.md) | Mục tiêu, mức UC, ownership và danh mục |
| 3 | [03-map-actors.md](steps/03-map-actors.md) | Đặc tả luồng, điều kiện và kết quả |
| 4 | [04-decompose-sub-ucs.md](steps/04-decompose-sub-ucs.md) | Quyết định tách/tái sử dụng và quan hệ |
| 5 | [05-build-traceability.md](steps/05-build-traceability.md) | Truy vết hai chiều, chi tiết và liên module |
| 6 | [06-write-diagrams.md](steps/06-write-diagrams.md) | View tổng quan/chi tiết, kiểm tra render |
| 7 | [07-assemble-verify.md](steps/07-assemble-verify.md) | Review và hồ sơ chờ phê duyệt |

Mặc định mỗi lượt hoàn tất một bước, ghi tiến độ rồi dừng chờ xác nhận rõ ràng.
Câu hỏi hoặc im lặng không phải đồng ý. Cổng này không ngăn việc cập nhật bộ
skill khi người dùng đã yêu cầu sửa skill.

Khi tiếp tục, đọc metadata/tiến độ: `current_step`, `completed_steps`,
`approved_steps`, `source_baseline`, `skill_version` và trạng thái tài liệu.
Thiếu tiến độ ở tài liệu cũ: đối chiếu nội dung/lịch sử xác nhận, không tự
coi đã được duyệt. FR đổi: đánh dấu phần chịu tác động, làm lại bước liên quan
và xác nhận lại; giữ dấu vết baseline đã duyệt trước đó.

Tin nhắn cổng:

```text
Bước N/7 — <phạm vi>: xong, chờ xác nhận.
Kết quả: <mục tiêu/luồng/quan hệ và vị trí đã ghi>.
Cần review: <quyết định, thiếu nguồn, lỗi hoặc giới hạn kiểm tra>.
Kiểm tra: <lệnh/kết quả thực tế; phần chưa kiểm tra>.
Trả lời “ok” để sang bước kế tiếp hoặc nêu chỗ cần sửa.
```

Trạng thái: `Đang soạn` → `Chờ duyệt` → `Đã duyệt`. Xong checklist bước 7
chỉ chuyển Chờ duyệt; chỉ ghi Đã duyệt khi người dùng chấp nhận kết quả cuối.
Phiên bản skill hiện hành: **2.0**.
