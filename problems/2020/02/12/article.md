---
title: Visual Studio Code Run Me extension
created: 2020-02-12
taxonomy:
  type: post
  tag: [problems, visual studio code]
  status: finished
---

# Problem
I frequently run the same commands with different parameters but I have a terrible memory. I also use Visual Studio Code a lot.

# Solution
I developed an extension in 2018 called [Run Me](https://marketplace.visualstudio.com/items?itemName=tomzx.run-me) whose goal is to allow you to define commands that you can customize through a form, which is a series of questions that will be asked to you, before launching the command with the parameters you provided.

I've used it to do all kinds of things, from launching [OBS](https://obsproject.com/) to resetting the Windows 7 visuals when it lowers them down due to low memory. I also use it to automate various tasks such as creating new articles using a template, opening my buffer document that I use on a daily basis to write notes and more.

Here's an example of my configuration file which I use to start OBS and to reset the Windows 7 visuals.
```json
"run-me": {
	"commands": [
		{
			"identifier": "start_obs",
			"description": "Start OBS x64",
			"command": "\"C:\\Program Files (x86)\\obs-studio\\bin\\64bit\\obs64.exe\"",
			"working_directory": "C:\\Program Files (x86)\\obs-studio\\bin\\64bit"
		},
		{
			"identifier": "reset_visuals",
			"description": "Reset W7 visuals",
			"command": "sc stop uxsms & sc start uxsms"
		}
	]
}
```

# Reference
* [Visual Studio Marketplace - Run Me extension](https://marketplace.visualstudio.com/items?itemName=tomzx.run-me)
* [Github repository - Run Me extension](https://github.com/tomzx/vscode-run-me)
