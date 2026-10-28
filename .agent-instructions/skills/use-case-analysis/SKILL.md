---
name: use-case-analysis
description: >
  Phân tích tài liệu Yêu cầu Chức năng (FR-Mxx.md) của một module iShare
  và sản xuất tài liệu Đặc tả Use Case (US-Mxx.md) lưu tại docs/specs/us/.
  Kết quả bao gồm: bảng tổng hợp chức năng con, sơ đồ Use Case tổng quan
  (macro), 3–6 Use Case Chính kèm actor và quy trình nghiệp vụ hoàn chỉnh,
  phân rã Use Case con với 3 loại quan hệ UML chuẩn: <<include>>, <<extend>>,
  và Generalization (Kế thừa / Cha-Con), cùng ma trận truy vết FR-to-UC đầy đủ.
  Dùng khi người dùng yêu cầu tạo, viết, hoặc phân tích use case
  (US document, tài liệu use case, phân tích use case) cho một module iShare.
---

# Phân tích Use Case cho một module iShare (use-case-analysis)

Bạn là chuyên viên phân tích nghiệp vụ. Bạn đọc tài liệu Yêu cầu Chức năng (FR)
đã được duyệt và phân rã thành tài liệu Đặc tả Use Case (US) chuẩn UML theo
đúng cấu trúc `output/us-template.md`.

Đây là đồ án tốt nghiệp. Tài liệu phân tích được chấm chặt — mỗi Use Case phải
truy được về đúng mã FR, mỗi sơ đồ Mermaid phải render không lỗi, và các phán
đoán phân loại quan hệ (`<<include>>`, `<<extend>>`, `Generalization`) phải có
lý do nghiệp vụ rõ ràng.

## Nguyên tắc cốt lõi

1. **Chỉ bám FR.** Nguồn duy nhất là tài liệu `FR-Mxx.md`. Không thêm Use Case hay hành vi mà FR không mô tả.
2. **Không đề xuất ngoài phạm vi.** Mọi Use Case (cả Chính và Con) phải ánh xạ tới ít nhất một mã chức năng `FR-Mxx-nn` hoặc một Business Rule `BR-Mxx-nn`. Tuyệt đối cấm tự suy diễn, sáng tạo thêm Use Case hay chức năng ngoài phạm vi tài liệu FR.
3. **Quy tắc xác định Use Case con (Bắt buộc — Tuyệt đối trong phạm vi FR & Đơn nghiệp vụ):**
   - **Giới hạn phạm vi nghiêm ngặt:** Việc xác định các Use Case con **CHỈ ĐƯỢC PHÉP TRONG PHẠM VI** các chức năng đã xác định trong tài liệu `FR-Mxx.md` tương ứng. Tuyệt đối không được vượt quá phạm vi; nghiêm cấm agent tự ý suy diễn hoặc "nghĩ ra" thêm các Use Case con không có căn cứ trong FR (chống Out-of-Scope / Hallucination).
   - **Hai cơ chế hình thành Use Case con hợp lệ từ FR:**
     + **Cơ chế 1 — Giữ nguyên (1-to-1):** Giữ nguyên một chức năng FR (hoặc chức năng chi tiết `FR-Mxx-yy.zz` đã nêu trong FR) làm một Use Case con độc lập.
     + **Cơ chế 2 — Gộp lại (N-to-1):** Có thể gộp các chức năng FR lại với nhau thành 1 Use Case con nếu chúng có liên quan mật thiết và cùng thực hiện trong một chuỗi thao tác/nghiệp vụ gắn kết.
   - **Tính đơn nhất về nghiệp vụ (Single Business Responsibility):** Dù giữ nguyên hay gộp, **mỗi Use Case con BẮT BUỘC chỉ được thực hiện ĐÚNG DUY NHẤT 1 nghiệp vụ xác định cụ thể**. Tuyệt đối không gom các nghiệp vụ khác biệt, rời rạc hoặc có mục đích hành vi khác nhau vào một Use Case con tạp nham.
   - **Truy vết minh bạch:** Mọi Use Case con đều phải ghi rõ căn cứ mã `FR-Mxx-nn` (khi gộp thì ghi đủ các mã thành phần, ví dụ `FR-M02-04.01 - 04.05`).
4. **Quy tắc đặt tên Use Case (Bắt buộc, chuẩn BA chuyên nghiệp):**
   - **Cấu trúc ngữ pháp:** `[Động từ duy nhất] + [Cụm danh từ bổ nghĩa]` (Verb + Noun Phrase). Cả tên tiếng Việt và tiếng Anh đi kèm đều tuân thủ nguyên tắc này.
   - **Chỉ chứa ĐÚNG 1 động từ:** Tuyệt đối **KHÔNG** dùng nhiều động từ ghép nối nhau qua các từ liên kết như "và", "với", "hoặc", "&", "/", dấu gạch chéo hay gạch nối. Động từ duy nhất này phản ánh chính xác nghiệp vụ đơn nhất của Use Case đó.
     - *Sai:* `Khám phá & Xem trang hồ sơ`, `Chỉnh sửa và tùy biến hồ sơ`, `Quản lý & khôi phục mật khẩu`, `Tải lên & đổi avatar`, `Tìm kiếm và gợi ý người dùng`.
     - *Đúng:* `Xem hồ sơ người dùng`, `Cập nhật hồ sơ cá nhân`, `Quản lý mật khẩu`, `Đổi ảnh đại diện`, `Gợi ý người dùng`.
   - **Mang tính con người (Human-centric), tường minh, đúng nghiệp vụ:**
     - Tên phản ánh đúng mục tiêu hành vi mà người dùng muốn đạt được (Actor Goal) theo góc nhìn tự nhiên của con người.
     - Dùng các động từ chuẩn mực của BA: `Xem`, `Cập nhật`, `Lưu`, `Bỏ lưu`, `Đổi`, `Xác minh`, `Đăng nhập`, `Đăng ký`, `Gửi`, `Nhắc tên`, `Khôi phục`, `Vô hiệu hóa`, `Kích hoạt`.
     - Áp dụng nghiêm ngặt cho cả Use Case Chính (`UC-Cnn`) và Use Case con (`UC-nn.n`).
5. **100% truy vết.** Mọi mã `FR-Mxx-nn` trong mục 4.4 của tài liệu FR phải xuất hiện trong ma trận truy vết (Mục 4 của US). Không bỏ sót.
6. **Ba loại quan hệ chuẩn UML giữa các Use Case:**
   - **`<<include>>` (Bao hàm bắt buộc):** Use Case chính bắt buộc phải thực hiện Use Case con để hoàn thành. Thiếu nó quy trình không thể kết thúc. (Chiều mũi tên nét đứt từ Chính sang Con: `UC_Chinh -.->|"<<include>>"| UC_Con`).
   - **`<<extend>>` (Mở rộng tùy chọn / Rẽ nhánh):** Use Case con mở rộng hoặc bổ sung hành vi cho Use Case chính tại điểm mở rộng khi thỏa mãn điều kiện nhất định. Use Case chính vẫn có thể hoàn tất mà không cần Use Case con này. (Chiều mũi tên nét đứt từ Con sang Chính: `UC_Con -.->|"<<extend>>"| UC_Chinh`).
   - **`Generalization` (Kế thừa / Khái quát hóa / Quan hệ Cha - Con):** Use Case con là một dạng chuyên biệt hóa cụ thể của Use Case cha tổng quát (*"is-a-kind-of"*). Use Case con kế thừa toàn bộ mục tiêu, quyền truy cập và hành vi cơ bản của cha, đồng thời chuyên biệt hóa cơ chế thực hiện.
     *Ví dụ kinh điển:* Use Case cha **"Đăng nhập hệ thống"** khái quát hóa cho 2 Use Case con: **"Đăng nhập bằng Email/Password"** và **"Đăng nhập bằng Google OAuth"**; hoặc **"Đăng ký tài khoản"** là cha của **"Đăng ký bằng Email"** và **"Đăng ký bằng Google OAuth"**. (Trong sơ đồ Mermaid dùng mũi tên nét liền từ Con trỏ về Cha: `UC_Con -->|"<<generalization>>"| UC_Cha`, tương ứng mũi tên tam giác rỗng trong UML).
7. **Phân định rõ chức năng không phải Use Case:**
   - **`*(Tiến trình ngầm)*`:** Các tác vụ daemon, cron job, batch job, rotation token nền tảng kỹ thuật tự động chạy (ví dụ `FR-M01-06`, `FR-M01-12`).
   - **`*(Tầng hiển thị)*`:** Các logic kiểm soát hiển thị thụ động, filter dữ liệu (ví dụ `FR-M01-13`).
   Cả hai nhóm này KHÔNG biến thành Use Case tương tác của Actor mà được ghi nhận vai trò đặc thù trong ma trận truy vết (Mục 4.1).
8. **Quan hệ linh hoạt giữa FR và Use Case:**
   - Khi gộp: Nhiều chức năng con FR liên quan có thể gom thành 1 Use Case con đơn nhiệm (N-to-1).
   - Khi tách/phân nhánh: Một mã `FR-Mxx-nn` có thể sinh ra nhiều Use Case con với các vai trò khác nhau (cả `<<include>>`, `<<extend>>`, `Generalization`).
   - Khi chia sẻ: Một mã `FR-Mxx-nn` có thể tham gia vào nhiều Use Case Chính (ví dụ `FR-M01-04` vừa thuộc `UC-C01` vừa thuộc `UC-C02`).
9. **Mermaid phải render.** Áp dụng nghiêm túc Quy tắc Mermaid ở mục cuối file này. Sơ đồ có lỗi cú pháp là lỗi nghiêm trọng.
10. **Ngôn ngữ:** Tài liệu viết bằng tiếng Việt, thuật ngữ kỹ thuật giữ nguyên tiếng Anh (`username`, `JWT`, `OAuth`, `ACTIVE`, `<<include>>`, `<<extend>>`, `Generalization`, v.v.).
11. **Một bước một lượt.** Mỗi lượt làm đúng một bước, rồi dừng chờ xác nhận.

## Bắt đầu hoặc tiếp tục

1. Xác định module (Mxx). Chưa rõ thì hỏi.
2. Đọc `input/INPUTS.md` và kiểm tra tệp FR tồn tại. Thiếu thì dừng, báo lỗi.
3. Nếu `US-Mxx.md` chưa có: chép `output/us-template.md` sang `docs/specs/us/US-Mxx.md`, điền metadata, bắt đầu Bước 1.
4. Nếu đã có: đọc phần cuối file để biết bước đã làm, tiếp tục bước kế tiếp.
5. Chỉ đọc file bước đang làm trong `steps/`. Không nạp trước file bước sau.

## Các bước

| Bước | Tệp | Kết quả chính ghi vào US |
|---|---|---|
| 1 | `steps/01-extract-functions.md` | Mục 1: Bảng tổng hợp chức năng con |
| 2 | `steps/02-identify-core-ucs.md` | Mục 2.1–2.2: Danh sách UC Chính + Macro Diagram |
| 3 | `steps/03-map-actors.md` | Mục 2.3: Actor + Quy trình nghiệp vụ hoàn chỉnh |
| 4 | `steps/04-decompose-sub-ucs.md` | Mục 3: Phân rã UC con (Include, Extend, Generalization) + Per-UC Diagrams |
| 5 | `steps/05-build-traceability.md` | Mục 4.1: Ma trận truy vết FR→UC |
| 6 | `steps/06-write-diagrams.md` | Mục 4.2: Sơ đồ tổng hợp toàn module |
| 7 | `steps/07-assemble-verify.md` | Kiểm tra cuối, hoàn thiện, chốt |

## Quy tắc cổng xác nhận (bắt buộc)

- Mỗi lượt làm **đúng một bước**, rồi dừng.
- Cuối bước gửi tin nhắn cổng và **chờ**.
- Chỉ sang bước sau khi người dùng đồng ý rõ ràng ("ok", "tiếp", "đồng ý").
- Im lặng hoặc câu hỏi ngược **không** phải là đồng ý.

### Mẫu tin nhắn cổng

```
Bước N/7 — <tên bước> — Mxx: xong, chờ bạn xác nhận.

Kết quả: <3–5 dòng điểm chính — số UC Chính, số UC con, số FR đã ánh xạ>
Cần bạn nhìn: <tối đa 6 dòng: điểm phán đoán, ngoài lệ, WARN>
Đã ghi: US-Mxx.md mục <…>

Trả lời "ok" để sang bước N+1, hoặc nói chỗ cần sửa.
```

## Quy tắc Mermaid (bắt buộc, không có ngoại lệ)

1. Chỉ dùng `flowchart LR` (macro) hoặc `flowchart TB` (per-UC và tổng hợp).
2. Node label có dấu ngoặc đơn `()`, dấu nháy, ký tự đặc biệt → **bắt buộc đặt trong chuỗi kép**: `["text"]` hoặc `(["text"])`.
3. Arrow label **bắt buộc đặt trong chuỗi kép**:
   - Include: `-.->|"<<include>>"|`
   - Extend: `-.->|"<<extend>>"|`
   - Generalization: `-->|"<<generalization>>"|`
   KHÔNG ĐƯỢC để nhãn không có dấu nháy.
4. **Không dùng `\n` trong nhãn.** Xuống dòng trong node → dùng `<br/>`.
5. **Không dùng HTML tags** (`<b>`, `<i>`, `<u>`) bên trong label node.
6. `classDef` cho style chuẩn:
   - Include: `classDef incStyle fill:#e8f5e9,stroke:#2e7d32,stroke-width:1.5px;` (xanh lá)
   - Extend: `classDef extStyle fill:#fffde7,stroke:#f57f17,stroke-width:1.5px,stroke-dasharray: 4 4;` (vàng đứt đoạn)
   - Generalization: `classDef genStyle fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1.5px;` (tím nhạt, nét liền)
   - Actor: `classDef actorStyle fill:#ffffff,stroke:#333333,stroke-width:2px;`
   - Core UC: `classDef coreUC fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,font-weight:bold;`
7. Test nhanh: Nếu label có `(` hoặc `)` → PHẢI bọc bằng `"..."`.
8. **Tuyệt đối không dùng dấu ngoặc nhọn kép `{{` hoặc `}}` bên trong code block Mermaid.** Trong cú pháp Mermaid, `{{` được hiểu là toán tử tạo hình Hexagon / Diamond (`DIAMOND_START`), sẽ gây lỗi phân tích cú pháp nghiêm trọng (`Parse error`). Khi làm template hoặc placeholder trong sơ đồ, chỉ dùng các định danh an toàn như `Actor1`, `Mxx_Core`, `UC_C01`.

## Tài liệu mẫu tham khảo

- Input mẫu: `docs/specs/fr/FR-M01.md`
- Output mẫu: `docs/specs/us/US-M01.md` ← **Chuẩn vàng, đọc trước khi bắt đầu**
