#!/usr/bin/env python3
"""Fetch a URL and emit condensed text for an agent to read.

Strips HTML tags, collapses whitespace, and truncates to --max-chars so a
worker can verify or extract facts without ingesting a full page. With
--extract prices, emits only lines containing currency amounts.

Usage:
  agents/scripts/fetch_url_text.py URL [--max-chars N] [--out FILE] [--extract prices]
"""
import argparse, os, re, sys, urllib.request


def fetch(url):
    req = urllib.request.Request(url, headers={"User-Agent": "agents-preprocess/1.0"})
    with urllib.request.urlopen(req, timeout=30) as r:
        raw = r.read()
        ctype = r.headers.get("Content-Type", "")
    try:
        text = raw.decode("utf-8")
    except UnicodeDecodeError:
        text = raw.decode("latin-1")
    return text, ctype


def strip_html(text):
    text = re.sub(r"<script[^>]*>.*?</script>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<style[^>]*>.*?</style>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"&nbsp;", " ", text)
    text = re.sub(r"&amp;", "&", text)
    text = re.sub(r"&lt;", "<", text)
    text = re.sub(r"&gt;", ">", text)
    text = re.sub(r"\s+", " ", text).strip()
    return text


def main():
    p = argparse.ArgumentParser()
    p.add_argument("url")
    p.add_argument("--max-chars", type=int, default=4000)
    p.add_argument("--out")
    p.add_argument("--extract", choices=["prices"])
    args = p.parse_args()

    text, ctype = fetch(args.url)
    if "html" in ctype.lower() or "<" in text[:200]:
        text = strip_html(text)

    if args.extract == "prices":
        price_re = re.compile(r"(?:\$|USD|EUR|£)\s?\d[\d,]*(?:\.\d{2})?|\d[\d,]*(?:\.\d{2})?\s?(?:USD|EUR|GBP|/mo|/month|/yr|/year)", re.I)
        lines = [ln for ln in text.split(".") if price_re.search(ln)]
        text = ". ".join(lines).strip()
        if not text:
            text = text[:0]

    text = text[: args.max_chars]
    if args.out:
        os.makedirs(os.path.dirname(os.path.abspath(args.out)), exist_ok=True)
        with open(args.out, "w", encoding="utf-8") as f:
            f.write(text + "\n")
    else:
        print(text)
    sys.stderr.write(f"fetch_url_text: {len(text)} chars from {args.url}\n")


if __name__ == "__main__":
    main()
