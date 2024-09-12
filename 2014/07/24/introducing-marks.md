---
title: Introducing Marks
date: 2014/07/24
slug: introducing-marks
---

In my previous two posts (<a title="Lacunas Everywhere" href="../../../2014/07/16/lacunas-everywhere/" target="_blank">here</a> and <a title="Thoughts On Bridging the “Lacuna Humana”" href="../../../2014/07/21/bridging-the-lacuna-humana/" target="_blank">here</a>), I described how and why programming languages can't talk about many issues that affect programmers--important issues like product requirements, design constraints, intellectual property, and more. I also inventoried the mechanisms that extend the semantics of languages today, and explored why those mechanisms have limited value. If you haven't read those posts, please do; what I say next won't make a lot of sense without that foundation.

In the <code>intent</code> programming language that I'm creating, the solution to this problem is called "marks" (a name which alludes to <a href="http://en.wikipedia.org/wiki/Markedness" target="_blank">linguistic markedness</a>). Marks play a role somewhat analogous to adjectives and adverbs in human language; they are crucial enrichers. They resemble decorators or annotations in other languages, though their power is much, much greater.

Without further ado, let me provide a blueprint for this bridge across the semantic gap that I've been lamenting--the design guidelines for "marks." Then I'm going to show you an example of how easy it could be to use marks, and how much power they give you.

[caption id="" align="aligncenter" width="640"]<img class="" src="https://farm3.staticflickr.com/2095/2402300942_2636483bdc_z.jpg" alt="" width="640" height="433" /> image credit: <a href="https://www.flickr.com/photos/curiousexpeditions/2402300942/sizes/z/" target="_blank">Curious Expeditions</a> (Flickr)[/caption]
<h3>Blueprint</h3>
<ol>
	<li>Code and its compiler(s) must have a <strong>compile-time API</strong> specified by the language.
<div style="margin:.7em;">It's not okay if Clang generates one type of AST, GCC a second, and MSVC a third; all compilers that support the language must expose a spec-compatible, programmable API for all language constructs. For example, I need to be able to find out what parameters and local variables are declared in a function, and what their data types and other characteristics are. This is similar to what reflection offers, but reflection doesn't help at all, because I need this before run-time. (Kudos to D, which provides compile-time reflection very similar to what I'm describing...) As I mentioned in my post about <a title="How to make a const-correct codebase in 4300 easy steps" href="../../../2014/03/25/how-to-make-a-const-correct-codebase-in-4300-easy-steps/">making a codebase const-correct</a>, the lack of this feature is really a serious design flaw. Why should code, of <em>all</em> things programmers deal with, be impossible to code against?</div></li>
</ol>
<!--more-->
<ol start="2">
	<li>Any object in code must support <strong>decoration</strong> (semantic marks).
<div style="margin:.7em;">Existing decorator/annotation/attribute mechanisms are fairly broad already. However, I haven't seen any solutions that let me decorate arbitrary blocks of code, individual assignments, conditionals... Plus:</div></li>
	<li>The <strong>scope of code</strong> must be expanded to include constructs above the level of a compilation unit.
<div style="margin:.7em;">Today, programmers usually write code for classes, packages, and modules, but all structures "above" that level (applications, libraries, assemblies, product suites) are described in some alternative mechanism (e.g. pom.xml, SConstruct, CMakeLists.txt, Visual Studio solution, Eclipse workspace). Typically these constructs are viewed as optional veneer offered by an IDE--often, they're not even formally defined in the language's spec. This means you can't decorate them (see #2), and they don't have a programmatic API that's unifiable with that of code at compile-time (see #1).</div></li>
	<li>Code must have a <strong>DOM</strong>.
<div style="margin:.7em;">This is really a corollary to items 1 through 3; any element of code must be reachable through the code's interface, which implies something DOM-like. It may be unnecessary to hold the entirety of a DOM in memory, though; perhaps a SAX-style interface would suffice. Interestingly, this requirement also makes code into true hypertext, which has other ramifications that I'm planning to blog about later.</div></li>
	<li><strong>Call graphs</strong> and other producer/consumer relationships must be part of the code interface.
<div style="margin:.7em;">The utility of this will become clear in examples.</div></li>
	<li>Decorator attachment must be <strong>richer than binary on/off</strong>.
<div style="margin:.7em;">This is a flaw in existing decorator mechanisms. If I put <code>@foo</code> on top of a class in Java, the annotation is present. If I don't put it there, it's not. Binary.</div>
<div style="margin:.7em;">Human brains and human languages don't work that way; they're more fuzzy. If I tell you that "Fred was an executive at Enron," you immediately generate theories about Fred. The fact that I imparted that information at all means that I consider it significant in some way--so you imagine reasons why, and associate them weakly/tentatively to Fred in your mind: he may have been fired, he may have been guilty of shady behavior, he may be a whistleblower, etc.</div>
<div style="margin:.7em;">At least the following modes of attachment need to be supported: explicitly affirmed (binary "on"), explicitly denied (binary "off"), implicitly affirmed (true unless I get explicit evidence to the contrary), implicitly denied.</div></li>
	<li>Semantic marks must support <strong>sophisticated combination and propagation</strong>.
<div style="margin:.7em;">For one, marks need to be able to subsume or imply other marks. In the real world, I can tell you that my car is a Lamborghini (in my dreams :-), and in doing so, I've already told that my car is a sports car, that it's expensive, that it's hard to find parts, that it's a favorite target for speed traps... Likewise, if I am writing a class, and I put a "prototype" mark on it, I may want you to also know that the class is "insufficiently tested", or "not shippable". Such logic must be under programmer control.</div>
<div style="margin:.7em;">Another aspect of propagation is that marks must cascade across various scopes. If I have a function that is marked as "not thread-safe", then any caller of that function must acquire the same mark. If I have an application that is marked as "free", then all modules used by that application must also be "free" by implication. If I mark a package as "internal use only", then no functions in that package should be used in projects that exports symbols from the package.</div></li>
	<li>Marks must be <strong>evaluated</strong> at compile-time.
<div style="margin:.7em;">Evaluation means running code that marks "carry". Think of this like static asserts on steroids.</div></li>
</ol>
<h3>Examples</h3>
Let's take one of the use cases that I've mentioned in previous posts: a programming team has a mandate not to use any GPL'ed code. Here's how simply that rule could be enforced in code, given the "marks" mechanism:
<ul>
	<li>Each component, package, module, or individual function is marked with its license. (Remember, since marks propagate, this is not an onerous task. It requires no more effort than today's informal convention of checking in a file named LICENSE or COPYING at the top of a folder. License marks would propagate through folder hierarchies unless/until overridden in a sub-folder.)</li>
	<li>All team projects receive a "no GPL in the call tree" mark. For now, imagine that this works more or less as follows:
<pre>@no_gpl
class my_project: project
    // body of project definition
</pre>
</li>
	<li>During compilation, the compiler evaluates the validity of marks. If the project includes any GPL'ed code, a "semantic error" (not a "syntax error") is generated, because the project-level mark and the lower-level mark(s) are incompatible.</li>
</ul>
Does this sound too good to be true? With a reasonable API to access the AST, writing marks that implement this logic is a piece of cake. Here's python-ish pseudocode for the implementation. (I'm using pseudocode instead of <code>intent</code> code, because I don't want to bog down this discussion in tons of extraneous details.)

https://gist.github.com/dhh1128/2ca442f3e7f28705ef28

As code is compiled, the compiler executes the <code>can_bind()</code> method of each mark that's been placed. This causes calculations about semantic compatibility, <em>without the compiler having to understand the semantics itself</em>.

I'm glossing over lots of details here. (At what point in the compilation process is the AST for a function known, making the API used by the marks useful? Which mark placement is tested first? How are errors reported? How does the compiler know that mark code is callable at compile time instead of just at runtime?) I have preliminary answers, but this post is not the place. For now, just take it on faith that the compile model is workable.

One more example, just for fun. Suppose you want to guarantee that across a large object model, all object instances have IDs which are strings. These strings must consist of a single line of between 20 and 40 printable characters; they cannot be null. Anywhere that member variables are named "id", or parameters are used to set a member variable named "id", you want these semantics enforced by precondition:

https://gist.github.com/dhh1128/1fc2a20ffb370ba39327

In my <a href="../../../2014/07/28/mountains-molehills-and-markedness/">next post</a>, I'll explore a bunch of additional examples, and I'll cover more details about how these marks work their magic.

---

David H (2014-07-25 06:42:02)

I woke up this morning and thought "wow, writing an external tool that creates an accurate call graph for Javascript would be really hard. How do you figure out where a closure gets used?" Valuable as it is, it would be difficult to retrofit your marks system to other programming languages...

---

Daniel Hardman (2014-07-25 06:57:29)

I had not seriously considered making marks work across a multilingual tool chain, but it's an intriguing enhancement. This is why I blogged--I needed smart people to point out ways this needed polish. Thank you!

I love the idea of statistics gathering, BTW. It fits very well with another natural use of marks, which is simple tagging. You can imagine stats for individual tags, but also for intersections and unions of tags that are interesting...

---

Mountains, Molehills, and Markedness | Codecraft (2014-07-28 08:44:42)

[…] out some symptoms of that deficit, and then made recommendations about bridging the gap. Finally I introduced “marks”–a feature of the intent programming language I’m creating–and gave you a taste […]

---

Daniel Hardman (2014-07-25 06:55:11)

Actually, tracking down the usage of closures is going to be hard no matter where/how it's done. Even tougher is accounting for the use of function pointers. That's been worrying me for a while.

Because of this, I think some kinds of propagation calculations will need to have caveats attached, if the compiler also detects the existence of phenomena that make calculation imperfect. :-(

---

Thoughts On Bridging the &#8220;Lacuna Humana&#8221; | Codecraft (2015-06-15 10:07:40)

[…] my next post, I’ll describe my bridge more concretely. Even before I do, though, the discussion above […]

---

Know Your Limits | Codecraft (2015-02-05 08:47:48)

[…] I’m a sadder but wiser programmer now. :-) I need to add marks such as +reasonable upper bound and +reasonable lower bound to the intent programming language […]

---

How to point in code | Codecraft (2014-09-25 08:39:02)

[…] how the semantic marks that I’ve discussed in previous posts provide a powerful way to qualify and query this sort […]

---

In Which Warnings Evolve Wings | Codecraft (2014-08-06 08:46:14)

[…] marks that I’ve recently described provide a nice, uniform solution to this hodgepodge of […]

---

trevharmon (2014-09-08 23:33:04)

In addition to the other comments already made, I feel like this is also addressing some of the bad behavior we do when we try to embed many of these ideas into the names of our functions or methods. Often, these because unnecessary habits that we carry from language to language. Why are all of my object initialization methods named _init()? At one point, because particular languages wouldn't enforce encapsulation, we were doing things like starting function names with underscores. We all "understood" this to mean, "don't call this function from outside this file". Even if encapsulation was enforced, we still tended to do it just so we could quickly look at the function name and gain some understanding of how it was to be used, not just what it did. I can think of probably another half-dozen such behaviors off the top of my head. However, personalized markup certainly had its problems. For example:

- Did I understand it? Yes... well... probably for the first few years.
- Did my group understand it? Probably.
- Did anyone new understand it? Maybe... but not guaranteed.
- Did the compiler understand it? Nope.

Yeah, that last one's the problem. :-)

I'm looking forward to seeing how this idea further develops.

---

David H (2014-07-24 11:24:47)

Daniel, this is looking very interesting.

Very few projects nowadays are all written in one programming language. In my professional work a single project involves a server written in C++, another one written in Java/Groovy, and a bunch of related code written in Python, all communicating with each other. Yet the example you give of "no GPL code" could apply across such a multi-language project.

Although I can see the value in a language designed around the marks concept, it would sure be useful to have an external toolchain implementing your marks system across multiple programming languages. The tools would know how to parse the langauges, generate graphs, and parse your style of marks.  An appropriate marking syntax would be devised for each programming language. Maybe decorators in Python, maybe specially formatted comments in other languages if necessary. The tool would run as part of building and/or testing. Such a toolchain could report code coverage statics. For example, "85% of the this code (written in C++, Python, and Javascript) is covered by an explicit license." And of course such a tool would work very well on code written in your intent programming language, which I am looking forward to reading more about.