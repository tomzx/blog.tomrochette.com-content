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
* If you look at the `.vscode/launch.json`, you will find all the tasks that can be executed from within VS Code debugger. One task of interest is `Launch VS Code` which will take care of launching VS Code for us so that we may debug it
	* In this file you will also discover that it runs `${workspaceFolder}/scripts/code.bat`, which is the next script we'll take a look at
* In `./scripts/code.bat`, we discover that this script will run `yarn` if the `node_modules` directory is missing, download the electron binaries if necessary and call `gulp compile` if the `out` directory is missing, then finally start the electron/vs code binary in the `.build/electron` directory
* We then start to look for common entry points file such as `index.ts/js` or  `main.ts/js`, for which we find a match in the `src` directory
* We take a quick look around, trying to find where electron is likely to be instantiated... There's a lot of code in `src/main.js` that would be better elsewhere to make it easier to navigate this file
* Close to the bottom of the file we discover the code we are interested in as a call to `app.once('ready', ...)`
	* Once the app is ready, we want to call `src/bootstrap-amd` and pass `vs/code/electron-main/main` as our entry point (per the signature of the exported function in `./src/bootstrap-amd`)
		* Here we can go to two places, either `src/bootstrap-amd` or `src/vs/code/electron-main/main`
			* We take a quick peek at both files and we can quickly tell that `src/bootstrap-amd` is used mainly to load `src/vs/code/electron-main/main` which is the file we're going to be interested in
* Once again, we quickly look around `src/vs/code/electron-main/main` and find that the main logic is at the bottom of the file
* First the command line arguments are parsed
* Then services are bootstrapped/instantiated
* Finally the `CodeApplication` is started up
* This leads us to look into `src/vs/code/electron-main/app.ts`
* As the file is quite large, we start by skimming through it, looking at the available methods on the `CodeApplication` class as well as its properties
* Looking at the constructor, we can see that a lot of objects are given to it. We also observe the use of the @... syntax (those are decorators)
	* In this case (and for most constructors), this is how VS Code does service (dependencies) injection
* One will also notice that most, if not all parameters have a visibility assigned to it. What this does is that it will create an associated property in the class as well as assigning the parameter value to this property in the constructor. Thus, instead of writing
<pre><code class="language-typescript line-numbers">
class AnotherClass {
	private someClass: SomeClass;

	constructor(someClass: SomeClass) {
		this.someClass = someClass;
	}
}
</code></pre>
you simply write
<pre><code class="language-typescript line-numbers">
class AnotherClass {
	constructor(private someClass: SomeClass) {
	}
}
</code></pre>
* Upon its creation, the `CodeApplication` class will register various event listeners on the electron app object
* If we remember, in `src/vs/code/electron-main/main`, after the `CodeApplication` object is instantiated, we call `startup()` on it. So, we want to take a look at what that method does
* Without knowing too much about the VS Code source, it appears that we are instantiating an IPC server (inter-process communication) and then the shared process
* After that is done, we initialize some more services in `CodeApplication::initServices`, such as the update service (which I guess takes care of checking for VS Code updates) and the telemetry (data about VS Code feature usage)
* We finally get to the point where we're about to open a window in `CodeApplication::openFirstWindow`!
	* This leads us to go read the class `WindowsManager` in `src/vs/code/electron-main/windows.ts`. Once again, this file is pretty large, so we want to skim it to see what it contains (functions, classes, properties, methods)
* There are a few large classes in `src/vs/code/electron-main/windows.ts` that I'd want to extract to make the file smaller and simpler (less cognitive load). However, the issue is that those classes are not declared as exported, and thus are only available in the local file. It would be possible to move these classes to other files and import them, but by doing so it would also "communicate" that others can use it, which is what having the classes as not exported prevents, at the cost of making single files larger and harder to comprehend
* We know that the constructor is first called, then from `CodeApplication::openFirstWindow`, we see that `WindowsManager::ready` and `WindowsManager::open` are both called.
	* In the `constructor` we instantiate the `Dialogs` class (takes care of open/save dialog windows) and the `WorkspacesManager` class (takes care of workspace management, such as open/save)
	* In `ready` event listeners are registered
	* In `open`

## Notes
* If you start VS Code using the debug feature, you will not be able to open the Chrome DevTools (at this moment, 2018-05-26) because only 1 process is allowed to attach to the Chrome DevTools instance, and that process is the VS Code editor that started the debugged VS Code instance
