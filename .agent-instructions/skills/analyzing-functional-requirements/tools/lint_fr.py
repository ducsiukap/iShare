#!/usr/bin/env python3
"""Kiểm tệp FR theo quy ước của skill (dùng ở cuối bước 5 và bước 7).

Cách dùng (từ gốc repo):
  python3 .../lint_fr.py --fr <FR-Mxx.md> --index <index.json> [--lineage <lineage.json>] [--final]

TR-07 (ERROR): một yêu cầu trích nguồn đã bị thay hẳn mà không trích nguồn thay thế.
TR-08 (WARN, mỗi cặp một dòng): nguồn bị sửa một phần, nhưng mục sửa không được trích ở đâu và không có trong C.2.

--final dùng ở bước 7: còn [GAP] hoặc TBD ảnh hưởng Cao thì là lỗi.
Mã kết quả: 0 không có ERROR, 1 có ERROR. WARN cần agent xem và giải thích ở cổng.
"""
import argparse
import os
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frlib  # noqa: E402

# Từ và cụm mơ hồ (theo tinh thần ISO 29148). Không dùng từ đơn "thường", "khoảng" vì trùng với
# "chữ thường", "khoảng trắng"; chỉ bắt các cụm thật sự mơ hồ.
VAGUE = ["hợp lý", "phù hợp", "nhanh chóng", "thân thiện", "dễ dùng", "dễ sử dụng", "linh hoạt", "tối ưu",
         "nếu có thể", "khi cần thiết", "v.v", "vân vân", "và/hoặc", "một số", "tương tự", "đáng kể",
         "gần như", "thông thường", "thường xuyên", "xấp xỉ", "khoảng chừng", "tốt nhất", "đủ lớn", "kịp thời"]
VAGUE_RE = [re.compile(r"(?<!\w)khoảng\s+\d")]  # "khoảng 5 phút"
TECH = re.compile(r"(?<!\w)(API|endpoint|database|cơ sở dữ liệu|table|column|schema|JSON|SQL|HTTP|REST|JWT|"
                  r"cron|cache|Redis|pgvector|pg_trgm|SSE|WebSocket|query|ENUM|boolean|foreign key|"
                  r"is_active|is_stale|post_tags)(?!\w)", re.I)
STARTERS = re.compile(r"^(Hệ thống phải|Khi |Trong khi |Nếu |Ở nơi )")
DRAFT_LIKE = re.compile(r"^(DM|DG)-[\w.]+$|^GL:.+|^MR-[\w-]+$|^F-[A-Z]+-\d{2}$")
BASIS = {"Nói thẳng", "Suy ra"}

out = {"ERROR": [], "WARN": [], "INFO": []}


def say(level, code, msg):
    out[level].append("%-5s %s  %s" % (level, code, msg))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fr", required=True)
    ap.add_argument("--index", help="chỉ mục nguồn để kiểm ID nguồn có tồn tại")
    ap.add_argument("--lineage", help="chuỗi sửa đổi để kiểm trích nguồn đã bị thay")
    ap.add_argument("--final", action="store_true")
    a = ap.parse_args()

    fr = frlib.parse_fr(frlib.read(a.fr))
    fm, mod, pats = fr["fm"], fr["module"], fr["pats"]
    units = frlib.load_json(a.index)["units"] if a.index else None
    chains = frlib.load_json(a.lineage)["edges"] if a.lineage else []

    for k in ("module", "ma_tai_lieu", "phien_ban", "trang_thai", "moc_nguon", "steps_completed"):
        if k not in fm:
            say("ERROR", "FM-01", "frontmatter thiếu khóa '%s'" % k)
    if not re.fullmatch(r"M(0[1-9]|1[0-6])", mod or ""):
        say("ERROR", "FM-02", "khóa module phải có dạng Mxx, đang là '%s'" % mod)
        return finish()

    # ID trùng và đúng dạng
    body = fr["body"]
    first_cells = re.findall(r"^\|\s*((?:FR|BR|TBD)-[^|\s]+)\s*\|", body, re.M)
    defining = [c for c in first_cells if not c in fr["appendix_a"]]
    seen = {}
    for c in re.findall(r"^\|\s*((?:FR-%s-\d{2}\.\d{2})|(?:BR-%s-\d{2}))\s*\|" % (mod, mod), body.split("## Phụ lục")[0], re.M):
        seen[c] = seen.get(c, 0) + 1
    for c, n in seen.items():
        if n > 1:
            say("ERROR", "ID-01", "%s được định nghĩa %d lần" % (c, n))
    for c in first_cells:
        if c.startswith(("FR-", "BR-", "TBD-")) and not pats["any"].fullmatch(c):
            say("ERROR", "ID-02", "ID sai dạng hoặc sai mã module: %s" % c)

    # 4.4 khớp 5.x
    l44 = [i for i in fr["list44"] if pats["upper"].match(i)]
    for i in l44:
        if i not in fr["upper_heads"]:
            say("ERROR", "ST-01", "%s có ở 4.4 nhưng không có mục 5.x" % i)
    for i in fr["upper_heads"]:
        if i not in l44:
            say("ERROR", "ST-02", "%s có mục 5.x nhưng không có ở 4.4" % i)
        txt = fr["upper_heads"][i]["text"]
        if "**Yêu cầu cấp trên:**" not in txt:
            say("ERROR", "ST-03", "%s thiếu dòng 'Yêu cầu cấp trên'" % i)
        if "**Lý do:**" not in txt:
            say("ERROR", "ST-04", "%s thiếu dòng 'Lý do'" % i)
        if not any(d == i for d in fr["defined"].values()):
            say("WARN", "ST-05", "%s chưa có yêu cầu cấp dưới" % i)

    # Câu yêu cầu cấp dưới
    for rid, txt in fr["lower_text"].items():
        if "[GAP" in txt:
            continue
        if not STARTERS.match(txt) or "hệ thống phải" not in txt.lower():
            say("WARN", "REQ-01", "%s không theo mẫu EARS tiếng Việt: %s" % (rid, frlib.excerpt(txt, 80)))
        if len(re.findall(r"\bphải\b", txt)) > 1:
            say("WARN", "REQ-02", "%s có hơn một 'phải', có thể gộp hai hành vi" % rid)
        low = txt.lower()
        for w in VAGUE:
            if re.search(r"(?<!\w)" + re.escape(w) + r"(?!\w)", low):
                say("WARN", "REQ-03", "%s có từ mơ hồ '%s'" % (rid, w))
        for rx in VAGUE_RE:
            mm = rx.search(low)
            if mm:
                say("WARN", "REQ-03", "%s có cụm mơ hồ '%s'" % (rid, mm.group(0)))
        m = TECH.search(txt)
        if m:
            say("WARN", "REQ-04", "%s có từ kỹ thuật '%s' (chi tiết cài đặt không thuộc FR)" % (rid, m.group(1)))

    # Ma trận quyền
    for r in fr["perm"]:
        if len(r) >= 6 and r[-1] in ("", "—"):
            say("WARN", "PERM-01", "dòng quyền '%s' chưa trỏ tới yêu cầu" % frlib.excerpt(r[0], 50))
        if len(r) >= 6:
            for i in pats["any"].findall(r[-1]):
                if i not in fr["defined"]:
                    say("ERROR", "PERM-02", "ma trận quyền trỏ tới %s chưa được định nghĩa" % i)

    # Phụ lục A
    A = fr["appendix_a"]
    for i in [d for d, k in fr["defined"].items() if k != "TBD"] + l44:
        if i not in A:
            say("ERROR", "TR-01", "%s không có dòng ở Phụ lục A" % i)
    superseded = {}
    for e in chains:
        superseded.setdefault(e["target"], []).append((e["by"], e["kind"]))
    for i, row in A.items():
        if (i not in fr["defined"] or fr["defined"][i] == "TBD") and i not in l44:
            say("ERROR", "TR-02", "Phụ lục A có %s nhưng ID này không được định nghĩa" % i)
        if not row["sources"] or row["sources"] == ["—"]:
            say("ERROR", "TR-03", "%s không có nguồn" % i)
        if row["basis"] not in BASIS:
            say("ERROR", "TR-04", "%s: căn cứ phải là 'Nói thẳng' hoặc 'Suy ra', đang là '%s'" % (i, row["basis"]))
        if row["basis"] == "Suy ra" and row["note"] in ("", "—"):
            say("ERROR", "TR-05", "%s căn cứ Suy ra nhưng không ghi phép suy luận" % i)
        for s in row["sources"]:
            if s == "—":
                continue
            if units is not None and s not in units and not DRAFT_LIKE.match(s):
                say("ERROR", "TR-06", "%s trích nguồn không tồn tại: %s" % (i, s))
            if units is not None and DRAFT_LIKE.match(s) and s not in units:
                say("ERROR", "TR-06", "%s trích mục draft/glossary/registry không có trong chỉ mục: %s" % (i, s))
            for by, kind in superseded.get(s, []):
                # Bị thay hẳn: dòng nào trích nguồn cũ cũng phải trích nguồn mới.
                if kind == "superseded" and by not in row["sources"]:
                    say("ERROR", "TR-07", "%s trích %s, mục này bị thay hẳn bởi %s nhưng %s chưa được trích" % (i, s, by, by))

    # Sửa một phần (amended/clarified/added): chỉ báo một lần cho mỗi cặp, và chỉ khi mục sửa
    # chưa được trích ở đâu trong Phụ lục A và cũng không có trong chuỗi quyết định C.2.
    cited_all = set()
    for row in A.values():
        cited_all.update(row["sources"])
    c2_ids = set(frlib.find_ids(fr["c2_text"]))
    pending = set()
    for s in cited_all:
        amenders = [(by, kind) for by, kind in superseded.get(s, []) if kind != "superseded"]
        # Một dấu sửa đổi thường nêu cả DEC lẫn QA/ISS nguồn của nó; khi có DEC thì chỉ xét DEC.
        if any(by.startswith("DEC-") for by, _ in amenders):
            amenders = [(by, kind) for by, kind in amenders if by.startswith("DEC-")]
        for by, kind in amenders:
            if by not in cited_all and by not in c2_ids:
                pending.add((s, by, kind))
    for s, by, kind in sorted(pending):
        say("WARN", "TR-08", "%s bị %s một phần bởi %s, nhưng %s chưa được trích ở Phụ lục A và chưa có trong C.2" % (s, kind, by, by))

    # GAP và TBD
    gaps = re.findall(r"\[GAP[^\]]*\]", body)
    if gaps:
        say("ERROR" if a.final else "INFO", "GAP-01", "còn %d chỗ [GAP]" % len(gaps))
    for t in fr["tbd"]:
        if t["impact"].strip().lower() == "cao":
            say("ERROR" if a.final else "WARN", "TBD-01", "%s ảnh hưởng Cao chưa được chốt" % t["id"])

    say("INFO", "SUM-01", "chức năng=%d, yêu cầu cấp dưới=%d, quy tắc=%d, dòng truy vết=%d" % (
        len(fr["upper_heads"]), len(fr["lower_text"]), len(fr["br"]), len(A)))
    return finish()


def finish():
    for lvl in ("ERROR", "WARN", "INFO"):
        for line in out[lvl]:
            print(line)
    print("---\nERROR=%d WARN=%d INFO=%d" % (len(out["ERROR"]), len(out["WARN"]), len(out["INFO"])))
    return 1 if out["ERROR"] else 0


if __name__ == "__main__":
    sys.exit(main())
