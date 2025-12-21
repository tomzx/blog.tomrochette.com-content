---
title: Visual Studio Code templates
created: 2020-03-01
taxonomy:
  type: post
  tag: [problems, visual-studio-code]
  status: finished
  readability: 3
---

# Problem
I use VS Code and I'd like to insert templates into my documents. How do I do this?

# Solution
In VS Code, the concept of templates is called [snippets](https://code.visualstudio.com/docs/editor/userdefinedsnippets). It is fairly easy to [create a snippet](https://code.visualstudio.com/docs/editor/userdefinedsnippets#_create-your-own-snippets), so I won't go into the details. Here's an example of a snippet I use to insert the date and time quickly into my documents.

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

With this snippet, I only have to type `dt` and then press <kbd>TAB</kbd> and `dt` gets replaced by the current date and time.

I use snippets to create the template of my [questions](../../../../questions/article.md) and [problems](../../../article.md) articles. My current approach is to open a non-existent file by calling `code /path/to/new/file` and VS Code opens the editor with this file. I can then write the content of this file, which will not automatically save until I manually save. Once I'm happy with the content of my article, I manually save, which means that in the future, any edit I make and then have the editor lose focus will be automatically saved and commit to git (my current workflow).

One of the things I don't particularly like with the current implementation of the snippets system is that the body needs to be a list of strings, where each item represents a new line. It is possible to create a single entry and use \n and \ to format the string, but that is not a clean approach. Those are limitations of jsonc. If it was possible to link to a file, then it would be "easy" to create a clean template.

# References
* https://code.visualstudio.com/docs/editor/userdefinedsnippets
