# use-case-analysis — Hướng dẫn sử dụng

[Vietnamese Doc]

Phân tích FR đã duyệt thành danh mục use case tổng quan và đặc tả chi tiết
phục vụ thiết kế, kiểm thử iShare.

## Cách gọi

- “Xác định use case tổng quan toàn dự án từ docs/specs/fr.”
- “Đặc tả use case M02 theo skill use-case-analysis.”
- “Review US-M01 với FR hiện hành, giữ ID đã duyệt.”

Đầu vào là FR đã chốt và FR liên quan. Đầu ra module:
`docs/specs/us/US-Mxx.md`; tổng quan: `docs/specs/us/US-overview.md`.
Phạm vi một phần được ghi rõ, không báo hoàn tất toàn module.

## Quy trình

1. Baseline, boundary và actor.
2. Mục tiêu, mức UC và danh mục.
3. Trigger, điều kiện, luồng chính/thay thế/ngoại lệ, kết quả.
4. Quyết định tách UC và quan hệ UML.
5. Truy vết chi tiết và liên module.
6. Sơ đồ và kiểm tra render.
7. Review, trình duyệt cuối.

Mỗi bước có xác nhận; tiến độ/baseline nằm trong US. Checklist kỹ thuật
hoàn tất không tự có nghĩa stakeholder đã phê duyệt.

## Các nguyên tắc

- Không có số UC cố định hoặc yêu cầu dùng đủ ba loại quan hệ.
- FR có thể là bước, điều kiện, quy tắc hoặc tác vụ tự động; không cần mỗi FR
  thành UC riêng. “UC chính/con” là cách tổ chức view, không mặc định cây UML.
- Viết luồng trước quan hệ. Nhánh điều kiện không tự đồng nghĩa extend.
- Giữ ID ổn định xuyên view; đọc và kiểm tra ý nghĩa nguồn.
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

