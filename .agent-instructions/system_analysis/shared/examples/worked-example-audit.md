# Ví dụ hoàn chỉnh: một finding và một khối "cần stakeholder quyết"

> Vai trò dùng: `sr-auditor`. Đọc trước khi chấm checklist.

Ví dụ **minh họa**, đối tượng và số liệu không phải nguồn của dự án. Nguồn giả định `DEC-901`: "Bình luận dài tối đa 500 ký tự. Người dùng chỉ được sửa bình luận trong 15 phút sau khi đăng."

**Dòng ma trận (mục 4 của báo cáo)**

| Nguồn | Mong đợi (Auditor) | Thực tế (SR / routing) | Kết quả | AUD |
|---|---|---|---|---|
| DEC-901 | SR: giới hạn 500; từ chối khi vượt; sửa trong 15 phút; từ chối khi quá hạn | SR: ISH-M99-001.1 (giới hạn 500) và ISH-M99-001.3 (sửa trong 15 phút) | Thiếu một phần | 03 |

**Finding (mục 5)**

```
### AUD-M99-03 — Thiếu yêu cầu cho bình luận vượt giới hạn 500 ký tự

| Lớp | DEFECT | Mức | Trung bình | Checklist | CL-B09 |
|---|---|---|---|---|---|

- Vị trí: ISH-M99-001.1 (ISH-SR-M99.md:84)
- Bằng chứng trong SR: "Hệ thống phải giới hạn mỗi bình luận tối đa 500 ký tự." (ISH-SR-M99.md:84)
- Bằng chứng trong nguồn: "Bình luận dài tối đa 500 ký tự." (decisions.md:512, DEC-901)
- Vấn đề: SR nêu giới hạn nhưng không có yêu cầu nào cho trường hợp người dùng gửi bình luận dài hơn 500 ký tự. Từ chối là suy ra hợp lệ của giới hạn (RULES §4.5).
- Hệ quả nếu không sửa: hành vi khi vượt giới hạn không kiểm chứng được.
- Hướng xử lý (Author quyết cách viết): thêm một yêu cầu cấp dưới cho trường hợp vượt giới hạn và một hàng Phụ lục A cơ sở Suy ra.
- Trạng thái (từ vòng 2): Mở
```

Hồ sơ xác minh (mục 9): `grep -n -F "tối đa 500 ký tự" ISH-SR-M99.md → 1 kết quả (dòng 84)`; `grep -n -i -E "vượt|dài hơn 500|từ chối" ISH-SR-M99.md → 0 kết quả liên quan đến giới hạn 500`.

**Khối cần stakeholder quyết (mục 6)** — chỉ dùng cho GAP, CONFLICT, OBSERVATION; ví dụ một GAP:

```
Vấn đề: Nguồn nêu bình luận dài tối đa 500 ký tự nhưng chưa nói ký tự xuống dòng có được tính không.
Nguồn: DEC-901 (decisions.md:512): "Bình luận dài tối đa 500 ký tự."
Lựa chọn: A) Tính cả ký tự xuống dòng — hệ quả: bình luận nhiều đoạn bị giới hạn chặt hơn.
          B) Không tính — hệ quả: cần định nghĩa cách đếm ở yêu cầu.
Đề xuất: A vì nguồn không loại trừ ký tự nào.
Liên quan: AUD-M99-05
```
