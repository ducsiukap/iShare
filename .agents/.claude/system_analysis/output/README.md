# Đầu ra của giai đoạn System Analysis — Hướng dẫn đọc và truy vết

> Thư mục này là workspace đầu ra của agent trong giai đoạn System Analysis của iShare.
> Mọi thứ ở đây là tài liệu làm việc, chưa phải bản chính thức.
> Tài liệu được stakeholder duyệt sẽ được chuyển sang `docs/approved/` (COMMON-RULES Rule 3).
> Cách làm từng loại tài liệu: xem `.agent-instructions/README.md`.

---

## Cấu trúc thư mục

```
output/
├── README.md              ← tệp này
├── phase0-intake.md       ← hiểu biết ban đầu về sản phẩm và lịch trình phỏng vấn
├── registers/             ← các register sống, cập nhật trong suốt quá trình phân tích
│   ├── issue-queue.md
│   ├── qa-log.md
│   ├── decisions.md
│   ├── open-issues.md
│   ├── assumptions.md
│   ├── glossary.md
│   └── module-registry.md
└── fr/                    ← tài liệu yêu cầu chức năng, mỗi module một tệp
    ├── FR-Mxx.md
    └── .work/             ← tệp tạm của tool (chỉ mục nguồn, bảng nguồn); xóa được, chạy lại sẽ sinh lại
```

Tài liệu FR được viết bằng skill `.agent-instructions/skills/analyzing-functional-requirements/`
(hướng dẫn cho người dùng: `README.md` trong thư mục đó).

---

## Các register — mục đích và cách đọc

### 1. `issue-queue.md` — Backlog phỏng vấn

**Dùng để làm gì:** danh sách vấn đề cần hỏi stakeholder, chia theo phase và module.

**Cách đọc:**
- `Closed` → đã hỏi và có câu trả lời (xem QA, DEC tương ứng).
- `Open` → chưa hỏi, hoặc còn treo (xem `open-issues.md`).
- Một ID có thể xuất hiện hai lần: ở bảng backlog và ở bảng đã đóng của phase sau.

**Mã:** `ISS-###`, hoặc `ISS-XXX-##` cho backlog theo nhóm (ví dụ `ISS-GRP-01`).

### 2. `qa-log.md` — Nhật ký hỏi đáp (nguồn gốc của mọi yêu cầu)

**Dùng để làm gì:** ghi câu hỏi và câu trả lời của stakeholder. Phase đầu ghi theo khối `### QA-###`, các phase sau ghi theo bảng.

### 3. `decisions.md` — Nhật ký quyết định

**Dùng để làm gì:** các quyết định đã chốt (`DEC-###`), kèm nguồn QA.

**Cách đọc:**
- Quyết định sửa một mục cũ được đánh dấu ngay trên mục cũ, ví dụ `**[Amended YYYY-MM-DD — DEC-nnn: …]**`, `AMENDED by …`, `supersedes …`.
- Mục cũ không bị xóa. Luôn đọc cả dấu sửa đổi trước khi dùng một quyết định.

### 4. `open-issues.md` — Điểm chưa giải quyết

**Dùng để làm gì:** những điểm **chưa có câu trả lời dứt khoát** hoặc **hoãn có chủ đích** (`OPEN-###`), kèm phần bị ảnh hưởng.
Trong tài liệu FR, các điểm này được ghi thành TBD, không hỏi lại.

### 5. `assumptions.md` — Giả định

**Dùng để làm gì:** giả định đã được stakeholder xác nhận (`ASM-###`). Hiện chưa có.

### 6. `glossary.md` — Thuật ngữ

**Dùng để làm gì:** định nghĩa thống nhất các khái niệm của dự án.

### 7. `module-registry.md` — Danh sách module

**Dùng để làm gì:** 16 module (M01–M16), mức ưu tiên MoSCoW, phụ thuộc, các đợt sửa phạm vi.
Lưu ý: cột MoSCoW và Dependencies đang bị lệch ở các dòng M02–M10 và M13, cần stakeholder bổ sung.

---

## Truy vết một yêu cầu về nguồn

```
1. Trong FR-Mxx.md, tìm ID yêu cầu (ví dụ FR-M05-01.02 hoặc BR-M05-01).
2. Phụ lục A của tệp đó ghi nguồn (DEC-###, QA-###, ISS-###, mục draft DM-x.y / DG-x) và căn cứ (Nói thẳng / Suy ra).
3. Mở register tương ứng, đọc nguyên văn, kèm các dấu sửa đổi.
4. Phụ lục C.2 của tệp FR ghi chuỗi quyết định, nếu quyết định đó đã bị sửa.
```

---

## Vòng đời

```
[Phỏng vấn]   → registers/ (sống, cập nhật liên tục)
     ↓
[Viết FR]     → fr/FR-Mxx.md (Bản nháp → Đã chốt, mỗi bước có stakeholder xác nhận)
     ↓ stakeholder duyệt
[Chính thức]  → docs/approved/
```

---

## Quy ước mã

| Mã | Nghĩa | Nằm ở |
|---|---|---|
| `ISS-###` | Vấn đề trong backlog phỏng vấn | issue-queue.md |
| `QA-###` | Câu hỏi và câu trả lời | qa-log.md |
| `DEC-###` | Quyết định | decisions.md |
| `OPEN-###` | Điểm chưa giải quyết hoặc hoãn có chủ đích | open-issues.md |
| `ASM-###` | Giả định đã xác nhận | assumptions.md |
| `FR-Mxx` | Tài liệu yêu cầu chức năng của module Mxx | fr/ |
| `FR-Mxx-nn` · `FR-Mxx-nn.mm` | Chức năng (yêu cầu cấp trên) · yêu cầu cấp dưới | fr/ |
| `BR-Mxx-nn` · `TBD-Mxx-nn` | Quy tắc nghiệp vụ · điểm chưa chốt trong tài liệu FR | fr/ |
| `NFR-CAT-###` | Yêu cầu phi chức năng (Phase 7, chưa làm) | — |

Mã không bao giờ đánh lại. Quy trình SR cũ (`ISH-SR-Mxx`, `ISH-RT-Mxx`, `OP-*`, `AUD-*`) đã ngừng dùng và đã bị xoá.

---

*Cập nhật: 2026-10-07 — chuyển sang tài liệu FR theo skill analyzing-functional-requirements.*
