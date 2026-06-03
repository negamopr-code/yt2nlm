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
const WORKDIR = process.env.CLAUDE_CWD || '/workspace';
const SESS_FILE = path.join(DIR, '.session');
const SYS = 'You are the assistant for the "27_074_2026" working notebook, reachable as a web chat at http://localhost:8096/. You have full access to the /workspace project files. Be concise and concrete.';

let sessionId = existsSync(SESS_FILE) ? readFileSync(SESS_FILE, 'utf8').trim() || null : null;
let chain = Promise.resolve(); // serialize so --resume stays consistent

function runClaude(message) {
  return new Promise((resolve) => {
    const args = ['-p', message, '--output-format', 'json', '--append-system-prompt', SYS];
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
  if (req.method === 'POST' && req.url === '/reset') {
    sessionId = null;
    try { await writeFile(SESS_FILE, ''); } catch {}
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
      chain = chain.then(() => runClaude(message)).then((result) => {
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
