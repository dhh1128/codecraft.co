---
title: What are your software's vital signs?
date: 2013/08/11
slug: what-are-your-softwares-vital-signs
---

Most software has a profoundly inadequate concept of "health." In order for applications to run, they must:
<ul>
	<li>have adequate resources (RAM, disk, network, CPU)</li>
	<li>receive cooperation from services exposed by the operating system or by network endpoints</li>
	<li>be adequately and correctly configured</li>
	<li>not be hacked</li>
	<li>acquire delegated privileges from users</li>
</ul>
... and so forth. And yet, most software that I've encountered in my career does little to see whether it's working properly and has what it needs. Sure, it may log a catastrophic error if the disk fills up, but it makes no effort to see the problem coming or to plan more graceful recovery than a crash.

In my <a title="cloudify - check vital signs" href="http://www.adaptivecomputing.com/blog-cloud/how-to-cloudify-your-software-part-4-check-those-vital-signs/" target="_blank">most recent post</a> on <a title="cloudify software series" href="http://codecraft.co/category/cloudify" target="_blank">cloudifying your software</a>, I explore how cloud computing is magnifying the need to understand and to regularly check your software's vital signs. Head on over to adaptivecomputing.com/blog and check it out.

[caption id="" align="aligncenter" width="500"]<img alt="" src="http://farm8.staticflickr.com/7323/9009986079_3ecc0332bc.jpg" width="500" height="333" /> Checking vitals isn't just for healthcare... Photo credit: U.S. Pacific Fleet (Flickr)[/caption]

Stay tuned for further installments of this series each Friday. As I said in <a title="Programmers: learn how to “cloudify”" href="http://codecraft.co/2013/07/23/programmers-learn-how-to-cloudify/" target="_blank">Part 1</a>, I believe that a competence with cloud–cloud-oriented programming, if you will–will be a checkbox on future tech resumes.