---
title: Continue
created: 2026-08-26
updated: 2026-09-05
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, llm=glm-5.3-flash, surfaces, ai-editors, open-source, byok]
readability: 3
audience_notes: >
  Engineers who used or evaluated Continue as an open-source Copilot alternative, and anyone studying how the extension-generation assistants ended.
  Assumes you know what a VS Code or JetBrains extension is and what BYOK means.
---

Continue was an Apache-2.0 open-source coding agent shipped as a VS Code extension, a JetBrains plugin, and a CLI; Cursor acquired it in June 2026 and the repository is now read-only with final 2.0.0 and 2.1.0 releases.
Facts below verified as of 2026-09-05.

**Its acquisition is the strongest evidence yet that a standalone open-source "Copilot alternative" extension was never a durable business, only a feature waiting to be absorbed, and Cursor bought the team, not the product.**

## What it is

**One config-driven agent across three surfaces**: the VS Code extension (4,073,489 marketplace installs as of 2026-09-05), a JetBrains plugin, and a CLI, all configured through YAML with rules, MCP servers, and any model provider you point it at.
Local models were a first-class path, with official guides for [Ollama](https://docs.continue.dev/guides/ollama-guide) and for running fully offline.
The final 2.x releases (2.0.0 and 2.1.0, both tagged 2026-06-19) removed anonymous telemetry and pulled out authentication entirely, leaving a self-hostable codebase with no account anywhere.

## Status

Dead as an independent, by acquisition.
The [homepage](https://www.continue.dev/) reads "Continue was acquired by Cursor", announced 2026-06-15 (the [HN thread](https://news.ycombinator.com/item?id=48548758) dates it).
The README states the repository "is no longer actively maintained and is read-only for all users", a notice that still stands even though the repo API recorded metadata pushes as recently as September 2026.
As of 2026-09-05 the repo shows about 35.8k stars and 5.3k forks, the docs remain online, and the marketplace extension still installs at a 3.3 average rating.
**A 2026-08-22 Ask HN titled "Continue coding agent is dead. Alternatives?" ([4 points](https://news.ycombinator.com/item?id=49398366)) is a fittingly quiet funeral for a tool with four million installs.**

## Strengths

- The only open-source assistant that spanned VS Code, JetBrains, and the terminal from one configuration.
- Genuinely provider-neutral: BYOK to any API, local models via Ollama, or fully offline.
- Its documentation set (custom code RAG, codebase awareness) remains some of the best practitioner writing on retrieval for coding agents, which is why this section still cites it.
- The final release stripped telemetry and auth, a cleaner end state than most sunsets leave behind.

## Cautions

- Unmaintained: no security fixes are coming, and the FAQ on the homepage is the whole support story.
- The 3.26 marketplace rating suggests the late-life quality drift that precedes most acquisitions.
- The docs are frozen but live, so every claim they ground is a snapshot, not a promise.
- New setups have no reason to start here; the acquisition FAQ points nowhere but Cursor.

## Pricing

Was free and open source with paid hub tiers earlier in its life.
Nothing is for sale anymore; the final 2.1.0 release needs no account or subscription for anything.

## Compared to

- [Cline](../cline/index.md): the extension-generation survivor that kept shipping instead of selling; the default open-source choice today.
- [VS Code + Copilot](../vscode-copilot/index.md): the incumbent Continue was built to undercut, now hosting rival agents as extensions itself.
- [Roo Code](../roo-code/index.md): the other 2026 death from the same extension generation, by pivot instead of acquisition.

## Bottom line

**Recommended as a codebase to read and fork, not a tool to adopt.**
I would not start a new project on it, but its docs and final release are a clean grave worth studying.
For the workflow it pioneered, use Cline or an ACP-speaking host.

## See also

- [Cline](../cline/index.md) - the surviving line of the extension generation
- [Roo Code](../roo-code/index.md) - the pivot death that completed the pattern
- [Semantic code search](../semantic-code-search/index.md) - grounded in Continue's retrieval decisions
- [Tree-sitter chunking](../tree-sitter-chunking/index.md) - its code RAG guide still ranks the strategies

## References

- https://www.continue.dev/ - the acquisition notice and FAQ
- https://github.com/continuedev/continue - README: read-only, final 2.1.0, telemetry and auth removed
- https://api.github.com/repos/continuedev/continue - stars, forks, last push date as of 2026-09-05
- https://news.ycombinator.com/item?id=48548758 - the June 15, 2026 acquisition thread
- https://news.ycombinator.com/item?id=49398366 - the August 2026 "dead, alternatives?" thread
- https://docs.continue.dev/guides/ollama-guide - the local-model path, still live
- https://marketplace.visualstudio.com/items?itemName=Continue.continue - install count and rating
