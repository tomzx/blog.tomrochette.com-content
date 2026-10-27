---
title: "Code Review Feature Matrix"
created: 2026-08-30
updated: 2026-10-27
status: finished
tags: [agent-curated, fully-ai-generated, llm=glm-5.3-flash, comparison, code-review, ai-review, developer-tools]
readability: 3
audience_notes: >
  Engineers shortlisting an AI code reviewer for their repositories who need the capability deltas at a glance.
  Assumes you know what a GitHub check, a learned-rules loop, and BYOK mean; each column links to a full note with sources.
---

This matrix compares the fourteen AI code-review tools profiled in this section, feature by feature, so the shortlisting step does not require reading thirteen notes.

**The deciding row is still where your code runs, not review quality: public quality benchmarks are new to 2026 and every one is run by an interested party (Qodo's own PR-Review-Bench in February, GitHub's ReviewBench on October 5, Kodus's CodeReviewBench, Agent Skills Hub's third-party eval on October 10), while five columns are vendor clouds, one is a local hook whose reviews still ride a vendor cloud (git-lrc), one runs in your VPC, five run on your machine or your own CI with your own keys or agent logins (Gito, the stateless pip install, joins this group), one is a dormant unlicensed Vercel Labs beta you deploy yourself (OpenReview), Graphite Diamond arrives already consolidated as a Cursor property, and the category's most-repeated outside fact is that the two biggest commercial reviewers both have Kudelski-disclosed exploit histories.**

Legend: ✓ supported, ✗ not supported, ~ partial or conditional, ? not verified.
Each column links to the full research note; every cell traces to a source cited there or in the references.

## The matrix

| Feature | [CodeRabbit](../coderabbit/index.md) | [Ellipsis](../ellipsis/index.md) | [git-lrc](../git-lrc/index.md) | [Gito](../gito/index.md) | [Graphite Diamond](../graphite-diamond/index.md) | [Greptile](../greptile/index.md) | [Kodus](../kodus/index.md) | [multi](../multi/index.md) | [OpenCodeReview](../open-code-review/index.md) | [OpenQodex](../openqodex/index.md) | [OpenReview](../openreview/index.md) | [Qodo](../qodo/index.md) | [roborev](../roborev/index.md) | [Sourcery](../sourcery/index.md) |
| --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
| Kind | commercial review service expanding into change management | agent cloud, review demoted to a use case | commit-time micro-review CLI from Hexmos, fronting the LiveReview cloud | solo MIT Python PR reviewer (pip gito.bot), GitHub Action plus CLI | AI review inside the Graphite stacked-PR platform, now Cursor-owned | hosted reviewer over a whole-repo graph index | open-source BYOK reviewer (Kody) with a paid cloud | solo multi-model consensus review plugin and CLI (Shell plus Python) | self-hosted hybrid rules-plus-LLM reviewer | open-source pre-push review CLI from Qodex.ai, the funnel for its hosted Qodex product | Vercel Labs beta demo, a self-hosted @mention review bot, dormant since March 2026 | open-core reviewer, MIT PR-Agent plus paid Qodo Merge | open-source commit-review daemon from Kenn Software (Wes McKinney), PR panels added | hosted reviewer from a static-analysis lineage, proprietary app over an MIT repo |
| Object judged | pull requests (diff plus learned repo context) | pull requests, as one configurable agent use case | the staged diff at every commit, with review status written into the git log | pull requests (GitHub Action) and local branch diffs against the default branch, unstaged files ignored | pull requests in the stacked-PR workflow | pull requests against the full codebase graph | pull requests on GitHub, GitLab, Bitbucket, Azure Repos, and Forgejo/Gitea | the target you name (a diff, a branch, files, a function, or a whole repo) from a frozen snapshot | git diffs and pull requests in CI | your unpushed change (unpushed commits plus uncommitted edits), plus branches and PRs on demand | GitHub pull requests, on an @openreview mention | pull requests via /review and /improve commands | every commit through a post-commit hook, plus GitHub/GitLab PRs via a CI poller | pull requests on GitHub and GitLab, plus a security-scan layer |
| Judge | LLM reviewers with team-learned rules | your chosen coding agent under its agents-as-code config | LLM review through the LiveReview pipeline (Gemini default, BYOK connectors), plus a local blast-radius scorer | your configured LLM provider (OpenAI-compatible, Anthropic, Google, local servers, or coding-agent CLIs like Claude Code and Gemini CLI) | Graphite Agent (ex-Diamond) with custom rules | review agent swarm reading the team's comment history | your BYOK model with plain-language custom rules | several model backends in parallel (Claude sub-agents, Codex, OpenCode, Kilo, Gemini, Copilot, headless Claude-compatible endpoints), findings merged into corroborated, single-source, disagreed, and dropped buckets | deterministic rules first, LLM agent second, precision-first | pinned scanners first (22 built-in), then a separate Claude Code or Codex process on a frozen copy, with scripted completeness checks | Claude inside a Vercel Sandbox microVM with full repo access (linters, formatters, tests) | LLM with configurable best-practices files, a specialized-agent swarm in Qodo 3.0 (2026-10) | your own installed coding agents, eleven named, synthesized into one review per PR by subagent panels | LLM reviewers on OpenAI and Anthropic models |
| Deployment | GitHub/GitLab app, IDE, CLI, Enterprise self-host | cloud with BYOC into your AWS VPC, REST API with public Python and TypeScript SDK mirrors | local global git hook and browser UI, LiveReview cloud coordination, Enterprise self-hosting | pip install plus a ready-made GitHub Action workflow, GitLab CI (beta), local CLI, per-repo TOML config | graphite.com SaaS, GitHub-centric, GHES support on Enterprise | cloud, self-host in your own AWS or air-gapped VPC | self-hosted, Kodus Cloud, or CLI, on your own model keys | local CLI plus Claude Code/Codex plugin install, TOML profiles, your own model subscriptions | self-hosted CLI, CI, agent plugins, MCP, an ACP service (2026-10), your model keys | local CLI and agent skill (Claude Code, Codex, Cursor, Cline), GitHub Action (full review with an Anthropic key, scanners only without), MCP code-graph server | one-click self-deploy on Vercel with Upstash KV, your GitHub App and Anthropic key | self-host PR-Agent, buy Qodo cloud, or install the Agentic Toolbox skills inside Claude Code, Codex, and Kiro | local daemon with TUI and browser UI, gh-action generator, PostgreSQL sync, ACP adapters | GitHub/GitLab app and IDE plugins, Enterprise self-host |
| CI gating | ✓ | ~ through its cloud runs | ~ through LiveReview dashboard CI/CD gates (jq rulesets) | ✓ GitHub Action workflow, GitLab in beta | ? | ✓ | ✓ CLI in CI/CD | ✗ no forge or CI integration, you run it | ✓ GitHub Action and GitLab CI | ~ GitHub Action, full review only with an Anthropic key | ~ reviews on mention, no check gate | ✓ via CI recipes | ✓ gh-action generator and the daemon CI poller | ? |
| Fixes or rewrites code | ~ Triage and Change Stack agents (2026 expansion) | ~ the agents it hosts fix what review finds | ✗ findings plus a copy-to-agent loop | ✗ comments only | ~ one-click fixes | ~ handoff to Claude Code, Cursor, Codex, Devin, TREX tests beta | ✗ comments only | ~ only the opt-in loop mode edits (fix, re-review, up to three rounds) | ✗ comments only | ~ hands findings to your agent to fix, editing nothing itself | ~ one-click suggestion blocks, plus direct commits for formatting, lint, and simple bugs | ~ /improve suggestions | ✓ roborev fix and the /roborev-refine loop | ~ agent-assisted fix path |
| Learns team rules | ✓ learnings | ~ agents-as-code config you write | ~ .lrc/rules markdown you write plus thumbs-up/down tuning; nothing learned from comments | ~ per-repo prompts and templates you write in TOML, nothing learned | ~ custom rules | ✓ from review comments, isolated per organization | ✓ plain-language rules, workflow learning | ✗ deliberately stateless between runs | ✗ fixed rule pipeline | ~ a committed instructions file you write tells the reviewer what never to flag | ✗ | ~ best-practices files you curate | ~ guidelines you write per repo (REVIEW.md fallback), nothing learned from comments | ? |
| License | ✗ proprietary, free forever for public repos | ✗ closed core, small OSS tooling repos | ✗ source-available under a modified Sustainable Use License, no resale or commercial redistribution | ✓ MIT | ✗ proprietary, Cursor-owned | ✗ proprietary | ~ AGPL-3.0 core, ee/ paths commercial | ✓ MIT | ✓ Apache-2.0 | ✓ Apache-2.0 | ~ README declares MIT, but no license file exists to back it | ~ PR-Agent MIT, Qodo Merge proprietary | ✓ MIT | ✗ reviewer proprietary, the MIT repo is the refactoring lineage |
| Pricing anchor | Essentials (ex-Pro) $24, Team (ex-Pro Plus) $48 per user/mo annual, new Advanced $72 annual ($90 monthly) with variable-priced full scans, public repos free | tokens at cost plus a 10% fee, support packages from $5k/mo (the free-for-individuals on-ramp left the site 2026-10-25) | free 30k LOC/mo with BYOK, Premium from $32/mo per 100k LOC in fixed doubling bands, unlimited users | free, your model tokens (or a local model) | Hobby free, Starter $20, Team $40 per user/mo | $1 per credit, no seat fees, credits shared across the org (2026-10-24) | Community free, Teams BYOK $10/dev/mo plus raw tokens, Enterprise custom with SOC 2, self-host free | free, your model subscriptions (about $3.50 of Claude usage per review per the author's table) | free, your model tokens | free, riding your Claude Code or Codex plan; hosted Qodex sibling paid per developer (price unpublished) | free; your Vercel Sandbox active-CPU bill and Anthropic usage | $0.012 per credit packs, Pro Team $30, no permanent free tier | free, your own agents' tokens | Pro $12, Team $24 per user/mo, open source repos free |
| Maturity and scale | $143M Series C at a $1.5B valuation, 17k customers (2026-08) | pivoted 2026-07, $2M seed (2024) | 1,470 stars, 55 releases in eight months (2026-10-23) | 452 stars, 40 PyPI releases in 17 months (2026-10-24) | ~$81M raised, $290M valuation, acquired by Cursor 2025-12 | $50M Series B led by Menlo at a $750M valuation (2026-10-19), $79M total, v5 | 1,461 stars, no verified funding (2026-10-11) | 23 stars, 24 tagged releases in three months (2026-10-16) | 46.9k stars, 140-plus releases in 5 months (stars 2026-10-13, v1.13.3 2026-10-22) | 653 stars, 7,739 npm downloads in the trailing month (2026-10-26) | dormant since 2026-03-06, 1,696 stars, zero releases (2026-10-11) | 13,339 stars (2026-10-11), $50M raised | 1,749 stars, 123-plus releases in nine months (2026-10-27) | repo since 2019, 1,875 stars, no verified funding (2026-10-11) |

## Reading the matrix

**Platform-native review is the threat the columns do not price in: Copilot's built-in reviewer overtook CodeRabbit on monthly PR volume by November 2025 per Pullflow's 40.3M-PR analysis, and every vendor here is selling against a checkbox your forge already ships.**
CodeRabbit still led cumulative 2025 volume, 632,256 to 561,382 distinct PRs, so the overtake is a rate, not a fait accompli, but it is the category's only independent market-share number.

**A reviewer holds privileged access, and the category's record proves it.**
Kudelski Security turned a malicious RuboCop config into RCE and write access on one million CodeRabbit-connected repositories in January 2025, and found a PR-comment-to-AWS-admin-key chain in Qodo Merge Pro the same year, both fixed after disclosure.
The caution is structural: whatever judges your code can execute in your CI context, so treat every column here as a privileged integration, not a linter.

**Quality measurement arrived in 2026, and every benchmark is run by an interested party.**
Qodo published the first vendor-run one in February (PR-Review-Bench: 580 injected issues across 100 merged PRs, seven rival tools compared, Qodo first at 60.1 percent F1, dataset public).
GitHub launched ReviewBench on October 5, an open benchmark of 219 public PRs across 19 languages with a public leaderboard, self-serve submissions, and a published judge, built and run by the platform that sells Copilot code review, and Kodus runs two surfaces: CodeReviewBench, which scores models on Kodus's own harness with best recall under 45 percent, and a tools benchmark where Kody beats CodeRabbit, GitHub Copilot, and Cursor on every severity band.
A fourth arrived on October 10 from outside the reviewed tools' vendor row entirely: Agent Skills Hub, a skill-discovery site, ran sixteen of these instruments end to end on twelve small PRs with eight planted defects and found that none beat its bare Claude Code control, which matched the top score of 8 of 8 alongside four review skills, roborev, and spencermarx's open-code-review, while git-lrc could not run at all because its reviews ride a vendor server.
None is independent of the party publishing it, and the tools benchmark's own methodology text disagrees with its results (nine selected PRs in one paragraph, 38 analyzed in the tables), so the row-level advice stands: ask where the benchmark's conflicts sit before trusting its ranking.

**Independent academic research landed the same week as the benchmarks.**
A JetBrains Research and Lund University study presented at ESEIW 2026 (participatory design with 17 practitioners, then a 43-developer validation survey) concludes that reviewing LLM-generated multi-file changes is a trust-calibration problem rather than a diffing problem, because LLMs present every line with uniform confidence no matter how uncertain each line was.
Its October 6, 2026 write-up names only partial counterparts among shipping tools (CodeRabbit's prose walkthroughs, Claude Code's severity-tagged reviewer agents, Graphite's stacked PRs) and states that no current tool imposes the overview-before-files-before-lines risk stratification its framework proposes.
If that framing holds, the deciding row eventually moves from where your code runs to which column surfaces risk where it matters.

**The license row is the cost row in disguise.**
The five open paths, OpenCodeReview's and OpenQodex's Apache-2.0, roborev's MIT, MIT PR-Agent, and Kodus's AGPL-3.0, trade turnkey convenience for wiring and model-token spend, and Kodus's badge is the narrowest of the five, since everything under its ee/ paths is commercially licensed.
Qodo's own README draws the line bluntly: the donated PR-Agent repo is a community-maintained legacy project, not the commercial free tier.
Greptile's self-hosting runs in your cloud but stays proprietary, so the VPC row buys data residency, not code ownership, Sourcery's MIT badge covers the 2019 refactoring repo, not the reviewer, and OpenReview's README declares MIT in one bare line with no license file behind it, so the grant is a claim, not a license.

**Review-alone is a hard business, and Ellipsis is the exit record.**
It launched as a 121-point Show HN review bot in 2024 and pivoted to managed agent infrastructure in July 2026, keeping review only as a configurable use case.
Its pricing is usage-based with a 10% platform fee on tokens, which briefly rose to 20% in early October 2026 before reverting, and the free-for-individuals on-ramp that pricing launched with left the site by October 25, 2026.

## Choosing from the matrix

- Turnkey cross-repo review with learned rules and a GitLab story: CodeRabbit, free on public repos, per-seat on private ones.
- Code that must never touch a vendor cloud: OpenCodeReview, Apache-2.0 with your own keys, Kodus, AGPL-3.0 with your own keys and a flat platform fee, MIT PR-Agent if you accept its community-maintenance status, or roborev if review should sit on every commit inside the loop rather than on the PR.
- Review before the push, on the agent subscription you already pay for: OpenQodex, Apache-2.0, scanners plus a separate reviewer process with a completeness contract.
- A one-file GitHub Action reviewer with any provider, including local models and coding-agent CLIs: Gito, MIT and stateless, GitHub-only today.
- A commit gate that records review attestations in the git log itself: git-lrc, free for individuals, with the caveat that its reviews ride Hexmos's cloud unless you pay for Enterprise self-hosting.
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
- 2026-10-09 - Refreshed the Kodus (1,458), OpenCodeReview (44.7k stars, 137 releases), Qodo (13,317), roborev (1,748), and Sourcery (1,873) maturity cells to their 2026-10-09 repo numbers; all other cells re-verified unchanged, with every pricing page re-fetched.
- 2026-10-10 - Added the git-lrc column (nine to ten members, inserted in its case-insensitive sorted position), with the Kodus (1,459), OpenCodeReview (45.6k stars), Qodo (13,326), roborev (1,748), and Sourcery (1,874) maturity cells refreshed to their 2026-10-10 repo numbers; all other cells re-verified unchanged, with every pricing page re-fetched.
- 2026-10-11 - Added the OpenQodex and OpenReview columns (ten to twelve members, inserted in their case-insensitive sorted positions), and qualified the benchmark story: Qodo's own public PR-Review-Bench (February 4, 2026, 100 PRs, 580 injected issues) predates the October benchmarks, so the thesis and the quality paragraph now name all three vendor-run surfaces, Kodus's included tools benchmark noted with its self-contradictory methodology.
- 2026-10-11 - Refreshed the git-lrc (1,470), Kodus (1,461), OpenCodeReview (46.0k stars), Qodo (13,339), roborev (1,749), and Sourcery (1,875) maturity cells to their 2026-10-11 repo numbers; all other cells re-verified unchanged, with every pricing page re-fetched.
- 2026-10-13 - Recorded OpenCodeReview's v1.13.0 (ChatGPT-plan reviews through the public Responses API, a new ACP service) in its deployment and maturity cells, and refreshed the OpenQodex maturity cell to 653 stars and 4,533 weekly npm downloads; all other cells re-verified unchanged, with every pricing page re-fetched.
- 2026-10-16 - Added the multi column (twelve to thirteen members, inserted in its case-insensitive sorted position after Kodus); all existing cells re-verified unchanged this run.
- 2026-10-18 - Added Agent Skills Hub's third-party end-to-end eval (October 10: sixteen tools, none beating the bare-agent control, git-lrc unrunnable) to the quality-measurement story, and broadened the thesis's vendor-run wording to run-by-an-interested-party; no cell values changed.
- 2026-10-20 - Corrected the OpenReview license cell and the license paragraph (its README declares MIT in one bare line with no license file behind it), widened the Kodus object row to Forgejo/Gitea per its docs and homepage FAQ, and recorded OpenCodeReview's v1.13.2 in its maturity cell.
- 2026-10-22 - Recorded OpenCodeReview's v1.13.3 in its maturity cell and refreshed OpenQodex's weekly npm downloads to 1,918 (week of October 12 to 18); star figures untouched per the standing exemption; all other cells re-verified unchanged.
- 2026-10-24 - Added the Gito column (thirteen to fourteen members, inserted in its case-insensitive sorted position after git-lrc); refreshed the Greptile pricing cell (Pro restructured to $1 per credit with no seat fees) and maturity cell ($50M Series B at a $750M valuation), the git-lrc and roborev release counts, and the OpenQodex npm figure to the trailing-month window; star figures untouched per the standing exemption.
- 2026-10-25 - Recorded Ellipsis's free-for-individuals on-ramp leaving the homepage and pricing FAQ (pricing cell and the Ellipsis paragraph updated); the Kodus, Qodo, roborev, and Sourcery volatile re-checks found no cell changes, with star figures untouched per the standing exemption.
- 2026-10-27 - Refreshed the roborev release count to 123-plus (v0.74.0, October 27) and the OpenQodex npm figure to 7,739 trailing-month downloads (month to October 26); star figures untouched per the standing exemption.

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
- https://www.qodo.ai/ai-code-review-benchmark/ - the Qodo benchmark page grounding the February qualification: F1 framing, dataset links, fetched 2026-10-11
- https://www.qodo.ai/blog/how-we-built-a-real-world-benchmark-for-ai-code-review - the February 4, 2026 methodology post: 100 PRs, 580 injected issues, seven rivals, 60.1 percent F1, fetched 2026-10-11
- https://raw.githubusercontent.com/zhuyansen/agent-skills-hub/main/ops/review-runs/RESULTS.md - the Agent Skills Hub end-to-end eval table behind the fourth benchmark: sixteen tools on twelve PRs, no tool beating the bare-agent control, git-lrc unrunnable locally, fetched 2026-10-18
