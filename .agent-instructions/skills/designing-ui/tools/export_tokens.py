#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""export_tokens.py - sinh tokens.css (Tailwind v4) và tokens.dtcg.json từ tokens.json.

tokens.json theo định dạng Design System của Claude Design là nguồn sự thật. Hai tệp sinh ra KHÔNG sửa tay.

  python3 export_tokens.py --tokens output/tokens/tokens.json --out-dir output/tokens [--prefix ""]

tokens.css:
- Khối @theme cho Tailwind v4: --color-<tên>, --font-<họ>, --text-<kiểu> (+ --line-height, --font-weight,
  --letter-spacing), --spacing-<bậc>, --radius-<cỡ>, --shadow-<mức>. Tailwind sinh lớp tiện ích từ đó
  (bg-surface, text-ink, font-body, text-h1, p-4, rounded-md, shadow-1). Biến cũng dùng được trực tiếp bằng var().
- Theme phụ (ví dụ dark): khối [data-theme="<id>"] ghi đè các --color-* khác theme chính.
Dùng trong app: @import "tailwindcss"; rồi @import "./tokens.css";

tokens.dtcg.json: cùng tokens ở định dạng Design Tokens Community Group (2025.10) để đưa sang công cụ khác
(Figma Variables qua plugin, Style Dictionary...). Theme phụ nằm trong $extensions."ishare.themes".
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


def css_name(s):
    return re.sub(r"[^A-Za-z0-9_-]", "-", s)


def strip_prefix(family, name):
    for p in STRIP.get(family, ()):
        if name.startswith(p):
            return name[len(p):]
    return name


def color_value(tokens, name, theme):
    """Giá trị CSS của một token màu: bí danh → var(--color-khác), còn lại giữ nguyên chuỗi gốc."""
    vals = tokens.raw_colors[name]
    v = vals.get(theme, vals.get(tokens.themes[0]))
    if v is None:
        return None
    m = re.fullmatch(r"\{([A-Za-z0-9][A-Za-z0-9_.-]*)\}", v.strip())
    if m:
        return "var(--color-%s)" % css_name(m.group(1))
    return v.strip()


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
    for fam in ("spacing", "radius", "shadow"):
        toks = (tokens.data.get(fam, {}) or {}).get("tokens", []) or []
        if toks:
            lines.append("  /* %s */" % fam)
            for t in toks:
                n = css_name(strip_prefix(fam, t.get("name", "")))
                v = t.get("value")
                if n and v is not None:
                    lines.append("  --%s-%s: %s;" % (NS[fam], n, _len(v) if fam != "shadow" else v))
    other = [k for k in tokens.data if k not in ("name", "version", "color", "type", "spacing", "radius", "shadow",
                                                  "meta")]
    for fam in other:
        block = tokens.data.get(fam)
        if isinstance(block, dict) and isinstance(block.get("tokens"), list):
            lines.append("  /* %s */" % fam)
            for t in block["tokens"]:
                if t.get("name") and t.get("value") is not None:
                    lines.append("  --%s-%s: %s;" % (css_name(fam), css_name(t["name"]), t["value"]))
    lines.append("}")
    for th in tokens.themes[1:]:
        over = []
        for name, vals in tokens.raw_colors.items():
            if th in vals and vals.get(th) != vals.get(main):
                over.append("  --color-%s: %s;" % (css_name(name), color_value(tokens, name, th)))
        if over:
            lines += ["", '[data-theme="%s"] {' % th] + over + ["}"]
    return "\n".join(lines) + "\n"


def _len(v, unitless_ok=False):
    if isinstance(v, (int, float)):
        return ("%g" % v) if unitless_ok else ("%gpx" % v)
    return str(v)


def build_dtcg(tokens):
    out = {}
    main = tokens.themes[0]
    if tokens.raw_colors:
        out["color"] = {}
        for name, vals in tokens.raw_colors.items():
            v = vals.get(main)
            m = re.fullmatch(r"\{([A-Za-z0-9][A-Za-z0-9_.-]*)\}", (v or "").strip())
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
    for fam, typ_name in (("spacing", "dimension"), ("radius", "dimension"), ("shadow", "shadow")):
        toks = (tokens.data.get(fam, {}) or {}).get("tokens", []) or []
        if toks:
            out[fam] = {}
            for t in toks:
                e = {"$type": typ_name, "$value": t.get("value")}
                if t.get("usage"):
                    e["$description"] = t["usage"]
                out[fam][t.get("name")] = e
    return out


def main():
    uilib.utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--tokens", required=True)
    ap.add_argument("--out-dir", required=True)
    args = ap.parse_args()
    tokens = uilib.Tokens(args.tokens)
    if tokens.errors:
        for e in tokens.errors:
            print("tokens.json: %s" % e, file=sys.stderr)
        sys.exit(1)
    # tên trùng giữa các nhóm
    names = list(tokens.raw_colors)
    for fam in ("spacing", "radius", "shadow"):
        names += [t.get("name") for t in (tokens.data.get(fam, {}) or {}).get("tokens", []) or []]
    dup = {n for n in names if names.count(n) > 1}
    if dup:
        print("Tên token trùng giữa các nhóm: %s" % ", ".join(sorted(dup)), file=sys.stderr)
        sys.exit(1)
    os.makedirs(args.out_dir, exist_ok=True)
    title = tokens.data.get("name") or "iShare"
    css = build_css(tokens, title)
    uilib.write(os.path.join(args.out_dir, "tokens.css"), css)
    uilib.write(os.path.join(args.out_dir, "tokens.dtcg.json"),
                json.dumps(build_dtcg(tokens), ensure_ascii=False, indent=2) + "\n")
    n_vars = css.count("\n  --")
    print("Đã ghi %s (%d biến, theme: %s) và tokens.dtcg.json" % (os.path.join(args.out_dir, "tokens.css"), n_vars,
                                                                   ", ".join(tokens.themes)))


if __name__ == "__main__":
    main()
