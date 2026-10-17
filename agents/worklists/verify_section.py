#!/usr/bin/env python3
"""Agents-section verification pass: internal links, front matter (type-field
ban, mandatory tags), matrix width incl. separator rows, matrix column sort and
membership by link slug, category index membership and sort, em/en-dash bans,
banned-term counts. Paths filtered to agents/."""
import os, re, sys, glob

ROOT = "/home/tomzx/src/blog.tomrochette.com-content/agents"
CATS = ["automated-research", "assistant-runtimes", "code-review", "context-engines",
        "control-planes", "evaluation-review", "executions", "harnesses",
        "hybrid-execution", "memory", "model-access", "orchestration",
        "people-and-publications", "protocols", "retrieval", "sandboxing",
        "session-analytics", "skills", "software-factory", "spec-driven-development",
        "surfaces", "task-management", "trackers-and-leaderboards"]
problems = []
banned_hits = {}

LINK = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

def front_matter(text):
    if not text.startswith("---"):
        return None
    m = re.match(r"^---\n(.*?)\n---\n", text, re.S)
    return m.group(1) if m else None

def check_file(path, research_note=None):
    with open(path) as f:
        text = f.read()
    rel = os.path.relpath(path, ROOT)
    fm = front_matter(text)
    if fm is None:
        problems.append(f"{rel}: front matter missing/unparsable")
        fm = ""
    if re.search(r"^type:", fm, re.M):
        problems.append(f"{rel}: forbidden type field")
    if research_note is not False:
        for tag in ("agent-curated", "fully-ai-generated"):
            if tag not in fm:
                problems.append(f"{rel}: missing mandatory tag {tag}")
        if "llm=" not in fm:
            problems.append(f"{rel}: missing llm= tag")
    if research_note and "research-note" not in fm:
        problems.append(f"{rel}: missing research-note tag")
    if "\u2014" in text or "\u2013" in text:
        problems.append(f"{rel}: em- or en-dash present")
    for term in ("shape", "honest", "load bearing", "load-bearing"):
        n = len(re.findall(term, text, re.I))
        if n:
            banned_hits.setdefault(term, []).append((rel, n))
    # internal md links resolve
    for link in LINK.findall(text):
        if link.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = link.split("#")[0].split("?")[0]
        if not target.endswith(".md"):
            continue
        full = os.path.normpath(os.path.join(os.path.dirname(path), target))
        if not os.path.exists(full):
            problems.append(f"{rel}: broken internal link {link}")

def check_section_page(path):
    """Category index page: front matter, no type field, no article tags by
    rule, dash bans, links resolve."""
    with open(path) as f:
        text = f.read()
    rel = os.path.relpath(path, ROOT)
    fm = front_matter(text)
    if fm is None:
        problems.append(f"{rel}: front matter missing/unparsable")
        fm = ""
    if re.search(r"^type:", fm, re.M):
        problems.append(f"{rel}: forbidden type field")
    if "\u2014" in text or "\u2013" in text:
        problems.append(f"{rel}: em- or en-dash present")
    for link in LINK.findall(text):
        if link.startswith(("http://", "https://", "mailto:", "#")):
            continue
        target = link.split("#")[0].split("?")[0]
        if not target.endswith(".md"):
            continue
        full = os.path.normpath(os.path.join(os.path.dirname(path), target))
        if not os.path.exists(full):
            problems.append(f"{rel}: broken internal link {link}")

def table_rows(text, title):
    rows = []
    for line in text.splitlines():
        s = line.strip()
        if s.startswith("|") and s.endswith("|"):
            rows.append(s)
    return rows

def split_cells(row):
    return [c.strip() for c in row.strip().strip("|").split("|")]

for cat in CATS:
    catdir = os.path.join(ROOT, cat)
    all_note_files = [n for n in sorted(glob.glob(os.path.join(catdir, "*", "index.md")))
                      if "/_index/" not in n and "-feature-matrix/" not in n]
    notes = all_note_files
    slugs = sorted(os.path.dirname(n).rsplit("/", 1)[-1] for n in notes)
    for n in notes:
        check_file(n, research_note=True)
    # category index page (a section page: no article tags by rule)
    idx = os.path.join(catdir, "_index.md")
    if not os.path.exists(idx):
        problems.append(f"{cat}: missing category index page")
    else:
        check_section_page(idx)
        with open(idx) as f:
            itext = f.read()
        linked = []
        for m in re.finditer(r"^- \[([^\]]+)\]\(([^)]+)\)", itext, re.M):
            target = m.group(2)
            if target.endswith("_index.md") or target.startswith("http"):
                continue
            mm = re.match(r"([^/]+)/index\.md$", target)
            if mm:
                linked.append((m.group(1), mm.group(1)))
        linked_slugs = [s for _, s in linked]
        if sorted(linked_slugs) != slugs:
            missing = set(slugs) - set(linked_slugs)
            extra = set(linked_slugs) - set(slugs)
            problems.append(f"{cat}/_index.md: entry list mismatch (missing {sorted(missing)}, extra {sorted(extra)})")
        titles = [t for t, _ in linked]
        if titles != sorted(titles, key=str.casefold):
            problems.append(f"{cat}/_index.md: entries not alphabetical by displayed title")
    # feature matrix
    mats = sorted(glob.glob(os.path.join(catdir, "*feature-matrix", "index.md")))
    if not mats:
        problems.append(f"{cat}: missing feature matrix")
    for mat in mats:
        check_file(mat, research_note=False)
        with open(mat) as f:
            mtext = f.read()
        rows = table_rows(mtext, mat)
        if len(rows) < 2:
            problems.append(f"{cat}: matrix has no table")
            continue
        header = split_cells(rows[0])
        sep = split_cells(rows[1])
        if len(sep) != len(header):
            problems.append(f"{cat}: matrix separator row width {len(sep)} != header {len(header)}")
        for r in rows[2:]:
            cells = split_cells(r)
            if len(cells) != len(header):
                problems.append(f"{cat}: matrix row width {len(cells)} != header {len(header)}: {cells[:2]}...")
        col_slugs, col_titles = [], []
        for cell in header[1:]:
            m = re.match(r"(.*)\]\(([^)]+)\)$", cell)
            if not m:
                m2 = re.match(r"\[([^\]]+)\]\(([^)]+)\)", cell)
                if not m2:
                    problems.append(f"{cat}: matrix header cell not a link: {cell}")
                    continue
                m = m2
            col_titles.append(m.group(1).strip())
            t = m.group(2)
            mm = re.search(r"([^/]+)/index\.md$", t)
            col_slugs.append(mm.group(1) if mm else t)
        if col_slugs:
            if sorted(col_slugs) != slugs:
                missing = set(slugs) - set(col_slugs)
                extra = set(col_slugs) - set(slugs)
                problems.append(f"{cat}: matrix membership mismatch (missing {sorted(missing)}, extra {sorted(extra)})")
            if col_titles != sorted(col_titles, key=str.casefold):
                problems.append(f"{cat}: matrix columns not sorted by title")

# section-root articles (essay dirs and the root matrices at root)
for d in sorted(glob.glob(os.path.join(ROOT, "*", "index.md"))):
    rel = os.path.relpath(os.path.dirname(d), ROOT)
    if rel in CATS or rel == "worklists":
        continue
    check_file(d, research_note=False)

print(f"categories: {len(CATS)}")
print(f"problems: {len(problems)}")
for p in problems:
    print("  PROBLEM:", p)
for term, hits in banned_hits.items():
    total = sum(n for _, n in hits)
    print(f"banned-term '{term}': {total} hits in {len(hits)} files (documented exceptions left in place)")
sys.exit(1 if problems else 0)
