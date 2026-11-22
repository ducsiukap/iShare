---
module: M15
ten_module: Analytics & Stats
ma_tai_lieu: DB-M15
phien_ban: 1.0
trang_thai: Đã chốt
ngay: 2026-11-22
tac_gia: Phạm Văn Đức
nguon: CD-M15 v1.0
steps_completed: [1, 2, 3, 4, 5]
---
# Thiết kế cơ sở dữ liệu — M15 Analytics & Stats

<!-- [Vietnamese Doc] Tài liệu tiếng Việt; tên bảng, cột, kiểu viết tiếng Anh. -->

| Mã tài liệu | DB-M15 |
|---|---|
| Dự án | iShare |
| Module | M15 — Analytics & Stats |
| Đầu vào | CD-M15 phiên bản 1.0 |
| Trạng thái | Đã chốt |
| Phiên bản | 1.0 |
| Ngày | 2026-11-22 |
| Tác giả | Phạm Văn Đức |

<!-- Quy ước chung cho mọi bảng dưới đây:
     - Không đổi tên cột, không xóa cột, không đổi số mục: tool đọc bảng theo số mục và tên cột.
     - Ô không có nội dung ghi "—". Mục chưa tới bước làm thì để dòng "(Chưa làm — bước N)".
     - Bảng chỉ sinh từ lớp, cột chỉ sinh từ thuộc tính, khóa ngoại chỉ sinh từ quan hệ (giữ mã R-Mxx-nn).
     - Mục 6 do build_schema.py sinh; không sửa tay.
     - Quy ước dùng (data-model/conventions.md): QU-06, QU-07; QU-08 cách ghép tên khóa ngoại và QU-09 kiểu cột
       (người dùng xác nhận 2026-11-22, DB-M01 Q-01, Q-02). Mọi khóa chính id kiểu bigint (QU-02: long). -->

## 1. Bảng

| Bảng | Từ lớp | Nhóm | Sở hữu | Ghi chú |
|---|---|---|---|---|
| user_stats | UserStat | Thống kê | M15 | Lớp thống kê: các cột được xét loại ở bước 5 |
| post_stats | PostStat | Thống kê | M15 | Lớp thống kê: các cột được xét loại ở bước 5 |
| comment_stats | CommentStat | Thống kê | M15 | Lớp thống kê: các cột được xét loại ở bước 5 |
| report_stats | ReportStat | Thống kê | M15 | Lớp thống kê: các cột được xét loại ở bước 5 |
| warning_stats | WarningStat | Thống kê | M15 | Lớp thống kê: các cột được xét loại ở bước 5 |
| ban_stats | BanStat | Thống kê | M15 | Lớp thống kê: các cột được xét loại ở bước 5 |
| appeal_stats | AppealStat | Thống kê | M15 | Lớp thống kê: các cột được xét loại ở bước 5 |

## 2. Cột

### 2.1 Cột từ thuộc tính

| Bảng | Cột | Kiểu | Null | Duy nhất | Từ thuộc tính | Ghi chú |
|---|---|---|---|---|---|---|
| user_stats | period | varchar(30) | Không | Không | UserStat.period | Giá trị: TODAY, LAST_7_DAYS, LAST_30_DAYS, ALL_TIME; Chọn sẵn ALL_TIME; ranh giới theo giờ Việt Nam, 7 ngày và 30 ngày theo ngày lịch gồm hôm nay (BR-M15-03, BR-M15-04) |
| user_stats | count_by_status | jsonb | Không | Không | UserStat.countByStatus | Map<UserStatGroup, Integer> lưu dạng jsonb (khóa → số đếm); Tài khoản tạo trong khoảng, mỗi tài khoản đúng một nhóm theo trạng thái lúc xem (BR-M15-20, BR-M15-18); Dẫn xuất ở CD: xét ở bước 5 |
| user_stats | registration_trend | jsonb | Không | Không | UserStat.registrationTrend | Map<Instant, Integer> lưu dạng jsonb (khóa → số đếm); Số tài khoản tạo theo từng giờ, ngày hoặc tháng của khoảng, kể cả chưa hoàn tất hoặc đã xóa (BR-M15-20, BR-M15-19); Dẫn xuất ở CD: xét ở bước 5 |
| user_stats | count_by_role | jsonb | Không | Không | UserStat.countByRole | Map<UserRole, Integer> lưu dạng jsonb (khóa → số đếm); Chỉ tài khoản đã xong bước 3, không DELETED (BR-M15-20); Dẫn xuất ở CD: xét ở bước 5 |
| user_stats | count_by_grade_level | jsonb | Không | Không | UserStat.countByGradeLevel | Map<GradeLevelGroup, Integer> lưu dạng jsonb (khóa → số đếm); Chỉ tài khoản đã xong bước 3, không DELETED (BR-M15-20); Dẫn xuất ở CD: xét ở bước 5 |
| user_stats | count_by_warning_level | jsonb | Không | Không | UserStat.countByWarningLevel | Map<WarningLevelGroup, Integer> lưu dạng jsonb (khóa → số đếm); Mỗi tài khoản đúng một nhóm: tài khoản BANNED chỉ ở nhóm BANNED, ADMIN ở nhóm CLEAN; chỉ tài khoản đã xong bước 3, không DELETED (BR-M15-20); Dẫn xuất ở CD: xét ở bước 5 |
| post_stats | period | varchar(30) | Không | Không | PostStat.period | Giá trị: TODAY, LAST_7_DAYS, LAST_30_DAYS, ALL_TIME; Như UserStat.period (BR-M15-03, BR-M15-04) |
| post_stats | count_by_publish_state | jsonb | Không | Không | PostStat.countByPublishState | Map<PostStateGroup, Integer> lưu dạng jsonb (khóa → số đếm); Bài tạo trong khoảng theo Post.createdAt; không đếm nháp; bài nhóm, ẩn danh, bị ẩn vì tác giả, vì nhóm, bị gỡ khỏi nhóm đếm theo trạng thái của chính bài (BR-M15-21); Dẫn xuất ở CD: xét ở bước 5 |
| post_stats | count_by_mod_state | jsonb | Không | Không | PostStat.countByModState | Map<ModState, Integer> lưu dạng jsonb (khóa → số đếm); Bài tạo trong khoảng, không đếm nháp (BR-M15-21); Dẫn xuất ở CD: xét ở bước 5 |
| post_stats | new_post_trend | jsonb | Không | Không | PostStat.newPostTrend | Map<Instant, Integer> lưu dạng jsonb (khóa → số đếm); Số bài theo từng giờ, ngày hoặc tháng của khoảng, theo thời điểm đăng (BR-M15-21, BR-M15-19); Dẫn xuất ở CD: xét ở bước 5 |
| post_stats | count_by_topic | jsonb | Không | Không | PostStat.countByTopic | Map<String, Integer> lưu dạng jsonb (khóa → số đếm); Khóa là tên Topic trong danh mục hiện tại; bài nhiều Topic đếm một lần ở mỗi Topic; bài của Topic đã gộp đếm ở Topic đích (BR-M15-17, BR-M15-21); Dẫn xuất ở CD: xét ở bước 5 |
| comment_stats | period | varchar(30) | Không | Không | CommentStat.period | Giá trị: TODAY, LAST_7_DAYS, LAST_30_DAYS, ALL_TIME; Như UserStat.period |
| comment_stats | new_comment_trend | jsonb | Không | Không | CommentStat.newCommentTrend | Map<Instant, Integer> lưu dạng jsonb (khóa → số đếm); Số bình luận theo từng giờ, ngày hoặc tháng theo thời điểm đăng, kể cả bình luận về sau bị ẩn hoặc bị xóa (BR-M15-21, BR-M15-19); Dẫn xuất ở CD: xét ở bước 5 |
| report_stats | period | varchar(30) | Không | Không | ReportStat.period | Giá trị: TODAY, LAST_7_DAYS, LAST_30_DAYS, ALL_TIME; Như UserStat.period |
| report_stats | count_by_status | jsonb | Không | Không | ReportStat.countByStatus | Map<ReportStatGroup, Integer> lưu dạng jsonb (khóa → số đếm); Đếm theo từng báo cáo, không theo vụ; mục do AI tạo, kể cả yêu cầu ban của hệ thống, là một báo cáo (BR-M15-11, BR-M15-22); Dẫn xuất ở CD: xét ở bước 5 |
| report_stats | count_by_reason | jsonb | Không | Không | ReportStat.countByReason | Map<ReportTargetType, Map<ReportReason, Integer>> lưu dạng jsonb (khóa → số đếm); Tách theo loại đối tượng: bài viết 8, bình luận 7, người dùng 2, nhóm 4 lý do; không gộp lý do cùng tên của hai loại (BR-M15-12, BR-M15-22); Dẫn xuất ở CD: xét ở bước 5 |
| warning_stats | period | varchar(30) | Không | Không | WarningStat.period | Giá trị: TODAY, LAST_7_DAYS, LAST_30_DAYS, ALL_TIME; Như UserStat.period |
| warning_stats | level_trend | jsonb | Không | Không | WarningStat.levelTrend | Map<Instant, Map<WarningLevel, Integer>> lưu dạng jsonb (khóa → số đếm); Số cảnh cáo theo từng giờ, ngày hoặc tháng, tách theo mức LIGHT, MEDIUM, HEAVY đạt ngay sau cảnh cáo; gồm cảnh cáo do AI và do Mod, Admin, kể cả về sau bị bỏ hoặc bị lật (BR-M15-13, BR-M15-22); Dẫn xuất ở CD: xét ở bước 5 |
| ban_stats | period | varchar(30) | Không | Không | BanStat.period | Giá trị: TODAY, LAST_7_DAYS, LAST_30_DAYS, ALL_TIME; Như UserStat.period |
| ban_stats | ban_trend | jsonb | Không | Không | BanStat.banTrend | Map<Instant, Map<BanKind, Integer>> lưu dạng jsonb (khóa → số đếm); Số ban theo từng giờ, ngày hoặc tháng, tách TEMPORARY và PERMANENT, kể cả ban về sau bị lật (BR-M15-14, BR-M15-22); Dẫn xuất ở CD: xét ở bước 5 |
| ban_stats | unban_trend | jsonb | Không | Không | BanStat.unbanTrend | Map<Instant, Integer> lưu dạng jsonb (khóa → số đếm); Chỉ đếm thao tác gỡ ban của Mod, Admin (dòng ModerationLog UNBAN); ban hết hạn, bị lật không tính (BR-M15-14, BR-M15-22); Dẫn xuất ở CD: xét ở bước 5 |
| appeal_stats | period | varchar(30) | Không | Không | AppealStat.period | Giá trị: TODAY, LAST_7_DAYS, LAST_30_DAYS, ALL_TIME; Như UserStat.period |
| appeal_stats | count_by_type | jsonb | Không | Không | AppealStat.countByType | Map<AppealType, Integer> lưu dạng jsonb (khóa → số đếm); Khiếu nại bài bị gỡ và khiếu nại gộp thuộc POST (BR-M15-10); Dẫn xuất ở CD: xét ở bước 5 |
| appeal_stats | count_by_result | jsonb | Không | Không | AppealStat.countByResult | Map<AppealResultGroup, Integer> lưu dạng jsonb (khóa → số đếm); Đếm theo kết quả hiện tại của khiếu nại (BR-M15-10, BR-M15-22); Dẫn xuất ở CD: xét ở bước 5 |

### 2.2 Thuộc tính đối tượng không chuyển

Không có: lớp của module không có thuộc tính đối tượng.

| Lớp | Thuộc tính | Kiểu | Lý do không chuyển |
|---|---|---|---|
| — | — | — | — |

## 3. Quan hệ giữa các bảng

"Dạng" đọc theo thứ tự Bảng A – Bảng B; quan hệ 1-n viết bảng phía 1 ở cột Bảng A.

Bản thiết kế lớp không có quan hệ thành phần – toàn thể và không có kế thừa.

| ID | Bảng A | Bảng B | Dạng | Xử lý | Ghi chú |
|---|---|---|---|---|---|
| — | — | — | — | — | — |

R-M15-01 (UserStat → User), R-M15-02 (PostStat → Post), R-M15-03 (CommentStat → Comment), R-M15-04 (ReportStat → Report), R-M15-05 (WarningStat → Warning), R-M15-06 (BanStat → Ban), R-M15-07 (AppealStat → Appeal) (Phụ thuộc) không sinh quan hệ giữa các bảng: lớp phụ thuộc chỉ dùng lớp đích để tính, không giữ đối tượng của nó.

Không có quan hệ n-n.

## 4. Khóa

### 4.1 Khóa chính

| Bảng | Khóa chính | Ghi chú |
|---|---|---|
| user_stats | Không có | Lớp thống kê không có id, không có lớp cha; bảng bị loại ở bước 5 |
| post_stats | Không có | Lớp thống kê không có id, không có lớp cha; bảng bị loại ở bước 5 |
| comment_stats | Không có | Lớp thống kê không có id, không có lớp cha; bảng bị loại ở bước 5 |
| report_stats | Không có | Lớp thống kê không có id, không có lớp cha; bảng bị loại ở bước 5 |
| warning_stats | Không có | Lớp thống kê không có id, không có lớp cha; bảng bị loại ở bước 5 |
| ban_stats | Không có | Lớp thống kê không có id, không có lớp cha; bảng bị loại ở bước 5 |
| appeal_stats | Không có | Lớp thống kê không có id, không có lớp cha; bảng bị loại ở bước 5 |

### 4.2 Khóa ngoại

Không có khóa ngoại.

| Bảng | Cột | Kiểu | Null | Duy nhất | Tham chiếu | Từ quan hệ | Ghi chú |
|---|---|---|---|---|---|---|---|
| — | — | — | — | — | — | — | — |

## 5. Loại dư thừa

### 5.1 Cột bị loại

| Bảng | Cột | Loại dư thừa | Căn cứ | Cách có lại giá trị |
|---|---|---|---|---|
| user_stats | period | Dẫn xuất | Thuộc tính của lớp thống kê; là tham số khoảng thời gian Admin chọn (BR-M15-03), không phải dữ liệu nghiệp vụ | Admin chọn ở bộ lọc (mặc định ALL_TIME); dùng làm điều kiện trên cột thời điểm của bảng nguồn theo giờ Việt Nam (BR-M15-04) |
| user_stats | count_by_status | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-20, BR-M15-18; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm users tạo trong khoảng (created_at) theo nhóm trạng thái lúc xem: users.status, users.verification_level (chờ xác minh email, chờ hoàn tất hồ sơ) trong khoảng đã chọn |
| user_stats | registration_trend | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-20, BR-M15-19; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm users theo created_at gom theo từng giờ, ngày hoặc tháng của khoảng, kể cả chưa hoàn tất hoặc đã xóa trong khoảng đã chọn |
| user_stats | count_by_role | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-20; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm users theo role, chỉ tài khoản đã xong bước 3, không DELETED trong khoảng đã chọn |
| user_stats | count_by_grade_level | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-20; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm theo profiles.grade_level (trống → NOT_SET), chỉ tài khoản đã xong bước 3, không DELETED trong khoảng đã chọn |
| user_stats | count_by_warning_level | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-20; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm theo mức từ user_warning_statuses.warning_count; tài khoản BANNED vào nhóm BANNED, ADMIN vào CLEAN; chỉ tài khoản đã xong bước 3, không DELETED trong khoảng đã chọn |
| post_stats | period | Dẫn xuất | Thuộc tính của lớp thống kê; là tham số khoảng thời gian Admin chọn (BR-M15-03), không phải dữ liệu nghiệp vụ | Admin chọn ở bộ lọc (mặc định ALL_TIME); dùng làm điều kiện trên cột thời điểm của bảng nguồn theo giờ Việt Nam (BR-M15-04) |
| post_stats | count_by_publish_state | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-21; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm posts tạo trong khoảng (created_at) theo publish_state, is_permanently_deleted; không đếm DRAFT trong khoảng đã chọn |
| post_stats | count_by_mod_state | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-21; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm posts tạo trong khoảng theo mod_state; không đếm DRAFT trong khoảng đã chọn |
| post_stats | new_post_trend | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-21, BR-M15-19; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm posts theo published_at gom theo từng giờ, ngày hoặc tháng của khoảng trong khoảng đã chọn |
| post_stats | count_by_topic | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-17, BR-M15-21; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm post_topics của bài trong khoảng theo topics.name của danh mục hiện tại trong khoảng đã chọn |
| comment_stats | period | Dẫn xuất | Thuộc tính của lớp thống kê; là tham số khoảng thời gian Admin chọn (BR-M15-03), không phải dữ liệu nghiệp vụ | Admin chọn ở bộ lọc (mặc định ALL_TIME); dùng làm điều kiện trên cột thời điểm của bảng nguồn theo giờ Việt Nam (BR-M15-04) |
| comment_stats | new_comment_trend | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-21, BR-M15-19; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm comments theo published_at gom theo từng giờ, ngày hoặc tháng, kể cả bình luận bị ẩn, bị xóa trong khoảng đã chọn |
| report_stats | period | Dẫn xuất | Thuộc tính của lớp thống kê; là tham số khoảng thời gian Admin chọn (BR-M15-03), không phải dữ liệu nghiệp vụ | Admin chọn ở bộ lọc (mặc định ALL_TIME); dùng làm điều kiện trên cột thời điểm của bảng nguồn theo giờ Việt Nam (BR-M15-04) |
| report_stats | count_by_status | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-11, BR-M15-22; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm reports theo report_cases.status, conclusion của vụ chứa báo cáo trong khoảng đã chọn |
| report_stats | count_by_reason | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-12, BR-M15-22; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm reports theo report_cases.target_type rồi theo reports.reason trong khoảng đã chọn |
| warning_stats | period | Dẫn xuất | Thuộc tính của lớp thống kê; là tham số khoảng thời gian Admin chọn (BR-M15-03), không phải dữ liệu nghiệp vụ | Admin chọn ở bộ lọc (mặc định ALL_TIME); dùng làm điều kiện trên cột thời điểm của bảng nguồn theo giờ Việt Nam (BR-M15-04) |
| warning_stats | level_trend | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-13, BR-M15-22; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm warnings theo issued_at gom theo giờ, ngày hoặc tháng, tách theo level_after, kể cả bị bỏ, bị lật trong khoảng đã chọn |
| ban_stats | period | Dẫn xuất | Thuộc tính của lớp thống kê; là tham số khoảng thời gian Admin chọn (BR-M15-03), không phải dữ liệu nghiệp vụ | Admin chọn ở bộ lọc (mặc định ALL_TIME); dùng làm điều kiện trên cột thời điểm của bảng nguồn theo giờ Việt Nam (BR-M15-04) |
| ban_stats | ban_trend | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-14, BR-M15-22; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm bans theo started_at gom theo giờ, ngày hoặc tháng, tách theo kind, kể cả bị lật trong khoảng đã chọn |
| ban_stats | unban_trend | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-14, BR-M15-22; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm moderation_logs có action_type = UNBAN theo created_at gom theo giờ, ngày hoặc tháng trong khoảng đã chọn |
| appeal_stats | period | Dẫn xuất | Thuộc tính của lớp thống kê; là tham số khoảng thời gian Admin chọn (BR-M15-03), không phải dữ liệu nghiệp vụ | Admin chọn ở bộ lọc (mặc định ALL_TIME); dùng làm điều kiện trên cột thời điểm của bảng nguồn theo giờ Việt Nam (BR-M15-04) |
| appeal_stats | count_by_type | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-10; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm appeals theo type trong khoảng đã chọn |
| appeal_stats | count_by_result | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M15-10, BR-M15-22; tính trực tiếp mỗi lần xem (BR-M15-05) | Đếm appeals theo kết quả hiện tại: status = PENDING → PENDING; còn lại theo conclusion trong khoảng đã chọn |

### 5.2 Bảng bị loại

Cả bảy bảng của module bị loại: lược đồ cuối của M15 không có bảng nào.

| Bảng | Lý do |
|---|---|
| user_stats | Lớp thống kê không có id, không có lớp cha; sau khi loại cột dẫn xuất không còn cột nào. Số liệu tính trực tiếp mỗi lần Admin mở trang hoặc đổi khoảng thời gian, không lưu sẵn (BR-M15-05) |
| post_stats | Lớp thống kê không có id, không có lớp cha; sau khi loại cột dẫn xuất không còn cột nào. Số liệu tính trực tiếp mỗi lần Admin mở trang hoặc đổi khoảng thời gian, không lưu sẵn (BR-M15-05) |
| comment_stats | Lớp thống kê không có id, không có lớp cha; sau khi loại cột dẫn xuất không còn cột nào. Số liệu tính trực tiếp mỗi lần Admin mở trang hoặc đổi khoảng thời gian, không lưu sẵn (BR-M15-05) |
| report_stats | Lớp thống kê không có id, không có lớp cha; sau khi loại cột dẫn xuất không còn cột nào. Số liệu tính trực tiếp mỗi lần Admin mở trang hoặc đổi khoảng thời gian, không lưu sẵn (BR-M15-05) |
| warning_stats | Lớp thống kê không có id, không có lớp cha; sau khi loại cột dẫn xuất không còn cột nào. Số liệu tính trực tiếp mỗi lần Admin mở trang hoặc đổi khoảng thời gian, không lưu sẵn (BR-M15-05) |
| ban_stats | Lớp thống kê không có id, không có lớp cha; sau khi loại cột dẫn xuất không còn cột nào. Số liệu tính trực tiếp mỗi lần Admin mở trang hoặc đổi khoảng thời gian, không lưu sẵn (BR-M15-05) |
| appeal_stats | Lớp thống kê không có id, không có lớp cha; sau khi loại cột dẫn xuất không còn cột nào. Số liệu tính trực tiếp mỗi lần Admin mở trang hoặc đổi khoảng thời gian, không lưu sẵn (BR-M15-05) |

### 5.3 Dẫn xuất nhưng giữ lại

Không có.

| Bảng | Cột | Lý do giữ | Nguồn |
|---|---|---|---|
| — | — | — | — |

### 5.4 Đã xét nhưng không coi là dư thừa

| Bảng | Cột | Vì sao không dư thừa |
|---|---|---|
| — | — | — |

## 6. Lược đồ cuối

### 6.1 Bảng và cột

<!-- BEGIN:SCHEMA -->
| Bảng | Cột | Kiểu | Khóa | Null | Duy nhất | Tham chiếu |
|---|---|---|---|---|---|---|
<!-- END:SCHEMA -->

### 6.2 Sơ đồ quan hệ

<!-- BEGIN:DIAGRAM -->
![Sơ đồ quan hệ — DB-M15](diagrams/DB-M15.png)

Mã nguồn sơ đồ: [diagrams/DB-M15.puml](diagrams/DB-M15.puml). Ảnh và tệp .puml do `build_schema.py` sinh từ các bảng của tài liệu này; muốn đổi sơ đồ thì sửa bảng rồi chạy lại tool, không sửa tay.
<!-- END:DIAGRAM -->

## 7. Liên module

### 7.1 Bảng của module khác được tham chiếu

| Bảng ngoài | Module sở hữu | Dùng thế nào |
|---|---|---|
| users | M01 | Nguồn của UserStat (R-M15-01). Đọc status, verificationLevel, createdAt, role |
| profiles | M02 | Đọc gradeLevel cho UserStat; không có quan hệ với lớp nào của M15 |
| user_warning_statuses | M08 | Đọc level cho UserStat; không có quan hệ với lớp nào của M15 |
| posts | M03 | Nguồn của PostStat (R-M15-02). Đọc publishState, modState, createdAt, publishedAt, isPermanentlyDeleted |
| topics | M05 | Đọc name, deletedAt cho PostStat; không có quan hệ với lớp nào của M15 |
| comments | M04 | Nguồn của CommentStat (R-M15-03). Đọc publishedAt |
| topic_suggestion_stats | M13 | Đọc tỷ lệ Topic gợi ý được giữ lại (FR-M15-02.07). Bảng này bị loại ở bước 5 của DB-M13 (tính trực tiếp mỗi lần xem); M15 tính từ suggested_topics, chosen_topics, topic_suggestion_feedbacks của M05 |
| reports | M08 | Nguồn của ReportStat (R-M15-04). Đọc status, conclusion, reason, reportedAt |
| report_cases | M08 | Đọc targetType cho ReportStat; không có quan hệ với lớp nào của M15 |
| warnings | M08 | Nguồn của WarningStat (R-M15-05). Đọc issuedAt, levelAfter |
| bans | M08 | Nguồn của BanStat (R-M15-06). Đọc kind, startedAt |
| moderation_logs | M08 | Đọc actionType, createdAt để đếm gỡ ban cho BanStat; không có quan hệ với lớp nào của M15 |
| appeals | M09 | Nguồn của AppealStat (R-M15-07). Đọc type, status, conclusion, submittedAt |

### 7.2 Khóa ngoại đề nghị cho bảng của module khác

<!-- Khi bảng của module khác là phía n của một quan hệ với bảng của module này. -->

| Bảng của module khác | Cột | Kiểu | Tham chiếu | Từ quan hệ |
|---|---|---|---|---|
| — | — | — | — | — |

## 8. Quyết định thiết kế

| Mã | Quyết định | Lý do |
|---|---|---|
| DD-M15-01 | Loại cả bảy bảng thống kê; cột period xếp loại Dẫn xuất (tham số khoảng thời gian) | Trả lời Q-01: BR-M15-05 tính trực tiếp, không lưu sẵn |

## 9. Câu hỏi và điểm chưa chốt

| Mã | Loại | Câu hỏi | Trả lời | Ghi vào |
|---|---|---|---|---|
| Q-01 | Xác nhận | Bảy bảng thống kê của M15 bị loại cả bảng: mọi số liệu tính trực tiếp mỗi lần xem, không lưu sẵn (BR-M15-05); cột period (tham số khoảng thời gian, CD ghi Lưu) xếp loại Dẫn xuất như cột kỳ của lớp thống kê trong case study. Cách tính lại từng số liệu ghi ở mục 5.1. Đồng ý? | Đồng ý (người dùng, 2026-11-22). Soát nghiệp vụ: số liệu tính trực tiếp mỗi lần Admin mở trang hoặc đổi khoảng thời gian, không lưu sẵn (BR-M15-05); DD-M15-01 | Mục 5.1, 5.2 |

## 10. Lịch sử sửa đổi

| Phiên bản | Ngày | Nội dung | Người sửa |
|---|---|---|---|
| 0.1 | 2026-11-20 | Tạo mới từ CD-M15 v1.0; làm liền bước 1–5 theo yêu cầu của người dùng (không dừng ở cổng); chưa qua duyệt, câu hỏi ở mục 9 chờ trả lời | Phạm Văn Đức |
| 0.2 | 2026-11-22 | Ghi trả lời mục 9 (DD-M15-01); chờ chốt | Phạm Văn Đức |
| 1.0 | 2026-11-22 | Chốt: người dùng chốt DB-M15 | Phạm Văn Đức |
