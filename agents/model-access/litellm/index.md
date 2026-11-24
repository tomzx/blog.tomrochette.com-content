---
title: LiteLLM
created: 2026-09-27
updated: 2026-11-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.4, llm=glm-5.3-flash, model-access, llm-gateway, self-hosted]
readability: 3
audience_notes: >
  For engineers deciding whether to self-host a gateway in front of their model providers.
  Assumes you know OpenAI-compatible APIs and per-token billing.
---

LiteLLM is the dominant self-hosted AI gateway, a Python SDK plus proxy server that exposes one OpenAI-compatible endpoint over 100+ provider APIs with routing, budgets, and spend tracking.

**Self-hosting the gateway means you own its availability, its config surface, and (since March 2026) its supply-chain risk, and that ownership is the entire trade.**

## What it is

BerriAI's gateway ships in two pieces: a Python SDK, a drop-in OpenAI-format client for 100+ providers, and a self-hosted proxy server with virtual keys, per-key budgets, rate limits, an admin UI, and spend tracking.
The Router adds retries, fallbacks, and load balancing across deployments, so an agent survives a single provider's outage or rate limit.
The proxy now also fronts MCP servers and A2A agents, making one deployment the gateway for models, tools, and agents at once.
A Rust core is in beta, and the repo description now reads "Rust core with Python SDK".
The core is MIT licensed; the `enterprise/` directory ships under a separate commercial license.

## Status

Very active: 61,356 stars as of 2026-10-16, repo pushed 2026-11-24 (as of 2026-11-24), publicly released July 2023.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=BerriAI/litellm&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=BerriAI/litellm&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=BerriAI/litellm&type=date&legend=top-left" />
</picture>

The cadence is extreme: a new minor line roughly every week, with v1.98.1, v1.99.4, v1.100.3, v1.101.2, and v1.102.1 all published between September 16 and 25, 2026, then v1.106.1 stable on 2026-10-20 through v1.106.5 on 2026-10-27, v1.106.6 on 2026-10-28 (with v1.105.7 patched the same day), a train carrying v1.109.0-dev.1 (2026-10-28), v1.108.0-rc.1 (2026-10-29, the first tag the then-never-stable v1.108 line had seen), and v1.109.0-dev.2 (2026-10-30), on 2026-11-04 v1.108.0 going stable (the v1.107 line never reaching stable at all) with v1.106.7 patched and v1.109.0-rc.1 published, then v1.108.1 (2026-11-05) and v1.108.2 (2026-11-06) patching the stable line, the never-stable v1.107 line picking up a v1.107.0-rc.3 on 2026-11-05 for two GitHub Copilot per-user fixes, and v1.110.0-dev.1 (2026-11-07) jumping the train head past the still-unstable v1.109 line, then v1.108.3 (2026-11-07) patching the stable line again as an LTS patch (11 PRs, 3 fixed, an AWS Bedrock request failure among them) with v1.110.0-dev.2 (2026-11-08) taking the train head, then on 2026-11-10 v1.108.5 patching the stable line while v1.104.9 and v1.103.11 patched lines outside the four-recent-minors window, on 2026-11-11 the never-stable-since-rc v1.109 line finally going stable (v1.109.0, with v1.106.8 patched the same day and v1.110.0-rc.1 published), and on 2026-11-12 v1.109.1, v1.108.6, and v1.106.9 patching their lines within hours of each other as v1.110.0-rc.2 took the train head, then v1.108.7 patching later the same day, on 2026-11-13 the train head jumping the never-stable v1.110 line to v1.111.0-dev.1 and v1.111.0-dev.2 while v1.108.8 patched the v1.108 line, and v1.106.10 landing 2026-11-14, with v1.108.9 patching the stable line that evening alongside a v1.107.0-rc.4, then on 2026-11-15 v1.110.0-rc.3 published as the v1.110 line passed its dev state and v1.111.0-dev.3 and v1.111.0-dev.4 taking the train head, with v1.108.10 (2026-11-16) patching the v1.108 line after it, PyPI latest holding at 1.109.1, and the repo pushed 2026-11-17, then the v1.110 line going stable on 2026-11-19 (v1.110.1, three PRs: a GPT-6.2 prompt-caching fix for system prompts sent with `store: false`, a slim-nginx UI image, and a Wolfi base bump) with v1.109.2, v1.108.12, and v1.106.11 patched the same day, v1.111.0-rc.2 taking the train head, and 2026-11-20 bringing v1.110.2 on the stable line, v1.109.3, v1.108.13, and v1.106.12 patches, a v1.112.0-dev.1 train head, and a v1.111.0-rc.3, with v1.108.14 landing that evening, then on 2026-11-21 v1.112.0-dev.2 taking the train head and v1.108.15 patching the v1.108 line (an LTS patch of 9 PRs: a ResetData provider added, a Groq and Meta transcription $0-spend fix, and keyless JSON-configured deployments now answering 401 until an api_key is set, flagged action required), with PyPI latest holding at 1.110.2 and the repo pushed 2026-11-24 (as of 2026-11-24). On 2026-11-23 and 11-24, v1.108.16 (2026-11-23, an LTS patch of 44 PRs, among them litellm_proxy decision support, Bedrock runtime endpoint routing for native chat and Responses, Gemini prompt-caching and batch-embedding billing fixes, and gateway DCR opt-in carried as a breaking change by its commit marker), v1.110.3 (2026-11-24, 5 PRs: the same DCR opt-in backport, audit log fixes, and router fallback by the group a pick was routed to), and v1.109.4 (2026-11-24, 2 PRs) patched their lines, PyPI latest moved to 1.110.3, and the train head stayed at v1.112.0-dev.2.
Since 2026-06-29 only the four most recent stable minor lines receive patches, a policy the company states is a direct cost of that cadence.
**In March 2026 the project's PyPI publishing credentials were compromised: poisoned 1.82.7 and 1.82.8 wheels shipped a credential stealer and were quarantined within about a day (PYSEC-2026-2).**
The release notes record supply-chain hardening in response to a later incident: after "the Oct 21 incident (#47826)" the project replaced the cosign key that signs its Docker images, and releases since then carry pinned-key cosign verification instructions (as of 2026-11-07).

## Strengths

- One OpenAI-compatible surface over 100+ providers, with the Router handling retries, fallbacks, and load balancing.
- Virtual keys, per-key and per-team budgets, rate limits, and spend tracking are in the free self-hosted tier, not gated.
- The MCP and A2A gateways converge into the same endpoint, so one deployment fronts models, tools, and agents.
- The observability surface is broad, with callbacks for Langfuse, MLflow, Helicone, and OpenTelemetry.
- Day-0 support for new providers is effectively weekly, which matters when an agent stack adopts a fresh model fast.

## Cautions

- **March 2026: compromised 1.82.7/1.82.8 PyPI wheels stole SSH keys, cloud credentials, and Kubernetes tokens, exfiltrating to a lookalike domain; TechCrunch later tied the Mercor breach to the same compromise.**
- A gateway aggregates every provider credential you own, so it is a single high-value theft target; pin versions and verify tags before pulling.
- The config surface moves fast: minor lines ship weekly and older lines lose support within four releases, so an unpinned deployment drifts.
- Community pushback exists: a September 2026 "LiteLLM without the bloat" fork hit 177 points on Hacker News, with commenters arguing the SDK has outgrown its size and dependency budget.
- SSO above 5 users, audit logs, and most built-in moderation guardrails require the enterprise license.
- No public enterprise pricing; everything beyond OSS is quote-based, with no published floor.

## Pricing

Self-hosted OSS: free, MIT licensed (excluding the `enterprise/` directory).
Enterprise: quote-based license scoped to deployment size, adding SSO/SCIM, audit logs, organization RBAC, IP allowlists, multi-region deployment, and secret-manager integration; SSO is free for up to 5 users.
Standard enterprise support is included with the license, and 24/7 SLAs (Sev 0 in 1 hour) cost extra.
No model-access fees: providers bill tokens directly and LiteLLM takes no cut, as of 2026-10-02.

## Compared to

[OpenRouter](../openrouter/index.md) is the hosted counterpart: the same multi-provider idea, but someone else runs it and takes a 5.5% credit fee; choose LiteLLM when data residency or key custody rules out a third party.
[OpenCode Zen](../opencode-zen/index.md) sells curation of benchmarked endpoints; LiteLLM sells control, with no curation guarantee.
[Requesty](../requesty/index.md) is the category's other hosted gateway, lighter to adopt; LiteLLM wins on self-hosting and enterprise controls.

## Bottom line

Recommended for platform teams that must keep provider keys and logs inside their own perimeter, or that need per-team budgets across many providers.
Not for a single-provider setup or a small project, where the gateway is operational overhead without a payoff.
My disagreeable claim: below three providers, self-hosting LiteLLM is negative value, because you are running a stateful service to avoid editing a base URL.

## Changes

- 2026-09-27 - Created when the owner's GitHub-stars scan surfaced it.
- 2026-10-06 - Converted the Compared-to cross-references from plain-text paths into working links.
- 2026-10-07 - Added the BerriAI/litellm star history chart to the Status section.
- 2026-10-16 - Release train refresh: the v1.105 line went stable with PyPI latest at 1.105.1 (2026-10-14), the first stable minor past 1.104.2, and the GitHub train advanced to v1.106.0-rc.4 (2026-10-15) and v1.107.0-dev.3 (2026-10-16); stars refreshed to 61,356.
- 2026-10-18 - Release train refresh: v1.106.0 left pre-release and went stable on 2026-10-18 (v1.103.5 patched 2026-10-17 behind it) with v1.107.0-dev.3 still on the train; stars stand at their 2026-10-16 verification.
- 2026-10-19 - Release train refresh: v1.107.0-rc.1 published 2026-10-18, the first rc on the v1.107 line, and PyPI latest moved to 1.106.0; stars stand at their 2026-10-16 verification.
- 2026-10-21 - Release train refresh: v1.106.1 went stable 2026-10-20 with v1.105.2, v1.104.4, and v1.103.6 patched the same day and v1.107.0-rc.2 on the train; PyPI latest moved to 1.106.1; stars stand at their 2026-10-16 verification.
- 2026-10-23 - Release train refresh: v1.106.2 went stable 2026-10-21 with v1.105.3, v1.104.5, and v1.103.7 patched the same day and v1.107.0-rc.2 still the train head; PyPI latest moved to 1.106.2 and the repo pushed 2026-10-23; stars stand at their 2026-10-16 verification.
- 2026-10-25 - Release train refresh: v1.106.3 went stable 2026-10-24 with v1.105.4, v1.104.6, and v1.103.8 patched the same day and v1.107.0-rc.2 still the train head; PyPI latest moved to 1.106.3 and the repo pushed 2026-10-25; stars stand at their 2026-10-16 verification.
- 2026-10-26 - Release train refresh: v1.106.4 went stable 2026-10-25 with v1.105.5, v1.104.7, and v1.103.9 patched the same day and v1.107.0-rc.2 still the train head; PyPI latest moved to 1.106.4 and the repo pushed 2026-10-26; stars stand at their 2026-10-16 verification.
- 2026-10-28 - Release train refresh: v1.106.5 went stable 2026-10-27 with v1.105.6, v1.104.8, and v1.103.10 patched the same day; PyPI latest moved to 1.106.5 and the train head jumped two lines to v1.109.0-dev.1 (2026-10-28), the v1.107 line never having passed rc.2 and no v1.108 tag existing at all; the repo pushed 2026-10-28; stars stand at their 2026-10-16 verification.
- 2026-10-29 - Release train refresh: v1.106.6 went stable 2026-10-28 with v1.105.7 patched the same day; PyPI latest moved to 1.106.6 and the v1.108 line, which had never been tagged, got its first rc with v1.108.0-rc.1 published 2026-10-29, so the train now carries both a v1.108 rc and the v1.109 dev tag; the repo pushed 2026-10-29; stars stand at their 2026-10-16 verification.
- 2026-11-01 - Release train refresh: v1.109.0-dev.2 published 2026-10-30 as the new train head, with v1.106.6 stable still the latest release and PyPI latest at 1.106.6; the repo pushed 2026-11-01; stars stand at their 2026-10-16 verification.
- 2026-11-04 - Release train refresh: v1.108.0 went stable on 2026-11-04, the line that had sat at rc.1 since 2026-10-29, with the v1.107 line never reaching stable at all, v1.106.7 patched the same day, and v1.109.0-rc.1 published as the train head; PyPI latest moved to 1.108.0 and the repo pushed 2026-11-04; stars stand at their 2026-10-16 verification.
- 2026-11-07 - Release train refresh: v1.108.1 (2026-11-05) and v1.108.2 (2026-11-06) patched the stable line with PyPI latest moving to 1.108.2, the never-stable v1.107 line got v1.107.0-rc.3 (2026-11-05) carrying two GitHub Copilot per-user fixes, and v1.110.0-dev.1 (2026-11-07) became the train head with the v1.109 line still holding at rc.1; the release notes also record that after "the Oct 21 incident (#47826)" the project replaced the cosign key signing its Docker images, so releases now carry pinned-key cosign verification; the repo pushed 2026-11-07; stars stand at their 2026-10-16 verification.
- 2026-11-08 - Release train refresh: v1.108.3 (2026-11-07) patched the stable line as an LTS release (11 PRs, 3 fixed, an AWS Bedrock request failure among them) with PyPI latest moving to 1.108.3, and v1.110.0-dev.2 (2026-11-08) became the train head with the v1.109 line still holding at rc.1; the repo pushed 2026-11-08; stars stand at their 2026-10-16 verification.
- 2026-11-12 - Release train refresh: v1.108.5 (2026-11-10) patched the stable line while v1.104.9 and v1.103.11 patched lines outside the four-recent-minors window, the v1.109 line went stable on 2026-11-11 with v1.109.0 (v1.106.8 patched the same day and v1.110.0-rc.1 published), and 2026-11-12 brought v1.109.1, v1.108.6, and v1.106.9 patches with v1.110.0-rc.2 as the train head; PyPI latest moved to 1.109.1 and the repo pushed 2026-11-12; stars stand at their 2026-10-16 verification.
- 2026-11-14 - Release train refresh: v1.108.7 landed later on 2026-11-12, the train head jumped the never-stable v1.110 line to v1.111.0-dev.1 (2026-11-13) and v1.111.0-dev.2 (2026-11-13) while v1.108.8 patched the v1.108 line that evening, and v1.106.10 landed 2026-11-14; PyPI latest held at 1.109.1 and the repo pushed 2026-11-14; stars stand at their 2026-10-16 verification.
- 2026-11-15 - Release train refresh: v1.108.9 (2026-11-14 evening) patched the stable line with a v1.107.0-rc.4 published behind it, then 2026-11-15 brought v1.110.0-rc.3 (the v1.110 line's first rc after its two dev tags) and v1.111.0-dev.3 and v1.111.0-dev.4 taking the train head; PyPI latest held at 1.109.1 and the repo pushed 2026-11-15; stars stand at their 2026-10-16 verification.
- 2026-11-17 - Release train refresh: v1.108.10 (2026-11-16) patched the v1.108 line, PyPI latest held at 1.109.1, and the repo pushed 2026-11-17; stars stand at their 2026-10-16 verification.
- 2026-11-21 - Release train refresh: the v1.110 line went stable on 2026-11-19 (v1.110.1: the GPT-6.2 prompt-caching fix for system prompts sent with `store: false`, a slim-nginx UI image, and a Wolfi base bump) with v1.109.2, v1.108.12, and v1.106.11 patched the same day and v1.111.0-rc.2 on the train, then 2026-11-20 brought v1.110.2, v1.109.3, v1.108.13, v1.106.12, v1.111.0-rc.3, and a v1.112.0-dev.1 train head, with v1.108.14 landing that evening; PyPI latest moved to 1.110.2 (2026-11-20) and the repo pushed 2026-11-21; stars stand at their 2026-10-16 verification.
- 2026-11-22 - Release train refresh: v1.112.0-dev.2 (2026-11-21) took the train head and v1.108.15 (2026-11-21) patched the v1.108 line as an LTS release (9 PRs, 1 added, 2 fixed: the ResetData provider, a Groq and Meta transcription $0-spend fix, and keyless JSON-configured deployments now returning 401 until an api_key is set, marked action required); PyPI latest held at 1.110.2 and the repo pushed 2026-11-22; stars stand at their 2026-10-16 verification.
- 2026-11-24 - Release train refresh: v1.108.16 (2026-11-23) patched the v1.108 LTS line (44 PRs, among them litellm_proxy decision support, Bedrock runtime endpoint routing, Gemini prompt-caching and batch-embedding billing fixes, and the gateway DCR opt-in marked breaking), v1.110.3 (2026-11-24, 5 PRs) and v1.109.4 (2026-11-24, 2 PRs) carried the same DCR backport to their lines with audit log fixes and router fallback by routed group on v1.110.3, the train head held at v1.112.0-dev.2, PyPI latest moved to 1.110.3, and the repo pushed 2026-11-24; rotation re-verification with all nine cited URLs re-fetched live and nothing else moved; stars stand at their 2026-10-16 verification.

## See also

- [OpenRouter](../openrouter/index.md) - the hosted gateway most teams compare against this one.
- [OpenCode Zen](../opencode-zen/index.md) - the curated-endpoint counterpoint to uncurated self-hosting.
- [Requesty](../requesty/index.md) - the category's other hosted gateway.
- [OpenCode](../../harnesses/opencode/index.md) - a coding harness that consumes gateways like this one.
- [Model provider feature matrix](../../model-provider-feature-matrix/index.md) - where LiteLLM sits among access providers.

## References

- https://api.github.com/repos/BerriAI/litellm - 60,260 stars, Python, license metadata, pushed 2026-10-07 (fetched via the GitHub API, 2026-10-07; re-fetched 2026-10-14 at 61,173 stars; re-fetched 2026-10-19, pushed 2026-10-19; re-fetched 2026-10-21, pushed 2026-10-21; re-fetched 2026-10-23, pushed 2026-10-23; re-fetched 2026-10-24, pushed 2026-10-24; re-fetched 2026-10-25, pushed 2026-10-25; re-fetched 2026-10-26, pushed 2026-10-26; re-fetched 2026-10-28, pushed 2026-10-28; re-fetched 2026-10-29, pushed 2026-10-29; re-fetched 2026-11-01, pushed 2026-11-01; re-fetched 2026-11-04, pushed 2026-11-04; re-fetched 2026-11-07, pushed 2026-11-07; re-fetched 2026-11-08, pushed 2026-11-08; re-fetched 2026-11-12, pushed 2026-11-12; re-fetched 2026-11-14, pushed 2026-11-14; re-fetched 2026-11-15, pushed 2026-11-15; re-fetched 2026-11-17, pushed 2026-11-17, 63,395 stars; re-fetched 2026-11-21, pushed 2026-11-21; re-fetched 2026-11-22, pushed 2026-11-22).
- https://docs.litellm.ai/docs/ - SDK and proxy feature claims, 100+ providers, MCP/A2A gateway, Rust beta (200).
- https://docs.litellm.ai/docs/enterprise - enterprise feature gates, SSO free to 5 users, four-line support window effective 2026-06-29 (200).
- https://raw.githubusercontent.com/BerriAI/litellm/main/LICENSE - MIT text with the enterprise/ directory carve-out (200).
- https://futuresearch.ai/blog/litellm-attack-transcript/ - minute-by-minute discovery of the March 2026 PyPI compromise, payload behavior, PYSEC-2026-2 (200).
- https://hn.algolia.com/api/v1/search?query=LiteLLM&tags=story&hitsPerPage=8 - the 938-point compromise thread, the Mercor/TechCrunch story, the litelm bloat fork (200).
- https://hn.algolia.com/api/v1/items/49662767 - litelm discussion, bloat criticism and rebuttals, 177 points (200).
- https://api.github.com/repos/BerriAI/litellm/releases?per_page=15 - release cadence, four stable lines patched the same day in September 2026 (200; re-fetched 2026-10-18 reading v1.106.0 stable of 2026-10-18 and v1.103.5 of 2026-10-17; re-fetched 2026-10-19 reading v1.107.0-rc.1 of 2026-10-18; re-fetched 2026-10-21 reading v1.106.1, v1.105.2, v1.104.4, and v1.103.6 all of 2026-10-20 plus v1.107.0-rc.2; re-fetched 2026-10-23 reading v1.106.2, v1.105.3, v1.104.5, and v1.103.7 all of 2026-10-21 with v1.107.0-rc.2 still the train head; re-fetched 2026-10-24, same state; re-fetched 2026-10-25 reading v1.106.3, v1.105.4, v1.104.6, and v1.103.8 all of 2026-10-24 with v1.107.0-rc.2 still the train head; re-fetched 2026-10-26 reading v1.106.4, v1.105.5, v1.104.7, and v1.103.9 all of 2026-10-25 with v1.107.0-rc.2 still the train head; re-fetched 2026-10-28 reading v1.106.5, v1.105.6, v1.104.8, and v1.103.10 all of 2026-10-27 with the train head now v1.109.0-dev.1 of 2026-10-28; re-fetched 2026-10-29 reading v1.106.6 and v1.105.7 both of 2026-10-28 with v1.108.0-rc.1 published 2026-10-29; re-fetched 2026-11-01 reading v1.109.0-dev.2 of 2026-10-30 as the train head, v1.106.6 still the latest stable; re-fetched 2026-11-04 reading v1.108.0 stable of 2026-11-04, v1.106.7 of 2026-11-04, and v1.109.0-rc.1 of 2026-11-04 as the train head; re-fetched 2026-11-07 reading v1.108.1 of 2026-11-05, v1.107.0-rc.3 of 2026-11-05 with the cosign key-replacement notice, v1.108.2 of 2026-11-06, and v1.110.0-dev.1 of 2026-11-07 as the train head; re-fetched 2026-11-08 reading v1.108.3 of 2026-11-07 and v1.110.0-dev.2 of 2026-11-08 as the train head; re-fetched 2026-11-12 reading v1.108.5 of 2026-11-10 with v1.104.9 and v1.103.11 patches the same day, v1.109.0 stable of 2026-11-11 with v1.106.8 and v1.110.0-rc.1, and v1.109.1, v1.108.6, v1.106.9, and v1.110.0-rc.2 all of 2026-11-12; re-fetched 2026-11-14 reading v1.108.7 of 2026-11-12, v1.111.0-dev.1 and v1.111.0-dev.2 of 2026-11-13 with v1.108.8 that evening, and v1.106.10 of 2026-11-14; re-fetched 2026-11-15 reading v1.108.9 of 2026-11-14 evening with v1.107.0-rc.4, then v1.110.0-rc.3 and v1.111.0-dev.3 and v1.111.0-dev.4 of 2026-11-15 as the train head; re-fetched 2026-11-17 reading v1.108.10 of 2026-11-16 the newest stable with the train head unchanged; re-fetched 2026-11-21 reading the v1.110 line stable (v1.110.1 of 2026-11-19, v1.110.2 of 2026-11-20), the v1.109.2/v1.109.3, v1.108.12/v1.108.13/v1.108.14, and v1.106.11/v1.106.12 patches, v1.111.0-rc.2 and v1.111.0-rc.3, and v1.112.0-dev.1 of 2026-11-20 as the train head; re-fetched 2026-11-22 reading v1.112.0-dev.2 of 2026-11-21 as the train head and v1.108.15 of 2026-11-21, an LTS patch with the keyless-deployment 401 action-required notice).
- https://pypi.org/pypi/litellm/json - PyPI latest at 1.106.2, published 2026-10-21 (200, re-checked 2026-10-23 and 2026-10-24; re-checked 2026-10-25 reading 1.106.3, published 2026-10-24; re-checked 2026-10-26 reading 1.106.4, published 2026-10-25; re-checked 2026-10-28 reading 1.106.5, published 2026-10-27; re-checked 2026-10-29 reading 1.106.6, published 2026-10-28; re-checked 2026-11-01, 1.106.6 unchanged; re-checked 2026-11-04 reading 1.108.0, published 2026-11-04; re-checked 2026-11-07 reading 1.108.2, published 2026-11-06; re-checked 2026-11-08 reading 1.108.3, published 2026-11-07; re-checked 2026-11-12 reading 1.109.1, published 2026-11-12; re-checked 2026-11-15, 1.109.1 unchanged; re-checked 2026-11-17, 1.109.1 still latest; re-checked 2026-11-21 reading 1.110.2, published 2026-11-20; re-checked 2026-11-22, 1.110.2 still latest).
