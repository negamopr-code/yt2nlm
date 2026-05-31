import { chromium } from 'playwright';
const browser = await chromium.launch({headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
const ctx = await browser.newContext();
const page = await ctx.newPage();
await page.goto('https://courses.glottos.com/fr/ru/lesson/classic50/1',{waitUntil:'domcontentloaded'});
await page.waitForTimeout(4000);
const info = await page.evaluate(()=>({
  localStorageKeys: Object.keys(localStorage),
  sessionStorageKeys: Object.keys(sessionStorage),
  cookieNames: document.cookie.split(';').map(c=>c.split('=')[0].trim()).filter(Boolean),
  hasFirebase: !!(window.firebase||[...document.scripts].some(s=>/firebase|gstatic.*identity|identitytoolkit/i.test(s.src))),
  authScripts: [...document.scripts].map(s=>s.src).filter(s=>/auth|firebase|supabase|clerk|google|identity|gsi/i.test(s)).slice(0,15),
  bodyHasGoogleBtn: /Google|anmelden|Войди|Sign in/i.test(document.body.innerText)
}));
console.log(JSON.stringify(info,null,2));
// also list IndexedDB databases (firebase uses these)
const dbs = await page.evaluate(async()=>{ try{ const l=await indexedDB.databases(); return l.map(d=>d.name);}catch(e){return ['(err)']} });
console.log('indexedDB:', JSON.stringify(dbs));
// cookies via context (captures httpOnly too)
const cks = await ctx.cookies('https://courses.glottos.com');
console.log('ctx cookies (logged-out):', JSON.stringify(cks.map(c=>({name:c.name,httpOnly:c.httpOnly,domain:c.domain})),null,2));
await browser.close();
