#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""merge_cd.py - kiểm kê qua các CD-Mxx.md và dựng bản nháp gộp thiết kế lớp toàn hệ thống.

  python3 merge_cd.py --dir <thư mục cd> --list
      Liệt kê gọn lớp, kiểu id và kiểu liệt kê đã có, để module đang làm dùng lại cho thống nhất.
  python3 merge_cd.py --dir <thư mục cd> --out-md .work/merge-cd.md
      Dựng bảng hợp nhất và danh sách điểm lệch cho lượt gộp hệ thống (steps/90-system-merge.md).

Tool chỉ liệt kê điểm lệch, không tự quyết định.
"""
import argparse
import glob
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdtab  # noqa: E402
from check_cd import load_cd  # noqa: E402


def md_table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join(["---"] * len(header)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(x if x else "—" for x in r) + " |")
    return "\n".join(out)


def collect(docs):
    classes, attrs, enums, objs, rels, kept = {}, {}, {}, [], [], []
    for d in docs:
        mod = d["module"]
        for r in d["rows"]["1"]:
            e = classes.setdefault(r["Lớp"], {"owners": [], "refs": []})
            (e["owners"] if r["Sở hữu"] == mod else e["refs"]).append((mod, r))
        for r in d["rows"]["2.1"]:
            attrs.setdefault((r["Lớp"], r["Thuộc tính"]), []).append((mod, r))
        for r in d["rows"]["2.2"]:
            enums.setdefault(r["Kiểu"], []).append((mod, r))
        for r in d["rows"]["4"]:
            objs.append((mod, r))
        for r in d["rows"]["3.1"]:
            rels.append((mod, r))
        for r in d["rows"]["3.2"]:
            kept.append((mod, r))
    return classes, attrs, enums, objs, rels, kept


def find_issues(docs, classes, attrs, enums, objs, rels):
    mods = set(d["module"] for d in docs)
    issues = []
    for c in sorted(classes):
        e = classes[c]
        owners = [m for m, _ in e["owners"]]
        if len(owners) > 1:
            issues.append(("Trùng sở hữu", c, "lớp %s được nhiều module sở hữu: %s" % (c, ", ".join(owners))))
        if not owners:
            for m in sorted(set(r["Sở hữu"] for _, r in e["refs"])):
                kind = "Thiếu ở module sở hữu" if m in mods else "Chưa có module sở hữu"
                issues.append((kind, c, "lớp %s ghi là của %s nhưng CD-%s không khai" % (c, m, m)))
    id_types = {}
    for (c, a), lst in attrs.items():
        if a == "id":
            for m, r in lst:
                id_types.setdefault(r["Kiểu"], []).append("%s.%s" % (m, c))
    if len(id_types) > 1:
        issues.append(("Kiểu id không thống nhất", "id", "; ".join("%s: %s" % (t, ", ".join(v)) for t, v in sorted(id_types.items()))))
    for (c, a), lst in sorted(attrs.items()):
        if len(lst) > 1:
            types = sorted(set(r["Kiểu"] for _, r in lst))
            note = "cùng kiểu" if len(types) == 1 else "KHÁC kiểu: " + " / ".join(types)
            issues.append(("Thuộc tính khai ở nhiều module", "%s.%s" % (c, a),
                           "%s.%s có ở %s (%s)" % (c, a, ", ".join(m for m, _ in lst), note)))
    for e, lst in sorted(enums.items()):
        vals = sorted(set(tuple(mdtab.split_list(r["Giá trị"])) for _, r in lst))
        if len(vals) > 1:
            issues.append(("Kiểu liệt kê khác giá trị", e, "%s khai ở %s với các tập giá trị khác nhau"
                           % (e, ", ".join(m for m, _ in lst))))
    owner_of = {c: (e["owners"][0][0] if e["owners"] else "") for c, e in classes.items()}
    names = {}
    for m, r in objs:
        holder = r["Lớp chứa"]
        if owner_of.get(holder) and owner_of[holder] != m:
            issues.append(("Thuộc tính đối tượng đề nghị cho lớp của module khác", "%s.%s" % (holder, r["Thuộc tính"]),
                           "%s đề nghị thêm %s.%s : %s vào lớp của %s (quan hệ %s)"
                           % (m, holder, r["Thuộc tính"], r["Kiểu"], owner_of[holder], r["Quan hệ"])))
        names.setdefault((holder, r["Thuộc tính"]), []).append(m)
    for (h, a), ms in sorted(names.items()):
        if len(ms) > 1:
            issues.append(("Trùng tên thuộc tính đối tượng", "%s.%s" % (h, a), "khai ở: %s" % ", ".join(ms)))
        if (h, a) in attrs:
            issues.append(("Thuộc tính đối tượng trùng tên thuộc tính thường", "%s.%s" % (h, a), ""))
    holds = set((r["Lớp chứa"], r["Kiểu"].rstrip("[]")) for _, r in objs)
    for (h, c) in sorted(holds):
        if h < c and (c, h) in holds:
            issues.append(("Tham chiếu vòng", "%s – %s" % (h, c), "%s và %s chứa lẫn nhau qua các module" % (h, c)))
    pairs = {}
    for m, r in rels:
        pairs.setdefault(frozenset((r["Thành phần"], r["Toàn thể"])), []).append((m, r))
    for key, lst in sorted(pairs.items(), key=lambda kv: sorted(kv[0])):
        if len(set(m for m, _ in lst)) > 1:
            sigs = set((r["Thành phần"], r["Toàn thể"], r["Loại"], r["Dạng"]) for _, r in lst)
            what = "khớp nhau, giữ một" if len(sigs) == 1 else "KHÁC nhau về bên toàn thể, loại hoặc dạng"
            issues.append(("Quan hệ khai ở nhiều module", " – ".join(sorted(key)),
                           "%s (%s)" % (", ".join("%s:%s" % (m, r["ID"]) for m, r in lst), what)))
    return issues


def render_list(classes, attrs, enums):
    rows = []
    for c in sorted(classes):
        e = classes[c]
        owner = ", ".join(m for m, _ in e["owners"]) or "(chưa có)"
        idt = next((r["Kiểu"] for m, r in attrs.get((c, "id"), [])), "")
        al = sorted("%s : %s" % (a, lst[0][1]["Kiểu"]) for (cc, a), lst in attrs.items() if cc == c and a != "id")
        rows.append([c, owner, idt, "; ".join(al)])
    out = [md_table(["Lớp", "Module sở hữu", "Kiểu id", "Thuộc tính : kiểu"], rows), ""]
    out.append(md_table(["Kiểu liệt kê", "Giá trị", "Khai ở"],
                        [[e, lst[0][1]["Giá trị"], ", ".join(m for m, _ in lst)] for e, lst in sorted(enums.items())]))
    return "\n".join(out)


def render_merge(docs, classes, attrs, enums, objs, rels, kept, issues):
    out = ["# Bản nháp gộp thiết kế lớp toàn hệ thống", "",
           "Sinh bởi merge_cd.py. Đây là dữ liệu để làm lượt gộp, chưa phải CD-SYS.md.", "", "## Tài liệu nguồn", ""]
    out.append(md_table(["Tài liệu", "Module", "Phiên bản", "Trạng thái"],
                        [[d["fm"].get("ma_tai_lieu", ""), d["module"], d["fm"].get("phien_ban", ""),
                          d["fm"].get("trang_thai", "")] for d in docs]))
    out += ["", "## Điểm lệch cần quyết định (%d)" % len(issues), ""]
    out.append(md_table(["#", "Loại", "Đối tượng", "Mô tả"], [[str(i + 1), k, o, m] for i, (k, o, m) in enumerate(issues)]))
    out += ["", "## Lớp và id (hợp nhất)", ""]
    rows = []
    for c in sorted(classes):
        e = classes[c]
        r = (e["owners"] or e["refs"])[0][1]
        owner = ", ".join(m for m, _ in e["owners"]) or r["Sở hữu"]
        rows.append([c, r["Nhóm"], owner, r["Lớp cha"], r["id"] if e["owners"] else "(chưa có chủ)", r["Ghi chú"]])
    out.append(md_table(["Lớp", "Nhóm", "Sở hữu", "Lớp cha", "id", "Ghi chú"], rows))
    out += ["", "## Thuộc tính và kiểu (hợp nhất)", ""]
    rows = []
    for (c, a) in sorted(attrs):
        m, r = attrs[(c, a)][0]
        rows.append([c, a, r["Kiểu"], r["Bắt buộc"], r["Ràng buộc"], r["Tính chất"], r["Căn cứ kiểu"],
                     ", ".join(x for x, _ in attrs[(c, a)])])
    out.append(md_table(["Lớp", "Thuộc tính", "Kiểu", "Bắt buộc", "Ràng buộc", "Tính chất", "Căn cứ kiểu", "Khai ở"], rows))
    out += ["", "## Kiểu liệt kê (hợp nhất)", ""]
    out.append(md_table(["Kiểu", "Giá trị", "Dùng ở", "Nguồn"],
                        [[e, lst[0][1]["Giá trị"], "; ".join(r["Dùng ở"] for _, r in lst), lst[0][1]["Nguồn"]]
                         for e, lst in sorted(enums.items())]))
    out += ["", "## Quan hệ thành phần – toàn thể (hợp nhất)", ""]
    out.append(md_table(["ID", "Thành phần", "Toàn thể", "Bội số thành phần", "Bội số toàn thể", "Dạng", "Loại",
                         "Loại ở phân tích", "Căn cứ"],
                        [[r["ID"], r["Thành phần"], r["Toàn thể"], r["Bội số thành phần"], r["Bội số toàn thể"],
                          r["Dạng"], r["Loại"], r["Loại ở phân tích"], r["Căn cứ"]] for _, r in rels]))
    out += ["", "## Quan hệ giữ nguyên (hợp nhất)", ""]
    out.append(md_table(["ID", "Loại", "Lớp", "Lớp đích", "Ghi chú"],
                        [[r["ID"], r["Loại"], r["Lớp"], r["Lớp đích"], r["Ghi chú"]] for _, r in kept]))
    out += ["", "## Thuộc tính đối tượng (hợp nhất)", ""]
    out.append(md_table(["Quan hệ", "Lớp chứa", "Thuộc tính", "Kiểu", "Quy tắc", "Khai ở"],
                        [[r["Quan hệ"], r["Lớp chứa"], r["Thuộc tính"], r["Kiểu"], r["Quy tắc"], m] for m, r in objs]))
    return "\n".join(out) + "\n"


def main():
    mdtab.utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="thư mục chứa các CD-Mxx.md")
    ap.add_argument("--list", action="store_true")
    ap.add_argument("--exclude", help="mã module bỏ qua, ngăn bởi dấu phẩy")
    ap.add_argument("--out-md")
    a = ap.parse_args()
    docs = [load_cd(p) for p in sorted(glob.glob(os.path.join(a.dir, "CD-M*.md")))]
    if a.exclude:
        ex = set(x.strip() for x in a.exclude.split(","))
        docs = [d for d in docs if d["module"] not in ex]
    if not docs:
        print("Chưa có tệp CD-Mxx.md nào trong %s" % a.dir)
        return
    classes, attrs, enums, objs, rels, kept = collect(docs)
    if a.list:
        print(render_list(classes, attrs, enums))
        return
    issues = find_issues(docs, classes, attrs, enums, objs, rels)
    text = render_merge(docs, classes, attrs, enums, objs, rels, kept, issues)
    if a.out_md:
        os.makedirs(os.path.dirname(os.path.abspath(a.out_md)), exist_ok=True)
        mdtab.write(a.out_md, text)
        print("Đã ghi %s (%d lớp, %d thuộc tính, %d quan hệ, %d điểm lệch)"
              % (a.out_md, len(classes), len(attrs), len(rels) + len(kept), len(issues)))
    else:
        print(text)


if __name__ == "__main__":
    main()
