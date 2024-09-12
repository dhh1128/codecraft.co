---
title: Good fences make good neighbors
date: 2013/05/15
slug: good-fences-make-good-neighbors
---

In Robert Frost's poem, "Mending Wall", two farmers meet each spring to rebuild the rock wall between their properties. One farmer is the narrator. He notes that the unseen forces of winter and weather always cause some decay ("something there is that doesn't love a wall"), and he wonders why the wall is necessary. There's apple orchard on one side, and pine forest on the other--it's not as if something will be kept in or out. The other farmer answers with the repeated aphorism "good fences make good neighbors."

[caption id="" align="aligncenter" width="500"]<a href="http://www.flickr.com/photos/dragonwoman/226824603/"><img alt="" src="http://farm1.staticflickr.com/74/226824603_1285fc9181.jpg" width="500" height="333" /></a> photo credit: DragonWoman (Flickr)[/caption]

This poem could be a treatise for the principle of encapsulation in software. In software as in life:
<ul>
	<li>Something there is that doesn't love a wall.</li>
	<li>Good fences make good neighbors.</li>
</ul>
<strong>What doesn't love a wall?</strong>

Subroutines, formal interfaces, data hiding, class hierarchies, the <a class="zem_slink" title="Opaque pointer" href="http://en.wikipedia.org/wiki/Opaque_pointer" target="_blank" rel="wikipedia">pimpl idiom</a>, and similar mechanisms all create barriers in software between consumers and providers of functionality. These techniques are well known, but we still have codebases littered with protected data members, unnecessary class declarations in headers, goto, and other suboptimal choices.

Why?<!--more-->

I believe there are many causes, but the most insidious is that we just don't care enough to make encapsulation our default habit. We take the easy way out.

How often have you seen code like the following in C++:
<pre style="margin-left:2em;padding:1em;background-color:#eee;border:solid 1px black;">class FooInternals { ... }

class Foo {
  public:
    Foo() { ... }
    std::string getName();
    void changeInternals(FooInternals const &);
    ...
};</pre>
 

or in java:
<pre style="margin-left:2em;padding:1em;background-color:#eee;border:solid 1px black;">class Foo {
    String name;
    String getName() { return name; }
    ....
}</pre>
 

What is wrong with these snippets of code?

In the first one, the programmer has a habit of immediately counteracting the private-by-default visibility rule for classes in C++; the first line makes what follows public. We can tell this is laziness rather than serious design, because the FooInternals class is fully declared in the header even though it's unnecessary, and the implementation of getName() is also wrong. It returns a string by value instead of const &, and it doesn't declare the method const either. This coder hasn't bought into the encapsulation that C++ offers.

In the second, the programmer uses default java visibility everywhere, without bothering to be more specific. Result: the getter has the same visibility as the instance variable that ought to be private; it is totally useless.

<strong>How to make good fences and good neighbors</strong>

Make a habit of being very deliberate about what information you expose. The default position ought to be to expose to consumers of your code as little as you can get away with. In other words, put a wall around your private domain and then maintain it.

What coding habits are evidence of this mindset?

In C++:
<ul>
	<li>Use forward decls anywhere you can. (Using a class by ptr, by ref, or as a return value does not mean you need its definition.)</li>
	<li>Use #include correctly. This means: #include everything you must have, but nothing you don't absolutely need. (This topic is probably worth a post of its own; in my entire career, I've only seen a handful of programmers who do this right.)</li>
	<li>Avoid headers that declare too much. 15 classes in my-master-header.h = bad.</li>
	<li>Keep implementation out of headers. (Templates are a special case that's worthy of separate discussion.)</li>
	<li>Consider using the pimpl idiom where it makes sense.</li>
	<li><a title="How Enums Spread Disease — And How To Cure It" href="../../../2012/10/29/how-enums-spread-disease-and-how-to-cure-it/">Use enums carefully</a>.</li>
	<li>Use anonymous namespaces and/or static scopes to hide private classes from the linker.</li>
	<li>Never have protected members. (Public members are okay for POD structs, but are otherwise just as toxic.)</li>
	<li><a title="Put Your Const Foot Forward" href="../../../2012/11/14/put-your-const-foot-forward/">Use const correctly</a>. This forces callers to respect mutability constraints in your corner of the codebase.</li>
	<li>Eliminate goto.</li>
</ul>
In Java:
<ul>
	<li>Consider using abstract classes instead of interfaces. (Another topic that's worthy of a post by itself. Java interfaces are overused and, because they are wholly public, sometimes force details out into the open.)</li>
	<li>Get in the habit of making members and methods private.</li>
	<li>Pray that the keepers of the language implement partial classes, like they did in C#. :-)</li>
</ul>
In Python:
<ul>
	<li>Use the _ prefix convention to signal private implementation details.</li>
	<li>Look for better alternatives to accessing _ prefixed internals. (Since at least python 2.2, the language has consistently added better alternatives to dirty hooks.)</li>
</ul>
In all languages:
<ul>
	<li><a title="Small Files Are Your Friends" href="../../../2013/03/21/small-files-are-your-friends/">Divide code into modules and files</a> that gives you a rational, mentally tractable separation of concerns.</li>
	<li>Be on the lookout for tight coupling and unnecessary leakage of implementation details.</li>
</ul>
(BTW, my <a title="My First Tangle With the Tower of Babel" href="../../../2013/04/26/my-first-tangle-with-the-tower-of-babel/">pondering on programming languages</a> leads me to believe that encouraging correct thinking about encapsulation is a desirable attribute. Not all languages do it equally well. Contrast the C++ guidelines above with what needs to be said about Smalltalk or Erlang; I think it's a bit eye-opening...)
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Talk back. What coding habits do you feel are most helpful at promoting encapsulation?</span></em></p>

<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://blog.startifact.com/posts/overwhelmed-by-javascript-dependencies.html" target="_blank">Overwhelmed by JavaScript Dependencies</a> (startifact.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://www.scilogs.com/endless_forms/2013/04/24/do-good-fences-make-good-neighbors-for-mesopredators/" target="_blank">Do Good Fences Make Good Neighbors for Mesopredators?</a> (scilogs.com)</li>
</ul>

---

tianyuzhu (2013-05-15 12:04:21)

Why should you avoid headers that "declare too much"?

In C++, public headers are used to define modules, which contain a set of declarations that work together. Consider the standard  module. It's got tons of declarations.

---

tianyuzhu (2013-05-15 12:05:30)

Sorry to double post. In my previous post, it says "Consider the standard module". I meant, "Consider the standard type_traits module".

---

Daniel Hardman (2013-05-15 13:03:58)

Excellent question.

Part of the issue is that big headers are hard to digest, mentally. See http://codecraft.co/2013/03/21/small-files-are-your-friends/.

This matters much more in high-level application code than it does in the headers for standard libraries, because we usually discover what we need to know about standard library functions and datatypes by reading a man page or similar documentation--not by browsing headers.

The headers in the c++ standard library have an additional dynamic that makes them outliers, which is that they're very template-centric. This means they not only have declarations, but also large blocks of implementation.

My "declare too much" comment basically reflects the following mindset: ideally, a header should declare only what a *consumer* of your code needs to know, not what the *implementation* of your code needs to know. Anything else is "too much," at least in theory, because it will obscure your intent about interfaces and tempt other coders to use the code incorrectly. However, I am pragmatic--sometimes the juice is not worth the squeeze.

---

dougbert (2013-05-16 11:08:51)

I concur with (and have done it myself) with smaller headers: I have an external interface header to my module for others to utilize, and internal header(s) for implementation only use. The two "should" never met, IMHO. Well, better said: A one way street. Implementation needs the external header to implement that interface, but external consumers don't need internal headers/interfaces.

Good thoughts/post as usually

---

Daniel Hardman (2013-05-16 11:32:20)

Doug: On an intuitive level, I have been splitting my headers into the internal and external categories for years, without realizing exactly why. Your comment made me realize that's what was going on, somewhere in the back of my mind. Thanks for twisting the focus knob!

---

What should code look like when we squint at it? | Codecraft (2013-09-19 08:23:04)

[…] classes out of a sea of thousands is not particularly easy. Interfaces allow you to encapsulate and suppress details—but they don’t tell you how they fit into a gestalt. Tests as a form […]

---

2 Surprising Truths About The Iron Triangle | Codecraft (2013-07-01 16:39:10)

[…] In a way, I’m suggesting the opposite strategy: if you push on quality in the right way, speed will accrue organically. Not at first, especially if you’re starting with an unhealthy codebase. Not with every checkin; sometimes you have to take one step back to take two steps forward. But over time, if you continue to invest in quality, your patient will get more healthy, and you will see your speed go up, not down. The mental models of your engineers and the entire value chain will align. You’ll create virtuous cycles that perpetuate the right kinds of tradeoffs for performance, scalability, and encapsulation. […]

---

Programmers: learn how to &#8220;cloudify&#8221; | Codecraft (2013-07-23 11:43:12)

[…] here on codecraft, such as what the programming language of the future ought to look like, how to encapsulate for cloud, and so […]

---

Lacunas Everywhere | Codecraft (2014-07-16 13:58:50)

[…] language shouldn’t be indicted for creating useless redundancy that undermines encapsulation and the accuracy of […]