---
title: "Teach Your Agent Skills to Use Tools That Render"
created: 2026-08-14
type: post
status: finished
tags: [ai, llm, agent-skills, tools, mermaid, sdlc, visualization, software-engineering, fully-ai-generated, llm=glm-5.2, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader already writes or uses agent skills (a SKILL.md or similar) inside a coding agent like OpenCode, Cursor, or Claude Code, and has hit the wall of verifying long prose output. No introduction to LLMs or to what a skill is.
---

The cheapest upgrade I have made to an agent skill was not a better prompt or a bigger model.
It was teaching the skill to emit a [mermaid](https://mermaid.js.org/) diagram instead of a paragraph.
Once the skill could draw, I could check its work by looking instead of reading, and looking is the one verification that stays fast when the prose has buried you.

**The highest-leverage thing you can do to an agent skill is wire it to a small tool that renders, because a rendered artifact moves verification from reading to looking, and looking is cheap, fast, and hard to fool.**

## Why prose-only skills plateau

A skill that only writes prose hands you prose to verify.
Prose asks you to read, and reading is exactly the bottleneck that working with agents moved into the foreground: the scarce, serial, finite attention you have left once generation became free ([Attention Engineering](../attention-engineering/index.md)).

The trap is that prose feels productive to generate and expensive to check.
The agent writes a fluent paragraph describing the data flow, the spec, or the migration plan, and you skim it and approve it, because reading it carefully would cost more attention than you have.
**A skill that outputs only text is a skill that can only be checked by the slowest checker you own, and the one that tires first, which is you, reading.**

## The pattern: pair the skill with a tool that renders

The fix is to give the skill a tool that turns text into something you can inspect at a glance.
The tool does the deterministic part, the layout, the rendering, the syntax checking, and the skill does the generative part, deciding what to put in the diagram.
The concerns separate cleanly, and the output becomes inspectable in a way prose never is.

Pairing a skill with a renderer is the same move as [Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md), applied to the artifacts a skill produces: stop trying to read, start trying to verify, and pick for each artifact the cheapest checker that catches the failure you care about.
**For a lot of artifacts, the cheapest checker is a picture.**

## Mermaid in the SDLC process

I started adding [mermaid](https://mermaid.js.org/) diagrams to my SDLC skills, and the payoff was immediate.
A plan that used to be three paragraphs of "first we do this, then that, and this component talks to that one" now ships with a sequence diagram.
A spec now ships with a state diagram or a flowchart of the happy path.

The diagrams fail in ways prose hides.
A sequence diagram with a message that has no receiver makes a missing step obvious.
A flowchart with two boxes that both claim to write the same column makes a race condition visible before a line of code exists.
**The wrong diagram is obvious in two seconds; the wrong paragraph is buried in the fourth reading, if it ever surfaces.**

Mermaid is the right tool for a skill for three reasons.
It is text, so the agent generates it directly, the same way it generates any other output.
It renders natively where the work already lives, because GitHub renders ` ```mermaid ` blocks in Markdown and most static site generators do too.
And it diffs cleanly, because the source is text, so a change to the plan shows up in the pull request as a diff you can review instead of a picture you have to compare by eye.

## Text-based tools are the sweet spot for skills

The mermaid case generalizes into a rule I now follow.
**When you pick a tool for a skill to drive, prefer a text-based one, because text is the medium the agent speaks, the medium git tracks, and the medium that renders to the artifact you inspect.**

[DBML](https://dbml.dbdiagram.io/docs/) is the database-schema version of the same idea.
It is a small markup language for tables, columns, and foreign keys, and a few lines of it render to a full entity-relationship diagram on [dbdiagram.io](https://dbdiagram.io/).
A skill that describes a schema now emits DBML, and I see the structure of the data model, the missing relationship, the redundant table, before I have read a single column definition.

The text basis is what makes it fit an agent workflow.
The agent writes DBML the way it writes code, the file lives next to the migration that creates the tables, it reviews and diffs like code, and the rendered diagram is a view on top of it rather than a separate artifact that drifts.
When the schema changes, the DBML changes in the same commit, and the diagram is never stale.

## Where the visual tool fits: on the human side

Preferring text-based tools does not mean GUI tools have no place.
[drawdb](https://drawdb.app/) is the mirror image of DBML: a browser editor where you drag tables and draw relationships by hand, and it exports the SQL for whatever you sketched.

The division of labor that works for me is to let the agent drive the text-based tools and let myself drive the visual ones.
I sketch in drawdb when I am still figuring the model out, when I want to move boxes around and feel my way through the design, and then the SQL/DBML it exports becomes an input the agent works from.
I let the agent drive DBML when the schema is already decided and I want a rendered view of it inside the repository.
**Text-based tools go in the skill, where the agent is fast and generation is cheap; visual tools go in my hands, where exploration is slow and taste is required.**

## How to pick the next tool to wire in

Three tests decide whether a tool is worth wiring into a skill.

The tool must be text-based, or have a text representation the agent can produce.
The whole pattern breaks if the agent cannot generate the source the renderer consumes.

The tool must render to something inspectable, a diagram, a table, a diff, a graph.
If the output is still prose, you have added a dependency and gained no new kind of check.

And the tool must be narrow enough that the skill can use it reliably.
[Mermaid](https://mermaid.js.org/) and [DBML](https://dbml.dbdiagram.io/docs/) win here because they are small languages with a fixed grammar, not sprawling APIs the model has to guess at.
**A tool the model gets wrong half the time is worse than prose, because you spend your attention debugging the tool instead of the idea.**

## What to Do Next

Pick one skill you already run that emits prose and teach it to render.
If it describes a flow, teach it mermaid.
If it describes data, teach it DBML.
If it describes a sequence of messages between components, teach it a sequence diagram.

Then read the next output it produces as a picture instead of a paragraph, and notice where your eye catches in two seconds what your reading would have missed in twenty minutes.
**That gap, between the cost of looking and the cost of reading, is the whole reason to give your skills tools that render.**

## See also

- [My AI Workflow: The Skills Are the Part That Compounds](../my-ai-workflow/index.md) - the case that skills, not models or shells, are the durable asset, and the library where these examples live
- [Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md) - the larger pattern this applies to artifacts: replace one slow reader with many cheap, tireless checkers
- [Attention Engineering](../attention-engineering/index.md) - why reading is the bottleneck a prose-only skill quietly pushes onto you
- [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md) - why a text-based, versioned artifact you can both see beats a transcript as shared context

## References

- [Mermaid](https://mermaid.js.org/) - text-based diagramming that renders in GitHub and most docs, the tool I wired into the SDLC skills
- [DBML syntax](https://dbml.dbdiagram.io/docs/) - a markup language for database schemas that renders to entity-relationship diagrams
- [dbdiagram.io](https://dbdiagram.io/) - the renderer for DBML, where the text turns into a diagram
- [drawdb](https://drawdb.app/) - a browser-based visual ER editor for sketching schemas by hand and exporting SQL
