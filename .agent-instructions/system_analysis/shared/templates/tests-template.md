# Ca kiểm — ISH-SR-Mxx phiên bản x.y
<!-- [Vietnamese Doc] -->

Tệp làm việc của Author (`specs/audit/work/tests-Mxx.md`). Quy tắc: `RULES` §11. Một dòng một ca; mọi yêu cầu cấp dưới có ít nhất một ca; cột "Giả định cần thêm" phải là `—` trước khi bàn giao.

| ID ca | ID yêu cầu | Loại | Given | When | Then | Giả định cần thêm |
|---|---|---|---|---|---|---|
| T-001 | ISH-Mxx-001.2 | Biên | Bài đã có 3 Chuyên mục | Người dùng chọn Chuyên mục thứ 4 | Hệ thống từ chối lựa chọn; bài vẫn có 3 Chuyên mục | — |
| T-002 | ISH-Mxx-006.1 | Công thức | Chuyên mục K có bài B (đăng 20 ngày trước, 10 lượt thích hôm qua) và bài C (đăng hôm qua, 0 lượt thích) | Tính điểm Hot của K | Điểm = … (ghi số và cách tính) | — |

Loại ∈ {Thường, Biên, Vi phạm, Quyền, Thời gian, Công thức, Lỗi, Chuyển trạng thái}.
