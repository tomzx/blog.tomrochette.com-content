---
title: deja
created: 2026-10-10
updated: 2026-10-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, memory, session-memory, transcripts, retrieval, mcp, open-source]
readability: 3
audience_notes: >
  Engineers running several coding agents who want cross-agent memory without installing
  a capture step, profiled against the capture-based plugins and the curated local stores.
  Assumes you know what MCP and BM25-style lexical search are.
---

deja (published as the deja-vu repository) is an MIT-licensed local memory tool for coding agents: a single Go binary that indexes the session transcripts your agents already write to disk, strips credentials on the way in, and serves recall back to any of them over one MCP tool, hooks, and a search skill.

**Its bet is that the capture step is the mistake: forty-three harnesses already save complete session records to disk, so memory can start full, months back, the moment you install it.**

## What it is

A Go CLI from Vladislav Shulcz (curl script, Homebrew, Scoop, winget, npm, or go install) that parses each harness's own store in place (Claude Code JSONL, Codex sessions, Cursor's SQLite, and 40 more per its format registry) and builds a local inverted index under ~/.cache/deja with incremental per-file state.
Recall is lexical by default with no model and no network; an optional semantic sidecar points at any local Ollama or OpenAI-compatible embedding endpoint.
The MCP server exposes a single tool (the README counts its definitions at 477 tokens per turn) covering recall, blame, fix, how, orient, remember, and handoff modes, and `deja install` wires recall hooks and guidance blocks into the 43 supported harnesses.
Beyond search it adds `deja promote` (curated notes with accepted and rejected lifecycle states that outrank raw hits), credential redaction with a scrub command, ssh sync between your own machines, and a docs site carrying per-harness memory guides.

## Status

**Young, fast-moving, and single-maintainer, with adoption ahead of any public discussion.**
1,206 stars and 120 forks as of 2026-10-16 (GitHub API), created 2026-07-14, pushed 2026-10-28, MIT, with 77 open issues and pull requests as of 2026-10-19 (GitHub API).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=vshulcz/deja-vu&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=vshulcz/deja-vu&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=vshulcz/deja-vu&type=date&legend=top-left" />
</picture>

Latest release v0.23.2 (2026-10-28), the eleventh of the October train (v0.21.4 through v0.23.2).
v0.23.1 halves the cold-build peak again (4.7 GB instead of 9.4 GB on a 40,000-session store), cuts redaction CPU 17x with the same output, and fixes a quadratic slowdown a search over many look-alike sessions hit; it adds MiniMax Code as the forty-third wired harness, project aliases in `~/.config/deja/projects` that name a directory tree as one project so every checkout and worktree under it shares one scope, and `deja search --sort date`.
v0.23.0 makes big stores cheap to keep current: an update pass appends the records of rewritten sessions instead of rewriting the whole log and reads only what changed, cutting a 20-transcript update from 24 seconds to 1.7 and peak memory from 7 GB to under 1 GB on a 40,000-session store, and a common-word search answers in about a second instead of 24; it treats sub-agents as sessions of their own in every reader that marks one, forks no longer take credit for what they copied, and recalled history can no longer run a command in opencode or end a dsh turn, with the index rebuilt once on upgrade and `DEJA_NO_AUTO_INDEX` plus `DEJA_SEARCH_ONLY` for busy machines.
v0.22.1 makes session playback show the code each edit changed, line by line, for Claude Code, Codex, and every harness whose transcript holds its edit calls, adds `deja resume <id> --app` to open a Codex session in the ChatGPT desktop app, cuts session start to 0.38 seconds and the per-prompt hook to 0.59 seconds on a 19,000-session index (from 1.46 and 1.65), masks secrets that slipped past redaction, and moves the index version to 70, so the store rebuilds once on the first run after upgrading.
v0.22.2 decrypts, authenticates, and indexes Windsurf and Devin Desktop's encrypted Cascade conversation files, taking the wired-harness count to 42, adds `deja delete` to erase a session from its agent and from deja after asking, and rebuilds Claude Code sessions whose transcript is gone as their prompts from `history.jsonl`.
The post-v0.23.1 train (about fifteen commits on 2026-10-27 and 28, previously tracked unreleased) shipped as v0.23.2: recall injection gated to prompts that name something the history holds, answers served from the previous index during rebuilds, a late MCP recall answer handed on with the next tool call, three regressions against 0.23.1 caught by replaying a real store, default source locations for copilot-chat, roo, kilocode, and cherrystudio, and the configurable MCP deadline.
On top of those, v0.23.2 doubles recall speed and shrinks the index a third with unchanged answers (on a 19,000-session store, MCP recall p50 drops from 170 to 85 ms and the index from 277 to 185 MB via 256-byte compressed records, while LongMemEval-S hit@1 ticks from 88.1 to 88.9), adds receipts provenance labeling (each recalled line is labeled by who wrote it, a model conclusion shows the command or edit behind it, and instructions no person in the project typed are cut to a placeholder), demotes recalled rules to untrusted reference data the agent asks before acting on, stops injecting recall blocks into spawned subagents (1,339 Claude Code subagents were handed a block over 60 days and none used it, and those blocks were 55 percent of all per-prompt recall), serves Qwen Code's External Context MCP profile through `deja mcp --context-search`, adds a Cursor marketplace plugin, and gains `DEJA_RECALL_GLOBAL` for ranking every project equally on request; unrelated per-prompt blocks fall from 171 to 51 across 240 replayed prompts.
I found no Hacker News thread for the tool through 2026-10-10 searches (the name collides with two decades of unrelated deja vu stories), so the 1.2k stars in three months rest on package managers, MCP registries, and its Awesome-Agent-Memory placement, the stars-ahead-of-discussion pattern this section has flagged across the category.

## Strengths

- **Retroactive memory is the differentiator**: it knows work from before you installed it, which no capture-based member here can offer at any price.
- The benchmark documentation is the category's most self-critical: runs committed as JSON artifacts with dataset hashes, a submission format so a rival's ranking can be scored by the same driver, and explicit warnings that LongMemEval is lexically tractable and that a number quoted without its question count looks like drift.
- Credential redaction at index time (provider keys, tokens, JWTs, PEM blocks) with a published redaction boundary, plus `deja secrets` to find and scrub what the source transcripts still hold.
- It survives harness cleanup and compaction: sessions indexed before Claude Code's 30-day transcript deletion stay searchable, and the docs measure what compaction itself keeps (77 percent of decisions, 0.2 percent of commands) against what deja hands back.

## Cautions

- **The headline numbers are self-run on the author's own harness**: the committed artifacts report LongMemEval-S 88.1 percent hit@1 on the cleaned 470-question set and 70.5 percent retrieval-only hit@1 on LoCoMo, while the README's headline table quotes 97.2 percent R@5 against named rivals (MemPalace 96.6, agentmemory 95.2) without an independent run behind either.
- Lexical retrieval loses where it says it loses: preference questions sit at 43.3 percent hit@1 and a whole-corpus search over 19,195 sessions lands near 19 percent, so the good numbers assume project scoping is doing its work.
- Parsing 43 supported harnesses' private store formats is a permanent maintenance treadmill; TRAE IDE's store is encrypted and only wired rather than read, and any harness that changes its session schema breaks its parser until the next release.
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
- 2026-10-18 - Recorded the v0.22.2 release (Windsurf and Devin Desktop's encrypted Cascade transcripts decrypted and indexed, `deja install windsurf` taking the wired-harness count from 41 to 42, and `deja delete` erasing a session from its agent and the index after asking); the harness count updated throughout, and the status line refreshed (pushed 2026-10-18, 74 open issues and PRs).
- 2026-10-22 - Recorded the v0.23.0 release: incremental index updates (a 20-transcript update on a 40,000-session store cut from 24 seconds to 1.7, peak memory from 7 GB to under 1 GB), sub-agents as first-class sessions, and the closure of the seam where recalled history could run a command in opencode or end a dsh turn.
- 2026-10-25 - Recorded the v0.23.1 release: MiniMax Code as the forty-third wired harness, project aliases under `~/.config/deja/projects`, `deja search --sort date`, the cold-build memory peak halved (4.7 GB versus 9.4 GB on 40,000 sessions), 17x cheaper redaction, and the quadratic look-alike-search fix; the harness count updated throughout, and the status push date refreshed to 2026-10-24.
- 2026-10-25 - Corrected the star-history chart fallback markup (the img fallback carried the dark-theme parameter; it now points at the default chart).
- 2026-10-26 - Corrected the star-history chart markup: the light-theme source carried the dark-theme parameter; it now points at the default chart.
- 2026-10-28 - Recorded the unreleased post-v0.23.1 main-branch train (about fifteen commits, 2026-10-27 and 28): recall injection gated to prompts that name something the history holds, answers served from the previous index during rebuilds, late MCP recall answers handed to the next tool call, three 0.23.1 regressions fixed via a real-store replay, default source locations for four more parsers, and the configurable MCP deadline; the push date refreshed to 2026-10-28.
- 2026-10-29 - The tracked train shipped as v0.23.2 (October 28), with additions: recall twice as fast and the index a third smaller on a 19,000-session store (MCP recall p50 170 to 85 ms, index 277 to 185 MB, LongMemEval-S 88.1 to 88.9), receipts provenance labeling (who wrote each line, the command or edit behind a model conclusion, instructions no person typed cut), recalled rules demoted to untrusted reference data, subagent recall injection stopped after a 60-day zero-use measurement, Qwen Code's External Context MCP profile, a Cursor marketplace plugin, and DEJA_RECALL_GLOBAL.

## See also

- [Memory Feature Matrix](../memory-feature-matrix/index.md) - the category comparison this note joins
- [agentmemory](../agentmemory/index.md) - the capture-based cross-agent server it benchmarks against
- [Engrim](../engrim/index.md) - the curated cross-CLI local store
- [claude-mem](../claude-mem/index.md) - the single-harness capture-and-compress leader
- [File-based agent memory](../file-based-agent-memory/index.md) - the convention whose rot problem the transcript index works around

## References

- https://github.com/vshulcz/deja-vu - repository, MIT, 1,169 stars, 112 forks, 11 open issues and PRs, created 2026-07-14, pushed 2026-10-10, as of 2026-10-11
- https://raw.githubusercontent.com/vshulcz/deja-vu/main/README.md - architecture, the 42-harness support matrix, the single-tool MCP surface, redaction, promote lifecycle, sync, install paths, and the comparison table
- https://api.github.com/repos/vshulcz/deja-vu/releases - the release train through v0.22.2 (2026-10-17)
- https://api.github.com/repos/vshulcz/deja-vu/license - the MIT license file, verified through the GitHub API
- https://vshulcz.github.io/deja-vu/ - the docs site: the 41-harness list, the no-capture positioning, and the per-harness memory guides
- https://vshulcz.github.io/deja-vu/guide/benchmarks.html - LongMemEval-S 88.1 percent cleaned-set hit@1, LoCoMo 70.5 percent retrieval-only hit@1, the committed run artifacts, the rival-submission format, and the self-critical readings
- https://hn.algolia.com/api/v1/search?query=deja-vu&tags=story - the footprint scan finding no thread for this tool (2026-10-10), only unrelated deja vu stories
