---
title: Geoffrey Huntley
created: 2026-09-24
updated: 2026-09-24
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, people, publications, coding-agents, agentic-engineering, automation]
readability: 3
audience_notes: >
  Engineers who keep hearing about the Ralph loop and want to know who created it, what the technique actually is, and how far to trust the claims.
  Assumes you have run a coding agent such as Claude Code or Amp at least once and understand what a context window is.
---

Geoffrey Huntley is an Australian software engineer (near San Francisco per his now page) who writes at ghuntley.com and created the Ralph loop, the while-loop technique for running coding agents autonomously that spread across the community in 2025.

**He is the voice that reduces agentic engineering to its smallest reproducible unit, one bash loop plus prompt discipline, and his value is the concrete method and the deliberate-practice mindset around it; his limit is a maximalist register that packages forecasts as settled facts.**

## What it is

A personal Ghost blog plus workshops, speaking, and media pages, where he publishes essays on coding agents, context engineering, and the economics of AI-generated software.
His signature artifact is Ralph, a technique named after Ralph Wiggum whose purest form is `while :; do cat PROMPT.md | claude-code ; done`, run until a plan file is exhausted.
The technique comes with real engineering rules: one task per loop, specifications as files, subagent fan-out for search and writing, tests and type systems as back pressure, and git loop-backs so each iteration can verify itself.
He frames the same idea at civilization scale with the slogan "AGI = artificial stupidity x infinite persistence", which community threads now quote back as shorthand.

## Status

Active, with a slower recent pulse: the homepage's newest post as of 2026-09-24 dates to July 2026 ("engineer away the slop"), after monthly-or-better output through the prior year, including "everything is a ralph loop" (2026-01-17), "Software development now costs less than the wage of a minimum wage worker" (2026-02-27), and several March-to-June 2026 essays and interviews.
He has been building The Weaving Loom (source on his GitHub), which he calls infrastructure for evolutionary software, and he reports running it under autonomous system-verification loops.
Role: his August 2025 workshop post states he was tech lead for developer productivity at Canva before joining Sourcegraph to work on the Amp agent, and his disclosures page commits to no sponsored content, but the site names no current employer as of 2026-09-24.
Reception is real but Hacker News undercounts it: an Algolia search returns 60 hits for "ghuntley ralph", the Ralph essay was submitted to Hacker News seven times (best: 18 points), derivative tools like ralph-addons appeared as Show HN posts crediting him, and mainstream outlets (VentureBeat, The Register, both linked from his pages) covered the technique.

## Strengths

- He demonstrates techniques on himself at absurd scale, for example Ralph building the CURSED programming language in Rust while the language was absent from training data, which makes the method's ceiling concrete.
- The Ralph essay is a genuinely teachable playbook: context-window budgeting, deterministic stack allocation, tuning failure modes by adding "signs", and wiring static analyzers as back pressure.
- He is candid about the technique's edges: greenfield only, roughly 90 percent completion expected, "you will wake up to a broken codebase", and senior engineers remain mandatory.
- His economics writing extends the same observations into consequences, including the barbell split between model-first and legacy companies.
- The free "how to build a coding agent" workshop demystifies agents into 300 lines of Go, which is the fastest cure for tool-comparison anxiety I know.

## Cautions

- The maximalist claims ("software development is dead", development at $10.42/hour) are forecasts and personal game theory, not measurements, and he says as much only in passing.
- Ralph is deliberately wasteful, burning tokens on repeated context allocation, and he admits it "is deterministically bad in an undeterministic world", so quality depends entirely on the operator's tuning time.
- Prompts are tuned to specific model behaviors; he warns that copying his PROMPT.md verbatim will not reproduce his outcomes.
- Skeptics in the fetched threads dismiss the technique as "just a while loop", and one commenter flagged the essay's serial reposting on Hacker News, so calibrate the hype accordingly.

## Compared to

- [Simon Willison](../simon-willison/index.md): the steady documenter versus the maximalist demonstrator; read Willison when you need verified day-to-day facts, Huntley when you need someone to prove the ceiling is higher than your process assumes.
- [Steve Yegge](../steve-yegge/index.md): fellow maximalist and builder of the Gas Town orchestrator that Huntley explicitly benchmarks himself against; Yegge scales horizontally across many agents, Huntley deliberately stays monolithic, one loop in one repo.
- [Dex Horthy](../dex-horthy/index.md): both treat the context window as the scarce resource; Horthy gives you a principled framework for designing around it, Huntley gives you a one-line loop plus hard-won tuning folklore.

## Bottom line

**Recommended for engineers who want to push autonomous greenfield generation past the fear stage and learn loop, back pressure, and tuning as first-class skills.**
Not for teams seeking a vetted brownfield process, and not for readers who cannot separate a practitioner's marketing register from his technique.

## Top 5 recommended reading

- [Ralph Wiggum as a "software engineer"](https://ghuntley.com/ralph/) - the source essay for the technique, including the prompt stacks, back pressure rules, and his own greenfield-only caveat.
- [everything is a ralph loop](https://ghuntley.com/loop/) - the 2026-01 follow-up that turns Ralph from a trick into a general mindset and introduces The Weaving Loom.
- [how to build a coding agent: free workshop](https://ghuntley.com/agent/) - the demystification piece: an agent is 300 lines of code in a loop, with his Canva-to-Sourcegraph/Amp history included.
- [Software development now costs less than the wage of a minimum wage worker](https://ghuntley.com/real/) - his economic thesis and the clearest statement of the barbell-disruption argument.
- [now](https://ghuntley.com/now/) - his now page, the fastest way to see what he is building and where he is based this month.

## Changes

- 2026-09-24 - Created.

## See also

- [Simon Willison](../simon-willison/index.md) - the counterweight chronicler who tests and documents what Huntley demonstrates at scale
- [Steve Yegge](../steve-yegge/index.md) - the other maximalist, whose Gas Town orchestration thesis Huntley answers with a monolithic loop
- [Claude Code](../../harnesses/claude-code/index.md) - the harness the canonical Ralph one-liner pipes PROMPT.md into
- [Amp](../../harnesses/amp/index.md) - the Sourcegraph agent he helped build and used for the publicized $297 contract run
- [The software factory](../../software-factory/_index.md) - the category his loom experiments push toward, five tools that own the loop end to end

## References

- https://ghuntley.com/ralph/ - the Ralph technique essay: the bash loop, prompt discipline, CURSED, and his own usage limits
- https://ghuntley.com/loop/ - the 2026-01 mindset essay and The Weaving Loom announcement
- https://ghuntley.com/agent/ - the free workshop post grounding his model taxonomy and his Sourcegraph/Amp role statement
- https://ghuntley.com/real/ - the economics essay grounding the minimum-wage and barbell-split claims
- https://ghuntley.com/ - the homepage grounding posting cadence through July 2026
- https://ghuntley.com/now/ - the now page grounding location and current focus
- https://ghuntley.com/disclosures/ - his no-sponsored-content commitment
- https://hn.algolia.com/api/v1/search?query=ghuntley%20ralph&hitsPerPage=8 - third-party footprint: 60 hits, derivative tooling, and the "artificial stupidity x infinite persistence" shorthand in 2026 threads
- https://hn.algolia.com/api/v1/items/46466538 - thread evidence including the serial-repost criticism of the Ralph essay
