# Kiểm tra scenario M03 Post & Content

[Vietnamese Doc] — 2026-11-08 — Đang soạn để review.

Đầu ra: [SC-M03.md](SC-M03.md), theo skill scenarios v1.3.

| Hạng mục | Kết quả |
|---|---|
| Catalog | 4 UC chính, 17 UC con; giữ20 mapping |
| Cách bao phủ | 4 aggregate, 14 UC sở hữu mục tiêu actor, 3 embedded (UC002/003/005) |
| Hành trình | 17 BF/SC sáu phần |
| Nhánh E | 129 |
| Đường thay actor V | 32 |
| Quy tắc nền | 11 mục, không có scenario AUT chỉ SYSTEM |
| Truy vết | 17 nhóm +151 FR chi tiết +51 BR =219 mã, không mã thiếu vị trí |
| Sơ đồ | 5 SVG khớp ID thành viên với US |
| Baseline | FR chính thức khớp byte/hash bản làm việc; US/overview Chờ duyệt |

## Các chức năng

| SC | Mục tiêu |
|---|---|
| [SC-M03-001](SC-M03.md#sc-m03-001) | Soạn và lưu bài nháp |
| [SC-M03-004](SC-M03.md#sc-m03-004) | Gửi hoặc gửi lại bài để đăng theo chính sách |
| [SC-M03-006](SC-M03.md#sc-m03-006) | Duyệt bài đang nằm trong hàng chờ Mod hệ thống |
| [SC-M03-007](SC-M03.md#sc-m03-007) | Đọc bài viết và kết quả poll được phép |
| [SC-M03-008](SC-M03.md#sc-m03-008) | Ghi, đổi hoặc bỏ phiếu poll của mình |
| [SC-M03-009](SC-M03.md#sc-m03-009) | Đổi hạn kết thúc của poll đang mở |
| [SC-M03-011](SC-M03.md#sc-m03-011) | Sửa và lưu phiên bản bài đã gửi của mình |
| [SC-M03-012](SC-M03.md#sc-m03-012) | Xem các phiên bản lịch sử sửa bài |
| [SC-M03-013](SC-M03.md#sc-m03-013) | Tự ẩn bài đang đăng của mình |
| [SC-M03-014](SC-M03.md#sc-m03-014) | Đặt mức khóa cho bài viết |
| [SC-M03-015](SC-M03.md#sc-m03-015) | Xóa mềm bài của mình |
| [SC-M03-016](SC-M03.md#sc-m03-016) | Khôi phục bài đã xóa trong thời hạn |
| [SC-M03-017](SC-M03.md#sc-m03-017) | Hiện lại bài đã tự ẩn |
| [SC-M03-018](SC-M03.md#sc-m03-018) | Xem lại bài từ ngữ cảnh xử lý hoặc khiếu nại liên quan |
| [SC-M03-019](SC-M03.md#sc-m03-019) | Kết thúc poll ngay |
| [SC-M03-020](SC-M03.md#sc-m03-020) | Thêm lựa chọn vào poll đang mở của bài đã gửi |
| [SC-M03-021](SC-M03.md#sc-m03-021) | Mở khóa hoặc hạ mức khóa bài viết |

## Kiểm tra thực tế

Validator skill: PASS, không lỗi cấu trúc cho các main/E; kiểm actor, sáu phần, mapping/owner/BF, nguồn ID, đích bước và khả năng kết thúc. Các main khởi đầu actor chính, có actor/SYSTEM, kết thúc SYSTEM/SUCCESS.

Các bảng V thay toàn bộ đường theo actor Guest/Mod/Admin: kiểm riêng actor khởi tạo, luân phiên chủ thể, đích kết thúc và hậu điều kiện. Validator graph mặc định không duyệt V; PASS không tự chứng minh graph V. Nguồn ID trong bảng V vẫn được validator đối chiếu.

Lệnh kiểm từ repo root:

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M03/SC-M03.md --fr docs/specs/fr/FR-M03.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M02.md --fr docs/specs/fr/FR-M05.md --fr docs/specs/fr/FR-M09.md --fr docs/specs/fr/FR-M11.md --fr docs/specs/fr/FR-M13.md --us docs/specs/us/US-M03.md
```

## Review nghiệp vụ và giới hạn

- Mỗi BF là chức năng actor hoàn tất; dữ liệu/trạng thái/vai trò là nhánh. Đính kèm/poll/chính sách được khai triển trong luồng bao chứa.
- Quét mới≥0.9 tự từ chối; quét lại≥0.5, kể cả≥0.9, gắn cờ; lỗi mới chờ Mod, lỗi quét lại giữ hiển thị. Retry đúng một lần theo M13.
- Admin miễn quét nhưng bài nhóm vẫn theo M11; Owner và member vào đúng hàng nhóm hoặc hàng Mod hệ thống.
- Khóa không ẩn bài; khóa toàn bộ không chặn bookmark/báo cáo. Tác giả không vượt khóa Mod.
- Xóa đủ7×24h gắn cờ giữ toàn bộ dữ liệu; khôi phục Chờ duyệt về Nháp, không phục hồi Bị Mod ẩn. Xem lại xóa hẳn chỉ đúng ngữ cảnh, tác giả không nhận dữ liệu người báo cáo.
- Các lỗi/giới hạn dùng bộ dữ liệu cụ thể; vòng sửa/gửi lại biểu diễn bằng quay về bước kiểm, không nhân vô hạn. Các lớp cùng lỗi/kết quả ghi chung guard; không tự khẳng định thứ tự báo nhiều lỗi.

Chưa chốt phần trăm poll khi tổng lượt chọn=0; giữ các TBD lượt xem/SSR-SEO, ngưỡng tạm và giới hạn transaction từ nguồn. Agent chưa thẩm định độc lập hoặc phê duyệt hộ stakeholder; nguồn US chưa duyệt nên đầu ra tiếp tục là bản soạn.
