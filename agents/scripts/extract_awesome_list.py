#!/usr/bin/env python3
"""Extract repository entries from an 'awesome' list README.

Given an owner/repo (or a raw URL), fetches the README, parses markdown
links pointing at github.com/<owner>/<repo>, and emits a compact JSON array
of {repo, title, description}. The description is taken from the text after
the link on the same line when present. Results are deduplicated and sorted
by repo name. Pass --exclude with a file of repos (one per line) to drop
already-known entries.

Usage:
  agents/scripts/extract_awesome_list.py OWNER/REPO [--out FILE] [--exclude FILE]
  agents/scripts/extract_awesome_list.py --url https://raw.githubusercontent.com/.../README.md
"""
import argparse, json, os, re, subprocess, sys, urllib.request


def fetch_readme(repo):
    # try raw.githubusercontent.com first
    for branch in ("main", "master"):
        url = f"https://raw.githubusercontent.com/{repo}/{branch}/README.md"
        try:
            with urllib.request.urlopen(url, timeout=30) as r:
                return r.read().decode("utf-8", "replace")
        except Exception:
            continue
    # fall back to gh api
    r = subprocess.run(["gh", "api", f"repos/{repo}/readme", "--jq", ".content"],
                       capture_output=True, text=True, timeout=45)
    if r.returncode == 0 and r.stdout.strip():
        import base64
        try:
            return base64.b64decode(r.stdout.strip()).decode("utf-8", "replace")
        except Exception:
            pass
    sys.exit(f"could not fetch README for {repo}")


def fetch_url(url):
    with urllib.request.urlopen(url, timeout=30) as r:
        return r.read().decode("utf-8", "replace")


LINK_RE = re.compile(r"\[([^\]]+)\]\((https?://github\.com/([\w.\-]+/[\w.\-]+)[^)]*)\)")


def extract(text):
    seen = set()
    out = []
    for line in text.splitlines():
        for m in LINK_RE.finditer(line):
            title = m.group(1).strip()
            repo = m.group(3).strip().rstrip(".")
            if repo.lower() in {"topics", "sponsors", "features"}:
                continue
            if repo.count("/") != 1:
                continue
            if repo in seen:
                continue
            seen.add(repo)
            # description: rest of the line after the link
            after = line[m.end():].strip().lstrip("-").strip()
            # strip leading punctuation
            after = after.lstrip(":").strip() if after.startswith(":") else after
            desc = after[:200].strip()
            out.append({"repo": repo, "title": title, "description": desc})
    out.sort(key=lambda x: x["repo"].lower())
    return out


def main():
    p = argparse.ArgumentParser()
    p.add_argument("repo", nargs="?")
    p.add_argument("--url")
    p.add_argument("--out")
    p.add_argument("--exclude", help="file with repos to drop, one per line")
    args = p.parse_args()

    if args.url:
        text = fetch_url(args.url)
    elif args.repo:
        text = fetch_readme(args.repo)
    else:
        sys.exit("provide OWNER/REPO or --url")

    excluded = set()
    if args.exclude and os.path.exists(args.exclude):
        with open(args.exclude, encoding="utf-8") as f:
            for ln in f:
                s = ln.strip()
                if s and not s.startswith("#"):
                    excluded.add(s)

    results = [r for r in extract(text) if r["repo"] not in excluded]
    out = json.dumps(results, separators=(",", ":"), ensure_ascii=False)
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out + "\n")
    else:
        print(out)
    sys.stderr.write(f"extract_awesome_list: {len(results)} entries\n")


if __name__ == "__main__":
    main()
