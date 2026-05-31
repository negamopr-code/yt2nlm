import { chromium } from 'playwright';
const browser = await chromium.launch({ headless:true, args:['--no-sandbox','--disable-dev-shm-usage'] });
const page = await browser.newPage({ viewport:{width:1366,height:900} });
try {
  await page.goto('https://courses.glottos.com/', { waitUntil:'domcontentloaded', timeout:60000 });
  await page.waitForTimeout(4000);
} catch(e){ console.log('nav warn:', e.message.slice(0,120)); }
await page.screenshot({ path:'shots/home.png', fullPage:true });
const info = await page.evaluate(()=>({
  title: document.title, url: location.href,
  headings: [...document.querySelectorAll('h1,h2,h3,h4')].map(e=>e.innerText.trim()).filter(Boolean).slice(0,40),
  links: [...document.querySelectorAll('a')].map(a=>({t:a.innerText.trim().slice(0,45), href:a.href})).filter(l=>l.t).slice(0,70),
  buttons: [...document.querySelectorAll('button,[role=button]')].map(b=>b.innerText.trim()).filter(Boolean).slice(0,40),
  hasVideo: !!document.querySelector('video'), hasAudio: !!document.querySelector('audio'),
  bodyText: document.body.innerText.slice(0,800)
}));
console.log(JSON.stringify(info,null,2));
await browser.close();
