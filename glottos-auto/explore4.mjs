import { chromium } from 'playwright';
const browser = await chromium.launch({headless:true,args:['--no-sandbox','--disable-dev-shm-usage','--use-fake-ui-for-media-stream','--use-fake-device-for-media-stream']});
const ctx = await browser.newContext({viewport:{width:1366,height:900},permissions:['microphone']});
const page = await ctx.newPage();
await page.addInitScript(()=>{ window.__mic=false; const md=navigator.mediaDevices; if(md&&md.getUserMedia){const g=md.getUserMedia.bind(md); md.getUserMedia=(...a)=>{window.__mic=true;return g(...a);};}
  window.__spoke=[]; if(window.speechSynthesis){const s=speechSynthesis.speak.bind(speechSynthesis); speechSynthesis.speak=u=>{try{window.__spoke.push(u.text)}catch(e){} return s(u);};}
  const SR=window.SpeechRecognition||window.webkitSpeechRecognition; window.__sr=!!SR; });
await page.goto('https://courses.glottos.com/fr/ru/lesson/classic50/1',{waitUntil:'domcontentloaded'});
await page.waitForTimeout(6000);
await page.screenshot({path:'shots/lesson-step.png'});
const L = await page.evaluate(()=>({
  url:location.href,
  buttons:[...document.querySelectorAll('button,[role=button]')].map(b=>b.innerText.trim().replace(/\s+/g,' ')).filter(Boolean).slice(0,40),
  micUsed:window.__mic, srAvailable:window.__sr, spoke:(window.__spoke||[]).slice(0,10),
  hasAudio:!!document.querySelector('audio'),
  bodyText:document.body.innerText.replace(/\n{2,}/g,'\n').slice(0,2000)
}));
console.log(JSON.stringify(L,null,2));
await browser.close();
