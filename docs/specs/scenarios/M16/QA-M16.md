# QA-M16 — Chat & Messaging

[Vietnamese Doc]

Ngày kiểm 2026-11-11. Đầu ra Đang soạn do6 GAP nguồn, US-M16/US-overview còn Chờ duyệt. PASS dưới đây xác nhận các kiểm tra đã thực hiện trên phạm vi có hợp đồng, các guard chưa chốt giữ đúng GAP.

## Kết quả và phạm vi

| Kiểm tra | Phương pháp | Kết quả thực tế | Giới hạn |
|---|---|---|---|
| Kiểm kê | Đối chiếu uc:catalog/decomposition/relations | PASS 24 UC, 26 mapping, 25 include. 4 aggregate, 15 scenario, 5 embedded, 15 BF/15 SC | Không dùng danh sách UC chọn ở overview để cắt bớt module |
| Cấu trúc native | check_scenarios.py với 9 FR và US-M16 | PASS 24 UC, 15 BF, 15 SC, 88 ngoại lệ E | Native chưa kiểm ngữ nghĩa và đồ thị V |
| Walkthrough | check_paths và review hành trình | PASS 162 đường, 88 E, 59 V. Sáu phần/SC, chủ thể hợp lệ/luân phiên, main khởi tạo actor và kết thúc SYSTEM | E thay đúng bước, V thay từ đầu. Không tạo giả thao tác để xen kẽ SYSTEM |
| Đối soát độc lập file đầu ra | Đọc lại Markdown và parse bảng V, đích next, hậu điều kiện, liên kết và SHA-256 | PASS 59 đường V với 130 bước, 41 liên kết cục bộ, 18 hash baseline | Kiểm trên file đã ghi, bổ sung kiểm cấu trúc native |
| Nguồn | So 177định nghĩa FR/BR phần thân với vị trí event/nền | PASS 17 nhóm/127 chi tiết/33 BR có vị trí truy vết | GAP không được coi là đã có chính sách đủ |
| Guard US | Bảng đối soát từng nhánh US với E/V hoặc GAP | PASS 50 nhánh có quyết định bao phủ | Các ví dụ helper là nhánh tại caller, không BF riêng |
| AUT/RULE | Review 3 AUT/8 RULE với N1–N10 và điểm gọi | PASS đầy đủ trigger/điều kiện/hiệu ứng và phạm vi | AUT001 theo tài khoản, không có actor khởi tạo nên ở nền |
| Dữ liệu | Kiểm độc lập trang 20, mốc/receipt, rate, 300 giây, cap và FIFO | PASS 45 tin→20+20+5, 23 cuộc→20+3, 299/300 được 301 từ chối, 98+5→100 với 3 bị từ chối | D giả lập độc lập. Tie/pending stale/atomic/receipt cựu ở GAP |
| Quyền | Review từng đường actor/cờ/membership/role/sender | PASS ADMIN miễn cờ còn role, Guest/BANNED từ chối, cựu chỉ lịch sử trước cutoff, Admin nhóm không miễn cờ | BANNED target khác BANNED caller, ACTIVE là dữ liệu chuẩn không thành luật chuyển quyền |
| Tách BF | Phép kiểm mục tiêu actor độc lập, walkthrough đầu-cuối | PASS 15 mục tiêu. Tạo pending là kết quả của yêu cầu bất đồng bộ, duyệt là chức năng Admin riêng | Gửi, thu hồi, đọc, thêm, lấy link, xin, duyệt, đổi cờ, xóa, đổi tên, chuyển, rời không ghép bắt buộc |


## Baseline FR chính thức và bản làm việc

| FR chính thức | Bản làm việc | SHA chính thức | SHA làm việc | Kết quả |
|---|---|---|---|---|
| docs/specs/fr/FR-M16.md | .agents/.claude/system_analysis/output/fr/FR-M16.md | c8ef96e52479806637b0eac334bbe57fa9fe4f73bdacc73913467960050f0671 | c8ef96e52479806637b0eac334bbe57fa9fe4f73bdacc73913467960050f0671 | Khớp byte |
| docs/specs/fr/FR-M01.md | .agents/.claude/system_analysis/output/fr/FR-M01.md | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a | Khớp byte |
| docs/specs/fr/FR-M02.md | .agents/.claude/system_analysis/output/fr/FR-M02.md | e86aca71e0415ee2e121a4fdc3628261be335e9d266fcf6e9654b2fdf3cd357e | e86aca71e0415ee2e121a4fdc3628261be335e9d266fcf6e9654b2fdf3cd357e | Khớp byte |
| docs/specs/fr/FR-M07.md | .agents/.claude/system_analysis/output/fr/FR-M07.md | 05fb18237e049e3742d06c49b824e76e238c7587e7099b8dc4a84a2e1daf4f5b | 05fb18237e049e3742d06c49b824e76e238c7587e7099b8dc4a84a2e1daf4f5b | Khớp byte |
| docs/specs/fr/FR-M08.md | .agents/.claude/system_analysis/output/fr/FR-M08.md | a92e6e370038af300a9ddd735414dcb2c4fbffe07c81abaaa3c92dff447c25f0 | a92e6e370038af300a9ddd735414dcb2c4fbffe07c81abaaa3c92dff447c25f0 | Khớp byte |
| docs/specs/fr/FR-M09.md | .agents/.claude/system_analysis/output/fr/FR-M09.md | 8ad8ae5e148c6e446f4bfec7f6e74ba9566c54747a0eda37a3930e94ab96faea | 8ad8ae5e148c6e446f4bfec7f6e74ba9566c54747a0eda37a3930e94ab96faea | Khớp byte |
| docs/specs/fr/FR-M10.md | .agents/.claude/system_analysis/output/fr/FR-M10.md | 3e1010a76db6ef4c5870f42765e669095efc8d38c202271d9b200d2da0823d2c | 3e1010a76db6ef4c5870f42765e669095efc8d38c202271d9b200d2da0823d2c | Khớp byte |
| docs/specs/fr/FR-M11.md | .agents/.claude/system_analysis/output/fr/FR-M11.md | 1908d300f75d5f7fa0fd5b31b1d375bc6a63ccd42da254de6e9d0d7d9ef16307 | 1908d300f75d5f7fa0fd5b31b1d375bc6a63ccd42da254de6e9d0d7d9ef16307 | Khớp byte |
| docs/specs/fr/FR-M13.md | .agents/.claude/system_analysis/output/fr/FR-M13.md | 54630715cc1e391b9ea361247784af26200fc2f01c1b1da96ea56ed1f75f9982 | 54630715cc1e391b9ea361247784af26200fc2f01c1b1da96ea56ed1f75f9982 | Khớp byte |


## Sơ đồ nguồn

| ID | Artifact | Số UC | Đối chiếu |
|---|---|---|---|
| C-M16 | [docs/specs/us/diagrams/M16/C-M16.svg](../../us/diagrams/M16/C-M16.svg) | 4 | PASS tập UC theo XML SVG |
| D-M16-030 | [docs/specs/us/diagrams/M16/D-M16-030.svg](../../us/diagrams/M16/D-M16-030.svg) | 7 | PASS tập UC theo XML SVG |
| D-M16-031 | [docs/specs/us/diagrams/M16/D-M16-031.svg](../../us/diagrams/M16/D-M16-031.svg) | 6 | PASS tập UC theo XML SVG |
| D-M16-032 | [docs/specs/us/diagrams/M16/D-M16-032.svg](../../us/diagrams/M16/D-M16-032.svg) | 8 | PASS tập UC theo XML SVG |
| D-M16-033 | [docs/specs/us/diagrams/M16/D-M16-033.svg](../../us/diagrams/M16/D-M16-033.svg) | 9 | PASS tập UC theo XML SVG |


Các SVG được parse XML và so tập ID với uc:diagrams. Thành viên sơ đồ được đối chiếu metadata, quan hệ và điều kiện được đối chiếu hợp đồng US.

## Giới hạn còn lại

GAP001 gồm lỗi ghi/giao, gửi lại/reconnect/đồng thời và nguyên tử tạo nhóm. GAP002 gồm nhóm rỗng/thứ tự hòa/empty UI. GAP003 gồm mốc và receipt cựu. GAP004 gồm pending trùng/stale/tài khoản đổi trạng thái/FIFO hòa. GAP005 gồm danh tính receipt và mốc vào lại. GAP006 gồm đích chuyển quyền không thể khôi phục/nhóm0/ngữ cảnh AUT đồng thời. Chi tiết và tác động giữ nguyên từ NOTE-M16-01–06 trong [SC-M16.md](SC-M16.md#7-gap-trạng-thái-và-kiểm-tra).

Giá trị người dùng, tên nhóm, mã cuộc/tin/pending, thời điểm và số lượng là giả lập, được chọn để kích hoạt guard rõ. Không có quyết định yêu cầu mới. FR/US/register/skill và scenario module khác được giữ làm nguồn. Kết quả chưa được người dùng phê duyệt.

## Lệnh kiểm tra

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M16/SC-M16.md --fr docs/specs/fr/FR-M16.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M02.md --fr docs/specs/fr/FR-M07.md --fr docs/specs/fr/FR-M08.md --fr docs/specs/fr/FR-M09.md --fr docs/specs/fr/FR-M10.md --fr docs/specs/fr/FR-M11.md --fr docs/specs/fr/FR-M13.md --us docs/specs/us/US-M16.md
```

Liên kết đầu ra [SC-M16.md](SC-M16.md). Baseline nguồn và SHA-256 tại mục 1 của SC.
