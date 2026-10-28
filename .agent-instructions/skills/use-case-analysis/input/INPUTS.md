# Đầu vào và baseline

[Vietnamese Doc]

Lệnh chạy từ repository root. Link trong US tương đối với file chứa link,
không gắn ổ đĩa cụ thể hoặc dùng file URI.

| Chế độ | Nguồn | Đầu ra |
|---|---|---|
| Module | docs/specs/fr/FR-Mxx.md có trạng thái Đã chốt | docs/specs/us/US-Mxx.md |
| Toàn dự án | Tập FR đã chốt thuộc phạm vi yêu cầu | docs/specs/us/US-overview.md |
| Một phần/review | Tập mã/tài liệu được chỉ định, ghi rõ giới hạn | Vị trí yêu cầu hoặc workspace draft |

Thiếu nguồn hoặc nguồn chưa chốt: thống kê phần đã có, ghi điểm cần làm rõ;
không chốt đặc tả phần thiếu. Không tự mở rộng scope khi đọc FR liên module.

## Đọc theo nội dung, không hard-code số mục

- Metadata, mục đích và trong/ngoài phạm vi: subject và baseline.
- Vai trò, ma trận quyền, giao tiếp dịch vụ ngoài: actor chính/hỗ trợ, quyền.
- Danh sách chức năng: kiểm kê nhóm FR.
- Yêu cầu chi tiết, BR, trạng thái, giao tiếp module, TBD và lịch sử sửa:
  xây luồng, tác vụ tự động, quyền xem và truy vết.
- FR được trích và review-cross-module.md: đối chiếu giao tiếp khi cần;
  báo cáo cũ không thay FR hiện hành.
- US-overview.md và US module đã có: tái sử dụng actor/UC ID, ownership.
  Chưa có thì lập danh mục trong scope, không tự viết lại các module khác.

Ghi đường dẫn và phiên bản từng FR đã dùng vào bảng nguồn. Tài liệu phương
pháp không cung cấp tính năng sản phẩm. Mâu thuẫn FR/register phát hiện sau
phải quay về phân tích yêu cầu, không tự bỏ qua FR đã chốt.

## ID và phạm vi

- UC mới: UC-Mxx-nnn; actor chung: ACT-nnn; tự động: AUT-Mxx-nnn;
  quy tắc: RULE-Mxx-nnn. Overview tham chiếu UC của module sở hữu.
- Giữ mã cũ đã duyệt; cần đổi thì lập old → new và xử lý tham chiếu trong
  scope được yêu cầu. Không tái đánh số toàn dự án.
- Viết đầy đủ mọi mã nguồn, ví dụ FR-M01-07.01, FR-M01-07.02;
  không dùng dạng rút gọn 07.01–07.02.
- Phạm vi nhóm FR gồm các mã con còn hiệu lực. BR được dùng và FR liên
  module vẫn phải tham chiếu chính xác.
- Ghi riêng mã đã bỏ cùng bằng chứng, không tạo lại hành vi.
- Các mã AUT/RULE là nơi đặc tả hành vi, không phải lý do miễn bao phủ.

Dùng [template hiện hành](../output/us-template.md);
không lấy quan hệ trong mẫu M01 cũ làm đáp án mặc định.

