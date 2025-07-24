---
title: Quickly recording notes using VS Code
created: 2020-03-02
taxonomy:
  type: post
  tag: [problems, visual studio code]
  status: finished
---

# Problem
I want to quickly take notes in the same file throughout the day using VS Code. How do I do that?

# Solution
My approach has been to use my VS Code extension [Run Me](https://marketplace.visualstudio.com/items?itemName=tomzx.run-me), which I use to bind a keyboard shortcut to one of the commands I created. In my particular case, on any VS Code window I can press <kbd>CTRL</kbd><kbd>Numpad 2</kbd> and it will open a file under the following path: buffer/YYYY/MM/DD.md, where YYYY/MM/DD is replaced with the year/month/day. In this file I record all my notes within the day.

I use the following snippet, which I can trigger using `dt`, then pressing <kbd>TAB</kbd>. This replaces the `dt` string with a string of the form `YYYY-MM-DD HH:MM:SS`, which is the current year-month-day hour:minute:second.

```json
{
	"Datetime": {
		"scope": "",
		"prefix": "dt",
		"body": [
			"$CURRENT_YEAR-$CURRENT_MONTH-$CURRENT_DATE $CURRENT_HOUR:$CURRENT_MINUTE:$CURRENT_SECOND"
		],
		"description": "Date time"
	}
}
```

I also use the [Script Commands](https://marketplace.visualstudio.com/items?itemName=mkloubert.vs-script-commands) extension to do something slightly more complicated, which is to create strings of the form `2020-03-02 21:19:05 [nid://952]`, where `nid://952` represents a unique note id (`nid`). The number that is generated is unique and is tracked by storing the last generated number in a text file that is read/written on each call to this command. A cheaper approach could have been to simply use the timestamp as unique note id. One downside of the timestamp as note id approach is that you don't have an idea of how many notes you've recorded so far, other than searching your notes and then counting the number of unique instances.

# References
* [Visual Studio Marketplace - Run Me extension](https://marketplace.visualstudio.com/items?itemName=tomzx.run-me)
* [Thoughts tracking](../../../../questions/2020/02/01/article.md)
