---
title: AGENTS.md
created: 2026-08-24
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, protocols, conventions, context-files]
readability: 3
audience_notes: >
  Engineers who maintain repositories that coding agents work in and are deciding how to instruct those agents.
  Assumes you have used at least one coding agent and know what a repo-level instruction file is.

---

AGENTS.md is an open convention for a Markdown file at the repository root that carries project-specific instructions for coding agents.
Facts below verified as of 2026-09-04.

**It won the instruction-file format war in under a year, and that matters more than any single tool choice because the file outlives every agent that reads it.**

## What it is

Plain Markdown with no required fields: build and test commands, code style, PR conventions, anything you would tell a new teammate.
Nested AGENTS.md files scope instructions per package, the nearest file wins, and explicit chat prompts override everything.
It emerged from collaboration across OpenAI Codex, Amp, Jules, Cursor, and Factory, went public on 2025-08-20, and **OpenAI donated it to the Linux Foundation's Agentic AI Foundation on 2025-12-09, where it is stewarded as an open format**.
The reference repository (MIT, about 24.0k stars as of 2026-09-02) mostly holds the website; the format itself is the convention.

## Status

**Active and effectively the standard.**
The official site counts more than 60,000 open-source projects carrying an AGENTS.md as of 2026-09-02.
Adopters include Codex, Gemini CLI, Cursor, GitHub Copilot's coding agent, Amp, Jules, Factory, goose, opencode, Zed, Warp, VS Code, Devin, Junie, Windsurf, and Aider.
In this index, [Codex](../codex/index.md) treats it as first-class, [OpenCode](../opencode/index.md) reads it alongside CLAUDE.md, and [Crush](../crush/index.md) initializes projects with one.
The glaring exception is [Claude Code](../claude-code/index.md): its AGENTS.md support request only reached the HN front page in August 2026, and version 2.1.207 still ignored the file per the July 2026 proxy study cited in that note.
On 2026-08-17 that request (6,500+ reactions) was closed as completed with only a community binary patch linked, no native support has shipped in the changelog, and commenters quote an Anthropic engineer saying easy AGENTS.md use is coming.

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

## See also

- [Model Context Protocol](../mcp/index.md) - the other convention agents consume, for tools rather than instructions
- [Codex](../codex/index.md) - the harness that popularized the format
- [Claude Code](../claude-code/index.md) - the major holdout on native support
- [OpenCode](../opencode/index.md) - reads both AGENTS.md and CLAUDE.md

## References

- https://agents.md - official site: format, nested scoping, adopter list, AAIF stewardship
- https://github.com/agentsmd/agents.md - MIT repository, stars as of 2026-09-02
- https://aaif.io/press/linux-foundation-announces-the-formation-of-the-agentic-ai-foundation-aaif-anchored-by-new-project-contributions-including-model-context-protocol-mcp-goose-and-agents-md/ - OpenAI donation, 60,000+ project adoption
- https://arxiv.org/abs/2602.11988 - empirical evaluation: no general success-rate gain, over 20% added inference cost
- https://vercel.com/blog/agents-md-outperforms-skills-in-our-agent-evals - counter-evidence: 100% versus 53% with a compressed docs index
- https://github.com/anthropics/claude-code/issues/6235 - Claude Code support request, front-page traction in August 2026, closed 2026-08-17 as completed via a community patch
