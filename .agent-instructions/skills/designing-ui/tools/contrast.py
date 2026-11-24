#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""contrast.py - kiểm độ tương phản WCAG 2.2 cho các cặp màu.

Hai cách dùng:
1. Kiểm nhanh một cặp:
     python3 contrast.py --fg "#1f2a37" --bg "#fbfaf7" [--min 4.5]
2. Kiểm mọi cặp của tokens ở mọi theme:
     python3 contrast.py --tokens output/tokens/tokens.json --pairs output/tokens/contrast-pairs.csv

contrast-pairs.csv có cột: fg,bg,min,note. fg/bg là tên token màu (hoặc mã màu trực tiếp). min là 4.5 (chữ thường),
3 (chữ lớn ≥ 24px hoặc ≥ 18.66px đậm, thành phần giao diện, vòng focus, icon mang nghĩa).
Màu có alpha được trộn lên nền trước khi tính.
Mã thoát: 0 nếu mọi cặp đạt, 1 nếu có cặp trượt, 2 nếu lỗi tham số/tệp.
"""
import argparse
import csv
import io
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uilib  # noqa: E402


def verdict(ratio, minimum):
    return "ĐẠT" if ratio + 1e-9 >= minimum else "TRƯỢT"


def main():
    uilib.utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--fg")
    ap.add_argument("--bg")
    ap.add_argument("--min", type=float, default=4.5)
    ap.add_argument("--tokens")
    ap.add_argument("--pairs")
    args = ap.parse_args()

    if args.fg and args.bg:
        fg, bg = uilib.parse_color(args.fg), uilib.parse_color(args.bg)
        if not fg or not bg:
            print("Không đọc được màu.", file=sys.stderr)
            sys.exit(2)
        r = uilib.contrast(fg, bg)
        print("%s trên %s: %.2f:1 — %s (ngưỡng %g)" % (args.fg, args.bg, r, verdict(r, args.min), args.min))
        print("  chữ thường 4.5: %s · chữ lớn / thành phần 3: %s" % (verdict(r, 4.5), verdict(r, 3)))
        sys.exit(0 if r + 1e-9 >= args.min else 1)

    if not (args.tokens and args.pairs):
        ap.print_help()
        sys.exit(2)
    tokens = uilib.Tokens(args.tokens)
    for e in tokens.errors:
        print("tokens.json: %s" % e)
    rows = list(csv.DictReader(io.StringIO(uilib.read(args.pairs))))
    fails, total, missing = 0, 0, 0
    print("contrast — %d cặp × %d theme (%s)" % (len(rows), len(tokens.themes), ", ".join(tokens.themes)))
    print("%-18s %-18s %-8s %-7s %-8s %-6s %s" % ("fg", "bg", "theme", "tỉ lệ", "ngưỡng", "", "ghi chú"))
    for row in rows:
        fgn, bgn = (row.get("fg") or "").strip(), (row.get("bg") or "").strip()
        try:
            minimum = float(row.get("min") or 4.5)
        except ValueError:
            minimum = 4.5
        for th in tokens.themes:
            def get(n):
                if n in tokens.colors:
                    return tokens.colors[n].get(th) or tokens.colors[n].get(tokens.themes[0])
                return uilib.parse_color(n)
            fg, bg = get(fgn), get(bgn)
            if not fg or not bg:
                missing += 1
                print("%-18s %-18s %-8s %-7s %-8s %-6s %s" % (fgn, bgn, th, "?", minimum, "THIẾU",
                                                              "không tìm thấy token/màu"))
                continue
            r = uilib.contrast(fg, bg)
            total += 1
            v = verdict(r, minimum)
            if v == "TRƯỢT":
                fails += 1
            print("%-18s %-18s %-8s %-7s %-8g %-6s %s" % (fgn, bgn, th, "%.2f" % r, minimum, v, row.get("note", "")))
    print("\nTổng: %d phép kiểm, %d trượt, %d thiếu token" % (total, fails, missing))
    sys.exit(1 if fails or missing else 0)


if __name__ == "__main__":
    main()
