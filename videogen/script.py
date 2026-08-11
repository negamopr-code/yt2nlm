"""Script generation: ONE Gemini (NotebookLM) query per video, strict JSON,
WordNet factual guardrail, slide expansion."""

from __future__ import annotations

import json
import re
import sys

from .config import STATE_DIR, WORKSPACE, norm_word, now_utc

sys.path.insert(0, str(WORKSPACE))
from yt2nlm import nlm  # noqa: E402  (reuses the serialized CLI wrapper)

PROMPT_TMPL = """You write a YouTube script for the channel "Another Word" (English vocabulary for learners and IELTS takers).
TARGET WORD: {word}
A real viewer asked (address it implicitly, do not quote it): {question}
Audience needs, from this corpus: an example sentence for EVERY synonym; register (formal/informal/neutral) and intensity guidance; at least {n_min} alternatives; NO archaic or obscure words; perfect spelling.
Return STRICT JSON only — no prose, no markdown fences:
{{"hook":"<=15 words, spoken, curiosity-driven",
 "intro":"1-2 spoken sentences: when and why to replace '{word}'",
 "synonyms":[{n_min} to {n_max} objects:
   {{"word":"...","register":"formal|informal|neutral","intensity":1-5,
     "nuance":"<=12 words on when to prefer it",
     "examples":[{n_ex} natural spoken sentence(s)]}}],
 "quiz":{{"question":"one fill-in-the-blank sentence with ___","options":["..","..",".."],
   "answer":0,"explain":"<=15 words"}},
 "title":"<=90 chars, must start with: Another Word for {word_title}",
 "description":"2-3 sentences; the LAST line must be exactly: More at anotherwordfor.net",
 "tags":[10-15 short lowercase strings]}}
Rules: everyday synonyms only; examples sound like real speech; vary sentence topics; no citation markers like [1]."""

RETRY_TMPL = """Your previous JSON had problems: {problems}.
Return the corrected STRICT JSON only, same schema, nothing else."""

REGISTERS = {"formal", "informal", "neutral"}


def _notebook_id() -> str:
    st = json.loads((STATE_DIR / "monitor-awf.json").read_text())
    return st["notebook_id"]


def _extract_json(text: str) -> dict:
    """First balanced {...} block."""
    start = text.find("{")
    if start < 0:
        raise ValueError("no JSON object in answer")
    depth = 0
    for i in range(start, len(text)):
        if text[i] == "{":
            depth += 1
        elif text[i] == "}":
            depth -= 1
            if depth == 0:
                return json.loads(text[start:i + 1])
    raise ValueError("unbalanced JSON in answer")


def validate(s: dict, cfg: dict, fmt: str) -> list[str]:
    problems = []
    for k in ("hook", "intro", "synonyms", "quiz", "title", "description", "tags"):
        if k not in s:
            problems.append(f"missing key {k}")
    syns = s.get("synonyms") or []
    if not (cfg["n_min"] <= len(syns) <= cfg["n_max"] + 2):
        problems.append(f"need {cfg['n_min']}-{cfg['n_max']} synonyms, got {len(syns)}")
    n_ex = cfg["examples_per_synonym"]["shorts" if fmt == "shorts" else "long"]
    for y in syns:
        if (y.get("register") or "").lower() not in REGISTERS:
            problems.append(f"bad register for {y.get('word')}")
        if not isinstance(y.get("intensity"), int) or not 1 <= y["intensity"] <= 5:
            problems.append(f"bad intensity for {y.get('word')}")
        if len(y.get("examples") or []) < n_ex:
            problems.append(f"need {n_ex} example(s) for {y.get('word')}")
    quiz = s.get("quiz") or {}
    if not (isinstance(quiz.get("answer"), int)
            and 0 <= quiz["answer"] < len(quiz.get("options") or [])):
        problems.append("bad quiz answer index")
    if "___" not in (quiz.get("question") or ""):
        problems.append("quiz question needs ___")
    if not (s.get("description") or "").rstrip().endswith("More at anotherwordfor.net"):
        problems.append("description must end with the exact CTA line")
    return problems


def wordnet_check(target: str, synonyms: list[dict], strictness: str) -> list[dict]:
    """Tag each synonym; drop hallucinations. Returns surviving list."""
    from nltk.corpus import wordnet as wn
    t_syns = wn.synsets(target.replace(" ", "_"))
    t_lemmas = {l.name().lower().replace("_", " ")
                for s in t_syns for l in s.lemmas()}
    out = []
    for y in synonyms:
        w = norm_word(y.get("word", ""))
        w_syns = wn.synsets(w.replace(" ", "_"))
        if not w_syns:
            y["wordnet"] = "unknown-lemma"      # typo/hallucination — drop
            print(f"  wordnet: DROP {w!r} (no lemma)", file=sys.stderr)
            continue
        w_lemmas = {l.name().lower().replace("_", " ")
                    for s in w_syns for l in s.lemmas()}
        if w in t_lemmas or target in w_lemmas or (t_lemmas & w_lemmas):
            y["wordnet"] = "verified"
        else:
            sim = max((a.path_similarity(b) or 0)
                      for a in (t_syns or w_syns) for b in w_syns) if t_syns else 0
            y["wordnet"] = "related" if sim >= 0.25 else "unrelated"
            if y["wordnet"] == "unrelated" and strictness == "drop":
                print(f"  wordnet: DROP {w!r} (unrelated)", file=sys.stderr)
                continue
        out.append(y)
    return out


def to_slides(s: dict, fmt: str) -> list[dict]:
    slides = [{"kind": "hook", "speech": s["hook"],
               "display": {"text": s["hook"]}}]
    if fmt == "long":
        slides.append({"kind": "intro", "speech": s["intro"],
                       "display": {"text": s["intro"]}})
    n = 5 if fmt == "shorts" else len(s["synonyms"])
    for y in s["synonyms"][:n]:
        ex = y["examples"][0]
        # Shorts pacing: nuance is SHOWN on the card but not spoken (a spoken
        # nuance per word pushed the first render to 90 s; target is <=60 s).
        speech = (f"{y['word']}. For example: {ex}" if fmt == "shorts" else
                  f"{y['word']}. {y.get('nuance', '')}. For example: {ex}")
        slides.append({"kind": "word", "speech": speech,
                       "display": {"word": y["word"], "register": y["register"],
                                   "intensity": y["intensity"],
                                   "nuance": y.get("nuance", ""),
                                   "example": ex}})
        if fmt == "long" and len(y["examples"]) > 1:
            slides.append({"kind": "example", "speech": f"Or: {y['examples'][1]}",
                           "display": {"word": y["word"],
                                       "example": y["examples"][1]}})
    q = s["quiz"]
    if fmt == "shorts":
        quiz_speech = ("Quick quiz! Which one fits this sentence best? "
                       "Pause and pick your answer.")
    else:
        opts = " … ".join(f"{chr(65 + i)}: {o}"
                          for i, o in enumerate(q["options"]))
        quiz_speech = (f"Quick quiz! {q['question'].replace('___', 'blank')} "
                       f"{opts}")
    slides.append({"kind": "quiz_q", "speech": quiz_speech,
                   "display": {"question": q["question"], "options": q["options"]}})
    slides.append({"kind": "quiz_reveal",
                   "speech": f"The answer is {q['options'][q['answer']]}. "
                             f"{q.get('explain', '')}",
                   "display": {"question": q["question"], "options": q["options"],
                               "answer": q["answer"], "explain": q.get("explain", "")}})
    slides.append({"kind": "outro",
                   "speech": "Find hundreds more alternatives at another word for dot net.",
                   "display": {"text": "More at\nanotherwordfor.net"}})
    return slides


def generate(topic: dict, cfg: dict, fmt: str) -> dict:
    word = topic["target"]
    n_ex = cfg["examples_per_synonym"]["shorts" if fmt == "shorts" else "long"]
    prompt = PROMPT_TMPL.format(
        word=word, word_title=word.title(),
        question=(topic["source"].get("text") or
                  f"What is another word for {word}?")[:1500],
        n_min=cfg["n_min"], n_max=cfg["n_max"], n_ex=n_ex)
    nb = _notebook_id()
    r = nlm.query(nb, prompt, timeout=300)
    try:
        s = _extract_json(r["answer"])
        problems = validate(s, cfg, fmt)
    except (ValueError, json.JSONDecodeError) as exc:
        s, problems = {}, [str(exc)]
    if problems:
        print(f"  script retry ({len(problems)} problems): {problems[:3]}",
              file=sys.stderr)
        r = nlm.query(nb, prompt + "\n\n" +
                      RETRY_TMPL.format(problems="; ".join(problems[:6])),
                      timeout=300)
        s = _extract_json(r["answer"])
        problems = validate(s, cfg, fmt)
        if problems:
            raise RuntimeError(f"script invalid after retry: {problems}")
    s["synonyms"] = wordnet_check(word, s["synonyms"], cfg["wordnet_strictness"])
    if len(s["synonyms"]) < cfg["n_min"]:
        raise RuntimeError(f"only {len(s['synonyms'])} synonyms survived WordNet")
    s.update({"format": fmt, "target": word, "topic_source": topic["source"],
              "slides": to_slides(s, fmt),
              "nlm": {"notebook_id": nb,
                      "sources_used": len(r.get("sources_used") or [])},
              "created_at": now_utc()})
    return s
