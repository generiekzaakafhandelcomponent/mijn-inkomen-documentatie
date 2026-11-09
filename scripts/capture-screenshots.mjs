import { chromium } from 'playwright';
import fs from 'node:fs';
const OUT='shots'; const BASE='http://localhost:4200';
const AB=`${BASE}/dossiers/aanvraag-algemene-bijstand-dcm`;
const log=[];
const b=await chromium.launch({channel:'chrome',headless:true});
const ctx=await b.newContext({viewport:{width:1600,height:1000},locale:'nl-NL',deviceScaleFactor:2});
const p=await ctx.newPage();
const shot=async(naam,opts={})=>{ await p.waitForTimeout(opts.wait??900);
  await p.screenshot({path:`${OUT}/${naam}.png`,fullPage:!!opts.full});
  log.push(naam); console.log('  ✓',naam); };

// ---------- 1. Inloggen ----------
await p.goto(BASE,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(2500);
if (p.url().includes('openid-connect')){
  await shot('01-inlogscherm',{wait:1200});
  await p.fill('#username','admin'); await p.fill('#password','admin');
  await p.click('#kc-login'); await p.waitForTimeout(6000);
}
await shot('02-dashboard',{wait:3000});

// ---------- 2. Navigatie ----------
await p.getByText('Dossiers',{exact:true}).first().click();
await shot('03-menu-dossiers',{wait:1600});

// ---------- 3. Zaaklijst ----------
await p.goto(AB,{waitUntil:'domcontentloaded'}); await p.waitForTimeout(5000);
await shot('04-zaaklijst-mijn');
const alle=p.getByText('Alle dossiers',{exact:true}).first();
if (await alle.count()){ await alle.click(); await shot('05-zaaklijst-alle',{wait:3500}); }
// zoekbalk openen
const zoek=p.locator('button:has-text("Zoeken"), [aria-label*="earch"], .cds--search input').first();
if (await zoek.count()){ await zoek.click().catch(()=>{}); await shot('06-zoeken',{wait:1500}); }

// ---------- 4. Dossier ----------
await p.locator('tbody tr').first().locator('td').nth(2).click();
await p.waitForTimeout(7000);
await shot('07-dossier-algemeen');

const TABS=['Brede Intake','Woonsituatie','Inkomen','Vermogen','Suwinet','Bewoning','Informatieverzoeken','Voortgang','Log','Documenten','Notities'];
for (const t of TABS){
  const el=p.getByRole('tab',{name:t}).or(p.getByText(t,{exact:true})).first();
  if (await el.count()){
    try { await el.click({timeout:4000}); await shot('08-tab-'+t.toLowerCase().replace(/\s+/g,'-'),{wait:2600}); }
    catch(e){ console.log('  – tab overgeslagen:',t); }
  }
}
// terug naar Algemeen
await p.getByText('Algemeen',{exact:true}).first().click().catch(()=>{});
await p.waitForTimeout(2000);

// ---------- 5. Taak ----------
const taak=p.getByText('Vaststellen persoon aanvrager').first();
if (await taak.count()){ await taak.click(); await shot('09-taak-formulier',{wait:5000}); }

// ---------- 6. Start-menu ----------
const start=p.getByRole('button',{name:/^Start/i}).first();
if (await start.count()){ await start.click(); await shot('10-startmenu',{wait:1800}); await p.keyboard.press('Escape'); }

fs.writeFileSync(`${OUT}/index.json`,JSON.stringify(log,null,1));
console.log('\nTotaal:',log.length,'screenshots');
await b.close();
