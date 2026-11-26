# Đầu vào giả lập để thực hành skill

[Vietnamese Doc]

**Chỉ là fixture phương pháp. M90 không phải module của iShare; các mã/luật
dưới đây không được dùng làm yêu cầu sản phẩm.** Boundary: hệ thống danh mục
minh họa. Tài liệu này cung cấp đủ nguồn để kiểm tra ví dụ mà không cần PDF.
Version: EXAMPLE-2; trạng thái: dữ liệu thực hành, không phải đã duyệt.

## FR giả lập

| id | requirement |
|---|---|
| FR-M90-01.01 | Biên tập viên có quyền ghi nhận nhãn có thể yêu cầu tạo nhãn mới; hệ thống cung cấp trường tên và lựa chọn Gửi hoặc Hủy. |
| FR-M90-01.02 | Khi biên tập viên gửi tên không rỗng, hệ thống tạo một nhãn mang tên đó và trả mã nhãn, tên, kết quả thành công. |
| FR-M90-01.03 | Khi gửi tên rỗng, hệ thống thông báo cần nhập tên, chưa tạo nhãn, cho phép sửa rồi gửi lại hoặc Hủy. Khi gửi lại, áp dụng cùng quy tắc kiểm tra. |
| FR-M90-01.04 | Khi biên tập viên chọn Hủy trước khi tạo thành công, hệ thống kết thúc thao tác, không tạo nhãn. |
| FR-M90-02.01 | Biên tập viên có quyền ghi nhận nhãn có thể gửi mã nhãn và tên mới không rỗng để đổi tên; nếu nhãn tồn tại, hệ thống lưu tên mới và trả mã, tên mới, kết quả thành công, giữ nguyên các thuộc tính khác. |
| FR-M90-02.02 | Nếu mã nhãn được gửi để đổi tên không tồn tại, hệ thống thông báo không tìm thấy và kết thúc yêu cầu, không thay đổi danh mục. |
| BR-M90-01 | Tên dùng để tạo hoặc đổi tên phải có ít nhất một ký tự không phải khoảng trắng. Không quy định giới hạn độ dài hoặc tính duy nhất trong fixture này. |

Không có quy định retry kỹ thuật, đăng nhập, xóa nhãn hoặc chính sách lưu
bản nháp. Không tự thêm chúng vào ví dụ.

## US giả lập

<!-- uc:actors -->
| id | name | kind |
|---|---|---|
| ACT-901 | Biên tập viên | human |

<!-- uc:catalog -->
| id | name | tier | level | primary | sources |
|---|---|---|---|---|---|
| UC-M90-010 | Quản lý nhãn | core | Summary | ACT-901 | FR-M90-01.01, FR-M90-02.01 |
| UC-M90-001 | Ghi nhận nhãn | sub | User goal | ACT-901 | FR-M90-01.01, FR-M90-01.02, FR-M90-01.03, FR-M90-01.04, FR-M90-02.01, FR-M90-02.02, BR-M90-01 |
| UC-M90-002 | Kiểm tra tên nhãn | sub | Subfunction | ACT-901 | BR-M90-01, FR-M90-01.02, FR-M90-01.03, FR-M90-02.01 |

<!-- uc:decomposition -->
| core | sub | rationale |
|---|---|---|
| UC-M90-010 | UC-M90-001 | Ghi nhận nhãn mới và đổi tên nhãn đã có trong phạm vi quản lý. |
| UC-M90-010 | UC-M90-002 | Kiểm tra tên bên trong tạo mới và đổi tên. |

### UC-M90-010

Core chỉ tổng hợp các hành trình, không yêu cầu tạo rồi đổi tên trong cùng
một lần thao tác. Không có quan hệ UML include/extend được quy định ở đây.

### UC-M90-001

Actor: ACT-901. Tiền điều kiện: biên tập viên có quyền ghi nhận nhãn.
Có hai trigger/hành trình độc lập: yêu cầu tạo mới; yêu cầu đổi tên bằng mã
đối tượng. Kết quả tương ứng là có nhãn mới; tên nhãn đã có được cập nhật.

- Tạo: actor yêu cầu → hệ thống cung cấp trường tên/lựa chọn → actor nhập/gửi
  → hệ thống kiểm tên và tạo nhãn. Tên rỗng: báo thiếu tên, cho sửa/gửi lại
  hoặc hủy. Chọn hủy ở lần nhập đầu hoặc sau lỗi: không tạo nhãn, kết thúc.
- Đổi tên: actor gửi mã và tên mới → hệ thống kiểm tồn tại và cập nhật/trả
  kết quả. Mã không tồn tại: thông báo không tìm thấy và kết thúc, không đổi
  danh mục. Dữ liệu tên mới trong hành trình minh họa này phải hợp lệ; fixture
  chưa đặc tả cách xử lý tên đổi mới rỗng, không nhận đã bao phủ tình huống đó.

Scope ví dụ: tạo mới với các nhánh đã nêu; đổi tên khi tên mới hợp lệ, gồm
mã tồn tại/không tồn tại. Giới hạn này phải xuất hiện trong bản scenario.

### UC-M90-002

Hệ thống kiểm tên theo BR-M90-01 tại lượt xử lý yêu cầu tạo/đổi tên của
UC-M90-001. Không có thao tác actor yêu cầu kiểm tên riêng. Đây là UC hỗ trợ
trong cùng lượt hệ thống, không có BF/SC độc lập. Khi tạo tên rỗng, trở về
nhánh sửa/hủy của tạo nhãn; khi tên hợp lệ, tiếp tục tạo/đổi tên và phản hồi.
Không thêm quan hệ UML chỉ từ bảng decomposition.
