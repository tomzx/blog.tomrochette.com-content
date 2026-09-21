---
title: AGENTS.md
created: 2026-08-24
updated: 2026-09-21
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, protocols, conventions, context-files]
readability: 3
audience_notes: >
  Engineers who maintain repositories that coding agents work in and are deciding how to instruct those agents.
  Assumes you have used at least one coding agent and know what a repo-level instruction file is.

---

AGENTS.md is an open convention for a Markdown file at the repository root that carries project-specific instructions for coding agents.
Facts below verified as of 2026-09-21.

**It won the instruction-file format war in under a year, and that matters more than any single tool choice because the file outlives every agent that reads it.**

## What it is

Plain Markdown with no required fields: build and test commands, code style, PR conventions, anything you would tell a new teammate.
Nested AGENTS.md files scope instructions per package, the nearest file wins, and explicit chat prompts override everything.
It emerged from collaboration across OpenAI Codex, Amp, Jules, Cursor, and Factory, went public on 2025-08-20, and **OpenAI donated it to the Linux Foundation's Agentic AI Foundation on 2025-12-09, where it is stewarded as an open format**.
The reference repository (MIT, about 24.5k stars as of 2026-09-21) mostly holds the website; the format itself is the convention.

## Status

**Active and effectively the standard.**
The official site counts more than 60,000 open-source projects carrying an AGENTS.md as of 2026-09-21.
Adopters include Codex, Gemini CLI, Cursor, GitHub Copilot's coding agent, Amp, Jules, Factory, goose, opencode, Zed, Warp, VS Code, Devin, Junie, Windsurf, and Aider.
In this index, [Codex](../../harnesses/codex/index.md) treats it as first-class, [OpenCode](../../harnesses/opencode/index.md) reads it alongside CLAUDE.md, and [Crush](../../harnesses/crush/index.md) initializes projects with one.
The last big holdout fell on 2026-09-18: Claude Code 2.1.277 added native AGENTS.md support, reading the file in any project without a CLAUDE.md, implemented as a built-in "mod" and not yet available on Bedrock, Vertex, or Foundry.
The history matters: the support request only reached the HN front page in August 2026, was closed as completed on 2026-08-17 with only a community binary patch linked, and commenters quoted an Anthropic engineer promising easy AGENTS.md use, which arrived a month later in the changelog.

## Strengths

- **Zero tooling, zero lock-in: a text file any agent can parse, which is why adoption outran every rival format.**
- Nested scoping makes monorepos workable (OpenAI's own repository carries 88 of them).
- A vendor-neutral home in the AAIF, alongside MCP and goose.
- Effective for the right content: Vercel's evals hit a 100% pass rate on Next.js 16 tasks with a compressed docs index in AGENTS.md, versus 53% baseline.

## Cautions

- **The evidence that AGENTS.md files help is weaker than the hype.**
  An ETH Zurich study (arXiv 2602.11988) found context files did not generally improve task success rates while raising inference cost by over 20%: instructions were followed, but repository overviews were not helpful.
- A bad file is worse than none, since stale instructions actively mislead agents, and practitioners have reported agents committing repo secrets into the file.
- Fragmentation persists: CLAUDE.md, GEMINI.md, and tool-specific rules coexist, and read quality varies by agent.
- Every token of the file rides along on every request, so length is a recurring cost.

## Pricing

**Free, MIT-licensed convention with nothing to buy.**
The real cost is maintenance discipline plus the per-request token overhead.

## Compared to

- CLAUDE.md and GEMINI.md: **same mechanism, vendor-scoped; AGENTS.md is the portable version most tools now read**.
- Agent Skills: on-demand knowledge packages; Vercel's evals found passive AGENTS.md context beat skills for framework knowledge.
- README.md: written for humans; AGENTS.md carries the operational detail (exact commands, gotchas) agents need.

## Bottom line

**Recommended for every repository an agent touches: commit one this week and keep it short and factual.**
The disagreeable part: I suspect most AGENTS.md prose is wasted tokens, and the defensible version of the advice is commands and conventions yes, repository overviews no.

## Changes

- 2026-08-24 - Created in the Protocols category seed.
- 2026-08-26 - Fixed the our-note antecedent to name the July 2026 proxy study and the Claude Code note, indented the ETH Zurich continuation, and added the updated field.
- 2026-09-21 - Claude Code shipped native AGENTS.md support in 2.1.277 (2026-09-18), so the holdout record moved from "no native support" to shipped-as-of-this-date, with the changelog and announcement added as references.

## See also

- [Model Context Protocol](../mcp/index.md) - the other convention agents consume, for tools rather than instructions
- [Codex](../../harnesses/codex/index.md) - the harness that popularized the format
- [Claude Code](../../harnesses/claude-code/index.md) - the former major holdout, native support shipped 2026-09-18
- [OpenCode](../../harnesses/opencode/index.md) - reads both AGENTS.md and CLAUDE.md

## References

- https://agents.md - official site: format, nested scoping, adopter list, AAIF stewardship
- https://github.com/agentsmd/agents.md - MIT repository, stars as of 2026-09-18
- https://aaif.io/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation-aaif-anchored-by-new-project-contributions-including-model-context-protocol-mcp-goose-and-agents-md/ - OpenAI donation, 60,000+ project adoption
- https://arxiv.org/abs/2602.11988 - empirical evaluation: no general success-rate gain, over 20% added inference cost
- https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals - counter-evidence: 100% versus 53% with a compressed docs index
- https://github.com/anthropics/claude-code/issues/6235 - Claude Code support request, front-page traction in August 2026, closed 2026-08-17 as completed via a community patch
- https://code.claude.com/docs/en/changelog - Claude Code changelog: 2.1.277 (2026-09-18) "Added AGENTS.md support: in a project with no CLAUDE.md, Claude Code reads AGENTS.md instead"
- https://simonwillison.net/2026/Sep/18/thariq-shihipar/ - the announcement quote: support built on Claude Code mods
- https://github.com/anthropics/claude-code/tree/main/mods/agents-md - the built-in agents-md mod in the Claude Code repository
