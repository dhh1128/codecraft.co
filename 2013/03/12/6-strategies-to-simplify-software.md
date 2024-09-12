---
title: 6 Strategies to Simplify Software
date: 2013/03/12
slug: 6-strategies-to-simplify-software
---

How do you make things simple?

I've written that <a title="The Power of Simplicity" href="../../../2013/02/15/the-power-of-simplicity/" target="_blank">simplicity is powerful</a>, and that it undergirds many deep architectural breakthroughs. In posts about <a title="Earned Pragmatism" href="../../../2013/01/18/earned-pragmatism/" target="_blank">pragmatism</a> and <a title="Good Code Is Balanced" href="../../../2012/08/27/good-code-is-balanced/" target="_blank">balance</a>, I've quoted Oliver Wendell Holmes about the simplicity on the other side of complexity.

But I've never talked about how to achieve it.

[caption id="" align="aligncenter" width="500"]<a href="http://www.flickr.com/photos/hurleygurley/16139468/"><img alt="" src="http://farm1.staticflickr.com/11/16139468_0d14545348.jpg" width="500" height="375" /></a> photo credit: hurley gurley (Flickr)[/caption]

This is not an easy question; if we knew how to make things simple, we'd do it more often and more quickly. It takes some serious effort (and genius) to go from centuries of experiments and volumes of equations to <code style="font-size:120%;color:#303048;">e = mc<sup>2</sup></code>. I've been pondering simplicity in software architecture for a decade, and I'm certain I've only scratched the surface.

Still, simplicity is a learnable skill, and some strategies are consistently helpful...<!--more-->

<strong>1. Encapsulate</strong>

I put this one first, because it is straightforward and virtually guaranteed to pay off. This strategy isn't a panacea, but it's a good place to start.

When a problem is complicated, fence it off behind a disciplined interface, and then ask yourself what the problem looks like on the outside. This will provide useful constraints. Now peer inside your complicated inner world, and repeat the process. How can the problem be divided into pieces that are individually tractable, even if they have a lot of gory detail inside?

Recurse as needed.

<strong>2. Cut corners</strong>

In many, many cases, the complexity we wrestle with comes from an overly ambitious scope. Overbuilding is probably my greatest weakness as an architect; I've <a title="Why I don’t blog about great code" href="../../../2012/10/03/why-i-dont-blog-about-great-code/" target="_blank">made the mistake way too often</a>.

Perhaps you want to improve logging in your product. At first it seems simple, until you start asking how to localize your logs, and how to handle thousands of logged events per second, and how to silo your logs so one tenant can't see what another tenant is doing.

One important way to simplify is to say: we're not going to localize, and we don't need to run fast when logging thousands of events per second, and we don't need multitenant distinctions in our logs.

You can't always get away with this sort of simplification, but it's worth considering.

<strong>3. Hire a specialist</strong>

Do you do your own taxes, your own dentistry, and your own legal work? Why not?

This is a complement to the "cut corners" strategy. If you can't make the tax code simpler, perhaps you can ignore the problem most of the time, and occasionally hire an accountant that reframes complexity to be more manageable. To continue the log example, maybe you write a script that gives each tenant a subset of the overall logs, on demand.

<strong>4. Delegate</strong>

Human beings realized long ago that even the smartest and most well rounded person in the world can't run an entire organization alone. A CEO hires someone else to think about marketing, about sales, about engineering, about support, about facilities, about accounting.

Many software architectures are crushed by complexity because they have a CEO that's trying to empty trash cans, pay the bills, woo customers, and keep the board happy, all at the same time. If your system has a centralized brain, and everything runs through it, consider putting some other brains to work. I have become convinced in the past decade that distributed architectures almost always beat centralized over the long haul, for this reason.

<strong>5. Change your metaphor</strong>

Suppose you have a workflow engine, and you're struggling to make it more responsive. You normally model worflow as a state machine, because it gives you crispness and predictability.

Well, maybe you should stop thinking of your workflow engine as a state machine, and start thinking of it as a bureaucracy. What makes bureaucracies grind to a halt? How do you get around them? Bribes work wonders in some bureaucracies; should you allow high-priority items to "bribe" their way through for faster outcomes? What if an urgent task walks in the front door of the bureaucracy's office and takes the Grand Poobah's secretary hostage?

I think this strategy is underutilized in almost every long-running architecture. Metaphor can drive insight in ways we don't talk about enough.

One other hint on this one: Do some reading about <a href="http://en.wikipedia.org/wiki/Gossip_protocol" target="_blank">gossip protocols</a> and <a href="http://en.wikipedia.org/wiki/Bully_algorithm" target="_blank">bully algorithms</a> some time. The richest sources of metaphor for me are human society (families, companies, social networks, politics, fraternities, multi-level marketing schemes, crime syndicates...) and life (cells, ecosystems, packs and herds, predators/prey, ...). This is why I'm writing a whole book about what life can teach software architects. Subscribe to my blog for more news on this.

<strong>6. Ask a child</strong>

It doesn't have to be someone young, really--the true requirement is that it needs to be someone with some intellectual distance from the problem, who's able to ask probing questions. Children are just the perfect prototype.

Years ago, thieves were raiding high-end clothing stores. They'd run in, sweep all the hangers to the end of the rack, lift off an armful of expensive merchandise, and run out the door before anybody could stop them. Stores tried all kinds of things, but the thieves were organized and fast, and they kept escaping.

Finally someone suggested turning every other hanger top in an opposite direction. Half the hangers would lift off to the left, half to the right. Next time the thieves came in, they discovered that it was impossible to pull an armload of clothes off the rack quickly. Problem solved.

And then there's the story of the <a href="http://www.thesimplest.net/stories/story-empty-soap-box" target="_blank">factory that went to great lengths</a> to prevent the 1-in-a-thousand box that exited the assembly line empty. They built xray machines to check the boxes, stationed someone to monitor the xray screen continuously... I bet they felt foolish when someone bought a cheap fan and simply blew the empty boxes off the conveyor belt...

<strong>7. ???</strong>

Undoubtedly, other helpful strategies can also contribute to simplicity. Like the ones I've listed above, they will probably have their limits. We are unlikely to discover a silver bullet--and even if we did, the arms race of our industry makes it probable that we'll need a silver missile in the near future. It takes hard thinking, and hard work, to wrestle complexity into clean, reusable packages that fit together nicely. And it always will.

But--ah!--the beauty of well crafted minimalism...

Perhaps Leonardo da Vinci said it best: "Simplicity is the ultimate sophistication."
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Identify a metaphor that's important to your architecture. Find at least one other metaphor that you could use to replace it. Spend 5 minutes exploring the alternate metaphor. Do you see strengths, weaknesses, opportunities, and threats to your architecture in new ways?</span></em></p>

<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://www.jbox.dk/quotations.htm" target="_blank"><span style="font-size:small;"><span style="line-height:19px;">Quotations on simplicity in software design</span></span><span style="color:#333333;font-size:13px;line-height:19px;"> (jbox.dk)</span></a></li>
</ul>

---

Julie (2013-03-13 15:05:25)

You hit the nail with a sledgehammer with this post!

Metaphor becomes more important every time I work with a new system that no one can explain. Usually the problem is that they don't have a metaphor to relate it to. People work best with an abstraction in their heads.

And, I will add another vote for simplicity. As systems become more distributed and massive, communication becomes the problem. Funny how that mirrors the human problem when people work together. The answer is often simplicity. Think of the largest autonomous system out there - the internet. TCP/IP works with what might be the simplest solution to multiple machines trying to talk at the same time "wait a bit and try again". I'm sure everyone can think of a much "better" solution. I am also sure it is more complicated, and I am resonable sure that it wouldn't work as well. 

My goal is: make it simple enough to understand and wrap that understanding in a memorable metaphor.

---

segmation (2013-03-12 09:04:09)

I like ask a child!  Children can come up with the greatest of things!  Thanks for sharing this awesome blog!

---

Daniel Hardman (2013-03-12 10:22:23)

The other day my young nephew and his older brother were having a conversation.

Older brother: "What's a baby dog called?"
Younger nephew: "A puppy."
Older brother: "What's a baby sheep called?"
Younger nephew: "A lamb."
Older brother: "What's a baby chicken called?"
Younger nephew: "A yolk!"

Funny. But also shows how kids have different perspectives that can break us out of the box. :-)

---

Daniel Hardman (2013-03-13 15:19:21)

The internet is such a good example. Not only is TCP/IP amazingly simple (in concept, not necessarily in impl), but so is the HTTP protocol. It seems amazing to me that I ever lived without it. Thank you, Tim Berners-Lee and Roy Fielding and all the other smart people who achieved so much by simplifying so much!

---

Small Files Are Your Friends | Codecraft (2013-03-21 08:55:47)

[...] Another way to say this is that file boundaries are an encapsulation barrier. Use them to hide data. (See my recent post about encapsulation as a simplicity strategy.) [...]

---

My First Tangle With the Tower of Babel | Codecraft (2013-04-26 08:48:28)

[...] think the answer may lie in finding new accommodations for all the complexity we wrestle. New ways to think about concurrency, distributed architectures, [...]

---

Why Your Software Should Cry | Codecraft (2013-05-06 11:50:46)

[...] how much we can accomplish in a good script with a few lines of code. However, if we want to truly master the bewildering growth of complexity in the universe of bits and bytes, we need pain. And we need [...]

---

A grumble about buckets | Codecraft (2015-04-08 13:39:18)

[…] developers limit the choices that are offered to their users as a way to simplify. This can be a good thing; I’m a big fan of […]

---

On Forests and Trees | Codecraft (2015-09-02 08:48:37)

[…] possible become unremarkable. It’s among the human mind’s most powerful techniques for coping with complexity, and it’s a hallmark of vigorous thinkers in any technical discipline. I like […]