# Tài liệu Đặc tả Use Case — {{MODULE_CODE}}: {{MODULE_NAME}} (US-{{MODULE_CODE}})

| Thuộc tính | Nội dung |
|---|---|
| **Mã tài liệu** | `US-{{MODULE_CODE}}` |
| **Dự án** | iShare — Nền tảng chia sẻ tri thức và hỏi đáp học sinh THPT |
| **Module** | {{MODULE_CODE}} — {{MODULE_NAME}} |
| **Tài liệu căn cứ (Nguồn)** | [`FR-{{MODULE_CODE}}.md`](file:///g:/documents/season9/iShare/docs/specs/fr/FR-{{MODULE_CODE}}.md) (Phiên bản {{FR_VERSION}} — Ngày {{FR_DATE}}) |
| **Mốc register căn cứ** | {{REGISTER_REFS}} |
| **Người thực hiện** | Antigravity Engine (Tổng hợp & Phân rã theo yêu cầu BA) |
| **Ngày lập** | {{DATE}} |
| **Trạng thái** | Đang thực hiện |

---

## 1. Bảng Tổng hợp các Chức năng con trong {{MODULE_CODE}}

Căn cứ theo mục 4.4 và mục 5 trong tài liệu [`FR-{{MODULE_CODE}}.md`](file:///g:/documents/season9/iShare/docs/specs/fr/FR-{{MODULE_CODE}}.md), module bao gồm {{N}} chức năng con với mô tả ngắn gọn như sau:

| STT | Mã chức năng | Tên chức năng con | Mô tả ngắn gọn phạm vi & nghiệp vụ |
|:---:|:---:|---|---|
| 1 | **FR-{{MODULE_CODE}}-01** | {{FUNCTION_NAME_1}} | {{SHORT_DESCRIPTION_1}} |
| 2 | **FR-{{MODULE_CODE}}-02** | {{FUNCTION_NAME_2}} | {{SHORT_DESCRIPTION_2}} |
| ... | ... | ... | ... |

---

## 2. Phân rã thành các Use Case Chính & Quy trình Nghiệp vụ Hoàn chỉnh

### 2.1 Tiêu chí phân rã Use Case Chính
- **Đủ lớn & Độc lập:** Đại diện cho một mục tiêu nghiệp vụ trọn vẹn của người dùng (User Goal) hoặc của hệ thống.
- **Có tương tác giao diện trực tiếp:** Bắt đầu bằng một hành động chủ động của Actor trên giao diện (UI) và kết thúc khi đạt được kết quả mong đợi.
- **Bao hàm các chức năng con:** Chứa đựng các bước thực hiện mang tính nghiệp vụ bắt buộc hoặc tùy chọn mở rộng.
- **Quy tắc đặt tên:** Cấu trúc `[1 Động từ duy nhất] + [Cụm danh từ]`. Tuyệt đối không dùng nhiều động từ nối nhau ("và", "&", "/", "hoặc"). Văn phong con người, chuẩn nghiệp vụ.

Từ {{N}} chức năng con, module được phân rã thành **{{M}} Use Case Chính** sau:
1. **UC-C01: {{UC1_NAME_VI}} ({{UC1_NAME_EN}})**
2. **UC-C02: {{UC2_NAME_VI}} ({{UC2_NAME_EN}})**
<!-- Thêm các UC Chính khác nếu có -->

---

### 2.2 Sơ đồ Use Case Tổng quan của Module {{MODULE_CODE}} (Macro Use Case Diagram)

```mermaid
flowchart LR
    %% ACTORS
    Actor1(["Actor 1"])
    Actor2(["Actor 2"])

    %% CORE USE CASES
    subgraph Mxx_Core ["MODULE Mxx: TÊN MODULE (TỔNG QUAN)"]
        direction TB
        UC_C01(["UC-C01: Tên Use Case Chính 1<br/>(Core UC 1 Name)"])
        UC_C02(["UC-C02: Tên Use Case Chính 2<br/>(Core UC 2 Name)"])
    end

    %% LIÊN KẾT ACTOR - USE CASE CHÍNH
    Actor1 --> UC_C01
    Actor1 --> UC_C02
    Actor2 --> UC_C02

    %% Styling
    classDef actorStyle fill:#ffffff,stroke:#333333,stroke-width:2px;
    classDef coreUC fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,font-weight:bold;
    class Actor1,Actor2 actorStyle;
    class UC_C01,UC_C02 coreUC;
```

---

### 2.3 Mô tả Quy trình Nghiệp vụ Hoàn chỉnh của từng Use Case Chính

<!-- Áp dụng Kiểu A (Quy trình tuần tự) HOẶC Kiểu B (Phân nhánh song song) tùy bản chất UC -->

#### 1. UC-C01: {{UC1_NAME_VI}} ({{UC1_NAME_EN}}) — [Ví dụ Kiểu A: Tuần tự]
- **Actor chính:** `{{ACTOR_1}}`.
- **Mục tiêu:** {{GOAL_DESCRIPTION_1}}.
- **Quy trình nghiệp vụ hoàn chỉnh:**
  1. *Khởi đầu:* {{STEP_1_START}}
  2. *Thực hiện & Kiểm tra:* {{STEP_1_EXECUTION}}
  3. *Kết thúc:* {{STEP_1_END}}

#### 2. UC-C02: {{UC2_NAME_VI}} ({{UC2_NAME_EN}}) — [Ví dụ Kiểu B: Phân nhánh song song]
- **Actor chính:** `{{ACTOR_A}}` (cho Nhánh 1), `{{ACTOR_B}}` (cho Nhánh 2).
- **Mục tiêu:** {{GOAL_DESCRIPTION_2}}.
- **Quy trình nghiệp vụ hoàn chỉnh:**
  - *Nhánh 1 — {{BRANCH_1_NAME}}:* {{ACTOR_A}} bắt đầu từ {{SCREEN_1}} $\to$ {{ACTIONS_AND_RULES_1}} $\to$ Hệ thống phản hồi {{RESULT_1}}.
  - *Nhánh 2 — {{BRANCH_2_NAME}}:* {{ACTOR_B}} bắt đầu từ {{SCREEN_2}} $\to$ {{ACTIONS_AND_RULES_2}} $\to$ Hệ thống phản hồi {{RESULT_2}}.

<!-- Tiếp tục mô tả cho các UC Chính tiếp theo -->

---

## 3. Xác định Use Case con Chi tiết và Mối quan hệ với Use Case Chính

Toàn bộ các Use Case con được phân rã strictly trong phạm vi các chức năng đã xác định trong tài liệu `FR-{{MODULE_CODE}}.md` (bằng cách giữ nguyên chức năng độc lập hoặc gộp các chức năng liên quan mật thiết); mỗi Use Case con đảm nhiệm đúng duy nhất 1 nghiệp vụ xác định cụ thể và tuân thủ quy tắc 1 động từ duy nhất.

Mối quan hệ giữa Use Case Chính và Use Case con được phân loại theo đúng 3 loại quan hệ chuẩn UML:
- **`<<include>>` (Bao hàm Bắt buộc):** Bước nghiệp vụ tiên quyết, bắt buộc phải có để Use Case chính thành công. (Mũi tên nét đứt từ Chính sang Con).
- **`<<extend>>` (Mở rộng Tùy chọn / Rẽ nhánh):** Bước mở rộng, tính năng tùy chọn hoặc nhánh ngoại lệ. (Mũi tên nét đứt từ Con sang Chính).
- **`Generalization` (Kế thừa / Cha - Con):** Use Case con là một dạng chuyên biệt hóa cụ thể của Use Case cha tổng quát (*is-a-kind-of*). (Mũi tên nét liền từ Con sang Cha).

---

### 3.1 Phân rã UC-C01: {{UC1_NAME_VI}}

```mermaid
flowchart TB
    Actor1(["Actor 1"]) --> UC_C01(["UC-C01: Tên Use Case Chính 1"])

    subgraph Sub_UCC01 ["Các Use Case phụ của UC-C01"]
        direction TB
        %% Bắt buộc (Include)
        INC_01_1(["UC-01.1: Tên UC con Bắt buộc<br/>[FR-Mxx-01]"])

        %% Tùy chọn / Mở rộng (Extend)
        EXT_01_1(["UC-01.2: Tên UC con Mở rộng<br/>[FR-Mxx-02]"])

        %% Kế thừa / Cha-Con (Generalization)
        GEN_01_1(["UC-01.3: Tên UC con Kế thừa Chuyên biệt hóa<br/>[FR-Mxx-03]"])
    end

    %% Quan hệ Include
    UC_C01 -.->|"<<include>>"| INC_01_1

    %% Quan hệ Extend
    EXT_01_1 -.->|"<<extend>>"| UC_C01

    %% Quan hệ Generalization
    GEN_01_1 -->|"<<generalization>>"| UC_C01

    classDef incStyle fill:#e8f5e9,stroke:#2e7d32,stroke-width:1.5px;
    classDef extStyle fill:#fffde7,stroke:#f57f17,stroke-width:1.5px,stroke-dasharray: 4 4;
    classDef genStyle fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1.5px;
    class INC_01_1 incStyle;
    class EXT_01_1 extStyle;
    class GEN_01_1 genStyle;
```

#### Bảng chi tiết quan hệ, điều kiện & lý do nghiệp vụ (UC-C01):
| Mã Use Case con | Tên Use Case con | Căn cứ FR/BR | Quan hệ | Điều kiện kích hoạt & Lý do nghiệp vụ |
|---|---|:---:|:---:|---|
| **UC-01.1** | {{INC_SUB_UC_NAME}} | FR-{{MODULE_CODE}}-01 | `<<include>>` | **Bắt buộc:** {{REASON_MANDATORY}} |
| **UC-01.2** | {{EXT_SUB_UC_NAME}} | FR-{{MODULE_CODE}}-02 | `<<extend>>` | **{{EXTENSION_TYPE}}:** {{REASON_CONDITIONAL}} |
| **UC-01.3** | {{GEN_SUB_UC_NAME}} | FR-{{MODULE_CODE}}-03 | Generalization | **Kế thừa (Chuyên biệt hóa):** Là một dạng hình thức cụ thể của Use Case cha; kế thừa toàn bộ mục tiêu và quy tắc của cha nhưng áp dụng phương thức thực thi chuyên biệt. |

---

### 3.2 Phân rã UC-C02: {{UC2_NAME_VI}}

<!-- Lặp lại cấu trúc sơ đồ và bảng quan hệ chi tiết cho UC-C02 và các UC Chính tiếp theo -->

---

## 4. Bảng Tổng kết Ánh xạ & Sơ đồ Use Case Chi tiết Toàn Module

### 4.1 Bảng Ma trận Ánh xạ Toàn bộ Chức năng con vào Hệ thống Use Case

| Mã FR | Tên chức năng con trong `FR-{{MODULE_CODE}}.md` | Thuộc Use Case Chính | Thuộc Use Case Phụ cụ thể | Vai trò quan hệ trong UC Chính |
|:---:|---|:---:|---|:---:|
| **FR-{{MODULE_CODE}}-01** | {{FUNCTION_NAME_1}} | **UC-C01** | UC-01.1: {{SUB_NAME_1}} | `<<include>>` (Bắt buộc) |
| **FR-{{MODULE_CODE}}-02** | {{FUNCTION_NAME_2}} | **UC-C01** | UC-01.2: {{SUB_NAME_2}}<br>UC-01.3: {{SUB_NAME_3}} | `<<include>>` (Bắt buộc)<br>`<<extend>>` (Tùy chọn) |
| **FR-{{MODULE_CODE}}-03** | {{FUNCTION_NAME_3}} | **UC-C01** | UC-01.4: {{SUB_NAME_4}} | Generalization (Chuyên biệt hóa) |
| **FR-{{MODULE_CODE}}-04** | {{FUNCTION_NAME_4}} | **UC-C01**<br>**UC-C02** | UC-01.5: {{SUB_NAME_5}}<br>UC-02.3: {{SUB_NAME_6}} | `<<extend>>` (Thay thế)<br>`<<extend>>` (Rẽ nhánh) |
| **FR-{{MODULE_CODE}}-05** | {{FUNCTION_NAME_5}} | *(Tiến trình ngầm)* | {{BACKGROUND_JOB_DESCRIPTION}} | Nền tảng hạ tầng kỹ thuật |
| **FR-{{MODULE_CODE}}-06** | {{FUNCTION_NAME_6}} | *(Tầng hiển thị)* | {{DISPLAY_FILTER_DESCRIPTION}} | Logic kiểm soát hiển thị |

---

### 4.2 Sơ đồ Use Case Chi tiết Toàn Module

```mermaid
flowchart TB
    %% ACTORS
    Actor1(["Actor 1"])
    Actor2(["Actor 2"])

    %% UC-C01 GROUP
    subgraph UCC01 ["UC-C01: Tên Use Case Chính 1"]
        direction TB
        UC_C01(["UC-C01: Tên Use Case Chính 1"])
        INC_C01_1(["UC-01.1: Tên UC con Bao hàm<br/>[FR-Mxx-01]"])
        EXT_C01_1(["UC-01.2: Tên UC con Mở rộng<br/>[FR-Mxx-02]"])
        GEN_C01_1(["UC-01.3: Tên UC con Kế thừa<br/>[FR-Mxx-03]"])
        UC_C01 -.->|"<<include>>"| INC_C01_1
        EXT_C01_1 -.->|"<<extend>>"| UC_C01
        GEN_C01_1 -->|"<<generalization>>"| UC_C01
    end

    %% UC-C02 GROUP
    subgraph UCC02 ["UC-C02: Tên Use Case Chính 2"]
        direction TB
        UC_C02(["UC-C02: Tên Use Case Chính 2"])
        INC_C02_1(["UC-02.1: Tên UC con Bao hàm<br/>[FR-Mxx-04]"])
        UC_C02 -.->|"<<include>>"| INC_C02_1
    end

    %% ACTORS TO CORE USE CASES
    Actor1 --> UC_C01
    Actor1 --> UC_C02
    Actor2 --> UC_C02

    %% STYLING
    classDef actorStyle fill:#ffffff,stroke:#333333,stroke-width:2px;
    classDef coreUC fill:#e1f5fe,stroke:#0288d1,stroke-width:2px,font-weight:bold;
    classDef incStyle fill:#e8f5e9,stroke:#2e7d32,stroke-width:1.5px;
    classDef extStyle fill:#fffde7,stroke:#f57f17,stroke-width:1.5px,stroke-dasharray: 4 4;
    classDef genStyle fill:#f3e5f5,stroke:#7b1fa2,stroke-width:1.5px;
    class Actor1,Actor2 actorStyle;
    class UC_C01,UC_C02 coreUC;
    class INC_C01_1,INC_C02_1 incStyle;
    class EXT_C01_1 extStyle;
    class GEN_C01_1 genStyle;
```
