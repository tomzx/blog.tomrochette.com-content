#!/usr/bin/env python3
"""One-call precommit check for the daily refresh coordinator.

Runs the section verification (verify_section.py), then audits the uncommitted
agents/ diff for banned terms in added lines and for `updated:` bumps that lack
a matching same-date `## Changes` bullet, and groups the working tree by scope.
Warnings do not block; verification failures and unexplained bumps do.
Exit 1 only when something blocks a commit.
"""
import os, re, subprocess, sys

ROOT = "/home/tomzx/src/blog.tomrochette.com-content"
AG = os.path.join(ROOT, "agents")
TERM = re.compile(r"\b(shape|honest|load[ -]bearing|posture|real)\b", re.I)
BUMP = re.compile(r"^\+updated:\s*(\d{4}-\d{2}-\d{2})\s*$", re.M)


def git(*a):
    return subprocess.run(["git", "-C", ROOT, *a], capture_output=True, text=True).stdout


def grouped_status():
    scopes = {}
    for line in git("status", "--porcelain", "--", "agents/").splitlines():
        if not line.strip():
            continue
        path = line[3:].strip().strip('"')
        parts = path.split("/")
        scope = parts[1] if len(parts) > 2 and parts[0] == "agents" else parts[-1]
        scopes.setdefault(scope, []).append((line[:2], path))
    return scopes


def main():
    blocked = False

    r = subprocess.run([sys.executable, os.path.join(AG, "worklists", "verify_section.py")],
                       capture_output=True, text=True)
    print(r.stdout.strip())
    if r.returncode != 0:
        blocked = True
        print("-> verify_section.py failed")

    diff = git("diff", "--", "agents/") + git("diff", "--cached", "--", "agents/")
    added = [l[1:] for l in diff.splitlines() if l.startswith("+") and not l.startswith("+++")]
    hits = {}
    for line in added:
        m = TERM.search(line)
        if m:
            hits.setdefault(m.group(0).lower(), []).append(line.strip()[:120])
    if hits:
        for term, lines in sorted(hits.items()):
            print(f"WARNING banned term in added lines: '{term}' x{len(lines)}")
            for l in lines[:3]:
                print(f"   {l}")
        print("   (new prose must avoid these; retained documented exceptions in edited lines are fine - judge each)")

    files = [f for f in git("diff", "--name-only", "--", "agents/").splitlines() if f.endswith("index.md")]
    for path in files:
        fdiff = git("diff", "--", path)
        m = BUMP.search(fdiff)
        if not m:
            continue
        date = m.group(1)
        body_changed = any(l[:1] in "+-" and not l.startswith(("+++", "---"))
                           and not re.match(r"^[+-](updated:|status:|tags:|readability:|audience_notes:|title:|created:)", l)
                           and l[1:].strip() for l in fdiff.splitlines())
        if not body_changed:
            print(f"BLOCK bare updated bump with no content change (dead-worker signature): {path}")
            blocked = True
        elif not re.search(rf"^\+- {date} - ", fdiff, re.M):
            print(f"WARNING updated bumped to {date}, content changed, no same-date Changes bullet (material change?): {path}")

    scopes = grouped_status()
    print(f"tree: {sum(len(v) for v in scopes.values())} changed paths under agents/, by scope:")
    for scope in sorted(scopes):
        entries = scopes[scope]
        preview = ", ".join(p for _, p in entries[:3])
        more = f" (+{len(entries) - 3} more)" if len(entries) > 3 else ""
        print(f"  {scope}: {len(entries)}  {preview}{more}")

    repos = {}
    for path in __import__("glob").glob(os.path.join(AG, "*", "*", "index.md")):
        if "/_index/" in path or "feature-matrix" in path or "/logs/" in path or "/worklists/" in path:
            continue
        try:
            text = open(path, encoding="utf-8").read()
        except OSError:
            continue
        m = re.search(r"star-history\.com/chart\?repos=([\w./,-]+)&", text)
        if m:
            t = re.search(r"^title:\s*(.+)$", text, re.M)
            repos.setdefault(m.group(1), []).append(
                (os.path.relpath(os.path.dirname(path), AG), (t.group(1).strip().strip('"') if t else "?")))
    for repo, notes in sorted(repos.items()):
        if len(notes) > 1:
            titles = [n[1].casefold() for n in notes]
            if len(set(titles)) < len(titles):
                print(f"BLOCK duplicate subject repository and title {repo}: " +
                      ", ".join(f"{p} ({t})" for p, t in notes))
                blocked = True
            else:
                print(f"note shared subject repository {repo}: " +
                      ", ".join(f"{p} ({t})" for p, t in notes) + " (subsystem note? judge once)")

    print("verdict:", "BLOCKED" if blocked else "ok")
    sys.exit(1 if blocked else 0)


if __name__ == "__main__":
    main()
