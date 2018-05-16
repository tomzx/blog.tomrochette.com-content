---
title: Accepting self-signed (or unknown) certificates with TortoiseGit
created: 2013-09-18T03:16:44-05:00
Author: tomzx
Permalink: /accepting-self-signed-or-unknown-certificates-with-tortoisegit/
taxonomy:
    type: post
    category: Programming
    tag: [certificates, git, tortoisegit]
---

For some odd reason it seems that the system designed into [TortoiseGit](https://code.google.com/p/tortoisegit/) doesn't allow the user to interact with git when it requires user interaction. For instance, accepting self-signed certificated is not possible, which gives you the known [issue 318](https://gitlab.com/tortoisegit/tortoisegit/issues/318).

As of TortoiseGit 1.8.5.0, it is still not possible to accept certificates through the GUI. But it is possible to get your git repository to work with TortoiseGit (and work with the required certificate).

You will need to have **msysgit** installed and available in your PATH for the following to work.

The first step is to run some git command, for instance `git clone https://myserver.com/depot` via a command line so that git may auto-accept (or ask you to accept) the certificate. This step is crucial to get the certificate details saved onto your machine.

What you will want to do next is go to `C:\Program Files (x86)\Git\.subversion` and copy everything into `%USERPROFILE%\.subversion`. Basically, this should copy the certicates that were accepted by msysgit so they can be used by TortoiseGit.

Another, and possibly better solution, is to create a symbolic link so that those 2 folders are in fact a single one. For instance, you could do something such as

<pre><code class="language-bash line-numbers">
move %USERPROFILE%\.subversion %USERPROFILE%\.subversion_backup
mklink /D %USERPROFILE%\.subversion "C:\Program Files (x86)\Git\.subversion"
</code></pre>

which will make `%USERPROFILE%\.subversion` point to your `C:\Program Files (x86)\Git\.subversion` folder. This has the benefit that any future certificate will work both for msysgit and TortoiseGit.

Thanks to [Mexx&#8217; C# Corner](http://blog.malook.de/2010/10/tortoisegit-as-frontend-to-https-svn.html) for pointing out the solution.
