#!/usr/bin/env python3
"""inventory.py - gom nguon (register + DRAFT) cho mot module iShare.

Cach dung:
  python3 inventory.py --registers <DIR registers> --module M05 \
      [--draft <DIR docs/_temp>] [--keywords "topic,tag,lop"] \
      [--out inventory-M05.md] [--json inventory-M05.json]

Dau ra:
  OWNED      : muc nam trong section "## ... Mxx ..." cua decisions/issue-queue/qa-log (+ dong module-registry)
  REFERENCING: muc o section khac nhung nhac "Mxx" hoac nhac ID cua muc OWNED (ung vien: amendment / module khac)
  CROSS-CUT  : chi muc (ID + tieu de) cua cac section khong gan module (Phase 6, prep...)
  DRAFT      : cac muc cua DRAFT co chua tu khoa (de doi chieu DRAFT <-> register)
Chi doc, khong sua file nao.
"""
import argparse, json, os, re, sys

ID_RE = re.compile(r'\b(ISS|QA|DEC|OPEN)-(\d{3})\b')
MOD_RE = re.compile(r'\bM(\d{2})\b')


def read(p):
    with open(p, encoding='utf-8') as f:
        return f.read().split('\n')


def sections(lines):
    """Tra ve list (heading, start_line_1based, [(lineno, text)])."""
    out, cur = [], ('(preamble)', 1, [])
    for i, t in enumerate(lines, 1):
        if t.startswith('## '):
            out.append(cur)
            cur = (t[3:].strip(), i, [])
        else:
            cur[2].append((i, t))
    out.append(cur)
    return out


def items_in(fname, body):
    """Tach muc theo dinh dang tung file. Tra ve list dict(id, line, title, text)."""
    items = []
    kind = {'decisions.md': 'DEC', 'issue-queue.md': 'ISS', 'qa-log.md': 'QA', 'open-issues.md': 'OPEN'}[fname]
    cur = None
    for ln, t in body:
        m_block = re.match(r'^###\s+(%s-\d{3})\b[:\s-]*(.*)$' % kind, t)
        m_old = re.match(r'^-\s+\*\*ID:\*\*\s+(%s-\d{3})' % kind, t) if kind == 'DEC' else None
        m_row = re.match(r'^\|\s*(%s-\d{3})\s*\|(.*)\|\s*$' % kind, t)
        if m_block or m_old or m_row:
            if cur:
                items.append(cur)
            if m_block:
                cur = dict(id=m_block.group(1), line=ln, title=m_block.group(2).strip(), text=[t])
            elif m_old:
                cur = dict(id=m_old.group(1), line=ln, title='', text=[t])
            else:
                cells = [c.strip() for c in m_row.group(2).split('|')]
                cur = dict(id=m_row.group(1), line=ln, title=cells[0] if cells else '', text=[t])
            continue
        if cur is not None:
            if t.startswith('---') or t.startswith('## ') or (t.startswith('|') and kind in ('ISS', 'QA', 'OPEN')):
                items.append(cur)
                cur = None
            else:
                cur['text'].append(t)
    if cur:
        items.append(cur)
    for it in items:
        it['text'] = '\n'.join(x for x in it['text'] if x.strip())
        if not it['title']:
            m = re.search(r'\*\*(?:Title|Tiêu đề|Question|Decision):?\*\*:?\s*(.*)', it['text'])
            it['title'] = (m.group(1) if m else it['text'].split('\n')[0])[:100]
    return items


def short(s, n=170):
    s = re.sub(r'\s+', ' ', s).strip()
    return s if len(s) <= n else s[:n - 1] + '…'


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--registers', required=True)
    ap.add_argument('--module', required=True, help='vi du M05')
    ap.add_argument('--draft')
    ap.add_argument('--keywords', default='')
    ap.add_argument('--out')
    ap.add_argument('--json')
    a = ap.parse_args()
    mod = a.module.upper()
    if not re.fullmatch(r'M\d{2}', mod):
        sys.exit('module phai co dang Mxx')

    owned, refs, cross, id_section = [], [], [], {}
    files = ['decisions.md', 'issue-queue.md', 'qa-log.md', 'open-issues.md']
    for fn in files:
        p = os.path.join(a.registers, fn)
        if not os.path.exists(p):
            print('CANH BAO: thieu', p, file=sys.stderr)
            continue
        for head, start, body in sections(read(p)):
            mods = set('M' + x for x in MOD_RE.findall(head))
            if fn == 'open-issues.md':
                scope = 'cross'
            elif mod in mods:
                scope = 'owned'
            elif mods:
                scope = 'other'
            elif head.startswith('Phase 5') or head.startswith('(preamble)') or head.startswith('Phase 3') or head.startswith('Phase 1') or head.startswith('Phase 2') or head.startswith('Phase 4'):
                scope = 'other'
            else:
                scope = 'cross'
            for it in items_in(fn, body):
                it.update(file=fn, section=head)
                id_section[it['id']] = scope
                {'owned': owned, 'cross': cross, 'other': refs}[scope].append(it)

    owned_ids = {i['id'] for i in owned}
    # REFERENCING: muc ngoai OWNED nhac Mxx hoac ID cua OWNED
    ref_hits = []
    for it in refs + cross:
        why = []
        if mod in {'M' + x for x in MOD_RE.findall(it['text'])}:
            why.append('nhac ' + mod)
        hit = sorted({m.group(0) for m in ID_RE.finditer(it['text'])} & owned_ids - {it['id']})
        if hit:
            why.append('nhac ' + ','.join(hit))
        if why:
            it2 = dict(it)
            it2['why'] = '; '.join(why)
            ref_hits.append(it2)
    hit_ids = {i['id'] for i in ref_hits}
    cross_items = [i for i in cross if i['id'] not in hit_ids]
    kw_list = [k.strip().lower() for k in a.keywords.split(',') if k.strip()]
    kw_hits = []
    if kw_list:
        for it in refs + cross:
            if it['id'] in hit_ids:
                continue
            low = it['text'].lower()
            ks = [k for k in kw_list if re.search(r'\b' + re.escape(k), low)]
            if ks:
                kw_hits.append(dict(it, why='tu khoa: ' + ','.join(ks)))
        cross_items = [i for i in cross_items if i['id'] not in {k['id'] for k in kw_hits}]

    # module-registry row
    reg_rows = []
    mr = os.path.join(a.registers, 'module-registry.md')
    if os.path.exists(mr):
        for ln, t in enumerate(read(mr), 1):
            if re.match(r'^\|\s*%s\s*\|' % mod, t) or (mod in t and ('Amend' in t or 'amend' in t)):
                reg_rows.append((ln, short(t, 400)))

    # DRAFT
    draft_hits = []
    kws = [k.strip().lower() for k in a.keywords.split(',') if k.strip()]
    if a.draft and kws:
        for fn in ('iShare_specs_general.md', 'iShare_modules.md', 'iShare_dev_priority.md'):
            p = os.path.join(a.draft, fn)
            if not os.path.exists(p):
                continue
            lines = read(p)
            heads = [(i, t) for i, t in enumerate(lines, 1) if re.match(r'^#{2,3}\s', t)]
            heads.append((len(lines) + 1, ''))
            for (s, h), (e, _) in zip(heads, heads[1:]):
                chunk = '\n'.join(lines[s - 1:e - 1]).lower()
                n = sum(chunk.count(k) for k in kws)
                if n:
                    draft_hits.append(dict(file=fn, start=s, end=e - 1, heading=h.strip('# ').strip(), hits=n))

    nxt = {}
    for k in ('ISS', 'QA', 'DEC', 'OPEN'):
        nums = [int(x.split('-')[1]) for x in id_section if x.startswith(k + '-')]
        nxt[k] = '%s-%03d' % (k, (max(nums) if nums else 0) + 1)
    # ---- render
    o = []
    o.append('# Inventory %s\n' % mod)
    o.append('Nguon: registers=%s | keywords=%s\n' % (a.registers, ','.join(kws) or '(none)'))
    o.append('ID ke tiep con trong (de ghi register): ' + ', '.join(nxt.values()) + '\n')
    o.append('## OWNED (%d muc)\n' % len(owned))
    for fn in files:
        sub = [i for i in owned if i['file'] == fn]
        if not sub:
            continue
        o.append('### %s (%d)\n' % (fn, len(sub)))
        o.append('| ID | Dong | Section | Tieu de / noi dung rut gon |\n|---|---|---|---|')
        for i in sub:
            o.append('| %s | %d | %s | %s |' % (i['id'], i['line'], short(i['section'], 40), short(i['title'] or i['text'], 120).replace('|', '/')))
        o.append('')
    o.append('### module-registry\n')
    for ln, t in reg_rows:
        o.append('- L%d: %s' % (ln, t))
    o.append('\n## REFERENCING (%d muc) - ung vien amendment / module khac, Author phai phan loai\n' % len(ref_hits))
    o.append('| ID | File:dong | Section | Ly do | Rut gon |\n|---|---|---|---|---|')
    for i in ref_hits:
        o.append('| %s | %s:%d | %s | %s | %s |' % (i['id'], i['file'], i['line'], short(i['section'], 30), i['why'], short(i['text'], 110).replace('|', '/')))
    o.append('\n## KEYWORD hits trong register (%d muc) - muc khong nhac %s nhung khop tu khoa; Author phan loai\n' % (len(kw_hits), mod))
    for i in kw_hits:
        o.append('- %s (%s:%d, %s) [%s] %s' % (i['id'], i['file'], i['line'], short(i['section'], 28), i['why'], short(i['title'] or i['text'], 110)))
    o.append('\n## CROSS-CUTTING index (%d muc, chua nhac module) - doc lai tieu de, chon muc ap dung cho %s\n' % (len(cross_items), mod))
    for i in cross_items:
        o.append('- %s (%s:%d) %s' % (i['id'], i['file'], i['line'], short(i['title'] or i['text'], 100)))
    o.append('\n## DRAFT hits (%d)\n' % len(draft_hits))
    o.append('| File | Dong | Muc | So lan khop |\n|---|---|---|---|')
    for d in draft_hits:
        o.append('| %s | %d-%d | %s | %d |' % (d['file'], d['start'], d['end'], d['heading'], d['hits']))
    txt = '\n'.join(o) + '\n'
    if a.out:
        with open(a.out, 'w', encoding='utf-8') as f:
            f.write(txt)
    else:
        print(txt)
    if a.json:
        payload = dict(module=mod, owned=[dict(id=i['id'], file=i['file'], line=i['line'], title=short(i['title'], 120)) for i in owned],
                       all_ids=sorted(id_section), next_ids=nxt,
                       referencing=[dict(id=i['id'], file=i['file'], line=i['line'], why=i['why']) for i in ref_hits],
                       draft=draft_hits)
        with open(a.json, 'w', encoding='utf-8') as f:
            json.dump(payload, f, ensure_ascii=False, indent=1)
    print('OWNED=%d REFERENCING=%d CROSS=%d DRAFT=%d' % (len(owned), len(ref_hits), len(cross_items), len(draft_hits)), file=sys.stderr)


if __name__ == '__main__':
    main()
