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
trace, diagrams và uc:spec <UC-ID> cho mỗi UC cần chi tiết. Từ v2.3 bắt buộc thêm
uc:associations; overview v2.3 thêm uc:overview-selection. Ngay sau marker là bảng
Markdown với header được template quy định. Không xóa marker khi sửa tài liệu.
Bảng không áp dụng giữ header và dòng phân cách, không thêm dòng giả.

- key/value của document chứa mode, modules, scope, status, tiến độ, baseline.
- scope=ALL cho module/overview. Với partial, scope là danh sách mã và lệnh
  phải có --scope tương ứng; công cụ in rõ PARTIAL.
- sources dùng đường dẫn repo-relative docs/specs/fr/FR-Mxx.md và version.
  Role owner/normative/related là nguồn quy định hành vi; context chỉ tham khảo.
  V2.3 chặn dùng mã context làm căn cứ và nguồn normative/related chưa Đã chốt.
- catalog có tier=core/sub riêng với level. decomposition có core/sub/rationale/
  sources: mỗi core có sub, mỗi sub có core, sub dùng chung giữ một ID.
- mode overview chỉ catalog core, có bảng module-models (module/path/baseline)
  trỏ tới US module từ repo root; tool đối chiếu ID/tên/owner và baseline.
  V2.3 metadata overview_selection=full|selected; bảng overview-selection có
  id/decision/rationale/sources, đúng một dòng cho mỗi core nguồn. Full lấy đủ
  core; selected giữ tập con, catalog đúng tập selected. Không phải overview
  thì giữ bảng selection rỗng, overview_selection=- trong template.
- associations có actor/use_case/role/permission/sources; endpoint tồn tại,
  không trùng cặp actor–UC, đủ vai trò/điều kiện quyền/nguồn. Bảng có thể rỗng
  khi không có tương tác trực tiếp; BA phải xác nhận tính hợp lý, tool không
  suy ra association từ actor chính/hỗ trợ hoặc quyết định quyền.
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
  Selected chỉ yêu cầu các nhóm FR xuất hiện trong evidence của core được chọn;
  nhóm ngoài tập được cảnh báo, không tự coi là Đủ. Cùng nhóm FR có thể chia
  giữa nhiều core, nên BA vẫn phải đọc nội dung phần được biểu diễn.
- ID/anchor trùng, actor không khai báo, hợp đồng thiếu, catalog/spec lệch.
  Kiểm mẫu UC-Mxx-nnn/ACT-nnn, tên thiếu, current_step ngoài1–7 và relation trùng
  cùng type/endpoints/at/condition/return. Không tự cấm mọi cặp có nhiều loại cạnh.
- Module thiếu core/sub, core không có sub, sub mồ côi, mapping sai tier;
  overview đưa sub vào hoặc core khác với US module nguồn.
- Endpoint relation, anchor điểm gọi, extension point đúng base, guard/return,
  cycle generalization; include cycle được cảnh báo để review.
- Tiến độ/phê duyệt nhất quán; --final yêu cầu ghi nhận semantic review và
  bằng chứng render. Mode partial nhỏ không sơ đồ có thể not-applicable.
- Tài liệu cũ chưa có marker được báo thiếu cấu trúc, không tự chuyển đổi.

Parser FR nhận diện các heading lịch sử tài liệu/truy vết/phụ lục theo ý nghĩa,
không cắt cứng tại mục6. Heading nghiệp vụ như “Lịch sử xử lý hồ sơ” vẫn được
đọc. Có thể dùng cặp marker `fr:requirements-start` / `fr:requirements-end` để
chỉ rõ vùng active trong nguồn khi được phép cập nhật nguồn. Marker thiếu/lặp/
đảo thứ tự và mã active trùng được báo lỗi. Bố cục/heading lạ vẫn cần người đọc
xác nhận; parser không hiểu ngữ nghĩa mọi tiêu đề hoặc tự sửa FR.

## Tương thích phiên bản

Tài liệu2.2 giữ hợp đồng cũ; không tự chèn marker, đổi version hoặc migrate.
Thiếu bảng associations cũ chưa bị lỗi schema; artifact không hợp lệ ở tài liệu
cũ được cảnh báo. Mọi tài liệu vẫn được kiểm ID, tên, tiến độ và cạnh trùng.
Artifact repo-relative trong2.2 vẫn được nhận để không cần sửa tài liệu cũ.
Từ2.3 áp dụng schema mới và SVG thật cho kiểm --final. Version phải là số dạng
major.minor hoặc major.minor.patch. Không đổi metadata để né kiểm tra.

## Giới hạn

Tool không đọc hiểu chất lượng mục tiêu, sự đúng nghĩa của mapping, tính đầy
đủ của luồng hoặc khả năng thay thế của generalization. Nó không kiểm chứng
sự thật của xác nhận người dùng, không chạy renderer, không xác minh hình hay
sơ đồ khớp mọi bảng. Cần review riêng theo modeling-rules và diagram-rules.
Các record pass/approval_evidence phải do người thực hiện ghi trung thực.

Bảng diagrams có view=core/detail/system. --final cho module cần view core và
**một dòng detail cho mỗi core**; focus là ID core, members là các UC trên hình.
Tool kiểm focus hợp lệ, core và đủ sub theo decomposition xuất hiện trong
members; overview cần view system. V2.3 đối chiếu members của view core/system
với tập core trong catalog. Mỗi view có bằng chứng render.
Artifact tương đối với US, phải là file.svg tồn tại, XML root svg; từ2.3 sai
artifact là lỗi. Đây là kiểm file, không chứng nhận render: XML mẫu trong tests
không phải hình đã render. Không nhận đường dẫn tuyệt đối ở contract mới.
Phải review riêng từng cạnh core–sub/sub–sub giữa bảng relation và hình; tool
không suy ra cạnh từ members hoặc xác nhận nội dung file hình.

Tests dùng FR/US tổng hợp trong thư mục tạm, không sửa FR hoặc US của dự án.
Đánh giá hành vi agent/discovery dùng [evaluation-scenarios](../references/evaluation-scenarios.md),
tách khỏi unit tests checker. Không dùng điểm pass của một fixture để chứng
minh ổn định trên mọi module hoặc hiệu quả nhân quả của skill.
