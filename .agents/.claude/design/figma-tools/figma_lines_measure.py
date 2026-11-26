"""Do so dong cua moi doan chu nhieu dong trong cac goi figma/*.html (Chromium).
Ghi multiline_text.json: {artboard: [[text, so_dong, be_rong_chu, be_rong_phan_tu], ...]}.
Dung kem figma_lines_sync.tpl.js (thay __PID__, __T__, __DATA__ = {artboard: [[chi_so_text, so_dong, be_rong_chu, be_rong_phan_tu]]})
de chinh so dong chu trong Figma khop trinh duyet. Khong do o nhap (input/textarea)."""
import json, glob, os, sys
from playwright.sync_api import sync_playwright
JS = r"""
() => {
  const out = {};
  for (const sec of document.querySelectorAll('section.ab')) {
    const list = [];
    const walker = document.createTreeWalker(sec, NodeFilter.SHOW_ELEMENT);
    let el = walker.currentNode;
    while (el) {
      const direct = [...el.childNodes].some(n => n.nodeType === 3 && n.textContent.trim());
      if (direct && !el.querySelector('br')) {
        const r = document.createRange(); r.selectNodeContents(el);
        const tops = [];
        for (const rc of r.getClientRects()) { if (rc.width < 1) continue; if (!tops.some(t => Math.abs(t - rc.top) < 3)) tops.push(rc.top); }
        const txt = el.textContent.replace(/\s+/g, ' ').trim();
        if (tops.length >= 2 && txt) { const rb = r.getBoundingClientRect(); list.push([txt, tops.length, Math.round(rb.width * 10) / 10, Math.round(el.getBoundingClientRect().width * 10) / 10]); }
      }
      el = walker.nextNode();
    }
    out[sec.id] = list;
  }
  return out;
}
"""
files = sorted(glob.glob('/home/claude/a/figma/*.html'))
# math packs (am-*) override plain packs for the same artboard
files = [f for f in files if not os.path.basename(f).startswith('am')] + [f for f in files if os.path.basename(f).startswith('am')]
res = {}
with sync_playwright() as p:
    b = p.chromium.launch()
    pg = b.new_page(viewport={'width': 1600, 'height': 1000})
    for f in files:
        pg.goto('file://' + f); pg.wait_for_timeout(300)
        pg.evaluate('document.fonts.ready')
        for k, v in pg.evaluate(JS).items(): res[k] = v
    b.close()
json.dump(res, open('/home/claude/a/qa_lines/multiline_text.json', 'w'), ensure_ascii=False)
print(len(res), sum(len(v) for v in res.values()))
