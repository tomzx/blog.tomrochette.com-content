---
title: Databricks Unity Gateway
created: 2026-10-02
updated: 2026-10-02
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, control-plane, governance, mcp, enterprise]
readability: 3
audience_notes: >
  Platform engineers who already run Databricks and need one governed door for every model call and MCP tool call their agents make.
  Assumes you know what an LLM gateway does and what Unity Catalog governs.
---

Databricks Unity Gateway is the governance layer, folded into Unity Catalog in April 2026, that routes every model and MCP service request from one control plane with permissions, guardrails, rate limits, budgets, and audit trails.

**Its bet is that agent governance should inherit data governance: the same catalog that already decides who can query a table decides which agent may call which model, MCP server, or API, under whose permissions.**

## What it is

A Databricks platform capability (AWS, Azure, and GCP docs), announced April 15, 2026, when AI Gateway became part of Unity Catalog and took its name.
Every request to a model or MCP server passes through the gateway: service policies (guardrails) run on requests and responses, rate limits apply at endpoint, user, or group level in QPM or TPM, and every call logs to Unity Catalog system tables with actual dollar costs.
MCP servers are first-class securables, with on-behalf-of execution so an MCP call runs with the requesting user's exact permissions instead of a shared service account.
Guardrails cover PII detection and redaction, content safety, prompt-injection detection, data-exfiltration prevention, and hallucination checks, each backed by an editable prompt and model (rolling out in beta), and inference tables capture full request and response payloads for debugging and audit.

## Status

Active and strategic: this is a core Databricks product line, documented across all three clouds, with the April 2026 announcement naming coding agents (Cursor, Codex, Claude Code) as governed callers.
**The gap to know is that coverage is uneven at the edges: rate limits do not apply to `ai_query` batch inference workloads (usage tracking only), output guardrails do not apply to streaming or embeddings, and the platform is unavailable on AWS GovCloud and Azure Government.**
The LLM-judge guardrails and the OpenAI-compatible unified API were still beta in the April announcement.

## Strengths

- One policy surface for models and tools: the same permissions, audit, and tagging model your data already uses, applied to agent traffic.
- On-behalf-of execution is the right default, an agent inherits the human's permissions rather than a god-mode service account.
- Cost attribution lands in system tables with real dollar figures, sliceable by endpoint tag, request tag, identity, or model, which FinOps can query like any other Delta table.
- Inference tables give engineering full payloads for debugging failures, and security gets who-called-what audit trails from the same log.
- Fallback chains route around quota exhaustion and outages without application changes.

## Cautions

- You buy the whole Databricks platform to get it: there is no standalone gateway, so a team not already on the lakehouse is paying for far more than governance.
- The known enforcement gaps matter in production: no rate limiting on batch inference, no output guardrails on streaming, and beta features rolling out region by region.
- The LLM-judge guardrails are prompts plus a model, so guardrail quality tracks model quality and each check adds latency and cost to the calls it inspects.
- Governance depth is Databricks-specific: policies do not follow your agents to another cloud or runtime.
- The renamed lineage (AI Gateway, then Unity Gateway) means older tutorials and configs describe a subset of the current product.

## Pricing

No standalone price list: Unity Gateway is consumed as part of the Databricks platform, billed through its usual usage-based model rather than a separate gateway subscription.

## Compared to

- [Veto](../veto/index.md): Veto intercepts individual tool calls before execution with policy and approvals at the agent-framework layer; Unity Gateway governs the model and MCP traffic from the platform layer instead.
- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md): the toolkit ships deterministic runtime enforcement you deploy; Unity Gateway is a managed capability of a platform you already run.
- [LiteLLM](../../model-access/litellm/index.md): LiteLLM is the self-hosted proxy for model routing and budgets without the catalog, identity, or MCP governance around it.

## Bottom line

**Recommended for teams already on Databricks whose agents now touch models, MCP servers, and governed data in the same request.**
Not for multi-cloud agent fleets, for batch-inference-heavy workloads that need enforced rate limits, or for anyone wanting gateway governance without a lakehouse.

## Changes

- 2026-10-02 - Created.

## See also

- [Control Planes Feature Matrix](../control-planes-feature-matrix/index.md) - the category comparison this note joins
- [Veto](../veto/index.md) - the tool-call interception layer at the agent framework level
- [Microsoft Agent Governance Toolkit](../microsoft-agent-governance-toolkit/index.md) - the deployable runtime-governance counterpart
- [LiteLLM](../../model-access/litellm/index.md) - the standalone model gateway without platform lock-in
- [Model Context Protocol (MCP)](../../protocols/mcp/index.md) - the protocol whose servers this gateway governs

## References

- https://www.databricks.com/blog/ai-gateway-governance-layer-agentic-ai - the April 15, 2026 announcement naming Unity Gateway: MCP governance, on-behalf-of execution, beta guardrails, fallbacks, and system-table cost attribution
- https://docs.databricks.com/aws/en/ai-gateway/ - the AWS documentation hub for AI governance with Unity Gateway
- https://docs.databricks.com/aws/en/ai-gateway/ai-governance - the setup guide: routing, service policies, and rate limits across model and MCP services
- https://docs.databricks.com/aws/en/ai-gateway/rate-limits - the endpoint, user, and group rate-limit mechanics in QPM and TPM
- https://learn.microsoft.com/en-us/azure/databricks/ai-gateway/ - the Azure Databricks mirror confirming cross-cloud documentation
- https://community.databricks.com/t5/generative-ai/ai-query-not-affected-by-ai-gateway-s-rate-limits/td-p/134257 - the vendor-forum confirmation that ai_query batch inference gets usage tracking only (the page 403s to curl, verified through the search excerpt)
- https://datapao.com/databricks-unity-ai-gateway/ - the third-party 2026 guide grounding the regional limits, the GovCloud absence, and the contextual service policies
