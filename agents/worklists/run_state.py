#!/usr/bin/env python3
"""Run-state doctor for the daily refresh: what an interrupted or dead run left.

Reports, in order:
- uncommitted agents/ changes grouped by scope, with file lists,
- scopes with uncommitted edits but no entry in the newest day log (the
  signature of a wave that died before logging),
- the newest day log's coverage across all scopes,
- untracked directories under agents/ (orphaned new notes),
- `updated:` bumps with no matching same-date Changes bullet (half-done edits).
"""
import os, re, subprocess, sys

ROOT = "/home/tomzx/src/blog.tomrochette.com-content"
AG = os.path.join(ROOT, "agents")
CATS = ["automated-research", "assistant-runtimes", "code-review", "context-engines",
        "control-planes", "evaluation-review", "executions", "harnesses",
        "hybrid-execution", "memory", "model-access", "orchestration",
        "people-and-publications", "protocols", "retrieval", "sandboxing",
        "session-analytics", "skills", "software-factory", "spec-driven-development",
        "surfaces", "task-management", "trackers-and-leaderboards"]
ROOT_SCOPES = CATS + ["section-root", "cross-category", "logs", "worklists"]


def git(*a):
    return subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True).stdout


def bump_detector():
    problems = []
    files = [f for f in git("diff", "--name-only", "--", "agents/").splitlines() if f.endswith("index.md")]
    for path in files:
        fdiff = git("diff", "--", path)
        m = re.search(r"^\+updated:\s*(\d{4}-\d{2}-\d{2})\s*$", fdiff, re.M)
        if not m:
            continue
        body_changed = any(l[:1] in "+-" and not l.startswith(("+++", "---"))
                           and not re.match(r"^[+-](updated:|status:|tags:|readability:|audience_notes:|title:|created:)", l)
                           and l[1:].strip() for l in fdiff.splitlines())
        if not body_changed:
            problems.append(f"{path}: bare updated bump with no content change (dead-worker signature)")
        elif not re.search(rf"^\+- {m.group(1)} - ", fdiff, re.M):
            problems.append(f"{path}: content changed, updated bumped to {m.group(1)}, no same-date Changes bullet (material change?)")
    return problems


def main():
    statuses = git("status", "--porcelain", "--", "agents/").splitlines()
    scopes = {}
    for line in statuses:
        if not line.strip():
            continue
        path = line[3:].strip().strip('"')
        parts = path.split("/")
        scope = parts[1] if len(parts) > 2 and parts[0] == "agents" else parts[-1]
        scopes.setdefault(scope, []).append((line[:2], path))

    print("== uncommitted agents/ changes by scope ==")
    if not scopes:
        print("  (clean)")
    for scope in sorted(scopes):
        print(f"  {scope} ({len(scopes[scope])}):")
        for st, path in scopes[scope][:8]:
            print(f"    {st} {path}")
        if len(scopes[scope]) > 8:
            print(f"    ... +{len(scopes[scope]) - 8} more")

    logs = sorted(glob_logs())
    today_log = logs[-1] if logs else None
    log_text = open(today_log, encoding="utf-8").read() if today_log else ""
    print(f"== newest log: {today_log or 'none'} ==")
    for scope in sorted(set(CATS) | {"section-root", "cross-category"}):
        hit = f"{scope}:" in log_text or f"{scope}/" in log_text
        dirty = scope in scopes
        if not hit or dirty:
            print(f"  {scope}: {'in log' if hit else 'NOT in log'}{' (has uncommitted edits)' if dirty else ''}")

    print("== untracked directories under agents/ ==")
    untracked = [l[3:] for l in statuses if l.startswith("??")]
    dirs = [u for u in untracked if os.path.isdir(os.path.join(ROOT, u))]
    print("  " + (", ".join(dirs) if dirs else "(none)"))

    print("== updated bumps without same-date Changes bullet ==")
    problems = bump_detector()
    print("  " + ("; ".join(problems) if problems else "(none)"))
    sys.exit(1 if problems else 0)


def glob_logs():
    d = os.path.join(AG, "logs")
    return [os.path.join(d, f) for f in os.listdir(d) if re.fullmatch(r"\d{4}-\d{2}-\d{2}\.md", f)]


if __name__ == "__main__":
    main()
