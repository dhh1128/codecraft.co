---
title: How to make a const-correct codebase in 4300 easy steps
date: 2014/03/25
slug: how-to-make-a-const-correct-codebase-in-4300-easy-steps
---

One of the codebases that I work on is theoretically C++, but if you peer under the hood, it looks more like 1990-vintage C. It's 500 KLOC of almost purely procedural code, with lots of structs and few true objects. More dusty and brittle than I'd like.

<figure><img src="http://farm3.staticflickr.com/2357/2090235485_56a89491d4.jpg" alt="" width="500" height="375" /><figcaption>Image credit: <a href="http://www.flickr.com/photos/tgillin/2090235485/" target="_blank">Tim Gillin</a> (Flickr)</figcaption></figure>

I am not a C++ bigot; I first began to do serious, professional coding in C, not long after this codebase got its start. I understand the C-isms pretty well. And although I think Linus got carried away in <a title="linus rant c++" href="http://article.gmane.org/gmane.comp.version-control.git/57918" target="_blank">his rant about the ugliness of C++</a>, I can appreciate the ways that lean C sometimes makes its descendant look ugly and inefficient. (Though C++11 and 14 are making this less true...)

This means that I don't consider the C-like style of this particular codebase a fatal flaw, in and of itself.

However, since my early coding adventures I've been converted to the advantages of OOP for complex projects and large teams, and I've also accumulated a lot of battlescars around multithreading. Our codebase needs OOP to solve some encapsulation antipatterns, and it needs RAII and C++11-style mutexing in the worst way. Its old, single-threaded mindset makes far too many things far too slow and error-prone.

A few months ago, we decided to make an investment to solve these problems.

To do it right, I had the team add a story to our scrum backlog about making the codebase const-correct. And therein lies a tale worth recounting...

<!--more-->
<h3>The naive approach</h3>
At first, the team assumed that I wanted a human being to manually inspect every parameter to all ~4300 functions in the whole codebase, adding "const" wherever it belonged.

They weren't thrilled. Although most were too polite to say so, they probably questioned the value of the exercise, privately wondering some of the same things that are articulated in <a href="http://stackoverflow.com/questions/136880/sell-me-on-const-correctness" target="_blank">this StackOverflow post</a>. They complained that as soon as they tried to fix const in one place, it had a domino effect that caused endless ripples elsewhere.

I convinced them to give it a shot with two arguments:
<ul>
	<li>The code could not be robustly multithreaded until we knew which functions modified which state--and thus, where mutexes were needed. The best way to codify that knowledge is to use const, because it's terse, standard, and enforced by the compiler.</li>
	<li>Perhaps more importantly, I knew a way to upgrade the whole codebase, with near 100% accuracy, with very little effort. And I could solve the ripple effect.</li>
</ul>
<h3>The clever approach</h3>
My idea for automated const-fixing was simple, I thought. I would write a python script that embodied the following algorithm:
<ol>
	<li>Use doxygen to generate call graphs for the whole codebase.</li>
	<li>Given a whole-codebase call graph, identify all "leaf" functions (functions that are only called, but are not themselves callers, of anything else in the codebase).</li>
	<li>For each leaf, find all function prototypes, including the one associated with the implementation.</li>
	<li>For each prototype on a given leaf function, iterate over its parameters. On parameters where "const" might make sense but where it is not present, add "const" and see if the code still compiles and all unit tests still pass.</li>
	<li>Prune all leaf functions from the call graph and repeat until no functions remain.</li>
</ol>
<h3>Turtles all the way down</h3>
I was hoping that after I described this straightforward algorithm, an enthused team member would volunteer. Nobody spoke up.

"Okay, I'll do it," I said. "I ought to be able to get that done in a few days."

Famous last words...

At first, I made steady progress. The skeleton of the script was done after an hour or two of coding.

Adding reliable "roll back a change that turned out to be invalid" logic took me another hour or so to code and test. And adding parameter fuzzing (so that a parameter declared <code>Foo * foo</code> in one place, <code>Foo *myfoo</code> in another, and <code>::Foo *</code> in another, would all be seen as semantic equivalents) took another hour.

Then I started cautious experiments to see how well my script was doing.

Ugh.

I already had regex-based python code that scanned code for function prototypes. Having done this sort of thing before, I knew that I was going to miss a few subtleties. I knew I'd have to handle inline <code>/* ... */</code> and <code>// ...</code> comments, and maybe an <code>#ifdef</code> here or there. I knew there were a handful of macros in the codebase, but I was pretty sure there was nothing truly insidious. I figured I'd get at least 95-98% accuracy pretty quickly, because the formatting was very regular. Because I could rely on the compiler to tell me if something broke, and because I had a robust rollback mechanism, the worst that could happen if I mis-parsed something was that I'd fail to add a "const" that might have been theoretically possible.

Here are few of the gotchas that I didn't anticipate, but that in hindsight should have been obvious:

<dl><dt>The imperative to minimize diffs</dt><dd>When I rewrote code, my first attempt reformatted the function prototype slightly. I dropped extra whitespace, and I didn't keep the original linewraps and indents. I figured this would not be a problem. However, on closer inspection, I realized that a lot of prototypes looked like this:

https://gist.github.com/dhh1128/9753554

The problem was that if I did a dumb rewrite of the function, I'd end up dropping the helpful comments. Also, my naive implementation drastically increased the noise in the diff, which was a big problem since we maintain half a dozen active branches of code for old maintenance releases, and depend on automatic merges to make bug fixes flow with minimal human intervention. It took me another hour or so to rewrite my "prototype rewrite" code so that it made the minimal possible change to alter constness.</dd><dt>Function pointers</dt><dd>Some function pointer declarations (as parameters, or as typedefs) gave my parser fits. I had to beef up my "function_decl" regex several times before I stopped getting false positives.</dd><dt>Typedefs</dt><dd>Sometimes a function was declared with one datatype, but defined using a typedef'ed alias. This caused my parameter correlation between the two instances of the prototype to fail. I ended up hard-coding my way around one particularly nasty instance of this. (Why not just fix the code, you ask? Excellent question. Remember my mandate to minimize diffs? Darn inconvenient...)</dd><dt>Function overrides</dt><dd>What if the same function name had more than one possible set of parameters? I couldn't just change the constness of the third parameter to <code>CalculateIdealWidgetSize()</code> blindly; I had to recognize clumps of functions that had a common parameter profile.</dd><dt>Mocks and stubs</dt><dd>This codebase includes a bunch of google test and gmock stuff. Each procedural function has its own testrunner, which links in a library of stubs for all the other functions in the codebase. This means that any given function in the codebase typically has 2 implementations (one real, one mocked), and often several different declarations. The mock declarations are in a totally different style from normal declarations. Some examples of mock declarations will give you a flavor:

https://gist.github.com/dhh1128/9754282

I had to not just find and update ordinary function prototypes, but all their mocked equivalents as well, in whatever mocking variation they might appear. And I still needed to be able to correlate all the variants so I could make a coherent change across all instances of a particular function.</dd><dt>External APIs</dt><dd>At first, I was attempting to change every function prototype that I saw. However, I realized after a while that some <code>extern</code>ed function declarations referred to functions exposed by dynamically linked libraries. The code would compile when I changed the <code>extern</code>ed declaration, and tests might even pass--but at run-time in production, I might fail to link the function I wanted. I modified my script to only update prototypes where I could find at least one definition; if all I saw was declarations, I left the functions alone.</dd><dt>Doxygen bugs</dt><dd>A week or so into the project, I realized that doxygen's call graph was inaccurate. I found one doxygen setting that I could tweak, to increase the depth of call tree analysis--but even after bumping up that limit, some of the function relationships that I needed to understand were just missing. I chalk this up to subtleties like call-through-function-pointer, macros that obscured some function calls, and so forth.</dd><dt>Recursion and mutual dependencies</dt><dd>My tidy algorithm assumed that the overall call tree for the application was a directed acyclic graph. In fact, later analysis showed that I had 59 functions that were directly recursive, and probably a lot of other ones where recursion was indirect. I was able to detect this recursion, and artificially break it, in many cases. However, I found that about 20 iterations into my algorithm, I ran out of "leaf" functions with about 1000 functions still remaining to analyze. These functions all called some other function in the remaining graph, due to dense, unfortunate coupling. I brute-forced my way through these, perhaps sacrificing some const fixups that might have been possible if I'd been willing to analyze changes to a clump of functions at a time, instead to a single function only.</dd></dl>
<h3>The detour</h3>
Partway through the project, a colleague suggested that I abandon the idea of parsing C/C++ with regular expressions, and switch to use a true grammar. I told him I had considered it. I knew of ply, which is a python implementation of lex/yacc. I'd noticed, last time I checked, that it shipped with a C grammar. We also discussed the possibility of using a compiler plugin for <a title="gcc plugin" href="http://gcc.gnu.org/onlinedocs/gccint/Plugins.html" target="_blank">GCC</a> or <a title="clang plugin" href="http://clang.llvm.org/docs/ClangPlugins.html" target="_blank">CLang</a>. Both of these let you hook into the compiler after an abstract syntax tree has been generated, to inspect and react to what the compiler understands from the code.

I ended up discarding this approach. Working from an AST makes "reading" the code easy, but it doesn't help write modifications. And the seemingly simple "function declarations" in the mocking layer actually resolve to very complex classes by the time google test/gmock's macros are expanded; making heads or tails of them is not for the faint of heart. However, my colleague successfully built a GCC plugin for a slightly different code analysis task, and it seems promising for certain use cases. Not having to parse code yourself is definitely an attractive option, if it applies.
<h3>The results</h3>
So fast-forward a couple calendar weeks. It didn't take me that much coding time to get this system working, but I was multitasking, trying to be a manager and a point of contact for the press, and interfacing with execs and product management... My coding time was pretty fragmented.

I finally got the code working pretty well, and I let it run...

... and run ...

... and run ...

Since I was validating my changes by doing a full compile and test cycle between each one (and an extra cycle at the end of each rollback, to guarantee that the code was copacetic), it took quite a while to crunch through this codebase. I let it run for probably a total of about 200 hours, during which time I analyzed all 4300 functions in the codebase, one by one.

I am proud of the outcome. Altogether, I think this script found about 2000 functions where one or more parameters should have been const but were not. About 4500 parameters were changed in those 2000 functions, generating about 7000 lines of changes. The day after I pushed my massive change set, the behavior of the codebase on our regression suite was unchanged.

It felt pretty awesome to check back periodically, and see the results of hours (and hours and hours) of analysis that no human being had to wade through. As Hannibal would say, "I love it when a plan comes together."

The script wasn't perfect, though. I estimate that maybe 50 functions were missed due to parsing subtleties. A few prototypes didn't match my regular expressions, and some false matches occurred as well. I also ended up ignoring the constness of member functions; there are only a handful in the whole codebase, and analyzing those would have required entirely different codepaths that I didn't have time to write. I suspect there are other fixes lurking, if I could untie the gordian knot of dependencies that makes some functions impossible to analyze independently.

The code for this "const_fix" python script is <a title="const_fix script on github" href="https://github.com/dhh1128/const_fix" target="_blank">available on github</a>, in case it's useful to anybody. It's not very well genericized; I make assumptions about the organization of the files and folders within the codebase, and it's hard-coded to email me if the script crashes. But you might be able to adapt it in an hour or two, if you have similar codebases that are scons/make/autotools-centric. I have since used the script on a second codebase, and the adaptation took me about an hour.
<h3>The moral(s) to the story</h3>
Stepping back from the details of this experience, I draw a few general conclusions:

<strong>Never get involved in a land war in Asia</strong>, as Vizzini would say. (Or in other words, don't invade unknown territory in your code, unless you're assuming some blood, sweat, and tears. :-)

<strong>On the other hand, <a title="Courage Counts" href="courage-counts.md">courage counts</a></strong>. A festering problem finally got fixed, because I was crazy enough to try.

<strong>It is a crying shame (and a glaring irony) that it's so hard to code my way to a productive manipulation of ... code</strong>. Programmers spend their whole careers validating the proposition that it's worthwhile to enable computers to do grunt work, so humans can focus on more interesting tasks. Yet the artifact that programmers produce is so plagued by inconsistencies, so susceptible to bugs, and so complex to process that it takes a major investment to automate working with it. I am going to fix this in the <a title="On bread recipes, maps, and intentions" href="on-bread-recipes-maps-and-intentions.md">programming ecosystem that I create</a>.

<strong>An imperfect solution still made a huge difference</strong>. Sometimes perfect is the enemy of good enough.

<strong>Coding something right is cheaper and a whole lot less hassle than <a title="Paying Off Technical Debt" href="paying-off-technical-debt.md">fixing an antipattern once it's firmly entrenched</a></strong>. We'll never get away from refactoring (nor would we want to)--but it pays to establish good habits of code hygeine, early, instead of after you write 500,000 lines of gunk.

<strong>Compilers ought to offer a "this should be const" warning, so this work would have been unnecessary</strong>. I googled; there isn't any such option that I could find. Yet my need is not that unusual. Why isn't this problem already solved?

---

Why you should use an IDE instead of vim or emacs | Codecraft (2014-05-13 10:16:41)

[…] while; I think they’d find it easier to generate momentum on unit tests, to eliminate fear of ambitious refactors, and to see their way past nagging tech debt. However, bigger concerns have kept me from pushing […]

---

λ (2014-04-27 04:15:17)

After some research I found this thread: http://gcc.gnu.org/ml/gcc-patches/2010-04/msg01465.html
And it turns out that Wsuggest-attribute is already implemented in gcc (http://gcc.gnu.org/onlinedocs/gcc/Warning-Options.html).
Sadly, it's only about functions but not their arguments.

Speaking of clang, there is a proposal http://lists.cs.uiuc.edu/pipermail/cfe-dev/2013-February/027816.html but I can't find any results of it.

---

Daniel Hardman (2014-03-27 21:46:16)

Hopefully they're not the kind of memories that wake you up at night, screaming... :-) We're making progress. Thanks for all the work you did to point us in a good direction.

---

Daniel Hardman (2014-03-27 21:45:10)

Yes, I smiled when I read your comment, because we both know other codebases where this would have been quite helpful. :-)

---

Jason Ivey (2014-03-27 20:11:13)

That is awesome.  I believe I had the exact same idea at a previous company where we were both employed.  It sounds like you were much more relentless than myself though.  After discovering only a few of these parsing problems I decided it was a problem that I didn't want to solve with a regular expression.  At the time I also looked at clang and gcc but came to a similar conclusion that once you were into the AST it was very difficult to do a replace on the original text.

I'm excited to see what you had to do to solve the problem for so many functions.

Jason

---

Daniel Hardman (2014-04-27 20:10:21)

Hey, thanks for the tip about Wsuggest-attribute! That is awesome, and I didn't know about it at all. I'm glad compilers are getting better.

---

dougbert (2014-03-25 13:10:26)

Oh the memories....the memories of code bases past.......

dougbert

---

λ (2014-04-26 13:48:13)

You're very right about compilers in the last statement. I think that's very good idea and I'd like to hear some compiler guys opinions.

---

Introducing Marks | Codecraft (2014-07-24 08:49:29)

[…] doesn’t help at all, because I need this before run-time. As I mentioned in my post about making a codebase const-correct, the lack of this feature is really a serious design flaw. Why should code, of all things […]