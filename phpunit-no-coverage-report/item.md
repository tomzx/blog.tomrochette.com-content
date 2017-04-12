---
title: PHPUnit - No coverage report
created: 2012-08-05T02:20:34-05:00
Author: tomzx
Permalink: /phpunit-no-coverage-report/
taxonomy:
    type: post
    category: Programming
    tag: [code coverage, php, phpunit]
---

I was trying to get PHPUnit to give me some coverage report for a project I had not worked on for a long time. I had received a github pull request from someone and I wanted to see what the coverage was on the project to see if the submitter had done a good job of covering his code, but I couldn't get PHPUnit to generate a report that contained any data. All I would get was a couple of empty directory folders pages, which was useless.

I had code coverage work on another project in the same environment I was in, so I was pretty sure that my problem had to do either with how I had setup PHPUnit for that particular project, or that something else was interfering with the report generation.

I tried a couple of things, starting by calling phpunit from the command line using different arguments:

```shell
--coverage-html report test\symbol_test.php
```
Would generate some report with data in it, good!

```shell
-c test\phpunit.xml (logging set in phpunit.xml)
```
Would generate an empty report, not good...

```shell
--coverage-html report -c test\phpunit.xml
```
Would generate an empty report, not good...

So at that point I saw that it was working correctly and that something was definitely wrong with my phpunit.xml configuration file. I went back to the [phpunit.de](https://phpunit.de/manual/current/en/code-coverage-analysis.html#code-coverage-analysis.whitelisting-files) manual, specifically on the configuration page, and tried to figure out my problem.

For code coverage to be included in your report, you have to add a filter, be it a blacklist or a whitelist, but you have to have a filter.

So I quickly added a filter such as

<pre><code class="language-markup line-numbers">&lt;filter&gt;
	&lt;whitelist&gt;
		&lt;directory&gt;../&lt;/directory&gt;
	&lt;/whitelist&gt;
&lt;/filter&gt;
</code></pre>

which would whitelist everything that is in the project (my project root is one level above test). Ran **phpunit ** in the test folder and I finally got a report with data!
