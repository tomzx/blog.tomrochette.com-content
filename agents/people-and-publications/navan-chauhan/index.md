---
title: Navan Chauhan
created: 2026-11-14
updated: 2026-11-14
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, software-factory, dark-factory, agentic-loops]
readability: 3
audience_notes: >
  Engineers building factory-style agent loops who want the validation and no-op details from someone inside a working no-human-review team.
  Assumes you have run coding agents in loops and know what a software factory claims to be.
---

Navan Chauhan is a founding member of StrongDM's three-person AI team and a blogger at web.navan.dev whose factory essays, agent-loop writeups, and Hacker News defenses turn the team's no-human-review software factory practice into public, buildable guidance.

**He is the voice from inside the most-cited dark-factory team in the field: the February 2026 StrongDM factory reveal (304 HN points, about 450 comments) is the in-window breakout that named the term's working practice, and his own posts supply the parts vendors skip, the task packets, the validation outside the agent's claims, and the no-op as a first-class outcome.**

## What it is

A personal blog (web.navan.dev, twelve posts in 2026, six of them agent-era, newest "Be More Ambitious" 2026-11-03), a GitHub fleet of 73 public repos, and a founding seat on StrongDM's AI team.
The team (Justin McCarthy, Jay Taylor, and Chauhan, formed July 2025) published "Software Factories and the Agentic Moment" on 2026-02-06, the essay that anchors the field's dark-factory vocabulary: specs and scenarios drive agents, code is neither written nor reviewed by humans, and satisfaction is measured probabilistically against a Digital Twin Universe of behavioral clones of Okta, Jira, Slack, and Google's docs suite.
His own factory essay, "How to Build Your Own Software Factory" (2026-05-06), is the practical companion: define what you manufacture, build the seed, make the no-op case mandatory, validate outside the agent's claims, and treat failure as data for the pipeline.
Around that core he writes agentic-loop economics ("The Unreasonable Effectiveness of Agentic Loops", 2026-03-17), reverse-engineers harness internals ("Peeking Into Claude Code", 2026-02-24, the Bun binary, prompt assembly, and tool schemas), and maps the next interface ("On Computer Use", 2026-08-19, a chief-of-staff agent driving cloud boxes instead of a coding-agent UI).

## Status

Active, with the breakout inside the section's coverage window.
The team's essay hit Hacker News on 2026-02-07 at 304 points with about 450 comments as of 2026-11-14, and Simon Willison's same-day writeup called the demoed system "a glimpse of one potential future of software development".
The blog cadence is a few posts a month, mixed between agent topics and personal projects (Siri shortcuts, self-hosting, Gopher clients), so the factory thread advances in bursts rather than weekly.
He stays in the public argument: an Algolia comment search shows him answering factory threads through 2026-10-16, including the critical "Why Software Factories Fail (or: harness engineering is not enough)" discussion in July 2026.
His GitHub (142 followers as of 2026-11-14) holds the tooling around the writing (Leash, a Cedar-policy sandbox; iGopherBrowser) rather than the factory itself, which stayed proprietary.

## Strengths

- He writes from inside a working no-review factory, not about one, so the failure modes he lists (agents that pass narrowly written tests, humans who cannot stop reviewing) are observed rather than projected.
- The factory essay is the field's best product-free build order: the loop, the task packet, the stopping rules, and the no-op case, none of it behind a vendor's platform.
- The reverse-engineering posts show harness internals firsthand, which pairs the factory argument with the ability to read the tools it runs on.
- He engages critics in public threads and concedes the human-judgment boundary ("human taste decides what to build") instead of defending the manifesto line by line.

## Cautions

- **The team's numbers are self-reported: the "$1,000 of tokens per engineer per day" floor and the satisfaction percentages come from the team's own writeups, and no third party has replicated the Digital Twin Universe results.**
- The open-source footprint is thin where it matters most: strongdm/attractor, the factory's core agent, shipped as three markdown spec files rather than code, so the loop cannot be cloned the way Owain Lewis's or Geoffrey Huntley's can.
- The blog's agent thread is part-time; most of his 2026 posts are non-agent projects, and the strongest factory material is co-authored with McCarthy and Taylor.
- The dark-factory framing invites over-transfer: a three-person team validating against behavioral clones is not a template for a regulated enterprise codebase, and he says so himself ("there is no one-size-fits-all software factory").

## Pricing

Does not apply.
The blog, the team essay, and the thread participation are all free; StrongDM the company sells an infrastructure-access product the factory content does not funnel into, and no paid tier exists on any of his output.

## Compared to

- [Geoffrey Huntley](../geoffrey-huntley/index.md): both reduce agent work to loops, but Huntley works alone at maximum persistence while Chauhan argues the loop's real product is validation, no-ops, and the pipeline fixes failure feeds back into.
- [Addy Osmani](../addy-osmani/index.md): both write multi-agent coordination practice, from opposite trust models, Osmani keeps plan approval and human review as the quality gates, Chauhan's team removed review entirely and moved the guarantee into scenarios.
- [Steve Yegge](../steve-yegge/index.md): Yegge proclaimed the factory era and then shut Gas Town down admitting it never worked for him; Chauhan is the quieter case from a team whose factory was still running a year later.

## Bottom line

**Recommended for engineers building factory-style agent loops who want the validation and no-op details from someone who runs one without human review.**
Not for readers who want daily output, a cloneable reference implementation, or independently verified production numbers.

## Top 5 recommended reading

- [How to Build Your Own Software Factory](https://web.navan.dev/posts/2026-05-06-how-to-build-your-own-software-factory.html) - the practical companion to the team's manifesto: what you are manufacturing, the seed, the task packet, validation outside the agent's claims, and the mandatory no-op case.
- [Software Factories and the Agentic Moment](https://factory.strongdm.ai/) - co-authored with Justin McCarthy and Jay Taylor, the team's manifesto and the in-window breakout: scenarios, satisfaction, and the Digital Twin Universe, with the "code must not be written or reviewed by humans" rules stated plainly.
- [On Computer Use](https://web.navan.dev/posts/2026-08-19-on-computer-use.html) - the chief-of-staff pattern, a control-plane agent driving execution boxes, the clearest statement of where he thinks the coding-agent interface is going.
- [The Unreasonable Effectiveness of Agentic Loops](https://web.navan.dev/posts/2026-03-17-the-unreasonable-effectiveness-of-agentic-loops.html) - the loop-economics essay, tokens in against verified outcomes out.
- [Peeking Into Claude Code](https://web.navan.dev/posts/2026-02-24-peeking-into-claude-code.html) - the reverse-engineering walkthrough of the Bun binary, prompt assembly, and tool schemas, the tool-internals grounding under the factory argument.

## Changes

- 2026-11-14 - Created.

## See also

- [Geoffrey Huntley](../geoffrey-huntley/index.md) - the solo-loop counterpoint to the team-factory account
- [Addy Osmani](../addy-osmani/index.md) - the keep-humans-reviewing trust model his team rejected
- [Steve Yegge](../steve-yegge/index.md) - the loud factory evangelist whose own build failed, the contrast case
- [Super Simple Software Factory](../../software-factory/super-simple-software-factory/index.md) - the cloneable loop his essay describes but did not ship
- [Machinist](../../software-factory/machinist/index.md) - the other build-in-public factory infrastructure, Owain Lewis's

## References

- https://web.navan.dev/posts/ - the blog index: the 2026 post list, cadence, and topic mix
- https://web.navan.dev/posts/2026-05-06-how-to-build-your-own-software-factory.html - his factory essay: build order, task packets, no-op case, failure modes
- https://factory.strongdm.ai/ - the team manifesto (2026-02-06): the Digital Twin Universe, scenarios and satisfaction, the no-human-review rules, and the three-person team roster
- https://simonwillison.net/2026/Feb/7/software-factory/ - the independent coverage naming him and the team, "a glimpse of one potential future"
- https://hn.algolia.com/api/v1/items/46924426 - the 304-point "Software factories and the agentic moment" Hacker News thread (about 450 comments as of 2026-11-14), the in-window breakout
- https://hn.algolia.com/api/v1/search?tags=comment,author_navanchauhan - his public thread participation through 2026-10-16, including the critical "Why Software Factories Fail" discussion
- https://github.com/navanchauhan - GitHub profile: 142 followers and 73 public repos as of 2026-11-14
- https://web.navan.dev/posts/2026-08-19-on-computer-use.html - the computer-use essay grounding the chief-of-staff pattern
- https://web.navan.dev/posts/2026-02-24-peeking-into-claude-code.html - the Claude Code reverse-engineering walkthrough
