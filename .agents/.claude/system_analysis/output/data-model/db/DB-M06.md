---
module: M06
ten_module: Search
ma_tai_lieu: DB-M06
phien_ban: 1.0
trang_thai: Đã chốt
ngay: 2026-11-22
tac_gia: Phạm Văn Đức
nguon: CD-M06 v1.0
steps_completed: [1, 2, 3, 4, 5]
---
# Thiết kế cơ sở dữ liệu — M06 Search

<!-- [Vietnamese Doc] Tài liệu tiếng Việt; tên bảng, cột, kiểu viết tiếng Anh. -->

| Mã tài liệu | DB-M06 |
|---|---|
| Dự án | iShare |
| Module | M06 — Search |
| Đầu vào | CD-M06 phiên bản 1.0 |
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
| post_search_stats | PostSearchStat | Thống kê | M06 | Lớp con của Post (kế thừa): không có id riêng, dùng khóa của bảng cha |

## 2. Cột

### 2.1 Cột từ thuộc tính

| Bảng | Cột | Kiểu | Null | Duy nhất | Từ thuộc tính | Ghi chú |
|---|---|---|---|---|---|---|
| post_search_stats | relevance_score | double precision | Có | Không | PostSearchStat.relevanceScore | 0–1; chỉ có với truy vấn có chữ; tìm ngữ nghĩa: (cosine(embedding truy vấn, embedding bài) + 1) ÷ 2; tìm full-text: số từ của truy vấn có trong tiêu đề hoặc nội dung chữ ÷ số từ của truy vấn (BR-M06-13, BR-M06-08); tập ứng viên là 120 bài có điểm cao nhất (FR-M06-02.28); Dẫn xuất ở CD: xét ở bước 5 |
| post_search_stats | engagement_raw | double precision | Không | Không | PostSearchStat.engagementRaw | = log(1 + Post.upvoteCount) × 2 + log(1 + Post.commentCount) × 1 (BR-M06-13); Dẫn xuất ở CD: xét ở bước 5 |
| post_search_stats | engagement_score | double precision | Có | Không | PostSearchStat.engagementScore | 0–1; chỉ có với truy vấn có chữ; chuẩn hóa min–max của engagementRaw trong tập ứng viên, mọi ứng viên bằng nhau thì 0 (BR-M06-13); Dẫn xuất ở CD: xét ở bước 5 |
| post_search_stats | final_score | double precision | Có | Không | PostSearchStat.finalScore | Chỉ có với truy vấn có chữ; = relevanceScore × 0,8 + engagementScore × 0,2; × 0,5 khi tác giả ở mức cảnh cáo HEAVY và đang xếp theo Liên quan (BR-M06-13, BR-M06-14); không hiện cho người tìm (FR-M06-02.12); Dẫn xuất ở CD: xét ở bước 5 |
| post_search_stats | snippet | text | Có | Không | PostSearchStat.snippet | Gồm 150 ký tự đầu cộng dấu '…' nên có thể dài 151 ký tự: dùng text, không đặt n; Tối đa 150 ký tự đầu của Post.contentText, cắt trước từ bị cắt dở và thêm "…"; không có khi bài không có nội dung chữ (BR-M06-18); không tô sáng từ khóa (FR-M06-02.15); Dẫn xuất ở CD: xét ở bước 5 |

### 2.2 Thuộc tính đối tượng không chuyển

Không có: lớp của module không có thuộc tính đối tượng.

| Lớp | Thuộc tính | Kiểu | Lý do không chuyển |
|---|---|---|---|
| — | — | — | — |

## 3. Quan hệ giữa các bảng

"Dạng" đọc theo thứ tự Bảng A – Bảng B; quan hệ 1-n viết bảng phía 1 ở cột Bảng A.

| ID | Bảng A | Bảng B | Dạng | Xử lý | Ghi chú |
|---|---|---|---|---|---|
| R-M06-01 | posts | post_search_stats | 1-1 | Cha–con | Kế thừa: bảng con không có id riêng, dùng khóa của bảng cha |

Không có quan hệ n-n.

## 4. Khóa

### 4.1 Khóa chính

| Bảng | Khóa chính | Ghi chú |
|---|---|---|
| post_search_stats | post_id | Bảng con: khóa chính là khóa ngoại tới bảng cha |

### 4.2 Khóa ngoại

| Bảng | Cột | Kiểu | Null | Duy nhất | Tham chiếu | Từ quan hệ | Ghi chú |
|---|---|---|---|---|---|---|---|
| post_search_stats | post_id | bigint | Không | Có | posts(id) | R-M06-01 | Cha–con: cũng là khóa chính của post_search_stats |

## 5. Loại dư thừa

### 5.1 Cột bị loại

| Bảng | Cột | Loại dư thừa | Căn cứ | Cách có lại giá trị |
|---|---|---|---|---|
| post_search_stats | relevance_score | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M06-13, BR-M06-08; tính theo từng truy vấn | Tính ở mỗi lần tìm: ngữ nghĩa = (cosine(embedding của truy vấn, posts.embedding) + 1) ÷ 2; full-text = số từ của truy vấn có trong posts.title hoặc phần chữ của posts.content ÷ số từ của truy vấn |
| post_search_stats | engagement_raw | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M06-13 | log(1 + số upvotes của bài) × 2 + log(1 + số comments đang hiển thị của bài) × 1 |
| post_search_stats | engagement_score | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M06-13 | Chuẩn hóa min–max của engagement_raw trong tập ứng viên của truy vấn; mọi ứng viên bằng nhau thì 0 |
| post_search_stats | final_score | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M06-13, BR-M06-14 | relevance × 0,8 + engagement_score × 0,2; nhân 0,5 khi tác giả ở mức HEAVY (user_warning_statuses.warning_count 5–6) và đang xếp theo Liên quan |
| post_search_stats | snippet | Dẫn xuất | Thuộc tính của lớp thống kê; BR-M06-18 | 150 ký tự đầu phần chữ của posts.content, cắt trước từ bị cắt dở, thêm '…'; không có khi bài không có nội dung chữ |

### 5.2 Bảng bị loại

Bảng duy nhất của module bị loại: lược đồ cuối của M06 không có bảng nào.

| Bảng | Lý do |
|---|---|
| post_search_stats | Bảng con của posts (kế thừa R-M06-01). Sau khi loại cột dẫn xuất chỉ còn khóa post_id, là một khóa ngoại; số liệu tính theo từng lần tìm, không lưu |

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
![Sơ đồ quan hệ — DB-M06](diagrams/DB-M06.png)

Mã nguồn sơ đồ: [diagrams/DB-M06.puml](diagrams/DB-M06.puml). Ảnh và tệp .puml do `build_schema.py` sinh từ các bảng của tài liệu này; muốn đổi sơ đồ thì sửa bảng rồi chạy lại tool, không sửa tay.
<!-- END:DIAGRAM -->

## 7. Liên module

### 7.1 Bảng của module khác được tham chiếu

| Bảng ngoài | Module sở hữu | Dùng thế nào |
|---|---|---|
| posts | M03 | Lớp cha của PostSearchStat (R-M06-01): mỗi kết quả bài viết là một bài viết. Đọc title, contentText để so khớp và cắt đoạn trích; publishedAt để lọc khoảng thời gian, xếp Mới nhất; isPubliclyVisible để chỉ giữ bài đang hiển thị công khai; commentCount (M04 bổ sung) và upvoteCount để tính engagementRaw, xếp Nhiều upvote nhất; isAnonymous cho bộ lọc đang theo dõi. upvoteCount và isAnonymous chưa có ở EC-M03 |
| users | M01 | Được tìm theo displayName, username làm gợi ý khi gõ và kết quả phụ, chỉ tài khoản có status ACTIVE và verificationLevel SETUP_COMPLETED; đọc status của tác giả bài viết (BANNED vẫn giữ trong kết quả). Không có quan hệ với lớp của M06 |
| tags | M05 | Được tìm theo name, bỏ Tag có status Bị vô hiệu hóa; dùng làm bộ lọc kết quả bài viết qua PostTag của M05. Không có quan hệ với lớp của M06 |
| topics | M05 | Được tìm theo name; dùng làm bộ lọc kết quả bài viết qua PostTopic của M05. Không có quan hệ với lớp của M06 |
| groups | M11 | Được tìm theo name, không theo mô tả; Group có privacy Private và bài viết của Group đó (R-M03-06) chỉ hiện với thành viên. Không có quan hệ với lớp của M06. Tên lớp và thuộc tính tạm, chờ EC-M11 |

### 7.2 Khóa ngoại đề nghị cho bảng của module khác

<!-- Khi bảng của module khác là phía n của một quan hệ với bảng của module này. -->

| Bảng của module khác | Cột | Kiểu | Tham chiếu | Từ quan hệ |
|---|---|---|---|---|
| — | — | — | — | — |

## 8. Quyết định thiết kế

| Mã | Quyết định | Lý do |
|---|---|---|
| — | — | — |

## 9. Câu hỏi và điểm chưa chốt

| Mã | Loại | Câu hỏi | Trả lời | Ghi vào |
|---|---|---|---|---|
| — | — | — | — | — |

## 10. Lịch sử sửa đổi

| Phiên bản | Ngày | Nội dung | Người sửa |
|---|---|---|---|
| 0.1 | 2026-11-20 | Tạo mới từ CD-M06 v1.0; làm liền bước 1–5 theo yêu cầu của người dùng (không dừng ở cổng); chưa qua duyệt, câu hỏi ở mục 9 chờ trả lời | Phạm Văn Đức |
| 0.2 | 2026-11-22 | Công thức có lại giá trị dùng phần chữ của posts.content vì posts.content_text bị loại ở DB-M03 (DD-M03-02); soát lại theo tiêu chí dẫn xuất của người dùng: số liệu tính theo từng truy vấn, không đổi; chờ chốt | Phạm Văn Đức |
| 1.0 | 2026-11-22 | Chốt: người dùng chốt DB-M06 | Phạm Văn Đức |
