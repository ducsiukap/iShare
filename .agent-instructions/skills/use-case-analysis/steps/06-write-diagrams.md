# Bước 6 — Sơ đồ UC chính tổng quan và UC con chi tiết

[Vietnamese Doc]

Đọc [diagram-rules](../references/diagram-rules.md). Đầu ra bắt buộc theo scope:

| Scope | Các sơ đồ phải có |
|---|---|
| Một module | Tổng quan module từ core; một sơ đồ chi tiết riêng cho từng core |
| Toàn hệ thống | Tổng hợp các core module thành tổng quan hệ thống, link về chi tiết module |
| Một phần | Đúng phần core/sub được yêu cầu, ghi rõ phần module chưa hoàn tất |

1. Lấy core/sub từ catalog và bảng decomposition, không tự tạo UC chỉ khi vẽ.
2. Tổng quan module: actor và UC chính. Với **mỗi UC chính**, tạo một sơ đồ
   chi tiết riêng: node core hiện rõ, toàn bộ sub theo decomposition và actor
   tương ứng. Vẽ mọi relation đã xác định có hai đầu thuộc tập node này:
   **core–sub và sub–sub**, đúng chiều và nhãn. Không thay core bằng tên package
   rồi bỏ node core, không chỉ vẽ các cạnh hình sao từ core xuống sub.
   Nếu cần UC dùng chung nằm ngoài nhóm, thêm node tham chiếu cùng ID để thấy
   quan hệ. Có thể thêm view phụ cho hình lớn nhưng không thay sơ đồ riêng bắt buộc.
3. Tổng quan hệ thống: đọc core của các module nguồn trong module-models,
   giữ ID/tên/owner, hợp nhất actor đúng vai trò. Chỉ core hiện trên hình này;
   không đưa sub vào hoặc tự tạo “UC tổng quan” khác với core nguồn.
4. Đối chiếu hai chiều: core module không thiếu trên tổng quan; sub không
   mồ côi trong chi tiết; sub dùng chung có cùng ID ở mọi view. Module thiếu
   phân tích không được nhận là hoàn tất tổng quan toàn hệ thống.
5. Boundary/association đúng; core–sub mapping không tự thành mũi tên UML.
   Cặp không có relation ghi kết luận bên dưới hình, không nối mũi tên giả.
   Mỗi view detail ghi focus=ID core, members=core và các sub/tham chiếu xuất hiện.
6. Xác minh renderer, chạy parser/render, kiểm hình và ghi QA theo diagram-rules.
   Không có renderer thì ghi chưa kiểm, không tuyên bố pass.
7. Đặt link từ từng module tới overview khi đã tồn tại, và từ overview về
   phân rã/đặc tả module. Chỉ cập nhật file ngoài scope nếu được yêu cầu.

Cập nhật tiến độ và trình cổng, báo số core/sub từng module và các view đã kiểm.
