# Bước 5 — Xây dựng Ma trận Truy vết Toàn bộ Chức năng (FR → UC)

**Mục tiêu:** Xây dựng Mục 4.1 trong tài liệu US, đảm bảo 100% chức năng trong FR được phân định rõ ràng vai trò và liên kết use case.

## Quy trình lập ma trận

1. Liệt kê toàn bộ danh sách chức năng con `FR-Mxx-nn` đã trích xuất từ mục 4.4 của tài liệu FR ở Bước 1.
2. Ánh xạ từng mã `FR-Mxx-nn` vào cấu trúc phân rã Use Case đã thực hiện ở Bước 2 và Bước 4:
   - **Thuộc Use Case Chính:** Mã UC Chính (`UC-C01`, `UC-C02`, ...), hoặc ghi `*(Tiến trình ngầm)*` / `*(Tầng hiển thị)*` nếu không phải UC tương tác.
   - **Thuộc Use Case Phụ cụ thể:** Mã và tên UC con (`UC-01.1: Tên...`), hoặc mô tả cơ chế nền tảng nếu là tiến trình ngầm / tầng hiển thị.
   - **Vai trò quan hệ trong UC Chính:**
     + `<<include>> (Bắt buộc)`: Bắt buộc hoàn thành trong luồng UC Chính.
     + `<<extend>> (Tùy chọn / Rẽ nhánh / Ngoại lệ)`: Các nhánh nghiệp vụ mở rộng hoặc tùy chọn.
     + `Generalization (Kế thừa / Chuyên biệt hóa)`: Use Case con là một dạng cụ thể của Use Case cha.
     + `Nền tảng hạ tầng kỹ thuật` hoặc `Daemon chạy tự động`: Dành cho `*(Tiến trình ngầm)*`.
     + `Logic kiểm soát hiển thị`: Dành cho `*(Tầng hiển thị)*`.
3. **Quy tắc xử lý ánh xạ (Giữ nguyên, Gộp, và Rẽ nhánh):**
   - **Giữ nguyên (1-to-1):** 1 mã FR ánh xạ trực tiếp tới đúng 1 UC con.
   - **Gộp lại (N-to-1):** Khi nhiều mã FR liên quan được gộp thành 1 UC con đơn nhiệm (ví dụ `FR-M02-04.01 - 04.05` gộp thành `UC-02.5: Đổi ảnh đại diện`), từng dòng mã FR trong ma trận đều ghi nhận ánh xạ tới UC con chung này.
   - **Rẽ nhánh / Nhiều vai trò (1-to-N):** Khi 1 mã FR sinh ra nhiều UC con, dùng thẻ `<br>` để chia dòng tương ứng giữa các cột:
     + Nếu 1 FR thuộc 2 UC Chính: Cột "Thuộc Use Case Chính" ghi `**UC-C01**<br>**UC-C02**`, các cột tiếp theo chia dòng tương ứng.
     + Nếu 1 FR sinh ra nhiều UC con: Liệt kê các UC con trên từng dòng nối bằng `<br>`, cột "Vai trò quan hệ" cũng chia các dòng tương ứng bằng `<br>`.
4. Rà soát đảm bảo 100% mã FR trong mục 4.4 đều có mặt trong bảng, không sót bất kỳ mã nào, và KHÔNG có bất kỳ Use Case con nào không xuất phát từ mã FR (chống Use Case con mồ côi / tự bịa).

## Cấu trúc bảng ma trận truy vết chuẩn (Mục 4.1 — Chuẩn vàng US-M01)

```markdown
| Mã FR | Tên chức năng con trong `FR-Mxx.md` | Thuộc Use Case Chính | Thuộc Use Case Phụ cụ thể | Vai trò quan hệ trong UC Chính |
|:---:|---|:---:|---|:---:|
| **FR-Mxx-01** | Đăng ký tài khoản... | **UC-C01** | UC-01.1: Nhập thông tin & Cam kết ToS (Bước 1) | `<<include>>` (Bắt buộc) |
| **FR-Mxx-03** | Thiết lập tài khoản | **UC-C01** | UC-01.3: Thiết lập Username & Display Name (Bước 3)<br>UC-01.5: Bổ sung thông tin tùy chọn (Bio, Khối, Avatar) | `<<include>>` (Bắt buộc)<br>`<<extend>>` (Tùy chọn) |
| **FR-Mxx-04** | Đăng ký, đăng nhập bằng Google | **UC-C01**<br>**UC-C02** | UC-01.4: Đăng ký nhanh qua Google OAuth<br>UC-02.3: Đăng nhập bằng Google / UC-02.4: Tự động liên kết | `<<extend>>` (Rẽ nhánh)<br>`<<extend>>` (Thay thế/Liên kết) |
| **FR-Mxx-06** | Duy trì phiên đăng nhập | *(Tiến trình ngầm)* | Quản lý Token kép JWT (Access 1h / Refresh 30d xoay vòng) | Nền tảng hạ tầng kỹ thuật |
| **FR-Mxx-12** | Tự động dọn dẹp... | *(Tiến trình ngầm)* | Cron Job tự động chuyển `DELETED` sau 14 ngày & Xóa sạch PII | Daemon chạy tự động |
| **FR-Mxx-13** | Hiển thị nội dung... | *(Tầng hiển thị)* | Bộ lọc ẩn bài viết & Đổi tên bình luận thành tên thay thế | Logic kiểm soát hiển thị |
```

## Kiểm tra trước khi trình cổng

- [ ] Tổng số dòng trong bảng khớp chính xác 100% với số lượng mục trong danh sách chức năng FR (mục 4.4).
- [ ] Không có ô trống ở bất kỳ dòng nào.
- [ ] Các chức năng nền được định danh đúng là `*(Tiến trình ngầm)*` hoặc `*(Tầng hiển thị)*`.
- [ ] Các mã FR có nhiều UC con được định dạng dòng tương ứng bằng `<br>`.

## Cổng xác nhận

Gửi tin nhắn theo mẫu trong SKILL.md và chờ.

