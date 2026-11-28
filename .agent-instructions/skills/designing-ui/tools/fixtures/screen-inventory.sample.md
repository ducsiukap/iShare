---
ma_tai_lieu: SCREEN-INVENTORY
phien_ban: 0.1
trang_thai: Bản nháp
ngay: 2026-11-24
tac_gia: Phạm Văn Đức
---
# Danh mục màn hình — mẫu cho module M03 (fixture để thử tool)

[Vietnamese Doc] — Ví dụ hình dạng `screen-inventory.md`, chỉ module M03, dựng từ US-M03 và SC-M03 hiện có. Không phải
kết quả bước 4 (bước 4 làm cho cả 16 module và phải qua cổng). Chạy:

```
python3 tools/check_inventory.py --inventory tools/fixtures/screen-inventory.sample.md --specs docs/specs --modules M03
```

## 2. Màn hình

<!-- ui:screens -->
| id | name | module | roles | uc | sc | sources | states | devices | batch | notes |
|---|---|---|---|---|---|---|---|---|---|---|
| SCR-M03-01 | Soạn và sửa bài viết | M03 | ACT-002, ACT-003 | UC-M03-001, UC-M03-002, UC-M03-003, UC-M03-004, UC-M03-011 | SC-M03-001, SC-M03-004, SC-M03-011 | FR-M03-01, FR-M03-02, FR-M03-03, FR-M03-04, FR-M03-11 | default, validation, long, error, pending, rejected | desktop, mobile | A | Đính kèm và poll là vùng trong trình soạn |
| SCR-M03-02 | Chi tiết bài viết | M03 | ACT-001, ACT-002, ACT-003 | UC-M03-007, UC-M03-008, UC-M03-009, UC-M03-013, UC-M03-017, UC-M03-014, UC-M03-015 | SC-M03-007, SC-M03-008, SC-M03-009, SC-M03-013, SC-M03-014, SC-M03-015, SC-M03-017, SC-M03-019, SC-M03-020, SC-M03-021 | FR-M03-07, FR-M03-08, FR-M03-09, FR-M03-10, FR-M03-13, FR-M03-14, FR-M03-15, BR-M03-50 | default, loading, long, not-found, forbidden, hidden, locked, deleted, owner, guest | desktop, mobile | A | Màn hình mẫu của bước 3; không có Accepted Answer, ảnh bìa (BR-M03-50) |
| SCR-M03-03 | Lịch sử sửa bài viết | M03 | ACT-001, ACT-002, ACT-003 | UC-M03-012 | SC-M03-012 | FR-M03-12 | default, loading, empty | desktop, mobile | A | |
| SCR-M03-04 | Bài viết đã xóa (khôi phục) | M03 | ACT-002 | UC-M03-016 | SC-M03-016 | FR-M03-16 | default, empty | desktop, mobile | A | Tab "Đã xóa" |
| SCR-M03-05 | Hàng chờ duyệt bài | M03 | ACT-003 | UC-M03-006 | SC-M03-006 | FR-M03-06 | default, loading, empty, error | desktop | C | |
| SCR-M03-06 | Xem bài trong ngữ cảnh kiểm duyệt | M03 | ACT-002, ACT-003 | UC-M03-018 | SC-M03-018 | FR-M03-17 | default, flagged, rejected | desktop, mobile | C | Mở từ thông báo kết quả xử lý |

## 3. UC không có màn hình riêng

<!-- ui:no-screen -->
| uc | reason | shown_as |
|---|---|---|
| UC-M03-005 | Chính sách kiểm duyệt khi công bố do hệ thống áp dụng trong luồng gửi bài | Trạng thái `pending`, `rejected` của SCR-M03-01 |

## 4. Chia đợt

<!-- ui:batches -->
| batch | name | order_reason |
|---|---|---|
| A | Đọc và viết | Dùng màn hình mẫu bước 3 |
| C | Kiểm duyệt và quản trị | |

## 5. Nguồn đã dùng

<!-- ui:sources -->
| path | version |
|---|---|
| docs/specs/fr/FR-M03.md | 1.10 |
| docs/specs/us/US-M03.md | 2026-10-30 |
| docs/specs/scenarios/M03/SC-M03.md | 2026-11-11 |
