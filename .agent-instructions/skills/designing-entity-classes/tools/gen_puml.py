#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""gen_puml.py - sinh sơ đồ lớp thiết kế của CD-Mxx.md từ các bảng (mục 1, 2.1, 2.2, 3.1, 3.2, 4).

Ghi mã PlantUML vào tệp riêng diagrams/<mã tài liệu>.puml cạnh tài liệu, render thành diagrams/<mã tài liệu>.png,
và đặt ảnh (không phải mã) vào mục 5 của tài liệu, giữa <!-- BEGIN:DIAGRAM --> và <!-- END:DIAGRAM -->.
Không sửa tay tệp .puml hay ảnh; muốn đổi sơ đồ thì sửa bảng rồi chạy lại.

  python3 gen_puml.py --cd CD-M05.md                 # ghi .puml, render .png, cập nhật mục 5
  python3 gen_puml.py --cd CD-M05.md --no-render     # chỉ ghi .puml và cập nhật mục 5
  python3 gen_puml.py --cd CD-M05.md --print         # chỉ in mã PlantUML
  python3 gen_puml.py --cd CD-M05.md --server https://www.plantuml.com/plantuml

Render cần một trong: java + plantuml.jar (tools/vendor/ của analyzing-entity-classes hoặc biến PLANTUML_JAR),
lệnh plantuml, hoặc --server. Trả mã thoát 2 khi không render được (tệp .puml vẫn được ghi).
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
    ap.add_argument("--print", action="store_true", help="chỉ in mã PlantUML, không ghi tệp")
    ap.add_argument("--no-render", action="store_true", help="không render PNG")
    ap.add_argument("--server", help="URL máy chủ PlantUML để render (gửi nội dung sơ đồ lên máy chủ đó)")
    ap.add_argument("--inplace", action="store_true", help=argparse.SUPPRESS)  # giữ cho lệnh cũ, không còn tác dụng
    a = ap.parse_args()
    d = load_cd(a.cd)
    code = build(d)
    if a.print:
        print(code)
        return
    doc_id = mdtab.doc_id_of(d["fm"], a.cd)
    ok, msgs = mdtab.write_diagram(a.cd, doc_id, code, os.path.dirname(os.path.abspath(__file__)),
                                   render=not a.no_render, server=a.server)
    text, found = mdtab.replace_block(d["text"], "DIAGRAM",
                                      mdtab.diagram_markdown(doc_id, "Sơ đồ lớp thiết kế — %s" % doc_id, "gen_puml.py"))
    if not found:
        print("ERROR: không thấy cặp <!-- BEGIN:DIAGRAM --> ... <!-- END:DIAGRAM --> ở mục 5 của tài liệu")
        sys.exit(1)
    if text != d["text"]:
        mdtab.write(a.cd, text)
    for m in msgs:
        print(m)
    sys.exit(0 if ok else 2)


if __name__ == "__main__":
    main()
