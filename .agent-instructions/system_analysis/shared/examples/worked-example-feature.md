# Ví dụ hoàn chỉnh: một tính năng đi từ nguồn đến SR, Phụ lục A, routing và câu hỏi

> Vai trò dùng: `sr-author`. Đọc trước khi viết tính năng đầu tiên.

Ví dụ **minh họa**, đối tượng và số liệu không phải nguồn của dự án. Dùng để hiểu cách một câu nguồn đi qua SR, Phụ lục A, routing và câu hỏi.

Nguồn giả định (`DEC-901`): "Người dùng viết bình luận cho bài viết. Bình luận dài tối đa 500 ký tự. Người dùng chỉ được sửa bình luận trong 15 phút sau khi đăng. Bình luận lưu kèm thời điểm đăng. Nút gửi màu xanh."

Mục 5.x:

````markdown
### 5.4 Viết bình luận

**Yêu cầu cấp trên**

| ID | Yêu cầu |
|---|---|
| ISH-M99-001 | Hệ thống phải cho phép người dùng viết bình luận cho một bài viết. |

**Lý do**

Nguồn chưa nêu lý do.

**Yêu cầu cấp dưới**

| ID | Yêu cầu |
|---|---|
| ISH-M99-001.1 | Hệ thống phải giới hạn mỗi bình luận tối đa 500 ký tự. |
| ISH-M99-001.2 | Khi người dùng gửi bình luận dài hơn 500 ký tự, hệ thống phải từ chối bình luận đó. |
| ISH-M99-001.3 | Khi người dùng sửa bình luận của mình trong vòng 15 phút sau khi đăng, hệ thống phải lưu nội dung đã sửa. |
| ISH-M99-001.4 | Khi người dùng sửa bình luận của mình sau 15 phút kể từ khi đăng, hệ thống phải từ chối việc sửa. |
````

Phụ lục A:

| ID | Nguồn | Cơ sở | Ghi chú |
|---|---|---|---|
| ISH-M99-001 | DEC-901 | Nói thẳng | |
| ISH-M99-001.1 | DEC-901 | Nói thẳng | |
| ISH-M99-001.2 | DEC-901 | Suy ra | Giới hạn "tối đa 500" ⇒ từ chối giá trị vượt (RULES §4.5) |
| ISH-M99-001.3 | DEC-901 | Nói thẳng | |
| ISH-M99-001.4 | DEC-901 | Suy ra | "Chỉ được sửa trong 15 phút" ⇒ từ chối khi quá hạn (RULES §4.5) |

Routing: hàng `DEC-901` ở R1 ("Bình luận lưu kèm thời điểm đăng; chi tiết lưu trữ thuộc mô hình dữ liệu") và ở R3 ("Nút gửi màu xanh; thuộc thiết kế giao diện"). Mục `DEC-901` nằm cả ở Phụ lục A lẫn routing vì chỉ một phần thành yêu cầu.

Mục "Lý do" ghi `Nguồn chưa nêu lý do.` nên Phụ lục B có thêm một `OP` loại Đề xuất (RULES §3.1), ví dụ `OP-M99-02`.

Điểm cần hỏi stakeholder (một câu hỏi theo RULES §8.3):

```
Vấn đề: Nguồn nêu bình luận dài tối đa 500 ký tự nhưng chưa nói ký tự xuống dòng có được tính không.
Nguồn: DEC-901: "Bình luận dài tối đa 500 ký tự."
Lựa chọn: A) Tính cả ký tự xuống dòng — hệ quả: bình luận nhiều đoạn bị giới hạn chặt hơn.
          B) Không tính ký tự xuống dòng — hệ quả: cần định nghĩa rõ cách đếm ở yêu cầu.
Đề xuất: A vì nguồn không loại trừ ký tự nào, và đây là cách hiểu theo nghĩa đen.
```

Trong lúc chờ trả lời: ghi `OP-M99-01` ở Phụ lục B (loại Mơ hồ, trạng thái Mở), giữ ISH-M99-001.1 như trên và nêu rõ với stakeholder rằng yêu cầu có thể đổi theo câu trả lời.
