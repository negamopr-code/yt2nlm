import { chromium } from 'playwright';
const browser = await chromium.launch({headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--use-fake-ui-for-media-stream','--use-fake-device-for-media-stream']});
const ctx = await browser.newContext({viewport:{width:1366,height:900},permissions:['microphone']});
const page = await ctx.newPage();
await page.addInitScript(()=>{ window.__mic=false; const md=navigator.mediaDevices; if(md&&md.getUserMedia){const g=md.getUserMedia.bind(md); md.getUserMedia=(...a)=>{window.__mic=true;return g(...a);};}});
await page.goto('https://courses.glottos.com/fr/ru/lesson/classic50/1',{waitUntil:'domcontentloaded'});
await page.waitForTimeout(4000);
async function tryClick(rx,label){ try{ await page.getByRole('button',{name:rx}).first().click({timeout:4000}); console.log('clicked',label); }
  catch(e){ try{ await page.getByText(rx).first().click({timeout:3000}); console.log('clicked(text)',label);}catch(e2){console.log('miss',label);} }
  await page.waitForTimeout(2500); }
// try opening the locked audio-practice tab
await tryClick(/Аудио-практика/,'audio-practice');
await page.screenshot({path:'shots/audio-tab.png'});
let after = await page.evaluate(()=>({ url:location.href, mic:window.__mic,
  signinPrompt:/войд|sign in|анмельд|зарегистр|разблок|подписк|премиум|оплат/i.test(document.body.innerText),
  visibleText:document.body.innerText.replace(/\n{2,}/g,'\n').slice(0,1200) }));
console.log('AFTER AUDIO CLICK:', JSON.stringify(after,null,2));
// also try "Выучи слова"
await tryClick(/Выучи слова/,'learn-words');
await page.screenshot({path:'shots/words-tab.png'});
let w = await page.evaluate(()=>document.body.innerText.replace(/\n{2,}/g,'\n').slice(0,900));
console.log('WORDS TAB TEXT:', JSON.stringify(w));
await browser.close();
