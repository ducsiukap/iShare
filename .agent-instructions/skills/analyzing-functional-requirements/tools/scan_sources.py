#!/usr/bin/env python3
"""Bước 1 — Lọc từ chỉ mục những mục nguồn liên quan tới một module, chia thành bốn nhóm.

  A  Trong section của module (heading có Mxx), dòng Mxx của module-registry,
     và các mục draft được chỉ định bằng --draft.
  B  Ngoài section nhưng khớp owner keyword (--keywords).
  C  Có quan hệ tham chiếu với nhóm A (A nhắc tới nó, hoặc nó nhắc tới A).
  D  Section dùng chung cho mọi module (--common), ví dụ Phase 6, Tech Stack, Privacy.

Dependency keyword (--dep-keywords) không tạo nhóm riêng; mục khớp được đánh dấu ở cột
"Dep" để agent nhận ra chỗ module này chạm tới module khác.

Cách dùng (từ gốc repo):
  python3 .../scan_sources.py --index <index.json> --module M05 \
     --keywords "topic,tag,trending,chủ đề" --dep-keywords "post,bài viết,search" \
     --draft DM-3.1,DM-3.2,DM-7.2 --out-md <scan.md> --out-json <scan.json>

Tool chỉ lo phần "không bỏ sót". Gắn nhãn Sở hữu / Phụ thuộc / Nhắc tới / Loại là việc của agent.
"""
import argparse
import os
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frlib  # noqa: E402

DEFAULT_COMMON = r"Phase 6|Cross-cutting|Tech Stack|Privacy"


def kw_regex(words):
    words = [w.strip() for w in words.split(",") if w.strip()]
    if not words:
        return None
    alt = "|".join(re.escape(w) for w in sorted(words, key=len, reverse=True))
    return re.compile(r"(?<!\w)(" + alt + r")(?!\w)", re.I)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--index", required=True)
    ap.add_argument("--module", required=True, help="ví dụ M05")
    ap.add_argument("--keywords", default="", help="owner keywords, phân tách bằng dấu phẩy")
    ap.add_argument("--dep-keywords", default="", help="dependency keywords, phân tách bằng dấu phẩy")
    ap.add_argument("--draft", default="", help="ID mục draft thuộc module, ví dụ DM-3.1,DM-3.2 (gồm cả mục con)")
    ap.add_argument("--common", default=DEFAULT_COMMON, help="regex tên section dùng chung")
    ap.add_argument("--exclude", default="", help="ID loại khỏi kết quả (agent đã xác nhận khớp nhầm)")
    ap.add_argument("--out-md")
    ap.add_argument("--out-json")
    a = ap.parse_args()

    data = frlib.load_json(a.index)
    units = data["units"]
    mod = a.module.upper()
    own = kw_regex(a.keywords)
    dep = kw_regex(a.dep_keywords)
    common = re.compile(a.common, re.I) if a.common else None
    drafts = [d.strip() for d in a.draft.split(",") if d.strip()]
    excluded = {e.strip() for e in a.exclude.split(",") if e.strip()}

    group = {}
    hits = {}
    for uid, u in units.items():
        if uid in excluded:
            continue
        in_section = mod in [s_m for s_m in [frlib.MODULE_RE.search(s) and "M" + frlib.MODULE_RE.search(s).group(1) for s in u["sections"]] if s_m]
        if in_section or uid == "MR-" + mod or any(uid == d or uid.startswith(d + ".") for d in drafts):
            group[uid] = "A"
        found = sorted({m.group(1).lower() for m in own.finditer(u["text"])}) if own else []
        if found:
            hits[uid] = found
            group.setdefault(uid, "B")
    a_ids = {k for k, g in group.items() if g == "A"}
    for uid, u in units.items():
        if uid in group or uid in excluded:
            continue
        if any(r in a_ids for r in u["refs"]):
            group[uid] = "C"
    for aid in a_ids:
        for r in units[aid]["refs"]:
            if r in units and r not in group and r not in excluded:
                group[r] = "C"
    for uid, u in units.items():
        if uid in group or uid in excluded:
            continue
        if common and any(common.search(s or "") for s in u["sections"]):
            group[uid] = "D"

    def key(uid):
        return (group[uid], units[uid]["kind"], uid)

    rows = []
    for uid in sorted(group, key=key):
        u = units[uid]
        d = sorted({m.group(1).lower() for m in dep.finditer(u["text"])}) if dep else []
        rows.append({"id": uid, "group": group[uid], "kind": u["kind"], "section": u["section"],
                     "home_module": u["home_module"], "keywords": hits.get(uid, []), "dep": d,
                     "file": u["file"], "lines": u["lines"], "excerpt": frlib.excerpt(u["text"])})

    counts = {g: sum(1 for r in rows if r["group"] == g) for g in "ABCD"}
    out = {"module": mod, "keywords": a.keywords, "dep_keywords": a.dep_keywords, "draft": drafts,
           "excluded": sorted(excluded), "counts": counts, "rows": rows}
    if a.out_json:
        frlib.dump_json(a.out_json, out)
    md = ["# Bảng nguồn ứng viên — %s" % mod, "",
          "Nhóm: A trong section module · B khớp owner keyword · C có tham chiếu với A · D dùng chung.", "",
          "Số mục: " + ", ".join("%s=%d" % (g, counts[g]) for g in "ABCD"), "",
          "| Nguồn | Nhóm | Loại | Section | Keyword | Dep | Vị trí | Trích |",
          "|---|---|---|---|---|---|---|---|"]
    for r in rows:
        md.append("| %s | %s | %s | %s | %s | %s | %s:%s | %s |" % (
            r["id"], r["group"], r["kind"], frlib.excerpt(r["section"], 40), ", ".join(r["keywords"]),
            ", ".join(r["dep"]), os.path.basename(r["file"]), ",".join(map(str, r["lines"][:3])),
            r["excerpt"].replace("|", "/")))
    if a.out_md:
        frlib.write(a.out_md, "\n".join(md) + "\n")
        print("Đã ghi", a.out_md)
    print("Số mục:", counts)


if __name__ == "__main__":
    main()
