#!/usr/bin/env python3
"""Bước 2 — Dựng chuỗi sửa đổi giữa các mục nguồn từ những dấu ghi trong register.

Các dấu được nhận ra (register đang dùng nhiều kiểu khác nhau):
  trong mục X:  **[Amended … Y …]**  /  [Amended: … Y]  /  [Clarified … Y]  /  [Added … Y]
                → X bị Y sửa / làm rõ / bổ sung
  trong mục X:  AMENDED by Y and Z                     → X bị Y, Z sửa
  trong mục Y:  supersedes X / amends X / (amends …X)  → X bị Y thay / sửa
  trong mục X:  superseded by Y                        → X bị Y thay
  trong mục Y:  "X … is amended / are superseded"        → X bị Y sửa / thay

Tool chỉ liệt kê cạnh tìm được và vị trí dấu. Câu nào hiện hành, câu nào bị thay là do agent
đọc nội dung và xác nhận ở bước 2 (một DEC "amend" thường chỉ sửa một phần của mục cũ).

Cách dùng (từ gốc repo):
  python3 .../lineage.py --index <index.json> [--scan <scan.json>] --out-md <lineage.md> --out-json <lineage.json>
Có --scan thì chỉ in các cạnh chạm tới ít nhất một mục trong bảng nguồn của module.
"""
import argparse
import os
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frlib  # noqa: E402

BRACKET = re.compile(r"\[(Amended|Clarified|Added|Updated)\b([^\]]*)\]", re.I)
AMENDED_BY = re.compile(r"AMENDED by ([^.\n:]*)")
FORWARD = re.compile(r"\b(supersedes|supersede|amends|amend)\b([^.\n;]{0,120})", re.I)
PASSIVE = re.compile(r"([^.\n]{0,80}?)\b(?:is|are|was|were)\s+(amended|superseded)\b", re.I)
SUPERSEDED_BY = re.compile(r"\bsuperseded by\b([^.\n;|]{0,80})", re.I)


def edges_of(uid, text):
    """Trả về list (target, by, kind, evidence)."""
    out = []
    for m in BRACKET.finditer(text):
        kind = m.group(1).lower()
        for y in frlib.find_ids(m.group(2)):
            if y != uid:
                out.append((uid, y, kind, m.group(0)))
    for m in AMENDED_BY.finditer(text):
        for y in frlib.find_ids(m.group(1)):
            if y != uid:
                out.append((uid, y, "amended", m.group(0)))
    for m in SUPERSEDED_BY.finditer(text):
        for y in frlib.find_ids(m.group(1)):
            if y != uid:
                out.append((uid, y, "superseded", m.group(0)))
    for m in PASSIVE.finditer(text):
        for x in frlib.find_ids(m.group(1)):
            if x != uid:
                out.append((x, uid, m.group(2).lower(), m.group(0)))
    for m in FORWARD.finditer(text):
        verb = m.group(1).lower()
        if verb.startswith("supersede") and "superseded" in m.group(0).lower():
            continue
        for x in frlib.find_ids(m.group(2)):
            if x != uid:
                out.append((x, uid, "superseded" if verb.startswith("supersede") else "amended", m.group(0)))
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--index", required=True)
    ap.add_argument("--scan", help="bảng nguồn JSON từ scan_sources.py")
    ap.add_argument("--out-md")
    ap.add_argument("--out-json")
    a = ap.parse_args()
    units = frlib.load_json(a.index)["units"]
    scope = None
    if a.scan:
        scope = {r["id"] for r in frlib.load_json(a.scan)["rows"]}
    edges = []
    seen = set()
    for uid, u in units.items():
        for e in edges_of(uid, u["text"]):
            k = e[:3]
            if k in seen:
                continue
            seen.add(k)
            edges.append({"target": e[0], "by": e[1], "kind": e[2], "evidence": frlib.excerpt(e[3], 160),
                          "found_in": uid})
    if scope is not None:
        edges = [e for e in edges if e["target"] in scope or e["by"] in scope]
    edges.sort(key=lambda e: (e["target"], e["by"]))
    chains = {}
    for e in edges:
        chains.setdefault(e["target"], []).append(e["by"])
    if a.out_json:
        frlib.dump_json(a.out_json, {"edges": edges, "chains": chains})
    md = ["# Chuỗi sửa đổi (do tool phát hiện, agent phải xác nhận)", "",
          "| Mục bị tác động | Bởi | Kiểu | Dấu tìm thấy ở | Trích dấu |", "|---|---|---|---|---|"]
    for e in edges:
        md.append("| %s | %s | %s | %s | %s |" % (e["target"], e["by"], e["kind"], e["found_in"],
                                              e["evidence"].replace("|", "/")))
    md += ["", "Tổng: %d cạnh, %d mục bị tác động." % (len(edges), len(chains))]
    if a.out_md:
        frlib.write(a.out_md, "\n".join(md) + "\n")
        print("Đã ghi", a.out_md)
    print("Cạnh:", len(edges), "· mục bị tác động:", len(chains))


if __name__ == "__main__":
    main()
