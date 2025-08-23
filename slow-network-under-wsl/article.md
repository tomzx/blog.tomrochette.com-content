---
title: Slow network under WSL
created: 2025-08-23
taxonomy:
  type: post
  status: finished
  tag: [wsl, network, performance]
---

When I started using WSL on Windows 11 I had slow network performance issues.

In `%USERPROFILE%\.wslconfig` add the following:

```
[wsl2]
networkingMode=mirrored
```
