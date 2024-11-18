---
title: Headers, babies, and bathwater
date: 2013-08-12
slug: headers-babies-and-bathwater
---

I claim that by eliminating the C/C++-style dichotomy between headers and implementation, most modern programming languages have thrown out the baby with the bathwater.

[caption id="attachment_1264" align="aligncenter" width="500"]<a href="../../../wp-content/uploads/2013/08/screen-shot-2013-08-11-at-7-35-35-pm.png"><img class="size-large wp-image-1264" alt="Don't throw out the baby with the bathwater! Photo credit: StubbyFingers (Flickr)" src="http://codecraft.co/wp-content/uploads/2013/08/screen-shot-2013-08-11-at-7-35-35-pm.png?w=500" width="500" height="438" /></a> Don't throw out the baby with the bathwater! Photo credit: <a href="http://www.flickr.com/photos/stubbyfingers/5940964193" target="_blank">StubbyFingers (Flickr)</a>[/caption]

If that sounds crazy, just hang with me for a minute.

I know my claim runs counter to popular wisdom; have a look at <a title="stackoverflow thread on headers" href="http://stackoverflow.com/questions/752793/should-c-eliminate-header-files">this thread on stackoverflow.com</a>. Designers of languages like python and go and D and ruby and java consider it a feature that developers don't have two redundant pictures of the same functionality. This comment from the C# 5.0 specification is typical:
<p style="padding-left:30px;"><em>"Because an assembly is a self-describing unit of functionality containing both code and metadata, there is no need for #include directives and header files in C#. The public types and members contained in a particular assembly are made available in a C# program simply by referencing that assembly when compiling the program"</em> (p 3)<em>.</em></p>
I agree.

Sort of...

<strong>Bad headers are a royal pain</strong>

It can be onerous to maintain the parallelism between a .h and a .cpp. And most C/C++ headers are managed so poorly that the benefits you might claim for them are theoretical rather than real. Three common antipatterns that I particularly detest:<!--more-->

1. Putting everything in one monster header.
<p style="padding-left:30px;">This couples all details of the system together in a single giant hairball. It may be fine for a project with 2 or 3 classes, but for dozens or hundreds of classes, it's a major problem, and it violates the <a title="Small Files Are Your Friends" href="small-files-are-your-friends.md">small file rule</a>.</p>
2. Writing function prototypes without any parameter names, because it's less typing:
<pre style="padding-left:30px;">int do_something(Foo *, bar *, char const *);</pre>
<p style="padding-left:30px;"></p>
<p style="padding-left:30px;">This is wrong-headed. It means that the only way you can understand how to call the implementation is to study the implementation itself, instead of just reading the header.</p>
3. Mismanaging #includes.
<p style="padding-left:30px;">When you #include  stuff that a consumer of a header doesn't really need, just for "convenience", what you're really doing is artificially coupling the system (see problem #1), making your build more fragile, subverting incremental builds, and making compile time longer.</p>
<p style="padding-left:30px;">When you leave out #includes because the .cpp files already #include what they need, you are making it harder to trace dependencies. If you ever hear that header X must be #included before header Y, you're suffering the consequences of this antipattern.</p>
<strong>What headers could be good for</strong>

One of the insights often attributed to Guido van Rossum (inventor of python) is that code is meant to be read--by humans. This insight is enshrined in the zen of python (by Tim Peters) with the pithy statement that "Readability counts." It reflects the same sentiment articulated by Martin Fowler, who said, "Any fool can write code that computers can understand. Good programmers write code that humans can understand." And it echoes the observation of the venerable C.A.R. Hoare: "The readability of programs is immeasurably more important than their writeability" (<em>Hints on Programming Language Design</em>, 1973).

These are not dumb guys.

So let me ask: <span style="color:#993300;"><em>Which is easier for a human to read and understand--a 50-line header, or a 800-line implementation?</em></span>

This is the the first baby that's being thrown out with the bathwater. Think <a title="Progressive Disclosure Everywhere" href="progressive-disclosure-everywhere.md">progressive disclosure</a>: headers could dramatically simplify what a consumer of code has to wade through. <em>If</em> they worked right. <em>If</em>.

You might say that modern IDEs make this a non-issue. When you open an 800-line .java file, you get a treeview with all the methods in the class, and you can sort and filter them in any way you like.

I don't buy it. The default views don't hide details that are irrelevant for the <em>consumer</em> of the code, because they're assuming you want to work on the <em>implementation</em>. That's the file you opened, after all. You see all the private methods and members, all the nested inner classes, all the gobbledygook.

But let me ask another question: <span style="color:#993300;"><em>In java or D or C#, if you make an innocuous change (say, renaming a private member or fixing a typo in a comment), who has to know?</em></span>

The answer is: <em>everybody!</em>

Consumers of your code are bound to the code's implementation, not its fixture. Because those are not separate constructs, distributed builds are impractical, and SDKs for these languages must test the consumer's compliance against compiled binaries.

You might say that since these languages compile so much faster than C++, recompiling has become painless. Fair enough. You might say that with JIT-compilation or interpreted languages, you can defer this problem until it goes away. But neither solution helps you if you have IP you must protect. For a C++ codebase, it's possible to provide headers to a third party without giving away patents and trade secrets. In languages without headers, you're up a creek. The best you can do is obfuscate, which may not satisfy the paranoid or the government regulator worried about export controls.

<strong>How headers ought to work</strong>

I can think of a way to have the best of both worlds: let implementers stop worrying about headers, and let consumers stop worrying about implementation:
<p style="padding-left:30px;">Generate the headers.</p>
Every time a compiler processes code, have it generate from the implementation a pure, simple interface that consumers can read. This is the basic idea behind <a title="lazy c++" href="my-first-tangle-with-the-tower-of-babel.md">writing my own programming language</a>, I'd take it much further:
<ul>
	<li>Have the compiler produce an "etag" or version stamp that unambiguously hashes the relevant header content, so consumers can identify a version to which they are bound. This etag should depend only on important details, not on comments or parameter names or other stylistic variations.</li>
	<li>Before replacing the old version of the header, have the compiler compare function/class signatures in old and new to see if compatibility has been broken. Distinguish between incremental additions (new functions don't break compatibility with old clients) and changes (renaming a function or removing a parameter). Besides writing out an etag for the header, have the compiler write out an incremented version number, plus the oldest version number of the header that existing consumers would still be compatible with.</li>
	<li>Compile the headers (not just the impl) into the final binaries to facilitate <a title="Decoupling Interfaces As Versions Evolve, Part 1" href="decoupling-interfaces-as-versions-evolve-part-1.md">semantic versioning</a>.</li>
	<li>Make sure the language can identify preconditions, postconditions, and invariants unambiguously, so these can be documented (automatically) in the header.</li>
	<li>Distinguish between public and private comments (using something a little slicker than javadoc), so that comments from the implementation can be carried across to the header as well.</li>
</ul>
I'm not sure headers like this would be worth creating for python, which often has code that's so simple it doesn't need a summary. But for large, complex codebases, I think this would be a real boon. If you've ever had to wrestle your way through half a million lines of C or java or C# without good headers, I'm guessing you know what I mean.
<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://stackoverflow.com/questions/18058937/how-do-compilers-know-when-not-to-recompile" target="_blank">How do compilers know when not to recompile?</a> (stackoverflow.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://stackoverflow.com/questions/3935183/forward-declaration-include-on-top-of-declaration-include-classfwd-h-class-h" target="_blank">Forward declarations and #include</a> (stackoverflow.com)</li>
</ul>

---

Julie Jones (2013-09-10 23:15:45)

I have been thinking about this from a different perspective, although it would be easy to extend to generating separate header files. I really like the self contained modules in languages like Java and C#. I think implementation in header files in C++ is a huge wart. What I want is everything in one file in one place. However, I want to be able to control the view of the module or class. When I look at is as client I just want to see the public interface (aka header). But when I need to see how something works I just want to drill down (think light table) and see more detail



---

Ryan Marcus (2013-08-12 15:18:48)

I generally agree with you -- but I had one question.

What's the difference between the "automatically generated headers" you suggest and, say, JavaDocs? It seems like, in Java code (and in other languages via Doxygen), the part of a 3rd-party package you are supposed to look at for understanding is the documentation. This doesn't seem unreasonable to me.

It seems like a header file provides an easy way to see function signatures. JavaDoc (and any good documentation engine) seems to do this for free, with the addition of providing multiple output formats and a standardized format for describing what those signatures mean.

Is it this "code should be readable" idea? It seems like automatically generated header files wouldn't really be "code" (written by the user) anymore than JavaDoc output is "code."

Please correct my misunderstanding. :)

Thanks for the post -- very thought provoking.

---

weberc2 (2013-08-12 16:28:16)

When you describe how headers "ought to work", you're describing Ada's Specification/Body files. Specs contain the API details (the interface), and the Body contains the implementation. And you get that as a guarantee, enforced by the compiler.

---

Daniel Hardman (2013-08-12 17:58:44)

You may be different, Dougbert--but I wish all the C++ programmers I've worked with over the years were different in exactly the same way! It would be a lot more fun to code if they understood how to keep interfaces clean... :-)

---

Daniel Hardman (2013-08-12 18:14:25)

Ryan: thanks for the thoughtful response!

You're right that javadoc overlaps quite a bit with the idea I'm suggesting. When I first discovered doxygen and javadoc long ago, I was infatuated with the tools, and I didn't see much gap between what they offered and the ideal I describe.

However, some differences remain:

- You can't compile against javadoc. Headers enable another programmer to not just understand the interface to your code, but to test his/her code against it, with full compiler enforcement. Headers or something similar is what you need to outsource a project without supplying implementation code.

- I have become disillusioned with forms of communication external to the code itself. On several codebases that I've worked with, I've gone to significant effort to write good doc comments, and to set up doc generation--only to see this doc get ignored by developers. They simply won't pull up a browser to read docs if the code is in front of them. (This is less true of java, where most IDEs have hover text based on javadocs--but in C++, it's the unfortunate truth.)

I do think there is a difference between generated headers and generated javadoc. Whether you call either or both of them "code", in one case you read the output with your code editor; in the other, you read with a browser. Also, in practice, the source for javadoc is checked into vcs, but not the output. So you can't browse the "code" output of javadoc in git logs. If you generated headers, you'd be checking them in to the vcs.

Nonetheless, I think your point about generated docs is a good one and somewhat weakens the value of what I'm proposing.

---

Daniel Hardman (2013-08-12 18:15:34)

Thanks for the note. I'm unfamiliar with Ada, but you are the third person who's told me that. Which tells me that it was a memorable feature of the language. I wonder why it got discarded?

---

Brady Kimball (@bradykimball) (2013-08-13 08:19:25)

Good points.  A few thoughts that I have on the matter include maintainability and syntactic cruft.  Why have separated interfaces for every class unless you need to?  Obviously, you should use interfaces for things like layer abstraction or collaborative projects with teams that you don't want to be dependent on.  I know this is a dangerous assumption that every developer is savvy enough to understand when to use them, but I would argue that part of the point that some of these more terse languages is to work around manual busy work overhead.

Your proposals at the end of the post are good food for thought as how to combat the maintenance and cruft issues.  Maybe it is personal preference, but I prefer good developer documentation.  This doesn't mean the developer needs to write a thesis on the class.  Often, the method signatures are enough with a simple description of any prerequisites or post conditions are sufficient.

---

Daniel Hardman (2013-09-12 19:55:59)

Self-contained modules are nice, most of the time. However, I periodically write java classes that are 1k to 2k lines, and that starts to feel a bit cumbersome. Certainly I could decompose further, but sometimes I wish I could split the impl into several files in the way that C# partial classes supports. I like those partial classes; they're a nice way to keep the eventing for a UI class separate from the procedural code. Also, I don't think that a pure view is adequate if you want to share an interface with someone without sharing the implementation (e.g., to protect IP).

---

Daniel Hardman (2013-08-13 16:54:03)

Good point about pragmatism, Brady. Although it might be nice to be able to separate interface and impl on key classes, perhaps doing it for everything is overkill.

I guess the developer docs vs. code question boils down to personal preference. I have never seen developers read docs consistently. They'll look up a prototype in a reference, but they like to be in the code rather than in some other tool. However, as I mentioned in the response to Ryan, modern IDEs often provide hover autoexpansion which makes this tool discrepancy vanish.

---

dougbert (2013-08-12 12:10:21)

I know what you mean. I really, really know what you mean.

To me, the headers represent the INTERFACE, not the implementation of an object. Sometimes I put an adapter pattern between the INTERFACE and internal implementation - I don't what my consumer to make assumptions that he/she can use to touch inside my box.

then again - I am a bit different