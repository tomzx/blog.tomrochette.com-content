---
title: RICHTX32.ocx registration fix
created: 2006-06-05T18:34:49-05:00
taxonomy:
    type: post
    tag: [computers, windows, dll]
---

> "richtx32.ocx" is not an executable file and no registration helper is registered for this file type.

I had this thing always appearing while using my FTP software so I had to fix it. I looked all over the internet to find any possible fix but no one gave me the answer I was looking for. After a while I decided I would try to find out the latest version of this file and almost every place I went to, I found the version 6.0.88.4 which was the one not working for me. Then I went to [http://www.martin2k.co.uk/][1] and grabbed his **Microsoft Rich Textbox Control 6.0 (SP4) (richtx32.ocx)** which was version 6.0.88.77. By executing `regsvr32 c:\windows\system32\RICHTX32.OCX` on my winXP computer, the damn thing finally registered itself!

 [1]: http://www.martin2k.co.uk/vb6/vb6download4.php
