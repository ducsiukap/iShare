# Bước 1 — Khoanh phạm vi và lập bảng nguồn

## Mục đích

Biết module làm gì, không làm gì, và có **đủ** mọi mục nguồn liên quan trước khi phân tích.
Bỏ sót nguồn ở bước này thì mọi bước sau đều thiếu.

## Đầu vào

Mã module; các tệp ở `input/INPUTS.md`.

## Việc làm

1. Chạy `index_sources.py --out $W/index.json`. Ghi lại "ID kế tiếp" để tính `moc_nguon`
   (mốc = ID kế tiếp trừ 1 của DEC, QA, ISS, OPEN).
2. Đọc nguyên văn: dòng `MR-Mxx` của module-registry; các mục draft của module (tìm trong
   `iShare_modules.md` và `iShare_specs_general.md` mục nói tới module); các section register có tên module
   ("Phase 5 — Mxx: …").
3. Lập **owner keywords**: thực thể, khái niệm, động từ nghiệp vụ riêng của module, cả tiếng Việt lẫn tiếng Anh
   như register đang dùng (ví dụ M05: topic, chủ đề, tag, hashtag, trending).
   Lập **dependency keywords**: thực thể của module khác mà module này chạm tới (ví dụ M05: post, bài viết,
   search, notification, feed).
4. Chạy `scan_sources.py` với keyword và `--draft` là các mục draft của module.
5. Đọc **nguyên văn** từng mục nhóm A, B, C. Với nhóm D (dùng chung), đọc trích dẫn và mở nguyên văn mục nào
   có thể chạm tới module. Gắn nhãn cho từng mục:
   - **Sở hữu**: mục quy định hành vi mà module này là nơi người dùng thấy kết quả.
   - **Phụ thuộc**: mục của module khác mà module này cần dùng hoặc phải tuân theo (kể cả quy định dùng chung
     như múi giờ, AI tắt/bật).
   - **Nhắc tới**: có nói tới module nhưng không quy định gì mới (ví dụ ISS đã có DEC trả lời).
   - **Khớp nhầm**: đưa vào `--exclude` rồi chạy lại `scan_sources.py`, để bảng nguồn cuối chỉ còn mục liên quan.
6. Phác phạm vi: trong phạm vi (nhóm hành vi thuộc module), ngoài phạm vi (hành vi liên quan nhưng module khác
   sở hữu, kèm mã module; điều đã quyết là không làm, ví dụ ở DG mục "Không làm").

## Ghi vào tệp FR

- Frontmatter: `module`, `ten_module`, `ma_tai_lieu`, `ngay`, `moc_nguon`.
- Mục 1.1 (nháp từ draft), 1.2 (trong/ngoài phạm vi), 3.1, 3.2.
- Phụ lục C: dòng keyword, mục draft, danh sách loại; bảng C.1 với **mọi** mục của bảng nguồn cuối.
  Cột Trạng thái tạm ghi "Hiện hành", cột Dùng ở ghi "—" (bước 2 và 5 điền).

## Tự kiểm trước cổng

- Mọi mục của `scan-Mxx.json` đều có dòng ở C.1.
- Mỗi mục ghi Sở hữu thật sự quy định hành vi của module này, không phải của module khác.
- Không có mục nào của section "Phase 5 — Mxx" bị loại mà không có lý do.

## Trình ở cổng

- Số mục theo nhóm A/B/C/D và theo nhãn.
- Phạm vi trong và ngoài, mỗi bên vài dòng.
- Owner và dependency keywords.
- Các mục **ngoài** section module nhưng được gắn Sở hữu (dễ sai nhất, liệt kê hết).
- Số mục bị loại vì khớp nhầm, kèm 3–5 ví dụ.
- Điểm nghi ngờ về ranh giới giữa module này và module khác.

## Không làm

Không phân tích nội dung, không đánh giá mâu thuẫn, không viết yêu cầu. Đó là việc của bước sau.
