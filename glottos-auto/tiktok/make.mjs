// Build the vertical TikTok-style glottos mockup: render HTML animation (Playwright),
// synth voices (espeak-ng), synth SFX + beat bed (ffmpeg), mix + mux to mp4.
import { chromium } from 'playwright';
import { spawnSync } from 'node:child_process';
import { readdirSync, statSync, mkdirSync } from 'node:fs';
import { fileURLToPath } from 'node:url';
import path from 'node:path';
import ffmpegPath from 'ffmpeg-static';

const DIR = path.dirname(fileURLToPath(import.meta.url));
const WORK = path.join(DIR, 'work');
const OUT = path.join(DIR, '..', 'out');
mkdirSync(WORK, { recursive: true }); mkdirSync(OUT, { recursive: true });
const ESPEAK = '/usr/bin/espeak-ng';
const DUR = 25;          // seconds of animation
const LEAD = 0.45;       // audio lead to match video paint/start
const w = (f) => path.join(WORK, f);

function run(bin, args, label) {
  const r = spawnSync(bin, args, { encoding: 'utf8' });
  if (r.status !== 0) { console.error(`FAIL ${label}\n`, (r.stderr || r.stdout || '').slice(-800)); process.exit(1); }
  return r;
}
const ff = (args, label) => run(ffmpegPath, ['-hide_banner', '-loglevel', 'error', '-y', ...args], label);

// ---- 1. voices (espeak-ng) -------------------------------------------------
const VOICES = {
  vo_hook : { v:'ru', s:165, p:55, t:'Ты учил французский годами... и всё равно молчишь?' },
  npc1    : { v:'fr', s:160, p:78, t:'Bonjour, vous désirez ?' },
  wrong1  : { v:'fr', s:118, p:35, t:'Je veux café.' },
  right1  : { v:'fr', s:150, p:48, t:"Un café, s'il vous plaît." },
  npc2    : { v:'fr', s:160, p:78, t:'Où allez-vous ?' },
  wrong2  : { v:'fr', s:118, p:35, t:'À aéroport.' },
  right2  : { v:'fr', s:150, p:48, t:"À l'aéroport, s'il vous plaît." },
  npc3    : { v:'fr', s:160, p:78, t:'Vous parlez très bien !' },
  right3  : { v:'fr', s:150, p:48, t:'Merci, je pratique chaque jour.' },
  vo_fin  : { v:'ru', s:160, p:55, t:'Три из трёх. Ты заговорил. Глоттос.' },
};
for (const [k, o] of Object.entries(VOICES))
  run(ESPEAK, ['-v', o.v, '-s', String(o.s), '-p', String(o.p), '-a', '170', '-w', w(`${k}.wav`), o.t], `espeak ${k}`);

// ---- 2. SFX + beat bed (ffmpeg lavfi) --------------------------------------
ff(['-f','lavfi','-i','sine=frequency=988:duration=0.12','-f','lavfi','-i','sine=frequency=1319:duration=0.24',
    '-filter_complex','[0]afade=t=out:st=0.02:d=0.1[a];[1]afade=t=out:st=0.05:d=0.19[b];[a][b]concat=n=2:v=0:a=1,volume=0.9',
    '-ar','44100', w('ding.wav')], 'ding');
ff(['-f','lavfi','-i','sine=frequency=1319:duration=0.10','-f','lavfi','-i','sine=frequency=1976:duration=0.26',
    '-filter_complex','[0]afade=t=out:st=0.02:d=0.08[a];[1]afade=t=out:st=0.06:d=0.2[b];[a][b]concat=n=2:v=0:a=1,volume=0.85',
    '-ar','44100', w('ding2.wav')], 'ding2');
ff(['-f','lavfi','-i','sine=frequency=140:duration=0.28','-af','tremolo=f=26:d=0.85,afade=t=out:st=0.16:d=0.1,volume=0.9',
    '-ar','44100', w('buzz.wav')], 'buzz');
ff(['-f','lavfi','-i','anoisesrc=d=0.5:c=brown:a=0.6','-af','highpass=f=250,afade=t=in:st=0:d=0.12,afade=t=out:st=0.22:d=0.28,volume=0.55',
    '-ar','44100', w('whoosh.wav')], 'whoosh');
ff(['-f','lavfi','-i',`aevalsrc=exprs=0.9*sin(2*PI*55*t)*exp(-7*mod(t\\,0.5)):d=${DUR}:s=44100`,
    '-f','lavfi','-i',`aevalsrc=exprs=0.22*(random(0))*exp(-55*mod(t\\,0.25)):d=${DUR}:s=44100`,
    '-f','lavfi','-i',`aevalsrc=exprs=0.12*sin(2*PI*110*t):d=${DUR}:s=44100`,
    '-filter_complex','[0][1][2]amix=inputs=3:normalize=0,lowpass=f=5000,volume=0.6',
    '-ar','44100', w('bed.wav')], 'bed');

// ---- 3. audio timeline (seconds → mix) -------------------------------------
const EV = [
  [0.0 ,'vo_hook',1.0],
  [2.5 ,'whoosh', 0.5],[3.3,'whoosh',0.5],
  [3.9 ,'npc1',   1.0],
  [5.95,'wrong1', 1.0],[6.55,'buzz',0.6],
  [7.45,'right1', 1.0],[8.25,'ding',0.55],[8.85,'ding2',0.5],
  [9.9 ,'whoosh', 0.5],
  [10.3,'npc2',   1.0],
  [11.45,'wrong2',1.0],[12.05,'buzz',0.6],
  [12.85,'right2',1.0],[13.65,'ding',0.55],[14.15,'ding2',0.5],
  [15.2,'whoosh', 0.5],
  [15.6,'npc3',   1.0],
  [16.85,'right3',1.0],[17.85,'ding',0.55],[18.45,'ding2',0.5],
  [19.5,'vo_fin', 1.0],[22.5,'ding',0.5],
];
const srcOf = (k) => w(`${k}.wav`);
const inputs = ['-i', w('bed.wav')];
let fc = '[0:a]aformat=channel_layouts=stereo:sample_rates=44100,volume=0.16[m0];';
const labels = ['[m0]'];
EV.forEach(([t, k, vol], i) => {
  inputs.push('-i', srcOf(k));
  const ms = Math.round((t + LEAD) * 1000);
  const lab = `[m${i + 1}]`;
  fc += `[${i + 1}:a]aformat=channel_layouts=stereo:sample_rates=44100,volume=${vol},adelay=${ms}|${ms}${lab};`;
  labels.push(lab);
});
fc += `${labels.join('')}amix=inputs=${labels.length}:normalize=0:dropout_transition=0,volume=1.9,alimiter=limit=0.95[mix]`;
ff([...inputs, '-filter_complex', fc, '-map', '[mix]', '-t', String(DUR), '-ar', '44100', w('audio.wav')], 'mix');
console.log('audio.wav built');

// ---- 4. render the HTML animation (Playwright, 1080x1920) ------------------
const before = new Set(readdirSync(WORK).filter(f => f.endsWith('.webm')));
const browser = await chromium.launch();
const ctx = await browser.newContext({
  viewport: { width: 1080, height: 1920 }, deviceScaleFactor: 1,
  recordVideo: { dir: WORK, size: { width: 1080, height: 1920 } },
});
const page = await ctx.newPage();
await page.goto('file://' + path.join(DIR, 'scene.html'));
await page.waitForFunction('window.__ready === true');
await page.waitForTimeout(DUR * 1000 + 900);
await ctx.close(); await browser.close();
const webm = readdirSync(WORK).filter(f => f.endsWith('.webm') && !before.has(f))
  .map(f => ({ f, m: statSync(w(f)).mtimeMs })).sort((a, b) => b.m - a.m)[0].f;
console.log('rendered', webm);

// ---- 5. mux video + audio --------------------------------------------------
const finalOut = path.join(OUT, 'glottos_tiktok_ru_fr.mp4');
ff(['-i', w(webm), '-i', w('audio.wav'),
    '-map', '0:v:0', '-map', '1:a:0',
    '-c:v', 'libx264', '-crf', '20', '-preset', 'veryfast', '-pix_fmt', 'yuv420p', '-r', '30',
    '-c:a', 'aac', '-b:a', '160k', '-shortest', finalOut], 'mux');
console.log('DONE →', finalOut);
