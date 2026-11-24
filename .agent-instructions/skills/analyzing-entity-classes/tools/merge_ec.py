#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""merge_ec.py - kiểm kê lớp qua các EC-Mxx.md và dựng bản nháp gộp hệ thống.

  python3 merge_ec.py --dir <thư mục ec> --list
      Liệt kê gọn các lớp đã có (lớp, module sở hữu, thuộc tính). Chạy trước bước 2 của mỗi module
      để dùng lại đúng tên lớp đã có.
  python3 merge_ec.py --dir <thư mục ec> --out-md .work/merge-ec.md
      Dựng bảng hợp nhất (lớp, thuộc tính, lớp liên kết, quan hệ) và danh sách điểm lệch cần quyết định
      cho lượt gộp hệ thống (steps/90-system-merge.md).

Tool không tự quyết định điểm lệch nào; nó chỉ liệt kê. Trả mã thoát 0.
"""
import argparse
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdtab  # noqa: E402
from check_ec import load_ec  # noqa: E402


def load_all(folder):
    docs = []
    for p in sorted(glob.glob(os.path.join(folder, "EC-M*.md"))):
        docs.append(load_ec(p))
    return docs


def norm(name):
    n = name.lower()
    return n[:-1] if n.endswith("s") else n


def collect(docs):
    classes = {}   # name -> {"owners": [(mod,row)], "refs": [(mod,row)]}
    attrs = {}     # (class, attr) -> [(mod,row)]   thuộc tính được định nghĩa (Nguồn nêu, Đề xuất)
    refs = {}      # (class, attr) -> [(mod,row)]   thuộc tính lớp ngoài mà module khác đọc hoặc ghi (Tham chiếu)
    rels, links = [], []
    for d in docs:
        mod = d["module"]
        for r in d["rows"]["2.2"]:
            e = classes.setdefault(r["Lớp"], {"owners": [], "refs": []})
            (e["owners"] if r["Sở hữu"] == mod else e["refs"]).append((mod, r))
        for r in d["rows"]["2.3"]:
            target = refs if r.get("Căn cứ") == "Tham chiếu" else attrs
            target.setdefault((r["Lớp"], r["Thuộc tính"]), []).append((mod, r))
        for r in d["rows"]["3.4"]:
            rels.append((mod, r))
        for r in d["rows"]["3.3"]:
            links.append((mod, r))
    return classes, attrs, refs, rels, links


def find_issues(docs, classes, attrs, refs, rels):
    mods = set(d["module"] for d in docs)
    issues = []
    for c in sorted(classes):
        e = classes[c]
        owners = [m for m, _ in e["owners"]]
        if len(owners) > 1:
            issues.append(("Trùng sở hữu", c, "lớp %s được nhiều module sở hữu: %s" % (c, ", ".join(owners))))
        if not owners:
            claimed = sorted(set(r["Sở hữu"] for _, r in e["refs"]))
            for m in claimed:
                if m in mods:
                    issues.append(("Thiếu ở module sở hữu", c,
                                   "lớp %s được %s tham chiếu là của %s, nhưng EC-%s không có lớp này"
                                   % (c, ", ".join(x for x, _ in e["refs"]), m, m)))
                else:
                    issues.append(("Chưa có module sở hữu", c, "lớp %s ghi là của %s, chưa có EC-%s.md" % (c, m, m)))
            if len(claimed) > 1:
                issues.append(("Lệch module sở hữu", c, "các module ghi chủ khác nhau cho %s: %s" % (c, ", ".join(claimed))))
        for m, r in e["refs"]:
            if owners and r["Sở hữu"] not in owners:
                issues.append(("Lệch module sở hữu", c, "%s ghi %s là của %s, thực tế do %s sở hữu"
                               % (m, c, r["Sở hữu"], ", ".join(owners))))
        vi = sorted(set(r["Tên tiếng Việt"] for _, r in e["owners"] + e["refs"] if not mdtab.is_empty(r["Tên tiếng Việt"])))
        if len(vi) > 1:
            issues.append(("Một lớp nhiều tên tiếng Việt", c, "%s: %s" % (c, " / ".join(vi))))
        groups = sorted(set(r["Nhóm"] for _, r in e["owners"] + e["refs"]))
        if len(groups) > 1:
            issues.append(("Lệch nhóm lớp", c, "%s: %s" % (c, " / ".join(groups))))
    names = sorted(classes)
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            if norm(a) == norm(b):
                issues.append(("Tên gần giống", a, "%s và %s có thể là một lớp" % (a, b)))
    by_vi = {}
    for c, e in classes.items():
        for _, r in e["owners"] + e["refs"]:
            v = r["Tên tiếng Việt"].lower()
            if v and not mdtab.is_empty(v):
                by_vi.setdefault(v, set()).add(c)
    for v, cs in sorted(by_vi.items()):
        if len(cs) > 1:
            issues.append(("Một tên tiếng Việt nhiều lớp", v, "'%s' ứng với các lớp: %s" % (v, ", ".join(sorted(cs)))))
    for (c, a), lst in sorted(attrs.items()):
        if len(lst) > 1:
            kinds = set(r["Tính chất"] for _, r in lst)
            cons = set(r["Ràng buộc nguồn nêu"] for _, r in lst)
            note = "" if len(kinds) == 1 and len(cons) == 1 else " (tính chất hoặc ràng buộc khác nhau)"
            issues.append(("Thuộc tính khai ở nhiều module", "%s.%s" % (c, a),
                           "%s.%s có ở: %s%s" % (c, a, ", ".join(m for m, _ in lst), note)))
    for (c, a), lst in sorted(refs.items()):
        if (c, a) in attrs:
            continue
        e = classes.get(c, {"owners": []})
        owners = [m for m, _ in e["owners"]]
        users = ", ".join(m for m, _ in lst)
        if owners:
            issues.append(("Thuộc tính được tham chiếu nhưng module sở hữu chưa khai", "%s.%s" % (c, a),
                           "%s đọc hoặc ghi %s.%s nhưng EC-%s không có thuộc tính này" % (users, c, a, owners[0])))
        else:
            issues.append(("Thuộc tính tham chiếu tới lớp chưa có module sở hữu", "%s.%s" % (c, a),
                           "%s đọc hoặc ghi %s.%s" % (users, c, a)))
    proposed = [(c, a, m) for (c, a), lst in sorted(attrs.items()) for m, r in lst if r.get("Căn cứ") == "Đề xuất"]
    if proposed:
        issues.append(("Thuộc tính đề xuất (để rà lại khi gộp)", "%d thuộc tính" % len(proposed),
                       "; ".join("%s.%s (%s)" % x for x in proposed)))
    by_class = {}
    for (c, a) in attrs:
        by_class.setdefault(c, []).append(a)
    for c, lst in sorted(by_class.items()):
        low = {}
        for a in lst:
            low.setdefault(a.lower(), []).append(a)
        for k, v in low.items():
            if len(v) > 1:
                issues.append(("Tên thuộc tính gần giống", c, "%s: %s" % (c, ", ".join(v))))
    pairs = {}
    for m, r in rels:
        key = frozenset((r["Lớp A"], r["Lớp B"]))
        pairs.setdefault(key, []).append((m, r))
    for key, lst in sorted(pairs.items(), key=lambda kv: sorted(kv[0])):
        if len(set(m for m, _ in lst)) > 1:
            sigs = set()
            for m, r in lst:
                if r["Lớp A"] <= r["Lớp B"]:
                    sigs.add((r["Loại"], r["Bội số A"], r["Bội số B"], r["Bên chính"]))
                else:
                    sigs.add((r["Loại"], r["Bội số B"], r["Bội số A"], r["Bên chính"]))
            what = "khớp nhau, giữ một" if len(sigs) == 1 else "KHÁC nhau về loại, bội số hoặc bên chính"
            issues.append(("Quan hệ khai ở nhiều module", " – ".join(sorted(key)),
                           "%s: %s (%s)" % (" – ".join(sorted(key)), ", ".join("%s:%s" % (m, r["ID"]) for m, r in lst), what)))
    return issues


def md_table(header, rows):
    out = ["| " + " | ".join(header) + " |", "|" + "|".join(["---"] * len(header)) + "|"]
    for r in rows:
        out.append("| " + " | ".join(x if x else "—" for x in r) + " |")
    return "\n".join(out)


def render_list(classes, attrs):
    rows = []
    for c in sorted(classes):
        e = classes[c]
        owner = ", ".join(m for m, _ in e["owners"]) or "(chưa có: " + ", ".join(sorted(set(r["Sở hữu"] for _, r in e["refs"]))) + ")"
        vi = next((r["Tên tiếng Việt"] for _, r in e["owners"] + e["refs"]), "")
        al = sorted(set(a for (cc, a) in attrs if cc == c))
        rows.append([c, vi, owner, ", ".join(m for m, _ in e["refs"]), ", ".join(al)])
    return md_table(["Lớp", "Tên tiếng Việt", "Module sở hữu", "Module tham chiếu", "Thuộc tính đã có"], rows)


def render_merge(docs, classes, attrs, refs, rels, links, issues):
    out = ["# Bản nháp gộp lớp thực thể toàn hệ thống", "",
           "Sinh bởi merge_ec.py. Đây là dữ liệu để làm lượt gộp, chưa phải EC-SYS.md.", "",
           "## Tài liệu nguồn", ""]
    out.append(md_table(["Tài liệu", "Module", "Phiên bản", "Trạng thái"],
                        [[d["fm"].get("ma_tai_lieu", ""), d["module"], d["fm"].get("phien_ban", ""),
                          d["fm"].get("trang_thai", "")] for d in docs]))
    out += ["", "## Điểm lệch cần quyết định (%d)" % len(issues), ""]
    out.append(md_table(["#", "Loại", "Đối tượng", "Mô tả"],
                        [[str(i + 1), k, o, m] for i, (k, o, m) in enumerate(issues)]))
    out += ["", "## Lớp (hợp nhất)", ""]
    rows = []
    for c in sorted(classes):
        e = classes[c]
        src = e["owners"] or e["refs"]
        r = src[0][1]
        owner = ", ".join(m for m, _ in e["owners"]) or r["Sở hữu"]
        rows.append([c, r["Tên tiếng Việt"], r["Nhóm"], owner, r["Mô tả"],
                     ", ".join(m for m, _ in e["refs"])])
    out.append(md_table(["Lớp", "Tên tiếng Việt", "Nhóm", "Sở hữu", "Mô tả", "Module tham chiếu"], rows))
    out += ["", "## Thuộc tính (hợp nhất)", ""]
    rows = []
    for (c, a) in sorted(attrs):
        lst = attrs[(c, a)]
        r = lst[0][1]
        rows.append([c, a, r["Tên tiếng Việt"], r["Tính chất"], r.get("Căn cứ", ""), r["Ràng buộc nguồn nêu"],
                     "; ".join("%s: %s" % (m, x["Nguồn"]) for m, x in lst), r.get("Ghi chú", "")])
    out.append(md_table(["Lớp", "Thuộc tính", "Tên tiếng Việt", "Tính chất", "Căn cứ", "Ràng buộc nguồn nêu", "Nguồn",
                         "Ghi chú"], rows))
    out += ["", "## Thuộc tính được module khác tham chiếu", ""]
    out.append(md_table(["Lớp", "Thuộc tính", "Module tham chiếu", "Module sở hữu đã khai?", "Ghi chú"],
                        [[c, a, ", ".join(m for m, _ in lst), "Có" if (c, a) in attrs else "Chưa",
                          "; ".join("%s: %s" % (m, r.get("Ghi chú", "")) for m, r in lst)]
                         for (c, a), lst in sorted(refs.items())]))
    out += ["", "## Lớp liên kết (hợp nhất)", ""]
    out.append(md_table(["Lớp liên kết", "Tách từ quan hệ n-n", "Thuộc tính riêng của liên kết", "Nguồn"],
                        [[r["Lớp liên kết"], r["Tách từ quan hệ n-n"], r["Thuộc tính riêng của liên kết"],
                          "%s: %s" % (m, r["Nguồn"])] for m, r in links]))
    out += ["", "## Quan hệ (hợp nhất, giữ ID của module)", ""]
    out.append(md_table(["ID", "Lớp A", "Bội số A", "Lớp B", "Bội số B", "Dạng", "Loại", "Bên chính", "Căn cứ", "Nguồn"],
                        [[r["ID"], r["Lớp A"], r["Bội số A"], r["Lớp B"], r["Bội số B"], r["Dạng"], r["Loại"],
                          r["Bên chính"], r["Căn cứ"], r["Nguồn"]] for m, r in rels]))
    return "\n".join(out) + "\n"


def main():
    mdtab.utf8_stdout()
    ap = argparse.ArgumentParser()
    ap.add_argument("--dir", required=True, help="thư mục chứa các EC-Mxx.md")
    ap.add_argument("--list", action="store_true", help="chỉ liệt kê lớp đã có")
    ap.add_argument("--exclude", help="mã module bỏ qua (ví dụ module đang làm), ngăn bởi dấu phẩy")
    ap.add_argument("--out-md")
    a = ap.parse_args()
    docs = load_all(a.dir)
    if a.exclude:
        ex = set(x.strip() for x in a.exclude.split(","))
        docs = [d for d in docs if d["module"] not in ex]
    if not docs:
        print("Chưa có tệp EC-Mxx.md nào trong %s" % a.dir)
        return
    classes, attrs, refs, rels, links = collect(docs)
    if a.list:
        print(render_list(classes, attrs))
        return
    issues = find_issues(docs, classes, attrs, refs, rels)
    text = render_merge(docs, classes, attrs, refs, rels, links, issues)
    if a.out_md:
        os.makedirs(os.path.dirname(os.path.abspath(a.out_md)), exist_ok=True)
        mdtab.write(a.out_md, text)
        print("Đã ghi %s (%d lớp, %d thuộc tính, %d quan hệ, %d điểm lệch)"
              % (a.out_md, len(classes), len(attrs), len(rels), len(issues)))
    else:
        print(text)


if __name__ == "__main__":
    main()
