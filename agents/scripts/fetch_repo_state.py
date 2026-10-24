#!/usr/bin/env python3
"""Batch-fetch compact state for a list of GitHub repositories.

For each repo (owner/name), fetches pushed_at, open issue count, star count,
archived flag, default branch, and the latest release tag + date. Emits a
compact JSON array (one object per repo) so a worker can compare against the
last-verified date without fetching each repo's full page.

Usage:
  agents/scripts/fetch_repo_state.py REPO [REPO ...] [--out FILE]
  agents/scripts/fetch_repo_state.py --file repos.txt [--out FILE]
"""
import argparse, json, os, subprocess, sys
from concurrent.futures import ThreadPoolExecutor


def gh(path):
    r = subprocess.run(["gh", "api", path], capture_output=True, text=True, timeout=45)
    if r.returncode != 0:
        return None
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return None


def state(repo):
    info = gh(f"repos/{repo}") or {}
    rel = gh(f"repos/{repo}/releases/latest")
    tag = None
    rel_date = None
    if isinstance(rel, dict):
        tag = rel.get("tag_name")
        rel_date = (rel.get("published_at") or rel.get("created_at") or "")[:10] or None
    return {
        "repo": repo,
        "pushed_at": (info.get("pushed_at") or "")[:10] or None,
        "stars": info.get("stargazers_count"),
        "open_issues": info.get("open_issues_count"),
        "archived": bool(info.get("archived")),
        "default_branch": info.get("default_branch"),
        "latest_release": tag,
        "latest_release_date": rel_date,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("repos", nargs="*")
    p.add_argument("--file", help="file with one owner/name per line")
    p.add_argument("--out", help="output file (default: stdout)")
    p.add_argument("--workers", type=int, default=8)
    args = p.parse_args()

    repos = list(args.repos)
    if args.file:
        with open(args.file, encoding="utf-8") as f:
            repos += [ln.strip() for ln in f if ln.strip() and not ln.strip().startswith("#")]
    repos = [r for r in repos if "/" in r]
    if not repos:
        sys.exit("no repos given")

    with ThreadPoolExecutor(max_workers=args.workers) as ex:
        results = list(ex.map(state, repos))

    out = json.dumps(results, separators=(",", ":"), ensure_ascii=False)
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out + "\n")
    else:
        print(out)
    sys.stderr.write(f"fetch_repo_state: {len(results)} repos\n")


if __name__ == "__main__":
    main()
