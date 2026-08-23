---
title: gh-cached - Browse GitHub issues and PRs without burning through your API rate limit
created: 2026-04-30
type: post
status: finished
tags: [go, github, cli, developer-tools, fully-ai-generated, llm=glm-5.1, llm=glm-5.3]
readability: 4
audience_notes: >
  Assumes the reader is a developer who uses the GitHub CLI regularly, has a GitHub token or `gh` installed, and has felt the API rate limit. No Go knowledge required.
---

> **Note (2026-07-02):** gh-cached has been merged into [ghx](https://github.com/tomzxcode/ghx).

I use the GitHub CLI (`gh`) heavily, and I kept hitting the API rate limit.
The pain is worst when I'm triaging issues across multiple repos or reviewing a backlog of PRs.
Every `gh issue list`, every `gh pr view`, every comment fetch costs API calls I don't need to spend.

I built [gh-cached](https://github.com/TomzxCode/gh-cached) to solve the rate limit problem.
**gh-cached is a standalone Go binary that wraps the GitHub GraphQL API and caches every response to disk, so subsequent commands read from the local cache instead of hitting GitHub again.**

## The problem

The official `gh` CLI is excellent, but it's designed for live, one-off interactions.
There's no built-in caching layer.
Running `gh issue list` twice in five minutes makes two API calls.
Browsing hundreds of issues with their comments in a large repository burns through the rate limit fast.

The problem gets worse when AI coding assistants query GitHub on my behalf.
Multiple agents, multiple tools, all hitting the same API.
**The rate limit becomes a real bottleneck.**

## How gh-cached works

```
go install github.com/tomzxcode/gh-cached@latest
```

The cache lives at `~/.cache/gh-cached/<host>/<owner>/<repo>`.
Each issue and PR is stored as its own JSON file, including all comments.

**Pre-populate the cache:**

```bash
gh-cached cache                          # current repo
gh-cached cache --repo cli/cli           # any repo
gh-cached cache --cache-duration 120     # fresh for 2 hours
```

**Browse issues and PRs from cache:**

```bash
gh-cached issue list                     # open issues
gh-cached issue list --state all         # everything
gh-cached issue list --label bug         # filter by label
gh-cached issue list --author alice      # filter by author
gh-cached issue view 42 --comments       # view with comments

gh-cached pr list --state merged         # merged PRs
gh-cached pr list --draft                # draft PRs only
gh-cached pr view 10 --comments          # view with comments
```

**When the cache is fresh, all filtering happens in-memory with zero API calls.**
When the cache is stale, gh-cached falls back to the GitHub API and updates the cache.

## Why a separate tool instead of a gh extension?

Two reasons.

First, gh-cached uses GraphQL under the hood, which lets the tool fetch issues and PRs with their comments in fewer round trips than the REST API the official CLI defaults to.
**The cache-then-filter pattern also means one pre-fetch can be sliced many ways without going back to GitHub.**

Second, independence.
gh-cached works with just a `GH_TOKEN` environment variable, or falls back to `gh auth token` if the GitHub CLI is already installed.
No plugin registration, no extension marketplace, just a binary to drop in your PATH.

## The caching strategy

The tool uses different strategies depending on the command:

- `cache` fetches everything (all states, with comments) and writes one JSON file per item.
  Skips items already cached within the `--cache-duration` window (default: 60 minutes).
- `issue list` / `pr list` reads cached files and filter in-memory when fresh.
  Falls back to the API with server-side filters when stale.
- `issue view` / `pr view` serves from the individual cached file if less than 60 minutes old.
  Otherwise fetches from the API and updates the cache.

**A single `gh-cached cache` run gives fast, offline-capable access to all issues and PRs for the next hour.**

## Authentication

Set the token in the environment:

```bash
export GH_TOKEN=ghp_...
or
export GITHUB_TOKEN=ghp_...
```

Or just have `gh` installed and authenticated: gh-cached will use `gh auth token` as a fallback.

## When gh-cached is useful

- **AI coding assistants** that query GitHub repeatedly.
  Pre-populate the cache once and let tools read from disk instead of making redundant API calls.
- **Repository triage** where hundreds of issues need scanning with different filters.
  One cache fetch, then instant in-memory filtering.
- **Working with multiple repositories** where context switches are frequent.
  Cache each repo once and browse offline.
- **Rate-limited environments** like CI pipelines or shared machines where every API call counts.

## What to Do Next

```bash
go install github.com/tomzxcode/gh-cached@latest
# or download a binary from https://github.com/TomzxCode/gh-cached/releases/tag/latest
gh-cached cache --repo your-org/your-repo
gh-cached issue list --state all
gh-cached pr list --state all
```
