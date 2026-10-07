#!/usr/bin/env python3
"""Bước 1 — Tách register và draft thành từng mục nguồn có ID, rồi ghi ra một chỉ mục JSON.

Cách dùng (chạy từ gốc repo iShare):
  python3 .agent-instructions/skills/analyzing-functional-requirements/tools/index_sources.py \
      --out .agents/.claude/system_analysis/output/fr/.work/index.json
  python3 .../index_sources.py --next-ids          # chỉ in ID kế tiếp cho DEC/QA/ISS/OPEN/ASM

Mã mục registry: MR-Mxx (dòng module), MR-Ann (đợt sửa phạm vi), F-XXX-nn (bảng tính năng),
MR-FB-Mxx (bảng AI fallback).
Mỗi mục nguồn gồm: id, kind, file, lines, section (heading cấp 2 bao quanh),
home_module (Mxx nếu section là của module), text, refs (ID khác được nhắc tới),
modules (Mxx được nhắc tới trong text).
Một ID xuất hiện nhiều lần (ví dụ ISS ở backlog rồi ở bảng Closed) được gộp thành một mục.
"""
import argparse
import os
import re
import sys

sys.dont_write_bytecode = True
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import frlib  # noqa: E402

ROW_ID = re.compile(r"^\|\s*((?:DEC|QA|OPEN)-\d{3}|ISS-(?:\d{3}|[A-Z]+-\d{2}))\s*\|")
HEAD_ID = re.compile(r"^#{3,4}\s+((?:DEC|QA)-\d{3})\b")


def home_module(section):
    m = frlib.MODULE_RE.search(section or "")
    return "M" + m.group(1) if m else ""


class Index:
    def __init__(self):
        self.units = {}

    def add(self, uid, kind, path, line, section, text):
        u = self.units.get(uid)
        if u is None:
            u = {"id": uid, "kind": kind, "file": path, "lines": [], "section": section,
                 "sections": [], "home_module": home_module(section), "text": ""}
            self.units[uid] = u
        u["lines"].append(line)
        if section not in u["sections"]:
            u["sections"].append(section)
        if not u["home_module"]:
            u["home_module"] = home_module(section)
        u["text"] = (u["text"] + "\n|| " if u["text"] else "") + text.strip()

    def finish(self):
        for u in self.units.values():
            u["refs"] = [i for i in frlib.find_ids(u["text"]) if i != u["id"]]
            u["modules"] = sorted({"M" + m for m in frlib.MODULE_RE.findall(u["text"])})
        return self.units


def parse_register(idx, root, rel, kind):
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        print("THIẾU tệp nguồn:", rel, file=sys.stderr)
        return
    lines = frlib.read(path).splitlines()
    section = ""
    block = None  # (id, start, [lines]) cho dạng heading ### DEC-xxx / ### QA-xxx

    def close_block():
        nonlocal block
        if block:
            idx.add(block[0], kind, rel, block[1] + 1, section_of_block[0], "\n".join(block[2]))
        block = None

    section_of_block = [""]
    for i, line in enumerate(lines):
        if re.match(r"^## ", line):
            close_block()
            section = line[3:].strip()
            continue
        hm = HEAD_ID.match(line)
        if hm:
            close_block()
            block = (hm.group(1), i, [line])
            section_of_block[0] = section
            continue
        if block is not None:
            if re.match(r"^#{1,3} ", line) or line.strip() == "---":
                close_block()
            else:
                block[2].append(line)
                continue
        rm = ROW_ID.match(line)
        if rm:
            idx.add(rm.group(1), kind, rel, i + 1, section, line)
    close_block()


def parse_glossary(idx, root, rel):
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        return
    lines = frlib.read(path).splitlines()
    for i, line in enumerate(lines):
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if not line.startswith("|") or len(cells) < 2:
            continue
        if re.fullmatch(r":?-{2,}:?", cells[0]) or cells[0].lower().startswith("term"):
            continue
        idx.add("GL:" + cells[0], "glossary", rel, i + 1, "Glossary", line)


def parse_registry(idx, root, rel):
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        return
    lines = frlib.read(path).splitlines()
    section = ""
    amend_n = 0
    buf = None
    for i, line in enumerate(lines):
        if line.startswith("## "):
            if buf:
                idx.add(buf[0], "registry", rel, buf[1], buf[2], "\n".join(buf[3]))
                buf = None
            section = line[3:].strip()
            if section.lower().startswith("amendment"):
                amend_n += 1
                buf = ("MR-A%02d" % amend_n, i + 1, section, [line])
            continue
        if buf is not None:
            buf[3].append(line)
            continue
        m = re.match(r"^\|\s*(M\d\d)\s*\|", line)
        if m:
            idx.add("MR-" + m.group(1), "registry", rel, i + 1, section, line)
            continue
        f = re.match(r"^\|\s*(F-[A-Z]+-\d{2})\s*\|", line)  # bảng tính năng theo module (F-POST-09…)
        if f:
            idx.add(f.group(1), "registry", rel, i + 1, section, line)
            continue
        fb = re.match(r"^\|\s*(M\d\d)\s+\S", line)  # bảng AI fallback: "| M05 Topic | …"
        if fb and "fallback" in section.lower():
            idx.add("MR-FB-" + fb.group(1), "registry", rel, i + 1, section, line)
    if buf:
        idx.add(buf[0], "registry", rel, buf[1], buf[2], "\n".join(buf[3]))


def parse_draft(idx, root, prefix, rel):
    path = os.path.join(root, rel)
    if not os.path.exists(path):
        print("THIẾU tệp draft:", rel, file=sys.stderr)
        return
    lines = frlib.read(path).splitlines()
    cur = None
    h2 = ""
    n = 0

    def close():
        if cur:
            idx.add(cur[0], "draft", rel, cur[1], cur[2], "\n".join(cur[3]))

    for i, line in enumerate(lines):
        m = re.match(r"^(#{1,4}) (.+)$", line)  # "#XácSuất" không có dấu cách nên không phải heading
        if m:
            close()
            title = m.group(2).strip()
            if len(m.group(1)) == 2:
                h2 = title
            num = re.match(r"^(\d+(?:\.\d+)*)\.?\s", title)
            if num:
                uid = "%s-%s" % (prefix, num.group(1))
            else:
                n += 1
                uid = "%s-x%02d" % (prefix, n)
            cur = (uid, i + 1, h2 or title, [line])
        elif cur is not None:
            cur[3].append(line)
    close()


def build(root):
    idx = Index()
    reg = frlib.REG_DIR
    parse_register(idx, root, reg + "/decisions.md", "decision")
    parse_register(idx, root, reg + "/qa-log.md", "qa")
    parse_register(idx, root, reg + "/issue-queue.md", "issue")
    parse_register(idx, root, reg + "/open-issues.md", "open")
    parse_register(idx, root, reg + "/assumptions.md", "assumption")
    parse_glossary(idx, root, reg + "/glossary.md")
    parse_registry(idx, root, reg + "/module-registry.md")
    for prefix, rel in frlib.DRAFT_FILES.items():
        parse_draft(idx, root, prefix, rel)
    return idx.finish()


def next_ids(units):
    out = {}
    for p in ("DEC", "QA", "ISS", "OPEN", "ASM"):
        nums = [int(u.split("-")[1]) for u in units if re.fullmatch(p + r"-\d{3}", u)]
        out[p] = "%s-%03d" % (p, (max(nums) + 1) if nums else 1)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=".", help="gốc repo iShare (mặc định: thư mục hiện tại)")
    ap.add_argument("--out", help="tệp JSON chỉ mục sẽ ghi")
    ap.add_argument("--next-ids", action="store_true", help="in ID kế tiếp rồi thoát")
    a = ap.parse_args()
    units = build(a.root)
    nxt = next_ids(units)
    if a.next_ids:
        print(" ".join("%s" % v for v in nxt.values()))
        return
    kinds = {}
    for u in units.values():
        kinds[u["kind"]] = kinds.get(u["kind"], 0) + 1
    data = {"root": os.path.abspath(a.root), "next_ids": nxt, "counts": kinds, "units": units}
    if a.out:
        frlib.dump_json(a.out, data)
        print("Đã ghi", a.out)
    print("Số mục nguồn:", len(units), kinds)
    print("ID kế tiếp:", " ".join(nxt.values()))


if __name__ == "__main__":
    main()
