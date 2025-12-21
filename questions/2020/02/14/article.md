---
title: Keeping a site up to date while highlighting changes
created: 2020-02-14
taxonomy:
  type: post
  tag: [questions]
  status: finished
  readability: 0
---

# Question
How can you keep a website up to date and yet have previous visitors recognize new content as fast as possible?

# Answer
As I am a developer, what is the most straightforward answer to this problem is to use a tool such as diff. When I write articles on my blog, I use Visual Studio Code which I have configured to save on window getting out of focus (or the current tab of the editor being changed). With this save event, I also create a git commit automatically with a very boring message "Automated save from VS Code.". The point is not to have a fancy commit message, but to have a trace of when the changes where made. This allows me to offer to my visitors the ability to view the history of changes that were done to an article.

The downside to this approach is that it is not very easy to diff the article between two versions using the github web UI. It requires manually playing around the url, to provide the base and latest article SHA1 hash and to find the article in the list of files changed, which makes the experience rather painful and likely to lead nobody to do it.

Given that the git repository is available on my server where the blog is hosted, it would be possible for me to run a `git diff` command provided the last version seen by the visitor. This would allow me to present the changes that were done since the visitor last came. For instance, removal of sentences would be simply not displayed as removed since it is likely to be irrelevant to the visitor, however new sentences would be highlighted in green.
