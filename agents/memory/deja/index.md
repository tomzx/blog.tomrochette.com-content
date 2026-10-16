---
title: deja
created: 2026-10-10
updated: 2026-10-16
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, session-memory, transcripts, retrieval, mcp, open-source]
readability: 3
audience_notes: >
  Engineers running several coding agents who want cross-agent memory without installing
  a capture step, profiled against the capture-based plugins and the curated local stores.
  Assumes you know what MCP and BM25-style lexical search are.
---

deja (published as the deja-vu repository) is an MIT-licensed local memory tool for coding agents: a single Go binary that indexes the session transcripts your agents already write to disk, strips credentials on the way in, and serves recall back to any of them over one MCP tool, hooks, and a search skill.

**Its bet is that the capture step is the mistake: forty-one harnesses already save complete session records to disk, so memory can start full, months back, the moment you install it.**

## What it is

A Go CLI from Vladislav Shulcz (curl script, Homebrew, Scoop, winget, npm, or go install) that parses each harness's own store in place (Claude Code JSONL, Codex sessions, Cursor's SQLite, and 38 more per its format registry) and builds a local inverted index under ~/.cache/deja with incremental per-file state.
Recall is lexical by default with no model and no network; an optional semantic sidecar points at any local Ollama or OpenAI-compatible embedding endpoint.
The MCP server exposes a single tool (the README counts its definitions at 477 tokens per turn) covering recall, blame, fix, how, orient, remember, and handoff modes, and `deja install` wires recall hooks and guidance blocks into the 41 supported harnesses.
Beyond search it adds `deja promote` (curated notes with accepted and rejected lifecycle states that outrank raw hits), credential redaction with a scrub command, ssh sync between your own machines, and a docs site carrying per-harness memory guides.

## Status

**Young, fast-moving, and single-maintainer, with adoption ahead of any public discussion.**
1,206 stars, 120 forks, and 22 open issues and pull requests, created 2026-07-14, pushed 2026-10-16, MIT, as of 2026-10-16 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=vshulcz/deja-vu&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=vshulcz/deja-vu&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=vshulcz/deja-vu&type=date&theme=dark&legend=top-left" />
</picture>

Latest release v0.22.1 (2026-10-12) after a seven-release October train (v0.21.4 through v0.22.1 in fourteen days).
v0.22.1 makes session playback show the code each edit changed, line by line, for Claude Code, Codex, and every harness whose transcript holds its edit calls, adds `deja resume <id> --app` to open a Codex session in the ChatGPT desktop app, cuts session start to 0.38 seconds and the per-prompt hook to 0.59 seconds on a 19,000-session index (from 1.46 and 1.65), masks secrets that slipped past redaction, and moves the index version to 70, so the store rebuilds once on the first run after upgrading.
I found no Hacker News thread for the tool through 2026-10-10 searches (the name collides with two decades of unrelated deja vu stories), so the 1.2k stars in three months rest on package managers, MCP registries, and its Awesome-Agent-Memory placement, the stars-ahead-of-discussion pattern this section has flagged across the category.

## Strengths

- **Retroactive memory is the differentiator**: it knows work from before you installed it, which no capture-based member here can offer at any price.
- The benchmark documentation is the category's most self-critical: runs committed as JSON artifacts with dataset hashes, a submission format so a rival's ranking can be scored by the same driver, and explicit warnings that LongMemEval is lexically tractable and that a number quoted without its question count looks like drift.
- Credential redaction at index time (provider keys, tokens, JWTs, PEM blocks) with a published redaction boundary, plus `deja secrets` to find and scrub what the source transcripts still hold.
- It survives harness cleanup and compaction: sessions indexed before Claude Code's 30-day transcript deletion stay searchable, and the docs measure what compaction itself keeps (77 percent of decisions, 0.2 percent of commands) against what deja hands back.

## Cautions

- **The headline numbers are self-run on the author's own harness**: the committed artifacts report LongMemEval-S 88.1 percent hit@1 on the cleaned 470-question set and 70.5 percent retrieval-only hit@1 on LoCoMo, while the README's headline table quotes 97.2 percent R@5 against named rivals (MemPalace 96.6, agentmemory 95.2) without an independent run behind either.
- Lexical retrieval loses where it says it loses: preference questions sit at 43.3 percent hit@1 and a whole-corpus search over 19,195 sessions lands near 19 percent, so the good numbers assume project scoping is doing its work.
- Parsing 41 private store formats is a permanent maintenance treadmill; TRAE IDE's store is encrypted and only wired rather than read, and any harness that changes its session schema breaks its parser until the next release.
- Bus factor of one, three months old, and no independent evaluation or public discussion footprint yet.

## Pricing

Pricing does not apply: free and MIT, fully local, with no hosted tier.
The optional semantic sidecar bills your own embedding endpoint.

## Compared to

- [agentmemory](../agentmemory/index.md): the capture-based cross-agent server; agentmemory records observations going forward, deja indexes what already happened, and the two cite each other in their benchmark tables.
- [Engrim](../engrim/index.md): the other cross-CLI local store; Engrim curates what agents choose to save, deja keeps everything the agents wrote.
- [File-based agent memory](../file-based-agent-memory/index.md): the convention deja extends from rules to recall; its rot-without-pruning caution is the problem deja answers from the transcript side.

## Bottom line

**Recommended for engineers running two or more coding agents who want cross-agent recall with no capture step and will accept a young, single-maintainer tool with self-run benchmarks.**
Not for teams needing multi-user memory, audited third-party evaluation, or recall over harness stores deja cannot parse.

## Changes

- 2026-10-10 - Created from the 2026-10-10 Awesome-Agent-Memory entrant scan, with seven fetched sources and the self-run-benchmark-plus-no-discussion-footprint combination recorded as the critical angle.
- 2026-10-13 - Recorded the v0.22.1 release (session playback showing each edit's removed and added lines, `deja resume <id> --app` opening Codex sessions in the ChatGPT desktop app, session start cut to 0.38 seconds and the per-prompt hook to 0.59 seconds on a 19,000-session index, post-redaction secret masking, and the index-version-70 one-time rebuild), extending the October train to seven releases; refreshed stars to 1,183 and the push date to 2026-10-12.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [agentmemory](../agentmemory/index.md) - the capture-based cross-agent server it benchmarks against
- [Engrim](../engrim/index.md) - the curated cross-CLI local store
- [claude-mem](../claude-mem/index.md) - the single-harness capture-and-compress leader
- [File-based agent memory](../file-based-agent-memory/index.md) - the convention whose rot problem the transcript index works around

## References

- https://github.com/vshulcz/deja-vu - repository, MIT, 1,169 stars, 112 forks, 11 open issues and PRs, created 2026-07-14, pushed 2026-10-10, as of 2026-10-11
- https://raw.githubusercontent.com/vshulcz/deja-vu/main/README.md - architecture, the 41-harness support matrix, the single-tool MCP surface, redaction, promote lifecycle, sync, install paths, and the comparison table
- https://api.github.com/repos/vshulcz/deja-vu/releases - the release train through v0.22.1 (2026-10-12)
- https://api.github.com/repos/vshulcz/deja-vu/license - the MIT license file, verified through the GitHub API
- https://vshulcz.github.io/deja-vu/ - the docs site: the 41-harness list, the no-capture positioning, and the per-harness memory guides
- https://vshulcz.github.io/deja-vu/guide/benchmarks.html - LongMemEval-S 88.1 percent cleaned-set hit@1, LoCoMo 70.5 percent retrieval-only hit@1, the committed run artifacts, the rival-submission format, and the self-critical readings
- https://hn.algolia.com/api/v1/search?query=deja-vu&tags=story - the footprint scan finding no thread for this tool (2026-10-10), only unrelated deja vu stories
