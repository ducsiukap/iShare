# Kiểm tra scenario

[Vietnamese Doc]

`check_scenarios.py` chỉ dùng thư viện chuẩn Python 3.10+. Công cụ đọc file,
không sửa FR/US/scenario và không cần dịch vụ bên ngoài. Chạy từ gốc repository.

## Lệnh

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M01/SC-M01.md --fr docs/specs/fr/FR-M01.md --us docs/specs/us/US-M01.md
```

Thêm `--fr <path>` cho mỗi FR liên module thực sự dùng. Không đưa toàn bộ FR
vào chỉ để che một nguồn sai module. `--final` kiểm thêm không còn UC có
treatment=gap; **không** phải lệnh tự phê duyệt hoặc chứng minh hết mọi GAP.

Ví dụ tự chứa:

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py .agent-instructions/skills/scenarios/references/worked-example.md --fr .agent-instructions/skills/scenarios/references/example-inputs.md --us .agent-instructions/skills/scenarios/references/example-inputs.md
python -X utf8 -m unittest discover -s .agent-instructions/skills/scenarios/tools -p test_check_scenarios.py
```

Mã thoát: 0 = qua kiểm cấu trúc; 1 = lỗi tài liệu; 2 = đầu vào không đọc được
hoặc lệnh không hợp lệ. Dùng `-X utf8` trên Windows để in tiếng Việt đúng.

## Hợp đồng bảng

Giữ marker và tên cột máy đọc trong [template](../output/scenario-template.md).
Ô chứa ký tự `|` phải escape thành `\|`. `subject` là **một** actor ID hoặc
SYSTEM; không ghi `ACT-001/SYSTEM`. `next` là một step ID trong cùng scenario
hoặc END:SUCCESS / END:REJECTED / END:CANCELLED / END:HANDED_OFF.

Mỗi nhánh được khai báo trong sc:exceptions, có bảng sc:branch riêng; `at`
chỉ bước luồng chính bị thay thế. Nhánh lồng được triển khai thành các đường
đầy đủ từ điểm rẽ tương ứng, hoặc vòng lặp quay lại bước kiểm tra. Không dùng
chuyển tiếp sang scenario khác để bỏ qua phần cần đặc tả: viết điểm chuyển
giao và hậu điều kiện có nguồn; review ngữ nghĩa liên kết với scenario nhận.

Từ v1.1, bảng luồng yêu cầu `primary`, `completion`, `covered_ucs`, `rationale`
bên cạnh các cột cũ. Luồng chính bắt đầu bằng actor chính, có cả actor và
SYSTEM, kết thúc bằng SYSTEM trả END:SUCCESS. Lỗi/từ chối/hủy là nhánh,
không phải luồng chính riêng. Kiểm tra này không suy luận được mục tiêu đã
thật sự hoàn tất hay bước actor có bị bịa để qua kiểm hay không.

UC `embedded` không sở hữu BF: liệt kê SC bao chứa, có `coverage` dạng
`SC-M90-001/M4` hoặc `SC-M90-001/E1.1` cho từng SC và xuất hiện trong
`covered_ucs` của luồng đó. UC `background` không có SC; coverage chỉ tới
ghi chú quy tắc nền, có rationale. Công cụ chỉ kiểm sự có mặt của ghi chú,
không đọc hiểu hiệu ứng nền. Chỉ sửa tài liệu cũ khi người dùng yêu cầu áp dụng
lại skill; cập nhật validator không tự cập nhật đầu ra các module.

## Máy kiểm được và chưa kiểm được

| Có kiểm | Cần người/agent review |
|---|---|
| Sáu mục theo thứ tự, bước có chủ thể/hành động/dữ liệu/đích/nguồn | Nội dung sáu mục đúng nghiệp vụ và đủ chi tiết |
| Actor/UC/mapping tồn tại trong US; full scope đối chiếu catalog | Phân tích UC nguồn đúng, source baseline còn hiệu lực |
| Mỗi BF có một SC riêng, UC owner và mapping SC không đứt | Danh mục BF có bỏ sót luồng trong FR/US hay không |
| Actor chính khởi đầu, có cả actor/SYSTEM, SYSTEM kết thúc SUCCESS | BF hoàn tất toàn bộ chức năng, không chỉ là một bước/guard hoặc nhánh trạng thái |
| UC embedded có SC/bước tồn tại, có mặt trong covered_ucs | UC con thực sự được thực hiện đủ tại các bước được dẫn |
| Chủ thể khác nhau trên cạnh bước, cả điểm quay lại | Câu hành động thực sự chỉ có một chủ thể, không thêm bước giả |
| Nhánh thay đúng bước, step tồn tại, có đường tới kết thúc | Guard khả thi, dữ liệu tương ứng, mọi lựa chọn đã có đường |
| ID FR/BR được định nghĩa trong file đầu vào | FR/BR thực sự chứng minh hành vi, không chỉ cùng ID |
| Endpoint có hậu điều kiện, chu trình không có lối ra bị báo | Điều kiện thoát khả thi, không có dữ liệu bị ghi sai hoặc mất |

Validator không đọc hiểu mọi lời dẫn, không tự chứng minh guard loại trừ,
không so SHA-256 với baseline và không thay kiểm trace hai chiều. PASS chỉ
có ý nghĩa ở cột trái. Khi fixture/source đổi, chạy lại và review phần ảnh hưởng.
