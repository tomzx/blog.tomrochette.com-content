---
title: Happier
created: 2026-11-01
updated: 2026-11-04
status: finished
tags: [research-note, agent-curated, fully-ai-generated, llm=glm-5.3-flash, orchestration, multi-agent, mobile, end-to-end-encryption]
readability: 3
audience_notes: >
  Engineers running coding agents on several machines who want to steer sessions from a phone or a second device without a vendor relay.
  Assumes you know what Claude Code, Codex, and OpenCode are.
---

Happier is an open-source, self-hostable control room that runs teams of 100-plus coding agents across your own machines and steers them from a phone, desktop, or browser.

**The bet is that supervision should follow you across devices with end-to-end encryption, so the control room is wherever you are instead of a desk-bound dashboard.**

## What it is

A desktop app (macOS, Windows, Linux), iOS and Android apps, and a web client, all attached to a CLI and daemon you install on your own machines.
Sessions are E2E encrypted and can spawn subagents across agents: Claude asks Codex for a review, Codex delegates to Claude subagents, and you can switch agents mid-session.
Seventeen agents ship built in (Claude Code, Codex, OpenCode, Gemini CLI, Auggie, Qwen Code, Kimi, Kilo, Kiro, Devin, Pi, GitHub Copilot, Cursor, Grok, FX, Droid, Antigravity), thirty-plus more are claimed, and anything that speaks ACP adds from settings.
You approve, steer, review diffs, and commit from whichever device is in your hand, riding your existing agent subscriptions.
By the happier-dev org, repository created 2025-12-16, MIT licensed, docs at docs.happier.dev.

## Status

Active: 2,102 stars, 209 forks, and 212 open issues and pull requests as of 2026-11-01 (GitHub API), pushed 2026-11-04, with 100-plus releases on parallel dev tracks (ui-web, server, cli) and the train pushing daily.
The `@happier-dev/cli` npm package (first version 2026-02-21) is at latest 0.2.20 (npm, as of 2026-11-04), with 3,624 downloads in October 2026.

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="https://api.star-history.com/chart?repos=happier-dev/happier&type=date&theme=dark&legend=top-left" />
  <source media="(prefers-color-scheme: light)" srcset="https://api.star-history.com/chart?repos=happier-dev/happier&type=date&legend=top-left" />
  <img alt="Star History Chart" src="https://api.star-history.com/chart?repos=happier-dev/happier&type=date&legend=top-left" />
</picture>

Zero independent coverage found: a Hacker News story search returns no thread about the project as of 2026-11-01, so the footprint is the repository, the CLI downloads, and the docs site itself.

## Strengths

- **Cross-agent subagent spawning is the differentiator: sessions that hand work between CLIs answer the multi-model workflow most multiplexers leave to you.**
- The E2E-encrypted, self-hosted design keeps session content off a vendor relay, unlike the hosted-relay mobile clients.
- Device continuity is thorough: switch agents mid-session, pick up the same session from phone, desktop, or browser.

## Cautions

- No independent coverage at all as of 2026-11-01; adoption evidence is the star count and CLI downloads, both young.
- The CLI sits at 0.2.x on a daily dev train, so expect churn and occasional breaking moves.
- The "teams of 100+ agents" scale claim has no published third-party benchmark behind it.

## Pricing

Free and open source under MIT, self-hosted.
No paid tier found as of 2026-11-01; you bring your existing agent subscriptions.

## Compared to

- [OpenHarness](../openharness/index.md): the native command center across linked machines with phone, web, and desk-device clients; Happier is the MIT, browser-and-mobile-first counterpart.
- [T3 Code](../t3code/index.md): the control surface driving six CLIs from native clients on your subscriptions; Happier adds cross-agent subagents and self-hosted encryption.
- [Happy Coder](../happy-coder/index.md): the encrypted mobile client wrapping Claude Code and Codex; Happier widens to seventeen-plus agents and desktop control.

## Bottom line

**Recommended for engineers running many agents across several machines who want encrypted phone steering without a vendor relay.**
Not for board-and-worktree workflows, which it does not model, and not for anyone who needs a battle-tested 1.0.

## Changes

- 2026-11-01 - Created.
- 2026-11-04 - Status refresh: the push date refreshed to 2026-11-04 and the npm CLI latest to 0.2.20.

## See also

- [OpenHarness](../openharness/index.md) - the multi-machine command center precedent this admission rides
- [T3 Code](../t3code/index.md) - the subscription-riding multi-client control surface
- [Happy Coder](../happy-coder/index.md) - the encrypted mobile client this widens on
- [hcom](../hcom/index.md) - the messaging-fabric alternative that keeps your own terminal setup

## References

- https://api.github.com/repos/happier-dev/happier - stars, license, activity, and creation date as of 2026-11-01
- https://raw.githubusercontent.com/happier-dev/happier/HEAD/README.md - the control-room model, supported agents, encryption, and install paths
- https://api.github.com/repos/happier-dev/happier/releases?per_page=100 - the 100-release dev train
- https://registry.npmjs.org/@happier-dev/cli - the CLI package, 45 versions, latest 0.2.17
- https://api.npmjs.org/downloads/point/2026-10-01:2026-10-31/@happier-dev/cli - October 2026 downloads (3,624)
- https://happier.dev/ - the product site
- https://docs.happier.dev/releases - the release channels documentation
- https://hn.algolia.com/api/v1/search?query=happier&tags=story&hitsPerPage=20 - the zero-story Hacker News footprint as of 2026-11-01
