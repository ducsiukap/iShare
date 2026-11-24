#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_inventory.py - kiểm danh mục màn hình (screen-inventory.md) với FR/US/SC và với các artboard đã vẽ.

  python3 check_inventory.py --inventory output/screen-inventory.md --specs docs/specs
  python3 check_inventory.py --inventory … --specs docs/specs --artboards canvas/giao-dien/project --batch A
  python3 check_inventory.py --inventory … --specs docs/specs --artboards canvas/giao-dien/project --require-artboards

Kiểm:
- bảng <!-- ui:screens -->: mã SCR-Mxx-nn / SCR-SHARED-nn đúng dạng, không trùng, khớp cột module; cột bắt buộc không
  trống; UC/SC/FR/BR được dẫn có tồn tại; slug trạng thái thuộc từ vựng (CONVENTIONS.md mục 4); thiết bị hợp lệ; đợt
  có trong bảng <!-- ui:batches -->;
- truy vết ngược: mọi UC con (tier = sub) có màn hình hoặc nằm trong <!-- ui:no-screen -->; SC chưa được nhắc tới;
- nguồn đổi: so bảng <!-- ui:sources --> (path | version) với phiên bản hiện tại (FR: phien_ban; US/SC: date);
- artboard (khi có --artboards): mỗi màn hình × trạng thái × thiết bị có tệp <id>--<state>--<device>.dc.html;
  artboard SCR-* không khớp danh mục.
Mã thoát: 0 nếu không có ERROR, 1 nếu có ERROR, 2 nếu lỗi tham số/tệp.
"""
import argparse
import collections
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import uilib  # noqa: E402

HERE = os.path.dirname(os.path.abspath(__file__))
CONVENTIONS = os.path.join(HERE, "..", "input", "CONVENTIONS.md")
ID_RE = re.compile(r"^SCR-(M\d{2}|SHARED)-\d{2}$")
UC_RE = re.compile(r"\bUC-M\d{2}-\d{3}\b")
SC_RE = re.compile(r"\bSC-M\d{2}-\d{3}\b")
REQ_RE = re.compile(r"\b(?:FR|BR)-M\d{2}-\d{2}(?:\.\d{2})?\b")
DEVICES = {"desktop", "mobile"}
REQUIRED = ("name", "module", "roles", "states", "devices", "batch")


def state_vocab():
    text = uilib.read(CONVENTIONS)
    m = re.search(r"^## 4\..*?$(.*?)^## ", text, re.S | re.M)
    vocab = set()
    if m:
        for line in m.group(1).splitlines():
            if line.startswith("|") and "`" in line:
                first = uilib.split_row(line)[0]
                vocab.update(re.findall(r"`([a-z0-9-]+)`", first))
    return vocab


def load_specs(specs):
    ucs, scs, reqs, versions = {}, {}, set(), {}
    for p in sorted(glob.glob(os.path.join(specs, "us", "US-M*.md"))):
        text = uilib.read(p)
        for _, header, rows, _ in uilib.tables_after_marker_prefix(text, "uc:catalog"):
            for r in rows:
                uid = (r.get("id") or "").strip()
                if UC_RE.fullmatch(uid):
                    ucs[uid] = {"tier": (r.get("tier") or "").strip().lower(), "name": r.get("name", ""),
                                "level": r.get("level", ""), "file": p}
        _, rows, _ = uilib.table_after_marker(text, "uc:document")
        kv = {(r.get("key") or "").strip(): (r.get("value") or "").strip() for r in rows}
        versions[os.path.normpath(p).replace("\\", "/")] = kv.get("date", "")
    for p in sorted(glob.glob(os.path.join(specs, "scenarios", "M*", "SC-M*.md"))):
        text = uilib.read(p)
        for m in re.finditer(r"<!--\s*sc:scenario\s+(SC-M\d{2}-\d{3})\s*-->", text):
            scs[m.group(1)] = p
        _, rows, _ = uilib.table_after_marker(text, "sc:document")
        kv = {(r.get("key") or "").strip(): (r.get("value") or "").strip() for r in rows}
        versions[os.path.normpath(p).replace("\\", "/")] = kv.get("date", "")
    for p in sorted(glob.glob(os.path.join(specs, "fr", "FR-M*.md"))):
        text = uilib.read(p)
        reqs.update(REQ_RE.findall(text))
        versions[os.path.normpath(p).replace("\\", "/")] = uilib.frontmatter(text).get("phien_ban", "")
    return ucs, scs, reqs, versions


def module_of(ident):
    m = re.search(r"M(\d{2})", ident)
    return "M" + m.group(1) if m else None


def main():
    uilib.utf8_stdout()
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--inventory", required=True)
    ap.add_argument("--specs", default="docs/specs", help="thư mục chứa fr/, us/, scenarios/")
    ap.add_argument("--artboards", action="append", default=[], help="thư mục artboard (lặp lại được)")
    ap.add_argument("--require-artboards", action="store_true", help="thiếu artboard là ERROR")
    ap.add_argument("--batch", help="chỉ kiểm artboard của một đợt (A–E)")
    ap.add_argument("--modules", help="giới hạn truy vết ngược cho các module, ví dụ M01,M03")
    args = ap.parse_args()

    if not os.path.isfile(args.inventory):
        print("Không thấy %s" % args.inventory, file=sys.stderr)
        sys.exit(2)
    if not os.path.isdir(args.specs):
        print("Không thấy thư mục specs %s" % args.specs, file=sys.stderr)
        sys.exit(2)

    errors, warns, infos = [], [], []
    inv = uilib.read(args.inventory)
    header, screens, lines = uilib.table_after_marker(inv, "ui:screens")
    if not header:
        print("ERROR: không thấy bảng <!-- ui:screens --> trong %s" % args.inventory)
        sys.exit(1)
    missing_cols = [c for c in ("id",) + REQUIRED + ("uc", "sc", "sources") if c not in header]
    if missing_cols:
        errors.append("Bảng ui:screens thiếu cột: %s" % ", ".join(missing_cols))
    _, noscreen, _ = uilib.table_after_marker(inv, "ui:no-screen")
    _, batches, _ = uilib.table_after_marker(inv, "ui:batches")
    _, sources, _ = uilib.table_after_marker(inv, "ui:sources")
    batch_ids = {(b.get("batch") or "").strip() for b in batches if (b.get("batch") or "").strip()} or set("ABCDE")

    vocab = state_vocab()
    ucs, scs, reqs, versions = load_specs(args.specs)
    scope = set(x.strip() for x in args.modules.split(",")) if args.modules else None

    seen = {}
    uc_used, sc_used = set(), set()
    per_module = collections.Counter()
    per_batch = collections.Counter()
    expected = {}  # artboard key -> (screen id, batch)
    for row, ln in zip(screens, lines):
        sid = (row.get("id") or "").strip().strip("`")
        where = "L%d %s" % (ln, sid or "(không mã)")
        if not ID_RE.match(sid):
            errors.append("%s: mã không đúng dạng SCR-Mxx-nn / SCR-SHARED-nn" % where)
        if sid in seen:
            errors.append("%s: trùng mã với dòng L%d" % (where, seen[sid]))
        seen[sid] = ln
        mod = (row.get("module") or "").strip()
        m = ID_RE.match(sid)
        if m and mod and mod != m.group(1):
            errors.append("%s: cột module '%s' không khớp mã" % (where, mod))
        for col in REQUIRED:
            if (row.get(col) or "").strip() in uilib.EMPTY:
                errors.append("%s: cột '%s' trống" % (where, col))
        for u in UC_RE.findall(row.get("uc") or ""):
            uc_used.add(u)
            if u not in ucs:
                errors.append("%s: %s không có trong uc:catalog của US" % (where, u))
        for s in SC_RE.findall(row.get("sc") or ""):
            sc_used.add(s)
            if s not in scs:
                errors.append("%s: %s không có trong SC" % (where, s))
        for r in uilib.split_list(row.get("sources")):
            if REQ_RE.fullmatch(r):
                if r not in reqs:
                    errors.append("%s: %s không có trong FR" % (where, r))
            elif not re.match(r"^(DEC|QA|ISS|OPEN|DD-UI)-", r):
                warns.append("%s: nguồn '%s' không phải mã FR/BR/DEC" % (where, r))
        states = uilib.split_list(row.get("states"))
        for st in states:
            if st not in vocab:
                errors.append("%s: trạng thái '%s' không thuộc từ vựng (CONVENTIONS.md mục 4)" % (where, st))
        if states and "default" not in states:
            warns.append("%s: không có trạng thái 'default'" % where)
        devices = [d.lower() for d in uilib.split_list(row.get("devices"))]
        for d in devices:
            if d not in DEVICES:
                errors.append("%s: thiết bị '%s' không hợp lệ (desktop, mobile)" % (where, d))
        if "desktop" not in devices and devices:
            warns.append("%s: không có bản desktop (CONVENTIONS mục 3: desktop bắt buộc)" % where)
        batch = (row.get("batch") or "").strip()
        if batch and batch not in batch_ids:
            errors.append("%s: đợt '%s' không có trong bảng ui:batches" % (where, batch))
        if mod != "SHARED" and not UC_RE.search(row.get("uc") or "") and not SC_RE.search(row.get("sc") or ""):
            warns.append("%s: không dẫn UC hay SC nào" % where)
        per_module[mod] += 1
        per_batch[batch] += 1
        for st in states:
            for d in devices:
                expected["%s--%s--%s" % (sid, st, d)] = (sid, batch)

    no_uc = set()
    for r in noscreen:
        for u in UC_RE.findall(r.get("uc") or ""):
            no_uc.add(u)
            if u not in ucs:
                errors.append("ui:no-screen: %s không có trong uc:catalog" % u)
            if (r.get("reason") or "").strip() in uilib.EMPTY:
                errors.append("ui:no-screen: %s thiếu lý do" % u)

    missing_uc = sorted(u for u, info in ucs.items()
                        if info["tier"] == "sub" and u not in uc_used and u not in no_uc
                        and (scope is None or module_of(u) in scope))
    for u in missing_uc:
        errors.append("UC con chưa có màn hình và không nằm trong ui:no-screen: %s %s" % (u, ucs[u]["name"]))
    unused_sc = sorted(s for s in scs if s not in sc_used and (scope is None or module_of(s) in scope))
    if unused_sc:
        by_mod = collections.defaultdict(list)
        for s in unused_sc:
            by_mod[module_of(s)].append(s)
        for mod, lst in sorted(by_mod.items()):
            warns.append("SC chưa được màn hình nào nhắc tới (%s): %s" % (mod, ", ".join(lst)))

    # nguồn đổi
    for r in sources:
        path = (r.get("path") or "").strip().strip("`").replace("\\", "/")
        ver = (r.get("version") or "").strip()
        if not path:
            continue
        cur = versions.get(path)
        if cur is None:
            key = next((k for k in versions if k.endswith(path) or path.endswith(k)), None)
            cur = versions.get(key) if key else None
        if cur is None:
            warns.append("ui:sources: không tìm thấy %s" % path)
        elif cur != ver:
            mod = module_of(os.path.basename(path))
            hit = [s.get("id") for s in screens
                   if mod and (mod in (s.get("module") or "") or mod in (s.get("uc") or "") + (s.get("sc") or "") +
                               (s.get("sources") or ""))]
            warns.append("Nguồn đã đổi: %s (%s → %s); màn hình liên quan: %s" % (
                path, ver, cur, ", ".join(hit) if hit else "không có"))

    # artboard
    found_total = None
    if args.artboards:
        files = set()
        for d in args.artboards:
            for dp, _, fn in os.walk(d):
                for n in fn:
                    mm = re.match(r"^(.*?)\.(?:dc\.html|html)$", n)
                    if mm:
                        files.add(mm.group(1))
        exp = {k: v for k, v in expected.items() if not args.batch or v[1] == args.batch}
        miss = sorted(k for k in exp if k not in files)
        found_total = len(exp) - len(miss)
        for k in miss:
            (errors if args.require_artboards else infos).append("Thiếu artboard: %s.dc.html" % k)
        for f in sorted(files):
            if f.startswith("SCR-") and f not in expected:
                warns.append("Artboard không khớp danh mục (sai tên hoặc màn hình/trạng thái chưa khai báo): %s" % f)

    # in
    print("check_inventory — %s" % args.inventory)
    print("Màn hình: %d · UC trong US: %d (con: %d) · SC: %d" % (
        len(screens), len(ucs), sum(1 for v in ucs.values() if v["tier"] == "sub"), len(scs)))
    if per_module:
        print("Theo module: " + ", ".join("%s=%d" % (k or "?", v) for k, v in sorted(per_module.items())))
    if per_batch:
        art = collections.Counter(v[1] for v in expected.values())
        print("Theo đợt: " + ", ".join("%s=%d màn hình/%d artboard" % (k or "?", per_batch[k], art[k])
                                        for k in sorted(per_batch)))
    if found_total is not None:
        total = len([1 for v in expected.values() if not args.batch or v[1] == args.batch])
        print("Artboard%s: có %d/%d" % (" đợt " + args.batch if args.batch else "", found_total, total))
    for lv, lst in (("ERROR", errors), ("WARN", warns), ("INFO", infos)):
        for msg in lst:
            print("  %-5s %s" % (lv, msg))
    print("\nTổng: ERROR=%d WARN=%d INFO=%d" % (len(errors), len(warns), len(infos)))
    sys.exit(1 if errors else 0)


if __name__ == "__main__":
    main()
