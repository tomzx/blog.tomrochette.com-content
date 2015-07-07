---
title: Munin, mysql and semaphore: how to deal with the &#8220;identifier removed&#8221; error
date: 2013-10-02T22:14:13-05:00
Author: tomzx
Template: post
Permalink: /munin-mysql-and-semaphore-how-to-deal-with-the-identifier-removed-error/
Categories: Programming
Tags: identifier removed, ipcrm, ipcs, munin, mysql, semaphore
---

The following depicts how I &#8220;solved&#8221; a problem I recently had regarding munin, its mysql plugins and the shared memory cache library used by the plugins (written in perl and using IPC::ShareLite).

First off, let&#8217;s begin with a description of the problem. I posted the following on [serverfault.com][1] in hope I&#8217;d get help from someone more experienced than I am.

> I&#8217;ve recently setup a munin-node on a CentOS server. All was working fine until I tried to add the apache plugin (which works fine).
> 
> For some odd reason, the mysql plugins for munin that used to work ceased to work&#8230; I&#8217;m now getting a weird error whenever I&#8217;m running the plugin with `munin-run`. For instance
> 
> `munin-run mysql_files_tables`
> 
> returns me
> 
> <pre><code class="bash">IPC::ShareLite store() error: Identifier removed at /usr/lib/perl5/vendor_perl/5.8.8/Cache/SharedMemoryBackend.pm line 156
</code></pre>
> 
> but sometimes it will also return
> 
> <pre><code class="bash">table_open_cache.value 64
Open_files.value 58
Open_tables.value 64
Opened_tables.value 19341
</code></pre>
> 
> but after a while it will revert to the previous error.
> 
> I do not have any knowledge about the IPC or the ShareLite library so I don&#8217;t really know were to start looking. Since it is a module related to shared memory, I tried tracking down shared memory segments with `ipcs` without much success.
> 
> I haven&#8217;t yet rebooted the machine as it is used for many projects (I&#8217;d obviously like to be able to diagnose the problem without requiring a restart if it was possible).
> 
> Has anyone faced this problem? (a quick search on google didn&#8217;t present any relevant help)
> 
> Thanks for the help!

Obviously, one can see quickly that this is a quite specific question that not many may have actually encountered. Thus, I didn&#8217;t expect to receive much help out of it (and I didn&#8217;t).

I had left this issue on the side for a couple of days hoping to come back to it at some point. Munin and the mysql plugins were installed on two servers and it was working fine on both of them (and a third one as master node). After a minor change, one of two *client* nodes stopped working correctly while the other was still fine. After a couple of days though the second server also decided to exhibit a similar issue&#8230;

Tonight I remembered about `strace`, which is pretty awesome in circumstances like this one. I went ahead and launched `strace munin-run mysql_files_tables` which outputted a lot of stuff and then stopped at the following point:

<pre><code class="bash">...
ioctl(4, SNDCTL_TMR_TIMEBASE or TCGETS, 0x7fff13da8e30) = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
read(4, "# Carp::Heavy uses some variable"..., 4096) = 4096
brk(0x163e7000)                         = 0x163e7000
read(4, "\n    redo if $Internal{$caller};"..., 4096) = 1737
read(4, "", 4096)                       = 0
close(4)                                = 0
write(2, "IPC::ShareLite store() error: Id"..., 123IPC::ShareLite store() error: Identifier removed at /usr/lib/perl5/vendor_perl/5.8.8/Cache/SharedMemoryBackend.pm line 156
) = 123
semop(14581770, 0x2ab08bb67cf0, 3
</code></pre>

and when it is actually fixed, the application would end instead (outputting a bunch of stuff such as the following)

<pre><code class="bash">...
stat("/usr/lib64/perl5/auto/Storable/_freeze.al", {st_mode=S_IFREG|0644, st_size=706, ...}) = 0
stat("/usr/lib64/perl5/auto/Storable/_freeze.al", {st_mode=S_IFREG|0644, st_size=706, ...}) = 0
open("/usr/lib64/perl5/auto/Storable/_freeze.al", O_RDONLY) = 4
ioctl(4, SNDCTL_TMR_TIMEBASE or TCGETS, 0x7fffe7223570) = -1 ENOTTY (Inappropriate ioctl for device)
lseek(4, 0, SEEK_CUR)                   = 0
read(4, "# NOTE: Derived from ../../lib/S"..., 4096) = 706
read(4, "", 4096)                       = 0
close(4)                                = 0
semop(917514, {{1, 0, 0}, {2, 0, 0}, {2, 1, SEM_UNDO}}, 3) = 0
semop(917514, {{2, -1, SEM_UNDO|IPC_NOWAIT}}, 1) = 0
semop(917514, {{1, 0, 0}, {2, 0, 0}, {2, 1, SEM_UNDO}}, 3) = 0
shmdt(0x7fc30021f000)                   = 0
semop(917514, {{2, -1, SEM_UNDO|IPC_NOWAIT}}, 1) = 0
...
</code></pre>

### How to &#8220;fix&#8221; the problem

What you can see in the first output above is pretty interesting. The semop call gives you the semid the process is trying to obtain (the semaphore used to synchronize different processes using the same shared memory). The signature of the semop function is as follow:

<pre><code class="cpp">int semop(int semid, struct sembuf *sops, unsigned nsops);</code></pre>

where  
**semid:** semaphore id  
**sops:** pointer to a sembuf struct

<pre><code class="cpp">struct sembuf {
	u_short sem_num; /* semaphore # */
	short   sem_op;  /* semaphore operation */
	short   sem_flg; /* operation flags */
};
</code></pre>

**nsops:** the length of sops

Upon first inspection, you can see that the sembuf in the first case seems to be invalid if you compare it with the working version where it is actually resolved (strace displays something such as `{{2, -1, SEM_UNDO|IPC_NOWAIT}}` instead of `0x2ab08bb67cf0`. But that is not helping me much.

With that semid you can do two things: first, you can check if it is still alive by calling `ipcs`, second, you can remove it with `ipcrm -s semid`.

In my case the &#8220;fix&#8221; itself was to remove the semaphore that the plugin wasn&#8217;t able to obtain (the reason of this still elude me though). After the removal of the semaphore, it is possible again to run munin correctly and the **identifier removed** error is gone.

I will have to do more research as to how/why this issue occurs as I&#8217;ve seen it happen only on CentOS machines so far (the master server is a Debian machine).

 [1]: http://www.http://serverfault.com/questions/542232/munin-mysql-plugins-results-inconsistent-with-ipcsharelite-store-error-ide