---
title: "Code Review Feature Matrix"
created: 2026-08-30
updated: 2026-10-08
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, code-review, ai-review, developer-tools]
readability: 3
audience_notes: >
  Engineers shortlisting an AI code reviewer for their repositories who need the capability deltas at a glance.
  Assumes you know what a GitHub check, a learned-rules loop, and BYOK mean; each column links to a full note with sources.
---

This matrix compares the nine AI code-review tools profiled in this section, feature by feature, so the shortlisting step does not require reading nine notes.

**The deciding row is still where your code runs, not review quality: public quality benchmarks only arrived this month (GitHub's ReviewBench on October 5 and Kodus's vendor-run CodeReviewBench), while five columns are vendor clouds, one runs in your VPC, three run entirely on your infrastructure with your keys, Graphite Diamond arrives already consolidated as a Cursor property, and the category's most-repeated outside fact is that the two biggest commercial reviewers both have Kudelski-disclosed exploit histories.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [CodeRabbit](../coderabbit/index.md) | [Ellipsis](../ellipsis/index.md) | [Graphite Diamond](../graphite-diamond/index.md) | [Greptile](../greptile/index.md) | [Kodus](../kodus/index.md) | [OpenCodeReview](../open-code-review/index.md) | [Qodo](../qodo/index.md) | [roborev](../roborev/index.md) | [Sourcery](../sourcery/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | commercial review service expanding into change management | agent cloud, review demoted to a use case | AI review inside the Graphite stacked-PR platform, now Cursor-owned | hosted reviewer over a whole-repo graph index | open-source BYOK reviewer (Kody) with a paid cloud | self-hosted hybrid rules-plus-LLM reviewer | open-core reviewer, MIT PR-Agent plus paid Qodo Merge | open-source commit-review daemon from Kenn Software (Wes McKinney), PR panels added | hosted reviewer from a static-analysis lineage, proprietary app over an MIT repo |
| Object judged | pull requests (diff plus learned repo context) | pull requests, as one configurable agent use case | pull requests in the stacked-PR workflow | pull requests against the full codebase graph | pull requests on GitHub, GitLab, Bitbucket, and Azure Repos | git diffs and pull requests in CI | pull requests via /review and /improve commands | every commit through a post-commit hook, plus GitHub/GitLab PRs via a CI poller | pull requests on GitHub and GitLab, plus a security-scan layer |
| Judge | LLM reviewers with team-learned rules | your chosen coding agent under its agents-as-code config | Graphite Agent (ex-Diamond) with custom rules | review agent swarm reading the team's comment history | your BYOK model with plain-language custom rules | deterministic rules first, LLM agent second, precision-first | LLM with configurable best-practices files, a specialized-agent swarm in Qodo 3.0 (2026-10) | your own installed coding agents, eleven named, synthesized into one review per PR by subagent panels | LLM reviewers on OpenAI and Anthropic models |
| Deployment | GitHub/GitLab app, IDE, CLI, Enterprise self-host | cloud with BYOC into your AWS VPC, REST API with public Python and TypeScript SDK mirrors | graphite.com SaaS, GitHub-centric, GHES support on Enterprise | cloud, self-host in your own AWS or air-gapped VPC | self-hosted, Kodus Cloud, or CLI, on your own model keys | self-hosted CLI, CI, agent plugins, MCP, your model keys | self-host PR-Agent, buy Qodo cloud, or install the Agentic Toolbox skills inside Claude Code, Codex, and Kiro | local daemon with TUI and browser UI, gh-action generator, PostgreSQL sync, ACP adapters | GitHub/GitLab app and IDE plugins, Enterprise self-host |
| CI gating | ✓ | ~ through its cloud runs | ? | ✓ | ✓ CLI in CI/CD | ✓ GitHub Action and GitLab CI | ✓ via CI recipes | ✓ gh-action generator and the daemon CI poller | ? |
| Fixes or rewrites code | ~ Triage and Change Stack agents (2026 expansion) | ~ the agents it hosts fix what review finds | ~ one-click fixes | ~ handoff to Claude Code, Cursor, Codex, Devin, TREX tests beta | ✗ comments only | ✗ comments only | ~ /improve suggestions | ✓ roborev fix and the /roborev-refine loop | ~ agent-assisted fix path |
| Learns team rules | ✓ learnings | ~ agents-as-code config you write | ~ custom rules | ✓ from review comments, isolated per organization | ✓ plain-language rules, workflow learning | ✗ fixed rule pipeline | ~ best-practices files you curate | ~ guidelines you write per repo (REVIEW.md fallback), nothing learned from comments | ? |
| License | ✗ proprietary, free forever for public repos | ✗ closed core, small OSS tooling repos | ✗ proprietary, Cursor-owned | ✗ proprietary | ~ AGPL-3.0 core, ee/ paths commercial | ✓ Apache-2.0 | ~ PR-Agent MIT, Qodo Merge proprietary | ✓ MIT | ✗ reviewer proprietary, the MIT repo is the refactoring lineage |
| Pricing anchor | Essentials (ex-Pro) $24, Team (ex-Pro Plus) $48 per user/mo annual, new Advanced $72 annual ($90 monthly) with variable-priced full scans, public repos free | tokens at cost plus a 10% fee, free for individuals on a Claude Code or Codex subscription, support packages from $5k/mo | Hobby free, Starter $20, Team $40 per user/mo | $30/seat plus credits, $1 per extra credit | Community free, Teams BYOK $10/dev/mo plus raw tokens, Enterprise custom with SOC 2, self-host free | free, your model tokens | $0.012 per credit packs, Pro Team $30, no permanent free tier | free, your own agents' tokens | Pro $12, Team $24 per user/mo, open source repos free |
| Maturity and scale | $143M Series C at a $1.5B valuation, 17k customers (2026-08) | pivoted 2026-07, $2M seed (2024) | ~$81M raised, $290M valuation, acquired by Cursor 2025-12 | $25M Series A (2025-09), v5 | 1,455 stars, no verified funding (2026-10-08) | 44.4k stars, 136 releases in 5 months (2026-10-08) | 13,303 stars (2026-10-08), $50M raised | 1,747 stars, 120 releases in nine months (2026-10-08) | repo since 2019, 1,872 stars, no verified funding (2026-10-08) |

## Reading the matrix

**Platform-native review is the threat the columns do not price in: Copilot's built-in reviewer overtook CodeRabbit on monthly PR volume by November 2025 per Pullflow's 40.3M-PR analysis, and every vendor here is selling against a checkbox your forge already ships.**
CodeRabbit still led cumulative 2025 volume, 632,256 to 561,382 distinct PRs, so the overtake is a rate, not a fait accompli, but it is the category's only independent market-share number.

**A reviewer holds privileged access, and the category's record proves it.**
Kudelski Security turned a malicious RuboCop config into RCE and write access on one million CodeRabbit-connected repositories in January 2025, and found a PR-comment-to-AWS-admin-key chain in Qodo Merge Pro the same year, both fixed after disclosure.
The caution is structural: whatever judges your code can execute in your CI context, so treat every column here as a privileged integration, not a linter.

**Quality measurement arrived in October 2026, from interested parties.**
GitHub launched ReviewBench on October 5, an open benchmark of 219 public PRs across 19 languages with a public leaderboard, self-serve submissions, and a published judge, built and run by the platform that sells Copilot code review, and Kodus's CodeReviewBench scores models on Kodus's own harness with best recall under 45 percent.
Neither is independent of the vendor publishing it, so the row-level advice stands: ask where the benchmark's conflicts sit before trusting its ranking.

**Independent academic research landed the same week as the benchmarks.**
A JetBrains Research and Lund University study presented at ESEIW 2026 (participatory design with 17 practitioners, then a 43-developer validation survey) concludes that reviewing LLM-generated multi-file changes is a trust-calibration problem rather than a diffing problem, because LLMs present every line with uniform confidence no matter how uncertain each line was.
Its October 6, 2026 write-up names only partial counterparts among shipping tools (CodeRabbit's prose walkthroughs, Claude Code's severity-tagged reviewer agents, Graphite's stacked PRs) and states that no current tool imposes the overview-before-files-before-lines risk stratification its framework proposes.
If that framing holds, the deciding row eventually moves from where your code runs to which column surfaces risk where it matters.

**The license row is the cost row in disguise.**
The four open paths, Apache-2.0, roborev's MIT, MIT PR-Agent, and Kodus's AGPL-3.0, trade turnkey convenience for wiring and model-token spend, and Kodus's badge is the narrowest of the four, since everything under its ee/ paths is commercially licensed.
Qodo's own README draws the line bluntly: the donated PR-Agent repo is a community-maintained legacy project, not the commercial free tier.
Greptile's self-hosting runs in your cloud but stays proprietary, so the VPC row buys data residency, not code ownership, and Sourcery's MIT badge covers the 2019 refactoring repo, not the reviewer.

**Review-alone is a hard business, and Ellipsis is the exit record.**
It launched as a 121-point Show HN review bot in 2024 and pivoted to managed agent infrastructure in July 2026, keeping review only as a configurable use case.
Its pricing now leads with a free on-ramp for individuals who bring their own Claude Code or Codex subscription, though the platform fee on tokens briefly rose to 20% in early October 2026 before reverting to 10%.

## Choosing from the matrix

- Turnkey cross-repo review with learned rules and a GitLab story: CodeRabbit, free on public repos, per-seat on private ones.
- Code that must never touch a vendor cloud: OpenCodeReview, Apache-2.0 with your own keys, Kodus, AGPL-3.0 with your own keys and a flat platform fee, MIT PR-Agent if you accept its community-maintenance status, or roborev if review should sit on every commit inside the loop rather than on the PR.
- Whole-repo graph context and house-rule enforcement without building it: Greptile, self-hosted in your own VPC.
- Already running Graphite's stacked-PR workflow: Graphite Agent adds review without adding a vendor, now with Cursor behind it.
- Free review for open-source repos or the cheapest paid seat: Sourcery, $12 with security scans bolted on.
- Already running many coding agents and want managed infrastructure with transcripts and budget caps: Ellipsis Agent Cloud, review included as a use case.
- GitHub-all-in and price-sensitive: Copilot's platform-native reviewer, covered inside the VS Code note, now leads monthly volume; measure whether its depth beats the dedicated columns before paying for one.

## Changes

- 2026-08-30 - Created in the Code review category seed with five columns and the where-your-code-runs thesis.
- 2026-09-13 - Added the Ellipsis free-for-individuals on-ramp (own ChatGPT or Claude subscription) to its pricing cell.
- 2026-09-13 - Added the Qodo Agentic Toolbox (September 9 launch, review and rules skills inside Claude Code, Codex, and Kiro) to its deployment cell.
- 2026-09-16 - Re-verified all cells against live sources; refreshed the Kodus, OpenCodeReview, and Sourcery maturity cells after their repo numbers moved.
- 2026-09-18 - Re-verified all cells; refreshed the Kodus and OpenCodeReview maturity cells and updated the Ellipsis free-individual subscription wording.
- 2026-09-20 - Refreshed the OpenCodeReview maturity cell to 37.9k stars and 131 releases and the Qodo cell to 13,054 stars; Kodus held at 1,397 stars.
- 2026-09-21 - Refreshed the Kodus (1,409), OpenCodeReview (38.7k), Qodo (13,089), and Sourcery (1,869) maturity cells; all other cells re-verified unchanged.
- 2026-09-24 - Removed the verification preamble line on owner request.
- 2026-09-24 - Refreshed the Kodus (1,416), OpenCodeReview (40.8k stars, 133 releases), and Qodo (13,142) maturity cells; all other cells re-verified unchanged.
- 2026-09-27 - Refreshed the OpenCodeReview maturity cell to 41.7k stars; all other cells re-verified unchanged.
- 2026-09-29 - Refreshed the OpenCodeReview maturity cell to 42.4k stars and 134 releases; all other cells re-verified unchanged.
- 2026-10-02 - Ellipsis's platform fee doubled to 20% of token cost (pricing cell and the Ellipsis paragraph updated); refreshed the Kodus, OpenCodeReview, and Qodo maturity cells to their 2026-10-02 repo numbers.
- 2026-10-03 - Ellipsis's platform fee reverted to 10% of token cost (pricing cell and the Ellipsis paragraph updated); refreshed the Kodus (1,442), OpenCodeReview (43.4k), and Qodo (13,246) maturity cells to their 2026-10-03 repo numbers.
- 2026-10-06 - Refreshed the Kodus (1,449), OpenCodeReview (43.9k stars, 136 releases), Qodo (13,274), and Sourcery (1,870) maturity cells to their 2026-10-06 repo numbers; all other cells re-verified unchanged, with every pricing page re-fetched.
- 2026-10-06 - Added the roborev column (eight to nine members), with the Qodo maturity cell refreshed to 13,276 stars the same day; all cells re-verified against live sources fetched this run.
- 2026-10-07 - Qualified the review-quality claim in the thesis and added a Reading-the-matrix paragraph: GitHub's ReviewBench (open 219-PR benchmark with a leaderboard, October 5) and Kodus's vendor-run CodeReviewBench now exist, both from interested parties; the Qodo judge cell records the Qodo 3.0 swarm.
- 2026-10-07 - Refreshed the Kodus (1,452), OpenCodeReview (44.1k stars), Qodo (13,291), roborev (1,746), and Sourcery (1,872) maturity cells to their 2026-10-07 repo numbers; all other cells re-verified unchanged, with every pricing page re-fetched.
- 2026-10-08 - Added a Reading-the-matrix paragraph on the JetBrains Research and Lund University trust-calibration study (ESEIW 2026): reviewing AI-generated multi-file changes is a trust-calibration problem no current tool addresses, with the paper and the announcement post added to References.
- 2026-10-08 - Refreshed the Kodus (1,455), OpenCodeReview (44.4k), Qodo (13,303), and roborev (1,747) maturity cells to their 2026-10-08 repo numbers; Sourcery held at 1,872 and all other cells re-verified unchanged.

## See also

- [Evaluation and Review Feature Matrix](../../evaluation-review/evaluation-review-feature-matrix/index.md) - the neighboring quality-control category, evals and observability rather than PR review
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - where review sits in the four-layer map
- [Plannotator](../../evaluation-review/plannotator/index.md) - the human-annotation counterpart to machine review
- [Rethinking Code Review in the Age of LLMs](../../../rethinking-code-review-in-the-age-of-llms/index.md) - the corpus essay this category answers
- [Code Review Without Reading the Code](../../../code-review-without-reading-the-code/index.md) - the corpus case for machine-scale review

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
- https://github.blog/ai-and-ml/github-copilot/reviewbench-an-open-benchmark-for-ai-code-review/ - the ReviewBench announcement grounding the quality-measurement paragraph
- https://codereviewbench.com/ - Kodus's vendor-run model benchmark, the second half of that paragraph
- https://blog.jetbrains.com/research/2026/10/review-ai-generated - the October 6, 2026 JetBrains Research post presenting the trust-calibration framework and its survey of current tools, fetched 2026-10-08
- https://arxiv.org/abs/2606.01969 - the ESEM SEIP 2026 paper behind it: N=17 participatory design, N=43 validation survey, the three-level workflow and seven design constructs, fetched 2026-10-08
