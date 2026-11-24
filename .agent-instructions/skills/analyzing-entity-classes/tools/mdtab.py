#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""mdtab.py - đọc tài liệu Markdown có frontmatter, mục đánh số và bảng.

Tệp này giống hệt nhau trong thư mục tools/ của ba skill
(analyzing-entity-classes, designing-entity-classes, designing-database).
Sửa ở một nơi thì chép sang hai nơi còn lại.
Chỉ dùng thư viện chuẩn của Python 3.

Phần cuối tệp là các hàm cho sơ đồ: mỗi sơ đồ là một tệp .puml riêng trong thư mục diagrams/ cạnh tài liệu, được
render thành ảnh PNG cùng tên, và tài liệu chỉ nhúng ảnh (không chép mã PlantUML vào tài liệu).
"""
import glob
import io
import os
import re
import shutil
import subprocess
import sys
import zlib

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


# ---------------------------------------------------------------------------------------------------------------------
# Sơ đồ: tệp .puml riêng + ảnh PNG render từ nó
# ---------------------------------------------------------------------------------------------------------------------
DIAGRAM_DIR = "diagrams"
PNG_MAGIC = b"\x89PNG\r\n\x1a\n"
_PU_ALPHA = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz-_"

RENDER_HELP = """Không render được ảnh PNG từ tệp .puml. Chọn một trong các cách sau rồi chạy lại lệnh:
  1. Dùng Java (máy đã có JDK là đủ) và tệp plantuml.jar: tải plantuml.jar từ https://plantuml.com/download,
     đặt vào .agent-instructions/skills/analyzing-entity-classes/tools/vendor/plantuml.jar
     (thư mục vendor/ đã được .gitignore), hoặc đặt biến môi trường PLANTUML_JAR trỏ tới tệp jar.
     Tool tìm java trong PATH, JAVA_HOME, rồi ~/.jdks/.
  2. Cài lệnh plantuml (ví dụ: scoop install plantuml, hoặc choco install plantuml) để có lệnh plantuml trong PATH.
  3. Dùng máy chủ PlantUML: thêm --server https://www.plantuml.com/plantuml (nội dung sơ đồ được gửi lên máy chủ đó).
Không có Graphviz thì tool tự dùng bố cục Smetana có sẵn trong PlantUML."""


def doc_id_of(fm, path):
    """Mã tài liệu (EC-M05, CD-SYS…) lấy từ frontmatter, không có thì lấy tên tệp."""
    return fm.get("ma_tai_lieu") or os.path.splitext(os.path.basename(path))[0]


def diagram_paths(doc_path, doc_id):
    d = os.path.join(os.path.dirname(os.path.abspath(doc_path)), DIAGRAM_DIR)
    return os.path.join(d, doc_id + ".puml"), os.path.join(d, doc_id + ".png")


def diagram_markdown(doc_id, caption, tool):
    """Đoạn Markdown đặt vào tài liệu: ảnh PNG và liên kết tới tệp .puml."""
    return ("![%s](%s/%s.png)\n\n"
            "Mã nguồn sơ đồ: [%s/%s.puml](%s/%s.puml). Ảnh và tệp .puml do `%s` sinh từ các bảng của tài liệu này; "
            "muốn đổi sơ đồ thì sửa bảng rồi chạy lại tool, không sửa tay."
            % (caption, DIAGRAM_DIR, doc_id, DIAGRAM_DIR, doc_id, DIAGRAM_DIR, doc_id, tool))


def plantuml_encode(text):
    """Mã hóa nội dung sơ đồ theo chuẩn URL của máy chủ PlantUML (deflate + bảng chữ 64 ký tự riêng)."""
    data = zlib.compress(text.encode("utf-8"), 9)[2:-4]
    out = []
    for i in range(0, len(data), 3):
        c = data[i:i + 3] + b"\x00\x00"
        b1, b2, b3 = c[0], c[1], c[2]
        out.append(_PU_ALPHA[b1 >> 2])
        out.append(_PU_ALPHA[((b1 & 0x3) << 4) | (b2 >> 4)])
        out.append(_PU_ALPHA[((b2 & 0xF) << 2) | (b3 >> 6)])
        out.append(_PU_ALPHA[b3 & 0x3F])
    return "".join(out)


def plantuml_decode(code):
    """Ngược với plantuml_encode (dùng để tự kiểm)."""
    vals = [_PU_ALPHA.index(ch) for ch in code]
    data = bytearray()
    for i in range(0, len(vals), 4):
        a, b, c, d = (vals[i:i + 4] + [0, 0, 0])[:4]
        data += bytes([(a << 2) | (b >> 4), ((b & 0xF) << 4) | (c >> 2), ((c & 0x3) << 6) | d])
    return zlib.decompressobj(-15).decompress(bytes(data)).decode("utf-8")


def find_java():
    j = shutil.which("java")
    if j:
        return j
    exe = "java.exe" if os.name == "nt" else "java"
    home = os.environ.get("JAVA_HOME")
    if home and os.path.isfile(os.path.join(home, "bin", exe)):
        return os.path.join(home, "bin", exe)
    for d in sorted(glob.glob(os.path.join(os.path.expanduser("~"), ".jdks", "*")), reverse=True):
        if os.path.isfile(os.path.join(d, "bin", exe)):
            return os.path.join(d, "bin", exe)
    return None


def find_plantuml_jar(tools_dir):
    env = os.environ.get("PLANTUML_JAR")
    if env and os.path.isfile(env):
        return env
    skills_dir = os.path.dirname(os.path.dirname(os.path.abspath(tools_dir)))
    for d in (os.path.join(tools_dir, "vendor"),
              os.path.join(skills_dir, "analyzing-entity-classes", "tools", "vendor")):
        found = sorted(glob.glob(os.path.join(d, "plantuml*.jar")))
        if found:
            return found[-1]
    return None


def render_png(puml_path, png_path, tools_dir, server=None, timeout=180):
    """Render tệp .puml thành PNG. Trả về (ok, thông báo)."""
    text = read(puml_path)
    server = server or os.environ.get("PLANTUML_SERVER")
    if server:
        import urllib.request
        url = "%s/png/%s" % (server.rstrip("/"), plantuml_encode(text))
        try:
            with urllib.request.urlopen(url, timeout=timeout) as resp:
                data = resp.read()
        except Exception as e:
            return False, "máy chủ PlantUML lỗi: %s" % e
        how = "máy chủ %s" % server
    else:
        layout = [] if (shutil.which("dot") or os.environ.get("GRAPHVIZ_DOT")) else ["-Playout=smetana"]
        java, jar, exe = find_java(), find_plantuml_jar(tools_dir), shutil.which("plantuml")
        # Sơ đồ toàn hệ thống vượt khung mặc định 4096 px của PlantUML (ảnh bị cắt): nâng giới hạn.
        limit = os.environ.get("PLANTUML_LIMIT_SIZE", "16384")
        if java and jar:
            cmd, how = [java, "-Djava.awt.headless=true", "-DPLANTUML_LIMIT_SIZE=%s" % limit, "-jar", jar], \
                "java -jar %s" % jar
        elif exe:
            cmd, how = [exe], exe
        else:
            missing = []
            if not java:
                missing.append("java")
            if not jar:
                missing.append("plantuml.jar")
            return False, "thiếu %s và không có lệnh plantuml.\n%s" % (" và ".join(missing), RENDER_HELP)
        cmd += ["-tpng", "-charset", "UTF-8", "-pipe"] + layout
        try:
            run = subprocess.run(cmd, input=text.encode("utf-8"), stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                                 timeout=timeout, env=dict(os.environ, PLANTUML_LIMIT_SIZE=limit))
        except Exception as e:
            return False, "chạy PlantUML lỗi: %s\n%s" % (e, RENDER_HELP)
        data = run.stdout
        if run.returncode != 0:
            err = run.stderr.decode("utf-8", "replace").strip().splitlines()[-5:]
            return False, "PlantUML trả mã %d: %s" % (run.returncode, " | ".join(err))
    if not data.startswith(PNG_MAGIC):
        return False, "kết quả render không phải ảnh PNG (%s)" % how
    with open(png_path, "wb") as f:
        f.write(data)
    return True, "đã render %s bằng %s" % (os.path.basename(png_path), how)


def _disp(path):
    rel = os.path.relpath(path)
    return os.path.abspath(path) if rel.startswith("..") else rel


def write_diagram(doc_path, doc_id, puml_text, tools_dir, render=True, server=None):
    """Ghi diagrams/<doc_id>.puml (chỉ khi nội dung đổi) và render PNG khi cần. Trả về (ok, [thông báo])."""
    puml_path, png_path = diagram_paths(doc_path, doc_id)
    os.makedirs(os.path.dirname(puml_path), exist_ok=True)
    puml_text = puml_text.rstrip("\n") + "\n"
    msgs = []
    old = read(puml_path) if os.path.isfile(puml_path) else None
    if old != puml_text:
        write(puml_path, puml_text)
        msgs.append("đã ghi %s" % _disp(puml_path))
    else:
        msgs.append("%s không đổi" % _disp(puml_path))
    if not render:
        msgs.append("bỏ qua render (--no-render)")
        return True, msgs
    stale = (not os.path.isfile(png_path)) or os.path.getmtime(png_path) < os.path.getmtime(puml_path)
    if not stale and server is None and not os.environ.get("PLANTUML_SERVER"):
        msgs.append("%s đã mới" % _disp(png_path))
        return True, msgs
    ok, m = render_png(puml_path, png_path, tools_dir, server)
    msgs.append(m)
    return ok, msgs


def check_diagram(rep, where, doc_path, doc_id, section_text, expected_puml):
    """Kiểm mục sơ đồ: có ảnh nhúng, không chép mã PlantUML, tệp .puml khớp các bảng, ảnh PNG không cũ hơn .puml."""
    tool_hint = "chạy lại tool sinh sơ đồ"
    if "@startuml" in section_text:
        rep.error(where, "mục sơ đồ đang chứa mã PlantUML; mã chỉ nằm trong tệp %s/%s.puml" % (DIAGRAM_DIR, doc_id))
    if "](%s/%s.png)" % (DIAGRAM_DIR, doc_id) not in section_text:
        rep.error(where, "mục sơ đồ chưa nhúng ảnh %s/%s.png (%s)" % (DIAGRAM_DIR, doc_id, tool_hint))
    puml_path, png_path = diagram_paths(doc_path, doc_id)
    if not os.path.isfile(puml_path):
        rep.error(where, "chưa có tệp %s/%s.puml (%s)" % (DIAGRAM_DIR, doc_id, tool_hint))
        return
    if read(puml_path).strip() != expected_puml.strip():
        rep.error(where, "tệp %s/%s.puml lệch với các bảng hiện tại (%s)" % (DIAGRAM_DIR, doc_id, tool_hint))
    if not os.path.isfile(png_path):
        rep.error(where, "chưa có ảnh %s/%s.png (%s)" % (DIAGRAM_DIR, doc_id, tool_hint))
        return
    with open(png_path, "rb") as f:
        if not f.read(8).startswith(PNG_MAGIC):
            rep.error(where, "%s/%s.png không phải ảnh PNG" % (DIAGRAM_DIR, doc_id))
    if os.path.getmtime(png_path) + 1 < os.path.getmtime(puml_path):
        rep.error(where, "ảnh %s/%s.png cũ hơn tệp .puml (%s)" % (DIAGRAM_DIR, doc_id, tool_hint))
