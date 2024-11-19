---
title: Tech Debt, Leverage, and Grandma's Envelope
date: 2012-10-30
slug: tech-debt-leverage-and-grandmas-envelope
redirect_from:
  - /2012/10/30/tech-debt-leverage-and-grandmas-envelope
comments:
  - author: dougbert
    date: 2012-10-30 11:03:22
    comment: >
      great solution to the inheirtance of tech-debt, here and there an improvement. Hopefully it won't be passed on to the next generation (like our feds are doing to my grandchildren). Then share (help/encourge)  the effort with others and over time, there is improvement.
  - author: Daniel
    date: 2012-10-30 11:06:01
    comment: >
      I saw you doing exactly this -- modeling good habits and trying to inspire your peers. Although you may not have made as much progress as you wanted, there is no doubt in my mind that you left things much better off than they would have been without that discipline. Thanks!
  - author: Learned Helplessness, Rats, and People Power &laquo; Codecraft
    date: 2012-11-26 08:40:03
    comment: >
      [...] previously written about my Grandma paying off her mortgage after many years of diligent effort. This was the harvest of a good habit, applied [...]
---
In my previous posts about tech debt, I focused on <a title="Coping With Organizational Alzheimers" href="paying-off-technical-debt.md">how tech debts are funded and paid back</a>.

[caption id="attachment_965" align="alignright" width="300"]<a href="http://www.flickr.com/photos/foei/9530111/"><img class="size-full wp-image-965" alt="Photo credit: Friends of the Earth International (Flickr)" src="http://codecraft.co/wp-content/uploads/2012/10/screen-shot-2013-02-01-at-8-20-20-am.png" width="300" height="222" /></a> Photo credit: Friends of the Earth International (Flickr)[/caption]

These topics hit a raw nerve with coders and testers. Those in the trenches often feel very keenly the cost of doing things in a messy way, and it's common for them to worry that others don't "get it."

They're not wrong to worry.

However, today I'd like to put on my executive hat and discuss tech debt from a perspective that code jockeys sometimes miss, because blindness is not just an executive disease.

<strong>Debt as Leverage</strong>

When you hear the word "leverage" in business circles, people are talking about debt: a "highly-leveraged" firm is one financing large portions of its strategy through debt; "leveraged buyouts" are transactions where the buyers borrow vast sums of money from a risk-taking lender to take a company private.

Technogeeks (like me): business people are not dumb. Why did they settle on this metaphor of debt as leverage?

The answer is that debt can allow a company to concentrate enough capital in a short enough timeframe to make high-impact strategic moves that would otherwise be impossible. It's an enabler and multiplier.

<figure><img alt="" src="http://imgs.xkcd.com/comics/archimedes.png" width="444" height="285" /><figcaption>Another take on leverage. Image credit: xkcd.</figcaption></figure>

Debt is a fundamental machine in the business toolkit, just as levers are a fundamental machine for mechanical engineers. Almost all businesses use debt to some extent. If a CEO can borrow capital at 9% and produce 12% ROI with it, and <!--more-->if the risk implied by that gap is low enough, then not borrowing would be a violation of his <a class="zem_slink" title="Fiduciary" href="http://en.wikipedia.org/wiki/Fiduciary" target="_blank" rel="wikipedia">fiduciary responsibility</a> to stockholders. In fact, I'd go so far as to say that capitalism is somewhat founded on the notion that debt allows money to flow to its most efficient use.

Don't get me wrong. I detest personal debt.  I think recent financial excesses, and the ensuing mess as we were forced to confront arbitrage and Wall Street shenanigans, are deplorable. I think most first-world countries are neck-deep in debt and are thus setting themselves up for hard times for many years to come.

I'm just saying that debt, like any other tool, has legitimate (and intelligent) uses, and it's not going away.

Now, think about "tech debt" from this perspective for a minute.

Yes, the tech debt is ugly. We hate the way it complicates our designs, slows our velocity, compromises our future.

But what have we been able to buy with our loan?

If the answer is "nothing worthwhile," then shame on executives. But if the answer is "we kept the company alive and entered a key market or landed a lighthouse customer," then maybe it was the right move.

Of course, just because it was smart to buy on credit doesn't mean you should make minimum payments forever. And just because the lender isn't pounding on your door doesn't mean your payment isn't due.

<strong>Another Moral</strong>

I can remember my grandmother whistling in the kitchen as she sealed an envelope and put a stamp on it.

<figure><img alt="" src="http://farm5.staticflickr.com/4088/4984697380_29b76f123f_m.jpg" width="240" height="161" /><figcaption>Image credit: Sean Loyless (Flickr)</figcaption></figure>

"What are you mailing?" I asked.

"My mortgage payment," she said with a smile. "The last one." (<em>I </em>think<em> it was the last; maybe she was still a few months away but could see the finish line. Anyway...</em>)

That moment came after years of patient, disciplined effort on Grandma's part. It did not come in a single, giant payback.

Technogeeks: here is another blindness that we sometimes suffer from. We think that if we push hard enough and make enough noise, we'll convince someone to pay back a tech debt in one grand gesture.

Grandma didn't have that kind of money, and neither do most of the companies we work for.

Thus, two words must get imprinted on our hearts and minds: <em>discipline</em> and <em>patience</em>.

<strong>Circle of Concern, Circle of Control</strong>

This is something <em>you</em> can control. Yes, you. You may not have a manager or executives that totally agree with you about how painful your tech debts are. You may not have veto power on the dev budget. You may not sit in strategic board meetings.

But you can get in the habit of mailing a check every month. Even the worst spiky-haired boss probably can't stop you.

Read <em>Refactoring</em> (Martin Fowler). Ponder.

Next time you're fixing a bug, take an extra 5 minutes to ument the function better. Then make that practice a habit.

In the spirit of <a href="six-learning-tips-for-tech-folks.md">my post about teaching to accelerate your own learning</a>, talk at what you're doing, and why. I remembered Grandma's comment for 35 years; you'll make an impression on others.

Don't accept anyone's claim that they don't have time to do things right, without a gentle and <a title="Humility" href="humility.md">humble</a> push-back. (As Seth Godin says: <a href="http://sethgodin.typepad.com/seths_blog/2012/09/doing-it-in-a-hurry-almost-always-takes-longer.html" target="_blank">haraka haraka, haina baraka</a>.)

Next time a behavior of the code puzzles you, write a unit test to understand it.

Next time you hear yourself complaining about how hard it is to install the product, assign yourself to spend half a lunch break improving a smart default.

<strong>One Last Insight</strong>

You may be saying: "That's all well and good, but it's a drop in the bucket compared to the massive problem we have with <em>X</em>."

Even if that's true, I guarantee that at least half of the massive problem you have with <em>X</em> is one of attitude. You'll never solve it if you can't <a title="Roland Whatcott: Manage momentum." href="roland-whatcott-manage-momentum.md">generate some momentum</a> and optimism for the future. Give yourself a reason to believe things can get better, and watch how much more tractable your tech debt becomes.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Identify a low-cost, high-impact habit that will raise your spirits and your team's vision with regard to tech debt, and ingrain that habit in your own day-to-day work.</span></em></p>
