#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_puml.py - sinh sơ đồ lớp phân tích của EC-Mxx.md từ các bảng (mục 2.2, 2.3, 3.3, 3.4).

Ghi mã PlantUML vào tệp riêng diagrams/<mã tài liệu>.puml cạnh tài liệu, render thành diagrams/<mã tài liệu>.png,
và đặt ảnh (không phải mã) vào mục 4 của tài liệu, giữa <!-- BEGIN:DIAGRAM --> và <!-- END:DIAGRAM -->.
Sơ đồ luôn được sinh từ bảng để không lệch với bảng; không sửa tay tệp .puml hay ảnh.

  python3 gen_puml.py --ec EC-M05.md                 # ghi .puml, render .png, cập nhật mục 4
  python3 gen_puml.py --ec EC-M05.md --no-render     # chỉ ghi .puml và cập nhật mục 4
  python3 gen_puml.py --ec EC-M05.md --print         # chỉ in mã PlantUML ra màn hình
  python3 gen_puml.py --ec EC-M05.md --server https://www.plantuml.com/plantuml   # render qua máy chủ PlantUML

Render cần một trong: java + plantuml.jar (tools/vendor/ hoặc biến PLANTUML_JAR), lệnh plantuml, hoặc --server.
Trả mã thoát 2 khi không render được (tệp .puml vẫn được ghi).
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
    # lớp liên kết vẽ theo ký pháp association class, như sơ đồ phân tích của case study
    skip = set()
    for r in d["rows"]["3.3"]:
        pair = mdtab.split_pair(r["Tách từ quan hệ n-n"])
        if not pair:
            continue
        lc = r["Lớp liên kết"]
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
    ap.add_argument("--print", action="store_true", help="chỉ in mã PlantUML, không ghi tệp")
    ap.add_argument("--no-render", action="store_true", help="không render PNG")
    ap.add_argument("--server", help="URL máy chủ PlantUML để render (gửi nội dung sơ đồ lên máy chủ đó)")
    ap.add_argument("--inplace", action="store_true", help=argparse.SUPPRESS)  # giữ cho lệnh cũ, không còn tác dụng
    a = ap.parse_args()
    d = load_ec(a.ec)
    code = build(d)
    if a.print:
        print(code)
        return
    doc_id = mdtab.doc_id_of(d["fm"], a.ec)
    ok, msgs = mdtab.write_diagram(a.ec, doc_id, code, os.path.dirname(os.path.abspath(__file__)),
                                   render=not a.no_render, server=a.server)
    text, found = mdtab.replace_block(d["text"], "DIAGRAM",
                                      mdtab.diagram_markdown(doc_id, "Sơ đồ lớp phân tích — %s" % doc_id, "gen_puml.py"))
    if not found:
        print("ERROR: không thấy cặp <!-- BEGIN:DIAGRAM --> ... <!-- END:DIAGRAM --> ở mục 4 của tài liệu")
        sys.exit(1)
    if text != d["text"]:
        mdtab.write(a.ec, text)
    for m in msgs:
        print(m)
    sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()
