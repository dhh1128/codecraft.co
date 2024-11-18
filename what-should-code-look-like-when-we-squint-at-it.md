---
title: What should code look like when we squint at it?
date: 2013/09/19
slug: what-should-code-look-like-when-we-squint-at-it
---

It's the start of another school year, and my seventh-grade son is learning algebra. As I sat beside him to coach him through some homework the other night, I shared my favorite bit of wisdom about how to make math problems—even complex ones—simple and error-free:
<p style="text-align:center;font-size:110%;border:solid 1px #333;background-color:#eee;padding:1em;font-style:italic;">Write the progression from known to unknown, one step at a time.</p>
In my experience, the surest recipe for disaster is to short-circuit this rule. Collapse a few steps in your head in the name of <em>efficiency, </em>and you'll forget a minus sign, or you'll group incorrectly, or you'll lose track of an exponent or an absolute value—and you'll end up with a mess. You'll have to debug your solution by slogging back through the problem from the beginning until you figure out where you went wrong.

It's interesting—and maybe, profound—how nicely this piece of advice maps onto the design principle of <a title="Progressive Disclosure Everywhere" href="progressive-disclosure-everywhere.md">progressive disclosure</a>. The human mind is simply wired to perceive in broad outlines, and then to gradually clarify, a few details at a time.

Don't believe me? Try a short experiment: draw this fractal.

<figure><img alt="" src="http://farm1.staticflickr.com/45/150592235_fcfe235767.jpg" width="500" height="375" /><figcaption>Fractals embody the principle of progressive disclosure. Image credit: Fábio Pinheiro (Flickr).</figcaption></figure>

I'll bet that instead of laying down every pixel, like a printer, you immediately produce a simplification that captures the general shape as lines, with a lot of detail suppressed. You did this as a kid, when you drew stick figures and triangle+half-circle sailboats.

Artists sometimes squint to blur out what they don't want to see, leaving only general patterns and colors. But coders never do, because we don't expect code to work that way.<!--more-->

<strong>Drowning in details</strong>

I think this is one of the flaws in most programming languages I know: they immediately plunge you waist-deep into implementation details that hide the forest among the trees. To see what I mean, try this experiment, which I did a couple weekends ago:
<ol>
	<li>Download an interesting and complex codebase that you haven't worked with before.</li>
	<li>Try to add a new feature that sounds conceptually simple to your naive ears. For example, just add a command-line switch or make the program crash in a common code path.</li>
</ol>
I did this with the <a title="julia programming language" href="http://julialang.org" target="_blank">Julia programming language</a>, but you could download Mozilla or Apache or Hadoop or anything else that sound interesting, and I think you'd have similar results: like me, I predict that you'll quickly be overwhelmed with questions. Which of 3 likely entry points is the true top of the call graph? What do all these #ifdefs mean, and which ones are going to be active in my build? Which parts of the code have dependencies I need to understand?<a title="download julia programming language source" href="https://github.com/JuliaLang/julia" target="_blank">
</a>

This is the equivalent of trying to solve the entire algebra problem by holding all the transformations of an equation in your head at the same time. It can be paralyzing. None of the techniques that are popular in programming communities today give satisfactory answers to this problem—not BDD or TDD, not golden threads, not design docs, not javadoc/doxygen, not aggressive commenting, not ER or UML diagrams, not architecture description languages.

This need for context, for a high-level picture, for a sketch that gives you a useful skeleton of a <a title="Why Mental Models Matter" href="why-mental-models-matter.md">mental model</a>, is the reason why any new hire into a team with a complex codebase gets a whiteboard-ish orientation from smart teammates. We intuitively know we need it, and we'll never get it from the code itself. On a codebase that I currently own, it is a major reason why the team hates the code and tells horror stories about its learning curve.

There's just no easy entrée.

<strong>What's in a book?</strong>

You could claim that all is for the best in this best of all possible worlds (nod to Pangloss). After all, teams <em>do</em> provide overviews and walkthroughs and design docs, and sooner or later, we get through the learning curve. But I think code could do a much better job of communicating, if we raised the bar.

Think about books for a minute. Hopefully you bought a print book recently enough to remember what it was like to pick it up and consider reading. How did you decide? If you're like me, you probably read a blurb on the front or back cover. Did you glance at the foreword or preface? Did you read the first page to see if it felt interesting? Did you scan a table of contents? Did you flip to an index to see everywhere that your favorite subtopic was referenced?

Code has only weak parallels for these broad-brushstroke mechanisms.  In some sense, the main() routine is like chapter 1—but what comes after that may quickly become indecipherable, especially if you're doing OOP or AOP or event-driven programming. You might liken java packages to a rough structure, but I think that in practice, they only deliver mediocre value because they tend to group by topic, not by code flow or by structural role. Headers insulate you from some details of an implementation, <a title="Headers, babies, and bathwater" href="smart-geeks-think-like-cheerleaders.md" target="_blank">gestalt</a>. Tests as a form of documentation are helpful, but they make it even harder to distinguish major themes from trivia. IDEs give you tree views, but trivia is intermixed with overarching concepts. Nowhere in a codebase do you typically find an explicit discussion about which constructs matter at install time, or which ones are important during startup but not during the later lifetime of the program.

<strong>Toward utopia</strong>

I don't think this lack-of-a-big-picture problem can be solved with a single silver bullet. But here are a few ways that a better programming language/environment/ecosystem might make things better:
<ul style="padding-left:30px;">
	<li><a href="../../../wp-content/uploads/2013/09/screen-shot-2013-09-18-at-10-25-28-pm.png"><img class="alignright size-full wp-image-1326" alt="google maps zoom slider" src="http://codecraft.co/wp-content/uploads/2013/09/screen-shot-2013-09-18-at-10-25-28-pm.png" width="33" height="228" /></a>Imagine a "granularity slider" in a code view, analogous to the zoom in/zoom out slider in google maps. What if a language understood the distinction between vital/domain/first-class objects and trivia, and could suppress details in a treeview or a code editor depending on your current zoom level? (IDEs already support collapsing class and file/folder views, and collapsing or expanding blocks of code. But to my knowledge, they don't analyze a callgraph and decide that some functions are unimportant at a particular level of detail, and they don't collapse file boundaries to make holistic program flow visible at a single glance.)</li>
	<li>Imagine that an IDE could generate, from some combination of static code analysis, profiling, and annotations in the language, a picture of how an application's object model evolves through its lifecycle. And imagine that this diagram's granularity could also be dialed in or out: <em>In the startup phase, you might have a hierarchy of objects that looks like X. In the config phase, it looks like X'. In the collaboration phase, it looks like X''...</em></li>
	<li>Imagine that a programming language supported—or even required—a mapping between a customer-facing use case (a "story" or "golden thread") and a theory of operation (and/or maybe a set of UML diagrams). And a further mapping between a theory of operation and a particular flow through the code. This would mean that you could explore the code at the highest level by saying "show me what happens when the 'Admin cancels a job' story is handled" -- and correlate that to object model state, call graphs, and architectural views at arbitrary levels of detail.</li>
	<li>Imagine that instead of working on an algorithm one function at a time, you could work one subset of a callgraph at a time. So the code for the whole callgraph is displayed as a tree (with adjustable detail). Using a REPL, you feed in a piece of input to a top-level function, and immediately see how those parameters change and flow into all the functions that the top-level function depends on.  (This is a feature of a cool IDE called <a title="LightTable IDE" href="http://www.lighttable.com/" target="_blank">LightTable</a>; I'd love to see it become more mainstream.)</li>
	<li>Imagine a language that lets you stub in rough broad-brush strokes, and just generates stubs automatically. This is two or three steps beyond what IDEs do today, where you can write code and highlight half a line and hit a keystroke that generates a stub, whereupon the IDE switches you to the generated stub and forces you to write an implementation then and there. I want to be able to write a line of pseudocode and have the compiler recognize that it's pseudocode, and just silently generate a stub that will compile, with a default impl that A) writes/logs something telling me the name of the stub I just hit, where it's called from, and what parameters it received; B) matches it to a stubbed unit test; C) lets me assign a hard-coded value; D) embeds a breakpoint in the impl such that when I run in a debugger, and hit the stub, I am prompted to supply more impl or more hard-coded values. I want to do all of that without breaking the flow of the higher-level algorithm I'm working on. Something like this:</li>
</ul>
<pre style="margin-left:3em;margin-right:5em;margin-bottom:2em;font-size:9pt;border:solid 1px gray;padding:1em;"><span style="color:green;">// normal function, not stubbed</span>
<span style="color:blue;">int</span> x = do_something(); 
<span style="color:green;">// stub declared, assigned a placeholder return value,
// and expected to compile with a working unit test
// without me ever leaving my flow</span>
<span style="color:blue;">int</span> y = do_something_else(a, b) <span style="color:#a0a;">stubbed with return</span> 25;</pre>
<ul>
	<li>Imagine that you could create classes without declaring their methods, and then start a debugger session where you (and teammates) could role play different class interactions to model what you expect to have happen--and that as you role played, the IDE recorded your choices as new stubs, methods, and workflows, so that by "playing" the system, you gradually build it. (See my <a title="role-play centered design" href="../../../?s=rpcd">posts about role-play centered design</a> for more on this.)</li>
</ul>
I have a few other ideas about how progressive disclosure might work in a <a title="better programming language" href="../../../category/better-programming-language/" target="_blank">better programming language</a>, but I think I'll stop there. I'm very curious to see if other smart people out there have good suggestions of their own.
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Tell me what you think would make it easier to perceive the rough behavior and structure of a big, complicated codebase in more efficient ways.</span></em></p>

<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://blog.jetbrains.com/pycharm/2013/08/working-with-uml-class-diagrams/" target="_blank">Working with UML class diagrams</a> (jetbrains.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://techblog.stickyworld.com/abandoning-php-for-python.html" target="_blank">Abandoning PHP for Python</a> (techblog.stickyworld.com)</li>
</ul>

---

trevharmon (2013-09-19 14:45:15)

Daniel, I know you and I discussed this for some length of time earlier, but I've come across another thought. And, it deals with the different approaches we use when coding. Naturally, I can only use myself as an example.

I wonder if some of this behavior comes from doing some form of bottom-up programming. What I mean by this is after the brainstorming that goes on when planning a project, do programmers naturally start by building the objects or building the flow?

Let's compare this to writing a paper vs. a computer program.

If I'm writing something small (e.g., for my blog), I'm likely to just do stream-of-conscience writing. Whatever comes into my head as the next logical step will be put directly written down without much thought. I do the same thing with quick-and-dirty scripts.

Now, when I'm writing something larger, my behavior changes. Even though the brainstorming may have resulting in many, many individual pieces, I start the actual writing process by defining a clear flow of ideas (usually through defining chapter/section/sub-section headings). The details are then filled in using the brainstormed material.

When coding a large project, I tend to do something different. Instead of starting with the overall flow, I go to creating the underlying objects. I build all of this infrastructure-providing pieces first. Later, I go back and add the logical flow. While both tasks are completed, it's clear my main focus is on the building blocks, not the overall flow.

Interestingly enough, on medium-sized programming projects, I do sometimes follow the pattern of doing flow first. That's seen in the progressive disclosure MAIN: section we were discussing. I have a section of code at the beginning of an obvious file that consists of the following:

- Initialization
- Functions and flow control
- Termination

In this case it's always clear what the flow is and everything else is built around it. If I do this first and use good function names, those function (in their call order) are then copied to later in the file to be used as the skeleton for the rest of the code.

Obviously, these are not large projects and are heavily skewed to procedural programming paradigms. As stated, in larger code bases my behavior appears to be different.

So, that's my long-winded way of agreeing with you that program flow and progressive disclosure are often not given the level of attention they deserve.

---

Daniel Hardman (2013-09-20 12:27:14)

Vladimir: I had not thought about how codebases are often associated with books, and how those books provide the sort of "granularity slider" I was wishing for. That's a good insight! Thanks.

I am somewhat familiar with SPARK, but I need to study it a little more. I think that it provides one kind of progressive disclosure, but not many of the other ones I want.

Thanks for the thoughtful comment!

---

Vladimir Starostenkov (2013-09-20 09:36:17)

Daniel, I thought you were talking mostly about project with existing code base in the post. Looks like Trev starts from scratch or POC. That's a huge difference. Consider adding few lines into linux kernel without being professional in it. No way. You have to take a book which has this built-in “granularity slider”.

You mentioned Hadoop. That's one more case. That's easy to read a pair of papers on Map-Reduce paradigm, look through a book on Hadoop and write your project on top of it. But you don't need to go through Hadoop code at all. That is why Hadoop is popular. The same case is Qt for C++ developer. You don't have to know how it works to use it properly. You have to accept the paradigm. If you want to learn the core without the “granularity slider” - you'd better start from scratch. Qt has it's audience not only because it's architectural integrity, but detailed documentation.

One more interesting example is SPARK project by Berkley AMP lab. It gives a Scala programmer the ability to work with distributed data structures just the same way he does with the local ones. That is against "Artists sometimes squint to blur out what they don’t want to see, leaving only general patterns and colors. But coders never do, because we don’t expect code to work that way." Sorry :)

---

Daniel Hardman (2013-09-19 21:52:39)

Interesting analysis, Trev. You've got me wondering if I do the same thing. I know I jump right into flow on small stuff, but I'm not sure what I do on large stuff; next time I embark, I'll turn my radar on.

I wonder if the "create the objects first" behavior comes from a subconsciously recognized need to have useful tools at your disposal before exploring flow. Maybe we can't think about flow until we have the object-level constructs to work with...

---

Why you should use an IDE instead of vim or emacs | Codecraft (2014-05-13 10:16:50)

[…] I’ve got some exciting ideas that I’m eager to share. Much of what’s possible is more likely to be realized in an IDE; where I’m headed, text editors won’t be […]

---

On Forests and Trees | Codecraft (2015-09-02 08:48:51)

[…] way to tell that code’s been wisely generalized is to ask yourself this question: “Can I see the forest for the trees?“ If a quick glance at any level of detail (a class, a function, a module, a project […]

---

Exploring the Power of Deixis | Codecraft (2014-09-23 08:34:54)

[…] to “flatland” dimensions. What might be the analog to image maps or tag clouds in a visual view of code? Could we shop in dependency stores and fill our carts with “code reuse packages”? […]