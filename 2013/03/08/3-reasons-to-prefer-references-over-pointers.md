---
title: 3 reasons to prefer references over pointers (C++)
date: 2013/03/08
slug: 3-reasons-to-prefer-references-over-pointers
---

I still remember what it was like, as a C programmer, to be introduced to the newfangled concept of references in C++. I thought: "This is dumb. It's just another way to use pointers. More syntactic sugar for no good reason..."

For a long time, I thought of pointers vs. references as a stylistic choice, and I've run into lots of old C pros who feel the same. (The debate on <a href="http://www.cplusplus.com/forum/beginner/3958/" target="_blank">this comment stream</a> is typical.) If you're one of them, let me see if I can explain why I now think I was wrong, and maybe convince you to use references where it makes sense. I won't try to enumerate every reason--just hit a few highlights.

[caption id="" align="aligncenter" width="500"]<a href="http://xkcd.com/371/"><img class=" " src="http://imgs.xkcd.com/comics/compiler_complaint.png" alt="" width="500" height="135" /></a> image credit: xkcd.com[/caption]

<strong>1. References have clearer semantics</strong>

<code>NULL</code> is a perfectly valid value for a pointer, but you have to do some headstands to create a reference to <code>NULL</code>. Because of these headstands, and because testing a reference for NULL-ness is a bit arcane, you can assume that references are not expected to be <code>NULL</code>. Consider this function prototype, typical of so much "C++" code written by folks with a C mindset:
<pre style="padding-left:30px;">void setClient(IClient * client);</pre>
With only that line, you don't know very much. Will client's state change during the call? Is it valid to pass <code>NULL</code>? In the body of the call, will client ever point to anything other than the value it had at the top of the function?

Veteran C programmers recognize that the semantics are unclear, so they come up with doc conventions to plug the gap, and they check assumptions at the top of the function:
<pre style="padding-left:30px;"><span style="color:#008000;">/**</span>
<span style="color:#008000;"> * @param client IN, cannot be NULL</span>
<span style="color:#008000;"> */</span>
void setClient(IClient * client) {
    if (client != NULL) { <span style="color:#008000;">//...do something</span></pre>
This is fine, except why depend on a comment and a programmer's inclination to read and obey, when you can enforce your intentions at compile time, and write less code, too?<!--more-->
<pre style="padding-left:30px;">void setClient(IClient const & client) { <span style="color:#008000;">//...do something</span></pre>
The <code>const</code> in this declaration tells you that client won't be modified. That's not really a pointer vs. ref thing, but I couldn't help myself. See <a title="Put Your Const Foot Forward" href="http://codecraft.co/2012/11/14/put-your-const-foot-forward/">my notes about <code>const</code></a>. The <code>&</code> tells you that the value of client will not change for the duration of <code>setClient</code>, and it also tells you that callers are not supposed to pass <code>NULL</code>. The comment and the check for <code>NULL</code> become unnecessary. As a caller of this function, if you're working with a pointer and you use the * operator to convert it to a pointer, you now know you have a responsibility to guarantee non-<code>NULL</code>-ness. The function writer has firewalled that issue out of his or her scope of concern, and forced someone who should understand it better to deal with it.

References also tell you that ownership of a particular resource lies elsewhere. Non-const pointers leave ownership ambiguous.

Using references is not always possible, precisely because their semantics are slightly different from those of pointers. If <code>NULL</code> is a valid value, then you have to use pointers. If you intend to assign to the same variable more than once, you have to use a pointer.

But when you <em>can</em> use a reference, you should. It's good defensive programming for the function writer, and it communicates intentions very clearly.

<strong>2. References allow value semantics in templates and operators</strong>

Algorithms and containers in the standard C++ library are written as if operating on values, not pointers. References allow the standard library to work transparently on objects in custom classes that you write, without writing messy adapters, because operators are invoked on values and references identically. For example, <code>std::sort()</code> will work on anything that defines the <code><</code> less-than operator -- but it will never work on pointers to things that define <code><</code>. References are also transparent to <code><<</code> and <code>>></code> stream operators, to boolean comparison operators, and so forth.

If you've done serious template work in C++, you know that this is important. This issue is what forced me to reassess my perspective that it was all a matter of style.

<strong>3. References enable move semantics in C++ 11</strong>

This is a huge deal. If you haven't already fallen in love with the performance optimization that move semantics offer, and you're an old C pro, then you're missing out. One of the common complaints that old C folks have about C++ is that things like std::vector are horribly inefficient to pass by value, and that smart pointers involve a lot of ref counting nonsense that's just useless overhead. The introduction of move semantics turns that on its ear. (<a title="move semantics" href="http://thbecker.net/articles/rvalue_references/section_02.html">Thomas Becker's explanation of move semantics</a> is a great place to start exploring this topic, if you're curious.)

<strong>Don't get me wrong...</strong>

If you think I'm a reference bigot, then I've failed. Pointers and references are just alternate incarnations of indirection, which (as my friend Moray is fond of pointing out) is one of the truly foundational techniques of CS. It's amazing how much more tractable certain problems become when you add a layer of indirection. And pointers were my first experience with the technique, so I can't help but be a fan. Besides the virtues of mutability and nullability, pointers are the easiest way to work with classes of functions having a common signature, and they are used in many advanced idioms. If you looked at my code, you'd see that I still use pointers in C-like ways sometimes. For example, I think functions that take a const char * instead of a std::string const & may make sense in many cases, depending on how layers are organized and how the parameters are used.

But I now try to use references wherever they seem to fit; if I can use either, I always prefer references. I think it makes my code more robust and cleaner--and it sets me up for good performance optimizations in the future.
<h6 class="zemanta-related-title" style="font-size:1em;">Related articles</h6>
<ul class="zemanta-article-ul">
	<li class="zemanta-article-ul-li"><a href="http://katyscode.wordpress.com/2013/02/27/c-explained-object-initialization-and-assignment-lvalues-and-rvalues-copy-and-move-semantics-and-the-copy-and-swap-idiom/" target="_blank">C++ Explained: Object initialization and assignment, lvalues and rvalues, copy and move semantics and the copy-and-swap idiom</a> (katyscode.wordpress.com)</li>
	<li class="zemanta-article-ul-li"><a href="http://stackoverflow.com/questions/15188894/why-doesnt-polymorphism-work-without-pointers-references" target="_blank">Why doesn't polymorphism work without pointers/references?</a> (stackoverflow.com)</li>
</ul>

---

katyscode (2013-03-09 04:12:21)

Thanks for the citation, agree 100% with what you wrote here. The non-nullability of references is both a blessing and a curse; it is frustrating not to be able to declare a reference as a class member and initialize it later, since it of course must be initialized in the constructor's initializer list, so you often end up being forced to use -> in your mehods when it would be syntactically cleaner and safer to use ".". As you said though, references are an important and integral part of C++, not just a syntactic sometimes-alternative to pointers.

---

Daniel Hardman (2013-03-09 09:41:32)

Yes, I've often found myself saying: "I'm happy to live with the limitation that I can only assign to this reference once; I just wish I could do it later than the constructor..." Lazy initialization is one obvious use case.

Great article on lvalues, rvalues, and move semantics, btw.

---

ardanew (2014-03-06 23:42:12)

1) void setClient(const IClient *const client);
2) template sort(...)
3) no use for move semantics when passing a pointer

---

ardanew (2014-03-06 23:43:12)

2) was cutted... sort with comparator

---

Daniel Hardman (2014-03-07 11:20:44)

All three of your points are valid. However, I'm not claiming that references are radically better than pointers--only that they're a better fit for certain problems. And they are:

1) -- answers my questions about changeability of the parameter during the course of the function, but does not clarify any semantics about NULL. The const * const prototype is more verbose and less rich in semantics than using a reference.

2) -- yes, you can use sort with a comparator, but you have to write a pointer-aware comparator that dereferences your pointers, in addition to implementing comparison logic. That violates the single responsibility principle; it's cleaner in many cases to implement comparison logic, and keep pointer-walking outside the comparator. STL is prejudiced this way; swimming against the stream results in code that's bigger and messier, except in trivial examples. (I'm not a purist on this; I've done exactly what you suggested, lots of times. But I do think it's a bit sub-optimal.)

3) -- passing pointers works fine, but you open yourself up to exception safety problems by not guaranteeing RAII. Not a big deal in a lot of code, but worth considering.

---

Corinne (2022-10-20 13:03:12)

I enjoyed readingg your post