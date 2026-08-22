---
title: Crush
created: 2026-08-22
updated: 2026-08-22
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, coding-agents, harnesses, terminal, go]
readability: 3
audience_notes: >
  Terminal-heavy engineers evaluating Charm's LSP-enhanced coding agent.
  Assumes you know what a language server does and what FSL licensing means.

---

Crush is Charm's terminal coding agent: a single Go binary that pulls context from language servers, runs any provider including local models, and carries the FSL-1.1-MIT license.
Facts below verified as of 2026-08-22.

**Crush is the best-looking and most portable harness in the field, and a license plus an origin story that community has not forgotten will keep it the second choice for teams that audit provenance.**

## What it is

An LSP-enhanced TUI: language servers feed it context the way they would an IDE, on top of multi-model chat with mid-session model switching.
It speaks MCP (stdio, http, sse, with OAuth), supports the Agent Skills standard including Claude-format skill directories, and initializes projects with an AGENTS.md (plus CRUSH.md for Crush-specific rules).
Configuration is a crushrc, which is literally Bash, and its model catalog auto-updates from Catwalk, a community database.
It runs on macOS, Linux, Windows, Android, and the BSDs.

## Status

Active.
About 27.6k stars, 2.2k forks, and 4,032 commits as of 2026-08-22, launched July 30, 2025.
It is the continuation of the original opencode-ai repository: creator Kujtim Hoxha joined Charm, the repo moved with him, and after the dispute that split the community, Charm renamed it Crush while the other developers kept the OpenCode name.
Charm's own telling is "Crush, come home"; the other side's version lives in the launch thread.

## Strengths

- The LSP integration is the differentiator: definitions and diagnostics as context, not just grep.
- A Go binary with no runtime dependency chain, on more platforms than anyone else bothers to support.
- Reads AGENTS.md, CLAUDE.md conventions via global config, and even Cursor and Claude skill directories.
- FSL-1.1-MIT converts every version to real MIT two years after release.

## Cautions

- Not open source by OSI definitions: FSL restricts competing use for two years per version; some teams will fail policy on it.
- The 2025 fork fight (repository move, history edits alleged, name split) still colors trust, and you should read both accounts before standardizing on it.
- Launch-era reviews reported weaker planning, more tokens, and rough edges versus OpenCode; verify against current releases before relying on those impressions either way.
- No subscription login: providers need API keys, including Anthropic.
- crushrc is arbitrary shell code; the README itself warns not to launch Crush in an unreviewed directory.

## Pricing

The tool is free under FSL-1.1-MIT.
BYOK means your providers bill you directly; Charm sells Hyper, its own subscription provider with a free tier and zero data retention, pitched as the optimized default (per the README; no stable public pricing page existed at verification time).

## Compared to

- [OpenCode](../opencode/index.md): same ancestor, MIT, bigger community; the safer institutional pick.
- [aider](../aider/index.md): also BYOK, REPL-feel; choose aider when you want zero spectacle.
- [Claude Code](../claude-code/index.md): subscription platform; the comparison is polish versus portability.

## Bottom line

Recommended for terminal aesthetes, LSP lovers, and local-model users.
Not for license-restricted organizations or communities that relitigate 2025.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - Crush in the independent tail of the harness layer
- [Iterating on Agent Skills](../../iterating-on-agent-skills/index.md) - the skill format Crush adopted
- [The Shifting Bottleneck](../../the-shifting-bottleneck/index.md) - why context quality (LSP) matters more than generation
- [OpenCode](../opencode/index.md) - the sibling it split from

## References

- https://github.com/charmbracelet/crush - features, license, provider matrix, as of 2026-08-22
- https://news.ycombinator.com/item?id=44736176 - launch thread with the full origin story and early comparisons
- https://fsl.software/ - what FSL-1.1-MIT permits and when it converts
- https://charm.land/blog/crush-comes-home/ - Charm's account of the project joining the company
- https://github.com/charmbracelet/catwalk - the community model database behind provider auto-update
