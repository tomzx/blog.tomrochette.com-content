#!/usr/bin/env python3
"""Assemble finished worker reports into the shared files.

Reads /tmp/opencode/agent-reports/<scope>-<date>.md for each scope and:
- appends the report's `## Log lines` block to agents/logs/<date>.md under
  `## (daily refresh, <wave>)` (creates the log file if missing; refuses a
  wave heading that already exists),
- bumps `last_checked` to the run date in agents/worklists/<scope>.yaml for
  every repo listed under `## Sources scanned`,
- appends `## Flags` lines to /tmp/opencode/agent-reports/flags-<date>.md so
  later dispatches can reference them,
- prints the report's `## Digest lines` and `## Queue bullets` blocks for the
  coordinator to apply to standing-decisions.md and queue.md by hand.

The report file format is fixed by agents/worker-contract.md.
"""
import argparse, os, re, sys

AG = "/home/tomzx/src/blog.tomrochette.com-content/agents"
REPORTS = "/tmp/opencode/agent-reports"


def section(text, name):
    m = re.search(rf"^## {re.escape(name)}\s*$", text, re.M)
    if not m:
        return []
    rest = text[m.end():]
    nxt = re.search(r"^## ", rest, re.M)
    body = rest[: nxt.start()] if nxt else rest
    return [line.rstrip() for line in body.splitlines() if line.strip()]


def slugs_of(scope):
    d = os.path.join(AG, scope)
    if not os.path.isdir(d):
        return set()
    return {n for n in os.listdir(d) if os.path.isdir(os.path.join(d, n))}


def normalize(line, scope, slugs):
    s = line.strip().lstrip("-").strip()
    head = s.split(":")[0].split("/")[0].strip()
    if head == scope or head in slugs:
        return f"- {s}"
    return f"- {scope}: {s}"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--date", required=True)
    p.add_argument("--wave", required=True)
    p.add_argument("--scopes", nargs="+", required=True)
    args = p.parse_args()

    log_path = os.path.join(AG, "logs", f"{args.date}.md")
    heading = f"## (daily refresh, {args.wave})"
    log = open(log_path, encoding="utf-8").read() if os.path.exists(log_path) else None
    if log and heading in log:
        sys.exit(f"refusing: {heading!r} already in {log_path}")

    flags_path = os.path.join(REPORTS, f"flags-{args.date}.md")
    new_log_lines, flags, bumped, digest, queue, missing = [], [], [], [], [], []
    for scope in args.scopes:
        rp = os.path.join(REPORTS, f"{scope}-{args.date}.md")
        if not os.path.exists(rp):
            missing.append(rp)
            continue
        text = open(rp, encoding="utf-8").read()
        slugs = slugs_of(scope)
        for line in section(text, "Log lines"):
            new_log_lines.append(normalize(line, scope, slugs))
        for line in section(text, "Flags"):
            flags.append(f"- {scope}: " + line.strip().lstrip("-").strip())
        repos = [l.strip().lstrip("-").strip() for l in section(text, "Sources scanned")]
        wl = os.path.join(AG, "worklists", f"{scope}.yaml")
        if repos and os.path.exists(wl):
            wt = open(wl, encoding="utf-8").read()
            for repo in repos:
                pat = re.compile(r"(repo: " + re.escape(repo) + r"\n    last_checked: )\S+")
                wt, n = pat.subn(r"\g<1>" + args.date, wt)
                bumped.append((scope, repo, n))
            open(wl, "w", encoding="utf-8").write(wt)
        digest += [(scope, l) for l in section(text, "Digest lines")]
        queue += [(scope, l) for l in section(text, "Queue bullets")]

    if missing:
        for rp in missing:
            print(f"MISSING report: {rp}", file=sys.stderr)
    if not new_log_lines and not flags and not bumped:
        sys.exit("nothing to assemble")

    if new_log_lines:
        log = (log or
               f"---\ntitle: Agents log {args.date}\ncreated: {args.date}\n"
               f"status: finished\ntags: [agents]\nreadability: 0\n---\n")
        log = log.rstrip("\n") + "\n\n" + heading + "\n\n" + "\n".join(new_log_lines) + "\n"
        open(log_path, "w", encoding="utf-8").write(log)
        print(f"log: appended {len(new_log_lines)} lines under {heading!r} -> {log_path}")

    if flags:
        os.makedirs(REPORTS, exist_ok=True)
        with open(flags_path, "a", encoding="utf-8") as f:
            f.write("\n".join(flags) + "\n")
        print(f"flags: appended {len(flags)} -> {flags_path}")

    for scope, repo, n in bumped:
        print(f"last_checked: {scope}.yaml {repo} -> {args.date}" + ("" if n else "  (NOT FOUND)"))

    if digest:
        print("\nproposed standing-decisions lines (apply by hand):")
        for scope, line in digest:
            print(f"  [{scope}] {line}")
    if queue:
        print("\nproposed queue bullets (apply by hand):")
        for scope, line in queue:
            print(f"  [{scope}] {line}")


if __name__ == "__main__":
    main()
