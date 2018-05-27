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
