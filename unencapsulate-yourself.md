---
title: Unencapsulate Yourself
date: 2012/10/22
slug: unencapsulate-yourself
---

<figure><img alt="" src="http://farm4.staticflickr.com/3040/2998411234_ceb9e6f752_n.jpg" height="320" width="212" /><figcaption>We loved to escape the boxes when we were kids... Photo credit: thewoodenshoes (Flickr)</figcaption></figure>

If I had to make a "top 5" list of foundational tools in software development, <em><a class="zem_slink" title="Encapsulation (object-oriented programming)" href="http://en.wikipedia.org/wiki/Encapsulation_%28object-oriented_programming%29" target="_blank" rel="wikipedia">encapsulation</a></em> would certainly make the cut. It's a major enabler of abstraction; it's what makes conceptual complexity tractable.

Recognizing its importance, most modern programming languages encourage encapsulation in one way or another. For example, languages friendly to <a class="zem_slink" title="Object-oriented programming" href="http://en.wikipedia.org/wiki/Object-oriented_programming" target="_blank" rel="wikipedia">OOP</a> lead coders to think about the world in terms of well encapsulated objects and the messages they pass.

I'm a big fan of encapsulation.

But if you never leave your boxes, you miss half the fun.

<strong>Layers and silos</strong>

As cells grow into tissues in biology, so similar objects in an OOP mindset often coalesce into horizontal layers composed of entities with compatible composition and duties. These strata get names: "the business logic layer", "the display layer", "middleware", "core engine", and so forth. If you've worked on anything MVC or n-tier or client-server, you know this mindset.

Less commonly, objects align on a vertical axis, producing semi-independent silos that span layers to produce decoupled top-level features. An optional accounting module that has its own db and middleware might be modeled as an independent stack in a vertical architecture. <a class="zem_slink" title="Aspect-Oriented Programming" href="http://www.techopedia.com/definition/204/aspect-oriented-programming-aop" target="_blank" rel="techopedia">Aspect-oriented programming</a> also spans layers, though in a less siloed way.

In either case, <a title="Why People Are Part of A Software Architecture" href="/2008/06/25/why-people-are-part-of-a-software-architecture/">the boxes you draw to model your architecture tend to correspond to teams</a>, and those teams tend to use different tools and processes, and those differences tend to isolate rather than converge organizations.

This is a problem.

<em>You should encapsulate code. People, not so much.</em>

<strong>Generalists and specialists</strong>

Specialists have their place. But if your dev organization is overly skewed toward specialists <!--more-->in each architectural box, it is not healthy. To understand why, join me in a thought experiment.

Bob is sick. He'd like to get some help. But he happens to live in a society where the health care system consists entirely of otolaryngologists and endocrinologists and neurosurgeons. He has no <a class="zem_slink" title="General practitioner" href="http://en.wikipedia.org/wiki/General_practitioner" target="_blank" rel="wikipedia">general practitioners</a> to listen while he paints a picture with broad brush strokes--nobody who will triage and cut to the chase.

You can imagine what happens next. Bob visits one specialist, but the specialist sees Bob's problem as only intersecting 20% with her particular expertise. Wanting to be sure she's not sued for malpractice, she recommends that he consult with another specialist as well. Bob makes another visit, and gets another referral. After half a dozen trips, he's now explored 100% of his symptoms, and he has a set of diagnoses and prescriptions that theoretically address his problem. However, nobody has examined the picture in the aggregate, looking for redundancy or incompatibility. Instead, nurses have been on the phone to other offices, and faxes and charts have passed back and forth like ping-pong balls, with uncertain results. Bob has spent so much money and accumulated so many complex recommendations for a cure that he's a bit bewildered. And it's taken a large amount of time.

Organizations that encapsulate people into layers or silos map nicely onto this thought experiment. If you want to build a new feature, or fix a bug, you ping-pong around to various specialists, trying to get a straight answer. Communication by document is the norm; people blame poor internal docs for design oversights. Estimates are high, mainly due to concern about touch points between layers. Use cases are written in terms of a horizontal layer; nobody seems to remember that the top of the stack is the entire universe as far as the user is concerned. Specialists don't trust one another's diagnoses. Fiefdoms proliferate; ambassadors may negotiate treaties, but political tensions are high. When time comes to actually implement the feature or the fix, you see an inordinate amount of baton-passing, cross-checking, critical-path'ing, and hand-wringing. These orgs struggle with integration (usually vertical) testing, since it doesn't map well onto the scope of concerns of any incorporated entity; even in the best of cases, they have a hard time identifying the highest-value test cases, since team walls limit insight into risk.

Give me a proactive, first-class generalist in a silo'ed or layered org, and I will give you a high-leverage change-maker that's a linchpin for company success. They will be invited to every meeting (although they won't succumb to death by meeting, if they're smart.) They'll cut through ambivalence, see the big picture, and make smart tradeoffs. They'll lubricate the cogs of the machine in a way that an equally smart, but siloed, technical pro cannot.

<strong>Pendulums</strong>

I'm not saying that everybody should be a consummate generalist; the pendulum can swing too far. Medicine needs pediatric allergists, and software needs the cube warrior who can make gdb sing on AIX on an RS-6000 like nobody else on the planet. But it's telling that you can't specialize in medicine until after you've satisfied general requirements for a medical degree.

If your software teams are overly siloed, consider instituting some cross-training. Start measuring how often a single person can solve a bug all the way up and down the stack. Incent your best engineers to learn to speak another team's language; maybe loan a few to another scrum team from time to time.

If you're an engineer, unencapsulate yourself.

Thinking outside the box pays big dividends.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Identify one way that you can learn something about the problem domain of a team other than your own. Pay the price for that learning. Then put your investment to good use.</span></em></p>

<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://dailyjs.com/2012/09/17/encapsulation-breaking/" target="_blank">Encapsulation Breaking</a> (dailyjs.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://philcrissman.com/2012/08/26/touching-the-stove/" target="_blank">Touching the stove, broken glass, and other people's mistakes</a> (philcrissman.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://architects.dzone.com/articles/breaking-ioc-containers" target="_blank">Breaking Up with IoC Containers</a> (architects.dzone.com)</li>
</ul>

---

Konstantin (2012-10-23 15:27:18)

I generally agree with your point, so just wanted to know how unusual your ideas are for the market of your country.
So thank you for the answer!

As for my experience, I can't imagine myself to be a really narrow-interested developer. There are the things that I am payed for (and they are not always challenging, sometimes just a routine with no adventure). 
And on the other hand there are some areas that I would like to investigate deeper but these areas are of quite academic sense (e.g. compilers, syntactic analyzers etc). And trying both directions to be satisfied makes me feel that I can do something :) I guess it is quite normal situation.

PS. A funny thing: in Russia the analog of "jack of all trades" (which sounds like 'all-hands master') has a positive connotation. So it makes sense to think positively :)

---

Konstantin (2012-10-23 14:02:21)

A really thoughtful post. But actually I thought that in both Europe and America it is more usual (and considered to be just better) to be a narrow-specialized engineer. Is it true?

---

Daniel (2012-10-23 14:20:52)

Good question, Konstantin. I think specialization is indispensable. You have to get really deep at a few things. It is impossible to be super deep in everything, and if you dilute your expertise and energy too much, you can become what English speakers call "jack of all trades, master of none." However, sometimes I have seen specialists get too comfortable in their narrow world, without understanding how their narrow focus imposes costs on the larger organization. It has been my experience that a specialist with a good, broad foundation is more valuable than a specialist that can't see the larger picture. It is also the case that organizations suffer if they don't have a certain percentage of very competent generalists to translate and facilitate.

In my own career, I have chosen to get very, very deep on topics like text processing, internationalization, and all things related to language and computers, due to my graduate studies in linguistics. I am moderately deep on topics like RESTful web services, database theory, and web UI. On many other topics, I am just deep enough to do journeyman bug fixes and to understand estimates, but not to solve subtle and multivariate problems.

Each engineer has to choose his or her own preferred balance, but I believe having some breadth is healthy, even if you prefer to operate mostly as a specialist.