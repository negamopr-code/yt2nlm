import { chromium } from 'playwright';
const browser = await chromium.launch({ headless:true, args:['--no-sandbox','--disable-dev-shm-usage'] });
const ctx = await browser.newContext({ viewport:{width:1366,height:900}, permissions:['microphone'] });
const page = await ctx.newPage();
await page.goto('https://courses.glottos.com/', { waitUntil:'domcontentloaded' });
await page.waitForTimeout(2500);
async function clk(rx,label){ try{ await page.getByText(rx).first().click({timeout:5000}); console.log('clicked',label);}catch(e){console.log('miss',label,e.message.slice(0,60));} }
await clk(/Русский/,'I-speak-RU'); await page.waitForTimeout(800);
await clk(/Français/,'learn-FR'); await page.waitForTimeout(1500);
await page.screenshot({ path:'shots/courses-fr.png', fullPage:true });
const courses = await page.evaluate(()=>[...document.querySelectorAll('a')].map(a=>({t:a.innerText.trim().slice(0,55),href:a.href})).filter(l=>l.t));
console.log('LINKS after FR:', JSON.stringify(courses,null,2));
let target = (courses.find(c=>/lesson|classic|урок|start|cours/i.test(c.t+c.href))||courses[0]);
if(target){ console.log('-> opening',target.href); await page.goto(target.href,{waitUntil:'domcontentloaded'}); await page.waitForTimeout(4000); }
await page.screenshot({ path:'shots/lesson1.png', fullPage:true });
const lesson = await page.evaluate(()=>({
  url:location.href, title:document.title,
  headings:[...document.querySelectorAll('h1,h2,h3')].map(e=>e.innerText.trim()).filter(Boolean).slice(0,20),
  buttons:[...document.querySelectorAll('button,[role=button]')].map(b=>b.innerText.trim()).filter(Boolean).slice(0,50),
  micWords:/(microphone|микрофон|🎤|record|запис|listen|слуша)/i.test(document.body.innerText),
  hasAudio:!!document.querySelector('audio'), hasVideo:!!document.querySelector('video'),
  bodyText:document.body.innerText.slice(0,1400)
}));
console.log('LESSON:', JSON.stringify(lesson,null,2));
await browser.close();
