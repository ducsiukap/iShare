---
name: use-case-analysis
description: >
  Xác định UC chính và UC con cho từng module iShare từ FR đã duyệt; tổng hợp
  UC chính thành sơ đồ toàn hệ thống và UC con thành sơ đồ chi tiết module,
  mỗi UC chính có một sơ đồ chi tiết riêng thể hiện cả chính–con và con–con,
  kèm đặc tả, truy vết và kiểm tra UML.
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
- Một module: `docs/specs/us/US-Mxx.md`, bắt buộc có **UC chính, UC con và bảng
  phân rã chính → con**, sơ đồ UC chính module và **một sơ đồ chi tiết cho từng
  UC chính**. Sơ đồ chi tiết có node UC chính, toàn bộ UC con liên quan, actor,
  các quan hệ UML chính–con và con–con đã xác định; không chỉ có nhóm UC con.
- Toàn hệ thống: `docs/specs/us/US-overview.md`, **tổng hợp UC chính đã xác định
  ở từng module**, giữ ID/owner/actor và trỏ về tài liệu module. Không lập một
  danh sách mục tiêu khác thay cho các UC chính module, không đưa UC con vào
  sơ đồ tổng quan hệ thống.
- Thực hiện module nào thì hoàn thiện hai tầng của module đó; chỉ tổng hợp toàn
  hệ thống khi được yêu cầu. Module chưa phân tích ghi còn thiếu, không tự bịa UC.
- Dùng [output/us-template.md](output/us-template.md). Tái sử dụng ID đã duyệt.
  US-M01–M04 hiện có cần được đối chiếu; **không phải chuẩn vàng**.
- Ví dụ có giới hạn phạm vi: [references/worked-example.md](references/worked-example.md).

## Quyết định phân tích

**Hợp đồng đầu ra hai tầng là bắt buộc:**

| Tầng | Vai trò trong tài liệu | Đầu ra sơ đồ |
|---|---|---|
| UC chính (`tier=core`) | Năng lực/mục tiêu nghiệp vụ bao quát của từng module; nêu actor, giá trị và phạm vi | Tổng quan module và tổng quan toàn hệ thống |
| UC con (`tier=sub`) | Mục tiêu cụ thể/hành vi nghiệp vụ gắn kết thuộc một hoặc nhiều UC chính | Sơ đồ chi tiết module và đặc tả chi tiết |

Mọi module hoàn chỉnh phải có cả hai tầng; mỗi UC chính có ít nhất một UC con,
mỗi UC con truy được về ít nhất một UC chính. Không đặt quota 3–6 UC chính.
UC con dùng chung có một ID, nhiều dòng mapping nếu thuộc nhiều UC chính.
`tier` là vai trò trong bộ đầu ra, **độc lập** với `level` (Summary / User goal /
Subfunction). UC chính có thể ở Summary hoặc User goal; UC con có thể là User
goal hoặc Subfunction. “Thuộc UC chính” là phân rã/ánh xạ phục vụ phân tích,
không tự tạo generalization, include hoặc extend. Vẽ các mũi tên UML chỉ khi
đặc tả chứng minh quan hệ; có thể biểu diễn nhóm bằng package và bảng mapping.

1. **Boundary trước actor.** Actor là vai trò ngoài subject, có thể là người hoặc
   hệ thống khác. Phân biệt actor chính/hỗ trợ với quyền truy cập. Không biến
   chính iShare hoặc module nội bộ thành actor ngoài iShare.
2. **Mục tiêu trước chức năng.** Ghi mức Summary / User goal / Subfunction.
   Không ấn định số lượng ngoài yêu cầu hai tầng. Package/nhóm chức năng không
   tự trở thành UC cha UML; UC chính phải có giá trị nghiệp vụ và phạm vi rõ.
3. **Mục tiêu gắn kết, không phải từng thao tác UI.** FR có thể được giữ, gộp,
   tách hoặc phân bổ vào UC, bước, nhánh, điều kiện, BR và tác vụ tự động.
   Không bắt buộc mỗi FR tạo oval. Tên dùng động từ và đối tượng, không đếm
   máy móc động từ hoặc cấm từ nối trong cụm danh từ.
4. **Phân rã rồi chứng minh quan hệ.** Xác định UC con, viết trigger, điều kiện,
   luồng chính, thay thế/ngoại lệ và kết quả trước khi quyết định quan hệ UML.
   Đầy đủ mapping chính–con không có nghĩa phải có mũi tên UC–UC.
5. **Quan hệ có bằng chứng.** Theo
   [references/modeling-rules.md](references/modeling-rules.md):
   include là chèn hành vi, không phải tiền điều kiện/thứ tự; extend cần
   extension point và không tự phát sinh từ mọi nhánh; generalization cần
   hành vi chung và chuyên biệt hóa, không bắt buộc cha abstract.
   Xét cả cặp core–sub lẫn sub–sub; UC con có thể là including/base/general
   trong một quan hệ khác. Không giới hạn mọi mũi tên vào một sơ đồ hình sao.
   Cặp không có quan hệ UML ghi kết luận và lý do, không tự nối để đủ hình.
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
| 2 | [02-identify-core-ucs.md](steps/02-identify-core-ucs.md) | UC chính và UC con ứng viên của từng module, actor/owner |
| 3 | [03-map-actors.md](steps/03-map-actors.md) | Quy trình UC chính, đặc tả các UC con |
| 4 | [04-decompose-sub-ucs.md](steps/04-decompose-sub-ucs.md) | Chốt phân rã chính → con, tái sử dụng và quan hệ UML |
| 5 | [05-build-traceability.md](steps/05-build-traceability.md) | Truy vết hai chiều, chi tiết và liên module |
| 6 | [06-write-diagrams.md](steps/06-write-diagrams.md) | Tổng quan từ UC chính; mỗi UC chính một sơ đồ chi tiết chính–con/con–con |
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
Phiên bản skill hiện hành: **2.2**.
