---
title: Claude on Windows
created: 2025-07-24
taxonomy:
  tag: [artificial-intelligence, claude, windows]
  status: in progress
  readability: 3
---

In this article I write myself some notes on my usage of Claude on Windows.
It may contain a variety of things that are unrelated to one another.

# Personal commands

The [claude documentation](https://docs.anthropic.com/en/docs/claude-code/slash-commands#personal-commands) indicates that personal commands can be set in `~/.claude`, but there is no documentation about Windows.

On Windows, the `~/.claude` directory is located in `C:\Users\<username>\.claude`, or `%USERPROFILE%\.claude`.

# New personal commands

New commands are not automatically added in existing sessions.
One has to restart the session to see the new commands.
