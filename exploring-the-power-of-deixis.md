---
title: Exploring the Power of Deixis
date: 2014-09-23
slug: exploring-the-power-of-deixis
redirect_from:
  - /2014/09/23/exploring-the-power-of-deixis
---

The other day my daughter was in the backseat as I pulled out of the driveway, and she instructed me to "turn that mirror over here."

"Which mirror?" I asked.

"That one," she said, without any clarification.

<figure><img class="" src="https://farm3.staticflickr.com/2207/2271777379_330a7108f4_z.jpg" alt="" width="640" height="426" /><figcaption>Image credit: fofie57 (Flickr)</figcaption></figure>

"<em>Which</em> one?" I said again. "I don't know what you mean when you say 'that'..."

Eventually I cracked the teenage code and tilted the center rearview mirror toward her so she could check her makeup. :-) But it was harder than it should have been.

A lot of frustration could have been avoided if I could have turned around to face her to see which direction her eyes were pointing--or if she'd just stretched out her finger.
<h3>Deixis</h3>
In linguistics, deixis is a sort of pointing—the juxtaposition of something against a reference context to provide meaning. Although we can define words like "here" and "there" in the abstract, their specific meaning always depends on the physical or metaphorical location of the speaker when they're used. Likewise, "now" and "then" are deictic with respect to the time of an utterance; pronouns like "we" and "you" use deixis that relies on interpersonal context; honorifics are deictic with respect to cultural relationships.

Since the web now permeates our collective experience, think of deixis as a kind of hyperlink. Imagine if I had written my daughter's sentence like this: "Turn <span style="text-decoration:underline;"><strong><span style="color:#333399;text-decoration:underline;">that</span></strong></span> mirror over <span style="text-decoration:underline;"><strong><span style="color:#333399;text-decoration:underline;">here</span></strong></span>." It sorta fits, doesn't it?

<!--more-->

That's no accident. Deixis and hyperlinks both involve pointing. Both enrich communication. Both allow semantic relationships to be built or discussed with minimal redundancy.
<h3>Deixis in code</h3>
Source code was doing hypertext long before anyone had heard of html. Function declarations, definitions, and invocations; variable declarations and uses; pointers; typedefs; objects and classes--all have reference/referent relationships. We even have a <code>this</code> pointer in many languages.

However, today deixis in code has some frustrating limitations:

<dl><dt>Many constructs in code are only valid referents in narrow constructs.</dt><dd>Preconditions and postconditions? No way to reference those except in doc. Dependencies? Can't declare them except at the module level with <code>import</code> or <code>#include</code> statements, and they're only a crude hint about true dependency relationships.</dd><dd>The return value and parameters of a function are easy to reference inside a function, but hard to reference outside it. There are workarounds--javadoc conventions let you write <code>@param</code> and <code>@returns</code>, and some languages let you name parameters as you invoke a function: <code>do_something(param3=x, param4=y)</code> But this is weak. Show me how I can use the return type of <code>functionA</code> as the data type of <code>paramX</code> of <code>functionB</code> without simply repeating myself, or without a code monstrosity that's uglier than simple repetition. (Yes, I know you can play slick tricks with templates to extract some of this info. But the code is mysterious, verbose, and not as broadly applicable as it ought to be.)</dd><dt>Many constructs in code are not valid referents at all.</dt><dd>How many times have you written code that looks like this:
<pre><span style="color:green;">} // end namespace foo</span></pre>
...or this:
<pre><span style="color:green;">#endif // win32</span></pre>
...or this:
<pre><span style="color:green;">// Always make sure this value is checked again, after
// the main loop but before final cleanup section. See
// the "CHECK AGAIN HERE" comment about 60 lines below.</span></pre>
Each of these comments is a workaround for something we can't easily point to.

And then there are all those human concerns that ought to be expressible in code, but are not--and because they are not, they can't be referenced, either. How can you hyperlink to a persona from the code that implements special behavior to make that persona happy--if a persona isn't even a valid topic for your source code? (This is the whole <a title="Lacunas Everywhere" href="lacunas-everywhere.md">lacuna humana</a> topic thatrecently explored.)

</dd><dt>The predominant, generic way to point at something in code (line numbers) is incredibly fragile.</dt><dd>What is the half-life of a line number in code?</dd><dd>One code checkin, maybe.</dd><dd>It is possible to remap line numbers across diffs, but it is an inexact science, and it's hard.</dd><dd>Most developers never notice, because we only <a title="In Which Warnings Evolve Wings" href="in-which-warnings-evolve-wings.md">worry about warnings</a> until our current build succeeds. But what if you use a static code analyzer like Coverity? Coverity builds up a DB of issues that developers are supposed to resolve over time, and the issues need to retain their identity even when line numbers change. Notice the permanent issue ID (CID 13674) versus the line number (line 421) in this screen shot:
<img class="aligncenter" src="https://cloud.githubusercontent.com/assets/2208904/2715771/cf7078f0-c515-11e3-80f6-4452c181f4b5.png" alt="" width="828" height="281" />
It turns out that Coverity has partly solved this problem (and I take my hat off to their dev team for doing so)—but whatever secret sauce they use, it is not something that's available for easy use by the programming community. Referring to a chunk of code at a specific "location" over its maintenance lifetime is almost guaranteed to be problematic due to changiline numbers at the very least—plus maybe changing filenames, directories, class names, namespaces, visibility, and so forth.</dd></dl>
<h3>What's the big deal?</h3>
You might say that this is an imaginary problem. After all, we've been coding for decades, and the whole system seems to work okay. We can point at the stuff we need, right? Our linkers usually find the externals they need to bind together, and our <a title="Why you should use an IDE instead of vim or emacs" href="why-you-should-use-an-ide-instead-of-vim-or-emacs.md">IDEs usually find the decl</a> for variables when we ask. The rest must not matter all that much.

I think that assertion is akin to a librarian in 1990, arguing that since books have tables of contents and indexes, and since there's a nice card catalog available for patron use, hypertext is not going to be particularly useful. Any benefits of the newfangled "web" will turn out to be illusory.

With the benefit of hindsight, would we buy that librarian's logic?

I think not.

Likewise, I suspect we really have only a vague appreciation for what we're missing by limiting ourselves to the clumsy pointing mechanisms that code provides today. Hyperlinks made ecommerce possible. Hash tags and @ mentions (more digital deixis) power social media. Search engines evaluate the relevance and value of content based on relationships that were undiscoverable before we had hypertext. VR worlds, Foursquare, Google Glass... all possible because of deixis.

<a name="examples"></a><h3>Innovation examples</h3>
Imagine what unfettered code deixis might do. What if instead of clumsy attempts to "turn that mirror over here" we had a finger that could easily and unambiguously idify targets for our ideas? Suppose we could point to code constructs across space and time instead of being limited to "<a href="what-should-code-look-like-when-we-squint-at-it.md">visual view of code</a>? Could we shop in dependency stores and fill our carts with "code reuse packages"? Would we be able to build something akin to vendor reputation for contributors of blocks of code? Could we trace code genealogies? Would we create more robust mappings between tests and requirements and coders and personas and use cases...? Could we point to design patterns or performance bottlenecks?

One of the goals of the <code>intent</code> programming ecosystem I've <a title="My First Tangle With the Tower of Babel" href="my-first-tangle-with-the-tower-of-babel.md">begun to create</a> is to empower this sort of deixis without creating any new overhead for engineering teams. As I've studied the problem, I've become convinced that there are mechanisms that deliver more deictic utility while respecting this goal—simultaneously saving time and increasing power. It's the sort of happy combination that made the web catch fire.
<h3>The way forward</h3>
So how do we bring code fully into the hypertext age?

I'm trying to turn over a new leaf and stop writing such long posts, so I'll lay out the solution I've begun to imagine in a follow-on installment soon. I'm not being coy; I'm just trying to take this one step at a time, and I'm running out of time to write before bedtime. :-)

I'll say this much tonight. Hypertext requires anchors, and anchors require names. Part of the problem with code today is that many constructs have no name. Humans have all sorts of strategies for dealing with unnamed items ("I like those blue flowers"; "Go 2 blocks straight ahead, then take your first left"). A smart compiler could emulate some of them. Humans also tend to triangulate with names (use more than one name for the same item), because they <a title="Why Mental Models Matter" href="good-code-is-named-right.md">some names are more intrinsic than others</a>. Again, a programming ecosystem could facilitate this.

Did I whet your appetite?

Tune in for a follow-up shortly.

