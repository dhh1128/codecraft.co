---
title: Flexibility is No Virtue
date: 2012-10-17
slug: flexibility-is-no-virtue
---

<blockquote><em>Vice is a monster of so frightful mien,
As to be hated needs but to be seen;
Yet seen too oft, familiar with her face,
We first endure, then pity, then embrace.</em>
<p style="padding-left:30px;">—<a class="zem_slink" title="Alexander Pope" href="http://en.wikipedia.org/wiki/Alexander_Pope" target="_blank" rel="wikipedia">Alexander Pope</a>, <em><a class="zem_slink" title="An Essay on Man" href="http://en.wikipedia.org/wiki/An_Essay_on_Man" target="_blank" rel="wikipedia">Essay on Man</a></em></p>
</blockquote>
If I had a penny for every programmer that I've heard, proudly touting the flexibility of what they've built, I'd be a wealthy man. I might even be able to afford my teenagers' car insurance. :-)

As a young coder, I took the implied excellence of flexibility for granted; after all, who wouldn't want to be flexible?

Now I know better.

If your software can be installed and configured a hundred different ways, this is <strong>Not Good</strong>. It is a sign that you don't know who your customer is, or what they want. If your programming language has nine separate functions that provide the same functionality, shame on its designers. If your UI presents users with oodles of choices and calls it a customer focus, go vomit into the nearest garbage can.

<figure><img class=" " src="http://upload.wikimedia.org/wikipedia/commons/thumb/1/15/3rd_Battalion_3rd_Marines_Osprey_flights.jpg/640px-3rd_Battalion_3rd_Marines_Osprey_flights.jpg" alt="" width="480" height="249" /><figcaption>V22-Osprey -- an unusually flexible aircraft. Photo credit: Sgt. Mike Fayloga (Wikimedia Commons)</figcaption></figure>

I can already hear the protests, so let me pause here to admit <!--more-->that my generalization isn't true 100% of the time. The Department of Defense spent billions of dollars developing the Osprey, because it really did want Marines to be able to take off and land like a helicopter or a plane, according to changing circumstances. And the DOD was not crazy.

This post is not about that kind of flexibility.

It's also not about the flexibility in construction that you address with modular designs. The set of objects you can build with legos is unbounded--flexible, if you will. But notice that the blocks themselves are not.

This post is about products that can be deployed and configured in a thousand permutations, when the reasons and the costs for that flexibility are not understood or acknowledged. <em>That</em> kind of flexibility pushes problem-solving onto the customer's plate (and QA's plate), and is usually laziness in disguise. Yet we tell ourselves it's a virtue so often that we start to believe it.

<strong>Cement as a poster child</strong>

When you pour cement to make a driveway, you value the pliable nature of the material just long enough to get it to fit your form. Ninety minutes of flexibility must be followed by decades of perfect rigidity, or you'll never buy from that cement maker again. You couldn't care less that the cement you purchased could be made to fit the shape of your neighbor's sidewalk, or of the basketball court at the park.

Think about that for a minute.

In the long run, does a customer value the ability of a "flexible" product to meet the needs of <em>any</em> configuration other than the one she needs? No! (It is possible that she will configure a single product in multiple ways on different hardware or at different points in time, but this is the exception that proves the rule. Even when reconfiguration is important, the customer will view it as a necessary evil that increases cost and bother--not as a delightful business enhancer.)

As with cement, once a customer gets things configured correctly, he is guaranteed to prefer "set it and forget it" to an experience where he can experience the wonders of your product's flexibility over and over again.

<strong>The cost of flexibility</strong>

The <a class="zem_slink" title="Bell Boeing V-22 Osprey" href="http://en.wikipedia.org/wiki/Bell_Boeing_V-22_Osprey" target="_blank" rel="wikipedia">MV-22 Osprey</a> makes a great cautionary tale. It took <em>much</em> longer to test, and was <em>far</em> more expensive to develop, than <a href="http://www.nytimes.com/2011/11/20/us/costly-osprey-symbol-of-fight-to-cut-pentagon.html" target="_blank">originally expected</a>.

Flexible software is no different.

But suppose, just suppose, we were perfect estimators, and we could tally up exactly how many dollars and hours we would spend on releasing something flexible... Suppose we did the analysis, even including a savvy assessment of opportunity cost, and decided it was worth it...

We still wouldn't be counting the cost accurately.

Besides the cost of developing and testing the Osprey, and the cost of purchasing models as they roll off the assembly line, the Department of Defense incurs an ongoing cost <em>to the Osprey's users</em> in terms of extra training time, more limited deployment theaters, less skill transfer for pilots and maintenance crews when they retire to civilian life, and so forth.

Again, flexible software is no different.

<strong>Rational self-interest and the invisible hand</strong>

If you want to sell into a varied market, you have to tolerate variety. Dev teams that make flexible products are attacking that problem, and they are behaving in a mostly rational fashion.

Does that sound like I'm contradicting myself?

I don't think so. It all hinges on understanding whose interests are being served by flexibility.

<em>Flexibility serves the self-interest of the ISV</em>. In most cases, customers would be delighted if products shipped pre-configured for exactly their needs, with no flexibility at all. They'd gladly accept a pre-fitted driveway, delivered by an invisible hand.

In other words, flexibility in a product's configuration is a necessary evil.

If it's necessary at all...

Theoretically, products could ship with smart defaults (so they'd require little tweaking), and could adjust themselves to unique needs with little effort on the part of customers. In some cases, they could even make these changes automatically and instantaneously, on deployment. Think about how much less doc we'd have to write, and how much less support we'd have to provide, if we didn't buy into the flexibility approach...

I know I'm being idealistic. But it seems to me that we should acknowledge who's benefitting from flexibility, and what it's costing. We should make easy and correct fit, rather than flexibility, the ideal for our customers, and do what we can to achieve it. We may always be stuck making things flexible for our own internal purposes, but that should be our problem, not the customer's.
<p style="padding-left:30px;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Study the "<a href="http://www.antipatterns.com/arch_cat.htm" target="_blank">Swiss Army Knife" and "Cover Your Assets" antipatterns</a>. These antipatterns are often associated with an incorrect admiration for flexibility. Look for places in your world where these antipatterns are used.</span></em></p>

<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://dl.acm.org/citation.cfm?id=1620482" target="_blank">"Weighing the Benefits and Costs of Flexibility in Making Software"</a> (Information Systems Research)</li>
</ul>

---

The Power of Simplicity &laquo; Codecraft (2013-02-15 08:56:51)

[...] And all the planning that built those features? They’re symptoms of a problem, not solutions. Nobody really wants a shopping cart framework with 10,000 configuration options; they want to sell in a way that delights and engages customers. (Okay, I guess some software [...]

---

Daniel Hardman (2015-09-22 12:44:07)

The more time goes by, the more I see this phenomenon everywhere. I don't think it's necessarily wrong to *start out* building in a lot of configurability; we might need it while we learn what's the right set of tradeoffs in the early days of our products. But once we have some experience in the field, we will eliminate some of the configuration options, in favor of "hardened" features. By then we should know that "give" in those places is counterproductive.

---

David H (2015-09-09 19:29:51)

Wow you hit on another hot-button topic for me. Super-configurable flexibility really benefits most the ISV salesperson who gets paid when the deal is signed, not when the customer is happy nor when the company makes a profit. It's about attempting (vainly) to be all things to everyone. "It is a sign that you don’t know who your customer is, or what they want." -> Nailed it.



---

David H (2015-09-23 07:01:04)

Have you ever seen configuration options removed from a product in real life? Maybe it can be done. I think it would help if it was explicitly stated up front, internally and externally "this product is in Beta and some configuration options will be removed in the future as we gain experience", or something to that effect.

---

Daniel Hardman (2015-09-23 10:16:49)

>>Have you ever seen configuration options removed

@David: it's a very astute question. The short answer is: "almost never". But at least I can hedge with "almost"... :-) You've made some wheels turn in my head about why it should be so hard to eliminated config. I'm pondering...