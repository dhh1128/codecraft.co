---
title: Encapsulation isn't just for code
date: 2013/08/02
slug: encapsulation-isnt-just-for-code
---

When computer science folks talk about encapsulation, they are usually thinking of how the principle applies to objects and functions inside a codebase. Best practice calls for a separation of concerns--each object responsible for one type of work, hiding all details from its neighbors.

That's great. But it's not the only way encapsulation ought to show up in software.

In actual deployment, software packages often manifest anti-patterns in the way that they are configured. A web server has to know all about three different database servers that contribute data for its pages; HA failover scripts must know the identity and responsibility of every actor in the system, as well as many particulars about how these entities use resources to accomplish their tasks.

No wonder our deployments are fragile and high-maintenance...

The cloud computing wave is raising the bar for encapsulation in the way applications--not just objects--discover and interact with one another. In this week's installment of my <a title="cloudify series" href="http://codecraft.co/category/cloudify">series of posts about how to "cloudify"</a>, I discuss how <a href="http://www.adaptivecomputing.com/blog-cloud/how-to-cloudify-your-software-part-3-do-you-want-fries-with-that/" target="top">role-based interactions insulate components</a> from details they don't need to know. It's encapsulation all over again. And this encapsulation pattern manifests itself in unlikely places--like the order queue at McDonald's...

[caption id="" align="aligncenter" width="500"]<a href="http://www.adaptivecomputing.com/blog-cloud/how-to-cloudify-your-software-part-3-do-you-want-fries-with-that/"><img class=" " alt="" src="http://farm1.staticflickr.com/102/258253832_927e23b2b9.jpg" width="500" height="375" /></a> What can McDonalds teach a developer of cloud-friendly software? <a href="http://www.flickr.com/photos/derfokel/258253832/sizes/m/in/photolist-oPBSh-F14J9-MQh6J-4c1HXK-4mEHoC-4ovGHD-4upuzt-4wYDLv-5jWmpq-5Xv7Wr-729ALs-76Locf-7E3LgF-9e8N8c-buruPp-bxadb4-biwGXv-e8ySUj-cEmmDf-ebusvW-8MBDdG-bvALeU-b5yiwg-9D3wMX/" target="_blank">photo credit: phogel (Flickr)</a>[/caption]

Stay tuned for further installments of this series each Friday. As I said in <a title="learn how to cloudify" href="/2013/07/23/programmers-learn-how-to-cloudify/">Part 1</a>, I believe that a competence with cloud–cloud-oriented programming, if you will–will be a checkbox on future tech resumes.

---

SutoCom (2013-09-04 03:51:41)

Reblogged this on <a href="http://sutocom.net/2013/09/04/encapsulation-isnt-just-for-code/" rel="nofollow">Sutoprise Avenue, A SutoCom Source</a>.