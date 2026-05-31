import { chromium } from 'playwright';
const W=1280,H=720;
const browser = await chromium.launch({headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
const ctx = await browser.newContext({viewport:{width:W,height:H}, recordVideo:{dir:'out', size:{width:W,height:H}}});
const page = await ctx.newPage();
const wait=ms=>page.waitForTimeout(ms);
async function caption(text, sub=''){ await page.evaluate(({text,sub})=>{
  let o=document.getElementById('__cap');
  if(!o){o=document.createElement('div');o.id='__cap';document.body.appendChild(o);
    o.style.cssText='position:fixed;left:0;right:0;bottom:0;z-index:999999;padding:30px 36px;'+
    'background:linear-gradient(0deg,#000e 30%,#0000);color:#fff;font-family:system-ui,sans-serif;'+
    'text-align:center;transition:opacity .45s;opacity:0';}
  o.innerHTML='<div style="font-size:32px;font-weight:800;line-height:1.2">'+text+'</div>'+
    (sub?'<div style="font-size:19px;font-weight:500;opacity:.9;margin-top:8px">'+sub+'</div>':'');
  requestAnimationFrame(()=>o.style.opacity='1');
},{text,sub}); }
async function hideCap(){ await page.evaluate(()=>{const o=document.getElementById('__cap'); if(o)o.style.opacity='0';}); await wait(450);}

try{
// 1 — HOOK
await page.goto('https://courses.glottos.com/',{waitUntil:'domcontentloaded'}); await wait(2500);
await caption('Учил французский — а читать и говорить не можешь?','Правила в голове ≠ речь во рту'); await wait(3800);
// 2 — pick RU -> FR
await hideCap();
await page.getByText(/Русский/).first().click({timeout:5000}).catch(()=>{}); await wait(800);
await page.getByText(/Français/).first().click({timeout:5000}).catch(()=>{}); await wait(1600);
await caption('Glottos: язык — это спорт, а не зубрёжка'); await wait(2600);
// 3 — lesson theory, 5/95 message
await hideCap();
await page.goto('https://courses.glottos.com/fr/ru/lesson/classic50/1',{waitUntil:'domcontentloaded'}); await wait(3000);
await page.getByText(/Натренировать рот/).first().scrollIntoViewIfNeeded({timeout:5000}).catch(()=>{}); await wait(900);
await caption('Знать правило = 5%. Натренировать рот = 95%.','Поэтому Glottos — про говорение, а не таблицы'); await wait(3800);
// 4 — reading rules
await hideCap();
await page.getByText(/Главное правило/).first().scrollIntoViewIfNeeded({timeout:5000}).catch(()=>{}); await wait(800);
for(let i=0;i<5;i++){ await page.mouse.wheel(0,240); await wait(750); }
await caption('10 правил чтения покрывают 90% французского','«Paris» → «пари» — уже с первого урока'); await wait(3800);
// 5 — CTA
await hideCap();
await caption('Открой первый урок бесплатно','courses.glottos.com'); await wait(3200);
}catch(e){ console.log('director warn:', e.message.slice(0,140)); }
await ctx.close(); await browser.close();
console.log('done');
