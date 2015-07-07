---
title: PHPUnit not outputting coverage-html
date: 2011-10-25T01:31:45-05:00
Author: tomzx
Template: post
Permalink: /phpunit-not-outputting-coverage-html/
Categories: Programming
Tags: code coverage, php, phpunit
---

I've been using PHPUnit recently to test a Kohana application I'm developing as my last semester project for my bachelor's degree.

At some point during the development, code coverage generation decided to stop working on my desktop (my remote CI still had no problem).

I started diagnosing the problem, being on Windows, I thought it could be due to the "poor job" I had done on installing php, pear and phpunit. I didn't want to go through the trouble or reinstalling everything though and just did the minimum: uninstall and reinstall phpunit. No success at that point.

I decided to go back a week or two in my SVN revisions, have it generate code coverage and get to the point were code coverage generation would fail. Took around 2 SVN "update to" to get to that point. After that, I tried updating the tests, but the new tests were using new features. So I updated the code first, then started updating the test files one by one. After a couple of files, I hit an interesting message:

> ErrorException [ 1 ]: Allowed memory size of 134217728 bytes exhausted (tried to allocate 543278 bytes) ~ C:\php\pear\Text\Template.php [ 134 ]

I never had that message show up before, which is kind of strange. I would have expected PHP to tell me that same message everytime it tried to generate the documentation but couldn't...

So, quick fix was for me to edit my php.ini so that the memory_limit = 256M instead of 128M.