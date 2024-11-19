---
title: A Quibble With Martin's "Optimize Later" Notion
date: 2012-08-28
slug: a-quibble-with-martins-optimize-later-notion
redirect_from:
  - /2012/08/28/a-quibble-with-martins-optimize-later-notion
comments:
  - author: 3 Commandments of Performance Optimization &laquo; Codecraft
    date: 2013-01-08 09:08:25
    comment: |
      [...] I don’t think either of these extremes is healthy in all cases. I have seen programmers who chronically think about performance too late,  creating large refactoring burdens and sabotaging their company’s success. Sometimes when you go from “make it work” to “make it fast” you find that all your original work is a waste, because a totally different design (even different tests, conceivably) is the only way forward; I wrote about this in “A Quibble with Martin’s ‘Optimize Later’ Notion“. [...]
---
In <a href="http://martinfowler.com/books/#refactoring" target="_blank"><em>Refactoring</em></a>, Martin Fowler (a brilliant engineer whom I greatly admire) articulates an idea that I have heard from smart engineers for a long time: <em>first make it work, then make it fast</em>. He puts it this way:
<blockquote>"Until I profile I cannot tell how much time is needed for the loop to calculate or whether the loop is called often enough for it to affect the overall performance of the system. Don't worry about this while refactoring. When you optimize you will have to worry about it, but you will then be in a much better position to do something about it, and you will have more options to optimize effectively."</blockquote>
I mostly agree. Certainly, premature optimization can cause lots of problems (pollute an otherwise clean design, overvalue corner cases, dilute conceptual integrity), and profiler-driven optimization (science, not black magic!) is the way to get the best results. Donald Knuth famously observed that "premature optimization is the root of all evil" &mdash; a bit over the top, maybe, yet true often enough to give me fits.

But implicit in Fowler's advice are the following problematic notions:
<ul>
	<li>Optimization is a discrete activity from ordinary coding. Especially, it is discrete from refactoring.</li>
	<li>Between the time that you code an original or refactored version, and the time you optimize, the existence of unoptimized code will have negligible effect on how the rest of the code's ecosystem evolves.</li>
</ul>
The flaws in the first notion should be obvious; optimization often requires concommitant refactoring. I won't beat that dead horse here. The second idea, however, deserves further comment.

<figure><img alt="" src="http://imgs.xkcd.com/comics/movie_seating.png" width="500" height="571" /><figcaption>Sometimes the only time to optimize is before decisions get made :-). Image credit: xkcd</figcaption></figure>

Before you get around to optimizing, what happens if programmers go looking for an API that does X, find your works-correctly-but-suboptimally function, and wrinkle their nose. "Code smell!" they cry. And they write their own function that does a binary rather than linear search, etc. They don't have time to investigate whether the original version was coded that way for a reason (and thus should simply be refactored); they just need something that works AND that is fast, and your function doesn't cut it.

I have seen this happen over and over and over again. Late optimization, while smart in many cases, must be managed (communicated, commented, evangelized, trained, reinforced, audited, planned for) carefully or else it will provoke a lot of NIH and contempt from (ironically) less savvy programmers. Result: more guck that needs refactoring.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Find a notoriously sub-optimized function in your code. Study how its existence in non-optimal form has influenced how other code has evolved.</span></em></p>
