---
title: Metrics, Plumb Lines, and System Thinking
date: 2012/11/12
slug: measurements-plumb-lines-and-system-thinking
---

Friday morning I was at a seminar taught by <a href="www.linkedin.com/in/jhtaylorjason" target="_blank">Jason Taylor</a>, CTO at <a href="http://www.allegiance.com" target="_blank">Allegiance</a>. We were discussing how dev team <a href="http://en.wikipedia.org/wiki/Velocity_(software_development)">velocity</a> and product quality can compete for our attention; sometimes we trade one for the other. Jason mentioned that he's a fan of competing metrics, and some neurons connected in my brain.

<figure><img alt="" src="http://farm4.staticflickr.com/3110/2600773685_8934c3327f_n.jpg" height="320" width="213" /><figcaption>Plumb line suspended from the center point of multiple balancing legs. Photo credit: suttonhoo (Flickr)</figcaption></figure>

I'm a big believer in measurement. As the old adage goes, you can't improve what you don't measure. Next time someone urges you to change a behavior, or tells you she's going to, ask what measurement of change is being proposed. If you get an unsatisfying answer, I predict you'll also get an unsatisfying outcome.

I'm also a big believer in balance, as I've written about before. <a title="Good Code Is Balanced" href="../../../2012/08/27/good-code-is-balanced/" target="_blank">Good software balances many considerations</a>.

Besides these existing predispositions, I'd recently read a <a href="http://sethgodin.typepad.com/seths_blog/2012/11/avoiding-the-false-proxy-trap.html" target="_blank">blog post by Seth Godin</a>, cautioning about the need to choose wisely what we measure. And I've been digesting <em>The Fifth Discipline</em>, by Peter Senge, which advocates wholistic, <a class="zem_slink" title="Systemics" href="http://en.wikipedia.org/wiki/Systemics" target="_blank" rel="wikipedia">systemic thinking</a>, where we recognize interrelationships that go well beyond simplistic, direct cause-and-effect.

All of these mental ingredients <!--more-->crystallized when Jason made his comment about competing metrics.

I realized that when we have a system that's out of balance, and we pull a lever to correct, if we measure progress with a single-minded metric, we are setting ourselves up for skew, overcorrection, or puzzlement. I think I've made this mistake several times in my career. We have to measure each factor that contributes to an overall <a class="zem_slink" title="System dynamics" href="http://en.wikipedia.org/wiki/System_dynamics" target="_blank" rel="wikipedia">system dynamic</a> if we want to shift balance efficiently and avoid pendulum behavior.

If you can directly measure balanced alignment to an ideal (i.e., you have a single metric that takes all competing factors into account), then you have the best of all worlds. I believe this is why <a title="Net Promoter" href="http://en.wikipedia.org/wiki/Net_Promoter" target="_blank" rel="wikipedia">net promoter score</a> is so powerful. These types of measurements are least susceptible to the <a href="http://keen-insights.com/?p=67" target="_blank">false proxy trap</a> Godin warns about; we can't "game" the system. But in many cases, the best we can do is measure multiple contributing factors.

If your organization is stuck in a binary tradeoff between quality and velocity, then a simple competing metric pair will suffice. Measure how quickly your team adds features (e.g., with <a href="http://scrummethodology.com/scrum-effort-estimation-and-story-points/" target="_blank">story points</a>), and measure how much your quality suffers (e.g., with a variant of <a href="http://www.isixsigma.com/methodology/metrics/exploring-defect-containment-metrics-agile/" target="_blank">containment rate</a>), and you'll have a good idea whether you should keep pushing on one side of the scale or the other.

However, a lot of systems are more complex, and it may be helpful to think of metrics as <em>complementary</em> rather than <em>competing</em>. Think legs of a tripod (or teepee), with a plumb line in the center. Adjust any leg, and the plumb line shifts. If your org sometimes trades velocity for quality, but also sometimes releases pressure by adding resources or by reducing scope, then you need to be measuring more than just quality and velocity to have a realistic idea of what's happening. You also need to be measuring how often, and by how much, your scope changes, and how often, and by how much, you shift resources around.

In my younger years, I grumbled a few times about how feature creep impacts quality, without providing any useful metrics that made that tradeoff real to product management or executives. I've gradually learned to be better, but now I realize I still have room for improvement. I don't think I've ever measured how many story points get deferred when an emergency drags resources away, or how many story points get done on a 4-month release versus an 8-month release.

I'm going to paint more complete pictures with my metrics, and see where it gets me.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Think of a team problem where you'd like a different balance. How can you measure each factor that plays into the overall dynamics of the situation?</span></em></p>

<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://managementhelp.org/systems/index.htm" target="_blank">Systems Thinking, Systems Tools and Chaos Theory</a> (managementhelp.org)</li>
	<li class="zemanta-article-ul-li"><a href="http://www.customerthink.com/blog/customer_metrics_measure_what_matters_most_to_customers" target="_blank">Customer Metrics: Measure what matters most to customers</a> (customerthink.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://hbr.org/2010/06/column-you-are-what-you-measure/ar/1" target="_blank">You Are What You Measure</a> (Harvard Business Review)</li>
	<li class="zemanta-article-ul-li"><a href="http://iterativepath.wordpress.com/2012/11/10/single-metric-you-need-to-care-or-do-you/" target="_blank">Single metric you need to care - Or do you?</a> (iterativepath.wordpress.com)</li>
</ul>

---

Daniel (2012-11-13 10:15:14)

Doug: I hadn't considered the analogy to flight, but I think it's a very insightful one. The problem of optimizing a particular number on the instruments, as opposed to seeking the overall best flying experience, is exactly the sort of problem that Seth Godin talked about with his caution about false proxies. We get enamored of a number and forget that it's only a means to an end.

That said, I'd rather have two or three useful numbers than just a vague intention. This is why it was so smart of you to pick a specific target (e.g., "no modules > 10k lines") and work to hit it in your moab work.

---

dougbert (2012-11-13 09:58:01)

I am not a pilot but I understand "instrument flying" operation.  It is possible to "fly the plane" by chasing the "artificial horizon", constantly trying to keep the horizon 'level'. Yet by solely following that type of flying, it is very easy to lose track of the overall objectuve if actually going somewhere desired. One can fly the plane correctly and safely, yet never get any where.

Tracking bugs fixed is good, but does that tracking increase or decrease the entropy of the code? A metric is there and can be used for reports, but what metric is used to measure "better code", "cleaner code", or "code that properly reflects the model of the problem being solved"?

As always, some great insight

---

Adios to &#8220;computer programming&#8221; | Codecraft (2013-04-05 09:34:37)

[...] need system thinking baked into our industry. We need programming languages that have sufficient expressive power to [...]

---

Why Your Software Should Cry | Codecraft (2013-05-06 11:51:00)

[...] we might aim for an “error gestalt” — the ability to notice system-level phenomena as the aggregate of many isolated signals. This would be analogous to a doctor diagnosing flue from [...]

---

Why you should use an IDE instead of vim or emacs | Codecraft (2014-05-13 10:16:26)

[…] show you a gestalt; they encourage you to think holistically about what you’re doing. If you write a method, and you don’t like the hover text that […]