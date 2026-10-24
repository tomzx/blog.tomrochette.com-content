#!/usr/bin/env python3
"""Fetch the owner's GitHub stars newer than a checkpoint and emit a compact list.

Reads the checkpoint from --checkpoint (a file holding one ISO 8601 UTC
timestamp, the format of agents/starred-checkpoint.txt). Fetches pages of
https://api.github.com/users/tomzx/starred newest-first with the
application/vnd.github.star+json media type so each entry carries
starred_at, and stops at the first entry whose starred_at is at or before
the checkpoint. Emits one compact JSON object per star (repo, description,
starred_at, stars, pushed_at, url) and optionally writes the new checkpoint.

Usage:
  agents/scripts/fetch_stars.py [--checkpoint FILE] [--out FILE] [--max-pages N]
                               [--write-checkpoint FILE]
"""
import argparse, json, os, subprocess, sys
from datetime import datetime, timezone


def gh(path):
    r = subprocess.run(
        ["gh", "api", path, "-H", "Accept: application/vnd.github.star+json"],
        capture_output=True, text=True, timeout=60,
    )
    if r.returncode != 0:
        sys.stderr.write(r.stderr)
        return None
    try:
        return json.loads(r.stdout)
    except json.JSONDecodeError:
        return None


def parse_ts(s):
    if not s:
        return None
    return datetime.fromisoformat(s.replace("Z", "+00:00"))


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--checkpoint", help="file with one ISO 8601 UTC timestamp")
    p.add_argument("--out", help="output file (default: stdout)")
    p.add_argument("--max-pages", type=int, default=10)
    p.add_argument("--write-checkpoint", help="file to write the newest starred_at to")
    args = p.parse_args()

    checkpoint = None
    if args.checkpoint and os.path.exists(args.checkpoint):
        checkpoint = open(args.checkpoint, encoding="utf-8").read().strip() or None
    cp_dt = parse_ts(checkpoint) if checkpoint else None

    results = []
    newest = None
    page = 1
    stop = False
    while page <= args.max_pages and not stop:
        data = gh(f"users/tomzx/starred?per_page=100&sort=created&direction=desc&page={page}")
        if not data:
            break
        for entry in data:
            starred_at = entry.get("starred_at")
            repo = entry.get("repo") or {}
            if newest is None and starred_at:
                newest = starred_at
            if cp_dt is not None and starred_at and parse_ts(starred_at) and parse_ts(starred_at) <= cp_dt:
                stop = True
                break
            results.append({
                "repo": repo.get("full_name"),
                "description": (repo.get("description") or "").replace("\n", " ").strip(),
                "starred_at": starred_at,
                "stars": repo.get("stargazers_count"),
                "pushed_at": (repo.get("pushed_at") or "")[:10] or None,
                "url": repo.get("html_url"),
                "archived": bool(repo.get("archived")),
            })
        page += 1
        if len(data) < 100:
            break

    out = json.dumps(results, separators=(",", ":"), ensure_ascii=False)
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(out + "\n")
    else:
        print(out)

    if args.write_checkpoint and newest:
        os.makedirs(os.path.dirname(os.path.abspath(args.write_checkpoint)), exist_ok=True)
        with open(args.write_checkpoint, "w", encoding="utf-8") as f:
            f.write(newest + "\n")
    sys.stderr.write(f"fetch_stars: {len(results)} new stars" + (f", checkpoint {newest}" if newest else "") + "\n")


if __name__ == "__main__":
    main()
