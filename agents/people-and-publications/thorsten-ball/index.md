---
title: Thorsten Ball
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, developer, coding-agents]
readability: 3
audience_notes: >
  Engineers deciding how seriously to take agentic development who want a working practitioner's written record of it.
  Assumes you know what a coding agent harness is; familiarity with interpreters and compilers helps for the books.
---

Thorsten Ball is the co-founder and co-creator of Amp and the author of the self-published Monkey interpreter and compiler books, writing through the weekly Register Spill newsletter and ampcode.com.

**He is the rare harness builder whose public record spans a decade of systems writing, which makes him the best first-person source on what professional development inside an agent actually feels like, as long as you remember every Amp word is also Amp marketing.**

## What it is

A German programmer, now co-founder of Amp Frontier Corporation after Amp spun out of Sourcegraph in December 2025, with earlier stints at Zed and two runs at Sourcegraph.
He self-published Writing An Interpreter In Go (2016) and its sequel Writing A Compiler In Go, sold direct as ebooks ($29 each, $50 bundled) plus Amazon paperbacks, and they remain the standard build-it-yourself path into language internals.
Since April 2023 he has written Register Spill, a Substack newsletter of engineering observations and link digests, over 9,000 subscribers as of 2026-09-24.
On the Amp side he publishes docs, news posts, and a 26-minute working-day screencast that shows his actual threads, orbs, and production rollouts.

## Status

Active on both fronts as of 2026-09-24.
Register Spill is near-weekly: the homepage lists issues 91 through 100 between July 11 and September 20, 2026, the centenary issue being "Joy & Curiosity #100" on September 20.
Amp ships visibly: news items through September 22, 2026 ("One Runner, Many Worktrees"), a Free Agent tier (September 13) making Amp free when you bring your own compute and model subscriptions, and his own screencast embedded front and center on the product homepage.
The spinout announcement he co-signed describes Amp as profitable; the Hacker News thread on it drew 90 points and the pricing pushback noted below.
The books are stable but frozen at their May 2020 editions (v1.7 and v1.2), so they teach the Go of that era.

## Strengths

- The screencast and "How I use Amp" are the most concrete first-person records available of a professional developer running a real codebase through an agent all day, from canary checks to closing bug reports by email.
- His books are the canonical on-ramp to understanding what an agent is actually manipulating, and they are still the books practitioners recommend for opening up the machinery under code.
- He writes in public about the product in his hands: the docs, the video, and the news posts all document his own usage rather than abstract claims.
- Long-formed prose craft, validated by a decade of self-publishing and blurbs from Steve Yegge and Mitchell Hashimoto on the book sites.

## Cautions

- Amp-related writing is inseparable from selling Amp; on the spinout thread the recurring criticism was price ("expensive, like running Opus the whole time"), with one commenter summing up the product as having no moat because "it's all prompts".
- Register Spill is mostly a Joy & Curiosity digest of links and short observations, not deep technical essays, so the newsletter is a signal feed rather than a teaching venue.
- The teaching depth now lives in books frozen in 2020, so nothing in his current record systematically teaches the new agentic material.
- The Free Agent pitch shifts costs onto subscriptions and compute you may not hold, so "free" depends on your existing stack.

## Compared to

- [Steve Yegge](../steve-yegge/index.md): the Amp orbit's evangelist versus its practitioner; Yegge declares the future in essays, Ball shows you his ordinary Tuesday inside the tool.
- [Simon Willison](../simon-willison/index.md): Willison covers the whole landscape daily from the outside, Ball covers one product from inside; read both if you want breadth and depth respectively.
- [Armin Ronacher](../armin-ronacher/index.md): the peer builder-blogger; Ronacher for architecture essays in progress, Ball for the lived-in daily practice and the systems-programming foundations.

## Bottom line

**Recommended for engineers who want to watch a working developer run production software through an agent, and for anyone who learns by building what the books build.**
Not for readers who want vendor-neutral tool comparisons, budget harness options, or a newsletter of deep technical essays.

## Top 5 recommended reading

- [Writing An Interpreter In Go](https://interpreterbook.com) - the build-it-yourself path into what an agent is actually manipulating when it edits code.
- [Writing A Compiler In Go](https://compilerbook.com) - the sequel that continues from interpreter to bytecode compiler and virtual machine.
- [Working Day to Day in Amp](https://ampcode.com/docs/using-amp/a-day-in-amp) - his 26-minute screencast of a real working day running production software through agents.
- [Amp Frontier Corporation](https://ampcode.com/news/amp-inc) - the spinout announcement he co-signed, with the profitability claim that set the terms of coverage.
- [Register Spill](https://registerspill.thorstenball.com) - his weekly newsletter of engineering observations, the ongoing signal feed between the books and the product.

## Changes

- 2026-09-24 - Created.
- 2026-09-24 - Added the Top 5 recommended reading section.

## See also

- [Amp](../../harnesses/amp/index.md) - the product he co-founded, tracked in detail in the Harnesses category
- [Steve Yegge](../steve-yegge/index.md) - the other prominent voice from the Amp story, in essay mode rather than screencast mode
- [Simon Willison](../simon-willison/index.md) - the daily external chronicler of the same agentic landscape
- [Agentic Coding Tools Landscape](../../agentic-coding-tools-landscape/index.md) - where Amp sits in the harness layer his work shapes

## References

- https://thorstenball.com - his bio: Amp co-founder, Zed and Sourcegraph history, books, and newsletter
- https://thorstenball.com/register-spill - the newsletter's own index page: weekly since April 2023, issues through #100 on 2026-09-20
- https://registerspill.thorstenball.com - the canonical Substack home, over 9,000 subscribers as of 2026-09-24
- https://ampcode.com - the Amp homepage: his working-day screencast, Orbs, and news through 2026-09-22
- https://ampcode.com/news/amp-inc - the spinout announcement with the co-founder list including him, and the profitability claim
- https://interpreterbook.com - Writing An Interpreter In Go: pricing, current version 1.7 (May 2020), and testimonials
- https://compilerbook.com - Writing A Compiler In Go: pricing, current version 1.2 (May 2020)
- https://github.com/mrnugget - his GitHub profile as of 2026-09-24: book links, @ampcode affiliation, 3.3k followers
- https://hn.algolia.com/api/v1/items/46124649 - the Hacker News discussion of the spinout with the pricing and moat criticism
