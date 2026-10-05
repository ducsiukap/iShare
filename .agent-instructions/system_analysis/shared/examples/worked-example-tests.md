# Ví dụ: ca kiểm của Author và ca kiểm độc lập của Auditor (module giả định M99)

> Dữ liệu giả định, không thuộc dự án. Mục đích: cho thấy ca kiểm làm lộ chỗ mơ hồ mà đối chiếu SR với nguồn không thấy.

**Nguồn giả định (DEC-901):** "Điểm Hot của một Chuyên mục = Σ(1 + 3 × lượt thích) trên mọi bài trong cửa sổ 7 ngày gần nhất, tính lại mỗi 15 phút."

**SR của Author (chép đúng nguồn):** ISH-M99-006.1 — "Hệ thống phải tính điểm Hot của một Chuyên mục bằng tổng, trên mọi bài thuộc Chuyên mục đó trong 7 ngày gần nhất, của giá trị 1 cộng 3 lần số lượt thích của bài viết."

Đối chiếu SR với nguồn: **khớp**. Không có lỗi nào lộ ra. Nhưng khi viết ca kiểm:

## Ca kiểm của Author (`tests-M99.md`)

| ID ca | ID yêu cầu | Loại | Given | When | Then | Giả định cần thêm |
|---|---|---|---|---|---|---|
| T-014 | ISH-M99-006.1 | Công thức | Chuyên mục K chỉ có bài B, đăng 20 ngày trước, hôm qua nhận 10 lượt thích | Tính điểm Hot của K | 0 hoặc 30 — chưa chọn được | "Trong 7 ngày" áp dụng cho ngày đăng bài hay ngày nhận lượt thích? |
| T-015 | ISH-M99-006.1 | Công thức | Chuyên mục K có một bài mới đăng hôm qua, chưa có lượt thích | Tính điểm Hot của K | 1 (nếu "1" là điểm cho mỗi bài trong cửa sổ) | Số "1" mỗi bài là điểm cho bài nào: mọi bài, bài đăng trong cửa sổ, hay bài có tương tác? |

Hai dòng cuối là **câu hỏi cho stakeholder** (khuôn §8.3), không được tự chọn rồi ghi `—`. Sau khi stakeholder trả lời và register có ID, SR được viết lại cho xác định, và hai ca được sửa lại với "Then" là một con số duy nhất.

## Ca kiểm độc lập của Auditor (lượt P3), dựng từ nguồn trước khi mở SR

| ID ca | Nguồn | Loại | Given | When | Then theo nguồn | Nguồn xác định? | ID yêu cầu SR | SR xác định? | Then theo ca kiểm của Author | Đối chiếu |
|---|---|---|---|---|---|---|---|---|---|---|
| A-007 | DEC-901 | Thời gian | K chỉ có bài B đăng 20 ngày trước; hôm qua B nhận 10 lượt thích | Tính điểm Hot của K | Cách 1: 0 điểm (chỉ tính bài đăng trong cửa sổ). Cách 2: 30 điểm (đếm lượt thích trong cửa sổ trên mọi bài) | **Mơ hồ** | ISH-M99-006.1 | Mơ hồ | "0 hoặc 30 — chưa chọn được" | Trùng (cả hai cùng nhận ra) |

Phân loại (`RULES` §11.4): nguồn `Mơ hồ` → **GAP** (CL-A11, mức Cao vì nằm ở công thức). Nếu Author đã hỏi và đã có ID register, SR theo đúng câu trả lời thì không có finding; nếu Author ghi `—` ở cột "Giả định cần thêm" mà vẫn chọn một cách đọc thì là CL-F04.
