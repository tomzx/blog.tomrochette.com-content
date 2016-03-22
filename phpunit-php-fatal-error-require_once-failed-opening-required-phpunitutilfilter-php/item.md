---
title: "PHPUnit - PHP Fatal error: require_once(): Failed opening required 'PHPUnit/Util/Filter.php'"
date: 2011-11-26T00:14:53-05:00
Author: tomzx
Permalink: /phpunit-php-fatal-error-require_once-failed-opening-required-phpunitutilfilter-php/
taxonomy:
    type: post
    category: Programming
    tag: [php, phpunit]
---

A friend of mine was trying to install PHPUnit on his mac (OS X Lion), but unfortunately, he got stuck during the process.

At some point, he was faced with this error being displayed. We both looked at the problem and first made sure that said file existed. It was the case, weird...

A bit of googling will reveal that this is frequently fixed by appending the path to the pear folder to your php include_path (defined in your php.ini). But in his case, that was already done and it still wasn't working.

Next up was to check permissions problem. Not having read permissions on the file would of been an easy one to fix, but again, this was not the cause of the problem.

At this point you might be asking yourself, how come the file exists, you have permission to read it, but yet, you can't...

Well, the actual problem was that his OS was set up such that the maxfiles was set to 256 and PHPUnit had already reached that amount of open files.

To check if you have the same problem, try running phpunit using `sudo dtruss -f -t open phpunit` (Linux users will want to use `strace -e open phpunit`). In your output, you should see the files being opened. At some point, you'll find `Err#24`, which indicates "To many file descriptors opened". If you have this problem, then the following should help you fix it.

The solution to this problem is quite easy. What you'll want to do is increase the maximum number of descriptors that can be used by a process. You can do it temporarily with `ulimit -S -n 1024` (to use 1024 instead of 256). Another way is to edit it and keep those settings (until you change them again) is to use `launchctl limit maxfiles 1024 unlimited`.
