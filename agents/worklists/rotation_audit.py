#!/usr/bin/env python3
"""Rotation audit for the daily refresh: which notes have gone longest without a
full re-verification.

The work lists order rotation by last_verified (the newest ## Changes bullet),
so a member refreshed daily never rotates while a clean note rotates every run.
This script derives the real order from the audit trail instead: the newest day
log line that records a rotation re-verification for a slug (and, with --date,
the same lines in today's not-yet-collected worker reports), then prints each
category's oldest-first slice of about one seventh.

Read-only. Prints a table for --all, or the slice for --category <name>.

  rotation_audit.py --all [--date YYYY-MM-DD]
  rotation_audit.py --category orchestration --date YYYY-MM-DD
"""
import argparse, glob, math, os, re, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
REPORTS = "/tmp/opencode/agent-reports"
SEVENTH = 7
FRESH_DAYS = 7  # a note created this recently is not due for a rotation yet

# A log line records a full rotation pass when it says so positively; "out of
# rotation" lines record an out-of-schedule fix and are not passes.
POSITIVE = re.compile(
    r"rotation re-verif|re-verif\w* (?:in|under) (?:the )?rotation|in (?:the )?rotation\b"
    r"|rotation (?:quarter|pass|slice|wave)? ?covered", re.I)
NEGATIVE = re.compile(r"(?:out of|outside) (?:the )?rotation", re.I)
MULTI = re.compile(r"rotation (?:quarter|pass|slice|wave)? ?covered", re.I)


def categories():
    return sorted(
        d for d in os.listdir(ROOT)
        if os.path.isdir(os.path.join(ROOT, d))
        and os.path.exists(os.path.join(ROOT, d, "_index.md"))
        and d != "logs"
    )


def members(cat):
    out = {}
    for ip in glob.glob(os.path.join(ROOT, cat, "*", "index.md")):
        slug = os.path.basename(os.path.dirname(ip))
        if "feature-matrix" in slug:
            continue
        text = open(ip, encoding="utf-8").read()
        m = re.search(r"^created:\s*(\d{4}-\d{2}-\d{2})", text, re.M)
        v = re.search(r"^## Changes\s*$", text, re.M)
        newest = None
        if v:
            dates = re.findall(r"^-\s*(\d{4}-\d{2}-\d{2})\s*-", text[v.end():], re.M)
            newest = max(dates) if dates else None
        out[slug] = {"created": m.group(1) if m else None, "last_verified": newest}
    return out


def is_rotation(line):
    return bool(POSITIVE.search(line)) and not (NEGATIVE.search(line) and not re.search(
        r"rotation re-verif|re-verif\w* (?:in|under) (?:the )?rotation|in (?:the )?rotation\b", line, re.I))


SCOPES = {"resolution", "section-root", "cross-category"}


def slugs_in_head(line, known, cats):
    """Slugs named in the leading segment of a log line: after an optional
    '<category>: ' prefix, up to the first ' - ' or ': '. A 'rotation ... covered
    a, b, and c' line names every member of its list before the first ';'."""
    s = line.strip().lstrip("-").strip()
    first = re.match(r"([a-z0-9-]+):\s+", s)
    # strip a leading scope prefix, but never when the line opens with a slug
    if first and first.group(1) not in known and (first.group(1) in cats or first.group(1) in SCOPES):
        s = s[first.end():]
    if MULTI.search(s):
        head = s.split(";", 1)[0]
        return sorted({w for w in re.findall(r"[a-z0-9][a-z0-9-]*", head) if w in known},
                      key=head.index)
    head = re.split(r"\s+-\s+|:\s+", s, maxsplit=1)[0]
    return [w for w in re.findall(r"[a-z0-9][a-z0-9-]*", head) if w in known]


def last_rotations(known, date, cats):
    last = {}
    for lf in sorted(glob.glob(os.path.join(ROOT, "logs", "2*.md"))):
        d = os.path.basename(lf)[:-3]
        for line in open(lf, encoding="utf-8"):
            if line.startswith("- ") and is_rotation(line):
                for slug in slugs_in_head(line, known, cats):
                    if d > last.get(slug, ""):
                        last[slug] = d
    if date:
        for rp in glob.glob(os.path.join(REPORTS, f"*-{date}.md")):
            text = open(rp, encoding="utf-8").read()
            m = re.search(r"^## Log lines\s*$", text, re.M)
            if not m:
                continue
            rest = text[m.end():]
            n = re.search(r"^## ", rest, re.M)
            for line in (rest[: n.start()] if n else rest).splitlines():
                if line.strip().startswith("- ") and is_rotation(line):
                    for slug in slugs_in_head(line, known, cats):
                        if date > last.get(slug, ""):
                            last[slug] = date
    return last


def slice_for(cat, last, date):
    mem = members(cat)
    rows = []
    for slug, d in mem.items():
        lr = last.get(slug)
        fresh = bool(date and d["created"] and d["created"] >= date_shift(date))
        due = lr is not None or not fresh
        rows.append((lr or "0000-00-00", slug, lr, d["created"], d["last_verified"], due))
    rows.sort()
    due_rows = [r for r in rows if r[5]]
    n = max(1, math.ceil(len(rows) / SEVENTH))
    return rows, [r[1] for r in due_rows[:n]]


def date_shift(date):
    from datetime import date as D, timedelta
    return (D.fromisoformat(date) - timedelta(days=FRESH_DAYS)).isoformat()


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--all", action="store_true")
    p.add_argument("--category")
    p.add_argument("--date", help="run date; also counts today's uncollected worker reports")
    a = p.parse_args()
    cats_all = categories()
    cats = [a.category] if a.category else cats_all
    known = set()
    for cat in cats:
        known |= set(members(cat))
    last = last_rotations(known, a.date, set(cats_all))
    for cat in cats:
        rows, sl = slice_for(cat, last, a.date)
        if not a.all:
            print(f"{cat}: rotation slice ({len(sl)} of {len(rows)}, oldest full re-verification first):")
            for r in rows:
                if r[1] in sl:
                    print(f"  {r[1]} (last rotation {r[2] or 'never'}, created {r[3]}, last_verified {r[4]})")
            continue
        never = sum(1 for r in rows if r[2] is None and r[5])
        print(f"{cat:28s} members={len(rows):3d} slice={len(sl):2d} never-rotated={never:3d} "
              f"last-rotation<=2026-11-10={sum(1 for r in rows if r[2] and r[2] <= '2026-11-10'):3d}")
        print("   slice: " + ", ".join(f"{s}({last.get(s) or 'never'})" for s in sl))


if __name__ == "__main__":
    main()
