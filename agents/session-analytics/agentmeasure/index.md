---
title: AgentMeasure
created: 2026-10-16
updated: 2026-10-31
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, session-analytics, cost-tracking, audit, cli, open-source]
readability: 3
audience_notes: >
  Engineers who need to know whether an AI usage number can survive scrutiny, and anyone comparing audit mechanisms across session analytics.
  Assumes you know what a session log and a token count are.
---

AgentMeasure is a free MIT local CLI that audits coding-agent session records for duplicate records, retry chains, and response conflicts, and re-counts AI support-billing exports against published vendor rules, refusing to turn missing evidence into a zero.

**AgentMeasure's bet is the opposite of every cost report in this category: where they estimate what you spent, it checks whether the record underneath the number can support a claim at all, and marks what the logs cannot decide as UNPROVABLE instead of zero.**

## What it is

A Python 3.9+ CLI (`pip install agentmeasure`, CLI 0.8.0 on PyPI) with two halves that share one evidence discipline.
On 2026-10-30 the project renamed itself Verovo and repositioned its center of gravity on buyer-side verification of AI service charges and delivery: charge review (do the charges match the applicable rules and records) and delivery review (does the work meet the buyer's stated requirements), each reported as separate PASS, FAIL, or UNPROVABLE verdicts.
The session-record checks this note was created for survive as the product's "Developer diagnostics" lane, and the free human-run measurement runs carry over, but the billing half is now the headline and the `verovo` PyPI package did not exist yet as of 2026-10-31 (the CLI installs from the v0.9.0 git tag, while `agentmeasure` 0.8.0 remains the last PyPI publish).
The session half reads local Codex and Claude Code logs: `agentmeasure check` reports duplicate records, retry amplification, and token anomalies, `agentmeasure demo` runs a bundled synthetic session with no account, and `response-audit` (0.8.0) compares usage snapshots for the same response across forked or resumed session files, reporting OBSERVED, CONFLICT, or INCOMPLETE rather than picking a winner.
The billing half re-counts AI customer-support exports (Intercom Fin, Zendesk AI Agents, HubSpot Breeze, Salesforce Agentforce, Ada, plus a generic per-resolution baseline) against each vendor's published rule, pinned and dated in a vendor-rules registry, and builds dispute and recovery packs when a recount disagrees with an invoice.
Around both sits unusual machinery for a tool this age: a conformance pack with PASS, FAIL, and UNPROVABLE verdicts, a core measurement specification and AMS-1 settlement standard, an MCP provider SDK (0.2.0 on npm) for capturing canonical observations, a claims index of dated findings against other tools, and a whitepaper.
Made by roy-tong, an independent developer, under MIT.

## Status

Young and shipping daily: 218 stars, 9 forks, 10 open issues, created 2026-08-16, pushed 2026-10-26 (the claims ledger accrued a delegation roll-up with new bill findings), with v0.6.0 (2026-10-11), v0.7.0 (2026-10-14, the claims index, SDK 0.2.0, and paid diagnosis), v0.7.1, v0.7.2, and v0.8.0 (2026-10-15) landing inside a week, as of 2026-10-26.
On 2026-10-21 the project pivoted to entirely free and open source: the $10 and $20 paid diagnostics were retired, replaced by free human-run measurement runs (bring 20 to 100 sanitized rows, a check usually within 48 hours), the review method behind the runs was open-sourced under docs/review-method/, and the same week's commits added an AMSBench v0.2 benchmark (a 16-injector generator over 5,600 synthetic instances with a rule-engine baseline evaluation) and the first external conformance fixtures from outside providers.
On 2026-10-30 the repository renamed from roy-tong/AgentMeasure to roy-tong/Verovo (the old URL redirects) and tagged v0.9.0, the rename release: the README now leads with buyer-side charge and delivery review over rules, usage and payment records, and delivery evidence, names business and engineering owners accountable for AI spending as its users with coding agents an initial application, and lists a Buyer Ledger of 26 catalog entries and launch case cards against named tools, while the coding-agent session checks moved to a "Developer diagnostics" row of its capability table, as of 2026-10-31 (10 forks, 9 open issues, pushed 2026-10-31).

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=roy-tong/AgentMeasure&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=roy-tong/AgentMeasure&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=roy-tong/AgentMeasure&type=date&legend=top-left" />
</picture>

Its credibility rests on the September audit: roughly 110 AI usage repositories audited 2026-09-06 to 09-09 with synthetic fixtures run through each tool's own parser, 65-plus evidence-backed filings, and fixes merged or accepted upstream, including three members of this category (CodeBurn, Tokscale, and Token Monitor, each fixing a fork or re-emission double-count).
I found no independent coverage beyond the project's own surfaces: a 2-point Show HN on 2026-09-19 and a 1-point companion post, leaving the author's claims index as the main public evidence ledger.
The README states plainly that engineering evidence does not establish paid demand or customer savings, and the response-audit guide adds that real customer adoption is not claimed.
**A solo operation whose audit is also its own demo, so the findings are checkable but the praise is self-graded, and there is not yet an independent verdict on either.**

## Strengths

- The UNPROVABLE state is a genuinely new cell in this category: missing evidence lands in cannot-settle and is never silently zeroed, which is exactly the discipline every estimate-printing tool here lacks.
- The audit produced checkable, merged fixes in three category members' parsers, so the evidence discipline is demonstrated on this category's own tools, not just asserted.
- Duplicate and retry detection answers a question the other members do not ask: not what did this cost, but is this record even countable.
- The billing half pins vendor rules with dated confidence grades and keeps recounts comparable across rule changes, an approach no member takes.
- Entirely free since 2026-10-21: local-only by default, with free human-run measurement runs and an open-sourced review method instead of paid tiers.

## Cautions

- The product's center of gravity has moved out of this category: the 2026-10-30 Verovo rename put buyer-side billing and delivery verification in the headline and demoted the coding-agent checks to a diagnostics lane, and the session half still covers only two harnesses against AgentTrace's thirteen.
- The session audit is self-graded: the conformance pack, the claims index, and the fixtures all come from the same repository, and no audited project endorses the tool.
- The free runs are still one person answering issue #6 and one inbox (first response within 24 hours, checks within 48 hours of a clean sample), so delivery depends on one volunteer, and the pivot left stale paid-service references inside the README and claims page.
- A 2-point Show HN and no independent coverage mean the star curve, not scrutiny, carries the adoption story so far.
- Response-audit reports SHA256 hashes of response IDs, which the guide itself warns can still link records across reports.

## Pricing

Everything is free and open source under MIT: the CLI, the public vendor rules, the conformance pack, the claims index, and, since 2026-10-21, the human-run measurement runs.
The $10 healthcheck diagnosis and $20 metering QA services were retired on 2026-10-21; a free run takes 20 to 100 sanitized rows through the same evidence discipline, usually within 48 hours of a clean sample, started from issue #6 or email.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-16 | Services | Baseline: free MIT CLI and public rules; $10 healthcheck diagnosis and $20 metering QA applied by email, checkout not yet online | https://roy-tong.github.io/Verovo/services.html (then published under the AgentMeasure name) |
| 2026-10-21 | Services | $10 healthcheck and $20 metering QA retired; the project became entirely free, with free human-run measurement runs in their place | https://roy-tong.github.io/Verovo/services.html (then published under the AgentMeasure name) |

## Compared to

- [AgentTrace](../agenttrace/index.md): the thirteen-format local auditor of cost, latency, and failures; AgentMeasure goes narrower (two harnesses) but checks record integrity with an evidence standard AgentTrace does not attempt.
- [ccusage](../ccusage/index.md): the estimate-printing incumbent whose catalog dollars AgentMeasure's own audit class showed can be systematically wrong; ccusage answers what did I spend, AgentMeasure asks whether the number survives scrutiny.
- [agentsview](../agentsview/index.md): the archive for history questions; AgentMeasure audits the integrity of the same records agentsview indexes.

## Bottom line

**Recommended for anyone who needs an AI usage or billing number to carry weight in a dispute, and for Codex and Claude Code users who want their session records checked for duplicates and retry inflation before trusting any report built on them.**
Not for multi-harness coverage, live observation, transcript search, or anyone wanting a cost report rather than an audit.

## Changes

- 2026-10-16 - Created from the 2026-10-15 awesome-agent-observability additions, admitted on its evidence-discipline audit cell, the 110-tool audit with merged fixes in three category members, and eleven fetched sources.
- 2026-10-23 - Rotation re-verification recorded the 2026-10-21 pricing pivot (the paid diagnostics retired for free measurement runs, an open-sourced review method, and the AMSBench benchmark and first external fixtures named in the Status), moved the Pricing and Price history to all-free, and re-fetched every cited URL.
- 2026-10-28 - Recorded the 2026-10-26 push that the 2026-10-26 Status revision had carried without a bullet (the claims ledger's delegation roll-up with new bill findings), with repository state re-verified unchanged today: forks 9 and open issues 10, no release after v0.8.0, and nothing new pushed since 2026-10-26.
- 2026-10-31 - Recorded the rename and pivot: the repository became roy-tong/Verovo on 2026-10-30 with v0.9.0 ("same measure, new name"), the product now leads with buyer-side charge and delivery review while the coding-agent session checks moved to a Developer diagnostics lane; the dead AgentMeasure Pages URLs were repointed to their Verovo locations, every cited URL re-fetched, and repository counts refreshed (forks 9 to 10, open issues 10 to 9, pushed 2026-10-31).

## See also

- [AgentTrace](../agenttrace/index.md) - the wider local audit this tool narrows into record integrity
- [ccusage](../ccusage/index.md) - the incumbent cost report whose estimate class this tool's audit probes
- [Session Analytics Feature Matrix](../session-analytics-feature-matrix/index.md) - the category comparison this note joins
- [agentsview](../agentsview/index.md) - the archive whose indexed records this tool audits

## References

- https://github.com/roy-tong/Verovo - the repository (renamed from roy-tong/AgentMeasure on 2026-10-30, the old URL redirecting), 218 stars and 9 forks as of 2026-10-16, MIT license, created 2026-08-16
- https://raw.githubusercontent.com/roy-tong/Verovo/main/README.md - the two workflows after the rename, the capability table with Developer diagnostics as the coding-agent lane, the Buyer Ledger, and the customer-value disclaimer
- https://roy-tong.github.io/Verovo/services.html - the free-run scopes, the email and issue application flow, and the 2026-10-21 retirement of the paid diagnostics (reached at the Verovo URL 2026-10-31 after the rename moved the pages)
- https://roy-tong.github.io/Verovo/claims.html - the claims index: the five verdict states, the vendor-rule scorecard, and the audit's named findings and clean passes (repointed to the Verovo URL 2026-10-31)
- https://raw.githubusercontent.com/roy-tong/Verovo/main/campaigns/audit-report-2026-09.md - the 110-tool audit, its five bug classes, the landed-fix list, and the methodology and honesty notes
- https://raw.githubusercontent.com/roy-tong/Verovo/main/docs/response-audit.md - the OBSERVED, CONFLICT, and INCOMPLETE verdicts, the ID hashing, and the no-adoption-claimed admission
- https://pypi.org/pypi/agentmeasure/json - the CLI package, latest 0.8.0, MIT, Python 3.9 or newer, first upload 2026-09-18 (still the newest PyPI publish after the 2026-10-30 rename; the verovo package did not exist yet, checked 2026-10-31)
- https://registry.npmjs.org/@agentmeasure/mcp - the provider SDK package, latest 0.2.0, created 2026-10-10 (the renamed SDK publishes as @verovo/mcp 0.3.0 with v0.9.0)
- https://api.github.com/repos/roy-tong/Verovo/releases - v0.9.0 (2026-10-30, the rename release: same measure, new name, SDK to 0.3.0), v0.8.0 through v0.6.0 (2026-10-11 to 2026-10-15)
- https://hn.algolia.com/api/v1/search?query=AgentMeasure - the 2-point Show HN of 2026-09-19 behind the thin-footprint claim
- https://github.com/getagentseal/codeburn/pull/1264 - the merged CodeBurn fix from the audit, grounding the category-member claim
- https://github.com/junhoyeo/tokscale/issues/1306 - the Tokscale fork double-count finding, fixed the same day
- https://github.com/Javis603/token-monitor/issues/627 - the Token Monitor fork dedup finding, closed completed
