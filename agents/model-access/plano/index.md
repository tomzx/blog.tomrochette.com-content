---
title: Plano
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, model-access, llm-gateway, self-hosted]
readability: 3
audience_notes: >
  Engineers choosing self-hosted gateway software to sit in front of their model providers.
  Assumes you know OpenAI-compatible APIs, BYOK, and what an Envoy proxy does.
---

Plano is Katanemo Labs' open-source, Envoy-based proxy for AI agents: an LLM gateway that routes model traffic by preference, with agent orchestration, guardrails, and observability in the same data plane.

**It enters this category as self-hosted gateway software, the slot LiteLLM holds, but its center of gravity has already widened from LLM gateway to agent data plane under new ownership, and that widening is the fact to watch.**

## What it is

A Rust data plane built on Envoy by a founding team that previously built Envoy at Lyft, the AWS API Gateway, and safety infrastructure at Meta, configured from one YAML file that declares agents, model providers with your own API keys, and filter chains.
It speaks OpenAI-compatible chat completions on both sides: apps and agents point at Plano's local LLM gateway (port 12001 in the default setup), and Plano routes to the provider you configured, with fallbacks, rate limiting, and traffic shaping from the Envoy layer.
The routing intelligence is the team's own small models: a 4B-parameter Plano-Orchestrator picks the agent, and the Arch-Router lineage (a 1.5B preference-aligned router) picks the model.
The project launched as Arch, then archgw (three Hacker News launches between 2024-10 and 2025-07), and carried the Plano name by its January 2026 relaunch.
Katanemo Labs was acquired by DigitalOcean on April 2, 2026, with co-founder and CEO Salman Paracha joining as SVP of AI.

## Status

Active and well resourced: 7,081 stars and 487 forks as of 2026-10-07, Apache-2.0, with release 0.4.37 published 2026-09-28 and the repo pushed the same week.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=katanemo/plano&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=katanemo/plano&type=date&theme=dark&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=katanemo/plano&type=date&theme=dark&legend=top-left" />
</picture>

The launch record is unusually deep for this category: the archgw Show HN of 2025-07-12 drew 118 points, the Arch-Router announcement drew 66 points a week earlier, and the Plano relaunch drew 8 in January 2026.
DigitalOcean's acquisition press release names Plano as the open-source piece of its Agentic Inference Cloud strategy, and the hosted Plano models are served free from the US-central region as a first-run experience.

## Strengths

- Model routing is preference-based rather than benchmark-based: you describe what you want in natural language and the Arch-Router lineage picks the provider, which no other member here does.
- It runs on stock Envoy (WASM filters, cluster-level rate limiting and failover), so the traffic layer is battle-tested rather than bespoke.
- Guardrail, jailbreak, and moderation hooks sit in the same proxy, enforced on every request outside application code.
- Free and open source under Apache-2.0 with no token fees: your provider keys bill you directly.
- The small routing models keep the decision layer cheap, single-digit milliseconds per the launch thread.

## Cautions

- The objection from its own 118-point thread stands: dozens of AI gateways do this, a commenter called Kong far ahead on features and adoption, and Plano's answer (Envoy pedigree, agent-native protocols) is a bet, not a measurement.
- The product has pivoted from LLM gateway to "AI-native proxy and data plane for agentic apps" under DigitalOcean, so model access is now one feature among orchestration, signals, and guardrails, and the roadmap belongs to a cloud vendor.
- Preference-based routing can misroute, the fallback is your own configuration, and I found no independent benchmark of Arch-Router or Plano-Orchestrator routing accuracy.
- The hosted free models are a first-run convenience only: production use means self-hosting or contacting the team for API keys, so there is no published hosted path.

## Pricing

Pricing does not apply: the data plane is free and open source under Apache-2.0 with no token markup, your providers bill you directly, and the hosted Plano models are free for a first-run experience with production access by contact, as of 2026-10-07.

## Compared to

[LiteLLM](../litellm/index.md) is the same self-hosted, zero-fee gateway idea with a far larger community and a weekly release cadence; choose LiteLLM for provider breadth and budgets, Plano when agent routing and guardrails belong in the same proxy.
[Experiential](../experiential/index.md) also routes at zero markup but is hosted-first and mines your traffic; Plano keeps everything on your infrastructure.
[Ollama](../ollama/index.md) serves models locally where Plano only routes to them, so a local stack can pair the two.

## Bottom line

Recommended for teams already standing up Envoy-style infrastructure that want agent routing, guardrails, and LLM fallbacks in one self-hosted layer.
Not for anyone who wants a mature, focused model gateway today, where LiteLLM is the safer pick.
My disagreeable claim: as a model-access product Plano is a side quest inside an agent-platform bet, and DigitalOcean's ownership makes it more likely to narrow around their cloud than to chase the gateway incumbents.

## Changes

- 2026-10-07 - Created when this run's awesome-list scan surfaced the renamed katanemo/plano gateway.

## See also

- [LiteLLM](../litellm/index.md) - the self-hosted gateway incumbent this one challenges.
- [Experiential](../experiential/index.md) - the other zero-markup router, hosted-first.
- [LLM Gateway](../llm-gateway/index.md) - the hosted low-fee gateway counterpart.
- [Ollama](../ollama/index.md) - the local serving layer Plano can route to.

## References

- https://api.github.com/repos/katanemo/plano - 7,081 stars, 487 forks, Rust, Apache-2.0, pushed 2026-09-28, created 2024-07-09 as archgw (fetched via the GitHub API, 2026-10-07).
- https://raw.githubusercontent.com/katanemo/plano/main/README.md - YAML configuration model, OpenAI-compatible gateway on port 12001, 4B orchestrator, free hosted first-run models, Envoy base (fetched 200, 2026-10-07).
- https://planoai.dev - positioning as AI-native proxy and data plane, the v0.4.37 banner, and the DigitalOcean acquisition banner and footer (fetched 200, 2026-10-07).
- https://www.businesswire.com/news/home/20260402272982/en/DigitalOcean-Acquires-Katanemo-Labs-to-Accelerate-the-Inference-Cloud-for-the-Agentic-Era - the April 2, 2026 acquisition press release naming Plano and the Arch-Router lineage (retrieved 2026-10-07).
- https://hn.algolia.com/api/v1/items/44546265 - the 118-point archgw Show HN: the Envoy-pedigree founding team, the WASM filter architecture, and the Kong crowding objection with the founders' reply (fetched 200, 2026-10-07).
- https://hn.algolia.com/api/v1/search?query=katanemo&hitsPerPage=10 - the 66-point Arch-Router thread (2025-07-01) and the 8-point Plano relaunch (2026-01-06) (fetched 200, 2026-10-07).
- https://api.github.com/repos/katanemo/plano/releases?per_page=5 - 0.4.37 published 2026-09-28 (fetched 200, 2026-10-07).
