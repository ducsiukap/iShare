# QA-M11 — Tái kiểm sau khắc phục

[Vietnamese Doc] — 11/11/2026, skill scenarios v1.4. Trạng thái Đang soạn theo nguồn nghiệp vụ.

## Kết quả hiện hành

| Kiểm tra | Kết quả |
| --- | --- |
| Validator chuẩn | PASS 29 UC, 22 BF, 22 SC, 257 nhánh E |
| Chuẩn hóa biến thể | 117 nhánh từ ID V lịch sử đã đăng ký E tại M1, bảng chuyển đổi ở cuối SC |
| Bảo toàn nội dung | 574 bước main/E/V lịch sử được đối chiếu trước/sau, chỉ đổi ID nhánh, vị trí dẫn và dữ liệu đã xác nhận trong QA-SC-02/03 |
| Phạm vi kiểm máy | Actor/nguồn, guard đăng ký, điểm thay/điểm vào, đích bước, luân phiên, khả năng kết thúc và hậu điều kiện của toàn bộ main/E |
| GAP và phê duyệt | Các GAP nguồn còn mở được liệt kê trong SC và báo cáo tái kiểm toàn bộ, đầu ra giữ Đang soạn |


Bản hiện hành [SC-M11.md](SC-M11.md). Kết quả toàn bộ và các quyết định còn chờ ở [báo cáo khắc phục](../QA-M01-M16-2026-11-11-khac-phuc.md).

## Bằng chứng lần soạn trước

Phần dưới lưu báo cáo của chính module này trước ngày chuyển đổi. Các số E/V và nhận xét giới hạn validator trong phần lịch sử phản ánh công cụ lúc soạn. Số liệu và kết quả áp dụng hiện tại nằm ở mục Kết quả hiện hành, các biến thể đã được kiểm bằng hợp đồng E.

# Kiểm tra scenario — M11 Group

[Vietnamese Doc] — 2026-11-11 — Skill scenarios v1.3 — Đang soạn.

Tài liệu chính: [SC-M11.md](SC-M11.md).

| Hạng mục | Kết quả |
|---|---|
| Scope UC | 5 chính +24 con =29 UC;30 mapping;32 include; không extend/generalization UC |
| Disposition | 19 UC sở hữu SC,6 embedded(015/016/021/022/023/024),4 aggregate(030/031/032/034) |
| BF/SC | 22 mục tiêu actor hoàn chỉnh; không BF chỉ xử lý nội bộ |
| Ngoại lệ E | 140 |
| Đường actor V | 117 |
| Mã nguồn | 17 nhóm +170 FR chi tiết +40 BR =227 hiệu lực; không mã bỏ |
| Hành vi nền | 6 AUT +6 RULE, không tính BF/SC |
| Nguồn/SVG | 17 baseline SHA-256;6 SVG XML/tập UC khớp US, không sửa/vẽ lại |
| GAP | 8 điểm theo NOTE01–08; GAP005 áp yêu cầu cụ thể vẫn hiện lối vào; TBD01 đã đóng |

## Chức năng đã triển khai

| SC | UC owner | Mục tiêu |
|---|---|---|
| [SC-M11-001](SC-M11.md#sc-m11-001) | UC-M11-001 | Tạo một nhóm và trở thành Owner đầu tiên |
| [SC-M11-002](SC-M11.md#sc-m11-002) | UC-M11-002 | Sửa thông tin và cài đặt một nhóm |
| [SC-M11-003](SC-M11.md#sc-m11-003) | UC-M11-003 | Xóa mềm một nhóm do mình làm Owner |
| [SC-M11-004](SC-M11.md#sc-m11-004) | UC-M11-004 | Xem danh sách các nhóm được phép xuất hiện |
| [SC-M11-005](SC-M11.md#sc-m11-005) | UC-M11-005 | Mở trang nhóm hoặc đọc nội dung nhóm theo quyền |
| [SC-M11-006](SC-M11.md#sc-m11-006) | UC-M11-006 | Xem danh sách thành viên kèm vai trò nhóm |
| [SC-M11-007](SC-M11.md#sc-m11-007) | UC-M11-007 | Tham gia nhóm hoặc gửi yêu cầu gia nhập theo cổng nhóm |
| [SC-M11-008](SC-M11.md#sc-m11-008) | UC-M11-008 | Rút yêu cầu tham gia đang chờ của mình |
| [SC-M11-009](SC-M11.md#sc-m11-009) | UC-M11-009 | Mời người khác đến nhóm bằng link chung hoặc lời mời |
| [SC-M11-010](SC-M11.md#sc-m11-010) | UC-M11-010 | Xét một yêu cầu tham gia nhóm |
| [SC-M11-011](SC-M11.md#sc-m11-011) | UC-M11-011 | Chặn một người gửi yêu cầu tham gia nhóm |
| [SC-M11-012](SC-M11.md#sc-m11-012) | UC-M11-011 | Xem danh sách người bị chặn tham gia nhóm |
| [SC-M11-013](SC-M11.md#sc-m11-013) | UC-M11-011 | Bỏ chặn một người khỏi danh sách chặn tham gia |
| [SC-M11-014](SC-M11.md#sc-m11-014) | UC-M11-012 | Bổ nhiệm một thành viên làm Group Mod |
| [SC-M11-015](SC-M11.md#sc-m11-015) | UC-M11-012 | Giáng một thành viên từ Group Mod về Member |
| [SC-M11-016](SC-M11.md#sc-m11-016) | UC-M11-013 | Kick một thành viên thuộc thẩm quyền khỏi nhóm |
| [SC-M11-017](SC-M11.md#sc-m11-017) | UC-M11-014 | Tự rời nhóm, bảo toàn nội dung và kế nhiệm khi cần |
| [SC-M11-018](SC-M11.md#sc-m11-018) | UC-M11-033 | Gửi bài mới hoặc gửi lại bài bị từ chối vào nhóm |
| [SC-M11-019](SC-M11.md#sc-m11-019) | UC-M11-017 | Tra cứu hàng chờ duyệt riêng của một nhóm |
| [SC-M11-020](SC-M11.md#sc-m11-020) | UC-M11-018 | Nhận giữ một bài chờ nhóm duyệt để xử lý |
| [SC-M11-021](SC-M11.md#sc-m11-021) | UC-M11-019 | Kết luận một bài đang chờ nhóm duyệt |
| [SC-M11-022](SC-M11.md#sc-m11-022) | UC-M11-020 | Gỡ một bài hoặc bình luận khỏi nhóm theo quyền nhóm |

22 chức năng dựa mục tiêu actor: UC011 có chặn/xem danh sách/bỏ chặn độc lập; UC012 có bổ nhiệm/giáng độc lập. Gửi lại thuộc gửi bài, loại bài/bình luận thuộc gỡ, phương thức link/người cụ thể thuộc mời, chấp nhận/từ chối thuộc xét/kết luận. Xem/nhận giữ/kết luận là ba mục tiêu của US, nhận giữ có xác nhận holder và chưa duyệt. Owner rời có chuyển trước/đưa ra sau, không BF chuyển quyền dang dở.

## Kiểm tra đã thực hiện

Validator skill PASS: metadata, sáu phần, actor/sourceID, mapping/inventory/BF, bước/đích và nhánh E thay đúng at, luân phiên chủ thể, đường tới terminal có hậu điều kiện. Main bắt đầu actor chính và kết thúc SYSTEM/SUCCESS của chức năng. Trường hợp gửi chờ xác nhận đã ghi nhận là kết quả bất đồng bộ đã được UC033 cho phép, chưa nhận là đã đăng. AI tự từ chối là REJECTED, khác người duyệt từ chối bài hợp lệ là SUCCESS của kết luận. Owner cuối không xác nhận là CANCELLED, không xóa.

V được kiểm riêng từ actor khởi tạo, actor hợp lệ, luân phiên, bước kế tiếp, SYSTEM cuối và result trong hậu điều kiện. Validator mặc định chỉ đi graph main/E; PASS không tự chứng minh V/đủ ngữ nghĩa. Không có nhánh chỉ SYSTEM gán thành BF, AI không khởi tạo gửi bài. Im lặng timeout không tạo hành động AI giả: SYSTEM gộp chờ5s/đợi2s/thử lại/chờ5s trong một lượt.

Đã đối chiếu FR chính thức với bản làm việc, nguồn/hash, UC/SVG/liên kết và walkthrough nghiệp vụ theo các ma trận trong SC. Không sửa FR/US/register/skill hoặc module khác. Lệnh chạy từ repo root:

```powershell
python -X utf8 .agent-instructions/skills/scenarios/tools/check_scenarios.py docs/specs/scenarios/M11/SC-M11.md --fr docs/specs/fr/FR-M11.md --fr docs/specs/fr/FR-M01.md --fr docs/specs/fr/FR-M02.md --fr docs/specs/fr/FR-M03.md --fr docs/specs/fr/FR-M04.md --fr docs/specs/fr/FR-M05.md --fr docs/specs/fr/FR-M06.md --fr docs/specs/fr/FR-M07.md --fr docs/specs/fr/FR-M08.md --fr docs/specs/fr/FR-M09.md --fr docs/specs/fr/FR-M10.md --fr docs/specs/fr/FR-M12.md --fr docs/specs/fr/FR-M13.md --fr docs/specs/fr/FR-M14.md --fr docs/specs/fr/FR-M15.md --us docs/specs/us/US-M11.md
```

## Đối soát nghiệp vụ

| Phép kiểm | Kết quả và giới hạn |
|---|---|
| Quyền | Owner/Group Mod theo đúng nhóm, khác Mod/Admin hệ thống. Admin qua cờ nhưng chịu membership/Private/Khóa/hạn tạo; quyền thấy danh tính thật không mở trangPrivate |
| Dữ liệu | Giá trị gửi và lưu nhất quán; tên100/101/mô tả500/501 dùng ASCII; role/id/mốc/câu trả lời theo cùng snapshot, không bắt SC nối tiếp |
| Gia nhập/mời | Đủ bốn tổ hợp/câu trả lời/trùng/chặn/quay lại/Guest; mời hoàn tất ở link hoặc thông báo, không thực thể accept/reject, không bypass cổng |
| Thành viên | Chặn khác kick/ban; bỏ chặn không tự thành Member; bổ nhiệm có mốc mới/thông báo, giáng không thông báo; kick giữ dữ liệu/điểm và quyền sau rời theo Public/Private |
| Owner | Rời còn người phải chọn/xác nhận/chuyển trước rồi ra; cuối xác nhận xóa, không xác nhận giữ; Khóa chặn Owner rời nhưng Member/Group Mod tự rời còn cho; tựkế nhiệm ưu tiên lần bổ nhiệm mới rồi join sớm, cũMember khi trở lại |
| Bài | Phân biệt AI tắt/lỗi/điểm, Owner/Admin; không Owner queue nhóm, Owner trung bình/lỗi queue Mod hệ thống, AdminOwner đăng ngay; Public/Private/ẩn danh giữ đúng phạm vi feed |
| Queue | Xem không cần holder và không loại bài mình; nhận không chiếm holder/cấm tự nhận; kết luận cần holder/quyền hiện tại/không tự duyệt/lý do khi từ chối; nhả30 phút từ lần thao tác cuối, không do người khác mở |
| Gỡ/xóa | Bài/bình luận có đầy đủ đường gỡ; giữ trạng thái đăng/tập xem/điểm/thông báo; quyết định nhóm không khiếu nại/tự hiện lại. Xóa nhóm toàn bộ không hiện, dữ liệu/điểm giữ, khác gỡ/ẩn |
| Nền/ranh giới | Sáu AUT được giữ trigger/dữ liệu/hiệu ứng/nguồn; M09 chấp nhận AI không quét lại, đã gửi lại không ghi đè; quyền Private khi xét cần làm rõ GAP008. Giao dịch/lỗi phát/role chuyển tiếp không tự quyết |
| Bao phủ | 227 mã đều có điểm đối soát; các đường chưa chốt giữ 8 GAP, không nhận mọi tổ hợp đã hoàn chỉnh hoặc nguồn đã được duyệt |

## Giới hạn còn lại

| GAP | Nguồn | Phần cần làm rõ |
|---|---|---|
| GAP-SC-M11-001 | NOTE-M11-01; FR-M11-11.01, FR-M11-11.02, BR-M11-26 | AUT002: hòa thời điểm bổ nhiệm/tham gia hoặc trạng thái tài khoản ứng viên kế nhiệm chưa chốt. Chỉ minh họa ứng viên có mốc khác nhau; không tự tie-break/lọc ACTIVE. Chặn đúng trường hợp ứng viên chưa xác định. |
| GAP-SC-M11-002 | NOTE-M11-02; FR-M11-01.08, FR-M11-01.09, FR-M11-02.11, BR-M11-31, BR-M11-08 | SC001/002/007/010: đơn vị Unicode/trim, độ dài câu hỏi/câu trả lời và phiên bản câu hỏi sau sửa chưa chốt. Biên dùng ASCII100/101 và500/501, không tự trim/chặn dài câu hỏi/snapshot câu cũ. |
| GAP-SC-M11-003 | NOTE-M11-03; BR-M11-05, FR-M11-14.08, FR-M11-14.01 | SC022: dùng quyền nhóm gỡ chính nội dung mình chưa rõ. Không tạo nhánh cho/chặn giả; quyền sửa/xóa của tác giả vẫn theo M03/M04, không đồng nghĩa gỡ nhóm. |
| GAP-SC-M11-004 | NOTE-M11-04; BR-M11-28, BR-M11-36, FR-M11-07.04 | SC008/012 và lượt xem danh sách của SC013: rút yêu cầu/đọc danh sách chặn khi nhóm Bị khóa chưa chốt. Không tự gán terminal SUCCESS/REJECTED cho hai trường hợp thiếu nguồn; bỏ chặn khi Khóa đã rõ là bị chặn. |
| GAP-SC-M11-005 | NOTE-M11-05; FR-M11-17.01, FR-M11-17.07, FR-M11-17.08, BR-M11-29 | SC004/UC024: câu chặn mọi thao tác so với vẫn hiện danh sách/lối vào. Áp dòng cụ thể17.07: liệt kê còn theo quyền, mở/tương tác bị chặn với người không ADMIN. Không chặn phần đã rõ; cần xác nhận cách diễn đạt nguồn, không coi list là mởPrivate. |
| GAP-SC-M11-006 | NOTE-M11-06; FR-M11-02.05, FR-M11-02.15, FR-M11-13.14, BR-M11-20, BR-M11-39, BR-M11-40, BR-M03-46 | SC018/020/021, AUT003/004: nhóm/Owner/role thay đổi giữa lúc AI/duyệt/khiếu nại chờ, Group Mod có bài chờ rồi thànhOwner, mất role holder chưa đủ hợp đồng. Kiểm quyền hiện tại, không tự nhả sớm/chuyển queue/xả bài; giữ ngoại lệ đã gửi lại không ghi đè. |
| GAP-SC-M11-007 | NOTE-M11-07; FR-M11-10.04, FR-M11-02.14, FR-M11-15.01, BR-M11-37 | SC002/003/017 và các nhánh phát sự kiện: giao dịch/thất bại/thứ tự phát, chấp nhận hàng loạt/đồng thời chưa chốt. Giữ thứ tự chuyển Owner trước khi đưa người cũ ra theo nguồn, không bịa atomicity/rollback/retry/outbox/thông báo lỗi. |
| GAP-SC-M11-008 | NOTE-M11-08; BR-M11-33, BR-M11-40, FR-M03-06.01, FR-M03-07.02, FR-M09-06.04, FR-M09-06.05 | SC005/AUT004: giao tiếp Private trong ngữ cảnh xét khiếu nại M09 chưa có mô tả tương ứng đủ rõ ở M11. Giữ quyền ngữ cảnh owner M09/M03/M08, không biến cấm mở trang thường thành cấm xét hợp lệ hoặc tự cho xem toàn Private. |

Tài liệu giữ Đang soạn. Kết quả kiểm tra là bằng chứng cấu trúc và review của agent, không là phê duyệt nghiệp vụ.

## Đối chiếu bổ sung

| Kiểm tra thực tế | Kết quả |
|---|---|
| Đường actor V | 117 đường, 268 bước; đúng người khởi tạo, chủ thể, thứ tự/đích và hậu điều kiện |
| Liên kết/baseline | 64 liên kết nội bộ và anchor hợp lệ;17 SHA-256 khớp nội dung nguồn |
| Phạm vi thay đổi | Chỉ tạo docs/specs/scenarios/M11/SC-M11.md và QA-M11.md; các nguồn và module trước không sửa |
