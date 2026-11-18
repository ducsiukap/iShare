#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_puml.py - sinh mã PlantUML của sơ đồ lớp phân tích từ các bảng trong EC-Mxx.md.

Sơ đồ luôn được sinh từ bảng (mục 2.2, 2.3, 3.3, 3.4) để không lệch với bảng.
  python3 gen_puml.py --ec EC-M05.md              # in ra màn hình
  python3 gen_puml.py --ec EC-M05.md --inplace    # ghi vào giữa <!-- BEGIN:PUML --> và <!-- END:PUML -->
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdtab  # noqa: E402
from check_ec import load_ec  # noqa: E402


def build(d):
    mod = d["module"]
    out = ["@startuml", "hide circle", "hide methods", "skinparam classAttributeIconSize 0", ""]
    attrs = {}
    for r in d["rows"]["2.3"]:
        mark = "/" if r["Tính chất"] == "Dẫn xuất" else ""
        attrs.setdefault(r["Lớp"], []).append("  -%s%s" % (mark, r["Thuộc tính"]))
    for r in d["rows"]["2.2"]:
        st = ""
        if r["Sở hữu"] != mod and mod != "SYS":
            st = " <<%s>>" % r["Sở hữu"]
        elif r["Nhóm"] == "Thống kê":
            st = " <<stat>>"
        out.append("class %s%s {" % (r["Lớp"], st))
        out.extend(attrs.get(r["Lớp"], []))
        out.append("}")
    out.append("")
    # Khi cùng hai đầu có nhiều quan hệ, vẽ hai nhánh 1-n của từng lớp liên kết
    # để PlantUML không gắn các lớp liên kết vào cùng một đường quan hệ.
    association_rows = []
    pair_counts = {}
    for r in d["rows"]["3.3"]:
        pair = mdtab.split_pair(r["Tách từ quan hệ n-n"])
        if pair:
            association_rows.append((pair, r["Lớp liên kết"]))
            key = frozenset(pair)
            pair_counts[key] = pair_counts.get(key, 0) + 1
    direct_pairs = {frozenset((r["Lớp A"], r["Lớp B"])) for r in d["rows"]["3.4"]}
    skip = set()
    for pair, lc in association_rows:
        key = frozenset(pair)
        if pair_counts[key] > 1 or key in direct_pairs:
            continue
        out.append("(%s, %s) .. %s" % (pair[0], pair[1], lc))
        for p in pair:
            skip.add(frozenset((lc, p)))
    for r in d["rows"]["3.4"]:
        a, b, kind, main = r["Lớp A"], r["Lớp B"], r["Loại"], r["Bên chính"]
        ma, mb = r["Bội số A"], r["Bội số B"]
        if kind == "Liên kết" and frozenset((a, b)) in skip:
            continue
        if kind == "Kế thừa":
            child = b if main == a else a
            out.append("%s <|-- %s" % (main, child))
        elif kind == "Phụ thuộc":
            user = b if main == a else a
            out.append("%s ..> %s" % (user, main))
        elif kind in ("Hợp thành", "Kết tập"):
            sym = "*--" if kind == "Hợp thành" else "o--"
            if main == a:
                out.append('%s "%s" %s "%s" %s' % (a, ma, sym, mb, b))
            else:
                out.append('%s "%s" %s "%s" %s' % (b, mb, sym, ma, a))
        else:
            out.append('%s "%s" -- "%s" %s' % (a, ma, mb, b))
    out += ["", "@enduml"]
    return "\n".join(out)


def main():
    mdtab.utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--ec", required=True)
    ap.add_argument("--inplace", action="store_true")
    a = ap.parse_args()
    d = load_ec(a.ec)
    code = "```plantuml\n" + build(d) + "\n```"
    if a.inplace:
        text, ok = mdtab.replace_block(d["text"], "PUML", code)
        if not ok:
            print("ERROR: không thấy cặp <!-- BEGIN:PUML --> ... <!-- END:PUML --> trong tệp")
            sys.exit(1)
        mdtab.write(a.ec, text)
        print("Đã ghi sơ đồ vào %s" % a.ec)
    else:
        print(code)


if __name__ == "__main__":
    main()
