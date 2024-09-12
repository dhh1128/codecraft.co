---
title: The Scaling Fallacy
date: 2012/12/19
slug: the-scaling-fallacy
---

<em>If X works for 1 ___ </em>[<em>minute | user | computer | customer | ...</em>]<em>, then 100X ought to work for 100, right? And 1000X for 1000?</em>

Sorry, Charlie. No dice.

One of my favorite books, <a href="http://www.amazon.com/Universal-Principles-Design-Revised-Updated/dp/1592535879" target="_blank">Universal Principles of Design</a>, includes a fascinating discussion of our tendency to succumb to scaling fallacies. The book makes its case using the strength of ants and winged flight as examples.

Have you ever heard that an ant can lift many times its own weight--and that if that if one were the size of a human, it could hoist a car over its head with ease? The first part of that assertion is true, but the conclusion folks draw is completely bogus. Exoskeletons cease to be a viable structure on which to anchor muscle and tissue at sizes much smaller than your average grown-up; the <a class="zem_slink" title="Specific strength" href="http://en.wikipedia.org/wiki/Specific_strength" target="_blank" rel="wikipedia">strength-to-weight ratio</a> just isn't good enough. Chitin is only about as tough as fingernails.

[caption id="" align="aligncenter" width="500"]<a href="http://www.flickr.com/photos/ink2012/8146750081/"><img alt="" src="http://farm9.staticflickr.com/8050/8146750081_0e07106d00.jpg" width="500" height="264" /></a> Tough little bugger -- but not an olympic champion at human scale. Image credit: D.A.Otee (Flickr)[/caption]

I'd long understood the flaws in the big-ant-lifting-cars idea, but the flight example from the book was virgin territory for me.

Humans are familiar with birds and insects that fly. We know they have wings that beat the air. We naively assume that at much larger and much smaller scales, the same principles apply. But it turns out <!--more--> that at the micro scale, wings don't move enough air molecules to be helpful when they flap, and at the giant scale (say, the size of an elephant), flapping wings become impractical due to structural challenges.

<strong>So what?</strong>

What does this have to do with software?

For one thing, what works in small codebases often doesn't work in large ones. The need for disciplined practices such as continuous integration, TDD, encapsulation, loose coupling, and so forth is just not profound if you're writing a 50-line bash script for your own consumption. This is one reason why I think <a href="http://steve-yegge.blogspot.com/2007/12/codes-worst-enemy.html" target="_blank">Steve Yegge's claim that size--not poor design--is code's worst enemy</a> is actually quite profound.

Setting aside the way scale affects processes and teams, think about what it does to product.

If you've ever tried to apply a design that works well at one scale to a problem domain that's a couple orders of magnitude different, you know that often, scaling is far more difficult that a simple linear calculation.

Grep is a great tool for finding text in files. It can crunch through all the files in a directory in a second or so, and all the files on my hard drive in a handful of minutes. But using grep to search all the documents in a company's archives is impractical.

A traditional enterprise search product is also a great tool for finding text in files. It's too cumbersome to set up to do the quick-and-dirty, small-scale work of grep, but it comes into its own when you need to find all emails sent by a company in the past decade that might be relevant to a lawsuit.

Enter big data...

Google's indexing of the internet is essentially a scaled-up, incredibly sophisticated, optimized version of traditional enterprise search. Last I heard, over 4 million (!) servers were behind www.google.com, servicing the queries that all of us feed it. It's impressive--miraculous, even--how effective the Google service (and Bing, and other competitors) has managed to be. I don't have major complaints about the user experience.

But it's the wrong architecture for internet scale. We're paying way too much for power and hardware to keep these sites running; we need something radically different, which is why technologies like the one I helped productize at <a href="http://www.perfectsearchcorp.com" target="_blank">Perfect Search</a> are the wave of the future. Perfect Search can sustain query speeds that are hundreds or thousands of times faster than a traditional index; sooner or later, the world will figure out that that matters.

<strong>Use better scaling assumptions</strong>

The next time you have to plan for a scale that's well outside original tolerances (whether that scale has to do with numbers of machines/threads/events, or with size of deployment, or whatever), try using the <a class="zem_slink" title="Pareto principle" href="http://en.wikipedia.org/wiki/Pareto_principle" target="_blank" rel="wikipedia">80:20 rule</a> instead of a linear formula as your guide: the 20% of the cases at the high end of what you're targeting will take 80% of the effort to address correctly. Recurse: of the 20% at the high end, 80% of those cases might be handled by a modest adjustment of the design, but 20% need a radical improvement. And recurse again.

I don't think there's anything magical about 80:20; maybe a simple exponential function is easier and more accurate. Or maybe you have a stair-step progression. Or maybe you simply can't progress to the higher scale at all, because money or physics or some other factor imposes a hard limit that no amount of hand-waving will overcome.

Bottom line: part of your job as a designer/architect is to understand these issues, wrestle with them, and provide a balanced roadmap that anticipates the best all-around compromises.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Analyze the amount of RAM, CPU, or disk that your program uses at several different scales. Is the curve linear, exponential, logarithmic, a stair-step? What does this tell you about business goals like selling to bigger customers?</span></em></p>

<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://spinnakr.com/blog/ideas/2012/12/three-big-economic-fallacies-behind-growth-hacking/" target="_blank">Three Big Economic Fallacies Behind Growth Hacking</a> (spinnakr.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://dead-logic.blogspot.com/2012/12/path-of-critical-thinker-meow.html" target="_blank">Path of a Critical Thinker (Meow)</a> (dead-logic.blogspot.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://pandodaily.com/2012/12/12/what-fred-wilson-and-the-vcs-dont-get-about-advertising/" target="_blank">What Fred Wilson and the VCs don't get about advertising</a> (pandodaily.com)</li>
</ul>

---

dougbert (2012-12-19 10:23:44)

good presentation on a principle that I have seen and encountered for 30 years. Though back in the day, 1 MEGA byte of RAM was a big constraint.  Several projects I worked on, trying to get management to understand that last 20% was NON-LINEAR was a huge (if not a NP) issue.

---

Andy Lawrence (2012-12-19 09:18:10)

Nice article. Scale means everything to the project I am working on. I have to be able to handle billions of data items in a fast, efficient manner. The software has to be able to break a problem apart so that it can be processed in parallel. The system architecture, the algorithms used, and the data structures used must be designed from the ground up with scaling in mind.

But when people talk about scaling software, they might be mixing up terms. In my blog "How Does It Scale?" at DidgetMaster.blogspot.com I discuss three different dimensions of scaling. While related, they are not the same. Your article touches on a couple of them.

---

Daniel (2012-12-19 09:35:40)

The article at didgetmaster is excellent; thanks for the link, Andy.

One aspect of scaling that I totally ignore here, but that you mention (by implication), is scaling *down*. In our rush to get bigger and faster, we sometimes overbuild. Didgets is that rare combination that can play in the world of big data, yet still be super practical at the micro scale. Nice! That's not very common in enterprise software, and I've come to recognize it as the mark of a truly fundamental advance as opposed to lipstick on a pig.

---

posicionamiento web (2013-03-05 07:58:47)

I simply couldn't leave your web site without saying that I loved the useful information. I'm going to be back regularly to check up on new posts.

---

Daniel Hardman (2013-02-01 08:14:57)

Your comment about "back in the day" leads me to make another connection: if the scale of resources that modern computers consume is so dramatically higher than it used to be, I wonder whether the complexity of the software we're building is drastically different as well. We programmers might be like the proverbial frog that's boiled by swimming in water as it heats on the stove--not noticing how much tougher it's getting to produce good stuff. Perhaps industry best practices like TDD and continuous integration, and better foundational libraries, are providing enough compensation to mostly compensate...

---

2 Surprising Truths About The Iron Triangle | Codecraft (2013-07-01 16:39:07)

[…] You’ll create virtuous cycles that perpetuate the right kinds of tradeoffs for performance, scalability, and […]