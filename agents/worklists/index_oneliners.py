#!/usr/bin/env python3
"""Check the section index's matrix one-liners against the matrices on disk.

For every matrix linked from agents/_index.md, prints the header's column count,
the matrix's newest Changes date, the date the one-liner states as "verified",
and the first number words stated in the one-liner (word counts such as
"twenty-six" are parsed; digit counts are read as digits). A line ending in
"<-- CHECK" means the first stated count differs from the header count; judge
it by hand, because some one-liners open with a count that is not the member
count ("three Cowork desktops", "two independent boards").

Read-only. Run it at resolution time, after admissions land.
"""
import os, re, sys

AG = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
UNITS = {"zero": 0, "one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6, "seven": 7,
         "eight": 8, "nine": 9, "ten": 10, "eleven": 11, "twelve": 12, "thirteen": 13,
         "fourteen": 14, "fifteen": 15, "sixteen": 16, "seventeen": 17, "eighteen": 18,
         "nineteen": 19, "twenty": 20, "thirty": 30, "forty": 40, "fifty": 50, "sixty": 60,
         "seventy": 70, "eighty": 80, "ninety": 90}
WORD = re.compile(
    r"\b((?:twenty|thirty|forty|fifty|sixty|seventy|eighty|ninety|ten|eleven|twelve|thirteen|"
    r"fourteen|fifteen|sixteen|seventeen|eighteen|nineteen|one|two|three|four|five|six|seven|"
    r"eight|nine)(?:-[a-z]+)?)\b")
DIGIT = re.compile(r"\bnow (\d+) columns\b")


def word_count(w):
    return sum(UNITS.get(p, 0) for p in w.split("-"))


def main():
    idx = open(os.path.join(AG, "_index.md"), encoding="utf-8").read()
    ones = re.findall(r"^- \[([^\]]+)\]\(([^)]+)-feature-matrix/index\.md\) - (.*)$", idx, re.M)
    ones += [(_, p, t) for _, p, t in
             re.findall(r"^- \[([^\]]+)\]\((model-[a-z-]*matrix)/index\.md\) - (.*)$", idx, re.M)]
    bad = 0
    for title, path, text in ones:
        cands = [os.path.join(AG, f"{path}-feature-matrix", "index.md"), os.path.join(AG, path, "index.md")]
        mp = next((c for c in cands if os.path.exists(c)), None)
        if mp is None:
            print(f"MISSING matrix for one-liner: {path}")
            bad += 1
            continue
        m = open(mp, encoding="utf-8").read()
        rows = [l.strip() for l in m.splitlines() if l.strip().startswith("|") and l.strip().endswith("|")]
        ncol = len(rows[0].strip().strip("|").split("|")) - 1 if rows else -1
        v = re.search(r"^## Changes\s*$", m, re.M)
        newest = max(re.findall(r"^-\s*(\d{4}-\d{2}-\d{2})\s*-", m[v.end():], re.M)) if v else None
        vd = re.search(r"verified (\d{4}-\d{2}-\d{2})", text)
        stated = [(w, word_count(w)) for w in WORD.findall(text)]
        dig = [(d, int(d)) for d in DIGIT.findall(text)]
        mark = ""
        first = (dig or stated or [("", None)])[0]
        if first[1] is not None and first[1] != ncol:
            mark = "  <-- CHECK"
            bad += 1
        name = path.split("/")[0]
        print(f"{name:28s} cols={ncol:3d} newestChanges={newest} verified={vd.group(1) if vd else '-'}  "
              f"stated={stated[:2]} digits={dig}{mark}")
    print(f"one-liners: {len(ones)}, to check by hand: {bad}")
    sys.exit(1 if bad else 0)


if __name__ == "__main__":
    main()
