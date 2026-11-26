# Scenario minh họa — SC-M90

[Vietnamese Doc]

Ví dụ phương pháp, **không phải yêu cầu iShare hoặc tài liệu được duyệt**.
Nguồn: [example-inputs.md](example-inputs.md), version EXAMPLE-2.
Boundary: hệ thống danh mục minh họa. Giá trị và mã nhãn đều giả lập.
Scope: tạo nhãn; đổi tên với tên mới hợp lệ. Chưa bao phủ xử lý tên mới
rỗng khi đổi tên vì nguồn chưa định nghĩa, không tuyên bố đủ mọi biến thể M90.

<!-- sc:document -->
| key | value |
|---|---|
| module | M90 |
| scope | UC-M90-001, UC-M90-002 |
| skill_version | 1.1 |
| status | Đang soạn |
| completed_steps | 1, 2, 3, 4 |
| date | 2026-11-08 |
| approval_evidence | - |

<!-- sc:actors -->
| id | name | kind | source |
|---|---|---|---|
| ACT-901 | Biên tập viên | human | US giả lập; FR-M90-01.01, FR-M90-02.01 |

## Nhóm UC chi tiết và luồng

<!-- sc:decomposition -->
| core | sub | source |
|---|---|---|
| UC-M90-010 | UC-M90-001 | Bảng decomposition của US giả lập |
| UC-M90-010 | UC-M90-002 | Bảng decomposition của US giả lập |

<!-- sc:ucs -->
| id | treatment | scenarios | coverage | rationale | sources |
|---|---|---|---|---|---|
| UC-M90-010 | aggregate | SC-M90-001, SC-M90-002 | Hai SC con | Tổng hợp hai hành trình, không thực thi nối tiếp bắt buộc | FR-M90-01.01, FR-M90-02.01 |
| UC-M90-001 | scenario | SC-M90-001, SC-M90-002 | Hai hành trình hoàn chỉnh bên dưới | Actor yêu cầu tạo đối tượng mới hoặc đổi tên đối tượng đã có, hai chức năng độc lập | FR-M90-01.01, FR-M90-02.01 |
| UC-M90-002 | embedded | SC-M90-001, SC-M90-002 | SC-M90-001/M4, SC-M90-001/E1.1, SC-M90-001/E3.1, SC-M90-002/M2 | Kiểm tên nằm trong lượt xử lý yêu cầu; actor không yêu cầu chức năng kiểm tên độc lập | BR-M90-01, FR-M90-01.03, FR-M90-02.01 |

<!-- sc:flows -->
| id | uc | primary | trigger | goal | completion | covered_ucs | rationale | scenario | sources |
|---|---|---|---|---|---|---|---|---|---|
| BF-M90-001 | UC-M90-001 | ACT-901 | Biên tập viên yêu cầu tạo nhãn mới | Tạo nhãn mới | Hệ thống tạo nhãn, trả mã, tên và kết quả thành công cho biên tập viên | UC-M90-001, UC-M90-002 | Tạo đối tượng mới theo yêu cầu riêng, không cần thực hiện đổi tên | SC-M90-001 | FR-M90-01.01, FR-M90-01.02 |
| BF-M90-002 | UC-M90-001 | ACT-901 | Biên tập viên gửi mã nhãn và tên thay thế | Đổi tên nhãn hiện có | Hệ thống cập nhật tên của đúng nhãn và trả kết quả cho biên tập viên | UC-M90-001, UC-M90-002 | Cập nhật đối tượng đã có theo yêu cầu riêng, không cần tạo mới trong cùng hành trình | SC-M90-002 | FR-M90-02.01 |

Hai BF đều có actor chủ động yêu cầu và SYSTEM trả kết quả hoàn tất chức
năng. UC-M90-002 được thực hiện tại bước hệ thống trong cả hai luồng, không
thành scenario thứ ba. Tên rỗng, hủy và không tìm thấy mã là nhánh của chức
năng tương ứng, không phải các BF mới. Luồng đổi tên hai bước là hợp lệ vì
nguồn cho phép actor gửi trực tiếp mã và tên, không yêu cầu thêm bước mở form.

| Quyết định/nhánh nguồn | Đích | Lý do |
|---|---|---|
| Tên tạo rỗng, chọn sửa rồi gửi | SC-M90-001 / E1 | Cùng mục tiêu tạo nhãn, nhánh phục hồi có quay lại M4 |
| Hủy trước khi gửi | SC-M90-001 / E2 | Lựa chọn người dùng ở M3 |
| Tên tạo rỗng, chọn hủy | SC-M90-001 / E3 | Cùng lỗi ban đầu nhưng lựa chọn tiếp sau/kết quả khác E1 |
| Mã đổi tên không tồn tại | SC-M90-002 / E1 | Từ chối và kết thúc được nguồn quy định |

## Dữ liệu giả lập

| Bộ | Dữ liệu | Trạng thái trước → sau | Ràng buộc |
|---|---|---|---|
| D1 | tên = Đại số; mã kết quả minh họa = NH-101 | Chưa có bản ghi đang tạo → nhãn NH-101 tên Đại số | BR-M90-01, FR-M90-01.02 |
| D2 | tên gửi ban đầu = chuỗi rỗng; tên sửa = Đại số | Chưa tạo sau lần lỗi → tạo NH-101 sau sửa/gửi | FR-M90-01.03 |
| D3 | mã = NH-200; tên cũ = Hình; tên mới = Hình học | NH-200 tồn tại → cùng mã, tên mới, thuộc tính khác giữ nguyên | FR-M90-02.01 |
| D4 | mã = NH-999; tên mới = Hình học | NH-999 không tồn tại → danh mục không thay đổi | FR-M90-02.02 |

Không kiểm tính duy nhất của tên hoặc độ dài tối đa vì nguồn không quy định.

<!-- sc:scenario SC-M90-001 -->
### SC-M90-001

#### 1. Tên kịch bản chuẩn

Tạo nhãn mới — BF-M90-001, UC-M90-001, thuộc UC chính UC-M90-010.
Trigger: biên tập viên yêu cầu tạo nhãn.

#### 2. Actor thực hiện

ACT-901 — Biên tập viên. Không có actor hỗ trợ.

#### 3. Tiền điều kiện

Biên tập viên có quyền ghi nhận nhãn. Yêu cầu hiện tại chưa tạo nhãn.
D1 dùng cho luồng chính; D2 dùng cho nhánh thiếu tên.

#### 4. Hậu điều kiện

<!-- sc:post SC-M90-001 -->
| result | condition |
|---|---|
| SUCCESS | Một nhãn có tên Đại số được tạo, mã minh họa NH-101 được trả cùng tên và kết quả thành công. |
| CANCELLED | Thao tác tạo đã kết thúc; không có nhãn nào được tạo bởi yêu cầu này. |

#### 5. Các sự kiện chính

<!-- sc:main SC-M90-001 -->
| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-901 | Biên tập viên yêu cầu tạo nhãn mới. | Mục tiêu tạo nhãn, chưa có tên | M2 | FR-M90-01.01 |
| M2 | SYSTEM | Hệ thống cung cấp trường tên và các lựa chọn Gửi, Hủy. | Trường tên chưa có giá trị; hai lựa chọn theo nguồn | M3 | FR-M90-01.01 |
| M3 | ACT-901 | Biên tập viên nhập tên Đại số và gửi yêu cầu tạo. | D1: tên = Đại số | M4 | FR-M90-01.02 |
| M4 | SYSTEM | Hệ thống kiểm tên hợp lệ, tạo nhãn và trả mã, tên, kết quả thành công. | D1: NH-101, Đại số; nhãn đã được tạo | END:SUCCESS | FR-M90-01.02, BR-M90-01 |

#### 6. Các ngoại lệ

Mỗi `at` là bước bị thay thế. E1 và E3 chung guard tên rỗng, phân biệt bởi
lựa chọn sau thông báo; đây là hai đường đi của cùng quyết định lỗi.

<!-- sc:exceptions SC-M90-001 -->
| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M4 | M3 gửi tên rỗng; sau thông báo, actor chọn sửa và gửi lại | E1.1 | FR-M90-01.03 |
| E2 | user-choice | M3 | Actor chọn Hủy thay cho nhập/gửi ở lần đầu | E2.1 | FR-M90-01.04 |
| E3 | system | M4 | M3 gửi tên rỗng; sau thông báo, actor chọn Hủy | E3.1 | FR-M90-01.03, FR-M90-01.04 |

<!-- sc:branch SC-M90-001 E1 -->
| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống thông báo cần nhập tên, chưa tạo nhãn và cho phép sửa/gửi lại hoặc Hủy. | D2: tên rỗng; danh mục chưa đổi | E1.2 | FR-M90-01.03, BR-M90-01 |
| E1.2 | ACT-901 | Biên tập viên chọn sửa, nhập Đại số và gửi lại. | D2: tên đã sửa = Đại số | M4 | FR-M90-01.03 |

Nhập lại M4: hệ thống kiểm tra bộ dữ liệu sửa, tạo nhãn và kết thúc SUCCESS.
Nếu gửi lại tên vẫn rỗng, áp dụng lại E1 hoặc E3 theo lựa chọn; nguồn không
giới hạn số lần. Lặp không làm tạo thêm nhãn trước khi dữ liệu hợp lệ.

<!-- sc:branch SC-M90-001 E2 -->
| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-901 | Biên tập viên chọn Hủy. | Yêu cầu tạo đang mở, chưa gửi tên | E2.2 | FR-M90-01.04 |
| E2.2 | SYSTEM | Hệ thống kết thúc thao tác tạo, không tạo nhãn. | Danh mục giữ nguyên | END:CANCELLED | FR-M90-01.04 |

<!-- sc:branch SC-M90-001 E3 -->
| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống thông báo cần nhập tên, chưa tạo nhãn và cho phép sửa/gửi lại hoặc Hủy. | D2: tên rỗng; danh mục chưa đổi | E3.2 | FR-M90-01.03 |
| E3.2 | ACT-901 | Biên tập viên chọn Hủy thay vì sửa tên. | Yêu cầu tạo đang bị từ chối dữ liệu | E3.3 | FR-M90-01.03, FR-M90-01.04 |
| E3.3 | SYSTEM | Hệ thống kết thúc thao tác, không tạo nhãn. | Danh mục giữ nguyên, thao tác đã đóng | END:CANCELLED | FR-M90-01.04 |

<!-- sc:end SC-M90-001 -->

<!-- sc:scenario SC-M90-002 -->
### SC-M90-002

#### 1. Tên kịch bản chuẩn

Đổi tên nhãn hiện có — BF-M90-002, UC-M90-001, thuộc UC chính UC-M90-010.
Trigger: biên tập viên gửi mã nhãn và tên mới hợp lệ.

#### 2. Actor thực hiện

ACT-901 — Biên tập viên. Không có actor hỗ trợ.

#### 3. Tiền điều kiện

Biên tập viên có quyền ghi nhận nhãn, cung cấp mã nhãn và tên mới thỏa BR-M90-01.
Sự tồn tại của mã được kiểm trong luồng, không đặt là điều kiện bắt buộc
để tránh loại bỏ nhánh không tìm thấy. D3 cho luồng chính, D4 cho ngoại lệ.

#### 4. Hậu điều kiện

<!-- sc:post SC-M90-002 -->
| result | condition |
|---|---|
| SUCCESS | NH-200 mang tên Hình học; mã và các thuộc tính khác giữ nguyên; kết quả trả cho actor. |
| REJECTED | Không cập nhật bất kỳ nhãn nào; yêu cầu đổi tên đã kết thúc với thông báo không tìm thấy. |

#### 5. Các sự kiện chính

<!-- sc:main SC-M90-002 -->
| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-901 | Biên tập viên gửi yêu cầu đổi tên nhãn NH-200 thành Hình học. | D3: mã NH-200, tên mới Hình học | M2 | FR-M90-02.01 |
| M2 | SYSTEM | Hệ thống xác định nhãn tồn tại, kiểm tên hợp lệ, lưu tên mới, giữ thuộc tính khác và trả kết quả thành công. | D3: tên Hình → Hình học; mã NH-200 không đổi | END:SUCCESS | FR-M90-02.01, BR-M90-01 |

#### 6. Các ngoại lệ

<!-- sc:exceptions SC-M90-002 -->
| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | M1 gửi mã NH-999 không tồn tại và tên mới hợp lệ | E1.1 | FR-M90-02.02 |

<!-- sc:branch SC-M90-002 E1 -->
| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống thông báo không tìm thấy nhãn và kết thúc yêu cầu, không cập nhật danh mục. | D4: NH-999 không tồn tại; dữ liệu giữ nguyên | END:REJECTED | FR-M90-02.02 |

Không có lựa chọn Hủy/thử lại riêng trong nguồn của hành trình đổi tên;
không tự bổ sung. Việc từ chối tại đây là kết thúc theo FR-M90-02.02.

<!-- sc:end SC-M90-002 -->

## Truy vết và kiểm đủ

| Nguồn | BF | SC/bước/nhánh | Bao phủ trong scope |
|---|---|---|---|
| FR-M90-01.01 | BF-M90-001 | SC-M90-001 / M1, M2 | Đủ |
| FR-M90-01.02 | BF-M90-001 | SC-M90-001 / M3, M4, SUCCESS | Đủ |
| FR-M90-01.03 | BF-M90-001 | SC-M90-001 / E1, E3, nhập lại M4 | Đủ cả sửa/gửi và hủy sau lỗi |
| FR-M90-01.04 | BF-M90-001 | SC-M90-001 / E2, E3, CANCELLED | Đủ hai điểm hủy nguồn đã nêu |
| FR-M90-02.01 | BF-M90-002 | SC-M90-002 / M1, M2, SUCCESS | Đủ với tên mới hợp lệ |
| FR-M90-02.02 | BF-M90-002 | SC-M90-002 / E1, REJECTED | Đủ |
| BR-M90-01 | Cả hai BF | SC-M90-001 / M4, E1; SC-M90-002 / tiền điều kiện | Giới hạn: chưa có quy trình tên rỗng khi đổi tên |

Mọi nhánh tạo có đường kết thúc. Lỗi tên rỗng có chu kỳ thử lại và đường
hủy; không liệt kê vô hạn số lần. Hai luồng độc lập, không nhân tổ hợp tạo
và đổi tên như thể cùng một lần thực thi. Dữ liệu D1/D2 và D3/D4 là các
đường thay thế, không đồng thời đúng trong một lần chạy.

GAP-SC-M90-001: quy trình khi đổi tên với tên rỗng chưa được fixture đặc tả;
ngoài scope minh họa đã nêu. Nếu mở rộng phạm vi phải giải quyết GAP này.
Ví dụ không dùng làm kết luận toàn module đã đủ và không được phê duyệt.
