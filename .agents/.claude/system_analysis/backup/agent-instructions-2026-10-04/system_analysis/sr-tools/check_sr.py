#!/usr/bin/env python3
"""check_sr.py - kiem tra tu dong mot tai lieu SR cua iShare (cau truc, ID, EARS, truy vet, bao phu).

  python3 check_sr.py --sr specs/ISH-SR-M05.md [--routing specs/routing/ISH-RT-M05.md] \
        [--inventory inventory-M05.json] [--json ket-qua.json]
Thoat 1 neu co ERROR. WARN/INFO khong lam that bai nhung phai duoc Author xu ly hoac giai thich.
Chi doc, khong sua file.
"""
import argparse, json, re, sys

ISH_ID = re.compile(r'\bISH-M(\d{2})-(\d{3})(?:\.(\d+))?\b')
SRC_ID = re.compile(r'\b(?:ISS|QA|DEC|OPEN)-\d{3}\b')
SRC_OK = re.compile(r'^(?:(?:ISS|QA|DEC|OPEN)-\d{3}|DRAFT §[\d.]+(?:\s*[–-]\s*[\d.]+)?)$')
STATUS = {'Bản nháp', 'Đã audit', 'Đã chốt'}
VAGUE = ['nhanh chóng', 'dễ dàng', 'thân thiện', 'phù hợp', 'thích hợp', 'hợp lý', 'đầy đủ', 'khoảng', 'v.v', 'vân vân',
         'etc', 'nếu có thể', 'nếu cần', 'khi cần thiết', 'tối ưu', 'linh hoạt', 'thông thường', 'một số', 'nhiều',
         'tương tự', 'bao gồm nhưng không giới hạn', 'tùy trường hợp', 'càng sớm', 'cơ bản', 'kịp thời', 'mượt']
ESCAPE = ['nếu có thể', 'nếu cần', 'khi cần thiết', 'nếu phù hợp', 'trừ khi cần', 'nếu khả thi', 'tùy trường hợp']
TECH = ['postgresql', 'pgvector', 'cloudinary', 'openai', 'gpt', 'websocket', 'sse', 'react', 'spring', 'redis', 'sql',
        'api', 'endpoint', 'json', 'jwt', 'tiptap', 'table', 'bảng dữ liệu', 'cột ', 'column', 'database', 'cơ sở dữ liệu',
        'cron', 'queue', 'hàng đợi', 'cache', 'index']
PRON = [r'\bnó\b', r'\bchúng\b', r'\bhọ\b']
EARS_START = ('hệ thống phải', 'khi ', 'trong khi ', 'đối với ', 'nếu ')
SNAKE = re.compile(r'\b[a-z]+(?:_[a-z0-9]+)+\b')

errs, warns, infos = [], [], []


def E(c, m, ln=None): errs.append((c, m, ln))
def W(c, m, ln=None): warns.append((c, m, ln))
def I(c, m, ln=None): infos.append((c, m, ln))


def cells(row):
    return [c.strip() for c in row.strip().strip('|').split('|')]


def is_sep(row):
    return bool(re.fullmatch(r'\s*\|?\s*:?-{2,}:?\s*(\|\s*:?-{2,}:?\s*)*\|?\s*', row))


def table_rows(lines, start):
    """Doc bang bat dau tu dong start (0-based, dong header). Tra ve [(lineno1, [cells])] khong gom header/separator."""
    out, i = [], start
    while i < len(lines) and lines[i].lstrip().startswith('|'):
        if i != start and not is_sep(lines[i]):
            out.append((i + 1, cells(lines[i])))
        i += 1
    return out


def find_table_after(lines, idx):
    for j in range(idx, min(idx + 8, len(lines))):
        if lines[j].lstrip().startswith('|'):
            return j
        if lines[j].startswith('#'):
            return None
    return None


def strip_code(lines):
    out, fence = [], False
    for t in lines:
        if t.strip().startswith('`' * 3):
            fence = not fence
            out.append('')
        else:
            out.append('' if fence else t)
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--sr', required=True)
    ap.add_argument('--routing')
    ap.add_argument('--inventory')
    ap.add_argument('--json')
    a = ap.parse_args()
    raw = open(a.sr, encoding='utf-8').read().split('\n')
    L = strip_code(raw)

    # ---- tieu de & header
    hdr = {}
    for i, t in enumerate(L):
        if t.lstrip().startswith('|'):
            c = cells(t)
            if len(c) >= 2 and not is_sep(t):
                hdr[c[0].strip('* ')] = (c[1], i + 1)
        elif t.startswith('## '):
            break
    for k in ['Mã tài liệu', 'Dự án', 'Module', 'Trạng thái', 'Phiên bản', 'Ngày', 'Tác giả']:
        if k not in hdr:
            E('HDR-01', 'Thiếu trường header "%s"' % k)
    for k in hdr:
        if re.search(r'duyệt|phê duyệt|reviewer|approver|kiểm tra|thẩm định', k, re.I):
            E('HDR-02', 'Không dùng trường người duyệt/thẩm định: "%s"' % k, hdr[k][1])
    mod = None
    if 'Mã tài liệu' in hdr:
        m = re.fullmatch(r'ISH-SR-M(\d{2})', hdr['Mã tài liệu'][0])
        if not m:
            E('HDR-03', 'Mã tài liệu phải dạng ISH-SR-Mxx, hiện là "%s"' % hdr['Mã tài liệu'][0], hdr['Mã tài liệu'][1])
        else:
            mod = m.group(1)
    if 'Tác giả' in hdr and hdr['Tác giả'][0] != 'Phạm Văn Đức':
        E('HDR-04', 'Tác giả phải là "Phạm Văn Đức"', hdr['Tác giả'][1])
    if 'Trạng thái' in hdr and hdr['Trạng thái'][0] not in STATUS:
        E('HDR-05', 'Trạng thái phải thuộc %s' % sorted(STATUS), hdr['Trạng thái'][1])
    if 'Phiên bản' in hdr and not re.fullmatch(r'\d+\.\d+', hdr['Phiên bản'][0]):
        E('HDR-06', 'Phiên bản phải dạng 0.1', hdr['Phiên bản'][1])
    if 'Ngày' in hdr and not re.fullmatch(r'\d{4}-\d{2}-\d{2}', hdr['Ngày'][0]):
        E('HDR-07', 'Ngày phải dạng YYYY-MM-DD', hdr['Ngày'][1])
    if 'Module' in hdr and mod and not hdr['Module'][0].startswith('M' + mod):
        E('HDR-08', 'Trường Module phải bắt đầu bằng M%s' % mod, hdr['Module'][1])

    # ---- heading
    heads = [(i + 1, t) for i, t in enumerate(L) if re.match(r'^#{2,3}\s', t)]
    h2 = [(n, t[3:].strip()) for n, t in heads if t.startswith('## ')]
    want = [r'^1\.\s', r'^2\.\s', r'^3\.\s', r'^4\.\s', r'^5\.\s', r'^6\.\s', r'^Phụ lục A', r'^Phụ lục B']
    pos = []
    for w in want:
        f = [n for n, t in h2 if re.match(w, t)]
        if len(f) != 1:
            E('STR-01', 'Mục cấp 2 "%s" phải xuất hiện đúng 1 lần (thấy %d)' % (w, len(f)))
        pos.append(f[0] if f else None)
    got = [p for p in pos if p]
    if got != sorted(got):
        E('STR-02', 'Thứ tự mục cấp 2 phải là 1,2,3,4,5,6,Phụ lục A,Phụ lục B')
    h3 = [(n, t[4:].strip()) for n, t in heads if t.startswith('### ')]
    for sub in ['1.1', '2.1', '2.2', '3.1', '3.2', '4.1', '5.1', '5.2']:
        if not any(t.startswith(sub + ' ') or t.startswith(sub + '.') for _, t in h3):
            E('STR-03', 'Thiếu mục %s' % sub)
    sec5 = [(n, t) for n, t in h3 if re.match(r'^5\.\d+\s', t)]
    if len(sec5) >= 4:
        if 'HMI' not in sec5[-2][1]:
            E('STR-04', 'Mục kế cuối của 5 phải là "Yêu cầu HMI"', sec5[-2][0])
        if not re.search(r'chuyển màn hình', sec5[-1][1], re.I):
            E('STR-05', 'Mục cuối của 5 phải là "Chuyển màn hình"', sec5[-1][0])
    else:
        E('STR-06', 'Mục 5 phải có tối thiểu 5.1, 5.2, 1 tính năng, HMI, Chuyển màn hình')
    nums = [int(re.match(r'^5\.(\d+)', t).group(1)) for _, t in sec5]
    if nums != list(range(1, len(nums) + 1)):
        E('STR-07', 'Số thứ tự mục 5.x phải liên tục từ 5.1: %s' % nums)

    # ---- tinh nang & yeu cau
    defs = {}      # id -> (line, text, kind)
    feats = []
    bounds = [n for n, _ in sec5] + [pos[6] or len(L) + 1]
    for idx, (n, t) in enumerate(sec5):
        if idx < 2 or idx >= len(sec5) - 2:
            continue
        end = bounds[idx + 1]
        blk = L[n:end - 1]
        base = n  # lineno cua dong sau heading = n+1
        feat = dict(title=t, line=n, upper=[], lower=[], reason=False)
        mode = None
        j = 0
        while j < len(blk):
            line = blk[j]
            s = line.strip()
            if re.match(r'^\*\*Yêu cầu cấp trên\*\*', s):
                mode = 'upper'
            elif re.match(r'^\*\*Lý do\*\*', s):
                mode = 'reason'
                feat['reason'] = True
            elif re.match(r'^\*\*Yêu cầu cấp dưới\*\*', s):
                mode = 'lower'
            elif s.startswith('|') and mode in ('upper', 'lower'):
                rows = table_rows(blk, j)
                for ln, c in rows:
                    if len(c) < 2:
                        E('REQ-01', 'Hàng yêu cầu phải có 2 cột: ID | Yêu cầu', base + ln)
                        continue
                    feat[mode].append((base + ln, c[0], c[1]))
                j += len(rows) + 1
            j += 1
        feats.append(feat)
        for ln, i_, tx in feat['upper']:
            defs[i_] = (ln, tx, 'upper')
        for ln, i_, tx in feat['lower']:
            defs[i_] = (ln, tx, 'lower')
        if len(feat['upper']) != 1:
            E('REQ-02', 'Mục %s phải có đúng 1 yêu cầu cấp trên (thấy %d)' % (t, len(feat['upper'])), n)
        if not feat['lower']:
            E('REQ-03', 'Mục %s chưa có yêu cầu cấp dưới' % t, n)
        if not feat['reason']:
            E('REQ-04', 'Mục %s thiếu "Lý do"' % t, n)
    if not feats:
        E('REQ-00', 'Không tìm thấy tính năng nào trong mục 5.3…')

    seen = {}
    all_rows = [(ln, i_, tx, 'upper') for f in feats for ln, i_, tx in f['upper']] + \
               [(ln, i_, tx, 'lower') for f in feats for ln, i_, tx in f['lower']]
    for ln, i_, tx, kind in all_rows:
        m = re.fullmatch(r'ISH-M(\d{2})-(\d{3})(?:\.(\d+))?', i_)
        if not m:
            E('ID-01', 'ID "%s" sai dạng ISH-Mxx-nnn[.n]' % i_, ln)
            continue
        if mod and m.group(1) != mod:
            E('ID-02', 'ID "%s" không thuộc module M%s' % (i_, mod), ln)
        if kind == 'upper' and m.group(3):
            E('ID-03', 'Yêu cầu cấp trên "%s" không được có hậu tố .n' % i_, ln)
        if kind == 'lower' and not m.group(3):
            E('ID-04', 'Yêu cầu cấp dưới "%s" phải có hậu tố .n' % i_, ln)
        if i_ in seen:
            E('ID-05', 'ID trùng "%s" (cũng ở dòng %d)' % (i_, seen[i_]), ln)
        seen[i_] = ln
    for f in feats:
        if len(f['upper']) == 1:
            up = f['upper'][0][1]
            for ln, i_, _ in f['lower']:
                if not i_.startswith(up + '.'):
                    E('ID-06', 'Yêu cầu cấp dưới "%s" phải thuộc cấp trên "%s" của cùng mục' % (i_, up), ln)

    # ---- lint noi dung
    for ln, i_, tx, kind in all_rows:
        low = tx.lower()
        if not low.startswith(EARS_START):
            E('EARS-01', '%s: câu phải bắt đầu bằng "Hệ thống phải", "Khi", "Trong khi", "Đối với" hoặc "Nếu"' % i_, ln)
        if 'hệ thống phải' not in low:
            E('EARS-02', '%s: thiếu cụm "hệ thống phải"' % i_, ln)
        if low.startswith('nếu ') and ' thì ' not in low:
            W('EARS-03', '%s: mẫu "Nếu … thì …" thiếu "thì"' % i_, ln)
        if low.count('phải') > 1:
            W('RULE-01', '%s: có hơn một "phải" — có thể chứa nhiều yêu cầu, cân nhắc tách' % i_, ln)
        if re.search(r'và/hoặc|\bvà\b.*\bhoặc\b|\bhoặc\b.*\bvà\b', low):
            E('RULE-02', '%s: không dùng "và/hoặc" hoặc trộn "và" với "hoặc" trong một câu' % i_, ln)
        for v in ESCAPE:
            if v in low:
                E('RULE-03', '%s: cụm thoát "%s" làm yêu cầu không kiểm chứng được' % (i_, v), ln)
        for v in VAGUE:
            if v not in ESCAPE and re.search(r'(?<!\w)' + re.escape(v) + r'(?!\w)', low):
                W('RULE-04', '%s: từ mơ hồ "%s" — thay bằng giá trị/điều kiện đo được' % (i_, v), ln)
        for p in PRON:
            if re.search(p, low):
                E('RULE-05', '%s: không dùng đại từ thay thế ("%s") — nhắc lại danh từ' % (i_, re.search(p, low).group(0)), ln)
        for v in TECH:
            if re.search(r'(?<![\w-])' + re.escape(v.strip()) + r'(?!\w)', low):
                W('RULE-06', '%s: có thuật ngữ giải pháp/công nghệ "%s" — SR không nêu giải pháp (để Phase 7/8)' % (i_, v.strip()), ln)
        sn = SNAKE.findall(tx)
        if sn:
            W('RULE-07', '%s: có tên trường/biến dạng snake_case %s — mô tả bằng khái niệm nghiệp vụ' % (i_, sn[:3]), ln)
        if len(tx.split()) > 60:
            W('RULE-08', '%s: dài %d từ — cân nhắc tách' % (i_, len(tx.split())), ln)
        if re.search(r'TBD|TODO|\?\?|\{\{|\[…\]|<[^>\n]{1,30}>', tx):
            E('RULE-09', '%s: còn placeholder/TBD' % i_, ln)
        if ISH_ID.search(tx):
            for m in ISH_ID.finditer(tx):
                if mod and m.group(1) == mod and m.group(0) not in defs:
                    E('REF-01', '%s: tham chiếu đến ID không tồn tại "%s"' % (i_, m.group(0)), ln)
                elif mod and m.group(1) != mod:
                    I('REF-02', '%s: tham chiếu module khác %s (cần kiểm ID tồn tại bên SR đó)' % (i_, m.group(0)), ln)

    # ---- phu luc A
    srcs_in_sr = set()
    appA = {}
    if pos[6]:
        a_idx = pos[6]
        t_i = find_table_after(L, a_idx)
        if t_i is None:
            E('TRC-01', 'Phụ lục A phải có bảng ID | Nguồn | Cơ sở | Ghi chú')
        else:
            hc = cells(L[t_i])
            if [x.lower() for x in hc[:3]] != ['id', 'nguồn', 'cơ sở']:
                E('TRC-02', 'Header Phụ lục A phải bắt đầu: ID | Nguồn | Cơ sở', t_i + 1)
            for ln, c in table_rows(L, t_i):
                if len(c) < 3:
                    E('TRC-03', 'Hàng Phụ lục A thiếu cột', ln)
                    continue
                i_, src, basis = c[0], c[1], c[2]
                note = c[3] if len(c) > 3 else ''
                if i_ in appA:
                    E('TRC-04', 'ID %s xuất hiện 2 lần trong Phụ lục A' % i_, ln)
                appA[i_] = ln
                toks = [x.strip() for x in re.split(r'[;,]', src) if x.strip()]
                if not toks:
                    E('TRC-05', '%s: cột Nguồn trống' % i_, ln)
                for tk in toks:
                    if not SRC_OK.match(tk):
                        E('TRC-06', '%s: nguồn "%s" sai dạng (ISS/QA/DEC/OPEN-nnn hoặc DRAFT §x.y)' % (i_, tk), ln)
                srcs_in_sr.update(SRC_ID.findall(src))
                if basis not in ('Nói thẳng', 'Suy ra'):
                    E('TRC-07', '%s: Cơ sở phải là "Nói thẳng" hoặc "Suy ra"' % i_, ln)
                if basis == 'Suy ra' and not note:
                    W('TRC-08', '%s: "Suy ra" nên có Ghi chú giải thích suy luận' % i_, ln)
        for i_ in defs:
            if i_ not in appA:
                E('TRC-09', 'ID %s chưa có trong Phụ lục A' % i_, defs[i_][0])
        for i_, ln in appA.items():
            if i_ not in defs:
                E('TRC-10', 'Phụ lục A có ID "%s" không tồn tại trong thân tài liệu' % i_, ln)

    # ---- phu luc B
    if pos[7]:
        end = len(L) + 1
        blkB = '\n'.join(L[pos[7]:end - 1])
        ops = re.findall(r'\bOP-M(\d{2})-(\d{2})\b', blkB)
        for mm, _ in ops:
            if mod and mm != mod:
                E('OPN-01', 'Mã điểm mở thuộc module khác (OP-M%s)' % mm)
        stat = hdr.get('Trạng thái', ('', 0))[0]
        none_ok = re.search(r'Không có', blkB)
        if stat == 'Đã chốt' and ops:
            E('OPN-02', 'Trạng thái "Đã chốt" nhưng Phụ lục B còn %d điểm mở' % len(set(ops)))
        if not ops and not none_ok:
            E('OPN-03', 'Phụ lục B phải liệt kê OP-Mxx-nn hoặc ghi "Không có"')

    # ---- lich su
    if pos[5] and pos[6]:
        t_i = find_table_after(L, pos[5])
        if t_i is None:
            E('REV-01', 'Mục 6 phải có bảng lịch sử sửa đổi')
        else:
            rows = table_rows(L, t_i)
            if not rows:
                E('REV-02', 'Lịch sử sửa đổi chưa có dòng nào')
            elif 'Phiên bản' in hdr and rows[-1][1][0] != hdr['Phiên bản'][0]:
                E('REV-03', 'Phiên bản dòng cuối lịch sử (%s) khác header (%s)' % (rows[-1][1][0], hdr['Phiên bản'][0]), rows[-1][0])

    # ---- bao phu so voi inventory + routing
    routed = set()
    if a.routing:
        rt = open(a.routing, encoding='utf-8').read()
        routed = set(SRC_ID.findall(rt))
        m = re.search(r'ISH-RT-M(\d{2})', rt)
        if not m or (mod and m.group(1) != mod):
            E('RT-01', 'Routing file phải có mã ISH-RT-M%s' % (mod or 'xx'))
    if a.inventory:
        inv = json.load(open(a.inventory, encoding='utf-8'))
        owned = [x['id'] for x in inv['owned']]
        for sid in owned:
            if sid not in srcs_in_sr and sid not in routed:
                E('COV-01', 'Mục nguồn %s chưa được xử lý (không có trong Phụ lục A, cũng không trong routing file)' % sid)
        known = set(inv.get('all_ids', owned))
        for sid in srcs_in_sr | routed:
            if sid not in known:
                E('COV-02', 'ID nguồn "%s" không tồn tại trong register' % sid)
        both = (srcs_in_sr & routed) & set(owned)
        for sid in sorted(both):
            I('COV-03', 'Nguồn %s vừa ở SR vừa ở routing (hợp lệ nếu một phần nội dung được chuyển đi — Author giải thích)' % sid)
        I('COV-00', 'OWNED=%d, trong SR=%d, trong routing=%d' % (len(owned), len(set(owned) & srcs_in_sr), len(set(owned) & routed)))
    else:
        I('COV-99', 'Chưa truyền --inventory nên bỏ qua kiểm bao phủ nguồn')

    # ---- ket qua
    for tag, lst in (('ERROR', errs), ('WARN', warns), ('INFO', infos)):
        for c, m, ln in lst:
            print('%-5s %-8s %s%s' % (tag, c, m, ('  [dòng %d]' % ln) if ln else ''))
    print('---\nERROR=%d WARN=%d INFO=%d | yêu cầu cấp trên=%d, cấp dưới=%d' % (
        len(errs), len(warns), len(infos), sum(1 for r in all_rows if r[3] == 'upper'), sum(1 for r in all_rows if r[3] == 'lower')))
    if a.json:
        json.dump(dict(errors=errs, warnings=warns, info=infos), open(a.json, 'w', encoding='utf-8'), ensure_ascii=False, indent=1)
    sys.exit(1 if errs else 0)


if __name__ == '__main__':
    main()
