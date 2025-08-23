---
title: Slow network under WSL
created: 2025-08-23
taxonomy:
  type: post
  status: finished
  tag: [wsl, network, performance]
---

When I started using WSL on Windows 11 I had slow network performance issues.
We're talking running `speedtest-cli` and getting ~3 Mbps download speeds while my connection can reach 400 Mbps.

After searching online for a while and trying a variety of things I finally found a solution.

In `%USERPROFILE%\.wslconfig` add the following:

```
[wsl2]
networkingMode=mirrored
```

With this fix applied I'm now getting ~400 Mbps download speeds in WSL, matching my native Windows performance.
