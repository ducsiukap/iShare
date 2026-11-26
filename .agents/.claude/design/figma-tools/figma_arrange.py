import json, sys
batch = sys.argv[1].lower(); page = sys.argv[2]
names = json.load(open("/tmp/scr_names.json", encoding="utf-8"))
heights = json.load(open("qa/heights_%s.json" % batch))
scrs = []
for k in heights:
    s = k.split("--")[0]
    if s not in scrs: scrs.append(s)
lab = {s: "%s · %s" % (s, names.get(s, "")) for s in scrs}
code = r'''const page = await figma.getNodeByIdAsync("%s");
if (!page || page.type !== "PAGE") return { pageNotFound: "%s" };
await figma.setCurrentPageAsync(page);
const ORDER = %s;
const LABEL = %s;
await figma.loadFontAsync({ family: "Be Vietnam Pro", style: "SemiBold" });
for (const n of [...page.children]) { if (n.type === "TEXT" && n.name.startsWith("Nhãn · ")) n.remove(); }
const frames = page.children.filter(n => n.type === "FRAME");
const renamed = [];
for (const f of frames) { const m = f.name.match(/^Section - (SCR-\S+?) \(iShare/); if (m) { f.name = m[1]; renamed.push(f.id); } }
const byScr = {};
for (const f of frames) { const s = f.name.split("--")[0]; (byScr[s] = byScr[s] || []).push(f); }
const order = (n) => { const st = n.split("--")[1]; const dark = n.endsWith("--dark"); return st === "default" ? (dark ? 1 : 0) : 2; };
let y = 0; const labels = []; const missing = [];
for (const s of ORDER) {
  const row = byScr[s]; if (!row) { missing.push(s); continue; }
  row.sort((a, b) => order(a.name) - order(b.name));
  const t = figma.createText(); t.fontName = { family: "Be Vietnam Pro", style: "SemiBold" }; t.fontSize = 48; t.characters = LABEL[s]; t.name = "Nhãn · " + s;
  page.appendChild(t); t.x = 0; t.y = y; labels.push(t.id);
  let x = 0, h = 0; y += 96;
  for (const f of row) { f.x = x; f.y = y; x += f.width + 80; h = Math.max(h, f.height); }
  y += h + 240;
}
return { frames: frames.length, renamed: renamed.length, labels: labels.length, missing, height: y };''' % (page, page, json.dumps(scrs), json.dumps(lab, ensure_ascii=False))
open("/tmp/arrange_%s.js" % batch, "w", encoding="utf-8").write(code)
print(len(code))
