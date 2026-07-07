---
title: "Straight to Main: Learnings from OpenClaw's Commit History"
created: 2026-07-07
type: post
status: finished
tags: [open-source, software-engineering, git, llm, ai, code-review, agents, governance, fully-ai-generated, llm=claude]
readability: 3
audience_notes: >
  Assumes the reader has run `git log` on someone else's project, knows what pull requests, squash merges, and conventional commits are, and has at least watched an LLM coding agent work. No introduction to version control or to what OpenClaw is beyond the first paragraph.
---

Scrolling through the commit history of [OpenClaw](https://github.com/openclaw/openclaw), a self-hosted AI assistant that grew from a personal playground into one of the fastest-moving open source projects around, I noticed something about its two most prolific contributors.
Peter Steinberger, the founder, commits straight to `main`, no pull request in sight.
Vincent Koc, the second most prolific contributor, shows a mix of both direct commits and merged pull requests.

My first reading was a story about personalities: Peter builds whatever he finds relevant without ever looking at the open issues, while Vincent and the other maintainers absorb the incoming stream of bug reports.
It is a satisfying story, and it might even be partially true.
But an impression formed by scrolling a commit feed is a hypothesis, not a finding, so I cloned the repository and measured.
**The data confirms that the two men are doing different jobs, but it locates the difference somewhere more interesting than merge etiquette, and the way it complicates the story is itself the first learning.**

## The shape of the repository

The numbers first, because OpenClaw's scale is what makes its patterns legible.
As of early July 2026, the repository holds about 64,900 commits from about 2,700 distinct authors, accumulated since the first commit in late November 2025.
That is roughly 290 commits per day, every day, for seven and a half months, on a project that renamed itself three times along the way (Warelay, then Clawdbot, then Moltbot, then OpenClaw).

Peter Steinberger has about 32,900 of those commits, slightly over half the project.
Vincent Koc has about 10,200, roughly 16 percent.
The third name, Shakker, has about 3,700.
After that the curve drops fast into a long tail of one-commit contributors, punctuated by bots: `github-actions` has landed over a thousand commits, and a janitorial bot named `clawsweeper` a couple hundred more.

Sit with Peter's number for a second.
An average of about 145 commits per day, sustained for seven months, is not a human typing rate.
It is the output of one person operating a fleet of LLM coding agents, and the repository is open about this: OpenClaw is an AI agent product, built visibly with AI agents, and its contribution guide treats AI-authored work as a first-class citizen.
Every pattern in this history has to be read with that in mind, because most of our intuitions about commit hygiene were formed when a commit cost a human twenty minutes.

## Testing the impression

Measuring the direct-to-main split is easy once you know one trick: when a commit lands through GitHub's merge button, the committer field is rewritten to `GitHub <noreply@github.com>`, while a direct push keeps the author as committer.
Combine that with the `(#1234)` suffix GitHub appends to squash merges and you can classify nearly every commit without leaving the terminal.

The impression survives its first contact with data.
About 96 percent of Peter's commits are direct pushes to `main`.
Vincent has landed about 1,200 commits through GitHub-merged pull requests, roughly 12 percent of his total, three times Peter's rate.
Peter straight to main, Vincent a mix: confirmed.

Then the data starts to push back, in three ways.

First, Vincent is not the process-following foil the story wants him to be.
87 percent of his commits are also direct pushes.
The real split is not "Peter bypasses review, Vincent uses it."
It is that both trusted maintainers default to direct commits, and Vincent routes somewhat more of his work through review than Peter does.

Second, the issue-tracker half of my hypothesis is unmeasurable from the commit log, and what little signal exists refuses to cooperate.
Of Peter's 32,900 commits, only 84 contain a `fixes #N`-style issue closer.
Vincent's rate is nearly identical: 43 out of 10,200.
Neither man's commits visibly reference the issue tracker, so the log cannot distinguish "ignores the issues" from "works the issues without citing them."
The honest statement is narrower than my hypothesis: the commit log shows what each person works *on*, not what prompted it.

Third, and most damaging to the personality story, the direct-to-main habit turns out not to be a fixed trait.
In the most recent thirty days the pattern inverted: roughly 70 percent of Peter's commits landed through pull requests, while Vincent, who out-committed Peter three-to-one in June, landed 95 percent of his work directly.
Whatever direct-to-main signals, it is not "who Peter is."
It tracks the kind of work each person happens to be doing that month.

## Learning 1: the pull request is a trust boundary, not a quality gate

So what does the direct-to-main pattern actually mean, if not carelessness?

Look at where OpenClaw *does* demand pull requests.
External contributors face a gauntlet: a PR template requiring a stated problem, user impact, and an evidence section with test output or screenshots; a mandatory AI-review pass (`codex review`) whose findings the author must address before a human looks; a hard cap of twenty open PRs per author, automatically enforced with a label and auto-close; outright refusal of refactor-only PRs; and a warning that PRs over about 5,000 changed lines are reviewed "only in exceptional circumstances."

Inside the maintainer circle, none of that applies.
The founder pushes to `main` at will, and so, it turns out, does Vincent.

**The pull request here is not functioning as a quality gate that all code must pass; it is functioning as a trust boundary, and process intensity is set by where you stand relative to that boundary, not by what the change contains.**
This offends the uniform-process instinct most teams carry, the one that says the rules are the rules for everyone.
But the uniform instinct quietly assumes review capacity is free.
Review by whom, exactly?
Peter wrote half the project.
A pull request from him would be reviewed by someone who knows less about the code than he does, which converts review from a defect filter into a ceremony.
Meanwhile every unit of maintainer attention spent on that ceremony is a unit not spent on the long tail of 2,700 strangers, where review actually catches things.
I have argued before, in [Developer Trust Profiles](../developer-trust-profiles/index.md), that automated review should scale scrutiny to the author's track record; OpenClaw applies the same principle to human process, in its bluntest possible form.

The lesson is not "let your best people skip review."
The lesson is that every project already has a trust boundary, and the only choice is whether it is explicit.
OpenClaw's is written down: a `CONTRIBUTING.md` that names a "Benevolent Dictator," about twenty-seven maintainers each with a listed area of ownership, and an instruction to contributors to route work through labels and `CODEOWNERS` rather than guessing whom to tag.
A project that claims uniform process while its founder quietly merges their own PRs thirty seconds after opening them has the same boundary and a less honest map of it.

## Learning 2: the roles are real, but they live in the prefixes, not the merge button

If merge behavior does not separate Peter and Vincent, what does?
The conventional-commit prefixes and scopes do, sharply.

Half of Vincent's commits are `fix:`.
Two percent are `feat:`.
He essentially owns a scope that barely exists in anyone else's history: of the 161 commits tagged `(deadcode)`, project-wide, 151 are his.
His fingerprint is that of a consolidator, someone cleaning, hardening, and deleting behind a fast-moving front.

Peter's distribution is flatter: 28 percent `fix`, 28 percent `test`, 14 percent `refactor`, 11 percent `docs`, with `feat`, `perf`, `ci`, and `chore` filling out the rest.
And his `feat` scopes trace the product frontier: the macOS app, iOS, Android, the browser, the gateway, plugins, skills.
He builds outward across the entire surface, and because his volume is triple Vincent's, he is simultaneously the project's largest bug-fixer in absolute terms.

So my original hypothesis was half right, and the half that was right was not the half I could see from the merge button.
There genuinely is a builder pushing the frontier and a consolidator keeping it from collapsing, and the pattern extends down the contributor list: Shakker, the third most prolific contributor, is two-thirds `test:` commits, a person whose entire beat is the safety net.
**The role structure of a project is written in its prefix distributions, and reading those beats reading merge behavior, because merge behavior measures trust while prefixes measure the actual division of labor.**

This distinction matters when you audit your own project.
The tempting inference, the one I started with, runs from process to character: he skips PRs, therefore he ignores the community.
The supported inference runs from work to role: her commits are half `fix` and she owns `deadcode`, therefore the project has a consolidator, and it needs one, because a codebase absorbing 290 commits a day accumulates entropy at 290 commits a day too.

## Learning 3: when commits are cheap, attention is the whole economy

The strangest thing about OpenClaw's contribution rules is how hostile they read until you price them in the right currency.

A hard cap of twenty open PRs per author.
Refactor-only PRs refused outright.
Test-only PRs chasing known `main` failures closed automatically.
A demand for evidence, screenshots, and a passing AI review before a human even looks.
Security-owned paths that contributors are told not to touch as "opportunistic cleanup targets."
And my favorite detail, buried in the maintainer recruitment section: applications to become a maintainer are reviewed carefully only if they are "human-only-written."

Every one of these rules is bizarre in the pre-agent world, where producing a plausible pull request took a competent human an afternoon and nobody could open twenty in a day.
Every one of them is obvious in the world OpenClaw actually inhabits, where an agent can generate a hundred plausible-looking PRs overnight and each one still costs a maintainer the same twenty minutes to review.
**When generation became free, the scarce resource in open source stopped being code and became reviewer attention, and OpenClaw's rulebook is best read as a tariff schedule on attention, written by people who learned each rate the hard way.**

The direct-to-main pattern from learning 1 is the same economics viewed from inside the boundary.
An operator steering agents reviews continuously, at the working tree, as the agent produces the work; a pull request would re-review the same diff with less context and more latency.
The gate is not being skipped.
It has moved upstream of the commit, into the operator's supervision loop, which is exactly where I have argued review is heading in [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md).

## Learning 4: transparency about AI, not gatekeeping of AI

The last learning is the policy most projects are still arguing about, sitting fully formed in OpenClaw's contribution guide.

AI-assisted PRs are explicitly welcome, with conditions: mark the PR as AI-assisted, include prompts or session logs when possible, confirm you understand what the code does, run the AI review pass yourself, and clean up after the review bots by resolving the conversations you addressed.
The guide's phrasing is exact: "AI PRs are first-class citizens here. We just want transparency so reviewers know what to look for."

Notice what this policy refuses to do.
It does not ban generated code, which is unenforceable and, for a project whose founder lands 145 agent-written commits a day, absurd.
It does not pretend generated code is indistinguishable from human code, which would forfeit the one signal reviewers most need.
It prices the externality instead: if your contribution was generated, you owe the reviewer provenance, evidence, and your own confirmation of understanding, because those are precisely the costs that generated code otherwise transfers onto the maintainer.
The "human-only-written" requirement for maintainer applications is the same principle at a different gate: the project happily accepts machine-written code, but the judgment it is recruiting for cannot be delegated to the machine, so the application is the one artifact where AI assistance defeats the purpose.

This is the most copyable thing in the repository.
Most projects will never have OpenClaw's commit volume, but every project is about to face its ratio of generated supply to human review capacity, and "first-class, but disclosed, with evidence" is the most coherent answer I have seen deployed at scale.

## What I take away

I started with a story about two personalities and ended with a story about one economy.
Peter committing straight to `main` and Vincent mixing in pull requests are not two attitudes toward discipline; they are two positions in a system that spends its scarcest resource, maintainer attention, only where trust has not already earned the work a cheaper path.
The roles I guessed at are real, but they show up in what the commits do, not in how they land.

The checks I would run on any project after this exercise, my own included: look at the prefix distribution per top contributor to find the builders and the consolidators, and worry if one of the two is missing.
Ask where the trust boundary actually sits, who commits without review and who cannot, and whether that boundary is written down anywhere or merely enacted.
And read the contribution rules as a ledger of attention costs: every harsh rule should trace back to a class of work that once drained review time without paying for it, and any rule that does not is friction with no revenue.

Also, the meta-lesson, since it is the one this article performed on itself: the commit log rewards suspicion of your first reading.
My scrolling-level impression was directionally right and mechanically wrong, and only measurement could tell me which parts were which.
Impressions about other people's process are cheap to form and expensive to hold when wrong; `git log` is sitting right there.

## See also

- [Developer Trust Profiles](../developer-trust-profiles/index.md) - the argument that review scrutiny should scale with the author's earned track record, which OpenClaw implements at the level of human process rather than automated review
- [Rethinking Code Review in the Age of LLMs](../rethinking-code-review-in-the-age-of-llms/index.md) - why the review gate migrates upstream into the operator's supervision loop when an agent produces the code, the dynamic behind trusted maintainers committing straight to main
- [The Merge Gate](../the-merge-gate/index.md) - gating on the blast radius and provenance of a change rather than uniformly on its existence, the principle behind OpenClaw's asymmetric process
- [The Pull Request Queue Outgrew You](../triaging-open-source-pull-requests/index.md) - the maintainer-side triage layer for the flood of generated pull requests that OpenClaw's rulebook is designed to survive
- [Software Engineering Teams in the Age of AI](../software-engineering-teams-in-the-age-of-ai/index.md) - distinguishing load-bearing friction from waste, the lens under which OpenClaw's harsh contributor rules are the former

## References

- [OpenClaw on GitHub](https://github.com/openclaw/openclaw) - the repository whose git history all measurements in this article come from, as cloned on 2026-07-06
- [OpenClaw CONTRIBUTING.md](https://github.com/openclaw/openclaw/blob/main/CONTRIBUTING.md) - the maintainer list, PR limits, evidence requirements, and AI-disclosure policy quoted throughout
- [OpenClaw VISION.md](https://github.com/openclaw/openclaw/blob/main/VISION.md) - the project's stated priorities and contribution rules, including the one-PR-one-topic and 5,000-line-review rules
- [Wikipedia, "Benevolent dictator for life"](https://en.wikipedia.org/wiki/Benevolent_dictator_for_life) - the governance role OpenClaw names explicitly in its maintainer list
