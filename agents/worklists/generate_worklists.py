#!/usr/bin/env python3
"""Generate the agents-section work lists: agents/worklists/<category>.yaml.

The daily refresh runs this before dispatching workers. Without --signals it
regenerates from the markdown alone (fast, offline). With --signals it also
records per-member movement (pushed_at, latest release tag) from one batched
GitHub pass via `gh api`, flagging members whose subject moved since their
last-verified date. Workers read these files instead of deriving work lists
from markdown or polling GitHub per note.

Data per member: slug, title, subject repo (from the star-history chart),
last-verified date (newest ## Changes bullet), last seen pushed_at and release
tag, and the resulting signals. Per category: mapped awesome-list sources with
their last-checked dates (preserved from the previous file unless --checked is
given) and the queue questions governing the scope.
"""
import argparse, json, os, re, glob, subprocess
from concurrent.futures import ThreadPoolExecutor
from datetime import date

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "worklists")

SOURCES = {
    "context-engines": ["Meirtz/Awesome-Context-Engineering"],
    "control-planes": ["agentrust-io/awesome-ai-governance"],
    "evaluation-review": ["anhermon/awesome-agent-observability"],
    "session-analytics": ["anhermon/awesome-agent-observability"],
    "memory": ["TeleAI-UAGI/Awesome-Agent-Memory"],
    "model-access": ["rafska/awesome-local-llm"],
    "orchestration": ["kaushikb11/awesome-llm-agents"],
    "protocols": ["punkpeye/awesome-mcp-servers", "punkpeye/awesome-mcp-clients", "insodimension/awesome-agent-protocols"],
    "retrieval": ["Yigtwxx/awesome-rag-production", "Danielskry/Awesome-RAG"],
    "sandboxing": ["arjan/awesome-agent-sandboxes"],
    "skills": ["VoltAgent/awesome-agent-skills", "ComposioHQ/awesome-claude-skills", "VoltAgent/awesome-claude-code-subagents"],
    "spec-driven-development": ["Engineering4AI/awesome-spec-driven-development"],
}

# q#N is the Nth "? for tom:" bullet in agents/queue.md, in file order.
QUESTIONS = {
    "orchestration": [("q7", "should any single-vendor agent-building SDK get an orchestration column"), ("q12", "should openai/symphony be profiled despite the mission-control tail rejection")],
    "harnesses": [("q22", "if a harnesses list gets wired, is the target walkinglabs or ai-boost (name collision)")],
    "people-and-publications": [("q5", "should METR be profiled as a voice after its tracker rejection"), ("q10", "is a vendor engineering blog admissible as a voice")],
    "automated-research": [("q26", "wire either, both, or neither of the two autoresearch lists")],
    "surfaces": [("q14", "which shelf (or rejection) holds for OpenBitFun")],
    "sandboxing": [("q2", "does E2B become a note of its own or stay comparison-only")],
    "evaluation-review": [("q6", "third observability column (Opik), second eval-framework column (promptfoo), or stand"), ("q19", "add a security-evaluation family or hold the output-judging scope")],
    "retrieval": [("q4", "should Haystack become a third framework column"), ("q17", "do CocoIndex, Crawl4AI, or DSPy deserve columns, or do the family scopes stand")],
    "task-management": [("q24", "owner-tools exception for TomzxCode/agentic or the rejection stands")],
    "assistant-runtimes": [("q13", "does openhuman break the absorbed-family rejection at OpenClaw-class scale")],
    "skills": [("q11", "do the skills-scale records change the pack policy"), ("q16", "admit the generator kind (Skill_Seekers) or hold the scope"), ("q20", "do the grown pack-scale records change the pack policy")],
    "code-review": [("q21", "wire the vendor-run stale kodustech list or stay on broad sources")],
}

def gh(path):
    r = subprocess.run(["gh", "api", path, "--jq", "."], capture_output=True, text=True, timeout=45)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return None

def fetch_state(repo):
    info = gh(f"repos/{repo}")
    pushed = (info or {}).get("pushed_at")
    rel = gh(f"repos/{repo}/releases/latest")
    tag = (rel or {}).get("tag_name")
    return pushed, tag

def categories():
    return sorted(
        d for d in os.listdir(ROOT)
        if os.path.isdir(os.path.join(ROOT, d))
        and os.path.exists(os.path.join(ROOT, d, "_index.md"))
        and d != "logs"
    )

def fm(text, key):
    m = re.search(rf"^{key}:\s*(.+)$", text, re.M)
    return m.group(1).strip().strip('"') if m else None

def last_verified(text):
    m = re.search(r"^## Changes\s*$", text, re.M)
    if not m:
        return None
    dates = re.findall(r"^-\s*(\d{4}-\d{2}-\d{2})\s*-", text[m.end():], re.M)
    return max(dates) if dates else None

def subject_repo(text):
    m = re.search(r"star-history\.com/chart\?repos=([\w./,-]+)&", text)
    return m.group(1) if m else None

def parse_old(cat):
    """Recover last_checked dates and per-member last_pushed/last_release from the previous yaml."""
    path = os.path.join(OUT, f"{cat}.yaml")
    state = {"checked": {}, "pushed": {}, "release": {}}
    if not os.path.exists(path):
        return state
    repo = checked = None
    for line in open(path, encoding="utf-8"):
        m = re.match(r"\s*- repo: (\S+)", line)
        if m:
            repo, checked = m.group(1), None
            continue
        m = re.match(r"\s*last_checked: (\S+)", line)
        if m and repo:
            state["checked"][repo] = m.group(1)
        m = re.match(r"\s*- slug: (\S+)", line)
        slug = m.group(1) if m else None
        m = re.match(r"\s*last_pushed: (\S+)", line)
        if m and slug:
            state["pushed"][slug] = m.group(1)
        m = re.match(r'\s*last_release: "?([^"\n]*)"?', line)
        if m and slug:
            state["release"][slug] = None if m.group(1) == "null" else m.group(1)
    return state

def yaml_str(v):
    if v is None:
        return "null"
    s = str(v)
    if re.match(r"^[A-Za-z0-9][A-Za-z0-9 ./_&()'-]*$", s):
        return s
    return '"' + s.replace('\\', '\\\\').replace('"', '\\"') + '"'

def build(cat, args):
    old = parse_old(cat)
    lines = [f"# Generated by agents/worklists/generate_worklists.py on {args.today}; do not hand-edit.",
             f"category: {cat}", f"generated: {args.today}"]
    if SOURCES.get(cat, []):
        lines.append("mapped_sources:")
        for s in SOURCES.get(cat, []):
            lines.append(f"  - repo: {s}")
            lines.append(f"    last_checked: {args.checked or old['checked'].get(s, args.today)}")
    qs = QUESTIONS.get(cat, [])
    if qs:
        lines.append("governing_questions:")
        for qid, summary in qs:
            lines.append(f"  - id: {qid}")
            lines.append("    summary: " + yaml_str(summary))
    members = []
    for ip in sorted(glob.glob(os.path.join(ROOT, cat, "*", "index.md"))):
        slug = os.path.basename(os.path.dirname(ip))
        if "feature-matrix" in slug:
            continue
        text = open(ip, encoding="utf-8").read()
        members.append({
            "slug": slug,
            "title": fm(text, "title") or slug,
            "repo": subject_repo(text),
            "verified": last_verified(text),
            "pushed": old["pushed"].get(slug),
            "release": old["release"].get(slug),
        })
    if args.signals:
        with ThreadPoolExecutor(max_workers=8) as ex:
            futures = {m["slug"]: ex.submit(fetch_state, m["repo"]) for m in members if m["repo"]}
            for slug, fut in futures.items():
                pushed, tag = fut.result()
                for m in members:
                    if m["slug"] == slug:
                        m["new_pushed"], m["new_release"] = pushed, tag
    lines.append("notes:")
    for m in members:
        sig = []
        if args.signals and m.get("new_pushed"):
            sig.append("pushed" if (m["verified"] or "") and m["new_pushed"][:10] > (m["verified"] or "") else "")
        if args.signals and m.get("new_release") is not None and m.get("release") is not None and m["new_release"] != m["release"]:
            sig.append("released")
        sig = [s for s in sig if s]
        lines.append(f"  - slug: {m['slug']}")
        lines.append("    title: " + yaml_str(m["title"]))
        lines.append("    subject_repo: " + (m["repo"] or "null"))
        lines.append("    last_verified: " + (m["verified"] or "null"))
        if args.signals and m["repo"]:
            np = m.get("new_pushed")
            lines.append("    last_pushed: " + (np[:10] if np else "null"))
            nr = m.get("new_release", "__unset__")
            lines.append("    last_release: " + ("null" if nr in (None, "__unset__") else yaml_str(nr)))
            lines.append("    signals: [" + ", ".join(sig) + "]" if sig else "    signals: []")
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, f"{cat}.yaml"), "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    return len(members), sum(1 for m in members if m["repo"])

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--signals", action="store_true", help="fetch pushed_at/release state via gh api (slow)")
    p.add_argument("--checked", help="set mapped_sources last_checked to this date")
    p.add_argument("--today", default=date.today().isoformat())
    p.add_argument("--categories", nargs="*", help="limit to these categories")
    args = p.parse_args()
    cats = args.categories or categories()
    for cat in cats:
        n, r = build(cat, args)
        print(f"{cat}: {n} notes, {r} with repos{' (signals fetched)' if args.signals else ''}")

if __name__ == "__main__":
    main()
