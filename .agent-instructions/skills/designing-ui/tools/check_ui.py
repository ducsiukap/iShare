#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_ui.py - kiểm artboard (.dc.html, .html) và CSS theo ANTI-PATTERNS.md và QUALITY-FLOOR.md.

Hai chế độ:
- Khám phá (không có --tokens): kiểm danh sách cấm (màu tím, gradient, font mặc định, emoji, lorem...).
- Thực thi (có --tokens): kiểm thêm mọi màu, font, khoảng cách, bo góc, cỡ chữ nằm ngoài tokens.

--design DESIGN.md: đọc bảng <!-- ui:ap-exceptions --> (ap | scope | reason | dd) và hạ cảnh báo đã được duyệt
xuống INFO.

Ví dụ:
  python3 check_ui.py canvas/kham-pha/project --design output/DESIGN.md
  python3 check_ui.py canvas/giao-dien/project --tokens output/tokens/tokens.json --design output/DESIGN.md
Mã thoát: 0 nếu không có ERROR, 1 nếu có ERROR, 2 nếu lỗi tham số/tệp.
"""
import argparse
import collections
import fnmatch
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uilib  # noqa: E402

# ------------------------------------------------------------------ danh sách

PURPLE_KNOWN = {
    "#667eea", "#764ba2", "#6366f1", "#4f46e5", "#4338ca", "#818cf8", "#a5b4fc",
    "#8b5cf6", "#7c3aed", "#6d28d9", "#a78bfa", "#a855f7", "#9333ea", "#7e22ce", "#c084fc",
    "#d946ef", "#c026d3",
}
TW_PURPLE = re.compile(r"\b(?:bg|text|border|from|to|via|ring|fill|stroke|outline|decoration|shadow|accent|caret)"
                       r"-(?:indigo|violet|purple|fuchsia)-\d{2,3}\b")
TW_DEFAULT = re.compile(r"\b(?:bg|text|border|ring|divide|from|to|via|fill|stroke|placeholder)"
                        r"-(?:slate|zinc|gray|neutral|stone)-\d{2,3}\b")
FONT_BANNED = {"inter", "roboto", "poppins", "geist", "geist sans", "open sans", "lato", "montserrat", "arial",
               "helvetica", "helvetica neue", "system-ui", "-apple-system", "blinkmacsystemfont", "segoe ui",
               "sans-serif", "serif", "ui-sans-serif"}
FONT_OVERUSED = {"space grotesk", "dm sans", "manrope", "plus jakarta sans", "outfit", "sora"}
FONT_SKIP = {"inherit", "initial", "unset", "monospace", "ui-monospace", "math", "cursive", "fantasy", "emoji"}
EMOJI_ERR = re.compile("[\U0001F000-\U0001FAFF☀-⛿✀-✒✙-➿⭐⭕⬛⬜"
                       "⤴⤵〰〽㊗㊙️]")
EMOJI_WARN = re.compile("[✓-✘]")
ARROW_IN_ACTION = re.compile(r"<(button|a)\b[^>]*>(?:(?!</\1>).){0,400}?(→|➜|➔|⟶|&rarr;)", re.S | re.I)
LOREM = re.compile(r"lorem|ipsum|dolor sit amet|tiêu đề ở đây|nội dung mẫu|văn bản mẫu|placeholder text|"
                   r"your text here|sample text", re.I)
CLICHE_EN = re.compile(r"\b(?:unlock(?:s|ing)?|elevate(?:s|d)?|supercharge(?:s|d)?|seamless(?:ly)?|empower(?:s|ing)?|"
                       r"revolutioni[sz]e|next[- ]level|game[- ]changer|cutting[- ]edge|unleash(?:es)?)\b", re.I)
CLICHE_VI = re.compile(r"khai phá|nâng tầm|bứt phá|liền mạch|đột phá|cách mạng hóa|cách mạng hoá|"
                       r"trải nghiệm tuyệt vời|mạnh mẽ|vượt trội|không chỉ là", re.I)
FAKE_STAT = re.compile(r"\b\d+(?:[.,]\d+)?\s?[xX]\s+(?:faster|better|more|nhanh|hiệu quả|tốt)|"
                       r"(?:nhanh|tốt|hiệu quả) hơn \d+(?:[.,]\d+)?\s?(?:lần|x\b)|gấp \d+ lần|"
                       r"\b\d+(?:[.,]\d+)?\s?[kKmM]\+|\b99[.,]9+\s?%|"
                       r"(?:hàng )?(?:nghìn|triệu|ngàn) (?:người dùng|học sinh|thành viên)", re.I)
FAKE_NAME = re.compile(r"Nguyễn Văn A\b|Trần Thị B\b|Lê Văn C\b|John Doe|Jane Doe|\bUser ?\d+\b|"
                       r"Người dùng \d+|Tên người dùng", re.I)
COLOR_ATTR = re.compile(r"\b(fill|stroke|stop-color|color|flood-color|lighting-color|bgcolor)\s*=\s*"
                        r"(\"[^\"]*\"|'[^']*')", re.I)
CLASS_ATTR = re.compile(r"\b(?:class|className)\s*=\s*(\"[^\"]*\"|'[^']*')")
STYLE_ATTR = re.compile(r"\bstyle\s*=\s*(\"[^\"]*\"|'[^']*')", re.I)
STYLE_BLOCK = re.compile(r"<style\b[^>]*>(.*?)</style>", re.S | re.I)
SCRIPT_BLOCK = re.compile(r"<script\b[^>]*>.*?</script>", re.S | re.I)
SPACING_PROPS = {"padding", "padding-top", "padding-bottom", "padding-left", "padding-right", "padding-inline",
                 "padding-block", "margin", "margin-top", "margin-bottom", "margin-left", "margin-right",
                 "margin-inline", "margin-block", "gap", "row-gap", "column-gap", "inset", "top", "left", "right",
                 "bottom"}
PX = re.compile(r"(-?\d*\.?\d+)(px|rem)\b")

AP_OF = {
    "UI-PURPLE-KNOWN": "AP-01", "UI-PURPLE-HUE": "AP-01", "UI-GRADIENT": "AP-02", "UI-GRADIENT-TEXT": "AP-03",
    "UI-GLOW": "AP-04", "UI-PURE-BLACK": "AP-05", "UI-FONT-BANNED": "AP-10", "UI-FONT-OVERUSED": "AP-10b",
    "UI-ONE-WEIGHT": "AP-11", "UI-EYEBROW": "AP-12", "UI-RADIUS-UNIFORM": "AP-30", "UI-SHADOW-WIDE": "AP-31",
    "UI-LEFT-STRIPE": "AP-32", "UI-GLASS": "AP-33", "UI-TW-DEFAULT": "AP-34", "UI-EMOJI": "AP-40",
    "UI-ARROW": "AP-43", "UI-LOREM": "AP-50", "UI-CLICHE": "AP-51", "UI-FAKE-STAT": "AP-52",
    "UI-FAKE-NAME": "AP-53", "UI-BOUNCE": "AP-60", "UI-NO-REDUCED-MOTION": "AP-61", "UI-LINE-HEIGHT": "AP-71",
    "UI-TOK-COLOR": "AP-80", "UI-TOK-FONT": "AP-80", "UI-TOK-SPACE": "AP-80", "UI-TOK-RADIUS": "AP-80",
    "UI-TOK-SIZE": "AP-80", "UI-TOK-ARBITRARY": "AP-80",
    "UI-A11Y-CLICKDIV": "QF-07", "UI-A11Y-IMG-ALT": "QF-07", "UI-A11Y-ICON-BUTTON": "QF-07",
    "UI-A11Y-INPUT-LABEL": "QF-08", "UI-HTML-LANG": "QF-13",
}

Finding = collections.namedtuple("Finding", "level rule file line message snippet")


# ------------------------------------------------------------------ tiện ích

class Doc:
    def __init__(self, path, text):
        self.path = path
        self.text = text
        self.is_css = path.lower().endswith(".css")
        self._nl = [i for i, ch in enumerate(text) if ch == "\n"]
        self.no_script = SCRIPT_BLOCK.sub(lambda m: " " * len(m.group(0)), text) if not self.is_css else text
        # Đoạn CSS: (offset, css_text, kind) kind = block | attr
        self.css = []
        if self.is_css:
            self.css.append((0, text, "block"))
        else:
            for m in STYLE_BLOCK.finditer(self.no_script):
                self.css.append((m.start(1), m.group(1), "block"))
            for m in STYLE_ATTR.finditer(self.no_script):
                self.css.append((m.start(1) + 1, m.group(1)[1:-1], "attr"))
        # Chữ hiển thị (thay thẻ bằng khoảng trắng để giữ vị trí)
        if self.is_css:
            self.visible = " " * len(text)
        else:
            t = STYLE_BLOCK.sub(lambda m: " " * len(m.group(0)), self.no_script)
            t = re.sub(r"<helmet\b.*?</helmet>", lambda m: " " * len(m.group(0)), t, flags=re.S | re.I)
            t = re.sub(r"<!--.*?-->", lambda m: " " * len(m.group(0)), t, flags=re.S)
            t = re.sub(r"<[^>]*>", lambda m: " " * len(m.group(0)), t)
            t = re.sub(r"\{\{[^}]*\}\}", lambda m: " " * len(m.group(0)), t)
            self.visible = t

    def line(self, pos):
        lo, hi = 0, len(self._nl)
        while lo < hi:
            mid = (lo + hi) // 2
            if self._nl[mid] < pos:
                lo = mid + 1
            else:
                hi = mid
        return lo + 1

    def snippet(self, pos, length=70):
        s = self.text[max(0, pos - 10):pos + length].replace("\n", " ")
        return re.sub(r"\s+", " ", s).strip()

    def blocks(self):
        """Khối khai báo CSS: [(offset, text)]."""
        out = []
        for off, css, kind in self.css:
            if kind == "attr":
                out.append((off, css))
                continue
            for m in re.finditer(r"\{([^{}]*)\}", css):
                out.append((off + m.start(1), m.group(1)))
        return out

    def declarations(self):
        """[(offset, prop, value, block_index)]"""
        out = []
        for bi, (off, body) in enumerate(self.blocks()):
            pos = 0
            for part in body.split(";"):
                if ":" in part:
                    prop, val = part.split(":", 1)
                    p = prop.strip().lower()
                    if p and re.fullmatch(r"[-a-z]+", p):
                        out.append((off + pos + len(prop) - len(prop.lstrip()), p, val.strip(), bi))
                pos += len(part) + 1
        return out

    def color_contexts(self):
        """Đoạn văn bản có thể chứa màu: CSS, thuộc tính màu SVG, class Tailwind tùy ý."""
        out = [(off, css) for off, css, _ in self.css]
        if not self.is_css:
            for m in COLOR_ATTR.finditer(self.no_script):
                out.append((m.start(2) + 1, m.group(2)[1:-1]))
            for m in CLASS_ATTR.finditer(self.no_script):
                for a in re.finditer(r"-\[([^\]]+)\]", m.group(1)):
                    out.append((m.start(1) + a.start(1), a.group(1)))
        return out

    def classes(self):
        if self.is_css:
            return []
        return [(m.start(1), m.group(1)) for m in CLASS_ATTR.finditer(self.no_script)]


def first_font(value):
    """Font đầu tiên của một font stack. None nếu stack bắt đầu bằng var(...) hoặc {{prop}} (đã dùng token/prop)."""
    for f in re.split(r",(?![^(]*\))", value):
        name = f.strip().strip("\"'").strip()
        if name.startswith("{{") or name.lower().startswith("var("):
            return None
        if not name or name.lower() in FONT_SKIP:
            continue
        return name
    return None


def px_value(token):
    m = re.fullmatch(r"(-?\d*\.?\d+)(px|rem)?", token.strip())
    if not m:
        return None
    n = float(m.group(1))
    if m.group(2) == "rem":
        n *= 16
    return n


# ------------------------------------------------------------------ kiểm

def check(doc, tokens):
    F = []

    def add(level, rule, pos, msg):
        """pos < 0: phát hiện ở mức cả tệp (không có dòng cụ thể)."""
        if pos < 0:
            F.append(Finding(level, rule, doc.path, 0, msg, ""))
        else:
            F.append(Finding(level, rule, doc.path, doc.line(pos), msg, doc.snippet(pos)))

    def check_font(name, pos):
        if not name or name.lower().startswith("katex"):
            return
        ln = name.lower()
        if tokens:
            if ln not in tokens.font_names:
                add("ERROR", "UI-TOK-FONT", pos, "Font ngoài tokens: %s" % name)
        elif ln in FONT_BANNED:
            add("ERROR", "UI-FONT-BANNED", pos, "Font mặc định làm font chính: %s" % name)
        elif ln in FONT_OVERUSED:
            add("WARN", "UI-FONT-OVERUSED", pos, "Font đang thành mặc định mới: %s (cần DD-UI)" % name)

    # --- font tải từ Google Fonts
    for m in re.finditer(r"fonts\.googleapis\.com/css2?\?([^\"'\s>]+)", doc.no_script):
        for fam in re.findall(r"family=([^&:\"']+)", m.group(1)):
            check_font(fam.replace("+", " ").strip(), m.start())

    token_hexes = tokens.color_hexes() if tokens else set()
    if tokens:
        for sv in tokens.shadows:
            for c, _ in uilib.find_colors(str(sv)):
                pc = uilib.parse_color(c)
                if pc:
                    token_hexes.add(uilib.to_hex(pc))

    # --- màu
    seen_tok_colors = {}
    for off, ctx in doc.color_contexts():
        for raw, p in uilib.find_colors(ctx):
            pos = off + p
            before = doc.text[max(0, pos - 30):pos]
            if re.search(r"(?:href|src|action|xlink:href)\s*=\s*[\"']$|url\($", before):
                continue
            c = uilib.parse_color(raw)
            if not c:
                continue
            hx = uilib.to_hex((c[0], c[1], c[2], 1.0))
            in_tokens = hx in token_hexes or uilib.to_hex(c) in token_hexes
            if hx in PURPLE_KNOWN:
                add("ERROR", "UI-PURPLE-KNOWN", pos, "Màu tím/indigo mặc định của giao diện AI: %s" % raw)
            else:
                h, s, l = uilib.hsl_of(c)
                if 235 <= h <= 300 and s >= 0.35 and 0.2 <= l <= 0.85 and c[3] > 0.3 and not in_tokens:
                    add("WARN", "UI-PURPLE-HUE", pos, "Màu thuộc dải tím/indigo/violet (%.0f°): %s" % (h, raw))
            if hx == "#000000" and c[3] >= 0.99:
                add("WARN", "UI-PURE-BLACK", pos, "Đen tuyền chưa pha sắc: %s" % raw)
            if tokens and not in_tokens:
                key = uilib.to_hex(c)
                seen_tok_colors.setdefault(key, []).append(pos)
    for key, poss in seen_tok_colors.items():
        add("ERROR", "UI-TOK-COLOR", poss[0], "Màu ngoài tokens: %s (%d chỗ)" % (key, len(poss)))

    for off, cls in doc.classes():
        for m in TW_PURPLE.finditer(cls):
            add("ERROR", "UI-PURPLE-KNOWN", off + m.start(), "Lớp màu tím/indigo của Tailwind: %s" % m.group(0))
        for m in TW_DEFAULT.finditer(cls):
            add("WARN", "UI-TW-DEFAULT", off + m.start(), "Lớp xám mặc định của Tailwind/shadcn: %s" % m.group(0))
        for m in re.finditer(r"\b(?:bg-gradient-to-\w+|bg-linear-\S+|bg-radial\S*)", cls):
            add("WARN", "UI-GRADIENT", off + m.start(), "Gradient trang trí: %s" % m.group(0))
        for m in re.finditer(r"\bbg-clip-text\b", cls):
            add("ERROR", "UI-GRADIENT-TEXT", off + m.start(), "Chữ gradient (bg-clip-text)")
        for m in re.finditer(r"\bbackdrop-blur\S*", cls):
            add("WARN", "UI-GLASS", off + m.start(), "Glassmorphism: %s" % m.group(0))
        for m in re.finditer(r"\bborder-l-(?:[2-8])\b", cls):
            add("WARN", "UI-LEFT-STRIPE", off + m.start(), "Dải viền trái trên khối: %s" % m.group(0))
        for m in re.finditer(r"\banimate-(?:bounce|ping|wiggle)\b", cls):
            add("WARN", "UI-BOUNCE", off + m.start(), "Chuyển động nảy: %s" % m.group(0))
        if tokens:
            for m in re.finditer(r"\b[\w:-]+-\[[^\]]+\]", cls):
                add("WARN", "UI-TOK-ARBITRARY", off + m.start(), "Giá trị tùy ý của Tailwind, ngoài tokens: %s" % m.group(0))
    rounded = sum(len(re.findall(r"\brounded-(?:2xl|3xl)\b", cls)) for _, cls in doc.classes())
    if rounded >= 5:
        add("WARN", "UI-RADIUS-UNIFORM", -1, "rounded-2xl/3xl dùng %d lần: bo góc lớn đồng loạt" % rounded)

    # --- khai báo CSS
    decls = doc.declarations()
    weights, radii, sizes_seen = set(), [], 0
    uppercase = 0
    wide_shadows = 0
    by_block = collections.defaultdict(dict)
    off_space, off_radius, off_size = {}, {}, {}
    for pos, prop, val, bi in decls:
        v = val.lower()
        by_block[bi][prop] = (val, pos)
        if re.search(r"(?:linear|radial|conic)-gradient\(", v):
            add("WARN", "UI-GRADIENT", pos, "Gradient trang trí trong %s" % prop)
        if prop in ("background-clip", "-webkit-background-clip") and "text" in v:
            add("ERROR", "UI-GRADIENT-TEXT", pos, "Chữ gradient (background-clip: text)")
        if prop in ("backdrop-filter", "-webkit-backdrop-filter") and v not in ("none",):
            add("WARN", "UI-GLASS", pos, "Glassmorphism (backdrop-filter)")
        if prop == "text-shadow" and v != "none":
            add("WARN", "UI-GLOW", pos, "Bóng/glow quanh chữ")
        if prop == "box-shadow" and v != "none":
            for sh in re.split(r",(?![^(]*\))", val):
                lens = [px_value(x) for x in re.findall(r"-?\d*\.?\d+(?:px|rem)?", sh)]
                lens = [x for x in lens if x is not None]
                blur = lens[2] if len(lens) >= 3 else 0
                cols = [uilib.parse_color(c) for c, _ in uilib.find_colors(sh)]
                if len(lens) >= 2 and lens[0] == 0 and lens[1] == 0 and blur >= 8:
                    for c in cols:
                        if c and uilib.hsl_of(c)[1] >= 0.5 and c[3] >= 0.3:
                            add("WARN", "UI-GLOW", pos, "Glow màu quanh khối")
                            break
                if blur >= 24:
                    wide_shadows += 1
        if prop == "font-weight":
            w = {"normal": "400", "bold": "700"}.get(v, v)
            weights.add(w)
        if prop == "font-size":
            sizes_seen += 1
            n = px_value(v.split()[0]) if v else None
            if tokens and n is not None and tokens.font_sizes and ("%gpx" % n) not in tokens.font_sizes:
                off_size.setdefault("%gpx" % n, pos)
        if prop == "text-transform" and "uppercase" in v:
            uppercase += 1
        if prop in ("border-left", "border-inline-start"):
            m = re.search(r"(\d*\.?\d+)px", v)
            if m and 2 <= float(m.group(1)) <= 12 and "solid" in v:
                add("WARN", "UI-LEFT-STRIPE", pos, "Dải viền trái %spx trên khối" % m.group(1))
        if prop in ("border-left-width",):
            n = px_value(v)
            if n and 2 <= n <= 12:
                add("WARN", "UI-LEFT-STRIPE", pos, "Dải viền trái %gpx trên khối" % n)
        if prop == "border-radius":
            for part in v.replace("/", " ").split():
                n = px_value(part)
                if n is None:
                    continue
                if n > 0 and n < 999:
                    radii.append(n)
                if tokens and tokens.radius and n not in (0,) and n < 999 and ("%gpx" % n) not in tokens.radius.values():
                    off_radius.setdefault("%gpx" % n, pos)
        if prop == "font-family" or prop == "font":
            fam = val
            if prop == "font":
                m = re.search(r"\d(?:px|rem|em|%)?(?:/[\d.]+\w*)?\s+(.+)$", val)
                fam = m.group(1) if m else ""
            check_font(first_font(fam) if fam else None, pos)
        if prop in ("transition-timing-function", "animation-timing-function", "transition", "animation"):
            for m in re.finditer(r"cubic-bezier\(([^)]*)\)", v):
                try:
                    nums = [float(x) for x in m.group(1).split(",")]
                    if len(nums) == 4 and (nums[1] > 1 or nums[1] < 0 or nums[3] > 1 or nums[3] < 0):
                        add("WARN", "UI-BOUNCE", pos, "Đường cong nảy/đàn hồi: cubic-bezier(%s)" % m.group(1))
                except ValueError:
                    pass
        if tokens and prop in SPACING_PROPS and tokens.spacing:
            allowed = set(tokens.spacing.values())
            for m in PX.finditer(v):
                n = float(m.group(1)) * (16 if m.group(2) == "rem" else 1)
                key = "%gpx" % abs(n)
                if abs(n) <= 1 or key in allowed:
                    continue
                off_space.setdefault(key, pos)
    for key, pos in off_space.items():
        add("WARN", "UI-TOK-SPACE", pos, "Khoảng cách ngoài tokens: %s" % key)
    for key, pos in off_radius.items():
        add("WARN", "UI-TOK-RADIUS", pos, "Bo góc ngoài tokens: %s" % key)
    for key, pos in off_size.items():
        add("WARN", "UI-TOK-SIZE", pos, "Cỡ chữ ngoài thang chữ của tokens: %s" % key)

    # line-height theo khối
    for bi, props in by_block.items():
        if "line-height" not in props:
            continue
        lhv, pos = props["line-height"]
        fs = px_value(props["font-size"][0].split()[0]) if "font-size" in props and props["font-size"][0] else None
        lh_num = None
        m = re.fullmatch(r"\s*(\d*\.?\d+)\s*", lhv)
        if m:
            lh_num = float(m.group(1))
        else:
            n = px_value(lhv.strip())
            if n is not None and fs:
                lh_num = n / fs
            m2 = re.fullmatch(r"\s*(\d*\.?\d+)%\s*", lhv)
            if m2:
                lh_num = float(m2.group(1)) / 100
        if lh_num is None:
            continue
        if fs is not None and fs <= 20 and lh_num < 1.5:
            add("WARN", "UI-LINE-HEIGHT", pos, "line-height %.2f cho chữ %gpx: tiếng Việt cần ≥ 1.5" % (lh_num, fs))
        elif fs is not None and fs > 20 and lh_num < 1.15:
            add("WARN", "UI-LINE-HEIGHT", pos, "line-height %.2f cho tiêu đề %gpx: dấu chồng dễ chạm dòng (≥ 1.2)" % (lh_num, fs))
        elif fs is None and lh_num < 1.2:
            add("WARN", "UI-LINE-HEIGHT", pos, "line-height %.2f quá chật cho tiếng Việt" % lh_num)
        # viền 1px + bóng rộng cùng khối
    for bi, props in by_block.items():
        if "box-shadow" in props and ("border" in props or "outline" in props):
            bv = props.get("border", props.get("outline"))[0]
            sv, pos = props["box-shadow"]
            lens = [px_value(x) for x in re.findall(r"-?\d*\.?\d+(?:px|rem)?", sv)]
            lens = [x for x in lens if x is not None]
            if re.search(r"\b1px\b", bv) and len(lens) >= 3 and lens[2] >= 16:
                add("WARN", "UI-SHADOW-WIDE", pos, "Viền 1px kèm bóng rộng trên cùng khối")
    if wide_shadows >= 3:
        add("WARN", "UI-SHADOW-WIDE", -1, "%d bóng mờ rộng (blur ≥ 24px): bóng trang trí khắp nơi" % wide_shadows)
    if len(radii) >= 5:
        common, cnt = collections.Counter(radii).most_common(1)[0]
        if common >= 12 and cnt / len(radii) >= 0.8:
            add("WARN", "UI-RADIUS-UNIFORM", -1, "%d/%d khối cùng bo góc %gpx" % (cnt, len(radii), common))
    if sizes_seen >= 3 and len(weights) <= 1:
        add("WARN", "UI-ONE-WEIGHT", -1, "Chỉ %d độ đậm cho %d cỡ chữ" % (len(weights), sizes_seen))
    cls_upper = sum(len(re.findall(r"\buppercase\b", cls)) for _, cls in doc.classes())
    if uppercase + cls_upper >= 3:
        add("WARN", "UI-EYEBROW", -1, "Viết hoa (text-transform: uppercase) dùng %d lần" % (uppercase + cls_upper))

    # chuyển động
    motion = re.search(r"@keyframes|\banimation\s*:|\banimation-name\s*:|transition\s*:[^;\"']*transform|\banimate-",
                       doc.no_script)
    if motion and not re.search(r"prefers-reduced-motion|motion-reduce|motion-safe", doc.no_script):
        add("WARN", "UI-NO-REDUCED-MOTION", motion.start(), "Có chuyển động nhưng không có nhánh prefers-reduced-motion")
    for m in re.finditer(r"@keyframes\s+([\w-]*(?:bounce|elastic|wiggle|jello|rubber|shake)[\w-]*)", doc.no_script, re.I):
        add("WARN", "UI-BOUNCE", m.start(), "Keyframes nảy/lắc: %s" % m.group(1))

    # --- chữ hiển thị
    vis = doc.visible
    for m in EMOJI_ERR.finditer(vis):
        add("ERROR", "UI-EMOJI", m.start(), "Emoji trong giao diện: %r" % m.group(0))
    for m in EMOJI_WARN.finditer(vis):
        add("WARN", "UI-EMOJI", m.start(), "Ký hiệu dingbat %r làm icon: nên dùng SVG của bộ icon" % m.group(0))
    for m in ARROW_IN_ACTION.finditer(doc.no_script):
        add("WARN", "UI-ARROW", m.start(2), "Mũi tên %r trong nút/link" % m.group(2))
    for m in LOREM.finditer(vis):
        add("ERROR", "UI-LOREM", m.start(), "Chữ giữ chỗ: %r" % m.group(0))
    for rx in (CLICHE_EN, CLICHE_VI):
        for m in rx.finditer(vis):
            add("WARN", "UI-CLICHE", m.start(), "Câu chữ sáo rỗng: %r" % m.group(0))
    for m in FAKE_STAT.finditer(vis):
        add("WARN", "UI-FAKE-STAT", m.start(), "Có thể là số liệu không nguồn: %r" % m.group(0))
    for m in FAKE_NAME.finditer(vis):
        add("WARN", "UI-FAKE-NAME", m.start(), "Tên mẫu giả: %r" % m.group(0))

    # --- a11y
    if not doc.is_css:
        src = doc.no_script
        for m in re.finditer(r"<(div|span|li|td|p|section)\b[^>]*\b(?:onclick|on-click|@click|role\s*=\s*[\"']button[\"'])",
                             src, re.I):
            add("ERROR", "UI-A11Y-CLICKDIV", m.start(), "Phần tử <%s> bấm được: dùng <button> hoặc <a href>" % m.group(1))
        for m in re.finditer(r"<img\b(?![^>]*\balt\s*=)[^>]*>", src, re.I):
            add("ERROR", "UI-A11Y-IMG-ALT", m.start(), "<img> thiếu alt")
        for m in re.finditer(r"<button\b([^>]*)>(.*?)</button>", src, re.S | re.I):
            inner = re.sub(r"<[^>]*>", "", m.group(2))
            inner = re.sub(r"\{\{[^}]*\}\}", "x", inner).strip()
            if not inner and not re.search(r"aria-label|aria-labelledby|\btitle\s*=", m.group(1), re.I):
                add("WARN", "UI-A11Y-ICON-BUTTON", m.start(), "Nút chỉ có icon nhưng thiếu aria-label")
        labels_for = set(re.findall(r"<label\b[^>]*\bfor\s*=\s*[\"']([^\"']+)[\"']", src, re.I))
        for m in re.finditer(r"<(input|textarea|select)\b([^>]*)>", src, re.I):
            attrs = m.group(2)
            t = re.search(r"\btype\s*=\s*[\"']?(\w+)", attrs, re.I)
            if m.group(1).lower() == "input" and t and t.group(1).lower() in ("hidden", "submit", "button", "reset", "image"):
                continue
            if re.search(r"aria-label|aria-labelledby", attrs, re.I):
                continue
            idm = re.search(r"\bid\s*=\s*[\"']([^\"']+)[\"']", attrs)
            if idm and idm.group(1) in labels_for:
                continue
            last_open = src.rfind("<label", 0, m.start())
            if last_open != -1 and src.rfind("</label", last_open, m.start()) == -1:
                continue
            add("WARN", "UI-A11Y-INPUT-LABEL", m.start(), "<%s> thiếu nhãn (label for/aria-label)" % m.group(1))
        h = re.search(r"<html\b([^>]*)>", src, re.I)
        if h and not re.search(r"\blang\s*=\s*[\"']vi", h.group(1), re.I):
            add("WARN", "UI-HTML-LANG", h.start(), "<html> nên có lang=\"vi\" (giao diện tiếng Việt)")
    return F


# ------------------------------------------------------------------ ngoại lệ, chạy

def load_exceptions(design_path):
    if not design_path:
        return []
    text = uilib.read(design_path)
    _, rows, _ = uilib.table_after_marker(text, "ui:ap-exceptions")
    out = []
    for r in rows:
        ap = (r.get("ap") or "").strip()
        if not ap or ap in uilib.EMPTY:
            continue
        out.append((ap, (r.get("scope") or "*").strip().strip("`") or "*", (r.get("reason") or "").strip()))
    return out


def apply_exceptions(findings, exceptions, root):
    out = []
    for f in findings:
        ap = AP_OF.get(f.rule, "")
        rel = os.path.relpath(f.file, root) if root else f.file
        base = os.path.basename(f.file)
        hit = None
        for eap, scope, reason in exceptions:
            if eap == ap and (fnmatch.fnmatch(base, scope) or fnmatch.fnmatch(rel, scope) or scope == "*"):
                hit = reason
                break
        if hit is not None:
            out.append(f._replace(level="INFO", message=f.message + " — ngoại lệ đã duyệt: " + (hit or "")))
        else:
            out.append(f)
    return out


def collect(paths):
    files = []
    for p in paths:
        if os.path.isdir(p):
            for dp, dn, fn in os.walk(p):
                dn[:] = [d for d in dn if not d.startswith(".")]
                for n in sorted(fn):
                    if re.search(r"\.(dc\.html|html|htm|css)$", n, re.I):
                        files.append(os.path.join(dp, n))
        elif os.path.isfile(p):
            files.append(p)
        else:
            print("Không tìm thấy: %s" % p, file=sys.stderr)
            sys.exit(2)
    return files


def main():
    uilib.utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", help="tệp hoặc thư mục artboard/CSS")
    ap.add_argument("--tokens", help="tokens.json (chế độ thực thi)")
    ap.add_argument("--design", help="DESIGN.md (bảng ngoại lệ ui:ap-exceptions)")
    ap.add_argument("--json", action="store_true", help="in kết quả dạng JSON")
    ap.add_argument("--quiet", action="store_true", help="chỉ in ERROR và tóm tắt")
    args = ap.parse_args()

    tokens = None
    if args.tokens:
        tokens = uilib.Tokens(args.tokens)
        for e in tokens.errors:
            print("tokens.json: %s" % e, file=sys.stderr)
    files = collect(args.paths)
    exceptions = load_exceptions(args.design)
    root = args.paths[0] if os.path.isdir(args.paths[0]) else os.path.dirname(args.paths[0])
    findings = []
    for f in files:
        doc = Doc(f, uilib.read(f))
        findings.extend(check(doc, tokens))
    findings = apply_exceptions(findings, exceptions, root)

    order = {"ERROR": 0, "WARN": 1, "INFO": 2}
    findings.sort(key=lambda x: (x.file, order[x.level], x.line))
    counts = collections.Counter(f.level for f in findings)
    if args.json:
        print(json.dumps({"mode": "thuc-thi" if tokens else "kham-pha", "files": len(files),
                          "counts": counts, "findings": [f._asdict() for f in findings]}, ensure_ascii=False, indent=1))
    else:
        mode = "thực thi (có tokens)" if tokens else "khám phá"
        print("check_ui — chế độ %s — %d tệp" % (mode, len(files)))
        cur = None
        for f in findings:
            if args.quiet and f.level != "ERROR":
                continue
            if f.file != cur:
                cur = f.file
                print("\n%s" % cur)
            where = ("L%d" % f.line) if f.line else "(tệp)"
            print("  %-5s %-22s %-6s %-6s %s" % (f.level, f.rule, AP_OF.get(f.rule, ""), where, f.message))
            if f.snippet:
                print("        … %s" % f.snippet[:110])
        print("\nTổng: ERROR=%d WARN=%d INFO=%d" % (counts["ERROR"], counts["WARN"], counts["INFO"]))
        by_rule = collections.Counter((f.level, f.rule) for f in findings if f.level != "INFO")
        if by_rule:
            print("Theo luật: " + ", ".join("%s %s×%d" % (lv, r, n) for (lv, r), n in sorted(by_rule.items())))
        if not files:
            print("Không có tệp .dc.html/.html/.css nào để kiểm.")
    sys.exit(1 if counts["ERROR"] else 0)


if __name__ == "__main__":
    main()
