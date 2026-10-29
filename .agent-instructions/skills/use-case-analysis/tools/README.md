# Kiểm tra tài liệu US

[Vietnamese Doc]

check_us.py dùng Python 3.10+ và thư viện chuẩn, không cần cài dependency.

## Lệnh

Chạy từ repository root:

```text
python -X utf8 .agent-instructions/skills/use-case-analysis/tools/check_us.py docs/specs/us/US-M01.md
python -X utf8 .agent-instructions/skills/use-case-analysis/tools/check_us.py docs/specs/us/US-M01.md --final
python -X utf8 .agent-instructions/skills/use-case-analysis/tools/check_us.py .agent-instructions/skills/use-case-analysis/references/worked-example.md --scope FR-M01-07
python -X utf8 -m unittest discover -s .agent-instructions/skills/use-case-analysis/tools -p test_check_us.py
```

Có thể dùng --repo để chọn repository nguồn khi kiểm tra bản sao độc lập.
Exit 1 có lỗi cấu trúc; exit 0 không chứng minh nghiệp vụ đúng.
Không chạy --final trước bước 7 để rồi suy rằng stakeholder đã duyệt.

## Bảng và marker

Template là hợp đồng đầu vào. Mỗi marker xuất hiện một lần:
uc:document, sources, actors, catalog, decomposition, extension-points, relations,
trace, diagrams và uc:spec <UC-ID> cho mỗi UC cần chi tiết. Ngay sau marker là bảng
Markdown với header được template quy định. Không xóa marker khi sửa tài liệu.
Bảng không áp dụng giữ header và dòng phân cách, không thêm dòng giả.

- key/value của document chứa mode, modules, scope, status, tiến độ, baseline.
- scope=ALL cho module/overview. Với partial, scope là danh sách mã và lệnh
  phải có --scope tương ứng; công cụ in rõ PARTIAL.
- sources dùng đường dẫn repo-relative docs/specs/fr/FR-Mxx.md và version.
- catalog có tier=core/sub riêng với level. decomposition có core/sub/rationale/
  sources: mỗi core có sub, mỗi sub có core, sub dùng chung giữ một ID.
- mode overview chỉ catalog core, có bảng module-models (module/path/baseline)
  trỏ tới US module từ repo root; tool đối chiếu ID/tên/owner và baseline.
- catalog nguồn FR/BR viết đầy đủ, anchor local phải tồn tại; UC liên module
  có brief/anchor trong tài liệu hiện tại và link tới đặc tả owner.
- trace một dòng mỗi requirement; target gồm các anchor local ngăn bằng dấu
  phẩy. Bước chi tiết cần anchor riêng; không dùng heading slug ngầm.
- relation at: include → anchor bước nguồn; extend → ID extension point của
  base; generalization → anchor hợp đồng cha. return_to cho include/extend là
  anchor cơ sở hoặc END: kết quả. Endpoint dùng UC ID.
- Đặc tả không cần actor hỗ trợ dùng dấu -; điều kiện không áp dụng viết rõ
  Không áp dụng cùng lý do thay vì để thiếu thông tin.

## Những gì kiểm được

- Baseline FR có thật/đã chốt/đúng phiên bản, mã FR/BR tồn tại và còn hiệu lực.
- Thiếu mapping cho nhóm FR, FR chi tiết, BR thuộc scope; retired không tự
  thành yêu cầu hiện hành. Draft báo WARN; --final báo ERROR.
- Overview chỉ kiểm kê nhóm, luôn cảnh báo không phải bao phủ chi tiết.
- ID/anchor trùng, actor không khai báo, hợp đồng thiếu, catalog/spec lệch.
- Module thiếu core/sub, core không có sub, sub mồ côi, mapping sai tier;
  overview đưa sub vào hoặc core khác với US module nguồn.
- Endpoint relation, anchor điểm gọi, extension point đúng base, guard/return,
  cycle generalization; include cycle được cảnh báo để review.
- Tiến độ/phê duyệt nhất quán; --final yêu cầu ghi nhận semantic review và
  bằng chứng render. Mode partial nhỏ không sơ đồ có thể not-applicable.
- Tài liệu cũ chưa có marker được báo thiếu cấu trúc, không tự chuyển đổi.

## Giới hạn

Tool không đọc hiểu chất lượng mục tiêu, sự đúng nghĩa của mapping, tính đầy
đủ của luồng hoặc khả năng thay thế của generalization. Nó không kiểm chứng
sự thật của xác nhận người dùng, không chạy renderer, không xác minh hình hay
sơ đồ khớp mọi bảng. Cần review riêng theo modeling-rules và diagram-rules.
Các record pass/approval_evidence phải do người thực hiện ghi trung thực.

Bảng diagrams có view=core/detail/system. --final cho module cần view core và
**một dòng detail cho mỗi core**; focus là ID core, members là các UC trên hình.
Tool kiểm focus hợp lệ, core và đủ sub theo decomposition xuất hiện trong
members; overview cần view system. Mỗi view có bằng chứng render.
Phải review riêng từng cạnh core–sub/sub–sub giữa bảng relation và hình; tool
không suy ra cạnh từ members hoặc xác nhận nội dung file hình.

Tests dùng FR/US tổng hợp trong thư mục tạm, không sửa FR hoặc US của dự án.
