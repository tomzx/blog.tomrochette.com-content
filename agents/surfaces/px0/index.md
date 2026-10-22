---
title: px0
created: 2026-10-11
updated: 2026-10-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, surfaces, code-review, browser-ide, go, open-source]
readability: 3
audience_notes: >
  Engineers whose day is mostly reading and reviewing what coding agents produce, deciding whether a browser review console can replace a full IDE.
  Assumes you know what a merge-base diff and a language server are.
---

px0 is Arpit Bhayani's MIT-licensed browser IDE for reviewing AI-generated code: one static Go binary serving read-first browsing, instant search, GitHub pull request review, and handoff to local coding harnesses over plain HTTP.

**Its bet is the inverted IDE: authoring happens in the terminal harness, so the editor's remaining job is reading, diffing, and approving, done at sub-millisecond start and a fraction of the heavyweight suite's memory.**

## What it is

A single Go binary with the web UI embedded (`go:embed`, no Electron, no Node, no CGO), installed by a curl script or built from source, that renders your working tree, any directory, or a GitHub pull request in the browser.
The review loop is the product: `px0 <pr-url>` opens scoped merge-base diffs in an ephemeral worktree, inline comments draft from the gutter, formal approvals submit to GitHub, and AI-generated commit messages and pushes go back to PR branches without a terminal.
Agent integration works through handoff rather than hosting: edits dispatch to Claude Code, Gemini CLI, Cursor Agent, Antigravity, OpenCode, Codex, Aider, or Goose per the README (the site headline counts four), with multi-turn agent threads anchored to code ranges, live tool-step streams over SSE, and queued batch inline edits with overlap protection.
Navigation targets the reading case: fuzzy file and symbol search, workspace regex, about 280 languages tokenized through Chroma, virtual rows that open 400,000-line files, optional zero-config LSP, and a remote-first mode (`px0 -host 0.0.0.0`) that serves any VM, container, or CI runner with path-traversal and DNS-rebinding guards, refusing agent edits through public tunnel hostnames.

## Status

**Young, fast-moving, and thin on independent validation.**
1,869 stars, MIT, written in Go, created 2026-06-24, pushed 2026-10-08, as of 2026-10-16 (GitHub API).
The release train is active: v0.1.11 through v0.1.16 landed between 2026-09-28 and 2026-10-03, v0.1.17 (October 18) followed with a hardened LSP client lifecycle fixing deadlocks and races, a committed-changes diff view, and a status-bar flicker fix, v0.1.18 (October 19, intra-line diff character highlighting with insertion carets, merged from the project's first outside pull request), and v0.1.19 (October 20) and v0.1.20 (October 21), two patch releases whose notes carry only changelog links, as the latest.
The Show HN thread (2026-09-13, submitted by the author) drew 7 points and 0 comments, and no third-party coverage surfaced this run, so the footprint is GitHub-side; the site's "engineers at" logo wall (Google, Meta, Stripe, and a dozen more) is unverifiable social proof, and a design-partner program is recruiting teams of ten plus.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=px0-ai/px0&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=px0-ai/px0&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=px0-ai/px0&type=date&legend=top-left" />
</picture>

## Strengths

- **Review is the product, not a panel: PR URLs open scoped merge-base diffs in milliseconds, comments draft inline, and fixes dispatch to your own harness with live reload, closing the loop without opening an IDE.**
- The performance discipline is measured, not vibed: benchmark scripts ship in the repo, and the memory accounting separates the 20 to 30 MB Go daemon from the browser tab's 80 to 150 MB, with idle memory returned to the kernel after 15 seconds.
- Remote-first without remote daemons: one static binary over HTTP on any box, sandboxed by architecture (traversal guards, origin checks, tunnel-hostname edit refusal).
- MIT end to end, read-first by default, no telemetry: the trust surface is auditable in an afternoon.

## Cautions

- **Independent validation is absent: one 7-point Show HN with no comments, no third-party review found this run, and self-run benchmark scripts as the only performance evidence.**
- v0.1.x at several releases per week is churn as the maintenance plan, and the editing model is deliberately constrained: read-first with agent-mediated writes, not a general editor.
- MCP and AGENTS.md support are undocumented anywhere this run could find, so harness-adjacent conventions stay outside the tool.
- The handoff list splits across sources (eight harnesses in the README, four on the site), and Codex is absent from the site's supported list, a gap for Codex-centric teams.
- One maintainer carries the whole stack, server, web UI, and the in-repo internals docs.

## Pricing

Free and open source under MIT, no account and no paid tier found as of 2026-10-11.
The design-partner program is a sales motion, not a price list, so no price history applies.

## Compared to

- [Whiteboard](../whiteboard/index.md): the other review-first surface; Whiteboard is a canvas the agent draws its work onto, px0 renders the codebase itself for review.
- [VS Code + Copilot](../vscode-copilot/index.md): the heavyweight default px0 benchmarks itself against; keep VS Code for extension breadth and general editing, pick px0 when the loop is read, diff, approve, dispatch.
- [OpenChamber](../openchamber/index.md): the session cockpit for driving agents; OpenChamber supervises the runs, px0 supervises the code those runs produce.

## Bottom line

**Recommended for engineers whose day is reviewing agent output across many repositories and remote boxes, who want it in a browser tab at trivial cost, and can accept v0.1.x with self-run benchmarks as the entire evidence file.**
Not for general-purpose editing, and not for teams that need independent validation before a review gate becomes habit.
My disagreeable claim: the read-only IDE is the correct end state for the agent era, and px0's existence argues the editor wars were always review wars wearing an editor costume.

## Changes

- 2026-10-11 - Created after the evaluation-review resolution routed the px0-ai/px0 candidate here as surfaces-kind, with the zero-coverage footprint recorded as the governing caution.
- 2026-10-18 - Recorded v0.1.17 (October 18, the LSP client-lifecycle hardening, a committed-changes diff view, and the status-bar flicker fix) as the new latest release.
- 2026-10-20 - Recorded v0.1.18 (October 19, intra-line diff character highlighting with insertion carets, from the first outside pull request) as the new latest release.
- 2026-10-22 - Recorded v0.1.19 (October 20) and v0.1.20 (October 21), patch releases whose notes carry no written changelog, as the new latest releases.

## See also

- [Whiteboard](../whiteboard/index.md) - the other review-first surface, a canvas where this is the codebase
- [VS Code + Copilot](../vscode-copilot/index.md) - the heavyweight default px0 benchmarks against
- [OpenChamber](../openchamber/index.md) - the session cockpit watching the runs px0 reviews
- [roborev](../../code-review/roborev/index.md) - the resident daemon automating the same commit-review loop
- [Surface Feature Matrix](../surface-feature-matrix/index.md) - the category comparison this note joins

## References

- https://github.com/px0-ai/px0 - repository, MIT, Go, 1,869 stars, created 2026-06-24, pushed 2026-10-08 (GitHub API, as of 2026-10-16)
- https://raw.githubusercontent.com/px0-ai/px0/HEAD/README.md - the feature set: PR review, harness handoff list, virtual rendering, remote mode, sandboxing, and the memory accounting
- https://px0.ai/ - the product site: the performance claims, the four-harness headline, the logo wall, and the design-partner program
- https://api.github.com/repos/px0-ai/px0/releases - the release train v0.1.11 through v0.1.16 (2026-09-28 to 2026-10-03), v0.1.17 (2026-10-18, LSP lifecycle hardening and the committed-changes diff view), v0.1.18 (2026-10-19, the intra-line diff highlighting pull request), and v0.1.19 and v0.1.20 (2026-10-20 and 2026-10-21) as the latest, re-fetched 2026-10-22
- https://hn.algolia.com/api/v1/items/49683668 - the Show HN thread: 7 points, 0 comments, 2026-09-13, the thin-footprint record
