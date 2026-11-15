#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mdtab.py - đọc tài liệu Markdown có frontmatter, mục đánh số và bảng.

Tệp này giống hệt nhau trong thư mục tools/ của ba skill
(analyzing-entity-classes, designing-entity-classes, designing-database).
Sửa ở một nơi thì chép sang hai nơi còn lại.
Chỉ dùng thư viện chuẩn của Python 3.
"""
import io
import re
import sys

EMPTY = {"", "—", "-", "–", "n/a", "N/A"}
ID_RE = re.compile(r"\b(?:FR|BR)-M\d{2}-\d{2}(?:\.\d{2})?\b")
HEAD_RE = re.compile(r"^(#{1,6})\s+(.*)$")
NUM_RE = re.compile(r"^(\d+(?:\.\d+)*)\.?\s+")
MULT_RE = re.compile(r"^(\d+|\*|n)(?:\.\.(\d+|\*|n))?$")
CLASS_RE = re.compile(r"^[A-Z][A-Za-z0-9]*$")
ATTR_RE = re.compile(r"^[a-z][A-Za-z0-9]*$")


def utf8_stdout():
    """Windows hay in lỗi tiếng Việt; ép stdout sang UTF-8."""
    try:
        sys.stdout.reconfigure(encoding="utf-8")
    except Exception:
        sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding="utf-8")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n")


def write(path, text):
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(text)


def frontmatter(text):
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    fm = {}
    if m:
        for line in m.group(1).splitlines():
            if ":" in line:
                k, v = line.split(":", 1)
                fm[k.strip()] = v.strip()
    return fm


def steps_completed(fm):
    return [int(x) for x in re.findall(r"\d+", fm.get("steps_completed", ""))]


def sections(text):
    """Danh sách mục theo thứ tự. Mỗi mục: level, num ('2.1' hoặc ''), title, body
    (phần ngay dưới tiêu đề, tới tiêu đề kế tiếp bất kỳ cấp nào)."""
    out, cur, in_code = [], None, False
    for ln in text.split("\n"):
        if ln.strip().startswith("```"):
            in_code = not in_code
        m = None if in_code else HEAD_RE.match(ln)
        if m:
            title = m.group(2).strip()
            nm = NUM_RE.match(title)
            cur = {"level": len(m.group(1)), "num": nm.group(1) if nm else "",
                   "title": title, "lines": []}
            out.append(cur)
        elif cur is not None:
            cur["lines"].append(ln)
    for s in out:
        s["body"] = "\n".join(s["lines"])
    return out


def section(text, num):
    for s in sections(text):
        if s["num"] == num:
            return s
    return None


def section_by_title(text, needle):
    """Mục đầu tiên có tiêu đề chứa `needle` (dùng cho FR: số mục 5.x khác nhau giữa các module)."""
    for s in sections(text):
        if needle.lower() in s["title"].lower():
            return s
    return None


def table_by_title(text, needle):
    """Bảng đầu tiên ngay dưới mục có tiêu đề chứa `needle`. Trả về (header, rows)."""
    s = section_by_title(text, needle)
    if not s:
        return None, []
    t = tables(s["body"])
    return t[0] if t else (None, [])


def section_with_children(text, num):
    """Thân của mục `num` gồm cả các mục con (2 gồm 2.1, 2.2...)."""
    parts = []
    for s in sections(text):
        if s["num"] == num or s["num"].startswith(num + "."):
            parts.append(s["title"] + "\n" + s["body"])
    return "\n".join(parts)


def strip_comments(text):
    """Bỏ chú thích HTML <!-- ... --> (mẫu tài liệu có chú thích hướng dẫn chứa chữ như '(Chưa làm')."""
    return re.sub(r"<!--.*?-->", "", text or "", flags=re.S)


def clean(cell):
    return re.sub(r"`|\*\*", "", cell or "").strip()


def is_empty(cell):
    return clean(cell) in EMPTY


def split_row(line):
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", line)]


def tables(body):
    res, lines, i = [], body.split("\n"), 0
    while i < len(lines):
        if (lines[i].strip().startswith("|") and i + 1 < len(lines)
                and re.match(r"^\s*\|?\s*:?-{3,}", lines[i + 1])):
            header = [clean(h) for h in split_row(lines[i])]
            rows = []
            i += 2
            while i < len(lines) and lines[i].strip().startswith("|"):
                cells = split_row(lines[i])
                cells += [""] * (len(header) - len(cells))
                row = {h: clean(c) for h, c in zip(header, cells)}
                first = clean(cells[0]) if cells else ""
                if not first.startswith("(Chưa làm") and any(not is_empty(c) for c in cells):
                    rows.append(row)
                i += 1
            res.append((header, rows))
        else:
            i += 1
    return res


def table(text, num):
    """Bảng đầu tiên ngay dưới mục `num`. Trả về (header, rows); (None, []) nếu không có."""
    s = section(text, num)
    if not s:
        return None, []
    t = tables(s["body"])
    return t[0] if t else (None, [])


def ids_in(cell):
    return ID_RE.findall(cell or "")


def split_list(cell):
    """Tách ô chứa nhiều giá trị ngăn bởi dấu phẩy hoặc chấm phẩy."""
    if is_empty(cell):
        return []
    return [clean(x) for x in re.split(r"[;,]", cell) if clean(x)]


def mult_upper(m):
    """'1' -> '1'; '0..1' -> '1'; '0..*', '1..*', '*', '1..3' -> 'n'; None nếu sai cú pháp."""
    m = clean(m).replace(" ", "")
    mm = MULT_RE.match(m)
    if not mm:
        return None
    hi = mm.group(2) or mm.group(1)
    if hi in ("*", "n"):
        return "n"
    if int(hi) == 0:
        return None
    return "1" if int(hi) == 1 else "n"


def mult_lower(m):
    """Cận dưới: 0, 1, ... ; '*' một mình coi là 0."""
    m = clean(m).replace(" ", "")
    mm = MULT_RE.match(m)
    if not mm:
        return None
    lo = mm.group(1)
    if lo in ("*", "n"):
        return 0
    return int(lo)


def split_pair(cell):
    """'Room – Booking' -> ('Room', 'Booking')."""
    parts = [clean(p) for p in re.split(r"\s[–—-]\s|\s*[–—]\s*", cell or "") if clean(p)]
    return tuple(parts) if len(parts) == 2 else None


def replace_block(text, name, new_body):
    """Thay nội dung giữa <!-- BEGIN:name --> và <!-- END:name -->. Trả về (text, ok)."""
    pat = re.compile(r"(<!-- BEGIN:%s -->)(.*?)(<!-- END:%s -->)" % (name, name), re.S)
    if not pat.search(text):
        return text, False
    return pat.sub(lambda m: m.group(1) + "\n" + new_body.rstrip("\n") + "\n" + m.group(3), text, count=1), True


class Report:
    def __init__(self, title):
        self.title = title
        self.items = []

    def error(self, where, msg):
        self.items.append(("ERROR", where, msg))

    def warn(self, where, msg):
        self.items.append(("WARN", where, msg))

    def info(self, where, msg):
        self.items.append(("INFO", where, msg))

    def need_cols(self, where, header, cols):
        """Báo lỗi nếu bảng thiếu hoặc thiếu cột. Trả về True nếu dùng được."""
        if header is None:
            self.error(where, "không tìm thấy bảng")
            return False
        miss = [c for c in cols if c not in header]
        if miss:
            self.error(where, "bảng thiếu cột: " + ", ".join(miss))
            return False
        return True

    def count(self, level):
        return sum(1 for i in self.items if i[0] == level)

    def finish(self):
        print("== " + self.title + " ==")
        for level in ("ERROR", "WARN", "INFO"):
            for lv, where, msg in self.items:
                if lv == level:
                    print("%-5s [%s] %s" % (lv, where, msg))
        print("-- %d ERROR, %d WARN, %d INFO" % (self.count("ERROR"), self.count("WARN"), self.count("INFO")))
        return 1 if self.count("ERROR") else 0
