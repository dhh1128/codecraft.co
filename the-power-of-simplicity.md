---
title: The Power of Simplicity
date: 2013/02/15
slug: the-power-of-simplicity
---

Most stories about zen masters, gurus, or other paragons of wisdom follow a similar pattern. The pupil discovers a problem. He or she struggles with it. The problem gets more and more overwhelming. Solutions are elusive. Finally the pupil goes to the master and pours out his heart, whereupon the master offers a pearl of insight that radically reinterprets the problem.

[caption id="attachment_989" align="aligncenter" width="500"]<a href="http://www.flickr.com/photos/departingyyz/6858912596/"><img class="size-full wp-image-989 " alt="Seek the simple... Photo credit: departing(YYZ) (Flickr)" src="http://codecraft.co/wp-content/uploads/2013/02/screen-shot-2013-02-14-at-10-12-29-pm.png" width="500" height="330" /></a> Seek the simple... Photo credit: departing(YYZ) (Flickr)[/caption]

There's a reason why this narrative exists in every culture: human beings need the insight that comes from synthesis, pared down to its essence. We crave the simple but profound:
<ul>
	<li>Less is more.</li>
	<li>Do unto others as you'd have others do unto you.</li>
	<li>A watched pot never boils.</li>
	<li>Freedom isn't free.</li>
</ul>
The software industry desperately needs this sort of insight, but far too often I see us operate in the stage of the narrative where the pupil misunderstands the problem, struggles, and makes things worse. <!--more-->This is true of all sorts of software--even mobile apps and consumer web sites--but I'm especially thinking about enterprise stacks. The architectures that I encounter today are significantly more complex than the ones I drew on whiteboards a decade ago. Applications used to consist of a binary and a handful of config files. Now they consist of hundreds or thousands of artifacts: executables, shared libraries, plugins, parsers, databases, triggers, stored procedures, data sets, documentation, brandable CSS, image libraries, drivers, rule sets, comm channels... Products have more features--<em>way</em> more. We sneer at offerings that aren't <em>solutions</em>. We build federated, distributed, loosely coupled fabrics that run in sophisticated clouds and that abstract physical geography, hardware, network interconnects.

We aren't as troubled by this complexity as we should be. All those features we're building into a product? And all the planning that built those features? They're <em>symptoms of a problem</em>, not solutions. <a title="Flexibility is No Virtue" href="../../../2012/10/17/flexibility-is-no-virtue/">Nobody really wants a shopping cart framework with 10,000 configuration options</a>; they want to sell in a way that delights and engages customers. (Okay, I guess <em>some</em> software really does make people happy with greater complexity. Photoshop has 10,000 menu items, and its power users love it. Perhaps this is because it enables enables human creativity and passion, and creativity thrives on possibilities. I don't think most software is like this...)

We imagine we're going to outrun all this complexity with kaizen. We'll get smarter, adhere more to agile methods, use more efficient tools, double down on use cases, or implement some other technique <em>du jour</em>. And we're not crazy--there are gains to be had, and they're important. Continuous integration kicks out dozens of builds per hour. Product management teams accomplish feats of planning, coordination, and analysis that would have caused jaws to drop a few years back. Test automation is light years ahead of where it was when I first did a handoff with a tester. The amount of data that we index, transform, and marshal to achieve business purposes grows at an astonishing rate.

But in the zen master stories, the pupil never wins through sheer grit.

<a href="https://www.adaptivecomputing.com/simiplicty-clouds-hidden-value-proposition/" target="_blank">On my work blog at Adaptive Computing, I posted an article</a> about how I think the entire cloud computing community misunderstands the true emotional motivation of its customers. IT folks who buy cloud management software may say that they want "cost savings" and "increased agility"--and I think that's accurate--but they also want simplicity. They want it in the worst way, even if they don't articulate that desire, don't measure it, and don't use it to justify purchase decisions.

IT is <em>drowning</em> in complexity.

If you want to be a zen master, don't give them 20 more menu items in the next release. Give them a release where 20 menu items become unnecessary.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">For a week, spend 2 minutes per day imagining ways to simplify. Incremental improvements are good, but also push yourself to think more radically. Could you deliver your product in a new way that totally obviates the need for an install, instead of just making the install easier? Instead of making two components talk more robustly through web services, could you collapse a process boundary altogether? Instead of integrating with a third-party app, could you throw away 1/3 of your product and simply use that app to get the job done?</span></em></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">I will be blogging more about how to simplify in coming weeks, and would be very interested in your thoughts on this topic. Please comment.</span></em></p>

<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://java.dzone.com/articles/why-scrum-won" target="_blank">Why Scrum Won</a> (java.dzone.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://www.theenterprisearchitect.eu/archive/2013/01/05/a-tale-of-a-7-year-journey-in-developing-software-for-the-enterprise" target="_blank">A tale of a 7 year journey in developing software for the enterprise</a> (theenterprisearchitect.eu)</li>
	<li class="zemanta-article-ul-li"><a href="http://www.hispanicbusiness.com/2013/2/7/ibm_simplifies_big_data_cloud_computing.htm" target="_blank">IBM Simplifies Big Data, Cloud Computing</a> (hispanicbusiness.com)</li>
</ul>

---

trevharmon (2013-02-15 11:42:58)

This is one of those phenomenon I've noticed, as well. In fact, I've spent quite a lot of time trying to understand the reasons behind it in what may be a misguided effort. I think if I can understand the cause, I can fix it. Here are some of the reasons defending complexity:

- Everyone else is doing it --- That argument didn't fly when I was a kid, so I don't see why it's valid now.
- Customers are demanding new features --- Maybe they are, but that doesn't necessarily mean those features should be enabled if they increase complexity. In my experience it's the edge cases that create the most complexity.
- Flexibility is more important than usability --- This is a philosophical debate, and I admit I fall into different camps depending on the circumstance. However, I'm always for simplicity.
- We prove how smart we are by making something complex --- No one ever says this one out loud, though I've seen it implied a number of times. There's an unfounded fear the finesse of a simple approach will hide the creator's brilliance. Oddly, usable simplicity is far more difficult to achieve than complexity. Anyone can make something more complex.

Now, assuming one provides a product and is not a bespoke services shop, I think I comes down to one of two things: fear or greed. Making something simple means one knows and understands their target customer, which by its very definition means one has limited the customer base. A simple to use product is not going to do everything any possible user may want. So, one is either fearful the simple to use product will overly limit the customer base or just plain doesn't want to limit it in any way. So, one falls into the trap of trying to make it work for everyone. Complexity rears its ugly head.

The trick is to truly know your one's customers and allow the product to be no more complex than is absolutely needed for their needs. That's why Photoshop works for some but is far too complex for the majority of digital camera owners.

Too bad it seems everyone feels compelled to build the IT equivalent of Photoshop.

---

Daniel Hardman (2013-02-15 15:18:40)

As always, I learn something from your thoughtful comments, Trev. I had not seen, before, such a clear summary of the "prove how smart we are" problem.

One of the reasons why I'm attracted to biology as a metaphor and guiding light for software is that life does incredible--perhaps "awe-inspiring" would be even more apt--things with complexity. The amount of complexity in something as "simple" as a single cell, or even a single strand of DNA, is mind-boggling. And yet that complexity is all encapsulated behind layers and layers of interfaces that allow us, at any given level of detail, to describe and predict interactions in useful ways. We can make sweeping generalizations at the level of an organ, an individual, or even an ecosystem, and find that those generalizations hold true, and allow us to manage with confidence. The system doesn't degenerate into chaos, even at levels of complexity many orders of magnitude beyond a single cell. I would like to be able to say the same about software, but although I see hopeful signs here and there, I think we're nowhere near as good as biology at making the complexity tractable.

---

Daniel Hardman (2013-02-19 12:42:51)

I hadn't thought about it in quite those terms before, Andy, but you're totally right. One more reason for Didgets, which in some ways has the same vision as the old "winfs" idea that MS used to talk about -- describe data in robust and general-purpose ways that provide efficient searching -- without imposing lots of burden on the data due to the particular application that's using it.

---

Andy Lawrence (2013-02-19 10:48:30)

It is not just software and systems where increased complexity has become the norm. Data itself is increasingly "locked" into very complex and proprietary formats. Instead of keeping data in its "raw" format and devising several different ways to view that data, the data itself is being wrapped in a ton of markup, imported into databases, or split into other kinds of separate systems. Such systems make it hard to extract out the original data in order to perform new and interesting functions against it.

---

6 Strategies to Simplify Software | Codecraft (2013-03-12 08:57:20)

[...] written that simplicity is powerful, and that it undergirds many deep architectural breakthroughs. In posts about pragmatism and [...]

---

My First Tangle With the Tower of Babel | Codecraft (2013-04-26 08:48:31)

[...] think the answer may lie in finding new accommodations for all the complexity we wrestle. New ways to think about concurrency, distributed architectures, object lifecycle, and [...]

---

Why Your Software Should Cry | Codecraft (2013-05-06 11:50:48)

[...] in a good script with a few lines of code. However, if we want to truly master the bewildering growth of complexity in the universe of bits and bytes, we need pain. And we need to pay attention to [...]

---

Why you should be proficient in a tool like vim or emacs | Codecraft (2014-05-15 08:46:17)

[…] I claim that if you only ever see the complexity of software engineering through the lens of an IDE, you have missed an important–even revelatory–learning […]

---

A grumble about buckets | Codecraft (2015-04-08 13:39:21)

[…] Sometimes developers limit the choices that are offered to their users as a way to simplify. This can be a good thing; I’m a big fan of simplicity. […]

---

On Forests and Trees | Codecraft (2015-09-02 08:48:39)

[…] unremarkable. It’s among the human mind’s most powerful techniques for coping with complexity, and it’s a hallmark of vigorous thinkers in any technical discipline. I like what Hegel […]