---
title: Paying Off Technical Debt
date: 2012/10/14
slug: paying-off-technical-debt
---

[caption id="" align="alignright" width="213"]<a href="http://www.flickr.com/photos/alancleaver/4105722502/"><img alt="" src="http://farm3.staticflickr.com/2785/4105722502_a442444bb9_n.jpg" height="320" width="213" /></a> We don't get spam about how to consolidate our technical debts. :-) Image credit: Alan Cleaver (Flickr)[/caption]
<blockquote><em>“Interest never sleeps nor sickens nor dies; it never goes to the hospital; it works on Sundays and holidays; it never takes a vacation; it never visits nor travels; it takes no pleasure; it is never laid off work nor discharged from employment; it never works on reduced hours. . . . Once in debt, interest is your companion every minute of the day and night; you cannot shun it or slip away from it; you cannot dismiss it; it yields neither to entreaties, demands, or orders; and whenever you get in its way or cross its course or fail to meet its demands, it crushes you.”</em>
<p style="padding-left:30px;"><em>— <a class="zem_slink" title="J. Reuben Clark" href="http://en.wikipedia.org/wiki/J._Reuben_Clark" target="_blank" rel="wikipedia">J. Reuben Clark</a></em></p>
</blockquote>
In my recent post about <a title="Coping With Organizational Alzheimers" href="/2012/10/12/coping-with-organizational-alzheimers/">how organizations forget technical debt</a>, I glossed over some important details. When you're in debt, you have an obligation to pay somebody back. So: <em>with technical debt, who must you pay, and how?</em>

<strong>More than just a code problem</strong>

A simplistic view--one that I've used for years--understands debt mainly as a deficiency in code. In this view, you pay yourself back by making the code better. Most discussions about technical debt take this view. It's natural, and true, and useful.

However, I don't think it's the full story.

It's good practice to borrow money from yourself. If you do things this way, you save a bunch of capital, and then you borrow against your own reserves. Paying yourself back consists of transferring money back into your own savings.

This is hard, and making large purchases this way requires years of prior planning and discipline.

A more common way to borrow is <!--more-->to use your future capital as collateral, and to borrow from an external lender. I think this is how most technical debt is incurred. (<a class="zem_slink" title="Technical debt" href="http://en.wikipedia.org/wiki/Technical_debt" target="_blank" rel="wikipedia">Technical debt</a> incurred against your own reserves implies engineers working nights and weekends to get <em>ahead</em>, so they can take a vacation without a schedule slip. This happens, but not on a large scale.)

<strong>Who is your lender?</strong>

When you ship code that does things in a compromised, kludgey way, you acquire revenue that you can't afford to pay for yet. Your loan is crowd-sourced:
<ul>
	<li>Your support and professional services organizations will have to guide users through workarounds and corner cases that you don't handle well. Your doc and user experience experts will do the same.</li>
	<li>Your marketing organization will have to nuance how they message your feature.</li>
	<li>Your sales force will need to be careful to qualify leads in a way that prevents frustrated customers and wasted POCs.</li>
	<li>Your product management team will have to understand that any release that builds on your kludge will be more expensive in the next release.</li>
	<li>Executives live with a watered-down strategic advantage. Normally, a unique feature also implies a unique capability in a dev team--but to the extent that you short-circuit correct development, you also short-circuit your own learning, and live with a deficient mental model of your problem domain. Executives marshal forces for battle not only having caveats to their super duper blaster, but also having a staff of scientists that <em>don't have experience building</em> super duper blasters.</li>
	<li>Your customers' enthusiasm gets diluted.</li>
	<li>Your dev and QA staff lose expertise and pride of ownership, and they have to spend energy on sub-optimal work that they'll later replace. (Notice that I put this last. This is the one most tech folks understand, but I think it's often overshadowed by other, less obvious problems.)</li>
</ul>
<strong>Don't forget the interest</strong>

As with financial borrowing, the cost of your technical debt compounds over time. The longer a kludge remains, the higher the chances that customers will find out, callers of an API will depend on its quirks, and tests will become brittle to a change. See quote by J. Reuben Clark.

<strong>When you must...</strong>

Despite all these disadvantages, sometimes debt is the only way forward. Few can afford to pay cash for their first house, and few companies have a large war chest of unused technical assets that they can shift into the next release whenever they feel inclined. But if you borrow, keep these two simple rules in mind:
<ol>
	<li>Your lenders should agree to the terms of the loan.</li>
	<li>You need a way to account for the debt and track its paying off.</li>
</ol>
In my experience, most problems with technical debt stem from one or both of these rules being ignored.

Regarding rule #1: engineering organizations need to be proactive about communicating these issues. And product managers need to be technical enough and savvy enough to take indebtedness seriously. I once had a product manager tell me that some refactoring work on a particular feature was unacceptable; I should be spending every last ounce of my energy on building new features. This was a communication failure on my part, because I hadn't made it crystal clear that refactoring was a precondition to most of the new features he valued. (Stay tuned for a post about the temptation of short-range profit maximization...)

Remember, though, that it's not just product management who needs to buy off on the debt. Professional services and support, documentation and sales and marketing and executives all have a stake.

For the last few years, I've been acutely aware of this issue, and I've worked hard to be a better communicator. This addresses rule #1. But it's not enough.

Hence rule #2.

If your organization doesn't understand where they're carrying technical debt, and how much it's costing them, then you must find a way to change. In <a title="Coping With Organizational Alzheimers" href="/2012/10/12/coping-with-organizational-alzheimers/">my last post</a>, I recommended using whatever ticketing system tracks your development tasks. I think that's a good start, but even that mechanism may not have enough visibility. When debt is killing you, you may need a special graph on an executive dashboard, a slide in the annual planning meeting, and/or half a dozen other ways to keep the issue in the minds of thought leaders.

Perhaps you feel that this is too much of a bother. For small debts, I guess it could be. But large debts have a way of creating toxic assets. You just cannot play shell games forever. Remember Bear Stearns and Lehman Brothers...
<p style="padding-left:30px;text-align:center;"><span style="color:#000080;"><strong>Action Item</strong></span></p>
<p style="padding-left:30px;"><span style="color:#000080;"><em>Find out which people in other departments besides dev understand how technical debt works. Recruit some allies and devise a plan to make your debts more auditable.</em></span></p>

<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://blog.xebia.com/2012/09/21/technical-debt-is-it-only-technical/" target="_blank">Technical debt; is it only technical?</a> (xebia.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://agile.dzone.com/articles/technical-debt-%E2%80%93-when-do-you" target="_blank">Technical Debt - When Do You Have To Pay It Off?</a> (agile.dzone.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://blog.orange11.nl/2012/09/18/be-thoughtful-when-measuring-technical-debt-with-sonar/" target="_blank">Be thoughtful when measuring Technical Debt with Sonar</a> (orange11.nl)</li>
</ul>

---

Don (2012-10-15 08:02:15)

The key in my opinion is not to let debt accumulate from sprint to sprint. Control the level of function such that the debt is managed. True doneness minimizes debt to an acceptable level and true doneness = real quality.

---

Daniel (2012-10-15 10:44:24)

Good insight, Don. Sounds a lot like the advice to pay off credit cards regularly... :-)

---

doug (2012-10-15 16:20:34)

you nail exactly what I have been thinking for MANY years, but not able to articulate. There is a COST to such debt, but there have NOT been metrics to expose it's reality to the decisions makers

---

Mike Ebert (@mike_ebert) (2012-10-16 00:39:33)

When technical debt becomes too great, sometimes organizations have to declare bankruptcy--certainly technical bankruptcy, if they survive financially--I'd be interested to hear thoughts about what's involved in technical bankruptcy, esp. if there's anything non-obvious.

---

Daniel (2012-10-16 02:01:31)

Good comment, Mike!

I would equate bankruptcy with declaring a codebase insolvent -- incapable of providing any future value. If you get to that point, you're looking at a total rewrite.

However, this may be too simplistic. In my post about "The 8th Characteristic," I claimed that codebases naturally die; maybe declaring a codebase dead isn't the same as declaring bankruptcy.

I'll noodle on it, and blog if I think of anything useful.

What kinds of events do you associated with bankruptcy?

---

Earned Pragmatism &laquo; Codecraft (2013-01-18 08:53:25)

[...] architectures healthy. Codebases owned by this type of “architect” tend to be rife with tech debt, with no roadmap or process to haul the team up and out. Where there is no vision, the people [...]

---

jasonodtr.inube.com (2013-03-06 20:25:02)

Wonderful insight. What a web site you have! Keep it up.

---

Kerry (2013-03-21 11:40:46)

Greetings from Colorado! I'm bored to death at work so I decided to browse your website on my iphone during lunch break. I really like the discussion of programming comments you provide here and can't wait to read more. Anyhow, awesome blog!

---

Why you should use an IDE instead of vim or emacs | Codecraft (2014-05-13 10:16:44)

[…] find it easier to generate momentum on unit tests, to eliminate fear of ambitious refactors, and to see their way past nagging tech debt. However, bigger concerns have kept me from pushing them hard in that […]

---

Courage Counts | Codecraft (2013-05-31 08:33:33)

[…] “Nobody will buy into the need to pay down technical debt.” […]

---

Features are not chunks of code | Codecraft (2013-07-25 11:19:49)

[…] never “done.” Sticking our heads in the sand to avoid this truth is a surefire way to incur tech debt, and not accounting for it with each release is a sin of […]

---

How to make a const-correct codebase in 4300 easy steps | Codecraft (2014-03-25 11:44:42)

[…] something right is cheaper and a whole lot less hassle than fixing an antipattern once it’s firmly entrenched. We’ll never get away from refactoring (nor would we want to)–but it pays to establish […]

---

Technical Debt is not only a "Technical" Problem | On Technical Debt (2015-07-06 11:05:33)

[…] To read the full post visit here. […]

---

On Forests and Trees | Codecraft (2015-09-02 08:49:00)

[…] One reason we don’t generalize is because we are being crushed by tech debt. We feel like we can’t afford it. This is a very real problem, but it is solvable–or at least improvable. […]