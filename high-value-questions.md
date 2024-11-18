---
title: What makes high-value questions?
date: 2012/06/20
slug: high-value-questions
---

<a href="http://www.perfectsearchcorp.com">Perfect Search</a> (where I used to work) makes a search engine that performs/scales orders of magnitude better than competitors like Solr/Lucene with hadoop, FAST, Autonomy, and Google Search Appliances. This makes them a best-of-breed tool for many big data problems. They can do on one box what it would take competitors an entire rack of hardware to pull off. And usually that one box still runs an order of magnitude faster.

[caption id="attachment_369" align="aligncenter" width="500"]<a href="../../../wp-content/uploads/2012/09/6637427465_2fb4695630.jpg"><img class="size-full wp-image-369" alt="semantic network for "big data"" src="http://codecraft.co/wp-content/uploads/2012/09/6637427465_2fb4695630.jpg" width="500" height="500" /></a> photo credit: metaroll (Flickr)[/caption]

Despite the compelling value, sales have ramped more slowly than Perfect Search would like (ain't it always the case...). Some reasons have to do with marketing, but I've recently had another insight that feels compelling to me.

My insight is this: <em>high-value questions demand insight, not fact retrieval</em>.

This might seem like old hat. After all, there's a reason why business intelligence is a market segment unto itself, and why <a href="http://thetrendpoint.com/2012/04/ibm-betting-big-bucks-on-data-analytics-software/" target="_blank">IBM is betting its corporate future on analytics</a>. I think BI is going after the right kind of thing, but a lot of that community has lost its way and become little more than glorified reporting.

Here's why.

<strong>Question categories</strong>

Questions that are interesting in the information age have answers that fall into three broad categories:
<ul>
	<li><strong>Unknowable</strong></li>
	<li><strong>Known</strong></li>
	<li><strong>Discoverable</strong></li>
</ul>
<em>Why is chocolate so awesome</em>? <strong>Unknowable</strong>.

<em>What is the population of Bangladesh</em>? <strong>Known</strong>.

<em>How can I sell more widgets to housewives between the ages of 25 and 40</em>? <strong>Discoverable</strong>.

For structured data, the preferred way to get known answers is a DBMS (or a noSQL DB, maybe). For unstructured data, Google's full text indexing is state-of-the-art (and Perfect Search's is a quantum improvement). But nowadays, looking up known answers is passé. The world needs tools to do it, but the technology is not especially interesting.

<strong>Do our BI tools discover anything?</strong>

The central value proposition of big data is inseparably connected to <strong>discoverable</strong> answers. <em>These gems are fundamentally different from facts waiting to be sliced; they're rational guesses based on deduction and supported by rigorous data analysis.</em>

In other words, if we're not building big data solutions that hypothesize rather than report, we're underdelivering. We call it <em>data science</em>, right? Isn't the scientific method all about hypotheses and testing?

Business intelligence products and services that show pretty dashboards or reports are not really delivering insight; they're exposing information and depending on the human intelligence in the minds of the users to provide the hypotheses and analysis that turns it into insight. Sometimes that happens, if a graph shows something interesting and noteworthy--but a lot of times, minutiae overwhelms, and BI is a waste of the customer's money.

Enterprise search struggles, as an industry, because it's trying to sell drill bits to customers who want holes, and it's forgotten that it's the hole, not the bit, that makes the customer passionate (thanks Zig Ziglar for the analogy). In other words, it is also depending on the customer to provide analysis that turns data into insight.

<strong>A new kind of big data technology</strong>

We can do better.

I propose a new kind of data analytics product/process/service that implements the scientific method on big data. <a href="https://docs.google.com/presentation/pub?id=1zz4sq1924gfbs4734h4Tc0oKkhXkbitF1iyF07dwhxo&start=false&loop=false&delayms=3000" target="_blank">Click here</a> for an overview presentation.
<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://blog.neolane.com/conversational-marketing/big-data/" target="_blank">Transforming Big Data Into Actionable Insight [Infographic]</a> (neolane.com)</li>
	<li class="zemanta-article-ul-li"><a href="making-sense-of-big-data-and-its-role-in-your-business.md" target="_blank">Making sense of big data and its role in your business</a> (itproportal.com)</li>
</ul>