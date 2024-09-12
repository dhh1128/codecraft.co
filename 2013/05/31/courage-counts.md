---
title: Courage Counts
date: 2013/05/31
slug: courage-counts
---

If you've read <em>Call it Courage</em>, then you know the story of Mafatu, the boy who was afraid.

Mafatu grows up in Polynesia, surrounded by the ocean—but everything about the sea terrifies him, because he remembers his mother drowning when he was young. Determined to conquer his fear or die trying, Mafatu sets out alone in a dugout canoe, into the element that terrifies him most. He ends up stranded on an island that harbors cannibals. In one memorable scene, his faithful companion dog is endangered by a tiger shark; Mafatu jumps in the water and attacks with only a knife. When he kills the shark, he realizes that something fundamental in his heart is now different.

He still feels fear, but it no longer overpowers him.

He is free.

I've been blogging about the skills and mindset of effective software architects for quite a while now, but I recently realized that I've omitted the fundamental subject of courage.

[caption id="" align="aligncenter" width="500"]<a href="http://www.flickr.com/photos/nalsa/2888919972/"><img alt="" src="https://farm4.staticflickr.com/3134/2888919972_b79a8432ff_z.jpg?zz=1" width="500" height="332" /></a> image credit: nalsa (Flickr)[/caption]

This is an important gap, because <em>courage counts</em>. The cleverest, most skilled architect or engineer will accomplish very little, at key junctures in a career, without it.

<strong>Symptoms of fear</strong>

In the past two decades, I've heard many people (myself included) make statements like the following:<!--more-->
<ul>
	<li>"We cannot do <em><risky change X></em> because it might destabilize the code."</li>
	<li>"Stay away from <<em>module Y</em>>. Here be dragons."</li>
	<li>"I'm not sure <<em>technique Z</em>> is wise. There are too many unknowns."</li>
	<li>"If I try to sell that idea to <<em>executives/product management/the dev team</em>>, they'll just roll their eyes and change the subject."</li>
	<li>"Nobody will buy into the need to <a title="Paying Off Technical Debt" href="http://codecraft.co/2012/10/14/paying-off-technical-debt/">pay down technical debt</a>."</li>
</ul>
Such statements are really just fear, dressed up in fancy clothing.

I'm not going to claim that these fears are irrational. It could very well be that your change is risky, courting allies is a recipe for frustration, and you'll fail.

Mafatu's fear of the sea was rational, too--and it was based on <a title="Earned Pragmatism" href="http://codecraft.co/2013/01/18/earned-pragmatism/">traumatic, real-world experience, not theory</a>. But when the need was great, Mafatu plunged in, met his fears, and mastered them.

Sometimes we need to do that as technical thought leaders.

<strong>When to confront our fears</strong>

This is particularly important in pivotal moments when the choice is between a "safe" dead end and a risky but maybe game-changing innovation. If we believe that without a change, our codebase or our product or our team is headed for extinction (especially, when it's "not with a bang, but a whimper"), we have a duty—to ourselves, our employers, and our customers—to jump in the water with our knife and do battle with the shark.

I am not advocating that we recklessly battle about every issue that lights up our radar. But I do think we need to notice when fear is inhibiting necessary change, take a deep breath, and commit. (Too bad <a title="All I Really Need To Know I Didn’t Learn In Compugarten" href="http://codecraft.co/2012/11/15/all-i-really-need-to-know-i-didnt-learn-in-compugarten/">they don't teach that to CS majors</a>. :-)

<strong>Case study 1</strong>

A while back, a large and mission-critical codebase under my purview was exhibiting frightening stability problems. My boss was beside himself. I was newly hired, and not yet battle-tested at the company or even in the industry where the codebase was focused. After some analysis, I recommended the commissioning of a "tiger team" to surge on a handful of key architectural initiatives.

This must have been scary for my boss. Should he bet his personal reputation, the credibility of the engineering team, and the revenue stream of the company on advice that he couldn't easily validate? Not only was I an unknown quantity, but I was proposing radical changes to an already shaky codebase; the possibility of making things worse was very real.

I halfway expected to be ignored, but my boss (and a lot of other stakeholders) had guts. He championed the strategy all the way to the CEO. The tiger team was born; in about 7 weeks we made a fundamental improvements to process, build, test framework, and code organization. The next release was a significant improvement.
<p style="padding-left:30px;"><em>Score</em>: <span style="color:red;">Fear</span> 0, <span style="color:green;">Courage</span> 1.</p>
<p style="padding-left:30px;"><em>Outcome</em>: Big <span style="color:green;">success</span>.</p>
<strong>Case study 2</strong>

From about 2004 to 2007, I worked to transition backup technologies at Symantec from a tape-centric to a disk-centric model. A big problem for us was the <a title="Why Cannibalism May Be Smart Business" href="http://codecraft.co/2012/10/05/why-cannibalism-may-be-smart-business/">fear of cannibalizing the revenue stream</a> of the traditional product. We ended up dithering long enough that the opportunity to ride a disruptive wave largely passed us by. Cloud and virtualization and SaaS all combined to erode the value prop of traditional backup.
<p style="padding-left:30px;"><em>Score</em>: <span style="color:red;">Fear</span> 1, <span style="color:green;">Courage</span> 0.</p>
<p style="padding-left:30px;"><em>Outcome</em>: Painful, lingering, and preventable <span style="color:red;">failure</span>. Shame on us. (A coward dies a thousand deaths; a hero only one...)</p>
<strong>Case study 3</strong>

In 2008, I started a company with several of my MBA buddies. We'd been experimenting with product concepts for months. We wrote a comprehensive business plan, bought the IP of a silicon valley startup that was looking to liquidate, and began to pitch to investors. We believed we had a technology recipe that could alter the social media landscape.

Remember what happened to the stock market in 2008?

Yeah.

That all went down just after I emptied my personal savings to fund our startup, and just before we were hoping for an infusion of investor capital.

I'll skip a long story and simply say that I've paid some tuition in the school of hard knocks.
<p style="padding-left:30px;"><em>Score</em>: <span style="color:red;">Fear</span> 0, <span style="color:green;">Courage</span> 1.</p>
<p style="padding-left:30px;"><em>Outcome</em>: One of my best <span style="color:red;">failure</span>s.</p>
<strong>The moral, part 1</strong>

If you're into combinatorial math, you'll notice that I've given you 3 out of 4 possible scenarios: <span style="color:green;">+courage</span> —> <span style="color:green;">success</span>, <span style="color:red;">-courage</span> —> <span style="color:red;">failure</span>, and <span style="color:green;">+courage</span> —> <span style="color:red;">failure</span>.

There's no 4th story, because <span style="color:red;">-courage</span> —> <span style="color:green;">success</span> is about as rare as frog fur; it only happens by random mutation.

If you want a chance to change the world, you need courage; listen to fear, and it's not hard to predict the outcome.

<strong>The moral, part 2</strong>

Most of the failures we fear are not all that catastrophic. I'm still kicking.

<strong>The moral, part 3</strong>

It's worth noting that I have no regrets about my "failure" where I took a risk. It didn't work out. Like Edison, I now know another way not to invent a lightbulb. I'm good with that. As <a title="hierarchy of failures" href="http://sethgodin.typepad.com/seths_blog/2013/05/a-hierarchy-of-failure-from-brave-to-shameful.html" target="_blank">Seth Godin says</a>, even mistakes can pay off in the long run.

On the other hand, I still bore anybody who'll listen, with my harangues about head-in-the-sand thinking in the backup market.

<strong>Challenge</strong>

In Shakespeare's <em>Henry IV, Part I</em>, Falstaff claims that discretion is the better part of valor--or in other words, it pays to be cautious.

This is certainly true. Sometimes. Mafatu was probably wise not to tangle with tiger sharks every day.

However, Falstaff is rationalizing. The audience knows it, and so does he.

I'm going to make a conscious effort to notice when I'm listening to fear more than I should, and I'm going to try to be more courageous when it matters.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Find a moment when courage counts, and seize it. Celebrate the success of the commitment, regardless of the outcome.</span></em></p>

<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://www.slaw.ca/2013/05/22/practicing-courage/" target="_blank">Practicing Courage</a> (slaw.ca)</li>
	<li class="zemanta-article-ul-li"><a href="https://plus.google.com/110981030061712822816/posts/KaSKeg4vQtz" target="_blank">Notes from the Mystery Machine Bus</a> (Steve Yegge, Google +)</li>
</ul>

---

Why you should use an IDE instead of vim or emacs | Codecraft (2014-05-13 10:16:38)

[…] IDE-land for a while; I think they’d find it easier to generate momentum on unit tests, to eliminate fear of ambitious refactors, and to see their way past nagging tech debt. However, bigger concerns have […]

---

Daniel Hardman (2013-05-31 10:48:26)

When I first read Dune as a teenager, I thought of the Bene Gesserit litany as pseudo martial arts mumbo jumbo that added some nice artistic flair to the milieu of the novel.

Since then I've decided that it's quite profound--maybe Herbert's great philosophical contribution.

Thanks for reminding me about it; I have something else that I need to print out and put on my door for inspiration.

BTW, your post on fear at http://dld.me/fear/ is awesome!

---

dougbert (2013-05-31 09:56:40)

Again spot on the mark.  Been there done that many times (fear and courage both). As I near retirement (13 years from now), I am more able to push on with MY ideas on things, backed up with some new ideas I read in a new book or a blog along with some ideas from here.

You second witness many things I come up with as well.

* Courage is being afraid but saddling up anyway . - John Wayne

---

Daniel Hardman (2013-05-31 10:44:49)

That's an awesome quote from the Duke! Thanks for sharing.

---

trevharmon (2013-05-31 09:11:27)

Well said, Daniel. It is much better to succeed or fail in spectacular fashion for one's passion than to linger in the soul-sucking mediocrity. As Henry David Thoreau wrote in Walden, "The mass of men lead lives of quiet desperation. What is called resignation is confirmed desperation." And, I agree with you, it is scary... really scary sometimes. That's why I appreciated you calling out the fact you're still kicking even after failures.

I must not fear.
Fear is the mind-killer.
Fear is the little-death that brings total obliteration.
I will face my fear.
I will permit it to pass over me and through me.
And when it has gone past I will turn the inner eye to see its path.
Where the fear has gone there will be nothing.
Only I will remain.

- Bene Gesserit Litany Against Fear - From Frank Herbert's Dune Book Series

---

How to make a const-correct codebase in 4300 easy steps | Codecraft (2014-03-25 11:44:36)

[…] the other hand, courage counts. A festering problem finally got fixed, because I was crazy enough to […]

---

Are We Smart Enough to Use Kind Words? | Codecraft (2015-10-06 16:35:53)

[…] by trial and error. Part of “tech progress” is raising the experience, confidence, and courage of those around us; in doing so, we learn more ourselves, and we are usually repaid in spades. Over […]