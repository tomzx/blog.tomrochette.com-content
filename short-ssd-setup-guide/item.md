---
title: Short SSD setup guide
created: 2013-01-05T08:12:09-05:00
taxonomy:
    type: post
    category: Computers
    tag: ssd
---

Backup everything. First rename, then remove when you confirmed it worked. Better safe than sorry.

<pre><code class="language-bash line-numbers">
REM Set the new root location
REM Ex. NEW_ROOT=D:
REM     NEW_ROOT=D:\Data
REM     NEW_ROOT=D:\MyStuff\MyComputer
set NEW_ROOT=D:

REM (Make sure that C:\Users doesn't exist anymore)
move C:\Users C:\Users.Backup
mklink /J C:\Users %NEW_ROOT%\Users

REM DO NOT DO THE FOLLOWING
REM (Rename C:\ProgramData before creating the link)
move C:\ProgramData C:\ProgramData.Backup
mklink /J C:\ProgramData %NEW_ROOT%\ProgramData

REM Update the TEMP folder at system level
setx /m TEMP %NEW_ROOT%\Windows\Temp
setx /m TMP %NEW_ROOT%\Windows\Temp

move C:\Windows\Temp C:\Windows\Temp.Backup
mklink /J C:\Windows\Temp %NEW_ROOT%\Windows\Temp
REM END DO NOT DO
</code></pre>
