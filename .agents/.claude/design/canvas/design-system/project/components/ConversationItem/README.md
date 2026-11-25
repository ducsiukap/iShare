# ConversationItem

Một cuộc trò chuyện trong Hộp thư Chat: tên (người hoặc nhóm chat), tin gần nhất, thời điểm, số tin chưa đọc.

**Dùng khi:** Hộp thư Chat (SCR-M16-01), mới nhất ở trên.

**Không dùng khi:** thông báo (dùng NotificationItem).

## Biến thể và trạng thái

- Có tin chưa đọc: tin gần nhất đậm + Counter; đang mở: nền `primary-soft`; đã tắt popup cuộc này: icon chuông gạch.

## Cần cung cấp

- Tên, avatar (nhóm chat: chữ cái đầu tên nhóm), tin gần nhất ("Bạn: …" nếu của mình), thời điểm, số chưa đọc.

## Khả năng truy cập

- Mỗi dòng là liên kết; số chưa đọc có nhãn đầy đủ.

## Class và token

`is-convo`, `is-convo--unread`, `is-convo__name`, `is-convo__last`, `is-convo__end` · token `primary-soft`, `primary`, `ink-muted`.
