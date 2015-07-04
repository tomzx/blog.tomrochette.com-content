/*
 title: Boot Camp and Windows install
 Author: tomzx
 Template: post
 Permalink: /boot-camp-and-windows-install/
 Date: 2007-11-12T01:30:14-05:00
 Categories: Computers
*/
If you're having a hard time getting Boot Camp to correctly install Windows and you're getting either a "disk error" or "hal.dll missing" error, here's how to actually fix it.

First, you'll have to restore your disk to a full Mac OS X partition.
Then, you'll reformat it to be a Mac OS X partition and a Windows partition (using Boot Camp).

This is now the important step. You must write over the partition. So load up the Terminal and enter

<pre><code class="bash">sudo dd if=/dev/zero of=/dev/rdisk0s3 bs=1m count=100</code></pre>

Where rdisk0s3 is the disk where the Windows Partition is. To know the name of your Windows partition, you can go to the Disk Utility (Applications-Utilies) and look for a partition under your hard drive.

When that is done, you can restart your computer with your Windows CD and install it. Everything should be fine now.

PS. Use at your own risk. The command involve writting 0's to your partition table, which might screw it up if done unproperly.

PPS. I cannot be held responsible for anything happening to you or your computer.