---

title: "Global Sessions: A Git Model for LLM Agent Context"
created: 2026-09-02
type: post
status: draft
tags: [llm, ai-agents, sessions, collaboration, git, distributed-systems, software-engineering, partially-ai-generated, llm=glm-5.3-flash]
readability: 3
audience_notes: >
  Assumes the reader regularly works with LLM coding agents (Claude Code, opencode, or similar) and knows git well enough that clone, push, pull, branch, and merge need no explanation. CRDTs and event sourcing are each explained in a sentence, so no distributed-systems background is assumed.
agent_sessions:
  - ses_f9ed7d01cffe6HXMNjm614YBFs
---

An LLM session is the most valuable working state in software development, and it is also the least portable state we have.
Start a conversation with an agent in a cloud sandbox, iterate all morning, close the lid, and the context stays stranded on that machine.
Coming back means pasting a summary into a fresh session and paying the same exploration cost twice.
Handing the work to a colleague means the same thing, with worse fidelity.
**The session, not the repository, is now where working state accumulates, and it deserves what code got twenty years ago: distribution, versioning, portability, and merge.**
I want sessions that run anywhere and can be continued anywhere, by me tomorrow on another machine, or by a colleague next week, or by two of us at once.
I call the idea a global session, and the design already exists.
It is git, applied to conversations instead of files.

## The Unit of Work Moved

Before git, collaboration went through a central server or through emailed patches.
You committed to a repository you did not own, branching was expensive, and working offline meant diverging on your own and hoping the merge back was survivable.
[Git](https://git-scm.com/about/distributed) changed the unit from a checkout of a central server to a distributed object graph that anyone can clone, push, pull, branch, and merge from anywhere.
Multi-machine and multi-person work stopped being a discipline and became a non-event.

Agents moved the unit of work again.
The expensive part of agentic coding is no longer producing the diff, it is everything that produces the diff: the exploration of an unfamiliar module, the failed hypotheses, the conventions you and the agent agreed on, the reasons the obvious approach did not work.
All of that lives in the session, in the message history, the tool results, and the trajectory of decisions.
The code is in git, global and mergeable.
The session is one process on one machine, format-private, dead the moment the process dies.
**We built distribution for the artifact and left it undone for the conversation that creates the artifact.**

## What a Session Actually Is

Making sessions portable starts with knowing what has to travel, and a session is more than a transcript.
I would split it into four parts.

The history is the message log: user turns, assistant turns, tool calls, tool results.
The trajectory is what the history implies: what was tried, what failed, which approach was rejected and why.
The environment is everything the history points at: a checkout pinned at a commit, installed dependencies, a running dev server, a database seeded with test data.
The authority is who the session acts as: credentials, tokens, permissions.

**A session is a history, a trajectory, an environment, and an authority.**
The history carries the trajectory inside it, since a log that records decisions records why they were made.
Portability fails when the environment and the authority stay behind, and that is exactly what happens when you copy a transcript or a summary to another machine.
The imported session remembers the conversation but cannot touch the files, cannot rerun the tests, cannot push a branch.
This is why every handoff today degrades into a human writing a summary for the next human or the next session, and why every handoff pays a cold-start tax.

## Sessions as Artifacts

The fix is to make the session a versioned artifact with an open format, then give it git's verbs.

The format is an event-sourced, append-only log of turns and tool calls, plus a checkpoint tree.
Checkpoints matter because replaying a raw history is slow and expensive: a week-old session can hold hundreds of thousands of tokens of tool output nobody needs verbatim.
Periodically the harness compacts the log into a checkpoint, a summary the next model can pick up from, and over time a session becomes a tree of checkpoints rather than a tape recording.
Rehydration loads the latest checkpoint and continues, the same way a git checkout gives you the tip and leaves the history there when you need to inspect it.

Alongside the log sits an environment manifest: the pinned commit, a [devcontainer](https://containers.dev/) or Nix specification, and the services the session expects.
The manifest is what makes the environment half portable, because a machine that has never seen this session can rebuild its world from the spec instead of guessing.

Then the verbs.
`session clone` rehydrates a session anywhere: checkout the pinned commit, build the environment from the manifest, load the checkpoint, continue.
`session push` and `session pull` sync changes against a session remote, a server holding session state addressable from anywhere the way origin holds branches, which is a natural fit for stateful, addressable server objects like [Cloudflare Durable Objects](https://developers.cloudflare.com/durable-objects/).
`session fork` splits a session at any checkpoint so two approaches can be tried from identical context.

None of this is speculative.
Claude Code already persists sessions and [resumes them with `--continue` and `--resume`](https://code.claude.com/docs/en/common-workflows), but only on the same machine and in a private format.
[opencode](https://opencode.ai/docs/share/) already lets you share a session to a link and fork one.
The pieces exist and none of them assemble into an open, portable whole.
**Checkpoint, manifest, clone, push, fork: every component is engineering that already exists somewhere, and what is missing is the openness, not the machinery.**

## Two People, One Context

Relay is the easy case: I push, my colleague clones, and the session continues on another machine in front of another person, the same move [tmate](https://github.com/tmate-io/tmate) offered for terminals years before agents existed.
The interesting case is concurrency, two people working in the same context at the same time, because that is where the git model earns its keep.

There are two known ways to share live state.
Collaborative documents use [CRDTs](https://automerge.org/), data structures that merge concurrent edits character by character so every replica converges.
That model fits keystrokes.
Agent work is not keystrokes: an agent turn is a chunky, coherent step that reads five files, edits three, and runs the tests.
Merging at the character level would interleave two agents mid-thought, and the interleaved mess would be worse than either thread alone.
**Sessions want git's model, not the shared document's: branch at checkpoints, diverge, and merge at turn boundaries.**

So two people, or a person and an agent, clone the same session, each runs it in their own worktree and environment, the histories diverge, and the sessions merge.
The file half of that merge is the problem git already solves.
The context half is new, and it has an obvious merge driver: the model itself.
A diff algorithm cannot reconcile two divergent conversations, because the conflict is semantic, two narratives that both claim to continue one history.
An LLM can read both branches and produce a merged history with the contradictions surfaced, the way a good tech lead reconciles two engineers who investigated the same bug from opposite ends.
The merged session is a commit like any other, and both people review it before it lands.
**For context, the merge driver cannot be an algorithm that compares lines, it has to be a reader that understands intent, and a reader is precisely what the session already contains.**

## The Hard Parts

None of this is trivial, and it is worth naming what is hard.

Authority travels with the session, and that is dangerous.
A session that can push to your repository holds credentials that can push to your repository, so a cloneable session is a copyable key.
Session artifacts need scoped, revocable identity, per-session tokens that a handoff grants and a departure revokes, not your personal credentials baked into the history.

Ephemeral state resists the manifest.
The running dev server and the populated test database are either rebuildable from the spec, snapshotted, or declared lost, and the format has to make that declaration explicit instead of silent.

Compaction loses fidelity.
Replaying a full history costs tokens, which is what checkpoints are for, but the compacted tip is a summary and summaries drop details.
The format has to keep the full log retrievable the way git keeps history, even when the working context is the checkpoint tip.

And there is a social change on the other side.
Reviewing a merged session history is a skill nobody has yet, the same way reviewing a patch over email was a skill nobody had before code review tools.

**None of these kill the idea.**
They are the same class of problem git had, signing keys and huge binaries and rebase etiquette, and the same class of problem every technology has solved once working state became shared state.

## What to Do Next

If you build agent tooling, the gap is specific: an open session format, push and pull, an environment manifest, and a session remote.
The harness that gets there first makes every other harness a peripheral.
Every vendor wants to be the hub, so none will build it voluntarily, which is why a protocol like [ACP](https://blog.jetbrains.com/ai/2025/10/jetbrains-zed-open-interoperability-for-ai-coding-agents-in-your-ide/) had to be pushed for editors.

Until then, the poor man's global session is available today and worth doing deliberately.
Externalize the session's state into the repo: a plan file, a decisions file, conventions in AGENTS.md.
Commit early and often.
Hand off a branch plus the files that carry the context, and the next person, or the next session, cold-starts in minutes instead of hours.
It works, and it is manual, and you pay the tax every single time, which is exactly how working with code felt before git.

**Code stopped being local once it became the thing people needed to share.**
Sessions are now that thing.
The next git will not version files.
It will version the conversations that produce them.

## See also

- [The Importance of Context When Interacting with LLMs](../the-importance-of-context-when-interacting-with-llms/index.md) - why the context, not the code, is the half of a session that carries the value
- [Speeding Up LLM Work on a Single Codebase](../speeding-up-llm-work-on-a-single-codebase/index.md) - the worktree patterns parallel sessions use today, and the single-machine ceiling global sessions remove
- [Managing Many Concurrent LLM Agent Sessions](../managing-many-llm-agent-sessions/index.md) - the human supervision problem that handoff-able sessions partially dissolve
- [The Agentic Development Environment Landscape](../the-agentic-development-environment-landscape/index.md) - the tooling layer where session remotes and open formats would have to live

## References

- [Git - About Distributed Version Control](https://git-scm.com/about/distributed) - the model being borrowed: every clone is a full repository and every machine a peer
- [Claude Code: Common workflows](https://code.claude.com/docs/en/common-workflows) - session resume with `--continue` and `--resume`, the same-machine kernel the idea extends
- [opencode docs - Share](https://opencode.ai/docs/share/) - session sharing and forking that exist today inside one harness
- [JetBrains and Zed announce the Agent Client Protocol](https://blog.jetbrains.com/ai/2025/10/jetbrains-zed-open-interoperability-for-ai-coding-agents-in-your-ide/) - precedent for harness interop won by protocol pressure, not vendor goodwill
- [Development containers](https://containers.dev/) - the environment manifest half: rebuildable environments from a spec
- [Automerge](https://automerge.org/) - CRDT-based convergence, the shared-document model argued against for sessions
- [Cloudflare Durable Objects](https://developers.cloudflare.com/durable-objects/) - stateful, addressable server objects, one natural way to build a session remote
- [tmate](https://github.com/tmate-io/tmate) - the pre-AI precedent of terminal sessions you can attach to and share
