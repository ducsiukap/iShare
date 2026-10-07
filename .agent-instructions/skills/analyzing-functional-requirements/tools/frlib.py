"""Thư viện dùng chung cho các tool của skill analyzing-functional-requirements.

Không có phụ thuộc ngoài thư viện chuẩn Python 3.8+.
"""
import json
import os
import re

# Đường dẫn mặc định, tính từ gốc repo iShare
REG_DIR = ".agents/.claude/system_analysis/output/registers"
DRAFT_FILES = {
    "DM": "docs/_temp/iShare_modules.md",        # draft: danh sách module và tính năng
    "DG": "docs/_temp/iShare_specs_general.md",  # draft: tổng quan dự án
}
FR_DIR = ".agents/.claude/system_analysis/output/fr"

# Mẫu ID nguồn. ISS có dạng chữ, ví dụ ISS-GRP-01.
ID_RE = re.compile(
    r"\b(?:DEC-\d{3}|QA-\d{3}|ISS-(?:\d{3}|[A-Z]+-\d{2})|OPEN-\d{3}|ASM-\d{3})\b"
)
MODULE_RE = re.compile(r"\bM(0[1-9]|1[0-6])\b")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def write(path, text):
    os.makedirs(os.path.dirname(os.path.abspath(path)), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def load_json(path):
    with open(path, encoding="utf-8") as f:
        return json.load(f)


def dump_json(path, obj):
    write(path, json.dumps(obj, ensure_ascii=False, indent=1))


SHORT_RE = re.compile(r"\b(DEC|QA|ISS|OPEN)-(\d{3})((?:/\d{3})+)")


def find_ids(text):
    """Tìm mọi ID nguồn, kể cả dạng viết gọn "DEC-092/093" (= DEC-092, DEC-093)."""
    ids = set(ID_RE.findall(text))
    for m in SHORT_RE.finditer(text):
        for n in m.group(3).strip("/").split("/"):
            ids.add("%s-%s" % (m.group(1), n))
    return sorted(ids)


def excerpt(text, n=140):
    t = re.sub(r"\s+", " ", text).strip()
    return t if len(t) <= n else t[: n - 1] + "…"


# ---------- Đọc tệp FR ----------

def split_frontmatter(text):
    """Trả về (dict frontmatter thô, phần thân). Chỉ đọc khóa: giá trị một dòng."""
    fm = {}
    if text.startswith("---\n"):
        end = text.find("\n---", 4)
        if end != -1:
            for line in text[4:end].splitlines():
                m = re.match(r"^([A-Za-z_]+):\s*(.*?)\s*(#.*)?$", line)
                if m:
                    fm[m.group(1)] = m.group(2)
            return fm, text[end + 4:]
    return fm, text


def sections(body):
    """Chia thân tài liệu theo heading. Trả về list (level, title, start_line, lines)."""
    out = []
    cur = (0, "", 0, [])
    for i, line in enumerate(body.splitlines()):
        m = re.match(r"^(#{1,6}) (.*)$", line)
        if m:
            out.append(cur)
            cur = (len(m.group(1)), m.group(2).strip(), i, [])
        else:
            cur[3].append(line)
    out.append(cur)
    return out


def table_rows(lines):
    """Lấy các dòng bảng Markdown (bỏ dòng tiêu đề và dòng ---). Trả về list các list ô."""
    rows = []
    header_seen = False
    for line in lines:
        s = line.strip()
        if not s.startswith("|"):
            header_seen = False
            continue
        cells = [c.strip() for c in s.strip("|").split("|")]
        if all(re.fullmatch(r":?-{2,}:?", c) for c in cells if c):
            header_seen = True
            continue
        if not header_seen:
            continue  # dòng tiêu đề
        rows.append(cells)
    return rows


def section_lines(body, title_pattern):
    """Gộp các dòng thuộc mọi heading khớp mẫu (kể cả heading con ngay sau nó)."""
    secs = sections(body)
    out = []
    active_level = None
    for level, title, _, lines in secs:
        if active_level is not None and level <= active_level:
            active_level = None
        if re.search(title_pattern, title, re.I):
            active_level = level
            out.extend(lines)
        elif active_level is not None:
            out.extend(lines)
    return out


# ---------- Phân tích tệp FR theo mẫu output/fr-template.md ----------

def id_patterns(mod):
    m = re.escape(mod)
    return {
        "upper": re.compile(r"^FR-%s-\d{2}$" % m),
        "lower": re.compile(r"^FR-%s-\d{2}\.\d{2}$" % m),
        "br": re.compile(r"^BR-%s-\d{2}$" % m),
        "tbd": re.compile(r"^TBD-%s-\d{2}$" % m),
        "any": re.compile(r"\b(?:FR-%s-\d{2}(?:\.\d{2})?|BR-%s-\d{2}|TBD-%s-\d{2})\b" % (m, m, m)),
    }


def parse_fr(text):
    """Đọc tệp FR. Trả về dict các phần mà tool kiểm tra cần."""
    fm, body = split_frontmatter(text)
    mod = fm.get("module", "").strip()
    pats = id_patterns(mod)
    secs = sections(body)
    res = {"fm": fm, "module": mod, "pats": pats, "body": body,
           "defined": {}, "upper_heads": {}, "list44": [], "lower_text": {},
           "appendix_a": {}, "c1": [], "crud": [], "states": {}, "interfaces": [],
           "perm": [], "tbd": [], "br": {}}
    in_app = False
    cur_upper = None
    cur_state = None
    for level, title, start, lines in secs:
        t = title
        if level == 2:
            in_app = t.lower().startswith("phụ lục")
            cur_upper = None
        m = re.match(r"^5\.\d+\s+(FR-\S+)\s*(.*)$", t)
        if level == 3 and m:
            cur_upper = m.group(1)
            res["upper_heads"][cur_upper] = {"title": m.group(2), "text": "\n".join(lines)}
            res["defined"].setdefault(cur_upper, "heading 5.x")
        elif level == 3:
            cur_upper = None
        if level <= 3 and not re.search(r"chuyển trạng thái", t, re.I):
            cur_state = None
        if re.search(r"chuyển trạng thái", t, re.I) and level == 3:
            cur_state = ""
        if level == 4 and cur_state is not None:
            cur_state = t
        rows = table_rows(lines)
        if in_app:
            if t.startswith("Phụ lục A"):
                for r in rows:
                    if len(r) >= 3:
                        res["appendix_a"][r[0]] = {"sources": [s.strip() for s in re.split(r"[,;]", r[1]) if s.strip()],
                                                   "basis": r[2], "note": r[3] if len(r) > 3 else ""}
            elif t.startswith("C.1"):
                for r in rows:
                    if len(r) >= 4:
                        res["c1"].append({"src": r[0], "label": r[1], "status": r[2], "used": r[3],
                                          "note": r[4] if len(r) > 4 else ""})
            elif t.startswith("B.2"):
                for r in rows:
                    if len(r) >= 3:
                        res["tbd"].append({"id": r[0], "text": r[1], "impact": r[2]})
            continue
        if t.startswith("4.4"):
            res["list44"] = [r[0] for r in rows if r and r[0]]
        if t.startswith("4.3"):
            res["perm"] = rows
        if re.search(r"quy tắc nghiệp vụ", t, re.I):
            for r in rows:
                if r and pats["br"].match(r[0]):
                    res["br"][r[0]] = r
                    res["defined"].setdefault(r[0], "BR")
        if re.search(r"giao tiếp với module", t, re.I):
            res["interfaces"] = rows
        if cur_state is not None and rows and len(rows[0]) >= 5:
            res["states"].setdefault(cur_state or "(không tên)", []).extend(rows)
        crud_lines = "\n".join(lines)
        if "CRUD" in crud_lines:
            after = crud_lines.split("CRUD", 1)[1].splitlines()
            res["crud"] = [r for r in table_rows(after) if len(r) >= 5]
        if cur_upper:
            for r in rows:
                if r and pats["lower"].match(r[0]):
                    res["lower_text"][r[0]] = r[1] if len(r) > 1 else ""
                    res["defined"].setdefault(r[0], cur_upper)
    return res
