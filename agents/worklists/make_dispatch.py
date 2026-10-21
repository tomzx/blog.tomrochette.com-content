#!/usr/bin/env python3
"""Emit a slim dispatch file for one refresh worker and print the chat prompt.

The dispatch file carries everything variable about a dispatch (scope, run
date, mapped sources, handoff flags from earlier waves) so the chat prompt
stays two lines. Rules live in agents/worker-contract.md; per-scope data in
agents/worklists/<scope>.yaml. Flags come from flags-<date>.md, written by
collect_reports.py.
"""
import argparse, os, re

AG = "/home/tomzx/src/blog.tomrochette.com-content/agents"
REPORTS = "/tmp/opencode/agent-reports"


def mapped_sources(scope):
    wl = os.path.join(AG, "worklists", f"{scope}.yaml")
    if not os.path.exists(wl):
        return None
    sources, inside = [], False
    for line in open(wl, encoding="utf-8"):
        if line.startswith("mapped_sources:"):
            inside = True
            continue
        if inside:
            m = re.match(r"\s*- repo: (\S+)", line)
            if m:
                sources.append(m.group(1))
            elif line.strip() and not line[0].isspace():
                break
    return sources


def flags_for(scope, date):
    fp = os.path.join(REPORTS, f"flags-{date}.md")
    if not os.path.exists(fp):
        return []
    out = []
    for line in open(fp, encoding="utf-8"):
        s = line.strip()
        if s.startswith("- ") and s[2:].split(":")[0].strip() == scope:
            out.append(s[2:])
    return out


def scope_path(scope):
    if scope in ("section-root", "cross-category"):
        return ("agents/ (essays, trackers, the model-provider matrix, the section index); writes only in the directories the contract's variants section names"
                if scope == "section-root" else
                "no category; writes nothing under agents/ except by coordinator instruction")
    return f"agents/{scope}/"


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--scope", required=True)
    p.add_argument("--date", required=True)
    p.add_argument("--handoff", action="append", default=[],
                   help="coordinator handoff text; repeatable")
    args = p.parse_args()
    scope, date = args.scope, args.date

    lines = [f"scope: {scope}",
             f"run date: {date}",
             "repo root: /home/tomzx/src/blog.tomrochette.com-content",
             f"scope path: {scope_path(scope)}"]
    wl = os.path.join(AG, "worklists", f"{scope}.yaml")
    if os.path.exists(wl):
        lines.append(f"work list: agents/worklists/{scope}.yaml")
    sources = mapped_sources(scope)
    if sources is None:
        lines.append("mapped sources: none; no work list for this scope (the contract's variants section applies)")
    elif sources:
        lines.append("mapped sources: " + ", ".join(sources))
    else:
        lines.append("mapped sources: none dedicated; broad sources ride the cross-category scanner")
    fl = flags_for(scope, date)
    if fl:
        lines.append("handoff flags naming this scope (resolve in this run):")
        lines += [f"  - {f}" for f in fl]
    if args.handoff:
        lines.append("coordinator handoffs:")
        lines += [f"  - {h}" for h in args.handoff]

    os.makedirs(REPORTS, exist_ok=True)
    out = os.path.join(REPORTS, f"dispatch-{scope}.txt")
    with open(out, "w", encoding="utf-8") as f:
        f.write("\n".join(lines) + "\n")
    print(f"dispatch file: {out}")
    print("\nchat prompt:")
    print(f"You are the {scope} worker in the daily refresh of the agents section at "
          f"/home/tomzx/src/blog.tomrochette.com-content. Read agents/worker-contract.md, "
          f"your dispatch file {out}, and your work list agents/worklists/{scope}.yaml, "
          f"then execute on the dispatch's run date. Write your full report to the report "
          f"file and end with the five-line summary; never paste the report into the reply.")


if __name__ == "__main__":
    main()
