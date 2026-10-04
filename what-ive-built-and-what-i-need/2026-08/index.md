---

title: "What I've built and what I need: August 2026"
created: 2026-10-04
type: post
status: finished
tags: [what-ive-built-and-what-i-need, personal-update, llm, ai-agents, automation, sdlc, pdlc, workflows, fully-ai-generated, llm=deepseek-v4.1-flash]
readability: 3
audience_notes: >
  A monthly status update for anyone following my work on LLM-driven software development pipelines. Assumes familiarity with the SDLC skills and introduces the new PDLC set; no prior exposure to the earlier updates is required.
agent_sessions:
  - ses_ef95d31a6ffe1z1L1kOJ1QEq12
---

The headline this month was **the product-side counterpart to the SDLC: a full PDLC skill set that carries an idea from discovery through measurement**.
August also realigned the verification skills around non-overlapping roles, added several new pipeline phases, and completed the ISO/IEC 25010 audit set.
The month came to 61 commits, over 500 files changed, and 30 new skills.

## What I Have Been Working On

**Shipped the [PDLC](https://github.com/tomzx/agents/blob/main/skills/pdlc/SKILL.md) pipeline.**
This was last month's open need, and it is now a self-contained product development lifecycle that wraps the engineering one.
It covers discovery, validation, strategy, definition, launch, and measurement, with a proceed, pivot, or kill gate at every phase.
[PDLC](https://github.com/tomzx/agents/blob/main/skills/pdlc/SKILL.md) is the only slash command; the 31 phase and cross-cutting sub-skills live under `skills/pdlc/skills/` and the orchestrator loads them on demand.
Artifacts live under `.pdlc/`, mirroring the `.sdlc/` conventions: a shared reference file, a `PDLC_DIR` fallback, a state file, and a revision mode.
Definition is the seam where the product work hands the settled what and why to SDLC.
Two supporting skills came with it, [create-roadmap](https://github.com/tomzx/agents/blob/main/skills/create-roadmap/SKILL.md) and [review-roadmap](https://github.com/tomzx/agents/blob/main/skills/review-roadmap/SKILL.md), and [identify-feature-opportunities](https://github.com/tomzx/agents/blob/main/skills/identify-feature-opportunities/SKILL.md) generates and ranks new ideas from the code surface.

**Realigned the verification skills.**
[validate-pr](https://github.com/tomzx/agents/blob/main/skills/validate-pr/SKILL.md), [verify-pr](https://github.com/tomzx/agents/blob/main/skills/verify-pr/SKILL.md), and [review-pr](https://github.com/tomzx/agents/blob/main/skills/review-pr/SKILL.md) had overlapping mandates, so I split them into three questions: validate-pr asks whether the change builds the right product, verify-pr asks whether the product is built right using runtime proof, and review-pr judges code craft from static reading alone.
The new [review-requested-prs](https://github.com/tomzx/agents/blob/main/skills/review-requested-prs/SKILL.md) orchestrator runs the three across the PRs waiting on me and skips any step already done for the current commit using SHA markers.
[analyze-test-coverage](https://github.com/tomzx/agents/blob/main/skills/analyze-test-coverage/SKILL.md) became its own skill for reporting introduced tests, change coverage, and uncovered code, and [review-pr-full](https://github.com/tomzx/agents/blob/main/skills/review-pr-full/SKILL.md) chains the whole review into one pass.

**Added SDLC phases and artifacts.**
A new [validate-assumptions](https://github.com/tomzx/agents/blob/main/skills/validate-assumptions/SKILL.md)/[review-assumption-validation](https://github.com/tomzx/agents/blob/main/skills/review-assumption-validation/SKILL.md) phase collects the assumptions made during design, runs the cheapest experiment that could invalidate each risky one, and blocks implementation when an assumption fails.
[create-lifecycle](https://github.com/tomzx/agents/blob/main/skills/create-lifecycle/SKILL.md)/[review-lifecycle](https://github.com/tomzx/agents/blob/main/skills/review-lifecycle/SKILL.md) document how a resource's states, transitions, and retention change over time, and [create-domain-model](https://github.com/tomzx/agents/blob/main/skills/create-domain-model/SKILL.md)/[review-domain-model](https://github.com/tomzx/agents/blob/main/skills/review-domain-model/SKILL.md) became standalone so a domain can be understood before solutioning.
[create-project](https://github.com/tomzx/agents/blob/main/skills/create-project/SKILL.md)/[review-project](https://github.com/tomzx/agents/blob/main/skills/review-project/SKILL.md) fill the context files for a new repository, and [create-question](https://github.com/tomzx/agents/blob/main/skills/create-question/SKILL.md)/[review-question](https://github.com/tomzx/agents/blob/main/skills/review-question/SKILL.md) record open questions with what they block.
[create-cli-design](https://github.com/tomzx/agents/blob/main/skills/create-cli-design/SKILL.md) settles a feature's command surface as a companion artifact to requirements.
Generated artifacts carry a `session_link` so a reviewer can reopen the session that produced them, `create-*` auto-dispatches its `review-*` in a subagent, and outcome files list the artifacts a phase produced.
A single HTML slide deck now presents the whole SDLC family.

**Completed the ISO/IEC 25010 audit set.**
[audit-sdlc](https://github.com/tomzx/agents/blob/main/skills/audit-sdlc/SKILL.md) is now the coordinator for the [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) quality model, with a mapping table from each characteristic to a skill.
One skill now covers each remaining characteristic: functional suitability, performance efficiency, compatibility, usability, reliability, maintainability, and portability, alongside the existing security and observability audits.

**Shipped general-purpose skills.**
[devils-advocate](https://github.com/tomzx/agents/blob/main/skills/devils-advocate/SKILL.md) argues the strongest case against an idea, plan, or decision before you commit.
[gh-stack](https://github.com/tomzx/agents/blob/main/skills/gh-stack/SKILL.md) manages stacked pull requests.
[post-slack-message](https://github.com/tomzx/agents/blob/main/skills/post-slack-message/SKILL.md) posts or threads a Slack message.
[stakeholder-announcement](https://github.com/tomzx/agents/blob/main/skills/stakeholder-announcement/SKILL.md) drafts and posts infrastructure updates to stakeholder channels.
[agents-section-daily-refresh](https://github.com/tomzx/agents/blob/main/skills/agents-section-daily-refresh/SKILL.md) runs the daily curation of the agent-maintained section of this blog.
[sync-articles](https://github.com/tomzx/agents/blob/main/skills/sync-articles/SKILL.md) brings a batch of articles into conformance with the writing rules.
[handle-pr-author-feedback](https://github.com/tomzx/agents/blob/main/skills/handle-pr-author-feedback/SKILL.md) (renamed from `handle-pr-feedback`) verifies that an author's new commits answer your review comments.

**Gated GitHub writes and reworked tooling.**
A `should-post-to-github` script now gates every GitHub content write, and the PR skills default to not posting, so a comment or merge only happens when `--post` is passed.
SDLC worktrees moved to `/tmp/sdlc/<owner>/<repo>/<issue>`, and `~/.sdlc/**` and `/tmp/sdlc/**` are pre-approved in the agent CLI so unattended runs are not stopped by a prompt.
Script references moved to `~/.agents/scripts/`, the audit and find skills switched from grep to ripgrep, and `CLAUDE.md` and `.claude` were replaced by `AGENTS.md` and `.agents` across the library.

**Tightened conventions.**
[create-article](https://github.com/tomzx/agents/blob/main/skills/create-article/SKILL.md) now requires naming the referent rather than leaving a vague it, and the 2-5 link cap on its See also sections was removed.

## What I Currently Need

I did not write this entry at the time, so I have no record of what I needed in August and am stating that plainly rather than reconstructing a list I cannot trust.

## See also

- [What I've built and what I need: July 2026](../2026-07/index.md) - the previous entry in this series; August delivers the PDLC pipeline it asked for.
- [The Self-Evolving Repository](../../the-self-evolving-repository/index.md) - the end-to-end automation vision that the SDLC and PDLC pipelines now serve.
- [Loops as Files](../../loops-as-files/index.md) - the scheduling layer that runs skills unattended, which the daily refresh and PR skills rely on.
- [Iterating on Agent Skills](../../iterating-on-agent-skills/index.md) - how the skill library changes over time, of which this month's 30 additions are one step.
- [A Pull Request Is a Claim, Not Evidence](../../a-pull-request-is-a-claim-not-evidence/index.md) - the reasoning behind splitting verification into a right-product check and a built-right check.

## References

- [agents](https://github.com/tomzx/agents) - the skill library where the PDLC pipeline, the verification realignment, and the audit set landed.
- [ISO/IEC 25010](https://en.wikipedia.org/wiki/ISO/IEC_25010) - the quality model the audit skills now map one to one.
- [ghx](https://github.com/TomzxCode/ghx) - the GitHub CLI used across the review and feedback skills.
