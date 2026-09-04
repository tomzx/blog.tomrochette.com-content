---

title: "Six Months with OpenChamber"
created: 2026-08-19
type: post
status: finished
tags: [ai, llm, ai-agents, opencode, openchamber, tools, partially-ai-generated, llm=glm-5.3]
readability: 3
audience_notes: >
  Assumes the reader already runs a coding agent such as OpenCode or Claude Code and knows what a git worktree is. No prior OpenChamber familiarity required.
agent_sessions:
  - ses_fe7a583bdffexEypaB46LzS4Ev
---

[OpenChamber 1.19.0](https://github.com/openchamber/openchamber/releases/tag/v1.19.0) was released today, which makes this a good moment to take stock.
I have used it almost daily since February 8.
Along the way I have opened 99 issues, and since April 16 I have had 29 pull requests merged.
**I am still using it every day not because it is polished, but because its core loop earns the friction, and because when the friction gets bad enough, I can fix it myself.**

## What I use it for

OpenChamber is an app built around [OpenCode](https://opencode.ai): sessions, worktrees, chat, files, and terminals in one surface.
My usage is narrow and deep.
I run multiple agent sessions in parallel against the same repositories, and I let OpenChamber own the [worktree](https://git-scm.com/docs/git-worktree) management.
Each session gets its own checkout and its own branch, and I steer all of them from one place.
Six months of this setup adds up to roughly 2,430 sessions across 61 projects, 54,000 messages, and 3.8 billion tokens, on models that moved from GLM 4.7 to GLM 5.3.

Because OpenChamber is always open, it also works as a scratchpad.
When a thought hits, I switch to the right project, write down a few lines, and let a session have a go at it.
**The 99 issues I mentioned were mostly built that way: I describe the problem, and the session turns it into a detailed issue, sometimes with a follow-up comment containing code investigation.**
An idea that would have died as a passing annoyance becomes an artifact, within minutes, inside the same window.

Input is also drifting away from the keyboard.
I use [Handy](https://github.com/cjpais/handy), a speech-to-text tool, more and more to talk to the agent, which speeds up iteration.
And sometimes it is simply how the work continues while my hands are full, eating.

**Iterating on ideas got a lot faster once trying a third approach meant spawning one more session instead of doing the stash-and-switch dance by hand.**
That single property is why I adopted OpenChamber and why I have not stopped.
It is also the last part I would give up.

## The reliability tax

**The hardest part of these six months has been that the chat, the one component whose entire job is to hold a long-running conversation, was sometimes unreliable.**
The causes were varied.
Sending a message to a session whose worktree was still being created blocked until the post-creation commands finished, so a message sent at the wrong moment just sat there.
At other times the connection between OpenChamber and OpenCode dropped, and a few breakages were regressions in OpenCode itself that surfaced downstream in OpenChamber.

The text editor had its own stretch of problems.
It glitched, and it regularly refused to open files it decided were outside the workspace or project, even when they were not.
Both classes of problems got addressed over the months.

## What still bothers me

My main gripe today is the terminal implementation.
Terminal sessions end up closed on their own, which is exactly the failure mode a tool like this should never have, because a terminal holds state you cannot reconstruct.
On Linux, opening the terminal sidebar sometimes shows nothing at all, and the workaround is creating another terminal.

The editing experience is my other daily friction.
The early glitching got fixed, but typing and file navigation in the built-in editor remain clunky next to [VS Code](https://code.visualstudio.com).
OpenChamber also ships as a VS Code extension, which I have never tried, because the point of OpenChamber for me is steering agents from one surface, not living in two.
**The practical cost is that I keep an editor open to review diffs before commits and to look at code from time to time, which is exactly the habit I should be trying to break.**

Two smaller issues have simply persisted for months.
Project selection and filtering in dropdowns remain weak across the app.
And the file matcher behind the `@` helper is still really bad, which is annoying in a tool where pointing an agent at the right file is a core interaction.

## Fixing it yourself changes the math

This is where the 29 pull requests matter.
A bug in a closed tool is a wall: you file it, you wait, and meanwhile you work around it.
**A bug in an open tool you already run every day is just a task, and the more it bothers you, the faster it jumps your queue.**
My 99 issues and 29 merged pull requests are the same friction recorded twice, once as a complaint and once as a fix.

Merging is the part I control least.
Getting a pull request adopted in the main repository sometimes takes real effort, and some of mine are still sitting open.
Since I find those changes useful regardless, I maintain a local branch where I apply my unmerged pull requests and run ahead of upstream.
**The tool I use daily is therefore slightly my own build: official releases plus the fixes I was not willing to wait for.**
It is a small patch queue, the same idea as a distro carrying packages ahead of upstream, and it comes with the same obligation to rebase and drop patches once they land for real.

The relationship with the tool changes as well.
I am no longer only a user deciding whether to stay or leave.
I am a stakeholder: when a release like 1.19.0 ships with fixes from a handful of outside contributors, I read the notes looking for my corners of the app.
That is a much better position than complaining in an issue tracker.

## Should you use it

If you run one agent at a time in a terminal, you probably do not need OpenChamber yet.
If you juggle several agents against the same repositories, parallel sessions plus automatic worktree management alone justify the setup cost, and idea iteration gets visibly faster.
Go in expecting rough edges.
**Then check whether the edge that would bother you most is one you are willing to fix yourself, because that question decides what kind of experience you will have.**

## See also

- [My AI Workflow](../my-ai-workflow/index.md) - where OpenChamber sits in my overall setup and why the skills are the part that compounds
- [Managing Many Concurrent LLM Agent Sessions](../managing-many-llm-agent-sessions/index.md) - the supervision problem that running parallel sessions creates
- [Verifying Code Without Reading It](../verifying-code-without-reading-it/index.md) - the argument behind the diff-reading habit I should be breaking

## References

- [OpenChamber](https://github.com/openchamber/openchamber) - the repository I have been using and contributing to
- [OpenChamber 1.19.0 release notes](https://github.com/openchamber/openchamber/releases/tag/v1.19.0) - the release that prompted this retrospective
- [OpenCode](https://opencode.ai) - the coding agent OpenChamber is built around
- [git worktree](https://git-scm.com/docs/git-worktree) - the mechanism behind per-session isolation
