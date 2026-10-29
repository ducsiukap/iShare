# Đặc tả use case — {{DOCUMENT_ID}}

[Vietnamese Doc]

## Metadata và tiến độ

<!-- uc:document -->
| key | value |
|---|---|
| document_id | {{DOCUMENT_ID}} |
| skill_version | 2.2 |
| mode | {{module_or_overview_or_partial}} |
| modules | {{Mxx_LIST}} |
| scope | {{ALL_or_FULL_FR_IDS}} |
| status | Đang soạn |
| current_step | 1 |
| completed_steps | - |
| approved_steps | - |
| source_baseline | {{SOURCE_VERSIONS}} |
| author | {{ACTUAL_AUTHOR}} |
| date | {{DATE}} |
| approval_evidence | - |
| semantic_review | pending |
| diagram_check | pending |

mode: module / overview / partial. scope: ALL hoặc danh sách đầy đủ các mã FR/BR
giới hạn phạm vi; partial phải ghi giới hạn và dùng --scope khi kiểm tra.
Overview hoàn tất danh mục/view, không hàm ý đặc tả sâu mọi UC.
completed_steps ghi sau khi làm xong; approved_steps chỉ ghi theo xác nhận thật.

| Bước | Phần đã hoàn tất/thay đổi | Xác nhận của người dùng | Baseline | Cần làm lại |
|---|---|---|---|---|
| 1 | {{CONTENT}} | {{PENDING_or_EVIDENCE}} | {{BASELINE}} | - |

## 1. Phạm vi và nguồn

**Mục đích sử dụng:** {{PURPOSE_AND_AUDIENCE}}
**Subject/boundary:** {{SYSTEM_UNDER_STUDY}}
**Trong phạm vi:** {{IN_SCOPE}}
**Ngoài phạm vi:** {{OUT_OF_SCOPE}}
**Mức đặc tả:** {{OVERVIEW_OR_DETAILED_SCOPE}}

<!-- uc:sources -->
| path | version | role |
|---|---|---|
| docs/specs/fr/FR-{{Mxx}}.md | {{VERSION}} | owner |

Ghi mọi FR liên quan thực sự đọc; role: owner / related. Rubric và tài liệu
phương pháp ghi riêng, không dùng thay nguồn tính năng.

### Danh mục actor

<!-- uc:actors -->
| id | name | kind | parent | boundary_reason | sources |
|---|---|---|---|---|---|
| ACT-001 | {{ROLE}} | human | - | {{WHY_EXTERNAL}} | {{FULL_SOURCE_IDS}} |

kind: human / external-system. Chính/hỗ trợ là vai trò trong từng UC;
parent tùy chọn dùng actor ID nếu có generalization đã kiểm chứng.

### Kiểm kê nhóm chức năng

| Mã nhóm FR | Mục tiêu/hành vi | Cách biểu diễn dự kiến | Owner | Căn cứ |
|---|---|---|---|---|
| {{FULL_FR_GROUP_ID}} | {{BEHAVIOR}} | {{UC_STEP_RULE_AUT}} | {{Mxx}} | {{SOURCE}} |

## 2. UC chính và UC con của module

### 2.1 Danh mục hai tầng

<!-- uc:catalog -->
| id | name | tier | level | primary | supporting | owner | anchor | sources |
|---|---|---|---|---|---|---|---|---|
| UC-{{Mxx}}-001 | {{CORE_GOAL}} | core | Summary | ACT-001 | - | {{Mxx}} | #uc-{{mxx}}-001 | {{FULL_SOURCE_IDS}} |
| UC-{{Mxx}}-002 | {{SUB_GOAL}} | sub | User goal | ACT-001 | - | {{Mxx}} | #uc-{{mxx}}-002 | {{FULL_SOURCE_IDS}} |

tier: core (UC chính) / sub (UC con), độc lập với level: Summary / User goal /
Subfunction. Mỗi module đầy đủ có cả hai tầng, không bắt buộc có cả ba level.
Một UC dùng chung có một ID, một owner, nhiều view. Overview hệ thống chỉ đưa
các dòng core vào catalog, lấy nguyên ID/tên/owner từ tài liệu module nguồn.

### 2.2 Bảng phân rã UC chính → UC con

<!-- uc:decomposition -->
| core | sub | rationale | sources |
|---|---|---|---|
| UC-{{Mxx}}-001 | UC-{{Mxx}}-002 | {{HOW_SUB_CONTRIBUTES_TO_CORE_GOAL}} | {{FULL_SOURCE_IDS}} |

Mỗi UC chính có ít nhất một UC con; mỗi UC con có ít nhất một dòng thuộc UC
chính. Dùng nhiều dòng cho UC con dùng chung, không nhân bản ID. Bảng này thể
hiện phân rã nghiệp vụ, không tự tạo include/extend/generalization.
Overview hệ thống giữ bảng rỗng và trỏ đến phân rã trong từng tài liệu module.

### 2.3 UC chính của các module dùng để tổng hợp hệ thống

<!-- uc:module-models -->
| module | path | baseline |
|---|---|---|

Chỉ điền ở mode overview: path là đường dẫn từ repo root đến US-Mxx.md, baseline
là source_baseline trong tài liệu module. Ghi một dòng mỗi module trong phạm vi.
Module chưa có danh mục hai tầng được ghi chưa hoàn tất, không tự điền UC thay thế.

| Quyết định | Hành vi FR | Biểu diễn được chọn | Vì sao giữ/gộp/tách | Phương án khác |
|---|---|---|---|---|
| D-001 | {{BEHAVIOR}} | {{REPRESENTATION}} | {{RATIONALE}} | {{ALTERNATIVE}} |

## 3. Đặc tả

### 3.1 Mô tả từng UC chính

Nêu actor, mục tiêu bao quát, giá trị/kết quả, ranh giới, các UC con và cách các
UC con đóng góp vào mục tiêu. Summary có quy trình tổng quát, không giả định mọi
UC con phải chạy trong cùng một lần. UC chính mức User goal có thêm hợp đồng và
luồng tương ứng. Tạo anchor theo catalog cho mọi UC chính.

<a id="uc-{{mxx}}-001"></a>

**UC-{{Mxx}}-001 — {{CORE_GOAL}}:** {{CORE_ACTOR_VALUE_SCOPE_AND_PROCESS}}.
UC con: {{SUB_UC_IDS_FROM_DECOMPOSITION}}.

### 3.2 Đặc tả từng UC con

Mọi UC con trong module phải có đặc tả sau, kể cả UC con mức User goal. Trong
từng đặc tả ghi UC chính liên quan theo bảng decomposition.

<a id="uc-{{mxx}}-002"></a>

### UC-{{Mxx}}-002 — {{GOAL}}

<!-- uc:spec UC-{{Mxx}}-002 -->
| key | value |
|---|---|
| goal | {{OBSERVABLE_VALUE}} |
| subject | {{BOUNDARY}} |
| level | User goal |
| primary | ACT-001 |
| supporting | - |
| trigger | {{EVENT}} |
| preconditions | {{SOURCE_BACKED_CONDITIONS}} |
| success | {{SUCCESS_POSTCONDITIONS}} |
| failure | {{SOURCE_BACKED_GUARANTEE_OR_OPEN_POINT}} |
| abstract | false |
| common_contract | {{IF_GENERALIZATION_OTHERWISE_NOT_APPLICABLE}} |

#### Luồng chính

<a id="uc-{{mxx}}-002-main-1"></a>

| Bước | Ai | Hành động/phản hồi | Tiếp tục | Nguồn |
|---|---|---|---|---|
| 1 | ACT-001 | {{ACTION}} | {{NEXT_STEP}} | {{SOURCE_IDS}} |
| 2 | Subject | {{RESPONSE}} | END: {{RESULT}} | {{SOURCE_IDS}} |

Tạo anchor riêng cho mỗi bước được relation/trace tham chiếu; ID anchor
bắt đầu bằng ID UC viết thường, theo sau là main-N / alt-N / pre / post / contract.

#### Luồng thay thế và ngoại lệ

<a id="uc-{{mxx}}-002-alt-1"></a>

| ID nhánh | Bước rẽ | Điều kiện | Xử lý | Quay lại/kết thúc | Nguồn |
|---|---|---|---|---|---|
| A1 | {{STEP}} | {{GUARD}} | {{ACTIONS}} | {{STEP_OR_END_WITH_RESULT}} | {{SOURCE_IDS}} |

Nếu không có nhánh theo FR, ghi rõ sau đối chiếu. Không bịa lỗi/retry để đủ bảng.

#### Quy tắc và điểm chưa rõ

<a id="uc-{{mxx}}-002-rules"></a>

{{SOURCE_BACKED_RULES_AND_OPEN_POINT_IDS}}

Lặp cấu trúc cho mọi UC con thuộc scope chi tiết; dùng ID của UC con tương ứng,
không sao chép ID core mẫu vào đặc tả sub. Core có anchor/brief riêng như 3.1.
Overview chỉ mô tả core và đường dẫn về module, không sao chép đặc tả UC con.

### Hành vi tự động / quy tắc xuyên UC

<a id="aut-{{mxx}}-001"></a>

| ID | Trigger | Điều kiện/trạng thái trước | Kết quả/trạng thái sau | Quy tắc dữ liệu | Nguồn |
|---|---|---|---|---|---|
| AUT-{{Mxx}}-001 | {{EVENT_TIME}} | {{BEFORE}} | {{AFTER}} | {{DATA_POLICY}} | {{SOURCE_IDS}} |

Xóa mục này nếu không áp dụng; không tự suy diễn cơ chế kỹ thuật.

## 4. Quan hệ

### Extension points

<!-- uc:extension-points -->
| id | base | at | description |
|---|---|---|---|

Không cần thêm dòng khi không dùng extend. at là anchor bước của UC base.

### Quan hệ UC–UC

<!-- uc:relations -->
| type | source | target | at | condition | return_to | rationale | sources |
|---|---|---|---|---|---|---|---|

type: include / extend / generalization.
include: source including, target included, at = anchor bước của source.
extend: source extension, target base, at = extension point ID của base;
condition và return_to bắt buộc (anchor base hoặc END: kết quả).
generalization: source specific, target general, at = anchor hợp đồng chung
của target; rationale ghi phần kế thừa và chuyên biệt. Không bắt cha abstract.

### Association actor–UC

| Actor ID | UC ID | Vai trò tương tác | Điều kiện quyền | Nguồn |
|---|---|---|---|---|

Không coi bảng quyền hoặc link màn hình tự tạo quan hệ giữa UC.

### Kết luận các cặp không có quan hệ UML

| UC chính đang xét | UC A | UC B | Kết luận/lý do | Cách thể hiện | Nguồn |
|---|---|---|---|---|---|

Rà core–sub và sub–sub theo luồng, không chỉ nối mọi sub về core. Bảng relation
có thể có source/target là core hoặc sub. Cặp không có quan hệ ghi rõ, không
thêm mũi tên chỉ vì cùng thuộc một UC chính.

## 5. Truy vết

<!-- uc:trace -->
| requirement | target | coverage | note |
|---|---|---|---|
| {{FULL_REQUIREMENT_ID}} | #{{ANCHOR}} | Chưa | {{EXPLANATION}} |

Một dòng mỗi FR nhóm/chi tiết hoặc BR, target có thể có nhiều anchor ngăn bằng
dấu phẩy. coverage: Đủ / Một phần / Chưa. Ghi Đủ sau review nội dung nguồn–đích;
mã tồn tại và anchor có thật chưa chứng minh đủ hành vi.
Overview chỉ bắt buộc nhóm FR; ghi rõ tham chiếu module chưa đặc tả, không
nhận là bao phủ chi tiết toàn dự án.

| Mã đã bỏ/hoãn | Bằng chứng nguồn hiện hành | Cách xử lý |
|---|---|---|

### Giao tiếp và tác động thay đổi

| Owner | UC/FR liên quan | Sự kiện/điều kiện/kết quả | Đối chiếu bên nhận | Thay đổi baseline |
|---|---|---|---|---|

## 6. Sơ đồ tổng quan từ UC chính và sơ đồ chi tiết từ UC con

### 6.1 Tổng quan module — UC chính

{{MODULE_CORE_USE_CASE_DIAGRAM}}

### 6.2 Sơ đồ chi tiết riêng cho từng UC chính

#### 6.2.1 UC-{{Mxx}}-001 — {{CORE_GOAL}}

**Focus:** UC-{{Mxx}}-001. **Node:** {{CORE_AND_ALL_SUB_IDS}}.

{{PER_CORE_DETAIL_DIAGRAM_WITH_CORE_SUB_AND_SUB_SUB_EDGES}}

| Source | Quan hệ | Target | Điểm gọi/mở rộng/chuyên biệt | Căn cứ |
|---|---|---|---|---|

Lấy cạnh từ bảng relation, hiển thị cả core–sub lẫn sub–sub có căn cứ. Core
phải là một node trong hình, không chỉ tên nhóm. Ghi kết luận các cặp không
có relation thay vì tự nối. Lặp mục này cho **mọi UC chính** của module.
Có thể thêm view phụ, không dùng một hình chung thay các hình riêng bắt buộc.

### 6.3 Tổng quan toàn hệ thống — tổng hợp UC chính module

{{SYSTEM_CORE_DIAGRAM_OR_LINK_TO_US_OVERVIEW}}

Module document ghi link tới US-overview.md nếu đã có. Khi chưa có hoặc ngoài
scope thì ghi chưa tổng hợp. Mode overview vẽ các core từ bảng module-models;
không đưa sub vào hình tổng quan và không tự tạo core khác với nguồn module.

Mỗi view ghi subject, scope, ID và renderer; dùng ký pháp UML phù hợp.
Không dựng mọi loại quan hệ chỉ để đủ mẫu.

## 7. Kiểm tra và phê duyệt

<!-- uc:diagrams -->
| id | view | focus | members | format | renderer | result | artifact |
|---|---|---|---|---|---|---|---|

view: core / detail / system. Module đầy đủ cần core và detail; overview cần
system. result: pass / pending / fail; format: plantuml / mermaid / illustrative.
Mỗi core có một dòng detail: focus=ID core, members=core và các sub/tham chiếu
trong hình (ngăn bằng dấu phẩy). View core/system dùng focus=-, members ghi
các ID xuất hiện. Thêm hình phụ ở QA, không tạo hai dòng detail chính cùng focus.
Ghi phiên bản renderer và vị trí hình xuất; không có sơ đồ thì ghi diagram_check
not-applicable kèm lý do trong bảng QA. Không dùng not-applicable để bỏ qua
sơ đồ bắt buộc của tài liệu tổng quan/module hoàn chỉnh.

| Hạng mục | Lệnh/phương pháp | Kết quả thực tế | Giới hạn/bằng chứng |
|---|---|---|---|
| Ngữ nghĩa | Đọc FR–UC và từng quan hệ | {{RESULT}} | {{EVIDENCE}} |
| Cấu trúc/truy vết | check_us.py | {{RESULT}} | Không chứng minh ngữ nghĩa |
| Sơ đồ | Parser + render + kiểm tra hình | {{RESULT}} | {{RENDERER_AND_ARTIFACT}} |

### Điểm cần làm rõ

| ID | Nguồn | Vấn đề | Ảnh hưởng | Trạng thái/quyết định |
|---|---|---|---|---|

### ID cũ → mới (khi thực sự cần chuyển đổi)

| ID cũ | ID hiện hành | Lý do | Tham chiếu đã xử lý |
|---|---|---|---|

Chỉ sau xác nhận cuối mới ghi Đã duyệt, approved_steps có 7 và approval_evidence.
