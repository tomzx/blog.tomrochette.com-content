---
title: ghx - A CLI for agentic code reviews on GitHub
created: 2026-05-27
type: post
status: finished
tags: [go, github, cli, developer-tools, ai, agents, fully-ai-generated, llm=glm-5.1]
---

I've been building AI agents that review pull requests, and the official `gh` CLI doesn't have what they need.
Agents can't leave inline comments on specific lines, can't manage pending reviews, and can't edit or delete comments.
These are table-stakes operations for any code review workflow, and they're only accessible through the GitHub web UI or the raw GraphQL API.

So I built [ghx](https://github.com/tomzxcode/ghx), a CLI designed to make agentic code reviews practical.

## What ghx does that gh doesn't

**Inline comments on files and lines.** The most fundamental operation for a code review agent: comment on a specific line of a diff.

```bash
$ ghx pr comment 42 --file src/main.go --line 10 --body "Nit: use fmt.Errorf"
Created inline comment on src/main.go:10 (thread PRRT_kwDOC0I7As5vKgVn)

$ ghx pr comment 42 --file src/main.go --line 10-15 --body "Consider extracting this"
Created inline comment on src/main.go:10-15 (thread PRRT_kwDOC0I7As5vKgVq)
```

File-level comments (without `--line`), top-level PR comments, and replies to existing threads are all supported.

**Pending reviews.** Accumulate review comments without submitting them immediately, then approve or comment when ready:

```bash
$ ghx pr comment 42 --file src/main.go --line 10 --body "Nit" --pending
Added pending inline comment on src/main.go:10 (thread PRRT_kwDOC0I7As5vKgVz, review PRR_kwDOC0I7As4B9Y2z)

$ ghx pr review submit 42 --event APPROVE --body "LGTM"
Submitted review PRR_kwDOC0I7As4B9Y2z as APPROVE
```

**Edit and delete comments.** Fix a typo or remove a comment. Use `ghx pr threads 42 --ids` to list IDs:

```bash
$ ghx pr threads 42 --ids
PRRT_kwDOC0I7As5vKgVn  src/main.go:10  [open]
  PRC_kwDOC0I7As5TKxYc  reviewer  Nit: use fmt.Errorf

  PRC_kwDOC0I7As5TKxYd  author  Good catch, will fix.
```

Then edit or delete:

```bash
$ ghx pr comment edit PRC_kwDOC0I7As5TKxYc --body "Use fmt.Errorf instead of errors.New"
Updated comment PRC_kwDOC0I7As5TKxYc

$ ghx pr comment delete PRC_kwDOC0I7As5TKxYc
Deleted comment PRC_kwDOC0I7As5TKxYc
```

**Review thread management.** List, filter, and inspect review threads:

```bash
$ ghx pr threads 42
src/main.go:10  [open]
  reviewer  Nit: use fmt.Errorf
  author    Good catch, will fix.

src/main.go:45-52  [resolved]
  reviewer  Consider extracting this into a helper
  author    Done in 3a1b2c4
```

Filter by state with `--state open`, `--state resolved`, or `--state all`.

**Issue comments and viewing.** Add, edit, and delete issue comments, and view issues with their full comment history:

```bash
$ ghx issue view 42
Fix race condition in worker pool  [open]  author

The worker pool has a race condition when multiple goroutines access
the shared counter without proper synchronization.

2 comment(s):

  contributor  I can reproduce this with `go test -race ./...`
  author       Fixed in #50

$ ghx issue comment 42 --body "This is fixed in #50"
Created comment IC_kwDOC0I7As5TKxZa on issue #42
```

## The stash system

ghx has a local stash system for review comments, modeled after `git stash`.

The main use case is enabling agents to batch many comments at once before submitting them all as a single review. Instead of making individual API calls per comment, an agent can stash comments locally and pop them into a pending review in one operation:

```bash
$ ghx pr comment 42 --file src/main.go --line 10 --body "Nit" --stash
Stashed comment on src/main.go:10 (stash@{0} now has 1 threads)

$ ghx pr comment 42 --file src/main.go --line 20-25 --body "Extract this" --stash
Stashed comment on src/main.go:20-25 (stash@{0} now has 2 threads)

$ ghx pr review stash list 42
stash@{0}:  2 threads, 2 comments
  src/main.go   10      1 comment(s)
  src/main.go   20-25   1 comment(s)

$ ghx pr review stash pop 42
Popped stash@{0} (2 threads, 2 comments) into review PRR_kwDOC0I7As4B9Y2z
```

It also solves a GitHub API constraint: you can't mix immediate comments with pending review comments on the same PR.
When you submit an immediate comment on a PR that has a pending review, ghx automatically stashes the pending review, submits the comment, and restores the pending review.
This means agents can use a push-pop workflow (stash, comment, comment, pop) instead of repeating push-comment-pop for every immediate comment.

The stash supports multiple entries, just like `git stash`: push, pop, drop, and list.

## Getting started

ghx is a single Go binary. Download the latest release from [GitHub](https://github.com/tomzxcode/ghx/releases), or install with Go:

```bash
go install github.com/tomzxcode/ghx@main
```

It picks up your existing `GH_TOKEN`, `GITHUB_TOKEN`, or `gh auth login` credentials. No extra configuration needed. All commands accept `--repo OWNER/REPO` or auto-detect from the current git remote.

ghx is [MIT-licensed](https://github.com/tomzxcode/ghx/blob/main/LICENSE) and written in Go with no runtime dependencies beyond the GitHub API.
