---
title: Slow git under WSL
created: 2025-08-23
taxonomy:
  type: post
  status: finished
  tag: [wsl, git, performance]
---

I have a `git` repository with 25k commits in it and 7k+ files.

Under Windows 11 using WSL, I noticed that `git` operations were significantly slower compared to running them natively on Windows.

I have [a script that I use to synchronize many branches](https://github.com/tomzx/personal-automation/blob/master/others/git-sync-branches.sh) that was taking forever to execute, but should have been relatively fast.
It also had trouble with line endings which caused issues when merging branches but reminded me of a setting I used to configure in my `~/.gitconfig` a very long time ago.

Given that `git` configuration under Windows and WSL are separate, I had to update the `~/.gitconfig` file in my Linux environment with the following.

```
[core]
    autocrlf = true
```

This immediately fixed my problem and `git` was fast again.
