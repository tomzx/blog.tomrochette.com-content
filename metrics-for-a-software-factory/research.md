---
topic: "Metrics and OKRs for a software factory where LLM agents run the full SDLC (2026)"
audience: "Software engineers and engineering leaders building agentic delivery systems"
status: draft
companion_to: "../index.md"
---

# Research Brief: Metrics for an Agent-Run Software Factory (2026)

## Scope

This brief maps the 2026 state of the art for measuring an agent-run software factory, meaning infrastructure where LLM agents carry work through the software lifecycle and a human supervises by exception. The question: what do practitioners and researchers say to measure, and why, when agents do the producing?

In scope: delivery frameworks (DORA and its agent-era extensions), factory and fleet metrics, autonomy and intervention measures, unit economics of agent runs, quality and rework guardrails, the leading indicators of agent effectiveness, capability benchmarks, and agent observability standards. Out of scope: model architecture, prompt technique, and code-generation methods.

Time bounds: roughly October 2025 through October 2026, with a few older anchors (METR 2025). "State of the art" here means two things together: what shipped in production tooling and what independent telemetry shows, since the most-cited factory metric set is still vendor-defined.

## Search Strategy

| Source type | Searched | Queries / notes |
|---|---|---|
| Surveys / reviews | Yes | "survey evaluating LLM coding agents benchmarks"; "agentic software engineering survey arXiv". Found the ACL 2026 agent-evaluation survey, the KDD 2025 agent-evaluation survey, the SDLC benchmark survey (2505.05283), and the reliability monograph (2608.13867). |
| Primary papers | Yes | arXiv, NBER, EASE 2026. Scaffold Effect (2607.22585), REAP/Harvest (2604.01527), Duma et al. PR review (2605.02273), Microsoft agentic-coding traces, Anthropic Claude Code expertise study. |
| Benchmark leaderboards | Yes | SWE-bench Verified and Pro, Terminal-Bench 4.0, DeepSWE, LiveCodeBench. Found SWE-bench Verified retired at the frontier in February 2026 and Terminal-Bench 4.0 released August 28, 2026. |
| Engineering blogs | Yes | DORA (2025 report, ROI 2026, "Balancing AI tensions", "tokenmaxxing"), Augment Code (factory metrics, maturity model), Warp (factory metrics, self-improvement), Port.io (agentic engineering metrics), Factory.ai, Cognition, Span, DX, Faros, Harness Engineering, Hiddedesmet. |
| Documentation / specs | Yes | OpenTelemetry GenAI semantic conventions (metrics, spans, registry attributes) and the OpenTelemetry GenAI observability blog (2026-05-14). |
| Community discussion | Yes | The tokenmaxxing thread across DORA, Faros, IBM, and InfoWorld (Meta Claudeonomics, Amazon Kirorank). |

Note: the search index mixes vendor guides with independent telemetry. Where a number comes from a vendor with a product in the category (Augment, Warp, Port, Factory, Span, LinearB), the entry is labeled as such.

## State of the Art

### Main Approaches

| Approach | Key idea | Representative work | Strengths | Limitations |
|---|---|---|---|---|
| DORA delivery metrics (pipeline) | Measure throughput and stability of the deploy pipeline | [DORA 2025](https://dora.dev/research/2025/dora-report), [DORA ROI 2026](https://dora.dev/ai/roi/report/), [five metrics guide](https://dora.dev/guides/dora-metrics/) | Established, comparable, free from existing CI/CD and incident data | Assumes human authorship; blind to generation volume; flat while agent output rises |
| Factory / fleet metrics | Measure the agent fleet and human reviewers as one production unit | [Augment, "Software Factory Metrics"](https://www.augmentcode.com/guides/software-factory-metrics), [Warp factory metrics](https://www.warp.dev/blog/agent-self-improving-software-factories), [Port.io catalog](https://www.port.io/guide/how-to-measure-agentic-engineering) | System-level; makes review capacity visible; gives cadence and owners | No dominant framework as of mid-2026; mostly vendor-defined; inconsistent definitions |
| Autonomy / intervention metrics | Measure how much work runs without a human | [Harness Engineering KPIs](https://github.com/Intense-Visions/harness-engineering/blob/main/docs/standard/kpis.md) (agent autonomy), Warp (automation percent), [Factory Analytics](https://factory.com/news/factory-analytics) (autonomy ratio), [Span](https://www.span.app/research/agent-effectiveness-july2026) (turn yield) | Directly measures the factory's purpose; moves week to week | No standard for what counts as an intervention; easy to raise by shrinking scope |
| Unit economics | Price output per accepted unit, not per token | [Cognition](https://cognition.com/blog/ai-productivity) (equivalent human hours), [Warp](https://www.warp.dev/blog/agent-self-improving-software-factories) (cost per PR), [Hiddedesmet](https://hiddedesmet.com/ai-coding-agents-need-kpis) (AI credits per merged PR) | Ties spend to delivered work; the metric a CFO reads | Attribution is noisy; token efficiency is only meaningful at system level, not per person |
| Quality / rework guardrails | Hold stability while autonomy climbs | DORA stability, [Faros tokenmaxxing data](https://www.faros.ai/blog/tokenmaxxing), SlopCodeBench, silent-failure telemetry | Catches the failure mode that volume hides | Churn and rework lag by 30 to 90 days; silent failures are invisible to agent self-report |
| Leading indicators / inputs | Steer the inputs that predict outcomes | [Span](https://www.span.app/research/agent-effectiveness-july2026) (prompt clarity, environment readiness, quality stewardship), Harness Engineering (context density) | Actionable in the current sprint; the levers a team can change | Correlational; vendor-run studies; small samples |
| Capability benchmarks | Rank models and harnesses on fixed tasks | [Terminal-Bench](https://www.tbench.ai/), [SWE-bench](https://www.swebench.com/verified), SWE-bench Pro, DeepSWE | Repeatable, comparable, good for shortlisting | Scaffold confound (2607.22585), contamination (SWE-bench Verified retired), saturation, weak predictor of production reliability |
| Observability standards | Standardize agent telemetry | [OpenTelemetry GenAI semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai) | Cross-vendor spans, metrics, and evaluation attributes; emitted by Copilot, Codex, Claude Code | Development status; client-side; no factory-level semantics yet |
| Productivity research (anchor) | Ground productivity claims in measurement | [METR](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study), [Anthropic Claude Code study](https://www.anthropic.com/research/claude-code-expertise), [NBER w35275](https://www.nber.org/papers/w35275) | Independent of vendors; large samples | Snapshots of a moving target; different settings |

### Current Best Results

What the numbers show, grouped by claim.

**Generation rises, delivery does not follow proportionally.**

- [Faros AI](https://www.faros.ai/blog/tokenmaxxing) (vendor telemetry), across 22,000 developers on 4,000 teams: task completion up 34%, epics per developer up 66%, but bugs per developer up 54%, median review time up 5x, PRs merged with no review up 31%, and code churn up 861% in high-adoption environments.
- A second Faros study across 1,255 teams found 98% more merged pull requests alongside 91% longer review times, with no organizational-level correlation between AI adoption and outcomes ([Augment, citing Faros](https://www.augmentcode.com/guides/software-factory-metrics)).
- [NBER w35275](https://www.nber.org/papers/w35275), over 100,000 GitHub developers: commits rise 40% for autocomplete, 140% for interactive agents, and 180% for autonomous agents, attenuating to 50% for projects and 30% for releases.

**Verification is the binding constraint.**

- [LinearB](https://linearb.io/library/ai-in-software-development) (vendor telemetry), 8.1 million pull requests across 4,800 teams: agentic pull requests wait 5.3 times longer than unassisted ones before pickup, and AI pull requests 4.6 times longer for a first review.
- [Duma et al., EASE 2026](https://arxiv.org/abs/2605.02273): most AI-generated pull requests receive no review at all, and the reviews they do receive are dominated by AI agents, not humans.
- DORA names the mechanism the [verification tax](https://dora.dev/insights/balancing-ai-tensions/): time saved writing is re-spent auditing, and 30% of developers report little or no trust in AI-generated code.

**Autonomy is measurable and currently modest.**

- [Anthropic's study of about 400,000 Claude Code sessions](https://www.anthropic.com/research/claude-code-expertise) (October 2025 to April 2026): people make most planning decisions and the agent makes most execution decisions. Verified success is about 30% for software occupations and 26% elsewhere, rising to 34% and 29% for sessions that produce code. Sessions rated expert reach verified success more than twice as often as novice ones.
- [Harness Engineering](https://github.com/Intense-Visions/harness-engineering/blob/main/docs/standard/kpis.md) defines agent autonomy as the percentage of PRs merged without human code intervention, places high autonomy in the 70% to 90% band, and reports 35% current against a 60% near-term target.

**Benchmarks do not predict production.**

- Terminal-Bench 4.0, released 2026-08-28, tops out near [58% on the public board](https://www.tbench.ai/) (GPT-6 Astra in Codex at 58.2%, Claude Fable 5.1 in Claude Code at 57.9%).
- [SWE-bench Verified](https://www.swebench.com/verified) is retired at the frontier; OpenAI stopped evaluating on it on 2026-02-23 after a test audit, and the leaderboard has no new entries since 2026-02-26.
- The [Scaffold Effect](https://arxiv.org/abs/2607.22585) paper finds harness choice induces up to a 40x difference in tokens per solved task, with pass-rate differences of 0 to 8 points, so a leaderboard row is a harness plus a model, not a model.
- Reported lab-to-production gap: about [37 points](https://sonnetcode.com/blog/enterprise-ai-agent-37-percent-lab-production-gap); production success across 4.5 million runs reported at [56.6%](https://prefactor.tech/blog/silent-wins-visible-fails-agent-production-success-metrics), with 45% to 75% of failures reported as success.

**The metric-gaming failure is documented.**

- [DORA on tokenmaxxing](https://dora.dev/insights/finding-balance-in-the-era-of-tokenmaxxing/): raw token count is an input, easy to game, and a vanity metric. The piece cites Salesforce Agentic Work Units, Shopify replacing a leaderboard with a usage dashboard plus circuit breakers, and Starburst measuring DORA plus cost per accepted change and rework.
- Meta's internal token leaderboard and Amazon's Kirorank were both withdrawn after engineers gamed them by running agents on idle work.

### Consensus and Disagreement

Where the field agrees:

- **AI raises activity, not delivery, on its own.** DORA 2025 finds AI amplifies the existing system, with higher adoption associated with both throughput and instability. The NBER and Faros data show the same gap.
- **The constraint moved from generation to verification.** Augment, Warp, Port, and DORA all locate the bottleneck at review capacity.
- **Effort and input metrics are not targets.** Tokens, lines, commits, and PR counts are consensus vanity metrics. DORA's Goodhart framing, Faros' tokenmaxxing critique, and IBM's "valuemaxxing" all agree.
- **Measure the system, never the individual.** DORA, DX, and Augment all warn against per-person use; DX treats agents as extensions of the team that directs them.
- **You need a pre-AI baseline and PR tags by producer type** before any attribution means anything (Augment, DX, Hiddedesmet).
- **Cost per accepted or completed unit beats cost per token.** Warp uses cost per PR; Hiddedesmet uses AI credits per merged PR; DORA cites cost per accepted change.

Where the field disagrees or has no standard:

- **No dominant fleet framework exists.** Augment states outright that no fleet-level framework has become dominant as of mid-2026, citing a Harness survey of 700 developers and leaders.
- **What counts as an intervention.** Warp counts human touchpoints per PR, Factory counts tool calls per user message, Span counts merged lines per human turn, Harness Engineering counts PRs merged without human code intervention. These are different units.
- **Whether autonomy or outcome leads.** Port.io puts outcome-verified "agent success rate" as the gold standard; Harness Engineering puts agent autonomy first.
- **Whether LLM judges are reliable.** Berkeley and Stanford work cited by [Prefactor](https://prefactor.tech/blog/silent-wins-visible-fails-agent-production-success-metrics) found LLM judges reach a maximum AUROC of 0.65 on false-success detection, and that deterministic state checks beat them.
- **How to count DORA lead time for agent-initiated PRs.** Hiddedesmet notes there is no consensus and recommends keeping agent PRs separate.
- **Model versus harness attribution.** The Scaffold Effect paper and the reliability monograph both treat this as open.

## Key Sources

| Source | Type | Year | Authority signal | Credibility | Why it matters |
|---|---|---|---|---|---|
| [DORA, State of AI-assisted Software Development 2025](https://dora.dev/research/2025/dora-report) | Report | 2025 | Long-running Google Cloud research program (State of DevOps since 2014) | Strong | The 90% adoption, 80% perceived productivity, 30% distrust figures; AI as amplifier; throughput up with instability |
| [DORA, ROI of AI-assisted Software Development](https://dora.dev/ai/roi/report/) | Report | 2026 | Same DORA program; ROI report leans advocacy | Strong | The J-curve and verification tax; a worked ROI model; the instability cost |
| [DORA, "Balancing AI tensions"](https://dora.dev/insights/balancing-ai-tensions/) | Insight | 2026 | Same DORA program | Strong | Names the verification tax and the review-capacity shift |
| [DORA, "Finding balance in the era of tokenmaxxing"](https://dora.dev/insights/finding-balance-in-the-era-of-tokenmaxxing/) | Insight | 2026 | Same DORA program | Strong | The clearest statement that input metrics are gameable, with company counterexamples |
| [Augment Code, "Software Factory Metrics"](https://www.augmentcode.com/guides/software-factory-metrics) | Vendor guide | 2026 | Vendor with a product in the category | Moderate | The five-category taxonomy, the instrumentation order, and the DORA-versus-factory comparison |
| [Warp, "Closing the loop with self-improving cloud software factories"](https://www.warp.dev/blog/agent-self-improving-software-factories) | Vendor blog | 2026 | Vendor with a product in the category | Moderate | The core factory metric set: PR throughput, cost per PR, automation percent, savings over human work |
| [Port.io, "How to measure agentic engineering"](https://www.port.io/guide/how-to-measure-agentic-engineering) | Vendor guide | 2026 | Vendor with a product in the category | Moderate | A 25-metric catalog including outcome-verified agent success rate and automation coverage by phase |
| [Cognition, "Estimating the Productivity of an Autonomous AI Software Engineer"](https://cognition.com/blog/ai-productivity) | Vendor research | 2026 | Vendor (Devin) measuring its own product | Moderate | Equivalent human hours as the unit, and evidence that lines changed is a weak proxy |
| [Span, "AI Coding Agent Effectiveness: Leading Indicators"](https://www.span.app/research/agent-effectiveness-july2026) | Vendor research | 2026 | Vendor with a product in the category; small, vendor-run study | Moderate | Prompt clarity, environment readiness, quality stewardship, with effect sizes |
| [Harness Engineering KPIs](https://github.com/Intense-Visions/harness-engineering/blob/main/docs/standard/kpis.md) | Open repo | 2026 | 21 stars, 12 forks; small org repo | Weak | A concrete autonomy target, the harness-coverage and context-density inputs, and a composite unwatched-safety outcome KPI |
| [Faros, "Tokenmaxxing"](https://www.faros.ai/blog/tokenmaxxing) | Vendor research | 2026 | Vendor with a product in the category; telemetry methodology not published | Moderate | Telemetry that pairs rising throughput with rising bugs, review time, and churn |
| [NBER w35275](https://www.nber.org/papers/w35275) | Paper | 2026 | NBER working paper (Demirer, Musolff, Yang) | Strong | Commit gains attenuate across the production hierarchy |
| [Scaffold Effect in Coding Agents](https://arxiv.org/abs/2607.22585) | Paper | 2026 | arXiv preprint; no citations yet | Moderate | Harness choice drives a 40x token spread; leaderboard rows are model-plus-harness |
| [Engineering Reliable Coding Agents](https://arxiv.org/abs/2608.13867) | Monograph | 2026 | arXiv preprint; single author | Moderate | Framing agents as systems; evaluation and operation as a dependency chain |
| [Duma et al., AI PR review](https://arxiv.org/abs/2605.02273) | Paper | 2026 | arXiv preprint (EASE 2026) | Moderate | Most AI PRs go unreviewed; AI agents do much of the review that happens |
| [Anthropic, Claude Code expertise](https://www.anthropic.com/research/claude-code-expertise) | Vendor research | 2026 | Vendor (model maker) studying its own product; large n | Moderate | Autonomy and success rates from about 400,000 live sessions |
| [METR, early-2025 AI and developer productivity](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study) | Paper | 2025 | Independent nonprofit; 16 developers, not a large sample | Strong (small n) | 19% slower while believing 20% faster; the perception gap |
| [OpenTelemetry GenAI semantic conventions](https://github.com/open-telemetry/semantic-conventions-genai) | Standard | 2026 | open-telemetry org repo; 407 stars, 116 forks | Strong | The emerging standard for agent telemetry, spans, token metrics, and evaluation attributes |
| [Bun, rewriting Bun in Rust](https://bun.com/blog/bun-in-rust) | Postmortem | 2026 | Company postmortem; self-reported and promotional | Moderate | The positive case: 535,496 lines in 11 days, zero tests removed, adversarial review, a present supervisor |

### Inline Citations Not Promoted to Key Sources

Sources cited in the body that do not carry a Key Sources row, listed with a rating so the gap is visible.

| Source | Type | Authority signal | Credibility | Issue |
|---|---|---|---|---|
| [DORA, "Software delivery metrics"](https://dora.dev/guides/dora-metrics/) | Docs | Same DORA program | Strong | Left off the Key Sources table only to avoid a fourth DORA row |
| [SWE-bench Verified](https://www.swebench.com/verified) | Leaderboard | Maintained benchmark; 500 human-reviewed instances | Strong | Cited for its retirement, not for a score |
| [Terminal-Bench](https://www.tbench.ai/) | Leaderboard | Maintained by Stanford, the Laude Institute, and Harbor | Moderate (model-plus-harness) | Scores shift with harness and version |
| [LinearB, "AI in software development"](https://linearb.io/library/ai-in-software-development) | Vendor research | Vendor of engineering-metrics tooling; two large PR datasets | Moderate (vendor) | Promotes the category it sells into |
| [Factory, "Factory Analytics"](https://factory.com/news/factory-analytics) | Vendor blog | Vendor with a product in the category | Moderate (vendor) | The autonomy ratio is vendor-defined |
| [DX, "Measuring AI code assistants and agents"](https://getdx.com/research/measuring-ai-code-assistants-and-agents/) | Vendor research | Vendor (DX platform), millions of benchmark samples | Moderate (vendor) | Cited for the system-not-individual stance |
| [IBM, "Tokenmaxxing is dead, long live valuemaxxing"](https://www.ibm.com/think/insights/tokenmaxxing-dead-long-live-valuemaxxing) | Vendor blog | Vendor (IBM Bob) | Moderate (vendor) | Coins a term on a page selling a platform |
| [Harness, State of Engineering Excellence](https://www.harness.io/state-of-engineering-excellence) | Vendor survey | Vendor (Harness); 700 self-reported respondents | Weak (self-reported vendor survey) | Reached second-hand through Augment |
| [Hiddedesmet, "AI coding agents need KPIs"](https://hiddedesmet.com/ai-coding-agents-need-kpis) | Personal blog | Named author, no sales pitch | Weak | A practitioner proposal, not evidence |
| [Sonnetcode, "37% lab-to-production gap"](https://sonnetcode.com/blog/enterprise-ai-agent-37-percent-lab-production-gap) | Services blog | No named author; ends in a sales pitch | Weak | States an 88.6% SWE-bench Verified score as current in July 2026 while the brief says the benchmark was retired in February 2026 |
| [Prefactor, "Silent wins, visible fails"](https://prefactor.tech/blog/silent-wins-visible-fails-agent-production-success-metrics) | Vendor blog | Vendor (Prefactor) | Weak | Cites its own posts; the Berkeley/Stanford LLM-judge finding links back to Prefactor, and the 56.6% figure links to a personal blog |

Also cited inline without a link, so they cannot be rated: SlopCodeBench, SWE-bench Pro, DeepSWE, the Meta token leaderboard and Amazon Kirorank withdrawals, and the OpenAI SWE-bench retirement date.

## Open Questions / Gaps

1. **No standard autonomy metric.** Every vendor defines intervention differently, so cross-organization comparison is impossible today.
2. **Silent failure is unmeasured.** Agent self-report succeeds while the environment shows failure in 45% to 75% of cases, and the field has no settled independent-state check.
3. **Model versus harness attribution.** Benchmarks and production results both mix the two, and the fix (a controlled harness variable) is only recently proposed.
4. **Long-horizon reliability measurement.** Per-step success compounds, and proposed tools (reliability decay curves) are not yet standard.
5. **Silent quality erosion.** SlopCodeBench and churn data suggest maintainability degrades across long agent runs while unit tests stay green.
6. **Economic attribution at scale.** Cost per accepted change is agreed in principle, but there is no common definition of "accepted."
7. **Metric governance.** The field agrees not to use these metrics on individuals, but no framework encodes that as a constraint.
8. **Comprehension debt.** Who can maintain the agent-written code, and how is ownership measured, remain open.

## Recommendation for the Article

**Core insight:** the field has converged on the claim the draft already makes. Generation is cheap, verification is the binding constraint, and the only factory metrics worth a target are the share of work that runs without a human and the share of that work that survives, priced per accepted change and guarded by stability. The draft's autonomy-plus-yield framing matches the strongest 2026 evidence; the new material is the proof behind it and the two refinements below.

**Angle:** keep the draft as the measurement layer of the software-factory literature, and use the 2026 telemetry as its evidence. Three upgrades are worth making.

1. **Ground the "output rises, outcomes do not" claim in telemetry.** The draft asserts it; Faros (98% more PRs, 91% longer reviews, churn +861%), NBER (commits +180% but releases +30%), and DORA (throughput up with instability) prove it. Add one or two of these numbers.
2. **Add independent verification as a named guardrail.** The 2026 evidence says agent self-report is not a success signal (45% to 75% false-success). This extends the draft's yield definition: yield must be measured by querying the environment, not by reading the agent's summary.
3. **Refine two claims.** DORA now carries five metrics and added deployment rework rate itself, so rework is not only a factory addition. And the autonomy definition should name the unit of intervention explicitly, since the field's disagreement is exactly there.

**Sources to lead with:** DORA 2025 and the ROI report; Augment "Software Factory Metrics"; Warp's factory metrics; Faros tokenmaxxing; Cognition; Anthropic Claude Code study; OpenTelemetry GenAI. The Bun postmortem remains the one positive case where high autonomy shipped, and it shipped because verification was dense.
