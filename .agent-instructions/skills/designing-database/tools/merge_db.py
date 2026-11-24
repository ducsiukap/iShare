#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""merge_db.py - kiểm kê qua các DB-Mxx.md và dựng bản nháp gộp cơ sở dữ liệu toàn hệ thống.

  python3 merge_db.py --dir <thư mục db> --list
      Liệt kê gọn các bảng đã có (bảng, module, khóa chính và kiểu) để module đang làm tham chiếu đúng.
  python3 merge_db.py --dir <thư mục db> --out-md .work/merge-db.md
      Dựng lược đồ hợp nhất từ lược đồ cuối (mục 6.1) của từng module và danh sách điểm lệch
      cho lượt gộp hệ thống (steps/90-system-merge.md).

Tool chỉ liệt kê điểm lệch, không tự quyết định.
"""
import argparse
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdtab  # noqa: E402
from check_db import load_db, final_schema, REF_RE  # noqa: E402


def md_table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join(["---"] * len(header)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(x if x else "—" for x in r) + " |")
    return "\n".join(out)


def collect(docs):
    tables = {}  # name -> [(mod, cols)]
    for d in docs:
        for name, cols in final_schema(d):
            tables.setdefault(name, []).append((d["module"], cols))
    return tables


def find_issues(docs, tables):
    issues = []
    pk = {}
    for name, lst in sorted(tables.items()):
        if len(lst) > 1:
            issues.append(("Bảng khai ở nhiều module", name, "%s có ở: %s" % (name, ", ".join(m for m, _ in lst))))
        for c in lst[0][1]:
            if "PK" in c["Khóa"]:
                pk.setdefault(name, {})[c["Cột"]] = c["Kiểu"]
    for name, lst in sorted(tables.items()):
        for mod, cols in lst:
            for c in cols:
                m = REF_RE.match(c["Tham chiếu"] or "")
                if not m:
                    continue
                rt, rc = m.group(1), m.group(2)
                if rt not in tables:
                    issues.append(("Khóa ngoại trỏ tới bảng chưa có", "%s.%s" % (name, c["Cột"]),
                                   "%s (%s) tham chiếu %s nhưng chưa module nào khai bảng này" % (name, mod, rt)))
                elif rc not in pk.get(rt, {}):
                    issues.append(("Khóa ngoại không trỏ vào khóa chính", "%s.%s" % (name, c["Cột"]),
                                   "%s(%s) không phải khóa chính của %s" % (rt, rc, rt)))
                elif pk[rt][rc] != c["Kiểu"]:
                    issues.append(("Khóa ngoại lệch kiểu", "%s.%s" % (name, c["Cột"]),
                                   "kiểu %s, trong khi %s(%s) kiểu %s" % (c["Kiểu"], rt, rc, pk[rt][rc])))
    for d in docs:
        for r in d["rows"]["7.1"]:
            t, owner = r["Bảng ngoài"], r["Module sở hữu"]
            owners = [m for m, _ in tables.get(t, [])]
            if not owners:
                removed = any(t in set(x["Bảng"] for x in o["rows"]["5.2"]) for o in docs)
                why = "bảng này đã bị loại ở bước 5 của module sở hữu" if removed else "chưa module nào khai bảng này"
                issues.append(("Bảng ngoài không tồn tại", t, "%s dùng %s của %s nhưng %s" % (d["module"], t, owner, why)))
            elif owner not in owners:
                issues.append(("Lệch module sở hữu bảng", t, "%s ghi %s là của %s, thực tế ở %s"
                               % (d["module"], t, owner, ", ".join(owners))))
        for r in d["rows"]["7.2"]:
            t, c = r["Bảng của module khác"], r["Cột"]
            have = any(x["Cột"] == c for _, cols in tables.get(t, []) for x in cols)
            status = "đã có" if have else "CHƯA có"
            issues.append(("Khóa ngoại đề nghị cho module khác", "%s.%s" % (t, c),
                           "%s đề nghị %s.%s → %s (quan hệ %s): bảng đích %s cột này"
                           % (d["module"], t, c, r["Tham chiếu"], r["Từ quan hệ"], status)))
    by_col = {}
    for name, lst in tables.items():
        for c in lst[0][1]:
            if not c["Khóa"]:
                by_col.setdefault(c["Cột"], []).append(name)
    for col, names in sorted(by_col.items()):
        if len(names) > 1:
            issues.append(("Cột cùng tên ở nhiều bảng (xét trùng lặp)", col, ", ".join(sorted(names))))
    return issues


def render_list(tables):
    rows = []
    for name in sorted(tables):
        mod, cols = tables[name][0]
        pk = ", ".join("%s : %s" % (c["Cột"], c["Kiểu"]) for c in cols if "PK" in c["Khóa"])
        rows.append([name, ", ".join(m for m, _ in tables[name]), pk, ", ".join(c["Cột"] for c in cols if "PK" not in c["Khóa"])])
    return md_table(["Bảng", "Module", "Khóa chính : kiểu", "Các cột khác"], rows)


def render_merge(docs, tables, issues):
    out = ["# Bản nháp gộp cơ sở dữ liệu toàn hệ thống", "",
           "Sinh bởi merge_db.py. Đây là dữ liệu để làm lượt gộp, chưa phải DB-SYS.md.", "", "## Tài liệu nguồn", ""]
    out.append(md_table(["Tài liệu", "Module", "Phiên bản", "Trạng thái"],
                        [[d["fm"].get("ma_tai_lieu", ""), d["module"], d["fm"].get("phien_ban", ""),
                          d["fm"].get("trang_thai", "")] for d in docs]))
    out += ["", "## Điểm lệch cần quyết định (%d)" % len(issues), ""]
    out.append(md_table(["#", "Loại", "Đối tượng", "Mô tả"], [[str(i + 1), k, o, m] for i, (k, o, m) in enumerate(issues)]))
    out += ["", "## Lược đồ hợp nhất", ""]
    rows = []
    for name in sorted(tables):
        for mod, cols in tables[name]:
            for c in cols:
                rows.append([name, c["Cột"], c["Kiểu"], c["Khóa"], c["Null"], c["Duy nhất"], c["Tham chiếu"], mod])
    out.append(md_table(["Bảng", "Cột", "Kiểu", "Khóa", "Null", "Duy nhất", "Tham chiếu", "Module"], rows))
    out += ["", "## Cột và bảng đã loại ở từng module", ""]
    rows = []
    for d in docs:
        for r in d["rows"]["5.1"]:
            rows.append([d["module"], r["Bảng"], r["Cột"], r["Loại dư thừa"], r["Cách có lại giá trị"]])
        for r in d["rows"]["5.2"]:
            rows.append([d["module"], r["Bảng"], "(cả bảng)", "—", r["Lý do"]])
    out.append(md_table(["Module", "Bảng", "Cột", "Loại dư thừa", "Cách có lại giá trị / lý do"], rows))
    out += ["", "## Dẫn xuất nhưng giữ lại ở từng module", ""]
    rows = []
    for d in docs:
        for r in d["rows"]["5.3"]:
            rows.append([d["module"], r["Bảng"], r["Cột"], r["Lý do giữ"], r["Nguồn"]])
    out.append(md_table(["Module", "Bảng", "Cột", "Lý do giữ", "Nguồn"], rows))
    return "\n".join(out) + "\n"


def main():
    mdtab.utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="thư mục chứa các DB-Mxx.md")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--exclude", help="mã module bỏ qua, ngăn bởi dấu phẩy")
    ap.add_argument("--out-md")
    a = ap.parse_args()
    docs = [load_db(p) for p in sorted(glob.glob(os.path.join(a.dir, "DB-M*.md")))]
    if a.exclude:
        ex = set(x.strip() for x in a.exclude.split(","))
        docs = [d for d in docs if d["module"] not in ex]
    if not docs:
        print("Chưa có tệp DB-Mxx.md nào trong %s" % a.dir)
        return
    tables = collect(docs)
    if a.list:
        print(render_list(tables))
        return
    issues = find_issues(docs, tables)
    text = render_merge(docs, tables, issues)
    if a.out_md:
        os.makedirs(os.path.dirname(os.path.abspath(a.out_md)), exist_ok=True)
        mdtab.write(a.out_md, text)
        print("Đã ghi %s (%d bảng, %d điểm lệch)" % (a.out_md, len(tables), len(issues)))
    else:
        print(text)


if __name__ == "__main__":
    main()
