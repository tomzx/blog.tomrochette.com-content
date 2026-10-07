---
title: Flowise
created: 2026-09-29
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, workflow, low-code]
readability: 3
audience_notes: >
  Engineers who used or were considering Flowise, and anyone tracking why the visual LLM-workflow genre is contracting.
  Assumes you know what a drag-and-drop LLM builder is.
---

Flowise was the drag-and-drop visual builder for LLM applications that reached 55,492 stars, was acquired by Workday in August 2025, and was archived in August 2026 (GitHub API, as of 2026-10-02).

**Flowise's shutdown note is the clearest public post-mortem of the visual-workflow genre: its own team wrote that coding agents made rigid low-code workflows obsolete.**

## What it is

A visual builder that wrapped LangChain and LlamaIndex into chatflows and agentflows you could assemble on a canvas and self-host from Node (`flowise` 3.1.4 on npm).
It launched publicly in April 2023, was built by FlowiseAI Inc, and claimed millions of downloads and 42,000+ GitHub stars by the time Workday announced the acquisition on 2025-08-14 (Workday newsroom).
The license was Apache 2.0 with the enterprise directory under a commercial license.

## Status

Dead, archived by its maintainers.
The README carries the banner "Flowise has been archived. Refer to Future of Flowise discussion 6727", and that discussion states the reason: developers increasingly rely on coding agents for complex tasks, and "the typical rigid workflow low-code approach quickly hits the limit when it comes to complexity" (GitHub API, 2026-08).
The last release was flowise@3.1.4 on 2026-07-29 and the last push 2026-08-13; the HN thread "Flowise is shutting down" drew 58 points on 2026-08-05.
npm still recorded 11,150 downloads in the month ending 2026-10-01, residual installs from a user base with nowhere to go.

[![Star History Chart](https://api.star-history.com/chart?repos=FlowiseAI/Flowise&type=date&legend=top-left)](https://www.star-history.com/?repos=FlowiseAI%2FFlowise&type=date&legend=top-left)

## Strengths

- At its peak it was the easiest on-ramp to LangChain and LlamaIndex, which is how it accumulated 55k stars.
- Self-hosting was genuinely simple (one npm package, one command), so a long tail of internal tools still runs on it.
- The acquisition price of attention (a Workday newsroom announcement) validated how many enterprises had built on it.

## Cautions

- **Archived means unmaintained**: no fixes, no releases, and security issues like the exploited RCE from 2026-04 will never receive a patch.
- Workday absorbed the team and the roadmap toward HR and finance agent building; the OSS is a stranded asset.
- The stated shutdown reason is a strategic warning for every visual-workflow tool in this category, not just this one.
- The community is still installing a dead package, which is exactly how unpatched deployments accumulate.

## Pricing

No active pricing: the project is archived, so its historical free self-host and paid cloud plans no longer exist as offerings.
Existing self-hosted deployments carry only their own model and infrastructure bills.

## Compared to

- [Dify](../dify/index.md): the natural migration target in the genre, with a bigger community and active releases.
- [Sim](../sim/index.md): the younger Apache-2.0 alternative for visual agent workflow building.
- [AutoGPT](../autogpt/index.md): the category's other workflow platform, alive and rebuilding; choose it for autonomous workflows rather than canvas building.

## Bottom line

Not recommended for anything new; this note is a death record in the same register as Crystal and Gas Town.
Recommended only for existing self-hosters planning an exit to Dify or Sim, and for anyone studying why the lowest-code end of the workflow genre died first.

## Changes

- 2026-09-29 - Created when the deferred framework-tier pile from the 2026-09-27 triage resolved.
- 2026-10-07 - Added the FlowiseAI/Flowise star history chart to the Status section.

## See also

- [Dify](../dify/index.md) - the active giant of the genre Flowise led
- [Sim](../sim/index.md) - the clean-license challenger inheriting its use cases
- [AutoGPT](../autogpt/index.md) - the surviving workflow-platform peer
- [Crystal](../crystal/index.md) - the category's other kept death record

## References

- https://api.github.com/repos/FlowiseAI/Flowise - GitHub API (200): 55,489 stars, 25,049 forks, pushed 2026-08-13, created 2023-03-31 (as of 2026-09-29)
- https://raw.githubusercontent.com/FlowiseAI/Flowise/main/README.md - README (200): "Flowise has been archived" banner (critical source)
- https://api.github.com/repos/FlowiseAI/Flowise/discussions/6727 - shutdown discussion via GitHub API (200): stated reason, coding agents versus rigid low-code (critical source)
- https://hn.algolia.com/api/v1/items/49176920 - "Flowise is shutting down" thread (200): 58 points, 45 comments, 2026-08-05
- https://hn.algolia.com/api/v1/items/47703569 - exploited max-severity RCE thread (200): 3 points, 2026-04-09 (critical source)
- https://newsroom.workday.com/2025-08-14-Workday-Acquires-Flowise,-Bringing-Powerful-AI-Agent-Builder-Capabilities-to-the-Workday-Platform - Workday acquisition press release (200)
- https://hn.algolia.com/api/v1/items/44905403 - acquisition thread (200): 10 points, 2025-08-14
- https://registry.npmjs.org/flowise - npm metadata (200): flowise 3.1.4, license "SEE LICENSE IN LICENSE.md"
- https://api.npmjs.org/downloads/point/last-month/flowise - npm downloads API (200): 11,150 downloads, month ending 2026-10-01
- https://raw.githubusercontent.com/FlowiseAI/Flowise/main/LICENSE.md - license text (200): Apache 2.0 plus commercial-license portions
