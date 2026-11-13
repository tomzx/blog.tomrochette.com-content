---
title: Qodo
created: 2026-08-30
updated: 2026-11-13
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, code-review, ai-review, open-source, developer-tools]
readability: 3
audience_notes: >
  Software engineers evaluating AI pull request reviewers, who know what a
  GitHub Action and a webhook are, have heard of CodeRabbit and Copilot code
  review, and want to compare licensing, self-hosting, and cost before
  installing a bot on their repositories.
---

Qodo is an AI code review and governance platform (formerly CodiumAI) whose MIT-licensed PR-Agent was marketed as the original open-source AI PR reviewer, and which has now donated that reviewer to the community while selling the heavier product above it.

## What it is

**Two products share one name, and the gap between them is the whole story.**
The open-source half is PR-Agent (now under the PR-Agent GitHub organization), a community-maintained reviewer that runs /describe, /review, /improve, and /ask as PR comments or CLI calls against GitHub, GitLab, Bitbucket, Azure DevOps, and Gitea, self-hosted with any model LiteLLM can reach.
The commercial half is Qodo (the former Qodo Merge), a hosted review platform with a context engine, rules mined from PR history, cross-repo review, and dashboards.
On September 9, 2026 it launched the Agentic Toolbox, a CLI-installed pack of skills (codebase wisdom, pre-PR local review, rules retrieval, review-issue resolution) that puts that commercial engine inside Claude Code, Codex, and Kiro sessions.
On September 15, 2026 it launched the Software Map in beta, an automatically derived map of repos, service contracts, and blast radius that layers review findings over the architecture and feeds its review agents.
On October 1, 2026 it shipped Qodo 3.0, repositioning the platform as quality control for the agentic software factory: PR Triage (research preview) groups cross-repo work packages with blast radius and review order, review runs as a swarm of specialized agents, PR Insights exposes what the system learned from the team's review decisions, and enterprise surfaces add Gerrit, on-prem, air-gapped, and NVIDIA Nemotron models.
The repo description draws the line in one sentence: "This project is not the Qodo free tier."

## Status

Active on both halves, and deliberately splitting apart.
The repo counts 13,339 stars and 1,951 forks as of 2026-10-11, MIT-licensed, with v0.48.0 released October 16, 2026 (after v0.47.0 on October 2), and the former qodo-ai/pr-agent URL now redirects to the repo's new home in the standalone PR-Agent organization.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=qodo-ai/pr-agent&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=qodo-ai/pr-agent&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=qodo-ai/pr-agent&type=date&legend=top-left" />
</picture>

v0.47.0 hardens the tool: Gitea webhooks now fail closed without a configured secret, the GitHub Action fails on swallowed tool errors, GitLab and Bitbucket comment commands require a leading slash, extra_config_url became host-only, and model support added Claude Opus 5.5 and Bedrock Kimi K3.
v0.48.0 (October 16, 2026) is the first release flagged with breaking changes: `pip install pr-agent` no longer bundles the forge SDKs (they moved to per-provider extras such as `pr-agent[github]` or `pr-agent[all]`), the Docker service images run as a non-root user with mounted secrets and output directories needing matching permissions, and Azure DevOps and Bitbucket Server webhooks now require credentials.
v0.49.0 (October 25, 2026) extends the same hardening: GitHub polling now needs a host-only repository allowlist (`github.polling_repositories`, empty ignores every notification), `litellm.extra_headers` became host-only, Jira `project_keys` defaults flipped to `["*"]` with an empty list disabling lookups, the default model moved to gpt-6.1-sol, a `pr-agent doctor` command preflights a deployment, and /describe, /review, and /improve gained `--json-output`.
v0.50.0 (November 7, 2026) keeps tightening and locks the release pipeline: repository `.pr_agent.toml` files can no longer override GitHub pacing and retry settings, `config.num_retries` (now capped at ten), custom-label settings, or `pr_code_suggestions.max_number_of_calls`, `config.ai_timeout` and the suggestion-call count can no longer ride command comments, `config.enable_auto_approval` became host-only with the auto-approval path still disabled, and PyPI releases moved to Trusted Publishing with package attestations and a commit-reachable-from-main gate, while the feature train added a Microsoft Teams output sink, commit messages inside /review and /improve prompts, Claude Sonnet 5.5 and Haiku 5.5 plus Kimi K3 and K3.1 Pro model support, and GitHub Enterprise Cloud data-residency support.
The company raised $11M in 2023, then $40M in September 2024 ($50M total), by which point TechCrunch already called it "Qodo, the startup previously known as CodiumAI".
The README states Qodo donated PR-Agent to the community, the project has its first external maintainer, and it is being donated to an open-source foundation.
The company's badges report 911.2K VS Code and 655.1K JetBrains extension installs plus roughly 13.5K Marketplace installs for the paid app, as of 2026-10-26.
On Hacker News the reviewer itself never caught fire (best thread 24 points, item 41500840), while company research posts reached 139 (item 44874736) and 87 points (item 41838348), and the Kudelski exploit write-up got 1 point (item 46824997).

## Strengths

- The only tool in this comparison series with a genuinely open, MIT-licensed core you can self-host and point at any model through LiteLLM.
- Each tool is a single LLM call at roughly 30 seconds, so cost is predictable, with token-aware PR compression for large diffs.
- The command surface is documented and boring: /describe, /review, /improve, /ask, /add_docs, /generate_labels, /similar_issue, /update_changelog.
- Since v0.39.0 the OSS agent feeds AGENTS.md and SKILL.md files to /review, /describe, and /improve by default, so it picks up repo conventions out of the box.
- The commercial platform adds what review programs actually fight about: rules mined from PR history, cross-repo review across Git providers, and BYOK or on-prem deployment.

## Cautions

- The README now calls the OSS project a "community-maintained legacy project" and contrasts it with the "feature-rich, context-aware" commercial offering, which is the vendor telling you where the real product lives.
- Kudelski Security walked from a PR comment to RCE and an AWS admin key on Qodo Merge Pro (all fixed as of October 2025), and the root cause, config overrides injected through PR comments and repo config files, is a design decision in the open tool too.
- A developer reported leaving the JetBrains plugin over near-zero public activity and piled-up issues (HN comment 45880645, November 2025).
- The "highest F1-score" claim on the homepage is measured on the company's own benchmark, not a neutral one: Qodo published that benchmark (PR-Review-Bench) on February 4, 2026, injecting 580 issues into 100 merged PRs, comparing against seven rival tools, and reporting 60.1 percent F1 for itself, with the dataset public and every advantage on the vendor's side of the harness.
- There is no permanent free tier for the commercial product, credits expire monthly, and the historical $19/month PR-Agent Pro plan is gone.
- /help_docs sits disabled in the OSS tool since v0.36.1 over a credential-exposure bug (issue #2445), a window into community-maintenance pace.
- The company renamed itself from CodiumAI and retro-edited old blog posts to insert "(now Qodo (formerly Codium))", which muddies citations of its own history.

## Pricing

PR-Agent is free under MIT, self-hosted with your own LLM keys.
The commercial product meters pooled credits: the pricing page reads $0.015 per credit as of 2026-11-07, raised from the $0.012 rate last confirmed on 2026-10-26, with credit packs of 2,000, 4,000, and 16,000 credits (about 14, 29, and 114 reviews per month) replacing the earlier 2,500/5,000/20,000-credit packs, and no per-seat sticker displayed anywhere on the page (the $30 Pro Team price last appeared in page HTML on 2026-10-06).
The two vendor surfaces disagreed on the re-fetch date: the homepage FAQ still carried the older $0.012 rate with the 2,500/5,000/20,000 packs, so treat the pricing page as the operative rate until they agree.
The page keeps no annual commitment on the Pro Team plan, no permanent free tier, and monthly credit expiration, and Enterprise begins at 30-plus users.
Enterprise adds SSO/SAML, audit logs, BYOK, single-tenant SaaS or on-prem, cross-repo review, and negotiated pricing.
Qualified open-source projects get the commercial reviewer free through a Marketplace app powered by Google.
For history: in September 2024 the paid Chrome-extension tier was $19 per month for private repos (item 41443605), so the model has moved repeatedly in two years.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2024-09 | Chrome extension | Paid tier $19/month for private repos. | HN quote, see References |
| 2026-09-18 | Pro Team | Current: $30/month billed monthly, pooled credits at $0.012 each, packs sized around 18/36/144 reviews; PR-Agent free under MIT. Re-verified unchanged 2026-09-21 and 2026-10-26 (the page text still shows the credit rate, the pack sizes, and the 30-user enterprise boundary, with the $30 sticker absent from it). | [qodo.ai/pricing](https://www.qodo.ai/pricing/) |
| 2026-11-07 | Credit packs | Per-credit rate raised $0.012 to $0.015, and pack sizes moved from 2,500/5,000/20,000 credits (about 18/36/144 reviews) to 2,000/4,000/16,000 credits (about 14/29/114); no plan sticker displayed. The homepage FAQ still showed the older $0.012 rate on the same date. | [qodo.ai/pricing](https://www.qodo.ai/pricing/) |

## Compared to

[Greptile](../greptile/index.md) and [CodeRabbit](../coderabbit/index.md) are commercial-first rivals; if you need an MIT-licensed core you can self-host, Qodo is the one in this series that still ships it, and Kudelski's research series covers exploit chains in both Qodo and CodeRabbit.
[Open Code Review](../open-code-review/index.md) takes the no-vendor path, and the LaReview author's complaint that bots like PR-Agent "mostly comment file-by-file" and auto-post noise (item 46659042) is exactly the dissatisfaction that path answers.
[Ellipsis](../ellipsis/index.md) sat in the same PR-automation aisle before its 2026 pivot to agent infrastructure; its note carries the review-versus-hosting comparison.

## Bottom line

**Recommended for teams that want a self-hostable, MIT-licensed reviewer with a boring, inspectable command surface, and for enterprises that want rule enforcement and governance with BYOK or on-prem deployment.**
Not for developers hunting a permanent free tier for private repos, because that tier no longer exists.
I also think the PR-Agent donation is less a gift than a repositioning: the repo itself says "community-maintained legacy project", and I read that as the vendor conceding that the single-LLM-call reviewer is a commodity, so anyone adopting the OSS half for the long haul is adopting code the company has already stopped competing on.

## Changes

- 2026-08-30 - Created in the Code review category seed, recording the open-core PR-Agent split and the Kudelski security chains.
- 2026-09-13 - Added the September 9 Agentic Toolbox launch, which moves Qodo review and rules inside coding-agent sessions.
- 2026-09-18 - Added the September 15 Software Map beta (auto-derived repo, contract, and blast-radius map as review context), and refreshed repo and install counts.
- 2026-09-20 - Added the Price history section tracking price changes in a table, per the new owner rule.
- 2026-09-24 - Refreshed the repo to 13,142 stars and 1,890 forks with v0.46.0 (September 21) as the latest release, and the VS Code badge to 905.7K; verified the qodo-ai/pr-agent redirect into The-PR-Agent/pr-agent.
- 2026-10-03 - Recorded v0.47.0 (October 2): fail-closed Gitea webhook secrets, the GitHub Action failing on tool errors, leading-slash comment commands on GitLab and Bitbucket, host-only extra_config_url, and Claude Opus 5.5 plus Bedrock Kimi K3 model support.
- 2026-10-07 - Added the qodo-ai/pr-agent star history chart to the Status section.
- 2026-10-07 - Recorded Qodo 3.0 (October 1, 2026): PR Triage research preview, swarm review, PR Insights, and the quality-control-for-the-agentic-software-factory positioning; repo and install-badge counts refreshed.
- 2026-10-11 - Recorded the vendor's own public benchmark behind the homepage F1 claim (PR-Review-Bench, February 4, 2026: 100 PRs, 580 injected issues, seven rivals, 60.1 percent F1), added its two URLs to References, and refreshed repo counts.
- 2026-10-17 - Recorded v0.48.0 (October 16), the first release flagged with breaking changes: forge SDKs moved out of the base pip install into per-provider extras, Docker service images run non-root, and Azure DevOps and Bitbucket Server webhooks require credentials.
- 2026-10-26 - Rotation re-verification: recorded v0.49.0 (October 25), the host-only hardening continued (GitHub polling allowlist, litellm.extra_headers, the flipped Jira default), the gpt-6.1-sol default model, the doctor preflight command, and --json-output for /describe, /review, and /improve; every cited URL re-fetched live, all prices unchanged, and the install badges refreshed to their 2026-10-26 readings.
- 2026-10-30 - Volatile re-verification: the push moved to October 29 with v0.49.0 still the latest release; nothing else changed.
- 2026-11-01 - Volatile re-verification: the push moved to November 1 with v0.49.0 still the latest release; nothing else changed.
- 2026-11-05 - Volatile re-verification: the push moved to November 5 with v0.49.0 still the latest release; nothing else changed.
- 2026-11-05 - Pointed the See-also matrix link at the Code Review Feature Matrix; its line described this note's own category matrix but linked the evaluation-review one.
- 2026-11-07 - Volatile re-verification recorded a repricing: the pricing page now reads $0.015 per credit with 2,000/4,000/16,000-credit packs (about 14/29/114 reviews), raised from $0.012 with 2,500/5,000/20,000-credit packs last confirmed October 26, while the homepage FAQ still showed the older rate on the same day; the push moved to November 7 with v0.49.0 still the latest release.
- 2026-11-08 - Volatile re-verification recorded v0.50.0 (November 7): the host-only hardening extended to GitHub pacing and retry settings, custom labels, suggestion-call counts, and auto-approval (still disabled), PyPI releases moved to Trusted Publishing with attestations, and a Microsoft Teams output sink, commit messages in review prompts, and Claude Sonnet 5.5, Haiku 5.5, and Kimi K3/K3.1 Pro model support landed; the push moved to November 7 with the release.
- 2026-11-11 - Volatile re-verification: the push moved to November 11 with v0.50.0 still the latest release; nothing else changed.
- 2026-11-13 - Volatile re-verification: the push moved to November 12 with v0.50.0 still the latest release; nothing else changed.

## See also

- [Greptile](../greptile/index.md) - the codebase-aware SaaS rival, for readers weighing hosted context depth against self-hosted control.
- [Open Code Review](../open-code-review/index.md) - the no-vendor path this donation-and-funnel story is a reaction to.
- [Copilot Automations](../../executions/copilot-automations/index.md) - GitHub-native review automation for readers staying inside one vendor.
- [Code Review Feature Matrix](../code-review-feature-matrix/index.md) - the shared-rows comparison where this note's cells are traced.
- [Agents.md](../../protocols/agents-md/index.md) - why v0.39+ feeding AGENTS.md by default matters for repo-convention-aware review.

## References

- https://api.github.com/repos/qodo-ai/pr-agent - redirects to The-PR-Agent/pr-agent, the repo's new home; stars, forks, push date, MIT license, and the "This project is not the Qodo free tier" description, queried as of 2026-10-11, re-queried 2026-10-17, 2026-10-20, 2026-10-22, 2026-10-24, 2026-10-25, 2026-10-26, 2026-10-30, 2026-11-01, 2026-11-05, 2026-11-07, 2026-11-08, 2026-11-11, and 2026-11-13 (v0.50.0 published November 7, 2026, pushed the same day; the November 13 re-query found the push moved to November 12 with v0.50.0 still latest).
- https://api.github.com/repos/The-PR-Agent/pr-agent/releases/tags/v0.50.0 - the November 7, 2026 release notes: the host-only expansion, the num_retries cap, auto-approval host-only and still disabled, PyPI Trusted Publishing with attestations and a main-reachability gate, and the Microsoft Teams output sink, Sonnet 5.5 and Haiku 5.5 plus Kimi K3/K3.1 Pro model support, and GitHub Enterprise Cloud data-residency items, fetched 2026-11-08.
- https://github.com/qodo-ai/pr-agent - README: donation to the community, tools table, platforms, release notes, sponsor status, "legacy project" wording.
- https://docs.pr-agent.ai/tools/ - the full OSS command surface, including the /help_docs disabling.
- https://www.qodo.ai/ - positioning, context engine, rules system, self-reported benchmark claim, credit FAQ, install badges, re-fetched 2026-11-07: the homepage FAQ still carried the older $0.012-per-credit rate with 2,500/5,000/20,000-credit packs on the day the pricing page showed $0.015 with 2,000/4,000/16,000 packs.
- https://www.qodo.ai/pricing/ - Pro Team credit pricing, pack sizes, plan comparison, no permanent free tier, credits expiring monthly; re-read 2026-11-07: the page banner now shows $0.015 per credit with 2,000/4,000/16,000-credit packs (about 14/29/114 reviews), replacing the $0.012 rate and 2,500/5,000/20,000 packs confirmed through 2026-10-26; the $30 sticker has been absent from the page text since 2026-10-06 (last seen in page HTML that day), and the Enterprise boundary now reads "custom plan for 30+ users".
- https://www.qodo.ai/blog/introducing-qodos-agentic-toolbox/ - the Agentic Toolbox launch post, September 9, 2026, skills and plugin surface.
- https://www.qodo.ai/blog/introducing-qodos-software-map/ - the Software Map beta launch post, September 15, 2026, blast radius and contracts as review-agent context.
- https://www.qodo.ai/blog/what-every-software-factory-needs-that-no-model-will-provide/ - the Qodo 3.0 announcement essay, October 1, 2026: PR Triage research preview, swarm review, PR Insights, Gerrit and on-prem surfaces, the wisdom-base positioning.
- https://www.qodo.ai/solutions/open-source/ - free commercial review for qualified OSS projects.
- https://www.qodo.ai/blog/qodo-powered-by-testgpt-accounces-beta-and-raised-11m/ - the $11M seed and the original test-generation mission (the codium.ai URL now redirects here).
- https://techcrunch.com/2024/09/30/qodo-raises-40m-series-a-to-bring-quality-first-code-generation-to-the-enterprise/ - the $40M Series A, $50M total, and the CodiumAI-to-Qodo rename.
- https://kudelskisecurity.com/research/qodo-dynaconf-aws-admin-key-leaked-twice - critical source: PR comment to RCE and AWS admin key on Qodo Merge Pro, fixed October 2025.
- https://hn.algolia.com/api/v1/search?query=pr-agent&tags=story - PR-Agent's thin HN footprint (18 stories, best 24 points) and the 2024 $19/month pricing quote.
- https://hn.algolia.com/api/v1/items/45880645 - critical developer comment on Qodo plugin maintenance, November 2025.
- https://www.qodo.ai/blog/codiumai-or-codeium-which-are-you-looking-for/ - the Codeium name confusion and the retro-edited "formerly Codium" branding.
- https://www.qodo.ai/ai-code-review-benchmark/ - the vendor benchmark page behind the F1 claim: precision, recall, F1, "strongest overall performance", dataset links, fetched 2026-10-11.
- https://www.qodo.ai/blog/how-we-built-a-real-world-benchmark-for-ai-code-review - the February 4, 2026 methodology post: 100 merged PRs, 580 injected issues, seven rival tools, 60.1 percent F1, fetched 2026-10-11.
- https://docs.qodo.ai/ - commercial surface: code review, governance, cross-repo review, rule miner (the former /qodo-documentation path redirects here).
