---
title: "Model Selection for Coding Tasks"
created: 2026-08-24
updated: 2026-09-10
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3, llm=x-preview-f-free, llm=glm-5.3-flash, model-selection, coding-agents, llm-pricing]
readability: 3
audience_notes: >
  Engineers who already drive a coding agent and now decide which model to point it at for edits, review passes, and long agentic loops.
  Assumes you know what input and output tokens cost and what a prompt cache does.
---

This is a maintained, opinionated guide to choosing models for coding, review, and agentic work.
Everything below was verified against live pricing pages and benchmark sources on 2026-09-04; every provider price was re-checked on 2026-09-05, 2026-09-06, 2026-09-07, and 2026-09-08 and none moved; on 2026-09-09 Kimi cut kimi-k2.7-code's price on OpenRouter, and this page moved with it; on 2026-09-10 the GLM-5.3-Flash promo resolved into its list price and DeepSeek shipped the cheaper V4.1-Flash while announcing V4 Pro's retirement, and this page moved with both.

**Model selection for coding is an economics decision before it is a capability decision: run the workhorse tier for the loop, buy the frontier by the minute, and give the reading to the cheap models.**
The part most engineers get backwards: **for anyone paying per token, the harness you run moves your bill about as much as the model you pick, and sometimes more.**

## Task class decides the tier

**Three task classes cover almost all coding work, and each maps to a price tier, not to a leaderboard rank.**

- Completion and small edits: the model writes a few dozen lines from tight context; latency and price matter more than peak reasoning, so the cheap tier wins (gpt-5.6-luna, Gemini 3.1 Flash-Lite, Claude Haiku 4.5, GLM-5.3-Flash).
- The agentic loop: explore, edit, test, repeat for minutes or hours; this is where most tokens die, and the mid tier (Claude Sonnet 5, gpt-5.6-terra, Gemini 3.1 Pro Preview) resolves most of it, while the Kimi, GLM, and DeepSeek challengers below price the same class far lower.
- Hard planning and review judgment: architecture choices, gnarly debugging, deciding what to let through; this is the only class where frontier spend reliably pays, and it is a small fraction of your turns.

Escalate by task class inside a session instead of picking one model for everything; Amp's low/medium/high/ultra modes and Codex's Sol/Terra/Luna defaults are this idea shipped as product (see the [Amp](../amp/index.md) and [Codex](../codex/index.md) notes).

## The lineup as of 2026-09-10

**The workhorse tier has converged to roughly $2 in and $10-12 out per million tokens at every major provider, which means switching costs are now measured in harness integration, not price.**

| Model | gpt-5.6-luna | gpt-5.6-terra | gpt-5.6-sol | gpt-5.3-codex | gpt-6-astra | Claude Haiku 4.5 | Claude Sonnet 5 | Claude Opus 5 | Claude Fable 5.1 | Gemini 3.1 Flash-Lite | Gemini 3.8 / 3.7 / 3.6 Flash | Gemini 3.1 Pro Preview | kimi-k2.7-code | kimi-k3 | GLM-5.3 | GLM-5.3-Flash | deepseek-v4-pro | deepseek-flash | qwen3.8-max | qwen3.8-flash |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Released | 2026-07-09 | 2026-07-09 | 2026-07-09 | 2026-02-05 | 2026-09-04 | 2025-10-15 | 2026-06-29 | 2026-07-24 | 2026-09-01 | 2026-05-07 | 2026-09-02 (3.8), 08-13 (3.7), 07-21 (3.6) | 2026-02-19 | 2026-06-12 | 2026-07-16 | 2026-08-14 | 2026-08-26 | 2026-08-12 | 2026-09-10 | 2026-08-03 | 2026-08-26 |
| Input / output per 1M | $0.20 / $1.20 | $2 / $12 | $4 / $20 | $1.75 / $14 | $10 / $50 | $1 / $5 | $2 / $10 | $5 / $25 | $10 / $50 | $0.25 / $1.50 | $0.75 / $3.75 | $2 / $12 | $0.71 / $3.50 | $3.00 / $15 | $1.40 / $4.40 | $0.15 / $0.50 | $1.32 / $3.96 | $0.30 / $1.20 | $2 / $6 | $0.15 / $0.47 |
| Cached input per 1M | $0.02 | ~10% of input | ~10% of input | ~10% of input | $1 | ~10% of input | ~10% of input | ~10% of input | 2.5% of input | ~10% of input | ~10% of input | ~10% of input | $0.15 | ~10% of input | ~20% of input | $0.03 | $0.044 | $0.006 | ? | ? |
| Context behavior | doubles past threshold | doubles past threshold | doubles past threshold | doubles past threshold | doubles past threshold | 200K | 1M flat | 1M flat | 1M flat | 1M flat | doubles past threshold | doubles beyond 200K | 256K | 1M flat | 1M flat | 1M flat | 1M flat, 384K max output | 1M flat, 384K max output | 1M flat | 1M flat |
| Pricing windows | none | none | promo through 2026-11-21 | none | none | none | intro price made standard, planned increase cancelled | none | none | none | intro to 2026-12-31, then doubles | none | HighSpeed variant at $1.90 / $8.00 | none | none | 50% promo ended 2026-09-09 into list | off-peak half ($0.66 / $1.98); routes to V4.1-Flash rates from 2026-09-14 | off-peak half ($0.15 / $0.60) | batch half price | 1M-token free quota for new accounts (90 days) |
| Notes | cheap tier | workhorse | frontier | coding-specialized API model | frontier, newest OpenAI generation | cheap tier | workhorse | frontier | top tier, Amp BYOK documents data-retention caveats | cheap tier | cost-led high-volume option | workhorse | challenger, coding-specialized, multimodal input | challenger flagship, always reasons with configurable effort | challenger, GLM-5 at $1/$3.20, GLM-4.7-Flash free | challenger cheap tier | challenger workhorse, Anthropic-format endpoint | challenger cheap tier, native vision, Anthropic-format endpoint | challenger flagship | challenger cheap tier |

A ? marks a property the verified pricing pages do not state.
The lineup keeps only models released within the last year, the oldest entry is Claude Haiku 4.5 on 2025-10-15, 35 days inside the window, and release dates and context windows follow the models.dev list reference, which also supplies the newest Gemini Flash siblings the table groups on shared intro pricing; deepseek-flash is the one exception, dated from DeepSeek's release announcement because models.dev has not caught up.

Four details the table hides:

- Batch mode is 50% off at OpenAI, Anthropic, Google, and Qwen3.8-Max, which makes overnight review sweeps half price by default.
- Cached reads run about one tenth of input price at OpenAI, Google, and Kimi K3, one tenth at Anthropic except the Fable 5.1 and Mythos 5.1 pair at one fortieth, closer to one fifth at GLM and kimi-k2.7-code, Qwen discounts hits without publishing a rate, and DeepSeek bills hits at about one fiftieth on Flash and one thirtieth on V4 Pro, so loop economics depend on both the cache-hit rate and the vendor's cache discount.
- Claude models from 4.6 onward include the full 1M-token context at standard pricing, and Kimi K3 matches the flat-1M policy at $3 in, while OpenAI and Google both double prices past their long-context thresholds, so whole-repository prompting is cheapest on Anthropic and second-cheapest on Kimi.
- The Claude 4.7+ tokenizer produces about 30% more tokens for the same text, so cross-vendor price comparisons understate Anthropic's effective cost by roughly that margin.

## The challengers reset the price floor

**Kimi, GLM, DeepSeek, and Qwen price the agentic loop at half the converged workhorse rate or less, which makes the $2/$10-12 "standard" a choice rather than a fact.**
GLM-5.3, 5.2, and 5.1 sit at $1.40 in and $4.40 out per million tokens, with GLM-5 at $1/$3.20, per Z.ai's pricing page as of 2026-09-10.
Kimi's coding-specialized kimi-k2.7-code undercuts that at $0.71/$3.50 with a 256K context and multimodal input, down from $0.95/$4.00 on OpenRouter while Moonshot's own pricing page still showed the old numbers as of 2026-09-10.
Its HighSpeed variant lists at $1.90/$8.00 for about 180-260 tokens per second of output.
Kimi K3 takes the other flank: $3/$15, always reasoning with a configurable effort, and a flat-price 1M context that only Claude otherwise offers.
Z.ai even keeps GLM-4.7-Flash free, which makes it the zero-dollar candidate for inline completion and routing experiments.
GLM-5.3-Flash fills the gap between free and $1.40: its 50 percent launch promo expired at 24:00 on 2026-09-09 Singapore time exactly as scheduled, and Z.ai's page billed the $0.15/$0.50 list price with cached reads at $0.03 when I re-checked on 2026-09-10.
DeepSeek V4 undercuts them all: v4-pro lists at $1.32 in and $3.96 out per million at peak, with every hour outside 01:00-04:00 and 06:00-10:00 UTC on weekdays billed at half, so off-peak runs pay $0.66/$1.98, and from 2026-09-14 the v4-pro id routes to V4.1-Flash at Flash rates until V4.1-Pro ships, which makes this row a two-week window.
On 2026-09-10 DeepSeek replaced v4-flash outright: deepseek-flash (V4.1-Flash) lists at $0.30/$1.20 peak and $0.15/$0.60 off-peak, adds native vision input, and both models keep a flat 1M context with 384K max output and thinking mode on by default.
DeepSeek's cache hits bill at $0.044 (pro) and $0.006 peak or $0.003 off-peak (flash) per million, the Flash hit about one fiftieth of a miss, the deepest cache discount of any vendor in this guide.
It also exposes an Anthropic-format endpoint, so harnesses that speak the Claude API can point at DeepSeek directly.
Qwen3.8-Max rounds out the field at $2 in and $6 out per million tokens with flat 1M pricing, at or below the converged workhorse rate at flagship quality, and Qwen3.8-Flash sits in the cheap tier at $0.15/$0.47.
Alibaba's Model Studio is not a native OpenCode provider the way Moonshot, Z.AI, and DeepSeek are, but it speaks the OpenAI-compatible format, so Qwen rides OpenRouter or any compatible endpoint.
Harness fit is solved: OpenCode lists Moonshot AI, Z.AI, and DeepSeek as native providers, so the lean BYOK harness plus a challenger model is one /connect away.
**My disagreeable claim: for a token-payer, the rational default loop in September 2026 is deepseek-flash, kimi-k2.7-code, or GLM-5.3 through OpenCode, and the big-three workhorses are what you escalate to, not what you default to.**
Whether the challengers hold quality on your codebase is exactly what SWE-bench's bash-only view and a two-week cost-per-merged-PR measurement are for; the economics alone no longer justify defaulting to the big three.
The era of Gemini Flash's $0.75 intro rate leading a price category is over: GLM-5.3-Flash now bills its $0.15/$0.50 list price, and deepseek-flash beats it permanently at $0.30 peak, $0.15 off-peak, with no expiry announced.

## Benchmarks decay faster than prices

**Benchmark points do not track price, and the last independent leaderboard that published cost per run makes the point brutally.**
The [aider polyglot leaderboard](https://aider.chat/docs/leaderboards/) froze in 2025 along with the tool's maintenance (see the [aider](../aider/index.md) note), but its dated runs still teach the right lesson.
In October 2025, DeepSeek-V3.2-Exp (Reasoner) scored 74.2% for $1.30 of API spend across the 225-exercise suite.
In June 2025, o3-pro (high) scored 84.9% for $146.32: ten points more for 113 times the money.

For current rankings, [SWE-bench Verified](https://www.swebench.com/verified.html) is the reference, and its default view now runs every model in the same minimal [mini-SWE-agent](https://www.swebench.com/) bash environment precisely so harnesses stop inflating scores.
The frontier of evaluation moved on again: CodeClash (November 2025) scores goal-oriented development and ProgramBench (May 2026) scores building artifacts from scratch.
My rule: use benchmarks for relative history and cost-per-point for decisions, and never quote a vendor's self-reported number, including the SWE-Rebench claim on Junie's own site (see the [Junie](../junie/index.md) note).

## The harness multiplies the price of everything

**The measured spread between harnesses is larger than the frontier premium at OpenAI and most of it at Anthropic.**
The July 2026 proxy study recorded in the [Claude Code note](../claude-code/index.md) measured about 33k input tokens sent before the user's prompt on a minimal task, mid-session cache re-writes up to 54x, and a 4.2x multiplier on a two-subagent fan-out.
The same study, recorded in the [OpenCode note](../opencode/index.md), measured about 7k baseline tokens for OpenCode with byte-stable cache prefixes, making it about 3.7x cheaper on a matched pass/fail benchmark.
Compare: Fable 5.1 costs 5x Sonnet 5 per token, and gpt-5.6-sol costs 2x terra.
So choosing OpenCode over Claude Code moves a token-payer's bill more than choosing terra over sol, and roughly matches skipping Fable 5.1 for Sonnet 5.
Models are substitutable across providers; a harness with a heavy baseline taxes every model you point through it, forever.

## Subscription or BYOK: pick by where your spend lands

**Subscriptions win below a spend threshold and handcuff you above it, so the unit that decides is dollars of monthly token spend, not features.**
The subscription side: Claude Code is included from Claude Pro ($20 monthly) through Max 20x ($200/month) per the [Claude Code note](../claude-code/index.md), and Codex is included from the ChatGPT Free tier upward per the [Codex note](../codex/index.md), though usage meters in shared five-hour windows with wide published ranges (10-100 local Sol messages on Plus).
Amp's Megawatt at $20/month makes a linked ChatGPT subscription's usage effectively unlimited at low and medium modes per the [Amp note](../amp/index.md), the cheapest delegation entry if you already pay for ChatGPT.
The BYOK side: OpenCode, Junie, Crush, and aider bill at provider rates with zero markup (Junie's cloud credits, 10 per 30 days on AI Pro, make BYOK effectively mandatory for real work per the [Junie note](../junie/index.md)).
The crossover math: $100 of Sonnet 5 API spend is 50M raw input tokens at the table's $2/M rate, and closer to 20M total tokens once you blend in output-priced generation at agentic ratios, which one heavy week can eat; if you reliably run past that, subscriptions cap your downside until their limits bite.
One fence to remember: Anthropic's March 2026 legal requests removed Claude subscription login from OpenCode (see the [OpenCode note](../opencode/index.md)), so subscription value does not transfer to third-party harnesses; subscribe to the vendor whose harness you will actually run.

## A decision guide

**Everything above collapses into one sentence per situation, and every price claim in it is dated in the table above.**

- Daily loop default: Claude Sonnet 5, gpt-5.6-terra, or Gemini 3.1 Pro Preview; pick by harness fit, they price the same.
- High-volume loops where cost leads: deepseek-flash at $0.30 peak and $0.15 off-peak with no expiry announced, GLM-5.3-Flash at $0.15/$0.50 now that its launch promo has ended, or Gemini 3.8/3.7/3.6 Flash at the shared $0.75/$3.75 intro rate (calendar the 2026-12-31 end).
- Price-floor loops, BYOK: deepseek-flash, kimi-k2.7-code, or GLM-5.3 through OpenCode, all native providers; nothing credible stays cheaper.
- Whole-repository reads: DeepSeek from $0.30 in, a 1M-context Claude or Qwen3.8-Max at $2, or Kimi K3 at $3 flat; all four keep 1M pricing flat.
- Frontier minutes only: gpt-6-astra, gpt-5.6-sol, or Claude Opus 5 for planning and stuck debugging; Fable 5.1 when nothing else resolves.
- Inline completion and edits: gpt-5.6-luna, Gemini 3.1 Flash-Lite, Claude Haiku 4.5, or GLM-5.3-Flash.
- Review passes and doc reading: cheap tier in batch mode, or a 1M-context Claude for whole-repo reads at standard price.
- Offline or air-gapped: local models through aider, Crush, or Junie BYOK.
- Already paying ChatGPT: run Codex, and consider Amp for delegated work.
- Already paying Claude: run Claude Code; do not expect that subscription to drive any other harness.

## What changes fast and how to re-verify

**Everything volatile in this guide is dated, and three clocks are running.**
GLM-5.3-Flash's half-price launch promo expired at 24:00 on 2026-09-09 Singapore time as scheduled, and Z.ai's page billed the $0.15/$0.50 list price when I re-checked on 2026-09-10.
DeepSeek starts routing v4-pro requests to V4.1-Flash at Flash rates at 04:00 UTC on 2026-09-14, Sol's promotional pricing runs at least through 2026-11-21, the Gemini Flash intro rate ends 2026-12-31, and benchmark relevance decays on roughly a quarterly cycle (CodeClash, then ProgramBench within six months).
Sonnet 5 shows the other direction: a scheduled September 2026 increase to $3/$15 was cancelled weeks before taking effect, so scheduled changes are announcements, not facts.
On each refresh I re-fetch the six provider pricing pages (OpenAI, Anthropic, Google, Moonshot, Z.ai, DeepSeek), the SWE-bench leaderboards, and one current harness-overhead measurement, and I update the table above and the as-of date together.
A fact that cannot survive that re-fetch gets deleted rather than hedged.

## What to Do Next

- Set your harness default to the workhorse tier this week, and escalate to a frontier model only for planning steps and stuck loops.
- Measure cost per merged PR on your own repository for two weeks; that number outranks every benchmark cited here.
- If you pay per token, prefer a harness with byte-stable cache prefixes, because the 54x cache re-write failure mode costs more than any model choice.
- Route review sweeps through batch mode; half price at all three providers is the cheapest quality improvement available.
- The 2026-09-10 GLM-5.3-Flash check resolved as predicted: the promo expired into the $0.15/$0.50 list price; calendar the 2026-09-14 DeepSeek routing change and the 2026-11-21 and 2026-12-31 promo deadlines to re-run your economics then.
- If you point a loop at DeepSeek, schedule the long runs off-peak; half price by the clock is the deepest vendor discount in this guide and it stacks with caching.

## See also

- [Model Provider Feature Matrix](../model-provider-feature-matrix/index.md) - this guide's prices regrouped into a provider-by-provider bundle comparison
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - the four-layer map this guide's harness claims sit inside
- [Claude Code](../claude-code/index.md) - the measured token overhead that anchors the harness-multiplier argument
- [Codex](../codex/index.md) - the Sol/Terra/Luna tiering as shipped defaults
- [OpenCode](../opencode/index.md) - the lean BYOK counterexample and the subscription-transfer fence
- [aider](../aider/index.md) - the frozen leaderboard whose cost data this guide leans on

## References

- https://platform.openai.com/docs/pricing - GPT-5.6 family and gpt-5.3-codex token prices, batch discount, promo end date, long-context doubling
- https://docs.claude.com/en/docs/about-claude/pricing - Claude 5 lineup, cache multipliers, 1M-context policy, tokenizer note, Sonnet 5 price decision
- https://cloud.google.com/vertex-ai/generative-ai/pricing - Gemini 3 family pricing, intro windows, long-context and batch rates
- https://www.swebench.com/verified.html - the Verified benchmark and the bash-only mini-SWE-agent comparison setup
- https://www.swebench.com/ - CodeClash and ProgramBench launch dates, mini-SWE-agent 65% result
- https://aider.chat/docs/leaderboards/ - the polyglot leaderboard with per-run costs and dates used for the cost-per-point argument
- https://platform.kimi.ai/docs/pricing/chat-k3 - Kimi K3 prices, cache-hit rate, flat 1M context, always-on reasoning with configurable effort
- https://platform.kimi.ai/docs/pricing/chat-k27-code - kimi-k2.7-code's official prices (still $0.95/$4.00 as of 2026-09-10), 256K context, HighSpeed variant prices and speeds
- https://docs.z.ai/guides/overview/pricing - GLM-5.x family prices, cached input rates, free Flash tiers, and the GLM-5.3-Flash list price billed after the 2026-09-09 promo
- https://opencode.ai/docs/providers/ - Moonshot AI, Z.AI, and DeepSeek as native OpenCode providers
- https://api-docs.deepseek.com/quick_start/pricing/ - DeepSeek lineup including V4.1-Flash and the V4 Pro routing notice, peak and off-peak rates, 1M context and 384K output, cache-hit prices, peak-hour definition (the trailing slash matters: without it the URL serves the first-API-call page)
- https://api-docs.deepseek.com/news/news260910 - the DeepSeek-V4.1-Flash release announcement of 2026-09-10: model id, V4-Flash retirement, the 2026-09-14 V4 Pro routing change, and open weights
- https://help.aliyun.com/zh/model-studio/billing-for-model-studio - Qwen3.8-Max and Qwen3.8-Flash official per-token prices, batch half price on Max, context-cache discount, the 0-1M token tier, and the new-account free quota
- https://openrouter.ai/api/v1/models - USD international listings for kimi-k2.7-code ($0.71/$3.50, cache hit $0.15), qwen3.8-max-0902 ($2/$6), and qwen3.8-flash ($0.15/$0.47), re-checked 2026-09-10
- https://models.dev - the community model list used as the lineup reference: model ids, release dates, and context windows for every model in the table (fetched 2026-09-10)
