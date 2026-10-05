# BA Output — Hướng dẫn đọc & Truy vết

> **Thư mục này là workspace output của BA agent** trong quá trình phỏng vấn hệ thống iShare.
> Mọi thứ ở đây là tài liệu làm việc — chưa phải output chính thức.
> Sau khi stakeholder approve, spec files sẽ được push sang `docs/approved/specs/`.

---

## Cấu trúc thư mục

```
output/
├── README.md              ← File này
├── registers/             ← 6 live registers (cập nhật liên tục trong suốt BA)
│   ├── issue-queue.md
│   ├── qa-log.md
│   ├── decisions.md
│   ├── open-issues.md
│   ├── assumptions.md
│   └── glossary.md
└── specs/                 ← Tài liệu System Requirement (DEC-139)
    ├── ISH-SR-Mxx.md        ← SR của module Mxx (tiếng Việt)
    ├── routing/ISH-RT-Mxx.md ← mục nguồn không thành yêu cầu chức năng
    └── audit/               ← báo cáo audit + tệp làm việc (work/)
```

---

## 6 Registers — Mục đích & Cách đọc

### 1. `issue-queue.md` — Backlog phỏng vấn

**Dùng để làm gì:** Danh sách tất cả câu hỏi BA cần hỏi stakeholder, được xây dựng từng scope.

**Cách đọc:**
- `Status: Closed` → đã hỏi và có câu trả lời → xem `Resulting QA-###`
- `Status: Open` + Scope Phase X backlog → chưa hỏi, sẽ hỏi khi vào Phase đó
- `Status: Open` + Scope Phase 1/2 → câu hỏi còn treo từ phase đã qua (xem `open-issues.md`)

**ID convention:** `ISS-###` (sequential) hoặc `ISS-MOD-##` (module-specific backlog)

---

### 2. `qa-log.md` — Nhật ký hỏi đáp (**nguồn gốc của mọi requirement**)

**Dùng để làm gì:** Ghi lại toàn bộ câu hỏi + câu trả lời của stakeholder + phân tích + implication.

**Cách đọc:**
- Mỗi block `QA-###` = 1 lần hỏi đáp
- `Issue ref` → ISS nào đã sinh ra câu hỏi này
- `Answer` → câu trả lời chính xác của stakeholder
- `Implication` → BA phân tích ảnh hưởng lên hệ thống
- `Traceability note` → ghi chú để mở rộng vào báo cáo luận văn

**Trace từ spec về nguồn gốc:**
```
Spec rule → QA-### → ISS-### → Phase X
```

---

### 3. `decisions.md` — Nhật ký quyết định

**Dùng để làm gì:** Ghi nhanh các quyết định thiết kế đã chốt.

**Cách đọc:**
- `DEC-###`: ID quyết định
- `Source: QA-###`: QA nào dẫn đến quyết định này
- Đọc khi cần biết nhanh **cái gì đã được quyết** mà không cần đọc toàn bộ QA log

---

### 4. `open-issues.md` — Vấn đề chưa giải quyết (chặn spec)

**Dùng để làm gì:** Theo dõi những điểm **chưa có câu trả lời dứt khoát** và ảnh hưởng đến việc viết spec.

**Cách đọc:**
- `OPEN-###`: ID vấn đề treo
- `Why it blocks`: feature/spec nào bị chặn
- `Affected features`: module/feature cụ thể bị ảnh hưởng
- Khác với `issue-queue`: OPEN-### là vấn đề **không thể giải quyết ngay** và cần ghi nhận chính thức

**Hiện tại:**
- `OPEN-001`: AI budget chưa chốt
- `OPEN-002`: Tech stack chưa quyết định

---

### 5. `assumptions.md` — Giả định của BA

**Dùng để làm gì:** Khi stakeholder không trả lời / bỏ qua, BA tự giả định và ghi lại để xác nhận sau.

**Cách đọc:**
- `ASM-###`: ID giả định
- `Status: Unconfirmed` → cần stakeholder xác nhận trước khi finalize spec
- Hiện trống — mọi câu hỏi đều đã được trả lời

---

### 6. `glossary.md` — Bảng thuật ngữ

**Dùng để làm gì:** Định nghĩa thống nhất các khái niệm domain, tránh hiểu nhầm giữa BA, dev, stakeholder.

**Cách đọc:** Tra cứu khi gặp từ lạ trong spec hoặc QA log.

---

## Cách trace requirement từ spec về nguồn

Khi đọc một spec file và muốn biết **tại sao rule đó tồn tại**:

```
1. Tìm ID trong spec (FR-###, BR-###, AC-###)
2. Spec file sẽ ghi "Source: QA-###"
3. Mở qa-log.md → tìm QA-### đó
4. Đọc Answer (câu trả lời gốc của stakeholder) + Traceability note
5. Nếu cần ngược thêm → xem "Issue ref: ISS-###" trong QA block
6. Mở issue-queue.md → tìm ISS-### → biết scope/phase câu hỏi được đặt ra
```

---

## Lifecycle của output

```
[BA Interview] → registers/ (live, cập nhật liên tục)
     ↓ Phase 5 complete + stakeholder confirm
[Spec draft] → specs/ (trong thư mục này)
     ↓ Stakeholder approve
[Official] → iShare/docs/approved/specs/ (xem README ở đó)
```

---

## Conventions

| Prefix | Loại | Register |
|---|---|---|
| `ISS-###` | Interview issue (câu hỏi phỏng vấn) | issue-queue.md |
| `QA-###` | Q&A pair | qa-log.md |
| `DEC-###` | Decision | decisions.md |
| `OPEN-###` | Unresolved blocking issue | open-issues.md |
| `ASM-###` | Assumption | assumptions.md |
| `FR-MOD-###` | Functional requirement | specs/ |
| `BR-MOD-###` | Business rule | specs/ |
| `AC-MOD-###` | Acceptance criteria | specs/ |
| `NFR-CAT-###` | Non-functional requirement | specs/ |
| `ISH-SR-Mxx` / `ISH-RT-Mxx` | Tài liệu SR / routing file của module Mxx | specs/ |
| `ISH-Mxx-nnn[.k]` | Yêu cầu SR (cấp trên / cấp dưới) — thay cho `FR-MOD-###` trong SR | specs/ |
| `OP-Mxx-nn` / `AUD-Mxx-nn` | Điểm mở tạm thời trong SR / phát hiện audit | specs/ |

> Quy tắc đầy đủ của SR: `.agent-instructions/system_analysis/shared/SR-DOCUMENT-RULES.md`. Các ID `FR/BR/AC-MOD` chỉ còn dùng cho mẫu SPEC theo feature cũ (không dùng trong SR).

---

*Last updated: Phase 2 — Actors, Roles & Permissions (confirmed pending)*
