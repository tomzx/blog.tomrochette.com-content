---
title: OpenAI Deep Research
created: 2026-09-13
updated: 2026-09-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, automated-research, openai, research-agent]
readability: 3
audience_notes: >
  Engineers and researchers deciding when to delegate literature work to an agent and how much to trust the output.
  Assumes you use ChatGPT or an equivalent assistant regularly.
---

Deep Research is OpenAI's ChatGPT agent that autonomously browses the web for five to thirty minutes and returns a cited report, making it the mass-market version of the automated research loop.
Facts below verified as of 2026-09-18.

**Deep Research is the breadth-first half of automated research, and its failure mode is exactly the one that matters: fluent synthesis with no verifier behind it, so the human stays the judge.**

## What it is

An agent inside ChatGPT, launched February 3, 2025 on a specialized version of the o3 reasoning model.
It finds, analyzes, and synthesizes hundreds of online sources across text, images, and PDFs, cites the source for each claim, and produces a structured report.
A lightweight o4-mini-based variant followed in April 2025 for free users, and a February 2026 update rebased it on GPT-5.2 with source picking, site limiting, and connections to your own data through MCP servers.
As of 2026-09-18, access is plan-gated: limited on Free and Go, included on Plus, Business, and Enterprise, and at a higher "maximum" allowance on Pro.

## Status

Shipping and actively developed.
The launch benchmark run scored 26.6 percent on Humanity's Last Exam against 13 percent for o3-mini-high and 9.4 percent for DeepSeek R1, with critics noting the tool could search the web while the baseline models could not.
OpenAI itself flags that Deep Research sometimes hallucinates facts, draws incorrect inferences, and cites rumors without conveying uncertainty.
GPT-5.4 (March 2026) further improved deep research behavior and cut factual errors by a claimed 33 percent versus GPT-5.2, per OpenAI's own reporting.

## Strengths

- Compresses a breadth-first literature scan from days to minutes, with per-claim citations you can spot-check.
- MCP connectors let it read your private data sources, not just the open web.
- Zero harness work: the loop is productized, so the cost of trying it is a prompt.
- The 2026 steering controls (source picking, site limiting) are exactly the levers an engineer wants for scoped research.

## Cautions

- Verification remains human and slow: University of Surrey's Andrew Rogoyski warned that checking a Deep Research report can take many hours, which is the whole job restated.
- Terence Tao's real-world test on an open Erdős problem found the ChatGPT research tool mostly re-summarized the very web page it read and surfaced no new literature.
- Quota-metered, so heavy research use lands on the $200/month Pro tier.
- The benchmark numbers are vendor-run, and the web-search asymmetry makes cross-model comparisons shaky.

## Pricing

Included in ChatGPT plans with quotas that vary by tier, as of 2026-09-18.
At launch, Pro ($200/month) got 100 queries per month; the June 2025 published table was 250 for Pro, 25 for Plus and Team, and 5 lightweight queries for free users, and OpenAI has since moved to in-product counters and plan-level descriptions.

## Compared to

- [OpenAI for Science](../openai-for-science/index.md): the lab program that uses models like this for actual discovery claims; Deep Research is the tool tier.
- [Harmonic Aristotle](../harmonic-aristotle/index.md): a research agent with a machine checker behind it; Deep Research has citations, Aristotle has proofs.
- The formal-proof systems in this category: they add the verifier Deep Research lacks, which is why their outputs compound and Deep Research's need re-reading.

## Bottom line

**Recommended for scoped literature recon where you will verify the load-bearing claims yourself anyway.**
Not as a source of established fact: treat every report as a hypothesis list with references, as of 2026-09-18.

## Changes

- 2026-09-13 - Created as the productized-loop member of the new Automated research category.

## See also

- [Automated Research Feature Matrix](../automated-research-feature-matrix/index.md) - the category comparison this note joins
- [OpenAI for Science](../openai-for-science/index.md) - the lab program upstream of the product
- [FrontierHarness Eval](../../evaluation-review/frontierharness-eval/index.md) - why vendor-run benchmarks need independent verification
- [Model Selection for Coding Tasks](../../model-selection-for-coding-tasks/index.md) - the per-token economics behind quota-metered agents

## References

- https://en.wikipedia.org/wiki/Deep_research - launch history, model lineage, benchmarks, quotas, and the documented hallucination caveats
- https://www.theguardian.com/technology/2025/feb/03/openai-deep-research-agent-chatgpt-deepseek - launch coverage and the skeptical verification-cost analysis
- https://www.windowscentral.com/software-apps/openai-deep-research-blows-chatgpt-o3-mini-and-deepseek-out-of-the-water - the Humanity's Last Exam numbers and the web-search caveat
- https://en.wikipedia.org/wiki/GPT-5.4 - the March 2026 model generation and its deep-research improvements
- https://www.erdosproblems.com/forum/thread/124 - Tao's hands-on test of research tools finding no new literature
