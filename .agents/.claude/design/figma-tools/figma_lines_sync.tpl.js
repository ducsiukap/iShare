const page = await figma.getNodeByIdAsync("__PID__");
await figma.setCurrentPageAsync(page);
const T = __T__;
const D = __DATA__;
const norm = s => s.replace(/\s+/g, " ").trim();
const loaded = new Set(); const fixed = [], ambiguous = [], unresolved = [];
const lines = (t) => { const lh = t.lineHeight; if (lh === figma.mixed) return null; const fs = t.fontSize === figma.mixed ? 16 : t.fontSize; const px = lh.unit === "PIXELS" ? lh.value : lh.unit === "PERCENT" ? fs * lh.value / 100 : fs * 1.2; return Math.round(t.height / px); };
for (const f of page.children) {
  const E = D[f.name]; if (f.type !== "FRAME" || !E) continue;
  const by = {}; for (const [i, L, wr, we] of E) (by[T[i]] = by[T[i]] || []).push([L, wr, we]);
  const groups = {};
  for (const t of f.findAllWithCriteria({ types: ["TEXT"] })) { if (t.characters.includes("\n")) continue; const k = norm(t.characters); if (by[k]) (groups[k] = groups[k] || []).push(t); }
  for (const k in groups) {
    const g = groups[k], b = by[k];
    const same = b.every(x => x[0] === b[0][0] && Math.abs(x[1] - b[0][1]) < 1);
    if (g.length > b.length || (!same && g.length !== b.length)) { ambiguous.push([f.name, k.slice(0, 30), g.length, b.length]); continue; }
    for (let i = 0; i < g.length; i++) {
      const t = g[i]; const [L, wr, we] = same ? b[0] : b[i];
      const l0 = lines(t); if (l0 === null || l0 === L) continue;
      for (const fn of t.getRangeAllFontNames(0, t.characters.length)) { const key = fn.family + "|" + fn.style; if (!loaded.has(key)) { await figma.loadFontAsync(fn); loaded.add(key); } }
      const p = t.parent; const inAL = p.layoutMode && p.layoutMode !== "NONE" && t.layoutPositioning !== "ABSOLUTE";
      const before = [lines(t), Math.round(t.width)];
      if (inAL) t.layoutSizingHorizontal = "FIXED";
      let w = Math.round(we * 10) / 10; t.resize(w, t.height); t.textAutoResize = "HEIGHT";
      if (lines(t) > L) { while (lines(t) > L && w < we * 1.04) { w += 1; t.resize(w, t.height); t.textAutoResize = "HEIGHT"; } }
      else if (lines(t) < L) { while (lines(t) < L && w > wr) { w -= 1; t.resize(w, t.height); t.textAutoResize = "HEIGHT"; } }
      if (lines(t) !== L) unresolved.push([f.name, k.slice(0, 30), "want", L, "got", lines(t), Math.round(w), we]);
      fixed.push([f.name.replace(/--desktop/, ""), k.slice(0, 24), before, [lines(t), Math.round(t.width)]]);
    }
  }
}
return { fixed: fixed.length, sample: fixed.slice(0, 25), ambiguous: ambiguous.slice(0, 15), nAmb: ambiguous.length, unresolved };
