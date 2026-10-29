# Ví dụ có giới hạn phạm vi — Đăng xuất

[Vietnamese Doc]

Đây là ví dụ phương pháp của skill 2.2, không phải tài liệu được stakeholder
duyệt và không đại diện toàn bộ M01. Chỉ đặc tả FR-M01-07 và hai yêu cầu con;
UC chính quản lý phiên được ghi để minh họa ngữ cảnh phân rã, không nhận là
đã phân tích đủ các UC con Đăng nhập/Duy trì phiên của toàn bộ M01.
Không thêm bước xác nhận đăng xuất vì nguồn không yêu cầu.

<!-- uc:document -->
| key | value |
|---|---|
| document_id | EXAMPLE-M01-LOGOUT |
| skill_version | 2.2 |
| mode | partial |
| modules | M01 |
| scope | FR-M01-07 |
| status | Đang soạn |
| current_step | 5 |
| completed_steps | 1, 2, 3, 4, 5 |
| approved_steps | - |
| source_baseline | FR-M01 1.10 |
| author | Ví dụ phương pháp của skill |
| date | 2026-10-28 |
| approval_evidence | - |
| semantic_review | pass |
| diagram_check | not-applicable |

## Boundary và nguồn

Subject: iShare. Actor là người đang có phiên đăng nhập; trạng thái thiết bị
khác là điều kiện dữ liệu, không phải actor riêng. Mục tiêu là kết thúc phiên
trên thiết bị hiện tại. Không mô tả cách lưu token.

<!-- uc:sources -->
| path | version | role |
|---|---|---|
| docs/specs/fr/FR-M01.md | 1.10 | owner |

<!-- uc:actors -->
| id | name | kind | parent | boundary_reason | sources |
|---|---|---|---|---|---|
| ACT-001 | Người dùng đang đăng nhập | human | - | Người dùng bên ngoài iShare yêu cầu kết thúc phiên | FR-M01-07.01 |

## Danh mục

<!-- uc:catalog -->
| id | name | tier | level | primary | supporting | owner | anchor | sources |
|---|---|---|---|---|---|---|---|---|
| UC-M01-020 | Quản lý phiên truy cập | core | Summary | ACT-001 | - | M01 | #uc-m01-020 | FR-M01-05, FR-M01-06, FR-M01-07 |
| UC-M01-001 | Đăng xuất | sub | User goal | ACT-001 | - | M01 | #uc-m01-001 | FR-M01-07.01, FR-M01-07.02 |

<!-- uc:decomposition -->
| core | sub | rationale | sources |
|---|---|---|---|
| UC-M01-020 | UC-M01-001 | Kết thúc phiên hiện tại là một mục tiêu cụ thể của quản lý phiên | FR-M01-07.01, FR-M01-07.02 |

<a id="uc-m01-020"></a>

UC chính Quản lý phiên truy cập đặt việc bắt đầu, duy trì và kết thúc phiên
vào bối cảnh quản lý quyền truy cập của chủ tài khoản. Ở ví dụ một phần này
chỉ đặc tả UC con Đăng xuất, không có mũi tên UML phát sinh từ bảng mapping.

ID minh họa, không tự dùng để đổi ID tài liệu M01 đã có.

<a id="uc-m01-001"></a>

## Đặc tả Đăng xuất

<!-- uc:spec UC-M01-001 -->
| key | value |
|---|---|
| goal | Kết thúc phiên hiện tại, giữ các phiên thiết bị khác |
| subject | iShare |
| level | User goal |
| primary | ACT-001 |
| supporting | - |
| trigger | Người dùng yêu cầu đăng xuất trên thiết bị hiện tại |
| preconditions | Thiết bị có phiên của người dùng |
| success | Phiên hiện tại kết thúc; phiên các thiết bị khác giữ nguyên |
| failure | Phạm vi FR-M01-07 không nêu cơ chế lỗi kỹ thuật; ví dụ không suy thêm |
| abstract | false |
| common_contract | Không áp dụng generalization |

<a id="uc-m01-001-main-1"></a>

1. ACT-001 yêu cầu đăng xuất. Nguồn: FR-M01-07.01.

<a id="uc-m01-001-main-2"></a>

2. iShare kết thúc phiên của thiết bị hiện tại. Các phiên trên thiết bị khác
   giữ nguyên. Kết thúc thành công. Nguồn: FR-M01-07.01, FR-M01-07.02.

Luồng thay thế: không được FR-M01-07 quy định trong phạm vi ví dụ.
Không tự thêm hộp xác nhận, redirect hoặc chiến lược retry.

<!-- uc:extension-points -->
| id | base | at | description |
|---|---|---|---|

<!-- uc:relations -->
| type | source | target | at | condition | return_to | rationale | sources |
|---|---|---|---|---|---|---|---|

Không có quan hệ UC–UC cần thiết trong phạm vi ví dụ.

<!-- uc:trace -->
| requirement | target | coverage | note |
|---|---|---|---|
| FR-M01-07 | #uc-m01-001 | Đủ | Một mục tiêu riêng |
| FR-M01-07.01 | #uc-m01-001-main-1, #uc-m01-001-main-2 | Đủ | Yêu cầu và kết thúc phiên |
| FR-M01-07.02 | #uc-m01-001-main-2 | Đủ | Bảo toàn phiên thiết bị khác |

<!-- uc:diagrams -->
| id | view | focus | members | format | renderer | result | artifact |
|---|---|---|---|---|---|---|---|

Ví dụ đặc tả nhỏ này không chứa sơ đồ. Tài liệu module đầy đủ vẫn phải có các
view theo bước 6.

## Các quyết định đối chiếu

| Trường hợp | Quyết định |
|---|---|
| Đăng xuất sau một lần đăng nhập đã kết thúc | UC độc lập, không extend Đăng nhập |
| Gõ @ trong Nhắc tên | Bước tương tác theo FR-M01-14.01, không mặc định UC riêng |
| Xác nhận lại chính sách | Trigger cả khi còn phiên theo FR-M01-16.01; không chỉ gắn vào lần đăng nhập |
| Email/Google | Có thể alternative flows; generalization chỉ khi đặc tả hợp đồng chung |
| Avatar | FR-M02-04.02 lưu ảnh gốc; .03 từ chối loại không hợp lệ; .04 từ chối quá dung lượng; .05 xóa avatar cũ |

Các dòng đối chiếu chỉ là lời hướng dẫn đọc nguồn, không mở rộng scope của
ví dụ Đăng xuất hoặc tuyên bố đã đặc tả đầy đủ các chức năng trên.

## Chạy kiểm tra từ repository root

```text
python -X utf8 .agent-instructions/skills/use-case-analysis/tools/check_us.py .agent-instructions/skills/use-case-analysis/references/worked-example.md --scope FR-M01-07
```

Kết quả là kiểm tra cấu trúc/truy vết cho phạm vi nhỏ, không phải phê duyệt M01.
Khi FR-M01 đổi phiên bản, công cụ báo stale baseline; review trước khi cập nhật.
