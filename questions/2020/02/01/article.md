---
title: Thoughts tracking
created: 2020-02-01
taxonomy:
  type: post
  tag: [questions]
  status: finished
  readability: 0
---

# Question
How do I track my thoughts?

# Answer
When I am on the go, I mostly rely on [Google Keep](http://keep.google.com/) to write down what on my mind. I use it because it loads fast, is straightforward and allows me to quickly dump my thought and go back to what I was doing. Since I'm always with my phone, it's always within reach. It also will synchronize with Google when I'm online so it is available on any other devices. This also means that I may sometimes record things either directly from my computer, my work computer, my phone or my tablet, depending on the medium I'm using at the time (defaulting to my phone if I'm not using any device when the thought crops up).

When I am at home, I've devised a simple system in Visual Studio Code where I use two keyboard shortcut, one that open today's [buffer](../../../../note-taking/article.md#my-current-system) (<kbd>CTRL</kbd><kbd>Numpad 2</kbd>) and one that inserts a datetime and note id on the current line (<kbd>CTRL</kbd><kbd>Numpad 0</kbd>).

When I am at work, I use this same system to take notes pertaining my work. I generally try to organize my thoughts per projects so that I can go back to any specific project and re-read the notes to get back in context. I also will write down notes related to issues I'm working on and identify them using the issue ID given by JIRA.

In both cases (at home and at work), I also have configured Visual Studio Code to commit automatically to git changes that are done in markdown files when the editor focus changes. This allows me to have a somewhat granular log of the changes that happen to my note files. At work, I have configured a cronjob that automatically pushes the notes to my private git repository. This allows me to pull those notes at home and read them whenever I want. I also push my personal notes to my private git repository, but I do not pull them on my work computer because I haven't had the need for it.

# References
* [Note taking](../../../../note-taking/article.md)
