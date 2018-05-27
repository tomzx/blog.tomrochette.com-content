---
title: Learning VS Code source
created: 2018-05-26
taxonomy:
  type: post
  category: [Programming]
  status: draft
---

# 2018-05-26
* Read `package.json` to discover what packages VS Code depends on
* Observe the root directory structure, and more specifically the `extensions` and `src` directories which contain the bulk of the source code
	* A lot of the code in the `extensions` directory appears to be dedicated to programming language support
		* The remainder of the extensions seem to provide functionality for things that aren't "core" to vscode, such as `configuration-editing`, `emmet`, `extension-editing` and some color themes
* If you look at the `./.vscode/launch.json`, you will find all the tasks that can be executed from within VS Code debugger. One task of interest is `Launch VS Code` which will take care of launching VS Code for us so that we may debug it

## Notes
* If you start VS Code using the debug feature, you will not be able to open the Chrome DevTools (at this moment, 2018-05-26) because only 1 process is allowed to attach to the Chrome DevTools instance, and that process is the VS Code editor that started the debugged VS Code instance
