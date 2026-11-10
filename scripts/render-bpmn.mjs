// Rendert het BPMN-model van elke business service naar SVG.
//
// Bron:    config/building-block/bs-*/<versie>/bpmn/*.bpmn in de backend
// Uitvoer: .gitbook/assets/bpmn/<key>.svg
//
// Draaien (vanuit de root van deze repo):
//     npm install bpmn-js playwright
//     node scripts/render-bpmn.mjs [pad-naar-backend]
//
// Zonder argument wordt ../mijn-inkomen-gzac-backend-v13 geprobeerd.

import { chromium } from 'playwright';
import fs from 'node:fs';
import path from 'node:path';
import os from 'node:os';

const DOCS = path.dirname(path.dirname(new URL(import.meta.url).pathname));
const BACKEND = path.join(
  process.argv[2] || path.join(path.dirname(DOCS), 'mijn-inkomen-gzac-backend-v13'),
  'src/main/resources/config/building-block'
);
const UIT = path.join(DOCS, '.gitbook/assets/bpmn');

if (!fs.existsSync(BACKEND)) {
  console.error(`Bouwblokken niet gevonden: ${BACKEND}`);
  process.exit(1);
}

// bpmn-js heeft een DOM nodig; we renderen daarom in een echte browser.
const bpmnDist = path.join(DOCS, 'node_modules/bpmn-js/dist');
if (!fs.existsSync(bpmnDist)) {
  console.error('bpmn-js niet gevonden. Draai eerst: npm install bpmn-js playwright');
  process.exit(1);
}

const html = `<!doctype html><html><head><meta charset="utf-8">
<link rel="stylesheet" href="${bpmnDist}/assets/bpmn-js.css">
<link rel="stylesheet" href="${bpmnDist}/assets/diagram-js.css">
<link rel="stylesheet" href="${bpmnDist}/assets/bpmn-font/css/bpmn-embedded.css">
<style>html,body{margin:0;background:#fff}#c{width:1600px;height:1000px}</style>
</head><body><div id="c"></div>
<script src="${bpmnDist}/bpmn-viewer.production.min.js"></script>
<script>
  window.viewer = new BpmnJS({ container: '#c' });
  window.renderBpmn = async function (xml) {
    await window.viewer.importXML(xml);
    window.viewer.get('canvas').zoom('fit-viewport', 'auto');
    const { svg } = await window.viewer.saveSVG();
    return svg;
  };
</script></body></html>`;

const tmp = path.join(os.tmpdir(), `bpmn-render-${process.pid}.html`);
fs.writeFileSync(tmp, html);

/** Zet een witte achtergrond onder het diagram.
 *  Zonder deze blijft de SVG transparant en is zwart lijnwerk
 *  onleesbaar in het donkere thema van GitBook. */
function metAchtergrond(svg) {
  return svg.replace(
    /(<svg[^>]*>)/,
    '$1<rect x="-100000" y="-100000" width="200000" height="200000" fill="#ffffff"/>'
  );
}

fs.mkdirSync(UIT, { recursive: true });

const blokken = fs.readdirSync(BACKEND).filter((d) => d.startsWith('bs-')).sort();
const browser = await chromium.launch({ channel: 'chrome', headless: true });
const page = await browser.newPage({ viewport: { width: 1600, height: 1000 } });
await page.goto('file://' + tmp);
await page.waitForFunction(() => typeof window.renderBpmn === 'function');

let ok = 0;
const overgeslagen = [];

for (const blok of blokken) {
  let bpmn = null;
  for (const versie of fs.readdirSync(path.join(BACKEND, blok))) {
    const dir = path.join(BACKEND, blok, versie, 'bpmn');
    if (!fs.existsSync(dir)) continue;
    const f = fs.readdirSync(dir).find((x) => x.endsWith('.bpmn'));
    if (f) bpmn = path.join(dir, f);
  }
  if (!bpmn) {
    overgeslagen.push(`${blok} (geen bpmn)`);
    continue;
  }
  try {
    const xml = fs.readFileSync(bpmn, 'utf8');
    const svg = await page.evaluate((x) => window.renderBpmn(x), xml);
    fs.writeFileSync(path.join(UIT, `${blok}.svg`), metAchtergrond(svg));
    ok++;
    console.log(`  ✓ ${blok} (${Math.round(svg.length / 1024)} kB)`);
  } catch (e) {
    overgeslagen.push(`${blok}: ${String(e.message).split('\n')[0].slice(0, 60)}`);
  }
}

await browser.close();
fs.unlinkSync(tmp);

console.log(`\n${ok} diagrammen gerenderd naar ${path.relative(DOCS, UIT)}/`);
if (overgeslagen.length) {
  console.log(`${overgeslagen.length} overgeslagen:`);
  overgeslagen.forEach((o) => console.log(`  – ${o}`));
}
