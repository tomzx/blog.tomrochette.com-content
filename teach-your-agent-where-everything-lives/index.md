---

title: "Teach Your Agent Where Everything Lives"
created: 2026-09-02
type: post
status: draft
tags: [ai, llm, agents, context-engineering, developer-tools, fully-ai-generated, llm=glm-5.3-flash]
readability: 3
audience_notes: >
  Assumes the reader is a software engineer who already runs an LLM coding agent inside a single repository and wants the same agent to answer questions and ship changes across their whole workspace. No introduction to what an LLM agent is.
agent_sessions:
  - ses_f9eb508dcffekD6XfZ9dCB5QZG
---

Every engineer accumulates questions whose answers exist somewhere in the company but not in any one place.
Why does the staging deploy fail, who decided to deprecate the v1 API, where is the pagination bug tracked, what did that Slack thread conclude about rate limits.
The answer exists.
The answer is scattered across Slack threads, GitHub issues, commits, design docs, and a dozen repositories.
**The difference between an agent that finds those answers and an agent that makes things up is not the model, it is what the agent can reach and whether it knows where to look.**

I run my agent this way.
I ask it to figure something out and it goes and looks: in the code, in the issues, in the pull requests, in the Slack cache, in the docs directory.
When it cannot find the answer, it tells me where the answer most likely lives and who to ask.
The same setup lets it ship changes across multiple repositories in the right order, because the map includes how the repositories relate.
Here is how the whole thing works.

## Access first, everything else second

An agent can only search places it can actually reach.
This sounds obvious and it is the step everyone skips.
People buy a smarter model, keep the agent locked inside one repository, and then wonder why it answers "I don't know" or, worse, invents something plausible.

Every place your answers live needs two things: a way in, and a pointer.

The way in is tooling.
For GitHub, the [gh CLI](https://cli.github.com) or a GitHub MCP server lets the agent search issues, read pull requests, and browse code.
MCP, the [Model Context Protocol](https://modelcontextprotocol.io), is the standard way to hand tools like these to an agent, and the reference [servers collection](https://github.com/modelcontextprotocol/servers) includes GitHub and Slack.
For Slack, either such a server or a local cache you can grep, which is what I prefer (I wrote about [slack-cached](../slack-cached/index.md), since renamed slackx).
For repositories, the single most valuable move costs nothing: check out every repository you touch into one parent directory, so one agent session sees all of them.
For documents, keep design docs, runbooks, and decision records in a directory the agent's file tools can already read.

The pointer is a line in your agent instructions file ([AGENTS.md](https://agents.md)) saying the source exists, what it contains, and when to use it.
**A source the agent can reach but does not know about is invisible, and a source the agent knows about but cannot reach is a tease.**

## The map: where everything lives

The instructions file is usually sold as a place for conventions: how to run the tests, which linter to obey.
That is half of it.
The other half is a map of your workspace: which repositories exist, what each one does, where the docs live, which Slack channels hold which decisions, who owns what.

Mine says things like: the platform repo contains the API and deploys first, the web repo consumes the API and deploys after it, billing questions end up in the billing channel, decision records live in docs/decisions with one file per decision.
None of this is secret knowledge.
All of it normally lives in the heads of people who have been at the company for three years.
**Writing the map down is the whole trick, because routing questions is knowledge, and knowledge that lives only in heads does not transfer to agents.**

Keep the map made of pointers, not contents.
"Decisions live in docs/decisions" beats pasting every decision into the instructions.
Anthropic's [context engineering guidance](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) calls this just-in-time retrieval and grounds it in the attention budget: every token spent on material the agent could look up when needed is attention taken away from the task at hand.
Dumping everything in also runs into the [lost-in-the-middle problem](https://arxiv.org/abs/2307.03172), where models recall the start and end of a long context far better than the middle.

Put the map in version control.
Update it by pull request, ideally pull requests opened by the agent itself.
When the agent discovers the map is wrong, a repository moved, a channel renamed, the fix is a one-line PR to the map, and the next session benefits.
I made this argument for the whole repository in [the self-evolving repository](../the-self-evolving-repository/index.md), and the map is the highest-value file to apply it to.

## Teach it to route, not to memorize

People expect the agent to know the answer.
The useful expectation is that the agent knows where answers live, and that it goes and checks.
The behavioral contract I use has four rules.

Search the most likely place first, then broaden outward: local code, then GitHub issues and pull requests, then Slack, then docs.
Cite where every claim came from, with a link or a file path.
Say "I could not find it" early instead of guessing late.
When there is no written answer, name the most likely place to ask: the channel, the repository, the owner listed in the map.

That last rule does more for me than the rest combined.
"I could not find an answer, the refund window behavior was last discussed in the payments channel, and the most recent relevant PR is #482, I would ask there" is a great answer.
It converts a dead end into the next concrete step.
**The deliverable is not the answer, the deliverable is the trail: what was checked, what was found, and where to go next.**

## Cross-repo changes need a deployment graph

The second job is making changes across repositories.
An agent will happily edit five repositories in five wrong orders unless it knows how they relate.
The fix is to put the relationships in the map, next to the list of repositories.

For each repository I record what it depends on and where it sits in the deploy order.
A shared library sits at the bottom and deploys first.
The services that consume it come next.
The web frontend comes last.
Now "rename this setting and use the new name in the dashboard" is a plan the agent can execute: open a PR against the library, open PRs against the consumers, order the merges, deploy in sequence, and check CI at each step.
The agent does not need to discover the dependency graph by reading package files and hoping.
The graph was written down.

This is where the worst failure mode lives, so be blunt about it.
**A wrong map produces confidently wrong work, because the agent trusts written instructions more than its own uncertain inferences.**
Keep the deploy order short and verify it against reality when it matters: the agent can read CI statuses and deployment logs, so let it confirm that what the map claims matches what happened.
Automated deploys are the complementary piece (I wrote about this as [zero-touch engineering](../zero-touch-engineering/index.md)): they turn "deploy in this order" from something you do by hand into something the agent can actually execute.

## Failure modes

The stale map is the main risk.
**A map is a claim about the world, claims age, and the agent will not notice on its own.**
Keep it short enough to review in a minute, and let the agent propose corrections as pull requests.

Credentials are the second risk.
A question-answering agent should hold read-only tokens wherever possible.
If the Slack integration can read channels you are not supposed to see, the agent will eventually read them, so scope the token to what you are allowed to see.
Save write access and production secrets for the sessions that specifically need them, and say in the map which those are.

The unverified citation is the third.
An agent under pressure to answer will produce a sentence that looks like an answer.
Requiring a source for every claim changes the failure from a confident hallucination to a visible "no source found", which is exactly what you want.
This is the corpus point I keep coming back to, that [context quality dominates model choice](../the-importance-of-context-when-interacting-with-llms/index.md): the same model with access and a map outperforms a better model with neither.

An agent wired this way stops being a code autocomplete with a chat window.
It becomes the first place I take any question about the work, because it either comes back with an answer and a trail, or with the next best place to look.
And when the work spans five repositories, the map is what turns five coordinated changes from a project into an instruction.

## What to Do Next

- Check out the repositories you touch into one parent directory so one agent session sees all of them.
- Write the map into your AGENTS.md: repositories and what they do, docs locations, Slack channels per domain, owners, deploy order.
- Give the agent a way into GitHub (the gh CLI) and Slack (a cache or MCP server), read-only first.
- Add the routing contract: search order, cite every claim, admit gaps, and name where to ask next.
- Test it on a question whose answer you already know, then on one you know is written nowhere, and check that the second produces "ask in this channel" instead of an invention.

## See also

- [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md) - the principle underneath the whole setup, that context quality determines output quality
- [The Self-Evolving Repository](../the-self-evolving-repository/index.md) - letting agents maintain their own instructions, which is how the map stays current
- [Scaling Yourself Horizontally](../scaling-yourself-horizontally/index.md) - why an agent that can find things on its own is one you can actually delegate to
- [slack-cached](../slack-cached/index.md) - one concrete way to give an agent read access to Slack
- [Zero Touch Engineering](../zero-touch-engineering/index.md) - automated deploys that make an agent-generated deploy order executable
- [Issues Are Free Now: Send the Implementation, Not the Idea](../send-implementation-not-issue/index.md) - what the agent can produce once it can reach everything

## References

- [AGENTS.md](https://agents.md) - the convention for per-repository agent instructions where the map lives
- [Model Context Protocol](https://modelcontextprotocol.io) - the standard for exposing tools and data sources to agents
- [Model Context Protocol servers](https://github.com/modelcontextprotocol/servers) - reference servers for GitHub, Slack, and other sources
- [gh CLI](https://cli.github.com) - the read path into GitHub for issues, pull requests, and code
- [Anthropic, "Effective Context Engineering for AI Agents"](https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents) - just-in-time retrieval and attention budgets, why pointers beat dumps
- [Liu et al., "Lost in the Middle: How Language Models Use Long Contexts"](https://arxiv.org/abs/2307.03172) - positional recall bias, why dumping everything into the window hurts
- [Claude Code memory documentation](https://code.claude.com/docs/en/memory) - how instruction files load into agent sessions in practice
