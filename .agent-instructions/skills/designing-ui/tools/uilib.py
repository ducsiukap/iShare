#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""uilib.py - thư viện dùng chung cho các tool của skill designing-ui.

Chỉ dùng thư viện chuẩn của Python 3. Gồm:
- đọc/ghi tệp UTF-8, frontmatter, bảng Markdown (theo marker <!-- ui:... --> hoặc <!-- uc:... -->);
- phân tích màu (hex, rgb, hsl, oklch), độ tương phản WCAG;
- đọc tokens.json theo định dạng Design System của Claude Design
  ({"color": {"themes": [...], "tokens": [{"name", "value", "usage"}]}, "type": {...}, "spacing": {"tokens": [...]}, ...}).
"""
import io
import json
import math
import re
import sys

EMPTY = {"", "—", "-", "–", "n/a", "N/A"}


# ---------------------------------------------------------------- tệp

def utf8_stdout():
    """Windows hay in lỗi tiếng Việt; ép stdout sang UTF-8."""
    for name in ("stdout", "stderr"):
        stream = getattr(sys, name)
        try:
            stream.reconfigure(encoding="utf-8")
        except Exception:
            setattr(sys, name, io.TextIOWrapper(stream.buffer, encoding="utf-8"))


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


# ---------------------------------------------------------------- bảng Markdown

def split_row(line):
    """Tách một dòng bảng Markdown thành các ô; giữ '|' được escape (\\|) hoặc nằm trong `code`."""
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|") and not line.endswith("\\|"):
        line = line[:-1]
    cells, cur, in_code, i = [], [], False, 0
    while i < len(line):
        ch = line[i]
        if ch == "\\" and i + 1 < len(line) and line[i + 1] == "|":
            cur.append("|")
            i += 2
            continue
        if ch == "`":
            in_code = not in_code
        if ch == "|" and not in_code:
            cells.append("".join(cur).strip())
            cur = []
        else:
            cur.append(ch)
        i += 1
    cells.append("".join(cur).strip())
    return cells


def parse_table(lines, start):
    """Đọc bảng bắt đầu từ dòng `start` (dòng tiêu đề). Trả (rows, line_numbers, end)."""
    header = [c.strip().lower() for c in split_row(lines[start])]
    rows, nums = [], []
    i = start + 2  # bỏ dòng phân cách
    while i < len(lines) and lines[i].strip().startswith("|"):
        cells = split_row(lines[i])
        cells += [""] * (len(header) - len(cells))
        rows.append({header[k]: cells[k] for k in range(len(header))})
        nums.append(i + 1)
        i += 1
    return header, rows, nums


def table_after_marker(text, marker):
    """Bảng đầu tiên sau dòng `<!-- marker -->`. Trả (header, rows, line_numbers) hoặc (None, [], [])."""
    lines = text.split("\n")
    pat = re.compile(r"<!--\s*" + re.escape(marker) + r"\s*-->")
    for idx, line in enumerate(lines):
        if pat.search(line):
            j = idx + 1
            while j < len(lines) and not lines[j].strip().startswith("|"):
                if lines[j].strip().startswith("<!--") and j > idx + 3:
                    return None, [], []
                j += 1
            if j + 1 < len(lines) and re.match(r"^\s*\|?\s*:?-{2,}", lines[j + 1]):
                return parse_table(lines, j)
            return None, [], []
    return None, [], []


def tables_after_marker_prefix(text, prefix):
    """Mọi bảng sau các marker bắt đầu bằng `prefix` (ví dụ 'uc:catalog')."""
    out = []
    lines = text.split("\n")
    for idx, line in enumerate(lines):
        m = re.search(r"<!--\s*(" + re.escape(prefix) + r"[^>]*?)\s*-->", line)
        if m:
            sub = "\n".join(lines[idx:])
            header, rows, nums = table_after_marker(sub, m.group(1))
            if header:
                out.append((m.group(1), header, rows, [n + idx for n in nums]))
    return out


def split_list(cell):
    if cell is None:
        return []
    cell = cell.strip()
    if cell in EMPTY:
        return []
    return [x.strip().strip("`") for x in re.split(r"[,;]", cell) if x.strip() and x.strip() not in EMPTY]


# ---------------------------------------------------------------- màu

NAMED = {"black": (0, 0, 0), "white": (1, 1, 1)}


def _clamp(x):
    return max(0.0, min(1.0, x))


def parse_color(s):
    """Trả (r, g, b, a) trong [0, 1] hoặc None. Hỗ trợ #rgb #rgba #rrggbb #rrggbbaa, rgb(a)(), hsl(a)(), oklch()."""
    if s is None:
        return None
    s = s.strip().lower()
    if s in NAMED:
        r, g, b = NAMED[s]
        return (r, g, b, 1.0)
    m = re.fullmatch(r"#([0-9a-f]{3,8})", s)
    if m:
        h = m.group(1)
        if len(h) in (3, 4):
            h = "".join(c * 2 for c in h)
        if len(h) not in (6, 8):
            return None
        r, g, b = (int(h[k:k + 2], 16) / 255 for k in (0, 2, 4))
        a = int(h[6:8], 16) / 255 if len(h) == 8 else 1.0
        return (r, g, b, a)
    m = re.fullmatch(r"(rgba?|hsla?|oklch)\((.*)\)", s)
    if not m:
        return None
    fn, args = m.group(1), m.group(2)
    parts = [p for p in re.split(r"[\s,/]+", args.strip()) if p]
    if len(parts) < 3:
        return None

    def num(p, scale=1.0):
        if p.endswith("%"):
            return float(p[:-1]) / 100 * scale
        if p.endswith("deg"):
            return float(p[:-3])
        return float(p)

    try:
        a = 1.0
        if len(parts) >= 4:
            a = num(parts[3]) if not parts[3].endswith("%") else float(parts[3][:-1]) / 100
        if fn.startswith("rgb"):
            vals = []
            for p in parts[:3]:
                vals.append(float(p[:-1]) / 100 if p.endswith("%") else float(p) / 255)
            return (_clamp(vals[0]), _clamp(vals[1]), _clamp(vals[2]), a)
        if fn.startswith("hsl"):
            h = num(parts[0]) % 360
            sat = float(parts[1].rstrip("%")) / 100
            lig = float(parts[2].rstrip("%")) / 100
            c = (1 - abs(2 * lig - 1)) * sat
            x = c * (1 - abs((h / 60) % 2 - 1))
            mm = lig - c / 2
            r, g, b = [(c, x, 0), (x, c, 0), (0, c, x), (0, x, c), (x, 0, c), (c, 0, x)][int(h // 60) % 6]
            return (_clamp(r + mm), _clamp(g + mm), _clamp(b + mm), a)
        if fn == "oklch":
            L = float(parts[0][:-1]) / 100 if parts[0].endswith("%") else float(parts[0])
            C = float(parts[1][:-1]) / 100 * 0.4 if parts[1].endswith("%") else float(parts[1])
            H = math.radians(num(parts[2]))
            la, lb = C * math.cos(H), C * math.sin(H)
            l_ = (L + 0.3963377774 * la + 0.2158037573 * lb) ** 3
            m_ = (L - 0.1055613458 * la - 0.0638541728 * lb) ** 3
            s_ = (L - 0.0894841775 * la - 1.2914855480 * lb) ** 3
            lin = (4.0767416621 * l_ - 3.3077115913 * m_ + 0.2309699292 * s_,
                   -1.2684380046 * l_ + 2.6097574011 * m_ - 0.3413193965 * s_,
                   -0.0041960863 * l_ - 0.7034186147 * m_ + 1.7076147010 * s_)

            def enc(v):
                v = _clamp(v)
                return 12.92 * v if v <= 0.0031308 else 1.055 * v ** (1 / 2.4) - 0.055

            r, g, b = (enc(v) for v in lin)
            return (r, g, b, a)
    except (ValueError, IndexError):
        return None
    return None


def to_hex(c):
    r, g, b, a = c
    h = "#%02x%02x%02x" % tuple(int(round(_clamp(v) * 255)) for v in (r, g, b))
    if a < 0.999:
        h += "%02x" % int(round(a * 255))
    return h


def composite(fg, bg):
    """Trộn màu có alpha lên nền đặc."""
    r, g, b, a = fg
    br, bgg, bb, _ = bg
    return (r * a + br * (1 - a), g * a + bgg * (1 - a), b * a + bb * (1 - a), 1.0)


def luminance(c):
    def lin(v):
        return v / 12.92 if v <= 0.04045 else ((v + 0.055) / 1.055) ** 2.4
    r, g, b, _ = c
    return 0.2126 * lin(r) + 0.7152 * lin(g) + 0.0722 * lin(b)


def contrast(fg, bg):
    if bg[3] < 1:
        bg = composite(bg, (1, 1, 1, 1))
    if fg[3] < 1:
        fg = composite(fg, bg)
    l1, l2 = luminance(fg), luminance(bg)
    hi, lo = max(l1, l2), min(l1, l2)
    return (hi + 0.05) / (lo + 0.05)


def hsl_of(c):
    r, g, b, _ = c
    mx, mn = max(r, g, b), min(r, g, b)
    lig = (mx + mn) / 2
    if mx == mn:
        return (0.0, 0.0, lig)
    d = mx - mn
    sat = d / (2 - mx - mn) if lig > 0.5 else d / (mx + mn)
    if mx == r:
        h = ((g - b) / d) % 6
    elif mx == g:
        h = (b - r) / d + 2
    else:
        h = (r - g) / d + 4
    return (h * 60, sat, lig)


COLOR_RE = re.compile(
    r"#[0-9a-fA-F]{8}\b|#[0-9a-fA-F]{6}\b|#[0-9a-fA-F]{3,4}\b|"
    r"\b(?:rgba?|hsla?|oklch)\([^()]*\)")


def find_colors(text):
    """Mọi màu viết trực tiếp trong một đoạn CSS/HTML: [(chuỗi, vị trí)]."""
    return [(m.group(0), m.start()) for m in COLOR_RE.finditer(text)]


# ---------------------------------------------------------------- tokens

class Tokens:
    """tokens.json theo định dạng Design System của Claude Design."""

    def __init__(self, path):
        self.path = path
        self.data = json.loads(read(path))
        self.errors = []
        color = self.data.get("color", {}) or {}
        self.themes = [t.get("id") for t in color.get("themes", [])] or ["light"]
        self.raw_colors = {}
        for t in color.get("tokens", []) or []:
            name, val = t.get("name"), t.get("value")
            if not name:
                self.errors.append("color token thiếu name: %r" % (t,))
                continue
            if isinstance(val, str):
                val = {self.themes[0]: val}
            if not isinstance(val, dict):
                self.errors.append("color token %s có value không hợp lệ" % name)
                continue
            self.raw_colors[name] = val
        self.colors = {}  # name -> {theme: (r,g,b,a)}
        for name in self.raw_colors:
            self.colors[name] = {}
            for th in self.themes:
                c = self.resolve(name, th, set())
                if c is not None:
                    self.colors[name][th] = c
        typ = self.data.get("type", {}) or {}
        self.families = {}
        for k, v in (typ.get("families") or {}).items():
            self.families[k] = v
        self.font_names = set()
        for v in self.families.values():
            first = v.split(",")[0].strip().strip("\"'")
            if first:
                self.font_names.add(first.lower())
        for f in typ.get("fonts") or []:
            if f.get("family"):
                self.font_names.add(f["family"].strip().strip("\"'").lower())
        self.type_styles = []
        for g in typ.get("groups") or []:
            for s in g.get("styles") or []:
                st = dict(s)
                st["family"] = st.get("family") or g.get("family")
                self.type_styles.append(st)
        self.font_sizes = {_norm_len(s.get("fontSize")) for s in self.type_styles if s.get("fontSize")}
        self.spacing = self._lens("spacing")
        self.radius = self._lens("radius")
        self.shadows = [t.get("value") for t in (self.data.get("shadow", {}) or {}).get("tokens", []) or []]

    def _lens(self, family):
        out = {}
        for t in (self.data.get(family, {}) or {}).get("tokens", []) or []:
            out[t.get("name")] = _norm_len(t.get("value"))
        return out

    def resolve(self, name, theme, seen):
        if name in seen or name not in self.raw_colors:
            return None
        seen.add(name)
        vals = self.raw_colors[name]
        v = vals.get(theme, vals.get(self.themes[0]))
        if v is None:
            return None
        v = v.strip()
        m = re.fullmatch(r"\{([A-Za-z0-9][A-Za-z0-9_.-]*)\}", v)
        if m:
            return self.resolve(m.group(1), theme, seen)
        return parse_color(v)

    def color_hexes(self):
        """Tập mã hex (chuẩn hóa) của mọi màu, mọi theme."""
        out = set()
        for name, byth in self.colors.items():
            for c in byth.values():
                out.add(to_hex(c))
                out.add(to_hex((c[0], c[1], c[2], 1.0)))
        return out


def _norm_len(v):
    """Chuẩn hóa độ dài về chuỗi px khi có thể: '16px' -> '16px', '1rem' -> '16px', 16 -> '16px'."""
    if v is None:
        return None
    if isinstance(v, (int, float)):
        return "%gpx" % v
    s = str(v).strip().lower()
    m = re.fullmatch(r"(-?\d*\.?\d+)(px|rem|em)?", s)
    if m:
        n = float(m.group(1))
        unit = m.group(2) or "px"
        if unit in ("rem", "em"):
            n *= 16
        return "%gpx" % n
    return s
