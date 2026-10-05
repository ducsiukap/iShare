# Mẫu lời gọi Auditor

Dùng khi chạy Auditor trong một phiên mới hoặc bằng subagent. Truyền **chỉ** nội dung trong khối dưới đây. Không đính kèm tóm tắt của Author, không đính kèm SR, không đính kèm đoạn nào của hội thoại. Mỗi lượt là một phiên/subagent riêng; P1, P2, P3 có thể chạy song song, MERGE chạy sau khi cả ba xong.

```
Bạn là Auditor của iShare. Đọc và làm theo tệp
.agent-instructions/system_analysis/roles/sr-auditor/AGENT.md.
Module: Mxx. Vòng: <n>. Lượt (PASS): <P1 | P2 | P3 | MERGE | VERIFY | RELEASE>. Gốc repo: <đường dẫn>.
[Vòng 2: báo cáo vòng 1 ở .agents/.claude/system_analysis/output/specs/audit/ISH-AUD-Mxx-r1.md.]
[VERIFY: Vòng: v1; báo cáo vòng 2 ở .agents/.claude/system_analysis/output/specs/audit/ISH-AUD-Mxx-r2.md.]
[RELEASE: Vòng: rel<n>; báo cáo audit gần nhất ở .agents/.claude/system_analysis/output/specs/audit/<tên báo cáo>.md; phiên bản đã audit: x.y.]
Chỉ ghi vào specs/audit/ (tệp của lượt mình). Trả về: tên tệp đã ghi, kết luận của lượt (hoặc kết luận báo cáo
nếu là MERGE/VERIFY/RELEASE), số finding theo lớp x mức, các vấn đề cần stakeholder quyết, phần bạn không kiểm được.
```

Công cụ nên cấp cho subagent: đọc tệp, tìm kiếm (`grep`/`glob`), shell (chỉ để chạy script, `grep`, `sed -n`, `diff`), ghi tệp (chỉ vào `specs/audit/`). Không cấp quyền gọi subagent khác, không cấp công cụ web.

Một người dùng không có subagent có thể chạy `PASS=ALL` trong một phiên (ba lượt tuần tự rồi MERGE); kết quả ít độc lập hơn và báo cáo sẽ ghi rõ điều đó.
