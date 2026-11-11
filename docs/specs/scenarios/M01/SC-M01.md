# Kịch bản nghiệp vụ — M01 Authentication & Account

[Vietnamese Doc] — Tái kiểm 11/11/2026 — Skill scenarios v1.4.

**Phạm vi:** 6 nhóm UC chính, 19 UC con, 20 mapping của US-M01. Boundary là iShare; module nội bộ đều là SYSTEM. Đầu ra tập trung vào chức năng actor thực hiện hoàn chỉnh.

**Trạng thái:** Đang soạn để review. US chưa duyệt; 8 GAP nguồn và TBD/OPEN còn được giữ, không tự giải quyết bằng yêu cầu mới.

## 1. Baseline và dữ liệu

<!-- sc:document -->

| key | value |
|---|---|
| module | M01 |
| scope | ALL |
| skill_version | 1.4 |
| output_dir | docs/specs/scenarios/M01 |
| date | 2026-11-11 |
| status | Đang soạn |
| completed_steps | 1, 2, 3, 4 |
| approval_evidence | - |


**Nguồn thực sự sử dụng:** phiên bản tài liệu lấy từ metadata; skill_version không thay cho phiên bản US. SHA-256 nhận diện chính xác snapshot. Các FR liên module chỉ đọc phần phụ thuộc nêu trong cột vai trò.

| Path từ repo root | Version | Ngày | Trạng thái | SHA-256 | Vai trò |
|---|---|---|---|---|---|
| [docs/specs/fr/FR-M01.md](../../fr/FR-M01.md) | 1.10 | 2026-10-24 | Đã chốt | d53a66dded755b787687ff8b96de3c0e7e89d7a9d671145e63d44f33cb29178a | Yêu cầu sở hữu; toàn bộ 16 nhóm, 172 FR chi tiết, 47 BR |
| [docs/specs/us/US-M01.md](../../us/US-M01.md) | Không có version tài liệu riêng; skill 2.2 | 2026-10-29 | Chờ duyệt | 198b47c1ff90ca67c1c2122e840fa2c8d1ee5f2281690631977e66dcd3d3ef4e | Catalog, mapping, brief/spec/quan hệ/điểm mở rộng, AUT/RULE |
| [docs/specs/us/US-overview.md](../../us/US-overview.md) | 1.1 | 2026-11-02 | Chờ duyệt | c1d624b7036ea2c7a9968eaa46c482c04fa1a15e2554d536cdfc12f177e26e33 | Boundary và lựa chọn UC chính toàn hệ thống; không giới hạn catalog M01 |
| [docs/specs/fr/FR-M02.md](../../fr/FR-M02.md) | 1.6 | 2026-10-24 | Đã chốt | e86aca71e0415ee2e121a4fdc3628261be335e9d266fcf6e9654b2fdf3cd357e | Bio/Lớp/Khối/avatar ở bước 3 và hợp đồng định danh sửa hồ sơ |
| [docs/specs/fr/FR-M06.md](../../fr/FR-M06.md) | 1.5 | 2026-10-24 | Đã chốt | 63606046efb11356276a2c9180f53cadad76f83e2e86502ed00341d915e0b084 | FR-M06-05.10, BR-M06-20: xóa lịch sử trình duyệt khi đăng xuất |
| [docs/specs/fr/FR-M07.md](../../fr/FR-M07.md) | 1.5 | 2026-10-24 | Đã chốt | 05fb18237e049e3742d06c49b824e76e238c7587e7099b8dc4a84a2e1daf4f5b | Hàng đợi/email sự kiện/thử lại và thông báo nhắc tên |
| [docs/specs/fr/FR-M09.md](../../fr/FR-M09.md) | 1.2 | 2026-10-24 | Đã chốt | 8ad8ae5e148c6e446f4bfec7f6e74ba9566c54747a0eda37a3930e94ab96faea | Thời hạn/quyền chuyển khiếu nại và kết quả ban/vai trò |


Đối chiếu FR-M01 với bản làm việc chung: cùng nội dung byte/SHA-256. Register OPEN-008 xác nhận phần còn hoãn của TBD-M01-01. Nguồn phương pháp: [skill scenarios](../../../../.agent-instructions/skills/scenarios/SKILL.md); không dùng tài liệu mẫu làm nguồn tính năng.

### Actor và ký hiệu

<!-- sc:actors -->

| id | name | kind | source |
|---|---|---|---|
| ACT-001 | Guest — người chưa có phiên đăng nhập | human | FR-M01-01.01, FR-M01-04.01, FR-M01-05.01, FR-M01-09.01, FR-M01-11.01, FR-M01-15.01 |
| ACT-002 | User — người có phiên đăng nhập | human | FR-M01-03.09, FR-M01-07.01, FR-M01-08.01, FR-M01-10.01, FR-M01-14.11, FR-M01-16.01 |
| ACT-003 | Người dùng có vai trò Mod hoặc Admin trong phạm vi M01 | human | FR-M01-13.05, BR-M01-41, FR-M01-10.04 |
| ACT-004 | Dịch vụ xác thực Google | external-system | FR-M01-04.01, FR-M01-04.04, FR-M01-04.06, BR-M01-08 |
| ACT-005 | Dịch vụ gửi email bên ngoài | external-system | FR-M01-15.05, FR-M01-01.03, FR-M01-11.01, FR-M07-04.01, FR-M07-04.02 |


`SYSTEM` là Hệ thống iShare. Mỗi sự kiện có đúng một chủ thể; các sự kiện liền kề trong cùng đường đi phải khác chủ thể. Cùng con người có thể đổi từ ACT-001 sang ACT-002 sau khi có phiên; không coi đó là hai người khác nhau. Tác vụ tự động chỉ là quy tắc nền, không có BF/SC độc lập.

`at=Mk` trong bảng ngoại lệ nghĩa nhánh **thay thế** Mk. `next` trỏ chính xác đến bước tiếp theo hoặc kết quả END. SUCCESS là hoàn tất mục tiêu cụ thể; REJECTED là yêu cầu bị từ chối; CANCELLED là lựa chọn thoát/hủy; HANDED_OFF là chuyển đúng ngữ cảnh sang mục tiêu khác đã nêu, không tuyên bố mục tiêu bên nhận đã xong.

Dữ liệu ở các sự kiện chính là bộ dữ liệu của đường chuẩn. Khi guard ngoại lệ nêu dữ liệu sai/khác (ví dụ mật khẩu sai), thay giá trị đầu vào của chính lần gửi tương ứng bằng bộ dữ liệu đó; không đồng thời gửi bộ chuẩn và bộ lỗi. Nếu lựa chọn làm thay đổi hành động actor thì nhánh thay ngay bước actor đó và viết rõ hành động mới.

### Dữ liệu giả lập dùng chung

| Bộ | Giá trị cụ thể | Phạm vi/ý nghĩa |
|---|---|---|
| D-ACCOUNT | A01 email an.study@example.test, An_12A1, Minh An; A02 Google binh.study@example.test; A03 bị ban; A04 ADMIN | Mỗi SC là snapshot độc lập; A01 trong hai SC không bắt buộc cùng thời điểm/lịch sử |
| D-PASSWORD | Mật khẩu cũ "  Mật khẩu 2026  ", mới "mật khẩu mới 2026" | Giả lập, có khoảng trắng/chữ có dấu; không dùng mật khẩu thật; không trim |
| D-DEVICE | P01 điện thoại, L01 laptop có phiên độc lập; P02 thiết bị đặt lại mật khẩu | Đổi mật khẩu/logout/làm mới khác với đặt lại hoặc vô hiệu hóa về ảnh hưởng phiên khác |
| D-LINK | L1/L2 và Reset-L1/Reset-L2 là nhãn liên kết, không phải token thật | Link xác minh 1 giờ; đặt lại 15 phút; mới vô hiệu cũ; không dùng lại link đã dùng |
| D-OTP | 482731 hoặc 615204 là mã giả 6 chữ số | Hạn 15 phút, sai lần 5 vô hiệu, gửi lại cách ≥60 giây; không suy quy tắc link sang OTP |
| D-POLICY | P1.0 trước, P2.0 hiện hành; thời điểm minh họa 06/11/2026 09:00 +07 | Đây là giá trị minh họa, không khẳng định phiên bản chính sách thực tế đã phát hành |
| D-MENTION-G | D-MENTION-G: truy vấn "Lan"; G12 là Group bài. U201=Lan (đang theo dõi), U202=Lan Anh (đang theo dõi), U203=Lan Chi (cùng G12), U204=Lan Hương (chỉ chung G99, không G12), U205=Lan Mai (khác), U206=Hoàng Lan (khác). Thứ tự minh họa: U201,U202,U203,U204,U205; U206 ngoài top 5. U204/U205 được giả lập có độ khớp khác nhau để không tự đặt quy tắc phá hòa. U207=Lan cũ DEACTIVATED; U208=Lan xóa DELETED; U209=Lan khóa BANNED; U210=Lan mới EMAIL_VERIFIED đều bị loại. | Snapshot ngữ cảnh Group; điều kiện độ khớp là dữ liệu giả lập của kết quả tìm |
| D-MENTION-P | D-MENTION-P: truy vấn "Lan"; ngoài Group. U201=Lan và U202=Lan Anh đang theo dõi; U204=Lan Hương có chung G99 với người soạn; U203=Lan Chi không có Group chung trong snapshot này; U205=Lan Mai và U206=Hoàng Lan còn lại. Trả U201,U202,U204,U203,U205, tối đa 5. U203/U205 giả lập có độ khớp khác nhau; U207/U208/U209/U210 bị loại như D-MENTION-G. | Snapshot ngoài Group; bình luận lấy ngữ cảnh bài chứa nó |


Giá trị minh họa không tạo ràng buộc mới. Các mốc ngày/giờ đều theo Asia/Saigon (+07:00). “A×156” là chuỗi A lặp đúng 156 ký tự; là dữ liệu xác định, không phải chỗ trống chưa điền. Trường hợp cùng lỗi/kết quả nhưng nhiều giá trị biên dùng cùng nhánh; không ép đếm mỗi giá trị thành một UC mới.



## 2. Nhóm UC và cách bao phủ

<!-- sc:decomposition -->

| core | sub | source |
|---|---|---|
| UC-M01-020 | UC-M01-001 | FR-M01-01, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| UC-M01-020 | UC-M01-002 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-10, BR-M01-38 |
| UC-M01-020 | UC-M01-003 | FR-M01-03, BR-M01-05, BR-M01-06, BR-M01-08 |
| UC-M01-020 | UC-M01-004 | FR-M01-04.01, FR-M01-04.02, FR-M01-04.03, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, BR-M01-08 |
| UC-M01-020 | UC-M01-016 | FR-M01-02.04, FR-M01-02.05, FR-M01-02.07, BR-M01-11, BR-M01-38 |
| UC-M01-021 | UC-M01-005 | FR-M01-05, BR-M01-18, BR-M01-37 |
| UC-M01-021 | UC-M01-015 | FR-M01-04.04, FR-M01-04.06, FR-M01-04.08, FR-M01-04.11, BR-M01-09, BR-M01-18 |
| UC-M01-021 | UC-M01-006 | FR-M01-07, FR-M01-05.18, FR-M01-16.03, BR-M01-17 |
| UC-M01-021 | UC-M01-017 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33 |
| UC-M01-021 | UC-M01-018 | FR-M01-05.01, FR-M01-05.03, FR-M01-05.04, FR-M01-05.05, FR-M01-05.06, FR-M01-05.07, FR-M01-05.08, FR-M01-05.09, FR-M01-05.10, FR-M01-05.11, FR-M01-05.12, FR-M01-05.19, BR-M01-18, BR-M01-19, BR-M01-37 |
| UC-M01-022 | UC-M01-007 | FR-M01-08, BR-M01-14, BR-M01-15, BR-M01-31, BR-M01-35 |
| UC-M01-022 | UC-M01-008 | FR-M01-09, BR-M01-12, BR-M01-13, BR-M01-39 |
| UC-M01-022 | UC-M01-019 | FR-M01-09.02, FR-M01-09.03, FR-M01-09.04, FR-M01-09.05, FR-M01-09.06, FR-M01-09.08, FR-M01-09.09, FR-M01-09.10, FR-M01-09.11, FR-M01-09.12, FR-M01-09.16, BR-M01-12, BR-M01-13, BR-M01-35, BR-M01-38, BR-M01-39 |
| UC-M01-023 | UC-M01-009 | FR-M01-10, BR-M01-20, BR-M01-21, BR-M01-45 |
| UC-M01-023 | UC-M01-010 | FR-M01-11, BR-M01-22, BR-M01-25 |
| UC-M01-023 | UC-M01-011 | FR-M01-13.05, BR-M01-41 |
| UC-M01-024 | UC-M01-013 | FR-M01-15, BR-M01-42, BR-M01-43, BR-M01-46 |
| UC-M01-024 | UC-M01-014 | FR-M01-16, BR-M01-44, BR-M01-45 |
| UC-M01-024 | UC-M01-009 | FR-M01-10, BR-M01-20, BR-M01-21, BR-M01-45 |
| UC-M01-025 | UC-M01-012 | FR-M01-14, BR-M01-26, BR-M01-27, BR-M01-28, BR-M01-29, BR-M01-40 |


<!-- sc:ucs -->

| id | treatment | scenarios | coverage | rationale | sources |
|---|---|---|---|---|---|
| UC-M01-020 | abstract | SC-M01-001 | SC-M01-001/M4, SC-M01-001/M7, SC-M01-001/E27.4, SC-M01-001/E27.7, SC-M01-001/E28.4, SC-M01-001/E28.7, SC-M01-001/E29.4, SC-M01-001/E29.7 | Hợp đồng đăng ký, bao phủ bằng hành trình cụ thể. | FR-M01-01, FR-M01-02, FR-M01-03, FR-M01-04, BR-M01-02, BR-M01-03, BR-M01-08 |
| UC-M01-021 | aggregate | SC-M01-007, SC-M01-014, SC-M01-039 | SC-M01-007/M1, SC-M01-007/M2, SC-M01-007/E3.1, SC-M01-007/E6.1, SC-M01-007/E6.2, SC-M01-007/E7.1, SC-M01-007/E8.1, SC-M01-007/E9.1, SC-M01-014/E1.1, SC-M01-014/E1.2, SC-M01-014/M1, SC-M01-014/M2, SC-M01-014/E2.1, SC-M01-014/E2.2, SC-M01-039/E1.6 | Nhóm chức năng độc lập, không ép chạy nối tiếp. | FR-M01-04, FR-M01-05, FR-M01-06, FR-M01-07 |
| UC-M01-022 | aggregate | SC-M01-017, SC-M01-018 | SC-M01-017/M1, SC-M01-017/M2, SC-M01-017/E1.1, SC-M01-017/E2.1, SC-M01-017/E3.1, SC-M01-017/E4.1, SC-M01-017/E5.1, SC-M01-017/E6.1, SC-M01-018/M4, SC-M01-018/E10.4, SC-M01-018/E7.1, SC-M01-018/E8.1, SC-M01-018/E9.1, SC-M01-018/E17.2, SC-M01-018/E18.2, SC-M01-018/E19.2 | Nhóm chức năng độc lập, không ép chạy nối tiếp. | FR-M01-08, FR-M01-09, BR-M01-13, BR-M01-14, BR-M01-15 |
| UC-M01-023 | aggregate | SC-M01-007, SC-M01-022, SC-M01-023, SC-M01-025, SC-M01-039 | SC-M01-007/E54.4, SC-M01-007/E59.4, SC-M01-007/E70.4, SC-M01-007/E81.4, SC-M01-007/E92.4, SC-M01-007/E97.4, SC-M01-007/E103.4, SC-M01-007/E109.6, SC-M01-022/M2, SC-M01-022/M1, SC-M01-022/E1.1, SC-M01-022/E2.1, SC-M01-022/E3.1, SC-M01-023/E2.1, SC-M01-023/E8.4, SC-M01-023/M1, SC-M01-023/M2, SC-M01-023/E4.2, SC-M01-023/E4.3, SC-M01-023/E5.2, SC-M01-023/E5.3, SC-M01-025/E1.1, SC-M01-025/E2.1, SC-M01-025/M1, SC-M01-025/M2, SC-M01-039/E2.6, SC-M01-039/E3.6 | Nhóm chức năng độc lập, không ép chạy nối tiếp. | FR-M01-10, FR-M01-11, FR-M01-12, FR-M01-13, BR-M01-20, BR-M01-21 |
| UC-M01-024 | aggregate | SC-M01-007, SC-M01-022, SC-M01-037, SC-M01-039 | SC-M01-007/E108.4, SC-M01-007/E108.6, SC-M01-007/E109.4, SC-M01-007/E109.6, SC-M01-007/E107.2, SC-M01-007/E107.4, SC-M01-007/E108.2, SC-M01-007/E109.2, SC-M01-022/M1, SC-M01-022/M2, SC-M01-037/M2, SC-M01-037/E1.2, SC-M01-037/M1, SC-M01-037/E1.1, SC-M01-039/E1.4, SC-M01-039/E1.6, SC-M01-039/E2.4, SC-M01-039/E2.6, SC-M01-039/E3.4, SC-M01-039/E3.6, SC-M01-039/M2, SC-M01-039/M4 | Nhóm chức năng độc lập, không ép chạy nối tiếp. | FR-M01-15, FR-M01-16, BR-M01-44, BR-M01-45 |
| UC-M01-025 | scenario | SC-M01-034 | SC-M01-034/M2, SC-M01-034/M4, SC-M01-034/E1.2, SC-M01-034/E2.2, SC-M01-034/E2.4, SC-M01-034/E5.2, SC-M01-034/E5.4, SC-M01-034/E8.2 | Actor chủ động thực hiện chức năng đến kết quả. | FR-M01-14, BR-M01-28, BR-M01-29, BR-M01-30 |
| UC-M01-001 | scenario | SC-M01-001 | SC-M01-001/M4, SC-M01-001/M7, SC-M01-001/E27.4, SC-M01-001/E27.7, SC-M01-001/E28.4, SC-M01-001/E28.7, SC-M01-001/E29.4, SC-M01-001/E29.7 | Actor chủ động thực hiện chức năng đến kết quả. | FR-M01-01, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| UC-M01-002 | embedded | SC-M01-001, SC-M01-007 | SC-M01-001/M5, SC-M01-001/M6, SC-M01-001/E8.4, SC-M01-001/E9.4, SC-M01-001/E27.5, SC-M01-001/E27.6, SC-M01-001/E28.5, SC-M01-001/E28.6, SC-M01-007/E6.3, SC-M01-007/E6.4, SC-M01-007/E12.3, SC-M01-007/E12.7, SC-M01-007/E12.8, SC-M01-007/E13.3, SC-M01-007/E13.7, SC-M01-007/E13.8 | Thực hiện trong hành trình bao chứa; không tách bước hỗ trợ/phương thức thành BF. | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-10, BR-M01-38 |
| UC-M01-003 | embedded | SC-M01-001, SC-M01-007 | SC-M01-001/M8, SC-M01-001/E11.1, SC-M01-001/E11.2, SC-M01-001/E12.1, SC-M01-001/E12.2, SC-M01-001/E13.1, SC-M01-001/E13.2, SC-M01-001/E14.1, SC-M01-007/E6.6, SC-M01-007/E12.10, SC-M01-007/E13.10, SC-M01-007/E15.6, SC-M01-007/E15.7, SC-M01-007/E15.8, SC-M01-007/E16.6, SC-M01-007/E16.7 | Thực hiện trong hành trình bao chứa; không tách bước hỗ trợ/phương thức thành BF. | FR-M01-03, BR-M01-05, BR-M01-06, BR-M01-08 |
| UC-M01-004 | embedded | SC-M01-001 | SC-M01-001/E16.6, SC-M01-001/E16.7, SC-M01-001/E21.8, SC-M01-001/E21.9, SC-M01-001/E22.6, SC-M01-001/E22.7, SC-M01-001/E23.6, SC-M01-001/E23.7 | Thực hiện trong hành trình bao chứa; không tách bước hỗ trợ/phương thức thành BF. | FR-M01-04.01, FR-M01-04.02, FR-M01-04.03, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, BR-M01-08 |
| UC-M01-005 | scenario | SC-M01-007 | SC-M01-007/M2, SC-M01-007/E3.1, SC-M01-007/E4.1, SC-M01-007/E6.2, SC-M01-007/E9.2, SC-M01-007/E10.2, SC-M01-007/E12.2, SC-M01-007/E13.2 | Actor chủ động thực hiện chức năng đến kết quả. | FR-M01-05, BR-M01-18, BR-M01-37 |
| UC-M01-006 | scenario | SC-M01-007, SC-M01-014, SC-M01-039 | SC-M01-007/M2, SC-M01-007/E44.2, SC-M01-007/E52.4, SC-M01-007/E90.4, SC-M01-007/E101.4, SC-M01-007/E107.2, SC-M01-007/E108.2, SC-M01-007/E109.2, SC-M01-014/M1, SC-M01-014/M2, SC-M01-014/E1.1, SC-M01-014/E1.2, SC-M01-014/E2.1, SC-M01-014/E2.2, SC-M01-039/E1.3, SC-M01-039/E1.4, SC-M01-039/E1.5, SC-M01-039/E1.6, SC-M01-039/E2.3, SC-M01-039/E2.4, SC-M01-039/E2.5, SC-M01-039/E2.6 | Actor chủ động thực hiện chức năng đến kết quả. | FR-M01-07, FR-M01-05.18, FR-M01-16.03, BR-M01-17 |
| UC-M01-007 | scenario | SC-M01-017 | SC-M01-017/M1, SC-M01-017/M2, SC-M01-017/E1.1, SC-M01-017/E2.1, SC-M01-017/E3.1, SC-M01-017/E4.1, SC-M01-017/E5.1, SC-M01-017/E6.1 | Actor chủ động thực hiện chức năng đến kết quả. | FR-M01-08, BR-M01-14, BR-M01-15, BR-M01-31, BR-M01-35 |
| UC-M01-008 | scenario | SC-M01-018 | SC-M01-018/M2, SC-M01-018/M4, SC-M01-018/E7.1, SC-M01-018/E8.1, SC-M01-018/E9.1, SC-M01-018/E10.2, SC-M01-018/E10.4, SC-M01-018/E11.2 | Actor chủ động thực hiện chức năng đến kết quả. | FR-M01-09, BR-M01-12, BR-M01-13, BR-M01-39 |
| UC-M01-009 | scenario | SC-M01-007, SC-M01-022, SC-M01-039 | SC-M01-007/E108.4, SC-M01-007/E108.6, SC-M01-007/E109.4, SC-M01-007/E109.6, SC-M01-007/E54.4, SC-M01-007/E59.4, SC-M01-007/E70.4, SC-M01-007/E81.4, SC-M01-022/M1, SC-M01-022/M2, SC-M01-022/E1.1, SC-M01-022/E2.1, SC-M01-022/E3.1, SC-M01-039/E1.4, SC-M01-039/E1.6, SC-M01-039/E2.4, SC-M01-039/E2.6, SC-M01-039/E3.4, SC-M01-039/E3.6 | Actor chủ động thực hiện chức năng đến kết quả. | FR-M01-10, BR-M01-20, BR-M01-21, BR-M01-45 |
| UC-M01-010 | scenario | SC-M01-023 | SC-M01-023/M4, SC-M01-023/E6.4, SC-M01-023/E9.6, SC-M01-023/E10.8, SC-M01-023/E11.8, SC-M01-023/E12.6, SC-M01-023/M2, SC-M01-023/E3.1 | Actor chủ động thực hiện chức năng đến kết quả. | FR-M01-11, BR-M01-22, BR-M01-25 |
| UC-M01-011 | scenario | SC-M01-025 | SC-M01-025/M2, SC-M01-025/E1.1, SC-M01-025/E2.1, SC-M01-025/M1 | Actor chủ động thực hiện chức năng đến kết quả. | FR-M01-13.05, BR-M01-41 |
| UC-M01-012 | embedded | SC-M01-034 | SC-M01-034/M2, SC-M01-034/E2.2, SC-M01-034/E5.2, SC-M01-034/E8.2, SC-M01-034/E11.2, SC-M01-034/E4.2, SC-M01-034/E7.2, SC-M01-034/E10.2 | Thực hiện trong hành trình bao chứa; không tách bước hỗ trợ/phương thức thành BF. | FR-M01-14, BR-M01-26, BR-M01-27, BR-M01-28, BR-M01-29, BR-M01-40 |
| UC-M01-013 | scenario | SC-M01-037 | SC-M01-037/M2, SC-M01-037/E1.2, SC-M01-037/M1, SC-M01-037/E1.1 | Actor chủ động thực hiện chức năng đến kết quả. | FR-M01-15, BR-M01-42, BR-M01-43, BR-M01-46 |
| UC-M01-014 | scenario | SC-M01-007, SC-M01-039 | SC-M01-007/E108.4, SC-M01-007/E108.6, SC-M01-007/E109.4, SC-M01-007/E109.6, SC-M01-007/E107.2, SC-M01-007/E107.4, SC-M01-007/E108.2, SC-M01-007/E109.2, SC-M01-039/E1.4, SC-M01-039/E1.6, SC-M01-039/E2.4, SC-M01-039/E2.6, SC-M01-039/E3.4, SC-M01-039/E3.6, SC-M01-039/M2, SC-M01-039/M4 | Actor chủ động thực hiện chức năng đến kết quả. | FR-M01-16, BR-M01-44, BR-M01-45 |
| UC-M01-015 | embedded | SC-M01-007 | SC-M01-007/E68.4, SC-M01-007/E73.4, SC-M01-007/E74.4, SC-M01-007/E75.4, SC-M01-007/E76.4, SC-M01-007/E77.4, SC-M01-007/E78.4, SC-M01-007/E79.4 | Thực hiện trong hành trình bao chứa; không tách bước hỗ trợ/phương thức thành BF. | FR-M01-04.04, FR-M01-04.06, FR-M01-04.08, FR-M01-04.11, BR-M01-09, BR-M01-18 |
| UC-M01-016 | embedded | SC-M01-001, SC-M01-007 | SC-M01-001/E8.1, SC-M01-001/E8.3, SC-M01-001/E9.1, SC-M01-001/E9.3, SC-M01-001/E38.6, SC-M01-001/E41.6, SC-M01-001/E42.6, SC-M01-001/E42.8, SC-M01-007/E12.4, SC-M01-007/E12.6, SC-M01-007/E13.4, SC-M01-007/E13.6, SC-M01-007/E6.4, SC-M01-007/E12.8, SC-M01-007/E13.8, SC-M01-007/E14.4 | Thực hiện trong hành trình bao chứa; không tách bước hỗ trợ/phương thức thành BF. | FR-M01-02.04, FR-M01-02.05, FR-M01-02.07, BR-M01-11, BR-M01-38 |
| UC-M01-017 | embedded | SC-M01-007 | SC-M01-007/E68.4, SC-M01-007/E73.4, SC-M01-007/E74.4, SC-M01-007/E75.4, SC-M01-007/E76.4, SC-M01-007/E77.4, SC-M01-007/E78.4, SC-M01-007/E79.4 | Thực hiện trong hành trình bao chứa; không tách bước hỗ trợ/phương thức thành BF. | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33 |
| UC-M01-018 | embedded | SC-M01-007 | SC-M01-007/M1, SC-M01-007/M2, SC-M01-007/E3.1, SC-M01-007/E6.1, SC-M01-007/E6.2, SC-M01-007/E7.1, SC-M01-007/E8.1, SC-M01-007/E9.1 | Thực hiện trong hành trình bao chứa; không tách bước hỗ trợ/phương thức thành BF. | FR-M01-05.01, FR-M01-05.03, FR-M01-05.04, FR-M01-05.05, FR-M01-05.06, FR-M01-05.07, FR-M01-05.08, FR-M01-05.09, FR-M01-05.10, FR-M01-05.11, FR-M01-05.12, FR-M01-05.19, BR-M01-18, BR-M01-19, BR-M01-37 |
| UC-M01-019 | embedded | SC-M01-018 | SC-M01-018/E1.1, SC-M01-018/E11.4, SC-M01-018/E2.1, SC-M01-018/E12.4, SC-M01-018/M2, SC-M01-018/M4, SC-M01-018/E3.1, SC-M01-018/E4.1 | Thực hiện trong hành trình bao chứa; không tách bước hỗ trợ/phương thức thành BF. | FR-M01-09.02, FR-M01-09.03, FR-M01-09.04, FR-M01-09.05, FR-M01-09.06, FR-M01-09.08, FR-M01-09.09, FR-M01-09.10, FR-M01-09.11, FR-M01-09.12, FR-M01-09.16, BR-M01-12, BR-M01-13, BR-M01-35, BR-M01-38, BR-M01-39 |


## 3. Danh mục luồng hoàn chỉnh

Các ID còn giữ là ID đại diện của bản trước; ID được gộp không tái sử dụng cho mục tiêu khác. covered_ucs ghi bao phủ, không thêm quan hệ UML.

<!-- sc:flows -->

| id | uc | primary | trigger | goal | completion | covered_ucs | rationale | scenario | sources |
|---|---|---|---|---|---|---|---|---|---|
| BF-M01-001 | UC-M01-001 | ACT-001 | Guest bắt đầu đăng ký bằng email | Đăng ký và hoàn tất tài khoản iShare | A01 ACTIVE/USER/SETUP_COMPLETED, email đã xác minh, định danh hợp lệ và bản ghi đồng ý P2.0 được lưu. Bio/Lớp-Khối/avatar không bắt buộc. | UC-M01-001, UC-M01-002, UC-M01-003, UC-M01-004, UC-M01-016 | Actor yêu cầu chức năng này độc lập; luồng đi đến kết quả, các phương thức/trạng thái chỉ là nhánh. | SC-M01-001 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.05, FR-M01-01.07, FR-M01-01.06, FR-M01-01.09, BR-M01-33, BR-M01-37, FR-M01-15.01, FR-M01-15.02, FR-M01-15.03, FR-M01-15.04, FR-M01-15.05, FR-M01-15.06, FR-M01-15.07, FR-M01-15.08, FR-M01-15.09, BR-M01-42, BR-M01-43, BR-M01-44, BR-M01-45, BR-M01-46, FR-M01-02.07, FR-M01-02.04, FR-M01-02.05, FR-M01-03.04, FR-M01-04.01, FR-M01-04.07, FR-M01-04.12, FR-M01-04.13, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, BR-M01-08, FR-M01-04.11, FR-M01-04.04, FR-M01-04.06, BR-M01-09, FR-M01-03.03, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-03.09, FR-M02-04.03, FR-M02-04.04, BR-M01-11 |
| BF-M01-007 | UC-M01-005 | ACT-001 | Guest gửi email và mật khẩu để đăng nhập | Đăng nhập và hoàn tất điều kiện để truy cập iShare | Actor nhận quyền truy cập đúng tài khoản/vai trò sau kiểm trạng thái, mức xác minh và chính sách. Nếu đăng ký còn dở, đã xác minh/thiết lập đến SETUP_COMPLETED. Nhánh rút đồng ý bằng vô hiệu hóa kết thúc DEACTIVATED và mọi phiên, không cho truy cập. Snapshot tài khoản và hiệu ứng cụ thể ghi tại từng nhánh; ADMIN không cấp quyền tương tự cho MOD. | UC-M01-002, UC-M01-003, UC-M01-005, UC-M01-006, UC-M01-009, UC-M01-014, UC-M01-015, UC-M01-016, UC-M01-017, UC-M01-018 | Actor yêu cầu chức năng này độc lập; luồng đi đến kết quả, các phương thức/trạng thái chỉ là nhánh. | SC-M01-007 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.12, BR-M01-16, BR-M01-17, BR-M01-18, FR-M01-05.13, BR-M01-15, FR-M01-05.04, FR-M01-05.03, FR-M01-12.04, FR-M01-05.19, BR-M01-37, FR-M01-05.10, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, BR-M01-02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-02.07, FR-M01-02.04, FR-M01-02.05, FR-M01-03.04, FR-M01-05.11, FR-M01-03.03, FR-M01-01.09, BR-M01-33, FR-M01-03.09, FR-M01-05.05, FR-M01-05.06, FR-M01-05.07, FR-M01-05.08, BR-M01-19, BR-M09-04, BR-M09-07, FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, FR-M06-05.10, BR-M06-20, FR-M01-05.09, FR-M09-01.05, BR-M09-08, FR-M01-04.06, FR-M01-04.04, FR-M01-04.08, FR-M01-12.06, FR-M01-12.08, BR-M01-21, FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08, FR-M01-04.09, FR-M01-04.05, FR-M01-04.11, BR-M01-09, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-03.08, FR-M01-16.01, BR-M01-44, FR-M01-16.02, FR-M01-16.03, BR-M01-45, FR-M01-16.04, FR-M01-10.01, FR-M01-10.02, FR-M01-10.07, FR-M01-13.01, FR-M01-13.03 |
| BF-M01-014 | UC-M01-006 | ACT-002 | Người dùng chọn Đăng xuất | Đăng xuất chủ động trên thiết bị hiện tại | Phiên P01 chấm dứt, lịch sử trình duyệt P01 rỗng, L01 không bị đăng xuất; trạng thái tài khoản và bản ghi đồng ý không tự đổi. | UC-M01-006 | Actor yêu cầu chức năng này độc lập; luồng đi đến kết quả, các phương thức/trạng thái chỉ là nhánh. | SC-M01-014 | FR-M01-07.01, FR-M01-07.02, BR-M01-17, FR-M06-05.10, BR-M06-20, FR-M01-05.07, FR-M01-05.18, BR-M01-19, FR-M01-16.03, FR-M01-16.04, BR-M01-45 |
| BF-M01-017 | UC-M01-007 | ACT-002 | Chủ tài khoản gửi mật khẩu cũ, mới và nhập lại | Đổi mật khẩu khi đã đăng nhập | Mật khẩu mới có hiệu lực, L01 vẫn giữ phiên; thông báo trong ứng dụng được ghi nhận và email sự kiện được xếp gửi bất đồng bộ qua M07. | UC-M01-007 | Actor yêu cầu chức năng này độc lập; luồng đi đến kết quả, các phương thức/trạng thái chỉ là nhánh. | SC-M01-017 | FR-M01-08.01, BR-M01-14, BR-M01-35, FR-M01-08.04, FR-M01-08.05, BR-M01-31, BR-M01-36, FR-M07-04.01, FR-M07-04.02, FR-M07-04.03, FR-M07-04.09, FR-M07-04.10, BR-M07-11, BR-M07-26, FR-M01-08.02, FR-M01-08.03, FR-M01-08.08, FR-M01-08.09, FR-M01-08.07, FR-M01-08.06, FR-M01-08.10, FR-M01-05.20, BR-M01-37 |
| BF-M01-018 | UC-M01-008 | ACT-001 | Guest gửi email ở chức năng Quên mật khẩu | Lấy lại mật khẩu tài khoản email ACTIVE | Mật khẩu mới hợp lệ được lưu, link mất hiệu lực, mọi phiên cũ kết thúc; P02 nhận phiên mới theo trạng thái. ACTIVE/SETUP_COMPLETED vào ứng dụng; BANNED chỉ nhận phiên hạn chế, không được mở khóa. Thông báo đổi mật khẩu được ghi nhận theo M07. | UC-M01-008, UC-M01-019 | Actor yêu cầu chức năng này độc lập; luồng đi đến kết quả, các phương thức/trạng thái chỉ là nhánh. | SC-M01-018 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39, FR-M01-09.02, FR-M01-09.03, FR-M01-09.04, FR-M01-09.12, FR-M01-09.16, BR-M01-13, BR-M01-35, FR-M07-04.01, FR-M07-04.02, FR-M07-04.03, FR-M07-04.09, FR-M07-04.10, BR-M07-11, BR-M07-26, FR-M01-09.05, FR-M01-09.10, FR-M01-09.06, FR-M01-09.08, FR-M01-09.09, BR-M01-15, FR-M01-09.07, FR-M01-09.15 |
| BF-M01-022 | UC-M01-009 | ACT-002 | Chủ tài khoản chọn Vô hiệu hóa trực tiếp hoặc sau khi từ chối chính sách | Vô hiệu hóa tài khoản của chính mình | A01 DEACTIVATED; mọi phiên kết thúc; nội dung/danh tính hiển thị theo trạng thái. Trong cửa sổ được kích hoạt lại; tại hạn cuối có AUT-M01-002, cảnh báo trước 24 giờ theo AUT-M01-003. | UC-M01-009 | Actor yêu cầu chức năng này độc lập; luồng đi đến kết quả, các phương thức/trạng thái chỉ là nhánh. | SC-M01-022 | FR-M01-10.01, FR-M01-10.03, BR-M01-20, BR-M01-45, FR-M01-10.02, FR-M01-10.07, FR-M01-13.01, FR-M01-13.02, FR-M01-13.03, FR-M01-13.07, BR-M01-21, BR-M01-23, FR-M01-10.04, FR-M01-10.05, FR-M01-10.06, FR-M01-05.20, BR-M01-37 |
| BF-M01-023 | UC-M01-010 | ACT-001 | Chủ tài khoản DEACTIVATED yêu cầu mã kích hoạt tại trang kích hoạt | Kích hoạt lại tài khoản bằng mã email | A01 ACTIVE, bài/bình luận hiển thị trở lại đúng danh tính còn lưu; P01 được đăng nhập bằng phiên mới. Quyền dùng tiếp vẫn chịu trạng thái, mức xác minh và phiên bản chính sách. | UC-M01-010 | Actor yêu cầu chức năng này độc lập; luồng đi đến kết quả, các phương thức/trạng thái chỉ là nhánh. | SC-M01-023 | FR-M01-11.01, FR-M01-11.09, BR-M01-22, FR-M01-11.02, FR-M01-11.03, FR-M01-11.04, FR-M01-11.05, FR-M01-11.06, FR-M01-11.07, FR-M01-11.08, BR-M01-25, FR-M01-11.10, FR-M01-12.01, FR-M01-12.04, BR-M01-21 |
| BF-M01-025 | UC-M01-011 | ACT-003 | Người kiểm duyệt mở bài của tác giả vô hiệu hóa | Mod/Admin xem bài ẩn và danh tính tác giả DEACTIVATED | ACT-003 xem được bài/danh tính thật trong giới hạn DEACTIVATED; người xem thông thường vẫn theo cách hiển thị thay thế. | UC-M01-011 | Actor yêu cầu chức năng này độc lập; luồng đi đến kết quả, các phương thức/trạng thái chỉ là nhánh. | SC-M01-025 | FR-M01-13.05, BR-M01-41, FR-M01-13.01, FR-M01-13.02, FR-M01-12.08, FR-M01-12.10, BR-M01-47, BR-M01-23, BR-M01-24 |
| BF-M01-034 | UC-M01-025 | ACT-002 | Người có phiên quyết định nhắc người khác trong bài/bình luận | Nhắc một tài khoản trong nội dung đang soạn | Mục tiêu UC-M01-025 hoàn tất tại bản soạn có tham chiếu đúng tài khoản được chọn: U203 trong luồng chính, U202 trong lựa chọn thay thế; công khai nội dung sau này kích hoạt AUT-M01-005. | UC-M01-012, UC-M01-025 | Actor yêu cầu chức năng này độc lập; luồng đi đến kết quả, các phương thức/trạng thái chỉ là nhánh. | SC-M01-034 | FR-M01-14.01, FR-M01-14.02, FR-M01-14.03, FR-M01-14.04, FR-M01-14.05, FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.12, FR-M01-14.13, FR-M01-14.14, BR-M01-26, BR-M01-27, BR-M01-28, BR-M01-29, BR-M01-40, FR-M01-14.10, BR-M01-30, FR-M01-14.09, FR-M01-14.11 |
| BF-M01-037 | UC-M01-013 | ACT-001 | Người xem mở trang hoặc liên kết Privacy Policy/ToS | Xem trang chính sách công khai | Trang hiện đúng phiên bản, đủ các nhóm/mục cần có. Việc đọc không tự tạo bản ghi đồng ý; nếu từ đăng ký, trở về đúng điểm đồng ý mà chưa tự gửi đăng ký. | UC-M01-013 | Actor yêu cầu chức năng này độc lập; luồng đi đến kết quả, các phương thức/trạng thái chỉ là nhánh. | SC-M01-037 | FR-M01-15.01, FR-M01-01.04, BR-M01-03, FR-M01-15.02, FR-M01-15.03, FR-M01-15.04, FR-M01-15.05, FR-M01-15.06, FR-M01-15.07, FR-M01-15.08, FR-M01-15.09, BR-M01-42, BR-M01-43, BR-M01-44, BR-M01-45, BR-M01-46, FR-M01-01.05, FR-M01-01.13, FR-M01-01.14 |
| BF-M01-039 | UC-M01-014 | ACT-002 | Người có phiên mở ứng dụng; hệ thống so phiên bản chính sách | Đồng ý phiên bản chính sách mới | Nếu đồng ý P2.0: lưu phiên bản/thời điểm và cho dùng tiếp trong quyền hiện có. Nếu bản hiện hành đã đồng ý: không hỏi/ghi lại. Nếu từ chối rồi chọn vô hiệu hóa hợp lệ: chuyển DEACTIVATED, kết thúc mọi phiên, không ghi đồng ý P2.0; đây là kết quả rút đồng ý của nhánh, không phải đồng ý thành công. | UC-M01-006, UC-M01-009, UC-M01-014 | Actor yêu cầu chức năng này độc lập; luồng đi đến kết quả, các phương thức/trạng thái chỉ là nhánh. | SC-M01-039 | FR-M01-16.01, BR-M01-44, FR-M01-16.02, FR-M01-16.03, BR-M01-45, FR-M01-07.01, FR-M01-07.02, FR-M01-16.04, FR-M06-05.10, FR-M01-10.01, FR-M01-10.02, FR-M01-10.07, FR-M01-13.01, FR-M01-13.03, BR-M01-21, FR-M01-10.04, FR-M01-10.05, FR-M01-10.06, FR-M01-16.05 |


Đăng ký gồm tạo → xác minh (email) → thiết lập xong; Google là phương thức thay thế. Đăng nhập gồm xác thực/cổng → tiếp tục bước đăng ký còn dở nếu cần → kết quả truy cập theo quyền. Lấy lại mật khẩu đi đến thay mật khẩu và phiên mới. Nhắc tên hoàn tất chèn khối vào bản soạn; công khai bài/bình luận thuộc M03/M04, thông báo là hiệu ứng khi công khai. Đọc chính sách hoàn tất khi nội dung được trả; đồng ý lại hoàn tất khi quyết định được xử lý.

## 4. Các scenario

<!-- sc:scenario SC-M01-001 -->

<a id="sc-m01-001"></a>

### SC-M01-001 — Đăng ký và hoàn tất tài khoản iShare

#### 1. Tên kịch bản chuẩn

**Đăng ký và hoàn tất tài khoản iShare** — BF-M01-001; UC owner: [UC-M01-001](../../us/US-M01.md#uc-m01-001); nhóm chi tiết: UC-M01-020. Trigger: Guest bắt đầu đăng ký bằng email.

#### 2. Actor thực hiện

ACT-001 Guest ở bước tạo/xác minh; cùng con người chuyển ngữ cảnh ACT-002 khi thao tác bước 3 có phiên hợp lệ; ACT-005 hỗ trợ email theo hợp đồng gửi. ACT-004 hỗ trợ phương thức đăng ký Google.

#### 3. Tiền điều kiện

Chưa có phiên trên thiết bị P01. Dữ liệu đường chuẩn: email chưa dùng; bảo trì/tạm dừng tạo mới tắt. Các điều kiện này được kiểm trong M4, không loại trừ các nhánh từ chối. Người này tiếp tục đăng ký tại bước 2/3 trong đúng ngữ cảnh tài khoản A01; GAP-SC-M01-001 ghi nhận việc nguồn chưa chỉ rõ lúc cấp phiên chuyển tiếp.

#### 4. Hậu điều kiện

<!-- sc:post SC-M01-001 -->

| result | condition |
|---|---|
| SUCCESS | A01 ACTIVE/USER/SETUP_COMPLETED, email đã xác minh, định danh hợp lệ và bản ghi đồng ý P2.0 được lưu. Bio/Lớp-Khối/avatar không bắt buộc. |
| REJECTED | Nếu từ chối tại bước tạo: không có tài khoản mới. Nếu từ chối link đã dùng: giữ mức xác minh hiện có, không hạ mức dù tài khoản có thể đã tiến xa hơn. Nếu lỗi thiết lập: chưa SETUP_COMPLETED và giữ tiến độ đã đạt; không vượt bước. |
| HANDED_OFF | Email Google đã thuộc tài khoản có sẵn: không tạo tài khoản thứ hai, chuyển mục tiêu sang đăng nhập SC-M01-007; không coi đăng ký mới thành công. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M01-001 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | M2 | FR-M01-01.01 |
| M2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | M3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| M3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | M4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| M4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | M5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| M5 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | M6 | FR-M01-02.01, BR-M01-10 |
| M6 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | M7 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| M7 | ACT-002 | Chủ tài khoản nhập username/display_name và bỏ qua ba trường tùy chọn rồi gửi. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | M8 | FR-M01-03.01, FR-M01-03.02, BR-M01-02 |
| M8 | SYSTEM | Hệ thống kiểm tên, trim display_name, lưu định danh đúng quy tắc và chuyển mức xác minh sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 ACTIVE/USER/SETUP_COMPLETED; display_name là tên chính, username giữ đúng An_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


#### 6. Các ngoại lệ

<!-- sc:exceptions SC-M01-001 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M4 | Không đánh dấu đồng ý chính sách | E1.1 | FR-M01-01.05 |
| E2 | system | M4 | Thiếu email hoặc mật khẩu | E2.1 | FR-M01-01.07 |
| E3 | system | M4 | Email đã thuộc tài khoản khác | E3.1 | FR-M01-01.06, BR-M01-04 |
| E4 | system | M4 | Mật khẩu dưới 8 hoặc trên 64 ký tự | E4.1 | FR-M01-01.10, BR-M01-35 |
| E5 | system | M4 | Công tắc tạm dừng đăng ký bật | E5.1 | FR-M01-01.08, FR-M01-01.09, BR-M01-33 |
| E6 | system | M4 | Chế độ bảo trì bật | E6.1 | FR-M01-01.12, BR-M01-37 |
| E7 | user-choice | M3 | Guest chọn đọc chính sách trước khi gửi đăng ký | E7.1 | FR-M01-01.04, FR-M01-15.01, FR-M01-15.02, FR-M01-15.03, FR-M01-15.04, FR-M01-15.05, FR-M01-15.06, FR-M01-15.07, FR-M01-15.08, FR-M01-15.09, BR-M01-42, BR-M01-43, BR-M01-44, BR-M01-45, BR-M01-46, FR-M01-01.01, FR-M01-01.13, BR-M01-03 |
| E8 | system | M6 | Link xác minh quá 1 giờ | E8.1 | FR-M01-02.03, FR-M01-02.06, FR-M01-02.07, BR-M01-38, FR-M01-02.04, FR-M01-02.05, FR-M01-02.01 |
| E9 | system | M6 | Link xác minh bị thay bởi lần gửi mới | E9.1 | FR-M01-02.03, FR-M01-02.06, FR-M01-02.07, BR-M01-38, FR-M01-02.04, FR-M01-02.05, FR-M01-02.01 |
| E10 | system | M6 | Link xác minh đã được dùng trước lần mở này | E10.1 | FR-M01-02.06, BR-M01-38 |
| E11 | system | M8 | Thiếu username hoặc display_name | E11.1 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E12 | system | M8 | Username ngoài độ dài hoặc tập ký tự cho phép | E12.1 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E13 | system | M8 | Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED | E13.1 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E14 | system | M8 | Display_name sau trim rỗng hoặc quá 50 ký tự | E14.1 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E15 | system | M8 | Display_name chứa ký tự không được nhận | E15.1 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E16 | user-choice | M1 | Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công | E16.1 | FR-M01-04.01, FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-04.13, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, FR-M01-01.02, FR-M01-01.12, BR-M01-01, BR-M01-08, FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |
| E17 | user-choice | M1 | Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Guest không đánh dấu đồng ý | E17.1 | FR-M01-04.01, FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-04.13 |
| E18 | user-choice | M1 | Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Tạm dừng tạo tài khoản mới bật | E18.1 | FR-M01-04.01, FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-04.13, FR-M01-04.10, FR-M01-04.11, BR-M01-33 |
| E19 | user-choice | M1 | Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Bảo trì bật | E19.1 | FR-M01-04.01, FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-04.13, FR-M01-01.12 |
| E20 | user-choice | M1 | Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Email Google đã thuộc tài khoản iShare | E20.1 | FR-M01-04.01, FR-M01-04.04, FR-M01-04.06, BR-M01-09 |
| E21 | user-choice | M1 | Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Guest chọn đọc chính sách trước khi quyết định đồng ý | E21.1 | FR-M01-04.01, FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-15.01, FR-M01-15.02, FR-M01-15.03, FR-M01-15.04, FR-M01-15.05, FR-M01-15.06, FR-M01-15.07, FR-M01-15.08, FR-M01-15.09, BR-M01-42, BR-M01-43, BR-M01-44, BR-M01-45, BR-M01-46, FR-M01-04.13, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, FR-M01-01.02, FR-M01-01.12, BR-M01-01, BR-M01-08, FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |
| E22 | user-choice | M1 | Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Thiếu username hoặc display_name | E22.1 | FR-M01-04.01, FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-04.13, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, FR-M01-01.02, FR-M01-01.12, BR-M01-01, BR-M01-08, FR-M01-03.01, FR-M01-03.02, FR-M01-03.04, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07 |
| E23 | user-choice | M1 | Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Username ngoài độ dài hoặc tập ký tự cho phép | E23.1 | FR-M01-04.01, FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-04.13, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, FR-M01-01.02, FR-M01-01.12, BR-M01-01, BR-M01-08, FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, BR-M01-05, BR-M01-06, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07 |
| E24 | user-choice | M1 | Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED | E24.1 | FR-M01-04.01, FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-04.13, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, FR-M01-01.02, FR-M01-01.12, BR-M01-01, BR-M01-08, FR-M01-03.01, FR-M01-03.02, FR-M01-03.06, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07 |
| E25 | user-choice | M1 | Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Display_name sau trim rỗng hoặc quá 50 ký tự | E25.1 | FR-M01-04.01, FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-04.13, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, FR-M01-01.02, FR-M01-01.12, BR-M01-01, BR-M01-08, FR-M01-03.01, FR-M01-03.02, FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.14, BR-M01-07 |
| E26 | user-choice | M1 | Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Display_name chứa ký tự không được nhận | E26.1 | FR-M01-04.01, FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-04.13, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, FR-M01-01.02, FR-M01-01.12, BR-M01-01, BR-M01-08, FR-M01-03.01, FR-M01-03.02, FR-M01-03.14, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, BR-M01-07 |
| E27 | user-choice | M1 | Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập | E27.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |
| E28 | user-choice | M1 | Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Thiếu username hoặc display_name | E28.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, FR-M01-03.04, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |
| E29 | user-choice | M1 | Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Username ngoài độ dài hoặc tập ký tự cho phép | E29.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, FR-M01-03.05, BR-M01-05, BR-M01-06, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |
| E30 | user-choice | M1 | Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED | E30.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, FR-M01-03.06, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |
| E31 | user-choice | M1 | Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Display_name sau trim rỗng hoặc quá 50 ký tự | E31.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.14, BR-M01-07, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |
| E32 | user-choice | M1 | Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Display_name chứa ký tự không được nhận | E32.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, FR-M01-03.14, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, BR-M01-07, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |
| E33 | user-choice | M1 | Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Yêu cầu không có phiên đăng nhập | E33.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, FR-M01-03.09 |
| E34 | user-choice | M1 | Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Bio sau trim dài hơn 155 ký tự | E34.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, FR-M02-03.04, FR-M02-03.11, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M02-03.03, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |
| E35 | user-choice | M1 | Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Lớp/Khối ngoài 10, 11, 12 | E35.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, FR-M02-03.06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |
| E36 | user-choice | M1 | Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Avatar sai loại, kể cả GIF động | E36.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, FR-M02-04.03, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |
| E37 | user-choice | M1 | Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Avatar vượt 5 MB | E37.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, FR-M02-04.04, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |
| E38 | user-choice | M1 | Đăng ký email; tại bước xác minh chọn mở link đã nhận | E38.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, FR-M01-02.07, FR-M01-01.09, BR-M01-10, BR-M01-33, BR-M01-38, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |
| E39 | user-choice | M1 | Đăng ký email; tại bước xác minh chọn mở link đã nhận; Link đã quá 1 giờ | E39.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, FR-M01-02.03, BR-M01-38 |
| E40 | user-choice | M1 | Đăng ký email; tại bước xác minh chọn mở link đã nhận; Link đã dùng | E40.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, FR-M01-02.06, BR-M01-38 |
| E41 | user-choice | M1 | Đăng ký email; tại bước xác minh chọn mở link đã nhận; Link cũ bị thay thế | E41.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.01, FR-M01-02.07, BR-M01-38 |
| E42 | user-choice | M1 | Đăng ký email; tại bước xác minh chọn mở link đã nhận; Chủ tài khoản còn NONE chọn xin lại email thay vì mở link hiện tại | E42.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.04, FR-M01-02.05, FR-M01-02.07, FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, FR-M01-01.09, BR-M01-10, BR-M01-33, BR-M01-38, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |
| E43 | user-choice | M1 | Đăng ký email; tại bước xác minh chọn yêu cầu gửi lại rồi mở link mới | E43.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.04, FR-M01-02.05, FR-M01-02.07, FR-M01-01.09, BR-M01-11, BR-M01-33, BR-M01-38, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |
| E44 | user-choice | M1 | Đăng ký email; tại bước xác minh chọn yêu cầu gửi lại rồi mở link mới; Yêu cầu lúc 09:00:45, chưa đủ 60 giây | E44.1 | FR-M01-01.01, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15, FR-M01-01.11, BR-M01-35, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, FR-M01-02.04, FR-M01-02.05, BR-M01-11, FR-M01-02.07, FR-M01-01.09, BR-M01-33, BR-M01-38, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E1: Không đánh dấu đồng ý chính sách.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối tạo tài khoản. | consent=false; chưa có tài khoản mới | END:REJECTED | FR-M01-01.05 |


**E2: Thiếu email hoặc mật khẩu.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối tạo tài khoản. | email="" hoặc password="" | END:REJECTED | FR-M01-01.07 |


**E3: Email đã thuộc tài khoản khác.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối tạo tài khoản thứ hai. | email=an.study@example.test đã được dùng; không làm lộ thêm thông tin ngoài FR | END:REJECTED | FR-M01-01.06, BR-M01-04 |


**E4: Mật khẩu dưới 8 hoặc trên 64 ký tự.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối mật khẩu và không tạo tài khoản. | password="1234567" hoặc "A"×65 | END:REJECTED | FR-M01-01.10, BR-M01-35 |


**E5: Công tắc tạm dừng đăng ký bật.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối tạo mới; không áp hạn chế này cho tài khoản đã qua bước 1. | registration_paused=true | END:REJECTED | FR-M01-01.08, FR-M01-01.09, BR-M01-33 |


**E6: Chế độ bảo trì bật.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối tạo tài khoản mới bằng email. | maintenance=true | END:REJECTED | FR-M01-01.12, BR-M01-37 |


**E7: Guest chọn đọc chính sách trước khi gửi đăng ký.** Thay thế M3; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | ACT-001 | Guest mở liên kết Privacy Policy/ToS ở điểm đồng ý. | Bản chính sách P2.0 | E7.2 | FR-M01-01.04 |
| E7.2 | SYSTEM | Hệ thống hiển thị trang chính sách công khai; việc đọc không ghi nhận đồng ý. | Phiên bản minh họa P2.0; Chính sách quyền riêng tư có dữ liệu thu thập, mục đích, dịch vụ ngoài, thời gian lưu, quyền, dưới 16 tuổi, thay đổi, liên hệ; Điều khoản có quy tắc/nội dung cấm, kiểm duyệt/cảnh báo, khóa/khiếu nại, quyền với nội dung. Bốn nhóm: tài khoản/hồ sơ; nội dung tạo; an toàn cộng đồng; dữ liệu qua AI. Nêu AI xử lý cả bản soạn khi bấm Gợi ý topic, dịch vụ đăng nhập/lưu ảnh/email/AI, không bán dữ liệu, lưu bình luận/tin nhắn/nhật ký sau xóa, quyền sửa/xóa/bản sao, rút đồng ý qua vô hiệu hóa. Không nêu tên nhà cung cấp hay phiên đăng nhập; MS1 chưa có tải bản sao; câu chữ chính sách và email liên hệ còn chờ hoàn thiện. | E7.3 | FR-M01-15.01, FR-M01-15.02, FR-M01-15.03, FR-M01-15.04, FR-M01-15.05, FR-M01-15.06, FR-M01-15.07, FR-M01-15.08, FR-M01-15.09, BR-M01-42, BR-M01-43, BR-M01-44, BR-M01-45, BR-M01-46 |
| E7.3 | ACT-001 | Guest quay lại điểm đồng ý, điền email/mật khẩu và đánh dấu đồng ý rồi gửi. | an.study@example.test; mật khẩu "  Mật khẩu 2026  "; consent=true | M4 | FR-M01-01.01, FR-M01-01.13, BR-M01-03 |


**E8: Link xác minh quá 1 giờ.** Thay thế M6; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống từ chối link này, chưa nâng mức xác minh; cho quay về yêu cầu gửi lại. | A01 vẫn NONE; link lỗi L-old | E8.2 | FR-M01-02.03, FR-M01-02.06, FR-M01-02.07, BR-M01-38 |
| E8.2 | ACT-001 | Chủ tài khoản yêu cầu gửi lại khi đã cách lần gửi trước ít nhất 60 giây. | Lần gửi trước 09:00; yêu cầu 10:05 | E8.3 | FR-M01-02.04, FR-M01-02.05 |
| E8.3 | SYSTEM | Hệ thống gửi link xác minh mới, vô hiệu link cũ; tài khoản vẫn NONE. | L-new gửi 10:05, hạn một giờ | E8.4 | FR-M01-02.04, FR-M01-02.07 |
| E8.4 | ACT-001 | Chủ tài khoản mở link mới chưa dùng lúc 10:10. | L-new còn hạn, thuộc A01 | M6 | FR-M01-02.01 |


**E9: Link xác minh bị thay bởi lần gửi mới.** Thay thế M6; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống từ chối link này, chưa nâng mức xác minh; cho quay về yêu cầu gửi lại. | A01 vẫn NONE; link lỗi L-old | E9.2 | FR-M01-02.03, FR-M01-02.06, FR-M01-02.07, BR-M01-38 |
| E9.2 | ACT-001 | Chủ tài khoản yêu cầu gửi lại khi đã cách lần gửi trước ít nhất 60 giây. | Lần gửi trước 09:00; yêu cầu 10:05 | E9.3 | FR-M01-02.04, FR-M01-02.05 |
| E9.3 | SYSTEM | Hệ thống gửi link xác minh mới, vô hiệu link cũ; tài khoản vẫn NONE. | L-new gửi 10:05, hạn một giờ | E9.4 | FR-M01-02.04, FR-M01-02.07 |
| E9.4 | ACT-001 | Chủ tài khoản mở link mới chưa dùng lúc 10:10. | L-new còn hạn, thuộc A01 | M6 | FR-M01-02.01 |


**E10: Link xác minh đã được dùng trước lần mở này.** Thay thế M6; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | SYSTEM | Hệ thống từ chối dùng lại; giữ mức xác minh hiện có, không hạ về NONE hoặc yêu cầu lại bước đã hoàn tất. | L1 đã dùng; A01 có thể đã EMAIL_VERIFIED hoặc SETUP_COMPLETED | END:REJECTED | FR-M01-02.06, BR-M01-38 |


**E11: Thiếu username hoặc display_name.** Thay thế M8; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="" hoặc display_name="" | E11.2 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E11.2 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | M8 | FR-M01-03.04, BR-M01-05, BR-M01-06 |


**E12: Username ngoài độ dài hoặc tập ký tự cho phép.** Thay thế M8; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="ab", hoặc "a"×21, hoặc "an.hoc" | E12.2 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E12.2 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | M8 | FR-M01-03.05, BR-M01-05, BR-M01-06 |


**E13: Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED.** Thay thế M8; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | An_12A1 trùng an_12a1; hoặc Cuong trùng username DELETED cuong | E13.2 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E13.2 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | M8 | FR-M01-03.06, BR-M01-05, BR-M01-06 |


**E14: Display_name sau trim rỗng hoặc quá 50 ký tự.** Thay thế M8; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | "   " hoặc "A"×51 | E14.2 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E14.2 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | M8 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |


**E15: Display_name chứa ký tự không được nhận.** Thay thế M8; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | display_name="An 😊" | E15.2 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E15.2 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | M8 | FR-M01-03.14, BR-M01-05, BR-M01-06 |


**E16: Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E16 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E16.1 | ACT-001 | Guest chọn đăng ký/đăng nhập bằng Google. | Thiết bị P01 | E16.2 | FR-M01-04.01 |
| E16.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Yêu cầu danh tính Google cho lần truy cập này | E16.3 | FR-M01-04.01 |
| E16.3 | ACT-004 | Google cung cấp danh tính đã xác thực cho iShare. | email=binh.study@example.test; tên Google=Trần Bình | E16.4 | FR-M01-04.01 |
| E16.4 | SYSTEM | Hệ thống xác định email chưa thuộc tài khoản, cung cấp liên kết chính sách và yêu cầu đánh dấu ô đồng ý. | P2.0; Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý. | E16.5 | FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E16.5 | ACT-001 | Guest đánh dấu đồng ý chính sách hiện hành. | P2.0; consent=true; không yêu cầu tuổi/ngày sinh | E16.6 | FR-M01-04.12, FR-M01-04.13 |
| E16.6 | SYSTEM | Hệ thống kiểm điều kiện tạo mới, tạo A02 ACTIVE/USER/EMAIL_VERIFIED không có mật khẩu iShare; lưu đồng ý; mở bước 3 với tên Google điền sẵn, username để người dùng tự đặt. | A02; P2.0, 06/11/2026 09:00; display_name=Trần Bình; username chưa có | E16.7 | FR-M01-04.01, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, FR-M01-04.13, FR-M01-01.02, FR-M01-01.12, BR-M01-01, BR-M01-08 |
| E16.7 | ACT-002 | Chủ tài khoản đặt username và sửa tên Google rồi gửi; bỏ qua các trường tùy chọn. | username=Binh_12A1; display_name=Bình Trần | E16.8 | FR-M01-04.02, FR-M01-04.03, FR-M01-03.01, FR-M01-03.02 |
| E16.8 | SYSTEM | Hệ thống kiểm định danh theo quy tắc bước 3, lưu tên đã sửa/username và hoàn tất SETUP_COMPLETED. | A02 ACTIVE/USER/SETUP_COMPLETED; Bình Trần; Binh_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E17: Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Guest không đánh dấu đồng ý.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E17 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E17.1 | ACT-001 | Guest chọn đăng ký/đăng nhập bằng Google. | Thiết bị P01 | E17.2 | FR-M01-04.01 |
| E17.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Yêu cầu danh tính Google cho lần truy cập này | E17.3 | FR-M01-04.01 |
| E17.3 | ACT-004 | Google cung cấp danh tính đã xác thực cho iShare. | email=binh.study@example.test; tên Google=Trần Bình | E17.4 | FR-M01-04.01 |
| E17.4 | SYSTEM | Hệ thống xác định email chưa thuộc tài khoản, cung cấp liên kết chính sách và yêu cầu đánh dấu ô đồng ý. | P2.0; Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý. | E17.5 | FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E17.5 | ACT-001 | Guest đánh dấu đồng ý chính sách hiện hành. | P2.0; consent=true; không yêu cầu tuổi/ngày sinh | E17.6 | FR-M01-04.12, FR-M01-04.13 |
| E17.6 | SYSTEM | Hệ thống từ chối tạo tài khoản Google. | consent=false | END:REJECTED | FR-M01-04.07, FR-M01-04.12 |


**E18: Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Tạm dừng tạo tài khoản mới bật.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E18 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E18.1 | ACT-001 | Guest chọn đăng ký/đăng nhập bằng Google. | Thiết bị P01 | E18.2 | FR-M01-04.01 |
| E18.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Yêu cầu danh tính Google cho lần truy cập này | E18.3 | FR-M01-04.01 |
| E18.3 | ACT-004 | Google cung cấp danh tính đã xác thực cho iShare. | email=binh.study@example.test; tên Google=Trần Bình | E18.4 | FR-M01-04.01 |
| E18.4 | SYSTEM | Hệ thống xác định email chưa thuộc tài khoản, cung cấp liên kết chính sách và yêu cầu đánh dấu ô đồng ý. | P2.0; Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý. | E18.5 | FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E18.5 | ACT-001 | Guest đánh dấu đồng ý chính sách hiện hành. | P2.0; consent=true; không yêu cầu tuổi/ngày sinh | E18.6 | FR-M01-04.12, FR-M01-04.13 |
| E18.6 | SYSTEM | Hệ thống từ chối tài khoản Google mới; không áp hạn chế này cho tài khoản đã tồn tại. | registration_paused=true; email chưa có | END:REJECTED | FR-M01-04.10, FR-M01-04.11, BR-M01-33 |


**E19: Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Bảo trì bật.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E19 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E19.1 | ACT-001 | Guest chọn đăng ký/đăng nhập bằng Google. | Thiết bị P01 | E19.2 | FR-M01-04.01 |
| E19.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Yêu cầu danh tính Google cho lần truy cập này | E19.3 | FR-M01-04.01 |
| E19.3 | ACT-004 | Google cung cấp danh tính đã xác thực cho iShare. | email=binh.study@example.test; tên Google=Trần Bình | E19.4 | FR-M01-04.01 |
| E19.4 | SYSTEM | Hệ thống xác định email chưa thuộc tài khoản, cung cấp liên kết chính sách và yêu cầu đánh dấu ô đồng ý. | P2.0; Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý. | E19.5 | FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E19.5 | ACT-001 | Guest đánh dấu đồng ý chính sách hiện hành. | P2.0; consent=true; không yêu cầu tuổi/ngày sinh | E19.6 | FR-M01-04.12, FR-M01-04.13 |
| E19.6 | SYSTEM | Hệ thống từ chối tạo tài khoản Google mới. | maintenance=true | END:REJECTED | FR-M01-01.12 |


**E20: Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Email Google đã thuộc tài khoản iShare.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E20 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E20.1 | ACT-001 | Guest chọn đăng ký/đăng nhập bằng Google. | Thiết bị P01 | E20.2 | FR-M01-04.01 |
| E20.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Yêu cầu danh tính Google cho lần truy cập này | E20.3 | FR-M01-04.01 |
| E20.3 | ACT-004 | Google cung cấp danh tính đã xác thực cho iShare. | email=binh.study@example.test; tên Google=Trần Bình | E20.4 | FR-M01-04.01 |
| E20.4 | SYSTEM | Hệ thống nhận diện tài khoản có sẵn, không tạo bản thứ hai; chuyển ngữ cảnh danh tính đã xác thực sang UC-M01-015. | Email binh.study@example.test đã có; danh tính Google được giữ cho hành trình đăng nhập; các SC Google hiện có ở nhóm UC-M01-015 tiếp nhận | END:HANDED_OFF | FR-M01-04.04, FR-M01-04.06, BR-M01-09 |


**E21: Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Guest chọn đọc chính sách trước khi quyết định đồng ý.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E21 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E21.1 | ACT-001 | Guest chọn đăng ký/đăng nhập bằng Google. | Thiết bị P01 | E21.2 | FR-M01-04.01 |
| E21.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Yêu cầu danh tính Google cho lần truy cập này | E21.3 | FR-M01-04.01 |
| E21.3 | ACT-004 | Google cung cấp danh tính đã xác thực cho iShare. | email=binh.study@example.test; tên Google=Trần Bình | E21.4 | FR-M01-04.01 |
| E21.4 | SYSTEM | Hệ thống xác định email chưa thuộc tài khoản, cung cấp liên kết chính sách và yêu cầu đánh dấu ô đồng ý. | P2.0; Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý. | E21.5 | FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E21.5 | ACT-001 | Guest mở liên kết chính sách ở bước đồng ý. | P2.0; chưa đồng ý | E21.6 | FR-M01-01.04, FR-M01-04.12 |
| E21.6 | SYSTEM | Hệ thống hiển thị trang chính sách công khai, không tự ghi đồng ý. | Phiên bản minh họa P2.0; Chính sách quyền riêng tư có dữ liệu thu thập, mục đích, dịch vụ ngoài, thời gian lưu, quyền, dưới 16 tuổi, thay đổi, liên hệ; Điều khoản có quy tắc/nội dung cấm, kiểm duyệt/cảnh báo, khóa/khiếu nại, quyền với nội dung. Bốn nhóm: tài khoản/hồ sơ; nội dung tạo; an toàn cộng đồng; dữ liệu qua AI. Nêu AI xử lý cả bản soạn khi bấm Gợi ý topic, dịch vụ đăng nhập/lưu ảnh/email/AI, không bán dữ liệu, lưu bình luận/tin nhắn/nhật ký sau xóa, quyền sửa/xóa/bản sao, rút đồng ý qua vô hiệu hóa. Không nêu tên nhà cung cấp hay phiên đăng nhập; MS1 chưa có tải bản sao; câu chữ chính sách và email liên hệ còn chờ hoàn thiện. | E21.7 | FR-M01-15.01, FR-M01-15.02, FR-M01-15.03, FR-M01-15.04, FR-M01-15.05, FR-M01-15.06, FR-M01-15.07, FR-M01-15.08, FR-M01-15.09, BR-M01-42, BR-M01-43, BR-M01-44, BR-M01-45, BR-M01-46 |
| E21.7 | ACT-001 | Guest quay lại điểm đồng ý, đánh dấu ô đồng ý với P2.0 rồi gửi. | consent=true; danh tính Google binh.study@example.test vẫn là ngữ cảnh hiện tại | E21.8 | FR-M01-04.12, FR-M01-04.13 |
| E21.8 | SYSTEM | Hệ thống kiểm điều kiện tạo mới, tạo A02 ACTIVE/USER/EMAIL_VERIFIED không có mật khẩu iShare; lưu đồng ý; mở bước 3 với tên Google điền sẵn, username để người dùng tự đặt. | A02; P2.0, 06/11/2026 09:00; display_name=Trần Bình; username chưa có | E21.9 | FR-M01-04.01, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, FR-M01-04.13, FR-M01-01.02, FR-M01-01.12, BR-M01-01, BR-M01-08 |
| E21.9 | ACT-002 | Chủ tài khoản đặt username và sửa tên Google rồi gửi; bỏ qua các trường tùy chọn. | username=Binh_12A1; display_name=Bình Trần | E21.10 | FR-M01-04.02, FR-M01-04.03, FR-M01-03.01, FR-M01-03.02 |
| E21.10 | SYSTEM | Hệ thống kiểm định danh theo quy tắc bước 3, lưu tên đã sửa/username và hoàn tất SETUP_COMPLETED. | A02 ACTIVE/USER/SETUP_COMPLETED; Bình Trần; Binh_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E22: Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Thiếu username hoặc display_name.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E22 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E22.1 | ACT-001 | Guest chọn đăng ký/đăng nhập bằng Google. | Thiết bị P01 | E22.2 | FR-M01-04.01 |
| E22.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Yêu cầu danh tính Google cho lần truy cập này | E22.3 | FR-M01-04.01 |
| E22.3 | ACT-004 | Google cung cấp danh tính đã xác thực cho iShare. | email=binh.study@example.test; tên Google=Trần Bình | E22.4 | FR-M01-04.01 |
| E22.4 | SYSTEM | Hệ thống xác định email chưa thuộc tài khoản, cung cấp liên kết chính sách và yêu cầu đánh dấu ô đồng ý. | P2.0; Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý. | E22.5 | FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E22.5 | ACT-001 | Guest đánh dấu đồng ý chính sách hiện hành. | P2.0; consent=true; không yêu cầu tuổi/ngày sinh | E22.6 | FR-M01-04.12, FR-M01-04.13 |
| E22.6 | SYSTEM | Hệ thống kiểm điều kiện tạo mới, tạo A02 ACTIVE/USER/EMAIL_VERIFIED không có mật khẩu iShare; lưu đồng ý; mở bước 3 với tên Google điền sẵn, username để người dùng tự đặt. | A02; P2.0, 06/11/2026 09:00; display_name=Trần Bình; username chưa có | E22.7 | FR-M01-04.01, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, FR-M01-04.13, FR-M01-01.02, FR-M01-01.12, BR-M01-01, BR-M01-08 |
| E22.7 | ACT-002 | Chủ tài khoản đặt username và sửa tên Google rồi gửi; bỏ qua các trường tùy chọn. | username=Binh_12A1; display_name=Bình Trần | E22.8 | FR-M01-04.02, FR-M01-04.03, FR-M01-03.01, FR-M01-03.02 |
| E22.8 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="" hoặc display_name="" | E22.9 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E22.9 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E22.10 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E22.10 | SYSTEM | Hệ thống kiểm định danh theo quy tắc bước 3, lưu tên đã sửa/username và hoàn tất SETUP_COMPLETED. | A02 ACTIVE/USER/SETUP_COMPLETED; Bình Trần; Binh_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E23: Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Username ngoài độ dài hoặc tập ký tự cho phép.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E23 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E23.1 | ACT-001 | Guest chọn đăng ký/đăng nhập bằng Google. | Thiết bị P01 | E23.2 | FR-M01-04.01 |
| E23.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Yêu cầu danh tính Google cho lần truy cập này | E23.3 | FR-M01-04.01 |
| E23.3 | ACT-004 | Google cung cấp danh tính đã xác thực cho iShare. | email=binh.study@example.test; tên Google=Trần Bình | E23.4 | FR-M01-04.01 |
| E23.4 | SYSTEM | Hệ thống xác định email chưa thuộc tài khoản, cung cấp liên kết chính sách và yêu cầu đánh dấu ô đồng ý. | P2.0; Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý. | E23.5 | FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E23.5 | ACT-001 | Guest đánh dấu đồng ý chính sách hiện hành. | P2.0; consent=true; không yêu cầu tuổi/ngày sinh | E23.6 | FR-M01-04.12, FR-M01-04.13 |
| E23.6 | SYSTEM | Hệ thống kiểm điều kiện tạo mới, tạo A02 ACTIVE/USER/EMAIL_VERIFIED không có mật khẩu iShare; lưu đồng ý; mở bước 3 với tên Google điền sẵn, username để người dùng tự đặt. | A02; P2.0, 06/11/2026 09:00; display_name=Trần Bình; username chưa có | E23.7 | FR-M01-04.01, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, FR-M01-04.13, FR-M01-01.02, FR-M01-01.12, BR-M01-01, BR-M01-08 |
| E23.7 | ACT-002 | Chủ tài khoản đặt username và sửa tên Google rồi gửi; bỏ qua các trường tùy chọn. | username=Binh_12A1; display_name=Bình Trần | E23.8 | FR-M01-04.02, FR-M01-04.03, FR-M01-03.01, FR-M01-03.02 |
| E23.8 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="ab", hoặc "a"×21, hoặc "an.hoc" | E23.9 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E23.9 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E23.10 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E23.10 | SYSTEM | Hệ thống kiểm định danh theo quy tắc bước 3, lưu tên đã sửa/username và hoàn tất SETUP_COMPLETED. | A02 ACTIVE/USER/SETUP_COMPLETED; Bình Trần; Binh_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E24: Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E24 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E24.1 | ACT-001 | Guest chọn đăng ký/đăng nhập bằng Google. | Thiết bị P01 | E24.2 | FR-M01-04.01 |
| E24.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Yêu cầu danh tính Google cho lần truy cập này | E24.3 | FR-M01-04.01 |
| E24.3 | ACT-004 | Google cung cấp danh tính đã xác thực cho iShare. | email=binh.study@example.test; tên Google=Trần Bình | E24.4 | FR-M01-04.01 |
| E24.4 | SYSTEM | Hệ thống xác định email chưa thuộc tài khoản, cung cấp liên kết chính sách và yêu cầu đánh dấu ô đồng ý. | P2.0; Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý. | E24.5 | FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E24.5 | ACT-001 | Guest đánh dấu đồng ý chính sách hiện hành. | P2.0; consent=true; không yêu cầu tuổi/ngày sinh | E24.6 | FR-M01-04.12, FR-M01-04.13 |
| E24.6 | SYSTEM | Hệ thống kiểm điều kiện tạo mới, tạo A02 ACTIVE/USER/EMAIL_VERIFIED không có mật khẩu iShare; lưu đồng ý; mở bước 3 với tên Google điền sẵn, username để người dùng tự đặt. | A02; P2.0, 06/11/2026 09:00; display_name=Trần Bình; username chưa có | E24.7 | FR-M01-04.01, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, FR-M01-04.13, FR-M01-01.02, FR-M01-01.12, BR-M01-01, BR-M01-08 |
| E24.7 | ACT-002 | Chủ tài khoản đặt username và sửa tên Google rồi gửi; bỏ qua các trường tùy chọn. | username=Binh_12A1; display_name=Bình Trần | E24.8 | FR-M01-04.02, FR-M01-04.03, FR-M01-03.01, FR-M01-03.02 |
| E24.8 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | An_12A1 trùng an_12a1; hoặc Cuong trùng username DELETED cuong | E24.9 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E24.9 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E24.10 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E24.10 | SYSTEM | Hệ thống kiểm định danh theo quy tắc bước 3, lưu tên đã sửa/username và hoàn tất SETUP_COMPLETED. | A02 ACTIVE/USER/SETUP_COMPLETED; Bình Trần; Binh_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E25: Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Display_name sau trim rỗng hoặc quá 50 ký tự.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E25 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E25.1 | ACT-001 | Guest chọn đăng ký/đăng nhập bằng Google. | Thiết bị P01 | E25.2 | FR-M01-04.01 |
| E25.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Yêu cầu danh tính Google cho lần truy cập này | E25.3 | FR-M01-04.01 |
| E25.3 | ACT-004 | Google cung cấp danh tính đã xác thực cho iShare. | email=binh.study@example.test; tên Google=Trần Bình | E25.4 | FR-M01-04.01 |
| E25.4 | SYSTEM | Hệ thống xác định email chưa thuộc tài khoản, cung cấp liên kết chính sách và yêu cầu đánh dấu ô đồng ý. | P2.0; Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý. | E25.5 | FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E25.5 | ACT-001 | Guest đánh dấu đồng ý chính sách hiện hành. | P2.0; consent=true; không yêu cầu tuổi/ngày sinh | E25.6 | FR-M01-04.12, FR-M01-04.13 |
| E25.6 | SYSTEM | Hệ thống kiểm điều kiện tạo mới, tạo A02 ACTIVE/USER/EMAIL_VERIFIED không có mật khẩu iShare; lưu đồng ý; mở bước 3 với tên Google điền sẵn, username để người dùng tự đặt. | A02; P2.0, 06/11/2026 09:00; display_name=Trần Bình; username chưa có | E25.7 | FR-M01-04.01, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, FR-M01-04.13, FR-M01-01.02, FR-M01-01.12, BR-M01-01, BR-M01-08 |
| E25.7 | ACT-002 | Chủ tài khoản đặt username và sửa tên Google rồi gửi; bỏ qua các trường tùy chọn. | username=Binh_12A1; display_name=Bình Trần | E25.8 | FR-M01-04.02, FR-M01-04.03, FR-M01-03.01, FR-M01-03.02 |
| E25.8 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | "   " hoặc "A"×51 | E25.9 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E25.9 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E25.10 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E25.10 | SYSTEM | Hệ thống kiểm định danh theo quy tắc bước 3, lưu tên đã sửa/username và hoàn tất SETUP_COMPLETED. | A02 ACTIVE/USER/SETUP_COMPLETED; Bình Trần; Binh_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E26: Guest chọn Google để tạo tài khoản mới; Google trả danh tính thành công; Display_name chứa ký tự không được nhận.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E26 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E26.1 | ACT-001 | Guest chọn đăng ký/đăng nhập bằng Google. | Thiết bị P01 | E26.2 | FR-M01-04.01 |
| E26.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Yêu cầu danh tính Google cho lần truy cập này | E26.3 | FR-M01-04.01 |
| E26.3 | ACT-004 | Google cung cấp danh tính đã xác thực cho iShare. | email=binh.study@example.test; tên Google=Trần Bình | E26.4 | FR-M01-04.01 |
| E26.4 | SYSTEM | Hệ thống xác định email chưa thuộc tài khoản, cung cấp liên kết chính sách và yêu cầu đánh dấu ô đồng ý. | P2.0; Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý. | E26.5 | FR-M01-04.07, FR-M01-04.12, FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E26.5 | ACT-001 | Guest đánh dấu đồng ý chính sách hiện hành. | P2.0; consent=true; không yêu cầu tuổi/ngày sinh | E26.6 | FR-M01-04.12, FR-M01-04.13 |
| E26.6 | SYSTEM | Hệ thống kiểm điều kiện tạo mới, tạo A02 ACTIVE/USER/EMAIL_VERIFIED không có mật khẩu iShare; lưu đồng ý; mở bước 3 với tên Google điền sẵn, username để người dùng tự đặt. | A02; P2.0, 06/11/2026 09:00; display_name=Trần Bình; username chưa có | E26.7 | FR-M01-04.01, FR-M01-04.02, FR-M01-04.03, FR-M01-04.10, FR-M01-04.13, FR-M01-01.02, FR-M01-01.12, BR-M01-01, BR-M01-08 |
| E26.7 | ACT-002 | Chủ tài khoản đặt username và sửa tên Google rồi gửi; bỏ qua các trường tùy chọn. | username=Binh_12A1; display_name=Bình Trần | E26.8 | FR-M01-04.02, FR-M01-04.03, FR-M01-03.01, FR-M01-03.02 |
| E26.8 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | display_name="An 😊" | E26.9 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E26.9 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E26.10 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E26.10 | SYSTEM | Hệ thống kiểm định danh theo quy tắc bước 3, lưu tên đã sửa/username và hoàn tất SETUP_COMPLETED. | A02 ACTIVE/USER/SETUP_COMPLETED; Bình Trần; Binh_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E27: Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E27 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E27.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E27.2 | FR-M01-01.01 |
| E27.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E27.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E27.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E27.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E27.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E27.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E27.5 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E27.6 | FR-M01-02.01, BR-M01-10 |
| E27.6 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E27.7 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E27.7 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn lưu cả thông tin tùy chọn rồi gửi bước 3. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB | E27.8 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E27.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; lưu hồ sơ tùy chọn, giữ ảnh avatar gốc; bio được trim và đếm emoji/xuống dòng theo M02; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-03.03, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |


**E28: Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Thiếu username hoặc display_name.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E28 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E28.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E28.2 | FR-M01-01.01 |
| E28.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E28.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E28.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E28.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E28.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E28.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E28.5 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E28.6 | FR-M01-02.01, BR-M01-10 |
| E28.6 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E28.7 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E28.7 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn lưu cả thông tin tùy chọn rồi gửi bước 3. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB | E28.8 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E28.8 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="" hoặc display_name="" | E28.9 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E28.9 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E28.10 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E28.10 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; lưu hồ sơ tùy chọn, giữ ảnh avatar gốc; bio được trim và đếm emoji/xuống dòng theo M02; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-03.03, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |


**E29: Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Username ngoài độ dài hoặc tập ký tự cho phép.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E29 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E29.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E29.2 | FR-M01-01.01 |
| E29.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E29.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E29.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E29.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E29.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E29.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E29.5 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E29.6 | FR-M01-02.01, BR-M01-10 |
| E29.6 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E29.7 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E29.7 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn lưu cả thông tin tùy chọn rồi gửi bước 3. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB | E29.8 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E29.8 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="ab", hoặc "a"×21, hoặc "an.hoc" | E29.9 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E29.9 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E29.10 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E29.10 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; lưu hồ sơ tùy chọn, giữ ảnh avatar gốc; bio được trim và đếm emoji/xuống dòng theo M02; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-03.03, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |


**E30: Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E30 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E30.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E30.2 | FR-M01-01.01 |
| E30.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E30.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E30.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E30.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E30.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E30.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E30.5 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E30.6 | FR-M01-02.01, BR-M01-10 |
| E30.6 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E30.7 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E30.7 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn lưu cả thông tin tùy chọn rồi gửi bước 3. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB | E30.8 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E30.8 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | An_12A1 trùng an_12a1; hoặc Cuong trùng username DELETED cuong | E30.9 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E30.9 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E30.10 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E30.10 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; lưu hồ sơ tùy chọn, giữ ảnh avatar gốc; bio được trim và đếm emoji/xuống dòng theo M02; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-03.03, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |


**E31: Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Display_name sau trim rỗng hoặc quá 50 ký tự.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E31 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E31.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E31.2 | FR-M01-01.01 |
| E31.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E31.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E31.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E31.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E31.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E31.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E31.5 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E31.6 | FR-M01-02.01, BR-M01-10 |
| E31.6 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E31.7 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E31.7 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn lưu cả thông tin tùy chọn rồi gửi bước 3. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB | E31.8 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E31.8 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | "   " hoặc "A"×51 | E31.9 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E31.9 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E31.10 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E31.10 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; lưu hồ sơ tùy chọn, giữ ảnh avatar gốc; bio được trim và đếm emoji/xuống dòng theo M02; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-03.03, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |


**E32: Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Display_name chứa ký tự không được nhận.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E32 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E32.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E32.2 | FR-M01-01.01 |
| E32.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E32.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E32.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E32.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E32.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E32.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E32.5 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E32.6 | FR-M01-02.01, BR-M01-10 |
| E32.6 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E32.7 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E32.7 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn lưu cả thông tin tùy chọn rồi gửi bước 3. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB | E32.8 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E32.8 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | display_name="An 😊" | E32.9 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E32.9 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E32.10 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E32.10 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; lưu hồ sơ tùy chọn, giữ ảnh avatar gốc; bio được trim và đếm emoji/xuống dòng theo M02; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-03.03, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |


**E33: Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Yêu cầu không có phiên đăng nhập.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E33 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E33.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E33.2 | FR-M01-01.01 |
| E33.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E33.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E33.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E33.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E33.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E33.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E33.5 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E33.6 | FR-M01-02.01, BR-M01-10 |
| E33.6 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E33.7 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E33.7 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn lưu cả thông tin tùy chọn rồi gửi bước 3. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB | E33.8 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E33.8 | SYSTEM | Hệ thống từ chối thiết lập; không nâng mức xác minh. | Không có phiên; giữ dữ liệu tài khoản trước yêu cầu | END:REJECTED | FR-M01-03.09 |


**E34: Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Bio sau trim dài hơn 155 ký tự.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E34 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E34.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E34.2 | FR-M01-01.01 |
| E34.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E34.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E34.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E34.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E34.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E34.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E34.5 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E34.6 | FR-M01-02.01, BR-M01-10 |
| E34.6 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E34.7 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E34.7 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn lưu cả thông tin tùy chọn rồi gửi bước 3. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB | E34.8 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E34.8 | SYSTEM | Hệ thống từ chối giá trị tùy chọn vi phạm; chưa hoàn tất bước 3; cho sửa hoặc bỏ thông tin tùy chọn. | bio="A"×156 | E34.9 | FR-M01-03.02, FR-M01-03.03, FR-M02-03.04, FR-M02-03.11 |
| E34.9 | ACT-002 | Chủ tài khoản bỏ trường tùy chọn bị lỗi và gửi lại username/display_name hợp lệ. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E34.10 | FR-M01-03.02, FR-M01-03.03, FR-M02-03.04, FR-M02-03.11 |
| E34.10 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; lưu hồ sơ tùy chọn, giữ ảnh avatar gốc; bio được trim và đếm emoji/xuống dòng theo M02; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-03.03, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |


**E35: Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Lớp/Khối ngoài 10, 11, 12.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E35 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E35.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E35.2 | FR-M01-01.01 |
| E35.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E35.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E35.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E35.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E35.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E35.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E35.5 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E35.6 | FR-M01-02.01, BR-M01-10 |
| E35.6 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E35.7 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E35.7 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn lưu cả thông tin tùy chọn rồi gửi bước 3. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB | E35.8 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E35.8 | SYSTEM | Hệ thống từ chối giá trị tùy chọn vi phạm; chưa hoàn tất bước 3; cho sửa hoặc bỏ thông tin tùy chọn. | Lớp/Khối=9 | E35.9 | FR-M01-03.02, FR-M01-03.03, FR-M02-03.06 |
| E35.9 | ACT-002 | Chủ tài khoản bỏ trường tùy chọn bị lỗi và gửi lại username/display_name hợp lệ. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E35.10 | FR-M01-03.02, FR-M01-03.03, FR-M02-03.06 |
| E35.10 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; lưu hồ sơ tùy chọn, giữ ảnh avatar gốc; bio được trim và đếm emoji/xuống dòng theo M02; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-03.03, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |


**E36: Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Avatar sai loại, kể cả GIF động.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E36 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E36.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E36.2 | FR-M01-01.01 |
| E36.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E36.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E36.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E36.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E36.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E36.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E36.5 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E36.6 | FR-M01-02.01, BR-M01-10 |
| E36.6 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E36.7 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E36.7 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn lưu cả thông tin tùy chọn rồi gửi bước 3. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB | E36.8 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E36.8 | SYSTEM | Hệ thống từ chối giá trị tùy chọn vi phạm; chưa hoàn tất bước 3; cho sửa hoặc bỏ thông tin tùy chọn. | avatar=an.gif, 1 MB | E36.9 | FR-M01-03.02, FR-M01-03.03, FR-M02-04.03 |
| E36.9 | ACT-002 | Chủ tài khoản bỏ trường tùy chọn bị lỗi và gửi lại username/display_name hợp lệ. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E36.10 | FR-M01-03.02, FR-M01-03.03, FR-M02-04.03 |
| E36.10 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; lưu hồ sơ tùy chọn, giữ ảnh avatar gốc; bio được trim và đếm emoji/xuống dòng theo M02; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-03.03, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |


**E37: Guest đăng ký email và chọn nhập thông tin tùy chọn tại bước thiết lập; Avatar vượt 5 MB.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E37 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E37.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E37.2 | FR-M01-01.01 |
| E37.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E37.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E37.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E37.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E37.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E37.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E37.5 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E37.6 | FR-M01-02.01, BR-M01-10 |
| E37.6 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E37.7 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E37.7 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn lưu cả thông tin tùy chọn rồi gửi bước 3. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB | E37.8 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E37.8 | SYSTEM | Hệ thống từ chối giá trị tùy chọn vi phạm; chưa hoàn tất bước 3; cho sửa hoặc bỏ thông tin tùy chọn. | avatar=an.png, 6 MB | E37.9 | FR-M01-03.02, FR-M01-03.03, FR-M02-04.04 |
| E37.9 | ACT-002 | Chủ tài khoản bỏ trường tùy chọn bị lỗi và gửi lại username/display_name hợp lệ. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E37.10 | FR-M01-03.02, FR-M01-03.03, FR-M02-04.04 |
| E37.10 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; lưu hồ sơ tùy chọn, giữ ảnh avatar gốc; bio được trim và đếm emoji/xuống dòng theo M02; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name="  Minh An  "; bio="  Thích Toán 📐  " → "Thích Toán 📐"; Lớp/Khối=12; avatar=an.png, PNG 1 MB; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-03.03, FR-M02-03.03, FR-M02-03.04, FR-M02-03.05, FR-M02-03.06, FR-M02-03.07, FR-M02-03.11, FR-M02-03.12, FR-M02-03.13, FR-M02-04.01, FR-M02-04.02, BR-M02-04, BR-M02-06, BR-M02-09, BR-M02-33, FR-M01-01.09, BR-M01-33 |


**E38: Đăng ký email; tại bước xác minh chọn mở link đã nhận.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E38 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E38.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E38.2 | FR-M01-01.01 |
| E38.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E38.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E38.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E38.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E38.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E38.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E38.5 | ACT-001 | Chủ tài khoản mở link xác minh đã nhận. | L1 gửi 09:00, mở 09:10; A01 NONE | E38.6 | FR-M01-02.01 |
| E38.6 | SYSTEM | Hệ thống kiểm hạn/hiệu lực, ghi nhận xác minh, không cho dùng lại link và đưa chủ tài khoản tới bước 3. | A01 EMAIL_VERIFIED; L1 đã dùng; bước thiết lập UC-M01-003 tiếp theo | E38.7 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, FR-M01-02.07, FR-M01-01.09, BR-M01-10, BR-M01-33, BR-M01-38 |
| E38.7 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E38.8 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E38.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E39: Đăng ký email; tại bước xác minh chọn mở link đã nhận; Link đã quá 1 giờ.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E39 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E39.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E39.2 | FR-M01-01.01 |
| E39.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E39.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E39.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E39.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E39.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E39.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E39.5 | ACT-001 | Chủ tài khoản mở link xác minh đã nhận. | L1 gửi 09:00, mở 09:10; A01 NONE | E39.6 | FR-M01-02.01 |
| E39.6 | SYSTEM | Hệ thống từ chối dùng link này; giữ mức xác minh hiện có, không chuyển ngược mức. Nếu còn NONE, có thể khởi tạo gửi lại theo SC-M01-001. | L1 gửi 09:00, mở 10:01 | END:REJECTED | FR-M01-02.03, BR-M01-38 |


**E40: Đăng ký email; tại bước xác minh chọn mở link đã nhận; Link đã dùng.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E40 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E40.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E40.2 | FR-M01-01.01 |
| E40.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E40.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E40.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E40.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E40.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E40.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E40.5 | ACT-001 | Chủ tài khoản mở link xác minh đã nhận. | L1 gửi 09:00, mở 09:10; A01 NONE | E40.6 | FR-M01-02.01 |
| E40.6 | SYSTEM | Hệ thống từ chối dùng link này; giữ mức xác minh hiện có, không chuyển ngược mức. Nếu còn NONE, có thể khởi tạo gửi lại theo SC-M01-001. | L1 đã xác minh trước đó; mở lần hai | END:REJECTED | FR-M01-02.06, BR-M01-38 |


**E41: Đăng ký email; tại bước xác minh chọn mở link đã nhận; Link cũ bị thay thế.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E41 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E41.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E41.2 | FR-M01-01.01 |
| E41.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E41.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E41.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E41.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E41.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E41.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E41.5 | ACT-001 | Chủ tài khoản mở link xác minh đã nhận. | L1 gửi 09:00, mở 09:10; A01 NONE | E41.6 | FR-M01-02.01 |
| E41.6 | SYSTEM | Hệ thống từ chối dùng link này; giữ mức xác minh hiện có, không chuyển ngược mức. Nếu còn NONE, có thể khởi tạo gửi lại theo SC-M01-001. | L1 bị L2 thay ở 09:05; mở L1 lúc 09:10 | END:REJECTED | FR-M01-02.07, BR-M01-38 |


**E42: Đăng ký email; tại bước xác minh chọn mở link đã nhận; Chủ tài khoản còn NONE chọn xin lại email thay vì mở link hiện tại.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E42 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E42.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E42.2 | FR-M01-01.01 |
| E42.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E42.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E42.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E42.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E42.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E42.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E42.5 | ACT-001 | Chủ tài khoản yêu cầu gửi lại khi đã đủ 60 giây từ lần gửi trước. | L1 gửi 09:00; yêu cầu 09:02 | E42.6 | FR-M01-02.04, FR-M01-02.05 |
| E42.6 | SYSTEM | Hệ thống gửi L2, làm L1 mất hiệu lực; chưa tự xác minh. | L2 gửi 09:02, còn hạn một giờ; A01 vẫn NONE | E42.7 | FR-M01-02.04, FR-M01-02.07 |
| E42.7 | ACT-001 | Chủ tài khoản mở L2 lúc 09:10. | L2 chưa dùng, chưa bị thay, thuộc A01 | E42.8 | FR-M01-02.01 |
| E42.8 | SYSTEM | Hệ thống kiểm hạn/hiệu lực, ghi nhận xác minh, không cho dùng lại link và đưa chủ tài khoản tới bước 3. | A01 EMAIL_VERIFIED; L1 đã dùng; bước thiết lập UC-M01-003 tiếp theo | E42.9 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, FR-M01-02.07, FR-M01-01.09, BR-M01-10, BR-M01-33, BR-M01-38 |
| E42.9 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E42.10 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E42.10 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E43: Đăng ký email; tại bước xác minh chọn yêu cầu gửi lại rồi mở link mới.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E43 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E43.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E43.2 | FR-M01-01.01 |
| E43.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E43.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E43.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E43.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E43.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E43.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E43.5 | ACT-001 | Chủ tài khoản yêu cầu gửi lại email xác minh. | A01; yêu cầu lúc 09:01; lần trước 09:00 | E43.6 | FR-M01-02.04 |
| E43.6 | SYSTEM | Hệ thống kiểm đủ 60 giây, gửi link L2 và làm L1 mất hiệu lực; trở về trạng thái chờ mở link. | L2 gửi 09:01, hạn một giờ; A01 vẫn NONE; L1 không còn hợp lệ | E43.7 | FR-M01-02.04, FR-M01-02.05, FR-M01-02.07, FR-M01-01.09, BR-M01-11, BR-M01-33, BR-M01-38 |
| E43.7 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E43.8 | FR-M01-02.01, BR-M01-10 |
| E43.8 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E43.9 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E43.9 | ACT-002 | Chủ tài khoản nhập username/display_name và bỏ qua ba trường tùy chọn rồi gửi. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E43.10 | FR-M01-03.01, FR-M01-03.02, BR-M01-02 |
| E43.10 | SYSTEM | Hệ thống kiểm tên, trim display_name, lưu định danh đúng quy tắc và chuyển mức xác minh sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 ACTIVE/USER/SETUP_COMPLETED; display_name là tên chính, username giữ đúng An_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E44: Đăng ký email; tại bước xác minh chọn yêu cầu gửi lại rồi mở link mới; Yêu cầu lúc 09:00:45, chưa đủ 60 giây.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-001 E44 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E44.1 | ACT-001 | Guest bắt đầu đăng ký bằng email. | Thiết bị P01; email dự định an.study@example.test | E44.2 | FR-M01-01.01 |
| E44.2 | SYSTEM | Hệ thống cung cấp bước nhập email/mật khẩu, liên kết đọc chính sách và ô đồng ý; không hỏi tuổi/ngày sinh. | Ô đồng ý: "Tôi đồng ý với Điều khoản và Chính sách quyền riêng tư. Nếu dưới 16 tuổi, tôi đã được cha mẹ hoặc người giám hộ đồng ý."; chính sách P2.0; không tự ghi đồng ý | E44.3 | FR-M01-01.04, FR-M01-01.13, FR-M01-01.15 |
| E44.3 | ACT-001 | Guest nhập email, mật khẩu giả lập và đánh dấu ô đồng ý rồi gửi. | an.study@example.test; password="  Mật khẩu 2026  "; consent=true | E44.4 | FR-M01-01.01, FR-M01-01.11, FR-M01-01.13, BR-M01-35 |
| E44.4 | SYSTEM | Hệ thống kiểm dữ liệu/công tắc, tạo A01 ACTIVE/NONE vai trò USER; lưu thời điểm và phiên bản đồng ý; gửi link xác minh tới email. | A01; P2.0 đồng ý 06/11/2026 09:00 +07; L1 gửi 09:00, hạn 1 giờ; chưa có username | E44.5 | FR-M01-01.01, FR-M01-01.02, FR-M01-01.03, FR-M01-01.08, FR-M01-01.10, FR-M01-01.11, FR-M01-01.12, FR-M01-01.14, BR-M01-01, BR-M01-02, BR-M01-03, BR-M01-04, BR-M01-35 |
| E44.5 | ACT-001 | Chủ tài khoản yêu cầu gửi lại email xác minh. | A01; yêu cầu lúc 09:01; lần trước 09:00 | E44.6 | FR-M01-02.04 |
| E44.6 | SYSTEM | Hệ thống từ chối gửi lúc này; không phát link mới. | Chỉ 45 giây từ lần gửi trước; A01 vẫn NONE | E44.7 | FR-M01-02.05 |
| E44.7 | ACT-001 | Sau khi đã đủ 60 giây, chủ tài khoản tự yêu cầu gửi lại. | Yêu cầu lại lúc 09:01:05; không tự suy ra đồng hồ đếm ngược trên UI | E44.8 | FR-M01-02.04, FR-M01-02.05, BR-M01-11 |
| E44.8 | SYSTEM | Hệ thống kiểm đủ 60 giây, gửi link L2 và làm L1 mất hiệu lực; trở về trạng thái chờ mở link. | L2 gửi 09:01, hạn một giờ; A01 vẫn NONE; L1 không còn hợp lệ | E44.9 | FR-M01-02.04, FR-M01-02.05, FR-M01-02.07, FR-M01-01.09, BR-M01-11, BR-M01-33, BR-M01-38 |
| E44.9 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E44.10 | FR-M01-02.01, BR-M01-10 |
| E44.10 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E44.11 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E44.11 | ACT-002 | Chủ tài khoản nhập username/display_name và bỏ qua ba trường tùy chọn rồi gửi. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E44.12 | FR-M01-03.01, FR-M01-03.02, BR-M01-02 |
| E44.12 | SYSTEM | Hệ thống kiểm tên, trim display_name, lưu định danh đúng quy tắc và chuyển mức xác minh sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 ACTIVE/USER/SETUP_COMPLETED; display_name là tên chính, username giữ đúng An_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**Ghi chú đường đi và giới hạn:** Luồng chính hoàn tất mục tiêu; các trường hợp trong mục 6 là đường thay thế, không chạy nối tiếp tất cả nhánh. Guard mô tả dữ liệu/ngữ cảnh thay thế của chính lần thực thi. Nhánh sửa gửi lại áp cùng điều kiện kiểm tra; không có giới hạn thử mới ngoài nguồn. Các GAP ở mục cuối vẫn áp dụng.

<!-- sc:end SC-M01-001 -->

<!-- sc:scenario SC-M01-007 -->

<a id="sc-m01-007"></a>

### SC-M01-007 — Đăng nhập và hoàn tất điều kiện để truy cập iShare

#### 1. Tên kịch bản chuẩn

**Đăng nhập và hoàn tất điều kiện để truy cập iShare** — BF-M01-007; UC owner: [UC-M01-005](../../us/US-M01.md#uc-m01-005); nhóm chi tiết: UC-M01-021. Trigger: Guest gửi email và mật khẩu để đăng nhập.

#### 2. Actor thực hiện

ACT-001 Guest khởi tạo; cùng con người chuyển ACT-002 sau khi có phiên, hoặc ACT-003 đúng vai trò. ACT-004 hỗ trợ phương thức Google; ACT-005 hỗ trợ xác minh email khi tiếp tục đăng ký.

#### 3. Tiền điều kiện

Thiết bị P01 chưa có phiên phù hợp. Tài khoản email tồn tại cho đường chuẩn; dữ liệu chuẩn ACTIVE/SETUP_COMPLETED. Trạng thái/mức xác minh/bảo trì được kiểm trong M2, không phải điều kiện bỏ qua cổng. Mật khẩu đều giả lập. Đường chuẩn đã đồng ý chính sách hiện hành; nhánh phiên bản mới triển khai quyết định trước quyền dùng tiếp. Google dùng danh tính ngoài đã xác thực; chưa chốt lỗi/hủy nhà cung cấp (GAP-007).

#### 4. Hậu điều kiện

<!-- sc:post SC-M01-007 -->

| result | condition |
|---|---|
| SUCCESS | Actor nhận quyền truy cập đúng tài khoản/vai trò sau kiểm trạng thái, mức xác minh và chính sách. Nếu đăng ký còn dở, đã xác minh/thiết lập đến SETUP_COMPLETED. Nhánh rút đồng ý bằng vô hiệu hóa kết thúc DEACTIVATED và mọi phiên, không cho truy cập. Snapshot tài khoản và hiệu ứng cụ thể ghi tại từng nhánh; ADMIN không cấp quyền tương tự cho MOD. |
| REJECTED | Đăng nhập bị từ chối, không tạo phiên mới và không tự đổi trạng thái tài khoản. Các phiên khác chịu quy tắc riêng, không bị đăng xuất chỉ bởi lần từ chối này. |
| CANCELLED | Đăng nhập không dẫn tới dùng ứng dụng: actor BANNED bấm OK hoặc từ chối chính sách rồi chọn Đăng xuất. Phiên thiết bị và lịch sử tìm kiếm kết thúc theo nhánh; không thay trạng thái tài khoản hoặc ghi đồng ý mới. |
| HANDED_OFF | Nhánh chọn Khiếu nại chuyển đúng lệnh ban sang M09 với phiên hạn chế; nhánh Google chưa có tài khoản chuyển mục tiêu sang đăng ký SC-M01-001. Không coi đã được gỡ ban hoặc đã tạo tài khoản. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M01-007 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | M2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| M2 | SYSTEM | Hệ thống xác thực email/mật khẩu, kiểm bảo trì và trạng thái trước mức xác minh; cấp phiên thiết bị P01 và cho vào ứng dụng theo quyền hiện có. | A01 ACTIVE/USER/SETUP_COMPLETED; P01 có phiên mới, truy cập hạn 1 giờ và làm mới hạn 30 ngày; L01 vẫn đăng nhập | END:SUCCESS | FR-M01-05.01, FR-M01-05.12, BR-M01-16, BR-M01-17, BR-M01-18 |


#### 6. Các ngoại lệ

<!-- sc:exceptions SC-M01-007 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Email hoặc mật khẩu không đúng | E1.1 | FR-M01-05.02 |
| E2 | system | M2 | Email thuộc tài khoản chỉ Google | E2.1 | FR-M01-05.13, BR-M01-15 |
| E3 | system | M2 | Tài khoản DEACTIVATED | E3.1 | FR-M01-05.01, FR-M01-05.04, BR-M01-18 |
| E4 | system | M2 | Tài khoản DELETED | E4.1 | FR-M01-05.03, FR-M01-12.04, BR-M01-18 |
| E5 | system | M2 | Bảo trì bật và không phải ADMIN | E5.1 | FR-M01-05.19, BR-M01-37 |
| E6 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh | E6.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.10, BR-M01-18, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, BR-M01-02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |
| E7 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Email hoặc mật khẩu không đúng | E7.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E8 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Email thuộc tài khoản chỉ Google | E8.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.13, BR-M01-15 |
| E9 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Tài khoản DEACTIVATED | E9.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.04, BR-M01-18 |
| E10 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Tài khoản DELETED | E10.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.03, FR-M01-12.04, BR-M01-18 |
| E11 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Bảo trì bật và không phải ADMIN | E11.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.19, BR-M01-37 |
| E12 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Link xác minh quá 1 giờ | E12.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.10, BR-M01-18, FR-M01-02.01, BR-M01-10, FR-M01-02.03, FR-M01-02.06, FR-M01-02.07, BR-M01-38, FR-M01-02.04, FR-M01-02.05, FR-M01-02.02, FR-M01-03.01, FR-M01-03.02, BR-M01-02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |
| E13 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Link xác minh bị thay bởi lần gửi mới | E13.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.10, BR-M01-18, FR-M01-02.01, BR-M01-10, FR-M01-02.03, FR-M01-02.06, FR-M01-02.07, BR-M01-38, FR-M01-02.04, FR-M01-02.05, FR-M01-02.02, FR-M01-03.01, FR-M01-03.02, BR-M01-02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |
| E14 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Link xác minh đã được dùng trước lần mở này | E14.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.10, BR-M01-18, FR-M01-02.01, BR-M01-10, FR-M01-02.06, BR-M01-38 |
| E15 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Thiếu username hoặc display_name | E15.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.10, BR-M01-18, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, BR-M01-02, FR-M01-03.04, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07 |
| E16 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Username ngoài độ dài hoặc tập ký tự cho phép | E16.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.10, BR-M01-18, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, BR-M01-02, FR-M01-03.05, BR-M01-05, BR-M01-06, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07 |
| E17 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED | E17.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.10, BR-M01-18, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, BR-M01-02, FR-M01-03.06, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07 |
| E18 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Display_name sau trim rỗng hoặc quá 50 ký tự | E18.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.10, BR-M01-18, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, BR-M01-02, FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.14, BR-M01-07 |
| E19 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Display_name chứa ký tự không được nhận | E19.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.10, BR-M01-18, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, BR-M01-02, FR-M01-03.14, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, BR-M01-07 |
| E20 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập | E20.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |
| E21 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Email hoặc mật khẩu không đúng | E21.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E22 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Email thuộc tài khoản chỉ Google | E22.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.13, BR-M01-15 |
| E23 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Tài khoản DEACTIVATED | E23.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.04, BR-M01-18 |
| E24 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Tài khoản DELETED | E24.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.03, FR-M01-12.04, BR-M01-18 |
| E25 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Bảo trì bật và không phải ADMIN | E25.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.19, BR-M01-37 |
| E26 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Thiếu username hoặc display_name | E26.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.04, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M01-01.09, BR-M01-33 |
| E27 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Username ngoài độ dài hoặc tập ký tự cho phép | E27.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.05, BR-M01-05, BR-M01-06, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M01-01.09, BR-M01-33 |
| E28 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED | E28.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.06, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M01-01.09, BR-M01-33 |
| E29 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Display_name sau trim rỗng hoặc quá 50 ký tự | E29.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.14, BR-M01-07, FR-M01-01.09, BR-M01-33 |
| E30 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Display_name chứa ký tự không được nhận | E30.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.14, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, BR-M01-07, FR-M01-01.09, BR-M01-33 |
| E31 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Yêu cầu không có phiên đăng nhập | E31.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.09 |
| E32 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa còn hạn khiếu nại | E32.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.05, FR-M01-05.06, FR-M01-05.07, FR-M01-05.08, BR-M01-18, BR-M01-19, BR-M09-04, BR-M09-07, FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, FR-M06-05.10, BR-M06-20 |
| E33 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa còn hạn khiếu nại; Email hoặc mật khẩu không đúng | E33.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E34 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa còn hạn khiếu nại; Email thuộc tài khoản chỉ Google | E34.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.13, BR-M01-15 |
| E35 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa còn hạn khiếu nại; Tài khoản DEACTIVATED | E35.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.04, BR-M01-18 |
| E36 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa còn hạn khiếu nại; Tài khoản DELETED | E36.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.03, FR-M01-12.04, BR-M01-18 |
| E37 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa còn hạn khiếu nại; Bảo trì bật và không phải ADMIN | E37.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.19, BR-M01-37 |
| E38 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa đã hết hạn khiếu nại | E38.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.05, FR-M01-05.06, FR-M01-05.07, FR-M01-05.09, BR-M01-18, BR-M01-19, BR-M09-04, FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, FR-M06-05.10, BR-M06-20 |
| E39 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa đã hết hạn khiếu nại; Email hoặc mật khẩu không đúng | E39.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E40 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa đã hết hạn khiếu nại; Email thuộc tài khoản chỉ Google | E40.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.13, BR-M01-15 |
| E41 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa đã hết hạn khiếu nại; Tài khoản DEACTIVATED | E41.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.04, BR-M01-18 |
| E42 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa đã hết hạn khiếu nại; Tài khoản DELETED | E42.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.03, FR-M01-12.04, BR-M01-18 |
| E43 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa đã hết hạn khiếu nại; Bảo trì bật và không phải ADMIN | E43.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.19, BR-M01-37 |
| E44 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập email khi hệ thống bảo trì | E44.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.12, FR-M01-05.19, BR-M01-16, BR-M01-17, BR-M01-18, BR-M01-37 |
| E45 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập email khi hệ thống bảo trì; Email hoặc mật khẩu không đúng | E45.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E46 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập email khi hệ thống bảo trì; Email thuộc tài khoản chỉ Google | E46.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.13, BR-M01-15 |
| E47 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập email khi hệ thống bảo trì; Tài khoản DEACTIVATED | E47.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.04, BR-M01-18 |
| E48 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập email khi hệ thống bảo trì; Tài khoản DELETED | E48.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.03, FR-M01-12.04, BR-M01-18 |
| E49 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập email khi hệ thống bảo trì; Bảo trì bật và không phải ADMIN | E49.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.19, BR-M01-37 |
| E50 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập tài khoản bị khóa và mở đường khiếu nại | E50.1 | FR-M01-05.01, FR-M01-05.05, FR-M01-05.06, FR-M01-05.07, FR-M01-05.08, BR-M01-19, BR-M09-04, BR-M09-07, FR-M09-01.05, BR-M09-08 |
| E51 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập tài khoản bị khóa và mở đường khiếu nại; Chủ tài khoản chọn OK để thoát thay vì Khiếu nại | E51.1 | FR-M01-05.01, FR-M01-05.05, FR-M01-05.06, FR-M01-05.07, FR-M01-05.08, BR-M01-19, BR-M09-04, BR-M09-07, FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, FR-M06-05.10 |
| E52 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập tài khoản Google đã hoàn tất thiết lập | E52.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.08, FR-M01-05.01, FR-M01-05.12, FR-M01-05.19, BR-M01-16, BR-M01-17, BR-M01-18, BR-M01-37 |
| E53 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập tài khoản Google đã hoàn tất thiết lập; Cổng nhận tài khoản DEACTIVATED | E53.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.04, BR-M01-18 |
| E54 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập tài khoản Google đã hoàn tất thiết lập; Cổng nhận snapshot DELETED | E54.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.08, BR-M01-18, BR-M01-21 |
| E55 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập tài khoản Google đã hoàn tất thiết lập; Bảo trì bật và người đăng nhập không phải ADMIN | E55.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.19, BR-M01-37 |
| E56 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập tài khoản Google đã hoàn tất thiết lập; Email Google chưa thuộc tài khoản nào | E56.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08 |
| E57 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo | E57.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.08, FR-M01-04.09, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |
| E58 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Cổng nhận tài khoản DEACTIVATED | E58.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.04, BR-M01-18 |
| E59 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Cổng nhận snapshot DELETED | E59.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.08, BR-M01-18, BR-M01-21 |
| E60 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Bảo trì bật và người đăng nhập không phải ADMIN | E60.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.19, BR-M01-37 |
| E61 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Email Google chưa thuộc tài khoản nào | E61.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08 |
| E62 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Thiếu username hoặc display_name | E62.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.08, FR-M01-04.09, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.04, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M01-01.09, BR-M01-33 |
| E63 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Username ngoài độ dài hoặc tập ký tự cho phép | E63.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.08, FR-M01-04.09, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.05, BR-M01-05, BR-M01-06, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M01-01.09, BR-M01-33 |
| E64 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED | E64.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.08, FR-M01-04.09, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.06, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M01-01.09, BR-M01-33 |
| E65 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Display_name sau trim rỗng hoặc quá 50 ký tự | E65.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.08, FR-M01-04.09, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.14, BR-M01-07, FR-M01-01.09, BR-M01-33 |
| E66 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Display_name chứa ký tự không được nhận | E66.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.08, FR-M01-04.09, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.14, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, BR-M01-07, FR-M01-01.09, BR-M01-33 |
| E67 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Yêu cầu không có phiên đăng nhập | E67.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.08, FR-M01-04.09, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.09 |
| E68 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh | E68.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09 |
| E69 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Cổng nhận tài khoản DEACTIVATED | E69.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.04, BR-M01-18 |
| E70 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Cổng nhận snapshot DELETED | E70.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.08, BR-M01-18, BR-M01-21 |
| E71 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Bảo trì bật và người đăng nhập không phải ADMIN | E71.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.19, BR-M01-37 |
| E72 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Email Google chưa thuộc tài khoản nào | E72.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08 |
| E73 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Thiếu username hoặc display_name | E73.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.04, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M01-01.09 |
| E74 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Username ngoài độ dài hoặc tập ký tự cho phép | E74.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.05, BR-M01-05, BR-M01-06, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M01-01.09 |
| E75 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED | E75.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.06, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M01-01.09 |
| E76 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Display_name sau trim rỗng hoặc quá 50 ký tự | E76.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.14, BR-M01-07, FR-M01-01.09 |
| E77 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Display_name chứa ký tự không được nhận | E77.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.14, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, BR-M01-07, FR-M01-01.09 |
| E78 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Yêu cầu không có phiên đăng nhập | E78.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.09 |
| E79 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập | E79.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09 |
| E80 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Cổng nhận tài khoản DEACTIVATED | E80.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.04, BR-M01-18 |
| E81 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Cổng nhận snapshot DELETED | E81.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.08, BR-M01-18, BR-M01-21 |
| E82 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Bảo trì bật và người đăng nhập không phải ADMIN | E82.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.19, BR-M01-37 |
| E83 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Email Google chưa thuộc tài khoản nào | E83.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08 |
| E84 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Thiếu username hoặc display_name | E84.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.04, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M01-01.09 |
| E85 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Username ngoài độ dài hoặc tập ký tự cho phép | E85.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.05, BR-M01-05, BR-M01-06, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M01-01.09 |
| E86 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED | E86.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.06, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-07, FR-M01-01.09 |
| E87 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Display_name sau trim rỗng hoặc quá 50 ký tự | E87.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.14, BR-M01-07, FR-M01-01.09 |
| E88 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Display_name chứa ký tự không được nhận | E88.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.14, BR-M01-05, BR-M01-06, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, BR-M01-07, FR-M01-01.09 |
| E89 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Yêu cầu không có phiên đăng nhập | E89.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18, FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02, FR-M01-03.09 |
| E90 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã thiết lập | E90.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.08, FR-M01-05.01, FR-M01-05.12, FR-M01-05.19, BR-M01-16, BR-M01-17, BR-M01-18, BR-M01-37 |
| E91 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã thiết lập; Cổng nhận tài khoản DEACTIVATED | E91.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.04, BR-M01-18 |
| E92 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã thiết lập; Cổng nhận snapshot DELETED | E92.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.08, BR-M01-18, BR-M01-21 |
| E93 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã thiết lập; Bảo trì bật và người đăng nhập không phải ADMIN | E93.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.19, BR-M01-37 |
| E94 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã thiết lập; Email Google chưa thuộc tài khoản nào | E94.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08 |
| E95 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google tài khoản bị khóa còn hạn khiếu nại | E95.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.08, FR-M01-05.05, FR-M01-05.06, FR-M01-05.07, FR-M01-05.08, BR-M01-18, BR-M01-19, BR-M09-04, FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, FR-M06-05.10, BR-M06-20 |
| E96 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google tài khoản bị khóa còn hạn khiếu nại; Cổng nhận tài khoản DEACTIVATED | E96.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.04, BR-M01-18 |
| E97 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google tài khoản bị khóa còn hạn khiếu nại; Cổng nhận snapshot DELETED | E97.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.08, BR-M01-18, BR-M01-21 |
| E98 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google tài khoản bị khóa còn hạn khiếu nại; Bảo trì bật và người đăng nhập không phải ADMIN | E98.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.19, BR-M01-37 |
| E99 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google tài khoản bị khóa còn hạn khiếu nại; Email Google chưa thuộc tài khoản nào | E99.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08 |
| E100 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: Đăng nhập Google tài khoản bị khóa còn hạn khiếu nại; Tài khoản vẫn BANNED nhưng thời hạn khiếu nại đã hết | E100.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.08, FR-M01-05.05, FR-M01-05.07, FR-M01-05.09, BR-M01-19, BR-M09-04 |
| E101 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập Google trong bảo trì | E101.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.08, FR-M01-05.01, FR-M01-05.12, FR-M01-05.19, BR-M01-16, BR-M01-17, BR-M01-18, BR-M01-37 |
| E102 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập Google trong bảo trì; Cổng nhận tài khoản DEACTIVATED | E102.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.04, BR-M01-18 |
| E103 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập Google trong bảo trì; Cổng nhận snapshot DELETED | E103.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.08, BR-M01-18, BR-M01-21 |
| E104 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập Google trong bảo trì; Bảo trì bật và người đăng nhập không phải ADMIN | E104.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-05.19, BR-M01-37 |
| E105 | user-choice | M1 | Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập Google trong bảo trì; Email Google chưa thuộc tài khoản nào | E105.1 | FR-M01-04.06, FR-M01-04.04, FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08 |
| E106 | system | M2 | Tại cổng đăng nhập, tài khoản ACTIVE/NONE yêu cầu bước thiết lập trước xác minh | E106.1 | FR-M01-03.08, FR-M01-02.01, BR-M01-10, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38, FR-M01-03.01, FR-M01-03.02, BR-M01-02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |
| E107 | user-choice | M1 | Đăng nhập ACTIVE/SETUP_COMPLETED; phiên bản chính sách mới hơn bản đã đồng ý; Đồng ý phiên bản chính sách mới | E107.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.12, BR-M01-16, BR-M01-17, BR-M01-18, FR-M01-16.01, BR-M01-44, FR-M01-16.02 |
| E108 | user-choice | M1 | Đăng nhập ACTIVE/SETUP_COMPLETED; phiên bản chính sách mới hơn bản đã đồng ý; Từ chối chính sách mới rồi đăng xuất | E108.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.12, BR-M01-16, BR-M01-17, BR-M01-18, FR-M01-16.01, BR-M01-44, FR-M01-16.03, BR-M01-45, FR-M01-07.01, FR-M01-07.02, FR-M01-16.04, FR-M06-05.10 |
| E109 | user-choice | M1 | Đăng nhập ACTIVE/SETUP_COMPLETED; phiên bản chính sách mới hơn bản đã đồng ý; Từ chối chính sách mới rồi vô hiệu hóa | E109.1 | FR-M01-05.01, FR-M01-05.02, BR-M01-35, FR-M01-05.12, BR-M01-16, BR-M01-17, BR-M01-18, FR-M01-16.01, BR-M01-44, FR-M01-16.03, BR-M01-45, FR-M01-10.01, FR-M01-10.02, FR-M01-10.07, FR-M01-13.01, FR-M01-13.03, BR-M01-21 |


**E1: Email hoặc mật khẩu không đúng.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối đăng nhập, không tạo phiên mới. | email=an.study@example.test; mật khẩu sai="khongdung" | END:REJECTED | FR-M01-05.02 |


**E2: Email thuộc tài khoản chỉ Google.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối đăng nhập bằng mật khẩu cho tài khoản Google. | A02 được tạo bằng Google, không có mật khẩu iShare | END:REJECTED | FR-M01-05.13, BR-M01-15 |


**E3: Tài khoản DEACTIVATED.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối đăng nhập; không tự kích hoạt lại. | A01 DEACTIVATED giữ nguyên; không cấp phiên mới | END:REJECTED | FR-M01-05.01, FR-M01-05.04, BR-M01-18 |


**E4: Tài khoản DELETED.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối đăng nhập, không phục hồi tài khoản. | Snapshot tài khoản đã xóa; không tìm/khôi phục mật khẩu đã xóa để xác thực | END:REJECTED | FR-M01-05.03, FR-M01-12.04, BR-M01-18 |


**E5: Bảo trì bật và không phải ADMIN.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối đăng nhập dù thông tin đúng. | maintenance=true; role=USER hoặc MOD; không tạo phiên | END:REJECTED | FR-M01-05.19, BR-M01-37 |


**E6: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E6.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E6.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 2; không cho dùng chức năng đòi hoàn tất đăng ký. | A01 ACTIVE/NONE; đích bước 2, mở link theo SC-M01-001 hoặc gửi lại SC-M01-001 | E6.3 | FR-M01-05.01, FR-M01-05.10, BR-M01-18 |
| E6.3 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E6.4 | FR-M01-02.01, BR-M01-10 |
| E6.4 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E6.5 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E6.5 | ACT-002 | Chủ tài khoản nhập username/display_name và bỏ qua ba trường tùy chọn rồi gửi. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E6.6 | FR-M01-03.01, FR-M01-03.02, BR-M01-02 |
| E6.6 | SYSTEM | Hệ thống kiểm tên, trim display_name, lưu định danh đúng quy tắc và chuyển mức xác minh sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 ACTIVE/USER/SETUP_COMPLETED; display_name là tên chính, username giữ đúng An_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E7: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Email hoặc mật khẩu không đúng.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E7.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E7.2 | SYSTEM | Hệ thống từ chối đăng nhập, không tạo phiên mới. | email=an.study@example.test; mật khẩu sai="khongdung" | END:REJECTED | FR-M01-05.02 |


**E8: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Email thuộc tài khoản chỉ Google.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E8.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E8.2 | SYSTEM | Hệ thống từ chối đăng nhập bằng mật khẩu cho tài khoản Google. | A02 được tạo bằng Google, không có mật khẩu iShare | END:REJECTED | FR-M01-05.13, BR-M01-15 |


**E9: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Tài khoản DEACTIVATED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E9.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E9.2 | SYSTEM | Hệ thống từ chối đăng nhập; không tự kích hoạt lại. | A01 DEACTIVATED giữ nguyên; không cấp phiên mới | END:REJECTED | FR-M01-05.01, FR-M01-05.04, BR-M01-18 |


**E10: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Tài khoản DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E10.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E10.2 | SYSTEM | Hệ thống từ chối đăng nhập, không phục hồi tài khoản. | Snapshot tài khoản đã xóa; không tìm/khôi phục mật khẩu đã xóa để xác thực | END:REJECTED | FR-M01-05.03, FR-M01-12.04, BR-M01-18 |


**E11: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Bảo trì bật và không phải ADMIN.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E11.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E11.2 | SYSTEM | Hệ thống từ chối đăng nhập dù thông tin đúng. | maintenance=true; role=USER hoặc MOD; không tạo phiên | END:REJECTED | FR-M01-05.19, BR-M01-37 |


**E12: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Link xác minh quá 1 giờ.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E12.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E12.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 2; không cho dùng chức năng đòi hoàn tất đăng ký. | A01 ACTIVE/NONE; đích bước 2, mở link theo SC-M01-001 hoặc gửi lại SC-M01-001 | E12.3 | FR-M01-05.01, FR-M01-05.10, BR-M01-18 |
| E12.3 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E12.4 | FR-M01-02.01, BR-M01-10 |
| E12.4 | SYSTEM | Hệ thống từ chối link này, chưa nâng mức xác minh; cho quay về yêu cầu gửi lại. | A01 vẫn NONE; link lỗi L-old | E12.5 | FR-M01-02.03, FR-M01-02.06, FR-M01-02.07, BR-M01-38 |
| E12.5 | ACT-001 | Chủ tài khoản yêu cầu gửi lại khi đã cách lần gửi trước ít nhất 60 giây. | Lần gửi trước 09:00; yêu cầu 10:05 | E12.6 | FR-M01-02.04, FR-M01-02.05 |
| E12.6 | SYSTEM | Hệ thống gửi link xác minh mới, vô hiệu link cũ; tài khoản vẫn NONE. | L-new gửi 10:05, hạn một giờ | E12.7 | FR-M01-02.04, FR-M01-02.07 |
| E12.7 | ACT-001 | Chủ tài khoản mở link mới chưa dùng lúc 10:10. | L-new còn hạn, thuộc A01 | E12.8 | FR-M01-02.01 |
| E12.8 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E12.9 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E12.9 | ACT-002 | Chủ tài khoản nhập username/display_name và bỏ qua ba trường tùy chọn rồi gửi. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E12.10 | FR-M01-03.01, FR-M01-03.02, BR-M01-02 |
| E12.10 | SYSTEM | Hệ thống kiểm tên, trim display_name, lưu định danh đúng quy tắc và chuyển mức xác minh sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 ACTIVE/USER/SETUP_COMPLETED; display_name là tên chính, username giữ đúng An_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E13: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Link xác minh bị thay bởi lần gửi mới.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E13.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E13.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 2; không cho dùng chức năng đòi hoàn tất đăng ký. | A01 ACTIVE/NONE; đích bước 2, mở link theo SC-M01-001 hoặc gửi lại SC-M01-001 | E13.3 | FR-M01-05.01, FR-M01-05.10, BR-M01-18 |
| E13.3 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E13.4 | FR-M01-02.01, BR-M01-10 |
| E13.4 | SYSTEM | Hệ thống từ chối link này, chưa nâng mức xác minh; cho quay về yêu cầu gửi lại. | A01 vẫn NONE; link lỗi L-old | E13.5 | FR-M01-02.03, FR-M01-02.06, FR-M01-02.07, BR-M01-38 |
| E13.5 | ACT-001 | Chủ tài khoản yêu cầu gửi lại khi đã cách lần gửi trước ít nhất 60 giây. | Lần gửi trước 09:00; yêu cầu 10:05 | E13.6 | FR-M01-02.04, FR-M01-02.05 |
| E13.6 | SYSTEM | Hệ thống gửi link xác minh mới, vô hiệu link cũ; tài khoản vẫn NONE. | L-new gửi 10:05, hạn một giờ | E13.7 | FR-M01-02.04, FR-M01-02.07 |
| E13.7 | ACT-001 | Chủ tài khoản mở link mới chưa dùng lúc 10:10. | L-new còn hạn, thuộc A01 | E13.8 | FR-M01-02.01 |
| E13.8 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E13.9 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E13.9 | ACT-002 | Chủ tài khoản nhập username/display_name và bỏ qua ba trường tùy chọn rồi gửi. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E13.10 | FR-M01-03.01, FR-M01-03.02, BR-M01-02 |
| E13.10 | SYSTEM | Hệ thống kiểm tên, trim display_name, lưu định danh đúng quy tắc và chuyển mức xác minh sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 ACTIVE/USER/SETUP_COMPLETED; display_name là tên chính, username giữ đúng An_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E14: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Link xác minh đã được dùng trước lần mở này.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E14.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E14.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 2; không cho dùng chức năng đòi hoàn tất đăng ký. | A01 ACTIVE/NONE; đích bước 2, mở link theo SC-M01-001 hoặc gửi lại SC-M01-001 | E14.3 | FR-M01-05.01, FR-M01-05.10, BR-M01-18 |
| E14.3 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E14.4 | FR-M01-02.01, BR-M01-10 |
| E14.4 | SYSTEM | Hệ thống từ chối dùng lại; giữ mức xác minh hiện có, không hạ về NONE hoặc yêu cầu lại bước đã hoàn tất. | L1 đã dùng; A01 có thể đã EMAIL_VERIFIED hoặc SETUP_COMPLETED | END:REJECTED | FR-M01-02.06, BR-M01-38 |


**E15: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Thiếu username hoặc display_name.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E15.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E15.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 2; không cho dùng chức năng đòi hoàn tất đăng ký. | A01 ACTIVE/NONE; đích bước 2, mở link theo SC-M01-001 hoặc gửi lại SC-M01-001 | E15.3 | FR-M01-05.01, FR-M01-05.10, BR-M01-18 |
| E15.3 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E15.4 | FR-M01-02.01, BR-M01-10 |
| E15.4 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E15.5 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E15.5 | ACT-002 | Chủ tài khoản nhập username/display_name và bỏ qua ba trường tùy chọn rồi gửi. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E15.6 | FR-M01-03.01, FR-M01-03.02, BR-M01-02 |
| E15.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="" hoặc display_name="" | E15.7 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E15.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E15.8 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E15.8 | SYSTEM | Hệ thống kiểm tên, trim display_name, lưu định danh đúng quy tắc và chuyển mức xác minh sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 ACTIVE/USER/SETUP_COMPLETED; display_name là tên chính, username giữ đúng An_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E16: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Username ngoài độ dài hoặc tập ký tự cho phép.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E16 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E16.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E16.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E16.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 2; không cho dùng chức năng đòi hoàn tất đăng ký. | A01 ACTIVE/NONE; đích bước 2, mở link theo SC-M01-001 hoặc gửi lại SC-M01-001 | E16.3 | FR-M01-05.01, FR-M01-05.10, BR-M01-18 |
| E16.3 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E16.4 | FR-M01-02.01, BR-M01-10 |
| E16.4 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E16.5 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E16.5 | ACT-002 | Chủ tài khoản nhập username/display_name và bỏ qua ba trường tùy chọn rồi gửi. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E16.6 | FR-M01-03.01, FR-M01-03.02, BR-M01-02 |
| E16.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="ab", hoặc "a"×21, hoặc "an.hoc" | E16.7 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E16.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E16.8 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E16.8 | SYSTEM | Hệ thống kiểm tên, trim display_name, lưu định danh đúng quy tắc và chuyển mức xác minh sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 ACTIVE/USER/SETUP_COMPLETED; display_name là tên chính, username giữ đúng An_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E17: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E17 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E17.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E17.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E17.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 2; không cho dùng chức năng đòi hoàn tất đăng ký. | A01 ACTIVE/NONE; đích bước 2, mở link theo SC-M01-001 hoặc gửi lại SC-M01-001 | E17.3 | FR-M01-05.01, FR-M01-05.10, BR-M01-18 |
| E17.3 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E17.4 | FR-M01-02.01, BR-M01-10 |
| E17.4 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E17.5 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E17.5 | ACT-002 | Chủ tài khoản nhập username/display_name và bỏ qua ba trường tùy chọn rồi gửi. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E17.6 | FR-M01-03.01, FR-M01-03.02, BR-M01-02 |
| E17.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | An_12A1 trùng an_12a1; hoặc Cuong trùng username DELETED cuong | E17.7 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E17.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E17.8 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E17.8 | SYSTEM | Hệ thống kiểm tên, trim display_name, lưu định danh đúng quy tắc và chuyển mức xác minh sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 ACTIVE/USER/SETUP_COMPLETED; display_name là tên chính, username giữ đúng An_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E18: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Display_name sau trim rỗng hoặc quá 50 ký tự.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E18 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E18.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E18.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E18.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 2; không cho dùng chức năng đòi hoàn tất đăng ký. | A01 ACTIVE/NONE; đích bước 2, mở link theo SC-M01-001 hoặc gửi lại SC-M01-001 | E18.3 | FR-M01-05.01, FR-M01-05.10, BR-M01-18 |
| E18.3 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E18.4 | FR-M01-02.01, BR-M01-10 |
| E18.4 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E18.5 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E18.5 | ACT-002 | Chủ tài khoản nhập username/display_name và bỏ qua ba trường tùy chọn rồi gửi. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E18.6 | FR-M01-03.01, FR-M01-03.02, BR-M01-02 |
| E18.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | "   " hoặc "A"×51 | E18.7 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E18.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E18.8 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E18.8 | SYSTEM | Hệ thống kiểm tên, trim display_name, lưu định danh đúng quy tắc và chuyển mức xác minh sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 ACTIVE/USER/SETUP_COMPLETED; display_name là tên chính, username giữ đúng An_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E19: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục bước xác minh; Display_name chứa ký tự không được nhận.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E19 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E19.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E19.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E19.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 2; không cho dùng chức năng đòi hoàn tất đăng ký. | A01 ACTIVE/NONE; đích bước 2, mở link theo SC-M01-001 hoặc gửi lại SC-M01-001 | E19.3 | FR-M01-05.01, FR-M01-05.10, BR-M01-18 |
| E19.3 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E19.4 | FR-M01-02.01, BR-M01-10 |
| E19.4 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E19.5 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E19.5 | ACT-002 | Chủ tài khoản nhập username/display_name và bỏ qua ba trường tùy chọn rồi gửi. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E19.6 | FR-M01-03.01, FR-M01-03.02, BR-M01-02 |
| E19.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | display_name="An 😊" | E19.7 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E19.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E19.8 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E19.8 | SYSTEM | Hệ thống kiểm tên, trim display_name, lưu định danh đúng quy tắc và chuyển mức xác minh sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 ACTIVE/USER/SETUP_COMPLETED; display_name là tên chính, username giữ đúng An_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E20: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E20 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E20.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E20.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E20.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 3; không coi đăng ký đã hoàn tất. | A01 ACTIVE/EMAIL_VERIFIED; đích UC-M01-003, SC-M01-001 hoặc SC-M01-001 | E20.3 | FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E20.3 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E20.4 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E20.4 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E21: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Email hoặc mật khẩu không đúng.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E21 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E21.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E21.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E21.2 | SYSTEM | Hệ thống từ chối đăng nhập, không tạo phiên mới. | email=an.study@example.test; mật khẩu sai="khongdung" | END:REJECTED | FR-M01-05.02 |


**E22: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Email thuộc tài khoản chỉ Google.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E22 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E22.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E22.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E22.2 | SYSTEM | Hệ thống từ chối đăng nhập bằng mật khẩu cho tài khoản Google. | A02 được tạo bằng Google, không có mật khẩu iShare | END:REJECTED | FR-M01-05.13, BR-M01-15 |


**E23: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Tài khoản DEACTIVATED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E23 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E23.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E23.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E23.2 | SYSTEM | Hệ thống từ chối đăng nhập; không tự kích hoạt lại. | A01 DEACTIVATED giữ nguyên; không cấp phiên mới | END:REJECTED | FR-M01-05.01, FR-M01-05.04, BR-M01-18 |


**E24: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Tài khoản DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E24 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E24.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E24.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E24.2 | SYSTEM | Hệ thống từ chối đăng nhập, không phục hồi tài khoản. | Snapshot tài khoản đã xóa; không tìm/khôi phục mật khẩu đã xóa để xác thực | END:REJECTED | FR-M01-05.03, FR-M01-12.04, BR-M01-18 |


**E25: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Bảo trì bật và không phải ADMIN.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E25 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E25.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E25.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E25.2 | SYSTEM | Hệ thống từ chối đăng nhập dù thông tin đúng. | maintenance=true; role=USER hoặc MOD; không tạo phiên | END:REJECTED | FR-M01-05.19, BR-M01-37 |


**E26: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Thiếu username hoặc display_name.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E26 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E26.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E26.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E26.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 3; không coi đăng ký đã hoàn tất. | A01 ACTIVE/EMAIL_VERIFIED; đích UC-M01-003, SC-M01-001 hoặc SC-M01-001 | E26.3 | FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E26.3 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E26.4 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E26.4 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="" hoặc display_name="" | E26.5 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E26.5 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E26.6 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E26.6 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E27: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Username ngoài độ dài hoặc tập ký tự cho phép.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E27 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E27.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E27.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E27.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 3; không coi đăng ký đã hoàn tất. | A01 ACTIVE/EMAIL_VERIFIED; đích UC-M01-003, SC-M01-001 hoặc SC-M01-001 | E27.3 | FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E27.3 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E27.4 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E27.4 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="ab", hoặc "a"×21, hoặc "an.hoc" | E27.5 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E27.5 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E27.6 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E27.6 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E28: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E28 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E28.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E28.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E28.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 3; không coi đăng ký đã hoàn tất. | A01 ACTIVE/EMAIL_VERIFIED; đích UC-M01-003, SC-M01-001 hoặc SC-M01-001 | E28.3 | FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E28.3 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E28.4 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E28.4 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | An_12A1 trùng an_12a1; hoặc Cuong trùng username DELETED cuong | E28.5 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E28.5 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E28.6 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E28.6 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E29: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Display_name sau trim rỗng hoặc quá 50 ký tự.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E29 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E29.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E29.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E29.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 3; không coi đăng ký đã hoàn tất. | A01 ACTIVE/EMAIL_VERIFIED; đích UC-M01-003, SC-M01-001 hoặc SC-M01-001 | E29.3 | FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E29.3 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E29.4 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E29.4 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | "   " hoặc "A"×51 | E29.5 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E29.5 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E29.6 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E29.6 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E30: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Display_name chứa ký tự không được nhận.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E30 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E30.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E30.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E30.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 3; không coi đăng ký đã hoàn tất. | A01 ACTIVE/EMAIL_VERIFIED; đích UC-M01-003, SC-M01-001 hoặc SC-M01-001 | E30.3 | FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E30.3 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E30.4 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E30.4 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | display_name="An 😊" | E30.5 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E30.5 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E30.6 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E30.6 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E31: Phương thức/ngữ cảnh thay thế: Đăng nhập email để tiếp tục thiết lập; Yêu cầu không có phiên đăng nhập.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E31 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E31.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E31.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E31.2 | SYSTEM | Hệ thống xác thực, áp dụng cổng rồi đưa chủ tài khoản về bước 3; không coi đăng ký đã hoàn tất. | A01 ACTIVE/EMAIL_VERIFIED; đích UC-M01-003, SC-M01-001 hoặc SC-M01-001 | E31.3 | FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E31.3 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E31.4 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E31.4 | SYSTEM | Hệ thống từ chối thiết lập; không nâng mức xác minh. | Không có phiên; giữ dữ liệu tài khoản trước yêu cầu | END:REJECTED | FR-M01-03.09 |


**E32: Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa còn hạn khiếu nại.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E32 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E32.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E32.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E32.2 | SYSTEM | Hệ thống xác thực, cấp phiên hạn chế và chỉ mở màn hình tài khoản bị khóa; hiển thị lý do, OK, thời gian còn lại và nút Khiếu nại; mọi thao tác khác ngoài phạm vi được phép bị chặn. | A03 bị ban vĩnh viễn lúc 01/11/2026 09:00 +07; lúc đăng nhập 06/11/2026 09:00 còn 85×24 giờ khiếu nại; lý do minh họa vi phạm quy tắc; OK và Khiếu nại có sẵn | E32.3 | FR-M01-05.01, FR-M01-05.05, FR-M01-05.06, FR-M01-05.07, FR-M01-05.08, BR-M01-18, BR-M01-19, BR-M09-04, BR-M09-07 |
| E32.3 | ACT-002 | Chủ tài khoản bấm OK trên màn hình tài khoản bị khóa. | P01; lịch sử tìm kiếm trình duyệt [đạo hàm, hình học]; L01 có phiên riêng | E32.4 | FR-M01-05.07, FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, BR-M01-19 |
| E32.4 | SYSTEM | Hệ thống kết thúc phiên truy cập và phiên làm mới P01; giữ các phiên thiết bị khác; xóa toàn bộ lịch sử tìm kiếm trên trình duyệt P01. | P01 không còn phiên; lịch sử=[]; L01 giữ nguyên; nếu chưa đồng ý P2.0 thì lần mở sau vẫn phải hỏi | END:CANCELLED | FR-M01-05.07, FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, BR-M01-19, FR-M06-05.10, BR-M06-20 |


**E33: Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa còn hạn khiếu nại; Email hoặc mật khẩu không đúng.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E33 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E33.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E33.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E33.2 | SYSTEM | Hệ thống từ chối đăng nhập, không tạo phiên mới. | email=an.study@example.test; mật khẩu sai="khongdung" | END:REJECTED | FR-M01-05.02 |


**E34: Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa còn hạn khiếu nại; Email thuộc tài khoản chỉ Google.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E34 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E34.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E34.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E34.2 | SYSTEM | Hệ thống từ chối đăng nhập bằng mật khẩu cho tài khoản Google. | A02 được tạo bằng Google, không có mật khẩu iShare | END:REJECTED | FR-M01-05.13, BR-M01-15 |


**E35: Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa còn hạn khiếu nại; Tài khoản DEACTIVATED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E35 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E35.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E35.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E35.2 | SYSTEM | Hệ thống từ chối đăng nhập; không tự kích hoạt lại. | A01 DEACTIVATED giữ nguyên; không cấp phiên mới | END:REJECTED | FR-M01-05.01, FR-M01-05.04, BR-M01-18 |


**E36: Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa còn hạn khiếu nại; Tài khoản DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E36 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E36.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E36.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E36.2 | SYSTEM | Hệ thống từ chối đăng nhập, không phục hồi tài khoản. | Snapshot tài khoản đã xóa; không tìm/khôi phục mật khẩu đã xóa để xác thực | END:REJECTED | FR-M01-05.03, FR-M01-12.04, BR-M01-18 |


**E37: Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa còn hạn khiếu nại; Bảo trì bật và không phải ADMIN.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E37 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E37.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E37.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E37.2 | SYSTEM | Hệ thống từ chối đăng nhập dù thông tin đúng. | maintenance=true; role=USER hoặc MOD; không tạo phiên | END:REJECTED | FR-M01-05.19, BR-M01-37 |


**E38: Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa đã hết hạn khiếu nại.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E38 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E38.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E38.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E38.2 | SYSTEM | Hệ thống xác thực, cấp phiên hạn chế và chỉ hiển thị lý do ban cùng OK; ẩn thời gian còn lại và nút Khiếu nại. | A03 ban vĩnh viễn từ 01/07/2026 09:00 +07, hiện 06/11/2026; không còn thời gian/nút Khiếu nại; chỉ OK để thoát | E38.3 | FR-M01-05.01, FR-M01-05.05, FR-M01-05.06, FR-M01-05.07, FR-M01-05.09, BR-M01-18, BR-M01-19, BR-M09-04 |
| E38.3 | ACT-002 | Chủ tài khoản bấm OK trên màn hình tài khoản bị khóa. | P01; lịch sử tìm kiếm trình duyệt [đạo hàm, hình học]; L01 có phiên riêng | E38.4 | FR-M01-05.07, FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, BR-M01-19 |
| E38.4 | SYSTEM | Hệ thống kết thúc phiên truy cập và phiên làm mới P01; giữ các phiên thiết bị khác; xóa toàn bộ lịch sử tìm kiếm trên trình duyệt P01. | P01 không còn phiên; lịch sử=[]; L01 giữ nguyên; nếu chưa đồng ý P2.0 thì lần mở sau vẫn phải hỏi | END:CANCELLED | FR-M01-05.07, FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, BR-M01-19, FR-M06-05.10, BR-M06-20 |


**E39: Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa đã hết hạn khiếu nại; Email hoặc mật khẩu không đúng.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E39 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E39.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E39.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E39.2 | SYSTEM | Hệ thống từ chối đăng nhập, không tạo phiên mới. | email=an.study@example.test; mật khẩu sai="khongdung" | END:REJECTED | FR-M01-05.02 |


**E40: Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa đã hết hạn khiếu nại; Email thuộc tài khoản chỉ Google.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E40 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E40.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E40.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E40.2 | SYSTEM | Hệ thống từ chối đăng nhập bằng mật khẩu cho tài khoản Google. | A02 được tạo bằng Google, không có mật khẩu iShare | END:REJECTED | FR-M01-05.13, BR-M01-15 |


**E41: Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa đã hết hạn khiếu nại; Tài khoản DEACTIVATED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E41 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E41.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E41.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E41.2 | SYSTEM | Hệ thống từ chối đăng nhập; không tự kích hoạt lại. | A01 DEACTIVATED giữ nguyên; không cấp phiên mới | END:REJECTED | FR-M01-05.01, FR-M01-05.04, BR-M01-18 |


**E42: Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa đã hết hạn khiếu nại; Tài khoản DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E42 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E42.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E42.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E42.2 | SYSTEM | Hệ thống từ chối đăng nhập, không phục hồi tài khoản. | Snapshot tài khoản đã xóa; không tìm/khôi phục mật khẩu đã xóa để xác thực | END:REJECTED | FR-M01-05.03, FR-M01-12.04, BR-M01-18 |


**E43: Phương thức/ngữ cảnh thay thế: Đăng nhập email tài khoản bị khóa đã hết hạn khiếu nại; Bảo trì bật và không phải ADMIN.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E43 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E43.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E43.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E43.2 | SYSTEM | Hệ thống từ chối đăng nhập dù thông tin đúng. | maintenance=true; role=USER hoặc MOD; không tạo phiên | END:REJECTED | FR-M01-05.19, BR-M01-37 |


**E44: Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập email khi hệ thống bảo trì.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E44 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E44.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E44.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E44.2 | SYSTEM | Hệ thống xác thực, nhận diện đúng vai trò ADMIN, áp dụng cổng trạng thái/mức xác minh và cấp phiên cho thiết bị; cho thao tác trong quyền ADMIN. | A04 ACTIVE/ADMIN/SETUP_COMPLETED; maintenance=true; P01 có phiên mới độc lập; không áp quyền này cho MOD | END:SUCCESS | FR-M01-05.01, FR-M01-05.12, FR-M01-05.19, BR-M01-16, BR-M01-17, BR-M01-18, BR-M01-37 |


**E45: Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập email khi hệ thống bảo trì; Email hoặc mật khẩu không đúng.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E45 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E45.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E45.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E45.2 | SYSTEM | Hệ thống từ chối đăng nhập, không tạo phiên mới. | email=an.study@example.test; mật khẩu sai="khongdung" | END:REJECTED | FR-M01-05.02 |


**E46: Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập email khi hệ thống bảo trì; Email thuộc tài khoản chỉ Google.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E46 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E46.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E46.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E46.2 | SYSTEM | Hệ thống từ chối đăng nhập bằng mật khẩu cho tài khoản Google. | A02 được tạo bằng Google, không có mật khẩu iShare | END:REJECTED | FR-M01-05.13, BR-M01-15 |


**E47: Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập email khi hệ thống bảo trì; Tài khoản DEACTIVATED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E47 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E47.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E47.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E47.2 | SYSTEM | Hệ thống từ chối đăng nhập; không tự kích hoạt lại. | A01 DEACTIVATED giữ nguyên; không cấp phiên mới | END:REJECTED | FR-M01-05.01, FR-M01-05.04, BR-M01-18 |


**E48: Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập email khi hệ thống bảo trì; Tài khoản DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E48 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E48.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E48.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E48.2 | SYSTEM | Hệ thống từ chối đăng nhập, không phục hồi tài khoản. | Snapshot tài khoản đã xóa; không tìm/khôi phục mật khẩu đã xóa để xác thực | END:REJECTED | FR-M01-05.03, FR-M01-12.04, BR-M01-18 |


**E49: Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập email khi hệ thống bảo trì; Bảo trì bật và không phải ADMIN.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E49 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E49.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E49.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E49.2 | SYSTEM | Hệ thống từ chối đăng nhập dù thông tin đúng. | maintenance=true; role=USER hoặc MOD; không tạo phiên | END:REJECTED | FR-M01-05.19, BR-M01-37 |


**E50: Phương thức/ngữ cảnh thay thế: Đăng nhập tài khoản bị khóa và mở đường khiếu nại.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E50 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E50.1 | ACT-001 | Guest gửi email và mật khẩu đúng của A03. | a03.study@example.test; P01 | E50.2 | FR-M01-05.01 |
| E50.2 | SYSTEM | Hệ thống tạo phiên hạn chế, mở màn hình bị khóa với lý do, OK, thời gian còn lại và nút Khiếu nại. | BANNED; còn 85×24 giờ; chỉ khiếu nại/đăng xuất theo quyền | E50.3 | FR-M01-05.05, FR-M01-05.06, FR-M01-05.07, FR-M01-05.08, BR-M01-19, BR-M09-04, BR-M09-07 |
| E50.3 | ACT-002 | Chủ tài khoản chọn Khiếu nại. | Lệnh ban đang hiệu lực của chính A03 | E50.4 | FR-M01-05.08, BR-M09-07 |
| E50.4 | SYSTEM | Hệ thống mở ngữ cảnh gửi khiếu nại của M09 cho chính lệnh ban đó; giữ nguyên trạng thái BANNED và quyền hạn chế. | M09 nhận A03, lệnh ban, phiên và thời hạn; chưa có kết luận hoặc thay đổi ACTIVE | END:HANDED_OFF | FR-M01-05.06, FR-M01-05.08, FR-M09-01.05, BR-M09-07, BR-M09-08 |


**E51: Phương thức/ngữ cảnh thay thế: Đăng nhập tài khoản bị khóa và mở đường khiếu nại; Chủ tài khoản chọn OK để thoát thay vì Khiếu nại.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E51 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E51.1 | ACT-001 | Guest gửi email và mật khẩu đúng của A03. | a03.study@example.test; P01 | E51.2 | FR-M01-05.01 |
| E51.2 | SYSTEM | Hệ thống tạo phiên hạn chế, mở màn hình bị khóa với lý do, OK, thời gian còn lại và nút Khiếu nại. | BANNED; còn 85×24 giờ; chỉ khiếu nại/đăng xuất theo quyền | E51.3 | FR-M01-05.05, FR-M01-05.06, FR-M01-05.07, FR-M01-05.08, BR-M01-19, BR-M09-04, BR-M09-07 |
| E51.3 | ACT-002 | Chủ tài khoản bấm OK trên màn hình bị khóa. | A03; P01 | E51.4 | FR-M01-05.18 |
| E51.4 | SYSTEM | Hệ thống kết thúc phiên P01, giữ nguyên phiên thiết bị khác và xóa lịch sử tìm kiếm trên trình duyệt P01. | P01 không còn phiên; không mở khiếu nại; lịch sử P01 rỗng | END:CANCELLED | FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, FR-M06-05.10 |


**E52: Phương thức/ngữ cảnh thay thế: Đăng nhập tài khoản Google đã hoàn tất thiết lập.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E52 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E52.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E52.2 | FR-M01-04.06 |
| E52.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E52.3 | FR-M01-04.06 |
| E52.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E52.4 | FR-M01-04.04, FR-M01-04.06 |
| E52.4 | SYSTEM | Hệ thống áp dụng cổng trạng thái/mức xác minh, cấp phiên mới cho P01 và cho vào ứng dụng theo quyền; phiên L01 giữ riêng. | P01 phiên mới truy cập 1 giờ, làm mới 30 ngày; ACTIVE/SETUP_COMPLETED; maintenance=false | END:SUCCESS | FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.12, FR-M01-05.19, BR-M01-16, BR-M01-17, BR-M01-18, BR-M01-37 |


**E53: Phương thức/ngữ cảnh thay thế: Đăng nhập tài khoản Google đã hoàn tất thiết lập; Cổng nhận tài khoản DEACTIVATED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E53 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E53.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E53.2 | FR-M01-04.06 |
| E53.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E53.3 | FR-M01-04.06 |
| E53.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E53.4 | FR-M01-04.04, FR-M01-04.06 |
| E53.4 | SYSTEM | Hệ thống từ chối đăng nhập, giữ DEACTIVATED; không tự kích hoạt lại và không cấp phiên truy cập. Liên kết nếu đã được xử lý trước cổng không được hiểu là mở khóa tài khoản. | Trạng thái kiểm ở cổng DEACTIVATED | END:REJECTED | FR-M01-04.06, FR-M01-05.04, BR-M01-18 |


**E54: Phương thức/ngữ cảnh thay thế: Đăng nhập tài khoản Google đã hoàn tất thiết lập; Cổng nhận snapshot DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E54 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E54.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E54.2 | FR-M01-04.06 |
| E54.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E54.3 | FR-M01-04.06 |
| E54.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E54.4 | FR-M01-04.04, FR-M01-04.06 |
| E54.4 | SYSTEM | Hệ thống từ chối truy cập DELETED; không phục hồi danh tính/phiên đã xóa. Không khớp Google vào tài khoản DELETED bằng email đã bị xóa. | Nếu email Google cũ nay chưa thuộc tài khoản nào thì đi hành trình tạo mới thay vì nhận diện lại DELETED | END:REJECTED | FR-M01-04.06, FR-M01-05.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.08, BR-M01-18, BR-M01-21 |


**E55: Phương thức/ngữ cảnh thay thế: Đăng nhập tài khoản Google đã hoàn tất thiết lập; Bảo trì bật và người đăng nhập không phải ADMIN.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E55 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E55.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E55.2 | FR-M01-04.06 |
| E55.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E55.3 | FR-M01-04.06 |
| E55.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E55.4 | FR-M01-04.04, FR-M01-04.06 |
| E55.4 | SYSTEM | Hệ thống từ chối đăng nhập, không cấp phiên. Không khẳng định thứ tự thay đổi liên kết trước/sau kiểm bảo trì khi FR/US chưa thống nhất; phần này bị đánh dấu GAP-SC-M01-001. | maintenance=true; USER/MOD; nhánh quyền truy cập đã rõ, thứ tự side effect liên kết còn cần xác nhận | END:REJECTED | FR-M01-04.06, FR-M01-05.19, BR-M01-37 |


**E56: Phương thức/ngữ cảnh thay thế: Đăng nhập tài khoản Google đã hoàn tất thiết lập; Email Google chưa thuộc tài khoản nào.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E56 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E56.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E56.2 | FR-M01-04.06 |
| E56.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E56.3 | FR-M01-04.06 |
| E56.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E56.4 | FR-M01-04.04, FR-M01-04.06 |
| E56.4 | SYSTEM | Hệ thống không đăng nhập vào một tài khoản giả định đã có; chuyển danh tính sang hành trình tạo mới có kiểm đồng ý, tạm dừng đăng ký và bảo trì. | UC-M01-004 / SC-M01-001 nhận danh tính Google từ bước M3; bắt đầu ở điểm kiểm email/đồng ý; chưa tạo mới chỉ vì chọn Google | END:HANDED_OFF | FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08 |


**E57: Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E57 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E57.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E57.2 | FR-M01-04.06 |
| E57.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E57.3 | FR-M01-04.06 |
| E57.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E57.4 | FR-M01-04.04, FR-M01-04.06 |
| E57.4 | SYSTEM | Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E57.5 | FR-M01-04.06, FR-M01-04.08, FR-M01-04.09, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E57.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E57.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E57.6 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E58: Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Cổng nhận tài khoản DEACTIVATED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E58 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E58.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E58.2 | FR-M01-04.06 |
| E58.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E58.3 | FR-M01-04.06 |
| E58.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E58.4 | FR-M01-04.04, FR-M01-04.06 |
| E58.4 | SYSTEM | Hệ thống từ chối đăng nhập, giữ DEACTIVATED; không tự kích hoạt lại và không cấp phiên truy cập. Liên kết nếu đã được xử lý trước cổng không được hiểu là mở khóa tài khoản. | Trạng thái kiểm ở cổng DEACTIVATED | END:REJECTED | FR-M01-04.06, FR-M01-05.04, BR-M01-18 |


**E59: Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Cổng nhận snapshot DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E59 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E59.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E59.2 | FR-M01-04.06 |
| E59.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E59.3 | FR-M01-04.06 |
| E59.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E59.4 | FR-M01-04.04, FR-M01-04.06 |
| E59.4 | SYSTEM | Hệ thống từ chối truy cập DELETED; không phục hồi danh tính/phiên đã xóa. Không khớp Google vào tài khoản DELETED bằng email đã bị xóa. | Nếu email Google cũ nay chưa thuộc tài khoản nào thì đi hành trình tạo mới thay vì nhận diện lại DELETED | END:REJECTED | FR-M01-04.06, FR-M01-05.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.08, BR-M01-18, BR-M01-21 |


**E60: Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Bảo trì bật và người đăng nhập không phải ADMIN.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E60 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E60.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E60.2 | FR-M01-04.06 |
| E60.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E60.3 | FR-M01-04.06 |
| E60.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E60.4 | FR-M01-04.04, FR-M01-04.06 |
| E60.4 | SYSTEM | Hệ thống từ chối đăng nhập, không cấp phiên. Không khẳng định thứ tự thay đổi liên kết trước/sau kiểm bảo trì khi FR/US chưa thống nhất; phần này bị đánh dấu GAP-SC-M01-001. | maintenance=true; USER/MOD; nhánh quyền truy cập đã rõ, thứ tự side effect liên kết còn cần xác nhận | END:REJECTED | FR-M01-04.06, FR-M01-05.19, BR-M01-37 |


**E61: Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Email Google chưa thuộc tài khoản nào.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E61 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E61.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E61.2 | FR-M01-04.06 |
| E61.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E61.3 | FR-M01-04.06 |
| E61.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E61.4 | FR-M01-04.04, FR-M01-04.06 |
| E61.4 | SYSTEM | Hệ thống không đăng nhập vào một tài khoản giả định đã có; chuyển danh tính sang hành trình tạo mới có kiểm đồng ý, tạm dừng đăng ký và bảo trì. | UC-M01-004 / SC-M01-001 nhận danh tính Google từ bước M3; bắt đầu ở điểm kiểm email/đồng ý; chưa tạo mới chỉ vì chọn Google | END:HANDED_OFF | FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08 |


**E62: Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Thiếu username hoặc display_name.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E62 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E62.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E62.2 | FR-M01-04.06 |
| E62.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E62.3 | FR-M01-04.06 |
| E62.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E62.4 | FR-M01-04.04, FR-M01-04.06 |
| E62.4 | SYSTEM | Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E62.5 | FR-M01-04.06, FR-M01-04.08, FR-M01-04.09, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E62.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E62.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E62.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="" hoặc display_name="" | E62.7 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E62.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E62.8 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E62.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E63: Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Username ngoài độ dài hoặc tập ký tự cho phép.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E63 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E63.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E63.2 | FR-M01-04.06 |
| E63.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E63.3 | FR-M01-04.06 |
| E63.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E63.4 | FR-M01-04.04, FR-M01-04.06 |
| E63.4 | SYSTEM | Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E63.5 | FR-M01-04.06, FR-M01-04.08, FR-M01-04.09, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E63.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E63.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E63.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="ab", hoặc "a"×21, hoặc "an.hoc" | E63.7 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E63.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E63.8 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E63.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E64: Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E64 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E64.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E64.2 | FR-M01-04.06 |
| E64.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E64.3 | FR-M01-04.06 |
| E64.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E64.4 | FR-M01-04.04, FR-M01-04.06 |
| E64.4 | SYSTEM | Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E64.5 | FR-M01-04.06, FR-M01-04.08, FR-M01-04.09, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E64.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E64.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E64.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | An_12A1 trùng an_12a1; hoặc Cuong trùng username DELETED cuong | E64.7 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E64.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E64.8 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E64.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E65: Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Display_name sau trim rỗng hoặc quá 50 ký tự.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E65 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E65.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E65.2 | FR-M01-04.06 |
| E65.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E65.3 | FR-M01-04.06 |
| E65.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E65.4 | FR-M01-04.04, FR-M01-04.06 |
| E65.4 | SYSTEM | Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E65.5 | FR-M01-04.06, FR-M01-04.08, FR-M01-04.09, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E65.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E65.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E65.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | "   " hoặc "A"×51 | E65.7 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E65.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E65.8 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E65.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E66: Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Display_name chứa ký tự không được nhận.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E66 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E66.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E66.2 | FR-M01-04.06 |
| E66.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E66.3 | FR-M01-04.06 |
| E66.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E66.4 | FR-M01-04.04, FR-M01-04.06 |
| E66.4 | SYSTEM | Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E66.5 | FR-M01-04.06, FR-M01-04.08, FR-M01-04.09, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E66.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E66.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E66.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | display_name="An 😊" | E66.7 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E66.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E66.8 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E66.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E67: Phương thức/ngữ cảnh thay thế: Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo; Yêu cầu không có phiên đăng nhập.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E67 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E67.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E67.2 | FR-M01-04.06 |
| E67.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E67.3 | FR-M01-04.06 |
| E67.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E67.4 | FR-M01-04.04, FR-M01-04.06 |
| E67.4 | SYSTEM | Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E67.5 | FR-M01-04.06, FR-M01-04.08, FR-M01-04.09, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E67.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E67.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E67.6 | SYSTEM | Hệ thống từ chối thiết lập; không nâng mức xác minh. | Không có phiên; giữ dữ liệu tài khoản trước yêu cầu | END:REJECTED | FR-M01-03.09 |


**E68: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E68 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E68.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E68.2 | FR-M01-04.06 |
| E68.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E68.3 | FR-M01-04.06 |
| E68.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E68.4 | FR-M01-04.04, FR-M01-04.06 |
| E68.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; chuyển NONE thành EMAIL_VERIFIED; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | A01 đã liên kết Google; không tạo A02; NONE → EMAIL_VERIFIED; P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E68.5 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E68.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E68.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E68.6 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E69: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Cổng nhận tài khoản DEACTIVATED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E69 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E69.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E69.2 | FR-M01-04.06 |
| E69.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E69.3 | FR-M01-04.06 |
| E69.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E69.4 | FR-M01-04.04, FR-M01-04.06 |
| E69.4 | SYSTEM | Hệ thống từ chối đăng nhập, giữ DEACTIVATED; không tự kích hoạt lại và không cấp phiên truy cập. Liên kết nếu đã được xử lý trước cổng không được hiểu là mở khóa tài khoản. | Trạng thái kiểm ở cổng DEACTIVATED | END:REJECTED | FR-M01-04.06, FR-M01-05.04, BR-M01-18 |


**E70: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Cổng nhận snapshot DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E70 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E70.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E70.2 | FR-M01-04.06 |
| E70.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E70.3 | FR-M01-04.06 |
| E70.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E70.4 | FR-M01-04.04, FR-M01-04.06 |
| E70.4 | SYSTEM | Hệ thống từ chối truy cập DELETED; không phục hồi danh tính/phiên đã xóa. Không khớp Google vào tài khoản DELETED bằng email đã bị xóa. | Nếu email Google cũ nay chưa thuộc tài khoản nào thì đi hành trình tạo mới thay vì nhận diện lại DELETED | END:REJECTED | FR-M01-04.06, FR-M01-05.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.08, BR-M01-18, BR-M01-21 |


**E71: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Bảo trì bật và người đăng nhập không phải ADMIN.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E71 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E71.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E71.2 | FR-M01-04.06 |
| E71.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E71.3 | FR-M01-04.06 |
| E71.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E71.4 | FR-M01-04.04, FR-M01-04.06 |
| E71.4 | SYSTEM | Hệ thống từ chối đăng nhập, không cấp phiên. Không khẳng định thứ tự thay đổi liên kết trước/sau kiểm bảo trì khi FR/US chưa thống nhất; phần này bị đánh dấu GAP-SC-M01-001. | maintenance=true; USER/MOD; nhánh quyền truy cập đã rõ, thứ tự side effect liên kết còn cần xác nhận | END:REJECTED | FR-M01-04.06, FR-M01-05.19, BR-M01-37 |


**E72: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Email Google chưa thuộc tài khoản nào.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E72 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E72.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E72.2 | FR-M01-04.06 |
| E72.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E72.3 | FR-M01-04.06 |
| E72.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E72.4 | FR-M01-04.04, FR-M01-04.06 |
| E72.4 | SYSTEM | Hệ thống không đăng nhập vào một tài khoản giả định đã có; chuyển danh tính sang hành trình tạo mới có kiểm đồng ý, tạm dừng đăng ký và bảo trì. | UC-M01-004 / SC-M01-001 nhận danh tính Google từ bước M3; bắt đầu ở điểm kiểm email/đồng ý; chưa tạo mới chỉ vì chọn Google | END:HANDED_OFF | FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08 |


**E73: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Thiếu username hoặc display_name.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E73 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E73.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E73.2 | FR-M01-04.06 |
| E73.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E73.3 | FR-M01-04.06 |
| E73.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E73.4 | FR-M01-04.04, FR-M01-04.06 |
| E73.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; chuyển NONE thành EMAIL_VERIFIED; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | A01 đã liên kết Google; không tạo A02; NONE → EMAIL_VERIFIED; P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E73.5 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E73.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E73.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E73.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="" hoặc display_name="" | E73.7 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E73.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E73.8 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E73.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E74: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Username ngoài độ dài hoặc tập ký tự cho phép.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E74 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E74.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E74.2 | FR-M01-04.06 |
| E74.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E74.3 | FR-M01-04.06 |
| E74.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E74.4 | FR-M01-04.04, FR-M01-04.06 |
| E74.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; chuyển NONE thành EMAIL_VERIFIED; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | A01 đã liên kết Google; không tạo A02; NONE → EMAIL_VERIFIED; P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E74.5 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E74.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E74.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E74.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="ab", hoặc "a"×21, hoặc "an.hoc" | E74.7 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E74.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E74.8 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E74.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E75: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E75 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E75.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E75.2 | FR-M01-04.06 |
| E75.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E75.3 | FR-M01-04.06 |
| E75.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E75.4 | FR-M01-04.04, FR-M01-04.06 |
| E75.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; chuyển NONE thành EMAIL_VERIFIED; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | A01 đã liên kết Google; không tạo A02; NONE → EMAIL_VERIFIED; P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E75.5 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E75.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E75.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E75.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | An_12A1 trùng an_12a1; hoặc Cuong trùng username DELETED cuong | E75.7 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E75.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E75.8 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E75.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E76: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Display_name sau trim rỗng hoặc quá 50 ký tự.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E76 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E76.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E76.2 | FR-M01-04.06 |
| E76.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E76.3 | FR-M01-04.06 |
| E76.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E76.4 | FR-M01-04.04, FR-M01-04.06 |
| E76.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; chuyển NONE thành EMAIL_VERIFIED; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | A01 đã liên kết Google; không tạo A02; NONE → EMAIL_VERIFIED; P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E76.5 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E76.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E76.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E76.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | "   " hoặc "A"×51 | E76.7 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E76.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E76.8 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E76.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E77: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Display_name chứa ký tự không được nhận.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E77 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E77.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E77.2 | FR-M01-04.06 |
| E77.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E77.3 | FR-M01-04.06 |
| E77.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E77.4 | FR-M01-04.04, FR-M01-04.06 |
| E77.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; chuyển NONE thành EMAIL_VERIFIED; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | A01 đã liên kết Google; không tạo A02; NONE → EMAIL_VERIFIED; P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E77.5 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E77.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E77.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E77.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | display_name="An 😊" | E77.7 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E77.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E77.8 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E77.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E78: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email chưa xác minh; Yêu cầu không có phiên đăng nhập.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E78 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E78.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E78.2 | FR-M01-04.06 |
| E78.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E78.3 | FR-M01-04.06 |
| E78.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E78.4 | FR-M01-04.04, FR-M01-04.06 |
| E78.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; chuyển NONE thành EMAIL_VERIFIED; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | A01 đã liên kết Google; không tạo A02; NONE → EMAIL_VERIFIED; P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E78.5 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E78.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E78.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E78.6 | SYSTEM | Hệ thống từ chối thiết lập; không nâng mức xác minh. | Không có phiên; giữ dữ liệu tài khoản trước yêu cầu | END:REJECTED | FR-M01-03.09 |


**E79: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E79 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E79.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E79.2 | FR-M01-04.06 |
| E79.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E79.3 | FR-M01-04.06 |
| E79.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E79.4 | FR-M01-04.04, FR-M01-04.06 |
| E79.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; giữ mức xác minh đã có; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | A01 đã liên kết Google; không tạo A02; EMAIL_VERIFIED giữ nguyên; P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E79.5 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E79.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E79.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E79.6 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E80: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Cổng nhận tài khoản DEACTIVATED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E80 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E80.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E80.2 | FR-M01-04.06 |
| E80.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E80.3 | FR-M01-04.06 |
| E80.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E80.4 | FR-M01-04.04, FR-M01-04.06 |
| E80.4 | SYSTEM | Hệ thống từ chối đăng nhập, giữ DEACTIVATED; không tự kích hoạt lại và không cấp phiên truy cập. Liên kết nếu đã được xử lý trước cổng không được hiểu là mở khóa tài khoản. | Trạng thái kiểm ở cổng DEACTIVATED | END:REJECTED | FR-M01-04.06, FR-M01-05.04, BR-M01-18 |


**E81: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Cổng nhận snapshot DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E81 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E81.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E81.2 | FR-M01-04.06 |
| E81.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E81.3 | FR-M01-04.06 |
| E81.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E81.4 | FR-M01-04.04, FR-M01-04.06 |
| E81.4 | SYSTEM | Hệ thống từ chối truy cập DELETED; không phục hồi danh tính/phiên đã xóa. Không khớp Google vào tài khoản DELETED bằng email đã bị xóa. | Nếu email Google cũ nay chưa thuộc tài khoản nào thì đi hành trình tạo mới thay vì nhận diện lại DELETED | END:REJECTED | FR-M01-04.06, FR-M01-05.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.08, BR-M01-18, BR-M01-21 |


**E82: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Bảo trì bật và người đăng nhập không phải ADMIN.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E82 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E82.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E82.2 | FR-M01-04.06 |
| E82.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E82.3 | FR-M01-04.06 |
| E82.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E82.4 | FR-M01-04.04, FR-M01-04.06 |
| E82.4 | SYSTEM | Hệ thống từ chối đăng nhập, không cấp phiên. Không khẳng định thứ tự thay đổi liên kết trước/sau kiểm bảo trì khi FR/US chưa thống nhất; phần này bị đánh dấu GAP-SC-M01-001. | maintenance=true; USER/MOD; nhánh quyền truy cập đã rõ, thứ tự side effect liên kết còn cần xác nhận | END:REJECTED | FR-M01-04.06, FR-M01-05.19, BR-M01-37 |


**E83: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Email Google chưa thuộc tài khoản nào.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E83 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E83.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E83.2 | FR-M01-04.06 |
| E83.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E83.3 | FR-M01-04.06 |
| E83.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E83.4 | FR-M01-04.04, FR-M01-04.06 |
| E83.4 | SYSTEM | Hệ thống không đăng nhập vào một tài khoản giả định đã có; chuyển danh tính sang hành trình tạo mới có kiểm đồng ý, tạm dừng đăng ký và bảo trì. | UC-M01-004 / SC-M01-001 nhận danh tính Google từ bước M3; bắt đầu ở điểm kiểm email/đồng ý; chưa tạo mới chỉ vì chọn Google | END:HANDED_OFF | FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08 |


**E84: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Thiếu username hoặc display_name.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E84 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E84.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E84.2 | FR-M01-04.06 |
| E84.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E84.3 | FR-M01-04.06 |
| E84.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E84.4 | FR-M01-04.04, FR-M01-04.06 |
| E84.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; giữ mức xác minh đã có; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | A01 đã liên kết Google; không tạo A02; EMAIL_VERIFIED giữ nguyên; P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E84.5 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E84.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E84.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E84.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="" hoặc display_name="" | E84.7 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E84.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E84.8 | FR-M01-03.04, BR-M01-05, BR-M01-06 |
| E84.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E85: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Username ngoài độ dài hoặc tập ký tự cho phép.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E85 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E85.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E85.2 | FR-M01-04.06 |
| E85.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E85.3 | FR-M01-04.06 |
| E85.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E85.4 | FR-M01-04.04, FR-M01-04.06 |
| E85.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; giữ mức xác minh đã có; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | A01 đã liên kết Google; không tạo A02; EMAIL_VERIFIED giữ nguyên; P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E85.5 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E85.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E85.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E85.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | username="ab", hoặc "a"×21, hoặc "an.hoc" | E85.7 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E85.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E85.8 | FR-M01-03.05, BR-M01-05, BR-M01-06 |
| E85.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E86: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Username trùng khi bỏ phân biệt hoa/thường, kể cả của DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E86 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E86.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E86.2 | FR-M01-04.06 |
| E86.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E86.3 | FR-M01-04.06 |
| E86.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E86.4 | FR-M01-04.04, FR-M01-04.06 |
| E86.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; giữ mức xác minh đã có; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | A01 đã liên kết Google; không tạo A02; EMAIL_VERIFIED giữ nguyên; P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E86.5 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E86.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E86.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E86.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | An_12A1 trùng an_12a1; hoặc Cuong trùng username DELETED cuong | E86.7 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E86.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E86.8 | FR-M01-03.06, BR-M01-05, BR-M01-06 |
| E86.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E87: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Display_name sau trim rỗng hoặc quá 50 ký tự.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E87 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E87.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E87.2 | FR-M01-04.06 |
| E87.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E87.3 | FR-M01-04.06 |
| E87.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E87.4 | FR-M01-04.04, FR-M01-04.06 |
| E87.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; giữ mức xác minh đã có; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | A01 đã liên kết Google; không tạo A02; EMAIL_VERIFIED giữ nguyên; P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E87.5 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E87.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E87.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E87.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | "   " hoặc "A"×51 | E87.7 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E87.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E87.8 | FR-M01-03.12, FR-M01-03.13, BR-M01-05, BR-M01-06 |
| E87.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E88: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Display_name chứa ký tự không được nhận.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E88 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E88.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E88.2 | FR-M01-04.06 |
| E88.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E88.3 | FR-M01-04.06 |
| E88.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E88.4 | FR-M01-04.04, FR-M01-04.06 |
| E88.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; giữ mức xác minh đã có; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | A01 đã liên kết Google; không tạo A02; EMAIL_VERIFIED giữ nguyên; P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E88.5 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E88.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E88.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E88.6 | SYSTEM | Hệ thống từ chối bộ thông tin chưa hợp lệ, giữ mức EMAIL_VERIFIED; cho sửa rồi gửi lại theo nhánh UC-M01-003/A2. | display_name="An 😊" | E88.7 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E88.7 | ACT-002 | Chủ tài khoản sửa về username khả dụng An_12A1 và display_name "  Minh An  ", rồi gửi lại. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E88.8 | FR-M01-03.14, BR-M01-05, BR-M01-06 |
| E88.8 | SYSTEM | Hệ thống kiểm quyền/mức xác minh và các giá trị; trim display_name; lưu username giữ hoa/thường, dùng display_name làm tên chính; chuyển sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 SETUP_COMPLETED; display_name lưu Minh An, được trùng người khác | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M01-01.09, BR-M01-33 |


**E89: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập; Yêu cầu không có phiên đăng nhập.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E89 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E89.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E89.2 | FR-M01-04.06 |
| E89.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E89.3 | FR-M01-04.06 |
| E89.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E89.4 | FR-M01-04.04, FR-M01-04.06 |
| E89.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; giữ mức xác minh đã có; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng, tạo phiên đăng nhập Google cho P01 và đưa tới bước 3, chưa cấp quyền như tài khoản đã hoàn tất. | A01 đã liên kết Google; không tạo A02; EMAIL_VERIFIED giữ nguyên; P01 phiên Google mới; ACTIVE/EMAIL_VERIFIED; đích UC-M01-003 | E89.5 | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.11, BR-M01-18 |
| E89.5 | ACT-002 | Chủ tài khoản nhập các giá trị, chọn bỏ qua bio, Lớp/Khối, avatar rồi gửi bước 3. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E89.6 | FR-M01-03.01, FR-M01-03.02, FR-M01-03.03, BR-M01-02 |
| E89.6 | SYSTEM | Hệ thống từ chối thiết lập; không nâng mức xác minh. | Không có phiên; giữ dữ liệu tài khoản trước yêu cầu | END:REJECTED | FR-M01-03.09 |


**E90: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã thiết lập.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E90 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E90.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E90.2 | FR-M01-04.06 |
| E90.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E90.3 | FR-M01-04.06 |
| E90.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E90.4 | FR-M01-04.04, FR-M01-04.06 |
| E90.4 | SYSTEM | Hệ thống nhận diện email trùng tài khoản email, tự liên kết Google không hỏi xác nhận; giữ mức xác minh đã có; ghi thông báo trong ứng dụng và email sự kiện liên kết qua M07. Hệ thống áp dụng cổng trạng thái/mức xác minh, cấp phiên mới cho P01 và cho vào ứng dụng theo quyền; phiên L01 giữ riêng. | A01 đã liên kết Google; không tạo A02; SETUP_COMPLETED giữ nguyên; P01 phiên mới truy cập 1 giờ, làm mới 30 ngày; ACTIVE/SETUP_COMPLETED; maintenance=false | END:SUCCESS | FR-M01-04.04, FR-M01-04.05, FR-M01-04.09, FR-M01-04.11, BR-M01-09, BR-M01-33, FR-M07-04.01, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.12, FR-M01-05.19, BR-M01-16, BR-M01-17, BR-M01-18, BR-M01-37 |


**E91: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã thiết lập; Cổng nhận tài khoản DEACTIVATED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E91 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E91.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E91.2 | FR-M01-04.06 |
| E91.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E91.3 | FR-M01-04.06 |
| E91.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E91.4 | FR-M01-04.04, FR-M01-04.06 |
| E91.4 | SYSTEM | Hệ thống từ chối đăng nhập, giữ DEACTIVATED; không tự kích hoạt lại và không cấp phiên truy cập. Liên kết nếu đã được xử lý trước cổng không được hiểu là mở khóa tài khoản. | Trạng thái kiểm ở cổng DEACTIVATED | END:REJECTED | FR-M01-04.06, FR-M01-05.04, BR-M01-18 |


**E92: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã thiết lập; Cổng nhận snapshot DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E92 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E92.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E92.2 | FR-M01-04.06 |
| E92.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E92.3 | FR-M01-04.06 |
| E92.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E92.4 | FR-M01-04.04, FR-M01-04.06 |
| E92.4 | SYSTEM | Hệ thống từ chối truy cập DELETED; không phục hồi danh tính/phiên đã xóa. Không khớp Google vào tài khoản DELETED bằng email đã bị xóa. | Nếu email Google cũ nay chưa thuộc tài khoản nào thì đi hành trình tạo mới thay vì nhận diện lại DELETED | END:REJECTED | FR-M01-04.06, FR-M01-05.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.08, BR-M01-18, BR-M01-21 |


**E93: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã thiết lập; Bảo trì bật và người đăng nhập không phải ADMIN.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E93 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E93.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E93.2 | FR-M01-04.06 |
| E93.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E93.3 | FR-M01-04.06 |
| E93.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E93.4 | FR-M01-04.04, FR-M01-04.06 |
| E93.4 | SYSTEM | Hệ thống từ chối đăng nhập, không cấp phiên. Không khẳng định thứ tự thay đổi liên kết trước/sau kiểm bảo trì khi FR/US chưa thống nhất; phần này bị đánh dấu GAP-SC-M01-001. | maintenance=true; USER/MOD; nhánh quyền truy cập đã rõ, thứ tự side effect liên kết còn cần xác nhận | END:REJECTED | FR-M01-04.06, FR-M01-05.19, BR-M01-37 |


**E94: Phương thức/ngữ cảnh thay thế: Đăng nhập Google và liên kết tài khoản email đã thiết lập; Email Google chưa thuộc tài khoản nào.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E94 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E94.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E94.2 | FR-M01-04.06 |
| E94.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E94.3 | FR-M01-04.06 |
| E94.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E94.4 | FR-M01-04.04, FR-M01-04.06 |
| E94.4 | SYSTEM | Hệ thống không đăng nhập vào một tài khoản giả định đã có; chuyển danh tính sang hành trình tạo mới có kiểm đồng ý, tạm dừng đăng ký và bảo trì. | UC-M01-004 / SC-M01-001 nhận danh tính Google từ bước M3; bắt đầu ở điểm kiểm email/đồng ý; chưa tạo mới chỉ vì chọn Google | END:HANDED_OFF | FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08 |


**E95: Phương thức/ngữ cảnh thay thế: Đăng nhập Google tài khoản bị khóa còn hạn khiếu nại.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E95 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E95.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E95.2 | FR-M01-04.06 |
| E95.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E95.3 | FR-M01-04.06 |
| E95.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E95.4 | FR-M01-04.04, FR-M01-04.06 |
| E95.4 | SYSTEM | Hệ thống áp dụng cổng trạng thái trước mức xác minh, tạo phiên hạn chế và chỉ hiển thị lý do ban, OK, thời gian/nút Khiếu nại còn hạn. | A03 BANNED; ban vĩnh viễn từ 01/11/2026 09:00, hiện 06/11/2026 09:00 còn 85×24 giờ; không dùng ứng dụng bình thường | E95.5 | FR-M01-04.06, FR-M01-04.08, FR-M01-05.05, FR-M01-05.06, FR-M01-05.07, FR-M01-05.08, BR-M01-18, BR-M01-19, BR-M09-04 |
| E95.5 | ACT-002 | Chủ tài khoản bấm OK trên màn hình tài khoản bị khóa. | P01; lịch sử tìm kiếm trình duyệt [đạo hàm, hình học]; L01 có phiên riêng | E95.6 | FR-M01-05.07, FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, BR-M01-19 |
| E95.6 | SYSTEM | Hệ thống kết thúc phiên truy cập và phiên làm mới P01; giữ các phiên thiết bị khác; xóa toàn bộ lịch sử tìm kiếm trên trình duyệt P01. | P01 không còn phiên; lịch sử=[]; L01 giữ nguyên; nếu chưa đồng ý P2.0 thì lần mở sau vẫn phải hỏi | END:CANCELLED | FR-M01-05.07, FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, BR-M01-19, FR-M06-05.10, BR-M06-20 |


**E96: Phương thức/ngữ cảnh thay thế: Đăng nhập Google tài khoản bị khóa còn hạn khiếu nại; Cổng nhận tài khoản DEACTIVATED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E96 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E96.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E96.2 | FR-M01-04.06 |
| E96.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E96.3 | FR-M01-04.06 |
| E96.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E96.4 | FR-M01-04.04, FR-M01-04.06 |
| E96.4 | SYSTEM | Hệ thống từ chối đăng nhập, giữ DEACTIVATED; không tự kích hoạt lại và không cấp phiên truy cập. Liên kết nếu đã được xử lý trước cổng không được hiểu là mở khóa tài khoản. | Trạng thái kiểm ở cổng DEACTIVATED | END:REJECTED | FR-M01-04.06, FR-M01-05.04, BR-M01-18 |


**E97: Phương thức/ngữ cảnh thay thế: Đăng nhập Google tài khoản bị khóa còn hạn khiếu nại; Cổng nhận snapshot DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E97 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E97.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E97.2 | FR-M01-04.06 |
| E97.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E97.3 | FR-M01-04.06 |
| E97.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E97.4 | FR-M01-04.04, FR-M01-04.06 |
| E97.4 | SYSTEM | Hệ thống từ chối truy cập DELETED; không phục hồi danh tính/phiên đã xóa. Không khớp Google vào tài khoản DELETED bằng email đã bị xóa. | Nếu email Google cũ nay chưa thuộc tài khoản nào thì đi hành trình tạo mới thay vì nhận diện lại DELETED | END:REJECTED | FR-M01-04.06, FR-M01-05.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.08, BR-M01-18, BR-M01-21 |


**E98: Phương thức/ngữ cảnh thay thế: Đăng nhập Google tài khoản bị khóa còn hạn khiếu nại; Bảo trì bật và người đăng nhập không phải ADMIN.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E98 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E98.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E98.2 | FR-M01-04.06 |
| E98.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E98.3 | FR-M01-04.06 |
| E98.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E98.4 | FR-M01-04.04, FR-M01-04.06 |
| E98.4 | SYSTEM | Hệ thống từ chối đăng nhập, không cấp phiên. Không khẳng định thứ tự thay đổi liên kết trước/sau kiểm bảo trì khi FR/US chưa thống nhất; phần này bị đánh dấu GAP-SC-M01-001. | maintenance=true; USER/MOD; nhánh quyền truy cập đã rõ, thứ tự side effect liên kết còn cần xác nhận | END:REJECTED | FR-M01-04.06, FR-M01-05.19, BR-M01-37 |


**E99: Phương thức/ngữ cảnh thay thế: Đăng nhập Google tài khoản bị khóa còn hạn khiếu nại; Email Google chưa thuộc tài khoản nào.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E99 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E99.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E99.2 | FR-M01-04.06 |
| E99.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E99.3 | FR-M01-04.06 |
| E99.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E99.4 | FR-M01-04.04, FR-M01-04.06 |
| E99.4 | SYSTEM | Hệ thống không đăng nhập vào một tài khoản giả định đã có; chuyển danh tính sang hành trình tạo mới có kiểm đồng ý, tạm dừng đăng ký và bảo trì. | UC-M01-004 / SC-M01-001 nhận danh tính Google từ bước M3; bắt đầu ở điểm kiểm email/đồng ý; chưa tạo mới chỉ vì chọn Google | END:HANDED_OFF | FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08 |


**E100: Phương thức/ngữ cảnh thay thế: Đăng nhập Google tài khoản bị khóa còn hạn khiếu nại; Tài khoản vẫn BANNED nhưng thời hạn khiếu nại đã hết.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E100 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E100.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E100.2 | FR-M01-04.06 |
| E100.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E100.3 | FR-M01-04.06 |
| E100.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E100.4 | FR-M01-04.04, FR-M01-04.06 |
| E100.4 | SYSTEM | Hệ thống cấp phiên hạn chế và chỉ hiển thị lý do ban cùng OK; ẩn nút/thời gian Khiếu nại. | Ban vĩnh viễn từ 01/07/2026; hiện 06/11/2026; chỉ OK để đăng xuất | END:SUCCESS | FR-M01-04.06, FR-M01-04.08, FR-M01-05.05, FR-M01-05.07, FR-M01-05.09, BR-M01-19, BR-M09-04 |


**E101: Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập Google trong bảo trì.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E101 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E101.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E101.2 | FR-M01-04.06 |
| E101.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E101.3 | FR-M01-04.06 |
| E101.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E101.4 | FR-M01-04.04, FR-M01-04.06 |
| E101.4 | SYSTEM | Hệ thống áp dụng cổng trạng thái/mức xác minh, cấp phiên mới cho P01 và cho vào ứng dụng theo quyền; phiên L01 giữ riêng. | P01 phiên mới truy cập 1 giờ, làm mới 30 ngày; ACTIVE/SETUP_COMPLETED; role=ADMIN, maintenance=true | END:SUCCESS | FR-M01-04.06, FR-M01-04.08, FR-M01-05.01, FR-M01-05.12, FR-M01-05.19, BR-M01-16, BR-M01-17, BR-M01-18, BR-M01-37 |


**E102: Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập Google trong bảo trì; Cổng nhận tài khoản DEACTIVATED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E102 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E102.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E102.2 | FR-M01-04.06 |
| E102.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E102.3 | FR-M01-04.06 |
| E102.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E102.4 | FR-M01-04.04, FR-M01-04.06 |
| E102.4 | SYSTEM | Hệ thống từ chối đăng nhập, giữ DEACTIVATED; không tự kích hoạt lại và không cấp phiên truy cập. Liên kết nếu đã được xử lý trước cổng không được hiểu là mở khóa tài khoản. | Trạng thái kiểm ở cổng DEACTIVATED | END:REJECTED | FR-M01-04.06, FR-M01-05.04, BR-M01-18 |


**E103: Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập Google trong bảo trì; Cổng nhận snapshot DELETED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E103 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E103.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E103.2 | FR-M01-04.06 |
| E103.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E103.3 | FR-M01-04.06 |
| E103.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E103.4 | FR-M01-04.04, FR-M01-04.06 |
| E103.4 | SYSTEM | Hệ thống từ chối truy cập DELETED; không phục hồi danh tính/phiên đã xóa. Không khớp Google vào tài khoản DELETED bằng email đã bị xóa. | Nếu email Google cũ nay chưa thuộc tài khoản nào thì đi hành trình tạo mới thay vì nhận diện lại DELETED | END:REJECTED | FR-M01-04.06, FR-M01-05.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.08, BR-M01-18, BR-M01-21 |


**E104: Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập Google trong bảo trì; Bảo trì bật và người đăng nhập không phải ADMIN.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E104 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E104.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E104.2 | FR-M01-04.06 |
| E104.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E104.3 | FR-M01-04.06 |
| E104.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E104.4 | FR-M01-04.04, FR-M01-04.06 |
| E104.4 | SYSTEM | Hệ thống từ chối đăng nhập, không cấp phiên. Không khẳng định thứ tự thay đổi liên kết trước/sau kiểm bảo trì khi FR/US chưa thống nhất; phần này bị đánh dấu GAP-SC-M01-001. | maintenance=true; USER/MOD; nhánh quyền truy cập đã rõ, thứ tự side effect liên kết còn cần xác nhận | END:REJECTED | FR-M01-04.06, FR-M01-05.19, BR-M01-37 |


**E105: Phương thức/ngữ cảnh thay thế: ADMIN đăng nhập Google trong bảo trì; Email Google chưa thuộc tài khoản nào.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E105 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E105.1 | ACT-001 | Guest chọn đăng nhập bằng Google. | P01; tài khoản Google dùng email an.study@example.test | E105.2 | FR-M01-04.06 |
| E105.2 | SYSTEM | Hệ thống khởi tạo việc nhận danh tính từ dịch vụ Google. | Lần truy cập Google cho P01 | E105.3 | FR-M01-04.06 |
| E105.3 | ACT-004 | Google trả danh tính đã xác thực. | Email=an.study@example.test; tên Google=Minh An; khớp email trong snapshot hiện hành | E105.4 | FR-M01-04.04, FR-M01-04.06 |
| E105.4 | SYSTEM | Hệ thống không đăng nhập vào một tài khoản giả định đã có; chuyển danh tính sang hành trình tạo mới có kiểm đồng ý, tạm dừng đăng ký và bảo trì. | UC-M01-004 / SC-M01-001 nhận danh tính Google từ bước M3; bắt đầu ở điểm kiểm email/đồng ý; chưa tạo mới chỉ vì chọn Google | END:HANDED_OFF | FR-M01-04.01, FR-M01-04.07, FR-M01-04.10, FR-M01-04.12, FR-M01-04.13, FR-M01-01.12, BR-M01-08 |


**E106: Tại cổng đăng nhập, tài khoản ACTIVE/NONE yêu cầu bước thiết lập trước xác minh.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E106 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E106.1 | SYSTEM | Hệ thống không cho bỏ qua bước xác minh; đưa về bước 2 trong ngữ cảnh tiếp tục đăng ký. | A01 ACTIVE/NONE; chưa được thiết lập | E106.2 | FR-M01-03.08 |
| E106.2 | ACT-001 | Chủ tài khoản mở link xác minh nhận trong email. | L1 mở 09:10, chưa dùng, chưa bị thay thế | E106.3 | FR-M01-02.01, BR-M01-10 |
| E106.3 | SYSTEM | Hệ thống kiểm link, chuyển NONE sang EMAIL_VERIFIED, làm link không dùng lại và đưa tới bước 3. | A01 ACTIVE/EMAIL_VERIFIED; L1 đã dùng; ngữ cảnh bước 3 | E106.4 | FR-M01-02.01, FR-M01-02.02, FR-M01-02.03, FR-M01-02.06, BR-M01-38 |
| E106.4 | ACT-002 | Chủ tài khoản nhập username/display_name và bỏ qua ba trường tùy chọn rồi gửi. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua | E106.5 | FR-M01-03.01, FR-M01-03.02, BR-M01-02 |
| E106.5 | SYSTEM | Hệ thống kiểm tên, trim display_name, lưu định danh đúng quy tắc và chuyển mức xác minh sang SETUP_COMPLETED. | username=An_12A1; display_name nhập="  Minh An  ", lưu="Minh An"; bio/Lớp-Khối/avatar bỏ qua; A01 ACTIVE/USER/SETUP_COMPLETED; display_name là tên chính, username giữ đúng An_12A1 | END:SUCCESS | FR-M01-03.01, FR-M01-03.02, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07 |


**E107: Đăng nhập ACTIVE/SETUP_COMPLETED; phiên bản chính sách mới hơn bản đã đồng ý; Đồng ý phiên bản chính sách mới.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E107 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E107.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E107.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E107.2 | SYSTEM | Hệ thống xác thực email/mật khẩu, kiểm bảo trì và trạng thái trước mức xác minh; cấp phiên thiết bị P01 và chưa cho dùng tiếp trước quyết định chính sách. Hệ thống yêu cầu đồng ý P2.0 trước khi dùng tiếp, kể cả phiên P01 đang còn; cung cấp nội dung chính sách hiện hành. | A01 ACTIVE/USER/SETUP_COMPLETED; P01 có phiên mới, truy cập hạn 1 giờ và làm mới hạn 30 ngày; L01 vẫn đăng nhập; Phiên bản minh họa P2.0; Chính sách quyền riêng tư có dữ liệu thu thập, mục đích, dịch vụ ngoài, thời gian lưu, quyền, dưới 16 tuổi, thay đổi, liên hệ; Điều khoản có quy tắc/nội dung cấm, kiểm duyệt/cảnh báo, khóa/khiếu nại, quyền với nội dung. Bốn nhóm: tài khoản/hồ sơ; nội dung tạo; an toàn cộng đồng; dữ liệu qua AI. Nêu AI xử lý cả bản soạn khi bấm Gợi ý topic, dịch vụ đăng nhập/lưu ảnh/email/AI, không bán dữ liệu, lưu bình luận/tin nhắn/nhật ký sau xóa, quyền sửa/xóa/bản sao, rút đồng ý qua vô hiệu hóa. Không nêu tên nhà cung cấp hay phiên đăng nhập; MS1 chưa có tải bản sao; câu chữ chính sách và email liên hệ còn chờ hoàn thiện.; bản đã đồng ý P1.0; chưa cho dùng tiếp vì có phiên sẵn | E107.3 | FR-M01-05.01, FR-M01-05.12, BR-M01-16, BR-M01-17, BR-M01-18, FR-M01-16.01, BR-M01-44 |
| E107.3 | ACT-002 | Chủ tài khoản chọn đồng ý P2.0. | consent=true lúc 06/11/2026 09:10 +07 | E107.4 | FR-M01-16.02 |
| E107.4 | SYSTEM | Hệ thống lưu thời điểm và phiên bản P2.0 đã đồng ý; cho tiếp tục trong quyền hiện có. | Bản ghi đồng ý A01/P2.0/09:10; không đổi trạng thái/quyền tài khoản | END:SUCCESS | FR-M01-16.02, BR-M01-44 |


**E108: Đăng nhập ACTIVE/SETUP_COMPLETED; phiên bản chính sách mới hơn bản đã đồng ý; Từ chối chính sách mới rồi đăng xuất.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E108 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E108.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E108.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E108.2 | SYSTEM | Hệ thống xác thực email/mật khẩu, kiểm bảo trì và trạng thái trước mức xác minh; cấp phiên thiết bị P01 và chưa cho dùng tiếp trước quyết định chính sách. Hệ thống yêu cầu đồng ý P2.0 trước khi dùng tiếp, kể cả phiên P01 đang còn; cung cấp nội dung chính sách hiện hành. | A01 ACTIVE/USER/SETUP_COMPLETED; P01 có phiên mới, truy cập hạn 1 giờ và làm mới hạn 30 ngày; L01 vẫn đăng nhập; Phiên bản minh họa P2.0; Chính sách quyền riêng tư có dữ liệu thu thập, mục đích, dịch vụ ngoài, thời gian lưu, quyền, dưới 16 tuổi, thay đổi, liên hệ; Điều khoản có quy tắc/nội dung cấm, kiểm duyệt/cảnh báo, khóa/khiếu nại, quyền với nội dung. Bốn nhóm: tài khoản/hồ sơ; nội dung tạo; an toàn cộng đồng; dữ liệu qua AI. Nêu AI xử lý cả bản soạn khi bấm Gợi ý topic, dịch vụ đăng nhập/lưu ảnh/email/AI, không bán dữ liệu, lưu bình luận/tin nhắn/nhật ký sau xóa, quyền sửa/xóa/bản sao, rút đồng ý qua vô hiệu hóa. Không nêu tên nhà cung cấp hay phiên đăng nhập; MS1 chưa có tải bản sao; câu chữ chính sách và email liên hệ còn chờ hoàn thiện.; bản đã đồng ý P1.0; chưa cho dùng tiếp vì có phiên sẵn | E108.3 | FR-M01-05.01, FR-M01-05.12, BR-M01-16, BR-M01-17, BR-M01-18, FR-M01-16.01, BR-M01-44 |
| E108.3 | ACT-002 | Chủ tài khoản chọn không đồng ý P2.0. | consent=false; bản đã đồng ý vẫn P1.0 | E108.4 | FR-M01-16.03 |
| E108.4 | SYSTEM | Hệ thống chỉ cung cấp hai đường thoát Đăng xuất hoặc Vô hiệu hóa; không cho dùng chức năng khác khi chưa đồng ý. | Không lưu đồng ý P2.0; lựa chọn vô hiệu hóa vẫn phải đáp ứng ACTIVE/chủ tài khoản | E108.5 | FR-M01-16.03, BR-M01-45 |
| E108.5 | ACT-002 | Chủ tài khoản chọn Đăng xuất. | P01; L01 là thiết bị khác; lịch sử P01 có đạo hàm | E108.6 | FR-M01-16.03 |
| E108.6 | SYSTEM | Hệ thống triển khai UC-M01-006: kết thúc phiên P01, giữ các phiên khác, xóa lịch sử tìm kiếm trình duyệt P01; không ghi đồng ý P2.0. | P01 không còn phiên, lịch sử rỗng; A01 vẫn ACTIVE; lần mở sau nếu chưa đồng ý phải hỏi lại | END:CANCELLED | FR-M01-07.01, FR-M01-07.02, FR-M01-16.03, FR-M01-16.04, FR-M06-05.10, BR-M01-45 |


**E109: Đăng nhập ACTIVE/SETUP_COMPLETED; phiên bản chính sách mới hơn bản đã đồng ý; Từ chối chính sách mới rồi vô hiệu hóa.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-007 E109 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E109.1 | ACT-001 | Guest gửi email và mật khẩu của tài khoản cần truy cập. | Email theo snapshot A01/A03/A04; password="  Mật khẩu 2026  "; P01 | E109.2 | FR-M01-05.01, FR-M01-05.02, BR-M01-35 |
| E109.2 | SYSTEM | Hệ thống xác thực email/mật khẩu, kiểm bảo trì và trạng thái trước mức xác minh; cấp phiên thiết bị P01 và chưa cho dùng tiếp trước quyết định chính sách. Hệ thống yêu cầu đồng ý P2.0 trước khi dùng tiếp, kể cả phiên P01 đang còn; cung cấp nội dung chính sách hiện hành. | A01 ACTIVE/USER/SETUP_COMPLETED; P01 có phiên mới, truy cập hạn 1 giờ và làm mới hạn 30 ngày; L01 vẫn đăng nhập; Phiên bản minh họa P2.0; Chính sách quyền riêng tư có dữ liệu thu thập, mục đích, dịch vụ ngoài, thời gian lưu, quyền, dưới 16 tuổi, thay đổi, liên hệ; Điều khoản có quy tắc/nội dung cấm, kiểm duyệt/cảnh báo, khóa/khiếu nại, quyền với nội dung. Bốn nhóm: tài khoản/hồ sơ; nội dung tạo; an toàn cộng đồng; dữ liệu qua AI. Nêu AI xử lý cả bản soạn khi bấm Gợi ý topic, dịch vụ đăng nhập/lưu ảnh/email/AI, không bán dữ liệu, lưu bình luận/tin nhắn/nhật ký sau xóa, quyền sửa/xóa/bản sao, rút đồng ý qua vô hiệu hóa. Không nêu tên nhà cung cấp hay phiên đăng nhập; MS1 chưa có tải bản sao; câu chữ chính sách và email liên hệ còn chờ hoàn thiện.; bản đã đồng ý P1.0; chưa cho dùng tiếp vì có phiên sẵn | E109.3 | FR-M01-05.01, FR-M01-05.12, BR-M01-16, BR-M01-17, BR-M01-18, FR-M01-16.01, BR-M01-44 |
| E109.3 | ACT-002 | Chủ tài khoản chọn không đồng ý P2.0. | consent=false; bản đã đồng ý vẫn P1.0 | E109.4 | FR-M01-16.03 |
| E109.4 | SYSTEM | Hệ thống chỉ cung cấp hai đường thoát Đăng xuất hoặc Vô hiệu hóa; không cho dùng chức năng khác khi chưa đồng ý. | Không lưu đồng ý P2.0; lựa chọn vô hiệu hóa vẫn phải đáp ứng ACTIVE/chủ tài khoản | E109.5 | FR-M01-16.03, BR-M01-45 |
| E109.5 | ACT-002 | Chủ tài khoản chọn Vô hiệu hóa tài khoản của mình. | A01 ACTIVE; chọn tại EP-POLICY-DECISION | E109.6 | FR-M01-16.03 |
| E109.6 | SYSTEM | Hệ thống triển khai UC-M01-009: kiểm ACTIVE/quyền chủ tài khoản, chuyển DEACTIVATED, kết thúc mọi phiên và áp cách hiển thị nội dung; tính cửa sổ 14×24 giờ. Không ghi đồng ý P2.0. | A01 DEACTIVATED lúc 06/11/2026 09:10, hạn 20/11/2026 09:10; bài ẩn, tên thay thế cho bình luận | END:SUCCESS | FR-M01-16.03, FR-M01-10.01, FR-M01-10.02, FR-M01-10.07, FR-M01-13.01, FR-M01-13.03, BR-M01-21, BR-M01-45 |


**Ghi chú đường đi và giới hạn:** Luồng chính hoàn tất mục tiêu; các trường hợp trong mục 6 là đường thay thế, không chạy nối tiếp tất cả nhánh. Guard mô tả dữ liệu/ngữ cảnh thay thế của chính lần thực thi. Nhánh sửa gửi lại áp cùng điều kiện kiểm tra; không có giới hạn thử mới ngoài nguồn. Các GAP ở mục cuối vẫn áp dụng.

<!-- sc:end SC-M01-007 -->

<!-- sc:scenario SC-M01-014 -->

<a id="sc-m01-014"></a>

### SC-M01-014 — Đăng xuất chủ động trên thiết bị hiện tại

#### 1. Tên kịch bản chuẩn

**Đăng xuất chủ động trên thiết bị hiện tại** — BF-M01-014; UC owner: [UC-M01-006](../../us/US-M01.md#uc-m01-006); nhóm chi tiết: UC-M01-021. Trigger: Người dùng chọn Đăng xuất.

#### 2. Actor thực hiện

ACT-002 chủ tài khoản; ACT-003 thực hiện cùng hành vi đối với tài khoản của chính mình.

#### 3. Tiền điều kiện

Có phiên P01 của chủ tài khoản; L01 là thiết bị khác đang có phiên riêng. Nhánh OK được phép trong BANNED, nhánh chính sách không đòi phải đồng ý P2.0 mới được thoát.

#### 4. Hậu điều kiện

<!-- sc:post SC-M01-014 -->

| result | condition |
|---|---|
| SUCCESS | Phiên P01 chấm dứt, lịch sử trình duyệt P01 rỗng, L01 không bị đăng xuất; trạng thái tài khoản và bản ghi đồng ý không tự đổi. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M01-014 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Chủ tài khoản chọn Đăng xuất trên P01. | P01; lịch sử tìm kiếm trình duyệt [đạo hàm, hình học]; L01 có phiên riêng | M2 | FR-M01-07.01, FR-M01-07.02, BR-M01-17 |
| M2 | SYSTEM | Hệ thống kết thúc phiên truy cập và phiên làm mới P01; giữ các phiên thiết bị khác; xóa toàn bộ lịch sử tìm kiếm trên trình duyệt P01. | P01 không còn phiên; lịch sử=[]; L01 giữ nguyên; nếu chưa đồng ý P2.0 thì lần mở sau vẫn phải hỏi | END:SUCCESS | FR-M01-07.01, FR-M01-07.02, BR-M01-17, FR-M06-05.10, BR-M06-20 |


#### 6. Các ngoại lệ

<!-- sc:exceptions SC-M01-014 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Chủ tài khoản BANNED bấm OK | E1.1 | FR-M01-05.07, FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, BR-M01-19, FR-M06-05.10, BR-M06-20 |
| E2 | user-choice | M1 | Người dùng từ chối chính sách và chọn Đăng xuất | E2.1 | FR-M01-16.03, FR-M01-16.04, FR-M01-07.01, FR-M01-07.02, BR-M01-45, FR-M06-05.10, BR-M06-20 |


**E1: Chủ tài khoản BANNED bấm OK.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-014 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Chủ tài khoản bấm OK trên màn hình tài khoản bị khóa. | P01; lịch sử tìm kiếm trình duyệt [đạo hàm, hình học]; L01 có phiên riêng | E1.2 | FR-M01-05.07, FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, BR-M01-19 |
| E1.2 | SYSTEM | Hệ thống kết thúc phiên truy cập và phiên làm mới P01; giữ các phiên thiết bị khác; xóa toàn bộ lịch sử tìm kiếm trên trình duyệt P01. | P01 không còn phiên; lịch sử=[]; L01 giữ nguyên; nếu chưa đồng ý P2.0 thì lần mở sau vẫn phải hỏi | END:SUCCESS | FR-M01-05.07, FR-M01-05.18, FR-M01-07.01, FR-M01-07.02, BR-M01-19, FR-M06-05.10, BR-M06-20 |


**E2: Người dùng từ chối chính sách và chọn Đăng xuất.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-014 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | Chủ tài khoản đã từ chối P2.0 chọn Đăng xuất trong hai lựa chọn còn được phép. | P01; lịch sử tìm kiếm trình duyệt [đạo hàm, hình học]; L01 có phiên riêng | E2.2 | FR-M01-16.03, FR-M01-16.04, FR-M01-07.01, FR-M01-07.02, BR-M01-45 |
| E2.2 | SYSTEM | Hệ thống kết thúc phiên truy cập và phiên làm mới P01; giữ các phiên thiết bị khác; xóa toàn bộ lịch sử tìm kiếm trên trình duyệt P01. | P01 không còn phiên; lịch sử=[]; L01 giữ nguyên; nếu chưa đồng ý P2.0 thì lần mở sau vẫn phải hỏi | END:SUCCESS | FR-M01-16.03, FR-M01-16.04, FR-M01-07.01, FR-M01-07.02, BR-M01-45, FR-M06-05.10, BR-M06-20 |


**Ghi chú đường đi và giới hạn:** Luồng chính hoàn tất mục tiêu; các trường hợp trong mục 6 là đường thay thế, không chạy nối tiếp tất cả nhánh. Guard mô tả dữ liệu/ngữ cảnh thay thế của chính lần thực thi. Nhánh sửa gửi lại áp cùng điều kiện kiểm tra; không có giới hạn thử mới ngoài nguồn. Các GAP ở mục cuối vẫn áp dụng.

<!-- sc:end SC-M01-014 -->

<!-- sc:scenario SC-M01-017 -->

<a id="sc-m01-017"></a>

### SC-M01-017 — Đổi mật khẩu khi đã đăng nhập

#### 1. Tên kịch bản chuẩn

**Đổi mật khẩu khi đã đăng nhập** — BF-M01-017; UC owner: [UC-M01-007](../../us/US-M01.md#uc-m01-007); nhóm chi tiết: UC-M01-022. Trigger: Chủ tài khoản gửi mật khẩu cũ, mới và nhập lại.

#### 2. Actor thực hiện

ACT-002 chủ tài khoản; ACT-003 có thể đổi mật khẩu của chính mình; ACT-005 gửi email sự kiện qua M07.

#### 3. Tiền điều kiện

Đường chuẩn A01 là tài khoản email ACTIVE, có phiên P01, bảo trì tắt; L01 có phiên riêng. Những điều kiện cấp quyền vẫn được hệ thống kiểm, các yêu cầu không đủ điều kiện có nhánh từ chối.

#### 4. Hậu điều kiện

<!-- sc:post SC-M01-017 -->

| result | condition |
|---|---|
| SUCCESS | Mật khẩu mới có hiệu lực, L01 vẫn giữ phiên; thông báo trong ứng dụng được ghi nhận và email sự kiện được xếp gửi bất đồng bộ qua M07. |
| REJECTED | Mật khẩu, mức xác minh và các phiên trước yêu cầu không bị thay bằng kết quả thành công; không phát thông báo mật khẩu đã đổi cho lần từ chối. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M01-017 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Chủ tài khoản nhập mật khẩu cũ, mật khẩu mới và nhập lại trùng mật khẩu mới rồi gửi. | Giá trị giả lập: mật khẩu cũ="  Mật khẩu 2026  "; mới="mật khẩu mới 2026"; không trim hai giá trị; repeat="mật khẩu mới 2026" | M2 | FR-M01-08.01, BR-M01-14, BR-M01-35 |
| M2 | SYSTEM | Hệ thống kiểm quyền/loại/trạng thái và các mật khẩu, thay mật khẩu; giữ các phiên thiết bị khác. Ghi thông báo trong ứng dụng và một email sự kiện mật khẩu đã đổi vào hàng đợi M07; hoàn tất thay đổi không chờ gửi email. | Giá trị giả lập: mật khẩu cũ="  Mật khẩu 2026  "; mới="mật khẩu mới 2026"; không trim hai giá trị; P01 và L01 không bị chấm dứt bởi việc đổi; sự kiện gửi M07 | END:SUCCESS | FR-M01-08.01, FR-M01-08.04, FR-M01-08.05, BR-M01-14, BR-M01-31, BR-M01-35, BR-M01-36, FR-M07-04.01, FR-M07-04.02, FR-M07-04.03, FR-M07-04.09, FR-M07-04.10, BR-M07-11, BR-M07-26 |


#### 6. Các ngoại lệ

<!-- sc:exceptions SC-M01-017 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Mật khẩu cũ không đúng | E1.1 | FR-M01-08.02 |
| E2 | system | M2 | Nhập lại không trùng mật khẩu mới | E2.1 | FR-M01-08.03 |
| E3 | system | M2 | Mật khẩu mới ngoài 8–64 ký tự | E3.1 | FR-M01-08.08 |
| E4 | system | M2 | Mật khẩu mới trùng mật khẩu hiện tại | E4.1 | FR-M01-08.09 |
| E5 | system | M2 | Chưa đăng nhập | E5.1 | FR-M01-08.07 |
| E6 | system | M2 | Tài khoản chỉ Google | E6.1 | FR-M01-08.06 |
| E7 | system | M2 | Tài khoản không ACTIVE | E7.1 | FR-M01-08.10 |
| E8 | system | M2 | Bảo trì bật, người thao tác không ADMIN | E8.1 | FR-M01-05.20, BR-M01-37 |


**E1: Mật khẩu cũ không đúng.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-017 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối đổi mật khẩu; với tài khoản chỉ Google thì không cung cấp chức năng mật khẩu. Không phát sự kiện đổi thành công. | old="sai 2026" | END:REJECTED | FR-M01-08.02 |


**E2: Nhập lại không trùng mật khẩu mới.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-017 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối đổi mật khẩu; với tài khoản chỉ Google thì không cung cấp chức năng mật khẩu. Không phát sự kiện đổi thành công. | new="mật khẩu mới 2026"; repeat="mật khẩu khác 2026" | END:REJECTED | FR-M01-08.03 |


**E3: Mật khẩu mới ngoài 8–64 ký tự.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-017 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối đổi mật khẩu; với tài khoản chỉ Google thì không cung cấp chức năng mật khẩu. Không phát sự kiện đổi thành công. | new="1234567" hoặc "A"×65 | END:REJECTED | FR-M01-08.08 |


**E4: Mật khẩu mới trùng mật khẩu hiện tại.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-017 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối đổi mật khẩu; với tài khoản chỉ Google thì không cung cấp chức năng mật khẩu. Không phát sự kiện đổi thành công. | new=old="  Mật khẩu 2026  " | END:REJECTED | FR-M01-08.09 |


**E5: Chưa đăng nhập.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-017 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối đổi mật khẩu; với tài khoản chỉ Google thì không cung cấp chức năng mật khẩu. Không phát sự kiện đổi thành công. | Không có phiên P01 | END:REJECTED | FR-M01-08.07 |


**E6: Tài khoản chỉ Google.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-017 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối đổi mật khẩu; với tài khoản chỉ Google thì không cung cấp chức năng mật khẩu. Không phát sự kiện đổi thành công. | A02 không có mật khẩu iShare | END:REJECTED | FR-M01-08.06 |


**E7: Tài khoản không ACTIVE.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-017 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống từ chối đổi mật khẩu; với tài khoản chỉ Google thì không cung cấp chức năng mật khẩu. Không phát sự kiện đổi thành công. | A01 BANNED/DEACTIVATED/DELETED | END:REJECTED | FR-M01-08.10 |


**E8: Bảo trì bật, người thao tác không ADMIN.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-017 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống từ chối đổi mật khẩu; với tài khoản chỉ Google thì không cung cấp chức năng mật khẩu. Không phát sự kiện đổi thành công. | maintenance=true; role=USER/MOD | END:REJECTED | FR-M01-05.20, BR-M01-37 |


**Ghi chú đường đi và giới hạn:** Luồng chính hoàn tất mục tiêu; các trường hợp trong mục 6 là đường thay thế, không chạy nối tiếp tất cả nhánh. Guard mô tả dữ liệu/ngữ cảnh thay thế của chính lần thực thi. Nhánh sửa gửi lại áp cùng điều kiện kiểm tra; không có giới hạn thử mới ngoài nguồn. Các GAP ở mục cuối vẫn áp dụng.

<!-- sc:end SC-M01-017 -->

<!-- sc:scenario SC-M01-018 -->

<a id="sc-m01-018"></a>

### SC-M01-018 — Lấy lại mật khẩu tài khoản email ACTIVE

#### 1. Tên kịch bản chuẩn

**Lấy lại mật khẩu tài khoản email ACTIVE** — BF-M01-018; UC owner: [UC-M01-008](../../us/US-M01.md#uc-m01-008); nhóm chi tiết: UC-M01-022. Trigger: Guest gửi email ở chức năng Quên mật khẩu.

#### 2. Actor thực hiện

ACT-001 chủ tài khoản; ACT-005 hỗ trợ gửi link và email sự kiện.

#### 3. Tiền điều kiện

Không yêu cầu phiên. Chuẩn A01 email ACTIVE/SETUP_COMPLETED; P01 và L01 có phiên cũ; P02 là thiết bị đặt lại. Bảo trì tắt.

#### 4. Hậu điều kiện

<!-- sc:post SC-M01-018 -->

| result | condition |
|---|---|
| SUCCESS | Mật khẩu mới hợp lệ được lưu, link mất hiệu lực, mọi phiên cũ kết thúc; P02 nhận phiên mới theo trạng thái. ACTIVE/SETUP_COMPLETED vào ứng dụng; BANNED chỉ nhận phiên hạn chế, không được mở khóa. Thông báo đổi mật khẩu được ghi nhận theo M07. |
| REJECTED | Không có lần đặt lại thành công từ yêu cầu bị từ chối; mật khẩu/phiên hiện có giữ nguyên bởi yêu cầu lỗi. Với email không tồn tại/chỉ Google/DEACTIVATED không gửi link; thông điệp tương ứng không bị coi là xác nhận đã gửi. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M01-018 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-001 | Chủ tài khoản nhập email ở Quên mật khẩu rồi gửi. | an.study@example.test; A01 email ACTIVE | M2 | FR-M01-09.01 |
| M2 | SYSTEM | Hệ thống phân loại email; gửi link đặt lại mới cho tài khoản email ACTIVE/BANNED, làm link cũ mất hiệu lực và hiển thị cùng thông điệp chung cho trường hợp được bảo vệ. | Reset-L2 gửi 09:00, hạn 15 phút; Reset-L1 mất hiệu lực; "Liên kết đã được gửi, vui lòng kiểm tra email của bạn" | M3 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39 |
| M3 | ACT-001 | Chủ tài khoản mở link mới lúc 09:10, nhập mật khẩu mới và nhập lại trùng rồi gửi. | Reset-L2; new=repeat="mật khẩu mới 2026"; khác mật khẩu cũ; P02 | M4 | FR-M01-09.02 |
| M4 | SYSTEM | Hệ thống kiểm link còn hiệu lực, nhập lại trùng, mật khẩu khác cũ và 8–64 ký tự; thay mật khẩu, làm link không dùng lại, chấm dứt mọi phiên cũ, cấp phiên mới cho P02 và cho vào ứng dụng theo quyền. Ghi thông báo trong ứng dụng và một email sự kiện mật khẩu đã đổi vào hàng đợi M07; hoàn tất thay đổi không chờ gửi email. | P01/L01 hết phiên; P02 có phiên mới; A01 ACTIVE/SETUP_COMPLETED; email sự kiện mật khẩu đã đổi được xếp gửi | END:SUCCESS | FR-M01-09.02, FR-M01-09.03, FR-M01-09.04, FR-M01-09.12, FR-M01-09.16, BR-M01-12, BR-M01-13, BR-M01-35, BR-M01-38, BR-M01-39, FR-M07-04.01, FR-M07-04.02, FR-M07-04.03, FR-M07-04.09, FR-M07-04.10, BR-M07-11, BR-M07-26 |


#### 6. Các ngoại lệ

<!-- sc:exceptions SC-M01-018 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M4 | Link đã quá 15 phút | E1.1 | FR-M01-09.05, BR-M01-12, BR-M01-35, BR-M01-38 |
| E2 | system | M4 | Link đã dùng | E2.1 | FR-M01-09.10, BR-M01-12, BR-M01-35, BR-M01-38 |
| E3 | system | M4 | Link cũ đã bị thay bằng link mới | E3.1 | FR-M01-09.11, BR-M01-12, BR-M01-35, BR-M01-38 |
| E4 | system | M4 | Nhập lại không khớp | E4.1 | FR-M01-09.06, BR-M01-12, BR-M01-35, BR-M01-38 |
| E5 | system | M4 | Mật khẩu mới ngoài 8–64 ký tự | E5.1 | FR-M01-09.08, BR-M01-12, BR-M01-35, BR-M01-38 |
| E6 | system | M4 | Mật khẩu mới trùng hiện tại | E6.1 | FR-M01-09.09, BR-M01-12, BR-M01-35, BR-M01-38 |
| E7 | system | M2 | Email không thuộc tài khoản nào | E7.1 | FR-M01-09.13, FR-M01-09.14, BR-M01-15, BR-M01-39 |
| E8 | system | M2 | Email thuộc tài khoản chỉ Google | E8.1 | FR-M01-09.07, BR-M01-15, BR-M01-39 |
| E9 | system | M2 | Email thuộc DEACTIVATED | E9.1 | FR-M01-09.15, BR-M01-15, BR-M01-39 |
| E10 | user-choice | M1 | Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế | E10.1 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39, FR-M01-09.02, FR-M01-09.03, FR-M01-09.04, FR-M01-09.12, FR-M01-09.16, BR-M01-13, BR-M01-35, FR-M07-04.01, FR-M07-04.02, FR-M07-04.03, FR-M07-04.09, FR-M07-04.10, BR-M07-11, BR-M07-26 |
| E11 | user-choice | M1 | Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Link đã quá 15 phút | E11.1 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39, FR-M01-09.02, FR-M01-09.05, BR-M01-35 |
| E12 | user-choice | M1 | Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Link đã dùng | E12.1 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39, FR-M01-09.02, FR-M01-09.10, BR-M01-35 |
| E13 | user-choice | M1 | Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Link cũ đã bị thay bằng link mới | E13.1 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39, FR-M01-09.02, BR-M01-35 |
| E14 | user-choice | M1 | Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Nhập lại không khớp | E14.1 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39, FR-M01-09.02, FR-M01-09.06, BR-M01-35 |
| E15 | user-choice | M1 | Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Mật khẩu mới ngoài 8–64 ký tự | E15.1 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39, FR-M01-09.02, FR-M01-09.08, BR-M01-35 |
| E16 | user-choice | M1 | Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Mật khẩu mới trùng hiện tại | E16.1 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39, FR-M01-09.02, FR-M01-09.09, BR-M01-35 |
| E17 | user-choice | M1 | Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Email không thuộc tài khoản nào | E17.1 | FR-M01-09.01, FR-M01-09.13, FR-M01-09.14, BR-M01-15, BR-M01-39 |
| E18 | user-choice | M1 | Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Email thuộc tài khoản chỉ Google | E18.1 | FR-M01-09.01, FR-M01-09.07, BR-M01-15, BR-M01-39 |
| E19 | user-choice | M1 | Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Email thuộc DEACTIVATED | E19.1 | FR-M01-09.01, FR-M01-09.15, BR-M01-15, BR-M01-39 |


**E1: Link đã quá 15 phút.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối đặt lại cho lần gửi này; không thay mật khẩu hoặc cấp phiên mới do yêu cầu không hợp lệ; không làm sống lại link cũ. | Gửi 09:00, mở/gửi lúc 09:16 | END:REJECTED | FR-M01-09.05, BR-M01-12, BR-M01-35, BR-M01-38 |


**E2: Link đã dùng.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối đặt lại cho lần gửi này; không thay mật khẩu hoặc cấp phiên mới do yêu cầu không hợp lệ; không làm sống lại link cũ. | Reset-L1 đã dùng thành công trước đây | END:REJECTED | FR-M01-09.10, BR-M01-12, BR-M01-35, BR-M01-38 |


**E3: Link cũ đã bị thay bằng link mới.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối đặt lại cho lần gửi này; không thay mật khẩu hoặc cấp phiên mới do yêu cầu không hợp lệ; không làm sống lại link cũ. | Reset-L2 gửi mới; đang mở Reset-L1 | END:REJECTED | FR-M01-09.11, BR-M01-12, BR-M01-35, BR-M01-38 |


**E4: Nhập lại không khớp.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối đặt lại cho lần gửi này; không thay mật khẩu hoặc cấp phiên mới do yêu cầu không hợp lệ; không làm sống lại link cũ. | new="mật khẩu mới 2026"; repeat="khac 2026" | END:REJECTED | FR-M01-09.06, BR-M01-12, BR-M01-35, BR-M01-38 |


**E5: Mật khẩu mới ngoài 8–64 ký tự.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối đặt lại cho lần gửi này; không thay mật khẩu hoặc cấp phiên mới do yêu cầu không hợp lệ; không làm sống lại link cũ. | new="1234567" hoặc "A"×65 | END:REJECTED | FR-M01-09.08, BR-M01-12, BR-M01-35, BR-M01-38 |


**E6: Mật khẩu mới trùng hiện tại.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | SYSTEM | Hệ thống từ chối đặt lại cho lần gửi này; không thay mật khẩu hoặc cấp phiên mới do yêu cầu không hợp lệ; không làm sống lại link cũ. | new=old="  Mật khẩu 2026  " | END:REJECTED | FR-M01-09.09, BR-M01-12, BR-M01-35, BR-M01-38 |


**E7: Email không thuộc tài khoản nào.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | SYSTEM | Hệ thống hiển thị đúng thông điệp chung nhưng không gửi link. | nobody@example.test; "Liên kết đã được gửi, vui lòng kiểm tra email của bạn" | END:REJECTED | FR-M01-09.13, FR-M01-09.14, BR-M01-15, BR-M01-39 |


**E8: Email thuộc tài khoản chỉ Google.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | SYSTEM | Hệ thống không gửi link, hiển thị yêu cầu dùng Google. | "Tài khoản này đăng nhập qua Google, vui lòng dùng Google để đăng nhập" | END:REJECTED | FR-M01-09.07, BR-M01-15, BR-M01-39 |


**E9: Email thuộc DEACTIVATED.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | SYSTEM | Hệ thống không gửi link và hướng tới trang kích hoạt lại. | A01 DEACTIVATED giữ nguyên; mục tiêu tiếp theo UC-M01-010 | END:REJECTED | FR-M01-09.15, BR-M01-15, BR-M01-39 |


**E10: Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | ACT-001 | Chủ tài khoản nhập email ở Quên mật khẩu rồi gửi. | a03.study@example.test; A03 BANNED | E10.2 | FR-M01-09.01 |
| E10.2 | SYSTEM | Hệ thống phân loại email; gửi link đặt lại mới cho tài khoản email ACTIVE/BANNED, làm link cũ mất hiệu lực và hiển thị cùng thông điệp chung cho trường hợp được bảo vệ. | Reset-L2 gửi 09:00, hạn 15 phút; Reset-L1 mất hiệu lực; "Liên kết đã được gửi, vui lòng kiểm tra email của bạn" | E10.3 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39 |
| E10.3 | ACT-001 | Chủ tài khoản mở link mới lúc 09:10, nhập mật khẩu mới và nhập lại trùng rồi gửi. | Reset-L2; new=repeat="mật khẩu mới 2026"; khác mật khẩu cũ; P02 | E10.4 | FR-M01-09.02 |
| E10.4 | SYSTEM | Hệ thống kiểm link và mật khẩu, thay mật khẩu, làm link không dùng lại, chấm dứt mọi phiên cũ và cấp phiên hạn chế mới cho P02; chỉ hiển thị màn hình bị khóa với lý do, OK và khiếu nại/thời gian khi còn hạn. Ghi thông báo trong ứng dụng và một email sự kiện mật khẩu đã đổi vào hàng đợi M07; hoàn tất thay đổi không chờ gửi email. | P01/L01 hết phiên; P02 có phiên mới; A03 vẫn BANNED, không mở ứng dụng thông thường; email sự kiện mật khẩu đã đổi được xếp gửi | END:SUCCESS | FR-M01-09.02, FR-M01-09.03, FR-M01-09.04, FR-M01-09.12, FR-M01-09.16, BR-M01-12, BR-M01-13, BR-M01-35, BR-M01-38, BR-M01-39, FR-M07-04.01, FR-M07-04.02, FR-M07-04.03, FR-M07-04.09, FR-M07-04.10, BR-M07-11, BR-M07-26 |


**E11: Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Link đã quá 15 phút.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-001 | Chủ tài khoản nhập email ở Quên mật khẩu rồi gửi. | a03.study@example.test; A03 BANNED | E11.2 | FR-M01-09.01 |
| E11.2 | SYSTEM | Hệ thống phân loại email; gửi link đặt lại mới cho tài khoản email ACTIVE/BANNED, làm link cũ mất hiệu lực và hiển thị cùng thông điệp chung cho trường hợp được bảo vệ. | Reset-L2 gửi 09:00, hạn 15 phút; Reset-L1 mất hiệu lực; "Liên kết đã được gửi, vui lòng kiểm tra email của bạn" | E11.3 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39 |
| E11.3 | ACT-001 | Chủ tài khoản mở link mới lúc 09:10, nhập mật khẩu mới và nhập lại trùng rồi gửi. | Reset-L2; new=repeat="mật khẩu mới 2026"; khác mật khẩu cũ; P02 | E11.4 | FR-M01-09.02 |
| E11.4 | SYSTEM | Hệ thống từ chối đặt lại cho lần gửi này; không thay mật khẩu hoặc cấp phiên mới do yêu cầu không hợp lệ; không làm sống lại link cũ. | Gửi 09:00, mở/gửi lúc 09:16 | END:REJECTED | FR-M01-09.05, BR-M01-12, BR-M01-35, BR-M01-38 |


**E12: Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Link đã dùng.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | ACT-001 | Chủ tài khoản nhập email ở Quên mật khẩu rồi gửi. | a03.study@example.test; A03 BANNED | E12.2 | FR-M01-09.01 |
| E12.2 | SYSTEM | Hệ thống phân loại email; gửi link đặt lại mới cho tài khoản email ACTIVE/BANNED, làm link cũ mất hiệu lực và hiển thị cùng thông điệp chung cho trường hợp được bảo vệ. | Reset-L2 gửi 09:00, hạn 15 phút; Reset-L1 mất hiệu lực; "Liên kết đã được gửi, vui lòng kiểm tra email của bạn" | E12.3 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39 |
| E12.3 | ACT-001 | Chủ tài khoản mở link mới lúc 09:10, nhập mật khẩu mới và nhập lại trùng rồi gửi. | Reset-L2; new=repeat="mật khẩu mới 2026"; khác mật khẩu cũ; P02 | E12.4 | FR-M01-09.02 |
| E12.4 | SYSTEM | Hệ thống từ chối đặt lại cho lần gửi này; không thay mật khẩu hoặc cấp phiên mới do yêu cầu không hợp lệ; không làm sống lại link cũ. | Reset-L1 đã dùng thành công trước đây | END:REJECTED | FR-M01-09.10, BR-M01-12, BR-M01-35, BR-M01-38 |


**E13: Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Link cũ đã bị thay bằng link mới.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | ACT-001 | Chủ tài khoản nhập email ở Quên mật khẩu rồi gửi. | a03.study@example.test; A03 BANNED | E13.2 | FR-M01-09.01 |
| E13.2 | SYSTEM | Hệ thống phân loại email; gửi link đặt lại mới cho tài khoản email ACTIVE/BANNED, làm link cũ mất hiệu lực và hiển thị cùng thông điệp chung cho trường hợp được bảo vệ. | Reset-L2 gửi 09:00, hạn 15 phút; Reset-L1 mất hiệu lực; "Liên kết đã được gửi, vui lòng kiểm tra email của bạn" | E13.3 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39 |
| E13.3 | ACT-001 | Chủ tài khoản mở link mới lúc 09:10, nhập mật khẩu mới và nhập lại trùng rồi gửi. | Reset-L2; new=repeat="mật khẩu mới 2026"; khác mật khẩu cũ; P02 | E13.4 | FR-M01-09.02 |
| E13.4 | SYSTEM | Hệ thống từ chối đặt lại cho lần gửi này; không thay mật khẩu hoặc cấp phiên mới do yêu cầu không hợp lệ; không làm sống lại link cũ. | Reset-L2 gửi mới; đang mở Reset-L1 | END:REJECTED | FR-M01-09.11, BR-M01-12, BR-M01-35, BR-M01-38 |


**E14: Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Nhập lại không khớp.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | ACT-001 | Chủ tài khoản nhập email ở Quên mật khẩu rồi gửi. | a03.study@example.test; A03 BANNED | E14.2 | FR-M01-09.01 |
| E14.2 | SYSTEM | Hệ thống phân loại email; gửi link đặt lại mới cho tài khoản email ACTIVE/BANNED, làm link cũ mất hiệu lực và hiển thị cùng thông điệp chung cho trường hợp được bảo vệ. | Reset-L2 gửi 09:00, hạn 15 phút; Reset-L1 mất hiệu lực; "Liên kết đã được gửi, vui lòng kiểm tra email của bạn" | E14.3 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39 |
| E14.3 | ACT-001 | Chủ tài khoản mở link mới lúc 09:10, nhập mật khẩu mới và nhập lại trùng rồi gửi. | Reset-L2; new=repeat="mật khẩu mới 2026"; khác mật khẩu cũ; P02 | E14.4 | FR-M01-09.02 |
| E14.4 | SYSTEM | Hệ thống từ chối đặt lại cho lần gửi này; không thay mật khẩu hoặc cấp phiên mới do yêu cầu không hợp lệ; không làm sống lại link cũ. | new="mật khẩu mới 2026"; repeat="khac 2026" | END:REJECTED | FR-M01-09.06, BR-M01-12, BR-M01-35, BR-M01-38 |


**E15: Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Mật khẩu mới ngoài 8–64 ký tự.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | ACT-001 | Chủ tài khoản nhập email ở Quên mật khẩu rồi gửi. | a03.study@example.test; A03 BANNED | E15.2 | FR-M01-09.01 |
| E15.2 | SYSTEM | Hệ thống phân loại email; gửi link đặt lại mới cho tài khoản email ACTIVE/BANNED, làm link cũ mất hiệu lực và hiển thị cùng thông điệp chung cho trường hợp được bảo vệ. | Reset-L2 gửi 09:00, hạn 15 phút; Reset-L1 mất hiệu lực; "Liên kết đã được gửi, vui lòng kiểm tra email của bạn" | E15.3 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39 |
| E15.3 | ACT-001 | Chủ tài khoản mở link mới lúc 09:10, nhập mật khẩu mới và nhập lại trùng rồi gửi. | Reset-L2; new=repeat="mật khẩu mới 2026"; khác mật khẩu cũ; P02 | E15.4 | FR-M01-09.02 |
| E15.4 | SYSTEM | Hệ thống từ chối đặt lại cho lần gửi này; không thay mật khẩu hoặc cấp phiên mới do yêu cầu không hợp lệ; không làm sống lại link cũ. | new="1234567" hoặc "A"×65 | END:REJECTED | FR-M01-09.08, BR-M01-12, BR-M01-35, BR-M01-38 |


**E16: Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Mật khẩu mới trùng hiện tại.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E16 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E16.1 | ACT-001 | Chủ tài khoản nhập email ở Quên mật khẩu rồi gửi. | a03.study@example.test; A03 BANNED | E16.2 | FR-M01-09.01 |
| E16.2 | SYSTEM | Hệ thống phân loại email; gửi link đặt lại mới cho tài khoản email ACTIVE/BANNED, làm link cũ mất hiệu lực và hiển thị cùng thông điệp chung cho trường hợp được bảo vệ. | Reset-L2 gửi 09:00, hạn 15 phút; Reset-L1 mất hiệu lực; "Liên kết đã được gửi, vui lòng kiểm tra email của bạn" | E16.3 | FR-M01-09.01, FR-M01-09.11, FR-M01-09.13, FR-M01-09.14, BR-M01-12, BR-M01-38, BR-M01-39 |
| E16.3 | ACT-001 | Chủ tài khoản mở link mới lúc 09:10, nhập mật khẩu mới và nhập lại trùng rồi gửi. | Reset-L2; new=repeat="mật khẩu mới 2026"; khác mật khẩu cũ; P02 | E16.4 | FR-M01-09.02 |
| E16.4 | SYSTEM | Hệ thống từ chối đặt lại cho lần gửi này; không thay mật khẩu hoặc cấp phiên mới do yêu cầu không hợp lệ; không làm sống lại link cũ. | new=old="  Mật khẩu 2026  " | END:REJECTED | FR-M01-09.09, BR-M01-12, BR-M01-35, BR-M01-38 |


**E17: Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Email không thuộc tài khoản nào.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E17 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E17.1 | ACT-001 | Chủ tài khoản nhập email ở Quên mật khẩu rồi gửi. | a03.study@example.test; A03 BANNED | E17.2 | FR-M01-09.01 |
| E17.2 | SYSTEM | Hệ thống hiển thị đúng thông điệp chung nhưng không gửi link. | nobody@example.test; "Liên kết đã được gửi, vui lòng kiểm tra email của bạn" | END:REJECTED | FR-M01-09.13, FR-M01-09.14, BR-M01-15, BR-M01-39 |


**E18: Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Email thuộc tài khoản chỉ Google.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E18 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E18.1 | ACT-001 | Chủ tài khoản nhập email ở Quên mật khẩu rồi gửi. | a03.study@example.test; A03 BANNED | E18.2 | FR-M01-09.01 |
| E18.2 | SYSTEM | Hệ thống không gửi link, hiển thị yêu cầu dùng Google. | "Tài khoản này đăng nhập qua Google, vui lòng dùng Google để đăng nhập" | END:REJECTED | FR-M01-09.07, BR-M01-15, BR-M01-39 |


**E19: Tài khoản email BANNED yêu cầu lấy lại mật khẩu; kết quả vẫn là phiên hạn chế; Email thuộc DEACTIVATED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-018 E19 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E19.1 | ACT-001 | Chủ tài khoản nhập email ở Quên mật khẩu rồi gửi. | a03.study@example.test; A03 BANNED | E19.2 | FR-M01-09.01 |
| E19.2 | SYSTEM | Hệ thống không gửi link và hướng tới trang kích hoạt lại. | A01 DEACTIVATED giữ nguyên; mục tiêu tiếp theo UC-M01-010 | END:REJECTED | FR-M01-09.15, BR-M01-15, BR-M01-39 |


**Ghi chú đường đi và giới hạn:** Luồng chính hoàn tất mục tiêu; các trường hợp trong mục 6 là đường thay thế, không chạy nối tiếp tất cả nhánh. Guard mô tả dữ liệu/ngữ cảnh thay thế của chính lần thực thi. Nhánh sửa gửi lại áp cùng điều kiện kiểm tra; không có giới hạn thử mới ngoài nguồn. Các GAP ở mục cuối vẫn áp dụng.

<!-- sc:end SC-M01-018 -->

<!-- sc:scenario SC-M01-022 -->

<a id="sc-m01-022"></a>

### SC-M01-022 — Vô hiệu hóa tài khoản của chính mình

#### 1. Tên kịch bản chuẩn

**Vô hiệu hóa tài khoản của chính mình** — BF-M01-022; UC owner: [UC-M01-009](../../us/US-M01.md#uc-m01-009); nhóm chi tiết: UC-M01-023, UC-M01-024. Trigger: Chủ tài khoản chọn Vô hiệu hóa trực tiếp hoặc sau khi từ chối chính sách.

#### 2. Actor thực hiện

ACT-002 chủ tài khoản; ACT-003 chỉ được thao tác lên tài khoản của chính mình.

#### 3. Tiền điều kiện

Đường chuẩn có phiên P01 của A01 ACTIVE, thao tác vào tài khoản của chính mình, bảo trì tắt. Các quyền/điều kiện vẫn được kiểm trong M2. Không có nút xóa trực tiếp; không suy thêm bước xác nhận mật khẩu.

#### 4. Hậu điều kiện

<!-- sc:post SC-M01-022 -->

| result | condition |
|---|---|
| SUCCESS | A01 DEACTIVATED; mọi phiên kết thúc; nội dung/danh tính hiển thị theo trạng thái. Trong cửa sổ được kích hoạt lại; tại hạn cuối có AUT-M01-002, cảnh báo trước 24 giờ theo AUT-M01-003. |
| REJECTED | Không vô hiệu hóa yêu cầu không đủ điều kiện, không tạo cửa sổ xóa mới và không cấp quyền đặc biệt cho Mod/Admin. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M01-022 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Chủ tài khoản yêu cầu vô hiệu hóa A01 của mình. | A01 ACTIVE; P01 và L01 đang có phiên; thời điểm 06/11/2026 09:00 +07 | M2 | FR-M01-10.01, FR-M01-10.03, BR-M01-20, BR-M01-45 |
| M2 | SYSTEM | Hệ thống kiểm quyền/trạng thái, chuyển DEACTIVATED, kết thúc mọi phiên, ẩn bài; bình luận giữ nội dung với tên thay thế và avatar mặc định. Đặt cửa sổ kích hoạt lại đủ 14×24 giờ; rút đồng ý bằng chính hành vi vô hiệu hóa. | A01 DEACTIVATED; P01/L01 mất phiên; hết hạn 20/11/2026 09:00; bài P101 bị ẩn; bình luận C101 giữ "Dùng Vi-ét", tác giả "Tài khoản tạm thời vô hiệu hoá" | END:SUCCESS | FR-M01-10.01, FR-M01-10.02, FR-M01-10.03, FR-M01-10.07, FR-M01-13.01, FR-M01-13.02, FR-M01-13.03, FR-M01-13.07, BR-M01-20, BR-M01-21, BR-M01-23, BR-M01-45 |


#### 6. Các ngoại lệ

<!-- sc:exceptions SC-M01-022 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Yêu cầu vô hiệu hóa tài khoản của người khác, kể cả Mod/Admin | E1.1 | FR-M01-10.04 |
| E2 | system | M2 | Tài khoản đích BANNED | E2.1 | FR-M01-10.05 |
| E3 | system | M2 | Người gửi chưa đăng nhập | E3.1 | FR-M01-10.06 |
| E4 | system | M2 | Bảo trì bật với người không ADMIN | E4.1 | FR-M01-05.20, BR-M01-37 |


**E1: Yêu cầu vô hiệu hóa tài khoản của người khác, kể cả Mod/Admin.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-022 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống từ chối vô hiệu hóa; không chuyển trạng thái hoặc kết thúc các phiên như một lần vô hiệu hóa thành công. | actor A01; target=A02 | END:REJECTED | FR-M01-10.04 |


**E2: Tài khoản đích BANNED.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-022 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối vô hiệu hóa; không chuyển trạng thái hoặc kết thúc các phiên như một lần vô hiệu hóa thành công. | A01 BANNED | END:REJECTED | FR-M01-10.05 |


**E3: Người gửi chưa đăng nhập.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-022 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối vô hiệu hóa; không chuyển trạng thái hoặc kết thúc các phiên như một lần vô hiệu hóa thành công. | Không có phiên | END:REJECTED | FR-M01-10.06 |


**E4: Bảo trì bật với người không ADMIN.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-022 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối vô hiệu hóa; không chuyển trạng thái hoặc kết thúc các phiên như một lần vô hiệu hóa thành công. | maintenance=true; role=USER/MOD | END:REJECTED | FR-M01-05.20, BR-M01-37 |


**Ghi chú đường đi và giới hạn:** Luồng chính hoàn tất mục tiêu; các trường hợp trong mục 6 là đường thay thế, không chạy nối tiếp tất cả nhánh. Guard mô tả dữ liệu/ngữ cảnh thay thế của chính lần thực thi. Nhánh sửa gửi lại áp cùng điều kiện kiểm tra; không có giới hạn thử mới ngoài nguồn. Các GAP ở mục cuối vẫn áp dụng.

<!-- sc:end SC-M01-022 -->

<!-- sc:scenario SC-M01-023 -->

<a id="sc-m01-023"></a>

### SC-M01-023 — Kích hoạt lại tài khoản bằng mã email

#### 1. Tên kịch bản chuẩn

**Kích hoạt lại tài khoản bằng mã email** — BF-M01-023; UC owner: [UC-M01-010](../../us/US-M01.md#uc-m01-010); nhóm chi tiết: UC-M01-023. Trigger: Chủ tài khoản DEACTIVATED yêu cầu mã kích hoạt tại trang kích hoạt.

#### 2. Actor thực hiện

ACT-001 chủ tài khoản chưa có phiên; ACT-005 hỗ trợ email.

#### 3. Tiền điều kiện

Không cần phiên. A01 vô hiệu hóa lúc 01/11/2026 09:00, hạn 15/11/2026 09:00; hiện 06/11/2026 09:01. Đây là lần yêu cầu mã đầu của hành trình minh họa. Thời hạn tài khoản và mã được kiểm lại trước khi kích hoạt; ví dụ dùng mốc tránh đúng 15 phút còn chưa rõ ở GAP-SC-M01-001.

#### 4. Hậu điều kiện

<!-- sc:post SC-M01-023 -->

| result | condition |
|---|---|
| SUCCESS | A01 ACTIVE, bài/bình luận hiển thị trở lại đúng danh tính còn lưu; P01 được đăng nhập bằng phiên mới. Quyền dùng tiếp vẫn chịu trạng thái, mức xác minh và phiên bản chính sách. |
| REJECTED | Không cấp phiên hoặc phục hồi tài khoản từ mã/email không hợp lệ; tài khoản còn hạn giữ DEACTIVATED, tài khoản đã DELETED không chuyển lại ACTIVE. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M01-023 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-001 | Chủ tài khoản nhập email tại trang kích hoạt và yêu cầu gửi mã. | an.study@example.test; A01 DEACTIVATED; yêu cầu 09:01 | M2 | FR-M01-11.01 |
| M2 | SYSTEM | Hệ thống kiểm tài khoản/cửa sổ và khoảng cách gửi lại; gửi mã 6 chữ số tới email. | Code=482731, gửi 09:01; A01 vẫn DEACTIVATED | M3 | FR-M01-11.01, FR-M01-11.09, BR-M01-22 |
| M3 | ACT-001 | Chủ tài khoản nhập mã nhận trong email và gửi xác nhận. | 482731 lúc 09:10; không có phiên trước yêu cầu | M4 | FR-M01-11.02 |
| M4 | SYSTEM | Hệ thống kiểm mã còn hiệu lực/hạn và cửa sổ 14 ngày; chuyển ACTIVE, hiển thị lại bài/bình luận với tên/avatar chủ tài khoản và cấp phiên mới cho P01. | A01 ACTIVE; P01 phiên mới; bài P101 và bình luận C101 phục hồi cách hiển thị tên Minh An/avatar cũ | END:SUCCESS | FR-M01-11.02, FR-M01-11.03, FR-M01-11.04, FR-M01-11.05, FR-M01-11.06, FR-M01-11.07, FR-M01-11.08, BR-M01-22, BR-M01-25 |


#### 6. Các ngoại lệ

<!-- sc:exceptions SC-M01-023 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Email không thuộc tài khoản DEACTIVATED | E1.1 | FR-M01-11.10 |
| E2 | system | M4 | Hết đủ 14×24 giờ trước lúc xác nhận | E2.1 | FR-M01-11.05, FR-M01-12.01, FR-M01-12.04, BR-M01-21 |
| E3 | system | M4 | Nhập sai mã nhưng tổng số lần sai chưa đến 5 | E3.1 | FR-M01-11.04, FR-M01-11.08, BR-M01-22, FR-M01-11.02 |
| E4 | system | M4 | Lần sai này là lần sai thứ 5 | E4.1 | FR-M01-11.04, FR-M01-11.08, FR-M01-11.01, FR-M01-11.09, BR-M01-22, FR-M01-11.02 |
| E5 | system | M4 | Mã đã quá 15 phút kể từ lúc gửi | E5.1 | FR-M01-11.07, FR-M01-11.01, FR-M01-11.09, BR-M01-22, FR-M01-11.02 |
| E6 | user-choice | M1 | Chủ tài khoản yêu cầu gửi lại mã trong cùng hành trình kích hoạt lại | E6.1 | FR-M01-11.01, FR-M01-11.09, BR-M01-22, FR-M01-11.02, FR-M01-11.03, FR-M01-11.04, FR-M01-11.05, FR-M01-11.06, FR-M01-11.07, FR-M01-11.08, BR-M01-25 |
| E7 | user-choice | M1 | Chủ tài khoản yêu cầu gửi lại mã trong cùng hành trình kích hoạt lại; Email không thuộc tài khoản DEACTIVATED | E7.1 | FR-M01-11.01, FR-M01-11.10 |
| E8 | user-choice | M1 | Chủ tài khoản yêu cầu gửi lại mã trong cùng hành trình kích hoạt lại; Hết đủ 14×24 giờ trước lúc xác nhận | E8.1 | FR-M01-11.01, FR-M01-11.09, BR-M01-22, FR-M01-11.02, FR-M01-11.05, FR-M01-12.01, FR-M01-12.04, BR-M01-21 |
| E9 | user-choice | M1 | Chủ tài khoản yêu cầu gửi lại mã trong cùng hành trình kích hoạt lại; Nhập sai mã nhưng tổng số lần sai chưa đến 5 | E9.1 | FR-M01-11.01, FR-M01-11.09, BR-M01-22, FR-M01-11.02, FR-M01-11.04, FR-M01-11.08, FR-M01-11.03, FR-M01-11.05, FR-M01-11.06, FR-M01-11.07, BR-M01-25 |
| E10 | user-choice | M1 | Chủ tài khoản yêu cầu gửi lại mã trong cùng hành trình kích hoạt lại; Lần sai này là lần sai thứ 5 | E10.1 | FR-M01-11.01, FR-M01-11.09, BR-M01-22, FR-M01-11.02, FR-M01-11.04, FR-M01-11.08, FR-M01-11.03, FR-M01-11.05, FR-M01-11.06, FR-M01-11.07, BR-M01-25 |
| E11 | user-choice | M1 | Chủ tài khoản yêu cầu gửi lại mã trong cùng hành trình kích hoạt lại; Mã đã quá 15 phút kể từ lúc gửi | E11.1 | FR-M01-11.01, FR-M01-11.09, BR-M01-22, FR-M01-11.02, FR-M01-11.07, FR-M01-11.03, FR-M01-11.04, FR-M01-11.05, FR-M01-11.06, FR-M01-11.08, BR-M01-25 |
| E12 | user-choice | M1 | Chủ tài khoản yêu cầu gửi lại mã trong cùng hành trình kích hoạt lại; Đang yêu cầu gửi lại nhưng chưa đủ 60 giây từ lần gửi trước | E12.1 | FR-M01-11.01, FR-M01-11.09, BR-M01-22, FR-M01-11.02, FR-M01-11.03, FR-M01-11.04, FR-M01-11.05, FR-M01-11.06, FR-M01-11.07, FR-M01-11.08, BR-M01-25 |


**E1: Email không thuộc tài khoản DEACTIVATED.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-023 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống không gửi mã kích hoạt lại. | email=noaccount@example.test hoặc ACTIVE/BANNED/DELETED; không suy ra thông điệp chưa có trong FR | END:REJECTED | FR-M01-11.10 |


**E2: Hết đủ 14×24 giờ trước lúc xác nhận.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-023 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống từ chối kích hoạt lại; tài khoản hết hạn chuyển DELETED theo tác vụ vòng đời và không được phục hồi. | 01/11 09:00 vô hiệu hóa; xác nhận 15/11 09:00 hoặc sau đó | END:REJECTED | FR-M01-11.05, FR-M01-12.01, FR-M01-12.04, BR-M01-21 |


**E3: Nhập sai mã nhưng tổng số lần sai chưa đến 5.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-023 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | SYSTEM | Hệ thống từ chối lần nhập sai; mã chưa bị vô hiệu bởi ngưỡng 5 lần, tài khoản vẫn DEACTIVATED. | Mã gửi 482731; nhập 482730; tổng lần sai=1 | E3.2 | FR-M01-11.04, FR-M01-11.08, BR-M01-22 |
| E3.2 | ACT-001 | Chủ tài khoản nhập đúng mã đang còn hạn và gửi lại. | 482731; lúc gửi lại 09:10, còn trong 15 phút và cửa sổ 14 ngày | M4 | FR-M01-11.02, BR-M01-22 |


**E4: Lần sai này là lần sai thứ 5.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-023 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | SYSTEM | Hệ thống từ chối và làm mã cũ mất hiệu lực. | Code1 sai lần 5; A01 vẫn DEACTIVATED | E4.2 | FR-M01-11.04, FR-M01-11.08 |
| E4.2 | ACT-001 | Sau khi đã cách lần gửi trước đủ 60 giây, chủ tài khoản yêu cầu mã mới. | Code1 gửi 09:01; xin mới 09:06 | E4.3 | FR-M01-11.01, FR-M01-11.09, BR-M01-22 |
| E4.3 | SYSTEM | Hệ thống gửi mã kích hoạt mới 6 chữ số theo điều kiện cửa sổ còn mở. | Code2=615204 gửi 09:06, hạn 15 phút | E4.4 | FR-M01-11.01 |
| E4.4 | ACT-001 | Chủ tài khoản nhập Code2 còn hạn và gửi. | 615204 lúc 09:10; không dùng lại mã đã mất hiệu lực | M4 | FR-M01-11.02 |


**E5: Mã đã quá 15 phút kể từ lúc gửi.** Thay thế M4; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-023 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | SYSTEM | Hệ thống từ chối mã hết hạn; chưa kích hoạt tài khoản. | Code1 gửi 09:01; gửi xác nhận 09:17 | E5.2 | FR-M01-11.07 |
| E5.2 | ACT-001 | Chủ tài khoản yêu cầu gửi mã mới khi đã đủ khoảng cách 60 giây. | Yêu cầu 09:18; cửa sổ 14 ngày còn mở | E5.3 | FR-M01-11.01, FR-M01-11.09, BR-M01-22 |
| E5.3 | SYSTEM | Hệ thống gửi mã mới theo điều kiện còn trong thời hạn vô hiệu hóa. | Code2=615204 gửi 09:18 | E5.4 | FR-M01-11.01 |
| E5.4 | ACT-001 | Chủ tài khoản nhập mã mới và gửi khi chưa quá hạn. | 615204 gửi 09:20 | M4 | FR-M01-11.02 |


**E6: Chủ tài khoản yêu cầu gửi lại mã trong cùng hành trình kích hoạt lại.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-023 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-001 | Chủ tài khoản nhập email tại trang kích hoạt và yêu cầu gửi lại mã. | an.study@example.test; A01 DEACTIVATED; yêu cầu 09:01 | E6.2 | FR-M01-11.01 |
| E6.2 | SYSTEM | Hệ thống kiểm tài khoản/cửa sổ và khoảng cách gửi lại; gửi mã 6 chữ số tới email. | Code=482731, gửi 09:01; A01 vẫn DEACTIVATED | E6.3 | FR-M01-11.01, FR-M01-11.09, BR-M01-22 |
| E6.3 | ACT-001 | Chủ tài khoản nhập mã nhận trong email và gửi xác nhận. | 482731 lúc 09:10; không có phiên trước yêu cầu | E6.4 | FR-M01-11.02 |
| E6.4 | SYSTEM | Hệ thống kiểm mã còn hiệu lực/hạn và cửa sổ 14 ngày; chuyển ACTIVE, hiển thị lại bài/bình luận với tên/avatar chủ tài khoản và cấp phiên mới cho P01. | A01 ACTIVE; P01 phiên mới; bài P101 và bình luận C101 phục hồi cách hiển thị tên Minh An/avatar cũ | END:SUCCESS | FR-M01-11.02, FR-M01-11.03, FR-M01-11.04, FR-M01-11.05, FR-M01-11.06, FR-M01-11.07, FR-M01-11.08, BR-M01-22, BR-M01-25 |


**E7: Chủ tài khoản yêu cầu gửi lại mã trong cùng hành trình kích hoạt lại; Email không thuộc tài khoản DEACTIVATED.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-023 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | ACT-001 | Chủ tài khoản nhập email tại trang kích hoạt và yêu cầu gửi lại mã. | an.study@example.test; A01 DEACTIVATED; yêu cầu 09:01 | E7.2 | FR-M01-11.01 |
| E7.2 | SYSTEM | Hệ thống không gửi mã kích hoạt lại. | email=noaccount@example.test hoặc ACTIVE/BANNED/DELETED; không suy ra thông điệp chưa có trong FR | END:REJECTED | FR-M01-11.10 |


**E8: Chủ tài khoản yêu cầu gửi lại mã trong cùng hành trình kích hoạt lại; Hết đủ 14×24 giờ trước lúc xác nhận.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-023 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | ACT-001 | Chủ tài khoản nhập email tại trang kích hoạt và yêu cầu gửi lại mã. | an.study@example.test; A01 DEACTIVATED; yêu cầu 09:01 | E8.2 | FR-M01-11.01 |
| E8.2 | SYSTEM | Hệ thống kiểm tài khoản/cửa sổ và khoảng cách gửi lại; gửi mã 6 chữ số tới email. | Code=482731, gửi 09:01; A01 vẫn DEACTIVATED | E8.3 | FR-M01-11.01, FR-M01-11.09, BR-M01-22 |
| E8.3 | ACT-001 | Chủ tài khoản nhập mã nhận trong email và gửi xác nhận. | 482731 lúc 09:10; không có phiên trước yêu cầu | E8.4 | FR-M01-11.02 |
| E8.4 | SYSTEM | Hệ thống từ chối kích hoạt lại; tài khoản hết hạn chuyển DELETED theo tác vụ vòng đời và không được phục hồi. | 01/11 09:00 vô hiệu hóa; xác nhận 15/11 09:00 hoặc sau đó | END:REJECTED | FR-M01-11.05, FR-M01-12.01, FR-M01-12.04, BR-M01-21 |


**E9: Chủ tài khoản yêu cầu gửi lại mã trong cùng hành trình kích hoạt lại; Nhập sai mã nhưng tổng số lần sai chưa đến 5.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-023 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | ACT-001 | Chủ tài khoản nhập email tại trang kích hoạt và yêu cầu gửi lại mã. | an.study@example.test; A01 DEACTIVATED; yêu cầu 09:01 | E9.2 | FR-M01-11.01 |
| E9.2 | SYSTEM | Hệ thống kiểm tài khoản/cửa sổ và khoảng cách gửi lại; gửi mã 6 chữ số tới email. | Code=482731, gửi 09:01; A01 vẫn DEACTIVATED | E9.3 | FR-M01-11.01, FR-M01-11.09, BR-M01-22 |
| E9.3 | ACT-001 | Chủ tài khoản nhập mã nhận trong email và gửi xác nhận. | 482731 lúc 09:10; không có phiên trước yêu cầu | E9.4 | FR-M01-11.02 |
| E9.4 | SYSTEM | Hệ thống từ chối lần nhập sai; mã chưa bị vô hiệu bởi ngưỡng 5 lần, tài khoản vẫn DEACTIVATED. | Mã gửi 482731; nhập 482730; tổng lần sai=1 | E9.5 | FR-M01-11.04, FR-M01-11.08, BR-M01-22 |
| E9.5 | ACT-001 | Chủ tài khoản nhập đúng mã đang còn hạn và gửi lại. | 482731; lúc gửi lại 09:10, còn trong 15 phút và cửa sổ 14 ngày | E9.6 | FR-M01-11.02, BR-M01-22 |
| E9.6 | SYSTEM | Hệ thống kiểm mã còn hiệu lực/hạn và cửa sổ 14 ngày; chuyển ACTIVE, hiển thị lại bài/bình luận với tên/avatar chủ tài khoản và cấp phiên mới cho P01. | A01 ACTIVE; P01 phiên mới; bài P101 và bình luận C101 phục hồi cách hiển thị tên Minh An/avatar cũ | END:SUCCESS | FR-M01-11.02, FR-M01-11.03, FR-M01-11.04, FR-M01-11.05, FR-M01-11.06, FR-M01-11.07, FR-M01-11.08, BR-M01-22, BR-M01-25 |


**E10: Chủ tài khoản yêu cầu gửi lại mã trong cùng hành trình kích hoạt lại; Lần sai này là lần sai thứ 5.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-023 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | ACT-001 | Chủ tài khoản nhập email tại trang kích hoạt và yêu cầu gửi lại mã. | an.study@example.test; A01 DEACTIVATED; yêu cầu 09:01 | E10.2 | FR-M01-11.01 |
| E10.2 | SYSTEM | Hệ thống kiểm tài khoản/cửa sổ và khoảng cách gửi lại; gửi mã 6 chữ số tới email. | Code=482731, gửi 09:01; A01 vẫn DEACTIVATED | E10.3 | FR-M01-11.01, FR-M01-11.09, BR-M01-22 |
| E10.3 | ACT-001 | Chủ tài khoản nhập mã nhận trong email và gửi xác nhận. | 482731 lúc 09:10; không có phiên trước yêu cầu | E10.4 | FR-M01-11.02 |
| E10.4 | SYSTEM | Hệ thống từ chối và làm mã cũ mất hiệu lực. | Code1 sai lần 5; A01 vẫn DEACTIVATED | E10.5 | FR-M01-11.04, FR-M01-11.08 |
| E10.5 | ACT-001 | Sau khi đã cách lần gửi trước đủ 60 giây, chủ tài khoản yêu cầu mã mới. | Code1 gửi 09:01; xin mới 09:06 | E10.6 | FR-M01-11.01, FR-M01-11.09, BR-M01-22 |
| E10.6 | SYSTEM | Hệ thống gửi mã kích hoạt mới 6 chữ số theo điều kiện cửa sổ còn mở. | Code2=615204 gửi 09:06, hạn 15 phút | E10.7 | FR-M01-11.01 |
| E10.7 | ACT-001 | Chủ tài khoản nhập Code2 còn hạn và gửi. | 615204 lúc 09:10; không dùng lại mã đã mất hiệu lực | E10.8 | FR-M01-11.02 |
| E10.8 | SYSTEM | Hệ thống kiểm mã còn hiệu lực/hạn và cửa sổ 14 ngày; chuyển ACTIVE, hiển thị lại bài/bình luận với tên/avatar chủ tài khoản và cấp phiên mới cho P01. | A01 ACTIVE; P01 phiên mới; bài P101 và bình luận C101 phục hồi cách hiển thị tên Minh An/avatar cũ | END:SUCCESS | FR-M01-11.02, FR-M01-11.03, FR-M01-11.04, FR-M01-11.05, FR-M01-11.06, FR-M01-11.07, FR-M01-11.08, BR-M01-22, BR-M01-25 |


**E11: Chủ tài khoản yêu cầu gửi lại mã trong cùng hành trình kích hoạt lại; Mã đã quá 15 phút kể từ lúc gửi.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-023 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-001 | Chủ tài khoản nhập email tại trang kích hoạt và yêu cầu gửi lại mã. | an.study@example.test; A01 DEACTIVATED; yêu cầu 09:01 | E11.2 | FR-M01-11.01 |
| E11.2 | SYSTEM | Hệ thống kiểm tài khoản/cửa sổ và khoảng cách gửi lại; gửi mã 6 chữ số tới email. | Code=482731, gửi 09:01; A01 vẫn DEACTIVATED | E11.3 | FR-M01-11.01, FR-M01-11.09, BR-M01-22 |
| E11.3 | ACT-001 | Chủ tài khoản nhập mã nhận trong email và gửi xác nhận. | 482731 lúc 09:10; không có phiên trước yêu cầu | E11.4 | FR-M01-11.02 |
| E11.4 | SYSTEM | Hệ thống từ chối mã hết hạn; chưa kích hoạt tài khoản. | Code1 gửi 09:01; gửi xác nhận 09:17 | E11.5 | FR-M01-11.07 |
| E11.5 | ACT-001 | Chủ tài khoản yêu cầu gửi mã mới khi đã đủ khoảng cách 60 giây. | Yêu cầu 09:18; cửa sổ 14 ngày còn mở | E11.6 | FR-M01-11.01, FR-M01-11.09, BR-M01-22 |
| E11.6 | SYSTEM | Hệ thống gửi mã mới theo điều kiện còn trong thời hạn vô hiệu hóa. | Code2=615204 gửi 09:18 | E11.7 | FR-M01-11.01 |
| E11.7 | ACT-001 | Chủ tài khoản nhập mã mới và gửi khi chưa quá hạn. | 615204 gửi 09:20 | E11.8 | FR-M01-11.02 |
| E11.8 | SYSTEM | Hệ thống kiểm mã còn hiệu lực/hạn và cửa sổ 14 ngày; chuyển ACTIVE, hiển thị lại bài/bình luận với tên/avatar chủ tài khoản và cấp phiên mới cho P01. | A01 ACTIVE; P01 phiên mới; bài P101 và bình luận C101 phục hồi cách hiển thị tên Minh An/avatar cũ | END:SUCCESS | FR-M01-11.02, FR-M01-11.03, FR-M01-11.04, FR-M01-11.05, FR-M01-11.06, FR-M01-11.07, FR-M01-11.08, BR-M01-22, BR-M01-25 |


**E12: Chủ tài khoản yêu cầu gửi lại mã trong cùng hành trình kích hoạt lại; Đang yêu cầu gửi lại nhưng chưa đủ 60 giây từ lần gửi trước.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-023 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | ACT-001 | Chủ tài khoản nhập email tại trang kích hoạt và yêu cầu gửi lại mã. | an.study@example.test; A01 DEACTIVATED; yêu cầu 09:01 | E12.2 | FR-M01-11.01 |
| E12.2 | SYSTEM | Hệ thống từ chối gửi mã mới ở thời điểm chưa đủ khoảng cách. | Lần trước 09:00; yêu cầu 09:00:40 | E12.3 | FR-M01-11.09 |
| E12.3 | ACT-001 | Sau khi đủ 60 giây và còn trong cửa sổ kích hoạt lại, chủ tài khoản yêu cầu mã mới. | Yêu cầu 09:01:05 | E12.4 | FR-M01-11.01, FR-M01-11.09, BR-M01-22 |
| E12.4 | SYSTEM | Hệ thống kiểm tài khoản/cửa sổ và khoảng cách gửi lại; gửi mã 6 chữ số tới email. | Code=482731, gửi 09:01; A01 vẫn DEACTIVATED | E12.5 | FR-M01-11.01, FR-M01-11.09, BR-M01-22 |
| E12.5 | ACT-001 | Chủ tài khoản nhập mã nhận trong email và gửi xác nhận. | 482731 lúc 09:10; không có phiên trước yêu cầu | E12.6 | FR-M01-11.02 |
| E12.6 | SYSTEM | Hệ thống kiểm mã còn hiệu lực/hạn và cửa sổ 14 ngày; chuyển ACTIVE, hiển thị lại bài/bình luận với tên/avatar chủ tài khoản và cấp phiên mới cho P01. | A01 ACTIVE; P01 phiên mới; bài P101 và bình luận C101 phục hồi cách hiển thị tên Minh An/avatar cũ | END:SUCCESS | FR-M01-11.02, FR-M01-11.03, FR-M01-11.04, FR-M01-11.05, FR-M01-11.06, FR-M01-11.07, FR-M01-11.08, BR-M01-22, BR-M01-25 |


**Ghi chú đường đi và giới hạn:** Luồng chính hoàn tất mục tiêu; các trường hợp trong mục 6 là đường thay thế, không chạy nối tiếp tất cả nhánh. Guard mô tả dữ liệu/ngữ cảnh thay thế của chính lần thực thi. Nhánh sửa gửi lại áp cùng điều kiện kiểm tra; không có giới hạn thử mới ngoài nguồn. Các GAP ở mục cuối vẫn áp dụng.

<!-- sc:end SC-M01-023 -->

<!-- sc:scenario SC-M01-025 -->

<a id="sc-m01-025"></a>

### SC-M01-025 — Mod/Admin xem bài ẩn và danh tính tác giả DEACTIVATED

#### 1. Tên kịch bản chuẩn

**Mod/Admin xem bài ẩn và danh tính tác giả DEACTIVATED** — BF-M01-025; UC owner: [UC-M01-011](../../us/US-M01.md#uc-m01-011); nhóm chi tiết: UC-M01-023. Trigger: Người kiểm duyệt mở bài của tác giả vô hiệu hóa.

#### 2. Actor thực hiện

ACT-003 Mod/Admin; SYSTEM kiểm quyền và trạng thái.

#### 3. Tiền điều kiện

Người kiểm duyệt có phiên khi gửi yêu cầu. Đường chuẩn có vai trò MOD/ADMIN hợp lệ; hệ thống kiểm lại quyền và trạng thái trước khi trả dữ liệu. Bài P101 có tác giả A01 DEACTIVATED ở đường chuẩn. Không phục hồi dữ liệu cá nhân DELETED.

#### 4. Hậu điều kiện

<!-- sc:post SC-M01-025 -->

| result | condition |
|---|---|
| SUCCESS | ACT-003 xem được bài/danh tính thật trong giới hạn DEACTIVATED; người xem thông thường vẫn theo cách hiển thị thay thế. |
| REJECTED | Không cung cấp bài/danh tính thật; nội dung ẩn không bị lộ qua đường truy cập trực tiếp. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M01-025 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-003 | Mod/Admin yêu cầu xem bài bị ẩn và danh tính tác giả. | P101; A01 DEACTIVATED; tên thật còn lưu Minh An; username An_12A1 | M2 | FR-M01-13.05 |
| M2 | SYSTEM | Hệ thống kiểm vai trò và trạng thái, hiển thị bài bị ẩn cùng danh tính thật còn được lưu của tác giả. | P101 và nội dung gốc; Minh An/An_12A1; không đổi trạng thái A01 hoặc công khai lại bài cho người khác | END:SUCCESS | FR-M01-13.05, BR-M01-41 |


#### 6. Các ngoại lệ

<!-- sc:exceptions SC-M01-025 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | system | M2 | Tác giả đã DELETED ở snapshot trả dữ liệu | E1.1 | FR-M01-13.01, FR-M01-13.02, FR-M01-12.08, FR-M01-12.10, BR-M01-41, BR-M01-47 |
| E2 | system | M2 | Quyền Mod/Admin hoặc phiên của người kiểm duyệt không còn hợp lệ lúc hệ thống trả dữ liệu; không được dùng yêu cầu đã gửi để vượt kiểm quyền | E2.1 | FR-M01-13.01, FR-M01-13.02, BR-M01-23, BR-M01-24, BR-M01-41 |


**E1: Tác giả đã DELETED ở snapshot trả dữ liệu.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-025 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | SYSTEM | Hệ thống không cung cấp danh tính thật đã xóa; bài vẫn ẩn. Nhật ký kiểm duyệt/AI còn liên kết qua username, không dùng để tái tạo thông tin cá nhân. | A01 DELETED; username An_12A1 giữ vĩnh viễn; display_name/email/avatar đã xóa | END:REJECTED | FR-M01-13.01, FR-M01-13.02, FR-M01-12.08, FR-M01-12.10, BR-M01-41, BR-M01-47 |


**E2: Quyền Mod/Admin hoặc phiên của người kiểm duyệt không còn hợp lệ lúc hệ thống trả dữ liệu; không được dùng yêu cầu đã gửi để vượt kiểm quyền.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-025 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | SYSTEM | Hệ thống áp dụng hiển thị thay thế, không trả bài ẩn hoặc danh tính thật; hiển thị đúng thông điệp Nội dung không tồn tại. | Thông điệp="Nội dung không tồn tại"; danh tính thật không cung cấp; bình luận/tin nhắn theo RULE-M01-001 ở phụ lục | END:REJECTED | FR-M01-13.01, FR-M01-13.02, BR-M01-23, BR-M01-24, BR-M01-41 |


**Ghi chú đường đi và giới hạn:** Luồng chính hoàn tất mục tiêu; các trường hợp trong mục 6 là đường thay thế, không chạy nối tiếp tất cả nhánh. Guard mô tả dữ liệu/ngữ cảnh thay thế của chính lần thực thi. Nhánh sửa gửi lại áp cùng điều kiện kiểm tra; không có giới hạn thử mới ngoài nguồn. Các GAP ở mục cuối vẫn áp dụng.

<!-- sc:end SC-M01-025 -->

<!-- sc:scenario SC-M01-034 -->

<a id="sc-m01-034"></a>

### SC-M01-034 — Nhắc một tài khoản trong nội dung đang soạn

#### 1. Tên kịch bản chuẩn

**Nhắc một tài khoản trong nội dung đang soạn** — BF-M01-034; UC owner: [UC-M01-025](../../us/US-M01.md#uc-m01-025); nhóm chi tiết: UC-M01-025. Trigger: Người có phiên quyết định nhắc người khác trong bài/bình luận.

#### 2. Actor thực hiện

ACT-002 người soạn; ACT-003 theo quyền soạn tương ứng.

#### 3. Tiền điều kiện

Đang có bản soạn bài hoặc bình luận theo module sở hữu. Đường chuẩn ACT-002 được phép soạn trong G12, DRAFT-101 chưa công khai; các nhánh thay ngữ cảnh trong/ngoài Group theo bài chứa bình luận. Hệ thống kiểm lại phiên tại lúc gợi ý. Quyền công khai thuộc M03/M04; mục tiêu tại đây là chèn khối nhắc vào bản soạn.

#### 4. Hậu điều kiện

<!-- sc:post SC-M01-034 -->

| result | condition |
|---|---|
| SUCCESS | Mục tiêu UC-M01-025 hoàn tất tại bản soạn có tham chiếu đúng tài khoản được chọn: U203 trong luồng chính, U202 trong lựa chọn thay thế; công khai nội dung sau này kích hoạt AUT-M01-005. |
| REJECTED | Không có khối nhắc mới được chèn từ yêu cầu không đủ điều kiện hoặc không có ứng viên; bản soạn không bị gán nhầm người. |
| CANCELLED | Actor đã xóa toàn bộ khối nhắc vừa chèn; bản soạn không còn lượt nhắc đó, không phát thông báo do thao tác bản soạn. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M01-034 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Người soạn gõ @Lan trong bài viết trong Group G12 và ngừng gõ 300 mili giây. | Chuỗi tìm Lan; bản soạn DRAFT-101; @ một mình chưa đủ điều kiện | M2 | FR-M01-14.01 |
| M2 | SYSTEM | Hệ thống tìm theo display_name và username, khớp mọi vị trí, bỏ phân biệt hoa/thường và dấu, hỗ trợ sai nhẹ/khoảng trắng; lọc tài khoản không hợp lệ, xếp người đang theo dõi → thành viên chính G12 → người còn lại rồi theo độ khớp trong mỗi tầng, trả tối đa 5 người. | D-MENTION-G: truy vấn "Lan"; G12 là Group bài. U201=Lan (đang theo dõi), U202=Lan Anh (đang theo dõi), U203=Lan Chi (cùng G12), U204=Lan Hương (chỉ chung G99, không G12), U205=Lan Mai (khác), U206=Hoàng Lan (khác). Thứ tự minh họa: U201,U202,U203,U204,U205; U206 ngoài top 5. U204/U205 được giả lập có độ khớp khác nhau để không tự đặt quy tắc phá hòa. U207=Lan cũ DEACTIVATED; U208=Lan xóa DELETED; U209=Lan khóa BANNED; U210=Lan mới EMAIL_VERIFIED đều bị loại.; mỗi dòng có avatar, display_name và username mờ | M3 | FR-M01-14.01, FR-M01-14.02, FR-M01-14.03, FR-M01-14.04, FR-M01-14.05, FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.12, FR-M01-14.13, FR-M01-14.14, BR-M01-26, BR-M01-27, BR-M01-28, BR-M01-29, BR-M01-40 |
| M3 | ACT-002 | Người soạn chọn U203 Lan Chi từ danh sách gợi ý. | U203 ACTIVE/SETUP_COMPLETED; username=lan_chi; danh sách hiện có U203 | M4 | FR-M01-14.06 |
| M4 | SYSTEM | Hệ thống chèn khối nhắc tên gắn U203; nhãn là display_name hiện tại Lan Chi, làm nổi bật, không có @ và không sửa từng ký tự; chưa gửi thông báo vì nội dung chỉ là bản soạn. | Khối tài khoản U203, nhãn Lan Chi; không phải chuỗi tên tự do; DRAFT-101 vẫn chưa công khai | END:SUCCESS | FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.10, BR-M01-28, BR-M01-29, BR-M01-30 |


#### 6. Các ngoại lệ

<!-- sc:exceptions SC-M01-034 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M3 | Người soạn muốn thay lựa chọn ban đầu bằng một người khác đang có trong gợi ý | E1.1 | FR-M01-14.06, FR-M01-14.07, FR-M01-14.10, BR-M01-28, BR-M01-30 |
| E2 | user-choice | M1 | Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bài viết trong Group G12 | E2.1 | FR-M01-14.01, FR-M01-14.02, FR-M01-14.03, FR-M01-14.04, FR-M01-14.05, FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.12, FR-M01-14.13, FR-M01-14.14, BR-M01-26, BR-M01-27, BR-M01-28, BR-M01-29, BR-M01-40, FR-M01-14.10, BR-M01-30 |
| E3 | user-choice | M1 | Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bài viết trong Group G12; Chỉ gõ @, hoặc chưa đạt 300 ms kể từ lần gõ gần nhất | E3.1 | FR-M01-14.01, BR-M01-26 |
| E4 | user-choice | M1 | Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bài viết trong Group G12; Không còn tài khoản phù hợp sau lọc | E4.1 | FR-M01-14.01, FR-M01-14.14, BR-M01-40 |
| E5 | user-choice | M1 | Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bài viết ngoài Group | E5.1 | FR-M01-14.01, FR-M01-14.02, FR-M01-14.03, FR-M01-14.04, FR-M01-14.05, FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.12, FR-M01-14.13, FR-M01-14.14, BR-M01-26, BR-M01-27, BR-M01-28, BR-M01-29, BR-M01-40, FR-M01-14.10, BR-M01-30 |
| E6 | user-choice | M1 | Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bài viết ngoài Group; Chỉ gõ @, hoặc chưa đạt 300 ms kể từ lần gõ gần nhất | E6.1 | FR-M01-14.01, BR-M01-26 |
| E7 | user-choice | M1 | Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bài viết ngoài Group; Không còn tài khoản phù hợp sau lọc | E7.1 | FR-M01-14.01, FR-M01-14.14, BR-M01-40 |
| E8 | user-choice | M1 | Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bình luận trên bài trong Group G12 | E8.1 | FR-M01-14.01, FR-M01-14.02, FR-M01-14.03, FR-M01-14.04, FR-M01-14.05, FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.12, FR-M01-14.13, FR-M01-14.14, BR-M01-26, BR-M01-27, BR-M01-28, BR-M01-29, BR-M01-40, FR-M01-14.10, BR-M01-30 |
| E9 | user-choice | M1 | Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bình luận trên bài trong Group G12; Chỉ gõ @, hoặc chưa đạt 300 ms kể từ lần gõ gần nhất | E9.1 | FR-M01-14.01, BR-M01-26 |
| E10 | user-choice | M1 | Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bình luận trên bài trong Group G12; Không còn tài khoản phù hợp sau lọc | E10.1 | FR-M01-14.01, FR-M01-14.14, BR-M01-40 |
| E11 | user-choice | M1 | Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bình luận trên bài ngoài Group | E11.1 | FR-M01-14.01, FR-M01-14.02, FR-M01-14.03, FR-M01-14.04, FR-M01-14.05, FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.12, FR-M01-14.13, FR-M01-14.14, BR-M01-26, BR-M01-27, BR-M01-28, BR-M01-29, BR-M01-40, FR-M01-14.10, BR-M01-30 |
| E12 | user-choice | M1 | Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bình luận trên bài ngoài Group; Chỉ gõ @, hoặc chưa đạt 300 ms kể từ lần gõ gần nhất | E12.1 | FR-M01-14.01, BR-M01-26 |
| E13 | user-choice | M1 | Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bình luận trên bài ngoài Group; Không còn tài khoản phù hợp sau lọc | E13.1 | FR-M01-14.01, FR-M01-14.14, BR-M01-40 |
| E14 | user-choice | M3 | Sau khi chọn người được nhắc, actor xóa lùi vào khối vừa chèn | E14.1 | FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.10, BR-M01-28, BR-M01-29, BR-M01-30, FR-M01-14.09 |
| E15 | user-choice | M3 | Sau khi chọn người được nhắc, actor thử sửa nhãn khối rồi chọn xóa trọn khối | E15.1 | FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.10, BR-M01-28, BR-M01-29, BR-M01-30, FR-M01-14.09 |
| E16 | system | M2 | Yêu cầu gợi ý không có phiên đăng nhập hợp lệ tại thời điểm kiểm tra | E16.1 | FR-M01-14.11 |


**E1: Người soạn muốn thay lựa chọn ban đầu bằng một người khác đang có trong gợi ý.** Thay thế M3; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Người soạn chọn U202 Lan Anh thay vì U203. | U202 ACTIVE/SETUP_COMPLETED, có trong top 5 | E1.2 | FR-M01-14.06 |
| E1.2 | SYSTEM | Hệ thống chèn khối gắn U202 với display_name Lan Anh, làm nổi bật và không có @; chưa gửi thông báo. | Khối U202; bản soạn chưa công khai | END:SUCCESS | FR-M01-14.06, FR-M01-14.07, FR-M01-14.10, BR-M01-28, BR-M01-30 |


**E2: Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bài viết trong Group G12.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | Người soạn gõ @Lan trong bài viết trong Group G12 và ngừng gõ 300 mili giây. | Chuỗi tìm Lan; bản soạn DRAFT-101; @ một mình chưa đủ điều kiện | E2.2 | FR-M01-14.01 |
| E2.2 | SYSTEM | Hệ thống tìm theo display_name và username, khớp mọi vị trí, bỏ phân biệt hoa/thường và dấu, hỗ trợ sai nhẹ/khoảng trắng; lọc tài khoản không hợp lệ, xếp người đang theo dõi → thành viên chính G12 → người còn lại rồi theo độ khớp trong mỗi tầng, trả tối đa 5 người. | D-MENTION-G: truy vấn "Lan"; G12 là Group bài. U201=Lan (đang theo dõi), U202=Lan Anh (đang theo dõi), U203=Lan Chi (cùng G12), U204=Lan Hương (chỉ chung G99, không G12), U205=Lan Mai (khác), U206=Hoàng Lan (khác). Thứ tự minh họa: U201,U202,U203,U204,U205; U206 ngoài top 5. U204/U205 được giả lập có độ khớp khác nhau để không tự đặt quy tắc phá hòa. U207=Lan cũ DEACTIVATED; U208=Lan xóa DELETED; U209=Lan khóa BANNED; U210=Lan mới EMAIL_VERIFIED đều bị loại.; mỗi dòng có avatar, display_name và username mờ | E2.3 | FR-M01-14.01, FR-M01-14.02, FR-M01-14.03, FR-M01-14.04, FR-M01-14.05, FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.12, FR-M01-14.13, FR-M01-14.14, BR-M01-26, BR-M01-27, BR-M01-28, BR-M01-29, BR-M01-40 |
| E2.3 | ACT-002 | Người soạn chọn U203 Lan Chi từ danh sách gợi ý. | U203 ACTIVE/SETUP_COMPLETED; username=lan_chi; danh sách hiện có U203 | E2.4 | FR-M01-14.06 |
| E2.4 | SYSTEM | Hệ thống chèn khối nhắc tên gắn U203; nhãn là display_name hiện tại Lan Chi, làm nổi bật, không có @ và không sửa từng ký tự; chưa gửi thông báo vì nội dung chỉ là bản soạn. | Khối tài khoản U203, nhãn Lan Chi; không phải chuỗi tên tự do; DRAFT-101 vẫn chưa công khai | END:SUCCESS | FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.10, BR-M01-28, BR-M01-29, BR-M01-30 |


**E3: Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bài viết trong Group G12; Chỉ gõ @, hoặc chưa đạt 300 ms kể từ lần gõ gần nhất.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-002 | Người soạn chỉ gõ @, hoặc gõ @Lan nhưng mới ngừng 200 mili giây. | @ chưa có ký tự tìm; hoặc @Lan mới ngừng 200 ms | E3.2 | FR-M01-14.01, BR-M01-26 |
| E3.2 | SYSTEM | Hệ thống chưa mở/tìm gợi ý theo trigger; không chèn lượt nhắc. | Chưa đạt điều kiện ít nhất một ký tự và ngừng gõ 300 ms; khi người soạn tiếp tục đủ điều kiện thì khởi tạo luồng chính | END:REJECTED | FR-M01-14.01, BR-M01-26 |


**E4: Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bài viết trong Group G12; Không còn tài khoản phù hợp sau lọc.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-002 | Người soạn gõ @Lan trong bài viết trong Group G12 và ngừng gõ 300 mili giây. | Chuỗi tìm Lan; bản soạn DRAFT-101; @ một mình chưa đủ điều kiện | E4.2 | FR-M01-14.01 |
| E4.2 | SYSTEM | Hệ thống không đưa tài khoản bị loại vào gợi ý; chưa có lựa chọn hợp lệ để chèn lượt nhắc. Không tự sáng tác thông báo cho danh sách rỗng. | Mọi ứng viên đều DEACTIVATED/DELETED/BANNED/chưa SETUP_COMPLETED hoặc không khớp | END:REJECTED | FR-M01-14.14, BR-M01-40 |


**E5: Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bài viết ngoài Group.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E5 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E5.1 | ACT-002 | Người soạn gõ @Lan trong bài viết ngoài Group và ngừng gõ 300 mili giây. | Chuỗi tìm Lan; bản soạn DRAFT-101; @ một mình chưa đủ điều kiện | E5.2 | FR-M01-14.01 |
| E5.2 | SYSTEM | Hệ thống tìm theo display_name và username, khớp mọi vị trí, bỏ phân biệt hoa/thường và dấu, hỗ trợ sai nhẹ/khoảng trắng; lọc tài khoản không hợp lệ, xếp người đang theo dõi → người có chung ít nhất một Group → người còn lại rồi theo độ khớp trong mỗi tầng, trả tối đa 5 người. | D-MENTION-P: truy vấn "Lan"; ngoài Group. U201=Lan và U202=Lan Anh đang theo dõi; U204=Lan Hương có chung G99 với người soạn; U203=Lan Chi không có Group chung trong snapshot này; U205=Lan Mai và U206=Hoàng Lan còn lại. Trả U201,U202,U204,U203,U205, tối đa 5. U203/U205 giả lập có độ khớp khác nhau; U207/U208/U209/U210 bị loại như D-MENTION-G.; mỗi dòng có avatar, display_name và username mờ | E5.3 | FR-M01-14.01, FR-M01-14.02, FR-M01-14.03, FR-M01-14.04, FR-M01-14.05, FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.12, FR-M01-14.13, FR-M01-14.14, BR-M01-26, BR-M01-27, BR-M01-28, BR-M01-29, BR-M01-40 |
| E5.3 | ACT-002 | Người soạn chọn U203 Lan Chi từ danh sách gợi ý. | U203 ACTIVE/SETUP_COMPLETED; username=lan_chi; danh sách hiện có U203 | E5.4 | FR-M01-14.06 |
| E5.4 | SYSTEM | Hệ thống chèn khối nhắc tên gắn U203; nhãn là display_name hiện tại Lan Chi, làm nổi bật, không có @ và không sửa từng ký tự; chưa gửi thông báo vì nội dung chỉ là bản soạn. | Khối tài khoản U203, nhãn Lan Chi; không phải chuỗi tên tự do; DRAFT-101 vẫn chưa công khai | END:SUCCESS | FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.10, BR-M01-28, BR-M01-29, BR-M01-30 |


**E6: Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bài viết ngoài Group; Chỉ gõ @, hoặc chưa đạt 300 ms kể từ lần gõ gần nhất.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E6 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E6.1 | ACT-002 | Người soạn chỉ gõ @, hoặc gõ @Lan nhưng mới ngừng 200 mili giây. | @ chưa có ký tự tìm; hoặc @Lan mới ngừng 200 ms | E6.2 | FR-M01-14.01, BR-M01-26 |
| E6.2 | SYSTEM | Hệ thống chưa mở/tìm gợi ý theo trigger; không chèn lượt nhắc. | Chưa đạt điều kiện ít nhất một ký tự và ngừng gõ 300 ms; khi người soạn tiếp tục đủ điều kiện thì khởi tạo luồng chính | END:REJECTED | FR-M01-14.01, BR-M01-26 |


**E7: Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bài viết ngoài Group; Không còn tài khoản phù hợp sau lọc.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E7 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E7.1 | ACT-002 | Người soạn gõ @Lan trong bài viết ngoài Group và ngừng gõ 300 mili giây. | Chuỗi tìm Lan; bản soạn DRAFT-101; @ một mình chưa đủ điều kiện | E7.2 | FR-M01-14.01 |
| E7.2 | SYSTEM | Hệ thống không đưa tài khoản bị loại vào gợi ý; chưa có lựa chọn hợp lệ để chèn lượt nhắc. Không tự sáng tác thông báo cho danh sách rỗng. | Mọi ứng viên đều DEACTIVATED/DELETED/BANNED/chưa SETUP_COMPLETED hoặc không khớp | END:REJECTED | FR-M01-14.14, BR-M01-40 |


**E8: Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bình luận trên bài trong Group G12.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E8 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E8.1 | ACT-002 | Người soạn gõ @Lan trong bình luận trên bài trong Group G12 và ngừng gõ 300 mili giây. | Chuỗi tìm Lan; bản soạn DRAFT-101; @ một mình chưa đủ điều kiện | E8.2 | FR-M01-14.01 |
| E8.2 | SYSTEM | Hệ thống tìm theo display_name và username, khớp mọi vị trí, bỏ phân biệt hoa/thường và dấu, hỗ trợ sai nhẹ/khoảng trắng; lọc tài khoản không hợp lệ, xếp người đang theo dõi → thành viên chính G12 → người còn lại rồi theo độ khớp trong mỗi tầng, trả tối đa 5 người. | D-MENTION-G: truy vấn "Lan"; G12 là Group bài. U201=Lan (đang theo dõi), U202=Lan Anh (đang theo dõi), U203=Lan Chi (cùng G12), U204=Lan Hương (chỉ chung G99, không G12), U205=Lan Mai (khác), U206=Hoàng Lan (khác). Thứ tự minh họa: U201,U202,U203,U204,U205; U206 ngoài top 5. U204/U205 được giả lập có độ khớp khác nhau để không tự đặt quy tắc phá hòa. U207=Lan cũ DEACTIVATED; U208=Lan xóa DELETED; U209=Lan khóa BANNED; U210=Lan mới EMAIL_VERIFIED đều bị loại.; mỗi dòng có avatar, display_name và username mờ | E8.3 | FR-M01-14.01, FR-M01-14.02, FR-M01-14.03, FR-M01-14.04, FR-M01-14.05, FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.12, FR-M01-14.13, FR-M01-14.14, BR-M01-26, BR-M01-27, BR-M01-28, BR-M01-29, BR-M01-40 |
| E8.3 | ACT-002 | Người soạn chọn U203 Lan Chi từ danh sách gợi ý. | U203 ACTIVE/SETUP_COMPLETED; username=lan_chi; danh sách hiện có U203 | E8.4 | FR-M01-14.06 |
| E8.4 | SYSTEM | Hệ thống chèn khối nhắc tên gắn U203; nhãn là display_name hiện tại Lan Chi, làm nổi bật, không có @ và không sửa từng ký tự; chưa gửi thông báo vì nội dung chỉ là bản soạn. | Khối tài khoản U203, nhãn Lan Chi; không phải chuỗi tên tự do; DRAFT-101 vẫn chưa công khai | END:SUCCESS | FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.10, BR-M01-28, BR-M01-29, BR-M01-30 |


**E9: Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bình luận trên bài trong Group G12; Chỉ gõ @, hoặc chưa đạt 300 ms kể từ lần gõ gần nhất.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E9 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E9.1 | ACT-002 | Người soạn chỉ gõ @, hoặc gõ @Lan nhưng mới ngừng 200 mili giây. | @ chưa có ký tự tìm; hoặc @Lan mới ngừng 200 ms | E9.2 | FR-M01-14.01, BR-M01-26 |
| E9.2 | SYSTEM | Hệ thống chưa mở/tìm gợi ý theo trigger; không chèn lượt nhắc. | Chưa đạt điều kiện ít nhất một ký tự và ngừng gõ 300 ms; khi người soạn tiếp tục đủ điều kiện thì khởi tạo luồng chính | END:REJECTED | FR-M01-14.01, BR-M01-26 |


**E10: Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bình luận trên bài trong Group G12; Không còn tài khoản phù hợp sau lọc.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E10 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E10.1 | ACT-002 | Người soạn gõ @Lan trong bình luận trên bài trong Group G12 và ngừng gõ 300 mili giây. | Chuỗi tìm Lan; bản soạn DRAFT-101; @ một mình chưa đủ điều kiện | E10.2 | FR-M01-14.01 |
| E10.2 | SYSTEM | Hệ thống không đưa tài khoản bị loại vào gợi ý; chưa có lựa chọn hợp lệ để chèn lượt nhắc. Không tự sáng tác thông báo cho danh sách rỗng. | Mọi ứng viên đều DEACTIVATED/DELETED/BANNED/chưa SETUP_COMPLETED hoặc không khớp | END:REJECTED | FR-M01-14.14, BR-M01-40 |


**E11: Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bình luận trên bài ngoài Group.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E11 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E11.1 | ACT-002 | Người soạn gõ @Lan trong bình luận trên bài ngoài Group và ngừng gõ 300 mili giây. | Chuỗi tìm Lan; bản soạn DRAFT-101; @ một mình chưa đủ điều kiện | E11.2 | FR-M01-14.01 |
| E11.2 | SYSTEM | Hệ thống tìm theo display_name và username, khớp mọi vị trí, bỏ phân biệt hoa/thường và dấu, hỗ trợ sai nhẹ/khoảng trắng; lọc tài khoản không hợp lệ, xếp người đang theo dõi → người có chung ít nhất một Group → người còn lại rồi theo độ khớp trong mỗi tầng, trả tối đa 5 người. | D-MENTION-P: truy vấn "Lan"; ngoài Group. U201=Lan và U202=Lan Anh đang theo dõi; U204=Lan Hương có chung G99 với người soạn; U203=Lan Chi không có Group chung trong snapshot này; U205=Lan Mai và U206=Hoàng Lan còn lại. Trả U201,U202,U204,U203,U205, tối đa 5. U203/U205 giả lập có độ khớp khác nhau; U207/U208/U209/U210 bị loại như D-MENTION-G.; mỗi dòng có avatar, display_name và username mờ | E11.3 | FR-M01-14.01, FR-M01-14.02, FR-M01-14.03, FR-M01-14.04, FR-M01-14.05, FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.12, FR-M01-14.13, FR-M01-14.14, BR-M01-26, BR-M01-27, BR-M01-28, BR-M01-29, BR-M01-40 |
| E11.3 | ACT-002 | Người soạn chọn U203 Lan Chi từ danh sách gợi ý. | U203 ACTIVE/SETUP_COMPLETED; username=lan_chi; danh sách hiện có U203 | E11.4 | FR-M01-14.06 |
| E11.4 | SYSTEM | Hệ thống chèn khối nhắc tên gắn U203; nhãn là display_name hiện tại Lan Chi, làm nổi bật, không có @ và không sửa từng ký tự; chưa gửi thông báo vì nội dung chỉ là bản soạn. | Khối tài khoản U203, nhãn Lan Chi; không phải chuỗi tên tự do; DRAFT-101 vẫn chưa công khai | END:SUCCESS | FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.10, BR-M01-28, BR-M01-29, BR-M01-30 |


**E12: Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bình luận trên bài ngoài Group; Chỉ gõ @, hoặc chưa đạt 300 ms kể từ lần gõ gần nhất.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E12 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E12.1 | ACT-002 | Người soạn chỉ gõ @, hoặc gõ @Lan nhưng mới ngừng 200 mili giây. | @ chưa có ký tự tìm; hoặc @Lan mới ngừng 200 ms | E12.2 | FR-M01-14.01, BR-M01-26 |
| E12.2 | SYSTEM | Hệ thống chưa mở/tìm gợi ý theo trigger; không chèn lượt nhắc. | Chưa đạt điều kiện ít nhất một ký tự và ngừng gõ 300 ms; khi người soạn tiếp tục đủ điều kiện thì khởi tạo luồng chính | END:REJECTED | FR-M01-14.01, BR-M01-26 |


**E13: Ngữ cảnh soạn thay thế: Chèn lượt nhắc tên khi soạn bình luận trên bài ngoài Group; Không còn tài khoản phù hợp sau lọc.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E13 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E13.1 | ACT-002 | Người soạn gõ @Lan trong bình luận trên bài ngoài Group và ngừng gõ 300 mili giây. | Chuỗi tìm Lan; bản soạn DRAFT-101; @ một mình chưa đủ điều kiện | E13.2 | FR-M01-14.01 |
| E13.2 | SYSTEM | Hệ thống không đưa tài khoản bị loại vào gợi ý; chưa có lựa chọn hợp lệ để chèn lượt nhắc. Không tự sáng tác thông báo cho danh sách rỗng. | Mọi ứng viên đều DEACTIVATED/DELETED/BANNED/chưa SETUP_COMPLETED hoặc không khớp | END:REJECTED | FR-M01-14.14, BR-M01-40 |


**E14: Sau khi chọn người được nhắc, actor xóa lùi vào khối vừa chèn.** Thay thế M3; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E14 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E14.1 | ACT-002 | Người soạn chọn U203 Lan Chi từ danh sách gợi ý. | U203 ACTIVE/SETUP_COMPLETED; username=lan_chi; danh sách hiện có U203 | E14.2 | FR-M01-14.06 |
| E14.2 | SYSTEM | Hệ thống chèn khối nhắc tên gắn U203; nhãn là display_name hiện tại Lan Chi, làm nổi bật, không có @ và không sửa từng ký tự; chưa gửi thông báo vì nội dung chỉ là bản soạn. | Khối tài khoản U203, nhãn Lan Chi; không phải chuỗi tên tự do; DRAFT-101 vẫn chưa công khai | E14.3 | FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.10, BR-M01-28, BR-M01-29, BR-M01-30 |
| E14.3 | ACT-002 | Người soạn xóa lùi vào khối nhắc Lan Chi. | Khối U203; con trỏ tại ranh giới khối | E14.4 | FR-M01-14.09 |
| E14.4 | SYSTEM | Hệ thống xóa toàn bộ lượt nhắc U203, không để lại một phần nhãn thành lượt nhắc khác. | Khối U203 không còn trong DRAFT-101; không còn nhãn Lan Ch; không phát thông báo mới chỉ vì xóa ở bản soạn | END:CANCELLED | FR-M01-14.08, FR-M01-14.09, BR-M01-29 |


**E15: Sau khi chọn người được nhắc, actor thử sửa nhãn khối rồi chọn xóa trọn khối.** Thay thế M3; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E15 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E15.1 | ACT-002 | Người soạn chọn U203 Lan Chi từ danh sách gợi ý. | U203 ACTIVE/SETUP_COMPLETED; username=lan_chi; danh sách hiện có U203 | E15.2 | FR-M01-14.06 |
| E15.2 | SYSTEM | Hệ thống chèn khối nhắc tên gắn U203; nhãn là display_name hiện tại Lan Chi, làm nổi bật, không có @ và không sửa từng ký tự; chưa gửi thông báo vì nội dung chỉ là bản soạn. | Khối tài khoản U203, nhãn Lan Chi; không phải chuỗi tên tự do; DRAFT-101 vẫn chưa công khai | E15.3 | FR-M01-14.06, FR-M01-14.07, FR-M01-14.08, FR-M01-14.10, BR-M01-28, BR-M01-29, BR-M01-30 |
| E15.3 | ACT-002 | Người soạn cố đổi nhãn Lan Chi thành tên khác trong khối. | Khối U203; nhãn mong đổi thành Lan Ch | E15.4 | FR-M01-14.08 |
| E15.4 | SYSTEM | Hệ thống không cho sửa nhãn của khối; giữ tham chiếu tài khoản và nhãn hiện tại. Nếu người soạn chọn xóa lùi thì dùng luồng xóa trọn khối. | U203 và Lan Chi không đổi; không chuyển khối sang tên tự do | E15.5 | FR-M01-14.08, BR-M01-29 |
| E15.5 | ACT-002 | Người soạn xóa lùi vào khối nhắc Lan Chi. | Khối U203; con trỏ tại ranh giới khối | E15.6 | FR-M01-14.09 |
| E15.6 | SYSTEM | Hệ thống xóa toàn bộ lượt nhắc U203, không để lại một phần nhãn thành lượt nhắc khác. | Khối U203 không còn trong DRAFT-101; không còn nhãn Lan Ch; không phát thông báo mới chỉ vì xóa ở bản soạn | END:CANCELLED | FR-M01-14.08, FR-M01-14.09, BR-M01-29 |


**E16: Yêu cầu gợi ý không có phiên đăng nhập hợp lệ tại thời điểm kiểm tra.** Thay thế M2; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-034 E16 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E16.1 | SYSTEM | Hệ thống không hiển thị gợi ý nhắc tên cho yêu cầu chưa đăng nhập và không chèn khối. | Không có danh sách được cung cấp; không có lượt nhắc mới | END:REJECTED | FR-M01-14.11 |


**Ghi chú đường đi và giới hạn:** Luồng chính hoàn tất mục tiêu; các trường hợp trong mục 6 là đường thay thế, không chạy nối tiếp tất cả nhánh. Guard mô tả dữ liệu/ngữ cảnh thay thế của chính lần thực thi. Nhánh sửa gửi lại áp cùng điều kiện kiểm tra; không có giới hạn thử mới ngoài nguồn. Các GAP ở mục cuối vẫn áp dụng.

<!-- sc:end SC-M01-034 -->

<!-- sc:scenario SC-M01-037 -->

<a id="sc-m01-037"></a>

### SC-M01-037 — Xem trang chính sách công khai

#### 1. Tên kịch bản chuẩn

**Xem trang chính sách công khai** — BF-M01-037; UC owner: [UC-M01-013](../../us/US-M01.md#uc-m01-013); nhóm chi tiết: UC-M01-024. Trigger: Người xem mở trang hoặc liên kết Privacy Policy/ToS.

#### 2. Actor thực hiện

ACT-001 Guest trong ví dụ; ACT-002/ACT-003 cũng được đọc trang công khai theo cùng cách.

#### 3. Tiền điều kiện

Không cần đăng nhập hoặc đồng ý trước. Bản nội dung hiện hành minh họa P2.0 đã được đội phát triển triển khai; không có màn hình Admin chỉnh/phát hành. Câu chữ hoàn chỉnh và liên hệ còn theo TBD-M01-01.

#### 4. Hậu điều kiện

<!-- sc:post SC-M01-037 -->

| result | condition |
|---|---|
| SUCCESS | Trang hiện đúng phiên bản, đủ các nhóm/mục cần có. Việc đọc không tự tạo bản ghi đồng ý; nếu từ đăng ký, trở về đúng điểm đồng ý mà chưa tự gửi đăng ký. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M01-037 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-001 | Guest mở trang Privacy Policy/ToS công khai từ chân trang. | P2.0; consent chưa được ghi nhận bởi lần đọc này | M2 | FR-M01-15.01, FR-M01-01.04, BR-M01-03 |
| M2 | SYSTEM | Hệ thống hiển thị đúng phiên bản và đầy đủ các phần nội dung chính sách đã quy định. | Phiên bản minh họa P2.0; Chính sách quyền riêng tư có dữ liệu thu thập, mục đích, dịch vụ ngoài, thời gian lưu, quyền, dưới 16 tuổi, thay đổi, liên hệ; Điều khoản có quy tắc/nội dung cấm, kiểm duyệt/cảnh báo, khóa/khiếu nại, quyền với nội dung. Bốn nhóm: tài khoản/hồ sơ; nội dung tạo; an toàn cộng đồng; dữ liệu qua AI. Nêu AI xử lý cả bản soạn khi bấm Gợi ý topic, dịch vụ đăng nhập/lưu ảnh/email/AI, không bán dữ liệu, lưu bình luận/tin nhắn/nhật ký sau xóa, quyền sửa/xóa/bản sao, rút đồng ý qua vô hiệu hóa. Không nêu tên nhà cung cấp hay phiên đăng nhập; MS1 chưa có tải bản sao; câu chữ chính sách và email liên hệ còn chờ hoàn thiện. | END:SUCCESS | FR-M01-15.01, FR-M01-15.02, FR-M01-15.03, FR-M01-15.04, FR-M01-15.05, FR-M01-15.06, FR-M01-15.07, FR-M01-15.08, FR-M01-15.09, BR-M01-42, BR-M01-43, BR-M01-44, BR-M01-45, BR-M01-46 |


#### 6. Các ngoại lệ

<!-- sc:exceptions SC-M01-037 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Actor mở chính sách từ điểm đồng ý đăng ký rồi trở về đúng điểm đó | E1.1 | FR-M01-15.01, FR-M01-01.04, BR-M01-03, FR-M01-15.02, FR-M01-15.03, FR-M01-15.04, FR-M01-15.05, FR-M01-15.06, FR-M01-15.07, FR-M01-15.08, FR-M01-15.09, BR-M01-42, BR-M01-43, BR-M01-44, BR-M01-45, BR-M01-46, FR-M01-01.05, FR-M01-01.13, FR-M01-01.14 |


**E1: Actor mở chính sách từ điểm đồng ý đăng ký rồi trở về đúng điểm đó.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-037 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-001 | Guest mở liên kết Privacy Policy/ToS ở điểm đồng ý đăng ký. | P2.0; consent chưa được ghi nhận bởi lần đọc này | E1.2 | FR-M01-15.01, FR-M01-01.04, BR-M01-03 |
| E1.2 | SYSTEM | Hệ thống hiển thị đúng phiên bản và đầy đủ các phần nội dung chính sách đã quy định. | Phiên bản minh họa P2.0; Chính sách quyền riêng tư có dữ liệu thu thập, mục đích, dịch vụ ngoài, thời gian lưu, quyền, dưới 16 tuổi, thay đổi, liên hệ; Điều khoản có quy tắc/nội dung cấm, kiểm duyệt/cảnh báo, khóa/khiếu nại, quyền với nội dung. Bốn nhóm: tài khoản/hồ sơ; nội dung tạo; an toàn cộng đồng; dữ liệu qua AI. Nêu AI xử lý cả bản soạn khi bấm Gợi ý topic, dịch vụ đăng nhập/lưu ảnh/email/AI, không bán dữ liệu, lưu bình luận/tin nhắn/nhật ký sau xóa, quyền sửa/xóa/bản sao, rút đồng ý qua vô hiệu hóa. Không nêu tên nhà cung cấp hay phiên đăng nhập; MS1 chưa có tải bản sao; câu chữ chính sách và email liên hệ còn chờ hoàn thiện. | E1.3 | FR-M01-15.01, FR-M01-15.02, FR-M01-15.03, FR-M01-15.04, FR-M01-15.05, FR-M01-15.06, FR-M01-15.07, FR-M01-15.08, FR-M01-15.09, BR-M01-42, BR-M01-43, BR-M01-44, BR-M01-45, BR-M01-46 |
| E1.3 | ACT-001 | Guest quay lại ngữ cảnh đăng ký sau khi đọc; chưa gửi quyết định đồng ý. | Điểm EP-REG-POLICY của UC-M01-020 | E1.4 | FR-M01-01.04, BR-M01-03 |
| E1.4 | SYSTEM | Hệ thống tiếp tục ngữ cảnh đăng ký tại điểm đồng ý; việc đọc trang không tự đánh dấu hoặc lưu sự đồng ý. | Trạng thái consent vẫn theo hành động rõ ràng của người đăng ký; chưa tạo tài khoản vì chỉ đọc | END:SUCCESS | FR-M01-01.05, FR-M01-01.13, FR-M01-01.14, BR-M01-03 |


**Ghi chú đường đi và giới hạn:** Luồng chính hoàn tất mục tiêu; các trường hợp trong mục 6 là đường thay thế, không chạy nối tiếp tất cả nhánh. Guard mô tả dữ liệu/ngữ cảnh thay thế của chính lần thực thi. Nhánh sửa gửi lại áp cùng điều kiện kiểm tra; không có giới hạn thử mới ngoài nguồn. Các GAP ở mục cuối vẫn áp dụng.

<!-- sc:end SC-M01-037 -->

<!-- sc:scenario SC-M01-039 -->

<a id="sc-m01-039"></a>

### SC-M01-039 — Đồng ý phiên bản chính sách mới

#### 1. Tên kịch bản chuẩn

**Đồng ý phiên bản chính sách mới** — BF-M01-039; UC owner: [UC-M01-014](../../us/US-M01.md#uc-m01-014); nhóm chi tiết: UC-M01-024. Trigger: Người có phiên mở ứng dụng; hệ thống so phiên bản chính sách.

#### 2. Actor thực hiện

ACT-002 chủ tài khoản; ACT-003 cũng phải đồng ý lại cho tài khoản của chính mình khi chính sách đổi.

#### 3. Tiền điều kiện

Có phiên P01; không đặt đã đồng ý P2.0 làm tiền điều kiện. Đường chuẩn A01 ACTIVE; trạng thái/quyền vẫn áp dụng sau mọi quyết định; bảo trì tắt.

#### 4. Hậu điều kiện

<!-- sc:post SC-M01-039 -->

| result | condition |
|---|---|
| SUCCESS | Nếu đồng ý P2.0: lưu phiên bản/thời điểm và cho dùng tiếp trong quyền hiện có. Nếu bản hiện hành đã đồng ý: không hỏi/ghi lại. Nếu từ chối rồi chọn vô hiệu hóa hợp lệ: chuyển DEACTIVATED, kết thúc mọi phiên, không ghi đồng ý P2.0; đây là kết quả rút đồng ý của nhánh, không phải đồng ý thành công. |
| CANCELLED | P01 đăng xuất, lịch sử trình duyệt rỗng, L01 không bị kết thúc bởi logout P01; chưa đồng ý P2.0 và lần mở ứng dụng sau vẫn hỏi lại. |
| REJECTED | Chưa đồng ý P2.0; không được dùng tiếp. Yêu cầu vô hiệu hóa không đủ điều kiện bị từ chối, trạng thái/phiên không đổi bởi thao tác bị từ chối; đường Đăng xuất hợp lệ vẫn có ở scenario từ chối–đăng xuất. |


#### 5. Các sự kiện chính

<!-- sc:main SC-M01-039 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| M1 | ACT-002 | Chủ tài khoản mở ứng dụng trên P01. | A01 ACTIVE; đã đồng ý P1.0, hiện P2.0 | M2 | FR-M01-16.01 |
| M2 | SYSTEM | Hệ thống yêu cầu đồng ý P2.0 trước khi dùng tiếp, kể cả phiên P01 đang còn; cung cấp nội dung chính sách hiện hành. | Phiên bản minh họa P2.0; Chính sách quyền riêng tư có dữ liệu thu thập, mục đích, dịch vụ ngoài, thời gian lưu, quyền, dưới 16 tuổi, thay đổi, liên hệ; Điều khoản có quy tắc/nội dung cấm, kiểm duyệt/cảnh báo, khóa/khiếu nại, quyền với nội dung. Bốn nhóm: tài khoản/hồ sơ; nội dung tạo; an toàn cộng đồng; dữ liệu qua AI. Nêu AI xử lý cả bản soạn khi bấm Gợi ý topic, dịch vụ đăng nhập/lưu ảnh/email/AI, không bán dữ liệu, lưu bình luận/tin nhắn/nhật ký sau xóa, quyền sửa/xóa/bản sao, rút đồng ý qua vô hiệu hóa. Không nêu tên nhà cung cấp hay phiên đăng nhập; MS1 chưa có tải bản sao; câu chữ chính sách và email liên hệ còn chờ hoàn thiện.; bản đã đồng ý P1.0; chưa cho dùng tiếp vì có phiên sẵn | M3 | FR-M01-16.01, BR-M01-44 |
| M3 | ACT-002 | Chủ tài khoản chọn đồng ý P2.0. | consent=true lúc 06/11/2026 09:10 +07 | M4 | FR-M01-16.02 |
| M4 | SYSTEM | Hệ thống lưu thời điểm và phiên bản P2.0 đã đồng ý; cho tiếp tục trong quyền hiện có. | Bản ghi đồng ý A01/P2.0/09:10; không đổi trạng thái/quyền tài khoản | END:SUCCESS | FR-M01-16.02, BR-M01-44 |


#### 6. Các ngoại lệ

<!-- sc:exceptions SC-M01-039 -->

| id | kind | at | condition | entry | sources |
|---|---|---|---|---|---|
| E1 | user-choice | M1 | Từ chối chính sách mới rồi đăng xuất | E1.1 | FR-M01-16.01, BR-M01-44, FR-M01-16.03, BR-M01-45, FR-M01-07.01, FR-M01-07.02, FR-M01-16.04, FR-M06-05.10 |
| E2 | user-choice | M1 | Từ chối chính sách mới rồi vô hiệu hóa | E2.1 | FR-M01-16.01, BR-M01-44, FR-M01-16.03, BR-M01-45, FR-M01-10.01, FR-M01-10.02, FR-M01-10.07, FR-M01-13.01, FR-M01-13.03, BR-M01-21 |
| E3 | user-choice | M1 | Từ chối chính sách mới rồi vô hiệu hóa; Tài khoản không còn ACTIVE hoặc người yêu cầu không đủ điều kiện vô hiệu hóa | E3.1 | FR-M01-16.01, BR-M01-44, FR-M01-16.03, BR-M01-45, FR-M01-10.04, FR-M01-10.05, FR-M01-10.06 |
| E4 | user-choice | M1 | Mở ứng dụng khi đã đồng ý phiên bản hiện hành | E4.1 | FR-M01-16.01, FR-M01-16.05, BR-M01-44 |


**E1: Từ chối chính sách mới rồi đăng xuất.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-039 E1 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E1.1 | ACT-002 | Chủ tài khoản mở ứng dụng trên P01. | A01 ACTIVE; đã đồng ý P1.0, hiện P2.0 | E1.2 | FR-M01-16.01 |
| E1.2 | SYSTEM | Hệ thống yêu cầu đồng ý P2.0 trước khi dùng tiếp, kể cả phiên P01 đang còn; cung cấp nội dung chính sách hiện hành. | Phiên bản minh họa P2.0; Chính sách quyền riêng tư có dữ liệu thu thập, mục đích, dịch vụ ngoài, thời gian lưu, quyền, dưới 16 tuổi, thay đổi, liên hệ; Điều khoản có quy tắc/nội dung cấm, kiểm duyệt/cảnh báo, khóa/khiếu nại, quyền với nội dung. Bốn nhóm: tài khoản/hồ sơ; nội dung tạo; an toàn cộng đồng; dữ liệu qua AI. Nêu AI xử lý cả bản soạn khi bấm Gợi ý topic, dịch vụ đăng nhập/lưu ảnh/email/AI, không bán dữ liệu, lưu bình luận/tin nhắn/nhật ký sau xóa, quyền sửa/xóa/bản sao, rút đồng ý qua vô hiệu hóa. Không nêu tên nhà cung cấp hay phiên đăng nhập; MS1 chưa có tải bản sao; câu chữ chính sách và email liên hệ còn chờ hoàn thiện.; bản đã đồng ý P1.0; chưa cho dùng tiếp vì có phiên sẵn | E1.3 | FR-M01-16.01, BR-M01-44 |
| E1.3 | ACT-002 | Chủ tài khoản chọn không đồng ý P2.0. | consent=false; bản đã đồng ý vẫn P1.0 | E1.4 | FR-M01-16.03 |
| E1.4 | SYSTEM | Hệ thống chỉ cung cấp hai đường thoát Đăng xuất hoặc Vô hiệu hóa; không cho dùng chức năng khác khi chưa đồng ý. | Không lưu đồng ý P2.0; lựa chọn vô hiệu hóa vẫn phải đáp ứng ACTIVE/chủ tài khoản | E1.5 | FR-M01-16.03, BR-M01-45 |
| E1.5 | ACT-002 | Chủ tài khoản chọn Đăng xuất. | P01; L01 là thiết bị khác; lịch sử P01 có đạo hàm | E1.6 | FR-M01-16.03 |
| E1.6 | SYSTEM | Hệ thống triển khai UC-M01-006: kết thúc phiên P01, giữ các phiên khác, xóa lịch sử tìm kiếm trình duyệt P01; không ghi đồng ý P2.0. | P01 không còn phiên, lịch sử rỗng; A01 vẫn ACTIVE; lần mở sau nếu chưa đồng ý phải hỏi lại | END:CANCELLED | FR-M01-07.01, FR-M01-07.02, FR-M01-16.03, FR-M01-16.04, FR-M06-05.10, BR-M01-45 |


**E2: Từ chối chính sách mới rồi vô hiệu hóa.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-039 E2 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E2.1 | ACT-002 | Chủ tài khoản mở ứng dụng trên P01. | A01 ACTIVE; đã đồng ý P1.0, hiện P2.0 | E2.2 | FR-M01-16.01 |
| E2.2 | SYSTEM | Hệ thống yêu cầu đồng ý P2.0 trước khi dùng tiếp, kể cả phiên P01 đang còn; cung cấp nội dung chính sách hiện hành. | Phiên bản minh họa P2.0; Chính sách quyền riêng tư có dữ liệu thu thập, mục đích, dịch vụ ngoài, thời gian lưu, quyền, dưới 16 tuổi, thay đổi, liên hệ; Điều khoản có quy tắc/nội dung cấm, kiểm duyệt/cảnh báo, khóa/khiếu nại, quyền với nội dung. Bốn nhóm: tài khoản/hồ sơ; nội dung tạo; an toàn cộng đồng; dữ liệu qua AI. Nêu AI xử lý cả bản soạn khi bấm Gợi ý topic, dịch vụ đăng nhập/lưu ảnh/email/AI, không bán dữ liệu, lưu bình luận/tin nhắn/nhật ký sau xóa, quyền sửa/xóa/bản sao, rút đồng ý qua vô hiệu hóa. Không nêu tên nhà cung cấp hay phiên đăng nhập; MS1 chưa có tải bản sao; câu chữ chính sách và email liên hệ còn chờ hoàn thiện.; bản đã đồng ý P1.0; chưa cho dùng tiếp vì có phiên sẵn | E2.3 | FR-M01-16.01, BR-M01-44 |
| E2.3 | ACT-002 | Chủ tài khoản chọn không đồng ý P2.0. | consent=false; bản đã đồng ý vẫn P1.0 | E2.4 | FR-M01-16.03 |
| E2.4 | SYSTEM | Hệ thống chỉ cung cấp hai đường thoát Đăng xuất hoặc Vô hiệu hóa; không cho dùng chức năng khác khi chưa đồng ý. | Không lưu đồng ý P2.0; lựa chọn vô hiệu hóa vẫn phải đáp ứng ACTIVE/chủ tài khoản | E2.5 | FR-M01-16.03, BR-M01-45 |
| E2.5 | ACT-002 | Chủ tài khoản chọn Vô hiệu hóa tài khoản của mình. | A01 ACTIVE; chọn tại EP-POLICY-DECISION | E2.6 | FR-M01-16.03 |
| E2.6 | SYSTEM | Hệ thống triển khai UC-M01-009: kiểm ACTIVE/quyền chủ tài khoản, chuyển DEACTIVATED, kết thúc mọi phiên và áp cách hiển thị nội dung; tính cửa sổ 14×24 giờ. Không ghi đồng ý P2.0. | A01 DEACTIVATED lúc 06/11/2026 09:10, hạn 20/11/2026 09:10; bài ẩn, tên thay thế cho bình luận | END:SUCCESS | FR-M01-16.03, FR-M01-10.01, FR-M01-10.02, FR-M01-10.07, FR-M01-13.01, FR-M01-13.03, BR-M01-21, BR-M01-45 |


**E3: Từ chối chính sách mới rồi vô hiệu hóa; Tài khoản không còn ACTIVE hoặc người yêu cầu không đủ điều kiện vô hiệu hóa.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-039 E3 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E3.1 | ACT-002 | Chủ tài khoản mở ứng dụng trên P01. | A01 ACTIVE; đã đồng ý P1.0, hiện P2.0 | E3.2 | FR-M01-16.01 |
| E3.2 | SYSTEM | Hệ thống yêu cầu đồng ý P2.0 trước khi dùng tiếp, kể cả phiên P01 đang còn; cung cấp nội dung chính sách hiện hành. | Phiên bản minh họa P2.0; Chính sách quyền riêng tư có dữ liệu thu thập, mục đích, dịch vụ ngoài, thời gian lưu, quyền, dưới 16 tuổi, thay đổi, liên hệ; Điều khoản có quy tắc/nội dung cấm, kiểm duyệt/cảnh báo, khóa/khiếu nại, quyền với nội dung. Bốn nhóm: tài khoản/hồ sơ; nội dung tạo; an toàn cộng đồng; dữ liệu qua AI. Nêu AI xử lý cả bản soạn khi bấm Gợi ý topic, dịch vụ đăng nhập/lưu ảnh/email/AI, không bán dữ liệu, lưu bình luận/tin nhắn/nhật ký sau xóa, quyền sửa/xóa/bản sao, rút đồng ý qua vô hiệu hóa. Không nêu tên nhà cung cấp hay phiên đăng nhập; MS1 chưa có tải bản sao; câu chữ chính sách và email liên hệ còn chờ hoàn thiện.; bản đã đồng ý P1.0; chưa cho dùng tiếp vì có phiên sẵn | E3.3 | FR-M01-16.01, BR-M01-44 |
| E3.3 | ACT-002 | Chủ tài khoản chọn không đồng ý P2.0. | consent=false; bản đã đồng ý vẫn P1.0 | E3.4 | FR-M01-16.03 |
| E3.4 | SYSTEM | Hệ thống chỉ cung cấp hai đường thoát Đăng xuất hoặc Vô hiệu hóa; không cho dùng chức năng khác khi chưa đồng ý. | Không lưu đồng ý P2.0; lựa chọn vô hiệu hóa vẫn phải đáp ứng ACTIVE/chủ tài khoản | E3.5 | FR-M01-16.03, BR-M01-45 |
| E3.5 | ACT-002 | Chủ tài khoản chọn Vô hiệu hóa tài khoản của mình. | A01 ACTIVE; chọn tại EP-POLICY-DECISION | E3.6 | FR-M01-16.03 |
| E3.6 | SYSTEM | Hệ thống từ chối vô hiệu hóa; không miễn kiểm trạng thái/quyền chỉ vì từ chối chính sách. Người dùng vẫn chưa được vào dùng tiếp. | BANNED hoặc không có phiên/chủ tài khoản; không ghi đồng ý mới | END:REJECTED | FR-M01-10.04, FR-M01-10.05, FR-M01-10.06, FR-M01-16.03, BR-M01-45 |


**E4: Mở ứng dụng khi đã đồng ý phiên bản hiện hành.** Thay thế M1; không thực hiện xong bước đó rồi lặp thêm phản hồi hệ thống.

<!-- sc:branch SC-M01-039 E4 -->

| step | subject | action | data | next | sources |
|---|---|---|---|---|---|
| E4.1 | ACT-002 | Chủ tài khoản mở ứng dụng trên P01. | A01 ACTIVE; đã đồng ý P2.0, hiện P2.0 | E4.2 | FR-M01-16.01 |
| E4.2 | SYSTEM | Hệ thống so phiên bản, không hỏi lại sự đồng ý đã có và cho tiếp tục theo quyền/trạng thái hiện hành. | Bản ghi P2.0 đã có; không ghi bản đồng ý mới chỉ do mở ứng dụng | END:SUCCESS | FR-M01-16.05, BR-M01-44 |


**Ghi chú đường đi và giới hạn:** Luồng chính hoàn tất mục tiêu; các trường hợp trong mục 6 là đường thay thế, không chạy nối tiếp tất cả nhánh. Guard mô tả dữ liệu/ngữ cảnh thay thế của chính lần thực thi. Nhánh sửa gửi lại áp cùng điều kiện kiểm tra; không có giới hạn thử mới ngoài nguồn. Các GAP ở mục cuối vẫn áp dụng.

<!-- sc:end SC-M01-039 -->

## 5. Quy tắc nền và hiển thị (không phải scenario)

Các tác vụ dưới không mang BF/SC hoặc cấu trúc sáu phần. Email giao dịch xác minh/reset/OTP chưa được tự áp policy retry email sự kiện (GAP-008). Quy tắc hồ sơ/ban/hiển thị là hợp đồng liên module, không thêm chức năng M01.

| ID nguồn/quy tắc | Trigger/điều kiện | Hiệu ứng và các trường hợp | sources |
|---|---|---|---|
| AUT-M01-001 | Phiên truy cập P01 hết hạn và thiết bị dùng phiên làm mới; A01 có phiên P01 và L01 riêng. Đường chuẩn P01 truy cập hết hạn 06/11/2026 09:00, phiên làm mới R1 còn hạn/hiệu lực; tài khoản vẫn được phép thao tác theo trạng thái/bảo trì/chính sách. | Hệ thống kiểm phiên làm mới còn hiệu lực/hạn, cấp phiên truy cập P01 mới hạn 1 giờ, thay R1 bằng R2 hạn 30 ngày tính từ lúc cấp và làm R1 mất hiệu lực. Giữ phiên L01 độc lập. Dữ liệu: Cấp 06/11/2026 09:00 +07; truy cập mới đến 10:00; R2 đến 06/12/2026 09:00; R1 không dùng lại; L01 không đổi Trường hợp Phiên làm mới đã mất hiệu lực bị dùng lại: Hệ thống từ chối làm mới bằng R1; không tự cấp quyền hoặc đồng loạt đăng xuất thiết bị khác. Dữ liệu: R1 đã bị dùng và thay bởi R2 Trường hợp Phiên làm mới đã hết hạn 30 ngày: Hệ thống từ chối làm mới và yêu cầu đăng nhập lại; giữ các phiên thiết bị khác. Yêu cầu đăng nhập mới được xử lý trọn đường trong các scenario UC-M01-005/015. Dữ liệu: R1 đã quá hạn; P01 cần đăng nhập; L01 vẫn hợp lệ Trường hợp Bảo trì bật, chủ phiên không ADMIN: Hệ thống từ chối thao tác qua phiên đang có, không suy ra bảo trì tự xóa mọi phiên. Dữ liệu: maintenance=true; role=USER/MOD | FR-M01-06.01, FR-M01-06.02, FR-M01-06.05, FR-M01-06.06, FR-M01-06.07, BR-M01-16, BR-M01-17, FR-M01-06.03, FR-M01-06.04, FR-M01-05.20, BR-M01-37 |
| AUT-M01-002 | Đến đúng thời hạn vô hiệu hóa mà tài khoản chưa được kích hoạt lại; A01 DEACTIVATED từ 06/11/2026 09:00 +07; đến 20/11/2026 09:00 vẫn chưa kích hoạt lại. Dữ liệu minh họa có email an.study@example.test, username An_12A1, 12 bookmark, 30 lượt theo dõi người, 1 lượt theo dõi Topic, 50 người theo dõi, bản ghi đồng ý và dữ liệu cá nhân. | Hệ thống chuyển A01 sang DELETED, giữ bản ghi tài khoản/trạng thái/vai trò và khóa username vĩnh viễn. Xóa email/mật khẩu/liên kết Google/display_name/avatar/bio/Lớp-Khối/mọi phiên/bookmark/follow người và Topic hai chiều/bản ghi đồng ý; giải phóng email. Giữ bài vẫn ẩn, bình luận/tin nhắn với danh tính thay thế, upvote đã cho không gắn người cho, nhật ký kiểm duyệt/AI qua username và phản hồi Topic không gắn danh tính. Không cho DELETED chuyển trạng thái khác. Dữ liệu: A01 DELETED; 0 bookmark/follow của A01; quan hệ 50 người theo dõi A01 bị gỡ; số follow các đối tượng nhận giảm tương ứng; email đăng ký mới được, An_12A1 không tái dùng; tác giả bình luận/tin nhắn [Người dùng đã xóa] | FR-M01-12.01, FR-M01-12.02, FR-M01-12.03, FR-M01-12.04, FR-M01-12.06, FR-M01-12.07, FR-M01-12.08, FR-M01-12.09, FR-M01-12.10, FR-M01-12.11, FR-M01-13.01, FR-M01-13.04, FR-M01-13.06, BR-M01-21, BR-M01-24, BR-M01-47 |
| AUT-M01-003 | Còn đúng 24 giờ trước thời điểm DELETED; A01 còn DEACTIVATED; mốc vô hiệu hóa 06/11/2026 09:00, hạn xóa 20/11/2026 09:00; hiện 19/11/2026 09:00 +07. Chưa kích hoạt lại. | Hệ thống phát sự kiện cảnh báo và ghi một email cho chủ tài khoản vào hàng đợi M07; không tạo thông báo trong ứng dụng vì tài khoản không đăng nhập được. Dữ liệu: Một email tới email còn lưu của A01; hạn còn 24 giờ; không có thông báo in-app; gửi thực tế theo M07 | FR-M01-12.05, BR-M01-32, FR-M07-04.01, FR-M07-04.03, FR-M07-04.06, BR-M07-04, BR-M07-11 |
| AUT-M01-004 | Đến thời điểm hết hạn ban tạm thời của M08; A03 BANNED do ban tạm thời 30 ngày từ 07/10/2026 09:00, hiện 06/11/2026 09:00 +07. Không áp dụng cho ban vĩnh viễn. | Hệ thống chuyển trạng thái từ BANNED về ACTIVE ngay lúc ban tạm thời hết hạn; giữ mức xác minh để lần truy cập tiếp theo áp dụng đúng cổng. Dữ liệu: A03 ACTIVE tại 06/11/2026 09:00; mức xác minh trước/ sau không tự tăng; không tự khôi phục vai trò đã mất | FR-M01-05.17, BR-M01-34 |
| AUT-M01-005 | M03/M04 phát sự kiện nội dung chứa mention được công khai; Nội dung có tham chiếu tài khoản đã được chèn đúng. Đường chuẩn P201 vừa công khai với U201/U203; người U203 đã tắt thông báo của bài. Lần sửa minh họa giữ hai người cũ, thêm U204. | Hệ thống xác định những tài khoản được nhắc khi nội dung hiển thị công khai và ghi thông báo nhắc tên trong ứng dụng qua M07, kể cả người đã tắt thông báo bài; không gửi email nhắc tên. Dữ liệu: U201/U203 nhận thông báo ở lúc P201 công khai; bản soạn trước đó không phát thông báo; áp dụng cả bài viết và bình luận Trường hợp Nội dung đã công khai được sửa, giữ U201/U203 và thêm U204: Hệ thống chỉ ghi thông báo cho U204 mới được nhắc thêm; không gửi lại cho U201/U203 do họ vẫn còn trong nội dung. Dữ liệu: Tập cũ={U201,U203}; tập mới={U201,U203,U204}; người nhận mới={U204} | FR-M01-14.10, BR-M01-30, BR-M07-03, BR-M07-06, FR-M01-14.17 |
| RULE-M01-001 | Nội dung hợp lệ được đọc, tác giả DEACTIVATED hoặc DELETED; Người xem được module sở hữu cho đọc nội dung; đường chuẩn tác giả A01 DEACTIVATED. Trường hợp đặc quyền xem bài ẩn/danh tính thật đã có tại UC-M01-011. | Người xem mở ngữ cảnh chứa bình luận C101 và tin nhắn T101 được phép đọc; hoặc truy cập địa chỉ bài P101 bị ẩn. Dữ liệu: C101="Dùng Vi-ét"; T101="Chào bạn"; A01 DEACTIVATED Hệ thống ẩn bài P101, địa chỉ bài hiện Nội dung không tồn tại; bình luận giữ nội dung gốc với tên Tài khoản tạm thời vô hiệu hoá và avatar mặc định; cung cấp đúng tên/avatar thay thế cho M16 hiển thị tin nhắn. Dữ liệu: C101/T101 giữ nội dung; tên thay thế, avatar mặc định; không mở lại bài ẩn cho người thường Trường hợp Tác giả DELETED thay vì DEACTIVATED: Hệ thống tiếp tục ẩn bài; giữ nội dung bình luận/tin nhắn nhưng dùng tên [Người dùng đã xóa] và avatar mặc định; không phục hồi dữ liệu cá nhân đã xóa. Dữ liệu: C101/T101 không mất nội dung; tên [Người dùng đã xóa]; P101 vẫn ẩn | FR-M01-13.01, FR-M01-13.02, FR-M01-13.03, FR-M01-13.07, BR-M01-23, FR-M01-13.04, FR-M01-13.06, BR-M01-24, BR-M01-47 |
| RULE-M01-002 | M02 nhận yêu cầu đổi username/display_name của chính chủ; A01 ACTIVE, có phiên và quyền sửa hồ sơ của mình theo M02. Username cũ An_12A1, mới An_Toan còn khả dụng; display_name mới "  An Minh  ". Quy tắc không giới hạn số lần đổi. | Chủ tài khoản gửi thay đổi định danh tại trang sửa hồ sơ M02. Dữ liệu: An_12A1 → An_Toan; display_name nhập "  An Minh  " Hệ thống kiểm username 3–20 ký tự đúng tập/duy nhất không phân biệt hoa thường kể cả username DELETED; trim và kiểm display_name 1–50 ký tự đúng tập. Lưu An_Toan đúng hoa/thường và An Minh; giải phóng An_12A1 ngay; dùng display_name làm tên chính. Dữ liệu: Username cũ khả dụng cho tài khoản khác; username An_Toan không trùng; người khác có display_name An Minh vẫn hợp lệ Trường hợp Username/display_name mới vi phạm quy tắc định danh: Hệ thống từ chối giá trị định danh không hợp lệ; không nhận tên sai hoặc giải phóng username cũ bởi một lần đổi username bị từ chối. Dữ liệu: username=Cuong trùng DELETED cuong; hoặc display_name="An 😊" Trường hợp Chủ tài khoản không ACTIVE hoặc yêu cầu sửa không phải của mình: Hệ thống từ chối sửa theo quyền M02 và ràng buộc trạng thái. Dữ liệu: A01 BANNED/DEACTIVATED hoặc actor A02 sửa A01 | FR-M01-03.15, FR-M01-03.16, BR-M01-36, FR-M01-03.05, FR-M01-03.06, FR-M01-03.07, FR-M01-03.10, FR-M01-03.11, FR-M01-03.12, FR-M01-03.13, FR-M01-03.14, BR-M01-05, BR-M01-06, BR-M01-07, FR-M02-03.09, FR-M02-03.10 |
| RULE-M01-004 | M08 hoặc M09 đã có quyết định nghiệp vụ có hiệu lực; Quyền ra quyết định/xét duyệt được module sở hữu kiểm. Đường chuẩn M08 phát sự kiện ban tài khoản A01 ACTIVE; M01 chỉ áp trạng thái. | Hệ thống chuyển A01 từ ACTIVE sang BANNED khi quyết định ban có hiệu lực; áp các hạn chế theo trạng thái. Dữ liệu: A01 ACTIVE → BANNED; lý do/thời hạn từ M08, không do M01 tự tính một mức ban mới Trường hợp M08 gỡ ban của tài khoản đang BANNED: Hệ thống chuyển BANNED sang ACTIVE ngay khi quyết định gỡ ban có hiệu lực. Dữ liệu: A01 ACTIVE; mức xác minh và vai trò theo dữ liệu module sở hữu Trường hợp M09 chấp nhận khiếu nại về ban đang hiệu lực: Hệ thống chuyển tài khoản từ BANNED sang ACTIVE ngay khi khiếu nại ban được chấp nhận; không coi đó là phục hồi tự động vai trò Mod. Dữ liệu: A01 ACTIVE; vai trò của người từng là Mod giữ USER theo M09 | FR-M01-05.14, BR-M01-34, FR-M01-05.15, FR-M01-05.16, FR-M09-08.01, FR-M09-08.11 |
| RULE-M01-005 | Người đang có phiên yêu cầu một thao tác khi công tắc bảo trì bật; A01 USER hoặc MOD đã đăng nhập trước bảo trì, hiện maintenance=true. Tác vụ cụ thể có điều kiện/quyền ở module sở hữu. | Người dùng gửi thao tác qua phiên P01 đang có. Dữ liệu: P01 được tạo trước bảo trì; role=USER Hệ thống từ chối thao tác trong bảo trì vì người dùng không có vai trò ADMIN; không suy ra tự xóa toàn bộ phiên. Dữ liệu: P01 không dùng thao tác trong bảo trì; không cấp quyền ADMIN; không khẳng định phiên bị thu hồi | FR-M01-05.20, BR-M01-37 |
| EMAIL-M01-001 | Lần quét hàng đợi email kế tiếp sau sự kiện mật khẩu/liên kết/cảnh báo; Sự kiện thuộc nhóm có email của M07 đã tạo một email Q1; thao tác M01 gây sự kiện đã hoàn tất độc lập. Lần quét minh họa 09:01, Q1 được tạo 09:00:20. | Hệ thống lấy Q1 trong lần quét mỗi một phút và gửi yêu cầu giao email tới dịch vụ ngoài. Dữ liệu: Q1; đúng người nhận/kênh của sự kiện; không đợi email để hoàn tất đổi mật khẩu/liên kết Dịch vụ email thực hiện giao theo yêu cầu của hệ thống. Dữ liệu: Q1; trường hợp chuẩn gửi thành công theo hợp đồng gửi email; không đồng nghĩa người nhận đã đọc Trường hợp Gửi đầu thất bại; cả ba lần gửi lại đều thất bại: Dịch vụ email không gửi thành công Q1 ở lần gửi đầu. Dữ liệu: Quét lần đầu 09:01; Q1 chưa được gửi Hệ thống giữ Q1 và yêu cầu gửi lại lần 1 ở lần quét kế tiếp. Dữ liệu: Q1; lần gửi lại 1; lúc 09:02 Dịch vụ email không gửi thành công Q1 ở lần gửi lại 1. Dữ liệu: Q1 chưa gửi; số lần gửi lại thất bại=1 Hệ thống giữ Q1 và yêu cầu gửi lại lần 2 ở lần quét kế tiếp. Dữ liệu: Q1; lần gửi lại 2; lúc 09:03 Dịch vụ email không gửi thành công Q1 ở lần gửi lại 2. Dữ liệu: Q1 chưa gửi; số lần gửi lại thất bại=2 Hệ thống giữ Q1 và yêu cầu gửi lại lần 3 ở lần quét kế tiếp. Dữ liệu: Q1; lần gửi lại 3; lúc 09:04 Dịch vụ email không gửi thành công Q1 ở lần gửi lại 3. Dữ liệu: Q1 chưa gửi; số lần gửi lại thất bại=3 Hệ thống dừng gửi Q1 sau ba lần gửi lại thất bại; không yêu cầu gửi tiếp ở lần quét sau, không hoàn tác thao tác M01 đã hoàn tất. Dữ liệu: Thất bại gửi lại 09:02/09:03/09:04; không gửi 09:05 Trường hợp Gửi đầu thất bại; lần gửi lại 1 là lần đầu thành công: Dịch vụ email không gửi thành công Q1 ở lần gửi đầu. Dữ liệu: Quét lần đầu 09:01; Q1 chưa được gửi Hệ thống giữ Q1 và yêu cầu gửi lại lần 1 ở lần quét kế tiếp. Dữ liệu: Q1; lần gửi lại 1; lúc 09:02 Dịch vụ email gửi Q1 thành công ở lần gửi lại 1. Dữ liệu: Q1 đã được gửi lúc 09:02; không tự coi đã đọc Trường hợp Gửi đầu thất bại; lần gửi lại 2 là lần đầu thành công: Dịch vụ email không gửi thành công Q1 ở lần gửi đầu. Dữ liệu: Quét lần đầu 09:01; Q1 chưa được gửi Hệ thống giữ Q1 và yêu cầu gửi lại lần 1 ở lần quét kế tiếp. Dữ liệu: Q1; lần gửi lại 1; lúc 09:02 Dịch vụ email không gửi thành công Q1 ở lần gửi lại 1. Dữ liệu: Q1 chưa gửi; số lần gửi lại thất bại=1 Hệ thống giữ Q1 và yêu cầu gửi lại lần 2 ở lần quét kế tiếp. Dữ liệu: Q1; lần gửi lại 2; lúc 09:03 Dịch vụ email gửi Q1 thành công ở lần gửi lại 2. Dữ liệu: Q1 đã được gửi lúc 09:03; không tự coi đã đọc Trường hợp Gửi đầu thất bại; lần gửi lại 3 là lần đầu thành công: Dịch vụ email không gửi thành công Q1 ở lần gửi đầu. Dữ liệu: Quét lần đầu 09:01; Q1 chưa được gửi Hệ thống giữ Q1 và yêu cầu gửi lại lần 1 ở lần quét kế tiếp. Dữ liệu: Q1; lần gửi lại 1; lúc 09:02 Dịch vụ email không gửi thành công Q1 ở lần gửi lại 1. Dữ liệu: Q1 chưa gửi; số lần gửi lại thất bại=1 Hệ thống giữ Q1 và yêu cầu gửi lại lần 2 ở lần quét kế tiếp. Dữ liệu: Q1; lần gửi lại 2; lúc 09:03 Dịch vụ email không gửi thành công Q1 ở lần gửi lại 2. Dữ liệu: Q1 chưa gửi; số lần gửi lại thất bại=2 Hệ thống giữ Q1 và yêu cầu gửi lại lần 3 ở lần quét kế tiếp. Dữ liệu: Q1; lần gửi lại 3; lúc 09:04 Dịch vụ email gửi Q1 thành công ở lần gửi lại 3. Dữ liệu: Q1 đã được gửi lúc 09:04; không tự coi đã đọc | FR-M07-04.01, FR-M07-04.02, FR-M07-04.03, BR-M07-03, BR-M07-11, FR-M07-04.09, BR-M07-26, FR-M07-04.10 |
| RULE-MENTION-035 | Người xem mở nội dung có khối nhắc đã lưu; Nội dung P201 được phép xem theo module sở hữu; đang có lượt nhắc gắn U203, không lưu danh tính chỉ bằng nhãn. Snapshot chuẩn U203 ACTIVE, display_name đổi từ Lan Chi thành Chi Lan. | Người xem mở P201 có lượt nhắc U203 đã được tạo trước đây. Dữ liệu: Khối lưu tài khoản U203; nhãn cũ Lan Chi Hệ thống hiển thị khối theo display_name hiện tại Chi Lan, làm nổi bật và không có @; không giữ nhãn cũ hoặc cho sửa nhãn thủ công. Dữ liệu: U203 hiện tại ACTIVE, display_name=Chi Lan; khối vẫn U203 Trường hợp Người được nhắc hiện DEACTIVATED: Hệ thống hiển thị tên thay thế Tài khoản tạm thời vô hiệu hoá cho khối, không dùng tên thật để vượt quy tắc hiển thị. Dữ liệu: U203 DEACTIVATED; tên thay thế; không mở hồ sơ khi bấm Trường hợp Người được nhắc hiện DELETED: Hệ thống hiển thị tên thay thế [Người dùng đã xóa] cho khối; không khôi phục danh tính cá nhân. Dữ liệu: U203 DELETED; tên thay thế; không mở hồ sơ khi bấm | FR-M01-14.07, FR-M01-14.08, BR-M01-28, BR-M01-29, FR-M01-14.15, FR-M01-14.16, BR-M01-40 |
| RULE-MENTION-036 | Người xem bấm khối nhắc tên thay thế; P201 được phép xem; khối U203 đã hiển thị tên thay thế vì U203 DEACTIVATED hoặc DELETED. Không áp quy tắc này cho BANNED nếu nguồn không nói. | Người xem bấm lượt nhắc U203 đang hiện tên thay thế. Dữ liệu: Tên="Tài khoản tạm thời vô hiệu hoá" hoặc "[Người dùng đã xóa]" Hệ thống không mở trang hồ sơ của tài khoản đó; giữ việc hiển thị khối theo tên thay thế. Dữ liệu: Không có truy cập hồ sơ qua lượt nhắc; không làm lộ danh tính đã ẩn/xóa | FR-M01-14.16, FR-M01-14.15, BR-M01-40 |


## 6. Đối chiếu ID bản cũ → bản sửa

| ID cũ | Mục tiêu hoặc đoạn cũ | Vị trí mới / cách xử lý |
|---|---|---|
| SC-M01-001 | Đăng ký email và hoàn tất cả ba bước | SC-M01-001/M1–M8 |
| SC-M01-002 | Xác minh email bằng magic link | SC-M01-001/E38 |
| SC-M01-003 | Gửi lại link xác minh email | SC-M01-001/E43 |
| SC-M01-004 | Hoàn tất thiết lập và bỏ qua thông tin tùy chọn | SC-M01-001 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |
| SC-M01-005 | Hoàn tất thiết lập có thông tin tùy chọn | SC-M01-001/E27 |
| SC-M01-006 | Đăng ký tài khoản Google và hoàn tất thiết lập | SC-M01-001/E16 |
| SC-M01-007 | Đăng nhập email vào ứng dụng khi đã hoàn tất thiết lập | SC-M01-007/M1–M2 |
| SC-M01-008 | Đăng nhập email để tiếp tục bước xác minh | SC-M01-007/E6 |
| SC-M01-009 | Đăng nhập email để tiếp tục thiết lập | SC-M01-007/E20 |
| SC-M01-010 | Đăng nhập email tài khoản bị khóa còn hạn khiếu nại | SC-M01-007/E32 |
| SC-M01-011 | Đăng nhập email tài khoản bị khóa đã hết hạn khiếu nại | SC-M01-007/E38 |
| SC-M01-012 | ADMIN đăng nhập email khi hệ thống bảo trì | SC-M01-007/E44 |
| SC-M01-013 | Đăng nhập tài khoản bị khóa và mở đường khiếu nại | SC-M01-007/E50 |
| SC-M01-014 | Đăng xuất chủ động trên thiết bị hiện tại | SC-M01-014/M1–M2 |
| SC-M01-015 | Đăng xuất bằng OK trên màn hình tài khoản bị khóa | SC-M01-014/E1 |
| SC-M01-016 | Đăng xuất sau khi từ chối chính sách mới | SC-M01-014/E2 |
| SC-M01-017 | Đổi mật khẩu khi đã đăng nhập | SC-M01-017/M1–M2 |
| SC-M01-018 | Lấy lại mật khẩu tài khoản email ACTIVE | SC-M01-018/M1–M4 |
| SC-M01-019 | Lấy lại mật khẩu tài khoản bị khóa và vào màn hình hạn chế | SC-M01-018/E10 |
| SC-M01-020 | Đặt mật khẩu qua link cho tài khoản ACTIVE | SC-M01-018 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |
| SC-M01-021 | Đặt mật khẩu qua link cho tài khoản BANNED | SC-M01-018 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |
| SC-M01-022 | Vô hiệu hóa tài khoản của chính mình | SC-M01-022/M1–M2 |
| SC-M01-023 | Kích hoạt lại tài khoản bằng mã email | SC-M01-023/M1–M4 |
| SC-M01-024 | Gửi lại mã và hoàn tất kích hoạt lại | SC-M01-023/E6 |
| SC-M01-025 | Mod/Admin xem bài ẩn và danh tính tác giả DEACTIVATED | SC-M01-025/M1–M2 |
| SC-M01-026 | Người dùng thường không được xem bài ẩn hoặc danh tính thật | SC-M01-025/E2 |
| SC-M01-027 | Chèn lượt nhắc tên khi soạn bài viết trong Group G12 | SC-M01-034/E2 |
| SC-M01-028 | Chèn lượt nhắc tên khi soạn bài viết ngoài Group | SC-M01-034/E5 |
| SC-M01-029 | Chèn lượt nhắc tên khi soạn bình luận trên bài trong Group G12 | SC-M01-034/E8 |
| SC-M01-030 | Chèn lượt nhắc tên khi soạn bình luận trên bài ngoài Group | SC-M01-034/E11 |
| SC-M01-031 | Guest yêu cầu gợi ý nhắc tên | SC-M01-034 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |
| SC-M01-032 | Xóa trọn khối nhắc tên bằng xóa lùi | SC-M01-034/E14 |
| SC-M01-033 | Từ chối sửa từng ký tự của nhãn nhắc tên | SC-M01-034/E15 |
| SC-M01-034 | Nhắc một tài khoản trong nội dung đang soạn | SC-M01-034/M1–M4 |
| SC-M01-035 | Hiển thị lượt nhắc cũ theo danh tính hiện hành | RULE-MENTION-035 (quy tắc hiển thị) |
| SC-M01-036 | Bấm lượt nhắc của tài khoản đã vô hiệu hóa hoặc đã xóa | RULE-MENTION-036 (quy tắc hiển thị) |
| SC-M01-037 | Xem trang chính sách công khai | SC-M01-037/M1–M2 |
| SC-M01-038 | Đọc chính sách từ luồng đăng ký rồi trở lại điểm đồng ý | SC-M01-037/E1 |
| SC-M01-039 | Đồng ý phiên bản chính sách mới | SC-M01-039/M1–M4; SC-M01-007/E107 |
| SC-M01-040 | Từ chối chính sách mới rồi đăng xuất | SC-M01-039/E1; SC-M01-007/E108 |
| SC-M01-041 | Từ chối chính sách mới rồi vô hiệu hóa | SC-M01-039/E2; SC-M01-007/E109 |
| SC-M01-042 | Mở ứng dụng khi đã đồng ý phiên bản hiện hành | SC-M01-039/E4 |
| SC-M01-043 | Đăng nhập tài khoản Google đã hoàn tất thiết lập | SC-M01-007/E52 |
| SC-M01-044 | Đăng nhập Google để tiếp tục thiết lập tài khoản đã tạo | SC-M01-007/E57 |
| SC-M01-045 | Đăng nhập Google và liên kết tài khoản email chưa xác minh | SC-M01-007/E68 |
| SC-M01-046 | Đăng nhập Google và liên kết tài khoản email đã xác minh, chưa thiết lập | SC-M01-007/E79 |
| SC-M01-047 | Đăng nhập Google và liên kết tài khoản email đã thiết lập | SC-M01-007/E90 |
| SC-M01-048 | Đăng nhập Google tài khoản bị khóa còn hạn khiếu nại | SC-M01-007/E95 |
| SC-M01-049 | ADMIN đăng nhập Google trong bảo trì | SC-M01-007/E101 |
| SC-M01-050 | Tự liên kết Google vào tài khoản email chưa xác minh | SC-M01-007 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |
| SC-M01-051 | Tự liên kết Google vào tài khoản email đã xác minh | SC-M01-007 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |
| SC-M01-052 | Áp dụng cổng cho ACTIVE đã hoàn tất | SC-M01-007 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |
| SC-M01-053 | Áp dụng cổng cho ACTIVE chưa xác minh | SC-M01-007 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |
| SC-M01-054 | Áp dụng cổng cho ACTIVE chưa thiết lập | SC-M01-007 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |
| SC-M01-055 | Áp dụng cổng cho BANNED còn hạn khiếu nại | SC-M01-007 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |
| SC-M01-056 | Áp dụng cổng cho BANNED hết hạn khiếu nại | SC-M01-007 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |
| SC-M01-057 | Cổng từ chối DEACTIVATED | SC-M01-007 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |
| SC-M01-058 | Cổng từ chối DELETED | SC-M01-007 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |
| SC-M01-059 | Cổng từ chối người không ADMIN trong bảo trì | SC-M01-007 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |
| SC-M01-060 | Cổng cho ADMIN đủ điều kiện trong bảo trì | SC-M01-007 — bước/nhánh hoặc quy tắc liên quan, xem truy vết nguồn |


## 7. Truy vết FR/BR và giới hạn

| Mã nguồn | SC/bước/nhánh hoặc quy tắc nền | Đối soát |
|---|---|---|
| FR-M01-01 | SC-M01-001/M1; SC-M01-001/M3; SC-M01-001/M4; SC-M01-001/E7.3; SC-M01-001/E27.1; SC-M01-001/E27.3; SC-M01-001/E27.4; SC-M01-001/E28.1; SC-M01-001/E28.3; SC-M01-001/E28.4; SC-M01-001/E29.1; SC-M01-001/E29.3; SC-M01-001/E29.4; SC-M01-001/E30.1; SC-M01-001/E30.3; SC-M01-001/E30.4; SC-M01-001/E31.1; SC-M01-001/E31.3; SC-M01-001/E31.4; SC-M01-001/E32.1; SC-M01-001/E32.3; SC-M01-001/E32.4; SC-M01-001/E33.1; SC-M01-001/E33.3; SC-M01-001/E33.4; SC-M01-001/E34.1; SC-M01-001/E34.3; SC-M01-001/E34.4; SC-M01-001/E35.1; SC-M01-001/E35.3; SC-M01-001/E35.4; SC-M01-001/E36.1; SC-M01-001/E36.3; SC-M01-001/E36.4; SC-M01-001/E37.1; SC-M01-001/E37.3; SC-M01-001/E37.4; SC-M01-001/E38.1; SC-M01-001/E38.3; SC-M01-001/E38.4; SC-M01-001/E39.1; SC-M01-001/E39.3; SC-M01-001/E39.4; SC-M01-001/E40.1; SC-M01-001/E40.3; SC-M01-001/E40.4; SC-M01-001/E41.1; SC-M01-001/E41.3; SC-M01-001/E41.4; SC-M01-001/E42.1; SC-M01-001/E42.3; SC-M01-001/E42.4; SC-M01-001/E43.1; SC-M01-001/E43.3; SC-M01-001/E43.4; SC-M01-001/E44.1; SC-M01-001/E44.3; SC-M01-001/E44.4; SC-M01-001/M2; SC-M01-001/E7.1; SC-M01-001/E16.4; SC-M01-001/E17.4; SC-M01-001/E18.4; SC-M01-001/E19.4; SC-M01-001/E21.4; SC-M01-001/E21.5; SC-M01-001/E22.4; SC-M01-001/E23.4; SC-M01-001/E24.4; SC-M01-001/E25.4; SC-M01-001/E26.4; SC-M01-001/E27.2; SC-M01-001/E28.2; SC-M01-001/E29.2; SC-M01-001/E30.2; SC-M01-001/E31.2; SC-M01-001/E32.2; SC-M01-001/E33.2; SC-M01-001/E34.2; SC-M01-001/E35.2; SC-M01-001/E36.2; SC-M01-001/E37.2; SC-M01-001/E38.2; SC-M01-001/E39.2; SC-M01-001/E40.2; SC-M01-001/E41.2; SC-M01-001/E42.2; SC-M01-001/E43.2; SC-M01-001/E44.2; SC-M01-037/M1; SC-M01-037/E1.1; SC-M01-037/E1.3; SC-M01-037/E1.4; SC-M01-001/E16.6; SC-M01-001/E21.8; SC-M01-001/E22.6; SC-M01-001/E23.6; SC-M01-001/E24.6; SC-M01-001/E25.6; SC-M01-001/E26.6; SC-M01-001/E5.1; SC-M01-001/E4.1; SC-M01-001/E6.1; SC-M01-001/E19.6; SC-M01-007/E56.4; SC-M01-007/E61.4; SC-M01-007/E72.4; SC-M01-007/E83.4; SC-M01-007/E94.4; SC-M01-007/E99.4; SC-M01-007/E105.4; SC-M01-001/E1.1; SC-M01-001/E2.1; SC-M01-001/E3.1; SC-M01-001/E27.8; SC-M01-001/E28.10; SC-M01-001/E29.10; SC-M01-001/E30.10; SC-M01-001/E31.10; SC-M01-001/E32.10; SC-M01-001/E34.10; SC-M01-001/E35.10; SC-M01-001/E36.10; SC-M01-001/E37.10; SC-M01-001/E38.6; SC-M01-001/E38.8; SC-M01-001/E42.8; SC-M01-001/E42.10; SC-M01-001/E43.6; SC-M01-001/E44.8; SC-M01-007/E20.4; SC-M01-007/E26.6; SC-M01-007/E27.6; SC-M01-007/E28.6; SC-M01-007/E29.6; SC-M01-007/E30.6; SC-M01-007/E57.6; SC-M01-007/E62.8; SC-M01-007/E63.8; SC-M01-007/E64.8; SC-M01-007/E65.8; SC-M01-007/E66.8; SC-M01-007/E68.6; SC-M01-007/E73.8; SC-M01-007/E74.8; SC-M01-007/E75.8; SC-M01-007/E76.8; SC-M01-007/E77.8; SC-M01-007/E79.6; SC-M01-007/E84.8; SC-M01-007/E85.8; SC-M01-007/E86.8; SC-M01-007/E87.8; SC-M01-007/E88.8 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-02 | SC-M01-001/M5; SC-M01-001/M6; SC-M01-001/E8.4; SC-M01-001/E9.4; SC-M01-001/E27.5; SC-M01-001/E27.6; SC-M01-001/E28.5; SC-M01-001/E28.6; SC-M01-001/E29.5; SC-M01-001/E29.6; SC-M01-001/E30.5; SC-M01-001/E30.6; SC-M01-001/E31.5; SC-M01-001/E31.6; SC-M01-001/E32.5; SC-M01-001/E32.6; SC-M01-001/E33.5; SC-M01-001/E33.6; SC-M01-001/E34.5; SC-M01-001/E34.6; SC-M01-001/E35.5; SC-M01-001/E35.6; SC-M01-001/E36.5; SC-M01-001/E36.6; SC-M01-001/E37.5; SC-M01-001/E37.6; SC-M01-001/E38.5; SC-M01-001/E38.6; SC-M01-001/E39.5; SC-M01-001/E40.5; SC-M01-001/E41.5; SC-M01-001/E42.7; SC-M01-001/E42.8; SC-M01-001/E43.7; SC-M01-001/E43.8; SC-M01-001/E44.9; SC-M01-001/E44.10; SC-M01-007/E6.3; SC-M01-007/E6.4; SC-M01-007/E12.3; SC-M01-007/E12.7; SC-M01-007/E12.8; SC-M01-007/E13.3; SC-M01-007/E13.7; SC-M01-007/E13.8; SC-M01-007/E14.3; SC-M01-007/E15.3; SC-M01-007/E15.4; SC-M01-007/E16.3; SC-M01-007/E16.4; SC-M01-007/E17.3; SC-M01-007/E17.4; SC-M01-007/E18.3; SC-M01-007/E18.4; SC-M01-007/E19.3; SC-M01-007/E19.4; SC-M01-007/E106.2; SC-M01-007/E106.3; SC-M01-001/E8.1; SC-M01-001/E9.1; SC-M01-001/E39.6; SC-M01-007/E12.4; SC-M01-007/E13.4; SC-M01-001/E10.1; SC-M01-001/E40.6; SC-M01-007/E14.4; SC-M01-001/E8.3; SC-M01-001/E9.3; SC-M01-001/E41.6; SC-M01-001/E42.6; SC-M01-001/E43.6; SC-M01-001/E44.8; SC-M01-007/E12.6; SC-M01-007/E13.6; SC-M01-001/E8.2; SC-M01-001/E9.2; SC-M01-001/E42.5; SC-M01-001/E43.5; SC-M01-001/E44.5; SC-M01-001/E44.7; SC-M01-007/E12.5; SC-M01-007/E13.5; SC-M01-001/E44.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03 | SC-M01-001/M7; SC-M01-001/M8; SC-M01-001/E16.7; SC-M01-001/E16.8; SC-M01-001/E21.9; SC-M01-001/E21.10; SC-M01-001/E22.7; SC-M01-001/E22.10; SC-M01-001/E23.7; SC-M01-001/E23.10; SC-M01-001/E24.7; SC-M01-001/E24.10; SC-M01-001/E25.7; SC-M01-001/E25.10; SC-M01-001/E26.7; SC-M01-001/E26.10; SC-M01-001/E27.7; SC-M01-001/E27.8; SC-M01-001/E28.7; SC-M01-001/E28.10; SC-M01-001/E29.7; SC-M01-001/E29.10; SC-M01-001/E30.7; SC-M01-001/E30.10; SC-M01-001/E31.7; SC-M01-001/E31.10; SC-M01-001/E32.7; SC-M01-001/E32.10; SC-M01-001/E33.7; SC-M01-001/E34.7; SC-M01-001/E34.10; SC-M01-001/E35.7; SC-M01-001/E35.10; SC-M01-001/E36.7; SC-M01-001/E36.10; SC-M01-001/E37.7; SC-M01-001/E37.10; SC-M01-001/E38.7; SC-M01-001/E38.8; SC-M01-001/E42.9; SC-M01-001/E42.10; SC-M01-001/E43.9; SC-M01-001/E43.10; SC-M01-001/E44.11; SC-M01-001/E44.12; SC-M01-007/E6.5; SC-M01-007/E6.6; SC-M01-007/E12.9; SC-M01-007/E12.10; SC-M01-007/E13.9; SC-M01-007/E13.10; SC-M01-007/E15.5; SC-M01-007/E15.8; SC-M01-007/E16.5; SC-M01-007/E16.8; SC-M01-007/E17.5; SC-M01-007/E17.8; SC-M01-007/E18.5; SC-M01-007/E18.8; SC-M01-007/E19.5; SC-M01-007/E19.8; SC-M01-007/E20.3; SC-M01-007/E20.4; SC-M01-007/E26.3; SC-M01-007/E26.6; SC-M01-007/E27.3; SC-M01-007/E27.6; SC-M01-007/E28.3; SC-M01-007/E28.6; SC-M01-007/E29.3; SC-M01-007/E29.6; SC-M01-007/E30.3; SC-M01-007/E30.6; SC-M01-007/E31.3; SC-M01-007/E57.5; SC-M01-007/E57.6; SC-M01-007/E62.5; SC-M01-007/E62.8; SC-M01-007/E63.5; SC-M01-007/E63.8; SC-M01-007/E64.5; SC-M01-007/E64.8; SC-M01-007/E65.5; SC-M01-007/E65.8; SC-M01-007/E66.5; SC-M01-007/E66.8; SC-M01-007/E67.5; SC-M01-007/E68.5; SC-M01-007/E68.6; SC-M01-007/E73.5; SC-M01-007/E73.8; SC-M01-007/E74.5; SC-M01-007/E74.8; SC-M01-007/E75.5; SC-M01-007/E75.8; SC-M01-007/E76.5; SC-M01-007/E76.8; SC-M01-007/E77.5; SC-M01-007/E77.8; SC-M01-007/E78.5; SC-M01-007/E79.5; SC-M01-007/E79.6; SC-M01-007/E84.5; SC-M01-007/E84.8; SC-M01-007/E85.5; SC-M01-007/E85.8; SC-M01-007/E86.5; SC-M01-007/E86.8; SC-M01-007/E87.5; SC-M01-007/E87.8; SC-M01-007/E88.5; SC-M01-007/E88.8; SC-M01-007/E89.5; SC-M01-007/E106.4; SC-M01-007/E106.5; SC-M01-001/E34.8; SC-M01-001/E34.9; SC-M01-001/E35.8; SC-M01-001/E35.9; SC-M01-001/E36.8; SC-M01-001/E36.9; SC-M01-001/E37.8; SC-M01-001/E37.9; SC-M01-001/E12.1; SC-M01-001/E12.2; SC-M01-001/E23.8; SC-M01-001/E23.9; SC-M01-001/E29.8; SC-M01-001/E29.9; SC-M01-007/E16.6; SC-M01-007/E16.7; SC-M01-007/E27.4; SC-M01-007/E27.5; SC-M01-007/E63.6; SC-M01-007/E63.7; SC-M01-007/E74.6; SC-M01-007/E74.7; SC-M01-007/E85.6; SC-M01-007/E85.7; RULE-M01-002; SC-M01-001/E13.1; SC-M01-001/E13.2; SC-M01-001/E24.8; SC-M01-001/E24.9; SC-M01-001/E30.8; SC-M01-001/E30.9; SC-M01-007/E17.6; SC-M01-007/E17.7; SC-M01-007/E28.4; SC-M01-007/E28.5; SC-M01-007/E64.6; SC-M01-007/E64.7; SC-M01-007/E75.6; SC-M01-007/E75.7; SC-M01-007/E86.6; SC-M01-007/E86.7; SC-M01-001/E14.1; SC-M01-001/E14.2; SC-M01-001/E25.8; SC-M01-001/E25.9; SC-M01-001/E31.8; SC-M01-001/E31.9; SC-M01-007/E18.6; SC-M01-007/E18.7; SC-M01-007/E29.4; SC-M01-007/E29.5; SC-M01-007/E65.6; SC-M01-007/E65.7; SC-M01-007/E76.6; SC-M01-007/E76.7; SC-M01-007/E87.6; SC-M01-007/E87.7; SC-M01-001/E15.1; SC-M01-001/E15.2; SC-M01-001/E26.8; SC-M01-001/E26.9; SC-M01-001/E32.8; SC-M01-001/E32.9; SC-M01-007/E19.6; SC-M01-007/E19.7; SC-M01-007/E30.4; SC-M01-007/E30.5; SC-M01-007/E66.6; SC-M01-007/E66.7; SC-M01-007/E77.6; SC-M01-007/E77.7; SC-M01-007/E88.6; SC-M01-007/E88.7; SC-M01-001/E11.1; SC-M01-001/E11.2; SC-M01-001/E22.8; SC-M01-001/E22.9; SC-M01-001/E28.8; SC-M01-001/E28.9; SC-M01-007/E15.6; SC-M01-007/E15.7; SC-M01-007/E26.4; SC-M01-007/E26.5; SC-M01-007/E62.6; SC-M01-007/E62.7; SC-M01-007/E73.6; SC-M01-007/E73.7; SC-M01-007/E84.6; SC-M01-007/E84.7; SC-M01-001/E33.8; SC-M01-007/E31.4; SC-M01-007/E67.6; SC-M01-007/E78.6; SC-M01-007/E89.6; SC-M01-007/E106.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-04 | SC-M01-001/E16.1; SC-M01-001/E16.2; SC-M01-001/E16.3; SC-M01-001/E16.6; SC-M01-001/E17.1; SC-M01-001/E17.2; SC-M01-001/E17.3; SC-M01-001/E18.1; SC-M01-001/E18.2; SC-M01-001/E18.3; SC-M01-001/E19.1; SC-M01-001/E19.2; SC-M01-001/E19.3; SC-M01-001/E20.1; SC-M01-001/E20.2; SC-M01-001/E20.3; SC-M01-001/E21.1; SC-M01-001/E21.2; SC-M01-001/E21.3; SC-M01-001/E21.8; SC-M01-001/E22.1; SC-M01-001/E22.2; SC-M01-001/E22.3; SC-M01-001/E22.6; SC-M01-001/E23.1; SC-M01-001/E23.2; SC-M01-001/E23.3; SC-M01-001/E23.6; SC-M01-001/E24.1; SC-M01-001/E24.2; SC-M01-001/E24.3; SC-M01-001/E24.6; SC-M01-001/E25.1; SC-M01-001/E25.2; SC-M01-001/E25.3; SC-M01-001/E25.6; SC-M01-001/E26.1; SC-M01-001/E26.2; SC-M01-001/E26.3; SC-M01-001/E26.6; SC-M01-007/E56.4; SC-M01-007/E61.4; SC-M01-007/E72.4; SC-M01-007/E83.4; SC-M01-007/E94.4; SC-M01-007/E99.4; SC-M01-007/E105.4; SC-M01-001/E16.4; SC-M01-001/E17.4; SC-M01-001/E17.6; SC-M01-001/E18.4; SC-M01-001/E19.4; SC-M01-001/E21.4; SC-M01-001/E22.4; SC-M01-001/E23.4; SC-M01-001/E24.4; SC-M01-001/E25.4; SC-M01-001/E26.4; SC-M01-001/E16.5; SC-M01-001/E17.5; SC-M01-001/E18.5; SC-M01-001/E19.5; SC-M01-001/E21.5; SC-M01-001/E21.7; SC-M01-001/E22.5; SC-M01-001/E23.5; SC-M01-001/E24.5; SC-M01-001/E25.5; SC-M01-001/E26.5; SC-M01-001/E16.7; SC-M01-001/E21.9; SC-M01-001/E22.7; SC-M01-001/E23.7; SC-M01-001/E24.7; SC-M01-001/E25.7; SC-M01-001/E26.7; SC-M01-001/E18.6; SC-M01-007/E68.4; SC-M01-007/E73.4; SC-M01-007/E74.4; SC-M01-007/E75.4; SC-M01-007/E76.4; SC-M01-007/E77.4; SC-M01-007/E78.4; SC-M01-007/E79.4; SC-M01-007/E84.4; SC-M01-007/E85.4; SC-M01-007/E86.4; SC-M01-007/E87.4; SC-M01-007/E88.4; SC-M01-007/E89.4; SC-M01-007/E90.4; SC-M01-001/E20.4; SC-M01-007/E52.3; SC-M01-007/E53.3; SC-M01-007/E54.3; SC-M01-007/E55.3; SC-M01-007/E56.3; SC-M01-007/E57.3; SC-M01-007/E58.3; SC-M01-007/E59.3; SC-M01-007/E60.3; SC-M01-007/E61.3; SC-M01-007/E62.3; SC-M01-007/E63.3; SC-M01-007/E64.3; SC-M01-007/E65.3; SC-M01-007/E66.3; SC-M01-007/E67.3; SC-M01-007/E68.3; SC-M01-007/E69.3; SC-M01-007/E70.3; SC-M01-007/E71.3; SC-M01-007/E72.3; SC-M01-007/E73.3; SC-M01-007/E74.3; SC-M01-007/E75.3; SC-M01-007/E76.3; SC-M01-007/E77.3; SC-M01-007/E78.3; SC-M01-007/E79.3; SC-M01-007/E80.3; SC-M01-007/E81.3; SC-M01-007/E82.3; SC-M01-007/E83.3; SC-M01-007/E84.3; SC-M01-007/E85.3; SC-M01-007/E86.3; SC-M01-007/E87.3; SC-M01-007/E88.3; SC-M01-007/E89.3; SC-M01-007/E90.3; SC-M01-007/E91.3; SC-M01-007/E92.3; SC-M01-007/E93.3; SC-M01-007/E94.3; SC-M01-007/E95.3; SC-M01-007/E96.3; SC-M01-007/E97.3; SC-M01-007/E98.3; SC-M01-007/E99.3; SC-M01-007/E100.3; SC-M01-007/E101.3; SC-M01-007/E102.3; SC-M01-007/E103.3; SC-M01-007/E104.3; SC-M01-007/E105.3; SC-M01-007/E52.1; SC-M01-007/E52.2; SC-M01-007/E52.4; SC-M01-007/E53.1; SC-M01-007/E53.2; SC-M01-007/E53.4; SC-M01-007/E54.1; SC-M01-007/E54.2; SC-M01-007/E54.4; SC-M01-007/E55.1; SC-M01-007/E55.2; SC-M01-007/E55.4; SC-M01-007/E56.1; SC-M01-007/E56.2; SC-M01-007/E57.1; SC-M01-007/E57.2; SC-M01-007/E57.4; SC-M01-007/E58.1; SC-M01-007/E58.2; SC-M01-007/E58.4; SC-M01-007/E59.1; SC-M01-007/E59.2; SC-M01-007/E59.4; SC-M01-007/E60.1; SC-M01-007/E60.2; SC-M01-007/E60.4; SC-M01-007/E61.1; SC-M01-007/E61.2; SC-M01-007/E62.1; SC-M01-007/E62.2; SC-M01-007/E62.4; SC-M01-007/E63.1; SC-M01-007/E63.2; SC-M01-007/E63.4; SC-M01-007/E64.1; SC-M01-007/E64.2; SC-M01-007/E64.4; SC-M01-007/E65.1; SC-M01-007/E65.2; SC-M01-007/E65.4; SC-M01-007/E66.1; SC-M01-007/E66.2; SC-M01-007/E66.4; SC-M01-007/E67.1; SC-M01-007/E67.2; SC-M01-007/E67.4; SC-M01-007/E68.1; SC-M01-007/E68.2; SC-M01-007/E69.1; SC-M01-007/E69.2; SC-M01-007/E69.4; SC-M01-007/E70.1; SC-M01-007/E70.2; SC-M01-007/E70.4; SC-M01-007/E71.1; SC-M01-007/E71.2; SC-M01-007/E71.4; SC-M01-007/E72.1; SC-M01-007/E72.2; SC-M01-007/E73.1; SC-M01-007/E73.2; SC-M01-007/E74.1; SC-M01-007/E74.2; SC-M01-007/E75.1; SC-M01-007/E75.2; SC-M01-007/E76.1; SC-M01-007/E76.2; SC-M01-007/E77.1; SC-M01-007/E77.2; SC-M01-007/E78.1; SC-M01-007/E78.2; SC-M01-007/E79.1; SC-M01-007/E79.2; SC-M01-007/E80.1; SC-M01-007/E80.2; SC-M01-007/E80.4; SC-M01-007/E81.1; SC-M01-007/E81.2; SC-M01-007/E81.4; SC-M01-007/E82.1; SC-M01-007/E82.2; SC-M01-007/E82.4; SC-M01-007/E83.1; SC-M01-007/E83.2; SC-M01-007/E84.1; SC-M01-007/E84.2; SC-M01-007/E85.1; SC-M01-007/E85.2; SC-M01-007/E86.1; SC-M01-007/E86.2; SC-M01-007/E87.1; SC-M01-007/E87.2; SC-M01-007/E88.1; SC-M01-007/E88.2; SC-M01-007/E89.1; SC-M01-007/E89.2; SC-M01-007/E90.1; SC-M01-007/E90.2; SC-M01-007/E91.1; SC-M01-007/E91.2; SC-M01-007/E91.4; SC-M01-007/E92.1; SC-M01-007/E92.2; SC-M01-007/E92.4; SC-M01-007/E93.1; SC-M01-007/E93.2; SC-M01-007/E93.4; SC-M01-007/E94.1; SC-M01-007/E94.2; SC-M01-007/E95.1; SC-M01-007/E95.2; SC-M01-007/E95.4; SC-M01-007/E96.1; SC-M01-007/E96.2; SC-M01-007/E96.4; SC-M01-007/E97.1; SC-M01-007/E97.2; SC-M01-007/E97.4; SC-M01-007/E98.1; SC-M01-007/E98.2; SC-M01-007/E98.4; SC-M01-007/E99.1; SC-M01-007/E99.2; SC-M01-007/E100.1; SC-M01-007/E100.2; SC-M01-007/E100.4; SC-M01-007/E101.1; SC-M01-007/E101.2; SC-M01-007/E101.4; SC-M01-007/E102.1; SC-M01-007/E102.2; SC-M01-007/E102.4; SC-M01-007/E103.1; SC-M01-007/E103.2; SC-M01-007/E103.4; SC-M01-007/E104.1; SC-M01-007/E104.2; SC-M01-007/E104.4; SC-M01-007/E105.1; SC-M01-007/E105.2 | Một phần — có GAP nguồn |
| FR-M01-05 | SC-M01-007/M1; SC-M01-007/M2; SC-M01-007/E3.1; SC-M01-007/E6.1; SC-M01-007/E6.2; SC-M01-007/E7.1; SC-M01-007/E8.1; SC-M01-007/E9.1; SC-M01-007/E9.2; SC-M01-007/E10.1; SC-M01-007/E11.1; SC-M01-007/E12.1; SC-M01-007/E12.2; SC-M01-007/E13.1; SC-M01-007/E13.2; SC-M01-007/E14.1; SC-M01-007/E14.2; SC-M01-007/E15.1; SC-M01-007/E15.2; SC-M01-007/E16.1; SC-M01-007/E16.2; SC-M01-007/E17.1; SC-M01-007/E17.2; SC-M01-007/E18.1; SC-M01-007/E18.2; SC-M01-007/E19.1; SC-M01-007/E19.2; SC-M01-007/E20.1; SC-M01-007/E20.2; SC-M01-007/E21.1; SC-M01-007/E22.1; SC-M01-007/E23.1; SC-M01-007/E23.2; SC-M01-007/E24.1; SC-M01-007/E25.1; SC-M01-007/E26.1; SC-M01-007/E26.2; SC-M01-007/E27.1; SC-M01-007/E27.2; SC-M01-007/E28.1; SC-M01-007/E28.2; SC-M01-007/E29.1; SC-M01-007/E29.2; SC-M01-007/E30.1; SC-M01-007/E30.2; SC-M01-007/E31.1; SC-M01-007/E31.2; SC-M01-007/E32.1; SC-M01-007/E32.2; SC-M01-007/E33.1; SC-M01-007/E34.1; SC-M01-007/E35.1; SC-M01-007/E35.2; SC-M01-007/E36.1; SC-M01-007/E37.1; SC-M01-007/E38.1; SC-M01-007/E38.2; SC-M01-007/E39.1; SC-M01-007/E40.1; SC-M01-007/E41.1; SC-M01-007/E41.2; SC-M01-007/E42.1; SC-M01-007/E43.1; SC-M01-007/E44.1; SC-M01-007/E44.2; SC-M01-007/E45.1; SC-M01-007/E46.1; SC-M01-007/E47.1; SC-M01-007/E47.2; SC-M01-007/E48.1; SC-M01-007/E49.1; SC-M01-007/E50.1; SC-M01-007/E51.1; SC-M01-007/E52.4; SC-M01-007/E57.4; SC-M01-007/E62.4; SC-M01-007/E63.4; SC-M01-007/E64.4; SC-M01-007/E65.4; SC-M01-007/E66.4; SC-M01-007/E67.4; SC-M01-007/E68.4; SC-M01-007/E73.4; SC-M01-007/E74.4; SC-M01-007/E75.4; SC-M01-007/E76.4; SC-M01-007/E77.4; SC-M01-007/E78.4; SC-M01-007/E79.4; SC-M01-007/E84.4; SC-M01-007/E85.4; SC-M01-007/E86.4; SC-M01-007/E87.4; SC-M01-007/E88.4; SC-M01-007/E89.4; SC-M01-007/E90.4; SC-M01-007/E101.4; SC-M01-007/E107.1; SC-M01-007/E107.2; SC-M01-007/E108.1; SC-M01-007/E108.2; SC-M01-007/E109.1; SC-M01-007/E109.2; SC-M01-007/E1.1; SC-M01-007/E7.2; SC-M01-007/E21.2; SC-M01-007/E33.2; SC-M01-007/E39.2; SC-M01-007/E45.2; SC-M01-007/E2.1; SC-M01-007/E8.2; SC-M01-007/E22.2; SC-M01-007/E34.2; SC-M01-007/E40.2; SC-M01-007/E46.2; SC-M01-007/E53.4; SC-M01-007/E58.4; SC-M01-007/E69.4; SC-M01-007/E80.4; SC-M01-007/E91.4; SC-M01-007/E96.4; SC-M01-007/E102.4; SC-M01-007/E4.1; SC-M01-007/E10.2; SC-M01-007/E24.2; SC-M01-007/E36.2; SC-M01-007/E42.2; SC-M01-007/E48.2; SC-M01-007/E54.4; SC-M01-007/E59.4; SC-M01-007/E70.4; SC-M01-007/E81.4; SC-M01-007/E92.4; SC-M01-007/E97.4; SC-M01-007/E103.4; SC-M01-007/E5.1; SC-M01-007/E11.2; SC-M01-007/E25.2; SC-M01-007/E37.2; SC-M01-007/E43.2; SC-M01-007/E49.2; SC-M01-007/E55.4; SC-M01-007/E60.4; SC-M01-007/E71.4; SC-M01-007/E82.4; SC-M01-007/E93.4; SC-M01-007/E98.4; SC-M01-007/E104.4; SC-M01-007/E50.2; SC-M01-007/E51.2; SC-M01-007/E95.4; SC-M01-007/E100.4; SC-M01-007/E50.4; SC-M01-007/E32.3; SC-M01-007/E32.4; SC-M01-007/E38.3; SC-M01-007/E38.4; SC-M01-007/E95.5; SC-M01-007/E95.6; SC-M01-014/E1.1; SC-M01-014/E1.2; SC-M01-007/E50.3; SC-M01-007/E51.3; SC-M01-007/E51.4; SC-M01-017/E8.1; SC-M01-022/E4.1; AUT-M01-001; RULE-M01-005; AUT-M01-004; RULE-M01-004 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-06 | AUT-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-07 | SC-M01-007/E32.3; SC-M01-007/E32.4; SC-M01-007/E38.3; SC-M01-007/E38.4; SC-M01-007/E51.4; SC-M01-007/E95.5; SC-M01-007/E95.6; SC-M01-007/E108.6; SC-M01-014/M1; SC-M01-014/M2; SC-M01-014/E1.1; SC-M01-014/E1.2; SC-M01-014/E2.1; SC-M01-014/E2.2; SC-M01-039/E1.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-08 | SC-M01-017/M1; SC-M01-017/M2; SC-M01-017/E1.1; SC-M01-017/E2.1; SC-M01-017/E3.1; SC-M01-017/E4.1; SC-M01-017/E5.1; SC-M01-017/E6.1; SC-M01-017/E7.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09 | SC-M01-018/M1; SC-M01-018/M2; SC-M01-018/E10.1; SC-M01-018/E10.2; SC-M01-018/E11.1; SC-M01-018/E11.2; SC-M01-018/E12.1; SC-M01-018/E12.2; SC-M01-018/E13.1; SC-M01-018/E13.2; SC-M01-018/E14.1; SC-M01-018/E14.2; SC-M01-018/E15.1; SC-M01-018/E15.2; SC-M01-018/E16.1; SC-M01-018/E16.2; SC-M01-018/E17.1; SC-M01-018/E18.1; SC-M01-018/E19.1; SC-M01-018/E3.1; SC-M01-018/E13.4; SC-M01-018/E7.1; SC-M01-018/E17.2; SC-M01-018/M3; SC-M01-018/M4; SC-M01-018/E10.3; SC-M01-018/E10.4; SC-M01-018/E11.3; SC-M01-018/E12.3; SC-M01-018/E13.3; SC-M01-018/E14.3; SC-M01-018/E15.3; SC-M01-018/E16.3; SC-M01-018/E1.1; SC-M01-018/E11.4; SC-M01-018/E2.1; SC-M01-018/E12.4; SC-M01-018/E4.1; SC-M01-018/E14.4; SC-M01-018/E5.1; SC-M01-018/E15.4; SC-M01-018/E6.1; SC-M01-018/E16.4; SC-M01-018/E8.1; SC-M01-018/E18.2; SC-M01-018/E9.1; SC-M01-018/E19.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-10 | SC-M01-007/E109.6; SC-M01-022/M1; SC-M01-022/M2; SC-M01-039/E2.6; SC-M01-022/E1.1; SC-M01-039/E3.6; SC-M01-022/E2.1; SC-M01-022/E3.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-11 | SC-M01-023/M1; SC-M01-023/M2; SC-M01-023/E4.2; SC-M01-023/E4.3; SC-M01-023/E5.2; SC-M01-023/E5.3; SC-M01-023/E6.1; SC-M01-023/E6.2; SC-M01-023/E7.1; SC-M01-023/E8.1; SC-M01-023/E8.2; SC-M01-023/E9.1; SC-M01-023/E9.2; SC-M01-023/E10.1; SC-M01-023/E10.2; SC-M01-023/E10.5; SC-M01-023/E10.6; SC-M01-023/E11.1; SC-M01-023/E11.2; SC-M01-023/E11.5; SC-M01-023/E11.6; SC-M01-023/E12.1; SC-M01-023/E12.3; SC-M01-023/E12.4; SC-M01-023/E12.2; SC-M01-023/M3; SC-M01-023/M4; SC-M01-023/E3.2; SC-M01-023/E4.4; SC-M01-023/E5.4; SC-M01-023/E6.3; SC-M01-023/E6.4; SC-M01-023/E8.3; SC-M01-023/E9.3; SC-M01-023/E9.5; SC-M01-023/E9.6; SC-M01-023/E10.3; SC-M01-023/E10.7; SC-M01-023/E10.8; SC-M01-023/E11.3; SC-M01-023/E11.7; SC-M01-023/E11.8; SC-M01-023/E12.5; SC-M01-023/E12.6; SC-M01-023/E3.1; SC-M01-023/E4.1; SC-M01-023/E9.4; SC-M01-023/E10.4; SC-M01-023/E2.1; SC-M01-023/E8.4; SC-M01-023/E5.1; SC-M01-023/E11.4; SC-M01-023/E1.1; SC-M01-023/E7.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-12 | SC-M01-007/E4.1; SC-M01-007/E10.2; SC-M01-007/E24.2; SC-M01-007/E36.2; SC-M01-007/E42.2; SC-M01-007/E48.2; SC-M01-007/E54.4; SC-M01-007/E59.4; SC-M01-007/E70.4; SC-M01-007/E81.4; SC-M01-007/E92.4; SC-M01-007/E97.4; SC-M01-007/E103.4; SC-M01-023/E2.1; SC-M01-023/E8.4; AUT-M01-002; SC-M01-025/E1.1; AUT-M01-003 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-13 | SC-M01-007/E109.6; SC-M01-022/M2; SC-M01-025/E1.1; SC-M01-025/E2.1; SC-M01-039/E2.6; AUT-M01-002; RULE-M01-001; SC-M01-025/M1; SC-M01-025/M2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14 | SC-M01-034/M1; SC-M01-034/M2; SC-M01-034/E2.1; SC-M01-034/E2.2; SC-M01-034/E3.1; SC-M01-034/E3.2; SC-M01-034/E4.1; SC-M01-034/E5.1; SC-M01-034/E5.2; SC-M01-034/E6.1; SC-M01-034/E6.2; SC-M01-034/E7.1; SC-M01-034/E8.1; SC-M01-034/E8.2; SC-M01-034/E9.1; SC-M01-034/E9.2; SC-M01-034/E10.1; SC-M01-034/E11.1; SC-M01-034/E11.2; SC-M01-034/E12.1; SC-M01-034/E12.2; SC-M01-034/E13.1; SC-M01-034/M3; SC-M01-034/M4; SC-M01-034/E1.1; SC-M01-034/E1.2; SC-M01-034/E2.3; SC-M01-034/E2.4; SC-M01-034/E5.3; SC-M01-034/E5.4; SC-M01-034/E8.3; SC-M01-034/E8.4; SC-M01-034/E11.3; SC-M01-034/E11.4; SC-M01-034/E14.1; SC-M01-034/E14.2; SC-M01-034/E15.1; SC-M01-034/E15.2; RULE-MENTION-035; SC-M01-034/E14.4; SC-M01-034/E15.3; SC-M01-034/E15.4; SC-M01-034/E15.6; SC-M01-034/E4.2; SC-M01-034/E7.2; SC-M01-034/E10.2; SC-M01-034/E13.2; AUT-M01-005; SC-M01-034/E14.3; SC-M01-034/E15.5; SC-M01-034/E16.1; RULE-MENTION-036 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-15 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-037/M1; SC-M01-037/M2; SC-M01-037/E1.1; SC-M01-037/E1.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-16 | SC-M01-007/E107.2; SC-M01-007/E108.2; SC-M01-007/E109.2; SC-M01-039/M1; SC-M01-039/M2; SC-M01-039/E1.1; SC-M01-039/E1.2; SC-M01-039/E2.1; SC-M01-039/E2.2; SC-M01-039/E3.1; SC-M01-039/E3.2; SC-M01-039/E4.1; SC-M01-007/E107.3; SC-M01-007/E107.4; SC-M01-039/M3; SC-M01-039/M4; SC-M01-007/E108.3; SC-M01-007/E108.4; SC-M01-007/E108.5; SC-M01-007/E108.6; SC-M01-007/E109.3; SC-M01-007/E109.4; SC-M01-007/E109.5; SC-M01-007/E109.6; SC-M01-014/E2.1; SC-M01-014/E2.2; SC-M01-039/E1.3; SC-M01-039/E1.4; SC-M01-039/E1.5; SC-M01-039/E1.6; SC-M01-039/E2.3; SC-M01-039/E2.4; SC-M01-039/E2.5; SC-M01-039/E2.6; SC-M01-039/E3.3; SC-M01-039/E3.4; SC-M01-039/E3.5; SC-M01-039/E3.6; SC-M01-039/E4.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-01.01 | SC-M01-001/M1; SC-M01-001/M3; SC-M01-001/M4; SC-M01-001/E7.3; SC-M01-001/E27.1; SC-M01-001/E27.3; SC-M01-001/E27.4; SC-M01-001/E28.1; SC-M01-001/E28.3; SC-M01-001/E28.4; SC-M01-001/E29.1; SC-M01-001/E29.3; SC-M01-001/E29.4; SC-M01-001/E30.1; SC-M01-001/E30.3; SC-M01-001/E30.4; SC-M01-001/E31.1; SC-M01-001/E31.3; SC-M01-001/E31.4; SC-M01-001/E32.1; SC-M01-001/E32.3; SC-M01-001/E32.4; SC-M01-001/E33.1; SC-M01-001/E33.3; SC-M01-001/E33.4; SC-M01-001/E34.1; SC-M01-001/E34.3; SC-M01-001/E34.4; SC-M01-001/E35.1; SC-M01-001/E35.3; SC-M01-001/E35.4; SC-M01-001/E36.1; SC-M01-001/E36.3; SC-M01-001/E36.4; SC-M01-001/E37.1; SC-M01-001/E37.3; SC-M01-001/E37.4; SC-M01-001/E38.1; SC-M01-001/E38.3; SC-M01-001/E38.4; SC-M01-001/E39.1; SC-M01-001/E39.3; SC-M01-001/E39.4; SC-M01-001/E40.1; SC-M01-001/E40.3; SC-M01-001/E40.4; SC-M01-001/E41.1; SC-M01-001/E41.3; SC-M01-001/E41.4; SC-M01-001/E42.1; SC-M01-001/E42.3; SC-M01-001/E42.4; SC-M01-001/E43.1; SC-M01-001/E43.3; SC-M01-001/E43.4; SC-M01-001/E44.1; SC-M01-001/E44.3; SC-M01-001/E44.4 | Một phần — có GAP nguồn |
| FR-M01-01.02 | SC-M01-001/M4; SC-M01-001/E16.6; SC-M01-001/E21.8; SC-M01-001/E22.6; SC-M01-001/E23.6; SC-M01-001/E24.6; SC-M01-001/E25.6; SC-M01-001/E26.6; SC-M01-001/E27.4; SC-M01-001/E28.4; SC-M01-001/E29.4; SC-M01-001/E30.4; SC-M01-001/E31.4; SC-M01-001/E32.4; SC-M01-001/E33.4; SC-M01-001/E34.4; SC-M01-001/E35.4; SC-M01-001/E36.4; SC-M01-001/E37.4; SC-M01-001/E38.4; SC-M01-001/E39.4; SC-M01-001/E40.4; SC-M01-001/E41.4; SC-M01-001/E42.4; SC-M01-001/E43.4; SC-M01-001/E44.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-01.03 | SC-M01-001/M4; SC-M01-001/E27.4; SC-M01-001/E28.4; SC-M01-001/E29.4; SC-M01-001/E30.4; SC-M01-001/E31.4; SC-M01-001/E32.4; SC-M01-001/E33.4; SC-M01-001/E34.4; SC-M01-001/E35.4; SC-M01-001/E36.4; SC-M01-001/E37.4; SC-M01-001/E38.4; SC-M01-001/E39.4; SC-M01-001/E40.4; SC-M01-001/E41.4; SC-M01-001/E42.4; SC-M01-001/E43.4; SC-M01-001/E44.4 | Một phần — có GAP nguồn |
| FR-M01-01.04 | SC-M01-001/M2; SC-M01-001/E7.1; SC-M01-001/E16.4; SC-M01-001/E17.4; SC-M01-001/E18.4; SC-M01-001/E19.4; SC-M01-001/E21.4; SC-M01-001/E21.5; SC-M01-001/E22.4; SC-M01-001/E23.4; SC-M01-001/E24.4; SC-M01-001/E25.4; SC-M01-001/E26.4; SC-M01-001/E27.2; SC-M01-001/E28.2; SC-M01-001/E29.2; SC-M01-001/E30.2; SC-M01-001/E31.2; SC-M01-001/E32.2; SC-M01-001/E33.2; SC-M01-001/E34.2; SC-M01-001/E35.2; SC-M01-001/E36.2; SC-M01-001/E37.2; SC-M01-001/E38.2; SC-M01-001/E39.2; SC-M01-001/E40.2; SC-M01-001/E41.2; SC-M01-001/E42.2; SC-M01-001/E43.2; SC-M01-001/E44.2; SC-M01-037/M1; SC-M01-037/E1.1; SC-M01-037/E1.3 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-01.05 | SC-M01-001/E1.1; SC-M01-037/E1.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-01.06 | SC-M01-001/E3.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-01.07 | SC-M01-001/E2.1 | Một phần — có GAP nguồn |
| FR-M01-01.08 | SC-M01-001/M4; SC-M01-001/E5.1; SC-M01-001/E27.4; SC-M01-001/E28.4; SC-M01-001/E29.4; SC-M01-001/E30.4; SC-M01-001/E31.4; SC-M01-001/E32.4; SC-M01-001/E33.4; SC-M01-001/E34.4; SC-M01-001/E35.4; SC-M01-001/E36.4; SC-M01-001/E37.4; SC-M01-001/E38.4; SC-M01-001/E39.4; SC-M01-001/E40.4; SC-M01-001/E41.4; SC-M01-001/E42.4; SC-M01-001/E43.4; SC-M01-001/E44.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-01.09 | SC-M01-001/E5.1; SC-M01-001/E27.8; SC-M01-001/E28.10; SC-M01-001/E29.10; SC-M01-001/E30.10; SC-M01-001/E31.10; SC-M01-001/E32.10; SC-M01-001/E34.10; SC-M01-001/E35.10; SC-M01-001/E36.10; SC-M01-001/E37.10; SC-M01-001/E38.6; SC-M01-001/E38.8; SC-M01-001/E42.8; SC-M01-001/E42.10; SC-M01-001/E43.6; SC-M01-001/E44.8; SC-M01-007/E20.4; SC-M01-007/E26.6; SC-M01-007/E27.6; SC-M01-007/E28.6; SC-M01-007/E29.6; SC-M01-007/E30.6; SC-M01-007/E57.6; SC-M01-007/E62.8; SC-M01-007/E63.8; SC-M01-007/E64.8; SC-M01-007/E65.8; SC-M01-007/E66.8; SC-M01-007/E68.6; SC-M01-007/E73.8; SC-M01-007/E74.8; SC-M01-007/E75.8; SC-M01-007/E76.8; SC-M01-007/E77.8; SC-M01-007/E79.6; SC-M01-007/E84.8; SC-M01-007/E85.8; SC-M01-007/E86.8; SC-M01-007/E87.8; SC-M01-007/E88.8 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-01.10 | SC-M01-001/M4; SC-M01-001/E4.1; SC-M01-001/E27.4; SC-M01-001/E28.4; SC-M01-001/E29.4; SC-M01-001/E30.4; SC-M01-001/E31.4; SC-M01-001/E32.4; SC-M01-001/E33.4; SC-M01-001/E34.4; SC-M01-001/E35.4; SC-M01-001/E36.4; SC-M01-001/E37.4; SC-M01-001/E38.4; SC-M01-001/E39.4; SC-M01-001/E40.4; SC-M01-001/E41.4; SC-M01-001/E42.4; SC-M01-001/E43.4; SC-M01-001/E44.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-01.11 | SC-M01-001/M3; SC-M01-001/M4; SC-M01-001/E27.3; SC-M01-001/E27.4; SC-M01-001/E28.3; SC-M01-001/E28.4; SC-M01-001/E29.3; SC-M01-001/E29.4; SC-M01-001/E30.3; SC-M01-001/E30.4; SC-M01-001/E31.3; SC-M01-001/E31.4; SC-M01-001/E32.3; SC-M01-001/E32.4; SC-M01-001/E33.3; SC-M01-001/E33.4; SC-M01-001/E34.3; SC-M01-001/E34.4; SC-M01-001/E35.3; SC-M01-001/E35.4; SC-M01-001/E36.3; SC-M01-001/E36.4; SC-M01-001/E37.3; SC-M01-001/E37.4; SC-M01-001/E38.3; SC-M01-001/E38.4; SC-M01-001/E39.3; SC-M01-001/E39.4; SC-M01-001/E40.3; SC-M01-001/E40.4; SC-M01-001/E41.3; SC-M01-001/E41.4; SC-M01-001/E42.3; SC-M01-001/E42.4; SC-M01-001/E43.3; SC-M01-001/E43.4; SC-M01-001/E44.3; SC-M01-001/E44.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-01.12 | SC-M01-001/M4; SC-M01-001/E6.1; SC-M01-001/E16.6; SC-M01-001/E19.6; SC-M01-001/E21.8; SC-M01-001/E22.6; SC-M01-001/E23.6; SC-M01-001/E24.6; SC-M01-001/E25.6; SC-M01-001/E26.6; SC-M01-001/E27.4; SC-M01-001/E28.4; SC-M01-001/E29.4; SC-M01-001/E30.4; SC-M01-001/E31.4; SC-M01-001/E32.4; SC-M01-001/E33.4; SC-M01-001/E34.4; SC-M01-001/E35.4; SC-M01-001/E36.4; SC-M01-001/E37.4; SC-M01-001/E38.4; SC-M01-001/E39.4; SC-M01-001/E40.4; SC-M01-001/E41.4; SC-M01-001/E42.4; SC-M01-001/E43.4; SC-M01-001/E44.4; SC-M01-007/E56.4; SC-M01-007/E61.4; SC-M01-007/E72.4; SC-M01-007/E83.4; SC-M01-007/E94.4; SC-M01-007/E99.4; SC-M01-007/E105.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-01.13 | SC-M01-001/M2; SC-M01-001/M3; SC-M01-001/E7.3; SC-M01-001/E16.4; SC-M01-001/E17.4; SC-M01-001/E18.4; SC-M01-001/E19.4; SC-M01-001/E21.4; SC-M01-001/E22.4; SC-M01-001/E23.4; SC-M01-001/E24.4; SC-M01-001/E25.4; SC-M01-001/E26.4; SC-M01-001/E27.2; SC-M01-001/E27.3; SC-M01-001/E28.2; SC-M01-001/E28.3; SC-M01-001/E29.2; SC-M01-001/E29.3; SC-M01-001/E30.2; SC-M01-001/E30.3; SC-M01-001/E31.2; SC-M01-001/E31.3; SC-M01-001/E32.2; SC-M01-001/E32.3; SC-M01-001/E33.2; SC-M01-001/E33.3; SC-M01-001/E34.2; SC-M01-001/E34.3; SC-M01-001/E35.2; SC-M01-001/E35.3; SC-M01-001/E36.2; SC-M01-001/E36.3; SC-M01-001/E37.2; SC-M01-001/E37.3; SC-M01-001/E38.2; SC-M01-001/E38.3; SC-M01-001/E39.2; SC-M01-001/E39.3; SC-M01-001/E40.2; SC-M01-001/E40.3; SC-M01-001/E41.2; SC-M01-001/E41.3; SC-M01-001/E42.2; SC-M01-001/E42.3; SC-M01-001/E43.2; SC-M01-001/E43.3; SC-M01-001/E44.2; SC-M01-001/E44.3; SC-M01-037/E1.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-01.14 | SC-M01-001/M4; SC-M01-001/E27.4; SC-M01-001/E28.4; SC-M01-001/E29.4; SC-M01-001/E30.4; SC-M01-001/E31.4; SC-M01-001/E32.4; SC-M01-001/E33.4; SC-M01-001/E34.4; SC-M01-001/E35.4; SC-M01-001/E36.4; SC-M01-001/E37.4; SC-M01-001/E38.4; SC-M01-001/E39.4; SC-M01-001/E40.4; SC-M01-001/E41.4; SC-M01-001/E42.4; SC-M01-001/E43.4; SC-M01-001/E44.4; SC-M01-037/E1.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-01.15 | SC-M01-001/M2; SC-M01-001/E16.4; SC-M01-001/E17.4; SC-M01-001/E18.4; SC-M01-001/E19.4; SC-M01-001/E21.4; SC-M01-001/E22.4; SC-M01-001/E23.4; SC-M01-001/E24.4; SC-M01-001/E25.4; SC-M01-001/E26.4; SC-M01-001/E27.2; SC-M01-001/E28.2; SC-M01-001/E29.2; SC-M01-001/E30.2; SC-M01-001/E31.2; SC-M01-001/E32.2; SC-M01-001/E33.2; SC-M01-001/E34.2; SC-M01-001/E35.2; SC-M01-001/E36.2; SC-M01-001/E37.2; SC-M01-001/E38.2; SC-M01-001/E39.2; SC-M01-001/E40.2; SC-M01-001/E41.2; SC-M01-001/E42.2; SC-M01-001/E43.2; SC-M01-001/E44.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-02.01 | SC-M01-001/M5; SC-M01-001/M6; SC-M01-001/E8.4; SC-M01-001/E9.4; SC-M01-001/E27.5; SC-M01-001/E27.6; SC-M01-001/E28.5; SC-M01-001/E28.6; SC-M01-001/E29.5; SC-M01-001/E29.6; SC-M01-001/E30.5; SC-M01-001/E30.6; SC-M01-001/E31.5; SC-M01-001/E31.6; SC-M01-001/E32.5; SC-M01-001/E32.6; SC-M01-001/E33.5; SC-M01-001/E33.6; SC-M01-001/E34.5; SC-M01-001/E34.6; SC-M01-001/E35.5; SC-M01-001/E35.6; SC-M01-001/E36.5; SC-M01-001/E36.6; SC-M01-001/E37.5; SC-M01-001/E37.6; SC-M01-001/E38.5; SC-M01-001/E38.6; SC-M01-001/E39.5; SC-M01-001/E40.5; SC-M01-001/E41.5; SC-M01-001/E42.7; SC-M01-001/E42.8; SC-M01-001/E43.7; SC-M01-001/E43.8; SC-M01-001/E44.9; SC-M01-001/E44.10; SC-M01-007/E6.3; SC-M01-007/E6.4; SC-M01-007/E12.3; SC-M01-007/E12.7; SC-M01-007/E12.8; SC-M01-007/E13.3; SC-M01-007/E13.7; SC-M01-007/E13.8; SC-M01-007/E14.3; SC-M01-007/E15.3; SC-M01-007/E15.4; SC-M01-007/E16.3; SC-M01-007/E16.4; SC-M01-007/E17.3; SC-M01-007/E17.4; SC-M01-007/E18.3; SC-M01-007/E18.4; SC-M01-007/E19.3; SC-M01-007/E19.4; SC-M01-007/E106.2; SC-M01-007/E106.3 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-02.02 | SC-M01-001/M6; SC-M01-001/E27.6; SC-M01-001/E28.6; SC-M01-001/E29.6; SC-M01-001/E30.6; SC-M01-001/E31.6; SC-M01-001/E32.6; SC-M01-001/E33.6; SC-M01-001/E34.6; SC-M01-001/E35.6; SC-M01-001/E36.6; SC-M01-001/E37.6; SC-M01-001/E38.6; SC-M01-001/E42.8; SC-M01-001/E43.8; SC-M01-001/E44.10; SC-M01-007/E6.4; SC-M01-007/E12.8; SC-M01-007/E13.8; SC-M01-007/E15.4; SC-M01-007/E16.4; SC-M01-007/E17.4; SC-M01-007/E18.4; SC-M01-007/E19.4; SC-M01-007/E106.3 | Một phần — có GAP nguồn |
| FR-M01-02.03 | SC-M01-001/M6; SC-M01-001/E8.1; SC-M01-001/E9.1; SC-M01-001/E27.6; SC-M01-001/E28.6; SC-M01-001/E29.6; SC-M01-001/E30.6; SC-M01-001/E31.6; SC-M01-001/E32.6; SC-M01-001/E33.6; SC-M01-001/E34.6; SC-M01-001/E35.6; SC-M01-001/E36.6; SC-M01-001/E37.6; SC-M01-001/E38.6; SC-M01-001/E39.6; SC-M01-001/E42.8; SC-M01-001/E43.8; SC-M01-001/E44.10; SC-M01-007/E6.4; SC-M01-007/E12.4; SC-M01-007/E12.8; SC-M01-007/E13.4; SC-M01-007/E13.8; SC-M01-007/E15.4; SC-M01-007/E16.4; SC-M01-007/E17.4; SC-M01-007/E18.4; SC-M01-007/E19.4; SC-M01-007/E106.3 | Một phần — có GAP nguồn |
| FR-M01-02.04 | SC-M01-001/E8.2; SC-M01-001/E8.3; SC-M01-001/E9.2; SC-M01-001/E9.3; SC-M01-001/E42.5; SC-M01-001/E42.6; SC-M01-001/E43.5; SC-M01-001/E43.6; SC-M01-001/E44.5; SC-M01-001/E44.7; SC-M01-001/E44.8; SC-M01-007/E12.5; SC-M01-007/E12.6; SC-M01-007/E13.5; SC-M01-007/E13.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-02.05 | SC-M01-001/E8.2; SC-M01-001/E9.2; SC-M01-001/E42.5; SC-M01-001/E43.6; SC-M01-001/E44.6; SC-M01-001/E44.7; SC-M01-001/E44.8; SC-M01-007/E12.5; SC-M01-007/E13.5 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-02.06 | SC-M01-001/M6; SC-M01-001/E8.1; SC-M01-001/E9.1; SC-M01-001/E10.1; SC-M01-001/E27.6; SC-M01-001/E28.6; SC-M01-001/E29.6; SC-M01-001/E30.6; SC-M01-001/E31.6; SC-M01-001/E32.6; SC-M01-001/E33.6; SC-M01-001/E34.6; SC-M01-001/E35.6; SC-M01-001/E36.6; SC-M01-001/E37.6; SC-M01-001/E38.6; SC-M01-001/E40.6; SC-M01-001/E42.8; SC-M01-001/E43.8; SC-M01-001/E44.10; SC-M01-007/E6.4; SC-M01-007/E12.4; SC-M01-007/E12.8; SC-M01-007/E13.4; SC-M01-007/E13.8; SC-M01-007/E14.4; SC-M01-007/E15.4; SC-M01-007/E16.4; SC-M01-007/E17.4; SC-M01-007/E18.4; SC-M01-007/E19.4; SC-M01-007/E106.3 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-02.07 | SC-M01-001/E8.1; SC-M01-001/E8.3; SC-M01-001/E9.1; SC-M01-001/E9.3; SC-M01-001/E38.6; SC-M01-001/E41.6; SC-M01-001/E42.6; SC-M01-001/E42.8; SC-M01-001/E43.6; SC-M01-001/E44.8; SC-M01-007/E12.4; SC-M01-007/E12.6; SC-M01-007/E13.4; SC-M01-007/E13.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.01 | SC-M01-001/M7; SC-M01-001/M8; SC-M01-001/E16.7; SC-M01-001/E16.8; SC-M01-001/E21.9; SC-M01-001/E21.10; SC-M01-001/E22.7; SC-M01-001/E22.10; SC-M01-001/E23.7; SC-M01-001/E23.10; SC-M01-001/E24.7; SC-M01-001/E24.10; SC-M01-001/E25.7; SC-M01-001/E25.10; SC-M01-001/E26.7; SC-M01-001/E26.10; SC-M01-001/E27.7; SC-M01-001/E27.8; SC-M01-001/E28.7; SC-M01-001/E28.10; SC-M01-001/E29.7; SC-M01-001/E29.10; SC-M01-001/E30.7; SC-M01-001/E30.10; SC-M01-001/E31.7; SC-M01-001/E31.10; SC-M01-001/E32.7; SC-M01-001/E32.10; SC-M01-001/E33.7; SC-M01-001/E34.7; SC-M01-001/E34.10; SC-M01-001/E35.7; SC-M01-001/E35.10; SC-M01-001/E36.7; SC-M01-001/E36.10; SC-M01-001/E37.7; SC-M01-001/E37.10; SC-M01-001/E38.7; SC-M01-001/E38.8; SC-M01-001/E42.9; SC-M01-001/E42.10; SC-M01-001/E43.9; SC-M01-001/E43.10; SC-M01-001/E44.11; SC-M01-001/E44.12; SC-M01-007/E6.5; SC-M01-007/E6.6; SC-M01-007/E12.9; SC-M01-007/E12.10; SC-M01-007/E13.9; SC-M01-007/E13.10; SC-M01-007/E15.5; SC-M01-007/E15.8; SC-M01-007/E16.5; SC-M01-007/E16.8; SC-M01-007/E17.5; SC-M01-007/E17.8; SC-M01-007/E18.5; SC-M01-007/E18.8; SC-M01-007/E19.5; SC-M01-007/E19.8; SC-M01-007/E20.3; SC-M01-007/E20.4; SC-M01-007/E26.3; SC-M01-007/E26.6; SC-M01-007/E27.3; SC-M01-007/E27.6; SC-M01-007/E28.3; SC-M01-007/E28.6; SC-M01-007/E29.3; SC-M01-007/E29.6; SC-M01-007/E30.3; SC-M01-007/E30.6; SC-M01-007/E31.3; SC-M01-007/E57.5; SC-M01-007/E57.6; SC-M01-007/E62.5; SC-M01-007/E62.8; SC-M01-007/E63.5; SC-M01-007/E63.8; SC-M01-007/E64.5; SC-M01-007/E64.8; SC-M01-007/E65.5; SC-M01-007/E65.8; SC-M01-007/E66.5; SC-M01-007/E66.8; SC-M01-007/E67.5; SC-M01-007/E68.5; SC-M01-007/E68.6; SC-M01-007/E73.5; SC-M01-007/E73.8; SC-M01-007/E74.5; SC-M01-007/E74.8; SC-M01-007/E75.5; SC-M01-007/E75.8; SC-M01-007/E76.5; SC-M01-007/E76.8; SC-M01-007/E77.5; SC-M01-007/E77.8; SC-M01-007/E78.5; SC-M01-007/E79.5; SC-M01-007/E79.6; SC-M01-007/E84.5; SC-M01-007/E84.8; SC-M01-007/E85.5; SC-M01-007/E85.8; SC-M01-007/E86.5; SC-M01-007/E86.8; SC-M01-007/E87.5; SC-M01-007/E87.8; SC-M01-007/E88.5; SC-M01-007/E88.8; SC-M01-007/E89.5; SC-M01-007/E106.4; SC-M01-007/E106.5 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.02 | SC-M01-001/M7; SC-M01-001/M8; SC-M01-001/E16.7; SC-M01-001/E16.8; SC-M01-001/E21.9; SC-M01-001/E21.10; SC-M01-001/E22.7; SC-M01-001/E22.10; SC-M01-001/E23.7; SC-M01-001/E23.10; SC-M01-001/E24.7; SC-M01-001/E24.10; SC-M01-001/E25.7; SC-M01-001/E25.10; SC-M01-001/E26.7; SC-M01-001/E26.10; SC-M01-001/E27.7; SC-M01-001/E27.8; SC-M01-001/E28.7; SC-M01-001/E28.10; SC-M01-001/E29.7; SC-M01-001/E29.10; SC-M01-001/E30.7; SC-M01-001/E30.10; SC-M01-001/E31.7; SC-M01-001/E31.10; SC-M01-001/E32.7; SC-M01-001/E32.10; SC-M01-001/E33.7; SC-M01-001/E34.7; SC-M01-001/E34.8; SC-M01-001/E34.9; SC-M01-001/E34.10; SC-M01-001/E35.7; SC-M01-001/E35.8; SC-M01-001/E35.9; SC-M01-001/E35.10; SC-M01-001/E36.7; SC-M01-001/E36.8; SC-M01-001/E36.9; SC-M01-001/E36.10; SC-M01-001/E37.7; SC-M01-001/E37.8; SC-M01-001/E37.9; SC-M01-001/E37.10; SC-M01-001/E38.7; SC-M01-001/E38.8; SC-M01-001/E42.9; SC-M01-001/E42.10; SC-M01-001/E43.9; SC-M01-001/E43.10; SC-M01-001/E44.11; SC-M01-001/E44.12; SC-M01-007/E6.5; SC-M01-007/E6.6; SC-M01-007/E12.9; SC-M01-007/E12.10; SC-M01-007/E13.9; SC-M01-007/E13.10; SC-M01-007/E15.5; SC-M01-007/E15.8; SC-M01-007/E16.5; SC-M01-007/E16.8; SC-M01-007/E17.5; SC-M01-007/E17.8; SC-M01-007/E18.5; SC-M01-007/E18.8; SC-M01-007/E19.5; SC-M01-007/E19.8; SC-M01-007/E20.3; SC-M01-007/E20.4; SC-M01-007/E26.3; SC-M01-007/E26.6; SC-M01-007/E27.3; SC-M01-007/E27.6; SC-M01-007/E28.3; SC-M01-007/E28.6; SC-M01-007/E29.3; SC-M01-007/E29.6; SC-M01-007/E30.3; SC-M01-007/E30.6; SC-M01-007/E31.3; SC-M01-007/E57.5; SC-M01-007/E57.6; SC-M01-007/E62.5; SC-M01-007/E62.8; SC-M01-007/E63.5; SC-M01-007/E63.8; SC-M01-007/E64.5; SC-M01-007/E64.8; SC-M01-007/E65.5; SC-M01-007/E65.8; SC-M01-007/E66.5; SC-M01-007/E66.8; SC-M01-007/E67.5; SC-M01-007/E68.5; SC-M01-007/E68.6; SC-M01-007/E73.5; SC-M01-007/E73.8; SC-M01-007/E74.5; SC-M01-007/E74.8; SC-M01-007/E75.5; SC-M01-007/E75.8; SC-M01-007/E76.5; SC-M01-007/E76.8; SC-M01-007/E77.5; SC-M01-007/E77.8; SC-M01-007/E78.5; SC-M01-007/E79.5; SC-M01-007/E79.6; SC-M01-007/E84.5; SC-M01-007/E84.8; SC-M01-007/E85.5; SC-M01-007/E85.8; SC-M01-007/E86.5; SC-M01-007/E86.8; SC-M01-007/E87.5; SC-M01-007/E87.8; SC-M01-007/E88.5; SC-M01-007/E88.8; SC-M01-007/E89.5; SC-M01-007/E106.4; SC-M01-007/E106.5 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.03 | SC-M01-001/E27.7; SC-M01-001/E27.8; SC-M01-001/E28.7; SC-M01-001/E28.10; SC-M01-001/E29.7; SC-M01-001/E29.10; SC-M01-001/E30.7; SC-M01-001/E30.10; SC-M01-001/E31.7; SC-M01-001/E31.10; SC-M01-001/E32.7; SC-M01-001/E32.10; SC-M01-001/E33.7; SC-M01-001/E34.7; SC-M01-001/E34.8; SC-M01-001/E34.9; SC-M01-001/E34.10; SC-M01-001/E35.7; SC-M01-001/E35.8; SC-M01-001/E35.9; SC-M01-001/E35.10; SC-M01-001/E36.7; SC-M01-001/E36.8; SC-M01-001/E36.9; SC-M01-001/E36.10; SC-M01-001/E37.7; SC-M01-001/E37.8; SC-M01-001/E37.9; SC-M01-001/E37.10; SC-M01-001/E38.7; SC-M01-001/E42.9; SC-M01-007/E20.3; SC-M01-007/E26.3; SC-M01-007/E27.3; SC-M01-007/E28.3; SC-M01-007/E29.3; SC-M01-007/E30.3; SC-M01-007/E31.3; SC-M01-007/E57.5; SC-M01-007/E62.5; SC-M01-007/E63.5; SC-M01-007/E64.5; SC-M01-007/E65.5; SC-M01-007/E66.5; SC-M01-007/E67.5; SC-M01-007/E68.5; SC-M01-007/E73.5; SC-M01-007/E74.5; SC-M01-007/E75.5; SC-M01-007/E76.5; SC-M01-007/E77.5; SC-M01-007/E78.5; SC-M01-007/E79.5; SC-M01-007/E84.5; SC-M01-007/E85.5; SC-M01-007/E86.5; SC-M01-007/E87.5; SC-M01-007/E88.5; SC-M01-007/E89.5 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.04 | SC-M01-001/E11.1; SC-M01-001/E11.2; SC-M01-001/E22.8; SC-M01-001/E22.9; SC-M01-001/E28.8; SC-M01-001/E28.9; SC-M01-007/E15.6; SC-M01-007/E15.7; SC-M01-007/E26.4; SC-M01-007/E26.5; SC-M01-007/E62.6; SC-M01-007/E62.7; SC-M01-007/E73.6; SC-M01-007/E73.7; SC-M01-007/E84.6; SC-M01-007/E84.7 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.05 | SC-M01-001/M8; SC-M01-001/E12.1; SC-M01-001/E12.2; SC-M01-001/E16.8; SC-M01-001/E21.10; SC-M01-001/E22.10; SC-M01-001/E23.8; SC-M01-001/E23.9; SC-M01-001/E23.10; SC-M01-001/E24.10; SC-M01-001/E25.10; SC-M01-001/E26.10; SC-M01-001/E27.8; SC-M01-001/E28.10; SC-M01-001/E29.8; SC-M01-001/E29.9; SC-M01-001/E29.10; SC-M01-001/E30.10; SC-M01-001/E31.10; SC-M01-001/E32.10; SC-M01-001/E34.10; SC-M01-001/E35.10; SC-M01-001/E36.10; SC-M01-001/E37.10; SC-M01-001/E38.8; SC-M01-001/E42.10; SC-M01-001/E43.10; SC-M01-001/E44.12; SC-M01-007/E6.6; SC-M01-007/E12.10; SC-M01-007/E13.10; SC-M01-007/E15.8; SC-M01-007/E16.6; SC-M01-007/E16.7; SC-M01-007/E16.8; SC-M01-007/E17.8; SC-M01-007/E18.8; SC-M01-007/E19.8; SC-M01-007/E20.4; SC-M01-007/E26.6; SC-M01-007/E27.4; SC-M01-007/E27.5; SC-M01-007/E27.6; SC-M01-007/E28.6; SC-M01-007/E29.6; SC-M01-007/E30.6; SC-M01-007/E57.6; SC-M01-007/E62.8; SC-M01-007/E63.6; SC-M01-007/E63.7; SC-M01-007/E63.8; SC-M01-007/E64.8; SC-M01-007/E65.8; SC-M01-007/E66.8; SC-M01-007/E68.6; SC-M01-007/E73.8; SC-M01-007/E74.6; SC-M01-007/E74.7; SC-M01-007/E74.8; SC-M01-007/E75.8; SC-M01-007/E76.8; SC-M01-007/E77.8; SC-M01-007/E79.6; SC-M01-007/E84.8; SC-M01-007/E85.6; SC-M01-007/E85.7; SC-M01-007/E85.8; SC-M01-007/E86.8; SC-M01-007/E87.8; SC-M01-007/E88.8; SC-M01-007/E106.5; RULE-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.06 | SC-M01-001/M8; SC-M01-001/E13.1; SC-M01-001/E13.2; SC-M01-001/E16.8; SC-M01-001/E21.10; SC-M01-001/E22.10; SC-M01-001/E23.10; SC-M01-001/E24.8; SC-M01-001/E24.9; SC-M01-001/E24.10; SC-M01-001/E25.10; SC-M01-001/E26.10; SC-M01-001/E27.8; SC-M01-001/E28.10; SC-M01-001/E29.10; SC-M01-001/E30.8; SC-M01-001/E30.9; SC-M01-001/E30.10; SC-M01-001/E31.10; SC-M01-001/E32.10; SC-M01-001/E34.10; SC-M01-001/E35.10; SC-M01-001/E36.10; SC-M01-001/E37.10; SC-M01-001/E38.8; SC-M01-001/E42.10; SC-M01-001/E43.10; SC-M01-001/E44.12; SC-M01-007/E6.6; SC-M01-007/E12.10; SC-M01-007/E13.10; SC-M01-007/E15.8; SC-M01-007/E16.8; SC-M01-007/E17.6; SC-M01-007/E17.7; SC-M01-007/E17.8; SC-M01-007/E18.8; SC-M01-007/E19.8; SC-M01-007/E20.4; SC-M01-007/E26.6; SC-M01-007/E27.6; SC-M01-007/E28.4; SC-M01-007/E28.5; SC-M01-007/E28.6; SC-M01-007/E29.6; SC-M01-007/E30.6; SC-M01-007/E57.6; SC-M01-007/E62.8; SC-M01-007/E63.8; SC-M01-007/E64.6; SC-M01-007/E64.7; SC-M01-007/E64.8; SC-M01-007/E65.8; SC-M01-007/E66.8; SC-M01-007/E68.6; SC-M01-007/E73.8; SC-M01-007/E74.8; SC-M01-007/E75.6; SC-M01-007/E75.7; SC-M01-007/E75.8; SC-M01-007/E76.8; SC-M01-007/E77.8; SC-M01-007/E79.6; SC-M01-007/E84.8; SC-M01-007/E85.8; SC-M01-007/E86.6; SC-M01-007/E86.7; SC-M01-007/E86.8; SC-M01-007/E87.8; SC-M01-007/E88.8; SC-M01-007/E106.5; RULE-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.07 | SC-M01-001/M8; SC-M01-001/E16.8; SC-M01-001/E21.10; SC-M01-001/E22.10; SC-M01-001/E23.10; SC-M01-001/E24.10; SC-M01-001/E25.10; SC-M01-001/E26.10; SC-M01-001/E27.8; SC-M01-001/E28.10; SC-M01-001/E29.10; SC-M01-001/E30.10; SC-M01-001/E31.10; SC-M01-001/E32.10; SC-M01-001/E34.10; SC-M01-001/E35.10; SC-M01-001/E36.10; SC-M01-001/E37.10; SC-M01-001/E38.8; SC-M01-001/E42.10; SC-M01-001/E43.10; SC-M01-001/E44.12; SC-M01-007/E6.6; SC-M01-007/E12.10; SC-M01-007/E13.10; SC-M01-007/E15.8; SC-M01-007/E16.8; SC-M01-007/E17.8; SC-M01-007/E18.8; SC-M01-007/E19.8; SC-M01-007/E20.4; SC-M01-007/E26.6; SC-M01-007/E27.6; SC-M01-007/E28.6; SC-M01-007/E29.6; SC-M01-007/E30.6; SC-M01-007/E57.6; SC-M01-007/E62.8; SC-M01-007/E63.8; SC-M01-007/E64.8; SC-M01-007/E65.8; SC-M01-007/E66.8; SC-M01-007/E68.6; SC-M01-007/E73.8; SC-M01-007/E74.8; SC-M01-007/E75.8; SC-M01-007/E76.8; SC-M01-007/E77.8; SC-M01-007/E79.6; SC-M01-007/E84.8; SC-M01-007/E85.8; SC-M01-007/E86.8; SC-M01-007/E87.8; SC-M01-007/E88.8; SC-M01-007/E106.5; RULE-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.08 | SC-M01-007/E106.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.09 | SC-M01-001/E33.8; SC-M01-007/E31.4; SC-M01-007/E67.6; SC-M01-007/E78.6; SC-M01-007/E89.6 | Một phần — có GAP nguồn |
| FR-M01-03.10 | SC-M01-001/M8; SC-M01-001/E16.8; SC-M01-001/E21.10; SC-M01-001/E22.10; SC-M01-001/E23.10; SC-M01-001/E24.10; SC-M01-001/E25.10; SC-M01-001/E26.10; SC-M01-001/E27.8; SC-M01-001/E28.10; SC-M01-001/E29.10; SC-M01-001/E30.10; SC-M01-001/E31.10; SC-M01-001/E32.10; SC-M01-001/E34.10; SC-M01-001/E35.10; SC-M01-001/E36.10; SC-M01-001/E37.10; SC-M01-001/E38.8; SC-M01-001/E42.10; SC-M01-001/E43.10; SC-M01-001/E44.12; SC-M01-007/E6.6; SC-M01-007/E12.10; SC-M01-007/E13.10; SC-M01-007/E15.8; SC-M01-007/E16.8; SC-M01-007/E17.8; SC-M01-007/E18.8; SC-M01-007/E19.8; SC-M01-007/E20.4; SC-M01-007/E26.6; SC-M01-007/E27.6; SC-M01-007/E28.6; SC-M01-007/E29.6; SC-M01-007/E30.6; SC-M01-007/E57.6; SC-M01-007/E62.8; SC-M01-007/E63.8; SC-M01-007/E64.8; SC-M01-007/E65.8; SC-M01-007/E66.8; SC-M01-007/E68.6; SC-M01-007/E73.8; SC-M01-007/E74.8; SC-M01-007/E75.8; SC-M01-007/E76.8; SC-M01-007/E77.8; SC-M01-007/E79.6; SC-M01-007/E84.8; SC-M01-007/E85.8; SC-M01-007/E86.8; SC-M01-007/E87.8; SC-M01-007/E88.8; SC-M01-007/E106.5; RULE-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.11 | SC-M01-001/M8; SC-M01-001/E16.8; SC-M01-001/E21.10; SC-M01-001/E22.10; SC-M01-001/E23.10; SC-M01-001/E24.10; SC-M01-001/E25.10; SC-M01-001/E26.10; SC-M01-001/E27.8; SC-M01-001/E28.10; SC-M01-001/E29.10; SC-M01-001/E30.10; SC-M01-001/E31.10; SC-M01-001/E32.10; SC-M01-001/E34.10; SC-M01-001/E35.10; SC-M01-001/E36.10; SC-M01-001/E37.10; SC-M01-001/E38.8; SC-M01-001/E42.10; SC-M01-001/E43.10; SC-M01-001/E44.12; SC-M01-007/E6.6; SC-M01-007/E12.10; SC-M01-007/E13.10; SC-M01-007/E15.8; SC-M01-007/E16.8; SC-M01-007/E17.8; SC-M01-007/E18.8; SC-M01-007/E19.8; SC-M01-007/E20.4; SC-M01-007/E26.6; SC-M01-007/E27.6; SC-M01-007/E28.6; SC-M01-007/E29.6; SC-M01-007/E30.6; SC-M01-007/E57.6; SC-M01-007/E62.8; SC-M01-007/E63.8; SC-M01-007/E64.8; SC-M01-007/E65.8; SC-M01-007/E66.8; SC-M01-007/E68.6; SC-M01-007/E73.8; SC-M01-007/E74.8; SC-M01-007/E75.8; SC-M01-007/E76.8; SC-M01-007/E77.8; SC-M01-007/E79.6; SC-M01-007/E84.8; SC-M01-007/E85.8; SC-M01-007/E86.8; SC-M01-007/E87.8; SC-M01-007/E88.8; SC-M01-007/E106.5; RULE-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.12 | SC-M01-001/M8; SC-M01-001/E14.1; SC-M01-001/E14.2; SC-M01-001/E16.8; SC-M01-001/E21.10; SC-M01-001/E22.10; SC-M01-001/E23.10; SC-M01-001/E24.10; SC-M01-001/E25.8; SC-M01-001/E25.9; SC-M01-001/E25.10; SC-M01-001/E26.10; SC-M01-001/E27.8; SC-M01-001/E28.10; SC-M01-001/E29.10; SC-M01-001/E30.10; SC-M01-001/E31.8; SC-M01-001/E31.9; SC-M01-001/E31.10; SC-M01-001/E32.10; SC-M01-001/E34.10; SC-M01-001/E35.10; SC-M01-001/E36.10; SC-M01-001/E37.10; SC-M01-001/E38.8; SC-M01-001/E42.10; SC-M01-001/E43.10; SC-M01-001/E44.12; SC-M01-007/E6.6; SC-M01-007/E12.10; SC-M01-007/E13.10; SC-M01-007/E15.8; SC-M01-007/E16.8; SC-M01-007/E17.8; SC-M01-007/E18.6; SC-M01-007/E18.7; SC-M01-007/E18.8; SC-M01-007/E19.8; SC-M01-007/E20.4; SC-M01-007/E26.6; SC-M01-007/E27.6; SC-M01-007/E28.6; SC-M01-007/E29.4; SC-M01-007/E29.5; SC-M01-007/E29.6; SC-M01-007/E30.6; SC-M01-007/E57.6; SC-M01-007/E62.8; SC-M01-007/E63.8; SC-M01-007/E64.8; SC-M01-007/E65.6; SC-M01-007/E65.7; SC-M01-007/E65.8; SC-M01-007/E66.8; SC-M01-007/E68.6; SC-M01-007/E73.8; SC-M01-007/E74.8; SC-M01-007/E75.8; SC-M01-007/E76.6; SC-M01-007/E76.7; SC-M01-007/E76.8; SC-M01-007/E77.8; SC-M01-007/E79.6; SC-M01-007/E84.8; SC-M01-007/E85.8; SC-M01-007/E86.8; SC-M01-007/E87.6; SC-M01-007/E87.7; SC-M01-007/E87.8; SC-M01-007/E88.8; SC-M01-007/E106.5; RULE-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.13 | SC-M01-001/M8; SC-M01-001/E14.1; SC-M01-001/E14.2; SC-M01-001/E16.8; SC-M01-001/E21.10; SC-M01-001/E22.10; SC-M01-001/E23.10; SC-M01-001/E24.10; SC-M01-001/E25.8; SC-M01-001/E25.9; SC-M01-001/E25.10; SC-M01-001/E26.10; SC-M01-001/E27.8; SC-M01-001/E28.10; SC-M01-001/E29.10; SC-M01-001/E30.10; SC-M01-001/E31.8; SC-M01-001/E31.9; SC-M01-001/E31.10; SC-M01-001/E32.10; SC-M01-001/E34.10; SC-M01-001/E35.10; SC-M01-001/E36.10; SC-M01-001/E37.10; SC-M01-001/E38.8; SC-M01-001/E42.10; SC-M01-001/E43.10; SC-M01-001/E44.12; SC-M01-007/E6.6; SC-M01-007/E12.10; SC-M01-007/E13.10; SC-M01-007/E15.8; SC-M01-007/E16.8; SC-M01-007/E17.8; SC-M01-007/E18.6; SC-M01-007/E18.7; SC-M01-007/E18.8; SC-M01-007/E19.8; SC-M01-007/E20.4; SC-M01-007/E26.6; SC-M01-007/E27.6; SC-M01-007/E28.6; SC-M01-007/E29.4; SC-M01-007/E29.5; SC-M01-007/E29.6; SC-M01-007/E30.6; SC-M01-007/E57.6; SC-M01-007/E62.8; SC-M01-007/E63.8; SC-M01-007/E64.8; SC-M01-007/E65.6; SC-M01-007/E65.7; SC-M01-007/E65.8; SC-M01-007/E66.8; SC-M01-007/E68.6; SC-M01-007/E73.8; SC-M01-007/E74.8; SC-M01-007/E75.8; SC-M01-007/E76.6; SC-M01-007/E76.7; SC-M01-007/E76.8; SC-M01-007/E77.8; SC-M01-007/E79.6; SC-M01-007/E84.8; SC-M01-007/E85.8; SC-M01-007/E86.8; SC-M01-007/E87.6; SC-M01-007/E87.7; SC-M01-007/E87.8; SC-M01-007/E88.8; SC-M01-007/E106.5; RULE-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.14 | SC-M01-001/M8; SC-M01-001/E15.1; SC-M01-001/E15.2; SC-M01-001/E16.8; SC-M01-001/E21.10; SC-M01-001/E22.10; SC-M01-001/E23.10; SC-M01-001/E24.10; SC-M01-001/E25.10; SC-M01-001/E26.8; SC-M01-001/E26.9; SC-M01-001/E26.10; SC-M01-001/E27.8; SC-M01-001/E28.10; SC-M01-001/E29.10; SC-M01-001/E30.10; SC-M01-001/E31.10; SC-M01-001/E32.8; SC-M01-001/E32.9; SC-M01-001/E32.10; SC-M01-001/E34.10; SC-M01-001/E35.10; SC-M01-001/E36.10; SC-M01-001/E37.10; SC-M01-001/E38.8; SC-M01-001/E42.10; SC-M01-001/E43.10; SC-M01-001/E44.12; SC-M01-007/E6.6; SC-M01-007/E12.10; SC-M01-007/E13.10; SC-M01-007/E15.8; SC-M01-007/E16.8; SC-M01-007/E17.8; SC-M01-007/E18.8; SC-M01-007/E19.6; SC-M01-007/E19.7; SC-M01-007/E19.8; SC-M01-007/E20.4; SC-M01-007/E26.6; SC-M01-007/E27.6; SC-M01-007/E28.6; SC-M01-007/E29.6; SC-M01-007/E30.4; SC-M01-007/E30.5; SC-M01-007/E30.6; SC-M01-007/E57.6; SC-M01-007/E62.8; SC-M01-007/E63.8; SC-M01-007/E64.8; SC-M01-007/E65.8; SC-M01-007/E66.6; SC-M01-007/E66.7; SC-M01-007/E66.8; SC-M01-007/E68.6; SC-M01-007/E73.8; SC-M01-007/E74.8; SC-M01-007/E75.8; SC-M01-007/E76.8; SC-M01-007/E77.6; SC-M01-007/E77.7; SC-M01-007/E77.8; SC-M01-007/E79.6; SC-M01-007/E84.8; SC-M01-007/E85.8; SC-M01-007/E86.8; SC-M01-007/E87.8; SC-M01-007/E88.6; SC-M01-007/E88.7; SC-M01-007/E88.8; SC-M01-007/E106.5; RULE-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.15 | RULE-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-03.16 | RULE-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-04.01 | SC-M01-001/E16.1; SC-M01-001/E16.2; SC-M01-001/E16.3; SC-M01-001/E16.6; SC-M01-001/E17.1; SC-M01-001/E17.2; SC-M01-001/E17.3; SC-M01-001/E18.1; SC-M01-001/E18.2; SC-M01-001/E18.3; SC-M01-001/E19.1; SC-M01-001/E19.2; SC-M01-001/E19.3; SC-M01-001/E20.1; SC-M01-001/E20.2; SC-M01-001/E20.3; SC-M01-001/E21.1; SC-M01-001/E21.2; SC-M01-001/E21.3; SC-M01-001/E21.8; SC-M01-001/E22.1; SC-M01-001/E22.2; SC-M01-001/E22.3; SC-M01-001/E22.6; SC-M01-001/E23.1; SC-M01-001/E23.2; SC-M01-001/E23.3; SC-M01-001/E23.6; SC-M01-001/E24.1; SC-M01-001/E24.2; SC-M01-001/E24.3; SC-M01-001/E24.6; SC-M01-001/E25.1; SC-M01-001/E25.2; SC-M01-001/E25.3; SC-M01-001/E25.6; SC-M01-001/E26.1; SC-M01-001/E26.2; SC-M01-001/E26.3; SC-M01-001/E26.6; SC-M01-007/E56.4; SC-M01-007/E61.4; SC-M01-007/E72.4; SC-M01-007/E83.4; SC-M01-007/E94.4; SC-M01-007/E99.4; SC-M01-007/E105.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-04.02 | SC-M01-001/E16.6; SC-M01-001/E16.7; SC-M01-001/E21.8; SC-M01-001/E21.9; SC-M01-001/E22.6; SC-M01-001/E22.7; SC-M01-001/E23.6; SC-M01-001/E23.7; SC-M01-001/E24.6; SC-M01-001/E24.7; SC-M01-001/E25.6; SC-M01-001/E25.7; SC-M01-001/E26.6; SC-M01-001/E26.7 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-04.03 | SC-M01-001/E16.6; SC-M01-001/E16.7; SC-M01-001/E21.8; SC-M01-001/E21.9; SC-M01-001/E22.6; SC-M01-001/E22.7; SC-M01-001/E23.6; SC-M01-001/E23.7; SC-M01-001/E24.6; SC-M01-001/E24.7; SC-M01-001/E25.6; SC-M01-001/E25.7; SC-M01-001/E26.6; SC-M01-001/E26.7 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-04.04 | SC-M01-001/E20.4; SC-M01-007/E52.3; SC-M01-007/E53.3; SC-M01-007/E54.3; SC-M01-007/E55.3; SC-M01-007/E56.3; SC-M01-007/E57.3; SC-M01-007/E58.3; SC-M01-007/E59.3; SC-M01-007/E60.3; SC-M01-007/E61.3; SC-M01-007/E62.3; SC-M01-007/E63.3; SC-M01-007/E64.3; SC-M01-007/E65.3; SC-M01-007/E66.3; SC-M01-007/E67.3; SC-M01-007/E68.3; SC-M01-007/E68.4; SC-M01-007/E69.3; SC-M01-007/E70.3; SC-M01-007/E71.3; SC-M01-007/E72.3; SC-M01-007/E73.3; SC-M01-007/E73.4; SC-M01-007/E74.3; SC-M01-007/E74.4; SC-M01-007/E75.3; SC-M01-007/E75.4; SC-M01-007/E76.3; SC-M01-007/E76.4; SC-M01-007/E77.3; SC-M01-007/E77.4; SC-M01-007/E78.3; SC-M01-007/E78.4; SC-M01-007/E79.3; SC-M01-007/E79.4; SC-M01-007/E80.3; SC-M01-007/E81.3; SC-M01-007/E82.3; SC-M01-007/E83.3; SC-M01-007/E84.3; SC-M01-007/E84.4; SC-M01-007/E85.3; SC-M01-007/E85.4; SC-M01-007/E86.3; SC-M01-007/E86.4; SC-M01-007/E87.3; SC-M01-007/E87.4; SC-M01-007/E88.3; SC-M01-007/E88.4; SC-M01-007/E89.3; SC-M01-007/E89.4; SC-M01-007/E90.3; SC-M01-007/E90.4; SC-M01-007/E91.3; SC-M01-007/E92.3; SC-M01-007/E93.3; SC-M01-007/E94.3; SC-M01-007/E95.3; SC-M01-007/E96.3; SC-M01-007/E97.3; SC-M01-007/E98.3; SC-M01-007/E99.3; SC-M01-007/E100.3; SC-M01-007/E101.3; SC-M01-007/E102.3; SC-M01-007/E103.3; SC-M01-007/E104.3; SC-M01-007/E105.3 | Một phần — có GAP nguồn |
| FR-M01-04.05 | SC-M01-007/E68.4; SC-M01-007/E73.4; SC-M01-007/E74.4; SC-M01-007/E75.4; SC-M01-007/E76.4; SC-M01-007/E77.4; SC-M01-007/E78.4; SC-M01-007/E79.4; SC-M01-007/E84.4; SC-M01-007/E85.4; SC-M01-007/E86.4; SC-M01-007/E87.4; SC-M01-007/E88.4; SC-M01-007/E89.4; SC-M01-007/E90.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-04.06 | SC-M01-001/E20.4; SC-M01-007/E52.1; SC-M01-007/E52.2; SC-M01-007/E52.3; SC-M01-007/E52.4; SC-M01-007/E53.1; SC-M01-007/E53.2; SC-M01-007/E53.3; SC-M01-007/E53.4; SC-M01-007/E54.1; SC-M01-007/E54.2; SC-M01-007/E54.3; SC-M01-007/E54.4; SC-M01-007/E55.1; SC-M01-007/E55.2; SC-M01-007/E55.3; SC-M01-007/E55.4; SC-M01-007/E56.1; SC-M01-007/E56.2; SC-M01-007/E56.3; SC-M01-007/E57.1; SC-M01-007/E57.2; SC-M01-007/E57.3; SC-M01-007/E57.4; SC-M01-007/E58.1; SC-M01-007/E58.2; SC-M01-007/E58.3; SC-M01-007/E58.4; SC-M01-007/E59.1; SC-M01-007/E59.2; SC-M01-007/E59.3; SC-M01-007/E59.4; SC-M01-007/E60.1; SC-M01-007/E60.2; SC-M01-007/E60.3; SC-M01-007/E60.4; SC-M01-007/E61.1; SC-M01-007/E61.2; SC-M01-007/E61.3; SC-M01-007/E62.1; SC-M01-007/E62.2; SC-M01-007/E62.3; SC-M01-007/E62.4; SC-M01-007/E63.1; SC-M01-007/E63.2; SC-M01-007/E63.3; SC-M01-007/E63.4; SC-M01-007/E64.1; SC-M01-007/E64.2; SC-M01-007/E64.3; SC-M01-007/E64.4; SC-M01-007/E65.1; SC-M01-007/E65.2; SC-M01-007/E65.3; SC-M01-007/E65.4; SC-M01-007/E66.1; SC-M01-007/E66.2; SC-M01-007/E66.3; SC-M01-007/E66.4; SC-M01-007/E67.1; SC-M01-007/E67.2; SC-M01-007/E67.3; SC-M01-007/E67.4; SC-M01-007/E68.1; SC-M01-007/E68.2; SC-M01-007/E68.3; SC-M01-007/E68.4; SC-M01-007/E69.1; SC-M01-007/E69.2; SC-M01-007/E69.3; SC-M01-007/E69.4; SC-M01-007/E70.1; SC-M01-007/E70.2; SC-M01-007/E70.3; SC-M01-007/E70.4; SC-M01-007/E71.1; SC-M01-007/E71.2; SC-M01-007/E71.3; SC-M01-007/E71.4; SC-M01-007/E72.1; SC-M01-007/E72.2; SC-M01-007/E72.3; SC-M01-007/E73.1; SC-M01-007/E73.2; SC-M01-007/E73.3; SC-M01-007/E73.4; SC-M01-007/E74.1; SC-M01-007/E74.2; SC-M01-007/E74.3; SC-M01-007/E74.4; SC-M01-007/E75.1; SC-M01-007/E75.2; SC-M01-007/E75.3; SC-M01-007/E75.4; SC-M01-007/E76.1; SC-M01-007/E76.2; SC-M01-007/E76.3; SC-M01-007/E76.4; SC-M01-007/E77.1; SC-M01-007/E77.2; SC-M01-007/E77.3; SC-M01-007/E77.4; SC-M01-007/E78.1; SC-M01-007/E78.2; SC-M01-007/E78.3; SC-M01-007/E78.4; SC-M01-007/E79.1; SC-M01-007/E79.2; SC-M01-007/E79.3; SC-M01-007/E79.4; SC-M01-007/E80.1; SC-M01-007/E80.2; SC-M01-007/E80.3; SC-M01-007/E80.4; SC-M01-007/E81.1; SC-M01-007/E81.2; SC-M01-007/E81.3; SC-M01-007/E81.4; SC-M01-007/E82.1; SC-M01-007/E82.2; SC-M01-007/E82.3; SC-M01-007/E82.4; SC-M01-007/E83.1; SC-M01-007/E83.2; SC-M01-007/E83.3; SC-M01-007/E84.1; SC-M01-007/E84.2; SC-M01-007/E84.3; SC-M01-007/E84.4; SC-M01-007/E85.1; SC-M01-007/E85.2; SC-M01-007/E85.3; SC-M01-007/E85.4; SC-M01-007/E86.1; SC-M01-007/E86.2; SC-M01-007/E86.3; SC-M01-007/E86.4; SC-M01-007/E87.1; SC-M01-007/E87.2; SC-M01-007/E87.3; SC-M01-007/E87.4; SC-M01-007/E88.1; SC-M01-007/E88.2; SC-M01-007/E88.3; SC-M01-007/E88.4; SC-M01-007/E89.1; SC-M01-007/E89.2; SC-M01-007/E89.3; SC-M01-007/E89.4; SC-M01-007/E90.1; SC-M01-007/E90.2; SC-M01-007/E90.3; SC-M01-007/E90.4; SC-M01-007/E91.1; SC-M01-007/E91.2; SC-M01-007/E91.3; SC-M01-007/E91.4; SC-M01-007/E92.1; SC-M01-007/E92.2; SC-M01-007/E92.3; SC-M01-007/E92.4; SC-M01-007/E93.1; SC-M01-007/E93.2; SC-M01-007/E93.3; SC-M01-007/E93.4; SC-M01-007/E94.1; SC-M01-007/E94.2; SC-M01-007/E94.3; SC-M01-007/E95.1; SC-M01-007/E95.2; SC-M01-007/E95.3; SC-M01-007/E95.4; SC-M01-007/E96.1; SC-M01-007/E96.2; SC-M01-007/E96.3; SC-M01-007/E96.4; SC-M01-007/E97.1; SC-M01-007/E97.2; SC-M01-007/E97.3; SC-M01-007/E97.4; SC-M01-007/E98.1; SC-M01-007/E98.2; SC-M01-007/E98.3; SC-M01-007/E98.4; SC-M01-007/E99.1; SC-M01-007/E99.2; SC-M01-007/E99.3; SC-M01-007/E100.1; SC-M01-007/E100.2; SC-M01-007/E100.3; SC-M01-007/E100.4; SC-M01-007/E101.1; SC-M01-007/E101.2; SC-M01-007/E101.3; SC-M01-007/E101.4; SC-M01-007/E102.1; SC-M01-007/E102.2; SC-M01-007/E102.3; SC-M01-007/E102.4; SC-M01-007/E103.1; SC-M01-007/E103.2; SC-M01-007/E103.3; SC-M01-007/E103.4; SC-M01-007/E104.1; SC-M01-007/E104.2; SC-M01-007/E104.3; SC-M01-007/E104.4; SC-M01-007/E105.1; SC-M01-007/E105.2; SC-M01-007/E105.3 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-04.07 | SC-M01-001/E16.4; SC-M01-001/E17.4; SC-M01-001/E17.6; SC-M01-001/E18.4; SC-M01-001/E19.4; SC-M01-001/E21.4; SC-M01-001/E22.4; SC-M01-001/E23.4; SC-M01-001/E24.4; SC-M01-001/E25.4; SC-M01-001/E26.4; SC-M01-007/E56.4; SC-M01-007/E61.4; SC-M01-007/E72.4; SC-M01-007/E83.4; SC-M01-007/E94.4; SC-M01-007/E99.4; SC-M01-007/E105.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-04.08 | SC-M01-007/E52.4; SC-M01-007/E57.4; SC-M01-007/E62.4; SC-M01-007/E63.4; SC-M01-007/E64.4; SC-M01-007/E65.4; SC-M01-007/E66.4; SC-M01-007/E67.4; SC-M01-007/E68.4; SC-M01-007/E73.4; SC-M01-007/E74.4; SC-M01-007/E75.4; SC-M01-007/E76.4; SC-M01-007/E77.4; SC-M01-007/E78.4; SC-M01-007/E79.4; SC-M01-007/E84.4; SC-M01-007/E85.4; SC-M01-007/E86.4; SC-M01-007/E87.4; SC-M01-007/E88.4; SC-M01-007/E89.4; SC-M01-007/E90.4; SC-M01-007/E95.4; SC-M01-007/E100.4; SC-M01-007/E101.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-04.09 | SC-M01-007/E57.4; SC-M01-007/E62.4; SC-M01-007/E63.4; SC-M01-007/E64.4; SC-M01-007/E65.4; SC-M01-007/E66.4; SC-M01-007/E67.4; SC-M01-007/E68.4; SC-M01-007/E73.4; SC-M01-007/E74.4; SC-M01-007/E75.4; SC-M01-007/E76.4; SC-M01-007/E77.4; SC-M01-007/E78.4; SC-M01-007/E79.4; SC-M01-007/E84.4; SC-M01-007/E85.4; SC-M01-007/E86.4; SC-M01-007/E87.4; SC-M01-007/E88.4; SC-M01-007/E89.4; SC-M01-007/E90.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-04.10 | SC-M01-001/E16.6; SC-M01-001/E18.6; SC-M01-001/E21.8; SC-M01-001/E22.6; SC-M01-001/E23.6; SC-M01-001/E24.6; SC-M01-001/E25.6; SC-M01-001/E26.6; SC-M01-007/E56.4; SC-M01-007/E61.4; SC-M01-007/E72.4; SC-M01-007/E83.4; SC-M01-007/E94.4; SC-M01-007/E99.4; SC-M01-007/E105.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-04.11 | SC-M01-001/E18.6; SC-M01-007/E68.4; SC-M01-007/E73.4; SC-M01-007/E74.4; SC-M01-007/E75.4; SC-M01-007/E76.4; SC-M01-007/E77.4; SC-M01-007/E78.4; SC-M01-007/E79.4; SC-M01-007/E84.4; SC-M01-007/E85.4; SC-M01-007/E86.4; SC-M01-007/E87.4; SC-M01-007/E88.4; SC-M01-007/E89.4; SC-M01-007/E90.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-04.12 | SC-M01-001/E16.4; SC-M01-001/E16.5; SC-M01-001/E17.4; SC-M01-001/E17.5; SC-M01-001/E17.6; SC-M01-001/E18.4; SC-M01-001/E18.5; SC-M01-001/E19.4; SC-M01-001/E19.5; SC-M01-001/E21.4; SC-M01-001/E21.5; SC-M01-001/E21.7; SC-M01-001/E22.4; SC-M01-001/E22.5; SC-M01-001/E23.4; SC-M01-001/E23.5; SC-M01-001/E24.4; SC-M01-001/E24.5; SC-M01-001/E25.4; SC-M01-001/E25.5; SC-M01-001/E26.4; SC-M01-001/E26.5; SC-M01-007/E56.4; SC-M01-007/E61.4; SC-M01-007/E72.4; SC-M01-007/E83.4; SC-M01-007/E94.4; SC-M01-007/E99.4; SC-M01-007/E105.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-04.13 | SC-M01-001/E16.5; SC-M01-001/E16.6; SC-M01-001/E17.5; SC-M01-001/E18.5; SC-M01-001/E19.5; SC-M01-001/E21.7; SC-M01-001/E21.8; SC-M01-001/E22.5; SC-M01-001/E22.6; SC-M01-001/E23.5; SC-M01-001/E23.6; SC-M01-001/E24.5; SC-M01-001/E24.6; SC-M01-001/E25.5; SC-M01-001/E25.6; SC-M01-001/E26.5; SC-M01-001/E26.6; SC-M01-007/E56.4; SC-M01-007/E61.4; SC-M01-007/E72.4; SC-M01-007/E83.4; SC-M01-007/E94.4; SC-M01-007/E99.4; SC-M01-007/E105.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.01 | SC-M01-007/M1; SC-M01-007/M2; SC-M01-007/E3.1; SC-M01-007/E6.1; SC-M01-007/E6.2; SC-M01-007/E7.1; SC-M01-007/E8.1; SC-M01-007/E9.1; SC-M01-007/E9.2; SC-M01-007/E10.1; SC-M01-007/E11.1; SC-M01-007/E12.1; SC-M01-007/E12.2; SC-M01-007/E13.1; SC-M01-007/E13.2; SC-M01-007/E14.1; SC-M01-007/E14.2; SC-M01-007/E15.1; SC-M01-007/E15.2; SC-M01-007/E16.1; SC-M01-007/E16.2; SC-M01-007/E17.1; SC-M01-007/E17.2; SC-M01-007/E18.1; SC-M01-007/E18.2; SC-M01-007/E19.1; SC-M01-007/E19.2; SC-M01-007/E20.1; SC-M01-007/E20.2; SC-M01-007/E21.1; SC-M01-007/E22.1; SC-M01-007/E23.1; SC-M01-007/E23.2; SC-M01-007/E24.1; SC-M01-007/E25.1; SC-M01-007/E26.1; SC-M01-007/E26.2; SC-M01-007/E27.1; SC-M01-007/E27.2; SC-M01-007/E28.1; SC-M01-007/E28.2; SC-M01-007/E29.1; SC-M01-007/E29.2; SC-M01-007/E30.1; SC-M01-007/E30.2; SC-M01-007/E31.1; SC-M01-007/E31.2; SC-M01-007/E32.1; SC-M01-007/E32.2; SC-M01-007/E33.1; SC-M01-007/E34.1; SC-M01-007/E35.1; SC-M01-007/E35.2; SC-M01-007/E36.1; SC-M01-007/E37.1; SC-M01-007/E38.1; SC-M01-007/E38.2; SC-M01-007/E39.1; SC-M01-007/E40.1; SC-M01-007/E41.1; SC-M01-007/E41.2; SC-M01-007/E42.1; SC-M01-007/E43.1; SC-M01-007/E44.1; SC-M01-007/E44.2; SC-M01-007/E45.1; SC-M01-007/E46.1; SC-M01-007/E47.1; SC-M01-007/E47.2; SC-M01-007/E48.1; SC-M01-007/E49.1; SC-M01-007/E50.1; SC-M01-007/E51.1; SC-M01-007/E52.4; SC-M01-007/E57.4; SC-M01-007/E62.4; SC-M01-007/E63.4; SC-M01-007/E64.4; SC-M01-007/E65.4; SC-M01-007/E66.4; SC-M01-007/E67.4; SC-M01-007/E68.4; SC-M01-007/E73.4; SC-M01-007/E74.4; SC-M01-007/E75.4; SC-M01-007/E76.4; SC-M01-007/E77.4; SC-M01-007/E78.4; SC-M01-007/E79.4; SC-M01-007/E84.4; SC-M01-007/E85.4; SC-M01-007/E86.4; SC-M01-007/E87.4; SC-M01-007/E88.4; SC-M01-007/E89.4; SC-M01-007/E90.4; SC-M01-007/E101.4; SC-M01-007/E107.1; SC-M01-007/E107.2; SC-M01-007/E108.1; SC-M01-007/E108.2; SC-M01-007/E109.1; SC-M01-007/E109.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.02 | SC-M01-007/M1; SC-M01-007/E1.1; SC-M01-007/E6.1; SC-M01-007/E7.1; SC-M01-007/E7.2; SC-M01-007/E8.1; SC-M01-007/E9.1; SC-M01-007/E10.1; SC-M01-007/E11.1; SC-M01-007/E12.1; SC-M01-007/E13.1; SC-M01-007/E14.1; SC-M01-007/E15.1; SC-M01-007/E16.1; SC-M01-007/E17.1; SC-M01-007/E18.1; SC-M01-007/E19.1; SC-M01-007/E20.1; SC-M01-007/E21.1; SC-M01-007/E21.2; SC-M01-007/E22.1; SC-M01-007/E23.1; SC-M01-007/E24.1; SC-M01-007/E25.1; SC-M01-007/E26.1; SC-M01-007/E27.1; SC-M01-007/E28.1; SC-M01-007/E29.1; SC-M01-007/E30.1; SC-M01-007/E31.1; SC-M01-007/E32.1; SC-M01-007/E33.1; SC-M01-007/E33.2; SC-M01-007/E34.1; SC-M01-007/E35.1; SC-M01-007/E36.1; SC-M01-007/E37.1; SC-M01-007/E38.1; SC-M01-007/E39.1; SC-M01-007/E39.2; SC-M01-007/E40.1; SC-M01-007/E41.1; SC-M01-007/E42.1; SC-M01-007/E43.1; SC-M01-007/E44.1; SC-M01-007/E45.1; SC-M01-007/E45.2; SC-M01-007/E46.1; SC-M01-007/E47.1; SC-M01-007/E48.1; SC-M01-007/E49.1; SC-M01-007/E107.1; SC-M01-007/E108.1; SC-M01-007/E109.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.03 | SC-M01-007/E4.1; SC-M01-007/E10.2; SC-M01-007/E24.2; SC-M01-007/E36.2; SC-M01-007/E42.2; SC-M01-007/E48.2; SC-M01-007/E54.4; SC-M01-007/E59.4; SC-M01-007/E70.4; SC-M01-007/E81.4; SC-M01-007/E92.4; SC-M01-007/E97.4; SC-M01-007/E103.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.04 | SC-M01-007/E3.1; SC-M01-007/E9.2; SC-M01-007/E23.2; SC-M01-007/E35.2; SC-M01-007/E41.2; SC-M01-007/E47.2; SC-M01-007/E53.4; SC-M01-007/E58.4; SC-M01-007/E69.4; SC-M01-007/E80.4; SC-M01-007/E91.4; SC-M01-007/E96.4; SC-M01-007/E102.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.05 | SC-M01-007/E32.2; SC-M01-007/E38.2; SC-M01-007/E50.2; SC-M01-007/E51.2; SC-M01-007/E95.4; SC-M01-007/E100.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.06 | SC-M01-007/E32.2; SC-M01-007/E38.2; SC-M01-007/E50.2; SC-M01-007/E50.4; SC-M01-007/E51.2; SC-M01-007/E95.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.07 | SC-M01-007/E32.2; SC-M01-007/E32.3; SC-M01-007/E32.4; SC-M01-007/E38.2; SC-M01-007/E38.3; SC-M01-007/E38.4; SC-M01-007/E50.2; SC-M01-007/E51.2; SC-M01-007/E95.4; SC-M01-007/E95.5; SC-M01-007/E95.6; SC-M01-007/E100.4; SC-M01-014/E1.1; SC-M01-014/E1.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.08 | SC-M01-007/E32.2; SC-M01-007/E50.2; SC-M01-007/E50.3; SC-M01-007/E50.4; SC-M01-007/E51.2; SC-M01-007/E95.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.09 | SC-M01-007/E38.2; SC-M01-007/E100.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.10 | SC-M01-007/E6.2; SC-M01-007/E12.2; SC-M01-007/E13.2; SC-M01-007/E14.2; SC-M01-007/E15.2; SC-M01-007/E16.2; SC-M01-007/E17.2; SC-M01-007/E18.2; SC-M01-007/E19.2 | Một phần — có GAP nguồn |
| FR-M01-05.11 | SC-M01-007/E20.2; SC-M01-007/E26.2; SC-M01-007/E27.2; SC-M01-007/E28.2; SC-M01-007/E29.2; SC-M01-007/E30.2; SC-M01-007/E31.2; SC-M01-007/E57.4; SC-M01-007/E62.4; SC-M01-007/E63.4; SC-M01-007/E64.4; SC-M01-007/E65.4; SC-M01-007/E66.4; SC-M01-007/E67.4; SC-M01-007/E68.4; SC-M01-007/E73.4; SC-M01-007/E74.4; SC-M01-007/E75.4; SC-M01-007/E76.4; SC-M01-007/E77.4; SC-M01-007/E78.4; SC-M01-007/E79.4; SC-M01-007/E84.4; SC-M01-007/E85.4; SC-M01-007/E86.4; SC-M01-007/E87.4; SC-M01-007/E88.4; SC-M01-007/E89.4 | Một phần — có GAP nguồn |
| FR-M01-05.12 | SC-M01-007/M2; SC-M01-007/E44.2; SC-M01-007/E52.4; SC-M01-007/E90.4; SC-M01-007/E101.4; SC-M01-007/E107.2; SC-M01-007/E108.2; SC-M01-007/E109.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.13 | SC-M01-007/E2.1; SC-M01-007/E8.2; SC-M01-007/E22.2; SC-M01-007/E34.2; SC-M01-007/E40.2; SC-M01-007/E46.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.14 | RULE-M01-004 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.15 | RULE-M01-004 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.16 | RULE-M01-004 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.17 | AUT-M01-004 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.18 | SC-M01-007/E32.3; SC-M01-007/E32.4; SC-M01-007/E38.3; SC-M01-007/E38.4; SC-M01-007/E51.3; SC-M01-007/E51.4; SC-M01-007/E95.5; SC-M01-007/E95.6; SC-M01-014/E1.1; SC-M01-014/E1.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-05.19 | SC-M01-007/E5.1; SC-M01-007/E11.2; SC-M01-007/E25.2; SC-M01-007/E37.2; SC-M01-007/E43.2; SC-M01-007/E44.2; SC-M01-007/E49.2; SC-M01-007/E52.4; SC-M01-007/E55.4; SC-M01-007/E60.4; SC-M01-007/E71.4; SC-M01-007/E82.4; SC-M01-007/E90.4; SC-M01-007/E93.4; SC-M01-007/E98.4; SC-M01-007/E101.4; SC-M01-007/E104.4 | Một phần — có GAP nguồn |
| FR-M01-05.20 | SC-M01-017/E8.1; SC-M01-022/E4.1; AUT-M01-001; RULE-M01-005 | Một phần — có GAP nguồn |
| FR-M01-06.01 | AUT-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-06.02 | AUT-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-06.03 | AUT-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-06.04 | AUT-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-06.05 | AUT-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-06.06 | AUT-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-06.07 | AUT-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-07.01 | SC-M01-007/E32.3; SC-M01-007/E32.4; SC-M01-007/E38.3; SC-M01-007/E38.4; SC-M01-007/E51.4; SC-M01-007/E95.5; SC-M01-007/E95.6; SC-M01-007/E108.6; SC-M01-014/M1; SC-M01-014/M2; SC-M01-014/E1.1; SC-M01-014/E1.2; SC-M01-014/E2.1; SC-M01-014/E2.2; SC-M01-039/E1.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-07.02 | SC-M01-007/E32.3; SC-M01-007/E32.4; SC-M01-007/E38.3; SC-M01-007/E38.4; SC-M01-007/E51.4; SC-M01-007/E95.5; SC-M01-007/E95.6; SC-M01-007/E108.6; SC-M01-014/M1; SC-M01-014/M2; SC-M01-014/E1.1; SC-M01-014/E1.2; SC-M01-014/E2.1; SC-M01-014/E2.2; SC-M01-039/E1.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-08.01 | SC-M01-017/M1; SC-M01-017/M2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-08.02 | SC-M01-017/E1.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-08.03 | SC-M01-017/E2.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-08.04 | SC-M01-017/M2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-08.05 | SC-M01-017/M2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-08.06 | SC-M01-017/E6.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-08.07 | SC-M01-017/E5.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-08.08 | SC-M01-017/E3.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-08.09 | SC-M01-017/E4.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-08.10 | SC-M01-017/E7.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09.01 | SC-M01-018/M1; SC-M01-018/M2; SC-M01-018/E10.1; SC-M01-018/E10.2; SC-M01-018/E11.1; SC-M01-018/E11.2; SC-M01-018/E12.1; SC-M01-018/E12.2; SC-M01-018/E13.1; SC-M01-018/E13.2; SC-M01-018/E14.1; SC-M01-018/E14.2; SC-M01-018/E15.1; SC-M01-018/E15.2; SC-M01-018/E16.1; SC-M01-018/E16.2; SC-M01-018/E17.1; SC-M01-018/E18.1; SC-M01-018/E19.1 | Một phần — có GAP nguồn |
| FR-M01-09.02 | SC-M01-018/M3; SC-M01-018/M4; SC-M01-018/E10.3; SC-M01-018/E10.4; SC-M01-018/E11.3; SC-M01-018/E12.3; SC-M01-018/E13.3; SC-M01-018/E14.3; SC-M01-018/E15.3; SC-M01-018/E16.3 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09.03 | SC-M01-018/M4; SC-M01-018/E10.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09.04 | SC-M01-018/M4; SC-M01-018/E10.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09.05 | SC-M01-018/E1.1; SC-M01-018/E11.4 | Một phần — có GAP nguồn |
| FR-M01-09.06 | SC-M01-018/E4.1; SC-M01-018/E14.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09.07 | SC-M01-018/E8.1; SC-M01-018/E18.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09.08 | SC-M01-018/E5.1; SC-M01-018/E15.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09.09 | SC-M01-018/E6.1; SC-M01-018/E16.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09.10 | SC-M01-018/E2.1; SC-M01-018/E12.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09.11 | SC-M01-018/M2; SC-M01-018/E3.1; SC-M01-018/E10.2; SC-M01-018/E11.2; SC-M01-018/E12.2; SC-M01-018/E13.2; SC-M01-018/E13.4; SC-M01-018/E14.2; SC-M01-018/E15.2; SC-M01-018/E16.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09.12 | SC-M01-018/M4; SC-M01-018/E10.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09.13 | SC-M01-018/M2; SC-M01-018/E7.1; SC-M01-018/E10.2; SC-M01-018/E11.2; SC-M01-018/E12.2; SC-M01-018/E13.2; SC-M01-018/E14.2; SC-M01-018/E15.2; SC-M01-018/E16.2; SC-M01-018/E17.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09.14 | SC-M01-018/M2; SC-M01-018/E7.1; SC-M01-018/E10.2; SC-M01-018/E11.2; SC-M01-018/E12.2; SC-M01-018/E13.2; SC-M01-018/E14.2; SC-M01-018/E15.2; SC-M01-018/E16.2; SC-M01-018/E17.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09.15 | SC-M01-018/E9.1; SC-M01-018/E19.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-09.16 | SC-M01-018/M4; SC-M01-018/E10.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-10.01 | SC-M01-007/E109.6; SC-M01-022/M1; SC-M01-022/M2; SC-M01-039/E2.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-10.02 | SC-M01-007/E109.6; SC-M01-022/M2; SC-M01-039/E2.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-10.03 | SC-M01-022/M1; SC-M01-022/M2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-10.04 | SC-M01-022/E1.1; SC-M01-039/E3.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-10.05 | SC-M01-022/E2.1; SC-M01-039/E3.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-10.06 | SC-M01-022/E3.1; SC-M01-039/E3.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-10.07 | SC-M01-007/E109.6; SC-M01-022/M2; SC-M01-039/E2.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-11.01 | SC-M01-023/M1; SC-M01-023/M2; SC-M01-023/E4.2; SC-M01-023/E4.3; SC-M01-023/E5.2; SC-M01-023/E5.3; SC-M01-023/E6.1; SC-M01-023/E6.2; SC-M01-023/E7.1; SC-M01-023/E8.1; SC-M01-023/E8.2; SC-M01-023/E9.1; SC-M01-023/E9.2; SC-M01-023/E10.1; SC-M01-023/E10.2; SC-M01-023/E10.5; SC-M01-023/E10.6; SC-M01-023/E11.1; SC-M01-023/E11.2; SC-M01-023/E11.5; SC-M01-023/E11.6; SC-M01-023/E12.1; SC-M01-023/E12.3; SC-M01-023/E12.4 | Một phần — có GAP nguồn |
| FR-M01-11.02 | SC-M01-023/M3; SC-M01-023/M4; SC-M01-023/E3.2; SC-M01-023/E4.4; SC-M01-023/E5.4; SC-M01-023/E6.3; SC-M01-023/E6.4; SC-M01-023/E8.3; SC-M01-023/E9.3; SC-M01-023/E9.5; SC-M01-023/E9.6; SC-M01-023/E10.3; SC-M01-023/E10.7; SC-M01-023/E10.8; SC-M01-023/E11.3; SC-M01-023/E11.7; SC-M01-023/E11.8; SC-M01-023/E12.5; SC-M01-023/E12.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-11.03 | SC-M01-023/M4; SC-M01-023/E6.4; SC-M01-023/E9.6; SC-M01-023/E10.8; SC-M01-023/E11.8; SC-M01-023/E12.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-11.04 | SC-M01-023/M4; SC-M01-023/E3.1; SC-M01-023/E4.1; SC-M01-023/E6.4; SC-M01-023/E9.4; SC-M01-023/E9.6; SC-M01-023/E10.4; SC-M01-023/E10.8; SC-M01-023/E11.8; SC-M01-023/E12.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-11.05 | SC-M01-023/M4; SC-M01-023/E2.1; SC-M01-023/E6.4; SC-M01-023/E8.4; SC-M01-023/E9.6; SC-M01-023/E10.8; SC-M01-023/E11.8; SC-M01-023/E12.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-11.06 | SC-M01-023/M4; SC-M01-023/E6.4; SC-M01-023/E9.6; SC-M01-023/E10.8; SC-M01-023/E11.8; SC-M01-023/E12.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-11.07 | SC-M01-023/M4; SC-M01-023/E5.1; SC-M01-023/E6.4; SC-M01-023/E9.6; SC-M01-023/E10.8; SC-M01-023/E11.4; SC-M01-023/E11.8; SC-M01-023/E12.6 | Một phần — có GAP nguồn |
| FR-M01-11.08 | SC-M01-023/M4; SC-M01-023/E3.1; SC-M01-023/E4.1; SC-M01-023/E6.4; SC-M01-023/E9.4; SC-M01-023/E9.6; SC-M01-023/E10.4; SC-M01-023/E10.8; SC-M01-023/E11.8; SC-M01-023/E12.6 | Một phần — có GAP nguồn |
| FR-M01-11.09 | SC-M01-023/M2; SC-M01-023/E4.2; SC-M01-023/E5.2; SC-M01-023/E6.2; SC-M01-023/E8.2; SC-M01-023/E9.2; SC-M01-023/E10.2; SC-M01-023/E10.5; SC-M01-023/E11.2; SC-M01-023/E11.5; SC-M01-023/E12.2; SC-M01-023/E12.3; SC-M01-023/E12.4 | Một phần — có GAP nguồn |
| FR-M01-11.10 | SC-M01-023/E1.1; SC-M01-023/E7.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-12.01 | SC-M01-023/E2.1; SC-M01-023/E8.4; AUT-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-12.02 | AUT-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-12.03 | AUT-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-12.04 | SC-M01-007/E4.1; SC-M01-007/E10.2; SC-M01-007/E24.2; SC-M01-007/E36.2; SC-M01-007/E42.2; SC-M01-007/E48.2; SC-M01-007/E54.4; SC-M01-007/E59.4; SC-M01-007/E70.4; SC-M01-007/E81.4; SC-M01-007/E92.4; SC-M01-007/E97.4; SC-M01-007/E103.4; SC-M01-023/E2.1; SC-M01-023/E8.4; AUT-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-12.05 | AUT-M01-003 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-12.06 | SC-M01-007/E54.4; SC-M01-007/E59.4; SC-M01-007/E70.4; SC-M01-007/E81.4; SC-M01-007/E92.4; SC-M01-007/E97.4; SC-M01-007/E103.4; AUT-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-12.07 | AUT-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-12.08 | SC-M01-007/E54.4; SC-M01-007/E59.4; SC-M01-007/E70.4; SC-M01-007/E81.4; SC-M01-007/E92.4; SC-M01-007/E97.4; SC-M01-007/E103.4; SC-M01-025/E1.1; AUT-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-12.09 | AUT-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-12.10 | SC-M01-025/E1.1; AUT-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-12.11 | AUT-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-13.01 | SC-M01-007/E109.6; SC-M01-022/M2; SC-M01-025/E1.1; SC-M01-025/E2.1; SC-M01-039/E2.6; AUT-M01-002; RULE-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-13.02 | SC-M01-022/M2; SC-M01-025/E1.1; SC-M01-025/E2.1; RULE-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-13.03 | SC-M01-007/E109.6; SC-M01-022/M2; SC-M01-039/E2.6; RULE-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-13.04 | AUT-M01-002; RULE-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-13.05 | SC-M01-025/M1; SC-M01-025/M2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-13.06 | AUT-M01-002; RULE-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-13.07 | SC-M01-022/M2; RULE-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.01 | SC-M01-034/M1; SC-M01-034/M2; SC-M01-034/E2.1; SC-M01-034/E2.2; SC-M01-034/E3.1; SC-M01-034/E3.2; SC-M01-034/E4.1; SC-M01-034/E5.1; SC-M01-034/E5.2; SC-M01-034/E6.1; SC-M01-034/E6.2; SC-M01-034/E7.1; SC-M01-034/E8.1; SC-M01-034/E8.2; SC-M01-034/E9.1; SC-M01-034/E9.2; SC-M01-034/E10.1; SC-M01-034/E11.1; SC-M01-034/E11.2; SC-M01-034/E12.1; SC-M01-034/E12.2; SC-M01-034/E13.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.02 | SC-M01-034/M2; SC-M01-034/E2.2; SC-M01-034/E5.2; SC-M01-034/E8.2; SC-M01-034/E11.2 | Một phần — có GAP nguồn |
| FR-M01-14.03 | SC-M01-034/M2; SC-M01-034/E2.2; SC-M01-034/E5.2; SC-M01-034/E8.2; SC-M01-034/E11.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.04 | SC-M01-034/M2; SC-M01-034/E2.2; SC-M01-034/E5.2; SC-M01-034/E8.2; SC-M01-034/E11.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.05 | SC-M01-034/M2; SC-M01-034/E2.2; SC-M01-034/E5.2; SC-M01-034/E8.2; SC-M01-034/E11.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.06 | SC-M01-034/M2; SC-M01-034/M3; SC-M01-034/M4; SC-M01-034/E1.1; SC-M01-034/E1.2; SC-M01-034/E2.2; SC-M01-034/E2.3; SC-M01-034/E2.4; SC-M01-034/E5.2; SC-M01-034/E5.3; SC-M01-034/E5.4; SC-M01-034/E8.2; SC-M01-034/E8.3; SC-M01-034/E8.4; SC-M01-034/E11.2; SC-M01-034/E11.3; SC-M01-034/E11.4; SC-M01-034/E14.1; SC-M01-034/E14.2; SC-M01-034/E15.1; SC-M01-034/E15.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.07 | SC-M01-034/M2; SC-M01-034/M4; SC-M01-034/E1.2; SC-M01-034/E2.2; SC-M01-034/E2.4; SC-M01-034/E5.2; SC-M01-034/E5.4; SC-M01-034/E8.2; SC-M01-034/E8.4; SC-M01-034/E11.2; SC-M01-034/E11.4; SC-M01-034/E14.2; SC-M01-034/E15.2; RULE-MENTION-035 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.08 | SC-M01-034/M2; SC-M01-034/M4; SC-M01-034/E2.2; SC-M01-034/E2.4; SC-M01-034/E5.2; SC-M01-034/E5.4; SC-M01-034/E8.2; SC-M01-034/E8.4; SC-M01-034/E11.2; SC-M01-034/E11.4; SC-M01-034/E14.2; SC-M01-034/E14.4; SC-M01-034/E15.2; SC-M01-034/E15.3; SC-M01-034/E15.4; SC-M01-034/E15.6; RULE-MENTION-035 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.09 | SC-M01-034/E14.3; SC-M01-034/E14.4; SC-M01-034/E15.5; SC-M01-034/E15.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.10 | SC-M01-034/M4; SC-M01-034/E1.2; SC-M01-034/E2.4; SC-M01-034/E5.4; SC-M01-034/E8.4; SC-M01-034/E11.4; SC-M01-034/E14.2; SC-M01-034/E15.2; AUT-M01-005 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.11 | SC-M01-034/E16.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.12 | SC-M01-034/M2; SC-M01-034/E2.2; SC-M01-034/E5.2; SC-M01-034/E8.2; SC-M01-034/E11.2 | Một phần — có GAP nguồn |
| FR-M01-14.13 | SC-M01-034/M2; SC-M01-034/E2.2; SC-M01-034/E5.2; SC-M01-034/E8.2; SC-M01-034/E11.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.14 | SC-M01-034/M2; SC-M01-034/E2.2; SC-M01-034/E4.2; SC-M01-034/E5.2; SC-M01-034/E7.2; SC-M01-034/E8.2; SC-M01-034/E10.2; SC-M01-034/E11.2; SC-M01-034/E13.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.15 | RULE-MENTION-035; RULE-MENTION-036 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.16 | RULE-MENTION-035; RULE-MENTION-036 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-14.17 | AUT-M01-005 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-15.01 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-037/M1; SC-M01-037/M2; SC-M01-037/E1.1; SC-M01-037/E1.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-15.02 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-037/M2; SC-M01-037/E1.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-15.03 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-037/M2; SC-M01-037/E1.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-15.04 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-037/M2; SC-M01-037/E1.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-15.05 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-037/M2; SC-M01-037/E1.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-15.06 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-037/M2; SC-M01-037/E1.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-15.07 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-037/M2; SC-M01-037/E1.2 | Một phần — có GAP nguồn |
| FR-M01-15.08 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-037/M2; SC-M01-037/E1.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-15.09 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-037/M2; SC-M01-037/E1.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-16.01 | SC-M01-007/E107.2; SC-M01-007/E108.2; SC-M01-007/E109.2; SC-M01-039/M1; SC-M01-039/M2; SC-M01-039/E1.1; SC-M01-039/E1.2; SC-M01-039/E2.1; SC-M01-039/E2.2; SC-M01-039/E3.1; SC-M01-039/E3.2; SC-M01-039/E4.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-16.02 | SC-M01-007/E107.3; SC-M01-007/E107.4; SC-M01-039/M3; SC-M01-039/M4 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-16.03 | SC-M01-007/E108.3; SC-M01-007/E108.4; SC-M01-007/E108.5; SC-M01-007/E108.6; SC-M01-007/E109.3; SC-M01-007/E109.4; SC-M01-007/E109.5; SC-M01-007/E109.6; SC-M01-014/E2.1; SC-M01-014/E2.2; SC-M01-039/E1.3; SC-M01-039/E1.4; SC-M01-039/E1.5; SC-M01-039/E1.6; SC-M01-039/E2.3; SC-M01-039/E2.4; SC-M01-039/E2.5; SC-M01-039/E2.6; SC-M01-039/E3.3; SC-M01-039/E3.4; SC-M01-039/E3.5; SC-M01-039/E3.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-16.04 | SC-M01-007/E108.6; SC-M01-014/E2.1; SC-M01-014/E2.2; SC-M01-039/E1.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| FR-M01-16.05 | SC-M01-039/E4.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-01 | SC-M01-001/M4; SC-M01-001/E16.6; SC-M01-001/E21.8; SC-M01-001/E22.6; SC-M01-001/E23.6; SC-M01-001/E24.6; SC-M01-001/E25.6; SC-M01-001/E26.6; SC-M01-001/E27.4; SC-M01-001/E28.4; SC-M01-001/E29.4; SC-M01-001/E30.4; SC-M01-001/E31.4; SC-M01-001/E32.4; SC-M01-001/E33.4; SC-M01-001/E34.4; SC-M01-001/E35.4; SC-M01-001/E36.4; SC-M01-001/E37.4; SC-M01-001/E38.4; SC-M01-001/E39.4; SC-M01-001/E40.4; SC-M01-001/E41.4; SC-M01-001/E42.4; SC-M01-001/E43.4; SC-M01-001/E44.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-02 | SC-M01-001/M4; SC-M01-001/M7; SC-M01-001/E27.4; SC-M01-001/E27.7; SC-M01-001/E28.4; SC-M01-001/E28.7; SC-M01-001/E29.4; SC-M01-001/E29.7; SC-M01-001/E30.4; SC-M01-001/E30.7; SC-M01-001/E31.4; SC-M01-001/E31.7; SC-M01-001/E32.4; SC-M01-001/E32.7; SC-M01-001/E33.4; SC-M01-001/E33.7; SC-M01-001/E34.4; SC-M01-001/E34.7; SC-M01-001/E35.4; SC-M01-001/E35.7; SC-M01-001/E36.4; SC-M01-001/E36.7; SC-M01-001/E37.4; SC-M01-001/E37.7; SC-M01-001/E38.4; SC-M01-001/E38.7; SC-M01-001/E39.4; SC-M01-001/E40.4; SC-M01-001/E41.4; SC-M01-001/E42.4; SC-M01-001/E42.9; SC-M01-001/E43.4; SC-M01-001/E43.9; SC-M01-001/E44.4; SC-M01-001/E44.11; SC-M01-007/E6.5; SC-M01-007/E12.9; SC-M01-007/E13.9; SC-M01-007/E15.5; SC-M01-007/E16.5; SC-M01-007/E17.5; SC-M01-007/E18.5; SC-M01-007/E19.5; SC-M01-007/E20.3; SC-M01-007/E26.3; SC-M01-007/E27.3; SC-M01-007/E28.3; SC-M01-007/E29.3; SC-M01-007/E30.3; SC-M01-007/E31.3; SC-M01-007/E57.5; SC-M01-007/E62.5; SC-M01-007/E63.5; SC-M01-007/E64.5; SC-M01-007/E65.5; SC-M01-007/E66.5; SC-M01-007/E67.5; SC-M01-007/E68.5; SC-M01-007/E73.5; SC-M01-007/E74.5; SC-M01-007/E75.5; SC-M01-007/E76.5; SC-M01-007/E77.5; SC-M01-007/E78.5; SC-M01-007/E79.5; SC-M01-007/E84.5; SC-M01-007/E85.5; SC-M01-007/E86.5; SC-M01-007/E87.5; SC-M01-007/E88.5; SC-M01-007/E89.5; SC-M01-007/E106.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-03 | SC-M01-001/M4; SC-M01-001/E7.3; SC-M01-001/E27.4; SC-M01-001/E28.4; SC-M01-001/E29.4; SC-M01-001/E30.4; SC-M01-001/E31.4; SC-M01-001/E32.4; SC-M01-001/E33.4; SC-M01-001/E34.4; SC-M01-001/E35.4; SC-M01-001/E36.4; SC-M01-001/E37.4; SC-M01-001/E38.4; SC-M01-001/E39.4; SC-M01-001/E40.4; SC-M01-001/E41.4; SC-M01-001/E42.4; SC-M01-001/E43.4; SC-M01-001/E44.4; SC-M01-037/M1; SC-M01-037/E1.1; SC-M01-037/E1.3; SC-M01-037/E1.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-04 | SC-M01-001/M4; SC-M01-001/E3.1; SC-M01-001/E27.4; SC-M01-001/E28.4; SC-M01-001/E29.4; SC-M01-001/E30.4; SC-M01-001/E31.4; SC-M01-001/E32.4; SC-M01-001/E33.4; SC-M01-001/E34.4; SC-M01-001/E35.4; SC-M01-001/E36.4; SC-M01-001/E37.4; SC-M01-001/E38.4; SC-M01-001/E39.4; SC-M01-001/E40.4; SC-M01-001/E41.4; SC-M01-001/E42.4; SC-M01-001/E43.4; SC-M01-001/E44.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-05 | SC-M01-001/M8; SC-M01-001/E11.1; SC-M01-001/E11.2; SC-M01-001/E12.1; SC-M01-001/E12.2; SC-M01-001/E13.1; SC-M01-001/E13.2; SC-M01-001/E14.1; SC-M01-001/E14.2; SC-M01-001/E15.1; SC-M01-001/E15.2; SC-M01-001/E16.8; SC-M01-001/E21.10; SC-M01-001/E22.8; SC-M01-001/E22.9; SC-M01-001/E22.10; SC-M01-001/E23.8; SC-M01-001/E23.9; SC-M01-001/E23.10; SC-M01-001/E24.8; SC-M01-001/E24.9; SC-M01-001/E24.10; SC-M01-001/E25.8; SC-M01-001/E25.9; SC-M01-001/E25.10; SC-M01-001/E26.8; SC-M01-001/E26.9; SC-M01-001/E26.10; SC-M01-001/E27.8; SC-M01-001/E28.8; SC-M01-001/E28.9; SC-M01-001/E28.10; SC-M01-001/E29.8; SC-M01-001/E29.9; SC-M01-001/E29.10; SC-M01-001/E30.8; SC-M01-001/E30.9; SC-M01-001/E30.10; SC-M01-001/E31.8; SC-M01-001/E31.9; SC-M01-001/E31.10; SC-M01-001/E32.8; SC-M01-001/E32.9; SC-M01-001/E32.10; SC-M01-001/E34.10; SC-M01-001/E35.10; SC-M01-001/E36.10; SC-M01-001/E37.10; SC-M01-001/E38.8; SC-M01-001/E42.10; SC-M01-001/E43.10; SC-M01-001/E44.12; SC-M01-007/E6.6; SC-M01-007/E12.10; SC-M01-007/E13.10; SC-M01-007/E15.6; SC-M01-007/E15.7; SC-M01-007/E15.8; SC-M01-007/E16.6; SC-M01-007/E16.7; SC-M01-007/E16.8; SC-M01-007/E17.6; SC-M01-007/E17.7; SC-M01-007/E17.8; SC-M01-007/E18.6; SC-M01-007/E18.7; SC-M01-007/E18.8; SC-M01-007/E19.6; SC-M01-007/E19.7; SC-M01-007/E19.8; SC-M01-007/E20.4; SC-M01-007/E26.4; SC-M01-007/E26.5; SC-M01-007/E26.6; SC-M01-007/E27.4; SC-M01-007/E27.5; SC-M01-007/E27.6; SC-M01-007/E28.4; SC-M01-007/E28.5; SC-M01-007/E28.6; SC-M01-007/E29.4; SC-M01-007/E29.5; SC-M01-007/E29.6; SC-M01-007/E30.4; SC-M01-007/E30.5; SC-M01-007/E30.6; SC-M01-007/E57.6; SC-M01-007/E62.6; SC-M01-007/E62.7; SC-M01-007/E62.8; SC-M01-007/E63.6; SC-M01-007/E63.7; SC-M01-007/E63.8; SC-M01-007/E64.6; SC-M01-007/E64.7; SC-M01-007/E64.8; SC-M01-007/E65.6; SC-M01-007/E65.7; SC-M01-007/E65.8; SC-M01-007/E66.6; SC-M01-007/E66.7; SC-M01-007/E66.8; SC-M01-007/E68.6; SC-M01-007/E73.6; SC-M01-007/E73.7; SC-M01-007/E73.8; SC-M01-007/E74.6; SC-M01-007/E74.7; SC-M01-007/E74.8; SC-M01-007/E75.6; SC-M01-007/E75.7; SC-M01-007/E75.8; SC-M01-007/E76.6; SC-M01-007/E76.7; SC-M01-007/E76.8; SC-M01-007/E77.6; SC-M01-007/E77.7; SC-M01-007/E77.8; SC-M01-007/E79.6; SC-M01-007/E84.6; SC-M01-007/E84.7; SC-M01-007/E84.8; SC-M01-007/E85.6; SC-M01-007/E85.7; SC-M01-007/E85.8; SC-M01-007/E86.6; SC-M01-007/E86.7; SC-M01-007/E86.8; SC-M01-007/E87.6; SC-M01-007/E87.7; SC-M01-007/E87.8; SC-M01-007/E88.6; SC-M01-007/E88.7; SC-M01-007/E88.8; SC-M01-007/E106.5; RULE-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-06 | SC-M01-001/M8; SC-M01-001/E11.1; SC-M01-001/E11.2; SC-M01-001/E12.1; SC-M01-001/E12.2; SC-M01-001/E13.1; SC-M01-001/E13.2; SC-M01-001/E14.1; SC-M01-001/E14.2; SC-M01-001/E15.1; SC-M01-001/E15.2; SC-M01-001/E16.8; SC-M01-001/E21.10; SC-M01-001/E22.8; SC-M01-001/E22.9; SC-M01-001/E22.10; SC-M01-001/E23.8; SC-M01-001/E23.9; SC-M01-001/E23.10; SC-M01-001/E24.8; SC-M01-001/E24.9; SC-M01-001/E24.10; SC-M01-001/E25.8; SC-M01-001/E25.9; SC-M01-001/E25.10; SC-M01-001/E26.8; SC-M01-001/E26.9; SC-M01-001/E26.10; SC-M01-001/E27.8; SC-M01-001/E28.8; SC-M01-001/E28.9; SC-M01-001/E28.10; SC-M01-001/E29.8; SC-M01-001/E29.9; SC-M01-001/E29.10; SC-M01-001/E30.8; SC-M01-001/E30.9; SC-M01-001/E30.10; SC-M01-001/E31.8; SC-M01-001/E31.9; SC-M01-001/E31.10; SC-M01-001/E32.8; SC-M01-001/E32.9; SC-M01-001/E32.10; SC-M01-001/E34.10; SC-M01-001/E35.10; SC-M01-001/E36.10; SC-M01-001/E37.10; SC-M01-001/E38.8; SC-M01-001/E42.10; SC-M01-001/E43.10; SC-M01-001/E44.12; SC-M01-007/E6.6; SC-M01-007/E12.10; SC-M01-007/E13.10; SC-M01-007/E15.6; SC-M01-007/E15.7; SC-M01-007/E15.8; SC-M01-007/E16.6; SC-M01-007/E16.7; SC-M01-007/E16.8; SC-M01-007/E17.6; SC-M01-007/E17.7; SC-M01-007/E17.8; SC-M01-007/E18.6; SC-M01-007/E18.7; SC-M01-007/E18.8; SC-M01-007/E19.6; SC-M01-007/E19.7; SC-M01-007/E19.8; SC-M01-007/E20.4; SC-M01-007/E26.4; SC-M01-007/E26.5; SC-M01-007/E26.6; SC-M01-007/E27.4; SC-M01-007/E27.5; SC-M01-007/E27.6; SC-M01-007/E28.4; SC-M01-007/E28.5; SC-M01-007/E28.6; SC-M01-007/E29.4; SC-M01-007/E29.5; SC-M01-007/E29.6; SC-M01-007/E30.4; SC-M01-007/E30.5; SC-M01-007/E30.6; SC-M01-007/E57.6; SC-M01-007/E62.6; SC-M01-007/E62.7; SC-M01-007/E62.8; SC-M01-007/E63.6; SC-M01-007/E63.7; SC-M01-007/E63.8; SC-M01-007/E64.6; SC-M01-007/E64.7; SC-M01-007/E64.8; SC-M01-007/E65.6; SC-M01-007/E65.7; SC-M01-007/E65.8; SC-M01-007/E66.6; SC-M01-007/E66.7; SC-M01-007/E66.8; SC-M01-007/E68.6; SC-M01-007/E73.6; SC-M01-007/E73.7; SC-M01-007/E73.8; SC-M01-007/E74.6; SC-M01-007/E74.7; SC-M01-007/E74.8; SC-M01-007/E75.6; SC-M01-007/E75.7; SC-M01-007/E75.8; SC-M01-007/E76.6; SC-M01-007/E76.7; SC-M01-007/E76.8; SC-M01-007/E77.6; SC-M01-007/E77.7; SC-M01-007/E77.8; SC-M01-007/E79.6; SC-M01-007/E84.6; SC-M01-007/E84.7; SC-M01-007/E84.8; SC-M01-007/E85.6; SC-M01-007/E85.7; SC-M01-007/E85.8; SC-M01-007/E86.6; SC-M01-007/E86.7; SC-M01-007/E86.8; SC-M01-007/E87.6; SC-M01-007/E87.7; SC-M01-007/E87.8; SC-M01-007/E88.6; SC-M01-007/E88.7; SC-M01-007/E88.8; SC-M01-007/E106.5; RULE-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-07 | SC-M01-001/M8; SC-M01-001/E16.8; SC-M01-001/E21.10; SC-M01-001/E22.10; SC-M01-001/E23.10; SC-M01-001/E24.10; SC-M01-001/E25.10; SC-M01-001/E26.10; SC-M01-001/E27.8; SC-M01-001/E28.10; SC-M01-001/E29.10; SC-M01-001/E30.10; SC-M01-001/E31.10; SC-M01-001/E32.10; SC-M01-001/E34.10; SC-M01-001/E35.10; SC-M01-001/E36.10; SC-M01-001/E37.10; SC-M01-001/E38.8; SC-M01-001/E42.10; SC-M01-001/E43.10; SC-M01-001/E44.12; SC-M01-007/E6.6; SC-M01-007/E12.10; SC-M01-007/E13.10; SC-M01-007/E15.8; SC-M01-007/E16.8; SC-M01-007/E17.8; SC-M01-007/E18.8; SC-M01-007/E19.8; SC-M01-007/E20.4; SC-M01-007/E26.6; SC-M01-007/E27.6; SC-M01-007/E28.6; SC-M01-007/E29.6; SC-M01-007/E30.6; SC-M01-007/E57.6; SC-M01-007/E62.8; SC-M01-007/E63.8; SC-M01-007/E64.8; SC-M01-007/E65.8; SC-M01-007/E66.8; SC-M01-007/E68.6; SC-M01-007/E73.8; SC-M01-007/E74.8; SC-M01-007/E75.8; SC-M01-007/E76.8; SC-M01-007/E77.8; SC-M01-007/E79.6; SC-M01-007/E84.8; SC-M01-007/E85.8; SC-M01-007/E86.8; SC-M01-007/E87.8; SC-M01-007/E88.8; SC-M01-007/E106.5; RULE-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-08 | SC-M01-001/E16.6; SC-M01-001/E21.8; SC-M01-001/E22.6; SC-M01-001/E23.6; SC-M01-001/E24.6; SC-M01-001/E25.6; SC-M01-001/E26.6; SC-M01-007/E56.4; SC-M01-007/E61.4; SC-M01-007/E72.4; SC-M01-007/E83.4; SC-M01-007/E94.4; SC-M01-007/E99.4; SC-M01-007/E105.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-09 | SC-M01-001/E20.4; SC-M01-007/E68.4; SC-M01-007/E73.4; SC-M01-007/E74.4; SC-M01-007/E75.4; SC-M01-007/E76.4; SC-M01-007/E77.4; SC-M01-007/E78.4; SC-M01-007/E79.4; SC-M01-007/E84.4; SC-M01-007/E85.4; SC-M01-007/E86.4; SC-M01-007/E87.4; SC-M01-007/E88.4; SC-M01-007/E89.4; SC-M01-007/E90.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-10 | SC-M01-001/M5; SC-M01-001/E27.5; SC-M01-001/E28.5; SC-M01-001/E29.5; SC-M01-001/E30.5; SC-M01-001/E31.5; SC-M01-001/E32.5; SC-M01-001/E33.5; SC-M01-001/E34.5; SC-M01-001/E35.5; SC-M01-001/E36.5; SC-M01-001/E37.5; SC-M01-001/E38.6; SC-M01-001/E42.8; SC-M01-001/E43.7; SC-M01-001/E44.9; SC-M01-007/E6.3; SC-M01-007/E12.3; SC-M01-007/E13.3; SC-M01-007/E14.3; SC-M01-007/E15.3; SC-M01-007/E16.3; SC-M01-007/E17.3; SC-M01-007/E18.3; SC-M01-007/E19.3; SC-M01-007/E106.2 | Một phần — có GAP nguồn |
| BR-M01-11 | SC-M01-001/E43.6; SC-M01-001/E44.7; SC-M01-001/E44.8 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-12 | SC-M01-018/M2; SC-M01-018/M4; SC-M01-018/E1.1; SC-M01-018/E2.1; SC-M01-018/E3.1; SC-M01-018/E4.1; SC-M01-018/E5.1; SC-M01-018/E6.1; SC-M01-018/E10.2; SC-M01-018/E10.4; SC-M01-018/E11.2; SC-M01-018/E11.4; SC-M01-018/E12.2; SC-M01-018/E12.4; SC-M01-018/E13.2; SC-M01-018/E13.4; SC-M01-018/E14.2; SC-M01-018/E14.4; SC-M01-018/E15.2; SC-M01-018/E15.4; SC-M01-018/E16.2; SC-M01-018/E16.4 | Một phần — có GAP nguồn |
| BR-M01-13 | SC-M01-018/M4; SC-M01-018/E10.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-14 | SC-M01-017/M1; SC-M01-017/M2 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-15 | SC-M01-007/E2.1; SC-M01-007/E8.2; SC-M01-007/E22.2; SC-M01-007/E34.2; SC-M01-007/E40.2; SC-M01-007/E46.2; SC-M01-018/E7.1; SC-M01-018/E8.1; SC-M01-018/E9.1; SC-M01-018/E17.2; SC-M01-018/E18.2; SC-M01-018/E19.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-16 | SC-M01-007/M2; SC-M01-007/E44.2; SC-M01-007/E52.4; SC-M01-007/E90.4; SC-M01-007/E101.4; SC-M01-007/E107.2; SC-M01-007/E108.2; SC-M01-007/E109.2; AUT-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-17 | SC-M01-007/M2; SC-M01-007/E44.2; SC-M01-007/E52.4; SC-M01-007/E90.4; SC-M01-007/E101.4; SC-M01-007/E107.2; SC-M01-007/E108.2; SC-M01-007/E109.2; SC-M01-014/M1; SC-M01-014/M2; AUT-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-18 | SC-M01-007/M2; SC-M01-007/E3.1; SC-M01-007/E4.1; SC-M01-007/E6.2; SC-M01-007/E9.2; SC-M01-007/E10.2; SC-M01-007/E12.2; SC-M01-007/E13.2; SC-M01-007/E14.2; SC-M01-007/E15.2; SC-M01-007/E16.2; SC-M01-007/E17.2; SC-M01-007/E18.2; SC-M01-007/E19.2; SC-M01-007/E20.2; SC-M01-007/E23.2; SC-M01-007/E24.2; SC-M01-007/E26.2; SC-M01-007/E27.2; SC-M01-007/E28.2; SC-M01-007/E29.2; SC-M01-007/E30.2; SC-M01-007/E31.2; SC-M01-007/E32.2; SC-M01-007/E35.2; SC-M01-007/E36.2; SC-M01-007/E38.2; SC-M01-007/E41.2; SC-M01-007/E42.2; SC-M01-007/E44.2; SC-M01-007/E47.2; SC-M01-007/E48.2; SC-M01-007/E52.4; SC-M01-007/E53.4; SC-M01-007/E54.4; SC-M01-007/E57.4; SC-M01-007/E58.4; SC-M01-007/E59.4; SC-M01-007/E62.4; SC-M01-007/E63.4; SC-M01-007/E64.4; SC-M01-007/E65.4; SC-M01-007/E66.4; SC-M01-007/E67.4; SC-M01-007/E68.4; SC-M01-007/E69.4; SC-M01-007/E70.4; SC-M01-007/E73.4; SC-M01-007/E74.4; SC-M01-007/E75.4; SC-M01-007/E76.4; SC-M01-007/E77.4; SC-M01-007/E78.4; SC-M01-007/E79.4; SC-M01-007/E80.4; SC-M01-007/E81.4; SC-M01-007/E84.4; SC-M01-007/E85.4; SC-M01-007/E86.4; SC-M01-007/E87.4; SC-M01-007/E88.4; SC-M01-007/E89.4; SC-M01-007/E90.4; SC-M01-007/E91.4; SC-M01-007/E92.4; SC-M01-007/E95.4; SC-M01-007/E96.4; SC-M01-007/E97.4; SC-M01-007/E101.4; SC-M01-007/E102.4; SC-M01-007/E103.4; SC-M01-007/E107.2; SC-M01-007/E108.2; SC-M01-007/E109.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-19 | SC-M01-007/E32.2; SC-M01-007/E32.3; SC-M01-007/E32.4; SC-M01-007/E38.2; SC-M01-007/E38.3; SC-M01-007/E38.4; SC-M01-007/E50.2; SC-M01-007/E51.2; SC-M01-007/E95.4; SC-M01-007/E95.5; SC-M01-007/E95.6; SC-M01-007/E100.4; SC-M01-014/E1.1; SC-M01-014/E1.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-20 | SC-M01-022/M1; SC-M01-022/M2 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-21 | SC-M01-007/E54.4; SC-M01-007/E59.4; SC-M01-007/E70.4; SC-M01-007/E81.4; SC-M01-007/E92.4; SC-M01-007/E97.4; SC-M01-007/E103.4; SC-M01-007/E109.6; SC-M01-022/M2; SC-M01-023/E2.1; SC-M01-023/E8.4; SC-M01-039/E2.6; AUT-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-22 | SC-M01-023/M2; SC-M01-023/M4; SC-M01-023/E3.1; SC-M01-023/E3.2; SC-M01-023/E4.2; SC-M01-023/E5.2; SC-M01-023/E6.2; SC-M01-023/E6.4; SC-M01-023/E8.2; SC-M01-023/E9.2; SC-M01-023/E9.4; SC-M01-023/E9.5; SC-M01-023/E9.6; SC-M01-023/E10.2; SC-M01-023/E10.5; SC-M01-023/E10.8; SC-M01-023/E11.2; SC-M01-023/E11.5; SC-M01-023/E11.8; SC-M01-023/E12.3; SC-M01-023/E12.4; SC-M01-023/E12.6 | Một phần — có GAP nguồn |
| BR-M01-23 | SC-M01-022/M2; SC-M01-025/E2.1; RULE-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-24 | SC-M01-025/E2.1; AUT-M01-002; RULE-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-25 | SC-M01-023/M4; SC-M01-023/E6.4; SC-M01-023/E9.6; SC-M01-023/E10.8; SC-M01-023/E11.8; SC-M01-023/E12.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-26 | SC-M01-034/M2; SC-M01-034/E2.2; SC-M01-034/E3.1; SC-M01-034/E3.2; SC-M01-034/E5.2; SC-M01-034/E6.1; SC-M01-034/E6.2; SC-M01-034/E8.2; SC-M01-034/E9.1; SC-M01-034/E9.2; SC-M01-034/E11.2; SC-M01-034/E12.1; SC-M01-034/E12.2 | Một phần — có GAP nguồn |
| BR-M01-27 | SC-M01-034/M2; SC-M01-034/E2.2; SC-M01-034/E5.2; SC-M01-034/E8.2; SC-M01-034/E11.2 | Một phần — có GAP nguồn |
| BR-M01-28 | SC-M01-034/M2; SC-M01-034/M4; SC-M01-034/E1.2; SC-M01-034/E2.2; SC-M01-034/E2.4; SC-M01-034/E5.2; SC-M01-034/E5.4; SC-M01-034/E8.2; SC-M01-034/E8.4; SC-M01-034/E11.2; SC-M01-034/E11.4; SC-M01-034/E14.2; SC-M01-034/E15.2; RULE-MENTION-035 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-29 | SC-M01-034/M2; SC-M01-034/M4; SC-M01-034/E2.2; SC-M01-034/E2.4; SC-M01-034/E5.2; SC-M01-034/E5.4; SC-M01-034/E8.2; SC-M01-034/E8.4; SC-M01-034/E11.2; SC-M01-034/E11.4; SC-M01-034/E14.2; SC-M01-034/E14.4; SC-M01-034/E15.2; SC-M01-034/E15.4; SC-M01-034/E15.6; RULE-MENTION-035 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-30 | SC-M01-034/M4; SC-M01-034/E1.2; SC-M01-034/E2.4; SC-M01-034/E5.4; SC-M01-034/E8.4; SC-M01-034/E11.4; SC-M01-034/E14.2; SC-M01-034/E15.2; AUT-M01-005 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-31 | SC-M01-017/M2 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-32 | AUT-M01-003 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-33 | SC-M01-001/E5.1; SC-M01-001/E18.6; SC-M01-001/E27.8; SC-M01-001/E28.10; SC-M01-001/E29.10; SC-M01-001/E30.10; SC-M01-001/E31.10; SC-M01-001/E32.10; SC-M01-001/E34.10; SC-M01-001/E35.10; SC-M01-001/E36.10; SC-M01-001/E37.10; SC-M01-001/E38.6; SC-M01-001/E38.8; SC-M01-001/E42.8; SC-M01-001/E42.10; SC-M01-001/E43.6; SC-M01-001/E44.8; SC-M01-007/E20.4; SC-M01-007/E26.6; SC-M01-007/E27.6; SC-M01-007/E28.6; SC-M01-007/E29.6; SC-M01-007/E30.6; SC-M01-007/E57.6; SC-M01-007/E62.8; SC-M01-007/E63.8; SC-M01-007/E64.8; SC-M01-007/E65.8; SC-M01-007/E66.8; SC-M01-007/E68.4; SC-M01-007/E68.6; SC-M01-007/E73.4; SC-M01-007/E73.8; SC-M01-007/E74.4; SC-M01-007/E74.8; SC-M01-007/E75.4; SC-M01-007/E75.8; SC-M01-007/E76.4; SC-M01-007/E76.8; SC-M01-007/E77.4; SC-M01-007/E77.8; SC-M01-007/E78.4; SC-M01-007/E79.4; SC-M01-007/E79.6; SC-M01-007/E84.4; SC-M01-007/E84.8; SC-M01-007/E85.4; SC-M01-007/E85.8; SC-M01-007/E86.4; SC-M01-007/E86.8; SC-M01-007/E87.4; SC-M01-007/E87.8; SC-M01-007/E88.4; SC-M01-007/E88.8; SC-M01-007/E89.4; SC-M01-007/E90.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-34 | AUT-M01-004; RULE-M01-004 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-35 | SC-M01-001/M3; SC-M01-001/M4; SC-M01-001/E4.1; SC-M01-001/E27.3; SC-M01-001/E27.4; SC-M01-001/E28.3; SC-M01-001/E28.4; SC-M01-001/E29.3; SC-M01-001/E29.4; SC-M01-001/E30.3; SC-M01-001/E30.4; SC-M01-001/E31.3; SC-M01-001/E31.4; SC-M01-001/E32.3; SC-M01-001/E32.4; SC-M01-001/E33.3; SC-M01-001/E33.4; SC-M01-001/E34.3; SC-M01-001/E34.4; SC-M01-001/E35.3; SC-M01-001/E35.4; SC-M01-001/E36.3; SC-M01-001/E36.4; SC-M01-001/E37.3; SC-M01-001/E37.4; SC-M01-001/E38.3; SC-M01-001/E38.4; SC-M01-001/E39.3; SC-M01-001/E39.4; SC-M01-001/E40.3; SC-M01-001/E40.4; SC-M01-001/E41.3; SC-M01-001/E41.4; SC-M01-001/E42.3; SC-M01-001/E42.4; SC-M01-001/E43.3; SC-M01-001/E43.4; SC-M01-001/E44.3; SC-M01-001/E44.4; SC-M01-007/M1; SC-M01-007/E6.1; SC-M01-007/E7.1; SC-M01-007/E8.1; SC-M01-007/E9.1; SC-M01-007/E10.1; SC-M01-007/E11.1; SC-M01-007/E12.1; SC-M01-007/E13.1; SC-M01-007/E14.1; SC-M01-007/E15.1; SC-M01-007/E16.1; SC-M01-007/E17.1; SC-M01-007/E18.1; SC-M01-007/E19.1; SC-M01-007/E20.1; SC-M01-007/E21.1; SC-M01-007/E22.1; SC-M01-007/E23.1; SC-M01-007/E24.1; SC-M01-007/E25.1; SC-M01-007/E26.1; SC-M01-007/E27.1; SC-M01-007/E28.1; SC-M01-007/E29.1; SC-M01-007/E30.1; SC-M01-007/E31.1; SC-M01-007/E32.1; SC-M01-007/E33.1; SC-M01-007/E34.1; SC-M01-007/E35.1; SC-M01-007/E36.1; SC-M01-007/E37.1; SC-M01-007/E38.1; SC-M01-007/E39.1; SC-M01-007/E40.1; SC-M01-007/E41.1; SC-M01-007/E42.1; SC-M01-007/E43.1; SC-M01-007/E44.1; SC-M01-007/E45.1; SC-M01-007/E46.1; SC-M01-007/E47.1; SC-M01-007/E48.1; SC-M01-007/E49.1; SC-M01-007/E107.1; SC-M01-007/E108.1; SC-M01-007/E109.1; SC-M01-017/M1; SC-M01-017/M2; SC-M01-018/M4; SC-M01-018/E1.1; SC-M01-018/E2.1; SC-M01-018/E3.1; SC-M01-018/E4.1; SC-M01-018/E5.1; SC-M01-018/E6.1; SC-M01-018/E10.4; SC-M01-018/E11.4; SC-M01-018/E12.4; SC-M01-018/E13.4; SC-M01-018/E14.4; SC-M01-018/E15.4; SC-M01-018/E16.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-36 | SC-M01-017/M2; RULE-M01-002 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-37 | SC-M01-001/E6.1; SC-M01-007/E5.1; SC-M01-007/E11.2; SC-M01-007/E25.2; SC-M01-007/E37.2; SC-M01-007/E43.2; SC-M01-007/E44.2; SC-M01-007/E49.2; SC-M01-007/E52.4; SC-M01-007/E55.4; SC-M01-007/E60.4; SC-M01-007/E71.4; SC-M01-007/E82.4; SC-M01-007/E90.4; SC-M01-007/E93.4; SC-M01-007/E98.4; SC-M01-007/E101.4; SC-M01-007/E104.4; SC-M01-017/E8.1; SC-M01-022/E4.1; AUT-M01-001; RULE-M01-005 | Một phần — có GAP nguồn |
| BR-M01-38 | SC-M01-001/M6; SC-M01-001/E8.1; SC-M01-001/E9.1; SC-M01-001/E10.1; SC-M01-001/E27.6; SC-M01-001/E28.6; SC-M01-001/E29.6; SC-M01-001/E30.6; SC-M01-001/E31.6; SC-M01-001/E32.6; SC-M01-001/E33.6; SC-M01-001/E34.6; SC-M01-001/E35.6; SC-M01-001/E36.6; SC-M01-001/E37.6; SC-M01-001/E38.6; SC-M01-001/E39.6; SC-M01-001/E40.6; SC-M01-001/E41.6; SC-M01-001/E42.8; SC-M01-001/E43.6; SC-M01-001/E43.8; SC-M01-001/E44.8; SC-M01-001/E44.10; SC-M01-007/E6.4; SC-M01-007/E12.4; SC-M01-007/E12.8; SC-M01-007/E13.4; SC-M01-007/E13.8; SC-M01-007/E14.4; SC-M01-007/E15.4; SC-M01-007/E16.4; SC-M01-007/E17.4; SC-M01-007/E18.4; SC-M01-007/E19.4; SC-M01-007/E106.3; SC-M01-018/M2; SC-M01-018/M4; SC-M01-018/E1.1; SC-M01-018/E2.1; SC-M01-018/E3.1; SC-M01-018/E4.1; SC-M01-018/E5.1; SC-M01-018/E6.1; SC-M01-018/E10.2; SC-M01-018/E10.4; SC-M01-018/E11.2; SC-M01-018/E11.4; SC-M01-018/E12.2; SC-M01-018/E12.4; SC-M01-018/E13.2; SC-M01-018/E13.4; SC-M01-018/E14.2; SC-M01-018/E14.4; SC-M01-018/E15.2; SC-M01-018/E15.4; SC-M01-018/E16.2; SC-M01-018/E16.4 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-39 | SC-M01-018/M2; SC-M01-018/M4; SC-M01-018/E7.1; SC-M01-018/E8.1; SC-M01-018/E9.1; SC-M01-018/E10.2; SC-M01-018/E10.4; SC-M01-018/E11.2; SC-M01-018/E12.2; SC-M01-018/E13.2; SC-M01-018/E14.2; SC-M01-018/E15.2; SC-M01-018/E16.2; SC-M01-018/E17.2; SC-M01-018/E18.2; SC-M01-018/E19.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-40 | SC-M01-034/M2; SC-M01-034/E2.2; SC-M01-034/E4.2; SC-M01-034/E5.2; SC-M01-034/E7.2; SC-M01-034/E8.2; SC-M01-034/E10.2; SC-M01-034/E11.2; SC-M01-034/E13.2; RULE-MENTION-035; RULE-MENTION-036 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-41 | SC-M01-025/M2; SC-M01-025/E1.1; SC-M01-025/E2.1 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-42 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-037/M2; SC-M01-037/E1.2 | Một phần — có GAP nguồn |
| BR-M01-43 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-037/M2; SC-M01-037/E1.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-44 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-007/E107.2; SC-M01-007/E107.4; SC-M01-007/E108.2; SC-M01-007/E109.2; SC-M01-037/M2; SC-M01-037/E1.2; SC-M01-039/M2; SC-M01-039/M4; SC-M01-039/E1.2; SC-M01-039/E2.2; SC-M01-039/E3.2; SC-M01-039/E4.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-45 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-007/E108.4; SC-M01-007/E108.6; SC-M01-007/E109.4; SC-M01-007/E109.6; SC-M01-014/E2.1; SC-M01-014/E2.2; SC-M01-022/M1; SC-M01-022/M2; SC-M01-037/M2; SC-M01-037/E1.2; SC-M01-039/E1.4; SC-M01-039/E1.6; SC-M01-039/E2.4; SC-M01-039/E2.6; SC-M01-039/E3.4; SC-M01-039/E3.6 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-46 | SC-M01-001/E7.2; SC-M01-001/E21.6; SC-M01-037/M2; SC-M01-037/E1.2 | Có vị trí triển khai; cần review ngữ nghĩa |
| BR-M01-47 | SC-M01-025/E1.1; AUT-M01-002; RULE-M01-001 | Có vị trí triển khai; cần review ngữ nghĩa |


## 8. GAP cần chốt nguồn

| ID | Nguồn | Điểm chưa rõ | Ảnh hưởng | Mức chặn |
|---|---|---|---|---|
| GAP-SC-M01-001 | US-M01 UC-M01-001/main-1 và A1; FR-M01-01.01, FR-M01-01.07 | US nêu nhập lại mật khẩu khi đăng ký email, FR chỉ quy định email/mật khẩu và chưa định nghĩa kiểm nhập lại. | SC-M01-001: chưa thêm trường/ngoại lệ nhập lại vào bước 1. Cần xác nhận có trường này rồi cập nhật nguồn tương ứng; phần chuẩn theo FR vẫn triển khai được. | Chặn việc chốt trường nhập lại; không chặn đường FR đã có. |
| GAP-SC-M01-002 | FR-M01-02.02, FR-M01-03.09, FR-M01-05.10, FR-M01-05.11; US-M01 UC-M01-003/preconditions | Bước 3 bắt buộc có phiên, nhưng thời điểm/cách cấp phiên được phép tiếp tục đăng ký khi NONE/EMAIL_VERIFIED và sau mở link xác minh chưa được FR mô tả rõ; không được tự coi đăng ký xong hoặc tự tạo loại phiên mới. | SC-M01-001/002/004/005/006 và các đường định tuyến bước 2/3: kịch bản ghi hợp đồng chuyển bước theo US, phần cấp/giới hạn phiên chuyển tiếp cần chốt. | Chặn xác nhận đầy đủ đoạn chuyển tiếp quyền ở đăng ký/tiếp tục bước 3; không chặn các scenario bắt đầu với phiên hợp lệ đã có. |
| GAP-SC-M01-003 | FR-M01-04.04, FR-M01-05.19, FR-M01-05.20, BR-M01-37; US-M01 UC-M01-015/main-2 và UC-M01-017 | US thực hiện tự liên kết trước cổng, còn bảo trì chỉ cho ADMIN đăng nhập/thao tác. Nguồn chưa nói rõ người không ADMIN bị chặn trước thay đổi liên kết hay vẫn có side effect rồi bị từ chối truy cập. | Các nhánh Google + tài khoản email khớp + bảo trì + không ADMIN: quyền truy cập chắc chắn bị từ chối; thứ tự/side effect liên kết chưa được chốt. Đường bảo trì tắt và ADMIN đủ điều kiện đã viết. | Chặn kết luận side effect của riêng tổ hợp này. |
| GAP-SC-M01-004 | FR-M01-02.03, FR-M01-09.05, FR-M01-11.07, BR-M01-10, BR-M01-12, BR-M01-22 | FR dùng “quá” 1 giờ/15 phút trong khi mô tả hạn dùng dùng từ “còn hạn”; cần thống nhất quy ước còn hợp lệ tại đúng thời điểm hết hạn cho link/OTP. Không đổi mốc 14×24 giờ vốn đã nêu rõ. | Ví dụ dùng 10 phút/16 phút hoặc 59 phút/61 phút; chưa tự chốt kết quả ở đúng 15 phút/1 giờ. | Chỉ chặn kết quả biên thời gian chưa được xác nhận. |
| GAP-SC-M01-005 | FR-M01-11.01, FR-M01-11.08, FR-M01-11.09, BR-M01-22 | Nguồn định nghĩa hạn OTP/lần sai/khoảng cách gửi lại nhưng chưa nêu mã trước còn hiệu lực hay không khi gửi mã mới, hoặc số lần sai tính riêng mỗi mã thế nào. | SC-M01-023/024 dùng đúng mã mới; chỉ làm mã cũ mất hiệu lực khi sai lần 5 hoặc hết hạn. Không áp quy tắc magic link sang OTP; cần quyết định để viết đường dùng lại mã cũ sau resend. | Chặn đường nhập mã trước sau khi gửi lại và quy tắc đếm gắn mã; đường dùng mã mới đã mô tả. |
| GAP-SC-M01-006 | FR-M01-14.02, FR-M01-14.12, BR-M01-26, BR-M01-27 | Chưa có ngưỡng “gõ sai nhẹ” hoặc quy tắc phá hòa khi mức khớp bằng nhau. Đây là phần cần đặc tả trước khi dùng dữ liệu bằng điểm để nghiệm thu thứ tự chính xác. | Các scenario gợi ý dùng truy vấn rõ ràng và bộ dữ liệu giả lập được phân biệt độ khớp; không invent điểm số/thuật toán. Không khẳng định thứ tự giữa hai ứng viên hoàn toàn ngang nhau. | Không chặn tương tác tìm/chọn/chèn; giới hạn việc nghiệm thu fuzzy/tie chính xác. |
| GAP-SC-M01-007 | FR-M01-04; US-M01 UC-M01-004/015 | Nguồn mô tả nhận danh tính Google thành công nhưng chưa định nghĩa kết quả khi Google không trả danh tính, trả lỗi hoặc người dùng hủy ở dịch vụ Google. | Kịch bản chỉ giả lập đường Google trả danh tính thành công; chưa bổ sung phản hồi, nút thử lại hoặc hành vi quay lại của những nhánh thiếu nguồn. | Chặn khẳng định đã bao phủ lỗi/hủy tại nhà cung cấp Google. |
| GAP-SC-M01-008 | FR-M01-01.03, FR-M01-09.01, FR-M01-11.01; FR-M07-04.01, BR-M07-03 | M01 yêu cầu email xác minh/đặt lại/OTP, nhưng danh sách sự kiện email M07 chỉ nêu email thông báo. Chưa rõ các email giao dịch này có cùng cơ chế quét/thử lại hay không và cách người dùng được xử lý khi gửi thất bại. | Đường thành công gửi link/OTP theo hợp đồng M01; EMAIL-M01-001 chỉ áp dụng email sự kiện đã được M07 liệt kê, không áp lịch retry đó cho link/OTP. | Chặn nhánh lỗi gửi email giao dịch; không chặn nhánh link/OTP đã nhận thành công. |
| TBD-M01-01 / OPEN-008 | FR-M01 Phụ lục B.2; BR-M01-42, FR-M01-15.07 | Email liên hệ, cách yêu cầu bản sao dữ liệu và câu chữ chính sách hoàn chỉnh được nguồn hoãn có chủ đích. | Scenario chính sách kiểm cấu trúc/nội dung phải có theo FR, không ghi địa chỉ liên hệ hoặc câu chữ pháp lý giả định; không tạo chức năng tải bản sao ở MS1. | Đã hoãn trong nguồn; chưa chốt chi tiết nội dung trang. |


## 9. Kiểm tra

Lệnh, kết quả và giới hạn kiểm tra ở [QA-M01.md](QA-M01.md). PASS chỉ chứng minh cấu trúc/đường đi; chưa phê duyệt và chưa giải quyết GAP nghiệp vụ.
