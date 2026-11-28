#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""font_test.py - sinh trang thử font với tiếng Việt nhiều dấu chồng và công thức.

Mỗi font được hiển thị ở nhiều cỡ chữ và line-height, với: bảng chữ có dấu chồng (hoa và thường), tiêu đề viết hoa,
đoạn văn dài xuống dòng (để thấy dấu của dòng dưới có chạm chữ dòng trên không), công thức inline (MathML).
Font dự phòng là monospace: ký tự nào trông như chữ máy đánh chữ nghĩa là font THIẾU glyph tiếng Việt đó.

  python3 font_test.py --font "Be Vietnam Pro:400;700" --font "Literata:400;600" --out font-test.dc.html
  python3 font_test.py --font "Newsreader:400;600" --sizes 40,24,17,14 --line-heights 1.2,1.3,1.6,1.5 --plain --out font-test.html

Mặc định ra artboard Claude Design (.dc.html, rộng 1440). --plain ra HTML thường để mở bằng trình duyệt.
"""
import argparse
import html
import os
import sys
import urllib.parse

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uilib  # noqa: E402

UPPER = "ẤẦẨẪẬ ẮẰẲẴẶ ẾỀỂỄỆ ỐỒỔỖỘ ỚỜỞỠỢ ỨỪỬỮỰ ỲỶỸỴ Đ"
LOWER = "ấầẩẫậ ắằẳẵặ ếềểễệ ốồổỗộ ớờởỡợ ứừửữự ỳỷỹỵ đ"
TITLE = "ĐỀ THI THỬ TỐT NGHIỆP THPT: giải phương trình bậc hai bằng mấy cách?"
PARA = ("Những người Việt ở Quảng Ngãi đều kể chuyện ngày ấy rất hấp dẫn. Thuở ấy, ở ngoài kia, những mầm xanh "
        "đã nảy lộc; Ỷ Lan, Ửng Hồng và Ngữ Yến cùng ôn bài Lịch sử, rồi hỏi nhau về Chiến dịch Điện Biên Phủ "
        "và Hiệp định Giơ-ne-vơ năm 1954.")
MATH = ('<math><mi>x</mi><mo>=</mo><mfrac><mrow><mo>−</mo><mi>b</mi><mo>±</mo><msqrt><mi>Δ</mi></msqrt></mrow>'
        '<mrow><mn>2</mn><mi>a</mi></mrow></mfrac></math>')
LABEL_STYLE = "font-family: ui-monospace, monospace; font-size: 12px; line-height: 1.5; color: #5a5650"


def parse_font(spec):
    name, _, w = spec.partition(":")
    weights = [x.strip() for x in w.replace(",", ";").split(";") if x.strip()] or ["400", "700"]
    return name.strip(), weights


def gf_url(fonts):
    fams = []
    for name, weights in fonts:
        fams.append("family=%s:wght@%s" % (urllib.parse.quote_plus(name), ";".join(sorted(set(weights), key=int))))
    return "https://fonts.googleapis.com/css2?%s&display=swap" % "&".join(fams)


def block(name, weights, sizes, lhs):
    fam = "'%s', monospace" % name.replace("'", "")
    out = ['<section style="display: flex; flex-direction: column; gap: 16px; padding: 32px 0; '
           'border-top: 1px solid #d8d3ca">',
           '<p style="%s; margin: 0">%s — độ đậm %s — dự phòng: monospace (thấy chữ kiểu máy đánh chữ = thiếu glyph)</p>'
           % (LABEL_STYLE, html.escape(name), ", ".join(weights))]
    for size, lh in zip(sizes, lhs):
        for w in (weights[0], weights[-1]) if len(weights) > 1 else (weights[0],):
            st = "font-family: %s; font-size: %spx; line-height: %s; font-weight: %s; color: #1d1b18; margin: 0" % (
                fam, size, lh, w)
            out.append('<p style="%s; margin: 0">%spx / %s / %s</p>' % (LABEL_STYLE, size, lh, w))
            out.append('<p style="%s">%s</p>' % (st, UPPER))
            out.append('<p style="%s">%s</p>' % (st, LOWER))
            if float(size) >= 24:
                out.append('<p style="%s; max-width: 900px">%s</p>' % (st, html.escape(TITLE)))
            else:
                out.append('<p style="%s; max-width: 560px">%s Nghiệm: %s.</p>' % (st, html.escape(PARA), MATH))
    out.append("</section>")
    return "\n".join(out)


def build(fonts, sizes, lhs, plain):
    url = gf_url(fonts)
    body = "\n".join(block(n, w, sizes, lhs) for n, w in fonts)
    head_note = ('<p style="%s; margin: 0">Thử font tiếng Việt — iShare (sinh bởi font_test.py). Kiểm: dấu chồng không '
                 'đè nhau, không chạm dòng trên, không bị cắt; công thức inline không làm lệch dòng.</p>' % LABEL_STYLE)
    root = ('<div style="width: 100%%; max-width: 1440px; box-sizing: border-box; padding: 48px 64px; '
            'background: #fbf9f4; display: flex; flex-direction: column">\n%s\n%s\n</div>' % (head_note, body))
    est_h = 140 + len(fonts) * (60 + len(sizes) * 2 * 210)
    if plain:
        return ('<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n<title>Thử font tiếng Việt</title>\n'
                '<link rel="stylesheet" href="%s">\n<style>body{margin:0}</style>\n</head>\n<body>\n%s\n</body>\n</html>\n'
                % (html.escape(url), root))
    props = '{"$preview":{"width":1440,"height":%d}}' % est_h
    return ('<!doctype html>\n<html lang="vi">\n<head>\n<meta charset="utf-8">\n<title>Thử font tiếng Việt</title>\n'
            '<script src="./support.js"></script>\n</head>\n<body>\n<x-dc>\n<helmet>\n'
            '<link rel="stylesheet" href="%s">\n<style>\nbody{margin:0}\n</style>\n</helmet>\n%s\n</x-dc>\n'
            "<script type=\"text/x-dc\" data-dc-script data-props='%s'>\n"
            "class Component extends DCLogic {\nrenderVals() {\nreturn {};\n}\n}\n</script>\n</body>\n</html>\n"
            % (html.escape(url), root, props)), est_h


def main():
    uilib.utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--font", action="append", required=True, help='"Tên font:400;700" (lặp lại cho nhiều font)')
    ap.add_argument("--sizes", default="40,24,17,14", help="cỡ chữ px, cách nhau bằng dấu phẩy")
    ap.add_argument("--line-heights", default="1.2,1.3,1.6,1.5", help="line-height tương ứng từng cỡ")
    ap.add_argument("--plain", action="store_true", help="HTML thường thay cho artboard .dc.html")
    ap.add_argument("--out", required=True)
    args = ap.parse_args()
    fonts = [parse_font(f) for f in args.font]
    sizes = [s.strip() for s in args.sizes.split(",") if s.strip()]
    lhs = [s.strip() for s in args.line_heights.split(",") if s.strip()]
    if len(lhs) < len(sizes):
        lhs += [lhs[-1] if lhs else "1.5"] * (len(sizes) - len(lhs))
    res = build(fonts, sizes, lhs, args.plain)
    if args.plain:
        uilib.write(args.out, res)
        print("Đã ghi %s (%d font)" % (args.out, len(fonts)))
    else:
        text, h = res
        uilib.write(args.out, text)
        print("Đã ghi %s (%d font). Mục boards trong canvas.json: w=1440, h=%d (trang co giãn)." % (args.out, len(fonts), h))


if __name__ == "__main__":
    main()
