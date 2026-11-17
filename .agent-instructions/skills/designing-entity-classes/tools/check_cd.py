#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_cd.py - kiểm cơ học tài liệu thiết kế lớp thực thể (CD-Mxx.md, CD-SYS.md).

Ví dụ:
  python3 check_cd.py --cd CD-M05.md --step 2 --ec EC-M05.md
  python3 check_cd.py --cd CD-M05.md --final --ec EC-M05.md
  python3 check_cd.py --cd CD-SYS.md --system --final --ec EC-SYS.md

Tool bắt lỗi cơ học: thiếu id, thiếu kiểu, kiểu lạ, còn quan hệ Liên kết chưa chuyển, thuộc tính đối tượng
sai quy tắc, lệch với bản phân tích. Trả mã thoát 1 khi có ERROR.
"""
import argparse
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdtab  # noqa: E402

BASE_TYPES = {"int", "long", "float", "double", "boolean", "String", "Date", "LocalDate", "LocalDateTime",
              "Instant", "BigDecimal", "Integer", "Long", "Float", "Double", "Boolean", "UUID", "byte[]"}
ID_STATES = {"Có", "Kế thừa", "Ngoài", "Không"}
ATTR_KINDS = {"Khóa", "Lưu", "Dẫn xuất"}
CLASS_GROUPS = {"Thực thể", "Liên kết", "Thống kê"}

COLS = {
    "1": ["Lớp", "Nhóm", "Sở hữu", "Lớp cha", "id", "Ghi chú"],
    "2.1": ["Lớp", "Thuộc tính", "Kiểu", "Bắt buộc", "Ràng buộc", "Tính chất", "Căn cứ kiểu"],
    "2.2": ["Kiểu", "Giá trị", "Dùng ở", "Nguồn"],
    "3.1": ["ID", "Thành phần", "Toàn thể", "Bội số thành phần", "Bội số toàn thể", "Dạng", "Loại",
            "Loại ở phân tích", "Căn cứ"],
    "3.2": ["ID", "Loại", "Lớp", "Lớp đích", "Ghi chú"],
    "4": ["Quan hệ", "Lớp chứa", "Thuộc tính", "Kiểu", "Quy tắc"],
    "6": ["Lớp", "Module sở hữu", "Module này dùng thế nào", "Đề nghị cho module sở hữu"],
    "7": ["Mã", "Quyết định", "Lý do"],
    "8": ["Mã", "Loại", "Câu hỏi", "Trả lời", "Ghi vào"],
}

EC_COLS = ["2.2", "2.3", "3.4"]


def load_cd(path):
    text = mdtab.read(path)
    d = {"path": path, "text": text, "fm": mdtab.frontmatter(text), "head": {}, "rows": {}}
    for num in COLS:
        h, r = mdtab.table(text, num)
        d["head"][num], d["rows"][num] = h, r
    d["module"] = d["fm"].get("module", "")
    return d


def load_ec_min(path):
    text = mdtab.read(path)
    d = {"fm": mdtab.frontmatter(text), "rows": {}}
    for num in EC_COLS:
        _, d["rows"][num] = mdtab.table(text, num)
    d["module"] = d["fm"].get("module", "")
    return d


def form_of(comp_mult, whole_mult):
    a, b = mdtab.mult_upper(comp_mult), mdtab.mult_upper(whole_mult)
    if a is None or b is None:
        return None
    return "%s-%s" % (a, b)


def expected_type(form, comp):
    return comp + "[]" if form == "n-1" else comp


def check_step1(d, rep, system):
    mod = d["module"]
    classes = {}
    if not rep.need_cols("1", d["head"]["1"], COLS["1"]):
        return classes
    for r in d["rows"]["1"]:
        c = r["Lớp"]
        if not mdtab.CLASS_RE.match(c):
            rep.error("1", "tên lớp '%s' phải là PascalCase tiếng Anh không dấu" % c)
        if c in classes:
            rep.error("1", "lớp %s xuất hiện hai lần" % c)
        classes[c] = r
        if r["Nhóm"] not in CLASS_GROUPS:
            rep.error("1", "%s: Nhóm '%s' không hợp lệ" % (c, r["Nhóm"]))
        if r["id"] not in ID_STATES:
            rep.error("1", "%s: cột id phải là Có, Kế thừa, Ngoài hoặc Không" % c)
    for c, r in classes.items():
        parent = "" if mdtab.is_empty(r["Lớp cha"]) else r["Lớp cha"]
        owned = system or r["Sở hữu"] == mod
        if parent and parent not in classes:
            rep.error("1", "%s: lớp cha %s không có trong bảng" % (c, parent))
        if not owned:
            if r["id"] != "Ngoài":
                rep.error("1", "%s do %s sở hữu: cột id phải ghi Ngoài (id được thêm ở tài liệu của %s)"
                          % (c, r["Sở hữu"], r["Sở hữu"]))
        elif parent:
            if r["id"] != "Kế thừa":
                rep.error("1", "%s kế thừa %s nên không thêm id riêng: cột id phải ghi Kế thừa" % (c, parent))
        elif r["Nhóm"] == "Thống kê":
            if r["id"] != "Không":
                rep.error("1", "%s là lớp thống kê không kế thừa lớp nào: không lưu nên không thêm id, "
                               "cột id phải ghi Không" % c)
        elif r["id"] != "Có":
            rep.error("1", "%s không kế thừa lớp nào nên phải có id: cột id phải ghi Có" % c)
    return classes


def check_step2(d, rep, classes, system):
    mod = d["module"]
    attrs, enums = {}, {}
    if d["head"]["2.2"] is not None and rep.need_cols("2.2", d["head"]["2.2"], COLS["2.2"]):
        for r in d["rows"]["2.2"]:
            e = r["Kiểu"]
            if not mdtab.CLASS_RE.match(e):
                rep.error("2.2", "tên kiểu liệt kê '%s' phải là PascalCase" % e)
            if e in classes:
                rep.error("2.2", "kiểu liệt kê %s trùng tên một lớp" % e)
            if mdtab.is_empty(r["Giá trị"]):
                rep.error("2.2", "%s chưa liệt kê giá trị" % e)
            if mdtab.is_empty(r["Nguồn"]):
                rep.error("2.2", "%s chưa ghi nguồn của các giá trị" % e)
            enums[e] = r
    if not rep.need_cols("2.1", d["head"]["2.1"], COLS["2.1"]):
        return attrs, enums
    used_enums = set()
    for r in d["rows"]["2.1"]:
        c, a, t = r["Lớp"], r["Thuộc tính"], r["Kiểu"]
        if c not in classes:
            rep.error("2.1", "thuộc tính %s thuộc lớp %s không có ở mục 1" % (a, c))
        if not mdtab.ATTR_RE.match(a):
            rep.error("2.1", "%s.%s: tên thuộc tính phải là camelCase tiếng Anh không dấu" % (c, a))
        if (c, a) in attrs:
            rep.error("2.1", "%s.%s xuất hiện hai lần" % (c, a))
        attrs[(c, a)] = r
        if mdtab.is_empty(t):
            rep.error("2.1", "%s.%s chưa có kiểu" % (c, a))
        elif t in classes or t.rstrip("[]") in classes:
            rep.error("2.1", "%s.%s có kiểu là lớp %s: thuộc tính đối tượng chỉ được thêm ở bước 4 (mục 4), "
                             "không ghi ở mục 2.1" % (c, a, t))
        elif t in enums:
            used_enums.add(t)
        elif t not in BASE_TYPES:
            rep.warn("2.1", "%s.%s: kiểu '%s' không thuộc danh sách kiểu cơ bản và chưa khai ở mục 2.2" % (c, a, t))
        if r["Bắt buộc"] not in ("Có", "Không"):
            rep.error("2.1", "%s.%s: Bắt buộc phải là Có hoặc Không" % (c, a))
        if r["Tính chất"] not in ATTR_KINDS:
            rep.error("2.1", "%s.%s: Tính chất '%s' không hợp lệ (Khóa, Lưu, Dẫn xuất)" % (c, a, r["Tính chất"]))
        if mdtab.is_empty(r["Căn cứ kiểu"]):
            rep.error("2.1", "%s.%s chưa ghi căn cứ chọn kiểu" % (c, a))
        if (a == "id") != (r["Tính chất"] == "Khóa"):
            rep.error("2.1", "%s.%s: chỉ thuộc tính id mang Tính chất = Khóa" % (c, a))
    for e in enums:
        if e not in used_enums:
            rep.warn("2.2", "kiểu liệt kê %s không được thuộc tính nào dùng" % e)
    for c, r in classes.items():
        has_id = (c, "id") in attrs
        if r["id"] == "Có" and not has_id:
            rep.error("2.1", "lớp %s phải có thuộc tính id (bước 1)" % c)
        if r["id"] in ("Kế thừa", "Ngoài", "Không") and has_id:
            rep.error("2.1", "lớp %s không được có id riêng (cột id ở mục 1 ghi %s)" % (c, r["id"]))
    return attrs, enums


def check_step3(d, rep, classes):
    rels = {}
    if rep.need_cols("3.1", d["head"]["3.1"], COLS["3.1"]):
        for r in d["rows"]["3.1"]:
            rid, comp, whole = r["ID"], r["Thành phần"], r["Toàn thể"]
            if rid in rels:
                rep.error("3.1", "ID %s trùng" % rid)
            rels[rid] = r
            for c in (comp, whole):
                if c not in classes:
                    rep.error("3.1", "%s: lớp %s không có ở mục 1" % (rid, c))
            if r["Loại"] not in ("Hợp thành", "Kết tập"):
                rep.error("3.1", "%s: sau bước 3 chỉ còn Hợp thành hoặc Kết tập (đang là '%s')" % (rid, r["Loại"]))
            form = form_of(r["Bội số thành phần"], r["Bội số toàn thể"])
            if form is None:
                rep.error("3.1", "%s: bội số sai cú pháp" % rid)
            else:
                if form == "n-n":
                    rep.error("3.1", "%s: quan hệ n-n; quay lại bước phân tích để tách" % rid)
                if r["Dạng"] != form:
                    rep.error("3.1", "%s: Dạng ghi '%s' nhưng bội số cho ra '%s' (thành phần–toàn thể)"
                              % (rid, r["Dạng"], form))
            if r["Loại"] == "Hợp thành" and mdtab.clean(r["Bội số toàn thể"]) != "1":
                rep.error("3.1", "%s: hợp thành thì mỗi thành phần thuộc đúng 1 toàn thể" % rid)
            if mdtab.is_empty(r["Căn cứ"]):
                rep.error("3.1", "%s chưa ghi căn cứ chọn bên toàn thể" % rid)
    if d["head"]["3.2"] is not None and rep.need_cols("3.2", d["head"]["3.2"], COLS["3.2"]):
        for r in d["rows"]["3.2"]:
            rid = r["ID"]
            if rid in rels:
                rep.error("3.2", "ID %s đã có ở mục 3.1" % rid)
            if r["Loại"] not in ("Kế thừa", "Phụ thuộc"):
                rep.error("3.2", "%s: mục 3.2 chỉ chứa Kế thừa và Phụ thuộc" % rid)
            for c in (r["Lớp"], r["Lớp đích"]):
                if c not in classes:
                    rep.error("3.2", "%s: lớp %s không có ở mục 1" % (rid, c))
            if r["Loại"] == "Kế thừa" and r["Lớp"] in classes:
                if classes[r["Lớp"]]["Lớp cha"] != r["Lớp đích"]:
                    rep.error("3.2", "%s: %s kế thừa %s nhưng mục 1 ghi lớp cha là '%s'"
                              % (rid, r["Lớp"], r["Lớp đích"], classes[r["Lớp"]]["Lớp cha"]))
    return rels


def check_step4(d, rep, classes, attrs, rels, system):
    mod = d["module"]
    if not rep.need_cols("4", d["head"]["4"], COLS["4"]):
        return
    seen, names, holds = {}, {}, set()
    proposals = set(r["Lớp"] for r in d["rows"]["6"] if not mdtab.is_empty(r.get("Đề nghị cho module sở hữu", "")))
    for r in d["rows"]["4"]:
        rid, holder, a, t = r["Quan hệ"], r["Lớp chứa"], r["Thuộc tính"], r["Kiểu"]
        if rid not in rels:
            rep.error("4", "thuộc tính %s.%s gắn với quan hệ %s không có ở mục 3.1" % (holder, a, rid))
            continue
        if rid in seen:
            rep.error("4", "quan hệ %s có hơn một thuộc tính đối tượng (mỗi quan hệ chỉ đi một chiều)" % rid)
        seen[rid] = r
        rel = rels[rid]
        if holder != rel["Toàn thể"]:
            rep.error("4", "%s: thuộc tính đối tượng phải nằm ở lớp toàn thể %s, không phải %s"
                      % (rid, rel["Toàn thể"], holder))
        exp = expected_type(rel["Dạng"], rel["Thành phần"])
        if t != exp:
            rep.error("4", "%s: dạng %s (thành phần–toàn thể) thì kiểu phải là %s, đang là %s"
                      % (rid, rel["Dạng"], exp, t))
        if not mdtab.ATTR_RE.match(a):
            rep.error("4", "%s.%s: tên thuộc tính phải là camelCase" % (holder, a))
        if (holder, a) in attrs or (holder, a) in names:
            rep.error("4", "%s.%s trùng tên một thuộc tính khác của lớp" % (holder, a))
        names[(holder, a)] = rid
        holds.add((holder, rel["Thành phần"]))
        if holder in classes and not system and classes[holder]["Sở hữu"] != mod and holder not in proposals:
            rep.error("4", "%s.%s nằm ở lớp của %s: phải ghi thành đề nghị ở mục 6 Liên module"
                      % (holder, a, classes[holder]["Sở hữu"]))
    for rid in rels:
        if rid not in seen:
            rep.error("4", "quan hệ %s chưa có thuộc tính đối tượng" % rid)
    for (h, c) in holds:
        if h != c and (c, h) in holds:
            rep.warn("4", "%s và %s chứa lẫn nhau (tham chiếu vòng); xem lại bên toàn thể" % (h, c))
    from gen_puml import build
    s5 = mdtab.section_with_children(d["text"], "5")
    mdtab.check_diagram(rep, "5", d["path"], mdtab.doc_id_of(d["fm"], d["path"]), s5, build(d))


def check_against_ec(d, rep, ec, classes, attrs, rels, upto, system):
    ec_ver = ec["fm"].get("phien_ban", "")
    if ec_ver and ec_ver not in d["fm"].get("nguon", ""):
        rep.warn("frontmatter", "trường nguon ghi '%s' nhưng bản phân tích đang ở phiên bản %s"
                 % (d["fm"].get("nguon", ""), ec_ver))
    if ec["fm"].get("trang_thai") and ec["fm"]["trang_thai"] != "Đã chốt":
        rep.error("đầu vào", "bản phân tích chưa ở trạng thái Đã chốt")
    ec_classes = {r["Lớp"]: r for r in ec["rows"]["2.2"]}
    for c, r in ec_classes.items():
        if c not in classes:
            rep.error("1", "lớp %s có ở bản phân tích nhưng thiếu ở đây" % c)
        else:
            if classes[c]["Nhóm"] != r["Nhóm"] or classes[c]["Sở hữu"] != r["Sở hữu"]:
                rep.error("1", "%s: Nhóm hoặc Sở hữu khác bản phân tích" % c)
    for c in classes:
        if c not in ec_classes:
            rep.error("1", "lớp %s không có ở bản phân tích; lớp mới phải được thêm ở bước phân tích" % c)
    if upto < 2:
        return
    # Thuộc tính của lớp ngoài (Căn cứ = Tham chiếu, hoặc lớp do module khác sở hữu) không chép sang CD của module:
    # module sở hữu lớp đó mới thiết kế chúng.
    own_classes = set(r["Lớp"] for r in ec["rows"]["2.2"] if system or r["Sở hữu"] == ec["module"])
    ec_attrs = {(r["Lớp"], r["Thuộc tính"]): r for r in ec["rows"]["2.3"]
                if r["Lớp"] in own_classes and r.get("Căn cứ") != "Tham chiếu"}
    for k, r in ec_attrs.items():
        if k not in attrs:
            rep.error("2.1", "%s.%s có ở bản phân tích nhưng thiếu ở đây" % k)
        elif attrs[k]["Tính chất"] != r["Tính chất"]:
            rep.error("2.1", "%s.%s: Tính chất khác bản phân tích (%s)" % (k[0], k[1], r["Tính chất"]))
    for k in attrs:
        if k[1] != "id" and k not in ec_attrs:
            rep.error("2.1", "%s.%s không có ở bản phân tích; thuộc tính mới phải được thêm ở bước phân tích" % k)
    if upto < 3:
        return
    kept = {r["ID"]: r for r in d["rows"]["3.2"]}
    for r in ec["rows"]["3.4"]:
        rid, kind = r["ID"], r["Loại"]
        if kind in ("Kế thừa", "Phụ thuộc"):
            if rid not in kept:
                rep.error("3.2", "quan hệ %s (%s) của bản phân tích thiếu ở mục 3.2" % (rid, kind))
            elif kept[rid]["Loại"] != kind:
                rep.error("3.2", "%s: loại khác bản phân tích (%s)" % (rid, kind))
        else:
            if rid not in rels:
                rep.error("3.1", "quan hệ %s (%s) của bản phân tích thiếu ở mục 3.1" % (rid, kind))
                continue
            x = rels[rid]
            if {x["Thành phần"], x["Toàn thể"]} != {r["Lớp A"], r["Lớp B"]}:
                rep.error("3.1", "%s: hai lớp khác bản phân tích (%s – %s)" % (rid, r["Lớp A"], r["Lớp B"]))
                continue
            if kind in ("Hợp thành", "Kết tập"):
                if x["Loại"] != kind:
                    rep.error("3.1", "%s: bản phân tích là %s, ở đây ghi %s" % (rid, kind, x["Loại"]))
                if x["Toàn thể"] != r["Bên chính"]:
                    rep.error("3.1", "%s: bên toàn thể khác bản phân tích (%s)" % (rid, r["Bên chính"]))
            comp_mult = r["Bội số A"] if x["Thành phần"] == r["Lớp A"] else r["Bội số B"]
            whole_mult = r["Bội số A"] if x["Toàn thể"] == r["Lớp A"] else r["Bội số B"]
            if r["Lớp A"] != r["Lớp B"] and (mdtab.clean(x["Bội số thành phần"]) != mdtab.clean(comp_mult)
                                            or mdtab.clean(x["Bội số toàn thể"]) != mdtab.clean(whole_mult)):
                rep.error("3.1", "%s: bội số khác bản phân tích" % rid)
    ec_ids = set(r["ID"] for r in ec["rows"]["3.4"])
    for rid in list(rels) + list(kept):
        if rid not in ec_ids:
            rep.error("3", "quan hệ %s không có ở bản phân tích" % rid)


def check_final(d, rep):
    if "(Chưa làm" in mdtab.strip_comments(d["text"]):
        rep.error("chốt", "còn mục ghi '(Chưa làm …)'")
    if d["head"]["8"] is not None and rep.need_cols("8", d["head"]["8"], COLS["8"]):
        for r in d["rows"]["8"]:
            if mdtab.is_empty(r["Trả lời"]):
                rep.error("8", "%s chưa có trả lời" % r["Mã"])
    for k in ("module", "ma_tai_lieu", "phien_ban", "trang_thai", "nguon"):
        if not d["fm"].get(k):
            rep.error("frontmatter", "thiếu trường %s" % k)


def main():
    mdtab.utf8_stdout()
    ap = argparse.ArgumentParser(description="Kiểm tài liệu thiết kế lớp thực thể")
    ap.add_argument("--cd", required=True)
    ap.add_argument("--ec", help="bản phân tích tương ứng (EC-Mxx.md) để đối chiếu")
    ap.add_argument("--step", type=int, choices=[1, 2, 3, 4])
    ap.add_argument("--final", action="store_true")
    ap.add_argument("--system", action="store_true")
    a = ap.parse_args()
    d = load_cd(a.cd)
    rep = mdtab.Report("check_cd %s" % os.path.basename(a.cd))
    upto = 4 if (a.final or a.step is None) else a.step
    classes = check_step1(d, rep, a.system)
    attrs, rels = {}, {}
    if upto >= 2:
        attrs, _ = check_step2(d, rep, classes, a.system)
    if upto >= 3:
        rels = check_step3(d, rep, classes)
    if upto >= 4:
        check_step4(d, rep, classes, attrs, rels, a.system)
    if a.ec:
        check_against_ec(d, rep, load_ec_min(a.ec), classes, attrs, rels, upto, a.system)
    if a.final:
        check_final(d, rep)
    sys.exit(rep.finish())


if __name__ == "__main__":
    main()
