# -*- coding: utf-8 -*-
"""Gói artboard thành HTML tự chứa cho html_to_figma: python3 figma_pack.py <batch> -> figma/<batch>-<n>.html (≤20 artboard/tệp)."""
import base64
import json
import os
import re
import sys

ROOT = "/home/claude/a/out/project"
FONTS = "/home/claude/ds/site/project/fonts"
OUT = "/home/claude/a/figma"
os.makedirs(OUT, exist_ok=True)

batch = sys.argv[1].lower()
per = int(sys.argv[2]) if len(sys.argv) > 2 else 20
canvas = json.load(open(os.path.join(ROOT, "canvas.json"), encoding="utf-8"))


def page_boards(b):
    """Thứ tự artboard theo canvas.json của trang dot-<b> (sáng rồi tối cạnh nhau)."""
    names = []
    def walk(x):
        if isinstance(x, dict):
            for k, v in x.items():
                if isinstance(v, str) and v.endswith(".dc.html") and v.startswith("SCR-"):
                    names.append(v)
                else:
                    walk(v)
        elif isinstance(x, list):
            for v in x:
                walk(v)
    pages = canvas.get("pages") or canvas
    target = None
    if isinstance(pages, list):
        for p in pages:
            if isinstance(p, dict) and (p.get("id") == "dot-" + b or p.get("slug") == "dot-" + b):
                target = p
    walk(target if target is not None else {})
    seen, out = set(), []
    for n in names:
        if n not in seen:
            seen.add(n); out.append(n)
    return out

from bs4 import BeautifulSoup

FRAC = ('display: inline-flex; flex-direction: column; align-items: center; vertical-align: middle; margin: 0 0.15em; line-height: 1.2')


def mathml_to_html(fragment):
    """Figma chuyển MathML thành chữ chồng lên nhau: đổi công thức sang HTML thường (chỉ cho bản Figma)."""
    if "<math" not in fragment:
        return fragment
    soup = BeautifulSoup(fragment, "html.parser")

    def conv(node):
        if isinstance(node, str):
            return node.replace("<", "&lt;")
        name = node.name
        inner = "".join(conv(c) for c in node.children)
        if name == "mi":
            return "<i>%s</i>" % inner if len(node.get_text()) == 1 else "<span>%s</span>" % inner
        if name in ("mn", "mtext", "mrow", "semantics"):
            return "<span>%s</span>" % inner
        if name == "mo":
            return "<span style=\"margin: 0 0.12em\">%s</span>" % inner
        if name == "msup":
            kids = [c for c in node.children if not isinstance(c, str)]
            return "<span>%s<sup>%s</sup></span>" % (conv(kids[0]), "".join(conv(k) for k in kids[1:])) if kids else inner
        if name == "msub":
            kids = [c for c in node.children if not isinstance(c, str)]
            return "<span>%s<sub>%s</sub></span>" % (conv(kids[0]), "".join(conv(k) for k in kids[1:])) if kids else inner
        if name == "mfrac":
            kids = [c for c in node.children if not isinstance(c, str)]
            if len(kids) == 2:
                return ("<span style=\"%s\"><span>%s</span><span style=\"border-top: 1px solid currentColor; padding-top: 1px\">%s</span></span>"
                        % (FRAC, conv(kids[0]), conv(kids[1])))
            return inner
        if name == "msqrt":
            return "<span>√<span style=\"border-top: 1px solid currentColor\">%s</span></span>" % inner
        if name == "math":
            return "<span class=\"fx-math\">%s</span>" % inner
        if name == "annotation":
            return ""
        return "".join(conv(c) for c in node.children) if name is None else str(node).replace(str(node), "<span>%s</span>" % inner)

    SUP = str.maketrans("0123456789+-−=()n'′", "⁰¹²³⁴⁵⁶⁷⁸⁹⁺⁻⁻⁼⁽⁾ⁿ'′")
    SUB = str.maketrans("0123456789+-−=()", "₀₁₂₃₄₅₆₇₈₉₊₋₋₌₍₎")

    def plain(node):
        """Công thức trong dòng -> chữ Unicode liền một mạch (Figma tách sai dòng khi có phần tử lồng giữa đoạn)."""
        if isinstance(node, str):
            return node
        name = node.name
        kids = [c for c in node.children if not isinstance(c, str) or c.strip()]
        if name == "annotation":
            return ""
        if name == "mo":
            t = node.get_text().strip()
            if t == ",":
                return ", "
            return " %s " % t if t in "=+−-<>≤≥≠×÷→⇒" and t else t
        if name in ("msup", "msub") and len(kids) >= 2:
            base, ex = plain(kids[0]), "".join(plain(k) for k in kids[1:]).strip()
            tab = SUP if name == "msup" else SUB
            ok = all(ch in "0123456789+-−=()n'′" for ch in ex) if name == "msup" else all(ch in "0123456789+-−=()" for ch in ex)
            return base + (ex.translate(tab) if ok else ("^(%s)" if name == "msup" else "_(%s)") % ex)
        if name == "mfrac" and len(kids) == 2:
            a, b = plain(kids[0]).strip(), plain(kids[1]).strip()
            wrap = lambda x: x if len(x) <= 2 or x.startswith("(") else "(%s)" % x
            return "%s/%s" % (wrap(a), wrap(b))
        if name == "msqrt":
            inner = "".join(plain(c) for c in node.children).strip()
            return "√" + (inner if len(inner) <= 2 else "(%s)" % inner)
        return "".join(plain(c) for c in node.children)

    for m in soup.find_all("math"):
        if m.get("display") == "block":
            m.replace_with(BeautifulSoup(conv(m), "html.parser"))
        else:
            txt = " ".join(plain(m).split()).replace("( ", "(").replace(" )", ")")
            m.replace_with(txt)
    return str(soup)


boards = page_boards(batch)
if not boards:
    heights = json.load(open("/home/claude/a/qa/heights_%s.json" % batch))
    boards = list(heights.keys())
if os.environ.get("ONLY_MATH"):
    boards = [b for b in boards if "<math" in open(os.path.join(ROOT, b), encoding="utf-8").read()]

css_tok = open(os.path.join(ROOT, "ds/ishare/tokens.css"), encoding="utf-8").read()
for f in os.listdir(FONTS):
    if f.endswith(".woff2"):
        b64 = base64.b64encode(open(os.path.join(FONTS, f), "rb").read()).decode()
        css_tok = css_tok.replace("url('./fonts/%s')" % f, "url(data:font/woff2;base64,%s) format('woff2')" % b64)
css_bundle = open(os.path.join(ROOT, "ds/ishare/components/bundle.css"), encoding="utf-8").read()
g = base64.b64encode(open("/home/claude/a/google-g.svg", "rb").read()).decode()
G_URI = "data:image/svg+xml;base64," + g


def board(name):
    s = open(os.path.join(ROOT, name), encoding="utf-8").read()
    m = re.search(r'"\$preview":\{"width":(\d+),"height":(\d+)\}', s)
    w, h = int(m.group(1)), int(m.group(2))
    helmet = re.search(r"<helmet>\s*<style>(.*?)</style>\s*</helmet>", s, re.S).group(1)
    body = s.split("</helmet>", 1)[1].split("</x-dc>", 1)[0].strip()
    body = body.replace("/_blob/dc5a5d64318dca708097b9c84dbc5eff", G_URI)
    body = mathml_to_html(body)
    label = name[:-len(".dc.html")]
    return helmet, ('<section class="ab" id="%s" data-name="%s" aria-label="%s" style="position: relative; width: %dpx; height: %dpx; overflow: hidden; flex: none">%s</section>'
                    % (label, label, label, w, h, body))


chunks = [boards[i:i + per] for i in range(0, len(boards), per)]
for ci, ch in enumerate(chunks, 1):
    helm, parts = "", []
    for n in ch:
        hm, sec = board(n)
        helm = helm or hm
        parts.append(sec)
    doc = ('<!doctype html><html lang="vi"><head><meta charset="utf-8"><title>iShare — %s</title><style>%s\n%s\n%s\n'
           'body{display:flex;flex-direction:column;align-items:flex-start;gap:80px;padding:40px;background:#e9ebe6}</style></head><body>%s</body></html>'
           % (batch.upper(), css_tok, css_bundle, helm, "\n".join(parts)))
    p = os.path.join(OUT, "%s%s-%d.html" % (batch, "m" if os.environ.get("ONLY_MATH") else "", ci))
    open(p, "w", encoding="utf-8").write(doc)
    print(p, len(ch), "%.1f KB" % (len(doc) / 1024), ch[0], "...", ch[-1])
