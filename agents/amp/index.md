---
title: Amp
created: 2026-08-22
updated: 2026-08-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3, coding-agents, harnesses, remote-execution, developer-tools]
readability: 3
audience_notes: >
  Engineers delegating long-running tasks to agents that keep working after the laptop closes.
  Assumes you have run a terminal agent and understand metered usage billing.

---

Amp is the coding agent from Amp Frontier Corporation ([spun out of Sourcegraph on December 2, 2025](https://ampcode.com/news/amp-inc)): a CLI plus web and phone surfaces, with threads that run on remote machines called orbs.
Facts below verified as of 2026-08-24.

**Amp's orbs are the most direct answer in the field to "the agent should keep working when I close my laptop", and the product is priced exactly like something that believes its own value.**

## What it is

The `amp` CLI runs the agent loop locally; threads can be handed to **orbs, remote machines that keep executing after you disconnect**, and picked up from any device.
Four modes (low, medium, high, ultra) trade speed against reasoning, with the oracle as a second-opinion model, the librarian for cross-repository GitHub search, subagents, schedules the agent sets itself, and a plugin system that can gate tool calls.
AGENTS.md is the guidance convention, and a linked ChatGPT subscription can supply GPT-5.6 usage.

## Status

**Active and independent.**
Amp was built inside Sourcegraph, was made free in October 2025, launched subscriptions, and spun out as a profitable separate company in December 2025 with a twenty-person founding team.
Shipping cadence in August 2026 is weekly (usage explainers, MCP in orbs, team handoffs, voice control via Puck).

## Strengths

- **Remote execution is the product, not a bolt-on**: orbs, runners, phone control, and thread sharing compose into actual delegated work.
- The oracle and librarian are direct answers to "the model should check itself and read other repos".
- Willingness to delete features keeps the surface small; the manual reads like a tool its builders use.
- BYOK works on usage billing, including Anthropic keys (with the data-retention caveat their [manual](https://ampcode.com/manual/) documents for Fable-class models).

## Cautions

- Closed source; you are trusting a startup's harness with your repository and its metering.
- Expensive by [community report](https://news.ycombinator.com/item?id=46124649): **usage-billed teams describe spending over $1,000/month per person**, and pay-as-you-go users describe watching budgets evaporate before they can judge the tool.
- No free tier anymore; the October 2025 free period ended with subscriptions.
- Tool calls do not ask approval by default; the permission model is opt-in via plugins, which is a real decision to make consciously.

## Pricing

Megawatt $20/month: 750 orb hours, $20 of included agent usage, **unlimited linked ChatGPT, X Premium+/SuperGrok, or SpaceX AI subscription usage**, low and medium modes (high with a linked ChatGPT subscription).
Gigawatt $200/month: 1,000 hours of xxlarge orbs, $200 included usage, all modes including ultra.
Usage billing and enterprise plans meter by API rates; students and teachers pay $10/month.

## Compared to

- [Claude Code](../claude-code/index.md) and [Codex](../codex/index.md): subscription platforms whose cloud forms are bounded by session caps; **Amp's orbs are the more aggressive delegation model**.
- [OpenCode](../opencode/index.md): the local, open, cheap end of the same decision.

## Bottom line

**Recommended for engineers whose bottleneck is supervision of long-running parallel work and whose budget is real.**
Not for open-source-only teams or anyone metering their own tokens.

## See also

- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - Amp as the remote-execution bet in the harness layer
- [Managing Many Concurrent LLM Agent Sessions](../../managing-many-llm-agent-sessions/index.md) - the supervision pattern orbs exist for
- [Scaling the LLM Agent Company](../../scaling-the-llm-agent-company/index.md) - where delegated agents point at company scale
- [The Codebase Gardener](../../the-codebase-gardener/index.md) - the human role left when agents run this far

## References

- https://ampcode.com/ - product overview, orbs, news cadence as of 2026-08-22
- https://ampcode.com/pricing/ - Megawatt, Gigawatt, usage billing, linked subscriptions
- https://ampcode.com/news/amp-inc - the December 2, 2025 spinout announcement
- https://ampcode.com/manual/ - modes, oracle, librarian, skills, plugins, permissions
- https://news.ycombinator.com/item?id=46124649 - spinout discussion with praise and cost complaints
