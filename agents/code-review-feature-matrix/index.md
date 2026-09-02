---
title: "Code Review Feature Matrix"
created: 2026-08-30
updated: 2026-09-02
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, code-review, ai-review, developer-tools]
readability: 3
audience_notes: >
  Engineers shortlisting an AI code reviewer for their repositories who need the capability deltas at a glance.
  Assumes you know what a GitHub check, a learned-rules loop, and BYOK mean; each column links to a full note with sources.
---

This matrix compares the eight AI code-review tools profiled in this section, feature by feature, so the shortlisting step does not require reading eight notes.
Everything below was re-verified against live sources on 2026-09-02; the three columns added on 2026-08-30 were Graphite Diamond, Kodus, and Sourcery.

**The deciding row is not review quality, which nobody has independently benchmarked, but where your code runs: five columns are vendor clouds, one runs in your VPC, two run entirely on your infrastructure with your keys, Graphite Diamond arrives already consolidated as a Cursor property, and the category's most-repeated outside fact is that the two biggest commercial reviewers both have Kudelski-disclosed exploit histories.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified as of the date above.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [CodeRabbit](../coderabbit/index.md) | [Ellipsis](../ellipsis/index.md) | [Graphite Diamond](../graphite-diamond/index.md) | [Greptile](../greptile/index.md) | [Kodus](../kodus/index.md) | [OpenCodeReview](../open-code-review/index.md) | [Qodo](../qodo/index.md) | [Sourcery](../sourcery/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | commercial review service expanding into change management | agent cloud, review demoted to a use case | AI review inside the Graphite stacked-PR platform, now Cursor-owned | hosted reviewer over a whole-repo graph index | open-source BYOK reviewer (Kody) with a paid cloud | self-hosted hybrid rules-plus-LLM reviewer | open-core reviewer, MIT PR-Agent plus paid Qodo Merge | hosted reviewer from a static-analysis lineage, proprietary app over an MIT repo |
| Object judged | pull requests (diff plus learned repo context) | pull requests, as one configurable agent use case | pull requests in the stacked-PR workflow | pull requests against the full codebase graph | pull requests on GitHub, GitLab, Bitbucket, and Azure Repos | git diffs and pull requests in CI | pull requests via /review and /improve commands | pull requests on GitHub and GitLab, plus a security-scan layer |
| Judge | LLM reviewers with team-learned rules | your chosen coding agent under its agents-as-code config | Graphite Agent (ex-Diamond) with custom rules | review agent swarm reading the team's comment history | your BYOK model with plain-language custom rules | deterministic rules first, LLM agent second, precision-first | LLM with configurable best-practices files | LLM reviewers on OpenAI and Anthropic models |
| Deployment | GitHub/GitLab app, IDE, CLI, Enterprise self-host | cloud with BYOC into your AWS VPC, REST API with public Python and TypeScript SDK mirrors | graphite.dev SaaS, GitHub-centric, GHES support on Enterprise | cloud, self-host in your own AWS or air-gapped VPC | self-hosted, Kodus Cloud, or CLI, on your own model keys | self-hosted CLI, CI, agent plugins, MCP, your model keys | self-host PR-Agent, or buy Qodo cloud | GitHub/GitLab app and IDE plugins, Enterprise self-host |
| CI gating | ✓ | ~ through its cloud runs | ? | ✓ | ✓ CLI in CI/CD | ✓ GitHub Action and GitLab CI | ✓ via CI recipes | ? |
| Fixes or rewrites code | ~ Triage and Change Stack agents (2026 expansion) | ~ the agents it hosts fix what review finds | ~ one-click fixes | ~ handoff to Claude Code, Cursor, Codex, Devin, TREX tests beta | ✗ comments only | ✗ comments only | ~ /improve suggestions | ~ agent-assisted fix path |
| Learns team rules | ✓ learnings | ~ agents-as-code config you write | ~ custom rules | ✓ from review comments, isolated per organization | ✓ plain-language rules, workflow learning | ✗ fixed rule pipeline | ~ best-practices files you curate | ? |
| License | ✗ proprietary, free forever for public repos | ✗ closed core, small OSS tooling repos | ✗ proprietary, Cursor-owned | ✗ proprietary | ~ AGPL-3.0 core, ee/ paths commercial | ✓ Apache-2.0 | ~ PR-Agent MIT, Qodo Merge proprietary | ✗ reviewer proprietary, the MIT repo is the refactoring lineage |
| Pricing anchor | Essentials (ex-Pro) $24, Team (ex-Pro Plus) $48 per user/mo annual, new Advanced $72 annual ($90 monthly) with variable-priced full scans, public repos free | tokens at cost plus a 10% fee, support packages from $5k/mo | Hobby free, Starter $20, Team $40 per user/mo | $30/seat plus credits, $1 per extra credit | Community free, Teams BYOK $10/dev/mo plus raw tokens, Enterprise custom with SOC 2, self-host free | free, your model tokens | $0.012 per credit packs, Pro Team $30, no permanent free tier | Pro $12, Team $24 per user/mo, open source repos free |
| Maturity and scale | $143M Series C at a $1.5B valuation, 17k customers (2026-08) | pivoted 2026-07, $2M seed (2024) | ~$81M raised, $290M valuation, acquired by Cursor 2025-12 | $25M Series A (2025-09), v5 | 1,346 stars, no verified funding (2026-09) | 116 releases in under 4 months | 12.8k-star OSS repo, $50M raised | repo since 2019, 1,858 stars, no verified funding |

## Reading the matrix

**Platform-native review is the threat the columns do not price in: Copilot's built-in reviewer overtook CodeRabbit on monthly PR volume by November 2025 per Pullflow's 40.3M-PR analysis, and every vendor here is selling against a checkbox your forge already ships.**
CodeRabbit still led cumulative 2025 volume, 632,256 to 561,382 distinct PRs, so the overtake is a rate, not a fait accompli, but it is the category's only independent market-share number.

**A reviewer holds privileged access, and the category's record proves it.**
Kudelski Security turned a malicious RuboCop config into RCE and write access on one million CodeRabbit-connected repositories in January 2025, and found a PR-comment-to-AWS-admin-key chain in Qodo Merge Pro the same year, both fixed after disclosure.
The caution is structural: whatever judges your code can execute in your CI context, so treat every column here as a privileged integration, not a linter.

**The license row is the cost row in disguise.**
The three open paths, Apache-2.0, MIT PR-Agent, and Kodus's AGPL-3.0, trade turnkey convenience for wiring and model-token spend, and Kodus's badge is the narrowest of the three, since everything under its ee/ paths is commercially licensed.
Qodo's own README draws the line bluntly: the donated PR-Agent repo is a community-maintained legacy project, not the commercial free tier.
Greptile's self-hosting runs in your cloud but stays proprietary, so the VPC row buys data residency, not code ownership, and Sourcery's MIT badge covers the 2019 refactoring repo, not the reviewer.

**Review-alone is a hard business, and Ellipsis is the exit record.**
It launched as a 121-point Show HN review bot in 2024 and pivoted to managed agent infrastructure in July 2026, keeping review only as a configurable use case.

## Choosing from the matrix

- Turnkey cross-repo review with learned rules and a GitLab story: CodeRabbit, free on public repos, per-seat on private ones.
- Code that must never touch a vendor cloud: OpenCodeReview, Apache-2.0 with your own keys, Kodus, AGPL-3.0 with your own keys and a flat platform fee, or MIT PR-Agent if you accept its community-maintenance status.
- Whole-repo graph context and house-rule enforcement without building it: Greptile, self-hosted in your own VPC.
- Already running Graphite's stacked-PR workflow: Graphite Agent adds review without adding a vendor, now with Cursor behind it.
- Free review for open-source repos or the cheapest paid seat: Sourcery, $12 with security scans bolted on.
- Already running many coding agents and want managed infrastructure with transcripts and budget caps: Ellipsis Agent Cloud, review included as a use case.
- GitHub-all-in and price-sensitive: Copilot's platform-native reviewer, covered inside the VS Code note, now leads monthly volume; measure whether its depth beats the dedicated columns before paying for one.

## See also

- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the neighboring quality-control category, evals and observability rather than PR review
- [Agentic Coding Tools Landscape](../agentic-coding-tools-landscape/index.md) - where review sits in the four-layer map
- [Plannotator](../plannotator/index.md) - the human-annotation counterpart to machine review
- [Rethinking Code Review in the Age of LLMs](../../rethinking-code-review-in-the-age-of-llms/index.md) - the corpus essay this category answers
- [Code Review Without Reading the Code](../../code-review-without-reading-the-code/index.md) - the corpus case for machine-scale review

## References

- https://pullflow.com/state-of-ai-code-review-2025 - the independent 40.3M-PR market-share analysis grounding the Copilot-overtake claim
- https://kudelskisecurity.com/research/how-we-exploited-coderabbit-from-a-simple-pr-to-rce-and-write-access-on-1m-repositories - the CodeRabbit exploit chain
- https://kudelskisecurity.com/research/qodo-dynaconf-aws-admin-key-leaked-twice - the Qodo Merge Pro exploit chain
- https://www.coderabbit.ai/pricing - the CodeRabbit pricing column
- https://kodus.io/pricing/ - the Kodus pricing column
- https://www.qodo.ai/pricing/ - the Qodo pricing column
- https://ellipsis.dev/pricing - the Ellipsis pricing column
- https://greptile.com/ - the Greptile product and pricing column
- https://github.com/alibaba/open-code-review - the OpenCodeReview architecture and license
