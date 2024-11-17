---
title: Coping With Organizational Alzheimers
date: 2012/10/12
slug: coping-with-organizational-alzheimers
---

Years ago, an astute manager summed up a problem that I had only vaguely intuited up to that point in my career.

<figure><img title="memory" alt="" src="http://farm4.staticflickr.com/3106/2819335335_185586a19c.jpg" height="500" width="270" /><figcaption>Do our memories leak? Image credit: xpectro (Flickr)</figcaption></figure>

"A big problem with most companies," said <a title="Roland Whatcott: Manage momentum." href="../../../2012/09/21/roland-whatcott-manage-momentum/" target="_blank">Roland</a>, "is that they have no institutional memory."

As I recall, Roland was describing capricious political winds, and lamenting that the only form of loyalty a company has to employees is the kind they put in writing. As soon as there's major M&A activity, or HR decides to rebalance salary allocations, or an incentive program gets adjusted to the latest management fad, all recollection of old priorities and soft obligations vanishes in a puff of smoke.

If anything, Roland was understating the problem. Companies routinely panic and change strategy half-way through an investment cycle, because they can no longer articulate the rational analysis that led them to take a plunge. Buzz floods the internet about some innovation that makes everybody excited, but we forget that we've heard the idea before, behind some different terminology. (Are you nodding your head because "cloud" in the last few years is just a recycling of "utility computing"from circa 2000? <a href="https://twitter.com/trev_harmon" target="_blank">Trev</a>, a colleague of mine at <a href="https://twitter.com/AdaptiveMoab" target="_blank">Adaptive Computing</a>, showed me a dog-eared copy of <em>The Challenge of the Computer Utility</em>, by <a class="zem_slink" title="Douglas Parkhill" href="http://en.wikipedia.org/wiki/Douglas_Parkhill" target="_blank" rel="wikipedia">Douglas Parkhill</a>. It's all there--XaaS, elastic and on-demand, in 1966. And who knows--maybe sci-fi writers or the designers of Eniac had thought of it even before Parkhill...)

But I digress.

One particularly insidious form of forgetfulness in software relates to <a class="zem_slink" title="technical debt" href="http://martinfowler.com/bliki/TechnicalDebt.html" target="_blank" rel="homepage">technical debt</a>. Another colleague, <a href="http://www.linkedin.com/profile/view?id=5417094&locale=en_US" target="_blank">Doug</a>, reacted to an expedient workaround this way:
<blockquote>My one regret with this is that by doing something that is good enough it will never get the attention it might deserve to be made better. This happens each release: we make compromises at the very end to get it out the door, promising ourselves that we'll revisit it later.</blockquote>
Folks, we don't keep these promises to ourselves very well; Alzheimers is endemic with regards to technical debt. The only thing that saves us is that <!--more-->engineers or product managers stumble upon the consequences of earlier kludges, which reminds us of the awkwardness from time to time. And there are enough passionate people in our industry that sometimes when an issue like this pops, we find a way to do it right. Sometimes.

I have two suggestions about how we can cope.

<strong>Suggestion 1. Log a new kind of ticket.</strong>

In most disciplined software companies, product planning captures <em>what</em> needs to happen in the next release. If you're doing waterfall, you write specs; if you're doing agile, you write stories. Either way, these artifacts commonly result in granular tickets that get assigned to implementers and testers. The tickets are then managed carefully until everything's been either closed or deferred, and a release comes to pass.

That's all well and good. But kludges aren't visible if the only thing you ever manage is <em>what</em>. Kludges satisfy <em>what</em>; they're yucky because of <em>how</em>.

What we need is a disciplined tracking of how.

"We already do that!" I hear you say. "We have design docs, UML diagrams, photos of whiteboard discussions, architectural reviews..."

Yes. That's all well and good, too.

But those mechanisms create alignment in the brains of people, and in their short-term behavior. Those people are part of an organization that has Alzheimers.

They need a memory aid.

Architects, log a ticket about <em>how</em> something must be done. If it gets deferred due to short-term expedience, you have tangible evidence of the debt that's been incurred, and in the next release cycle, management will be forced to reckon with it. If the ticket gets ignored, give the"blocker" priority a whirl... :-)

<strong>Suggestion 2: Be the change you want to see in the world.</strong>

If you're a manager: Orgs that believe in <a href="http://en.wikipedia.org/wiki/Kaizen" target="_blank">kaizen</a> are great. But if you always drive kaizen from the top down, you're missing the boat. What you need to do is let trusted engineers do kaizen from the bottom up. Every good engineer that I know has a few items they're itching to improve. Let slip the dogs of war and see what happens.

If you're an individual contributor: find a way. Don't sit around and wait for your manager to tell you you've been assigned to refactor. Just do it. Advocate. Read <a href="http://www.sethgodin.com" target="_blank">Seth Godin</a>'s book, <em>Poke the Box</em>. Then go poke.

<strong>A note of caution</strong>

Not every itch justifies a scratch. Engineers have a tendency to envision the ideal, and to love the freedom to go create it without mapping that activity back to hard business constraints. I know I do! :-)

If you're a manager, notice that I said you should give this freedom to <em>trusted</em> engineers -- not just anybody. Trust folks that can tell you how 2 days of effort will delight customers and save the company thousands of dollars. They'll probably take 4 days (or 6, if they're as bad at estimating as I am) to get the job done, but at least they have a tightly defined task with a specific payoff. Don't trust <a href="http://steve-yegge.blogspot.com/2008/02/portrait-of-n00b.html" target="_blank">"teenage" engineers</a> who try to sell you on total rewrites.

If you're an engineer, earn the trust I'm talking about.
<p style="padding-left:30px;text-align:center;"><span style="color:#000080;"><strong>Action Item</strong></span></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Find three examples where technical debt has been conveniently forgotten, and do something to keep the memory loss from becoming permanent.</span></em></p>

---

SutoCom (2012-10-12 12:35:37)

Reblogged this on <a href="http://sutocom.net/2012/10/12/2284/" rel="nofollow">Sutoprise Avenue, A SutoCom Source</a>.

---

ryancorradini (2012-10-16 06:34:58)

The “how” tickets are a great idea, but in my experience, they frequently tend to end up in the forever-in-the-future “unobtainium” release, because there are *always* going to be new feature requests / legitimate bugfixes / etc, and those will always take priority over refactoring tasks. That said, sometimes when I have a new task that touches on one of these needs-to-be-rewritten code blocks, if I can justify it, I do the refactoring anyway, guerilla-style, as part of the new feature. The challenge is knowing when it’s worth doing so.

---

Daniel (2012-10-16 08:34:16)

Ryan: You've got a nice way with words. The "unobtanium release" made me laugh. So true. Sigh...

Martin Fowler dedicated an entire book, <em>Refactoring</em>, to the question of how to make sure needed changes don't languish. It probably isn't fair to try to boil him down to a single pithy piece of advice, but I'll try anyway. He advocates changing our perspective on refactoring so that it's no longer a behavior separable from maintenance/improvement/extension. Instead, refactoring becomes a sort of dialog that you always have with the code as you evolve it into its next form. If you do refactoring that way, it just happens naturally, and code remains very healthy.

This is a radical change of mindset, but it seems to me that it would help us in many ways.

---

ryancorradini (2012-10-16 09:04:28)

I like the concept of a constantly-evolving codebase. That kind of approach would also enable some potentially interesting "code health" metrics derivable from your source control system. (e.g. percentage of code change between releases/milestones, etc). I'll have to look up that book, thanks for the recommendation.

As an aside, your link to Steve Yegge's post spurred some productive conversation at work. Always nice when that happens.

---

Paying Off Technical Debt | On Technical Debt (2014-03-17 03:59:39)

[…] my recent post about how organizations forget technical debt, I glossed over some important details. When you’re in debt, you have an obligation to pay […]

---

Tech Debt, Leverage, and Grandma's Envelope | On Technical Debt (2014-03-17 04:00:07)

[…] my previous posts about tech debt, I focused on how we can help organizations remember their debts, and on understanding how tech debts are funded and paid […]

---

Features are not chunks of code | Codecraft (2013-07-25 11:19:51)

[…] What this means, in practical terms, is that, even if you can code a feature in X hours, and even if it’s a simple feature with unusually minor demands on the rest of a team, its cost is never X hours. All features have a carrying cost, which is the ongoing expense of keeping the feature alive and connected to the blood supply on the rest of the face, through all future incarnations. In this sense, features are never “done.” Sticking our heads in the sand to avoid this truth is a surefire way to incur tech debt, and not accounting for it with each release is a sin of omission. […]

---

On Forests and Trees | Codecraft (2015-09-02 08:48:45)

[…] Where code is wisely generalized, maintenance goes down, testability goes up, and it’s easy to learn a correct mental model. The inverse is also true: bad choices about generalization usually hide the forest behind the trees, which causes pernicious tech debt. […]