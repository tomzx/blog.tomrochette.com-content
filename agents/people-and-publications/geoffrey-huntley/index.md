---
title: Geoffrey Huntley
created: 2026-09-24
updated: 2026-10-08
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

Active with the fastest pulse of the window: six essays in the first nine days of October 2026, led by "--help on your CLI is all you need for LLM context until you don't." (2026-10-09, at ghuntley.com/tier/), which sorts developer-tooling companies into an S tier already inside the model weights and an F tier that is not, and tells the F tier to optimize a CLI's --help text, automate measuring whether a model can walk the help verbs, and do ASEO instead of shipping skill packs or MCP servers, before "to Kodak yourself out of business" (2026-10-08), which reads JetBrains's first recorded net loss as proof that domain expertise becomes the blind spot (his own 2025 IDEs-are-dead call made good, with the lesson generalized to labs that believe better models will solve verification), and "the world hasn't figured out yet that you can literally just fix everything with a Nix overlay" (2026-10-07), which argues Nix overlays and NixOS tests as the single source of truth for agent environments, including developing on NixOS with sudo granted to his agents because the system is rollback-safe and a public nix-demo repository that patches force-push out of git for agent sandboxes, following "an application in lisp you grow by talking to it" (2026-10-05), arguing that programming languages will converge on something not yet defined and demonstrating an application grown through conversation with agents rather than assembled, two essays in one day on 2026-10-02, "software doesn't need to be readable anymore. it needs to be explainable." and "the craft has been commoditized, but access has not", the September 2026 recap of his May 2026 AI Engineer Singapore talk ("the eighteen-month recap", posted 2026-09-27), and "engineer away the slop" (July 2026), after monthly-or-better output through the prior year, including "everything is a ralph loop" (2026-01-17) and "Software development now costs less than the wage of a minimum wage worker" (2026-02-27).
The readable essay extends his loop thesis to the artifact itself: a codebase no longer needs to be optimized for humans to read cold, only for a model to explain on demand, with type systems as the verification back pressure that lets cheaper models keep the loop closed.
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
- 2026-09-29 - Newest-post check refreshed: the homepage now leads with "the eighteen-month recap: AI Engineer, Singapore, May 2026" (posted September 2026), after the July 2026 essay noted previously.
- 2026-10-02 - Newest-post check refreshed: two new essays on 2026-10-02 ("software doesn't need to be readable anymore. it needs to be explainable." and "the craft has been commoditized, but access has not") ended the slower pulse; both added to References.
- 2026-10-06 - Newest-post check refreshed again: "an application in lisp you grow by talking to it" (2026-10-05) makes three essays in four days, arguing applications are now grown through conversation with agents rather than assembled; added to Status and References (URL fetched this run).
- 2026-10-08 - Two more essays, making five in October's first eight days: "the world hasn't figured out yet that you can literally just fix everything with a Nix overlay" (2026-10-07, Nix overlays and NixOS tests as agent-environment single source of truth, with the nix-demo repo patching force-push out of git for agents) and "to Kodak yourself out of business" (2026-10-08, JetBrains's first recorded net loss as the domain-blindness lesson); both added to Status and References (URLs fetched this run).

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
- https://ghuntley.com/readable/ - the 2026-10-02 essay arguing artifacts need to be explainable by a model rather than readable by humans, with types as back pressure
- https://ghuntley.com/access/ - the 2026-10-02 essay on the craft being commoditized while access has not
- https://ghuntley.com/lisp/ - the 2026-10-05 essay demonstrating an application in Lisp grown through conversation with agents, and the argument that languages will converge on something not yet defined
- https://ghuntley.com/nix/ - the 2026-10-07 essay on Nix overlays and NixOS tests as the single source of truth for agent environments, with sudo-in-loops and the nix-demo repo
- https://ghuntley.com/kodak/ - the 2026-10-08 essay reading JetBrains's first recorded net loss as the domain-expertise-blindness lesson, generalized to the labs
