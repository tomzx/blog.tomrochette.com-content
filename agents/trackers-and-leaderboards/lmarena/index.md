---
title: LMArena
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, trackers-and-leaderboards, evaluation, leaderboards, human-feedback]
readability: 3
audience_notes: >
  Engineers who want to know what LMArena's ranks measure, how they get gamed, and when a preference vote is the wrong number to trust.
  Assumes you know what a blind A/B comparison is.
---

LMArena ranks AI models by blind human preference votes: two anonymous models answer the same prompt, you pick the winner, and Bradley-Terry-style statistics turn millions of those picks into leaderboards spanning text, image, video, vision, search, web development, and agents.

**It is the field's mood ring: the most cited signal of which model people prefer, and the easiest leaderboard in existence to game.**

## What it is

A website (lmarena.ai), a family of leaderboards (Agent Overall, Text, WebDev, Image, Video, Vision, Document, Search), a WebDev arena (web.lmarena.ai), a blog, and open methodology repositories, run by Arena Intelligence Inc., the company that grew out of the UC Berkeley and LMSYS Chatbot Arena project.
The founding paper (arXiv:2403.04132, March 2024) describes the pairwise crowdsourcing method and 240K+ votes at the time; the leaderboard methodology source is published as the `arena-rank` repository, pushed August 2026.
The company raised $100M at a $600M valuation in May 2025, led by Andreessen Horowitz and UC Investments, and labs including OpenAI, Google, and Anthropic partner with it to put flagship models in front of voters.
Recent product motion includes AutoEval scores added to the leaderboards (to complement slowly collected human votes), agent leaderboard categories with task costs (August 2026), and a HarnessTax research post (September 2026).

## Status

The most-cited leaderboard in the field: a critical paper describing Chatbot Arena as "the go-to leaderboard for ranking the most capable AI systems" is itself the best evidence of that status.
The blog posts within days of verification, the arenas run continuously, and HN threads routinely open with its rankings as the premise.
The company is well capitalized and has converted the academic project into a venture-scale business, which is also the source of its hardest questions.

## Strengths

- Preference at scale is a measurement no benchmark suite replaces: it captures whatever makes people pick one answer over another, including style, format, and thoroughness.
- The methodology code and the voting procedure are public, so the statistics are checkable even when the data pipelines are not.
- The arena expansion (WebDev, agents, image, video) follows usage: it measures the surfaces people actually use models on.

## Cautions

- The gaming record is documented: Meta's Llama 4 Maverick episode (an "experimental chat version" tested on the arena that differed from the shipped model) forced a policy update, and LMArena's own statement conceded "Meta's interpretation of our policy did not match what we expect from model providers".
- The Leaderboard Illusion paper (arXiv:2504.20879) documents "undisclosed private testing practices" that "benefit a handful of providers", counting 27 private Meta variants tested before the Llama 4 release and sampling-rate asymmetries favoring closed models.
- The sharpest criticism (Surge AI's "LMArena is a cancer on AI", 246 points on HN in January 2026) argues the format "rewards superficiality over accuracy" because "the easiest way to climb the leaderboard isn't to be smarter; it's to hack human attention span".
- A preference rank is not a capability claim: verbosity and sycophancy win votes that lose tasks, so the number is routinely over-read by headlines.

## Pricing

Free to use and to vote.
No public pricing page exists; the company is venture funded, and its "Try Arena" product surfaces are free at the time of verification.
No reader-facing price is stated, so no price history applies.

## Compared to

- [Artificial Analysis](../artificial-analysis/index.md): controlled first-party evals with published weights; choose it when you need price and speed, the arena when you need preference.
- [OpenRouter Rankings](../openrouter-rankings/index.md): revealed preference (spend) versus stated preference (votes).
- [LLM Stats](../llm-stats/index.md): benchmark aggregation, which at least labels what it cannot verify.

## Bottom line

**Recommended as the fastest read on which models feel better to people, and as a required filter on any headline of the form "X tops the arena"; not as the number you commit money against.**
My disagreeable claim: the leaderboard is the least valuable thing the arenas produce, because the vote stream is quietly one of the largest human-feedback datasets ever assembled, and whoever holds it holds a training asset, not just a ranking.

## Changes

- 2026-09-24 - Created.
- 2026-09-26 - Removed the "Facts below verified as of" stamp per owner policy; the site is a client-rendered app, so vote and model counts beyond the founding paper's figures could not be read from its HTML.

## See also

- [Artificial Analysis](../artificial-analysis/index.md) - the controlled-eval counterpart to crowd preference
- [OpenRouter Rankings](../openrouter-rankings/index.md) - what people pay for, against what they vote for
- [Epoch AI](../epoch-ai/index.md) - the research-nonprofit model of measurement this company left behind
- [Trackers and Leaderboards Feature Matrix](../trackers-and-leaderboards-feature-matrix/index.md) - the category comparison this note joins
- [You Cannot Out-Review a Machine by Hand](../../../you-cannot-out-review-a-machine-by-hand/index.md) - human judgment as a bottleneck, applied to review instead of ranking

## References

- https://lmarena.ai/ - homepage meta: blind comparison, vote-driven leaderboards across text, image, and code (fetched 200, 2026-09-24)
- https://blog.lmarena.ai/ - Arena Intelligence Inc. identity, leaderboard families, 2026 post dates (fetched 200, 2026-09-24)
- https://blog.lmarena.ai/how-it-works/ - the vote flow and identity reveal procedure (fetched 200, 2026-09-24)
- https://arxiv.org/abs/2403.04132 - the founding paper: method and 240K+ votes (fetched 200, 2026-09-24)
- https://arxiv.org/abs/2504.20879 - The Leaderboard Illusion: private testing, 27 Meta variants, sampling asymmetries (fetched 200, 2026-09-24)
- https://techcrunch.com/2025/05/21/lm-arena-the-organization-behind-popular-ai-leaderboards-lands-100m/ - $100M seed, $600M valuation, investors, Berkeley origin (fetched 200, 2026-09-24)
- https://www.theverge.com/meta/645012/meta-llama-4-maverick-benchmarks-gaming - the Maverick gaming episode and LMArena's policy response (fetched 200, 2026-09-24)
- https://surgehq.ai/blog/lmarena-is-a-plague-on-ai - the strongest critical essay on the format (fetched 200, 2026-09-24)
- https://github.com/lmarena - methodology repositories including arena-rank, pushed 2026-08-04 (fetched 200, 2026-09-24)
- https://web.lmarena.ai/ - the WebDev arena surface (fetched 200, 2026-09-24)
