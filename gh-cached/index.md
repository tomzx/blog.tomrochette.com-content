---
title: gh-cached - Browse GitHub issues and PRs without burning through your API rate limit
created: 2026-04-30
type: post
status: finished
tags: [go, github, cli, developer-tools]
readability: 4
---

If you use the GitHub CLI (`gh`) heavily, you've hit the API rate limit.
It's especially painful when you're triaging issues across multiple repos or reviewing a backlog of PRs.
Every `gh issue list`, every `gh pr view`, every comment fetch costs API calls you don't need to spend.

I built [gh-cached](https://github.com/TomzxCode/gh-cached) to solve this.
It's a standalone Go binary that wraps the GitHub GraphQL API and caches every response to disk.
Subsequent commands read from the local cache instead of hitting GitHub again.

## The problem

The official `gh` CLI is excellent, but it's designed for live, one-off interactions.
There's no built-in caching layer.
If you run `gh issue list` twice in five minutes, you make two API calls.
If you're working with a large repository and need to browse hundreds of issues with their comments, you'll burn through your rate limit fast.

This gets worse when you're using AI coding assistants that query GitHub on your behalf.
Multiple agents, multiple tools, all hitting the same API.
The rate limit becomes a real bottleneck.

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

When the cache is fresh, all filtering happens in-memory with zero API calls.
When it's stale, gh-cached falls back to the GitHub API and updates the cache.

## Why a separate tool instead of a gh extension?

Two reasons.

First, gh-cached uses GraphQL under the hood, which lets it fetch issues and PRs with their comments in fewer round trips than the REST API the official CLI defaults to.
The cache-then-filter pattern also means you can pre-fetch once and slice the data many ways without going back to GitHub.

Second, independence.
It works with just a `GH_TOKEN` environment variable or falls back to `gh auth token` if you already have the GitHub CLI installed.
No plugin registration, no extension marketplace, just a binary you drop in your PATH.

## The caching strategy

The tool uses different strategies depending on the command:

- `cache` fetches everything (all states, with comments) and writes one JSON file per item.
  Skips items already cached within the `--cache-duration` window (default: 60 minutes).
- `issue list` / `pr list` reads cached files and filters in-memory when fresh.
  Falls back to the API with server-side filters when stale.
- `issue view` / `pr view` serves from the individual cached file if less than 60 minutes old.
  Otherwise fetches from the API and updates the cache.

This means a single `gh-cached cache` run gives you fast offline-capable access to all issues and PRs for the next hour.

## Authentication

Set your token in the environment:

```bash
export GH_TOKEN=ghp_...
or
export GITHUB_TOKEN=ghp_...
```

Or just have `gh` installed and authenticated — gh-cached will use `gh auth token` as a fallback.

## When this is useful

- **AI coding assistants** that query GitHub repeatedly.
  Pre-populate the cache once and let tools read from disk instead of making redundant API calls.
- **Repository triage** where you need to scan hundreds of issues with different filters.
  One cache fetch, then instant in-memory filtering.
- **Working with multiple repositories** where you switch contexts frequently.
  Cache each repo once and browse offline.
- **Rate-limited environments** like CI pipelines or shared machines where every API call counts.

## Try it

```bash
go install github.com/tomzxcode/gh-cached@latest
# or curl/wget one of the binary from https://github.com/TomzxCode/gh-cached/releases/tag/latest
gh-cached cache --repo your-org/your-repo
gh-cached issue list --state all
gh-cached pr list --state all
```

[Repository and source code](https://github.com/TomzxCode/gh-cached)
