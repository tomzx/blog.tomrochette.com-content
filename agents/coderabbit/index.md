---
title: CodeRabbit
created: 2026-08-30
updated: 2026-08-30
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, code-review, ai-review, developer-tools]
readability: 3
audience_notes: >
  Engineers and engineering leads choosing an AI reviewer for pull requests.
  Assumes you know what a pull request is, what a GitHub App's repository permissions grant, and how per-seat SaaS pricing works.
---

CodeRabbit is a commercial AI code review service (the coderabbitai GitHub and GitLab app, plus CLI and IDE surfaces) that reviews every pull request automatically and is expanding into triage, change explanation, and security under the banner of Agentic Change Management.
Facts below verified as of 2026-08-30.

## What it is

**It is the category's default install: the most-installed AI app on GitHub and GitLab, positioned as the independent verifier for code that agents write.**
Reviews run on PRs using a codegraph, dozens of context sources, and a learning loop ("Learnings") that picks up each team's conventions, then loops with coding agents like Claude Code, Codex, Cursor, and Gemini to fix what it flags.
Surfaces cover the pull request (GitHub/GitLab), the IDE (VS Code, Cursor, Windsurf since May 2025), and the terminal (CLI since September 16, 2025), and August 2026 added Triage for prioritizing the PR queue, Change Stack for explaining massive diffs, and Security for post-merge monitoring.
It is proprietary SaaS from CodeRabbit, Inc., founded by Harjot Gill and Gur Singh, with self-hosting reserved for Enterprise and free reviews forever for public repositories.

## Status

**Very active, well-funded, and mid-pivot from reviewer to platform.**
Funding: $16M Series A led by CRV (August 13, 2024), then $60M Series B led by Scale Venture Partners with NVIDIA's NVentures (September 16, 2025, $550M valuation, $88M total raised), then $143M Series C at a $1.5B valuation co-led by Atomico and Smash Capital on August 12, 2026, with revenue up more than 5x year over year per that announcement.
Scale as of 2026-08-30: 17,000+ customers, 6M repositories, and more than 2M reviews per week, versus 2M repos installed and 13M cumulative PR reviews at the Series B a year earlier.

## Strengths

- **Distribution is real and compounding: 6M repositories under review and the top AI-assisted spot on GitHub Marketplace as of 2026-08-30.**
- One reviewer covers every surface code moves through (PR, IDE, CLI, agent handoffs), which is exactly what multi-agent teams need.
- The per-team Learnings loop and 40+ context sources target the false-positive noise that gets these tools turned off.
- Ranked #1 by online F1 in Martian's independent code review benchmark across nearly 300K PRs (vendor-reported, March 2026).
- The open source posture is more than a free tier: $1.2M delivered on the first $1M pledge, and more than $10M committed on August 26, 2026.

## Cautions

- **In August 2025, Kudelski Security published an RCE exploit against CodeRabbit: a malicious .rubocop.yml in a PR executed attacker-controlled Ruby outside the sandbox on production servers, leaked API keys including the GitHub App private key, and could grant read and write access to 1M repositories including private ones.**
- The remediation is verified on both sides: Kudelski disclosed January 24, 2025, CodeRabbit disabled RuboCop within 1 hour, rotated credentials within 3, and shipped the sandboxing fix within 12, and Kudelski's writeup confirms the quick fix while noting other vendors it contacted never responded at all.
- The generalizable lesson: any PR-review SaaS holds write tokens across every repo you install it on, so one vendor bug is one bug across your whole portfolio.
- Critical market-share signal: Pullflow's analysis of 40.3M public PRs found GitHub Copilot overtook CodeRabbit as the top AI reviewer by PRs per month by November 2025, though CodeRabbit still led the cumulative 2025 count (632,256 vs 561,382 distinct PRs), and the metric measures participation, not review quality.
- Competitors position it as the verbose-but-cheaper option (Greptile's founder says switchers cite verbosity and concedes the price point), and the incident's "no customer data was accessed" claim is CodeRabbit's own, not independently verifiable.
- Metering creeps in at the edges: 5 PR reviews per developer per hour on Pro (fair-use capped), and the Slack agent bills $0.50 per agent minute.

## Pricing

**Per-seat pricing with a genuinely free open source tier, as of 2026-08-30.**
Pro is $24 per user per month and Pro Plus is $48 (both billed annually, 14-day free trial), with Enterprise adding SSO, RBAC, API access, EU SaaS, and self-hosting at custom pricing.
CodeRabbit Security is a separate $40 per user per month, the Slack agent is usage-billed at $0.50 per agent minute, and a usage add-on covers unlimited CLI and PR reviews ($0.25 per file reviewed per the CLI FAQ).
Public repositories get reviews free forever, no setup required.

## Compared to

- [Greptile](../greptile/index.md): the review-only rival betting on learned rules and self-hosting in your own VPC; its founder concedes CodeRabbit is cheaper, Greptile's pitch is fewer and sharper comments.
- [OpenCodeReview](../open-code-review/index.md): Alibaba's Apache-2.0 CLI with bring-your-own model keys; choose it when code cannot leave your infrastructure, CodeRabbit when you want turnkey.
- GitHub Copilot code review: platform-native and, per Pullflow, now ahead on monthly PR volume; choose CodeRabbit for cross-repo context, learning loops, and GitLab coverage, Copilot if you are all-in on GitHub and want one fewer vendor.

## Bottom line

**Recommended for teams flooded with agent-generated PRs that want one reviewer covering PR, IDE, and CLI across GitHub and GitLab.**
Not for teams whose threat model rules out a third party holding write tokens across all their repositories, or that need self-hosting below the Enterprise tier.
My disagreeable take: the exploit history makes CodeRabbit more credible, not less, because surviving a public RCE with remediation measured in hours is better operational evidence than any benchmark win, and I would still rather pay this bill than pay the false-negative cost of a human-only queue at agent PR volumes.

## See also

- [Greptile](../greptile/index.md) - the closest hosted rival and its learned-rules counter-bet
- [OpenCodeReview](../open-code-review/index.md) - the self-hosted, license-zero end of the same category
- [Evaluation and Review Feature Matrix](../evaluation-review-feature-matrix/index.md) - the category matrix this note joins
- [Rethinking Code Review in the Age of LLMs](../../rethinking-code-review-in-the-age-of-llms/index.md) - the corpus essay on what review means when agents write the code
- [You Cannot Out-Review a Machine by Hand](../../you-cannot-out-review-a-machine-by-hand/index.md) - why the review queue needed automation in the first place

## References

- https://www.coderabbit.ai/ - product surface, 17K customers and 6M repositories claims as of 2026-08-30
- https://www.coderabbit.ai/pricing - tiers, prices, and rate limits as of 2026-08-30
- https://www.coderabbit.ai/blog/introducing-agentic-change-management - Series C: $143M at a $1.5B valuation, August 12, 2026, 2M weekly reviews, 17K customers, 150K OSS projects, Triage/Change Stack/Security launch
- https://www.coderabbit.ai/blog/coderabbit-series-b-60-million-quality-gates-for-code-reviews - Series B: $60M led by Scale Venture Partners with NVentures, September 16, 2025, 2M repos, 13M PRs reviewed
- https://www.coderabbit.ai/blog/coderabbit-announces-16m-series-a-funding-led-by-crv - Series A: $16M led by CRV, August 13, 2024
- https://www.coderabbit.ai/blog/coderabbit-cli-free-ai-code-reviews-in-your-cli - CLI launch, September 16, 2025
- https://www.coderabbit.ai/blog/coderabbit-expands-its-commitment-to-open-source - the $10M+ open source commitment, August 26, 2026
- https://www.coderabbit.ai/blog/our-response-to-the-january-2025-kudelski-security-vulnerability-disclosure-action-and-continuous-improvement - the vendor's remediation timeline for the exploit
- https://kudelskisecurity.com/research/how-we-exploited-coderabbit-from-a-simple-pr-to-rce-and-write-access-on-1m-repositories - the Kudelski Security writeup, August 19, 2025
- https://pullflow.com/state-of-ai-code-review-2025 - the critical 40.3M-PR market-share analysis
- https://hn.algolia.com/api/v1/items/44953032 - the exploit thread on Hacker News: 687 points, 227 comments, posted August 19, 2025
- https://hn.algolia.com/api/v1/items/42451968 - the Greptile thread where its founder positions CodeRabbit as verbose but cheaper
