#!/usr/bin/env python3
"""Kiểm độ phủ hai chiều giữa bảng nguồn và tệp FR (dùng ở bước 4, 5 và 7).

Kiểm:
  COV  mọi mục của bảng nguồn có dòng ở Phụ lục C.1 (thiếu nhóm A là lỗi, nhóm khác là cảnh báo); mục Sở hữu + Hiện hành phải
       được dùng ở đâu đó (ID trong tài liệu, "Chuyển Myy", hoặc "Không áp dụng: lý do");
       mọi nguồn trích ở Phụ lục A phải có ở C.1.
  CRUD thực thể thiếu ô Tạo hoặc Đọc (ô "—").
  STATE trạng thái không có đường vào, dòng chuyển trạng thái không trỏ tới yêu cầu.
  XMOD (khi có --others) phần "Giao tiếp với module khác" có khớp với tệp FR của module kia.

Cách dùng (từ gốc repo):
  python3 .../trace_check.py --fr <FR-Mxx.md> --scan <scan-Mxx.json> [--others <thư mục fr/>]
"""
import argparse
import glob
import os
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frlib  # noqa: E402

out = {"ERROR": [], "WARN": [], "INFO": []}
LABELS = {"Sở hữu", "Phụ thuộc", "Nhắc tới", "Loại"}


def say(level, code, msg):
    out[level].append("%-5s %s  %s" % (level, code, msg))


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fr", required=True)
    ap.add_argument("--scan", required=True)
    ap.add_argument("--others", help="thư mục chứa các tệp FR-Myy.md khác để đối chiếu chéo")
    a = ap.parse_args()
    fr = frlib.parse_fr(frlib.read(a.fr))
    scan = frlib.load_json(a.scan)
    pats = fr["pats"]
    defined = set(fr["defined"]) | set(fr["list44"])
    c1 = {r["src"]: r for r in fr["c1"]}

    # COV
    for r in scan["rows"]:
        if r["id"] not in c1:
            lvl = "ERROR" if r["group"] == "A" else "WARN"
            say(lvl, "COV-01", "nguồn nhóm %s %s chưa có dòng ở C.1 (khớp nhầm thì chạy lại scan với --exclude)" % (r["group"], r["id"]))
    scan_ids = {r["id"] for r in scan["rows"]}
    for src, r in c1.items():
        if r["label"] not in LABELS:
            say("ERROR", "COV-02", "%s: nhãn '%s' không hợp lệ" % (src, r["label"]))
        if src not in scan_ids:
            say("WARN", "COV-03", "%s có ở C.1 nhưng không có trong bảng nguồn của bước 1" % src)
        used = r["used"].strip()
        if r["label"] == "Loại" or re.match(r"^(Bị thay|Trùng)", r["status"]):
            continue
        if r["label"] == "Sở hữu" and r["status"].startswith(("Hiện hành", "Sửa một phần")):
            if used in ("", "—"):
                say("ERROR", "COV-04", "nguồn sở hữu %s chưa được dùng ở đâu (bỏ sót?)" % src)
        if used.startswith("Không áp dụng") and ":" not in used:
            say("ERROR", "COV-05", "%s ghi 'Không áp dụng' nhưng thiếu lý do" % src)
        for i in pats["any"].findall(used):
            if i not in defined:
                say("ERROR", "COV-06", "%s trỏ tới %s nhưng ID này chưa được định nghĩa" % (src, i))
        if r["status"].startswith("Mâu thuẫn"):
            say("WARN", "COV-07", "%s đang ghi Mâu thuẫn: phải có câu hỏi ở B.1 và được giải quyết trước khi chốt" % src)
    cited = set()
    for row in fr["appendix_a"].values():
        cited.update(s for s in row["sources"] if s != "—")
    for s in sorted(cited):
        if s not in c1:
            say("ERROR", "COV-08", "nguồn %s được trích ở Phụ lục A nhưng không có ở C.1" % s)
        elif c1[s]["status"].startswith(("Bị thay", "Trùng")):
            say("ERROR", "COV-09", "nguồn %s được trích nhưng C.1 ghi '%s'" % (s, c1[s]["status"]))
    for src, r in c1.items():
        if r["label"] == "Sở hữu" and r["status"].startswith(("Hiện hành", "Sửa một phần")):
            ids = pats["any"].findall(r["used"])
            if ids and src not in cited:
                say("WARN", "COV-10", "%s ghi dùng ở %s nhưng Phụ lục A của các ID đó không trích %s" % (src, ", ".join(ids), src))

    # CRUD
    for r in fr["crud"]:
        ent, c, rd = r[0], r[1], r[2]
        for name, cell in (("Tạo", c), ("Đọc", rd)):
            if cell.strip() in ("", "—"):
                say("WARN", "CRUD-01", "thực thể '%s' chưa rõ ai %s (ô '—')" % (ent, name.lower()))
        for cell in r[1:5]:
            for i in pats["any"].findall(cell):
                if i not in defined:
                    say("ERROR", "CRUD-02", "CRUD của '%s' trỏ tới %s chưa được định nghĩa" % (ent, i))

    # STATE
    for ent, rows in fr["states"].items():
        froms = {r[0] for r in rows}
        tos = {r[3] for r in rows}
        for s in froms - tos - {"(bắt đầu)"}:
            say("WARN", "STATE-01", "%s: trạng thái '%s' không có đường vào" % (ent, s))
        for r in rows:
            if not pats["any"].findall(r[4]):
                say("WARN", "STATE-02", "%s: chuyển '%s' → '%s' chưa trỏ tới yêu cầu" % (ent, r[0], r[3]))

    # XMOD
    if a.others:
        me = fr["module"]
        for path in sorted(glob.glob(os.path.join(a.others, "FR-M*.md"))):
            if os.path.abspath(path) == os.path.abspath(a.fr):
                continue
            other = frlib.parse_fr(frlib.read(path))
            om = other["module"]
            mine = [r for r in fr["interfaces"] if len(r) >= 3 and r[1] == om]
            theirs = [r for r in other["interfaces"] if len(r) >= 3 and r[1] == me]
            for r in mine:
                want = "Cung cấp" if r[0] == "Dùng" else "Dùng"
                if not any(t[0] == want for t in theirs):
                    say("WARN", "XMOD-01", "%s ghi '%s %s: %s' nhưng FR-%s không có dòng '%s %s'" % (
                        me, r[0], om, frlib.excerpt(r[2], 60), om, want, me))
            for t in theirs:
                if not mine:
                    say("WARN", "XMOD-02", "FR-%s có dòng '%s %s: %s' nhưng tài liệu này chưa ghi gì về %s" % (
                        om, t[0], me, frlib.excerpt(t[2], 60), om))

    say("INFO", "SUM-01", "C.1=%d dòng, nguồn trích ở Phụ lục A=%d, bảng nguồn=%d mục" % (len(c1), len(cited), len(scan["rows"])))
    for lvl in ("ERROR", "WARN", "INFO"):
        for line in out[lvl]:
            print(line)
    print("---\nERROR=%d WARN=%d INFO=%d" % (len(out["ERROR"]), len(out["WARN"]), len(out["INFO"])))
    return 1 if out["ERROR"] else 0


if __name__ == "__main__":
    sys.exit(main())
