#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""build_schema.py - dựng lược đồ cuối (mục 6) của DB-Mxx.md từ các bảng của từng bước.

Lược đồ cuối = bảng ở mục 1 trừ bảng bị loại (5.2); cột = cột từ thuộc tính (2.1) + khóa ngoại (4.2)
trừ cột bị loại (5.1); khóa chính lấy từ 4.1. Sinh luôn mã PlantUML của sơ đồ quan hệ.

  python3 build_schema.py --db DB-M05.md              # in ra màn hình
  python3 build_schema.py --db DB-M05.md --inplace    # ghi vào giữa <!-- BEGIN:SCHEMA --> ... <!-- END:SCHEMA -->
                                                      # và <!-- BEGIN:PUML --> ... <!-- END:PUML -->
Luôn chạy lại sau khi sửa bất kỳ bảng nào ở mục 1–5, để mục 6 không lệch.
"""
import argparse
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdtab  # noqa: E402
from check_db import load_db, final_schema, REF_RE  # noqa: E402


def schema_table(schema):
    out = ["| Bảng | Cột | Kiểu | Khóa | Null | Duy nhất | Tham chiếu |", "|---|---|---|---|---|---|---|"]
    for name, cols in schema:
        for c in cols:
            out.append("| %s | %s | %s | %s | %s | %s | %s |" % (
                name, c["Cột"], c["Kiểu"], c["Khóa"] or "—", c["Null"], c["Duy nhất"], c["Tham chiếu"] or "—"))
    return "\n".join(out)


def puml(d, schema):
    ext = {r["Bảng ngoài"]: r["Module sở hữu"] for r in d["rows"]["7.1"]}
    out = ["@startuml", "hide circle", "skinparam linetype ortho", ""]
    names = set(n for n, _ in schema)
    lines = []
    used_ext = set()
    for name, cols in schema:
        out.append("entity %s {" % name)
        pk = [c for c in cols if "PK" in c["Khóa"]]
        rest = [c for c in cols if "PK" not in c["Khóa"]]
        for c in pk:
            fk = " <<FK>>" if "FK" in c["Khóa"] else ""
            out.append("  * %s : %s <<PK>>%s" % (c["Cột"], c["Kiểu"], fk))
        out.append("  --")
        for c in rest:
            req = "* " if c["Null"] == "Không" else ""
            fk = " <<FK>>" if "FK" in c["Khóa"] else ""
            out.append("  %s%s : %s%s" % (req, c["Cột"], c["Kiểu"], fk))
        out.append("}")
        for c in cols:
            m = REF_RE.match(c["Tham chiếu"] or "")
            if not m:
                continue
            target = m.group(1)
            if target not in names:
                used_ext.add(target)
            left = "|o" if c["Null"] == "Có" else "||"
            right = "o|" if (c["Duy nhất"] == "Có" or "PK" in c["Khóa"]) else "o{"
            lines.append("%s %s--%s %s : %s" % (target, left, right, name, c["Cột"]))
    for t in sorted(used_ext):
        out.append("entity %s <<%s>> {" % (t, ext.get(t, "ngoài")))
        out.append("}")
    out.append("")
    out.extend(lines)
    out += ["", "@enduml"]
    return "\n".join(out)


def main():
    mdtab.utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True)
    ap.add_argument("--inplace", action="store_true")
    a = ap.parse_args()
    d = load_db(a.db)
    schema = final_schema(d)
    table = schema_table(schema)
    code = "```plantuml\n" + puml(d, schema) + "\n```"
    if a.inplace:
        text, ok1 = mdtab.replace_block(d["text"], "SCHEMA", table)
        text, ok2 = mdtab.replace_block(text, "PUML", code)
        if not (ok1 and ok2):
            print("ERROR: thiếu cặp đánh dấu <!-- BEGIN:SCHEMA --> / <!-- BEGIN:PUML --> trong tệp")
            sys.exit(1)
        mdtab.write(a.db, text)
        print("Đã ghi lược đồ cuối (%d bảng) và sơ đồ vào %s" % (len(schema), a.db))
    else:
        print(table)
        print()
        print(code)


if __name__ == "__main__":
    main()
