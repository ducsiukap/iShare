# Kịch bản nghiệp vụ — SC-{{Mxx}}

[Vietnamese Doc]

Mục đích: {{PURPOSE}}. Boundary: {{SYSTEM_BOUNDARY}}.
Trong phạm vi: {{SCOPE}}. Ngoài phạm vi: {{OUT_OF_SCOPE}}.

## Metadata và nguồn

<!-- sc:document -->
| key | value |
|---|---|
| module | {{Mxx}} |
| scope | {{ALL_or_COMMA_SEPARATED_UC_IDS}} |
| skill_version | 1.3 |
| output_dir | {{SOURCE_PACKAGE_ROOT}}/scenarios/{{Mxx}} |
| status | Đang soạn |
| completed_steps | - |
| date | {{YYYY-MM-DD}} |
| approval_evidence | - |

| Path từ repo root | Version | Ngày | Trạng thái nguồn | SHA-256 | Vai trò |
|---|---|---|---|---|---|
| {{FR_PATH}} | {{VERSION}} | {{DATE}} | {{STATUS}} | {{HASH}} | Yêu cầu nghiệp vụ |
| {{US_PATH}} | {{VERSION_OR_NONE}} | {{DATE}} | {{STATUS}} | {{HASH}} | Mô hình và đặc tả |
| {{OVERVIEW_PATH_OR_MISSING}} | {{VERSION}} | {{DATE}} | {{STATUS}} | {{HASH_OR_NONE}} | Ngữ cảnh boundary |

<!-- sc:actors -->
| id | name | kind | source |
|---|---|---|---|
| ACT-{{nnn}} | {{ROLE_FROM_US}} | human | {{US_ANCHOR_AND_FR_IDS}} |

SYSTEM là Hệ thống iShare, không đưa vào danh mục actor ngoài hệ thống.

## Kiểm kê các nhóm UC chi tiết

<!-- sc:decomposition -->
| core | sub | source |
|---|---|---|
| UC-{{Mxx}}-{{CORE}} | UC-{{Mxx}}-{{SUB}} | {{US_MAPPING}} |

<!-- sc:ucs -->
| id | treatment | scenarios | coverage | rationale | sources |
|---|---|---|---|---|---|
| UC-{{Mxx}}-{{CORE}} | aggregate | SC-{{Mxx}}-001 | {{SC_REFERENCES}} | {{WHY_AGGREGATE_OR_ABSTRACT}} | {{SOURCE_IDS}} |
| UC-{{Mxx}}-{{SUB}} | scenario | SC-{{Mxx}}-001 | {{SC_REFERENCES}} | {{INDEPENDENT_ACTOR_GOAL}} | {{SOURCE_IDS}} |
| UC-{{Mxx}}-{{SUPPORT_SUB}} | embedded | SC-{{Mxx}}-001 | SC-{{Mxx}}-001/M2 | {{WHY_PART_OF_CONTAINING_JOURNEY}} | {{SOURCE_IDS}} |

treatment: scenario / embedded / aggregate / abstract / background / gap.
Xóa dòng minh họa không có trong nguồn. Core có mục tiêu độc lập cũng dùng
scenario; không nhân bản cùng hành trình ở core và sub. Một UC dùng chung
chỉ một dòng, nhiều mapping. `embedded` phải có SC/bước cụ thể trong coverage
(ví dụ SC-M90-001/M4, SC-M90-001/E1.1); mỗi SC được liệt kê phải có vị trí.
aggregate/abstract dẫn tới các SC cụ thể. background không có SC, ghi coverage
trỏ tới ghi chú quy tắc nền và rationale; không đếm như BF/SC.

## Danh mục luồng nghiệp vụ

<!-- sc:flows -->
| id | uc | primary | trigger | goal | completion | covered_ucs | rationale | scenario | sources |
|---|---|---|---|---|---|---|---|---|---|
| BF-{{Mxx}}-001 | UC-{{Mxx}}-{{SUB}} | ACT-{{nnn}} | {{ACTOR_INITIATING_ACTION}} | {{COMPLETE_FUNCTION_GOAL}} | {{RESULT_RETURNED_TO_ACTOR}} | {{OWNER_AND_PARTICIPATING_UC_IDS}} | {{WHY_INDEPENDENT_ACTOR_GOAL}} | SC-{{Mxx}}-001 | {{FULL_FR_BR_IDS_AND_US_ANCHOR}} |

Chỉ gán BF sau phép kiểm ở bước 3. Không ghi trạng thái bị từ chối, kiểm
quyền hoặc tác vụ nền thành một BF. covered_ucs không tạo quan hệ UML mới.

| UC | Quyết định/nhánh nguồn | Biểu diễn SC/ngoại lệ | Tách/gộp và lý do | Còn thiếu |
|---|---|---|---|---|
| {{UC_ID}} | {{SOURCE_GUARD_OR_CHOICE}} | {{SC_ID_AND_E_ID}} | {{RATIONALE}} | {{NONE_OR_GAP}} |

## Dữ liệu minh họa dùng chung

| Bộ dữ liệu | Trường/đối tượng | Giá trị giả lập | Trước → sau | Ràng buộc nguồn |
|---|---|---|---|---|
| D1 | {{BUSINESS_FIELD}} | {{SYNTHETIC_VALUE}} | {{BEFORE_AFTER}} | {{BR_OR_FR_ID}} |

Không biến giá trị minh họa thành quy tắc. Chọn giá trị cụ thể kích hoạt đúng
luồng và guard; ghi bộ khác cho lỗi/sửa/hủy khi cần.

## Scenario

<!-- sc:scenario SC-{{Mxx}}-001 -->
### SC-{{Mxx}}-001

#### 1. Tên kịch bản chuẩn

{{VERB_OBJECT_AND_BUSINESS_VARIANT}} — BF-{{Mxx}}-001; UC owner:
UC-{{Mxx}}-{{SUB}}; thuộc UC chính {{CORE_IDS}}. Trigger: {{TRIGGER}}.

#### 2. Actor thực hiện

{{PRIMARY_ID_AND_ROLE_MATCHING_FLOW_PRIMARY}}; hỗ trợ: {{SUPPORTING_IDS_OR_NONE}}.
Actor chính theo đuổi mục tiêu chức năng và khởi đầu luồng. Không có actor
khởi tạo thì ứng viên không đủ điều kiện là scenario của skill này.

#### 3. Tiền điều kiện

{{SOURCE_BACKED_STATE_PERMISSION_CONTEXT_AND_DATA}}.
Không đặt điều kiện loại trừ chính ngoại lệ cần mô tả.

#### 4. Hậu điều kiện

<!-- sc:post SC-{{Mxx}}-001 -->
| result | condition |
|---|---|
| SUCCESS | {{OBSERVABLE_SUCCESS_STATE_AND_SIDE_EFFECTS}} |
| CANCELLED | {{STATE_AFTER_CANCEL_IF_SOURCED}} |
| REJECTED | {{STATE_AFTER_REFUSAL_IF_SOURCED}} |

Xóa kết quả không dùng; HANDED_OFF chỉ cho ngoại lệ chuyển sang mục tiêu
khác có hợp đồng tiếp nối rõ. Luồng chính kết thúc SUCCESS của toàn chức năng.

#### 5. Các sự kiện chính

<!-- sc:main SC-{{Mxx}}-001 -->
| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-{{nnn}} | {{ACTOR_ACTION}} | {{DATA_D1}} | M2 | {{FR_US_SOURCE}} |
| M2 | SYSTEM | {{SYSTEM_RESPONSE_AND_EFFECT}} | {{RESULT_DATA}} | END:SUCCESS | {{FR_BR_US_SOURCE}} |

#### 6. Các ngoại lệ

<!-- sc:exceptions SC-{{Mxx}}-001 -->
| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | {{SOURCE_BACKED_GUARD}} | E1.1 | {{SOURCE}} |

`at` là bước **bị thay thế**. Luồng chính M1 → M2 trở thành M1 → E1.1.
Nếu không có ngoại lệ trong nguồn: giữ bảng rỗng, ghi phạm vi đã rà và bằng
chứng; xóa bảng branch minh họa. Thiếu thông tin phải ghi GAP, không ghi không có.

<!-- sc:branch SC-{{Mxx}}-001 E1 -->
| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | {{RESPONSE_TO_GUARD}} | {{FAILURE_STATE}} | END:REJECTED | {{SOURCE}} |

<!-- sc:end SC-{{Mxx}}-001 -->

Hai dòng trên là khung, không phải giới hạn số bước. Viết đủ tương tác cần
thiết đến kết quả chức năng; không nén các lượt actor vào một câu SYSTEM.
Lặp khối sáu phần cho mọi BF đạt phép kiểm, không cho UC hỗ trợ/tác vụ nền.

## Quy tắc nền có liên quan (không phải scenario)

| UC/AUT/RULE nguồn | Trigger/điều kiện | Hiệu ứng | SC/bước/hậu điều kiện liên quan hoặc lý do không có | Nguồn |
|---|---|---|---|---|

Chỉ ghi nếu nguồn có tác vụ nền cần truy vết; không dựng khối sáu phần phụ.

## Truy vết và đối soát bao phủ

| FR/BR hoặc UC/nhánh nguồn | BF | SC + bước/ngoại lệ/điều kiện | Mức bao phủ | Bằng chứng/thiếu sót |
|---|---|---|---|---|
| {{SOURCE_ID}} | {{BF_ID}} | {{SC_ID}} / {{STEP_OR_BRANCH}} | {{Đủ_Một_phần_Chưa}} | {{REASON}} |

| Vòng lặp/tổ hợp/lớp dữ liệu | Đường khả thi đã mô tả | Loại trừ/gộp | Lý do từ nguồn |
|---|---|---|---|

## GAP và kiểm tra

| ID | Nguồn | Điều chưa rõ | SC/bước bị ảnh hưởng | Chặn? | Trạng thái/quyết định |
|---|---|---|---|---|---|

| Kiểm tra | Phương pháp/lệnh | Kết quả thực tế | Giới hạn/bằng chứng |
|---|---|---|---|
| Cấu trúc, chủ thể, đích bước | check_scenarios.py | {{RESULT}} | Không chứng minh ngữ nghĩa |
| BF là chức năng actor hoàn chỉnh | Phép kiểm bước 3 và walkthrough đầu–cuối | {{RESULT}} | Không tách trạng thái/bước nội bộ thành BF |
| Nguồn, quyền, dữ liệu, guard | Đọc FR/US và walkthrough từng đường | {{RESULT}} | {{EVIDENCE}} |
| Bao phủ toàn scope | Đối soát UC, FR/BR, BF, lựa chọn/nhánh nguồn | {{COUNTS_AND_RESULT}} | {{GAPS_OR_NONE}} |

Phê duyệt: {{PENDING_OR_ACTUAL_EVIDENCE}}.
