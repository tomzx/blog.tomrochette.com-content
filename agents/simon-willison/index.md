---
title: Simon Willison
created: 2026-08-29
updated: 2026-08-29
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=big-pickle, people, publications, developer, llm-practitioner]
readability: 3
audience_notes: >
  Engineers already using daily coding agents who want a single dense feed that tracks the tool-and-model churn in real time.
  Assumes you know who Simon Willison is: the Django co-creator who turned his blog into the reference signal on practical LLM tooling.
---

Simon Willison's Weblog is the densest real-time record of what software engineers can actually do with LLMs, published daily by someone who uses them in his own practice.
Facts below verified as of 2026-09-02.

**No other voice tracks the tool-and-model churn of agentic development day-by-day with the same density and the same willingness to name what is hype; if you follow one feed for this domain, this is the one.**

## What it is

A long-running personal blog, plus a companion TIL site and a monthly sponsor-funded digest, written by Simon Willison, the Django co-creator and author of Datasette and the LLM CLI.
He writes first-person, every day, about models, coding agents, MCP, sandboxing, and Python tooling, usually from direct hands-on use rather than press releases.
He coined the widely quoted framing of LLMs as a "weird, over-confident intern" and maintains an [Agentic Engineering Patterns](https://simonwillison.net/tags/agentic-engineering/) stream that distills working practice.

## Status

Active and as influential as ever.
As of 2026-09-02 the homepage shows multiple posts a day through 1 September 2026, with dedicated tag streams for agentic-engineering, coding-agents, and ai-assisted-programming.
He ships code on the blog too: the sqlite-utils 4.0 release notes record that much of it was written by a coding agent, so the blog is documentation of his own agent loops, not just commentary on them.

## Strengths

- Daily cadence means he catches and explains changes while they are still news, not after they settle into a retrospective.
- He uses the tools he writes about: agent-written releases, sandboxed agent experiments, and prompt-injection testing all appear as first-hand notes.
- The tag archives (agentic-engineering, code-review, sandboxing) act as a searchable playbook, not just a feed.
- Repeatedly surfaces skeptical and security-critical coverage, from prompt-injection results to supply-chain attacks.

## Cautions

- Volume is high; without a filter the firehose buries the signal, which is why the sponsor digest exists.
- Coverage is Python-and-open-source weighted, so the IDE-centric and enterprise story gets less depth.
- He is a tool builder (LLM, Datasette) which biases the notes toward command-line, open, and local workflows.

## Pricing

Free to read.
The blog is sponsor-funded (GitHub sponsors at $10/month buy a monthly curated digest), with no paywall on the core feed.

## Compared to

- [Latent Space](../latent-space/index.md): the podcast-and-conference synthesis of the same landscape; read Willison for the day-to-day working notes, listen to Latent Space for the interviews and the industry view.
- [Steve Yegge](../steve-yegge/index.md): the provocative thesis-setter versus the reliable daily chronicler; Yegge declares, Willison documents.
- [The Pragmatic Engineer](../the-pragmatic-engineer/index.md): engineering-org and industry analysis versus hands-on tool notes; Orosz for the org, Willison for the terminal.

## Bottom line

**Recommended for any engineer who works with LLMs daily and wants a low-DSP, high-signal feed plus a searchable archive of working patterns.**
Not for people who prefer periodic synthesis over daily volume, or who want a vendor-neutral enterprise take.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the map his daily notes keep current
- [Context Management Patterns](../context-management-patterns/index.md) - a pattern stream he has written into explicitly
- [Model Selection for Coding Tasks](../model-selection-for-coding-tasks/index.md) - the model churn he reports on daily, distilled to a process
- [The Codebase Gardener](../../the-codebase-gardener/index.md) - the human role his hands-on notes presuppose

## References

- https://simonwillison.net/ - the blog: daily entries, tag streams, and the current-model testing notes
- https://til.simonwillison.net/ - the Today I Learned companion archive
- https://llm.datasette.io/ - the LLM CLI he builds and documents on the blog
- https://simonwillison.net/2026/Jan/8/llm-predictions-for-2026/ - his annual predictions, including the coding-agent predictions central to this domain
- https://simonwillison.net/guides/agentic-engineering-patterns/ - his distilled agentic engineering patterns
- https://arstechnica.com/ai/2025/03/is-vibe-coding-with-ai-gnarly-or-reckless-maybe-some-of-both/ - a critical press take on vibe coding that quotes his views
