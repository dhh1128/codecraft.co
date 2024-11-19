---
title: Put Your Const Foot Forward
date: 2012-11-14
slug: put-your-const-foot-forward
redirect_from:
  - /2012/11/14/put-your-const-foot-forward
comments:
  - author: dougbert
    date: 2012-11-14 11:22:17
    comment: >
      I have to admit, I learned that (0 == i) trick myself in the past 18 months, but I adopted it myself AND it saved me from introducing several bugs within DAYS of coding it that way. I continue to do it now.
      
      Yeah, the old C "left, right" reading can be very helpful
      
      How this "trick"?  Better variable naming to help the reader of your code understand what you were trying to do!
      
      Instead of:  C   Use:  ConfigurationData
  - author: Daniel
    date: 2012-11-14 22:17:13
    comment: >
      The trick of choosing good names is so fundamental it deserves its own post. Have a look at <a href="good-code-is-named-right.md" title="Good Code Is Named Right" rel="nofollow">Good Code is Named Right</a>.
      
      (I can tell you've got battlescars; young engineers are often blind to the power of that particular habit. :-)
  - author: Julie
    date: 2012-11-26 14:25:09
    comment: >
      First, I would like to add a reference for how to use const. It provides a very good description of why to put const after the type. It is the original reference from Dan Saks that I based my style change on. http://www.dansaks.com/articles/1999-02%20const%20T%20vs%20T%20const.pdf
      
      As for assignment in a conditional, I used to recommend the constant on the left. However, I no longer do. Over time two things have changed my mind: 1) compilers issue warnings for use of an assignment in a conditional (which can be turned of by an extra set of parenthesis if that is what you really desire), and 2) It often makes the code harder to understand for a human reader. 
      
      More details about understanding a conditional -
      
      In many languages there are other operators which are similar to "==". In most of those cases changing the order of operands changes the meaning, or is invalid. This would be obvious for an ordering operation such as less than. "a < b" is not at all the same as "b < a". "a isa b" is not the same as "b isa a". And one that I use often in Python "a is None" is nonsensical as "None is a".
      
      I have definitely noticed that unseasoned C/C++ programmers often get confused when they see "if (0 == foo())". Instead of explaining the reasoning for that non-obvious operand order I explain that turning on compiler warnings is a good idea. :-)
  - author: Daniel
    date: 2012-11-26 21:03:12
    comment: >
      Julie: So glad you added a reference to the Dan Saks article. He explains it so much better than I could!
      
      The constant on the left is a tradeoff. I agree that it doesn't read as nicely, and that modern compilers are better at warning about the issue. However, I recently started working on some open source code, and there are members of the community for this particular codebase that are using pre-1990s C (not C++) compilers. I kid you not. So dialing up warnings is not always feasible. Where it is, I think I agree that the pendulum swings the other way.
  - author: How Sutter&#8217;s Wrong About const in C++ 11 &laquo; Codecraft
    date: 2013-01-02 08:50:24
    comment: >
      [...] community’s attention. I learned something important; I recommend that you watch the talk. Using const well is an essential skill. But I think in his enthusiasm about the way the language has evolved to make semantics clearer, [...]
  - author: Dan
    date: 2014-05-20 20:17:20
    comment: >
      Note that as long as the code still at least compiles under newer compilers, I'd argue that this isn't a valid justification for outdated or otherwise sub-optimal practices. If at least one member of the community encounters the warning, in principle the entire community is aware of the problem. A heterogeneous collection of compilers has access to the *union* of their respective warnings, not the intersection.
  - author: Daniel Hardman
    date: 2014-05-20 20:26:22
    comment: >
      @Dan: You make a fair point. Unfortunately, in the codebase I mentioned above, the community as a whole is in the habit of ignoring warnings; if it compiles, it must be good. Aargh!
      
      I wonder if your last sentence is a gem of wisdom that explains the power of open source in general. Good food for thought...
---
Here are two C++ style habits that I recommend. Neither is earth-shattering, but both have a benefit that I find useful. Both relate to the order in which constness shows up in your syntax.

1. When you write a conditional, consider putting the constant (unchangeable) value first:
<pre style="padding-left:30px;font-size:100%;margin-bottom:1em;">if (0 == i)</pre>
... instead of:
<pre style="padding-left:30px;font-size:100%;margin-bottom:1em;">if (i == 0)</pre>
The reason is simple. If you forget/mis-type and accidentally write a single <code>=</code> instead of two, making the expression into an assignment, you'll get a compile error, instead of subtle and difficult-to-find misbehavior. (Thanks to my friend Doug for reminding me about this one not long ago.)

<figure><img src="http://imgs.xkcd.com/comics/pointers.png" height="209" width="252" /><figcaption>Ah, the joys of pointers... Image credit: xkcd.</figcaption></figure>

2. With any data types that involve pointers, prefer putting the <code>const</code> keyword <em>after</em> the item that it modifies:
<pre style="padding-left:30px;font-size:100%;margin-bottom:1em;">char const * VERSION = "2.5";</pre>
... instead of:
<pre style="padding-left:30px;font-size:100%;margin-bottom:1em;">const char * VERSION = "2.5";</pre>
This rule is simple to follow, and it makes semantics about constness crystal clear. It lets you read data types backwards (from right to left) to get their semantics in plain English, which helps uncover careless errors. In either of the declarations of VERSION given above, the coder probably intends to create a constant, but that's not what his code says. The semantics of the two are identical, as far as a compiler is concerned, but the first variant makes the mistake obvious. Reading right-to-left, the data type of VERSION is "pointer to const char" -- so VERSION could be incremented or reassigned.

Use the right-to-left rule in reverse to solve the problem. If we want a "const pointer to const char", then we want:
<pre style="padding-left:30px;font-size:100%;margin-bottom:1em;">char const * const VERSION = "2.5";</pre>
<em>That</em> is a true string literal constant in C++. (Thanks to my friend <a title="Julie Jones: Learn voraciously." href="julie-jones-learn-voraciously.md">Julie</a> for teaching me this one.)

This might seem like nit-picky stuff, but if you ever get into const_iterator classes and <a class="zem_slink" title="Standard Template Library" href="http://en.wikipedia.org/wiki/Standard_Template_Library" target="_blank" rel="wikipedia">STL</a> containers, this particular habit helps you write or use templates with much greater comfort. It also helps if you have pointers to pointers and the like. (For consistency, I prefer to follow the same convention for reference variables as well. However, this is not especially important, since references are inherently immutable and therefore never bind to <code>const</code>.)
<p style="padding-left:30px;text-align:center;"><strong><span style="color:#000080;">Action Item</span></strong></p>
<p style="padding-left:30px;"><em><span style="color:#000080;">Share a tip of your own, or tell me why you prefer different conventions.</span></em></p>
