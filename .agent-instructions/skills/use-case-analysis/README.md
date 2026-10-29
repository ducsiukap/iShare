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

## Quy trình

1. Baseline, boundary và actor.
2. UC chính và UC con ứng viên của từng module.
3. Quy trình UC chính và đặc tả từng UC con.
4. Chốt bảng UC chính → UC con, tái sử dụng và quan hệ UML.
5. Truy vết chi tiết và liên module.
6. Tổng quan từ UC chính; mỗi UC chính có một sơ đồ chi tiết riêng gồm chính
   UC đó, các UC con và quan hệ chính–con/con–con; kiểm tra render.
7. Review, trình duyệt cuối.

Mỗi bước có xác nhận; tiến độ/baseline nằm trong US. Checklist kỹ thuật
hoàn tất không tự có nghĩa stakeholder đã phê duyệt.

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
- [Template](output/us-template.md): đầu ra và các bảng kiểm tra bằng máy.
- [Công cụ](tools/README.md): cách chạy, mức kiểm tra và giới hạn.

US-M01–M04 cũ cần review trước khi dùng làm ví dụ; cập nhật skill không tự
cho phép viết lại các tài liệu này.

