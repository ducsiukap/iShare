#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""check_ec.py - kiểm cơ học tài liệu phân tích lớp thực thể (EC-Mxx.md, EC-SYS.md).

Ví dụ:
  python3 check_ec.py --ec EC-M05.md --step 2 --fr FR-M05.md
  python3 check_ec.py --ec EC-M05.md --final --fr FR-M05.md --others <thư mục ec>
  python3 check_ec.py --ec EC-SYS.md --system --final

Tool chỉ bắt lỗi cơ học (thiếu cột, tên sai dạng, còn n-n, lớp mồ côi, nguồn không tồn tại...).
Đúng sai về nghĩa (phân loại danh từ, loại quan hệ) do agent tự kiểm theo checklist của từng bước
và do người dùng duyệt ở cổng. Trả mã thoát 1 khi có ERROR.
"""
import argparse
import glob
import os
import re
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import mdtab  # noqa: E402

LEDGER_KINDS = {"Lớp", "Thuộc tính", "Loại bỏ"}
CLASS_GROUPS = {"Thực thể", "Liên kết", "Thống kê"}
ATTR_KINDS = {"Lưu", "Dẫn xuất"}
ATTR_BASIS = {"Nguồn nêu", "Đề xuất", "Tham chiếu"}
REL_KINDS = {"Kế thừa", "Hợp thành", "Kết tập", "Liên kết", "Phụ thuộc"}
REL_WITH_MULT = {"Hợp thành", "Kết tập", "Liên kết"}
REL_WITH_MAIN = {"Kế thừa", "Hợp thành", "Kết tập", "Phụ thuộc"}

COLS = {
    "1.2": ["Câu", "Nội dung câu", "Nguồn"],
    "2.1": ["#", "Danh từ", "Xuất hiện ở", "Phân loại", "Kết quả", "Lý do"],
    "2.2": ["Lớp", "Tên tiếng Việt", "Nhóm", "Sở hữu", "Mô tả", "Thuộc tính", "Nguồn"],
    "2.3": ["Lớp", "Thuộc tính", "Tên tiếng Việt", "Tính chất", "Căn cứ", "Ràng buộc nguồn nêu", "Nguồn", "Ghi chú"],
    "2.4": ["Thực thể trong FR", "Trong mô hình", "Xử lý"],
    "3.2": ["Cặp", "Câu A → B", "Câu B → A", "Dạng", "Xử lý"],
    "3.3": ["Lớp liên kết", "Tách từ quan hệ n-n", "Thuộc tính riêng của liên kết", "Nguồn"],
    "3.4": ["ID", "Lớp A", "Bội số A", "Lớp B", "Bội số B", "Dạng", "Loại", "Bên chính", "Căn cứ", "Nguồn"],
    "5": ["Lớp", "Module sở hữu", "Module này dùng thế nào", "Thuộc tính module này bổ sung"],
    "6": ["Mã", "Loại", "Câu hỏi", "Trả lời", "Ghi vào"],
}


def load_ec(path):
    text = mdtab.read(path)
    d = {"path": path, "text": text, "fm": mdtab.frontmatter(text), "head": {}, "rows": {}}
    for num in COLS:
        h, r = mdtab.table(text, num)
        d["head"][num], d["rows"][num] = h, r
    d["module"] = d["fm"].get("module", "")
    return d


def derived_form(ma, mb):
    ua, ub = mdtab.mult_upper(ma), mdtab.mult_upper(mb)
    if ua is None or ub is None:
        return None
    return "%s-%s" % (ua, ub)


def norm_text(t):
    t = mdtab.strip_comments(t or "")
    t = re.sub(r"`|\*\*", "", t)
    return re.sub(r"\s+", " ", t).strip()


def sentence_count(d):
    return len(d["rows"]["1.2"]) if d["head"]["1.2"] else 0


def check_step1(d, rep, fr_text, system):
    if system:
        return
    s = mdtab.section(d["text"], "1.1")
    para = norm_text(s["body"] if s else "")
    if not para or para.startswith("(Chưa làm"):
        rep.error("1.1", "chưa có đoạn mô tả")
        return
    if re.search(r"\(S\d+\)", para):
        rep.error("1.1", "đoạn mô tả không được chứa mã câu dạng (S1) (S2)…; số câu chỉ nằm ở bảng 1.2")
    if not rep.need_cols("1.2", d["head"]["1.2"], COLS["1.2"]):
        return
    pos = 0
    for k, r in enumerate(d["rows"]["1.2"], 1):
        num = re.sub(r"^Câu\s*", "", r["Câu"]).strip()
        if num != str(k):
            rep.error("1.2", "dòng thứ %d phải ghi Câu = %d (đang là '%s')" % (k, k, r["Câu"]))
        sent = norm_text(r["Nội dung câu"])
        if mdtab.is_empty(sent):
            rep.error("1.2", "câu %d chưa chép nguyên văn câu" % k)
            continue
        idx = para.find(sent, pos)
        if idx < 0:
            rep.error("1.2", "câu %d không khớp nguyên văn với đoạn mô tả (hoặc sai thứ tự): '%s…'" % (k, sent[:60]))
            continue
        gap = para[pos:idx].strip(" .;,:")
        if gap:
            rep.error("1.2", "phần '%s…' của đoạn mô tả chưa nằm trong câu nào của bảng 1.2" % gap[:60])
        pos = idx + len(sent)
        if mdtab.is_empty(r["Nguồn"]):
            rep.error("1.2", "câu %d chưa ghi nguồn" % k)
    tail = para[pos:].strip(" .;,:")
    if tail and d["rows"]["1.2"]:
        rep.error("1.2", "phần '%s…' cuối đoạn mô tả chưa nằm trong câu nào của bảng 1.2" % tail[:60])
    if fr_text:
        cited = set()
        for r in d["rows"]["1.2"]:
            for i in mdtab.ids_in(r["Nguồn"]):
                cited.add(i.split(".")[0])
                if i not in fr_text:
                    rep.error("1.2", "câu %s: nguồn %s không có trong FR" % (r["Câu"], i))
        _, funcs = mdtab.table_by_title(fr_text, "Danh sách chức năng")
        for f in funcs:
            fid = f.get("ID", "")
            if fid and fid not in cited:
                rep.error("1.2", "chức năng %s của FR chưa được câu nào trong đoạn mô tả nói tới" % fid)


class FrIndex:
    """Tra mã FR/BR về đúng tài liệu FR của module ghi trong mã (FR-M13-03.01 → FR-M13.md).

    Sau lượt gộp hệ thống, cột Nguồn của một module có thể dẫn mã FR của module khác (thuộc tính do module khác
    bổ sung vào lớp của module này, hoặc thuộc tính của lớp ngoài được ghi đủ). FR của module khác được tìm cạnh
    tệp --fr.
    """

    def __init__(self, fr_path, module):
        self.dir = os.path.dirname(os.path.abspath(fr_path))
        self.module = module
        self.cache = {module: mdtab.read(fr_path)}

    def text_for(self, fid):
        m = re.match(r"^(?:FR|BR)-(M\d{2})-", fid)
        mod = m.group(1) if m else self.module
        if mod not in self.cache:
            p = os.path.join(self.dir, "FR-%s.md" % mod)
            self.cache[mod] = mdtab.read(p) if os.path.exists(p) else None
        return mod, self.cache[mod]


def check_sources(d, rep, fr_index, num, label_col):
    if not fr_index:
        return
    for r in d["rows"][num]:
        for i in mdtab.ids_in(r.get("Nguồn", "")):
            mod, text = fr_index.text_for(i)
            if text is None:
                rep.error(num, "%s: không tìm thấy FR-%s.md cạnh tệp --fr để đối chiếu nguồn %s"
                          % (r.get(label_col, "?"), mod, i))
            elif i not in text:
                rep.error(num, "%s: nguồn %s không có trong FR-%s" % (r.get(label_col, "?"), i, mod))


def check_step2(d, rep, fr_text, system, fr_index=None):
    mod = d["module"]
    ok22 = rep.need_cols("2.2", d["head"]["2.2"], COLS["2.2"])
    ok23 = rep.need_cols("2.3", d["head"]["2.3"], COLS["2.3"])
    classes, attrs = {}, {}
    if ok22:
        for r in d["rows"]["2.2"]:
            c = r["Lớp"]
            if not mdtab.CLASS_RE.match(c):
                rep.error("2.2", "tên lớp '%s' phải là PascalCase tiếng Anh không dấu" % c)
            if c in classes:
                rep.error("2.2", "lớp %s xuất hiện hai lần" % c)
            classes[c] = r
            if r["Nhóm"] not in CLASS_GROUPS:
                rep.error("2.2", "%s: Nhóm '%s' không hợp lệ (%s)" % (c, r["Nhóm"], ", ".join(sorted(CLASS_GROUPS))))
            if not re.match(r"^M\d{2}$", r["Sở hữu"]):
                rep.error("2.2", "%s: Sở hữu phải là mã module dạng Mxx" % c)
            if mdtab.is_empty(r["Nguồn"]):
                rep.error("2.2", "%s chưa ghi nguồn" % c)
            if mdtab.is_empty(r["Tên tiếng Việt"]):
                rep.warn("2.2", "%s chưa có tên tiếng Việt" % c)
        check_sources(d, rep, fr_index, "2.2", "Lớp")
    if ok23:
        for r in d["rows"]["2.3"]:
            c, a = r["Lớp"], r["Thuộc tính"]
            if c not in classes:
                rep.error("2.3", "thuộc tính %s thuộc lớp %s không có ở mục 2.2" % (a, c))
            if not mdtab.ATTR_RE.match(a):
                rep.error("2.3", "%s.%s: tên thuộc tính phải là camelCase tiếng Anh không dấu" % (c, a))
            if a == "id" or re.search(r"Id$", a):
                rep.warn("2.3", "%s.%s: ở bước phân tích chưa thêm id và chưa có khóa ngoại; "
                                "quan hệ ghi ở mục 3, id thêm ở bước thiết kế lớp" % (c, a))
            if (c, a) in attrs:
                rep.error("2.3", "%s.%s xuất hiện hai lần" % (c, a))
            attrs[(c, a)] = r
            if r["Tính chất"] not in ATTR_KINDS:
                rep.error("2.3", "%s.%s: Tính chất '%s' không hợp lệ (Lưu, Dẫn xuất)" % (c, a, r["Tính chất"]))
            if mdtab.is_empty(r["Nguồn"]):
                rep.error("2.3", "%s.%s chưa ghi nguồn" % (c, a))
            basis = r["Căn cứ"]
            if basis not in ATTR_BASIS:
                rep.error("2.3", "%s.%s: Căn cứ '%s' không hợp lệ (%s)" % (c, a, basis, ", ".join(sorted(ATTR_BASIS))))
            elif basis == "Đề xuất":
                if mdtab.is_empty(r["Ghi chú"]):
                    rep.error("2.3", "%s.%s là đề xuất: cột Ghi chú phải nêu lý do (chức năng hoặc quy tắc nào cần)" % (c, a))
                if fr_text and not mdtab.ids_in(r["Nguồn"]):
                    rep.error("2.3", "%s.%s là đề xuất: cột Nguồn phải ghi mã FR/BR của chức năng hoặc quy tắc cần nó"
                              % (c, a))
            elif basis == "Tham chiếu":
                if system:
                    rep.error("2.3", "%s.%s: bản hệ thống không còn dòng Tham chiếu (thuộc tính phải nằm ở lớp của "
                                     "module sở hữu)" % (c, a))
                elif c in classes and classes[c]["Sở hữu"] == mod:
                    rep.error("2.3", "%s.%s: Tham chiếu chỉ dùng cho lớp của module khác" % (c, a))
                if mdtab.is_empty(r["Ghi chú"]):
                    rep.error("2.3", "%s.%s là tham chiếu: cột Ghi chú phải nêu module này đọc hoặc ghi nó để làm gì"
                              % (c, a))
        check_sources(d, rep, fr_index, "2.3", "Thuộc tính")
    if ok22 and ok23:
        for c, r in classes.items():
            mine = [a for (cc, a) in attrs if cc == c]
            owned = system or r["Sở hữu"] == mod
            listed = set(x.lstrip("/").strip() for x in mdtab.split_list(r["Thuộc tính"]))
            if listed != set(mine):
                miss, extra = sorted(set(mine) - listed), sorted(listed - set(mine))
                rep.error("2.2", "%s: cột Thuộc tính lệch mục 2.3 (thiếu: %s; thừa: %s)"
                          % (c, ", ".join(miss) or "—", ", ".join(extra) or "—"))
            if owned and not mine:
                if r["Nhóm"] == "Thực thể":
                    rep.error("2.3", "lớp %s chưa có thuộc tính nào: liệt kê đủ thuộc tính (nguồn nêu hoặc đề xuất kèm "
                                     "lý do); không có thật thì xem lại nó có phải thuộc tính của lớp khác" % c)
                elif r["Nhóm"] == "Thống kê":
                    rep.warn("2.3", "lớp thống kê %s chưa có thuộc tính nào" % c)
            if not owned and not mine:
                rep.warn("2.3", "lớp ngoài %s chưa có thuộc tính nào: liệt kê các thuộc tính module này đọc hoặc ghi "
                                "(Căn cứ = Tham chiếu)" % c)
    if system:
        return classes, attrs
    if rep.need_cols("2.1", d["head"]["2.1"], COLS["2.1"]):
        seen, used = {}, set()
        for r in d["rows"]["2.1"]:
            noun, kind, res = r["Danh từ"], r["Phân loại"], r["Kết quả"]
            for part in [p.strip().lower() for p in noun.split("/")]:
                if part in seen:
                    rep.error("2.1", "danh từ '%s' xuất hiện ở dòng %s và dòng %s (mỗi danh từ chỉ tính một lần)"
                              % (part, seen[part], r["#"]))
                seen[part] = r["#"]
            if kind not in LEDGER_KINDS:
                rep.error("2.1", "dòng %s: Phân loại '%s' không hợp lệ (Lớp, Thuộc tính, Loại bỏ)" % (r["#"], kind))
            elif kind == "Lớp":
                if res not in classes:
                    rep.error("2.1", "dòng %s: lớp '%s' chưa có ở mục 2.2" % (r["#"], res))
                used.add(res)
            elif kind == "Thuộc tính":
                m = re.match(r"^([A-Za-z0-9]+)\.([A-Za-z0-9]+)$", res)
                if not m:
                    rep.error("2.1", "dòng %s: Kết quả của thuộc tính phải viết dạng Lớp.thuộcTính" % r["#"])
                elif (m.group(1), m.group(2)) not in attrs:
                    rep.error("2.1", "dòng %s: %s chưa có ở mục 2.3" % (r["#"], res))
            elif kind == "Loại bỏ" and mdtab.is_empty(r["Lý do"]):
                rep.error("2.1", "dòng %s: danh từ bị loại phải ghi lý do" % r["#"])
            where = r["Xuất hiện ở"]
            mm = re.match(r"^Câu\s+(\d+)$", where)
            if mm:
                if not 1 <= int(mm.group(1)) <= sentence_count(d):
                    rep.error("2.1", "dòng %s: '%s' không có ở bảng 1.2" % (r["#"], where))
            elif not where.startswith("Quét:"):
                rep.error("2.1", "dòng %s: Xuất hiện ở phải ghi 'Câu n' hoặc 'Quét: <mã FR>'" % r["#"])
        for c, r in classes.items():
            if r["Nhóm"] != "Liên kết" and c not in used:
                rep.warn("2.1", "lớp %s không đến từ danh từ nào trong sổ danh từ" % c)
    if fr_text:
        _, ents = mdtab.table_by_title(fr_text, "Dữ liệu nghiệp vụ")
        if rep.need_cols("2.4", d["head"]["2.4"], COLS["2.4"]):
            listed = set(r["Thực thể trong FR"].lower() for r in d["rows"]["2.4"])
            for e in ents:
                name = e.get("Thực thể", "")
                if name and name.lower() not in listed:
                    rep.warn("2.4", "thực thể '%s' ở mục Dữ liệu nghiệp vụ của FR chưa được đối chiếu" % name)
            for r in d["rows"]["2.4"]:
                if mdtab.is_empty(r["Xử lý"]):
                    rep.error("2.4", "'%s' chưa ghi cách xử lý" % r["Thực thể trong FR"])
    return classes, attrs


def check_step3(d, rep, fr_text, system, classes, attrs, fr_index=None):
    mod = d["module"]
    if not rep.need_cols("3.4", d["head"]["3.4"], COLS["3.4"]):
        return
    ids, linked = set(), {}
    for r in d["rows"]["3.4"]:
        rid, a, b, kind = r["ID"], r["Lớp A"], r["Lớp B"], r["Loại"]
        if rid in ids:
            rep.error("3.4", "ID %s trùng" % rid)
        ids.add(rid)
        if not re.match(r"^R-(M\d{2}|SYS)-\d{2,3}$", rid):
            rep.error("3.4", "ID '%s' sai dạng (R-Mxx-nn)" % rid)
        for c in (a, b):
            if c not in classes:
                rep.error("3.4", "%s: lớp %s không có ở mục 2.2" % (rid, c))
            linked[c] = linked.get(c, 0) + 1
        if kind not in REL_KINDS:
            rep.error("3.4", "%s: Loại '%s' không hợp lệ (%s)" % (rid, kind, ", ".join(sorted(REL_KINDS))))
            continue
        if kind in REL_WITH_MULT:
            form = derived_form(r["Bội số A"], r["Bội số B"])
            if form is None:
                rep.error("3.4", "%s: bội số '%s' / '%s' sai cú pháp (1, 0..1, 0..*, 1..*, 1..3)"
                          % (rid, r["Bội số A"], r["Bội số B"]))
            else:
                if form == "n-n":
                    rep.error("3.4", "%s: còn quan hệ n-n giữa %s và %s; phải tách bằng lớp liên kết" % (rid, a, b))
                if r["Dạng"] != form:
                    rep.error("3.4", "%s: Dạng ghi '%s' nhưng bội số cho ra '%s'" % (rid, r["Dạng"], form))
        if kind in REL_WITH_MAIN:
            if r["Bên chính"] not in (a, b):
                rep.error("3.4", "%s: Bên chính phải là %s hoặc %s (lớp cha / lớp toàn thể / lớp được dùng)"
                          % (rid, a, b))
            elif kind == "Hợp thành":
                whole_mult = r["Bội số A"] if r["Bên chính"] == a else r["Bội số B"]
                if mdtab.clean(whole_mult) != "1":
                    rep.error("3.4", "%s: hợp thành thì mỗi thành phần thuộc đúng 1 toàn thể; bội số phía %s "
                                     "đang là '%s'" % (rid, r["Bên chính"], whole_mult))
        if kind == "Kế thừa" and a == b:
            rep.error("3.4", "%s: lớp không thể kế thừa chính nó" % rid)
        if mdtab.is_empty(r["Căn cứ"]):
            rep.error("3.4", "%s chưa ghi căn cứ chọn loại quan hệ" % rid)
        if mdtab.is_empty(r["Nguồn"]):
            rep.error("3.4", "%s chưa ghi nguồn" % rid)
    check_sources(d, rep, fr_index, "3.4", "ID")
    # lớp liên kết
    link_rows = {}
    if d["head"]["3.3"] is not None and rep.need_cols("3.3", d["head"]["3.3"], COLS["3.3"]):
        for r in d["rows"]["3.3"]:
            lc = r["Lớp liên kết"]
            link_rows[lc] = r
            if lc not in classes:
                rep.error("3.3", "lớp liên kết %s không có ở mục 2.2" % lc)
            elif classes[lc]["Nhóm"] != "Liên kết":
                rep.error("3.3", "%s phải có Nhóm = Liên kết ở mục 2.2" % lc)
            own_attrs = [a for (cc, a) in attrs if cc == lc]
            if not own_attrs and mdtab.is_empty(r["Thuộc tính riêng của liên kết"]):
                rep.error("3.3", "%s chưa có thuộc tính: ghi rõ ở cột 'Thuộc tính riêng của liên kết' vì sao không có" % lc)
            pair = mdtab.split_pair(r["Tách từ quan hệ n-n"])
            if not pair:
                rep.error("3.3", "%s: 'Tách từ quan hệ n-n' viết dạng 'LớpA – LớpB'" % lc)
            else:
                for p in pair:
                    if p not in classes:
                        rep.error("3.3", "%s: lớp %s không có ở mục 2.2" % (lc, p))
                    elif not any((x["Lớp A"], x["Lớp B"]) in ((lc, p), (p, lc)) for x in d["rows"]["3.4"]):
                        rep.error("3.3", "%s: thiếu quan hệ 1-n giữa %s và %s ở mục 3.4" % (lc, p, lc))
    for c, r in classes.items():
        # lớp liên kết của module khác được tách ở module sở hữu nó; ở đây chỉ là lớp ngoài
        if r["Nhóm"] == "Liên kết" and c not in link_rows and (system or r["Sở hữu"] == mod):
            rep.error("3.3", "lớp %s có Nhóm = Liên kết nhưng không có dòng ở mục 3.3" % c)
        if (system or r["Sở hữu"] == mod) and c not in linked:
            rep.warn("3.4", "lớp %s không có quan hệ với lớp nào (lớp mồ côi)" % c)
    if not system:
        if d["head"]["3.2"] is None:
            rep.error("3.2", "không tìm thấy bảng quan hệ số lượng")
        elif rep.need_cols("3.2", d["head"]["3.2"], COLS["3.2"]):
            for r in d["rows"]["3.2"]:
                if mdtab.is_empty(r["Câu A → B"]) or mdtab.is_empty(r["Câu B → A"]):
                    rep.error("3.2", "cặp %s: phải viết câu theo cả hai chiều" % r["Cặp"])
                if r["Dạng"] not in ("1-1", "1-n", "n-1", "n-n"):
                    rep.error("3.2", "cặp %s: Dạng '%s' không hợp lệ" % (r["Cặp"], r["Dạng"]))
                if mdtab.is_empty(r["Xử lý"]):
                    rep.error("3.2", "cặp %s chưa ghi cách xử lý" % r["Cặp"])
        ext_rows = {r["Lớp"]: r for r in d["rows"]["5"]} if d["head"]["5"] else {}
        for c, r in classes.items():
            if r["Sở hữu"] != mod and c not in ext_rows:
                rep.error("5", "lớp %s do %s sở hữu nhưng chưa có ở mục 5 Liên module" % (c, r["Sở hữu"]))
        for (c, a), r in attrs.items():
            if c in classes and classes[c]["Sở hữu"] != mod and r["Căn cứ"] != "Tham chiếu":
                added = ext_rows.get(c, {}).get("Thuộc tính module này bổ sung", "")
                if a not in [x.lstrip("/") for x in mdtab.split_list(added)]:
                    rep.warn("5", "%s.%s do module này thêm vào lớp của %s: ghi ở cột 'Thuộc tính module này bổ sung'"
                             % (c, a, classes[c]["Sở hữu"]))
    from gen_puml import build
    s4 = mdtab.section_with_children(d["text"], "4")
    mdtab.check_diagram(rep, "4", d["path"], mdtab.doc_id_of(d["fm"], d["path"]), s4, build(d))


def check_others(d, rep, classes, others_dir):
    mod = d["module"]
    owners = {}
    found_modules = set()
    for p in sorted(glob.glob(os.path.join(others_dir, "EC-M*.md"))):
        if os.path.abspath(p) == os.path.abspath(d["path"]):
            continue
        o = load_ec(p)
        found_modules.add(o["module"])
        for r in o["rows"]["2.2"]:
            if r.get("Sở hữu") == o["module"]:
                owners.setdefault(r["Lớp"], []).append(o["module"])
    for c, r in classes.items():
        own = r["Sở hữu"]
        if own == mod:
            if c in owners:
                rep.error("liên module", "lớp %s đã được %s sở hữu; module này phải tham chiếu hoặc đổi tên"
                          % (c, ", ".join(owners[c])))
        elif own in found_modules:
            if own not in owners.get(c, []):
                rep.warn("liên module", "lớp %s ghi là của %s nhưng EC-%s.md không có lớp này" % (c, own, own))
        else:
            rep.info("liên module", "lớp %s của %s: chưa có EC-%s.md để đối chiếu, sẽ kiểm ở lượt gộp" % (c, own, own))


def check_final(d, rep, system):
    if "(Chưa làm" in mdtab.strip_comments(d["text"]):
        rep.error("chốt", "còn mục ghi '(Chưa làm …)'")
    if d["head"]["6"] is not None and rep.need_cols("6", d["head"]["6"], COLS["6"]):
        for r in d["rows"]["6"]:
            if mdtab.is_empty(r["Trả lời"]):
                rep.error("6", "%s chưa có trả lời" % r["Mã"])
    for k in ("module", "ma_tai_lieu", "phien_ban", "trang_thai", "nguon"):
        if not d["fm"].get(k):
            rep.error("frontmatter", "thiếu trường %s" % k)


def main():
    mdtab.utf8_stdout()
    ap = argparse.ArgumentParser(description="Kiểm tài liệu phân tích lớp thực thể")
    ap.add_argument("--ec", required=True)
    ap.add_argument("--fr", help="tệp FR-Mxx.md để kiểm nguồn và độ phủ chức năng")
    ap.add_argument("--step", type=int, choices=[1, 2, 3], help="chỉ kiểm tới bước này")
    ap.add_argument("--final", action="store_true", help="kiểm đầy đủ trước khi chốt")
    ap.add_argument("--system", action="store_true", help="tài liệu gộp hệ thống (EC-SYS.md)")
    ap.add_argument("--others", help="thư mục chứa các EC-Mxx.md khác để đối chiếu tên lớp")
    a = ap.parse_args()
    d = load_ec(a.ec)
    rep = mdtab.Report("check_ec %s" % os.path.basename(a.ec))
    fr_text = mdtab.read(a.fr) if a.fr else None
    fr_index = FrIndex(a.fr, d["module"]) if a.fr else None
    upto = 3 if (a.final or a.step is None) else a.step
    if upto >= 1:
        check_step1(d, rep, fr_text, a.system)
    classes, attrs = {}, {}
    if upto >= 2:
        res = check_step2(d, rep, fr_text, a.system, fr_index)
        classes = res[0] if res else {}
        attrs = res[1] if res else {}
    if upto >= 3:
        check_step3(d, rep, fr_text, a.system, classes, attrs, fr_index)
    if a.others and classes and not a.system:
        check_others(d, rep, classes, a.others)
    if a.final:
        check_final(d, rep, a.system)
    sys.exit(rep.finish())


if __name__ == "__main__":
    main()
