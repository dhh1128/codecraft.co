---
title: On bread recipes, maps, and intentions
date: 2013-10-24
slug: on-bread-recipes-maps-and-intentions
redirect_from:
  - /2013/10/24/on-bread-recipes-maps-and-intentions
---

<p style="font-style:italic;margin-left:3em;font-size:92%;color:#555;">[I've been quiet for the past three weeks &mdash; not because I have less that I want to talk about, but because I have more. Major wheels turning in my head. I'm having a hard time getting from the "intuited ideas" mode to the "crisp enough to put it in writing" mode, though. Consider this a down payment on some future discussions...]</p>
One of my mother's talents is bread-making. She's been kneading and baking and pulling beautiful loaves out of the oven for as long as I can remember. Bread is one of the ways she says "I love you" to family and friends.

<figure><img alt="" src="http://farm5.staticflickr.com/4121/4860405142_3c49fd683f.jpg" width="500" height="500" /><figcaption>photo credit: <a href="http://www.flickr.com/photos/treehouse1977/4860405142/" target="_blank">treehouse1977 (Flickr)</a></figcaption></figure>

A few years back, she created a cookbook full of family recipes, and gave one to each adult child for Christmas. I was struck by how she began the bread section. Instead of launching right into the recipes, she included a couple of pages of "bread theory", if you will. The section about water is typical:
<p style="padding-left:30px;">"Water &mdash; Just about any edible liquid could be used as the base for bread. Some that come to mind are vegetable cooking water, potato water, milk, and so on. There is no problem with substituting any of these for liquid called for in a recipe, but you should keep in mind that if the liquid is salty, the salt should be adjusted; if the liquid is sweet, the sugar should be adjusted... Fresh milk can be a problem because of enzymes that would prevent yeast action. For this reason, most old recipes that call for milk specify that the milk be scalded first. This isn't necessary if you are using water and powdered milk, but remember that the mechanics of the recipe probably depend on at least warm milk (so use warm or even hot water)."</p>
If you're wondering why I am writing about bread recipes in this blog that focuses on software craftsmanship, consider how much that paragraph resembles a really high-value comment in source code.

It has to do with principles and <em>intentions</em>.

<span style="color:#000080;"><strong>Software is all about recipes, right?</strong></span>

Recipes are a lot like software algorithms (especially in <a class="zem_slink" title="Imperative programming" href="http://en.wikipedia.org/wiki/Imperative_programming" target="_blank" rel="wikipedia">imperative programming</a> styles): First, do this; next, do that; wait 25 minutes; <code>return new Loaf()</code>... We even talk about "recipes" and "cookbooks" when we make catalogs of software techniques.

How is this metaphor instructive... or worrisome?

It is not an accident that my mother, a master bread maker, feels the need to describe intentions and their ramifications before laying out the "procedural code" of her individual bread-making subroutines. She has hard-won expertise, and she knows what governing principles need to be understood by anyone wanting to follow in her footsteps.

Think about that for a minute: <em>governing principles need to be understood</em>. Notice the implicit value that's placed upon the intelligence of those who come behind.

Do you really need to understand <em>principles</em> to follow a recipe <em style="color:#555;">[compile or execute a subroutine]</em>? Or can you just be a mindless automaton, given sufficiently detailed instructions?

How you answer that question says a lot about how deeply you understand the craft of breadmaking... or software.

<span style="color:#000080;"><strong>A detour with a map</strong></span>

Let me triangulate on the value of intentions with a little thought experiment. Hang with me and I promise we'll end up somewhere interesting...

Suppose a long-lost friend finds you on Facebook, renews happy memories, and proposes a meeting. You gladly agree &mdash; but the rendezvous point is a place you've never visited, so you ask for directions. Your friend looks up the destination on Google Maps and emails step-by-step navigation instructions to you.

But there's a problem.

Your friend is a bit careless with a mouse, and what they copy happens to miss the top few lines (the part that says "Directions from Point A to Point B"). In the interest of brevity they also omit the last line that says "You've now arrived at Point B." (After all, your message stream on Facebook already identified where you're meeting...) And to make matters worse, your friend assumes you still live in your old neighborhood, even though you moved across town years ago. So the starting point is wrong.

You barely glance at the directions when they arrive in your email. What could go wrong, when you've got 15-step instructions from Google, accurate to a tenth of a mile? When the day of the meeting arrives, you rush out the door with a printout of the instructions. Four blocks from the house, as you wait at the light by the main road, you glance at the paper, and your brow furrows...

<span style="color:#000080;"><strong>Intentions to the rescue</strong></span>

In the age of smart phones, this example is a bit contrived. Most of us would immediately pull over and call our friend to get clarification, and we'd have a happy ending. (Notice how I promised you a happy ending to our thought experiment detour, before I began that section of this post? People need to know where you're headed...) I'll go further: nowadays, we'd usually get a hyperlink to the navigation instructions in the first place, instead of step-by-step text divorced from context. If the hour of departure arrived, and we found ourselves leaving from a kid's soccer game instead of from our own driveway, we'd let the GPS adjust the first few steps of the instructions automatically.

Like smart humans navigating in traffic, master breadmakers know dozens of ways to adapt to variations and still end up with a superb loaf &mdash; and they know that knowledge will come in handy, sooner or later. This is why my mom spent time explaining general principles.

Strategies for smart adaptation depend on... you guessed it: <em>understanding intentions</em>. If you know where you intend to go, adapting wisely is practical and straightforward. If you don't, you're in trouble.

A lot of the best practices I've advocated on this blog &mdash; and a lot of tantipatterns I've lamented &mdash; are evidence of this principle at work:
<ul>
	<li><a title="Good Code Is Named Right" href="good-code-is-named-right.md">Goodde is named right</a>, because it tells another coder what you intend for it to do. (Notice how much confusion in our thought experiment is attributable to the missing title on the navigation instructions. Notice how breadmaking recipes start, not with ingredients, but with a title.)</li>
	<li><a title="// Comments on Comments" href="coding-standards.md">waste of time</a> when theust state the obvious or provide no insight.</li>
	<li>Building <a title="Why Mental Models Matter" href="why-mental-models-matted">accurate mental models</a> is a function of understanding the intentions of users and system designers.</li>
	<li><a title="Smart Geeks Think Like Cheerleaders" href="smart-geeks-think-like-cheerleaders.md">System thinking</a> is enabled by a grasp of the principles underlying various components, coupled with pondering about the ramifications of those principles as the system encounters dynamic conditions.</li>
	<li><a title="Good Code Plans for Problems" href="why-your-software-should-cry.md">communicating</a> when intentions aren't satisfied.</li>
	<li>A major reason why I keep harping on Martin Fowler's observation ("Any fool can write code that a computer can understand. Good programmers write code that humans can understand.”) is that it recognizes the primacy of human understanding of <em>intention</em> &mdash; not just Turing completeness or Von Neumann executability &mdash; in writing software.</li>
</ul>
I could go on and on, but I'll leave other examples as an exercise for the reader...

<span style="color:#000080;"><strong>A critique of most programming languages</strong></span>

As I've written before, I decided to explore the idea of <a title="Headers, babies, and bathwater" href="headers-babies-and-bathwater.md">writing a new programming language</a> because I wanted to deepen my understanding of theoretical CS and also of the craft in general.

It's been instructive. Pretty quickly I concluded that simple syntactic sugar was a waste of time &mdash; and that I'd dipped my toe in a mighty deep ocean. But another insight has gradually come into focus as well:
<p style="margin-left:2em;margin-right:2em;border:solid 1px #606060;padding:1em;background-color:#f0f0f0;font-weight:bold;font-size:105%;">Most programming languages pursue the goal of communicating unambiguous instructions to a computer with maximum power or elegance, and relegate human needs to optional, secondary status. They exhibit surprisingly similar weaknesses as a result.</p>
It's ironic. We expend vast time and effort trying to improve the UX of our products, but we're using programming languages that themselves have a UX prejudiced toward the compiler and the CPU, not the coders.

Some quick examples will show you what I mean:

1. How many programming languages require you to describe the users of the system, write stories about their use cases, or map those use cases to specific paths through the code? How many allow you to attach whiteboard diagrams to lines of code, and have IDEs that automatically display those whiteboard diagrams when the context is right?

2. Why is Bertrand Meyer's design-by-contract methodology an optional library in so many languages, but not a first-class feature? Why do compilers do so little with preconditions and postconditions? (Think about how these concepts clarify intention...)

3. How often have you seen a block of code, in any programming language, that looks or feels like this:
<pre style="font-size:105%;">    <span style="color:green;">// Validate that policy constraints apply.</span>
    <span style="color:blue;">if</span> (*maxMigrations == 0) || 
        (*policies->migrationsDoneForNode)(loads,vMLoads,nodeItem,vMItem) == <span style="color:blue;">true</span> ||
        (!vMIsEligible(vMItem,FALSE) && (migrationType != vmmpFeatureCheck)))
    {
        <span style="color:green;">// do something awesome</span>
    }</pre>
 

Suppress your gag reflex and think about where intent and humanity is manifest in this snippet. The language syntax requires you, for a conditional statement, to tell the compiler how to make a decision &mdash; but it doesn't require you to provide any clarification about why that decision matters, how a human might describe the choice, or what you're hoping to accomplish. The only evidence of intent is the anemic comment. No wonder we burn the bread so often!

<span style="color:#000080;"><strong>Hope on the horizon</strong></span>

Notice that I wasn't universal in my critique just now. I see bright spots of innovative, intentional thinking in many places. <a title="Dan North: Introducing BDD" href="http://dannorth.net/introducing-bdd/" target="_blank">Behavior-driven development</a> is about validating code behavior against use cases, which is promising. The DSLs and testing specs in <a title="cucumber testing" href="http://cukes.info/" target="_blank">cucumber</a> and <a title="spock unit test framework" href="https://code.google.com/p/spock/" target="_blank">spock</a> are elegant and actionable exprions of intent. <a title="Eiffel DBC" href="http://www.eiffel.com/developers/design_by_contract.html" target="_blank">Eiffel bakes design-by-contract</a> into the language. Charles Simonyi's work on <a title="intentional programming" href="http://en.wikipedia.org/wiki/Intentional_programming" target="_blank">intentional programming</a> is really cool, even if Microsoft Research dropped the idea a few years back. Heck, the whole phenomenon of TDD and disciplined unit testing is about making sure we understand our intentions...

I've also imagined some ways that a new programming language/ecosystem/methodology could raise the bar for our craft even further &mdash; ways that recognize the human dimension, that are simple to learn and use, that can be implemented without science fiction, and that are likely to pay off big. I'll be blogging about these ideas in future posts, and I'm using the name "intent" for the effort. Hopefully this will culminate in an "intent" compiler, an "intentional" IDE, and so forth. (Thanks to my friend <a title="Julie Jones: Learn voraciously." href="julie-jones-learn-voraciously.md">Julie</a> for suggesting this name and collaborating with me on the effort. Anybody else want in?)

In the meantime, I'd be very interested in your thoughts. Where do you see lack of clarity about intentions as a problem in code? What techniques address the need?













