// glottos marketing-strategy assistant — serves the chat UI + answers each
// message via a headless `claude -p` agent (subscription auth, /root/.claude).
// One continuous conversation, persisted (session id + full transcript to disk).
import http from 'node:http';
import { spawn } from 'node:child_process';
import { readFile, writeFile } from 'node:fs/promises';
import { existsSync, readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const DIR = path.dirname(fileURLToPath(import.meta.url));
const PORT = process.env.PORT || 8097;
const WORKDIR = process.env.CLAUDE_CWD || '/workspace/glottos-marketing';
const SESS_FILE = path.join(DIR, '.session');
const STATE_DIR = path.join(DIR, 'state');
const TRANSCRIPT_FILE = path.join(STATE_DIR, 'transcript.json');

const SYS = [
  'You are the GROWTH / MARKETING STRATEGIST for "glottos", an online language course (courses.glottos.com), reachable as a web chat at http://localhost:8097/. The user asks questions and you give concrete, actionable marketing strategy.',
  'Save artifacts you produce (plans, ad scripts, hook lists, funnels) into /workspace/glottos-marketing/state/ so everything is kept on this page.',
  'PRODUCT: online self-study language course. First market = RU->FR (Russian speakers learning French), program "classic50", URL pattern /{fr}/{ru}/lesson/classic50/{N}. Tabs: Theory + Memo (free, no login); Words / Exercises / AUDIO-PRACTICE (the speaking drill) behind a free Google login.',
  'THE CORE INSIGHT (from real customer-comment data): pain #1 = "I understand but cannot speak" (RU "понимаю, но не говорю") — rules in the head != speech in the mouth; no speaking practice, no conversation partner, fear of speaking, ~5% actually speak vs 95% who do not. Anchor positioning to THIS pain.',
  'ESTABLISHED DOCTRINE (reuse, build on): (1) "speaking = leveling up" — gamify output, every spoken line is XP/level-up. (2) "advertising without advertising" — the product solving the exact pain is always on screen; record the real tool, no talking-head. (3) The AI conversation partner is BOTH the demo-generator AND a sellable product feature — show in the ad exactly the feature you sell (practice speaking with no partner, no fear). (4) $0 production: screen-record Chrome demo -> vertical TikTok/Reels/Shorts, OBS + CapCut.',
  'EXISTING ASSETS you can reference/critique: glottos-shell playable demo at http://localhost:8092 ("speaking=level" game, /workspace/glottos-shell); a 9:16 TikTok mockup + real-glottos screen-recorded ads in /workspace/glottos-auto; customer-comment pain analytics live under /workspace (yt2nlm / customer-comments — read for voice-of-customer phrasing).',
  'NOTEBOOKLM KNOWLEDGE BASE (connected 2026-09-27): notebook "Glottos — go-to-market", id 8306c0a9-1418-41e2-a988-1c0459eafc89, Google account drawnformula@gmail.com (profile drawnformula; env NLM_PROFILE=drawnformula is set). It holds: the 10 GTM strategy docs from state/, the VERBATIM learner-pain corpus (~30k YouTube comments + 41 transcripts from 59 language-learning videos, packed text volumes titled "Glottos learners — ..."), and per-problem competitor evidence documents titled "PROBLEM NN — <pain>" (competitor videos with views/likes/comments/engagement + their transcripts). CLI: N=/workspace/glottos-marketing/.nlmvenv/bin/nlm. Ask: $N notebook query 8306c0a9-1418-41e2-a988-1c0459eafc89 "<question>" --profile drawnformula --json and use only .value.answer (the JSON is huge). Queries cost the account\'s NotebookLM quota (~50/day), so ask FEW, big, precise questions; listing and reading sources is free ($N source list <nb> --profile drawnformula ; $N source content <source-id> --profile drawnformula). Studio artifacts: $N infographic create / slides create / data-table create / audio create / report create <nb> --profile drawnformula, then $N download ... — use them as raw material and re-brand/re-format them with your own scripts (logo, palette, 9:16), never publish them raw. RULES: you may ADD text sources for new findings, titled with the problem they address (e.g. "PROBLEM 01 — ..."); YouTube links are never kept as sources (method = add link, read its transcript with source content, delete that temporary source, keep the text); only delete sources you added yourself and only temporary ones; never create or delete notebooks; never touch other notebooks or other accounts.',
  'BEHAVE AS A STRATEGIST: be concrete and prioritized. When relevant give hooks/scripts (with the exact RU on-screen text), channel & funnel plans, positioning angles, A/B ideas, target segments, offer/pricing thoughts, and KPIs — not vague advice. Use the customers\' own words. You may read /workspace files and WebSearch for competitor/market/trend research. Ask a sharp clarifying question only when it changes the answer; otherwise give your best concrete recommendation and note assumptions. End substantive turns with a crisp next step.'
].join(' ');

let sessionId = existsSync(SESS_FILE) ? readFileSync(SESS_FILE, 'utf8').trim() || null : null;
let transcript = existsSync(TRANSCRIPT_FILE) ? JSON.parse(readFileSync(TRANSCRIPT_FILE, 'utf8')) : [];
let chain = Promise.resolve(); // serialize so --resume stays consistent

async function saveTranscript() {
  try { await writeFile(TRANSCRIPT_FILE, JSON.stringify(transcript, null, 1)); } catch {}
}

// Seed for a fresh session when the stored one is gone (Claude Code auto-deletes
// session transcripts after cleanupPeriodDays, default 30) — replays recent turns.
function contextSeed() {
  const turns = [];
  for (let i = 0; i + 1 < transcript.length; i += 2) {
    const a = transcript[i + 1];
    if (a && !String(a.text).startsWith('[backend error]')) turns.push(transcript[i], a);
  }
  let out = '';
  for (let i = turns.length - 1; i >= 0 && out.length < 30000; i--)
    out = `${turns[i].role.toUpperCase()}: ${String(turns[i].text).slice(0, 4000)}\n\n` + out;
  return out ? `[Earlier conversation from this page, restored after the original session expired — continue from it; artifacts are in state/]\n\n${out}---\nNEW MESSAGE:\n` : '';
}

async function runClaude(message) {
  const r = await runClaudeOnce(message);
  if (!r.ok && sessionId && /No conversation found with session ID/.test(r.reply)) {
    sessionId = null;
    try { await writeFile(SESS_FILE, ''); } catch {}
    return runClaudeOnce(contextSeed() + message);
  }
  return r;
}

function runClaudeOnce(message) {
  return new Promise((resolve) => {
    const args = ['-p', message, '--output-format', 'json', '--dangerously-skip-permissions', '--append-system-prompt', SYS];
    if (sessionId) args.push('--resume', sessionId);
    const child = spawn('claude', args, { cwd: WORKDIR, env: process.env, stdio: ['ignore', 'pipe', 'pipe'] });
    let out = '', err = '';
    child.stdout.on('data', d => out += d);
    child.stderr.on('data', d => err += d);
    const killer = setTimeout(() => child.kill('SIGKILL'), 600000);
    child.on('close', async (code) => {
      clearTimeout(killer);
      try {
        const j = JSON.parse(out);
        if (j.session_id) { sessionId = j.session_id; await writeFile(SESS_FILE, sessionId); }
        resolve({ ok: !j.is_error, reply: j.result ?? '(empty)' });
      } catch {
        resolve({ ok: false, reply: `[backend error] exit=${code}\n${err || out || 'no output'}`.slice(0, 4000) });
      }
    });
  });
}

const server = http.createServer(async (req, res) => {
  if (req.method === 'GET' && (req.url === '/' || req.url === '/index.html')) {
    const html = await readFile(path.join(DIR, 'chat.html'), 'utf8');
    res.writeHead(200, { 'content-type': 'text/html; charset=utf-8' });
    return res.end(html);
  }
  if (req.method === 'GET' && req.url === '/history') {
    res.writeHead(200, { 'content-type': 'application/json' });
    return res.end(JSON.stringify({ transcript }));
  }
  if (req.method === 'POST' && req.url === '/reset') {
    sessionId = null; transcript = [];
    try { await writeFile(SESS_FILE, ''); } catch {}
    await saveTranscript();
    res.writeHead(200, { 'content-type': 'application/json' });
    return res.end(JSON.stringify({ ok: true }));
  }
  if (req.method === 'POST' && req.url === '/chat') {
    let body = '';
    req.on('data', c => body += c);
    req.on('end', () => {
      let message = '';
      try { message = (JSON.parse(body).message || '').trim(); } catch {}
      if (!message) { res.writeHead(400); return res.end(JSON.stringify({ ok: false, reply: 'empty message' })); }
      chain = chain.then(() => runClaude(message)).then(async (result) => {
        transcript.push({ role: 'user', text: message }, { role: 'assistant', text: result.reply });
        await saveTranscript();
        res.writeHead(200, { 'content-type': 'application/json' });
        res.end(JSON.stringify({ ...result, session_id: sessionId }));
      }).catch((e) => {
        res.writeHead(500, { 'content-type': 'application/json' });
        res.end(JSON.stringify({ ok: false, reply: String(e) }));
      });
    });
    return;
  }
  // static artifacts: GET /state/<file> (download/preview anything saved to state/)
  if (req.method === 'GET' && req.url.startsWith('/state/')) {
    const name = path.basename(decodeURIComponent(req.url.slice('/state/'.length).split('?')[0]));
    const fp = path.join(STATE_DIR, name);
    if (name && existsSync(fp)) {
      const ext = path.extname(name).toLowerCase();
      const types = { '.png':'image/png', '.jpg':'image/jpeg', '.jpeg':'image/jpeg', '.svg':'image/svg+xml',
        '.gif':'image/gif', '.webp':'image/webp', '.mp4':'video/mp4', '.pdf':'application/pdf',
        '.md':'text/markdown; charset=utf-8', '.json':'application/json', '.txt':'text/plain; charset=utf-8' };
      const buf = await readFile(fp);
      res.writeHead(200, { 'content-type': types[ext] || 'application/octet-stream', 'cache-control':'no-cache' });
      return res.end(buf);
    }
    res.writeHead(404); return res.end('not found');
  }
  res.writeHead(404); res.end('not found');
});

server.listen(PORT, '0.0.0.0', () => console.log(`glottos-marketing chat on :${PORT} (cwd=${WORKDIR}, session=${sessionId || 'new'})`));
