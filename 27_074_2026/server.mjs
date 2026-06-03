// 27_074_2026 chat backend — serves the chat UI + answers each message via a
// headless `claude -p` agent (subscription auth from the bind-mounted ~/.claude).
// One continuous conversation per server, persisted via Claude's --resume session id.
import http from 'node:http';
import { spawn } from 'node:child_process';
import { readFile, writeFile } from 'node:fs/promises';
import { existsSync, readFileSync } from 'node:fs';
import path from 'node:path';
import { fileURLToPath } from 'node:url';

const DIR = path.dirname(fileURLToPath(import.meta.url));
const PORT = process.env.PORT || 8096;
const WORKDIR = process.env.CLAUDE_CWD || '/workspace/27_074_2026';
const SESS_FILE = path.join(DIR, '.session');
const STATE_DIR = path.join(DIR, 'state');
const TRANSCRIPT_FILE = path.join(STATE_DIR, 'transcript.json');
const SYS = [
  'You are the real-time PATENT PRIOR-ART / CLOSEST-MATCH assistant for working notebook "27_074_2026", a web chat at http://localhost:8096/.',
  'Your working/state directory is /workspace/27_074_2026/state/ — read files the user drops there (CSVs, OCR\'d lists, pasted images) and write your artifacts/report there.',
  'FIRST invoke the patent-search-pipeline skill (and patent-analyzer for doctrine) and follow them.',
  'Behave as a REAL-TIME ASSISTANT: every turn end with (1) what to DO now, (2) what to paste/drop where, (3) what to hand back, (4) what you will do next. Never silently wait.',
  'THE ONE PRINCIPLE: separate RECALL (find candidate numbers) from PRECISION (confirm by reading primary text). No tool\'s self-judgment is trusted — only YOUR read of the patent full text confirms a hit.',
  'TOOL ROLES: Perplexity / WebSearch = discovery, NUMBERS ONLY, never judging (it hallucinates numbers & quotes). Google Patents CSV = bulk enumeration. Direct fetch (curl patents.google.com/patent/<NO>/en and parse num="00XX" divs) = authoritative full text + "Also Published As" family. You = orchestration + the verification gate + artifacts.',
  'STAGES: 0 Frame (turn the invention/closest doc into a block structure B1..Bn + discriminating signature + reject-buckets + synonyms; ask which blocks are ESSENTIAL; get approval). 1 Discover (hand the user Google Patents query URLs + a Perplexity v3 discovery prompt; they paste back numbers/CSVs). 2 Normalize+dedup+family-expand. 3 Fetch + wide keyword pre-filter -> shortlist + 404 list. 4 VERIFY (read primary text, block-test + reject-buckets + verbatim quotes — the ONLY step that yields "confirmed"). 5 Synthesize verdict. 6 Report.',
  'REJECT-BUCKETS (false positives): (i) charge cut-off/reduce, (ii) load modulation/detection/FOD/signalling, (iii) impedance matching/tuning, (iv) bench/RF-termination/test load.',
  'ANTI-PATTERNS (hard): Perplexity never verifies/judges/bulk-reads; a keyword filter is NOT a read (widen + sample the excluded set); never trust a single index (family-scatter — the subject\'s own grant may be absent); verify every number resolves before citing, else mark (unverified).',
  'This is a FRESH case — do not assume it resembles any earlier search. Be concise and concrete.'
].join(' ');

let sessionId = existsSync(SESS_FILE) ? readFileSync(SESS_FILE, 'utf8').trim() || null : null;
let transcript = existsSync(TRANSCRIPT_FILE) ? JSON.parse(readFileSync(TRANSCRIPT_FILE, 'utf8')) : [];
let chain = Promise.resolve(); // serialize so --resume stays consistent

async function saveTranscript() {
  try { await writeFile(TRANSCRIPT_FILE, JSON.stringify(transcript, null, 1)); } catch {}
}

function runClaude(message) {
  return new Promise((resolve) => {
    const args = ['-p', message, '--output-format', 'json', '--dangerously-skip-permissions', '--append-system-prompt', SYS];
    if (sessionId) args.push('--resume', sessionId);
    const child = spawn('claude', args, { cwd: WORKDIR, env: process.env });
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
      // queue this request behind any in-flight claude call
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
  res.writeHead(404); res.end('not found');
});

server.listen(PORT, '0.0.0.0', () => console.log(`27_074_2026 chat on :${PORT} (cwd=${WORKDIR}, session=${sessionId || 'new'})`));
