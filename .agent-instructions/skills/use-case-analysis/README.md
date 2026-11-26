# use-case-analysis — Hướng dẫn sử dụng

[Vietnamese Doc]

Phân tích FR đã duyệt để xác định **UC chính và UC con trên từng module**.
UC chính dùng ghép sơ đồ tổng quan toàn hệ thống; UC con dùng xây sơ đồ chi tiết
module và đặc tả nghiệp vụ phục vụ thiết kế, kiểm thử.

## Cách gọi

- “Xác định use case tổng quan toàn dự án từ docs/specs/fr.”
- “Đặc tả use case M02 theo skill use-case-analysis.”
- “Review US-M01 với FR hiện hành, giữ ID đã duyệt.”

Đầu vào là FR đã chốt và FR liên quan. Đầu ra module:
`docs/specs/us/US-Mxx.md`; tổng quan: `docs/specs/us/US-overview.md`.
Phạm vi một phần được ghi rõ, không báo hoàn tất toàn module.
V2.3 phân biệt overview full (mọi core trong scope) và selected (tập core được
chọn từ module hiện có). Selected ghi lý do selected/excluded cho mọi core,
không tạo UC tổng quan mới, không nâng sub và không nhận bao phủ toàn bộ FR.
Tổng quan có một boundary iShare, không chia khối module con.

Mỗi sơ đồ chỉ bàn giao **một file SVG** và nhúng/link trong tài liệu US.
Không tạo bộ ba SVG + PNG + PlantUML; file nguồn/render trung gian chỉ nằm
trong workspace agent khi cần để tạo hoặc kiểm tra SVG.

## Quy trình

1. Baseline, boundary và actor.
2. UC chính và UC con ứng viên của từng module.
3. Quy trình UC chính và đặc tả từng UC con.
4. Chốt bảng UC chính → UC con, tái sử dụng và quan hệ UML.
5. Truy vết chi tiết và liên module.
6. Tổng quan từ UC chính; mỗi UC chính có một sơ đồ chi tiết riêng gồm chính
   UC đó, các UC con và quan hệ chính–con/con–con; kiểm tra render.
7. Review, trình duyệt cuối.

Mặc định mỗi bước có xác nhận; nếu người dùng cho phép làm liên tục trong scope
hiện tại thì tiếp tục, vẫn giữ xác nhận thực hiện tách khỏi duyệt kết quả.
Tiến độ/baseline nằm trong US. Checklist kỹ thuật
hoàn tất không tự có nghĩa stakeholder đã phê duyệt.

Bản nháp mới mặc định ở workspace theo COMMON-RULES; docs/specs/us là đích bàn
giao hoặc nơi được người dùng yêu cầu trực tiếp. Cập nhật skill không tự migrate
US cũ, đổi version metadata, sửa SVG hoặc đóng các điểm chưa rõ của dự án.

## Các nguyên tắc

- Mỗi module có hai tầng core/sub và mapping đầy đủ; không ấn định số UC
  chính hoặc ép dùng đủ ba loại quan hệ UML.
- FR có thể là bước, điều kiện, quy tắc hoặc tác vụ tự động; không cần mỗi FR
  thành UC riêng. Phân rã chính–con bắt buộc nhưng không tự tạo mũi tên UML.
- Viết luồng trước quan hệ. Nhánh điều kiện không tự đồng nghĩa extend.
- Tổng quan hệ thống lấy nguyên core từ module, giữ ID/tên/owner và link về
  module. Không đưa sub lên sơ đồ tổng quan hệ thống.
- Thiếu yêu cầu được ghi để làm rõ, không tự bổ sung trong US.

## Tài liệu

- [SKILL.md](SKILL.md): entry point và cổng.
- [Đầu vào](input/INPUTS.md): nguồn, scope và baseline.
- [Quy tắc mô hình hóa](references/modeling-rules.md): quyết định và nguồn phương pháp.
- [Sơ đồ](references/diagram-rules.md): ký pháp, renderer, lệnh.
- [Ví dụ giới hạn phạm vi](references/worked-example.md): Đăng xuất và phản ví dụ.
- [Walkthrough quan hệ](references/relation-walkthrough-example.md): fixture phương pháp độc lập.
- [Kiểm soát chất lượng](references/quality-gates.md): chọn core, độ gắn kết, luồng, gap và owner.
- [Đánh giá hành vi](references/evaluation-scenarios.md): fixture/rubric khi kiểm chứng skill.
- [Template](output/us-template.md): đầu ra và các bảng kiểm tra bằng máy.
- [Công cụ](tools/README.md): cách chạy, mức kiểm tra và giới hạn.

US-M01–M04 cũ cần review trước khi dùng làm ví dụ; cập nhật skill không tự
cho phép viết lại các tài liệu này.

## Bước tiếp theo: scenario cho từng luồng nghiệp vụ

Khi đã có FR + US, dùng [scenarios](../scenarios/SKILL.md)
để kiểm kê các nhóm UC chi tiết và xây dựng scenario sáu phần cho từng luồng
nghiệp vụ, với dữ liệu minh họa và nhánh ngoại lệ đầy đủ. Skill này giữ mô
hình/ID của US, không thay thế quy trình phân tích use case hoặc tự phê duyệt US.

