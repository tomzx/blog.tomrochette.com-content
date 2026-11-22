---
title: LMArena
created: 2026-09-24
updated: 2026-11-22
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

A website (arena.ai since an October 2026 rebrand to the shorter name Arena; lmarena.ai redirects there), a family of leaderboards (Agent Overall, Text, WebDev, Image, Video, Vision, Document, Search, Alignment), a WebDev arena (now arena.ai/code), a blog still at blog.lmarena.ai, and open methodology repositories, run by Arena Intelligence Inc., the company that grew out of the UC Berkeley and LMSYS Chatbot Arena project.
The founding paper (arXiv:2403.04132, March 2024) describes the pairwise crowdsourcing method and 240K+ votes at the time; the leaderboard methodology source is published as the `arena-rank` repository (Apache-2.0), which moved in November 2026 from the lmarena GitHub organization to a new Arena-OSS organization and has not pushed to its main branch since August 2026.
The company raised $100M at a $600M valuation in May 2025, led by Andreessen Horowitz and UC Investments, and labs including OpenAI, Google, and Anthropic partner with it to put flagship models in front of voters.
On 8 October 2026 it announced a $200M Series B at a $3.1B valuation, and launched the Arena Alignment Index with it, a leaderboard scoring 27 models across 90,000 real-world agent sessions on how well models act in line with human intent.
Recent product motion includes AutoEval scores added to the leaderboards (to complement slowly collected human votes), agent leaderboard categories with task costs (August 2026), a HarnessTax research post (September 2026), a research post showing LLM judges prefer their own responses 70% more often than humans do (30 September 2026), an October 2026 research post that post-trains a text-to-image model on 5 million Arena preference votes plus rubric rewards, which is direct evidence for the training-asset claim below, Max (12 October 2026), an agentic router from Arena itself that claims frontier performance in Agent Arena at 37% lower cost than top models, putting the ranking operator into competition with the models it ranks, and the October 2026 rebrand that consolidated the product surfaces onto arena.ai under the name Arena, with the company still Arena Intelligence Inc. and its GitHub organization renamed to match.
Two more posts landed on 30 October 2026: a Factuality leaderboard that ranks models by the factual accuracy of their responses alongside human preference, and Connectors in Agent Mode.
Two November posts followed: Interaction-as-a-Judge (13 November), a research post using computer-use agents to evaluate applications and reporting inference-time-scaling gains from it, and Introducing the Agent Arena Index (18 November), which rebuilt the agent leaderboards around a topline Agent Arena Index averaging the Task Completion, Praise vs Complaint, Steerability, and Bash Reliability signals plus an agent-mode Alignment Index scoring Unauthorized Action, False Attribution, and Deceptive Completion, moved scores onto a new scale where one index point is a thousandth of a signal standard deviation (rankings unchanged from the previous methodology), and retired the Tool Hallucination signal as frontier models rarely call nonexistent tools now.

## Status

The most-cited leaderboard in the field: a critical paper describing Chatbot Arena as "the go-to leaderboard for ranking the most capable AI systems" is itself the best evidence of that status.
The blog posts within days of verification, the arenas run continuously, and HN threads routinely open with its rankings as the premise.
The company is well capitalized and has converted the academic project into a venture-scale business, which is also the source of its hardest questions, and it reported a $100M annualized run rate in June 2026, eight months in, with 10M+ monthly users and 82M+ votes contributed.

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
- 2026-10-04 - Added the 2026-10-02 research post on post-training text-to-image models with 5 million Arena preference votes to the product-motion record, the first documented case of the vote stream training a model.
- 2026-10-06 - Added the company's June 2026 disclosure of a $100M annualized run rate (10M+ monthly users, 82M+ votes) and the 30 September 2026 research post finding LLM judges prefer their own responses 70% more often than humans do.
- 2026-10-10 - Added the $200M Series B at a $3.1B valuation (announced 8 October 2026) and the Arena Alignment Index launched with it (27 models across 90,000 real-world agent sessions).
- 2026-10-16 - Recorded Max (announced 12 October 2026), Arena's own agentic router claiming frontier Agent Arena performance at 37% lower cost than top models, the first time the ranking operator has entered the market its rankings measure.
- 2026-10-25 - Rotation re-verification with every cited URL re-fetched live: recorded the October 2026 rebrand, lmarena.ai now 301-redirecting to arena.ai, the WebDev arena redirecting to arena.ai/code, the blog navigation rebranded "Try Arena" with its newest post still the 12-13 October Max router post, and the GitHub organization renamed Arena with its blog field pointing at arena.ai/blog while arena-rank remains unpushed since August.
- 2026-11-07 - Rotation re-verification with every cited URL re-fetched live: recorded the two 30 October 2026 posts, a Factuality leaderboard ranking models by the factual accuracy of responses beside human preference and Connectors in Agent Mode, with the redirect pattern unchanged (lmarena.ai to arena.ai, the WebDev arena to arena.ai/code, how-it-works to arena.ai/blog), arena-rank still unpushed since 2026-08-04, and every third-party source (both arXiv papers, the TechCrunch and Verge articles, the Surge AI critique) live.
- 2026-11-22 - Rotation re-verification with every cited URL re-fetched live: recorded the two November posts, Interaction-as-a-Judge (13 November) and the Agent Arena Index rebuild (18 November, a topline index plus an agent-mode Alignment Index on a thousandth-of-a-standard-deviation score scale with rankings unchanged and the Tool Hallucination signal retired), the redirect pattern unchanged (lmarena.ai to arena.ai, which bot-walls this client at 403; the WebDev arena to arena.ai/code; how-it-works to arena.ai/blog/how-it-works/), and the methodology fleet's move: the public repositories left the lmarena organization (now zero public repos) for a new Arena-OSS organization (created 2026-08-20, 13 public repositories, blog field arena.ai/blog), with arena-rank among them, still Apache-2.0 and unpushed on main since 2026-08-04 (its 2026-11-20 pushed_at moves landing on side-branch copybara syncs, the section's ruled pattern), and every third-party source (both arXiv papers, the TechCrunch and Verge articles, the Surge AI critique) live.

## See also

- [Artificial Analysis](../artificial-analysis/index.md) - the controlled-eval counterpart to crowd preference
- [OpenRouter Rankings](../openrouter-rankings/index.md) - what people pay for, against what they vote for
- [Epoch AI](../epoch-ai/index.md) - the research-nonprofit model of measurement this company left behind
- [Trackers and Leaderboards Feature Matrix](../trackers-and-leaderboards-feature-matrix/index.md) - the category comparison this note joins
- [You Cannot Out-Review a Machine by Hand](../../../you-cannot-out-review-a-machine-by-hand/index.md) - human judgment as a bottleneck, applied to review instead of ranking

## References

- https://lmarena.ai/ - homepage meta: blind comparison, vote-driven leaderboards across text, image, and code (fetched 200, 2026-09-24; re-fetched 2026-10-25, now 301-redirecting to arena.ai, which bot-walls this client; re-fetched 2026-11-07, still 301 to arena.ai)
- https://lmarena.ai/ - homepage meta: blind comparison, vote-driven leaderboards across text, image, and code (fetched 200, 2026-09-24; re-fetched 2026-10-25, now 301-redirecting to arena.ai, which bot-walls this client; re-fetched 2026-11-07, still 301 to arena.ai; re-fetched 2026-11-22, still 301 to arena.ai, whose root serves 403 to this client)
- https://blog.lmarena.ai/ - Arena Intelligence Inc. identity, leaderboard families, and 2026 post dates including the 8 October 2026 Series B and Arena Alignment Index announcement, the 12-13 October Max router post, the 30 September judge self-preference post, and the 2026-10-02 post-training research post (re-fetched 200, 2026-10-25 via curl after a fetch-tool failure, newest post still Max, navigation rebranded "Try Arena" with links to the arena.ai surfaces; re-fetched 200, 2026-11-07 via curl, newest posts now the two 30 October 2026 entries, Factuality in the Arena and Connectors in Agent Mode, with the Max post still listed; re-fetched 200, 2026-11-22, the newest posts now Interaction-as-a-Judge and Introducing the Agent Arena Index, with the October entries still listed)
- https://blog.lmarena.ai/blog/introducing-the-agent-arena-index/ - the 18 November post behind the agent-board rebuild: the topline Agent Arena Index (Task Completion, Praise vs Complaint, Steerability, Bash Reliability averaged), the agent-mode Alignment Index (Unauthorized Action, False Attribution, Deceptive Completion), domain- and capability-specific indexes, the new score scaling (one index point a thousandth of a signal standard deviation, rankings unchanged), and the Tool Hallucination signal retirement (fetched 200, 2026-11-22; the post page is client-rendered, so the content was read from the streamed payload and dated from the sitemap)
- https://blog.lmarena.ai/sitemap.xml - the post inventory grounding the new posts' dates (Agent Arena Index 2026-11-18, Interaction as a Judge 2026-11-13) (fetched 200, 2026-11-22, resolving to arena.ai URLs)
- https://blog.lmarena.ai/how-it-works/ - the vote flow and identity reveal procedure (fetched 200, 2026-09-24; re-fetched 200, 2026-10-25 via redirect to arena.ai/blog/how-it-works; re-fetched 2026-11-07, still 301 to arena.ai/blog/how-it-works/; re-fetched 2026-11-22, still 301 to arena.ai/blog/how-it-works/)
- https://arxiv.org/abs/2403.04132 - the founding paper: method and 240K+ votes (fetched 200, 2026-09-24; re-fetched 200, 2026-10-25; re-fetched 200, 2026-11-07; re-fetched 200, 2026-11-22)
- https://arxiv.org/abs/2504.20879 - The Leaderboard Illusion: private testing, 27 Meta variants, sampling asymmetries (fetched 200, 2026-09-24; re-fetched 200, 2026-10-25; re-fetched 200, 2026-11-07; re-fetched 200, 2026-11-22)
- https://techcrunch.com/2025/05/21/lm-arena-the-organization-behind-popular-ai-leaderboards-lands-100m/ - $100M seed, $600M valuation, investors, Berkeley origin (fetched 200, 2026-09-24; re-fetched 200, 2026-10-25; re-fetched 200, 2026-11-07; re-fetched 200, 2026-11-22)
- https://www.theverge.com/meta/645012/meta-llama-4-maverick-benchmarks-gaming - the Maverick gaming episode and LMArena's policy response (fetched 200, 2026-09-24; re-fetched 200, 2026-10-25; re-fetched 200, 2026-11-07; re-fetched 200, 2026-11-22)
- https://surgehq.ai/blog/lmarena-is-a-plague-on-ai - the strongest critical essay on the format (fetched 200, 2026-09-24; re-fetched 200, 2026-10-25; re-fetched 200, 2026-11-07; re-fetched 200, 2026-11-22)
- https://github.com/lmarena - methodology repositories including arena-rank, pushed 2026-08-04 (fetched 200, 2026-09-24; re-fetched via API, 2026-10-25, organization renamed Arena, blog field now arena.ai/blog, arena-rank still pushed 2026-08-04; re-fetched via API, 2026-11-07, blog field still arena.ai/blog, arena-rank still pushed 2026-08-04; re-fetched via API, 2026-11-22, the organization now holds zero public repositories, its fleet moved to Arena-OSS (created 2026-08-20, 13 public repositories, blog field arena.ai/blog), where arena-rank resolves at Arena-OSS/arena-rank via redirect, still Apache-2.0, 126 stars, default branch unpushed since 2026-08-04 with the 2026-11-20 pushed_at moves on side-branch copybara syncs)
- https://web.lmarena.ai/ - the WebDev arena surface (fetched 200, 2026-09-24; re-fetched 2026-10-25, now redirecting to arena.ai/code; re-fetched 2026-11-07, still 301 to arena.ai/code; re-fetched 2026-11-22, still 301 to arena.ai/code)
