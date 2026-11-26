# scenarios — Hướng dẫn sử dụng

[Vietnamese Doc]

Bộ skill biến FR + tài liệu US của module thành các scenario sáu phần, có
dữ liệu minh họa, hành động actor/hệ thống và ngoại lệ có đường đi đầy đủ.
Dùng sau khi đã xác định UC chính và UC con bằng `use-case-analysis`.

## Cách gọi

```text
Dùng skill scenarios cho M01.
Đọc docs/specs/fr/FR-M01.md, docs/specs/us/US-M01.md và US-overview.md.
Thực hiện đủ bốn bước, viết scenario cho các luồng nghiệp vụ trong từng
nhóm UC chi tiết; giữ nguồn Chờ duyệt là Chờ duyệt, ghi riêng GAP còn thiếu.
```

```text
Dùng scenarios để viết các scenario của UC-M01-007.
Đọc FR-M01 và US-M01, giới hạn scope ở UC này và các nhánh của nó.
Không tuyên bố đã bao phủ toàn bộ module M01.
```

```text
Review SC-Mxx theo FR + US hiện hành: rà thiếu luồng, hai bước cùng chủ thể,
dữ liệu không nhất quán và ngoại lệ chưa có đường kết thúc.
```

Tên skill được tìm qua index của repository và pointer Claude. Trong phiên
Codex chưa tự liệt kê skill repo, chỉ định đường dẫn
`.agent-instructions/skills/scenarios/SKILL.md`; không cần cài toàn cục.

## Quy trình và sản phẩm

1. Chọn module, chốt phạm vi công việc và ghi baseline nguồn.
2. Kiểm kê các nhóm UC chi tiết: UC chính và toàn bộ UC con, kể cả UC dùng chung.
3. Xác định các chức năng actor thực hiện hoàn chỉnh: actor bắt đầu, tương
   tác với hệ thống, nhận kết quả; gắn UC hỗ trợ và nhánh vào từng chức năng.
4. Viết đủ scenario, kiểm tra bao phủ, từng đường đi và các điều kiện trước/sau.

Một file `SC-Mxx.md` chứa danh mục, truy vết, các scenario và QA. Từng scenario
có đúng sáu phần theo mẫu PDF. Luồng nghiệp vụ độc lập có scenario riêng;
nhánh của luồng được triển khai đầy đủ trong phần **Các ngoại lệ**, không
chỉ liệt kê tên lỗi. Khác trạng thái, quyền, lỗi hoặc phương thức không tự
động tạo luồng mới; phải có mục tiêu chức năng độc lập được nguồn hỗ trợ.

Ví dụ UC chính **Quản lý người dùng** có các chức năng độc lập thêm, cập
nhật, xác thực, xóa: tạo bốn luồng tương ứng, mỗi luồng từ actor yêu cầu đến
khi hệ thống trả kết quả hoàn tất chức năng. Kiểm dữ liệu, kiểm quyền, lưu
bản ghi là bước trong luồng; không tạo scenario riêng cho từng bước đó.
UC con hỗ trợ được đánh dấu `embedded` và truy vết đến bước/nhánh. Xem
[phép kiểm và ví dụ phân rã](steps/03-business-flows.md).

Đầu ra nằm trong `scenarios` **cùng cấp với `fr` và `us` của đầu vào**:

```text
<base>/
├── fr/FR-Mxx.md
├── us/US-Mxx.md
└── scenarios/
    └── Mxx/
        ├── SC-Mxx.md
        └── QA-Mxx.md  (nếu có báo cáo riêng)
```

Mỗi thư mục con dùng mã module lấy từ FR. Với M01 của dự án, đích là
`docs/specs/scenarios/M01/`. Skill chỉ tạo thư mục cho module đang triển khai
khi cần ghi đầu ra, không tạo sẵn thư mục các module chưa làm. Lưu cả bản
soạn/chờ duyệt tại đây, giữ nguyên trạng thái và
GAP; việc nằm trong `docs/specs` không tự chứng minh đã duyệt. Chỉ cache và
file trung gian nằm trong workspace agent. Bản cũ trong workspace được đưa
về đích chung khi có yêu cầu triển khai/tiếp tục, kèm sửa và kiểm liên kết.

Đây là tài liệu nghiệp vụ, chưa
phải bộ test case hoặc thiết kế màn hình/CSDL. Không cần tạo Word/PDF khi
người dùng chỉ yêu cầu scenario Markdown.

## Khi nguồn thiếu

Nguồn US chưa duyệt vẫn dùng để soạn nháp, có ghi trạng thái. Thiếu FR/US
hoặc mâu thuẫn làm thay đổi kết quả: ghi GAP cho phạm vi đó, triển khai phần
độc lập. Không tự thêm retry, hủy, lỗi mạng hoặc bước “OK” để kịch bản dài hơn.
Tác vụ chỉ do hệ thống thực hiện được gắn vào hành trình liên quan hoặc ghi
ở quy tắc nền; không tạo scenario riêng, không bịa actor để hợp thức hóa.

Skill v1.1 thay quy tắc v1.0 cho phép scenario một bước SYSTEM. Khi người
dùng yêu cầu cập nhật skill, chỉ sửa skill; không tự chạy lại hoặc chỉnh
đầu ra module cũ. Khi có yêu cầu áp dụng lại, rà ranh giới mục tiêu trước,
giữ truy vết ID cũ → gộp/chuyển thành nhánh/bước, không tái dùng ID sai nghĩa.

Xem [SKILL.md](SKILL.md), [template](output/scenario-template.md),
[ví dụ](references/worked-example.md) và [lệnh kiểm tra](tools/README.md).
