---
title: Good Code Is Named Right
date: 2012/08/28
slug: good-code-is-named-right
---

<p style="text-align:right;"><em><span style="color:#404040;">(Another post in my "<a title="What Is “Good Code”?" href="what-is-good-code.md">What is 'Good Code'?</a>" series...)</span></em></p>
A rose by any other name may smell as sweet, but in software, the names you choose have consequences.

<figure><img title="rosa berberifolia" src="http://farm1.staticflickr.com/28/51430866_94b353ee35_m.jpg" alt="" width="240" height="225" /><figcaption>Rosa berberifolia. Photo credit: I Believe I Can Fry (Flickr).</figcaption></figure>

Names can confuse or cohere. In <em>The Mythical Man-Month</em>, Fred Brooks emphasizes the need for code to have "conceptual integrity." He means that code that should embody a unifying and consistent vision, with minimal distraction or dissonance. Names of classes, functions, applications, interfaces, resources in RESTful URLs -- all are a reflection of the code's cohesiveness or its chaos.

I once worked with an engineer who liked to pull variable names out of the random hopper at the top of his brain: "apple", "banana", "ick"... Although his code provoked an occasional snort of amusement, it didn't do much to guide later readers into a productive mindset.

One way I can distinguish a mediocre engineer from a great one is by the quality of their language--particularly, the names she or he chooses. Mediocre engineers are sloppy and inconsistent in their names, because they undervalue the way their code communicates to human beings. Mediocre engineers think that comments are for humans, and code is for computers. Code, like java or C++ or ruby, doesn't communicate to computers at all, folks; it has to be turned into op-codes and 1s and 0s before a computer can use it! Code is <em>human language</em>. Comments are like parenthetical asides in normal human speech -- needed occasionally, but annoying if they restate the obvious and distract from flow.

Good engineers understand this. It bothers them if something is called a "Controller" in the code, but it fails to implement IController. It bothers them if .ReadLine() doesn't always read a line of text from a file; when they run across such a function, they are prone to rename it ReadUpToAFullLine() so the function's semantics are obvious. If they implement a method that calculates a standard deviation, they are likely to name it something like calcStandardDeviation() instead of stdv() or calc(). (This is not about naming conventions, BTW. I don't have a problem with short forms or whatever casing convention you prefer; I'm just emphasizing clarity.) Code from great engineers says what they mean, and means what they say. Notice how Martin Fowler (a great engineer) takes this for granted as he discusses an appropriate name for a class in <em>Refactoring</em>:
<blockquote>Does the price class represent an algorithm for calculating the price (in which case I prefer to call it Pricer or PricingStrategy), or does it represent a state of the movie (<em>Star Trek X</em> is a new release). At this stage the choice of pattern (and name) reflects how you want to think about the structure. At the moment I'm thinking about this as a state of a movie. If I later decide a strategy communicates my intention better, I will refactor to do this by changing the names.</blockquote>
Somewhere (maybe Scott Meyers?) I remember reading an expert's lament about people naming classes FooManager, BarManager, etc. His point was that "Manager" says little or nothing about the class's responsibilities. I agree (although I must admit I've written a few XManager classes in my time :-).

Truly<em> great</em> engineers take the language insight of good engineers one step further. Not only do they want clear and consistent names--they want their code to resonate to a unifying metaphor.

In the early days of ecommerce (I was writing CC processing stuff in about 1996), nobody talked about "shopping carts." You just wrote code that accepted credit cards, and you kept track of what the user wanted to buy until they were ready to pay. You accumulated customer state in your session, or maybe your db, in whatever way you could cobble together. Messy. Once the shopping cart metaphor was introduced, it was easy to see how you could let a customer change quantities at the last minute, handle partial payments with different cards, apply discounts and coupons, and so forth.

The power of metaphor in code is so pervasive that it may be invisible unless you're looking for it. Good metaphor leaks from coders to their managers and marketers and support staff and tech writers--and because it explains so much, so clearly and concisely, the audience gloms onto it immediately. From there it leaks out to customers and the blogosphere, and we start taking it for granted. Which says more to you: "a software application that lets you pretend to be running a full OS with simulated hardware" or "virtual machine"? How about "self-replicating program that subverts the normal purpose of software" or "virus"?
<p style="text-align:center;padding-left:30px;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Find a place in code where comments are compensating for a class, function, or variable with a less-than-ideal name, and fix it.</span></em></p>
<p style="text-align:center;padding-left:30px;"><span style="color:#000080;"><strong>Extra Credit</strong></span></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Find a place in code where you have a weak or inconsistent metaphor. List implications of that metaphor problem. Brainstorm improvements; if one of the improvements seems particularly helpful, implement it.</span></em></p>

---

Exploring the Power of Deixis | Codecraft (2014-09-23 08:35:03)

[…] than one name for the same item), because they understand that names may be temporary, and that some names are more intrinsic than others. Again, a programming ecosystem could facilitate […]