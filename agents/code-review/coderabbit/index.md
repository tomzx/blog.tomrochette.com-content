---
title: CodeRabbit
created: 2026-08-30
updated: 2026-11-26
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, llm=glm-5.4, code-review, ai-review, developer-tools]
readability: 3
audience_notes: >
  Engineers and engineering leads choosing an AI reviewer for pull requests.
  Assumes you know what a pull request is, what a GitHub App's repository permissions grant, and how per-seat SaaS pricing works.
---

CodeRabbit is a commercial AI code review service (the coderabbitai GitHub and GitLab app, plus CLI and IDE surfaces) that reviews every pull request automatically and is expanding into triage, change explanation, and security under the banner of Agentic Change Management.

## What it is

**It is the category's default install: the most-installed AI app on GitHub and GitLab, positioned as the independent verifier for code that agents write.**
Reviews run on PRs using a codegraph, dozens of context sources, and a learning loop ("Learnings") that picks up each team's conventions, then loops with coding agents like Claude Code, Codex, Cursor, and Gemini to fix what it flags.
Surfaces cover the pull request (GitHub/GitLab), the IDE (VS Code, Cursor, Windsurf since May 2025, and a JetBrains plugin announced in beta on November 9, 2026), and the terminal (CLI since September 16, 2025), August 2026 added Triage for prioritizing the PR queue, Change Stack for explaining massive diffs, and Security for post-merge monitoring, and the pricing page lists two on-demand products beside the plans, CodeRabbit Agent (coding tasks and automations assigned through Slack) and Deep Scan (a whole-codebase security scan at variable pricing).
Late October 2026 added two marketplace distributions: the Grok Build Plugin Marketplace via the SpaceX Super Intelligence Partner Network (October 22) and Cursor Origin's app marketplace as a launch partner (October 13).
November 2026 widened the platform again: a REST API with a hosted MCP server at mcp.coderabbit.ai (November 13), a configuration directory of Markdown review rules under `.coderabbit/` (November 13), Automatic Approvals with a minimum blocking severity (November 19), and CodeRabbit Verify (November 17, free during its beta), which starts the app in an isolated sandbox, exercises a pull request the way a user would, and posts the bugs it hits with reproduction steps, screenshots, and a session recording.
Reviews have scanned agent configuration since June 11, 2026: CodeRabbit runs Nvidia's SkillSpector on changed `SKILL.md`, `mcp.json`, `mcp-config.json`, `claude_desktop_config.json`, `.cursorrules`, and `codex.yaml` files to detect security risks in agent skills and MCP configuration, on by default and turned off with `reviews.tools.skillspector.enabled: false`.
The changelog then kept moving: Deep Scan Focus mode (November 20), Configuration V3 (November 21, an opt-in layout for review settings where custom pre-merge checks live as Markdown files under `.coderabbit/`, many keys move, and the built-in title and description checks turn off), Learnings as documentation PRs (November 23), and CLI v0.9.7 with `coderabbit verify` in the terminal (November 24).
It is proprietary SaaS from CodeRabbit, Inc., founded by Harjot Gill and Gur Singh, with self-hosting reserved for Enterprise and free reviews forever for public repositories.

## Status

**Very active, well-funded, and mid-pivot from reviewer to platform.**
Funding: $16M Series A led by CRV (August 13, 2024), then $60M Series B led by Scale Venture Partners with NVIDIA's NVentures (September 16, 2025, $550M valuation, $88M total raised), then $143M Series C at a $1.5B valuation co-led by Atomico and Smash Capital on August 12, 2026, with revenue up more than 5x year over year per that announcement.
Scale as of 2026-10-11: 17,000+ customers, 6M repositories, and more than 2M reviews per week, versus 2M repos installed and 13M cumulative PR reviews at the Series B a year earlier; the homepage claims moved to 20K customers and 8.5M repositories as of 2026-11-18 (still displayed 2026-11-24).

## Strengths

- **Distribution is real and compounding: 6M repositories under review and the top AI-assisted spot on GitHub Marketplace as of 2026-08-30.**
- One reviewer covers every surface code moves through (PR, IDE, CLI, agent handoffs), which is exactly what multi-agent teams need.
- The per-team Learnings loop and 40+ context sources target the false-positive noise that gets these tools turned off.
- Agent-skill security scanning is built in and on by default: SkillSpector runs sandboxed with LLM analysis disabled, a static pass that makes no LLM or network calls.
- Ranked #1 by online F1 in Martian's independent code review benchmark across nearly 300K PRs (vendor-reported, March 2026).
- The open source commitment is more than a free tier: $1.2M delivered on the first $1M pledge, and more than $10M committed on August 26, 2026.

## Cautions

- **In August 2025, Kudelski Security published an RCE exploit against CodeRabbit: a malicious .rubocop.yml in a PR executed attacker-controlled Ruby outside the sandbox on production servers, leaked API keys including the GitHub App private key, and could grant read and write access to 1M repositories including private ones.**
- The remediation is verified on both sides: Kudelski disclosed January 24, 2025, CodeRabbit disabled RuboCop within 1 hour, rotated credentials within 3, and shipped the sandboxing fix within 12, and Kudelski's writeup confirms the quick fix while noting other vendors it contacted never responded at all.
- The generalizable lesson: any PR-review SaaS holds write tokens across every repo you install it on, so one vendor bug is one bug across your whole portfolio.
- Critical market-share signal: Pullflow's analysis of 40.3M public PRs found GitHub Copilot overtook CodeRabbit as the top AI reviewer by PRs per month by November 2025, though CodeRabbit still led the cumulative 2025 count (632,256 vs 561,382 distinct PRs), and the metric measures participation, not review quality.
- Competitors position it as the verbose-but-cheaper option (Greptile's founder says switchers cite verbosity and concedes the price point), and the incident's "no customer data was accessed" claim is CodeRabbit's own, not independently verifiable.
- Metering creeps in at the edges: 5 PR reviews per developer per hour on Essentials (fair-use capped, 8 on Team and 10 on Advanced), and the Slack agent bills $0.40 per agent minute.
- Scope keeps widening, and the newest surfaces carry no posted price: Verify is free during its beta, Deep Scan bills by variable pricing, and the agent minute and the per-reviewed-file rates sit outside the per-seat plans.

## Pricing

**Per-seat pricing with a genuinely free open source tier, as of 2026-10-11.**
The plans were renamed in late August 2026: Essentials is the new name for Pro and Team the new name for Pro Plus, at the same prices, Essentials $24 per user per month and Team $48 (both billed annually, $30 and $60 monthly, 14-day free trial), with Enterprise adding SSO, RBAC, API access, EU SaaS, and self-hosting at custom pricing.
The standalone $40 Security plan is gone: a new Advanced tier ($72 annual, $90 monthly) folds in continuous security monitoring and per-PR security review, and full codebase security scans outside it use variable pricing.
The Slack agent remains usage-billed, at $0.40 per agent minute as of 2026-10-10 (down from $0.50 in early September), and usage-based reviews bill $0.25 per reviewed file beyond included limits.
Public repositories get reviews free forever, no setup required.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-08 | Essentials, Team | Plans renamed from Pro and Pro Plus at unchanged prices: Essentials $24/user/mo, Team $48 (annual; $30 and $60 monthly). | [coderabbit.ai/pricing](https://www.coderabbit.ai/pricing) |
| 2026-08 | Advanced | New Advanced tier ($72 annual, $90 monthly) replaced the standalone $40 Security plan. | [coderabbit.ai/pricing](https://www.coderabbit.ai/pricing) |
| 2026-09 | Slack agent | Usage price cut from $0.50 to $0.40 per agent minute. | [coderabbit.ai/pricing](https://www.coderabbit.ai/pricing) |

## Compared to

- [Greptile](../greptile/index.md): the review-only rival betting on learned rules and self-hosting in your own VPC; its founder concedes CodeRabbit is cheaper, Greptile's pitch is fewer and sharper comments.
- [OpenCodeReview](../open-code-review/index.md): Alibaba's Apache-2.0 CLI with bring-your-own model keys; choose it when code cannot leave your infrastructure, CodeRabbit when you want turnkey.
- GitHub Copilot code review: platform-native and, per Pullflow, now ahead on monthly PR volume; choose CodeRabbit for cross-repo context, learning loops, and GitLab coverage, Copilot if you are all-in on GitHub and want one fewer vendor.

## Bottom line

**Recommended for teams flooded with agent-generated PRs that want one reviewer covering PR, IDE, and CLI across GitHub and GitLab.**
Not for teams whose threat model rules out a third party holding write tokens across all their repositories, or that need self-hosting below the Enterprise tier.
My disagreeable take: the exploit history makes CodeRabbit more credible, not less, because surviving a public RCE with remediation measured in hours is better operational evidence than any benchmark win, and I would still rather pay this bill than pay the false-negative cost of a human-only queue at agent PR volumes.

## Changes

- 2026-08-30 - Created in the owner-requested Code review category seed, recording the funding ladder, the Kudelski exploit record, and the Pullflow market analysis.
- 2026-09-02 - Pricing restructured: Essentials and Team renames, plus a new Advanced tier replacing the $40 Security plan.
- 2026-09-04 - Slack agent price cut from $0.50 to $0.40 per agent minute.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-10-01 - Reworded banned-term words out of the prose; meaning unchanged.
- 2026-10-16 - Rotation re-verification: added the Engineer on-demand product (Slack-driven coding tasks and automations) to the surface inventory; every cited URL re-fetched live, all prices unchanged.
- 2026-10-24 - Rotation re-verification: every cited URL re-fetched live, all prices unchanged (Essentials $24, Team $48, Advanced $72 annual, $0.40 agent minute), homepage claims (17K customers, 6M repositories) still displayed; added the Grok Build Plugin Marketplace and Cursor Origin marketplace distributions from the vendor's October 21 to 22 posts.
- 2026-10-31 - Rotation re-verification: every cited URL re-fetched live; prices unchanged (Essentials $24, Team $48, Advanced $72 annual, $0.40 agent minute) and the homepage claims (17K customers, 6M repositories) still displayed; no factual drift.
- 2026-11-05 - Pointed the See-also matrix link at the Code Review Feature Matrix; its line described the category matrix this note joins but linked the evaluation-review one.
- 2026-11-11 - Rotation re-verification: every cited URL re-fetched live (the Pullflow report now resolves through a www redirect with the analysis intact); all prices unchanged (Essentials $24, Team $48, Advanced $72 annual, $0.40 agent minute, $0.25 per reviewed file) and the homepage claims (17K customers, 6M repositories) still displayed; no factual drift.
- 2026-11-18 - Rotation re-verification: every cited URL re-fetched live, all prices unchanged (Essentials $24, Team $48, Advanced $72 annual, $0.40 agent minute, $0.25 per reviewed file), and the homepage scale claims moved from 17K customers and 6M repositories to 20K and 8.5M; the funding, exploit, benchmark, and market-share facts all stood unchanged.
- 2026-11-24 - Rotation re-verification: every cited URL re-fetched live, all prices unchanged (Essentials $24, Team $48, Advanced $72 annual, $0.40 agent minute, $0.25 per reviewed file) and the homepage claims still 20K customers and 8.5M repositories; corrected the Cursor Origin post's date from October 21 to October 13, 2026, its published date on the live page, and the on-demand product naming, the pricing page listing CodeRabbit Agent and Deep Scan where the note said Engineer; recorded the November launches from the vendor changelog in What it is (the API and hosted MCP server, the configuration directory, Automatic Approvals with a minimum blocking severity, the JetBrains plugin beta, and CodeRabbit Verify) and added a scope caution.
- 2026-11-26 - Full re-verification on a cross-category handoff: every cited URL re-fetched live, all prices unchanged (Essentials $24, Team $48, Advanced $72 annual, $0.40 agent minute, $0.25 per reviewed file) and the homepage claims still 20K customers and 8.5M repositories; recorded SkillSpector (changelog entry of June 11, 2026: reviews run Nvidia's scanner on changed agent-skill and MCP configuration files by default, opt-out `reviews.tools.skillspector.enabled: false`, its tool guide at docs.coderabbit.ai/tools/skillspector fetched while www.coderabbit.ai/tools/skillspector answers 404) in What it is and Strengths, and the changelog entries of November 20 to 24 (Deep Scan Focus mode, Configuration V3, Learnings as documentation PRs, and `coderabbit verify` in CLI v0.9.7).

## See also

- [Greptile](../greptile/index.md) - the closest hosted rival and its learned-rules counter-bet
- [OpenCodeReview](../open-code-review/index.md) - the self-hosted, license-zero end of the same category
- [Code Review Feature Matrix](../code-review-feature-matrix/index.md) - the category matrix this note joins
- [Rethinking Code Review in the Age of LLMs](../../../rethinking-code-review-in-the-age-of-llms/index.md) - the corpus essay on what review means when agents write the code
- [You Cannot Out-Review a Machine by Hand](../../../you-cannot-out-review-a-machine-by-hand/index.md) - why the review queue needed automation in the first place

## References

- https://www.coderabbit.ai/ - product surface, 17K customers and 6M repositories as displayed 2026-10-31, re-fetched 2026-11-11 (unchanged), re-fetched 2026-11-18 (the scale claims moved to 20K customers and 8.5M repositories), re-fetched 2026-11-24 (both claims still displayed, Verify now the homepage's fifth pillar), re-fetched 2026-11-26 (both claims still displayed)
- https://www.coderabbit.ai/pricing - Essentials/Team/Advanced tiers and prices as of 2026-10-31 (re-fetched unchanged); the $0.40 Slack agent minute and the $0.25-per-reviewed-file usage rate still displayed on the 2026-11-11 re-fetch; re-fetched 2026-11-18 (prices, tiers, review-velocity caps, and usage rates all unchanged); re-fetched 2026-11-24 (all unchanged, the on-demand products listed as CodeRabbit Agent and CodeRabbit Deep Scan, the hourly review allowances reading 5, 8, 10, and 12 across Essentials, Team, Advanced, and Enterprise); re-fetched 2026-11-26 (prices and usage rates unchanged)
- https://www.coderabbit.ai/blog/introducing-agentic-change-management - Series C: $143M at a $1.5B valuation, August 12, 2026, 2M weekly reviews, 17K customers, 150K OSS projects, Triage/Change Stack/Security launch
- https://www.coderabbit.ai/blog/coderabbit-series-b-60-million-quality-gates-for-code-reviews - Series B: $60M led by Scale Venture Partners with NVentures, September 16, 2025, 2M repos, 13M PRs reviewed
- https://www.coderabbit.ai/blog/coderabbit-announces-16m-series-a-funding-led-by-crv - Series A: $16M led by CRV, August 13, 2024
- https://www.coderabbit.ai/blog/coderabbit-cli-free-ai-code-reviews-in-your-cli - CLI launch, September 16, 2025
- https://www.coderabbit.ai/blog/coderabbit-expands-its-commitment-to-open-source - the $10M+ open source commitment, August 26, 2026
- https://www.coderabbit.ai/blog/our-response-to-the-january-2025-kudelski-security-vulnerability-disclosure-action-and-continuous-improvement - the vendor's remediation timeline for the exploit
- https://kudelskisecurity.com/research/how-we-exploited-coderabbit-from-a-simple-pr-to-rce-and-write-access-on-1m-repositories - the Kudelski Security writeup, August 19, 2025
- https://pullflow.com/state-of-ai-code-review-2025 - the critical 40.3M-PR market-share analysis, re-fetched 2026-11-11 (now served from the www host by a redirect, the analysis itself unchanged) and 2026-11-24 (unchanged)
- https://hn.algolia.com/api/v1/items/44953032 - the exploit thread on Hacker News: 687 points, 227 comments, posted August 19, 2025, re-fetched 2026-10-31, 2026-11-11, and 2026-11-24 (unchanged)
- https://hn.algolia.com/api/v1/items/42451968 - the Greptile thread where its founder positions CodeRabbit as verbose but cheaper, re-fetched 2026-10-31, 2026-11-11, and 2026-11-24
- https://www.coderabbit.ai/blog/coderabbit-spacex-super-intelligence-partner-network - the Grok Build Plugin Marketplace listing via the SpaceX Super Intelligence Partner Network, October 22, 2026, fetched 2026-10-24, re-fetched 2026-11-24
- https://www.coderabbit.ai/blog/coderabbit-independent-validation-cursor-origin - the Cursor Origin app-marketplace launch-partner post, October 13, 2026 (the note recorded October 21 until the 2026-11-24 re-fetch read the page's published date), fetched 2026-10-24 and re-fetched 2026-11-24
- https://docs.coderabbit.ai/changelog - the vendor changelog (coderabbit.ai/changelog redirects there): the JetBrains IDE beta and risk instructions (November 9, 2026), review threads and Triage priority in the API (November 10), the configuration directory, the CodeRabbit API and hosted MCP server, and Triage for open-source organizations (November 13), CodeRabbit Verify (November 17), and Agent Skills as review guidelines plus the minimum blocking severity for Automatic Approvals (November 19), fetched 2026-11-24, re-fetched 2026-11-26 (the SkillSpector entry of June 11, 2026, and entries through CLI v0.9.7, November 24)
- https://docs.coderabbit.ai/tools/skillspector - the SkillSpector tool guide: the six file names it runs on, on by default, the `reviews.tools.skillspector.enabled` key and the Reviews → Tools toggle, sandboxed static analysis with LLM analysis disabled, fetched 2026-11-26
