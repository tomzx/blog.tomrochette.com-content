---
title: CrowdStrike Falcon Guardian
created: 2026-10-04
updated: 2026-11-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, governance, security]
readability: 3
audience_notes: >
  Security engineers and platform teams deciding whether an endpoint-security
  vendor can also govern their AI agents. Assumes familiarity with CrowdStrike
  Falcon and with what agent governance layers do.
---

CrowdStrike Falcon Guardian is a commercial AI detection and response (AIDR) capability that discovers AI agents, turns AI usage policy into enforceable controls, and protects autonomous agents at runtime where they execute, anchored in the Falcon endpoint sensor and extending to cloud and SaaS.

## What it is

Falcon Guardian launched at Fal.Con 2026 as CrowdStrike's agent-security layer: shadow-AI discovery, prompt-to-action tracing, governance controls, and runtime protection against prompt injection and poisoned tools.
It connects AI activity with endpoint telemetry, so a user prompt can be followed into the downstream processes and system actions it caused.
Coverage is pitched across endpoint, cloud, and SaaS.
At Fal.Con Europe on 2026-11-03 the vendor made the Falcon AI Gateway generally available and included it with Guardian, made agent-level hooks available for Claude Code, OpenAI Codex, GitHub Copilot, OpenCode, and Cursor, and shipped an AI kill switch that cuts model access off at the gateway; cloud coverage (Linux, cloud workloads, Kubernetes, Amazon Bedrock AgentCore) and a Claude Cowork integration are pre-beta.
There is no public repo, no version number, and no public price; distribution is the Falcon platform and its sales motion.

## Status

New and vendor-controlled: announced at Fal.Con 2026 (September 2026), expanded at Fal.Con Europe 2026-11-03 with the AI gateway, agent-level hooks, and the kill switch live per the vendor's announcement blog.
The 99 percent prompt-attack efficacy and sub-100-millisecond latency claims that carried the launch page no longer appear on it as of 2026-11-07 (the page was reworked around the Europe announcements); no independent test of any efficacy figure has appeared.
The product page now carries named customers (Cogentrix, TaxSlayer), and detection is attributed to SafeMind models built with NVIDIA, all vendor-supplied.
Community response started skeptical: the r/crowdstrike thread asks what happens to agents that do not run on managed endpoints and reads the product as sensor-bound, which is the objection this category's endpoint-anchored entrants always face.

## Strengths

- **Enforcement at the point of execution closes the gap that dashboard-only governance leaves open, and endpoint telemetry is a genuine data advantage for seeing what agents did.**
- Prompt-to-action tracing answers the question governance boards usually cannot: which instruction caused which system change.
- Distribution is unfriendly but undeniable: organizations already running Falcon get agent security through a console they already operate.
- Discovery of shadow AI use, including token consumption visibility, addresses the adoption problem before the policy problem.

## Cautions

- The anchor is the endpoint: agents running in containers, CI, cloud shells, or unmanaged machines are outside the sensor's sight, which is exactly where much agentic coding work happens.
  The agent-level hooks answer part of this for five coding agents, and the cloud coverage that answers the rest is pre-beta.
- Every performance figure is self-reported, and the product is three months old, so nothing has an independent record yet.
- Closed and quote-priced: no repo, no version, no public per-agent price, and procurement goes through the Falcon platform relationship.
- The AI gateway is now generally available and included with Guardian per the vendor's blog, but every capability description still comes from the vendor, so verify its scope in a pilot.

## Pricing

Quote-based per-endpoint Falcon licensing; CrowdStrike publishes no standalone price for Falcon Guardian or the AI gateway capability.
Without stated prices there is no price history to track.

## Compared to

- Microsoft Agent Governance Toolkit is the open-source counterpart: deterministic policy and identity you run yourself, no sensor required, but no telemetry estate behind it either.
- Databricks Unity Gateway governs at the model and MCP request boundary instead of the endpoint, which covers agents on any machine but never sees what happened on the host afterwards.
- Veto is the minimal in-process kernel for teams who want authorization receipts without a platform relationship.

## Bottom line

Recommended for organizations already inside the Falcon estate that want agent governance tied to endpoint reality and can accept closed, quote-priced, weeks-old software.
Not for teams whose agents run outside managed endpoints, and not for anyone who needs public prices, public code, or independent benchmarks before adopting a control plane.

## Changes

- 2026-10-04 - Created.
- 2026-10-16 - Rotation re-verification: every reference re-fetched, the product page still carrying the 99 percent prompt-attack efficacy and sub-100-millisecond claims plus the AI gateway announcement, the docs path still a client-rendered shell, and the Reddit thread still blocking scripted fetches; no drift found.
- 2026-10-23 - Rotation re-verification: every reference re-fetched, the product page still carrying the 99 percent and sub-100-millisecond internal-benchmark claims with the AI gateway still marked coming soon, the launch blog (September 1) and AIDR solution page unchanged, the docs path still a client-rendered shell, and the Reddit thread still 403 to scripted fetch; no drift found.
- 2026-10-30 - Rotation re-verification: every reference re-fetched with the same result set, the product page still carrying the internal-benchmark claims with the AI gateway still marked coming soon (the FAQ now naming 200-plus prompt-injection techniques), the launch blog and AIDR solution page unchanged, the docs path still a client-rendered shell, and the Reddit thread still 403 to scripted fetch; no drift found.
- 2026-11-07 - Full rotation re-verification with drift: the product page and solution page were reworked for the Fal.Con Europe 2026-11-03 announcements, the 99 percent and sub-100-millisecond claims no longer appear on either page, the Falcon AI Gateway is now generally available and included with Guardian, agent-level hooks are available for Claude Code, OpenAI Codex, GitHub Copilot, OpenCode, and Cursor, an AI kill switch shipped at gateway enforcement, cloud coverage and the Claude Cowork integration are pre-beta, and named customers and the SafeMind-with-NVIDIA attribution were added; the launch blog (September 1) unchanged, the docs path still a client-rendered shell, the Reddit thread still 403 to scripted fetch, and the Fal.Con Europe advances blog added as a reference.
- 2026-11-14 - Full rotation re-verification: every reference re-fetched and live, no drift (the product page still carrying the gateway GA, the five-agent hooks, the live kill switch with per-agent-type gateway enforcement as coming soon, Agent Graph, the SafeMind attribution, and the Cogentrix and TaxSlayer customer stories; the launch blog and the Fal.Con Europe advances blog unchanged; the docs path still a client-rendered shell; the Reddit thread still 403 to scripted fetch).

## See also

- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md) - the open-source enforcement-side counterpart and the category's closest architectural contrast.
- [Databricks Unity Gateway](../databricks-unity-gateway/index.md) - the other commercial platform-layer entrant, governing at the request boundary instead of the endpoint.
- [Veto](../veto/index.md) - the minimal authorization kernel for teams rejecting platform relationships entirely.
- [Paperclip](../paperclip/index.md) - the self-hosted extreme of the category: governance inside a company runtime you own.

## References

- https://www.crowdstrike.com/en-us/platform/falcon-guardian-aidr/ - product page: AIDR positioning, shadow-AI discovery, prompt-to-action tracing, the 99 percent and sub-100ms claims, and the AI gateway announcement, fetched 2026-10-04.
- https://www.crowdstrike.com/en-us/blog/falcon-guardian-defines-next-generation-of-ai-security/ - launch blog defining discovery, governance, data protection, runtime security, investigation, and response as the product's scope, fetched 2026-10-04.
- https://www.crowdstrike.com/en-us/solutions/ai-detection-and-response/ - the AIDR solution page grounding the endpoint-telemetry connection claim, fetched 2026-10-04.
- https://docs.crowdstrike.com/help/falcon-guardian - official documentation path (200, client-rendered application shell; content not extractable by script this run).
- https://www.reddit.com/r/crowdstrike/comments/1w5ovkv/crowdstrike_falcon_guardian_secure_ai_agents/ - the skeptical community thread on endpoint-bounded coverage (403 to scripted fetch; content read via search this run).
- https://www.crowdstrike.com/en-us/blog/crowdstrike-advances-ai-security-and-safety-falcon-guardian/ - the Fal.Con Europe 2026-11-03 announcement grounding the gateway GA, the agent hooks, the AI kill switch, the pre-beta cloud coverage, and the SafeMind attribution.
