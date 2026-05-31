import { chromium } from 'playwright';
const browser = await chromium.launch({headless:true,args:['--no-sandbox','--disable-dev-shm-usage']});
const ctx = await browser.newContext({viewport:{width:1366,height:900},permissions:['microphone']});
const page = await ctx.newPage();
await page.goto('https://courses.glottos.com/fr/ru/classic50',{waitUntil:'domcontentloaded'});
await page.waitForTimeout(3000);
const links = await page.evaluate(()=>[...document.querySelectorAll('a')].map(a=>({t:a.innerText.trim().replace(/\s+/g,' ').slice(0,45),href:a.href})));
console.log('ALL LINKS:', JSON.stringify(links.filter(l=>/classic50|урок|lesson|введ/i.test(l.t+l.href)).slice(0,25),null,2));
let l1 = links.find(l=>/урок 1\b|lesson 1\b|введ/i.test(l.t)) || links.find(l=>/classic50\/(1|lesson)/i.test(l.href)) || links.find(l=>l.href.match(/classic50\/\w/));
if(l1){ console.log('-> opening', l1.href); await page.goto(l1.href,{waitUntil:'domcontentloaded'}); await page.waitForTimeout(4500);}
else console.log('no lesson link found, staying on syllabus');
await page.screenshot({path:'shots/lesson1-ui.png',fullPage:false});
const L = await page.evaluate(()=>({
  url:location.href, title:document.title,
  buttons:[...document.querySelectorAll('button,[role=button]')].map(b=>b.innerText.trim().replace(/\s+/g,' ')).filter(Boolean).slice(0,60),
  inputs:[...document.querySelectorAll('input,textarea')].map(i=>i.type||i.tagName),
  micWords:/(микрофон|🎤|запис|произнес|скажи|повтори|listen|record|вслух)/i.test(document.body.innerText),
  speechSynth:'speechSynthesis' in window,
  bodyText:document.body.innerText.slice(0,1600)
}));
console.log('LESSON1 UI:', JSON.stringify(L,null,2));
await browser.close();
