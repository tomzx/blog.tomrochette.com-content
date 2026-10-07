---
title: Lars Faye
created: 2026-10-07
updated: 2026-10-07
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, skill-formation, debugging, skepticism]
readability: 3
audience_notes: >
  Engineers and leads worried that agent-first workflows are eroding the skills their use depends on, who want the case for friction argued with cited studies.
  Assumes you already use coding agents and have felt the pull of delegating work you do not fully understand.
---

Lars Faye is a developer and studio owner of more than twenty years whose 2026 essay "Agentic Coding Is a Trap" became one of the year's most-discussed counter-arguments to agent-first development, and who now sells coaching and a debugging course built on the same thesis.

**He is the category's skill-formation skeptic: where the hands-on voices show what agents can do and the evaluators measure whether output works, he argues the friction agents remove is the friction that builds the expertise their use demands, and his boundary is that he sells the remedy.**

## What it is

A personal essay site (larsfaye.com), a coaching practice, and the Confident Coding debugging course, run by Lars Faye, a developer and agency owner with 20-plus years in the industry (Chee Studio since 2013, per his about page).
The four 2026 essays form one argument arc: delegation as a learnable skill (January), the question as the irreplaceable skill (February), the trap of agentic-first workflows and cognitive debt (April), and why AI coding will prevent expertise from forming at all (July).
The flagship essay's core claims: the "skilled orchestrator paradox", that supervising agents requires the same coding skills agents erode through use; vendor dependence, where a Claude Code outage stalls whole teams; and an inverted priority list where speed of generation displaces understanding and conciseness.
He argues from cited research rather than his own experiments, leaning on Anthropic's 2026 coding-skills study, the ACM novice-programmer study JetBrains highlighted, and the UPenn PNAS learning study, and linking each primary source.

## Status

Active as an essayist and newly a course seller as of 2026-10-07.
The RSS feed shows four essays in 2026, one every six to eight weeks, with the newest "AI Coding will Prevent Expertise" on 2026-07-22 and nothing since (feed last built 2026-09-24).
The flagship essay reached 463 points and 375 comments on Hacker News (2026-05-03, third-party submission), and his post page records podcast coverage by Cal Newport and a read-through by Theo Brown, reach no other new-voice candidate in this run's scan matched.
He is monetizing the thesis: coaching for agencies and individuals, billed hourly or on retainer, plus the Confident Coding course, a $199 debugging course on a Q4 2026 waitlist with a $100 early-bird price.
One stability note: the site's /articles index returned a 500 error when fetched on 2026-10-07, so the RSS feed is the reliable catalog surface.

## Strengths

- **The supervision-paradox framing is the sharpest one-paragraph case against agent-first defaults I have found, quoting Anthropic's own admission that effectively supervising Claude requires the coding skills that may atrophy from overuse.**
- The follow-up names the demographic problem precisely: novices are told to wield tools that demand expert judgment while being handed a shortcut around the friction that builds it, the "expert novice".
- The prescription is specific and falsifiable: never generate more than you can review in a sitting, stay hands-on for 20 to 100 percent of implementation depending on the task, and use models as Socratic partners rather than answer machines.
- He links the studies behind each claim, so a reader can audit how far the evidence actually reaches instead of trusting the summary.

## Cautions

- The remedy is his product: the essays argue for exactly the debugging discipline his coaching and $199 course sell, so read the thesis as partly marketing.
- The evidence is curated secondhand: he selects studies that support the arc and runs no evaluations of his own, so the citations deserve the same scrutiny he asks of agent output.
- Cadence is thin: four essays in 2026 with nothing since July 22, and I found no talks, interviews, or community threads worth listing, so there is little record against which to test the thesis over time.
- No standalone critical rebuttal has surfaced yet; the 375-comment Hacker News thread is the only public stress test, and I sampled it through the API rather than reading it whole.

## Pricing

Free to read on the essay site.
The business layer is paid: coaching billed hourly or on retainer, and the Confident Coding course listed at $199 with a $100 early-bird waitlist price ahead of a Q4 2026 launch.

## Price history

| Date | Plan | Change | Source |
| ---- | ---- | ------ | ------ |
| 2026-10-07 | Confident Coding course | Baseline: essays and RSS free; course listed at $199 with a $100 early-bird waitlist price before the Q4 2026 launch. | https://confident-coding.com/ |

## Compared to

- [Simon Willison](../simon-willison/index.md): Willison's cognitive-debt confession is the first-person data point Faye's argument leans on; Willison documents his own atrophy, Faye generalizes it into a warning about the pipeline.
- [Addy Osmani](../addy-osmani/index.md): both write the don't-outsource-your-learning essay, Osmani from inside frontier labs at enterprise scale, Faye from a twenty-year agency practice aimed at individuals and agencies.
- [Kent Beck](../kent-beck/index.md): Faye quotes Beck's "coding's actually a great way to cement understanding" and extends the augmented-coding position into the expertise-pipeline argument Beck leaves implicit.

## Bottom line

**Recommended for engineers and leads deciding how much of their workflow to hand to agents, and for anyone designing onboarding or mentoring around coding agents.**
Not for tool selection, release tracking, or anyone looking for the case for agents; this is the case for keeping your hands on the keyboard.

## Top 5 recommended reading

- [Agentic Coding is a Trap](https://larsfaye.com/articles/agentic-coding-is-a-trap) - the flagship: cognitive debt, the supervision paradox, and the inverted priority list, with the studies linked.
- [AI Coding will Prevent Expertise](https://larsfaye.com/articles/ai-coding-will-prevent-expertise) - the follow-up that names the expert novice and the inverted-learning problem with study evidence.
- [Your Indispensable Value in the AI Era](https://larsfaye.com/articles/the-question-is-the-work) - the shortest statement of his positive thesis: answers are cheap now, the question is the work.
- [Everyone Can Delegate Now](https://larsfaye.com/articles/everyone-can-delegate-now-to-ai) - the arc's starting point, delegation as a learnable skill with its own failure modes.
- [Confident Coding](https://confident-coding.com/) - the course site, where the thesis becomes a product and the four modules show what he thinks the skill actually is.

(The record is thin beyond four essays and a course: I found no talks or interviews worth listing, so the fifth slot leans on his course rather than padding.)

## Changes

- 2026-10-07 - Created after this run's new-voice scan surfaced him through the Hacker News record; he fills the category's skill-formation skeptic slot.

## See also

- [Simon Willison](../simon-willison/index.md) - the first-person cognitive-debt account his argument cites
- [Kent Beck](../kent-beck/index.md) - the augmented-coding position Faye extends into the expertise-pipeline argument
- [Addy Osmani](../addy-osmani/index.md) - the enterprise-hands-on version of the don't-outsource-the-learning warning
- [Claude Code](../../harnesses/claude-code/index.md) - the agent-first workflow his essays argue against defaulting to

## References

- https://larsfaye.com/articles/agentic-coding-is-a-trap - the flagship essay (April 2026): the trap thesis, the supervision paradox, and the post-publish coverage record
- https://larsfaye.com/articles/ai-coding-will-prevent-expertise - the July 2026 follow-up: the expert novice, inverted learning, and the cited studies
- https://larsfaye.com/articles/everyone-can-delegate-now-to-ai - the January 2026 essay on delegation as a skill with its own failure modes
- https://larsfaye.com/articles/the-question-is-the-work - the February 2026 essay on the question as the irreplaceable skill
- https://larsfaye.com/rss.xml - the feed grounding the four-essay 2026 catalog and the quiet stretch since July 22 (last built 2026-09-24)
- https://larsfaye.com/about - twenty-plus years in the industry, Chee Studio, Wallabie, and Confident Coding
- https://larsfaye.com/coaching - the paid coaching offer built around the thesis
- https://confident-coding.com/ - the $199 debugging course on a Q4 2026 waitlist, grounding the commercial model and its four modules
- https://hn.algolia.com/api/v1/items/48002442 - the Hacker News record of the flagship essay: 463 points, 375 comments, 2026-05-03, third-party submission
