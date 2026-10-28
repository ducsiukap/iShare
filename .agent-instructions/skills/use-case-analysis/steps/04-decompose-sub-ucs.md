# Bước 4 — Phân rã Use Case con & Xác định Quan hệ

**Mục tiêu:** Với mỗi UC Chính, xác định các UC con strictly trong phạm vi FR, phân loại theo 3 quan hệ chuẩn UML (`<<include>>`, `<<extend>>`, `Generalization`), và xây dựng Per-UC Diagram + Bảng quan hệ chi tiết cho Mục 3.

---

## 1. Quy tắc Nghiệp vụ Cốt lõi: Xác định Use Case con — Tuyệt đối trong phạm vi FR & Đơn nghiệp vụ

### A. Ranh giới phạm vi tuyệt đối (Scope Boundary — Chống vẽ thêm Use Case ngoài FR)
- **Chỉ trong phạm vi FR:** Việc phân rã Use Case con **BẮT BUỘC CHỈ ĐƯỢC PHÉP NẰM TRONG PHẠM VI** các chức năng đã được định nghĩa trong tài liệu `FR-Mxx.md` (mục 4.4 và mục 5.x).
- **CẤM TUYỆT ĐỐI:** Agent không được tự suy diễn, phỏng đoán hoặc "bịa" ra các Use Case con ngoài phạm vi (Out-of-Scope Hallucination). Mọi Use Case con xuất hiện trong tài liệu US đều phải có căn cứ truy vết trực tiếp về ít nhất một mã chức năng `FR-Mxx-nn` hoặc quy tắc nghiệp vụ `BR-Mxx-nn`.

### B. Hai cơ chế hình thành Use Case con hợp lệ từ FR
Để chuyển hóa các chức năng trong FR thành Use Case con, chỉ có **ĐÚNG 2 CƠ CHẾ HỢP LỆ** sau:

1. **Cơ chế 1: Giữ nguyên chức năng FR (1-to-1 Mapping)**
   - Áp dụng khi một chức năng con trong FR đại diện cho một hành vi độc lập, rõ ràng của Actor trên UI.
   - *Ví dụ:* `FR-M02-05: Lưu bài viết` $\to$ Giữ nguyên thành Use Case con `UC-03.2: Lưu bài viết`.
   - *Ví dụ:* `FR-M02-06: Bỏ lưu bài viết` $\to$ Giữ nguyên thành Use Case con `UC-03.3: Bỏ lưu bài viết`.

2. **Cơ chế 2: Gộp các chức năng FR liên quan (N-to-1 Mapping / Aggregation)**
   - Áp dụng khi 2 hoặc nhiều chức năng con (hoặc các chức năng chi tiết `FR-Mxx-yy.zz`) trong FR có liên quan mật thiết với nhau, cùng phối hợp giải quyết một chuỗi thao tác kỹ thuật/giao diện để hoàn thành một mục tiêu duy nhất.
   - *Ví dụ:* Trong `FR-M02-04`, các chức năng chi tiết bao gồm `FR-M02-04.01` (Tải ảnh từ máy lên), `FR-M02-04.02` (Kiểm tra dung lượng/định dạng), `FR-M02-04.03` (Cắt và nén ảnh), `FR-M02-04.04` (Lưu ảnh đại diện mới) $\to$ **Gộp lại thành 1 Use Case con duy nhất:** `UC-02.5: Đổi ảnh đại diện`.

### C. Nguyên tắc Nghiệp vụ Đơn nhất (Single Business Responsibility — Điều kiện bắt buộc khi gộp)
- **Đúng 1 nghiệp vụ xác định cụ thể:** Dù giữ nguyên hay gộp, **mỗi Use Case con BẮT BUỘC chỉ được thực hiện ĐÚNG DUY NHẤT 1 nghiệp vụ xác định cụ thể**.
- **Không gom tạp nham:** Tuyệt đối không được gom các nghiệp vụ khác biệt, rời rạc, không liên quan về mặt mục đích người dùng vào làm một Use Case con đa nhiệm.
- **Bảng đối chiếu kiểm chứng:**

| Trạng thái | Use Case con đề xuất | Căn cứ FR | Phân tích nghiệp vụ & Đánh giá |
|:---:|---|:---:|---|
| ✅ **Hợp lệ** | `UC-02.5: Đổi ảnh đại diện` | `FR-M02-04.01 - 04.05` | **Hợp lệ:** Gộp các bước tải ảnh, kiểm tra file, cắt ảnh, lưu ảnh. Đạt tính đơn nghiệp vụ (chỉ phục vụ duy nhất 1 mục đích: đổi avatar). |
| ✅ **Hợp lệ** | `UC-01.1: Xem thông tin hồ sơ` | `FR-M02-01.01, 01.02` | **Hợp lệ:** Gộp hiển thị header và các tab bài viết/đã lưu. Cùng phục vụ 1 nghiệp vụ là nạp dữ liệu hồ sơ. |
| ❌ **Sai phạm (Đa nghiệp vụ)** | `UC-02.3: Cập nhật thông tin cá nhân và đổi avatar` | `FR-M02-03`<br>`FR-M02-04` | **Sai nghiêm trọng!** Vi phạm tính đơn nghiệp vụ: Cập nhật tiểu sử/khối lớp và Đổi ảnh đại diện là 2 nghiệp vụ độc lập, người dùng có thể thực hiện một trong hai mà không cần cái kia. |
| ❌ **Sai phạm (Tự nghĩ ra ngoài FR)** | `UC-02.7: Chia sẻ hồ sơ lên Facebook / Zalo` | *(Không có trong FR)* | **Sai nghiêm trọng!** Trong tài liệu `FR-M02.md` không hề có chức năng chia sẻ mạng xã hội bên ngoài. Agent tự suy diễn ngoài phạm vi. |
| ❌ **Sai phạm (Tự nghĩ ra ngoài FR)** | `UC-01.8: Đăng nhập bằng sinh trắc học (Vân tay/FaceID)` | *(Không có trong FR)* | **Sai nghiêm trọng!** `FR-M01` chỉ có Email/Password và Google OAuth. Tuyệt đối không được thêm sinh trắc học nếu FR không mô tả. |

---

## 2. Quy tắc phân loại 3 quan hệ UML chuẩn (Visual Paradigm / UML Standard)

### A. Quan hệ `<<include>>` (Bao hàm Bắt buộc / Tiên quyết)
- Dùng khi UC con là **bước bắt buộc phải thực hiện** để UC Chính hoàn thành.
- Nếu thiếu hoặc thất bại ở bước này, toàn bộ UC Chính bị dừng / không thể hoàn tất.
- Chiều mũi tên: Nét đứt từ UC Chính sang UC Con:
  `UC_Chính -.->|"<<include>>"| UC_Con`
- Node styling: `classDef incStyle fill:#e8f5e9,stroke:#2e7d32,stroke-width:1.5px;` (xanh lá).

### B. Quan hệ `<<extend>>` (Tùy chọn / Mở rộng / Rẽ nhánh / Ngoại lệ)
- Dùng khi UC con thuộc một trong các tình huống nghiệp vụ sau:
  + **Tính năng tùy chọn (Optional):** Bước người dùng có thể làm hoặc bỏ qua mà quy trình chính vẫn hoàn thành (ví dụ: điền Bio, Avatar, Khối lớp ở Bước 3 thiết lập).
  + **Nhánh ngoại lệ / Điều kiện rẽ nhánh (Conditional / Exception):** Chỉ kích hoạt khi thỏa mãn điều kiện nhất định (ví dụ: gửi lại Magic Link khi link cũ hết hạn; màn hình khóa khi tài khoản `BANNED`; yêu cầu Re-consent khi chính sách đổi).
  + **Tương tác mở rộng ngữ cảnh:** Chức năng bổ trợ gắn liền với màn hình nhưng không bắt buộc (ví dụ: nút Nhắn tin 1-1 từ hồ sơ người khác, nút xem chi tiết danh sách follower).
- Chiều mũi tên: Nét đứt từ UC Con sang UC Chính:
  `UC_Con -.->|"<<extend>>"| UC_Chính`
- Node styling: `classDef extStyle fill:#fffde7,stroke:#f57f17,stroke-width:1.5px,stroke-dasharray: 4 4;` (vàng viền đứt).

### C. Quan hệ `Generalization` (Khái quát hóa / Kế thừa / Quan hệ Cha - Con)
- **Bản chất nghiệp vụ:** Thể hiện quan hệ "là-một-dạng-của" (*is-a-kind-of*). Use Case con là một dạng chuyên biệt hóa (specialization) cụ thể của một Use Case cha tổng quát (generalization).
- **Cơ chế kế thừa:** Use Case con kế thừa toàn bộ mục tiêu của cha, vai trò của Actor, các ràng buộc và quan hệ chung, nhưng cụ thể hóa quy trình nghiệp vụ hoặc cơ chế kỹ thuật thực thi. Khi người dùng thực hiện một trong các Use Case con, họ đồng thời hoàn thành mục tiêu của Use Case cha.
- **Khi nào áp dụng:**
  + Khi một mục tiêu nghiệp vụ có nhiều phương thức thực hiện hoàn toàn khác nhau về luồng xử lý hoặc nguồn xác thực, nhưng cùng mang lại một kết quả cuối cùng.
  + *Ví dụ kinh điển trong Visual Paradigm:*
    - **Cha:** `Đăng nhập hệ thống (User Authentication)`
      + **Con 1:** `Đăng nhập bằng Email & Mật khẩu (Login via Credentials)`
      + **Con 2:** `Đăng nhập bằng Google OAuth (Login via Google OAuth)`
    - **Cha:** `Đăng ký tài khoản (User Registration)`
      + **Con 1:** `Đăng ký bằng Email truyền thống (Register via Email Flow)`
      + **Con 2:** `Đăng ký nhanh qua Google OAuth (Register via Google OAuth)`
    - **Cha:** `Quản lý bài viết đã lưu (Manage Saved Posts)`
      + **Con 1:** `Lưu bài viết (Save Post)`
      + **Con 2:** `Bỏ lưu bài viết (Unsave Post)`
- **Phân biệt rành mạch giữa 3 quan hệ:**
  + `<<include>>`: Con là một *mảnh ghép/bước bắt buộc* bên trong Cha (Cha chứa Con).
  + `<<extend>>`: Con là một *phần mở rộng tùy chọn/ngoại lệ* của Cha (Cha chạy độc lập được mà không cần Con).
  + `Generalization`: Cha là một *khái niệm trừu tượng*, Cha không tự thực thi độc lập được mà bắt buộc phải chạy thông qua một trong các Con chuyên biệt (Con thay thế cho Cha tại thời điểm chạy).
- **Chiều mũi tên:** Mũi tên nét liền trỏ từ Use Case Con (chuyên biệt hóa) về Use Case Cha (tổng quát):
  `UC_Con -->|"<<generalization>>"| UC_Cha`
- **Node styling:** `classDef genStyle fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1.5px;` (màu tím nhạt, nét liền).

---

## 3. Quy ước đặt mã và đặt tên Use Case con (Chuẩn BA chuyên nghiệp)

1. **Quy ước mã:**
   - UC con của `UC-C01` $\to$ `UC-01.1`, `UC-01.2`, `UC-01.3`, ...
   - UC con của `UC-C02` $\to$ `UC-02.1`, `UC-02.2`, ...
   - Số đầu tiên tương ứng với số thứ tự của UC Chính.

2. **Quy tắc đặt tên Use Case con:**
   - **Cấu trúc:** `UC-nn.n: [Động từ duy nhất] + [Cụm danh từ]`.
   - **Chỉ chứa ĐÚNG 1 động từ duy nhất:** Tuyệt đối không dùng nhiều động từ nối với nhau ("và", "&", "/", "hoặc"). Động từ này đại diện cho chính xác 1 nghiệp vụ đơn nhất.
   - *Ví dụ sai:* `UC-01.1: Nhập thông tin & Cam kết ToS` $\to$ *Ví dụ đúng:* `UC-01.1: Điền thông tin đăng ký`.
   - *Ví dụ sai:* `UC-01.3: Thiết lập Username & Display Name` $\to$ *Ví dụ đúng:* `UC-01.3: Đặt định danh tài khoản`.
   - *Ví dụ sai:* `UC-02.5: Tải lên & Thay đổi Ảnh đại diện Avatar` $\to$ *Ví dụ đúng:* `UC-02.5: Đổi ảnh đại diện`.
   - *Ví dụ sai:* `UC-02.4: Cập nhật hoặc bỏ chọn Lớp/Khối` $\to$ *Ví dụ đúng:* `UC-02.4: Cập nhật khối lớp`.
   - *Ví dụ sai:* `UC-01.5: Xem chi tiết danh sách Người theo dõi & Đang theo dõi` $\to$ *Ví dụ đúng:* `UC-01.5: Xem danh sách theo dõi`.
   - *Ví dụ sai:* `UC-01.4: Duyệt toàn bộ bài viết & tab Đã xóa` $\to$ *Ví dụ đúng:* `UC-01.4: Quản lý bài viết cá nhân`.

---

## 4. Xử lý quan hệ giữa mã FR và Use Case con

1. **Một mã FR có thể sinh ra nhiều Use Case con:**
   - Khi một mục trong tài liệu FR mô tả nhiều hành vi (vừa có phần bắt buộc, vừa có phần tùy chọn hoặc xử lý ngoại lệ), hãy tách thành các UC con riêng rẽ với các quan hệ độc lập (`<<include>>`, `<<extend>>`, hoặc `Generalization`).
   - *Ví dụ:* `FR-M01-03` tách thành `UC-01.3: Đặt định danh tài khoản` (`<<include>>`) và `UC-01.5: Bổ sung thông tin tùy chọn` (`<<extend>>`). `FR-M01-05` tách thành 4 UC con.
2. **Nhiều mã FR liên quan gộp thành một Use Case con (Đơn nghiệp vụ):**
   - Khi các mã FR cùng phục vụ một quy trình gắn kết $\to$ gộp thành 1 Use Case con, ghi rõ toàn bộ các mã FR thành phần trong cột căn cứ.
3. **Một mã FR có thể tham gia vào nhiều UC Chính:**
   - *Ví dụ:* `FR-M01-04` (Google OAuth) vừa là phương thức đăng ký chuyên biệt trong `UC-C01`, vừa là phương thức đăng nhập chuyên biệt trong `UC-C02`.
4. **Chức năng không tạo UC con:**
   - Các chức năng được xác định là `*(Tiến trình ngầm)*` (cron job dọn dẹp, token refresh) hoặc `*(Tầng hiển thị)*` (logic ẩn/hiện nội dung tài khoản bị khóa/xóa) **KHÔNG** tạo Use Case con ở bước này. Chúng sẽ được định danh trực tiếp trong ma trận truy vết ở Bước 5.

---

## 5. Quy trình thực hiện với từng UC Chính

1. Gom các chức năng con `FR-Mxx-nn` và các quy tắc nghiệp vụ `BR-Mxx-nn` thuộc phạm vi UC Chính này (đối chiếu danh sách ở Bước 1).
2. Quyết định cơ chế cho từng chức năng: Giữ nguyên (1-1) hoặc Gộp (N-1), kiểm tra tính đơn nghiệp vụ.
3. Tuyệt đối loại bỏ mọi ý tưởng hoặc hành vi không có trong tài liệu FR.
4. Xác định đúng quan hệ của từng Use Case con: `<<include>>`, `<<extend>>`, hay `Generalization`.
5. Vẽ sơ đồ phân rã (`flowchart TB`) riêng cho từng UC:
   - Thể hiện Actor liên quan.
   - Thể hiện UC Chính và các UC con trong một subgraph.
   - Đường nối đúng cú pháp:
     + Include: `UC_Chính -.->|"<<include>>"| UC_Con`
     + Extend: `UC_Con -.->|"<<extend>>"| UC_Chính`
     + Generalization: `UC_Con -->|"<<generalization>>"| UC_Chính`
   - Áp dụng đúng classDef màu sắc: `incStyle` (xanh lá), `extStyle` (vàng đứt), `genStyle` (tím liền).
6. Lập bảng quan hệ chi tiết ngay dưới sơ đồ:
   - Cột: `Mã Use Case con | Tên Use Case con | Căn cứ FR/BR | Quan hệ | Điều kiện kích hoạt & Lý do nghiệp vụ`.
   - Cột "Quan hệ" ghi rõ: `<<include>>`, `<<extend>>`, hoặc `Generalization (Kế thừa)`.

---

## 6. Kiểm tra trước khi trình cổng (Gate Checklist)

- [ ] **100% trong phạm vi FR:** Không có bất kỳ Use Case con nào do agent tự suy diễn hoặc bịa ra ngoài tài liệu `FR-Mxx.md`.
- [ ] **Đơn nghiệp vụ:** TẤT CẢ các Use Case con (dù giữ nguyên hay gộp) đều đảm nhiệm đúng duy nhất 1 nghiệp vụ xác định cụ thể.
- [ ] **Tên Use Case con chuẩn BA:** 100% tuân thủ cấu trúc `[1 Động từ duy nhất] + [Cụm danh từ]`.
- [ ] Phân định rõ ràng giữa `<<include>>`, `<<extend>>`, và `Generalization`, không có sự lẫn lộn.
- [ ] Mũi tên Mermaid đúng chiều chuẩn UML:
  + Include: từ Chính sang Con.
  + Extend: từ Con sang Chính.
  + Generalization: nét liền từ Con chuyên biệt về Cha tổng quát.
- [ ] Nhãn mũi tên và node Mermaid bọc ngoặc kép đầy đủ, không gây lỗi cú pháp parser.
- [ ] Bảng quan hệ có căn cứ FR/BR chính xác (kể cả khi gộp nhiều mã).

---

## 7. Cổng xác nhận

Gửi tin nhắn theo mẫu trong SKILL.md và chờ.
