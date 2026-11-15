#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_db.py - kiểm cơ học tài liệu thiết kế cơ sở dữ liệu (DB-Mxx.md, DB-SYS.md).

Ví dụ:
  python3 check_db.py --db DB-M05.md --step 4 --cd CD-M05.md
  python3 check_db.py --db DB-M05.md --final --cd CD-M05.md
  python3 check_db.py --db DB-SYS.md --system --final --cd CD-SYS.md

Tool bắt lỗi cơ học: lớp chưa có bảng, thuộc tính chưa thành cột, quan hệ 1-n thiếu khóa ngoại, khóa ngoại
lệch kiểu, thuộc tính dẫn xuất chưa xử lý, bảng chỉ còn một khóa ngoại, lược đồ cuối lệch với các bảng bước.
Trả mã thoát 1 khi có ERROR.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdtab  # noqa: E402

COLS = {
    "1": ["Bảng", "Từ lớp", "Nhóm", "Sở hữu", "Ghi chú"],
    "2.1": ["Bảng", "Cột", "Kiểu", "Null", "Duy nhất", "Từ thuộc tính", "Ghi chú"],
    "2.2": ["Lớp", "Thuộc tính", "Kiểu", "Lý do không chuyển"],
    "3": ["ID", "Bảng A", "Bảng B", "Dạng", "Xử lý", "Ghi chú"],
    "4.1": ["Bảng", "Khóa chính", "Ghi chú"],
    "4.2": ["Bảng", "Cột", "Kiểu", "Null", "Duy nhất", "Tham chiếu", "Từ quan hệ", "Ghi chú"],
    "5.1": ["Bảng", "Cột", "Loại dư thừa", "Căn cứ", "Cách có lại giá trị"],
    "5.2": ["Bảng", "Lý do"],
    "5.3": ["Bảng", "Cột", "Lý do giữ", "Nguồn"],
    "6.1": ["Bảng", "Cột", "Kiểu", "Khóa", "Null", "Duy nhất", "Tham chiếu"],
    "7.1": ["Bảng ngoài", "Module sở hữu", "Dùng thế nào"],
    "7.2": ["Bảng của module khác", "Cột", "Kiểu", "Tham chiếu", "Từ quan hệ"],
    "9": ["Mã", "Loại", "Câu hỏi", "Trả lời", "Ghi vào"],
}
HANDLING = {"Tách riêng", "Gộp", "Cha–con"}
REF_RE = re.compile(r"^([A-Za-z_][A-Za-z0-9_]*)\(([A-Za-z_][A-Za-z0-9_]*)\)$")
NO_PK = "Không có"


def to_snake(name):
    """PascalCase/camelCase -> snake_case: BookedRoom -> booked_room, isCheckedIn -> is_checked_in."""
    return re.sub(r"(?<=[a-z0-9])(?=[A-Z])|(?<=[A-Z])(?=[A-Z][a-z])", "_", name).lower()


def plural(snake):
    """Số nhiều tiếng Anh của từ cuối: post_topic -> post_topics, category -> categories."""
    head, _, last = snake.rpartition("_")
    if re.search(r"[^aeiou]y$", last):
        last = last[:-1] + "ies"
    elif re.search(r"(s|x|z|ch|sh)$", last):
        last += "es"
    else:
        last += "s"
    return (head + "_" if head else "") + last


def table_names(cls, style):
    """Tên bảng hợp quy ước QU-06 cho một lớp. snake: snake_case, số nhiều (đã chốt 2026-11-15)."""
    if style == "tbl":
        return ["tbl" + cls]
    if style == "snake":
        return [plural(to_snake(cls))]
    return []


def column_name(attr, style):
    """Tên cột hợp quy ước QU-07 cho một thuộc tính."""
    if style == "snake":
        return to_snake(attr)
    if style == "tbl":
        return attr
    return None


def load_db(path):
    text = mdtab.read(path)
    d = {"path": path, "text": text, "fm": mdtab.frontmatter(text), "head": {}, "rows": {}}
    for num in COLS:
        h, r = mdtab.table(text, num)
        d["head"][num], d["rows"][num] = h, r
    d["module"] = d["fm"].get("module", "")
    return d


def load_cd_min(path):
    text = mdtab.read(path)
    d = {"fm": mdtab.frontmatter(text), "rows": {}}
    for num in ("1", "2.1", "3.1", "3.2", "4"):
        _, d["rows"][num] = mdtab.table(text, num)
    d["module"] = d["fm"].get("module", "")
    return d


def pk_cols(cell):
    if mdtab.clean(cell) == NO_PK:
        return []
    return mdtab.split_list(cell)


def final_schema(d):
    """Lược đồ cuối tính từ mục 1, 2.1, 4.1, 4.2, 5.1, 5.2. Trả về list (bảng, [dict cột])."""
    removed_tables = set(r["Bảng"] for r in d["rows"]["5.2"])
    removed_cols = set((r["Bảng"], r["Cột"]) for r in d["rows"]["5.1"])
    pks = {r["Bảng"]: pk_cols(r["Khóa chính"]) for r in d["rows"]["4.1"]}
    out = []
    for t in d["rows"]["1"]:
        name = t["Bảng"]
        if name in removed_tables:
            continue
        cols, seen = [], set()
        for r in d["rows"]["2.1"]:
            if r["Bảng"] == name and (name, r["Cột"]) not in removed_cols:
                cols.append({"Cột": r["Cột"], "Kiểu": r["Kiểu"], "Null": r["Null"], "Duy nhất": r["Duy nhất"],
                             "Tham chiếu": "", "fk": False})
                seen.add(r["Cột"])
        for r in d["rows"]["4.2"]:
            if r["Bảng"] != name or (name, r["Cột"]) in removed_cols:
                continue
            if r["Cột"] in seen:
                for c in cols:
                    if c["Cột"] == r["Cột"]:
                        c["Tham chiếu"], c["fk"] = r["Tham chiếu"], True
            else:
                cols.append({"Cột": r["Cột"], "Kiểu": r["Kiểu"], "Null": r["Null"], "Duy nhất": r["Duy nhất"],
                             "Tham chiếu": r["Tham chiếu"], "fk": True})
                seen.add(r["Cột"])
        for c in cols:
            keys = []
            if c["Cột"] in pks.get(name, []):
                keys.append("PK")
            if c["fk"]:
                keys.append("FK")
            c["Khóa"] = ", ".join(keys)
        out.append((name, cols))
    return out


def check_step1(d, rep, cd, system, style):
    mod = d["module"]
    tables = {}
    if not rep.need_cols("1", d["head"]["1"], COLS["1"]):
        return tables
    for r in d["rows"]["1"]:
        t = r["Bảng"]
        if t in tables:
            rep.error("1", "bảng %s xuất hiện hai lần" % t)
        tables[t] = r
        want = table_names(r["Từ lớp"], style)
        if want and t not in want:
            rep.warn("1", "tên bảng %s không khớp quy ước QU-06 cho lớp %s (mong đợi: %s)"
                     % (t, r["Từ lớp"], " hoặc ".join(want)))
        if not system and r["Sở hữu"] != mod:
            rep.error("1", "bảng %s của %s: bảng của module khác không tạo ở đây, ghi ở mục 7.1" % (t, r["Sở hữu"]))
    if cd:
        by_class = set(r["Từ lớp"] for r in d["rows"]["1"])
        ext = set(r["Bảng ngoài"] for r in d["rows"]["7.1"])
        n_ext = 0
        for r in cd["rows"]["1"]:
            owned = system or r["Sở hữu"] == cd["module"]
            if owned and r["Lớp"] not in by_class:
                rep.error("1", "lớp %s của bản thiết kế lớp chưa có bảng (bước 1: mỗi lớp một bảng)" % r["Lớp"])
            if not owned:
                n_ext += 1
                want = table_names(r["Lớp"], style)
                if want and not any(w in ext for w in want):
                    rep.error("7.1", "lớp %s của %s chưa được ghi là bảng ngoài ở mục 7.1 (mong đợi: %s)"
                              % (r["Lớp"], r["Sở hữu"], " hoặc ".join(want)))
        if not system and not table_names("X", style) and len(ext) < n_ext:
            rep.error("7.1", "bản thiết kế lớp có %d lớp ngoài nhưng mục 7.1 chỉ có %d bảng ngoài" % (n_ext, len(ext)))
        cd_classes = set(r["Lớp"] for r in cd["rows"]["1"])
        for c in by_class:
            if c not in cd_classes:
                rep.error("1", "bảng tạo từ lớp %s không có ở bản thiết kế lớp" % c)
    return tables


def check_step2(d, rep, tables, cd, system, style):
    cols = {}
    if not rep.need_cols("2.1", d["head"]["2.1"], COLS["2.1"]):
        return cols
    class_of = {t: r["Từ lớp"] for t, r in tables.items()}
    for r in d["rows"]["2.1"]:
        t, c = r["Bảng"], r["Cột"]
        if t not in tables:
            rep.error("2.1", "cột %s thuộc bảng %s không có ở mục 1" % (c, t))
        if (t, c) in cols:
            rep.error("2.1", "%s.%s xuất hiện hai lần" % (t, c))
        cols[(t, c)] = r
        if mdtab.is_empty(r["Kiểu"]):
            rep.error("2.1", "%s.%s chưa có kiểu" % (t, c))
        if r["Null"] not in ("Có", "Không"):
            rep.error("2.1", "%s.%s: Null phải là Có hoặc Không" % (t, c))
        if r["Duy nhất"] not in ("Có", "Không"):
            rep.error("2.1", "%s.%s: Duy nhất phải là Có hoặc Không" % (t, c))
        src_attr = r["Từ thuộc tính"].split(".")[-1]
        want = column_name(src_attr, style) if src_attr else None
        if want and c != want:
            rep.warn("2.1", "cột %s.%s không khớp quy ước QU-07 cho thuộc tính %s (mong đợi: %s)" % (t, c, src_attr, want))
    if cd:
        table_of = {v: k for k, v in class_of.items()}
        src = set(r["Từ thuộc tính"] for r in d["rows"]["2.1"])
        cd_classes = set(r["Lớp"] for r in cd["rows"]["1"])
        owned = set(r["Lớp"] for r in cd["rows"]["1"] if system or r["Sở hữu"] == cd["module"])
        for r in cd["rows"]["2.1"]:
            key = "%s.%s" % (r["Lớp"], r["Thuộc tính"])
            if r["Lớp"] in owned and key not in src:
                rep.error("2.1", "thuộc tính %s chưa được chuyển thành cột (bước 2)" % key)
        for r in d["rows"]["2.1"]:
            if r["Kiểu"].rstrip("[]") in cd_classes:
                rep.error("2.1", "%s.%s có kiểu là lớp %s: thuộc tính đối tượng không chuyển thành cột"
                          % (r["Bảng"], r["Cột"], r["Kiểu"]))
        dropped = set("%s.%s" % (r["Lớp"], r["Thuộc tính"]) for r in d["rows"]["2.2"])
        if d["head"]["2.2"] is None:
            rep.error("2.2", "không tìm thấy bảng thuộc tính đối tượng không chuyển")
        for r in cd["rows"]["4"]:
            key = "%s.%s" % (r["Lớp chứa"], r["Thuộc tính"])
            if r["Lớp chứa"] in owned and key not in dropped:
                rep.error("2.2", "thuộc tính đối tượng %s chưa được ghi ở mục 2.2" % key)
            if key in src:
                rep.error("2.1", "thuộc tính đối tượng %s không được chuyển thành cột" % key)
        _ = table_of
    return cols


def check_step3(d, rep, tables, cd):
    rels = {}
    if not rep.need_cols("3", d["head"]["3"], COLS["3"]):
        return rels
    ext = set(r["Bảng ngoài"] for r in d["rows"]["7.1"])
    for r in d["rows"]["3"]:
        rid = r["ID"]
        if rid in rels:
            rep.error("3", "ID %s trùng" % rid)
        rels[rid] = r
        for t in (r["Bảng A"], r["Bảng B"]):
            if t not in tables and t not in ext:
                rep.error("3", "%s: bảng %s không có ở mục 1 và không phải bảng ngoài ở mục 7.1" % (rid, t))
        if r["Dạng"] == "n-n":
            rep.error("3", "%s: quan hệ n-n giữa %s và %s; quay lại bước phân tích để tách, không sửa ở đây"
                      % (rid, r["Bảng A"], r["Bảng B"]))
        elif r["Dạng"] not in ("1-1", "1-n", "n-1"):
            rep.error("3", "%s: Dạng '%s' không hợp lệ" % (rid, r["Dạng"]))
        if r["Xử lý"] not in HANDLING:
            rep.error("3", "%s: Xử lý phải là một trong: %s" % (rid, ", ".join(sorted(HANDLING))))
        if r["Dạng"] == "1-1" and mdtab.is_empty(r["Ghi chú"]):
            rep.error("3", "%s: quan hệ 1-1 phải ghi lý do gộp hay tách ở cột Ghi chú" % rid)
        if r["Xử lý"] == "Gộp" and r["Dạng"] != "1-1":
            rep.error("3", "%s: chỉ quan hệ 1-1 mới được gộp bảng" % rid)
    if cd:
        for r in cd["rows"]["3.1"]:
            if r["ID"] not in rels:
                rep.error("3", "quan hệ %s của bản thiết kế lớp chưa được chuyển thành quan hệ giữa các bảng" % r["ID"])
        for r in cd["rows"]["3.2"]:
            if r["Loại"] == "Kế thừa":
                if r["ID"] not in rels:
                    rep.error("3", "quan hệ kế thừa %s chưa có dòng Cha–con" % r["ID"])
                elif rels[r["ID"]]["Xử lý"] != "Cha–con":
                    rep.error("3", "%s là kế thừa: Xử lý phải là Cha–con" % r["ID"])
            elif r["ID"] in rels:
                rep.warn("3", "%s là quan hệ phụ thuộc: không sinh quan hệ giữa các bảng" % r["ID"])
    return rels


def check_step4(d, rep, tables, cols, rels, cd, style):
    ext = {r["Bảng ngoài"]: r for r in d["rows"]["7.1"]}
    pks = {}
    if rep.need_cols("4.1", d["head"]["4.1"], COLS["4.1"]):
        for r in d["rows"]["4.1"]:
            if r["Bảng"] not in tables:
                rep.error("4.1", "bảng %s không có ở mục 1" % r["Bảng"])
            pks[r["Bảng"]] = pk_cols(r["Khóa chính"])
        for t in tables:
            if t not in pks:
                rep.error("4.1", "bảng %s chưa có dòng khóa chính" % t)
    fks = {}
    if not rep.need_cols("4.2", d["head"]["4.2"], COLS["4.2"]):
        return pks, fks
    all_cols = dict(cols)
    for r in d["rows"]["4.2"]:
        t, c = r["Bảng"], r["Cột"]
        if t not in tables:
            if t in ext:
                rep.error("4.2", "khóa ngoại %s.%s nằm ở bảng của module khác: ghi ở mục 7.2, không ghi ở 4.2" % (t, c))
            else:
                rep.error("4.2", "bảng %s không có ở mục 1" % t)
            continue
        if (t, c) in fks:
            rep.error("4.2", "%s.%s xuất hiện hai lần" % (t, c))
        fks[(t, c)] = r
        all_cols.setdefault((t, c), r)
        if style == "snake" and not c.endswith("_id"):
            rep.warn("4.2", "khóa ngoại %s.%s không khớp quy ước QU-08 (snake_case, kết thúc bằng _id)" % (t, c))
        if style == "tbl" and not re.search(r"Id$", c):
            rep.warn("4.2", "khóa ngoại %s.%s không khớp quy ước QU-08 (kết thúc bằng Id)" % (t, c))
        m = REF_RE.match(r["Tham chiếu"])
        if not m:
            rep.error("4.2", "%s.%s: Tham chiếu viết dạng tên_bảng(cột), ví dụ posts(id)" % (t, c))
            continue
        rt, rc = m.group(1), m.group(2)
        if rt in tables:
            if rc not in pks.get(rt, []):
                rep.error("4.2", "%s.%s tham chiếu %s(%s) nhưng %s không phải khóa chính của %s" % (t, c, rt, rc, rc, rt))
            ref = cols.get((rt, rc)) or fks.get((rt, rc))
            if ref and ref["Kiểu"] != r["Kiểu"]:
                rep.error("4.2", "%s.%s kiểu %s khác kiểu %s của %s(%s)" % (t, c, r["Kiểu"], ref["Kiểu"], rt, rc))
        elif rt not in ext:
            rep.error("4.2", "%s.%s tham chiếu bảng %s không có ở mục 1 và không ghi ở mục 7.1" % (t, c, rt))
        if r["Từ quan hệ"] not in rels:
            rep.error("4.2", "%s.%s: quan hệ '%s' không có ở mục 3" % (t, c, r["Từ quan hệ"]))
        if r["Null"] not in ("Có", "Không") or r["Duy nhất"] not in ("Có", "Không"):
            rep.error("4.2", "%s.%s: Null và Duy nhất phải là Có hoặc Không" % (t, c))
    for t, pk in pks.items():
        for c in pk:
            if (t, c) not in all_cols:
                rep.error("4.1", "khóa chính %s.%s không phải là cột của bảng" % (t, c))
    proposed = set((r["Bảng của module khác"], r["Từ quan hệ"]) for r in d["rows"]["7.2"])
    by_rel = {}
    for (t, c), r in fks.items():
        by_rel.setdefault(r["Từ quan hệ"], []).append((t, c, r))
    for rid, r in rels.items():
        a, b, form, how = r["Bảng A"], r["Bảng B"], r["Dạng"], r["Xử lý"]
        if how == "Gộp" or form not in ("1-1", "1-n", "n-1"):
            continue
        got = by_rel.get(rid, [])
        if how == "Cha–con":
            ok = [x for x in got if x[0] == b and x[2]["Tham chiếu"].startswith(a + "(")]
            if not ok:
                rep.error("4.2", "%s (cha–con): bảng con %s phải có khóa ngoại tham chiếu khóa chính của bảng cha %s" % (rid, b, a))
            elif pks.get(b) != [ok[0][1]]:
                rep.error("4.1", "%s (cha–con): khóa chính của bảng con %s phải chính là khóa ngoại %s" % (rid, b, ok[0][1]))
            continue
        if form == "1-n":
            many, one = b, a
        elif form == "n-1":
            many, one = a, b
        else:
            many, one = None, None
        if form == "1-1":
            ok = [x for x in got if (x[0] == a and x[2]["Tham chiếu"].startswith(b + "(")) or
                  (x[0] == b and x[2]["Tham chiếu"].startswith(a + "("))]
            if not ok and not ((a, rid) in proposed or (b, rid) in proposed):
                rep.error("4.2", "%s (1-1, tách riêng): cần một khóa ngoại ở một trong hai bảng" % rid)
            for x in ok:
                if x[2]["Duy nhất"] != "Có":
                    rep.error("4.2", "%s (1-1): khóa ngoại %s.%s phải có Duy nhất = Có" % (rid, x[0], x[1]))
            continue
        if many in ext:
            if (many, rid) not in proposed:
                rep.error("7.2", "%s: bảng phía n là %s của module khác; ghi khóa ngoại đề nghị ở mục 7.2" % (rid, many))
            continue
        ok = [x for x in got if x[0] == many and x[2]["Tham chiếu"].startswith(one + "(")]
        if not ok:
            rep.error("4.2", "%s: 1 %s – n %s nên bảng %s phải có khóa ngoại tham chiếu %s" % (rid, one, many, many, one))
    if cd:
        cdrel = {r["ID"]: r for r in cd["rows"]["3.1"]}
        for (t, c), r in fks.items():
            x = cdrel.get(r["Từ quan hệ"])
            if not x:
                continue
            one_mult = x["Bội số toàn thể"] if x["Dạng"] == "n-1" else x["Bội số thành phần"]
            lo = mdtab.mult_lower(one_mult)
            want = "Có" if lo == 0 else "Không"
            if lo is not None and r["Null"] != want:
                rep.warn("4.2", "%s.%s: bội số phía 1 là '%s' nên Null nên là %s (đang là %s)" % (t, c, one_mult, want, r["Null"]))
    return pks, fks


def check_step5(d, rep, tables, cols, pks, fks, cd, system):
    all_cols = dict(cols)
    for k, r in fks.items():
        all_cols.setdefault(k, r)
    removed_tables = set()
    if d["head"]["5.2"] is not None and rep.need_cols("5.2", d["head"]["5.2"], COLS["5.2"]):
        for r in d["rows"]["5.2"]:
            if r["Bảng"] not in tables:
                rep.error("5.2", "bảng %s không có ở mục 1" % r["Bảng"])
            if mdtab.is_empty(r["Lý do"]):
                rep.error("5.2", "bảng %s bị loại phải ghi lý do" % r["Bảng"])
            removed_tables.add(r["Bảng"])
    removed = set()
    if rep.need_cols("5.1", d["head"]["5.1"], COLS["5.1"]):
        for r in d["rows"]["5.1"]:
            k = (r["Bảng"], r["Cột"])
            if k not in all_cols:
                rep.error("5.1", "%s.%s không phải cột đã có ở mục 2.1 hoặc 4.2" % k)
            if r["Loại dư thừa"] not in ("Trùng lặp", "Dẫn xuất"):
                rep.error("5.1", "%s.%s: Loại dư thừa phải là Trùng lặp hoặc Dẫn xuất" % k)
            if mdtab.is_empty(r["Căn cứ"]) or mdtab.is_empty(r["Cách có lại giá trị"]):
                rep.error("5.1", "%s.%s: phải ghi căn cứ và cách có lại giá trị sau khi loại" % k)
            if r["Cột"] in pks.get(r["Bảng"], []) or k in fks:
                rep.error("5.1", "%s.%s là cột khóa: bước 5 không loại cột khóa (khóa mất theo bảng khi cả bảng bị loại)" % k)
            removed.add(k)
    kept = set()
    if d["head"]["5.3"] is not None and rep.need_cols("5.3", d["head"]["5.3"], COLS["5.3"]):
        for r in d["rows"]["5.3"]:
            k = (r["Bảng"], r["Cột"])
            if k not in all_cols:
                rep.error("5.3", "%s.%s không phải cột của bảng" % k)
            if k in removed:
                rep.error("5.3", "%s.%s vừa bị loại ở 5.1 vừa được giữ ở 5.3" % k)
            if mdtab.is_empty(r["Lý do giữ"]) or mdtab.is_empty(r["Nguồn"]):
                rep.error("5.3", "%s.%s: giữ thuộc tính dẫn xuất phải có lý do và nguồn (yêu cầu nào đòi lưu)" % k)
            kept.add(k)
    if cd:
        col_by_attr = {r["Từ thuộc tính"]: (r["Bảng"], r["Cột"]) for r in d["rows"]["2.1"]}
        for r in cd["rows"]["2.1"]:
            if r["Tính chất"] != "Dẫn xuất":
                continue
            k = col_by_attr.get("%s.%s" % (r["Lớp"], r["Thuộc tính"]))
            if k and k not in removed and k not in kept and k[0] not in removed_tables:
                rep.error("5.1", "%s.%s đến từ thuộc tính dẫn xuất nhưng chưa được loại (5.1) hay ghi lý do giữ (5.3)" % k)
    for t in tables:
        if t in removed_tables:
            continue
        mine = [k for k in all_cols if k[0] == t and k not in removed]
        pk = pks.get(t, [])
        if not pk:
            rep.error("5", "bảng %s còn lại sau bước 5 nhưng không có khóa chính" % t)
        nonkey = [k for k in mine if k[1] not in pk and k not in fks]
        nfk = len([k for k in mine if k in fks])
        if not nonkey and nfk <= 1:
            rep.warn("5.2", "bảng %s không còn thuộc tính nào ngoài khóa và %d khóa ngoại: theo bước 5 có thể loại bảng này"
                     % (t, nfk))
    for (t, c), r in fks.items():
        if t in removed_tables:
            continue
        m = REF_RE.match(r["Tham chiếu"])
        if m and m.group(1) in removed_tables:
            rep.error("5.2", "%s.%s tham chiếu bảng %s đã bị loại" % (t, c, m.group(1)))
    return removed_tables


def check_schema(d, rep):
    if not rep.need_cols("6.1", d["head"]["6.1"], COLS["6.1"]):
        return
    want = set()
    for name, cols in final_schema(d):
        for c in cols:
            want.add((name, c["Cột"], c["Kiểu"], c["Khóa"], c["Null"], c["Duy nhất"], c["Tham chiếu"]))
    have = set()
    for r in d["rows"]["6.1"]:
        have.add((r["Bảng"], r["Cột"], r["Kiểu"], "" if mdtab.is_empty(r["Khóa"]) else r["Khóa"], r["Null"],
                  r["Duy nhất"], "" if mdtab.is_empty(r["Tham chiếu"]) else r["Tham chiếu"]))
    if want != have:
        for x in sorted(want - have):
            rep.error("6.1", "lược đồ cuối thiếu hoặc lệch dòng %s.%s (chạy lại build_schema.py --inplace)" % (x[0], x[1]))
        for x in sorted(have - want):
            rep.error("6.1", "lược đồ cuối thừa hoặc lệch dòng %s.%s (chạy lại build_schema.py --inplace)" % (x[0], x[1]))
    s6 = mdtab.section_with_children(d["text"], "6")
    if "@startuml" not in s6:
        rep.error("6.2", "chưa có mã PlantUML của sơ đồ quan hệ (chạy build_schema.py --inplace)")


def check_final(d, rep):
    if "(Chưa làm" in mdtab.strip_comments(d["text"]):
        rep.error("chốt", "còn mục ghi '(Chưa làm …)'")
    if d["head"]["9"] is not None and rep.need_cols("9", d["head"]["9"], COLS["9"]):
        for r in d["rows"]["9"]:
            if mdtab.is_empty(r["Trả lời"]):
                rep.error("9", "%s chưa có trả lời" % r["Mã"])
    for k in ("module", "ma_tai_lieu", "phien_ban", "trang_thai", "nguon"):
        if not d["fm"].get(k):
            rep.error("frontmatter", "thiếu trường %s" % k)


def main():
    mdtab.utf8_stdout()
    ap = argparse.ArgumentParser(description="Kiểm tài liệu thiết kế cơ sở dữ liệu")
    ap.add_argument("--db", required=True)
    ap.add_argument("--cd", help="bản thiết kế lớp tương ứng (CD-Mxx.md) để đối chiếu")
    ap.add_argument("--step", type=int, choices=[1, 2, 3, 4, 5])
    ap.add_argument("--final", action="store_true")
    ap.add_argument("--system", action="store_true")
    ap.add_argument("--table-style", default="snake", choices=["snake", "tbl", "none"],
                    help="quy ước tên bảng, cột, khóa ngoại (QU-06..08): snake = snake_case, tên bảng số nhiều "
                         "(mặc định); tbl = 'tbl' + tên lớp và cột camelCase như phương pháp gốc; none = không kiểm tên")
    a = ap.parse_args()
    d = load_db(a.db)
    rep = mdtab.Report("check_db %s" % os.path.basename(a.db))
    cd = load_cd_min(a.cd) if a.cd else None
    if cd:
        ver = cd["fm"].get("phien_ban", "")
        if ver and ver not in d["fm"].get("nguon", ""):
            rep.warn("frontmatter", "trường nguon ghi '%s' nhưng bản thiết kế lớp đang ở phiên bản %s"
                     % (d["fm"].get("nguon", ""), ver))
        if cd["fm"].get("trang_thai") and cd["fm"]["trang_thai"] != "Đã chốt":
            rep.error("đầu vào", "bản thiết kế lớp chưa ở trạng thái Đã chốt")
    upto = 5 if (a.final or a.step is None) else a.step
    tables = check_step1(d, rep, cd, a.system, a.table_style)
    cols, rels, pks, fks = {}, {}, {}, {}
    if upto >= 2:
        cols = check_step2(d, rep, tables, cd, a.system, a.table_style)
    if upto >= 3:
        rels = check_step3(d, rep, tables, cd)
    if upto >= 4:
        pks, fks = check_step4(d, rep, tables, cols, rels, cd, a.table_style)
    if upto >= 5:
        check_step5(d, rep, tables, cols, pks, fks, cd, a.system)
        check_schema(d, rep)
    if a.final:
        check_final(d, rep)
    sys.exit(rep.finish())


if __name__ == "__main__":
    main()
