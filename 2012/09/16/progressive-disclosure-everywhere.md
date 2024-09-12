---
title: Progressive Disclosure Everywhere
date: 2012/09/16
slug: progressive-disclosure-everywhere
---

If you google "progressive disclosure," you'll get hits that describe the phrase as an interaction design technique. UI folks have long recognized that it's better to show a simple set of options, and allow users to drill into greater detail only when they need it. (Thanks to James Russell--a brilliant UI designer--for teaching me PD years ago.)

But calling progressive disclosure a "technique" is, I think, a serious understatement. Progressive disclosure aligns with a profound cognitive principle, and its use is (and should be) pervasive, if you have eyes to see.

<strong>The Principle</strong>

Here's my best attempt to distill the operative rule behind progressive disclosure:
<p style="text-align:center;font-weight:bold;font-size:150%;background-color:#eee;border:solid 1px #CCC;padding:.5em 1em;">Focus on essence. Elaborate on demand.</p>
In other words, begin by addressing fundamentals without cluttering detail. When more detail is needed, find the next appropriate state, and move there. Repeat as appropriate.

Stated that way, perhaps you'll see the pattern of progressive disclosure in lots of unexpected places. I've listed a few that occur to me...

<strong>Manifestations</strong>

The scientific method is an iterative process in which hypotheses gradually align to increasingly detailed observation. We learn by progressive disclosure.

Good conversationalists don't gush forever on a topic. They throw out an observation or a tidbit, and wait to see if others are interested. If yes, they offer more info.

The development of a complex organism from a one-celled zygote, through differentiation and all subsequent phases, into adulthood, could be considered a progressive disclosure of the patterns embedded in its DNA. The recursive incorporation of the golden mean in many morphologies is another tie to biology.

[caption id="" align="aligncenter" width="356"]<a href="http://en.wikipedia.org/wiki/File:NautilusCutawayLogarithmicSpiral.jpg"><img class="  " title="nautilus shell" src="http://upload.wikimedia.org/wikipedia/commons/thumb/0/08/NautilusCutawayLogarithmicSpiral.jpg/635px-NautilusCutawayLogarithmicSpiral.jpg" alt="" width="356" height="269" /></a> A nautilus grows--progressively discloses--the protective covering it requires over its lifespan. The golden mean, repeated and repeated... Photo credit: Wikimedia Commons.[/caption]

In journalism, the <a href="http://en.wikipedia.org/wiki/Inverted_pyramid" target="_blank">inverted pyramid</a> approach to storytelling is a form of progressive disclosure. So are headlines.

Depending on how you're reading this post, you might see a "Read more..." link that I've inserted right after this paragraph. Making below-the-fold reading optional is progressive disclosure at work. TLDR...

<!--more-->

Agile software development is a form of progressive disclosure. You start out with vague requirements, and turn your clarifying attention to a small subset, one sprint/iteration at a time. Contrast waterfall, where all requirements must be spelled out in great detail, in advance.

Derivatives and integrals in calculus (not to mention fractals, and lots of other mathematical concepts) capture the result of a limit-as-x-approaches-zero function.

<a href="http://en.wikipedia.org/wiki/Markedness" target="_blank">Markedness in language</a> reveals a linguistic community's preference for what can be assumed or omitted, and what must be explicitly stated. To override the default semantic payload, extra negotiation and effort (the "mark") is required.

<a href="http://www.sprez.com/articles/task-documentation-design.html" target="_blank">Task-based documentation</a> is motivated by the insight that people rarely want to know everything they possibly could about a given topic--they're happier just knowing enough to get their job done, and finding information aligned with their current focus.

In many religious traditions, the idea of reaching higher and higher levels of enlightenment over time is important. A common observation in such world views is that simple beginnings form the foundation for later growth. C.S. Lewis explored this spiritual odyssey in <em>The Great Divorce</em>; he returned to it in <em>The Last Battle</em> with the metaphor of a stable bigger on the inside than the outside, and repeated invitations to "come further up, further in."

In software ecosystems, the increasingly popular philosophy of convention over configuration allows uninteresting details to be deferred and often ignored entirely.

Most education gives high-level summaries in introductory courses, saving complex details for a follow-on.

In gaming, the pervasive notion of "levels" allows the creators to disclose experience a little at a time.

In programming languages, constructs such as default parameters, interfaces, abstract base classes, abstract factories, templates, and mixins all help to minimize the level of detail that must be mastered to work effectively in unfamiliar contexts.

In western culture, traditions of healthy dating and courtship involve a progression of increasing intimacy in which each party gradually comes to know the other more and more deeply, in a variety of settings.

In sports, a champion is often derived through a tournament, in which the best competitors become obvious through repeated elimination rounds.

In music theory, a theme is typically articulated in the opening bars of a composition, and then elaborated and embellished as the piece develops.

Treeviews and fish-eye lenses in software UI are forms of progressive disclosure.

In <em>Great By Choice</em>, Jim Collins' notion of firing bullets, then cannonballs is an attempt to describe how successful companies commit resources incrementally.

In children's literature, the idea of a reiterated and expanded problem or solution crops up repeatedly. Think of Kipling's <em>The Elephant's Child</em>, Hansel and Gretel, Goldilocks and the three bears, Sheherazade...

<strong>The Moral</strong>

What should we learn from this principle's pervasiveness?

I believe one important lesson is that we ignore this principle at our peril. Humans need gradually expanded focus, not sudden overload. Flout progressive disclosure in a conversation, and people will think you're a bore or a know-it-all. Use cheats to get to level 99 in an MMORPG, and you'll miss the experience that makes the game rich. Skip courtship in favor of one-night stands, and you get existential angst.

Applied to software, I think we need to be much, much more aware of when we're disclosing too much too soon. There's a reason why encapsulation is one of the foundational ideas in OO theory, and why tight coupling is a major problem for living software ecosystems.

I have some ideas about how progressive disclosure might manifest more cleanly in programming languages, and in the software craft in general. I explored one in my series of posts on <a title="Role-Play Centered Design" href="../../../2012/06/20/role-play-centered-design/">role-play centered design</a>. I'll disclose some more ideas ... progressively ... in other posts. :-)
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Analyze a piece of code with progressive disclosure lenses. What do you (what does the compiler) have to know about this code to interact with it successfully? For example, does a C++ header #include a bunch of other headers when it could use a forward declaration instead? Could you use the pimpl idiom to decrease what's exposed? Is there a class that should be used through an interface? Do the comments and names disclose the right amount of detail in the right places?</span></em></p>

---

What should code look like when we squint at it? | Codecraft (2013-09-19 08:22:54)

[…] maybe, profound—how nicely this piece of advice maps onto the design principle of progressive disclosure. The human mind is simply wired to perceive in broad outlines, and then to gradually clarify, a few […]

---

Headers, babies, and bathwater | Codecraft (2013-08-12 11:02:29)

[…] is the the first baby that’s being thrown out with the bathwater. Think progressive disclosure: headers could dramatically simplify what a consumer of code has to wade through. If they worked […]