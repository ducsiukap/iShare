#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_puml.py - sinh mã PlantUML của sơ đồ lớp thiết kế từ các bảng trong CD-Mxx.md.

Sơ đồ luôn được sinh từ bảng (mục 1, 2.1, 3.1, 3.2, 4) để không lệch với bảng.
  python3 gen_puml.py --cd CD-M05.md              # in ra màn hình
  python3 gen_puml.py --cd CD-M05.md --inplace    # ghi vào giữa <!-- BEGIN:PUML --> và <!-- END:PUML -->
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdtab  # noqa: E402
from check_cd import load_cd  # noqa: E402


def build(d):
    mod = d["module"]
    out = ["@startuml", "hide circle", "hide methods", "skinparam classAttributeIconSize 0", ""]
    attrs = {}
    for r in d["rows"]["2.1"]:
        mark = "/" if r["Tính chất"] == "Dẫn xuất" else ""
        attrs.setdefault(r["Lớp"], []).append("  -%s%s : %s" % (mark, r["Thuộc tính"], r["Kiểu"]))
    for r in d["rows"]["4"]:
        attrs.setdefault(r["Lớp chứa"], []).append("  -%s : %s" % (r["Thuộc tính"], r["Kiểu"]))
    for r in d["rows"]["1"]:
        st = ""
        if r["Sở hữu"] != mod and mod != "SYS":
            st = " <<%s>>" % r["Sở hữu"]
        elif r["Nhóm"] == "Thống kê":
            st = " <<stat>>"
        out.append("class %s%s {" % (r["Lớp"], st))
        out.extend(attrs.get(r["Lớp"], []))
        out.append("}")
    enums = d["rows"]["2.2"]
    for r in enums:
        out.append("enum %s {" % r["Kiểu"])
        for v in mdtab.split_list(r["Giá trị"]):
            out.append("  " + v)
        out.append("}")
    out.append("")
    for r in d["rows"]["3.1"]:
        sym = "*--" if r["Loại"] == "Hợp thành" else "o--"
        out.append('%s "%s" %s "%s" %s' % (r["Toàn thể"], r["Bội số toàn thể"], sym,
                                           r["Bội số thành phần"], r["Thành phần"]))
    for r in d["rows"]["3.2"]:
        if r["Loại"] == "Kế thừa":
            out.append("%s <|-- %s" % (r["Lớp đích"], r["Lớp"]))
        else:
            out.append("%s ..> %s" % (r["Lớp"], r["Lớp đích"]))
    out += ["", "@enduml"]
    return "\n".join(out)


def main():
    mdtab.utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--cd", required=True)
    ap.add_argument("--inplace", action="store_true")
    a = ap.parse_args()
    d = load_cd(a.cd)
    code = "```plantuml\n" + build(d) + "\n```"
    if a.inplace:
        text, ok = mdtab.replace_block(d["text"], "PUML", code)
        if not ok:
            print("ERROR: không thấy cặp <!-- BEGIN:PUML --> ... <!-- END:PUML --> trong tệp")
            sys.exit(1)
        mdtab.write(a.cd, text)
        print("Đã ghi sơ đồ vào %s" % a.cd)
    else:
        print(code)


if __name__ == "__main__":
    main()
