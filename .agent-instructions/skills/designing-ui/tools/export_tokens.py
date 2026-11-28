#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""export_tokens.py - sinh tokens.css (Tailwind v4), tokens.dtcg.json và (tùy chọn) tệp CSS thuần từ tokens.json.

tokens.json theo định dạng Design System của Claude Design là nguồn sự thật. Các tệp sinh ra KHÔNG sửa tay.

  python3 export_tokens.py --tokens output/tokens/tokens.json --out-dir output/tokens \
      [--plain output/handoff/css/tokens.vars.css] [--font-url-prefix ./]

tokens.css (luôn sinh):
- Khối @theme cho Tailwind v4: --color-<tên>, --font-<họ>, --text-<kiểu> (+ --line-height, --font-weight,
  --letter-spacing), --spacing-<bậc>, --radius-<cỡ>, --shadow-<mức>, --<nhóm khác>-<tên>. Tailwind sinh lớp tiện
  ích từ đó (bg-surface, text-ink, font-body, text-h1, p-4, rounded-md, shadow-1).
- Theme phụ (ví dụ dark): khối [data-theme="<id>"] ghi lại các --color-* khai báo riêng cho theme đó và mọi màu là
  bí danh (để đúng cả khi data-theme đặt trên phần tử con), cùng mọi token khác (ví dụ bóng) có giá trị riêng.
- Chỉ dùng được khi có Tailwind: @import "tailwindcss"; rồi @import "./tokens.css";. Không có Tailwind thì trình
  duyệt bỏ qua cả khối @theme — dùng tệp CSS thuần (--plain) thay thế.

Tệp CSS thuần (--plain <tệp>, cho app không dùng Tailwind):
- Biến mang đúng tên token, không tiền tố nhóm: --ink, --primary-soft, --space-4, --radius-sm, --shadow-1,
  --control-h; họ font --font-<họ>. Cùng tên với tokens.css mà Claude Design sinh cho design system.
- :root, [data-theme="<theme chính>"] chứa mọi màu và các token có giá trị theo theme; mỗi theme phụ một khối
  [data-theme="<id>"]; token không đổi theo theme nằm trong :root.
- Lớp kiểu chữ .<kiểu> (font-family, font-size, line-height, font-weight, letter-spacing) và @font-face cho các tệp
  font trong tokens.json (đường dẫn = --font-url-prefix + "file", mặc định "./").

Giá trị theo theme: một token (màu, bóng hoặc nhóm khác) có "value" là đối tượng {"<theme>": "<giá trị>", ...}; theme
thiếu lấy giá trị của theme chính.

tokens.dtcg.json: cùng tokens ở định dạng Design Tokens Community Group để đưa sang công cụ khác (Figma Variables qua
plugin, Style Dictionary...). Giá trị của theme chính nằm ở $value; theme phụ nằm trong $extensions."ishare.themes".
Bóng ghi dạng đối tượng shadow (color, offsetX, offsetY, blur, spread, inset; nhiều lớp thành mảng).
"""
import argparse
import json
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uilib  # noqa: E402

STRIP = {"spacing": ("spacing-", "space-"), "radius": ("radius-", "rounded-"), "shadow": ("shadow-", "elevation-")}
NS = {"spacing": "spacing", "radius": "radius", "shadow": "shadow"}
SKIP = ("name", "version", "color", "type", "meta")
ALIAS = re.compile(r"\{([A-Za-z0-9][A-Za-z0-9_.-]*)\}")


def css_name(s):
    return re.sub(r"[^A-Za-z0-9_-]", "-", s)


def strip_prefix(family, name):
    for p in STRIP.get(family, ()):
        if name.startswith(p):
            return name[len(p):]
    return name


def _len(v, unitless_ok=False):
    if isinstance(v, (int, float)):
        return ("%g" % v) if unitless_ok else ("%gpx" % v)
    return str(v)


def families(tokens):
    """Các nhóm token dạng {"tokens": [...]} ngoài màu và kiểu chữ, theo thứ tự trong tokens.json."""
    out = []
    for fam, block in tokens.data.items():
        if fam in SKIP:
            continue
        if isinstance(block, dict) and isinstance(block.get("tokens"), list):
            out.append((fam, [t for t in block["tokens"] if t.get("name") and t.get("value") is not None]))
    return out


def themed(tokens, value):
    """{theme: giá trị} cho mọi theme; giá trị không theo theme thì như nhau ở mọi theme."""
    main = tokens.themes[0]
    if isinstance(value, dict) and value and set(value) <= set(tokens.themes):
        base = value.get(main, next(iter(value.values())))
        return {th: value.get(th, base) for th in tokens.themes}, True
    return {th: value for th in tokens.themes}, False


def color_value(tokens, name, theme, prefix="color-"):
    """Giá trị CSS của một token màu: bí danh → var(--<prefix>khác), còn lại giữ nguyên chuỗi gốc."""
    vals = tokens.raw_colors[name]
    v = vals.get(theme, vals.get(tokens.themes[0]))
    if v is None:
        return None
    m = ALIAS.fullmatch(v.strip())
    if m:
        return "var(--%s%s)" % (prefix, css_name(m.group(1)))
    return v.strip()


def color_in_theme(tokens, name, th):
    """Màu có mặt trong khối theme: theme chính có mọi màu; theme phụ có màu khai báo riêng cho theme đó và mọi màu là
    bí danh (var(--khác)) — khai báo lại để bí danh trỏ đúng giá trị khi data-theme đặt trên một phần tử con."""
    vals = tokens.raw_colors[name]
    if th == tokens.themes[0] or th in vals:
        return True
    return bool(ALIAS.fullmatch((vals.get(tokens.themes[0]) or "").strip()))


def fam_var(fam, name):
    """Tên biến trong tokens.css (Tailwind)."""
    if fam in NS:
        return "--%s-%s" % (NS[fam], css_name(strip_prefix(fam, name)))
    return "--%s-%s" % (css_name(fam), css_name(name))


def fam_val(fam, v):
    return _len(v) if fam in ("spacing", "radius") else str(v)


# ---------------------------------------------------------------- tokens.css (Tailwind v4)

def build_css(tokens, title):
    lines = ["/* %s — generated from tokens.json by export_tokens.py; do not edit by hand */" % title, "",
             "@theme {"]
    main = tokens.themes[0]
    if tokens.raw_colors:
        lines.append("  /* color (theme: %s) */" % main)
        for name in tokens.raw_colors:
            v = color_value(tokens, name, main)
            if v:
                lines.append("  --color-%s: %s;" % (css_name(name), v))
    typ = tokens.data.get("type", {}) or {}
    fams = typ.get("families") or {}
    if fams:
        lines.append("  /* font families */")
        for k, v in fams.items():
            lines.append("  --font-%s: %s;" % (css_name(k), v))
    if tokens.type_styles:
        lines.append("  /* text styles */")
        for s in tokens.type_styles:
            n = css_name(s.get("name", ""))
            if not n:
                continue
            if s.get("fontSize") is not None:
                lines.append("  --text-%s: %s;" % (n, _len(s["fontSize"])))
            if s.get("lineHeight") is not None:
                lines.append("  --text-%s--line-height: %s;" % (n, _len(s["lineHeight"], unitless_ok=True)))
            if s.get("fontWeight") is not None:
                lines.append("  --text-%s--font-weight: %s;" % (n, s["fontWeight"]))
            if s.get("letterSpacing") is not None:
                lines.append("  --text-%s--letter-spacing: %s;" % (n, _len(s["letterSpacing"])))
    over = {th: [] for th in tokens.themes[1:]}
    for fam, toks in families(tokens):
        if not toks:
            continue
        lines.append("  /* %s */" % fam)
        for t in toks:
            vals, by_theme = themed(tokens, t["value"])
            lines.append("  %s: %s;" % (fam_var(fam, t["name"]), fam_val(fam, vals[main])))
            if by_theme:
                for th in tokens.themes[1:]:
                    if vals[th] != vals[main]:
                        over[th].append("  %s: %s;" % (fam_var(fam, t["name"]), fam_val(fam, vals[th])))
    lines.append("}")
    for th in tokens.themes[1:]:
        block = []
        for name in tokens.raw_colors:
            if color_in_theme(tokens, name, th):
                block.append("  --color-%s: %s;" % (css_name(name), color_value(tokens, name, th)))
        block += over[th]
        if block:
            lines += ["", '[data-theme="%s"] {' % th] + block + ["}"]
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- CSS thuần

def _q(family):
    return "'%s'" % family.strip().strip("\"'")


def build_plain(tokens, title, font_prefix="./"):
    main = tokens.themes[0]
    themes = {th: [] for th in tokens.themes}
    common = []
    for name in tokens.raw_colors:
        for th in tokens.themes:
            if color_in_theme(tokens, name, th):
                v = color_value(tokens, name, th, prefix="")
                if v:
                    themes[th].append("  --%s: %s;" % (css_name(name), v))
    for fam, toks in families(tokens):
        for t in toks:
            vals, by_theme = themed(tokens, t["value"])
            n = "--%s" % css_name(t["name"])
            if by_theme:
                for th in tokens.themes:
                    if th == main or vals[th] != vals[main]:
                        themes[th].append("  %s: %s;" % (n, fam_val(fam, vals[th])))
            else:
                common.append("  %s: %s;" % (n, fam_val(fam, vals[main])))
    typ = tokens.data.get("type", {}) or {}
    for k, v in (typ.get("families") or {}).items():
        common.append("  --font-%s: %s;" % (css_name(k), v))

    lines = ["/* %s — plain CSS variables, generated from tokens.json by export_tokens.py --plain; do not edit by hand */"
             % title, ""]
    lines += [':root, [data-theme="%s"] {' % main] + themes[main] + ["}"]
    for th in tokens.themes[1:]:
        if themes[th]:
            lines += ["", '[data-theme="%s"] {' % th] + themes[th] + ["}"]
    if common:
        lines += ["", ":root {"] + common + ["}"]
    styles = [s for s in tokens.type_styles if s.get("name")]
    if styles:
        lines.append("")
        for s in styles:
            decl = []
            if s.get("family"):
                decl.append("font-family: var(--font-%s)" % css_name(s["family"]))
            if s.get("fontSize") is not None:
                decl.append("font-size: %s" % _len(s["fontSize"]))
            if s.get("lineHeight") is not None:
                decl.append("line-height: %s" % _len(s["lineHeight"], unitless_ok=True))
            if s.get("fontWeight") is not None:
                decl.append("font-weight: %s" % s["fontWeight"])
            if s.get("letterSpacing") is not None:
                decl.append("letter-spacing: %s" % _len(s["letterSpacing"]))
            lines.append(".%s { %s; }" % (css_name(s["name"]), "; ".join(decl)))
    fonts = [f for f in (typ.get("fonts") or []) if f.get("family") and f.get("file")]
    if fonts:
        lines.append("")
        for f in fonts:
            file = f["file"][2:] if f["file"].startswith("./") else f["file"]
            src = "url('%s%s')" % (font_prefix, file)
            if f["file"].lower().endswith(".woff2"):
                src += " format('woff2')"
            lines.append("@font-face { font-family: %s; src: %s; font-weight: %s; font-style: %s; }"
                         % (_q(f["family"]), src, f.get("weight", "400"), f.get("style", "normal")))
    return "\n".join(lines) + "\n"


# ---------------------------------------------------------------- tokens.dtcg.json

def _split_top(s, sep=","):
    out, depth, cur = [], 0, ""
    for ch in s:
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth -= 1
        if ch == sep and depth == 0:
            out.append(cur)
            cur = ""
        else:
            cur += ch
    out.append(cur)
    return [x.strip() for x in out if x.strip()]


LEN = re.compile(r"^-?\d*\.?\d+(px|rem|em)?$")


def shadow_dtcg(v):
    """Chuỗi box-shadow → đối tượng shadow DTCG (mảng nếu nhiều lớp); không đọc được thì trả None."""
    if not isinstance(v, str):
        return None
    layers = []
    for part in _split_top(v):
        words = []
        buf = part
        m = re.search(r"(rgba?|hsla?|oklch|oklab|color)\([^)]*\)|#[0-9A-Fa-f]{3,8}\b", buf)
        color = None
        if m:
            color = m.group(0)
            buf = (buf[:m.start()] + " " + buf[m.end():]).strip()
        inset = False
        for w in buf.split():
            if w == "inset":
                inset = True
            elif LEN.match(w):
                words.append(w if not re.match(r"^-?\d*\.?\d+$", w) else ("%spx" % w if w not in ("0", "-0") else "0px"))
            elif color is None:
                color = w
            else:
                return None
        if color is None or not 2 <= len(words) <= 4:
            return None
        words += ["0px"] * (4 - len(words))
        layer = {"color": color, "offsetX": words[0], "offsetY": words[1], "blur": words[2], "spread": words[3]}
        if inset:
            layer["inset"] = True
        layers.append(layer)
    if not layers:
        return None
    return layers[0] if len(layers) == 1 else layers


def build_dtcg(tokens, warn):
    out = {}
    main = tokens.themes[0]
    if tokens.raw_colors:
        out["color"] = {}
        for name, vals in tokens.raw_colors.items():
            v = vals.get(main)
            m = ALIAS.fullmatch((v or "").strip())
            entry = {"$type": "color", "$value": ("{color.%s}" % m.group(1)) if m else v}
            extra = {th: vals[th] for th in tokens.themes[1:] if th in vals}
            if extra:
                entry["$extensions"] = {"ishare.themes": extra}
            out["color"][name] = entry
    typ = tokens.data.get("type", {}) or {}
    if typ.get("families"):
        out["fontFamily"] = {k: {"$type": "fontFamily", "$value": [x.strip().strip("\"'") for x in v.split(",")]}
                             for k, v in typ["families"].items()}
    if tokens.type_styles:
        out["typography"] = {}
        for s in tokens.type_styles:
            val = {}
            if s.get("family"):
                val["fontFamily"] = "{fontFamily.%s}" % s["family"]
            for k in ("fontSize", "lineHeight", "fontWeight", "letterSpacing"):
                if s.get(k) is not None:
                    val[k] = s[k]
            out["typography"][s.get("name", "style")] = {"$type": "typography", "$value": val}
    types = {"spacing": "dimension", "radius": "dimension", "shadow": "shadow"}
    for fam, toks in families(tokens):
        if not toks:
            continue
        out[fam] = {}
        for t in toks:
            vals, by_theme = themed(tokens, t["value"])
            typ_name = types.get(fam) or ("dimension" if all(isinstance(x.get("value"), (int, float)) or
                                                            LEN.match(str(x.get("value"))) for x in toks) else None)

            def conv(x):
                if typ_name == "shadow":
                    sh = shadow_dtcg(x)
                    if sh is None:
                        warn.append("shadow %s: không đọc được '%s', giữ chuỗi" % (t["name"], x))
                        return x
                    return sh
                return x

            e = {"$value": conv(vals[main])}
            if typ_name:
                e = {"$type": typ_name, "$value": e["$value"]}
            if by_theme:
                extra = {th: conv(vals[th]) for th in tokens.themes[1:] if vals[th] != vals[main]}
                if extra:
                    e["$extensions"] = {"ishare.themes": extra}
            if t.get("usage"):
                e["$description"] = t["usage"]
            out[fam][t["name"]] = e
    return out


def main():
    uilib.utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tokens", required=True)
    ap.add_argument("--out-dir", required=True, help="thư mục ghi tokens.css và tokens.dtcg.json")
    ap.add_argument("--plain", metavar="TỆP", help="ghi thêm tệp CSS thuần (không Tailwind), ví dụ tokens.vars.css")
    ap.add_argument("--font-url-prefix", default="./", help="tiền tố đường dẫn font trong @font-face của tệp --plain")
    args = ap.parse_args()
    tokens = uilib.Tokens(args.tokens)
    if tokens.errors:
        for e in tokens.errors:
            print("tokens.json: %s" % e, file=sys.stderr)
        sys.exit(1)
    # tên trùng giữa các nhóm (tệp CSS thuần dùng tên token trần nên tên phải duy nhất)
    names = list(tokens.raw_colors)
    for _, toks in families(tokens):
        names += [t.get("name") for t in toks]
    dup = {n for n in names if names.count(n) > 1}
    if dup:
        print("Tên token trùng giữa các nhóm: %s" % ", ".join(sorted(dup)), file=sys.stderr)
        sys.exit(1)
    os.makedirs(args.out_dir, exist_ok=True)
    title = tokens.data.get("name") or "iShare"
    css = build_css(tokens, title)
    uilib.write(os.path.join(args.out_dir, "tokens.css"), css)
    warn = []
    uilib.write(os.path.join(args.out_dir, "tokens.dtcg.json"),
                json.dumps(build_dtcg(tokens, warn), ensure_ascii=False, indent=2) + "\n")
    for w in warn:
        print("CẢNH BÁO %s" % w, file=sys.stderr)
    n_vars = css.count("\n  --")
    print("Đã ghi %s (%d biến, theme: %s) và tokens.dtcg.json" % (os.path.join(args.out_dir, "tokens.css"), n_vars,
                                                                   ", ".join(tokens.themes)))
    if args.plain:
        plain = build_plain(tokens, title, args.font_url_prefix)
        d = os.path.dirname(os.path.abspath(args.plain))
        os.makedirs(d, exist_ok=True)
        uilib.write(args.plain, plain)
        print("Đã ghi %s (CSS thuần, %d biến)" % (args.plain, plain.count("\n  --")))


if __name__ == "__main__":
    main()
